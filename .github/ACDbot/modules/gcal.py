import os
import json
import re
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import base64
import pytz
import sys
import calendar


def encode_calendar_eid(event_id, calendar_id):
    """Encode Google Calendar event ID and calendar ID into proper eid parameter."""
    try:
        # Format calendar ID by replacing @group.calendar.google.com with @g
        if "@group.calendar.google.com" in calendar_id:
            formatted_calendar_id = calendar_id.replace("@group.calendar.google.com", "@g")
        else:
            formatted_calendar_id = calendar_id

        # Combine event ID and calendar ID with a space
        combined = f"{event_id} {formatted_calendar_id}"

        # Base64 encode
        encoded = base64.b64encode(combined.encode('utf-8')).decode('utf-8')

        # Remove trailing = characters
        eid = encoded.rstrip('=')

        return eid
    except Exception as e:
        print(f"⚠️  Could not encode calendar eid: {e}")
        return None

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
        event_id: ID of the existing recurring event to update
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

    try:
        service = get_calendar_service()

        try:
            # First try to get the event to verify it exists
            existing_event = service.events().get(
                calendarId=calendar_id,
                eventId=event_id
            ).execute()
            print(f"[DEBUG] Found existing event with ID: {existing_event.get('id')}")

            # Check if this is actually a recurring event
            is_recurring = 'recurrence' in existing_event and existing_event['recurrence']
            print(f"[DEBUG] Existing event is recurring: {is_recurring}")

            if not is_recurring:
                print(f"[DEBUG] Existing event is one-time, but we need recurring behavior")
                print(f"[DEBUG] Creating new recurring event instead of trying to convert one-time event")

                # Create a new recurring event instead of trying to convert a one-time event
                new_recurring_event = create_recurring_event(
                    summary=summary,
                    start_dt=start_dt,
                    duration_minutes=duration_minutes,
                    calendar_id=calendar_id,
                    occurrence_rate=occurrence_rate,
                    description=description
                )

                print(f"[DEBUG] Created new recurring event to replace one-time event: {new_recurring_event.get('id')}")
                return new_recurring_event

        except Exception as e:
            error_msg = f"Failed to find existing event: {str(e)}"
            print(f"[DEBUG] {error_msg}")
            raise ValueError(error_msg)

        # Get all instances of the recurring event
        instances = service.events().instances(
            calendarId=calendar_id,
            eventId=event_id
        ).execute()

        print(f"[DEBUG] Found {len(instances.get('items', []))} instances of recurring event")

        # Find the specific instance for our target date
        target_instance = None
        for instance in instances.get('items', []):
            instance_start = instance.get('start', {}).get('dateTime')
            if instance_start:
                instance_dt = datetime.fromisoformat(instance_start.replace('Z', '+00:00'))
                # Compare dates (ignore time)
                if instance_dt.date() == start_dt.date():
                    target_instance = instance
                    break

        if target_instance:
            print(f"[DEBUG] Found target instance with ID: {target_instance.get('id')}")
            print(f"[DEBUG] Target instance date: {target_instance.get('start', {}).get('dateTime')}")
            print(f"[DEBUG] Target instance current summary: {target_instance.get('summary')}")
            print(f"[DEBUG] Target instance current description: {target_instance.get('description', 'No description')[:100]}...")

            # Update the specific instance
            target_instance['summary'] = summary
            target_instance['description'] = description
            target_instance['start'] = {
                'dateTime': start_dt.isoformat(),
                'timeZone': 'UTC'
            }
            target_instance['end'] = {
                'dateTime': end_dt.isoformat(),
                'timeZone': 'UTC'
            }

            print(f"[DEBUG] Updating instance with new summary: {summary}")
            print(f"[DEBUG] Updating instance with new description: {description[:100]}...")

            # Update the instance
            updated_instance = service.events().update(
                calendarId=calendar_id,
                eventId=target_instance['id'],
                body=target_instance
            ).execute()

            event_id = updated_instance.get('id')
            html_link = updated_instance.get('htmlLink')
            print(f"[DEBUG] Successfully updated instance with ID: {event_id}")
            print(f"[DEBUG] Updated instance summary: {updated_instance.get('summary')}")
            print(f"[DEBUG] Updated instance description: {updated_instance.get('description', 'No description')[:100]}...")
            print(f"[DEBUG] Updated instance start: {updated_instance.get('start', {}).get('dateTime')}")
            print(f"[DEBUG] Updated instance end: {updated_instance.get('end', {}).get('dateTime')}")
            print(f"[DEBUG] Updated instance is recurring: {'recurringEventId' in updated_instance}")
            if 'recurringEventId' in updated_instance:
                print(f"[DEBUG] Updated instance belongs to recurring event: {updated_instance['recurringEventId']}")

            # Return the original series ID, not the instance ID
            original_series_id = updated_instance.get('recurringEventId', event_id)
            print(f"[DEBUG] Returning original series ID: {original_series_id} (not instance ID: {event_id})")

            return {
                'htmlLink': html_link,
                'id': original_series_id,
                'action_detail': 'instance_updated'
            }
        else:
            print(f"[DEBUG] No matching instance found for date {start_dt.date()}")
            print(f"[DEBUG] Available instance dates:")
            for i, instance in enumerate(instances.get('items', [])[:5]):
                instance_start = instance.get('start', {}).get('dateTime')
                if instance_start:
                    instance_dt = datetime.fromisoformat(instance_start.replace('Z', '+00:00'))
                    print(f"[DEBUG]   {i+1}. {instance_dt.date()} - {instance.get('id')}")

            # Check if the recurrence has ended before our target date
            recurrence_rules = existing_event.get('recurrence', [])
            recurrence_ended = False
            for rule in recurrence_rules:
                if 'UNTIL=' in rule:
                    # Extract the UNTIL date
                    until_match = re.search(r'UNTIL=(\d{8}T\d{6}Z?)', rule)
                    if until_match:
                        until_str = until_match.group(1)
                        # Parse the until date
                        if 'T' in until_str:
                            until_dt = datetime.strptime(until_str.replace('Z', ''), '%Y%m%dT%H%M%S')
                        else:
                            until_dt = datetime.strptime(until_str, '%Y%m%d')
                        until_dt = until_dt.replace(tzinfo=pytz.utc)

                        if until_dt < start_dt:
                            recurrence_ended = True
                            print(f"[DEBUG] Recurrence ended on {until_dt.date()}, before target date {start_dt.date()}")
                            break

            if recurrence_ended:
                # Extend the recurrence to include the new date
                print(f"[DEBUG] Extending recurrence to include new date")

                # Update the UNTIL date in the recurrence rule to at least cover the new date
                # Add some buffer (e.g., 6 months from the new date)
                new_until = start_dt + timedelta(days=180)
                new_until_str = new_until.strftime('%Y%m%dT%H%M%SZ')

                updated_recurrence = []
                for rule in recurrence_rules:
                    if 'UNTIL=' in rule:
                        # Replace the old UNTIL with the new one
                        rule = re.sub(r'UNTIL=\d{8}T\d{6}Z?', f'UNTIL={new_until_str}', rule)
                    updated_recurrence.append(rule)

                print(f"[DEBUG] Updated recurrence rules: {updated_recurrence}")

                # Update the event with extended recurrence
                event_body = {
                    'summary': summary,
                    'description': description,
                    'start': existing_event.get('start'),
                    'end': existing_event.get('end'),
                    'recurrence': updated_recurrence,
                }

                event = service.events().update(
                    calendarId=calendar_id,
                    eventId=event_id,
                    body=event_body
                ).execute()

                print(f"[DEBUG] Extended recurring event to include new date")
                print(f"[DEBUG] New recurrence: {event.get('recurrence')}")

                # Now try to get the specific instance for the target date
                # Need to refetch instances after updating the recurrence
                instances = service.events().instances(
                    calendarId=calendar_id,
                    eventId=event_id
                ).execute()

                for instance in instances.get('items', []):
                    instance_start = instance.get('start', {}).get('dateTime')
                    if instance_start:
                        instance_dt = datetime.fromisoformat(instance_start.replace('Z', '+00:00'))
                        if instance_dt.date() == start_dt.date():
                            # Found the new instance, return its link
                            print(f"[DEBUG] Found new instance after extending recurrence")
                            return {
                                'htmlLink': instance.get('htmlLink'),
                                'id': event_id,  # Return the series ID, not instance ID
                                'action_detail': 'recurrence_extended'
                            }

                # Return the series link if no specific instance found
                return {
                    'htmlLink': event.get('htmlLink'),
                    'id': event_id,
                    'action_detail': 'recurrence_extended'
                }
            else:
                # Recurrence hasn't ended, just update metadata
                print(f"[DEBUG] No specific instance found, updating master recurring event metadata")
                print(f"[DEBUG] This will update the series metadata while preserving the recurrence pattern")

                # Update only the metadata (summary, description) but preserve the original start time and recurrence
                event_body = {
                    'summary': summary,
                    'description': description,
                    'start': existing_event.get('start'),
                    'end': existing_event.get('end'),
                    'recurrence': existing_event.get('recurrence', []),
                }

                event = service.events().update(
                    calendarId=calendar_id,
                    eventId=event_id,
                    body=event_body
                ).execute()

                print(f"[DEBUG] Updated master recurring event metadata")

                return {
                    'htmlLink': event.get('htmlLink'),
                    'id': event_id,
                    'action_detail': 'metadata_updated'
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
