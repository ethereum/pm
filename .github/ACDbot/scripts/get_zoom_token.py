#!/usr/bin/env python3
"""
Zoom OAuth 2.0 Authorization Tool

This script helps set up the initial OAuth 2.0 tokens for a Zoom General (User Managed) app.
It will guide you through the process of:
1. Setting up a local HTTP server to receive the authorization code
2. Opening a browser to authorize your app
3. Exchanging the authorization code for access and refresh tokens

Usage:
  python get_zoom_token.py --client-id CLIENT_ID --client-secret CLIENT_SECRET --redirect-uri REDIRECT_URI
"""

import argparse
import webbrowser
import http.server
import socketserver
import urllib.parse
import requests
import json
import os
import sys
from urllib.parse import urlparse, parse_qs

# Default port for the local server
DEFAULT_PORT = 8000

class OAuthCallbackHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, *args, client_id=None, client_secret=None, redirect_uri=None, **kwargs):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.authorization_code = None
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        """Handle the callback from Zoom OAuth redirect"""
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        
        # Check if the path is the redirect URI path
        if parsed_path.path == urllib.parse.urlparse(self.redirect_uri).path:
            if 'code' in query_params:
                self.authorization_code = query_params['code'][0]
                
                # Exchange the code for tokens
                token_response = self.exchange_code_for_tokens(self.authorization_code)
                
                # Send success response to the browser
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                if token_response.get('error'):
                    response_html = f"""
                    <html>
                    <body>
                        <h1>Error</h1>
                        <p>{token_response.get('error_description', 'Unknown error')}</p>
                    </body>
                    </html>
                    """
                else:
                    response_html = """
                    <html>
                    <body>
                        <h1>Authorization Successful!</h1>
                        <p>You can close this window and return to the terminal.</p>
                    </body>
                    </html>
                    """
                
                self.wfile.write(response_html.encode())
                
                # Signal the server to shut down
                self.server.token_response = token_response
                self.server.should_shutdown = True
            else:
                # Handle error response
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                error_html = """
                <html>
                <body>
                    <h1>Authorization Failed</h1>
                    <p>No authorization code was received from Zoom.</p>
                </body>
                </html>
                """
                self.wfile.write(error_html.encode())
        else:
            # Respond to any other requests
            self.send_response(404)
            self.end_headers()
    
    def exchange_code_for_tokens(self, code):
        """Exchange the authorization code for access and refresh tokens"""
        token_url = "https://zoom.us/oauth/token"
        
        auth = (self.client_id, self.client_secret)
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_uri
        }
        
        try:
            response = requests.post(token_url, auth=auth, data=data)
            return response.json()
        except Exception as e:
            return {'error': 'request_failed', 'error_description': str(e)}
    
    def log_message(self, format, *args):
        """Suppress logging"""
        return

def create_oauth_handler(client_id, client_secret, redirect_uri):
    """Create a handler class with the OAuth credentials pre-configured"""
    def handler_factory(*args, **kwargs):
        return OAuthCallbackHandler(*args, client_id=client_id, client_secret=client_secret, 
                                 redirect_uri=redirect_uri, **kwargs)
    return handler_factory

def main():
    parser = argparse.ArgumentParser(description="Get Zoom OAuth tokens")
    parser.add_argument("--client-id", required=True, help="Zoom OAuth Client ID")
    parser.add_argument("--client-secret", required=True, help="Zoom OAuth Client Secret")
    parser.add_argument("--redirect-uri", required=True, 
                        help="Redirect URI (must match one configured in your Zoom app)")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT,
                        help=f"Local server port (default: {DEFAULT_PORT})")
    parser.add_argument("--scopes", default="meeting:write meeting:read:admin recording:read:admin", 
                        help="Space-separated list of scopes")
    
    args = parser.parse_args()
    
    # Validate redirect URI
    try:
        parsed_uri = urllib.parse.urlparse(args.redirect_uri)
        if parsed_uri.scheme not in ['http', 'https'] or not parsed_uri.netloc:
            print("Error: Invalid redirect URI. Must be a valid http:// or https:// URL")
            sys.exit(1)
        
        # Extract port from redirect URI if it's local
        if parsed_uri.netloc in ['localhost', '127.0.0.1']:
            if parsed_uri.port:
                args.port = parsed_uri.port
    except Exception as e:
        print(f"Error parsing redirect URI: {e}")
        sys.exit(1)
    
    # Set up the local server
    handler = create_oauth_handler(args.client_id, args.client_secret, args.redirect_uri)
    
    with socketserver.TCPServer(("", args.port), handler) as httpd:
        # Add attributes to the server
        httpd.token_response = None
        httpd.should_shutdown = False
        
        # Construct the authorization URL
        auth_params = {
            'response_type': 'code',
            'client_id': args.client_id,
            'redirect_uri': args.redirect_uri,
            'scope': args.scopes
        }
        auth_url = f"https://zoom.us/oauth/authorize?{urllib.parse.urlencode(auth_params)}"
        
        print(f"Starting server on port {args.port}...")
        print(f"Opening browser to authorize Zoom app access...")
        print(f"Authorization URL: {auth_url}")
        
        # Open the default web browser
        webbrowser.open(auth_url)
        
        # Handle one request at a time until should_shutdown is True
        while not getattr(httpd, 'should_shutdown', False):
            httpd.handle_request()
        
        # Print the token information
        token_response = httpd.token_response
        
        if token_response and 'refresh_token' in token_response:
            print("\n=== OAuth Authentication Successful ===")
            print(f"Access Token: {token_response['access_token']}")
            print(f"Refresh Token: {token_response['refresh_token']}")
            print(f"Token Type: {token_response.get('token_type', 'Bearer')}")
            print(f"Expires In: {token_response.get('expires_in', 'N/A')} seconds")
            
            # Save to environment file
            save = input("\nWould you like to save these tokens to a .env file? (y/n): ")
            if save.lower() == 'y':
                env_file = input("Enter filename (.env): ") or ".env"
                
                # Check if file exists and ask for confirmation to overwrite
                if os.path.exists(env_file):
                    confirm = input(f"{env_file} already exists. Overwrite? (y/n): ")
                    if confirm.lower() != 'y':
                        print("Not saving to file.")
                        return
                
                with open(env_file, 'w') as f:
                    f.write(f"ZOOM_CLIENT_ID={args.client_id}\n")
                    f.write(f"ZOOM_CLIENT_SECRET={args.client_secret}\n")
                    f.write(f"ZOOM_REFRESH_TOKEN={token_response['refresh_token']}\n")
                
                print(f"Tokens saved to {env_file}")
                print("\nIMPORTANT: Keep your refresh token secure! It provides access to your Zoom account.")
            
            print("\nTo use with GitHub Actions:")
            print("1. Go to your GitHub repository settings")
            print("2. Navigate to Secrets and Variables > Actions > New repository secret")
            print("3. Add the following secrets:")
            print(f"   - ZOOM_CLIENT_ID: {args.client_id}")
            print(f"   - ZOOM_CLIENT_SECRET: {args.client_secret}")
            print(f"   - ZOOM_REFRESH_TOKEN: {token_response['refresh_token']}")
        else:
            print("\n=== OAuth Authentication Failed ===")
            if token_response and 'error' in token_response:
                print(f"Error: {token_response.get('error')}")
                print(f"Description: {token_response.get('error_description', 'No description')}")
            else:
                print("Unknown error occurred.")

if __name__ == "__main__":
    main() 