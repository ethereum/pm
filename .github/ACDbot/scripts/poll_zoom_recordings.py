import os
import json
import argparse
from datetime import datetime, timedelta
import pytz
from modules import zoom, transcript, youtube_utils, rss_utils
from github import Github, InputGitAuthor

MAPPING_FILE = ".github/ACDbot/meeting_topic_mapping.json"

def load_meeting_topic_mapping():
    if os.path.exists(MAPPING_FILE):
        with open(MAPPING_FILE, "r") as f:
            return json.load(f)
    return {}

def save_meeting_topic_mapping(mapping):
    with open(MAPPING_FILE, "w") as f:
        json.dump(mapping, f, indent=2)

def commit_mapping_file():
    commit_message = "Update meeting-topic mapping"
    branch = os.environ.get("GITHUB_REF_NAME", "main")
    token = os.environ["GITHUB_TOKEN"]
    repo_name = os.environ["GITHUB_REPOSITORY"]
    g = Github(token)
    repo = g.get_repo(repo_name)
    author = InputGitAuthor(
        name="GitHub Actions Bot",
        email="actions@github.com"
    )
    file_path = MAPPING_FILE
    with open(file_path, "r") as f:
        file_content = f.read()
    try:
        contents = repo.get_contents(file_path, ref=branch)
        repo.update_file(
            path=contents.path,
            message=commit_message,
            content=file_content,
            sha=contents.sha,
            branch=branch,
            author=author,
        )
        print(f"Updated {file_path} in the repository.")
    except Exception:
        repo.create_file(
            path=file_path,
            message=commit_message,
            content=file_content,
            branch=branch,
            author=author,
        )
        print(f"Created {file_path} in the repository.")

def is_meeting_eligible(meeting_end_time):
    """
    Check if the meeting ended more than 30 minutes ago.
    """
    now_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
    return now_utc - meeting_end_time >= timedelta(minutes=30)

def validate_meeting_id(meeting_id):
    return str(meeting_id).strip()

def process_meeting(meeting_id, mapping):
    """Process a single meeting's recordings and transcripts"""
    entry = mapping.get(meeting_id)
    if not isinstance(entry, dict):
        print(f"Skipping meeting {meeting_id} - invalid mapping entry")
        return

    # Skip if already processed
    if entry.get("transcript_processed"):
        print(f"Meeting {meeting_id} is already processed")
        return

    # Skip if max attempts reached
    if entry.get("upload_attempt_count", 0) >= 10:
        print(f"Skipping meeting {meeting_id} - max upload attempts reached")
        return
        
    # Skip if meeting hasn't occurred yet
    start_time = entry.get("start_time")
    if start_time:
        try:
            from datetime import datetime
            import pytz
            meeting_time = datetime.fromisoformat(start_time.replace('Z', '+00:00'))
            now = datetime.now(pytz.UTC)
            
            if meeting_time > now:
                print(f"Skipping meeting {meeting_id} - scheduled for future ({start_time})")
                return
                
            # Also skip if meeting ended less than 30 minutes ago
            duration = entry.get("duration", 60)  # Default to 60 minutes if duration not specified
            meeting_end_time = meeting_time + timedelta(minutes=duration)
            
            if now < meeting_end_time + timedelta(minutes=30):
                print(f"Skipping meeting {meeting_id} - ended less than 30 minutes ago")
                return
                
        except Exception as e:
            print(f"Error parsing meeting time {start_time}: {e}")
            # Continue processing if we can't parse the time

    try:
        # For recurring meetings, we don't need to upload to YouTube
        is_recurring = entry.get("is_recurring", False)
        if is_recurring:
            print(f"Skipping YouTube upload for recurring meeting {meeting_id}")
            # Mark as processed to avoid future attempts
            entry["skip_youtube_upload"] = True
            entry["Youtube_upload_processed"] = True
            save_meeting_topic_mapping(mapping)
            commit_mapping_file()
        # Only attempt upload for non-recurring meetings that haven't been processed
        elif not entry.get("Youtube_upload_processed") and not entry.get("skip_youtube_upload", False):
            # Import directly from package path rather than relative path
            import sys
            import os
            script_dir = os.path.dirname(os.path.abspath(__file__))
            sys.path.append(os.path.dirname(script_dir))
            from scripts.upload_zoom_recording import upload_recording
            upload_recording(meeting_id)

        # Process transcript regardless of meeting type
        discourse_topic_id = entry.get("discourse_topic_id")
        if discourse_topic_id:
            transcript.post_zoom_transcript_to_discourse(meeting_id)
            entry["transcript_processed"] = True
            save_meeting_topic_mapping(mapping)
            commit_mapping_file()
            
            # Update RSS feed with transcript info
            try:
                rss_utils.add_notification_to_meeting(
                    meeting_id,
                    "transcript_posted",
                    "Meeting transcript posted to Discourse",
                    f"{os.environ.get('DISCOURSE_BASE_URL', 'https://ethereum-magicians.org')}/t/{discourse_topic_id}"
                )
                print(f"Updated RSS feed with transcript info for meeting {meeting_id}")
            except Exception as e:
                print(f"Failed to update RSS feed: {e}")

    except Exception as e:
        # Increment attempt counter on failure
        entry["transcript_attempt_count"] = entry.get("transcript_attempt_count", 0) + 1
        save_meeting_topic_mapping(mapping)
        commit_mapping_file()
        print(f"Error processing meeting {meeting_id}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Poll Zoom for recordings and post transcripts.")
    parser.add_argument("--force_meeting_id", required=False, help="Force processing of a specific Zoom meeting ID")
    args = parser.parse_args()

    if args.force_meeting_id:
        meeting_id = validate_meeting_id(args.force_meeting_id)
        if meeting_id:
            print(f"Force processing meeting {meeting_id}")
            mapping = load_meeting_topic_mapping()
            process_meeting(meeting_id, mapping)
            return
        else:
            print("Invalid force_meeting_id provided")
            return

    # Process last 5 meetings from mapping
    print("Checking last 5 meetings from mapping")
    mapping = load_meeting_topic_mapping()
    processed_count = 0
    
    # Process newest meetings first
    for meeting_id, entry in reversed(list(mapping.items())[-5:]):
        if not isinstance(entry, dict):
            continue
            
        process_meeting(meeting_id, mapping)
        processed_count += 1

    if processed_count == 0:
        print("No recent unprocessed meetings found")
        # Check for new recordings
        recordings = zoom.get_recordings_list()
        
        for recording in recordings:
            meeting_id = str(recording.get("id"))
            if not meeting_id:
                continue

            # Skip if already fully processed
            entry = mapping.get(meeting_id, {})
            if isinstance(entry, dict):
                if entry.get("transcript_processed") and (entry.get("Youtube_upload_processed") or entry.get("is_recurring")):
                    continue

            process_meeting(meeting_id, mapping)

if __name__ == "__main__":
    main()
