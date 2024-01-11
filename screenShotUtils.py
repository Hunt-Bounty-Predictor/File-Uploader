import io
from pynput import keyboard
import pyautogui as pg
import pygetwindow as gw
import datetime

def takeHuntScreenshot():

    my = gw.getWindowsWithTitle("Hunt: Showdown")[0]

    x, y, width, height = my.left, my.top, my.width, my.height

    # Take the screenshot
    screenshot = pg.screenshot(region=(x, y, width, height))

    # Save the screenshot
    return screenshot

def getScreenshotBytes(screenshot):
    byteObj = io.BytesIO()
    screenshot.save(byteObj, format='JPEG')
    byteObj.seek(0)
    
    return byteObj