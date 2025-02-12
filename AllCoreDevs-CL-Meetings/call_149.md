# Consensus Layer Call 149

### Meeting Date/Time: Thursday 2025/1/9 at 14:00 UTC
### Meeting Duration: 1 hour
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1258) 
### [Audio/Video of the meeting](https://youtu.be/uIjPkGezPOg) 
### Moderator: Stokes
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
149.1  |**Pectra Devnet 5 & 6** A gas estimation bug caused a three-way chain split on Pectra Devnet 5. The network, according to EF DevOps Engineer Rafael Matias, is still not finalizing. The Nethermind, Reth, Erigon, and Besu client teams are working on bug fixes. Matias added that the latest hive test run on Pectra Devnet 5 also failed, so his team is investigating what happened.
149.2  |**Pectra Devnet 5 & 6** Based on pending changes to Pectra specifications and recent network failures on Pectra Devnet 5, developers agreed they should launch another devnet, Devnet 6, before upgrading public testnets. Matias said that client teams should work on bug fixes first and once hive tests have been run against the updated clients, his team can launch Devnet 6. Stokes highlighted that there are specifications changes to EIP 7702 that still need to be finalized on GitHub. Geth developer “Lightclient” said that he would do this. Stokes also flagged that there is a new CL specifications release for Pectra, version 1.5.0-beta.1, but there are no substantial changes in it that make it very different from the prior release.
149.3  |**Pectra Devnet 5 & 6** Stoked asked how quickly client teams feel confident to launch Devnet 6. Developers agreed to aim for a devnet launch early next week. EF DevOps Engineer Parithosh Jayanthi wrote in the Zoom chat that in parallel developers can also start planning a shadow fork to test Pectra. As background, a shadow fork is a devnet created by forking a live testnet or mainnet. Shadow forks unlike regular devnets keep the same state and history of the forked network so transactions from the forked network can be replayed on the shadow fork.
149.4  |**Pectra Public Testnet and Mainnet Fork Timing** developers discussed the timing for upgrading Ethereum public testnets and mainnet. EF Protocol Support Lead Tim Beiko suggested aiming for a mainnet activation on March 11 as this would mean Pectra activates on Ethereum less than one year from its prior upgrade, Dencun, which occurred on March 13, 2024. A hopeful mainnet activation on March 11 means that public Ethereum testnets, Sepolia and Holesky, must be upgraded on February 19 and 24, respectively, at the latest. Ideally, the two testnets are upgraded earlier on February 12 and 19 to allow end-users and the broader Ethereum ecosystem more time to adequately prepare for the mainnet upgrade.
149.5  |**Pectra Public Testnet and Mainnet Fork Timing** There were no objections to Beiko’s proposed timeline, though clearly, the timeline is tentative as developers have yet to fix the bugs on Devnet 5 and launch Devnet 6. Beiko said that he would follow up with specific block numbers to accompany the proposed dates and put these block numbers up for discussion on the next ACD call. He stressed that if client teams are serious about the proposed timeline then near-final client releases must be ready by February 3, 2025.
149.6  |**PeerDAS** A developer by the screen name “Manu” shared updates about progress on PeerDAS. Other than Lighthouse and Prysm, other client teams are in the process of implementing the latest specifications for PeerDAS. Testing is underway for both Lighthouse and Prysm PeerDAS implementations. Manu said that developers are debugging issues with client interoperability between the two clients.
149.7  |**PeerDAS** PeerDAS is the next major scaling improvement to Ethereum that is tentatively planned for activation in the upgrade after Pectra, which is called Fusaka. PeerDAS will enable “data availability sampling” on Ethereum so that Ethereum nodes have a greater capacity to process and include blob transactions in blocks. EF Research Ansgar Dietrichs said that developers on the call should anticipate PeerDAS to increase the blob throughput of Ethereum by 8x.
149.8  |**PeerDAS** Stokes raised a proposal by OP Labs Engineer “protolambda” to expedite Ethereum’s scaling roadmap by implementing blob parameter-only (BPO) forks. In a post by Protolambda, they explained, “BPO forks are simple Ethereum forks that only change two parameters: blob targets and blob limits. BPO forks give Ethereum flexibility to safely scale blobs in smaller, more regular increments and they give builders confidence that Ethereum will continuously grow its capacity.”
149.9  |**PeerDAS** Prysm developer Terence Tsao cautioned that increasing blob throughput by 8x with PeerDAS could be “a little harder than we think” and will require more research and testing before developers can know for certain how best to roll out the sampling-related code changes. Beiko said in the Zoom chat that another possibility for supporting BPO forks could be to “move the blob target for validators to control” like how validators control the block gas limit.
149.10  |**PeerDAS** Lightclient said that the discussion about BPO forks seemed premature as Pectra will already increase blob capacity to what the network can safely handle and encouraging ways to increase the blob limits beyond this could be unsafe. Dietrichs echoed Lightclient’s concerns. Nethermind developer Ben Adams said that unlike the block gas limit, changes to the blob gas limit may be more difficult for node operators to vote on and fine-tune as each additional blob in a block carries up to 128kB of additional data.
149.11  |**Fusaka Fork Planning Process** Beiko asked developers for their thoughts about the Ethereum fork planning process, its strengths and weaknesses, and areas for improvement considering how planning for Pectra has gone and in preparation for planning the next upgrade, Fusaka. “As some of you may have noticed, people have opinions about All Core Devs and I think Pectra has been kind of a wild fork in terms of coordination and planning,” said Beiko. Stokes echoed Beiko’s sentiments about Pectra and said he is supportive of taking the time to “reflect” on the governance process and improve it for the Fusaka upgrade.
149.12  |**Fusaka Fork Planning Process** Beiko said that he would create an Ethereum Magicians forum to continue the discussion on improvements to Ethereum governance and the ACD process. He encouraged client teams and the broader Ethereum community to chime in with their thoughts. Stokes reminded client teams about the Pectra testing call on Monday, January 27, and EF Researcher Piper Merriam reminded client teams in the Zoom chat that there are less than 100 days left before the self-imposed deadline of May 1, 2025, to remove pre-Merge history from clients.


