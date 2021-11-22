# Ethereum Sharding Implementers Call 0 Notes
### Meeting Date/Time: Thu, Aug 2, 2018 14:00 UTC
### Meeting Duration: ~1 hour
### [GitHub Agenda Page](https://github.com/ethereum/beacon_chain/issues/44)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=Ynqrka5DQOI&feature=youtu.be)

# Agenda
1. General Introduction of Sharding Meeting
2. Client Updates
3. Research Updates
4. Open Discussion
    * [v2.1 spec](https://notes.ethereum.org/SCIg8AH5SA-O4C1G1LYZHQ#)
    * [Conforming to p2p messages, prysmatic protocol buffers](https://github.com/ethereum/beacon_chain/issues/44#issuecomment-405298161), and other p2p related discussion
    * [BLS signature standard libraries](https://github.com/ethereum/beacon_chain/issues/44#issuecomment-405415540)
        * https://github.com/milagro-crypto/amcl/tree/master/version3
    * Current state of cross shard communication research
    * Actionable items for clients and research
    * Format/Timing of future meetings

# Client Updates
* Lighthouse (Paul)
	* Waiting for v2.1 spec to finalize
	* Have first version of beacon chain implemented
	* Working on minimal p2p
	* Looking at BLS implementations
* Python beacon_chain (Danny)
	* Almost done with v2.1
* Nimbus (Mamy)
	* Working on v2.1 from spec
	* Exploring BLS options
		* Wrapper in NIM for [Milagro Crypto](https://github.com/milagro-crypto/milagro-crypto-c)
		* Considering building from scratch
* Prysm (Raul)
	* Migrated away from geth -- independent eth2.0
	* Local network p2p via gossipsub
	* Full beacon node running (v2.1)
		* State transition functions
		* Shuffling, cutoffs
		* Induct incoming validators from pow receipts
		* Working on forkchoice and chain sync
	* Sharding client (separate process communicates via RPC)
	* Simulator tool for simulating incoming blocks
* Pegasys (Ben Edgington)
	* Team building -- Olivier and another new hire
	* Looking into BLS implementation
	* RNG research
	* Working on beacon chain implementation
* Harmony (Mikhail)
	* Beacon chain
		* Deposit contract and induct validators from receipts
		* Working on block production, state transition functions, etc
	* [Progress and plans](https://github.com/ethereum/ethereumj/wiki/Sharding-Implementation)
* Lodestar Chain (Mikerah)
	* Javascript beacon chain implementation
	* Looking into BLS options
		* Trying to use Milegro crypto primatives to build BLS curve
		* Looking into compiling from rust to web assembly
	* Beginning to implement v2.1 state transition functions
	* Project started at internal hackathon. Steady progress

# Research Updates
* Vitalik
	* Recursive Proximity to Justification (RPJ) forkchoice
		* [minimal partial spec on ethresearch](https://ethresear.ch/t/beacon-chain-casper-ffg-rpj-mini-spec/2760)
			* focuses just on ffg+rpj
			* Goal to be analyzed and formally proven
		* RPJ design goals
			* Maintain safety and liveness of FFG
			* Simplicity
			* Stability
				* Forkchoice is a good prediction of future forkchoice
				* hybrid rules are bad at this
				* RPJ is good
			* Maximize resistance to manipulation of RNG
				* resistant up to 80-90% of chain being overtaken by attackers as long as majority of attesters are honest
	* 99% fault tolerant article coming soon
* Mamy
	* [Collection of research and materials](https://github.com/status-im/athenaeum/blob/master/ethereum_research_records.json) related to sharding
	* Please create pull request if anything missing
* Justin
	* Randomness Beacon
		* how to construct once we have VDF
		* Which VDF to use
			* Favorite -- [Construction by Benjamin Wesolowski](https://eprint.iacr.org/2018/623)
			* True VDF -- exponential gap between compute/verify
			* Based on RSA Groups so need to think about setup (how to pick RSA modulus)
				* Can use small random numbers as moduli for parallel sub-VDFs
				* If at least one modulus cannot be factored, then who construction is safe
		* VDF cryptographers meeting in SF to discuss
		* Hardware manufacturing
			* Build VDF ASIC commodity
			* Needs to be close to no-expense-spared attacker ASIC
			* Access to these commodity ASICs will counter no-expense-spared attacker
		* Full RNG spec likely in 1.5 to 2 months
* WASM execution engine and cross-shard txs (Casey)
	* Black box sharding phase 1 in an effort to prototype phase 2 (execution and cross-shard execution)
		* black box the ordered data-blobs and links between them
		* phase 2 prototype will just process ordered datablobs from json
	* Advantages prototyping phase 2 in JS
		* libp2p library
		* access to native jit engine
	* Delayed state execution model

# BeaconChain v2.1
* Vitalik
	* Parts of this spec are provisional. Expect to change broadly if RPJ is included
		* Dynasty transition
			* just have one validator set for now
		* Epoch transition
		* RNG
	* Things worth working on
		* BLS aggregate signatures
		* General structure
			* ActiveState
			* CrystallizedState
			* bitfield tracking aggregate signatures
		* Stub what shard to work on
			* each height can just correspond to one particular shard
	* If you get to the above and block box the suggested, then try working on p2p
	* Rest of protocol details will be filled in likely over next 2 months
* What is v2.1
	* Danny: combining block attestations and shard crosslinks also serving as FFG votes
	* Vitalik: three things
		* ffg voting
		* small scale block attestation
		* shard crosslinks
	* Vitalik
		* If num_validators is too small to have one distinct committee at every height, will probably have committees overlap.

# P2P
* p2p message format
	* Preston
		* Prysmatic currently using [protobufs](https://developers.google.com/protocol-buffers/)
		* protobufs have unordered fields which can be a problem with hashing
		* Exploring alternatives such as FlatBuffers
		* Proposal: Agree early on a schema with wide adoption
	* Hsaio-Wei: Is it deterministic serialization?
	* Jacek
		* Protobuf spec doesn't define the order
		* Little extra features that make protobuf difficult to use in a hashing setting
		* Stripped down version could work
	* Mamy: FlatBuffer and CaptainProto are options
	* Hsaio-Wei
		* Prysm is using protobufs for messages but which serialization are you using for encoding the data for database?
		* If we use different serialization for data and p2p, we might have to do two serializations when syncing
	* Raul
		* Prysm uses proto for serialization in DB
		* protos for all process communication
	* Vitalik
		* Why crystallizedstate need any special serialization when you can just pack values together
	* Raul: because state is communicated between processes
* Signature aggregation wrt network
	* Mikhail
		* What does this look like? How many messages required to attest?
	* Vitalik
		* Not much yet
		* validators publishing messages that need to be aggregated every ~8 seconds could be a bottleneck and warrant a separate p2p
		* If naive is too hard, we can consider hierarchical scheme
			* Selected nodes are in charge of aggregation for subset of network
	* Justin
		* Could use random path strategy
			* tag on own signature as attestation is passed around
	* Vitalik
		* That takes O(N) time
		* Need something that takes 2-3 rounds of network communication
	* Raul
		* Currently setting up pieces of system to be able to test aggregation
* RLP
	* Mikhail: what's wrong with RLP
	* Hsaio-Wei: Too complicated
	* Preston: RLP not very fast
	* Jacek
		* RLP missing a schema
		* Would like a schema
* Further discussion on message format at [ethresearch](https://ethresear.ch/t/discussion-p2p-message-serialization-standard/2781)
* P2P layer (Gossipsub?)
	* Paul: Is Prysm using gossipsub?
	* Raul: Yes 
	* Danny: Is the beaconchain and shard chains p2p going to be the same?
	* Vitalik: Beacon chain should be on some layer everyone downloads by default
	* Raul: Beacon nodes on topic "shard -1" and have network for separate shards
	* Kevin
		* Beacon chain messages in a global topic
		* So everyone in same network but segregated
	* Justin
		* How many topics per shard?
		* could be -- one for headers, one for unsigned blocks and unaggregated signatures, one for fully signed and aggregated blocks
	* Mikhail: Does number of channels affect network amplification rate?
	* Kevin
		* You only broadcast to peers that have subscribed
		* If receive message not subscribed to, can band peer
	* Mikhail
		* More concerned about discovery being impacted by number of channels
	* Kevin: worth testing
	* Justin
		* One strategy is to have common discovery layer for all channels and have gossip on top.
	* Kevin
		* We currently have a global channel for discovery
		* Exploring other discovery protocols
	* Danny: gitter channel for testing and discussing [here](https://gitter.im/ethresearch/sharding-p2p-poc)
	* Mamy: It's not worth implementing libp2p from scratch because we haven't made a firm decision, right?
	* Danny: Yes, we don't have enough testing to say we are going to use it for sure at this point.
# BLS Signatures
* Danny: So it seems that there aren't a ton of standard BLS implementations across the various languages
* Vitalik
	* There are standards for BN128 because we put it as [precompile](https://eips.ethereum.org/EIPS/eip-196) in [Byzantium](https://eips.ethereum.org/EIPS/eip-197)
	* Not sure how substantial it is to migrate these libraries to BLS12-381
* Danny: What's the benefit of changing the curve?
* Vitalik
	* [Higher security margin](https://blog.z.cash/new-snark-curve/) (~100 bits --> 128 bits)
	* ZCash and other projects are standardizing so worth going with the flow.
* Justin: Chia too
* Jacek: Chances of community finding another curve?
* Vitalik
	* Unlikely due to standardization effort going in
	* Unlikely something broken in bls12-381
	* One property a new curve could have that would be better:
		* if new curve pointed to a pair of curves where one is the modulus of the other, and the other is the curve order of the first. This would be really nice for zkSNARKS
* Danny: What needs to be done to standarize these libraries?
* Vitalik
	* I need all the params and a couple hours of hand-holding with a knowledgable cryptographer
* Jacek: Outlook for fully audited reference implementation for this curve?
* Justin
	* Rust implementation being spearheaded by ZCash
	* Has been audited by security company
	* Abstract spec has also been audited another security company
	* Rust impl has been worked on for many years
* Paul: Does it have aggregates?
* Justin
	* It's for base layer operations
	* Aggregation is trivial on top
* Paul
	* We hacked together an implementation but probably "as safe as broken glass"
* Vitalik
	* Preference for dealing with "rogue key attacks" is [proof of possession](https://rist.tech.cornell.edu/papers/pkreg.pdf) at deposit time.
	* Not currently implemented but fairly trivial
* Paul: on PoW chain or separate?
* Vitalik
	* Do on beacon chain
	* Probably should do as little as possible on PoW chain to facilitate migrating deposits to shard chains
* Paul: Should probably put a note about rogue key attack in reference implementation
* Danny
	* It's in the v2.1 spec but still in PoW chain.
	* Likely just going to do the burn in the PoW contract and do all the validation of validator init data in beacon chain
* Justin
	* As much as possible in beacon chain
	* Question remains: how to do the bootstrapping process to onboard initial validators
	* Research post coming soon
	* Rust BLS implementation is performant but not constant time crypto so possibly vulnerable to timing attacks
* Vitalik
	* Pairings do not need anti-side-channel protection because just verification
	* Elliptic curve multiplications need it
	* There are decades of research on this so no fundamental obstacle here

# Cross-shard communication research
* Mikerah
	* v2.1 doesn't really go into cross-shard comms. Does research team have any more formal ideas, writings, etc
* Vitalik
	* v2.1 spec doesn't cover state execution at all
	* There are various posts on [cross-shard txs](https://github.com/ethereum/wiki/wiki/Sharding-FAQs#how-can-we-facilitate-cross-shard-communication) and [yanking](https://ethresear.ch/t/cross-shard-contract-yanking/1450). That's the extent at this point
* Casey
	* In terms of the phase 2 proto type, are phase 1 and 2 sufficiently decoupled for this to work?
* Vitalik
	* If they are to be entirely decoupled, execution and data consensus would have to be separate.
	* Blocks would not contain state roots
* Casey
	* That's delayed state execution?
* Vitalik
	* Yes, if we make an agreement that we are doing delayed state execution, then the two are fully decoupled.
	* If use eth1.0 model, they are coupled
* Justin
	* Considering not shuffling shard proposers often  so they don't have to incur the cost of syncing state
* Casey
	* In stateless execution, don't have that problem
	* In general, execution and cross-shard comm are relatively understudied.
	* Hoping to spike more interest in this problem
	* Even names phase 1 and phase 2 give impression of not being able to work on phase 2 before phase 1 is built.
	* Would like to see more work on phase 2 in parallel

# Last remarks
* Sharding workshop
	* Ben Edgington: Any interest in workshop/get-together around devcon?
	* Justin: Makes sense to do an event immediately before or after
	* Jacek
		* Status hosting hack-a-thon before in Prague. Might be able to use venue. Will check with team
* `get_shuffling` 
	* Paul: Looks like it might have an infinite loop
	* Vitalik
		* It is the case that there is no upper bound
		* But sharp probablistic bounds
	* Danny: I remember there being a loop too, will check it out
* Shared repo for testing and contracts
	* Raul: Makes sense to open a shared repo for testing and contracts
	* Danny: I agree esp on testing. Are we ready for shared testing?
	* Raul: No, not yet.
	* Danny: Let's get something together in the next couple of weeks.
* [Justin VDF presentation on gitcoin](https://twitter.com/drakefjustin/status/1025040874386939904)
	* VDF presentation
	* Sharding AMA

# Links shared during meeting
* [Status sharding research records](https://github.com/status-im/athenaeum/blob/master/ethereum_research_records.json)
* [Prysmatic message proto](https://github.com/prysmaticlabs/prysm/blob/master/proto/sharding/p2p/v1/messages.proto)
* [Prysmatic serialization github issue](https://github.com/prysmaticlabs/prysm/issues/150)
* [Cap'n Proto](https://capnproto.org/)
* [Flat Buffers](ttps://google.github.io/flatbuffers/)
* [how protobuf is non-deterministic](https://developers.google.com/protocol-buffers/docs/encoding#order)
* [protobuf notes gist](https://gist.github.com/kchristidis/39c8b310fd9da43d515c4394c3cd9510)
* [Harmony sharding implementation progress](https://github.com/ethereum/ethereumj/wiki/Sharding-Implementation)
* [JS Lodestar Chain](https://github.com/ChainSafeSystems/lodestar_chain)
* [Serialization comparison table](https://notes.ethereum.org/15_FcGc0Rq-GuxaBV5SP2Q)
* [Serialization ethresearch post](https://ethresear.ch/t/discussion-p2p-message-serialization-standard/2781)
* [Milagro crypto](https://github.com/milagro-crypto/milagro-crypto-c)
* [VDF Construction by Benjamin Wesolowski](https://eprint.iacr.org/2018/623)
* [Justin VDF presentation on gitcoin](https://twitter.com/drakefjustin/status/1025040874386939904)
* [VDF Reading list](https://t.co/hDVSNImQ40)

# Attendees
* Justin Drake (EF/Research)
* Danny Ryan (EF/Research)
* Raul Jordan (Prysmatic)
* Nikolay Volf (Parity)
* Mikhail Kalinin (Harmony)
* Dmitry (Harmony)
* Ben Edgington (Pegasys)
* Olivier (Pegasys)
* Preston Van Loon (Prysmatic)
* Jannik Luhn (Brainbot/Research)
* Hsiao-Wei Wang (EF/Research)
* Mamy Ratsimbazafy (Status)
* Ryan (Status)
* Jarrad Hope (Status)
* Jacek Sieka (Status)
* Chris Spannos (EF scaling grant recipient)
* Paul Hauner (Lighthouse/Sigma Prime)
* Adrian Manning (Lighthouse/Sigma Prime)
* Carl Beekhuizen (Decentralized staking pools)
* Chih Cheng Liang (EF/Research)
* Lang Rettig (EF/eWASM)
* Kevin Chia (EF/Research)
* Nicholas Lin (EF/Research)
* Vitalik Buterin (EF/Research)
* Mikerah (Lodestar/ChainSafeSystems)
* Casey Detrio (EF/ethereumJS)
* Alex Beregszaszi (EF/Ewasm)