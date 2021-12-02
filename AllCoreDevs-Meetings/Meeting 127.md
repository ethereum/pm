# All Core Devs Meeting 127
### Meeting Date/Time: November 26, 2021, 14:00 UTC
### Meeting Duration: 1 hour 30 min
### [Github Agenda](https://github.com/ethereum/pm/issues/416)
### [Video of the meeting](https://youtu.be/js4HLK4MyQI)
### Moderator: Tim Beiko
### Notes: Alen (Santhosh)

## Decisions Made / Action items
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
|127.1 | To have devnets that stable with clean branch with command line flag for the non-client people to use over the holidays  | [29.04](https://youtu.be/js4HLK4MyQI?t=1684)|
|127.2 | Client team to have a prototype of 4488 in next two weeks  | [88.03](https://youtu.be/js4HLK4MyQI?t=5284)|
|127.3 | Ansgar to look at the worst block in the current packing algorithm  | [91.20](https://youtu.be/js4HLK4MyQI?t=5455)|
 




## Intro:

**Tim Beiko**
* Hello everyone. Welcome to AllCoreDevs 127.
* First thing quickly before we get into it, we have the Arrow Glacier happening in two weeks for anyone listening. So it's happening now on December 8th. if you run an, if they're a maintenance mode, please upgrade it in the agenda for this call. There's a link to the Arrow Glacier spec with the, release versions for all of the clients. again, the Arrow Glacier  is just an upgrade to the difficulty bomb, so it doesn't do any kind of substantial changes. and yet you want to upgrade before December 8th or block 13.773 million with that out of the way. yeah. So, Mikhail I saw you had a couple points you wanted to discuss about Kintsugi. I think we could probably just get a quick update from the different client teams and then, and then dive into those. yeah, I don't know if any team wants to start and share kind of their progress over the past two weeks. I know there was some sinking, that was happening this morning or last night and I'll call on Marius because I don't get was the, one of the syncing clients would I think PICU. 

## Merge Updates

**Marius Van Der Wijden**
* Yeah. Yes, I can. I can go first. yeah, so the devnet zero, I'm not sure if we talked about Def net zero on the last call, but definitely zero, basically broke because I ran two minus, at the, at the head, which meant we had like two competing, proof of work blocks and, clients were not able to, to, fork to the correct one or like two to two to a fork after, after the proof of work was, after the proof of stake chain started, which meant that like half of the network was on one chain, half of the network what's on the other, chain. this is not really fixed yet. So we have to, think more about how we can, make sure or how we can, work with these, like these folks around, the, terminal proof of work block. and also maybe how we can, show that to the user, to make the user where, that there are two folks and that he has to decide between them. and then, like we can have a social consensus on like the, the right proof of work block and then build on that. And, yeah, that w there was, the first step net, the second or devnet one, zero-based, definite one, broke because I, made, like I wrote a book, and, and, yeah, but we have updated guests now and we, fortunately another mind was correct, was correctly, producing the chain and we, then, fixed GAF and sent to the chain. And I think, currently on, on the chain it's, another mind guest, E piece. So, I'm not really sure. and for the consensus, layer clients, loads, light house, take who the currently running, I think. And, yeah, it's, it's, it's going, going. Okay. and I also tested today, tested the optimistic sync, with, with, Teku, which like the, there was a bucket that prevented Chico from optimistic sinking. but that is also working nice. So Teku team, it works, it was just the bug on our side and the going to fix it. That's basically it well.

**Tim Beiko**
* Yeah, great progress. 

**Marius Van Der Wijden**
* And anyone from any of the other client teams want to add some more context? 

**Marek Moraczynski**
* Okay. So from Nethermind to, we have to do several not critical fixes and quite lot, lots of forever factoring. our sync process allow us to work in any devnet. However, this is not our final solution. We plan to rebuild it. we are in sync and we are producing blocks on. So definitely like Maurice side. it seems that Nethermind  is working fine. and we will definitely continue testing different client combination. Yeah. I think that the  update from Nethermind, 

**Tim Beiko**
* Thanks anyone else? 

**Gary Schulte**
* Yep. From Besu, we've implemented the consu spec and, we've successfully interrupt with, merge Mach. but we have been focusing more on trying to get our merge branch emerged in domain. And, we haven't tried to interrupt on the dev nets yet. we're at a point now where we probably could do that, but we aren't at a point where we can do that with, the main branch. So, yeah, it will probably jp in with, a client from, our merge branch instead. 

**Tim Beiko**
Got it., Andrew, you have your hand up, 

**Andrew Ashikhmin**
* Right.  So for Aragon west, we're still developing, the knowledge that we, so we haven't been able to, sync yet. I have a question about the merge. So now , we will have, EIP-4399 as well. and, there is, no, button, but if, EIP-3675 says that mix hash should be zero while in EIP-4399 We are reusing mix hash. So can we actually clarify 3675 So that mix hash, doesn't have to be zero. 

**Tim Beiko**
* I put in a PR I think two days ago to clarify that. 

**Tim Beiko**
* But you could Danny that you wanna explain. Okay. I think I can, again, yeah. So w we, we put in a PR in 3675, I think we just added a note say, Mike, that these parameters that are set the zero can be overridden, you know, based on subsequent EIP. didn't want to asse that like, every implementation, like if there's another network or something that wants to use 3675, that they did also use 4399. but yeah, just tried to make it clear. and yeah, the 4399 does superseed, basically, 3675. So you do use the mixed hash. Cool. Yeah. Let me tell sharp PR in the, in the chat. Cool. 
* Perry. I see you have your, your, your hand up. 

**Parithosh**
* Yeah. so while the aim of mainnetwork, wasn't a test, execute like random transactions, etc cetera. There is however a forcep deployed. So someone has interesting edge cases. They want to try out, please clean some Ether, tested out. I'll also just share a couple of more resources. So if you find something to break, feel free to, but it could, 

**Marius Van Der Wijden**
* Also if, people are, testing the execution data that there's a, 4399 transaction or difficulty before the merge and random upcode after the merge. So, both in the testnet. So if you don't have all 4399, enabled, then you cannot sync the post-match change. You will crash on block 1641, I think so, just FYI. 

**Tim Beiko**
* Cool. Any other updates from teams working on this? Okay. in that case, Miquel you had two issues you wanted to discuss, the first was the message ordering for the, engine API and how do we reset the request IDs? 

**Mikhail Kalinin**
* Yeah. So there is the PR two engine API that refines the message order in section and the one corner case was, yeah, it's dropping be yeah. Or thanks them. Okay. So there is a discussion about one edge case scenario. let me just give a quick context. what's, what's the edge case is, so we are, it's very important that fork choice is updated Messages are propagated in the same order as they appear in cl. And, for this purpose, we use, requests that JSON RPC  request IDs. So they must be constantly increasing and EL must not process, pork chops, updated medicals, if they have the ID that is lower than the previously processed call of this method.  that's how it's, that's how this PR, proposes to, to adhere to that message or to do the audio, focus, updated having an OCL and, the edge case, then, suppose when cl just when the fly and got back and get back. 
* So, it will either need to persist, the request ID to start from the same value, otherwise, or we need to reset it somehow. Why engine API, otherwise, the counter we'll start, we'll start, like, let's say from some default value, which is one or zero and execution layer. We'll have to, if it's, if it follows this back with, we'll just have to reject those messages, until the time when the counter gets back to, to do the same state and it wasn't before the restart cl clients. So in the proposal for a second discounter is just, executionally our clients see that, the request ID is zero. Then it means that we counter, sat down count and starts from zero and goes onwards, that's it, 

**Danny**
* This seems totally reasonable to me. The edge case's is even worse than that. It's not just like one single cl resetting, like cl a should be able to be swapped for CLB transparently to Yale. And so anything that you have to persist across those two layers to be able to communicate after that swap is worse than just resetting CLA. so I would, I think that the zero makes sense to me. 

**Mikhail Kalinin**
* Is there any, like a position to implementing it this way, or if yes, you, you, you let's discuss it now if, if not, if there is no strong a position in which just go through these threads comments, put a comment there, otherwise, I guess it will the merged, with the, this proposal, this reset mechanism. 

**Daniel Lehrner**
* Cool. And, there was a second, issue you wanted to bring up also to add, Eth get blogged body, or sorry, engine get logged bodies method. 

**Mikhail Kalinin**
* Yep. yeah, there is, it's, it's a proposal yet. It's, it's not even a PR, it's like a request for comments, but, that we can drop the issue. what is proposed is to, implement, get block bodies and methods in engineered BI. It allows for pruning execution payloads on a sales side and say, like potentially a lot of space, on the desk, in this case, the cl clients will request the block bodies, which is just it's transaction-based, after, after the merge, and, w whenever it needs to serve a block, beacon blocks to their node PR or to the user at all, just go, to, you know, under request by, bodies and request transactions of those payloads that are supposed to be served. one thing we're mentioned here is that this get blocked bodies maps on the protocol. So it, I, I'm assing that it's pretty straight forward for execution layer clients to implement, to expose this logic, this same logic flag engine API, because basically the logic already exists, and we just need another one interface to be accessible. 

**Peter Szilagyi**
* Question, the response. Do you expect it in json format or included? 

**Mikhail Kalinin**
* It's basically, it's, it's the array of bytes, according to EIP 2718. So it's either ROP or binary, encoded transaction, according to this EIP. 

**Peter Szilagyi**
* Yeah. We'll keep that as a single transaction, but the recent transactions through our sentence format in, or whatever that is. So not the JSON format, rather the binary form, 

**Mikhail Kalinin**
* Right. It's it should be, yeah. It's encoded transactions. It's not our LPN code. It's array of transactions. Yep. 

**Danny**
* I'd say something like, this seems very reasonable. if this becomes a complexity, though, I think it can be a optional on, at the point in the merge and something that's pretty high priority to get in place after not, not that I, or even just utilization of the printing mechanism, even if the, the method exists. but I think the duplication doesn't make sense. 

**Peter Szilagyi**
* No, I mean, the, the foundation on these things by lines. So I was saying that the implementation of this exhibition, they are site is five lines of code. So it's reasonable to just add it to the stack as mandatory it's zero effort. 

**Danny**
* Okay. So mandatory as part of the spec, but, whether Cl is doing pruning at the point of merger or not, can be, 

**Peter Szilagyi**
* Yeah, I mean, you can do whatever you want. There's mandatory then you know, that the client will be able to serve you so that you can swap out on site for the other. 

**Tim Beiko**
* Does anyone think we should not include it or like, have it as an optional? Okay. I guess we Cal you have your feedback, 

**Mikhail Kalinin**
* So thanks. Sense to open a PR probably, or, yeah, I'll just wait for some sometime probably open the PR next week. 

**Tim Beiko**
* Cool. Anything else about the Kintsugior or the current merge implementations? 

**Mikhail Kalinin**
* I was going just to say that we are about to release the next version of this Kintsugior spec pretty soon. they need to be one Ted's anything here. 

**Danny**
* Yeah. so I think as Yolo where the devnets are now launched on Tuesday rather than Thursday. and we had spoken about attempting to do the persistent tests at the next week or the week after I think given progress and given some of the iterative changes that are still coming out on the Kintsugi specs. I think we'll be able to conse V3, by about Monday or Tuesday. I would suggest that we are aiming for the persistent testnet, that launch on the 14th rather than seven. just to give us time to, I would say to give you three specs are out Monday or Tuesday, so then the seventh can be a V3, devnet and then the 14th is going to be the, persistent test. Not assing things are going well. I know that begins to push us close to holidays. I think it's at least reasonably far away from Christmas. but, obviously open a feedback on that, the shift in the timeline 

**Mikhail Kalinin**
* At what answering the question marrows has, yeah, we'll, we'll have the change log and the Kintsugi spec in the table. 

**Tim Beiko**
* One thing I'll point out for, the client team. So if we do aim to have, say a devnets that stable and that we want basically non-client people to use over the holidays, I think it was in for, maybe Coinbase mentioned that just having it in master with a flag, really helps. yeah. So just, if, if that's something that we can aim for on the client sides for like the December 14 release, I think it will help just get more folks onboarded to it. 

**Peter Szilagyi**
* Not going to happen. Nah, I mean, if you were, if the requirement for possible have the everything virtually verse on the master. 

**Tim Beiko**
* Got it. So it's still easier to keep it on a branch by then. 

**Peter Szilagyi**
* But the problem is that once we merged something to master it's,  it's I mean it, or I would certainly say past few years, and my previously going to just dig it up again to see if there's something wrong with it or not. So it's kind of us. 

**Tim Beiko**
* Yeah, fair enough. I think, yeah, in that case, you know, having like a clean branch, we can point them to you and, and if it's possible to have a command line flag on that branch, that's, that's probably as good as we can do. 

**Peter Szilagyi**
* Yeah. That's the reasonable, 

**Tim Beiko**
* Anything else on Kintsugi? 

**Peter Szilagyi**
* Yes, Danny will be away for the next, few weeks, the month. so you're stuck with me and Miquel 

## EIP discussion

**Tim Beiko**
* So, okay, so we had two other topics from the last call that, that we had kind of bucketed, basically how we do fork IDs for the merge and, the discussion around the EIP for 4444, and how, you know, we want to go about potentially implementing that after the merge. I think it's worth, maybe moving to the next section first because it might affect those discussions. So in parallel to that in the past two weeks, there's been a lot of discussions about, transaction costs on roll-up and how we can, potentially help alleviate those. And there have been two proposals kind of brought forward, which would, kind of reduce the call data gas costs in different ways, potentially with the desire to see if those could be, brought to mainnet fairly quickly, given that, one of them is a delivery, one character change. so I think it makes sense to maybe just have, the authors, if they're all on the call, kind of walk through those proposals wider, valuable, and it gets some general feedback there and that, yeah, the impact of those probably the turbines, like how we want to deal with fork IDs and, and what we have to do with regards to historical data. so, let me see if I could, yeah. Is there an author of either of the EIPs that wants to give context? 

**Vub**
* I'm happy to talk about EIP-4488. 

**Tim Beiko**
* Sure. Okay.

**Vub**
* So the idea behind EIP-4488 is that, that it's decrease the call data gas costs, from 16 gas per byte, two or three Gas par bite. So decreases with buying more by more than a factor of five. And to this, it would make roll-ups five to five times cheaper. so like something like, I think on average optimism and arbitrage tends to be around the two to $5 range. You would bring them up under $1 and then, Lupron and ZK sink are often about a quarter and it would bring them back, bring them back onto your 5 cents. the one extra fee feature that the CA he has is that it also adds a separate call data size, limit per block. so it says that Asia block, can have at most one megabyte of total transaction and called data plus a 300 bytes for every additional transaction. So this is, like in terms of code it's fair, it's still fairly easy to implement that a, it's a one-line function, but in terms of consequences, this basically this does mean that instead of having a single dimensional limit, we have Asia two dimensional limits. So there's a limit to gas and, there's a limit to call data. And historically, I think we've been wary of adding two dimensional limits because two dimensional limits make the algorithms for, figuring out, well, what transactions do you include harder because you can't just like take the top priority fees and the next priority. And then, and then the next priority for you and keep going down until you run out of space. so there's a, so the EIP has a couple of mitigations to this. one is just the facts that we already did it yet. The 1559, based means that the, the, the nber of case, like most of the time, blocks or the constraint is not going to be block size. Most of the time, the constraints will just be like, you take everything that's willing to pay. That's willing to pay the base fee until the, until the memo about level clears. and then also the, just the facts that the limit is fair. the limit is quite high. I don't think we've even seen a, bill today that rise to anywhere close to that limit. And so the average somewhere around 15 times, less than the limit, and also this extra stipend of a 300 bytes per transaction, which basically says, even if you create a walk and walk shows up to the RTV call data limit, you would still be able to keep on including transactions with less than 300 bytes or less than 300 bytes of full data, which is on average, about 90% of all of the, of all of the transactions in the memory. So the reason behind this limit is basically to, it, because historically we have been concerned about the possibility of that, if there is a really, really big block, then that would just temporarily crash the network in a ways, in ways that we don't, that we don't fully understand because we haven't really had blocks of that size yet. and, and so this is basically just a keyhole solution. It says, well, you can't have, blocks that are larger than, than a level like, which is somewhere between one and one and a half megabytes, which has, actually the same limit, like actually lower than the current, defacto limit of, of blocks like today. let's see, radically, we are just more deconstruct as a 1.8, 7 million bytes. And then with this, w with the limits in the EIP, what would be between one and 1.5 million bytes, depending on the amount of gas of gas and the nber of shares. Okay. 

**Tim Beiko**
* And maybe before we go to comments, it's worth just highlighting and also kind of the  proposal, which was, 4490. So this one would basically basically propose this to just reduce call data from 16 to six. so a smaller reduction, but then does not add these mechanisms to cap the amount of call data in a block or the transaction stipend. So it's just like a one line change to, the actual gas cost of, call data in transactions. And Micah, I see you have your hand up. Okay.

**Micah Zoltu**
* It's for comment, you said no comments until after you talked about that. 

**Tim Beiko**
* Oh, so sorry. That was like the overview of the second proposal, basically like, 

**Micah Zoltu**
* Yeah, 4488. Why have the Gas per block as a function of the nber of transactions in block, rather than just having the gas per block, you get fixed value? Like if our goal is to targets for big, why don't we just say, 

**Vub**
* Right. So this mitigates to the, the two dimensional, optimization, problems, like basically that, the problem with adding any kind of extra limit other than the gas on it is that it means that the naive algorithm for filling the blocks is not going to be optimal anymore, which would mean that like either, we have to, actually implement some much worse if it's a sophisticated algorithm, or, blocks created in a non-standard way are going to be more, more profitable. And so like more people are going even more blocks. They're going to be great if they're flash plus. so the idea behind the 300 bytes stipends per transaction is basically that if you still create a block using the current naive algorithm and your block shows up to the call data maxim before you run out of transactions, or before it hits the gas maxim, that you would still be able to keep on, including any transaction with more data, less than 300 bytes. So you'd still be able to keep on including 90% 

**Ansgar Dietrichs**
* And just prefer to that. Like, it's important to note that basically in the extreme scenarios, so like say roll-ups become very, popular while this is an effect, and you have a one big roll up transaction, every single book, more or less, that would fill up almost all the call data. this would also start interfering with the 1559 I with them, right? Because basically if you don't have a stipend, then after this roll-up transaction, that could only be  Eth transfers because those are the only transactions that don't conse any extra call data. but you might just not have enough, Eth transfer demand at this kind of base fee level. And so the base you would be at officially depressed, and then you basically have the, the, of transactions doing a first place auction again on the, on the, on the, priority feet. So basically this is just insurance that blocks can be produced as normal, Right? 

**Vub**
* So like in that kind of extreme world, basically the roll-ups would sometimes end up competing by priority by setting high priority. And if you're a transaction, isn't one of those 10% that has really been all data, then you would have to push your priority fee up to compete with the roll-ups. But if it's under 300, then you would still be able to, get in with a pre with this game, usual priority fee of ones with rain. 

**Tim Beiko**
* Andrew, see, you have your hand up, 

**Andrew Ashikhmin**
* Right. I'd like to relate Alexis concern and his concern is that with this change here, we might incentivize, we might actually prohibit the adoption of data sharding because the input data on the execution layer will be so cheap that actually nobody will be incentivized to like to move to data sharding. That was his concern. 

**Tim Beiko**
* Got it. 

**Danny**
* Let me do a quick rebuttal or on that before we move on. Yeah. Go for it. Oh, just the data sharding one would have eventually much more capacity than what it can be provided there and does not have the competition mechanism for, additional execution. And I think naturally you would see the mood state charting because one that would be, like capacity would be exceeded, and like a combined cheaper data elsewhere. if that actually became a problem and like the overuse and abuse of that mechanism, you could have a fork to up the guests, price of that after you'd had sufficient data sharding. 

**Tim Beiko**
* Right. So this would be kind of a temporary fix and that's worst case scenario where, 

**Danny**
*Yeah, I'm not necessarily advocating for having to update it, but that is something that could be done in the future if we, if we really needed to directly incentivize moving to data shards. But I Suspect that 

**Dankrad Feist**
* Generally there's a strong case for just, revising this change when we have data shards by why not 

**Tim Beiko**
* Great, I guess. Yeah. One thing, in the chat, that enscar said is obviously sharding is probably still a couple of years away. so it's, you know, kind of a medium term problem contrasted to like the current state that just high fees on the network. Martin, you have your hand up. 

**Martin Holst Swende**
* Yes. And we're wondering about possibilities to game, this algorithm, so say you're a miner and you've just filled it to the full base facts, quality per block, but you have personality juice, the transaction about 600 bytes that we want to include. So therefore you make three tiny, tiny transactions. that just, I don't know, or at the minimum that fees you up gives you another 900 bytes that you can put into the block. Is that something that can be simply happen? And is that something we should think about and be concerned about? 

**Ansgar Dietrichs**
* Right. So actually, this is, in a sense intended. So basically the idea is to say that in a block, the first megabyte of data is really cheap. You basically just get that more or less for free, and you just have to pay the normal, call it a pricing that the reduced three bites three is the guests by bites, but then afterwards called it, it just becomes really expensive, meaning that basically for every 300 bites you want to conse extra and turn by just like super tiny fraction of one megabyte, right? So then for every 300 bites, you want to put some extra bits that you have to include one word transaction. That's like the, the minim of 21,000, a thousand cuts. And so, if you really like, if you're in this situation, they'd say you have a 600 bytes transaction, and you're really willing to pay quite a bit to get that in the evening. you know, you're not falling into compete for the prime spot in the beginning of the book, it's perfectly fine to even, I don't know, say it use flashcards to create a bundle where you add an e-transfer in front or something. Again, this would be like a super rare what round, but the, the, the, the risk of the idea is just that it makes, call there to after this first megabyte expensive. It's not that there's a hard cap of 200. 

**Vub**
* Yeah. You don't actually need flashlights. You just send a series of transactions with the same Ascender and sequential.

**Ansgar Dietrichs**
* That might end up in a different box though. 

**Vub**
* Ah, okay. Yeah, that's true. 

**Martin Holst Swende**
* Yeah. So what I word it basically, or what I see as a potential problem is if we suddenly start getting these padding transactions included in the block, just to push it a bit further, which, but the, the pending's actions are basically useless, and just take a box space. 

**Ansgar Dietrichs**
* Right. But there's just like, so depending on actually would only be a workaround for inefficient mining algorithms. So, because if you actually, if the miner is runs, the mining node that actually can deal with this, then it kind of just reorder certain sections because they like it again, the trend bites is chosen the way where like 90% of its actions are below it. So if you basically, once you kind of deduct the big one, I go by drill up protection. the rest of the block kind of like almost an old circstances would on average conse, less, less call data than 300 per, per transaction, basically smooth over over them. And so kind of like the only problem they can kind of kind of cursed us that if the miner, they easily assembled to the blog, they might skip a transaction with 600 call that even if, if they just ran all of them, it would still on average, just work out fine and the blocks would be valid. 
* And so if they're smart about it, this will just never happen. And so this is really, basically just a work around for, either minus that just drowning in inefficient mining algorithm, or the very occasional block where the average is, even, even for, like for after the, the, the big, college transaction is through, it, average quality size is still about 300, but like, this might be worth two bucks, but I would just asse that it's correct. I don't want one block a day or something. And then to having like two or three pending transactions a day, shouldn't be a problem, 

**Vub**
* Right? Yeah. Like, basically as that gets, a very exceptional case, because it would be both for the subset of transactions that is bigger than 300. and for the, transactions, in those particular, in that, exceptional case where call the data actually is going over the camp. and also the other, it would have to be a situation where priority fees are getting so high that, like padding with, junk transactions is a, a cheaper strategy for the, for the standard than just a mopping up. They're a priority for you. Right. Cause if you're willing to, add on, a bunch of junk transactions, then you would also be willing to add on a, a pretty priority for you. so that is, that would be my answer if we really want to admit it to, to make this a, not an issue, we could basically say, that like, there's the possibility of not redesigning the EIP. It's a basically say that the data under 300 bytes doesn't, like, increase the stipend. So instead of saying it's called like the total call data, that has to be a less than a million plus 300 times the nber of transactions, we would say the total nber of bytes exceeding the byte. Nber 300 of each, of, of each transaction can say, I can't exceed one megabyte. So I guess that would be an, like, that would be less exploitable. so that would also increase the nber of the nber of times in which that, in which the limit actually we get Smith, like basically, because just people's random accidental, or transfers would not, would not increase the limits. And we could basically say, that like there's the possibility of not redesigning the EIP. It's a basically say that the data under 300 bytes doesn't, like, increased the stipend. So instead of saying it's, called like the total called data has to be less than a million plus 300 times the nber of transactions, we would say the total nber of bytes exceeding the byte. Nber 300 of each, of, of each transaction can say, I can't exceed one megabyte. So I guess that would be an, that would be a less exploitable. so that would also increase the nber of the nber of times in which that, in which the limit actually gets net, like basically, because just people's random accidental, or ease transfers would not, would not increase the limits. 

**Ansgar Dietrichs**
* Yeah. And just for the record, if this would really be a sustained concern, then basically, I'm sure we would find someone who would be willing to just write an optimized mind algorithm that, that is smart about this. So, so this, yeah, so this won't be relevant if no one else would do it. I mean, I'd be happy to do it myself. 

**Tim Beiko**
* Lucas, you've had your hand up for awhile. 

**Lukasz Rozmej**
* So, is this possible that that will incentivize my miners to like keep the, a huge call data transactions and have an, effects, opposite of the desired 

**Ansgar Dietrichs**
* And why would that be the case? 

**Lukasz Rozmej**
* So for example, it makes the block smaller so they can propagate them quicker, etc.

**Ansgar Dietrichs**
* Right. So that's actually a good point. I think, if you, if we look at, say the conversations around what is the expected, optimal priority fee, there was some kind of reasoning that like we would expect a priority for you slightly buff, one way, to account for the increased ankle risk of, basically, having a bigger blocks. And so it could well be that indeed minus choose to, demand a priority fee of about one way specifically for big collector transactions, right? That this would be a trivial rule to add. You could still get the call at 10, if it's some threshold to basically say, okay, I ignore transactions. If they don't at least have 2, 3, 4, or five way, whatever the minus choose to count the bank risk, but this should like be just a normal, simple kind of economic decision. And it, and then there's this the simple level of, of the fee. So it might well be that roll-ups just have to pay a little bit more priority just to kind of like, make minus whole day. 

**Tim Beiko**
* And I guess in this instance, a bit more is not five X, right? Like probably not enough. 

**Vub**
* Yes. Yeah. And that would only happen in the, you know, like a dream world where we actually are getting net like a megabyte of roll-ups data, roadblocks, 

**Tim Beiko**
* Yeah, Dan  that I saw you, commenting same thing, about this this week. And I think you feel pretty strongly, this is something you should do sooner rather than later. So do you want to take maybe like a minute to explain kind of your position and like why you think this is really important and like yeah.And, and, and probably sh 

**Dankrad Feist**
* Yeah, I mean, I think, right. Yeah. I mean, I, I think like, is this like an, an amazing opportunity we have, like, if we think slightly less, like only about the tech and risk side, but also about, well, I've said before, it would be nice to have some users on all core depths, because like phased off, like hundreds of dollars are crazy. And like, everyone talks about this, like literally everyone in the crypto universe and like we're pushing users away left right. And center. And like, this would be the opportunity of a lifetime probably to like, show that we're doing something and actually be doing something. And in, I think actually sustainable way, because we do have a long-term solution for the roll-ups. So it's just like a temporary kind of subsidy you could say for the roll-ups in order to push the us. And, I, yeah, I, I would basically argue that we should try to just get this done, like even this year, even if there are some risks associated with that, but I think it's a nice, simple change. And, and, I think that would show the community that like, we really do care and, and if they're still alive and panting and isn't like completely ossified and can't even make a change like Dustin in several months. 

**Peter Szilagyi**
* Well, I mean, the theory sounds nice, but, I think you seriously underestimate the effects that it has on every other part of the system. I mean, of course it's one change to drop the mic, the gas limit, or the gas price, but, for example, get forensic image transactions to be maxim  138 kilobytes, not acute. All of a sudden you want a lot of transactions going up to one to two megabytes. If that's a gigantic change, that's an order of magnitude change on the network side, 

**Dankrad Feist**
* But do we need to do that? I don't see why we need to increase single transaction so I can roll up kind of  simply use like two or three transactions to, to load all that data on the, into the block. So I don't see why we need to change that. 

**Peter Szilagyi**
* Well, they would use, if you want to use a 1.5 megabyte that will be 15 transaction Or Not, for me particularly,

**Dankrad Feist**
* Well, I don't know how groups are currently constructed, but I think the teams are probably much, much better at making quick changes than we are. And so if they need to pack it into five transactions to make use of this, I'm pretty sure they will. 

**Danny**
* Yeah. There's two very clear clean mechanisms to do that. One is they just limit the size of the blocks and be able to check in multiple blocks in a single,  one block. And then the other is there already are mechanisms, optimism. This were optimism pre pre-loads the data in a free, in a transaction, and then use the subsequent transaction system. So check in the data. and so you could batch the, you could do batch list on the first, rather than meeting a monolith. 

**Tim Beiko**
* Sorry, what did you say the Vub? 

**Vub**
* I was just saying, does it start, we're using those tricks already because I think there are starts are going to be obviously bigger than 128. 

**Danny**
* Yeah, it seems likely. 

**Peter Szilagyi**
* So the reason I kind of brought that up because, I think the past week or so some of the, I think Arbor Trp was opening issues and I get people asking whether we could raise the actual limits to half a Mac. And, essentially, I mean, there's definitely a sweet spot. was kinda put there as a, as a Senator a little bit, cause we could go a little bit up, but, there are, so the problem is that as long as nobody's actually using 1088 transactions, or maybe there's one per day, it is almost impossible to, to see what the effect of this is on the lab work. 

**Dankrad Feist**
* I think that's an orthogonal issue. I mean, it's certainly something interesting as well, but I would say this has completely orthogonal to this, to this change. I would not say like we will make those changes. We have to make that change as well. 

**Peter Szilagyi**
* Okay. But okay. That name, the same vein. The other downside, which I think is also mentioned in with Alex EIP, is that the girl, so essentially if you, if all of a sudden, every block would max out its capacity, I think you mentioned that that would be about a three terabyte chain growth per year. So what do we do about that? 

**Micah Zoltu**
* And this, this was my comment as well, that I agree with what Peter said last meeting, which was that, well, we don't need to implement the EIP 4444 right away. We need to commit to implementing 4444 in the future. And 4444 of those don't remember is the one where we assert that we're going to start dropping historical bodies and receipts. with that then the, history, history growth is much less of a concern without that. Then I agree. That's like a big, big concern. so I would, I don't have a problem with EIP as long as it comes with the promise of committing to 4444 eventually, which means we advertise to users today that, Hey, we are going to be dropping history, rewrite your depths to not rely on infinite history storage. 

**Danny**
* I totally agree. And proof of stakes, which is a great time to begin to advertise that promise and to develop a group that figures out what the pain points are and helps resolve them, you know, on the order of seven, 10 fall months, time. 

**Peter Szilagyi**
* Yeah. So that's, that's what I was also on wanting to go towards is, I mean, it's, so the thing is what we of need to be aware of is what the timeline would be. So, I mean, we, we could commit to 4444 saying that, yes, we will start dropping, but we kind of need a realistic role attack plan for the whole thing, because just promising that we will do it someday. And then, the changes grows wild, in between it's is a bad place to be at. 

**Danny**
* I think that we can reasonably form a working group that pushes this out within, by the end of 2022. I mean, with an even more aggressive timeline, potentially being available. I think a lot of the changes, a lot of these things like don't have to concern this group directly. and so it can be done in parallel without taking a lot of resources from this. 

**Peter Szilagyi**
* Yeah, well, yeah. So from my personal perspective, if, if we can get the 4444 off the ground, I don't see anything particularly issue with it. probably daily. It will be a week. We have a big,  hiccupy when you have a sudden you'll have large box appearing. So I'm kind of curious how, how will that work? We'll take it. 

**Dankrad Feist**
* Wow. Yeah. I think we have tests on that right there. They read tests. I don't have the data in front of you, but it has been done. 

**Danny**
* Yeah. I'll drop the link right here. 

**Dankrad Feist**
* Maybe also comment on 4444. I mean, I think that is the assption for data shards already. Anyway, that's such a mechanism exists. So I, I see, like I see it as a, given that that's some point we both switched to such a mechanism, maybe a question on this. So right now, the only real concern about having the chain data, like realistically, I could run a node with dropping all the chain data, except that, I'm not a fully functional P2P client, right. That's people could request data from me and I can't, I can't give them those blocks because I don't have them. 

**Micah Zoltu**
* Also, there are large nber of applications out there that will not work if you don't have history, which I think is the harder problem that we need to do some community outreach, 

**Danny**
* Primarily receipts.Is that the mechanism that we're worried about here? 

**Micah Zoltu**
* Yes.There are some who also use call data, which annoys me greatly, but, 

**Vub**
* Yeah, like, are these, your implants stopped Stuart like reserving transactions and we'll do it in a year. I forget what the exact change was 

**Peter Szilagyi**
* In that same transactions. That's all that are older. So if you, you cannot look up transactions by hash, but if you know that you want as extra strong block five and you can feel it. 

**Vub**
* Okay. Got it. 

**Micah Zoltu**
* And that's what, and that's what a lot of apps do is they just troll through all of block history and ask for the logs for every single block in history. 

**lightclient**
* I think that's generally okay though, because if they're doing this to populate their own database and we can just require them to download those out of band and run them through maybe a more sophisticated client, but I'm like worried about the case where the dApps are literally calling your local client and they're requesting historical data. 

**Vub**
* Right. So I guess my impression would be that a lot of those applications are going to be increasingly slow in the world where you're not talking to you and if you're already right, like there's a bunch of dApps that already basically even had to switch to the graph because like using Ethere's built in like a log query and for very one-time spans, let's just do a slow, 

**Micah Zoltu**
* Yeah. The one issue, the one issue I have with that point of view is that we're basically saying everyone who built their apps to be censorship resistant, sorry, you're screwed everyone who is using a centralized server. Everything will be fine for you. That does that make sense? 

**Danny**
* Barely with being said, because being able to get historic receipts and compute them in some way, like, and help me get historic blocks, it could be them in somebody should be part of 4444. It's also being able to index them in a sane way should be part of 4444, 

**Vub**
* Yeah, I think it can be done and be, especially given that I'm expecting to have a serious, a serious push for the revival of a light clients and usage. and now that's, like, and especially past the merge now that we have Altera now that, very efficient, like clients are possible. and once they have like clients, then like if you have a one of interest model, then like dueling history where it isn't doing log queries and everything is pretty simple. 

**Tim Beiko**
* Just, I guess kind of bubble this up a little bit. do, so obviously there's concerns about a change to the growth, some concerns about just like the max transaction size, which are, you know, we, we can kind of sidestep for, for now. we, we spent a lot of time talking, earlier about like the kind of optimal block packing strategy. I, I'd be curious to hear like, just between the two proposals, like, do people feel like having, you know, a lower call data costs with a couple additional constraints is, you know, significantly harder to implement than just changing the actual call data cost, is the, or basically the flip side of that is whether just changing the call data costs, even if it's not lowering yet by as much is already kind of too much in terms of the worst case block size.So we would, there's not a world where we just lower the call data costs because we need some cap anyway. so I guess that kind of around the, about the way of asking, like, you know, is there basically like a proposal, people feel it is more realistic or like, you know, simpler to implement? yeah, just so we can kind of focus the conversation and otherwise more explicitly, like would say we just reduced from 16 to six and had no other mechanisms and no cap in the block and whatnot, but that the, you know, chain data growth aside, which would be slightly slower, than, than, producing to three, you know, would that be reasonable? 

**Vub**
* So that would be a, a maxim block size of five megabytes, 30 million divided by X. 

**Danny**
* Yeah. That seems worse to not have it. And I think the additional complexity is probably minimal to get the additional validation rolling. 

**Tim Beiko**
* Does everyone agree with that? Okay. 

**Micah Zoltu**
* I agree. As long as we're okay with, punting, the block stuffing strategies to searchers and professional block producers, and we just say, Hey, it's their problem. because in that case, it really is very easy to change as one line basically. if we want to force the geth team on their hands to go and design a better block stuffing strategy, then that, you know, core dev time significantly more, And they can just approve it. As a proof of state all their clients. 

**Ansgar Dietrichs**
* Yeah. Yeah. But I mean, just to reiterate there, like that, that's basically exactly what the stipend mechanism is supposed to address. So like, I mean, we talked about it earlier, like with the, even if you do the naive thing, it's already basically, you already get 95% to 12 optimal blocks. You have the occasional suggestion where it's maybe a little bits of optimal, but it's very close to optimal even, even with an. 

**Tim Beiko**
* Great. 

**Micah Zoltu**
* So if everybody's okay with that, then I don't have any problem with, 4490, no, the other 

**Ansgar Dietrichs**
* 4488. 

**Micah Zoltu**
* Yep. 

**Tim Beiko**
* Yep.I guess, can we get like a client team to confirm or say they have no idea and needs to, needs to look into it more? Oh, I see. Gary is I needed it. 

**Gary Schulte**
* Yeah. I was going to say, I don't think basically it has a significant portion of mainnet mining, but I think that we're okay with the making this change. 

**Tim Beiko**
* Got it. And Ansgar your hand is still up. Is that, just 

**Ansgar Dietrichs**
* This, this time it's actually on purpose. 

**Tim Beiko**
* Okay, perfect. 

**Ansgar Dietrichs**
* Now is, is this briefly one to, to, kind of try and bring us back on timeline discussion because, I generally agree that the kind of a general commitment to something like 4444, or just in general, basically that we say that in the medi term we expect, or like we have certain that the chain like that, that fines will no longer by default provide all the history. Basically, if we are certain about that in any version. Right. Like it doesn't matter like how exactly we ended up doing this, but like that, I think something like that is indeed would be important to you. but at the same time, I would want to say for context that right now, we only have a few roll-ups life on magnet. And those usually only settle very occasionally. I mean, I haven't looked specifically at the optimism, but like Zika St concerned that that's, I think last time I checked was at a couple of hours. And so there's a long way to go between the concentration and the situation where they set every single bed, like one or upset it's every single block. I mean, hopefully of course we get there because that, that means we have more adoption, but it won't be that like, we turn this on and we immediately have a kind of yearly growth of, of three terabytes. this, this would be like the long run situation. And even then, like, it would take a year to get to the three terabytes. So I think it's something that is, as you were saying, as big, as long as we kind of reasonably certain that by the end of next year, we have some version of history, limiting history in place, even by early mid 2023, this will be perfectly fine. the question is just like, are we busy? Because, because if, if I think a lot of people here would really want to see this change in an, in a special purpose fault before the merge. And for that, of course the timeline would have to be quite an accelerated on decision-making. and the question is like, if 4444 takes us a lot of time to kind of like discuss the details of focal fall on the way there, basically, how comfortable are we with already making a preliminary decision on like a special purpose Pope for this before we kind of fully worked out the details and 4444 before? I think that's really the, the main question, 

**Tim Beiko**
* Right. And I guess maybe to like, they have some context on the timeline, you know, that the default say path, if this was accepted, as we'd say like, oh, it goes into Shanghai and realistically, you know, Shanghai is like a year away, plus or minus a quarter. and you know, the, the pushback there would be, well, transaction fees are already super expensive. They're like, non-trivial on roll-ups. And like waiting another year to reduce them is, is just really bad. and so basically the, the options you have is then, like, there's something between the merge in Shanghai, that's just this. and then, you know, you also open up the Canberra of like all the other things we want to do after the merge. then obviously with the merge itself, that's a fork. and, and, and, you know, we're, we're already making two EIP's there. the trade off is you're obviously adding more complexity to this already massive upgrade. The other thing is, we discussed on the last call potentially having like, an empty fork before to merge, to just set the fork ID, for the merge. and so that's, a time where like, we might have to get everybody to upgrade their nodes anyway, and then the other option is like, you have just, you know, a completely separate fork would just this, and at the risk of potentially pushing back the timeline for the merge. I think that's the other thing it's obviously, obviously, you know, people are very excited about the merge. you don't want to push it back for, you know, for a bunch of reasons. so if, if we have a completely separate fork, you know, is that actually pushing things back or is that maybe the most efficient way to do it because then you're just separating concerns much more. I think that's kind of the timeline discussion, like, yeah, the, yeah, the way I see it is like either we have something completely separate either we bundled it with like some fork ID change or with the actual merger itself, or we basically wait until after the merge. And then the problem is just, you know, high fees on roll-ups, basically persist until then. 

**Danny**
* So the, the fork idea change wouldn't that wouldn't be to software releases. So like that would be, say the fork ID changes two or four weeks before the merge is supposed to happen. You upgrade your node before then, and you don't upgrade your node a second time later. So if you coupled this or anything with that, then you now have coupled them an extra plea and are there. So you don't do that really until the merger is ready to be released. And so I think that Type, if you do want to do an aggressive timeline for those tightly, coupling that in that way, actually it encbers things and makes things a bit harder rather than doing something independent. My 2 cents, 
  
**Peter Szilagyi**
* My 2 cents would be not to couple this thing with the merge, because the merge is messing up by itself. And you don't want one extra stuff to debug now as for whether to do it before or after. I guess if somebody just created a proof of concept to see what it would be, then it might be interesting to investigate whether we can wrap it in before the merge, without delaying the merge, if not doing it after the most early, only downside there is that, that will take, I don't know, half a year, at least, the outside will be however that after the merge, we will have a nice, nice, simple, so to say hard for, to desktop how we can fork stuff, post-merger world, which isn't a bad thing either. Is it, oh, sorry. And scar, go ahead. And Andrew after. 

**Ansgar Dietrichs**
* Alright. I just wanted to mention, so the quotes locally into a, just a full curiosity into like an implementation of hopefully a date and, physically implemented today and gets on tested yet. So it's kind of like, definitely only like a prototype, but that was pretty straightforward. So I don't, I don't think implementation complexity would be high. and just the other company that I would want to make. It's just that I think we have talked in the past repeatedly about that there's problem with the Allcoredevs governance structure and that like user voices, kind of underrepresented. And I think this is really kind of like by far the most kind of pure purified example, Alana instance of this thing, we basically, like, I think that the user side is very overwhelming for kind of trying to do something like this before the much, if there's any chance, but, and listening to it, it sounds like on this call, everyone was listed ambivalent. So I didn't get any strong opposition against this. So I would just kind of like argued that we should do this before the merge, because we are more or less in the ambivalent, but the community is like extreme, like very strongly. I don't want to overstate it, but like, it seems like the community is very strongly in favor of sometimes before the match. I even saw a lot of people saying like, yeah, it's a much, it's delayed by a couple of weeks. and I don't even think that's necessarily the case, but if, even if that was the case, that would be more than worth it. So I really think we should kind of like try, and even if no one is on the call here, like to represent these, that this kind of this broader set of people, but like, I, I think we should really keep in mind that that is an important, 

**Dankrad Feist**
* Yeah, maybe we should treat it and we should do it before Christmas. That's my opinion.

**Louis Guthmann**
* I agree. I agree with that. When do we present? I think it's, it's, we'd provide the change in booking narrative and cost for, for users to do the migration to, to roll up. So in general.

**Tim Beiko**
* Thanks for sharing, Andrew. 

**Andrew Ashikhmin**
* I think, eh, it's not a good idea to do it alone, like at the time with the merge, because yeah, I agree with Peter that the image is already complex enough. and if we decide to do it before the merge, my slight preference will be to go for the simpler 4492, because it's a kind of more trivial change than 4488. 

**Tim Beiko**
* Got it.

**Andrew Ashikhmin**
* And is this based on like Aragon's engineering capacity or just on like analyzing kind of the second order impacts of the change, I think is the second order impact, because like, it's not hard to add a next validation, but like them, there might be, implications for block proposers and so on. 

**Tim Beiko**
* So would it be valuable to say like in the next couple of weeks, get feedback from, I don't know, say flash bots or I dunno what team, like some team that has experience in like the mentor pool to see, you know, how easy or hard it is to have an optimal strategy, would that like help with these concerns? I know Aragon also has like a separate design for the transaction for, so I'm not sure if like, yeah, if it's helpful to say have an implementation and geth, or if that's just so different from what you all have. yeah, I guess I don't. Yeah. W what would be kind of the way for you to like, feel more comfortable about that? Does it just taking more time? Is it seeing your of concept? 

**Andrew Ashikhmin**
* Well, it's probably a relatively easy change so we can do it, but it's like, it will be some development work. It's not like changing a single constant. Right. So it will delay the merge more than just like changing a single constant. Right. 

**Louis Guthmann**
* I even want to point out that we could mix, you know, make for your 4490, like, you know, before, and then do a 4488. Like, there are no, I mean, they are, 4490 is just a simplified version and a 44 ADA goes just deeper. 

**Vub**
* Right. But then are we okay with, what's the possibility of five megabyte blocks? 

**Louis Guthmann**
* Yeah. I mean, that's a, that's a very good question. And, and I don't have a good answer for that. I don't expect those to actually happen because obviously there is a, there is a max size transaction by a geth, which is a hundred kilobytes, which mean that every time we're going to publish a transaction, that is at least 20,000, gas spends on the, on the, on the signature itself, like in those, the base cost. So we will never get to that nbers, but I didn't quantify the actual mass. 

**Vub**
* Right. But then if the argent is that we'll never actually get to what, then that's also an argent that what, for the issues with optimization wasn't block optimization. 

**Micah Zoltu**
* Right. The, I think the thing we need to remember is that if the, someone can like crash the network or break the network or whatever, by making a five megawatt block, we will see if I might go that block. I don't think the question is, are we likely to see what naturally it's will one break the network? And if so, we will see it. 

**Danny**
* And block production often bypasses the  mempool. So the mental is doesn't necessarily like the validations and the employer doesn't really in today's practice bound down to what is going to go in there. 

**Louis Guthmann**
* That's a, that's a very fair statement. I, yeah, I don't have a clear answer for that. It's also not someone said that, in the worst case, it's also good to 10 gigabyte on the worst case, in, in the worst case scenario, when yeah, because the third scene, meaning, 

**Tim Beiko**
* Well, isn't it like 30 million divided by six gas, the five megabyte block. Isn't that the worst case? 

**Louis Guthmann**
* Let me check. 

**Tim Beiko**
* Yeah. Cause I mean, 4466 geth per 

**Louis Guthmann**
* Right, right, right, right. You're right. Yeah. Yeah. I got confused. Sorry. Sorry about that. 

**Tim Beiko**
* Yeah. So the worst case is a five megabytes, not a 10 megabytes. and obviously that's worth noting that like, it's, it's easy to send one of these worst case blocks, but then if you're spamming the network with these five megabyte blocks, the cost goes up exponentially. So, so you, you know, you can't send like a hundred, five megabyte blocks in a row, the cost to do that would just like be millions of ether with the basically going up. 

**Louis Guthmann**
* Exactly. Yeah. But you can, no one can, no one will sustainable sustainably be able to push those blocks. 

**Tim Beiko**
* You can basically send Penn way to half an hour, send 10, wait a half an hour. That's like expensive, but not like completely out of reach strategy. Yeah. Or do 2.5 megabyte blocks forever. 

**Peter Szilagyi**
* So just to add, since we're talking about five minutes, by the time when I'm at a loss, I want to add that as has a message limit of 10 megabytes. So essentially I have a bite block would be impossible. probably possibly eight megabyte is low. So I, I'm not entirely sure what the payload caps are, but, I think that has a cap of megabytes or something. I don't have a video versus a cap on how much it's going forward. So that's one potential issue. And another financial issue that we, we should not forget is that the law of propagation is essentially every block is forward, but it's amassed work, but it's also forwarded to square without your peers. Now you've got by default problems with basic peers that have means square 50 box seven. So you will actually be propagated to seven years. And you kind of expect that the putting together from seven other peers that you have, so you're going to cross your network line 14 times five block by block. That's seven deep megabyte of data traffic just for tampon law propagate through that. That's a pretty happy bandwidth requirement, right? 

**Tim Beiko**
* One thing, sorry, Lucas, I'll get to you right after this. But one thing that's sort of highlighting also is, next call is the last call of the year. So next Allcoredev  calls will be December 10th. Then the next one would fall on December 24th. I don't think anyone here wants to have a call, on Christmas Eve. And even if some people did, we'd probably get quite low attendance. and if, obviously we're talking about potentially doing one of these changes before to merge, you know, we probably want to have consensus on it, if not, you know, by the next call, definitely by the absolute first call in January. and so I think it's just worth kind of highlighting that, like to see, I don't like the people think we should like think, basically plan out to think about prototype a potential for, for this in February. I don't think we need to agree to it today. and if so, basically what are the, what are the things that we want to figure out then the next two weeks, right. Like, and, and can we potentially come back with that then and make a decision or like get closer to a decision on the next call, just because yeah. If, if, if we are doing this before to merge it, we, we, we need to make the decision sooner than we otherwise would. 

**Micah Zoltu**
* Can we make the decision today on committing to 4444 or something along those lines? So that way we can start the outreach process sooner rather than later, is there anyone that disagrees that we should do 4444, or, 

**Louis Guthmann**
* There w there is some community disagreement over the changing security assption, folk music brought up. So I don't know if the community, we do not fight those already seen someone on Twitter being extremely active against 4444. 

**Ansgar Dietrichs**
* Maybe because you might be the best to ask. It isn't because we expect roll-ups to, to move to, sharding data availability in the next two or three years. Anyway, I pointed out has already the same security. kind of like providing like data availability of the data, but not, not the history. So, so it isn't basically isn't that the same situation that we have to end up wrong come anyway. 

**Dannny**
* Yes. 

**Dankrad Feist**
* And I think it's a misunderstanding that people, people confuse data storage and data availability. These are different properties. And, I, I don't, I dunno like, Louis, did you get this from any, from any actually, like roll-up people I know there was someone on Twitter who did that, but I think they didn't understand. 

**Louis Guthmann**
* So, so from the perspective as the there is the solution to, 4444, which is to have like enough chain, queue of, of latest, like when floods were touched or modified. So that wouldn't be too, I mean, there is a way around, for security to manage that I'm not familiar how of this equipment can sustain this general assption. So I, I, I can talk on behalf of optimism with from here. 

**Tim Beiko**
* Oh, Andrew. 

**Andrew Ashikhmin**
* Yeah, so we discussed, 4444 inside the team and, we are not opposed to it. So Aragon is in favor of it. 

**Tim Beiko**
* Thanks. 

**Danny**
* Right. And I mean, the assumption is that 4444 coupled with a historic block distribution standards that are outside of the PDP network, and that the blocks are available by any of these standards, you can always recursively validate all the way to the base of the chain, via knowing, recent information to secure information about the head. And so the expectation and data availability is that data's made available. and then those that want to have it and can use it. And there's not a security risks around state of holding texts. and then once it's made available and infrastructure and communities are utilizing it, then it's ultimately their problem. The story in the long run. 

**Dankrad Feist**
* Yes. Agreed. Basically we should be careful because data storage is not on the attack vector. You can't make someone forget data. You can only withhold data in the first place. That's an attack factor. 

**George Kadianakis**
* So when it comes to our labs, we don't have optimistic roll-ups people care, but since Starkweather here, how does it start? Where would, why would four fours impact this Ichiro roll-up? Where would the roll-up use? 

**Louis Guthmann**
* that's a very good question for Zika. What up? I think there is a solution, which is, are, they said keeping queue of the, of the, like, data being stored on like, when he was modifying, published and republished it, before the grace, like before the destruction of the data to, to guarantee the WWT over time. what I'm saying is of course we require engineering work and, it's something that would be quite a, like an extensive medication of, of the, what we called Corvus of stark nets. once we can manage it, we can probably work around it. But the, what I'm saying,, I don't, I can't talk on their behalf, so the, they should come or so, or, which to reach out, 

**Dankrad Feist**
* To jumpp in there. I don't like, I understand what you're doing, but I think you are, you're operating from an extremely pessimistic security model. And I think what, what you do there is not necessarily in smarter ways to do The same. You basically want to use the Etherum data availability layer as your storage layer, which is what your solution does. 

**Louis Guthmann**
* That's what I mean, that's, that's, I'm just saying if we want, I I'm just reflecting. I mean, something we've been discussing publicly, internally, whatever, I'm just some shit on rerunning the network and to being able to reconstruct the storage on there, 4444, I think the carer can make it, I don't know, for optimistic. Maybe we should change 

**Dankrad Feist**
* The reason I'm correcting you here is because I think they're spreading fat. I don't think like you are having a super pessimistic security assption that you say everything has to be reconstructible from the current data availability layer. And I don't think that 

**Tim Beiko**
* Yeah, just cause we have only like five minutes left, obviously 4444 is going to need a lot of community outreach. I suspect whatever version goes live. It's probably not exactly what's the Eth today. but something like it, this probably like has to happen at some point. yeah. And, and we can't, I don't know, like we, we can make some commitments towards like pushing this and what not. I think we probably can't do that in the next two or three minutes. what I think we can do is try to highlight like, you know, what the different teams want to see to be comfortable with 4488 for in the next two weeks. and so obviously trying to have implementations across all clients is one thing. And then Andrew's concerns about like, and others have raised this as well, but just around, like how you do optimal kind of block packing. I'm not sure if that's something we can get done in two weeks, but it might be, it might be something that even say we have, you know, the client implementations ready. we still need to figure that out, but we, we, we don't necessarily have to block everything on it. And I don't know how, like, would most client teams have the bandwidth to prototype this in the next two weeks? if not, I'm happy to reach out and try to find teams or contractors that can, that can work on prototypes. yeah. How, I guess I appreciate how realistic is it for like five teams to actually spend some of their cycles on that. Then the next on 4488 to be clear in the next two weeks, 

**Lukasz Rozmej**
* Nethermind can try to prototype it in this two weeks. 

**Louis Guthmann**
* I just want to correct one thing before I drop, before we dropped, I'd I get done don't cry. I, I, I'm not trying to fun them. Just, you know, that's like, I was just expressing like you're in security Monday night. Maybe there's a particular can be changing. I agree with that. I was about it. I was just saying that, we shoot 

**Dankrad Feist**
* Cole. We should take that call to explain to you why I think it should be different. 

**Danny**
* That'd be too critical that that is becomes the model. If you plan on data Sharding, because that data Sharding not going to provide persistent data storage guarantees for all. 

**Marius Van Dar Wijden**
* So, Tim, one thing that I would really like to see is what's the, like, what's the worst block? What's the, what's the worst? Like with the current packing algorithm, if we change it to, to, to, to this new one, like, what's the difference between, like a, like how, how different can this, this block be from like a really, like smartly packed block. and if like, if someone could work on that, that would be really, really nice. 

**Tim Beiko**
* The worst, you mean the most damaging from D for to network? Basically? 

**Marius Van Dar Wijden**
* No, I mean, I mean, like, like given a set of transaction, and, like a smart algorithm to pack them, how, like how much overhead can, can there be to like the, the naively packed, version of that, 

**Ansgar Dietrichs**
* When you say that you mean kind of like lost profit for minus that kind of like just leave transaction, but I think it does make sense to kind of analyze like an ad official worst case because, you know, it's this construct a case, whereas the transactions are pending in just the right way that you kind of find clues lose out on a lot of profit. But like, I mean, that's not an attack factor kind of like taunting someone who's potential profit and then giving it to them that that's not an attack. so, so basically what you'd have to look, this is just like, historically like historical just real world blocks and say, okay, if we had this naive algorithm basically, and we just assed they would have been one extra big transaction in the front that used up a lot of the cubicle that cut kind of like, how much would you have left on the table, but then that might be an interesting analysis. 

**Tim Beiko**
* Is that something you have the bandwidth to look at the Ansgar, cause you seem to understand the problem pretty well. And, and given the short timeline. 

**Ansgar Dietrichs**
* Yeah, Yeah. I could do that. Someone else also wants to look into this something if we do to reach out coordinate 

**Tim Beiko**
* And, yeah. So basically, so there is a PR against Geth. Nethermind can prototype Aragon can probably pull in the consensus changes, but not the transaction for changes. and w it would take some extra bandwidth to do that, Besu, I get, okay. So there's a comment by Besu you. Is this something you think you could prototype in the next two weeks, or is this something where if somebody submitted a PR to Besu, you would make your life much easier? 

**Justin Florentine**
* Yeah, we're always open to PRs. you know, two weeks for a prototype would be Type for us, but, I'd have to talk to the rest of the team. 

**Tim Beiko**
* Okay. So I guess let's see what we can do in the next two weeks, if you are listening to this call and like, you've got a Java or GO background and you can help with PR, please reach out to me. yeah, we can definitely kind of find or set up some, some bounties and whatnot for that. and yeah, I guess in two weeks we can get back to you and discuss and see kind of what the progress made. You know, how, how realistic is it to put this, potentially before the merge? 

**Danny**
* I want to say, I think that  can also commit to, providing resourcing for pushing 4444 a long, throughout 2022. 

**Tim Beiko**
* Cool. We are one minute away from time, but there's someone on the call who had a quick shout out. so Zach is here, he's working on a documentary about Ethereum, called infinite garden. So, he'll probably be trying to reach out to a bunch of people on this call and, and others in the community over the next few months it's already started. so yeah, I just wanted to give him a few minutes to kind of explain, what they're working on and yeah. 

**Zack Ingrasci**
* Thanks, Tim. yeah, just don't want to take too much time, but I wanted to jump on. And obviously we are huge fans of the work of the core devs and, we're making this film called Ethereum the infinite garden, which was actually funded by the community via a mirror, a crowdfund on mirror. And, it's a lot of  kind of focus on how Ethereum is already affecting people's lives around the world. We've been filming all around the world, and how Ethereum will affect people's lives in the future. So we're filming through the merge, and obviously the work of the core devs is fundamental to the story of this film. So, I just wanted to jump on and, you know, if, we pop into your telegrams, we wanted you to know who it was. So, you know, we'll be talking to a lot of you moving forward and yeah, really, I just appreciate the time and all the work you're doing. 

**Tim Beiko**
* Thank you. where's the best place for people to reach out if, you know, they want to pin you, they have something interesting to share. 

**Zack Ingrasci**
* Yeah, absolutely. my email is zack@optimist.co And, you can check out all our work, our previous films that are on Netflix and HBO on Zack, on optimist.co. so you can check out the website and our contact info is on there as well. but yeah, probably email's the best. 

**Tim Beiko**
* Awesome. Thanks. yeah. And one last quick thing before we go, at Trent is organizing emerge community call next week at, Allcoredev  time. So 1400 UTC, which, is now a new time in, I guess you're up in north America because of daylight savings. so, yeah, if you are, basically infrastructure provider tooling provider application that wants to like, see what, the merge what's happening with the merge, ask your questions, get the updates. please come next Friday. If there's a link in the chat here, it's on the Ethere PM repo, for the agenda. And, yes. Final shout out, please update your notes. if you are running a note on the proof of work network right now, Arrow Glacier will have happened before to next Allcore devs. Yeah. Happy Thanksgiving for Americans. and yeah, thanks for anyone in the U S who made it on this call much appreciate you spending your holiday weekend. Share with us. Yeah, I think that's it. thanks a lot, everyone. This was, this was really, really good. Thanks Tim. 

## Chat Highlights:
- 08:55:44 From lightclient to Everyone:
	gm mr trent
- 08:55:55 From Trenton Van Epps to Everyone:
	GM LC
- 08:56:14 From Trenton Van Epps to Everyone:
	light client
	layer consensus
- 08:58:28 From Tim Beiko to Everyone:
	https://youtu.be/js4HLK4MyQI
- 09:01:25 From Trenton Van Epps to Everyone:
	vitalik what does the u stand for in vub
- 09:01:35 From lightclient to Everyone:
	u don't wanna know
- 09:01:42 From danny to Everyone:
	unstoppable
- 09:01:53 From lightclient to Everyone:
	gm danny
- 09:02:00 From lightclient to Everyone:
	gr also
- 09:02:04 From danny to Everyone:
	gr
- 09:02:05 From Trenton Van Epps to Everyone:
	vitalik "unstoppable" buterin
- 09:03:36 From Marius Van Der Wijden (M) to Everyone:
	upsetting_miners
- 09:07:50 From parithosh to Everyone:
	Nethermind, Geth + nimbus, lighthouse, lodestar, Prysm are working. Teku should work, but I haven’t deployed it yet.
- 09:10:53 From Mikhail Kalinin to Everyone:
	https://github.com/ethereum/EIPs/pull/4476
- 09:11:31 From parithosh to Everyone:
	Faucet: https://faucet.merge-devnet-1.wenmerge.dev/
- 09:11:31 From danny to Everyone:
	audio fixed
- 09:12:01 From parithosh to Everyone:
	explorer: https://explorer.merge-devnet-1.wenmerge.dev/
- 09:12:11 From parithosh to Everyone:
	beaconchain: https://beaconchain.merge-devnet-1.wenmerge.dev/
- 09:13:04 From Tim Beiko to Everyone:
	https://github.com/ethereum/execution-apis/pull/133/files#r756365294
- 09:13:09 From Mikhail Kalinin to Everyone:
	https://github.com/ethereum/execution-apis/pull/133/files#r756365294
- 09:17:09 From Mikhail Kalinin to Everyone:
	https://github.com/ethereum/execution-apis/issues/137
- 09:22:29 From Marius Van Der Wijden (M) to Everyone:
	do you have a changelog for the specs?
- 09:22:42 From Tim Beiko to Everyone:
	Good idea!
- 09:23:42 From Marius Van Der Wijden (M) to Everyone:
	great! makes implementing way ea3
- 09:24:03 From Marius Van Der Wijden (M) to Everyone:
	*easier
- 09:25:03 From danny to Everyone:
	quick heads up. I’m having a kid sometime in the next few days… will generally be off most of december and joining back in at the start of January.
- 09:26:06 From Gary Schulte to Everyone:
	Good luck Danny 👶
- 09:26:15 From Micah Zoltu to Everyone:
	We should start a collection plate to buy Péter a good mic, microphone arm, and some sound absorbing panels for the bathroom that he calls into these meetings from.  😬
- 09:26:32 From Gary Schulte to Everyone:
	😆
- 09:26:43 From Trenton Van Epps to Everyone:
	maybe he doesn't know the audio is not good hha
- 09:27:08 From Tim Beiko to Everyone:
	https://github.com/ethereum/EIPs/pull/4488
- 09:29:07 From Ansgar Dietrichs to Everyone:
	important to note: the 300 byte per-tx stipend makes the 2d optimization aspect only relevant for txs with exceptionally large calldata
- 09:30:39 From Justin Florentine to Everyone:
	Congrats Danny, #dadlife
- 09:35:50 From Ansgar Dietrichs to Everyone:
	also, the motivation for this is to facilitate rollups in the short term. sharding is still 2 years away.
- 09:36:45 From Micah Zoltu to Everyone:
	2-10 years away!  The public listens to this call Tim.  😬
- 09:36:50 From Tim Beiko to Everyone:
	I didn’t say that?
- 09:37:06 From Micah Zoltu to Everyone:
	"You quoted Ansgar that Data Sharding is 2 years away.  😅
- 09:37:07 From Barnabé to Everyone:
	Seems very unlikely that even after repricing, execution layer call data fees would be much cheaper than data sharding
- 09:37:18 From Tim Beiko to Everyone:
	Ahhhh, you meant it’s too optimistic
- 09:37:19 From Tim Beiko to Everyone:
	Sure!
- 09:37:24 From Tim Beiko to Everyone:
	But I think it will be less than 10 :-)
- 09:37:42 From Micah Zoltu to Everyone:
	Sure, but we shouldn't give dates to the public this far out.  You know, my usual argument.  😛
- 09:37:54 From Dankrad Feist to Everyone:
	I'm think it will be less than 2!
- 09:38:03 From Dankrad Feist to Everyone:
	it really isn't that difficult
- 09:38:10 From Tim Beiko to Everyone:
	Need a prediction market set up after this call...!
- 09:38:32 From danny to Everyone:
	I think you  can get a number of shards with committee security released in not too long.
- 09:38:36 From danny to Everyone:
	CL-only upgrade
- 09:38:57 From Dankrad Feist to Everyone:
	with every core dev being sponsored into a 1 yr position @ prediction market
- 09:39:08 From Marius Van Der Wijden (M) to Everyone:
	I'm willing to bet .1 Eth that we need more than 2 years
- 09:40:12 From danny to Everyone:
	4 shards, 4 subnets. don’t think we need 2 years
- 09:40:27 From Tim Beiko to Everyone:
	Guess we have a market!
- 09:40:38 From danny to Everyone:
	but this damn merge thing provides an unknown in the estimated timeline.
- 09:42:36 From Tim Beiko to Everyone:
	Lukasz, please go after this :-)
- 09:45:31 From Marius Van Der Wijden (M) to Everyone:
	how much heavier is verification after 4488?
- 09:45:41 From Micah Zoltu to Everyone:
	One assertion.
- 09:45:52 From Micah Zoltu to Everyone:
	Block production is harder, verification is epsilon harder.
- 09:48:03 From Ansgar Dietrichs to Everyone:
	agree with Dankrad’s sentiment, but this year seems unrealistic. but would strongly be in favour of having a special fork for this early next year
- 09:49:22 From Marius Van Der Wijden (M) to Everyone:
	but if that's possible, why do the limit on the block and not on the transaction indivdually?
- 09:50:55 From Marius Van Der Wijden (M) to Everyone:
	*if it's possible to split the updates into multiple transactions
- 09:51:38 From Marius Van Der Wijden (M) to Everyone:
	Hmm math doesn't check out...
- 09:52:05 From Marius Van Der Wijden (M) to Everyone:
	1mb /1000 = 1kb max calldata per tx is probably a bit low
- 09:52:50 From Micah Zoltu to Everyone:
	Just throw Trent at it.  They can make dapps change.  It is their superpower.
- 09:53:13 From danny to Everyone:
	https://ethereum-magicians.org/t/eip-2028-transaction-data-gas-cost-reduction/3280/35
- 09:53:14 From danny to Everyone:
	big red dot
- 09:53:26 From Trenton Van Epps to Everyone:
	😅
- 09:58:11 From lightclient to Everyone:
	unrelated - is the purpose of the EIP-3529 refund cap to cap the max size the block can be? e.g. was reduced from 50% to 20%
- 09:58:25 From Ansgar Dietrichs to Everyone:
	we did do an example implementation of 4488 in geth btw: https://github.com/quilt/go-ethereum/commits/calldata-eip
- 09:58:45 From Ansgar Dietrichs to Everyone:
	was pretty simple, I assume complexity in other clients is also small
- 09:58:48 From lightclient to Everyone:
	"we" - all ansgar
- 10:00:13 From lightclient to Everyone:
	half four half eight
- 10:00:29 From danny to Everyone:
	two four, two 8
- 10:00:34 From lightclient to Everyone:
	double double
- 10:00:36 From danny to Everyone:
	2428
- 10:00:47 From lightclient to Everyone:
	two4two8
- 10:00:54 From danny to Everyone:
	2lat
- 10:00:56 From danny to Everyone:
	2late
-10:01:04 From lightclient to Everyone:
	2late2furious
- 10:01:04 From Micah Zoltu to Everyone:
	Besu will be constructing blocks as of The Merge won't they?
- 10:01:15 From Micah Zoltu to Everyone:
	@Gary
- 10:01:16 From Justin Florentine to Everyone:
	yes
- 10:01:17 From Marius Van Der Wijden (M) to Everyone:
	22 times 102
- 10:01:26 From Marius Van Der Wijden (M) to Everyone:
	hahahah
- 10:01:29 From lightclient to Everyone:
	LOL
- 10:01:31 From Marius Van Der Wijden (M) to Everyone:
	44 times 102
- 10:03:59 From Marius Van Der Wijden (M) to Everyone:
	i think we could schedule something in February
- 10:04:38 From danny to Everyone:
	I think you can as well. parallelize it with 1 resource per team
- 10:04:59 From danny to Everyone:
	0.5 resource per team
- 10:06:23 From Ansgar Dietrichs to Everyone:
	agree with sentiment against coupling
- 10:06:43 From Louis Guthmann to Everyone:
	Was EIP4488/4490 been discussed yet?
- 10:06:52 From Louis Guthmann to Everyone:
	I messed up the timezone
- 10:07:01 From Trenton Van Epps to Everyone:
	yes
- 10:07:02 From Micah Zoltu to Everyone:
	Talking about them now.
- 10:07:02 From Tim Beiko to Everyone:
	Yes! People seem OK with the general complexity of 4488
- 10:07:26 From Louis Guthmann to Everyone:
	Cool. So I can abandon 4490, right?
- 10:07:32 From Louis Guthmann to Everyone:
	When will it be added?
- 10:07:36 From Louis Guthmann to Everyone:
	Was it discussed?
- 10:07:37 From danny to Everyone:
	link to 4488 geth branch?
- 10:07:38 From Micah Zoltu to Everyone:
	That is what is being discussed now.
- 10:07:41 From Louis Guthmann to Everyone:
	Got it
- 10:07:44 From Louis Guthmann to Everyone:
	Thanks
- 10:08:07 From lightclient to Everyone:
	@danny  https://github.com/quilt/go-ethereum/commits/calldata-eip
- 10:08:11 From Tim Beiko to Everyone:
	I think we’re leaning towards dropping 4490 in favour of 4488, timelines are being figured out!
- 10:08:15 From danny to Everyone:
	users talking about 4488 https://www.reddit.com/r/ethfinance/comments/r0yy6c/why_calldata_gas_cost_reduction_is_crucial_for/
- 10:09:18 From Pooja Ranjan to Everyone:
	People have questions on timeline on YouTube Chat
- 10:09:20 From Trenton Van Epps to Everyone:
	Ansgar we are users as well
- 10:09:21 From Trenton Van Epps to Everyone:
	lol
- 10:10:20 From Gary Schulte to Everyone:
	I think this is more of a signaling about commitment to rollups and to show ethereum can be agile and responsive.  Most of the gas complaints are about L1 and this isn’t going to change any of that
- 10:10:53 From Micah Zoltu to Everyone:
	I have seen people complain about L2 prices being too high too.
- 10:12:31 From lightclient to Everyone:
	if 5mb block can harm the network it's very possible someone does it
- 10:14:25 From Micah Zoltu to Everyone:
	s/very possible/essentially guaranteed/
- 10:14:55 From Micah Zoltu to Everyone:
	Or do 2.5MB blocks indefinitely.
- 10:15:18 From Justin Florentine to Everyone:
	P2p allows 10mb
- 10:15:30 From Justin Florentine to Everyone:
	D’oh, what Peter is saying
- 10:15:37 From danny to Everyone:
	I think 4488 is worth the additional complexity
- 10:16:55 From Micah Zoltu to Everyone:
	5MB block, 35MB down + 35MB up, ~2.7 MB/sec
- 10:17:08 From Micah Zoltu to Everyone:
	Half that for sustained attack.
- 10:17:10 From Marius Van Der Wijden (M) to Everyone:
	@danny agree
- 10:17:17 From Mikhail Kalinin to Everyone:
	post-Merge 5mb blocks might be less of a concern as the proposal mechanics will be different. as long as 5mb block may be propagated and executed in time (before attestation threshold) it should be fine, also, a block full of calldata should have less execution time than a block that is full of regular txes. bandwidths and trhougtput are still the concerns, chain history as well
- 10:17:26 From Ansgar Dietrichs to Everyone:
	I think best path would be to explore 4488 further over the next two weeks, clients assessing complexity, and then make a final call next acd on a Feb fork
- 10:17:35 From Mikhail Kalinin to Everyone:
	less of the concern from block production PoV*
- 10:18:18 From Marius Van Der Wijden (M) to Everyone:
	if we have a prototype in every client in 2 weeks, I would be happy to schedule it
- 10:18:33 From Trenton Van Epps to Everyone:
	still feels early to make a decision on 4444
- 10:19:17 From Marius Van Der Wijden (M) to Everyone:
	Rollup companies should put their engineers on doing these prototypes imo
- 10:19:20 From Micah Zoltu to Everyone:
	It will always feel early to make it, but we are hurting ourselves by continuing to *not* make it.
- 10:19:35 From Trenton Van Epps to Everyone:
	it was proposed relatively recently
- 10:19:50 From Micah Zoltu to Everyone:
	The *idea* of regenisis has been around for a long time and we keep punting on it.
- 10:19:57 From Micah Zoltu to Everyone:
	This is the latest instantiation of that general concept.
- 10:20:10 From Ansgar Dietrichs to Everyone:
	I was always under the assumption that rollups would be their own “chains”, with their own clients that store rollup history locally with rollup users
- 10:20:13 From Tim Beiko to Everyone:
	There is already a PR against Geth, so we’d need an implementation across Besu (Java), Erigon (Go) and Nethermind (.NET)
- 10:20:34 From Tim Beiko to Everyone:
	I can reach out to rollup teams if these client teams don’t have the bandwidth in the next 2 weeks.
- 10:20:59 From Louis Guthmann to Everyone:
	StarkWare won’t have any bandwidth outside of me. So no engineer on our end
- 10:21:23 From Mikhail Kalinin to Everyone:
	An year of 1MB blocks is already about 2.5Tb of disk space, probably 4444 should be more restrictive on the number of the history blocks that are guaranteed to be stored
- 10:21:38 From Micah Zoltu to Everyone:
	I like that statement @Dankrad.
- 10:23:27 From Ansgar Dietrichs to Everyone:
	I don’t understand how the DA layer needs to provide more than the beacon chain does under the merge for the execution chain: provide canonical ordering, and DA, but use your own clients for history storage. execution clients don’t ask their consensus clients for history, they keep it on their own
- 10:24:16 From Ansgar Dietrichs to Everyone:
	the tl;dr here really just seems to be: you can’t be lazy and use the base layer for permanent history storage. this is not a security concern, just a lazyness concern
- 10:24:48 From Louis Guthmann to Everyone:
	I do not oppose this. I’m simply exposing the current security model of Rollups
- 10:25:08 From Louis Guthmann to Everyone:
	Not trying to FUD anything 🙂
- 10:25:09 From Micah Zoltu to Everyone:
	It isn't just rollups, there are dapps with the same model.
- 10:25:24 From Ansgar Dietrichs to Everyone:
	right, also lazy & wrong
- 10:25:42 From Tim Beiko to Everyone:
	Andrew, can Erigon pull in a geth implementation or not really?
- 10:25:46 From Ansgar Dietrichs to Everyone:
	and for rollups, if we have a forcing function for rectifying this sooner, they will be in a better shape to make use of sharding as soon as that comes online
- 10:26:16 From Andrew Ashikhmin to Everyone:
	Erigon has its own tin pool, so we can’t take gets implementation verbatium
- 10:26:29 From Tim Beiko to Everyone:
	Got it, so you could take the consensus changes but not everything else?
- 10:27:19 From danny to Everyone:
	I believe you can parallelize 4488 with the merge and release in February while  at the same time the merge resources and processes barely even notice it happened
- 10:28:21 From Justin Florentine to Everyone:
	Similar story for Besu. Would require txpool refactor if we need to implement the stipend. Gas cost change is trivial
- 10:28:46 From danny to Everyone:
	<3 PRs lol
- 10:30:01 From Ansgar Dietrichs to Everyone:
	geth 4488 prototype PR: https://github.com/ethereum/go-ethereum/pull/23983
- 10:31:03 From Trenton Van Epps to Everyone:
	there is also a Merge Community Call next week at this same time
	https://github.com/ethereum/pm/issues/419
- 10:31:11 From Trenton Van Epps to Everyone:
	1400 UTC, 9 ET
- 10:31:22 From Tim Beiko to Everyone:
	Optimist, not Optimism!
- 10:31:54 From Ansgar Dietrichs to Everyone:
	as always, come join us in the discord lounge after this call!
- 10:32:04 From danny to Everyone:
	lounge will be fire today
- 10:32:10 From Marius Van Der Wijden (M) to Everyone:
	update your nodes!!!
- 10:32:31 From lightclient to Everyone:
	happy thanksgiving americans!
  
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

## Next meeting on: December 10, 2021, 14:00 UTC
[Agenda](https://github.com/ethereum/pm/issues/428)
