import os
import time
import tempfile
import requests
import argparse
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from modules import zoom, transcript, discourse, tg
from github import Github
from google.auth.transport.requests import Request
import json
import subprocess
from modules.zoom import (
    get_meeting_recording,
    get_access_token,
    get_meeting_summary
)
from google.oauth2 import service_account

# Import RSS utils
try:
    from modules import rss_utils
except ImportError:
    rss_utils = None

# Reuse existing zoom module functions
SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube.force-ssl",
    "https://www.googleapis.com/auth/youtube"
]
CLIENT_SECRETS_FILE = "client_secrets.json"

# Add these functions at the top of the file
MAPPING_FILE = ".github/ACDbot/meeting_topic_mapping.json"

def get_authenticated_service():
    # Initialize credentials from environment variables
    creds = Credentials(
        token=None,
        refresh_token=os.environ["YOUTUBE_REFRESH_TOKEN"],
        client_id=os.environ["GOOGLE_CLIENT_ID"],
        client_secret=os.environ["GOOGLE_CLIENT_SECRET"],
        token_uri="https://oauth2.googleapis.com/token",
        scopes=SCOPES
    )
    
    # Token already refreshed at workflow start
    return build("youtube", "v3", credentials=creds)

def video_exists(youtube, meeting_id):
    """Check if video for this meeting ID already exists in mapping"""
    mapping = load_meeting_topic_mapping()
    video_id = mapping.get(meeting_id, {}).get("youtube_video_id")
    if video_id is None or str(video_id).lower() in ("none", "null", ""):
        return False
    return True

def download_zoom_recording(meeting_id):
    """Download Zoom recording MP4 file to temp location"""
    try:
        recording_info = get_meeting_recording(meeting_id)
    except Exception as e:
        print(f"Error fetching meeting recording for meeting {meeting_id}: {e}")
        return None

    if not recording_info or 'recording_files' not in recording_info:
        return None

    for file in recording_info['recording_files']:
        if file.get('file_type') == 'MP4' and file.get('download_url'):
            download_url = file['download_url']
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
            
            headers = {
                "Authorization": f"Bearer {get_access_token()}",
                "Content-Type": "application/json"
            }
            
            response = requests.get(download_url, headers=headers, stream=True)
            if response.status_code == 200:
                for chunk in response.iter_content(chunk_size=1024*1024):
                    if chunk:
                        temp_file.write(chunk)
                temp_file.close()
                return temp_file.name
    return None

