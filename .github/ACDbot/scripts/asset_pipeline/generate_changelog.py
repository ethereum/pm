#!/usr/bin/env python3
"""
Generate a changelog of corrections for an Ethereum transcript using Claude API.
Review transcript_changelog.tsv before applying with apply_changelog.py
"""

import argparse
import csv
import re
from pathlib import Path
from dotenv import load_dotenv
import anthropic

# Load .env from ACDbot directory
load_dotenv(Path(__file__).parent.parent.parent / ".env")

PROMPT = """## Task
Identify misspelled Ethereum-specific terms in this WebVTT transcript that should be corrected.

## Rules
1. Output ONLY individual terms (1-3 words max), NOT full phrases or sentences
2. Terms must be safe for global find/replace (no common words that could cause false positives)
3. Focus on proper nouns, protocol names, technical terms from the vocabulary reference
4. Only correct obvious transcription errors where context supports the correction
5. When uncertain, leave unchanged

## Examples of GOOD corrections (specific terms):
- Nethermine → Nethermind
- Glamstadam → Glamsterdam
- Fossil → FOCIL
- Allcodev's → All Core Devs

## Examples of BAD corrections (avoid these):
- Full sentences or long phrases
- Common words like "the", "from", "and"
- Phrases with punctuation that may not match exactly

## Output Format
Return ONLY a TSV (tab-separated) with these columns, no markdown formatting:
original\tcorrected\tconfidence

- confidence: high (obvious error), medium (likely error), low (uncertain)
- Each row should be a unique term (don't repeat the same correction)

If no changes needed, return only the header row.

## Vocabulary Reference
{vocab}

## Transcript
{transcript}
"""

MODEL_PRICING = {
    # Pricing per million tokens (input, output)
    "claude-opus-4-5-20251101": (15.00, 75.00),
    "claude-sonnet-4-20250514": (3.00, 15.00),
    "claude-haiku-3-5-20241022": (0.80, 4.00),
}

# Base paths relative to this script
SCRIPT_DIR = Path(__file__).parent
ARTIFACTS_DIR = SCRIPT_DIR.parent.parent / "artifacts"
DEFAULT_VOCAB = SCRIPT_DIR / "ethereum_vocab.yaml"


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

def generate_changelog(transcript: str, vocab: str, model: str = "claude-opus-4-5-20251101"):
    """Call Claude API to generate changelog. Returns (text, usage_dict)."""
    client = anthropic.Anthropic()

    message = client.messages.create(
        model=model,
        max_tokens=8096,
        messages=[
            {"role": "user", "content": PROMPT.format(vocab=vocab, transcript=transcript)}
        ]
    )

    usage = {
        "input_tokens": message.usage.input_tokens,
        "output_tokens": message.usage.output_tokens,
    }
    return message.content[0].text, usage


def calculate_cost(model: str, usage: dict) -> float:
    """Calculate cost in USD based on model and token usage."""
    input_price, output_price = MODEL_PRICING.get(model, (0, 0))
    input_cost = (usage["input_tokens"] / 1_000_000) * input_price
    output_cost = (usage["output_tokens"] / 1_000_000) * output_price
    return input_cost + output_cost

def parse_response(response: str) -> list[tuple]:
    """Parse Claude's TSV response into list of tuples."""
    rows = []
    lines = response.strip().split('\n')

    for line in lines:
        # Skip header
        if line.startswith('original') or not line.strip():
            continue
        parts = line.split('\t')
        if len(parts) >= 3:
            rows.append((parts[0], parts[1], parts[2]))

    return rows

def main():
    parser = argparse.ArgumentParser(
        description='Generate changelog using Claude API',
        epilog='Example: python generate_changelog.py --call acde --number 226'
    )
    # Shorthand arguments for call directory lookup
    parser.add_argument('--call', '-c', help='Call type (e.g., acde, acdc, acdt)')
    parser.add_argument('--number', '-n', type=int, help='Call number (e.g., 226)')
    # Explicit path arguments (override call/number)
    parser.add_argument('--transcript', '-t', help='Input VTT file')
    parser.add_argument('--vocab', '-v', help='Vocabulary YAML file')
    parser.add_argument('--output', '-o', help='Output changelog TSV')
    parser.add_argument('--model', '-m', default='claude-opus-4-5-20251101', help='Claude model to use')
    args = parser.parse_args()

    # Resolve paths based on call/number or explicit arguments
    if args.call and args.number:
        call_dir = find_call_directory(args.call, args.number)
        transcript_path = args.transcript or call_dir / "transcript.vtt"
        vocab_path = args.vocab or DEFAULT_VOCAB
        output_path = args.output or call_dir / "transcript_changelog.tsv"
        print(f"Using call directory: {call_dir}")
    else:
        transcript_path = args.transcript or "transcript.vtt"
        vocab_path = args.vocab or DEFAULT_VOCAB
        output_path = args.output or "transcript_changelog.tsv"

    # Load files
    with open(transcript_path, 'r', encoding='utf-8') as f:
        transcript = f.read()
    with open(vocab_path, 'r', encoding='utf-8') as f:
        vocab = f.read()

    print(f"Loaded transcript ({len(transcript)} chars) and vocab ({len(vocab)} chars)")
    print(f"Calling {args.model}...")

    # Generate changelog via API
    response, usage = generate_changelog(transcript, vocab, args.model)
    corrections = parse_response(response)

    # Write TSV
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(["original", "corrected", "confidence"])
        for row in corrections:
            writer.writerow(row)

    # Display usage and cost
    cost = calculate_cost(args.model, usage)
    print(f"\nTokens: {usage['input_tokens']:,} input, {usage['output_tokens']:,} output")
    print(f"Cost: ${cost:.4f}")

    print(f"\nGenerated {output_path} with {len(corrections)} corrections")
    if args.call and args.number:
        print(f"Review the file, then run: python apply_changelog.py -c {args.call} -n {args.number}")
    else:
        print("Review the file, then run: python apply_changelog.py")

if __name__ == '__main__':
    main()