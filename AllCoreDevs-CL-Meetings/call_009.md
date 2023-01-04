# Ethereum 2.0 Implementers Call 9 Notes
### Meeting Date/Time: Thursday 2019/1/3 at [14:00 GMT](https://savvytime.com/converter/gmt-to-germany-berlin-united-kingdom-london-ny-new-york-city-ca-san-francisco-china-shanghai-japan-tokyo-australia-sydney/jan-3-2019/2pm)
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/21)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=6trA-5rjZUQ)

# Agenda
1. Client Updates [_(6:19)_](https://youtu.be/6trA-5rjZUQ?t=379)
2. Research Updates [_(17:56)_](https://youtu.be/6trA-5rjZUQ?t=1076) 
3. General spec discussion [_(47:58)_](https://youtu.be/6trA-5rjZUQ?t=2878)
4. Open Discussion/Closing Remarks [_(1:10:51)_](https://youtu.be/6trA-5rjZUQ?t=4251)

# Client Updates
* Lodestar - Greg Markou [_(6:21)_](https://youtu.be/6trA-5rjZUQ?t=381)
  * Started building out PoW chain deposit contract  
    * collecting deposits up to the chain start event
    * looking to start genesis and slot0
  * Finished up fixed size number library (few tweaks left to fix in test cases)
    * going to be importing uints and ints into the beacon chain end of this week/early next week
    * allowing to be close to spec as they can, especially with types
    * [_(Link)_](https://github.com/ChainSafeSystems/fixed-sized-numbers-ts/)
  * Outside of ChainSafe, have got some outside contributors who are pretty active as well. Which is cool
  * Have been working on bls a bit more as well
* Nimbus - Mamy [_(9:03)_](https://youtu.be/6trA-5rjZUQ?t=543)
  * In sync with latest spec changes
  * State simulator, we can transition between states, 1 epoch/second, next step is fork choice rule
  * Network simulation working, works real-time, next step is persistence
  * Testgen repo has been moved to eth2.0-tests
  * Now offering a Vagrant container and tutorial to setup the Nim ethereum 2.0 ecosystem on your Windows or Linux machine: [_(Link)_](https://our.status.im/setting-up-a-local-vagrant-environment-for-nim-development/)
  * December development updates: [_(Link)_](https://our.status.im/nimbus-development-update-2018-12-2/)
* Py-EVM - Hsiao-Wei Wang [_(11:20)_](https://youtu.be/6trA-5rjZUQ?t=680)
  * Syncing with the specs, next week: tree hashing + documentation
* Pegasys - Joseph Delong [_(12:19)_](https://youtu.be/6trA-5rjZUQ?t=680)
  * Open-sourced Artemis and started getting some contributors
  * Opened up a Gitter channel to bridge communication: [_(Link)_](https://gitter.im/PegaSysEng/artemis)
  * Completed vrc interface for Artemis
  * Starting work on jRPC and bls verification and hash tree root
     * opened a minor PR that was closed and merged (#351) that was a minor modification to the validator relay contract
  * Ben's What's New in ETH2 from Dec. 28: [_(Link)_](https://notes.ethereum.org/c/Sk8Zs--CQ/https%3A%2F%2Fbenjaminion.xyz%2Fnewineth2%2F20181228.html)
* Prysmatic - Terence [_(14:13)_](https://youtu.be/6trA-5rjZUQ?t=853)
  * Implemented about 90% of block processing and beacon processing functions
  * Also finished implementing function to process the validator deposits
  * SSZ and tree hashing algorithm done
  * Working on state simulator backend 
* Sigma Prime / Lighthouse - Paul Hauner [_(15:14)_](https://youtu.be/6trA-5rjZUQ?t=914)
  * Working on sync, waiting for some test vectors 
* Harmony - n/a [_(16:02)_](https://youtu.be/6trA-5rjZUQ?t=962)
  * Excused due to holidays
* Parity - Fredrik Harrysson [_(16:22)_](https://youtu.be/6trA-5rjZUQ?t=982)
  * Working through the holidays making progress on beacon chain implementation in Substrate
  * Participation in the proposal to switch serialisation to Little-Endian [(Link)](https://github.com/ethereum/eth2.0-specs/pull/139)
# 2. Research Updates  
* Justin Drake [_(18:05)_](https://youtu.be/6trA-5rjZUQ?t=1083)
    * Still finding bugs and fixing them. Which is nice
    * Trying to simplify the spec where possible
       * simplification of the validator status code logic -- used to have somewhat complicated state machine w/ various validator status codes and they were all sorts of edge cases when you would do transitions. That's mostly gone now, and has been replaced with timestamps in the validator records. Still have some "status flags" but there are only two.
       * looking to move towards this idea of locally computable shuffling. What we have now with the [Fischer-Yates logic](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle) is that in calculating the shuffling of a specific validator or specific committee it scales linearly with the size of the validator pool. We want this to scale better. Once we have this locally computable shuffling, it means we can be light client friendly w/o all sorts of light client specific infrastructure. 
           * this means that we can also simplify the beacon state. (specifically "shard-committees-at-slots" data structure and "persistent-committee-reassignments") This was infrastructure for light clients. But now that we have more information about the validators w/ these timestamps and looking to have this locally computable shuffling, we can remove those.
       * looking to potentially remove the validator registry delta chain, and rely on the double-batched merkle log accumulator that was added recently ([_Link_](https://ethresear.ch/t/double-batched-merkle-log-accumulator/571) to JD's original ethresearch post from January '18)
       * trying to push for a clean separation between phase0 and phase1&2 so a few bits a pieces of logic and constants have been removed
       * trying to push for cleanups of the spec as well. But will take some time, and expecting to have a nice and clean spec by the end of January
    * Question was asked regarding phase0 and phase 1. Seeing things, such as placeholders, being added to phase1. From a spec implementation point of view, this likely complicates things. And if we are going to do phase1 sometime after phase0 we would have learned many lessons and want further changes. So, as a general approach, wouldn't it be better to focus on upgradeability and making sure upgradeability of the protocol is solidm and leave the phase1 stuff out?
       * further discussion ensued to address this, specifically with stubbing the data structures in terms of messages that are passed around and gossiped, as well as the structure of the beacon state. The idea there is that once we do the upgrade, we don't have to fiddle with that and add special cases. Also, beyond these placeholders, we are also trying to avoid any logic other than for phase0.
       * Danny added that there's a balance between trying to figure out what the future holds and trying to reduce the amount of spaghetti code that will be in these clients. You don't really get the chance to get rid of logic and get rid of old code as you upgrade a blockchain. So it's a bit different than creating most systems. So if we know something is going to be there, perhaps it should be embedded in the data structure. But maybe we can also make a more informed decision in February.
       * There was further talk that if, before we launch the phase0 beacon chain, we have what looks like beginnings of a robust phase1 spec - then perhaps we should put the data structures in there along with the components of the data structures in there. But if it seems like a major unknown, then perhaps we should just pull it out. 
* PegaSys - Ben Edgington [_(26:09)_](https://youtu.be/6trA-5rjZUQ?t=1569)
    * Main focus in on the Stanford Blockchain Conference where they are presenting a paper on bls signature aggregation
    * Something to share ahead of the conference should be coming in the upcoming weeks.
    * So far only ran large scale experiment on the simulator Wittgenstein: https://github.com/ConsenSys/wittgenstein
    * Planning on running large scale experiment next week. Development is in pretty good shape, and experimentation phase is up next.
        * going to try to run on 4,000-5,000 nodes
* BSC - Leo [_(28:06)_](https://youtu.be/6trA-5rjZUQ?t=1686)
    * Have open sourced the simulators, and currently available on Github
    * Planning to tackle two questions:
        * 1.) How slow different shards will evolve in the case of having a low number of validators? (around stability of fork choice rule)
        * 2.) Relationship between consumed gas in the blocks and the uncle rate. Paper was written on this, but it's a couple of years old.                
* Libp2p - Raúl [_(34:18)_](https://youtu.be/6trA-5rjZUQ?t=2058)
    * Wanted to say thanks for feedback given on the roadmap ([Link](https://docs.google.com/document/d/1Rd4yNw1TNQBvfRrKeEMSTseb6fvPzS-C--obOn0nul8/edit#heading=h.3p8vr9ix3es9))
    * Libp2p team will be meeting in two weeks time to finalize roadmap discussions. Open and public for everyone to attend
    * Finished goal setting for Q1 2019 for libp2p project (particularly for the Go and js implementation)
    * Other key topics focusing on are multi-string 2.0 to reduce the latency of establishing connections and leverage certain functionalities of new transports that they're introducing, like QUIC, which allows for zero round trip negotiation.
        * also going to be working on a plan which they're calling DHT 2.0 - which introduces a number of new functionalities such as overlay DHT's, privacy, secrecy, and other features
        * focusing on interoperability testing and visualization tools
        * starting to discuss packet switching with a bit more depth than what they've done in the past
    * On the Py-Libp2p front, they are waiting on the grant resolution to move the project to the Libp2p organization. Looking like that is going to be picking up some more speed in January as well
    * Usage of gx as a package manager has been a bit of a pain point for downstream adopters, and they are going to be evaluating go.mod in general and even replacing gx if go.mod allows them to bring in some features, such as content addressability and so forth.
    * Provided a follow-up on conversation had in the last call regarding the native bindings for the libp2p daemon. Been working with PegaSys to support compliling native libraries w/ bridges to other languages
        * one of the use cases being targeted is embedding the libp2p daemon in environments such as IOS 
           * also talked about how somebody from Status suggested that having a deployable form of libp2p for IOS environments, in particularly the libp2p daemon, would be useful as a first experiment of running libp2p in IOS applications - basically the idea they came up with, was now that we have a daemon and the daemon is exposing local endpoints over IPC and apparently IOS supports IPC in UNIX domain sockets, then creating a native implementation of the libp2p daemon that compiles down into a native library that can then be deployed onto an IOS environment would be useful as a first experiment.
           * idea is to find a form such that an IOS app can start the daemon and interact with it over UNIX domain sockets, inside the operating system itself
           * possible problems were raised about having some trouble with UNIX sockets on IOS -- libp2p team is open to suggestions
    * One of the focuses for the next year is going to be mobile adoption - as it's important for a lot of offline use cases for libp2p. Expects at some point to be seeking a Swift native implementation of libp2p
        * problem with current model of deployment of the libp2p daemon is that it's basically a binary, and we can't run a binary in IOS just as is. So, by compiling it down to a native library, this would enable one to interact with the daemon, to start to the daemon as a library inside one's IOS app and interact with it over IPC or TCP local endpoints, etc.
        * further discussion between Status team and libp2p team to be had
* discv5 - Felix [_(44:12)_](https://youtu.be/6trA-5rjZUQ?t=2652)
    * Effort on discv5 is comprised of two parts:
        * 1.) Frank was put on the wire protocol, and is taking care of getting a preliminary spec in place
        * 2.) When it comes to the topics, not much has changed. Still at the point where Felix is trying to run the simulations that Jannik did
# 3. General spec discussions
* Mikerah asked a question regarding the running of beacon nodes (& incentives for running them)
    * active issue regarding that in the spec. Some concerns that Bruno brought up in the previous call, in which we would have to design the validator clients in a particular way in order to preserve privacy. 
    * Further talks ensued around the incentives to run a beacon node. Danny added that one incentive would be that a validator has a direct connection to the netowrk to get the state of the world and to sign messages and seek profit. Another might be that one has some sort of service that provides information of the state of the world to others (either altruistically for free, or in some paid model). Another reason to run one of these nodes is because you may be running an application (block explorer for example). Similar to why one runs a current PoW node, one small set of people doing that is for mining and the rest are either altruistic actors in the network or people who have applications etc. The beacon chain is the core system level stuff needed to sync the application chains/shard chains - so that's a core piece of infrastructure. And then one syncs whatever chains are relevant to one's needs, whether they're a validator or a block explorer application, or any other application that may need to sync one of these chains.
    * [Link](https://github.com/ethereum/eth2.0-specs/issues/157) to issue: #157
* Joseph Delong asked about issue #386 [(Link)](https://github.com/ethereum/eth2.0-specs/issues/386) and why are validator balances no longer part of ValidatorRecord?
    * [PR#317](https://github.com/ethereum/eth2.0-specs/pull/317) was the update that made the changes to that
    * Moving the validator balance into the beacon state is for hashing optimization, no? Is that language specific to python?
      * Discussion ensued, and Danny added that 1.) yes, moving the validator balance into the beacon state _is_ for hashing optimization. And 2.) no, it is not language specific to python. We used to have two states (active and crystallized). The active state was small and had to get re-hashed frequently. The crystallized state was very large and had to get re-hashed every epoch. We had the separation because we were using a flat hash and had no ability to cache the components of the state that had _not_ changed. When we moved to the ssz tree hash, we now have isolated the various components (array, objects) from each other, into this hash tree. _So_, when we update just the balance of one validator, in order to re-hash the data structure, most of the components of the tree remain stable and we have to a relatively low number of hashes in order to update. This was generally perceived as good and fine when we were using blake as the hash. However, when we switched to keccak256, we had a performance loss on hash computation time. Most of the validator record is _not_ updated frequently, but most of the validator _balances_ are being updated every epoch via the rewards and penalites. So, by moving the balances out, we've isolated the large component of what needs to be re-hashed into a smaller data structure. And so we're able to benefit from caching the hashes of the validator records a lot more, and isolate the amount of hashing that has to be done. All in an effort to reduce the increase in hash time when we moved from blake to keccak256.
      * This is also covered in Ben's issue of What's New in ETH2.0 
* Ben was curious about expected behavior of beacon chain block proposers?
    * As an exercise, Ben discussed how he went through how block proposers are supposed to deal with deposit receipts from the main chain.
    * Asked though, what exactly is the proposer supposed to be doing? Is there a plan for documentation where we spell out the details?
       * discussion ensued, and Danny described that what a validator does is implicit on what is considered _valid_ in the beacon chain. Also agreed on the fact that having an accompanying document on what an honest validator does would be a valuable addition to the spec repo. 
       * issue to be opened up for that
* Question was asked about the validator client architecture:
    * Question was that, in the spec, we have to validate that block-state-root is equal to the tree hash of the state. So, does that mean as a validator client, you would actually have to conmpute the state transition on the client side - and then attach it to the block? And then you issue the block to the beacon node?
       * Danny chimed in saying - no, that relation, the node is calculating that state root and providing it to the validator. The _providing_ essentially is a block proposal to sign. Similar to a PoW miner, the node provides a proposal that the PoW miner supposed to try and hash. So the heavy lifting should happen in the node. The main information that needs to pass along to the validator is enough information that the validator can decide if this is a _safe_ or a _dangerous_ message to sign. Strategies for the validator to assess the validity of the information, that is more of a trust relationship. And the validator should be asking multiple nodes perhaps. But, essentially, the signing entity should not be doing much of the heavy lifting. You wouldn't want to be passing the entire state to the validator. But instead, passing more of the block proposals to sign.
    * Raul from Prysmatic followed up with: We think that having the validator client rely upon the node for syncing shards and to not have it connected to the p2p network actually makes it harder to decouple the validator from a single node.
    * Danny: I think the opposite. I think it makes it much more difficult. The validator should be responsible for signing messages and remembering the relevant details of those messages to have the requisite information to continue to safely sign messages in the future. It can request this information from any nodes -- a nodes it runs, a set of nodes it runs, a node it runs and a public service node, etc. The validator then makes local decisions about what it should sign, store any information it needs to about these decisions so that it can make good decisions in the future, and then it passes these signed decisions along to any entity to broadcast them to the network. Once you start putting p2p requirements on a validator, you've increased the scope of this entity massively, and you've also directly connected a validator with signing keys to the internet and to potentially malicious peers. So even just from a security standpoint you've moved a validator out of a place of isolation and into a risky position. Back to the swapping, if the validator only asks questions about the state of the world then it becomes very easy to swap from whom the validator is asking these questions as long as there is a common interface for these requests. If we add p2p requirements, state processing requirements, etc, we actually just begin to build a node inside of a validator. If there are already robust node implementations, why rebuild these components in a separate place. And again, you cannot sync shard data without a constant connection to the beacon chain. If a validator were to sync shards directly, it would have to constantly be passing information between the beacon chain and the shard chains and would end up coming a core piece of communication infrastructure between these components. Beyond that, a node needs to be able to sync shards without a validator existing because there are many use cases of a node outside of validation.
*  Justin Drake discussed that he doesn't think a decision has been finalized on the endian-ness of ssz. Encouraged others to comment on the open pull request. 
    * Also commented on the honest behavior to add more clarity -- basically, step0 is just apply the validator rules on the various blocks that you've received and then you've got this block tree. So you have various forks. Then you apply the fork choice rule, so you get a single canonical blockchain. And now you're duty as an honest proposer is to build on top of the tip of this canonical chain. There's basically only two things needed to do from the point of view of deposit roots. 1.) You need to cast a vote for a deposit root from the Ethereum1.0 deposit contract. And the rule there is that we want to vote the latest one which is contained in the block, which has height 0 mod some power of 2. So, for example, every 1024 blocks on the Ethereum1.0 chain you're going to have a corresponding deposit root for whatever you consider the canonical Etherum1.0 chain. And then you just vote for that. And as soon as you have the required threshold of validators who have voted for that specific root (right now it is called it's called `processed_deposit_root`, but it will soon be called `latest_deposit_root`) _So_, right now you have this latest deposit root, and the second thing you need to do, 2.) Is to include deposit receipts from Ethereum1.0 into Ethereum2.0. You need to include them _in order_, you need to include up to 16 of them (specified in the `MAX_DEPOSITS` constant), and you need to include them up to the latest deposit root that has been voted upon.
    * Danny chimed in, adding that we are currently missing a validity condition on the ordering of those deposits. (will be added in the spec)
    * Complexities are there -- so worth spelling out in a document (especially as some knowledge is floating around, but not specifically stated anywhere. For example, the timing of when we're expected to do things w/ respect to a slot. We're expected to attest the head of a slot half-way through the slot, and not at the beginning.) There's going to be an increasing number of requirements for a validator as we move through phase1 and phase2 as well.    
# 4. Open Discussion/Closing Remarks
* Jacek pointed out that the Nimbus team will be congregating in Brussels just after FOSDEM (Feb.2-8) in case anyone wants to meet up and have a hack&chat.
* Future meetups looking to be around Q2 (April-May range) - at least on the EF side
# Links shared during meeting
* https://our.status.im/setting-up-a-local-vagrant-environment-for-nim-development/
* https://our.status.im/nimbus-development-update-2018-12-2/
* https://gitter.im/PegaSysEng/artemis
* https://github.com/ethereum/eth2.0-specs/issues/157
* https://docs.google.com/spreadsheets/d/11GKG1DBRIIAiQnHvLD7_IqWxDGsVdaZFpxJM6NWtXe8/edit?ts=5c178888#grid=0
* https://github.com/libp2p/go-libp2p-daemon/pull/28#issuecomment-449014187

# Attendees
* johns 
* Tomasz S (Pegasys)
* Akhila Raju (Pegasys)
* Greg Markou (ChainSafe)
* Felix Lange (IXDS)
* Mikerah (ChainSafe)
* Fredrik Harrysson (Parity)
* Kevin Mai-Hsuan (Chia)
* Adrian Manning (Lighthouse/Sigma Prime)
* Paul Hauner (Lighthouse/Sigma Prime)
* Raúl Kripalani (Protocol Labs)
* Blazj Kolad (Pegasys)
* Terence (Prysmatic)
* Leo (BSC)
* Nicolas Gailly (Pegasys)
* Stanislaw Drozd
* Nishant Das (Prysmatic)
* Joseph Delong (ConsenSys)
* Danny Ryan (EF/Research)
* Carl Beekhuizen (Decentralized staking pools)
* Olivier Begassat (ConsenSys)
* Raúl Jordan (Prysmatic)
* Justin Drake (EF/Research)
* Chih-Cheng Liang (EF/Research)
* Mamy Ratsimbazafy (Status/Nimbus)
* Hsiao-Wei Wang (EF/Research)
* Jacek Sieka (Status/Nimbus) 
* Ben Edgington (Pegasys)
* Peter Gallagher (Meeting Notes)
