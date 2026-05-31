#!/usr/bin/env python3
"""Compose a Zoom recording with fixed bumper clips.

The production ACDT upload shape is:

    first 45 seconds of bumper + Zoom recording + last 45 seconds of bumper

Zoom access and ffmpeg execution stay at the edge. Selection and command
construction are pure enough to keep covered by focused unit tests.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import requests


PEAK_LEVEL_PATTERN = re.compile(r"Peak level dB:\s+(-inf|[-0-9.]+)")
VTT_CUE_PATTERN = re.compile(
    r"(?P<start>\d{2}:\d{2}:\d{2}\.\d{3}|\d{2}:\d{2}\.\d{3})\s+-->\s+"
    r"(?P<end>\d{2}:\d{2}:\d{2}\.\d{3}|\d{2}:\d{2}\.\d{3})"
)
REQUIRED_VIDEO_LAYOUT = "shared_screen_with_speaker_view"
DEFAULT_BUMPER_CLIP_SECONDS = 45.0


@dataclass(frozen=True)
class SelectedRecordingFiles:
    video_file: dict[str, Any]
    audio_file: dict[str, Any] | None
    transcript_file: dict[str, Any] | None


@dataclass(frozen=True)
class ZoomTrimWindow:
    start_seconds: float
    end_seconds: float | None


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
    zoom_audio_path: Path | None = None,
    zoom_trim: ZoomTrimWindow | None = None,
    bumper_clip_seconds: float = DEFAULT_BUMPER_CLIP_SECONDS,
    width: int = 1280,
    height: int = 720,
    fps: int = 30,
) -> list[str]:
    """Build the ffmpeg command for bumper intro + Zoom + bumper outro."""
    if bumper_duration < bumper_clip_seconds * 2:
        raise ValueError(
            f"Bumper must be at least {bumper_clip_seconds * 2:.0f} seconds; "
            f"got {bumper_duration:.3f}s"
        )

    outro_start = bumper_duration - bumper_clip_seconds
    zoom_start = zoom_trim.start_seconds if zoom_trim else 0
    zoom_end = zoom_trim.end_seconds if zoom_trim else None
    zoom_video_trim = f"trim=start={zoom_start:.6f}"
    zoom_audio_trim = f"atrim=start={zoom_start:.6f}"
    if zoom_end is not None:
        zoom_video_trim += f":end={zoom_end:.6f}"
        zoom_audio_trim += f":end={zoom_end:.6f}"

    video_normalize = (
        f"scale={width}:{height}:force_original_aspect_ratio=decrease,"
        f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=black,"
        f"setsar=1,fps={fps},format=yuv420p"
    )
    audio_normalize = "aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo"
    filter_complex = ";".join(
        [
            f"[0:v]trim=start=0:end={bumper_clip_seconds:.6f},setpts=PTS-STARTPTS,{video_normalize}[v0]",
            f"[0:a]atrim=start=0:end={bumper_clip_seconds:.6f},asetpts=PTS-STARTPTS,{audio_normalize}[a0]",
            f"[1:v]{zoom_video_trim},setpts=PTS-STARTPTS,{video_normalize}[v1]",
            f"[{2 if zoom_audio_path else 1}:a]{zoom_audio_trim},asetpts=PTS-STARTPTS,{audio_normalize}[a1]",
            f"[0:v]trim=start={outro_start:.6f}:end={bumper_duration:.6f},setpts=PTS-STARTPTS,{video_normalize}[v2]",
            f"[0:a]atrim=start={outro_start:.6f}:end={bumper_duration:.6f},asetpts=PTS-STARTPTS,{audio_normalize}[a2]",
            "[v0][a0][v1][a1][v2][a2]concat=n=3:v=1:a=1[v][a]",
        ]
    )

    command = [
        "ffmpeg",
        "-y",
        "-hide_banner",
        "-i",
        str(bumper_path),
        "-i",
        str(zoom_path),
    ]
    if zoom_audio_path:
        command.extend(["-i", str(zoom_audio_path)])
    command.extend(
        [
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
    )
    return command


def normalize_recording_type(recording_type: str) -> str:
    """Treat Zoom's closed-caption variant as the same video layout."""
    return recording_type.removesuffix("(CC)")


def required_video_rank(file_info: dict[str, Any]) -> tuple[int, int]:
    recording_type = file_info.get("recording_type", "")
    is_not_caption_variant = int(recording_type != f"{REQUIRED_VIDEO_LAYOUT}(CC)")
    return is_not_caption_variant, -(file_info.get("file_size") or 0)


