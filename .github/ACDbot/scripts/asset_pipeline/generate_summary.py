#!/usr/bin/env python3
"""
Generate a structured JSON summary (tldr.json) for an Ethereum meeting.
Uses Claude API with meeting transcript, chat, and GitHub issue agenda.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

import anthropic
import requests
from dotenv import load_dotenv
from meeting_identity import get_occurrence_call_number

# Load environment variables
load_dotenv(Path(__file__).parent.parent.parent / ".env")

from utils import SCRIPT_DIR, find_call_directory, calculate_cost

ACDBOT_DIR = SCRIPT_DIR.parent.parent
MAPPING_FILE = ACDBOT_DIR / "meeting_topic_mapping.json"
DEFAULT_PROMPT = SCRIPT_DIR / "prompts" / "summarize.md"
PROMPTS_DIR = SCRIPT_DIR / "prompts"
VOCAB_FILE = SCRIPT_DIR / "ethereum_vocab.yaml"

# Example summaries by call type
# Note: ACDE intentionally uses the ACDC example as they share similar format
EXAMPLE_SUMMARIES = {
    "acdt": PROMPTS_DIR / "example_acdt_summary.json",
    "acde": PROMPTS_DIR / "example_acdc_summary.json",
    "acdc": PROMPTS_DIR / "example_acdc_summary.json",
}


def parse_call_directory(dir_name: str) -> tuple[str | None, int | None]:
    """Parse an artifact directory name into date and public call number."""
    match = re.match(r'^(\d{4}-\d{2}-\d{2})(?:_(\d+))?$', dir_name)
    if not match:
        return None, None
    return match.group(1), int(match.group(2)) if match.group(2) else None


def get_occurrence_from_mapping(call_type: str, date_str: str, number: int | None = None) -> dict | None:
    """Look up one occurrence by call type, date, and optional public call number."""
    if not MAPPING_FILE.exists():
        return None

    try:
        with open(MAPPING_FILE, 'r', encoding='utf-8') as f:
            mapping = json.load(f)

        series_data = mapping.get(call_type)
        if not series_data:
            return None

        matches = []
        for occ in series_data.get('occurrences', []):
            start_time = occ.get('start_time', '')
            if not start_time or not start_time.startswith(date_str):
                continue
            if number is not None and get_occurrence_call_number(occ) != number:
                continue
            matches.append(occ)

        return matches[0] if len(matches) == 1 else None
    except Exception:
        return None


def get_meeting_title_from_mapping(issue_number: int) -> str | None:
    """Look up the issue_title from the mapping file by issue number."""
    if not MAPPING_FILE.exists():
        return None

    try:
        with open(MAPPING_FILE, 'r', encoding='utf-8') as f:
            mapping = json.load(f)

        for series_data in mapping.values():
            for occ in series_data.get('occurrences', []):
                if occ.get('issue_number') == issue_number:
                    return occ.get('issue_title')
        return None
    except Exception:
        return None


def get_example_summary(call_type: str) -> str:
    """Get the appropriate example summary for the call type."""
    example_path = EXAMPLE_SUMMARIES.get(call_type.lower())
    if example_path and example_path.exists():
        return example_path.read_text()
    # Fallback to acdc example if call type not found
    fallback = PROMPTS_DIR / "example_acdc_summary.json"
    if fallback.exists():
        return fallback.read_text()
    return ""


def fetch_github_issue_agenda(issue_number: int, repo: str = "ethereum/pm") -> str | None:
    """Fetch the Agenda section from a GitHub issue via the REST API.

    Reads the issue body markdown (stable) instead of scraping rendered HTML.
    Uses GITHUB_TOKEN when available to avoid unauthenticated rate limits.
    """
    url = f"https://api.github.com/repos/{repo}/issues/{issue_number}"
    base_headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")

    try:
        response = requests.get(
            url,
            headers={**base_headers, "Authorization": f"Bearer {token}"} if token else base_headers,
        )
        # A stale/invalid token (e.g. from a local .env) should not block the
        # public read; retry unauthenticated on auth failures.
        if token and response.status_code in (401, 403):
            print(f"  GITHUB_TOKEN rejected ({response.status_code}); retrying unauthenticated")
            response = requests.get(url, headers=base_headers)
        if response.status_code != 200:
            print(f"  Failed to fetch GitHub issue #{issue_number}: {response.status_code}")
            return None

        body = (response.json().get("body") or "").replace("\r\n", "\n")
        if not body.strip():
            print(f"  Issue #{issue_number} has no body")
            return None

        # Extract the "### Agenda" section up to the next markdown heading.
        agenda_match = re.search(
            r'^#{1,6}\s*Agenda\s*$\n(.*?)(?=^#{1,6}\s|\Z)',
            body,
            re.DOTALL | re.IGNORECASE | re.MULTILINE,
        )
        if not agenda_match:
            print(f"  Could not find 'Agenda' section in issue #{issue_number}, using full body")
            return body.strip()

        return agenda_match.group(1).strip()

    except Exception as e:
        print(f"  Error fetching GitHub issue: {e}")
        return None


def find_breakout_transcripts(meeting_dir: Path) -> list[tuple[str, Path]]:
    """Find breakout transcripts (e.g. transcript_cl.vtt) as (label, path) pairs.

    Breakout rooms held in a separate Zoom meeting have their own recording
    timeline, so each gets its own tldr_<label>.json rather than being merged
    into the main call's tldr.json (whose timestamps refer to transcript.vtt).
    """
    breakouts = []
    for path in sorted(meeting_dir.glob("transcript_*.vtt")):
        if path.name == "transcript_corrected.vtt":
            continue
        breakouts.append((path.stem.removeprefix("transcript_"), path))
    return breakouts


def build_prompt(
    meeting_title: str | None,
    agenda: str,
    vocab: str,
    example_summary: str,
    transcript: str,
    chat: str,
    zoom_summary: str,
    prompt_template: str,
) -> str:
    """Assemble the full summarization prompt for one transcript."""
    return f"""## Meeting Title

