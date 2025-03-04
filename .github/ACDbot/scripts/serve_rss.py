#!/usr/bin/env python3
"""
Simple HTTP server to serve the RSS feed.
This can be used for testing or as a simple production server.
For production, consider using a proper web server like Nginx or Apache.
"""

import os
import sys
import http.server
import socketserver
import argparse
from modules import rss_utils
from modules.transcript import load_meeting_topic_mapping

# Default port
PORT = 8000

class RSSHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve the RSS feed"""
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/rss' or self.path == '/rss/':
            self.serve_rss()
        elif self.path == '/update' or self.path == '/update/':
            self.update_rss()
        else:
            # Serve static files
            super().do_GET()
    
    def serve_rss(self):
        """Serve the RSS feed"""
        try:
            # Ensure RSS file exists
            if not os.path.exists(rss_utils.RSS_FILE_PATH):
                mapping = load_meeting_topic_mapping()
                rss_utils.create_or_update_rss_feed(mapping)
            
            # Read the RSS file
            with open(rss_utils.RSS_FILE_PATH, 'rb') as f:
                content = f.read()
            
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/rss+xml')
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            self.send_error(500, f"Error serving RSS feed: {str(e)}")
    
    def update_rss(self):
        """Update the RSS feed"""
        try:
            mapping = load_meeting_topic_mapping()
            rss_utils.create_or_update_rss_feed(mapping)
            
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"RSS feed updated successfully")
        except Exception as e:
            self.send_error(500, f"Error updating RSS feed: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Serve the RSS feed")
    parser.add_argument("--port", type=int, default=PORT, help=f"Port to serve on (default: {PORT})")
    parser.add_argument("--update-only", action="store_true", help="Update the RSS feed and exit")
    args = parser.parse_args()
    
    # Change to the directory containing the RSS file
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    if args.update_only:
        try:
            mapping = load_meeting_topic_mapping()
            rss_file_path = rss_utils.create_or_update_rss_feed(mapping)
            print(f"RSS feed updated at {rss_file_path}")
            return
        except Exception as e:
            print(f"Error updating RSS feed: {e}")
            sys.exit(1)
    
    # Start the server
    with socketserver.TCPServer(("", args.port), RSSHandler) as httpd:
        print(f"Serving RSS feed at http://localhost:{args.port}/rss")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")

if __name__ == "__main__":
    main() 