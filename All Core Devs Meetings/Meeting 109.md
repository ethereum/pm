
# All Core Devs Meeting 109

### Meeting Date/Time: Friday, April 2nd, 2021 14:00 UTC

### Meeting Duration: 1 hour 45 min

### [GitHub Agenda](https://github.com/ethereum/pm/issues/289)

### [Video of the meeting](https://youtu.be/V-Qz4UN6Z88)

### Moderator: Tim Beiko

### Notes: Alita Moore

### Summary

## Decisions Made

| Decision Item | Description |
| ------------- | ----------- |
| **1**   | Use geological faults for testnet names |      
| **2** | Postpone EIP 3074 and prioritize client dev security investigation from a user perspective; generally, there's contention among the core developers regarding security concerns of EIP 3074 because it introduces a whole new security paradigm; the core developers want more time to take the necessary due diligence in understanding the security implications and to begin client developer outreach for similar reasons. Alexey, Martin, and Tomasz expressed their concerns. |
| **3**   | Although consensus is not perfectly clear, it appears that the core devs agree that both the BLS precompile and EVM384 (EIP to enable BLS cryptography on the EVM via arithmetic optimizations) should be done. BLS precompile is to be included as soon as possible (not in Berlin but potentially Shanghai merge) and EVM384 is to be done at a later date; according to Micah, the primary motivator for this is because the pre-compile is easier to manage versus its EVM based counterpart due to a lack of knowledge cryptographers in the core developers. |  
| **4**   | Include 1559 and Basefee only in the first dev net | 
| **5** | Delay discussion on the second dev net until next meeting |

## Actions Required

| Action Item | Description                                                                                             |
| ----------- | ------------------------------------------------------------------------------------------------------- |
| **1** |  Update your node before next meeting (google for ethereum foundation blog post) |
| **2** |  Tim to upload spec on eth1 specs repo regarding 1559 breaking changes  |
| **3** | Danny will reach back out to EIP 3074 team about user-side security audit |
| **4** | Thomasz will review and implement EIP 3074 more deeply to provide his perspective |

---