**Alex**
* Okay. Hey, everyone, this is consensus layer. Call 149. I'll put the link to the agenda here in the chat. it's issue 1258 on the PM repo that we all know and love. And yeah, so the agenda is pretty light today. I imagine everyone's really busy with Devnet five and getting ready for main net. So yeah let's go ahead and just jump in. And first up yeah we'll open with devnet five.  I'd love to hear how we think about how this is going. I know there have been a number of issues with clients people have been working through. I looked at the Devnet yesterday and this morning and yeah, it's well, it's looking better this morning than yesterday in terms of the chain health, but we still aren't finalizing.
* So yeah. Anyone want to give an overview of the latest progress there. And if there's anything we need to touch on to get back to finalizing There. 

**Rafael**
* Yes. So Perry is not around, so I'm giving the update. yeah. Regarding devnet five, as you said, we had a couple of problems there. It's currently not finalizing. There was a problem with, regards with gas as a gas estimation bug, which caused like a three way fork, between Geth. There was Nethermind and Aragon that has been patched, and, we now have, like, devnet amount and at the same fork. but there's also on the rest side, there's like another issue that they are actively looking into right now we also had a bunch of changes on Aragon that just got merged, that we have deployed recently there is also a bug on some basal nodes that are being investigated by the team And, we have also updated yeah, that's mainly on devnet five.
* And then regarding also tests and hive. we have updated hive to the latest images. We also updated the kurtosis configs on the interrupt channel on the pinned messages. and yeah, we try to run a, execute a hive run just before this call to, to kind of Yeah. Tell you guys the results. But unfortunately, that hive run failed, so we. Yeah, we have to investigate why that happened and just retrigger it yeah, I think that's mainly it regarding Devnet five and, which means that. Yeah, we are just we have all the client teams looking into these bugs and. Yeah, they they basically have to be fixed And, there's also regarding Devnet six, so there's going to be, an execution spec test release soonish. And we are basically going to rely on that relay to also, run hive tests against the clients.
* And once we have, like these devnet five bugs fixed and, start running these hive tests, I think then we will be ready, like to start Devnet 6. Okay, great. 

