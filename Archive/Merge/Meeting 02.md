# Merge Implementers' Call #2 Notes

### Meeting Date/Time: Thursday 2021/4/15 at 13:00 UTC
### Meeting Duration: 90 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/299)
### [Audio/Video of the meeting](https://youtu.be/ODcNpWiLASk)
### Moderator: Mikhail Kalinin
### Notes: Santhosh(Alen)

# Agenda
- New terminology
  - ethereum/eth2.0-specs#2319
  - https://hackmd.io/@n0ble/the-merge-terminology
- Execution-layer discussion
  - Communication protocol
  - Fork choice and chain management
  - State and block sync
  - Gas limit/target voting
  - Slot clock ticks
- Consensus-layer discussion
  - Improved transition process: set TRANSITION_TOTAL_DIFFICULTY at TRANSITION_EPOCH
  - Consider max block size in relation to max size of ExecutionPayload (transactions max size is 16GB)
  - Consider Union type for transaction list with a single OPAQUE_SELECTOR for first merge fork
  - Consider eliminating uint256 requirement on beacon-chain side
- Rayonism updates ☀
- Open discussions

# Intro
**Mikhail Kalinin**
Welcome to the Merge Implementers' Call #2

**Mikhail Kalinin**
* So, while some ethereum core developers might be able to join this call, let's just go over the agenda and discuss some things that we can do without them.
* To begin, we have this new terminology uh the key replacement here is that we replaced the application term uh with the execution one, so there is the uh execution layer instead of the application layer this is to not confuse people with the smart contracts and applications using them so applications built on top of the mainnet that is the purpose of it.
* The term layer is arguably not the best one for execution and consensus because they are not really layered, and yes, we will think about it more here.
* I don't want to spend too much time on this, but it's probably best to name it subsystems or engines or whatever, and yeah, if people have any suggestions, just drop them in discord and we'll probably address it offline, so something on the terminology, any questions here.

# Terminology
  - Consensus (eth2), Execution (eth1), Application (dapps)
  - Engine or Sub-system, not layer
  - We can discuss this offline in Discord further on this.

# Execution discussion

**Mikhail Kalinin**
* I was just going through the main parts of the execution stuff and asking for any updates or understanding for possibly queries from uh ethereum developers so that's the initial concept so we can probably do this anyway so any questions to the like communication protocol.

**Danny**
* Where can I find the most recent updated link? Rayonism is inspecting the contact protocol to ensure that you are maintaining Mikhail.

**Mikhail Kalinin**
* Yeah right that's the one I have put the link to the previous one uh the new link the ram is blink is put to the top of the previous document so that's like the latest one anyway the yeah anyway this is json rpc for ionism but it's probably not going to be production so we can you know we can get to this discussion later okay so who has reviewed or who has any thoughts or suggestions regrading that.

**Nethermind**
* By communication protocol do you mean eth1 to communication by rpc or anything else 

**Mikhail Kalinin**
* So, yeah, that's yep.
* Okay, nothing in particular, but if you have any questions, please let me know.

**Nethermind**
* I have a query because I'm not completely sure how to handle potential problems and errors in this protocol. For example, if the assemble book fails, the new block fails, or the set head fails because the payload is incorrect or any internal error occurred, I'm not sure how to handle it. The specification makes no mention of error handling.

**Mikhail Kalinin**
* Yeah, there are statuses for finalize block set head and obviously for new block I mean that you can return false if it wasn't done correctly yeah you're right but assemble block doesn't have any. yes, that's right Yeah, that's a good question. I think we should add some kind of status there as well, so it'll be an item and the status alongside it.

**Danny**
* Right, particularly because you can specify as a parent hash now, you might point to anything that's just terrible, so there's certainly a failure case there, or something that's non-existent.

**Mikhail Kalinin**
* Also, the other alternative is to use the errors in json rpc that we have today, right? You mean the result, right? Is it in the spec? Okay, I see the issue.

**Nethermind**
* One thing because I'm not sure whether it's specifically defined assembly block doesn't have it so after assemble block new block will be called or do we assume that new block won't be called and it can be called just by set head uh we actually in general expect that new block will be called So there is a state transition occurring on the consensus side when the block is assembled and it's suggested it should yeah, which the state transition is uh called triggered and yep it will activate the call to the new block method okay so it's assemble block then new block yeah you can like I wouldn't say I would, Danny.

**Danny**
* Assume that get work does not add it to the block tree today. Only if they find a solution, uh, does something get added to the block tree.

**Tomasz Stanczak**
* So it's kind of similar logic, yeah, but in a proof of authority chain, you'd create the block and edit it right away, so yeah, I understand your argument here because there's a difference in time, like when you keep preparing the blocks with the assemble block, you can theoretically call it several times right with the same parent because can you?

**Danny**
* You might presumably, but there isn't an instantly clear use case for that, unless, of course, there isn't. There is no obvious application for that.

**Mikhail Kalinin**
* You may want to give a block and stop repeating the same transactions.

**Danny**
* Right, as you would expect Yeah, you can imagine doing it slightly earlier to get something ready to broadcast and then doing it again quite close to the time of broadcast to see whether you've got a better coinbase output on the mev side, but even then, I don't know that's a very obviously good strategy just a possible strategy actually an useful is it worth the complexity.
* In having the ability to point to something arbitrarily to build build on rather than just the head, I mean presumably the beacon node keeps the execution engine in sync with what it thinks is the current head and so if there was a reorg you can trigger that and then call symbol block uh and just ask me primarily when you definitely know the head.
* And you can say the parent hash to build on, but that opens up a design constraint on the fusion engine to be able to build on arbitrary heads, which I'm not sure is worth the complexity.

