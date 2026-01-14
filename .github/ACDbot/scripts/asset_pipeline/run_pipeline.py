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
import os
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
ARTIFACTS_DIR = SCRIPT_DIR.parent.parent / "artifacts"


def find_call_directory(call: str, number: int) -> Path:
    """Find the directory for a given call type and number."""
    call_dir = ARTIFACTS_DIR / call
    if not call_dir.exists():
        return None

    # Find directory ending with _{number} (zero-padded to 3 digits)
    padded = str(number).zfill(3)
    for d in call_dir.iterdir():
        if d.is_dir() and d.name.endswith(f"_{padded}"):
            return d
        # Also check non-padded
        if d.is_dir() and d.name.endswith(f"_{number}"):
            return d

    return None


def find_most_recent_directory(call: str) -> tuple[Path, int] | None:
    """Find the most recent meeting directory for a call series."""
    call_dir = ARTIFACTS_DIR / call
    if not call_dir.exists():
        return None

    # Get all directories, sort by name (date_number format)
    dirs = sorted(
        [d for d in call_dir.iterdir() if d.is_dir()],
        key=lambda x: x.name,
        reverse=True
    )

    if not dirs:
        return None

    most_recent = dirs[0]
    # Extract number from directory name (e.g., "2024-12-12_226" -> 226)
    parts = most_recent.name.split("_")
    if len(parts) >= 2:
        try:
            number = int(parts[-1])
            return most_recent, number
        except ValueError:
            pass

    return most_recent, None


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


def prompt_review(changelog_path: Path, open_editor: bool = False) -> str:
    """Prompt user to review the changelog. Returns 'y', 'n', or 'skip'."""
    print(f"\n{'='*60}")
    print(f"  REVIEW REQUIRED")
    print(f"{'='*60}\n")

    print(f"📄 Changelog generated at:\n   {changelog_path}\n")

    # Show preview of corrections
    if changelog_path.exists():
        with open(changelog_path, 'r') as f:
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
    parser.add_argument('--model', '-m', default='claude-opus-4-5-20251101',
                        help='Claude model for changelog generation')
    parser.add_argument('--summarize', action='store_true',
                        help='Generate structured summary (tldr.json) after corrections')
    args = parser.parse_args()

    # Validate arguments
    if not args.recent and args.number is None:
        parser.error("Either --number or --recent is required")

    call = args.call
    number = args.number

    # If --recent, find the most recent meeting
    if args.recent:
        result = find_most_recent_directory(call)
        if result is None:
            print(f"❌ No meetings found for series '{call}'")
            sys.exit(1)
        meeting_dir, number = result
        if number:
            print(f"📋 Most recent meeting: {call} #{number}")
        else:
            print(f"📋 Most recent meeting directory: {meeting_dir.name}")

    # Check if meeting directory exists (for --resume)
    meeting_dir = find_call_directory(call, number) if number else None

    print(f"\n🚀 Asset Pipeline: {call} #{number}")
    print(f"{'='*60}")

    # Step 1: Download assets
    if not args.resume:
        download_cmd = [
            sys.executable, "download_zoom_assets.py",
            "--series-name", call,
        ]
        if args.recent:
            download_cmd.extend(["--recent", "1"])
        elif number:
            # Use --date if we can find it from directory, otherwise use --recent
            if meeting_dir:
                # Extract date from directory name
                date_part = meeting_dir.name.split("_")[0]
                download_cmd.extend(["--date", date_part])
            else:
                download_cmd.extend(["--recent", "1"])

        if not run_step("Step 1: Download Assets", download_cmd):
            sys.exit(1)

        # Re-check for meeting directory after download
        if args.recent:
            result = find_most_recent_directory(call)
            if result:
                meeting_dir, number = result

    # Verify meeting directory exists
    if number:
        meeting_dir = find_call_directory(call, number)

    if not meeting_dir or not meeting_dir.exists():
        print(f"❌ Meeting directory not found for {call} #{number}")
        sys.exit(1)

    transcript_path = meeting_dir / "transcript.vtt"
    changelog_path = meeting_dir / "transcript_changelog.tsv"
    corrected_path = meeting_dir / "transcript_corrected.vtt"

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
                "--call", call,
                "--number", str(number),
                "--model", args.model,
            ]
            if not run_step("Step 2: Generate Changelog", changelog_cmd):
                sys.exit(1)

    # Verify changelog exists
    if not changelog_path.exists():
        print(f"❌ Changelog not found: {changelog_path}")
        print("   Run without --resume to generate it")
        sys.exit(1)

    # Step 3: Review (pause)
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
            "--call", call,
            "--number", str(number),
        ]
        if not run_step("Step 4: Apply Corrections", apply_cmd):
            sys.exit(1)

    # Step 5: Generate summary (optional)
    tldr_path = meeting_dir / "tldr.json"
    if args.summarize:
        summary_cmd = [
            sys.executable, "generate_summary.py",
            "--call", call,
            "--number", str(number),
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
