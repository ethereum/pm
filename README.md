# Ethereum Project Management Repository

This repository is used for project management for various initiatives affecting the Ethereum protocol.
This repository is for:
- [Execution](https://github.com/ethereum/pm/issues?q=is%3Aissue%20label%3AACD%20label%3AExecution) and [Consensus](https://github.com/ethereum/pm/issues?q=is%3Aissue%20label%3AACD%20label%3AConsensus) Layer AllCoreDevs meetings
- [Breakout Rooms](https://github.com/ethereum/pm/issues?q=(label%3ABreakout%20label%3AConsensus)%20OR%20(label%3ABreakout%20label%3AExecution)%20) on various L1-related topics
- [L2 interop](https://github.com/ethereum/pm/issues?q=is%3Aissue%20label%3AL2%20)
 breakout meetings

Agendas for these meetings can be found on the [Issues](https://github.com/ethereum/pm/issues) tab. This [Google Calendar](https://calendar.google.com/calendar/embed?src=c_upaofong8mgrmrkegn7ic7hk5s%40group.calendar.google.com) also tracks upcoming protocol meetings.

Past meetings with call summaries, related links, and discussions can be found on [Ethereum Magicians](https://ethereum-magicians.org/c/protocol-calls/63).

## AllCoreDevs Meetings Overview

### Purpose

AllCoreDevs is a weekly meeting held by the Ethereum development community to discuss technical issues and coordinate work on the Ethereum protocol. The meetings are attended by core contributors from various organizations. During the call, participants discuss potential protocol changes, testing, and other related issues.

On one week, the focus of the call is on Ethereum's consensus layer (i.e. proof-of-stake, the Beacon Chain, etc.) and on alternate weeks, the focus of the call is on Ethereum's execution layer (i.e. the EVM, gas schedules, etc.).

The calls are livestreamed and saved on the [@EthereumProtocol YouTube channel](https://www.youtube.com/@ethereumprotocol).

### Agendas

To add an item to an [agenda](https://github.com/ethereum/pm/issues), simply add a comment to one of the agenda issues. Anyone is welcome to add an item to the agenda as long as it follows these guidelines:

- The topic is technical in nature.
- The topic involves the Ethereum protocol at a low-level. This means Ethereum applications and ERCs are generally not allowed as topics, unless their mention relates to protocol changes.
- The topic should not be philosophical. The core developer meetings are not meant to decide philosophical, contentious issues that should be decided by the community. There are exceptions to this, but generally these topics distract from more productive technical discussions. [Ethereum Magicians forum](https://ethereum-magicians.org/) is a better venue for such discussions.

### Who Can Attend

Protocol developers, researchers and EIP authors are invited to attend the meetings. Regular attendees include Ethereum client developers, testing and security teams, and independent contributors.

Sometimes non-core contributors with particular expertise on a topic are invited on to discuss a specific agenda item. If you feel you would contribute to the meetings with your attendance please reach out to [Tim Beiko](mailto:tim@ethereum.org).

### Who Facilitates the Meetings

Current facilitators:
- Execution: [Ansgar Dietrichs](https://github.com/adietrichs) (interim, Oct '25)
- Consensus: [Alex Stokes](https://github.com/ralexstokes) (Sep '24)

Past facilitators:
- Tim Beiko
- Danny Ryan
- Hudson Jameson
- Lane Rettig
- George Hallam

Breakout Rooms are usually chaired by the expert/champion for the topic at hand. The [Ethereum Cat Herders](https://github.com/ethcatherders) provide full transcripts (linked below) for AllCoreDevs meetings, as well as some Breakout Rooms.

While the meetings are independent of any organization, the current facilitators are part of the Ethereum Foundation.

## Previous AllCoreDevs Meetings

| Date | Type | № | Issue | Summary | Discussion | Recording | Logs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 26 Jan 2026 | ACDT | 67 | [#1882](https://github.com/ethereum/pm/issues/1882) | - | [EthMag](https://ethereum-magicians.org/t/27511) | [video](https://youtu.be/EUhKZYGRjBw) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-067_2026-01-26) |
| 22 Jan 2026 | ACDC | 173 | [#1874](https://github.com/ethereum/pm/issues/1874) | [forkcast](https://forkcast.org/calls/acdc/173) | [EthMag](https://ethereum-magicians.org/t/27425) | [video](https://youtu.be/APiyToa6UmI) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDC/Call-173_2026-01-22) |
| 19 Jan 2026 | ACDT | 66 | [#1878](https://github.com/ethereum/pm/issues/1878) | [forkcast](https://forkcast.org/calls/acdt/066) | [EthMag](https://ethereum-magicians.org/t/27395) | [video](https://youtu.be/Y61OpUvVpFM) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-066_2026-01-19) |
| 15 Jan 2026 | ACDE | 228 | [#1867](https://github.com/ethereum/pm/issues/1867) | [forkcast](https://forkcast.org/calls/acde/228) | [EthMag](https://ethereum-magicians.org/t/27400) | [video](https://youtu.be/SMC83TdqgLY) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDE/Call-228_2026-01-15) |
| 12 Jan 2026 | ACDT | 65 | [#1865](https://github.com/ethereum/pm/issues/1865) | [forkcast](https://forkcast.org/calls/acdt/065) | [EthMag](https://ethereum-magicians.org/t/27395) | [video](https://youtu.be/b70x8N8xG2A) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-065_2026-01-12) |
| 08 Jan 2026 | ACDC | 172 | [#1844](https://github.com/ethereum/pm/issues/1844) | [forkcast](https://forkcast.org/calls/acdc/172) | [EthMag](https://ethereum-magicians.org/t/27168) | [video](https://youtu.be/ZXxk3cV7Tjw) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDC/Call-172_2026-01-08) |
| 05 Jan 2026 | ACDE | 227 | [#1854](https://github.com/ethereum/pm/issues/1854) | [forkcast](https://forkcast.org/calls/acde/227) | [EthMag](https://ethereum-magicians.org/t/27356) | [video](https://youtu.be/1B03r5t03bU) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDE/Call-227_2026-01-05) |
| 18 Dec 2025 | ACDE | 226 | [#1837](https://github.com/ethereum/pm/issues/1837) | [forkcast](https://forkcast.org/calls/acde/226) | [EthMag](https://ethereum-magicians.org/t/27004) | [video](https://youtu.be/_KGsKUeH77g) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDE/Call-226_2025-12-18) |
| 15 Dec 2025 | ACDT | 64 | [#1842](https://github.com/ethereum/pm/issues/1842) | [forkcast](https://forkcast.org/calls/acdt/064) | [EthMag](https://ethereum-magicians.org/t/27137) | [video](https://youtu.be/JbHnZnkl2Mc) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-064_2025-12-15) |
| 11 Dec 2025 | ACDC | 171 | [#1825](https://github.com/ethereum/pm/issues/1825) | [forkcast](https://forkcast.org/calls/acdc/171) | [EthMag](https://ethereum-magicians.org/t/26782) | [video](https://youtu.be/LcDW43G82bA) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDC/Call-171_2025-12-11) |
| 08 Dec 2025 | ACDT | 63 | [#1834](https://github.com/ethereum/pm/issues/1834) | [forkcast](https://forkcast.org/calls/acdt/063) | [EthMag](https://ethereum-magicians.org/t/26875) | [video](https://youtu.be/tcANELFmOjU) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-063_2025-12-08) |
| 04 Dec 2025 | ACDE | 225 | [#1808](https://github.com/ethereum/pm/issues/1808) | [forkcast](https://forkcast.org/calls/acde/225) | [EthMag](https://ethereum-magicians.org/t/26515) | [video](https://youtu.be/2KU93ZHf-ww) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDE/Call-225_2025-12-04) |
| 01 Dec 2025 | ACDT | 62 | [#1820](https://github.com/ethereum/pm/issues/1820) | [forkcast](https://forkcast.org/calls/acdt/062) | [EthMag](https://ethereum-magicians.org/t/26739) | [video](https://youtu.be/J4tWSYe_nWQ) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-062_2025-12-01) |
| 27 Nov 2025 | ACDC | 170 | [#1812](https://github.com/ethereum/pm/issues/1812) | [forkcast](https://forkcast.org/calls/acdc/170) | [EthMag](https://ethereum-magicians.org/t/26620) | [video](https://youtu.be/1IA-NZa4VZ8) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDC/Call-170_2025-11-27) |
| 13 Nov 2025 | ACDC | 169 | [#1790](https://github.com/ethereum/pm/issues/1790) | [forkcast](https://forkcast.org/calls/acdc/169) | [EthMag](https://ethereum-magicians.org/t/26395) | [video](https://youtu.be/W-uqWQskV9o) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDC/Call-169_2025-11-13) |
| 10 Nov 2025 | ACDT | 61 | [#1797](https://github.com/ethereum/pm/issues/1797) | [forkcast](https://forkcast.org/calls/acdt/061) | [EthMag](https://ethereum-magicians.org/t/26434) | [video](https://youtu.be/uU4Vq7yeiGc) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-061_2025-11-10) |
| 06 Nov 2025 | ACDE | 224 | [#1781](https://github.com/ethereum/pm/issues/1781) | [forkcast](https://forkcast.org/calls/acde/224) | [EthMag](https://ethereum-magicians.org/t/25950) | [video](https://youtu.be/QWkAtpeIa4o) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDE/Call-224_2025-11-06) |
| 03 Nov 2025 | ACDT | 60 | [#1786](https://github.com/ethereum/pm/issues/1786) | [forkcast](https://forkcast.org/calls/acdt/060) | [EthMag](https://ethereum-magicians.org/t/26001) | [video](https://youtu.be/Um_f9tR-e_Q) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-060_2025-11-03) |
| 30 Oct 2025 | ACDC | 168 | [#1772](https://github.com/ethereum/pm/issues/1772) | [forkcast](https://forkcast.org/calls/acdc/168) | [EthMag](https://ethereum-magicians.org/t/25893) | [video](https://youtu.be/JelYN_iyU84) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDC/Call-168_2025-10-30) |
| 27 Oct 2025 | ACDT | 59 | [#1778](https://github.com/ethereum/pm/issues/1778) | [forkcast](https://forkcast.org/calls/acdt/059) | [EthMag](https://ethereum-magicians.org/t/25914) | [video](https://youtu.be/zfrPOtUxK90) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-059_2025-10-27) |
| 23 Oct 2025 | ACDE | 223 | [#1764](https://github.com/ethereum/pm/issues/1764) | [forkcast](https://forkcast.org/calls/acde/223) | [EthMag](https://ethereum-magicians.org/t/25807) | [video](https://youtu.be/In1-paNfjzQ) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDE/Call-223_2025-10-23) |
| 20 Oct 2025 | ACDT | 58 | [#1769](https://github.com/ethereum/pm/issues/1769) | [forkcast](https://forkcast.org/calls/acdt/058) | [EthMag](https://ethereum-magicians.org/t/25859) | [video](https://youtu.be/5qqcQaAet2o) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-058_2025-10-20) |
| 16 Oct 2025 | ACDC | 167 | [#1754](https://github.com/ethereum/pm/issues/1754) | [forkcast](https://forkcast.org/calls/acdc/167) | [EthMag](https://ethereum-magicians.org/t/25679) | [video](https://youtu.be/XBvBEHPqGhM) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDC/Call-167_2025-10-16) |
| 13 Oct 2025 | ACDT | 57 | [#1756](https://github.com/ethereum/pm/issues/1756) | [forkcast](https://forkcast.org/calls/acdt/057) | [EthMag](https://ethereum-magicians.org/t/25688) | [video](https://youtu.be/R7cs3ogM7f4) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-057_2025-10-13) |
| 09 Oct 2025 | ACDE | 222 | [#1748](https://github.com/ethereum/pm/issues/1748) | [forkcast](https://forkcast.org/calls/acde/222) | [EthMag](https://ethereum-magicians.org/t/25624) | [video](https://youtu.be/OxvLP6cstSE) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDE/Call-222_2025-10-09) |
| 06 Oct 2025 | ACDT | 56 | [#1750](https://github.com/ethereum/pm/issues/1750) | [forkcast](https://forkcast.org/calls/acdt/056) | [EthMag](https://ethereum-magicians.org/t/25633) | [video](https://youtu.be/dfngSRH8r4E) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-056_2025-10-06) |
| 02 Oct 2025 | ACDC | 166 | [#1740](https://github.com/ethereum/pm/issues/1740) | [forkcast](https://forkcast.org/calls/acdc/166) | [EthMag](https://ethereum-magicians.org/t/25573) | [video](https://youtu.be/d-uG-anQWA0) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDC/Call-166_2025-10-02) |
| 25 Sep 2025 | ACDE | 221 | [#1723](https://github.com/ethereum/pm/issues/1723) | [forkcast](https://forkcast.org/calls/acde/221) | [EthMag](https://ethereum-magicians.org/t/25424) | [video](https://youtu.be/1NIvzSliv44) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDE/Call-221_2025-09-25) |
| 22 Sep 2025 | ACDT | 54 | [#1731](https://github.com/ethereum/pm/issues/1731) | [forkcast](https://forkcast.org/calls/acdt/054) | [EthMag](https://ethereum-magicians.org/t/25509) | [video](https://youtu.be/xJe3erOIb4k) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-054_2025-09-22) |
| 18 Sep 2025 | ACDC | 165 | [#1716](https://github.com/ethereum/pm/issues/1716) | [forkcast](https://forkcast.org/calls/acdc/165) | [EthMag](https://ethereum-magicians.org/t/25351) | [video](https://youtu.be/CTfwQ4kOhE4) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDC/Call-165_2025-09-18) |
| 11 Sep 2025 | ACDE | 220 | [#1707](https://github.com/ethereum/pm/issues/1707) | [forkcast](https://forkcast.org/calls/acde/220) | [EthMag](https://ethereum-magicians.org/t/25290) | [video](https://youtu.be/wc40rKbl2LY) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDE/Call-220_2025-09-11) |
| 04 Sep 2025 | ACDC | 164 | [#1700](https://github.com/ethereum/pm/issues/1700) | [forkcast](https://forkcast.org/calls/acdc/164) | [EthMag](https://ethereum-magicians.org/t/25240) | [video](https://youtu.be/wF0gWBHZdu8) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDC/Call-164_2025-09-04) |
| 01 Sep 2025 | ACDT | 51 | [#1703](https://github.com/ethereum/pm/issues/1703) | [forkcast](https://forkcast.org/calls/acdt/051) | [EthMag](https://ethereum-magicians.org/t/25250) | [video](https://www.youtube.com/watch?v=KjIujvLQYWU) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-051_2025-09-01) |
| 28 Aug 2025 | ACDE | 219 | [#1687](https://github.com/ethereum/pm/issues/1687) | [forkcast](https://forkcast.org/calls/acde/219) | [EthMag](https://ethereum-magicians.org/t/25106) | [video](https://youtu.be/S4p0Ha_M_oE) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDE/Call-219_2025-08-28) |
| 25 Aug 2025 | ACDT | 50 | [#1692](https://github.com/ethereum/pm/issues/1692) | [forkcast](https://forkcast.org/calls/acdt/050) | [EthMag](https://ethereum-magicians.org/t/25152) | [video](https://youtu.be/r7bdQdnBclo) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-050_2025-08-25) |
| 21 Aug 2025 | ACDC | 163 | [#1673](https://github.com/ethereum/pm/issues/1673) | [forkcast](https://forkcast.org/calls/acdc/163) | [EthMag](https://ethereum-magicians.org/t/25104) | [video](https://youtu.be/gQly_DxdCHI) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDC/Call-163_2025-08-21) |
| 18 Aug 2025 | ACDT | 49 | [#1680](https://github.com/ethereum/pm/issues/1680) | [forkcast](https://forkcast.org/calls/acdt/049) | [EthMag](https://ethereum-magicians.org/t/25078) | [video](https://youtu.be/KuAtOO46Bxs) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-049_2025-08-18) |
| 14 Aug 2025 | ACDE | 218 | [#1652](https://github.com/ethereum/pm/issues/1652) | [forkcast](https://forkcast.org/calls/acde/218) | [EthMag](https://ethereum-magicians.org/t/24979) | [video](https://youtu.be/iPYHJnEeY9g) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDE/Call-218_2025-08-14) |
| 11 Aug 2025 | ACDT | 48 | [#1662](https://github.com/ethereum/pm/issues/1662) | [forkcast](https://forkcast.org/calls/acdt/048) | [EthMag](https://ethereum-magicians.org/t/25017) | [video](https://youtu.be/lsJhGRKrpes) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDT/Call-048_2025-08-11) |
| 07 Aug 2025 | ACDC | 162 | [#1638](https://github.com/ethereum/pm/issues/1638) | [forkcast](https://forkcast.org/calls/acdc/162) | [EthMag](https://ethereum-magicians.org/t/24919) | [video](https://youtu.be/RU4DgyH662c) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDC/Call-162_2025-08-07) |
| 31 Jul 2025 | ACDE | 217 | [#1629](https://github.com/ethereum/pm/issues/1629) | [forkcast](https://forkcast.org/calls/acde/217) | [EthMag](https://ethereum-magicians.org/t/24840) | [video](https://youtu.be/IUS5Z-BD79M) | [logs](https://github.com/nixorokish/eth-protocol-transcripts/tree/main/ACDE/Call-217_2025-07-31) |
| 30 Nov 2015 | ACDE | 1 | - | [notes](https://github.com/ethereum/pm/blob/master/AllCoreDevs-EL-Meetings/Meeting%201&2.md) | - | - | [logs](https://github.com/ethereum/pm/blob/master/AllCoreDevs-EL-Meetings/Meeting%201&2.md) |