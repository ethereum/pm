# PeerDAS Breakout Room #20

## Meeting info
- Date: 2025.03.11
- Agenda: https://github.com/ethereum/pm/issues/1326
- YouTube video: [Not provided]

>The next breakout call will be **Tuesday 1400 UTC!**

## Consensus Client Team Updates
| Team | Updates |
|---------------|---------|
| Lighthouse | • Fixed a Prysm interop issue where Lighthouse prunes the Prysm mesh peer due to a libp2p race condition, causing the gossip columns to not be sent to Prysm. This has been fixed and is under review.<br>• Drafting a consensus-spec PR to specify distributed blob publishing behaviour, will share in the next few days |
| Prysm | • Implemented validator custody, under review<br>• inode limitation issue: currently store 1 file per data column, after 18 days, there were 10M files, and hit the limit. Working on a fix<br>• Niran from Base working on ByRoot RPC method<br>• Francis on getBlobsV2 integration |
| Teku | • Working on validator custody, not much progress due to Holeksy but shifting focus back to PeerDAS now |
| Nimbus | • Had some Issue with missing blob sidecars<br>• Working on column syncing (dual mechanism)<br>  - Greedy mechanism (prioritise peer with higher CGC, default)<br>  - Require more resources and bandwidth<br>  - Will share more results when implemented<br>• Had sync issue on devnet-5, issue is now fixed and stable on devnet-5 |
| Lodestar | • Almost completed refactor, and have a PR to simplify validator custody<br>  - Gajinder proposed a spec change [here](https://github.com/ethereum/consensus-specs/pull/4154)<br>  - **ACTION**: client team to review and provide feedback ASAP |
| Grandine | • Looking into resource issue during sync |

## Execution Client Team Updates
| Team | Updates |
|---------------|---------|
| Geth | • Working on EL support and should have it ready soon |
| Nethermind | • Working on EL support and should have it ready soon |
| Besu | • No update provided |
| Erigon | • No update provided |
| Reth | • No update provided |

## Devnet / Testing Updates
| Topic | Details |
|-------|---------|
| Running some nodes as full nodes | - **ACTION**: all clients to verify if all nodes are set up as full nodes |
| Devnet-5 testing | - Checkpointz provider?<br>  - **ACTION**: pandaops will sort it out<br>- Prysm withhold column test<br>  - **ACTION**: pandops will deploy 1 node with this flag |
| Devnet-6 scope | - Main change is new CL-EL integration with cell proofs<br>- Banabas proposed to discuss timeline<br>  - Marius (Geth) will work on it today<br>  - Nethermind and ethereumjs will also participate<br>  - CL teams are mostly busy with validator custody<br>  - Client teams to share in chat when ready |
| Mining node keys (Rafael) | - Rafael suggested to pre mine some nodes keys to make sure we have nodes across all column subnets when launching devnets<br>- All clients support overriding node keys, some via CLI flag and some via file path |

## EIP / Spec Updates and Discussions
| Topic | Details |
|-------|---------|
| Validator custody | - Nimbus asked if it can advertise a property to indicate the node is backfilling, so the node doesn't get penalised while backfilling<br>  - Current spec behaviour: delay advertise CGC until backfill is complete |
| Distributed blob publishing | - Prysm doesn't have it currently, but will implement it using getBlobsV2<br>  - Marius planning to implement getBlobsV2 soon<br>- Teku and Lighthouse has is it implemented with getBlobsV1<br>- Nimbus had some issue with EL hit rate, so have it disabled |
| Networking Format | - Felix on networking format (https://github.com/ethereum/EIPs/pull/9378/)<br>- Propose having an explicit version identifier for the proof type<br>  - Nethermind: backward compatibility? But not a problem to add it<br>  - The cell proof may change again, and KZG is not quantum resistant, so it makes sense to have a version identifier<br>- **ACTION**: teams to provide feedback and finalise in the next 2 days |

## Open discussion
| Topic | Details |
|-------|---------|
| PeerDAS Roadmap | - PeerDAS Roadmap from Francis - please review and help update: [link](https://docs.google.com/document/d/1MXf5zTU58mRj0Yq88EPBP1gCJzWTY9FRfUdpZjcfgqw/edit?tab=t.0)<br>- Teams to review and provide feedback on the spec change PRs, goal is to finalise spec ASAP! |


## Links Shared
- https://github.com/ethereum/pm/issues/1326
- https://github.com/ethereum/consensus-specs/pull/4154
- https://github.com/ethereum/EIPs/pull/9378/
- https://docs.google.com/document/d/1MXf5zTU58mRj0Yq88EPBP1gCJzWTY9FRfUdpZjcfgqw/edit?tab=t.0
