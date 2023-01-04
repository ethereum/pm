# All Core Devs Meeting 122

### Meeting Date/Time: Sep 17, 2021, 14:00 UTC

### Meeting Duration: 1 hour 30 min

### [Github Agenda](https://github.com/ethereum/pm/issues/384)

### [Video of the meeting](https://www.youtube.com/watch?v=NorHRk5fFZU)

### Moderator: Tim Beiko

### Notes: Joshua Douglas

## Decisions Made / Action items

| Decision Item | Description                                                                                                                                                                                   | Video ref                                      |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| 122.1         | Miners should update Nethermind to v1.11.2                                                                                                                                                    | [8.45](https://youtu.be/NorHRk5fFZU?t=525)     |
| 122.2         | Terminal total difficulty to be hardcoded, [exact details to be handled async](https://github.com/ethereum/consensus-specs/pull/2605)                                                         | [29.04](https://youtu.be/NorHRk5fFZU?t=1744)   |
| 122.3         | Geth dropping fast sync - users don't have to do anything.                                                                                                                                    | [40.52](https://youtu.be/NorHRk5fFZU?t=2449)   |
| 122.4         | Not include EIP-3756: Gas Limit Cap in any upgrade but spec out what the transition mechanism would look to adjust downwards and have this incase we need it in November or around the merge. | [1.00.15](https://youtu.be/NorHRk5fFZU?t=3613) |
| 122.5         | Decision to include EIP-3860 in Shanghai upgrade or not to be made on the next all core devs call.                                                                                            | [1.26.51](https://youtu.be/NorHRk5fFZU?t=5208) |

_**Note:** The first 30 seconds of the call are missing as the stream was accidently still muted._

# [Update Nethermind nodes to v1.11.2](https://youtu.be/NorHRk5fFZU?t=525)

**Marek Moraczyński**

Yeah, sure, so all the people should upgrade their Nethermind nodes v1.11.2. It was quite random that sometimes the on the previous version we can skip the validation of proof of work. And that is all. Lukasz do you want d you want to add something about it?

**Tim Beiko**

So what's the version that people should upgrade to?

**Łukasz Rozmej**

1.11.2

**Tim Beiko**

Yeah, okay, 1.11.2. Okay, awesome. Yeah, thanks for the update. So people, please upgrade. If you're running Nethermind. And in the next call, or the one after, we'll probably go into more details about the actual vulnerability itself.

# [Merge Interop Updates EIP-3675: Upgrade consensus to Proof-of-Stake](https://youtu.be/NorHRk5fFZU?t=590)

## [Engine API](https://youtu.be/NorHRk5fFZU?t=590)

**Tim Beiko**

Cool, I guess, first on the agenda. We have updates around the merge and interoperability between the different clients on the execution and consensus layer. Mikhail, do you want to just give a quick high level overview of the different updates you had?

**Mikhail Kalinin**

Yeah, sure. Thanks. We've done on the operation of this Engine API. And I think it will be published pretty soon. Probably today or early next week. Mad to think how much time do we need to do this, presume that it's ready to document? It should be straightforward right?

Okay. Cool. parts of this Engine API stuff. There is a couple of updates that I would like to share here. First, is the proposal on using the hard coded terminal total difficulty in both clients in the consensus client and in the execution client. Here is the link to the pull request ([https://github.com/ethereum/consensus-specs/pull/2605](https://github.com/ethereum/consensus-specs/pull/2605)). Again, the beacon spec, it has the link to the pull request have made to be EIP as well. And you may go there and read for the details and rationale behind this, in general as reducing the complexity and protecting us from various edge cases that could arise around implementation and usage of the dynamic terminal total difficulty that previously were had in this back.

So another thing, this is a small kind of thing is the extra data I brought back. So the deprecation of extra data fail field has been removed from the EIP. And it's been added to the execution payload. So it's back again. And yeah, the rationale here is that it's useful in investigations of various incidents on the Mainnet, as it's the default usage for the extra data is to just express the Client version, which is pretty helpful. So, what's next here? Yeah. Also, in general about the merge interop specs, I think we will have them and their versions settled down and published, in the middle of the next week, probably early next week. So stay tuned on that. Yeah, this is regarding to updates. I have also want to make one proposal here and to hear from client devs. What they're thinking about it.

This is the about message ordering. Between the consensus and execution clients, like the order of Engine API calls to be more strict. And for for the interop thing, the proposal is to like, is to use synchronous calls on the consensus client side, which means that if the call is made, the consensus client just waits for the response before moving forward with its flow of block processing or block production, or any other stuff or the factories. The reason here is that the easiest way to, to handle the message ordering stuff. And I think it's reasonable to simplify this part for the interrupt. And we can further discuss the production ready solution for this part of the protocol. And to not focus on on that just during the intro, I think it's not super important. For interrupts it's done. So that's just the proposal, what are the people think about it?

**Łukasz Rozmej**

Sorry, didn't hear that? You're mentioning changing something to synchronous which one exactly.

**Mikhail Kalinin**

The consensus client will synchronously make the Engine API calls. So it will send the request when for response, instead of like, send one request, then go to then get back to the like, usual block persist flow and send in one one and other requests without waiting for the previous one to get processed. And that could lead to the mess around the message ordering and some inconsistencies. If we don't have like a strict mechanism specified to preserve the best order of messages. And that's just a workaround for the interrupt just temporal solution to not like, get into discussion and get into justification and implementation of any message consistency mechanism. That is more sophisticated than just synchronous calls. So that's the proposal.

**Łukasz Rozmej**

Yeah, so we have this kind of asynchronousity by on the let's say, not transport layer, right, like you're saying, but on the protocol layer - prepared payload get payload gives us some kind of asynchronousity and the execute payload is then consensus validated and then remember, the last one, also validated message would be giving us asynchronicity on the protocol level, but not on transport layer level, right.

**Mikhail Kalinin**

It depends on the transport. But yeah. So we have this asynchronicity and we want to have it, but it's, like implies that we need to deal with order of messages. And it needs to be preserved. Like if you're receiving like the message about like, some payload, some child paylod or while the parents payload lot hasn't been yet processed that could be a problem.

**Łukasz Rozmej**

I'm totally for it. So when we want asynchronicity, we should just implement it in the protocol level and not on the don't rely on the transport level for that. So I'm all for it. I'm all for it.

**Tim Beiko**

Cool. Does anyone disagree with that? Oh, Danny, you kind of came on, but we didn't hear you.

**Danny Ryan**

I agree that it makes sense, like an iterative step, get it, get it right in a synchronous method and then layer asynchrony and where it makes sense.

**Mikhail Kalinin**

I also need to need to, like just let, yeah, this this will go. I mean, this requirement will be exposed in the kind of merchants are up at the stack. So, like the consensus client developers will have it there. And that's pretty much it from my side.

**Alex Beregszaszi**

Okay, and I guess yeah, I just had one question to make sure it's clear so that the decision to hardcode the terminal total difficulty it seemed like there was mostly consensus on that on Discord. But I'm curious if anyone like, feels otherwise, because I, as I understand it, the trade off is then you just need to put out like an extra release potentially, which has that that terminal total difficulty hardcoded? Is that is that right?

**Mikhail Kalinin**

I think there there is a couple of options here.

- One option is to make a release with the total difficulty hard coded, but with the some like pretty advanced value. So we're definitely sure that the merge fork on the beacon chain happens before, this total difficulty to hits on the main net.
- The other option is to have like a couple of releases. One is to clean this merge hard fork on and wait for the hard fork and then another one that just releases the clients with this total difficulty value hardcoded. That's kind of two options here. And in this in this second option, actually, the first release potentially not affects the execution clients. This is this is yet to figure out. But that might work this way. So we'll have like only one release, as we as we used to have, like with this dynamic total difficulty for the execution clients. So if it even reduces the complexity of releasing this stuff, at all, I mean, like, removing this one extra release from the execution client side.

**Tim Beiko**

Got it. Okay. And yeah, we don't need to necessarily decide that as we're making the change in the spec, basically?

**Danny Ryan**

The risk in doing one releases that you have to forecast total difficulty and a longer time period, which could be subject to attack or just high variance. I think I personally would take the hit and just do one release. Because there also is specified the manual override in the event of an attack or say terminal total difficulty just or total difficulty dropping lower and lower, or difficulty each block dropping lower and lower. So it takes a really long time. So there is a manual overhead there, which I think I prefer instead of doing two releases.

**Marius Van Der Wijden**

Have you thought about the the other way around that the miner would speed up the block times and forge the timestamp to create a higher difficulty chain?

**Danny Ryan**

We have discussed that. Is it actually practical? Can you actually spoof the network in doing so? Or would timestamps like that be rejected?

**Marius Van Der Wijden**

I think would be possible

**Dankrad Feist**

What's the problem with that? Then the merge happens a bit earlier. So?

**Marius Van Der Wijden**

if someone would mine their own chain, the separate chain with higher difficulty and then I don't know drop it on everyone. I'm not sure.

**Dankrad Feist**

It's a 51% Attack essentially.

**Mikhail Kalinin**

Won't they need bigger hashing power, to keep mining this.?

**Micah Zoltu**

Yeah, it'd be a 51% attack. And same as any other 51% attack you just sensor blocks that aren't part of your 51%.

**Danny Ryan**

There's two secrets within the beacon chain hard forks to actually update the data structures to have the allow for the payload, and it's empty. And then after that the terminal total difficulty is hit. And the execution layer payload is inserted into the beacon chain. And so the risk on an acceleration would be if they could hit terminal total difficulty prior to the actual beacon chain fork. Because then I think the fork would end up once the fork happens, the transition happened immediately and happen a past block. So there is like a little bit of an attack there.

**Micah Zoltu**

I see. The issue here is because the beacon chain does not time its fork based on the execution engines total difficulty.

**Tim Beiko**

Micah I think you're correct. Where the beacon chain upgrade is triggered by I assume epoch or slot number. And, yeah, it's not triggered by the total difficulty itself.

**Micah Zoltu**

So the real the real source of all these problems, then is the fact that the beacon chain execution chain are forking on different metrics. And those no matter what those metrics are, they there's a possibility that they will diverge. And when will happen before after the other. We need them to happen in the correct order, right? beacon chain first.

Can't we just do the beacon chain for months in advance? Like, do we need to wait until just before?

**Danny Ryan**

That's the that's the Mikhail argument of two releases. And if you I wouldn't want to do two releases in like a two week time stamp. But if we did time at such that the beacon-chain forked months before, I think that's a much more palatable to release schedule.

**Micah Zoltu**

Is there an argument against that, other than just... does the beacon chain actually two releases or just be the beacon chain releases and then two months later the execution chain releases.

**Danny Ryan**

No they both need to know the terminal total difficulty.

**Mikhail Kalinin**

Right? It should be synchronised.

**Micah Zoltu**

so the beacon chain releases, and then we decide the terminal total difficulty? And then we need to release both beacon or consensus and execution clients. Is that correct?

**Mikhail Kalinin**

Yes. We'll need this. If we follow this path, we will need a small tweak in packages back to before that. So but it's doable, complete. And this is to my understanding, in the current moment of time, I haven't like thought much about this error.

**Micah Zoltu**

Is there any reason we can't do the consensus client update or fork or whatever long, long in advance, like, let's say next week? Just just throwing it out there? Is there some reason that we need to do it some kind of near the actual proof of stake switch? Or can we do it anytime prior?

I think it just makes the timeline is longer, right? That would be the only reason like if you have to wait two months, then that's two months extra to the merge.

Yeah, sure. But I'm saying like we could, can we just do the consensus client update now like whatever the next patch goes out?

**Dankrad Feist**

The blocker is like setting on one spec that we're all happy with, like, if you do it now, then in two months, you might come up with some changes in like, oh, now it's too late.

**Alex Beregszaszi**

I'd want to be much deeper in the engineering cycle before we would release on the beacon chain in production.

**Micah Zoltu**

Just to make sure I understand here the when this consensus client goes out, that is the start of the merge. But there is not any sort of time constraint between between when this new consensus client goes out, and when the execution client eventually goes out. And when hard fork happens. That duration can be whatever we want, it just needs to be an order that right?

**Mikhail Kalinin**

Both software's should be tested with each other, like with the most recent version of each other before making this release.

**Tim Beiko**

In the next couple months, as we're working on this, it probably makes sense that maybe default to hard coding the total difficulty because it'll be mostly on devnets, and whatnot. As we're further down with the spec, and we start actually thinking about how to release this on Mainnet, I feel like we'll have a much more context about it, once we've actually like, implemented it in the in the happy path.

**Micah Zoltu**

So I agree that we shouldn't hold up definites for this, but at the same time, I think we do want to test the production code paths, as soon and early as possible. Like, I don't want to wait until the last minute to change the way we do our releases, and then have like, you know, it's only run on Goerli, every test net will see this mechanism for hard forking.

**Dankrad Feist**

I don't understand, why are we talking about like, one month to like, change a single number in the execution plans? Yeah, I agree, like cutting a new release is something difficult, but not if it if the change is literally just a single number, like, you know exactly what you're gonna release?

**Tim Beiko**

Yeah, it's not the it's not the time to do the release. Obviously, that can be done in, you know, a day or two, it's getting everybody to upgrade to the release. I do think if we wanted to go the two release route we can get around that where we tell people like, you know, first release is out on that date x second release is out on date y. So they know that they should be expecting two releases. But there's just a risk that like, yeah, every time we do releases, people don't upgrade, and they don't get the memo. And if there's two of them, you know, there's just the risk that like they've updated the first one, and they're not aware that they need to upgrade again. But I don't think it's any, it's not a technical barrier.

**Dankrad Feist**

But even that, if you're if you have made it very clear, hey, in the next week, there will be a release that, like you need to instal, then what's really the percentage of people who don't get that? And should they really be maintaining failure modes?

**Tim Beiko**

Just to give a recent example, geth basically did that a few weeks ago, and two major mining pools had not upgraded, right.

**Dankrad Feist**

Luckily, luckily, it doesn't matter if the mining pools don't do it.

**Danny Ryan**

I look i i agree Dankrad, that it might be the most palatable solution, and you can orchestrate and make sure you communicate well, but it's definitely a consideration. And I also think that we don't necessarily need to decide right now. We can spend a little bit of time over the next few days to think through whether the dynamic setting of terminal total difficulty can be done actually in a trackable way, there was an issue that emerged that kind of highlighted, there might be a number of corner cases here so we can think through it and try to make sure that we definitely want to scrap it by mid next week. And then if so, then we're kind of working with the static, which I think is also solves a couple of other problems.

**Micah Zoltu**

What problems does static total difficulty solve?

**Alex Beregszaszi**

Dankrad brought this up on allcoredevs two weeks ago. If a user naively runs an execution engine and doesn't connect the beacon node, and it was relying on being told from the beacon node, the termina total difficulty and never connected to one, then it would literally just follow the proof of work chain forever and not like not following the transition would not show up as a failure to them, even if they wanted to be following the transition. Whereas if there was a terminal total difficulty released in the execution engine, then they would see essentially a failure at the point of the transition and not see any new blocks, that would be essentially an alert that something's wrong. And then they'd figure out that they need to run their beacon node. That's the primary thing it solves other than some of the corner cases with sync we identified a couple days ago.

**Micah Zoltu**

Didn't we come up with an alternative potential solution where we set the execution client such that if you are not connected to a consensus client by this difficulty, then shut down? And and just that just means you must be connected to the network? Basically?

**Mikhail Kalinin**

Yeah, there is. Also some other some other, like, details and implications of these dynamic total difficulty stuff. So they're just exposed in the issue. I mean, they're just described in detail, so you can drop the link.

**Micah Zoltu**

Yes, if someone could drop a link, that'd be great. I'm just it at the moment. It sounds like dynamical total difficulty is the better option. And I'd like to better understand what the arguments against or sounds like there are someone I don't understand them.

**Alex Beregszaszi**

Yeah, I would, I would suggest we take it to that issue and move on.

**Tim Beiko**

Mikhail already linked it in the chat. So [this pr 2605 on, on the consensus specs](https://github.com/ethereum/consensus-specs/issues/2605), and that links to another issue as part of its rationale. [Yeah. Oh, and then there's also pr 2603](https://github.com/ethereum/consensus-specs/issues/2603). Oh, I guess anything else on this specific topic?

**Diederik Loerakker**

I open this issue on the consent specs repository about transaction typing. So the API and the execution layer, don't change, but within the consensus spec. There's something we can change to be more compatible in the future. There's new transaction types. So if you're interested in typing them, just have a look.

**Tim Beiko**

Cool. And that's [issue 2608 in the consensus specs](https://github.com/ethereum/consensus-specs/issues/2608).

And then there was something that Trent put in the chat before we started. I think this is from Paul from lighthouse. If, if that's correct, but he was wondering if there's any execution team that already has the latest API's implemented? Yeah. Basically, the Engine API spec.

**Marius Van Der Wijden**

I have created an interface for it. And I started writing the code for it, but we haven't implemented it in Geth yet. And also, there were some questions regarding the interface that we already, like talked about when I implemented it.

**Tim Beiko**

Okay. Anyone else have an update?

**Gary Schulte**

About the same for Besu. We have the latest spec stubbed out for the moment. We're working on the implementation. We're not ready.

**Marek Moraczyński**

Nethermind not ready - we started working on interfaces. But I think we have a good progress.

**Mikhail Kalinin**

Just wanted to repeat that. Stay tuned. We'll just publish the spec very soon for this Engine API. It'll be different to the design doc. Some stuff some details. But in general, it's the same.

**Tim Beiko**

Yeah. We'll share that in all core devs and maybe in the announcement channels as well, on the r&d discord for people to follow next week.

And anything else on the merge before we move on?

## [Sync process](https://youtu.be/NorHRk5fFZU?t=2294)

**Mikhail Kalinin**

I wanted to discuss sync.

**Tim Beiko**

Oh, did you have a specific question, or is it just asking where the teams are at?

**Mikhail Kalinin**

I was like, yeah, this is an agenda. Sure. I was just looking to get any updates on the specs documentation on this draft design proposal. Felix?

**Tim Beiko**

Felix is not on the call, I saw on discord that he was working on updates to the document, but I haven't seen anything published yet.

**Marius Van Der Wijden**

Oh, yeah. So he had some dentistry going on. And so he wasn't really able to work this week. He's going to finish it next week.

**Mikhail Kalinin**

Is there plans with the client developers to implement the sync for the interop? And you have capacities for that? Like, who is planning to do this?

**Martin Holst Swende**

So from Geth's perspective the feature is implemented. But in order to do it, he is doing some major refactorings that are needed. Before you can really get started on the new stuff. Marius do you have the same the same impression?

**Marius Van Der Wijden**

Yeah, so we need to implement some stuff before we can start that. And But Peter is doing that. I'm not sure if we, if we can actually make it until the merge until, until the interop. But we should until the merge, probably. But until the interop, but we should have at least some some beta version that we can try.

**Alex Beregszaszi**

Maybe at the beginning of October. There will be enough r&d done that we can make better decisions about communication protocols, and that kind of stuff at that point.

**Tim Beiko**

And I guess one thing that's just worth mentioning, I saw Peter say this week is as part as these refractors within Geth, to support kind of merge sync. Fast sync is being dropped. So if you're a guest user running fast, I think you should probably switch to snap sync going forward. I don't know Marius, or Martin, if that's roughly right.

**Martin Holst Swende**

Well, there's nothing really from a user perspective that you need to do.

**Tim Beiko**

Okay, it'll just stop being available.

**Martin Holst Swende**

Yeah. I mean, at some point, there will be no node that sir, Geth node data on the network, and it used an old Geth person, I think you're gonna be start at some point in the future

**Łukasz Rozmej**

by dropping fast sync, do you mean dropping get node data? That would affect Nethermind ability to sync somewhat because we are still using that.

**Mikhail Kalinin**

So if we don't have concrete PR. It's more of something that has been checked around a bit. And yeah, sooner or later, it's going to be dropped.

It's been in the wind for a long time. But at some point, there's gonna be a dropped.

**Łukasz Rozmej**

There, it sounds like it's understandable that it's not scaling extremely well. So we are planning either to implement snap sync or either to go move to more like Erigon style. I'm more in favour implementing snap sync, but with everything going on with the merge, etc we haven't managed to do that yet.

**Tim Beiko**

Yeah, so please keep an eye out for the announcements of that, yeah, every client, and I guess infrastructure, or users should be moving away from fast sync at the very least.

**Marius Van Der Wijden**

And just for the people listening in, snap sync is way faster than fast sync is way faster and takes way less bandwidth. And it's in all aspects superior to it, except in name.

**Tim Beiko**

Cool. Anything else on the merge?

**Guillaume Ballet**

Just a quick question for Martin, do you know if we have merged Gary's PR about the transition process? Because that's going to be necessary too.

**Mikhail Kalinin**

I don't know, sorry.

**Guillaume Ballet**

Okay, well, we need to find out.

# **[Proposal to include EIP-3756: Gas Limit Cap](https://youtu.be/NorHRk5fFZU?t=2657)**

**Tim Beiko**

Next up, like client wanted to give an update on EIP-3756. So the gas limit cap. Yeah, but right.

**Matt Garnett**

Can you hear me? Okay?

**Tim Beiko**

Yes.

**Matt Garnett**

Yeah, we presented this, the last allcoredevs didn't have a lot of time to discuss it. So just to briefly reiterate, the gas limit cap is motivated by putting an upper bound on what the gas limits can be set to by block proposers. In the benign case, high gas limits can increase the size of the state industry faster, we can sustain the malicious case it amplifies attacks on clients. In the past, this hasn't really been a significant issue, because miners have worked pretty diligently with allcoredevs to set gas limits. But they've shown in the last few months that they are potentially willing to be incentivized to increase limits beyond what may be considered safe. So this is a EIP proposal to set an upper bound on that limit. Sir, any feedback on this?

**Mikhail Kalinin**

Well, I know there are some people who are heavily opposed to this. Yeah, so I'd like to hear the cons. From those people or general thoughts.

**Micah Zoltu**

I can give the cons the primary one is that it means that all core devs will have to actually come to consensus on a gas limit - the upper bound. Previously, we have kind of able to shrug off having to make that decision. If we make this change, we will now have to officially make that decision as a group. And the that then leads to we need to then decide what is an acceptable rate of state growth, and there is a huge amount of diversity amongst client devs for what is reasonable in terms of state growth. And there's also, you know, disagreement on just execution time per block. what's reasonable there? So I think the the biggest con here is that we will be taking something that currently we can kind of ignore, or at least have plausible deniability of. And we're then turning it into something that now we have to actually talk about and agree on, and a very, very hard decision.

**Dankrad Feist**

Well, I think actually that all core devs would be fine at making the decision, my concern would be that takes much longer, like how long does a reason, like take from an all core devs decision like? Will it take an EIP every time, which takes what at least half a year or something?

**Micah Zoltu**

Yeah, so when we want to change, increase it, we wouldn't do any if if this EIP passes, and we want to presumably would have some default, I'm guessing 30 million is reasonable default. If we want to then change it later to something bigger, so 45 million or whatever, then we would need to have any EIP and then wait for the next hard fork can get included in hard fork.

**Dankrad Feist**

I think that was an idea to make it automatically increase according to Moore's law or something like that. I think that would be a better idea.

**Martin Holst Swende**

My question is basically, is this EIP? Is the motivation for it is that we think that before the merge, miners are going to be like, not have the long view on Ethereum. Let's just say YOLO and in the last time they have? Or is the is the is the motivation more longer than that? Do you think that even in the future when we're up to the merge, if it's going to be needed, or wanted or desirable,

**Alex Beregszaszi**

I think that if those tokenomics work, and that the hype around collecting tokens is around when staking is around that stakers could easily be motivated as well, to abuse the limit. There's maybe a bit of counteraction there because they have a longer term view. But I think a lot of them have machines that can easily run 40 million instead of 30 million, and would do so at the cost of others. But I can't speak for all the stakers, but I think the the incentives are still there, even if you have, you know, a four year time horizon instead of a one. But I think that's because they don't know all of the issues.

**Micah Zoltu**

So I think even with the if the incentives were aligned, we still have the problem of education, where the people who are stakers aren't necessarily the same people who have a very, very deep understanding of the pros and cons of higher gas limits. Everybody, most people I talked to who are not core devs seem to and even a lot of core devs have a belief that, you know, state growth is not a problem. Yet, you know, there are definitely core devs mean me very much included, who believe state growth is a major problem. Even if they're altruistic, it doesn't mean they're well informed. And so if we do decide to go that route we would need to make sure we have some mechanism of ensuring those people are in fact well informed and educating them, which is, again, a hard problem. Like I think all the options here are hard problems.

To answer Martin's question though, I do think that whatever rule we applied to miners, we should probably similarly apply to stakers. I think their incentive structures are similar, there is slightly longer time horizon, as Danny mentioned, but it's not that much longer, like the state growth problem some aspects of the state growth problem are on time prizes that are, you know, multi years. And if you take out in three months, then you might not care about the state of Ethereum three years. Whereas if you just let block state growth grow indefinitely, and we don't mitigate it effectively, you know, three years, maybe when we really start paying for it.

**Ansgar Dietrichs**

Yeah, just wanted to briefly point out that with this EIP, I think this there would be like a lot of room in how to use it. So because like say we said we set the upper limit at 30 million, that was actually basically be a recommendation of like, going with 30 million unless we have technical issues where we temporarily reduce it to something. One alternative could also to be today set at say say 40 million 50 million somebody that way, like, we don't recommend people to actually go that far. But it's like, this is the limit where we still consider the network, technically safe or something. Right. And in that circumstance where we usually expect not to be at the limit, this kind of change would be much less invasive, while still giving like at least some other bounce. So there's no limitless, like, potential for catastrophe.

**Tim Beiko**

Right, and then it becomes more of a communication, then technical challenge, right, like saying, we allow 40 million, but please don't use 40 million.

**Micah Zoltu**

I think as a kind of shelling point 30 million is a reasonable start. But I just just to give everybody a fair warning. I will argue to lower from that. I personally think the 30 million is too high for a number of reasons.

**Alex Beregszaszi**

I have a question is there any update on the usage of EGL? Has there been voting has there been movement?

**Matt Garnett**

I haven't followed the voting as much. But I've looked at the mining pools that are still using it, it looks like two smaller pools are still sweeping rewards Flexpool and B-pool. F2Pool was doing it in the beginning. And it looks like they didn't sweep rewards for a pretty long time. But I saw that they did sweep rewards a few days ago. So it's not clear exactly what their involvement still is. But there are two small mining pools that are actively sweeping rewards.

**Tim Beiko**

And another I guess thing that's worth mentioning is the gas limit is still 30 million. Right. Yeah, so. So yeah, it's it's not currently being pushed upwards. But obviously, that could that could change.

**Matt Garnett**

Is anyone from Erigon on the call?

**Andrew Ashikhmin**

Yeah, it's me, Andrew. Well, I think our position is the same as before that we are not in favour of this EIP. But if like the majority decides that we are going through with this EIP then we are not going to fight, and we're not going to die on that hill.

Another question that would be is, like, if we were to move forward with this EIP would the plan be basically have it ready for the future for after the merge, or what the plan B to basically bundle the merge with basically, as like the one exception to the rule of not having features, as part of the merge, just so in case we need it earlier, it were already be implemented and ready for like a short notice emergency fork. I mean, again, with the understanding that he probably wouldn't do that unless it would start being a problem.

**Matt Garnett**

I think the question is more, Are we trying to put it in Shanghai? Or we try and do a soft fork before Shanghai?

**Alex Beregszaszi**

Right. And knowing we also need to upgrade in December because of the difficulty Bob? Right. Yeah. Marius, you have your hand up?

**Marius Van Der Wijden**

Yeah, I would, I would oppose moving this into Shanghai or like the next fork. Just because I think we should really keep the focus as clean as possible. And if we were to include a new EIP, it has to be like a hard consensus critical EIP and don't think that this EIP is security critical enough to do that. So I'm in favour of the EIP, but I would want to have the fork in November be as small as possible. And if we were to need something that it would need to be security critical at this point. And not something that may be introduced in the future or something?

**Tim Beiko**

I guess on that note, like, it might be helpful to understand from client devs. Like, how, how much work would it be to activate this as a soft fork. So say that, you know, two weeks from now we have a call and the block limit is at you know, 40 million because either because of miners moving it up or EGL moving it up or whatever other reason. And it's felt that that's unsafe, and how, given this is like a minimal change, how quickly can you know this be deployed? Is it a matter of like weeks?

**Martin Holst Swende**

So how do you mean deploying it as a soft fork?

**Alex Beregszaszi**

you still need to coordinate and get everyone to upgrade and especially because if if you picked 100 million, and you know, we were nowhere near it, maybe you could argue doing a soft fork and it just like takes time for ripple out. But you would still need to coordinate like it's a hard fork in my opinion.

**Matt Garnett**

The only benefit is I don't think you have to coordinate all of the user clients. It's more the hashing power, right?

**Alex Beregszaszi**

One of the user clients or the the power against the hashing power and software.

**Dankrad Feist**

The hashing power might not want the fork, so you need to users to upgrade to enforce it.

**Alex Beregszaszi**

Like users, exchanges, etc.

We have the fork in November, then we have the merge. Is this something that would be easy to like? How much lead time? Would we need to add this to the November fork? If we wanted to, right, like, is this something basically, is this something to deploy across all of the testnets?

**Martin Holst Swende**

Yeah. It's pretty trivial change. Yes, that was what you were getting at? That's a simple thing.

**Tim Beiko**

Following off, Marius, his comments around, you know, keeping the the merge as lean as possible? Is this something that we can have a spec for? That's kind of ready to implement? And if we see an issue, we can combine it with either, basically the november fork or the merge?

**Mikhail Kalinin**

Yeah, we can have in the back pocket, if we have to, and not otherwise, schedule it as part of Shanghai. That's possible.

**Alex Beregszaszi**

I do want to mention, and I apologise if this actually in the in the spec there. But I think it's implied to me that it wasn't because software. If the gas limit on Mainnet is already above the target that we'd want to select that you would actually need some sort of hard fork to discreetly change it to that point, is that already coverd in the EIP? apologise if it is? It's not?

**Dankrad Feist**

Could also makethe soft fork so that it only accepts down votes when the limit is currently above. So that would be a soft fork.

**Tim Beiko**

But yeah, I do think that would be worth specking. Kind of in advance.

**Alex Beregszaszi**

Yeah. If we want to keep in our back pocket as a reaction to an attack, and then we need to have what the reaction is because we have to assume that it's going to be above our target already.

**Tim Beiko**

So I guess this that generally makes sense to everyone, as a next step, not kind of, you know, include this in any upgrade right now spec out what the transition mechanism would look like they adjusted downward. And yeah, have this in case we need it either in November or around the merge.

**Matt Garnett**

I didn't quite understand the exact argument against bundling this in Shanghai.

**Alex Beregszaszi**

I think there's not a lot of consensus. I think people feel a bit mixed about it.

**Tim Beiko**

As I understand it, there is wanting to keep the shangai, you know, lean, wanting, like, I guess some core devs obviously, being opposed to it, and needing to come up with an actual value for it, which I guess we could default to 30 million. But yeah, those seem to be like the three issues.

**Matt Garnett**

Yeah. My views, there's never really a good time exactly, to do some of these things. And if we don't do it in Shanghai, it's already a simple change. There's not anything in Shanghai already. We're not going to do it during the merge are likely not going to do it after the merge, because there's a lot of other things to do. And so then it's going to be sitting around for a while, and the attack vector isn't going away. It's not clear how important it is for the security of the chain. But from my point of view, it seems like Shanghai is a good time to do it.

**Tim Beiko**

Right? Um, yeah, I guess one thing I don't like I know there's also other kind of EIPs on the agenda today that people wanted to discuss for Shanghai and yeah, it does kind of feel like we had this consensus earlier to only focus on the merge at the moment until we have devnets up for the merge and you know, we're far enough in the implementations and then kind of make decisions around what we do in November based on on how much bandwidth we have. So I think that the big concern I have is that it kind of sets a precedent where we move away from just being focused on the merge to starting to work on this and potentially other things. When we don't yet have the merge or devnets set-uup, and we don't have a good feel for, like, how much work is left to do on that? Yeah, I don't know what other client teams or developers think? What are your thoughts?

**Mikhail Kalinin**

Yeah, I kind of agree I, I mostly want to focus on the merge now, and not have as much other features.

**Tim Beiko**

The exception to that would be if we do see the gas limit being raised to like, levels we consider unsafe on Mainnet, having this already speced out it would basically increase the the urgency that we need this with having it already speced out to be valuable. But assuming the kind of urgency for it stays the same, it seems like it, it just might be better to focus on the merge exclusively until we're at least farther along with the implementation of it.

**Micah Zoltu**

This, it feels like if we want to go down that path, we then need to come to some sort of agreement on what a dangerous level is. I believe there are some core devs who believe 30 million is a dangerous level already. Due to some known EOS vectors against certain clients. Like is 31 million safe? 39? 45? Like, like, if we say, if people reached dangerous levels, then we will do an emergency fork. That means we need to define an advanced I believe what an emergency or what they dangerous level is, and so we still have to solve that part of the problem, even if we go down this path. Unless we're just saying if the miners raise it above 30 million, then we emergency fork.

**Tim Beiko**

It seems to me like that's kind of the implicit consensus already. We're like, we have this limit. And we sort of agreed to it around London. But yeah, I'm curious what, what others think?

**Mikhail Kalinin**

If we if our stance is this, this gives us problems, then we might have to roll up. I don't think we need to define it. [inaudible] Yeah. If you're thinking about that, it would be [inaudible].

**Tim Beiko**

your mic, I think. Yeah, it was was not great. Martin. I think what I got was that we can't really define like a specific number now that if this becomes a problem in the future, we can we can have a fork for it. I don't know. f you want to maybe fix your mic. It was a bit low there.

**Mikhail Kalinin**

Oh, sorry. Well, from a denial of service perspective. I don't think we need to pre define what would be a problem or how a problem would look like because we would notice if we become bitten by it. But from a state growth perspective, is that is the concern. Then I'm not sure. Yeah, exactly that how to define what are dangerous levels of state growth and what are okay levels of state growth.

**Tim Beiko**

Ansgar?

**Ansgar Dietrichs**

Yeah, I'd personally be in favour of at least stating clearly that we consider participation in EGL to raise the gas limit illegitimate. And like, even if we wouldn't immediately act, right, because there's definitely some room above 30 million where it wouldn't immediately become problematic in any sense. But, but just because this is like the slippery, slippery slope situation where maybe 32 million is still okay for state growth and maybe 33 is, but maybe 34 isn't or something. Like, just because if we set no ambivalence, I think a lot of miners will be much more interested in the future to kind of be involved there. And so I think, at least basically stating very clearly that we would very much expect them to not participate in that race to raise it above 30 million. And if they do, we basically will likely do something about it, even if like, there's probably some room where if it's only a little bit, we might just not bother to look into it or something. But I feel like if we if we basically sit now that there is some some room before we would act then that best implicitly just like making an endorsement, I think, in a sense. So I think that's the interest.

**Tim Beiko**

I'm fine, plus one-ing that. I don't know that others, like I don't want to speak on behalf of everyone.

**Matt Garnett**

I'm fine. Moving on to the next things in the call. I'm still of the mindset that I would like to see it in Shanghai, but I understand it seems like that's the minority view.

# [Proposal to add EIP-3855 (PUSH0 instruction) into Shanghai](https://youtu.be/NorHRk5fFZU?t=4192)

**Tim Beiko**

Any other thoughts? Okay. And, Alex had two EIPS that he wanted to discuss. One is EIP-3855 (Push0 instruction). And then the other one is EIP-3680 (limit and metre initcode). Alex, you want to give a quick overview of them?

**Alex Beregszaszi**

Yeah, yeah, I will give an overview of the push zero and the Pawel about the init code. So the push zero is a very simple one, it just introduces a new instruction, which pushes the constant zero onto the stack. And this is specified in a way that it can actually be implemented in the same place where the rest of the pushes are implemented. Because most of the the EVMs implement it such that they just have the starting opcode and in the current opcode, and they just subtract it. So they know how many bytes to read. And in case of push zero, they don't need to read anything. So that's on the technical side. And then regarding the motivation, I think the EIP does a pretty good job explaining the motivation, and I will try to replicate it here, but probably won't be as good as what we put into writing. But basically, there are a lot of cases where someone needs to push zero on to the stack. A good example, is calls. Since return data has been introduced quite a few years ago many of the calls would just end up with at least two zeros at the very end, which would be the pointer in size for the return memory. And because people are not using that anymore, they'd rather use the explicit return data opcode to retrieve the data. So that's one good example to see where the zeros are used, but many more cases and the problem we have seen - so we have been motivated by looking at actual byte code on the network as well as talking to solidity and some challenges they face in this regard. So basically, pushing zero can be done or at least can be done in many different ways. One we use just with the push instruction which means that is two bytes, and it costs three gas. But one can can also use a dupe if in case it was already understand that that also cost three gas. And these are like the clean and nice ways to do it. But people are always looking out to save gas. So there are certain other instructions, which in certain cases can return zero. So one example is return data size in case there has been no return data, it will be zero, call this call data size the same and plenty of others, that are listed in the EIP. So in many cases, contracts, and people start to use these just in order to save gas, because some of these only cost to gas at runtime and they're only one bite, and so they're cheaper to deploy. And the one problem we have seen with this is, this kind of puts us in a position that certain changes would be harder to do. One example was the transaction packages, which would change the behaviour of return data size. So that's one reason why this is this optimization is like a bad direction for many people to go. And the other the reason is, is what's happening in solidity, the team is looking for it. I like that the new code generator to to have like a nice way to to push like unknown value in the cheapest possible way. And they don't really want to go to the extent to try to use these other instructions. And then lastly, we also did an analysis on how much gas has been wasted on tests. And we only looked at all the bytecode deployed, and how many push one zero instructions they had. So which is like the 60 - 00 in hex. And according to that, it seems that I think like 60 billion gas, just check it quickly. Yeah, 68 billion on a gas has been wasted so far, on deploying such code. So that's the long motivation.

**Tim Beiko**

That's a lot of gas. Does anyone have thoughts or comments on this?

**Martin Holst Swende**

Cute EIP. I mean, like a lot of these EIPs that touch something about the EVM. It's nice. and not terribly difficult to implement but is neither is screamingly important. So yeah, I'm kind of in favour of it, but I'm not widely in favour. Lukewarm.

**Matt Garnett**

I feel like this is hard, because there's lots of small changes that slowly improve the EVM. And none of them are necessary screaming, this needs to immediately go in. And so how do we at a higher level, drive the protocol to improve in EVM?

**Tim Beiko**

Right, I think this is the higher level conversation where we have these things like say, the merge, which is obviously very important. And after the merge, there's going to be other pretty important things to do in the protocol. It does feel like we have like a pretty strong consensus about not doing any, any changes before the merge. But yeah, I think, not necessarily today, but we need to figure out how do we keep making these improvements to the EVM and you know, this is not the only one there's, you know, Alex has proposed the EIP-3540, which was very popular, there's been EIP-3074, which also had like a lot of community support.

**Martin Holst Swende**

But in the end, I mean, I'm, I'm in favour of it wouldn't mind including this in a future fork. as it's so easy to implement and easy to test. There are no corner cases to screw up on.

**Dankrad Feist**

The marginal value of this field is very low. Like I'm really surprised somehow, like, just reserving even one opcode for the seems, seems a lot just to save one byte.

**Tim Beiko**

Andrew?

**Andrew Ashikhmin**

So from my point of view, I'm in favour of this. I have a suggestion, maybe when we can create tentatively a placeholder for the Hard Fork of the merge so and we can tentatively approve EIPs that can go into the next post merge fork?

**Tim Beiko**

Right, I think that generally makes sense. It feels like it's maybe a bit early for that, just because we're again, like at the very beginning of implementing the merge. But I don't know, I, I do agree that like, when we're going to start having the merge implemented, it makes sense to look at what's after. And we already have like a pretty long list of proposals. I mentioned a couple and they're all I've like, purposely left them all open in the Ethereum Pm repo. So we have like a pretty long list of ones that basically are last for Shanghai. And I think we have consensus like, assuming, you know, what's the fork in November to move back the difficulty bomb is called Shanghai. It seems like we don't want to add any other features to that. But we have a lot of features that like are valuable, that we want to do after the merge. Yeah, I'm just not sure what's like the right time to start discussing that. It feels like it's probably a bit early. But we probably don't want to, to wait super long either.

And I guess, Alex, to give a quick summary, because you dropped off, it seems like people are like, you know, weakly in favour of the proposal. It seems like, we don't want to do it before the merge. And it seems like there's also a desire to start thinking more deeply about what we want to do after the merge given this and all the other proposals that are pending anything else on this EIP?

Okay, the next one then was EIP-3860.

## [Proposal to include EIP-3860 (Limit and meter initcode) into Shanghai](https://youtu.be/NorHRk5fFZU?t=4804)

**Pawel Bylica**

Hi, yeah, Pawel here, I should take care of this one. So this EIP adds some limits to the init code size and additional cost to it. And so the quick background, before the EVM can execute any code, it needs to do jumpdest-analysis of the code. And its cost of this analysis is not directly reflected anywhere. This is partly limited by by two factors. First one the call or create cost is quite high. So, the kind of limits the attack vector and also deployed code has size limit. So analysis of the deployed code is at least capped by this limit. And for init code, there's no limit. So this is unbounded and the sizes can be in megabytes and in practice, meaning like attacking scenarios. So, previously, there was like a previous version of this this concept EIP-2677, which only introduces the size limit for init code. And at some point, we realised that currently there is the precedence for for charging conditional gas for initcode size, which is related to the the requirement of hashing the initcode, and we want to include the similar mechanism for initcode in general. So this gap proposes charging two gas per initcode word size, for reference, create two already charges, six gas for that. So that would be increased to eight and for create, like kreger create, the cost should be two. And the cost were taken from from the performance of current Geth implementation of the jumpdest-analysis. In our opinion is quite low. So yeah, that's that's mostly the the description of the EIP.

**Tim Beiko**

Thanks. Oh, Martin?

**Martin Holst Swende**

I'm one of the co authors so I'm obviously in favour. But what I wanted to add was I've been basically wanting to have something like this for a number of years. That's why I wrote the limitation of the initcode EIP earlier. That one is a bit of a hack. And I think it's not great. This is more rigorous attach that adds a linear cost, which we are, which is proper, because it is, I think it is currently a denial of service factor against Ethereum which we should fix. And we should have fixed a couple years ago. But yeah, we're here now. That's it.

**Tim Beiko**

Thanks for sharing. And of course, anyone else have thoughts on this?

**Diederik Loerakker**

No, it's might actually relate to the merge, where in the merge, we have this consensus type to describe a transaction, which as have maximum size. So I suppose that you just want this kind of bounds on transactions as well as initcodes in internal transactions. And basically, if you have like a proper balance.

**Tim Beiko**

Right, so I guess I don't know, Martin and Pawel - are you proposing this should be coupled with the merge?

**Pawel Bylica**

Firstly, I want to confirm t I think it should work more or less the same. So there might be some coordination, if that's required. It's also the EIP also applies the cap on the transaction, if I recall correctly, and for internal calls. And in terms of when it should happen, I actually don't have strong opinions about that. I don't think it's my job to decide this, but I think I will leave to others.

**Tim Beiko**

And yeah, Does anyone else have thoughts on this? Marius, I see you're off mute. Did you want to add some there?

**Marius Van Der Wijden**

Yeah, I'm probably a bit unfair, because I'm also in the Geth team. But I would also like to have this in as soon as possible. One thing we might need to look at is the increase in gas costs to two gas. I know that some some clients are way worse in the jumpdest-analysis. So it might make sense to increase the gas cost even more. But I think the limitation of initcode size is a no brainer for me. I think that should go in either way. And the gas costs increase should go in too.

**Tim Beiko**

so I guess it it does seem like I don't know the Geth team given I guess Martin is an author and the authors are like most familiar with this. Does it make sense to just kind of give everybody two weeks to familiarise themselves with this and see what all the client teams thoughts are about including this alongside the merge. I did like the idea of like, not having a precedent that we don't accept something into an upgrade on the same call as proposed just to make sure people have time. Yeah, exit you have your hand up.

**Alex Beregszaszi**

I was wondering why why should this go in with the merchant and maybe not before? So like in Shanghai just to reduce the scope of the merge.

**Tim Beiko**

Oh, good point. I guess one reason I can think of an please let me know if this is wrong is if we include this in the merge, we're gonna have testnets for the merge. Regardless, if Shanghai is just the difficulty bomb pushback, we don't need to deploy that across all the testnets. So that's one reason I can think of. But there might be others. I guess there's a comment by lightclient about adding EIP-3680 is bigger than obviously the two other EIPS we discussed. I guess, from what I'm getting is like the Geth team feels there's like a kind of security risk. And proto mentioned, there might be just the better interaction with how the beacon chain is already set up. Yeah. So that's seems to be the rationale.

**Matt Garnett**

I guess my understanding of the pushback against the other two simpler EIPs is that if we wanted to have Shanghai not have any features, The initial energy required to have other features in the fork was great enough to not include these, like relatively simple EIPs. But if people want to do EIP-3860, then there has to be effort put into building out the tests, then it seems like the marginal cost of also adding one or two of these other EIPs is incredibly small, because the decision has already been made have features into the fork. Is that a misunderstanding?

**Tim Beiko**

But are you referring to Shanghai?

**Matt Garnett**

Shanghai or the merge? I am personally fairly opposed to including anything in the merge doesn't need to absolutely go in. But I'm specifically curious about Shanghai.

**Marius Van Der Wijden**

I would also be opposed to putting this in the merge. I was thinking about Shanghai for for this.

**Tim Beiko**

Got it. Sorry. So I got that wrong. I do think that case, yeah, your argument is probably good lightclient were like, yeah, it if we are going to set up infrastructure for Shanghai with this, then it basically becomes a proper feature fork and we need testing and we need to deploy across the testnets and whatnot, then that's. Yeah, that's like a much bigger overhead.

**Matt Garnett**

Is that other people's understanding?

**Tim Beiko**

Oh, Alex,

**Alex Beregszaszi**

Are you saying that for the difficulty bomb, you wouldn't even set up a testnet, just launch it as it is?

**Tim Beiko**

I think that's what we did in the past. But I might be wrong there. But I think from your glaciar, we did set up a test net, right? Because none of the testnets have difficulty bombs. So we obviously we would add reference tests, but I don't think we would spin up a testnet.

**Martin Holst Swende**

They don't have proof of work.

**Tim Beiko**

Yeah, so I think this is kind of the big difference is if we just push back the difficulty bomb, it's something we can only release for Mainnet and literally not have an upgrade on testnets. And then if we do have anything else we need to be on the testnets. And that also implies that kind of the work has to be done much sooner. Because say we wanted to fork mainnet mid November with the difficulty bomb. That means like at least a month before, ideally, we fork the testnet. So that's like mid October. And that basically means you want releases out you would want releases out for clients in like two weeks, like early October. And that just seems kind of unrealistic timewise. So I'm not sure I don't know I I struggled to see how we would put anything in Shanghai at this point, which is not, which has to go through a full testnet deployment. And one thing I can do in the next two weeks is I can just double check the difficulty bomb calculations and whatnot to see if anything has changed. But as I understand it, it's supposed to go off, you know, early December. And I think no one wanted to fork like around the holidays. So it's like, yeah, as I understand it today, kind of the latest we could have a mainnet upgrade is December. That means, November is the latest we're done with with, with testnets. And that means on October, we basically need fully tested releases out. And that's two weeks from now.

**Matt Garnett**

Are people strongly in favour of trying to EIP-3860 in Shanghai?

**Martin Holst Swende**

I wouldn't wouldn't be strongly favour, including this. Wouldn't be curious to hear from these and other mine what they feel about the code.

**Łukasz Rozmej**

And so Nethermind recently optimised it a bit, looking at the Geth code. I would say we are in case of vulnerabilities more, more or less at the same level, of course, there's some maybe runtime overhead or something but generally, I agree that this probably needs to be done. But I wasn't the one doing the analysis. So I don't have that strong of an opinion.

**Tim Beiko**

Any other thoughts?

**Marius Van Der Wijden**

I would, I would say, it's crucially important to do this. And not only because of the current clients, but also because of some other clients.

**Matt Garnett**

What is the timeline look like to make this happen, then if we want to do this in Shanghai?

**Tim Beiko**

I think we would need to be like 100% in agreement on the next call. And that's like the absolute latest we could do it. I can kind of I could look into what like with the difficulty bomb and whatnot, what it would look like. But yeah, that's my understanding is we can't really go past next call to make a decision on that, because then it'll be mid October. And that just seems way too late.

**Matt Garnett**

Is it possible to make a decision now? Or do we really want to wait? All right, you know, make a decision in one week rather than two? Right.

**Marius Van Der Wijden**

I don't think we should make a decision now. I think that's too early and set a precedent. I think every client team that wants it that's in favour of it should implement it until next week, and then maybe have some discussions over the all coredev channel or something. I don't really want to have another recorded meeting next week. Because I think it's also bad if we have them every week.

**Tim Beiko**

Yeah, and I think the fact that these proposals are also kind of new, I'd be I'm like less inclined to have like an off schedule meeting where we just put them in and yeah, I do think like people watch these calls. They read the notes, the notes take a couple days to come out. So I think there's value in like discussing yet on the discord over next few weeks. But and yeah, teams who think this is really important, having at least a preliminary implementation. And yeah, we can we can make a call on on the next all core devs

Okay. Yeah, we're already at time. But I guess a couple just announcements, before we wrap up, Geth put out a post mortem on the split that happened. When they they basically announced that there was a vulnerability that they patch. This is linked to the all core devs agenda. You can read it there. There's two other or I guess there's three other kind of EIPS. We didn't have time to discuss that are not urgent. And if people want to have a look async those are also linked in the agenda. Yep, that's pretty much it. So thanks, everyone.

**Diederik Loerakker**

Thanks.

**Łukasz Rozmej**

Thank you. Thanks.

**Danny Ryan**

Thanks bye

**Martin Holst Swende**

bye

---

## Attendees

- Alex Stokes
- Andrew Ashikhmin
- Ansgar Dietrichs
- Baptise Marchand
- Dan Buchholz
- Dankrad Feist
- Danno Ferrin
- Danny Ryan
- Diederik Loerakker protolambda (protolambda)
- Gary Schulte
- George Hervey
- Guillaume Ballet
- Joshua Douglas
- Justin Florentine
- Łukasz Rozmej
- Marek Moraczyński
- Marius Van Der Wijden
- Martin Holst Swende
- Matt Garnett (lightclient)
- Micah Zoltu
- Mikhail Kalinin
- Nhlanhla Hasane
- Paweł Bylica
- Pooja Ranjan
- Ratan Sur
- Sajida Zourahi
- Sam Wilson
- SasaWebUp
- Tim Beiko
- Trenton Van Epps

---

## Next meeting on: October 1, 2021, 14:00 UTC
