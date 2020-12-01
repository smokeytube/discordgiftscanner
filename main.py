#Coded completely by smokeytube
from selenium import webdriver
import time
from tkinter import *
import pyautogui


def click(image):
        start = pyautogui.locateOnScreen(image, confidence=0.01)
        print (image)
        pyautogui.moveTo(start)
        pyautogui.click()
        time.sleep(0.001)

def imageProcess(image):
        print ("imageProcess")
        return pyautogui.locateOnScreen(image, region=(400,400,200,600), confidence=0.8)

userw = input("Discord email: ")
passw = input("Discord password: ")

CHROME_DVR_DIR = '/webdrivers/chromedriver.exe'
driver = webdriver.Chrome(CHROME_DVR_DIR)

driver.get('https://discord.com/login?redirect_to=%2Fchannels%2F%40me')

usernameinput = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input')
passwordinput = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')
submitbutn = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')

usernameinput.send_keys(userw)
passwordinput.send_keys(passw)
submitbutn.click()

time.sleep(5)

# x = 15
# print ("You have 15 seconds to select the server and channel to scan")
# while x != 0:
#     print (x)
#     time.sleep(1)
#     x = x-1

accept = 'hello.png'

print ("Scan initiated")
while True:
    if imageProcess(accept):
        click(accept)
        print ("Gift claimed!")
        time.sleep(69420)
    else:
        print ("Could not locate. Trying again")
