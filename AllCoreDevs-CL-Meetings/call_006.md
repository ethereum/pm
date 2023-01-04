# Ethereum 2.0 Implementers Call 6 Notes
### Meeting Date/Time: Thu, November 15, 2018 14:00 GMT
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/15)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=VNwANifX7qE)

# Agenda
1. Client Updates [_(5:45)_](https://youtu.be/VNwANifX7qE?t=345)
2. Research Updates [_(16:02)_](https://youtu.be/VNwANifX7qE?t=962)
3. Working Group follow-up [_(17:30)_](https://youtu.be/VNwANifX7qE?t=1050)
    * [notes](https://notes.ethereum.org/2-HRUzGjSc6jmwRgsVJqsg)
4. [min libp2p requirements](https://github.com/ethresearch/p2p/issues/4#issuecomment-436702674) [_(39:00)_](https://youtu.be/VNwANifX7qE?t=2341) 
5. [Proposal to use SSZ for consensus only](https://github.com/ethereum/eth2.0-specs/issues/129) [_(39:59)_](https://youtu.be/VNwANifX7qE?t=2399)
    * Should we have two serialization formats?
    * b. If so, what should the second be? ([@rawfalafel](https://github.com/rawfalafel) suggests protobufs in the above issue)
6. [big vs little endian](https://github.com/ethereum/eth2.0-pm/issues/15#issuecomment-439029818)  [_(48:45)_](https://youtu.be/VNwANifX7qE)
7. Spec discussion [_(51:00)_](https://youtu.be/VNwANifX7qE?t=3060)
8. Closing remarks [_(53:35)_](https://youtu.be/VNwANifX7qE?t=3215)

# Client Updates
* Lighthouse (Paul Hauner) [_5:45-6:25_](https://youtu.be/VNwANifX7qE?t=345)
  * Focusing on onboarding and expanding the team. As a result, Alex Stokes has joined the team
  * Going to start to shift focus towards state transitions and fork choice
  * One of their security team members has been working to point the AFL fuzzer library at their ssn implementation to see if they can break it  
      
* Nimbus (Mikhail)  [_12:24-13:47_](https://youtu.be/VNwANifX7qE?t=744)
  * Hoping to contribute a bit more to the easy-to-understand explaining guides
    * Started a new [repository](https://github.com/status-im/the-explainers) where they will be publishing a few tutorials. One on validators is already out. Another is coming out on the beacon chain
    * Encouraging others to help contribute with reviews and comments
  * Focusing on the light-client working groups. Investigating how to approach light clients secure fashion, while learning some of the lessons from ETH1.0
    * A testing group is also making progress. With a channel for discussions
  * Progress on libp2p daemon, tree hashing functions
* Harmony (Mikhail)  [_6:55-7:33_](https://youtu.be/VNwANifX7qE?t=415)
  * Finished with attestations, and now working on bls and finality
    * Regarding BLS, they decided to start with Milagro, evaluate it, and then decide if it is efficient for them or not. And then decide to maybe experiment and some trials to get a custom implementation of bls 
   
* Pegasys (Ben Edgington)  [_7:37-9:40_](https://youtu.be/VNwANifX7qE?t=457)
  * Nothing to report on the client development front
    * So far have implemented the state transition  
  
* Prysmatic (Terence) [ _9:44-11:10_](https://youtu.be/VNwANifX7qE?t=585)
  * Following closely with the spec, working towards transitioning between the crystallized state and active state into a singular state
  * Implementing a Go wrapper for bls12-381
  * bls library being used is called [Herumi](https://github.com/herumi/mcl)
* PyEVM (Hsiao-Wei Wang)  [_11:14-12:22_](https://youtu.be/VNwANifX7qE?t=674)
    * In the coming weeks, will be isolating time towards the Trinity client implementation with Danny
    * Will write a bounty code for ssz python implementation, which will make it be a more productioned version
    * Sorting out the version of the spec for the Trinity testnet. Hope that could be built by the end of 2018.
    * Danny and Hsiao-Wei are going to be working through all the changes in the spec pretty soon, and expect a lot of minor bugs, fixes, etc.
* ChainSafe (Mikerah)  [_13:50-14:30_](https://youtu.be/VNwANifX7qE?t=831)
    * Focusing and regrouping after Devcon
    * This weekend, will be holding another hackathon 
    * Going to focus more on turing their implementation towards more of a light-client, and plug into more of the dev-tools for the Ethereum JavaScript ecosystem.
  
* Parity (Fredrik Harryson)  [_14:36-15:34_](https://youtu.be/VNwANifX7qE?t=876)
    * Looking into the details of the spec
    * Looking to add more people in the near-term future to start building stuff out again
    * Plan right now is to still use Substrate
  
* Geth (Péter Szilágyi)   [_15:35-15:49](https://youtu.be/VNwANifX7qE?t=936)
    * Nothing really to report in terms of updates for this call
# 2. Research Updates  
* Pegasys (Ben Edgington/Nicolas Lionchon)  [_7:55–9:40_](https://youtu.be/VNwANifX7qE?t=475)
    * [White Block](https://www.whiteblock.io/) platform decided to open source, so another good simulation tool out there.
    * Continue to work on the simulator. Plan to present it in the call in 2 weeks
      * Fredrik Harryson chimed in, wondering if the simulator would be of importance to what we have in ETH1.0. Nicolas responded, saying it could be used for 1.0 as well. Research link was then sent to Fredrik for any further thought into the matter.
* Danny  [_16:31_](https://youtu.be/VNwANifX7qE?t=991)
    * Refining the spec
    * Recently pulled out phase0 and phase1 as two separate documents, in which phase0 - now that we've unified the state and made some minor changes - really expect it to be solidifying in the next couple of weeks
    * Phase1 document is still up for lots of changes. (Phase1 is adding of the data shard chains)
    * call for review and contribution
# 3. Working group follow-up 
* Had a work group follow-up the day before Devcon
  * [follow-up notes](https://notes.ethereum.org/2-HRUzGjSc6jmwRgsVJqsg)
* The working session Lane participated in (the ETH2.0 meet-up) was mainly about project management, coordination, etc. 
  * There was a pretty strong consensus that a pm/coordinator type role would be really helpful for managing the ETH1.0 roadmap. Not quite there for ETH2.0 for the time being
* Justin on VDF research [_20:06_](https://youtu.be/VNwANifX7qE?t=1206)
  * Estimated costs are down from an estimated $20-30 million to less than $20 million
    * Initial discussions have begun with Tezos for collaborating on research and production
  * Security
    * "Effective A_max" of 4 * A_max (about 1 in a million chance for an attacker controlling 2/3 of the slots to bias one bit)
    * Will write an ethresearch post deep-diving into the various cryptographic and hardware assumptions
  * Progress with MPC
    * Ligero to publish academic paper in December
    * Simulations with 256 participants for 256 bit modulus => very promising
    * Writing custom code for 2048-bit bignum crypto
  * Influx of interest after Devcon talk
    * 3 Bitcoin mining companies
    * Various individuals
    * Shopping around for team to manage manufacturing
    * More projects interested in using VDF's (e.g. a DEX using them to prevent front-running)
  * Found a team of FinFET compressor experts
  * Another VDF day on February 4
  * Investigating hybrid Pietrzak-Wesolowski prover with nice tradeoff between prover and verifier overhead
* Danny [_21:38_](https://youtu.be/VNwANifX7qE?t=1298)
  * One interesting thing noted was that, Vitalik and Al from Web3, realized that just fork choice rules based upon justification have this inherent flip-flop issue
    * [ethresearch](https://ethresear.ch/t/beacon-chain-casper-ffg-rpj-mini-spec/2760/21) post that proposes ways to make LMD Ghost in the context of justified epochs "stickier"
  * Paul asked a question regarding the shards living in the same client node software as the beacon node
    * Expectation is that multiple shards should be able to run in the context of a standard computer
    * so, presumably, one validator client piece of software could talk to one node that has a beacon node and multiple shards
      * but because the validator client software would be talking via RPC to a node, it could talk to multiple nodes, and one node could sync shards 3, 5, and 6. Another could sync shards 10, 11 for example
        * So, yes, the shards live in the same client node software as the beacon node. But if we design the API appropriately, the validator software could talk to multiple ETH2.0 nodes and tell each one what shards to sync.
* Jacek [_24:45_](https://youtu.be/VNwANifX7qE?t=1485) had a question regading the architecture
  * How much do we want to put in the spec as an implementation requirement? 
    * some client and use cases it might be reasonable to use a different constellation of actors
    * seemed to be some consensus. Danny chimed in, discussing one succinct goal he has, of defining an API such that a piece of validator software can be cleanly pulled out of a node. He imagines a node often might ship with a built in piece of validation software, but we want to keep the separations clean, such that someone else can write a validation piece of software so we can have a diverse set-up. 
      * a kin to the RPC methods of ETH1.0
  * Terence chimed in regarding the architecture, asking how should a validator manage private and public keys? 
    * Discussion ensued, specifically around the fact that a node should not be managing keys, and that the layer outside should be
      * but in terms of best practices of HOW the client should go about that - more dicussion around embedding keys and secured pieces of hardware are needed. For Ethereum, perhaps it would be best to recommend and cite a manual of best practices
* Paul [_31:43_](https://youtu.be/VNwANifX7qE?t=1903) chimed in regarding the ability for a validator to be able to hide on the network
  * work on aggregation scheme, not sure how that would affect ability for validator to hide?
    * Carl responded [_32:25_](https://youtu.be/VNwANifX7qE?t=1947) Always aware who the first person is that generates the data before the aggregation starts. (not necessarily who you received the data from, just that you received the data from that person first)
    * Nicolas [_33:30_](https://youtu.be/VNwANifX7qE?t=2010): depends on the number of shards that you add on a single computer. In terms of anonymity, if you used the tree based logic, then you need to notified as a participant in the aggregation protocol. You can be participating w/o telling where the aggregation comes from, and you don't have to say where the signature comes from, but you do have to be notified as a participant
      * you can have a specific key just for participating. And can be different from that one being signed
      * In that type of tree structure, you network ID can be different than your validator ID
      * All in all though, it does out you as a validator. W/o bringing some sort of alternative incentivization, tough to see user nodes participating in the protocol.
      * Further discussion ensued. And perhaps the best we can do is ensure that the network level identifiers are not who we really are, and the p2p network is not inherently tied to our validator identification
# 4. [Min libp2p requirements](https://github.com/ethresearch/p2p/issues/4#issuecomment-436702674)
  * Danny  [_39:00_](https://youtu.be/VNwANifX7qE?t=2341) 
    * Raul and Kevin defined the minimal libp2p implementation 
      * in an effort to help people who are working on p2p implementation to narrow the scope in what they are going to work on
    * Jacek chimes in to say he really appreciates the effort :]
      
# 5. [Proposal to use SSZ for consensus only](https://github.com/ethereum/eth2.0-specs/issues/129) 
* Something that was brought up by Alexey in the past, and recently brought up again
* One of the motivations being that, now we are moving towards the tree hashing algorithm for the state, some of the presumed benefits are no longer there
* Paul Hauner commented in the issue, and can see how it may make hashing faster, but not personally convinced w/o seeing benchmarks/data that it is actually a problem
  * spec is trying to avoid heavy optimization, and lean towards simplicity
  * by shrinking down ssz, we don't make the spec less complicated, but more - as now we are doing an import of all of protobuf into the spec. and we end up 2 encoders and 1 decoder
  * further discussion to be had two fold:
    * does SSZ not serve our purposes for the protocol serialization and should we be looking into an alternative?
    * and if yes, what should that alternative be?
    
# 6. [big vs little endian](https://github.com/ethereum/eth2.0-pm/issues/15#issuecomment-439029818) 
* Jacek, on the potential benefits of moving from big endian to little endian
  *	Hardware today basically uses little endian. Modern serialization formats tend to favor little endian for this reason because you are better mechanically aligned with the software & hardware
  * Consistency argument for using big endian on network protocols for historical reasons
  * Will write up a proposal to make clear his position for further discussion
# 7. General spec discussion 
* Been discussing the different phases (phase0 and phase1, etc.) and now we are moving towards having a clear delineation in the spec. 
  * the idea is that a phase-N is dependent upon all the phases less than N. And that all the phases less than N can be built without thinking about phase N
    * right now that is just the beacon chain (internally phase0), and the shard data chains on the outside of that. State execution on the layer outside of that, etc.
* Unified the state into a single state root, because we are using the tree hashing algo, such that when block changes happen, most of the state doesn't change so, therefore, most of the tree hash won't have to be re-hashed
  * effort for simplicity and also allows us to serve components to the tree easily (light clients)
* Phase0 stuff -- trying to get all of the big changes in now, so that people can really dig in and target that phase0
# 8. Closing remarks 
* Danny: considering organizing another workshop. Maybe in Q1, maybe before/after ETHDenver
* Mamy chimed in, saying that FOSDEM (biggest free and open source conference) submitted a request for a dev room, and that they will have a decentralized internet room
  * some from Nimbus will be there, and he invited others to join as well
  * Fredrick chimed in, saying Parity will be there
  * might make sense to get together the day before and hack on some of these issues
  * Quick talks (10 min) can be applied for, w/ the deadline to apply ending in 15 days 
 # Links shared during meeting
* https://github.com/ethereum/eth2.0-pm/issues/15
* https://github.com/ConsenSys/wittgenstein
* https://github.com/herumi/mcl
* https://github.com/prysmaticlabs/go-bls
* https://notes.ethereum.org/2-HRUzGjSc6jmwRgsVJqsg
* https://github.com/ethereum/eth2.0-tests/pull/3/files
* https://ethresear.ch/t/beacon-chain-casper-ffg-rpj-mini-spec/2760/21
* https://hackmd.io/KAYlfelmSE2gHnK_6cZy4g?both
* https://github.com/status-im/the-explainers
* https://notes.ethereum.org/9MMuzWeFTTSg-3Tz_YeiBA?view# 
* https://github.com/ethereum/eth2.0-specs/issues/129
 # Attendees
* Péter Szilágyi (EF/geth)
* Nicolas Lin (EF/Research)
* Nicolas Liochon (Pegasys)
* Nishant Das (Prysmatic)
* Alex Stokes (Lighthouse/Sigma Prime)
* Jarrad Hope (Status)
* Jonny Rhea (Pegasys)
* Joseph Delong (ConsenSys)
* Daniel Ellison (ConsenSys)
* Lane Rettig (EF/eWASM)
* George (Clearmatics)
* Danny Ryan (EF/Research)
* Carl Beekhuizen (Decentralized staking pools)
* Terence (Prysmatic)
* Justin Drake (EF/Research)
* Kevin Chia (EF/Research)
* Jannik Luhn (Brainbot/Research)
* Paul Hauner (Lighthouse/Sigma Prime)
* Chih-Cheng Liang (EF/Research)
* Adrian Manning (Lighthouse/Sigma Prime)
* Mamy Ratsimbazafy (Status/Nimbus)
* Hsiao-Wei Wang (EF/Research)
* Jacek Sieka (Status/Nimbus)
* Fredrick Harryson (Parity) 
* Mikerah (ChainSafe)
* Blazj Kolad (Pegasys)
* Ben Edgington (Pegasys)
* Martin Holst Swende (EF/geth/testing)
* Meeting notes by: Peter Gallagher (Independent Ethereum Researcher)
