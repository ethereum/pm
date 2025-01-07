
# PeerDAS Breakout Room #2

Note: This file is copied from [here](https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit#heading=h.tubwqb51zcjq)

## Meeting Info: 
**Date**: 2024.06.25

**Agenda**: https://github.com/ethereum/pm/issues/1070

**YouTube Video**: https://www.youtube.com/watch?v=P86Dr9ABGeg

## Notes
### Peerdas-devnet-1
- https://notes.ethereum.org/@ethpandaops/peerdas-devnet-1 (v1.5.0-alpha.3)
- Pandaops needs peerdas-devnet-1 branches from Nimbus, Lodestar, and Grandine. Please check if these branch names are correct:
  - prysm: peerDAS
  - lighthouse: das
  - teku: nashatyrev-das
  - nimbus: wip-peerdas
  - grandine: das
  - lodestar: peerDAS 

### Configuration
DATA_COLUMN_SIDECAR_SUBNET_COUNT=64

SAMPLES_PER_SLOT=16

CUSTODY_REQUIREMENT=4

TARGET_NUMBER_OF_PEERS=70
  - ACTION: Check the above info on Discord:
  - https://discord.com/channels/595666850260713488/1252403418941624532/1255111016702935060

### Client updates
- **Prysm**
  - Implemented reconstruction - with a delay. The node waits for 3 seconds into the slot, before sending via gossip
  - Improvements to sampling, and implemented LossyDAS / IncrementalDAS
- **Lighthouse**
  - improvements to reconstruction to make it non-blocking
  - 1.5.0-alpha.3 spec compliant and passing spec tests
  - devnet-1 ready, although still working on a sync bug
  - Next:
  - Fix sync and implement checkpoint sync
  - Try out Kev's Rust PeerdasKzg library (ckzg alternative)
  - Experiment with fetching blobs from EL for reconstruction and publishing (distributed blob building). Michael has a PR for Deneb, and the team is planning to port it over to PeerDAS.
- **Teku**
  - Comply with alpha.3 spec
  - Grandine, lodestar, and nimbus are not ready for devnet-1
  - 
### spec discussion
- Blob max limit
  - Solution 1: pass 'max_blobs_per_block'
  - https://github.com/ethereum/consensus-specs/pull/3800
  - Solution 2: pass `​​base_fee_per_blob_gas`
  - https://github.com/ethereum/consensus-specs/pull/3813
  - Client teams favor solution 1 today
  - **Gajinder** (Lodestar) is in favor of passing the target gas limit (#1), less inclined for #2
  - **Lion:** Gas calculation requires UIN256 calculation, most CLs don't do this yet.
  - **Nishant:** Prefers #1 as well, as we can leave the gas computation in the EL.
- ACTION: Add this to Thursday's call agenda
  - 'get_extended_sample_count'
  - https://github.com/ethereum/consensus-specs/pull/3782 ready to merge? -> will merge before Thursday if no objection
  - https://github.com/ethereum/consensus-specs/pull/3794 -> will merge before Thursday if no objection
### Open discussion
- Do we want to increase the blob count on devnet-1?
   - Some devs think it would be useful, however, MAX_BLOBS_PER_BLOCK is currently a preset value and not configurable in some clients
   - Everyone agreed MAX_BLOBS_PER_BLOCK should be configurable
   - ACTIONS:
   - Lion to make a spec PR for this
   - Barnabas will launch devnet-1 without blob increase for now to not delay the launch and will test the blob increase on a few clients with higher blob count later
- **Lion**: Micheal's experiment on fetching from EL pool - apply this technique to PeerDAS
   - This would make it more feasible for home stakers in remote areas without good internet
   - If blobs are made available in the mempool, supernodes can help reconstruct and distribute
   - Nishant (Prysm) also likes this
   - Nishant raised concern about the EL bandwidth increase however no one on the call knows exactly what the impact would be
   - ACTION: Lion to make a writeup on this
   - [20240701 update] Lion’s writeup: https://hackmd.io/@dapplion/blob_fetch
- Devenet-1 num of supermodes per client
   - People agreed that we should launch supernode on multiple clients so that the network still has nodes to serve all columns if one client has a bug - more data availability to keep the network alive (likely the reason devnet-0 died)
   - ACTION: DevOps would like Prysm / Teku flag for this - teams to share on discord

## Zoom chat links
https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit#heading=h.94w8lt9y3mc7

https://github.com/ethpandaops/ethereum-package/blob/606ba6401241a12bd972980a4df9c77ba03b18a2/.github/tests/peerdas-fork.yaml

https://github.com/ethereum/consensus-specs/pull/3800

https://github.com/ethereum/consensus-specs/pull/3813

https://github.com/ethereum/consensus-specs/pull/3782

https://github.com/ethereum/consensus-specs/pull/3794

https://eips.ethereum.org/EIPS/eip-4844#networking
