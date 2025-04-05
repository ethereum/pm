# beam call #3: research updates | p2p networking

**Prev:** [Call 02](https://github.com/ethereum/pm/blob/master/Breakout-Room-Meetings/beam-chain/meeting_02.md)

**Meeting Date/Time:** Friday 2025/4/4 at 14:00 UTC

**Meeting Duration:** 1.75 hours

[GitHub Agenda](https://github.com/ethereum/pm/issues/1389)

[Audio/Video of the meeting](https://youtu.be/dJkuwuh2Nrs?feature=shared)

Moderator: Justin Drake

Facilitators: Ladislaus von Daniels & Will Corcoran
- Facilitator emails: ladislaus@ethereum.org // will@ethereum.org
- Facilitator telegrams: @ladislaus0x // @corcoranwill

## Agenda
| Agenda Item | Topic | Link |
| --- | --- | --- |
| Intro | Social Layer Updates by @justindrake | [link](https://docs.google.com/presentation/d/1yavZUvmfnTYzsOuY086AaJgtTMEayANfNBVnmxL1_Kg/edit?usp=drive_link) |
| Pres 01 | Hash-based SNARKs w/ Small Proofs by @TomWambsgans | [link](https://docs.google.com/presentation/d/10pRsghxatnjju_8oKAmrhas1t5P_jtiTxUme3w1U7CY/edit?usp=drive_link) |
| Pres 02 | Permissionless Aggregation by @justindrake | [link](https://docs.google.com/presentation/d/11z8uO3rTHO2dxsNmRqWFqgJgMtRQAzYUq2nNT0UAPdY/edit?usp=drive_link) |
| Pres 03 | Generalized Gossipsub by @AgeManning | [link](https://docs.google.com/presentation/d/1AtsSryG_xiiuhUBRbHjSWAu4YlBPq1x-lulyLhDnYVc/edit?usp=sharing) |
| Pres 04 | Gossipsub V2 by @ppopth | [link](https://docs.google.com/presentation/d/1jDC5pV710PEz_-Flgdt4zGeo8zlzdAszWXaxjprRPiw/edit?usp=drive_link) |
| Pres 05 | Grid Topology by @kamilsa | [link](https://hackmd.io/@kamilsa/rJ7SjSZaye#/) |
| Pres 06 | Set Reconciliation by @yangl1996 | [link](https://docs.google.com/presentation/d/1zqBpF-o7qFFuYUPESgK0jIYvVbiD2dlu9X2dpaS1ySQ/edit?usp=drive_link) |
| Pres 07 | libp2p in C by @uink45 | [link](https://docs.google.com/presentation/d/1nDm8wk2psmRIYbh0cb5ye11KmABu-D-kmVv3VuIdZoY/edit?usp=drive_link) |
| Pres 08 | libp2p in Zig by @zen-eth | [link](https://docs.google.com/presentation/d/1WU0X-7sAKIoNy3gwA32PTtv5X6biRlLwXwsbVBXDUkQ/edit?usp=sharing) |


## Intro: Social Updates by @justindrake

| Topic | Details |
| --- | --- |
| Beam Day Event | • June 29th in Cannes, France (day before ETH-CC)<br>• Limited capacity - DM coordinators or find Luma page for details<br>• Preference given to developers and researchers |
| Ethproofs Call #1 | • First call scheduled for April 25th at 2pm UTC<br>• Telegram group available to join for discussions<br>• Has synergies with Beam Chain due to zkVM accelerationism |
| 2025 Call Schedule | • Calls 2-6 will cover high-level research updates<br>• Q3-Q4 will focus on spec'ing calls<br>• Will start with subspecs and then develop a holistic, feature-complete Beam spec |
| EF Networking Team | • Foundation building internal networking team<br>• Pop and Marco have joined the team<br>• Third person joining soon |
| Agenda Overview | • 8 speakers covering P2P networking topics<br>• Call extended from 1 hour to 1.5 hours to accommodate all presentations |

## Pres 01: Hash-based SNARKs w/ Small Proofs by @TomWambsgans

| Topic | Details |
| --- | --- |
| Technology Overview | • Technical note on hash-based SNARKs with short proofs for post-quantum aggregate signatures |
| Key Innovation | • Uses WIR (Weierstrass Isogeny Representation) commitment scheme as replacement for Fiat-Shamir |
| Performance | • Achieves smaller proofs (100-200 KB) compared to alternatives like Plonky3<br>• Approximately 10x better than previous approaches |
| Implementation Options | • Three ways to leverage WIR in AIR arithmetization context:<br>  1. Direct replacement for FRI committing to univariate columns and quotient polynomial<br>  2. Encode all univariate columns into single multilinear polynomial<br>  3. Commit to entire AIR table as multilinear polynomial using Lagrange basis |
| Results | • Implemented quantum signature aggregation with best-in-class proof sizes<br>• Code complexity of only 6,000 lines for Prover and Verifier combined |
| Background | • Emile appeared "out of nowhere" :) and quickly implemented post-quantum signature aggregation<br>• Achieved both best-in-class proof sizes and codebase simplicity |

## Pres 02: Permissionless Aggregation by @justindrake

| Topic | Details |
| --- | --- |
| Design Goals | • Create potato-friendly peer-to-peer networking layer<br>• "Potato" defined as very weak computing device (phone, Raspberry Pi, watch) |
| Simplifications | 1. **Reuse infrastructure:** Use libp2p (Discovery v5, Gossip Sub) from beacon chain<br>2. **Maintain pre-quantum security:** For networking layer as it's ephemeral, off-chain, low-value<br>3. **Non-potato aggregators:** ~1/8th of nodes to handle heavy lifting/aggregation<br>4. **Recursive aggregation:** Allows local greedy, collaborative, censorship-resistant aggregation<br>5. **Cap on active validators:** Instead of complicated sampling |
| Aggregator Concept | • Nodes run benchmark at runtime to determine if they can be aggregators<br>• Default on parameter (opt-out available)<br>• ~1/8 of nodes estimated to be powerful enough (e.g., laptops with decent CPU/GPU) |
| Scaling Goal | • Target: 1 million active validators per slot<br>• Start with 8,000 in proof of concept (2025)<br>• Leverage Nielsen's Law: Internet bandwidth doubles every 2 years<br>• Quadratic scaling: 4x validators every time bandwidth doubles |
| High-Level Design | • **Subnets:** Break validators into 8 subnets (e.g., 1,024 attesters per subnet)<br>• **Two-level aggregation:**<br>  1. Local aggregation of signatures per subnet<br>  2. Global aggregators observe all subnets<br>• **Bit field first approach:** Nodes advertise available signatures and best aggregate as bit fields<br>• Reduces redundant downloads/uploads of large signatures/aggregates |
| Anti-Censorship | • Recursive aggregation allows anyone to take a censoring aggregator's work and add the censored attestations |

## Pres 03: Generalized Gossipsub by @AgeManning

| Topic | Details |
| --- | --- |
| P2P Design Space | • Three key features in trade-off relationship:<br>  1. Low latency (LL)<br>  2. High resilience (HR)<br>  3. Low bandwidth (LB) |
| Current Implementations | • LL + LB = Lean broadcast tree<br>• LL + HR = Floodsub<br>• HR + LB = Pure gossip<br>• Gossipsub sits in the middle, allowing trade-offs |
| Current Challenges | • Trade-offs in gossipsub affect all protocol topics<br>• Privacy concerns (pseudo-anonymity, not true privacy)<br>• Difficult to simulate real-world networks<br>• Changes impact multiple networks (Ethereum, Filecoin, IPFS) |
| Proposed Solution | • **Generalized Gossipsub:**<br>  - Modularize trade-offs as optional "strategies"<br>  - Apply different strategies per topic and network<br>  - Allows implementations to use different trade-offs for different applications<br>  - Can adapt to different bandwidth constraints |
| Privacy Discussion | • Current system offers pseudo-anonymity, not true privacy<br>• Suggestion to consider whether privacy is needed for beam chain<br>• Transparent IP registration could enable more efficient network structures |
| Implementation Status | • Specification draft exists<br>• Plan to implement in Rust libp2p for simulations and testing |

## Pres 04: Gossipsub V2 by @ppopth

| Topic | Details |
| --- | --- |
| Current Gossipsub Issues | • Peers forward messages immediately, causing duplicate messages<br>• Uses IHAVE/IWANT mechanism only at heartbeats<br>• Wastes bandwidth with multiple copies of the same message |
| V2 Improvements | • Peers send IANNOUNCE instead of full message<br>• Recipients send INEED only to first peer sending IANNOUNCE<br>• Introduces cascading IANNOUNCE/INEED with timeout<br>• Configurable probability for sending IANNOUNCE vs. full message |
| Timeout Mechanism | • Time-out needed when peer doesn't respond to INEED<br>• If timeout occurs, send INEED to second peer<br>• Must configure timeout carefully (not too high to avoid delays, not too low for global network) |
| Simulation Results | • Tested scenarios with different IANNOUNCE/message ratios<br>• V2 allows doubling of message count without performance degradation<br>• Significant reduction in duplicate messages |
| Future Improvements | • Potential use of erasure coding to remove timeout requirement<br>• Consider "choke/unchoke" mechanism to let receivers decide message format<br>• Using trustworthiness metrics to prioritize mesh peers for INEED messages |

## Pres 05: Grid Topology by @kamilsa

| Topic | Details |
| --- | --- |
| Assumptions | • 16k validators<br>• Each validator generates a 1.5 KB signature<br>• Untrusted, altruistic aggregators/provers generate SNARKs<br>• Validator addresses are known |
| Grid Structure | • Validators use common source of randomness to form grid view<br>• Each validator maintains connections with row and column neighbors<br>• Two-dimensional grid latis with known coordinates |
| Distribution Pattern | • Three-step process for signature propagation:<br>  1. Validator sends signature to all row/column neighbors<br>  2. Neighbors propagate in orthogonal direction<br>  3. All nodes send IHAVE messages to prevent eclipse attacks |
| Benefits | • Maximum distance between any two validators is 2 hops<br>• Each validator receives same message from at most 2 peers<br>• Linear number of total signature messages in validator network<br>• Easier to simulate due to deterministic nature |
| Signature Aggregation | • Multiple grids used to reduce bandwidth requirements<br>• Separate aggregator subnets for each validator grid<br>• Final aggregation sent to all validators through single grid |
| Real-world Usage | • Implemented in Polkadot with 600-1000 validators<br>• Successfully distributes statements within 6-second slots |

## Pres 06: Set Reconciliation by @yangl1996

| Topic | Details |
| --- | --- |
| Problem Statement | • Optimize performance and trade-offs in p2p networks<br>• Address redundant message issue in gossip protocols<br>• IANNOUNCE not always optimal for short messages |
| Set Reconciliation | • Allows peers to efficiently learn only new items from each other<br>• Information-theoretically optimal solution exists but has quadratic computation cost<br>• Recent advancements: log-linear computation, no need to pre-know difference size |
| Performance | • Communication cost: ~1.35 times the size of the difference to reconcile<br>• Computation: log-linear, tens of megabits per second per CPU core<br>• Single trip for reconciliation to finish |
| Applications | • Potential use in signature aggregation for Beam Chain<br>• Being deployed in Bitcoin for transaction propagation (e.g., Erlay proposal)<br>• Possible use in state healing for Ethereum |
| Implementation Status | • Ready implementation in Golang (supported by Ethereum Foundation)<br>• Community implementations available in C++ and Rust<br>• Next steps: Simulations needed to measure potential gains |

## Pres 07: libp2p Implementation in C by @uink45

| Topic | Details |
| --- | --- |
| Development Timeline | • Started March 7th, repository recently made public<br>• Currently implementing core modules |
| Current Progress | • Implemented multiformats modules<br>• Working on multi-address and peer ID modules |
| Implementation Scope | • Multibase: Supports all base encoding formats with final status in spec<br>• Multihash: Implemented common SHA functions (except deprecated SHA-1)<br>• CID: Implementing support for v0 and v1 |
| Goals | • Support interaction with Ethereum consensus layer beacon nodes<br>• Implement remaining modules including gossipsub |
| Status | • Not yet ready for public usage due to potential API changes<br>• Once core modules are complete, will provide usage documentation<br>• Will accept feedback and pull requests |

## Pres 08: libp2p Implementation in Zig by @zen-eth

| Topic | Details |
| --- | --- |
| Core Projects | • Three focus areas:<br>  1. Multi-formats<br>  2. Noise protocol<br>  3. Kademlia (YAMX) |
| Progress | • Multi-formats and noise protocol mostly complete<br>• Current focus on YAMX and adding examples to noise protocol |
| Goals | • Pass all interop test vectors provided by libp2p |
| Project Status | • Open-source work at github.com/zen-eth<br>• Currently self-funded project done in personal time<br>• Seeking community engagement and contributions |
