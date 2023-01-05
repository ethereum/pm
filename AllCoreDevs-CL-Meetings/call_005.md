# Ethereum 2.0 Implementers Call 5 Notes
### Meeting Date/Time: Thu, Oct 11, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/11)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=cNLO3vyod-E)
 # Agenda
1. Client Updates
2. Research Updates
3. libp2p updates
4. Testing
5. [Alternative tree structure storage](https://github.com/ethereum/eth2.0-pm/issues/8#issuecomment-424849447)
6. v2.1 discussion
7. Open discussion/closing remarks

# Client Updates
* Pegasus (Ben & Blazej)  _(N/A)_
  * Network simulator, currently exploring behavior
  * Make BLS sig aggregate efficient (similar to Lighthouse and Status) but want to drop Milagro
  * Question on signature size:
     * V: sig G2 element to size
     * D: is it for BN128?
     * M: in Milagro sig is 4x48 bytes
     * V: checking (but on his phone) it's using the top part of...for parity
     * JD: def compress_G2 (pt)
      * Blazej and V: 0.2 ms pairing in Java, 10 ms in Python
      
* Harmony (Mikhail)  _2:45-4:09_
  * Working on state transtion logic and in middle of progress
  * Several small fixes that reflect latest spec change
  * Implemented multiple validator service that carries as much validators as JVM could hold 
    * Useful in terms of testing or benchmarking. So when less logic is implemented we can have a thousand validators and measure the time of signature aggregation, and proposing. This time won't inlcude network latency (but network latencies could be emulated)

* Lodestar (Mikerah)  _4:15-4:50_
  * Almost done their implementation of simple serialize (SSZ)
    * Testing to start soon and then packaged it a nom module 
    * Expected to be completed before DevCon
  * Going to start writing a simulation percent functions in the beacon chain spec to get a deeper understanding before continuing to implement
    
* Parity (Wei)  _4:55-6:51_
  * Building a shasper implementation using the substrate framework
    * So far have implemented the state transition 
    * Have a basic skeleton for the networking transaction pool 
      * Meant to be a general blockchain framework and there are some benefits. They don’t need to rewrite our block or backend storage so that is why it is slightly faster
    * Focusing on implementing some of the features in substrate that might be potential blockers for shasper 
      * Two things they have found:
        1. Blackbox consensus. They have not implemented the fork-choice rule, implemented according to the shasper spec. 
        2. Multiple state routes. Which they don’t need yet, but they will when they get the validator trie. 
  
* Lighthouse (Adrian)  _6:59-7:45_
  * Focusing on block processing and block pre-processing
  * Drafted the simple serialize (SSZ) spec
  * Built some YAML tests for shuffling that have not been released yet. 
  * Been looking into doing the networking side of their clients
    * Looking at gossipsub in Rust, and have started going down the path of implementing it into Rust next

* Prysmatic (Raul)  _7:47-9:35_
  * Did their PoC and demo release, where they allow a single validator the network simulator to advance the beacon chain based on seed conditions
    * They relaxed a few of the constraints and some parameters to allow for this to happen
  * Working on getting BLS integrated
    * Dealing with some issues on finding a good Go library that has permissioned licenses and has everything they need for BLS12-381
  * Currently implementing fork-choice rule 
    * Using the last finalized slot, the last justified slot, and current block slot as weighting factors in the scoring rule
    * In the meantime, while they wait for settling on the immediate message ghost, or LMD
      * Discussion ensued with Prismatic and Vitalik, and further thought on the matter is needed
      * [Implementation of latest message](https://github.com/ethereum/research/tree/master/clock_disparity) in the clock disparity folder of the research repo
        * Talked about how it was surprisingly more simple than immediate message ghost in certain ways
  * Going to be starting work on simple serialize (SSZ) very soon

* Nimbus (Mamy)  _9:43-13:48_
  * Implemented the sparse merkle trees (SMT) and benchmarks should be coming in the next couple of weeks
    * Was done by someone outside of Status, through the use of bounties 
    * [Sample implementation](https://github.com/ethereum/research/tree/master/trie_research/bintrie2) done by Vitalik for how to optimize them by basically layering hex patricia trees on top of them, so you get the same level of database efficiency.
  * Concerned about the fact that libp2p requires UNIX domain sockets. Which means that it only works on the latest Windows 10, and won’t work on Windows 8, for example. 
    * Will discuss with the libp2p team 
  * Hardened the simple serialize implementation with regards to alignment and made a proposition about padding
    * Hoping to get some kind of test format, so they can start working on a test generator and test all implementations
  * Hoping to give some constructive feedback when the design of EVM 2.0 is reached, as they had some lessons learned with 1.0 regarding signed and unsigned ints. 
  * Focus for the following weeks before Prague will be to create several benchmarks so when everyone from Status meets they can test the 2.0 on phones, routers, raspberry pi, etc.
  * As a side note: Status has been moving away from slack to a full whisper/status desktop. And Nimbus will be developing a Whisper/Gitter bridge to live completely on the blockchain 

# 2. Research Updates   
* Danny  _14:15–14:48_
    * On the spec, maintenance of it has primarily moved to the github, there’s been a lot of rapid development
      * A lot has been focus on making things clearer, making minor adjustments, renaming, reorganizing etc. 
      * Ben Edgington: [What's New in Eth2.0](https://docs.google.com/document/d/1yDoXocazwE0LRDTQbm2yGz_3MkIL0f32xQVRt1nTKig/edit)
 * Vitalik  _14:50–16:10_
    * On the spec side, something that may be worth dedicating more time to specifically is the possibility of replacing the hash algorithm with some kind of merkle hashing
     * Made an issue on this: [issue#54](https://github.com/ethereum/eth2.0-specs/issues/54)
       * Idea is that instead of hashing everything, you hash the object in a merkle tree, and the merkle tree hashing is done along the lines of the object syntax tree itself, as that makes things simpler in many ways
       * As part of that: Justin brought up that we would probably merge the crystallized state and the active state
 * Justin  _16:20–23:55_
   * On the randomness beacon, there was a nice improvement to RANDAO that was found. Basically about hardening RANDAO against all orphan reveals
      * (an orphan reveal being, when someone reveals their RANDAO commitment, but for some reason or another it doesn’t go on chain. Whether due to latency, active censorship, etc. )
      * Problem with orphan reveals is that when the revealer is invited to reveal the next time, everyone already knows what they are going to reveal. So it is as if they had already skipped their slot. 
      * Solution: Count the number of times that a revealer was invited to reveal, but no proposal made it to the canonical chain. And then when the revealer does eventually reveal, then they reveal n+1 layers deep (where n is the number of times that they didn’t reveal on chain)
   * Filecoin has confirmed that they are collaborating with us on 50/50 on the financial side for the various studies being done with regards to the VDF
     *	Three studies that are being looked in to. Starting with analog performance study
        * Seeing how much performance can be squeezed by designing custom cells at the transistor level
     * There has been some progress on the state of the art modular squaring circuits
     * Working in conjunction with the team in China, the team over there got a reduction from 7 nanoseconds down to 5.7 nanoseconds - for a 20% improvement
   * Discussion ensued about how we would organize the circuit competitions. 
      * Do we want to invite anyone in the world to some sort of circuit competition to find the fastest circuit? There would be a large bounty for such a competition. And one complication is figuring out which cell library to use for benchmarking all the various circuits
       * Generally the cell libraries have a lot of IP protections, and the vendors are not very keen to working with open source projects
       * There is a 7 nanometer predictive PDK, called ASAP 7, which has been developed by academics and which is open source. Talks have begun to use it for the competition if possible. 
   * In terms of the spec, more time will gradually be spent on the spec by Justin. And he talked about how the pace of change to the spec will continue to change, and maybe even accelerate, in the near future - potentially all the way to the end of 2018
     * Lots of detail that needs to be written down, and the existing detail also has to be tested. Also some not so insignificant changes, like merging the crystallized state and the active state
      * Justin created a to-do list as well: With one of his goals outside of the content of the spec being the presentation and the readability of the spec. Perhaps maybe writing something similar to what he wrote in ethresearch for what was called “Phase 1”, where there are lots of clear definitions and the presentation is polished.
    * Unknown/Justin _22:00–23:45_ Talk with someone and Justin regarding the time it takes to do some squaring operations. And was wondering if that was done with a specific field in mind, and if there was any kind of theoretical advance or if it was just an optimization that happened?
     * While Justin didn’t have much visibility in terms of how the team in China improved the latency, he imagined it was all optimizations. He talked about how, one of the things that these hardware multipliers have are large reduction trees. And you can try and be clever in the way you organize the cells into what he calls “compressor modules” and then how you arrange your compressor modules to reduce the critical path of the circuit. And he imagined they had some optimizations for that.
     * The specific group being worked in is an RSA group. A 2000 bit modulus, and they’re just doing squaring in that root. Modular squaring whether the modulus is fixed and has size 2048 bits
 * Kevin  _23:55–24:40_
    * Merged with Python and Go logics
    * More actively testing the p2pdaemon and working on the Python bindings for it
 * Danny  _24:41–25:00_
    * Forgot to mention in client updates the fact that Hsiao-Wei has been porting a lot of the Python PoC stuff into PyEVM to start working on a more production Python implementation

# 3. libp2p updates
* Raul (Danny speaking in place of)  _25:01-26:20_
* Notes from Raul: From the [agenda](https://github.com/ethereum/eth2.0-pm/issues/11)

  * libp2p daemon/binding interface spec. 
    * We have approved and merged an initial spec for the libp2p daemon \o/
  * Reference Go binding implementation. 
    * We have developed a Go binding implementation. It adheres to the above spec, and is in continuous evolution. We'd love your feedback!
  * Supporting binding development. 
    * When are Eth2.0 teams planning to start work on Python, Nim, Java bindings for the libp2p daemon? Would love to get ballparks so we can line up support.
  * DHT support now merged in the daemon \o/
    * We use the libp2p/ipfs bootstrap peers by default, but you can pass a different set through CLI options.
  * Spec review and update. 
    * Some of us libp2p folks are huddling up this week to review the specs and bring them up to speed with implementations. Watch pull requests on the [libp2p specs repo](https://github.com/libp2p/specs/pulls)
  * Mike Goelzer and I will be attending the Eth2.0 meetup on Oct 29th in Prague.
  
# 4. Testing
  * Danny  _26:26–28:30_ 
    * Efforts to define a general format for testing using YAML
      * Opened up a can of worms into how you actually structure those tests and where this test lives in the format of those tests
      * Further discussion need needed, consensus being to continue talks in Prague. 
    * Mamy/Danny _27:20–28:25_ Talks with unknown and Danny regarding this general format for testing. Discussed possibly the best way forward is to start on a small scope, using it for SSZ and maybe the shuffling algorithm. 
      * Further discussion on the subject to be had 
      
# 5. Alternative tree storage structures
* Alexey  _28:40–34:30_  
*	https://github.com/ethereum/eth2.0-pm/issues/8#issuecomment-424849447

*	Reviewed what Vitalik had posted, and was aware of this optimization before. And thought about using the different types of trees for actually storing things in a database, and this is where his current research is going.
* While working on TurboGeth, and trying to see where the sub optimality of the trade-offs go between update efficiency of the storage, efficiency in accessing the storage, and the storage efficiency in terms of the size of the database. 
  * Starting to believe we are very far from the optimal set of trade-offs in terms of how we have done things so far. Some of it having to do with the choice of the databases being used, etc.
  * Idea currently being done as a PoC (hoping to finish in 2-3 weeks time) is to fuse together the key value database with the temporal elements so that you can store the history. Something he noted that lacking with TurboGeth in terms of efficiency. 
  * With the native support for some sort of tree hashing algorithms, and also with the ease of pruning there are 4 stages of this proof-of-concept. Currently on Stage 2:
    * _Stage 1_: Implement weight balance trees with tight as possible balance parameters and make it non recursive so there’s efficient bulk updates (done already) 
    * _Stage 2_: If you take these binary search trees and start grouping the sub trees (like little fragments, as Vitalik had described it in his article) together so that they fit on the page (4kb page, efficiency of storage). And you then use some sort of page split & merge operations in order to maintain this page size. So at the end of the stage, hoping to see what kind of storage efficiency there is, and efficiency when you mutate this page tree. And this would be used to pretend that we are mutating the Ethereum state from the mainnet, for example. 
    * _Stage 3_: Maintaining the prunable history of changes. Which basically introduces a temporal element to it, so that not only the tree of the current state will be stored, but also the history. (lesson learned from TurboGeth is that when you store the history in such a way that you record the updates relative to the past, then it becomes really difficult to prune such a structure. But once you start recording the updates the other way, so that you always record the reverse diff from the current. So therefore, your past records are always referencing the future records, so the pruning becomes a pretty trivial thing.) Hope to finish Stage 3 in a couple weeks time.
    *	_Stage 4_: Similar to Vitalik’s idea, regarding the embedding of the different tree hashing algorithm into the database. So you can use the Patricia tress, or the Sparse Merkle Trees, or AVL trees (maybe) in the same place as the weight balanced trees (WBT) that Alexey is using at the moment. You try to record one hash per page to assist in computing hashes. Which is currently what TurboGeth is lacking. 
  *	Once the PoC is completed and we have the numbers, we will know whether this whole set of ideas works or not. And hope that further discussion of it can be done in more detail. 

  * Talks ensued regarding what kind of changes will be proposed if the proof-of-concept is complete and we are happy with the numbers. If that happens, one of the outcomes of Stage 4, which is essentially how you can graph the different types of trees onto the WBT. Alexey would want to measure the overhead that we were going to get, so that essentially the systems that will be based natively on these WBT will be the most efficient by using the storage, but the systems that will use different hashing algorithms will pay some overhead. So Alexey will hopefully be able to tell what kind of level this is going to be. If it is reasonably large, a suggestion could be proposed to consider using the WBT trees instead of the Sparse Merkle Trees. 
    *	While yes, there are all these optimizations that can be done in a SMT, the main complaint is that in order to maintain the balance of the tree in adversarial settings, you have to pre hash they keys. You basically have to randomize the key. Otherwise your attacker could create really long sibling nodes which will always have a very long merkle proofs. 
    *	So if your keys are randomized, then it’s not a problem. But as we see in the current Ethereum, we basically do double or triple hashing of everything (e.g. Solidity hashing the keys of the mappings and then you get these indices on the storage get hashed again before they are ensured on the Patricia Tree. And then you get another hashing which happens over the Patricia trees.) For performance reasons, less hashing would be optimal.
  *	_36:50–37:59_  Discussion between Vitalik and Alexey regarding the fact that key hashing may not be that big of a deal, given the fact that in any of these tree structures you needs to hash a huge number of times due to tree updates. Further clarification came from Alexey in that tree hashing is not only for performance, but also for convenience - as we have to keep the preimage database, and currently for archive nodes in Ethereum, preimage is about 16GB. 
    *	Further discussion to be had when the numbers come in during the next couple of weeks
    
# 6. v2.1 Discussion
* (Mikhael)  _38:55–44:12_
  *	Proposed the idea to store big structures, like the validator set, in a merkle tree and maybe in a PMT or SMT. And use, for example, the public key as a path in the tree. Discussion ensued and Vitalik responded by saying that one of the reasons why we did things with indices is because the validator set potentially large (could go up to a few hundred megabytes) and we wanted it to be maximally easy to just store the whole thing in RAM. So there is a worry that adding any more complex structures apart from just a simple list would lead to huge inefficiencies. 
  *	Is it really needed to store this big structure in RAM?
      *	Discussion ensued, and there was talk that the entire thing has to definitely be in RAM because the entire validator set gets updated every time there’s a recalculation. There doesn’t seem to be that much benefit to a data structure that makes it easier to change small pieces at a time because we are changing everything at once. 
      *	It is also needed in RAM because every time you’re pulling in an attestation you need to compute a group public key from the validators and you don’t know which validators you’re going to have to have before you get the attestation. 
  *	Will need to store all the structures in disk in case of restarts, we need to load them from somewhere. 
  *	Further thought on the matter will be needed. We need to keep the crystallized state in memory. And would any techniques that would make that infeasible would be a road that we would probably not want to go down. 
    *	With that being said, one might be taking snapshots of the state  every cycle or so and storing them in your database so that – at least since the last finalized state, you could probably prune beyond that. Storing the current in memory, but probably having references to snapshots of it in the database. 
*	Upon further discussion of crystallized states, Jacek asked if you could potentially have multiple crystallized states? _(45:30)_ 
    * With the answer being yes, you could receive two conflicting blocks that cause a state transition. One of which would be considered the head, and the other being a close second, creating two conflicting crystallized states, probably locally in your database, that you would only prune later once you’ve finalized which direction the chain would go in. 
    *	Maximum amount of validator shuffling that could happen per cycle/multiple of cycles is 1/32 (about 3%). So that amount of the validator set could change on a roughly per cycle basis. And then all of the different shuffling (currently being debated if we should keep the shuffling in state) can change on the order of every cycle. 
    *	The validator set is the largest component of the crystallized state, and therefore there is a generational aspect to the crystallized set as the validators themselves won’t change. All the other components of the crystallized state are smaller, and will fully change within the crystallized state often. 
*	_48:10_ Justin asked whether there are bounds on how much can change per slot (like 128, for example). In which case, wouldn’t it make sense to try and amortize the costs on a slot by slot basis instead of during a huge batched operation at the end which could be quite expensive? For updating balances, or if someone made an attestation could we then just reward them in the slot in which the attestation was made?
    *	Vitalik - The problem with that is that we would change 1/64 of the validators every time. And we would be doing something like 6x more hashing than right now, as we would have to update a bunch of extra merkle branches whereas now we would just reconstruct the entire tree. 
* (Blazj) _51:10–53:30_ Question about aggregation of signatures, and whether it’s just a question of taste – or does including a given signature multiple times introduce any kind of security problems. Would one prefer to have an aggregate signature which represents any given signature only once at most, or if there’s any security reduction/problem with including any given signature multiple times.
    * Vitalik _(52:05)_  Yes, it would be better taste, but if you start admitting that then the set of which keys are included have to turn into some weird data structure and could really reduce efficiency. 
    * Justin _(52:50)_  Don’t think there is any security implications. One possible compromise would be to replace the bit field with a 2 bit field  where every validator has 2 bits and their signature could be included at most three times. And that would keep the complexity and performance low and high, respectively. 
    * Danny _(53:22)_ Agreed, adding that the more bits you allow for a validator the more allowance you have for creating some multiple of complexity for calculating the group public key. Would prefer to see a reasonable solution that doesn’t have multiple representations for aggregate, but agrees that there might be some compromise there depending on the aggregation strategy off-line and some of the real world results around that. 
        * Need to further define what that aggregation strategy is on the network level as well. And until that happens, it may not be worth adding the complexity and the data structures.

# 7. Open Discussion/Closing Remarks
* Further discussion to be had off-line regarding if people will be available for the next Implementers Call, scheduled for 10/25/2018.

# Links shared during meeting
* https://github.com/ethereum/eth2.0-pm/issues/8#issuecomment-424849447
* https://docs.google.com/document/d/1yDoXocazwE0LRDTQbm2yGz_3MkIL0f32xQVRt1nTKig/edit
* https://github.com/ethereum/eth2.0-pm/issues/11
* https://github.com/ethereum/research/tree/master/clock_disparity
* https://github.com/status-im/nim-eth-trie/blob/master/eth_trie/sparse_binary.nim
* https://ethresear.ch/t/optimizing-sparse-merkle-trees/3751
* https://github.com/ethereum/eth2.0-specs/pull/39
* https://github.com/ethereum/research/tree/master/trie_research/bintrie2
* https://github.com/ethereum/eth2.0-specs/issues/54
* https://github.com/libp2p/specs/pulls

# Attendees
* Lane Rettig (eWASM)
* George (Clearmatics)
* Vitalik Buterin (EF/Research)
* Alexey Akhunov (turbo-geth) 
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
* Afri (Parity)
* Jacek Sieka (Status/Nimbus)
* Prateek Reddy (EF/Research)
* Fredrick Harryson (Parity) 
* Dmitry (Harmony)
* Mikerah (ChainSafe)
* Wei Tang (Parity)
* Blazj Kolad (ConsenSys)
* Ben Edgington (ConsenSys)
* Olivier Begassat (ConsenSys)
* Raúl Jordan (prysmatic)
* Martin Holst Swende (EF/Researcher)
* Meeting notes by: Peter Gallagher
