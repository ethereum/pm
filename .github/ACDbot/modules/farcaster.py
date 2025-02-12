import os
import requests

def get_farcaster_client():
    """Initialize Farcaster client with credentials"""
    return {
        "api_url": os.environ.get("FARCASTER_API_URL", "https://api.farcaster.xyz/v2"),
        "access_token": os.environ["FARCASTER_ACCESS_TOKEN"]
    }

def create_cast(text: str, parent_url: str = None):
    """Post a new cast to Farcaster"""
    client = get_farcaster_client()
    headers = {
        "Authorization": f"Bearer {client['access_token']}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "text": text,
        "embeds": [{"url": parent_url}] if parent_url else []
    }
    
    try:
        response = requests.post(
            f"{client['api_url']}/casts",
            json=payload,
            headers=headers
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error creating Farcaster cast: {str(e)}")
        return None 