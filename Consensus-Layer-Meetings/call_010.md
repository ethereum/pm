# Ethereum 2.0 Implementers Call 10 Notes

### Meeting Date/Time: Thursday 2019/1/17 at [14:00 GMT](https://savvytime.com/converter/gmt-to-germany-berlin-united-kingdom-london-ny-new-york-city-ca-san-francisco-china-shanghai-japan-tokyo-australia-sydney/jan-17-2019/2pm)
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/23)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=KZ9fms_PrQU)

# Agenda
1. Client Updates [_(12:13)_](https://youtu.be/KZ9fms_PrQU?t=733)
2. Research Updates [_(28:54)_](https://youtu.be/KZ9fms_PrQU?t=1734) 
3. [PoW -> PoS ether transfers](https://github.com/ethereum/eth2.0-pm/issues/23#issuecomment-453925393) [_(47:56)_](https://youtu.be/KZ9fms_PrQU?t=2876)
4. Test formats discussion [_(1:04:00)_](https://youtu.be/KZ9fms_PrQU?t=3840) 
   - [ssz](https://github.com/ethereum/eth2.0-tests/issues/8)
   - [tree hashing](https://github.com/ethereum/eth2.0-tests/issues/11)
5. Spec discussion [_(1:12:00)_](https://youtu.be/KZ9fms_PrQU?t=4321)
6. Open Discussion/Closing Remarks [_(1:27:48)_](https://youtu.be/KZ9fms_PrQU?t=5268)

# Client Updates
* Lighthouse - Paul Hauner [_(12:41)_](https://youtu.be/KZ9fms_PrQU?t=761)
  * Been implementing gRPC APIs in the spec
  * Started validator services. Focusing on the run-time in rpc
  * One of the security members on their team has been looking to start adapting the ETH1.0 C++ fuzzer. To try and point it at ETH2.0
  * Research team looking into how they can do hashing to G2 in Milagro
* Parity - Wei Tang [_(13:20)_](https://youtu.be/KZ9fms_PrQU?t=800)
  * LMD Ghost fork choice: [(Link)](https://github.com/paritytech/shasper/blob/609b8cd326c64d6735ad10d06671f13ebcba1f5a/consensus/src/block_import.rs#L146) (to be optimized)
  * Refactoring substrate to be able to invoke fork choice per slot
* Nimbus - Mamy [_(15:17)_](https://youtu.be/KZ9fms_PrQU?t=917)
  * Keeping in sync with latest changes
  * Focus on Documentation, CI and reproducible builds
  * BLS - scheme 4, copied Harmony approach, still unsure of spec compatability
     * Python test vectors this week
  * Fork choice rule implemented
  * Libp2p-daemon: wrapper is done (for unix)
     * waiting for the libp2p team to improve windows support
  * Next steps: Block storage + sync
* Harmony - Mikhail [_(17:11)_](https://youtu.be/KZ9fms_PrQU?t=1031)
  * Started to work on a reimplemented from scratch about a month ago
  * Previously were working in EthereumJ code base (licensed under LGPL)
      *but for the final client do not want this license
  * Implemented - BLS, SSZ, Consensus almost done
  * Next steps: fork choice rule, validator service, and PoW chain integration
  * [(Link)](https://github.com/harmony-dev/beacon-chain-java) to repository
* Pegasys - Joseph Delong [_(20:56)_](https://youtu.be/KZ9fms_PrQU?t=1256)
  * Added two more collaborators on the project
  * Defined the primitives from the spec
  * Implemented the slot processing logic that's detailed in the state of the spec
  * Started epoch processing and laid out scaffolding for libp2p interface
  * Shifted to microservices architecture, as it may be beneficial in the long term, with projects like Infura who want to house supernodes
  * Continuing talks with Harmony to potentially combine efforts in the Java client
* ChainSafe / Lodestar - Greg Markou [_(22:04)_](https://youtu.be/KZ9fms_PrQU?t=1324)
  * Spending time architecting and working on supplementary repos, like ssz and bls
  * Will update to latest specs only once every 2 week, as changes are very frequent 
* Py-EVM - Hsiao-Wei [_(23:22)_](https://youtu.be/KZ9fms_PrQU?t=1402)
  * Moved beacon chain out of py-evm repo and into Trinity for time being for ease of development https://github.com/ethereum/trinity/tree/master/eth2
  * tree hashing and py ssz refactoring done
  * Discussing test formats, proposed by Jannik, later after client updates
* Prysmatic - Raúl [_(24:21)_](https://youtu.be/KZ9fms_PrQU?t=1461)
  * Finished block processing
  * Listener that starts beacon chain processing
  * Use of Vyper contract
  * Started on LMD Ghost fork choice rule - slow to choose a new head, will be optimized
  * Removed shard committee
  * YAML test for state transition: https://github.com/prysmaticlabs/prysm/tree/master/beacon-chain/chaintest
* Swift Implementation - Dean Eigenmann [_(26:40)_](https://youtu.be/KZ9fms_PrQU?t=1600)
  * Started implementing spec in Swift. Done with most of the helper functions
  * Next steps: Implement ssz, bls, and then start working on the fork choice rule
  
# Introduction
* Stan Drozd, new at Lighthouse
* Christoph Burgdorf, Trinity

# 2. Research Updates  
* Vitalik [_(28:54)_](https://youtu.be/KZ9fms_PrQU?t=1734) 
    * Focus on LMD Ghost improvements 
    * Looking forward to client implementation feedback on fork choice speed and state transition speed
    * Light client proposal - https://github.com/ethereum/eth2.0-specs/issues/459 
        * looking forward to get some thoughts and review on this
* Justin Drake [_(31:49)_](https://youtu.be/KZ9fms_PrQU?t=1909)
    * In terms of logistics of the github repo, going to try and move things a little bit faster. So close down all the issues that have been addressed or that are stale. Try and move fast on the PR.
    * One thing that might be a good idea is avoid working directly on Master (e.g. proof-of-concept releases that are spaced out by six weeks) and then we work on some sort of scratch pad.
        * specs will have “releases” with a level branch and release tag
    * A lot of progress with VDFs. Moving forward with Filecoin on some of the studies. There will be a VDF day of Feb. 3, and various other VDF activities on Feb. 4 & 5th. 
        * hoping to write an update communicating all of the progress that has been made sometime in February.
* Pegasys - Nicolas Liochon [_(34:53)_](https://youtu.be/KZ9fms_PrQU?t=2093)
    * Still working on signature aggregation
    * Received the Amazon nodes and have started testing. Hoping to have results in the next two weeks.
        * testing the aggregation of thousands of bls signatures
        * on the simulation it works, and they've done an implementation in Go, but going to be testing in 3,000 nodes.         
* Barcelona Supercomputing Center - Leo [_(35:47)_](https://youtu.be/KZ9fms_PrQU?t=2147)
    * Been working on a way to visualize different results of the simulations [(Link)](http://leobago.com/static/shardsim/net.png)
    * Simulates 64 nodes
    * repo: https://github.com/leobago/shardSim    
*  Q&A Research
    * Terence: [_(42:15)_](https://youtu.be/KZ9fms_PrQU?t=2535) CBC trickling down to Phase 0? Vitalik: no
    * Justin: [_(44:05)_](https://youtu.be/KZ9fms_PrQU?t=2645) Reddit AMA coming soon
    * Raul: [_(44:34)_](https://youtu.be/KZ9fms_PrQU?t=2674) optimisations on fork choice
        * Vitalik: One of the largest optimisations is that, instead of treating every single validator as a separate unit, you would store a list of the most recent block hash that every validator voted for. But when you calculate the fork choice rule, you would treat everyone who voted for a particular block hash as a single block. This reduces the number of units you have to worry about. There's also some small tweaks in terms of how you actually calculate the Ghost fork choice rule. There's this binary search mechanism for finding the most recent block that still has over 50% support.  
    * Mamy: [_(46:33)_](https://youtu.be/KZ9fms_PrQU?t=2793) Fenwick Tree/Binary Index Tree [(more information)](https://en.wikipedia.org/wiki/Fenwick_tree)
        * Doesn't track by validator, but by committee
# 3. [PoW -> PoS ether transfers](https://github.com/ethereum/eth2.0-pm/issues/23#issuecomment-453925393)
* Alexey [48:19](https://youtu.be/KZ9fms_PrQU?t=2899) - Presents initial thoughts on how to improve the state of things, with the first being the finality gadget on the PoW chain. Is it going to be possible, and how soon will it be possible after the introduction of the beacon chain? 
    * Second point brought up is the tapering the PoW rewards. How are we going to stop the PoW rewards, inflating the supply in Ethereum2.0? Because it could sort itself out to be some sort of competition between miners in PoW and validators in PoS. Suggestion so far is to implement a finality gadget, then it's possible to tie the mining reward with the remaining ether supply on the PoW chain. Since the PoW client will have to start watching the beacon chain to start implementing the gadget, they could also request information on what supply levels are on the PoW chain. 
    * Third, Alexey was thinking about uneven distribution of validators in Eth2.0. And people depositing their amounts in the new chain, and not necessarily leaving room for others in. The current spec is designed that they have to vote on the PoW block. But what if they don't vote, is there any penalty for them? One of the ideas Alexey had is to tie the validator reward in PoS with the fact that they're actually letting people in.  
    * Lastly, Alexey brought up censorship resistance of deposits. If the miners aren't friendly in the future then they might prevent the PoS launch. There's still a few details left to be figured out, but Alexey talks about his proposal for perfect censorship of deposits. This idea allows the individual depositors to prevent a reorg attack as well, as they can wait until an efficient time to reveal their deposit to the beacon chain so that they can prevent these attacks. 
* Further discussion to be had. Danny to put on the agenda for next meeting. 
# 4. Test formats discussion
* Jannik has two new YAML test formats [1:04:30](https://youtu.be/KZ9fms_PrQU?t=3870)
    * [ssz](https://github.com/ethereum/eth2.0-tests/issues/8) has three kinds of tests. The first one where everything is valid, the type of thing we want to serialize, the value, and then the serialized value in pipes and x string. We also test values that have been serialized invalidly. (e.g. strings that are too long or too short). They do not specificy the value, but only the string and shard description of why that is wrong. Types (if possible) is specified by strings. For lists, they are specified as a YAML list w/ a single element that specifies the element of the list. Containers are used via YAML mappings (should not be a problem as we do not care about order of fields).
    * [tree hashing](https://github.com/ethereum/eth2.0-tests/issues/11) same value definitions, added the tree hash of the value. 
* Danny asked a question regarding the difference between the correct serialized value vs. the invalid value? To which Jannik responded by saying the difference is the direction. One has a value we can't serialize because we can't match the type, and the other way around is - you get the serialized string and you can't deserialize it properly. Essentially, one has the ssz provider and one has the value provider.
* Stan Drozd also asked that, in the first scenario, where everything is valid. We are going to want to include some sneaky edge cases. Maybe it would be valuable to include a description in there as well, so the developer can focus on what is hard to get in a particular case? Jannik responded, saying one thing he thinks could be valuable is that the description is almost always the same (or some kind of tag) because this way we can recognize some types of edge cases. 
    * In the general format, the description is optional for all test cases. Mamy suggested having some kind of formal tag. Because, for example, in Ethereum1.0 we had a lot of overflow tests, but no tags for overflow. 
# 5. General spec discussions
* Terence [1:12:20](https://youtu.be/KZ9fms_PrQU?t=4340) wanted to give a shout-out to Danny to working on the validator spec. And it has been very helpful on the implementation side. Still a PR, but the bones are in place. 
* Justin: adding a list of suggested implementations for implementers could be a good idea in the future as well, once the spec matures.
* Wei Tang brought up the issue of, when we prefixed the length on the container in list types, we made it difficult to stream. Mikhail discussed that the main argument in favor of prefixing was that the serialization format is going to be used over the network. And for network related things, it's important to know how big the object is going to be. 
    * Alexey also chimed in, saying that with the problem Wei had described, if you try to use it for hashing you have to reallocate the memory. 
        * Alexey also agrees that, if this format is going to be wrapped into the other packages (e.g. libp2p) then that packaging would add necessary prefixes so you don't need to design ssz for that purpose. So, that means you'd need to optimize it for something else. If it's going to be used as an input for hashing then it may not be wise to use prefixes. 
* Danny discussed PR #139 [(Link)](https://github.com/ethereum/eth2.0-specs/pull/139) that recently just improved. Generally, the arguments laid out favored slightly in the direction of little-endian. It also helps substrate, because they only support little-endian right now. 
    * Consensus was made to merge the PR after the call
# 6. Open Discussion/Closing Remarks
* ETHDenver coming up in the middle of February. As of now, no specific event is being coordinated, but many are planning to meet.
# Links shared during meeting
* https://github.com/ethereum/eth2.0-pm/issues/23
* https://github.com/harmony-dev/beacon-chain-java
* https://github.com/paritytech/shasper/blob/609b8cd326c64d6735ad10d06671f13ebcba1f5a/consensus/src/block_import.rs#L146
* https://github.com/ethereum/trinity/tree/master/eth2
* https://github.com/prysmaticlabs/prysm/tree/master/beacon-chain/chaintest
* https://github.com/yeeth/BeaconChain.swift
* https://github.com/ethereum/research/blob/master/ghost/ghost.py
* https://github.com/prysmaticlabs/prysm/tree/master/beacon-chain/chaintest
* https://github.com/prysmaticlabs/prysm/pull/1310/files
* https://github.com/ethereum/eth2.0-specs/issues/459
* https://github.com/leobago/shardSim
* https://bit.ly/2RNL7nx
* leobago.com/static/shardsim/net.png
* https://en.wikipedia.org/wiki/Fenwick_tree
* https://github.com/ethereum/eth2.0-tests/issues/8
* https://github.com/ethereum/eth2.0-specs/pull/139

# Attendees
* Dmitrii (Harmony)
* Jonny Rhea (Pegasys)
* Alex Stokes (Lighthouse/Sigma Prime)
* Mikhail Kalinin (Harmony)
* Akhila Raju (Pegasys)
* Christoph Burgdorf (py-evm)
* Greg Markou (ChainSafe)
* Nicholas Lin (EF/Research)
* Daniel Ellison (ConsenSys)
* Dean Eigenmann (ENS/ZK Labs/Harbour Project)
* Mikerah (ChainSafe)
* Alexey Akhunov (turbo-geth)
* Ameen Soleimani (SpankChain)
* Fredrik Harrysson (Parity)
* Kevin Mai-Hsuan (Chia)
* Adrian Manning (Lighthouse/Sigma Prime)
* Jannik Luhn (Brainbot/Research)
* Paul Hauner (Lighthouse/Sigma Prime)
* Blazj Kolad (Pegasys)
* Terence (Prysmatic)
* Vitalik Buterin (EF/Research)
* Wei Tang (Parity)
* Leo (BSC)
* Nicolas Gailly (Pegasys)
* Stanislaw Drozd (Lighthouse/Sigma Prime)
* Nishant Das (Prysmatic)
* Steven Schroeder (PegaSys)
* Joseph Delong (ConsenSys)
* Danny Ryan (EF/Research)
* Carl Beekhuizen (Decentralized staking pools)
* Olivier Begassat (ConsenSys)
* Raúl Jordan (Prysmatic)
* Justin Drake (EF/Research)
* Chih-Cheng Liang (EF/Research)
* Mamy Ratsimbazafy (Status/Nimbus)
* Hsiao-Wei Wang (EF/Research)
* Ben Edgington (Pegasys)
* Peter Gallagher (Meeting Notes)
