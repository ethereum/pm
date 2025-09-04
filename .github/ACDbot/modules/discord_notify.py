import requests
import os

CALL_SERIES_TO_WEBHOOK = {
    "acdc": os.environ.get("DISCORD_ACD_WEBHOOK"),
    "acde": os.environ.get("DISCORD_ACD_WEBHOOK"),
    "acdt": os.environ.get("DISCORD_ACD_WEBHOOK"),
}

def send_discord_notification(call_series, message):
    webhook_url = CALL_SERIES_TO_WEBHOOK.get(call_series.lower())
    if not webhook_url:
        print(f"No webhook configured for call series: {call_series}")
        return False
    data = {"content": message}
    response = requests.post(webhook_url, json=data)
    return response.status_code == 204