from KeyboardListner import KeyboardListener
from FileSender import FileSender
from screenShotUtils import takeHuntScreenshot, getScreenshotBytes
from pynput.keyboard import Key

if __name__ == "__main__":
    fs = FileSender()
    
    kl = KeyboardListener().start_listener()
    
    try:
        while True:
            key = kl.getNextKey()
            try:
                if key == Key.f10:
                    print("Exiting")
                    break
                elif key.vk == 97:
                    fs.sendScreenshot(getScreenshotBytes(takeHuntScreenshot()))
                    print('screenshot taken')
                else:
                    pass
            except AttributeError:
                pass
                
    except KeyboardInterrupt:
        pass
    
    