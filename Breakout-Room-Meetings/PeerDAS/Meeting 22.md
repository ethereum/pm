# PeerDAS Breakout Room #22

## Meeting info
- Date: 2025.03.25
- Agenda: https://github.com/ethereum/pm/issues/1401
- YouTube video: [Not provided]


## Consensus Client Team Updates
| Team | Updates |
|---------------|---------|
| Lighthouse | • Sync improvements and fixes on devnet-5 issues<br>• Distributed blob publishing spec drafted and reviewed<br>• Validator custody progressing, still 1-2 weeks away |
| Prysm | • Database redesign to fix the inode issue on devnet-5<br>• Francis from Base worked on EL getBlobsV2 and getPayloadV5 integration |
| Teku | • Tested validator custody internally<br>• New PeerDAS metrics from Katya |
| Nimbus | • No updates provided |
| Lodestar | • Good progress with refactor<br>• New contributor helping with validator custody<br>• Looking at peer management improvements, making sure there's always peers in all subnets for publishing |
| Grandine | • Update in chat<br>• Started implementing getBlobsV2 integration |

## Execution Client Team Updates
| Team | Updates |
|---------------|---------|
| Geth | • Have an open PR, have not reviewed it yet<br>• Some team members away this week |
| Nethermind | • POC branch with EL methods implemented and tx propagation should work, would like to test on multiclient environment |
| Besu | • No update provided |
| Erigon | • No update provided |
| Reth | • Types implemented<br>• Looking forward to locking in the spec. Will 1-2 days once spec finalised. |

## Devnet / Testing Updates
| Topic | Subtopic | Details |
|-------|----------|---------|
| **Peerdas-devnet-5** | Malicious Peer Testing | - Have been gradually increasing the number of malicious peers<br>- Since a week ago, 30% of network is acting maliciously |
| | Implementation Progress | - Barnabas is rolling out a Prysm fix, and will continue to roll out additional malicious nodes |
| **Sunnyside Labs** | Max Blobs Testing | - Max blobs testing (https://testinprod.notion.site/Sunnyside-Devnet-Updates-03-18-1ba8fc57f54680a29153e02aaf684620)<br>- Tried different CL client combinations, see above link for more details |
| | Issues Identified | - Some EL clients are hitting some tx pool limits |
| | Reporting | - Will publish another report in a couple of hours after the call |
| **Testing tooling updates** | Spammoor | - Tx format for tx submitter does not change, so no change required |
| | P2p Tester | - Sam is still working on its - won't be ready in the next few weeks |
| | Checkpointz | - Waiting for spec to finalise. For now its possible to checkpoint sync via beacon nodes |
| **Misc Testing Discussion Items** | Pre-mined Node Keys | - Pre mined node keys done - mined all required keys for test network to cover all columns |
| | Timeline Check | - TEMP CHECK: ship peerdas-devnet-6 and fusaka-devnet-0 by June 1 |
| | Devnet-6 Status | - Pari: waiting for some spec changes to be merged before we finalise devnet-6 |
| | Priority Order | - Focus on cell proof computation and launch devnet-6 when clients are ready, and then validator custody (can be deployed any time as it's forward compatible) |

## EIP / Spec Updates and Discussions
| Topic | Subtopic | Details |
|-------|----------|---------|
| **Validator Custody** | PR Status | - Open PR from Gabriel & Alex (https://github.com/ethereum/consensus-specs/pull/4188)<br>- Mostly language clarification. Not much to discuss. Awaiting review |
| **Static Custody Proposal** | Status | - (https://github.com/ethereum/consensus-specs/pull/4154)<br>- Some comments on the PR, no additional comments on the call |
| **getBlobs w/ DataColumnSidecar** | Optimization | - (https://github.com/ethereum/consensus-specs/issues/4186)<br>- Small optimization to call getBlobs as soon as any data column sidecar is received<br>- Columns contain all the KZG commitments, so waiting for blocks is not necessary |
| **Distributed Blob Publishing** | EL Concerns | - (https://github.com/ethereum/consensus-specs/pull/4183)<br>- Gajinder: if we call getBlobs too early, EL may not have blobs? |
| | Propagation Priority | - It's not only about satisfying custody, it's also important to contribute to propagation, so it should ideally be done as soon as possible |
| | EL Proposal | - Gajinder also proposed to do something similar on the EL side, to fetch the blobs from peers when getBlobs is called |
| **Cell Proof Computation** | Relevant PRs | - Execution-apis (https://github.com/ethereum/execution-specs/pull/1161)<br>- Builder-specs (https://github.com/ethereum/builder-specs/pull/117) |
| **Cell Proof Computation Discussion** | Design Finalization | - Francesco: be good to EL clients to talk about this, and finalise design, so we can move forward with the other specs and implementation |
| | Fork Boundary | - PR comment: on fork boundary, drop all blob tx from previous fork?<br>- There might be no blob tx included in the first block if this is done |
| | Client Implementation | - Felix: client could choose to either implement conversion (additional work on the client) or drop<br>- `wrapper_version` added to indicate how to decode the RLP (the intended type of the proof)<br>- EL devs agreed to leave this to EL clients on the implementation (felix's suggestion above) |
| | P2P Handling | - How to handle this (different proof types) in p2p<br>- Up to the clients to poll these transactions? Is there any way to tell whether it's an old/new blob tx?<br>- Can't be 100% sure just from looking at the data length, due to calldata<br>- Use a "cut-off" size to determine whether the tx contains a blob?<br>- Clients can choose to reject old blob txs in the second release after the fork |
| **Beacon Metrics** | Implementation Status | - (https://github.com/ethereum/beacon-metrics/pull/14)<br>- Katya is implementing these metrics in all the clients<br>- Next update will be around Validator Custody and the first client to get the update will be Teku |
| **EIP-7892 BPO hard forks** | Data Structure | - Keep the same data structure in the new fork, only blob count increases<br>- Low code change, still require coordination effort |
| | Alternative | - Francesco suggested an alternative option to schedule a linear increase |

## Links Shared
- https://github.com/ethereum/pm/issues/1401
- https://github.com/ethereum/consensus-specs/pull/4188
- https://github.com/ethereum/consensus-specs/pull/4154
- https://github.com/ethereum/consensus-specs/issues/4186
- https://github.com/ethereum/consensus-specs/pull/4183
- https://github.com/ethereum/execution-specs/pull/1161
- https://github.com/ethereum/builder-specs/pull/117
- https://github.com/ethereum/beacon-metrics/pull/14
- https://testinprod.notion.site/Sunnyside-Devnet-Updates-03-18-1ba8fc57f54680a29153e02aaf684620
