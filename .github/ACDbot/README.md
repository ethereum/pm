# ACDbot

ACDbot is a suite of Python scripts and GitHub Actions workflows designed to automate the logistics of Ethereum protocol meetings in this repository. Calls are scheduled by creating an issue, parsed by the bot which creates EthMagicians thread, Youtube stream and later publishes transcript or a summary.

> [!WARNING]
> ACDBot contains bugs and is currently being refactored. Be aware of potential issues when using it and always check its outputs.

## Features

-   Creates **Zoom meeting links, Google Calendar events and EthMagicians posts** based on information in issue created with templates for [Protocol Call Form](/.github/ISSUE_TEMPLATE/protocol-call-form.yml).
-   Optionally creates **YouTube live stream** for recurring meetings (up to 4 future events) and automatically uploads recordings afterwards.
-   Polls Zoom for **meeting transcripts**, downloads them when available, and posts them to the corresponding Discourse topic with optional summary.
-   Generates an **RSS feed** summarizing meeting events and links.

## Usage

The bot can be used to create meetings by creating an issue in this repository. A workflow action will be triggered that parses information from the issue and runs scripts to create meeting posts and links.

When creating a new issue, use the predetermined templates for setting up a recurring or one-time call. Fill the template and follow the suggested format to avoid issues. You can always edit the issue and the bot will be triggered to update the meeting. It will also automatically check for same existing events to avoid duplicates.

### Creating a meeting

To schedule a call using ACDbot, simply open an issue using given templates and fill all fields:

* Meeting title, date, time, duration. (Make sure to use correct datetime format to avoid parsing issues)
* `Recurring meeting` (true/false) and their `Occurrence rate`
* `Call series` (e.g., ACDE, ACDC) name for recurring meetings
* `Already on Ethereum Calendar` (true/false) to optionally skip Zoom/GCal creation
* `Need YouTube stream links`, set false if you don't want YouTube stream
* Facilitator email for contact

Based on options you chose, this will automatically create a new EthMagicians topic or updates an existing one (if editing existing meeting) with the meeting title, body, and a link back to the GitHub issue. This includes created Zoom link and Youtube stream which will be posted also as a comment under the issue. The Zoom link is also sent to the facilitator's email address.

### After the call

The bot monitors all existing issues and when meeting concluded, it pulls transcript and recording from Zoom to upload them. It automatically posts a summary comment on the GitHub issue and link to the recording. This is done by running a cron job every 6 hours, it doesn't happen immediately after the meeting.

These workflows like uploading recording and transcript can be also triggered manually in Github Action tab.

## Troubleshooting

ACDbot is maintained by EF Protocol Support support team. Before contacting maintainers, check whether the workflow failed in Actions tab and at which step an issue occurred. All logs and errors printed by bot can be found in corresponding action workflow.

- **Fail when creating a meeting**
    - Make sure you filled the template in correct format. This can be caused by format issue, expired tokens or a bug in the bot itself. Check the failed workflow to see the error output.
- **Fail to post transcript**
    - Transcript is not pulled right away but after couple of hours. Bot connects to Zoom to fetch the transcript, it only works with configured Zoom account credentials. If you are using correct account, make sure the transcript exists.
- **Fail to post Youtube recording**
    - The recording might not be available or permissions are not set correctly. Make sure the credentials correspond to the existing tokens and server is not rate limiting.
-  **Mapping File Conflicts**
    - The mapping json file is the main database of the bot. If multiple workflows try to write to `meeting_topic_mapping.json` simultaneously, merge conflicts might occur. Updates or different versions of the bot can cause issues in the file that need to be fixed by manual edit.

## Contributing

### Configuration

The bot in this repository is configured with existing accounts that facilitate Ethereum protocol meetings but can be customized for other use cases.

#### GitHub Secrets

Because this is Github Actions bot, it relies on admin configuring secret variables in the Github repository.

In Settings -> Secrets and variables -> Actions:

-   `ACDBOT_GITHUB_TOKEN`: A GitHub Personal Access Token (PAT) with limited `repo` and `workflow` scopes to allow workflows to commit changes and trigger other workflows. **Do not use the default `GITHUB_TOKEN`**.
-   `ZOOM_ACCOUNT_ID`, `ZOOM_CLIENT_ID`, `ZOOM_CLIENT_SECRET`: Credentials for a Zoom Server-to-Server OAuth app.
-   `ZOOM_REFRESH_TOKEN_PATH`: Path within the repository where the Zoom refresh token is stored (e.g., `.github/ACDbot/zoom_refresh_token.txt`). The token itself is managed automatically.
-   `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`: Credentials for a Google Cloud OAuth 2.0 Client ID (Web application type).
-   `YOUTUBE_REFRESH_TOKEN_PATH`: Path within the repository where the YouTube/Google refresh token is stored (e.g., `.github/ACDbot/youtube_refresh_token.txt`). Requires manual refresh process upon expiry (see Google OAuth docs).
-   `DISCOURSE_API_KEY`, `DISCOURSE_API_USERNAME`: Credentials for a Discourse user with API access.
-   `DISCOURSE_BASE_URL`: The base URL of the target Discourse instance (e.g., `https://ethereum-magicians.org`).
-   `SENDER_EMAIL`, `SENDER_PASSWORD`: Credentials for the email account used to send facilitator notifications. Consider using an App Password if using Gmail with 2FA.
-   `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`: Credentials for a Telegram bot and the target chat ID for notifications.

### Core files and flow

The database that keeps track of existing events is in `meeting_topic_mapping.json`. This JSON file stores the state and linking IDs across different services (GitHub Issue -> Zoom Meeting ID -> Discourse Topic ID -> GCal Event ID -> YouTube Video/Stream ID -> Call Series). It's crucial for tracking meetings and preventing duplicates. It is automatically updated and committed by the workflows.

-   **Scripts (`.github/ACDbot/scripts/`):**
    -   `handle_protocol_call.py`: Main script for processing GitHub issues using the new form-based workflow.
        - It parses the issue, loads mapping and checks for duplicates
        - Creates/updates EthMag topic and based on chosen options or existence of an event creates Zoom meeting ID, GCal event, YouTube stream
        - Comments on the issue with created artifacts, sends an email to facilitator and commits changes to mapping file
    -   `poll_zoom_recordings.py`, `upload_zoom_recording.py`, `zoom-transcript-poll.yml`
        - Scripts for downloading and uploading recordings/transcripts
        - Runs on a scheduled cron job every 6 hours (`0 */6 * * *`) to periodically check for finished meetings based on mapping and Zoom API
        *   Uploads the recording to YouTube using `youtube_utils`, uploads the transcript to EthMag topic
        *   Updates the mapping file with `youtube_video_id`, marks `youtube_upload_processed` and `transcript_processed` to true.
        *   Posts the YouTube link to the Discourse topic, updates the RSS feed and commits the mapping file.
        *   Can be manually triggered from GitHub Actions with a specific meeting ID.
       -   `serve_rss.py`:
        - Generates the RSS feed
        - Triggered automatically after the completion of issue handling, transcript polling, or YouTube upload workflows
        - Periodically runs `serve_rss.py` which uses `rss_utils.py` to read the mapping file and generate/update an RSS feed file (`meetings_rss.xml`) based on the meeting data and artifact links (YouTube, Discourse, etc.).
        *   Commits the updated RSS file.
    -   `get_zoom_token.py`, `direct_token_exchange.py`, `get_refresh_token.py`: Utilities for managing Zoom OAuth tokens.
    -   `refresh_youtube_token.py`: Utility for refreshing the YouTube/Google token (often run manually or via a separate workflow).
