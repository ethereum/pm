import time
from modules.zoom import get_meeting_recording
from modules.email_utils import send_email

def send_recording_email(meeting_id, recipient_email):
    max_attempts = 12  # Check every 5 minutes for 1 hour
    wait_time = 300  # 5 minutes in seconds

    for attempt in range(max_attempts):
        recording_info = get_meeting_recording(meeting_id)
        if recording_info and recording_info.get('recording_files'):
            for file in recording_info['recording_files']:
                if file.get('file_type') == 'MP4':
                    recording_url = file.get('play_url')
                    subject = f"Recording for Meeting ID {meeting_id}"
                    body = f"""
                    <p>Dear recipient,</p>
                    <p>The recording for meeting ID {meeting_id} is now available.</p>
                    <p>You can access it here: <a href="{recording_url}">{recording_url}</a></p>
                    """
                    send_email(recipient_email, subject, body)
                    print("Recording email sent.")
                    return
            print("No MP4 recording found yet.")
        else:
            print("Recording not yet available. Retrying...")
        time.sleep(wait_time)
    print("Recording was not available after multiple attempts.")
