# Asset Pipeline

Scripts for downloading, processing, and cleaning Zoom meeting assets for Ethereum All Core Devs calls.

## Overview

The asset pipeline handles:
1. Downloading Zoom recordings, transcripts, chat logs, and AI summaries
2. Cleaning transcripts to fix Ethereum-specific terminology errors
3. Generating human-reviewable changelogs before applying corrections

## Prerequisites

- Python 3.10+
- Zoom OAuth credentials configured in `.env`
- Anthropic API key for transcript cleaning

Required environment variables (in `.github/ACDbot/.env`):
```
ZOOM_ACCOUNT_ID=...
ZOOM_CLIENT_ID=...
ZOOM_CLIENT_SECRET=...
ANTHROPIC_API_KEY=...
```

Install dependencies:
```bash
pip install anthropic pyyaml python-dotenv requests
```

## Directory Structure

Assets are saved to `.github/ACDbot/artifacts/<series>/<date>_<number>/`:
```
artifacts/
├── acde/
│   ├── 2024-12-12_226/
│   │   ├── config.json              # Issue number, YouTube URL, sync offsets
│   │   ├── transcript.vtt           # Original Zoom transcript
│   │   ├── transcript_changelog.tsv # Generated corrections (review before applying)
│   │   ├── transcript_corrected.vtt # Cleaned transcript
│   │   ├── chat.txt                 # Zoom chat log
│   │   ├── summary.json             # Zoom AI summary
│   │   └── tldr.json                # Structured meeting summary (optional)
│   └── ...
├── acdc/
└── ...
```

## Quick Start

Use `run_pipeline.py` to run the full pipeline with a single command:

```bash
# Process a specific meeting
python run_pipeline.py --call acde --number 226

# Process the most recent meeting in a series
python run_pipeline.py --call acdc --recent
```

The pipeline will:
1. Download assets from Zoom (transcript, chat, summary)
2. Generate a changelog of corrections using Claude
3. **Pause for your review** - preview corrections and edit if needed
4. Apply corrections to create `transcript_corrected.vtt`
5. (Optional) Generate structured summary (`tldr.json`)

Options:
- `--call`, `-c` (required): Call type (acde, acdc, acdt, epbs, focil, etc.)
- `--number`, `-n`: Call number (e.g., 226)
- `--recent`: Process the most recent meeting for the series
- `--resume`: Skip download/changelog generation, jump to review step
- `--open-editor`: Open changelog in `$EDITOR` during review
- `--model`, `-m`: Claude model for changelog generation (default: `claude-opus-4-5-20251101`)
- `--summarize`: Generate structured summary after corrections

Example workflow:
```bash
# Run full pipeline
python run_pipeline.py --call acde --recent

# Run full pipeline with summary generation
python run_pipeline.py --call acde --recent --summarize

# If you need to re-review or re-apply corrections
python run_pipeline.py --call acde --number 226 --resume --open-editor
```

---

## Manual Workflow

The individual scripts can also be run separately for more control.

### Step 1: Download Assets

Download assets for a specific meeting series using `download_zoom_assets.py`:

```bash
# Download the most recent meeting
python download_zoom_assets.py --series-name acde --recent

# Download the 5 most recent meetings
python download_zoom_assets.py --series-name acde --recent 5

# Download assets for a specific date
python download_zoom_assets.py --series-name acde --date 2024-12-12

# Download by specific meeting ID/UUID
python download_zoom_assets.py --series-name acde --meeting-id <uuid>
```

Options:
- `--series-name` (required): Call series name (e.g., `acde`, `acdc`, `epbs`, `focil`)
- `--recent N`: Download N most recent meetings (default: 1)
- `--date YYYY-MM-DD`: Download meeting on a specific date
- `--meeting-id`: Download a specific meeting by ID/UUID
- `--min-duration`: Minimum meeting duration in minutes (default: 10)

### Step 2: Generate Changelog

Review the transcript for errors, then generate a changelog of corrections:

```bash
# Using call type and number (recommended)
python generate_changelog.py --call acde --number 226

# Using explicit paths
python generate_changelog.py --transcript path/to/transcript.vtt
```

Options:
- `--call`, `-c`: Call type (acde, acdc, acdt, etc.)
- `--number`, `-n`: Call number
- `--transcript`, `-t`: Explicit input VTT path
- `--vocab`, `-v`: Vocabulary file (default: `ethereum_vocab.yaml`)
- `--output`, `-o`: Output TSV path
- `--model`, `-m`: Claude model (default: `claude-opus-4-5-20251101`)

The script outputs a TSV file with columns:
- `original`: The misspelled term
- `corrected`: The correct term
- `confidence`: high/medium/low

**Important**: Review `transcript_changelog.tsv` before proceeding. Remove any incorrect suggestions.

### Step 3: Apply Changelog

After reviewing, apply the corrections:

```bash
# Using call type and number
python apply_changelog.py --call acde --number 226

# Using explicit paths
python apply_changelog.py --input transcript.vtt --changelog transcript_changelog.tsv
```

Options:
- `--call`, `-c`: Call type
- `--number`, `-n`: Call number
- `--input`, `-i`: Input VTT file
- `--changelog`: Changelog TSV file
- `--output`, `-o`: Output VTT file

Output: `transcript_corrected.vtt`

### Step 4: Generate Summary (Optional)

Generate a structured JSON summary (`tldr.json`) of the meeting:

```bash
# Using call type and number
python generate_summary.py --call acde --number 226

# Using explicit directory path
python generate_summary.py --dir artifacts/acde/2024-12-12_226
```

Options:
- `--call`, `-c`: Call type (acde, acdc, acdt, etc.)
- `--number`, `-n`: Call number
- `--dir`, `-d`: Meeting directory (alternative to --call/--number)
- `--prompt`, `-p`: Custom prompt file (default: `scripts/prompts/summarize.md`)
- `--model`, `-m`: Claude model (default: `claude-3-5-sonnet-20241022`)
- `--force`, `-f`: Regenerate even if `tldr.json` exists

The script fetches the meeting agenda from the GitHub issue and uses it along with the transcript and chat to generate a structured summary with highlights, action items, decisions, and targets.

### Step 5: Copy into Forkcast

If doing this for Forkcast's sake, paste the generated directory and files into Forkcast's `/artifacts/` directory.

## Files

| File | Description |
|------|-------------|
| `run_pipeline.py` | Orchestrates the full pipeline with interactive review |
| `download_zoom_assets.py` | Downloads transcripts, chat, summaries from Zoom API |
| `generate_changelog.py` | Uses Claude to identify transcript corrections |
| `apply_changelog.py` | Applies corrections from changelog to transcript |
| `generate_summary.py` | Generates structured meeting summary (tldr.json) using Claude |
| `ethereum_vocab.yaml` | Vocabulary reference for Ethereum terminology |

## Vocabulary Reference

`ethereum_vocab.yaml` contains:
- Client names (Geth, Nethermind, Prysm, etc.)
- Upgrade names (Pectra, Fusaka, Glamsterdam)
- Acronyms (EIP, EOF, ePBS, PeerDAS, FOCIL)
- Common transcription error patterns

Update this file to add new terminology or common errors.
