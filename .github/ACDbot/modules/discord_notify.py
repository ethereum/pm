import requests
import os

# Map call series to Discord webhook URLs via environment variables
CALL_SERIES_TO_WEBHOOK = {
    "acdc": os.environ.get("DISCORD_ACDC_WEBHOOK"),
    "acde": os.environ.get("DISCORD_ACDC_WEBHOOK"),
    "rollcall": os.environ.get("DISCORD_ROLLCALL_WEBHOOK"),
    # Add more as needed
}

def send_discord_notification(call_series, message):
    webhook_url = CALL_SERIES_TO_WEBHOOK.get(call_series.lower())
    if not webhook_url:
        print(f"No webhook configured for call series: {call_series}")
        return False
    data = {"content": message}
    response = requests.post(webhook_url, json=data)
    return response.status_code == 204 