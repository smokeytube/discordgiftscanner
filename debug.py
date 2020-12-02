#Coded completely by smokeytube
import time
from tkinter import *
import pyautogui
from datetime import datetime




def click(image):
        start = pyautogui.locateOnScreen(image, confidence=0.01)
        pyautogui.moveTo(start)
        pyautogui.click()
        time.sleep(0.001)

def imageProcess(image):
        return pyautogui.locateOnScreen(image, region=(400,400,200,600), confidence=0.8)


# x = 15
# print ("You have 15 seconds to select the server and channel to scan")
# while x != 0:
#     print (x)
#     time.sleep(1)
#     x = x-1

accept = 'hello.png'
now = datetime.now()
x = 0

print ("Scan initiated")
while True:
    if imageProcess(accept):
        click(accept)
        print ("Gift claimed!")
        time.sleep(69420)
    else:
        current_time = now.strftime("%H%M%S")
        if int(current_time, 10) == int(current_time, 10) + 60:
            print ("Scanned " + x + "times in 1 minute (" + x/60 + " scan(s) per second.)")
            x = 0
        x = x + 1
        current_time2 = now.strftime("%H%M%S")