def upload_recording(meeting_id, occurrence_issue_number=None):
    """Uploads Zoom recording to YouTube for a specific occurrence."""

    # Ensure meeting_id is a string
    meeting_id = str(meeting_id)

    youtube = get_authenticated_service()
    mapping = load_meeting_topic_mapping()
    
    series_entry = mapping.get(meeting_id)

    if not series_entry:
        print(f"[ERROR] Meeting ID {meeting_id} not found in mapping.")
        return False # Indicate failure

    # Find the specific occurrence
    if occurrence_issue_number is None:
        # Try to find the most recent occurrence if not specified (best effort)
        if series_entry.get("occurrences"):
            matched_occurrence = series_entry["occurrences"][-1] # Assume last is latest
            occurrence_index = len(series_entry["occurrences"]) - 1
            occurrence_issue_number = matched_occurrence.get("issue_number", "[Unknown]")
            print(f"[WARN] occurrence_issue_number not provided, attempting upload for latest occurrence: Issue #{occurrence_issue_number}")
        else:
            print(f"[ERROR] No occurrences found for meeting {meeting_id} and occurrence_issue_number not specified.")
            return False
    else:
        matched_occurrence, occurrence_index = find_occurrence_by_issue_number(series_entry, occurrence_issue_number)

    if matched_occurrence is None:
        print(f"[ERROR] Occurrence with issue number {occurrence_issue_number} not found for meeting ID {meeting_id}.")
        return False # Indicate failure

    # --- Use occurrence-specific data --- 
    print(f"Processing YouTube upload for Meeting ID {meeting_id}, Occurrence Issue #{occurrence_issue_number}")

    # Check if this occurrence should skip YouTube upload
    if matched_occurrence.get("skip_youtube_upload", False):
        print(f"  -> Skipping: Occurrence marked as skip_youtube_upload.")
        # Mark as processed anyway so we don't retry?
        # mapping[meeting_id]["occurrences"][occurrence_index]["Youtube_upload_processed"] = True # Or leave as is?
        # save_meeting_topic_mapping(mapping) # No commit here, let poll script handle batch commit
        return True # Indicate already processed

    # Check attempt counter within the occurrence
    attempt_count = matched_occurrence.get("upload_attempt_count", 0)
    if attempt_count >= 10:
        print(f"  -> Skipping: Max upload attempts reached for occurrence.")
        return False # Indicate failure

    # Increment attempt count immediately
    mapping[meeting_id]["occurrences"][occurrence_index]["upload_attempt_count"] = attempt_count + 1
    save_meeting_topic_mapping(mapping) # Save attempt count increment

    # Only proceed if not already processed
    if matched_occurrence.get("Youtube_upload_processed"):
        print(f"  -> Skipping: YouTube upload already processed for occurrence.")
        return True # Indicate already processed

    video_title = matched_occurrence.get("issue_title", f"Meeting {meeting_id} - Issue {occurrence_issue_number}")
    video_description = (
        f"Recording of {video_title}\n\n"
        f"Original Zoom Meeting ID: {meeting_id}"
        f"\nGitHub Issue: https://github.com/{os.environ.get('GITHUB_REPOSITORY', '')}/issues/{occurrence_issue_number}" # Add link to specific issue
    )

    video_path = download_zoom_recording(meeting_id)
    if not video_path:
        print(f"No MP4 recording available for meeting {meeting_id}")
        return False # Indicate failure

    try:
        title = video_title
        description = video_description

        request_body = {
            'snippet': {
                'title': title,
                'description': description,
                'categoryId': '28'
            },
            'status': {
                'privacyStatus': 'public',
            }
        }

        media = googleapiclient.http.MediaFileUpload(video_path, chunksize=-1, resumable=True)
        response = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=media
        ).execute()

        # --- Update occurrence flags in mapping ---
        mapping[meeting_id]["occurrences"][occurrence_index]["youtube_video_id"] = response['id']
        mapping[meeting_id]["occurrences"][occurrence_index]["Youtube_upload_processed"] = True
        # Reset attempt count on success
        # mapping[meeting_id]["occurrences"][occurrence_index]["upload_attempt_count"] = 0 # Optional reset

        save_meeting_topic_mapping(mapping)
        commit_mapping_file()
        
        youtube_link = f"https://youtu.be/{response['id']}"
        print(f"Uploaded YouTube video: {youtube_link}")

        # Post to Discourse (if applicable)
        discourse_topic_id = matched_occurrence.get("discourse_topic_id")
        if discourse_topic_id:
            post_body = f"YouTube recording available: {youtube_link}"

            discourse.create_post(
                topic_id=discourse_topic_id,
                body=post_body # Use the simplified body
            )

        # --- Update RSS feed for this occurrence ---
        if rss_utils:
            try:
                rss_utils.add_notification_to_meeting(
                    meeting_id,
                    occurrence_issue_number, # Pass issue number to identify occurrence
                    "youtube_upload",
                    f"Meeting recording uploaded: {video_title}",
                    youtube_link
                )
                print(f"Updated RSS feed with YouTube video for occurrence #{occurrence_issue_number}")
            except Exception as e:
                print(f"Failed to update RSS feed: {e}")

        # Send Telegram notification similar to handle_issue
        try:
            # Find the specific occurrence to get the telegram message ID
            occurrence_telegram_message_id = matched_occurrence.get("telegram_message_id")

            telegram_message = (
                f"✅ YouTube Upload Successful!\n\n"
                f"Title: {video_title}\n"
                f"URL: {youtube_link}"
            )
            # Reply to the original occurrence announcement if possible
            if occurrence_telegram_message_id:
                tg.send_message(telegram_message, reply_to_message_id=occurrence_telegram_message_id)
            else:
                tg.send_message(telegram_message)
            print("Telegram notification sent for YouTube upload.")
        except Exception as e:
            print(f"Error sending Telegram message for YouTube upload: {e}")

        return True # Indicate success
    except HttpError as e:
        print(f"YouTube API error: {e}")
        return False # Indicate failure
    finally:
        os.unlink(video_path)  # Clean up temp file

