import requests
from telegram_pack import config


def send_message(text: str, channel_id: int):
    token = config.TOKEN
    url = "https://api.telegram.org/bot"
#    channel_id = -1001178910709
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })


def send_photo(text: str, link: str, channel_id: int):
    token = config.TOKEN
    url = "https://api.telegram.org/bot"
#    channel_id = -1001178910709
    url += token
    method = url + "/sendPhoto"

    files = {'photo': open(text, 'rb')}

    r = requests.post(method, files=files, data={
        "chat_id": channel_id,
        "caption": link
          })


def send_to_telegram(text):
    url = "https://api.telegram.org/bot1388568494:AAFZCASLFx64WZnpQLyqmBjht66Y3LU9xEI/sendMessage"

    payload = {
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False,
        "disable_notification": False,
        "chat_id": "-1001414238186"
    }
    headers = {
        "Accept": "application/json",
        "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
