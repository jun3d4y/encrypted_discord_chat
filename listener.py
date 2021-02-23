from src import custom_privnote_api as privnote_api
from src import custom_discord_api as discord_api
import socket
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
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 6666))


print(f"{CColor.Blue}[?]{CColor.White} This window is where messages will be printed")
while True :
    message = client.recv(9999).decode('utf-8')
    print(message)
