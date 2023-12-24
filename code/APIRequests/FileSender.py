import requests as r

BASE_URL = 'http://localhost:8000/api/'
class FileSender:
    def __init__(self):
        self.APIKey = self.getAPIKey()
        
    def getAPIKey(self) -> str:
        response = r.get(BASE_URL + "APIKey")
    
        return response.json()['APIKey']
    
    def sendFile(self, filePAth: str) -> bool:
        with open(filePAth, 'rb') as file:
            """data = {
                    'fileData': f, 
                    'APIKey': self.APIKey, 
                    'fileName': filePAth.split('/')[-1]
                    }
            response = r.post(BASE_URL + "upload", data = data)"""
            
            files = {'file': file}
            response = r.post(BASE_URL + "upload", files=files, timeout=5)

            
            return response.json()['status']
        
f = FileSender()

f.sendFile(r'E:\replays\Hunt Showdown\Map\CB.png')