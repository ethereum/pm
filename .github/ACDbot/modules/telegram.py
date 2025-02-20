import os
import requests

ZOOM_CLIENT_ID = os.environ.get("ZOOM_CLIENT_ID")
ZOOM_CLIENT_SECRET = os.environ.get("ZOOM_CLIENT_SECRET")
ZOOM_ACCOUNT_ID = os.environ.get("ZOOM_ACCOUNT_ID")

DISCOURSE_API_KEY = os.environ.get("DISCOURSE_API_KEY")
DISCOURSE_API_USERNAME = os.environ.get("DISCOURSE_API_USERNAME")
DISCOURSE_BASE_URL = os.environ.get("DISCOURSE_BASE_URL")


def send_message(text: str):
    """
    Sends a message to a Telegram channel or group.
    """
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
    }

    resp = requests.post(url, data=data)
    resp.raise_for_status()

    return resp.json()
