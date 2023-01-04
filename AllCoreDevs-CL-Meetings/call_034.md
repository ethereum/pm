# Ethereum 2.0 Implementers Call 34 Notes

 ### Meeting Date/Time: Thursday 2020/2/27 at 14:00 GMT

 ### Meeting Duration: 1 hr.
 ### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/129)
 ### [Audio/Video of the meeting](https://www.youtube.com/watch?v=tLiMgFoG_vs)

 #### Moderator: Danny Ryan
 #### Notes: Pooja Ranjan
 ----------

 **Danny**: Welcome everyone! 

 # 1. Testing and Release Updates
 
**Danny**: I'm a little bit behind. Eth Denver and then the flu has set me back a little bit. so I am behind on getting that release out that has some stuff that came out of Least Authority audit which we should be shared publicly very soon. As well as bunch of little thing that we've catching, specially on the network side  in the past few weeks. That should be on next few days should be a lot stable target. Post audit  target we're looking for.

Along with that, I believe that Alex from TX/RX has started or is starting on some Fork Choice test that has been working on from Java and the Pi spec. Hopefully some of that get out soon. In addition to that I did huge pass on the testing to get basic testing a place for phase 1,  which also involves doing some fun stuff to get testing working across forks properly in many cases. That PR is up and should be in soon. that's primarily it. Proto is there anything at your end?

**Proto**: During Eth Denver, I continued to work on networking repo. I hope to test client's networking functionalities, Disc V5, and RPC as well. Still working on testing, if the compression of RPC work so. It relates to the open PR, its how we do compression from object to training. Since the networking call move to next week, it may be good to talk to networking people as to this kind of feaure makes it into the next release. That's about it.

**Danny**: Cool! I think generally people have not care that much or have been positive in response, so I do want to get that out into the next release but if you feel strongly about it, now is the time or after the call in that PR, if you want to speak up. 

We don't have Mehdi, right?

**Adrain**: Yeah, Mehdi is not around but I can get an update on on the beacon fuzz, if interested. 

**Danny**: Yeah cool!

### Beacon fuzz

**Adrain**: We recently published a blog post that gives progress update, which is on our website. Main points are
 * found an interesting bug which is invalid within local proofs in Nimbus,that is patched.
 * Almost completed all the block processing state transition functions, I covered in the Beacon fuzzing. 
 * Remaining things are: process random and process Eth 1 data, should be done by the next update.  
 * Prysm successful integrated. We have to use a fork of Go. Go-fuzz build which allows us to use the shared library compilation and symbolic linking. But that has some issues because Nimbus also uses Go in their Go wrap around LibP2P.
 * Expect to have Prysm support in master by next week.
 * We've improved some of the tooling,so that we can programmatically generate corpus from the test repo, provided we give it a specific spec version which helps us build these things faster
 * We've got a better build process, so we've updated the make file.

**Next steps**
 * start including the epoch state transitions,
 * java integration and
 * updtae to Eth2 spec to v 10.1
 
 **Danny**: Thank you very much.
  
**Jacek**: I am a little bit surprised that you're adding Go on the fuzzing side?
 
**Adrain**: Are you no longer wrapping libP2P using native Nim.
 
**Jacek**: Oh! we're wrapping that but is libP2P part of the fuzzing?

**Adrain**: Yeah! the issue is using multiple Go different libraries.
 
**Jacek**: We shouldn't have Go as the part of the normal build. The NIM code shouldn't be tainted by Go. I an just surprised, we can take it offline. 
  
**Adrain**: Fair point. I will talk to you after. 

**Danny**: Cool! any other testing update ?
 
 
 # 2. Client Updates
 
**Danny**: Okay! Client updates.
I'd like to hear the details of what's been going on but also with an eye for multi client testnets,  in the coming month.I'd like to hear the biggest bottleneck,  what y'all are currently doing to address it and also if we should be probably seeing some similar issues across clients so if there are things to share if you back to each other, please chime in. We can start with Teku.
 
 ## Teku
 