**Mikhail Kalinin**
* That's a good question because it might be the case when there is the arbitrary like block becomes the head afterwards I can imagine this kind of stuff with racing between a bit of racing between the new head and assemble block or yeah so wha what if the head has changed during the block has been assembled what could happen here I mean you even imagine if the head is being changed when the block has been assembled.
* What could happen here, I mean, imagine if the head is moved when the block is being proposed, then how will this work? How can the beacon node manage this?

**Danny**
* I mean, at some point, the beacon node has to make a decision on what it thinks the head is and assemble the block based on that, but the idea is that when I start assembling a block, another subsystem triggers that there's a new head halfway through me assembling a block, and I ask the execution engine for the transaction payload, but it's gotten a trigger from somewhere else, but there's a new head halfway through me assembling.
* In a block, I ask the execution engine for the transaction payload, but it's received a trigger from somewhere else, but there's a new head, and I'm now out of sync on that, and this protects against that.

**Mikhail Kalinin**
* Yes, some degree of consistency is needed.

**Protolambda**
* uh sir go ahead.

**Danny**
* no please please 

**Protolambda**
* Cases of consistency are extremely important in general, but remember the situation where there are many beacon notes referring to the same thing if you're not sure.

**Nethermind**
* Okay, so I'd say we should think about any concurrent calls to those rpcs. For example, if we have one set head and a second set head, we should probably cue them that the last one wins or something like that in the implementations. Uh, finalized blocks are probably not significant, and new blocks are probably not important.

**Danny**
* That the other relationship between fat head and and some of the other calls may be important.

**Mikhail Kalinin**
* Yes, my feeling is that all of these messages should be processed sequentially, but what should be but yeah, new set head and new block are causally based, so they must be processed sequentially, but others may be processed concurrently, but I'm not sure whether this is true in all situations.

**Danny**
* Yeah, I can see how a symbol bot and set head might get out of sync depending on whether different subsystems in the beacon chain are out of sync and therefore the parent hashes are certainly immediately it's a nice simple fix without having to worry about things deeper but it could open up complications on the execution engine side um but I'm not sure.

**Mikhail Kalinin**
* Okay, so the assemble block should have some we've started from the error message okay, so let me think about it and we'll continue fine probably.
* If there is something else here, we will proceed to full choice and chain management.

**Danny**
* Yeah, I just want to highlight the current like with that parent hash in there and there's not really any bounds on that that like a cymbal block might trigger an arbitrary not reorg because it wouldn't be changing the head but trigger an arbitrary like attempt like you have to go and put yourself into this different state to build a block and so there could be complexity.
* It's worth people looking into that over the next week or two so we can talk about it again the next time we meet.

**Protolambda**
* For the time being, I'll simply lift the error if the consistent consistency check fails, and then we can adjust implementations to actually handle the situation.

**Nethermind**
* So, if we have a finalized block, it probably affects what parent hashes can be supplied to the new block, doesn't it? So, we can't organize finalized blocks, so we do have some constraints on this parent hash.

**Danny**
* right, correct So they are arbitrary in the sense of finality in the subblock tree, yes, but.

**Mikhail Kalinin**
* I would not impose these checks on the execution engine because this is the duty of consensus, and in some situations, um consensus may move from one finalized checkpoint to the concurrent one, which is similar to some forks or whatever.

**Danny**
* Even locally you'd never reverse penalty like yeah even if there was enough contact value well it can't happen locally even even though there was enough contact value

**Dankrad Feist**
* is it likely with manual intervention? You might have ended up on the wrong fork and then changed it, but the node will never do that.

**Nethermind**
* Yeah so I have a question so uh finalize block how many uh how much height of the chain may not be finalized yet i'm not aware of that because it's important uh for state management pruning implementations things like that that's a problem that that is rise here of what i'm uh aware of in from eth one side so practicality of this problem is how big this unfinalized chain.

**Danny**
*  Because in regular operation it's two epochs is the depth so that's because that's usual operation because you get in the happy case you get pruning on fair depths but you can't actively prune if you're in a time of non-finality and you know you might go days without finality so there's certainly a variance that has to be managed on pruning.

**Mamy Ratsimbazafy**
* so the risk about non-finalized state is what happened during medarsha for a couple of days the chain didn't finalize and we had many many forks and in that case uh theoretically you can store all the forks in your client so maybe they will become legitimate but if one fork just has a few votes it might not be worth it.

**Dankrad Feist**
* The issue is that if a new block builds on one of those forks, you have to validate that block so you later need to see if attestations to that block are valid, which I believe is the issue, but I can say that on mainnet, we should definitely be prepared for longer non-finality periods, but hopefully not days, so maybe we can get a more reason a compromise like days would be pretty extreme, and if we ran into that, it would be a pretty insane failure.

**Milkhail Kalinin**
* Okay, so something else about the protocol of communication between ssi execution is fine.

#  let's just move to the folk (time:20:18)

**Milkhail Kalinin**
* Chain management options I know that people have begun to investigate and that how difficult it will be to make the fork option pluggable and how much of an effect it has on changing the chain management of their clients what I just wanted to ask about any changes and thoughts here about how it could be enhanced like from any point so.