**Alex**
* Thanks. Mario 

**Mario**
* Yeah. So we have two trackers now. So the first one, I'll share it here is the, the devnet, 51.30.0 release. This is basically compatible with 1.2. and we're just waiting. Waiting on a couple of PRs to be merged before we tag the release and just make the release to to the clients. this still does not contain any breaking change. so it should be compatible with the clients that are now, right now, running on Devnet 5. Sorry. And we also have another tracker here, which is just contains one more issue. and this this should be the one that we see if we are going to launch a devnet six. so this will contain the, the update to 7702. And this is incompatible with the client's current Devnet five releases.
* Yeah, that's basically it. If there are any comments, please just, chime in and, and to see if we can, make any changes that are necessary, just let us know, please 

**Alex**
* Cool. Awesome. Thank you so much yeah. I mean, that was gonna be my next question is, what was the difference between 6 and 5 on the spec level? And yeah, there was A7702 change. let's see. I mean, I think that tees us up for another thing, I wanted to call out, which was essentially the CL specs release coming up. it'll be let's see, I believe beta one. Yeah. So version 150, beta one. The only change from 0 to 1 here on the CL side is some extra testing at the moment. So yeah, nothing substantial 
* There. And then in terms of specs on the side there's A7702 change. So yeah, I mean given the turbulence in Devnet five and yeah the, the spec change with 7702 uh devnet. Six makes sense and yeah. Okay I guess that's where we're at anyone Yeah. I guess one question is, like, timing wise, do we want to aim for Devnet six? Like, next week is like, even, you know, early next week would be ideal anyone feel like that's too aggressive or is there any sense of timing to fix Devnet five. 

**Mario**
* Mario. Yeah. So maybe I can give an update on the timing release of the six release, I think, I think, yes, it's doable. we just have to merge 
* Basically two PRS for the five new release and one for the other one. So I think it's doable. We have to make the changes on yields still, but I think they are pretty manageable. Yeah. So next week sounds sounds good on the testing side 

**Rafael**
* Yeah. I mean as I mentioned like once clients have fixed the bugs, they they are looking into currently on Devnet five and like the five tests are passing, we can do it 

**Alex**
* Okay. Great 

**Rafael**
* Yeah 

**Rafael**
* Paris. Paris. Also saying in this chat that yeah, we are planning also Shadowhawk 

**Alex**
* Yeah. Amazing we got a thumbs up from another mind. Any client teams feel like Do they feel good about this? Do they feel like it's too aggressive? point being is, as soon as we knock this out, we can then think about, testnets and mainnet. So we would like to ship Petra as quickly as possible as we all Tim has a question. Do we want all devnet five bugs fixed or do we want in devnet six ready teams? Yeah. So this is a good question. Like, you know, rather than blocking on every last issue with five, we need to go ahead and pipeline six a bit. anyone opposed to something like this, we could basically say clients who are ready with devnet five now, then we can turn around and launch six, you know, again pretty early next week 

**Sean**
* I like that idea 

**Justin**
* Yeah. Same 

**Alex**
* Okay, cool. 

**Marek**
* So I think it would be good to verify that clients fix Devnet five bugs. So we can use this network to test, but it shouldn't block us to start. devnet. Six with the clients that are ready. that's my opinion Great 

**Alex**
* Let's see. And then there is. Okay, so it looks like, this PR is open. Is this the seven, 7 or 2 update? I don't know if this was an update to the update 
* PR 9248. I lost track of who is owning these changes. Is anyone here responsible for them Do we have. Is Ansgar on the call? You're an author here I don't see him. Oh, here you are 

**Ansgar**
* Yes. I was away for a second. Which? Which. Yeah 

