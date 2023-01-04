# All Core Devs Meeting 129

**Meeting Date/Time: January 7, 2022, 14:00 UTC**

**Meeting Duration: 1 hour 35 min**

**[Github Agenda](https://github.com/ethereum/pm/issues/436)**

**[Video of the meeting](https://youtu.be/wCSNMSyJV7Y)**

**Moderator: Tim Beiko**

**Notes: Yalamanchi**

## Decisions Made / Action items

| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
|129.1 | Danny to work on minor spec update | [19:41](https://youtu.be/wCSNMSyJV7Y?t=1181)|
|129.2 | Pari will work on Shadow fork Goreli testnet| [19:54](https://youtu.be/wCSNMSyJV7Y?t=1194)|
|129.3 | No decision on the inclusion of EIP-1153 in Shanghai. Proposer is advised to look into pros and cons and continue [discussion on Fellowship of Ethereum Magicians](https://ethereum-magicians.org/t/eip-transient-storage-opcodes/553). | [45:40](https://youtu.be/wCSNMSyJV7Y?t=2740)|
|129.4 | Shanghai Planning to be continued in the next meeting [Shanghai Planning](https://github.com/ethereum/pm/issues/450) | [1:20:30](https://youtu.be/wCSNMSyJV7Y?t=4830)|

# Meeting begins

**Tim Beiko**: And we are live. Hi everyone. Welcome to All Core Devs #129. First one of the New Year. Posting the agenda in the chat here. Umm. Basically 3 things to cover today. First updates about the merge and... kintsugi. There's the issue that we found and Marius recently wrote about. Then Moody is here to talk about eip-1153. And then the last thing is, now that, you know, we're starting to see the final stages of the Merge. There is a bunch of things in the backlog for Shanghai and is probably worth starting to have some conversations about how we want to think about that. But what we want to prioritise and what not. I guess to start on the Merge stuff maybe makes sense, I don't know, Marius 'cause you have the tweaks today. Do you want give us kind of a quick recap of, you know, what you saw over the holidays and then the issue that came up today.

# Kintsugi

**Marius Van Der Wijden(M)**: Sure. Can you guys hear me on this mic? Yeah. Probably. So, over the holidays, Kintsugi went pretty well. No major issues. I created a Bad Block generator. So it generates Bad Blocks with like different stratergies. And one of the stratergy is to replace fields in the block with other fields. And today, maybe, yesterday. This actually hit a bug. So, what the fuzzer did was replace the Block hash field in the execute payload parameters with the parent hash and so implementation should get all the fields from the execute payload parameter, construct the block, verify hash of this block is equal to the block hash that is passed in with the execute payload. Umm... Problem here was that because the past block hash was a valid block hash from the previous payload. Umm... some clients had some caching in place. Particularly, nethermind had some caching in the place. Just looked up the Block hash and returned valid, even though the block itself was not valid regarding this rule. So there was a big problem that created a fork between geth and nethermind, besu. So netheremind, besu both had this issue, that they didn't correctly check that. It's fixed in Netheremind, already. Then there was also a fork between lighthouse and teku on the geth side. So, the geth chain went for a bit and it split. And I think.. we currently think that the issue is similar that there's some kind of caching, in teku, going on. Wasn't working properly if you provide the block hash of a valid block with another payload. So, it's really nice the fuzzer actually found this. But, it means that right now, Kintsugi is not finalising. But we hope to update the node soon to have it finalise again.

**Tim Beiko**: When did it last finalise?

**Marius Van Der Wijden(M)**: Umm...

**Danny**: 129 epochs ago.

**Marius Van Der Wijden(M)**: 129 epochs ago.

**Danny**: 1307 hours

**Tim Beiko**: Is there case where like I guess we can't fix Kintsugi. I assume as soon as we have a fix on besu and netheremind deployed as well as the lighthouse teku one then we will finalize again and we can keep using the network.

**Danny**: It's proabably worth going through the exercise atleast to some amount of our effort to get it to finalise. Because...

**Vub**: Right. This is gonna happen on mainnet eventually. So like we are not gonna give up mainnet.

**Time Beiko**: Hopefully not.

**Vub**: Right. Well. Ok. We need to be prepared for the chance when it will happen on mainnet.

**Tim Beiko**: Right. Great work on the fuzzer, Marius. Very cool that we got this on devnet.

**Marius Van Der Wijden(M)**: Thanks.

**Tim Beiko**: Pari. I think I saw you come off mute. Do you wanna add something? .... If you are speaking, we can't hear you.

**Parithosh**: Sorry. Do you hear me now?

**Tim Beiko**: Yeah. We do.

**Parithosh**: Just for argument's sake. The nethermind and besu fix won't give us enough participation such that we finalize. We need the Teku fix in because teku accounts for about 36%. So as along as teku is fixed, then we reach finality. Yeah.

**Tim Beiko**: And that's ok. I mean even seeing the other 2 join back and seeing that as 60%, you know, for the next day is a reasonable state for the network to be in for us to serve.

**Parithosh**: Definitely, and we still need to figure out why Teku forked off again, because right now we see 3 forks. Most of the analysis so far has been done for the first fork.

**Tim Beiko**: Thanks for sharing. Uhm, aside from basically this issue, was there anything else that anyone wanted to discuss about Kintsugi?

**Danny**: Uh, I just want to say there are probably one to 4 test cases that should come out of this. Just they must.

**Tim Beiko**: So I'm... Yeah, go ahead Danny.

**Danny**: Then, so yeah, I spoke with Mikhail couple days ago I was off during most of December, so I'm playing a bit of catch Up this week, but the feeling was that very few things coming in the pipeline on the execution API. I think there's a refinement on what returning syncing means in the execute in the fork choice, and I think there's maybe like a one naming change on a couple of things like that. So the the goal is to get this done very quickly and get get an update out. Um.., and likely to once that comes out on the order of 3-4 weeks, do a testnet reboot for public testnet. Get things in order. Then from there, decide you know what is the timeline on forking and stuff. So there is a minor spec update in the pipeline and so I would say we continue to play with Kintsugi and you break Kintsugi and you resolve Kintsugi up until that comes out. I think simultaneously Pari and others are looking to Shadow Fork Goreli and to be able to do that in an automated basis. The nice thing there is that we can on a more continuous effort, actually test the transition. Um.. so kind of 2 efforts their on like testnet would be, the path... continual path on public testnets and then a path to kind of continuously test the transition process, which obviously could give us issues and hasn't done.

**Tim Beiko**: That makes sense, and I think the only like 2 other bits that that are probably like kind of outstanding there's all this stuff around, optimistic sync, but that seems in progress. The other one...

**Danny**: Right and I did it catch up with Mikhail and Paul about that one and there's a spec For optimistic sync, it has been blended or is being implemented by clients and is generally agreed upon as... some of the the corner cases that they were concerned about our result here. But there's plenty of testing to do on that so.

**Tim Beiko**: And then the last bit is the auth between the consensus and execution layer. So that's something we talked about a couple times, but I don't think have settled on a spec or a standard for.

**Danny**: Right?
And I think Mikhail and our conversation was hoping that Martin Swende he had said he might jump in on that. Uh Martin here so I think maybe you Mikhail and I should think on that in the next... early next week so that we can get that into this final update.

**Tim Beiko**: Yeah, and Marty, I'm...

**Martin Holst Swende**: Sorry yeah I have been dragging my feet but yeah we should have a discussion about it.

**Tim Beiko**: Does it make sense to have?

**Danny**: OK, I'll ping you early this week.

**Tim Beiko**: And I think that's the last kind of feature or big thing, aside from all the testing that was still missing and if we're targeting another kind of long lived testnet, we probably want to have this in so that we can test it as part of that.

**Danny**: Yeah, that was on Mikhail list I had just written about it.

**Tim Beiko**: Anything else about Kintsugi or The Merge that people feel we should we should discuss?

**Danny**: That's all on my plate till the, you know 2 weeks from now I think will be the spec will have been released by the next one and we'll give us, you know, the new discussion on what the next step that looks like.

**Tim Beiko**: Yeah, and we. Uh, yeah. We also have the the consensus layer call next Thursday so we can use the first bit of that to also cover anything that comes up.
Cool! Um.. yeah thanks everyone. Uh, it really feels like we're kind of getting there and there's more and more just more and more finalizations.

**Danny**: Yeah, awesome work on... from everyone on Kintsugi before the holidays... is really awesome to do that.

# EIP Discussion

- ## [Proposal to include EIP-1153 in Shanghai](https://github.com/ethereum/pm/issues/438)

**Tim Beiko**: Cool and yeah. Ok, so we have Moody here. Uh, who has been working on eip-1153 and he wanted to take a couple minutes to chat about it and why it can help. Lots of applications. Uniswap included on mainnet. Uhm, yeah, so Moody you want to take a few minutes kind of walk us through the context behind. Yeah. Share thoughts.

**Moody**: Yeah, sounds good. Thank you. Hi everyone, I'm Moody. I'm a smart contract developer at Uniswap and yeah, this might be a little bit early to be discussing this eip, but the context is that I'm experimenting with some improvements to our smart contract design and just give the full context. The idea is that we want to put all the pools in a single contract and allow you to flash... do any action across all the pools. And so basically, you'll be able to like mint, swap, burn without paying anything but the diffs at the end of the transaction. And so you're also not transferring any token, so it's a lot more efficient in terms of like how many slots it touches. And and so there's 2 ways to do this, as far as I can tell. Well, one way like create some sort of like VM within the EVM where you pass some bytecode to the Singleton contract, and then it executes through just time, it's like a custom set of operations that you can give to the Singleton contract. And store the diffs... the balance diffs in memory. But this isn't very flexible. It's not very elegant. The other way, which I think is more elegant, is that you call into the Singleton contract and you acquire a lock and then you can do whatever you want and the contract just keeps track of what the diffs are. And at the end of the lock you just have to have net zero deltas. In any tokens, you owe. So this just feels a lot like easier to work with as an integrator or developer. And also we get to reuse the EVM so they can make all the calls they want, to like, other contracts. But it requires us to have some sort of like persistent memory between these like calls to this singleton contract like swaps, mints and burns. So for that all we have today is like storage and storage I guess, as everyone here probably knows is has some like refund mechanism for transient torage. So if you set a slot from zero to non zero and then back to zero. So then you get a refund, a large refund, which is the majority of the storage cost. But that refund is capped in the latest hard fork to 28% of the total gas costs. But you can't do it. You can't do it sufficiently if there's a lot of slots that you need for like accounting, which we do need a lot of slots. And then you also have to SLOAD each of these slots just to know that they're zero, which they always will be in this pattern. So like SLOAD and SSTORE don't work very well for this. It also doesn't interact very well with execution parallelization because you should be able to parallelize all the transactions that touch these slots, 'cause they're always zero at the start and the end of the transaction. So, there's some interaction there with like access lists that is messy. So the proposal is that, uh, eip-1153 introduces these 2 new opcodes, TSTORE and TLOAD, which operate basically exactly the same as SLOAD and STORE , except the first TLOAD of a slot or the slots always start at zero, and at the end of the transaction, the slots were never persisted. So in between transactions there's no interaction. And yeah, it also has much lower gas cost because you don't have to load anything from from disk or from the state tree And yeah, I think this would be like a very successful pattern if there was some sort of like persistent memory between calls and I think like these opcodes can also just be a lot more efficient than the existing opcodes. There's also existing use cases like obviously reentrancy locks. But that's just one slot, so it's not as beneficial there. Yeah, I guess I'm interested in hearing if there's like other solutions that are better than this that I can push forward 'cause one of the big cons here is that any existing contracts that could make use of this will now need to upgrade and deploy new contracts. So, yeah, that's. Do you have any feedback? Love to hear it.

**Tim Beiko**: Yeah, thanks for sharing. Martin's Hand is already up so we can start there.

**Martin Holst Swende**: Yep, thank you. So I remember this proposition it's fairly old it's from 2018. And also so this one is basically a SSTORE which doesn't exist, and then it persist across the transaction. So you have the it across the call frames and I know there were other variants. I think there were at least one other variant of these of how temporary and they differed somewhat and I'm just curious if anyone recalls the other flavors Of temporary storage that are like if we're considering it, what which ones? Which variations would be on the table? That's kind of my question. I guess we collectively...

**Tim Beiko**: Yeah, and I guess Alexey is an author on this EIP and from what I skimmed on Discord, I think this was his kind of counter proposal to some of these variants, so it might just be worth also asking Alexey offline with the different variants where and their trade offs.

**Micah Zoltu**: In a in a hypothetical future where we have witnesses for everything one can imagine, I think providing as part of the witness providing just an assertion that this slot will be loaded and I guarantee you that it will be zero at the start and I guarantee it easier at the end. So the contract actually have to do any reads. So hypothetically this would allow us to also backport transient storage to legacy contracts. If that was something we desire because we basically put it at the transaction layer and say the transaction can declare. You know what some storage slot is going to be at start and end and it will guarantee that it will be the same, so we don't have to do the disk hits.
**Rai**: So are you suggesting changing the semantics of a SLOAD and SSTORE in the cases where they coincide with the slots that have that guarantee.

**Micah Zoltu**: Yeah, so basically you already guarantee as part of the transaction and then the EVM would then say Oh I Already know this is not going to change and so I can treat it as transient storage even though I'm doing that SLOAD and SSTORE.
I'm channeling my inner Aragon team. This will add complexity to the EVM versus just adding new opcode is much simpler. So I can definitely appreciate the argument for just using the new opcodes.

**Moody**: In that design, which you do not need to load the original value to see it is. What the transaction says it is.

**Micah Zoltu**: Yeah, you're basically just asserting that you know you could even just assert you know when... You can imagine it this way when you submit transaction the transaction as part of the signed transaction, it says, yeah, that might this won't work, ignore me. This little break stuff, yeah, never mind.

**Rai**: Yeah, and I was going to say also that that scales with the that scales with the size of the storage that you end up touching, like the maximum size that you end up using in the process of executing the transaction, how much transient storage you're using, which we might not want that scaling in the witness. Whereas if you have the TLOAD and TSTORE then yeah.

**Martin Holst Swende**: But for for like being in the concrete use cases with this I'm now asking   Moody, like the contract? Would you use this? Typically a lot of this, or just like very interested ... one or 2? Right? I'm feeling that the win and having accepted TLOAD and TSTORE is not that great if you're just using one of them. But if you were to need like 20 or 30 or 50, there will be a huge difference in the gas consumed.

**Moody**: Yeah, so so for the accounting. And the example I gave I've written a prototype and it's like a minimum if you just do one swap. It's like a minimum of 6 slots and that one swap itself might cost 100K Gas, but then these 6 SSTORE cost another 120K, of which you're only going to get up to like a 40K refund. So, It's it's very expensive to use storage transiently and that's why we need this opcode 'cause otherwise it's not really feasible. This pattern.

**Micah Zoltu**: Yeah, and I can sit back when I worked on Augur, we ran into this class of problem quite a bit where we had some piece of data that we're basically just passing from one call frame to the next, and it would need to be passed, you know, through all of them, and so your options are passive is called data through everything and you just have to keep passing it over and over and over and over and over again. Like for the entire call stack. If you had some sort of transient storage, you could just write into the transient storage and then the entire call stack would now have access to that, so you don't have to keep incurring the calldata at a cost each each frame, so there's another place where this comes up, where transient storage could reduce costs for everyone.

**Martin Holst Swende**: There there's no cost to calldata cost frame

**Micah Zoltu**: There's not?

**Martin Holst Swende**: Well, there is a memory expansion costs, but no, there's no calldata cost frame.

**Micah Zoltu**: Even across contracts?

**Martin Holst Swende**: Yep, even yeah I mean.

**Micah Zoltu**: Well, ignore me, I'm apparently totally out of it today. I must be misremembering.

**Martin Holst Swende**: But yeah, I mean there's still nowhere because when you access this in the next contract, optics on the memory in order to read it so, there is an overhead just hold it over.

**Micah Zoltu**: Yeah, maybe that wasn't...

**Moody**: So if I remember correctly, I think that this EIP was originally like preceded by like the different accounting for SSTORE of transient slots. But I think what makes it kind of unusable is just the refund cap. So, if there was no refund cap this might be workable even though you have to pay a bunch of gas up front you.
You still have to SLOAD the slots. But, yeah, I think like I think it's worth putting these into a separate opcode, because we don't want them to break and they have different semantics as far as like parallelization and like yeah, storage rental stuff.

**Martin Holst Swende**: My feeling here is the this is one of those EIPs that a lot of us think are like fine and it would be really nice if we had it many years ago and just a good thing, but it's kind of hard for us to like put a... how important is this and how much better would the world be like for a contract developers, if it exists and kind of, how do we prioritize this against other feature changes in the EVM? And and I think that's probably maybe where it has not been implemented. And there just hasn't been large enough cry from the like community of developers that we need this, and I think so what I mean... technically. Yeah, I mean it's worth, but it's not undoable. But yeah, how? How important is that and I think there needs to be some kind of work done to make it explicit how much better would it be? What kind of savings are looking at, how often you know? Yeah, how? How much do people want this? Is there a strong developments that decides this feature? So we can like rate, compare it with other features, prioritise.

**Vub**: You know one thing to add also is that there is a... like in the EIP for changing gas costs for verkle trees, there's a version of the proposal that adds back the refunds in the case where the slot is the same at the end as of the transaction as it was at the beginning. So like there is an alternative that like sort of works perfectly buggy but that's part of the benefit I guess would be interesting to compare both with the status quo.

**Micah Zoltu**: Is that something we get as soon as we get Verkle trees, or is that so we have to add on top of Verkle trees?

**Vub**: So there is... right now there's 2 of these Proto EIPS. One of the proto EIPs only changes that gas costs for reading and then there was another proto EIP that changes the gas costs for writing which is in my opinion we should do eventually, it's better, it's more comprehensive, it kind of it puts things like Storage edits and sending people ETH under the same framework. And that one has an extension for or we has a version in it for making the gas costs or refunding the gas when you reset something. And so yeah, it's like so. Basically it's it's in an extension.

**Moody**: So would that... you still have to pay the lowest cost as far as I understand.

**Vub**: Right, you still have to pay the load costs though, like that can be shared across an entire transaction or across many operations.

**Micah Zoltu**: Once we have witnesses, hypothetically, the initial gas costs... the initial SLOAD gas costs, do we expect that's going to drop down significantly, since everything is just going to be witness?

**Vub**: I think it'll be about the same, actually. Because witnesses are still a significant amount of data. Like the costs have been increased like over the like in a few times over the last 5 years. 5 years like. Part of that is the DoS issue, but part of that also is because of the witness size issues. The ones actually the one thing that will happen is actually. This might even be important is that the gas costs were accessing adjacent storage slots. That will decrease too. I think. The the current suggestions are either 200 or 150 and so like you'll be able to pay the 2000 points and you'll have a pretty big chunk of storage that you can use for all the transient stuff you want.

**Tim Beiko**: Uhm, Ansgar, you've had your hand up for awhile.

**Ansgar Dietrichs**: Yeah, I just wanted to add to this that I would also say that this will be the most important question for this EIP would be first I think to answer like is this something we can make work for the existing storage mechanism save with something like Verkle trees or is it something that that that will be an
extra feature addition. Because if it's feature addition which the counts EIP, at least, this I think we should really kind of take the time to go through all the alternative. Just as we were talking about earlier like that in the past several times and kind of really get this fight if it's something we completely add new because for me for example, it's to me it seems like if it's completely transient it would make more sense to have it be like a new type of memory rather than new type of storage because the whole kind of key value stores stores kind of design of the storage system is really just designed that way to be optimized for like databases and trees and whatever. And none of this really is relevant for transients and kind of storage, so it seems like would make more sense that just be like a continuous new type of memory block that's shared between contract unifications within the same transaction. So,
'cause they're saying like I feel like we should really for this EIP, it would really important figure out. Can we just basically modify the existing storage mechanism to make this cheaper again? Or if it's a new thing, really get the design for the new feature right and take the time for it?

**Martin Holst Swende**: Yeah, and that actually so in this EIP by Alexey. He does reference the point number 7 and shared memory and it says borrowed from an early draft of the similar EIP. So I think I did write the similar it once, which did not, so the difference was that it used to share memory... shared memory which could be shared by different contracts. So this EIP, you could have a temporary storage and you can come back later in another call frame back to your same contract and you can read what you wrote earlier. But, another variant would be to have a shared memory which you can write, and then you go execute in another contract and that can read the same memory that you wrote to earlier, which is another way to make life different for contract bugs.
Well, I'm sure there are different and then we have the gas using SSTORE with some new variations. Yeah, someone should really go through and figure out the different options we have.

**Moody**: So it sounds like it sounds like there's a couple follow-ups. One is like, how impactful is this for, like, all smart contract developers? Uhm, which I'm not sure what like evidence would be most convincing there, like I could maybe. I guess some feedback from other teams if that would be helpful. And then the other one is like what other... what is like the perfect, the ideal design for this... for solving this problem? And it might be memory instead of like the the key value storage. Design is that it is the 2.

**Micah Zoltu**: I think for metrics that wouldn't help to evaluate, even if you have a prototype for like 2 versions, one that has the temp transient storage, one that doesn't, and you can then show at least 4, you know next of Uniswap the gas cost difference for doing the exact same overall thing is X. That alone, I think, provides some evidence, like if we can show, hey, you know it's going to cost us 3 times as much to build our next version of Uniswap with without transient storage, then that's meaningful. Even if we don't have like a, you know, blanket from every dApp developer. Just having one developer who has done the research to show this to have a meaningful impact when designing things would be valuable. I mean, the more, the more that we can get the better, of course.

**Moody**: Uh, for that particular I have written a test of a swap that uses the transient storage and a swap that just doesn't and the difference is like double the gas. I guess I don't know exactly how to best share that stuff.

**Tim Beiko**: Definitely linking within the ETH-Magicians thread. I don't know if you have a maybe it's already there, but that seems like somewhere where, yeah, we can just.

**Danny**: I mean writing report in there or linking it external with like, not just Uniswap, but a number of case studies that would be very compelling.

**Moody**: OK, I mean the the code isn't public, so yeah.

**Tim Beiko**: Oh, right.

**Tim Beiko**: Yeah, at the very least, if you can just share what you know like shared on this call, like high level like you know... it saves about past the gas savings and and you know this is this is why that's valuable? I think if there's other applications that can you know, chime in. Similarly, like if they think that it would help with another version of their application and provide like significant gas costs. Yeah, that's also great. Yeah, and and I guess you. Know looking either at just like you know, number of users or the amount of gas they use on mainnet or something like that like where? Just to have a feeling for like how like their scale and the impact it would have on the overall network would be good.

**Micah Zoltu**: I suspect realistically the thing this the decision is likely to come down to whether or not we're going to get a solution to this for free with the Verkle trees if we do, then it seems like there's no point in spending the energy building this. If Verkle trees essentially solves this class of problems. But if it doesn't, then like Martin said, this is one of those things that is useful and valuable, and we could probably. I can imagine the CoreDevs being convinced that it's worthwhile, I don't know is if.. how far away are we from knowing which Verkle tree path we're going to go down? Are we like?
Years away or next, next call?

**Vub**: I feel like the specs of Verkle trees hasn't really changed significantly for quite a while. It's just like in an execution and testing slug

**Rai**: Why does? It's not obviously the Verkle trees then give us this for free?

**Vub**: Because then for the Verkle Tree EIP includes this gas costs changes that make that can be extended to add refunds and that make it easier to or that that reduce gas costs for things like getting many chunks of storage that are beside each other.

**Tim Beiko**: And I guess that's kind of an assumption we have on the protocol dev side. But like Moody, that's maybe also something that that can be valuable. If you know like you can just say for Uniswap specifically like how much you know how much better or how close does Verkle tree get you to buy this similar gas savings? That that would be really good to know.

**Moody**: Yeah, I think. The one thing that like Verkle trees, as far as I understand, we'll never be able to solve, is that you still have to put the original value, like it's still going to impact parallelization because you don't. You can't assume that the value is going to be zero at the beginning and gonna be thrown away at the end so it's like.

**Vub**: I, uh, I posted the link in case anyone wants to find the way.

**Moody**: I think there are some principle differences between what Verkle trees it helps with and like what this opcode does like that just can't be fixed and then also like there may be refunds, but like there's the cap, right? But I think Vitalik said earlier there wouldn't be a cap on these.

**Vub**: Right, I think there doesn't need to be a cap.

**Moody**: And then one other thing with Verkle trees is that if you write to a slot you can't remove that from the tree as far as I understand.
So like you're going to have some additional leaf which has zero and even though it's always going to be zero.

**Micah Zoltu**: If we start and end transaction at zero, is that true? Don't do we actually write the Verkle right few state if it stays zero permanently?

**Vub**: We do well we, I think in the current spec we like if it was none before then it switches over from one to zero. No, but if it was here before, then it's which is here is zero and there's no right.

**Micah Zoltu**: I see so, but but it does like create this kind of bloat this unnecessary.

**Vub**: So actually no. Though thinking out loud, there might be arguments against doing refunds, because if we do refunds and we do ERC-4337 then there might be a possibility of that gas tokens come back. Need to think through this. Right, so even if there are no refunds with the Verkle tree gas costs, the extra cost of using storage drops from being like 5000 and being like 700 for a slot.

**Moody**: Are you thinking in those first 63 slots?

**Vub**: Yeah, exactly.

**Moody**: That does prohibit the use of mappings for those transient storage, which...

**Vub**: I see.

**Moody**: And then we, in our worst case, access like we have to make more accesses to see I mean, yeah, maybe we could do mappings in that first 63 slots somehow, but it's pretty... it might be difficult.

**Vub**: Right, I see what you mean. The the application gets uglier. Yeah, I... right, I guess like the challenge with all of this is that like it's adding yet another type of memory as a significant increase through the I mean, if total complexity of the execution layer, and so if we can discover some way to get like either all of the benefits or even most of the benefits with the tweaks to existing stuff. That's something that probably should be explored first. But if there isn't, then maybe there isn't.

**Ansgar Dietrichs**: So one thing that I would just want to point out because I think in general and then like one thing we could do better in this awkward if is to be a little bit more more kind of open in setting expectations for your piece and and in this specific case I would just say because the kind of the the issue in the PM repro of course is called proposal to include the EIP in Shanghai. And so I would just say that right now I would probably say I would give this EIP a 10% chance of actually ending up in Shanghai. And if it's so so, because just because there's still so much that would have to be to be done here like first of exploring the vertical direction, and if it really turns out that this is just not sufficiently, doesn't get us sufficiently fine to that direction, then really kind of explaining that very clearly in making sure that everyone agrees that that's indeed the case, that there's a need for something like this then really figuring out what the very best version of this looks like, including having a lot of people kind of look over this, and agreeing that this is the best flavor of this that we can do, having everything prepared and ready. And even then it's kind of still depends on kind of there just being room in Shanghai. And so I would just basically say that like if this is really something that would be very important to try and get into Shanghai for you then... Then at least think that is something that would require a lot of effort between now and even relatively soon from now just... chance just to be transparent about that.

**Moody**: Yeah, that that makes sense. I agree I would love just more like attention, not because I'm not really a client dev and I feel very like out of my element trying to like figure out what is the best version of this so if anyone has any ideas to put on the thread like that would be great. And I feel bad I've already taken so much time in this meeting, but yeah I would I would love other ideas or other proposals to look at just any guidance firm devs, I can definitely provide stuff from the smart contract side.

**Tim Beiko**: I think I think that makes a lot of sense and like, yeah, trying to again, like we said, quantify the impact on the apps, figure out the best design, see the like pros and cons of Verkle trees is probably the right next steps and yeah, the the speed and at which we do that definitely plays a big role in whether this this might make in the Shanghai. Uh, yeah, right? Do you have one last comment on on this as well?

**Rai**: Did you...

**Tim Beiko**: Sorry what?

**Rai**: Did you call me? I didn't hear. OK.

**Tim Beiko**: Did you have a final comment on the EIP

**Rai**: yeah, I just I wanted to just check some my intuition about the parallelization. It's it sounds to me like not a big win, because yeah, you have that you know that property for the TLOAD that it's always going to be zero. But as soon as you hit your first SLOAD like validate executions gonna serialize again. Am I missing something there or, yeah, I just want to understand how much of a value add that is. This is just like a marginal one.

**Moody**: Well, in the case of this, like singleton design like you may not, you may have 2 swaps on different pools that don't touch any of the same slots. But if if they're using these this like transient storage and they are necessarily touching the same slots 'cause they all use the same slots for accounting. So like upfront, you can't know whether they can be parallelized or not, even though the starting and ending value those slots. The starting values always here in the ending value doesn't matter, so. They should theoretically be able to be parallelized.
# Shanghai Planning

**Rai**: OK, I can look into it more.

**Tim Beiko**: OK so yeah, last thing on the agenda we had is quite the can of worms. But basically Shanghai planning so Andrew had this comment like there is a lot of stuff already in the in the PM repo that's been proposed for Shanghai. Uhm, beyond all the EIPs that are directly in the repo there, there's also a Verkle trees which are kind of in a prototype state and there's obviously also the Beacon ETH withdrawals post merge, which which does not are not specified in an EIP yet. I guess yeah, Andrew, you know you had a comment about like you know, we don't necessarily want to go over everything, that's their proposed, but giving you a feel of what you know, we want to prioritize for Shanghai so. I guess maybe we can start with the like. Did you have thoughts about approaching this or priorities or yeah?

**Andrew Ashikhmin**: Well, I think. From Argon's team we are happy to work on the EVM improvements on on this track from EIP-3540 and EIP-3670 EIP-3690... so so the EVM objects format that that will be a a nice direction. I also have a general observation on that we have like we have 2 strategic directions, probably the the Verkle tree and limiting history availability. But for the and there might be some interesting interplay between the the 2 because for the Verkle tree you probably need to move to the unhashed state as the primary format, right? So currently probably only Argon uses the state with unhatched keys as the primary format, but you know, given the gas reforms in the Verkle tree, you you probably need to move to that. But it means that you know things like snap sync in gas have probably be... to switch to the unhashed state and also it, but it also means that for safer that transition from forsake guest notes that are currently snapped sync, you need to to be able to provide free images for from nodes that have been seen from from Genesis. So for instance error nodes can help with that Yeah, but so then from the hash state to unhashed state, you need a population of nodes sync from Genesis. On the other hand, if we pursue this direction with limited history availability, we are actually moving away away from the possibility of genesis sync and we need to kind of it's OK, I think in the long run. To do to limit history availability. But probably if we do that, we need to think carefully about how.. what are the mechanisms of historical availability and what do we do in terms of the sink that that the sync is based on on the unhashed state? And maybe yeah, so it's not well thought through through. Yeah, sorry about this is what I see that this kind of interdependency between history availabilities sync from Genesis and unhatched state for the Verkle tree.

**Tim Beiko**: Right yeah, thanks. Thanks for sharing I agree it's always kind of the hardest when there's like these, these big pieces of of like very applied R&D works that that interplay with each other and making sure we kind of ship them in the right the right sequence. Uhm, there's a comment in the chat for Martin asking, uh, that he'd like to hear from Vitalik about what he thinks the most important aligned things are. Uh, hum.

**Vub**: Hold on what's the what the the most important, then aligned with future plans things. I feel like OK, I'm... history expiry is definitely I think a top priority, both because it's just like it's just so obviously needed for any kind of like any of the scalability paths that we're looking at. Whether it's EIP 4488 or something or some version of sharding, UM? And I saw. Well, these withdrawals, I guess that got mentioned in the chat I personally feel like might feel like withdrawals waiting 6 months is less harmful than history expire E waiting 6 months given how much the scalability hinges on it, but I guess there's the question of like withdrawals are more a consensus layer thing, and I mean history expiry is more of an execution layer saying so is there even a trade off between them? Given that totally different people will be working on them. Uhm, other stuff oh. There is Verkle tree prep so that Verkle tree prep I guess includes some of the gas cost changes and yeah, and this is a self destruct them. These are probably the top that like I. But I think are like important for a few. Well, there's sharding stuff as well, but sharing stuff is still kind of under R&D. And so I mean, it's on track like that stuff. Seems the most important for future plans. OK CSLS, which shows might not be that minimal for EL. I don't know. I stand by my comments that withdrawls waiting for 6 months as well as the less bad than history expiry waiting another 6 months though I know if that's the traversal.

**Danny**: Right, but registry expiry we can and probably should be parallelizing. Right now, because it's not even related to a hard fork.

**Vub**: I agree, yeah, like I think a lot of this stuff actually like it can be parallelized quite a bit. What are some?

**Micah Zoltu**: I mean so... regarding parallelization, that is true only if you're all the client teams have different sets of people who would be working on hard fork stuff versus history.

**Danny**: Right, I mean I think the... because not a lot of it's also like design and interfacing with community and like setting expectations and stuff. There are technical things to do certainly, but there are like softer things that should be finalised today.

**Tim Beiko**: Yeah, it's almost like the EIP-4444 the consensus changes like the final thing you actually do. Right? You want the network to be in a spot where we can operate without history being fetched over the peer to peer layer. And there are kind of options available and then we just shut it off at the peer to peer layer. Or once you know that's been done. But yes, most of the work for that one can happen outside of consensus changes. And there are people working on it so it is already being paralyzed, yeah.

**Vub**: On the vertical stuff, I think I'm like. It's OK to like it's OK if Verkle trees get delayed more more than like say yeah EIP-4444 and scaling critical stuff gets delayed, but we do need to be proactive and early on it because there are a couple of backwards compatibility breaking things in there. One of them is the gas cost for reading code and the other is the self destruct ban. Like, I just want those things to, you know, not be a yes. One of those surprises where everyone suddenly freaks out about the need for half for half a year of research 2 months before we were hoping it would get in. I know there has been some proactive work on it. It would just be nice if there was a more proactive work on it. Oh I see the question of gas cost changes before Verkle right, right? OK, so this was say a, like basically the there was a proposal made to have gas price changes needed for Verkle trees go in before the Verkle hard fork. I guess it's not strictly important for that to for that to happen like you like. It's definitely totally fine everything to happen at the same time as well. I'm actually I think it might have been Dankrad who suggested that multi step road map so he would be yeah better to give the rationale for the for giving gas cost...

**Dankrad Feist**: Well, my main reason is like that... so the reason why I wanted to suggest that is that I think like every day that you don't like you, you know what the that, what the future of gas schedules should roughly look like. And every day that it is further away from that like you get more contracts that rely on current assumptions deployed, so that's my main reasoning for it. But I agree, so like also from my viewpoint when I looked at this further I actually think many things are not that far from our desired gas schedule, so my preference would actually be to focus on the self destruct like that's something that I think we should get out of the way earlier.

**Vub**: I do think that like the one big remaining difference between current gas costs and Verkle gas costs as the per chunk access of code, right? And like there are like, there are some exceptional cases where the EIP would give what more than a factor of 5 increase right?

**Dankrad Feist**: Yes yeah. Yeah, I know. But that that one it's also very hard to just do on its own, like if you only do that none of the things that make it cheap, it will be very hard to get that accepted, I think, yeah.

**Vub**: Right, I agree that's fair like it would just add a lot of transition complexity and we might as well just like move to the entire to the right event scheme, all all at the same time.

**Tim Beiko**: Ansgar, you have your hand up I know, and there's been a ton of comments and chats in parallel. So yeah, I just wanna make sure.

**Ansgar Dietrichs**: So yeah, I was just briefly going to ask and in general like do we think like we would we prefer Shanghai? That is slimmer but comes earlier or I mean I think we all agree the history kind of like that for EIP-4444, but it's important. But that again that doesn't need hard folk so we can just do it whenever. But like for the hard fork over changes in the heart folk, do we prefer a slimmer hard folk that can arrive sooner? Or do we want basically want to have a hard fork that has at least as many of the EIPs as we can reasonably fit into a hard fork and maybe takes couple months longer to write because I think that's really...

**Vub**: Do we need to do we need to decide now is the other question like we have more information 3 months...

**Tim Beiko**: We probably don't. But I think there's a I think there's probably a trade off between, do we include stuff that's mostly finalized and like you know, pretty straightforward or do we include things that are like more fundamental changes to how the network operates? Because we we do have there was this comment earlier in the chat about like the last feature fork we had was Berlin and we do have a lot of EIPs that are basically ready that are you know, standard EIPs that we kind of know how to do, and then we have things obviously like Verkle trees, history expiry those are like much bigger overhauls. So I don't know if it's a question of like how many EIPs you put in, but maybe there's an argument for putting this stuff that's like pretty well specified, pretty minor and and for example. Yes, there's BLS that's there. There's a ton of other ones that have been pending for over a year. Yeah, so I think there can be an argue... and then you know in parallel obviously we have people working on on history expiry. We have people working on Verkle trees but maybe it's simplest to just you know not consider those efforts for Shanghai and just try to get stuff that's pretty well specified out and and not like a massive kind of change. Include and I guess... I was gonna say sorry the one thing I think might actually be like a non trivial change is the mechanism by which we credit beacon chain withdrawals into the EVM there's nothing like this that exists, but it's it's not that it's like super complicated, but it's it's very new. And that it all...

**Danny**: There is something like it it the issuance the coin base is kind of similar.

**Tim Beiko**: Right, but the issue is the...

**Danny**: I know, I know it is very I'm being confusion Coinbase I personally have in my intuition is that the value of this work is one to get withdrawals out and to to as the pressure relief valve on all the on many of the more minor EVM and user related features and I think that in your intuition that, yes, you have this thing that kind of does fundamentally change something that's withdrawals. And maybe we shouldn't have 3 other things that fundamentally change something, and you know hit that fundamental change and then a bunch of pressure relief that things for users.

**Tim Beiko**: Yeah, I agree with that. Uh, Andrew?

**Andrew Ashikhmin**: Ah yes, sorry. I wasn't clear earlier. I just wanted to say that if we do history expiry before before the local tree, then we actually might hinder the Verkle tree transition because for Verkle tree will probably need a population of nodes sync from Genesis. And if we do history expire that might be problematic.

**Vub**: Wait, can you elaborate why we would need a population of notes thing from Genesis for the Merkle tree?

**Andrew Ashikhmin**: Because for so currently there are many geth nodes that that are sent to using get snap sync and there they don't have pre images so all the keys are hashed and they for them to unhash the keys they need pre images.

**Vub**: Umm, I see so they can have the full...

**Dankrad Feist**: How, how? What's the size of your status as? Like only keys is probably not that huge.

**Andrew Ashikhmin**: It's fine, so like because Argon nodes... all Argon nodes are synced from from Genesis we can provide them relatively easy... is what I'm saying is that if we like this you this history expiry path then it will be probably more and more problematic to have a population now it seems from Genesis and then this transition will be more problematic. But in terms of the volume of the preimages, it shouldn't be a problem at the moment.

**Dankrad Feist**: But I mean just provide that as a...

**Andrew Ashikhmin**: Umm yeah, but still like if well, how reliable is that? So I'm saying like are currently before we do history expiry, we can do that relatively easy later. It will be more problematic.

**Dankrad Feist**: Wait, but I'm not sure, but I mean what what you're saying is that your suggestion for recomputing those keys is to replay the whole history, because only when we play the history you know all the keys, right?

**Andrew Ashikhmin**: Right, right, but but we already have a sizable population of Argon nodes that already have our archive nodes and have that information.

**Dankrad Feist**: But like I mean, I would need to look into this but but but you're like if the solution to the missing keys is like every node replace all it's old history again to retrieve those keys. That doesn't seem better.

**Andrew Ashikhmin**: No no no. So snap synced geth notes can say ask either 4 archive geth notes or Argan notes to provide those keys. The snap sync notes they don't have to replay everything from scratch, they only needs to acquire the pre images.

**Dankrad Feist**: Right or even simpler, they you just get a torrent file of a few 100 megabytes or something that has the keys.

**Andrew Ashikhmin**: Well, it's a moving target. Stores like torrent, it's possible and we are developing something like a torrent based solution for Argon V2 bugs.

**Martin Holst Swende**: We basically go submit pre images can be cryptographically verified when we receive them. Torrents, there's no cryptographic type torrent. We don't have a header that says full... torrent.

**Dankrad Feist**: Yeah, but the client only contains the pre images. So you can like cryptographically verify the whole file once you have it. There's no trust. There's no trust in that torrent or anything. It's only a way to actually get those keys.

**Peter Szilagyi**: I mean, you don't really need to verify anything, you can just download the keys from wherever and just hash the money. You don't have that image. Yeah, I, I mean there's not much to verify, although with the story.

**Dankrad Feist**: Yes, yeah, I agree, I agree. Yeah, so like any source where you can download this seems seems like a solution to that.

**Peter Szilagyi**: Yeah, but with the torrent will always be outdated so we will always miss the most recent number of pre images.

**Micah Zoltu**: I believe the general strategy idea with torrents as solution is you would just do like a torrent every 6 months and from there... But why why? Why would be a new?

**Dankrad Feist**: There's no new torrent once you have made the transition this is this is only old keys that we're talking about, right? From the point in time when the verkle transition happened, there's no more keys added to this, and even before like so, the problem seems to be that some clients currently don't store those keys like we could make an upgrade now that start storing all those keys at..., right?

**Peter Szilagyi**: But so storing keys, you can store the keys for the blocks that you process, but if you do a fresh sync you will not have those key because those keys are not part of the network protocols. There's no way to repeat those keys currently. I cannot sync them.

**Dankrad Feist**: Right, I agree, but I'm I'm the only thing I'm saying is that this doesn't have to be like a super instant process, that right now I need the torrent with all the keys, right? This can be like a like say, 2 week before the before the Verkle transition. Every client starts locally building up or the all the keys that they encounter. And then the torrent would only need the all the keys as of 2 weeks ago. And there would never have to be an update to the torrent. And from my perspective, this does not seem like a major argument and like in terms of the ordering that we need to do. The worker before history I, I don't. I don't see that.

**Tim Beiko**: Yeah, and I guess this kind of comes back to like for Shanghai. Do we do we want to use it as more like a pressure release mechanism as these things are getting fleshed out and prototyped in parallel. There's another comment about like the timelines in in the in the chat I think we probably don't want to like feel like we have to rush Shanghai right after The Merge. Given the amount of like rush or or like pressure there is around the merge already. Uhm, we obviously want to ship it. You know, after, but like, I don't think there's like anything in in Shanghai that requires kind of a massive level of urgency and so it's kind of hard to say like exactly when it would land given we're not even sure when when when, the merge will be on mainnet, but I think we we should try to, you know obviously you have these discussions about clarifying. What was the scope of it? What do we want and gradually we will get kind of a better picture for it, but uhm? Yeah, I wouldn't rush to say like we need to ship these things. You know 3 months after the merge or something like that. Ansgar you have your hand up.

**Ansgar Dietrichs**: Yeah, I just wanted to say that maybe one thing again that we should definitely should decide today of course, but that at least I think would be helpful to keep talking about a little bit over the next 2 calls is whether we might want to just commit on having 2 feature forks, the Shanghai and one after it, and then the next topical fork that I assume would be verkle related or whatever. Maybe else bakers is ready just because I think, uh, last time was with London. One of the problems was that it basically really felt like the last feature fork for the next 18 to 24 month. And so a lot of your peers really wanted to get in, and then we can decide not to to put some in inside back here. But you can get into the November fork and then we of course later on, just silently decided to not have a feature for in November, and so I just feel like physically managing expectations by just being very upfront about. OK, this is one chance to get your..., but we are already committing to having another feature fork 4 to 6 months later. And so, so that that that it's it's OK to basically only go ahead with with Shanghai with like the smallest number set of simple things that are already ready relatively soon after the match or something. I think that would really simplify things. I'm not saying we should do that necessarily, but I think we should always consider that option and potentially commits to doing that relatively early on in the process.

**Tim Beiko**: And I guess the argument there is if you have 2 small 2 small forks, you can kind of do them quickly and and and like I get I guess yeah, maybe. The other way to put this is like If you have 2 small forks, you do delay, you know verkle trees, for example by an extra 3 to 6 months at least. So is there an argument that like instead of just having these 2 small, you just make one kind of medium or large hard fork and and that's it like and then the next one is more of a you know protocol level change rather than like application level change, if that makes sense. Because like I guess my fear is like if we do something like you commit the 2 future forks you delay the kind of longer term kind of protocol research, but then it's also maybe the stuff that's in the second fork. Wasn't like actually that important, because if it was then it would have been in the first fork. So that's yeah, I'm. Yeah, I'm not sure how we how we just make sure that like we're not just creating a delay and and have a yeah and delaying the stuff that's really important for the protocol because we feel there's just too many things and and and it's like an excuse not to just prioritize a bit better. Obviously, yeah, it's not like the last conversation we have about this and we'll need to have more in the coming in the coming calls. I think one thing though, that for Shanghai is for people listening, like if you do have any IP that you want to propose for Shanghai it should probably happen sooner rather than later. And even you know, like today, Ansgar your comments felt like it, it's unlikely. Or it's not like yeah, it's definitely not a certainty that, like EIP-1153, makes it in and I think given the amount of stuff that's already there, that's like scoped out and what not. Like we probably don't have a ton of bandwidth for new proposals to come in and, and if so, they probably need to be presented soon and you know, kind of show or yeah, articulate why they're more urgent in a way than than what's already being there. So yeah, I think if if people have ideas or proposals for Shanghai they should probably bring him in quite soon so that we can have at least like a, uh, a rough final list of stuff to consider in the coming month or so.

**Martin Holst Swende**: Yeah, I'm a bit surprised. Like half a year or a year ago there was. A large group of people really push for EIP-3074, but I haven't heard about that since then. I'm curious suggesting people pushing for it.

**Tim Beiko**: I think light client is maybe too polite to keep bringing it up.

**Danny**: I think that like I think the 3074 crew realized that The merge needed to happen before the EIP-3074 conversation can continue.

**Ansgar Dietrichs**: Alright, yeah, maybe just briefly on the status of EIP-3074 and so basically it just because it keeps getting mentioned also in chat and everything I just think that we as a team just realized that a lot of people having concerns and of course no change in that should ever get accepted into protocol. While a lot of people served.
And so we're just basically waiting for a moment in time that is sufficiently kind of peaceful. But we have some time to try and convince people once more, and also of course we are in the background kind of looking into the EIP. Maybe things we can change to make it to address some of the concerns, so it's definitely something that that we still want to try and bring to mainnet at some point if there's an opportunity, but only dependent on us actually being able to convince people ofcourse. But it's not. It's not dead, it's just waiting for for us to calm down and and maybe have that have an opportunity to to look into there.

**Light Client**: We're also available to discuss any concerns with 3074 people. I know that there are still people who don't think EIP-3074 is is is safe or they have other concerns about it and we're available to to discuss it. We I've just stopped talking about it incessantly in the calls because there's other important things to discuss. But we would really like to propose EIP-3074 for Shanghai.

**Tim Beiko**: Yes, and it is on the list, right? Like and oh, by the way, I guess if people want to see the list, it's not perfect. But uh, issues repo of the Ethereum/PM. Uh, yeah, the issues linked sorry of the Ethereum/PM repo, has everything I think that's being proposed. The only thing that's missing from it is basically beacon ETH withdrawals because there's no, there's no formal EIP yet, and also I think the EVM Object format EVM EIP-3540 is is in that list, and there's a couple companion EIPs I think might not be in... But yeah, if you want to get like a rough deal for like all this stuff that that has been proposed for Shanghai, that's the place to look. And then in today's agenda, Andrew also re compiled the list there and has the Beacon ETH withdrawals there. Yeah, oh and verkle Vertical trees also. Yeah, doesn't have a specific EIP such as proto EIPs. But that's where people should go... And if people want to propose something for Shanghai to just open an issue there, like you can literally copy paste any of the ones that's already open, and we'll make sure to add it in one of the the the upcoming calls. Anyone had anything else? They want to cover either about Shanghai or from the merge or any other topic?

**Greg**: Yeah, I also wanted to support the EOF related ones. Yeah, the EVM work has been sort of stalled for a long time and those are just a fundamental basis for making for making further progress. And I don't want to see though, it's delayed anymore than necessary the team has been doing really good work on that, and they're pretty much ready to go, I think.

**Tim Beiko**: Yeah, I agree, there's been a ton of really good work and like iterations on the EVM EIPs which led to this this series and it would be really nice to see them see them get deployed.

**Light Client**: I also think... I just want to say also on EOF. I think that there are interesting longer term proposals that do rely on having the ability of having different types of contracts in in the EVM, and so the sooner that we can get the basic version of the EOF onto mainnet the sooner we can start to really think about you know future things that can be built on top of it.

**Micah Zoltu**: Do we have? So the we we talked about having like one or 2 hard forks from Shanghai. Is it? Is there anyone any reason we can't commit to all those little easy things like the EOF ones and BLS? And just like the stuff that we sounds like, everybody kind of agrees, is easy, non contentious, we just need to get it in the pressure release valve stuff is that going into Shanghai, no matter whether Shanghai is big or small.

**Tim Beiko**: So the reason I don't think we want to commit this 'cause there's probably like 10 of them and I can see a world where, like we just do 5. You know, I don't know these are never accurate, but like I think... and I also want to let people you know give people time to like digest this call and and and discuss things async. But like assuming we did want to go like the the the pressure release route, I don't think we can include everything that's like in the backlog and so you don't want to tell people like, oh yeah. If your EIPs been pending for 2 years, it's going to be in...

**Ansgar Dietrichs**: Just for the record, I think even something like EOF, which I think everyone that is looking to adjust excited, but I'm certainly quite excited about it, but I think even that has like sufficiently big long term implications to the EVM that I think it would be important that everyone basically is familiar with it and we do spend some time alone AllCoreDevs talking about the implications and if we're all comfortable with it and I would hate for this to basically happen so late in the process of the the hard fork that for some reason maybe concerns can be addressed in time or something, and then it would be kicked out of the the the the forks. I think that's something that we should also do sufficiently long before before the hard fork that it yeah doesn't impose a risk.

**Tim Beiko**: Oh, and one last thing related to hard forks without Shanghai. The consensus layer folks have found a name for their merge hard forks or the hard fork at which they basically set the the TTD and and hard code it. If we want, uh, yeah. Basically, if we want suggestions for that, we should definitely not call that thing Shanghai, given the amount of attention that there's been already. But basically the release of the yeah, the release of execution clients that basically supports the transition. And Marius says the merge is good enough. I personally disagree. I like the idea that the merge is the whole process and and you know each of the client releases have have upgrades, but we can discuss that async. But yeah, we I the thing I do feel strongly about this. We definitely should not call that thing Shanghai. I think there's enough like consensus around Shanghai being the first feature for after dinner after the merge. Anything else anybody wanted to bring up? OK, well yeah thanks everybody uhm.
I will see you all in 2 weeks and there is the consensus layer call next Thursday to discuss merge stuff.

**Everyone thanks each other and says goodbye.**

## Chat Highlights:

- 08:58:20 From  Marius Van Der Wijden (M) to Everyone: hat are we going to do against the bogdanoffs dumping eth?
- 08:58:43 From  Gary Schulte  to  Everyone: 😭
- 08:59:00 From  Trenton Van Epps  to  Everyone: the bogdanoffs are dead
- 08:59:22 From  Gary Schulte  to  Everyone: stuff
- 08:59:26 From  Marius Van Der Wijden (M)  to  Everyone: hey guys
- 08:59:30 From  Marek Moraczyński  to  Everyone: Hi!
- 08:59:39 From  Tim Beiko  to  Everyone: Happy new year, Marius!
- 09:00:20 From  Marius Van Der Wijden (M)  to  Everyone: Thanks! Happy new year to you too
- 09:01:19 From  Greg Colvin  to  Everyone: https://youtu.be/Re4-HaLdmR8
- 09:02:18 From  Trenton Van Epps  to  Everyone: the memes will persist
- 09:02:21 From  Trenton Van Epps  to  Everyone: have no fear
- 09:02:28 From  Trenton Van Epps  to  Everyone: also your mic is very noisy
- 09:02:41 From  Marius Van Der Wijden (M)  to  Everyone: new mic :/
- 09:02:52 From  Gary Schulte  to  Everyone: HNY
- 09:03:14 From  Tim Beiko  to  Everyone: https://github.com/ethereum/pm/issues/436
- 09:07:27 From  pari  to  Everyone: Deploying nethermind’s fix now, we should know more soon 🙂
- 09:07:44 From  Marek Moraczyński  to  Everyone: 🙏
- 09:07:53 From  Gary Schulte  to  Everyone: Just now woke up to this bug - will get besu fix up post haste
- 09:09:31 From  Tomasz Stańczak  to  Everyone: destroyer of testnets stroke again
- 09:09:53 From  MariusVanDerWijden  to  Everyone: :D
- 09:16:25 From  Rai  to  Everyone: https://eips.ethereum.org/EIPS/eip-1153
- 09:19:48 From  Micah Zoltu  to  Everyone: Worse, witnesses will grow significantly in this use case without transient storage.
- 09:20:32 From  Tomasz Stańczak  to  Everyone: 1. this would be a non-quadratic cost memory access
- 09:20:43 From  Micah Zoltu  to  Everyone: Non-quadratic?
- 09:21:05 From  Tomasz Stańczak  to  Everyone: currently the cost of memory is non-linear
- 09:21:17 From  Tomasz Stańczak  to  Everyone: this would make the memory cost linear
- 09:21:28 From  Tomasz Stańczak  to  Everyone: and it could be used as an alternative / cheaper way of allocating much memory
- 09:21:39 From  Micah Zoltu  to  Everyone: Are you talking about the gas cost, or the operational cost (which *should* be the same, but isn't always)?
- 09:22:01 From  Tomasz Stańczak  to  Everyone: gas cost
- 09:22:03 From  Micah Zoltu  to  Everyone: Oh, you are saying that the current spec does linear, but it should be non-linear?
- 09:22:32 From  Tomasz Stańczak  to  Everyone: EIP01153 spec provides a linear cost
- 09:22:46 From  Micah Zoltu  to  Everyone: 👍
- 09:22:49 From  Tomasz Stańczak  to  Everyone: 32bytes 200 gas each
- 09:23:15 From  Trenton Van Epps  to  Everyone: Somu if you are talking your mic isn't working
- 09:24:31 From  Tomasz Stańczak  to  Everyone: any security risks if someone tries to control the contract flow to enforce a pattern of memory updates via reentrancy
- 09:27:26 From  Ansgar Dietrichs  to  Everyone: why the choice of transient storage rather than persistent memory btw?
- 09:28:17 From  Micah Zoltu  to  Everyone: What do you mean by persistent memory?
- 09:28:57 From  Ansgar Dietrichs  to  Everyone: similar to the transient storage, contracts have access to a second type of memory that is persistent within a single tx (for that contract)
- 09:30:06 From  Micah Zoltu  to  Everyone: What is the difference between the two?
- 09:30:28 From  Rai  to  Everyone: vibes
- 09:30:36 From  Ansgar Dietrichs  to  Everyone: the way you interact with it (each word individually vs larger chunks)
- 09:33:18 From  Rai  to  Everyone: Ok what am I missing it looks like MLOAD and SLOAD both interact the same way? With 1 word loads?
- 09:34:31 From  Micah Zoltu  to  Everyone: MLOAD gas costs aren't fixed per WORD or something, if I understand what Thomasz was saying is correct?
- 09:34:45 From  Micah Zoltu  to  Everyone: Or maybe it is MSTORE that isn't constant.
- 09:35:44 From  Moody   to  Everyone: axic mentioned this here https://ethereum-magicians.org/t/eip-1153-transient-storage-opcodes/553/44?u=moodysalem
- 09:41:53 From  Vub  to  Everyone: https://notes.ethereum.org/@vbuterin/verkle_write_gas_extension
- 09:51:32 From  Ansgar Dietrichs  to  Everyone: +1 to EOF, it would require some core dev attention, but seems like an important building block for the future of the EVM
- 09:51:42 From  Martin Holst Swende  to  Everyone: re shanghai features-- I'd be interested to hear what @Vub thinks are most important / aligned with future plans
- 09:54:26 From  Ansgar Dietrichs  to  Everyone: I think a general question for Shanghai is: do we want the minimal fork as quickly as possible (mainly for withdrawals), or do we want the best feature fork we can have? because we haven’t really had a feature fork since Berlin…
- 09:54:57 From  Trenton Van Epps  to  Everyone: withdrawals should be top priority?
- 09:55:10 From  danny  to  Everyone: but history expiry doesn’t have to be placed int a hard fork
- 09:55:20 From  Micah Zoltu  to  Everyone: That isn't far enough future for Vitalik to think about Trent.  😆
- 09:55:37 From  Trenton Van Epps  to  Everyone: imo withdrawals are crucial for shanghai
- 09:55:41 From  Tim Beiko  to  Everyone: Is Withdrawal really a CL level thing?
- 09:55:46 From  danny  to  Everyone: it’s both
- 09:55:50 From  Micah Zoltu  to  Everyone: CL+EL for withdraws.
- 09:55:54 From  danny  to  Everyone: probably a bit more complexity on CL
- 09:56:10 From  Tim Beiko  to  Everyone: Yes, but I think it might not be that minimal for EL given that we don’t really have a clean way to “credit ETH from somewhere else”?
- 09:56:24 From  Ansgar Dietrichs  to  Everyone: I don’t like listing 4444 as an EIP for Shanghai, given that it would only be something “to do around Shanghai”, not an actual protocol rule change
- 09:57:09 From  Ansgar Dietrichs  to  Everyone: I would be strongly opposed to Shanghai without withdrawals, but think that 4444 can come before Shanghai
- 09:57:57 From  danny  to  Everyone: I agree. really need withdrawals imo
- 09:58:05 From  danny  to  Everyone: already broke a promise to *not* have them right at the merge
- 09:58:27 From  Micah Zoltu  to  Everyone: Meh, I'm with Vitalik that withdraws aren't *that* critical.  As long as people believe they'll be able to *eventually* withdraw the economics generally work out.
- 09:58:30 From  MariusVanDerWijden  to  Everyone: What gas cost changes should go in before verkle? Does it make sense to have these before the actual code is in place?
- 09:58:46 From  Micah Zoltu  to  Everyone: We just can't delay so much that people stop believing withdraws will ever happen.
- 09:58:50 From  Ansgar Dietrichs  to  Everyone: I personally prefer having all Verkle-related changes be part of the main Verkle fork
- 09:59:31 From  Tomasz Stańczak  to  Everyone: we have one engineer and one intern working on Verkle trees in Nethermind if anybody is interested
- 10:00:32 From  MariusVanDerWijden  to  Everyone: Agree, yeet selfdestruct asap
- 10:00:33 From  Tomasz Stańczak  to  Everyone: withdrawals are critical imho from the perspective of financial markets around them
- 10:02:13 From  Micah Zoltu  to  Everyone: Ansgar: "Do we prefer slim sooner or fat later?" Micah: "Is the EIP I care about in the slim version?  😬"
- 10:02:24 From  Rai  to  Everyone: lol
- 10:02:31 From  danny  to  Everyone: 🤣
- 10:02:34 From  Tomasz Stańczak  to  Everyone: generally in favour of slimmer bot more frequent forks
- 10:02:39 From  Ansgar Dietrichs  to  Everyone: I don’t think we need a decision now, but we should start having some thoughts around the timeline here
- 10:02:44 From  Tomasz Stańczak  to  Everyone: lol at Micah's comment :D
- 10:03:05 From  Micah Zoltu  to  Everyone: We know how to do BLS, does that mean it is going into Shanghai?  😬
- 10:03:14 From  danny  to  Everyone: plzzzz
- 10:03:44 From  Tomasz Stańczak  to  Everyone: we all got the BLS implemented, do we? did it age since then?
- 10:04:36 From  Tim Beiko  to  Everyone: I think I agree with Danny’s “pressure valve” metaphor :-)
- 10:04:53 From  Trenton Van Epps  to  Everyone: yes, agree as well (for as much as my opinion is weighed lol)
- 10:05:07 From  MariusVanDerWijden  to  Everyone: I think there are some no-brainer EIPs that should go in: EIP-3855 (Push0), EIP-3651 (warm coinbase), EIP-3860 (limit initcode) and maybe EIP-4396 (time aware basefee)
- 10:05:25 From  Micah Zoltu  to  Everyone: Trent, your opinion weighs more then mine, so you have that going for you at least.
- 10:05:39 From  Tim Beiko  to  Everyone: I personally think 4396 is in the “changes big things” bucket, but not a super strong opinion!
- 10:05:54 From  Tim Beiko  to  Everyone: I also think we should probably have it prototyped in case we realize, post-merge, that we *really* need it ASAP
- 10:07:00 From  Ansgar Dietrichs  to  Everyone: waiting for Verkle before we do 4444 would delay 4444 by a year
- 10:07:15 From  danny  to  Everyone: We have a CL withdrawals PR in progress. I plan to clean this up in next week and aim to get an associated EL EIP for handling that side out shortly after
- 10:07:33 From  Tim Beiko  to  Everyone: One EIP I’d be curious to “dive back in” is 3074, too.
- 10:08:06 From  Tim Beiko  to  Everyone: (Not on this call, but it seemed like it could happen, and there was a lot of application support for it)
- 10:08:09 From  Greg Colvin  to  Everyone: Looking at the Magicians thread 4444 is controversial.  So far I remain against it as it stands.
- 10:08:10 From  Ansgar Dietrichs  to  Everyone: +1 for 3074, if we will be able to address all the remaining concerns of course ;-)
- 10:08:22 From  MariusVanDerWijden  to  Everyone: 3074 is very big bucket imo. And associated discussion will probably delay the fork
- 10:08:41 From  lightclient  to  Everyone: That’s why we should start early :)
- 10:08:48 From  Trenton Van Epps  to  Everyone: well, now is the time to start that discussion lol
- 10:08:52 From  lightclient  to  Everyone: (already started almost a year ago fwiw)
- 10:09:06 From  Tim Beiko  to  Everyone: It is: we’re still finding consensus bugs on merge devnets :-)
- 10:09:42 From  Ansgar Dietrichs  to  Everyone: what’s the timeline here? are we happy to make final decisions about EIPs to include after the merge has happened, or would we want a final decision earlier so that we can already have implementations & do the fork very close after the merge?
- 10:10:06 From  lightclient  to  Everyone: i feel like around march/april we should have a pretty concrete view of the fork?
- 10:10:12 From  Tim Beiko  to  Everyone: I think we don’t want to set the expectation of “very close” after the merge
- 10:10:17 From  Micah Zoltu  to  Everyone: Damn it, I am doing horrible today.  I thought we were talking about 4444, not verkle tries.  😖
- 10:10:28 From  danny  to  Everyone: pay attention Micah!
- 10:10:29 From  Tim Beiko  to  Everyone: The merge is a _huge_ bit of work, and I don’t think we want to put pressure to ship the next thing ASAP
- 10:10:31 From  Ansgar Dietrichs  to  Everyone: (so basically, are we targeting August or December - February for Shanghai)
- 10:11:01 From  MariusVanDerWijden  to  Everyone: I am also against 3074 in it's current form, especially given the recent flood of news about people getting their NFTs etc stolen by signing weird stuff
- 10:11:02 From  Tim Beiko  to  Everyone: But yes, I think as the merge hits mainnet, we should have a pretty clear view of what Shanghai should be
- 10:13:23 From  Trenton Van Epps  to  Everyone: > I am also against 3074 in it's current form, especially given the recent flood of news about people getting their NFTs etc stolen by signing weird stuff  so no change from the status quo?
- 10:13:58 From  MariusVanDerWijden  to  Everyone: Well 3074 would actually make it worse in my opinion
- 10:14:58 From  Ansgar Dietrichs  to  Everyone: can we please not discuss 3074 now? :-)
- 10:14:59 From  Micah Zoltu  to  Everyone: For 3074 to go wrong, I believe wallets would need to be modified to be *worse* than they currently are.
- 10:15:13 From  lightclient  to  Everyone: Do you btw happen to have a link that describes what’s happening when these ppl are signing weird stuff?
- 10:15:18 From  lightclient  to  Everyone: (anyone)
- 10:15:20 From  Micah Zoltu  to  Everyone: By default, wallets protect users from 3074 shenanigans by default (and in fact prevent its use entirely IIRC?)
- 10:17:08 From  Rai  to  Everyone: I think they died
- 10:17:15 From  Micah Zoltu  to  Everyone: Just their souls.
- 10:17:15 From  Sam Wilson  to  Everyone: I'm still here >.<
- 10:17:19 From  Moody   to  Everyone: i am very pro 3074
- 10:17:46 From  Tim Beiko  to  Everyone: AIUI, for NFTs, people don’t “sign weird stuff”, but literally send their seed phrase
- 10:17:56 From  Moody   to  Everyone: ^
- 10:17:59 From  lightclient  to  Everyone: that’s what i thought too haha
- 10:18:07 From  Moody   to  Everyone: ban self custody?
- 10:18:10 From  Rai  to  Everyone: hahha
- 10:18:13 From  Trenton Van Epps  to  Everyone: yes, seconding tim
- 10:18:14 From  Micah Zoltu  to  Everyone: 😂
- 10:18:34 From  MariusVanDerWijden  to  Everyone: WTF really?
- 10:18:40 From  Tim Beiko  to  Everyone: Yes
- 10:18:48 From  Micah Zoltu  to  Everyone: Often.
- 10:18:58 From  Trenton Van Epps  to  Everyone: marius sounds like you need to do some NFT user research haha
- 10:19:03 From  Micah Zoltu  to  Everyone: Giving away seed phrases is the new cool thing to do.
- 10:19:16 From  pari  to  Everyone: Accepting seed phrases starting 2 mins ago, DMs open
- 10:19:17 From  Sam Wilson  to  Everyone: I think the counter argument is that if people send their seed phrases, I can't expect them to care about what invokers they sign for.
- 10:19:17 From  MariusVanDerWijden  to  Everyone: Yeah maybe we should do a whitelist for users
- 10:19:34 From  Micah Zoltu  to  Everyone: 😖
- 10:19:36 From  Ansgar Dietrichs  to  Everyone: maybe only let accredited investors send txs on Ethereum?
- 10:19:45 From  Micah Zoltu  to  Everyone: 😱
- 10:19:59 From  Greg Colvin  to  Everyone: The EOF related ones — EIP-3540, EIP-3670 and EIP-4200 — are easy enough.  The work I’m doing on 2315 and 3779 for subroutines and EVM safety depend on then.
- 10:19:59 From  Trenton Van Epps  to  Everyone: alright chat, save it for the after-party call
- 10:20:04 From  pari  to  Everyone: Call it EIP-Nein ?
- 10:20:16 From  Moody   to  Everyone: i would love feedback on eip-1153 and help coming to consensus on the best form of this feature, so if anyone has time please message me on telegram 773-469-4911 or discord  user id 383836935480803339
- 10:20:32 From  MariusVanDerWijden  to  Everyone: Every transaction needs to be manually vetted by a core dev
- 10:20:49 From  Ansgar Dietrichs  to  Everyone: (talking about the after-party call, be sure to find us in the #party-lounge voice channel of the Eth R&D discord after this call!)
- 10:22:12 From  Shashank Yalamanchi  to  Everyone: @ansgar For sure!
- 10:22:37 From  MariusVanDerWijden  to  Everyone: The only thing I would worry about with these is testing
- 10:22:42 From  Danno Ferrin  to  Everyone: Five sounds ambitious
- 10:22:55 From  Tomasz Stańczak  to  Everyone: they seem to be easy but they probably need a focused postmerge environment to say yes to
- 10:22:58 From  Ansgar Dietrichs  to  Everyone: I think even EOF (big fan!) needs some amount of core dev attention, to make sure we all feel like the current form is the version we want to bring to mainnet
- 10:22:58 From  Micah Zoltu  to  Everyone: Some are like 1 character changes I think.  😬
- 10:23:00 From  MariusVanDerWijden  to  Everyone: Hard to test 8 different proposals which might interact
- 10:23:40 From  Tim Beiko  to  Everyone: Right, cross-testing might be the best argument towards “two Shanghais"
- 10:23:52 From  Tim Beiko  to  Everyone: Testing 2x 4 EIPs might be easier than 1x 8
- 10:24:32 From  MariusVanDerWijden  to  Everyone: No, we don't want to name it
- 10:24:33 From  Micah Zoltu  to  Everyone: Wouldn't it be testing (n+4) + (n+8) vs (n+8)?
- 10:24:41 From  MariusVanDerWijden  to  Everyone: TheMerge is good enough
- 10:24:48 From  MariusVanDerWijden  to  Everyone: Less bikeshedding
- 10:25:05 From  stokes  to  Everyone: could leverage a glacier name
- 10:25:20 From  lightclient  to  Everyone: ^
- 10:25:22 From  danny  to  Everyone: a glacier name because it helps fight global warming
- 10:25:30 From  Shashank Yalamanchi  to  Everyone: lolol
- 10:25:32 From  Rai  to  Everyone: How about YEET
- 10:25:33 From  MariusVanDerWijden  to  Everyone: TheMerge glacier

## Attendees:
- Tim Beiko
- Danny
- Andrew Ashikhmin
- Ansgar Dietrichs
- Martin Holst Swende
- Daniel Lehrner
- Fabio Di Fabio
- Vitalik Buterin (Vub)
- Lightclient
- Marek Moraczynski
- MariusVanDerWijden
- Micah Zoltu
- Pooja R.
- Rai
- Moody
- Peter Szilagyi
- Trenton Van Epps
- Somu Bhargava
- Dankrad Feist
- Alex Stokes
- Justin Florentine
- HP
- gunnim
- Mateusz Morusiewicz
- Gottfried Herold
- Gary Schlte
- Greg Colvin
- Jose
- Shashank Yalamanchi
- Sam Wilson
- dade
- proto
- Tomasz Stanczak
- Andrei Maiboroda
- Lukasz Rozmej
- Danno Ferrin

---------------------------------------

### Next meeting on: January 21, 2022, 14:00 UTC

[Agenda](https://github.com/ethereum/pm/issues/449)