**Nethermind**
* So maybe I'll start from a different mindset it's actually fairly easy we had it fairly broken down already the problem there might be that I haven't investigated that much is later syncing the network up to the head and then starting it so integrating the syncing and the fork choice management itself might be harder than just but for starting from the head like for the hackathon we want it's fairly easy.

**Danny**
* Yeah, since we're hackers, we just have like this absolute difficulty uh rules for the beginning, and there's progress on Guthrie yeah.

**Proto**
* If no one from Guff is in the call, I suppose I can send an update.

**Danny**
* Currently, Peter has been unmuted and silenced a couple of times, so we can't hear you if you've been speaking.

**Peter Szilagyi**
* So, if the question was what's the guest's progress on these matters, we had a meeting with proto, I believe yesterday or two days ago, and he kind of went through different stuff. I suppose the conclusion was that if you need anything for Monday, the closest we can give you is guillaume's pr, which just kind of hacks into hacks of things into basically guillaume's PR.
* We started working on an essentially new consensus engine that does the whole new fork option rule but we haven't integrated it in yet because as far as we know, it only explicitly inserts into the blockchain and hacks through all the internals.
* I know it's not finalized yet, and I've also started working on the synchronization, but I'm a little sidetracked because, in order to make the synchronization work, I also need to change some other parts of production get, and I'm not super keen on hacking stuff together in production parts, so I just want to make it properly, which means it's going to take a little longer.

**Milkhail Kalinin**
* Great, thanks Peter.

**Nethermind**
* If I could ask the pr you're talking about if this is the pr i've seen is following the old spec it's not a big deal but the jason rpc gui is different than the new spec it's not a big deal.

**Gullaume**
*  So it's not following the old spec, no uh, it needs some modifications, but it'll be finished after this call.

**Nethermind**
* Okay.

**Milkhail Kalinin**
* yeah, any questions about chain management and book selection? Okay, so this scene process is just a high-level proposal in the design dock we discussed on the previous call on how to download the state and do the boxing, and if people have any opinions on whether it's viable or not, or any other inputs, that would be great.

**Danny**
* I assume we'll say that, but some people haven't quite made it there yet, so we should probably bring it up as well.

**Milkhail Kalinin**
* I agree, let's just assume for the time being that it would work. There was a question in the chat in the discord, I don't remember where exactly, perhaps in this court, on which part will decide on the gas limit and target voting after the merge, so my basic my basic thoughts are that it doesn't change so the execution engine has this voting mechanism and every proposes.

**Danny**
*  I'd say by default it remains the same, which is a block producer, regardless of whether it's a minor proposer or validator, it does it similarly to how 1559 post merge you know the block producer will be responsible for paying base fee for transaction and figuring that out in a similar method don't know on on e1 clients today what's the how does one access that is it in a similar method don't know on on e1 clients today what's the how.

**Milkhail Kalinin**
*  Has a flag with only a number on it, which is the goal for the gas limit, and it will be increased according to the gas limit formula per block, from what I recall.

**Danny**
* So, well, the features should stay stable and work well.

**Peter Szilagyi**
* I mean, we can always add methods to adjust it because it's such a small thing, but I don't think people want to keep changing it at runtime, but yeah, if there's a need to be able to tweak the limits at runtime, it's more than trivial, it's real to just change it.

**Milkhail Kalinin**
*  Added it correctly, and now if a miner wants to do anything like raise the gas cap, it simply restores the node with the new parameter.

**Peter Szilagyi**
* Yes, but if you look at mainnet generally, miners still run with the maximum gas cap that was kind of considered secure for the network, and it's just modified maybe once every half-year or so, so it's not like you have to constantly adjust it right?

**Milkhail Kalinin**
* I believe that following a consensus update, there should be no need to change this section.

**Danny**
* Okay.

**Milkhail Kalinin**
* So one thing for the next the next item is just slot clock ticks this is I suppose it's been missing like on the previous call and in the dog but I think it might be relevant because there is the consensus component that has the slots clock and these sticks could be propagated to the execution I guess because the sticks timestamp goes to the block to the next block and and it's probably necessary for transactions that use the timestamp of code to be up to date with this kind of details, so some additional message or order might be required.

**Danny**
* So you're saying that transactions in the mempool might be invalidated, or that they're not as important, or that there's logic that's based on them?

**Milkhail Kalinin**
* Yes, they could adjust the way they execute their like execution flow uh inside of a smart contract method it calls, and it might be necessary for the pending block functionality because you have to restart the block any time a new timestamp is observed.

**Peter**
* Could you elaborate on this a little bit, so what exactly is this notion that I'm missing?

**Danny**
* Proof of stake blocks only have a time stamp determined by the slot, and the slot is only every 12 seconds, so there's no granularity of time like you'd find for transactions reaching timestamps opcodes that aren't on those 12 second boundaries, so it's fine. The activation engine can either know the time and determine where it is and use that, or it can be told the time and use that, okay?

**Peter**
* But then, basically, this would mean that the eth1 blocks could also reach the same twelve seconds, right? So, when you call produce block or whatever it's called, you'd specify the timestamp to produce it at, right?

**Danny**
*  Right okay, this is more of an uh, I think Milkhail is concerned about systems that are maybe dependent on time stamp that aren't right at the granularity of produce block like managing the mempool thing, which is good because it gives you a deterministic outcome. I think michael is concerned about systems that are maybe dependent on time stamp that aren't right at the granularity of produce block like managing the mempool thing.

