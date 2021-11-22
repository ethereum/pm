# Ethereum 2.0 Implementers Call 7 Notes
### Meeting Date/Time: Thu, November 29, 2018 14:00 GMT
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/17)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=Zl-yusB8oqY)

# Agenda
1. Client Updates [_(10:10)_](https://youtu.be/Zl-yusB8oqY?t=610)
2. Research Updates [_(24:07)_](https://youtu.be/Zl-yusB8oqY?t=1447)
3. p2p discovery protocol [_(47:47)_](https://youtu.be/Zl-yusB8oqY?t=2867)
    * Current state of [discv5](https://github.com/fjl/p2p-drafts/blob/master/discv5-eip.md)
      * Does it meet our needs?
      * What implementations exist?
      * Complexity of implementing from scratch
    * Any alternatives being considered?
4. Validator privacy and roles [_(57:37)_](https://youtu.be/Zl-yusB8oqY?t=3457)
    * [val privacy discussion](https://github.com/ethresearch/p2p/issues/5)
    * [WIP min validator interface](https://notes.ethereum.org/Ia2kvjy0RX2J-GxrWfoCAQ?view)
    * [prysmatic val service protos](https://github.com/prysmaticlabs/prysm/blob/master/proto/beacon/rpc/v1/services.proto)
    * pros/cons of strict polling interface (like eth1.0 rpc methods) vs. streaming interface (something like [grpc](https://grpc.io/))
5. [libp2p 2019 roadmap](https://docs.google.com/document/d/1Rd4yNw1TNQBvfRrKeEMSTseb6fvPzS-C--obOn0nul8/edit)[_(1:11:22)_](https://youtu.be/Zl-yusB8oqY?t=4282)
6. Spec discussion [_(1:14:00)_](https://youtu.be/Zl-yusB8oqY?t=4440)

# Client Updates
* Nimbus (Mamy) [_(10:10-14:02)_](https://youtu.be/Zl-yusB8oqY?t=610)
  * Caught up with spec changes
  * Nim wrapper working for the libp2p daemon. Now they can have two team members chatting through libp2p daemon with the nim  wrapper
  * Target of running demo beacon node for December. In doing so, they reorganized their repo. 
    * Cleanly separated between spec, client implementation, network protocol, and Nimbus
  * Started implementing 3rd bls signature aggregation scheme. Expressed the need for common tests 
    * Checked zcash tests, but they are using rng
    * Saw some differences from Chia as well [(Link)](https://github.com/ethereum/eth2.0-specs/issues/184)
      * Mamy suggested that if they could have an Alice, Bob and Eve key test, like what is done in the ETH2.0 repo [(Link)](https://github.com/ethereum/eth-keys/blob/master/tests/backends/conftest.py#L35-L66) and, after, add them as a sanity check to the YAML test file
      * In the appendix in the bls spec, they expressed the fact that some kind of sanity check would be nice. Danny responded saying he will reach out to coordinate around bls tests.        
* Lighthouse (Paul Hauner)  [_14:05-14:30_](https://youtu.be/Zl-yusB8oqY?t=845)
  * Have been in the process of expanding the team, which has been quite successful
  * More updates to come next meeting.    
* Parity (Fredrik Harrysson)  [_14:32-14:40_](https://youtu.be/Zl-yusB8oqY?t=872)
  * No major update   
* Lodestar (Mikerah) [_14:42-15:30_](https://youtu.be/Zl-yusB8oqY?t=882)
  * Focusing on converting to typescript
  * Slowly starting a bls signature aggregation library as well  
* PyEVM (Hsiao-Wei Wang)  [_15:35-16:36_](https://youtu.be/Zl-yusB8oqY?t=935)
    * Helping to review the spec
    * Working on data structures and helper functions
    * Have internal consensus on the Trinity test net [(Link)](https://github.com/ethereum/py-evm/issues/1502) and what the components the mvp will contain 
* Harmony (Mikhail) [_16:41-20:04_](https://youtu.be/Zl-yusB8oqY?t=1001)
    * Catching up with the spec
    * Integrated milagro and using it for bls verification implementation
      * Relative to Nimbus, it's 1.5 to 2x slower (not sure if we can really judge these numbers at the moment though)
        * Jacek Sieka (Nimbus) also added that they have not really optimized things yet on their side, so even their numbers may not really be ones to benchmark yet. 
* Prysmatic (Raúl Jordan)  [_20:08-22:13_](https://youtu.be/Zl-yusB8oqY?t=1208)
    * Regarding bls, they are using the herumi library, which uses an underlying cryptographic library called mcl (however the dependency for gnp was just removed yesterday. So benchmarks will be done to see if removing gnp will make things any slower)
    * Working on optimizing a Miller loop so that they can have signatures in G2, and public keys in G1
    * Refactoring code base to match having a single beacon state (removed thounsands of line from code base)
    * Have a kubernetes configuration in place for a test net. Have a DHT discovery working with a relay node that helps traffic inbound connections to nodes in the cluster. And they also have a boot node for the beacon node.
    * Focusing on aligning with the spec   
* Pegasys (Joseph Delong)  [_22:15-23:54_](https://youtu.be/Zl-yusB8oqY?t=1208)
    * Brought in three new team members
    * Started an implementation of ssz, but put on hold as they further align with the spec
    * Started writing a Solidity version of the validator relay contract  
    * Team member Jonny Rhea worked with Raúl on a libp2p daemon. Compile is a shared object library so you can interface libp2p with the client regardless of the language [(Link)](https://github.com/libp2p/go-libp2p-daemon/pull/28/files)
# 2. Research Updates  
* Vitalik [_24:15_](https://youtu.be/Zl-yusB8oqY?t=1455)
    * Justin, Danny, Hsiao-Wei, and Vitalik have been working quite a bit to get the spec to a point of it being feature ready for what we want to have for phase0
    * Most recent things added were the tree hashing mechanism, active and crystallized state merging, and then switching back from using cycles to using epochs (which is a fairly considerable gain in simplicity)
    * Some modifications to the casper ffg that fixes a couple of bugs, along with some code that adds in preliminary placeholders for proof of custody, and a couple of other various small things
    * Basically at the point where phase0 is going through spec re-writing, and cleaning up and making it easier to read to find and fix bugs and so forth
    * On the phase1 side - there is definitely still quite a bit of work to do, and different ideas that still need to be thought about (like what data roots get committed into the data hash that goes into the cross link. Still have quite a bit more time to think about, however.)
    * Danny also added that one of their intentions with the phase0 vs. phase1 is to get all the data structures ready for phase1
      * Designing phase0 for future compatibility with the array of things that we will likely want to include for phase1 and phase2
    * Justin also added: we might have to change the format if there is something we find after launch 
      * Basically in clean-up mode finding bugs. He gave a heads up to the room, saying that he expects there to be at least 100 bugs that still need to be found 
      * One of the things he is working on, and it is helping w/ the review, is that he is re-writing the whole spec (called the Transparent Paper). It is meant to be a bit like the Yellow Paper for Ethereum 1.0, but instead of being super formal - it is meant to be designed for insight and designed for readability and transparency
        * In addition to the spec, it has definitions for every single term, and has explanations on design decisions etc.
        * Hoping to get that out by end of January 2019 (along with a close to finalized spec on github as well)
        
* Leo (BSC) [_31:05_](https://youtu.be/Zl-yusB8oqY?t=1865)
    * Have a first prototype of a simulator that can run on a supercomputer
      * Not completely up to do date with latest developments of the spec, as nothing has really been added in the last couple of months 
    * Gave a talk about sharding at a meetup in Barcelona & exchanged a couple of emails with Justin and Vitalik
    * Hoping to get more up to date with the spec with regards to the simulator in the coming future
    * In terms of the type of data they plan to report - they want to see different aspects and behaviors relating to the spec. For example, they want to try and simulate different latencies between different nodes and different clients, and try and see different loading balances between the number of Tx to see how that affects the number of cross shard Tx and those types of things.

* Pegasys [_36:10_](https://youtu.be/Zl-yusB8oqY?t=2170)
    * Continuing to work on the tree based aggregation
    * Have something working, but it is still very basic
      * More tests to come in the coming weeks
    * Soon will be doing a presentation for protocol simulations (will put an invite on Gitter for those interested)
    * Looking into potential alignment and convergence of an onion transport for anonymity (currently on libp2p roadmap as well)
    * From libp2p standpoint, QUIC is definitely a priority for them 
      * QUIC is a UDP-based transport protocol that provides many of the guarantees of TCP in terms of congestion control and reliability. It also implements multiplexing, and it also includes security and encryption constructs on top of the transport itself.
      * Two reasons for Pegasys to use it:
        * Hopefully will be able to use it to connect to a lot of peers w/o consuming too many resources 
        * UDP allows for much better opportunities for holepunching and different techniques (alphabetic activity, etc.)
        
 * Jonny Rhea [_47:18_](https://youtu.be/Zl-yusB8oqY?t=2838)
    * Question to Raúl about adding a flag to the libp2p daemon to expose that QUIC transport. 
      * Raul responded, saying that would be something that could be done, and to follow up with an issue and that they will get that moving
# 3. p2p discovery protocol 
* Danny [_47:56_](https://youtu.be/Zl-yusB8oqY?t=2876) talked about the general discussion happening, especially around devcon, on moving towards discv5 as the p2p discovery protocol
  * feasible to start using now?
  * does it meet our needs?
  * Jannik Luhn responded, saying he likes it, and estimated that it should not be too slow
    * doesn't think it would be too difficult to implement
    * only problem he sees is that the spec is not very stable at the moment
  * discv5 specifically implements the feature we need, in that it advertises the topics that we subscribe to
  * Discussion ensued about possible alternatives to discv5
    * Ultimately, further discussion led to consensus about getting in touch with Felix to make discv5 happen, so that teams can move on it
  * Danny asked Jannik that, if teams were wanting to use a discovery protocol right now, and only use the beacon subnet (instead of all the shard subnets), would targeting discv4 make sense, in that most of the underlying components of v4 is what v5 uses as well?
    * further discussion ensued [_52:39_](https://youtu.be/Zl-yusB8oqY?t=3158)
    * libp2p team have been in touch w/ Felix and have had meetings with him and are happy to collaborate
    * Jacek also added, that a critical feature that led to adoption of v5 with Status, was the fact that you could negotiate peers with specific capabilities - so that you know that the peer you're looking for has support for a particular feature. Something that perhaps should be a hard requirement for a discovery protocol, that we have the capability of feature discovery of the peers that we're talking to.
      * libp2p has in their roadmap, that they are intending to build an abstraction for service discovery that can be driven by other discovery protocols (locals, connected, or over a local network, etc.)  
# 4. Validator privacy and roles
* Ongoing discussion around validator privacy in the p2p research repo
* Jannik started the conversation, saying that he thinks everyone agrees that validator privacy is important. And suggested that perhaps a discussion ensue around the idea of having multiple proposers for each slot, so that if one proposer is attacked another can take its place.
  * Vitalik responded [_59:06_](https://youtu.be/Zl-yusB8oqY?t=3546) saying that it's fairly complicated to implement at this point. And also runs into potential race conditions.
    * Talked about how the nice thing about the 1 validator per slot approach is that it makes it simple that you have a 6 second window in which to propose or not, and if you don't, then someone else does.
* zkproof .::. ring signature construction used to fight against potential eclipse attacks of the shard subnets
* Design goal right now is to make the validator as distinct from their position in the network as possible
  * such that validators can create any set of node setup that makes sense for their security concerns
  * Danny alluded to airing on the side of simplicity with regards to the base protocol, unless we have a very compelling solution native to the protocol
* Raul added [_1:01:25_](https://youtu.be/Zl-yusB8oqY?t=3546) - with respect to syncing and the role of validators. Perhaps the beacon node could be in charge of syncing the shard, and the hand off that data off to the validators.
  * Team at Prysmatic has been discussing this, and they don't understand why this sidecar approach is really that effective - and why can't validators be in charge on syncing side chains?
    * Danny responded, saying that the general distinction in the software is that we have a client piece of software that can run and process the entire blockchain, beacon chain, and shard chains. And the validator is a special, user piece of software, that connects and talks to a client piece of software. Once we put in shard syncing and peer management into the validator piece of software, we now have two node pieces of software (and we make the barrier of entry to create a new validator piece of software being very high)
    * the distinction of the validator piece of software being so thin (controlling keys, controlling secrets, and signing things) can allow for very diverse set-ups. A validator could talk to ten different nodes, controlling them via commands, ask information about the shards, sign information and broadcast as they please. But putting actual block processing and consensus rules within that piece of software may not be the design decision that gives us the most optimal set of potential set ups. 
    * as long as you keep the validator secure, he can talk to whatever nodes he wants. If he has five nodes he's communicating with - and one of those becomes hacked, or is attacked, there is redundancy there. However, if it is in charge of syncing its own data and connecting to peers, then it becomes a single point of failure. 
    * General consensus in that a node should be general purpose and be able to sync the beacon chain and shard chains
    * Paul Hauner chimed in [_1:06:38_](https://youtu.be/Zl-yusB8oqY?t=3998), saying that the way he's been thinking about it is that the validator has this schedule that they need to operate on. So they need to gain from the beacon node this idea that over these periods/slots they are going to need to create some action. So the solution that he came to, was that the scheduling is inside the validating client (retrieving and maintaining schedule)
      * means the validator can swap around between nodes
      * if it starts to maintain this schedule, over time it can start to have this idea that when they aren't getting the responses they can swap around. While if that schedule is inside the beacon node, then if the beacon node stumbles then there is nothing really checking it
        * Danny to make an issue around these issues to dig in and debate even more this idea around the design decisions     
# 5. [libp2p 2019 roadmap](https://docs.google.com/document/d/1Rd4yNw1TNQBvfRrKeEMSTseb6fvPzS-C--obOn0nul8/edit) 
* Raúl [_1:11:38_](https://youtu.be/Zl-yusB8oqY?t=4298) talked about an open call for participation in the roadmap. Defining together what they want to focus on in the future (in terms of vision and where to take the future of p2p networks)
* wants to lock down the wish list of all the items 
  * collecting input from many communities
  * what are priorities?
  * by the next couple of weeks - they hope to have prioritized these ideas, and build a roadmap and a timeline to build them out for 2019 and forward 
  * [Link](https://docs.google.com/document/d/1Rd4yNw1TNQBvfRrKeEMSTseb6fvPzS-C--obOn0nul8/edit#heading=h.bbb5kq80e8n)
# 6. General spec discussion
* Mikerah [_1:14:31_](https://youtu.be/Zl-yusB8oqY?t=4471) started the conversation, specifically asking a question about persistent chain splits
  * what happens if something like a DAO attack happens, and people would want to split in ETH2.0? How would that work?
  * Danny responded - saying there is a general versioning structure in there to handle splits and forks (contentious or not). What the versioning does, is that it puts signatures into a separate domain, such that people running a previous version of the software are not "colliding" the signatures with the newer version of the software.
    * so, in the case that someone wants to coordinate a permanent fork, they would use that mechanism to essentially run a slightly modified version of the software and to ensure that their signatures are in a different domain
* Notes from Starks working group from Prague (Team from Starkware gave the notes to Danny who cleaned them up) [(Link)](https://notes.ethereum.org/b8DsLbLcRmKHlWAXEXt_Rw)
* Jacek [_1:17:30_](https://youtu.be/Zl-yusB8oqY?t=4650) asked about unsigned integers. And if you are looking for bugs, one good source to find them is through unsigned arithmetic
    * further discussion ensued from Jacek, adding that perhaps some of the data in the beacon spec is redundant, with the biggest point being the shard committees (derived from a different field in the state). As far as he is concerned, perhaps it would be more simple if it wasn't in the state, but rather that it was such that the beginning of processing - client implementers could cache if they wish to
      * Discussion ensued, particularly around the fact that removing it from the state means you lose the ability to serve it, and to serve portions of it (say, to light clients), means you put the requirement of doing the shuffling and maintaining the shuffling at all times on every client/node that is in the network 
      * Mikhail chimed in, saying he had been thinking about other parts of the state that perhaps could not be in the state - such as recent block hashes
        * Danny added that one of the general goals has been that, with the previous state + recent block hashes, you can calculate the entire state transition function (which is why the recent block hashes are in there - to verify attestations on the epoch boundaries. Once you take that out, you make the state encompass multiple blocks and to process the state, you still need the state locally, but you've kind of hidden it as opposed to making it explicit with regards to what the peer requirements are.)
* Issue to be opened up for debate and discussion to be had
* Issue #129 -- some debate going on around the use of ssz vs. protobuf
  * regardless of what we use on the network level (if we move towards protobuf) - we will be using ssz for the tree hashing algorithm for the actual hashing of the state
  * Mikhail added, saying that one of his concerns with ssz, on his side, is that it's not forward compatible with regards to adding new fields to any structure (an example being the chain ID field from ETH1.0. Although, it has been added, and it had to be encoded in the existing transaction structure. Mikhail went on to say that it would be great if ssz had this feature, albeit it's not essential)  
 # Links shared during meeting
* https://github.com/ethereum/eth2.0-pm/issues/17
* https://github.com/ethereum/eth-keys/blob/master/tests/backends/conftest.py#L35-L66
* https://github.com/ethereum/eth2.0-specs/issues/184
* https://github.com/ethereum/py-evm/issues/1502
* https://github.com/libp2p/go-libp2p-daemon/pull/28/files
* https://github.com/chronaeon/beigepaper/blob/master/README.md
* https://github.com/ethresearch/p2p/issues/6
* https://github.com/ConsenSys/oath
* https://hypelabs.io/
* https://github.com/libp2p/go-libp2p-daemon/issues/33
* https://docs.google.com/document/d/1Rd4yNw1TNQBvfRrKeEMSTseb6fvPzS-C--obOn0nul8/edit#heading=h.bbb5kq80e8n
* https://notes.ethereum.org/b8DsLbLcRmKHlWAXEXt_Rw
* https://github.com/ethereum/eth2.0-specs/pull/160
* https://github.com/ethereum/eth2.0-specs/issues/129

# Attendees
* Akhila
* Ankit
* Christoph Burgdorf (py-evm)
* Zahary (Status/Nimbus
* Leo (BSC)
* Nicolas Gailly (Pegasys)
* Mikhail Kalinin (Harmony)
* Nicholas Lin (EF/Research)
* Nicolas Liochon (Pegasys)
* Nishant Das (Prysmatic)
* Prateek Reddy (EF/Research)
* Jonny Rhea (Pegasys)
* Vitalik Buterin (EF/Research)
* Joseph Delong (ConsenSys)
* Daniel Ellison (ConsenSys)
* George (Clearmatics)
* Danny Ryan (EF/Research)
* Carl Beekhuizen (Decentralized staking pools)
* Raúl Jordan (Prysmatic)
* Justin Drake (EF/Research)
* Jannik Luhn (Brainbot/Research)
* Paul Hauner (Lighthouse/Sigma Prime)
* Chih-Cheng Liang (EF/Research)
* Adrian Manning (Lighthouse/Sigma Prime)
* Mamy Ratsimbazafy (Status/Nimbus)
* Hsiao-Wei Wang (EF/Research)
* Jacek Sieka (Status/Nimbus)
* Fredrick Harryson (Parity) 
* Mikerah (ChainSafe)
* Ben Edgington (Pegasys)
* Martin Holst Swende (EF/geth/testing)
* Peter Gallagher (Meeting Notes) 
