# Ethereum Core Devs Meeting #151
### Meeting Date/Time: November 10, 2022, 14:00 UTC
### Meeting Duration: 1 hour 40 mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/675)
### [Video of the meeting](https://youtu.be/y8jZ11_CQGo)
### Moderator: Tim Beiko
### Notes: Rory Arredondo

-------------------------------------------

## Action Items and Decision notes from [Tim Beiko](https://discord.com/channels/595666850260713488/745077610685661265/1050440218739753141)

1. We agreed to the scope for Shanghai: we will move forward with all previously included EIPs (Withdrawals, PUSH0, Warm COINBASE, Limit/Meter initcode) as well as the 5 EOF EIPs (3540, 3670, 4200, 4750, 5450), as long as they do not delay withdrawals significantly

2. To ensure this re: EOF, we'll have two "gates" early next year: EL client implementations completed & tested by ACD on Jan 5, and EL cross-client interop by ACD on Jan 19. If we miss either of these, we agreed to remove EOF from Shanghai and ship only the 4 other EIPs to ensure withdrawals are not delayed. 

3. We agreed that EIP-4844 should be included in the fork after Shanghai, to reflect how the CL specs are right now. There isn't really a way to do this on the EL side, so for now I'll create cancun.md and list EIP-4844 as Included. Open to better options if people have suggestions! 

4. @MariusVanDerWijden will be putting together an EIP for time-based EL forking 🔜, geth already has an implementation

5. We agreed to include these two Engine API changes in Shanghai, unless we see them cause unexpected delays for teams: https://github.com/ethereum/execution-apis/pull/314 & https://github.com/ethereum/execution-apis/pull/218 

6. Alongside EIP-4844, there may be other things we want to make a decision on quickly for the next upgrade. In the first few calls next year, we'll discuss those. Client teams should try and review what's posted on the agenda before then and highlight anything they feel particularly strongly about!



## Intro
## [KZG Ceremony update](https://github.com/ethereum/kzg-ceremony/blob/main/FAQ.md)

**Trent van Epps** (5:19) - Yes, I will keep it brief. Thanks for the time. So some people might be aware but for those that aren't Ethereum is running a trusted setup, also called the Summoning Ceremony or Parameter Generation event, but we're running this to enable 4844 and danksharding in the future. If you're curious about what this is or want to learn more about how to participate, there's a channel in the Ethereum R&D Discord called KZG ceremony so you can go there, ask questions. There's some probably some links in there as well that will fill you in more but if you're interested in participating, go there or just reach out to myself or Carl, and we can point in the right direction. Additionally, if you're interested in writing your own implementation, we'd love to support you in that either technically or I will be running it branch around a little bit later. But yeah, just so anybody who isn't aware we are going to be doing this in the next probably starting in the next month, early next year, likely. So reach out if you're interested and we'll we'll give you the information to help you find your way. Alright, that's it. 

## [Engine API spec improvement proposal](https://github.com/ethereum/execution-apis/issues/321)

**Tim Beiko** (6:28) - Thank you, Trent. And is there a link? Yes, there is a link on the (inaudible) there for people to learn more. Okay, next up, Mikhail you had you had three Engine API things but there was one that we really wanted to get to from November so literally a month ago, the Engine API spec improvement issues. 321. You want to take a couple of minutes to chat about that.

**Mikhail Kalinin** (7:00) - Thanks, Tim. Let me just give a quick overview over this proposal. And its status also. Okay, so there are two parts. First of all, do people hear me well? Just two parts in this proposal. First one is to make the spec itself more neat for spec writers and for engineers. The proposal is to just break down this specification MD into several files. And the debates are about how to do this. What's the best way? What's the best approach? First, first approach is to break down them by features or forks. So each file will contain all methods that are used, newly introduced by some hard fork or modified by the hard fork. Then after hard fork work on scope is finalized, all those methods are finalized and we move to the next documents. I'm starting to add an editing spec there as first so we'll have like, every fork will likely introduce Engine API changes will have a separate document. The other way is do this by functional breakdown. So meaning that all matters like interacting with payloads will be in one file, fork choice stuff will be in the other one. Both has pros and cons. So if you're interested in it, read more in the comments in the in the issue. The other part of this proposal is about (inaudible) method whether we need it or not. This method this basically for CL clients to know which methods are supported by EL client and allows for introducing new methods outside of hard forks without any coordination of deployment and development and deprecate old methods. And here we would like to, to listen to hear from CL client developers. First whether they need those these methods and if they do need it and they find it useful. Then we'll back on ACD call back, EL client, EL client devs to implement it basically about like breaking down this spec. I think we want to do this as soon as possible because Shanghai work is in progress. And the faster we do this, the better so it probably it will happen next week to anyone who is interested, go to this issue. Leave your comments, ask me in Discord. So whatever. Thanks. 

## Withdrawals devnet/testing updates and [Shanghai Planning](https://github.com/ethereum/pm/issues/450#issuecomment-1242103736)

**Tim Beiko** (9:57) - Thank you. Any quick questions are comments? Okay. And then, okay, and then the last thing I want to make sure we cover because last call we ran out of time before discussing it, is the current status of the withdrawal work. So I know there was a devnet stood up. So, Marius, do you want to give us a quick update of just where devnets are out with withdrawals and can go from there?

**Marius Van Der Wijden** (10:33) - Maybe Barnabas?

**Barnabas Busa** (10:35) - Should I yeah, I think I can give a very quick overview of how we are looking right now. Yep. So currently we have two private devnets on the private I mean, we don't expect anyone from the public to participate in it. We have a premerge devnet, which is the premerge (inaudible). There we have Prysm Geth, Psysm Nethermind, Lighthouse Geth, Lighthouse Nethermind, Teku Geth and Teku Nethermind. (inaudible) during this devnet but I don't see the point for doing and we have here (inaudible) works. But we would like to focus on the post merge chain because we don't want to deal with the merge stuff thing anymore. In the long term, we would like to run only one devnet for boosters, and for that we would launch it with a postmerge Genesis. Currently we have Lodestar (inaudible) and Bezu and Lighthouse with Geth and Teku with Geth testing there. What we have tested so far, basically full withdrawal, working on both chains, partial withdrawal is working on both chains because the execution just change is distributed. And currently we only have a single tool to do this BLS execution conversion (inaudible). It would be nice to have another tool at least that could do this and where people could verify their signatures. Maybe we can have an update from someone that certainly is taking deposits CLI whether this is a feature that they're planning to implement or not. What we haven't tested so far is a mass withdrawals where we just have a big queue and merging with a large number of exits, or every submit from that data or just some source information. Maybe the (inaudible) can come up with particular tests and test them and just make some documentation so whether you can also test this. So we would like to start a public devnet hopefully on the 15th or 16th of December, so that a one week from now. For that we would like to run all clients on that but I know that probably not gonna be possible. What we need for getting working is Prysm going to work at the post merge Genesis because they only going to have a single chain which is serving the post merge Genesis (inaudible). Bezu has to work with the Shanghai time but we would need to have an update from them. Nimbus would have to have something working and Erigon would have to have something working. But I think Bezu (inaudible) within Erigon are non blockers and the only more blocker would be Prysm. I would be happy to test that Prysm but I know that 80% of the public is still running Prysm node and for them it would be very useful if they could also participate in the public testnet. Alternative route is to just let them work on their chain or their implementation and let them drain later stage. So that's about it. It would be great to hear from CL devs how are they? What are their status right now? Sure, yeah.

**Kasey Kirkham** (14:33) - I can say that we we've been working on start putting from a Bellatrix block and we actually have an end to end test passing with that as of this morning. So we used to look more clean up and and look at the results will be more but it's it's basically you know, next couple days we'll have that available. 

**Danny Ryan** (14:57) - Who's we in? In terms of Team. 

**Kasey Kirkham** (14:59) - Sorry Prysm. 

**Danny Ryan** (15:01) - Thanks. 

**Sean Anderson** (15:06) - Sweet. So for Lighthouse, we are able to start with the post merge Genesis. We've actually just recently started testing them with like 4844. I haven't been working with withdrawals, but it should work the same for withdrawals. And generally for withdrawals, I know we're working on cleaning stuff up to get the merge time stable in the near term. So that's our status.

