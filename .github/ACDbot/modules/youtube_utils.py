from googleapiclient.discovery import build
import os
from datetime import datetime, timedelta
import pytz
import sys
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError
import calendar

def get_youtube_service():
    """
    Gets an authenticated YouTube service using OAuth2 credentials
    """
    try:
        # Check for required OAuth2 environment variables
        required_vars = ["YOUTUBE_REFRESH_TOKEN", "GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET"]
        missing_vars = [var for var in required_vars if not os.environ.get(var)]
        
        if missing_vars:
            error_msg = f"Error: Missing required environment variables: {', '.join(missing_vars)}"
            print(f"::error::{error_msg}")
            raise ValueError(error_msg)
        
        # Create credentials using refresh token
        creds = Credentials(
            token=None,
            refresh_token=os.environ["YOUTUBE_REFRESH_TOKEN"],
            client_id=os.environ["GOOGLE_CLIENT_ID"],
            client_secret=os.environ["GOOGLE_CLIENT_SECRET"],
            token_uri="https://oauth2.googleapis.com/token",
            scopes=[
                "https://www.googleapis.com/auth/youtube.upload",
                "https://www.googleapis.com/auth/youtube.force-ssl",
                "https://www.googleapis.com/auth/youtube"
            ]
        )
        
        # Refresh the access token
        request = Request()
        creds.refresh(request)
        print("[DEBUG] Successfully refreshed YouTube OAuth2 token")
        
        # Create the YouTube service with the credentials
        return build('youtube', 'v3', credentials=creds)
    
    except RefreshError as e:
        error_msg = f"Error: Failed to refresh YouTube OAuth2 token: {str(e)}"
        print(f"::error::{error_msg}")
        print("Manual reauthorization required - run get_refresh_token.py to generate a new refresh token")
        raise ValueError(error_msg)
    except Exception as e:
        error_msg = f"Error: Failed to authenticate with YouTube API: {str(e)}"
        print(f"::error::{error_msg}")
        raise ValueError(error_msg)

def get_channel_id_by_custom_url(custom_url):
    try:
        youtube = get_youtube_service()

        response = youtube.channels().list(
            part='id',
            forUsername=custom_url
        ).execute()

        items = response.get('items', [])
        if items:
            return items[0]['id']
        else:
            # Try retrieving by channel custom URL path
            response = youtube.search().list(
                part='snippet',
                q=custom_url,
                type='channel',
                maxResults=1
            ).execute()
            items = response.get('items', [])
            if items:
                return items[0]['snippet']['channelId']
            else:
                raise Exception("Channel not found")
    except Exception as e:
        error_msg = f"Error finding channel by custom URL: {str(e)}"
        print(f"::error::{error_msg}")
        raise

def get_channel_videos(channel_id):
    try:
        youtube = get_youtube_service()

        videos = []
        next_page_token = None

        while True:
            res = youtube.search().list(
                part='snippet',
                channelId=channel_id,
                maxResults=50,
                pageToken=next_page_token,
                order='date',
                type='video'
            ).execute()

            videos.extend(res['items'])
            next_page_token = res.get('nextPageToken')

            if not next_page_token:
                break

        return videos
    except Exception as e:
        error_msg = f"Error getting channel videos: {str(e)}"
        print(f"::error::{error_msg}")
        raise

