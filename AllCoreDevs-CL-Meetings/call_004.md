# Ethereum 2.0 Implementers Call 4 Notes
### Meeting Date/Time: Thu, Sept 27, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/8)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=SvcqFEwyZo0)
 # Agenda
1. Client Updates
2. Research Updates
    1. [3d visualization of beacon chain and shard blocks](https://beta.observablehq.com/@cdetrio/shasper-viz-0-4)
3. [Block processing timing results](https://github.com/ethereum/beacon_chain/issues/103)
4. Libp2p daemon
    1. [work in progress repo](https://github.com/libp2p/go-libp2p-daemon)
    2. @raulk from Protocol Labs will be [joining us](https://github.com/ethereum/eth2.0-pm/issues/8#issuecomment-424039741)
5. Testing
    1. [YAML chain test format](https://github.com/ethereum/eth2.0-pm/issues/8#issuecomment-424039741)
    2. [Proposed formats for SSZ tests](https://github.com/ethereum/beacon_chain/issues/115)
    3. [(empty) Unified Tests repo](https://github.com/ethereum/eth2.0-tests)
6. [Proposal to use separate serialization format for wire vs. hashing](https://github.com/ethereum/eth2.0-pm/issues/8#issuecomment-424849447)
7. [Alternative tree storage structures](https://github.com/ethereum/eth2.0-pm/issues/8#issuecomment-424849447)
8. V2.1 Discussion
9. Open Discussion/Closing Remarks
 # Client Updates
* Prysmatic (Raul & Terence)  _2:25-3:55_
  * Progress in the creation of a meaningful demo of a beacon chain workflow
    * Initial genesis chain starting & advancing through attestations and proposals
     * Able to stream to validator clients, assignments, shard IDs, and  their validator index at every single cycle transition
     * Able to request a subset of public keys (streamed to clients connected via PC)
  * Got up to date with v2.1 spec 
    * Updated the FFG rewards 
    * Proposed attestation check during block verification
    * Implemented attestation service for the beacon note 
      * Used to aggregate attestation and then save the aggregated attestation to the local DB. 
* PegaSys (Nicolas)  _4:00-5:10_
  * Team is setup. Beginning work on beacon chain implementation
  * Simulation of Casper IMD
  * Began work on libp2p
  * Began work on bls implementation

* Nimbus (Mamy)  _5:15-6:36_
  * Focused on simple serialize and implementing it fully and into the proposed YAML test format
  * Starting to focus on block processing timing that was proposed two weeks prior 
  * Planning to have common tests for simple serialized but also BLAKE2 and BLS signature
    * Helpful so everyone is on same page
    * Could be starting tests like what is done with Aleth in Eth1.0 
    * [New repo](https://github.com/ethereum/eth2.0-tests) created by Danny where we can put these common tests 
* ChainSafe (Aiden)  _6:42-7:20_
  * Working on, and implementing, simple serialize in pure js
    * Expected to finish in two weeks
    * Will be available as an NPM module 
  * Working on R&D for gossipsub pairings, BLS, and VDF libraries
    * Created several issues, hoping to get other people more involved
* Lighthouse (Paul)  _7:25-8:10_
  * Working on BLS implementation
    * Created standard crate and wrote a bunch of tests that it is passing, but could use some professional cryptographers to look at it and make sure it works 
  * Got implementation of simple serialize working 
  * Implemented some database fundamentals and are building out the core of the program 
  * Did some benchmarking on block validation using BLS
* Python (Danny)  _8:13-9:10_
  * Working through the rewards 
    * Found a few different bugs that have been fixed, and a few different bugs in the spec that have been fixed 
  * When benchmarking – a bug was found in the shuffling algorithm that made the number of committees per cycle unbounded, whereas the number of committees per cycle should be bounded via the shard count. 
    * That bug was fixed w/ minor changes
  * Working on beginning the process of porting into PyEVM to move towards a more production Python implementation 
* Harmony (Mikhail)  _9:16-10:12_
  * Completed work on block proposers 
    * Some areas of the implementation seem not to be aligned with the spec, especially in its base schema part. Working on attestations now. 
  * Updated their roadmap
    * up next: Casper, finality, and BLS signature aggregation
# Research Updates   
* Research updates (Vitalik)  _10:30-18:00_
  * Fixed another couple of bugs in the spec
  * Noted that in [one of the ethresearch threads](https://ethresear.ch/t/beacon-chain-casper-ffg-rpj-mini-spec/2760/17) – raised the suggestion of changing the fork choice rule from being immediate message driven to latest message driven. 
    * Discussion between Vitalik and Danny regarding the parameterization between the two perhaps being the way to go. 
      * Further thought is needed 
  * Discussion arose regarding whether to move forward with a two-layer beacon chain message attestation aggregation 
    * Because of the current spec, it was calculated that the average minimum peer-to-peer network load is around 50 kilobytes/sec. In the worst case scenario, gets closer to 500 kilobytes/sec. 
       * Further discussion ensued regarding a reduction to those numbers by having a structure that uses the shard networks to aggregate the attestations for a shard, and then broadcast the attestations into the main network. 
  * Discussion regarding launch roadmap:
     * One possibility that was discussed was creating a version of the spec that says we add an additional validity condition that states – if the main chain actually accepts some particular attestation for the shard, then that main chain should only be valid if that attestation is actually valid. 
      * Phase 0
        * Discussion regarding strategies about how to launch the sharding mainnet. One launch strategy discussed was deploying the sharding mainnet with “training wheels” through a version where: a node would not consider the beacon chain valid if it links to an attestation that’s invalid. (i.e. A version where every node is required to validate every piece of data, and the beacon chain would not be valid until that happens.) With the idea being that all of the shard gas limits (i.e. byte limit in this instance since there would be no computation) would be very low.
             * Discussion arose around the realistic possibility of having large staking pools (e.g. 1% of total ether) – and that those large staking pools would probably end up getting called into every shard anyway, so they’re going to have to have the data from all the shards regardless. Which was the rationale behind having everyone just run a super full node.
* VDF (Justin)  _18:05-27:05_
  * Posted a day earlier (ethresearch) about a minimal VDF randomness beacon
     * https://ethresear.ch/t/minimal-vdf-randomness-beacon/3566
     * “Minimal” in the sense that it goes right at the core of the construction, and does not have complexities like difficulty adjustment and direct incentivization for the valuators. 
        * Suggested that we don’t necessarily need these complexities – at least for the foreseeable future
     * Quote received from Obelisk (one of the companies potentially going to help design and manufacture the VDF ASIC)
     * Team in UK working on prover aspects
        * VDF has two parts: Evaluator & Prover
           * Prover is not as latency sensitive, it is more limited by throughput. 
           * Looking at hardware that would be most appropriate to implement the prover
  * Various calls had with Intel 
     * 3 guys interested in the VDF ASIC
          * 2 of them engineers at Intel for 20 years each
          * Able to provide a lot of perspective and interesting remarks 
   * Looking ahead in the coming months, Justin talked about how he would like to try and wrap up the feasibility study. 
     * Feasibility estimate as of right now has been around 75% - so gradually increasing. 
         * That remaining 25% is comprised of various components that have to work together simultaneously. Biggest uncertainty now revolves around the hardware (hardware in relation to the finances). Can we get something with very strong security at a reasonable budget? 
         * Further discussion ensued by Vitalik regarding what failure at the hardware side could potentially look like – bringing up an example of getting 2x speed gains by paying 8x more. All the way up to infinity. 
         * Uncertainty also around the circuit design side of things. Possibility of new breakthroughs on how multiplication is done, for example. More discussion with the researchers around optimization is being planned. 
        * Cost of fabrication per VDF rig is another uncertainty. 
            * Latest proposal: Suggesting that the Ethereum Foundation fully subsidizes all the hardware in collaboration w/ Filecoin and others. 
            * Instead of having direct, in protocol, rewards and thus buying an ASIC as an investment. Discussion was had about scrapping the rewards internally to the protocol and giving the hardware for free. 
            * Further discussion was had about having tiny rewards as an incentive mechanism, but only slightly enough to incentive inclusion. Further thought will be needed.
  * Hope is that perhaps by early 2019, could have some initial test net for CPU only VDFs, in addition to Randao

* Discussion Around Launching Network with just RANDAO initially – with VDF layered in at later phase (Casey, Vitalik, Justin)  _27:15-28:50_
  * Preliminary consensus reached that it would be fine, and even required, to launch the network with just RANDAO initially. In part due to the fact that it will take some time to develop the necessary VDF hardware (estimate given of at least 18 months)
  * Protocol layer can survive on RANDAO – it just means the security analysis of the protocol will be more difficult. Further thought on the subject of proper security margins put in place will be had at a later date. 
     * When the VDF upgrade is initiated, further discussion will to be had beforehand on whether to make the whole protocol more performance based by removing the margins, or make it more robust by keeping the margins and having this margin of error elsewhere. 
      * Note: A lot of value seems to lie at the application layer – where we exposed an opcode for strong randomness. Which is really only meaningful for Phase 2+

* Visualization of Sharded Chain work (Casey) _31:30-35:45_
  * https://beta.observablehq.com/@cdetrio/shasper-viz-0-4
  * Goal was to visualize how Phase 2 would look
    * Shows beacon chain, shard chains, crosslinks, and finalized blocks
  * Beacon block –> points to a crosslink – > after the beacon block, then all the shard boxes appear on the same slot. 
     * Simulations of network latency and possible forking are not present. 
     * No simulations present – more of a visualization. 

# libp2p
* Libp2p daemon (Raul from Protocol Labs)  _39:25-58:15_
  * Work on daemon has begun, but still in its protophases
  * Libp2p is a modular networking stack for building p2p assistance and has enhancing features, such as discovery, DHT, protocol transports, etc.
  * Implementations available in Go, Javascript, and Rust
      * In parallel, developing the p2p daemon, which is conceived as a standalone process that encapsulates the universe of the p2p features in a single binary, and allows for local applications running on the same machine to interact with the p2p network. No matter the language they are written in. 
  * Daemon takes care of connection management, stream management, multiplexing, security negotiation, etc. And essentially get role streams back, where each stream maps to a backend stream in the p2p, with a specific peer over a specific protocol. 
      * Also able to send control messages back and forth from the daemon
  * Actively developing
  * Engaging with Eth1.0 team in developing a libp2p based proof-of-concept of whisper v.6
  * Platform support:
      * Systems that support Unix domain sockets
      * Looks like Windows supports these to some extent
      * Looking at a shared memory transport to ensure availability on all platforms
  * Discussion ensued from Jannik regarding that – if the higher level protocols don’t work out, then we can still use the lower levels of the libp2p stack. Therefore, getting started on the implementation of libp2p, or at least a bridge to the libp2p could be beneficial. 
      * As such, if gossipsub does not end up being the precise higher level protocol, there was preliminary consensus that the bones of libp2p might be enough to have a slightly different, higher level protocol.

# Block processing
* Block Processing Timing Results  (Danny)  __58:15-1:01:30_
  * Lighthouse & Python beacon chain implementation did some quick analysis to sanity check estimates done on being able to process signatures at scale. 
     * https://github.com/ethereum/beacon_chain/issues/103
     * Results were very much in the bounds of reason and lent credit to initial estimates. 
         * Seems as though as long as we can figure out the aggregation on the network layer, these aggregate signatures are going to serve our purposes even in the extreme case where all ETH is validating. 
  * No unified test vectors for BLS implementations at this point
     * Need for standardization  
  * Lighthouse is using concurrency to attestation validation. 
     * Interesting note: If we had 10 million ETH, it was calculated to take 0.6 seconds to validate a block. However, if that shoots up to 100 million ETH, a 10x increase was not being shown. Not sure what was causing that to happen – but the theory is that it might be overhead due to threads. 
     * Would be interesting to see with no concurrency if we are getting the approximate 10x. Further tests to be done by Paul Hauner on that matter.

# Testing

* YAML Chain Test Format (Danny)  _1:01:32-1:02:50_
  * Mamy proposed an [SSZ test format](https://github.com/ethereum/beacon_chain/issues/115#issuecomment-423503435) that had a little more meta data that would allow use of the same general test structure for various tests
     * Teams to review, as a new test repo for the unified test will start to be filled out with tests under this format. 
     * The room noted the need to start targeting some unified testing – especially on things like extra libraries
       * No further comments – teams to review further the SSZ test format and the proposed structure in general

# Multiple serialization formats
* Wire vs. Hashing Serialization Formats (Alexey)  _1:02:52-1:25:25_
  * Impossible to derive a sufficient structure from the serialized stream when you don’t have schema information
    * Might have consequences due to things that preclude a lot of generic tooling (e.g. tools for traffic, visualizers, etc.)
    * Discussion arose regarding RLP, and how there was prior confusion between use cases for the wire format and the format for hashing.
      * RLP not good for producing hashing inputs because you have to pre-allocate a lot of large buffers before you can actually start hashing.  
      * Length prefixes of wire format are a positive, as they allow you to pre-allocate the buffers and allows you to derive sufficient structure w/o even looking at the schema.
        * This allows you to know how many items there are, where they begin and end, etc.
      * Length prefixes for the hashing itself, though, upon further discussion does not seem like a great idea. This is because it requires you to have that buffer before you start hashing. 
        * Suggestion: Have a format which doesn’t have a prefixes so you can actually stream into the hash function. Use the property of the sponge (e.g. If you need to hash a huge hash tree, then you can actually start streaming from the leaves, and as you go up you have one stream per level, and you can then hash the whole tree very efficiently. As opposed to now, where you need the buffers at each level, which is rather memory intensive.) 
          * Suggestion: Split up the serialization format and make them optimized for their respective uses. 
          * Further discussion to be had.
* Discussion ensued regarding SSZ in the context of shard chain Tx with the EVM
  * Talks about how the SSZ exists at a low level, but do not even need to exist at the Tx level were had. 
    * This is because the way that blocks will be divided into Tx is something completely different. (e.g. a format in which you have a bunch of shares, and each share is 256 bytes and the 1st byte of each share tells you where the separators are.)
    * The format of a Tx: it really could be anything. Because, ultimately, different Tx could have differing formats because of abstraction.
      * Note: We don’t even have to use RLP or SSZ, we could use a different format, it may not matter as much. Further discussion on the matter to be had.
* Discussion regarding tree-hashing along the structure lines instead of just hashing the whole thing as a blob. The idea being that, light-client access of the crystallized state would be easier.
  * Alternative to all of this would be:
    * Instead of having a hashing format, we basically hash the data structure as a merkle tree. And we would have a standard that says, “If you see a variable-sized array. You first make a merkle tree hash of the variable sized array, and then at higher levels you pretend that the byte is 32.”
    * Goal is to make hash updating cheaper in some cases, and in other cases, make light-client access of any state variable simpler. Can partition the data as well & may even be able to parallelize hashing. 
      * Costs of this will need to be further analyzed, and further discussion is to be had

# v2.1 Discussion 
* Staking  _1:25:39-1:29:30_
  * Jacek
    * Question brought up regarding the feasibility of adding an ice-age. And that, since there is only one-way staking going from ETH1.0 to ETH2.0, adding an ice-age in case the beacon chain contains some critical fault that would cause deposits to be refunded? (unless consensus was reached to move on from it)
      * (i.e. A proposal where people could get their money back out of that initial deposit contract if a certain time limit has passed and proper remedies have not taken place.) 
    * Discussion ensued regarding the matter. And further thought is needed. 

# Links shared during meeting
* https://github.com/ethereum/eth2.0-tests
* https://ethresear.ch/t/beacon-chain-casper-ffg-rpj-mini-spec/2760/17
* https://ethresear.ch/t/minimal-vdf-randomness-beacon/3566
* https://beta.observablehq.com/@cdetrio/shasper-viz-0-4 
* https://medium.com/rocket-pool/rocket-pool-beta-v1-postmortem-1809391d91b9 
* https://github.com/libp2p/go-libp2p-daemon
* https://github.com/libp2p/go-libp2p-daemon/pull/9
* https://github.com/ethereum/beacon_chain/issues/103
* https://github.com/ethereum/beacon_chain/issues/115
* https://github.com/ethereum/EIPs/blob/master/EIPS/eip-706.md
* https://github.com/mkg20001/libp2p-dissector
* https://media.consensys.net/releasing-wireshark-dissectors-for-ethereum-%C3%B0%CE%BEvp2p-protocols-215c9656dd9c


# Attendees
* Lane Rettig (eWASM)
* Vitalik Buterin (EF/Research)
* Alexey Akhunov (turbo-geth)
* Nishant Das (Prysmatic)
* Mikhail Kalinin (Harmony) 
* Danny Ryan (EF/Research)
* Carl Beekhuizen (Decentralized staking pools)
* Terence (Prysmatic)
* Justin Drake (EF/Research)
* Kevin Chia (EF/Research)
* Jannik Luhn (Brainbot/Research)
* Paul Hauner (Lighthouse/Sigma Prime)
* Chih-Cheng Liang (EF/Research)
* Adrian Manning (Lighthouse/Sigma Prime)
* Nicolas Liochon (PegaSys)
* Mamy Ratsimbazafy (Status/Nimbus)
* Casey Detrio (eWASM/EthereumJS)
* Jacek Sieka (Status/Nimbus)
* Hsiao-Wei Wang (EF/Research)
* Afri (Parity)
* Nicholas Lin (EF/Research)
* Karl Floersch (EF/Research)
* George Ornbo (Clearmatics)
* Raúl Kripalani (Protocol Labs)
* Aidan Hyman (ChainSafe)
* Prateek Reddy (EF/Research)
* Boris Petrov (Status)
* Alex Stokes (Ephemeral Labs)
* Tim Siwula (ConsenSys)

* Meeting notes by: Peter Gallagher 
