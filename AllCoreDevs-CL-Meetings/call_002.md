# Ethereum 2.0 Implementers Call 2 Notes
### Meeting Date/Time: Thu, Aug 30, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/3)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=66SFMJC0RQo)

# Agenda
1. Client Updates
2. Research Updates
3. Beacon chain testing lang
4. Q/A on v2.1
5. Practical details of random beacon and committee selection
6. Practical VDF implementations
7. Cross-shard communication
8. Proof of Custody
9. Closing remarks


# Client Updates
* Harmony (Mikhail)
  * working on block processing - nodes can propose and process blocks
  * state stored on disk
  * placeholder for state transition and fork choice
  * Next steps: state transition and attestations
  * planning on proposing alternative to handling state in spec
* Prysmatic (Raul)
  * Finishing PRs related to v2.1
    * attestations
    * infrastructure for applying fork choice
    * initial chanin sync
  * working on receiving attestations via p2p when assigned to a slot
    * considering using "one shard" on the p2p layer for the validators
* Lodestar (Mikerah)
  * implementing and understanding state transition functions
  * working on gossip sub in JS
* Nimbus (Mamy)
  * finished multi-sig BLS in Nim
    * Nim implementation of BLS can be exported to C++
    * No common serialized test for BLS available in Rust. Need to come up with
      a standard
  * finished 80% of "per block processing"
  * beginning to implement the IMD GHOST
  * provided feedback for test proceedures
* Pegasys (Nicolas)
  * New hires arriving next month
  * Investigating new version of casper in detail
* Lighthouse (Paul)
  * p2p serialization research to be shared
  * digging deep into state transition
  * going to start pushing blocks around soon (just pick serialization format
    for now)


# Research Updates
* eWASM (Alex)
  * Last three works working on testnet
  * eWasm/EthereumJS spending time on simulation of execution engine
    * black-box lower layer and simulate execution engine on top
* Sharding p2p poc (Kevin)
  * introduced communication between python and Go
    * data passed to python from go. validated in python, then passed back to
      go
    * sent via GRPC
  * added new tracer checker for more tracing
  * spending time surveying connection manager in gossip sub and look into introducing
    reputation system
* gossipsub simulations (Jannik)
  * progress. results expected in two weeks
* Randomness/VDF (Justin)
  * VDF day in Stanford went well. New results found
    * New way of [aggregating proofs by Benjamin Wesolowski](https://eprint.iacr.org/2018/623.pdf)
    * New way to watermark proofs with Validator's specific public key (for
      incentivization)
  * Dan Boneh encouraged using a ceremony to build RSA modulus for VDF config
    * similar concept to zCash ceremony
    * investigating viability
    * result is a 2000 bit RSA Modulus with no known factorization
  * IPFS and Chia might use same VDF so we might collaborate with them on
    research and buildling a VDF ASIC
  * Been digging into building RSA moduli trustlessly
    * pick 4000 bit random number. If no obvious small factors, it has high
      probability of being usable (~70%)
    * so if we pick enough, we have a high probability of picking at least one
      that meets the requirement which will satisfy the VDF.
    * tradeoff is you have to run multiple VDFs at once and proof sizes/outputs
      are large (~8KB)
  * ASIC looks like it will require on the order of 10W. More in the range of a
    graphics card, instead of just simply a USB stick
  * also been digging into modular multiplication algorithms
    * basis of VDF we are looking into
    * rich area of research
  * feeling more confident about VDF approach
    * confident on crypto-economics
    * confident on instantiating a praticular one
    * ASIC was biggest source of uncertainty but looking good
      * exotic processes other than silicon do not look feasible because
        complexity of ASIC will draw too much power
          * gallium-arsenide
          * silicon-germanium
      * ASIC looks feasible on CMOS silicon