# 1. Berlin Updates
Video | [11:51](https://youtu.be/V-Qz4UN6Z88?t=711)

**Tim** - Welcome to all core devs number 109. I'll post the agenda in the zoom chat right now folks want to follow along? So we have a bunch of different things on the agenda high level mostly covering what's happening with Berlin how we're tracking it on for the London work and then both the different like high level approaches for Shanghai and a bunch of specific EIPs. So I guess just to get started. The first thing is burden happened on ranked be between the last two calls. Does anyone have an update for that? Seems like everything went pretty smoothly, but did anyone wanted to want to share anything? Okay, so we'll call that a smooth update on Rinkeby and then for people listening the update on Mainnet will be happening before the next call. So sometimes over the next two weeks. I think it's scheduled to happen late on the 14th and maybe early on the 15th. So middle of the night for North America and probably during the day of the 15th for for some parts of Europe. In Asia, Pooja the cat herders are hosting a viewing party right? You want to talk about that a bit?

**Pooja** - Yeah, thank you Tim. So the catherders are organizing countdown party in which we have invited the EAP on others for the proposals which are getting into Berlin upgrade. We have published announcement blog. I'm going to share the link here for details. It's open for everyone to join and we hope to watch the watch the stream.

**Tim** - so if people want to join I'll be there. I think it'll be midnight there two or three in the morning West Coast North America. Anything else on Berlin?

# 2. London

Video | [14:22](https://youtu.be/V-Qz4UN6Z88?t=862)

Action 1 | [14:29](https://youtu.be/V-Qz4UN6Z88?t=869)

    Update your node before next meeting (google for ethereum foundation blog post)

**Tim** -  Okay, and yeah, if you haven't updated your node now is obviously the time to do so, there's any Ethereum Foundation blog post which lists all of the client versions. So if you just Google search for that, that should be pretty easy to see. Yeah. So make sure you update your node sometime in the next two weeks. So next on the agenda was London and there's been like a lot of conversations we had last time around. You know, what should the scope of London be and how. Kind of skinny versus how how skinny should we keep it and I think what's probably most useful to decide that this getting a feel of where we're actually at with the implementations and what we expect needs to be done to properly test 1559. So, I don't know if one of the client teams just wants to give a quick update of where where we're at in terms of testing in terms of implementation readiness for just 1559.

**Abdelhamid** - Yeah, I can start so we have a small each clients integration testnet with besu geth and nethermind. So we have a consensus on the transaction encoding/decoding using the type of transaction and developed and access list, but geth and besu we have to update the transaction receipt to include effective gas for 1559 transactions. Yeah, that's where we are. 

**Matin** - Excuse me. I was just curious. So this geth implementation with 1559. Is that as far as I know there is no such open PR against geth. Unless I'm mistaken. 

**Lightclient** - We haven't opened it against geth yet. We've been tracking it on our teams branch.

**Martin** - Whenever it's ready, but it will be interesting to see so take your time. 

**Lightclient** - Yeah, I mean, I think we can go ahead and open it as a draft. It's because we were splitting it into the consensus portion and into all the other, you know transaction pool that kind of stuff related related topics. So we can open the consensus one first since that's mostly done.

**James** - Is the one Abdel mentioned use transactions envelope EIP. [yes] there was some like theory theorizing that it would be easier to implement if use through using transaction envelopes. I'm just curious like was that the case or there's any kind of differences.

**Lightclient** - I didn't personally implement it before and so it felt pretty natural with transaction types. But I also had worked on the transaction types even before that so I am not sure if this is 

**James** -  I was just curious it's alright if 1559 we can go into a more deeper. I mean those that I can go more deeper on the channels for that.

**Tim** - And the other thing that came up in the chat was there just a reference test for 1559. So I know I think there weren't any I don't know if there were any period. And I know specifically there weren't any for the transactions. Does anyone have just a update on that and what would be needed to do over the next few weeks?

**Gray Schule** - I'm actually working on reference tests for 1559 right now. I've had a couple of things that I've had to sort out for getting them running with transaction types against Besu. And then after that I'm going to be taking objects existing 1559 tests and getting them into reference test form and at least start the conversation around what those what other reference tests use cases might be necessary.

**Martin** - about the reference tests. I'm assuming that tests for 1559 has to be block chain tests, right? [yes]

**Tim** - I think this is your first time on the call Gary, but Gary is on the besu team. He recently joined. [...] So sweet, so I guess yeah, we'll definitely make progress on the reference desk over. The next two weeks is there I guess is it too early to try and set up a YOLO type Network or I don't know. I guess we already have it tested that's running between the different clients. But should we set up kind of a London proper integration testing is like we did for Berlin what are people's thoughts on that?

**Abdhelamid** - Yeah, I think that would be useful for wallet and libraries implementers, but we are just waiting to have a full consensus between the three clients. So we have very close. Like I said only the transaction receipt is missing on geth and Besu and once we have that we can think about the YOLO London testnet.

**Micah** - Will the current testnet build off of Berlin or is it building off of some pre-Berlin branch? [Berlin]

**Tim** - Yeah, I have a bit of a question. Do we need a new YOLO dust? That's because the one that we have is on top of the laneway VIP 1559 and the receipt changes. This is my question. Here's the receipt changes will be caused a change in the in the harshest of the blocks. If you don't then we can continue with the same network and just make it more available.

**Micah** - It should change the block hash because of the receiver route.

**Tomasz** - Yeah, I'm just not sure whether the only change in receipts is in the transport like when sending messages of her Geth P2P or it's actually in the content receipts changing the receipt root 

**Lightclient** - I think it's actually in the content. [yeah]

Action 2 | [22:17](https://youtu.be/V-Qz4UN6Z88?t=1337)

    Tim to upload spec on eth1 specs repo

**Tim** - So then to be clear then that will be kind of a consensus breaking change and it'd be easier to start up a new testnet after that it's all right. [yes] So let's do that and I'll put up a spec on the eth1 specs repo like we had for the YOLO networks given we've already kind of used a lot of the YOLO testnets and we use that name for people to not think this was Berlin but it ended up being Berlin are people fine with I don't know saying something like London integration test net or I don't know. Is there a name or we can do like YOLO V4 or something like that..

**Tomasz** - Maybe we should start calling them devnets instead of testnets so you can have distinction

**Tim** - so London devnet V1?

**Lightclient** - I just had a proposal which we could name them after geological fault lines since we're kind of looking for faults in consensus clients and that gives us a pretty large sample set of names. 

**Tim** - Okay, and from the chat, there's also yo-London and London integration test net, which is lit.

**Sam Wilson** - So I like the fault lines but lit is also pretty good and goes well with London, so

**Martin** - I personally don't I don't care about the names that we can go with whatever but I think maybe we shouldn't tie too hard to London unless we are absolutely certain about the scope of london because yeah, the idea with is like YOLO1, YOLO2 etc so that we can explore whatever features we want in them and then they go into Berlin maybe they go in maybe not. It's not if we call it like London first version testnet then we kind of set the scope London.

**Tim** - Yeah, and it's harder to take things out. 

**James** - Yes, and we did take stuff out previously. So they kind of that it did happen where we test it and then took it out and I put it back in or not. 

Decision 1 | [24:34](https://youtu.be/V-Qz4UN6Z88?t=1474)

    Use geological faults for testnet names

**Tim** - Okay, that's a really good point. So I guess in that case the fault lines is probably the best kind of neutral thing where it doesn't associate the London. Yeah, like I'd if you want to propose something you during the chat here and awkward ends get er, I can use that and put together a spec on the eth1 specs repo. Sweet, anything else on I guess the work that's been done on London so far. 

# 3. Shanghai & The Merge Proposals
Video | [25:06](https://youtu.be/V-Qz4UN6Z88?t=1506)

**Tim** - Okay, I'm so I guess the next big Topic in its kind of a maybe one is the idea of the scope for Shanghai and the merge so we briefly touched on that last call but basically there's been more and more conversations in the community about whether the eth one clients should focus directly on the merge right after London and similarly the eth two to clients right after the Altair upgrade which is going to happen also this summer and and you know, they're starting to have merge calls and specs and there's there re and ISM hackathon where a bunch of eth one and two teams will work together on building prototypes for this but then on the other hand, there's also a pretty long list of EIPs that people have been working on and would like to see on mainnet. It's unclear how much of those we can actually add in London. So obviously if we focus on the merge and London is very small in scope than those EIPs will have to wait for a while before they are deployed on mainnet. So I'm curious. I don't know the people have General thoughts about this and it's a very vague and open question. Yeah, people have their hands up.

**Ansgar** - Yeah, so I just wanted to say that from my perspective at least it seems like Community sentiments mostly seems to favor like merge as soon as possible. And so I would say that is the first kind of like decision would compromise and effect respective would be just to say it's like after London independent of how big London will be let's focus on the merge and so whatever doesn't make it into london basically people will have to wait and then like an acceptance thing that I would say that's and try and basically include as much of these kind of it many of these features into London as we can but definitely like always have to fall back of it keeping it kind of like slimmer if we run out of time or something, but I think the most important thing should be focused on the merge after London independent of how much we end up fitting into into it.

**Tomasz** - Yeah, I think that if the community were given any information that they kind of also putting EIP 1559 delay at stake if they were choosing for the for the heavier London and maybe it will change like the kind of sentiment that we see with the community. So that's why I was pushing for the as quickly as possible. Well-defined and slim London and then discussing what comes next and comparing whether we can run in parallel the EIPS and and the merge or the merge happens first or the EIPs first. I think we'll also know a lot more after the rani's in May will be much easier to take some decisions then as well.

**Micah** - Are we operating under the assumption that one or more of the dev teams is only capable of doing one of either feature work or the merge at once; is that accurate? like no, we can't all just work have like if you learn big enough to have emerged being worked on as well as future feature working.Is that correct?

**Martin** - I would say that it depends on many of these suggested EIPs our kind of tiny and the actual implementation would fit on the sleeve basically. So in those cases, I don't see it as a problem; something a bit larger like 1559.. Yeah, in those cases it becomes more of a resource. Not always but in general.

**Micah** - Do we have some mechanism of identifying which of the desired features for post London fall into the the camp of we could probably work on this in parallel or we just have to kind of go through them one more time and identify that. 

**Martin** - I think the question is more like which which which are the ones who take the most work. And I think it's two things here, it's implementation work and kind of, uh, larger work of figuring out what are the what are the implications here? What are the quirks or test cases that we need to cover? What are the possible faults of someone can possibly do? Well, implement this and how do we ensure that those faults aren't present, etc, etc., which is probably more work on actually implementing it. But both of those things are easier if the change is a one liner, obviously. Yeah, I guess it's a case by case basis. 

**James** - I was just wondering if there's anything that's kind of close enough to be thinking about even being part of the next YOLO part of London. Or any of the EIPs that close?

**Sam Wilson** - I mean, I think 3074 is pretty close. We have a testnet already up with our own implementation.

**Micah** - Yeah that's been done for like nine months.

**Tomasz** - Yeah. We have the BLC curve which would basically be a one liner, not one liner, but a few lines of code and testing should be very easy as well. The partial removal of refunds may require a bit more conversation, which I think is well defined and actually not that hard to implement. I'm not sure about everything else. 3074 might be interesting, but we'll see this might be more work, I guess, but it bases of some is 2718. So 2718 opened a lot of opportunities for us.

**Alexey** - I think I kind of expressed this previously, and I do understand that we want to be super optimistic about these things, like, oh, you can do this, you can do that. But the my current feeling is that, yes, we should do everything. We should do London. We should also start doing merge and we should also do tons of EIPs. But yes, it is the resource drain, as Martin said, and yes, we do have to already I do already have to send people to work on the on the merge and now I have to find out who is going to do the London. And then and then what happens next is that we will basically completely cut me off from even looking at the EIP that are proposed. And so we will get to the situation, which is kind of a bit reminding of the 2315 where we were so busy we couldn't look at anything and then something was going on in the all core dev calls. And then we, we spotted something last minute. I mean, yes, that was my impression, that we're trying to be super optimistic and just try to pile things in. But as far as I understand it, not every development team is the same and they are not on the same kind of path. So, for example, we're still we're still essentially refactoring. We're still trying to finish things. And, yeah, we are slowing down because we have to do lots of new features. But I'm not complaining, but I'm saying that please.. because basically all this work has to start right now, even though the merger plan for Shanghai. But the work already has to start right now. As far as I understand, it's not like we can wait till whatever June to try to work on it. That's what I want to say.

**Tomasz** - I think we're in a good place that's mostly like model code for long for July, he's practically ready and tested. I don't know if you've ever been in such a great place before on out on such a big change. And as for the merge, as I say, we will have a lot of revision after after May. But looking at the first call, it looks very promising and being quite smooth transition and a bit of research and be so many people involved. I mean, obviously, I don't want to say this are not a reasonable concern. I think Alexei also has a good way of thinking about things that they maybe maybe it was better to be a bit more cautious here and there. But from our perspective of nethermind, I think that we are very, very confident about the set of changes. Even looking at all of those EIPs, we've already tried of some of those. We already have implementation for 2395 8935. We have London ready. We have started to look at merge and it seems to be not that great, not a great effort from the perspective of just one client, more and more like research analysts perspectives. You know.

**Mercelo** - I wanted to support with what Alexis is saying regarding resources at open ethereum I think right now we're a very tight. When resources were still there, implementation of the 1559, so we would we would rather not rush some new stuff.

**Ansgar** - Yes, I had a question mainly for developers. I think Martin was saying earlier that, like for the kind of before London, we shouldn't constrain ourselves to like having the exact EIP set for london. I'm just wondering how much like how feasible would it be to basically go ahead with all the EIPs that are ready? And we would kind of ideally want to see I mean, it it's just kind of like is fully tested in the beginning and then just kind of like free kick out those that we feel like it just turn out not to be quite ready and then just basically shrink, shrink away down instead of shrinking down now and then just going with a small set. 

**Tomasz** - You know, I personally think it's a great idea to create this like YOLO like testnet with all of the steps that we have listed on the agenda today. It would be great to see it and literally suggest that this is Shanghai or Cancun or not even name it. just if they're all behaving fantastically, then maybe only then we can talk about them in London. I think it's quite nice to really change anything on London. I would prefer to keep it slim, but definitely if it has gone super well, then we can say, oh, it's totally fine to go in parallel with the merge because we will actually see how the work is progressing. If it's progressing slowly, then it's a very clear suggestion that actually we are focused on the merge and it takes our brainpower to think about it, to research it, and we will have the visibility of really what the resource strain is there.

**Tim** - So I guess trying to aggregate all of this feedback, you know, clearly some client teams are a bit more resource constrained than others. At the same time, there are like a lot of proposals that can add a lot of value that are not, you know, that that we might want to do. Does it make sense to, like, maybe grow the network? So say, like, let's start with YOLO or whatever we're calling it? I think it was aluthe. So like the first dev net to have just 1559. And then maybe if that's up and running smoothly, we add a few more EIPS on the second version and then we add a few more EIPS on the third version and try to get a list of EIPS that are easy to add or ready to add. Yeah Martin, I see your hand is up.

**Martin** - Yes, so I didn't really understand that idea about having all the EIPs in the first half and then effectively removing them, because I just think it will basically no clients be go in the first testnet maybe onee time, but therefore it makes more sense to me to start with a limited set and grow it because then all the clients who want to do anything and how to implement everything from scratch from the get go. I mean, there was another thing. Also, I realize we're talking about work that that clients need to do. And I just like to remind all the client that at some point geth will switch over to fully eth 66. I mean, we're not going to yeah, we we would like everyone to join us on eth 66 so we can drop support for not 66. Yeah, and I hope I was just hoping that that work is also getting some some, uh, yeah. Getting done. Yeah, it's just one more thing that I wanted to, uh, I wanted to remind everyone about.

**Lightclient** - I just wanted to say, you know, if we do these testnets, that's where we start out with the EIPS and kind of call it back down. My worry is, is that the EIPs that go in really needs to go through some process and be agreed on like or does to some some reasonable degree. Because exactly what Martin said, if if we just today cut the meeting off right now and start implementing if they're on the list, some of these issues are probably things that are immediately going to get shot down while we discuss them or immediately if people are going to want to push them back later hardforks. And so that's just a lot of work that's going to go into implementing and maintaining the force for the EIPs that it's really the light of day. So I'd like to see the EIPs that go into the testnet and at least be considered for inclusion or some sort of stage where core devs at least feel on principle that it makes sense and they're willing to put it into hard fork if it's implemented properly. And there's nothing that comes out there and the integration, nothing comes up in the community in the coming months.

**Tim** - Yeah, I think that makes sense and you know, James has a final comment to get to you, James, before we move on, but I think one way to have a better feel for that is to take some time now to go over the list and get people's feelings about the various things there. Yeah, James, your hand is up.

**James** - I was just for it for something realistically to get into London. It would need to be on like a dev net in the next six to eight weeks, probably, or less. So having like round one of the dev nets being 1559 plus maybe whatever, if there's something easy to add and then round to be is what we can fit in actual resources wise, because a bunch of them seem like you could just throw them in and it would take like two weeks to get most of them done and then kind of start from there as deciding if it should go into London or not or if it should go into Shanghai. We maybe just go through and our packaging what what we think could be packaged.

**Tim** - Yes, I agree that generally makes sense, like the time it takes to implement them and how ready they are will be a big factor. So, yeah, maybe we do have like a pretty long list. And I know a bunch of people are on the call to kind of give an updates or discuss their EIP. So maybe it's worth taking a few minutes to go over the list and then coming back at the end to see, you know, how people feel about. Yeah, the different ones and their scope open. What the are.

**Micah** - Let's focus on the easy ones, yeah, maybe like a sentence.

**Tim** - Ok, so I guess, yeah, I listed them on the agenda, I guess, in the order of like. How much people have signaled roughly that they'd like this to be potentially in London or shortly after, but this is like a very subjective list.

**James** - Yeah, I was going to say the first question we could triage is would would this fit in like the next step and scope of work? Just like to get a flavor for how simple it is.

## 3403

**Tim** - Yeah, yeah, I think that's probably simplest. So the first one is 3403, so this is the partial removal of refunds, the kind of updated EIP by Vitalik. I see. William, you have your hand up. Yes.

**William Morris** - So have you thirty four or three as the net negative first, the proposal removes any incentive to declare a state except for in the same transaction case. When smart contracting engineers build around such incentives, we'll see more state bloat. Approving less than infinite will be phased out in the U.S. selling all of your tokens and much interface leave one unit behind. Sotrage arrays will be cleared by setting the field size to one rather than zero, and leaving all entries dirty because it would be foolish to clear them. But these are only a few of the design implications that propose. The proposal also sacrifices current elasticity, which smooths gas price by stiring peak congestion. 1559 does not provide sufficient elasticity because peak congestion lasts hours, not minutes. By sacrificing refund elasticity concurrently with one five five nine, we should expect a net increase in volatility that would counteract the anticipated improvements and signature time gas price estimation. Well, the motivations for the proposal cite brief, for instance, possibly dangerous. I believe them to be the top feature of one five five nine grocers don't raise their prices during peak hours. They hire part time workers so their customers don't complain and flee to other stores. The long term costs of potential for exports are amortized during periods of lower congestion, but all nodes should be able to verify the consecutive for export smoothly, or else they wouldn't be able to sink the block chain in any reasonable time frame, as proof that the network can handle four times the present today I present Binance smart chain, which sets a higher gas limit of thirty million every three seconds, approximately eleven times the current capacity. My geth node, which runs on an older low end processor, it's seventy megabits per second in Berlin, so I would still be able to sync binance blockchain if all of their blocks before 4X. In the previous meeting, we agreed to table 3403. It wasn't a security concern. There have been better ideas floated in the discord, such as separate markets for competition, gas and storage with less resolution might do more good than harm. And we could free up in engineering for more bandwidth, for more important work, such as the base fee opcode.

**Tim** - Thanks, I guess. Martin, you have your hand up, but one comment from the chat William, if you have a copy of your remarks that people can read async, I think they think that would be valuable. Martin?

**Martin** - Yeah, I won't answer all of that, but I do want to say that, yeah, I can stand up and not only my Raspberry Pi, which can do what 10x what ethereum can do from a clean slate program where they were. And that wasn't really what I wanted to say. What I want to talk about was the changes that have been made on all three since the last call. We did change the EIP a little bit so that we can now make it better and the execution setting the zero back to zero. Then if you use the EIP 2121 but it's better to using 1010 pattern than resetting something back. Something else. The one of the implementation of the full implementation of this in geth, there is monitoring from the EIP. The possible coroner cases and edge cases from this, I think are fairly limited, are easy to pass through them like those stories and more on the full coverage of it. So I don't think is a large burden on testing. And the last thing I want to mention is something that we're seeing a lot is that miners are at times of low capacity, they're using the refunds as a battery and they fill the mint tokens at various times into their blocks because it's free for them. And at later points in other people's pockets, they can get extra money and people use their mint geth tokens. And this battery, yeah, so the use of the battery to get more money from you in the block and I see this as highly problematic for state growth and think in the state of mind, you know, that's something I really think it's important to get rid of as much as possible.

**Vitalik** - I also just wanted to add that I do think that it's worth taking the 4x variance risk seriously, in part because it's likely that are very possible post berlin miners are going to vote the cost of it up just because these are extremely high and 2929 does mitigate some of the risks of doing that. They're still the same size issue that will realistically end up getting handled after the merge. And so like basically it's not just a possibility of 50 billion collected, potentially a possibility of a higher than 50 billion gas blocks. And the user, like the user experience benefits of opening up more gas space are very significant. And they're probably just in terms of raw magnitude, it much more significant than the inconveniences of making it somewhat less well. So. Just for that reason, I would be kind of wary of saying, you know, we can handle current blocks in 300 milliseconds so we can we we can handle things that are 4 times bigger just fine.

**Tim** - I guess, yeah, before we make any decisions about what moves into testnets and devnets and whatnot, it probably makes sense to just go over the entire list. So we have a feel for what are the different proposals. Does anyone else have any final comments on 30 final 3403 before we move on to the next step?

**Wiliam Moriss** - Yes, I think that the forex should be very brief in scope and most nodes that are able to process it specifically the miners would be fine. And even if a Raspberry Pi was left behind, it would be able to catch up in the meantime. And the reason that 4X should be fine in the long term is that sink time is the primary motivation. I think. for setting target gas limit.

## Base Fee Opcode

**Tim** - Thanks. So next on the list was the basically up code, we've talked about this a few times and I don't think anybody had any concerns about it or the concerns that were there, I think were addressed by Vitalik in the issue itself. Does anyone have any thoughts, comments about it?

**Vitalik** - It's as close to a literal one liner as it is likely to get. And so I know to me it feels low cost.

**Martin** - That seems like a one line.

## EIP 3074

**Tim** - So, yeah, let's go back to it at the end. Next up, EIP 3074 Yes. So this is the first time, I think or maybe second we discussed it on the call, but I know there's been a lot of change on the EIP, so it's probably worth taking a minute or two to just give some background on what it is and the changes that have been made.

**Sam Wilson** - So quick summary of 3074, it's coming out of sponsored transactions, but it actually has a lot of uses besides that, it introduces 2 opcodes off and on call. So off lets you take a Signs message that's socially constructed and it's such a context variable that stores the recovery address from that signature. And then we have the off-call opcode. When you when you use it, it works like a normal call, except it sets the caller address to the recovered address from the previous signature. And this lets you do things like sponsor other people's transactions. Do an erc20 approven transfer in a single transaction. It has a really a lot of really like UI kind of improvements for users that we want to bring to ethereum.

**James** - Is this something that someone could like, we could have community members testing what it would be like to interact if it was on like a YOLO like some stuff you sort of need more state or some stuff is more tools and integration testing.

**Sam** - Yeah. So so you could interact with this today? It's a little a little tricky because we don't have to assign arbitrary messages, but we have test net up already if anybody wants to play with it. And yeah, you can absolutely start using it right now and writing special contracts that use it.

**Ansgar** - I think it is worthwhile noting that the GOP, while maybe a little bit contentious here, I think it does have quite a quite a bit of interest by kind of application developers. And so at least with regards to the question of like what could this be meaningfully tested like from the user side already, like in one of these YOLO testnets. I think in general, the answer is yes. Also, just because I think a lot of these well, the developers and services like insurance on would be very interested in kind of like already experimenting with it once, once it is in it. So I would expect like some prototype kind of support for it to match very quickly. It's part of the testnet stage

**Sam** - We had a community call, I think it was last week, and we had a ton of interest and lots of people were interested in using it, so.

**Tomasz** - Oh, yes. I wanted to ask about security considerations. Like, is it introducing any risk that people will behave similarly to allowing unlimited spending on the ERC 20 tokens if there's a risk that people will be.

**Sam** - Yes, there are a lot of like significant security kind of considerations and I think you really have to be aware of. So we have this concept of like Invoker contract and I'm just going to talk about it now because we're going to talk about it a lot. So a contract is the contract, which contains the authority, outcall instructions. So these Invoker contracts are going to be like if you sign a message to one of these Invoker contracts, you're basically delegating control of your EOA. So you're saying I am authorizing this invoker to act on my behalf. So he's kind of invoker contracts are going to have to be, you know, fairly well audited. Users are going to have to trust them. And it's probably only going to be a handful of these well audited, vetted contracts that exist. Yeah, so it's kind of like giving away instead of getting control of your EOA.

**Ansgar** - And just just for context there, like we are of the initial conversations that we had with a couple of our pilots, like, you know, this or that and attacks people on the ground and so on. And I think most people, at least right now, would anticipate that it would be like one of a handful of ERCs for like a specific implementation plan of contract. And then those wallets would only even expose functionality to sign for like these exact implementations and to kind of like remove exactly this kind of risk for the users.

**Alexey** - I'm sorry, guys, so I just wanted to say, because I had this conversation on the on a discussion, but I suppose it wasn't mentioned here. I'm not going to be fighting it all the time because it's going to be very exhausting for me to do that. But I just wanted to remind that I had serious objections to this EIP. And this is because, as Thomas mentioned, the security considerations and I think it's it's the it does change the properties of the signature in Ethereum, not only for the users of this particular EIP, but for everybody. So and although you can argue that it's not significant and it could be you know, it's the same in the same level as the batched transactions, but nevertheless, it is introducing something which hasn't existed before in terms of security. So the security of signing something for smart contracts does change with this EIP. And I actually wanted to compare it jokingly, only semi jokingly. You might have seen the pseudocode being proposed as a first April joke. And I actually did look at it the other way. And it does have a similarity with this one. Of course, it doesn't allow you to be sued for, you know, without any restrictions. But the restriction that this EIP is actually setting up on pseudo is that there has to exist a certain signature that authorizes the sudo. But once this signature exists, it basically authorizes any number of transactions. So that is my main objections. And, of course, we can still push through it. And it's very well kind of needed. But you cannot use this thing needs to be decided so explicitly decided whether we are actually as ethereum users, all ethereum users are going to accept this extra security relaxation.

**Sam** - So I think the specific complaint that you are concerned that you're raising is that we're changing the property of signatures from being able to perform a single action, to be able to perform many actions. So as an example, like right now, you can make a signature that or all of your like a single EC20 with EIP 3074 before you can get a single signature that empties your entire account and take all of your ERC20s. And that's kind of, I think what you're saying? 

**Alexey** - Yes, correct. So this wasn't possible before this EIP, but it will be possible after this. So just one signature and it will empty everything that you bought from all the tokens. 

**Sam** - Right. So I think this is similar to giving away your private key would be the equivalent like non-EIP 3074 analogy for this. But I think 3074 is a lot safer than giving away your private key 

**Alexey** - Because people don't give away their private right now, right? 

**Sam** - Exactly right. Because it's not safe. But we want to be able to enable the use cases that, you know, give away your private key does, but do it in a safe way. And that's what EIP 3074 does. We say we're getting your, you know, getting control of your area to a particular contact which can be vetted and it can be verified. Like right now, people might want to give away their private key, but they can't because it's not us we're enabling that could be used in a trustless way. 

**Ansgar** - I think it's also important to note that wallets we had before, and I think we've been like five different major ones, I think all of these and they all intend to just basically lock down ability to sign over 75 messages completely. So basically, like, not exposed at all and then only selectively introduced that again for like specific ERCs that again, that are like well audited, or something. I mean, it's also important to you to know that like a part of this organization scheme that that the EIP provides is that you can sign of a specific date. So it's so this my country can and is expected in general to have restrictions about what it can what it can actually do. Right. So so as long as it's not a malicious, again, attack where you just sign an arbitrary like a take up provided payload basically. But again, what would you disclose the functionality if you signed a specific message to one of these well designed, then they would include like a restriction that the signatures only valid for one time transaction that re-application. All of that integrated in the contract. 

**Alexey** - Yes. OK, you don't need to convince me right now, but I just wanted to make a record that I did object against it. And you can't say later on that nobody objected. 

**Martin** - So what I want to say and I want to say basically exactly what Aleksi said, including the thing that, yeah, this is basically the real issue, though, of course. And I I totally get that this is very useful. Sudo is useful and a lot of things are very useful. But I think, I may be wrong, but I think that the people who are interested in this and who are pushing this, they see the usefulness of this and the developers and the advanced, though, to aggregate the transactions or whatever, I think maybe it has not been thoroughly vetted from the security perspective on the application level and they were on. And I think once this is introduced, there may be new attack vectors that come to light and get discovered as side effect of this. And I think that it's too early to think about adding it, even if it's like even if it were simple to implement on the part on there, I'm not sure. I'm not fully convinced that all the the downsides from the UX perspective, whatever implementation on the ground there, too, has been fully brought to light and I think this needs more time. That's my.. So I'm with Alexey on this at the moment. 

**James** - I was wondering if I'm understanding this right, that the security considerations as far as by client developers and client implementations isn't so much in the client itself, but it's that it's pushing security, that it's pushing a lot of security stuff to the application layer that hasn't really existed before. And that's like where the big security question is, is there any of the underlying security things that bother people for like client developers, I mean, client development side of it, or like DOS vectors or stuff like that? 

**Martin** - I don't think this is a vector kind of thing. I, I mean, I think we can handle consensus changes as well. Yeah. What worries me is the user. Cut the sharp edges for users. 

**Lightclient** - Have you had a chance to look at the threat document we wrote on 3074 is that kind of was produced by Alexei? 

**Martin** - Right now, I would have like to read about it and spent a lot of time on it, and I think that would be needed. But I promise and I guess the reason why I think it's premature. And I mean, I suspect a lot of people would need to sit down with us and read it and to think about it hard for a number of days and I'm not sure enough people have done. 

**Alexey** - Yeah, basically sorry for what's in it, but I think it took me about four iteration of basically trying to understand what it does and then by explaining what it is. And I was like, OK, I was wrong like four times about what the EIP actually does. So I think it just given a glance does not cut it, you actually have to spend a lot of time to look at it, to understand it. So that's why, you know, if we only have a few people who looked at it, I think it might just overlooked something 

**Sam** - like implementation is pretty simple, but like grasping why it's why it's safe takes a few reads through. 

**Alexey** - Sure. And then it's posted and then it goes it goes back to my comment in the beginning of this call that you essentially, when all these things are piling up on us, you know, you've got to prepare for London. You've got to prepare for Shanghai to review these things. I remember when I was actually looking at this EIP, I literally spent the entire day trying to actually even just look at this EIP. I wanted to do it. But you can see that it does drain a lot of energy and time from from the core devss. 

**Martin** - And so the topic has raised concerns about security reviews. Normally, when we're changing something in the platform, we as client developers can kind of get the sense of, yeah, we kind of know what we're doing with this new opcode. I think we can handle it. With something like this, which touches the application layer might be actually make more sense to opt to some smart or maybe not hand it over to hire some smart people that really know the application layer and you stuff and have them do this. And I think that would be a good step. 

**Ansgar** - just mentioned that briefly, like again, because I think I generally agree with all these points raised, just like on the topic of many people would have to look at it, I think it's maybe not kind of like obvious and the way we present it, but like I think we have been relatively active in kind of reaching out to people. It's been mostly focused more on the ballot applications because, again, that's where it's more relevant. But like a lot of teams have been looking into it already and I would say fairly detailed level, for example, also like the consensus intelligence team has been very involved in the process as well and so on. It can just be a combination of like that. There are a lot of applications that would really like to have something like this in the protocol that we are uncertain whether it will be, I think, all of this and no reason at all to make kind of compromise on the security side. All I propose at this point was like, if it makes sense at all, maybe at least move forward with it into the dev net phase just because we already have the implementations ready, if at all. And then just see if people like by the time we have to make the final decisions, get in a position where they are comfortable enough, having looked at it enough and all of this, and if not, then like fine and can just move forward to the next iteration for Shanghai or whatever else the next hard fork is. I personally like I mean, of course we are like we are biased here, but like because we have spent a lot of time with the protocol, people looking at this, I think there's a very decent chance that people would be convinced if we're in a secure by the time that decision has to be made. So I would personally prefer to put this move forward to that stage. But I do believe, of course, people are already convinced that there's no chance that it will make it in then I think there's no reason why it should and be part of it.

**Vitalik** - So I just wanted to say that I think in the long term, the ability for a single transaction to trigger an arbitrary number of operations is going to happen just because I think in the long run, we want to move ETHX people to using smart contract. Well, let's find out whether that happens, you know, through EIP2938 type destruction or through some flash lasting or something else. And so we can't rely on this idea that, you know, you can only do one operation or thing that you sign as a long term security property. But I do see the like kind of the rationale for not doing this too quickly. I think one thing that could be helpful that might be helpful is for kind of people who are skeptical about this, about the security issues to at least kind of think through and maybe write up the documents about what their specific concerns are. Just so we have moved toward having an understanding of what the issues are on paper, because we are going to have to come up with ways of addressing them regardless. 

**Tomasz** - Yeah, I think I just feel that this intuition that Martin was mentioning is important here, so we were asked not only about the security of this particular EIP, but also to answer, which of this is can be very lightly included in Dev nets without thinking that they are very heavy ones. I think this one is heavy because it requires a lot of organization of talking to the application layer developers, to wallet creators and so on. So maybe arranging some calls that would be specifically dedicated to this. Similarly, as we did with 1559, I mean, I think a lot a lot of thinking and I'm here on the other side as well. And it's the one that may drain a bit more time from us to to analyze properly, to reach, to think of it. 

**Lightclient** - I do just want to mention that we did have a community call about a week ago with several wallet teams that we've talked with, like on the order of probably two dozen people or teams specifically about this. And I would feel I do feel like the number of people who have gone in depth on this type is probably greater than 15. So that may not be being communicated very well because we don't post about it on all core devs, but we have done pretty substantial outreach to application developers. And, you know, it's we can't force for developers to review this sort of stuff. But I and I feel like we're kind of at a point where we're really happy with where the EIP is and it provides a lot of value and it's kind of down to the point where it needs to be reviewed by core developers. And I don't know how long it would take a day or multiple days, but I think that that's really the main work that needs to be done on this, because we have the resources to continue pursuing it, you know, to London or Shanghai, whatever the next feature fork is, it's just a matter of getting some sort of of green light about this. It makes sense to put into a protocol. And then, you know, teams have already committed resources to help, you know, any client changes that need to be done or develop things on top of it. 

**Sam** - Like, for example, the interior transaction's team has already written an example invoker, that they could use with this, like there's already people that are like chomping at the bit for this EIP.

**Tim** - So I guess clearly, you know, like it seems like there's value in getting obviously client devs to look into this more, but I'm kind of mindful of the comments about, you know, there's a ton of stuff that people need to look at. Does it make sense to go over the other EIPs right now? And if, you know, at the end, we decide this is something we do want to look at, sooner rather than later, we can organize something like a breakout room or whatnot. But I'm a bit cautious of like deciding to organize one right now if it just leads to, like, client devs not prioritizing it and, you know, then there's not a ton of value or just doesn't move the EIP forward much.

**Martin** - Yeah, I think one thing that I, I think we have we can probably have I would feel a little better if we have a trail of bits or whatever or take a look at the EIP and like make an actual report from a user perspective. That I think we can do that from the foundation. 

Decision 2 | [1:14:49](https://youtu.be/V-Qz4UN6Z88?t=4489)

    Postpone EIP 3074 and prioritize client dev security investigation from a user perspective; generally, there's contention among the core developers regarding security concerns of EIP 3074 because it introduces a whole new security paradigm; the core developers want more time to take the necessary due diligence in understanding the security implications and to begin client developer outreach for similar reasons. Alexey, Martin, and Tomasz expressed their concerns.

**Danny** - Yeah, we can put together and RFP on that and we can circle back with your team on the scope of that [That sounds good]

Action 3 | [1:14:49](https://youtu.be/V-Qz4UN6Z88?t=4489)

    Danny will reach back out to EIP 3074 team about user-side security audit

Action 4 | [1:14:49](https://youtu.be/V-Qz4UN6Z88?t=4489)

    Thomasz will review and implement EIP 3074 more deeply to provide his perspective

**Tim** - OK, so let's have that as the next step, and Thomasz, you have a comment and a chat about looking at it and implementing it and giving your perspective. So if you want to do that as well? That's obviously very, very valuable. 

## EIP 2537

**Tim** - OK, next up on our this is 2537, so I think there's two things actually here. So Kelly is on the call to give an update on the actual pre compile. And Paul is on the call to give an update about EVM384. So, Kelly, do you want to go ahead first. 

**Kelly** - Yeah, sure. So, I mean, I think the brief update on that 2537 is that, you know, largely in the same state it was. You know, about six months ago, there's been some minor repricing to the to the pre-compile. But other than that, you know, basically no changes. And so really, what I what I wanted to chat about in the call today is just sort of, you know, what additional information is needed by the core developers. Or if any, you know, in terms of moving this forward to eligible for inclusion, one other note I will make is that I did put a report out into the all core devs chat yesterday that gives some comparisons versus EVM384 for that has done a lot of great work on. So I would just note that, you know, I don't think that this is necessarily an either or scenario between 2537 versus EVM384, but that they both have their own merits. And I think the question is how best to support BLS12-381 natively in ethereum. 

**Martin** - You mentioned pricing updates. And I'm curious because the current pricing model was going to be pretty good, I think. 

**Kelly** - Sure, yeah. I mean, from what I recall, they were they were relatively minor. So like, you know, a point edition went from 600 to 500. Everything is still even with the new pricing is over 25 million gas per second with this new pricing. So those are some changes that I'd seen Axic had made who originally authored the idea maybe a couple of weeks ago. But they were relatively modest changes and it still seems like it's well within a safe boundary. 

**James Prestwich** - as far as I know, the pricing adjustments are related to actual improvements in the implementations being used. As a side note, you know, 2537 and 2539 are scheduled to activate on Celo sometime towards the end of this month. So we're taking those to mainnet. 

**Kelly** - Great. Yeah, yeah, maybe one other thing got into addition to that, one of those developments with the 2537 is that a library has been created, built off of blast, which is that the library used by ethereum clients has undergone an audit and is undergoing formal verification. So while this isn't what's implemented in theory on clients today, it is now a new option for something that, you know, maybe has some higher assurance properties. And I guess, you know, to James' Point, this library is on average about 2x or more faster across every operation versus the one that's implemented today. So from a gas perspective, you know, longer term, I think there's an opportunity to reduce it even further. But in the short term.. so this is an option. You know, if there were concerns about gas pricing, you know, certainly this could be used as well. 

**Paul** - EVM384 was mentioned in the issue, the agenda item issue linked from the second item, and I just wanted to share good news about EVM 384 for there were a bunch of breakthroughs in the past few months. It is now hour within one to three weeks of pretty compatible and it has has to explore common cases and I have to share some evidence. You can reproduce, so again, one, two, three, times slow down with EVM384 and two extra common criticisms. 

**Tomasz** - Yes, we have it implemented because this was one of the questions of how quickly we can use it, so we have it implemented based on the previous libraries, which means for we would have to rewire it, but there shouldn't be too much of a problem. I think what's I'd love to hea is the list of use cases. Who exactly will be using it? Because that's slightly similar to 2315. I believe that the only concern of mine is that there are like two or three people pushing for it for some reason, which are just not fully understand as like what is the reason? What exactly are the use cases, why it was so important for Celo? And I believe there might be some fantastic cases because I just compare it to 384. And I wonder, is it great to push this one? Because it seems that it is needed as we have one year already when we talk about it and people keep asking for it. So there is some expectation from the community that it will be there. 

**Kelly** - I can maybe speak to that briefly, so, I mean, I think, you know, one of the largest use cases, which is, you know, will take a while to materialize, is the support of eth two signatures. Right. being able to use data from ethreum two. And I think that was one of the least original modifications as we had looked at sort of starting ethereum two prior to the merge. So I think that was an original motivation. The second one, I would say, is interoperability. So currently, ZCash, File Coin, Pesoz, Chia, and Harmony as other blocks chains all support or use the whole 381 curve in some way. And by and large, the main use cases, there are sort of new cryptographic capabilities. So things like aggregated signatures and threshold signatures as well as there has been some desire to, for those that are doing ZK roll-ups to move to a higher level security curve. So I you know, certainly I think that's going to be something that is is going to follow, you know, after it gets implemented. Right. I mean, I don't think that most of these ZK-Roll up projects are sort of commercially driven projects and they're using what's available today, which is the BM Curves. But I do think there is a desire to move to a higher level security curve at some point. 

**Vitalik** - One comment I would add is that the eth 2 related motivation does continue to apply despite the accelerated merge plan, because in order to have a roll up, that verifies or that works off of a data in eth2 shards, you need to be able to verify that it actually equals to a piece of data that is going to be. And to do that, you need to be able to do a nebulus EVM381 fast propogation inside the EVM. 

**Tim** - And I guess just to come back to the original question that, Kelly, you ask is like what core devs want to see, you know, to move this forward? I think, Micah, you had done some work there a while back investigating. I recall there was a conversation about what happens if there's a consensus failure. How do we deal with that? Is that still kind of the main blocker to including this? Like what library do we use? What do we do if there's a divergence between different kinds of implementations and what not? 

**Micah** - Or was that directed at me or using my name and the question? 

**Tim** - So I know you I think you were one of the last people, or at least you were the person, I think, who summarized all those conversations. If you have the latest, you know, summary of where we're at, that would be useful. But if anybody else has it that's also good.

**Micah** - I should say, my impression of previous conversations was just that the main concern in the court is that they do not have on staff cryptography experts. And so if at 5:00 a.m. at night, wherever the is live, there's a consensus failure, they don't have the expertise to step in and rapidly fix it. You'd have to call out to third parties and get a hold of them. And this complicates things. It changes the risk parameters for the core devs. That's the issue I have with that particular argument, and this is why I'd like to come up with a solution, is that eventually we are going to include new cryptographic remedies like bls because stuff like eth2. And so if we need to solve that problem eventually and the longer we put it off, I think the harder it becomes, because right now we there are some techniques we could use to address the problem of short term, such as like we put it in as a pre compile and we just assert to everybody out there that if this is failure, the quick fix is to disable the precompile and then we'll get the chain back up and running once the merger happens. And we need to do real things, we can't turn it off anymore and we lose that ability. The longer we wait, the more it can down the road, I think the harder it will be for us to to take some easy paths to kind of testing the waters with the BLS. 

**Kelly** - That makes sense. Yeah, I think those are great points. I guess you just had on, you know, some of the work that we've been trying to do over the past couple of months is to make last option, just as it does have a slightly higher insurance level in and would be compatible, you know, consensus bugs and all with ethereum 2. I think, you know, maybe another thing to that point is that there is a wide group now of developers that has at least experience with the library. Obviously cryptographic, you know, carrying a cryptographic expertise is a limited resource. But I do think that there's a number of eth developers who are quite familiar with the internals of Glas as well that can hopefully mitigate some of those risks. 

**James Hancock** - I was just trying this out in the chat, but I was wondering if the bls is something that we need that would be best to do before the merge. If we did it at the merge, would it have a extra security considerations or could we just say, let's do it after the merge kind of a thing? 

**Dankrad** - I think it's not critical for the merge. I think it has to do it after and would be good to have it before sharding. 

**James Hancock** - So probably not during the merge, but either in the future fork before or after. 

**Danny** - I think there's little appetite to do any modifications to the EVM at the same time of swapping consensus root to proof of stake for security.

**Kelly** - I mean, one question I would have is, is, is it eligible for London Pre-merge, given that it's implemented already on the clients and it's been run on two YOLO test nets already?

Decision 3 | [1:27:38](https://youtu.be/V-Qz4UN6Z88?t=5248)

    Although consensus is not perfectly clear, it appears that the core devs agree that both the BLS precompile and EVM384 (EIP to enable BLS cryptography on the EVM via arithmetic optimizations) should be done. BLS precompile is to be included as soon as possible (not in Berlin but potentially Shanghai merge) and EVM384 is to be done at a later date; according to Micah, the primary motivator for this is because the pre-compile is easier to manage versus its EVM based counterpart due to a lack of knowledge cryptographers in the core developers.

**James** - Are we at the point where we can just say we should do both BLS and EVM? [some contention] I mean in general, we should just be both eventually when you're ready. 

**Paul** - I just want to mention for EVM384 I'm in touch with cryptographers who will use it for various reasons. And also EVM384 I'm pretty sure it's useful for deprecating, for example, deprecating the BM precompile. So it has a lot of applications independently. So I think that's a nice way to put it, James, to do both. But I don't know what the client devs wants. 

**Tomasz** - I just wanted to defend London once again, I think I think that the shanghai parallel with the merge would be great place where I would fully support it to be included 2537. As for London, I would love to see just 1559 there. The difficulty fork. 

## EIP 2327

**Tim** - Got it just yet, because we do have a few more EIPs, I think, before we make any decisions for the devnets and whatnot. Hopefully we can go a bit quicker, these three last one seem a bit smaller. 2327 BEGINDATA, I don't think the person who actually wanted this is on the call today. So does anyone feel strongly or have any comments about it? Worst case, we can move it back to another call. 

**Greg** - I'd like to support it. Yeah, Martin's not here. This person brought it up for the agenda. The only possible issue, I thought, and Martin might be able to speak to this is whether we're concerned about existing contracts, possibly counting on invalid op codes to stop themselves, I think is the issue. Would that be correct, Martin. 

**Martin** - I can't say I. because I think this BEGINDATA. I think it's maybe not sufficient and it could be done differently and better, and I know that's problematic. And the two more are working on this proposal, which would supersede the BEGINDATA and the loan proposal. Yeah, I'm yeah, I don't know what else I'm I'm not a fan of the BEGINDATA proposal I've mentioned before. 

**Greg** - I'm a fan of some such functionality, to not have to squeeze data into unreachable sections of code, 

**Tim** - So I guess you have to keep it short, you know, because they're close the time. Clearly, there's not like strong consensus and there's still active discussions on this yet. So I think we can move on to the next..

**Greg** - OK, I'll just I'll jump ahead and save time. Actually, this 384 Axic, superceding this with an encapsulation format. Several other things are all EVM changes. So I've just reopened a magician's group on that. We have the EVM channel on Discord and I just encourage us to come together there some and discuss these EVM changes together so they can appear as sort of one coordinated set of changes whenever they do appear and not just be a scattershot set of EIPs. And certainly that's not London and probably not Shanghai. It's going to exist. 

**Tim** - I posted the link to that magicians thread in the top here for people who want to contribute. 

**Paul** - Just to respond to Greg, I agree, I think Chris called for a conference on improvements conference or something where we can all get together. So I think this is a line for during the subroutines discussion recently, but I think it's a good idea to have us all come together. I just want to say, I think there's too many moving parts right now with the merge with 1559, all of these things, like you said. So I think that nothing is so urgent that it has to be done immediately. But, yes, I agree that we could all come together and all have some sort of conference or meetings about future of the EVM and future of EVM improvement.

## EIP-2677

**Tim** - Yeah, lots of things we would like to have conferences for right now. Unfortunately we can't. Next up, I think this was a pretty small EIP. 2667 this is limiting the size of the initcode. Martin, you were the author on this? 

**Martin** - I was.. it limites the size of initcode because it was already limited and, apparently someone can execute one megabyte of code, which is not really a problem. It has happened many times, which can pull some chain, can obviously handle it. However, there might be situations where we want to do more work. And I'm picking up things like we want to validate more things about the execution. And not only do we want to do other kinds of validations, and whenever we want to implement that, it would be nice to have a guarantee that, you know, we don't have to do this on a piece of code which is larger than forty eight KB, which your implementation can do whatever kind of validation is needed within a certain amount of time or data, and you're going to be fine. And then we're going to have a new case of service attacks with someone exploits these valuations on two megabytes malicious and initcode data. That's it,implimentation wise it's small. There are, it touches three points, create, create2, and transaction query. And the semantics of erroring in these cases are not new. 

**Vitalik** - one kind of longer term point on code. So when we have code medicalisation and so we'll be able to have witnesses that only touch that part of the code in a particular transaction executes one side effect of this is that it would theoretically be possible to allow create to create much larger contracts because each transaction would only still be able to access a small portion of that code because of gas restriction on do we anticipate do we anticipate any kind of secondary risks of that? Like do we do we anticipate there being any kind of fundamental risks of code that gets created going up, as you say, half a megabyte, even taking into account the degree of opcodes which have to pay 200 gas for that? 

**Martin** - I would say no, because if we even look back on arbitrarily large code, that code is mercalized, then we don't have to load that entire code into memory to validate because the merkalization will already provide us with that information. However, if we have the initcode, which is still useful at that point to have a limited initcode.

**Vitalik** - Right, because you have to do a linear time pre-processing and whatever the merkling is, you have to do the linear time pre-processing and that's fine if you charge 200 gas for it. 

**Martin** - And the I think the main security concern here is that. Oh, yeah, whether that limit is high enough that we don't break anything. Um, that is something which is kind of easy to check. Um, I have not done so, I don't know someone else has either. 

**Paul** - I have played around with some cash thrashing attacks with EVM code, and they do increase. So if you have a large bytecode and you can make like a lot of money, perhaps jumps on each one for the cash level or something, there is a slowdown. I don't know how big it is. I got up to two times slowdown. Maybe people can do worse as the byte code size grows. So it's this sort of cash hardware you have to understand how the hardware works. I don't know what the limit is, but I think we should talk about it. I'm willing to prototype or semi-prototype to larger longer byte code sizes and stuff like that. 

**Martin** - I wasn't really referring to attacks using large initcodes. I think we I mean, I know the worst case, the notorious case for geth and I think client developers [would be aware of] what is the notorious case for their client. I was more thinking of their existing contract, large contracts where the initcode is more than 48K, because the incode employs not only one, but one, you know, two or three contracts at the same time. And we would just destroy them for this kind of change. That's what I mean. Not that we haven't really investiate. And I think it would be prudent to do that. 

## EIP 2935 Save historical block hashes in state

**Tim** - OK, I just we only have a minute. I guess we're going to go over by a few minutes, that's not too bad. Tomasz, I ask about 2935 in the chat. I don't think we can get in depth into it now, but do you have any quick comments you want to make or things that people should look at they're considering.

**Tomasz** - So we have the initial implementation of the 2935 and we'll focus on adding the test cases for this that can be used by other clients to test implementations of 2935 introduces other opportunities for the stateless clients and synchronization of stateless clients, but also interesting use cases for the decentralized finance applications where we can do some checks on the past states and make estimates based on that. Yeah, I'd like to propose it to the dev nets alongside the other opcodes. 

**James** - quick question of implementation, like, is that like a week kind of thing before we get complexity just handwaving number? 

**Tomasz** - It took me three hours, but I think to properly analyze around it, it may take maybe a day or two. 

##  EIP-3238 - Difficulty Bomb

**Tim** - OK, and then the last one we had on the list was discussing the difficulty bombs that we all agreed to put it in. We never agreed how far to push back the bomb. But I feel like that's a better conversation to have once we've agreed whether Shangai is the merge or not and have a better view for London. Does anyone have any kind of urgent comment about the difficulty bomb. If not, I think yeah, if people can stay for a minute or two, the last thing that would be useful to figure out is what do we want to do for the different devnets? Just being mindful of.. so for the devnets a lot of people have mentioned there's already a lot of things we're working on. I would propose that the first definite maybe only 1559, and that we start to tentatively add stuff for like a second one, that people have. Any thoughts on that? 

**James Hancock** - maybe, just maybe the base fee opcode, possibly, as 

Decision 4 | [1:41:17](https://youtu.be/V-Qz4UN6Z88?t=6077)

    Include 1559 and Basefee only in the first dev net

**Micah** - I say basically as well, that one feels like.. I don't see any reason to not put it in there. Just so simple. 

**Tim** - Anyone disagree with that basefee opcode in 1559? I'm OK to include it. OK, so let's do that, let's add the basefee opcode to the dev net do we want to discuss it over already over time what we would potentially put into a second dev net? Or do we just want to wait and see how this one goes and have that conversation in two weeks. 

Decision 5 | [1:42:00](https://youtu.be/V-Qz4UN6Z88?t=6120)

    Delay discussion on the second dev net until next meeting

**James** - I put something in chat, but I could just put it in the Discord. 

**Tim** - OK, I see your comment. OK, so let's yeah, let's maybe wait another two weeks anyways, there's still some work to do on 1559 to resolve this se[c]. So it's not like we're setting up the devnet tomorrow, but I'll put this up, put a specification for the devnet up probably early next week, but just at a high level we'll include 1559 and the basefee code in this first version and we'll use, I forget what the name was but the name that I like kind of proposed earlier on in the call. And that was it. Any final comments, thoughts?

## Attendees

- Tomasz Stanczak
- Tim Beiko
- James Prestwich
- Rai @ consensys
- William Morriss
- Martin Holst Swende
- Lightclient
- Pooja Ranjan
- Vitalik Buterin
- Trent Van Epps
- Greg Colvin
- Kelly
- Mikhail Kalinin
- Abdelhamid Bakhta
- Marcelo Ruiz de Olano
- Danny
- Ansgar Dietrichs
- Paul D.
- James Hancock
- John
- Karim T.
- Afri
- Gary Schulte
- Sam Wilson
- Dankrad Feist
- Micah Zoltu
- SasaWebUp
- Marek Moroczynski
- Pawel Bylica
- Marcin Sobczak

## Next Meeting

April 16th, 2021 @ 1400 UTC
