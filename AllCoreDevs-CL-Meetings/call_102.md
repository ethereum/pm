# Consensus Layer Call Meeting #102
### Meeting Date/Time: February 9, 2023, 14:00 UTC
### Meeting Duration: 1 hour 30 mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/711)
### [Video of the meeting](https://www.youtube.com/watch?v=YMu50yNUz5Y&ab_channel=EthereumFoundation)
### Moderator: Danny Ryan
### Notes: Rory Arredondo

-------------------------------------------

## Summary and quick contemporaneous notes from [Ben Edgington](https://hackmd.io/@benjaminion/BJcVqOzpj)

## Intro

**Danny Ryan** (8:22) - Test test test.

**Gajinder** (8:24) - I'm on too. Hello Danny. 

**Danny Ryan** (8:27) - You can hear me?

**George Kadianakis** (8:30) - Yes. 

**Danny Ryan** (8:30) - Could you not hear me when I kicked off the call? Like a minute ago? No?

**Marius Van Der Wijden** (8:39) - Yeah, we could not.

## Capella
## Devnet updates

**Danny Ryan** (8:46) - I'm sorry. We're kicking off the call. Can somebody give us an update as to the current Shapella testnets?

**Barnabas Busa** (8:58) - Yes sure. So we just had two days ago Shadow fork on Zheijang testnet and we would like we had a great success. I feel like we managed to pull everything off. We didn't encounter any issues actually.

**Danny Ryan** (9:25) - Did we send bad blocks and things?

**Marius Van Der Wijden** (9:29) - No, we didn't. I don't think we should on this Public testnet. But one issue that we found is some Geth nodes syncing up would encounter bad block and no. The issues most likely that some client is not RP encoding the block correctly. And so we most likely will not 100% sure. Most likely we get a block from the network that is not encoded correctly, we decode it and then at some point we error because instead of the withdrawals being an empty list, it is nil and so our encoding and decoding is correct, we check that. And so yeah, I would encourage all other execution layer clients to also make sure or create a test that they encode and decode withdrawals correctly.

**Barnabas Busa** (10:51) - This did not happen when you're thinking from genesis right?

**Łukasz Rozmej** (10:56) - Yes. Like it it can happen if you sync from genesis. It's dependent on the peer that gives you a block to block. Like the peer might give you the block in like in a wrong (inaudible). And so, yeah, it really depends on the peer if this block corrected or not. And usually, we would, we would, like discard these blocks in an earlier stage. But because it is a valid RP encoding, it's just the wrong RP encoding. We only find this when trying to execute a block.

**Łukasz Rozmej** (11:00) - Nethermind, but can you maybe like block this peer when this happens? Especially on the network? 

**Łukasz Rozmej** (11:54) - Yeah, well, the problem is that it's it's very unreliable, because it only happens on on empty on blocks with empty withdrawals, which is only the first one I think, because now we have this withdrawal credential set. I can I can try to I can try to do more things and see if if like there's there's a lot of things that have to go right for for for us to notice this right. We have to think this specific block from this specific from one peer that like, that has this block. And so yeah, I can try.

**Danny Ryan** (12:40) - You could presumably just ask for that block for a bunch of peers, but people can also just look at their code.

**Łukasz Rozmej** (12:46) - Yes I think everyone should just should should create some unit tests.

**Barnabas Busa** (12:54) - I can also just spin up a new network where we don't do any BLS changes, and then this would be a very small number. That we would be able to test this. 

**Łukasz Rozmej** (13:05) - Yeah, and I think in the end, we will we will probably be able to reproduce this with a with a hash test with the hive sync tests, but we don't have those yet for post Shanghai.

**Danny Ryan** (13:32) - Okay, thank you, Marius. Yeah, I mean, even if we find a new testnet this should definitely end upstream and you know, test so let's take a look. Anything else on this testnet?

**Barnabas Busa** (13:50) - We haven't done too many of BLS changes on it to allow different users to test their withdrawals and BLS changes. So I don't even intend to do any more of them. So if we need to do more BLS changes, I would advise to just spin up devnet seven I think we can do some more of that. But I'm just curious if anyone has been asked to do some BLS change testing?


## Relayer/builder testing


**Danny Ryan** (14:32) - Yeah. Does anybody else need devnet seven to do BLS change testing or hope we hit that sufficiently another (inaudible)? My gut is that people are pretty comfortable with that at this point. Okay. Someone raised relayer builder testing. I believe this has not yet been tested on any of the devnets nor on the current testnet. Does anybody know the status of being able to test these (inaudible)?

**Barnabas Busa** (15:17) - I have tried to reach out to Flashbots regarding trying to get someone on board on to this new testnet. I have heard nothing back.

**Terence** (15:30) - Alex's latest update he say that he has a implementation from MEV boost that's Capella ready, so if anyone wants to pass they can ping him. But I think the (inaudible) here is just to have a (inaudible) there and builder that is what's missing. today. So yeah, the sooner we can get through that the better.

