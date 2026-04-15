#!/usr/bin/env python3
"""
Manual meeting asset ingest script.

Handles the scenario where a meeting was recorded on a personal Zoom account
(or other non-standard source) and assets need to be placed into the pipeline
manually.

Expects transcript.vtt (and optionally chat.txt) to already exist in the
artifact directory: artifacts/{series}/{date}_{number_zfill3}/

Usage:
    python ingest_manual_meeting.py \
        --series fcr --number 5 \
        --youtube-url "https://youtube.com/watch?v=XXXXX" \
        --summarize --auto-approve
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlparse

SCRIPT_DIR = Path(__file__).parent
ACDBOT_DIR = SCRIPT_DIR.parent
PIPELINE_DIR = SCRIPT_DIR / "asset_pipeline"
ARTIFACTS_DIR = ACDBOT_DIR / "artifacts"
MAPPING_FILE = ACDBOT_DIR / "meeting_topic_mapping.json"

# modules/ needs to be on path for bare imports inside functions (mapping_manager)
sys.path.insert(0, str(ACDBOT_DIR / "modules"))


def resolve_occurrence(series: str, number: int):
    """Look up a meeting occurrence from the mapping file.

    Returns (occurrence_dict, series_key, issue_number, date, discourse_topic_id)
    or raises SystemExit on failure.
    """
    from mapping_manager import MappingManager

    manager = MappingManager(str(MAPPING_FILE))
    series_data = manager.get_call_series(series)
    if not series_data:
        print(f"Error: series '{series}' not found in mapping file.")
        sys.exit(1)

    for occ in series_data.get("occurrences", []):
        issue_title = occ.get("issue_title", "")
        match = re.search(r"#\s*(\d+)", issue_title)
        occ_number = int(match.group(1)) if match else occ.get("occurrence_number")
        if occ_number == number:
            date = occ.get("start_time", "").split("T")[0]
            return occ, series, occ.get("issue_number"), date, occ.get("discourse_topic_id")

    print(f"Error: occurrence #{number} not found in series '{series}'.")
    sys.exit(1)


def get_meeting_dir(series: str, date: str, number: int) -> Path:
    """Return the expected artifact directory path."""
    return ARTIFACTS_DIR / series / f"{date}_{str(number).zfill(3)}"


def extract_youtube_video_id(url: str) -> str:
    """Extract the video ID from a YouTube URL."""
    parsed = urlparse(url)
    if parsed.hostname in ("youtube.com", "www.youtube.com"):
        qs = parse_qs(parsed.query)
        if "v" in qs:
            return qs["v"][0]
    if parsed.hostname == "youtu.be":
        return parsed.path.lstrip("/")
    print(f"Error: could not extract video ID from YouTube URL: {url}")
    sys.exit(1)


def run_pipeline_step(description: str, cmd: list[str], dry_run: bool,
                      check: bool = True) -> bool:
    """Run a single pipeline step via subprocess."""
    if dry_run:
        print(f"  [dry-run] {description}: {' '.join(cmd)}")
        return True

    print(f"\n  {description}")
    print(f"  Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=PIPELINE_DIR)
    if result.returncode != 0:
        if check:
            print(f"  Warning: step failed with code {result.returncode}")
            return False
        else:
            print(f"  Warning: step had issues (code {result.returncode}), continuing...")
    return True


def run_pipeline(series: str, number: int, meeting_dir: Path, summarize: bool,
                 auto_approve: bool, dry_run: bool) -> bool:
    """Run changelog generation, corrections, and optional summary.

    Skips the Zoom download step (files are already in place).
    """
    changelog_path = meeting_dir / "transcript_changelog.tsv"

    # Step 1: Generate changelog (if not already present)
    if changelog_path.exists():
        print(f"  Changelog already exists, skipping generation")
    else:
        cmd = [sys.executable, "generate_changelog.py",
               "--call", series, "--number", str(number)]
        if not run_pipeline_step("Generating changelog...", cmd, dry_run):
            return False

    # Step 2: Apply corrections
    if auto_approve:
        print(f"  Auto-approve mode: applying corrections without review")
    cmd = [sys.executable, "apply_changelog.py",
           "--call", series, "--number", str(number)]
    if not run_pipeline_step("Applying corrections...", cmd, dry_run):
        return False

    # Step 3: Generate summary (optional)
    if summarize:
        cmd = [sys.executable, "generate_summary.py",
               "--call", series, "--number", str(number)]
        run_pipeline_step("Generating summary...", cmd, dry_run, check=False)

    return True


def update_youtube_metadata(series: str, issue_number: int, youtube_url: str,
                            dry_run: bool):
    """Update mapping with YouTube video ID and processing flags."""
    from mapping_manager import MappingManager

    video_id = extract_youtube_video_id(youtube_url)
    update_data = {
        "youtube_video_id": video_id,
        "youtube_upload_processed": True,
        "skip_youtube_upload": True,
    }

    if dry_run:
        print(f"  [dry-run] Would update mapping for issue #{issue_number}:")
        for k, v in update_data.items():
            print(f"            {k}: {v}")
        return

    manager = MappingManager(str(MAPPING_FILE))
    if manager.update_occurrence(series, issue_number, update_data):
        manager.save_mapping()
        print(f"  Updated mapping: youtube_video_id={video_id}")
    else:
        print(f"  Warning: failed to update mapping for issue #{issue_number}")


def mark_transcript_processed(series: str, issue_number: int, dry_run: bool):
    """Set transcript_processed=True in the mapping."""
    from mapping_manager import MappingManager

    if dry_run:
        print(f"  [dry-run] Would set transcript_processed=True for issue #{issue_number}")
        return

    manager = MappingManager(str(MAPPING_FILE))
    if manager.update_occurrence(series, issue_number, {"transcript_processed": True}):
        manager.save_mapping()
        print(f"  Marked transcript_processed=True for issue #{issue_number}")
    else:
        print(f"  Warning: failed to mark transcript processed for issue #{issue_number}")


def regenerate_manifest(dry_run: bool):
    """Run generate_manifest.py to rebuild manifest.json."""
    cmd = [sys.executable, "generate_manifest.py"]
    if dry_run:
        print(f"  [dry-run] Would run: {' '.join(cmd)}")
        return
    print(f"  Running: {' '.join(cmd)}")
    subprocess.run(cmd, cwd=PIPELINE_DIR)


def main():
    parser = argparse.ArgumentParser(
        description="Manually ingest meeting assets into the pipeline."
    )
    parser.add_argument("--series", "-s", required=True,
                        help="Call series key (e.g., fcr)")
    parser.add_argument("--number", "-n", type=int, required=True,
                        help="Meeting number (e.g., 5)")
    parser.add_argument("--youtube-url", type=str,
                        help="YouTube URL to record in mapping")
    parser.add_argument("--summarize", action="store_true",
                        help="Generate tldr.json after corrections")
    parser.add_argument("--auto-approve", action="store_true",
                        help="Skip interactive changelog review")
    parser.add_argument("--skip-pipeline", action="store_true",
                        help="Skip transcript correction pipeline")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would happen without making changes")
    args = parser.parse_args()

    # Step 1: Resolve meeting metadata
    print(f"Resolving {args.series} #{args.number} from mapping...")
    occ, series, issue_number, date, discourse_topic_id = resolve_occurrence(
        args.series, args.number
    )
    print(f"  Found: issue #{issue_number}, date={date}, discourse_topic={discourse_topic_id}")

    # Step 2: Verify artifact directory and transcript exist
    meeting_dir = get_meeting_dir(series, date, args.number)
    transcript_path = meeting_dir / "transcript.vtt"
    if not transcript_path.exists():
        print(f"\nError: transcript not found at expected path:\n  {transcript_path}")
        print(f"\nPlace transcript.vtt (and optionally chat.txt) in:\n  {meeting_dir}/")
        sys.exit(1)
    print(f"  Artifacts dir: {meeting_dir}")

    actions_taken = []

    # Step 3: Run transcript pipeline
    pipeline_ok = False
    if not args.skip_pipeline:
        print("\nRunning transcript pipeline...")
        pipeline_ok = run_pipeline(
            series, args.number, meeting_dir, args.summarize, args.auto_approve,
            args.dry_run
        )
        if pipeline_ok or args.dry_run:
            actions_taken.append("Ran transcript correction pipeline")

    # Step 4: Update YouTube metadata
    if args.youtube_url:
        print("\nUpdating YouTube metadata...")
        update_youtube_metadata(series, issue_number, args.youtube_url, args.dry_run)
        actions_taken.append("Updated YouTube metadata in mapping")

    # Step 5: Mark transcript processed
    if pipeline_ok or args.dry_run:
        print("\nMarking transcript as processed...")
        mark_transcript_processed(series, issue_number, args.dry_run)
        actions_taken.append("Marked transcript as processed")

    # Step 6: Regenerate manifest
    if actions_taken:
        print("\nRegenerating manifest...")
        regenerate_manifest(args.dry_run)
        actions_taken.append("Regenerated manifest")

    # Summary
    print("\n" + "=" * 50)
    if args.dry_run:
        print("DRY RUN COMPLETE - no changes were made.")
    else:
        print("Done! Actions taken:")
        for action in actions_taken:
            print(f"  - {action}")
        print("\nRemaining steps:")
        print("  - Review generated artifacts")
        print("  - git add, commit, and push changes")


if __name__ == "__main__":
    main()
