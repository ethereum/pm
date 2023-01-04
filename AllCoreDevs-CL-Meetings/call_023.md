# Ethereum 2.0 Implementers Call 23 Notes

### Meeting Date/Time: Thursday August 15, 2019 at 14:00 GMT
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/68)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=Av74vZRXeKo)
### Moderator: Danny Ryan
### Scribe: Brent Allsop

----

## Agenda
- [1. Testing and Release Updates](#1-testing-updates)
  * VDF update
- [2. Client Updates](#2-client-updates)
- [3. Networking](#4-network)
  * Block capacity and compression
  * BFT vs scalability in p2p network
- [4. Research Updates](#4-research-updates)
- [5. Spec Discussion](#5-spec-discussion)
- [6. Open Discussion/Closing Remarks](#6-open-discussionclosing-remarks)

## 0. Welcome

**Danny Ryan**(https://www.youtube.com/watch?v=Av74vZRXeKo&t=7m19s)began by saying he'd messed up the tests before going on vacation, so BLS tests were not included. Subsequently, they have been pushed into master but not cut as a new release. Added some additional SSZ generic tests. Intention is to cut 0.8.3. on 8/19 or 8/20. 0.8.3. is non-substantive and is essentially the same as 0.8.2. with additional tests. This is the Interop target for the September gathering. Asked if anyone was opposed, and no one was.


## 1. [Testing and Release Updates](https://www.youtube.com/watch?v=Av74vZRXeKo&t=9m16s)

**Diederik Loerakker(@protolambda)** issued last call for final feedback on tests for new release.

**Danny Ryan**(https://www.youtube.com/watch?v=Av74vZRXeKo&t=10m4s)discussed other things on the horizon for releases. Runtime verification found a Viper compiler bug that is being fixed. Also going to be adding a checksum to locally compute what the SSZ route of your data should be. Will stay in dev until mid to late September. At the same time, will also be removing current machinery in place for light clients that doesn't quite work and adds substantial hashing overhead. This will be a deletion of active index routes. Will also be removing transfers.

**Shahan Khatchadourian**(https://www.youtube.com/watch?v=Av74vZRXeKo&t=12m9s) asked for links that discuss the removals. Danny responded that he believed there were and asked participants to find and share them.

## 2. [Client Updates](https://www.youtube.com/watch?v=Av74vZRXeKo&t=12m56s)

**Yeeth**(https://www.youtube.com/watch?v=Av74vZRXeKo&t=13m01s) said they're working on a validator client rather than the beacon chain. Using Lodestar's beacon chain node for their validator client. Discussed RFP for Malik independent validator client.

**[Mikhail Kalinin (Harmony)](https://www.youtube.com/watch?v=Av74vZRXeKo&t=14m16s)** Main executable now allows for chain storage to be dropped on disk. Worked on Eth1 integration and implemented clients based on JSON RPC. This PR is still waiting to get merged. Anton has finished a gossip sub implementation and is testing that with the daemon. Getting close to the release and hope to be ready for interop in September. Have started to work on 0.8.2 upgrade and the QA and fuzzer to get all this to work with the network stack.  

**[Hsiao-Wei Wang (Trinity)](https://www.youtube.com/watch?v=Av74vZRXeKo&t=16m37s)** Mostly focusing on the requirements of the interop. Most work is on the pilot p2p module for interop usage. Still some minor inconsistencies in the pilot p2p that are being fixed. Building a beacon chain receive server for handling wire protocol message requests. That's an open PR that will be merged as soon as possible. Working on Discovery v5 functionality for the Trinity Eth1 client.

**[Shahan Khatchadourian (Artemis)](https://www.youtube.com/watch?v=Av74vZRXeKo&t=18m17s)** introduced himself as he just joined Artemis. Has a background in database related blockchain stuff and Sandcastle. Artemis working on SSZ debugging state routes as well as the serialization. Working on state tests. Plugged in Lighthouse to Artemis. If anyone has any questions about the upcoming interop, get in touch with Joseph DeLong.

**[Adrian Manning (Lighthouse)](https://www.youtube.com/watch?v=Av74vZRXeKo&t=20m24s)** has been trying to optimize their database and working on their testnet stability, looking at extra metering and doing some bug squashing. They've been updating their networking stack and are modifying and improving the syncing algorithm to match with the new RPC. Working on BLS standardization and connecting Lighthouse to Eth1 with the Eth1 deposit contract. Improving HTTP API.   

**Terence Tsao (Prysmatic Labs, @terenc3t)(https://www.youtube.com/watch?v=Av74vZRXeKo&t=21m52s)** has some parallel efforts going on. Working on ramping current sync to align with networking stack to make it easier to query. Working on benchmarking optimization. Goldpro library is making POS improvements, making it possible to verify 128 public keys in 20 milliseconds.

**[Cayman (Lodestar)](https://www.youtube.com/watch?v=Av74vZRXeKo&t=23m17s)** Introduced Eric (Weather Cam) as the new member of the team researching assembly script integrations. Working up to date on 0.8.2 spec tests. Migrated their code management to a mono-repo style, all in the Lodestar repository. Published SSZ types on NPN and beacon chain configurations. Working on networking for interop. Fixing libp2p protocols.  

**[Wei Tang (Parity)](https://www.youtube.com/watch?v=Av74vZRXeKo&t=25m05s)** was absent.

**[Mamy Ratsimbazafy (Nimbus)](https://www.youtube.com/watch?v=Av74vZRXeKo&t=25m15s)** has a new developer, Dmitriy Ryajov, who is working on libp2p and networking. They have gotten the new SSZ implemented in the past 3 weeks. Created a way to bootstrap Eth2 genesis. Link is in the chat. Implemented a new networking spec. Libp2p working again on Windows.     

**Diederik Loerakker(@protolambda)(https://www.youtube.com/watch?v=Av74vZRXeKo&t=26m44s)** has been chatting with Whiteblock and is putting together a survey to map out where everyone wants to go for all different features. Putting together a table and comparison chart to see where all the teams are. Putting a questionnaire in Github and meeting with people one on one.

## 3. [Networking](https://www.youtube.com/watch?v=Av74vZRXeKo&t=30m58s)

**Felix Lange** gave an update on Discovery v5. Started an audit of the spec graph that has been going on for one week and will continue for at least one to two weeks more. Initial report shows that it is not very well explained. On the implementation side, not much has changed, and implementation is up to where the spec is. Interested to see if they can do any interop testing on it. Go and the spec are now the same, because they changed the spec.

**Mikhail Kalinin(https://www.youtube.com/watch?v=Av74vZRXeKo&t=34m56s)** asked about a spec security consideration. Felix responded that they've added new text to explain new security guarantees. Discussion of icons.

**Mike Goelzer (Protocol Labs)(https://www.youtube.com/watch?v=Av74vZRXeKo&t=38m10s)**
said they didn't have much to update. Announced devgrants that can be found at https://github.com/libp2p/devgrants. Said there will be bounties at the Hackathon.  

**Whiteblock(https://www.youtube.com/watch?v=Av74vZRXeKo&t=40m40s)** had no real updates but announced they were hosting a webinar a couple of hours after the call "talking shop." Will share additional information on the next call.

**Shahan Khatchadourian (Artemis)(https://www.youtube.com/watch?v=Av74vZRXeKo&t=41m47s)** asked Felix Lange about the Disc v5 handshake and overlap with other handshakes.

**Danny Ryan (https://www.youtube.com/watch?v=Av74vZRXeKo&t=44m10s)** discussed Harmony's work on network load with regard to attestation aggregation and attestation propagation. Investigating pros and cons of various structure strategies. Might need to increase max attestations for blocks. There are a lot of trade-offs in design to consider. Mentioned that Vitalic suggested that to avoid some of the aggregate overlaps, we could have smaller shard subnets.

**Mikhail Kalinin (https://www.youtube.com/watch?v=Av74vZRXeKo&t=46m47s)** spoke to this issue and said Harmony has started research investigating aggregation strategies and discovered that aggregation strategies are not a bottleneck for the system, but attestation delivery could become a bottleneck down the road as the network grows. Called for greater research and more teams to get involved.

## 4. [Research Updates](https://www.youtube.com/watch?v=Av74vZRXeKo&t=52m55s)

**Vitalik Buterin(EF/Research)(https://www.youtube.com/watch?v=Av74vZRXeKo&t=52m55s)** said a couple of PRs got merged including 1186, which is modifying the way that Merkle Proof verification works. Instead of providing separate index in depth, it provides a generalized index, and there's a set of methods for working with generalized indices. There's also an unfinished PR, 1316, re: beacon chin updates for phase 1 that adds persistent committee routes.

There is also an updated PR defining the default light client syncing algorithm. The important message is that there is now enough to go off of in order to start actually building light clients. Encourages to developers to think about and implement it. Also raised the possibility of making some kind of infrastructure to make it easier for people to start building and testing their light clients. Currently, it is not possible to make a practical light client until Phase 1 launches.

Also looking at private information retriever protocols that make light clients more privacy preserving. So far, stuff exists but it raises the overhead significantly. The idea is that you make a request and the server replies, and the server has no idea what Merkle branch you asked for.

Discussed 3 different kinds of private information retrieval (PIR). First is using trust of execution environments.

Second is information theoretic PIR, which is when you talk to end servers and you ask each of the servers to evaluate a function on all of the data, and each server gets a different function and none of the servers know what you're accessing.

Third is computational PIR, which works by sending the server a mathematical object, and the server applies some transformation based on every piece of data, and the mathematical structure has some trap door that you include that has the effect that when you decrypt the results, it includes information of the specific piece of data without the server's knowledge.

The main drawback of 2 and 3 is the overhead on the server side.

**Justin Drake(https://www.youtube.com/watch?v=Av74vZRXeKo&t=62m02s)** gave a few updates. First is an announcement of Phase 0 bounties. Any adjustment to the Phase 0 spec will get rewarded 5 ETH or 1000 DAI.

Second is that BLS standardization is now feature complete with no known issues and can be considered frozen. Plan is to integrate new BLS spec into dev but not merging into master too soon.

Finally, discussed quantum apocalypse insurance, where in the event of a quantum apocalypse, we can disable all the BLS signatures and have a way for validators to safely transfer the balance on to whatever new platform comes next that is quantum secure.

**Will Villaneuva(https://www.youtube.com/watch?v=Av74vZRXeKo&t=68m45s)** has been benchmarking single pass, multi-branch updates/Merkle proofs on a sparse Merkle tree implementing SSZ within an execution environment in the context of simple transfers. Getting preliminary results and benchmarking numbers. Continuing to build out phase 1.

**Musab Alturki(https://www.youtube.com/watch?v=Av74vZRXeKo&t=71m00s)** said we are reaching a state where we have more complete case specification of the Phase 0 steps. Hope to have something there by the end of the week. This is to be followed by building the testing framework and making sure that all the tests pass. Updating specs to 0.8.2. Deposit contract generally complete other than a couple of negative conditions that need to be verified.

## 5. [Spec Discussion](https://www.youtube.com/watch?v=Av74vZRXeKo&t=72m58s)

**Joseph DeLong** discussed Interop. Originally said to be there at 3:30. They will end up doing waves of vans to take everyone out to the cult's headquarters. Will set up an Interop telegram channel to do a call on 8/16.

Event will be the 6th to the 13th. Don't need to bring food. It's catered for about 45 people. There is a cabin that supports 30 people. There are additional cabins with extra space for 10-15 people. RSVP so you don't starve to death. Antoin will organize the technical portion of what they're doing. If you have a particular accommodation you want, let them know.

**Diederik Loerakker(@protolambda)** talked about gamifying test nuts doing an NFT for participating in the deposit contract. If anyone is in Berlin, reach out. Conversation about fuzzing, where there are no real new developments.

## 6. [Open Discussion](https://www.youtube.com/watch?v=Av74vZRXeKo&t=80m10s)

None. Next meeting will be in two weeks time.

## Attendees

- [Adrian Manning (Lighthouse/Sigma Prime)](https://github.com/AgeManning)
- [Alex Stokes (Lighthouse/Sigma Prime)](https://github.com/ralexstokes)
- [Ben Edgington](https://github.com/benjaminion)
- [Carl Beekhuizen (EF/Research)](https://github.com/CarlBeek)
- Cayman
- [Cem Ozer](https://github.com/cemozerr)
- [Daniel Ellison(Consensys)](https://github.com/zigguratt)
- [Danny Ryan](https://github.com/djrtwo)
- [Dmitriy Ryajov](https://github.com/dryajov)
- ericsson
- [Felix Lange](https://github.com/fjl)
- [Hsiao-Wei Wang](https://github.com/HSIAO-WEI)
- [Jacek Sieka](https://github.com/arnetheduck)
- [Jannik Luhn](https://github.com/jannikluhn)
- [Jonny Rhea](https://github.com/jrhea)
- [Joseph Delong](https://github.com/dangerousfood)
- Justin Drake
- [Kevin Main-Hsuan Chia](https://github.com/mhchia)
- [Mamy Ratsimbazafy (Nimbus/Status)](https://github.com/mratsim)
- [Marin Petrunić](https://github.com/mpetrunic)
- [Matt Garnett](https://github.com/c-o-l-o-r)
- Mehdi | Sigma P
- [Mike Goelzer](https://github.com/mgoelzer)
- [Mikerah](https://github.com/Mikerah)
- [Mikhail Kalinin (Harmony)](https://github.com/mkalinin)
- [Musab Alturki](https://github.com/malturki)
- [Nishant Das](https://github.com/nisdas)
- Nicholas (Hsiu-Ping)
- [Shahan Khatchadourian](https://github.com/shahankhatch)
- Terence Tsao (Prysmatic Labs, @terenc3t)
- [Trenton Van Epps](https://medium.com/@trenton.v)
- [Vitalik Buterin(EF/Research)](https://vitalik.ca/)
- Weather Cam
- [Will Villanueva](https://github.com/Williamcvillan5)