**Meridith**: I can speak for Teku. So,
* we're making progress on sync
* we're connecting to and downloading blocks from Prysm Sapphire test net 
* we haven't yet caught up to chain head, we're working through performance and reliability issues that are slowing us down so there's more work to do, but exciting that we are downloading blocks from a live test net
* we have also been doing some work related to deposit processing. We should now be correctly processing pre and post genesis deposits 
* done some work on Disc V 5 implementation from Harmony to make integration with Teku easier. We've confirmed it works well enough to discover nodes from Lighthouse. 
* we've also been making progress we've also been making progress on our rest APIs
* focusing on APIs required by block explorers
* We've started working on an encrypted key store for local key management and and also stand alone and signing service for management of keys externally

**Bottlenecks**

* one issue that we definitely need to address is storage. We're using absurd amount of disk space right now.
* We haven't really started looking at optimizing this at all. Also if people have ideas that would be interesting 
* we floated some ideas about maybe using a tri-backed State Storage, so we store only disks between states or maybe state snapshot strategy where we only store like a few States and basically rebuild them as needed. If people have ideas about general storage schema, we'd be interested

Cem if you're online, I think you had issues related to Eth1 data management. I don't know if you want to speak to that?
 
**Cem**: Yeah I'm online. One problem we're having is while trying to process deposits efficiently, for that we want to use event logs instead of asking blocks and getting deposits in them when starting up Teku. However when we do that there is an issue of miss a Genesis block which might have a no deposits but any content stuff. So that's kind of like an edge case that we've been working on for like the past week but like I'm curious if any other clients have thought about that scenario or already fixed that. If anybody did fix it, I'd really appreciate knowing how they did it. so basically the issue is just like getting deposit events and using deposit events because otherwise it's just efficiently you're hitting the Eth1 node for each block after your contract deployment part basically. And being able to trigger Genesis on a block that doesn't have any deposit event due to its time stamp. Was that clear?
 
**Danny**:  Yeah, so is it the only block that you're aware of or those with deposit events?
 
**Cem**: Yeah!
 
**Danny**: So API is not available to give you just the existence of a block?

**Cem**: Mean just like one block.

**Danny**: Right.

**Cem**: Yeah it is definitely able to do that. In that scenario, we would be asking for basically each block after the Eth2 deposit block contract deployment block. That is very bad way to get all deposit events. I feel, there must be a better way to do it. 

**Danny**: I would definitely reach out to Paula after the call. I think he's been deepest in this.

**Cem**: Good idea, thank you! Any ideas for Meredith on reducing state size on disk?

**Proto**: Just after SBC, we've been looking into straight? How to reduce for Lighthouse? [Audio not clear] 
What you can do is store the fabulous state in a flat manner and you load it into the state. [Audio not clear]
We can take it after the call.

**Meredith**: Cool! yeah I think that makes sense.

**Danny**: Cool, thank you!

How about Trinity?

**Carl**: Before we move on, Meredith you mentioned that you're implementing a signing interface? Can you speak to exactly what you're implementing there or can you share the link to what that is ?

**Meredith**: Yes I'm someone actually dropped me a [link](https://github.com/ethereum/EIPs/pull/2335) to an EIp, let me find the actual specification.

**Carl**: Awesome, thank you!

**Meredith**: I'll find it and I'll drop it in the chat. 

**Ben**: Internally, we're calling it to sign up as a standalone signing as a service. If you look at the PegaSys Eth2 GitHub repo, there is Eth 2 signing repo, we've just started. Just now we haven't made a huge amount of progress just yet. It would be good to get some common interfaces on this stuff if anyone else is interested. 

**Carl**: Yeah I agree. It woul dbe really cool to have a common interface particularly if you want to support HSM for signing for the down the line.

**Ben**: Yeah, back end and front end interfaces for sure.

**Carl**:  Yup!

**Danny**: Cool!

## Trinity

