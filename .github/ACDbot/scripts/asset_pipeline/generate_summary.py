#!/usr/bin/env python3
"""
Generate a structured JSON summary (tldr.json) for an Ethereum meeting.
Uses Claude API with meeting transcript, chat, and GitHub issue agenda.
"""

import argparse
import json
import re
import sys
from html import unescape
from pathlib import Path

import anthropic
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv(Path(__file__).parent.parent.parent / ".env")

from utils import SCRIPT_DIR, find_call_directory, calculate_cost

DEFAULT_PROMPT = SCRIPT_DIR / "prompts" / "summarize.md"
PROMPTS_DIR = SCRIPT_DIR / "prompts"

# Example summaries by call type
# Note: ACDE intentionally uses the ACDC example as they share similar format
EXAMPLE_SUMMARIES = {
    "acdt": PROMPTS_DIR / "example_acdt_summary.json",
    "acde": PROMPTS_DIR / "example_acdc_summary.json",
    "acdc": PROMPTS_DIR / "example_acdc_summary.json",
}


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
    """Fetch the agenda section from a GitHub issue by scraping the public page."""
    url = f"https://github.com/{repo}/issues/{issue_number}"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"  Failed to fetch GitHub issue #{issue_number}: {response.status_code}")
            return None

        html_content = response.text

        # Look for the markdown-body div which contains the rendered issue content
        body_pattern = r'<div[^>]*class="[^"]*markdown-body[^"]*"[^>]*>(.*?)</div>\s*</div>\s*</div>\s*</div>\s*<div class="Box-sc'
        body_match = re.search(body_pattern, html_content, re.DOTALL)

        if not body_match:
            # Try alternative pattern for the NewMarkdownViewer wrapper
            body_pattern = r'class="Box-sc-[^"]*\s+markdown-body\s+NewMarkdownViewer[^"]*"[^>]*>(.*?)</div>'
            body_match = re.search(body_pattern, html_content, re.DOTALL)

        if body_match:
            body_html = body_match.group(1)

            # Try to find the "Agenda" heading and extract content after it
            agenda_pattern = r'<h3[^>]*>.*?Agenda.*?</h3>(.*?)(?=<h[123]|</div>|$)'
            agenda_match = re.search(agenda_pattern, body_html, re.DOTALL | re.IGNORECASE)

            if agenda_match:
                agenda_html = agenda_match.group(1)

                # Convert HTML to text
                agenda_html = re.sub(r'<script[^>]*>.*?</script>', '', agenda_html, flags=re.DOTALL)
                agenda_html = re.sub(r'<style[^>]*>.*?</style>', '', agenda_html, flags=re.DOTALL)
                agenda_html = re.sub(r'<br\s*/?>', '\n', agenda_html)
                agenda_html = re.sub(r'</li>', '\n', agenda_html)
                agenda_html = re.sub(r'<li[^>]*>', '- ', agenda_html)
                agenda_html = re.sub(r'</p>', '\n\n', agenda_html)
                agenda_html = re.sub(r'<p[^>]*>', '', agenda_html)
                agenda_html = re.sub(r'</ul>', '\n', agenda_html)
                agenda_html = re.sub(r'<ul[^>]*>', '\n', agenda_html)
                agenda_html = re.sub(r'<[^>]+>', '', agenda_html)

                agenda_text = unescape(agenda_html)
                agenda_text = re.sub(r'\n\s*\n\s*\n+', '\n\n', agenda_text)
                agenda_text = re.sub(r'^\s+', '', agenda_text, flags=re.MULTILINE)
                return agenda_text.strip()
            else:
                print(f"  Could not find '### Agenda' section in issue #{issue_number}")
                # Return full body as fallback
                body_text = re.sub(r'<br\s*/?>', '\n', body_html)
                body_text = re.sub(r'</li>', '\n', body_html)
                body_text = re.sub(r'<li[^>]*>', '- ', body_html)
                body_text = re.sub(r'<[^>]+>', '', body_text)
                body_text = unescape(body_text)
                return re.sub(r'\n\s*\n\s*\n+', '\n\n', body_text).strip()
        else:
            print(f"  Could not parse issue body from HTML")
            return None

    except Exception as e:
        print(f"  Error fetching GitHub issue: {e}")
        return None


def generate_summary(
    meeting_dir: Path,
    prompt_file: Path,
    call_type: str,
    model: str = "claude-sonnet-4-5-20250929",
    force: bool = False
) -> bool:
    """Generate tldr.json using Claude API."""
    # Paths
    config_path = meeting_dir / "config.json"
    transcript_path = meeting_dir / "transcript.vtt"
    chat_path = meeting_dir / "chat.txt"
    summary_path = meeting_dir / "summary.json"
    tldr_path = meeting_dir / "tldr.json"

    # Check if already exists
    if tldr_path.exists() and not force:
        print(f"tldr.json already exists (use --force to regenerate)")
        return True

    # Validate required files
    if not config_path.exists():
        print(f"config.json not found in {meeting_dir}")
        return False

    if not transcript_path.exists():
        print(f"transcript.vtt not found in {meeting_dir}")
        return False

    # Load config for issue number
    try:
        with open(config_path, encoding='utf-8') as f:
            config = json.load(f)
        issue_number = config.get("issue")
        if not issue_number:
            print("No issue number in config.json")
            return False
    except Exception as e:
        print(f"Error reading config.json: {e}")
        return False

    # Fetch agenda from GitHub
    print(f"Fetching agenda from GitHub issue #{issue_number}...")
    agenda = fetch_github_issue_agenda(issue_number)
    if not agenda:
        print("Could not fetch agenda")
        return False

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

    # Build prompt
    full_prompt = f"""## Meeting Agenda

{agenda}

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

    # Call Claude API
    print(f"Calling {model}...")
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


def main():
    parser = argparse.ArgumentParser(
        description='Generate tldr.json summary using Claude API',
        epilog='Example: python generate_summary.py --call acde --number 226'
    )
    parser.add_argument('--call', '-c', help='Call type (e.g., acde, acdc, acdt)')
    parser.add_argument('--number', '-n', type=int, help='Call number (e.g., 226)')
    parser.add_argument('--dir', '-d', type=Path, help='Meeting directory (alternative to --call/--number)')
    parser.add_argument('--prompt', '-p', type=Path, default=DEFAULT_PROMPT,
                        help='Prompt file (default: asset_pipeline/prompts/summarize.md)')
    parser.add_argument('--model', '-m', default='claude-sonnet-4-5-20250929',
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
