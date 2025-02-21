import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import base64
import pytz

SCOPES = ['https://www.googleapis.com/auth/calendar']

def create_event(summary: str, start_dt, duration_minutes: int, calendar_id: str, description=""):
    """
    Creates a Google Calendar event using the Google Calendar API.
    Handles both datetime objects and ISO format strings for start_dt.
    """
    print(f"[DEBUG] Creating calendar event: {summary}")

    # Convert start_dt to datetime object if it's a string
    if isinstance(start_dt, str):
        start_dt = datetime.fromisoformat(start_dt.replace('Z', '+00:00'))
    elif not isinstance(start_dt, datetime):
        raise TypeError("start_dt must be a datetime object or ISO format string")
    
    # Ensure timezone awareness
    if not start_dt.tzinfo:
        start_dt = start_dt.replace(tzinfo=pytz.utc)
    
    # Calculate end time using datetime math
    end_dt = start_dt + timedelta(minutes=duration_minutes)
    
    # Format for Google Calendar API
    event_body = {
        'summary': summary,
        'description': description,
        'start': {'dateTime': start_dt.isoformat()},
        'end': {'dateTime': end_dt.isoformat()},
    }

    # Load service account info from environment variable
    service_account_info = json.loads(os.environ['GCAL_SERVICE_ACCOUNT_KEY'])
    credentials = service_account.Credentials.from_service_account_info(
        service_account_info, scopes=SCOPES)

    service = build('calendar', 'v3', credentials=credentials)

    event = service.events().insert(calendarId=calendar_id, body=event_body).execute()
    print(f"[DEBUG] Created calendar event with ID: {event.get('id')}")

    return event.get('htmlLink')

def update_event(event_id: str, summary: str, start_dt, duration_minutes: int, calendar_id: str, description=""):
    """Update an existing Google Calendar event"""
    print(f"[DEBUG] Updating calendar event {event_id} with summary: {summary}")
    
    # Same datetime handling as create_event
    if isinstance(start_dt, str):
        start_dt = datetime.fromisoformat(start_dt.replace('Z', '+00:00'))
    elif not isinstance(start_dt, datetime):
        raise TypeError("start_dt must be a datetime object or ISO format string")
    end_dt = start_dt + timedelta(minutes=duration_minutes)

    # Ensure timezone awareness
    if not start_dt.tzinfo:
        start_dt = start_dt.replace(tzinfo=pytz.utc)
    
    event_body = {
        'summary': summary,
        'description': description,
        'start': {'dateTime': start_dt.isoformat()},
        'end': {'dateTime': end_dt.isoformat()},
    }

    service_account_info = json.loads(os.environ['GCAL_SERVICE_ACCOUNT_KEY'])
    credentials = service_account.Credentials.from_service_account_info(
        service_account_info, scopes=SCOPES)

    service = build('calendar', 'v3', credentials=credentials)
    
    try:
        # First try to get the event to verify it exists
        existing_event = service.events().get(
            calendarId=calendar_id,
            eventId=event_id
        ).execute()
        print(f"[DEBUG] Found existing event with ID: {existing_event.get('id')}")
    except Exception as e:
        print(f"[DEBUG] Failed to find existing event: {str(e)}")
        raise  # Re-raise the exception to be handled by the caller

    event = service.events().update(
        calendarId=calendar_id,
        eventId=event_id,
        body=event_body
    ).execute()
    print(f"[DEBUG] Successfully updated event with ID: {event.get('id')}")

    return event.get('htmlLink')
