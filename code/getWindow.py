import pygetwindow as gw
import pyautogui

my = gw.getWindowsWithTitle("Hunt: Showdown")[0]

x, y, width, height = my.left, my.top, my.width, my.height

# Take the screenshot
screenshot = pyautogui.screenshot(region=(x, y, width, height))

# Save the screenshot
screenshot.save("screenshot.png")