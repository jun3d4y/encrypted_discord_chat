from src import custom_privnote_api as privnote_api
from src import custom_discord_api as discord_api
import time
import sys
import os

class CColor:
    Red = '\033[91m'
    Green = '\u001b[32m'
    Yellow = '\u001b[33m'
    Blue = '\u001b[34m'
    Cyan = '\u001b[36m'
    White = '\033[0m'
os.system('color')
discord = discord_api.Discord(sys.argv[1], sys.argv[2])

while True :
    messages = discord.get_messages()
    for message in messages :
        if "https://privnote.com/" in message :
                print(f'{CColor.Red}{privnote_api.retrieve_text(message)}{CColor.White}')
        elif message == "YOU" :
            print(f"{CColor.Green}YOU SENT A MESSAGE")
    time.sleep(1)
