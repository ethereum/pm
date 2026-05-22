#!/usr/bin/env python3
"""Run a one-off Recall.ai gallery_view_v2 capture test.

This is intentionally a manual spike harness. Production integration should use
scheduled bots and Recall webhooks instead of API polling.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

import requests


DEFAULT_RECALL_API_BASE = "https://us-east-1.recall.ai/api/v1"


def build_create_bot_payload(
    *,
    meeting_url: str,
    bot_name: str,
    screenshare_mode: str,
    rtmp_url: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    recording_config: dict[str, Any] = {
        "video_mixed_mp4": {},
        "video_mixed_layout": "gallery_view_v2",
        "video_mixed_participant_video_when_screenshare": screenshare_mode,
    }

    if rtmp_url:
        recording_config["video_mixed_flv"] = {}
        recording_config["realtime_endpoints"] = [
            {
                "type": "rtmp",
                "url": rtmp_url,
                "events": ["video_mixed_flv.data"],
            }
        ]

    payload: dict[str, Any] = {
        "meeting_url": meeting_url,
        "bot_name": bot_name,
        "recording_config": recording_config,
        "metadata": metadata or {"purpose": "acd-gallery-v2-spike"},
    }

    return payload


def find_video_mixed_download_url(bot: dict[str, Any]) -> str | None:
    for recording in bot.get("recordings", []):
        video_mixed = recording.get("media_shortcuts", {}).get("video_mixed")
        if not video_mixed:
            continue

        data = video_mixed.get("data") or {}
        download_url = data.get("download_url")
        status_code = (video_mixed.get("status") or {}).get("code")
        if download_url and status_code == "done":
            return download_url

    return None


def recall_headers(api_key: str) -> dict[str, str]:
    return {
        "Authorization": api_key,
        "accept": "application/json",
        "content-type": "application/json",
    }


def create_bot(api_base: str, api_key: str, payload: dict[str, Any]) -> dict[str, Any]:
    response = requests.post(
        f"{api_base.rstrip('/')}/bot/",
        headers=recall_headers(api_key),
        json=payload,
        timeout=30,
    )
    if not response.ok:
        raise RuntimeError(f"Recall create bot failed: HTTP {response.status_code} {response.text}")

    return response.json()


def retrieve_bot(api_base: str, api_key: str, bot_id: str) -> dict[str, Any]:
    response = requests.get(
        f"{api_base.rstrip('/')}/bot/{bot_id}/",
        headers=recall_headers(api_key),
        timeout=30,
    )
    if not response.ok:
        raise RuntimeError(f"Recall retrieve bot failed: HTTP {response.status_code} {response.text}")

    return response.json()


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def download_file(url: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with requests.get(url, stream=True, timeout=30) as response:
        response.raise_for_status()
        with output_path.open("wb") as output:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    output.write(chunk)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a Recall.ai gallery_view_v2 capture spike")
    parser.add_argument("--meeting-url", required=True, help="Zoom meeting URL for the bot to join")
    parser.add_argument("--output-dir", default="recall-spike-output", help="Directory for metadata and MP4 output")
    parser.add_argument("--api-base", default=os.environ.get("RECALL_API_BASE", DEFAULT_RECALL_API_BASE))
    parser.add_argument("--bot-name", default="Ethereum ACD Recorder Test")
    parser.add_argument(
        "--screenshare-mode",
        choices=["beside", "overlap", "hide"],
        default="beside",
        help="How participant video/gallery should appear while screen share is active",
    )
    parser.add_argument("--rtmp-url", default=os.environ.get("RECALL_RTMP_URL"))
    parser.add_argument("--poll", action="store_true", help="Poll until Recall exposes the mixed MP4 download URL")
    parser.add_argument("--poll-interval", type=int, default=30)
    parser.add_argument("--timeout-minutes", type=int, default=120)
    parser.add_argument("--download", action="store_true", help="Download the mixed MP4 when it is ready")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    api_key = os.environ.get("RECALL_API_KEY")
    if not api_key:
        print("RECALL_API_KEY is required", file=sys.stderr)
        return 2

    output_dir = Path(args.output_dir)
    payload = build_create_bot_payload(
        meeting_url=args.meeting_url,
        bot_name=args.bot_name,
        screenshare_mode=args.screenshare_mode,
        rtmp_url=args.rtmp_url,
    )
    write_json(output_dir / "create_bot_payload.json", payload)

    print("[INFO] Creating Recall bot with gallery_view_v2 layout")
    print(f"[INFO] RTMP streaming enabled: {bool(args.rtmp_url)}")
    bot = create_bot(args.api_base, api_key, payload)
    write_json(output_dir / "create_bot_response.json", bot)

    bot_id = bot.get("id")
    if not bot_id:
        raise RuntimeError("Recall create bot response did not include an id")

    print(f"[INFO] Recall bot id: {bot_id}")
    if not args.poll:
        print("[INFO] Bot created. Re-run with --poll after the meeting ends to fetch the MP4 URL.")
        return 0

    deadline = time.monotonic() + args.timeout_minutes * 60
    while time.monotonic() < deadline:
        bot = retrieve_bot(args.api_base, api_key, bot_id)
        write_json(output_dir / "retrieve_bot_response.json", bot)
        status = (bot.get("status") or {}).get("code")
        download_url = find_video_mixed_download_url(bot)

        print(f"[INFO] Bot status: {status or 'unknown'}; mixed video ready: {bool(download_url)}")
        if download_url:
            (output_dir / "video_mixed_download_url.txt").write_text(download_url + "\n", encoding="utf-8")
            if args.download:
                output_path = output_dir / "recall-gallery-v2.mp4"
                print(f"[INFO] Downloading mixed MP4 to {output_path}")
                download_file(download_url, output_path)
            return 0

        time.sleep(args.poll_interval)

    print("[ERROR] Timed out waiting for Recall mixed MP4", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
