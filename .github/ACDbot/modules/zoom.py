import requests
import os
from datetime import datetime, timedelta, timezone
import json
import urllib.parse

account_id=os.environ["ZOOM_ACCOUNT_ID"]
client_id=os.environ["ZOOM_CLIENT_ID"]
client_secret=os.environ["ZOOM_CLIENT_SECRET"]

auth_token_url = "https://zoom.us/oauth/token"
api_base_url = "https://api.zoom.us/v2"

def create_meeting(topic, start_time, duration):

    access_token = get_access_token()

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    # Get alternative hosts from environment
    alternative_hosts = os.environ.get("ZOOM_ALTERNATIVE_HOSTS", "")
    
    payload = {
        "topic": topic,
        "type": 2,  # Scheduled meeting
        "start_time": start_time,  # ISO 8601 format, e.g., "2025-01-18T14:00:00Z"
        "duration": duration,  # Duration in minutes
        "settings": {
            "auto_start_meeting_summary": True,
            "auto_start_ai_companion_questions": True,
            "join_before_host": True,  
            #"waiting_room": True,
            "meeting_authentication": False,
            "auto_recording": "cloud",  
            "approval_type": 2,  
            "alternative_hosts": alternative_hosts,  
            "recording": {
                "auto_recording": "cloud",
                "cloud_recording_download": True,
                "cloud_recording_thumbnails": True,
                "recording_audio_transcript": True, 
            },
        }
    }
    resp = requests.post(f"{api_base_url}/users/me/meetings", 
                            headers=headers, 
                            json=payload)
    
    if resp.status_code!=201:
        print("Unable to generate meeting link")
        resp.raise_for_status()
    response_data = resp.json()
    
    content = {
                "meeting_url": response_data["join_url"], 
                "password": response_data.get("password", ""),
                "meetingTime": response_data["start_time"],
                "purpose": response_data["topic"],
                "duration": response_data["duration"],
                "message": "Success",
                "status":1
    }
    print(content)
    return response_data["join_url"], response_data["id"]

def get_access_token():
    data = {
        "grant_type": "account_credentials",
        "account_id": account_id,
        "client_secret": client_secret
    }
    response = requests.post(auth_token_url, 
                                auth=(client_id, client_secret), 
                                data=data)
    
    if response.status_code!=200:
        print("Unable to get access token")
        response.raise_for_status()
    else:
        response_data = response.json()
        return response_data["access_token"]

def get_meeting_recording(meeting_id):
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    # URL-encode the meeting id to ensure a compliant endpoint URL.
    meeting_id_encoded = urllib.parse.quote(str(meeting_id), safe='')
    url = f"{api_base_url}/meetings/{meeting_id_encoded}/recordings"

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        error_details = response.json()
        print(f"Error fetching meeting recording: {response.status_code} {response.reason} - {error_details}")
        return None

    return response.json()

def get_meeting_transcript(meeting_id):
    """
    Fetches the transcript file content for a given meeting ID.

    :param meeting_id: The Zoom meeting ID
    :return: Transcript text content
    """
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    url = f"{api_base_url}/meetings/{meeting_id}/recordings"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching meeting recordings: {response.status_code} {response.text}")
        response.raise_for_status()
    data = response.json()
    recording_files = data.get('recording_files', [])

    # Find the transcript file
    transcript_file = None
    for file in recording_files:
        if file.get('file_type') == 'TRANSCRIPT':
            transcript_file = file
            break

    if not transcript_file:
        print(f"No transcript found for meeting {meeting_id} - available files: {recording_files}")
        return None

    download_url = transcript_file.get('download_url')
    if not download_url:
        raise ValueError("Transcript download URL not found.")

    # Download the transcript file
    transcript_content = download_zoom_file(download_url, access_token)
    return transcript_content

def download_zoom_file(download_url, access_token):
    """
    Downloads a file from Zoom using the access token.

    :param download_url: The URL to the file
    :param access_token: Zoom access token
    :return: Content of the file
    """
    response = requests.get(download_url, headers={"Authorization": f"Bearer {access_token}"})
    if response.status_code != 200:
        print(f"Error downloading file: {response.status_code} {response.text}")
        response.raise_for_status()
    return response.content.decode('utf-8')

def get_recordings_list():
    """
    Retrieves a list of cloud recordings for the user.
    """
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "page_size": 100,
        "from": (datetime.utcnow() - timedelta(days=7)).strftime("%Y-%m-%d"),  # Adjust time range as needed
        "to": datetime.utcnow().strftime("%Y-%m-%d")
    }
    response = requests.get(f"{api_base_url}/users/me/recordings", headers=headers, params=params)
    if response.status_code != 200:
        print(f"Error fetching recordings: {response.status_code} {response.text}")
        response.raise_for_status()
    data = response.json()
    return data.get("meetings", [])

def get_meeting_summary(meeting_uuid: str) -> dict:
    """Temporary workaround for summary endpoint"""
    try:
        # First try with server-to-server token
        access_token = get_access_token()
        headers = {"Authorization": f"Bearer {access_token}"}
        encoded_uuid = requests.utils.quote(meeting_uuid, safe='')
        
        print(f"Attempting summary with UUID: {encoded_uuid}")  # Debug
        
        response = requests.get(
            f"https://api.zoom.us/v2/meetings/{encoded_uuid}/meeting_summary",
            headers=headers
        )
        
        print(f"API Response: {response.status_code}")  # Debug
        
        if response.status_code == 404:
            print("Zoom API: Summary not found")
            return {}
            
        response.raise_for_status()
        summary = response.json()
        print(f"Raw summary data: {json.dumps(summary, indent=2)}")  # Debug
        return summary
        
    except requests.HTTPError as e:
        print(f"Zoom API Error ({e.response.status_code}): {e.response.text}")
        return {}
    except Exception as e:
        print(f"General error: {str(e)}")
        return {}
