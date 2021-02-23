from src import custom_privnote_api as privnote_api
from src import custom_discord_api as discord_api
from subprocess import Popen, CREATE_NEW_CONSOLE
import configparser
import threading
import socket
import time
import os

class CColor:
    Red = '\033[91m'
    Green = '\u001b[32m'
    Yellow = '\u001b[33m'
    Blue = '\u001b[34m'
    Cyan = '\u001b[36m'
    White = '\033[0m'

def receiver(client, discord) :
    while True :
        messages = discord.get_messages()
        for message in messages :
            to_send = None
            if "https://privnote.com/" in message :
                to_send = f'{CColor.Red}[ FRIEND ] {CColor.Green}SECURE{CColor.White} : {privnote_api.retrieve_text(message)}'
            elif message == "YOU" :
                to_send = f"{CColor.Green}[ YOU ]{CColor.White} YOU SENT A MESSAGE"
            else :
                to_send = f"{CColor.Red}[ FRIEND ] {CColor.Yellow}UNSECURE{CColor.White} : {message}"

            if to_send is not None :
                client.send(to_send.encode('utf-8'))
        time.sleep(1)



os.system('color')
print(f"""{CColor.Cyan}
          ////     ////////////*    /////
       ///.///////////////////////////// ///
     /////////////////////////////////////////
    ///////////////////////////////////////////
   .///////////////////////////////////////////,        {CColor.Red}DISCORD END TO END{CColor.Cyan}
   /////////////////////////////////////////////          {CColor.Red}ENCRYPTED CHAT{CColor.Cyan}
  ////////////       /////////      /////////////
  ///////////         ///////        ////////////   {CColor.Red}DEVELOPPED BY JuneDay#0001{CColor.Cyan}
 ////////////.        ///////        /////////////
 //////////////,    ///////////    ///////////////
 /////////////////////////////////////////////////
 //////////,  ///////////////////////.  //////////
   /////////////                   /////////////
        //////                      ,//////

        {CColor.White}""")


###Setting variables###
parser = configparser.ConfigParser()
parser.read('config.conf')
token = parser.get('discord', 'token')
user_id = input(f"{CColor.Yellow}[?]{CColor.White} What is your friend id ?\n>")
discord = discord_api.Discord(token, user_id)
commands = ("/u ", "/help", "/switch ")
help_message = """
/u [message]      :  Send a unsecure message
/help             :  Display this message
/switch [user id] :  Change interlocutor"""




socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('localhost', 6666))
Popen(f'python listener.py', creationflags=CREATE_NEW_CONSOLE)
socket.listen(5)
client, address = socket.accept()
threading.Thread(target=receiver, args=(client, discord, )).start()
print(f"{CColor.Blue}[?]{CColor.White} Receiver is connected, you can now send messages")
while True :
    message = input("\r>")
    if message.startswith(commands) :
        if message.startswith("/u ") :
            discord.send_message(message.replace("/u ", ""))
        elif message.startswith("/help") :
            print(help_message)
        elif message.startswith("/switch ") :
            discord.user_id = message.replace("/switch ", "")
            discord.open_dm()
            discord.get_messages()
            print(f"{CColor.Blue}[?]{CColor.White} You are now speaking to {discord.user_id}")
    else :
        discord.send_message(privnote_api.upload_text(message))
