# PeerDAS Breakout Room #6
Note: This file is copied from [here](https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit#heading=h.tubwqb51zcjq)

## Meeting info

Date: 2024.08.20

Agenda: https://github.com/ethereum/pm/issues/1136

YouTube Video: ​​https://www.youtube.com/watch?v=szACus93VNU
## Notes

### client updates
**Prysm**
- Improving test coverage, clearing up tech debts, getting PeerDAS into a merge-able state
- Implemented GET blob sidecars API support for nodes with >50% data columns
- Improved data column gossip validation
- Testing against rebased-electra version
- Prysm can starts PeerDAS either on Deneb or Electra

**Lodestar**

- Working on decouple subnets from groups
- Will work on rebasing PeerDAS on Electra

**Lighthouse**

- Fixed range sync and an issue with sampling sending excessive requests to a single peer
- Focused on merging das branch changes to main branch
- Made some progress on the optimisation to fetch blobs from EL (aka decentralized blob building)
- Some initial testing results show that proposers that don't publish all data columns can still propose a block fine, with the help from supernode on blob building and propagation.
- Increasing blob count may be challenging with the current way we compute proofs (200ms per blob and memory allocation on stack)
- This week focus on checkpoint sync and preparing for devnet
**Grandine**
Clarified sampling requirements, may join next devnet?
Nimbus
[not here today]
Teku
Implemented MetaDataV3 and getBlobSidecars API for nodes with >50% columns
Fixed sampling bug
Haven't started rebasing to Electra, probably start after devnet-2 launch

### Peerdas-devnet-2

Still Deneb based 

PR-3870 to be included

Alpha 5 

Metadata v3

Launch by end of the week (~23rd of Aug 2024)

Spec: https://notes.ethereum.org/@ethpandaops/peerdas-devnet-2 

### Peerdas-devnet-3

Electra rebased version

2-3 weeks from now

include decouple subnets PR

Sticking to EIP7594_FORK_VERSION and EIP7594_FORK_EPOCH for activating peerdas even after electra. 

### open discussion

**KZG**: How many blobs can we support for compute_cells and recover_cells, in terms of CPU, memory, time
- **Lighthouse** has concern that it would take longer once we go above 32 blobs, even with parallelization. Was wondering if it's possible to distribute the blob computation and have each supernode compute a subset of blobs, however this will require propagating cells instead of data columns
- **Csaba**: potentially more complexity in cell distribution
Francesco: if we increase blob count, the proposer could publish the block first and have supernodes to compute the blob proofs and propagate. The computation should be perfectly parallelizable, so shouldn't be an issue for a supernode.
- **Lighthouse** experiment on distributed computation and propagation PR

Validator custody - views on accountable validator custody?
- Is there any reason for wanting to do this now?
  -  **Pop**: it allows attacker to map to the node
- Bitfields for custody groups
  - Prysm already does this for syncsubnets, it wouldn't be too hard and it's a rational idea

Is it worth increasing custody_requirement for the devnet before we have validator custody
- Lighthouse propose to increase from current value 4 to 8 (future validator custodty requirement)
- Reason is to distribute the RPC requests to fullnodes, as all RPC requests currently go to supernodes and become center of failures
- Not much impact on a small devnet of 10-12 nodes, but wouldn't harm to try overriding the config if all clients support it.


## Zoom meet links

https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit

https://discord.com/channels/595666850260713488/1272838678443462667/1275380194621784156

https://github.com/ethereum/consensus-specs/pull/3870

https://github.com/ethereum/consensus-specs/pull/3889

https://github.com/ethereum/consensus-specs/pull/3800

https://notes.ethereum.org/@ethpandaops/peerdas-devnet-2