**Gajinder** (15:51) - Lodestar is also Capella ready to test the (inaudible). 

**Barnabas Busa** (16:03) - Is this something we should be testing on Sepolia only or should we bringing it to the public testnet, not to just launch.

**Stokes** (16:09) - Do you mean Zhejiang or another one? 

**Barnabas Busa** (16:14) - Yeah that one.

**Stokes** (16:16) - I mean, yeah, the plan is to test on Zhejiang as you know, things are ready in time. If we fork Sepolia then we may as well just test there. But yeah, that'd being said, I know Flashbots is working on getting something ready. And I think in the next couple of days, if not next week, so pretty soon.

**Potuz** (16:39) - I think we shouldn't even talk about forking Sepolia without testing first the builder.

**Marius Van Der Wijden** (16:50) - I disagree.

**Stokes** (16:52) - Yeah, I don't think we should really wait because there's no reason to. So all clients have a fallback in the event that this MEV boost pipeline fails.

**Danny Ryan** (17:07) - Any other inputs on that? I do think if we're moving toward assuming the order Sepolia, Goerli, mainnnet if we're moving into Goerli and haven't had this test today, I think we should certainly be having a conversation about timelines and and making sure that it gets tested.

**Dustin Brody** (17:30) - One concern I would have about not testing this before Sepolia is that there are we have basically two chances before mainnet to test to test the transition the fork transition behaviour of this and to the degree that there's anything particularly interesting around that they won't be, then that's it. Like we have Sepolia and we have Goerli and that's it. And so it's I think adding that one chance by having some kind of devnet or some some other situation where we can get some sense of what the builder, relayer are gonna do and the different clients are going to do is useful I would agree with Potuz on this.

**Danny Ryan** (18:24) - So at least, we're about to talk about timelines, the date tossed around 27, 28, so we're talking about 20 days. Those that have been working on MEV boost, those have been talking to two Flashbots and others is that a reasonable timeline to have this up on Sepolia. Is that the expectation here?

**Stokes** (19:01) - I think it's hard to say without having people from Flashbots here. I was just looking, I don't see them on the call. But yeah, definitely that would be the intention.

**Danny Ryan** (19:12) - Got it.

**Barnabas Busa** (19:24) - Moving forward with forks, I don't think Flashbots is going to move forward with development. So I feel like this is something to (inaudible).

**Tim Beiko** (19:35) - Right. I do think generally like we've not sort of waited on infrastructure providers, and mostly because of that reason, like the protocol already moves pretty slowly. And so if, like, We're not the ones to sort of set the pace then the fork just never makes it to the top of teams priority list. Understand MEV boost is like a different than something like say Infura like that. But yeah, I think there's sort of a risk if we started sort of moving your timelines based on everyone in the ecosystem being ready, that will sort of be be blocked by by the slowest ones. 

**Danny Ryan** (20:25) - Potuz?

**Potuz** (20:27) - So the way testing works is, so we're gonna go without having ever tested a builder. And 95% of our blocks go through builders currently. So we have a couple of stages that that will save us. The first one is that if there is a bug and the bug is in the builder, not in the relayer then we're just going to pull back to the local execution. This is not really being tested at all either. Then there is if there's more serious bugs and blocks start missing because the bug is in the relayer, which again, hasn't been tested. Then we're going to fall back on using using this this check that if certain number of blocks are missing, we're gonna hold back to local execution, but this also hasn't been tested. So we have like an entire system entire fork, which is hanging on completely untested software. I don't feel comfortable at all, signing off my own clients, my own work on something that I haven't tested.

**Danny Ryan** (21:38) - I hear you, is there a reasonable way to test those flows on our testnets? Because I think that's ultimately what this group can be responsible for. And I think given a MEV boost implementation, we can very likely hit both of those. Right?

**Potuz** (22:03) - I think it's very easy for us to agree not to support MEV boost at the fork for a while and just ship at a later date a fix when the builder is actually tested. We can agree that every CL client is not going to support MEV boost at the fork. And fine if if there is a pool that actually wants to fork our clients and risk it so be it.

**Tim Beiko** (22:32) - And what does it mean to not support MEV boost? Is it yea I'm curious how you would frame that.

**Potuz** (22:38) - (inaudible) execution, right, so we can easily afford a local execution on a Capella block. 

**Tim Beiko** (22:46) - Okay so not even just be because you can imagine a softer version of this where you just put like a big warning, right like where you just say in the docs or whatnot like you know, this is untested with MEV boost, run it at your own risk. But you're saying you go a step beyond that where the default code paths are turned off. Is that right?

**Potuz** (23:10) - I'm saying that the only two reasonable things in my mind either waiting until this is tested, and then delaying the fork until we actually have tested this or just disabled MEV boost support, disable any non local execution on the CL clients until this is tested.

**Sean Anderson** (23:31) - So I mean, it's off by default. And I think that we shouldn't have the timeline be defined by external like infrastructure. And we can test as much as we can test which is specifically like the consensus client interaction with MEV boost/the relay. Because we can make like fake relays but we like I don't think we can just wait for Relay implementation to appear.

