import os
import json
import argparse
from datetime import datetime, timedelta
import pytz
from modules import zoom, transcript
from github import Github, InputGitAuthor

MAPPING_FILE = "meeting_topic_mapping.json"

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
    Check if the meeting ended more than 4 hours ago.
    """
    now_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
    time_difference = now_utc - meeting_end_time
    return time_difference >= timedelta(hours=4)

def validate_meeting_id(meeting_id):
    return str(meeting_id).strip()

def main():
    parser = argparse.ArgumentParser(description="Poll Zoom for recordings and post transcripts.")
    parser.add_argument("--force_meeting_id", help="Force processing of a specific Zoom meeting ID")
    args = parser.parse_args()

    if args.force_meeting_id:
        meeting_id = validate_meeting_id(args.force_meeting_id)
        print(f"Force processing meeting {meeting_id}")
        try:
            # Get discourse_topic_id BEFORE processing
            mapping = load_meeting_topic_mapping()
            entry = mapping.get(meeting_id)
            discourse_topic_id = entry.get("discourse_topic_id") if isinstance(entry, dict) else entry
            
            if not discourse_topic_id:
                raise ValueError(f"No Discourse topic mapping found for meeting {meeting_id}")

            # Process transcript with verified ID
            transcript.post_zoom_transcript_to_discourse(meeting_id)
            
            # Update mapping with proper format
            mapping[meeting_id] = {
                "discourse_topic_id": discourse_topic_id,
                "issue_title": entry.get("issue_title", f"Meeting {meeting_id}"),
                "youtube_video_id": None
            }
            save_meeting_topic_mapping(mapping)
            commit_mapping_file()
            
        except Exception as e:
            print(f"Error processing meeting {meeting_id}: {e}")
        return

    # Load processed meetings from mapping file
    mapping = load_meeting_topic_mapping()
    processed_meetings = set(mapping.keys())

    # Fetch recordings from Zoom
    recordings = zoom.get_recordings_list()
    meetings_to_process = []

    for meeting in recordings:
        meeting_id = str(meeting.get("id"))
        end_time_str = meeting.get("end_time")
        if not meeting_id or not end_time_str:
            continue  # Skip if essential data is missing

        # Check if already processed (both formats)
        existing_entry = mapping.get(meeting_id)
        if existing_entry:
            # Handle dictionary format
            if isinstance(existing_entry, dict) and existing_entry.get("discourse_topic_id"):
                print(f"Meeting {meeting_id} has already been processed.")
                continue
            # Handle legacy string format
            elif isinstance(existing_entry, (int, str)):
                print(f"Meeting {meeting_id} has already been processed.")
                continue

        # Parse end time
        meeting_end_time = datetime.strptime(end_time_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=pytz.utc)
        if is_meeting_eligible(meeting_end_time):
            meetings_to_process.append((meeting_id, meeting.get("topic")))
        else:
            print(f"Meeting {meeting_id} is not yet eligible for processing.")

    if not meetings_to_process:
        print("No new meetings to process. Exiting.")
        return

    for meeting_id, topic in meetings_to_process:
        print(f"Processing meeting {meeting_id}: {topic}")
        try:
            # Get actual topic ID from successful transcript post
            topic_id = transcript.post_zoom_transcript_to_discourse(meeting_id)
            
            # Update mapping with new format
            mapping[meeting_id] = {
                "discourse_topic_id": topic_id,
                "issue_title": topic,
                "youtube_video_id": None
            }
        except Exception as e:
            print(f"Error processing meeting {meeting_id}: {e}")

    # Save and commit the updated mapping file
    save_meeting_topic_mapping(mapping)
    commit_mapping_file()

if __name__ == "__main__":
    main()
