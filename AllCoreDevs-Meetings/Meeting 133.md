# ACD 133 Meeting Notes

### Date/Time: March 4, 2022, 14:00 UTC

### Duration: 90 minutes

### [Recording](https://youtu.be/ZKPElqIfteU)

### [Agenda](https://github.com/ethereum/pm/issues/481)

### Moderator: Tim Beiko

### Notes: George Hervey

## Decisions Made

| Decision Item | Description | Video Ref |
| --- | --- | --- |
| 133.1 | Change Latest to safe head by default | [30:43](https://youtu.be/ZKPElqIfteU?t=1843) |
| 133.2 | Put together metaspec and proposal for engine API | [1:00:00](https://youtu.be/ZKPElqIfteU?t=3600) |
| 133.3 | Review and engage EIP-4844 transaction type in Sharding channel in Discord | [1:21:42](https://youtu.be/ZKPElqIfteU?t=4902) |
| 133.4 | Not include EIP-3978 in Shanghai due to verkle tree update and high complexity | [1:36:48](https://youtu.be/ZKPElqIfteU?t=5808) |

## Merge Updates

**Tim Beiko:** 
Okay. Good morning, everyone. Welcome. To All Core Devs number 133. We, have a couple of things today, so obviously, a lot of time discussing Kiln and the latest merge, updates. Then we have some updates on a bunch of EIPS we had previously we discussed for Shanghai. So, one around Beacon, chain withdrawals, which is actually a new EIP with a different approach, an update on the prototyping that happened for the Shard Blob transactions, and then finally an update on EIP. we discussed this a while back, but, the idea of having the Coinbase address be warm rather than cold with regards to gas costs. Then finally, we have, I'm sorry, I'm blanking on the name right now. Somebody from 1Inch apologies here, to talk about another EIP which reprices, reverted upcodes. Oh, Anton. Yes, sorry about that. So I'm down to talk about your prices reverted operations. and the last thing I'll give a quick shout out now, but we, had been discussing how to call the execution layer client release for the merge. So, there's already a name for the consensus layer ones next week at the same time as this call for 1400 UTC on Friday. We'll have a breakout room to discuss that. So if you have strong opinions about namings, this is where you should show up.

### Kiln Updates

**Tim Beiko:** 
Cool. So for Kiln, Marius, I saw you were in the discord trying every possible client combination. Do you want to give a quick update and then we can probably get others to chime in?

**MariusVanDerWijden:** 
Yes, sure. so, I've been trying to set up a, document for all the different clients the same way we did with Kinsugi, so that once we launch Kiln, the community can come together and run. Some of them haven't had, proper Auth support, yet, or they don't use Auth for, the normal operations, that are not like, the normal calls that are not part of the engine API spec. And so I think that's something that we need to discuss whether we want, for example, the east calls on, the engine API Port on the authenticated Port, to also require, authentication. And I would prefer that because that's way easier to implement for us. or if we are going the route that some of the consensus layer clients chose to do the calls for the  ETH calls without authentication and only do the engine API calls with authentication. So maybe Mikhail has some thoughts about this.

**Danny:** 
My opinion is that anything on that Port should be authenticated, and I think that's probably how it's specified. And if it's not, then it should be clarified.

**Mikhail Kalinin:** 
Yeah, I agree. It's like the authentication is for the endpoint point. Has two namespaces. Current base, choose engine and ETH. Subset of ETH.

**Justin Florentine:** 
Yeah, this is based on here. That's how exactly how we read the spec and that's how it's been implemented.

**MariusVanDerWijden:** 
Same for Nethermind.

**Danny:** 
Yeah, we can circle back on that, make sure there's any clarifying text that needs to be there, and just also coordinate with the other side.

**MariusVanDerWijden:** 
That's good. Okay. Yeah and we also plan to maybe not run the unauthenticated, endpoints. we might choose not to run the unauthenticated endpoints, and that would break clients that don't have this, otherwise, it looks pretty good. Teku and Lighthouse already support the, authentication out of the box. Load Star supports authentication for the engine calls, and, I'm not 100% sure about Nimbus and Prism. There seems to be some issues with the authentication. That's it. Cool.

**Tim Beiko:** 
Thanks for sharing. Anyone else have updates on Kiln?

**Danny:** 
Maybe Pari on DevNet Five?

**Pari:** 
Yes sure. So we did launch Merge DevNet 5 yesterday. The, Merge fork Epoch has been hit earlier today, and we already found one issue with the client team that's looking into it, but TTD hasn't been hit yet. Most, likely it would take another two or three days. And latest on Monday. We're just going to run a bunch more miners to hit the TTD. Tooling links are up. I'll post, a link on the chat, and we should have more information on Kiln sometime next week.

**Tim Beiko:** 
Yeah, and I guess unrelated to Kiln, one thing to note is we'll do an announcement on the EF blog like we did with Kintsugi, kind of explain to the community what it is and whatnot we'll, link Meredith's Doc, which has kind of the pair wise instructions, between clients. But if client teams want to have a one pager or short bit of documentation about how, to kind of get Kiln running on, their client, that's really helpful as well. And I'll reach out and we can include those for the teams that, have it.

**MariusVanDerWijden:** 
My document will be extremely brief, so I think, it's more for, like, really technical people, and it would be nice to have longer, explanations, for people that are not that into, running stuff on the CLI and stuff. So if you're out there and you're, interested in doing something for the Merge and helping us out, then you can just create a blog post with your favorite combination, and explain, to the average user how they can set up a note on Kiln. That would be really great.

**Tim Beiko:** 
Yeah, very good point. And, yeah, I guess just to kind of check in with the other teams, is everyone roughly on track for being, ready to go on a more public Kiln version next week?

**Marek Moraczynski:** 
From there at my site, we are ready without, we tested it with one sale client. We are likely going  to launch the first node with Auth on the Merge DevNet 5 probably on Monday.

**Andrew Ashikhmin:** 
Well, I'm still working on fixing the tests, in hive. I've just realized that there are still things to be done in our code base, so we'll try to make it, but it's a bit uncertain.

**Tim Beiko:** 
Got it.

**Gary Schulte:** 
Basically it was on track for A Kiln release with or without auth next week.

**Tim Beiko:** 
Cool. Great. Anything else on Kiln or just the merge devnets that people wanted to discuss?

**Mikhail Kalinin:** 
We actually have a small spec update. Is it okay to share it now?

**Tim Beiko:** 
Of course, yeah.

**Mikhail Kalinin:** 
Okay, cool. So, we have several PRs to the engine API. They are mostly clarification PRs. One of them sets quality of service to Exchange transition configuration method. And this quotatures requires a bit of attention from implementation side. Also, we have a slight update, to the optimistic syncs back. Really slight one. All these updates are backwards compatible with V2 version and what we are about to do is to release all of this under V2.1 version. So it should be pretty much okay to have a DevNet or a test net with V2 and then clients will be able to upgrade to V2.1 once each client is ready. So that's like the plan. And I guess we will have this V2.1 release early next week. That's the update.

**Tim Beiko:** 
Is it possible to have a kind of very clear separation of V2 and V2.1 just in terms of the meta specs? Because we're probably going to link V2 if not linking it directly, it'll be like sub linked somewhere in the Kiln blog post. So just to make sure that that link stays pointing towards V2 and V2.1 is like.. 

**Danny:** 
Why not just link to V2.1 considering that these are all afterwards compatible and don't change anything for end users?

**Tim Beiko:** 
I don't have a strong opinion. My reason is just like you don't want people to look at the spec and then look at the clients and there's a mismatch, but I don't have a strong opinion there.

**Mikhail Kalinin:** 
Yeah, I think it will be just released like as a regular bump of Kiln version or Kintsugi version, but just V2.1 to reflect that it's backward compatible. Marius, I hear your question and there will be like a few PRS in engine API, a couple of them clarifying things and polishing them. One, is set in the quality of service which actually on the Exchange transition configuration method, which actually for EL, from implementation side, it means that EL should fire message in the log if CL hasn't triggered this method for 60 seconds or for 120 seconds. So this kind of stuff. So it's like to be sure that CL is that EL is driven by some CL, that's it basically for EL side.

**Danny:** 
I was saying on the optimistic sync side there's a case in which you can be a little bit more liberal in what you're allowed to import and so it's kind of expansive in that and so the other does not reduce the spec.

**Mikhail Kalinin:** 
Yeah, good question. We don't have spec for finalized, latest and unsafe yet. It's actually a slight change to the execution APIs. It's a matter, of adding like these values, to the enum that is already there in the spec, but in terms of implementation might be much more invasive.

**MariusVanDerWijden:** 
Yeah, and I think that's a pretty big change. It might be a big change on the user side. So I would vote for doing this spec pretty quickly so that we can implement it and then have the service providers and everyone testing this.

**Danny:** 
To be clear, the user can do nothing because Latest is still there, which is the addition of the other two. But yeah, if they want to actually leverage the new functionality they need to practice.

**Mikhail Kalinin:** 
Yeah, the question is do we want to have this for Kiln? For the record, it can be implemented by Kiln. testnet can be launched and then this feature is implemented and deployed. They're like not a blocker to launch.

**Danny:** 
Yeah, I think we should get it written down and I think that people can roll it out and that should definitely be out by the public testnets. Not Kiln, but the existing public testnets.

**Mikhail Kalinin:** 
Yeah, I guess then if we want to have this for public testnets, we would like also to test it on Kiln probably at the end of this.

**Tim Beiko:** 
It seems like the biggest. So actually doing the JSON-RPC spec is not like the biggest thing. I think the biggest challenge was actually getting the safe head exposed and kind of passed through the execution layer and then kind, of dealing with that in the execution layer. I guess that probably is something that you don't want to hold Kiln on.

**Danny:** 
Yeah. So both of these values are paths already. It's a matter of the execution layer than kind of tracking and tagging them as blocks and states that can be retrieved by those keywords.

**MariusVanDerWijden:** 
Like the big problem that I faced when I started to implementing, I started implementing, finalized that, was pretty easy. The issue is that, Latest currently just uses the internal blockchain object and so we will return the unsafe head. And I think having Latest as the unsafe makes more sense because you want to build on top of Latest.

**Micah Zoltu:** 
The vast majority of people who are using JSON-RPC though are not building blocks. They are dapp developers or integrators and whatnot who very much do not want Latest. Yeah, but you want unsafe head when they are on Latest.

**MariusVanDerWijden:** 
But you want to create your transactions on top of Latest.

**Micah Zoltu:** 
I don't think so. I think you want the safe head. I think you're correct that you want your transactions to be executed against. When it comes to gas pricing, for example, Latest or Unsafe is going to give you a more correct gas pricing however, for determining what the state of the universe is like has a transaction final or is a transaction mind, so to speak. I think safe head is what basically every user wants. And so ideally, dapps will switch to using Safe and unsafe appropriately. And so the question is what is the default that most people are going to want most of the time? I think Safe is that.

**Danny:** 
Yeah, I guess I'm a bit mixed on this. I know we hashed this out months ago, but the proof of work block in the first 2nd is also something like unsafe in that it does get uncled. It's, not rare for it to get uncled. So like the Latest does not really imply that it's going, to be there forever. Whereas if we had a new keyword that was Safe, that then now is new and allows me to make like firmer decisions than block confirmations. One block confirmation and allows me to make not quite as firm decision as finalists. 

**Dankrad Feist:** 
As a counterpoint, in proof of work, there's no balancing. So there isn't the danger that someone intentionally creates a block that is likely to be reorged.

**Danny:** 
I agree. With the intention of a block. that might be. I don't care about the intention. I just know that if I get ahead and proof of work, it might be uncles. But if it's.

**Mikhail Kalinin:** 
I think it depends mostly on the general use case for which people use the Latest. And can it be distinguished for some use cases where unsafe is, the one thing that people want to use easily, juggled in dapp and services that use JSON-RPC.

**Tim Beiko:** 
Is it easier to implement Safe as a separate endpoint than it is to rewire Latest?

**Danny:** 
Probably. I think what Mario is saying is Latest is Latest and it's used in this very particular way for certain things. Obviously it's used also to read the state of the world. but if you just add Safe and unsafe and kind of say hey, stop using Latest and be more particular about Safe and unsafe in the future, that might be a path.

**Tim Beiko:** 
Right. Because it feels like if we do want... 

**Dankrad Feist:** 
Sorry, I'm a bit confused there because we are adding the new endpoint anyway, that's already it. I don't see the argument.

**Danny:** 
No, the issue here is that whether you're, wiring Latest to be the tip of the chain as it is, or wiring it to be this thing that might lag.

**Dankrad Feist:** 
But I mean also another counter point to the earlier argument that Latest is what you want to build the transaction on. Well, if you have a transaction that can only be built on Latest, that is like, that is also not safe anyway, right? Like any transaction that assumes one particular state can simply fail to encounter that state when it's actually included.

**MariusVanDerWijden:** 
But you want to build the nons on top of.

**Micah Zoltu:** 
I don't think transaction nons are a big deal. Basically,  everyone's wallets handle it. The wallets handle the nons, and they track them internally. They don't use the node for that, so I'm not to worry about that particular aspect.

**MariusVanDerWijden:** 
I think it depends a bit on whether you want to read or write the blockchain. For writing the blockchain calls on like, wiring latest to unsafe might be better. And for reading the blockchain, safe to, save might be better. Sorry, Latest, to save, might be better. I remember that it used to be that we had, the most used call was ETH Call, ETH estimate gas, stuff.

**Micah Zoltu:** 
I think it depends on what type of user you are. If you are a MEV miner, for example, you're definitely going to want unsafe head, but I'm not, too worried about default for those people. Those people can very easily change their code to use unsafe if that's what they want. And what I'm more worried about is the average user who is not an Ethereum expert barely understands what gas is, or probably doesn't understand what gas is. They're just trying to use some dapp or buy an NFT or whatever. And when it says their transaction has bind, like they're completed, like they get that little TADA thing at the end of their dapp that says, "Hey, you got your NFT or whatever it is you're trying to do is done now." I want that done to really mean done. And so for these users who are using dapps today, they're using Latest because the only option and that done doesn't actually mean done, because there's reorg potential. But luckily, if we reorg, probably your transactional still making, but maybe not, depending on what you're doing. 

And so if we switch all those users over to Safe, done means done in almost all scenarios, right? Except for the very weird scenario where we actually have a safe head reorg, which can happen, but rarely will. Those users won't run into problems, and those are the ones that I think we should be optimizing defaults for, not the power users who want to play at the very edge, of the chain. And they're worried about doing these uniswap transactions or whatever that needs to go in at the exact moment in time that the price moves or whatever. I think we should focus more on those users that don't know what Ethereum is, barely know what they're doing. They installed MetaMask, and that's kind of it.

**Tim Beiko:** 
And I guess one data point I can add in favor of that is it still takes a long time for even very popular apps to have proper 1559 support. A lot of times I'll still use a random application and the web3 or Ethers version that they're using basically populates, your transaction as a legacy transaction, even though it's been like nine months since 1559 is live. So I think, that you, if we can switch everyone by default, there's a large portion of applications that will provide a better UX that otherwise just might not.

I guess the one thing I'd be curious to just understand it better is the engineering, cost. Like, is it ten times harder to rewire Latest than it is to just have Safe as a separate, flag and Latest, kind of map the unsafe? yeah, that seems to also be important.

**Micah Zoltu:** 
I can't speak for all of the client teams obviously, but from the client code bases I have with that generally JSON, RPC receives a message over JSON RPC. And when it's parsing those variables, you can do that aliasing right there. and it shouldn't matter what you're alisting too.

**Danny:** 
Yeah, I guess it's only Latest is also double used for things deep in the code base that aren't really related to JSON RPC.

**Micah Zoltu:** 
Yeah. So I guess from a naming perspective within a given client code base, it's certainly possible that a client may be using the word Latest everywhere in their code base to refer to the unsafe head. And then it's kind of weird to have the JSON RPC have some aliasing to Safehead. I'm, not terribly worried about that because you can do the aliasing like, right as you enter, basically at the very edge, and so it shouldn't cause problem in your, code base overall. But again, this is can't speak to a specific client. Just in general.

**Danny:** 
Given that Safe and Unsafe are almost equivalent almost 100% of the time on maintenance, I'm not, too, concerned about the distinction of which one gets fired here. So I'm going to withdraw my caring.

**MariusVanDerWijden:** 
I just took a look at our code and I think we can pretty easily rewire it, so, yeah, it should be okay.

**Tim Beiko:** 
Okay. And so there's a bunch of comments in the chat. So are we like, roughly aligned? Obviously finalizes there? Do we want to expose both Safe and Unsafe alongside Latest? So to have like, Safe?

**Micah Zoltu:** 
Yeah, I think the only contention from what I'm gathering is what will Latest alias do. I think everybody sounds like an agreement. We will expose finalized Safe unsafe, and we just need to decide again what Latest will alias to which of those. 

**Mikhail Kalinin:** 
And by default, it probably makes sense to make it an LS to Unsafe. there are probably some patterns where it is expected, but Latest will return the head, like, literally the tip of the chain if we change this semantics to, make it not always the head. So, probably some dapps and services, will have to adjust their code bases to use the new tag.

**Micah Zoltu:** 
There will be some, but those will be like professionals that care that much. The only people that care about a four to 6 seconds difference is like MEV miners, Frontrunners, etc. And I really don't care about designing our system to favor them. I would much rather design our system to favor the idiot that doesn't know what they're doing.

**MariusVanDerWijden:** 
Yeah, I think they're the same people.

**Tim Beiko:** 
Yeah, I know. Personally, just based on the experience of rolling out 1559 and like the time it takes to adopt, which was much longer than I expected, I would, push a bit to having Latest defaults to the Safe head because we kind of with a bit more rewiring, we kind of give this extra security for free to a bunch of end users who might not be aware about it, and that seems like a win and otherwise I suspect it'll take years for certain applications to update.

**Micah Zoltu:** 
Yeah, I concur with the timeline like it's going to be many years before we see Latest stop being used, and that's assuming that we can get all docs updated to discourage use.

**Danny:** 
Yeah, I think I agree. I do also agree with Mikhail that the change has the chance to break more things, but if those are sophisticated users that can handle breakage, then I guess that's okay.

**MariusVanDerWijden:** 
And that's why I think we should create this spec as soon as possible. Implement it as soon as possible so we can have users test it.

**Tim Beiko:** 
So I guess, does it make sense to go ahead with the assumption that Latest is Safe head, get that implemented as a high priority after, Kiln if we obviously see that something breaks in a way that is very hard to fix or whatnot we can change this decision. But yeah, at the very least we'll know it once it's implemented. and I suspect once we fork the public test nets is when we'll get a lot of data. about how real applications kind of react to this.

**MariusVanDerWijden:** 
One question would be what happens, in the case if we don't have a safe head yet? So, for example, in Proof of Work, we don't have a safe head then we need to, do the latest back rewired back to unsafe.

**Micah Zoltu:** 
If you are talking about like if you want to release your client with end points ahead of the merge, which probably would want to do right, ideally, I would say like finalized is some number of confirmations and safe one confirmation, but I don't like that either. That's, significantly longer than Proof of Stake. 

**Danny:** 
Sweep it under the rug and point safe. What that would do.

**Tim Beiko:** 
I think it's very weird to return something like a proof of work value to Finalize because they're very different concepts.

**Micah Zoltu:** 
I don't think we want to narrow it though, because we want people to update their dapps before the merge happens. That way, when the merge happens, they seamlessly transition into it. And so if Finalized don't make sense for a particular dapp, they can start using Finalized, which means something, useful like six confirmations or whatever, or ten confirmations or something that's approximately what finalized. Something that's useful to them and is kind of representative, in terms of time scales that's similar to what finalized will be in the merge. That way their dapp can still work today, but they can have it merge ready. So as soon as the merge happens, they can immediately start using the correct Safe unsafe finalized if they want.

**Danny:** 
So the spec can have if these methods are exposed prior to the merge. These are recommended values?

**Micah Zoltu:** 
Yeah, something like that.

**Danny:** 
I don't think we need to be super dictatorial on those recommended values. Okay.

**Mikhail Kalinin:** 
I'm sure it will be easy to define this recommended value, so probably get it. Think about it.

**Micah Zoltu:** 
We can discuss it in discord. I'm happy to hold on this conversation.

**Tim Beiko:** 
Cool. But just to be clear, do we have rough agreement that Latest is Safe head? Does anyone have a strong objection to that?

**Mikhail Kalinin:** 
I think that actually that developers should have this objection. personally, I don't have an objection to have analysis, safe or unsafe either way is good for me personally.

**Tim Beiko:** 
Cool yeah. So I guess as soon as Kiln is released, this is probably the next big thing that we should be working, on.

**Mikhail Kalinin:** 
So Latest is Safe, right?

**Tim Beiko:** 
Yes, I think we go for that with that for now. If some infrastructure provider, or application tells us this breaks everything in a very complicated way, we can change it. But assuming that that's not the case. You can just go ahead with that.

**Mikhail Kalinin:** 
Yeah. One thing to clarify here is that we have safe block hash currently point into finalized to the finalized hash. So we either should. Yeah. This will happen until we have get Safe head, implementation of.. That's the opposite.

**Danny:** 
I think it's the head and safe head are equivalent right now.

**Mikhail Kalinin:** 
Oh, really? Sorry for confusion. Yeah, I was just going to suggest.

**Danny:** 
Yeah. So there's actually work on the consensus layer side that I think is ongoing. We can catch up on that in the call, next week, but I believe they're trying to kind of, make sure the engineering requirements are trackable with respect to the algorithm.

**Vitalik Buterin:** 
One quick concern on Safehead. So the Safehead formula basically means that the Safehead does not progress if more than 50% of validators are offline. But the, whole point of having something other, like actually having the chain and not just doing LMD on the weekends, they all, have a chain that keeps progressing in that case. So do we want to try to account for that in any way?

**Danny:** 
I mean, that's an argument for keeping the latest as is. Right.

**Vitalik Buterin:** 
Or it's an argument for modifying Safe so that it only, takes into account it's based on recently online validators or something like that.

**Dankrad Feist:** 
I mean, shouldn't this be a manual intervention by the user? Because that's literally what Safehead is trying to protect you against. Like, say you are on the minority fork, then what you're suggesting is literally not Safe. That is exactly like you will be on the 10% chain because your, optical fiber went offline or something.

**Vitalik Buterin:** 
Right. But that's already a situation where you're assuming, like, high latency, that's causing you to not see the majority chain. Right. So safehead is already conditional on that.

**Dankrad Feist:** 
It would in practice protect you from that, though. Like, it would in practice exactly in this situation. Stop that. Also, it's true that I guess you can't prove safety under this condition, but it would protect you from exactly that. So, I mean, my feeling is that this should be a manual user intervention like the situation you described should be me as a user saying, yeah, I checked. This is not due to a catastrophic outage of, networking split between US and Europe. It is instead because, a majority client, went offline due to a bug. So I want to trust this chain.

**Vitalik Buterin:** 
I don't know how I feel intuitively how I feel about that. That does really move away from how we've been treating the head of the circumstances so far.

**Dankrad Feist:** 
Right. But isn't a network split the most likely thing that leads to such a condition? 

**Vitalik Buterin:** 
It depends. There could also be lots of notes going offline at the same time.

**Danny:** 
We should probably have this conversation out of the call.

**Tim Beiko:** 
I guess we can use just the merge general channel to flush this out. Sure.

**Micah Zoltu:** 
Yeah, I think if I'm correct me wrong, but this particular discussion is consensus layer, right. And whatever this layer feeds the execution client is what the execution client.

**Tim Beiko:** 
Cool. Anything else on Kiln or the merge?

## Shanghai Planning

### EIP-4863: Beacon chain push withdrawals

**Tim Beiko:** 
Okay, next up, we have a new, EIP for beacon chain withdrawals, which uses a push format. Danny and, Alex or the authors. I don't know if Alex. Yeah, both of them are on the call. Do you want to give, a quick rundown about the changes?

**Alex Stokes:** 
Yeah, I can. Last time we talked about withdrawals that would be implemented in this pool style where the user would have some proofs there'd be some information committed to an EVM, and then you could affect the withdrawal. Danny actually did an analysis, of how the spec was written. And basically based on that, that kind of got, us more confident in a place where we could move to a push style withdrawal, where the idea is basically when the conditions are met on the beacon chain, you can imagine these withdrawals are sort of forced into the head of an execution block and, then validate it that way. You can read the EIP, but the main thing is a new transaction type, a new EIP 2718 transaction type that is treated pretty specially rather than having the EVM execution. It essentially just instruction for a balance transfer or a balance increase. Yeah. The one thing that I think we want to do that we haven't yet with this EIP is add, logs. That was the one thing most people are doing so far with these types of withdrawals. Otherwise yeah, I guess the main question here is just general approach sounds good to everyone with this new transaction type with the new semantics and yeah? Danny, was there anything else you wanted to add?

**Danny:** 
Yeah, the document I shared here pretty much in the spec for the validator that defines these credentials which so called ETH 1 which are all credentials that can be deployed on maintenance today it says that code would be executed. So we did analysis to see if anyone's actually depending on that because if they were heavily that would kind of preclude this and really need pull to handle gas accounting and things. It doesn't seem to be the case.

**Danny:** 
So I think it does open this up and open up being able to change this withdrawal credential definition. But yeah, it's pretty much the consensus layer maintaining a queue of these withdrawal receipts and queueing them into the execution layer and that being a consensus layer validity condition that the exact proper type three transactions are put into that execution layer block and the execution layer just does the balance updates accordingly. No signatures and things or proofs required. Mikhail.

**Mikhail Kalinin:** 
Yeah, I think that's simple on the outside, but one thing here. I understand why withdrawal operation is made as a transaction to reuse over the existing mechanism and probably reduce the complexity. But I think that semantical withdrawal is not a transaction because what we usually use for transaction is the application layer transaction and withdrawal operation is not an application layer stuff, it's more in protocol thing. So I think it would make sense to have like a separate set, separate list of operations, separate list of withdrawals and just to make things more clear in code and more clear like less conditions to check. So we have a separate list which is checked by consensus layer and it doesn't need to be combined with the transaction place. So that's what's in mind. 

**Danny:** 
Right.

**Micah Zoltu:** 
I think there's minor benefit I think in having them include transactions just because tooling that already exists for tracking deposits and withdrawals on chain, just like tracking east and the movement of ETH and whatnot, we'll all just kind of just work more or less or at the very least you'll see a new transaction type now knowing you need to deal with. Whereas if we put it somewhere else it easily gets missed by tools that are trying to aggregate.
This is minor, not a not big deal. Just to keep an eye on. 

**Danny:** 
Right, right now on the consensus layer we do track it in a separate list and there's a couple of different designs but you could pass it as a separate list on the engine API and then the execution layer could then construct the execution layer block in whatever way we decide is reasonable. I think right now it's a type three transaction after some discussions with geth. And I do think, that's a reasonable approach. But if people wanted to make a new kind of system operation list and deal with it differently, I'm open to it, but I think there's less friction in doing it as a type three transaction.

**Andrew Ashikhmin:** 
Yeah, I would like to have a, more comprehensive document, because here in this EIP, I see only very limited set of changes, only concerning, the execution layer. I'm like, personally, I'm uncomfortable implementing this without understanding the entire picture. What's done on the consensus layer or what are the security guarantees? Basically, I like how the other EIP 4844, should have block transactions specified. It concerns both layers and I think going forward in general, it would be nice to have, like, if it's a set of changes concerning, both layers, that they should be all specified in a single document.

**Danny:** 
So I do have the consensus layer specified. It's in a PR, because that's ultimately where it needs to live, because that's the way that spec is written. Certainly, there can be more exposition in EIPS, and I think that is a conversation we have in the merge EIP itself. It's not in the merge EIP itself. there are these events and you just listen. These events and the entirety of that beacon chain, functionality is not specified. there and is instead specified. Kind of an, ancillary, reflective spec. But I'm open to this is more about EIP process. The functionality is defined and I'll link to it in, a comment on there so that you can go look at it. Ultimately, if, we had to find it in there, we're going to have to find it somewhere else as well. And so I'm a bit hesitant to be writing things down in two places.

**Andrew Ashikhmin:** 
Because right now, what are the security guarantees? I just personally don't understand them that no malicious player includes such transactions. So to me, it seems a bit very raw at the moment.

**Danny:** 
Well, I'm going to point you to the reflection of the consensus layer specs. Quite frankly, these are bound by literal, withdrawals and ETH and validators are put into a queue and they're ensured that they are precisely the correct amount is put into the execution layer. That, is the functionality and its consensus layer validation. But I will show you, a link to the PR right now.

**Micah Zoltu:** 
Am I correct that this is an alternative to doing withdraws via traditional Ethereum transaction and a contract that can validate approve?

**Danny:** 
Correct, right.

**Alex Stokes:** 
And not needing the beacon state or anything like that.

**Micah Zoltu:** 
Contextually. The advantage or the argument in favor of the other one is that it doesn't require anything on the execution layer. Right. Like student client team doesn't need to do anything at all. Is that accurate?

**Danny:** 
What do you mean? On which one?

**Micah Zoltu:** 
If we go with the special contract that just, has a bunch of ETH in it?

**Danny:** 
Well, they need to have the beacon root opcode for one and for two, it needs to be able to send transactions from no ETH at the source or to mint 10 to the 10 million ETH end of this contract at some fork boundary.

**Micah Zoltu:** 
That's right.

**Danny:** 
Which the latter, after discussions last couple weeks is most people, do not want to do at all.

**MariusVanDerWijden:** 
I think my main point was we don't want to have another way to start a transaction. We don't want to have another way to start an EVM execution because that might add additional, complexities. So what if the transaction reverts? What if the transaction, I don't know, creates another contractor?

**Micah Zoltu:** 
Is there a reason that people are doing withdrawals can't just be expected to have some ETH on layer one to pay for it.

**MariusVanDerWijden:** 
The problem is if this transaction can revert, then you need, to tell, the consensus layer about it. And by doing it this way, only the consensus layer tells the execution layer do this and then there's no data flowing in the opposite direction.

**Danny:** 
Yeah, you pretty much, can't do push in the same way if it's going to be triggering code execution that is unbounded. You can do pull. And so I think those are the two options on the table.

**Mikhail Kalinin:** 
Will this transaction type if we go with transaction, which is banned in the mempool?

**Alex Stokes:** 
No. Yeah, it will only be part of blocks pass, from the client.

**Mikhail Kalinin:** 
There will be exceptions, so there will be exception in the mempool code. So if you see this transaction just drop and then they're not propagated it just...

**Danny:** 
Yeah, there's no value to it and no way to validate it.

**MariusVanDerWijden:** 
I wouldn't even really, call it a transaction. I think it should be passed in the engine API as a block and then we include it as a transaction into the block, but not really use it as a right.

**Danny:** 
So in the engine API, you can have essentially a new list of system operations that the meta system of the beacon chain is dictating to put into the blocking them with the transaction list.

**Micah Zoltu:** 
The way it accidentally gets them propagated is if you, block gets uncled. Or I guess we don't have uncles anymore.

**Danny:** 
You have blocks that are uncled. 

**Micah Zoltu:** 
So at least under proof of work, if the block gets uncled, all the transactions that were in the uncle block can get propagated across networks. Like when you receive that block, you receive all the transactions that were in it and they just are a big list of transactions you're like, oh, here's new transactions. I can start spreading these out. If we're adding a new transaction type that, should not spread out. That means the code will need to be added in that area that says when you're blasting out all the transactions on a block, don't include these unless the block is actually mined, in which case do include them.

**MariusVanDerWijden:** 
It's not hard to do that.

**Danny:** 
Yeah, but any exceptional argument, any exceptional condition like that does lend argument to making it a new system operations list rather than transaction. I don't have the depth to say which one is more reasonable. My intuition is the type free transaction, but I could be convinced.

**Micah Zoltu:** 
I think I'm very weakly in preference of a system actions, system operations, list, but very weak at the moment.

**MariusVanDerWijden:** 
Yeah. I'm also weakly in favor of system operation because we're doing a lot of like precondition checking on transactions. Yeah, I think we have to implement it, prototype it and see what works, what creates like, mess.

**Danny:** 
Alex, you did do something on a prototype right?

**Alex Stokes:** 
Yeah, I didn't touch any gossiping or networking, but essentially it has a transaction types. I mean, it's super streamlined because it's just another transaction type. There's like one minor check to say, hey, if this is one of these type three transactions, then just do a balance increase. Otherwise, hop into the EVM. I thought it was not, that bad. I'll go grab a link.

**Micah Zoltu:** 
Are there other system operations we have in mind anywhere on our current roadmap?

**Danny:** 
No.

**Micah Zoltu:** 
Even five or ten years down the road. Is, there anything that we're thinking about that would also fall into this category?

**Danny:** 
I can't think of anything immediately.

**Lukasz Rozmej:** 
So not system operations, but account obstruction uses some kind of user operation that's also concept separately and bundled into transactions.

**Danny:** 
Right, but those ultimately making it into normal transactions, right?

**Lukasz Rozmej:** 
Yes, but not sure. But maybe when included to the block and before that they leave a separate entity. But I'm not entirely sure.

**Tim Beiko:** 
Right, there's a comment from Proto in the chat about how LTs also have a similar concept where when you deposit funds from L One to L Two, it's kind of similar than depositing or moving from the beacon chain, back to the execution layer. So perhaps, if the mechanism kind of can be reused, that, might be interesting. 

I guess in terms of next steps here, is it worth trying to prototype a sort of system operations version of this and perhaps having both side by side can kind of help, decide?

**Alex Stokes:** 
I'm happy to do so, but does anyone actually want to see that?

**Andrew Ashikhmin:** 
Yeah, I think it makes more sense. I agree with Mario that it makes more sense to have it rather than transactions as kind of system operations. and my understanding is that Engine API should definitely, be involved. The EIP is not complete. I don't see any mentioning of Engine API at all here.

**Danny:** 
The Engine API has not made it into EIPs before but instead has these kind of operations or these events from the consensus layer. So it would be the expansion of an event like, the new block event or whatever, that would also have these operations.

**Andrew Ashikhmin:** 
Well, my point is, it doesn't have to be, like verbatim in a single document, but at least there should be references so that when you have a single document that references, it has all the necessary references that I can have a single point of entry, and then I'm able to understand the entire picture. What changes on the consensus layer? What changes on the engine API? What changes on the execution layer? Otherwise, it seems like, separate bits without any unifying picture. Okay, sorry. That's my two cents.

**Tim Beiko:** 
Right.

**Micah Zoltu:** 
I think what Andrew is asking for is the thing that I always push the Core EIP authors to build, which is don't include that in the EIP, please. But, big EIPs like this definitely benefit from having, like a HackMD article or something that ties it all together like Tim did with EIP 1559. I use that as my example always. It's an excellent example of tying the whole picture together in some meta document. And the EIP can remain just the spec.

**Tim Beiko:** 
Right. This is, I guess, kind of it.

**Danny:** 
Yeah. We can put all the pieces together in one place.

**Tim Beiko:** 
Yeah, I guess we do that withdrawal sort of meta spec. Yeah.

**Micah Zoltu:** 
The downside is it requires a bunch of writing. No one likes doing that.

**Tim Beiko:** 
Does that make sense in terms of next steps, though? To prototype the systems operations version and to put together a kind of more comprehensive meta spec?

**Danny:** 
Yeah. And the, document, the consensus layer, and engine API, I think will look almost exactly the same, whether it's the system operations or not. And then there will, be two options on the execution layer. So two EIPs choice at that point.

**Micah Zoltu:** 
To tac on a question that was asked earlier, would a prototype actually sway anyone one way or the other? I agree that we shouldn't have to waste their time building prototype. If that will not sway any opinions.

**Danny:** 
Maybe it's worth writing down and kind of a stripped down EIP before doing the prototype. Sure, to see any partages.

**Tim Beiko:** 
I guess yeah. Marius, Andrew, would that sway? Yeah, I guess it's mostly for your consumption. So, any thoughts on that? I don't know if you're speaking, Marius, but we can't hear you on Zoom.

**MariusVanDerWijden:** 
I'm not speaking.

**Tim Beiko:** 
Okay, sorry.

**MariusVanDerWijden:** 
yeah, I'm happy either way. I looked at Alex's PR, and it looks pretty good. So I would be also okay with having the transaction style. I don't know.

**Danny:** 
Well, let's put the metaspec together, have a proposal for the engine API, finish the networking components and log components, of the existing EIP, and get some feedback from there. And then if people, feel strongly about after, they get to chew on it a little bit, a different operations list, we can address that at that point.

**Tim Beiko:** 
That sounds good. Cool. Just because we're starting to run  short on time, that seems like a good next step. We do have a couple more EIPS, so I'll move to the Shard Blob, transactions. 

### EIP-4844: Shard Blob Transactions

**Tim Beiko:** 
Basically, last time we discussed this, everyone seemed to think this was a very valuable thing to have in Shanghai. But there were questions about how easy it would be, to actually implement this, what it would take. And a few people implemented a prototype during EthDenver. Proto was one of them and he posted an update on the agenda today. Do you want to take a couple of minutes, to just walk through the prototype you implemented and then you have a couple of questions you wanted to address on the call?

**Protolambda:** 
Yes, sure. Thank you, Tim. So hello everyone. We're presenting EIP 4844 titled Sharp Log transactions. So not to be confused with 4488, the older call data expansion thing. This just focuses on the separate data works differently. Bear with me. I'll summarize the EIP. this introduces a new transaction type. The transaction type has all the same features as a regular 1559 transaction has. However, it adds this additional data outside of the transaction. This data is not encoded within the execution layer. This data is instead stored within the consensus node it can be pruned after being available for a sufficient amount of time. This data is formatted as these field elements. so this means we can do this case G commitment over the data instead of regular hashing. And this EIP also introduces two pre compilers and an Opcode to verify this data within the EVM in an efficient way. And then this VIP is also forward compatible with the fill sharding design where we introduce data availability sampling. Then the tricky points with this EIP are really that we are introducing this transaction type that has this additional data that lives with the transaction when it's produced and it's propagated but not within the execution payload. But then the data is stored as this Blob and it's referenced in the beacon block. It's referenced to the transaction but it's not stored along with it. It's temporarily retained within the consensus layer or not for this shorter term availability.

And then in Agenda, I listed a few points, how we can extend this EIP and if this is the right approach. This EIP 2718 that first introduced the transactions describes how to encounter these transactions. But now that we have this additional data, we might want to define how this network payload differs from the encoding as presented within the regular transactions list. And then how do we relay this block data? it could relate with the transaction or there may be more efficient ways. And then similar to the withdrawal transaction type, this also looks at implementing a transaction type of different encoding with SSE. And then we also have this question how we will introduce KCG commitments into Ethereum. We have been looking at how we can facilitate the trusted setup, how we can introduce this in various different clients. there are libraries that offer this case G functionality and we are looking to minimize it as much as possible so that it's actually really simple extension to the POS work that's already present in clients. And then from there we need to work on Dev nets. And we built this prototype for the execution layer, for the consensus layer. I'd like your review on those implementations so it can improve the EIP.

**Tim Beiko:** 
Thanks for sharing all this. There is a question about science in the chat. I guess we can start there where the case at G commitment is probably the biggest or like most contentious thing as part of this. What are client team's thoughts about doing this in basically the next year?

**Danny:** 
The commitments came because of the kind of cryptographic complexity of those operations and just needing new and robust libraries. Is that what you mean?

**Micah Zoltu:** 
Like I think it's basically the same argument that kept BLS from getting integrated for two years.

**Protolambda:** 
Right. But KCG is mostly BLS, right?

**Micah Zoltu:** 
Sure. So if we still don't have BLS.

**Danny:** 
But we do have BLS in production, we just don't have EVM operations. We use it quite a bit. Millions of operations.

**Micah Zoltu:** 
Not on the execution layer though, right?

**Danny:** 
Correct. But not in the EVM.

**Tim Beiko:** 
Andrew has his hand up.

**Andrew Ashikhmin:** 
Yeah, I guess I missed the original discussion about BLSing the execution layer. To my mind, there is already better proven library that can be used. So I'm not that worried because it already exists. So from my perspective, we can implement it and ever gone relatively easily. There are a couple of corrections, small things really. So that in the signature in the it uses V, but V is this legacy field that blends chain ID and Y parity. And we should use Y parity similar to EIP 1559 transactions and also in the intrinsic gas. A couple of things are omitted. The create cost for create transactions and the cost of access to this. I made the comments on the magicians. It's just minor corrections.

**Protolambda:** 
Yes, thank you for your comments. We'll get back to those on the forum. In general, all the functionality is just the same costs and everything else we have EIP 1559. If there are differences, then we'll try to reduce those. The only real addition here is that we're adding this additional data. So this list of version hashes and those hashes refer to the data that's been propagated along with the transaction.

**MariusVanDerWijden:** 
Can you expand a bit on the upcode and the two precompiles? What do they do?

**Protolambda:** 
So the pre compilers are to verify this type of case commitment. There's one way to verify a single point of data, and there's another way to verify all of it at the, same time. And the idea really here is that we want to not introduce the stateless requirements to the EVM where we are directly accessing this transaction data, but instead we provide a proof and the original data score data into the EVM and, they can prove that it matches the case of G commitment. So we can prune away this information and the EVM exclusion will still work. The book data is really independent from the EVM.

**Tim Beiko:** 
There's a question in the chat about, concerns about history growth.

**Protolambda:** 
Yeah, so the transaction type does the same thing as 1559 so in that regard it doesn't grow more, and then the additional data on the block that's retained in the consensus layer, not in the execution layer. So it doesn't affect history growth by all that much. Within the execution layer, there's this list of version hashes, but it's a maximum of 16 hashes, so that's not really not that much compared to at least other limits with the EVM. The real growth is in the consensus layer, and this is limited to, say, a month of data, even, when we have large blocks, and then we say we have a megabyte of data per block, then we have a month of data. This is still capped to the maximum and doesn't grow out of bounds. And these parameters like for how long do they retain the data for how many of these plots do we want to start with? These are up for discussion. Got you.

**Danny:** 
Yeah, it's worth just noting that data availability that is needed for roll ups doesn't mean persistent data storage. it means ensuring there are these data withholding attacks and that those that want the data within some bound time can get that data and that, it's made available, but not that it's been persistent forever. Similar to dissimilar to the chain persistent requirements that the Proof of Work network has right now.

**Tim Beiko:** 
Guillaume, you have your hand up.

**Guillaume:** 
Yeah, I just had a quick question about the KCG again. I, used it for verkle trees in the past. I'm confident it's not such a big deal, but we moved away from that for verkle trees. How about using IPA instead of KCG? Has that been considered?

**Vitalik Buterin:** 
Yeah. So I actually wrote a big ETH research post considering it. And the answer is basically that doing data availability sampling, and all of that associated stuff just gets much harder with IPAs because they don't have a lot of the nice algebraic, properties that KCG does.

**Guillaume:** 
Okay.

**Protolambda:** 
Right. So one of the features of this EIP is that it tries to be forward compatible with the full Sharding roadmap. And central to that is data availability sampling, which has been designed around KCG and optimized for KCG and so by building, on top of that, we are forward compatible and we can roll out sharding without further changes to the execution layer. It'll just be consensus layer changes after this.

**Danny:** 
Right. So a nice way to think about it from that full sharding map is really blackboxing. Is data available? That's this function that the consensus has to call. And in this proposal you just download the data, but in subsequent proposals you swap that functionality and new data availability sampling as there was some more and more data.
There have been some questions about a trusted set up. Yes, KCG, commitments in the scheme would require a trusted setup of relatively low number of power, something on the order of like 16. Actually, I think it requires twelve, but we would do 16 to, handle quite a bit of growth from there in the future. And this, is something that would be required for sharding no matter what. So it's something that the EF is looking into doing right now and kind of surveying the landscape of previous, powers tile that have been done and looking to reuse some of that tech, but also too, because it's a low number of powers likely doing some sort of browser based ceremony being available, to get much wider participation than prior ceremonies. but working.

**Micah Zoltu:** 
Low power just means the computation required to participate is lower. Right.

**Danny:** 
Yeah. Our estimates is you could do this in like a minute and a half on, your browser as opposed to doing it in a highly optimized compiled thing that still took 20, minutes.

**Tim Beiko:** 
Great. Just again, because we're a bit short on, time in terms of next steps here. obviously there's been like some technical, feedback on various aspects of it, but I guess what are people's biggest, what are the things that people would most want to see to consider pursuing this further?

**Danny:** 
So I just want to say it seems pretty critical that some sort of scaling relief is provided in Shanghai. I think our two options are repricing and modifying call data, which has chain growth issues and also isn't really elegant with respect to the future sharding map. Whereas this brings in probably quite a bit more complexity, but is synergistic and essentially it lays the foundation for extending it to be compatible with full sharding. So it kind of lays the foundations and kind of iteratively gets us to sharding. So it's really a complexity trade off versus the elegance of this integrating into the charting room map in general. And I think it'd be very valuable to get client influencers take on the complexity here. There is that prototype that Proto and others worked on. Yeah. I mean, getting Peter, getting Martin, getting anyone a deeper look at this would be really valuable.

**Ansgar Dietrichs:** 
Yeah, I just wanted to say for context, maybe just going forward, I, think the important thing is really just as Danny was saying that we basically really want to do something for Shanghai, for scaling. And I think the one thing we want to avoid is everyone agreeing that this would be nice. And I think right now it sounds like everyone, our clients are agreeing that this would be nice and then only four or five months from now, people kind of get to the point where they're like, yeah, but unfortunately it's just too much complexity. We just won't be able to do that for Shanghai. And at that point we'll be very late to try and simplify or try and do other things. So basically the idea would just be like ideally we would want to get feedback on how realistic as soon as possible. And I think for example Lifetime had looked into simplifying that removing the KCG part, which would be great because then you lose some of forward compatibility, some of the usefulness for ZK roll up. So it's not great, but at least it would be something we could do, try to do if this is just too complex. But like it would be really important to get back feedback on how realistic, not just how desirable but how realistic is this for like a timeline that would have this in Shanghai at the end of this year?

**Tim Beiko:** 
And I think one thing I'll add to that is we've already committed to one thing which is actually a set of EIPs, but like to the whole EVM object format. I guess call it a feature for Shanghai. we have these discussions about beacon chain withdrawals, which clearly are like a non trivial thing to do no matter what approach we take. And then we have this. These are set of EIPs. Those three features alone are kind of already a very large hard fork. And that's probably something like I guess as soon as the merge code is wrapped up that we need to consider if we did those three, is that even realistic? If not, what else can we do?

**Danny:** 
Real quick, removing the KCG that would essentially be using a different commitment scheme currently to reduce complexity, knowing that full data is going to be downloaded and you don't need to do data availability sampling. And then in the future you would essentially deprecate that transaction type for a new transaction type that had KCG commitments that allowed for the data availability sampling. is that the idea?

**Ansgar Dietrichs:** 
Yeah. The commitments are already versioned in the way we specified it.

**Dankrad Feist:** 
So using a different commitment scheme would basically making version zero of the commitment scheme being a hash based one.

**Danny:** 
Right. But we'd have to get that commitment scheme from Sharding because you wouldn't be able to do the data availability, basically. 

**Dankrad Feist:** 
Yes.

**Protolambda:** 
The transaction type still has to encode it in one way or another and Federated in one way or another, even though it's versioned within the EVM, there will be some difference.

**Dankrad Feist:** 
It also would not, allow the evaluation at a point 1, which would mean it would be, much less useful for ZK roll ups.

**Tim Beiko:** 
Okay, I guess just to time box this because we do have two other topics to cover before the end of the call. Where's the best place, I guess, for people to, review this and engage. Do we have, like, a channel on discord for this or something?

**Protolambda:** 
There is the Sharded data channel, which we can revive originally for the full Sharding roadmap. This is a stepping stone. So let's start there. And then there are two prototypes. One on the execution layer, one on the consensus layer. If you're specialized in either one of those, then please have a look and reach out and give your feedback.

**Tim Beiko:** 
Cool. yeah, let's use the Sharded data channel.

### EIP 3651: Warm COINBASE

**Tim Beiko:** 
Okay. thanks a lot for everyone on this. Next up, there's another EIP that we had discussed briefly for Shanghai, EIP 3651, which proposes to treat the Coinbase address as warm. We have William on the call. Do you want to give a quick summary and I guess, reason why you'd like to see this in Shanghai? 

**William Morriss:** 
Yes. For Berlin, we added EIP 2929, which initialized the access list to include origin, the recipients, and the set of all pre compiles this missed Coinbase, unfortunately. So the proposal is, to add Coinbase to this list. It would reduce the cost of direct Coinbase transfers, which are used by conditional transaction fees, such as, systems like Flashbots, where there's, an option system often, but you're trying to pay the miner conditionally only if your transaction succeeds or does what you want. And I currently believe these are overpriced because we already modify the Coinbase's eth balance and account several times during the block to receive the block reward and the transaction fees. So by making Coinbase warm, it should already be correctly priced to reduce that cost. Thank you.

**Tim Beiko:** 
Thanks. I appreciate what our clients thoughts on this. Andrew.

**Andrew Ashikhmin:** 
Yeah, I think it's a simple and useful proposal, so, I think we can do it in Shanghai.

**Tim Beiko:** 
Anton? Sorry. Anton. Then, Marius. Anton, you're back on mute.

**Anton Bukov (1inch):** 
Can you hear me?

**Tim Beiko:** 
Yes.

**Anton Bukov (1Inch):** 
Sorry. Hi, everyone. I have also the, question regarding, this, as far as I remember, each, call with value attached will, cost also nine K, of gas extra. This maybe also should be, reviewed, maybe with another improvement proposal, because this, is also a lot.

**William Morriss:** 
Yes, I agree with that. That $9,000 for eth transfers might make sense in a cold context, but not in a warm context, that, should be reviewed in the future.

**Vitalik Buterin:** 
So in the verkle tree writes Gas, cost EIP. This is one of the companion EIPS through the verkle tree EIP. I do have a proposal that basically removes all of those kind of special purpose gas costs and moves them all into the cold warm system. So one of the side effects will be that, like, warm eth moving will be cheaper.

**William Morris:** 
Thank you.

**Tim Beiko:** 
And Marius, you are going to say something earlier.

**MariusVanDerWijden:** 
Yes. Even though it benefits, mev people and I don't like mev people. I'll support this EIP. It was an oversight, in the original one, and I think it's a no brainer to include it. 

**Tim Beiko:** 
I guess am I right in thinking this is literally like a one line change in a way where we just add a parameter to the list of things that is warming?

**MariusVanDerWijden:** 
Not a one line change, but maybe five to ten. 

**Danny:** 
Plus like hundreds of lines of tests.

**Tim Beiko:** 
We already have included a couple of similar fixes, if you want, in Shanghai. I'd like to pull it up right now. basically push zero seems like another small one. limiting and metering in a toad. So is this something that people feel confident that we can kind of include as another small win and that, I guess, probably wouldn't affect our ability to ship these larger features we were just talking about? I guess to put it differently, does anyone feel like if we did do this, it might impact whatever we do? Block transactions, EV chain withdrawals?

**MariusVanDerWijden:** 
I think we can pretty easily include this. It increases the amount of testing we have. Every EIP exponentially increases the amount of testing we have to do, but it's not that bad.

**Tim Beiko:** 
Okay, I guess. Any objections with moving it to CFI for Shanghai and starting to implement it when we start the Shanghai devnets?

**Guillaume:** 
Yeah, it's basically repeating what Vitalik said, but, because of the verkle tree stuff that comes in the fork right after Shanghai, that, kind of makes this whole thing mute. Yeah, I just wonder. And in fact, it's also a comment about the next EIP. I just wonder if it really makes sense to bother doing this when it's going to, be. Yeah, sorry I forgot the word, but it's not going to be used afterwards.

**Micah Zoltu:** 
I think my one counter argument to that is just that, well, optimistically verkle trees will be included in the fork after Shanghai, history has shown that we are not super great at predicting our future roadmaps. And so for something super easy, there's an undefined duration.

**Guillaume:** 
Actually, the gas changes are supposed to happen in Shanghai.

**Andrew Ashikhmin:** 
I don't think it's true because that entails a refactoring, a fundamental refactoring on the data structures. So I don't think that gas changes for the verkle tree can happen in Shanghai.

**Tim Beiko:** 
Right. I guess, to be clear, the only thing we've agreed so far to include in Shanghai were the four EIPS basically related, the EVM, object formats 3540, 3670, which was the EOF code validation. Then we added, these two other small ones that push zero instruction and limiting and metering, in its code. And we had some sort of soft commitments, towards including obviously, beacon chain withdrawals and some kind of, scaling solution. Like we just discussed whether that's a whole new system or something more simple like reducing the call data costs. Yeah, it's worth noting those three things like EOF, beacon chain withdrawals, and block transactions are all pretty significant. So, I'm personally a bit skeptical of including any, other bigger thing until we have more clarity on those. But, yeah, I guess the question is, can we include this? there seems to be some consensus that we can include this small change. The question is, is it worthwhile to include it if in nine months after it gets obsoleted. Maybe quickly we can cover that before we move on and, hopefully stay like a couple of minutes after for the last EIP?

**MariusVanDerWijden:** 
I think it makes sense to include it.

**Micah Zoltu:** 
yeah, I don't, but.

**Tim Beiko:** 
Do any other client teams have an opinion on this?

**Andrew Ashikhmin:** 
Fine to include from Aragon.

**Gary Schulte:** 
Yeah, from a basic perspective, it doesn't seem like it's going to be a significant additional load, but it could be one of those death, by 1000 cut things.

**Tim Beiko:** 
Right. and Thomas or anyone else from Nethermind.

**Lukasz Rozmej:** 
Actually, I don't have a hard stance about it, but I think it's fine.

**Tim Beiko:** 
To be clear, when we say included, we're moving it to consider for inclusion, which is like this in between States, which will get it prototyped on the devnets and whatnot. So I think it probably makes sense to move, it there try to get it on the devnets. If we do see that, for whatever reason, this adds some overhead, that is just too great, we can always choose to remove it. And that's probably true of all the other small kind of quick fixes. If there is like an exponential testing increase by just having these small fixes, we can obviously decide to just focus on, the larger changes, but it seems reasonable to at least move it to consider for inclusion and try to get it on devnets.

## EIP Discussions

### EIP-3978: Reprice reverted SSTORE/CREATE/SELFDESTRUCT/LOGX operations to 100 gas via gas refund mechanism due to state non-modification

**Tim Beiko:** 
Okay. We're, already at time. I appreciate it if people have a couple of extra minutes, we can discuss Anton's EIP, which is EIP 3978. I appreciate you kind of bearing with us through the call. Anton, do you want to take a couple of minutes to just describe the EIP and, why you think it's valuable?

**Anton Bukov:** 
Yes. Hi, everyone. I was with my colleague Michael, first time participating in such a call. So we propose this EIP 3978, which basically, reprice the rewarded transactions. We discovered, operations. I would say, because we discovered that in case, of reward, all, gather fund is being erased. and users, they pay for reverted operations. Same price as for persistent operations. This sounds really unfair, because it increases costs of reward transactions. And in general it seems that we can switch this behavior to keep excess costs and refund the modification costs. Basically that's it. We enumerated the most expensive operations, proposal to use access costs for the separations, in case they will be reverted.

**Tim Beiko:** 
Thanks. There is a discussion too linked in the EIP. So we can have longer discussions there, but the people just have quick comments or questions before we wrap up. Do Andrew then Guillaume.

**Andrew Ashikhmin:** 
I think it's. Well, definitely not for Shanghai. and in general, Aragon's perspective is that instead of making small tweaks to the gas schedule, we should concentrate on bigger scalability improvements. So we are kind of tentatively against this.

**Guillaume:** 
Yes, same argument that I made before and what Andrew just said. This one is going to be very difficult to or at least very intricate to bill and it's becoming pointless after the verkle tree updates. So I would really be against this one.

**MariusVanDerWijden:** 
And I totally agree with Guillaume on this one.

**Tim Beiko:** 
Got it. Anton, do you have your hand up again? Yeah.

**Anton Bukov:** 
One more thing here I want to add. There is an interesting example. If some DEX is swapping user assets, it will be cheaper to return funds back to user to keep at least some guys refund instead of reverting whole transaction. This sounds a little bit strange and ridiculous.

**Micah Zoltu:** 
Am I correct understanding that if we don't make this change and dapps optimize, then they will optimize for the more operationally expensive choice which is to do more work. Is that correct? And actually write data?

**William Morriss:** 
That's right.

**Micah Zoltu:** 
That's unfortunate. I do think that this change is correct. It is the right thing to do. But I do want to Echo what said. I think the complexity is high and with verkle trees kind of doing the same thing functionally, much more questionable and more importantly.

**Tim Beiko:** 
So I guess the clearly does not like consensus for this. And like we just discussed, there's a ton of other things that seem to have really high, consensus for Shanghai plus verkle trees kind of slated for after. I guess if people do want to discuss this, there is a discussion to link in the EIP, but we won't be moving yet to CFI. We're already overtime the last thing on the agenda. Like I mentioned at the very beginning, we do have a call next Friday at this time.

## Announcements

### **EL Merge Client Release Naming Breakout Room #491**

**Tim Beiko:** 
So 1400 UTC to discuss the naming of the client releases for the merge on the execution layer side. If people want to join that, there's a link in the agenda. Anything else anybody wanted to cover quickly before we wrap up? 

Okay. Thank you very much, everybody. Thanks, William, Anton, and the others for coming out to present EIPS and we will see you in two weeks.

— End of Transcript —

## Attendees (39)

- Ansgar Dietrichs
- Tim Beiko
- Matthew Slipper
- Justin Florentine
- protolambda
- MariusVanDerWijden
- Pooja Ranjan
- Marek Moraczynski
- Greg Colvin
- Anton Bukov
- Trenton Van Epps
- Mikhail Kalinin
- Guillaume
- Mikhail Melnik
- Pari
- Gottfried Herold
- Vitalik Buterin
- Andrew Ashikhmin
- Karim T.
- Marcin Sobczak
- Danny
- Lukasz Rozmej
- Dankrad Feist
- Alex Stokes
- Fabio Di Fabio
- Jami Lokier
- Daniel Lehmar
- George Kadianakis
- Tomasz Stanczak
- SasaWebUp
- jmederos
- Micah Zoltu
- Jorge Arce-Garro
- Danno Ferrin
- Rai
- Ben
- Gary Schulte
- William Morriss
- lightclient
