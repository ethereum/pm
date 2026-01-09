Championing an EIP to get included in an Ethereum hard fork can be a non-trivial time & energy commitment. It is recommended to familiarize yourself with the process before volunteering.

# EIP Champion Guide

A lightweight guide for championing an EIP through a fork planning cycle.

---

## What being a “champion” means

*tl;dr:* A champion does the work to create strong consensus across the majority of client teams that the EIP is needed & ready. EIPs benefit from a technical champion who understands implementations and can keep process moving.

If you champion an EIP, you are the point person who keeps it moving:

- coordinate implementation progress (you or client teams)
- surface concerns and drive them to resolution, often via spec iteration
- keep information current & easy to find
- engage in predictable venues (calls + Discord) when the EIP is being discussed

## Checklist

1. **Time commitment:** are you actually available in the next few months to do coordination + follow-ups?
2. **Draft a Forkcast entry:** template at the bottom of this doc.
3. **Know who needs to understand the feature**
    - Execution vs consensus vs cross-layer
    - Which client teams are most impacted (who you’ll need to engage)
    - What other stakeholders need to know about these changes?
4. **Familiarize yourself with known concerns / tradeoffs:** anything that needs benchmarking, careful reasoning, or is likely contentious
5. **Loosely consider an implementation plan:** who’s likely to implement, and what’s the *first* concrete artifact / milestone that will need to happen
6. **Communications:** plan to be responsive (R&D Discord / GitHub / etc)

## Technical details

### Headliners vs non-headliners

- Headliners (major features) are chosen first, aiming to CFI a maximum of one per layer.
- Non-headliners are then collected until the proposal deadline and evaluated as a batch.

### EIP stages (PFI → CFI → SFI)

