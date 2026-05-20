#!/usr/bin/env python3
"""
Asset Pipeline Orchestrator

Runs the full asset pipeline for a meeting:
1. Download assets from Zoom
2. Generate changelog of corrections using Claude
3. Pause for human review of changelog
4. Apply corrections to transcript
5. (Optional) Generate structured summary (tldr.json)
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from meeting_identity import get_occurrence_call_number
from utils import SCRIPT_DIR, ARTIFACTS_DIR

ACDBOT_DIR = SCRIPT_DIR.parent.parent
MAPPING_FILE = ACDBOT_DIR / "meeting_topic_mapping.json"


def load_mapping() -> dict | None:
    """Load the meeting topic mapping file."""
    if not MAPPING_FILE.exists():
        return None

    try:
        with open(MAPPING_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


def get_occurrence_date(occurrence: dict) -> str | None:
    """Return the YYYY-MM-DD date for a mapped occurrence."""
    start_time = occurrence.get('start_time', '')
    if not start_time:
        return None
    return start_time.split('T')[0]


def find_most_recent_from_mapping(call: str, max_age_days: int | None = None) -> tuple[str, int | None] | None:
    """
    Find the most recent occurrence from the mapping file.
    Returns (date, number) tuple or None if not found or too old.

    Args:
        call: The call series name
        max_age_days: If set, only return meetings within this many days
    """
    mapping = load_mapping()
    if not mapping:
        return None

    series_data = mapping.get(call)
    if not series_data or 'occurrences' not in series_data:
        return None

    occurrences = series_data['occurrences']
    if not occurrences:
        return None

    # Sort by start_time descending to get most recent
    # Filter out occurrences with None/empty start_time before sorting
    sorted_occs = sorted(
        [occ for occ in occurrences if occ.get('start_time')],
        key=lambda x: x.get('start_time', ''),
        reverse=True
    )

    # Filter to only past meetings and apply max_age_days if set
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=max_age_days) if max_age_days is not None else None

    for occ in sorted_occs:
        start_time = occ.get('start_time', '')
        if not start_time:
            continue
        try:
            meeting_dt = datetime.fromisoformat(start_time.replace('Z', '+00:00'))
            # Skip future meetings
            if meeting_dt > now:
                continue
            # Skip if too old (when max_age_days is set)
            if cutoff and meeting_dt < cutoff:
                continue
            # Found a valid meeting
            most_recent = occ
            break
        except ValueError:
            continue
    else:
        # No valid meeting found
        return None

    date = get_occurrence_date(most_recent)
    number = get_occurrence_call_number(most_recent)

    return date, number


def find_date_for_call_number(call: str, number: int) -> str | None:
    """Find the unique mapped date for a public call number."""
    mapping = load_mapping()
    if not mapping:
        return None

    series_data = mapping.get(call)
    if not series_data:
        return None

    matches = []
    for occurrence in series_data.get('occurrences', []):
        occurrence_number = get_occurrence_call_number(occurrence)
        occurrence_date = get_occurrence_date(occurrence)
        if occurrence_number == number and occurrence_date:
            matches.append(occurrence_date)

    if len(matches) > 1:
        dates = ", ".join(matches)
        raise ValueError(f"Ambiguous mapped occurrences for {call} #{number}: {dates}")

    return matches[0] if matches else None


def find_call_directory_by_date_and_number(call: str, date: str, number: int | None) -> Path | None:
    """Find the artifact directory for one mapped occurrence identity."""
    if number is None:
        return None

    call_dir = ARTIFACTS_DIR / call
    if not call_dir.exists():
        return None

    candidates = [
        call_dir / f"{date}_{number:03d}",
        call_dir / f"{date}_{number}",
    ]
    for candidate in candidates:
        if candidate.is_dir():
            return candidate

    return None


def get_all_series_from_mapping() -> list[str]:
    """Get all series names from the mapping file."""
    mapping = load_mapping()
    if not mapping:
        return []
    return list(mapping.keys())


def run_step(name: str, cmd: list[str], check: bool = True) -> bool:
    """Run a pipeline step and return success status."""
    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"{'='*60}\n")

    result = subprocess.run(cmd, cwd=SCRIPT_DIR)

    if result.returncode != 0:
        if check:
            print(f"\n❌ Step failed: {name}")
            return False
        else:
            print(f"\n⚠️  Step completed with warnings: {name}")

    return True


def prompt_yes_no(question: str) -> bool:
    """Prompt user with a yes/no question. Returns True for yes, False for no."""
    while True:
        response = input(f"{question} [y/n]: ").strip().lower()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        else:
            print("Please enter 'y' or 'n'")


def prompt_review(changelog_path: Path, open_editor: bool = False) -> str:
    """Prompt user to review the changelog. Returns 'y', 'n', or 'skip'."""
    print(f"\n{'='*60}")
    print(f"  REVIEW REQUIRED")
    print(f"{'='*60}\n")

    print(f"📄 Changelog generated at:\n   {changelog_path}\n")

    # Show preview of corrections
    if changelog_path.exists():
        with open(changelog_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        correction_count = len(lines) - 1  # Subtract header
        print(f"📊 Found {correction_count} suggested corrections\n")

        if correction_count > 0 and correction_count <= 20:
            print("Preview:")
            for line in lines[:21]:  # Header + up to 20 corrections
                print(f"   {line.rstrip()}")
            print()
        elif correction_count > 20:
            print("Preview (first 10):")
            for line in lines[:11]:
                print(f"   {line.rstrip()}")
            print(f"   ... and {correction_count - 10} more\n")

    if open_editor:
        editor = os.environ.get('EDITOR', 'vim')
        print(f"Opening {changelog_path} in {editor}...")
        subprocess.run([editor, str(changelog_path)])

    print("Please review the changelog and remove any incorrect suggestions.")
    print("Options:")
    print("  [y] Continue - apply corrections")
    print("  [n] Abort - exit without applying")
    print("  [s] Skip - skip corrections, keep original transcript")
    print()

    while True:
        response = input("Review complete? [y/n/s]: ").strip().lower()
        if response in ('y', 'yes'):
            return 'y'
        elif response in ('n', 'no'):
            return 'n'
        elif response in ('s', 'skip'):
            return 'skip'
        else:
            print("Please enter 'y', 'n', or 's'")


def main():
    parser = argparse.ArgumentParser(
        description='Run the full asset pipeline for a meeting',
        epilog='Example: python run_pipeline.py --call acde --number 226'
    )
    parser.add_argument('--call', '-c', required=True,
                        help='Call type (e.g., acde, acdc, acdt)')
    parser.add_argument('--number', '-n', type=int,
                        help='Call number (e.g., 226)')
    parser.add_argument('--recent', action='store_true',
                        help='Process most recent meeting for the series')
    parser.add_argument('--resume', action='store_true',
                        help='Resume from review step (skip download and changelog generation)')
    parser.add_argument('--open-editor', action='store_true',
                        help='Open changelog in $EDITOR for review')
    parser.add_argument('--model', '-m', default='claude-sonnet-4-6',
                        help='Claude model for changelog generation')
    parser.add_argument('--summarize', action='store_true',
                        help='Generate structured summary (tldr.json) after corrections')
    parser.add_argument('--include-zoom-summary', action='store_true',
                        help='Download Zoom meeting summary (summary.json) during asset download')
    parser.add_argument('--auto-approve', action='store_true',
                        help='Auto-approve corrections without interactive review (for CI/automation)')
    parser.add_argument('--max-age-days', type=int, default=None,
                        help='Only process meetings within this many days (for CI, e.g., --max-age-days 7)')
    parser.add_argument('--min-duration', type=int, default=15,
                        help='Minimum meeting duration in minutes for asset download (default: 15, set to 0 to process all)')
    args = parser.parse_args()

    # Validate arguments
    if not args.recent and args.number is None:
        parser.error("Either --number or --recent is required")

    call = args.call
    number = args.number

    # Resolve the pipeline target from mapping. Artifact directories are used
    # only after identity is known; they must not choose which call to process.
    target_date = None
    meeting_dir = None
    if args.recent:
        result = find_most_recent_from_mapping(call, args.max_age_days)
        if result is None:
            if args.max_age_days:
                # Not an error - just no recent meetings within the cutoff
                sys.exit(0)
            else:
                print(f"❌ No meetings found for series '{call}'")
                sys.exit(1)
        target_date, number = result

        # If number couldn't be determined, skip in CI mode or error otherwise
        if target_date is None or number is None:
            if args.max_age_days:
                print(f"⏭️  Could not determine meeting number for series '{call}' - skipping")
                sys.exit(0)
            else:
                print(f"❌ Could not determine meeting number for series '{call}'")
                sys.exit(1)

        meeting_dir = find_call_directory_by_date_and_number(call, target_date, number)
        print(f"📋 Most recent mapped meeting: {call} #{number} on {target_date}")
    else:
        if number is not None:
            try:
                target_date = find_date_for_call_number(call, number)
            except ValueError as e:
                print(f"❌ {e}")
                print("   Use a date-specific ingestion command or fix duplicate public numbers in meeting_topic_mapping.json.")
                sys.exit(1)

            if not target_date:
                print(f"❌ Could not find mapped date for {call} #{number}")
                sys.exit(1)

            meeting_dir = find_call_directory_by_date_and_number(call, target_date, number)

    print(f"\n🚀 Asset Pipeline: {call} #{number}")
    print(f"{'='*60}")

    # Step 1: Download assets
    if not args.resume:
        download_cmd = [
            sys.executable, "download_zoom_assets.py",
            "--series-name", call,
            "--min-duration", str(args.min_duration),
        ]
        if target_date:
            download_cmd.extend(["--date", target_date])
            if number is not None:
                download_cmd.extend(["--number", str(number)])
        elif args.recent:
            download_cmd.extend(["--recent", "1"])
        if args.include_zoom_summary:
            download_cmd.append("--include-summary")

        if not run_step("Step 1: Download Assets", download_cmd):
            sys.exit(1)

        # Re-check only the selected occurrence after download.
        if target_date and number is not None:
            meeting_dir = find_call_directory_by_date_and_number(call, target_date, number)

    # Verify meeting directory exists
    if target_date and number is not None:
        meeting_dir = find_call_directory_by_date_and_number(call, target_date, number)

    if not meeting_dir or not meeting_dir.exists():
        if args.max_age_days:
            # In automated mode, missing directory means no recording available - not an error
            print(f"⏭️  No recording available for {call} #{number} (directory not created)")
            sys.exit(0)
        else:
            print(f"❌ Meeting directory not found for {call} #{number}")
            sys.exit(1)

    transcript_path = meeting_dir / "transcript.vtt"
    changelog_path = meeting_dir / "transcript_changelog.tsv"
    corrected_path = meeting_dir / "transcript_corrected.vtt"
    tldr_path = meeting_dir / "tldr.json"

    # Early exit if all artifacts already exist (in auto-approve/CI mode)
    if args.auto_approve:
        required_artifacts = [transcript_path, changelog_path, corrected_path]
        if args.summarize:
            required_artifacts.append(tldr_path)

        if all(p.exists() for p in required_artifacts):
            print(f"⏭️  All artifacts already exist for {call} #{number}")
            sys.exit(0)

    # Check for transcript
    if not transcript_path.exists():
        print(f"❌ Transcript not found: {transcript_path}")
        sys.exit(1)

    # Step 2: Generate changelog
    if not args.resume:
        if changelog_path.exists():
            print(f"\n⏭️  Changelog already exists: {changelog_path}")
            print("   Use --resume to skip directly to review")
        else:
            changelog_cmd = [
                sys.executable, "generate_changelog.py",
                "--transcript", str(transcript_path),
                "--output", str(changelog_path),
                "--model", args.model,
            ]
            if not run_step("Step 2: Generate Changelog", changelog_cmd):
                sys.exit(1)

    # Verify changelog exists
    if not changelog_path.exists():
        print(f"❌ Changelog not found: {changelog_path}")
        print("   Run without --resume to generate it")
        sys.exit(1)

    # Step 3: Review (pause) - skip in auto-approve mode
    if args.auto_approve:
        print(f"\n⚡ Auto-approve mode: applying corrections without review")
        review_result = 'y'
    else:
        review_result = prompt_review(changelog_path, args.open_editor)

    if review_result == 'n':
        print("\n❌ Pipeline aborted by user")
        sys.exit(1)
    elif review_result == 'skip':
        print("\n⏭️  Skipping corrections - transcript unchanged")
    else:
        # Step 4: Apply changelog
        apply_cmd = [
            sys.executable, "apply_changelog.py",
            "--input", str(transcript_path),
            "--changelog", str(changelog_path),
            "--output", str(corrected_path),
        ]
        if not run_step("Step 4: Apply Corrections", apply_cmd):
            sys.exit(1)

    # Step 5: Generate summary (optional)
    run_summary = args.summarize  # In auto-approve mode, only run if --summarize is set
    if not run_summary and not args.auto_approve:
        run_summary = prompt_yes_no("\n📝 Generate structured summary (tldr.json)?")

    if run_summary:
        summary_cmd = [
            sys.executable, "generate_summary.py",
            "--dir", str(meeting_dir),
            "--model", args.model,
        ]
        if not run_step("Step 5: Generate Summary", summary_cmd, check=False):
            print("⚠️  Summary generation had issues, continuing...")

    # Summary
    print(f"\n{'='*60}")
    print(f"  ✅ Pipeline Complete")
    print(f"{'='*60}\n")

    print(f"📂 Meeting directory: {meeting_dir}")
    print(f"📄 Files:")
    print(f"   - transcript.vtt (original)")
    if corrected_path.exists():
        print(f"   - transcript_corrected.vtt (corrected)")
    print(f"   - transcript_changelog.tsv (corrections)")
    if (meeting_dir / "chat.txt").exists():
        print(f"   - chat.txt")
    if (meeting_dir / "summary.json").exists():
        print(f"   - summary.json")
    if (meeting_dir / "config.json").exists():
        print(f"   - config.json")
    if tldr_path.exists():
        print(f"   - tldr.json (structured summary)")


if __name__ == '__main__':
    main()