* P2P serialization formats (Paul)
  * [benched several serialization formats](https://github.com/sigp/serialization_sandbox)
    * sizes for each
    * working on timing
  * [Simple Serialize](https://github.com/ethereum/beacon_chain/blob/master/beacon_chain/utils/simpleserialize.py) generally always smallest
    * gets to make assumptions about schema
  * probably going to hash these datastructures when you get them off the
    network so seems to make sense to push packets around the network in the
    same format that they will be hashed in
  * bringing in a third party library for deterministic formatting seems a bit
    brittle

# Beacon chain testing lang
* Danny
  * been discussing alternative formats to the string format proposed by Vitalik
  * JSON looks promising
  * String is easily writable, so a compromise should be to support string
    format and just parse it into the more universal JSON (or whatever we
    choose)
* Preston
  * Language does initially look quite bizarre
  * But how we derive the data doesn't really matter
  * If we go with JSON, we don't need a language specific parser
  * Why we need references to slots, if we are just trying to find head of
    chain given a set of blocks
* Danny
  * Goals of test
    * what is head
    * what is most recent justified
    * what is most recent finalized
  * fork choice and finality test that brings in the construction of the beacon
    chain along with "epochless" casper
  * slots are important because an attestation of a block at a slot is actually
    an FFG vote for that block and the ancestors of that block that span a
    CYCLE_LENGTH
  * there can be gaps in slots in a chain so you have to have a notion of this
    to capture everything that can happen in a fork choice
  * RNG doesn't really play a part here. Simply divide validators into slots
    and think about each committee at each slot starting at index 0
* Preston
  * How do we know what the global index is for a given validator selected in a
    slot?
* Danny
  * These are all equal weighted validators so you can just slice and split
    evenly into slots
* Mamy
  * currently two issues on github. one in beacon_chain and one in prysmatic.
    Where will future convo happen?
  * Json does not support comments. comments important for research.
  * 2ML and YAML also good options with comment support
* Danny
  * Agree, YAML makes sense
  * Conversation will continue on [Prysmatic issue](https://github.com/prysmaticlabs/prysm/issues/420) so follow that one

# Q/A on v2.1
* Shuffling look ahead
  * Paul
    * Does shuffling apply immediately or is there a look ahead?
  * Danny
    * no shuffling currently
    * reshuffling likely going to occur at dynasty boundaries (some multiple of
      cycle_length and if finalization)
    * at that point, you'd immediately have reshuffling
      * you've finalized and brought in validators so you have a notion of a
        new validator set that is ready to begin their work immediately
* Bad attestations in block
  * Terence
    * If you receive a block with some bad attestations in the block, what do
      you do? Maybe bad signature or incorrect slot height
  * Danny
    * That would be considered an invalid block and should be discarded
  * Justin
    * If you have one vote with a bad signature, it will pollute the entire
      aggregate signature. So doesn't really make sense to have a single
      signature wrong
  * Danny
    * Yes, but the entire attestation could fail the signature
    * The block producer should have known that, not included it, and not
      broadcast it
    * It's like someone producing a PoW block with an unacceptable difficulty.
      It should have been discarded
  * Justin
    * This is something to be considered from a DOS perspective.
    * PoW is very easy to check and expensive to create blocks that pass the
      initial easy pow check
    * If PoS block has a bunch signatures and only the last one is bad, it
      could waste a bunch of time
  * Mikhail
    * PoW is actually not that easy to check unless have precomputed data set
  * Justin
    * BLS signature verification takes on the order of miliseconds (2-3ms)
    * So if you have 64 attestations, maybe 100ms is worst case
  * Danny
    * We talked about dfinity style zero knowledge proofs to allow for
      privilaged actors. Do you have anymore insight on that?
  * Justin
    * learned at a meetup
    * Have not seen concrete details on this
    * Next whitepaper is about the networking layer
* Hanging onto good attestations from bad block
  * Paul
    * back to the last question, if you get to the end of a block and have a
      bunch of good attestations and just one at the end, it is probably worth
      hanging onto the good ones, correct?
  * Danny
    * If you haven't seen them yet and they are valid, they are worth putting
      in DB
    * Would likely be seeing them come in out of blocks. Might be worthwhile
      depending on if we are seeing a bunch of bad blocks


# Practical details of random beacon and committee selection
* Mikerah
  * How do nodes actually come to agreement on random number? Proposed RANDAO + VDF  but how do we agree on the output?
  * How do we actually sample committees?
* Danny
  * As for committees, `indices_for_slots` in `CrystallizedState` has one
    position for each slot. Each slot is an array of `ShardAndCommittee`
    objects that have a shard_id and a committee of validators.
  * `get_new_shuffling` outputs with `indices_for_slots` when given a new seed
  * `get_new_shuffling` will be used on dynasty changes to update `indices_for_slots`
* Justin
  * [slides from VDF day](https://docs.google.com/presentation/d/13OAGL42yzOvQUKvJJ0EBsAAne25yA7sv9RC8FfPhtyo/edit#slide=id.p)
  * Blocks will have RANDAO reveal. At the end of an epoch, XOR reveals to get
    RANDAO number. This is a weak source of entropy
  * Feed this output into the VDF
  * Some block producer finds output of VDF with a proof and includes it on chain
  * difficulty is adjusted depending on if before or after target_delay
  * target delay is a function of A_max (the assumed advantage an attacker
    can have)
  * This is incentivized by watermarking the proof with the validators public
    key so it can be rewarded and not stolen
* Danny
  * from an implementers perspective, another field in a block where the VDF
    output can be included and rules around whether VDF output is valid
    (inclusion time, proof check, etc)
  * This output can then serve as a seed of randomness and there will be rules
    around what seed of randomness to use when reshuffling


# Practical VDF implementations
* Danny
  * Justin shared a lot of this earlier in discussion of RSA Moduli
* Mikerah
  * Any results to be shared from VDF day?
* Justin
  * Main results from Benjamin Wesolowski paper. He said he is
    going to update this paper soon.


# Cross-shard communication
* Casey
  * Two main issues with [recent post](https://ethresear.ch/t/simple-synchronous-cross-shard-transaction-protocol/3097)
    * number one concern is if state execution gadget can keep up if too many
      rounds of communication/latency
    * second issue: phase 1 treats datablobs as generic. so how do we
      incentivize not stuffing these with junk?
* Hsiao-Wei
  * it is possible that block is full of junk
  * a decentralized twitter could pay validators to include not junk
* Danny
  * isn't that the point that there is no structure?
* Casey
  * If malicious validators could stuff with junk, there'd be no space left for
    useful data
  * Easy to design execution layer if we can assume there is useful tx data
* Justin
  * In sharding phase 1, every block to be the same size so every block will be
    100% filled. What goes in is ignored until launching VM
  * What incentivizes? same was current bitcoin and ethereum -- opportunity
    cost of missed fees by not including txs
  * Prior to having VM, can have out-of-band fees. Could imagine plasma chain
    to pay next proposer to include some tweet or something.
* Danny
  * But when an execution layer is added, do we not get a notion of block
    validity and blocks that could be discarded if invalid in terms of valid?
* Justin
  * only unavailable blocks will be discarded
  * Every block will serialize deterministically and not throw an error
  * once VM implemented, some of these blobs will become txs and run
  * some blobs might be related to other mechanisms or alternative execution
    engines
* Casey
  * Phase 1 only has block rewards, not tx/fee rewards.
* Justin
  * Yes, this is correct. This part of the design hasn't changed for almost 1
    year.
* Casey
  * looks like similar freedom to current EVM, proposers can create empty
    blocks or include a bunch of txs with gasprice 0.
* Justin - yes, exactly the same


# Proof of Custody
* Danny
  * in terms of just the beacon chain, there is no notion of proof of custody
  * This only comes into play with the building of the shard chains
* Terence
  * Seen some research threads, but haven't seen anything in the spec yet
  * Is this because we just haven't gotten there in the implementation?
* Danny - Yes
* Justin
  * Yes, need to sit down and spec
  * 1-bit custody scheme seems optimal in terms of overhead
  * not too worried about overhead of challenge game
  * need to figure out which hash function to use. Ideally a STARK friendly
    function. MIMC or one based on AES. STARK-ware is producing a public report
    on this soon
  * need to consider how long challenge period and secrecy period. Mainly
    parametrizations, don't affect design too much
* Danny
  * No stubs currently for validator's PoC bit and slashing conditions
* Justin
  * Yeah, we can just set custody bit to 0 for now

  
# Closing remarks
* Danny - predevcon eth2.0 meeting probably the 29th. details to come soon
* Carl
  * Still not happy with Proof of custody for decentralized staking pools
  * Trying to have a notion of no one in the pool being able to have enough of
    a secret that they can get the entire pool slashed
  * No solution on the top of my head
* Justin
  * There was an issue around hash-onion in pool.
  * Solution is to just move to separate commit/reveal per randao proposal
  * In terms of building proof of custody with hashing, still an issue
* Carl
  * If the degree to which you get slashed is minimal, then we can
    incentivize/punish in the context of the pool.


# Links shared during meeting
* [aggregating proofs by Benjamin Wesolowski](https://eprint.iacr.org/2018/623.pdf)
* [Sigma Prime serialization sandbox](https://github.com/sigp/serialization_sandbox)
* [Simple Serialize](https://github.com/ethereum/beacon_chain/blob/master/beacon_chain/utils/simpleserialize.py)
* [Discussion of testing lang on Prysmatic repo](https://github.com/prysmaticlabs/prysm/issues/420)
* [Justin slides from VDF day](https://docs.google.com/presentation/d/13OAGL42yzOvQUKvJJ0EBsAAne25yA7sv9RC8FfPhtyo/edit#slide=id.p)
* [recent post on simple cross-shard communication](https://ethresear.ch/t/simple-synchronous-cross-shard-transaction-protocol/3097)


# Attendees
* Mikerah (Lodestar/ChainSafeSystems)
* Danny Ryan (EF/Research)
* Chih-Cheng Liang (EF/Research)
* Dmitrii (Harmony)
* Mikhail Kalinin (Harmony)
* Paul Hauner (Lighthouse/Sigma Prime)
* Kevin Chia (EF/Research)
* Hsiao-Wei Wang (EF/Research)
* Jannik Luhn (Brainbot/Research)
* Ben Edgington (Pegasys)
* Carl Beekhuizen (Decentralized staking pools)
* Mamy Ratsimbazafy (Status/Nimbus)
* Nicolas Liochon (Pegasys)
* Nicholas Lin (EF/Research)
* Raul Jordan (Prysmatic)
* Jarrad Hope (Status/Nimbus)
* Jacek Sieka (Status/Nimbus)
* Alex Beregszaszi (eWASM)
* Preston Van Loon (Prysmatic)
* Justin Drake (EF/Research)
* Pawel Bylica (Aleth)
* Casey Detrio (eWASM/EthereumJS)
* Boris Petrov (Status/Nimbus)
* Terence (Prysmatic)
* Yutaro (Prysmatic)
* Nishant (Prysmatic)
