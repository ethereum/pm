# ACDbot

ACDbot (AllCoreDevs Bot) is a suite of Python scripts and GitHub Actions workflows designed to automate the logistics surrounding Ethereum protocol meetings (like All Core Developers calls, Consensus Layer calls, etc.). It handles scheduling, communication, and post-meeting tasks based on GitHub issues raised in the `ethereum/pm` repository.

## Features

-   **Automated Scheduling:** Creates Zoom meetings and Google Calendar events based on information provided in GitHub issues.
-   **Issue Templates:** Utilizes specific [Recurring Protocol Call](/.github/ISSUE_TEMPLATE/recurring-protocol-calls.md) and [One-Time Protocol Call](/.github/ISSUE_TEMPLATE/onetime-protocol-call.md) templates for structured input.
-   **Discourse Integration:** Creates or updates topics on the Ethereum Magicians forum (or other configured Discourse instances) with meeting agendas and details extracted from the GitHub issue.
-   **YouTube Integration:**
    -   Optionally creates YouTube live stream events for recurring meetings (up to 4 future occurrences).
    -   Automatically uploads meeting recordings to YouTube for one-time meetings or recurring meetings where live streaming wasn't requested.
-   **Transcript Processing:** Polls Zoom for meeting transcripts, downloads them when available, and posts them to the corresponding Discourse topic.
-   **Notifications:** Sends Zoom join links to the designated facilitator via email. Posts updates (YouTube links, transcript links) to Discourse and Telegram.
-   **State Management:** Uses a `meeting_topic_mapping.json` file to track the relationship between GitHub issues, Zoom meetings, Discourse topics, Google Calendar events, and YouTube videos/streams.
-   **Duplicate Prevention:** Prevents creation of duplicate Zoom/Calendar events for the same recurring call series by checking the `Call series` field in the issue and the mapping file.
-   **RSS Feed:** Generates an RSS feed summarizing meeting events and artifacts.
-   **Robust Error Handling:** Includes mechanisms for handling API errors, token refreshes (Zoom, YouTube), and provides feedback via issue comments and logs.

## Workflow

The primary workflow is triggered by GitHub issues:

1.  **Issue Creation:** A user creates a new issue in the `ethereum/pm` repository using one of the designated templates (`recurring-protocol-calls.md` or `onetime-protocol-call.md`). Key fields include:
    *   Meeting title, date, time, duration.
    *   `Recurring meeting` (true/false).
    *   `Occurrence rate` (weekly, bi-weekly, monthly) for recurring meetings.
    *   `Call series` (e.g., ACDE, ACDC) for recurring meetings to link related issues.
    *   `Already on Ethereum Calendar` (true/false) to optionally skip Zoom/GCal creation.
    *   `Need YouTube stream links` (true/false) for recurring meetings.
    *   Facilitator email.
