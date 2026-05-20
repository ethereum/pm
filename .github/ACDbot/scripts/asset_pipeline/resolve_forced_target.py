#!/usr/bin/env python3
"""Resolve a forced asset pipeline target before side-effecting workflow steps."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from meeting_identity import get_occurrence_call_number, parse_public_call_number


SCRIPT_DIR = Path(__file__).parent
ACDBOT_DIR = SCRIPT_DIR.parent.parent
DEFAULT_MAPPING_FILE = ACDBOT_DIR / "meeting_topic_mapping.json"


def occurrence_date(occurrence: dict) -> str:
    """Return the occurrence date if present."""
    start_time = occurrence.get("start_time", "")
    return start_time.split("T")[0] if start_time else ""


def describe_occurrence(occurrence: dict) -> str:
    """Describe an occurrence enough to explain an ambiguous forced target."""
    date = occurrence_date(occurrence) or "unknown date"
    issue = occurrence.get("issue_number", "unknown issue")
    title = occurrence.get("issue_title", "untitled")
    return f"{date} issue {issue}: {title}"


def resolve_forced_target(mapping: dict, series: str, number: int) -> dict:
    """Resolve a forced workflow input to one mapped occurrence."""
    series_data = mapping.get(series)
    if not series_data:
        raise ValueError(f"Series {series} not found")

    matches = [
        occurrence
        for occurrence in series_data.get("occurrences", [])
        if get_occurrence_call_number(occurrence) == number
    ]

    if not matches:
        raise ValueError(f"No mapped occurrence for {series} #{number}")

    if len(matches) > 1:
        details = "; ".join(describe_occurrence(occurrence) for occurrence in matches)
        raise ValueError(f"Ambiguous mapped occurrences for {series} #{number}: {details}")

    occurrence = matches[0]
    meeting_id = str(occurrence.get("meeting_id") or series_data.get("meeting_id") or "").strip()
    issue_number = occurrence.get("issue_number")
    date = occurrence_date(occurrence)
    if not meeting_id:
        raise ValueError(f"Mapped occurrence for {series} #{number} has no meeting_id")
    if not issue_number:
        raise ValueError(f"Mapped occurrence for {series} #{number} has no issue_number")
    if not date:
        raise ValueError(f"Mapped occurrence for {series} #{number} has no start_time")

    return {
        "meeting_id": meeting_id,
        "issue_number": int(issue_number),
        "date": date,
        "number": number,
    }


def write_github_env(path: Path, target: dict) -> None:
    """Append resolved target fields to GitHub Actions environment output."""
    with path.open("a", encoding="utf-8") as env_file:
        env_file.write(f"FORCED_MEETING_ID={target['meeting_id']}\n")
        env_file.write(f"FORCED_ISSUE_NUMBER={target['issue_number']}\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Resolve a forced asset pipeline target")
    parser.add_argument("--series", required=True, help="Call series key")
    parser.add_argument("--number", required=True, help="Public call number")
    parser.add_argument("--mapping", type=Path, default=DEFAULT_MAPPING_FILE)
    parser.add_argument("--github-env", type=Path, help="Path to append GitHub Actions env vars")
    args = parser.parse_args()

    number = parse_public_call_number(args.number)
    if number is None:
        raise SystemExit(f"Invalid public call number: {args.number}")

    with args.mapping.open("r", encoding="utf-8") as mapping_file:
        mapping = json.load(mapping_file)

    try:
        target = resolve_forced_target(mapping, args.series, number)
    except ValueError as error:
        raise SystemExit(str(error)) from error

    if args.github_env:
        write_github_env(args.github_env, target)

    print(
        f"Resolved forced target: {args.series} #{target['number']} "
        f"on {target['date']} issue {target['issue_number']} meeting {target['meeting_id']}"
    )


if __name__ == "__main__":
    main()
