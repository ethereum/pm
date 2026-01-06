import requests
import os

from .call_series_config import get_discord_webhook_mapping

# Load webhook env var names from config and resolve to actual URLs
_WEBHOOK_ENV_MAPPING = get_discord_webhook_mapping()


def _get_webhook_url(call_series: str) -> str | None:
    """Get the webhook URL for a call series by resolving the env var name."""
    env_var_name = _WEBHOOK_ENV_MAPPING.get(call_series.lower())
    if env_var_name:
        return os.environ.get(env_var_name)
    return None


def send_discord_notification(call_series, message):
    webhook_url = _get_webhook_url(call_series)
    if not webhook_url:
        print(f"No webhook configured for call series: {call_series}")
        return False
    data = {"content": message}
    response = requests.post(webhook_url, json=data)
    return response.status_code == 204