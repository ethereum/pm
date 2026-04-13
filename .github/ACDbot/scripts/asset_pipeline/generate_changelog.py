#!/usr/bin/env python3
"""
Generate a changelog of corrections for an Ethereum transcript using Claude API.
Review transcript_changelog.tsv before applying with apply_changelog.py
"""

import argparse
import csv
from pathlib import Path

import anthropic
from dotenv import load_dotenv

# Load .env from ACDbot directory
load_dotenv(Path(__file__).parent.parent.parent / ".env")

from utils import SCRIPT_DIR, find_call_directory, calculate_cost

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

DEFAULT_VOCAB = SCRIPT_DIR / "ethereum_vocab.yaml"

def generate_changelog(transcript: str, vocab: str, model: str = "claude-opus-4-5-20251101"):
    """Call Claude API to generate changelog. Returns (text, usage_dict)."""
    client = anthropic.Anthropic()

    message = client.messages.create(
        model=model,
        max_tokens=8192,
        messages=[
            {"role": "user", "content": PROMPT.format(vocab=vocab, transcript=transcript)}
        ]
    )

    usage = {
        "input_tokens": message.usage.input_tokens,
        "output_tokens": message.usage.output_tokens,
    }
    return message.content[0].text, usage

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
    print(f"⏳ Calling Claude API ({args.model}) to generate corrections - this may take a minute...")

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