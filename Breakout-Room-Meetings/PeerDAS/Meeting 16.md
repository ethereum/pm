# PeerDAS Breakout Room #16

## Meeting info
- Date: 2025.02.04
- Agenda: https://github.com/ethereum/pm/issues/1259
- YouTube video: https://youtu.be/Y1tWb1EUATY


## Consensus Client Team Updates
| Team | Updates |
|---------------|---------|
| Lighthouse | • Interop testing with other clients, discovered a few non PeerDAS related bugs<br>• Starting to work on validator custody |
| Prysm | • Started working on validator custody<br>• Tested Prysm with all clients that are ready, found and fix some small bugs |
| Teku | • Implemented subnet decoupling<br>• Implemented reconstruction of columns from EL blobs, only on supernodes (distributed blob building) |
| Nimbus | • Not present |
| Lodestar | • Subnet decoupling done<br>• Looking at validator custody, peerdas-devnet-4 ready |
| Grandine | • Fixed a sync bug that caused peer disconnection<br>• Fixed some bugs found during interop testing<br>• Found a few sync issues not related to PeerDAS |

## Devnet / Testing Updates
| Topic | Subtopic | Details |
|-------|----------|---------|
| **peerdas-devnet-4** | Launch Priority | - Prysm: we should launch devnet ASAP |
| | Network Configuration | - Francesco suggested starting with a supernode-only network<br>- Teams agreed to have validators on supernodes only, and some full nodes without validators<br>- Once stable, switch some validators to full nodes |
| | Network Size | - devnet-3: 10-15 nodes<br>- No comment to increase/reduce number of nodes |
| | Branch Information | - Same branch (devnet-4 spec link above) for Teku, Prysm, LH, Grandine, Lodestar |
| | Action Item | - **ACTION**: Pari to launch peerdas-devnet-4 some time after this call🚀 |
| **peerdas-devnet-5** | Feature Inclusion | - Include validator custody for all clients<br>- Blob count increase if things go well in devnet-4 |
| | Distributed Blob Building | - How do we measure the effectiveness of this?<br>- Might be worth drafting up some test scenarios |
| | Test Scenarios | - Try different peer counts? (max peers) lower peer count so not all nodes are connected to all nodes<br>- Pari: we could enable rate limit, pack drop, peer count, internet bandwidth etc<br>- Csaba: disable publishing to some subnets<br>- Some nodes to not publish any columns |
| | Action Item | - **ACTION**: Jimmy to start with some basic test scenarios on the spec page, and teams to update as we go. |

## EIP / Spec Updates and Discussions
| Topic | Subtopic | Details |
|-------|----------|---------|
| **Validator Custody** | Specification Concerns | - Should we specify how column backfilling and CGC update works in spec?<br>- Spec doesn't currently mention backfill on extra clients, teams agree it should ideally be explicit |
| | CGC Update Timing | - If we update CGC first, node may get disconnected if peers ask for older columns before backfill completes<br>- Francesco proposed to only update CGC once backfill is complete<br>- Teams agree this is a simple solution |
| | Action Item | - **ACTION**: Spec PR to specify "Not updating until after backfilling, and explicit requirement to backfill" |
| **Distributed blob building** | Documentation | - May be worth adding publishing behaviour into the spec |
| | Action Item | - **ACTION**: Jimmy to create issue on consensus-spec |
| | Gradual Publication | - Not necessarily useful in the spec, and teams can optimise this differently |
| **DAS parameters** | Subnet Configuration | - Subnet count? Why 128 instead of 64? Some clients may struggle with finding peers on all subnets<br>- More efficient, and less data per subnet |
| | Status | - No proposed action, keep monitoring in devnets |

## Open Discussions
| Topic | Subtopic | Details |
|-------|----------|---------|
| **State of KZG libraries** | Overview | - George: c-kzg, rust-kzg and go-kzg are all ready and will get audited |
| | Prysm | - Uses c-kzg, plan is to switch to go-kzg<br>- c-kzg performance is not as good as go-kzg<br>- Benchmarks c-kzg vs go-kzg: https://github.com/prysmaticlabs/prysm/pull/14804 |
| | Lodestar | - Switching from c-kzg to rust |
| | Teku | - Support both c-kzg and rust-kzg, but prefers c-kzg |
| | Grandine | - Recently switched to their own rust-kzg library |
| | Lighthouse | - Currently use c-kzg for Deneb and rust-eth-kzg for PeerDAS |
| | Current Status | - Currently at least one client using each library |
| **Katya on Metrics** | Display Issues | - Metrics Charts are not displaying well due to default 15s scrape interval vs 12s slots |
| | Action Item | - **ACTION**: Pari will update scrape interval for the next devnet to 12s |
| | Custody Column Count | - Total custody column count metric (`beacon_custody_columns_count_total`)<br>- Manu: What does this metric give us? |
| | Discussion Follow-up | - **ACTION**: We ran out of time. Teams to continue discussion async in the link below:<br>- https://github.com/ethereum/beacon-metrics/pull/14 |
| **Misc Discussion** | Column Distribution | - Francesco: can we send columns within 1 subnet, sequentially to mesh peers? So we make sure we have at least one copy is sent out first<br>- Staggered sending (time-based) in nim libp2p implementation<br>- This is not part of libp2p specification but seems like a useful behaviour |
| | Implementation Action | - **ACTION**: Csaba will help specify this. |
| | Meeting Schedule | - Pari suggested moving this call to 3pm (same time as ACD)<br>- Frequency: consensus to change this from once every 2 weeks -> every week |
| | Schedule Action | - **ACTION**: Pari to start a poll on Discord. Once decided, contact Tim to change this call |

## Links Shared
- https://github.com/ethereum/pm/issues/1259
- https://youtu.be/Y1tWb1EUATY
- https://notes.ethereum.org/@ethpandaops/peerdas-devnet-4
- https://notes.ethereum.org/@ethpandaops/peerdas-devnet-5
- https://github.com/prysmaticlabs/prysm/pull/14804
- https://github.com/ethereum/beacon-metrics/pull/14