**Danny Ryan** (15:38) - Any other kinds of question about the CLI? My understanding is that that the CLI will be able to do the BLS changes, key changes. And I know Xiao Wei was working on that but it was a little sidetrack this week, so I think that's a soon item.

**Marius Van Der Wijden** (16:02) - Mario, can you quickly tell us about Hive? 

**Mario Vega** (16:05) - Yeah, of course. So basically on Hive, at the moment we only have one suite for withdrawals, which is the execution client part only. Basically, this is just the feel marker, doing interaction with execution client and testing all the Engine API endpoints on the execution client. I have a list of test cases that we have added there can also the entire well the source of this of these tests. And even we still have to start the interrupt suite for Hive which is the EL plus CL clients testing suite. That's still to start, but if anyone has any comments or wants to see the current status of the EL test cases, you can just take a look at this page. And just let me know in the comments.

**Marius Van Der Wijden** (17:10) - So new EL teams that want to be part of this just like message either Mario or me. So we can add you to Hive.

**Mario Vega** (17:20) - Yeah, at the moment I've been testing on Geth and Nethermind and I will be starting testing Erigon, which I think has just completed the Docker image. So Yeah.

**Tim Beiko** (17:38) - Sweet. anything else? I guess any other clients want to share updates on where they're at with withdrawals or testing?

**Ben Edgington** (17:45) - Yeah, Teku is co-complete we believe and feature complete so seems to be going well on the on the test net. So we're good to go ahead.

**Ziogaschr** (18:00) - As I said the last week, (inaudible), I'm from the ADC team. We try to port everything on Erigon client. Erigon is at the same state I think as you go with you as we port in the same PR. Gundry only a 54 Sorry. Yeah, 5450 is missing and it's able to sync with (inaudible). So the state is pretty similar to go through meeting.

**Tim Beiko** (18:42) - And this is for withdrawals as well or?

**Ziogaschr** (18:44) - And yeah, they have worked the Erigon team has worked on another PR with withdrawals and I think it's there already, but I cannot tell that because I haven't checked on it.

**Andrew Ashikhmin** (18:57) - Yea we're still working on withdrawals. I don't think it's complete yet. Sorry, the other the other PR it's probably referring to EOF.

**Tim Beiko** (19:13) - Right okay yea that's what I thought. Yeah.

**Marius Van Der Wijden** (19:20) - The way Andrew I found a really, really tiny issue in Geth so if you're if you're porting Geth withdrawal implementation to Erigon, then make sure to also include this. I can send you a link with.

**Andrew Ashikhmin** (19:38) - Oh yes please.

**Marek Moraczyński** (19:43) - Okay, so on our site, we are working fine on devnet and we are reviewing cases because a few of them are failing. However, for us, it would be helpful if we discussed getpayloadv2 with blocked value. I know that. Mikhail added it to agenda.

**Tim Beiko** (20:05) - Okay, so blocked okay. Yeah, let's come back to that at the end. Yeah, I'm making a note so I don't forget.

**Jiri Peinlich** (20:17) - From Besu perspective, I think the only thing I don't understand right now is what exactly we're doing with the timestamp and how we do to fork IDs, but I think that's on the agenda later. So. 

**Tim Beiko** (20:31) - Yeah, so there's not there's not an EIP for it yet. Okay, so yeah, let's make sure to cover those two things. Yeah, so the timestamp and the block value.

**Jiri Peinlich** (20:45) - Otherwise currently we are, I think, failing around 11 of the Hive tests locally. So there's obviously 

**Tim Beiko** (20:53) - Got it. Thank you. Any other client teams?

**Phil Ngo** (21:04) - Lodestar is able to start from a post merge state as well and we are pretty much good for withdrawals at this point. We've been on the Shandong testnet. So everything's good from Lodestar end.

**Tim Beiko** (21:15) - Anyone else I think that's pretty much all the teams. Okay, so

**Danny Ryan** (21:33) - Call out if you run into a withdrawals issue, and the test did not catch it. Reach out tomorrow, get it in the doc. That's all.

**Tim Beiko** (21:47) - Thanks. And Mario shared the doc above. Okay, and yeah, so the two things I think it makes sense to come back to is like this timestamp issue and then getpayloadv2. I think that. So the most important thing to get right on this call is how do we approach Shanghai kind of broadly, so that teams can have like a clear scope for what to work on. Like I said at the beginning, this is going to be the last call this year. And so you know, if we can agree on on what the scope of Shanghai should be, I think this gives us effectively an extra month where we can work with like a finalized set of EIPs and move forward with that. And so there's there's a lot of value in making that decision earlier rather than later. There were a couple of comments on the agenda about this like, high level which approach we should take, how the different pieces fit together. I think that probably the starting point is like everyone seems to agree on is we want withdrawals to happen relatively quickly, on Mainnet this is clearly the highest priority for everybody. Teams are working on it. And you know, both on the last All Core Devs and the CL call last week. That seems pretty clear. You know, people seem to generally want to target around March ish for for this to happen on Mainnet. And I think from there, you know, the question is, assuming that's that's what we want to do, and target kind of withdrawals around March or so. What what should we be coupling around around that upgrade? Are there things that we think are high value that make sense to send alongside withdrawals and would not kind of alter that timeline significantly? And I think, after that, you know, we can have a conversation about what do we do with everything else that you know, doesn't, doesn't kind of make that cut? Because clearly there's also a bunch of other important things that we've been discussing for like the past two, three months now on these calls. That it probably makes sense to like align on priorities. But yeah, I think that the most important bit is definitely figuring out, you know, given we want withdrawals to go quickly. There's a bunch of other proposals that can come alongside it. What are the most important ones to include that won't kind of incurred delays or lead us to incur delays when shipping withdrawals? So yeah, I guess I'd be curious to hear from just like the EL teams first like how they generally feel about that, if their opinions kind of evolved in the past few weeks on this, but yeah, assuming we want to target the relatively quick withdrawal fork, and we already have a couple of other tiny EIPs you know, like, I won't go through all of them but the warm Coinbase push zero and whatnot, are other things that that client, client teams feel we should include. And yeah, there's some comments in the chat, you know, around what does it mean to be relatively quick? I think people people said around March or so. And with that he was saying in the chat is that there's now 100 comments in the chat said is that if we want to hit Mainnet around March, we'd have to do this by then like January we were doing Mainnet shadow forks for this. So like, where, you know, the code is probably not quite ready to push the testnets, but you know, we're pretty, pretty happy with it. We think that it's feature complete, we want to see it, you know, run against mainnet environment, see what's breaks, fix some final bugs and move the test that's shortly after. Okay, so I'll pause here. I'm curious to hear just from the client teams on the on the EL side specifically like of the different EIPs that are being considered have been CFI'd. Are the things you think it makes sense to include alongside withdrawals, and that won't affect this timeline too much?

**Péter Szilágyi** (25:57) - I would like to have 4844.

**Tim Beiko** (26:06) - Alongside withdrawals and shipping in March?

**Péter Szilágyi** (26:11) - No, probably shipping that later but wasn't that the idea always that we have 4844 the delays only maybe a couple of months. 

**Tim Beiko** (26:22) - So my feeling from the last like All Core Devs and CL call last week was client teams would rather have would rather have withdrawals ship really soon around March or so. But yeah, I don't know. How do other client teams feel about this? So yeah, maybe Danny and then Peter, again, 

**Danny Ryan** (26:49) - The the consensus layer call, definitely from those teams, there's a feeling that 4844 is just not in the same state of readiness as withdrawals and thus coupling would be a significant delay and at least on those sides of the teams. Currently, there's no desire to couple.

**Péter Szilágyi** (27:11) - Okay, but we are aware that if we don't couple them then 4844 will probably arrive earliest autumn?

**Danny Ryan** (27:21) - I think that can probably be debated? But I you know, I think that that's not unrealistic.

**Péter Szilágyi** (27:30) - Just looking at all the past hard forks we did, I don't see a way of shifting hard fork past. Our track record shows that we are incapable of shipping hard forks faster than (inaudible)

**Tim Beiko** (27:44) - Berlin and London was four months but I think yeah, like it's

**Péter Szilágyi** (27:53) - Almost March, then July add a couple of delays. That's autumn.

