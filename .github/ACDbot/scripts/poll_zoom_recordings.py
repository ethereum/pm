import os
import json
import argparse
from datetime import datetime, timedelta
import pytz
from modules import zoom, transcript, youtube_utils
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

    try:
        # For recurring meetings, we don't need to upload to YouTube
        if not entry.get("is_recurring"):
            # Process recording upload for non-recurring meetings
            if not entry.get("Youtube_upload_processed"):
                from modules.upload_zoom_recording import upload_recording
                upload_recording(meeting_id)

        # Process transcript regardless of meeting type
        discourse_topic_id = entry.get("discourse_topic_id")
        if discourse_topic_id:
            transcript.post_zoom_transcript_to_discourse(meeting_id)
            entry["transcript_processed"] = True
            save_meeting_topic_mapping(mapping)
            commit_mapping_file()

    except Exception as e:
        # Increment attempt counter on failure
        entry["upload_attempt_count"] = entry.get("upload_attempt_count", 0) + 1
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
