from src import custom_privnote_api as privnote_api
from src import custom_discord_api as discord_api
import time
import os
from subprocess import Popen, CREATE_NEW_CONSOLE
import configparser

class CColor:
    Red = '\033[91m'
    Green = '\u001b[32m'
    Yellow = '\u001b[33m'
    Blue = '\u001b[34m'
    Cyan = '\u001b[36m'
    White = '\033[0m'


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


parser = configparser.ConfigParser()
parser.read('config.conf')
token = parser.get('discord', 'token')
user_id = input(f"{CColor.Yellow}[?]{CColor.White} What is your friend id ?\n>")
discord = discord_api.Discord(token, user_id)

Popen(f'python listener.py {token} {user_id}', creationflags=CREATE_NEW_CONSOLE)
while True :
    message = input("\r>")
    discord.send_message(privnote_api.upload_text(message))