**Tim Beiko** (28:02) - Yeah, like I think obviously, if you do decouple them, yes, it will ship later. And then the question is, you know, how much delay would teams feel comfortable having I think, yeah, on the CL side. Last week, it felt pretty clear that coupling them would have like significant delay for withdrawals. And that wasn't something that teams wanted. But I don't know. Like, around. Yeah, I'm curious from other folks on the EL side like.

**Péter Szilágyi** (28:40) - Well, can I guess my challenge is that withdrawals, brings absolutely nothing to make Ethereum better. Yeah, sure, we need to do it. It's something that it's kind of like finishes the merge. Agreed. But yeah, it's just Ethereum remains exactly the same thing whether whether withdraws work or not, whereas with 4844 you actually have the capacity to make it better and I know for me personally, I kind of feel that scaling Ethereum is significantly more important than withdrawals and scaling, the whole thing just delays withdrawals a bit.

**Tim Beiko** (29:31) - Dankrad and then Proto.

**Dankrad Feist** (29:34) - Yeah, I mean, first question is what does significant mean? Is it one or two months or more, because that's like a pretty big question. And the second of course, is like, are client teams the right people to decide whether whether that trade off is worth it?

**Tim Beiko** (30:01) - Yeah, I think significant. I don't know, what I perceive is like, one month or two, I think with regards to like the client teams. It's like aligning what they can implement relatively, in a relatively aligned way. But yeah, there's a bunch of other hands up so Proto?

**Danny Ryan** (30:25) - Can you get closer to the mic?

**Protolambda** (30:31) - Better?

**Péter Szilágyi** (30:32) - Yes. 

**Protolambda** (30:34) - Okay. So 4844 we have many layer twos that are very motivated to ship 4844. At the same time, I also believe, withdrawals are also a priority. And so I'm asking what does a timeline look like where we do withdrawals first and then 4844 as soon as possible afterwards? If we aim for like a May, June, kind of targets, like how do we have to plan these public testnets? Is it possible to try and paralyze work now to to make 4844 happen after withdrawals without delaying withdrawals that still in the first timeline?

**Tim Beiko** (31:24) - I think that's like a really good question. I'm I'd be curious to hear maybe from some of the client teams on that, where like, yeah, if we, if we, if we separate them from like a code perspective, how quickly do we think we can we can get them out? Don't know on that. So there's a bunch. There's a bunch of CL folks. Lodestar, Prysm, Teku, in the chat saying that, you know, it can be parallelizable quite easily for teams so that you know, we can ship withdrawals first and still keep the work on 4844 so that happens quite quite quickly after I don't know on the EL side. How the folks feel about that? 

**Péter Szilágyi** (32:19) - Our experience is that people absolutely do not touch an EIP as long as there's a hard fork scheduled before it. So, at least in Ethereum (inaudible), most people most dev teams only touch an EIP once there was actually somebody already implemented it. And if there's a hardfork scheduled, which does not contain a EIP, then most people will just not care about the EIP because it's just the future thing. Currently now that's an interesting question, but historically, it didn't happen. 

**Tim Beiko** (33:01) - Yeah, I think I think I agree with that. And I think the question is, then can we schedule two forks, right, like, could we do something like, you know, we scheduled this withdrawal fork we finalize the scope, and then you know, we already have 4844 as kind of the main things scheduled for the next fork does that is possible basically? Dapplion?

**Lion Dapplion** (33:31) - Yeah, I wanted to comment on Consensus sides. We are pretty close to done on both forks. And there are no unknown unknowns for 4844. So I think testing would have would give us plenty of time to iron out the bugs. So I don't really from our side, I don't see the need to give us a multi month period to keep implementing. 

**Tim Beiko** (33:55) - Andrew?

**Andrew Ashikhmin** (33:58) - Well, I think that withdrawals take priority and that's let's like, that's really important to deliver. And I've changed my position on EOF because I think there was some statement from solidity they're very much in favor of EOF so, I would either pick 4844 or EOF to deliver in Shanghai, but not both like they're delivering withdrawals. 4844 and EOF in Shanghai it's it's doomed to failure. It's too much. So basically, withdrawals plus either EOF or 4844.

**Tim Beiko** (34:39) - Got it. Danny?

**Danny Ryan** (34:43) - I read this in the chat, but my opinion would be to in terms of withdrawals and 4844 is keep the spec separate, especially on the consensus layer not encumbering these two things. You know, it's a bit cleaner probably on the way EIP is justified. At if at the end of January withdrawals and 4844 actually look realistic like in a May time horizon, ship from the same software but stagger activation for by a week because they are separate specs and encumbering the specs of that point will be difficult especially on the consensus layer side. And if not, then say, okay, 4844's next fork, and withdrawals, will come out. I mean, I think everyone that's working on 4844 plans on having what looks like future complete nearing production is testnets by the end of January. If that's not it does not net than, than I do believe at that point it would significantly delay withdrawals and thus separate at that point. But keep them kind of intellectually specified separate.

**Tim Beiko** (35:46) - Got it. And Sean?

**Sean Anderson** (35:48) - Yeah, so I think we're pretty far along as far as the initially the this, the spec that we currently have for 4844 but I do actually think there are some significant unknowns, which would change the timeline on the order of like, a couple months, maybe more, I'm not really sure. And that would be like specifically seeing what having big blobs in the gossip network looks like because that could change like how we have to specify things. And on top of that, like big question, I think that we've had is about how bandwidth looks with adding blobs, and this could require something like episub as an upgrade to gossipsub, which, I mean, I think Lighthouse is pretty far along with but I'm not sure if other teams have really worked on it. Yes, it's things like that. And also, I think Mike could just point to it in the chat. Like the question about like, whether the data availability window should be like have a hard upper bound at 18 days. I think that's like a pretty deep sort of philosophical question, and that would have bigger implications if that's if we don't make that a hard 18 days. Yeah, so to me, there are some unknowns with the current spec, though we are pretty far along.

**Tim Beiko** (37:22) - Got it. So clearly like it seems like you know, there's a desire to do 4844 as quickly as possible, not affect withdrawals too much. And, and yeah, make sure those two things kind of come out quickly, but but they're not holding each other back. On the CL side, they luckily have these nice executable specs which make it easy to specify things these this way, and kind of have this this logical dependency between them. We don't quite have this on the EL yet. So I think if we do something similar like we have this Shanghai spec, which is the equivalent of the Capella spec on the, on the CL where, you know, we implement withdrawals. We we then can basically have, you know, EIPs that are like, scheduled on top of that. Where, you know, it would basically be like planning the next fork and having 4844 on top of it, and then we can decide whether we want to activate them in quick succession or not. Do people feel like on the EL side, like this is something we we can do as well like where we just say, you know, we're gonna have withdrawals as the as the Shanghai fork. We then have a specification for what comes after it includes 4844 and yeah, this way, you know, if, if we're really confident in the work on 4844, and it's going quite well. We can have the activation happened really quickly after but if for whatever reason, you know, it takes longer than we ended up in a spot where yeah, we can delay 4844 and there's no like technical coupling to the withdrawals fork, which can go live. So basically, kind of have a spec for a new fork. Have 4844 included in that and keep Shanghai as the spec for withdrawals and, you know, potentially some other things Does anyone disagree with that approach?

**Danny Ryan** (39:55) - Yeah, I think whether that is independently whether that's realistic, but they might have actually been coupled is dependent on 4844, but also it was kind of additional dependencies of what else goes in Shanghai, not conditionally, you know, and that could also make or break, whether the strategy's even realistic. But, you know, depends on the items. 

**Tim Beiko** (40:20) - Right, right. And I think yeah, there's Yeah, and but the first point, there's, like, you know, can we just align the specs in a kind of weird way so that we do have like, we have 4844 specified as happening after withdrawals have that not be really like up for debate in that like, you know, it is kind of considered the main thing that's coming into the next upgrade and we make this decision now, basically. Jesse?

**Jesse Pollak** (40:52) - Yeah, I just want to say I also don't want to forget EOF, I feel like they've been doing a really good job executing on this. And it is the sort of developer productivity thing that can can get left behind. And so I want to plus one, what Proto said and what it sounds like a lot of folks will be excited about which is the idea of like, pushing towards like as fast as possible withdrawals fork super narrow, and then kind of all of us rallying together to ship a fast follow fork with 4844 and EOF basically as quickly as possible. After that, hopefully in the first half of next year. That kind of gets everyone working together to both scale Ethereum and provide a great experience for developers. I'd be really excited about that.

