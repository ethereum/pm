import os
import requests
from telegram import ParseMode

ZOOM_CLIENT_ID = os.environ.get("ZOOM_CLIENT_ID")
ZOOM_CLIENT_SECRET = os.environ.get("ZOOM_CLIENT_SECRET")
ZOOM_ACCOUNT_ID = os.environ.get("ZOOM_ACCOUNT_ID")

DISCOURSE_API_KEY = os.environ.get("DISCOURSE_API_KEY")
DISCOURSE_API_USERNAME = os.environ.get("DISCOURSE_API_USERNAME")
DISCOURSE_BASE_URL = os.environ.get("DISCOURSE_BASE_URL")


def send_message(text: str):
    """
    Sends a message to a Telegram channel or group.
    Returns the message ID for future updates.
    """
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }

    resp = requests.post(url, data=data)
    resp.raise_for_status()
    return resp.json()["result"]["message_id"]

def update_message(message_id: int, text: str):
    """
    Updates an existing message in the Telegram channel or group.
    Returns True if successful, False if message not found.
    """
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    url = f"https://api.telegram.org/bot{token}/editMessageText"
    data = {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": text,
        "parse_mode": "HTML"
    }

    try:
        resp = requests.post(url, data=data)
        resp.raise_for_status()
        return True
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 400 and "message to edit not found" in e.response.text.lower():
            return False
        raise
