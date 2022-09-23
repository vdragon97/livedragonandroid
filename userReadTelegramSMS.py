import requests
import json

def __loadLastMessage__():
    try:
        resp = requests.get("https://api.telegram.org/bot5362503047:AAEKZnPi4mf5lJKUs3emODA4wK4Sz-wrIDc/getUpdates?offset=-1")
    except Exception:
        print("An unexpected error occurred when receiving message")
    return json.loads(resp.text)["result"][0]["channel_post"]["text"]

if __name__=="__main__":
    contentMessage = __loadLastMessage__()
    print(contentMessage) 