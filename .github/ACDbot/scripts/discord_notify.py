import json
from datetime import datetime, timedelta, timezone
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from modules.discord_notify import send_discord_notification
from modules.mapping_utils import load_mapping

MAPPING_FILE = ".github/ACDbot/meeting_topic_mapping.json"

NOTIFY_WINDOW_MINUTES = 10

def main():
    try:
        mapping = load_mapping()
    except Exception as e:
        print(f"Failed to load mapping file: {e}")
        return
    now = datetime.now(timezone.utc)

    # Process all call series and one-off meetings
    for call_series, series_data in mapping.items():
        if call_series == "one-off":
            # Process one-off meetings
            for meeting_id, entry in series_data.items():
                start_time = entry.get("start_time")
                if not start_time:
                    continue
                try:
                    start_dt = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
                except Exception:
                    continue
                seconds_until = (start_dt - now).total_seconds()
                if 0 <= seconds_until <= NOTIFY_WINDOW_MINUTES * 60:
                    title = entry.get("issue_title", "One-off Meeting")
                    issue_number = entry.get("issue_number")
                    message = f"Reminder: {title} (issue #{issue_number}) starts at {start_dt.strftime('%H:%M UTC')}!"
                    send_discord_notification("one-off", message)
        else:
            # Process recurring series occurrences
            call_series_lower = call_series.lower()
            for occurrence in series_data.get("occurrences", []):
                start_time = occurrence.get("start_time")
                if not start_time:
                    continue
                try:
                    start_dt = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
                except Exception:
                    continue
                seconds_until = (start_dt - now).total_seconds()
                if 0 <= seconds_until <= NOTIFY_WINDOW_MINUTES * 60:
                    title = occurrence.get("issue_title", f"{call_series.upper()} Meeting")
                    issue_number = occurrence.get("issue_number")
                    message = f"Reminder: {title} (issue #{issue_number}) starts at {start_dt.strftime('%H:%M UTC')}!"
                    send_discord_notification(call_series_lower, message)

if __name__ == "__main__":
    main()