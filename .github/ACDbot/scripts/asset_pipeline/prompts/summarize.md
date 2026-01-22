Generate a structured JSON summary of the Ethereum Core Developer meeting with highlights, action items, decisions, and target dates.
## Input Files
- agenda - Meeting agenda with section headers
- example output from a prior summarization
- transcript.vtt - WebVTT transcript with timestamps
- chat.txt - Meeting chat messages with timestamps
- summary.json - AI-generated summary (optional/supplemental)
## Output Format
Generate a JSON structure with the following schema:
json
{
  "meeting": "[Meeting Name] - [Date]",
  "highlights": {
    "[category_name]": [
      {
        "timestamp": "HH:MM:SS",
        "highlight": "[Concise description of important point]"
      }
    ]
  },
  "action_items": [
    {
      "timestamp": "HH:MM:SS",
      "action": "[What needs to be done]",
      "owner": "[Who is responsible]"
    }
  ],
  "decisions": [
    {
      "timestamp": "HH:MM:SS",
      "decision": "[Formal decision that was made]"
    }
  ],
  "targets": [
    {
      "timestamp": "HH:MM:SS",
      "target": "[Scheduled event or milestone confirmed]"
    }
  ]
}

## Category Guidelines
Use these standard categories for highlights (add others as needed):
- fork_status_and_schedule - Hard forks, BPOs, network upgrades
- critical_infrastructure - Urgent changes, shutdowns, migrations
- client_updates - Client releases, bug fixes, new features
- testing_progress - devnets, test results, compatibility updates
- documentation - Blog posts, specs, guides being created/updated
- organizational - Process changes, communication updates, meeting schedules
## Extraction Rules
### Highlights
- Extract the most important technical updates and changes
- Include specific numbers/dates when mentioned (e.g., "10 target/15 max blobs")
- Each highlight should be self-contained and understandable without context
- Order chronologically within each category
### Action Items
Only include explicit commitments where someone agrees to do something:
- "I'll/We'll create..." → Include
- "Will release..." → Include
- "Going to work on..." → Include
- General discussion without commitment → Exclude
- Past tense descriptions → Exclude
### Decisions Made
Only formal decisions with clear consensus:
- "We decided to..." → Include
- "Will be shut down by [date]" → Include
- "Keeping [feature] as currently specified" → Include
- Proposals or suggestions → Exclude
### Notable Targets
Scheduled events and confirmed milestones:
- Fork dates
- devnet launches
- Spec finalizations
- Release schedules
## Timestamp Rules
- Use exact timestamps from transcript.vtt
- Format: "HH:MM:SS"
- Use the timestamp where the topic/decision/action BEGINS
- For action items, use the start of when the commitment is made
## Quality Checks
1. Every timestamp must exist in the transcript
2. Action items must have clear owners (team or group)
3. Highlights should cover all major topics from the agenda
4. Descriptions should be distilled to their simplest form
5. Remove duplicate information across sections
## Priority Order
When reviewing the transcript, prioritize capturing:
1. Network-critical changes (forks, shutdowns)
2. Security fixes and bug resolutions
3. Protocol specification decisions
4. Testing milestones and results
5. Coordination changes affecting multiple teams
6. Documentation for external users/operators
## Example Patterns to Look For
**Action Item Patterns:**
- "I'll publish/create/release..."
- "We're going to..."
- "[Team] will..."
- "Let me work on..."
**Decision Patterns:**
- "We've decided..."
- "The consensus is..."
- "We're keeping/changing..."
- "It will be [specific outcome]"
**Commitment Patterns:**
- "Scheduled for [date]"
- "Will happen on [date]"
- "Target is [date/milestone]"
- "[Thing] is finalized/ready"
Generate the complete JSON summary based on the provided transcript and supplemental files.

IMPORTANT:
- Combine, condense, deduplicate where possible. Remove items that may be superfluous or unimportant enough for a summary. Reference the example output provided for an approximate desired length.
- Distill each line item to 12 words or less.