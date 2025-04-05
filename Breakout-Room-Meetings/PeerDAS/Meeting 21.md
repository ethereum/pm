# PeerDAS Breakout Room #21

## Meeting info
- Date: 2025.03.18
- Agenda: https://github.com/ethereum/pm/issues/1364
- YouTube video: [Not provided]


## Consensus Client Team Updates
| Team | Updates |
|---------------|---------|
| Lighthouse | • Working on mostly refactoring |
| Prysm | • Number of files/inode issue still persistent. -> Working on a fix to include all subnets into one file instead of many different files. |
| Teku | • Working on validator custody - still WIP |
| Nimbus | • Working on column syncing - ~3d<br>• Working on validator custody - takes a bit more time |
| Lodestar | • Validator custody spec discussions<br>• No implementation updates |
| Grandine | • No update provided |

## Execution Client Team Updates
• No update provided

## Devnet / Testing Updates
| Topic | Details |
|-------|---------|
| Devnet 5 | - Prysm bug with the inodes running out of space<br>- Withholding columns did not trigger any new issues<br>- Validator custody changes can be rolled out on devnet 5 |
| Devnet 6 | - Validator custody - all clients still working on it<br>- Prysm has not implemented backfill yet |
| Sunnyside labs update | - https://testinprod.notion.site/Sunnyside-Devnet-Updates-03-18-1ba8fc57f54680a29153e02aaf684620?pvs=4<br>- Baseline comparison between electra/fulu using the same blobs<br>- Test cases: as similar to mainnet as possible, worst case, best case scenario testing, potentially limiting mempool bandwidth |

## EIP / Spec Updates and Discussions
| Topic | Details |
|-------|---------|
| Columns backfilling | - Active discussion about whether a client should start serving columns that it does not have vs one that it has already<br>- Current peer scoring algorithms should be able to handle it<br>- We might need to add backfilling progress advertised in the enr<br>- This might be an issue only with limited number of peers (like current devnets) |
| Static Custody Proposal | - Make validator custody static for beacon node run session (https://github.com/ethereum/consensus-specs/pull/4154)<br>- Adjust the PR to change the phrasing to enable validator stake instead of validator_indicies<br>- This will follow a re-review by client teams |

## Open discussion
| Topic | Details |
|-------|---------|
| Cell proof computation | - Base: prysm PR up, small fixes needed, EL side (geth) work in progress<br>- Consensus specs and builder specs PRs coming soon<br>- Nethermind: WIP not ready yet<br>- Reth: Started adding EL changes - looking for tests<br>- Testing: no available tests yet |
| Batch publishing columns | - Work in progress from multiple clients (lh, prysm)<br>  - https://github.com/sigp/rust-libp2p/pull/571<br>- https://ethresear.ch/t/improving-das-performance-with-gossipsub-batch-publishing/21713/10 |
| Engine/RPC | - We need a transaction tool |

## Links Shared
- https://github.com/ethereum/consensus-specs/pull/4154
- https://github.com/sigp/rust-libp2p/pull/571
- https://ethresear.ch/t/improving-das-performance-with-gossipsub-batch-publishing/21713/10
- https://testinprod.notion.site/Sunnyside-Devnet-Updates-03-18-1ba8fc57f54680a29153e02aaf684620?pvs=4