**Tim Beiko** (41:36) - Thanks. Yeah. So I guess just to get, yeah, just get the first withdrawals and 4844 settled and then we can discuss EOF and all the other things where they would fall in those buckets. But does anyone oppose the idea of like, yeah, having withdrawals be the main thing for Shanghai trying to ship it as quickly as possible? Basically, including 4844 in a spec for the next fork like is that on the CL side? And, you know, trying to ship that as quickly as possible after withdrawals, keeping the work parallelized like it effectively already is. And then we can discuss the effort the other various EIPs, you know, where they should fall whether in either of those buckets or none of those buckets? Or we're not, like ready to make a decision about that today. But just high level withdrawals in 4844 does anyone opposed that? Okay. Okay, so let's let's go with that. We don't quite have a way to do this on the EL spec side yet about like adding 4844 and like an upgrade after, I'll, try to come up with something after the call and I'll post it on Core Devs, but effectively, yeah, let's center Shanghai around withdrawals, have 4844 be the kind of center of the next fork. And then from there, you know, assuming I think again, we want it to have quick withdrawals. There's a bunch of comments in the chat about, you know, EOF and just these comments on the call. I guess I'd be curious to hear from maybe the EL teams. What do you feel should go alongside, what do you feel should go alongside either withdrawals or 4844? Yeah, on the on the EE side.

**Marek Moraczyński** (43:39) - So we will prefer smaller forks, so withdrawals and small EIPs however, we are also okay with withdrawals and EOF if other clients feel it would be the best decision and we all can deliver it to some smaller fork but we are okay with EOF and withdrawals. 

**Tim Beiko** (44:00) - Okay, thanks. Any other client team?

**Andrew Ashikhmin** (44:05) - I think it's the same for Erigon, as Marek said, we are fine with a small real Shanghai with just withdrawals but they're also fine with withdrawals plus EOF. 

**Tim Beiko** (44:18) - OK. Besu?

**Justin Florentine** (44:24) - Echoing the same status for Besu, withdrawals plus EOF is pretty ideal for us. 

**Tim Beiko** (44:31) - Okay, and Geth?

**Lightclient** (44:33) - I'm not sure if anybody else from the team wants to chime in obviously, I've been working on EOF a fair bit and I think it makes sense to do EOF withdrawals, but that's just my point of view.

**Péter Szilágyi** (44:48) - Yeah, I think that's fine. If Matt or Randy has those things covered, I trust this decision.

**Tim Beiko** (45:03) - And I guess, yeah. Danny has two comments about the EOF spec status updates in the chat. So yeah, I don't know Matt or Axic because on the call, but do either of you want to give a quick update on where, yeah, where EOF is that and yeah. With like the recent changes have been added.

**Lightclient** (45:31) - Yeah, I can share a couple of things and then I'm sure Axic can probably share some stuff. The last couple weeks we've been working on just like resolving some of these like, small open questions in this checklist. And pretty much all of those things are, have been resolved. I think that there's basically just like one sort of like optimization question around the header about how to encode the code section sizes that were like debating a little bit. But I think, you know, other than that, everything else is pretty much resolved. We're finishing some of the PRs EIPs Paul was on vacation this week. So a couple of the things that he was like working on, we haven't been able to merge those to the EIPs. But we've written this unified spec, which is sort of a meta spec of all of the EOF EIPs and it has the like updated versions of all these things. So it's best to look at that unified spec to try and understand that overall change set of what EOF is providing. And I think that if you look at that unified spec, you'll realize that the overall change that of these five EIPs is actually smaller than you know, it feels what's the five EIPs so that's kind of where the spec is. Alex and some of the Epislon people have been talking a lot with the Solidity team. We've just changed a little bit of the exact opcodes that are provided to support like exactly what the Solidity team feels is important for EOF. But, you know, adding EOF is the main thing and so having like, what additional opcode is like extremely trivial to implement it to test. It's mainly about providing that container format and providing the like semantic environment to execute. And I don't know if Leo, if you want to give us perspective from Solidity too?

**Leo** (47:25) - Hey, yeah, so this is Leo from Solidity, Daniel couldn't join, so I'm here on his behalf. So yes, Solidity's in full support of EOF and the jist just like there's a lot of nice thing that we that we think would help the language, the compiler and the users as well and the developers in terms of gas security, optimizations, UX, debugging different things. So yeah, so it's one of the priority items in the current solidity roadmap and we have a few PRs that were merged already and a few others that are in progress right now. So yeah, I think it's really well. Yes. The other thing that I want to bring up was 663. So but I'm not sure if it's, this is the right time. So I'll leave it at that.

**Tim Beiko** (48:16) - Yeah, let's do 663 after but thanks for the context Leo. Danny?

**Danny Ryan** (48:23) - So I look at the look at the checklist and seems like a lot. I'm not deep in this. Do we think that we will have we will be able to do mainnet shadow forks of a feature complete frozen spec in January, just given given where we're at on that?

**Lightclient** (48:42) - I feel pretty comfortable with that. I think the implementation is relatively straightforward. It's like one to two weeks tops engineering time and most clients are already 70% or farther on the spec.

**Tim Beiko** (49:02) - Does any yeah EL team feel like really uneasy from that. Like the idea of an EOF and mainnet shadow fork with EOF and withdrawals in in January? Okay, Proto?

**Protolambda** (49:28) - So I want to emphasize that not delaying withdrawals is a common goal between everyone here. Just for withdrawals itself, but also not to delay public testnets of all the features afterwards, including 4844 and so it's really like some strong commitments from EL teams that they do not believe that anything they'll delay the withdrawals hard fork. 

**Tim Beiko** (50:03) - Yeah, yeah. Do any of the EL teams want to chime in?

**Marek Moraczyński** (50:10) - We will work on the (inaudible) on all features so EOF 4844 and withdrawals. Shadow fork in January might be a bit challenging but I think we are okay with that.

**Tim Beiko** (50:30) - Besu and Erigon?

**Justin Florentine** (50:36) - Besu is happy with that EOF is well on hand, withdrawals is well in hand. We should be happy with a mainnet shadow fork in January, I guess let's talk about maybe more specific when January. I mean early January feels like a non starter due to vacations and whatnot.

**Tim Beiko** (50:52) - Yeah, I think yeah, we usually mean like the late January obviously because basically coming back from vacation. You know, maybe we have like two weeks where people kind of finalize implementations. We run some devnets with all the clients and then you know, we're in a spot where we're ready to shadow fork. I think that'd be. 

**Justin Florentine** (51:12) - Okay. Sounds good.

**Andrew Ashikhmin** (51:17) - From Erigon withdrawals EOF is fine, I think shadow fork late January, early but probably more like early February is not realistic.

**Tim Beiko** (51:34) - Dankrad?

**Dankrad Feist** (51:38) - Yeah, I mean, I have to say I'm honestly extremely surprised by this discussion. Because like, it's it feels like when you've when people talk about still implementing new opcodes that come out of a Solidity team that this is more ongoing research. Like, are we really implementing the best version of EOF if we literally make the time pressure to free specs like basically right now? So that's my first question was because it seems like the specs are very much in flux. And the second question is like, so I mean from from what people say, it does not feel like this does not delay withdrawals. So like, why like it seems very likely that this will actually delay withdrawals. And so I would be extremely against coupling this with withdrawals hard fork if we're saying oh, we can't. We can't couple EOF, sorry, 4844 with it. Since that is I think like infinitely more important the future of Ethereum. 

**Tim Beiko** (52:49) - I guess, does anyone like on the part of like EOF spec readiness. I know Danno you had a comment in the chat. Do you want to maybe, yeah, share your thoughts on like, how, like, where you live is that and then yeah, then we can do Ansgar.

**Danno Ferrin** (53:05) - So some of these opcodes have been brought in and discussed literally for years. They've been tested, implemented and things like EVM one. So these are not like new ideas that are being brought in. All the new ideas that are coming in already established there. So it's been discussed is bringing in things that people have been, you know, back in 2020. This whole any significant EVM changes put on pause until the merge is done. So it's all been done being held in abeyance until then. What we're really just waiting, is for a finished spec to say okay, this is exactly what's in it. So there's not too terribly much research going on and to some of the some of these new opcodes are being asked to be put in and they're quite, you know, isolated and separate from one another. The only real burden is getting the testing the testing, specs done in the Ethereum test. And there's people that have written tests for those who are ready to those are also sitting in some cases in PRs, waiting just to be checked in and turned on.