**Alex**
* This is to 7702. so there is a kind of last minute update over the last week or two and. Yeah, in any case, like plans here. He says I'll merge it. So I think I think Matt has had the the closest kind of focus on the EIP Okay. Thanks. so great. We can do that. And yeah, that should have all the specs settled. And then we'll get the testing release together and we'll pipeline 10.6, get it out the door as soon as we can Very good anything else on Petra? we could go ahead and talk about potential test net or main net fork timings. I don't know if that's going to be a bit of a distraction for us today Do we want to wait until net six is out and looks stable before talking about that in earnest Okay I assume that's a yes. but in that case, then maybe since the bugs are known right Well, and more, I mean more just to get, you know, start to build a consensus around timelines.
* Like, ideally we can have six out next week and hopefully it looks perfect. And from there, yeah, we can at least think about moving to test nets. in February. Yeah. Okay. I'm looking at the calendar Might be a little tight, but yeah, I mean, again, ideally then we can do a test match in February and aim for a march main net fork Does anyone disagree with these high level timelines Okay, we got to. Let's try okay. Yeah. So yeah there's there's generally consensus in the chat. So yeah I think that'll generally be the plan. And then sure you know as things come up we'll have to maybe adjust here or there. But it seems achievable to me oh yeah Tim has a nice comment here. So if we fork before March 13th, that would be less than one year since we shipped the blobs to then turn around and upgrade the blobs again, which is super cool. So yeah, it gives us some anchor in mid March and that'll just mean, yeah, we'll be quite busy with releases.
* And then also the test net forks in February, but assuming we can get five and six wrapped up in the next week, let's say I think we'll be in a really good place for that Yeah. Okay. So Tim here has a suggestion. Say we go for like March 11th for me. Net then that would suggest yeah I think what is that the second week of February. Either way February you know 12th or 19th or then a week to 19 or 26 for test nets. So February is kind of short. Those are kind of pretty much our only options. But from the chat, it sounds like people are generally okay with those. 

**Tim**
* So if we wanted to do February 12th, it means we want the client releases out, say, on February 3rd, which is less than two weeks from now. If we wanted to do February like 19th for the first, then we want the the releases out, maybe for like February 10th, which is like three weeks, a bit less than three weeks from now. so I don't know if like, yeah, practically teams have a feel of like it's two ish weeks reasonable for test net releases. Is three weeks more reasonable? yeah 

**Alex**
* I feel like historically it's been more like two and. Yeah. 

**Tim**
* And then from now. Right, it's more like, yeah. So from now, do we think we can actually get client releases and like 

**Tim**
* Two weeks, right. Yeah. Or is it more like three weeks. Yeah 

**Sean**
* Yeah. I think we can do two weeks on the lighthouse side 

**Alex**
* So yeah, I mean, focus on five bugs. We'll get six up next week. Then from there, assuming six looks great, then yeah, we can charge ahead with releases and two test sites in February You know, when everyone seems to be generally on the same page that this is not impossible, which is good to hear 

**Tim**
* Great. So maybe in terms of next steps, I can propose some blocks, async in the chat. We can agree to that on next week's call, assuming things are going well. And then if, if next if you know things are fine by next week's call clients should be ready to put out a release sometime between, like, next Thursday and the Monday after that. And then we'd have the blog post go out, you know, on somewhere between the third and the fifth and then first focus first for Koski and then, podium 

**Alex**
* Sounds great to me one question I'd have is if we can basically pipeline the test net releases, like, could we cut a release for the client each? Yeah. Like, could we have one client release that has both civilian and 

**Tim**
* Yes. Sorry. Yeah, that was my assumption. So on Feb three, we release clients for yeah. With the four blocks for both test nets. And then once we fork the test net, we release, clients with the four block for main net 

