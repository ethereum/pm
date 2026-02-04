#!/usr/bin/env python3
"""
Generate a manifest.json file listing all available call artifacts.

This manifest is consumed by forkcast to know what resources exist.
"""

import argparse
import json
import re
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).parent
ACDBOT_DIR = SCRIPT_DIR.parent.parent
ARTIFACTS_DIR = ACDBOT_DIR / "artifacts"
CALL_SERIES_CONFIG = ACDBOT_DIR / "call_series_config.yml"
MAPPING_FILE = ACDBOT_DIR / "meeting_topic_mapping.json"
MANIFEST_PATH = ARTIFACTS_DIR / "manifest.json"

# Known resource files and their types
RESOURCE_FILES = {
    "transcript.vtt": "transcript",
    "transcript_corrected.vtt": "transcript_corrected",
    "transcript_changelog.tsv": "changelog",
    "chat.txt": "chat",
    "summary.json": "summary",
    "tldr.json": "tldr",
}


def load_call_series_config() -> dict:
    """Load call series configuration from YAML."""
    if not CALL_SERIES_CONFIG.exists():
        return {}

    with open(CALL_SERIES_CONFIG, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    return config.get("call_series", {})


def load_mapping_file() -> dict:
    """Load the meeting topic mapping file."""
    if not MAPPING_FILE.exists():
        return {}

    try:
        with open(MAPPING_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def get_youtube_video_url(occurrence: dict) -> str | None:
    """Extract YouTube video URL from occurrence data."""
    # Check for uploaded video ID first (preferred)
    if occurrence.get('youtube_video_id'):
        return f"https://www.youtube.com/watch?v={occurrence['youtube_video_id']}"

    # Check for stream URLs in youtube_streams
    youtube_streams = occurrence.get('youtube_streams')
    if youtube_streams and isinstance(youtube_streams, list) and len(youtube_streams) > 0:
        stream_url = youtube_streams[0].get('stream_url')
        if stream_url:
            return stream_url

    return None


def find_occurrence_in_mapping(mapping: dict, series_id: str, date: str) -> dict | None:
    """Find an occurrence in the mapping file by series and date."""
    series_data = mapping.get(series_id, {})
    for occurrence in series_data.get('occurrences', []):
        start_time = occurrence.get('start_time', '')
        if start_time and start_time.startswith(date):
            return occurrence
    return None


def parse_call_directory(dir_name: str) -> tuple[str, int | None]:
    """
    Parse a call directory name into (date, number).

    Examples:
        "2024-12-12_226" -> ("2024-12-12", 226)
        "2024-12-12" -> ("2024-12-12", None)
    """
    match = re.match(r'^(\d{4}-\d{2}-\d{2})(?:_(\d+))?$', dir_name)
    if match:
        date = match.group(1)
        number = int(match.group(2)) if match.group(2) else None
        return date, number
    return None, None


def get_call_resources(call_dir: Path) -> dict[str, str]:
    """Get available resources for a call directory."""
    resources = {}
    for filename, resource_type in RESOURCE_FILES.items():
        filepath = call_dir / filename
        if filepath.exists():
            resources[resource_type] = filename
    return resources


def generate_manifest() -> dict:
    """Generate the complete manifest."""
    call_series_config = load_call_series_config()
    mapping = load_mapping_file()

    manifest = {
        "version": 1,
        "series": {}
    }

    # Scan artifacts directory for series
    if not ARTIFACTS_DIR.exists():
        return manifest

    for series_dir in sorted(ARTIFACTS_DIR.iterdir()):
        if not series_dir.is_dir():
            continue

        series_id = series_dir.name

        # Get series metadata from config
        series_config = call_series_config.get(series_id, {})
        display_name = series_config.get("display_name", series_id)
        youtube_playlist = series_config.get("youtube_playlist_id")

        calls = []

        # Scan call directories
        for call_dir in sorted(series_dir.iterdir(), reverse=True):
            if not call_dir.is_dir():
                continue

            date, number = parse_call_directory(call_dir.name)
            if not date:
                continue

            resources = get_call_resources(call_dir)
            if not resources:
                continue  # Skip empty directories

            call_entry = {
                "date": date,
                "path": f"{series_id}/{call_dir.name}",
                "resources": resources,
            }

            if number is not None:
                call_entry["number"] = number

            # Look up issue number and video URL from mapping file
            occurrence = find_occurrence_in_mapping(mapping, series_id, date)
            if occurrence:
                if occurrence.get("issue_number"):
                    call_entry["issue"] = occurrence["issue_number"]
                video_url = get_youtube_video_url(occurrence)
                if video_url:
                    call_entry["videoUrl"] = video_url

            calls.append(call_entry)

        if calls:
            manifest["series"][series_id] = {
                "name": display_name,
                "youtubePlaylist": youtube_playlist,
                "calls": calls,
            }

    return manifest


def main():
    parser = argparse.ArgumentParser(
        description='Generate manifest.json for call artifacts',
        epilog='Example: python generate_manifest.py'
    )
    parser.add_argument('--output', '-o', type=Path, default=MANIFEST_PATH,
                        help=f'Output path (default: {MANIFEST_PATH})')
    parser.add_argument('--dry-run', action='store_true',
                        help='Print manifest to stdout without writing')
    args = parser.parse_args()

    manifest = generate_manifest()

    # Count totals
    total_series = len(manifest["series"])
    total_calls = sum(len(s["calls"]) for s in manifest["series"].values())

    if args.dry_run:
        print(json.dumps(manifest, indent=2))
    else:
        # Ensure output directory exists
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2)
        print(f"Generated {args.output}")

    print(f"  {total_series} series, {total_calls} calls")


if __name__ == '__main__':
    main()
