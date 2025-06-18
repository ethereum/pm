# Full DAS

### Summary

This session aims to discuss research and development points related to reaching FullDAS. FullDAS is here defined as blocks of 32MBs that are 2D erasure-coded into 128MBs, sharded into rows/columns, diffused effeciently over the network, and cell-wise sampled within the required time.  

### Facilitator: Leo Bautista-Gomez, Csaba Kiraly

### Note Taker: Leo Bautista-Gomez, Csaba Kiraly, Mikel Cortes. [Here](https://hackmd.io/lqs5GePQSCWHIrYhIYYWtw)

### Pre-reads:

* [Sampling](https://ethresear.ch/t/full-das-sampling-analysis/20912)
* [FullDAS](https://ethresear.ch/t/fulldas-towards-massive-scalability-with-32mb-blocks-and-beyond/19529)
* [PeerDAS](https://ethresear.ch/t/peerdas-a-simpler-das-approach-using-battle-tested-p2p-components/16541)


### Optional:

* [LossyDAS](https://ethresear.ch/t/lossydas-lossy-incremental-and-diagonal-sampling-for-data-availability/18963/3)
* [Big Blocks](https://ethresear.ch/t/big-block-diffusion-and-organic-big-blocks-on-ethereum/17346)
* [DAS](https://blog.codex.storage/data-availability-sampling/)
* [Danksharding](https://ethereum.org/en/roadmap/danksharding/)

### Slides: WIP

- [ Intro and Sampling Horizons - Leo](https://drive.google.com/file/d/15Snd5RYBrfUtkPVN_4zxjpPqGU95Kk0c/view?usp=drive_link) 
- [FullDAS Ingredients - Csaba](https://drive.google.com/file/d/15N8oLiYEIRKzlOi1LOYh30GaNEljpNXr/view?usp=drive_link)

## Agenda

* **Introduction and outline of the session (15 min - Leo)**
The session wil start by enumerating the list of topics that we want to cover during the session and asking the audience if they want to add anything missing topic.

* **The ingredients of FullDAS (20min - Csaba)**
This will be an interactive talk presenting some of the components necessary to reach full DAS. 

* **Sampling Study for FullDAS (20min - Leo)**
This will be an interactive talk presenting some of the research done on sampling and outlining a list of actions necessary to take, to reach full DAS.

* **Open Discussion (20min - Csaba)**
Open mic to discuss all remaining topics and adress pending questions.

* **Summary and Conclusions (15min - Leo)**
Summary of TODOs and actions list towards FullDAS.


## Notes & Actions Items

### Full DAS, as we discuss here (after PeerDAS session)

- next logical step after PeerDAS
- aiming for maximum scalability
- targeting 32 MB blob space
- using 2D erasure code (improved diffusion, repair, and sampling)
- granular sampling at cell level

### Sampling
Problem with the sampling:
- While sampling, there are some edgy cases where peers could think:
    - blobs are available when they aren't -> False Positive (Not too common scenario, but bad for safety, hance we limit probability to 0.0000...1)
    - blobs aren't available when they are -> False Negative (tooooo common, which hurts performance and maybe even liveness)

**LossyDAS** / **Availability Amplification**
- LossyDAS: sample more (increasing the BW requirements), allowing some of them to fail, while having a better availability view from the network
- Availability Amplification: fundamental difference between 1D encoding with only columns-based distribution, and 2D encoding with cell-based distribution. Latter allows repair by any node, not just supernodes.

**Horizons on sampling**
how many cells from the 2D blob structure can you see at different hop-count distances.

- Flat custody 
    - depends on the level of connections
    - limits you on the % of successfull sampling you do from the network 

- Proportional Custody 
    - topic subscription should be linked to the validator count on the node
    - ~5% of the network hosts enough validators  to become super-nodes
    - There are some techniques to even support a 90% of the network being malicious ("exponential sampling"?). However, there are some concerns about spamming that 10% of honest peers and DOS them

**Questions**
- should there be something in between PeerDAS and FullDAS?
    - There is no PeerDAS even, neither sampling (yet)
- On the sampling side, who decides the randomness of each validator's sampling
    - your validator ID (pubkey))?
    - do you decide it yourself
- Proof of Validator
    - avoid spamming and sybil attacks by proving that you have a validator
    - how to use it is still under discussion
        - create a sub-network from these nodes with a proof of validator
        - should it be used to protect both diffusion and sampling?
        - should it be delayed?

### Networking side of things
- GossipSub could be be used to propagate the blob-parts, but investigating improvements and other protocol choices
- Use custody values to define how many topics will each node subscribe to
- This should be deterministic with the "Deterministic Custody" coming from the NodeID

## Open topics for discussion
### Distributed Block Building and Sharded Mempool

With new designs mempool has its own DA issues.
- How should we handle DA at the mempool level?
- Should transactions be pre-encoded in mempool?

Discussion left for separate session.

### Networking stack
- should we stick to libp2p? 
- should try other options?

Problems with Libp2p:
1. discover nodes that have what we need
2. we need to connect peers for sampling and there are limitations to this (error rates?)
3. All this is needed for req/resp over TCP 

Possible solutions:
1. use UDP-based stack
2. reuse Libp2p but add "ephemeral connect"
3. multi-hop approaches / DHT-like?