**Peter Szilagyi**
* Okay, so I think the only thing I wanted to emphasize is that everything that transaction execution depends on needs to be stuffed into the block header because otherwise we won't be able to synchronize best box.

**Danny**
* Right.

**Peter Szilagyi**
* So you can add so we've discussed it with diamond a few days ago that the original rpc apis already had this round out thing plus some second field right which at least in the past api they were only passed along as two more fields independent of the block and I just wanted to ask that if we ever want to add those fields back then we probably need to have them integrated into the header, and because we've nuked out three four fields, for example, the mix digest and others, we can still repurpose them if we want to get them in with minimal harm to the I mean the remote adjustments to the iphone clients.

**Danny**
* correct, there isn't really a need for another field because the time stamp field's consistency with the slot can be checked on the consensus side and we can check it outside, so I don't think you really need it. I think Mikhail is more concerned about the execution engine knowing what slot it is without the context of a new block being called, and so I don't think you really need it.

**Mikhail Kalinin**
* So, my question was about how two ample transactions are executed on which block is a dependent block that is generated and restored each time after the new block is obtained and imported from the wire.

**Peter Szilagyi**
* I'm not sure what other question you're asking.

**Mikhail Kalinin**
* The question is, before propagating the transaction to the y, you must check and confirm it.

**Peter Szilagyi**
No, you just check if the sender has enough balance to condemn his correspondence when you receive the transaction.

**Mikhail Kalinin**
* And yeah, I get it, and it does matter which time stamp is used for a dependent block, right?

**Peter Szilagyi**
*  So, for the pending block, I guess the question is if there's uh, if you want to implement this 12 12 second issue, it would make sense to add a rule into the consensus engineer that the time stamps for the pending block are again on this 12 second boundary, but I guess that's an important spec question.

**Danny**
* I mean, calls to the assemble block will only ever be on that 12 second boundary, so anything opportunistic, like the pending block, should respect that. Then there's the question of whether the execution engine can just use its local time to modify these 12 second boundaries, or if it needs to be explicitly told on, say, a click from the beacon node. okay new slot okay new slot okay new slot so it doesn't have to worry about time sync issues

**Peter Szilagyi**
* no, I think it's better to just let them let the pen fly. I mean, you don't really care what the real world time is, you just care that it's in line with your 12 second click right and the pending block is either way just some opportunistic let's try to execute a batch of transactions and see what happens but it's not a good idea.

**Danny**
* so the concern will be if I have the beacon node and the execution engine on different machines and the pending block becomes is like one second off and so it's a slightly different spot and then when I actually call symbol block the pending block's not as useful to me that would be the reason for the beacon node clicking you know ticking on that boundary so that they can

**Peter Szilagyi**
* Yeah, I truly believe that in Geth, if you are not mining, you are creating these pending blocks, and if you are mining, you are not creating these spending blocks, but rather mining blocks, which are a little different and done differently.
* So for validates, average nodes will just guess the next time and they won't care because they won't ever be caught to finalize anything, and for miners, well, well, I guess for miners you won't really poke at the pending block because you just want to wait for the next thing right?

**Dannyi**
* what is the aim of the pending block when it is for non-mining nodes?

**Peter Szilagyi**
* Ok, to be honest, I think it's pointless, yeah, well.

**Mikhail Kalinin**
*  I was under the impression that miners used band and block.

**Peter Szilagyi**
*  so the reason I say it's useless is because you have 4000 transactions in the pool or maybe even larger if you count the larger pools and miners can pick a few so your local note sees 4000 transactions fix 200 to execute and then you can check the result but even if you swap two of them which are doing some uni-swap things then you will get wildly differing results.

**Danny**
* how is this being made available to users today?

**Peter Szilagyi**
* Like the pending block, you can only query the pending state, so instead of having the balance of the network's current status, you can query the balance of the funding state, but as I said, it's not very useful right now.
* Sorry, only one more thing: the only reason we didn't really press for getting rid of the pending block is that it serves as a nice little caching layer, which means that I keep a list of transactions that I believe will be included in the network.
* I choose the best 200 and run them as pending blocks, but there's a good chance that only 150 of those 200 will actually land in the next block, so by the time I'm executing those 150, all of the storage slots that it hits are already hot in memory.
* But we'll keep the precast. Okay, so it saves you some cash.

**Danny**
*  A little hotter but they got it because if you want to keep the functionality we pretty much just need to get the execution engine respect uh mod 12 second time stamps and then I think you get most of the functionality of today so no problem and even then even if you didn't you probably get most functionality because most things probably aren't calling the execution engine.

**Peter Szilagyi**
* Yeah, so I think the only request I have is that if there is this particular behaviour that uh any block will be on twice or not by second mark, then it could just be applied to the spec that this is to be anticipated, and that pending blocks should behave accordingly.

**Mikhail Kalinin**
* Exactly  yeah yeah and also I was thinking that any block could be useful for applications that send any transaction and just get read from there from the nodes they are hosted to send transactions I mean this band in block series dependent state um okay anyway uh by the way then uh what is the uh functionality that is used for miners is it just creating a block

