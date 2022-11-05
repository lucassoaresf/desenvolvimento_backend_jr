import json

import requests

url = "https://api.adviceslip.com/advice"

rq = requests.request("GET", url)
message = json.loads(rq.text)

for i in message.keys():
    print(message['slip']["advice"])

