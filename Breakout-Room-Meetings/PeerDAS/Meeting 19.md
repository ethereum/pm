# PeerDAS Breakout Room #19

## Meeting info
- Date: 2025.02.25
- Agenda: https://github.com/ethereum/pm/issues/1303
- YouTube video: https://youtu.be/NGgQuRoiHNo

## Consensus Client Team Updates
| Team | Updates |
|---------------|---------|
| Lighthouse | • Added new test CLI flags to delay block & data column publishing<br>• Made some sync fixes, will continue devnet-5 testing<br>• Validator custody impl started (without backfill initially) |
| Prysm | • Working on validator custody, have working implementation (without backfill)<br>  - Updates CGC when there's enough peers and connected to subnets<br>• Noticed a bug with Lighthouse <> Prysm, Prysm sometimes don't receive some gossip messages due to PRUNE messages sent by LH<br>  - Less likely to occur on regular full node or supernode<br>  - Happens more on nodes with exactly 64 custody columns (if missing one columns, block cant be made available)<br>  - Prysm & LH to investigate further |
| Teku | • Data column reconstruction implemented<br>• Started on validator custody |
| Nimbus | • Started validator custody, but gone back to refactor column syncing (greedily sync with supernode and reconstruct during sync - pro is it doesn't need supernode to sync)<br>• **ACTION**: will continue async discussion on sync approach |
| Lodestar | • Refactor on DA code and clean up syncing to make validator custody impl easier<br>• Node is syncing on devnet-5! |
| Grandine | • Not on the call |

## Devnet / Testing Updates
| Topic | Details |
|-------|---------|
| peerdas-devnet-5 | - Rafael: peerdas-devnet-5 launched 5 days ago (devnet-4 relaunch with fixed geth version)<br>- Grandine is failing and have pushed a fix but OOM |

## EIP / Spec Updates and Discussions
| Topic | Subtopic | Details |
|-------|----------|---------|
| **Sampling Concept** | PR Comment | - "Removing/altering sampling concept from the FULU spec" |
| | Terminology | - Manu: there's confusion between "sampling" and "peer sampling" |
| | Francesco's Explanation | - Custody sampling: 4 for full nodes, done via subnets<br>- Extra sampling: 4 extra for full nodes with validators, can be replaced via peer sampling but currently done via subnets |
| | Current Teku Behavior | - Check custody but no peer sampling<br>- Subscribe to 4 subnets and only samples 4 columns |
| | CGC Questions | - Manu: If one validator is attached to the full node (CGC bumps from 4 to 8), does the node still do random sampling? Since it now custody 8 columns<br>- Francesco: could switch some of the custody to random sampling (to get bandwidth benefits of peer sampling)<br>- (More details on the call) |
| | Peer Sampling Value | - Manu: Is it still worth implementing peer sampling? It only benefits full nodes with no validators, and adds lots of complexity<br>- It makes full nodes lighter to run |
| | Consensus | - Custody and sampling are currently treated the same, except for advertised CGC<br>- Teams agree this adds extra complexity<br>- No strong opinion to change the spec, because implementation was straightforward even though the spec was a bit convoluted |
| | Action Item | - Teams to continue discussion async and decide if spec change is needed |

## Open Discussions
| Topic | Subtopic | Details |
|-------|----------|---------|
| **Metrics** | Gossip Verification | - Katya raised issue with gossip verification metric |
| | Issue Identified | - LH has less than 128 columns gossiped per slot |
| | Action Item | - Jimmy to investigate metric issues |
| **Supernode %** | Research Question | - Determine supernode % on mainnet (agnish) |
| | Current Efforts | - Research & estimate of supernodes in the network |
| | Team Perspective | - Matt: shouldn't rely on supernodes, and treat it as nice to haves<br>- Most participants agree to this |
| | Context | - The question was mainly to help estimating sync speed on mainnet |
| | Action Item | - Add R&D task to research sync speed (consider with validator custody in place) |

## Links Shared
- https://github.com/ethereum/pm/issues/1303
- https://youtu.be/NGgQuRoiHNo
