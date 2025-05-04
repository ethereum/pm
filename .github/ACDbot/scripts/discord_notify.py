import json
from datetime import datetime, timedelta, timezone
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from modules.discord_notify import send_discord_notification

MAPPING_FILE = ".github/ACDbot/meeting_topic_mapping.json"

NOTIFY_WINDOW_MINUTES = 10

def main():
    try:
        with open(MAPPING_FILE) as f:
            mapping = json.load(f)
    except Exception as e:
        print(f"Failed to load mapping file: {e}")
        return
    now = datetime.now(timezone.utc)
    for meeting in mapping.values():
        call_series = meeting.get("call_series", "").lower()
        for occ in meeting.get("occurrences", []):
            start_time = occ.get("start_time")
            if not start_time:
                continue
            try:
                start_dt = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
            except Exception:
                continue
            seconds_until = (start_dt - now).total_seconds()
            if 0 <= seconds_until <= NOTIFY_WINDOW_MINUTES * 60:
                title = occ.get("issue_title", "Meeting")
                issue_number = occ.get("issue_number")
                message = f"Reminder: {title} (issue #{issue_number}) starts at {start_dt.strftime('%H:%M UTC')}!"
                send_discord_notification(call_series, message)

if __name__ == "__main__":
    main() 