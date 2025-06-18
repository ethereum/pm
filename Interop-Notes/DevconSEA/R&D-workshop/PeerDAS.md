# PeerDAS

**Summary:** This session will cover the latest state of research and development of PeerDAS, the next planned upgrade to increase Ethereum's data availability throughput. We will cover the current state of implementation, and discuss future roadmap items that aim to unlock even more throughput.

**Facilitator:** Alex Stokes and Jimmy Chen

**Note Taker:** Manu (Prysm)

**Pre-Reads:**

* High-level overviews of DAS and data sharding
    * https://hackmd.io/@vbuterin/sharding_proposal
    * https://www.paradigm.xyz/2022/08/das
* PeerDAS specifics
    * https://ethresear.ch/t/peerdas-a-simpler-das-approach-using-battle-tested-p2p-components/16541
    * https://eips.ethereum.org/EIPS/eip-7594
    * https://hackmd.io/m7RvWICeQjeMBjglOKgrVg
* DAS roadmap exploration
    * https://notes.ethereum.org/@fradamt/path-to-scaling-DA

Optional:
* PeerDAS cryptography deep-dive: https://eprint.iacr.org/2024/1362.pdf
* Fork choice concerns and DA: https://notes.ethereum.org/xwRXoNTtQO-Z_t68S11nDg
* https://ethresear.ch/t/peerdas-with-significantly-less-bandwidth-consumption/20932
* List of PeerDAS from Francesco: https://hackmd.io/UzW5OamOTwe6iLF8b5n-5w

**Slides:** See links in notes.

**Notes:** https://hackmd.io/9Os1iYJbSmagOM0pT-dRZw

## Agenda 

### 45 mins: Presentations on state of R&D
* [Alex] Intro to DAS, with focus on PeerDAS
* [Jimmy] Overview of PeerDAS implementation and devnet status
* [Alex] Review of open R&D topics on DAS

### 30 mins: Breakouts

Attendees will break into a number of smaller groups for focused discussion. Exact topics can be decided during the session, subject to participant demand.

Possible breakout topics:
* Devnet coordination/implementation status or blockers
    * What is blocking shipping stable PeerDAS devnets?
    * Implementation status of sample distribution and sampling
* Sharded mempool design
    * Keep node bandwidth manageable in the face of high(er) blob counts
* Distributed block building to leverage high-bandwidth nodes for blob distribution
    * Early research:
        * https://notes.ethereum.org/wcg_u2qORiqpyZ7KbPjRAA?view
        * https://notes.ethereum.org/@dankrad/Bky8ieRkye
    * Proof computation bottlenecks?
    * Upload bandwith bottlenecks?
* Syncing strategy at high blob counts (esp. under network asynchrony)
* Future roadmap/path to deployment
    * Can we break up PeerDAS features into phases for devnet implementation? And possibly for hard fork implementation?
    * Concrete suggestion for Pectra blob count adjustments, or blockers here

### 15 mins: Breakout summaries and conclusion

All session attendees will rejoin to review breakout topics and highlight next steps.

## Notes

## General presentation of peerDAS by Alex (30 min)
[Link to the slides](https://docs.google.com/presentation/d/1-VXgKxbC7k64VH3H08dYsClOEHxTmCSQXiZ4v-lQf2w/edit).

***Summary:***
- **EIP-4844**: The first major step in Ethereum’s data availability roadmap introduces blobs—128 KB fixed-size data packets that increase data throughput.

- **Need for More Blobs**: To support more affordable decentralized applications, including Layer 2 rollups, Ethereum needs to increase the number of blobs. However, this requires reducing the load and bandwidth demands on individual nodes to maintain decentralization. Data Availability Sampling (DAS) is essential in achieving this, as it enables nodes to verify data availability without downloading all data, paving the way for scaling the blob count efficiently.

- **Data Availability Sampling (DAS)**: PeerDAS aims to scale data throughput on Layer 1 by allowing nodes to download only a small part of the (chunked) blobs, rather than all the blobs, as it is done in EIP-4844, while still ensuring full data availability through cryptographic commitments and sampling techniques. This approach uses peers for sampling.

- **DAS Framework (DSR)**:
  - **Distribution**: Involves broadcasting data to the network (e.g., block producers distributing blobs).
  - **Sampling**: Allows nodes to verify data availability by sampling commitments.
  - **Reconstruction**: Through erasure encoding, nodes can recover missing data if certain parts are lost, maintaining network resilience.

- **PeerDAS Sampling and Reconstruction**: EIP-7594 builds on EIP-4844, adding networking capabilities for random sampling. Nodes use DAS to avoid downloading full blobs, relying instead on sample-based signals for consensus. This supports data scaling while keeping node bandwidth requirements stable.

- **~~Ultrapeers~~ - Supernodes**: Some nodes, known as ultrapeers, support more data subnets than required, strengthening the network's data sampling and distribution backbone.

PeerDAS allows Ethereum to scale by verifying data availability in a decentralized manner, maintaining security while managing bandwidth and promoting cost efficiency for Layer 2 solutions.


## PeerDAS implementation status by Jimmy (30 min)
Link to the [HackMD](https://hackmd.io/WmglRaFaRIaUR3h62Kil-w) document.

## Questions (30 min)

**Q**: What happen if all supernodes go away?
**A**: Supernodes (voluntary opt-in) are not stricly needed for peerDAS to success. Although not essential for PeerDAS’s success, supernodes increase data reliability across the network. Additionally, as validator custody is implemented, some beacon nodes will naturally connect to more subnets than the minimum required. Large node operators will thus naturally evolve into supernodes.

**Q**: Do devnets use peer sampling or only subnet sampling?
**A**: In the first devnet, some clients implemented peer sampling, but later all switched to subnet sampling. Although subnet sampling needs more bandwidth, it’s simpler to implement.

**Q**: If fusaka, do we plan to change the forkchoice?
**A**: No (unless we switch back from subnet sampling to peer sampling with trailing fork choice?)

**Q**: Do clients wait for completing reconstruction before considering a block available (and so, vote for it)?
**A**: Currently, super LH nodes wait for all data columns to be fully downloaded and verified before marking a block as available. If reconstruction is needed, LH will wait for the complete reconstruction of all columns. Prysm operates differently, considering the block available once 50% of the columns are downloaded and pass the gossip validation.

**Q**: Has any stress testing been conducted on the devnets?
**A**: Not really. Devnets already struggle to maintain finality for more than a few days, even under optimal conditions. The goal is to first ensure that finality can be achieved for a reasonable period in ideal conditions, and only then attempt to stress test the network. However, both LH and Prysm implement an option to "withhold" data columns, allowing nodes to avoid publishing all 128 data columns, which forces supernodes on the network to reconstruct the data.

**Q**: When do nodes decide to reconstruct?
**A**: The specification does not clearly define the behavior. LH begins reconstruction as soon as 50% of the columns are received and then gossips the reconstructed columns. Prysm, on the other hand, waits for 3 seconds into the slot (an arbitrary value that could be adjusted) before starting the reconstruction. Only the reconstructed data columns are then gossiped. Some randomness in timing should be introduced before reconstruction to prevent all nodes from reconstructing and gossiping the columns simultaneously.

## Related
- A fullDAS session happens the same day, during the afternoon.
- A Road to shipping PeerDAS session happens the next day, during the morning.