**Alex**
* Okay, then, anything else on Pectra? it sounds like we have a path to main net, which is really exciting and otherwise. Yeah, everyone's pretty heads down on getting their 
* Anything else we should touch on right now Okay, cool. Then we will move on in the agenda. next up. Yeah. Section around blob scaling and. Yeah, I guess one, question to ask is if there's been any update with, the PeerDas work. there is a parallel stream with PeerDas, and I saw from the testing call the other day that, people are kind of progressing, but no, no big update there for the moment 

**Manu**
* I can give a quick, quick update yes. So, um Paris ran a devnet with prism only during about five days. but prism has a very slow memory leak. And so the Kubernetes kurtosis, or the prism supernova after five days. Not sure if it's related to birds. And we are investigating it for since yesterday, there is lighthouse and prism, which are ready to interop so the devs started to interrupt lighthouse and prism. There is some issues and we are investigating and other clients are, still implementing the spec, for the next devnet 

**Alex**
* Okay. That's cool. Okay Great. So, yeah, I mean, hopefully once Pectra's out, you know, this should be on top of everyone's mind, and, yeah, we can really dig into kudos on top of the foundation from Yeah, this work stream that's been happening in parallel. Thank you. Ansgar ?

**Ansgar**
* Maybe just to just a quick remark on that point. Wait. Wrong microphone Yeah, I can hear you. yeah. Just a quick moment on that. I think right now for these, dev nets or the probation for the dev nets, we're still using relatively low throughput numbers just to, to make it easier to basically reach stability there. But just to basically the expectations are set, right. Like I think at least the goal maybe it's a bit of a stretch goal, but the stretch goal basically for us would in principle be to like roll it out at eight x the throughput of, Petra. So basically six nine, both values times eight, basically more or less, because that is in principle on paper, kind of like the efficiency gains you should get going to sampling. Now, the expectation is that then once we kind of have mature dev nets, there might be some bottlenecks that we run into that basically just like will require some work to resolve so that maybe we then decide to not actually ship for Osaka quite at that level.
* And we go back down a little bit. But just for the people, don't expect that just the throughput levels would be the ones that that are basically the target for, for, for Osaka. Just so that kind of that expectation is set as early as possible yeah. Just wanted to mention that.

**Ben**
* What what numbers did you say 

**Ansgar**
* Basically, eight times the, Pectra throughput. So wait, what is that, six times eight? So like 48 and nine times eight. So 4872 should be like the at least the the what we should aim for for like mature dev nets. And then we can see if we can actually stay at that level or if we have to go back down before we roll it out. But but yeah, 4872 I think should like would be the logical on paper kind of goal to aim for here given the efficiency gains of sampling Cool 

**Alex**
* More Bob's is better. So yeah. that'll be really exciting to see Okay there's nothing else around PeerDAS in particular. I do want to bring up this idea, a number of people have been discussing lately, on Twitter in various places, like. Yeah, essentially, how can we think about, making core development, faster essentially, with lower latency to these different things. And, you know, one obvious suggestion would be to parallelize things. there's this concept that's come up of a blob parameter only fork, a BPO fork where we would essentially make a commitment to treat the blobs, kind of like very fully as a different layer of the stack. And in doing so, you could imagine that, once we are convinced that, you know, some increase to the blob count, say, like what Ellensburg is suggesting with, with us and this ADX scaling, once we know that it's ready to go, we basically greenlight that and have some sort of accelerated, stream or lane, let's say, to act to make that happen. I think it's a pretty exciting idea.
* And yeah, I'm not sure if anyone else has seen this, but in any case, I did want to bring it up. Get it on your radar.
* I think it's a really interesting prompt just to think about like, yeah, you know, we do have these very important parts of the protocol. And, you know, sometimes we can get really in the weeds with some particular IP discussion, which then can block other things. given again how important blobs are to scaling Etherethis seems like a natural fit to be one of these things that we kind of focus on in a special way Terence, we have a comment. 

**Terence**
* Yeah. So I think given the current testing is around 12 max blobs per block, I think eight times, I don't want to like sound like a negative Nancy, but it sounds I think it's a little hard. It could be a little harder than we think. I think it all depends on testing results. So I think like the sooner we can simulate, the better, I suspect. Like we may need something like epbs at the end of the day to do more delayed pipelining such that there are, 12 seconds to propagate the blobs versus today is only one second because of we're close to the four second deadline, so I think timing might be an issue. There 

