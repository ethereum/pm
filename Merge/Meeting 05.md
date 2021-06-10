# Merge Implementers' Call 5
### Meeting Date/Time: Thursday, June 3rd, 2021 13:00 UTC
### Meeting Duration: 55 min
### [Agenda](https://github.com/ethereum/pm/issues/331)
### [Video of the meeting](https://youtu.be/j61FqoQwEHo)
### Moderator: Mikhail Kalinin
### Notes: Shane Lightowler

# Inmplementation updates

**Mikhail Kalinin**

* No active testnets at the moment post-Rayonism.
* Client teams are busy with Altair and London.
* [New PR](https://github.com/ethereum/go-ethereum/pull/22827
) in GETH repo. PR by Gary. Contains changes re: transition logic implemented on Catalyst side. 
* When this logic is implemented on beacon chain side we can test it.
* Work is happening on state sync. Query for GETH... what is the progress update?

**Guillaume**

* PR by Gary got tested during Rayonism and works. Will get back to you re: state sync.

**Mikhail Kalinin**

* State sync is not top priority at the moment (transition process is). Will be #1 pretty soon.

# Research updates

**Mikhail Kalinin**

* Transition process with computed total difficulty. [See PR](https://github.com/ethereum/eth2.0-specs/pull/2462)
* This is the implementation of the transition process where we can view the transition total difficulty at the moment of the merge fork. 
* Would encourage everyone to review this PR. Hopefully can be merged within a week to start implementing on beacon chain.
* There is some debate as to how total difficulty is computed but there is rough consensus around the approach.

**Vitalik Buterin**

* Did we want to talk about transition difficulty offset is calculated?

**Mikhail Kalinin**

* The general idea is to compute it when merge logic is enabled and beacon chain code is transitioned to the merge fork.
* There are two ways to compute difficulty. Based on Eth1 data. One way is to to take a number and preconfigure it in client code deployment. Eg a month before the computation takes place. The other way is to take the difficulty of this particular block that is referred by the eth1 data and multiply it by the number of blocks that we expect to happen.
* The first way is more conservative. The other way is more predictable.

**Vitalik**

* I consider the second way to be more conservative.
* For the offset, its going to get computed based on some formular. Two questions - 1: is that formula going be one that just we core developers use to come up with a number and we put that number into clients when we distribute them to people? (when does the formula run) and 2: what formula is that?
* In both cases we would expect the formula to be 'take what we think the difficulty is going to be at that time and multiply it by the number of blocks in one week'.
* The issue with precalculating it is that if you precalculate it you just put the result as a number into client code, then you're relying on info that is at least 3 weeks older than the actual fork. Lots of things could happen in that time depending on price etc. 
* Making a decision earlier when we have less info seems more risky than putting the decision in the protocol to execute at precisely merge time.
* The best argument against this is if miners coordinate to turn off their miners for the period prior to the calculation being made. They could push the difficulty down or up to speed up or slow down the merge. Having a better estimate vs being more vulnerable to attacks - its a trade off.
* Hybrid option - making it be the minimum of these two.

**Mikhail Kalinin**

* I think taking the minimal difficulty at the point of the deployment is what was suggested. We could make it a constant. Could we estimate the entire hashpower that could be put onto the network instead of relying on network conditions at moment in time?

**Vitalik**
Signal breaks up.

**Micah Zoltu**

* Just to clarify, if miners switch off for two days and then switch back on, that would move the merge closer or further away?

**Mikhail Kalinin**

* That would move the merge closer as it will take the lower difficulty as the estimate.
* Minimally safe difficulty - we can take the value from the network at this moment in time but it can be lower. If we see this going down, the hashrate goes down significantly, we have lower cap/boundary that we take for estimation. 

**Micah Zoltu**

* The one problem is that its a possibility that the total hashrate decreases as the merge gets closer due to people selling off their hardware. We might legit see a reduction in hashrate. This could delay the merge as the minimum value needs to be met.

**Danny Ryan**

* This would happen if we set an offset anyway (eg a fixed offset based off of the hashrate at that time, thus delays).

**Tomasz Stanczak**

* Do we provide rewards for mining for a few months post-merge? Can we delay the time it stops being profitable?

**Micah**

* We considered this as an option to realign incentives. Most seemed to agree this was to complex to be worth it.

**Dankrad Feist**

* If it's delayed for more than a week it would be easy to coordinate this during that period to make it a week? We could tune the parameter?

**Micah**

* I worry about a command line parameter that is a consensus rule which we expect to change. Miners should know how to do that but this would create a technical barrier for normal users who I wouldnt expect to be amending via CLI.
* We want Ethereum to be accessible to the average person. We should avoid required CLI arguments.

**Dankred**

* This would only be a worst-case fallback.
* We need a fallback for a forced merge in case of a miner attack.

**Jacek Sieka**

* We should make it the other way run - that you cant run the software without the parameter. Make it needed.

**Micah**

* That reduces chances of having a fork, but I fear it would drive away novice users.

**Mikhail**

* We may want a mechanism to check the computed value ie to communicate the transitional difficulty, to allow users to check what theyd get on their local nodes.
* If we need to hard code a parameter here in this formula, then we would need to fall back to the hard coded transition total difficulty?

**Vitalik** (garbled)

* No strong opinions.

**Danny**

* Let's take it to the issue.

**Mikhail**

* Heads up on consensus API... have been thinking about it and am leaning towards that get duplex communication channel as a requirement. We can use web sockets but lets think about it later. This would introduce a new kind of message into the protocol.

**Micah**

* Question on the two way communication / duplex socket. Does it need to be trusted by both sides? Or does one side on thr trust in that relationship?

**Mikhail**

* The execution clients trusts what has been sent from the consensus. 
* When the clients exchange messages, what is the head block at the moment? Beacon chain client will need to rewind some blocks and feed them back to the execution client. Probably requires some trust as well, depending on use case.
* Need to think about it more as is more complicated than what we have now.


# Spec Discussion

## Remove ExecutionPayloadHeader

[27:39](https://youtu.be/j61FqoQwEHo?t=1659)

Ref: [eth2.0-specs#2463](https://github.com/ethereum/eth2.0-specs/pull/2462)

**Mikhail**

* There is a proposal by Justin to remove the execution payload header.

**Danny**

* This in statelessness becomes a much larger object. Not sure if there's much value in keeping this in state. Although the most recent header/block you're probably keeping around anyway.
* Dont feel strongly but gut feel is to put the header in there.

**Mikhail**

* Understand the sentiment - there is already a large number of block related structures.
* The idea is to simplify this a bit and just have execution payload. But it implies the transactions of the recent block will be stored in the state.
* We use the execution payload and put it inside of the state.
* Do we want to make this trade off? Spec simplicity vs additional state complexity
* Currently it is max 1.5mb which is negligible.

**Danny**

* The validator set does not change frequently, state to state. If you're duplicating and youre keeping an epochs worth of state in a tree structure, you dont have to duplicate the validator set. Whereas this entire block payload changes every block. In statelessness, this is like 5-10 mb diff on each one. I can write this up in the issue...

**Vitalik**

* Are we going to try to make beacon block execution stateless?

**Danny**

* No, Justin is suggesting putting the entirety of the execution payload in state at each slot. The most recent, rather than a header.
* What youd get out of that is that you dont have another object, which is an execution payload header, and youd have transactions readily available.

**Protolambda**

* The execution payload, if we embed the transactions in the state, they can do these types of transitions. So if we do end up with MEV protection, we need this look back to the previous block. 
* Re: state size: it would add a lot of noise to the beacon state format itself. This would change every block and duplicate a lot of block information.

**Danny**

* Lets take this to the issue.

## DIFFICULTY opcode and randomness after The Merge

[33:24](https://youtu.be/j61FqoQwEHo?t=2004)

**Mikhail**

* There are two specs here - Difficulty and Block Hash.
* Difficulty...
* The difficulty opcode currently returns the difficulty. We have a constant for the difficulty field already in the execution block for after the merge.
* Its a constant and some applications already use the difficulty opcode for various sources of randomness. By setting this value to a constant this will break these applications.
* We have two options... 1 (desirable) is to rename difficulty opcode to random or randao and pass the most recent randao makes from the beacon chain side to the EVM. This is a long term solution. Requires EVM change which we want to avoid for initial merge. For the initial merge we can just grab the first 8 bytes of randao makes and put this as the difficulty parameter into a block.
* My preference is the simplicity of the latter solution.

**Micah**

* Why do we care about users who ignore security advice saying 'dont use difficulty for randomness'?

**Mikhail**

* Do we need to help other people?
* This is the same for using block hash for randomness.
* We want to give the ability to have real randomness. We want to provide this in the EVM. Taking the above randao approach would be the first step to a more permanent solution.

**Danny**

* Although I dont feel like we necessarily need to protect apps that use this poorly, I dont think this is a bad approach - to rename and insert something in that is pretty random.

**Micah**

* Would the renaming just be in the documentation or is it a consensus change?

**Danny**

* We would call it something different in docs and have a new source for the value, ie randao.

**Micah**

* From an engineering standpoint, if thats low cost or easy I think its fine. I just wouldnt want to add on extra engineering effort.

**Mikhail**

* Ok, so at the merge we do nothing - we use constants for difficulty. With post-merge EVM changes we will implement this new scheme to rename difficulty to randao.

**Danny**

* The weird part here is you end up with a not insignificant stretch of time where everything does break. Then they unbreak.

**Mikhail**

* I dont want to break anything!

**Danny**

* I think its better to break it once and then dont unbreak it.
* The unintended consequences of having lotteries break and then unbreak is harder to reason about than breaking.

**Micah**

* It would be good if we could reuse opcodes though as there is a finite set. We can extend it and we're not running out just yet, but itd be nice to be able to reuse unused ones.

**Vitalik** Garbled

* Having specialised opcodes where we just push numbers zero/one doesnt work.

**Danny**

* At that point we need to promise not to change it from being value = 1. Or are we saying dont use this for value 1?

**Micah**

* There are people who push 0 as the first opcode so that they can dupe it because its cheaper to dupe it than to push 0.
* If you can save another 3 gas by using difficulty to get 0 or 1, they will do that.
* Its almost exclusvely bot authors who would do that. Their bots come and go weekly. Theyre not the worst people to break as they can upgrade very easily.
* That being said i would prefer it to return invalid. If we're doing an EVM change why not throw randao in there?
* The ideal solution if we're going to break it and we want to reuse the opcode would be to have it throw or be an invalid opcode during that interim time. But if we are doing that that would require an EVM change, and if we're doing an EVM change with the merge we may as well put randoao in there.
* Our options are, put randao in for difficulty, or have difficulty now become the push 1 opcode.

**Mikhail**

* Right. Anything else re: difficulty?
* Ok, so block hash stuff... this is going to be broken in terms of randomness. It wont be protected by PoW after the merge. We cant do anything because the block hash has its original semantics which might be used by existing applications. We cant change it to anything.
* If anyone hears this recording and they have apps that depend either o difficulty or the block hash as the source of randomness, reach out to us in ETH R&D discord so that we can discuss it and potential solutions.

**Vitalik**

* Its important to not leave these issues open for too long - we risk causing delays due to this not being done.

**Micah**

* Anyone know what Click does with the difficulty opcode?

**Adrian Sutton**

* Its hard coded to 2 for an in turn block and 1 for an out of turn. Difficulty is used as difficulty.

**Protolambda**

* How about other EVM chains? We need to align shared tooling.
* Ethereum is not the only chain with EVM, so if we mirror other PoS or PoA chains with these opcodes then they might be bust.

**Mikhail**

* It would be worth checking this.

# Open Discussion

[46:03](https://youtu.be/j61FqoQwEHo?t=2763)

**Vitalik**

* what is the plan with block hash? Would the block hash opcode just return the  execution block itself?

**Mikhail**

* Yes. Thats the default plan - do nothing.

**Vitalik**

* At some point in the furture we are going to have to break all of the old proofs. At some point we'll want to retire RLP and change the format over to some new SSZ based thing. And probably at the same time add some more proof verification precompiles that are more future proof. Doesnt have to be solved till after the merge.

**Micah**

* Why is it hard to get randao into that spot at the merge? In my head the consensus client simply sends over to the execution client when it asks it to build a block and says 'use this for difficulty'. The execution client then uses that.

**Mikhail**

* If we're talking about setting the execution blocks difficulty field to something derived from randao. This is easier than taking the whole randao mix - give it to the execution client and the execution client will embed it into the EVM and expose via the difficulty opcode.

**Vitalik**

* When you say its something derived from randao, wy not the randao? Why does this need deriving?

**Mikhail**

* I mean derived as in the difficulty field is obviously 60bit long...

**Vitalik**

* From a long term perspective I dont think it makes sense to have an opcode that returns the last 8 bytes of the randao because that would just be redundant.

**Mikhail**

* That's a fair point. So the complexity is just to do anything with the EVM at the point of merge.

**Micah**

* Isnt the difficulty 256 bits? In the block header i think it is?

**Mikhail**

* Its 64 bits iirc. The difficulty opcode may return up to 256 bits.

**Micah**

* In the block header its 64 bits?

**Mikhail**

* Right.

**Vitalik**

* The block header is RLP so it could be any number.
* Is there a consensus rule that prevents it from being 263?
* I know that there are other things that result in a 64 bit limit. Difficulty feels like something that would be risky to cap.

**Micah**

* If this is the only thing holding us back, we should investigate with the clients to see if they have that, in which case it may be a consensus issue. 
* GETH for example, the nonce is 64 bits internally but consensus-wise that is not a consensus rule.
* We do have known consensus issues but they cant be reached. Difficulty is one that may be in a similar boat, but possibly reachable.

**Mikhail**

* Thats a good thing to investigate. We are probably just going to drop the whole randao into the difficulty field?

**Micah**

* Does that change the argument here? Lets say hypothetically it is a 256 bit field and all clients support that, does this seal the deal and we just say put randao in there and we're done?

**Mikhail**

* Id say so.
* But do you mean done in the long term? Probably not, its sub optimal.

**Micah**

* Meaning we can put the full randao mix into the difficulty field and we never have to change the opcode again.

**Mikhail**

* Right. We can just change the way the randao makes it transfer into the opcode

**Micah**

* Sure. We might have another mechanism of getting it there later that is a little cleaner than having the client send it, but the gist is that opcode will just be the randao mix from merge on.

**Mikhail**

* So its gonna be mixed into the block hash this way. It doesnt matter much because block hash as a source of randomness wont be secure as it is now.
* We should stop here as we have 5 mins to the next call. Thanks everyone.

-------------------------------------------
## Speaking Attendees
- Mikhail Kalinin
- Dankrad Feist
- Protolambda
- Vitalik Buterin
- Danny Ryan
- Micah Zoltu
- Adrian Sutton
- Protolambda

---------------------------------------
## Next Meeting
June 17th, 2021 @ 13:00 UTC







