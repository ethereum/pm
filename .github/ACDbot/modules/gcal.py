import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import base64
import pytz
import sys

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    """
    Creates and returns an authenticated Google Calendar service
    with proper error handling for credentials
    """
    try:
        # Check if GCAL_SERVICE_ACCOUNT_KEY exists in environment
        if 'GCAL_SERVICE_ACCOUNT_KEY' not in os.environ:
            error_msg = "Error: GCAL_SERVICE_ACCOUNT_KEY environment variable not found"
            print(f"::error::{error_msg}")
            raise ValueError(error_msg)
            
        # Load service account info from environment variable
        service_account_info = json.loads(os.environ['GCAL_SERVICE_ACCOUNT_KEY'])
        credentials = service_account.Credentials.from_service_account_info(
            service_account_info, scopes=SCOPES)
            
        return build('calendar', 'v3', credentials=credentials)
    except json.JSONDecodeError as e:
        error_msg = f"Error: Failed to parse GCAL_SERVICE_ACCOUNT_KEY as JSON: {str(e)}"
        print(f"::error::{error_msg}")
        print(f"Context access might be invalid: GOOGLE_APPLICATION_CREDENTIALS")
        raise ValueError(error_msg)
    except Exception as e:
        error_msg = f"Error: Failed to authenticate with Google Calendar API: {str(e)}"
        print(f"::error::{error_msg}")
        print(f"Context access might be invalid: GOOGLE_APPLICATION_CREDENTIALS")
        raise

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

    try:
        service = get_calendar_service()
        event = service.events().insert(calendarId=calendar_id, body=event_body).execute()
        print(f"[DEBUG] Created calendar event with ID: {event.get('id')}")
        return event.get('htmlLink')
    except Exception as e:
        error_msg = f"Error creating calendar event: {str(e)}"
        print(f"::error::{error_msg}")
        raise

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

    try:
        service = get_calendar_service()
        
        try:
            # First try to get the event to verify it exists
            existing_event = service.events().get(
                calendarId=calendar_id,
                eventId=event_id
            ).execute()
            print(f"[DEBUG] Found existing event with ID: {existing_event.get('id')}")
        except Exception as e:
            error_msg = f"Failed to find existing event: {str(e)}"
            print(f"[DEBUG] {error_msg}")
            raise ValueError(error_msg)

        event = service.events().update(
            calendarId=calendar_id,
            eventId=event_id,
            body=event_body
        ).execute()
        print(f"[DEBUG] Successfully updated event with ID: {event.get('id')}")
        return event.get('htmlLink')
    except Exception as e:
        error_msg = f"Error updating calendar event: {str(e)}"
        print(f"::error::{error_msg}")
        raise

def create_recurring_event(summary: str, start_dt, duration_minutes: int, calendar_id: str, occurrence_rate: str, description=""):
    """
    Creates a recurring Google Calendar event
    Args:
        summary: Event title
        start_dt: Start datetime (string or datetime)
        duration_minutes: Duration in minutes
        calendar_id: Google Calendar ID
        occurrence_rate: weekly, bi-weekly, or monthly
        description: Optional event description
    Returns:
        Event HTML link
    """
    print(f"[DEBUG] Creating recurring calendar event: {summary}")

    # Convert start_dt to datetime object if it's a string
    if isinstance(start_dt, str):
        start_dt = datetime.fromisoformat(start_dt.replace('Z', '+00:00'))
    elif not isinstance(start_dt, datetime):
        raise TypeError("start_dt must be a datetime object or ISO format string")
    
    # Ensure timezone awareness
    if not start_dt.tzinfo:
        start_dt = start_dt.replace(tzinfo=pytz.utc)
    
    # Calculate end time
    end_dt = start_dt + timedelta(minutes=duration_minutes)
    
    # Set up recurrence rule
    if occurrence_rate == "weekly":
        recurrence = ['RRULE:FREQ=WEEKLY']
    elif occurrence_rate == "bi-weekly":
        recurrence = ['RRULE:FREQ=WEEKLY;INTERVAL=2']
    elif occurrence_rate == "monthly":
        recurrence = ['RRULE:FREQ=MONTHLY']
    else:
        raise ValueError(f"Unsupported occurrence rate: {occurrence_rate}")

    event_body = {
        'summary': summary,
        'description': description,
        'start': {'dateTime': start_dt.isoformat()},
        'end': {'dateTime': end_dt.isoformat()},
        'recurrence': recurrence,
    }

    try:
        service = get_calendar_service()
        event = service.events().insert(calendarId=calendar_id, body=event_body).execute()
        print(f"[DEBUG] Created recurring calendar event with ID: {event.get('id')}")
        return event.get('htmlLink')
    except Exception as e:
        error_msg = f"Error creating recurring calendar event: {str(e)}"
        print(f"::error::{error_msg}")
        raise