**Tim Beiko** (54:03) - Thanks, Ansgar?

**Ansgar Dietrichs** (54:06) - Oh, yeah, I just wanted to briefly say that I think it's probably not very productive to keep having doing the kind of discussion of whether or not we believed EOF was ready enough or not, because it's seems like most client teams are pretty confident. So the only thing I would say is that kind of once we have our first ACD in January, we should come into this with a mindset of if withdrawals is ready and anything else in the Shanghai hard fork is not quite ready, even if it's just looking like it's a week or two or three or four delay. We should be very (inaudible) and said can we slim down Shanghai for to just withdrawals and move ahead. And as long as I think we all kind of have that commitment in mind. I think it makes sense to just move ahead with EOF in it. Sounds like everyone's optimistic on that front.

**Tim Beiko** (54:56) - Yeah, and I guess on that note, how, because there is some engineering costs to remove EIPs once we've started coupling them too much and we've seen consensus issues in the past because we like, made a mistake when removing an EIP from a client. So I, I agree conceptually with your proposal Ansgar, but like from the perspective of like, the implementations, how doable is this so like, if we come if we come to January and you know we want to actually remove EOF, is you know, is this gonna take like three weeks extra do properly do well? Like what? Yeah, and are we like kind of back in the same spot? Yeah, I don't, I'd be curious to hear from just the client teams like how easy it is to remove if if we choose to go that way.

**Marek Moraczyński** (55:54) - So for us, it is no problem for removing EIPs.

**Tim Beiko** (56:02) - And Geth is saying it's easy, as well. Basically, Erigon is it easy on your end as well?

**Andrew Ashikhmin** (56:14) - Yeah, it's relatively easy.

**Tim Beiko** (56:21) - And Besu, just want to confirm as well. 

**Danno Ferrin** (56:29) - Ditto.

**Tim Beiko** (56:30) - So I don't know yeah, um is like, I think again, like there's a ton of comments in the chat about delaying withdrawals, like on the EL side, the client teams feel like having Shanghai being basically withdrawals, EOF, and like have three tiny EIPs that were already there. Like that this will not basically delay the withdrawal that will be ready for like, January, Mainnet shadow fork basically.

**Péter Szilágyi** (57:11) - Pretty much Erigon thinks it that it won't be ready for them. For for January. 

**Andrew Ashikhmin** (57:23) - Yeah, but early. Yeah, maybe late January, early February. That should be fine.

**Marek Moraczyński** (57:31) - I think late January on our side.

**Marius Van Der Wijden** (57:35) - Let's aim for early January, please, and just put some more resources on it and we can do it.

**Tim Beiko** (57:46) - And when I guess, yeah. When would people want to make a call about removing EOF if we're not happy? So we have the first All Core Devs will be January 5, and then we'll have January 19. What would we want to have seen on both of those calls, you know, to keep our confidence that this is not going to delay withdrawals? Andrew?

**Andrew Ashikhmin** (58:24) - Well, I don't understand why, like I mean, it depends on how much by how much withdrawals are delayed. To my mind, a week is like, why would a week or even two weeks or even a month, be that critical? I'm not saying that we should delay withdrawals by a month but to my mind, a week is nothing.

**Tim Beiko** (58:50) - Yeah, I think a week it's probably hard to like even know like that a week. Yeah, can that's like we could plan a week delay that far in advance. I do think if people feel like it's gonna be a month or more then and we feel that way today, then that's a sign that like it's probably going to be more than that. Yeah. Yeah. Holger, you had your hand up then Danny.

**Hdrewes** (59:22) - Yeah. So I think I would add to the discussion that two months or so actually makes a huge differences regarding delaying and so if we're talking about a March Shanghai hard fork, for me, adding EOF in was was this kind of this kind of like current specs, status and and planning on all the testnets and everything sounds extremely ambitious. So I would really go along with with (inaudible), so certain reservations or if we're talking about May, this might be rather doable, this is kind of like I think we this is pretty narrow what we are planning here. Yes. So I've actually posted on the on the issue agenda. This is another suggestion that we could actually do a relatively quick hard fork after the Shanghai hard fork and then like two or three months after that, and then bundle 4844 and EOF. And from my perspective, since since EOF is not so pressing, nevertheless, great to have but really not super pressing. This would be the more attractive possibility still because then we have two or three months more time, can can calmly plan our testnets and this would not do so much harm. So I think this might be another attractive alternative here.

**Tim Beiko**  (1:00:49)  
There's, yeah, some plus ones in the chat for this. Danny, you had your hand up as well.

**Danny Ryan** (1:00:55) - Yeah, I was just gonna comment. You know, the, what is the week delay? What is two week delay? I just I know that many, if not all the teams on this call are planning on hitting, testnet kind of milestone targets at the end of January. And that's why I think it keeps coming up. You know, if we get to the end of that and don't have strong signal and something like that's, that is a that is reason for delay, because that is going to be a big development target. So you know, if then you can ship it there next week. That's probably fine, but I just think we're going to have a lot of information at the end of January. 

**Tim Beiko** (1:01:47) - Yeah, I think the so clearly, you know, on the EL side, teams feel like they can do something alongside withdrawals, and and like, generally feel like EOF is possible. If so, if we go that route, and EOF like is not ready, I think the what this means then is we basically remove EOF from Shanghai and also that none of the other potentially smaller EIPs that you know, we've been discussing will make it in Shanghai. And I think that's basically kind of the the trade off there like where we need to be okay with saying in January like EOF is not ready. Let's just do withdrawals. By that point, it won't be possible I think to add something else to like, replace EOF because you have to incur like a bunch of testing overhead so so that means you know, there's a possibility we ship we ship Shanghai on the EL side with specifically like literally just withdrawals and like these three tiny EIPs and the time it's going to take to like remove EOF safely from the codebase and whatnot means you know, we probably won't be able to add something else if we don't want to delay withdrawals. So I guess you know, like our EL teams like okay with that trade off, basically. I see Moody you have your hands up so it might be worth taking a minute or two to cover 1153 and where it's at because I think if we go that route, this is you know, one of the things we're like, implicitly not including in Shanghai. Yea, Moody?

**Moody** (1:03:49) -  Yeah. I was just gonna ask that we don't couple EOF with 1153. I think they're pretty unrelated and 1153 is ready to go into testnet, as soon as it's ready. As soon as the testnet goes up. It's implemented in three of the five clients and one of the PRs is just waiting for clarity that it will be in Shanghai. And so I think it it can go into testnets as soon as we just move it to the inclusion category.

**Tim Beiko** (1:04:27) - Right but then the question is the teams feel like we can like have the bandwidth to test that and have it on side? Andrew?

**Andrew Ashikhmin** (1:04:39) - Well, I think we can just schedule it for Cancun along with 4844. So I would not include it into Shanghai because back withdrawals plus EOF it's on the board or borderline, it's it's not delay. It's more like like delayed by a week. But booting anything else will definitely delay it more. So yeah, I would I would just schedule 1153 and 4844 for Cancun.

**Moody** (1:05:14) - In past calls it was moved to CFI I believe the conclusion was to get it into a testnet and if there's any delay to the testing, we could drop it so this seems like a change which is because EOF recently got made CFI. Just want to make sure I understand like the process here.

**Andrew Ashikhmin** (1:05:44) - Well, we have so many EIPs in the CFI. We cannot implement them all in Shanghai.

**Tim Beiko** (1:05:51) - Right. We have to choose a subset of that. And I think obviously like any incremental thing we add, has like some costs and I think if if basically if we feel like EOF is like the single thing and it's already quite big then yeah, then it doesn't make sense to include something even like in addition to EOF and withdrawals. I do want that like yeah, there's a bunch of comments in the chat about you know, is is like is Erigon like with the idea that like EOF might be borderline possible for Erigon like what does that mean? And you know, those that ended up having a delay so I I don't know. Yeah, Andrew like, if it was just up to Erigon, do you think EOF is like significantly bigger to implement alongside withdrawals then, you know, something like 1153? I guess. Yeah. Or maybe like I think what I'm trying to understand is, you know when you say that it's unclear if you'd be ready for a January shadow fork, is this because of like the size of EOF? Is it because of like withdrawals? EOF just like, generally, like, or? And yeah, how does EOF basically change like Erigon's readiness for Shanghai? 

