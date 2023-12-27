import os
import webbrowser
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Scopes define the level of access you are requesting from the user.
SCOPES = ['https://www.googleapis.com/auth/userinfo.profile']

def login():
    creds = None

    # The file token.json stores the user's access and refresh tokens.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                r'E:\replays\Hunt Showdown\Map\testing\code\credentials.json', SCOPES)  # credentials.json is downloaded from Google Cloud Console
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def getUserInfo(creds):
    service = build('oauth2', 'v2', credentials=creds)

    # Fetch the user info
    userInfo = service.userinfo().get().execute()
    return userInfo

print(getUserInfo(login()))