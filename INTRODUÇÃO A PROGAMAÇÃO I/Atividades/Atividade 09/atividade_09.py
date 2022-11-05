import json
import requests
from deep_translator import GoogleTranslator

url = "https://api.adviceslip.com/advice"

rq = requests.request("GET", url)
message = json.loads(rq.text)
text = message['slip']["advice"]

translate = GoogleTranslator(source='english', target='portuguese').translate(text)

print(f"Texto original: {text}")
print(f"Texto traduzido para português: {translate}")