**Andrew Ashikhmin** (1:07:22) - Well, there is a PR for EOF against Erigon and maybe it might there might be PR for 1153 I don't remember. But with, I'm just thinking that because so EOF is kind of this pack is ready, almost ready and the implementation is almost ready and so on. So we have it won't be an act bigger an additional chunk of work and I would rather yeah. So with the so there's a delay compared withdrawals with EOF and compared to the withdrawals without the the delay that you have adds probably small like one week or something. So from my point of view, I'm happy to do EOF and Shanghai. 

**Tim Beiko** (1:08:36) - Okay, I think yeah, I think that basically coming back to the, the earlier point and you know, not delaying withdrawals, like basically what is the cut off that we want? I think on both of the All Core Devs to decide EOF is actually not ready and you know, we should remove it to not delay anything further. That seems to be generally the direction EL teams wanna gonna go in is to try and get EOF. But it's very easy if we go down that path. I feel like you know, I feel like we have some costs and oh, it's only two more weeks and it's only two more weeks and next thing you know, we've delayed withdrawals six weeks because of this. So you know, there's a bunch of yeah, there's a bunch of, I guess, things that we need between between like, going live on mainnet and and having like the specs ready, so like when we come back in January is basically I think three kind of check ins. So there's the first two All Core Devs. So January 5, January 19. Then there's going to be a client team interop week and the week after that so like, what are the things that we want to be sure we have for like, like, what are the stages we want to be at basically on the fifth, the nineteenth, and like the end of the interop week, such that like we're happy with EOF and we feel like we're ready to move and if we don't if we're not at that spot, then we should we should just remove it. I'm curious to hear just from like client teams like on January 5, like on the next All Core Devs, where should we be at and then two weeks after that's right before interop, where should we be at? If no one has suggestions. I have some thoughts but so I think yeah, and Barnabas has a comment about you know, we're obviously going into the holidays. So I think it is realistic to expect though that a month from now. Like one that EOF spec should be like, really final. We should have implementation in all of the client teams. And ideally like complete test coverage and things like Hive and Etherum/tests. I think we have most of that, all of this already. I think on the 19th, two weeks after that, I would want us to have like a first basically, yeah, after the first All Core Devs, so after the fifth, I would want us to have a devnet which has EOF with all of the EL clients in the week after that so you know the week of the ninth, then by the like, next All Core Devs, we should be planning like a either a Goerli shadow fork or a mainnet shadow fork, like the first one, I think with EOF kind of withdrawals. And if we want to hit March, that's roughly where we need to be. So like, yeah, I think we need basically full implementation or and you know, spec readiness and testing like in the next month and like shadow forks and devnets happening in between January say like fifth and nineteen so that we go to interop we know that like it works across all the teams. We finish in like we iron down some cross client issues during that, we hopefully we have like a clean mainnet shadow fork during the interop week. And then we know that like 4844 and withdrawals are solid and they're ready to be moved to devnets. I think if, yeah, if we get to like the second like the basically the first All Core Devs, and we don't have client implementations that are pretty much ready across all teams, or the second All Core Devs and like we're not able to have all of those running on a devnet or like soon on a mainnet shadow fork. To me that would be the signals that like we cut EOF out and and literally just ship just ship withdrawals and the three small EIPs. Does anyone disagree with that?

**Micah Zoltu** (1:13:13) - Week of January, is there an ACD before that, or is that the first ACD call?

**Tim Beiko** (1:13:18) - It's the first, yeah, so so the fifth of January is the next one.

**Micah Zoltu** (1:13:25) - Sorry, the fifth of January is the first week of January? 

**Tim Beiko** (1:13:28) - Correct. 

**Micah Zoltu** (1:13:29) - So this will be one week after the first ACD call, is that correct? That we're targeting?

**Tim Beiko** (1:13:35) - Correct. So I think on the first January on the first week on the All Core Devs, we want to make sure like the clients have implementations that are basically done. They work together like they're interoperating between the two All Core Devs so that on the nineteenth, we can basically be planning mainnet shadow forks.

**Micah Zoltu** (1:13:52) - Okay. So functionally the cut off is the first January 5, like if not everybody if everybody isn't done with the EOF and withdrawals, but January 5, we're dropping EOF.

**Tim Beiko** (1:14:07) - Yeah, I think single client implementations that's what I would say. And because there's like two steps to this one is like you know, is it implemented in your client and like there's a generally passed the test suite. I think we'd want that by the first All Core Devs, so the first week of January, and then it's always like trickier to then get them all on devnets because different implementations need to like agree with each other and you might find bugs and I think this is what we want to iron out between the first and second All Core Devs with next year basically. And if by the second All Core Devs were not like pretty confident that we can run this stuff on devnets, you know with different client teams and it January works. I think we should we should remove it from from Shanghai at that point.

**Micah Zoltu** (1:14:51) - So just just so everybody who's not looking at calendars aware, functionally if you take about a week or two off for Christmas, that means everything's be done in two weeks. Right? 

**Tim Beiko** (1:15:00) - Correct. 

**Micah Zoltu** (1:15:00) - Like two weeks from now. Now for two weeks, get everything done. You take two weeks off for Christmas, and then as soon as you get back, we're going to evaluate if everybody's finished. 

**Tim Beiko** (1:15:10) - Correct.

**Danny Ryan** (1:15:14) - Is there a how clear do people feel about the kind of requirements that are needed in the first week of January? Like when we get on that call, is it black and white? Exactly what it means to be either yes, ready or not?

**Marius Van Der Wijden** (1:15:43) - I would say have an implementation and test the test vectors. I think we have already test vectors for EOF, so, if you're testing those and Martin worked on a tool, where we can first the like the verification mechanism of the EOF. So you should also implement this thing so that we can fast your implementation for the contract verification I would.

**Tim Beiko** (1:16:17) - I would maybe like add to that. We should make sure that there are test vectors for like the entire spec, right like obviously, like the spec kind of changed relatively recently. So like, there should be like full test coverage as well. If we don't have that by early January, that seems like another problem.

**Marius Van Der Wijden** (1:16:42)  - Um, Mario, can you quickly comment on what we have for EOF tests. 

**Mario Vega** (1:16:49) - I'm currently working on a separate EOF test but the currently available set, I'm not really sure if they are updated. I will get back to you.

**Lightclient** (1:17:01) - There's also tests and retest these from the epsilon team.

**Tim Beiko** (1:17:10) - Yeah, so we should make sure that you know all the functionality is tested, either retest suite or Mario's test suite so that clients can can check against it. And we expect that by the first week of January this first All Core Devs, clients are basically passing tests for EOF. Does that and then because this basically tells us that single client implementations are ready, I think then we get another two weeks to make sure that cross client interop works well, basically. And I think those are like the two cut offs. Does anyone disagree with that? And then sorry, I know Potuz and Moody your hand has been up for a while. We'll get to that right next, I just want to make sure on these two, these two milestones. Any disagreements? Okay. Okay, so let's move forward with that. So, Jan five, single client implementation, full test coverage and then Jan nineteenth, interop and Shadow forking after that. Potuz and Moody?

**Potuz** (1:18:37) - So I have a question that is kind of related. It's not hard fork requirements, but so we wanted to have a decision on Engine API, and Marek suggested today to have the block value by Shanghai. So at the fork, and I was wondering if, if we can get some clarification from EL clients if this is possible, if it's going to be ready or not, because depending on that is whether or not we're going to implement this now or not.

**Marius Van Der Wijden** (1:19:10) - We will be ready, I have a draft PR. I'm just waiting for the spec to finish like to be like finalized. So I will. It's it's like five line change for Geth and presumably for all the other clients as well. So yeah.

**Potuz** (1:19:31) - We good if we just move to add this to our Capella branches and we start testing this on even on their devnets.

**Marius Van Der Wijden** (1:19:38) - Yes. From my side, I think yes. 

