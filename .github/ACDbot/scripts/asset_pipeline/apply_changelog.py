#!/usr/bin/env python3
"""
Apply corrections from transcript_changelog.tsv to a VTT transcript.
Replaces all occurrences of each original term with its correction.
"""

import csv
import argparse
from dataclasses import dataclass
from pathlib import Path

# Base paths relative to this script
SCRIPT_DIR = Path(__file__).parent
ARTIFACTS_DIR = SCRIPT_DIR.parent.parent / "artifacts"


def find_call_directory(call: str, number: int) -> Path:
    """Find the directory for a given call type and number."""
    call_dir = ARTIFACTS_DIR / call
    if not call_dir.exists():
        raise FileNotFoundError(f"Call type directory not found: {call_dir}")

    # Find directory ending with _{number} (check both zero-padded and non-padded)
    padded = str(number).zfill(3)
    for d in call_dir.iterdir():
        if d.is_dir() and (d.name.endswith(f"_{padded}") or d.name.endswith(f"_{number}")):
            return d

    raise FileNotFoundError(f"No directory found for {call} #{number}")


@dataclass
class Change:
    original: str
    corrected: str
    confidence: str


def load_changelog(path: str) -> list[Change]:
    """Load changelog from TSV file."""
    changes = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            changes.append(Change(
                original=row['original'],
                corrected=row['corrected'],
                confidence=row['confidence']
            ))
    return changes

def apply_changelog(content: str, changes: list[Change]) -> tuple[str, dict[str, int], list[str]]:
    """Apply all corrections. Returns corrected content, counts per term, and unmatched."""
    result = content
    counts = {}
    unmatched = []

    for change in changes:
        count = result.count(change.original)
        if count > 0:
            result = result.replace(change.original, change.corrected)
            counts[f"'{change.original}' -> '{change.corrected}'"] = count
        else:
            unmatched.append(change.original)

    return result, counts, unmatched

def main():
    parser = argparse.ArgumentParser(
        description='Apply changelog corrections to VTT',
        epilog='Example: python apply_changelog.py --call acde --number 226'
    )
    # Shorthand arguments for call directory lookup
    parser.add_argument('--call', '-c', help='Call type (e.g., acde, acdc, acdt)')
    parser.add_argument('--number', '-n', type=int, help='Call number (e.g., 226)')
    # Explicit path arguments (override call/number)
    parser.add_argument('--input', '-i', help='Input VTT file')
    parser.add_argument('--changelog', help='Changelog TSV file')
    parser.add_argument('--output', '-o', help='Output VTT file')
    args = parser.parse_args()

    # Resolve paths based on call/number or explicit arguments
    if args.call and args.number:
        call_dir = find_call_directory(args.call, args.number)
        input_path = args.input or call_dir / "transcript.vtt"
        changelog_path = args.changelog or call_dir / "transcript_changelog.tsv"
        output_path = args.output or call_dir / "transcript_corrected.vtt"
        print(f"Using call directory: {call_dir}")
    else:
        input_path = args.input or "transcript.vtt"
        changelog_path = args.changelog or "transcript_changelog.tsv"
        output_path = args.output or "transcript_corrected.vtt"

    changes = load_changelog(changelog_path)
    print(f"Loaded {len(changes)} corrections from {changelog_path}")

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    corrected, counts, unmatched = apply_changelog(content, changes)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(corrected)

    total = sum(counts.values())
    print(f"\nApplied {total} replacements -> {output_path}\n")

    for term, count in counts.items():
        print(f"  {term}: {count}x")

    if unmatched:
        print(f"\nWarning: {len(unmatched)} terms not found:")
        for u in unmatched:
            print(f"  '{u}'")

if __name__ == '__main__':
    main()