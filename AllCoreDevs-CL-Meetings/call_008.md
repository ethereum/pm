# Ethereum 2.0 Implementers Call 8 Notes
### Meeting Date/Time: Thursday 2018/12/13 at 14:00 GMT
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/19#issuecomment-446142928)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=NO9UlkpFKA0)

# Agenda
1. ♦ Client Updates [_(10:10)_](https://youtu.be/Zl-yusB8oqY?t=610)
2. ♦ Research Updates [_(16:45)_](https://www.youtube.com/watch?v=NO9UlkpFKA0)
3. ♦ ["low hanging fruits" for testing](https://github.com/ethereum/eth2.0-pm/issues/19#issuecomment-446023967) [_(58:43)_](https://youtu.be/NO9UlkpFKA0?t=3523) 
4. ♦ [unsigned under and overflow problems](https://github.com/ethereum/eth2.0-pm/issues/19#issuecomment-446142928) [_(1:00:58)_](https://youtu.be/NO9UlkpFKA0?t=3658)
5. ♦ General spec discussion [_(1:08:10)_](https://youtu.be/NO9UlkpFKA0?t=4090)
6. ♦ Open Discussion/Closing Remarks [_(1:16:01)_](https://youtu.be/NO9UlkpFKA0?t=4561)

# Client Updates
* Nimbus (Mamy)
  * At most 1 day off the spec
  * Implemented our scheme for BLS signature
  * Implemented the commit-and-reveal scheme for Randao
  * showcased a YAML test generator for the shuffling 
    * Dedicated repo: https://github.com/status-im/eth2-testgen
    * Request for tests, BLS signature and aggregation (internally and from other teams)
  * Implemented a mock GossipSub based on RLPx
  * Blocked on issue in libp2p pubsub: https://github.com/libp2p/go-libp2p-pubsub/issues/130#issuecomment-446886342
    * When multiple connection are done to the same peer if one connection is closed all connection are also closed.
  * Community:
    * https://our.status.im/tag/nimbus/
    * 2.0 series - Chinese, Croatian and Albanian
      * Intro to beacon chain
      * Intro to validators
      * Transition PoW to PoS
* Py-EVM (Hsiao-Wei Wang) 
  * BLS impl, waiting for review
  * Trying to catch up the specs    
* Harmony (Mikhail Khalinin)
  * BLS refactor, trying to be generic over elliptic curves
  * implement SSZ
  * high-level tools for annotation for SSZ
  * abstracting from EthereumJ
  * Touch base with Pegasys —> collaboration for crypto and libp2p
* Pegasys (Akhila Raju)
  * Coming soon - open-sourcing beacon chain repo -- Artemis, torchbearer, god of lightness 
* Prysmatic (Terence)
  * Catching up with spec
  * Refactoring sync services, combining initial and normal sync
  * SSZ implemented 
* Lodestar
  * [Update](https://github.com/ethereum/eth2.0-pm/issues/19) was given by Mikerah in the agenda
  * Successfully migrated to typescript 
* Parity
  * substrate coming along 
# 2. Research Updates  
* Mamy [_16:45_](https://www.youtube.com/watch?v=NO9UlkpFKA0)
    * [Whitebloc](https://www.whiteblock.io/) had some updates from the simulation groups from a call the week prior that Mamy had some notes on. 
      * Call with 8 people - main topic about network emulation
      * They started some nodes, and anyone can join
      * Main issue talked about and raised by Alexey was how to generate network activity (txs, etc)
    * next step for simulation group is coming up with a test plan
      * propose test plan and ask for collaboration 
      * repo is in the plan, and some generic type of tests that everyone can get inspiration from to test on their client
        
* Leo (BSC) [_20:27_](https://youtu.be/NO9UlkpFKA0?t=1227)
    * Been doing some refactoring on the simulator that he plans to run on the supercomputer
    * Added a couple of features:
      * previously, every single MPI process (Message Passing Interface). More info on what MPI is can be found [here](https://computing.llnl.gov/tutorials/mpi/)
        * every single process was simulating a single node in the network. Now, one single MPI process can simulate multiple nodes in the p2p network
          * allows for more larger scale simulations
      * added some speed up time features. Can speed up time up to 100x - so that the execution of the blockchain happens 100x faster than it would happen in real life
    * had some questions:
      * Right now using small-sizes for the simulations for testing the software 
      * when we look at the spec, we have appx. 1000 shards and 256 validators per shard. Wanted to know how this compares to the current number of nodes in the current Ethereum network? 
        * Further discussion ensued. The number of validators per shard actually scales. It scales in a function called `get_new_shuffling`. 
        * Essentially, if we reach a certain threshold of validators, then per cycle, we crosslink all shards each cycle 
          * but if we do not reach a minimal threshold, then it starts taking mutliple cycles to crosslink all the shards (so that we don't have too few validators in our committees that are crosslinking)
          * the # of shards is to be fixed. The minimum # of validators for this to begin is defined by a threshold constant in the pow deposit contract. (which is 2^14, or 16,384)
          * another thing to consider is that these validators are 32ETH instances. And, in all likelihood, a lot of actual physical nodes in the network will represent multiple validator instances
            * don't know exactly what that distribution will exactly be. But say we have 300,000 validators, and we have the same # of nodes in the network today (let's say appx. 16,000). That equals out to be about 18-19 validators living in each node, and participating in multiple shard subnets
            * so, when we are doing simulations, we have to make some sort of assumptions about distributions of how many validator instances are in a physical node
          * Say we have 10million ETH validating, with about 300,000 validators, the actual distribution of nodes on the network (in this instance, let's say 10,000-15,000 nodes on the network now) - would we expect to have a similar amount of nodes in the network and just have many validator entities crunched into each one? What do we expect that to look like?
            * VB responded, saying it's tough to tell now, and that he thinks we'll definitely see a power law distribution of some kind. 
            * One nice thing, brought on by JD, is that the amount of resources required for validator (as in a node with multiple validators) grows linearly up to roughly 1,000 validators (32,000 eth). So, if you have relatively small validators that are not pooling, then that should lead to a lot of physical machines. Although it's hard to predict how much pooling will happen.           
     * Talks ensued and someone brought up if the system scales dynamically, in terms of # of shards, or if scaling happens instead with how fast the shards get validated?
       * Scaling 2 things: (at least in the current spec)
          * 1. How frequently crosslinks appear (load on the beacon chain)
          * 2. This might only be in the Phase1 file right now - but if the # of validators is too small, then we allow some of them not to submit proofs of custody (PoC). With the idea that, at least some of the validators won't actually be doing full validation, they will basically just be validating data availability proofs or something similar.
            * idea is that, to compensate for the fact that we have fewer validators, each one would have to do much more work, we would instead allow some of them to not submit the PoC bits (this allows mean that they have to check more blocks, but for most of the blocks they would be able to skip doing most of the work)
            * essentially random sampling on who has to do the hard work so that your resource requirements stay close to constant, even though you're distributed across more of the network
       * general idea from a design perspective is to enable a graceful degredation, and we could have a dynamic # of shards but reducing the # of shards is something that is very disruptive
     
* Justin [_38:53_](https://youtu.be/NO9UlkpFKA0?t=2333)
    * wanted to give some visibility into significant changes that will happen to the spec
    * One of the things being considered is to pull out validator balances separate from the registry. 
      * the idea here is that the balances are updating very frequently for the validators, but not so much the rest. So, for example, we could save on the hashing and do less hashing at every epoch
        * moving to keccak256, that might be a requirement, just to reduce the load per epoch on the hashing
    * relatively minor changes in terms of the actual implementation side of things (same validator, same index into that entity) but significant from a data structure re-org
    * in terms of data structure reorg, we are considering merging some of the fields for justification and finality (4 different fields right now. we could merge them all into a single bit field that grows by one bit epoch, and that bit represents whether or not the epoch was justified)
    * considering adding more RANDAO mixes to the state 
    * need to include various placeholders (for PoC and VDFs). Hoping for these to be additions to the existing data structures.
    * in terms of significant changes:
      * there will be some changes simply due to bug fixing that is happening (many bugs have been squashed the last couple of weeks, but Justin still thinks there is a lot of unidentified bugs lurking. Needs academic review)
      * fork choice rule
      * need a review of the bls hash function
      * new logic around the justification and finalization for Casper FFG (more people need to look at that and try to break it, or ty and prove that it's correct)
    * Discussion ensued around a single miner taking ownership of the blockchain
      * Danny talked about the attestation fork choice, in that many validators get to participate in the fork choice of each block being proposed. And beyond that, up to the way the group rewards and penalties are calculated. (and that the more participants in the consensus, the higher the rewards there are)
      * Vitalik also chimed in, thinking that analyzing incentive compatability and stability and various other properties is really important. So far, all that we really have to work off of are existing arguments that we know about off of GHOST.
        * the one thing that still makes him feel uncomfortable about GHOST is the stitching between the fork choice rule and the finality gadget. And that seems to be one of those areas where there could be some kinks (stitching is also where the flip flop issue arose)
      * Justin also chimed in on the topic of block proposers having this monopolistic issue because we only have a single proposer having full control over the next block
        * agrees with Danny in that this has been addressed to a large extent with attestations
        * doesn't address things like censorship, however. Proposer could create an empty block if they want, but it does address things like trying to build on top of an ancestor and trying to do short term things like take-over attacks and such.
        
* Jannik [_50:13_](https://youtu.be/NO9UlkpFKA0?t=3013)
  * talked to Felix a little bit, and he was happy that we considered discv5 and discussed three things we can do:
    * 1. finding gaps in the spec (things not talked about, or only touched briefly upon)
    * 2. formalize it
    * 3. wire protocol, there are no messages or anything defined 
  * Danny addressed the room, saying if anyone has any familiarity with p2p discovery protocols it would be a good place to start contributing to.
  * https://github.com/ethereum/devp2p/blob/master/devp2p.md 
# 3. ["low hanging fruits" for testing](https://github.com/ethereum/eth2.0-pm/issues/19#issuecomment-446023967)
* Mamy [_58:43_](https://youtu.be/NO9UlkpFKA0?t=3523) 
    * For shuffling, if everything is in the spec he just copy/pastes in the test generator and we can have shared test vectors in YAML
    * If some are missing (like bls) he just asks the py-evm team if there is some kind of implementation that they can use
    * if there are some suggestions on test vectors, feel free to open a PR on the test gen repo
      * goal is to push that upstream, so that in ETH2.0 tests, once there is something solid other people can use it. But for now, they are using the Status repo 
# 4. [unsigned under and overflow problems](https://github.com/ethereum/eth2.0-pm/issues/19#issuecomment-446142928)
* Mamy [_1:00:58_](https://youtu.be/NO9UlkpFKA0?t=3658)
    * Issue raised twice in the last couple of weeks from Jacek and Paul H. 
    * maybe just remove the minus (-) from the spec and use the plus (+) everywhere?
    * talked last call about some kind of implementer good practices
      * seemed to be some consensus on moving towards the plus (+), but as Paul pointed out, anything coming in from a user might actually just be very high values that mess up that plus (+) and cause overflows (even though it's highly unlikely because most of them are related to slots. But if it's user supplied data, it could cause that.)
    * Seemed to be consensus on having a separate best practices document being started on
* Haven't really solved the underflow/overflow problem. We know it is a problem and need to make sure it's addressed.
# 5. General spec discussion
* As for doing another formal meetup, on the research team they are airing on the side of not doing anything specific in Q1
* Thinking maybe in April to target getting anyone together, and keep Q1 focused on work
* Raúl [_1:10:06_](https://youtu.be/NO9UlkpFKA0?t=4206) sparked a discussion about overall issuance for Ethereum.
  * before we migrate the state, there's going to be validators earning rewards, and overall the cumulative issuance of ether will go up - has this been thought about in terms of how the transition will happen/the economics of eth throughout that process/etc?
    * The issuance to validators is generally marginal compared to the issuance of miners. So we don't foresee it being a major concern. 
    * Beyond that, there is a proposal floating around to do this hybrid PoW/PoS proposal where you begin to utilize the beacon chain for finality
    * Over time, ultimately, issuance will go down when the system is entirely PoS
      * during that time, validators can move stake over through this deposit contract. But when state execution exists on shard chains, there will likely be another enshrined transfer contract/deposit mechanism to move from eth1.0 --> eth2.0
      * a lot of little things to think and talk about still regarding that
 * https://www.ethhub.io/ run by Eric Conner, is a great place for community contribution. And goes more into the economic aspects of the transition/PoS/derivative contracts/etc. 
# 6. Open Discussion/Closing Remarks
* With the holidays coming up, next meeting likely to be had in the first/second week of January perhaps
* Potential meetup in Barcelona sometime in 2019? Further discussion to be had.
# Links shared during meeting
* https://consensys.zoom.us/recording/play/4s4cWk5uEoCR3SeIv3U-6gggJCiPKBwx-F5Tp_F2hg6p6ISRJ--WKW-LjhgPEXoE?continueMode=true
* https://github.com/ethereum/eth2.0-pm/issues/19
* https://github.com/status-im/eth2-testgen
* https://github.com/libp2p/go-libp2p-pubsub/issues/130#issuecomment-446886342
* https://our.status.im/tag/nimbus/
* https://notes.ethereum.org/Q_kQKXZUQD29YCshej1qPQ
* https://notes.ethereum.org/QFLP8uBYSRiAbzpx1Rr9Rw
* https://wb-genesis.appspot.com
* https://whiteblock.io/library/ubiq-report.pdf
* https://github.com/ethresearch/sharding-p2p-poc
* https://www.ethhub.io/

# Attendees
* ♦ Ankit
* ♦ Akhila Raju (Pegasys)
* ♦ Christoph Burgdorf (py-evm)
* ♦ Kevin Mai-Hsuan (Chia)
* ♦ Jarrad Hope (Status)
* ♦ Blazj Kolad (Pegasys)
* ♦ Alex Stokes (Lighthouse/Sigma Prime)
* ♦ Lane Rettig (EF/eWASM)
* ♦ Terence (Prysmatic)
* ♦ Leo (BSC)
* ♦ Nicolas Gailly (Pegasys)
* ♦ Mikhail Kalinin (Harmony)
* ♦ Nicholas Lin (EF/Research)
* ♦ Nicolas Liochon (Pegasys)
* ♦ Nishant Das (Prysmatic)
* ♦ Prateek Reddy (EF/Research)
* ♦ Jonny Rhea (Pegasys)
* ♦ Vitalik Buterin (EF/Research)
* ♦ Joseph Delong (ConsenSys)
* ♦ Daniel Ellison (ConsenSys)
* ♦ Danny Ryan (EF/Research)
* ♦ Carl Beekhuizen (Decentralized staking pools)
* ♦ Olivier Begassat (ConsenSys)
* ♦ Raúl Jordan (Prysmatic)
* ♦ Justin Drake (EF/Research)
* ♦ Jannik Luhn (Brainbot/Research)
* ♦ Chih-Cheng Liang (EF/Research)
* ♦ Mamy Ratsimbazafy (Status/Nimbus)
* ♦ Hsiao-Wei Wang (EF/Research)
* ♦ Jacek Sieka (Status/Nimbus) 
* ♦ Ben Edgington (Pegasys)
* ♦ Peter Gallagher (Meeting Notes)