{meeting_title if meeting_title else "(Use the title from the agenda)"}

## Meeting Agenda

{agenda}

## Ethereum Vocabulary Reference (use correct spellings from this list)

{vocab if vocab else "(No vocabulary reference available)"}

## Example Output (for reference on structure and length)

{example_summary if example_summary else "(No example available)"}

## Transcript (transcript.vtt)

{transcript}

## Chat Messages (chat.txt)

{chat if chat else "(No chat file available)"}

## Zoom AI Summary (summary.json)

{zoom_summary if zoom_summary else "(No summary file available)"}

---

{prompt_template}"""


def call_claude_and_save(full_prompt: str, model: str, tldr_path: Path) -> bool:
    """Call the Claude API with the prompt and save the JSON result."""
    print(f"⏳ Calling Claude API ({model}) to generate summary - this may take a minute...")
    try:
        client = anthropic.Anthropic()
        message = client.messages.create(
            model=model,
            max_tokens=16000,
            messages=[{"role": "user", "content": full_prompt}]
        )

        usage = {
            "input_tokens": message.usage.input_tokens,
            "output_tokens": message.usage.output_tokens,
        }

        response_text = message.content[0].text

        # Extract JSON from response
        json_match = re.search(r'```json\s*(.*?)\s*```', response_text, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        else:
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            json_str = json_match.group(0) if json_match else response_text

        # Parse and save
        try:
            tldr_data = json.loads(json_str)
            with open(tldr_path, 'w', encoding='utf-8') as f:
                json.dump(tldr_data, f, indent=2)

            cost = calculate_cost(model, usage)
            print(f"\nTokens: {usage['input_tokens']:,} input, {usage['output_tokens']:,} output")
            print(f"Cost: ${cost:.4f}")
            print(f"\nGenerated {tldr_path}")
            return True

        except json.JSONDecodeError as e:
            print(f"Response was not valid JSON: {e}")
            return False

    except anthropic.APIError as e:
        print(f"API request failed: {e}")
        return False
    except Exception as e:
        print(f"Error calling API: {e}")
        return False


def generate_summary(
    meeting_dir: Path,
    prompt_file: Path,
    call_type: str,
    model: str = "claude-sonnet-4-6",
    force: bool = False
) -> bool:
    """Generate tldr.json (and tldr_<label>.json per breakout) using Claude API."""
    # Paths — prefer corrected transcript when available
    corrected_path = meeting_dir / "transcript_corrected.vtt"
    transcript_path = corrected_path if corrected_path.exists() else meeting_dir / "transcript.vtt"
    chat_path = meeting_dir / "chat.txt"
    summary_path = meeting_dir / "summary.json"
    tldr_path = meeting_dir / "tldr.json"

    breakout_transcripts = find_breakout_transcripts(meeting_dir)

    # Check if all outputs already exist
    main_exists = tldr_path.exists()
    pending_breakouts = [
        (label, path) for label, path in breakout_transcripts
        if not (meeting_dir / f"tldr_{label}.json").exists()
    ]
    if main_exists and not pending_breakouts and not force:
        print(f"tldr.json already exists (use --force to regenerate)")
        return True

    # Validate required files
    if not transcript_path.exists():
        print(f"transcript.vtt not found in {meeting_dir}")
        return False

    # Extract identity from directory name (e.g., "2026-02-05_174")
    date_str, number = parse_call_directory(meeting_dir.name)
    if not date_str:
        print(f"Could not parse meeting directory name: {meeting_dir.name}")
        return False

    # Look up occurrence data from mapping file
    occurrence = get_occurrence_from_mapping(call_type, date_str, number)
    if not occurrence:
        label = f"{date_str} #{number}" if number is not None else date_str
        print(f"No occurrence found in mapping for {call_type} on {label}")
        return False

    issue_number = occurrence.get('issue_number')
    if not issue_number:
        label = f"{date_str} #{number}" if number is not None else date_str
        print(f"No issue number in mapping for {call_type} on {label}")
        return False

    # Get meeting title from occurrence
    meeting_title = occurrence.get('issue_title')
    if meeting_title:
        print(f"Meeting title: {meeting_title}")

    # Fetch agenda from GitHub
    print(f"Fetching agenda from GitHub issue #{issue_number}...")
    agenda = fetch_github_issue_agenda(issue_number)
    if not agenda:
        print("Could not fetch agenda, proceeding without it")
        agenda = "(Agenda not available)"

    # Load prompt
    if not prompt_file.exists():
        print(f"Prompt file not found: {prompt_file}")
        return False

    prompt_template = prompt_file.read_text()

    # Load transcript
    transcript = transcript_path.read_text()

    # Load chat (optional)
    chat = chat_path.read_text() if chat_path.exists() else ""

    # Load Zoom AI summary (optional)
    zoom_summary = ""
    if summary_path.exists():
        try:
            zoom_summary = summary_path.read_text()
        except Exception:
            pass

    # Load example summary for reference (based on call type)
    example_summary = get_example_summary(call_type)

    # Load vocabulary reference for correct spelling of Ethereum terms
    vocab = ""
    if VOCAB_FILE.exists():
        vocab = VOCAB_FILE.read_text()

    success = True

    # Main call summary (includes any breakout held in the same Zoom meeting,
    # e.g. the ACDT EL breakout in the later portion of transcript.vtt)
    if not main_exists or force:
        full_prompt = build_prompt(
            meeting_title, agenda, vocab, example_summary,
            transcript, chat, zoom_summary, prompt_template,
        )
        if not call_claude_and_save(full_prompt, model, tldr_path):
            success = False
    else:
        print(f"tldr.json already exists, generating breakout summaries only")

    # Separate summary per breakout held in its own Zoom meeting. Each breakout
    # transcript has its own timeline, so timestamps only make sense in a
    # dedicated tldr_<label>.json.
    breakouts_to_generate = breakout_transcripts if force else pending_breakouts
    for breakout_label, breakout_transcript_path in breakouts_to_generate:
        breakout_tldr_path = meeting_dir / f"tldr_{breakout_label}.json"
        breakout_chat_path = meeting_dir / f"chat_{breakout_label}.txt"
        breakout_chat = breakout_chat_path.read_text() if breakout_chat_path.exists() else ""

        breakout_title = (
            f"{meeting_title} ({breakout_label.upper()} breakout)"
            if meeting_title else None
        )
        print(f"\nGenerating {breakout_tldr_path.name} from {breakout_transcript_path.name}...")
        full_prompt = build_prompt(
            breakout_title, agenda, vocab, example_summary,
            breakout_transcript_path.read_text(), breakout_chat, "", prompt_template,
        )
        if not call_claude_and_save(full_prompt, model, breakout_tldr_path):
            success = False

    return success


def main():
    parser = argparse.ArgumentParser(
        description='Generate tldr.json summary using Claude API',
        epilog='Example: uv run --project .github/ACDbot .github/ACDbot/scripts/asset_pipeline/generate_summary.py --call acde --number 226'
    )
    parser.add_argument('--call', '-c', help='Call type (e.g., acde, acdc, acdt)')
    parser.add_argument('--number', '-n', type=int, help='Call number (e.g., 226)')
    parser.add_argument('--dir', '-d', type=Path, help='Meeting directory (alternative to --call/--number)')
    parser.add_argument('--prompt', '-p', type=Path, default=DEFAULT_PROMPT,
                        help='Prompt file (default: asset_pipeline/prompts/summarize.md)')
    parser.add_argument('--model', '-m', default='claude-sonnet-4-6',
                        help='Claude model to use')
    parser.add_argument('--force', '-f', action='store_true',
                        help='Regenerate even if tldr.json exists')
    args = parser.parse_args()

    # Resolve meeting directory and call type
    if args.dir:
        meeting_dir = args.dir
        # Infer call type from directory path (e.g., artifacts/acdt/2026-01-12_065)
        call_type = meeting_dir.parent.name if meeting_dir.parent else "acdc"
    elif args.call and args.number:
        meeting_dir = find_call_directory(args.call, args.number)
        call_type = args.call
    else:
        parser.error("Either --dir or both --call and --number are required")

    print(f"Meeting directory: {meeting_dir}")
    print(f"Call type: {call_type}")

    success = generate_summary(meeting_dir, args.prompt, call_type, args.model, args.force)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
