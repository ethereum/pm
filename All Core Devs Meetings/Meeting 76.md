# Ethereum Core Devs Meeting 76 Notes
### Meeting Date/Time: Friday 29 November 2019 at 14:00 UTC
### Meeting Duration: 1.5 hrs scheduled, 1 hour actual
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/140)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=BMMkxeH72U0&feature=youtu.be)
### Moderator: Hudson Jameson
### Notes: Jim Bennett

## EIP Status
| EIP | Status |
|-------|----------|
| EIP-1679 | `Accepted & Final` |
| EIP-152  | `Accepted & Final` |
| EIP-1108 | `Accepted & Final` |
| EIP-1344 | `Accepted & Final` |
| EIP-1803 | `Accepted & Final` |
| EIP-1884 | `Accepted & Final` |
| EIP-2028 | `Accepted & Final` |
| EIP-2200 | `Accepted & Final` |
| EIP-2384 | `Accepted & Final` |
| EIP-2387 | `Last Call`
| EIP-1702 | `Eligible for Inclusion` Pending Champion. Not accepted into Berlin |
| EIP-663 | May not be ready. Currently depends on EIP-1702 |
| EIP-1962 | Requires more Specification. Contact Champion |
| EIP-1380 | `Eligible for Inclusion` |
| EIP-1985 | Decision required around needing a Hard Fork |
| EIP-2046 | `Eligible for Inclusion` |
| EIP-1559 | `Eligible for Inclusion` |


## Decisions
| EIP | Status |
|-------|----------|
| EIP-2384 | `Accepted & Final` |
| EIP-2387 | `Last Call`

## AGENDA

## 1. [Istanbul HF Community Call Next Wednesday :)](https://ethereum-magicians.org/t/istanbul-hard-fork-community-call/3816)

**Hudson**

Call will be held next Wednesday at 2:00 PM UTC. Anyone in All CoreDev calls is welcome to be on the actual. Will be taking questions on Ethereum Magician's Forum, Reddit, and Twitter.

## 2. [Ice Age Hard Fork](https://eips.ethereum.org/EIPS/eip-2387)