**Danny Ryan** (24:10) - And there's definitely some comments in the chat worth servicing. I think people are worried about the precedent of getting hung up on infrastructure providers. I think it's also people would be deciding between the profits that they are seeking or not having those versus running non canonical forks. Also, those large infrastructure providers, or large staking providers are going to have private MEV regardless or around forked clients regardless, so then you get the highest symmetries between those types of providers and home stakers. Are there any other comments people want to service from the chat or on this in general?

**Stokes** (25:03) - One thing I can add is around the merge. We started work on some kurtosis test to test the fallback and like an automated way. That's something we can definitely send back up and running. I do think it makes sense to do what is within our control and then separately you know, Flashbots, whoever others timelines or their own timelines. 

**Danny Ryan** (25:27) - Right. And we aren't just I think that's important. We're not just talking about Flashbots. There's a whole ecosystem of people that run relayers and builders that are highly incentivized to do this, even not on our timeline.

**Tim Beiko** (25:43) - And also, it's worth noting, so like, say, we talked about forking Sepolia late February which is still like 20 days for now. I don't believe there's any like living in builder infrastructure set up on that that builder infrastructure is set up on Goerli, I believe. So that means you probably have another week or two, you know, before you fork the Goerli, assuming Sepolia went well. So then you're sort of like, I don't know, call it like early mid March, which is, you know, over a month from now. And then after Goerli you probably you know, I think Goerli is when you'd want to see hopefully something like MEV boost be ready and relay implementations be sort of ready to support it. Doesn't seem like a month is like insanely short timeline. And then even beyond that, you would get a couple of weeks after Goerli forking before the mainnet upgrade. So I think basically the sort of timeline pressure we would be putting on by by moving to Sepolia now is something like in the next month you know, MEV boost MEV boost software providers would need to like, be ready, and I yeah. It seems kind of different to say that than say like a week from now they should be ready.

**Danny Ryan** (27:16) - So it seems like we could potentially test backup flows in Kurtosis we could potentially test backup flows in Hive, although I don't know if MEV boost is integrated in Hive at all right now. And we could potentially test them on a transient devnet. Do we have the resources to do so I know that we don't we wouldn't be testing necessarily be Flashbots relay at that point, but we can certainly sanity check that these code paths that we care about work.

**Stokes** (27:52) - Yeah, and it's worth calling out that you know with this fall back like it almost doesn't matter when other people you know, do their thing. For example, if Flashbots doesn't update software in time then like the very first step will fail and you'll fall back to local production and you know, the chain will be fine. So it's I think, mostly important to focus on that.

**Terence** (28:13) - I guess the concern here is that we haven't even had a fallback so that we don't believe the (inaudible) back will work at first place.

**Sean Anderson** (28:23) - We've actually hid it in Lighthouse on a testnet in the past but not with any of the current code.

**Stokes** (28:36) - So we can definitely. Go ahead. 

**Dustin Brody** (28:40) - Sorry. One concern is that from for me that it's, it's not I mean, people are articulating these scenarios where either just works or it doesn't work. And my concern is sort of the broad middle ground where it's kind of glitchy it's technically there, all the clients fault. Okay, maybe not this year but but like most most of the clients may be claimed to support it Flashbots came to support it, but it's basically just not been tested all that well. And and then it's if nothing else, setting this expectation of will the fallbacks be expected? There will be a lot of support requests, I think that case of people expecting it to work, but not expect experiencing it not working for any number of reasons. So either so this is my concern, not just like that it will not work. Or it will work. Even if the fallbacks work as designed as in theory they should, then I think there's a downside risk for the CLs.

**Stokes** (29:45) - Right so I think to mitigate that risk, we want to do like a staged rollout. So like you know, let's say that none of this stuff is ready in time for like Shapella then like we basically are using the fallbacks and then each ranking team can decide like, once they feel comfortable then you know, basically add support for the new thing.

**Dustin Brody** (30:13) - Sure, that's that's one approach.

**Danny Ryan** (30:21) - Okay, I think importantly, it'd be really valuable to ask these fallbacks in more automated way. Or at least in a in a devnet. Does anybody have a vision for how to do that or do we need to take this to an issue?

**Stokes** (30:47) - Does anyone know what the status of like Hive would be? I think we feel pretty comfortable with working on Hive. Otherwise, yeah, I can work on the Kurtosis stuff.

**Mario Vega** (30:56) - Hi. Currently there's no support for any MEV boost related stuff in Hive. We need to rework Hive in order to be able to test anything.

**Stokes** (31:10) - What does reworking just like? Is that involve like invasive changes or just like adding support for the new piece? 

**Mario Vega** (31:19) - I don't really know how much of a change it is, but it's not. It's not something that we instantiate in clients currently with. So at least the configuration and all that should (inaudible). But yeah, to know how much deep deep of a change it is, I need to take a look.

