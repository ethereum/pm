# Ethereum 2.0 Implementers Call 57 Notes <!-- omit in toc --> 

### Meeting Date/Time: Thursday 2021/02/11 at 14:00 UTC <!-- omit in toc --> 
### Meeting Duration:  1 hr <!-- omit in toc --> 
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/203) <!-- omit in toc --> 
### [Audio/Video of the meeting](https://youtu.be/z3Gj6TXgcb0) <!-- omit in toc --> 
### Moderator: Danny Ryan <!-- omit in toc --> 
### Notes: Shane Lightowler <!-- omit in toc --> 
### [Previous Call (56)](https://github.com/ethereum/eth2.0-pm/issues/200)

-----------------------------

# Contents <!-- omit in toc --> 

- [1. Client Updates](#1-client-updates)
  * [Teku](#teku)
  * [Lodestar](#lodestar)
  * [Prysm](#prysm)
  * [Lighthouse](#lighthouse)
  * [Nimbus](#nimbus)
- [2. HF1 / Upgrade Update](#2-hf1---upgrade-update)
- [3. Merge Discussion](#3-merge-discussion)
- [4. Sharding Discussion](#4-sharding-discussion)
- [5. Other Research Updates](#5-research-updates)
- [6. Spec Discussion](#6-spec-discussion)
- [7. Open Discussion/Closing Remarks](#7-open-discussion-closing-remarks)
- [Annex](#annex)
  * [Attendees](#attendees)
  * [Next Meeting Date/Time](#next-meeting-date-time)

## Action Items

Action Item | Description
| --- | --- |

- **57.1:** Contribute to the [naming of HF1.](https://github.com/ethereum/eth2.0-pm/issues/202)
- **57.2:** Review HF1 bonus features [PR 2192.](https://github.com/ethereum/eth2.0-specs/pull/2192)
- **57.3:** Feed back on [fork choice block slot pair PR.](https://github.com/ethereum/eth2.0-specs/pull/2197)
- **57.4:** Attend next ACD call to discuss future roadmap.
- **57.5:** Let Danny know if you'd like to attend the Stateless calls but don't know about them yet.

-----------------------------

# 1. Client Updates

Video | [3:26](https://youtu.be/z3Gj6TXgcb0?t=206)
| --- | --- |

Danny - I rearranged things a bit this week so that we can leave some room for followup and discussions on far future upgrades and things coming up. We’ll talk about client updates first, then we’ll talk about Upgrade 1. [Naming for this is up for grabs.](https://github.com/ethereum/eth2.0-pm/issues/202) Then we can talk about the merge and sharding. After last week’s workshop there have been different conversations going around on the merge. On the next All Core Devs (ACD) call next Friday, there’s some room there on the schedule to talk about the merge and roadmap. I’ll be there and you’re all invited. Then we’ll leave some room for R&D/spec discussion. Let’s go ahead and get started with client updates, starting with Teku.

## Teku

Video | [4:57](https://youtu.be/z3Gj6TXgcb0?t=297)
| --- | --- |

Ben - We’ve implemented UPnP for router config. We were finding the #1 issue on the support forum was missing peers due to mis-configured routers, so hopefully this will help. Gossip scoring is now in - we havent enabled it by default yet. Many thanks to Lighthouse for helping to get that sorted out. We’ve basically followed the same approach. The forthcoming upgrade - it involves a lot of refactoring work. Im sure we’re all going through the same thing. We’re mostly prototyping good ways to support versioned data structures at the moment. Speaking of refactoring, we’ve done a huge refactor of our SSZ library to bring it into the 21st century, making it more maintainable for future. Anton has done a huge amount of the heavy lifting on that. The weak subjectivity calculations have been updated as per the latest version in the specs repo. We’ve done a lot of housekeeping on getting the Blast library integrated with our CI process. So, lots going on under the hood, maybe not so much on the surface. Adrian worked up an analysis of the work that would be involved in implementing the proposed LMD GHOST balancing attack mitigation, which has been circulated on the forums. I’ve made a start on KZG commitments library in C that we might use for prototyping work in Teku before something better comes along before production. That’s it from team Teku.

Danny - That’s awesome. Very busy indeed. Were there any learnings or things worth sharing on the SSZ fixes or is this mainly an incorporation of what others are already doing?

Ben - I’m not really familiar with the details but the way the code was originally written was somewhat opaque, so it was mostly making it much more transparent and maintainable and playing much more nicely with the backing tree structures.

Danny - Cool.

Ben - Might be worth a conversation with Anton some time.
  
## Lodestar

Video | [7:59](https://youtu.be/z3Gj6TXgcb0?t=479)
| --- | --- |

Danny - Thank you. Let’s move on to Lodestar.

Cayman - Hey everybody. We’ve been working on refactoring our sync and peer management, making it a lot more robust rather than just ‘you get what you get’. We’ve landed half of the sync refactoring… just initial up to finalised is landed in our latest release and work in progress is our peer management and some of the unfinalised sync. Other stuff that’s work in progress - we’re also working on refactoring the codebase to handle hard different versions of the data structures. Should be nearing the ability to test out the hard fork. I think we’ve implemented a few of the state transition changes. And the last thing that we’re also working on is the multiproof creation and consumption and linking that to our SSZ library. Right now we can do single proofs on SSZ objects and now we’re working on expanding that to multiproofs.

## Prysm

Video | [9:26](https://youtu.be/z3Gj6TXgcb0?t=566)
| --- | --- |

Danny - Thank you. Prysm.

Terence - Hi guys, Terence here. So we released version 1.2.0 on Monday. It included the feature of slashing protection that allows import and export, which satisfies EIP-3076. We’re continuing work on the Eth2 API and are about 50% done. We fixed some minor bugs by reducing log time in attesting and we’re also working on trailing slot cache. So we cache the next slot state immediately after processing and verifying the beacon block. Credit to Paul and Lighthouse for the idea. And that’s it from team Prysm.

## Lighthouse

Video | [10:20](https://youtu.be/z3Gj6TXgcb0?t=620)
| --- | --- |

Danny - Great, thank you. Lighthouse.

Paul - Hello! So we’ve also been working on optimisations for block propagation like Prysm mentioned. We’ve also adopted a strategy that Teku is using. So continuing the clients syncing while the other client is, so thanks to Teku for their input there. We found that we can reduce our memory usage by about two thirds by modifying new allocator params. So we’re looking at what that means and seeing if we can pass those savings on to users by default. We’re researching attacks on the P2P network, creating some real world exploits so we can test clients in a safe, controlled environment. We’re expanding the team via hiring. We’re hoping to have some new people starting next month but we’ll see. We had a PR merged in the networking spec. It’s very minor, its just about checking that the blocks slot is higher than its parent. You can find the PR in the specs repo with the number 2196. We’ve also changed the IPs of our bootnodes and we made a PR to Eth2 clients / Eth2 testnets repo. That PR is number 37 - its the only open one. That’s it from me!

## Nimbus

Video | [11:46](https://youtu.be/z3Gj6TXgcb0?t=706)
| --- | --- |

Danny - Nice. Thank you. And Nimbus?

Mamy - So we released v1.0.7 this past week. It has significant performance improvements on ghost traffic and scoring, block validation and Eth1 deposit ETH use. So things that we talked about weeks ago. It also includes doppleganger detection, that was coined by Superphiz. This should detect and prevent people from having two validators in different places running at the same time. One of them will be shut down preventatively. Also we had the Nimbus dashboard challenge. We’ll extend the deadline. Expect a new blog post soon with more details. Although we’ve had great interest we havent had any submissions yet. Some people understand that they could use Pyrmont instead of being a full validator on mainnet to participate in the challenge. Also, not directly Nimbus related but ConsenSys Diligence disclosed a vulnerability in Nim package manager and HTTP module. So we want to say that we dont use Nim package manager or HTTP module in Nimbus and also that this was fixed yesterday by the Nim team and will be going into the new release which I expect over the weekend or next week. We also want to thank ConsenSys for helping auditing the Nim language. And also thanks to user jcrtp who improved Nim JSON RPC over the weekend and integrated Nimbus into Rocketpool. Otherwise we have upcoming changes that are available in the unstable branch and will land in version 1.0.8, related to IO optimisation - Refactoring of slashing protection to fit EIP-3076 and address high IO and improve doppleganger detection. Both features were developed in parallel, dont depend on each other, and are slightly inefficient right now. Also adding a new benchmarking tool to analyse bottlenecking db storage and to improve IO further down the line.

Danny - Great, on doppleganger detection. As it starts does that immediately scan the chain for recent signed messages that are not in the slashing database?

Mamy - Right now, no. We didn’t want it to depend on the slashing db right away because it was under refactoring. Right now what it does is wait for 2 epochs just making sure that there are no attestations  - or validators - that are not from us when it starts validating. So there is on restart that can be skipped but there are always 2 attestations that will be lost. In the next release we will improve that so that you can look into the past 2 epochs instead of waiting 2 epochs.

Danny - Thanks, I think that is a very important feature. 

# 2. HF1 / Upgrade Update

Video | [16:00](https://youtu.be/z3Gj6TXgcb0?t=960)
| --- | --- |

Danny - We will move on to the state of the unnamed upgrade 1. There is an [open issue](https://github.com/ethereum/eth2.0-pm/issues/202) in the eth2 pm repo to discuss the naming of the upgrade. Please contribute. 

**Action item 57.1:** Contribute to the naming of HF1.

Danny - So there’s still this [Vitalik doc](https://notes.ethereum.org/@vbuterin/HF1_proposal) from a few weeks ago. This is still primarily what’s going on. Sync committee and accounting stuff is merged. We are working on the adjustment to the penalty constants right now. Theres [another PR](https://github.com/ethereum/eth2.0-specs/pull/2192) that encompasses a bit of these bonus features which does per validator inactivity leak accounting. And at the same time reduces the overhead of processing empty epochs by a factor of 64. This recently we just finished getting some testing done. I invite you to take a look at this feature to assess both that it does what it claims to do in reducing the overhead in empty epoch processing, and the technical evaluation - how deep of a change is this to get it into the codebase. If we get some general thumbs ups on that I expect that we’d merge Monday/Tuesday. 

**Action item 57.2:** Feed back on HF1 bonus features [PR 2192.](https://github.com/ethereum/eth2.0-specs/pull/2192)

Danny - Hsiao-Wei and I as well as Aditya are spending time trying to clean up the last bits on this. I’d like to get you a pre-release on this mid-next week that has the initial test vectors cut so that we can get engineers running through this to feed back inevitably into the spec. I’m sure there’s something wrong in there, so let’s get more eyes on it to tighten it up ahead of a full release. Additionally, as I said, Aditya is doing some work here - there is this [fork choice block slot pair PR](https://github.com/ethereum/eth2.0-specs/pull/2197) that went up in the past 36 hours or so. I’m doing some review and I expect some iteration there, but also I'd love for client teams to come and chime in. 

**Action item 57.3:** Feed back on [fork choice block slot pair PR.](https://github.com/ethereum/eth2.0-specs/pull/2197)

The balance attack change I think is in progress. Aditya and I need to take a look at [Adrian’s document](https://hackmd.io/@ajsutton/balancing_attack) which was just shared. So, things are generally moving forward. The stuff that is in the Vitalik doc that are under proposed consensus changes are happening. The proposed fork choice changes are also happening, barring some discussion on this balancing attack and the feasibility of implementation. And additionally there’s this bonus feature that is slated to go in, but I’d really really like some engineering feedback on it before we merge it early next week. I’m still trying to work out how to do pre-releases and test vectors of pre-releases but we’ll figure it out and get them out soon. So all in all, I think we’re at the point where we’re going to flip the switch from the specifications of these things into an engineering cycle to sanity check and get things basically in place. I’m really glad that a lot of the teams have been working on figuring out how to handle forking and in terms of databases and conditional things, also with these test vectors on our big to-do list is how to get these actual fork tests - how to test these fork boundaries so that we can all make sure we’re doing these fork transitions properly. Additionally, Hsiao-Wei is owning the fork choice test vectors. Since I’m not owning it, it will actually get done. On our list of HF1 things is to actually get us some consensus tests on fork choice which since we’re changing/fixing things this is a good time to get done. Any questions/concerns on the HF1 proposal? *long silence* Ok. 

# 3. Merge Discussion

Video | [20:55](https://youtu.be/z3Gj6TXgcb0?t=1255)
| --- | --- |

Danny - Proto’s not here but he’s been working on eth2 integrations and modualisation extension of hive to handle getting eth2 clients in there. This will be useful for testing the merge - eth1 and eth2 clients live in the same environment. Manually testing the merge code every time is a painful process. If Proto’s work gets merged relatively soon we can experiment with getting eth2 clients in there and practicing/working on fork tests. Next up is the merge. Thanks everyone for attending the [eth2 researchers workshop](https://blog.ethereum.org/2021/02/11/eth2-quick-update-no-22/) last week - thanks to Mikhail and Guillaume for presenting on the merge specifically. I know there’s been a bit of conversation on discord and various channels since then. I want to open it up in case people want to talk about merge, theory, practice, questions, concerns (I know there’s plenty of concerns). We can chat here or async. *long silence* Mikhail - what is the state of the proto-specifications that you have? I know that there’s a little bit of review going on right now. 

Mikhail Kalinin - Yes, there is a draft of the specification that needs to be reformatted but the draft of the beacon chain spec and validator/block choice change… eth1/eth2 communication protocol needs some reformatting to be published. I guess it will happen in 1 or 2 weeks. I can just publish the draft if anyone is interested in it.

Danny - I’ve done a little bit of review and will finish in the next couple of days. The sooner we can get something out the better.

Mikhail - Yeah sure, agree. Also as was suggested we are going to have conversation between the core devs and implementors on the technical aspects. Do you have a sense as to when this can happen?

Danny - When what can happen exactly?

Mikhail - I mean to continue the conversation with eth1 core devs.

Danny - Right. So I was talking to Tim a bit and I believe that on the next ACD call we will talk about this more broadly in terms of roadmap. Tim, I and others then need to spend some time enumerating what needs to get done. And then it would be good to start a monthly, at least, call to sync on the various things. Some of us that have been working on the past handful of months on this have been doing a private working group call but I think its time now to open that up. Let’s do the ACD call in a weeks time and from there get something in the schedule where we can regularly iterate on this. Prior to that there’s always the discord comms as well.

Mikhail - Sounds great to me. If anybody has any other concerns or thoughts reach out to me on any channel. 

Danny - I invite a member from each team to come to the ACD call next week where we will begin to talk about the things that need to get done on that side of the stack. 

**Action item 57.4:** Attend next ACD call to discuss roadmap.

# 4. Sharding Discussion

Video | [26:17](https://youtu.be/z3Gj6TXgcb0?t=1577)
| --- | --- |

Danny - Next up I want to open up time for questions/discussions on sharding R&D. Thanks to Vitalik and Dankrad for digging deep into some of the components there last week in the workshop. Open up for questions/comments/thoughts.

Terence - Yeah, I have a question on single secret leader elections. Is that going to be part of the sharding roadmap?

Vitalik - I think it’s definitely part of the roadmap. Though as Justin pointed out a couple of weeks ago, in order to help alleviate *sound muffled* …we want to focus on scaleability oriented features earlier and security oriented features later. We should still continue working on single secret leader elections together with proof of custody and data availability sampling. But its not a hard requirement for sharding to be launched.

Danny - A quick update on the state of the research. I know there have been a couple of fairly viable paths identified there? Justin, can you give us a quick update on where we’re at?

Justin - We are very advanced. The theoretical research is basically done and Mary M has some formal proofs, which is great. Those are on Github. We also have a proof of concept in Rust. The performance is great but we think we can squeeze out even more performance with optimisations. I’d say we are in a great position from an R&D standpoint.

Danny - Do these utilise zero knowledge proofs?

Justin - Yes, this is basically a custom zero knowledge proof with a very specific shuffle statement. We’re basically doing this permutation and we want to prove that this permutation was done correctly, so its not a generic proof system. And so one of the things that we gain from specialising is that theres less heavy duty infrastructure so we can ship it faster. There are also fewer assumptions that we need to make on the cryptographic side of things. As Vitalik mentioned, I think it makes sense to ship MVP sharding (just shard data) to start with. All of the security features can after the MVP (eg SSLE, proof of custody, VDFs, data availability sampling). The rationale is that we likely have plenty of security right now. Getting to the point where we have World War grade security can wait a year or two.

Danny - Thanks for the update. Any other items people want discuss around sharding in general? Whats the status of the validity proof for data availability sampling? Is it fully specified or is there still R&D taking place on the topic?

Vitalik - By validity proof do you mean length proof?

Danny - Matt?

Matt - I’m not exactly sure what the construction is at this point. I was under the assumption that there is some kind of root that we know, because its a validity proof, that we can prove that the merkle root was constructed correctly…

Vitalik - There is no merkle root. There is just a kate commitment. Kate commitments are self-validating in that sense. The only thing we need to prove is the degree of the polynomial because that represents how much data the kate commitment is actually storing. For that the protocol is basically finished - it’s extremely simple. If you want to prove the polynomial is at most degree n and you have t powers in your trust setup then you just provide the same polynomial multiplied by x to the power of t minus n. And then you do one pairing check to verify that. 

Matt - Ok great.

Danny - Thank you. Any other questions or general discussion points around sharding before we move on? 

# 5. Other Research Updates

Video | [32:10](https://youtu.be/z3Gj6TXgcb0?t=1930)
| --- | --- |

Danny - Ok. Any other research updates that people want to share today? Ok. A point of note for this group - the stateless calls have begun again and it seems like there is renewed energy in stateless research. If you aren’t aware of those calls and you want to get on the email group let me know. 

**Action item 57.5:** Let Danny know if you'd like to attend the Stateless calls but don't know about them yet.

# 6. Spec Discussion

Video | [33:05](https://youtu.be/z3Gj6TXgcb0?t=1985)
| --- | --- |

Danny - Ok, general spec discussion - I think we have covered a lot of these points especially when talking about the unnamed HF1… are there any other discussion points around spec?

# 7. Open Discussion/Closing Remarks

Video | [33:33](https://youtu.be/z3Gj6TXgcb0?t=2013)
| --- | --- |

Danny -  Ok. Open discussion and closing remarks? Perfect. Thanks everyone. I will keep you all updated as we get these pre-release test vectors out and otherwise continue to collaborate in all of the asynchronous channels we all hang out in!

------

# Annex 


## Attendees 

- Danny Ryan
- Paul Hauner
- Terence (Prysmatic)
- Mamy Ratsimbazafy
- Ben Edgington
- Cayman Nava
- Mikhail Kalinin
- Justin Drake
- Matt (Lightclient)
- Vitalik Buterin
- Alex Stokes
- Raul Jordan
- Zahary
- Leo (BSC)
- Carl Beekhuizen
- Jacek Sieka
- Aditya Asgoaonkar
- Lakshman Sankar
- Nishant
- Ansgar Dietrichs
- Hsiao-Wei Wang



## Next Meeting Date/Time

Thursday, February 25, 2021, UTC 14:00.