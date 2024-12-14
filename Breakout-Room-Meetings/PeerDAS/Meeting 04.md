---
title: Meeting 04

---

# PeerDAS Breakout Room #4

## Meeting info

**Date**: 2024.07.23

**Agenda**: https://github.com/ethereum/pm/issues/1103

**YouTube Video**: https://www.youtube.com/watch?v=Rqd_DuPQMvg
## Notes
### Client updates

**Prysm**
- Optimized reconstruction to run in parallel across multiple blobs
- Optimisation to make blob available once 64 columns is available since node can always reconstruct

**Lighthouse**
- Working on devnet-1 issues, including the stack overflow issue with peerdas-kzg. Hoping to have a fix this week.
- Still working on sync issues, hoping to stabilize data column rpc methods before the next devnet
- Focused on getting das branch changes into our main branch

**Teku**
- All spec tests updated and passing
- Working on client stability and more tests
- Refactor sampler and added LossyDAS sampler

**Nimbus**
- Solidifying the code around p2p
- Found issues around syncing - full node sending out bad range requests
- Working with Kev on PeerDAS KZG lib and refactor reconstruction logic
- Working on sampling this week

**Grandine**
- EPF working on PeerDAS
- Still working on some sync issues

**Lodestar**
- Refactored syncing
- PeerDAS functionalities mostly working now, also support supernode via CLI params
- Added tests for block production, passing and should be able to participate in the next devnet
- ACTION: Before the next devnet start, we should have MetaDataV3 rpc methods to make sure nodes can identify peer custody columns correctly.

### Devnet Update

'peerdas-devnet-1' was shut down last week. There was a discussion on Discord on client readiness for the next devnet - client teams agree to postpone devnet-2 launch and focus on fixing current issues

**Prysm:** in the last devnet, clients had issues with initial syncing, we should aim to have this working before the next devnet so we can deploy new nodes

**Lighthouse:** Agree, also adding that clients should be able to serve data column rpc queries reliably

**Nimbus** asked how other clients are activating PeerDAS. Having PeerDAS activated at the same epoch as Deneb is difficult for Nimbus

- Lodestar and Prysm are able to activate the PeerDAS fork from Deneb without issue, however it's difficult for Nimbus to activate PeerDAS at the same time as Deneb as PeerDAS is a separate fork.
- Lodestar suggested that as a workaround for Nimbus, we could start with Deneb + PeerDAS at genesis but not send any blobs until Nimbus is ready. Nimbus agreed this would be helpful.
- ACTION: note to delay blob flooding when launching the next devnet

Clients talked about rebasing PeerDAS on Electra
- Prysm has already worked this out and can activate at Electra
- Will require Teku a week to rebase on Electra

Question raised: why are we activating PeerDAS at Deneb? It's never going to happen
- Teams agree that Electra is not stable enough for the purpose of testing PeerDAS, it makes sense to focus on getting PeerDAS functionality working properly on deneb, and rebase at a later time.

### Spec updates

No agenda items this week, however there are two significant upcoming spec changes that teams are encouraged to look at, and be good to finalize these
- PeerDAS fork-choice, validator custody and parameter changes #3779
- EIP-7594: Decouple network subnets from das-core #3832

Prysm raised a question regarding validator custody: if node doesn't reply with their custody columns, it can downscore the peer but not sure how this can be done with validator custody?
- ACTION: Manu to comment on the PR, as there wasn't a solution on the call.

## Zoom

https://github.com/ethereum/consensus-specs/pull/3821 