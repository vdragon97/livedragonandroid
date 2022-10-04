import telegram
import requests
from telegram import ParseMode
from requests.structures import CaseInsensitiveDict

def send_test_message(inputMessage):
    try:
        telegram_notify = telegram.Bot("5481822840:AAE1vS9H6fZXsFfsRAKqYjbTGbS-l-gMUTk")
        #Shark Combat -1001705730750
        telegram_notify.send_message(chat_id="-1001705730750", text=inputMessage, parse_mode=ParseMode.HTML)
        #Deceitful Candle -1001400996369
        #telegram_notify.send_message(chat_id="-1001400996369", text=inputMessage, parse_mode=ParseMode.HTML)
        print("-----chatBotTelegram send sms to Deceitful Candle Channel successfully-----")
    except Exception as ex:
        print(ex)
        print("---------------------------chatBotTelegram error---------------------------")
        
def send_json_message(inputMessage):
    try:
        url = "https://api.telegram.org/bot5481822840:AAE1vS9H6fZXsFfsRAKqYjbTGbS-l-gMUTk/sendMessage?chat_id=-1001705730750"
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        resp = requests.post(url, headers=headers, json=inputMessage)
        print(resp.status_code)
    except Exception as ex:
        print(ex)
        print("---------------------------chatBotTelegram error---------------------------")
#send_test_message("Hello there!!!")