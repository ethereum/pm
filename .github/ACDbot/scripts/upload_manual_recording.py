"""Upload a locally provided recording to YouTube for a specific occurrence.

Used for meetings recorded outside the org Zoom account (e.g. a personal Zoom),
where the normal pipeline has nothing to download. Mirrors the publishing
behaviour of upload_zoom_recording.upload_recording (title, description,
thumbnail, playlist, mapping update, notifications) but sources the video from a
local file. Deliberately does not import modules.zoom, so no Zoom credentials
are required.
"""

import argparse
import os
from pathlib import Path

import googleapiclient.http
from googleapiclient.errors import HttpError

from modules import discourse, tg, mattermost_notify
from modules.youtube_utils import add_video_to_appropriate_playlist, get_youtube_service
from modules.mapping_utils import (
    load_mapping as load_meeting_topic_mapping,
    save_mapping as save_meeting_topic_mapping,
    find_meeting_by_id,
    find_call_series_by_meeting_id,
    find_occurrence_with_index,
)

try:
    from modules import rss_utils
except ImportError:
    rss_utils = None

UPLOAD_THUMBNAIL_PATH = str(Path(__file__).resolve().parent.parent / "thumbnails" / "recording_thumbnail.png")


def upload_recording_manual(meeting_id, occurrence_issue_number, video_file, error_collector=None):
    """Upload ``video_file`` to YouTube for the given occurrence.

    Returns:
        True: Successfully uploaded
        False: Failed with error (should be reported)
        None: Expected skip (should not be reported)
    """
    meeting_id = str(meeting_id)

    if not os.path.exists(video_file):
        error_msg = f"❌ Manual YouTube upload aborted: video file not found: {video_file}"
        print(f"[ERROR] {error_msg}")
        if error_collector is not None:
            error_collector.append(error_msg)
        else:
            tg.send_message(error_msg)
        return False

    youtube = get_youtube_service()
    mapping = load_meeting_topic_mapping()

    series_entry = find_meeting_by_id(meeting_id, mapping)
    if not series_entry:
        error_msg = f"❌ Manual YouTube upload aborted: Unknown meeting_id {meeting_id} in mapping."
        print(f"[ERROR] {error_msg}")
        if error_collector is not None:
            error_collector.append(error_msg)
        else:
            tg.send_message(error_msg)
        return False

    call_series_key = find_call_series_by_meeting_id(meeting_id, occurrence_issue_number, mapping)
    if not call_series_key:
        print(f"[ERROR] Could not find call series for meeting {meeting_id}")
        return False

    matched_occurrence, occurrence_index = find_occurrence_with_index(
        call_series_key, occurrence_issue_number, mapping
    )
    if matched_occurrence is None:
        error_msg = f"❌ Manual YouTube upload aborted: Occurrence #{occurrence_issue_number} not found for meeting {meeting_id}."
        print(f"[ERROR] {error_msg}")
        if error_collector is not None:
            error_collector.append(error_msg)
        else:
            tg.send_message(error_msg)
        return False

    print(f"Processing MANUAL YouTube upload for Meeting ID {meeting_id}, Occurrence Issue #{occurrence_issue_number}")

    if matched_occurrence.get("skip_youtube_upload", False):
        print("  -> Skipping: Occurrence marked as skip_youtube_upload.")
        return None

    if matched_occurrence.get("youtube_upload_processed"):
        print("  -> Skipping: YouTube upload already processed for occurrence.")
        return None

    video_title = matched_occurrence.get("issue_title", f"Meeting {meeting_id} - Issue {occurrence_issue_number}")
    video_description = (
        f"Recording of {video_title}\n\n"
        f"GitHub Issue: https://github.com/{os.environ.get('GITHUB_REPOSITORY', '')}/issues/{occurrence_issue_number}"
    )

    try:
        request_body = {
            'snippet': {
                'title': video_title,
                'description': video_description,
                'categoryId': '28'
            },
            'status': {
                'privacyStatus': 'public',
            }
        }

        print(f"[INFO] Uploading provided video file: {video_file}")
        media = googleapiclient.http.MediaFileUpload(video_file, chunksize=-1, resumable=True)
        response = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=media
        ).execute()

        mapping[call_series_key]["occurrences"][occurrence_index]["youtube_video_id"] = response['id']
        mapping[call_series_key]["occurrences"][occurrence_index]["youtube_upload_processed"] = True
        save_meeting_topic_mapping(mapping)

        youtube_link = f"https://youtu.be/{response['id']}"
        print(f"Uploaded YouTube video: {youtube_link}")

        # Set custom thumbnail for uploaded recording
        if os.path.exists(UPLOAD_THUMBNAIL_PATH):
            try:
                thumbnail_response = youtube.thumbnails().set(
                    videoId=response['id'],
                    media_body=googleapiclient.http.MediaFileUpload(UPLOAD_THUMBNAIL_PATH)
                ).execute()
                print(f"[INFO] Successfully set custom thumbnail: {thumbnail_response['items'][0]['default']['url']}")
            except Exception as thumb_error:
                print(f"[WARN] Failed to set custom thumbnail: {thumb_error}")

        # Add video to appropriate playlist; must be done after upload is successful
        call_series = series_entry.get("call_series")
        if call_series:
            playlist_results = add_video_to_appropriate_playlist(response['id'], call_series)
            if playlist_results:
                print(f"[INFO] Successfully added video to {len(playlist_results)} playlist(s) for {call_series}")
            else:
                print(f"[WARN] Failed to add video to any playlist for {call_series}")
        else:
            print(f"[WARN] No call_series found for meeting {meeting_id}, skipping playlist assignment")

        # Post to Discourse (if applicable)
        discourse_topic_id = matched_occurrence.get("discourse_topic_id")
        if discourse_topic_id:
            discourse.create_post(
                topic_id=discourse_topic_id,
                body=f"YouTube recording available: {youtube_link}"
            )

        # Update RSS feed for this occurrence
        if rss_utils:
            try:
                rss_utils.add_notification_to_meeting(
                    meeting_id,
                    occurrence_issue_number,
                    "youtube_upload",
                    f"Meeting recording uploaded: {video_title}",
                    youtube_link
                )
                print(f"Updated RSS feed with YouTube video for occurrence #{occurrence_issue_number}")
            except Exception as e:
                print(f"Failed to update RSS feed: {e}")

        # Send Telegram + Mattermost notifications
        telegram_message = (
            f"✅ YouTube Upload Successful!\n\n"
            f"Title: {video_title}\n"
            f"URL: {youtube_link}"
        )
        try:
            tg.send_message(telegram_message)
            print("Telegram notification sent for YouTube upload.")
        except Exception as e:
            print(f"Error sending Telegram message for YouTube upload: {e}")

        try:
            mattermost_notify.send_mattermost_notification(telegram_message)
        except Exception as e:
            print(f"Error sending Mattermost message for YouTube upload: {e}")

        return True
    except HttpError as e:
        print(f"YouTube API error: {e}")
        err_text = getattr(e, 'content', None) or str(e)
        error_msg = f"❌ Manual YouTube upload failed for meeting {meeting_id} (issue #{occurrence_issue_number}).\nError: {err_text}"
        if error_collector is not None:
            error_collector.append(error_msg)
        else:
            tg.send_message(error_msg)
        return False


def main():
    parser = argparse.ArgumentParser(description="Upload a local recording file to YouTube for a specific occurrence")
    parser.add_argument("--meeting_id", required=True, help="Zoom meeting ID of the series occurrence")
    parser.add_argument("--occurrence_issue_number", required=True, type=int, help="Issue number of the occurrence")
    parser.add_argument("--video-file", required=True, help="Path to the local video file to upload")
    args = parser.parse_args()

    print(
        f"Attempting MANUAL upload for occurrence: Meeting ID {args.meeting_id}, "
        f"Issue #{args.occurrence_issue_number}, file {args.video_file}"
    )
    try:
        result = upload_recording_manual(args.meeting_id, args.occurrence_issue_number, args.video_file)
    except Exception as e:
        print(f"Failed manual upload for {args.meeting_id} / {args.occurrence_issue_number}: {e}")
        raise SystemExit(1)

    if result is False:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
