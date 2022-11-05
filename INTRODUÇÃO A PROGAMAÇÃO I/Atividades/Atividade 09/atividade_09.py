import json
import requests
from deep_translator import GoogleTranslator
from loguru import logger


def chamar_api():
    url = "https://api.adviceslip.com/advice"

    rq = requests.request("GET", url)
    message = json.loads(rq.text)
    text = message['slip']["advice"]

    translate = GoogleTranslator(source='english', target='portuguese').translate(text)

    print(f"Texto original: {text}")
    print(f"Texto traduzido para português: {translate}")

    return text, translate
def salver_traducao(texto, texto_traduzido):

    try:
        with open("frases_traduzidas.txt", 'a', encoding='utf-8') as f:
            t = texto_traduzido + "; " + texto + "\n"
            f.write(t)

    except Exception as error:
        logger.exception(error)

for i in range(30):
    x, y = chamar_api()

    salver_traducao(x, y)