**Peter Szilagyi**
* Since get currently recreates a block several times during a single mining cycle, it first creates an empty blocks empty log, then it fills it, and then it tries to build better blocks with different transactions, all of which can be mined.
* So, with the proof of work network, you simply build the block with a click whenever a request to the block is sent.
* So, from the e3 viewpoint, one alternative is to simply wait for these two clients to request a block and then run the transactions; however, this will take either half a second or longer.
* however long it takes to mine it to generate a block from scratch, or the other option is to try to prepare a few blocks in advance by guessing the timestamp, and then when you request it, we simply give you the best one and return instantly.

**Mikhail Kalinin**
* Correct, I believe lifetime ticks will be used as input for this type of optimization as well.

**Danny**
* Yeah, either works, and if there's a half-second delay to be expected, then the proposer will essentially call it early until they're supposed to broadcast right at the boundary to be able to pack the block, but if it's doing the pre-packing, it can call it later.

**Mikhail Kalinin**
*  Yeah, I was thinking about just standing not only the current uh time stamp rate but also the timestamp of the next slot to match this kind of functionality that prepares the block in advance okay nice um let's just yeah i'll think about it more I mean and probably add this to the specification as a separate message

**Peter Szilagyi**
*  why would you need a separate message when you're giving us new blocks anyway, and the new blocks are supposedly on the right time slot, so I can just add 12 seconds to that?

**Mikhail Kalinin**
* It's not likely now, so it's possible that the latest block is similar to previous blocks; it's not always the case.

**Peter Szilagyi**
* Oh yeah, but if these two chains correctly monitor the 12 second marks every block is another second mark then I can just measure which will be the next 12 second mark based on my chain head or and the current time so I don't think that's an issue there is when you give me a produce block request and I have to remake the block

**Protolambda**
* Will most likely function if you account for capsules as well.

**Danny**
* Yeah, it will work depending on the time.

**Mikhail Kalinin**
*  I mean, I'd like to add a separate message that just stands for the time this time update.

**Peter Szilagyi**
* You can just extra because in the first round you will most likely not even attempt to be clever, but just whenever the miner says "I will never quit." If a client requests a block, I can simply create one, and the waiting time of 500 milliseconds is reasonable. However, is it acceptable if each client requests a block, what is the protocol, what is the time out, and how do I proceed?

**Danny**
* is the planned propagation time, formation time, and so on, and then sometimes there's like a little bit of pre-work done because you know you're about to propose um, and then propagation can happen in that sub second on regular service.

**Peter Szilagyi**
* so if there were planned latencies in producing a block, you'd only start your work a little bit earlier yeah but so uh let's say it takes me half a second unless it takes me one second to produce a block
What effect does this have on the e2 consensus? Does it matter whether it takes one second or not?

**Danny**
* If I wait until the slot boundary and it takes one second, as long as I only have one to two seconds propagation for the entire network, it's perfect. You're aiming for something like a sub four second time from when I start my job and when you get maximum propagation, but
* If there were delays in getting the block that took you know a second, I as a block for this manufacturer will just start my job early so that I have the block ready at the start of the slot rather than waiting for a slot and then not having the block fix until one second later.

**Peter Szilagyi**
* So I don't think it's a good idea to make the e2 client smarter. What I mean is that it takes one second depending about how many transactions I cram in and it might take less or more so I'm just wondering about the worst case scenario that if I take one second what happens does that consensus break block output or is it just a bit unpleasant?

**Danny**
* It's most definitely perfect. uh, if you're taking two or three seconds, it's no longer appropriate.

**Dankrad Feist**
* Why would you not take, I mean, my assumption is that what a miner does is continuously process make new blocks and always whenever they have the block available they start mining on that can't you do a similar approach that you start making blocks maybe four seconds before your slot time and whenever you're done you start making the next block with the latest information and send the current one to the beacon node so that it can immediately make a block

**Peter Szilagyi**
*  if it's yeah at if I make a block with a specific timestamp and it turns out that the actual timestamp of the validated requests from me is different, then I have to remake the book.

**Dankrad Feist**
* No, but the validator will still request the block with the time stamp of the time when it actually has a slot like that's determined like well at that time it's deterministic like you already said.

**Danny**
* Imagine the time sync between the beacon node and the execution engine being off by three seconds or something.

**Dankrad Feist**
* Likes that, so you can only tell it what timestamp it needs.

**Danny**
* That's what makes well, yes, yes it is, but if the execution engine was opportunistically generating blocks for the slightly incorrect timestamp and thus the incorrect thought, then once you ask.

**Dankrad Feist**
*  No, it shouldn't do that. My theory is that when a beacon node detects a block, it notifies the execution engine, say, six seconds before, and then the execution engine begins making blocks with that timestamp, which is still a few seconds in the future, but that doesn't matter.

**Danny**
* so in the current functionality, you should only call the symbol block several times leading up and take the best one right right yeah connected the last one you can get.

**Dankrad Feist**
* That would potentially give you more fees here, but I don't think we need an anagram.

**Danny**
* Oh, this is the time slot.

**Mikhail Kalinin**
* yeah yes, I get it, so that's just fine, and Lucas, there are certainly things to optimize on this and think about the training contact.

**Nethermind**
* Yes, so what I meant to say is that I wouldn't put too many constraints in the spec on how long it should take to produce the block okay, of course we can put some max value that we expect because I will consider this implementation detail that can also vary for example on hardware because depending on your hardware it can take longer or shorter to produce a block so if I was implementing.

**Peter Szilagyi**
*  Instead of using a single method saying give me a block and then scattering to make a block, you can split it into two methods simply calling it prepare block, which says i'm going to ask for a block with this specific timestamp in the next whatever time and then the e3 client can try to make the best block possible and then when you actually request the block I  i will give you back whatever the best is i have.