**Stokes** (31:41) - Okay. I mean, I think most of what we need to do (inaudible) has already been done in Kurtosis. So I'll start there and I'll circle back around with you. 

**Danny Ryan** (31:50) - Okay, and Pari says Barnabas and I can work on a transient testnet, we can set up a mock relay and then MEV boost on enough nodes we can disable the mock relay to test a fallback, so that that will test the secondary fallback, which is when that'll test the primary fallback, but it won't test the like, fallback in which the relay sends a bit and then does not send the full block. Nonetheless, I think what tests

**Sean Anderson** (32:23) - Well, there's no fallback there anyways, right?

**Danny Ryan** (32:26) - That's the if I don't see enough blocks on chain I stopped using MEV boost so that that is (inaudible).

**Sean Anderson** (32:36) - Yeah. We could we could also test those scenarios on a transient testnet though because we could just like

**Danny Ryan** (32:41) - Oh right, we can just turn off the (inaudible) validators. Okay. Okay. Pari, Barnabas, let's make a plan outside of this to test those fallbacks. Simultaneously, let's hopefully get Alex's MEV boosts in some sort of testing tested form. We can dig into Hive support as well. My gut is to not currently halt Sepolia but to paralyse a lot of these testing efforts and continue to assess over the next couple of weeks.

**Barnabas Busa** (33:29) - I think personally, that MEV should not affect at all, Shanghai.


## Sepolia fork date


**Danny Ryan** (33:40) - Yeah, and I believe there's certainly a contingent large contingent here that that agrees. I do think that we can do a lot more diligence on on testing what we're in control of though. Okay, anything else on builder relay boost? Okay, the next item, which we've been partially discussing, is Sepolia fork date. On the execution layer  call last week, it was a general agreement if the current testnet went well, to pick a Sepolia fork date. I've seen discussions of end of February. So that's something like the 28th to put it on a Tuesday. That's about 20 days from now. Let's open it up for comments on potential dates, or rejections of readiness. 

**Tim Beiko** (34:56) - Maybe just one thing there if we fork on the, call it the 28th, I think it would be great to have the blog posts out at like you know, the 20th, maybe the 21st. And so that means ideally, we get client releases out like next Friday, or the Monday after that, like, I don't so just to put it in perspective for client teams. 

**Danny Ryan** (35:22) - Right, so a week lead time and Sepolia which is a dated validator set is probably correct but that becomes you know, week and a half release lead time. Right, I actually I was saying Tuesday because of our biases when we're testing proof of work forks, we wanted to make sure it didn't accidentally land on the weekend, but a Monday fork is actually fine because we can well time it. So Barnabas did say the 27th at 2pm UTC, which is epoch 56700.

**Tim Beiko** (36:07) - One thing that's nice with the Tuesday is people who forget, have the Monday. Like we can kind of make it last call on Monday for people like infrastructure providers and whatnot that's like the fork is tomorrow. So I have a slight preference for the Tuesday but not a hill I would play on.

**Danny Ryan** (36:34) - Sepolia is a closed validator set but it's also they are humans and we've seen issues before.

**Barnabas Busa** (36:47) - I'm not a human. 

**Danny Ryan** (36:51) - Did you say I'm not a human? Fair. Okay, I think the I think a Tuesday date given people waking up on Monday and saying oh shit and doing their work. Accounting for that is probably reasonable here. I don't think we gain or lose much in that plus or minus day in that realm. Can does anybody fundamentally opposed to that as we also parallelize our builder relay while back testing? Okay, opposition, we will do this as default but we will circulate this in public All Core Devs for the next 24 hours before this begins to be announced, etc. For anyone who is not here to speak up, but I think we're in pretty good shape to move forward. I will say that Paul did leave a comment. He said March 27. And that we're very comfortable moving forward march 27. I think he meant February 27. Can anyone from Lighthouse comment on that?

**Sean Anderson** (38:16) - I also think he meant February 27.

**Danny Ryan** (38:20) - Okay, great. Okay. So Feb 28th. We can do a look at Adrian's tool, it's on Symphonious and pick a fork epoch. And in the next 24 hours, we'll kind of put that up an issue. People with thumbs up and we'll keep moving. Okay, anything else on Shapella for today?

**Barnabas Busa** (39:06) - Any discussion (inaudible) maybe? Or would we want to wait till Shapella's finished?

**Danny Ryan** (39:16) - I think especially given the builder relay testing that we want to achieve that we should put that more of a discussion point at the end of February. Potuz?

**Potuz** (39:30) - It actually if if we go with Sepolia, it would be better for us to actually have a date or a tentative date, so that we can include it in today's release or in next week's release. So that we don't need to make three releases before mainnet.

**Danny Ryan** (39:49) - Okay. Do others?

**Potuz** (39:57) - I mean it's fine it's like their the same release for Goerli and mainnet or the same release for Sepolia and Goerli. And I believe that the second option is better for us. But I'm not sure if everyone agrees.