**Potuz** (1:19:42) - That's good. 

**Tim Beiko** (1:19:45) - Moody?

**Moody** (1:19:48) - Hey. So I think in the chat, like, the concern with 1153 is that we, it might delay withdrawal, especially in combination with EOF, but I mean, from my perspective, it doesn't seem like it. It seems like one of the only EIPs that won't delay withdrawals to quote Sara. And so just to get some consistency be great to understand, like, who, who thinks it would delay withdrawals because it's already implemented everywhere. It has a lot of test coverage with Ethereum tests. So I just wanted to pitch in understand, like, why we think it'll delay withdrawals if it's included. 

**Tim Beiko** (1:20:37) - Marius?

**Marius Van Der Wijden** (1:20:40) - Yeah, so I think it already delayed delayed withdrawals. And I think a lot of the other EIPs already delayed withdrawals by the way. I think one of the big issues I have with 1153 Is that kind of from from process perspective, youth and like other people from Uniswap, and an Optimism has been pushing that very, very hard. And it's I don't think it's a very important EIP. It's like a really, really small improvement to the Ethereum protocol. And so, just having like, just scheduled like, the, like the technical part is only one part of the equation. Right? And I think the bigger part is like the headroom and like thinking about it, trying to schedule it. Trying to test it trying to test it in together with other EIPs. That's kind of its kind of like in my concern and then of course the like the concern that Solidity still hasn't declared that they can use it, or that they are going to use it. I'm not saying we should make a decision solely based on what Solidity thinks. But I think in order for this EIP to be a positive for the network, we need to have buy in from the big language teams. And I have not seen that. And that's why I'm a bit hesitant to schedule this anytime soon.

**Micah Zoltu** (1:22:25) - Other than other than the Solidity thing you mentioned at the end, are all those or none of those or some subset of those things that other people could do or some of them things that only Geth team members can do? 

**Marius Van Der Wijden** (1:22:39) - Sorry again? 

**Micah Zoltu** (1:22:40) - Like you mentioned, like testing and stuff like that. Are these things that some third party could pitch in and do or are they things that you really want the Geth team specifically to do? Like for example, PR reviews, a lot of teams prefer to have someone who's on their team do the PR review they don't want an outside contributor to do the PR review like we cannot kind of work for testing and other things or what can't be outsourced?

**Marius Van Der Wijden** (1:23:04) - No, I think like some testing can be outsourced. But in the end those people like those outside people are not the people like paying the price if something goes wrong, it's it's it's us and so it's very important for us to also have a look at it.

**Tim Beiko** (1:23:28) - Leo and Sara?

**Leo** (1:23:32) - Hey, just wanted to quickly clarify from from the Solidity perspective, there's like two sides of this thing. There's a personal opinion of team members like me, Chris or Daniel about the EIP itself and whether it should be included and in the current shape or not. It's kind of things. On the other side, Solidity as a tool, would of course include transient storage if it gets in. This is this is not a discussion right? So if it goes in the compiler will, at least right away support the basics, which is just like add the opcodes or supported via the bottom, which is which you can already use it that way too. And what would take a longer amount of time is just like using it like supporting it properly and the optimizers and this kind of thing. So yes, as far as support goes, there would be immediate support in like very, very basic support. And it would take longer to fully support it and you optimize these kind of things. And there's a different thing which is a personal opinion of team members on the itself. Thanks for for sharing.

**Tim Beiko** (1:24:41) - Sara.

**Sara Reynolds** (1:24:43) - Hi. Yeah, I'm more of a response to back Marius. It, it sounds like a lot of your critiques are mostly around sort of the rallying and who's implemented the EIP, which I don't see, you know, that doesn't have a lot of technical merit in it. And I actually think it's been an EIP you know, that that can set the precedent for having outside contributors. You know, non client devs work on things like this. And so, I yeah, I think that, you know, it's been awesome to see that from the community and we'd like to see more of that from other EIPs. I think at this point, it's ready. It's done. It's been tested. It would not delay withdrawals, and I don't really see any technical merit in pushing it past Shanghai.

**Tim Beiko** (1:25:44) - I guess does any client team feel like we should bring it in and that they have the bandwidth? I think, to me, this is like the main thing is just, you know, EOF already feels like it is somewhat of a stretch and that, you know, we're having pretty specific kind of gates that we want to see. And you know, we have high confidence but not certainty that we can reach those gates. So like, does any client team feel like adding 1153 alongside that would still mean you know, we have really high confidence we're gonna reach those gates?

**Marek Moraczyński** (1:26:32) - So I read some discussion, that marking from Geth team had some concerns about this EIP. However, I don't know details, but if the concerns are valid, I don't know.

**Andrew Ashikhmin** (1:26:56) - I agree with Marius I think it's about the headroom. So to my mind, EIP 1153 might be a good one, but it is not important enough to like to occupy our headroom for with it in Shanghai. We have a Shanghai is already for withdrawals and let's concentrate on that. Let's postpone 1153. And like stop wasting our time. Like let's concentrate on Shanghai. Please

**Tim Beiko** (1:27:33) - Okay, so I think you know, just we only have five minutes left and there's two at least Shanghai related things that we we need to cover. So like, my understanding at this point is for Shanghai, what we want are the currently included EIPs, so the ones that were already in, so this is a warm COINBASE one, the push the zero limited meter initcode, which are I believe, already implemented in pretty much all the clients. Obviously want withdrawals, which is the main thing and then we will add the five EOF EIPs 3540, 3670, 4200, 4750, 50 5450. Five EOF EIPs that people have been working on and then if we don't have those implemented in clients and kind of well tested by the first by the first All Core Devs, so January 5, we remove it. So we remove EOF to be explicit. Then assuming we are in that spot, early January, right after this first All Core Devs. We started working on cross client interop if we get to the second All Core Dev if we get to the second All Core Devs, then we we and we don't have cross client interop. We remove EOF to make sure that we don't we don't delay withdrawals. Does anyone have a different view of what just happened? That's my rough understanding. At least for Shanghai.

**Jesse Pollak** (1:29:13) - Can you play that through for 4844? (inaudible) it's been this called came up for 4844 and there was a (inaudible) there.

**Tim Beiko** (1:29:20) - Yea. So I think for 4844, so assuming this is all like we're on the same page about this for Shanghai, we would say 4844 is the main thing that goes into the next upgrade. We'll figure out some way to specify that on the EL side because doesn't currently exist. But I think we have a commitment that that's what we want to do. And then given we only have three minutes left, I don't think it's worth discussing today if there's anything else you know, we want a couple in that upgrade but I think early January, this is what we would probably discuss on All Core Devs, you know like, if stuff like 1153 for example, should also be kind of included as part of this this next upgrade. But I think for now having a commitment on the specific complete scope of Shanghai and a commitment on 4844 being included in the next fork and kind of the main thing there are the two bits that are really important. And thirdly having clear gates that we want to achieve for EOF being part of for EOF being part of Shanghai and then removing EOF if it does not meet that and the implication being I think like we just heard that client teams will not be able to consider other things for Shanghai. So if EOF doesn't make it, then this implies that like Shanghai is just literally the four small EIPs that are already included. So warm COINBASE, push zero, limit initcode and withdrawals. So that was a long recap, but does anyone sort of disagree with this view? Antonio you have your hand up?

**Antonio Sanso** (1:31:04) - Yeah. Thanks a lot for the recap Tim, just like want to add like if we can have kind of malcommitment if with the next like upgrade of EIP 4844. If we can have like, as well EIP 2537 be taken into consideration.

## Timestamp fork spec and [Add engine_getpayloadV2 with locally built block value](https://github.com/ethereum/execution-apis/pull/314)

**Tim Beiko** (1:31:22) - Yeah, let's talk about that early next year. I I think it makes sense, you know, if we are this like if we've agreed that make 4844 kind of the center of the next upgrade. There's definitely a bunch of other stuff that's like, you know, really important like 1153 like 2537 and whatnot. I think it makes sense to have a conversation about whether we want to like proactively include some of those as well to give kind of clarity to those teams. I just don't think we have the time to do it in one minute today. But yeah, let's let's do early Jan, and I think the two things hopefully we can discuss today, even if it means staying on for an extra couple of minutes, are the timestamp forking spec and then get payloadv2 with the built block value, I guess, with regards to timestamp, forking Marius, I believe you said in the chat earlier today, you're going to come up with a spec for it like an extension would exist. You want to give a quick update there?

