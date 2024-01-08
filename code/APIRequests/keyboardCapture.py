from pynput.keyboard import Key, Listener
import threading
import queue
from functools import partial

class KeyboardListener:
    def __init__(self):
        self.keystrokes = queue.Queue()
        self.listener_thread = None

    def on_press(self, key):
        self.keystrokes.put(key)
        if key == Key.f10:  # Stop execution
            return False

    def on_release(self, key):
        pass

    def start_listener(self):
        def listen():
            with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
                listener.join()

        self.listener_thread = threading.Thread(target=listen)
        self.listener_thread.start()

    def stop_listener(self):
        if self.listener_thread:
            self.listener_thread.join()

    def get_queue(self):
        return self.keystrokes
    
    def getNextKey(self):
        return self.keystrokes.get()
    
if __name__ == "__main__": # Example of how to use this class
    # Create an instance of the class
    keyboard_listener = KeyboardListener()

    # Start the listener
    keyboard_listener.start_listener()

    # Main thread logic
    try:
        while True:
            key = keyboard_listener.getNextKey()
            if key == Key.f10:
                print("Exiting")
                break
            else:
                print(key)

    except KeyboardInterrupt:
        pass

    # Stop the listener thread
    keyboard_listener.stop_listener()
