# PeerDAS Breakout Room #24
Note: This file is copied from [here](https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit?tab=t.0#heading=h.5bsq101keahm)

## Meeting info
- Date: 2025.04.08
- Agenda: https://github.com/ethereum/pm/issues/1425
- YouTube video: https://www.youtube.com/watch?v=ZzPAW-0xsa8

## Consensus Client Team Updates
| Team | Updates |
|---------------|---------|
| Lighthouse | • Fixed bug with DA check causing node instability (going up/down repeatedly)<br>• Root cause: lookup gets stuck requiring range sync mode<br>• Fix developed but targeting `peerdas-devnet-6` branch (can backport to devnet-5 if needed)<br>• Implemented cell proof computation PR<br>• Added distributed blob publishing implementation for full nodes<br>• Implemented max blobs per block configuration parameter<br>• Completed validator custody implementation (basic version without backfill) |
| Prysm | • Worked on validation pipeline for data<br>• Ready for integration with `getBlobsV2`, `getPayloadV5`<br>• Testing with Smokeping for 20 blocks |
| Teku | • Updated distributed blob recovery according to spec<br>• Working on cell proof implementation<br>• Fixed bug in canonical/non-canonical sidecars returned via API<br>• Fixing validator custody requirement calculation bug<br>• Added metrics for blob reconstruction with 50%+ columns |
| Nimbus | • Paused work on validator custody to focus on `getBlobsV2`<br>• Improved column syncer with successful testing on `peerdas-devnet-5`<br>• Full nodes can reliably sync using reconstruction<br>• Successfully serving range requests to Lighthouse |
| Lodestar | • Completed validator custody implementation<br>• PR ready for merging<br>• Working on backfilling implementation<br>• Planning implementation for `getBlobsV2` and `getPayloadV5` |
| Grandine | • Testing and hardening cell proof integration<br>• Found runtime crash when processing >30 blobs<br>• Stack overflow issue related to parallelized process<br>• Adding support for multiple KZG backends |

## Execution Client Team Updates
| Team | Updates |
|---------------|---------|
| Geth | • Working on implementation of `getBlobsV2` and cell proof calculation<br>• Moving from proof-of-concept to robust implementation<br>• New image available with fixes |
| Nethermind | • Fixed small bug in API<br>• Participating in custody testing<br>• Planning efficiency improvements for engine API `getBlobsV2` |
| Reth | • Completed implementation (PR merged)<br>• Fixed blob schedule issues<br>• Fixed bug handling transactions with >9 blobs<br>• Supporting consolidation of meeting time |
| EthereumJS | • Waiting for PRs to merge<br>• Planning to implement new transaction wrapper this week<br>• Working on changes for getBlobsV2 and new payload/blobs bundle |

## Devnet / Testing Updates
| Topic | Subtopic | Details |
|-------|----------|---------|
| **peerdas-devnet-6 Status** | Client Pairing | - Client pairs working: Nethermind + Reth<br>- Lighthouse and Grandine operational<br>- Latest Prysm image pending testing |
| | Spammer Configuration | - v0 records for pre-Fulu<br>- v1 type wrappers where possible |
| **Probe Lab Testing** | Mempool Analysis | - 86% of block transactions present in public mempool<br>- 82% of total proposed transactions arrive before slot start |
| **Metrics Development** | Client Support | - Nimbus has metrics for `getBlobsV1` full/partial/no responses<br>- Nethermind sending about 85-90% of requested blobs on mainnet<br>- Teams planning to implement metrics to measure `getBlobsV2` effectiveness |

## API & Protocol Discussions
| Topic | Subtopic | Details |
|-------|----------|---------|
| **getBlobsV2 Response Behavior** | Current Behavior | - Returns partial responses when some blobs available<br>- Takes ~200ms to get response from EL |
| | Proposed Change | - Return empty response unless all requested blobs available<br>- Rationale: Partial responses not useful for Fusaka implementation<br>- Only useful response states: complete set or nothing |
| | Performance Considerations | - Reduces bandwidth usage and JSON parsing overhead<br>- CL clients already discard partial responses<br>- Empty responses allow CL to try alternative methods faster<br>- Nimbus retries across threads with 1s timeout |
| | Consensus Decision | - Implement empty-or-full response behavior for getBlobsV2<br>- Leave getBlobsV1 behavior unchanged<br>- FLCL from Nethermind will create PR to update specification |
| **Validator Registration API Consolidation** | Proposal | - Consolidate prepareBeaconProposer and registerValidator APIs<br>- Different client implementations use varying cache strategies |
| | Implementation Differences | - Teku: Different timeouts and caching strategies<br>- Some clients do period-to-period calculations<br>- Various batch vs. single call patterns |
| | Concerns | - Cache pruning behavior alignment across clients<br>- Different frequency of API calls<br>- Potential impact on DVT integration |
| | Next Steps | - Teams to comment on GitHub issue regarding implementation details<br>- Consider validator calculation "period to period" rather than dynamic per epoch |

## Progress & Next Steps
| Topic | Details |
|-------|---------|
| **Notable Progress & Merges** | • Positive feedback on BPO concept/blob increasing schedule<br>• PRs for EIP 7594 merged last week<br>• Consensus Spec: v1.5.0-beta.4 pre-released last week<br>• API spec for self-proof computation merged |
| **Meeting Administration** | • Decision to move meeting time to 2PM UTC every week<br>• Noted conflict with Geth internal call at that time<br>• Aiming for wider audience availability with consistent time |
| **Open Issues & Next Steps** | • Implement `getBlobsV2` empty-or-full response behavior<br>• Teams focusing on `getBlobsV2` implementation as priority<br>• Continue work on validator custody implementation<br>• Prepare for `peerdas-devnet-6` launch once sufficient client pairs ready<br>• Collect metrics on blob propagation and getBlobsV1/V2 effectiveness |

## Links Shared
- https://github.com/ethereum/pm/issues/1425
