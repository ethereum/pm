---
title: Meeting 07

---

# PeerDAS Breakout Room #7
Note: This file is copied from [here](https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit#heading=h.tubwqb51zcjq)

## Meeting info 
Date: 2024.09.03
Agenda: https://github.com/ethereum/pm/issues/1139
YouTube Video: https://youtu.be/3UaTXEM1J_w

## Notes 

### Client updates
**Prysm**
- Having race condition issue after changing from 32 to 128 col subnets
- Measured data column building performance, had some issues (computation takes 5-7s) but narrowed issue down to c-kzg library
- Switched to go-kzg library and metrics look much better
- Implemented a switch to choose between c-kzg & go-kzg

**Lodestar**
- Tested supernode with other clients but unable to peer due to issues with csc format

**Lighthouse**

- Merged DAS branch into main branch (“unstable”), and made a few fixes to make PeerDAS work with Electra. Need testing.
- Spec tests updated, MetadataV3 updated, and is devnet-2 ready
- Working on getting max_blobs_per_block configurable & checkpoint sync support
- Tested PeerDAS with increased blob count (using the “fetch blob from el” branch) to 32 and 16 blobs. However there's a high miss rate with ~30 blobs, and a bit more stable with 16 blobs. Will come back with more metrics

**Teku**

- Working on fork choice with DA check
- Implemented csc in ENR and metadata, and other refactoring

**Grandine**

- Made some progress, still working on syncing with other clients

### Devnet

Devnet-2 has not launched, clients have different csc formats

csc discussion: https://github.com/ethereum/consensus-specs/pull/3908

Teams currently doing local testing peering its own supernode & fullnode
- Prysm & Lighthouse are able to sync between its own nodes from genesis
- Worked before for Teku but hasn’t tested recently

ACTION: merge above PR. Client teams to implement and test

### Open discussion

Bottleneck with computing KZG proofs PeerDAS vs 4844
- This is now done in the CL, and it could take up to 1s to compute this proof
- Ideas: 
  - EL could compute the proofs in advance prior to proposal?
  - We could shift proof computation outside of the block proposal window
  - CL needs better access to the mempool
  - Nodes could fetch blobs from EL mempool instead of waiting for data columns (Lighthouse has a prototype)

**Kev**: how does client allocate resources / threads for parallel computation
 - **Prysm**: allocation done by the go runtime
 - **Lighthouse**: no explicit allocation right now, allocation by the global threadpool, but may explore more controlled allocation
 - Teku has command line option to override number of threads

**Jimmy**: would like to hear feedback on “getBlobsV1” proposal

- https://github.com/ethereum/consensus-specs/pull/3864
- This would help reduce block available time as the CL don’t have to wait for data columns from the network if it already has the blobs
- Need to wait for the execution-api to be merged: https://github.com/ethereum/execution-apis/pull/559 

## Zoom chat links

https://github.com/ethereum/pm/issues/1139

https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit

https://github.com/ethereum/consensus-specs/pull/3908

https://github.com/ethereum/consensus-specs/pull/3864

https://github.com/ethereum/execution-apis/pull/559