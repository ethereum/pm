#!/usr/bin/env python3
"""Compose an ACD recording with an intro/outro bumper.

The output shape is:

    first half of bumper + Zoom recording + last half of bumper

Zoom access and local process execution are kept at the script edge so the
selection and ffmpeg command construction stay easy to test.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ACDBOT_DIR = Path(__file__).resolve().parents[1]
MAPPING_FILE_PATH = ACDBOT_DIR / "meeting_topic_mapping.json"


@dataclass(frozen=True)
class OccurrenceTarget:
    series: str
    meeting_id: str
    issue_number: int | None
    title: str
    start_time: str | None


def parse_utc_timestamp(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def select_occurrence_candidates(
    mapping: dict[str, Any],
    series: str,
    number: int | None = None,
    now: datetime | None = None,
) -> list[OccurrenceTarget]:
    """Return newest plausible mapped occurrences for a call series."""
    series_entry = mapping.get(series)
    if not series_entry:
        raise ValueError(f"Series '{series}' was not found in {MAPPING_FILE_PATH}")

    meeting_id = str(series_entry.get("meeting_id") or "")
    if not meeting_id:
        raise ValueError(f"Series '{series}' does not have a meeting_id")

    now = now or datetime.now(timezone.utc)
    candidates: list[OccurrenceTarget] = []

    for occurrence in series_entry.get("occurrences", []):
        start_time = occurrence.get("start_time")
        start_dt = parse_utc_timestamp(start_time)

        if number is not None and occurrence.get("occurrence_number") != number:
            continue
        if number is None and start_dt and start_dt > now:
            continue

        issue_number = occurrence.get("issue_number")
        candidates.append(
            OccurrenceTarget(
                series=series,
                meeting_id=meeting_id,
                issue_number=int(issue_number) if issue_number is not None else None,
                title=occurrence.get("issue_title") or f"{series.upper()} recording",
                start_time=start_time,
            )
        )

    candidates.sort(
        key=lambda item: parse_utc_timestamp(item.start_time) or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )
    return candidates


def probe_duration(path: Path) -> float:
    command = [
        "ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "json",
        str(path),
    ]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    duration = float(json.loads(result.stdout)["format"]["duration"])
    if duration <= 0:
        raise ValueError(f"Could not determine a positive duration for {path}")
    return duration


def build_ffmpeg_command(
    bumper_path: Path,
    zoom_path: Path,
    output_path: Path,
    bumper_duration: float,
    width: int = 1280,
    height: int = 720,
    fps: int = 30,
) -> list[str]:
    half = bumper_duration / 2
    video_normalize = (
        f"scale={width}:{height}:force_original_aspect_ratio=decrease,"
        f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=black,"
        f"setsar=1,fps={fps},format=yuv420p"
    )
    audio_normalize = "aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo"
    filter_complex = ";".join(
        [
            f"[0:v]trim=start=0:end={half:.6f},setpts=PTS-STARTPTS,{video_normalize}[v0]",
            f"[0:a]atrim=start=0:end={half:.6f},asetpts=PTS-STARTPTS,{audio_normalize}[a0]",
            f"[1:v]setpts=PTS-STARTPTS,{video_normalize}[v1]",
            f"[1:a]asetpts=PTS-STARTPTS,{audio_normalize}[a1]",
            f"[0:v]trim=start={half:.6f}:end={bumper_duration:.6f},setpts=PTS-STARTPTS,{video_normalize}[v2]",
            f"[0:a]atrim=start={half:.6f}:end={bumper_duration:.6f},asetpts=PTS-STARTPTS,{audio_normalize}[a2]",
            "[v0][a0][v1][a1][v2][a2]concat=n=3:v=1:a=1[v][a]",
        ]
    )
    return [
        "ffmpeg",
        "-y",
        "-hide_banner",
        "-i",
        str(bumper_path),
        "-i",
        str(zoom_path),
        "-filter_complex",
        filter_complex,
        "-map",
        "[v]",
        "-map",
        "[a]",
        "-c:v",
        "libx264",
        "-preset",
        "veryfast",
        "-crf",
        "23",
        "-c:a",
        "aac",
        "-b:a",
        "160k",
        "-movflags",
        "+faststart",
        str(output_path),
    ]


def download_zoom_recording_for_latest_candidate(
    candidates: list[OccurrenceTarget],
    min_duration: int,
    max_candidates: int,
) -> tuple[OccurrenceTarget, Path]:
    from scripts.upload_zoom_recording import download_zoom_recording

    attempted = candidates[:max_candidates]
    if not attempted:
        raise ValueError("No mapped occurrences matched the requested series/number")

    for candidate in attempted:
        print(
            "[INFO] Trying Zoom recording for "
            f"{candidate.series.upper()} issue={candidate.issue_number} start={candidate.start_time}"
        )
        video_path = download_zoom_recording(
            candidate.meeting_id,
            min_duration_minutes=min_duration,
            target_start_time=candidate.start_time,
            tolerance_minutes=180,
        )
        if video_path:
            return candidate, Path(video_path)

    raise RuntimeError(f"No downloadable Zoom MP4 was found after trying {len(attempted)} candidate(s)")


def write_metadata(path: Path, target: OccurrenceTarget, zoom_path: Path, output_path: Path) -> None:
    metadata = {
        "series": target.series,
        "meeting_id": target.meeting_id,
        "issue_number": target.issue_number,
        "title": target.title,
        "start_time": target.start_time,
        "zoom_file": str(zoom_path),
        "output_file": str(output_path),
        "output_size_bytes": output_path.stat().st_size if output_path.exists() else None,
    }
    path.write_text(json.dumps(metadata, indent=2) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an intro + Zoom + outro test video")
    parser.add_argument("--series", default="acde", help="Call series key from meeting_topic_mapping.json")
    parser.add_argument("--number", type=int, help="Public occurrence number, e.g. 236")
    parser.add_argument("--bumper", required=True, type=Path, help="Path to ev.mp4 or equivalent bumper")
    parser.add_argument("--output", required=True, type=Path, help="Path for the stitched MP4")
    parser.add_argument("--metadata", type=Path, help="Optional JSON metadata output path")
    parser.add_argument("--min-duration", type=int, default=10, help="Minimum Zoom recording duration in minutes")
    parser.add_argument("--max-candidates", type=int, default=5, help="How many recent occurrences to try")
    args = parser.parse_args()

    if not args.bumper.exists():
        raise FileNotFoundError(f"Bumper file does not exist: {args.bumper}")

    with MAPPING_FILE_PATH.open() as file:
        mapping = json.load(file)

    candidates = select_occurrence_candidates(mapping, args.series, args.number)
    target, zoom_path = download_zoom_recording_for_latest_candidate(
        candidates,
        min_duration=args.min_duration,
        max_candidates=args.max_candidates,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    bumper_duration = probe_duration(args.bumper)
    command = build_ffmpeg_command(args.bumper, zoom_path, args.output, bumper_duration)

    print(f"[INFO] Bumper duration: {bumper_duration:.3f}s")
    print(f"[INFO] Composing output: {args.output}")
    subprocess.run(command, check=True)

    if args.metadata:
        args.metadata.parent.mkdir(parents=True, exist_ok=True)
        write_metadata(args.metadata, target, zoom_path, args.output)

    try:
        os.unlink(zoom_path)
    except FileNotFoundError:
        pass

    print(f"[SUCCESS] Wrote {args.output} ({args.output.stat().st_size / 1024 / 1024:.1f} MiB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
