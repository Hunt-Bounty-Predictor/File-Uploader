from pynput.keyboard import Key, Listener
import threading
import queue
from functools import partial

class KeyboardListener:
    def __init__(self, stopKey=Key.f10):
        self.keystrokes = queue.Queue()
        self.listener_thread = None
        self.screenshotKey = self.selectKey("Please select the key you would like to use to take a screenshot.")
        self.exitKey = self.selectKey("Please select the key you would like to use to exit the program.")

    def captureKeyInput(self) -> Key:
        selectedKey = None

        def on_press(key):
            nonlocal selectedKey
            selectedKey = key
            return False
        
        with Listener(
            on_press=on_press, suppress=True) as listener:
            
            listener.join()

        return selectedKey
    
    def selectKey(self, prompt: str) -> Key:
        while True:
            print(prompt)

            key = self.captureKeyInput()

            response = input(f"You selected: {key}, is this correct? (y/n)")

            if response.lower().strip() == "y" or response.strip() == "":
                return key

            print("Please try again.\n")

    def on_press(self, key):
        pass

    def on_release(self, key):
        self.keystrokes.put(key)
        if key == self.exitKey:  # Stop execution
            return False

    def start_listener(self):
        def listen():
            with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
                listener.join()

        self.listener_thread = threading.Thread(target=listen)
        self.listener_thread.start()
        
        return self

    def stop_listener(self):
        if self.listener_thread:
            self.listener_thread.join()

    def get_queue(self):
        return self.keystrokes
    
    def getNextKey(self):
        return self.get_queue().get()
    
    def getScreenShotKey(self):
        return self.screenshotKey
    
    def getExitKey(self):
        return self.exitKey
    
if __name__ == "__main__": # Example of how to use this class
    # Create an instance of the class
    keyboard_listener = KeyboardListener()

    # Start the listener
    keyboard_listener.start_listener()

    # Main thread logic
    try:
        while True:
            key = keyboard_listener.getNextKey()
            if key == keyboard_listener.exitKey:
                print("Exiting")
                break
            else:
                print(key)

    except KeyboardInterrupt:
        pass

    # Stop the listener thread
    keyboard_listener.stop_listener()