**Danny Ryan** (40:12) - Right so being able to do two instead of three. I given the testing that we want to achieve between now and Sepolia, I am a bit more comfortable and saying let's pick Goerli and mainnet simultaneously rather than picking Sepolia with picking Goerli with Sepolia today, but if others feel strongly about trying to pick a tentative Goerli today, I'm okay with that. Any sentiment on picking Goerli as well today?

**Dustin Brody** (41:05) - I think would be useful to see how Sepolia goes first. And I don't think there's much to gain from picking Goerli today.


## 4844
## Block/blob decoupling (simulation results)


**Danny Ryan** (41:18) - Okay, yeah, I would like to move forward to Sepolia with the builder testing in parallel, and when we get near the end of the month, have the conversation around. Or I guess at the start of the month called the second of March. Have the conversation around Goerli and mainnet simultaneously. Okay moving on to 4844. I think the biggest item on the consensus layer is the block/blob decoupling. There is an open PR which I've done some review on Jacek wrote and I will open back up today. Hopefully, there's another chance to look at it. A lot of minor refinement rather than anything major and should be able to get this done out very soon. Any discussion around that PR any particular items that we want to surface here rather than in the PR itself? Okay. That's just no no big surprises in that PR if you've been part of the design discussions up to this point. We do have some simulation results. Anton has been looking into what coupling versus decoupling does in a simulated environment for gossip. So, Anton, can you maybe share your screen and show us some of these results? 

**Anton Nashatyrev** (43:00) - Yeah, just a second. Yeah, so yeah, this is basically decoupling looks pretty good. So here is like dissemination, delayed distribution for do you see my screen?

**Danny Ryan** (43:26) - Yes. Yes. And are we looking at full time propagation or average?

**Anton Nashatyrev** (43:32) - Yes, this is full time propagation. So I mean, like, on the vertical axis, there is like the number of nodes which received the message or decouple or all of the couple message and they're like in the time slots on the horizontal axis like so. So, yeah, you can see that the like, for the couple this is, this is fully decoupled messages, which means like, a block, block, 128 kilobytes and four blobs, they're all five are disseminated on their, on their own subnets. So, here is like a network of 1000 peers. Ever everyone has 100 megabit per seconds per second. And like this is like distribution of, of the message delay. So decoupled looks pretty, pretty cool. They're all most of them disseminated within a second and to and to decouple and coupled this kind of, like two and a half seconds. So yeah, there are like more, more simulations with networks where like 10 10% of peers have 10 megabit per seconds. Others have higher throughput, bandwidth. So the picture is almost the same here. Right. On the right side, there. layer there are some peers that receive receive a message within four seconds, but these are the peers which have this low bandwidth. So they are peers with low bandwidth basically don't influence on the delivery time for for high bandwidth peers. Yeah, and these are, I would like to match these up for for the gossip (inaudible) with with floods with with flood publish option of here is a seven hour graph, which compares how flood publish affects like the initial initial initial message propagation. So yeah, so off when flood publishes off, the messages will disseminate much faster. Yeah, because of because of if publisher have good a good outbound channel, like or maybe gigabit or even 10 gigabits, it shouldn't affect their results. So yeah, that's it. 

**Danny Ryan** (47:31) - So we're seeing worse we're seeing worse on average on flood publish being on whereas that's the default, correct? 

**Anton Nashatyrev** (47:38) - Yeah. 

**Danny Ryan** (47:39) - Okay.

**Mikhail Kalinin** (47:43) - Could you please repeat the size of the blobs or the number of blobs?

**Anton Nashatyrev** (47:52) - Sorry, question for me?

**Mikhail Kalinin** (47:55) - Yes. 

**Danny Ryan** (47:57) - I think it's 128 kilobyte block, and then four 128 kilobyte blobs and the coupled is that all being one payload versus decoupled, that being five different payloads on five different (inaudible).

**Anton Nashatyrev** (48:09) - Yeah, right.

**Mikhail Kalinin** (48:13) - Have you also tried to refer to disable flood publish for blobs only and keep it enabled for blocks?

**Anton Nashatyrev** (48:26) - Actually, at the moment, the way the flood publish option is like, global parallel topics. Yeah. Actually, it makes sense to probably discuss this option to be to be topic specific. So yeah, it makes a may make sense.

**Danny Ryan** (48:52) - So right now, the simulation results are showing better average and worst case propagation times on the order of, you know, 40 or 50% time reduction and are also showing that our current flood publish strategy might need to be revisited.

**Anton Nashatyrev** (49:14) - Yeah.

**Danny Ryan** (49:15) - Correct? 

**Anton Nashatyrev** (49:16) - Yeah.

**Pawan Dhananjay** (49:19) - Also the the repub like on the gossip sub layer in the simulation to be republish as soon as we receive receive the message or to be like have some delay for the processing time for the individual blobs and blocks?

**Anton Nashatyrev** (49:34) - Yes, I had, like 10 milliseconds for validation, but it doesn't affect too much.