**Hudson**
Comment was made with the [meta-EIP](https://eips.ethereum.org/EIPS/eip-2387). I'll hand it off to James, the hard fork coordinator.

**Tim**
YouTube livestream sound is not working.

**Hudson**
I will post a recording of the Zoom call later in YouTube.

**James**
A couple of things to get through with regard to the difficulty bomb and a hard fork related to the difficulty bomb. Inside of the retargeting algorithm that helps keep blocktimes stable for Ethereum, there is something called the Ice Age built in that, after every 100,000 blocks, it increments up. At some point, it starts to affect block times, which has been happening on the network for about the last three weeks. To update that, we have to push back the Ice Age in the clients, which is fairly trivial to do. We can start with [EIP 2384](https://eips.ethereum.org/EIPS/eip-2384). Let's get consensus on how far to push the difficulty bomb back. It's been discussed pretty extensively on Gitter, but I'd like to hear from people here.

We have an option of pushing all the way back, which is 9,000 blocks back, or what we did last time, which was 3,000/3 million blocks back. This time it would be 5 million blocks back, which is about as far back as we can go.

**Martin**
As far as I can see, there are a couple of suggestions that have been made. One is to make a rewind kind of like we've done before, which is what [2384](https://eips.ethereum.org/EIPS/eip-2384) is. Other proposals have been to replace the difficulty calculation with something else, maybe something linear. It's been kind of vague. The third suggestion has been to immediately remove the difficulty bomb. Before we discuss the particulars of [2384](https://eips.ethereum.org/EIPS/eip-2384), I would just like to hear form everyone here if we should not do what we've done previously and should instead one of the options that has not been done before.

**Peter**
I would just like to add a bit of information to that. Essentially the problem here is not that we need to decide what to do with the difficulty, but that the Ice Age is coming really, really fast, so it would be nice if we had a solution that we could roll out at the beginning of January. Because of the Holiday Season, we can expect people to not be available starting one or two weeks from now. Which means that if we want to have any update to the Ethereum network, we have to release next week.

Because of this, there are three possible solutions as to what we can do with the Ice Age. The question is which is riskier and which is less risky. Because, from my perspective, up until now we've delayed the Ice Age twice, o delaying a third time is a no-brainer. We can do what we did previously: modify one parameter and done. Whereas the other two, we have the question marks of how involved it is and the unknown risks that we haven't thought about.

**Martin**
I agree. I just wanted to check to see if there's someone who thinks we should do one of the other options.

**Hudson**
I had a question about that, Martin. Would it be possible for us to roll it back now, because that's the one that we know works so we wouldn't have to do testing on it? Or if we do things like disable it or change it to a linear formula, how much testing would we have to do? And could we in theory do a change to the difficulty bomb after the rollback so we have this hard fork and then after it, we do another change to the difficulty bomb in, say, whatever Berlin is?

**Martin**
Yeah. We could definitely change the difficulty formula at the next hard fork whenever we want. regarding testing, we probably have to do quite a lot of testing. If we do it like we've done previously, it's pretty easy to generate tests for this. It will need more thorough testing if we do something else.

**James**
In the Gitter chat, it came up that with the Ice Age, changes to that should also be brought to the community a little bit more than we have with this opportunity, because we have to act more quickly to get a change out. Doing what we have done before is something that the community already has approved, and any further changes should take some more time and more polling to make sure we understand the values of everyone.

**Hudson**
I think that's a good point. The one I would add to that is if we're changing the formula, we probably don't need community support, because that doesn't change the fact that we have a bomb or an Ice Age, so I think that if we change the formula, it wouldn't matter, but if we take it out, it would matter.

**Martin**
So I'm curious to hear if it's sufficient in 2384 or if we should roll back more because of this period thingee which seems to have a further accelerated effect.

**James**
Can we actually do that? If we go back 9 million, we would start putting in negative numbers.

**Martin**
2384 does not go back 9 million.

**Danno**
It say to take block to 9 million and rolls it back 4 million. If we were to do the third of 9.2, it would put us in the second Ice Age block, which would be adding 2 difficulty per rather than 2 billion difficulty per.

**James**
4 million relative to now, but it pushes it back 9 million from the beginning of the chain as far as the fake block number is concerned in the difficulty calculation.

**Danno**
It's essentially like we're starting over at block 200,000 if we set a fake block at 9 million.

**James**
Are there are any other thoughts on if that number should be different? Should we try to push that further, or should we have it be 8 million, 9 million? I think this gives us at least a year an a half before the next ones show up. We've already had some discussion on Gitter as well, so if there aren't any more thought on this, we should just accept 9 million. So we'll push it back 9 million. As far as 2384 concerned, we should move it into accepted.

**Hudson**
I would say we could move it to accepted, but not until we have a block number.

**James**
We'll do that at the end of the call.

**Alex**
Is this a good time to briung up the other question which was raised on the channel that some of the Istanbul EIPs are still in draft, and that they should be marked Final or go to Last Call? It's a similar question.

**Peter**
They are pretty much final. Nobody is going to change them.

**Hudson**
That's the argument I made with Will who brought this up. Where we came to in that conversation is that switching them to Last Call would be doing process for the sake of process. It would be doing a lot of PR changing that would open up a vector for someone to stop the process. I doubt that would happen at this stage, but it is a risk. I think process for the sake of process is stupid.

**Alex**
His argument was that the Last Call is in a very a special position on the EIP repo for one single reason: that there is an RSS feed for the Last Call EIPs only. There was a proposal to have separate feeds for each of the statuses, but the only one that exists is the one for Last Call. His argument was that if something is moved into Last Call, it's going to show up in the RSS feed and maybe some new people are going to be notified about it, and they could find something this late in the process.

**Hudson**
That's not a bad point. What do others think?

**Peter**
[Crosstalk] That was a month ago.

**James**
Yeah, and historically, core EIPs haven't gone through the Last Call process. I don't know if that was meant to happen or if it just sort of happened. The better way to do what Last Call is trying to do is having the RSS feed pull out the EIPs marked as eligible for inclusion, so community members know to look at those, as the core devs have already looked at them and taken that seriously.

**Hudson**
I guess it would be easy to do Last Call and switch it to final, but I've only heard of one person who wants it, so I'm not enthusiastic about changing it.

**Alex**
Generally, I think it would be a good idea to do Last Call even for core hard fork EIPs, because if it gives us a chance to reach out to more people, that's always good. But in this particular case, I'm not sure if it's going to make any difference if you're talking about putting it into Last Call just for a few days.

**Hudson**
I'd say don't bother.

**Martin**
But if you do, that's pretty nice, because it will pop up into the feed and then it will become final.

**Hudson**
From a process perspective, that's pretty nice. I actually don't have a strong opinion on it, so Alex, if you don't mind doing that, I guess we can. It's not going to hurt anything.

**Alex**
Yeah, I can do that. The only remaining question is that the only one he marked as Last Call is the gas reduction for the Calldata bytes. Everything else is marked Final or Ready. Pragmatically, we would need to mark all of them Last Call just so it shows up and then mark all of them final.

**Hudson**
Is that something you can do, or is that something the champions or authors have to do?

**Alex**
I can do it if we agree that that's a good gesture, and maybe next time we can follow the Last Call process. We could even do it right now.

**James**
We could certainly do it for 2384 and 2387 as well, moving forward.

**Hudson**
Yeah, that's a good idea, especially once we have the block number.

**Martin**
For 2387, there's actually a block number proposed. Do we want to discuss that now, or just go with it?

**James**
Yes, we should discuss it, because the the block number written is 9,200,000, which is the next time the difficulty bomb increments, which should be first week of January - January 5th or 6th.

The last bump just happened not too long ago, so if we did 9,200,000, that is right before block time should be hitting 25-30 seconds. "Should be" is in quotes because I don't know exactly what the next increment will be. At some point, the block times start doubling but I'm not sure if we've hit that point yet. Right now, it's about 15 second block times from looking at Etherscan.

We have two options. Either we go straight for when the next increment happens around January 6, or we could push it a few weeks into the next period for the Ice Age and just have a network be a bit slower for that week. Does anyone shave strong feelings in either direction?

**Hudson**

I think the 6th sounds nice. I don't see why we should delay it an extra week unless people think there's a chance of non-adoption.

**James**
It certainly would be nice to get it in before the next bump as far as community is concerned and making sure it gets adopted sufficiently before that time. That's five weeks from today.

I'm hearing 9.2 is okay. If anyone has strong opinions otherwise, speak now.

**Martin**
I support it.

**Peter**
I support Martin.

**James**
OK, now we're good to go. Let's agree on 9.2 as the block number, and also include that it gets pushed back the 9 million blocks.

**Alex**
Just to confirm, there's agreement that the Ice Age is its own hard fork called the Mountain Glacier, and Berlin is going to happen afterwards.   

**James**
We haven't discussed the name yet. That didn't come up.  

**Alex**
But since we're talking about 2387, it's not Berlin; it's something else.

**James**
I would support that it should be considered something else, because, from a narrative perspective, it is something different than we had expected.

**Tim**
I agree there.

**Martin**
Just to be explicit, we should move this to Last Call as well. There's no strong objections to any of the numbers.

**Alex**
It has to be defined for the other testnets. Do we need to set block numbers there?

**James**
No.

**Peter**
Actually, there's an interesting question. We have this Fork ID thing which tracks forks are applied at which blocks. If we apply a fork that doesn't do anything, even though the network is functionally the same as before, the fork ID will change because it thinks something has been upgraded. So my suggestion is that we explicitly spell out that this fork does not happen on the POA networks.

**Danno**
So there's a different count of blocks on forks on the POA networks then there is on mainnet?

**Peter**
POA networks don't have difficulty.

**Danno**
Right, but I'm thinking for forward when we got to Berlin, do we presume they should happen with Berlin on the POA networks, or do they have a different count of fork blocks?

**Peter**
The fork ID only cares about the numbers when some fork happens. If the fork doesn't happen, then that's fine. The networks don't have to have the same number of forks. There can be an arbitrary different forks on different networks.

**James**
I just marked down of adding that the POA testnets explicitly don't need this, but we still do need to decide about Ropsten.

**Martin**
Ropsten has previously applied the exact same fake block number adjustments.

**Danno**
Right. So we're not going to get the same value testing as we would other changes because it's going to go to zero, or if the clients have implemented poorly a negative Ice Age period.

If the clients haven't implemented properly the difficulty calculation, it floors at zero, and they take the max value of the period, so it would be zero if we go to block 9 million for a few million blocks on Ropsten. That's why we didn't just do block 50 billion for the Ice Age, because we were concerned that some clients might not have that floor in correctly and accidentally go negative. It was a hedge against risk.

**James**
So what I'm hearing is Ropsten has different block heights, so that the same number could have a different effect if they didn't implement the clients correctly?

**Martin**
Yeah. So the thing is if we activate on Ropsten now, which is I don't know, 6 million, and the fake block number is minus 9 million, then it's way at the floor, which should be fine. It has happened previously when we did previous changes.

**Danno**
So in the 2124 test cases, it had Petersburg going in at the same time as Istanbul. It had it a zero length block length for what was calculated for those.

**James**
We could also just use a block number on Ropsten that's different than the 9 million. That just pushes it back to the same starting 200,000 block. Or not.

**Peter**
I would vote against having a different block number. The fork is defined by its own block number. It also has a parameter. For example, Geth does not have a capability to configure parameters for forks. And I don't want to add it. So I'd rather we keep it dumb and simple.

**James**
So the EIP will be the same, but it's just a matter of choosing a block height to implement.   

**Martin**
Since we're not going to get any test coverage from the Ropsten rollouts, we don't actually have to bother to make sure it happens three weeks before the mainnet one, because it won't give us anything anyway. So we can spit out some number that sounds good.

**Danno**
We could just skip it and do it with Berlin.

**Martin**
Does that make things easier?

**Danno**
A whole lot easier.

**Alex**
Wouldn't that mean that we change the final EIP with a block number when when we have the block number for Berlin, or does it mean that this EIP is not final until then?

**Martin**
I actually don't think it makes it simpler, because of dissonance between what the forks are on the mainnets and testnets. We already have one with Petersburg and Constantinople, and why intentionally add another one? We have it split up in two phases on mainnet, and then we have it lumped together on Ropsten.

**James**
So I don't know enough about Ropsten, but we could potentially roll out something this next week. Is that possible? Can we release Robson and the client at the same time?

**Martin**
Well people need to have a little bit of time to update.

**Peter**
I would argue that if you want to release something on Ropsten, too, then let's pick a block number that's at least a month out. There's absolutely no value from a testing perspective, but there is no point to break people's testnet work just just because we want to. So let's try to keep it a bit stable.

**Martin**
Ropsten is at 6.87 million right now.

**James**
So doing the math, what would end up December be for that? Or January 1st or 2nd.

**Peter**
Why is it important to be January 1st or 2nd?

**James**
It would be a week before Mountain Glacier would happen.

**Peter**
Well, yeah, but we know that it doesn't matter. It doesn't have a value. And you don't want to fork on New Year's Eve, because I'm sure there'll be somebody using Ropsten for something, and they won't have the people they need to update or fix it.

**James**
And so we can target the same time period, then.

**Peter**
Yeah, probably makes sense.

**James**
So what would the number be for January 6th, then?

**Danno**
[Ropsten-stats.parity.io](https://ropsten-stats.parity.io) shows that there are 13.23 seconds per block right now.

**Martin**
So while you're calculating, I haven't heard anything from Parity. Wei, are you guys on board with this?

**Wei**
Yes. We are on it.

**James**
39 days.

As far as the name goes for Alex's thing, we should have a discussion on that as well. I just put that in as a name. I saw your point on using something like Muir Glacier, a glacier that has been receding. So I'd like to bring up the topic of name for a moment while I'm calculating.

**Martin**

Yeah. Does anyone have a different suggestion?

**Hudson**
What's the receding one? Mirrored? How do you spell that?

**Danno**
M-U-I-R. It's a glacier in Alaska that we have photographic evidence that it has pulled back quite a bit. That's why they liked that one for global warming talk.

**Hudson**
Cool. This could be kind of a political thing. (I'm joking.)

**Alex**
Yeah. It's not all that important. I just liked the idea of naming it after a receding glacier because that's what we are trying to do here. But it's really not so important that we should spend hours on this.

**Hudson**
I like that name, personally.  Will people be confused how to pronounce that? That might be the only thing, but that might not matter, either. What'd you call yours, James?

**James**
Mountain Glacier.

**Martin**
Yeah, I'm okay with the name.

**Hudson**
Let's do Muir Glacier, because it actually has a meaning and that'll be neat to talk about in the future. Anybody else have an opinion?

**James**
Is it being politically charged? Is that something we want to have be a part of this?

**Hudson**
I don't see anything political on the Wikipedia page.

**James**
Global warming is pretty political.

**Danno**
I'm concerned about the discourse that might go on later when we talk about delaying the difficulty bomb or eliminating it. People who want to eliminate it will be called "climate change deniers" because it's gonna blow up, and I'm just concerned about secondary name calling that would go along with it.

**Hudson**
Yeah, especially since we're giving ideas on this call. Let's go with the original one then. I'm only making decisions because no one else is.

**Alex**
My vote is for Muir Glacier.

**Hudson**
All right. I'm good with that. And Paul says "good name."" I don't know which one for Mary glacier. Oh, I see. Okay. Okay.

**Peter**
I will update the the EIP for that.

**Danno**
Do we want it literally to happen at the same time as mainnet?

**Hudson**
I mean it doesn't have to be exactly the date, but we can estimate it toward the exact date, sure.

**Peter**
I did the Monday before.

**Danno**
The 5th?

How about Block number 9284829? On my spreadsheet, it's going to happen through 2.25 on 1/6 at 1119 at 13 and a half, on 1/7 at 2016, at 14 it'll happen on 1/10 at 410.

**Martin**
What do you mean "9284829?" We're at block 6 million now.

**Danno**
Oh yeah. Never mind. Good catch.

**Peter**
My suggestion is 7171717. Somebody calculate the date.

**James**
I'll go back and check that. We'll call that good for now.

**Hudson**
Okay, cool. We're just starting Ropsten fork on Gitter. We got the name; we got the mainnet stuff, so we can start sending out emails for that. Was there anything else with the Ice Age?

**James**
I had it included in the EIP a declaration of intention to fix part of what's happening. So either to make it something that's easy to model and predict when it occurs. So I think that's something we should look at as a group in the next few months or so.

## 3. [Testing Updates](https://youtu.be/BMMkxeH72U0?t=2839)

**Dimitry**
There are some new tests, so it is better to run the tests from the develop branch, not from the release. Also there is a file in the test repo called "peerlog." So you can see the recent updates with the pull requests down to the repo. For example, there was a new key wallet test and some key store tests for my crypto file and some difficulty tests added recently. Just check the peerlog.md file in the development branch.

**Hudson**
Sounds good to me. Anybody else?

**Martin**
Yes. As I wrote in the AllCoreDev channel, we now have four EBMs all passing. I just checked, and it's done 435,000 executions. That's Parity, Geth, Aleth, and Nethermind who have all implemented the standard JSON outputs and tracing. So they can run state tests and output traces which are then compared between each other every step of the execution. So the stack value are compared, not the memory contents, but stack values and the operations and the gas counters and the resulting state groups that the tests result in. Pretty good coverage.

**Danno**
Can you post a link to the documentation on how to get on that in the call notes?

**Martin**
Yes, it's posted somewhere, but I think it needs to be updated, so I can revise that and post it.

**Hudson**
And we can edit the call notes after the fact. Danno, if you want that in there, we can get it from Martin.

## 3. [Eligibility for Inclusion EIP Review](https://youtu.be/BMMkxeH72U0?t=3123r)

**Hudson**
I don't think there's any that we're going over today.

The Ethereum improvement proposal meeting hasn't happened yet. I was waiting until we had the Ethereum Cat Herder call to talk about what we were going to do more. And we had that call on Tuesday, so I'll try to plan for the meeting as soon as I can plan for it, but then the date for that will be out a little bit.

## 3. [Review previous decisions made and action items](https://youtu.be/BMMkxeH72U0?t=3138)

**Hudson**
803 was last call - rename op codes for clarity. So it's been two weeks. Does anyone have any final anything on that?

**Alex**
I added eight new suggestions to it on the Magicians Discussion URL.

**Hudson**
Okay. Would you like to restart the last call process, then, or do you think it's pretty clear that people are fine with this?

**Alex**
I don't think anyone looked at it. It was only added a day ago.

**Hudson**
Okay, we can wait two more weeks.

**Hudson**
I would say restart the clock.

**Hudson**
Okay. So make note to check on that if you care about it. It's in the Magician's thread for EIP 1803.

Also, Alex, you asked if 2384 was accepted. Yes, it was accepted.

**Alex**
Was it accepted as is or are there any changes required?

**James**
There weren't any changes. We as a group officially should move 2387 and 2384 to Last Call and have the date that the clients are released be when we update it to Final.

**Hudson**
I agree with that. I think we should do it that way.

Okay. That is the last decision thing to go over right now. So that's done. There are no other agenda items.

Two weeks from now will be December 13th, and we'll have a meeting then, and then we probably will skip the meeting after that because it'll be Christmas week.

Thanks everyone. See you in two weeks.


# Attendees

* Alex Beregszaszi
* Andrei Maiboroda
* Daniel Ellison
* Danno Ferrin
* Dimitry
* Guillaume
* Hudson Jameson
* James Hancock
* Martin Holst Swende
* Pawel Bylica
* Peter Szilagyi
* Pooja Ranjan
* Tim Beiko
* Wei Tang

# Date for Next Meeting: 4th October 2019, at 1400 UTC.
