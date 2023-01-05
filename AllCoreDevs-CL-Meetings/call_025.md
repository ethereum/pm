# Ethereum 2.0 Implementers Call 25 Notes

### Meeting Date/Time: Thursday September 19, 2019 at 14:00 GMT
### Meeting Duration: ~ 50 mins
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/85)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=pEdqjXO6euY)
### Moderator: Danny Ryan
### Notes: Pooja Ranjan

----------

## Agenda
1. Testing and Release Updates
2. Client Updates
3. Research Updates
4. Network
5. [Next interop steps](https://github.com/ethereum/eth2.0-pm/issues/85#issuecomment-532835822)
6. Spec discussion
7. Open Discussion/Closing Remarks

**Danny**: Welcome everyone!

## 1. Testing and Release Updates

**Danny**: We [published](https://blog.ethereum.org/2019/09/19/eth2-interop-in-review/) quick follow up to celebrate success on EF blog.

**Danny**: Great, so we will get started with testing.
* In interop, we had three or four consensus area failure showed up primarily, interesting enough. A few corner cases, that's surprising in spec but they happen between epoch transition 1 and 2. This is the first time we are doing account balances, we have enough information.
* We built test cases for interop and shared. Those are generally valid test factors, it could be running into 0.8.3 clients.
* As we make many changes to spec, so we're going to handwrite some test that capture the complexity. We did work though lot of those at interop and cleaned up  lot of these crosslinks and other stuff, which is good.
* Unless, you take those scnario in that repo and create some hand written tests, thats on my agenda today. That along with updates in network spce which worked out at interop  and a very small things to be released. 0.8.4 come up likely in next few days with updated network spec and new test cases.
Proto, do you want to add any other thing?

**Protolambda**: During interop, due to state-transition running with all clients, it speed up progress and time we needed to find bugs. I want to automate it and start writing this to triger state transition and get the real fast result of all different clients of certain state transition and hopefully the next up would be to attach it to the testnet. My goal is to automate the efforts we have put in interop and make it distinguish.

**Danny**: Right, the expectation is, as we make more testnets and more tests with different clients and in different scenarios, we still find some of these consensus errors and to capture them.

### Fuzzing

**Danny**: On the fuzzing front, we do plan on the next couple weeks open up, reopen the differential fuzzer, *Medi* from Sigma Prime is going to be helping out that effort. There are texts to the goal and we are at the point, where we begin integrating clients into differential fuzzers. More to come in the next few weeks on that.

## 2. Client Updates

**Danny**: Today, I know we could probably talk about all the exciting things that happened instead instead we will save that for twitter, for individual blog updates.

### Sigma Prime

**Adrian**: I will make this pretty short.
* At interop, we had some successes and LightHouse finalizes blocks. In that process, we find some of bugs that we still need to fix and some discrepancies between other clients that we've been working on that.
* We focusing a little bit more on building over the last week since interop will be adding some extra tool for interop testing. Because we found that during some of our testing, it would have been extra functionality to find some of the bugs quicker.
* We're going to start focus on Discovery and making it interoperable with Go; so the Rust that we've  built, we're going to start testing it with Go, which is inside Prysm.
* We're also finishing off some of the updates for the latest networks specs so that we can start syncing and hopefully have some longer lasting multiclient testnets.
That's it from us, thanks.

**Danny**: Cool, thanks.

### Prysmatic

**Terence**: Yeah, pretty much the same update as Adrian. Our top priorities are working on:
* sync resilience. We currently don't handle missing blocks very well
* scaling validator account to 1024
* we found a few BLS having issues
* updating to the latest network spec PR
* also working on SSZ resilience.
* we have made some fuzz testing on there and stuff working on test coverage improvement
* doing some mutation testing
* we're also cleaning up our package and documentation
* and make sure our frameworks are up to date.

**Danny**: Cool, thanks.

### Artemis

**Joseph**: Since interop,
* we integrated JVM libP2P.
* we started working on our sync.
* we're just cleaning up some technical debt and the test. That covers it.

**Danny**: Great.

**Shahan**: We're also updating Artemis to integrate Handle protocol.

**Danny**: Cool, thanks.

### Lodestar

**Cayman**:This week,
* we've been working on merging in our interop changes in master, fixing those up.
* we're also working on some roadmaps for the next few months so that we kind of have a better sense of priorities in or working on
* we started also developing a roadmap spe cifically for light client work, so want that to flesh out and get started with it.

**Danny**: Cool, thanks.


### Trinity

**Hsiao-wei Wang**:
* we've learned about many issues during interop that could be summarized into two things:
1. the stablility, that we are now focusing on make internal test to be more stable and to organize logs to people structural eyes and also make well clear dashboard to monitorit
2. is the ability to distribute the software and set up the client that Alex and Brian have made a file during the interop and decide exploring other solution for various different operation system to support  different OS to install the Trinity software.

**Danny**: thanks.

### Harmony

**Mikhail**: Similar to other teams,
* we are doing some interop follow ups - some fixes and some new stuff that were created during interop.
* Also apart from interop, I am going to work on Discovery. It has already almost implemented, the only one thing left is handshake and cryptography.
* This implementation doesn't include a topic Discovery. So it's probably would make sense to do some integration tests with Lighthouse, when we are ready.
* also working on QA, doing some testnet stuff.
* We decided to start the work on the fork choice testing maybe we can do some work here and publish some tests that are useful for or the other implementation because we think that fork choice is also important.
That's probably it for us.

**Danny**: Cool, thanks.

### Nimbus

**Danny**: Most of them are on flight. From [mratsim](https://github.com/ethereum/eth2.0-pm/issues/85#issuecomment-533089773)

The Nimbus team will be in transit so here are our updates:

* great interop, thank you all especially Joe D for the organization.
* we are slowly merging back our interop branch into master.
* we gathered plenty of scripts to start all clients at: https://github.com/status-im/nim-beacon-chain/tree/interop/multinet
* we propose to create a common repo or even a separate eth2.0-clients organization to store and maintain them with every client teams with admin rights (did I hear a DAO in the back)
* That repo/org could also be used to maintain simple chat apps code and running scripts to debug all libp2p implementations
    * Lodestar will be committed soon (living locally on @arnetheduck computer)
    * Artemis and Shasper are missing
* we'll see you in Devcon

### Parity

**Danny**: Parity wasn't anble to attend but I know that Wei has been working through some pair wise interoperability tests. Last I heared, I knew hedid some work with Lighthouse and updating client to 0.8.3. Wei will be with us in Devcon.
Great, did I miss anyone?


## 3. Research Updates

**Danny**: Vitalik and Justin are not here. I know, this busyness with Devcon comming up we've interop and something is going on in Tel Aviv.
* The spec repo has been a little bit slow. There some big PR submerge, some last updates to get in.
* A **lot of focus** has been **in ensuring that** **Phase 1 sharding chain spec is clean** and to begin to  **revisit** a lot of **the custody games**.
* Relative high complexity in the custody games right now wrt some of the corner cases and edge cases, so planning on giving that a lot of love.
Beyond that I am sure there would be a plenty of updates at the Devcon.
Other research updates?

**Nicolas**: Outside normally changes, but we're looking at the integration of and learning after needs, so I implemented kind of Proof of Concept in **Vintage Time Protocol Simulator**. I will be working with team inside ConsenSys, specially Sahahan on how to add details. And likely to work with this as well we have recruited a team inside ConsenSys. It's more on implementation point of view. we're not changing the protocol itself.

**Mikhail**: Guys excuse me, may I have a question to Nicolas?
Okay, we've been looking into the attestation and aggregation a bit and the things that I am not able to figure out is for example, handle applicable to work in that P2P Network? Does it strictly require a direct connection between validator and agregrators?

**Nocolas**: It requires directly. So the way we see it on peer to peer layer when the committe is established, people will be able to exchange, maybe encrypted messages - what's my IP address of aggregator we're using and then there will be direct messages between those aggregators.

**Mikhail**: Yeah, I see. Okay, thank you.

**Shahan**: Hey Anton, I'm so sorry for butting in. There is [document](https://docs.google.com/document/d/16Srarfae9FOWPsr67OVL7aWrSujbtRrzPBz4Kv9PTak/edit ) that Nicolas and I are working on. What we used is synchronized asynchronously. About question like that, I can share that with you.

**Danny**: Okay, thanks.

### Beacon chain

Musab, any **updates on Beacon chain**?

**Musab**: The **specification is now almost finalized**. All the tests passed, which serves as a very nice validation of the model and right now we are doing **Coverage Analysis**. This is specific to the *K tune* we are using. We are hoping that we get some kind of evaluation of the test suit. And may be suggest some other tests to increase coverage.
Once this is done, which we hope to be very soon, sometime; we will hopefully be able to share this with everyone. We're very excited to have this done once this is ready.

**Danny**: Thanks. And some conversations to figure out next steps with the model. How to actually use it to verify some of the properties, we are interested - safety, being the most obvipus ones.

**Musab**: Right.

**Danny**: Great, thanks.
Any other research updates?


**Protolambda**: We really create this, from the K framework we can drive the invariance for the fishing efforts. We can define stricter rules to put on the fishing harness. Question would be, can we have derive something like this from the current work or coul does work, since its really improve forcing?

**Danny**: The question being, can you use the case say, transition model to derive invarients about the state transition, are you familiar with any work related to that?

**Musab**: I am not entirely sure about deriving invarients, at least not with the current model. Not deriving invariance but stating and verifying the variance woul dbe soemthing that would be possible with the next step development.

**Danny**: Thank you.
Other research updates?

### EWASM

**Alex**: I can give some **update regarding Phase 2**.
Some of the Ewasm team members also attended interop and had some discussion at the interop. In past couple of months, the main focus for both teams at work were just to prove the feasibility of the idea. We've been focusing on two different efforts:
* one **having hashing function and elliptic curve functions in EWASM** and executed to an interpretor and the goal was to fit that into the execution time limit we have set.
* second work was related to **having good schemes for Merkle Proofs** and all the witnesses and obviously we've to look into SSZ partials and we also looked into Alexey's multi proof, which is in interval gases, if you guys have heared about that before.
* And there was a couple of other new initiatives to have some different schemes for Merkle proofs and businesses. Many of theses were implemented in different languages as well. Rust, Assembly script editor are major ones we want to be looking at.
And we've some synthetic benchmarks.
* The end results of this work is that the whole concept seems to be feasible, that we are kind of ready to move on to next stage.
* The **next stage is to actually  create usefull execution environments and benchmark them as a whole**.
* The main execution environment that we are looking at is just a simple token transfer execution environment. Because that's like the core function needed for a couple of components as well, like the fee market.
* The Ewasm team is really focusing on what I just explained. We all are really **focused in understanding our markets and fee markets better**.

At the interop, we need to look at it more in an integrated
manner because they have a heavy influence on the design. I think that's the next step for the two teams to work on this more closely.

The very last thing that happened at the interop was **Vitalik came up with a new proposal for phase2**. We spent quite a bit of time discussing it with him trying to understand it and comparing it to the current proposal. It was quite a busy period, sorry for the long update. Thank you.

**Danny**: No, Thank you. Appreciate it.
I know, there's still a lot of questions out there regarding us. Some of that because it's still heavy research but some of this because of less information. For example, I haven't responded yet but somebody on the discor id asking about the **faith of the Eth 1 chain**, where it lies? I think, although we don't have 100% answers, **the execution environments have a bright future for the Eth1 chain, living inside the Eth 2**. I'll respond that to on discord too.

Is anyone from Quilt here?

Any other research updates before we move on?



## 4. Network

**Danny**: There was much work done on the network spec at interop. A lot of this primarily had to do with the structure of the request response messages sync and all the related sync messages rather than the gossip and some of the other structures. So, someone working on that would you like to give us a quick report on what happened there?

**Adrian**: Yep, sure. So, it was proposed that it would be more efficient and little bit more general, that when requesting large amounts of blocks, previously the Spec required like batched amounts of blocks. So for long range, we're thinking we had blocks, **"blocks by range" is the new name of the RPC request** which you can request. Let's say a hundred blocks and previously you would have to buffer this and get the whole number of blocks in one hit. Now, you can effectively stream them through the networks. So,  you send one block wrapped in an RPC response and then another one and then, until either you've completed the entire request or an error has happened. So, this allows implementations to read a single block from the database send it across the network and do this opposed to having to buffer large amounts of blocks. SO, that's the **main change in the two RPC request that required large amount of blocks**.  We've renamed them
* one is **block by range** and
* the other one is **blocks by roots** or effectively you can stream these things now that was the major change.
 That's it in summary. If anyone else has any questions.  

**Danny**: I have to ask, that code that you didn't want to remove and delete and rework, did you end up doing that?

**Adrian**: Partially, I couldn't delete all of it. So, I found a way to keep some of it. It still does batches so we can process blocks in batches but we stream across the network now.

**Danny**: Cool, thanks.
Any other question regarding that? As I mentioned on the discord, this spec parent lives in the b08x branch and is released into master, a minor release in next few days. But if you're working on that work sync, please check that out rather than the current one  with me on 0.8.3.

Did I see someone from Protocol Labs here? Is Michael here or Mike here?

**Mike**: I am here. Raul's on vacatio this week. We really didn't have much of an update. I know some of the language teams have been making progress, which is great. They can speak to that if they want. We didn't have update for LibP2P to feed like, overall.

**Danny**: Some work at interop was initially just ironing out some of the idiosyncrasies between some of the language implementation. So at least on the interop subset of LibP2P that we're using, we do have general conformance and implementation starting is exciting.

**Mike**: Awesome.

**Mikhail**: About JVM libP2P, basically, we're ready to  0.1 version. I think it probably could be released already. I'm not sure, I need to reach Anton again. But the thing is about to publish artifacts and do some documentation. May be I am missing something else. Also Shahan is working on the noise implementation which is not required by this version. SO, it could release it like in the next month.
Thanks Artemis for being the second users for JVM libP2P. That was very exciting to see that it really works.

**Danny**: Yeah, great work to Anton for getting that out.

**Whiteblock**, do you have updates for us?

**Trent**: Yeah, I can give a quick update. I wasn't at interrupt, so I'll just keep it short. This is coming from the team that was there. As most of you know it went very well, as super productive we had Antoine Renee and Daniel there. They spent most of the week adapting Eth2 clients to work in Genesis, white black Genesis. Which is, for those of you that don't know, is we're going to be testing the network and scale on. Like I said, it was super productive in, one of the things that we weren't able to complete were **prep for testing gossip sub** for a client like what variables we can change and also **how to optimize gossip subs**. So these are two big things that we're going to be attacking in the next few weeks. We will be refining the test cases that were already developed at interop, from here on out and actually starting to see how we can test them at scale. I'll drop that [link](https://github.com/whiteblock/gossipsub-tests) to the test cases in the chat and we will be presenting a near-term roadmap, medium-term roadmap externally soon as to what are methodologies going to be and releasing results once they're completed. That's it.

**Danny**: great, thanks.
Anything else to be discussed on network, stack or should we move on?

**Antoine**: Should I add, separately, from this we also study on network on libP2P and Gossip table. SO, we've people from protocol Labs, we are going to meet proto as well this week. We're going to get started on implementing a Go based client. The authoroties open source is under The White Block critical or gossip sub - testing. The idea is to take up the work that we had done early this year and really prioritise is using a specific implementation on libP2P for it that we really can streach and test at scale. In terms of testing the variables for the sub, testing the behaviours, this is something that for each attack.

**Danny**: great,anything else on networking.


## 5. [Next interop steps](https://github.com/ethereum/eth2.0-pm/issues/85#issuecomment-532835822)

Preston brought up what are our next interop goals are before and after Devcon? This is something that I am going to be thinking about a lot and organizing next steps with respect to public test networks and some incentivize test networks. We're not quite there as we all know there's a lot of work to do to stabilize clients  get sync in place and things like that but before we get there, start thinking about manual testnets is alos something that we need to be looking into the next level piece.
Any thoughts and comments on goals?

**Antoine**: Yeah, I would like to throw my hat in the ring to help you see from the whiteblock perspective. We can see so many new built comming in. We can have to be test to that. So, I think we'd be happy to be involved in help the community in terms of metrics analysis efforts.

**Danny**: Great.
**For the public** -  There are increasingly build scripts and things where you can pull down and do some stuff but we don't have any of these like multi client. That's not ready yet. We're planning on supporting users on anything, we still have somethings to do with respect to stabilizing and especially getting the clients conforming to these specification.
Is Preston here? Anything you would want to add or talk about?

**Preston**: I've been thinking, Devcon is 3 weeks away. We just walked away from interop, that was really good. I was wondering, if we have anything specific in mind, we need to target in the next 3 weeks and then Q4 is coming. Prysmatic were just planning out for rest of the quarter to hear from you or anybody who is interested what the specific goals were coming up?

**Danny**: On my end, it's CI network informants mapping out a plan for public testnets and incentivise that. On client side, I expect continual stability. I know some of them post interop had a big sprint to get to interrupt but now we have a lot of things to clean up around that. Then, I guess going into Devcon, a lot of conversation is there about things coming out next couple of months.

**Preston**: Okay, sounds great. I will follow up with you offline.

**Danny**: Anything else on this?


## 6. Spec discussion

**Danny**: Any questions, concerns things that you've run into this goes here.

None.

## 7. Open Discussion/Closing Remarks

**Danny**: Anythig that wouldn't been addressed that is worth one?

**Mikhail**: Devcon??

**Danny**:I do not have anything organized primarily because we just have this huge meet up and it seemed a little bit like over kill. There is so Day 1 of four  is relatively light of Devcon wrt some of the content but there is a room that's dedicated to community. I think Eth magician is organizing that stuff. I think there is Eth2 section talk to the community and a section to break out and talk about roadmap planning. So, I invite all of you to attend that and beyond that my expectation is to have a lot of organic conversations and meetings about what our next steps are and plans. I haven't planned anything for the day before and I currently am not planning on it but try out a little bit today.

**Mikhail**: Thank you.
Also the other question, what about contract deployment during the Devcon?

**Danny**: You mean deposit contract?

**Mikhail**: Yeah.

**Danny**: The primary blocker on the deposit contracts being deployed is the BLS standardization process which although has reached what is deemed and relatively stable place. People are still working on early implementations and test vectors. From the perspective of the deposit, we can't reasonably deploy that until we've the standard, in case anything related to public keys and the required  initials signature changed. The current, almost certainly will not be deploy that come, because of this walker. Although it is moving fast for a standard, because there's a lot of demand for another blockchains that are involved. It's quite simply not going to be ready by October time.
On this form verification, that is complete. There was an issue in Vyper compiler bug, which I believe has been merged and the updated bytecode has been tested and verified and relating on an actual cut released from Vyper but that's no longer seen as a bottleneck.

**Mikhail**: Okay, I see.

**Danny**: Anything else?

**Joseph**: I was planning on doing a kind of retro for Interop for people who were there or like to join. I think may be, give some feedback , so when we do it next time, things like may be not make it seven days kind of thing. That's TBD. I'll send out an invite and probably drop it into the interop channel and into the sharding Gitter.

**Danny**: Great, thank you. Thank you again for organizing that. I think I said a number of times. There I was a little skeptical so, I work of productivity and how it was going to go but it was pretty unbelievable and thank you for that.

**Joseph**: I am just happy that everyone came. I am happy that all the clients showed up, ready to rock. That was the big surprise for me.

**Danny**: Looking up the calender. October 3rd is two week from now, shall we plan for meeting then?

**Joseph**: Sure, that is great.

**Danny**: Sorry, I meant about this call.
I think, 3rd make sense?
Cool.

Thank you everyone.

# Date for Next Meeting: October 3, 2019 at 1400 UTC

## Attendees

* Alex Stokes (Lighthouse/Sigma Prime)
* Adrian Manning
* Alex Beregszaszi (axic)
* Antoine Toulme
* Ben Edgington (PegaSys)
* Cayman
* Carl Beekhuizen
* Cem Ozer
* Chih-Cheng Liang
* Daniel Ellison (Consensys)
* Danny Ryan (EF/Research)
* Greg Markou
* Hsiao-Wei Wang
* Ivan Martinez
* Jannik Luhn (Brainbot/Research)
* Jonny Rhea (Pegasys)
* Joseph Delong
* Kevin Mai-Hsuan Chia
* Leo (BSC)
* Marin Petrunic
* Mike Goelzer (libp2p)
* Mikerah (ChainSafe)
* Mikhail Kalinin
* Musab
* Nicolas Lin
* Nishant Das
* Olivier
* Preston (Prysmatic Labs)
* Protolambda
* Pooja Ranjan
* Robert Drost
* Shahan K.
* Sweater Cam
* Terence Tsao (Prysmatic Labs)
* Tomasz Stanczak
* Trent (Whiteblock)


## Links discussed in call:

* https://blog.ethereum.org/2019/09/19/eth2-interop-in-review/

* https://github.com/ethereum/eth2.0-pm/issues/85

* https://github.com/djrtwo/interop-test-cases/

* https://github.com/status-im/nim-beacon-chain/tree/interop/multinet
* https://docs.google.com/document/u/4/d/16Srarfae9FOWPsr67OVL7aWrSujbtRrzPBz4Kv9PTak/mobilebasic#

* https://notes.whiteblock.io/EBV_n3b6SWy6GZ76ZrApmA

* https://github.com/whiteblock/gossipsub-tests