**Marius Van Der Wijden** (1:32:32) - Yeah, I'm going to write an EIP I have an implementation in Geth and so I can also add test vectors to the EIP for the fork ID based on based on timestamp.

**Tim Beiko** (1:32:46) - Okay, any questions, comments there? Okay, and then last topic for today, get payloadv2 with the locally built block value. Do we want to have this as part of Shanghai basically the clients want to implement this now have they already implemented it? I think Nethermind said they had, but curious to hear from from other teams.

**Marius Van Der Wijden** (1:33:21) - We haven't implemented not as not as part of Shanghai yet but as like a separate thing, but I'm going to move it to the Shanghai branch. And we should we should finalize the spec.

**Marek Moraczyński** (1:33:35) - So generally the next withdrawal definitely should contain this change right Marius? 

**Marius Van Der Wijden** (1:33:41) - Yes, this and the fork ID change. 

**Marek Moraczyński** (1:33:44) - And getpayload bodies? 

**Marius Van Der Wijden** (1:33:47) - And get payload bodies. Yes. 

**Marek Moraczyński** (1:33:49) - Yeah. Okay. I'm okay.

**Tim Beiko** (1:33:53) - Anyone? Sorry, please.

**Mikhail Kalinin** (1:33:57) - Yeah, just wanted to put it another way it will like this block value, and get payload bodies delayed, Shanghai delivery when I hear from All Core Devs.

**Marius Van Der Wijden** (1:34:09) - It's super super easy.

**Potuz** (1:34:12) - So do we want to include this in the next devnet this week or next week?

**Marius Van Der Wijden** (1:34:18) - I would hope so. Yes. 

**Potuz** (1:34:20) - Okay. 

**Marius Van Der Wijden** (1:34:28) - I think Erigon is probably would probably be fine with it. Besu I don't know that they don't have forking on timestamps yet so might be bigger rework for them.

**Danno Ferrin** (1:34:43) - Under review. 

**Marius Van Der Wijden** (1:34:46) - Perfect.

**Potuz** (1:34:51) - So the forking on timestamp is not so bad because you can just jumping on the devnet that it's already been running and it's already forked. But the other one is bad because we're gonna failed out on blocks that are missing or having the extra field.

**Marius Van Der Wijden** (1:35:05) - Not really if we if we do the if we do the fork it changed and also like this forking

**Potuz** (1:35:11) - You're gonna have to have the hash. Yeah, right.

**Marius Van Der Wijden** (1:35:13) - Yes, exactly.

**Tim Beiko** (1:35:20) - Mikhail, yes.

**Mikhail Kalinin** (1:35:21) - Yeah. Just want to hear from Erigon, Besu about block value and getpayload bodies. The confirmation and from them that wants to delay in Hive from their perspective it time to think just reach out in Discord.

**Andrew Ashikhmin** (1:35:47) - Well it should be okay, just not sure. I think Julian mentioned that we have a draft here I have to double check whether that's the case but in theory, it should be fine.

**Marius Van Der Wijden** (1:36:01) - So for those unaware, get blocked bodies just returns the block bodies, like you give it a hash and it returns the transactions and withdrawals and the other one, sorry, what was the other one? A block value? Value? Yeah, exactly. You just return the value of the block basically, that the transaction fees that you give to the Coinbase and you return that in the new in the getpayload call. So you have you have to compute that value already. You just have to pass it to the caller.

**Andrew Ashikhmin** (1:36:55) - Okay, should be straightforward.

**Mikhail Kalinin** (1:37:01) - And for Besu?

**Jiri Peinlich** (1:37:06) - Sounds straightforward to us as well, I think.

**Mikhail Kalinin** (1:37:10) - So let's just consider them to be included in the Shanghai spec and if we see any issues with that particular delay in Shanghai because of more time needed to implement this, the methods and additions to engineer by then we can consider. 

**Tim Beiko** (1:37:30) - Sounds good. Anything else people want to bring up quickly before we wrap up? Okay, there were two, sorry, Alex. Yeah.

**Alex Beregszaszi** (1:37:54) - Oh, maybe you were actually bringing it up. I 6046. I wanted to just 30 seconds. 

**Tim Beiko** (1:38:01) - Yeah, go for it.

**Alex Beregszaszi** (1:38:04) - Yeah, I'm actually not so 6046 is a alternative to the previous self destruct removal EIPs. I didn't want it to bring it up for Shanghai. I really wanted to bring it up, just mentioned it that there's this alternative proposal and there has been quite a number of discussions about it on Ethereum Magicians. And yeah, just wanted to let everyone know that it would be interesting to discuss the self destruct topic once more. Probably not on All Core Devs but you know, in the coming weeks and months.

**Tim Beiko** (1:38:38) - Yeah, I think I I agree. And I think that's something also like in like when we start looking for the next fork, clearly, all teams felt like doing something with self destruct sooner rather than later was really important and, and so that might be the type of thing we want to also like include alongside 4844 and a future upgrade. That's sort of linked to the EIPs in the agenda. Leo, your hand is up as well.

**Leo** (1:39:10) - Yeah, just wanted to quickly also support 663. It's a very small change that has been accepted in the past and dependent on a (inaudible) or you would have for something this and if you have EOF I think it's a very clear next step. That would be great to add and it would massively aid every EVM, high level language and also users.

**Tim Beiko** (1:39:34) - So people also should review that one. And yeah, I think early next year, we'll probably discuss all this CFI stuff alongside those two. So I would I would encourage folks to have a look. And then beyond that. There were two other small things on the agenda. We didn't get to that at people should have a look at so first is a new endpoint called Eth accounts and proposed by Martin. So if people want to review that a sync, and then second there was a new EIP that wanted to discuss on the call, but we've bumped it two or three calls now already. So if people want to look async at EIP 5988. This is a pre compile for the proceed on hash function which would help ZK roll ups to be carried out, you know, none of these last ones are what would be it would be for Shanghai, but I think it's good context to know that they're being proposed when we start discussing things after Shanghai earlier next year. And then I thank you, Proto for posting your view of the timeline on the agenda. I'll make sure to review that I haven't had time to actually read through this during the call, but skimming it quickly. It seems, seems roughly right. Anything else before we wrap up? Okay, well, thank you very much, everyone. There is a CL call next week as a heads up, but then no All Core Devs until January fifth. We will see you all there. Thanks. Bye bye, everyone.

-----------------------


### Attendees
* Tim Beiko
* Danny Ryan
* Pooja Ranjan
* Micah Zoltu
* Jiri Peinlich
* Marius Van Der Wijden
* Potuz
* Evan Van Ness
* Moody
* Tynes
* Lightclient
* Alex Beregszaszi
* Marek Moraczyński
* Justin Florentine
* Alexey
* Ben Edgington
* Terence
* Lion Dapplion
* Mrabino1
* Barnabas Busa
* Łukasz Rozmej
* Péter Szilágyi
* Danno Ferrin
* Andrew Ashikhmin
* Hdrewes
* Crypdough.eth
* Pari
* Ameziane Hamlat
* Liam Horne
* Georgios Konstantopoulos
* Mehdi Aouadi
* Mikhail Kalinin
* Carlbeek
* Bob Summerwill
* Jesse Pollak
* Stefan Bratanov
* Sara Reynolds
* Phil Ngo
* Caspar Schwarz-Schilling
* Ahmad Bitar
* Marcin Sobczak
* Kasey Kirkham
* Sean Anderson
* Saulius Grigaitis
* Stokes
* Ruben
* George Kadianakis
* Dankrad Feist
* Andrei Maiboroda
* Protolambda
* Gcolvin
* Ansgar Dietrichs
* Jared Wasinger
* Diego López León
* Daniel Celeda
* Trent
* Mario Vega
* Kamil Chodoła
* Ziogaschr
* Kevaundray
* Antonio Sanso
* Oleg Jakushkin
* Leo
* Nishant Das
* Pote
* Sam
* Vitalik
* Tomasz K. Stanczak
* Matt Nelson
* Josh
* Gary Schulte
* Rory Arredondo

-------------------------------------

## Next Meeting
January 5, 2023, 14:00 UTC