def create_youtube_stream(title, description, start_time, privacy_status='public'):
    """
    Creates a YouTube live stream event
    Args:
        title: Stream title
        description: Stream description
        start_time: Start time in ISO format
        privacy_status: public, private, or unlisted
    Returns:
        Dictionary containing stream_id and stream_url
    """
    try:
        youtube = get_youtube_service()
        
        print(f"[DEBUG] Creating YouTube stream: {title}")
        
        # Ensure start_time is in correct ISO 8601 format
        # YouTube requires the format: YYYY-MM-DDThh:mm:ss.sZ
        if start_time.endswith('Z'):
            # Convert to standard format expected by YouTube
            from datetime import datetime
            try:
                dt = datetime.fromisoformat(start_time.replace('Z', '+00:00'))
                # Format to YouTube's expected format with milliseconds
                start_time = dt.strftime('%Y-%m-%dT%H:%M:%S.000Z')
            except ValueError:
                # If parsing fails, leave as is
                pass
                
        print(f"[DEBUG] Using formatted start time: {start_time}")
        
        # Create the broadcast
        broadcast_insert_response = youtube.liveBroadcasts().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": title,
                    "scheduledStartTime": start_time,
                    "description": description,
                },
                "status": {
                    "privacyStatus": privacy_status,
                    "selfDeclaredMadeForKids": False,
                }
            }
        ).execute()

        broadcast_id = broadcast_insert_response["id"]
        print(f"[DEBUG] Created broadcast with ID: {broadcast_id}")

        # Create the stream
        stream_insert_response = youtube.liveStreams().insert(
            part="snippet,cdn",
            body={
                "snippet": {
                    "title": title,
                },
                "cdn": {
                    "frameRate": "variable",
                    "ingestionType": "rtmp",
                    "resolution": "variable"
                }
            }
        ).execute()

        stream_id = stream_insert_response["id"]
        print(f"[DEBUG] Created stream with ID: {stream_id}")

        # Bind the broadcast to the stream
        youtube.liveBroadcasts().bind(
            part="id,contentDetails",
            id=broadcast_id,
            streamId=stream_id
        ).execute()
        print(f"[DEBUG] Bound broadcast {broadcast_id} to stream {stream_id}")

        # Get the ingestion URL and stream name for RTMP streaming
        ingestion_address = stream_insert_response.get("cdn", {}).get("ingestionInfo", {}).get("ingestionAddress", "")
        stream_name = stream_insert_response.get("cdn", {}).get("ingestionInfo", {}).get("streamName", "")
        rtmp_url = f"{ingestion_address}/{stream_name}" if ingestion_address and stream_name else ""

        return {
            "broadcast_id": broadcast_id,
            "stream_id": stream_id,
            "stream_url": f"https://youtube.com/watch?v={broadcast_id}",
            "rtmp_url": rtmp_url
        }
    except Exception as e:
        error_msg = f"Error creating YouTube stream: {str(e)}"
        print(f"::error::{error_msg}")
        if "quota" in str(e).lower():
            print(f"[DEBUG] This may be a quota issue with the YouTube API")
        raise

