from KeyboardListner import KeyboardListener
from FileSender import FileSender
from ScreenShotUtils import takeHuntScreenshot, getScreenshotBytes

if __name__ == "__main__":
    fs = FileSender()
    
    kl = KeyboardListener().start_listener()
    
    print(f"""Welcome to the Hunt Showdown Screenshot Capturer.
          
This program will send screenshots of your Hunt Showdown games to the server.
This program will only capture screenshots of the hunt showdown game window.
It will not take pictures of any other window.

This program does moniter keyboard input, but it does not send any of your keyboard input to the server.
It only cares about single key presses of the {kl.screenshotKey} and {kl.exitKey} keys.

If you are worried about your privacy, you can look at the source code of this program.
https://github.com/Hunt-Bounty-Predictor

The server is located at server.oms.bio.
I run this server personally on my own hardware, so please don't abuse it.
If you have any questions, please contact me at 'omgitshappy' on discord

This program will run in the background and will send a screenshot when you press the {kl.screenshotKey} key.
You can exit the program by pressing the {kl.exitKey} key.""")
    
    
    try:
        while True:
            key = kl.getNextKey()
            try:
                if key == kl.getExitKey():
                    print("Exiting")
                    break
                elif key== kl.getScreenShotKey():
                    print("Taking screenshot")
                    fs.sendScreenshot(getScreenshotBytes(takeHuntScreenshot()))
                else:
                    pass
            except AttributeError:
                pass
                
    except KeyboardInterrupt:
        pass
    
    