2.  **GitHub Action Trigger (`issue-workflow.yml`):** When an issue with the `recurring` or `onetime` label is opened or edited, this workflow runs.
3.  **Issue Handling (`handle_issue.py`):** This core script performs the main automation tasks:
    *   **Parses Issue:** Extracts details from the issue body using regex.
    *   **Loads Mapping:** Reads the `meeting_topic_mapping.json` file.
    *   **Checks for Duplicates:**
        *   If it's a recurring meeting, checks if an entry with the same `call_series` already exists in the mapping. If yes, sets `already_on_calendar` to true to prevent duplicate Zoom/GCal events.
        *   Checks if YouTube streams already exist for the `call_series`.
    *   **Discourse:** Creates a new Discourse topic or updates an existing one (if found via the mapping file) with the issue title, body, and a link back to the GitHub issue. Adds existing YouTube stream links if found.
    *   **Zoom:**
        *   If `already_on_calendar` is false, creates a new Zoom meeting (one-time or recurring based on issue fields). Handles the bi-weekly scheduling quirk.
        *   If a meeting exists in the mapping for this *specific issue*, updates it if the time/duration changed.
        *   Stores the Zoom `meeting_id` and `join_url`.
    *   **Google Calendar:**
        *   If `already_on_calendar` is false, creates a new Google Calendar event (one-time or recurring).
        *   If an event exists in the mapping for this *specific issue*, updates it.
        *   Stores the `calendar_event_id`.
    *   **YouTube Streams:**
        *   If it's a recurring meeting and `Need YouTube stream links` is true:
            *   If existing streams for the `call_series` were found, reuses them.
            *   Otherwise, calls `youtube_utils.create_recurring_streams` to create 4 upcoming stream events.
            *   Sets `skip_youtube_upload` flag to `true` in the mapping.
            *   Adds stream links to the comment and Discourse post.
        *   If streams are not needed or it's a one-time call, sets `skip_youtube_upload` to `false`.
    *   **Notifications:** Sends the Zoom link to the facilitator's email address.
    *   **Updates Mapping:** Saves the updated `meeting_topic_mapping.json` with details like `meeting_id`, `discourse_topic_id`, `calendar_event_id`, `youtube_streams` (if any), `call_series`, `skip_youtube_upload`, etc., keyed by the Zoom `meeting_id`.
    *   **Comments on Issue:** Posts a summary comment on the GitHub issue with links to the Discourse topic, Google Calendar event, Zoom details, and YouTube streams (if created).
    *   **Commits Mapping:** Commits the updated `meeting_topic_mapping.json` back to the repository.
4.  **Post-Meeting Workflows:**
    *   **YouTube Upload (`youtube-uploader.yml`, `upload_zoom_recording.py`):**
        *   Periodically checks the mapping file for meetings that have finished.
        *   For meetings where `skip_youtube_upload` is `false`, it downloads the MP4 recording from Zoom.
        *   Uploads the recording to YouTube using `youtube_utils`.
        *   Updates the mapping file with `youtube_video_id` and marks `Youtube_upload_processed` as true.
        *   Posts the YouTube link to the Discourse topic and Telegram.
        *   Updates the RSS feed.
        *   Commits the mapping file.
    *   **Transcript Polling (`zoom-transcript-poll.yml`, `poll_zoom_recordings.py`):**
        *   Periodically polls the Zoom API for completed recordings and available transcripts for recent meetings listed in the mapping file.
        *   If a transcript (`.vtt`) is found and not already processed (`transcript_processed` is false):
            *   Downloads the transcript.
            *   Posts the transcript content to the Discourse topic.
            *   (Future enhancement: Could generate an LLM summary here).
            *   Updates the mapping file, setting `transcript_processed` to true.
            *   Updates the RSS feed.
            *   Commits the mapping file.
    *   **RSS Feed Generation (`rss-feed-generator.yml`, `serve_rss.py`):**
        *   Periodically runs `serve_rss.py` which uses `rss_utils.py` to read the mapping file and generate/update an RSS feed file (`meetings_rss.xml`) based on the meeting data and artifact links (YouTube, Discourse, etc.).
        *   Commits the updated RSS file.

## Configuration

Configuration relies heavily on GitHub Actions secrets and a mapping file.

### GitHub Secrets

The workflows require the following secrets to be set in the `ethereum/pm` repository's Settings -> Secrets and variables -> Actions:

