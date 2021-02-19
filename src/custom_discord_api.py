import requests
import random
import string
import json

class CColor:
    Red = '\033[91m'
    Green = '\u001b[32m'
    Yellow = '\u001b[33m'
    Blue = '\u001b[34m'
    Cyan = '\u001b[36m'
    White = '\033[0m'

class Discord :

    def __init__(self, token, user_id) :

        self.message_read = set()
        self.user_id = user_id
        self.token = token

        self.headers = {
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMC4zMDkiLCJvc192ZXJzaW9uIjoiMTAuMC4xODM2MyIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoiZnIiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo3NzE5MiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
            "Authorization": self.token,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36"
        }

        if self.connect() :
            print(f"{CColor.Green}[+]{CColor.White} Hello {self.user_name}, you are connected !")
        else :
            raise Exception("Something is wrong with your token")

        self.open_dm()
        self.get_messages()

    def connect(self) :
        response = json.loads(requests.get(f'https://discord.com/api/v8/users/@me', headers=self.headers).text)
        if "username" in response :
            self.user_name = response["username"]
            return True
        else :
            return False

    def open_dm(self) :

        custom_hearder = self.headers
        custom_hearder["Content-Type"] = "application/json"

        data = {
            "recipients":[self.user_id]
        }
        response = json.loads(requests.post('https://discord.com/api/v8/users/@me/channels', headers=self.headers, data=json.dumps(data)).text)
        if "id" in response :
            self.discution_id = response["id"]
        else :
            raise Exception("Error, wrong user id.")

    def get_messages(self) :

        message_unread = set()
        response = json.loads(requests.get(f'https://discord.com/api/v8/channels/{self.discution_id}/messages?limit=50', headers=self.headers).text)

        if "message" in response :
            raise Exception("Error, ivalid channel id")

        for element in response :
            if element["author"]["username"] != self.user_name :
                if element["id"] not in self.message_read :
                    self.message_read.add(element["id"])
                    message_unread.add(element["content"])
            else :
                if element["id"] not in self.message_read :
                    message_unread.add("YOU")
                    self.message_read.add(element["id"])

        return message_unread

    def send_message(self, message) :

        custom_hearder = self.headers
        custom_hearder["Content-Type"] = "application/json"

        data = {
            "content": message,
            "nonce":self.get_nonce(),
            "tts":False
        }

        r = requests.post(f'https://discord.com/api/v8/channels/{self.discution_id}/messages', headers=custom_hearder, data=json.dumps(data))

    def get_nonce(self) :
        pool=string.ascii_lowercase+string.digits
        return "".join(random.choice(pool) for i in range(10))