**Alex**
* Right. So I mean, I think this was Ansgar's point is like, you know, the max that Paradise would give us would be sort of this apex scaling. But then, you know, obviously if we're on test nets, slash dev nets and we see that there are issues like this, we would scale it back down. yeah. Francesco had a question here. Is that because of local block building or. Yeah. Was there like something in particular where you started to see these tight timings? 

**Terence**
* I mean just today like timing game is inevitable right. Builders there are even relayers they delay until three seconds to do anything because they get more time for the getheader. Right. So because of that, you either see timing gain or if there is a huge MeV opportunity, then builders are just willing to censor blobs. They just choose not to include blobs. And that's not ideal either. So yeah. So you have this inherent like, contradicting force at play 

**Alex**
* Right Yeah. So I mean pipelining is good if we, you know, definitely if we find that we need it, that's like a tool in our toolbox to also consider, as we like, think about these changes and maybe circling back to this idea, like, you know, that would be an obvious sort of caveat. If, you know, we need like the vision with this vp0 fork is that, you know, almost like the Ice age. But for the blob count, you could imagine we have like almost semi-regular forks where you're like, bumping up the blob counts to numbers that we have, you know, done the analysis and research to understand is safe. If we need, say, like some massive consensus change, like moving from pure dos to, you know some other DS construction, then yeah, it's not as simple as just dialing up a number. And that's like a bit more complicated So, you know, and to your point, this is something that we could see where it's like, yeah, you know if we do run into some like timings either due to timing games or just like, you know, client software today, then we might need more invasive changes to get to a safe spot Kenneth has a question.
* This would be in the worst case, returning games are being done and the proposer falls back Right. Well, I mean, so Terence's point is that even with remote building or like using the ML pipeline, like builders still play timing games, but they basically just, you know, they do it at the expense of blobs. So, you know, blobs are relatively big. They also don't block propagation. So what you can do instead of yeah. Like if you want to like get that extra edge by like delaying a bit, you would just have your blobs and then you can still land on chain in time. But then yeah, there's, there's less blob throughput My client has a comment here. The fact that we need to do analysis to verify a particular blob parameter increase is safe means it's nothing like difficult to bomb. And yeah, I mean, maybe that wasn't a helpful analogy, but ultimately the idea is to make a commitment as a kid to like, focus on this and yeah, have it be like a primary thing that we think about.
* One point here to recognize is that a number of different layer twos have reached out, and I think they're very interested in helping us with any analysis we need to do. so very much they, they want more blobs. We want more blobs. We can work together to get more blobs. So, yeah, I'm pretty optimistic that this is, definitely at least an avenue worth exploring on our 

**Ansgar**
* Yeah. I just wanted to say on this kind of general topic, like, I do think ultimately blob throughput is mostly like a supply side thing, not a demand side thing. So basically, yes, we should, of course, in terms of setting priorities, always have an eye on like how many blobs could would there be demand for. and I think right now the answer is as many as we can give. So basically like definitely it should be a priority for us. But ultimately, at the end of the day, kind of there are always the technical constraints of like within whatever thing we think is the acceptable maximum load on any given node, how many blobs of throughput can we have? And then the only times that ever changes is usually whenever we actually change the protocol, in one way or another. or I mentioned chat, like for example, if, say we roll out a sharded mempool design or something, sometimes those could be out of protocol changes, but still usually only when there's actual like an actual change in how much we can sustain sustainably, basically support. so I don't really see the case of like basically we can't just be like, oh, okay, now there's more demand. 
* So like tomorrow we are increasing by 20% because presumably, hopefully nodes already run at the maximum that they can support at any given technology stage 

