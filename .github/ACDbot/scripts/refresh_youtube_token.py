from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import os
from google.auth.exceptions import RefreshError
import sys

creds = Credentials(
    token=None,
    refresh_token=os.environ["YOUTUBE_REFRESH_TOKEN"],
    client_id=os.environ["GOOGLE_CLIENT_ID"],
    client_secret=os.environ["GOOGLE_CLIENT_SECRET"],
    token_uri="https://oauth2.googleapis.com/token",
    scopes=["https://www.googleapis.com/auth/youtube.upload"]
)

try:
    request = Request()
    creds.refresh(request)
except RefreshError as e:
    print(f"Refresh failed: {str(e)}")
    print("::error::YouTube token refresh failed - manual reauth required")
    sys.exit(1) 