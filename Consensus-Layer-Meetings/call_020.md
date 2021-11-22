# Ethereum 2.0 Implementers Call 20 Notes
	
### Meeting Date/Time: Thursday June 27, 2019 at 14:00 GMT
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/51)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=Y8rhSbtY-Pg)

Moderator: Danny Ryan
Scribe: Brett Robertson

## NOTE

**NOTE 20.1**: January 3rd, 2020 is not a deadline for the implementation of Ethereum 2.0 Phase 0. 

## Action Items

**Action Item 20.1**: Danny Ryan to review the [wiki](https://hackmd.io/UzysWse1Th240HELswKqVA) and provide feedback of where it is best placed to live.
**ACTION 20.2**: Look at the options for funding the testing of libp2p in the Ethereum 2.0.
**ACTION 20.3**: Danny to engage with Diederik to move all discussion to Discord.
**ACTION 20.4**: Diederik to raise an issue in the spec test repo regarding Graffiti use-case in testing.
**ACTION 20.5**: Danny to raise an issue in the Ethereum 2.0 PM repo regarding what the minimum requirements will be to be production ready.


----------

Testing Updates
Client Updates
Research Updates
Network
Move to discord
Graffiti in testing
Spec discussion
Open Discussion/Closing Remarks

# 0. Welcome
[Timestamp 0:35](https://youtu.be/Y8rhSbtY-Pg?t=35)

**Danny**: This is the last call before the Phase 0 Spec Freeze. We are working hard on the last few PRs that we want to get in. In general the intention here is to be feature complete, to be clean and to have it stable for implementers, auditors, verification people, fuzzing, etc. 

Obviously the 3 out of the 4 of these groups is to find issues. So if there issues are found then they will be graded according to severity. Relatively minor bugs we will release minor releases. We will continue with the testing efforts. So we will be releasing v0.8.0 P.1 T.2 if we incrementally on testing and not substantive things. Just increasing the test vectors real. The increase in test vectors may find some minor bug which we will fix and release as a minor version. 

On the audit and formal verification stuff there might be some structural stuff that come up. There might be some deeper change where maybe some additional abstraction is warranted for X, Y or Z. We will deal with those on a case by case basis as they come up, potentially releasing as a major version if it is small, isolated and worthwhile getting out. Or we may pile up a few of these and after a long run of feedback, maybe on the 3 or 4 month time horizon, we would do a fairly major version bump. But again I don't know what those are because we have not found them yet. So we will address them as they come.

I would like to thank everyone who has contributed to this Spec Freeze. The amount of people involved has been pretty awesome and unbelievable. If you do find any issues please keep contributing and fixing them up stream. 


# 1. Testing Updates
[Timestamp 3:09](https://youtu.be/Y8rhSbtY-Pg?t=189)

**Diederek**: [PR #1206](https://github.com/ethereum/eth2.0-specs/pull/1206) is open and it hopes to complete the Spec-Test coverage hunt. There are two open issues remaining;

1. For how we formalise the finalization.
2. How we deal with the bit field.

Basically it is how we represent data and we hope to complete both these edge cases soon. All other tests are complete. So we should get a much higher coverage of the spec.

**Danny**: Good, will there be much more test vector coverage in the coming release? I believe there is still fuzzing of py-spec and the go-spec on going?

**Diederek**: It is still ongoing. We have been trying to improve how we move on from the initial set of states to a more diverse set of states. The difficult thing here is it is not like a virtual machine where there is many different input states. The input states are relatively sparse cause there is all these inference that have to be met by the states. So what we do is maybe create input states but then first block changes and then we continue from there. So it expands and expands the output states. 

The difficult thing here is to limit it in an intelligent way and not overflow this prestate collection. We want meaningful states.

If you are interested in this please join the telegram chat or the [gitter channel](https://gitter.im/ethereum/sharding?utm_source=share-link&utm_medium=link&utm_campaign=share-link).


# 2. Client Updates
[Timestamp 6:03](https://youtu.be/Y8rhSbtY-Pg?t=363)

## Trinity 
[Timestamp 6:10](https://youtu.be/Y8rhSbtY-Pg?t=370)

**Hsiao-wei Wang**:
* We joined the Python Team's Retreat. We discussed and played around with the new Python libraries. 
* We plan to migrate to [python-trio](https://github.com/python-trio/trio) which is another Python synchronised library.
* The primary reason for this is because Alex has a huge PR folder of v.0.7.1 and also since the spec freeze is coming we plan to bump to version 0.8 altogether. 

## Harmony
[Timestamp 7:22](https://youtu.be/Y8rhSbtY-Pg?t=442)

**Anton**:
* We have updated our client to the latest spec 0.7.1 and have included ssz union.
* We have done some quite small tests from github and our benchmark shows no significant performance changes since spec 0.6.
* We are working on libp2p minimal implementation.
* We are going to add persist to our client.

## Lodestar 
[Timestamp 8:33](https://youtu.be/Y8rhSbtY-Pg?t=513)

**Cayman**:
* We have been building out a few last pieces of the client. Things like;
* Getting a valid ETH 1.0 data for creating a new block. 
* Getting our deposit processing working with the real Merkle Tree. 
* Getting a real sync between the network and the chain going. 
* Still in the process of moving to spec 0.7.1.
* We are working on getting a benchmarking chassis setup.

**Danny**: Last time you mentioned you were still working on getting some assembly script working. Is that still on the horizon?

**Cayman**: Yeah, we have a rough implementation of the LMD Ghost. We have not integrated it yet. It is still in a PR. And we are also thinking about rewriting SSZ with assembly script. The blocker there is a SHA implementation. It will take a little bit of time but we are still working on them as a priority.


## Prysmatic
[Timestamp 10:36](https://youtu.be/Y8rhSbtY-Pg?t=636)

**Raul**: 
* We are passing all the 0.7.1 spec tests except for one final one that we working on today. 
* We finished our Go SSZ - passing all the spec tests.
* We are going to be fixing up every part of the run time so that it matches all the core changes so that we can optimise benchmarking and improve the client itself. 
* We have spent a bit of time transforming the heximals because they use binary data instead of heximal base 64. 
* There have been quite a few hiccups based on this but things are good now. 
* We put together a central repo for [Ethereum 2.0 API schemas](https://github.com/prysmaticlabs/ethereumapis).

**Preston**: 
* The goal here is we just wanna get some feedback and collect together these API schemas so that people wanting to build on Ethereum 2.0 have one place to go to. 
* This could go into upstream or into the spec repo or live here we don't really have a preference. 
* Primary purpose is to get feedback on this idea.

## Artemis 
[Timestamp 12:18](https://youtu.be/Y8rhSbtY-Pg?t=738)

**Johnny**:
* We have upgraded from v5.1 to v7.1 of the specs in 5 days.
* Working on stuff with deposits and tweeking that.
* Incorporating some feedback from the hobbit spec. A lot  of credit goes to Dean and Rene for agreeing to rewrite the spec.

## Parity
[Timestamp 14:16](https://youtu.be/Y8rhSbtY-Pg?t=856)

**WeiTang**:
* We updated to v7.1 tests, we were happy to see the bug fixes allowing us to remove our work arounds.
* We fixed our IRIS in rocksdb so it is more stable. 
* We did a major overhaul for our binary Merkle library which still has not been integrated.
* The substrate network stack is still in the works.

## Lighthouse
[Timestamp 15:18](https://youtu.be/Y8rhSbtY-Pg?t=918)

**Luke**: 
* We are passing all of the 0.6.3 tests.
* We have decided not to keep up to date with the 0.7.1 and we will wait instead for the spec freeze and jump to that one.
* Because the Spec Freeze is happening we have started to do releases and we are targeting a 0.0.1 release of Lighthouse next month which of course remains for developers and researchers.
* So instead of focusing on moving all the spec updates to 0.7 we have instead been working on things like the reduced tree fork choice which was discussed at IC3 and we are already seeing some good speed improvements with that at around 5x faster than our previous implementation without any significant overheads which is great but we don't have any direct benchmarking to show that yet, so you should expect that soon.
* Networking front we are making great progress with our libp2p implementation especially Discovery version 5. We are proud to say we have Discovery version 5 running in Lighthouse doing discovery but it just an initial implementation for our purposes and it is not the full spec yet.
* We have been having a chat with the Apache Milagro maintainers and we will start pushing some fixes up to them as this is our core DLS library.

**Danny**: On the Discover v.5 are you doing the advertisement or topic discover yet or just base?

**Adrian**: Just base discovery.

## Nimbus
[Timestamp 17:16](https://youtu.be/Y8rhSbtY-Pg?t=1036)

**Mamy**:
* We have move of 0.7.1 implemented.
* We have also updated the Test Suite to the official test vectors for DLS shuffling and the integer part of SSZ. 
* We are focusing on performance for the upcoming weeks. 
* Implementing SOS style SSZ to enable the rest of the official tests.
* We will start refactoring the state transition because with 0.7 we have names for all the state transition functions like process_slot, process_block and things like this.
* Because of this we will refactor the mocking part of the test suites like mocking blocks and state.
* We also continue working on the sync library because we forked the Nim sync library and we added add more functions for P2P networking.
* We also launched a libp2p daemon based testnet last week and so we are now Testnet 0 based on RPX and Testnet 1 based on libp2p. We will do a blog post within 2 weeks from now explaining how to install everything. We are still ironing out some details.
* We have an Ethereum 1.0 watch contract already. We did encounter some issues with log filtering and some RPC methods that are not intuitive on Ethereum 1.0.
* Our other team over at Status now have a lot of interest in Ethereum 2.0 now that it is being stabilized. 
* Jacque Wagner the main dev of Vyper started to use NIM as an EWASM contract generator. See [Thread](https://discuss.status.im/t/nim-contract-language/1249).
* NIM might come with official EWASM facilities. 
* We are starting to talk with the Embark team at Status so that each team knows what the challenges are for developing dapps on Ethereum 2.0.

## Yeth
[Timestamp 20:35](https://youtu.be/Y8rhSbtY-Pg?t=1235)

**Dean**:
* No real updates. Once the once the spec freeze occurs I am gonna catch up to 7.1 faster than Artemis.

## Formalising the Beacon Chain in K Framework.
[Timestamp 21:27](https://youtu.be/Y8rhSbtY-Pg?t=1287)

**Daejun**: We started about a month ago. We have been trying to understand the rationale first and are only now starting to model it in K Framework. 


# 3. Research Updates
[Timestamp 24:01](https://youtu.be/Y8rhSbtY-Pg?t=1441)

## Phase 1 
[Timestamp 24:12](https://youtu.be/Y8rhSbtY-Pg?t=1452)

**Vitalik**: 
* I wrote up a small, incomplete (checklist)[https://github.com/ethereum/eth2.0-specs/issues/1211] of things we will need to decide on changing for Phase 1, these include:
1. Shard Block time - will it be the same as a Beacon Block time, or half or quarter or something else?
2. Size of Beacon Block
3. How the Cross Link Data works
4. Consider removing the attestation list and having one attestation object or at least pushing from the one attestation object into the header. The reason being that I am not convinced there is a need to have space for more than one attestation because the things we are using these shard attestations for is much less than the equivalent for beacon attestations.
5. A couple of smaller other ones.
* If anyone wants to take a look at that list.
* Once Phase 0 is frozen then we will want to move full steam ahead to get Phase 1 finalised. So this would be definitely good to start looking at.

## Phase 2
[Timestamp 26:24](https://youtu.be/Y8rhSbtY-Pg?t=1584)

Vitalik: 
* I have been talking with Ethereum 2 Researchers to try and understand now fee markets would work.
* Some of the issues around batching transactions to ensure this is censorship resistant.
* How to ensure we get the efficiency gains from Batching and so forth.
* The concrete possible changes to the execution environment or basic phase 2 spec that would seem more likely.
* One of them is to ensure that you can have multiple top level transactions in one shard block.
* One of them is allowing larger execution environment states for example you could have 32 bytes but could go all the way up to 32KB. 
* The upper limit being something that is still small enough to fit into a beacon block for a fraud proof. 
* But otherwise it can be larger and being larger it has a lot of some really nice benefits, for example:
1. You can have some level of proof batching happen between blocks. 
2. You can have multiple transactions where merkle proofs get created independently get included without either of them breaking.

## Ethereum Research 
[Timestamp 28:30](https://youtu.be/Y8rhSbtY-Pg?t=1710)

Vitalik: 
* Karl has been doing some wonderful thinking where you take plasma ideas and applying them to an Ethereum 2 context where data just gets published on chain. 
* And it turns out you can do that to do some really nice things, for example:
1. Do cross shard transactions much more easily. 
2. Improve efficiency. Theoretically in the normal case you will note even need to publish Merkle proofs into the chain.
3. If you stand shard block times at a protocol where validators predeclare when the are going to make a shard block very soon then you can achieve an extremely fast defacto confirmation times for any application. Even if the individual shard block times are still longer like 4 or 8 seconds etc.
* I am really excited about this as it lets us create a user experience equivalent to all these other more centralised platforms without the need to be more centralised.
* So Yeah!


[Timestamp 30:06](https://youtu.be/Y8rhSbtY-Pg?t=1806)

**Justin Drake**: 
* Vitalik and I were at ZCon and there is some excitement for this new curve called DLS12-377. 
* It is similar to DLS12-381, it has the same embedding degree of 12 but a slightly different bit size with 377. 
* The reason for the excitement is because you can do efficient snark proofs about snarks. 
* You have this one level of recursion that is not like an infinite recursion at least one level.
* You can also do efficient snark proofs about signatures.
* One of the things we were considering was whether or not we should move to this new curve which has this interesting property. 
* The bad news is that DLS12-377 is a bit more than just changing parameters and constants.
* So there is a little bit of work to take the existing implementations and port them over.
* The other downside is that it has a cost in terms of Hash to G2. So that becomes a bit more expensive.
* So at this point in time pragmatically speaking we will stick with DLS12-381. Which has more maturity, more infrastructure and more testing.
* By sticking with DLS12-381 we can also meet the DevCon suggestion of launching the deposit contract during a public ceremony.
* It will be interesting to see how this space evolves in the future because it is mind boggling how much improvement we are seeing over time. And I would not be surprised if there are new suggestions that come up this year and next year.
* Maybe during Phase 1 or Phase 2 we can evaluate a change to a new curve but I say in the short term stick with DLS12-381.

**Mamy**: The community may be fragmented between standardisation on the 381 or 377, right?

**Justin Drake**: Yes, one of the things that needs to be done with regard to the standardisation effort is that everyone is on the same page. It seems that of the other 10 or so blockchain projects that would want to launch on such a curve. We are the first that want to deploy the deposit contract. 
* Ethereum does have a bit of weight in this space and momentum. The fact that do we go ahead with DLS12-381 may be enough of an incentive for others to come in. 
* One of the things that was voiced during the standardisation meetings was that other people also want no fragmentation and cohesiveness.
* We will see what the next meeting in just under two weeks comes up with.

**Vitalik**: That does sound like at some level there will be some form of fragmentation especially going further into the future. Whether someone wants it or not. Because if we expect to find curves that have better and better capabilities and we will find one that has a full level of recursion with pairings and one that has two levels of recursion. Eventually someone may find a cycle or a more efficient curve with a cycle.
* So there is definitely a high probability that we will need to prepare for an Elliptical Curve World that will a bit messy for the next decade or until quantum computers come and nuke the whole space.

**Justin Drake**: So one of the things we are trying to do with the standardisation effort is to have the notion of a cypher suite or basically a little bit of metadata which specifies which curve you are using and which hash function.
* This will be a good test of the robustness of the cypher suite. How well does it work with the existing curves that we know of.
* The IETF standardisation effort is not just for the blockchain project so that will be interested in standardising all of the meaningful options. 
* This is good news for us because it means we have some level of preparedness in this possible messy world of lots of different curves.

## [EIP-2028](https://eips.ethereum.org/EIPS/eip-2028)
[Timestamp 36:34](https://youtu.be/Y8rhSbtY-Pg?t=2194)

**Leo BSC**: I have been contacted by the Starkware team. They have shown some interest in working with the simulator.
* The idea would be to study how various network parameters are affected by block size.
* This is in the context of the Ethereum Improvement Proposal [EIP-2028](https://eips.ethereum.org/EIPS/eip-2028). 

## eWASM
[Timestamp 37:13](https://youtu.be/Y8rhSbtY-Pg?t=2233)

**Alex**: We have recently released a tool called scout.
* This is a black box prototype environment for phase 2 execution.
* It uses WASM internally.
* It was based on Vitalik’s Phase 2 Proposal 2. 
* There is an EthResearch [Post](https://ethresear.ch/t/phase-2-execution-prototyping-engine-ewasm-scout/5509) introducing Scout and giving some background.
* The code itself can be found at [scout](https://github.com/ewasm/scout).
* For the black box is most of the Phase 0 and Phase 1 stuff accepted as required.
* It is a tool that operates on a YAML test file. 
* It can execute execution environments using that YAML test file. 
* The shard blocks and WASM code can be defined for the execution environment.
* The main goal with this design is to quickly prototype features in execution environments and be able to benchmark those features.
* Initially we have implemented a couple of different execution environments with different basic functionality.
* We do have: 
A scout verification that is integrated with socrates.
We do have DLS signature verification.
Some code for a token contract samples.
* All of these are nice to prove that all these features can be implemented and applied to WASM.
* But at the moment we are focusing on the more important questions: 
The speed of the WASM code; and
The throughput of what the execution environments have to do.
*  The key part execution environments have to work on is that they have to get a witness first state and they have to verify that witness and then they need to apply the changes on it.
* First goal right now is prototype these witness verifications.
* One way to do that is using SSZ parcials. We don’t have that implemented yet but that is one of the next steps. 
* The main outcome we are hoping to get out of this witness benchmarking is to prove that a stateless model is the right direction and that is the first thing we have to prove.
* As mentioned this black box is pretty much everything from Phase 0 and Phase 1 because whilst we don’t need it for benchmarking we do need it on proper infrastructure to test execution environments.
* As part of testing it would be nice to have this functionality implemented into a proper Ethereum 2.0 client.
* And such a client would also need to implement a lot of the Phase 1 spec. 
* As well as whatever is needed based on this phase 2 proposal.
* The EWASM team is working together with the Quilt team.
* It would be nice to have the execution on the testnet at some point to have proper hands on experience with execution environments. 

## Quilt
[Timestamp: 41:49](https://youtu.be/Y8rhSbtY-Pg?t=2509)

**Will**: I worked on a [wiki](https://hackmd.io/UzysWse1Th240HELswKqVA)
* This covers a lot of the glossary terms, a lot of the material, a lot of the different conversations and basically consolidates all the info on Phase 2 in one spot. 
* I would like to get this on to the Ethereum Github wiki but I am not sure the best place to put it up.

** **
**ACTION 20.1**: Danny Ryan to review the [wiki](https://hackmd.io/UzysWse1Th240HELswKqVA) and provide feedback of where it is best placed to live.
** **

**Will**: We have been collaborating with the EWAM team on various things.
* We are trying to support scout. 
* We have been working on implementing SSZ partials and rust and helping in that effort.
* We have dived into the theory and ideas behind the relay market based on the discussion in EthResearch. 
* We are looking to get a Phase 1 testnet up that can support a certain number of shards that we can integrate scout into and have a basic execution engine from that, so that we can have playgrounds with execution environments.
* This is so that a number of assumptions can be tests and explored.
* We are in a transitory phase so we will have an official roadmap here soon.
* On the next call there will be a couple things that we will be looking to expand on and dive into.

## Pegasys Research
[Timestamp 44:55](https://youtu.be/Y8rhSbtY-Pg?t=2695)

**Pegasys**: We expect to have a new update to the paper out in August.
* We are looking at how to use rollups for Ethereum 2.0 on a way to execute transactions on any shard from any rollup.
* We are going to look at a simple case first which is transfer between rollups and we have one proposal ready and we are going to discuss that with Barry Whitehat next week to see where we can merge efforts.

## Protocol Labs
[Timestamp 46:12](https://youtu.be/Y8rhSbtY-Pg?t=2772)

**Danny**: We have a couple guys here from Protocol Labs.

**Mike Goelzer**: We have no updates on Grants yet. We are very close to making a couple of grants. Some in conjunction with other funding sources. Some on our own. 
* So we will probably have an announcement about that sometime next week. 
* Both are focused on building libp2p implementations in the languages that all the current client implementations need.
* We are hoping they will bear fruit by September when we need them.
* Last call we had a question “What security is being provided by TLS vs what the application layer will need to provide?”
* Assuming that is a correct question:

**Raúl Kripalani**: Transport Level Security is necessary to, first of all, not be subject to [Man in the middle attacks](https://en.wikipedia.org/wiki/Man-in-the-middle_attack). 
* That could potentially alter the payload that is being transported.
* To be able to authenticate the peer that you are interfacing with.
* If you have for example a public key for that peer then when you authenticating them when you are establishing the connection you are handshaking and are able to certify that you are really speaking with them.
* Of course, encryption is necessary as well at the Transport Layer. for all kinds of reasons including to avoid upserverability and censorship etc. 
* If the application itself needs to use crypto primitives to sign for example specific pieces of data by specific roles or nodes on the network, check validators and so on then you could imagine where you have a piece of data transaction instead of a log or collision or whatever that is signed by a particular validator and that message is gossiped through the network.
* As it is being gossiped through the network Transport Layer Security would be making the actual transmission of that message secure between peers.
* But those peers would need to verify that the origin of that original message is actually the validator they would expect it to be.
* That would be an application of a signature for example.
* The one does not exclude the necessity of the other.
* There are two reasons why we want to adopt TLS 1.3:
The first is that it is a prerequisite for quick(sp?).
Adopting TLS 1.3 would help a lot with censorship resistance. 
* When HTTP/3 is deployed you can easily imagine a transport that mimics HTTP/3 by using quick TLS1.3 over port 443 for example. It would therefore be very difficult for censors to block traffic or do any unpack and inspection.
* Of course they can always block IP addresses.
* The libp2p stack is designed for plugability at the security level, at the secure channel level. Which means that algorithm another approach another secure channel that we are looking into is [noise](http://noiseprotocol.org/noise.html).
* We have some experiments in this area.
* We will probably be funding a team to implement primitives that are lacking the Javascript environment to be able to conduct noise in not user land essentially.
* Basically we are looking at a system that can conduct the IX or IK handshake based on what we have available. 

**Danny**: Does noise provide some clear benefits over secio?

**Raúl Kripalani**: It does.
* One of the clear messages that I am excited about is that it allows us to send push data on the first message.
* As the handshake is being completed or going through the different steps any push data or any accessory data that is conveyed in any of those handshake messages acquires different levels of security based on the state of that handshake. 
* On an IX handshake for example the first initiator message to the peer that accessory data or push data would be plain text. 
* But if the other peer wants to push back any data then on that response because there is enough cryptographic material to secure that push data it would be right.
* It makes this very elegant.
* DLS 1.3 also provides this ability but for example in Go I don’t think that Go SDK is capable of sending zero round trip data yet. It should be on the road map but noise does already.
* There is also a variant of quick as well that accepts noise for its handshakes as well. 
* So I do see some very interesting developments there and major adoption from projects that have important reputations.
* So I am pretty confident in this.

**Danny**: So is this relatively mature or more mature that secio or widely adopted?

**Raúl Kripalani**: I would say that secio was necessary in the early days of libp2p but we definitely want to move away from secio. That is to say it is pretty trivial to implement. 
* For a baseline interpretability cross libp2p implementations you will want to implement secio because this is what all libp2p implementations support.
* Not all programming languages support DLS 1.3 yet. 
* So that is something against the state of DLS 1.3 at this point but there is practically a noise library for every language out there.
* It would make for a very good second baseline encryption mechanism.

**Mike Goelzer**: secio has as of right now not been security audited that will probably change by the end of the year. 
* noise has however gone through a formal verification.
* DLS 1.3 is an IETF standard. 
* So there is that to consider as well.

**Zak**:  Users will be able to choose which implementation that they would like right? 

**Raúl Kripalani**: Correct. 
* In parallel with all of this there is a re architecture of multistream .
* Right now the selection of the encryption channel is being conducted in plain text - which is not great.
* But it does allow for that pugability so peers negotiate on what secure channel they want to adopt for that connection. 
* This will probably move to the multi adder as a component.
* You can imagine a multi adder IP4 address / tcp / port number / secio or noise IK or DLS 1.3
* That would allow peers to directly initiate a secure channel without having to conduct any plain text negotiations out in the open which makes the system prone to unpack and inspection. 

**Raúl Kripalani**: Libp2p would be implementing and adopting the SDK library in each language.

## Testing Ethereum 2.0
[Timestamp 57:35](https://youtu.be/Y8rhSbtY-Pg?t=3455)

**Jonny**: What do we need to do with regard to testing to ensure the libp2p and lib-gossip protocol are production ready? The timelines for Ethereum 2.0 may be different form libp2p and so I was wondering if there was going to be Grant to assist with this testing?

**Mike Goelzer**: There are two aspects of testing:
Interoperability testing between the different languages
* This is an area we are very interested in making a Grant. We have a rudimentary system call IPTV which we think could orchestrate interoperability tests but we would need someone with time to turn it into a property interop test suite. Which could also be used to validate the particular libp2p implementation depending on the requirements.
The other side of testing is production readiness testing basically integration tests of the whole system to get data on performance and longevity tests that you are running to see if it falls over or not.
* For that we have built a system that we call [testlab](https://github.com/libp2p/testlab/). 
* Basically it is an orchestrator built on top of nomad. What it does is spin up a large number of libp2p nodes (like 1000 and could probably go beyond that.)
*  That is our plan for testing real world production scenarios. 

**Jonny**: What is performant for some many not be performant for others. What would be nice if we could do a sweeps on things like message rates, packet size, bandwidth limitations, like how fast we need actual gossip messages to propagate through the network. Just so that we are aware of where things breakdown because there is always options if something needs to be tweaked we can fix it. I feel for Ethereum 2.0 we should really focus on that. Is that something you would have funds to work on as well?

**Mike Goelzer**: I guess we would be open to funding something in that area. We have started out with the idea that we need to support language implementers first or people fixing deficiencies in the languages. 

**Danny**: The EF is also interested in funding such work. Let’s take this offline as there are a couple proposals under evaluation and we are trying to work out the best way to move forward.

** **
**ACTION 20.2**: Look at the options for funding the testing of libp2p in the Ethereum 2.0.
** **

**Jonny**: It makes sense that that Protocol Labs would want to do the interoperability testing first but we have a deadline of January 3rd. Offline perhaps we can discuss how everyone feels. Realistically can we play out with these tests with a long running testnet? How realistic is it, really? Is January 3rd, realistic?

**Danny**: January 3rd was a suggestion that is a nice target but is not a deadline. I would not want people to believe that this is a hard and fast date as there is a lot of things that are being juggled right now and a lot of smaller things that need to be completed before then with too many unknowns. We would like to do it quickly but more importantly we would like to do it right.

**Justin**: We are more interested in the idea that we will not launch around the December holidays but anytime after January 3rd is a realistic possibility. What I have done is survey some of the implementers to as them if they would be production ready for a launch in January 3rd, 2020 and two client teams have responded positively. 
* At the end of the day we only need two clients to be ready to go live. And we will see how the landscape evolves organically over this time. 
* For sure I am not expecting the majority of the clients to be ready by the end of 2019.

**Jonny**: What do we define ready as? Are we saying there will be a 3 month long multi-client testnet starting in September so that we can sort out any bugs that are found? This would mean that we would be running flawlessly for during this time before we go live and I am not sure this is probable. 


# 4. Network
[Timestamp 1:07:13](https://youtu.be/Y8rhSbtY-Pg?t=4033)

**Zak**: We have been working with Prysmatic and three other teams. Rene has been working on implementing hobbits. 
* We are planning on doing an impromptu meeting in Toronto next week for anyone that is around. I think it is going to be Preston, Rene, Dean, Greg and the Chainsafe guys, Antoine might be joining us as well. 
* If anyone else is interested we are going to kind of start working out some of the networking stuff and try to come up with some sort of a loose specification for what that stack is going to look like. 
* Next we will move on to do some research in terms of data sync and peer discovery etc. 
* If anyone would like to join us please do we will be in Toronto next week.

**Rene**: As Jonny mentioned we have a few updates to the [hobbit spec]( https://github.com/deltap2p/hobbits/pull/15) that largely came out of the conversation with Prysmatic. Any feedback on this is welcome.


# 5. Open Discussion/Closing Remarks

## Proposal to move all discussion to Discord
[Timestamp 1:08:43](https://youtu.be/Y8rhSbtY-Pg?t=4123)

**Danny**: Greg from Chainsafe suggested that we move proposal to discord. Primarily we have discussions in two or three Gitters. Then there is fragmented Telegram communications and emails and things like that. The proposal is to have a more unified place to talk. 
* The main downside is that it is harder to come in and ease drop as you do need to create a username and log in. 
* The main requirement from me is to bridge the current sharding in Gitter to the general room on the discord.
* Otherwise it seems people are otherwise very positive about this. 
* Is anyone not?

**Vitalik**: I like bridges too. I had a bridge to Telegram. 

**Unknown**: Bridging to telegram is a real positive. As it means a lot of people don’t need another messaging app.

** **
**ACTION 20.3**: Danny to engage with Diederik to move all discussion to Discord.
** ** 

## Graffiti use-case in testing
[Timestamp 1:10:40](https://youtu.be/Y8rhSbtY-Pg?t=4240)

**Diederik**: The idea here is that you can use this one field that can contain any data in the block body to use it for debugging during testing. 
* So you can put this metadata in it like what kind of client is running or producing the block where the client is located, for how long it has been running, etc. 
* And in so doing we can easily debug large amount of blocks. 
* What we need is to agreement on the same format.
* If would be worth collecting information from all the clients on what data they could want that would be useful for interop testing and then somewhat standardise it.
* It is primarily just for testing.

**Mamy**: Perhaps we can open an issue in the spec test repo and everyone can then contribute their ideas. 
* 32 bytes is large and small at the same time.
* For example IP addresses you need 4 bytes as a minimum and so we could run out of space.

**Diederik**: Yes we could have for example a client vendor, a time stamp, some statistics and an ip address. So that this is a set of 4 bytes each. So fitting in 32 bytes.
* Also the client version.

** **
**ACTION 20.4**: Diederik to raise an issue in the spec test repo regarding Graffiti use-case in testing
** ** 

**Danny**: Clearly there is a lot of discussion around figuring out the minimum requirements to be production ready. Some of this is a little fuzzy as there is still a lot of unknowns that we will encounter in the next 4-5 months but it is probably worth beginning to enumerate the knowns. Let’s create an issue in the Ethereum 2.0 PM repo and start a list and start the conversation from there.

** **
**ACTION 20.5**: Danny to raise an issue in the Ethereum 2.0 PM repo regarding what the minimum requirements will be to be production ready.
** ** 

## Interop Meetup

**Danny**: There is a meetup from the 6th to the 13th September. It would be good to get an RSVP out in the next couple of weeks to everyone so that they can respond and get it in their calendar as I believe there will be a cap and for planning purposes it would be useful to have things clarified to get things firmed up on peoples calendars.

**Johnny**: Invites are going out today. Three to four per team and the dates are set to the 6th - 13th September.

# 6. Spec discussion

None






## Attendees

* Aaron Beatt
* Adrian Manning (Lighthouse/Sigma Prime)
* Alex Beregszaszi 
* Alex Stokes (Lighthouse/Sigma Prime)
* Antoine Toulme (ConsenSys)
* Ben Edgington (PegaSys)
* Benjamin Bur
* Brent Allsop
* Brett Robertson
* Carl Beekhuizen (EF/Research)
* Cayman
* Cem Ozer
* Chih-Cheng Lia
* Daejun Park
* Daniel Ellison
* Dankrad
* Danny Ryan (EF/Research)
* Dean Eigenmann
* Diederik Loerakker/Protolambda (EF)
* Dmitrii (Harmony)
* Greg Mark
* Hsiao-
* Jacek Sieka (Status/Nimbus)
* Jannik Luhn (Brainbot/Research)
* Jim Bennett
* John Adler
* Jonny Rhea (Pegasys)
* Joseph Delong (PegaSys)
* JosephC
* Justin Drake
* Julien Bouteloup
* Leo (BSC)
* Luke Anderson (Lighthouse/Sigma Prime)
* Mamy Ratsimbazafy (Nimbus/Status)
* Marin
* Matt Garnett
* Michael 
* Mike Goelzer (libp2p)
* Mikerah (ChainSafe)
* Nate
* Nicholas(Hsiu-Ping
* Nicolas Liochon
* Nishant D
* Pooja Ranjan (Ethereum Cat Herders)
* Preston (Prysmatic)
* Raul Jordan (Prysmatic Labs)
* Raúl Kripalani (Protocol Labs)
* Rene Nayman
* Steven Schroeder
* Terence Tsao (Prysmatic Labs)
* Trenton Van Epps
* Vitalik Buterin (EF/Research)
* Wei Tang (Parity)
* Will Villanueva
* Zahary
* Zak Cole (Whiteblock)
