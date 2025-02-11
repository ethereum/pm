# PeerDAS Breakout Room #14
Note: This file is copied from [here](https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit?tab=t.0#heading=h.8tstytung49h)

## Meeting info
- Date: 2025.01.07
- Agenda: https://github.com/ethereum/pm/issues/1236
- YouTube video: https://youtu.be/0QfCxSbhRk8

## Notes
### Client updates:
#### Prysm
- Able to start at Deneb and transition to Electra & Fulu
- Able to start a node at Fulu
- Working on csc -> custody group count

#### Lodestar
- Switching to custody groups & switching implementers

#### Nimbus
- Done with custody groups (spec test passing)
- Remaining work: column syncing and Fulu activation

####  Lighthouse
- Implemented custody groups and getBlobSidecars API
- Working on checkpoint sync and Fulu activation
####  Teku
- Have Fulu branch that needs polishing
- Will work on subnet decoupling next

### Devnet updates:
- Devnet spec
  - https://notes.ethereum.org/@ethpandaops/peerdas-devnet-4
    - Spec alpha.10 release
    - Validator custody (Optional)
      - This may make all nodes supernodes (>=64 validators), Pari will make some nodes run 1 validator
    - **ACTION**: Pari is updating the devnet spec above. 

### Spec
- https://github.com/ethereum/consensus-specs/pull/4073
  - Keeping blob sidecars by root and by range V2 RPC endpoints, and removing get blobs by root and range V3
  - **ACTION**: Will include this in the next devnet

### Open discussions:
- Metrics (Katya)
  - PeerDAS metrics are not showing for Teku & Lighthouse
    - This is because ethereum-package deprecated `EIP7594_FORK_EPOCH` hence PeerDAS isn’t getting activated. This will work again once Fulu activation is implemented. In the meantime, using `ethereum-package` v4.4.0 should work.
 
### Links shared in meetings
- https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit?usp=sharing
- https://github.com/ethereum/consensus-specs/pull/4073
- https://notes.ethereum.org/@ethpandaops/peerdas-devnet-4
- https://github.com/ethereum/consensus-specs/compare/master
- https://github.com/ethereum/consensus-specs/pull/3864
- https://github.com/ethereum/beacon-metrics/pull/14
