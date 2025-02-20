from google_auth_oauthlib.flow import InstalledAppFlow
from urllib.parse import urlparse, parse_qs

# Same scopes as your production code
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

flow = InstalledAppFlow.from_client_secrets_file(
    "client_secrets.json",  # Download from Google Cloud Console
    scopes=SCOPES,
    redirect_uri="http://localhost:8080"  # Use localhost instead of OOB
)

# Generate authorization URL
auth_url, _ = flow.authorization_url(
    prompt="consent",
    access_type="offline"
)

print("Please open this URL in your browser manually:")
print(auth_url)
print("\nAfter authorization, copy the ENTIRE redirect URL from your browser's address bar (even if it shows connection refused):")

redirect_url = input("Paste redirect URL here: ").strip()

# Extract code from URL
parsed = urlparse(redirect_url)
code = parse_qs(parsed.query)['code'][0]

flow.fetch_token(code=code)

print(f"\nRefresh token: {flow.credentials.refresh_token}") 