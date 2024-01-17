# Hunt Showdown Bounty Predictor (BP)

### Welcome to the Hunt Showdown Screenshot Capturer.
          
This program will send screenshots of your Hunt Showdown games to the server.
This program will only capture screenshots of the hunt showdown game window.
**It will not take pictures of any other window.**

The related code for taking screenshots is located in [screenShotUtils.py](screenShotUtils.py)

This program does moniter keyboard input, but it does not send any of your keyboard input to the server.
It only cares about single key presses of the 'f10' and 'f11' keys.

If you are worried about your privacy, the related files for keyboard capture is located in [KeyboardListner](KeyboardListner.py)

The server is located at server.oms.bio.
I run this server personally on my own hardware, so please don't abuse it.
The code for this server is hosted at [API-Server](https://github.com/Hunt-Bounty-Predictor/API-Server)
If you have any questions, please contact me at 'omgitshappy' on discord.

This program will run in the background and will send a screenshot when you press the 'f10' key.
You can exit the program by pressing the 'f11' key.

# Installation
Please nagvigate to the most [recent](https://github.com/Hunt-Bounty-Predictor/File-Uploader/releases) release in the [releases](https://github.com/Hunt-Bounty-Predictor/File-Uploader) tab and download the executable (.exe)

Once downloaded you just need to run the program and it will guide you from there.

# Developers
Pull the code down from the repo. You will need to pull down the code from the API server and run it locally. This enables you to test against a server that you have control of. In the future a development server may be avaliable.

When you create your API server you must add a .env file that changes the API endpoint to your local server.