def get_meeting(meeting_id):
    """
    Retrieves details for a specific Zoom meeting.
    Returns: dict with meeting details including 'join_url'
    """
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    get_url = f"{api_base_url}/meetings/{meeting_id}"
    response = requests.get(get_url, headers=headers)
    response.raise_for_status()
    
    return response.json()

def update_meeting(meeting_id, topic, start_time, duration):
    """
    Updates an existing Zoom meeting using the PATCH method.
    See Zoom API documentation: https://developers.zoom.us/docs/api/meetings/#tag/meetings/PATCH/meetings/{meetingId}
    
    :param meeting_id: Zoom meeting ID to update.
    :param topic: Updated meeting topic/title.
    :param start_time: Updated start time in ISO 8601 format (e.g., "2025-01-18T14:00:00Z").
    :param duration: Updated duration in minutes.
    :return: A dict confirming the update.
    """
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "topic": topic,
        "start_time": start_time,
        "duration": duration
    }
    update_url = f"{api_base_url}/meetings/{meeting_id}"
    resp = requests.patch(update_url, headers=headers, json=payload)
    
    if resp.status_code != 204:
        print(f"Error updating meeting {meeting_id}: {resp.status_code} {resp.text}")
        resp.raise_for_status()
    
    # Get updated meeting details to retrieve join_url
    meeting_details = get_meeting(meeting_id)
    
    return {
        "id": meeting_id,
        "join_url": meeting_details["join_url"],
        "message": "Meeting updated successfully"
    }

def create_recurring_meeting(topic, start_time, duration, occurrence_rate):
    """
    Creates a recurring Zoom meeting
    Args:
        topic: Meeting title
        start_time: Start time in ISO format
        duration: Duration in minutes
        occurrence_rate: weekly, bi-weekly, or monthly
    Returns:
        Tuple of (join_url, meeting_id)
    """
    access_token = get_access_token()

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    # Map occurrence rate to Zoom recurrence type
    recurrence = {
        "type": 2,  # Default to weekly
        "repeat_interval": 1,
        "weekly_days": "1",  # Default to Monday
        "end_times": 1  # Number of occurrences
    }
    
    if occurrence_rate == "weekly":
        recurrence["type"] = 2
        recurrence["repeat_interval"] = 1
    elif occurrence_rate == "bi-weekly":
        recurrence["type"] = 2
        recurrence["repeat_interval"] = 2
    elif occurrence_rate == "monthly":
        recurrence["type"] = 3
        recurrence["repeat_interval"] = 1
    
    # Get alternative hosts from environment
    alternative_hosts = os.environ.get("ZOOM_ALTERNATIVE_HOSTS", "")
    
    # First attempt with all settings
    payload = {
        "topic": topic,
        "type": 8,  # 8 for recurring meeting with fixed time
        "start_time": start_time,
        "duration": duration,
        "recurrence": recurrence,
        "settings": {
            "auto_start_meeting_summary": True,
            "auto_start_ai_companion_questions": True,
            "join_before_host": True,  
            "meeting_authentication": False,
            "auto_recording": "cloud",  
            "approval_type": 2,  
            "alternative_hosts": alternative_hosts,  
            "recording": {
                "auto_recording": "cloud",
                "cloud_recording_download": True,
                "cloud_recording_thumbnails": True,
                "recording_audio_transcript": True, 
            },
        }
    }

    print(f"[DEBUG] Creating recurring Zoom meeting with payload: {json.dumps(payload, indent=2)}")

    try:
        resp = requests.post(
            f"{api_base_url}/users/me/meetings",
            headers=headers,
            json=payload
        )
        
        # Check for specific alternative host error (code 1114)
        if resp.status_code == 400:
            error_data = resp.json()
            if error_data.get("code") == 1114 and "alternative host" in error_data.get("message", "").lower():
                print(f"[DEBUG] Alternative host error detected, retrying without alternative hosts")
                
                # Remove alternative hosts and try again
                payload["settings"].pop("alternative_hosts", None)
                
                print(f"[DEBUG] Retrying with modified payload: {json.dumps(payload, indent=2)}")
                
                resp = requests.post(
                    f"{api_base_url}/users/me/meetings",
                    headers=headers,
                    json=payload
                )
        
        if resp.status_code != 201:
            print(f"[DEBUG] Zoom API Error Response: {resp.status_code} {resp.text}")
            print(f"[DEBUG] Request payload: {json.dumps(payload, indent=2)}")
            print(f"[DEBUG] Request headers: {headers}")
            resp.raise_for_status()
        
        response_data = resp.json()
        print(f"[DEBUG] Successfully created recurring meeting: {json.dumps(response_data, indent=2)}")
        return response_data["join_url"], response_data["id"]
        
    except requests.exceptions.RequestException as e:
        print(f"[DEBUG] Error creating recurring meeting: {str(e)}")
        if hasattr(e, 'response') and e.response:
            print(f"[DEBUG] Error response: {e.response.text}")
        raise

