# PeerDAS Breakout Room #25
Note: This document is based on the notes from [Call #25](https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit?tab=t.0#heading=h.wh43ed18k111)

## Meeting info
- Date: 2025.04.15
- Agenda: https://github.com/ethereum/pm/issues/1441
- YouTube video: https://youtu.be/D0WRpEbqLVU?feature=shared

## Consensus Client Team Updates
| Team | Updates |
|---------------|---------|
| Prysm | - Continued work on data columns verification pipeline<br>- Working to address verification computation time issues on devnet-6<br>- Implementing blob bundle v2 structure (replacing current v1 with extended size limit)<br>- Backfill implementation ongoing but proving more complex than expected |
| Teku | - Completed distributed cell proofs implementation<br>- Final PR under review, aiming to merge today<br>- Planning to join devnet-6 once PR is merged<br>- Starting process to transition PeerDAS code from feature branch to production codebase (~2 month timeline) |
| Nimbus | - Addressing CPU utilization issues in devnet-6<br>- Optimizing multiple read/writes on column database from gossip and EL sides<br>- Local testing complete, re-syncing with devnet-6<br>- Additional optimizations planned<br>- Working on backfill cases (requested devnet-5 remain available for testing) |
| Lodestar | - Merged validator custody and getBlobsv2 implementations<br>- Adding second column pull per spec with metrics to identify timing/delivery issues<br>- Completed cell proof changes implementation<br>- Ongoing refactor work (~3-4 weeks timeline)<br>- Successfully synced to head on devnet-6 (non-validating) |
| Grandine | - Ongoing issue with Grandine-Reth pairing<br>- Investigation suggests possible issue on Reth side with slow payload processing |

## Execution Client Team Updates
| Team | Updates |
|---------------|---------|
| Nethermind | - Added metrics for getBlobs success/failure rates<br>- Shared PR with implementation details in chat<br>- Working on PoC for SSZ endpoint for getBlobsV2<br>- Waiting for consensus on BPO implementation |
| Ethereum JS | - Started PR for implementation<br>- Working on extending micro-eth-signer library to include cell-based functions<br>- Planning to extend WASM KZG library<br>- Engine API and transaction implementation targeted for this week |

## Devnet / Testing Updates
| Topic | Subtopic | Details |
|-------|----------|---------|
| **PandaOps** | Kurtosis Updates | - Breaking changes coming to Kurtosis for spammor configuration<br>- Now two separate processes for transaction and block spamming<br>- New web UI for spammer control<br>- Spammor running in devnet-6 |
| | Client Onboarding | - Onboarded Lodestar (no validators yet)<br>- Planning to onboard Teku<br>- Asked if devnet-5 could be shut down (Nimbus requested it remain available for backfill testing) |
| **Sunnyside Labs Testing** | Client Performance | - Tested Lighthouse with multiple ELs (Geth, Erigon, Besu, Reth, Nethermind)<br>- Besu: 50 blobs per block (highest)<br>- Erigon: 18 blobs per block (lowest)<br>- Geth: ~45 blobs per block with lower resource usage (most efficient)<br>- Noted need for unified metrics across ELs<br>- Shared document with detailed testing results |

## API & Protocol Discussions
| Topic | Subtopic | Details |
|-------|----------|---------|
| **Unified EL Metrics** | Proposal | - Standardized metrics across EL clients for PeerDAS<br>- Shared detailed proposal document in chat |
| | Implementation Approaches | - Option 1: Unified naming conventions<br>- Option 2: External mapping table<br>- Roman noted differences in metric types (e.g., "histograms" in Reth are actually summaries)<br>- Nethermind shared PR with their metrics implementation<br>- Additional getBlobs metrics suggested for tracking success rates<br>- Question raised about whether getBlobsV2 metrics are needed on both EL & CL sides |
| **getBlobsV2 Timeout** | Current Status | - Current 1-second timeout in spec considered too long<br>- Proposal to reduce to 250ms or less (100ms suggested as ideal in chat)<br>- Strong consensus from multiple participants to reduce timeout<br>- Dustin noted ELs don't necessarily have timeouts as servers<br>- Agreement to continue detailed discussion async |
| **BPO Configuration Format** | Format Options | - Proposal to remove placeholder max blobs per block value<br>- CL side preference for array in primary configuration<br>- Discussion of dictionary vs. array of records in YAML (array of records preferred)<br>- Question about handling potential need to reduce blob counts (BPO should allow this)<br>- Preference for "release" rather than "config" approach<br>- Concern raised about sustainability of increased blob counts<br>- Discussion about whether BPO changes should be treated like regular hard forks |
| **Cells vs. Blobs Architecture** | Proposal | - Proposal to use cells throughout the stack instead of blobs<br>- Potential computation efficiency benefits<br>- Strong concerns about bandwidth impact from multiple participants<br>- Blobs are 4 times smaller than cells in space for full PeerDAS<br>- Concern about sending twice as much data in the mempool<br>- Concern about timing and scope of such a large change<br>- Agreement to develop detailed written proposal async |

## Progress & Next Steps
| Topic | Details |
|-------|---------|
| **Timeline** | - Devnet-6 currently live<br>- Petra mainnet planned for May 5th<br>- Fusaka-devnet-0 with BPO implementation target: May 20th<br>- Coordination with EOF team needed |
| **Action Items** | - Finalize BPO configuration format (preference for array of records)<br>- Continue devnet-6 testing<br>- Draft cells vs. blobs proposal<br>- Review/merge open PRs for cell proof computation<br>- Implement unified metrics approach<br>- Schedule EL client BPO config structure discussion for ACD |
| **Next Meeting Agenda** | - Continue BPO configuration discussion<br>- Review cells vs. blobs proposal<br>- Track devnet-6 performance |

## Links Shared
- https://grafana.observability.ethpandaops.io/d/MRfYwus7k/nodes?orgId=1&var-consensus_client=nimbus&var-consensus_client=lighthouse&var-execution_client=All&var-network=peerdas-devnet-6&var-filter=ingress_user%7C%21~%7Csynctest.%2A&viewPanel=34&from=now-1h&to=now
- https://testinprod.notion.site/Proposal-for-Unified-EL-metrics-for-PeerDAS-1d28fc57f54680f2a3cbfe408d7db4b8
- https://github.com/NethermindEth/nethermind/pull/8495/files
- https://testinprod.notion.site/Sunnyside-Devnet-Updates-04-15-1d18fc57f54680498c85e6ce41dd7c4e
- https://github.com/ethereum/consensus-specs/pull/4183
- https://github.com/ethereum/consensus-specs/issues/4266
- https://github.com/ethpandaops/spamoor/pull/30
