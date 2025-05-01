import os
import json
from modules import zoom, discourse, tg
import requests

MAPPING_FILE = ".github/ACDbot/meeting_topic_mapping.json"

def load_meeting_topic_mapping():
    if os.path.exists(MAPPING_FILE):
        with open(MAPPING_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"::error::Failed to decode JSON from {MAPPING_FILE}. Returning empty mapping.")
                return {}
    return {}

def save_meeting_topic_mapping(mapping):
    with open(MAPPING_FILE, "w") as f:
        json.dump(mapping, f, indent=2)

def post_zoom_transcript_to_discourse(meeting_id: str, occurrence_details: dict = None):
    """
    Posts the Zoom meeting recording link and summary to Discourse.
    Uses occurrence_details if provided to find the correct Discourse topic ID.
    """
    # Load the mapping
    mapping = load_meeting_topic_mapping()
    discourse_topic_id = None
    meeting_topic = f"Meeting {meeting_id}" # Default title
    entry = mapping.get(str(meeting_id))

    if not entry or not isinstance(entry, dict):
        print(f"::error::Mapping entry for meeting ID {meeting_id} not found or invalid.")
        return False

    # Find the correct Discourse topic ID
    if occurrence_details and isinstance(occurrence_details, dict):
        # If occurrence details are provided, use the topic ID from there
        discourse_topic_id = occurrence_details.get("discourse_topic_id")
        meeting_topic = occurrence_details.get("issue_title", meeting_topic)
        print(f"[DEBUG] Using occurrence details. Topic ID: {discourse_topic_id}, Title: {meeting_topic}")
    else:
        # Fallback for non-recurring or older calls (legacy)
        discourse_topic_id = entry.get("discourse_topic_id")
        meeting_topic = entry.get("issue_title", meeting_topic)
        print(f"[DEBUG] Using top-level entry details. Topic ID: {discourse_topic_id}, Title: {meeting_topic}")

    if not discourse_topic_id or str(discourse_topic_id).startswith("placeholder"):
        print(f"::error::No valid Discourse topic ID found for meeting ID {meeting_id} (occurrence: {occurrence_details.get('issue_number', 'N/A') if occurrence_details else 'N/A'}). Provided ID: {discourse_topic_id}")
        return False # Indicate failure

    # Check existing posts in Discourse
    if discourse.check_if_transcript_posted(discourse_topic_id, meeting_id):
        print(f"Transcript already posted for meeting {meeting_id} in topic {discourse_topic_id}.")
        return True

    # Get recording details
    recording_data = zoom.get_meeting_recording(meeting_id)
    if not recording_data:
        print(f"::error::No recording data found for meeting ID {meeting_id} via Zoom API.")
        return False # Failed to get recording data

    meeting_uuid = recording_data.get('uuid', '')
    if not meeting_uuid:
        print(f"::error::Meeting UUID not found in recording data for meeting {meeting_id}.")
        return False

    # Get summary using properly encoded UUID
    try:
        summary_data = zoom.get_meeting_summary(meeting_uuid=meeting_uuid)
        print(f"Summary data for meeting {meeting_id}: {json.dumps(summary_data, indent=2)}")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"::warning::Meeting summary not found for {meeting_uuid} (Meeting ID: {meeting_id}). Might still be processing or unavailable. Status: {e.response.status_code}")
            summary_data = None # Proceed without summary
        else:
            print(f"::error::HTTP error fetching summary for {meeting_uuid}: {e}")
            return False
    except Exception as e:
        print(f"::error::Error fetching or parsing summary for {meeting_uuid}: {e}")
        return False # Failed to get summary

    # Process summary data
    summary_overview = ""
    summary_details = ""
    next_steps = ""
    
    if summary_data:
        # Extract summary overview
        summary_overview = summary_data.get("summary", "No summary overview available")
        
        # Extract detailed summaries in a collapsible section
        if summary_data.get("summary_details"):
            details = []
            for detail in summary_data.get("summary_details", []):
                section_title = detail.get("section_title", "")
                section_summary = detail.get("summary", "")
                if section_title and section_summary:
                    details.append(f"**{section_title}**\n{section_summary}")
                elif section_summary:
                    details.append(section_summary)
            
            if details:
                summary_details = "<details>\n<summary>Click to expand detailed summary</summary>\n\n"
                summary_details += "\n\n".join(details)
                summary_details += "\n</details>"
        
        # Format next steps
        if summary_data.get("next_steps"):
            steps = [f"- {step}" for step in summary_data["next_steps"]]
            next_steps = "### Next Steps:\n" + "\n".join(steps)
    else:
        summary_overview = "No summary available yet"
    
    # Extract proper share URL and passcode (new format)
    share_url = recording_data.get('share_url', '')
    passcode = recording_data.get('password', '')
    
    # Get transcript download URL from recording files
    transcript_url = None
    chat_url = None
    
    for file in recording_data.get('recording_files', []):
        if file.get('file_type') == 'TRANSCRIPT':
            transcript_url = file.get('download_url')
        elif file.get('file_type') == 'CHAT':
            chat_url = file.get('download_url')
    
    # Build post content with the new format
    post_content = f"""### Meeting Summary:
{summary_overview}

{summary_details}

{next_steps}

### Recording Access:
- [Join Recording Session]({share_url}) (Passcode: `{passcode}`)"""

    # Add transcript link if available
    if transcript_url:
        post_content += f"\n- [Download Transcript]({transcript_url})"
        
    # Add chat file link if available
    if chat_url:
        post_content += f"\n- [Download Chat]({chat_url})"

    try:
        discourse.create_post(
            topic_id=discourse_topic_id,
            body=post_content
        )
        print(f"Posted recording links for meeting {meeting_id} to topic {discourse_topic_id}")
    except Exception as e:
        print(f"::error::Failed to create Discourse post for topic {discourse_topic_id}: {e}")
        return False

    # Now, send the same content to Telegram
    try:
        tg.send_message(post_content)
        print("Message sent to Telegram successfully.")
    except Exception as e:
        print(f"Error sending message to Telegram: {e}")
    
    return True