**Danny Ryan** (49:52) - Okay, so at least these simulation results are very promising, very significantly, very promising to continue forward with the decoupling spec and implementation. I think Pop also has simulation framework he's been working with. So when we do get some decoupled and limitations, we can also validate some of the results in that environment as well. Any other questions for Anton or comments on these results? Great, thank you, Anton. This is very valuable to have at this point. I really appreciate it. Okay, looking at our agenda, anything else in 4844 for discussion today?

**George Kadianakis** (51:00) - So, on the cryptography side of this, free the blob PR, we have implemented the verification strategy that would work with the free the blobs approach such that even the blobs that travel decoupled can get validated if we want. We implemented it in KZG and got some initial benchmarks. The verification is slightly slower than slightly slower than the old approach with the aggregated proof which was created for that specific purpose. But it's not horrific, like like it's not that bad. I think, given the fact that that the capital strategy allows us to get the blobs faster. And we're talking about network latency which is usually much more than cryptographic latency. I think the the delay and verification can be easily excused. But this is like an initial investigation and we will do more as the days go by. But, like, I don't think it's it's reasonable to dump a bunch of numbers on this call right now. But if people are interested in discussing verification times and what we think is too much or what we think is good get in touch or asking the KZG channel.

**Danny Ryan** (52:47) - Thank you, George. Yeah, and with the if we run into a wall there the fallback alternative being to send just the aggregate and doing the verification crypto verification at the end. So I think either way, we're probably going to land in a reasonable spot. Okay, any questions for George? Great. Lightclient what PR is this?

**Barnabas Busa** (53:25) - This is changing the daily transaction sig hash back to hash triggered.

**Marius Van Der Wijden** (53:35) - Yeah, any objections to moving this in and getting this into our specifications for the next devnet?

**Etan (Nimbus)** (53:46) - It doesn't work for for the unsigned hash because that can be collisions with other transaction types. Like the transaction message, it doesn't encode any anywhere that it is a blob TX type. So if there is another transaction type, that (inaudible) additional field that can have a zero value to it will have the same hash.

**Lightclient** (54:17) - But it's a Merkel root so you don't have malleability of the message of the preimage.

**Etan (Nimbus)** (54:24) - Merkel roots have this problem. But we can discuss in the PR. There is compute signing root for CL as well.

**Danny Ryan** (54:40) - Okay, Anton if you can jump in there, so that we can have that discussion. I appreciate it. Thank you.

**Danny Ryan** (54:52) - Anything else on 4844?

**Sean Anderson** (54:57) - Yeah, I open an issue on the beacon API's repo about the API's for signing blobs. So generally just looking for feedback there if anyone's interested. I just linked in the chat. 

## Research, spec, etc
## Warning about merge of [Updated eip4844 references to deneb consensus-spec#3215](https://github.com/ethereum/consensus-specs/pull/3215)

**Danny Ryan** (55:12) - Right. And so specifically, this is the validator namespace on the beacon API to allow for the decoupling correct? Right. Okay, great. Thank you for keeping up moving. Anything else on 4844? Great. Hsiao-Wei, you have a consensus layer spec warning.

**Hsiao-Wei Wang** (55:47) - Yes. So thanks to Paul Harris. (inaudible) that we had a PR about we the renaming of the old 4844 fork, and then the new name will be Deneb, and there might be other featuring with them (inaudible) updates and so this PR here thanks Danny posted this PR will once this PR is merged it definitely will break. Like we have the other like ten open 4844 PRs. So I think by (inaudible) AKA me I will try to meddle in the PR to maybe that's (inaudible) because I think the I think two big rename. I mean, the folder rename it's easier to use (inaudible) then add more commits, append to PRs. So by default, I will try to meddling and and the process might be slow and just oh, if you want to update your PRs as soon as possible, you can do it by yourself or just ping me and I will try to prioritise it. That's the warning here.

**Danny Ryan** (57:26) - And sorry if you said this, when, when is this going in?

**Hsiao-Wei Wang** (57:32) - I think as soon as possible. We can do it today.

**Danny Ryan** (57:37) - Okay, so this is going to be in the next release. That's the warning. 

**Hsiao-Wei Wang** (57:41) - Yes. 

**Danny Ryan** (57:41) - So likely there'll be a release when we get the decoupled stuff merged, and this will certainly be associated with it?

**Hsiao-Wei Wang** (57:51) - Yup.


## Open Discussion/Closing Remark
## [CL EIP and editors](https://github.com/ethereum/pm/issues/711#issuecomment-1423020244)


**Danny Ryan** (57:56) - Any questions? Okay, Tim has a comment about consensus layer EIPs and editors. 

