import click
from . import zoom, discourse, telegram, gcal, transcript

@click.group()
def cli():
    """
    ACD Bot command-line interface.
    Use subcommands like:
      - create-zoom
      - create-discourse
      - send-telegram
      - create-calendar-event
      - publish-transcript
    """
    pass

@cli.command()
@click.option("--title", required=True, help="Title of the Zoom meeting")
@click.option("--start-time", required=True, help="Start time in ISO 8601 format (UTC)")
@click.option("--duration", required=False, help="Meeting duration, default 60 min")

def create_zoom(title, start_time, duration):
    """
    Create a Zoom meeting and prints the join URL.
    Example usage:
        python -m modules.cli create-zoom --title 'My Meeting' --start-time '2025-01-01T13:00:00Z'
    """
    try:
        duration = duration if 'duration' in locals() else 60
        zoom_link = zoom.create_meeting(title, start_time, duration)
        click.echo(f"Zoom Meeting Created: {zoom_link}")
    except Exception as e:
        click.echo(f"Error creating Zoom meeting: {e}", err=True)

@cli.command()
@click.option("--title", required=True, help="Title of the Discourse topic")
@click.option("--body", required=True, help="Body/content of the Discourse post")
@click.option("--category-id", default=63, help="Discourse category ID (default 63)")
def create_discourse(title, body, category_id):
    """
    Create a topic on Discourse.
    Example usage:
        python -m modules.cli create-discourse --title 'Proposal' --body 'My content' --category-id 63
    """
    topic_data = discourse.create_topic(title, body, category_id)
    click.echo(f"Created Discourse topic with ID {topic_data.get('topic_id')}")

@cli.command()
@click.option("--message", required=True, help="Message to send on Telegram")
def send_telegram(message):
    """
    Send a message to a Telegram channel.
    Example usage:
        python -m modules.cli send-telegram --message 'Hello from ACD Bot!'
    """
    response = telegram.send_message(message)
    click.echo(response)

@cli.command()
@click.option("--summary", required=True, help="Summary of the calendar event")
@click.option("--start", required=True, help="Start time (ISO 8601, UTC)")
@click.option("--duration", default=60, help="Duration in minutes")
@click.option("--calendar-id", required=True, help="Google Calendar ID")
def create_calendar_event(summary, start, duration, calendar_id):
    """
    Create a Google Calendar event.
    Example usage:
        python -m modules.cli create-calendar-event --summary 'Team Sync' \
          --start '2025-01-01T10:00:00' --duration 30 --calendar-id 'mycalendarid@group.calendar.google.com'
    """
    from datetime import datetime
    start_dt = datetime.fromisoformat(start.replace("Z", ""))  # naive parse

    link = gcal.create_event(
        summary=summary,
        start_dt=start_dt,
        duration_minutes=duration,
        calendar_id=calendar_id
    )
    click.echo(f"Calendar Event Created: {link}")

@cli.command()
@click.option("--meeting-id", required=True, help="Zoom meeting ID for which to fetch the transcript")
@click.option("--category-id", default=63, help="Discourse category ID to post transcript (default 63)")
def publish_transcript(meeting_id, category_id):
    """
    Fetch a transcript from a Zoom call and upload it to Discourse as a new topic.

    Example usage:
        python -m modules.cli publish-transcript --meeting-id 123456789 \
          --category-id 63
    """
    # This helper function calls Zoom to fetch the transcript text
    # and then calls Discourse to create a topic with that transcript.
    discourse_topic = transcript.post_zoom_transcript_to_discourse(
        meeting_id=meeting_id,
        category_id=category_id
    )
    topic_id = discourse_topic.get("topic_id")
    click.echo(f"Transcript posted to Discourse with topic_id={topic_id}")

if __name__ == "__main__":
    cli()
