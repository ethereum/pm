
# Ethereum Core Devs Meeting 116 Notes



### Meeting Date/Time: June 25, 2021, 14:00 UTC
### Meeting Duration: 90 minutes
### [Agenda](https://github.com/ethereum/pm/issues/337)
### [Video of the Meeting](https://www.youtube.com/watch?v=uhvhfxiC-NA)
### Moderator: Tim Beiko
### Notes: Golden Gringo

-----------------------------

## **ACTIONS REQUIRED** 
Set a block number for London fork.


## **DECISIONS MADE**
Using code hash rather than code size: [Video Reference 1:20:00](https://youtu.be/uhvhfxiC-NA?t=4799)



-----------------------------

Moderator: Tim Beiko

# 1. [London](https://github.com/ethereum/eth1.0-specs/blob/master/network-upgrades/mainnet-upgrades/london.md) Updates
## i. Ropsten Fork

**Tim Beiko**

* Hi everyone, welcome to all core devs 116; a couple things on the agenda today, the first of which is just going over the Ropsten Fork that happened two days ago now.
* High level, I think it went okay.  We had the fork, it took a couple minutes to find the block on Ropsten after, because I think a lot of the old mining power didnt switch over. Luckily at least Besu had a miner and they mined the first bloack a few minutes after.  Everyone was on the same chain after that, I think there was one bad block mined on the old chain and that was it.
* There was a small bug in the forkmon software which made the hashes shown on forkmon, although they were all consistent on forkmon, they were different from everywhere else, which was also all consistent and we found that one of the underlying libraries that calculated the block hash on forkmond did not have London support, so it got to a different hash.
* But that aside, eveything seemed to work well.  I know the Besu team ran a pretty big spam test on the network yesterday, they ran the spammer for like 12 - 15 hours.  We go the base fee up to thousands of GWEI and then they shut it down and it went back down to its minimum value where i think its sitting now.
* We had people send 1559 and non 1559 style transaction.  I had somebody kinda deploy a smart contract, add some storage slots to it, clear those storage slots and self destruct the smart contract and that seems to have gone well and the network hasnt split so, 3529 seems like its implemented correctly across the clients.
* The only kind of odd thing i've seen, two odd things, one was Vitalik mentioned that the kind of distribution of the block gas usage was a bit odd, where there were a lot of blocks that were 80% full, and I think somebody looked into that and it seemed due to how the transactions from the spammer were batched, and the gas cost used by those transctions.
* And then finally somebody posted, yesterday some transaction that they said worked before and doesn't work anymore.  I dont think anyones quite looked into that yet.  Thats kinda all ive seen over the past two days I dont know if anyone wanted to add anything else?

**Gary Schulte**

* Thats a pretty great synopsys.

## ii. [Testnet Stress Tests](https://github.com/ethereum/pm/issues/341)

**Tim Beiko**

* Thanks.  Theres been stress testing on Ropsten.  I feel like we've kinda done that pretty extensively already.  I know Marius, you also wanted to do it which your tool which is different from Besu, do you have any updates or just thoughts on that?

**Marius Van Der Wijden**
* I already sent some transactions today, I don't know if it would make sense to do it together, so we have a huge chunk of transactions, but in general I dont know, we've put the network through way more than mainnet

**Tim Beiko**
* Yeah, I guess we could probably run it for like at least an hour with the two of them together.

**Trenton Van Epps**
* I remember you pointed out that it looked like the base fee was updating outside of the 12.5% did you look into that?

**Tim Beiko**
* Yeah, it was Peter who pointed this out.  You shared some base fee had gone from like 240 to 370.  I don’t know if you have more thoughts on that?  I’ve looked at several blocks and I couldn’t find something like that

**Péter Szilágyi**
* So, I only saw it on that website, but I don’t know whether it could be for a couple of blocks, so I don’t know what happens if there’s a rework of say one of two block, and that could explain if one side pushes the base fee up, while the other side pushes it down.  I don’t know how these rules are handled by that website, so it could just be a fluke of that website.

**Marius Van Der Wijden**
* The website should calculate it correctly, I think it calculates the base fee or it takes the base fee directly from hub block, from the block itself.

**Péter Szilágyi**
Yeah, what I mean is that if you report the base fee per block and as the second number and then there’s a rule that pushes it in the other direction…

**Marius Van Der Wijden**
* You’re right… 

** Tim Beiko**
* I’m curious how the different clients are feeling about deploying this on mainnet.  The people want to potentially set a block now.  Do we want to wait?

## iii. [London timing / difficulty bomb impact](https://github.com/ethereum/pm/issues/245#issuecomment-866193842)

** Tim Beiko**
* It seems like we are going to start seeing the impact any time after the first week of August.  
* If we feel like we want to see more of the  networks fork and we’re willing to wait a bit later, then the impact is we’ll see something between like 20 to maybe 50 thousand blocks in the new period of the difficulty bomb before it gets reset, so I’m curious what are peoples thoughts are about that.  How confident do they feel about London?  Do we want to see more before we pick a block or are we comfortable doing that right now?

**Péter Szilágyi**
* One of the catches with testing 1559 on testnets is that essentially if you look at Ropsten the base fee is zero or roughly around zero
*  And if you do a quick scan over Görli or Rinkeby blocks, we will kinda see the same thing where they are less than 50% full which means that if we ask miners to double the block limits, they will be a quarter full.  So essentially in both test networks we expect the base fee to drop to 7, so none of the test nets will be a realistic scenario for mainnet.

**Gary Schulte**
* Do you think that it was not a successful test even in the context of the spamming that is going on and is still planned?  Were definitely going to see blocks over 50% full, it would be contrived, but we’ll see that case.

**Gary Schulte**
* Does the call have to be made on an all core devs call?  What about next Friday instead?

** Tim Beiko**
* I think if we do that, we’ll probably have to reconfirm the block anyways on all core devs.  I think its kinda the main way that everybody hears about it.

**Péter Szilágyi**
* It doesn’t really matter if it will take a week.

**Yuga Cohler**
* One question I had was, are the clients planning on doing one more release before mainnet fork?

** Tim Beiko**
* They have to, but I guess is your question more about features?

**Yuga Cohler**
* Yeah, there were a couple of things, like there was a bug in OpenEthereum with the Eth call method and Marius and I were talking about, there may have been a regression in geth for tracing contract internal transactions.  
* So there were just a couple of things, it would be nice to get in before the fork.

**Artem Vorotnikov**
* Don’t use open Ethereum, move to Aragon.
* OpenEthereum is deprecated.

**Micah Zoltu**
* OpenEthereum plans on being London compatible though right?

**Artem Vorotnikov**
* Yes, but it will be the last hard fork.  Basically it’s just to support the transition.

**Łukasz Rozmej**
* Similar with Nethermind, we don’t have everything yet implemented for the RPC for London, there’s still some things still being revised and there are some other unrelated features that we will be releasing.

**Tim Beiko**
* So would two weeks be a realistic amount of time for the different teams to both fix any bugs, or add any missing Jason RPC calls, and then also have that release contain a mainnet fork block. 

**Dusan Stanivukovic**
* Yes it seems doable.

**Péter Szilágyi**
* Yeah so that currently is pretty stable, we are not aware of any huge bug.  
* Investigating a performance regression tracer
* But Geth can release whenever

**Tim Beiko**
* There’s also, The fee history API I saw Besu had merged that.  I think Geth still had an open PR, Im not sure about the other clients, so that seems like the one big feature that’s not merged in most clients.

**Péter Szilágyi**
* Yes, that a planning thing.

**Tim Beiko**
* Is that something that’s realistic to get done in the next two weeks as well?

**Péter Szilágyi**
* Yeah

**Tim Beiko**
* So I guess this is what I would propose, we wait and see how Görli goes

**Trenton Van Epps**
* Would that be a month from now, or a month from next Monday?

**Tim Beiko**
* Early August / August 4th.  

**Gary Schulte**
* I think that sounds like really good timing.

**Tim Beiko**
* When im back on Monday the fifth well settle on something.

# 2. Other Discussion Items
## i. [EIP-3074 Alternatives](https://ethereum-magicians.org/t/a-case-for-a-simpler-alternative-to-eip-3074/6493)

**Tim Beiko**
* Yoav made a very elaborate thread highlighting some potential issues along with some potential alternatives.

**Yoav**
* I was looking at EIP 3074 and seeing what it aims to achieve, because it seems to me that it is quite powerful, which also translates to risky in this case.  I wanted to see if we could achieve the same with less risk.
* Talks about 3074 vulnerabilities, 
* So I demonstrated a case where a perfectly secure invoker runs on one chain, and the user transacts there and then later when the user moves assets to the other chain with a bridge later someone deploys using the same key, deploys another invoker and this one doesn’t bother looking at the commit, so it can do whatever it wants.  And then it can do anything on behalf of the user like remove all the assets.
* The other case I demonstrate was a governance hijacking

**Tim Beiko**
* Thanks a lot for sharing, lightclient or Sam, I know the two of you have responded to the thread

**Lightclient**
* I think there is a lot of things to unpack and since this is a pretty difficult discussion to have with voice cause there’s many nuances to these arguments, for and against 3074
* If we can ensure that the invoker is not malleable then we can formally verify the invoker to be safe.  And I don’t understand these arguments about, “Oh well just do it at the client level”, because it’s just code, and so if we’re going to be writing code to do these checks, I would rather it be something that’s open and permissionless for other people to try and develop and something that doesn’t have to go through all core devs, if we take one of the proposals he suggested, there’s things like replay protection that’s really hard to do in a safe way.  And the core development team should be the ones checking that these are valid proposals and those things should be whitelisted via EIP’s and go through the all core devs process.
* Because no wallet supports it, I think that’s like a different way of thinking about smart contracts that we’re not used to

**Sam Wilson** 
* Sure, so I think what it really comes down to is there’s a philosophical difference between the people who are pro 3074 and the people who aren’t, one of the big concerns brought up is that you delegate control of your entire account to this invoker.  
* We think the delegation should be complete and that you delegate complete control to an invoker then the invoker decides what to do with it, then the other way of doing it is letting core devs decide how to delegate control and letting client and protocol developers.

**Yoav**
* So I didn’t mean for core devs to decide on how to delegate, I meant that the wallet would do it, but the wallet would delegate things by actually signing the operation.
* The thing I suggested was that all core devs was only a small part of the protection, so I don’t know if we should get into the specifics of that, but the general idea is that the user will have to sign each operation 

**Sam Wilson** 
* And by operation, you mean a specific call right?

**Yoav**
* yeah, a specific call.  I suggested that if we are signing a commit that is interpreted by the contract then the contract invoker can do anything, the contract will only be able to perform if signed by the user.
* So I think that the disaster that we see, if someone sneaks in a malicious invoker that is widely used, it can be something that can be in the order of The DAO or much worse

**Tim Beiko**
* Vitalik, you’ve had your hand up for a while

**Vitalik**
* I just wanted to also quickly summarize the issue that I brough up in my own Eth magicians thread, which is a forward accountability with account extraction.
* So basically the idea there is that I think long term we’re going to have to switch to account extraction at some point and I think that there’s a lot of reasons for this, like one of them is just the big gains from having smart contract wallets for things like multi sigs and other kinds of wallets
* Another longer term one is quantum resistance, like once we want to make Ethereum quantum resistant
that to be future compatible with that world
* My concern was that the auth call mechanism in its current form doesn’t really, it feels like it goes in the opposite direction of future compatibility a little bit, basically because what auth is, is  it’s a call scope to variable that basically introduces a new way of getting the permission to send something from another account.
* Now if, in the future we end up having smart contract wallets, auth would have to be replaced by some mechanism that calls the wallet and that calls some kind of delegate function
* I suggested a couple of alternatives, so one of them is, I think Yoav’s alternative EIP 3074 where you just sign over a series of messages, it actually performs much better on that metric.
* Another idea was replacing auth and auth calls with pre-compiles, just because pre-compiles can be replaced with code and they don’t just dangle and be EDM forever
* And a third was explicitly putting a finite lifetime on the mechanism so that developers know that eventually they’re going to have to move to something else.

**Sam Wilson**
* So I have a couple of follow up questions on that.  How do you feel about the proposal that Matt and I sketched out in your thread
* Instead of putting the signature on the stack, you put it into memory of variable sized space, and then currently that would just get verified as an ECDSA signature, but in the future it would get sent to the smart contract wallet to do whatever verification it wants to do on that block of bytes, that way today it will be an ECDSA signature, and then in the future it can be upgraded to whatever smart contract wallet system that they want.

**Vitalik**
* Yep, that’s definetly an improvement.  I think even with that improvement there are still the aspects that the EIP is permanently complicating the call structure in the sense that we already have an op code that has a call and now we have another opcode that does a special kind of call.

**Sam Wilson**
* Why is a precompile technical debt better than a opcode technical debt?

**Vitalik**
* Because you can just hot swap the precompile for a piece of EVM code, like in our specific case what would happen is that the precompile would just be hot swapped for a couple of EVM code bytes that just directly call the delegate function of whatever the target account is.

**Sam Wilson**
* Can you implement an opcode in terms of other opcodes right now?

**Ansgar Dietrichs**
* So I just briefly wanted to ask, a bit of a process question because to me it feels like it’s a little bit of an unfortunate situation.
* I’m just wondering, is there some process change that would make it easier to separate the protocol discussion changes more clearly from the feature discussion in some way?

**Tim Beiko**
* I see what you mean, so I think the conversation on Eth magicians is obviously very valuable.  I think the best we can do in all core devs is summarize it and point people there to resolve the issue there.

**Ansgar Dietrichs**
* I don’t want to propose another call, it just feels like it’s a bit inefficient that the caller process is kinda this single track thing where we’re all kind of different changes are being discussed.
* For 3074 specifically, we can definitely find a solution.

**Tim Beiko**
* At the end of the day, you will need clients to implement it
* I feel like a big part of the discussion does not involve all the client teams, and that is something we can take out, right like iterating towards a proposal and having something say addresses the stuff we just discussed doesn’t have to happen on all core devs.
* But at the end of the day, because all the client teams have to implement it, were going to need to bring it up and discuss it here.
* We can talk about this offline, ill try to think about it as well, I agree sometimes this feels like a bottleneck, if we can make that better than we should.

**Vitalik**
* I just wanted to add on to that, its definitely a problem I feel as well
* I have some proposals that I’ve been promoting, state expiry is one of them, banning self-destruct and make Merkel tree implementation considerably simpler is another one.
* These ideas, I personally would want them to be block tested sooner rather than later, and it’s definitely ideal to have a format where people either have concerns, or people want to investigate them to figure out what kinds of issues they have and then actually incorporate more peoples feedback without it being stuck as being part of a 90 minute call every two weeks.

**Tim Beiko**
* The challenge is like as you add more calls, you lose attendees
* It seems when we do ASYNC discussions, the conversation sort of stalls, maybe that’s a que.

**Lightclient**
* I think it would be useful for a group discussion about 3074, and what people want to see or know more about it.
* I’m curious, what things do we need to do still to have it potentially be scheduled for a hard fork.

* I think the way 3074 is proposed is the least permissioned way of doing it.

**Yoav**
* I never said that all innovation should go through all core dev
* I don’t think it’s the most permissionless way to achieve this, you can still achieve anything, and deploy any invoker you like

**Lightclient**
* You can’t, because if you’re signing over a nonce, then the protocol has to define how that nonce is interpreted and if you do normal way, you have to do a sequentially validated nonce, that’s how they are done.
* If you want to do something else, that’s when you have do a proposal to change.

**Yoav**
* Right, that’s the exception I mentioned
* Let’s say that we leave the nonce to the invoker, even though I’m not a fan, still we end up with something more secure than the current version.
* Because, if under attack, the users message can’t be modified only replayed.

**Lightclient**
* Sure, but there are other things we might want to do.
* We have malleability through social recovery
* If you lose your EOA, you can have them sign to recover.

*Lightclient and Yoav talking about the specifics of how two different systems would work

**Tim Beiko**
* There is a lot of diminishing returns here, there is talk of moving this conversation to another venue.
* I want to make sure we cover some other things, Alex had some comments how this impacts address based extension, just so everyone is aware.

**Alex B (axic)**
* So, address base extension is the aim to extend the addresses from 20 bytes to 32 bytes this is driven by 2 reasons
* Increase collision resistance, and addresses could have reserve bytes for additional use cases like expiry, epoch numbers could be stored there.
* With address extension, a single private key could correspond to multiple addresses, if you have this, we have to look into how signature recovery works in 3074, because you have to make a decision on which address you want to recover.
* I don’t have any solutions, I just wanted to raise it as a discussion point.
* Main question here is timing of features
* If we think this is important, than we should get it in to 3074 before the hard fork

**Péter Szilágyi**
* If we make addresses the same length as hashes, a lot of things can go horribly wrong if you can’t differentiate them in the code.
* I don’t want to talk for or against expanding them, just against the same length as hashes.



## ii. eth1.0-specs PRs:
* [Add Transaction Type List](https://github.com/ethereum/eth1.0-specs/pull/220)
* [Pyspec framework](https://github.com/ethereum/eth1.0-specs/pull/219)

**Tim Beiko**
* RicMoo added transaction type list to the Eth1 specs repo
* A list of transaction types we’re reserving, and potentially reserving to avoid collisions
* We can merge it sometime next week if there are no objections
* Lightclient and quilt team have been working on python executable spec for eth1, want to give some background?

**Lightclient**
* Sure, The way that Eth2 has been able to use pispec as a mechanism to discuss change has been powerful.
* Many reasons for writing a spec for eth1, so I think it’s really valuable
* We’ve taken some time to implement Eth1 and python, this is different from how snake charmers have done it.
* We want it to be the most simple way to read for people who are python literate. 

**Danny**
* The 2 spec repo version has been really useful to do test writing

**Tim Beiko**
* Marius go ahead, Update on 3607

**Marius Van Der Wijden**
* 3607 is rejecting transactions where the sender has the block code.
* Basically someone requested us to have a full sync of mainnet with the new roots to see if that has happened yet.  It hasn’t.
* Right now this is checking that the code slice is zero, but it might make sense to check that the empty code is the empty code hash.

**Alex B (axic)**
* That’s really interesting.  That’s something useful to look into, it would be nice to have it clarified.

**Dankrad Feist**
* I wouldn’t worry about finding a preimage precompile.
* We can consider that cryptographically impossible

**Tim Beiko**
* Does anyone have any objections about using the code hash rather than the code size?
* Okay, we can go with that.
* Anything else?
* Let’s see how Gorli goes for London, thank you!



## Date and Time for the next meeting
Ethereum Core Devs Meeting #117, July 9th, 2021 @ 1400 UTC


## Attendees
- Dankrad Feist
- Tim Beiko
- Alex B. (axic)
- RicMoo (ethers.js)
- Justin Florentine
- Rai
- Kelly
- Asmbaty
- Marek Moraczyński
- Siri
- Vitalik
- Yoav
- Péter Szilágyi
- Micah Zoltu
- Karim T.
- Bhargavasomu
- Łukasz Rozmej
- Paweł Bylica
- Artem Vorotnikov
- Sam Wilson
- Tomasz Stańczak

## Links discussed in the call (zoom chat)
https://github.com/ethereum/eth1.0-specs/pull/219

https://github.com/ethereum/eth1.0-specs/pull/220

https://ethereum-magicians.org/t/we-should-be-moving-beyond-eoas-not-enshrining-them-even-further-eip-3074-related/6538

https://ethereum-magicians.org/t/a-case-for-a-simpler-alternative-to-eip-3074/6493