-   `ACDBOT_GITHUB_TOKEN`: A GitHub Personal Access Token (PAT) with `repo` and `workflow` scopes to allow workflows to commit changes (like the mapping file) and potentially trigger other workflows. **Do not use the default `GITHUB_TOKEN`**.
-   `ZOOM_ACCOUNT_ID`, `ZOOM_CLIENT_ID`, `ZOOM_CLIENT_SECRET`: Credentials for a Zoom Server-to-Server OAuth app.
-   `ZOOM_REFRESH_TOKEN_PATH`: Path within the repository where the Zoom refresh token is stored (e.g., `.github/ACDbot/zoom_refresh_token.txt`). The token itself is managed automatically.
-   `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`: Credentials for a Google Cloud OAuth 2.0 Client ID (Web application type).
-   `YOUTUBE_REFRESH_TOKEN_PATH`: Path within the repository where the YouTube/Google refresh token is stored (e.g., `.github/ACDbot/youtube_refresh_token.txt`). Requires manual refresh process initially or upon expiry (see Google OAuth docs).
-   `DISCOURSE_API_KEY`, `DISCOURSE_API_USERNAME`: Credentials for a Discourse user with API access.
-   `DISCOURSE_BASE_URL`: The base URL of the target Discourse instance (e.g., `https://ethereum-magicians.org`).
-   `SENDER_EMAIL`, `SENDER_PASSWORD`: Credentials for the email account used to send facilitator notifications. Consider using an App Password if using Gmail with 2FA.
-   `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`: Credentials for a Telegram bot and the target chat ID for notifications.

### Core Files

-   `.github/ACDbot/meeting_topic_mapping.json`: This JSON file acts as the central database, storing the state and linking IDs across different services (GitHub Issue -> Zoom Meeting ID -> Discourse Topic ID -> GCal Event ID -> YouTube Video/Stream ID -> Call Series). It's crucial for tracking meetings and preventing duplicates. It is automatically updated and committed by the workflows.
-   `.github/ACDbot/scripts/client_secrets.json`: Contains the Google Cloud OAuth client secrets (downloaded from Google Cloud Console). It's used alongside the refresh token for YouTube/GCal authentication. This file *should* be committed to the repository as it only contains client identifiers, not user credentials.
-   Token files (e.g., `zoom_refresh_token.txt`, `youtube_refresh_token.txt`): These store the active refresh tokens and are managed by the scripts/workflows.

## Key Scripts and Modules

-   **Scripts (`.github/ACDbot/scripts/`):**
    -   `handle_issue.py`: Main script for processing GitHub issues.
    -   `upload_zoom_recording.py`: Handles downloading recordings and uploading to YouTube.
    -   `poll_zoom_recordings.py`: Polls Zoom for recordings and transcripts.
    -   `serve_rss.py`: Generates the RSS feed.
    -   `get_zoom_token.py`, `direct_token_exchange.py`, `get_refresh_token.py`: Utilities for managing Zoom OAuth tokens.
    -   `refresh_youtube_token.py`: Utility for refreshing the YouTube/Google token (often run manually or via a separate workflow).
-   **Modules (`.github/ACDbot/modules/`):** Contain reusable functions for interacting with external APIs and performing specific tasks.
    -   `zoom.py`: Zoom API interactions (create/update meetings, get recordings/transcripts).
    -   `gcal.py`: Google Calendar API interactions.
    -   `discourse.py`: Discourse API interactions.
    *   `youtube_utils.py`: YouTube Data API interactions (upload videos, create streams).
    *   `email_utils.py`: Sending emails.
    *   `tg.py`: Sending Telegram messages.
    *   `rss_utils.py`: Generating RSS feed data.
    *   `transcript.py`: Transcript processing utilities.

## Troubleshooting

-   **Token Expiry:** Zoom and Google refresh tokens can expire or be revoked. Ensure refresh mechanisms are working or manually refresh tokens if needed. Check workflow logs for authentication errors.
-   **API Permissions:** Ensure the OAuth apps (Zoom, Google) have the necessary scopes/permissions enabled (e.g., `meeting:write`, `recording:read`, `calendar.events`, `youtube.upload`).
-   **Mapping File Conflicts:** If multiple workflows try to write to `meeting_topic_mapping.json` simultaneously, merge conflicts might occur. Workflows generally run sequentially for a given issue, but concurrent runs on different issues could potentially conflict if git operations overlap heavily.
-   **GitHub Actions Logs:** The primary source for debugging. Check the output of workflow runs for error messages and `[DEBUG]` statements printed by the scripts.
-   **Rate Limits:** Frequent API calls might hit rate limits for Zoom, Google, or Discourse. The scripts generally don't include sophisticated rate limit handling.