**Alex**
* Right. Yeah. But I don't think we always know that. Right. So like you could imagine that we do. You know, I think historically the HDD posture has been quite conservative. We could say, hey, you know, let's start with 3.6. And, you know, did anything actually change with respect to get to 6.9. Well, what changed is just our confidence in seeing this on mainnet and understanding that, you know, it actually works and that there's headroom to do this. So I think that's where this sort of idea is coming from is like, yes, we would have these like technical changes that would unlock sort of new regimes of like possible numbers. But you could still then imagine almost like a linear or like a scaling on some curve, to unlock more blobs. And in a world where that's the case, then something like a fork or like sequence of forks, I think starts to make a lot of sense There was another idea floating around that Tim shared here. another version would be to move blob target control under the validators domain. So the idea here would be treating it like the gas limit, whereas today, you know, if we want to pump the gas to say 36 million, that's up for validators to signal. And then as they go to build blocks, the gas limit can raise or lower over time.
* There has been this idea to do this with the blobs as well. yeah, it's an interesting one. I don't know if anyone has any thoughts on this. would we want to basically take the blob limit, these blob parameters out of the protocol and put them into Stakers hands Ben 

**Ben**
* I think it's I think it's an interesting idea, and it would be good. However it's a hard one because the gas limit is easy to vote on because it's so fine grained whereas the blob limit, since it's, you know, hard, low, low value integer numbers. I don't know how that would work unless, you know, people voted for actions like they do with the gas and only went past or dropped below. You know, you took the you can have five blobs when it's 5.5. 

**Tim**
* So you can set the blob. The let me get the name right here, but the target blob gas per block. And this would mean it's not necessarily like a full integer, but I don't know A researcher told me you could target a non-integer value, in the client, but then I don't know if this is only true at a spec level. But then, you know, the clients make all these assumptions surrounding, roundings internally that it would break. but there could be a way to, like. Yeah we have a bit more of, like, a gradual like some gradual threshold, a bit like the gas limit. And then when we go over that threshold, then, you know, we raise by one or lower by one, right? 

**Alex**
* That was what Ben was suggesting just now. But I mean, at the end of the day, like the blobs are, you know, they're discrete, they are relatively big. So like it would be like, say, adding another 128kB for every increment, right? it's not something where you can like just very gradually do this. And then if you think about it, it's like, okay, as like a home staker, like, yeah. Am I supposed to be like, oh yeah, I feel like I have more bandwidth. Let me just bump this up. I mean, it would have to be interesting idea 

**Ben**
* It would have to be post peer to us where there's, you know, a lot more flexibility in the capacity 

**Alex**
* Okay. So some interest but a lot of open questions. It sounds like around having validators control the limit cool. I did drop a link to more information if anyone's curious where did it go. So there's an Eth magicians post here. Proto has a nice post here I think explaining more of the idea. Let's see. I think I saw proto on the call. I don't know if you want to say anything else, but if not, yeah. I think to continue the conversation, go to Eth magicians and yeah, definitely an interesting idea 

**Proto**
* Yes. Feedback. Welcome on if magicians we are here to support, the safe increase of blobs 

**Alex**
* Sweet. Thank you And, yeah, I mean, just from scanning the chat, it looks like there's more interest than I would have thought for having this be a validator controlled parameter. So I would say that's another avenue to explore Cool. Okay. if there's anything else on the blobs for now, there was a comment here. Tim wanted to make a suggestion around again, improving a seed process, and in particular a bit of a retrospective on Pectra Tim, I don't know if you'd want to give any context. Otherwise I can say a few words 

