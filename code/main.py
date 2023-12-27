from pynput import keyboard
import pyautogui as pg
import pygetwindow as gw
import datetime
        
BASEPATH = "E:/replays/Hunt Showdown/Map/Images"
FIRSTCLUE = '/First Clue/'
SECONDCLUE = '/Second Clue/'
THIRDCLUE = '/Third Clue/'
BOSS = '/Boss/'
NEXTTOBOSS = BOSS + '/Next to Boss/'
AWAYFROMBOSS = BOSS + '/Away from Boss/'
        
import os, re

last = {
    "First Clue": 0,
    "Second Clue": 0,
    "Third Clue": 0,
    "Next to Boss": 0,
    "Away from Boss": 0
}



for root, dirs, files in os.walk(BASEPATH):
    folder = re.search(r'[\w\s]*$', root).group()
    if folder in last:
        try:
            files = sorted(files, key=lambda x: int(x.split(".")[0]))
            lastFile = files[-1]
            
            num = int(lastFile.split(".")[0])
            
            last[folder] = num
        except IndexError:
            pass
        
last = max(list(last.values()))
print(last)

def takeHuntScreenshot(name: str):

    my = gw.getWindowsWithTitle("Hunt: Showdown")[0]

    x, y, width, height = my.left, my.top, my.width, my.height

    # Take the screenshot
    screenshot = pg.screenshot(region=(x, y, width, height))

    # Save the screenshot
    screenshot.save(name)
    
def getCurrTime():
    currentTime = datetime.datetime.now()
    
    return currentTime.strftime("%H:%M:%S")


    
    
screenshotsTaken = 0

def on_press(key):
    global last, screenshotsTaken
    if hasattr(key, 'vk') and 96 <= key.vk <= 105:
        if key.vk == 97:
            print("Starting Map")
            last += 1
            screenshotsTaken += 1
            #s = pg.screenshot()
            #s.save(BASEPATH + FIRSTCLUE + str(last) +".jpg")
            takeHuntScreenshot(BASEPATH + FIRSTCLUE + str(last) +".jpg")
            
            
        if key.vk == 98:
            print("First Clue")
            #s = pg.screenshot()
            #s.save(BASEPATH + SECONDCLUE + str(last) +".jpg")
            takeHuntScreenshot(BASEPATH + SECONDCLUE + str(last) +".jpg")

        if key.vk == 99:
            print("Second Clue")
            #s = pg.screenshot()
            #s.save(BASEPATH + THIRDCLUE + str(last) +".jpg")
            takeHuntScreenshot(BASEPATH + THIRDCLUE + str(last) +".jpg")
            
        if key.vk == 100:
            print("Extract next to boss")
            #s = pg.screenshot()
            #s.save(BASEPATH + NEXTTOBOSS + str(last) +".jpg")
            takeHuntScreenshot(BASEPATH + NEXTTOBOSS + str(last) +".jpg")
            
        if key.vk == 101:
            print("Extract away from boss")
            #s = pg.screenshot()
            #s.save(BASEPATH + AWAYFROMBOSS + str(num) +".jpg")
            takeHuntScreenshot(BASEPATH + AWAYFROMBOSS + str(last) +".jpg")
            
        if 96 < key.vk < 102:
            print(f"Screenshot taken at {getCurrTime()} for screenshot {screenshotsTaken}.")
            
    if key == keyboard.Key.f10:
        print("You took " + str(screenshotsTaken) + " screenshots")
        print("Exiting")
        exit()
        
with keyboard.Listener(
    on_press=on_press) as listener:
    listener.join()