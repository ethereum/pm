# PeerDAS Breakout Room #26
Note: This document is based on the notes from [Call #26](https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit?tab=t.0#heading=h.h0hcp5xs4ja8)

## Meeting info
- Date: 2025.04.22
- Agenda: https://github.com/ethereum/pm/issues/1491
- YouTube video: https://youtu.be/mbbCjiCIXuQ?feature=shared

## Consensus Client Team Updates
| Team | Updates |
|---------------|---------|
| Lighthouse | - Fixed issue with clients not serving data columns from peers who were not synced |
| Prysm | - Manu on vacation; Terence fixed disconnection bugs during initial sync<br>- Properly implemented blobs bundle v2 structure to replace previous hack with extended size<br>- Added missing unit and spec tests<br>- Improved verification time of columns by 10x (from 100ms to ~10ms)<br>- Slowly merging chunks of PeerDAS branch into develop branch (KZG library and RPC structure) |
| Teku | - Completed distributed cell proofs and block production with execution layer reconstruction<br>- Implemented getBlobsV2<br>- Working on builder flow integration with local production complete<br>- Builder support still pending |
| Nimbus | - Investigating issues related to devnet-6<br>- Improving column syncing |
| Lodestar | - Implemented getBlobsV2 with first poll for objects crossing gossip<br>- PR ready for second poll a few seconds into slot to measure timing discrepancies<br>- Implemented getPayloadV5, PR pending final approval<br>- Fixed bug with supernode flag being overridden by validator custody<br>- Multiple PRs for data availability pipeline refactor |
| Grandine | - Hangleang returned from holidays and started addressing previously reported issues<br>- No significant fixes yet |

## Execution Client Team Updates
| Team | Updates |
|---------------|---------|
| Geth | - No team member present on call |
| Nethermind | - Working on potential optimizations for network encoding<br>- Investigating whether flat data structure would be more performant than separate traces<br>- Branch ready for review |
| Reth | - Restarted Reth nodes paired with other clients on Friday<br>- No further insights gained on syncing issues<br>- Unable to reproduce reported problems |
| Ethereum JS | - Mostly completed PR based on CKZG implementation<br>- Need to add test cases<br>- Once MicroSigner library is ready, will remove CKZG dependency<br>- Should be ready to participate in devnets this week |

## Devnet / Testing Updates
| Topic | Subtopic | Details |
|-------|----------|---------|
| **DevNet-6 Status** | Issues | - Degradation started April 17-18 with OOM issues in Geth<br>- Each Geth OOM triggered 30,000 block resyncs from block 18,000<br>- Network achieved finality sporadically when Geth nodes reached head<br>- Situation worsened when Nethermind also started experiencing OOM issues<br>- Multiple CL client bugs in advertising/syncing prevented network self-healing<br>- API reliability issues across clients with inconsistent error codes<br>- Barnabas shared script to parse logs and track client restarts |
| | Next Steps | - Short-term fix: Increase RAM from 8GB to 16GB (considered excessive for devnet)<br>- Discussion about whether to repair DevNet-6 or move to DevNet-7 with client fixes<br>- Barnabas suggested fixing OOM handling to be more graceful |
| **Sunnyside Labs** | Testing Status | - Running 70 nodes with DevNet-6 specs<br>- Waiting for fixes before conducting detailed testing<br>- Will continue monitoring and report issues in Discord |

## API & Protocol Discussions
| Topic | Subtopic | Details |
|-------|----------|---------|
| **BlobsBundleV2 Format** | Current Format | - Commitments, blobs, proofs coded as RLP strings in arrays<br>- Managed languages create many allocations and copies |
| | Proposal | - Use SSZ list of fixed-size containers to save on copying<br>- Need to benchmark to quantify performance improvement<br>- Major change but potentially more efficient |
| **BPO Configuration** | Implementation | - PR implements blob schedule configuration as list of records<br>- Included Deneb in schedule for completeness<br>- Agreement to remove placeholders to avoid setting expectations |
| | Client Adoption | - Discussion about how clients should adopt the schema format<br>- Client releases would be bundled with consensus specs release providing versioning<br>- Need API to query current/next blob parameters (similar to EL gas limit approach) |
| **Custody Group Bugfix** | Issue | - Small bug in the spec related to custody group function<br>- Variable for number of columns used instead of number of custody groups<br>- PR submitted for one-line change |
| **API Standardization** | Error Handling | - Inconsistent behavior across clients for API error handling<br>- Need to standardize error codes for better interoperability<br>- Barnabas offered to compile a list of issues if needed |
| **MEV Builder Support** | Current Status | - Justin updated sticky builder with full PeerDAS support<br>- MavBoost has been updated but not tested<br>- Need to update relay to support SSZ as well<br>- Builder does support SSZ |
| **Data Column Optimization** | Proposal | - Data columns contain duplicated block routes<br>- Potential to reduce request size from 40KB to 132B (75% reduction)<br>- Trade-off in semantics as list format would need to indicate missing columns<br>- Discussion to continue in Discord channel |
| **GossipSub Performance** | Improvements | - GossipSub API changes can improve PeerDAS publishing performance<br>- Branch available in GossipSub, client teams encouraged to implement<br>- Extends gossipsub batch publishing capability<br>- Lighthouse already implementing this feature |
| **Custody Group Metrics** | Implementation | - Added metrics regarding custody groups<br>- Seeking input on whether logic is only on beacon node side or also needed in validator clients<br>- Will open thread to continue discussion |

## Progress & Next Steps
| Topic | Details |
|-------|---------|
| **DevNet Status** | - Dealing with OOM issues in Geth and Nethermind<br>- Considering whether to repair DevNet-6 or move to DevNet-7<br>- Short-term fix: Increase RAM allocation |
| **Optimization Work** | - Data column optimization discussions<br>- GossipSub performance improvements<br>- BlobsBundleV2 format considerations |
| **Ongoing Implementation** | - Builder support for PeerDAS<br>- Client teams merging PeerDAS code into main branches<br>- API standardization needed for error codes |

## Links Shared
- BPO PR: Introduce blob only parameter forks
- Custody Group Bugfix PR
- GossipSub Batch Publishing
- Consensus Dev Channel Thread on Data Column Optimization
- Clarification on custody sampling
- Update EIP-7594: Add blob count per tx limit via blobSchedule
- execution-apis: Add EIP-7594 (PeerDAS) related changes
- Remove placeholder MAX_BLOBS_PER_BLOCK_FULU
- feat(gossipsub): Add MessageBatch
- Improving DAS performance with GossipSub Batch Publishing
- PeerDAS metrics: add data column, kzg, custody metrics