**Tim Beiko** (58:17) - Yes, okay. So we we discussed this a little bit at the Interop in Austria. So, to give some background, the idea that like right now, the EL and CL have very different specs, processes, you know, the CL obviously has the Python spec. The EL used to use sort of EIPs in the yellow paper. We've made a bunch of progress on the technical side on the EL to sort of align with with the CL does we now have Python spec that is basically at the mainnet. And that said, you know, we think the EIPs are still valuable as a way to describe sort of in plain English why a change is being done and sort of the high level kind of design decisions. And it would be nice to start having those on the CL side as well. So let's say, you know, there is a change. Like I mean, the EIP 4844 is actually an example we're we've done this right but there is an EIP that describes sort of the rationale why we have blobs, you know, some of the risks. And then the specs are all kind of in the Python spec. But moving to something like that would be quite nice so that you know users and people submitting the EIPS just have a single process to use if they want to make a change to Ethereum. That said, there's been some reluctance from the CL side to sort of move to the EIP process because it's perceived to have a lot of friction. And I think that's a fair concern. So we've been trying to figure out like, what's a good way that we could, you know, softly onboard CL folks into the EIP process, not sort of have them burdened with all of the, I guess, overhead of the process as little as possible. And so, we had a meeting with EIP editors yesterday, and one thing we'd ended on was the idea of having this designated CL folks join as EIP editors, which would give them kind of two things. One is obviously like the ability to just review and approve EIPs for CL folks so that I think one of the the reasons why EIPs are slow is there's just not a lot of editors and so you know, you sort of have to wait in the queue to get reviewed. So having somebody on the CL side who just like focuses on that can help speed the process up. And then the other thing that they could do is, which hopefully you don't have to do too often is basically override like whatever technical checks the bot does on the EIP side. So that, you know, we could be in a spot where CL EIPs sort of get merged even though they don't pass all the say like spec compliance checks that happen automatically in the EIP repo so this would be a way where like, you know, someone from the CL side can actually force merge this stuff. And then obviously, if and when that happens, we can sort of reflect on like, what was the thing that sort of caused the friction and can we adapt the process that to like, minimise that friction in the future? So the ask is, you know, if anyone on the CL side is interested in sort of take that on, and again, the scope would be just like narrowed to like, basically core EIPs and even just like CL, EIPs, as you don't have to care about ERCs or you know, anything else, but it's really a way to like enable your colleagues on the CL to like, write easy EIPs and get them merged in quickly so that we can hopefully move towards something that's that's a bit more unified. Yep. Any takers?

**Danny Ryan** (1:01:56) - If you're interested, reach out directly to Tim.

**Tim Beiko** (1:02:02) - Yeah. 

**Marius Van Der Wijden** (1:02:03) - What's the status of the ERC out of EIPs?

**Tim Beiko** (1:02:11) - So that's the yeah, still contentious. I think. Yeah. So the other the other proposal that we had was to basically split out EIPs and ERCs altogether from the repo. There is some technical overhead to do that. So like I think, you know, the EIPs editors don't want to just do it for the sake of doing it which I can sympathise with. I still think we should do it, you know, and like, especially as we have more CL folks join, like, clearly the processes will diverge. But I do think, you know, it's easier to first bring somebody from the CL have them like, start playing around with the process and I think that'll make it clear if and how we want the processes to diverge. Yeah, and also, yeah, just make sure that like once we do fork the repo, like, like, if we're doing it's like, we're very sure about it, and we're not just incurring all of this technical debt and maintenance on both sides. There is a thread on ETH Magicians about forking the repos that I'll post it in the chat here if people want to engage there.


## [Engine API: deprecate exchangeTransitionConfiguration execution-apis#375](https://github.com/ethereum/execution-apis/pull/375)


**Danny Ryan** (1:03:28) - Any other questions for Tim? Okay, and Tim did threaten if we don't get any editors to work on this or people to write the CL EIPs, then he's just gonna dump our GitHub conversations onto the EIPs which, maybe it will work. Okay, and then and oh, Mikhail, I skipped this when we were in the Capella, I apologise. It's an API deprecation PR that Mikhail wants to propose. Mikhail? 

**Mikhail Kalinin** (1:04:12) - Yeah, no worries thanks Danny. So this PR yeah, the topic is deprecated and exchange transition configuration which I believe every everyone is open to do this. Because, yeah, this this method call actually useless after the merge. And yeah, there are alternatives for. For instance, for node operators, they can use ETH chain ID or any other ETH method expose exposed in their engine API endpoints to test that this endpoint is alive. CL clients doesn't need any kind of ping functionality because they are constantly calling (inaudible) updated and a new payload and first. So yeah, I believe that we should deprecate this method and just remove it from from this from clients. So and I see two potential ways to do this. First one is simple and straightforward. So we just use the any, we just use a hard fork as a coordination point. And we just remove this method support from both sides. The downside of this approach is that if someone just you know publish a release of their clients without support this method, but the counterparty client that they saw the operator is running, does not support yet does not yet support the removal. So they will be warning messages in the logs of one of the clients for some period of time unless the other part is and until the other part is upgraded, as well. Yeah, so that's the only downside, but it's simple and so it doesn't require any additional interactions. The other ways to just say that okay, so CL clients will still call this method but if this method does not exist, it will not file any error messages and the EL clients on the other side will not log any error messages if this method is not called at all. This this would be the first iteration and we will use the in this approach will use the hard fork as a coordination point to introduce this first step. And then the second step was just that would not require any coordination and client developers Yeah, grant teams will be able to remove the support of this method whenever they want. So this this actual PR, proposes the second approach, but I don't feel that it is probably a big issue with going with the first approach. I just want to open this question up for client developers. What do they think about the potential approach to deprecate it? And the other question is whether there is a capacity to do this. I know that we don't want to make any last changes if they are not related to security upgrades or other other significant things, but this one is kind of like a side of like, the main bulk processing stuff aside of main client functionality, so this is probably okay to to make attempt to Shapella. So yep. What do people think about it?

