import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import base64
import pytz
import sys
import calendar

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
        'start': {
            'dateTime': start_dt.isoformat(),
            'timeZone': 'UTC'
        },
        'end': {
            'dateTime': end_dt.isoformat(),
            'timeZone': 'UTC'
        },
    }

    try:
        service = get_calendar_service()
        event = service.events().insert(calendarId=calendar_id, body=event_body).execute()
        event_id = event.get('id')
        html_link = event.get('htmlLink')
        print(f"[DEBUG] Created calendar event with ID: {event_id}")
        return {
            'htmlLink': html_link,
            'id': event_id
        }
    except Exception as e:
        error_msg = f"Error creating calendar event: {str(e)}"
        print(f"::error::{error_msg}")
        raise

def update_event(event_id: str, summary: str, start_dt, duration_minutes: int, calendar_id: str, description=""):
    """Update an existing Google Calendar event"""
    print(f"[DEBUG] Attempting to update calendar event {event_id} with summary: {summary}")
    
    if not event_id:
        raise ValueError("No event_id provided for update")
    
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
        'start': {
            'dateTime': start_dt.isoformat(),
            'timeZone': 'UTC'
        },
        'end': {
            'dateTime': end_dt.isoformat(),
            'timeZone': 'UTC'
        },
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
            
            # Instead of raising an error, let the caller know that this event doesn't exist
            # so they can create a new one
            print(f"[DEBUG] Event not found, suggest creating a new one")
            raise ValueError(error_msg)

        # If we're here, the event exists, so update it
        event = service.events().update(
            calendarId=calendar_id,
            eventId=event_id,
            body=event_body
        ).execute()
        event_id = event.get('id')
        html_link = event.get('htmlLink')
        print(f"[DEBUG] Successfully updated event with ID: {event_id}")
        return {
            'htmlLink': html_link,
            'id': event_id
        }
    except ValueError:
        # Re-raise ValueError to let caller know this needs a new event
        raise
    except Exception as e:
        error_msg = f"Error updating calendar event: {str(e)}"
        print(f"::error::{error_msg}")
        raise