def select_recording_files(recording_info: dict[str, Any]) -> SelectedRecordingFiles | None:
    recording_files = recording_info.get("recording_files", [])
    video_files = [
        file_info
        for file_info in recording_files
        if file_info.get("file_type") == "MP4" and file_info.get("download_url")
    ]

    if video_files:
        available = ", ".join(
            f"{file_info.get('recording_type', 'unknown')}:{file_info.get('file_size', 'unknown')}"
            for file_info in video_files
        )
        print(f"[INFO] Available Zoom MP4 layouts: {available}")

    required_video_files = [
        file_info
        for file_info in video_files
        if normalize_recording_type(file_info.get("recording_type", "")) == REQUIRED_VIDEO_LAYOUT
    ]
    video_file = min(required_video_files, key=required_video_rank) if required_video_files else None
    if video_file is None:
        print(f"[WARN] Recording had no required MP4 video layout: {REQUIRED_VIDEO_LAYOUT}")
        return None

    print(
        "[DEBUG] Selected required video layout: "
        f"{video_file.get('recording_type', 'unknown')} size={video_file.get('file_size', 'unknown')}"
    )

    audio_candidates = [
        file_info
        for file_info in recording_files
        if file_info.get("file_type") == "M4A" and file_info.get("download_url")
    ]
    audio_candidates.sort(key=lambda file_info: file_info.get("file_size") or 0, reverse=True)
    audio_file = audio_candidates[0] if audio_candidates else None
    if audio_file:
        print(
            "[DEBUG] Selected separate audio: "
            f"{audio_file.get('recording_type', 'unknown')} size={audio_file.get('file_size', 'unknown')}"
        )
    else:
        print("[WARN] No separate M4A audio found; using the MP4 audio track")

    transcript_candidates = [
        file_info
        for file_info in recording_files
        if file_info.get("file_type") == "TRANSCRIPT" and file_info.get("download_url")
    ]
    transcript_candidates.sort(key=lambda file_info: file_info.get("file_size") or 0, reverse=True)
    transcript_file = transcript_candidates[0] if transcript_candidates else None
    if transcript_file:
        print(
            "[DEBUG] Selected transcript: "
            f"{transcript_file.get('recording_type', 'unknown')} size={transcript_file.get('file_size', 'unknown')}"
        )
    else:
        print("[WARN] No Zoom transcript found; dead-air trimming will be skipped")

    return SelectedRecordingFiles(video_file=video_file, audio_file=audio_file, transcript_file=transcript_file)


def parse_vtt_timestamp(value: str) -> float:
    parts = value.split(":")
    if len(parts) == 2:
        minutes, seconds = parts
        return int(minutes) * 60 + float(seconds)
    if len(parts) == 3:
        hours, minutes, seconds = parts
        return int(hours) * 3600 + int(minutes) * 60 + float(seconds)
    raise ValueError(f"Unsupported VTT timestamp: {value}")


def transcript_speech_window(
    transcript_text: str,
    duration_seconds: float,
    padding_seconds: float = 10,
) -> ZoomTrimWindow | None:
    cue_times = [
        (parse_vtt_timestamp(match.group("start")), parse_vtt_timestamp(match.group("end")))
        for match in VTT_CUE_PATTERN.finditer(transcript_text)
    ]
    if not cue_times:
        return None

    first_start = min(start for start, _ in cue_times)
    last_end = max(end for _, end in cue_times)
    start_seconds = max(0, first_start - padding_seconds)
    end_seconds = min(duration_seconds, last_end + padding_seconds)
    if end_seconds <= start_seconds:
        return None
    return ZoomTrimWindow(start_seconds=start_seconds, end_seconds=end_seconds)


def download_zoom_file(file_info: dict[str, Any], access_token: str, suffix: str) -> Path:
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        with requests.get(file_info["download_url"], headers=headers, stream=True) as response:
            if response.status_code != 200:
                raise RuntimeError(f"Failed to download Zoom file: HTTP {response.status_code}")
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    temp_file.write(chunk)
    finally:
        temp_file.close()

    path = Path(temp_file.name)
    print(f"[SUCCESS] Downloaded {suffix} to: {path} ({path.stat().st_size / 1024 / 1024:.1f} MiB)")
    return path


def extract_peak_level_db(ffmpeg_output: str) -> float | None:
    peak_levels = []
    for match in PEAK_LEVEL_PATTERN.finditer(ffmpeg_output):
        value = match.group(1)
        peak_levels.append(-math.inf if value == "-inf" else float(value))
    finite_levels = [level for level in peak_levels if math.isfinite(level)]
    return max(finite_levels) if finite_levels else None