**Alex**: Back to Trinity. Hey everyone things have been a little slow. 
* mainly just working on spec updates
* we have some work on stability of our pilot P2P Library 
* update to fork choice and some integration with Milagro

I really can't speak to bottlenecks like we've been discussing at the moment. I'd imagine we will have all the same issues as everyone else as this happens.

**Danny**: Cool, thanks!

## Nimbus

**Mamy**: We've lot of updates in past few week. 
On spec side, we're
* targeting 10.2
* created a (?) detection and a report on skipped tests because we realized that when factoring repos, sometimes we forgot to re-enable tests and sometimes it show up on fuzzing that should be catched up much earlier.
* We've BLS signatures implementation ready 
* so far we have been waiting for the new test Vector fixes but we go ahead the next week, because this is blocking implementation of (?) spec which is implemented except everything that touches BLS signatures. 
* We are WIP on attestation aggregation and fork choice 
* More than a year ago and we had the Bounty program to maintain Eth 1. We restarted this bounty program. 
* The first two bounties would be on improving test runners, so that can be used with Nimbus on HTTPS server, so that it can be used for correcting metrics and for Eth2 API. 

**Networking** 

* We've new code to manage peer lifetime.
* we have a significant focus on Discovery in the past 3 weeks
* we have some  issues on Windows, maybe NAT traversal 
* all of these issues manifest as finalization issues.

**Lib p2p2**

* Excellent progress on noise and  we are now looking for an interop testing candidate with our own active Lib P2P backend.

**Speed** 

* We have implemented a lightweight stack traces and this improves both computation and run time of Nimbus by twice. 
* Because we enable stack traces and they take significant toll on the binary because that prevents lot of compiler optimization. So this is a very welcome improvement.


**Dev Ops**

* Fixed all testnet deployment
* Because we sometimes add nodes that we're not reset every week and that caused issue. 
* Also we have specialized infrastructure to test finalization issues. I talked about discovering that manifest of additional issues but also when we have speed issues, like we have too many nodes on the same machine, the way we detect that is by finalization and we want to know if finalization issue come from- spec or speed or networking.  

**Eth1**

* Passed all the transaction test from Eth 1, same as Geth and Parity
* Other EVMC implementation done. 

**Next step** is 12 0 fuzzing evm implementation with the same tools as EVM 1

**Bottleneck**

* One of the major bottleneck that we have is Discovery to be able to connect with our test nets without  having to have use some bootstrap nodes.
* It's a bottleneck more for testing and debugging it's a log volume. Right now we create about 80 megabytes per hour of compressed logs. Assuming we grow to tens of thousands of nodes it would be impossible to manage by hands to debug. So we we need some kind of passer to deal with all of those. 
* For volume, we just rotates the logs every 4 hours to keep it's a manageable.

**Fork choice**

* One straight copy paste from the spec and one implementation from Proto array. The idea is to make it to almost to an independent module so that it's easier to fuzz.

**Testing**

* We use the same approach as Lighthouse which is to create some kind of interpreter that says okay push a block at another slots. Now run process slots and then now run a fork choice.

**Danny**: Got it. Anyone else running the issues with massive amounts of blocks and writing a custom and have any advice or thoughts?

**Adrain**: We kind of dump ours all into AWS and AWS consume it. That's not fancy to help there. But you did mention traversal? I want to ask, what kind of traversal techniques you're using? 

**Mamy**: It's mini uPNP.

**Adrain**: Cool, thanks!

**Ben**: Could I ask a couple questions? You mention spec V 0.10.2, this is not official release, right? what do you mean by this ?

**Mamy**: Sorry so it says 0.8.1. Maybe I was thinking of suspected then it was supposed to release. 

**Danny**: Fair enough. 

**Ben**: On the BLS as well, you mentioned you're working on test vectors on, is it the current state of the BLS standard because we know it's going to change a little bit more or did you implement the newer stuff as well?