def main():
    parser = argparse.ArgumentParser(description="Upload Zoom recording to YouTube")
    parser.add_argument("--meeting_id", required=False, help="Zoom meeting ID to process")
    parser.add_argument("--occurrence_issue_number", required=False, type=int, help="Issue number of the specific occurrence to upload (requires --meeting_id)")
    args = parser.parse_args()

    # Handle case where specific occurrence is provided
    if args.meeting_id and args.occurrence_issue_number:
        print(f"Attempting upload for specific occurrence: Meeting ID {args.meeting_id}, Issue #{args.occurrence_issue_number}")
        try:
            upload_recording(args.meeting_id, args.occurrence_issue_number)
        except Exception as e:
            print(f"Failed to process specific occurrence {args.meeting_id} / {args.occurrence_issue_number}: {e}")
        return # Exit after processing specific occurrence

    # Handle case where only meeting_id is provided (legacy or manual run?)
    if args.meeting_id and not args.occurrence_issue_number:
        print(f"[WARN] Only --meeting_id provided. Attempting upload for the LATEST occurrence of {args.meeting_id}.")
        try:
            upload_recording(args.meeting_id) # Will try latest occurrence by default
        except Exception as e:
            print(f"Failed to process latest occurrence for {args.meeting_id}: {e}")
        return

    # Handle case where NO arguments are provided (check mapping)
    if not args.meeting_id and not args.occurrence_issue_number:
        print("No meeting ID provided - checking last 5 meetings from mapping")
        mapping = load_meeting_topic_mapping()
        
        # Get last 5 meetings sorted by insertion order (Python 3.7+ preserves dict order)
        recent_meetings = list(mapping.items())[-5:]
        
        for meeting_id, details in recent_meetings:
            if not isinstance(details, dict):
                continue  # Skip legacy format entries
                
            # Iterate through occurrences within this meeting entry
            if "occurrences" in details:
                # Process occurrences in reverse (most recent first) for this check
                for occurrence in reversed(details["occurrences"]):
                    occ_issue_num = occurrence.get("issue_number")
                    yt_processed = occurrence.get("Youtube_upload_processed", False)
                    yt_skipped = occurrence.get("skip_youtube_upload", False)

                    # Process if not skipped and not already processed
                    if not yt_skipped and not yt_processed and occ_issue_num:
                        print(f"\nProcessing occurrence from mapping: Meeting ID {meeting_id}, Issue #{occ_issue_num}")
                        try:
                            upload_recording(meeting_id, occ_issue_num)
                            # Optionally break after processing one to avoid long runs?
                            # break
                        except Exception as e:
                            print(f"Failed to process {meeting_id} / {occ_issue_num}: {e}")
            # else: Handle non-recurring meetings if needed (legacy structure)
            elif not details.get("is_recurring", False):
                yt_processed = details.get("Youtube_upload_processed", False)
                yt_skipped = details.get("skip_youtube_upload", False)
                if not yt_skipped and not yt_processed:
                    print(f"\nProcessing non-recurring meeting from mapping: {meeting_id}")
                    try:
                        upload_recording(meeting_id) # Assumes it needs top-level processing
                    except Exception as e:
                        print(f"Failed to process {meeting_id}: {e}")

def load_meeting_topic_mapping():
    if os.path.exists(MAPPING_FILE):
        with open(MAPPING_FILE, "r") as f:
            return json.load(f)
    return {}

def save_meeting_topic_mapping(mapping):
    with open(MAPPING_FILE, "w") as f:
        json.dump(mapping, f, indent=2)

def commit_mapping_file():
    """Commit and push changes to the mapping file"""
    try:
        # Configure git user (required in CI)
        subprocess.run(
            ["git", "config", "--global", "user.email", "actions@github.com"],
            check=True
        )
        subprocess.run(
            ["git", "config", "--global", "user.name", "GitHub Actions"],
            check=True
        )
        
        # Commit and push
        subprocess.run(["git", "add", MAPPING_FILE], check=True)
        subprocess.run(
            ["git", "commit", "-m", f"Update YouTube video mapping"],
            check=True
        )
        subprocess.run(["git", "push"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to commit mapping file: {e}")

def find_occurrence_by_issue_number(series_entry, issue_number):
    """Helper function to find an occurrence by issue number."""
    if not series_entry or "occurrences" not in series_entry:
        return None, -1
    for index, occ in enumerate(series_entry["occurrences"]):
        if occ.get("issue_number") == issue_number:
            return occ, index
    return None, -1

if __name__ == "__main__":
    main()