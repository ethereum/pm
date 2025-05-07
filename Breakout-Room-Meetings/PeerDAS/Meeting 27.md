# PeerDAS Breakout Room #27
Note: This document is based on the notes from [Call #27](https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit?tab=t.0#heading=h.t4ps7ebtyevu)

## Meeting info
- Date: 2025.04.29
- Agenda: https://github.com/ethereum/pm/issues/1505
- YouTube video: https://youtu.be/KoTEe7i3LSo?feature=shared

## Consensus Client Team Updates
| Team | Updates |
|---------------|---------|
| Lighthouse | - Working on fixing sync issues, particularly edge cases in range sync handling<br>- Fixed issues with clients not serving data columns from non-synced peers<br>- Testing fixes on Sunnyside's network and identifying additional edge cases |
| Prysm | - Continuing to merge PeerDAS branch into main branch (18,000 lines still to go)<br>- Implemented column verification pipeline improvements with caching for inclusion proofs<br>- Added new flag to only subscribe to data column subnets without other subnets<br>- Working on builder API integration<br>- Implemented emergency sync for full nodes to reconstruct missing columns when no peers serve specific columns |
| Teku | - Implemented changes to handle columns in by-root RPC<br>- Completed distributed self proofs for block production<br>- Implemented execution layer reconstruction with getBlobsV2<br>- Working on builder flow integration - local production complete but builder support still pending<br>- Code ready for review but not yet merged |
| Nimbus | - Current focus is investigating issues related to DevNet-6<br>- Improving column syncing implementation |
| Lodestar | - Merged all open PRs from past weeks<br>- Made progress on refactoring work<br>- Implemented getBlobsV2 with polling at different times to measure timing discrepancies<br>- Implemented getPayloadV5 (PR pending final approval)<br>- Fixed bug where supernode flag was overridden by validator custody<br>- Working on integration testing with Kurtosis |
| Grandine | - Hong returned from vacation and implemented several fixes<br>- Fixed API issues including null response handling for engine getBlobsV2<br>- Investigating syncing issues when peers don't return requested columns consistently<br>- Considering implementing column reconstruction during syncing when fetch fails |

## Execution Client Team Updates
| Team | Updates |
|---------------|---------|
| Geth | - Updated Fusaku branch removing EOF components while updating to latest master<br>- Working on fixing issue with V1 blobs in payload<br>- Will move updated branch to upstream repo |
| Nethermind | - No significant updates<br>- Working on internal reviews to prepare PR for master branch<br>- No functional changes or new features |
| Reth | - No functional changes since last week<br>- Rebasing branch on top of main (may surface new bugs) |
| Ethereum JS | - Development complete with test cases for cell transactions and network wrapper<br>- End-to-end client tests implemented<br>- Ready to test with Kurtosis and join DevNet-7 this week |

## Devnet / Testing Updates
| Topic | Subtopic | Details |
|-------|----------|---------|
| **PandaOps** | DevNet-6 Status | - Faced issues with EL clients processing blocks very slowly<br>- Some CL clients had bugs in data custody implementation, reporting incorrect subnets<br>- Main focus shifting to Pectra debugging with shadow fork<br>- Possible DevNet-7 could be scheduled for end of week if needed |
| **Sunnyside Labs** | Network Status | - Network running with DevNet-6 specifications (70 nodes)<br>- Network working fine for testing needs<br>- Can maintain network for longer if needed while resources focus on Pectra<br>- Can update images with new features as teams develop them |

## API & Protocol Discussions
| Topic | Subtopic | Details |
|-------|----------|---------|
| **Column Reconstruction During Sync** | Implementation Status | - Grandine considering implementing reconstruction of missing columns during sync<br>- Prysm already working on similar implementation for emergency sync<br>- Strategy useful for unhealthy networks where columns aren't reliably served<br>- Lighthouse already performs reconstruction at head but not during range sync |
| **BPO Schedule Configuration** | Implementation | - PR implements blob schedule as list of records including Deneb and Elektra<br>- Removing placeholder BPO values to avoid setting expectations<br>- Testing challenges with the implementation due to far-future epochs<br>- EL side can align syntax but doesn't need standardization as different genesis formats exist<br>- Agreement to handle BPO like regular forks on EL side |
| **Blob Sidecar Deprecation** | Proposal | - PR for deprecating blobSidecarsByRange/Root APIs after Fusaku support period<br>- Proposal to not penalize peers requesting Fusaku blocks during the 18-day window<br>- General agreement from all client teams |
| **DataColumnSidecarsByRoot Request** | Improvement | - Changed request to use one route with multiple indices instead of one route/index per request<br>- More efficient approach with smaller worst-case size<br>- PR already merged |
| **Engine API Changes** | Validation Rules | - Engine API changes merged<br>- GetBlobsV2 will return null for invalid/pre-Fusaku blob hashes<br>- GetBlocksV2 and GetPayloadV4 will return unsupported fork errors after Fusaku |
| **Get Blobs API** | Discussion | - Debate about all-or-nothing approach to blob retrieval<br>- Concern that private mempool transactions might make API less useful<br>- Clarification that API primarily supports local block building where blobs are in public mempool<br>- Data showing 60% success rate with current getBlobsV1 on mainnet<br>- Agreement that network should remain stable even without getBlobsV2 functioning |

## Progress & Next Steps
| Topic | Details |
|-------|---------|
| **Fusaku Timeline** | - Question about schedule impact since EOF is no longer part of Fusaku<br>- Consensus that EOF removal doesn't significantly impact PeerDAS timeline<br>- ModX implementation will be needed before Fusaku DevNet-0 |
| **BPO Implementation** | - Suggestion to schedule BPO fork during Fusaku DevNet-0<br>- Agreement that this would be beneficial for testing |
| **Builder Support** | - Note that builders could serve as super nodes to help with blob retrieval<br>- Possibility of adding this to builder specification |

## Links Shared
- BPO PR: Introduce blob only parameter forks
- Fulu BlobSidecarsByRange/Root Deprecation Support PR
- Improve DataColumnSidecarsByRoot request PR
- Engine API PR for PeerDAS-related changes
- Ethereum Magicians thread on BPO config format
- Theoretical Blob Transaction Hit Rate Research Post
