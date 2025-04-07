# PeerDAS Breakout Room #17

## Meeting info
- Date: 2025.02.11
- Agenda: https://github.com/ethereum/pm/issues/1284
- YouTube video: https://youtu.be/Hd3rs1OEXGg?feature=shared

## Consensus Client Team Updates
| Team | Updates |
|---------------|---------|
| Lighthouse | • Found sync issue where peers are added before getting metadata (not considered super node despite having ENR)<br>• Working on refactoring |
| Prysm | • Working on validator custody implementation (more complex than expected)<br>• Found a Fu/Electra issue where states and blocks are identical, causing type identification problems |
| Teku | • No update provided |
| Nimbus | • Working on parallel reconstruction, testing in local devnets<br>• Observed latency in validating gossip in all-supernode network<br>• Implemented getBlobsV1, testing on local devnets which seems to fix latency issues<br>• Started work on validator custody<br>• Current sync algorithm is somewhat optimistic, relying on super nodes<br>• Considering a separate peer pool for peers with subset of custody |
| Lodestar | • Successfully syncing on devnet-4<br>• Using the PeerDAS branch |
| Grandine | • No update provided |


## Devnet / Testing Updates
| Topic | Details |
|---------|---------|
| Devnet-4 Update | - Devnet-4 is up and running at ~98% and almost 1,000 epochs in<br>- Looking significantly better than previous devnets (which started breaking at 3-5 day range)<br>- Grandine has a known issue - person working on PeerDAS codebase is currently out of office<br>- Lodestar is now syncing on devnet-4 |
| Testing plans | - First step: Test checkpoint sync with one node per client<br>- Second step: Add withhold data column flags to test reconstruction<br>- Third step: Convert some super nodes to full nodes (proposed ratio: 80% super nodes, 20% full nodes)<br>- Rafael suggested pre-mining node keys to ensure nodes across all column subnets when launching devnets<br>- All clients support overriding node keys (some via CLI flags, some via file path) |

## EIP / Spec Updates and Discussions
| Topic | Details |
|---------|---------|
| Moving proof computation to tx-sender | - Discussion about moving KZG proof computation burden from CL to transaction senders<br>- Concerns about changing cell size in the future requiring changes to how KZG proofs are computed<br>- Agreement that users are primarily L2s who can handle the needed work<br>- Jimmy planning to draft document and present to execution layer teams |
| Validator custody and backfilling | - Discussion about announcing updated custody group count (CGC) before/after backfill completion<br>- Francesco: Current spec behavior is to delay advertise CGC until backfill is complete<br>- Concern that backfill could take up to a week, during which a potential super node is not serving as one<br>- Suggestion to have separate peer pools - one for useful block/gossip peers, one for column-specific peering<br>- Discussion of different peer scoring approaches for column vs. block/blob related failures |

## Action items:
- Pari to handle devnet configurations (converting some super nodes to full nodes)
- Test checkpoint sync with one client from each implementation
- Test Genesis sync
- Test withholding data columns
- Ask Marius about where cell proof computation specification should go
- Jimmy to work on specification
- Continue discussion of validator custody implementation designs in Discord

## Links Shared
- [No links explicitly shared in the transcript]
