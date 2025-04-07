# PeerDAS Breakout Room #23

## Meeting info
- Date: 2025.04.01
- Agenda: https://github.com/ethereum/pm/issues/1415
- YouTube video: https://youtu.be/RdzhIoZprl0


## Consensus Client Team Updates
| Team | Updates |
|---------------|---------|
| Lighthouse | • Merged PR for validator custody (still in progress)<br>• Fixed addressing issue causing client crashes<br>• Updated offload KZG+ computation PR to latest pending spec<br>• Working on sync fixes for devnet stability<br>• Implementing max blobs per block config parameter and flag for advanced testing |
| Prysm | • Continued work on database redesign (running on PeerDAS devnet-5)<br>• Working on unit tests and data column backfill implementation<br>• Reviewed Base team requests for getBlobV2, getPayloadV5, and spec modifications |
| Teku | • Working on distributed block publishing<br>• Refactoring needed due to spec changes allowing reconstruction from data column sidecars<br>• No other significant progress this week |
| Nimbus | • Improved getBlobsV1 implementation with performance enhancements<br>• Created column syncer to improve peer pool management and scoring<br>• Successfully tested in PeerDAS devnet-5 with fast sync<br>• Tested with ~30 blobs per block in Sunnyside Labs environment<br>• Planning work on getBlobsV2 this week |
| Lodestar | • Started implementing validator custody with good progress<br>• Continuing unit testing and refactoring work<br>• Planning to begin backfilling next week |
| Grandine | • Stabilized PeerDAS implementation<br>• Added distributed block publishing |

## Execution Client Team Updates
| Team | Updates |
|---------------|---------|
| Geth | • Updated branch to avoid calculating cell proofs on every block<br>• Computing proofs when transactions arrive via RPC or network<br>• Network changes still needed |
| Nethermind | • Branch with API implementation according to draft<br>• Handling mempool for new proof propagation<br>• Fixed issue with proof formats (V1 vs V2)<br>• Implementation ready for end-to-end testing |
| Besu | • No update provided |
| Erigon | • No update provided |
| Reth | • No prioritization last week but committing to complete implementation this week<br>• Expected timeline: 1-2 days of work  |

## Devnet / Testing Updates
| Topic | Subtopic | Details |
|-------|----------|---------|
| **peerdas-devnet-6 Plans** | Status | - Specs prepared but waiting for client implementations |
| | Launch Criteria | - Will launch once 2-3 client pairs are ready |
| | Current Decision | - No point launching before that milestone |
| **Sunnyside Labs Testing** | Test Configuration | - Conducted tests with 50 nodes of various client pairs |
| | Client Performance | - Measured maximum blob throughput per client:<br>  - Lighthouse/geth: 40 blobs/block<br>  - Teku/geth: 30 blobs/block<br>  - Prysm/geth: 25 blobs/block (without getBlobsV2)<br>  - Lodestar/geth: 25 blobs/block<br>  - Grandine/geth: 20 blobs/block |
| | Observations | - Observed correlation between declining getBlobsV1 hit rate and network instability |
| | Current Investigation | - Investigating geth's blobpool behavior |
| **Future Testing Plans** | EL Client Comparisons | - Test with alternative EL clients to compare blobpool implementations |
| | PeerDAS Evaluation | - Run tests without EL blob gossiping to evaluate pure PeerDAS performance |
| | Improvement Analysis | - Quantify distributed blob publishing improvements |
| | Metrics | - Standardize metrics across clients for better comparisons |

## EIP / Spec Updates and Discussions
| Topic | Subtopic | Details |
|-------|----------|---------|
| **Proof Format Clarification** | Available Versions | - Only two versions exist:<br>  - Version 0 (deneb/4844 format): One proof per blob<br>  - Version 1 (PeerDAS format): 128 proofs per blob, new wrapper version |
| | Terminology | - Agreement to stop using "version 2" terminology to avoid confusion |
| **Client Behavior** | Fork Handling | - Consensus to drop old proof format transactions after fork<br>- No conversion on client side for optimal performance |
| | Transaction Management | - After fork, only type-1 blob transactions should exist in mempool and P2P |
| | Implementation Flexibility | - Client implementations may vary on handling transactions at fork boundary |
| **Nethermind Implementation Fix** | Issue Resolution | - Fixed error when processing engine_getPayloadV5 requests<br>- Issue stemmed from incompatible blob proof formats |
| | Solution | - Solution: ignore older proof-format transactions when building Osaka/Fulu blocks |
| **getBlobsV2 Strategy Discussion + Implementation Priority** | Consensus | - General agreement to prioritize getBlobsV2 over validator custody |
| | Importance | - Essential for integration testing and determining supportable blob counts |
| | Team Commitment | - CL teams committed to focusing on this implementation |
| **Testing Requirements** | Baseline Testing | - Need to test network without getBlobsV2 to understand baseline performance |
| | Hardware Requirements | - High-bandwidth proposers (1+ Gbps) should be used for testing |
| | Performance Assessment | - Important to evaluate CL diffusion path performance independently |
| | Benefits | - Testing without getBlobsV2 helps identify gossip implementation weaknesses |

## Open Discussions
| Topic | Subtopic | Details |
|-------|----------|---------|
| **BPO Blob Schedule Proposal** | Timeline | • Start with current blob count parameters at Fulu launch<br>• Two-week observation period to ensure PeerDAS works well |
| | Scaling Approach | • Double blob counts every two months until reaching theoretical max |
| | Implementation Method | • Implementation as parameter changes rather than hard forks |
| **Client Compatibility** | Confirmed Support | • Confirmed architecture compatibility with Nimbus, Lighthouse, and other clients |
| | Parameter Design | • Implementation will use epoch-based parameters (BPO1_EPOCH) rather than fork names |
| | Code Efficiency | • Avoids extensive boilerplate code requirements for formal hard forks |
| **Configuration Details** | Metrics Needed | • Need to establish specific metrics for approving/reverting schedule changes |
| | Parameter Structure | • Parameters will include MAX_BLOBS_PER_BLOCK_BPO1, BPO1_EPOCH, etc. |
| | Fee Adjustments | • Potential to automate blob base fee update fraction with each increase |
| **getBlobSidecars Considerations** | Post-Fork Storage | • Post-fork, CL nodes will only store data columns, not direct blobs |
| | API Compatibility | • Proposal to maintain old getBlobSidecars API for compatibility |
| | Reconstruction | • Clients will implement reconstruction logic based on available columns |
| | Optimization | • API can return empty/zero proofs to save computation |
| | Trust Model | • API treated as trusted on client side (similar to beacon state queries) |
| **Validator Client Communication** | Performance Concerns | • Concerns about transmission time for large blob counts:<br>  - ~100ms for 48 blobs with 1Gbps connection<br>  - ~200ms for 96 blobs |
| | Payload Optimization | • Proposal to remove proofs and blobs from beacon API request payload |
| | API Design | • Trade-off between stateless and stateful API design |
| | Compression Options | • Compression option considered but may just transfer network latency to CPU |
| **KZG Library Functions** | Function Needs | • Interest in creating functions for efficient blob reconstruction:<br>  - recoverCells (no proofs)<br>  - cellsToBlob<br>  - recoverBlob |
| | Performance Metrics | • Current KZG proof generation takes ~200ms per blob on a single core |
| **Metrics Standardization** | Unified Approach | • Need for unified metrics across clients for PeerDAS |
| | Repository Proposal | • Proposal to create repository for EL metrics similar to beacon metrics repo |
| | Support Offered | • Sunnyside team offered to help with implementation |


## Links Shared
- https://github.com/ethereum/pm/issues/1415