**Danny**
*  Right, instead of making a poll on that one tweet, you just say, "Start working, and I'll ask you in a minute.

**Peter Szilagyi**
* so the issue with the poll is that you ask for a blog but I'm not sure whether I should make better ones or stop can you request once, twice, or 300 times or what happened paul's a little unpredictable whereas if you make two calls then at least I know that okay I gave you my best block I can throw away all that scratch work because it won't be used anymore.

**Danny**
* Yeah, that's intriguing, but I think it's fair.

**Dankrad Feist**
* I think you can replicate that with cool as well, like how the eth2 node just uh pulls and then whenever it gets a block it just starts the next request and uses the last one it got from that sequence.

**Danny**
* Yes, the execution engine doesn't know when to quit optimizing.

**Dankrad Feist**
*  well, it would because you stopped making I guess it produces potentially one more block than appropriate I guess that would be the only downside but that doesn't seem to be a big deal.

**Peter Sziagyi**
*  I don't believe so.

**Danny**
* but it's a constant check, right?

**Peter Sziagyi**
* so currently what get does is that when I start mining proof of work networks, I create a block and give it to the miners to start crunching on it, but then some more transactions arrive and I assemble a new block that's better so I give that new block to the miners, and then some more transactions arrive and I create a third block and I'll keep doing that.

**Danny**
*  all right, so it's a continuous optimization, not just a discrete optimization, so make it the next block.

**Peter Sziagyi**
* Basically, any time a transaction arrives, there's a chance that I can make a better block, so I need a signal to avoid making new blocks. Perhaps the signal will be a fixed head as well.

**Danny**
* also, if the execution engine is more than a slot past the last calls for the slot, you know that no one's going to ask for it even if there's some kind of time explanation but then you're starting to make assumptions about time and the relationship between the two, which is probably not great yeah so.

**Peter Sziagyi**
* I suppose this is a kind of open question for us first spec, but I'd say just ask for it once and if I have a block, I'll give it to you; if not, I'll make one and give it to you; and as long as it's quick enough, it shouldn't be a problem all right yeah okay cool yeah great.

**Mikhail Kalinin**
* Well, so it's much clearer now, at least for me, so I think we can move on to the consensus.

# [Consensus discussion](https://www.youtube.com/watch?v=ODcNpWiLASk&t=3190)

**Mikhail Kalinin**
* So yeah, engine to the consensus so yeah, I have a few things to address here and there and some updates okay so the first thing for consensus is that there is an understanding of an enhanced transfer mechanism which is basically like.
* We have a transition epoch, and when the epoch occurs, the consensus node decides on the total difficulty of the transition total difficulty. This could be done by taking the current take the difficulty of the most recent block multiply multiply it by 10 or and setting this as the offset for this total difficulty and computing the total difficulty that will occur in the future what is great about it.

**Danny**
* Take the most recent e1 data because it is understood to be available on the client right now.

**Mikhail Kalinin**
* That's what I was going to ask, which one to use, because if we take the most recent block, it would have to be some sort of decided upon by all, which includes some additional agreement mechanism method, but we already have this f1 data voting so that might be right so when transition epoch happens yeah.
* So the eth one data that are in the state right we can use this block hash to get the difficulty and add the difficulty to the most recent block probably yeah so there actually the why is this a good idea is because we have um the exact point in time regardless of what difficulty would be on the network and we have this kind of total difficulty mechanism preserved which has its benefits.

**Danny**
* And transfer epoch is basically a beacon chain fork because that's the stage at which you modify the data structures to help the execution payload even though they're null, and then there's a fork that actually occurs.
* When the fork occurs, the actual change in update of the consensus code occurs with a lead time before the actual transition and places the new code in place, and then the transition occurs, and then doing it as a function of that dynamically makes sense uh because it also removes another thing miners can potentially play with, like if 75 of the miners go offline, you know they don't.

**Mikhail Kalinin**
* Well, so the open question here is how to compute this transition total difficulty what to use so we can think about it and get to this discussion. I will also think about how to do it like what potential ways of doing it we have um with relay with the relation to the inputs that we already have like in the beacon state and the beacon block and those that we can get from the beacon

**Danny**
* Yeah, I guess the actual worst case scenario in hard-coding it rather than doing it as a function of this transition epoch is that you get a beacon chain fork that adds new functionality, as if you set the total difficulty say three months ahead and miners actually sped things up, which is obviously difficult and unlikely, but they sped things up and made the transitions total difficulty happen prior to the actual forking of the code and this prevents that that kind of crazy case from happening.

**Mikhail Kalinin**
* Do you have any questions about the transfer process? Well, fine. Um, the other thing to talk about is the.

# [Execution Payload discussion](https://www.youtube.com/watch?v=ODcNpWiLASk&t=3463)

**Mikhail Kalinin**
* The execution payload size, which is the largest area here, is transactions, which have a mac size of up to 16 gigabytes at the moment, so we have to treat two separate situations where there are a few transactions with massive transaction data and a lot of transactions with no transaction data.
* That is why it is, because there are two constraints, namely the amount of bytes in each transaction and the number of transactions, which is why this 16 gigabyte is technically feasible and has the potential.

**Danny**
*  Should add some sense yeah the ssd sse lists have a max size because this comes into play and the structure of the mercalization rules and like the tree and so max like these stuff all have to have a max size and so when you take the max as the byte payload and max number of transactions currently then you get some crazy numbers like microsoft.

