import os
import requests
from telegram.constants import ParseMode

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

def send_private_message(username: str, text: str, parse_mode=None):
    """
    Sends a private message to a Telegram user using their username.
    First gets the chat_id for the user, then sends the message.
    Returns True if successful, False otherwise.
    
    Parameters:
    - username: Telegram username (with or without @)
    - text: Message text to send
    - parse_mode: Optional. Mode for parsing entities ('MarkdownV2', 'HTML', or 'Markdown')
    """
    try:
        token = os.environ["TELEGRAM_BOT_TOKEN"]
        if not token:
            print(f"[ERROR] TELEGRAM_BOT_TOKEN environment variable is not set")
            return False
            
        # Clean username by removing @ prefix if present
        clean_username = username.lstrip('@')
        print(f"[DEBUG] Attempting to send message to Telegram user: @{clean_username}")
        
        # First try to get user chat ID via API
        # This requires the bot to have been started by the user already
        chat_id = None
        
        # First try getChat API method
        try:
            url = f"https://api.telegram.org/bot{token}/getChat"
            data = {"chat_id": f"@{clean_username}"}
            print(f"[DEBUG] Attempting to get chat info for @{clean_username}")
            
            resp = requests.post(url, data=data)
            if resp.status_code == 200 and resp.json().get("ok"):
                chat_data = resp.json()
                chat_id = chat_data["result"]["id"]
                print(f"[DEBUG] Successfully got chat_id ({chat_id}) for @{clean_username}")
            else:
                error_msg = resp.json().get("description", "Unknown error")
                print(f"[DEBUG] Failed to get chat info via getChat: {error_msg}")
        except Exception as e:
            print(f"[DEBUG] Error using getChat method: {str(e)}")
            
        # If getChat failed, try alternate method
        if not chat_id:
            try:
                # Try sending a direct message with username
                url = f"https://api.telegram.org/bot{token}/sendMessage"
                data = {
                    "chat_id": f"@{clean_username}",
                    "text": "Preparing to send you meeting details...",
                }
                
                print(f"[DEBUG] Attempting direct message to @{clean_username}")
                resp = requests.post(url, data=data)
                
                if resp.status_code == 200 and resp.json().get("ok"):
                    # If this works, get the chat_id from the response
                    result = resp.json().get("result", {})
                    chat_id = result.get("chat", {}).get("id")
                    print(f"[DEBUG] Direct message worked, got chat_id: {chat_id}")
                else:
                    error_msg = resp.json().get("description", "Unknown error")
                    print(f"[DEBUG] Failed to send direct message: {error_msg}")
            except Exception as e:
                print(f"[DEBUG] Error sending initial message: {str(e)}")
        
        # If we still don't have chat_id, we can't send messages
        if not chat_id:
            print(f"[ERROR] Failed to get chat_id for @{clean_username}. The user may need to start a chat with the bot first.")
            print(f"[INFO] Please ask the facilitator to message @{bot_username(token)} on Telegram first.")
            return False
            
        # Now send the actual message
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": text,
        }
        
        # Add parse_mode if specified
        if parse_mode:
            data["parse_mode"] = parse_mode
            print(f"[DEBUG] Using parse_mode: {parse_mode}")
            
        print(f"[DEBUG] Sending actual message to chat_id: {chat_id}")
        resp = requests.post(url, data=data)
        
        if resp.status_code != 200 or not resp.json().get("ok"):
            error_msg = resp.json().get("description", f"Status code: {resp.status_code}")
            print(f"[ERROR] Failed to send message: {error_msg}")
            return False
            
        print(f"[DEBUG] Successfully sent message to @{clean_username}")
        return True

    except Exception as e:
        print(f"[ERROR] Failed to send Telegram message to @{username}: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return False

def bot_username(token):
    """Get the bot's username to provide better instructions"""
    try:
        url = f"https://api.telegram.org/bot{token}/getMe"
        resp = requests.get(url)
        if resp.status_code == 200 and resp.json().get("ok"):
            return resp.json()["result"]["username"]
        return "your_bot"
    except:
        return "your_bot"
