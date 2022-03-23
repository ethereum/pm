# All Core Devs Meeting 132
### Meeting Date/Time: February 18, 2022, 14:00 UTC
### Meeting Duration: 1 hour 30 min
### [Github Agenda](https://github.com/ethereum/pm/issues/472)
### [Video of the meeting](https://youtu.be/Oo_Nnk3CdLA)
### Moderator: Tim Beiko
### Notes: Alen (Santhosh)

## Decisions Made / Action items
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
|132.1 | As a result, the v2 may be released with what we currently have. I think we've had enough feedback on that. We can simply release the V2 version on Monday and Tuesday, and then have a DevNet whenever we think it's reasonable to have with this new version open the following week. - Mikhail Kalinin.| [24.07](https://youtu.be/Oo_Nnk3CdLA?t=1449)|
|132.2 | Maybe the one thing I'd say is that if we can add something to the merge readiness checklist about confirming that we've removed the unauthenticated ports before, ideally like the public testnet or the release Kiln, but like the Goerli with that, it's probably worth noting. - Tim | [25.00](https://youtu.be/Oo_Nnk3CdLA?t=1508)|
|132.3 | PREVRANDAO to be without underscore - Tim .| [43.20](https://youtu.be/Oo_Nnk3CdLA?t=2577)|



## Chitchat:

**Tim Beiko**
* Hey, everyone.Hi, Gary. Hi, Greg. 

**Gary Schulte**
* Good morning.From here.It's good morning. 

**Tim Beiko**
* Yeah, from here. It's early morning. I think there's only two more calls before we change the time again. 

**Gary Schulte**
* 06:00 A.m. Is rough. 

**Greg Colvin**
* Which way does it change the calls? 

**Tim Beiko**
* you're like in the Midwest, right? 

**Greg Colvin**
* Does it get earlier? Does it get earlier or later? 

**Tim Beiko**
Later by 1 hour. 

**Gary Schulte**
* Later by 1 hour. I'll praise the Lord. 

**Micah Zoltu**
* The call stays the same time. It's you guys, that all just rearrange your clocks randomly. 

**Greg Colvin**
* Yeah, California, we're trying to get rid of daylight savings.That's crazy. If somebody went to the legislature and said, we need a new law that everybody is going to get up an hour earlier in the summer, the legislature would go, what the hell are you talking about?But instead it's like, oh, we're going to move the clock. 

**Tim Beiko**
* Oh, well, I know. Yeah. It's terrible. 

**Greg Colvin**
* That's my rant for this morning. 

**Tim Beiko**
* I tried changing the Coredev calls times two years ago.We tried having rotating times. 

**Greg Colvin**
* Oh, God. that was horrible. 

**Tim Beiko**
* Yeah, I know. I had to get up at, like, two or three in the morning a couple of times to go on these. 

**Greg Colvin**
* I just never knew what time they were. 

**Tim Beiko**
* Yeah. 

**Greg Colvin**
* Over, the years, I think we found this is the only bracket. If we start getting people from India, it's going to get really hard. 

**Tim Beiko**
* Well, I mean, we have people from Australia, and they just don't come. Right.And that's pretty bad. Yeah. 

**Micah Zoltu**
* I think this is the best option because you have a giant ocean between the biggest, mostly empty space on the planet,is overnight right now.So like the middle of the week where it's really late. 

**Tim Beiko**
* I'd call it the lease source option rather than the best. 

**Greg Colvin**
* We could have, like, a meeting in the most convenient bracket for them. 

**Tim Beiko**
* No one will show up. 

**Greg Colvin**
* No, I mean, two meetings on that day,and you'd only manage to get to one of them. 

**Tim Beiko**
* The challenge is you can't make a decision then. 

**Greg Colvin**
* Oh, I know. 

**Tim Beiko**
* Yeah.

**Greg Colvin**
* It will take three meetings to make a decision. 

**Tim Beiko**
* My dream, when I have time, I'll maybe work on that is to just, like, not use these meetings as a way, as a blocker to make decision decisions and move that whole process async. And you can,, still have calls and maybe you keep the slots, but more of, like,a breakout room /technical discussion.but, yeah, I would love if you didn't rely on YouTube live stream calls as the main way of actually making the decision.I'm fine with us having the call. I think there's value. There's stuff that's, like, higher bandwidth to discuss on a call,but then you could also have, like, if you have more topical calls, you just schedule them based on who's interested. And so if you do need Australians to get involved, then you find a time that works with them, but other things keep being much higher priority than me reorganizing how this whole process works.So unlikely to happen very soon. 

**Greg Colvin**
* Well, I better go get another cup of coffee so I'm not faced down on the keyboard. I know it's 09:00 a.m. Here, but I worked like an idiot.I have a friend in Australia, so when we work together, I'm up all night.He's trying to do something recursive in I don't know what functional language. 

**Danny**
* Hello. Hi, Debbie. 

**Tim Beiko**
* Yeah,, let's give another minute and we can get started. But, yeah, I think we have people from all the teams. I think this is the most on time. We've been across five teams. 

**Micah Zoltu**
* Do you have 1 minute to convince me that Noah is wrong? Danny go. 

**Danny**
* Yeah. So there is,, a beacon state at each slot,and there's a notion of Randall at each slot.There is a block at each slot, and that block at each slot is if nothing happened,it was the prior block. And similarly,if you read the state for any empty slot,it would be the Randal from any prior slot. So there is semantically that's definitely what's going on on the beacon chain.And now if you have a bunch of empty slots, and from the perspective of the execution layer,latest random, which is the opcode,, that's in there right now, would return the latest random, which is whatever the parent execution layer block is, which is essentially the N minus one, N minus two, N minus three, whatever, until you get to the most prior spot. And so you do have this notion even latest random also has this notion of finding what the most recent block was,and using that.And so essentially any skip slots in between, from the perspective of the latest random as well, is also that kind of like at or before. 

**Micah Zoltu**
* So,the beacon chain currently doesn't actually have empty slots. They just Port forward.The last issue. 

**Danny**
* There is a state transition at every slot. So if I go from end to end plus five, then there's a state transition at N plus one and plus two plus three. The notion of if I voted on a block at N plus one or M plus two in that empty chain, I'd be voting on the block of N, saying that is the head and there are accumulators that essentially do that as well.I could be convinced,otherwise.I do think that if you do have the notion of slots in the execution layer for these calls and you can return null or miss,then that also has the chance of much more error in transactions.If I'm expecting to get random and I hit that and I don't get anything,, then all of a sudden I can naively, my transaction might fail, or I need to do multiple queries and things like that. So I think that it adds complexity rather than otherwise, but I haven't thought about all the use cases people might use this for. 

**Mikhail Kalinin**
* Do we have time for this conversation right now? 

**Tim Beiko**
* Yeah. Can we, I guess, get started and then we might discuss that.As far as the Kiln stuff, does that make sense? 

**Danny**
* Yeah. 

## Intro:

**Tim Beiko**
* Cool.Okay,let me turn this on.Welcome everyone to Allcoredev 132. Let me share the link in the agenda here. A couple, of things today. One, there was a Goerli issue,, and I think it's still ongoing, so it's worth addressing that. But right after that, a couple of merge updates, some stuff on Kiln.There was some discussion about changing,the random versus difficulty,upcode in the it 43, 90, nine. And we have the Forks. We have the folks from Kurtosis on the call as well, who've been helping with testing for the merge, and they'll take a couple of minutes to walk through what they've been doing and see if we can schedule a more in depth testing discussion in the next couple of weeks. And then some Shanghai stuff with some updates on the, beaconchain withdrawals. And finally, there was a comment about one EIP, where we would just cap, the amount of transaction gas to a large integer value.So I guess to get started on Goerli, does anyone on the call have kind of been updated about what's happening? 

## Goerli updates:

**Tomasz Stanczak**
* Hey, yeah, we're on the call there, so, I see two validators down from POA or from Nethermind. We are investigating, multiple things. First of all, why we got the alert, so late, which is just 20 minutes ago after many hours.And I think Ronin's,note is down as well, but I'm chasing now.Everyone is down.We re syncing Nethermind and we'll see how quickly you can come back. We're looking also on our backup notes that we are running both gaff openeth nethermind style,and see if we can move the, signer key on our side there.And I don't have the latest snapshot yet,so I cannot tell each other. Validators are not signing at the moment. 

**Micah Zoltu**
* Got it.Is there only Nethermind down or are there other clients that are also down? 

**Tomasz Stanczak**
* I cannot tell. I think POA and the mine are down and I cannot tell about others.I think the drones might be down as well. And Afri said that he is rethinking as well.So you have four notes down out of nine, but then still refer down.It should be progressing, which means that probably there is the typical click problem of the branches split where validators, are waiting on two different branches and not signing because they're assuming it's not their order.That's the one thing that was suggested. I call the improvement a few months back, but, was dismissed as potentially with some security concerns I think Daniel is necessarily.Peter is reviewing that, and I think there are some concerns. 

**Tim Beiko**
* Yeah, I don't know, Michael, if I understood your question correctly, but were you asking whether the Nethermind operated node was down or whether if we knew that all the effective validators were running the same client the letter one? 

**Micah Zoltu**
* I'm curious if this is a client consensus issue or if this is just. 

**Tomasz Stanczak**
* No, I don't fix it, but still, we'll be investigating because both POA and Nethermind are running the none of my nodes. Okay, so we'll see.

**Tim Beiko**
* Got it. 

**Micah Zoltu**
* Does anybody know about any nodes early signer nodes that are down that are not Nethermind. 

**Tomasz Stanczak**
* So if we have nine signers, only two of them are running, on Nethermind, and the network would be progressing without. 

**Gary Schulte**
* Checking the consensus validator. It's the first I heard of the problem.It's still, pretty early here. 

**Fabio Di Fabio**
* I can say that our basic validator is up and running. 

**Tim Beiko**
* Okay, that's itself. Yeah. 

**Fabio Di Fabio**
* It's not producing the sock. 

**Micah Zoltu**
* Does the basic validator or anybody's validator give any hints as to what the problem might be other than just you can't find enough peers to reach consensus? 

**Fabio Di Fabio**
* We are investigating. 

**Micah Zoltu**
* Okay. 

**Tim Beiko**
* Yeah,so I guess we'll keep an eye on the Allcore chat for updates about this. Anyone else have,, anything to add up on this? 

**Peter Szilagyi**
* Okay, is it that we don't have enough sign ups to reach 50, percent?Or is it just a split?Because a split could be solved by rolling back one of the Tigers and just moving it to the other thing. 

**Tomasz Stanczak**
* I think that's why Offer is resyncing to, fix the split problem. And that's when Nethermind,is retyncing as well.
That's what you can do on Gas. I don't think you can, do that on Nethermind or open Ethereum. We don't have those, tools, but then maybe Infirra team could try it if you can get, in touch with them. I think EGS is on the Allcoredev channel, so, maybe that could help them. 

**Peter Szilagyi**
* The problem.We have all the sign ups and statistics, so we know what they are doing. But on girly, the signers aren't good reporting, so, nobody knows who is offline, which is on which chain can become a black box. 

**Tomasz Stanczak**
* And there's less visibility. I mean, there's stats cared in that, but I don't have access directly to each signer snapshot. Otherwise I'll be able to check, like who is on what branch. 

**Tim Beiko**
* There was a streaming problem, and YouTube didn't get most of this audio. But in short, to discuss the Goerli issue. we're still investigating the issue. We haven't found it, and we'll post updates in the Allcoredev, chat, and I'm sure people will share them on Twitter. Apologies.I'll try to make sure that we get the Zoom recording for the notes so there's a full transcript even though the video misses part of the audio.Anything else on Goerli? Okay, so next up, merge updates.,, I guess, first of all, maybe it's worth Perry going over the Devnet, that we launched and what the status is there? 

## Merge updates:

**Pari**
* Sure.Hey, so yesterday we launched a, new Merch Devnet Four. It's based off the Karen V one specs and we've had almost all the client teams taking part.I know that last night a couple more independently were able to sync up, so I think,, almost everyone has an implementation by now. I paste the link in chat with information on where to join. How to join.The only tooling that doesn't work right now is beacon chain, because our fork of beacon chain relies on Lighthouse. And yes, maybe you won't be able to get Lighthouse up and running, but that should be fixed soon.While,the network was reaching TTD, we did have multiple folks and different consensus layer nodes. Did observe different terminal block hashes. even, then the network resolved itself as expected and it's finalizing and working fine.Mikhail has just written a tweet with what the logic is for it to resolve itself.Again,to reiterate,there was no intervention done.This worked exactly as expected. 

**Danny**
* Did we induce the proof of work working? 

**Pari**
* Why did we have that Mario's computer was too fast. 

**Danny**
* That's great.Awesome. 

**Pari**
* Yeah, he just randomly started mining at some point and I think he,, was mining blocks so quickly it wasn't importing anywhere else. 

**Danny**
* Excellent.Very nice.

**Tim Beiko**
* And I guess, does this give us any kind of data or confidence about once we do this on mainnet? Like how long we want to wait until we consider kind of the merge,, complete?Because you mentioned, I think on Twitter,, it took overall like a number of minutes for this process to happen. Is that like roughly what we'd be expecting on mainnet as well, that after a couple of minutes the fork choice gets decided and we managed to finalize a block. 

**Danny**
* In normal conditions, I would expect it even on the order of a slot or a few, it sounds like because the resolution on Marius's end, because he was mining blocks so fast, there might have been portions in the network that were still importing blocks and that might have been the delay there, whereas that would be much more difficult to induce on mainnet. 

**Pari**
* So we have three folks on the network. Two of the Fox hit TTD with about like, 58 seconds apart, and the third fork was extremely behind. So the first two fork resolved themselves within a matter of a slot or two, I think. And the third fork was exactly like Danny said, the amount of time the notes took to sync up. 

**Tim Beiko**
* Right, got it.That's really helpful. 

**Danny**
* Nice.And so,I mean, assuming you have made that level participation on some fork and you see finality of a proof of work block. So on the order of two epochs is not only when I'd expect Forks to resolve, but also when, you know, things have gone really well or things are chaotic. 

**Tim Beiko**
* Cool. Yeah, that's really useful. 

**Danny**
* When we had the beacon chain launch,we wrote down what we expected to see and what we thought some of the bad things that could be over the course of the first mini epochs and probably doing that so that when we're watching and when others are watching, we can very easily digest what's going on. 

**Tim Beiko**
* Great.We have, the first Devnet up. We've also basically merged both PRS for Kiln v2. I'm curious,implementation wise,, how are clients tracking for, the V2 spec? 

## Kiln v2 updates:

**Danny**
* I think I saw Taku geth the authentication. So at least we have an implementation. Right? 

**Tim Beiko**
* Right. 

##Teku
**Maarek Moraczynski**
* We implemented Exchange transition, and we are progressing with authentication, but it is not full. Right yet. 

**Tim Beiko**
* Got it. 

## Besu
**Gary Schulte**
* Yeah.Basically, we're still actually a couple of PR away from,having Kiln in our main,merge branch and the two off stuff. We, have PRS.We're working on that.But we're not there, yet. 

**Tim Beiko**
* Got it. And Nethermind.Sorry.Did someone speak up? 

## Nethermind
**Andrew Ashikhmin**
* Yeah, Larry already did.I wanted to tell about Aragon. So we are the same as, Bezel. We have a few PR still left on Kyung V One and V Two is in progress, so I think the ETA is about two weeks. 

**Tim Beiko**
* Got it. Thanks.That's helpful. Maarek?

**Maarek Moraczynski**
* Sorry. We have exchanged transition, and we are progressing with authentication. 

**Tim Beiko**
* Okay.So I guess it seems like we're probably not going to have,, V2 across everybody next. Or maybe we'll have some of them next week. Do we think we want another DevNet next week running V2? Do we prefer to wait, an extra week after that to give clients more time? Or, just having another DevNet next week, even though there's not everybody, and then maybe having a good real Kiln in two or three weeks?I'm curious what people's references here are.

**Danny**
* The authentication PR is written in such a way that you can use the old Port if you're not ready,right?I believe so. In that case, I mean, I would suggest we begin to call it V2, put on the pressure to have these two done, and if you're communicating on an authenticated Port, you get there soon. But I think given that there's a handful of limitations,and that are complete and many of them work in progress,I think calling it, too, at this point is probably a good call.I also personally think even if, client teams aren't involved, which they probably should be, doing some weekly builds just to kind of get a feel for it and continue practicing the transition. Like a call. 

**Andrew Ashikhmin**
* Yeah. I have a question about, the ports. I think there was a discussion,, on this discord whether there should be a single Port for the engine API or two ports, or we should have, some kind of transitional period. So I'm not certain the Spec thing says that there should be two ports, but then on discord, kind of it was agreed that should be only one.Maybe we can do two ports during the transition and then disable the authenticated, Port.What do people think? 

**Micah Zoltu**
* Someone correct me is wrong here, but I think there's two separate discussions. One is there's the unauthenticated Port and authenticated Port before the merge. The unauthenticated Port should be removed in every client and make sure that happens separately.There's a discussion of whether there should be a separate Port for Http, versus W WebSockets, and that one would remain either one Port or two ports through the Merge. 

**Danny**
* Yeah. So on the former, I'd say the fact that there are two ports allows us to continue to do interrupt testing for the next month, even if people don't have authentication. But that the non authenticated Port for the engine API. I would say should be deprecated prior to the main net releases and say must, not should.I can go with Must as well. Martin. 

**Martin Holst Swende**
* Yeah,so I think they leave whether to have one or two ports for, Http versus website. I know for our geth it was quite a hassle to have it all work on one Port. If all clients or all El clients can handle that, that's great.I think we should just do that,some El clients have problems,with that I think we should keep them separate. 

**Micah Zoltu**
* Am I correct in the understanding that the problem was is that back in 2016 or whatever? When Geth was written originally, the libraries didn't support it seamlessly, but they now do so in Go. It's relatively easy these days. 

**Mikhail Kalinin**
* I can't say exactly what the problems were.Felix and renewed.we are not removing this Port an authenticated Port for the Kilns back, so the version 2 may be released with what we have currently is back.I think we get enough of the feedback on that, that. We can just release, the V2 version on Monday, Tuesday, and then,have a DevNet whenever we think it's reasonable to have with this new version open next week. 

**Tim Beiko**
* That seems reasonable. Maybe the one thing I would say is if we can add something in the merge readiness checklist about confirming that we've removed the unauthenticated ports before, ideally like the public tested or the I release not killed, but like the Guardian with that, that's probably, worth making sure we don't forget. 

**Mikhail Kalinin**
* Yeah, good,fine.

**Tim Beiko**
* I'll do this.Yeah, thanks.Was there anything else on the Kiln specs that people wanted to discuss aside from the 4399 random? Of course they will., do that next. But there's anything else before that? 

**Mikhail Kalinin**
* There will be minor updates to the spec, but they can be done after  v2 is released.This  is the strict subset of ETH methods. Instead of broad support of entire ETH namespace, and some minor removing these exchange transition settings. One  of the statements from, probably from this method. It's a bit misleading, but it's unsubstantial. So it will be done. 

**Danny**
* And to be clear, the restriction of a subset of E methods is going to just be the set that people are using, so that shouldn't break any functionality, right? Mikkel? 

**Mikhail Kalinin**
* Yeah, right.Exactly.On the outside, it just doesn't need to.I think it doesn't need any engineering. It may be just entire It name space and we just want this to be restricted on the stack level,not necessarily on the client's level. Got, it. 

**Tim Beiko**
* Anything else on the Kiln spec? 

**Micah Zoltu**
* Just a minor correction there. It may require some engineering for clients because ideally,, we want the chosen API endpoints in the namespace that are going to be migrated over to the engine API. We want to make sure they're well specified. And so because there is not consistency between clients, some clients may have to adjust some things in order to make them actually spec compliant. 

**Mikhail Kalinin**
* But how do we want to specify these methods?do we have like,I don't know one place where these methods are satisfied? and we'll just say that in order to be compliant with the Spec, you should implement the Spec as. It's described in this document.It has something like that. 

**Micah Zoltu**
* We do have the JSON RPC spec documents.It is not complete and it basically is the lowest common denominator at the moment, which means if three different clients return three different things, the Spec currently says your result will be one of these three things like this.Maybe it'll be null.Maybe it'll be zero, maybe it will be empty array or whatever. I do recommend for the methods that we Port over.We make sure we have much tighter specs before we go live for those methods. 

**Danny**
* Yeah, I agreed. I think any methods that service in there are subject to, we should all put some final set of eyes and see if there's any ambiguities there. 

**Mikhail Kalinin**
* Yeah. Okay. So I was just saying that no engineering is required on the assumption that these methods that I used are more or less unified and have parameters across the client implementation. 

**Tim Beiko**
* One other, I guess just an RPC comment or question is I know we had discussed like  adding the finalized status to a lot of the blocks related queries. I'm curious if any clients have implemented that, and if not, what's the milestone by which we what do we want to gate based on that.I guess.First, has anyone implemented kind of the finalized JSON PC endpoint. 

**Danny**
* Is that an additional Bull on a block or is that an additional endpoint where you can ask if a block is finalized? 

**Tim Beiko**
* It's a boolean flag, so that if you return a block, basically you can get, the last finalized one.And I think this was also,, ideally you would also want to have the unsafe tag. So this is, like. Yeah. 

**Danny**
* And we're working hard on that,safe,unsafe algorithm to be specified and, should make a decision on if and how to surface this. 

**Tim Beiko**
* Yeah. And I think we definitely don't need this for Kiln, but we probably want it once we fork the public testnet,, to make sure that like, you know, infrastructure providers and whatnot are, able to rely on these.The non consensus changes? I think that's probably the biggest in a way, even though it's not a huge. Yeah. 

**Danny**
* Additionally, I think we need to make sure we write about and communicate well about confirmations and finality in this new context. 

**Tim Beiko**
* Yeah.Cool.Anything else on Kiln or the specs?If not? Mikael, do you want to summarize the summary about the random versus difficulty upcode and the changes you're considering? 

**Mikhail Kalinin**
* Yeah, sure.I'll try to be short and clear.Okay, so current proposal,is to rename the upcode to difficulty upcode to rent them.And it has some, issues with this naming,, with this particular  name, because random is a bit abstract in the context and under the random name we use the exact, implementation of this random machinery, which is the Rendell currently, and of course this new random upcode after the merge, returns the randomness out. But, that is much less biasable than what's returned by difficulty in the proof of work. But anyway,it's visible.And now this Rendell machinery,using the Rendell machinery under the hood of random has,some security implications.Using the, Randall makes from the exact previous,previous block from the exact previous plot also has,some other security implications.And if we want to secure,random, in the future. So we will probably need,, a few different semantics of this method.We will probably need this instruction to accept slot number.So here we have the conflict.So, we have this random upcode that doesn't accept any parameter.And to have like a more secure random in the future, we will have to have another random of upcode that will accept Clotama as a parameter.And that's why the, question of naming real . 

**Danny**
* Estate has been why do you have slot parameter? 

**Mikhail Kalinin**
* That'S because,, you want your application to use exact render makes,from exact slots to give proposals less influence,, power in some circumstances. in the case if we use VDF, if we use VDF, from a certain spot which is not that far from the current moment.this is all about future compatibility. So, yeah, we just need this number for some reasons.Yeah, that's why the thought is to, use a different name. And Alex basically made a good suggestion. so let's just use the name this thing exactly what it is. This is the last Rendal. and we can just explain that Rendez has its own,availability property.Using the last previous Rendell also adds more security implications,and so forth. So,, that's the approach I think we should take. Just wondering what people think about it on the naming. 

**Micah Zoltu**
* One thing to add to that is this discussion is really just up naming. but the idea here is what we name it is most likely,, what solidity is going to name the Opcode and that's most likely what documentation and tutorials went under.Name it. And what we want is we want to make it clear to users that this is not a good source of randomness. You should not be using this to run a lottery on chain or something like that.In the future. We do want to add some things that will enable those features, but previous Rendow or whatever is not a good solution for that it is better than difficulty, so it's, iteratively better, but it's still bad. And so naming it just random is very likely to result in people thinking, oh, we've got a random number generator that is secure, we can use that. And that is very much not the case. 

**Danny**
* The intention here was to when you can essentially give you the best randomness and Harden it over time with other techniques.So is the intention. Now if you had a BDF to have two Opcodes and have one that is Randall and one that is Random or BDF Random, what do you do or do you call it? We could rename it again right now and rename it again. 

**Mikhail Kalinin**
* If we use like previndel and one day we have VDS and we agree that's true randomness. We can either use random or VDF random.Yeah, we could either rename it or, we can introduce a separate code if it will need to be introduced. 

**Danny**
* I do think that if we do Harden this and intend to Harden it, we should make it clear that if Randomness is hardened that this Opcode will Harden it so that applications know that if in the future there's better randomness, they get it by default here or we need to make it clear that we wouldn't because both of them have design. 

**Mikhail Kalinin**
* That one of the ways to make it hardened.One of the requirements is it might not be the case, but it might be the case that we will need this extra parameter.So what we'll do in this case it's not that clear.So we can't have two up codes called random, one with perimeter, one without it. 

**Micah Zoltu**
* Is there a, 1 minute description of the PDF solution that convinces me that it will actually be securely random? 

**Danny**
* You have to notice but you yes assume I believe in PDF you type in the input of Randall into a VDF the VDF is revealed later the assumption is that an, attacker cannot when they're deciding to reveal or not reveal have computed the VDS the output of the BDS and you have them revealed in the future. 

**Micah Zoltu**
* BDF based random works in general I'm curious how you would get that all into one off code. 

**Danny**
* No, I was just going to say naively they're many different constructions you can do with the VDF so the idea that you'd have a PDF output per slot is probably not correct you'd probably. 

**Danny**
* Yes, you type in the input of Randall into a VDF., the VDF is revealed later. The assumption is that an attacker cannot, when they're deciding to reveal or not reveal, have computed the VDS, the output of the BDS and you have them revealed in the future.Based random works in general. I'm curious how you would get that all into one off code.No, I was just going to say naively. Like there are many different constructions you can do with the VDF. So the idea that you'd have a VDF output per slot is probably not correct.You'd probably have one per epoch just because of the way you may or may not. So as I verbally explore the notion of just hot swapping this the semantics are likely different because the granularity is maybe not on a slot basis. 

**Micah Zoltu**
* Even it was on a slot basis. It feels like if you're designing an application to utilize that, you need to have two steps. Basically a VDF gives you a commit review where the review is guaranteed, but you need to do a two step process.It's not a one step, just read the random generator and you're done. 

**Danny**
* I don't follow that. The commit reveal is on the beacon chain level. and so the beacon chain would have these VDF reveals essentially. And so if you had it on basis, you could feed them into this random opcode in the same way. 

**Micah Zoltu**
* Right. But at the moment we don't know the distance that you need to declare you're making a bet or whatever you need to bet and then wait a certain amount of time that is longer than the fastest someone could get a PDF. Right. And so we don't know what that number is. And so we can't start advising people on using Randall.And so you really can't build an app today that uses Randall that will then seamlessly switch to using the hardened BDF version in the future. Because like the design of those apps. 

**Danny**
* Yeah. And as I think about it, the naive swap has a number of edge cases to think through. I would be fine calling it pre brand hours, something like that.I do think that it is important to continue forward with the inserting of this value into the difficulty parameter because almost every application of difficulty is bad randomness and if we put a zero in there, it likely breaks things. Sure. 

**Mikhail Kalinin**
* I just wanted to add that if we even add currently we add this randal that accepts the slots as perimeter. It may also increase the security for a bit. So it's not only about PDF, so this is like the solution to support legacy applications that utilizes difficulty as the source of randomness.And yes, the initial intentions thanks for the explanation was to Harden it over,the time,but it might have some issues,it might have some issues with this. 

**Tim Beiko**
* And if we do Harden it, we can always rename it.And I know that it's not.Like, trivial to do.
* But it's also not impossible, given that we're already doing it right now.Yeah.In the spirit of ideally moving forward on this, does anyone object? Previndo. 

**Danny*
* This is good. If people start thinking about what Rendell is, they will go to the spec and read about it and read security implications if they see random. So it's pretty clear that no security implications needs to be read it on. No,definition of this.machinery will need to be learned. So it's just random. That's also good in, terms of producing some term that requires some additional digging into the specs.And also considering that PDFs are not happening soon, the, remaining shouldn't induce huge complexity. 

**Tim Beiko**
* Okay, we're up to one final mythic in the chat. Do, we use an underscore or not? Historically, it seems that Opcodes do not have an underscore. I don't know if it breaks anything, but to be on the safe side, does anyone have. 

**Danny**
* I wouldn't put underscores in it.I have no problem. 

**Tim Beiko**
* Okay, so, prev Grandale,it is without. 

**Micah Zoltu**
* And someone has strong opinions.Otherwise,feel free to talk to, Mikael and me in this discord. 

**Tim Beiko**
* And can we timebox that so that we basically, it would be good if early next week when we have the Kiln v2 spec, we have this merged and like.Yeah. 

**Micah Zoltu**
* If you have strong opinions, contact someone within the next 24 hours. 

**Danny**
* Yeah, I think I would assume almost anyone with a strong opinion and then has touched us at all is probably right here. 

**Tim Beiko**
* Cool.Yeah, let's definitely make this final, when we release the v2 specs for film. Pretty next week. 

**Mikhail Kalinin**
* Yeah, sounds great. 

**Tim Beiko**
* Cool.anything else on this?Okay, next up, we have gallon from Kurtosis. their team have been working on doing, like, simulation testing for the merge. They've been working closely with all the time teams. do you want to take a couple of minutes to walk you through basically what you've been doing so far and, how clients can use what you've built? 

**Galen Marchetti**
* Yeah, absolutely.Thanks, Tim. Hey, everyone. We have been working with Paris and a bunch of the folks on the client that teams our product, Kurtosis. It allows you to spin up, multi client test nets locally. So,Kurtosis, we have a layer on top of Docker, and that layer encodes all the logic you need to tie the things together in a configurable way.we actually have Kevin on the line as well. He's been doing a lot of the deep engineering work for this and can dive into all the details. But the way it kind of works is when you run Kryptosis on your own laptop, you can run, a local network that goes from proof of work to proof of stake with the clients that you want to have. And we have some reservability tools in there you can debug,you know, when things go wrong with your particular client or connection between your client and other clients. And you can do that all in a fast iteration loop.So you have more chances to see what's going wrong rather than only waiting for the next merge net when that moment happens,and I'll, pass it over to Kevin for a little bit more details on that. 

**Kevin Today**
* Yeah. So basically, Kurtosis is a tool actually,I can just share my screen really quick. 

**Tim Beiko**
* Sure. Yeah. 

**Kevin Today**
* Okay.You guys seeing this? 

**Danny**
* Yes. 

**Kevin Today**
* Cool. So Kryptos is a tool to clay just, a client that gets installed by Home Brew or whatever. And the idea behind it is that you have these things called enclaves, which are sort of like isolated environments where you can spin up a bunch of different services and shut them down and manipulate them, and then under the covers that actually ends up as a Docker subnetwork, where we spin up a bunch of containers inside of the Docker subnetwork so you can think of like a little walled garden for whatever you want. So on top of Krystos, we have built what we call a Krythosis module.And this is a Docker image. This guy right here that runs a contained set of logic, which in this case is spin up an Ethernetwork,first an El network, and then followed by a CL network and add a whole bunch of tools and do bits of validation, like making sure that the El nodes are mining and the CL nodes are,producing blocks and everything is working gravy. So I actually,took the time to prerun this,before this,just because it takes a little while to wait for mining and everything to go on. But you can run this locally on your machine. And basically what will happen is we'll go ahead and do all the machinery necessary to create one of those enclaves right here.so I've created this each two enclave, and then I've fed in a bunch of parameters. So every module can pick in parameters.You can kind of think of it like a function. And this will allow you to configure the actual network that's getting started inside of Kitess. So specifically that allows you to configure the local net that is getting created.So once that gets fed in, Kirtosis is going to do a whole bunch of work and you can see everything that's going on right here. We're basically generating the El, Genesis data right here. We're going, ahead and adding the one El client, which in this case was Guest, which comes from the specification right here. We're waiting for Gas to get going. Actually,I set a couple of debugging flags here to make this a little bit faster.You'll, see where that'll come in in just a second. And then we get the CL CL client, which is going to get connected to the, guest instance, and then we get some debugging tools on top of this to, make sure our network is working. So the first of which is forkmont. So there's a fork month instance which is started, and connected to the network. So we can see that our one tech node is right here.We can see how slots are progressing. We can see which 

**Tim Beiko**
* We don't see your fourth one.We're still seeing your command line. 

**Kevin Today**
* Thank you.Let me go ahead and change that.Yes, that's work on cool. Yeah. So basically the module will return output just, like a function. You'll get back a bunch of output JSON format, and then I can just go to this fork Mon URL, and this is fork Mon right here. So technically, what this is, this is a fork Mon instance that is running inside of a Kirtosis enclave, which means inside of a Docker network with Kurtosis orchestrating all the necessary different parts, and then it is exposed to your machine on a Port.So you can see that I've got this ephemeral Port up here at the top, and then that allows you to see how the network, is going. And then, of course, if you had a bunch of different nodes and you'd see everything going through and we also have Grafana, we just added this or shaking out a couple of bugs with this. So if I go to Grafana, I'm actually going to see no data here, which is one of the bugs we're trying to track down right here. But if you start the network right away, you'll see the beacon head slot creeping up, and then you'll see the peer, count for each of the nodes. We think that, basically there's a retention thing that we have to fix because it seems to drop, data, like about a couple of minutes after the network starts.But once we fix that bug, then you're going to also have Grafana, showing up inside of here. And you can basically do a,bunch of manipulations with the Kirtuss's network as you work with it. So if we do kertosis enclave inspect and then the Ethereum network, you can see a bunch of information about the Ethereum network that's,inside of Kurtosis. One thing I forgot to mention is we actually spin up a transaction spammer. Thank you, Marius.That will constantly be sending transactions to the network just to make sure the network is actually doing work. And then you'll see a bunch of, these other services, here, like the CL CL client, the El client Forkman, et cetera. And then the local Port bindings on your machine if you wanted to connect to them and, make requests to them, as well as manipulate, them you can see like the discovery ports and everything like that going on.yeah, I think that's most of it. we have a couple of debugging tools like you can shell into a service by grabbing the enclave ID. And then if we wanted to get into this guy, then we could of course have a shell into the service to start messing around with it just like with Docker, you can do grab logs of services as they continue and then, the last thing is you can also dump the enclave logs and container inspect output to your um file system, which is very useful for debugging. So we've seen like as people are debugging and find issues inside of their crytosis network. One, you can give the repo by saying hey, my commands, my parameters that I started the module with are these which will allow say like if a client Dev was having a problem they could give to another client of they could be like hey, these are the parameters I started Ketosis with.This is how you Repro the problem. And then these are the logs and the container inspect output of everything that is going on inside of the Kryptos enclave. So yeah, it's kind of like a super lightning, speed overview of Kurtosis and the kurtosis module that we built. Any questions?Any thoughts? 

**Mikhail Kalinin**
* Can we have some pretty fun scenarios. I don't know. Two miners are minor separate two different Forks and just test this transition stuff like a simple example of it. 

**Kevin Today**
* You mean like scenarios?Kurtosis actually has an API, so the kurtosis engine is just doing whatever you tell it to like start the service, stop the service, repartition the network, dump these logs, et cetera. And modules are just packages of instructions to the Ketosis API. So you could actually wrap the module in basically whatever you want. So maybe an easy example of this is like showing how we use our internal tests.So I use this module, Cly here like this module exec command in order to start this module, with certain parameters. I just pumped this JSON file in. But if you wanted to test a very specific scenario, you could even just write like a go test here and then hook up to the Kutosa's engine and say hey, create me an enclave, and then in this particular case you'd say execute the module to do whatever scenario you want actually. And then that would be your predefined uh scenario. You could even run it as a unit test, you put it inside a CI.Does that kind of answer the question or am I missing? 

**Mikhail Kalinin**
* Yeah, cool. 

**Micah Zoltu**
* Sorry if I missed this at the beginning. Does this support all eight clients? Never mind death, Issu, Techu, prison, etcetera. 

**Kevin Today**
* So, we do have eight clients. I just want to make sure that they're the ones that you're thinking of.So we have Netherland, we have Gas, we have Bezu. We have,Lodestar, Nimbus, Lighthouse, Taco, and Prism. those ones you're thinking of. 

**Micah Zoltu**
* I was thinking of Eregon in that list as well, but that answered, my question. 

**Kevin Today**
* No, we don't have Eregon right now. 

**Tim Beiko** 
* Yeah, I guess. Would it be useful for client teams to have to book, like, a sort of breakout room to go into this in more detail and cover potentially some more complex scenarios? I have, like, one plus one in the chat, but I'm curious beyond Bay suit. Would other teams be interested in this? 
* Okay 

**Mikhail Kalinin**
* One last question. Is it like an alternative, to Hive or something complimentary? Yeah. 

**Kevin Today**
* I would say we're definitely complementary to Hive. So, Ketosis focuses a lot on spinning up the network, like the full network, via, Docker containers, rather than doing these specific, like the mocks and making sure that,you're really getting kind of a low level. You can do that with Kratosis, but you'd have to, handcraft doesn't have the tool set that Hive does. I think Hive is, like a network getter, test, if I'm not mistaken. So Kurtosis is more about, like, hey, you have the full network, and what do you want to do with the full network? 

**Mikhail Kalinin**
* Oh, yeah, looks like I get it.So this is like system testing versus Hype. Is integration testing or this kind of person yet?Cool. 

**Kevin Today**
* Yeah. To the breakout, session. We're totally happy to give folks onboarding. We can do that. Even if folks want to do that after this meeting, we can do it, schedule a date in the future as well, if that works better.We're totally happy, to give a rundown and dive a little bit deeper and all the different things that you can do with us. 

**Tim Beiko**
* Usually we get people to show up if we schedule it. I'm actually away next week, but I don't know if maybe, like, one week from now, basically Friday at the same time as this call. Would, make sense. I don't know if any or someone else can just host it, but we know that client teams can generally attend this time slot. 

**Galen Marchetti**
* Sure.Yeah, that works for us. 

**Tim Beiko**
* Sorry.Go ahead. 

**Kevin Today**
* I was just going to say it'd be great to meet all you all as well, because you probably see me, on your discord. I view briefs on discord. I probably been asking all, all you different questions about how your, client works as we've been setting it up, in Kryptosis. So great to meet you in person.

**Tim Beiko**
* I'll create a GitHub issue with just the information, for the session, and I'll try, to post a note also in the consensus here call agenda so that people that's the day before. So at least we can tell the CL teams that if they want to join, it's basically the day after their weekly call. 

**Kevin Today**
* Perfect.Sounds good.Sweet.Any other thoughts? Questions?on Kurtosis.Okay, yeah, thanks, guys, for coming on and obviously for doing all this work to help with testing the merge next. So, Shanghai stuff. Alex and Danny have put together an EIP to expose the beacon state group in the EVM, and have, I, guess pre EIP or idea about how to use that to enable beacon chain withdrawals. Do either, of you want to take a few minutes to walk through kind of the current EIP and how that kind of sets the stage for withdrawals? 

**Stokes**
* Yeah, I can do that.So, yeah, at a high level, this is for, beacon chain withdrawals, and there's at least two high level pieces. The first one is exposing the beacon state route. We can kind of walk, through EIP. I might even, just share my screen in a second and just kind of go through the EIP step by step.The second bit, is just exposing, well, using the stateroom to consume withdrawals in some way, and we, can share our thoughts on what we're thinking there after. so, yeah, let me share my screen and we'll just walk through the EIP.Okay.Can everyone see it?Yes.So, four, seven, eight. This EIP basically, takes the simplest approach to this.Several, of you have already given really good feedback, and I think that we're going to probably, deviate a bit from the approach here, but we could just walk through it briefly and, even still, there'll be questions and things I'm sure someone will want to weigh in on. So, to get started, there's, some constants that aren't super important. we'll come to them as we go through this. There are two sort of components to the CIP. The first one is supplying, the beacon state route, in each execution block, and committing to that in some way.Then there's the second bit, which is changing the EVM. so we'll start with the first bit, which is putting in the block the CIP suggests to essentially put it into the owners part of the block that essentially is enforced with the merged fork to be empty and we're just not going to use it. you also then commit to this via the owners hash like we do today. And then that is how you get into the block from there. essentially, with every block that you have, you have to say, okay, I'm going to write this to a special storage address that we define.This IP has, this key by block number. And if we just skip ahead, a little bit, there's comments by Vitalik and others to basically say, okay, we should keep this by slot number. At this point, I'm pretty set on this being the better path, and I'm currently working on getting the IP to index it that way. There is some more complication this way because if there are skips lost in the beacon chain, you may then have sort of an unbounded amount of work to do to write all the state routes that have been missing from the last execution block to this one. But yeah, I think there's ways around that and ultimately we don't expect too many skips less than mainnet.So it should be okay.let's see. I think the first thing I can ask is does anyone have any comments about committing to it in the blocks via the OMERS hash? There's a comment either on the PR or any magicians about using OMERS. Um hash in this way. Does anyone want to discuss that right now? 

**Danny**
* Well, I do want to say that if, you do fill in for listing slots, I think beacon block route all of a sudden makes much more sense than being considered. 

**Stokes**
* Yeah, right, yeah, exactly. So there's also that point too. This is also why I wanted to discuss this. There's like a bunch of little decisions since the state route, we'd also use the block route.There's some overhead, there because in my opinion, you mainly want to get to the state. And so then to get from the block route to the state route, it has a couple of hashes.But not the end of the world. 

**Micah Zoltu**
* So I can just lay out my argument for why, I wearily disagree with the way the owner's hash is being used. it's being used that way. It's basically always a list of one, if I understand correctly. And the reason for that, is important to the APS rationale is that it's the smallest change because we don't, change the layout of the block. I'm curious, for execution layer client devs, is it actually significantly easier to not turn that into just a hash rather than an array of one like an, RLP array of single item?If it's not actually easier in any extra plan, then I would prefer to do the right thing, which is just include a hash. There not an array of one item. 

**Stokes**
* There is one other bit there, which is just if there's other things we'd want to change in the block moving forward, then having this flexibility with this list of owners, let's just do that. Rather than having just like the owners hash becomes the block route or stay root and then that's that. 

**Micah Zoltu**
* Yes.Is it significantly easier to add items to this list versus just adding items to the block itself? Is there a meaningful difference there? I feel like in both cases you're changing the shape of the block, right? 

**Danny**
* Are you changing the shape of the block? I mean,a list is a list. 

**Micah Zoltu**
* Yes, but I believe the uh list is in the header.Right. This is a bit of a pedantic argument. One could argue that the block is just a list of values in fixed order, and whether we put an item in the middle or, at the end doesn't really matter.And again, I'm curious, from execution layer client devs perspective, is this actually easier, or would it be just as easy to have single? 

**Peter Szilagyi**
* What do you mean? Putting a value in the middle of the same at the end? So there's no RLP doesn't contain field names and it doesn't contain schema, so you cannot mess with anything in the middle. 

**Micah Zoltu**
* Right.So I guess the question is, in the future, let's say we use the Omar's like proposed here. So it's going to be an RLP list of items, and at the moment that we'll have one item, and then later we've got something we want to add to the execution block header. Is it easier to add it to that RLP list of things that we currently call owners, or is it just as easy to just put another item on the end of the block? Are those equally difficult? 

**Peter Szilagyi**
* I would say putting it at the end of the block is significantly simpler because you can just extend the block so you can just interpret it.Hey, there's one more item. We know what the type is, et cetera. In, the overs. Well, currently it's a hash. What happens if you want to put 33 bytes?Well, you cannot, because it's Typed that every item is 32 bytes, so the size kind of restricts you as to what you can put in there. 

**Danny**
* I'd be totally fine with adding a field instead of messing with a summer's list item. 

**Martin Holst Swende**
* From the client perspective, it's also the uh fact that if we add it as an extra item in the header, then the raw data makes it distinguishable what type it is without any further context. If we just put it as a hash uh where they previously were hashes, it will not be distinguishable from the previous type.From other perspectives, though, we talked about earlier that if, for example, a uh header is verified on chain, then, if there are such cases, then that will break if we modify the structure of a header. And I think that has been like a governing thought previously. I don't know if we care about that. 

**Micah Zoltu**
* My feeling on that is that I suspect eventually we're going to have to break that pseudo promise that people think was made. I think there is value in delaying how long it is until we break that promise, or lack of promise, whatever, or that assumption. but I, do think that we're going to eventually have to break it. 

**Danny**
* This is the assumption of the shape of the header hasn't won't change. 

**Micah Zoltu**
* Yeah, like so far, the shape of the header has.I think never changed, right? 

**Danny**
* Where did baseball go? 

**Micah Zoltu**
* Actually, you're right. We did just break that, didn't we? Oh, yeah. I'm okay with changing the block header shape then. 

**Danny**
* I was actually operating on assumption, too, and then I realized that basically changed it, right?Confirmed. Yes. 

**Peter Szilagyi**
* So that's the thing. As long as you're offending stuff. 

**Tim Beiko**
* Right, so we could live with the empty homers fields forever and just append stuff. And it's a bit nasty. 

**Danny**
* Yeah, we could take over the owners hatch. That's an option other than a Pend. Yeah, but that isn't an abuse of semantics. Uh. 

**Micah Zoltu**
* The OMERS hash does take 32 bites, so that would be nice to not have that just be wasted. 

**Mikhail Kalinin**
* Yeah, it does. 

**Danny**
* Compress. Well, it's not a zero at the merge, isn't it? 

**Micah Zoltu**
* No, it's not zero. 

**Mikhail Kalinin**
* It's like the hash of the empty list.  

**Micah Zoltu**
* My boat then is to use the owners hash for Beacon State Route. Use that position in the block header for Beacon State Route or Beacon Block Route, and just leave the owners an empty ROP list. Maybe at some point in the future, if we need a list of things, we can use the OMERS for that. 
* I agree.Barring an engineering reason not to. 

**Mikhail Kalinin**
* If we use OMERS cash, then we should drop OMERS at all.I mean, if we use OMERS hash for Beacon State or Beacon Block Route, then we should drop this Omar's list from the execution block body. 

**Tim Beiko**
* By drop, you mean put a zero rather than the RLP encoded empty list? Or by drop, do you mean change the block format? 

**Micah Zoltu**
* This is what Peter was getting at is that changing the shape of existing things is much more dangerous than just adding things on the end or replacing things with similarly shaped stuff. So having an RL empty list is one bite. So it's not too bad.And it's someone, who's currently, like, reading through and parsing what they know doesn't get hurt by that. like they'll just find an empty list, which is already the case in many blocks. Whereas if we change that to zero or something, then someone who's parsing it now is expecting an empty list and they're getting zero, which doesn't make sense. And their parser crashes or breaks or whatever. And so I think we should keep Omar's there.Maybe we rename it to unused or whatever. Omar's hash would become the Beacon State Route or Beacon Block Route in terms of, naming. And that's the position that would go in. 

**Stokes**
* Yeah, I think what Michael said sounds good. Just after hearing all the feedback. Does anyone, disagree with that? 

**Peter Szilagyi**
* Can I have a, weird question? 

**Tim Beiko**
* Yes. 

**Peter Szilagyi**
* I'm curious. I just want to check. Okay.The uncles owners, where are they stored? I mean, they're not part of the header and there is no notion of a block RLP.There's no such thing.As a block. 

**Micah Zoltu**
* You mean where they stored right now. 

**Peter Szilagyi**
* No, I'm curious. within the context of the CIP, it says that owners are, stored in the block body, but as part of the business, that's not the consensus thing.So you have the block headers, which has a consensus format. You have the Omar, which is just headers, a, list of headers, and you have the transactions, which is a list of transactions. But there's no that's completely it. These are three things stored for separately. 

**Micah Zoltu**
* Yeah, you're just saying, like the way this is Worded doesn't quite align with current state of, the world. 

**Danny**
* Yeah, that's a mistake. 

**Peter Szilagyi**
* So I still want to replace homers with some other content. Homers are kind of dangling things. So it's not a field somewhere that you just replaced. 

**Micah Zoltu**
* We're just putting a hash into the block header somewhere. Nothing else is going in. What was that? 

**Peter Szilagyi**
* Yeah, I was just saying that is the owner, cash, for example, in the middle of the screen, there's the number one entry. Set the value of Omer fields in the block. There's no owners field because there's no block. There's no notion of block. 

**Micah Zoltu**
* I think that means in the block header, because the block header does have an RLP list of header hashes. Right. Or OMERS header hashes. 

**Andrew Ashikhmin**
* Not in the header, only OMERS hash, but not the same.yeah, I follow now. Sorry. 

**Danny**
* I'm, not sure I follow. The owners list is in the block somewhere. Correct. 

**Micah Zoltu**
* Put.It over the network. 

**Martin Holst Swende**
* The block body contains two lists, a list of transactions and the list of headers. 

**Danny**
* Okay, so you can put anything in that list. Correct. 
* You explain. 

**Peter Szilagyi**
* So the block body is not a consensus. It's just defined as, something on the east network. But you could define it. 

**Danny**
* Understood. You could still take over that and utilize it for something else, especially if you're committing to it in the hash in the header. 

**Martin Holst Swende**
* Why do you need to have something on the side? 

**Danny**
* I'm not anymore. The idea was if there's this place that has a commitment in the header and we might want to grow the things that we want to shove in there, this is a place that could be used. 

**Micah Zoltu**
* But I'm not claiming anymore that that's a good place to be used.Yeah, if I understand Peters and Martin's argument here, this is basically just another argument saying we should put it in the OMERS hash because it will let us drop the network traffic of OMERS entirely. We just simply don't need to do that traffic. Pass that around at all. And so we 

**Peter Szilagyi**
* Simplified network, layer.If there's go homer, then you don't transfer anything. 

**Micah Zoltu**
* Got it?Not even an empty list. 

**Martin Holst Swende**
* We shortcut. We see that there's an empty list. We don't even query the network about it. 

**Peter Szilagyi**
* Interesting. Okay.Actually checks it on the owner hashes, the hash of the empty list, or the empty whatever country that we don't request it. So Gas doesn't do any network traffic. The only thing that costs for Gas is one, Byte per block in the database storing the empty, Homer City.But again, that would be a lot more painful to reinsurface and hack around. 

**Martin Holst Swende**
* So if we wanted to suddenly swap the, actual current header list, which we call the Omer list, to some other kind of structs, that would be a big pain in, the, downloader. Right Peter? 

**Peter Szilagyi**
* Yes, with a different site, that's very problematic.So you can change stuff as long as it kind of keeps the same shape, the same number of bytes. You can reinterpret fields, but once you change the size of the field, everything goes to, I mean, it just goes up. And in general, uh. 

**Micah Zoltu**
* So if we put the Beacon state route in the owners uh hash field of the header, is that going to cause a whole bunch of problems? Because you're now going, to see that that is not the hash of the empty list, and then you're going to try to query for owners or something?Or is that relatively easy to change? That happens. 

**Peter Szilagyi**
* It's time to hardwork. So I can just say that, okay, this hard fork block about block number X, the overs hash, is interactive. That's fine. 

**Micah Zoltu**
* Okay. 

**Peter Szilagyi**
* It's just in general, every single library code that people have written might get screwy. So, for example, one really nice example is that in Click, I, reinterpreted a couple of the fields. For example, I reinterpreted the minor field to mean some minor booking thing. And I know five years past or how much and people are still saying that, oh, why is the minor field all zero?How can I get the minor? So even five years down the line, it's causing problems. Obviously Click is roughly minor compared, to main active two stuff. But, reinterpreting stuff is a bit nasty. As long as we can just add it, that will be better.If we feel in my case, the Homer cash is consuming, too much, which I agree, we could maybe just add a specification, change, to allow that deal to be zero length. 

**Micah Zoltu**
* I feel like that would cause more problems than. 

**Martin Holst Swende**
* Trying to send the owners on the side instead of just putting them in the house. I mean, that's state route. 

**Micah Zoltu**
* It sounds like that's the direction we're heading. We're going to put them in the header. 

**Danny**
* Definitely very convinced that the abuse of the owners list does not bias anything except complexity. 

**Micah Zoltu**
* Do you believe that the complexity of replacing the future complexity and problems down the road of replacing the OMERS ash with the Beacon state route is worth the cost of having those 32 bites, extra sitting there doing nothing? 

**Peter Szilagyi**
* That's my thing. In my opinion, reinterpreting the owners cash is a huge pain in the ass. It's definitely not worth it. And if we think that 32 bytes wasted uh is a problem that we can just allow OMERS have to be empty because that way extending fixing the code to consider the empty owners have the same thing as the hash of the empty thing.is very simple. So if we want to optimize out those 30 device, that can be done much more simply without interpreting the state route, I just dumped it as the next field. 

**Micah Zoltu**
* I'm going to push back a little bit there. My experience with decoding a block header is the opposite. Having a thing with 32 bites in that spot would be relatively easy change, whereas making it so what was previously a fixed length field is now not a fixed length field adds linksity. This is partially because the way I was doing block header decoding because I only need two values from the header is I would just like skip forward this many bytes into the header and then read the thing that was at that location. And so we're starting to change the length of items in the header.It moves things around a lot. 

**Martin Holst Swende**
* So you can skip by bites during RLP instead of under very specific circumstances. Normally you have to skip by index, so you go to next item, next item in the left. 

**Micah Zoltu**
* Yeah. So after, the fixed length, if I were correct, it's been a while to step up to the header. But if I remember correctly, the first and items are fixed length, then you have some variables. 

**Martin Holst Swende**
* Well, they kind of are the fixed length one.They kind of are but they don't have to be, because if the header were to be extremely large, then the initial length of the header would be more practice. You're right. You can pick up a couple of first feels statically and absolutely everything but it's not like the robust um way to do it. 

**Micah Zoltu**
* Yes.What I would do is I would parse the first few bytes to get that length field off because that is dynamic. And then I would fix the length jump from there some distance in and then I would read the length of the next one and then skip that many ahead read the next one. Once I got back to some static deals again, I could jump big blocks. 

**Martin Holst Swende**
* That's the hacky way to do it. Which has worked.But it's not a robust way, to do it. 

**Micah Zoltu**
* Yes, but the happy way to do it is what, you do in solidity because you have gas. 

**Martin Holst Swende**
* Yeah, that's true. 

**Stokes**
* Okay, so I think we want to jump to the next topic. But just before that, it sounds, like what I'm hearing is that we went to append the state route to the header, as in Newfield, and leave the owners alone. 

**Micah Zoltu**
* I would like to discuss that more, but it can be out of this call. The two options sounds like we're either replace the owners ash with the beacon state route or append the state route to the end. I would like a little more discussion, but I don't want to consume this call.  Great. 

**Tim Beiko**
* Any other comments on that? 

**Danny**
* I don't know. Danny or Alex, click on this one.for a while we're thinking that the path to do withdrawals was first of all, you have this route to consume proofs against from accumulator and you consume withdrawal receipts to get the ease back on the execution layer. This would involve a pre compile in our thoughts and would involve a stateful premise because you need something like a bit field to say you've consumed receipts so they can't be consumed before. Given that, there are not stateful precompiles right now, and given that there is an option, an opportunity to pull some of the development and verification and testing work out of client team development, we're much more interested in pursuing a withdrawal contract.The withdrawal contract. Being able to call this opcode that we've been discussing about the beacon block or beacon, state route, taking a Merkel branch and taking a withdrawal receipt that consume that you approve and then consume the receipt and it stores and its storage whether it's been consumed or not. This would be one function withdrawal and has one interesting complexity to discuss. Ultimately, it needs to in the execution layer be able to send e that was previously deposited and issued on the beacon chain. This is a requisite for a pre compiled version of it as well, but it looks a little bit more funny coming from a contract.There's two options. One, the special contract. The special function can essentially pull from zero and send ease that is validated as in these withdrawal seats. The other would be to add a hard fork dump seemingly infinite into this contract. I think that is the most simple version.But then you have some accounting issues because you have this contract that has ten to the 30 of ethnic we're going to put something together and we can discuss this a bit more. Micah, I think there is massive gain to put this in a contract. I think it has a nice symmetry with the deposit contract and it means that it can be totally parallelize with all of the infinite things that we want to do with in the coming couple of hardcore because it is an independent set, they can write the contract.Then it is set.They can verify the contract, they can audit and test it.But anyway, let's talk about it soon. 

**Mikhail Kalinin**
* One small thing. It does mean that user will have to submit transaction to get their friends withdrawal. Right? 

**Danny**
* Sorry, what was the question? 

**Mikhail Kalinin**
* User will need to submit a transaction transaction to get the fence withdrawal. 

**Danny**
* Yes, and that is kind of a requisite. You have push for a poll debate here, but because people have smart contracts, that are expected to receive eating, I think it is most best, to be able to do that in a normal contract that has a normal transaction that has to consume gas. But let's move on, I would say, and we'll put a firmware proposal together very soon. 

**Tim Beiko**
* Yeah.Thanks, for sharing.Alex, you wanted to discuss, EIP 48 three, which limits the transaction gas to the 60 three minus one. 

**Alex B**
* So this is similar to another EIP we had discussed half a year ago, setting a limited amount and on that's kind of agreed to do multiple smaller EIPS for other fields because initially we had quite large EIP, um 1985 which tried to set bands to every single field in the transaction and also a lot of instructions in EDM. instead of that, we pulled out, smaller changes. So the non limit was one from last year and this one is only concerned about the gas limit filled in the transaction. And this proposed limit of 63 minus one can be applied, retroactively with because due to how the gas field is validated, currently there never has been a possibility to have arbitrary large limits. So this doesn't need an actual hard work.There's one, added benefit.The main benefit is that of course this field is now 64 bits. Calculations are much nicer and in fact most of the clients already do this implicitly.the reason we propose six four is to have space for assignment, aka this number can be maintained as a sign number and checking whether something run out of gas is simple. Check against is the limit less than zero.And added benefit next to this is we could actually get rid of the call depth limit. there's an explanation, why on the discussion, URL. But lastly there's also a proposal to pay if not due to the 63, but rather two to the 31, because in that case the customer could be regular number in JavaScript as well. 

**Micah Zoltu**
* I think that's I believe the two to 31 also gives us some benefits with regards to stack depth, doesn't it? Wasn't there something brought up by this, Livia? 

**Alex B**
* Yeah, I need to run the calculations again, but we run it with 63 with the 100 gas. minimum cost for any call. I think even the 31 has the same effect on the call deck, but I'm not entirely sure. 

**Andrew Ashikhmin**
* Well, Erica and I think, guest already implement if 48 or three. so that would be a codification of a defective practice. 

**Tim Beiko**
* Do any client teams have an objection with this?Okay, does it make sense to do like last time to just move it to last call and then check in a couple of weeks? Oh, It's Still A Draft, so I Guess You Can Move It To Review Before Then. Move It To Last Call, But Then Check In A Couple Of Calls.If Crises, Have Implemented It And Then Move It To Final And We Can Also Add It To This Spec, I Think, Alex, You Actually Added The Other EIP, that We Use To Cap.What Was The Other One? I'm Lucky On The Number. Anyway, Sorry. Yeah, I Forgot. But We Did Tap Something Else Recently And Kind Of Retroactively Applied From Genesis.And I Think You Added That To The Execution Specs, Alex, so I Think We Should Probably Add This At The Same Place And Move It To Review And Then Move It To Final When We Have Teams That Have Implemented It. 

**Alex B**
* In The Specs. Actually, It Wasn't Just A Non In, The Execution Specs Repo, But They Check Against EOA. 

**Tim Beiko**
* Oh, Right. 

**Alex B**
* Yes, that Also Is A Similar Case. Now, I Think this 63, Bits That Is Already Implemented Practically In Every Client.But I Guess, Mica, If You Want To Fight For The 31 Bits, Then You, Have To Pick That Up.

**Micah Zoltu**
* I Was Going To Ask If Any One Is Strongly Against 31 Bits. If Not, I Can Just Debate, With Alex Out Of Band, And We Will Just Choose Whichever One The Two Of US Agree To. 

**Andrew Ashikhmin**
* I'm Against It Because It's Already Implemented As Three Bits, So, Why Reimplement It. 

**Micah Zoltu**
* Currently In Guest And, Eregon, It's 64 Bits Or 63 Bits Minus One? 

**Andrew Ashikhmin**
* So Currently The Maximum Is In The E. It's Two To The 63 Minus One, Both In Gas And Aragon, So I Would Rather Leave It As Is. 

**Tim Beiko**
* We're At Time, But I, Saw That Gordy Is Back Up. I Don't Know, if. Thomas, You Have Any Quick Comments You Want To Share Or Anyone Else? Gordy 

**Tomasz Stanczak**
* Touching The Window.It Was Minimized, for, Now I Can Celebrate It Back Up.I See That In, The Note Key Was The First One Signing After The Break, So I Just Need To Confirm With Monica And Matteos Whether It Was The, Note That We Are Rethinking Or We Just Moved The Key To Somewhere Else While The Other Body Daters Are Coming Back As Well, And We'll Just Reconfuse More Time. We Have, Already Scheduled Monday Call To Check Off The, Alerting And The Note Be Here. 

**Tim Beiko**
* Cool.Thanks For Sharing.Anything Else Anyone Wanted To Cover Before We Go?Cool.Thank You Very Much, Everyone. And I'll See You In Two Weeks. 

**Micah Zoltu**
Bye Bye. 


---------------------------------------

## Zoom chat:
* lightclient:	gm
* Tim Beiko:	gm!
* Gary Schulte:	Gm lightclient!
* Tim Beiko:	https://github.com/ethereum/pm/issues/472
* Micah Zoltu:	Apparently you took more than 1 minute Danny.  😬
* danny:	not kiln relevant, imo
* danny:	renaming RANDOM to something else could be (?)
* Mikhail Kalinin:	RANDOM relevant
* danny:	I took the “convincing you” part more serious than the 30 seconds part. sorry
* danny:	!
* Micah Zoltu:	😆
* Mikhail Kalinin:	all good on my end
* danny:	additionally in Kiln updates, would like Pari or someone else to give a quick status on the new devnet
* Tomasz Stańczak:	stats.goerli.net
* pari:	https://devnet4.themerge.dev/
* pari:	https://twitter.com/mkalinin2/status/1494590871366479875
* danny:	woo!
* danny:	haa
* Mikhail Kalinin:	yeah, it’s a matter of all validating nodes have processed terminal block — once it’s done transition is immediately resolved
* Mikhail Kalinin:	then wait for finality and we’re done
* pari:	If anyone wants validators on devnet4, lemme know
* Tim Beiko:	https://github.com/ethereum/execution-apis
* Jared Doro:	Yeah I will be working to finalize the sepc this weekend.
* Tim Beiko:	The JSON RPC one, Jared?
* Jared Doro:	Yeah
* Tim Beiko:	Nice!!
* danny:	clearly, the methods *work* right now… gnerally
* danny:	great work on kiln everyone!
* danny:	I like just naming it LATEST_RANDOM
* Micah Zoltu:	I like `PREV_RANDAO`.
* danny:	LATESET
* danny:	LATEST!
* Micah Zoltu:	It isn't the latest.
* danny:	LAST implies “final”
* danny:	right prev is good
* Jamie Lokier:	Call it INSECURERANDOM :-)
* Alex Beregszaszi:	Once we have VDF, will randao be dropped?
* stokes:	the vdf is just layered on top of the RANDAO construction
* danny:	right
* Tim Beiko:	RANDOM2
* Alex Beregszaszi:	So both will be available?
* stokes:	the VDF can just be seen as a way to strengthen the RANDAO output
* stokes:	it would like like the same thing
* Tim Beiko:	My 2 gwei is that describing “what it is” is probably better than “what we expect it to do in the future”
* danny:	PREV_RANDAO seems reasonable. but then “what is randao” is likely the first thing a new reader thinks
* Tim Beiko:	They google it :-)
* Alex Beregszaszi:	There are no underscores in instruction names 🙂
* Micah Zoltu:	That is great, because they are more likely to read about how it isn't random.  :)
* Tim Beiko:	Could argue the same about DIFFICULTY
* danny:	lol
* danny:	wtf is that
* Tim Beiko:	@Alex, is that because it’s impossible or by convention?
* Alex Beregszaszi:	It has been the practice so far
* danny:	PREVIOUSRANDOMDAOCONSTRUCTION
* Micah Zoltu:	Convention.  Every opcode has no underscores right now.
* danny:	FROMTHEBEACONCHAIN
* Alex Beregszaszi:	PREVRANDAO then
* danny:	:thumbsup:
* Tim Beiko:	PREVRANDAO
* Fredrik:	yeah
* pari:	Bonus points for the first client team to use kurtosis in their CI
* Micah Zoltu:	Is there a Docker Compose/Stack file and/or generator for running EL+CL+Validator?  Something for mainnet + testnets?
* pari:	We have it for devnets, found here: https://github.com/parithosh/consensus-deployment-ansible/tree/master/scripts/quick-run/merge-devnets
* danny:	some work over here too https://github.com/z3n-chada/ethereum-testnet-bootstrapper
* danny:	still wip
* pari:	If you just want to generate genesis data for a merge testnets, you can use this docker image: https://github.com/skylenet/ethereum-genesis-generator
* Micah Zoltu:	👍
* danny:	network partitions, latency, etc
* pari:	All the Geth nodes added on the network are mining by default, So just running more Geth nodes means you have multiple miners
* pari:	(I mean geth nodes on kurtosis)
* Tim Beiko:	Would it be useful for client teams to have a deep dive session in Kurtosis in the next week or two?
* Karim T.:	+1
* Galen Marchetti:	We do have SDK for doing hard/soft network partitions from within go-test (or cli interactive shell) and can add latency to the feature set as well
* pari:	All the client teams used in merge-devnet-4 were sanity checked with kurtosis beforehand,  so we were relatively sure the devnet would work without issues.
* Karim T.:	Yes for Besu
* Micah Zoltu:	Link?
* Tim Beiko:	https://github.com/ethereum/EIPs/pull/4788
* Micah Zoltu:	https://eips.ethereum.org/EIPS/eip-4788
* Tim Beiko:	Would the field be renamed?
* Tim Beiko:	*fields
* Alex Beregszaszi:	I actually wanted to comment on the discussion url that we could also introduce a “system contract” (aka code at the address) to read the storage and return the value, instead of an opcode.
* danny:	right, we were thinking about that recently as well
* danny:	then you can handle skip slots in a more algorithmically optimal way instead of needing one write per slot
* Marius Van Der Wijden (M):	i overslept -.-'
* Tim Beiko:	gm@
* Mikhail Kalinin:	and we can expand this storage to keep other consensus data in the future, like randaos etc
* Galen Marchetti:	Hey all - Kurtosis team will hop off. Will coordinate on discord to get the right meeting set up for the information session!
* Jamie Lokier:	+1 agree with regard to the type being clear
* Ansgar Dietrichs:	Sounds like the omers list can just completely be dropped then
* Marius Van Der Wijden (M):	Should this change go in with the merge?
* Mikhail Kalinin:	I think no
* Marius Van Der Wijden (M):	👍
* stokes:	i’d say shanghai just in terms of overhead to actually impl and test
* Mikhail Kalinin:	the less changes the less complexity for the merge
* Alex B.:	the block header part could still be part of the merge, without expoaing it to the evm
* Alex B.:	*exposing
* Tim Beiko:	Is there a benefit in doing it?
* stokes:	it could but: “the less changes the less complexity for the merge”
* Alex B.:	changing the block header one fewer times
* Tim Beiko:	Going to time box this in ~5 mins so we can cover the last topic :-)
* Tim Beiko:	@Alex, is ~5 mins enough to discuss the txn gas cap?
* Alex B.:	sure, it is tiny
* Jamie Lokier:	Same way as 32-byte empty codehash and empty storageRoot are replaced with single-byte empty list in the SNAP/1 protocol.
* Micah Zoltu:	I like precompile.  I dislike special contracts.
* Micah Zoltu:	Can we put the special contract in the precompile numberspace?
* danny:	yes
* Alex B.:	There are other options from just minting infinite amounts. Could be synced at the beginning of the block.
* Mikhail Kalinin:	PUSH is better IMO but let’s discuss
* stokes:	push is much more complex than pull
* danny:	push isn’t tractable imo
* danny:	destination contracts consume gas
* danny:	and can have failures
* danny:	so you have to have pull to deal with failures
* danny:	so if you have push, it’s additive to pull
* danny:	which is way more complexity
* danny:	and the gas consumption problem is still a problem
* Ansgar Dietrichs:	I think it is unfortunate as is that the deposit contract messes with correct ETH accounting. Would like to fix that in a future fork, rather than make the accounting situation worse with an infinite ETH contract. Better to go with a system contract / precompile that can mint ETH imo
* Mikhail Kalinin:	One issue with pull is storing unconsumed receipts on the beacon chain. This is what push can simplify
* danny:	you don’t need to do that on pull
* Tim Beiko:	+1 to Ansgar
* danny:	you just need an accumulator
* danny:	the complexity of what client devs need to do and test goes up quite a bit if you don’t have a contract balance to draw from
* Micah Zoltu:	We could add a precompile for "mint ETH" that just has a restriction that only contract at address X can call it.
* danny:	I like reducing complexity as much as possible but won’t die on that hill
* Micah Zoltu:	Then the precompile portion is simple, and we can parallelize the contract work.
* stokes:	@ansgar would you rather have “cleaner” accounting or room for something like 4488 / mini-danksharding in shanghai?
* Tim Beiko:	A happy medium and potentially slightly delayed Shanghai :-) ?
* Mikhail Kalinin:	I was thinking about new Withdrawals operation on EL side and process withdrawals in protocol. But it’s the complexity and additional burden on client devs. Though, may be a simple and clear solution with much less things to reason about than with precompile or a contract that mints ETH or holding infinite amount of ETH
* Tomasz Stańczak:	nope
* Gary Schulte:	Just noticed our goerli validator is moving
* danny:	this is an extremely minimal EIP for clint devs if it is a special contract + (essentially) infinite supply behind it. It goes from near zero to moderately substantive wrt dev and testing if you go the other route
* Tomasz Stańczak:	goerli back up
* Mikhail Kalinin:	Accumulators makes users to store  and probably update proofs to old withdrawal receipts. Otherwise, there is a risk to lose them (thou archive nodes may help here)
* stokes:	that’s why we want to keep all beacon roots (rather than just the latest) in the state somewhere
* Ansgar Dietrichs:	@stokes I would be fine with a more hacky solution for Shanghai if it gives us room for mini-danksharding. Would still prefer an "accounting-consistent" hack like the "mint ETH precompile only the withdrawal contract can call" solution Micah proposed
* stokes:	yeah i’ll think about that direction a bit more
* danny:	I don’t know if you need another pre-compile if you go that route
* Mikhail Kalinin:	Yeah, a kind of call to a “kernel” function
* danny:	blocks already “mint” each block
* danny:	it just needs special logic that 0xWITHCONTRACT can send without having sufficient balance
* Ansgar Dietrichs:	Ah, that might work
* Jamie Lokier:	I see Goerli came back a few minutes ago too.
* lightclient:	bye!
* Fredrik:	bye!

---------------------------------------
## Attendees:
- Tim Beiko
- Danny
- Andrew Ashikhmin
- Ansgar Dietrichs
- Martin Holst Swende
- Barnabe
- Daniel Lehrner
- Fabio Di Fabio
- Fredrik
- George Kadianakis
- Giuliorebuffo
- Jose
- Karim T.
- Lightclient
- Marek Moraczynski
- MariusVanDerWijden
- Micah Zoltu
- Mikhail Kalinin
- Pooja R.
- Peter Szilagyi
- Trenton Van Epps
- Tomasz Stanczak
- Somu Bhargava
- Lukasz Rozmej
- Pawel Bylica
- Dankrad Feist
- Sam Wilson
- Alex Stokes
- Justin Florentine
- SasaWebUp

---------------------------------------
## Next meeting on: March 4, 2022, 14:00 UTC
[Agenda](https://github.com/ethereum/pm/issues/481)


