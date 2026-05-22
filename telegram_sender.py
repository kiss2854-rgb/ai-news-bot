import requests

BOT_TOKEN = "8891502281:AAGD2y3mjl9PHaAp6tnS-H-Ayvh_eQ_U8cg"
CHAT_ID = "5549780085"

def send_message(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=data)
