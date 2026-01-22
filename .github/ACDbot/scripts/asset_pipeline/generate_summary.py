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
from html import unescape
from pathlib import Path

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv(Path(__file__).parent.parent.parent / ".env")

# Base paths relative to this script
SCRIPT_DIR = Path(__file__).parent
ARTIFACTS_DIR = SCRIPT_DIR.parent.parent / "artifacts"
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

MODEL_PRICING = {
    # Pricing per million tokens (input, output)
    "claude-opus-4-5-20251101": (15.00, 75.00),
    "claude-sonnet-4-5-20250929": (3.00, 15.00),
    "claude-sonnet-4-20250514": (3.00, 15.00),
    "claude-3-5-sonnet-20241022": (3.00, 15.00),
    "claude-haiku-3-5-20241022": (0.80, 4.00),
}


def find_call_directory(call: str, number: int) -> Path:
    """Find the directory for a given call type and number."""
    call_dir = ARTIFACTS_DIR / call
    if not call_dir.exists():
        raise FileNotFoundError(f"Call type directory not found: {call_dir}")

    # Find directory ending with _{number} (zero-padded to 3 digits)
    padded = str(number).zfill(3)
    for d in call_dir.iterdir():
        if d.is_dir() and d.name.endswith(f"_{padded}"):
            return d
        # Also check non-padded
        if d.is_dir() and d.name.endswith(f"_{number}"):
            return d

    raise FileNotFoundError(f"No directory found for {call} #{number}")


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


def calculate_cost(model: str, usage: dict) -> float:
    """Calculate cost in USD based on model and token usage."""
    input_price, output_price = MODEL_PRICING.get(model, (0, 0))
    input_cost = (usage["input_tokens"] / 1_000_000) * input_price
    output_cost = (usage["output_tokens"] / 1_000_000) * output_price
    return input_cost + output_cost


def generate_summary(
    meeting_dir: Path,
    prompt_file: Path,
    call_type: str,
    model: str = "claude-sonnet-4-5-20250929",
    force: bool = False
) -> bool:
    """Generate tldr.json using Claude API."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("ANTHROPIC_API_KEY not found in environment")
        return False

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
        with open(config_path) as f:
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

{("(Available at summary.json)" if summary_path.exists() else "(No summary file available)")}

---

{prompt_template}"""

    # Call Claude API
    print(f"Calling {model}...")
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    payload = {
        "model": model,
        "max_tokens": 16000,
        "messages": [{"role": "user", "content": full_prompt}]
    }

    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=payload,
            timeout=300
        )

        if response.status_code != 200:
            print(f"API request failed: {response.status_code} - {response.text}")
            return False

        result = response.json()
        usage = {
            "input_tokens": result.get("usage", {}).get("input_tokens", 0),
            "output_tokens": result.get("usage", {}).get("output_tokens", 0),
        }

        if "content" not in result or not result["content"]:
            print("Unexpected API response format")
            return False

        response_text = result["content"][0]["text"]

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
            with open(tldr_path, 'w') as f:
                json.dump(tldr_data, f, indent=2)

            cost = calculate_cost(model, usage)
            print(f"\nTokens: {usage['input_tokens']:,} input, {usage['output_tokens']:,} output")
            print(f"Cost: ${cost:.4f}")
            print(f"\nGenerated {tldr_path}")
            return True

        except json.JSONDecodeError as e:
            print(f"Response was not valid JSON: {e}")
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