Stages are defined in [EIP-7723](https://eips.ethereum.org/EIPS/eip-7723).

- **Proposed for Inclusion (PFI)**

    An EIP becomes PFI when someone opens a PR to add it to the fork’s Meta EIP PFI list during the designated PFI window. Champion actions after PFI:

    1. Ensure implementations are being created (you or by engaging client teams).
    2. Surface concerns early and address them (often via spec iteration).
    3. Stay active and responsive in Eth R&D Discord.
    4. Create/maintain a strong Forkcast entry - optional, but a good way to get your EIP better understood and on more radars. Your goal is to enable an *informed* signal from client teams. If it isn’t well understood or has unknowns, build shared understanding and drive down uncertainty (explanations, answering questions, spec work, breakout if needed).

- **Considered for Inclusion (CFI)**

    Moving PFI → CFI happens after the EIP is discussed on an ACD call during the designated discussion window and rough consensus is achieved. The ACD facilitator then updates its status on the Fork Meta EIP.

- **Scheduled for Inclusion (SFI)**

    SFI generally implies the EIP has achieved rough consensus across client teams and is on the implementation/testing path (devnets → testnets → mainnet).

### Implementations & Tests

It is strongly encouraged to implement the EIP's protocol changes in the relevant Python specifications as early as possible. This allows the community to help collaboratively disambiguate the specifications and generate reference tests for client teams. Note that in order for an EIP to move to the SFI stage, it MUST have executable specifications (see [EIP-7723](https://eips.ethereum.org/EIPS/eip-7723)).

<details>
<summary>If your EIP impacts the Execution Layer:</summary>

- Implement your changes in the [execution-specs](https://github.com/ethereum/execution-specs) (EELS)
  - EIP authors are encouraged to attempt the implementation on their own. Once a PR is created, EELS maintainers regularly step in to provide feedback or polish the implementation.
  - Reference the [EIP Author's Manual](https://github.com/ethereum/execution-specs/blob/master/EIP_AUTHORS_MANUAL.md).
  - Add test cases in an appropriate sub-folder of [`tests/unscheduled/`](https://github.com/ethereum/execution-specs/tree/b3543e94d12288e994fc1adea606c1a417db4a9f/tests/unscheduled). EELS maintainers will help with coverage, but simple tests can help you to verify your implementation.
- For any help you may need, reach out to the [STEEL Team](https://steel.ethereum.foundation/) in the [Eth R&D Discord](https://discord.gg/EVTQ9crVgQ), `#el-testing` channel.

</details>

<details>
<summary>If your EIP impacts the Consensus Layer:</summary>

- Implement the feature in the [consensus-specs](https://github.com/ethereum/consensus-specs) repository. Once a PR is created, maintainers will provide feedback and guide next steps.
- Update [generators](https://github.com/ethereum/consensus-specs/tree/dev/tests/generators) and generate client tests.  
- Reference the feature addition [docs](https://github.com/ethereum/consensus-specs/blob/master/docs/docs/new-feature.md)
- Reach out for help in the [Eth R&D Discord](https://discord.gg/EVTQ9crVgQ), `#cl-testing` channel.

</details>

## Where decisions happen

- **ACD**
  - **ACDE / ACDC:** higher-level planning + “what goes in the fork” decisions
  - **ACDT:** implementation/testing. Usually for current forks once something is already CFI’d.
  - **Agendas:** organized in [**ethereum/pm** repo issues](github.com/ethereum/pm/issues). ACD agendas are typically updated the day before the call. Anyone is free to leave a comment on the call issue, requesting for their topic to be added to the agenda.
- **Async:** Eth R&D Discord is the primary async venue.

## Forkcast

When your EIP is actively in the conversation, you can use Forkcast as a tool to help ACD participants understand and keep up-to-date with the EIP. Fill out the Forkcast template below and PR it into the [EIPs directory](https://github.com/ethereum/forkcast/tree/main/src/data/eips). Keep the Forkcast entry updated after any significant status changes.

## Calls: expectations

If your EIP is on the agenda, it is strongly encouraged to attend the relevant ACD call.

If you can’t attend:

- submit a written update ahead of time. These can be added to the call agenda if appropriate or in the relevant R&D discord channel. Or you can send someone else to represent your update
- [catch up](https://forkcast.org/calls/) by rewatching the call / reading the transcript and summary
- decisions *can* be made without you, so attendance (or sending a representative) is strongly encouraged

## Decisions: avoid being surprised

To know when decisions are likely to be made,

- follow the [EF blog](https://blog.ethereum.org/) Checkpoint series
- read messages in Eth R&D Discord #allcoredevs
- watch the [fork timeline](https://forkcast.org/upgrade/glamsterdam#glamsterdam-timeline) on Forkcast, catch up on the [Calls](https://forkcast.org/calls/) page with transcripts & summaries
- check ethereum/pm agendas the day before ACD calls

## Running a Breakout call

### When to start a breakout

Breakout calls are organized via issues in the ethereum/pm Github repo and you, as the call facilitator, are responsible for getting the right people to attend. Start a breakout if:

- there’s active development / implementation work or open questions to address, and
- it can’t fit responsibly in the ACD agenda
- there’s enough interest that multiple participants will attend

### Setting up a breakout call

Contact Protocol Support:

- **wolovim** (`@wolovim` on Discord / Twitter) or
- **nixo** (`@nixo.eth` on Discord, `nixo@ethereum.org` by email)

Provide: title, cadence, reason for the breakout, associated EIP(s), target fork

You can use your own zoom meeting or you can use the EF zoom-bot to create the zoom link. The benefit of the EF zoom-bot is that it provides transcripts, an AI summary, and youtube video upload.

## Templates

### Forkcast TL;DR

```markdown
{
    "id":,
    "title": "",
    "status": "Draft",
    "description": "",
    "author": "",
    "type": "Standards Track",
    "category": "Core",
    "createdDate": "YYYY-MM-DD",
    "discussionLink": "",
    "reviewer": "expert",
    "forkRelationships": [
      {
        "forkName": "Glamsterdam",
        "status": "Proposed",
        "layer": "choose EL or CL",
        "champion": {
          "name": "Your Name",
          "discord": "yourdiscordusername"
      }
      }
    ],
    "laymanDescription": "<=60 words",
    "stakeholderImpacts": {
      "endUsers": {
        "description": "~20 words"
      },
      "appDevs": {
        "description": "~20 words"
      },
      "walletDevs": {
        "description": "~20 words"
      },
      "toolingInfra": {
        "description": "~20 words"
      },
      "layer2s": {
        "description": "~20 words"
      },
      "stakersNodes": {
        "description": "~20 words"
      },
      "clClients": {
        "description": "~20 words"
      },
      "elClients": {
        "description": "~20 words"
      }
    },
    "benefits": [
      "16 words max",
      "16 words max",
      "16 words max",
      "16 words max"
    ],
    "tradeoffs": [
      "16 words max",
      "16 words max"
    ],
  },
```