**Danny Ryan** (1:07:53) - I mean we're at the point where we're intending to have releases in eight or nine days for Sepolia. So this is probably on the simpler side of things, but I and I'm not willing unless people are very, very pro to kind of force this down at this point. Are there outspoken people for this change? Anyone very against?

**Dustin Brody** (1:08:40) - I'm in general for either option, either the options but to happen, rather, rather sooner than later. I feel they're quite low risk, and this has been useless for a long time.

**Danny Ryan** (1:09:02) - Thank you. Any other comments here? Yeah, I mean, given the closeness, this is a very tough one to make a call on without comment. I think by default, we shouldn't be adding changes unless there's very strong consensus to do so. So I'm going to default silence to not doing this for the fork. I know, Dustin, thank you for your comment. But otherwise, if there are not comments, I think we should default to no. 

**Mikhail Kalinin** (1:09:49) - Yeah, I agree with that. So it is okay to wait for another fork, so should not be a big problem. 

**Danny Ryan** (1:10:02) - Okay, please do take a look at, oh, I did not see that Marius and Sean had spoken up. So there are people that people are pro not necessarily Shanghai, Sean might look at team capacity, Potuz can look at team capacity. So I guess if Monday, Tuesday, all the teams on this PR say let's go, you know and that needs then then we can, but I think by default unless we do rally a bit of support the next by early next week, then we should not do this. Cool, but Mikhail, if you want to keep it moving, you can knock on.

**Mikhail Kalinin** (1:10:52) - Yeah, of course.

**Danny Ryan** (1:10:55) - Okay, Marius says not do it. Default not do it, unless a bunch of supporters rally. Alright.

**Mikhail Kalinin** (1:11:07) - So not do it like meaning in this hard fork right?

**Danny Ryan** (1:11:12) - Correct. 

**Mikhail Kalinin** (1:11:13) - Okay, so then let's just responding to the next one. Thank you.


## [SSZ Transactions Breakout Room #721](https://github.com/ethereum/pm/issues/721)


**Danny Ryan** (1:11:25) - Okay, last, SSZ transaction breakout room.

**Tim Beiko** (1:11:33) - Yes, so there's been a lot of conversations about how the ELs go about SSZing the transaction types. And then it came up yesterday again on 4844 on the 4844 call. It's becoming I think having a path forward on that is becoming not quite a blocker yet, but like will soon be a blocker and like, EL work on 4844 so. We set up a breakout room next week, Wednesday 15 UTC to discuss this in more detail. Obviously this is mostly an EL thing but since EL folks have strong opinions about transaction and coding as well. So if you if you care about this, this is a time to show up. And then hopefully we agree on the path forward but yeah, we'll see how that goes.

**Danny Ryan** (1:12:31) - Okay, thank you. Any other comments? Or discussion points for today? Great, thank you. I'm excited to keep Shapella moving and exciting on decoupling. Talk to y'all soon. Take care. Thank you.


-----------------------------

### Attendees

* Potuz
* Danny Ryan
* Oleg Jakushkin
* Marius Van Der Wijden
* Etan (Nimbus)
* Barnabas Busa
* Radek
* Caspar Schwarz-Schilling
* Dustin Brody
* Tim Beiko
* Stokes
* Terence
* Justin Florentine
* Guillaume
* Sean
* Ryan C
* Fredrik
* George Kadianakis
* Mikhail Kalinin
* Dankrad Feist
* Sammy
* Pooja Ranjan
* Anton Nashatyrev
* Ben Edgington
* Ruben
* Enrico Del Fante (tbenr)
* Pari
* Hsiao-Wei Wang
* Lightclient
* Stefan Bratanov
* Pop
* Fabio Di Fabio
* Daniel Lehrner
* Andrew Ashikhmin
* Mehdi Aouadi
* Gajinder
* 0x
* La Donna Higgins
* Phil Ngo
* Zachary
* Ansgar Dietrichs
* Mike Kim
* Łukasz Rozmej
* Andy Martinez
* Mario Vega
* Trent
* Dan Lee
* Marek Moraczyński
* Kasey Kirkham
* James He
* Carlbeek
* Nazar Hussain
* Damian
* Pawan Dhananjay
* Saulius Grigaitis 
* Rory Arredondo

-------------------------------------

## Next Meeting
February 23, 2023, 14:00 UTC
