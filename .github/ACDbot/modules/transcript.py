import os
import json
from modules import zoom, discourse
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
    if summary_data:
        # Extract detailed summaries
        summary_content = ""
        if summary_data.get("summary_details"):
            summaries = [detail.get("summary", "") for detail in summary_data["summary_details"]]
            summary_content = "\n\n".join(summaries)
        
        # Format next steps
        next_steps = ""
        if summary_data.get("next_steps"):
            steps = [f"- {step}" for step in summary_data["next_steps"]]
            next_steps = "\n\n**Next Steps:**\n" + "\n".join(steps)
        
        final_summary = f"{summary_content}{next_steps}"
    else:
        final_summary = "No summary available yet"
    print(f"Final summary text: {final_summary}")
    
    # Extract proper share URL and passcode (new format)
    share_url = recording_data.get('share_url', '')
    passcode = recording_data.get('password', '')
    
    # Get transcript download URL from recording files
    transcript_url = next(
        (f['download_url'] for f in recording_data.get('recording_files', [])
         if f['file_type'] == 'TRANSCRIPT'),
        None
    )

    # Build post content with actual summary text
    post_content = f"""**Meeting Summary:**
{final_summary}

**Recording Access:**
- [Join Recording Session]({share_url}) (Passcode: `{passcode}`)"""

    # Add transcript link if available
    if transcript_url:
        post_content += f"\n- [Download Transcript]({transcript_url})"

    discourse.create_post(
        topic_id=discourse_topic_id,
        body=post_content
    )
    
    print(f"Posted recording links for meeting {meeting_id} to topic {discourse_topic_id}")

    # Now, send the same content to Telegram
    try:
        import modules.telegram as telegram  # Ensure telegram module is available
        telegram.send_message(post_content)
        print("Message sent to Telegram successfully.")
    except Exception as e:
        print(f"Error sending message to Telegram: {e}")
    
    return discourse_topic_id