**Peter Sziagyi**
* So, as far as I know, the death peer-to-peer network has a message size cap of 16 megabytes, but gath restricts the east suburb packages to 10 megabytes, which implies that if anyone mines an 11 megabyte block, gas would be unable to propagate.
* If someone mines a 20 megabyte block of ethereum one, clients will be unable to propagate it with the current specs, but that doesn't mean we can't upgrade it, patch it, or expand it; this is just a mental notice, okay?

**Mikhail Kalinin**
* Well, I think this is the way to restrict this kind of stuff on the network, by simply restricting the size of gossip messages.

**Danny**
*  Yeah, on the beacon block gossip caps, you can win gossip validation requirements, and you can certainly manage it there based on maybe a feature of like gas cap so and so forth.

**Mikhail Kalinin**
*  We already have these kinds of boundaries in the gossip, if you know what I mean.

**Danny**
* We do have validation criteria, and you may easily add this.

**Peter**
* Another thing to bear in mind is that, at least with the ethmoid network, we've found that unless you have a quite very beefy link aka amazon, you have so for snapsync we're using half a megabyte packets and I can request packets from quite a few peers simultaneously and we've actually managed to overwhelm the local node with requests.
* So we've had timeouts not because the remote node isn't sending us the data fast enough, but because we simply overwhelm our own inbound bandwidth with data and it takes too long to bring it through. In essence, what I was saying is that once you get to this half-megabyte message size, things start to get weird.
* So, once again, I'm not sure what the long-term targets are for scaling stuff, but we should definitely keep in mind that network messages should be of some variety.

**Mikhail Kalinin**
* Okay so get it the app is to limit it on gossip even the gas limit should work but yeah I don't think like this is the gas limit will be checked after the message is received because if there is like a 16 16 gigabyte message nobody wants to download it so it makes sense makes a lot of sense to reduce to to get just refuse this kind of thing something on the gossip network s

**Danny**
* Agreed.

**Mikhail Kalinin**
* Okay, the next thing is specific to the structures to the execution payload we have the we are going to have like multiple transaction types right on the mainnet or we already have them since berlin so the default option for the consensus side is to not deal with these different transaction types and just use this op transaction approach which is just the representing transaction as an rlp string and just which is working from consensus standpoint.
* It's just a string of bytes um and have like this introduced this is what it's already done but we can also introduce the union type with like a park selector which will allow for now just one type this string of fights but will give us some forward compatibility with the next updates when we decide to like stem from a back transaction and have them explicitly in the executable.

**Danny**
* Yes, that is the plan. Uh, the concept is that when you incorporate transaction types structured in the ssd payload, you can get a little bit nicer proof structure rather than only getting the opaque rlp by load, but that for convenience, we can do opaque selector for now and then deprecate opaque selector with unique collectors in the future. I believe this is an idea from Proto. Do you have anything to add?

**Protolambda**
* So the current z-spec defines a union form. We do not use the union type, but we can boost it by defining it as a single prefix byte to the transaction and then defining a single selector for the back transaction for all of the current forms in their encoded form.
* Then I'm talking about the envelope, which includes the inner selector that applies to the ether1 data, but outside of that we'd like this structured data for nice miracle proofs, and for that we'd like to define other options in the union that are more structured with ssc, and then we get this second byte, which is also kind of like a selector that applies to all the new types of transactions after the merge.

**Mikhail Kalinin**
* So I think we should just do this at some point in time, so I don't think there's much to discuss in this regard here, so if someone wants to, if anyone has an opinion, let's discuss it offline.

# [Consider eliminating uint256 requirement on beacon-chain side](https://www.youtube.com/watch?v=ODcNpWiLASk&t=3970s)
**Mikhail Kalinin**
* and the last thing is the uint256 uh in the beacon chain stack which is used for complete difficulty which is around 72 bytes I don't remember well you which is uh like just exceeds the unit unit 64. And we need to use something larger, so the first choice is not to exclude it entirely because it is not used in any arithmetic except for contrast..
* So the spec simply compares whether the change total difficulty has already occurred or not, and yes, it could be done. The other alternative would be to, I don't know, denominate it in some way, but that would most likely necessitate some distinction happening on the um execution engine side because it returns little difficulty. I don't think it's likely to succeed, but it does necessitate additional, well, work. I'm not sure which approach is preferable.

**Proto**
* I believe I skipped the fact that you're searching for an encoding for a large integer in if2 uh.

**Danny**
* Basically, we've avoided bigent's arithmetic and he's two on the node side so far um and right now there is a big end yes right but it's not going to be encoded it's just got from the execution engine compare it to the constant.

**Mikhail Kalinin**
* No, it's not going to be encoded in ssd structures.

**Nethermind**
*  I'm sorry, but I don't understand why the execution engine returns summer complete difficulty to the consensus engine. This is expected for the transformation procedure's transition phase.

**Mikhail Kalinin**
*  So the transformation occurs after a certain total complexity is reached.

**Danny**
* Right now, the beacon node simply does not have big end arithmetic, so the total difficulty should be denominated in an un64 and a bunch of the um precision removed, and you'd still need a function it returns that with the lesson precision.

 **Mikhail Kalinin**
 * Yeah, so the question is how difficult it would be to implement in 256 on the beacon chain side, and if it's not too difficult, I'd like to leave it there.

