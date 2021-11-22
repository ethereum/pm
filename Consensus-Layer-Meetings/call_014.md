# Ethereum 2.0 Implementers Call 14 Notes

### Meeting Date/Time: Thursday 2019/3/14 at [14:00 GMT](https://savvytime.com/converter/gmt-to-germany-berlin-united-kingdom-london-ny-new-york-city-ca-san-francisco-china-shanghai-japan-tokyo-australia-sydney/feb-14-2019/2pm)
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/33)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=zeceWlmxseY)

# Agenda
1. Testing Updates [_(6:56)_](https://youtu.be/zeceWlmxseY?t=416)
2. Client Updates [_(9:14)_](https://youtu.be/zeceWlmxseY?t=554)
3. Research Updates [_(44:03)_](https://youtu.be/zeceWlmxseY?t=2643) 
4. [quick update from raul/protocol labs](https://github.com/ethereum/eth2.0-pm/issues/33#issuecomment-472866505) [_(23:51)_](https://youtu.be/zeceWlmxseY?t=1431)
5. [lighthouse benchmarks update](https://github.com/ethereum/eth2.0-pm/issues/33#issuecomment-472857213) [_(24:29)_](https://youtu.be/zeceWlmxseY?t=1469)
6. [Leap seconds](https://github.com/ethereum/eth2.0-pm/issues/33#issuecomment-472029888) and time drift [_(30:56)_](https://youtu.be/zeceWlmxseY?t=1856)
7. [Network spec](https://github.com/ethereum/eth2.0-specs/pull/763) [_(1:03:44)_](https://youtu.be/zeceWlmxseY?t=3824) 
8. [serialization benchmarks](https://github.com/ethereum/eth2.0-pm/issues/33) [_(1:28:28)_](https://youtu.be/zeceWlmxseY?t=5308)
9. Spec discussion [_(1:34:52)_](https://youtu.be/zeceWlmxseY?t=5692)
10. Open Discussion/Closing Remarks [_(1:34:20)_](https://youtu.be/zeceWlmxseY?t=5660)

# 1. Testing Updates
* Python spec 0.5 is now fully executable. Now have some state tests against the executable spec, which will allow everyone to be able to run the same code soon. 
* Shuffling test updated to v0.4 and released. Shuffling algo has also not changed between v0.4 and v0.5, so that remains stable/
# 2. Client Updates
* Pegasys - Cem Ozer [_(9:18)_](https://youtu.be/zeceWlmxseY?t=558)
  * successfully integrated LMD Ghost to the state processors
  * currently can generate blocks which, in turn, the beacon nodes successfully can run state transitions on 
  * implemented a data provider inside the client to output information 
  * started profiling code to look at performance bottlenecks 
  * working with Zak from Whiteblock on getting a test net set up, and implementing the Hobbits wire protocol 
* Prysmatic - Terence [_(10:06)_](https://youtu.be/zeceWlmxseY?t=606)
  * mostly working on validator run time
  * https://medium.com/prysmatic-labs/ethereum-2-0-development-update-24-prysmatic-labs-6d081025d47
  * been leveraging prometheus and jaeger monitoring tools which allow us to track any metric we want from our nodes as well as look at what functions take up the longest in any section of our runtime
  * Implemented LMD Ghost fork
    * prelimindary benchmark results are documented [here](https://github.com/prysmaticlabs/prysm/pull/1950)
    * overall optimization improvement plan is being tracked [here](https://github.com/prysmaticlabs/prysm/issues/1951)
    * confident the fork choice will work in an 8 validator set up. In the meantime, need to optimize the fork choice as they scale up to 100,000's of validators.
  * finished updating code base to match the changes of new validator activiation and new validators can now get activated within Prysm 
  * been fixing up sync services so that the beacon node will be able to perform both regular sync and initial sync
    * major PRs tackled over the last few weeks have handled skipped slots in sync, syncing from the last finalized state over [here](https://github.com/prysmaticlabs/prysm/pull/1939) and [here](https://github.com/prysmaticlabs/prysm/pull/1955).
  * Upcoming work: complete end-to-end testing
  * Also, Ivan Martinez has joined as a core contributor
* Yeeth - Dean Eigenmann [_(11:29)_](https://youtu.be/zeceWlmxseY?t=689)
  * taken a break from working on the actual client
  * currently looking to implement libp2p in Swift in order to start working on networking
* Parity - Wei Tang [_(11:52)_](https://youtu.be/zeceWlmxseY?t=712)
  * mostly focusing on the testing 
  * still plan to do a lot of refactoring for the run time. But want to make sure that the refactoring is correct
* Lodestar - Greg Markou [_(13:37)_]
  * finished up state transitions, and going to start testing w/ a fake 1.01x deposit 
  * almost done getting libp2p done. Waiting on a few PR's
  * starting up a validator client 
* Harmony - Mikhail Kalinin [_(14:31)_](https://youtu.be/zeceWlmxseY?t=871)
  * working on a simulator and released its first version. Based on spec as is - w/ the only optimization is with the shuffling algo
    * not chaching the shuffling per epoch. Danny alluded that this could be one of biggest bottlenecks, but also one of the easiest things to resolve at this point.
  * simulator works well with 100's of validators, but with 1000's it become increasingly slow
  * next step would be to work with ~50,000 validators and do some benchmarks on these large figures. Still a work in progress
  * doing benchmarks on smaller sets of validators, several bottlenecks were found. These had nothing to do with the spec though, and were subsequently fixed
  * for those interested in trying out the simulator: [Link](https://github.com/harmony-dev/beacon-chain-java/releases/tag/v0.1.0)
* Lighthouse - Paul Hauner [_(16:39)_](https://youtu.be/zeceWlmxseY?t=999)
  * been building out run time. Working on syncing. Trying to get the phase 0 wire protocol in
  * been doing a lot of bench markings. Did benchmarks for 16k/300k/and 4million validators
  * got a full time resource working on the validator client. Part time resource working on bugs  
* Nimbus - Mamy [_(17:26)_](https://youtu.be/zeceWlmxseY?t=1046)
  * been working on libp2p nim. Considering bounties to progress further
  * with regards to the sync on the beacon chain, Nimbus had an open question on the handshake. And are using ROP serialization for the wire protocol that they implemented, and they want to kill ROP in that
  * regarding the state. In the past month, spec has been moved to v0.4. 
  * Nimbus development update: https://our.status.im/nimbus-development-update-03/
    * added a blockpool and ironed out some performance issues 
    * blockpool makes it easy for a beacon node to catch up to the others if it falls out of sync. And it also makes it possible to fix gaps in a node's blockchain.
    * work [has begun](https://github.com/status-im/nim-beacon-chain/pull/175) on fork choice implementation
    * used visualization tools to help detect a [Nimbus memory leak:](https://github.com/status-im/nimbus/issues/262)
    * implemented an initial version of the wire protocol specification in the [sync protocol](https://github.com/status-im/nim-beacon-chain/blob/master/beacon_chain/sync_protocol.nim) The clients will now say hello to each other, exchange header blocks, roots and bodies, reject connections on too long weak subjectivity times, and more.
    * Mamy's presentation at EthCC, on what can go wrong when building Eth2.0 clients, and how tests can help (and how they can harm): [Link](https://www.youtube.com/watch?v=6c4mQg5L6Rs)
* Trinity - Hsiao-Wei Wang [_(21:20)_] (https://youtu.be/zeceWlmxseY?t=1280)
  * working on spec syncing. Targeting v0.5
  * moved bls module to the pycc library. Since the bls signature verification is the biggest bottleneck, trying to isolate it
  * libp2p integration is still ongoing 
# 3. Research Updates
* Vitalik [_(46:41)_](https://youtu.be/zeceWlmxseY?t=2801) discussed a couple of spec formatting issues that came up. One of which was doing the shuffling in two different ways. At least as it's currently written in Phase 0 and Phase 1. The distinction is, is the shuffling a function of the integer going in being the role and the integer going out being the validator performing the role? Or is the function such that the input is the validator and the output is the role that it's performing. 
  * In Phase 0 what we're doing is shuffling, and then splitting the shuffle which says the validator indeces go in and roles go out. But in Phase 1, roles go in and validator indeces go out. It would be good to agree on one of the other. 
    * Input from Danny was to roll with what Phase 0 is doing, unless there is an argument to go with what's happening in Phase 1. 
    * Further discussion to be had. There are two issues in the spec relating to this issue: One is issue #729 and the other is #774 
* Vitalik also talked about another spec formatting issue. Specifically, that we are currently having hash tree roots taking one argument. The implication being that, with one argument you can infer what the type is. But there are some cases where we can't infer the type from the argument, with the most egregious one of those being lists. Because we can't distinguish between a static list and a dynamic list. 
  * One possible solution to this is make it so that hash tree root consistantly take both an object and a type.
  * The other approach is that we add wrapper classes for static lists and dynamic lists and apply them more consistently 
  * This is more on the Python side than anything, as a lot of those languages are going to have some form of internal distinction anyway. 
* Vitalik also talked about issue [#766](https://github.com/ethereum/eth2.0-specs/pull/766) and added light client related files. 
  * This includes several new ideas. One of which is a concept of a merkle multi-proof. Which is a theoretically optimal way to make a merkle proof formal to all objects. This potentially is ~20/30% more efficient than just having separate merkle proofs for different values.  
  * The second new idea revolves around the algorithm of get_generalized_indices. And that you can represent an arbitrary ssz hash tree. And so, you can represent a path (a path being a fn that, given a block as an input, return the public key of the 197th validator. Or return the length of the list of open challenges or something like that). So it takes a path and it turns it into a generalized index in the merkle tree. What direction do you go, how deep do you go, all expressed by a number. And from there it becomes really easy to make a multi-proof of multiple accesses going into ssz objects. This makes it really easy to define light client protocols for creating minimal ssz merkle proofs for calculating any kind of function you may need. 
  * Vitalik also discussed the idea of the merkle partial. Which is set of merkle proofs that you can then use in place of an ssz object and treat as an ssz object. 
  * The goal of all of this is to have a basic framework that you can use to do anything that you might want to do as a lightclient. 
* Justin Drake had a research update [_(1:01:39)_](https://youtu.be/zeceWlmxseY?t=3699) regarding an improvement to the challenge game in the custody bit scheme. In the optimistic case, where there are no challenges, you get this for free. It's just one extra bit in the attestations. But in the worst case, there is this challenge game that happens. And it turns out, that the Phase 1 spec grew much more complex than what we would have liked it to. The good news is this new challenge game drastically simplifies the communication complexity when a challenge happens. We can basically have a challenge which is a 2 step game of a single round of a challenge and a response. Which will hopefully allow us to have the Phase 1 spec be 4-8x more simpler than the Phase 0 spec. 
  * Also made a bunch of progress regarding the issues in #675 And hopefuly spec v.0.6 will have most of these checked off.
# 4. [quick update from Raúl/protocol labs](https://github.com/ethereum/eth2.0-pm/issues/33#issuecomment-472866505)
* Danny gave an update from Raúl of Protocol Labs: [_(23:51)_](https://youtu.be/zeceWlmxseY?t=1431)
  * working to add depracation notices to the areas of the spec that are outdated.
  * making significant strides on the new [docs.libp2p.io](https://docs.libp2p.io/)
  * writing a non-normative walkthrough of the libp2p stack that everyone can use as a reference, and engaging on various debates on github.
  * any questions feel free to reach out to Raúl  
# 5. [lighthouse benchmarks update](https://github.com/ethereum/eth2.0-pm/issues/33#issuecomment-472857213)
* Did a lot of parallelization which saved a lot of time
* One of the interesting things done was rewards processing as a parallel map to validator balances. And the spec was really well designed for it
* Suprised about decompressing a point in G1 cost the same amount as aggregating 2 points in G1. 
    * had a problem where, when processing a deposit, they wanted to see whether a public key exists in the validator registry or not. So they were building a hash map of pub-keys to a validator index. And when they were doing that, they found that going to bites was really slow, so instead of storing it as a point for the bls library, they stored it as uncompressed bites. Which made the hash map really fast and made the ssz serialization really slow because then they had to compress it. So they were wondering why they were compressing the public key bites, as it seems like everyone will need it in uncompressed form anyways. 
      * Vitalik had a comment on that. Saying that he doesn't think it will be a good idea to alter to the spec to store uncompressed points. Because it would require us to standardize serialization for uncompressed points, as well as standardizing serialization for compressed points. Especially given that the uncompressed points doesn't really get changed or accessed. 
* A more general point that Vitalik pointed out to keep in mind as we start exploring different efficiency trade-offs. For the beacon chain it might not be too bad, but especially once we delve into the shard chains there are going to be a lot of clients running ~ 5 shards/10 shards/50 shards - so we want to keep in mind what the marginal costs of being a validator on one of the shards are and what trade-offs exist. Have a clear model of what we think the costs are of a percent of cpu power vs. a gigabite of RAM vs. a gigabite of SSD and so forth. And seeing whether or not it makes sense to go in a particular direction. Basically because we do have an important task of running a validator being marginally cheap, because if its not it's going to significantly eat into validator profits. Which could really hurt participation and encourage things like stake pooling.     
* The other thing to benchmark on would be a minimal cost vps. Although, we don't really want to encourage people to stake on vps'
* Should avoid the trap on running benchmarks on powerful hardware because we don't to repeat the mistake of Eth1.0 and have it have really high spec requirements. Would be good to get numbers on something like a ~$200 laptops
# 6. [Leap seconds](https://github.com/ethereum/eth2.0-pm/issues/33#issuecomment-472029888) and time drift
* Justin added a note that leap seconds is handled in unix time, and we are conforming to unix time. 
* Justin further goes on to discuss that we need some notion of time in Ethereum 2.0. We have two options: one is unix time which subtracts the number of leap seconds. And the other option is international atomic time. There are several reasons why we are favoring this unix time over international atomic time:
  * It's much more commonly accessible in programming language. So ease of use for the programmer
  * It's compatible with Eth1 timestap, as it uses unix timestamps. 
  * It provides a nice invariance that at midnight UTC, the slot number is going to be a multiple of 14,400. 
* One of the things done with Eth2.0 genesis is to have the genesis be at midnight UTC. And so, this invariance would remain over time if we take into account the lead seconds.
* By having this invariance, we lose the invariance as every slot is exactly 6 seconds (or whatever constant we set it in the future)
* Justin adds that he thinks this is the right trade-off to make. But is happy to hear counter arguments
  * Danny added that a timer without going back to set some sort of system clock seems rather dangerous. And seems like we could get much drift over time. 
  * Vitalik added that the kind of bug he could foresee happening with relying on doing timers without going back to a system clock is that, what if your computer temporarily slows down and it takes you 19sec to verify some block. Or even just if your computer sleeps and wakes up. 
  * An interesting note is that 14,400 is a multiple of 64, which means we get really nice epoch boundaries at midnight every time. 
* Currently should be using system time to currently determine slots. Specifically, system time that conforms to unix that would adjust for leap seconds over time
* [Link](https://ethresear.ch/t/network-adjusted-timestamps/4187) to Vitalik's post on ethresearch. Urged people to implement it or for folks to come up with reasons for something else
* Leo commented at [42:30](https://youtu.be/zeceWlmxseY?t=2550) his work on the supercomputer. He implemented local timers for the nodes. But he also implemented some global synchronization every 5 seconds. With that 5 second paramater being one that could be customized. 
# 7. [Network spec](https://github.com/ethereum/eth2.0-specs/pull/763)
* Zak chimed in, discussing how him and a few others have started to build out a lightweight PoC type of wire protocol (Hobbits). The idea is to create something that works right now, and have just about finished implementing it. 
* Matt Elder talked about the feedback being created. Not a lot of activity going on with regards to testing peers talking to each other. And, even though libp2p is being used to find peers more at a higher level, maybe there should be something at the lower level that is a simple wire protocol which people can start iterating and start communicating. 
  * cretaed an ebnf grammar, which is inspired by http but is very narrow and minimalistic to the use case of sending binary payloads in an rpc manner
* Discussion ensued around the matter of ssz, libp2p, and its relation to the application layer and the wire protocol at [1:11:47](https://youtu.be/zeceWlmxseY?t=4307) 
* Felix gave an update on discv5 [1:25:14](https://youtu.be/zeceWlmxseY?t=5114): Hasn't really been busy with it the last couple of weeks because of trying to push eth v64 discussion forward (mostly concerns Eth1.0). 
  * did revamp Eth1.0 specifications
  * still implementing discv5. Specifications live in the repo
# 8. [serialization benchmarks](https://github.com/ethereum/eth2.0-pm/issues/33)
* Piper's been digging into serialization more at the application layer
* Ran a bunch of benchmarks w/ some extensive data coming out of it:
  * gist is that ROP is actually really terrible for Eth2.0 data structures (almost doubles the size) because of all of the little link prefixes and deep nesting of things like blocks and attestations
* Been looking at old version of ssz spec. Has his own compact serialization format he's been tinkering with. 
* Been pushing to modify the ssz spec to include the sos style offset pattern, so that we can have a serialization format that also works as a contract abi. And those two things combined together give us reasonably compact messages that can also be used to talk directly into contracts that give us that fast indexing into data structures. Which, at the application layer, may not be useful. But inside the context of the EVM/eWASM - being able to reach into these things and be able to grab the data you need is actually useful. 
* Tree hash maps well onto any of these formats
* Some experiments with ssz suggest that there's maybe 9-10% size gains that can be improved, but it's reasonably efficient from the get go. Not as the wire protocol, but the inner part of it. 
* Antoine asked about cpu utilization, and if there is a big difference. In which Piper suspects that the more compact version is less cpu intensive assuming you're decoding the whole thing. 
* https://github.com/ethereum/eth2.0-pm/issues/33
# 9. Spec discussion
* Danny informed the group that he will be sending out v0.5 that day
* Can handle any question in the gitter
* Vitalik brought up that we have talked before about being in favor of having class wrappers to separate static and dynamic lists so that they have different Python types
  * Danny: Yes, because that translates more over to the statically typed languages anyways. No need to make any wrappers for numbers.
* Research team to start doing a pass on adding explicit invariants 
# 10. Open Discussion/Closing Remarks
* Danny brought up that there will be a meeting on April 9th in Syndey from 9-5 for those that want to attend
  * Will share location and get a doc sent around as to who will be there, what will be worked on
* Actual EDCON starts April 11th 

# Links shared during meeting
* https://github.com/harmony-dev/beacon-chain-java/releases/tag/v0.1.0
* https://docs.libp2p.io
* https://ethresear.ch/t/network-adjusted-timestamps/4187
* https://github.com/ethereum/eth2.0-specs/pull/766
* https://github.com/ethereum/eth2.0-specs/pull/766
* https://github.com/ethereum/research/tree/master/merkle_tree
* https://github.com/ethereum/eth2.0-specs/blob/dev/specs/core/0_beacon-chain.md#beaconblockheader
* https://github.com/ethereum/eth2.0-specs/pull/763
* https://github.com/Whiteblock/hobbits
* https://discourse.deltap2p.com/t/hobbits-or-there-and-back-again-a-lightweight-multiclient-wire-protocol-for-web3-communications/36
* https://notes.ethereum.org/ZHaCS6_bQNSxr5bSPcObLw#
* https://notes.ethereum.org/QF8jgOQbRTWUhK1zoi8D4Q#

# Attendees
* Danny Ryan (EF/Research)
* Adrian Manning (Lighthouse/Sigma Prime)
* Alex Stokes (Lighthouse/Sigma Prime)
* Vitalik Buterin (EF/Research)
* Antoine Toulme (ConsenSys)
* Anton Nashatyrev (Harmony)
* Ben Edgington (PegaSys)
* Blazj Kolad (Pegasys)
* Carl Beekhuizen (EF/Research)
* Cem Ozer (PegaSys)
* Chih-Cheng Liang (EF/Research)
* Daniel Ellison (ConsenSys)
* Dean Eigenmann (Yeeth)
* Dankrad Feist (HiDoc Technologies)
* Diederik Loerakker (Independent)
* Felix Lange (EF/geth)
* Fredrick Harrysson (Parity)
* Greg Markou (ChainSafe)
* Greg Orbo (Clearmatics)
* Hsiao-Wei Wang (EF/Research)
* Jacek Sieka (Status/Nimbus)
* Jannik Luhn (Brainbot/Research)
* Jonny Rhea (Pegasys)
* Joseph Delong (PegaSys)
* Justin Drake (EF/Research)
* Kevin Mai-Hsuan (EF/Research)
* Leo (BSC)
* Nicolas Liochon (PegaSys)
* Mamy Ratsimbazafy (Nimbus/Status)
* Matthew Slipper (Kyokan)
* Matthew Elder (Whiteblock)
* Mikerah (ChainSafe)
* Mikhail Kalinan (Harmony)
* Nicholas (Hsiu-Ping) Lin (EF/Research)
* Nicolas Gailly (PegaSys)
* Olivier Begassat (ConsenSys)
* Paul Hauner (Lighthouse/Sigma Prime)
* Piper Merriam (Trinity/Py-EVM)
* Raúl Jordan (Prysmatic)
* Terence Tsao (Prymatic)
* Wei Tang (Parity)
* Zak Cole (Whiteblock)
* Meeting notes by: Peter Gallagher























