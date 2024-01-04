import requests as r

from screenShotUtils import takeHuntScreenshot, getScreenshotBytes
import io

from pynput import keyboard
import pyautogui as pg
import pygetwindow as gw
import datetime

def getYesNo(prompt: str) -> bool:
    prompt = prompt + " (y/n): "
    while True:
        response = input(prompt)
        
        if response.lower() == 'y':
            return True
        elif response.lower() == 'n':
            return False
        else:
            print("Please enter y or n.")

BASE_URL = 'http://localhost:8000/api/'
class FileSender:
    def __init__(self):
        self.session = r.Session()
        self.getAPIKey()
        self.getUserInfo()
        
        
        
    def getAPIKey(self) -> str:
        response = r.get("http://localhost:8000/APIKey")
        #print(response.json())
        self.session.headers.update({"access_token": response.json()['APIKey']})
    
        #return response.json()['APIKey']
    
    def sendFile(self, filePAth: str) -> bool:
        with open(filePAth, 'rb') as file:
            
            files = {'file': file}
            response = self.session.post(BASE_URL + "upload", files=files, timeout=5)
            
            if response.status_code == 200:
                print("File uploaded successfully.")
                
            else:
                print("File upload failed.")
                
    def sendScreenshot(self, screenshot : io.BytesIO):
        files = {'file': screenshot}
        response = self.session.post(BASE_URL + "upload", files=files, timeout=5)
        
        if response.status_code == 200:
            print("File uploaded successfully.")
            
        else:
            print(response.json())
            print("File upload failed.")
        
    def getUserInfo(self):
        
        # Check if user has saved account, if so login.
        # Otherwise ask if they have created an account before, if they have prompt them for their username.
        # If they have not, prompt them to create an account.
        
        import json
        
        try:
            userInfo = json.load(open('userInfo.json'))
            
            name = userInfo['name']
            
            response = self.session.post(BASE_URL + "login", json={'username': name}, timeout=5)
            
            if response.status_code == 500:
                raise FileNotFoundError
            
            else :
                print("Login successfull.")
                
            
        except FileNotFoundError:
            response = getYesNo("Have you created an account before?")
            
            if response == False:
                while True:
                    name = input("Please enter a username: ")
                    
                    # Register user
                    
                    payload = {'username': name}
                    
                    response = self.session.post(BASE_URL + "register", json=payload, timeout=5)
                
                    print(response.json())
                    
                    if response.status_code == 200:
                        print("Registered successfully.")
                        break
                    
                    else:
                        print(response.json()['detail']['message'], "Please try again.")
                
            elif response == True:
                while True:
                    name = input("Please enter your username: ")
                    
                    payload = {'username': name}
                    
                    response = self.session.post(BASE_URL + "login", json=payload, timeout=5)
                    
                    if response.status_code == 200:
                        print("Login successfull.")
                        break
                    
                    else:
                        print(response.json()['detail']['message'], "Please try again.")
                    
                    #print("Invalid username. Please try again.")
                    
            json.dump({"name": name}, open('userInfo.json', 'w'))
                
        self.name = name
        
        self.session.headers.update({"Username": name})
            
                
        
f = FileSender()

import time

def on_press(key):
    if hasattr (key, 'vk') and key.vk == 97:
        f.sendScreenshot(getScreenshotBytes(takeHuntScreenshot()))
        print('screenshot taken')
        
    if key == keyboard.Key.f10:
        print("Exiting")
        exit()

if __name__ == "__main__":
    while True:
        with keyboard.Listener(
            on_press=on_press
        ) as listener:
            listener.join()
