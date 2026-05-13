# Ethereum Project Management Repository

This repository is used for project management for initiatives affecting the Ethereum protocol.

This repository is for:

- [Execution](https://github.com/ethereum/pm/issues?q=is%3Aissue%20label%3AACD%20label%3AExecution) (ACDE) and [Consensus](https://github.com/ethereum/pm/issues?q=is%3Aissue%20label%3AACD%20label%3AConsensus) (ACDC) Layer AllCoreDevs meetings
- [Testing](https://github.com/ethereum/pm/issues?q=is%3Aissue%20label%3AACD%20ACDT) meetings
- [Breakout calls](https://github.com/ethereum/pm/blob/master/Breakout-Room-Meetings/active-breakout-series.md) on specific Ethereum core development topics

Agendas for these meetings can be found on the [Issues](https://github.com/ethereum/pm/issues) tab. This [Google Calendar](https://calendar.google.com/calendar/embed?src=c_upaofong8mgrmrkegn7ic7hk5s%40group.calendar.google.com) also tracks upcoming protocol meetings.

Discussions happen in the [Ethereum R&D Discord server](https://discord.com/invite/qGpsxSA) and on [Ethereum Magicians](https://ethereum-magicians.org/c/protocol-calls/63). Upcoming and past call information, including transcripts, video links, and summaries, can be found on [Forkcast](https://forkcast.org/calls/) and in the generated meeting table below. Recordings are hosted on the [@EthereumProtocol YouTube channel](https://www.youtube.com/@ethereumprotocol).

## Machine-Readable Meeting Index

Meeting metadata is maintained in a structured data source instead of being manually maintained only in this README:

- [`data/meetings.json`](data/meetings.json) contains the canonical meeting index.
- [`data/meetings.schema.json`](data/meetings.schema.json) defines the validation schema for meeting metadata.
- The meeting table in this README is generated from `data/meetings.json`.

This keeps the README human-facing while making protocol meeting metadata reliable, queryable, and reusable by external tooling such as Forkcast, dashboards, calendars, bots, archival tools, and CI checks.

Each meeting entry supports the following canonical fields:

- `type`: Meeting series, such as `ACDE`, `ACDC`, or `ACDT`.
- `number`: Meeting number within the series.
- `date`: Meeting date in ISO 8601 format (`YYYY-MM-DD`).
- `agenda`: GitHub issue URL for the agenda.
- `summary`: Summary or notes URL.
- `discussion`: Ethereum Magicians, forum, Reddit, X/Twitter, or other discussion URL.
- `recording`: Recording URL.
- `logs`: Transcript or log URL.
- `forkcast`: Forkcast call URL.

CI should validate:

- JSON Schema compliance.
- Required fields.
- Valid URL formats.
- Duplicate meeting numbers per meeting type.
- Date ordering.
- Generated README table consistency.
- Broken or unreachable links where practical.

## AllCoreDevs Meetings Overview

### Purpose

AllCoreDevs is a weekly meeting held by the Ethereum development community to discuss technical issues and coordinate work on the Ethereum protocol. The meetings are attended by core contributors from various organizations. During the call, participants discuss potential protocol changes, testing, and other related issues.

On one week, the focus of the call is on Ethereum's consensus layer, including proof-of-stake and the Beacon Chain. On alternate weeks, the focus of the call is on Ethereum's execution layer, including the EVM, gas schedules, and related execution-layer changes.

### Agendas

To add an item to an [agenda](https://github.com/ethereum/pm/issues), add a comment to one of the agenda issues. Anyone is welcome to add an item to the agenda as long as it follows these guidelines:

- The topic is technical in nature.
- The topic involves the Ethereum protocol at a low level. Ethereum applications and ERCs are generally not agenda topics unless they directly relate to protocol changes.
- The topic should not be primarily philosophical. Core developer meetings are not intended to decide broad philosophical or contentious issues that should be decided by the wider community. [Ethereum Magicians](https://ethereum-magicians.org/) is a better venue for those discussions.

### Who Can Attend

Protocol developers, researchers, and EIP authors are invited to attend the meetings. Regular attendees include Ethereum client developers, testing and security teams, and independent contributors.

Sometimes non-core contributors with specific expertise are invited to discuss a particular agenda item. If you feel you would contribute to the meetings with your attendance, reach out on the [Ethereum R&D Discord](https://discord.com/invite/qGpsxSA) in the relevant channel or contact [Nixo](mailto:nixorokish@pm.me).

### Who Facilitates the Meetings

Current facilitators:

- **Execution**: coleads [Ansgar Dietrichs](https://github.com/adietrichs) and [Nixo](https://github.com/nixorokish/)
- **Consensus**: [Parithosh Jayanthi](https://github.com/parithosh) interim, with [Alex Stokes](https://github.com/ralexstokes) currently out of office
- **Testing**: coleads [EF EthPandaOps team](https://github.com/ethpandaops/) and [EF STEEL team](https://steel.ethereum.foundation/team/)

Past facilitators:

- Tim Beiko
- Danny Ryan
- Hudson Jameson
- Lane Rettig
- George Hallam

Breakout Rooms are usually chaired by the expert or champion for the topic at hand.

### Who Manages This Repo

This repo is managed by the Ethereum Foundation's [Protocol Support team](https://ps.ethereum.foundation/team) and ACD call facilitators.

## Previous AllCoreDevs Meetings

The table below is generated from [`data/meetings.json`](data/meetings.json). Do not edit the generated table manually. Update the source data and regenerate this section instead.

<!-- BEGIN GENERATED MEETINGS TABLE -->
| Date | Type | № | Issue | Summary | Discussion | Recording | Logs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11 May 2026 | ACDT | 79 | [#2038](https://github.com/ethereum/pm/issues/2038) | [forkcast](https://forkcast.org/calls/acdt/079) | [EthMag](https://ethereum-magicians.org/t/28438) | [video](https://youtu.be/2MouT9NiGS8) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-079_2026-05-11) |
| 07 May 2026 | ACDE | 236 | [#2033](https://github.com/ethereum/pm/issues/2033) | [forkcast](https://forkcast.org/calls/acde/236) | [EthMag](https://ethereum-magicians.org/t/28353) | [video](https://youtu.be/19Hi3SbT6tc) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDE/Call-236_2026-05-07) |
| 23 Apr 2026 | ACDE | 235 | [#2015](https://github.com/ethereum/pm/issues/2015) | [forkcast](https://forkcast.org/calls/acde/235) | [EthMag](https://ethereum-magicians.org/t/28203) | [video](https://youtu.be/eSN27EDNdp8) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDE/Call-235_2026-04-23) |
| 20 Apr 2026 | ACDT | 78 | [#2019](https://github.com/ethereum/pm/issues/2019) | [forkcast](https://forkcast.org/calls/acdt/078) | [EthMag](https://ethereum-magicians.org/t/28229) | [video](https://youtu.be/ZvG3OkEt8_o) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-078_2026-04-20) |
| 16 Apr 2026 | ACDC | 177 | [#1990](https://github.com/ethereum/pm/issues/1990) | [forkcast](https://forkcast.org/calls/acdc/177) | [EthMag](https://ethereum-magicians.org/t/28080) | [video](https://youtu.be/KTRviKfUEf4) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDC/Call-177_2026-04-16) |
<!-- END GENERATED MEETINGS TABLE -->