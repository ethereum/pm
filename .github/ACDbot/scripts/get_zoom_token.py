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
import subprocess
import time

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
        
        # Test endpoint to verify the server is accessible
        if parsed_path.path == '/test':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f"Server is running and accessible at {self.redirect_uri}".encode())
            return
        
        # Extract the callback path from the redirect URI for comparison
        redirect_path = urllib.parse.urlparse(self.redirect_uri).path
        
        # Check if the path matches our redirect URI path
        if parsed_path.path == redirect_path:
            print(f"Received callback request to: {parsed_path.path}")
            if 'code' in query_params:
                self.authorization_code = query_params['code'][0]
                print(f"Authorization code received: {self.authorization_code[:5]}...")
                
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
                        <p>Error code: {token_response.get('error')}</p>
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
                
                error = "No authorization code was received"
                if 'error' in query_params:
                    error = f"Error: {query_params['error'][0]}"
                    if 'error_description' in query_params:
                        error += f" - {query_params['error_description'][0]}"
                
                error_html = f"""
                <html>
                <body>
                    <h1>Authorization Failed</h1>
                    <p>{error}</p>
                </body>
                </html>
                """
                self.wfile.write(error_html.encode())
        else:
            # Respond to any other requests
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f"404 Not Found. Expected path: {redirect_path}, got: {parsed_path.path}".encode())
    
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
            print(f"\nExchanging authorization code for tokens...")
            print(f"POST {token_url}")
            print(f"Headers: Authorization: Basic <credentials>")
            print(f"Data: {data}")
            
            response = requests.post(token_url, auth=auth, data=data)
            result = response.json()
            
            print(f"Response status: {response.status_code}")
            if response.status_code != 200:
                print(f"Error response: {result}")
                
                # Special handling for error 4700
                if result.get('error') == '4700' or '4700' in str(result):
                    print("\n[TROUBLESHOOTING HELP]")
                    print("Error 4700 typically indicates an issue with the OAuth redirect URL.")
                    print("Possible solutions:")
                    print("1. Verify the redirect URL in your Zoom app settings EXACTLY matches what's used here")
                    print(f"   - App redirect URL: The URL you added in the Zoom App Marketplace")
                    print(f"   - Used redirect URL: {self.redirect_uri}")
                    print("2. Make sure your ngrok tunnel is stable and accessible")
                    print("3. Try adding both HTTP and HTTPS versions of your redirect URL in the Zoom App settings")
                    print("4. Check if you're using a paid or free ngrok account - free accounts have limitations")
            
            return result
        except Exception as e:
            print(f"Exception during token exchange: {str(e)}")
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

def setup_ngrok(port):
    """Set up ngrok to create a secure tunnel to the local server"""
    try:
        # Check if ngrok is installed
        try:
            subprocess.run(["ngrok", "--version"], check=True, capture_output=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("ngrok not found. Please install ngrok first:")
            print("Visit https://ngrok.com/download or run:")
            print("  curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo \"deb https://ngrok-agent.s3.amazonaws.com buster main\" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok")
            return None
            
        # Start ngrok in a separate process
        ngrok_process = subprocess.Popen(
            ["ngrok", "http", str(port), "--log=stdout"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Wait for ngrok to start and extract the public URL
        print("Starting ngrok tunnel... (this may take a few seconds)")
        start_time = time.time()
        ngrok_url = None
        
        # Check the ngrok API to get the URL
        while time.time() - start_time < 10:  # Try for 10 seconds
            try:
                response = requests.get("http://localhost:4040/api/tunnels")
                if response.status_code == 200:
                    data = response.json()
                    tunnels = data.get("tunnels", [])
                    if tunnels:
                        for tunnel in tunnels:
                            if tunnel.get("proto") == "https":
                                ngrok_url = tunnel.get("public_url")
                                break
                if ngrok_url:
                    break
            except Exception:
                pass
            time.sleep(0.5)
            
        if not ngrok_url:
            print("Failed to get ngrok URL. Make sure ngrok is running correctly.")
            ngrok_process.terminate()
            return None
            
        print(f"ngrok tunnel established: {ngrok_url}")
        
        # Test if the ngrok URL is publicly accessible
        try:
            test_url = f"{ngrok_url}/test"
            print(f"Testing if ngrok URL is accessible: {test_url}")
            test_response = requests.get(test_url, timeout=5)
            if test_response.status_code == 200:
                print(f"✅ ngrok URL is accessible! Server response: {test_response.text}")
            else:
                print(f"⚠️ Warning: ngrok URL returned status code {test_response.status_code}")
        except Exception as e:
            print(f"⚠️ Warning: Could not verify ngrok URL accessibility: {str(e)}")
        
        return ngrok_url
        
    except Exception as e:
        print(f"Error setting up ngrok: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Get Zoom OAuth tokens")
    parser.add_argument("--client-id", required=True, help="Zoom OAuth Client ID")
    parser.add_argument("--client-secret", required=True, help="Zoom OAuth Client Secret")
    parser.add_argument("--redirect-uri", help="Redirect URI (must match one configured in your Zoom app)")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT,
                        help=f"Local server port (default: {DEFAULT_PORT})")
    parser.add_argument("--scopes", default="meeting:write meeting:read:admin recording:read:admin", 
                        help="Space-separated list of scopes")
    parser.add_argument("--use-ngrok", action="store_true", 
                        help="Use ngrok to create a secure HTTPS tunnel (recommended for production apps)")
    parser.add_argument("--ngrok-url", help="Use an existing ngrok URL instead of creating a new one")
    
    args = parser.parse_args()
    
    # Determine if we should use ngrok
    if args.ngrok_url:
        # Use the provided ngrok URL
        print(f"Using provided ngrok URL: {args.ngrok_url}")
        if not args.ngrok_url.endswith('/callback'):
            args.redirect_uri = f"{args.ngrok_url}/callback"
        else:
            args.redirect_uri = args.ngrok_url
        print(f"Redirect URI set to: {args.redirect_uri}")
        
        # Test if the ngrok URL is accessible
        try:
            test_url = f"{args.ngrok_url.rstrip('/callback')}/test"
            print(f"Testing if ngrok URL is accessible: {test_url}")
            test_response = requests.get(test_url, timeout=5)
            if test_response.status_code == 200:
                print(f"✅ ngrok URL is accessible! Response: {test_response.text}")
            else:
                print(f"⚠️ Warning: ngrok URL returned status code {test_response.status_code}")
        except Exception as e:
            print(f"⚠️ Warning: Could not verify ngrok URL accessibility: {str(e)}")
            
    elif args.use_ngrok:
        print("Setting up ngrok tunnel for HTTPS redirect...")
        ngrok_url = setup_ngrok(args.port)
        if not ngrok_url:
            print("Failed to establish ngrok tunnel. Exiting.")
            sys.exit(1)
        
        args.redirect_uri = f"{ngrok_url}/callback"
        print(f"Using ngrok URL as redirect URI: {args.redirect_uri}")
    elif not args.redirect_uri:
        # If not using ngrok and no redirect URI provided, use localhost
        args.redirect_uri = f"http://localhost:{args.port}/callback"
        print(f"Using default redirect URI: {args.redirect_uri}")
        print("NOTE: If you're using a production Zoom app, you may need to use HTTPS URLs.")
        print("      Consider using --use-ngrok if you get redirect errors.")
    
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