def create_recurring_streams(title, description, start_time, occurrence_rate, num_events=1):
    """
    Creates multiple YouTube live stream events for recurring meetings
    Args:
        title: Base title for streams
        description: Stream description
        start_time: Initial start time in ISO format
        occurrence_rate: weekly, bi-weekly, or monthly
        num_events: Number of future events to create
    Returns:
        List of dictionaries containing stream details
    """
    try:
        streams = []
        
        # Ensure start_time is parsed correctly
        if isinstance(start_time, str):
            # Handle different ISO formats
            if start_time.endswith('Z'):
                start_time = start_time.replace('Z', '+00:00')
            current_time = datetime.fromisoformat(start_time)
        else:
            current_time = start_time
            
        print(f"[DEBUG] Creating {num_events} recurring streams for '{title}' starting at {current_time}")
        
        for i in range(num_events):
            # Calculate next event time based on occurrence rate
            if i > 0:
                if occurrence_rate == 'weekly':
                    current_time += timedelta(days=7)
                elif occurrence_rate == 'bi-weekly':
                    current_time += timedelta(days=14)
                elif occurrence_rate == 'monthly':
                    # For monthly recurrence, we want to keep the same day of the week
                    # E.g., the second Wednesday of each month
                    
                    # First, record the original weekday
                    original_weekday = current_time.weekday()  # 0=Monday, 6=Sunday
                    
                    # Calculate the target month's date to preserve the same weekday position
                    # Get current year and month
                    year = current_time.year
                    month = current_time.month
                    
                    # Move to the next month
                    if month == 12:
                        year += 1
                        month = 1
                    else:
                        month += 1
                    
                    # Determine which week of the month the current day falls on (1-based)
                    # First, get the first day of the current month
                    first_day_of_month = current_time.replace(day=1)
                    
                    # Calculate which occurrence of this weekday we're on
                    week_of_month = (current_time.day - 1) // 7 + 1
                    
                    # If this is the last occurrence of this weekday in the month
                    days_in_current_month = calendar.monthrange(current_time.year, current_time.month)[1]
                    if current_time.day + 7 > days_in_current_month:
                        # This is the last occurrence of this weekday in the month
                        # We'll need to find the last occurrence in the target month
                        last_occurrence = True
                        print(f"[DEBUG] This is the last {calendar.day_name[original_weekday]} of the month")
                    else:
                        last_occurrence = False
                        print(f"[DEBUG] This is the {week_of_month}{'st' if week_of_month == 1 else 'nd' if week_of_month == 2 else 'rd' if week_of_month == 3 else 'th'} {calendar.day_name[original_weekday]} of the month")
                    
                    # Now calculate the equivalent day in the next month
                    if last_occurrence:
                        # Find the last day of the target month
                        last_day_of_next_month = calendar.monthrange(year, month)[1]
                        
                        # Start from the last day and go backward to find the last occurrence of the weekday
                        target_day = last_day_of_next_month
                        target_date = datetime(year, month, target_day, 
                                               hour=current_time.hour,
                                               minute=current_time.minute,
                                               second=current_time.second,
                                               microsecond=current_time.microsecond,
                                               tzinfo=current_time.tzinfo)
                        
                        # Go backward until we hit the right weekday
                        while target_date.weekday() != original_weekday:
                            target_day -= 1
                            target_date = target_date.replace(day=target_day)
                        
                        print(f"[DEBUG] Last {calendar.day_name[original_weekday]} of next month ({year}-{month}) is day {target_day}")
                    else:
                        # Find the first occurrence of this weekday in the target month
                        first_of_next_month = datetime(year, month, 1,
                                                       hour=current_time.hour,
                                                       minute=current_time.minute,
                                                       second=current_time.second,
                                                       microsecond=current_time.microsecond,
                                                       tzinfo=current_time.tzinfo)
                        
                        # Calculate the first occurrence of the desired weekday
                        days_until_first_occurrence = (original_weekday - first_of_next_month.weekday()) % 7
                        first_occurrence_day = 1 + days_until_first_occurrence
                        
                        # Now find the nth occurrence where n is week_of_month
                        target_day = first_occurrence_day + (week_of_month - 1) * 7
                        
                        # Check if this day exists in the target month
                        days_in_next_month = calendar.monthrange(year, month)[1]
                        if target_day > days_in_next_month:
                            # The target week doesn't exist in this month (e.g., 5th Thursday)
                            # Use the last occurrence instead
                            print(f"[DEBUG] The {week_of_month}{'st' if week_of_month == 1 else 'nd' if week_of_month == 2 else 'rd' if week_of_month == 3 else 'th'} {calendar.day_name[original_weekday]} doesn't exist in {year}-{month}")
                            
                            # Find the last occurrence instead
                            target_day = days_in_next_month
                            target_date = datetime(year, month, target_day,
                                                  hour=current_time.hour,
                                                  minute=current_time.minute,
                                                  second=current_time.second,
                                                  microsecond=current_time.microsecond,
                                                  tzinfo=current_time.tzinfo)
                            
                            # Go backward until we hit the right weekday
                            while target_date.weekday() != original_weekday:
                                target_day -= 1
                                target_date = target_date.replace(day=target_day)
                                
                            print(f"[DEBUG] Using last {calendar.day_name[original_weekday]} of month instead: day {target_day}")
                        else:
                            print(f"[DEBUG] The {week_of_month}{'st' if week_of_month == 1 else 'nd' if week_of_month == 2 else 'rd' if week_of_month == 3 else 'th'} {calendar.day_name[original_weekday]} of {year}-{month} is day {target_day}")
                    
                    # Update current_time with the new target date
                    current_time = current_time.replace(year=year, month=month, day=target_day)
                    print(f"[DEBUG] Next stream scheduled for: {current_time.strftime('%Y-%m-%d %H:%M:%S %Z')} ({calendar.day_name[current_time.weekday()]})")
            
            # Format in the standard YouTube API expects: YYYY-MM-DDThh:mm:ss.sZ
            # YouTube's API is specific about the format - needs milliseconds
            formatted_start_time = current_time.strftime('%Y-%m-%dT%H:%M:%S.000Z')
            
            event_title = f"{title} {i+1}"
            print(f"[DEBUG] Creating stream {i+1}/{num_events}: {event_title}")
            
            stream_details = create_youtube_stream(
                event_title,
                description,
                formatted_start_time
            )
            
            # Store the scheduled time in the stream details for later use
            stream_details['scheduled_time'] = formatted_start_time
            
            streams.append(stream_details)
        
        return streams
    except Exception as e:
        error_msg = f"Error creating recurring YouTube streams: {str(e)}"
        print(f"::error::{error_msg}")
        raise

def get_live_streams(channel_id):
    try:
        youtube = get_youtube_service()

        live_streams = []
        next_page_token = None

        while True:
            res = youtube.search().list(
                part='snippet',
                channelId=channel_id,
                eventType='live',
                type='video',
                order='date',
                maxResults=50,
                pageToken=next_page_token
            ).execute()

            live_streams.extend(res['items'])
            next_page_token = res.get('nextPageToken')

            if not next_page_token:
                break

        return live_streams
    except Exception as e:
        error_msg = f"Error getting live streams: {str(e)}"
        print(f"::error::{error_msg}")
        raise

if __name__ == "__main__":
    try:
        custom_url = "EthereumProtocol"
        channel_id = get_channel_id_by_custom_url(custom_url)
        print(f"Channel ID: {channel_id}")

        videos = get_channel_videos(channel_id)
        print("Videos:")
        for video in videos:
            video_id = video['id']['videoId']
            title = video['snippet']['title']
            print(f"{title}: https://www.youtube.com/watch?v={video_id}")

        live_streams = get_live_streams(channel_id)
        print("\nLive Streams:")
        for stream in live_streams:
            stream_id = stream['id']['videoId']
            title = stream['snippet']['title']
            print(f"{title}: https://www.youtube.com/watch?v={stream_id}")
    except Exception as e:
        print(f"Error in main: {str(e)}")
        sys.exit(1) 