**Mamy**: No this is the draft 5, so the one that is current and the vectors I am waiting for, it's the fast aggregator verify because some of the test vectors are expecting wrong signatures and actually correct. It's a problem that you raised.

**Ben**: Yeah, if you re-download the test repo that correct in the latest tar.gz [not clear].. Danny did not up. They change the version number on the test. So if you cashed it previously, they're wrong but the latest version is correct.

**Mamy**: Already? Okay, I will check it out.

**Danny**: I believe they're incorrect actually in the repo, in the code in the repo in the files but they are correct in the tar.gz right associated with it. Which was may be a confusing decision making, my apologies. 

**Carl**: Speaking further on the BLS front, as was mentioned that there's a new PR on the Hash-the-curve repo. We were supposed to have finalized BLS there, have been some complaint as to the efficiencies of this particular no power devices amongst few other things. SO, there's a new [PR](https://github.com/cfrg/draft-irtf-cfrg-hash-to-curve/pull/212), it only affect the hash to base, which is not called hash to field this is the first part of the ashing into the curve. It should be relatively minor change,  and the people seem very certain that this is the very final version. I think, it's worthwhile making the change to try avoid v2.  Until we launch mainnet, I think it's advisable to try and make changes to follow the BLS spec. I do really think that this is the final one. I think having spoken to these authors of the specs.

**Danny**:  The next step in the process is there is another kind of quarterly meeting.

**Carl**: Yes I would guess. So nothing came up at the last quarterly meeting, they were perceived issues. But this was something else realized internally. The quarterly meeting aren't enough when it's officially a standardized, it's more just to bring it out to the public as a point to get feedback on these kind of changes. so I guess maybe this is the result of the last meeting in some way around that way, but certainly was not the intention. 

**Danny**: Got you. Thanks

**Mamy**: You were talking about hash to curve being finalized but regarding the BLS signature itself which depends on hash to curve and use a separate spec how stable is it?

**Carl**: To the extent that I know, it is 100% stable so there is one minor caveat to that, well two actually, one is the external test vectors,  so much expect t ochange to add test vectors. As a part of some of the BLS pre-compile work I've been doing lately. Maybe we generated some test vectors  there. So, maybe we can we can leverage those. The other thing which may change is officially the spec, the draft expired or BLS because there hasn't been any changes to it for over a year now. So they would have to be I think a version bump I'm not exactly familiar with intricacies or versioning under these standards. There would be a version bump  but I don't expect any changes on that front.

**Mamy**: Thank you!

**Danny**: Moving on. 

 
 ## Prysm 
 
**Terence**: We've a bunch of updates. We're 

* working on slasher servers 
* a beacon node was able to detect surround vote and we're able to include the slashing object in the block.
* The next thing to verify is that slashing actually happened and the validator gets rejected. We're working on that.
* I am also working on better state management service. Where do we store state aka post finalized state
* Design is highly motivated by Lighthouse design, so props to them in being a pioneer on that.
* Implementation is mostly done just working on micro optimisation
* Few **tests** we are working on - Dynamic attestation subnet subscription, better concurrent block fashion for syncing. Also, how to use less memory doing initial syncing and 
* we also updated tester wait time from 1/3 to right away when he sees the block.


**Bottleneck**

* Today, basically we subscribe to all the subnet for the committee id 
* tons of aggregated signature to verify
* we've tons of aggregated signature to verify 
* I just put a profile before this call and it looks like 30% of all run time  we just put verifying on aggregating these signatures. Like Mamy said, that's not sustainable. We are working towards solving that

**Danny**: Thanks Terence! Anyone having comments for Prysm?

**Adrain**:  If you're subscribed to all the subnet what checks do you have for checking the other attestation before re-propagating on the cross gossip Sub

**Terence**: We basically implement watching the spec today which I believe it does check the signature. Basically checking the signature is the heaviest part, so that the debates whether you check the signature before you obligate.  I think, we do check the signature today. 

**Jacek**: Which block /state do you use?

**Terence**: We use the target state, I believe.

**Jacek**: Alright cool!

**Mamy**: For verifying signatures are you already using at everything is implementation?

**Terence**: We're not using the latest one, we're using the previous implementation. I think it is updated to version 10 which are not incorporated yet. 

**Jacek**: One more question, I was curious whether you cache the target epoch state or any epoch state or do you always load them from the DB before doing the checking.

**Terence**: So, we have for cache on top of the DB for the state so those  cache get hit pretty often-ish, given this is a target state and a we use a lot so yes it's cache.

**Jacek**: Alright, that's cool.

**Danny**: Anything else? Okay!
 
## Nethermind

**Sly**: We've 
* Libp2p (Mothra) wrap for that 
* working .net integrated into Nethermind Eth2 beacon node that can actually Gossip blocks between couple of local nodes. We've a thread of that working. 
* No attestation yet. 
* At version 0.9.1 of the spec or something
* It's good to have Mothra library, a quick leg up to get that started 

**Next Step**
* Try and update the version 10.1
* The changing things like getting rid of signing root.  I think will make it easier to finish off the rest of the stuff like attestation.

**Bottlenecks**
* We are behind other people. Prysm say 9.3 on the website, but I don't know if that's correct.

**Terence**: Yeah, they are still 9.3 on the testnet but then like our client actually runs 10.1. we just haven't  updated number yet.

**Sly**: That's cool so, I will probably try to get a 10.1 because things have some improvements over for the rest of the development. It will be good to try. Once I get in there, I'll try and get it working with interop  with one or the other clients and I met some guys from Teku who are locally in Brisbane but that's probably going to be my target. But I am happy to talk to some other people and get some interop working.

**Danny**: Thank you!

## Lighthouse

**Adrain**: Hey everyone, I'll try make it relatively quick. 

* Added two new developers. Welcome to Diva and Adam. You guys will be hearing from them very shortly in the near future. 
* We raised a 4k validator testnet for Eth Denver which turn out to be quite useful for some developers and research is to prototype with. It's been running for about 93,000 slots and we kind of haven't touched , it's just running smoothly. WE just had it as it is as a test for the Eth Denver hackathon. Our team met up with Proto and implemented the local Merkle Tree based storage system for validated field in the Beacon state. It's shown pretty significant reductions in tree hashing time but it increased during reward and penalties. We are still deciding whether to adopt the approach or not throughout the client. We did a project wide sweep of temporary heap allocation because we're finding a whole heap of using a ridiculous amount of memory, more than what we needed. 
* We actually reduced our memory footprint by out half again . So, since the start of the month right down to about quarter them up of what we were originally using. 
* We're still using a 2-4 GB of RAM for a Beacon node on a 100K validator test net but we still think we can probably get a little bit better than that. The RAM usage depends on how many validate is it using the nodes local API. The reduction of heap allocations and memory issues also gave us a 30% improvement in block processing in time which is pretty good so that also help us syncing space. 
* we're in the process of refactoring on BLS libraries, so that at compile time, you can choose to whether to use the Milagro or Harumi implementations.
* We still have to find out which is a benchmark , which is faster?

**Interoperability**
* This is kind of one of my main focuses in the very near future.
* We're pretty much in the process of upgrading Lighthouse to what we are calling on a version 0.2.0 and this is going to have pretty much be feature complete for mainet launch. So that means, it will include the attestation aggregation strategy, noise and (?) compression. So we pretty much have most of that implemented. There's still a bit of code to go but we probably need to go into a fair amount of testing before we move that to Master but once we have that merged into Master, we will be ready to do interop with everybody, we assume so. As soon as we get that merged down, we're going to start up an interop test net which will be a long lasting test net that we hope others can join. But we will also try and join other clients test-nets. 
* So the first thing is finishing off the testing of that.
* I guess the last thing is that we've kicked off a process to build a UI front end for our validator client and that's currently in like the research phase. So I probably will be updating everyone as that develops.

**Bottleneck** 

**Adrain**: Yeah, We have performance bottlenecks. But this is the RAM that kind of been targetting. I think we fixed and tracked down most of our deadlocks. In terms of  actually just getting to an interop  testnet and test with other clients. It's just a matter of finishing off the last bit of code thoroughly testing it internally before releasing a testnet because we don't really want to have a testnet and then realize oh we need to change something and restart the testnet.

**Danny**: You said that memory is scaling with the number of validators  using the local API, is that correct?

**Adrain**: Yeah

**Danny**: So the number of like local validators that are signing into the test should Beacon node?

**Adrain**:  Yes, we are still tracking down why that's the case? Why we're still getting memory fragmentation across there, that seems to be the case. 

**Danny**: But you also have nodes that has 1000s or 10,000s validators, that's sure?

**Adrain**: Oh yeah yeah. I'm in reality that's probably not going to happen but we have that in.

**Danny**: Can you give us any details on your strategy to find validators of particular attestaion subnets given? 

**Adrain**: As I was saying on that thread, the original plan was just to, so when a validator  kind of subscribes, we know in advance when it needs to subscribes to a subnet. so we have given ourselves a kind of epoch leeway. SO we know any epoch in advance, which subnet we kind of need to subscribe to. So,  the initial plan is to use Disc v5 and just kind of search for random pages and when will only connect to ones that have the subnet in our field, but failing that if that's too slow or if that doesn't give us results, it'll be dependent on the number of nodes on the network that are validators versus number of nodes just sitting there that aren't subscribed to any other subnets. The other solution which is what Alex suggested is to just crawl the DHT, which isn't very difficult but it will be a different kind of search where we just ask all that not all the other peers that they know about that have this particular field in and out and you can specify return me at least three of them and the query hopefully shouldn't take you long, definitely not an epoch I imagine. That's the second strategy, if we need it. 

**Jacek**: Have you thought about the reorg happening right then? 

**Adrain**: Yes, if reorg happens, the validator client will detect it because it kind of holds all the time for it's duties and so it will resend a subscription. So we have a service thats looking after all these subscriptions on the beacon nodes. So it will update and realize that it will change which subnets it need to connect to. SO if a re-org happen it will re-adjust itself. We may have less than an epoch in some circumstances like you validate it just connects any things to perform an attestation on the next slot. Well in those circumstances obviously not not gonna have enough time to track down peers. In a long-running scenario, we in principal should.

**Danny**: Something also to consider is that the attestation subnet subscriptions in ENRs are relatively stable on the order everyday. So, there's also the chance to pre-walk the DHT and the information that you think is correct, it was very likely correct, locked and loaded?

**Adrain**: So when you say the order of a day, that's the the random subscription you're talking about, right?

**Danny**: Those are the only ones that actually go into.  I believe what is it doesn't say if you're just joining for that epoch worth of duties that, I don't think you put it in the ENR.

**Adrain**: Yeah, I'll be shortly subscribed. Yes that make sense. So, the idea is that as long as the constant is the number of random subnets he's supposed to connect should recover all the subnets.

**Danny**: Should recover all the subnets, what do you mean? 

**Adrain**: Yeah I mean as long as they are based on the numbers of peers like if you have as long as at least a thousand validators, then it shouldn't be too difficult to find those thousands validate across any sub that you needed it. I guess, we will find that in practice.

**Danny**: Correct. Any question for Lighthouse?

**Cem**: I was curious which spec version you guys will go for testnet?

**Adrian**: I think I'll be going for 10.1. another quick thing is that we've  implanted noise and we're testing that. Nimbus said they needed a testing pattern to check out their noise, then that will be interesting to interop with.

**Danny**: Great!


## Lodestar

**Cayman**: Hello, in the past few weeks, we've 
 * upgraded our BLS implementation to  10.1 release and 
 * we've cut into a release of that based on Herumi implementation compiled to WASM
 * everything else in our repo still at 0.9 level 
 * we have some fork choice things that we are still upgrading in our our network.
 * I'd says it's probably a bottleneck at this point so we have noise implementation that were interoping with Go.  At the moment I don't know exactly the status is. so I don't want to offer us a testing partners, but I'm not seeing progress and 
 * we have a PR open for snappy compression and 
 * we are going to begin working again on disc V5. We're about halfway through and we had stopped work for a while and now we are going to get back to that. 
 * some other things, we emerged in this new SSZ implementation that we have been working on for a while and just merging it in. No changes, kind of speedup our position by roughly 10-100x and 
 * then just lightly memoizing a few functions speed it up another 10 - 100 and we'll probably  stop there for now because I don't not have liked the best data to benchmark against,  but I think once we start resyncing a bunch of blocks we'll have something we can test against and take a little further. 
 * We're also going to be working on fixing up our state management similarly to how to describes a few people earlier we're going to the store to checkpoint, historical States and then have a more rich history of the recent States kept in memory and sharing a lot of data between them.
 
**Danno**: Cool. Any particular bottleneck you want to discuss? 

**Cayman**: Maybe Disc V5 but started some conversations in a few other channels and I think it will get that sorted.

**Danno**: Great, congrats on the SSZ and state transition.

**Cayman**:  Thanks!

**Danno**:  Okay other client updates or items?
 
## 3. Research Updates
 
### TXRX
 
**Joseph Delong**: Sure. Okay, so yeah we are at Eth Denver and we worked with a feature and we made an EE. It was kind of rudimentary execution environment to see what some of the components are and we're using that to inform some research. Some of our team also helping quilt with Ease and we made some updates to that just last week.

**Ease**, if you're unfamiliar is a Truffle like interface to help you build EEs. It is still in a pretty rudimentary place, but it's going to be a fantastic tool going forward.  

We have two pending write-ups right now
1. from Mikhail around **safety on Eth1 <-> Eth2 bridge and Eth1 <-> Eth2 bridge finality gadget**. If it's not out already, it should be out today. 
2. a writeup on **Discv5** from Alex is imminent.
Yeah, we're making research progress right now. We did Eth 22 too, that was great.

**Danny**: Thank you! Proto has put together a draft Phase II spec. If you want to take a look at the specs repo, PR is open. Other research items we want to go over. 


**Ansgar**: I can give a summary for the Quilt team. Will is currently on a plane. We spent  last week at SBC and had many productive discussions there. Synced up with the other research teams. Before SBC, we polished the Eth research post on our vision for phase 2. If you guys want to look on that, basically all our thoughts are around Phase 2. In our opinion, they are not real blockers left for Phase 2, still a huge design space but the approach we find on taking is to just the minimal implementation, minimal phase 2 spec implementations that we see and that's basically also what Proto started writing the specs on. They came from the same discussions around that. We want to shift our focus to now implementing that. With a target of having a MVP version of Phase 2 implementation and done, so that we can then iterate on that and compare with other research done there. Next few months will be mostly focused on getting this minimal Phase 2 implemented. 

Other few small updates, Sam and I have been looking into this whole question around dynamic that existed, aesthetic site access that some of you might of heard of that. That's DSA vs SSA topic. Account internal preference is to likey go with SSA for Phase 2, we have been looking a little bit into the feasibility there.

I've been specifically looking into existing popular Eth1 project to see how easily SSA similar use cases can be implemented in SSA phase 2 world. They are talking great so far. Sam has been working for the last two weeks specifically on a Analysis Tool for Solidity integration. The idea here is to have a tool that is basically doing optimization pass overhaul and checking contracts for DSA. So, if we were to go with purely SSA, then we would need developer tooling around detecting DSA and would just like any syntax checker would highlight the part of the code that use DSA patterns, so you can correct that. Overwrite the check if you know what you're really doing. That's really looking great so far as well as there's a writeup on the Eth research on that and basically done as an MVP for now. I think we will have a more comprehensive writeup on the whole SSA idea topic as soon as we have a clear picture on the remaining questions there. 

Last update from my side. As Joseph already said that Matt and Johnny had a new release of the Eth 2. That is the idea, that is the core library for the Eth development and we hope that it will be really helpful for prototyping and going forward so we don't really have to implement all those things - state, account structure every single time we want to prototype a new EE. Johnny post a summary on the [twitter](https://twitter.com/JonnyRhea/status/1230195894236086277?s=19). 

**Danny**: Awesome, good work!

**Carl**: So having had some quite a few discussions about the whole SSA, it's a very interesting change. It's definetly the right move and simplifies a lot of the harder problems. It's easier to come up with a solution. But it does mean changing the standard pattern. I'd like to encourage people to  stay up to date with us because it's important that we get as many eyes as possible on whether this is a feasible direction to go towards how we do stage in the future. From what we discussed, we could not see any major design patterns that we prevent by switching others to SSA and certainly it's worth it for because of the simplification that could be made. I'd like to advise people to follow what's happening here. It's an interesting design space, it's important to fully. understand the decisions we're making.

**Danny**: Thanks Carl! Other research updates. 


 ## 4. Networking
 
**Danny**: Okay we will have a networking call on Wednesday, a week from yesterday. I pushed that. Sorry about that. Are there any pressing item that we're going to bring up today?

**Jacek**: I can just briefly mention that I pushed a PR for segregating attestation (not really all) broadcast topics by fork version. Have a look at that in case any one interested.

**Danny**: Thanks Jacek!
  
  
 ## 5. Spec discussion
 
**Danny**:  Okay specs discussion, thoughts, comments, concerns issues ? 

 
 ## 6. Open Discussion/Closing Remarks

**Danny**: Closing comments?

**Joseph D**: Who's going to be in Paris? Are we going to have a get-together for Eth2? 

**Hsiao**: Hello! I'm thinking about it, so we can have something on March 6th. There is this Eth 2 discord channel, where we can check people's opinion on having it on the 6th. If you are interested in, please DM me or give some signal on Eth 2 discord. I know that the Gorli testnet team might want to organizing some event. That discussion is also on discord.  

**Danny**: There is the Eth CC channel in the discord. 

**Proto**: ETH London? For everyone who is around, let's talk about Ethereum 2. 

**Ben**: I'll see you there too. 

**Danny**: Anything else?

 # Date for Next Meeting: March 12, 2020
 
 **Danny**: Keep up good work, w do this call in  next 2 weeks. Networking call next week.
 
 Thanks everyone!
 

 ## Attendees

* Alex Stokes (Lighthouse/Sigma Prime)
* Adrian Manning
* Ansgar Dietrichs
* Ben Edgington (PegaSys)
* Cayman
* Carl Beekhuizen
* Cem Ozer
* Chih-Cheng Liang
* D
* Danny Ryan (EF/Research)
* Guillaume
* Hsiao-Wei Wang
* Jacek Sieka
* John Adler
* JosephC
* Joseph Delong
* Lakshman Sankar
* Mamy
* Marin Petrunic
* Meredith Baxter
* Mikhail Kalinin
* Milan Patel
* Musab
* Protolambda
* Pooja Ranjan
* Sly Grphon
* Terence Tsao (Prysmatic Labs)
* Tomasz Stanczak
* Trenton Van Epps (Whiteblock)
* Zahary


 ## Links discussed in call:
 
 * Agenda: https://github.com/ethereum/eth2.0-pm/issues/129 
 * beacon fuzz update: https://blog.sigmaprime.io/beacon-fuzz-02.html
 * Meredith: https://github.com/ethereum/EIPs/pull/2335
 * Ben: https://github.com/PegaSysEng/eth2signer
 * Carl: https://github.com/cfrg/draft-irtf-cfrg-hash-to-curve/pull/212
 * Joseph Delong: https://twitter.com/JonnyRhea/status/1230195894236086277?s=19

