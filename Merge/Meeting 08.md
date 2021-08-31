# The Merge: Consensus API design space
### Meeting Date/Time: Thursday, Aug 26 at 13:00 UTC
### Meeting Duration: 60 minutes
### [Github Agenda](https://github.com/ethereum/pm/issues/378)
### [Video of the meeting](https://youtu.be/il0nha1HSiE)
### Moderator: Mikhail Kalinin
### Notes: Alen (Santhosh)

## Decisions Made / Action items
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
|8.1 |Discussion about the 'coinbase might be overridden by the execution client or not' to be taken up in the Discord for further discussion | [36.13](https://youtu.be/il0nha1HSiE?t=2173)|
|8.2 |Usage of the safehead, we need to decide is that the unsafe head is at the safe head or is that finalized safe head? I think is the best option here because it's very close to the tip, but it's also very safe. And where is finalized is potentially pretty old and we don't want to give user block. That's, you know, several minutes old and unsafe is unnecessarily risky to the user. | [50.04](https://youtu.be/il0nha1HSiE?t=3004)|
|8.3 |Mikhail proposed to reach out the Geth team in this Discord to talk about this singe find requirements of the same process and on the API sync.. | [51.43](https://youtu.be/il0nha1HSiE?t=3083)|
|8.4 |Tim proposed to use Coredev next week to discuss about the merge | [53.05](https://youtu.be/il0nha1HSiE?t=3182)|



# Introduction
**Mikhail Kalinin**
* Okay, so I think we should start. Okay. So today we have this dog to walk through, and about the format of the call. We will just go through these documents if some breaks for discussion and some Force. Yep. I would like to like directly edit and add more info to this document right away. So let's just if they will be like a rough consensus around some stuff that is not an option or won't be on go to the standard of the Epi eventually. So we will just make the comments and drop it. Then the more important part I think would be to get more input on some stuff that is missed here that I've been missed here like scene. It says, we will stop for it in the middle. It gets sync is not like explicitly mentioned here as a section. Yeah, so but it should be, I guess. Yep. Or yeah, that's that's like the Enterprise like that. Yeah. Absolutely. Please don't hesitate to stop me at any point to make a comment or ask a question. If anyone Rises. And I might not see it today time. So just break the ends and go ahead with your stuff. So. Let's start to any, any questions. Yes. Conspiracy around. Turn on this edit mode. And thanks everyone for coming. Thanks a lot. Glad to see you here everyone.

**Mikhail Kalinin**
* So the first thing we will start from is the title. There have been a discussion in the Discord and Encore deaths channel. So, too, I think we should do this like renamed. These Epi to the engine API. So, the reason behind this is that we, we have the consensus API, which is the API of the, that is exposed by the software on the consensus layer, which is the second node API, which is the users. And what are the requirements? We also have the execution player API, which is the Ethereum JSON-RPC. It has several names. Namespaces. We are not about to rename those namespaces. But in general, this is going to be like referred by the execution API. And yeah, we have something in between those two layers, which is more specific to developers than users and like engine. I think it's reasonable Choice here to avoid to avoid the confusion. And also engine is a bit confusing because like client developers may say that they have the consensus engine in their pocket, textured design and they have this execution engine, but it's less like confusing than the other choice. This that we fight. 

**Danny**
* Alternative is maybe execution engine. API engine API data for short, like the name space, but then that kind of has a conflict, the execution API,

**Mikhail Kalinin**
* Right? So do we does anybody opposed to start using this term? In application is a set of methods that is explained in this dark and that will go through the standard. 

**Speaker 03**
* You drop a link to this page in the chat. To this. 

**Mikhail Kalinin**
* Yeah, it's already there. The time isn't it?

**Danny**
* Depends on when you join on whether you can see it. Oh, yeah. Yes. Yeah. Thanks.

**Mikhail Kalinin**
* Looks like I got one from someone. Okay, so I think we're good with this name and let's move on. Yeah. Okay. 
* So we are this is the design space. We will shape it shape it and more stuff removed some stuff. Okay, so in Yeah, we are. We want to reuse as much of existence, JSON-RPC implementation, which is obvious. Like, the reason behind this. 
* The security of this API is critical and it's been agreed that it will be exposed on the independent Port. Don't think we should stop here for in discussion. Also, we are picking up the new namespace name, and we keep this idea that was proposed by Proto to try to reuse the set of methods for the execution client. Try to use them on the layer-2 Solutions in the Roll-Ups, in the clients that will in the software that will be used to run those Roll-Ups. So, but anyway, the are one first and what can unify and what we can Use on there too. Old be like, figure it out. And yeah, we, but let's keep it in mind. I think it's pretty reasonable. Okay. 
* So the encoding part don't think we should stop here. It's just you will use the it follows this like logic. So, let's reuse as much of the existing JSON-RPC. See the will use the encoding that is used by json-rpc. It might be convenient to some places like that. Anyway, it's we have libraries. We have like intimidations kind of this. Yep, brought in series. So the minimal set of methods. It's been derived and debate extended and modified from what we had in the area in during the Renaissance. So let's move through all of them. 
* So there is the sample payload, which is the new name. I think a lot is more specific and more like sounds to what we have. So it's just Build a wall then returns back to the consensus client. So the addition here is from previous to be random, but it's yeah, it's just, went down makes to to be execution engine to embedded into the block. There will be a corresponding EIP to describe the specification on the execution are site about this. And what was it? It's recently is the current pace. There are comments and there is the like a kind of opposition. Well was exposed by Mikah. Sorry, Martin. 

**Martin**
* Yes, so regarding this method. There's some book payload, which I understand to be, basically, please collate the block for me in particular transactions. The way it works now in is one is that as soon as we have a new head we want to start mining immediately. So we start working on the on the empty block. Then while that is happening. The client actually trying to find the best transactions and for mev guess I mean, they're working on finding the best set of sequences of No, these bundles and they keep working on it and improving it from time to time updating the work package. And I'm thinking of having just one method called assemble payload might not really cover. Then it leads to the situation that the, the 2.0. Oh, sorry for using the term client calls, the consensus API. And It needs to make a subjective like this session. Can I spend 100 milliseconds on? It can spend 200 can spend two seconds on it. So I'm thinking it might be better to First tell the consensus layer. Here's the latest tip. And yes, you are the one who's I'm going to ask you to deliver a new block on top of this in a little while. Because I think we know that when we, when we have the new block that the next one 2.0. And then later on, WE the total client can could ask like could you give me the new payload now for the block that I already told you to start working on and something like that, maybe a bit more. I don't know. Some kind of interactiveness. I think might be 

**Speaker 04**
* If I understand correctly, you basically have 2.0 in time one, which is when the consensus client knows all the information that will go into the next block, but it's not the last point in time where it's reasonable to receive it and have another point in time later where it's like, okay now is the last chance to give me a block, right?

**Martin**
* I don't think that was quite what I meant. But I mean it's like if we're given a one-off chance to produce a block on top of some other random block. There's going to be like a start-up costs to just figure. I get the state in order and stuff. And then then there's this iterative process. What, what transaction should I fill it with? And if we want to, you know, if the most pressing issue, is that no, we need to deliver. For something now then obviously we need to we're going to deliver an empty set of transactions and rate. 

**Tim**
* So I guess what I'm thinking of is we have that set up the details. We can start building the final block until we have those four things right in the parent, hash timestamp, random, and the coinbase I'm going based, presumably might no longer advance, but like the timestamp and the parent hash, but perhaps, definitely don't know until Some short period of time, right before trying to build the block right,

**Danny**
* You know, because it's relative to the slot. It has to be fixed in the slot so functions lot and they're, you know, very know you're going sorry, but the parent hash, you know is going to be from the prior slot. So you have the block is coming in, attestations are coming in likely in the 4 to 6, second time frame of the prior slot, you know, certainly without In almost all cases that you're going to propose so you have that information. So my gut here is maybe you have the method that does an instantaneous, like get Block, which is like the very basic method. And then you have, you know, an alternative optional method where you can pretty much signal start work and then if you signaled start work before, you're going to get a better block when you call get block. And if you call get Block without having done that or prepare Block in, Then you're going to get my something more instantaneous or a client underneath, the hood could leverage that. They're always trying to make a block from the previous tip and not leverage that extra method, but the extra method maybe is an optimization. 

**Martin**
* Yeah and do the does the optimization really critical because I don't know as for me the strategy went because his clients just starts to Call the assemble payload in advance and it's pulling like several times and fix the latest block that it got from the execution quiet. When they when it is time to propose the blog series, using the alternative could be and 

**Danny**
* I think we had this conversation many months ago. The alternative could be once. I know I'm going to want to block. I just call a simple block over and over again and the execution engine knows that it should keep trying to Make a Better Block. Because you might call it again just makes a block. 

**Martin**
* So it makes it by upon request. So it's pretty simple. Practice Fusion required to decide, so it received the message. 

**Speaker 05**
* All resource intensive. Is it to try and build that optimal set of transactions? 

**Mikhail**
* So it there will always be improvements that can be made because depending pool is constantly changing. And so even, you know, in the last no second, you can get new transaction in the totally changes with the optimal block is. And so the optimal strategy for a block preparer or block Builder is to always try to Build a Better Block every opportunity you get. So, as fast as you can, you will better and better blocks. And as soon as long as transactions can even come in, which is basically always happens. There will always be some improvement. You can make

**Speaker 06**
* Just one more note. So Mikhail you mentioned that the it sounded like you meant that the this method could be called multiple times and get incrementally better. But that means well, how should the execution layer know that? Okay. I can stop. I can stop working on this now because sufficiently I return timestamp. 

**Mikhail**
* It may finish like work on the past, right? Yeah, let me finish like this work on, I mean, each request will have corresponding response if it's not requested, the block is not being built, right? 

**Speaker 06**
* But if it's if the working is scoped to the to the lifetime of the RPC request, then you're saying it should not continue working after the RPC request stands. I thought you meant it would, right. 

**Danny**
* So actually we have this conversation with Peter months ago and the, the answer that we had come up with then and I think there's two sufficient answers one- Is that you do an explicit prepare and then you get it when you want it. And the other is you call a symbol payload whenever you're ready and you get, you get a response, but timestamp is in fact in the future timestamp is the slot that you're going to propose at which is either immediately now or is, you know, four seconds, six seconds lead time because you know, you're about to go. So if you call it and there's six seconds lead time, you could on the execution layer know that timestamp. So the future and they're likely to call this again. And so that could be your signal to continue to do work and or not. So I think you can you can either leverage this method that way or you can do an explicit prepare and then and then I get.

**Speaker 06**
* Now I get what? What two alternatives we have. So one is the execution client responsible for building these blocks and storing them returning. The one that is latest pondered upon additional request, or remove this responsibility to the consensus clients, which will do the same. Actually, and I think, if we have this functionality already Implement in the execution client, it makes sense to keep it there and just provide this additional method. That was what was suggested by Martin, right? 

**Danny**
* Yeah. And Martin there's a desire. So there's a functionality is you kind of always be building the best block but because we now know if we're going to actually want the best block soon, then we might as well not always be building the best block and instead on demand be building the best block, right? Because you could just keep it as is and just always be working on a pending block, right? 

**Mikhail**
* Does it my correct in understanding the consensus client has a single point in time where they submit a single block? The network and they will never submit a second one,
 
 **Danny**
 * That correct. Correct for that slot for that. 

**Mikhail**
* All right. So there is at least the consensus is going nose. Like now is the last chance for a block right? The how much like latency is acceptable? Therefore that communication. So like between the time the consensus client says, okay, like I want to submit a block to the network right now. If it takes 200 milliseconds to actually get that response from execution engine. Is that okay? Or is that gonna be a problem? 

**Danny**
* There are much better off broadcasting immediately at the start of the slot rather than like starting to do their work at the start of the slot? 

**Mikhail**
* Okay, so the incentives are such that. That,

**Danny**
* You know, we haven't, we been hearing so you should be preparing and then just actually get it out on time. Gotta stand. That timestamp is,

**Speaker 07**
* I think, I think the, the prepare payload plus get payload, is a lot clearer because it means, you know, prepare it gets dark Billy, get payload. That is you just deliver what you have. And if you have just assemble payload, then it will be this, you know, right? Trying to measure how long have I spend time doing this. So should I believe it now and wait? Another 15 seconds problem for justice. 

**Danny**
* Yeah. I think I agree. It adds some statefulness here, but it as long as get payload can be operated without statefulness, you know without a previous prepare and it would just give you something very quickly. I think that's a reasonable trade off between statefulness and not.

**Speaker 08**
* Yeah, also one question here. How do you be like the client decide when to like stop building block or it's just constantly if it see one more transaction at all, like build yet another block and supporters 

**Danny**
as long as you have it done and get for the preparer than it would continue to try to build. Right? So the it's like up to one transaction and my right. I mean, to yeah, it should be relate to which shipped Excuse one transaction, that's all. But yeah, I don't know. I mean, yeah, that's how often the block is. The new version of The Block is being built. That's like my question. 

**Mikhail**
* In seconds. 

**Speaker 08**
* If we send this, prepare payload, how often will it block is being well, the new version of the block is being built by the execution plan. So, what is the condition here? Just started building a new one? 

**Danny**
* More of a modified one. If I understand correctly, 

**Speaker 08**
* Is this depends on your transaction arrives and the new block built at the like with a new set of transactions? Yes. 

**Tim**
  So it depends on the particular minor each. Well, my return strategies, I believe in Martin crackling wrong here that Geth, just every three seconds, builds a new one while there may. Well, prove work has been worked on like somewhere else. If you're running like any vegans or something, though. It's dependent. Again depends on. The particular minor but there are miners out there that are building constantly there. If this end of the new block stuff that they're working on, you actually getting full blocks from third parties that you then compare against the existing block you got from some third party. So I think from a design standpoint, we should assume the blocks are basically being constantly produced at maximal, velocity through some potentially distributed Network on the back end. So from the consensus client's perspective, you know, that, you know, on the other side of those API, By some amount of work is continuing to be done. Just until we call assemble, block and someone's working real hard back. There is what I recommend designing around. 

**Danny**
* Yeah, I think we should expect yes, 

**Speaker 08**
* Regardless, regardless of exactly right now, I think,

**Mikhail**
* Yeah, so that was the reason kind of a question that we might want to have like a new strategy in the perfect stake world. I mean, for building block, for updating the block. Okay. So in some sense doesn't actually care about any of those intermediate blocks, right? They only compare care about the very last one. All right, knock. They don't need to pull in between because they know exactly when they they want to get the final result or the best result. Right? 

**Speaker 08**
* I would say that like three seconds might be a good good one at 4 / 4 but yeah it with 13 seconds per blog but here we have much less like twice as less right? 

**Danny**
* And and maybe get their potentially not even following the same strategy. So I think you should expect kind of a lot of innovation on the layer and expect potentially continuous work. 

**Tim**
* Continuous and distributed and I think that's the key to keep in mind. Like the thing, you're talking to the execution plan, talking to May just validate the block at the end. Like they might not actually be building a block. They may have this work farmed out to third parties. 

**Speaker 09**
* Yeah, I suggest the coin base argument. Is it possible to have it only as a hint so validator can suggest the coinbase Box, the execution engine can decide to suggest different coinbase? Like, I'm thinking about all the scenarios where we don't have a matching one to one between the validator like beacon chain and the ethereum one operator. That's some scenarios where you have Market work. The builders are independent and can decide to have different strategy of coinbase and splitting, the cash flows of the transaction fees, and the, and the reward. 

**Speaker 08**
* Yeah, that's a good question. I think it should be an option for overriding the coinbase sent, or, like not doing the override and in the option in the command line interface for the execution client. So, which will explicitly say that the coinbase will be over reading, even though it sent over this method, it will be overridden by the following address around this load. So if you need this setup, I don't know if it's even appropriate override it. But probably in some cases. It is necessary to have this kind of function, 

**Danny**
* But I think it was I think his question was in the other direction because you're saying, there may be a default coinbase execution engine, and this will override, he was saying that the execution could say, I'm not going to listen to you and use my own, which I don't think should be. It should be designed in that scenario. And 

**Speaker 08**
* I would have thought that it was optional in both directions that it's reasonable for someone running an execution engine to say, actually not. I'm only in the coinbase. I want these rewards because I'm running the engine. I'm paying the costs for this. It's also reasonable for a beacon node to not know what the count when they should be. So it doesn't Supply one inning and expects the execution in general provide a default on strong on that.It seems to provide the flexibility that the color Sense. In, in terms of working through the use cases. 

**Mikhail**
* I think that in a world in which we have a proof of custody for the execution of the of that layer, that you essentially like the execution engine cannot be outsourced at that point and it needs to listen to what the directives are. And that if a market is dictating that if the market makers dictating that they can set their own coinbase and That you know that needs to be negotiated beforehand rather than not listen to that point. I just I don't think it's very clear but there's a lot of active research working on making sure that you can't Outsource execution like this. And that you actually as a validator need to execute even if somebody else is providing the payloads. And so I think I said to consider out the design. 

**Tim**
* I think that last thing you said is critical there. The we definitely To prevent people from Outsourcing execution clients, but I don't think that means we care about people, Outsourcing block production and the Coinbase base reward. May make total sense to go to the block producer and not to 

**Danny**
* I agree. But the the consensus layer needs to like the consensus client needs to have actually known that they're entering into a market like that because it cannot validate like if it thinks that it's providing a coinbase where fees are going to go to it. It, it won't validate. Whether that information was actually respected or not. So I think that it's It's very strange for the consensus layer to think. I'm gonna get these fees and then pass it along and then not have actually gotten it even if it's doing all the execution and stuff. Whereas I think if you were entering into a market where like that would be bypassed and your you should have configured your system in such a way. 

**Tim**
* So, the problem there is that means that we need to know. Like we definitely negoiate the coinbase before we produce a block where we don't produce the block. Like, if we're doing a market for Block production, the block producers. Coming from all over and you don't know what the coinbase is going to be. Until after the block is produced. Like we have an order there that's going to cause problems, I think. All right.

**Danny**
* So maybe coinbase should be a configuration. Is it requisite that Builders use coinbase to actually pay? Is there something there? Like you want to be able to make your generic your block generic? 

**Tim**
* To and I think there's some like, economic arguments of, you know, we want to encourage in theory. If you Eth to actually be used for payment for transaction fees and coinbase kind of helps nudge people in that direction. Doesn't enforce it. There's also like because there's a Coinbase opcode. It gives people submitting transactions a way to pay the block Builder and so it gives a inaudible trail of payments from the people are spending transactions, so you don't end up with like layer. Payments or some off my other channel payments for this stuff. Again. These aren't super strong argument. So I cannot deal breakers, but it just helps a transparency and stuff like that. 

**Speaker 08**
* So let me see. It's untenable for blog Builders to wait for prepare block before knowing coinbase address. Why is that the case? 

**Tim**
* So if the if you have someone summon a transaction and they want to bribe, the person who is constructing a block. They need to send money to coinbase Via either. Via gas phase detour via in a transaction. They do coin based on transfer request based out of Colorado. And so they don't know who Who's that's going to be if you have a market for Block Builder, so you might submit your transaction out to a dozen block Builders and they're all competing with each other to try to build the most profitable block for the block for the exclusion Kleiner. The rivers slot is upright, but they want, the people who are staying transactions to pay them because they're the ones who are need to be incentivized to sort their transactions appropriately. And so we it's possible to, you know, have other ways of paying those block Builders it, just you lose transparency, if you move it off to another layer.Can the consensus Ascension validate the coinbase? That's part of the blog header, right? 

**Speaker 08**
* Yeah, so they seem like they could they could validate it but I think probably the more important question is what are they going to do about it? They've got two choices. They can either give up all their rewards ditch the block or they can accept it and publish it and get the rewards on a beacon channel. Yeah. And go out the coinbase. They're going to accept it maybe publish and well EP Lord as well like a good walk with him to be long. Yeah, I see. 

**Speaker 09**
* I see the markets, were the exact the consensus engine, actually speaks to multiple execution engines, and allows them to select coinbase, and may have its own execution engine that it relies on as a last resort one. Who are it knows that the coinbase will be agreed on. So, and then you can selectively, which one is the most valuable for developing later. 

**Danny**
* I think that's Inflating this like block Builder, separation from like the validator actually executing things which in a world in which your proof of custody on execution layer. The validator is going to FX have to execute things. And so the fact that you got If and how you got a block from somebody and how it's paid for is kind of an independent thing. And I don't think that we should have this like super position where you're asking. You don't know if the coinbase is going to be set. Even though you're going to still need to execute, but are we assuming fighting multiple conversations this point? 

**Tim**
* Are we are assuming the consensus engine and the execution engine are trusted relationship? Are we assuming there and 

**Danny**
* I'm arguing that that will certainly be the case, because it is a security flaw for not to be. And there there's going to be a push in RnD to make that the case over time. That if you're running, if you're, if you're running a beacon node , no valid. You have to actually literally do the execution, even if you Outsource block, production or block building. 

**Tim**
* So in that case, I feel like we could just say that the coinbase is Say recommendation or it's like a just a place to put the coinbase. Then it's up to individual operators. to decide. Do I want my validator node to decide the coinbase or do I want the execution engine to aside the coinbase? And so this is basically a way to facilitate. It feels facilitate that communication but we don't have to like enforce that in any way we can just say and now it's up to individual operators decide which side decides the final coinbase. 
* Here's a mode for communicating that information between the two. In case you decide you want to go. The model where your consensus engine is the one that makes the suggestion. 

**Thomas**
* Right. I think that's reasonable their options here and there and it means that we like for the standard, it would mean that we will use like not must said the coinbase working but shoot or like, you know, with the notion that made the overridden. I don't know why the execution quiet 

**Danny**
* And Thomas, the what I'm arguing is that your execution engine might ask many Market sources for a valuable payload, but then your execution engine ultimately is going to run it. And it needs to be configured to decide if it was happy with the setting of the coin based or not rather than the consensus layer talking to ten different execution engines. You know, I think you have consensus later execution engine and then a market for execution engine. And and those are three different things rather than conflating. Execution engines as the market providers. 

**Thomas**
* Oh, yeah, I just used it as a shortcut so you can have an execution engine, which is like an aggregator of execution engines, but in the end architectural, it will still be talking to the consensus layer. And if or consensus layered will be transparent. However, if you remove this ability to upgrade the coinbase, then the aggregating execution, engine cannot really rely on multiple ones. It cannot even allow them to, to act independently upfront, and try to Different blocks and it actually what's cool about it is it's a bit more friendly for multiple solo, execution engine, validators Runners for solo validators. Smart be harder to extract the Mev. So to create very efficient execution engines, but they always want to make sure that they don't publish incorrect ones. So they will run the execution engine, that will verify everything invalidate, but it will be like a default low value 1. But for the actual block construction, very often, they will just redirect it to someone who can we can do that better because they can find them EV Nexus. All validators will have really, really limited ability to extract them EV,
* Which we see may end up being like 70% additional Revenue. So, if we don't allow these coinbase to be overwritten, obviously, Maybe it protects us all validators in a way that they for sure. We'll get the the transaction fees. But on the other hand, the block executors like the block. Builders may be less likely to provide any significant value because the debates the after the burning the coinbase from confuse, not that relevant. And in any limits light in the market, makes it much more rigid 

**Danny**
* Is coinbase overridden. Go on. 

**Thomas**
* I might be healthier to, to all of this to be overridden because it creates like, there's multiple execution engines that compete but also validate each other and creates a bit more healthy Market with probably gonna have liquids taking, you have be validators small MEV Runners and all like talking to different validators. Saying, this is what I can propose you, but I assume that you're running something to verify if I'm running the correct thing because otherwise, it might be not voted on at the desk. And this would be a big loss for you. I'd stop here on the coinbase discussion. 

**Speaker 10**
* So, Do we have like a legit case when we when the coinbase might be overridden by the execution client or not? 

**Thomas**
* I'm not seeing it yet because I think that the way that Mev is extracted as and in an open market doesn't need to override coinbase, but I'm also probably speaking beyond my understanding the point and I don't know if we're going to solve that this call.

**Speaker 10**
* What's the proof of custody takes up? Most of the cases? I can imagine it being useful? 

**Mikhail**
* I don't think it matters are still. There are still lots of cases, but I agree that we should probably move this to Discord. 

**Speaker 08**
* Yeah. Okay, so if we have the coinbase here, it implies that it will need to be like and it will need to be added to be by later client API as well. So this is to consider for because this is flyable implementers. So let's move forward. We have the these two methods 

**Tim**
* Really like quick. Sorry, Mikhail. I did we decide before you got to track for the coinbase. Tough to. We get decide on. Switching that first method up to a prepare and geth so then send you will call prepare and then okay. Sorry, Miss them. 

**Mikhail**
* Yeah, I think we have a rough consensus around this. Unless anyone I'm supposed to. That. Okay. So yeah, execute payroll and consensus related, which might have an alternative name. I personally don't like this much. This one much. So yeah, what, what's here was about this method. Obviously, we have the payload to execute and verify by the execution quiet. And we have a big block to be verified by the beacon note. By the consensus client, and it doesn't make any sense. And the payload, even if it's a valid one, but the consensus they beacon block is not valid. This payload, my must be discarded. This is why the second method method appears here. Like the other option would be, by sending the, by calling the Execute payroll. It's only after the consensus client has validated the beacon block and proves the proof that it's valid but it restricts the parallel parallel realizability that we want to Leverage The like meaning the parallel processing of the execution payload And the beacon block to save us some time
* Hence. We need these two methods and yeah, the reasons like the book resistant flow, the sequence, diagrams that illustrates how two different cases of how these two methods are combined. It also implies the cash in on the execution client side, which is mentioned like like in the bottom of this document, like the execution phase, We'll have to cash have storage in some ways until the consensus validated message received and it can be easily discarded or persisted for like, I don't think any specific thing to mention here is instead of base like that. This consensus validated methods maps on the group's a consensus. Well, if you Grant from the EIP  3675. And yeah, there is the number enumeration of it just returns valid or invalid. I don't think I don't know if known is valuable here. Probably not and same here. It's just propagates that this D execution. The consensus rule set has been validated and it either valid or invalid because that's the these two methods. Let me know. Of these two methods. Does anybody have any questions here? It's pretty straightforward. 

**Speaker 10**
* Just make sure I understand. So the execute payload will come in when the censensus engine is saying, hey, here's a block. 

**Mikhail**
* Yeah, let's go here. 

**Speaker 10**
Yes. block arrives, the execution process and and consensus client starts to validate the beacon Block in the meantime when it's validated. It sends consensus validated. So then the execution slide response, and after all these done the block, maybe persisted or discs or should be discarded. It is not the case. When the execution it won't be consensus related comes after the the payload is being has been validated, which is I don't think it's like potentially like the freaking case probably when the execution  is completely empty. No transactions. That might happen. Anyway, it should be considered that.

**Speaker 10**
* Well, what does an execution client need to do to recognize that the consensus validated will never come? 

**Mikhail**
* Good question. You mean that when it should like, dropped the case for?

**Speaker 10**
* Yeah, at some point. The so execution client receives, executing payload. It starts building and block at some point. I'm assuming it should throw that box away, if it never receives a follow-up, consensus validated is that, is that right? Or should hold onto it, forever rides with my way and for finalized walk. 

**Mikhail**
* You can't and drop the cash. Yeah, probably not. Actually if the yeah, if the payload is behind the checkpoint that has been finalized and the fog that has been finalized. It should drop, it should clear the cache. So it should bring the cash in his case, 

**Speaker 10**
* Okay, so hold box until finalization. And then once violation occurs, clear, everything that's not in the finalized history, but is prior to it in terms of slot numbers.

**Mikhail**
* Right, and there is another possible case. When it could be cleared up if the consensus client was out. But yeah, that's that's related to the recovery of the failures and there will be an explicit place. We're at the institution. Quite understand that consensus find has been out. If we follow the proposal in this document. And in this case, it can also release to cash. Like what was Cash before doesn't matter anymore because consensus trees, right? Just started and will drop like new information, like fresh information. So that's two possible cases for flashing. This cash for a drop in skin. Okay. Yeah, we have like 10 minutes. Anyway, 

# [Fork Choice update](https://youtu.be/il0nha1HSiE?t=2626)
**Mikhail** 
* Yeah, the fork Choice, updated method. It unifies the two previous methods that we have on the folk Choice State updates, which is finalized block and set had. The reason behind this to behind this unification. Is that the folk Choice information. Namely, the finalized Talk and the head must be updated. Atomically must be applied atomically to the bookstore, to avoid the corner case, which is rare, but it's, it can appear, and it will allaged. The corner case is about the situation. When the like the new finalized block will be on a different Fork than the previous finalized block,
* The message. To finalize block arrives, do the execution client, and it should update this finalized finalized, checkpoint, and it will update it. But, after this update, the head and the finalized checkpoint will be on different branches, which is, which is the lack of consistency between the two and the, yeah, of course, set had that we want the date. They had to the new duties, new Will arrive like, in a few milliseconds. But anyway, the world like point of there will be a short period of time when these two to two blocks to check too. Two things are inconsistent. So that's why it needs to be. Like the atomic update will be had and finalized block. 

**Danny**
* So, the reason I just want to note that given the discussions led by Don grid and maybe the definition of what is unsafe pads. The most eager had than safe had which option would map to the same thing, maybe with a little bit of delay. And then also finalized. I think that this would be the method where we'd actually want to insert that information. Those three things would always be on the same chain, but if you want to expose that additional information? The execution engine for the user apis that we discussed. The this is where we were inserted.

**Speaker 10** 
* I would not propagate this information to the execution client or the rather would requested like from two sources. This is just my opinion. We've been discussing committing this curve. 

**Mikhail** 
* Just the head block hash in this current draft, that would be equivalent to what we've been talking about as the unsafe head. Correct?

**Speaker 10** 
* Yes. Oh, yeah. Yeah. Yeah, it will be unsafe and you're saying, 

**Danny**
* you'd want to route as a proxy through to the second node rather than giving the information, right?. 

**Speaker 10** 
* So, because we might want to or might want to expose some other information consensus layer to the users API in the future, so it might be more, it should be more flexible. And if we propagate this This all the information that the user needs to the user may request from the Json RPC to the execution client. This kind of like every every time we add something new to the from from the consensus, where to the users API, we will have to update both the consensus clients and the execution. 

**Danny**
* Yeah, I'd argue not putting most of the consensus layer stuff into the user API and for them to be separate. And if you actually do want to leverage stuff from the beacon chain run web3.beacon. Beacon and ask for it directly. I think this is an exceptional case because this is your maps to them understanding the head of the execution chain essentially and that it's relatively Limited in the information in that the you can change is good at calculating it, but it might as well hand it off to the execution engine because it's relevant to it, but I Obviously have the I think we could debate this.

**Marius**
* Yeah. Yeah, I think. Yeah, I see. I see what I think the important part here is for backwards compatibility. Unless we want the thing that everybody currently calls latest to be the unsafe head. We need to make sure that execution engine is aware of what the safe head is. And I think it sounds like most of us agree that safehead is the reasonable replacement for latest. And so the execution engine needs to know that in order to not break everything, 

**Danny**
* Then what we don't normally agree on yet is whether The API proxies through the beacon chain or if so that you can extend Beacon chain functionality into the user API more easily. Or if this is kind of an isolated case and you just pass the additional information and don't proxy the API through say, even if we did proxy, 

**Marius**
* I think we still need to tell the execution engine, what the safe head is. Regardless of the decision of proxy or not proxy, that your changing needs to know safehead so it can return something when users ask for latest.

**Danny**
* Marius. Safe head is not finalized that is under you know, if you if you assume the network is synchronous and you see sufficient applications come in, you can quickly know that it is very, very unlikely to be reordered and that that's kind of what we're calling. And that but that you could also be in a position where the head of your for choice is not had sufficient information and come in, and it's still the head but it's not, you can't make like as concrete. Probabilistic we go to the decision. 

**Speaker 11**
* Yeah, so we we currently have the model that everything not finalized is unsafe for us. So we're not like I agree that it might be, might be, might be good to, to, publish a safe head to the user for the user of facing apis. But internally, we will not break. I'd do anything with it and I, 

**Danny**
* Yeah, I wouldn't suggest you. The only thing that I would do with it is potentially how you router to user apis. I don't think that it has. Yeah, sure with how you handle your data model or anything like that. 

**Mikhail** 
* Yeah, for context. This is when a user through the json-rpc API talking to an execution clients, using Legacy apis only. So, they have not upgrade anything for the merge. They say, give me the latest block, the Executioner. Needs to return them something. And we need to decide is that the unsafe head is at the safe head or is that finalized safe head? I think is the best option here because it's very close to the tip, but it's also very safe. And where is finalized is potentially pretty old and we don't want to give user block. That's, you know, several minutes old and unsafe is unnecessarily risky to the user.

**Speaker 11**
* Okay, so yeah, back through these like I do see while you in, if we say that, we propagate all this information to the folk Choice like this informations information to the execution client sends, you will not get back to these pattern for any other data. So that might be valuable and it might be reasonable to do. Once and also this, this unification requires the corresponding, updating the 3675, because there are two like events that this method maps on.

**Mikhail** 
* Yep. Yeah, we have like four minutes and it was we're going to talk about the scene. But I think we have not, we have not enough time for this. So I propose to reach out the Geth team in this Discord to talk about this in. Go find the requirements of the same process on the, on the API. And what do you think about making a call? What is the better time for? The next goal is, like, one week or Weeks from from from this.

**Speaker 12**
* So we're currently working on our part of this Spec of what we think about the sync, which guarantees we can provide and Felix is unfortunate not here today, but he is currently writing down a new document with basically everything about about the sync. So I think, in one week, we should be finished. If you you all have, like, time there. I don't know. 

**Mikhail** 
* Yeah, I would make a call like one week after if I like using the same time slot. So any other opinions on that? 

**Tim**
* I mean we can use like half of all core devs or two-thirds of all core devs to discuss the same for the merge like we and its basic. It's not exactly one week and it's not exactly the same time but it might be a good enough place. 

**Mikhail** 
* If we can do this that the awesome sure. Yeah, it's hard to see what's higher priority.

**Tim**
* Yeah, so I guess yeah just in terms of next steps. Like as soon as they get team has like a sync right up just posted in the El Cortez agenda and we'll make sure to cover that first on the call next week. 

**Mikhail** 
* Yep, and whatever time will tell, whatever time periods. It's really awkward to have. So we'll have to go through. We'll just try to do as much as we can. Like, I mean just follow this discussion there. Okay, I'm stop sharing. Thanks everyone for coming. I was like, expecting, not reaching the end of the document today. Thank you so much. See you later. Exactly.


-------------------------------------------
## Attendees
* Mikhail Kalinin
* Lukasz Rozmej  
* Pooja | ECH
* Gary Schulte
* Micah Zoltu  
* Dustin Brody
* Terence
* Danny
* Jacek Sieka
* Paul Hauner
* Alex stokes  
* Vitalik
* Dankrad Feist Kevaundray Wedderburn
* DCinvestor
* Ben Edgington 
* Protolambda 
* Sajida Zouarhi 
* Hsiao-Wei Wang
* Karim T
* Kristof Gazso 
* Adrian Sutton 
* Bhargavasomu 
* Tim Beiko 
* Trenton Van Epps  
* Mamy  
* Tomasz Stanczak 
* Ansgar Dietrichs
-------------------------------------------


## Zoom chat:
09:00:46 From  MariusVanDerWijden  to  Everyone:
  Yes  
09:00:53 From  thegostep  to  Everyone:
  tty  
09:01:02 From  MariusVanDerWijden  to  Everyone:
  Can you paste the link to the md in chat?  
09:01:08 From  lightclient  to  Everyone:
  “gm”  
09:01:17 From  Ben Edgington  to  Everyone:
  https://hackmd.io/@n0ble/consensus_api_design_space  
09:01:27 From  Mikhail Kalinin  to  Everyone:
  The call will be recorded and uploaded to youtube  
09:01:37 From  Mikhail Kalinin  to  Everyone:
  oops, it’s being recorded already :))  
09:05:16 From  Pooja | ECH  to  Everyone:
  my mic is not working it seems.  
09:07:17 From  Pooja | ECH  to  Micah Zoltu(Direct Message):
  it wasn't inappropriate and should have been fine Micah  
09:08:14 From  Micah Zoltu  to  Pooja | ECH(Direct Message):
  Oh, why did you cut it then?  I assumed because it was determined to be "too inappropriate" for a public call?  
09:08:17 From  Pooja | ECH  to  Micah Zoltu(Direct Message):
  I just removed so people don't start leaving useless comments failing to understand the humor we were having.  
09:08:42 From  Micah Zoltu  to  Pooja | ECH(Direct Message):
  Ah, I see.  
09:08:58 From  Pooja | ECH  to  Micah Zoltu(Direct Message):
  I guess, I shouldn't have removed that.  
09:09:05 From  Pooja | ECH  to  Micah Zoltu(Direct Message):
  would have been fine....  
09:09:43 From  Pooja | ECH  to  Micah Zoltu(Direct Message):
  generally we don't receive any thing for good we discuss, just people love to point what went wrong.  
09:09:49 From  Mamy Ratsimbazafy  to  Everyone:
  https://hackmd.io/@n0ble/consensus_api_design_space  
09:11:47 From  Trenton Van Epps  to  Everyone:
  gary you are unmuted  
09:11:56 From  Gary Schulte  to  Everyone:
  Thx sorry  
09:16:47 From  thegostep  to  Everyone:
  assemblePayload should be called at the latest possible point in time and should be able to have a pending block ready to propose  
09:17:35 From  Gary Schulte  to  Everyone:
  prepareBlock  
09:19:21 From  thegostep  to  Everyone:
  the optimal block is likely to be built outside the node  
09:23:24 From  MariusVanDerWijden  to  Everyone:
  We're trying to deprecate the notion of pendingBlock since it is not reliable in post-mev world  
09:24:30 From  thegostep  to  Everyone:
  I would suggest only having a single prepare and a single assemble call per block instead of a polling approach  
09:25:50 From  Tomasz Stańczak  to  Everyone:
  what is a 'post-mev' world? @Marius?  
09:25:54 From  thegostep  to  Everyone:
  it depends - mev-geth is whenever it receives a better block construction  
09:26:56 From  Micah Zoltu  to  Everyone:
  I also like prepare => get  
09:30:16 From  Tomasz Stańczak  to  Everyone:
  I agree with Adrian  
09:30:29 From  Tomasz Stańczak  to  Everyone:
  it gives great flexibility for markets  
09:32:00 From  thegostep  to  Everyone:
  it's untenable for block builders to wait for "prepareBlock" before knowing coinbase address  
09:32:17 From  Tomasz Stańczak  to  Everyone:
  I expect the consensus layer to be able to allow or not the coinbase change  
09:32:31 From  Tomasz Stańczak  to  Everyone:
  so validator will always knowingly accept or reject the overwrite  
09:34:32 From  Tomasz Stańczak  to  Everyone:
  agreed with Micah  
09:35:39 From  Martin Holst Swende  to  Everyone:
  I'm going to need to drop off in 5 minutes, will try to catch up with the discussion later  
09:35:54 From  Tim Beiko  to  Everyone:
  It will be on Youtube, Martin :-)  
09:36:09 From  Tim Beiko  to  Everyone:
  Will post the link in the Github issue for the call/on discord  
09:39:48 From  thegostep  to  Everyone:
  imo there is benefit for coinbase to be static and publicly tied to validator (e.g. withdrawal address)  
09:41:25 From  Mikhail Kalinin  to  Everyone:
  There is a 0x02 proposal in this direction, right?  
09:42:15 From  Rai (ratan.sur@consensys.net)  to  Everyone:
  I feel like I'm missing something obvious. Why would I want to use a third-party created block that takes all the transaction fees as opposed to a suboptimal block where I get all the fees?  
09:42:30 From  Tomasz Stańczak  to  Everyone:
  prepare, get sounds good  
09:42:31 From  Rai (ratan.sur@consensys.net)  to  Everyone:
  suboptimal block (of my own creation)  
09:42:36 From  Gary Schulte  to  Everyone:
  Alternative  payment backchannel  
09:42:51 From  MariusVanDerWijden  to  Everyone:
  I would also think the basic spec should have the coinbase static. If mev enabled clients would want to have this in the future, it can be changed after the fact  
09:43:06 From  Adrian Sutton  to  Everyone:
  Worth nothing that execution engines need to be able to deal with getting a prepare and then having the get never arrive (eg consensus client crashed)  
09:43:11 From  danny  to  Everyone:
  I also don’t think an MEV market needs to rely on overriding COINBASE to do the extraction for the builder. and often, builders even user COINBASE to pay the block producer  
09:44:02 From  Micah Zoltu  to  Everyone:
  We could have two addresses in the block... block builder address and validator address.  
09:44:06 From  Tomasz Stańczak  to  Everyone:
  I am talking about a market where block builder, execution engine and validator are three different entities  
09:44:13 From  Micah Zoltu  to  Everyone:
  That way we can appropriately target payments in an auditable way to the appropriate parties.  
09:44:18 From  Micah Zoltu  to  Everyone:
  Rather than conflating them into a single address.  
09:45:25 From  Micah Zoltu  to  Everyone:
  I like just VALID|INVALID (remove KNOWN).  
09:45:25 From  Ben Edgington  to  Everyone:
  If it's useful and not in the API, then it's just going to be done out-of-band (separate non-standard API, whatever). So might as well go in the API.  
09:45:36 From  Tomasz Stańczak  to  Everyone:
  validator rewards, tx fees and MEV payments are three different types of cashflows then can be split to create better markets that distribute risks (but I just wanted to suggest it for longer discussion / make you aware that it may be useful)  
09:46:27 From  Alex Stokes  to  Everyone:
  If it's useful and not in the API, then it's just going to be done out-of-band (separate non-standard API, whatever). So might as well go in the API.  
09:46:33 From  Alex Stokes  to  Everyone:
  but this may be an out-of-band thing  
09:46:36 From  danny  to  Everyone:
  in the block builder separation, the block producer needs to know that they are getting paid. the most obvious way to do so is to route payments to COINBASE and for the builder to get payment in a path constructed by them. and so even in this separation, I’m unsure what value is gotten by the builder altering COINBASE  
09:46:53 From  Alex Stokes  to  Everyone:
  establish the extra relationships outside the scope of this API, focus on just consensus/security via the concerns of this API  
09:47:28 From  thegostep  to  Everyone:
  I tend to agree with your evaluation @danny  
09:48:37 From  thegostep  to  Everyone:
  though I would suggest a longer discussion on this, lots of moving parts / potential marketplace design are tied to how coinbase is set  
09:49:38 From  Tim Beiko  to  Everyone:
  @thegostep, agreed, and IMO it is probably worth having another document which details the tradeoffs and use cases  
09:50:11 From  thegostep  to  Everyone:
  i'll try to draft my thoughts on this before our next discussion  
09:53:58 From  MariusVanDerWijden  to  Everyone:
  Safe head is not finalized block right?  
09:54:32 From  Mikhail Kalinin  to  Everyone:
  it is the most recent confirmed (got 2/3 votes) block from the canonical chain  
09:54:46 From  thegostep  to  Everyone:
  "safe" may cause a lot of confusion  
09:55:44 From  danny  to  Everyone:
  I need to run. consensus-layer call in 5 minutes  
09:55:51 From  Mikhail Kalinin  to  Everyone:
  sure  
09:55:52 From  danny  to  Everyone:
  I’m okay with picking a different name for “safe” heh  
09:57:10 From  Tim Beiko  to  Everyone:
  Should we schedule another one of these next week?  
09:58:08 From  Alex Stokes  to  Everyone:
  1 wk from now is the prater fork FYI  
09:59:10 From  Micah Zoltu  to  Everyone:
  Unfortunately for you all, I will show up no matter when you schedule it.  😈  
09:59:10 From  Tim Beiko  to  Everyone:
  https://github.com/ethereum/pm/issues/379  