**Danny**
*  If any of your clients want to speak up, please do so.

**Terence**
* It's not too complicated for us to shift, Terence, and we do use speaking in some places.

**Meredith Baxter**
* Yeah for Terence i don't see it being difficult.

**Meredith Baxter**
* We already have a beginning for f1, so we can change it.

**Danny**
* great, let's uh ask the lighthouse people as well, but let's just act as though we can do a big end comparison for this one little thing before we hear otherwise.

 **Mikhail Kalinin**
 * Yep great yeah, so let's just leave it as is and if there's a problem, we can change it.

**Jacek Sieka**
* Okay, if it's only for order, you can do a byte-by-byte encoding uh contrast with the proper encoding.

**Mikhail Kalinin**
* Oh yeah right yeah but you will receive it uh from why uh in json format I think yeah but you can I see if it's encoded you can compare and compare it as like.

**Mamy Rasimbazafy**
* lexicographical collection that's like an exact decimal type but otherwise, more difficult.

**Mikhail Kalinin**
* Okay good anyway, we have about 15 minutes here, let's go to Rayonism and update so Proto do you want to sorry?

# [Rayonism discussion](https://www.youtube.com/watch?v=ODcNpWiLASk&t=4269s)
**Proto**
* Sure, in the last week or so, we've had a couple of these office hour cars, which are more casual cars where you can remain on the cutting edge of Rayonism.
* But we looked at the first devnet in how to plan the genesis and then also chatted with a few clients about how we move forward with the rpc and now we have this one genesis tool ready to go to prepare a test network.
* We have a guide for anyone who wants to set up their own test nuts on how to use this kind of thing, and I think we should basically concentrate on the rpc on upgrading to the new spec and then we'll be ready for the first prototype devnet.

**Mikhail Kalinin**
* thanks, um i'd just go through client updates um on where everyone is with regard to ray and is um yep so maybe we can start from geth.

**Peter Szilagyi**
* so actually the first uh first version was the decision was that uh we're going to keep Guillaume's api updated to I mean it will be tweaked and updated to validate to whatever spec the new api is but otherwise it will still be focused on directly only injecting data into the chain something else

**Mikhail Kalinin**
* Yep, that's fine, but never mind.

**Nethermind**
* So, we have an initial implementation that I am currently testing. I expect to finish testing and stabilizing it by tomorrow, and if any of the eth2 clients would like to engage in testing integration with the rpc, please contact me. I would be very happy to work on anything like that, for example, tomorrow.

**Mikhail Kalinin**
* cool yeah great so um actually work on like taku i'm going to to you it's going to be ready tomorrow so I think I can experiment with catalyst and with another mind as well so just reach out yeah cool thanks everybody from open ethereum to turbo gas, bazoo, and abezu is starting to work on this back as well okay cool 

# [Consensus-layer discussion](https://www.youtube.com/watch?v=ODcNpWiLASk&t=4521s)
**Mikhail Kalinin**
* So let's just go to the consensus um clients we can we can uh we can be managing clients so as I said takuru um should be ready by tomorrow I guess uh we'll test with catalyst first then try another mind hopefully someone else do bagath and know what's their status is so.

 **Terencen**
 * Yeah, I'm still not making much progress on the api side from my end, I'm still reviewing the changes so I think once the api becomes more formalized I'll put it to one side it'll probably take me a while to catch up so that's not too bad other than that we built a faucet and for our regism it's fully configurable it comes with a ready react and angular project as a reference it's also dockerized so

**Mikhail Kalinin**
*  Yeah, thank you very much for this falset um serious all integrated I think in the first stage net i'm just dropping the guide on how to run prison that you listed okay nimbus members do you have any updates with ricardo rennis?

**Zahary Karadjov**
* we're working on ryan ism now we have a pr but at this stage we're playing with catalyst but it's not here we'll be ready for the first testament that's our target we still have a little bit more work to do in the rpc interface between members and catalysts.

**Mikhail Kalinin**
* okay great someone from the lighthouse nobody's here anyone else want to give the an update okay great thanks everybody

**Nethermind**
* I have a question rather than an update; if possible, could you provide a rough estimation of the dates and plans for the devnet?

**Proto**
* Sure, so the original idea was to start the devnet sometime in the first week of the hackathon just as an experimental short left and it's like okay whether you join later or otherwise but this is this kind of opportunity where you just look at can we try the rpc in something more of a shared devnet and so I just like to try and spin up some kind of prototype we have in the next week.
* I have this example configuration for the first deafness up in the realism repository, which I'll share again in the chat, and there I specify Monday as the ethereum one uh genesis and this can be skipped and then then stay as the actual genesis because there's this delay of knowing the exact genesis state of the theorem one and then from there you can compute the one for ethereum two and so on.
* I need I'd like to confirm this, and I'll probably wait for one or two more office hours to hear about client preparation.

**Nethermind**
* Thank you very much.

**Mikhail Kalinin**
* Any other discussions questions or announcements something else before we wrap up nice i'm sorry for screwing up the call this zoom connection, that so okay thank you so much for coming see you tomorrow next week next month um every time so bye bye thank you bye bye everyone.


-------------------------------------------
## Speaking Attendees
**Mikhail Kalinin**
**Proto**
**Zahary Karadjov**
**Terencen**
**Peter Szilagyi**
**Danny**
**Dankrad Feist**
**Gullaume** 
**Mamy Ratsimbazafy**

-------------------------------------------






