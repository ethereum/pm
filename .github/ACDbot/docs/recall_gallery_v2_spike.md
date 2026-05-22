# Recall Gallery V2 Spike

This is a manual evaluation path for testing whether Recall.ai can replace a
human OBS operator for ACD livestream capture.

The goal is to validate three things before productionizing anything:

1. `gallery_view_v2` shows useful fallback tiles for participants with cameras off.
2. `beside` screen-share mode preserves the presentation while keeping participant presence visible.
3. The same bot can produce both a live RTMP stream and a post-meeting mixed MP4.

Relevant Recall docs:

- Video layouts: <https://docs.recall.ai/docs/video-layouts>
- RTMP mixed video: <https://docs.recall.ai/docs/stream-real-time-video-rtmp>
- Mixed MP4 recording: <https://docs.recall.ai/docs/receive-a-recording>
- Create Bot API: <https://docs.recall.ai/reference/bot_create>

## Manual Test

Use a test Zoom meeting with a few camera-off participants and at least one
screen share. If testing live output, use a private/unlisted YouTube stream or
another disposable RTMP destination.

```bash
cd .github/ACDbot
export RECALL_API_KEY="..."
export RECALL_RTMP_URL="rtmp://host/app/stream-key" # optional

uv run --locked python scripts/recall_gallery_v2_spike.py \
  --meeting-url "https://zoom.us/j/..." \
  --output-dir /tmp/recall-gallery-v2-spike \
  --screenshare-mode beside \
  --poll \
  --poll-interval 15 \
  --download
```

The script writes:

- `create_bot_payload.json`
- `create_bot_response.json`
- `retrieve_bot_response.json`
- `video_mixed_download_url.txt`
- `recall-gallery-v2.mp4` when `--download` is set and the MP4 is ready

## What Good Looks Like

The output is acceptable only if:

- Camera-off participants appear as readable fallback tiles.
- Screen share remains legible during presentation segments.
- Speaker identity is understandable without losing the group context.
- Audio stays in sync in the downloaded MP4.
- The RTMP stream can start without manual intervention once the bot joins.

## Production Notes

Recall recommends scheduled bots with `join_at` at least 10 minutes ahead for
production reliability. This spike script uses polling for convenience; a real
integration should use Recall bot status webhooks and should avoid storing RTMP
stream keys in logs or artifacts.

This is not intended to replace the current Zoom cloud recording stitch job yet.
That job remains the archive-first fallback while the live bot path is evaluated.