def audio_has_signal(path: Path, minimum_peak_db: float = -50.0) -> bool:
    command = [
        "ffmpeg",
        "-hide_banner",
        "-i",
        str(path),
        "-af",
        "astats=metadata=1:reset=0",
        "-f",
        "null",
        "-",
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    peak_level = extract_peak_level_db(result.stderr)
    if peak_level is None:
        print(f"[WARN] Could not measure audio signal for {path}")
        return False

    print(f"[INFO] Measured audio peak for {path}: {peak_level:.2f} dB")
    return peak_level >= minimum_peak_db


def compose_zoom_recording(
    recording_info: dict[str, Any],
    bumper_path: Path,
    output_path: Path,
    access_token: str,
    bumper_clip_seconds: float = DEFAULT_BUMPER_CLIP_SECONDS,
) -> Path | None:
    """Download selected Zoom media and compose the final upload MP4."""
    selected_files = select_recording_files(recording_info)
    if not selected_files:
        raise RuntimeError(
            "Zoom recording exists but does not include required video layout "
            f"{REQUIRED_VIDEO_LAYOUT}. Check the host's Zoom cloud recording settings."
        )

    zoom_path = download_zoom_file(selected_files.video_file, access_token, ".mp4")
    zoom_audio_path = download_zoom_file(selected_files.audio_file, access_token, ".m4a") if selected_files.audio_file else None
    zoom_transcript_path = (
        download_zoom_file(selected_files.transcript_file, access_token, ".vtt")
        if selected_files.transcript_file
        else None
    )

    try:
        audio_source = zoom_audio_path or zoom_path
        if not audio_has_signal(audio_source):
            print(f"[WARN] Rejecting silent Zoom recording candidate: {audio_source}")
            return None

        output_path.parent.mkdir(parents=True, exist_ok=True)
        bumper_duration = probe_duration(bumper_path)
        zoom_trim = None
        if zoom_transcript_path:
            zoom_duration = probe_duration(zoom_path)
            zoom_trim = transcript_speech_window(
                zoom_transcript_path.read_text(encoding="utf-8", errors="replace"),
                duration_seconds=zoom_duration,
            )
            if zoom_trim:
                print(
                    "[INFO] Trimmed Zoom segment from transcript cues: "
                    f"{zoom_trim.start_seconds:.3f}s to {zoom_trim.end_seconds:.3f}s"
                )
            else:
                print("[WARN] Could not derive a transcript trim window; using full Zoom recording")

        command = build_ffmpeg_command(
            bumper_path,
            zoom_path,
            output_path,
            bumper_duration,
            zoom_audio_path,
            zoom_trim,
            bumper_clip_seconds=bumper_clip_seconds,
        )

        print(f"[INFO] Bumper duration: {bumper_duration:.3f}s")
        if zoom_audio_path:
            print(f"[INFO] Using separate Zoom audio: {zoom_audio_path}")
        print(f"[INFO] Composing output: {output_path}")
        subprocess.run(command, check=True)
        print(f"[SUCCESS] Wrote {output_path} ({output_path.stat().st_size / 1024 / 1024:.1f} MiB)")
        return output_path
    finally:
        for path in [zoom_path, zoom_audio_path, zoom_transcript_path]:
            if not path:
                continue
            try:
                os.unlink(path)
            except FileNotFoundError:
                pass


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a composed Zoom recording upload")
    parser.add_argument("--recording-json", required=True, type=Path, help="Path to Zoom recording JSON")
    parser.add_argument("--bumper", required=True, type=Path, help="Path to the bumper MP4")
    parser.add_argument("--output", required=True, type=Path, help="Path for the composed MP4")
    parser.add_argument("--bumper-clip-seconds", type=float, default=DEFAULT_BUMPER_CLIP_SECONDS)
    args = parser.parse_args()

    if not args.bumper.exists():
        raise FileNotFoundError(f"Bumper file does not exist: {args.bumper}")

    from modules.zoom import get_access_token

    recording_info = json.loads(args.recording_json.read_text(encoding="utf-8"))
    output = compose_zoom_recording(
        recording_info,
        args.bumper,
        args.output,
        get_access_token(),
        bumper_clip_seconds=args.bumper_clip_seconds,
    )
    return 0 if output else 1


if __name__ == "__main__":
    sys.exit(main())