**Tim**
* Sure. So, as some of you may have noticed, people have opinions about Alcor devs. and I think Petro has been kind of a wild, fork in terms of coordination and planning and, also a lot of change over the past couple years. So we've had a few of these, Alcor devs like retrospectives in person at different points. but I think before we kind of jumped into plan Pusaka, it might be worth having, like longer conversation around how do we want to approach the process? Are there things we want to do differently? I think we've done a couple tweaks in the past year, which hopefully will be good, but, yeah, I wanted to open the floor of like, you know, one, are people generally interested in this? And then two, how do people feel we should like gather input or feedback? My sense is if we just like dedicated all core devs to this without any prior context, it'll be kind of a mess.
* So, I was thinking either we do some sort of like breakout room tracks, or we have an Eth Magicians thread where people can chime in and then, you know, I can try to summarize that before a call.
* So, yeah, curious how people feel. And then maybe the other dimension as well is like, to what extent we want this to be, you know, client teams feedback versus like the community's feedback and how we should potentially, you know, separate those two things. yeah.
* So I guess it's kind of like a meta conversation about how we improve the process. And then, if we do want to move forward from this, based on the feedback today, I can make, like a more concrete proposal of how we do this. as we wrap up, Petra 

**Alex**
* Yeah, I think it's a great idea. I think, like you said, and we all very much feel Petro is quite of, uh. Yeah, wild, hard fork relative to the others. So taking a moment to reflect and, you know, just generally check in with, like, act as, as a body and as a process. sounds super valuable. So. Yeah, I mean, I think what you said with, like, having a magicians thread, we can leave that up for, like, say, two weeks or something and then find an act to kind of discuss feedback and, and have a conversation there 

**Justin**
* I think, this is Justin from Basu here. I think wild probably means different things to different people. So I'd love for whatever conversation we have to, you know, call it some of the explicit things and cite examples of, hey, this was this was tough or stressful or whatever. The impression 

**Rafael**
* Yeah, I agree. And I think one thing that could be quite helpful, for client teams is if every client team could, like, think through this internally and then share some sort of summary, kind of like we did for the hard fork inclusion proposals. So like understanding like, you know, this is what the 

**Tim**
* Basic team thought and this is what like never mind thought. and if people want to share their personal opinions in addition to that, I think that that's fine as well. But like, yeah, being able to like average out or get like the, the rough mapping of all the, all the client teams would be good. And then 
* Yeah. And then I my sense is I would also open this for the community and we can figure out based on how much input, like what do we want to do on a call. But it would be good to get like external observers and and users perspectives into this as well 
* Yeah. What's your sense having like, should we just have one massive like awkward dev or sorry, magicians thread or maybe like one that's like more community focused one? You know, I think at times we've talked about having sort of like gated participation. Not really. I think we tend just to keep the conversation manageable. 
* I can handle one single thread. there's now an AI summarizer as well on each magician, so if it gets too wild, we can rely on llms. and then I'll try. Yeah. So I'll open a thread and then I'll try to like, pin, you know, the client team's perspectives. And then if there's any particularly good comments or writeups, to try and 
* Keep it a bit cleaned up. and based on how, based on how Petra like shipping goes, we can find the right call where, like, we're kind of waiting around for it to activate on main net or something to have a deeper discussion 

**Alex**
* Yeah. Sounds great Cool. Okay that was it on the agenda. anything else anyone would like to discuss today.

 

---- 


### Attendees
* Stokes
* Tim
* Arnetheduck
* Marek
* Lance
* Micah
* Paul Hauner
* Ben Edgington
* Loin Dapplion
* Terence
* Enrico Del Fante
* Pooja Ranjan
* Hsiao-Wei Wang
* Saulius Grigaitis 
* Roberto B
* Olegjakushkin
* Chris Hager
* Stokes
* Dankrad Feist
* Caspar Schwarz
* Seananderson
* Andrew
* Crypdough.eth
* Zahary
* Matt Nelson
* George Avsetsin
* James HE
* Marius
* Ansgar Dietrichs
* Lightclient
* Stefan Bratanov
* Afri 
* Ahmad Bitar
* Lightclient
* Nishant
* Gabi
* Pari
* Jimmy Chen
* Gajinder
* Ruben
* Mikhail
* Zahary
* Daniel Lehrner
* Andrew
* Daniel Lehrner
* Fredrik
* Kasey Kirkham
* Protolambda
* Cayman Nava
* Stefan Bratanov
* Ziad Ghali
* Barnabas Busa
* Potuz
* Trent
* Jesse Pollak




