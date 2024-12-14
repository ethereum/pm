---
title: Meeting 09

---

# PeerDAS Breakout Room #9
Note: This file is copied from [here](https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit#heading=h.tubwqb51zcjq)
## Meeting info
Date: 2024.10.01
Agenda: https://github.com/ethereum/pm/issues/1155
YouTube video: https://youtu.be/v5BWEX4FYnw

## Notes

### Client updates
**Prysm**
- Still offline on devnet-2, having issues with invalid sidecars published by Grandine, therefore Prysm disconnected with all other peers
- Discv5 (?) very slow with Grandine in the mix
- Had issues with syncing, fixed and working locally (fullnode)

**Lodestar**
- Had some configuration issues, nodes couldn’t sync
- Some supernode peers not replying with data columns, so lodestar couldn’t sync
- Posted the sync issues in the chat, Nimbus has been investigating

**Teku**
- Updated Rust KZG
- Implemented GetDataColumns API, could use for debugging

**Lighthouse**

- Having issue of supernode not serving columns, investigating
- Looking to update and try “rust-eth-kzg”, the new version has computation time reduced from 200ms to 150ms
- Released PeerDAS metrics with 16 blobs in this post

### Devnet updates
Devnet-2 participation at 50%, should we relaunch devnet-2?
- Prysm has a fix and is trying to sync
- Keep devnet-2 for now

Wait for pectra devnet-4 to have a stable base for rebasing on Pectra (maybe 2-3 weeks from now)
Devnet-3 target
 - https://notes.ethereum.org/@ethpandaops/peerdas-devnet-3 

### Spec updates

Decouple network subnets(https://github.com/ethereum/consensus-specs/pull/3832)
- **Lighthouse**: not sure if it’s high priority and a necessary abstraction right now, compared to higher priority changes like validator custody
- Prysm: not difficult to implement

Readiness to rebase on Pectra (devnet-3)
- **Prysm & Lighthouse**: ready, Lighthouse need testing
- **Teku**: need 2 weeks 
- **Lodestar**: 1-2 weeks

Spec release
- alpha.7
  - Will merge https://github.com/ethereum/consensus-specs/pull/3893
- alpha.8
  - Decouple subnets https://github.com/ethereum/consensus-specs/pull/3832
- Next spec release will include Pectra changes, so next peerdas devnet will include these changes
- Focus on Pectra rebase for the next peerdas devnet

Validator Custody
- https://github.com/ethereum/consensus-specs/pull/3871
- **Prysm**: how do we ensure nodes do this, and not cheat?
- **Lion**: there will be sufficient supernodes in the network, and it would cost them more to maintain a fork of the clients then use more bandwidth
- Most people run with default flags, so probably not an issue

Metrics spec (Katya)
- Renaming metrics to spec
- LH considers metrics renames as breaking changes
- Some metrics are from libp2p libraries, and may be difficult to rename, but we could rename peerdas specific metrics
- Gossip and Req/Resp metrics are difficult to rename, because they’re existing metrics for most clients (Prysm, LH, Teku). Might be worth starting with the DataColumns specific metrics

ACTION: Client teams to check the PR against client metric names and comment on the PR

Katya will be adding a Grafana dashboard into Kurtosis

Fetch Blobs (https://github.com/ethereum/execution-apis/pull/559)
- Lion raised this PR on the call as he thinks it will be an important change for increased blob count and PeerDAS
- LH has implemented this for Deneb
- **Prysm**: been discussing the designs, but not all ELs have implemented
- Teku is adding getBlobsV1 to Pectra
- Lodestar WIP, will also add for PeerDAS
- Most EL clients have implemented the getBlobs endpoint (Besu, Geth, Nethermind and EthereumJS), missing Geth

Has Clients implemented EIP-7742 (https://github.com/ethereum/EIPs/blob/master/EIPS/eip-7742.md)
- Not yet, ELs have not implemented this yet
- Barnabas proposed adding config for MAX_BLOBS_PER_BLOCK_FULU and TARGET_BLOBS_PER_BLOCK_FULU, to target for devnet-4

Josh and Hsiao-Wei looked into future PeerDAS project management
- https://notes.ethereum.org/tJaC6buSSj-YNOKVmAfbCg?view 
- Create a website like verkle.info for PeerDAS\
- Will share forms after this call

## Zoom Chat Links

https://github.com/ethereum/consensus-specs/pull/3832#issuecomment-2344120009

https://github.com/ethereum/consensus-specs/pull/3893

https://github.com/ethereum/consensus-specs/pull/3871

https://grafana.observability.ethpandaops.io/d/ddr7j9b1mlszkm/peerdas-metrics-specs?orgId=1&refresh=5s&var-consensus_client=All&var-network=peerdas-devnet-2&var-instance=All&from=1727773112949&to=1727776712949

https://docs.google.com/spreadsheets/d/1OrToYWl-XeIfTItBM6iqEsWjynmXu0ctyOj-83qzBVM/edit?gid=0#gid=0

https://github.com/ethereum/execution-apis/pull/559

https://github.com/ethereum/EIPs/blob/master/EIPS/eip-7742.md

https://notes.ethereum.org/tJaC6buSSj-YNOKVmAfbCg?view