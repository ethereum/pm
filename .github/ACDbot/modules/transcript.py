import os
import json
from modules import zoom, discourse, tg
import requests

MAPPING_FILE = ".github/ACDbot/meeting_topic_mapping.json"

def load_meeting_topic_mapping():
    if os.path.exists(MAPPING_FILE):
        with open(MAPPING_FILE, "r") as f:
            return json.load(f)
    return {}

def save_meeting_topic_mapping(mapping):
    with open(MAPPING_FILE, "w") as f:
        json.dump(mapping, f)

def post_zoom_transcript_to_discourse(meeting_id: str):
    """
    Posts the Zoom meeting recording link and summary to Discourse.
    """
    # Load the mapping to find the corresponding Discourse topic ID
    mapping = load_meeting_topic_mapping()
    entry = mapping.get(str(meeting_id))  # Ensure string key lookup
    if entry is None:
        raise ValueError(f"Meeting ID {meeting_id} not found in mapping for transcript processing")
    if not isinstance(entry, dict):
        # Convert legacy string format to dictionary for safe updates
        entry = {"discourse_topic_id": entry}
        mapping[str(meeting_id)] = entry
        meeting_topic = f"Meeting {meeting_id}"
    else:
        discourse_topic_id = entry.get("discourse_topic_id")
        meeting_topic = entry.get("issue_title", f"Meeting {meeting_id}")
    if not entry.get("discourse_topic_id"):
        raise ValueError(f"No Discourse topic mapping found for meeting ID {meeting_id}")
    discourse_topic_id = entry.get("discourse_topic_id")

    # Check existing posts
    if discourse.check_if_transcript_posted(discourse_topic_id, meeting_id):
        print(f"Transcript already posted for meeting {meeting_id}")
        return discourse_topic_id

    # Preemptively mark transcript as processed to avoid race conditions
    entry["transcript_processed"] = True
    save_meeting_topic_mapping(mapping)

    # Get recording details
    recording_data = zoom.get_meeting_recording(meeting_id)
    meeting_uuid = recording_data.get('uuid', '')
    
    # Get summary using properly encoded UUID
    summary_data = zoom.get_meeting_summary(meeting_uuid=meeting_uuid)
    print(f"Summary data for meeting {meeting_id}: {json.dumps(summary_data, indent=2)}")
    
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

    discourse.create_post(
        topic_id=discourse_topic_id,
        body=post_content
    )
    
    print(f"Posted recording links for meeting {meeting_id} to topic {discourse_topic_id}")

    # Now, send the same content to Telegram
    try:
        tg.send_message(post_content)
        print("Message sent to Telegram successfully.")
    except Exception as e:
        print(f"Error sending message to Telegram: {e}")
    
    return discourse_topic_id
