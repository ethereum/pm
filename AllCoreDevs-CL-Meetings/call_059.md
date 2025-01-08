# Ethereum 2.0 Implementers Call 59 Notes <!-- omit in toc --> 

### Meeting Date/Time: Thursday 2021/03/11 at 14:00 UTC <!-- omit in toc --> 
### Meeting Duration:  45 minutes <!-- omit in toc --> 
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/208) <!-- omit in toc --> 
### [Audio/Video of the meeting](https://youtu.be/s017DQlsCCw) <!-- omit in toc --> 
### Moderator: Danny Ryan <!-- omit in toc --> 
### Notes: Alita Moore <!-- omit in toc --> 
### [Previous Call (58)](https://github.com/ethereum/eth2.0-pm/issues/206)

-----------------------------

# Contents <!-- omit in toc --> 

- [1. Client Updates](#1-client-updates)
  - [Nimbus](#nimbus)
  - [lighthouse](#lighthouse)
  - [Teku](#teku)
  - [Prism](#prism)
  - [Lodestar](#lodestar)
- [2. Altair](#2-altair)
- [3. Prater](#3-prater)
- [4. Research Updates](#4-research-updates)
- [5. Spec Discussion](#5-spec-discussion)
- [6. General Discussion](#6-general-discussion)
- [Annex](#annex)
  - [Attendees](#attendees)
  - [Next Meeting Date/Time](#next-meeting-datetime)

## Action Items

Action Item | Description
| --- | --- |
**1** | Danny to review Afr Schoe's PR and get it merged 

## Decision Items

Decision Item | Description
| --- | --- |
 **1** | Push back Genesis one week and then start passing out validator keys (Genesis is in two weeks)

-----------------------------

# 1. Client Updates
Video | [5:30](https://youtu.be/s017DQlsCCw?t=329)

**Dannny** - Okay, great. The stream should be transferred over and here is the agenda will go over to some client updates and we're talking about Altair which we have the final little bits to decide on and then we can do a pre-release from there. We'll talk about Prater. I know the status seems to be a little bit in limbo research updates General discussion. Okay. So today we can go ahead and get started with nimbus.

## Nimbus

**Mamy** - Okay. So we've had or one point zero point ten release this morning. We skipped 1.0.9 There is almost no difference between them except default. So the main things in the release, we updated or vlst and versus the library and we are so includes. Up-to-date list of trusted root certificates. So we recommend you upgrade to one point zero point ten and also we are compliant with the 1.0.1 spec which only includes respond update to the if one withdrawal credential we fixed a number of bugs in particular one that affected the pole where we had a crush on some Hardware configurations if you build a nimbus from Source, we also fixed some long processing delays that were triggered when we receive at the stations that were actually to prevent the states from before finalization. We have better p2p pure management because we had a lot of negative collection and actions that could be accumulated and we have fixed false positive in doppelganger detection when an node decisions while so received after significant delay and in terms of new features as the highlights of the release is improved format of the slashing protection database. We will roll out the update in one point zero point ten and the next version. So in this version, we will have nimbus supporting both sold and the new format to have easier rollbacks if needed, but we hope we don't need it and something from next version it will significantly improve reduce these clothes when you have a large number of validators. So thousands or more mainly for us on puremont. But if we have a large stickers that would be helpful for him as well. And we have also improved the automatic configuration and detection of external IP addresses. 

## lighthouse

**Mehdi** - Hey everyone. We've also had a release about 24 hours ago. One point 2.0 includes several improvements to Lighthouse stability and performance same as names. I guess particularly for users running multiple validators one of the cool optimizations that whole landed effects are block production times. I believe you managed to reduce that by four times by introducing a block browser cache and also running slow processing before the actual proposal. We're handling better early blocks just gonna be good for the overall Network. We started pruning the status protection database periodically to essentially prevent from it being oversized and slowing down the signing. We've removed the public key case file which cause a few issues historically and we're storing that information alone database. We've added the ability for users to set the graphing from files also updated on the others Library apart from that some of us have been going through the heart folks back Michael provided some extensive feedback. Yeah. That's pretty much it 

## Teku

**Meredith** - So we've been focusing on upcoming hard fork; we made some good progress on refactoring Beacon State and Beacon blackbody data structures to support versioning. We merged in an implementation of the fork Choice balanced attack mitigation. Although we still need to do more testing and performance analysis on that. We spent some time looking into the blocks lat pork Choice change. We merge some initial refactorings as it looks like this isn't going to be included in altair. And we have a pending config update for the new Praiter test net. But we're waiting on the upstream PR to be finalized before we merge that that's a like that thanks.

## Prism

**Raul Prysmatic** - We have been also working a lot on the hard fork preparation and you know similar to teku just making sure that our data structures are you know can last the test of time we don't want to make we don't want to have a lot of crazy conditionals or spaghetti code as a as there are more folks in the future. So just a lot of thinking ahead a lot of preparations a lot of refactoring to ensure that it's maintainable more further work on the standard eth2 API. We've been working on our optimized slashing implementation. Hoping to release that by the end of this month and aside from that. Yeah, just how to release fairly minor just you know, some improvements runtime improvements and helping improve the experience or stakers. That's pretty much it great.

## Lodestar

**Cayman** - Hey everybody. So we are also working still working on getting altair compatible. So just a lot of refactoring. We just finished refactoring the gossip validation and handling to support different vorks. We also been doing a lot more profiling and adding a metrics just to kind of help with some of the performance issues. We see in the past. We just fixed a memory leak that's haunted us for months and reduced a lot of memory while we're sinking. So things are looking good on that front. And finally we're working on just proof of concept lightclient things right now, like right now it's looking like exposing the like light sync updates and multi proofs on some endpoints and working with like request and response of those things. And then the last thing is we are working on like weak subjectivity state infrastructure, and I'm kind of curious how other teams handle this like how do they distribute these states or put frequency? They're updating them and maybe we can ask that question later.

# 2. Altair
Video | [13:01](https://youtu.be/s017DQlsCCw?t=781)

**Danny** - Yep, bring that up. Thank you. Okay, let's move on to discuss Altair there is kind of a large PR that have asked an overview to review that had this 64 Epoch boundary processing update. Where essentially when there is emptiness like empty blocks you forgo processing a lot of pretty much everything most of the validator set until these boundaries to reduce the load based upon feedback from a number of the engineering teams. It's unclear whether this is the proper optimization. It kind of targets first and foremost computational load whereas it is unclear exactly how disk IO comes in and whether that can be optimized in a similar manner and so to that it's also a relatively deep future. So to that end I would recommend not putting this in Altair it seems like that's the recommendation of engineering teams and that any such optimization to the spec should probably be a company with some like Rd on at least one client and some data driving it is anyone up there's also another feature that was in this that is validator independent leak inactivity leak. And so there's a leak score array like score list that was pulled out into a separate PR so it can be considered independent. We can talk about both these things, but first and foremost, is there anyone opposed to leaving this 64-epoch feature boundary out? I know discuss the soft line. I just kind of want to let anyone error any grievances. Okay, so there's an independent PR on the league scores. This is a very nice feature and when it's independent, it's actually relatively thin and I think a very manageable and a good thing to put into Altair. So there's that PR with some testing and it's ready to go in. I guess I'll merge that this afternoon unless anyone has some issues here or has a chance to take a look at the day and wants to speak out against it. I think it's a much clearer cleaner future than the other and is not overhead impliment. And specifically this attempts to resolve some of the issues that we saw on the testnets where you have say a week of leaking and then you get to finality and then the leak restarts and then you drop, you know, one percent and all of a sudden you're not finalizing again, whereas this offlinededness is kind of tracked independently of each other validator. And so if that leak started up again and they hadn't come back online they kind of start where they were and that quadratic leak. This helps kind of the network result partitions in a much cleaner way. Any comment on that? If not, please if you want take a look at it. Otherwise, we're going to merge this this afternoon and preparation for I think tomorrow's pre-release. Okay. Now we've seen some conversation around blocks lot edited. You want to give us kind of the status update and what we're thinking on this.

**Aditya** - Yep, so I have two pending for Choice pull requests that are open. One of them is 2197, which is blocks slot. The other is to 101 which was randomized timing for at a stations and block production. It looks like we are definitely not going to include them in hard fork one and we are most likely going to abandon these because of some issues with how these fixes work and whether they actually solve the underlying problem so we are definitely going to not include them in hard fork one and how we can include them later whether that becomes a hard fork or just a point of coordination that is up for discussion and we can take it on when we have a concrete fix in mind.

**Danny** - Yeah, so especially with blocks lot the solution might be worse than the problem. If not, if we don't add any additional mitigations and that puts a pretty significant for second. Assumption on latency and the blockchain just kind of becomes live not live in sin when there is longer than that on block propagation times, which is not great. So we're investigating a bunch of other stuff. We're hope to bring some other people and to think about this problem and there's some leads but it's just not ready to put into this fork and point of coordination in terms of the aditya right in that most Fork Choice changes as long as they're not contentuous with a consensus like a state transition change can be done outside of a hard fork but there's also a potential that it could be coupled with a consensus change. So we shall see some of these attacks are somewhat exotic and probably pretty unlikely to be seen in the next six months, but we'll keep our ear to the ground in case they work. Okay, there's a open issue on that age opened up in January to 183 and there's a pending there's a fix out for that right now. Essentially. It's a removal of an aggregate after station propagation condition that was kind of short circuiting. It wasn't doing what it's supposed to do because of the way the interplay with message ID and and some of the way gossip soap works was actually probably inducing more load on nodes than it than if it were the attempted optimization were not included. There's a PR for that this we too will likely merge today you could potentially do. An alternative that does like a type specific message ID my gut is that this is probably not worth it, but we can chat about if anybody has any thing to talk any recommendation on it right now. Let me know. Otherwise check out this PR that's 2225 and the accompanying issue we can chat there, but this will likely go in very soon.  Okay, and then we have some exciting test format updates coming out is show way on the call know Proto.. would Proto are shalae we say would you like to talk about the changes and test updates actually Proto? You probably have a better handle on that with the snappy compression. Can you give us a tldr?

**Protolambda** - The rustest PR opens in October last year, but introduced compression to the test formats. So that is going to take as much as like 10 or more gigabytes of this data, but rather like half a gigabytes, so you're tests would have to go through this compression step that aside from that. It's an improvement in the like a large improvement in the test size and then later on we had this issue opens about further improving that those test formats everyone kind of agreed on compression. So we're leaving it at that's right now. Maybe in the future we'll have a more sophisticated customers with deduplication. But right now this seems like the better and more direct option to reduce the test size for the next hard work.

**Danny** - great in the numbers ran in October I think werre reducing the outputs from 11 gigabytes like half a gigabyte that's probably changed now with an additional Fork that still very significant. And this just adds in dot SOC Snappy extension rather than just SOC and we also removed the dot yaml versions of states and operations, which from our understanding and investigation in October there weren't really used by anybody. Okay, and showei what's the status on fork choice tests? Are we going to have maybe a sample of that coming out in the pre-release. 

**Hsiao-Wei** - Yes. So currently the PR 2202 has shown with a preview of the incoming test format and it's follow-up of Alex Vlasov's previous work. I think it was discussed on the to state tests repo. So there are some differences between the previous proposal and this proposal. Mainly it's for making it more easy for high-stake to generate the test. So you can if you want to see the test vectors there example of the get hat test and you can check the states file, which is it's kind of like a our beta configuration, but it shows us other states that the client has to check and checks is basically like the assertions like you have to check the value if it's equal to the test vectors and we have the block and attestations files in the test vector output so currently I use just attestation and participation has roots to present the file. But I'm thinking I can maybe just use the first eight bytes or like four bytes to make the filename shorter. Yeah. So if you if you have time, you can check the test vectors up to 202 and see if it would be like some drawbacks in this PR right now. And if there's no further issues, then I will first compute to get testnet for clients to try out.

# 3. Prater
Video | [26:23](https://youtu.be/s017DQlsCCw?t=1583)

**Danny** - Great. Yeah, so check that out any questions for show a or Proto on some of these test format updates. Great, and as it is a pre-release if you get into it, and there's something that totally didn't make sense in these new formats. Just let us know and we can iterate. Okay, next I want to talk about Prater a freeze on the call who has put together that PR and there's been some coordination. Although I'm not quite certain the status of launch and things like that. So afri or somebody else want to give us an update on where we stand.

**Afr Schoe** - Yeah, sure. So I missed last call so kind of the back story was from how I understand it is we wanted to front run main-net with the test net. It has significantly more validators and we want to propose this test net project with bit more than 200,000 validators and instead of spamming the Goerli test networks a lot of deposits we decided to pre-populate the Genesis with certain amount of validators and Proto was so kind to write a small go tool to generate test net canisters from a handful of seeds and this PR on the eth2 testnets repository is ready to go. So we took genesis type from the deposit contract on Goerli which was I don't know 11 days ago and had half a custom Genesis delays that puts it to I think next week on Wednesday, which should be the 11th or 16th of March and this is ready to be merged and I think unless anyone has any comments on that we can move on with this and look forward to Genesis next week. Yeah regarding genesis validators we have pre-populated genesis with 210,000 validators. I'm not sure where we stand regarding the regarding the just put this up here. We have a spreadsheet. I opened all the links except this one. So let's for each client teams 40K validators. We probably finished distributing the keys before the weekend, hopefully and then we can make sure that everyone is running their validators next week. I don't know Proto. Did you hand out any keys yet? 

**Proto** - No

**Danny** - I just want to make sure that client teams are ready in terms of infrastructure and have time before Genesis to get things done.

**Ben Edgington** - Yeah, so I flagged earlier on the Teku side. So we were advised that the signal to fine like that everything was final would be the merging of the pr; so it hasn't been merged yet so we haven't done anything and less than a week just isn't enough time either to bake the Genesis State into a release or to get the infrastructure up and running. Reliably, I mean. It's a lot of infrastructure to run this this number of nodes. So we I think We would propose we would request putting back Genesis by a week just to allow us to get a release out with the Genesis data in and just to make sure the infrastructure is in place without having to rush and work the weekend and all of that.

Decision 1 | Video | [30:10](https://youtu.be/s017DQlsCCw?t=1810)

    Push back Genesis one week and then start passing out validator keys (Genesis is in two weeks)

**Afr Schoe** - Just perfectly fine for me, it's just so I can push this back one week, regenerate genesis, and then we start to distribute the keys and everyone should have enough time next week to prepare our clients and set up validators.

**Danny** - Yeah, it's totally fine for me. This isn't this is something we need to do and we've identified that we need to do. But it's not critical that it happens next week. So I'm all right. And will the PR be merged or will it stand as is for the next week? But we have all agreed that it's happening. I don't just process your thoughts so I can merge.

Action 1 | Video | [31:06](https://youtu.be/s017DQlsCCw?t=1866)

    Danny to review Afr Schoe's PR and get it merged

**Afr Schoe** - I mean, I have write access, but I was hoping that someone else could just say, OK, this looks good or something or someone else merge it. Just so we know this is fine to go. I mean, I can merge this if no one has time... 

**Danny** - make the make the update to the Genesis time and maybe pinging on discord. And I will certainly do a review with a explicit approval and maybe others will, but we can merge from there. I think we're all in agreement that Genesis is in two weeks.

**Proto** - And make sure to have the correct states in your client's changing. The Genesis time also affects the stateful.

# 4. Research Updates
Video | [32:00](https://youtu.be/s017DQlsCCw?t=1919)

**Danny** - Ok, so is there anything else people want to discuss around Prater before we move on? Excellent. Let's do some research updates, maybe we'll start with Mikhail. I think you have some stuff to talk about.

**Mikhail** - As things stand, there is like the open PR with the merge stuff to this spec repository, it contains like the executable beacon chain proposal. So drop it in chat now. Now, this is like a good time to start looking at it and so forth. It should be fairly easy to reason about because the amount of change, that's not that huge.  It requires some like upcoming work, like we can expect executable running tests and grading new tests and so forth, but yeah, it's ready to be ready for everyone to start looking at it. So that's pretty much it on the merge.

**Danny** - Good. Thank you. Other research updates?

**Vitalik** - Nothing on the eth2 side for me this time around.

# 5. Spec Discussion
Video | [33:41](https://youtu.be/s017DQlsCCw?t=2021)

**Danny** - Moving on, it was the state of kind of recertativity, recertativity state distribution and things like that was brought up by caymen in at the start of this call; Caymen do you want to pose a question or is anybody else want to kind of get the state of what people are considering?

**Cayman** - Yeah, I'm kind of curious just how you are generating the state and then distributing the state. If anyone has any thoughts.

**Danny** - Aditya what's the status of kind of the format to distribute states and some state providers and stuff in the network right now.

**Aditya** - The last time we talked about this, the status was that we are just assuming that we shared the state in alternate channels, maybe tied in to somewhere else. We haven't talked about how to share the state over the ETH2 P2P network. We can try to think about how we can compress the state or break it down into simpler pieces and reduce the load on our P2P network. The main problem seems to be that state sizes are running into a couple of NBs at least, and that would kind of weight down the P2P network a lot. So this would be a larger research problem to think about.

**Danny** - Yeah, I understand. Is anyone planning on cutting these into their releases and others kind of a back and forth on that many months ago?

**Meredith** - We had talked about it at one point, but we never got around to it.

**Danny** - I think that we there's definitely a desire to kind of have this machinery in place around Altair, so it's probably worth us running through some of the various scenarios and making sure the machinery is in place. Do the command line options generally exist on clients today to be able to start from a state rather than from Genesis.

**Ben Edington** - For Teku it's a yes

**Mamy** - we have something in Nimbus, but it's not tested

**Mehdi** - Yeah, Michael's working on this. I think that's the branch that has that feature, but certainly not stable.

**Terence** - Preston is working on this as well. 

**Danny** - OK, good. So I think and this has been recommended in another context with the kind of targeting this to be in a version one for Altair, although it doesn't affect kind of the core specs precisely, I think is a good a good target. So we talk about it off line a bit and we'll bring it up in the next call as well, kind of check checking on status, I was anything else to talk about today? I know there's kind of a lot of nebulous items related to that that aren't so clearly defined. If people want to chat about them more now, by all means, otherwise we can chat about offline.

**Mikhail** - I have like one thing that I would like to share as well, it's related to the merge and pull request, but yeah, so I'll drop it in the chat. This is like the proposal by Dan to which is about deferring the execution by a slot. So the idea behind this is to give more time for testers and for Proposers To execute transactions of the previous block, it has its own trade offs, but would be great to chat about it, discuss it. Those who are interested.

**Danny** - So isn't it delays the commitment to the state route until the next slot so that you can continue computation throughout the entire slot, right?

**Mikhail** - Yeah, right. So like the proposer of the block is like the, uh, is like the sequencer for the current application payload and the executor of the previous one. So that's the idea.

# 6. General Discussion
Video | [38:52](https://youtu.be/s017DQlsCCw?t=2314)

**Danny** - Okay, moving on to general discussion, just general discussion, anything else you want to talk about today?

**Vitalik** - Anything about merge plans to talk about or do we still want to have more time to formulate the options?

**Danny** - Options with respect to..? 

**Vitalik** - speeding it up.

**Danny** - So I think the next thing that we plan on doing is during the next call, maybe next week, definitely by the following week, to kind of invite at least an hour from each team to begin allocating resources to it. That's the main speed up other than getting specs written, which is now in the works. I mean. And I think you and I have talked about this, a number of Mikhail and I've talked about this and that there are the way the specs are going to be written are going to be very the most minimal merge on the first pass. And that's the first target people can begin working on. And that can even be what we bring to bring to mean that that might forgo a handful of features, including, say, validator withdrawals. You could go to main net without that and do a fork three or four months after. So definitely in terms of speed up, that's also the strategy is to really scope the tightest version of it.

**Mikhail** - And like the what also was discussed for a bit is like the consensus upgrade is what they to separate it from the version, the application chain with the beacon chain, which means that the application chain similar to beacon and and this like merge in the chain is going to be like the separate.
Upgrade that through. The governance and other procedures

**Danny** - right, and some of that might seem a bit abstract, Mikhail and I are both working on kind of technical roadmap documents that we plan on sharing soon that show kind of the dependencies and the middle version of the merge and things like that. So we can make it more concrete soon. Anything else today?Ok, very cool, cool, I appreciate it. We are on the final little bits of getting a temporary release out to you. Thank you for sprinting ahead, taking a look at those features and getting ready. I imagine there's going to be kind of a round of feedback there that we're going to want to do. And implementaitons they're going to want to do before we set a date, but definitely still targeting that approximate June date.

------

# Annex 


## Attendees 

- Mamy
- Danny
- Trent Van Epps
- Terence
- Mehdi | Sigma Prime
- Carl Beekhuizen
- Mikhail Kalinin
- Dankrad Feist
- Alex Stokes
- Raul Jordan
- Aditya Asgaonkar
- Leo @ BSC
- Meredith Baxter
- Ben Edgington
- Hsiao-Wei Wang
- Lakshman Sankar
- Cayman Nava
- Protolambda
- Ansgar Dietrichs
- Afr Schoe
- Justin Drake
- Preson Van Loon
- Vitalik Buterin



## Next Meeting Date/Time

Thursday, March 25th, 2021, UTC 14:00.
