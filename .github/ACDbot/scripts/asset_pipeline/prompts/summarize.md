Generate a structured JSON summary of the Ethereum Core Developer meeting with highlights, action items, decisions, and target dates.
## Input Files
- agenda - Meeting agenda with section headers
- example output from a prior summarization
- transcript.vtt - WebVTT transcript with timestamps
- chat.txt - Meeting chat messages with timestamps
- summary.json - AI-generated summary (optional/supplemental)
## Output Format
Generate a JSON structure with the following schema:

```json
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
```

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
Be highly selective. Include only what a core developer **must know** if they missed the call.

#### INCLUDE:
- Decisions or changes affecting protocol specs
- New devnet launches, fork dates, or schedule changes
- Critical bugs or security issues discussed
- Significant blockers or delays announced
- Cross-team coordination requirements
- Breaking changes to shared infrastructure

#### EXCLUDE:
- Routine client progress updates ("Client X made progress on feature Y")
- Minor bug fixes already resolved
- Work-in-progress without concrete outcomes
- Incremental test result improvements
- Status updates that don't require action from others

#### Guidelines:
- Include specific numbers/dates when mentioned (e.g., "10 target/15 max blobs")
- Each highlight should be self-contained and understandable without context
- Order chronologically within each category
- **Target ~3-5 highlights per category maximum** - if you have more, keep only the most important
### Action Items
Focus on **cross-team coordination and ecosystem-wide awareness** rather than individual development tasks.

#### INCLUDE:
- Cross-team coordination needs (e.g., "All CL teams coordinate on devnet timing")
- Community feedback requests (e.g., "Gather app developer feedback on gas repricing")
- Specification/standards work affecting multiple teams
- Breaking changes requiring broad communication
- Important deadlines affecting multiple parties
- External dependencies (e.g., "Coordinate with L2 teams on rollup implications")

#### EXCLUDE (routine development work):
- Individual bug fixes ("Fix MIN_EPOCHS handling")
- Client-specific PR merges ("Besu: Merge metrics and prefetch PRs")
- Standard implementation work ("Implement engine API method")
- Code review requests for client-specific code ("Review and merge BAL PRs")
- Client-internal tasks without cross-team coordination aspect
- Work already implied by being a core developer
- Generic/obvious statements ("All EL teams: Increase test pass rates") - this is implied by their job

#### Key distinction - Shared vs Client-specific:
- **Shared specs/APIs** (execution-apis, consensus-specs, beacon-APIs) → INCLUDE
  - e.g., "Merge execution-apis PRs 726 and 727" affects all EL teams
- **Client implementations** (Geth, Besu, Reth, Lighthouse, etc.) → EXCLUDE
  - e.g., "Besu: Merge metrics PRs" is internal to one team

#### Quality filter - before including, ask:
1. Would teams outside the mentioned team benefit from knowing this?
2. Does this require coordination between multiple parties?
3. Is this more than routine development work?

If all answers are "no", exclude the item.
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
- Be ruthlessly selective. This summary is for busy developers - only include what they MUST know.
- Combine, condense, deduplicate aggressively. When in doubt, leave it out.
- Reference the example output for approximate length, but aim ~25% shorter than a comprehensive list.
- Distill each line item to 12 words or less.
- Action items should be rare (0-3 per meeting) - most meetings have no cross-team coordination needs.