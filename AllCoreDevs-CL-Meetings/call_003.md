# Ethereum 2.0 Implementers Call 3 Notes
### Meeting Date/Time: Thu, Sept 13, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethresearch/eth2.0-pm/issues/5)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=cp0LxJiyV3I)

# Agenda
1. Client Updates
2. Research Updates
3. [YAML test format](https://notes.ethereum.org/-1cuR-dzR3W4R3qJJXyrSw)
3. v2.1 Discussion
4. Tentative decision on the following:
    1. p2p serialization format
    2. p2p network protocol
    3. p2p discovery protocol


# Client Updates
* Prysmatic (Terence)
  * Aligning with v2.1
    * new state and dynasty updates
    * need to do FFG balance updates
  * implemented validator service 
    * with partial proposer responsibilities
    * with partial attester responsibilities
  * refactored codebase for readibility and maintainability
  * Currently using levelDB but benchmarking others
* Lodestar (Mikerah)
  * Planning dev of libraries
    * Pairings library in JS (research phase)
    * GossipSub (research phase)
    * BLS sig library
    * VDF Library
* Lighthouse (Paul)
  * [Implemented simple serialize (SSZ) in Rust](https://github.com/sigp/lighthouse/tree/master/ssz)
    * raised [issue](https://github.com/ethereum/beacon_chain/issues/92) about issue
  * working on block processing
    * investigating dos resistance for beacon chain blocks (wrt attestations)
  * [issue on get_new_shuffling](https://github.com/ethereum/beacon_chain/issues/91)
  * working more on state transition library
  * working more on ancillary libraries
* Pegasys (Ben)
  * Onboarding new hires
  * Researchers analyzing and modeling new casper
  * Blaze getting up to speed on p2p protocols
  * Beginning to write some beacon chain code
* Nimbus (Jacek)
  * implementing fork choice
  * [concern around using sequence of hash tables](https://ethresear.ch/t/beacon-chain-casper-ffg-rpj-mini-spec/2760/13)
  * looking into implementing altbn library due to licensing issues
* Harmony (Mikhail -- read by Danny)
  * working on State transition
  * attestations are next milestone
  * still working on potential proposal of DB state changes
* Parity (Afri)
  * Probably start working on new client for Eth2.0
  * Team meeting in two weeks to discuss path forward for eth2.0
* beacon_chain (Danny)
  * implemented dynasty change
  * some work on justified_slot in attestation
  * working through reward logic to clean up spec


# Research Updates
* eWASM (Lane)
  * Focussed on preparing testnet for launch before devcon
  * Casey working on shasper sim and prototypes around state execution
* add to v2.1 (Vitalik)
  * Dynasty transition
  * balance changes
* [Simplified Casper Slashing condition](https://ethresear.ch/t/a-tight-and-intuitive-casper-slashing-condition/3359) (Justin)
  * Slashing conditions can be weakened to single slashing condition
  * Safety proof still holds
* VDF (Justin)
  * how to program moduli (hardcoded or programmable)
    * looks like hard coded is better for us
  * picking moduli carfeully can reduce logic gates in ASIC (reduced die area)
  * debating class groups vs RSA groups
    * Chia likely to use class groups
    * Eth still considering RSA groups
  * Can construct hybrid between two provers. Between
    * one that is optimal and size
    * one that is efficient to compute
  * [Obelisk Launchpad](https://obelisk.tech/launchpad.html) might be good service to build the ASIC
  * Considering multi-party ceremony for picking RSA modulus
    * approach seems viable
    * only need one honest player to destroy their source
    * new constructions are 10x faster and one team thinks can do 1000s of
      participants in a few minutes
  * Been discussing modular multiplication with specialized teams
* Trusted cermony notes (Vitalik)
  * even if we go with the ceremony approach, the casper ghost alg is designed
    with the idea that the VDF can be broken and we still get the basic
    guarantees of security
  * If VDF is secure, then security tolerances can be much lower and the RNG
    can be used for applications.
* sharding p2p poc (Kevin)
  * refactoring and debugging
  * working on log aggregation
  * restructuring relationship between go and python to move most of logic in
    python
  * To do
    * looking into testing more at scale
    * looking into alternative protocols for discovery
* gossipsub simulations (Jannik)
  * [Simulated collation propogation in single shard](https://github.com/jannikluhn/sharding-netsim/issues/2)
    * nothing too surprising
    * max block size in this network was 3MB
    * All but slowest nodes have available bandwidth
    * number of peers didn't matter too much. Good numbers between 4 and 8 peers
  * Tested push-pull protocol
    * No obvious advantages over gossip sub
  * next up is peer discovery
  * GossipSub
    * Simple
    * can handle the load
    * appears to do what we want
* Structured aggregation
  * Vitalik - has anyone given any thought to protocols that aggregate sigs
    step by step instead of putting entire burden on proposer
  * Danny - so thought is to have subset of notes that aggregate subsections of
    the network and aggregating?
  * Vitalik 
    * essentially, yes. There are probably lots of ways to do this
    * Unstructured aggregation will likely result in duplicates that
      can't be aggregated anymore
  * Justin - We can make the bitfields handle some amount of overlap
  * Vitalik 
    * This might complicate unnecessarily. We should try to solve at
    network level first
    * It will be okay do it naively during testnets, but we'll need something
      before launch
    * IDEA:
      * validators already in shard p2p
      * dual purpose existing shard subnets for sub aggregation
      * republish aggregates to main p2p for proposer to fully aggregate
      * requires bridge nodes and multiple rounds of communication
      * might need slot length to be 16s instead of 8s
* Benchmarks on block verification
  * Vitalik - Have there been benchmarks assuming a certain number of validators?
  * Danny
    * Python implementation could pump these numbers out easily
    * I'll make an [issue](https://github.com/ethereum/beacon_chain/issues/103) so multiple clients can try this
  * Vitalik - As opposed to eth1.0, beacon chain won't have potential issues with
    quadratic blowup do the state calculations
* RSA Modulus
  * Mamy - do we need to implement RSA wrt the RSA modulus or is it just for
    the VDF?
  * Justin 
    * Just for VDF
    * Just RSA in the sense that it has same requirements -- unfactorizable
* Sparse merkle tree
  * Alexey - any implementations yet?
  * Nishant - [one in go](https://github.com/musalbas/smt)
  * Jannik - [one in python](https://github.com/ethereum/py-trie/pull/58/files). not sure how far along it is

# YAML Test Format
* Danny
  * [Proposed YAML chain test format](https://notes.ethereum.org/-1cuR-dzR3W4R3qJJXyrSw)
  * Isomorphic with previous string format
  * Do people have comments?
  * Let's get comments between now and next meeting

# v2.1 Discussion
* libp2p support
  * Blaze
    * Any discussion about porting libp2p to other languages?
    * How to make it available in other languages
  * Paul
    * Protocol labs interested in assisting new implementations
  * Jacek
    * Discussing an implementation in Nim which would expose an impl in C
    * No where near completion
  * Mamy
    * Still unsure about libp2p so not dedicating too much resources yet
  * Danny
    * Are we feeling confident in deciding to use libp2p and gossipsub?
  * Jannik
    * I like gossipsub based on research
    * Not sure about discovery yet
  * Danny - So close, but not quite ready to make decision
  * Jannik - existing discovery mechanism could work for testnet purposes
  * Kevin
    * We can use some common code with GRPC to allow other languages like we are
      doing with python/go in PoC now.
  * Blaze
    * protocol labs provided an http daemon for IPFS.
    * Maybe we do same for gossipsub
  * Hsiao-Wei
    * Longterm we want a python implementation of gossipsub
  * Danny
    * Research team signalling 90/95% sure on gossipsub
    * probably worth investigating what an implementation in your language would
      look like
    * _close_ to decision
* BLS Proof of Possession
  * Terence - how do we generate?
  * Vitalik
    * there is a standard formula
    * for now, use your key to sign a hash of your public key
  * Danny
    * Needs to be a different hash function
    * these params will almost certainly be verified in beacon chain
    * so beacon chain will to support main hash plus auxiliary hash for Proof
      of possession
* Generating public/private key
  * Terence
    * Have we decided on library for generating private/public key?
  * Vitalik
    * Either using bn256 or BLS12-381
    * as far as library it depends on your language and what is available
* Shuffling motiviations
  * Paul
    * What motivations of `get_new_shuffling`
    * Assuming
      * spread out validators across slots evenly
      * ensure every shard is attested to
    * there are some cases where there are enough validators to create
      commmittees of min size and attest to every shard, but not always doing
      that
    * seems to target `2*min_committee_size`
  * Vitalik
    * intention is for `min_committee_size` to be a min, not a target
    * as validators --> infinity, committee size should stablize toward `2 * min_committee_size`
  * Paul
    * going to write out some requirements for clearly understanding and testing
    * will request feedback
* Rejecting blocks quickly
  * Paul
    * figuring out how to most quickly reject invalid blocks to prevent dos
      attacks
    * Is there a way we can easily see if block producer sig is in the
      attestations to easily throw out if not
  * Vitalik
    * We can make spec put proposer attestation at the 0th position
  * Danny
    * block validity rule is premised upon inclusion attestation from _parent_ block proposer
    * but, I shouldn't process a block unless I see a proposer attestation for
      the block in question come in on the wire
    * 4 conditions before processing -- one is receiving proposer attestion
      with block
* p2p serialization
  * Danny
    * previously discussed using [ssz](https://github.com/ethereum/beacon_chain/tree/master/ssz) for serialization
      of wire protocol
    * are there any objections?
    * can we make decision today?
    * silence says, we are making a tentative decision
    * decision made
  * Paul
    * lighthouse has been implementing and it seems pretty simple and optimal
  * Mamy
    * Can we create test repo for shared tests
    * maybe use new YAML scheme?
  * Danny
    * the YAML scheme is more of a chain test
    * Will consider if it can be more generic for this purpose
    * definitely time for test repo
  * Paul
    * I found a small [issue with ssz](https://github.com/ethereum/beacon_chain/issues/92)
    * Would like people to take a look
  * Vitalik
    * looking now... 
    * oh wait what version of ssz is this?
  * Paul
    * version from beacon_chain
  * Vitalik
    * in this version, because length of `int32` is known, no length is part of the serialization
    * seems like name collision issue
    * this was designed to optimize for the availability of direct mappings for
      datatypes
    * speeds up block processing
    * length in serialization only occurs for variable length datatypes
  * Mamy
    * We can use compression on top of ssz to compress the space
  * Jacek
    * How does this differ from parsing a format into binary convenient to you
  * Vitalik
    * true but has a clean separation of layers
    * serialization alg isn't going to achieve optimal no matter what so people
      will be incentivized to compress
  * Jacek
    * need to look at blow up attacks for decompression
  * Vitalik
    * good to look at
    * but fundamental scalability of protocol does not need compression
  * Mikerah
    * Need formal spec of ssz
  * Vitalik - Should work on one
  * Danny
    * good target
    * currently only what is in beacon chain
    * will pull it out as library as well
* Discovery protocol
  * Danny
    * Not enough research yet
    * tabling this decision


# Tentative Decisions
* p2p serialization format
  * decided [ssz](https://github.com/ethereum/beacon_chain/tree/master/ssz)
  * need formal spec and shared tests
* p2p network protocol
  * 90/95% sure on gossipsub
* p2p discovery protocol
  * too early 
  * need more research


# Links shared during meeting
* [Lighthouse implementation of SSZ in Rust](https://github.com/sigp/lighthouse/tree/master/ssz)
* [Issue about SSZ](https://github.com/ethereum/beacon_chain/issues/92)
* [issue about get_new_shuffling requirements](https://github.com/ethereum/beacon_chain/issues/91)
* [Simplified Casper Slashing condition](https://ethresear.ch/t/a-tight-and-intuitive-casper-slashing-condition/3359)
* [Obelisk Launchpad](https://obelisk.tech/launchpad.html) for potentially
  building VDF ASIC
* [Concern around using sequence of hash tables in forkchoice](https://ethresear.ch/t/beacon-chain-casper-ffg-rpj-mini-spec/2760/13)
* [p2p simulation results](https://github.com/jannikluhn/sharding-netsim/issues/2)
* [Block processing time estimates issue](https://github.com/ethereum/beacon_chain/issues/103)
* [Sparse Merkle Tree in go](https://github.com/musalbas/smt)
* [Sparse Merkle Tree in python](https://github.com/ethereum/py-trie/pull/58/files)
* [Proposed YAML chain test format](https://notes.ethereum.org/-1cuR-dzR3W4R3qJJXyrSw)
* [ssz in python](https://github.com/ethereum/beacon_chain/tree/master/ssz)


# Attendees
* Lane Rettig (eWASM)
* Vitalik Buterin (EF/Research)
* Alexey Akhunov (turbo-geth)
* Nishant Das (Prysmatic)
* Blaze (Pegasys)
* Mikerah (Lodestar/ChainSafeSystems)
* Danny Ryan (EF/Research)
* Carl Beekhuizen (Decentralized staking pools)
* Terence (Prysmatic)
* Justin Drake (EF/Research)
* Liam Horne (L4)
* Kevin Chia (EF/Research)
* Jannik Luhn (Brainbot/Research)
* Paul Hauner (Lighthouse/Sigma Prime)
* Chih-Cheng Liang (EF/Research)
* Martin Holst Swende (EF/geth/security)
* Adrian Manning (Lighthouse/Sigma Prime)
* Nicolas Liochon (Pegasys)
* Ben Edgington (Pegasys)
* Mamy Ratsimbazafy (Status/Nimbus)
* Casey Detrio (eWASM/EthereumJS)
* Preston Van Loon (Prysmatic)
* Jacek Sieka (Status/Nimbus)
* Hsiao-Wei Wang (EF/Research)
* Afri (Parity)
* Nicholas Lin (EF/Research)