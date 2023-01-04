# Ethereum 2.0 Implementers Call 68 Notes
Meeting Date/Time:  Thursday 2021/07/15 at 14:00 UTC

Meeting Duration: 1 hour

[GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/226)

[Audio/Video of the meeting](youtube.com/watch?v=-Bzq4s8Lr5E)

Moderator: Danny Ryan

Notes: Darkfire-rain


## Contents
[altair-devnet-1](#altair-devnet-1)

[client updates](#client-updates)

[altair](#altair)
   * release and testing
   * planning

[Research updates](#research-updates)

[some merge discussion points](#merge)

[Open discussion/closing remarks](#closing-remarks)


## Summary 

- Progress on the devnet will be discussed in the next meeting. 

## altair-devnet-1

### Devnet launch

**Danny:** Great, stream should be transferred, if your in the youtube chat you can let us know, here is the agenda, slightly mixed up things because we had a devnet launch this morning, it happened 2 hours ago, the fork happened about an hour ago, Pari you helped coordinate that, can you just give us and the people on the internet an update on the status.

**Paritosh:** Yes, so the altair devnet 1 launched about 2ish hours ago, and we forked epoch 10, we seem to still be finalizing, and hovering about the 80% participation rate, so we still seem to be figuring out some issues, but we are doing great.

## Client updates

### Prysm
**Danny:** Cool, great, we can discuss once we get to altair a bit of the planning stuff. Okay lets run into client updates, lets start with prysm

**Terence:** Hey guys, terence here, so the last two weeks we have been mostly working on optimizing altair, so mostly optimizing across the sync committee, receiver side of things, and we made decent progress on that. Unfortunately this morning with the launch of the devnet we had an issue where we were not able to propagate block to the peers, so it seems like something to do with the peering related thing, so we will give you an update once we figure it out.


**Danny:** Quick question, are you receiving blocks, or are you following the caniocal chain you just can't get your own blocks out?

**Terence** So what we suspect is that we had a bug in the sync validation pipeline in the pdp so we basically the sync committee which we should not be, because of that we started banning peers right away, so we don't have any new peers at the end other than that we are enhancing our slasher, other then that we are done with the eth 2.0 api implementation, so that is exciting as well, so that's pretty much it.


### Lodestar

**Danny**: Thank you, and lodestar
**Danny:** I don't think we have anyone from lodestar here, lodestar was on the devnet launch this morning, and they proposed the first block and it looks like they're following that. Other than that i'm sure they are working on light clients and other fun things.

### Grandine

**Danny** How about grandine, is that how you pronounce that?	

**Saulius**: It's actually pronounced grandina. We have been doing some small fixes and optimizations, and we have been working on the experiment that we talked about last time, and we are trying to run multiple forks at the same time ,and I have some things I want to talk about during the merge part of the discussion. That's all from me.
 
### Lighthouse

**Danny**: Thank you, and How about lighthouse

**Paul**: Hello, paul here, we are pretty much up to date with altair, working on merging some features, merging some front pr’s, we've also started working on optimizing altair, we've added one past method, and it seems to be doing well so far. WEve realized we have to change some metric and validation inclusion apis. And now we know if they have a timely source of information.

### Nimbus

**Danny** Thank you, and nimbus, 

**Zachary** we've had to develop the code in a hurry, so we are still trying to test it as an improvement, and there are very few missing features, and we still have a lot to do on the light client sync. And we have partially implemented committee sync.

## Teku

**Danny** Thank you, and teku

**Adrian** Hi, we've really been polishing off the altair stuff on the devnet, and the official one now, has been doing some profiling on that, making sure the api all align. And a bunch of testing around there has been the main thing. That's about it for us.


## Altair
	

**Danny:** Got it, thank you, and congrats on being on the devnet this morning.  And the first block, moving on, we will now start discussing altair. Alex, myself, and some others, spent a lot of time testing what came out in beta 1 yesterday. It sounds like everyone got those passes, I kind of hoped we would hit a corner case and trip you up but we didn't. We moved from alpha to beta, everyone had been on devnet at that point. Also jim as you all know did some analyses on the sync aggregator suggestion constant, and that's the only significant change from alpha to beta. For planning, two weeks ago we said we were gonna do a couple of devnets, which we did, and we said that if things went well we were gonna target the last week of july for upgrading pyrmont. As of this morning we have at least one client who still has some issues with devnet, so we are not 100% sure if we can hit that.

**Paul** I would just like to say that we are dropping our devnet notes soon.

## Research updates

**Danny** Ok moving on, are there any research updates anyone would like to mention.
**Danny:** Easy, so we did cancel a meeting this morning, but we do have some merge discussion points. Mikhail, would you like to go through them?

## Merge

**Mikhial** Yes, so the first one is a mixed hash for randao. And exposing for the bbm. 

**Adrian** I think the main concern I have right now is that we haven't seen the sync committee stuff working particularly well at all. 50-70% is the best we do. I think we know the problems, but I don't think we have seen it actually work. 

**Danny:** And when you say that you think we already know the problem we think it is a mixture of 1. Prysm is offline currently and 2. That choice of 4 rather than 16 so we were seeing non aggregators on some of the devnets sometimes.

**Micah**: So in the geth code base specifically 80 bits. They store it internally, as far as the header is concerned, it's just rlp so it can be up to 40 billion bits

**Danny:** so do we also kind of cut the spector out at its lengths by using a constant 32 bite size?

**Micah**: What would the dospecter be here?

**Danny:** Infinite, rlp encoded bite size.

**MIcah:** I think technically we already have that problem everywhere, when your rlp decoding you already have to deal with that, there are a bunch of rlp encoded quantities in the header.

**Danny:** You already need to have some limits

**Micah** I think by convention we just assert that none of them will be more than 256 bits, so i suspect that most clients decode under that assumption

**Danny:** Yes. Next, between the merge fork and the terminal pow block, whats on your mind

**Mikhail**: They could potentially be the case for merge happening in steps, the first step is the merge beacon chain. Next step is the actual transition.

**Danny:** So a weak checkpoint is really just something that has been finalized within the time period that you deem safe to load from. And you certainly could choose something on that range, unless deemed unsafe by our discussion. What do you see as an issue in using such a point?

**Mikhail** Yeah if it happens between the fork and the transition process,the nodes that start would have to somehow compute the total difficulty. We are not storing the total difficulty in the beacon state so it will not be presented in the beacon state. There are two options, weather we include the transition store, or we somehow prevent this checkpoint happening

**Danny** Alright I see what you're saying, I think the easiest solution is to once that fork happens, subjectivity states at the fork points, once the transitions finalize they only serve them after that point. One thing to bring up here is that there aren't super robust standards.

**Danny:** Does anyone else want to chime in on this discussion topic before we move on?

**Micah** If something does go wrong during that one week, what happens?

**Danny:** That has not yet been discussed.

**Danny:** Mikhail, did you want to bring up that last point, i can give the context since I proposed it.

**Danny:** So there's this notion of a terminal pow block, once you have a canaiocal chain going, that's the last pow block that needs to go in there. There's rules on what this can be. Currently that rule is that the terminal pow block must be greater than the total difficulty. That total difficulty is calculated prior and is a constant in the chain and so the beacon chain continues to be built. The Pos chian would then build from 10 minute ago, and essentially do a 12 minute reversion

**Dankrad**: Right so i think there should just be one block, we shouldn't try to select a later block, and if the beacon chain is offline then you're trying to get a higher service level for the transition time. So if either of the chains it should still work, but that's not true before or after, so why should it be true during the transition time.

**Danny**: Yes and I agree with you, and if miners can figure out how to take down the beacon chain they can mine for longer, and I don't think that's a good incentive.

**Mikhail:** Yeah, one of my concerns is that if we want to enforce the most  condition, we wil have to add more rules, and if we want to stop gossiping blocks about the terminal blocks, and the terminal block candidates so we will have to also introduce these restrictions for the block gossip functions

**Dankrad:** I mean that doesnt matter if they gossip as long as they dont, execute.

**Danny:** Well incorporated into what the execution layer sees as its caniaocal chain. Whether its gossip or not. The eth 1 client does not know the total difficulty currently. It is calculated dynamically at the beacon chain fork.  The override on the execution layer, just shows there is a block there.

**Dankrad**: That doesn't sound safe to me, because it is a raised condition, where there could be another pow block, and some people still follow it, and only later it is communicated that it is not valid. 

**Danny** Well it's an override on the fork choice, essentially its any pos block.

**Dankrad**: Yes, just saying there is a raised condition there. Because for example imagine someone is running this, and accidentally ends the transaction, their eth 2 client goes down, its not that unlikely, then all the eth 1 client connected to it would keep running it, which would not be safe

**Danny** Right, I see what you're saying, and i'm not necessarily claiming that it is safe, i'm just saying that the way that it works now, is the delivery of that pos block is the delivering of this is your fork choice now.

**Dankrad** And it feels like maybe the eth 2 client needs a way to tell the eth 1 client hey, this is the height at which to stop.

**Danny**: Right which it could a week prior, given the way it's configured, that's just the additional complexity.

**Micah**: I tend to agree with dankrad here, if the pow client continues on the pow chain for to long, eventually it will not be able to revert back to the proper transition, so if it goes down for half a day, which is not unreasonable, then you're stuck and have to resync everything.	

**Danny:** Right, and I mean each pow client has different values for maximum rework, but they are not incredibly deep.

**Mikhail** Right so we might probably need to communicate this transition total difficulty down to be a solution client, to avoid this kind of basis.

**Danny**: Okay, so intuitively, once the beaconchian is supposed to take over we should act as though the beacon chain is taken over even if there is a liveness failure.

**MIkhail** There could be a slight liveness failure, due to partitioning the pow network, if the block is not fully propagated.

**Danny**: Okay so i think we have a bit of work to do for these things, anything else on Mikhail’s points

**Danny:** OKay, saulius, you had since you wanted to bring up with respect to merge and your client investigations.

**Saulius**: Yes, so this was booked on top of my previous ideas of running the two run times, so we introduced a term called fork time, it is runtime that contains everything needed around a fork except the shared components. So basically a client was able to run multiple forks at the same time, so we think that this approach would be usable during the merge. The main motive is that during the merge there could be some terrible incident that  we may not have thought about and the code is not ready to handle it. So if client is  using 2 fork times to run altair, let's say we fork merge from altair, instead of forking from altair and hoping everything will go well, we can have two run times, which would have one running altair, to make sure there are no interruptions, and the other would be trying to do a proper merge. So if the merge is successful, then we can forget about it, and if it is not, then we can basically drop this attempt and try again, after we fix the cases that broke the first attempt. This also would decrease  the motivation for  bad people to try to do a coordinated attack because we will probably just say that we will try to merge as many times as needed for it to be successful. To me this just seems like a safer way.

**Danny:** So there is a lot there, one, i am excited to see someone experiment with multiple forks, but the second thing is most  clients don't run like this and it might introduce significant complexity if we try to run it like that, and make it a dependency on a fork, i think the main pushback that is probably worth pondering is that failure of a fork is probably hard to define, its probably very hard to codify, so you could have a social consensus where you run -- revert and go back to the chain that was still being run in parallel. More often than not, a failure in a fork would look more like emergency fixes and working through it and getting to a success state then an abort. And defining what an abort is might be difficult.

**Saulius**: Okay so i think i get your idea, but the key thing for me is that i saw that, it was mentioned in this call, that this fork is probably going to be the most complex fork in ethereum, so i dont know. Yeah, It brings complexity, for some clients it would be really hard to change to this approach, but on the other hand I see that it looks like it is safer.

**Danny:** Any other reactions?

**Paul** So is the idea to build blocks on the alt chain and the new chain so you basically double up what you were doing before? 

**Saulius** Yes, but this discussion is that clients are already doing a lot of competitions, and this would make it double competition, is that a bad thing?

**Danny:** Would be double computation, double database, and double bandwidth, which on our  resource constrained devices which there are mainnet validotrs on relatively resource constrained devices, I think that's certainly breaking a promise going from 100 to 200% in the stretch of a week or two.

## Closing remarks

**Danny:** Any other discussion points or closing remarks?

**Adrian**: Yes sync committees are already looking better on the devnet

**Danny:** Cool, thanks everyone for coming, we will patch it up and monitor it by wednesday. Congrats on the devnet launch, talk to you all soon.

## Attendees
* Saulius, 
* Danny, 
* Mikhail,
* Zachary, 
* Pooja,
* Adrian,
* Paul,
* Protolamba, 
* Ben, 
* Hslao-wei, 
* Parithosh, 
* Micah,
* Mehdi,
* Leonardo,
* Terence,
* Dankrad,
* Alex,
* Raul, 
* Nishant, 
* Lion, 
* Zahoor

## Next meeting
Jul, 29, 2021 at 1400 UTC
