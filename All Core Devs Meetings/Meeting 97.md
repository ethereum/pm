# All Core Devs Meeting 97 Notes

### Meeting Date/Time: Friday, Oct 2 2020, 14:00 UTC

### Meeting Duration: 1:24 hrs

### [GitHub Agenda](https://github.com/ethereum/pm/issues/211)

### [Audio/Video of the meeting](https://youtu.be/v5Q5WPdN1jk)

### Moderator: Hudson Jameson

### Notes: Alita Moore

---

# Summary

## Decisions Made

| Decision Item | Description |
| ------------- | ----------- |


**97.1.1**: The expected EIPs in YOLO V2 are the two EIPs from YOLO V1 plus 2929
**97.1.2**: Tomasz Stanczak to be the champion of EIP 2935
**97.1.3**: Nothing else should go into V3 and potentially adopting Tomasz's idea -- to be fleshed out offline
**97.1.4**: Don't include 2565 in YOLO V3 until the benchmarks are done and clients are more assured -- reassess if done within two weeks
**97.1.5**: V1: 2315, 2537; V2: 2929; V3: 2718, 2930 -- 2935 (no YOLOs), 2565 -- determined next meeting if going into V3

## Actions Required

| Action Item | Description |
| ----------- | ----------- |


**97.2.1**: Ansger to bring back up CFI for EIP 2938 in two weeks

## Helpful Links

| Link Item | Link |
| --------- | ---- |