def update_recurring_event(event_id: str, summary: str, start_dt, duration_minutes: int, calendar_id: str, occurrence_rate: str, description=""):
    """
    Update an existing recurring Google Calendar event, preserving recurrence settings
    Args:
        event_id: ID of the existing event to update
        summary: Event title
        start_dt: Start datetime (string or datetime)
        duration_minutes: Duration in minutes
        calendar_id: Google Calendar ID
        occurrence_rate: weekly, bi-weekly, or monthly
        description: Optional event description
    Returns:
        Dict with htmlLink and id
    """
    print(f"[DEBUG] Attempting to update recurring calendar event {event_id} with summary: {summary}")
    
    if not event_id:
        raise ValueError("No event_id provided for update")
    
    # Same datetime handling as create_event
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
        # For monthly recurrence, we want to maintain the same day of the week
        # (e.g., the second Wednesday of each month)
        
        # Get the day of the week (1=Monday, 7=Sunday in iCalendar format)
        day_of_week = start_dt.isoweekday()
        
        # Calculate which week of the month this day falls on (1-based)
        day_of_month = start_dt.day
        week_of_month = (day_of_month - 1) // 7 + 1
        
        # Check if this is the last occurrence of this weekday in the month
        days_in_month = calendar.monthrange(start_dt.year, start_dt.month)[1]
        if day_of_month + 7 > days_in_month:
            # This is the last occurrence of this weekday in the month
            # Use -1 to indicate the last occurrence
            week_of_month = -1
            
        # Format for iCalendar: 
        # FREQ=MONTHLY;BYDAY={week_of_month}{day_of_week_shortname}
        # Week of month is numeric (1, 2, 3, 4 or -1 for last)
        # Day of week shortname is MO, TU, WE, TH, FR, SA, SU
        
        # Map day of week to shortname
        day_map = {1: "MO", 2: "TU", 3: "WE", 4: "TH", 5: "FR", 6: "SA", 7: "SU"}
        day_shortname = day_map[day_of_week]
        
        # Create the BYDAY value
        byday = f"{week_of_month}{day_shortname}"
        
        recurrence = [f'RRULE:FREQ=MONTHLY;BYDAY={byday}']
        
        print(f"[DEBUG] Setting up monthly calendar recurrence on the {week_of_month if week_of_month != -1 else 'last'} {day_shortname} of each month")
    else:
        raise ValueError(f"Unsupported occurrence rate: {occurrence_rate}")

    try:
        service = get_calendar_service()
        
        try:
            # First try to get the event to verify it exists
            existing_event = service.events().get(
                calendarId=calendar_id,
                eventId=event_id
            ).execute()
            print(f"[DEBUG] Found existing recurring event with ID: {existing_event.get('id')}")
        except Exception as e:
            error_msg = f"Failed to find existing recurring event: {str(e)}"
            print(f"[DEBUG] {error_msg}")
            
            # Instead of raising an error, let the caller know that this event doesn't exist
            # so they can create a new one
            print(f"[DEBUG] Event not found, suggest creating a new recurring event")
            raise ValueError(error_msg)

        # Build event body with recurrence information
        event_body = {
            'summary': summary,
            'description': description,
            'start': {
                'dateTime': start_dt.isoformat(),
                'timeZone': 'UTC'
            },
            'end': {
                'dateTime': end_dt.isoformat(),
                'timeZone': 'UTC'
            },
            'recurrence': recurrence,
        }

        # If we're here, the event exists, so update it while preserving recurrence
        event = service.events().update(
            calendarId=calendar_id,
            eventId=event_id,
            body=event_body
        ).execute()
        event_id = event.get('id')
        html_link = event.get('htmlLink')
        print(f"[DEBUG] Successfully updated recurring event with ID: {event_id}")
        return {
            'htmlLink': html_link,
            'id': event_id
        }
    except ValueError:
        # Re-raise ValueError to let caller know this needs a new event
        raise
    except Exception as e:
        error_msg = f"Error updating recurring calendar event: {str(e)}"
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
        Dict with htmlLink and id
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
        # For monthly recurrence, we want to maintain the same day of the week
        # (e.g., the second Wednesday of each month)
        
        # Get the day of the week (1=Monday, 7=Sunday in iCalendar format)
        day_of_week = start_dt.isoweekday()
        
        # Calculate which week of the month this day falls on (1-based)
        day_of_month = start_dt.day
        week_of_month = (day_of_month - 1) // 7 + 1
        
        # Check if this is the last occurrence of this weekday in the month
        days_in_month = calendar.monthrange(start_dt.year, start_dt.month)[1]
        if day_of_month + 7 > days_in_month:
            # This is the last occurrence of this weekday in the month
            # Use -1 to indicate the last occurrence
            week_of_month = -1
            
        # Format for iCalendar: 
        # FREQ=MONTHLY;BYDAY={week_of_month}{day_of_week_shortname}
        # Week of month is numeric (1, 2, 3, 4 or -1 for last)
        # Day of week shortname is MO, TU, WE, TH, FR, SA, SU
        
        # Map day of week to shortname
        day_map = {1: "MO", 2: "TU", 3: "WE", 4: "TH", 5: "FR", 6: "SA", 7: "SU"}
        day_shortname = day_map[day_of_week]
        
        # Create the BYDAY value
        byday = f"{week_of_month}{day_shortname}"
        
        recurrence = [f'RRULE:FREQ=MONTHLY;BYDAY={byday}']
        
        print(f"[DEBUG] Setting up monthly calendar recurrence on the {week_of_month if week_of_month != -1 else 'last'} {day_shortname} of each month")
    else:
        raise ValueError(f"Unsupported occurrence rate: {occurrence_rate}")

    event_body = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_dt.isoformat(),
            'timeZone': 'UTC'
        },
        'end': {
            'dateTime': end_dt.isoformat(),
            'timeZone': 'UTC'
        },
        'recurrence': recurrence,
    }

    try:
        service = get_calendar_service()
        event = service.events().insert(calendarId=calendar_id, body=event_body).execute()
        event_id = event.get('id')
        html_link = event.get('htmlLink')
        print(f"[DEBUG] Created recurring calendar event with ID: {event_id}")
        return {
            'htmlLink': html_link,
            'id': event_id
        }
    except Exception as e:
        error_msg = f"Error creating recurring calendar event: {str(e)}"
        print(f"::error::{error_msg}")
        raise
