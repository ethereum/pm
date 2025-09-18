import json
from datetime import datetime, timedelta, timezone
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from modules.discord_notify import send_discord_notification
from modules.mapping_utils import load_mapping, save_mapping

MAPPING_FILE = ".github/ACDbot/meeting_topic_mapping.json"

# Notification window: send alerts between 60-30 minutes before meeting
NOTIFY_EARLY_MINUTES = 60  # Start sending notifications this many minutes before
NOTIFY_CUTOFF_MINUTES = 30  # Stop automated notifications this many minutes before

def build_discord_message(call_series, occurrence, series_data):
    """Build the enhanced Discord message with agenda, zoom, and YouTube links."""
    call_series_upper = call_series.upper()

    # Get the meeting start time for dynamic Discord timestamp
    start_time = occurrence.get("start_time")
    try:
        from datetime import datetime
        start_dt = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        # Convert to Unix timestamp for Discord
        unix_timestamp = int(start_dt.timestamp())
        # Use Discord's relative timestamp format
        time_display = f"<t:{unix_timestamp}:R>"
    except Exception as e:
        print(f"[ERROR] Failed to parse timestamp for Discord: {e}")
        print(f"[ERROR] Cannot build message without valid timestamp, halting")
        return None

    # Build message lines
    message_lines = [f"**{call_series_upper} {time_display}**"]

    # Agenda link (GitHub issue)
    issue_number = occurrence.get("issue_number")
    if issue_number:
        agenda_url = f"https://github.com/ethereum/pm/issues/{issue_number}"
        message_lines.append(f"Agenda: <{agenda_url}>")

    # YouTube link - only show if stream exists
    youtube_streams = occurrence.get("youtube_streams", [])
    if youtube_streams and len(youtube_streams) > 0:
        # Get the first/main stream URL
        stream_url = youtube_streams[0].get("stream_url")
        if stream_url:
            message_lines.append(f"Stream: <{stream_url}>")

    # Zoom link - use the same logic as _generate_comprehensive_resource_comment
    meeting_id = series_data.get("meeting_id")
    if meeting_id and not str(meeting_id).startswith("placeholder") and meeting_id != "custom":
        try:
            from modules import zoom
            enhanced_url = zoom.get_meeting_url_with_passcode(meeting_id)
            if enhanced_url:
                zoom_url = enhanced_url
            else:
                zoom_url = f"https://zoom.us/j/{meeting_id}"
        except Exception as e:
            # Fallback to basic URL if enhanced URL fails
            zoom_url = f"https://zoom.us/j/{meeting_id}"
            print(f"[ERROR] Failed to get enhanced Zoom URL for {meeting_id}: {type(e).__name__}: {e}")
            print(f"[DEBUG] Falling back to basic URL: {zoom_url}")

        message_lines.append(f"Zoom: <{zoom_url}>")

    return "\n".join(message_lines)

def has_discord_notification_been_sent(occurrence):
    """Check if Discord notification has already been sent for this occurrence."""
    return occurrence.get("discord_notification_sent", False)

def mark_discord_notification_sent(mapping, call_series, occurrence_issue_number):
    """Mark that Discord notification has been sent for this occurrence."""
    try:
        # Find and update the occurrence
        series_data = mapping.get(call_series, {})
        occurrences = series_data.get("occurrences", [])

        for occurrence in occurrences:
            if occurrence.get("issue_number") == occurrence_issue_number:
                occurrence["discord_notification_sent"] = True
                print(f"[DEBUG] Marked Discord notification as sent for issue #{occurrence_issue_number}")
                return True

        print(f"[ERROR] Could not find occurrence with issue #{occurrence_issue_number} to mark notification sent")
        return False
    except Exception as e:
        print(f"[ERROR] Failed to mark Discord notification as sent: {e}")
        return False

def main():
    try:
        mapping = load_mapping()
    except Exception as e:
        print(f"Failed to load mapping file: {e}")
        return
    now = datetime.now(timezone.utc)
    notifications_sent = False

    for call_series, series_data in mapping.items():
        # Only process ACDE, ACDC, ACDT calls
        if call_series.lower() not in ["acde", "acdc", "acdt"]:
            continue

        # Process all series occurrences
        call_series_lower = call_series.lower()
        for occurrence in series_data.get("occurrences", []):
            start_time = occurrence.get("start_time")
            if not start_time:
                continue

            # Skip if notification already sent
            if has_discord_notification_been_sent(occurrence):
                continue
            try:
                start_dt = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
            except Exception:
                continue
            seconds_until = (start_dt - now).total_seconds()
            # Notify between 60-30 minutes before meeting for early warning
            # This gives people advance notice while leaving time for manual intervention
            notify_early_seconds = NOTIFY_EARLY_MINUTES * 60  # 60 minutes before
            notify_cutoff_seconds = NOTIFY_CUTOFF_MINUTES * 60  # 30 minutes before

            # Debug logging for time calculations
            if seconds_until < 0:
                print(f"[DEBUG] Skipping past meeting {call_series}: {seconds_until/60:.1f} minutes ago")
                continue
            elif seconds_until > notify_early_seconds:
                print(f"[DEBUG] Skipping future meeting {call_series}: {seconds_until/60:.1f} minutes away (too early, waiting for {NOTIFY_EARLY_MINUTES}min window)")
                continue
            elif seconds_until < notify_cutoff_seconds:
                print(f"[DEBUG] Skipping late meeting {call_series}: {seconds_until/60:.1f} minutes away (past {NOTIFY_CUTOFF_MINUTES}min cutoff, manual intervention needed)")
                continue

            if notify_cutoff_seconds <= seconds_until <= notify_early_seconds:
                message = build_discord_message(call_series, occurrence, series_data)
                if message is None:
                    print(f"[ERROR] Skipping notification for {call_series} due to message build failure")
                    continue
                print(f"Sending notification for {call_series}: {message}")

                # Send notification
                success = send_discord_notification(call_series_lower, message)

                if success:
                    # Mark as sent to prevent duplicate notifications
                    issue_number = occurrence.get("issue_number")
                    if mark_discord_notification_sent(mapping, call_series, issue_number):
                        notifications_sent = True

    # Save mapping if any notifications were sent
    if notifications_sent:
        try:
            save_mapping(mapping)
            print("[DEBUG] Saved mapping with Discord notification flags")
        except Exception as e:
            print(f"[ERROR] Failed to save mapping: {e}")

if __name__ == "__main__":
    main()