import requests as r

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
        print(response.json())
        self.session.headers.update({"access_token": response.json()['APIKey']})
    
        #return response.json()['APIKey']
    
    def sendFile(self, filePAth: str) -> bool:
        with open(filePAth, 'rb') as file:
            
            files = {'file': file}
            response = self.session.post(BASE_URL + "upload", files=files, timeout=5)

            
            return response.json()['status']
        
    def getUserInfo(self):
        
        # Check if user has saved account, if so login.
        # Otherwise ask if they have created an account before, if they have prompt them for their username.
        # If they have not, prompt them to create an account.
        
        import json
        
        try:
            userInfo = json.load(open('userInfo.json'))
            
            name = userInfo['name']
            
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
                        print(response.json()['detail']['message'])
                
            elif response == True:
                while True:
                    name = input("Please enter your username: ")
                    
                    payload = {'username': name}
                    
                    response = self.session.post(BASE_URL + "login", json=payload, timeout=5)
                    
                    if response.status_code == 200:
                        print("Login successfull.")
                        break
                    
                    else:
                        print(response.json()['detail']['message'])
                    
                    #print("Invalid username. Please try again.")
                
        self.name = name
            
                
        
f = FileSender()

#f.sendFile(r'E:\replays\Hunt Showdown\Map\CB.png')