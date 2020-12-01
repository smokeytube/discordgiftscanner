import pyautogui
import time

time.sleep(4)

iml = pyautogui.screenshot(region=(400,400,200,600))
iml.save(r"C:\Users\Zach\discordgiftscanner\tempr.png")