**97.3.1**: [EIPs for ephemeral testnet and Berlin upgrade
](https://docs.google.com/spreadsheets/d/1BomvS0hjc88eTfx1b8Ufa6KYS3vMEb2c8TQ5HJWx2lc/edit#gid=408811124)

---

# Agenda

- 1. EIP Discussion
  - a. EIP-1559: Fee market change for ETH 1.0 chain
  - b. EIP-2938: Account Abstraction
- 2. YOLO / YOLOv2 & Berlin state tests update
  - a. EIP & Upgrades Updates
  - b. Testing Green Light Discussion
  - c. YOLOv2 EIPs: EIP-2565, EIP-2935, EIP-2929, EIP-2718, EIP-2315, EIP-2537
  - d. @lightclient comment on a few EIPs
- 3. Other updates / discussion

# 1.a EIP-1559: Fee market Change for ETH 1.0 Chain

Video | [1:10](https://youtu.be/v5Q5WPdN1jk?t=74)

**Hudson** - Hello, everyone, and welcome to Ethereum core developer meeting number ninety seven, I'm your host, Hudson, and we'll get started with agenda item number one a this is an update to EIP fifteen fifty nine, the feed market change for the Ethereum 1.0 chain. This is going to be from Tim, who left a comment that's linked and the agenda, by the way, I updated the agenda like seven minutes ago. So refresh the page if you have an old copy of it. So, Tim, go right ahead into the update and major questions.

**Time** - Sure, thanks. So just to give a quick background on fifteen fifty nine, I think a lot of folks are probably very familiar with it is it's a proposal to change the ethereum fee market. So it has a couple of nice properties. The first is that it's hard codes, the transaction fee and the blocks. So it makes it easier to query what the right fee should be for a transaction. And the second is that it burns part of the the transaction fees in each transactions, which which creates a nice kind of feedback loop between the usage on ethereum and the amount of fees that is burned so that other people are in favor of it because of that. And it can also help potentially mitigate against some some attacks where when the fees become much higher than the block reward than miners have an incentive to reorgs. So all this to say, like a lot of different folks have been interested in this for a long time. And on the basic theme, we we started somewhat championing it again earlier this summer. So right now, both us and the vulcanize team have been working on implementations of the EIP. Another mine just joined this week. I believe they're thinking a little test that that we have at the moment. So I guess I just wanted to give this quick update. I linked a more detailed one on the agenda if people want to read that. And when I was reading through the previous discussions on all core devs, the biggest reason why why people were reluctant to include this was the potential denial of service risk on main net. So this EIP achieves all of its goals by creating by essentially doubling the black limit and aiming to keep your average block only 50 percent full. But it's possible to fill those blocks if you pay if you pay enough. So that means that we're effectively increasing the block size in the worst case by a factor of two. So I guess, first of all, I just wanted to ask the people, see other major risks or have other major concerns with this EIP. The the potential risks of having twice the black size is something we're definitely looking into. But I am curious. Yeah, I just want to see, first off, if anybody had other major objections or just general thoughts they wanted to share about it.

**Hudson** - Ok, do we have anybody?

**James** - Can I volunteer Martin.

**Hudson** - Only if he wants to go.

**Martin** - Yeah, well, problems that we see with fifteen fifty nine. Well, Denial-of-service. Aside from the, uh. It's there are basically no big issues we see with it, but it's it's a bit unclear whether the motivators or this being a minor UX benefit or if it is about the whole value proposition of doing the reorg, having a value. I mean, if the minor revenue stems from a transaction or the system from mining rewards, and how does that affect the security? If it makes if it makes sense for miners, it's nice to get a larger incentive to reorgs to get highly valuable blocks, whereas currently it doesn't really make sense to keep mining on this block or that block or it doesn't make sense to mine an old block because they're all about equally worth worthwhile. So yeah. But for yeah, is mainly the denial service, but that's what the life service, the issues that can be exacerbated if the gas limits can be raised to its.

**Hudson** - Anybody have any insight on that that they can provide? I know that.. go ahead.

**Tim** - I was going to say, I think, yeah, for for those types of security concerns, I'm happy to just paying people and follow up offline. So I think that's to me, that's fine. And already we already had kind of an understanding of those. I think it's mostly if if people have other concerns that they want to raise, that we get to discuss. And also, I guess, to get a feel for maybe folks like James around like what type of testing and whatnot they would want to see EIP like this before it went into something like it won't be in Berlin, but like a YOLO network for whatever whenever the next upgrade is. Yeah. That would also be very valuable.

**Rai** - I'd also like to know if the denial service worries people have are from the theoretical standpoint of just too many blocks taking too long, or if it's more from a kind of practical implementation standpoint of what happens to the existing clients if they have to handle so many big blocks in sequence. Because right now I don't see the issue as is with the theory of it, because doesn't the base fees just basically just increase and render each block harder and harder to fill for denial-of-service purposes?

**Tim** - Yes, but even if. Like, even if the base fee increases, those blocks are not that expensive for the film. So it's like and I take over, as I call it, whatever, like 30 to 60 Minutes, it would become much too expensive for much more expensive than, say, fifty one percent attacking etherium. But you could still get like you could still get like a short call at 15 to 30 minutes filling of blocks at a reasonable price if you want.

**James** - I'm curious in other minds, sort of starting to gear up to work more on 15 fifty nine and as has you guys just sort of started looking at it, is there something that has stood out from your team as if you're here and I can hear you?

**Tomasz** - Interestingly, I was looking at this potential denial of service attack. Before when I was analyzing just just the AP on paper, the theory behind it, and I discussed it with a few people, and I think we quickly realized that after you calculate the cost of attack, then that's it's not that serious. For example, like the current current gas prices, it would be immediately more costly than 51 percent attack. I think what I what I saw as a potential threat was that this kind of attack, you don't you don't need to have the infrastructure in place so it can be a minority minor and start doing that to some extent by just filling your blocks. Always and. But it wasn't that that's critical after we analyze that further. So I almost felt like, OK, I was over excited about finding some problem and then everyone analyzed it quickly and they said, OK, so the problem.

**Martin** - Yeah, I don't know if I follow the reasoning, but maybe we could just take that offline, so sure I understood what you meant.
**Hudson** - Ok, also, and pardon me if you mentioned this already, Tim, but I think there's like a formal analysis by Tim Roth Garden to see, and I think that might cover part of this. Would that be right, Tim?
**Tim** - So, yes, there is a formal analysis by Tim Garden, but no, I don't think it'll cover that. So the goal of Tim's analysis is more around, just like the game theoretic properties of the EP. So basically, you know, if we implement this, we actually end up in a spot where the fee market is more efficient, you know, but I don't think, like you might consider some sort of potential potential attack scenarios, but he's definitely not looking at that from like a network security perspective first.

**Hudson** - Got it, got it. OK, thank you. And the other comments on this. All right, thanks, Tim. We have some follow up to do offline on this, and we can definitely do that. The next thing on... Oh, Micah, do you have something?

**Micah** - I think there's one more thing on eBay. One five five nine, isn't there, Tim?

**Tim** - Oh, yes. So, Michael, you're, I guess, your PR around the merging of two transaction pools that that you're referring to. Yes, are we good to go on that, I guess, yeah, I'd be curious to Isaiah Thomas. I think Thomas is the only person on the call right now who's actually working on the implementation. So I yeah, I feel like we might want to also just ask afterwards into the discourse that we have, because there's more implementers there. But yeah, I'm curious, Thomas, if you have any thoughts on that, like the two, the merging of the two transaction pools and the sort of conversion of legacy transactions that 15 people, nine transactions.

**Tomasz** - Yeah, I like this idea because it was very natural for me to start looking at the legacy transactions as a VIP one five five nine transactions with particular properties set in a way that represents the meaning of the legacy transaction. It was very natural and all the code worked nicely this way, we just sent the the premium to the gas price and in the base, in effect, these gas prices well, and the transaction in then it's exactly the same behavior, almost like you said, the the premium on the new transaction to be the gas price minus the base fee and that's it. And and it's just works out of the box, I think. I really like this.

**Tim** - I was also in favor and the only I guess the only concern I potentially have is other cases where some transactions can't be converted for a reason or another. Yeah, but maybe that's something that's easier to follow up on offline as well.

**James** - It may be good to have an EIP update, what is the breakout?

**Tim** - So, no, there's an implementors call next Thursday. So next Thursday, same time as our core devs, basically six days from now, we have an IP fifteen fifty nine call scheduled already. So I'm happy to

**Hudson** - there's two chat rooms and Eth research and Discord already for it.

**Tim** - Yes. Sorry about the link to the calendar Zoom charts here if anyone wants to come, but I think that maybe these issues are easier to flesh out there and over the discord in the meantime.

**Hudson** - Great, anybody else?

**Tomasz** - I just want to say that he opened 1559 is like so noninvasive that it can be even like we were thinking of merging it to master and leaving as a as a switch in configuration, like on the implementation side is really not much change.

**Danny** - I looked at the PR and it was huge.

**Tomasz** - No, I think it took just a few hundred lines.

# 1.b EIP-2938: Account Abstraction

Video | [14:50](https://youtu.be/v5Q5WPdN1jk?t=890)

**Hudson** - I think the next item is IP twenty nine thirty eight account abstraction, I think, Ansger is here to talk about a summary of the discussion over the last few weeks and get opinions about moving the CFI for after Berlin.

**Ansgar** - Yeah, exactly. I have just a brief update. We've been obviously talking about a kind of correction since we published the EIP a few weeks ago and last two weeks since the last call, there was quite a bit of feedback in general. It seems like a lot of people were pointing out that basically because we have this this design where we did the consensus changes would be quite minimal. And then you could basically in mantel we would have iterative versions that would add more and more advanced support for and the EIP itself only fully specifies the the smallest of these of these versions with only what we call single tenant support. And like a lot of people are pointing out that there were a few, few, few of the advanced features that they would really want to to see fully spaced out and ready to also be implemented before a would be before they would consider a useful enough so that there was some libraries and then also a lot of questions around the compatibility response of transactions. And so we're currently just trying to to just working out the exact specifications for these features so they would also be ready. And then we had like a small issue with with around transaction has uniqueness. There was one case where that wasn't guaranteed. So we'd be free to to attempt to fix this data as well. Yeah. And then then basically for for for this call, our main question would be, is, is this EIP currently in a state where it could be moved to CFI obviously understanding it's not considered for Berlin and for for the Hartford after it's still very possible that people think it's not worth it. But but in general, it's at least we like we feel like it's in a state where the pieces are there. So it could at least. Yeah, it's ready for CFI. So I just would be grateful for any any feedback there.

**Hudson** - All right, does anyone have any feedback?

**Ansgar** - I'm not sure who best to address this

**James** - context for getting things in CFI were changed it to be considered for inclusion. FDR was properly formed and it could be considered, I feel like you guys are actually even further along than you would need to be, that would just be me. I'm breaking up for people.

**Hudson** - Yeah, you're breaking up a little bit. But I think I heard what you said. If this was to be considered for CFI, in your estimation, they are further along than other EIPs that would be going into CFI at this point or are in CFI.

**James** - Yes, yes, OK.

**Ansger** - Ok, and then what was the impetus to move to CFI

**James** - the idea of it is if the PR was right..

**Hudson** - Yeah, you're totally cut out now, James..

**Martin** - So I would say from the gut team regarding CFI and CFI, uh, we cannot say I don't think any one of us has thought of this in sufficient depth to, uh, say the way. But now we're aware of it at least. So maybe in two weeks say something about it.

97.2.1 | [18:45](https://youtu.be/v5Q5WPdN1jk?t=1125)

    Ansger to bring back up CFI for EIP 2938 in two weeks

**Ansgar** - Ok, sounds good to me

# 2 YOLO / YOLOv2 & Berlin state tests update

Video | [19:13](https://youtu.be/v5Q5WPdN1jk?t=1153)

**Hudson** - Any other client teams want to comment? Yeah, let's all look at this for the next two weeks, and that'll be good. OK, so next up, we have the YOLO slash YOLO V to Anberlin state test update. So this is going to be James if he doesn't sound like a robot anymore.

**James** - I'm hoping I don't sound like a robot. Do I sound like a robot?

**Hudson** - Very small amount, but it's it's manageable.

**James** - Ok, robot, passable robot. All right. I promise I'm not a real robot yet. Updates, updates on the YOLO V2 from the team, from the team working on deploying. It is where we start.

**Hudson** - Ok, so let's just have a team go first, the clients that are doing YOLO to, I believe are nethermind and geth and tip of my tongue, what's the other one?

**Martin** - Open Ethereum

**James** - lets start with, like, nethermind then.

Nethermind | [20:15](https://youtu.be/v5Q5WPdN1jk?t=1215)

**Tomasz** - So the two EIPs that were being prepared for Burlin are obviously in there. I was looking at two nine to nine analyzing that one. I think it may be one of the more complex ones, but I'm planning the day or two of work for this one. So hopefully soon. Um, I was looking at two five six five, I believe, this morning. And I still think that the construction of the IP was not perfect for analyzing and implementing it in other clients. And guess because there was this a spreadsheet that was suggesting some libraries that were available in go suggesting some benchmarks that were also get specific benchmarks and not providing the exact numbers. I think someone responded that there is a new version of the EIP new number with some more details. So I'll have to look at that one. And there is two nine three five, which I'm super excited to implement. And the question is whether everyone else wants to go with this one, because I think there was some one or two sessions when people are asking whether there is a champion for that. And no one was saying anything, but I would love to have this to have it implemented and we can implement it in that amount and show to everyone, like how it looks, how it behaves so they can decide whether they want it to look. Yeah, I think that's it, right? And the two seven 18, the transaction robbers, I prepared some bigger work to enable it, and I think this will be fine to be implemented as well. So we have like two out of six, but they analyzed all of them. And I think the most controversial for is to five, six, five, because we didn't feel like we could properly analyze it and compare it with the benchmarks.

**Hudson** - I think Martin had a comment on the magician's thread about having some trouble with that EIP too. That's the one that Kelly, though.

**Martin** - So to make a long story short, the original one was better and there and that wasn't didn't make sense. It wasn't reworked. And modified quite recently, I think maybe last week. So it's actually makes us and I implemented that in Geth and Benchmark's. My estimate was that, yes, now with the changes in 2565 and the benchmark results are more stable, they don't go off the charts cost wise. So it looks like it makes sense in geth, I can't say anything about anyone else. But I think this specification, although I know Micah has some suggestions about how to phrase it better, but I think the specification is defined enough so it can be implemented. I also thought, however, that YOLO V2, we had already removed 2565. I thought we had removed the block hashed and removed 2718, and we were only going with the previous two for YOLO V2.

**Tomasz** - Yeah I had a seperation last week, too, and then I noticed that six of those appeared for YOLO V2. I mean, I'm fine to add some of them, but something definitely happened like outside of the conversation somewhere. And that all of those were back.

**Hudson** - I think it could be an agenda er actually. Is that are you talking about the ones listed in the agenda.

**Martin** - The ones listed on the specs, the project on those specs.

**James** - If those are out of sync then I might need to update them. To what the consensus is.

**Hudson** - OK, so can we in this call so we can write it down and get a canonical what's going what is going in? I guess so people aren't doing too much extra work or anything. [yep]

97.1.1 | Video | [24:25](https://youtu.be/v5Q5WPdN1jk?t=1465)

    The expected EIPs in YOLO V2 are the two EIPs from YOLO V1 plus 2929

**Tim** - OK, so that would be great from the Besu side. Yeah, I think we agree with nethermind and geth. YOLO V2 was YOLO V1 plus 2929

**Hudson** - And the other ones were at this point undecided, right?

**Pooja** - So this Excel sheet where we have a list of all the clients status, I think the the EIP considered for V2 are mentioned there and some like two seven one eight four possibly. That is probably three that would be required for whatever was agreed on the last breakout meeting. So it's two EIPs from V1 plus 2929. And the decision, like, as Marc mentioned, for 2565, it was pending in that meeting. But now that we have clarity on it, probably we can discuss on if it should be included.And we do want should be considered for that.

**Martin** - Yeah, let me just briefly give the status update for geth, we have a pr which implements YOLO V2 and we're in it appears so generated around the status and produced state roots for all the tests. And we are in sync with Besu on all of those. open ethereum still have still a couple of bifs and when implemented in 2929. But they're almost there, it looks like. And so we're kind of ready to go with YOLO V2, uh, at any time. As for 1565, I personally don't think we should jump in of it to right now, but it would be good, I think, if the other clients, some of the clients implemented it and checked, if the benchmarks, if they look good or bad, kind of. That's the burning question. I mean, it's not like.. for 2929 it's really a lot of complexity, some semantic changes, but 1565 repricing is fairly trivial. But we need to ensure that benchmarks don't show any vulnerabilities.

97.3.1 | [EIPs for ephemeral testnet and Berlin upgrade
](https://docs.google.com/spreadsheets/d/1BomvS0hjc88eTfx1b8Ufa6KYS3vMEb2c8TQ5HJWx2lc/edit#gid=408811124)

**Hudson** - Pooja mentioned the Google Docs link and the chat. That's that's a really good thing to use to see where everyone's at as of the September 21st meeting.And yeah. So it looks like we have everything from YOLO V1 plus 2929 are the ones going into YOLO V2, is that right?

**Martin** - Yeah, and regarding testing, by the way, Demitrius has done a lot of work on and changing a bit. So when we modified the gas costs, it made some of the pillars go and basically fail because they expected most states that changed. And so they need to be modified in order to generate a new set of tests. But that's coming along. Um, yeah, it's [?] as me to mention that we've had a guy who's worked on testing documentation and he has written a couple of tutorials for generating tests and how to work with testing. So there are a bunch of them, actually. And if anyone wants to. Yeah. Learn more about the test process and how they can use client to generate the tests, these tutorials exist.

**Hudson** - Ok, that's interesting. So, yeah, check that out. Is that just on the ethereum organizations that have under testing or is there like a repo.

**Martin** - Good question. It's on record, but I cannot say right now where they are.

**Hudson** - Ok, no problem. Retest eth is in the ethereum organization. I'm guessing the wiki or something. And if it's linked to there, it can be found. Ok, let's go over besu now. For the YOLO V2 to update.

Besu | Video | [28:50](https://youtu.be/v5Q5WPdN1jk?t=1730)

**Danno** - We're in the same position as Geth, we have YOLO V1 stuff done and we're in sync with what tests can be generated for 2929.

Open Ethereum | Video | [29:12](https://youtu.be/v5Q5WPdN1jk?t=1752)

**Hudson** - Ok, great, and finally open Ethereum. Not sure if there's anyone who can update on open ethereum on the call or if you're muted.

**Marcelo** - Yes, yes, it's here with Open Ethereum. We are for the moment, we're not going to participate in YOLO because we don't have the enough resources to to do it.

# 2.c YOLOv2 EIPs: EIP-2565, EIP-2935, EIP-2929, EIP-2718, EIP-2315, EIP-2537

Video | [30:05](https://youtu.be/v5Q5WPdN1jk?t=1805)

**Hudson** - Ok, thanks for the update. Now for I guess let's get YOLO V2 out the door and then we can consider 2718 and 2565 for V3. And then there was a question of EIP 2935 needing a champion. But I thought Vitalik was the champion. Or do we need someone who's more active as a champion. Is that the argument.

**Tim** - Yes

**Hudson** - OK. Sounds good. I can talk to Vitalik about that and just ask if he has someone in mind. And this is twenty nine thirty five champion. Ok, yeah, I'll just put that down or something to do I guess.

**Tim** - Tomasz is saying in the chat that he can be the champion for 2935.

97.1.2 | Video | [30:19](https://youtu.be/v5Q5WPdN1jk?t=1819)

    Tomasz Stanczak to be the champion of EIP 2935

**Hudson** - Wonderful.

**Tomas** - It's implemented and I can convince others

**Hudson** - Ok, cool. Uh, starting next meeting you can start convincing because we're going to release V2 then start on V3 and hopefully Yeah, I'll I'll leave it to James to kind of continue on what's what's the next steps for V2 and V3 and everything.

**James** - I've I've been thinking about that and I wanted to get thoughts from that group. As far as so there's the stage of doing things on a client integration, test them like YOLO, and then the next stage is to get it onto a test, the public test. I'm hoping I'm not a robot at this point and then into Main net. So as far as from a testing perspective, is there a testing OK, perspective, saying that we wanted to go through each EIP and say this one has tested sufficiently that we should move it over or should it be a we looked at, you alluded to and it's and it's green light tested or is there another even better version?

**Hudson** - I think that the way it should go is after YOLO v2, we only have one more YOLO before going to the public test net if we even want that third YOLO for Berlin, I guess. And at that point we cut off what's going in or not because we aren't adding any more EIPs to consideration for Berlin is what it looks like. Right? Or is this just not accurate?

**James** - Yeah, I would agree. I would agree with that. My my what I'm trying to do is bridging the YOLO world into the main net world. How do we say something is ready to go to a test that in what's the process for that?

**Hudson** - I see. Um hmm.

**James** - Because that's the that's the uncharted territory we're reaching at the moment.

**Hudson** - Well, let's think about how we usually do it, we would usually do it EIPs would be haphazardly added to roadmaps to go into future hard forks, and then we would put them on the ropsten test net. And then other tests like Gawley and Koven and Marinka B would pick their dates to do their forks as well. And usually Robsten would be the first. And so I say after it's been running for at least two weeks on a YOLO net, I don't see why it shouldn't go into why it shouldn't go into something like Robsten. Once we've determined that the clients have all built out those EIPs, the ones who want to participate in the test net fork or network upgrade or stuff like that, which I mean at this point would probably need to be all clients. But, you know, besides maybe like Trinity or others who might not want to participate at that point, it'll just depend. So all that being said, that was kind of just a long way of saying after YOLO V2, I think we should just go into Robsten.Unless we want to do more stuff and..

**James** - I'll be fine, I'd be fine with YOLO V2 going into Berlin and then YOLO V3 going into the next one. it's just doing it sooner and smaller and smaller pieces

**Martin** - on this counter argument would be that if we do 2959 but don't have support for the system transactions, then we may. Yeah, things will become broken between Berlin and the next one.

**Hudson** - That's right, I forgot about that.

**James** - So maybe that one.

**Tim** - I also think maybe we have like two or three EIPs that were just discussed that are kind of almost ready and, you know, there is kind of a high fixed cost to mainnet upgrades. So if you know, I agree, we probably shouldn't to a spot we're considering something brand new. But I think if you know, something can make it into a YOLO V3 in the next two, three weeks, I personally would rather see like a single upgrade on main net where we can communicate it clearly with the stuff that's like 90 percent done right now, then having Berlin and then two months after having to communicate again that, hey, no, actually this is another upgrade with these other things. Yeah.

**James** - Do we think we could have the YOLO V3 before the next all core devs happens?

**Hudson** - we're not even sure what's going into V3, right?

**Tim** - Yeah, I don't think so. I think we can have the V2 before the next ACD because it's not even up yet. But I think and then in the next ACD, if if between now and the next ACD, we can also finalize what's going to V3, then for the call after that's like a month from now. We can probably have V3.

**Tomasz** - I think with the current approach, we are risking this YOLO thing to grow a lot before it's being merged. would it be better to actually decide which of the EIPs are connected and cannot go by themselves and then build various networks that would just be dedicated to those groups of EIPs have to go together. So for example 2929 and access lease together, but 2935 would be separate and some other things would be separate. And then when we decided in the multi-client testnet for the given EIP works then we can move it to the test net I. then we are closer to something that we envisioned in the past of being EIP focused rather than the upgrade focus.

**Hudson** - Yes, I think that's a good idea. I also think, Pooja, if this is your document, the one that you linked in the side, could you add a column? It could be after the meeting, but add a column for bundled or dependent or like bundle dependent where we link these EIPs together the need to go in together to a fork, that that would be a good idea to keep that straight on the document. And the only ones that are linked that I can see from this are 2929. And is access list even in here.

**Pooja** - No, it was not like as far as I remember, it was decided that it would not be getting into v2, but it would go along on the mainnet.

**Hudson** - Oh, because it's simple enough that it wasn't even go into a YOLO net or.. [yes] Oh, OK.

**LightClient** - So I guess I was I guess I was under the assumption that there would be a V3 that would have 2718 and 2930.

**Hudson** - 2930 or 2935.

**Lightclient** - So 2930, but that's what we were talking about here.

**Pooja** - Yeah, for access list was 2930 that was supposed to get that 2929 on the main net got it.

**Hudson** - Ok, so that's also bundled. So 2929. Sorry, 2029, 2718 and 2930 are all kind of grouped up. Right. [yes] That is interesting. Well, we know we're not they're not getting into V2, so we could there is a high cost to doing a main net upgrade, but at the same time, we don't want to spend forever on YOLO's. The thing that, like, jumps out to me, though, is that a lot it seems like the implementation cost for putting 2718, 2930 and 2929 into a V3 seems low. Or if I remember correctly, they all three of those zippers I think were like low implementation cost. Right. Because I think they're together,

**Micah** - so, yeah, so for some context, these EIPs, most of them actually started bundled with other things and in order to keep modularity in EIPs, they're split apart. But so it's almost more of a clerical reason that they're split than an actual split.

**Hudson** - I think we should have V3 be the last YOLO and have everything that's listed here try to go into voluntary, but that's my opinion. James.

**James** - I'd almost rather if we have something that's packaged and somewhat ready to ship, then I would rather do things small or earlier. And then ship the next one after that, rather than keep pushing Berlin back, needed to do they need to do this and then they'll just continually pushing out Berlin timeline versus we can just say now let's do the small things we have ready, plus any security stuff that Martin had brought up and then we can have. And so then in two weeks, we can have the we can decide like a fork block for Robsten. Basically, instead of eight weeks from now, this four block for Robsten.

**Hudson** - Anybody else have opinions on this?

**Axic** - I'm a bit lost.. we're trying to keep track, which EIPs are now part of this YOLO V2 and which aren't. But to me, there seems to be two categories. One is. Is basically the repricing of the storage and cold related instructions, so 2929. And that depends on this entire transaction transaction type. EIPs as well. So I think that that's one group and they seem to be going together, otherwise a lot of people would be, I guess, disadvantaged on mainnet. I mean, and then the second category we have is repricing of the precompiles, which have been outstanding for quite a bit. And I heard on this call that some some clients still didn't have the time to look at those, so they don't seem to be ready. And then then the last category of changes are which are neither of these, which includes a new recompile, the BLS recompile, it also includes the Block has stuff. And those seem to be also a bit more out. And I'm unclear which of these are now really close to to shipping, and I would argue that the more important one would be the repricing and the transaction types around it, unless the the precompile repricing are close enough because those are kind of small to be shipped.

**Kelly** - So what were you saying, Kelly, before we go on?

**Kelly** - Oh, yeah, I was just sort of going to agree with what you had to do in terms of, you know, if we could set a set, this list is final candidates for the next hard work. You know, clearly, as I just mentioned, some of the repricing ones have been outstanding for a number of months now. So it'd be great if we could get those in if they're relatively small changes not related to the next part, you know, official hard fork.

**Hudson** - I see, OK, and then, Thomas, did you have a comment about either test nets or YOLO?

**Tomasz** - Yes, I'm just thinking that down the road, some jobs that people started treating YOLO as a policy for Berlin and they started pushing for things to go on YOLO because they are worried this is the way to the mainnet and the only way. So you always just start using different name for being really them. And it means the trial itself, meaning that it was meant to her. And I think that what we can start doing is start building the MultiClient testnets, which are EIP specific. And when we have only clients agreeing and implementing assessment and synchronizing it, then it can be approved to go to the one of the major tests nets available for users so like ropsten. And those EIP specific testnets should always have a bundle of EIPs that are interdependent that cannot be going by themselves to other test nets. So they have to be together if they have dependencies and if there are dependencies, but they are bundled together, for example, like you can push, you can push first to nine to nine and 2930, but only later or something like two to seven, eight. And you can push it and only later you can push one five five nine, because it would require is a dependency, but it's a little bundle because it can push first one of them and then the other so they can be separate testnets. But we need to define them that they are having this temporary dependency. They have to go one after another. And the other thing is the bundles that can only go together in one hard fork. So if you understand the concept so we have the test, that's where clients can decide that, oh yes, we managed to synchronize in between the between the clients and there's like a thousand blocks and everyone is synchronising It's fine. There are some like quick, fast testing. And then you can go to bigger GasNet for users.

**Hudson** - If we do that, would we would just be a lot of, like smaller hard forks that go on every month or two. In your mind at the completion

**Tomasz** - I think it would it would enable it finally, as we were hoping for in the past, that we could actually have the proper process for EIP focused deliveries.

**Hudson** - What does everyone else think of that or James, specifically, if you have thoughts?

**James** - I mean, I guess I'm kind of in between, I'd rather just saying stuff will go into the next one and then be better about moving forward with the next one. We had kind of this lull for a while, which happened with other things beyond. Client work like the the break we took to talk about other stuff, so it would be. But I just like to I can I can hear the concerns. I want to make sure the stuff that's ready to go goes, but I don't want the stuff that's ready to go to wait for this stuff that's almost ready to go, because the list of things that are almost ready to go just increases.

**Hudson** - If we say that list has stopped, though, and we dedicate to not putting anything else into YOLO V3 at this point, except for the ones that we've mentioned as possibilities to go into YOLO V3, that might solve that.

**Hudson** - [chatter] yeah, if we get better at saying no than yeah, that would work. I think. What were you saying, Micah and James?

**Micah** - Just to echo what Thomas was saying, it sounds like YOLO v2 means Berlin now, like originally, although I understand it was supposed to mean, you know, this is not Berlin. This is just stuff that is pretty easy to implement. And so we throw it out of there and see how it works. Maybe it ends up in Berlin. Maybe it doesn't. Who cares? But it sounds very much this conversation like YOLO V2 or 3 is Berlin. Like that's Berlin. Is that correct?

**Hudson** - It turned into that.

**James** - It turned into that. I think the natural process is that stuff goes into a YOLO test net that and we don't know if it will go into main net, but then we start solidifying what actually will go to mean that through that process. So we started with a maybe things won't make it and we end with a this is the stuff that will make it.

**Hudson** - Yeah. Doing it in separate test nets like Thomas was suggesting is a really good idea I think. Because then it prevents YOLO from becoming that pre hard fork. A pretest net test net that people know their stuff will get in this first one, it was inevitable this was going to happen, though, because it's the first one. So it's kind of hard to not have all of them go in at first. I think I think it'll be easier to say no after this. If we put our mind to it.

**Tim** - I think I agree that maybe maybe like if this time you you want to say, YOLO v3 is like the pre-Berlin because it's kind of what we've done. I think the way to avoid that in the future is what Thomas proposed. You know, have a single or small bundles of testnets that people could try out and then they could just activate one at the time. And then that means we'll still need this sort of integration step. Right. Because if we want to do, say, fifty fifty nine and I don't know, twenty nine, thirty five in the next hardfork, you still need you need some test net. That's where you're trying those two together and making sure that that doesn't break.

97.1.3 | Video | [49:29](https://youtu.be/v5Q5WPdN1jk?t=2969)

    Nothing else should go into V3 and potentially adopting Tomasz's idea -- to be fleshed out offline

**Hudson** - Yeah. I think that's I think I agree with you, Tim, I think for this we should put our foot down. Nothing else goes into YOLO V3 Anything that is brought up from now on has to go into V4 later. And V3 should be Berlin.

**Tim** - Yeah, can we just remove the V3, there's no V4

**James** - V4 will be the next part because we've got we'll keep working on client integration test net or whatever. It might not be the next fork, but it'll be the next group of EIPs we're testing.

**Hudson** - Yeah. Yeah, definitely not the next fork necessarily, but the next group of the EIPS being tested. And we might not even be able to call it YOLO anymore because they'll be multiple tests nets potentially with Thomas's plan. If we if we flesh that out a little bit more offline and agree to do it.

**Tim** - Yeah, that's what I meant. Like YOLO V3 is the last kind of multi EIP ephemeral testnet and then if after that we can move to like more of a single EIP or closely bundled EIPS that have to be together, that those won't all be like YOLO. They'll be like, you know, the fifty fifty nine testnet the twenty nine. Thirty five testnet etc.

**Hudson** - I like that, James what do you think?

**James** - I still need to think more about Thomas's suggestion and how it fits with other things, but I think we should think about it and then take them, because that's a change in the process. So I want to take a little bit of time.

**Hudson** - Yeah, yeah. We don't have to decide that today, but we do need to decide. Well, we don't have to decide what's going to Berlin, but we probably should figure out, like if we're putting our foot down for things not going in. Right, I think we are mostly in agreement that nothing else should go into V3, right?

**James** - Yes, yeah. let's get V3. I'm OK with that. And then we'll be all be better at just saying keeping the scope down on things. And then as long as we keep, that will tend to us having more hard forks. Because there's stuff that people want, and so then they want to keep going.

**Hudson** - Ok, that sounds good. So is the is the so just to make sure I understand, is the agreement for the EIP listed on the document Pooja listed. Plus 2718. Wait that's already in there. Plus 2930 and I felt like there was one more

**Tim** - can we list the full list of what would go in V3 and V2 just to make it clear.

**Hudson** - Yeah so V2 we have down. That's everything from the V1 plus EIP 2929, Right?

**Tim** - Yes, and that includes the BLS precompile, if I remember correctly,

**Hudson** - I said V1 stuff, so that includes BLS. so V1 as twenty three fifteen simple subroutines. It is also EIP twenty five thirty seven bls curves. That's the V1. V2 only adds one EIP twenty nine twenty nine. Gas cost increases for state access op codes. for V3 we would have twenty seven eighteen type transaction envelope that needs to be bundled with twenty nine thirty five historical. Twenty seven eighteen type transaction envelope's that needs to be bundled with 2930.That also needs to be bundled with a third thing. What was that.

**Pooja** - 2565, is it?

**Micah** - 2929, access list. we really should not do the gas replacements without access lists like we either do both..

**Hudson** - Yeah. Yeah. So 2918, 2929, 2930. Three bundled ones for V3. And then finally the one that isn't the ones that aren't bundled. But will go into V3. We have a champion for 2935 and that seems like a pretty small change. Do we want to go ahead with that for V3. I wasn't sure if that's even was that even CFI? James, do you remember?

**Martin** - what's that one?

**Hudson** - historical block hashes in state 2935. I'm blanking on if that one even got very far in the process.

**Martin** - Yeah, I wonder if it did

**lightclient** - I know we had planned on talking about it the breakout session a few weeks ago, but there wasn't anyone there to champion it, so I don't think it's been thoroughly discussed.

**Hudson** - Let's leave that out for V3 is my recommendation. So we don't run into more delays since it hasn't been thoroughly discussed, although it does have a champion now and it can be one of the first ones to go into the whatever we decide to do after YOLO V3 and then 2565 Sounds like a lot of stuff there was resolved recently. So that should go into V3. Right.

**Martin** - Noo..? So I mean so. What remains is for all I mean, each client team to check if it's. If the new prices would cause problems for them, or if it looks good.

**Hudson** - Ok, so is that is that a recommendation for you to not put it into V3, or is that just a statement of what's going on right now?

**Martin** - I think we should schedule it. I don't know, it's a bit of a -- the recursive dilemma. I mean, if we schedule it. We might have to take it out because it might be a denial of service some. We don't get it, but maybe people want to do the benchmarks and we don't have a final.

**Kelly** - Depends on the EIP 2565, those benchmarks can be done today without any changes to the gas because we know what the gas is for the test sectors in the test sectors aren't changing. So if that's the concern it seems like what we need is just Besu and Nethermind if Open ethereum isn't participating in these YOLO type things to just run through the existing tests, text-based test sectors that are already there.

**Martin** - Right. And then scale by the actual working protocols that would be implemented.

**Kelly** - Exactly.

**Hudson** - What do others think about including this into YOLO V3 or not?

**Alex Vlasov** - Before we go much further, there is, at least that was before the bot has merged it, his first printing draft to adjust the numbers and in 2537, which is a to BLS precompile, those were just changes of the constants and I didn't merge them. So like people who already have V2 implementation would not need to go into the code base and adjusted once again. So I can just merge it goes into V2 or I can wait until V3 and it's up to developers

**Hudson** - To make it a little easier, I'd say. But it's up. Yeah, it's up to devs like you said. OK. Um hmm. So we're at a bit of a question mark on 2565 going into V3 or not.

**Kelly** - I mean, on 2565 maybe. Is there someone from netheremind or besu that could commit to, you know, they can run the benchmark which is likely already in their testing today. You know, over this weekend we could resolve whether it's going to be a denial-of-service issue for them or not. I mean, we have it on the benchmarks, on open ethereum, and the pricing was crafted explicitly to not cause those issues for open if they haven't been run for besu and nethermind. So it has work to be done. But, you know, some of them were were relaxed for open ethereum. So the question is, is nethermind or besu going to be slower than either geth or open ethereum?

**Hudson** - Can anyone from besu or nethermind comment?

**Tomasz** - For this particular precompile, most likely on nethermind, will be quite large, and that's why I'm looking at those benchmarks and trying to find the exact numbers thrown at not to not to miss anything that has like the area of attack on the pricing of five, six, five why would be potentially more expensive is because because we still use the standard book in your library and the 2565 only suggests the libraries that are not easily incorporated into nethermind, because I think there is a GMP library suggested, which is not on the permissive license [?] I guess. And the other benchmark was done with some like internal library, so maybe that one is more optimized. I think this is possible that we can rewrite it in nethermind with the current libraries that we have to work on. I need to benchmark the exact numbers, like so I think I mentioned that already a few months ago, and there was only this Excel spreadsheet that doesn't keep the numbers. I just described some benchmarks which are referred somewhere else.

**Martin** - Yeah, then I would say let's not speculate.

**Hudson** - There seems to be a little bit of.. or not a little bit there seems to be unknown's enough that if the client does feel it's going to take a good amount of effort and time to resolve this, or there could be things pop up, maybe it shouldn't go into V3 like Martin's suggesting. Does Basu have an opinion?

**Tim** - We haven't benchmarked either. I mean, we could in the next two weeks, if that was if that was kind of the main blocker. Yeah, well, we don't have a strong opinion.

**Kelly** - Yeah, I mean, the only other thing I would add on that is that, you know, while the GMP and Open SSL and other libraries are recommended, that's really those are only benchmarked because the Rust big int library is particularly poor performance at this operation, which is which is surprising. So the go to go library is, you know, perfectly performant. And I would expect probably, you know, maybe not exact same performance for, say, the standard libraries in .NET or in Java. But I guess my point is, is that I don't know that it's going to require a library chain for those clients. So it may really just be changing the gas pricing. And then similarly on the besu side, as mentioned before, there's not, you know, in terms of doing the benchmark, these test sectors should already exist in Besu. So they should be able to be run, you know, presumably with a few commands. So it should be relatively trivial work without even changing any of the code.

**Tomasz** - So I think that the .NET library should be very similar, either slightly worse or slightly better to the go one. It's just the way the EIP was written. It looks like it was suggesting to move from the in libraries in towards GMP because they were more efficient. So I started thinking maybe this requires much more efficient libraries to be added, which would be written in C or rust or whatever, and that's why it looks like potentially being a hurdle because of the requirement building and testing in the library.

**Kelly** - Yeah, yeah. Unfortunately, that was an artifact of Rust having a particularly bad big int library or at least for this specific modular exponentiation. So, you know, other libraries, other sort of standard libraries, we wouldn't expect that. So a lot of that work was done in modifications are really because of this problem with Rust. So, you know, the goal was to not require any library changes and and was even sort of the repricing was done in such a way to not require that on open ethereum, either.

**Hudson** - Ok. Um. Hmm. James, what do you think I mean,

**Kelly** - one thing I can say.. I'm happy to work with folks from nethermind or besu to collect those benchmarks. And, you know, just just see what the gas per second looks like with their current implementation in the current test vectors that are already in in their clients

**Tomasz** - I think it would be enough to clean up the EIP description and just remove what is not needed to remove what was like the work in progress and describe what it changes. I think someone was suggesting that in the discussion of EIP just it doesn't explain it properly. What is the change and what is what is the history? What is the benchmark and how do we test it?

**Kelly** - Yeah, I agree, there is a there is a new PR that does clarify the ratings parameters, change out of max function and then change the complexity formula. So there's a PR and I'm happy to share that in the chat after this call.

97.1.4 | Video | [1:03:33](https://youtu.be/v5Q5WPdN1jk?t=3813)

    Don't include 2565 in YOLO V3 until the benchmarks are done and clients are more assured -- reassess if done within two weeks

**Hudson** - I was on mute, sorry, I'm already I've already heard from a from at least one client Dev, that we should probably delay this one to not put on V3. So I'm thinking we should go with that, because there doesn't sound like there's a lot of assuredness about this one being. You know, not delaying the rest of them. I think that's kind of what I'm picking up, but it's really hard to find a consensus on this one, James.

**James** - I would say, uh, they basically there's two weeks for. [robot] The client concerns and if it doesn't happen by then, then doesn't happen.

**Hudson** - Ok, so V3, that makes sense, so we have everything for V3 right now except for that EIP, which is now dependent on these benchmarks if they happen. Right.

**James** - Yeah, and if they do happen by the next time, then I say we can do it.

**Hudson** - Ok. So that'll be up to the client teams and then also to Kelly's team to update the PR and communicate with the client teams, how best to move forward with this. Does that sound good, Kelly?

**Kelly** - Yeah, that works great, and I'll work directly with those two client teams to to run through and look at the benchmarks

**Hudson** - Okay, and can you keep us at the and the a theory. Are you in the Eth R&D discord? If you're not, let me know. But yeah, there's an all cores dev channel on there. We move from Getter. Oh okay. Great. So. Next up...

**Tim** - let's let's finish this one up, I should say. Yeah, can we sorry, like I know we kind of did this already, but we just talked for another 20 minutes. So can we just get, like, a summary of this one or two of you three just to make it easier for..

97.1.5 | Video | [1:05:31](https://youtu.be/v5Q5WPdN1jk?t=3931)

    V1: 2315, 2537; V2: 2929; V3: 2718, 2930  --  2935 (no YOLOs), 2565 -- determined next meeting if going into V3

**Hudson** - sure, so I'll try to do this. People stop and correct me if I'm wrong. in V1, we have 2315 simple subroutines and 2537 bls12-381 curve operations for YOLO V2 we have EIP 2929 gas cost increases for state access OP codes. For V3 we have EIP 2718 type transaction envelope's and EIP 2930 optional access list and then for EIP 2935 save historical block hashes and state will not be in any YOLOs for the time being and EIP 2565 repricing of the Mahdi pre recompile will be determined next meeting if it is going into V3. So to summarize, we have V2 has one of the three bundled EIPs that deal with transaction types and gas cost around state access op codes and then V3 sorry, and then. Yeah, so and then V3 has the other two of that three three EIP bundle which is 2718 and 2930. 2565 the repricing of the Mahdi precompile will be decided next time if it's going into V3. And then is that accurate. Anybody.

**James Prestwich** - Question: One of the outcomes of the previous call was that we did not want to put 2539 into V2, but left the door open for things after that. is 2539 also on this list, or should I plan on delaying that work till after V3 as well.

**Hudson** - I would say delay it till after V3, but James and others, what do you think?

**James** - In the context of last time was that V3 would be post Berlin stuff, but now it's kind of the V3 is getting us closer to Berlin. So it would be whatever after that. Yeah, but keep working on it.

**James Prestwich** - yeah, we're spinning up the testnet for it ourselves.

**Hudson** - Thanks, James, or thanks both James, but mostly Prestwich.. Is everyone clear on what.. Ok, Pooja, just ask a question, what was the question, it was 2711 oh did we not go over that one?

**Pooja** - That's was also, in my mind, was supposed to be blended together. So do we have any indication for that? It's already CFI.

**Micah** - It is CFI, but there was some issues people brought up with it, particularly with the batch transactions piece and then some minor issues with the expiring transactions. So most likely one of the breakout sessions we discussed it. Most likely what will happen is we'll split that out. And the first piece of that that will go in will be sponsored transactions. I don't think there's anything that's pressing enough that it needs to go into Berlin. It's basically UX improvements. And so I'm guessing that at this point, it probably will not make it unless someone else wants to push hard for it. I'm not going to push hard for it for Berlin.

**Lightclient** - I don't want to push super hard, but I do feel like smart [?] up debt by using meta transactions. And so the sooner that we can give them some sort of layer one, an escape hatch is the best.

**Hudson** - Ok, noted.

**Micah** - that is very true, there like six people have drafted for meta transaction standards and on every single one of them, I tell them, hey, this is going to be obsolete. As soon as we get to say, I'm like, yeah, but I don't know how long it's going to be. So they keep building stuff.

**lightclient** - I mean, if it was if we had a clear schedule for when the next hard fork would be, I would be happier to say, let's just wait a sec till the next one and four or five months. But, you know, it could be June or later for the next hard fork. And then we've spent another, I don't know, eight to ten months of our contract does develop into our contracts and meta transaction systems that are going to be obsolete once we have layer one.

**Hudson** - I understand the concern, but we do have to kind of go in order, and the first one is resolving the issues that Micah outlined. So with those resolved, we'd be able to better indicate if it's going into future ephemeral testnets. And then from there, when it's going into a fork, I guess.

**Micah** - So if there's if there's a desire to get the transaction specifically by itself, then I could have that extracted out into a separate EIP within a couple of days. I think by early next week, I would say. if there's there's drive, but if there's not then that's low priority for me.

**lightclient** - yeah, I've talk to a handful of people building these meta transaction systems, and it seems like batching transactions is a pretty critical element. So I think that sponsored transactions alone, if that's the best that we can do, it may it may not make sense to do it on its own.

**Micah** - Ok, yeah, Batching, there's some serious I think it was the geth team that mentioned it, but I think other teams reiterated that batch transactions create a bunch of complexity in the clients that people wanted to avoid and also overlaps with rich transactions and account abstraction, which are also going in. So it gets hard and complicated, especially with the timeline on Berlin. That seems much less likely if that's required.

**lightclient** - Yeah, I'm planning to implement some derivation of 2711 over the next few weeks, so hopefully maybe by the next meeting I can have a little bit more insight to what that may actually look like on an application standpoint.

**Martin** - So which one which one specifically we're talking about batch?

**lightclient** - Yeah, yeah, I'm thinking of doing the batch and sponsored transaction as one implementation.

**Martin** - So the problem with that isn't so much the what the implementation will look like. The problem we see is more like theoretical. But, you know, in order to verify the batch. I have I mean, right now that there is a transaction which uses one million gas, you do the works or doesn't the charge of something. But if you have a badge and you execute ten transactions. And then eventually find out that, no, the batch, the total batch cannot be included in a block because the tenth transaction cannot be executed because number nine burned the remaining value or something like that.

**lightclient** - So. You know, so I mean, it seems like the idea was that each of these transactions in the batch would specify their own gas limits and then the overall batch would specify some gas price and assigner to it, who is basically saying that they will pay for this entire batch of transactions and all that needs to be done to validate it as they need to go through and verify the signature for each of those transactions if it's not the same as the overall sender.

**Martin** - Right. But they can have interplay. So if one of the transaction makes the transaction invalid, then they all need to be.

**lightclient** - well, but how can you make a leader transaction valid? Because we can already verify constant time if the transaction is valid. So that means we should therefore be able to verify constant time if all the transactions are valid.

**Micah** - I think there's a miscommunication here. So there's there's there's two ways we can go about this. One is the entire thing is atomic. And either all all the Batch succeeds or fails. The other way is it's not atomic, meaning that each individual transaction will succeed or fail on its own and they will charge gas separately. If I remember correctly, there is a separate problem. If you go with the latter, which is I think what was talking about or do not atomic. I don't know what the problem was. The gas brought it up. And if you remember, Martin.

**James** - I think we're we're getting kind of closer to the end of the calls, what might be just from a YOLO V2 V3 perspective, that there's more work that needs to be done than I can for this time. But I if the next fork is in June, I don't think we're doing things correctly. So I would much rather it be Q1 of next year.

**Hudson** - Yeah, I agree. I don't think it'll be June.

**James** - Either way there's stuff to figure out

**lightclient** - I guess we can take this offline, I can spend a little time and think through some of these edge cases as well.

**Hudson** - Ok, thanks. Ok, is everyone clear on what's going in to YOLO V2 and V3? And we will have this in the notes [;)] and updated in the chart, I'm guessing that might already be worked on, actually.

**Pooja** - Yeah, and I'll create seperate tabs for YOLO V2 and V3 in the excel sheet if that would be helpful to people

# 2.d lightclient comments on a few EIPs

Video | [1:15:26](https://youtu.be/v5Q5WPdN1jk?t=4526)

**Hudson** - Thank you, the sheets are really well done everybody who'd worked on it, I don't know who worked on it. I'm guessing it was Pooja and James. Next up, I had light client comments on a few tips, and we've already gone over all of them, I think, except for maybe the status of 2584.

**Lightclient** - Yeah, that's right.

**Hudson** - That was Gaiam. And he's not here to talk about that. Did you have an update like lightclient or are you just wondering

**lightclient** - I mean, I am wondering what the status of the binary tri migration is. And I'm generally just curious to know what people are thinking is the status of stateless ethereum in general, because I think that it's an important thing to have before we [?] 1.5. which is potentially going to happen in the next 12 to 18 months. And stateless ethereum has been, you know, in progress for about at least a year now. And it seems like it's really cool down in the last four or five months. And I was just wondering if anyone has more insight into why that is and how we can reinvigorate it.

**Hudson** - So one thing that I'd say about that is that the primary people working on that would be the quilt team, right?

**lightclient** - I don't think the quilt team is the primary people working on it. I think the primary people who are working on it were, you know, Piper was sort of leading that effort. There was a lot of work that Piper was helping coordinate around the witness spec. I think there was someone from Turbo Geth and maybe Policinski spent a little time on the witness spec and and then obviously Gaiam spent some time on the binary try migration. But it's to me, it appears that a lot of this work is like reaching the point where it's getting solidified and it's starting to broach into, you know, getting it through governance. And it doesn't I'm not seeing what the clear path is like. We have a EIP that says how to go from Patricia Merkle tree to a binary tree, but there's no one who's coming here to, you know, ask what are the next steps, what are the next steps? I'm afraid that we're going to go six months down the line with all this happening. And then, you know, phase one, point five is going to be right around the corner. And we're going to get into a situation where we're going to ship phase one point five. And every Eth2 validator has to be a full Eth1 node, which, you know, there's concerns around that.

**Hudson** - Yeah, I understand. I think talking to Piper would be the best bet because I know he was at one time, like you mentioned, leading it up, see if that's why that's dropped off. And yeah, I'd be interested to hear why it's dropped off myself, but I don't know if we'll have any answers today, unfortunately.
Yeah, that was a very interesting piece of research, though, that I'd be super curious to hear where the full statuses of it.

**James** - As far as I'm aware, they're still working on it. We just don't have the.. [muted] the right people on the call to give updates so that oh.. the work is ongoing. We just don't have people on the call to give an update on it.

**lightclient** - Is there anyone on the call who has, like, better direct communications with these people and ask them to come to the next meeting or start coming to be a little bit more regularly?

**Martin** - Giam is on the geth team so I can ask him

**Hudson** - Thanks, Martin. We have about six minutes left. There's nothing else on the agenda. Did I miss anything? Is there other discussion points or updates?Ansgar, you had a comment? Oh, that was just a comment, I thought it was a question maybe. Just about, yeah, go ahead.

**Ansgar** - I just wanted to say that there were some concerns about how to best, like, combine and sponsor transactions. Obviously, I don't want to kind of hold up the progress on the transaction, which is something I will be looking into over the next few weeks to figure to just make sure they duplicate it.

**Hudson** - Ok, great. Is there any other updates from anybody or discussion topics. Ok, looks like we can probably in this one early. I do want to mention that I'm starting to brainstorm ways to improve the all core devs call and just our processes in general. So we're not, like, starting to get known as the Bitcoin, you know, ossifying, very slow, never does anything layer. So I think that I'll start pulling people in. And if you're interested in being involved in that, reach out to me. But I'll pull in some people to kind of help brainstorm some around some of that. But if you have good ideas about how to make the meeting better or feedback for myself or for James or others who usually play a bigger role in the call, please reach out. We love feedback, hurt my feelings. Let me know where I'm doing bad. Hit me up. All right. The next call is going to be October 16th at fourteen hundred UTC. Thanks everyone for joining. Have a great day.

---

## Attendees

- Rai Sur
- Hudson Jameson
- James Hancock
- Youssef El Housn
- lightclient
- Pooja Ranjan
- Alex Vlasov
- Micah Zoltu
- Tomasz Stanczak
- James Prestwich
- Tim Beiko
- Karim Taam
- Kelly
- Tren Van Epps
- Artem Vorotnikov
- Alex B. (Axic)
- Ansgar Dietrichs

## Next Meeting Date / Time

Friday, Oct 16th 2020, 14:00UTC
