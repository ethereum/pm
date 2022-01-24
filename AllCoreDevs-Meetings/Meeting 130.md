# All Core Devs Meeting 130
### Date/Time: January 21, 2022, 14:00 UTC
### Duration: 90 minutes
### [Recording](https://youtu.be/VffwWtklJvA)
### [Agenda](https://github.com/ethereum/pm/issues/449#issue-1096429590)
### Moderator: Tim Beiko
### Notes: George Hervey

## Decisions Made
| Decision Item | Description                                                              | Video ref |
| ------------- | ------------------------------------------------------------------------ | ------------- |
| 130.1 | Clarify PR for Engine API around the canonical vs. non-canonical chain | [25:05](https://youtu.be/VffwWtklJvA?t=1507) |
| 130.2 | Submit PR for authentication using JWT and discuss with CL team | [31:46](https://youtu.be/VffwWtklJvA?t=1906) |
| 130.3 | No current change to EIP 4399 but can discuss on Ethereum Magicians | [1:02:18](https://youtu.be/VffwWtklJvA?t=3738) |
| 130.4 | Created an issue on Github to discuss decisions on testnets post-merge | [01:13:13](https://youtu.be/VffwWtklJvA?t=4393) |

## Kintsugi Office Hours
Tim Beiko
Morning, everyone. Welcome to All Core Devs 130. Basically, a bunch of merge stuff to discuss today, along with some discussion on a couple of EIPS for Shanghai, potentially. 

## Engine API: extend semantics of executePayload and forkchoiceUpdated methods
***Highlights***
- ***Change proposes to remove requirement of semantics on executing the payload***
- ***This optionality is to give EL clients the flexibility in terms of the design.***
- ***Next steps are to clarify PR around the canonical versus non canonical chain and then review.***

Tim Beiko: 
First on the merge stuff. Mikhail, I saw you proposed a change to the Engine API based on some of the reorg issues we've been seeing on Kintsugi. Do you maybe want to take a minute or two to kind of describe the issue that led to this PR and what you're proposing in the change? 

Mikhail Kalinin: 
Sure. Um, thanks then. So this is the change, the changes that have been discussed recently on the Call and previously in the Discord. 

Um, let me just go briefly through a set of changes and probably we can discuss either fine or address some hard questions. Uh, right now. Uh, first of all, the um Execute payload previously had uh, two uh semantics which is syncing if there is not enough data for executing a payload and validating it and getting activity content by a client with the minimal response and execution semantics. And um in the case, if there is enough data, the execution semantics was kind of mandatory. So this change proposes to remove uh, this uh, um requirement, uh, this strict requirement on executing the payload. 

So the execution where the client may just keep blockhash or do whatever else with the payload. It's not executed. 

Mainly this is to address the case when the payload is coming from the site work, which is like missing data for the payload to be executed or the client according to its implementation doesn't execute payloads on the side forks unless they become canonical chain blocks. So it just doesn't require to execute it anymore. Um, also the validator is updated now, becomes uh aware of execution and if that need be, according to the client implementation, it may execute and validate payload before updating the fork choice state. So that's like a major change in this set of changes. Also we have an accepted status for Execute payload. By the way, execute payload is renamed to new payload to um, make it more sound with respect to removing this execution semantics with respect to making it optional. 

Um, yeah, accepted status which may be returned to a new payload would mean that a payload is uh accepted. The block hash is valid, but um, the uh execution isn't going to do anything with this. It isn't going to initiate either the receiving process or execute this payload. Uh, so that's the new status that we have in response. By the way, this change proposed to have the block hash validation, um, it stated explicitly and the new payload method, so the blockhash must be validated disregarding the state of the software because it doesn't need any additional data, um, except for the payload and um the Constance from the EIP 3675. 

Also there is one change that is required by the optimistic sync um and if the payload is from the canonical chain but uh execution uh their clients making catching up some site work. Let's assume this case and um there is a new payload. The child of the current head of the chain is coming from the consensus client. Execution layer client must validate uh it and respond accordingly um and not respond syncing. 

So we have the syncing process on the side branch, but the uh software can still verify the payload on the um canonical chain and it's currently stated in the fact that it must validate the payload. In this case, this is required by the optimistic sync to um avoid uh turn optimistic for no reason yet. It's some additional stuff there. So there is the payload validation process section and sync process section that gives a notion of the uh execution process, how it looks like. And this reference from the fork choice updated meditation from the new payload added now. 

And yes, there is a sync process section that just gives a brief description of what the same process is. Basically, this does not introduce huge changes to the El client software and the main purpose of this is to reflect the current state of the uh art of the logic of different clients and support logic of different clients. When do they run the execution and how do they maintain works and payloads for different works. But uh, the complexity on the CL CL client CL side might be increased because CL uh client will need to learn how to handle different statuses and different um and different semantics on the function updated method. So it may return syncing, it may run execution, it may do uh nothing and engage uh clients from both sides of the stack to take a look at this PR and comment out. 

That's pretty much it. With respect to this PR, I can drop a link. 

Tim Beiko: 
Yeah, I put a link in the chat already. Uh, Lucas, you had a question. 

Lukas Rozme: 
Yes. So if the execution isn't mandatory, then we don't, validate the state route, right? 
What would happen? Could this be a potential issue? 

Mikhail Kalinin: 
Yeah, that's it. It's not just execution called validation. So you don't validate this take root. But the potential uh issue here is that… the caveat is that if you receive forkchoice updated and it's about set head to some um block, it must be validated. So you must run this uh validation process at some point. 

So, uh on the new payload, you may just store this block and you receive the pictures updated and you must validate it before you update the forkchoice state. 

Lukas Rozme: 
Okay. So it complicates the consensus layer, right? Because they might think the block is fine and when they try to set it aside. They know that okay, it's not fine. 

Mikhail Kalinin: 
Yeah, they will have to follow. 

The example is like new payload returns accepted. So it's okay in terms of block hash, the payload deals correctly in the block hash as well. But consensus where client doesn't have any information with respect to alludity and it doesn't have any information with respect to whether anything is required, like all of this process is required to validate this payload and then it send boxers, updated them, wait for the uh response and response might be valid, which would mean that the payload has been executed, has been validated, and it's valid. And uh the fork choice date has been set to have been updated accordingly. 

Tomasz Stanczak: 
So does it mean now that the entire voting process attestation process and consensus layer happens on a block that is uh not known to anyone voting whether it's correct or not? 

Mikhail Kalinin: 
No, it does not mean that. The optimistic uh sync back says that um until the consensus client receives the valid status for the payload, it doesn't matter whether uh the new payload or updated response with the status um, but until it's received. And if um the canonical chain, um, if the head of canonical chain hasn't been yet validated, so it hasn't been sent for the canonical chain, then, um the node turns optimistic. It applies the consensus below clock optimistically without verifying the validity of um the payload, the execution payload, and in this case, while their client stops attesting um and proposing a block. And then in the case when the voucher is updated, it induces the validation process. In some edge cases it might be the case, it might turn the note optimistic. Um, for example, rework happens to the fork which uh is more than one block lands. 

And in this case the software response was syncing because it has to execute multiple payloads and so forth. So yes, there are implications, and most of these implications are for consensus layer clients, not for the execution layer clients. 

Martin Hoist Swende: 
I have a question which I guess it's kind of similar to the question that someone else asked. The client software should validate the payload, but what if we are all on the execution layer decide that now for this method, it's just "ah shoot. I'll just validate it. I'll do it later." What would happen then? Wouldn't it mean that the CL level would have to attest optimistically? 

Mikhail Kalinin: 
No, it must not be attested optimistically. So if it happens with the canonical chain, it will turn uh into optimistic mode and we'll wait for the execution layer to make those validations. 

Martin Hoist Swende: 
And what triggers the execution layer to make those validation? 

Mikhail Kalinin: 
Um, it's now up to execution there. It may be triggered upon receiving new payload or for choice, updated. 

Martin Hoist Swende: 
Right. But it doesn't trigger on the new pedal because it's optional. 

Mikhail Kalinin: 
Yeah, and this change proposed if they changed the reply, that could uh be the case when neither new payload nor forkchoice updated have um triggered the execution. 

So it might be the case, then the CL client will stay in limbo forever until, um, it's resolves or if it can be resolved. 

Uh, this optionality is to give, uh, execution layer clients the flexibility in terms of the design. 

Martin Hoist Swende: 
Right. So, um, if it says that we should validate the payload, if we can, then we can all make the implementation decision that. Yeah, we'd rather not. We'd rather wait a bit because that's easier. 

Mikhail Kalinin: 
Right. 

Martin Hoist Swende: 
Would you make it this wouldn't be better if the client offer must battle payload requested data repair validation is local available, right? 

Mikhail Kalinin: 
Um, yeah, I see. So I guess, uh, we can do this for the canonical chain if this is like the child of the head of the canonical chain. 

I mean, if we uh, require validate every payload, disregarding whether it's from the side chain, from the canonical one, we make the spec uh, too strict for the clients that does not execute a um, loss from side chain. 

Martin Hoist Swende: 
Yeah, I'm just saying that you shouldn't leave it as like implementation choice if you want to validate it or not when you can. 

Mikhail Kalinin: 
Oh, yeah, that's a good point. I think it should be in the spec. 

So will it be good to say that it may skip payload validation if it's not on the canonical chain, but uh, it must validate if it's the canonical chain. 

What do you think about it? 

Martin Hoist Swende: 
Um, I don't know. Off the top of my head, probably better. 

Andrew Ashikhmin: 
Yeah, it sounds fine for Aragon. 

Mikhail Kalinin: 
Cool. Okay. 

Micah Zoltu: 
How does the execution layer know whether it's a canonical chain or not? Does that part of the request from this client in the current hash will be matching the current canonical chain. 

So if the latest head the execution layer has matches the parent hash of the incoming payload, then it's considered canonical chain and the execution layer is expected to execute it. And if the parent hash doesn't match, then the execution layer is not expected to execute. Is that accurate? 

Mikhail Kalinin: 
It may not execute. It doesn't mean that it's not expected. 
Yeah, there's no expectation. 

Micah Zoltu: 
So, um, when it receives a new payload that is not part of the canonical chain, how does it know when the appropriate time to switch canonical chains is? We don't want the execution client to just be stuck always thinking forever. I'm waiting for the next block above my current head and just never sees it because the chain forked and went down different paths. 

Mikhail Kalinin: 
Then you, um, will receive the choice update that switches you to the new chain and you will have to execute all the payloads from this side chain if they haven't been executed yet before updating the forkchoice state. 

Micah Zoltu: 
Got you. Okay. 

Tomasz Stanczak: 
So this would sound very similar to the current implementations of proof of work. I think at least that I might. So what we do is whenever we receive a block that will be on top then we execute it validated and receive something on the side chain, and we only start executing the entire chain of side blocks if the total difficulty becomes higher, which means this is like for forkchoice updated situation. So this will be fine, I believe, further on. 

Tim Beiko: 
So in terms of next steps here, obviously there's a small change we just discussed. Um, is it realistic that by the consensus layer call next Thursday we can have a PR that's like every client team has reviewed and we've either already merged or are ready to merge so that we can then kind of get to implementing the change, uh, across the clients? 

I guess another way to phrase this. Does anyone feel like the next four days next week is not enough time for them to probably review and think through the implications of this? Or is this pretty straightforward? 

Peter Szilagyi: 
I think the suggestion changes are mostly relaxing stuff, so, uh, wondering if a client doesn't do anything, I think they might still be. 

Tim Beiko: 
Got it right. Okay, so I guess in terms of next steps, just probably, uh, Mikhail just doing the clarification around like the canonical versus non canonical chain and um, then making sure that we get people to review it. But then we can assume that this general behavior is going to be going, uh, to be the actual spec. I guess the one thing their clients probably do all need to do is the renaming, but that's pretty small. 

Peter Szilagyi: 
So one, uh, question regarding this topic. I don't know if there's a discussion around testing or hive test or whatnot, but I think these interesting markets that uh, would be nice to have some high test for it. 

I guess the point would be that every client can decide exactly how they want to operate. But I think it would be nice to have the best suits for the weird cases so that at least they know what their client is doing in strange scenarios.

Tim Beiko: 
Yeah, that makes sense. Um, I'll reach out to the folks working on the Hive testing. 
Anything else on this PR? 

## Engine API: proposal for authentication
***Highlights***
- ***Purpose is to prevent someone from exposing their nodes and its consequences***
- ***JWT is the proposed method for authentication***
- ***Agreed to submit a PR and continue conversation with consensus layer team***

Tim Beiko: 
Okay, next on the agenda is a proposal by Martin around the authentication for the engine API and the consensus layer node. This seems like the last kind of feature that we haven't implemented yet. There was already some conversation on the issue this week, but Martin, do you maybe want to take like a minute to kind of describe your proposal here? 

Martin Holst Swende: 
Yes. Okay, 1 minute. One thing not mentioned here is that this would be on a new Port, so we would have the next Port after the one we're using already. On that Port would be the engine API and the other API. Because CL needs to talk to both of them. We want some authentication on that, mainly to prevent that someone just exposes their nodes to the Internet. Happens very often or mainly today, but the consequences could be worse with the engine API. 

The um authentication we discussed in Greece where we discussed several. One of them was JWT which is in the Http headers um token which is signed with a key that is shared with the El and CL. 

We could do other variations as well. Jwt is one of the options. If I want a strong opinion about this, please write them on the tickets. Um, I don't think we're married to JWT. It just seems like the thing we could use the um design as I said, is for just not any random stranger or web page being able to interact with it. It's not designed to be super robust in like wholesale environments where people can sniff your network traffic or whatever. 

Yeah, I don't know what else to say. I guess my minutes are up. 

Tim Beiko: 
I guess. Does anyone have thoughts or comments about this? 

Micah Zoltu: 
I'm generally a fan, but just to play Devil's advocate very briefly, the um Http and WebSocket have headers, but things like IPC do not have headers. Are we pretty confident we're going to stick with WebSockets for the foreseeable future? Is that not an issue? 

Martin Holst Swende: 
So the idea is that we would consider IPC and the actual WebSocket connection to be already authenticated because for the WebSocket that is handled during uh, the handshake and there is no JWT token passing during the actual WebSocket communication. 

So I don't look for a continuous Http dialogue that uh, we uh, continuously generate and validate JWT tokens um, sure. 

Micah Zoltu: 
So you're relying on the TCP connection being or whatever underneath um to be stable and secured in some way? 

Martin Holst Swende: 
Yeah. 

Mikhail Kalinin: 
I just wanted to say that this proposal looks reasonable to me and uh, it's like the um, minimal stuff to my observation that we can do and to get the desired result. 

Martin, um, what do you think about submitting a PR and continuing the conversation? 

Martin Holst Swende: 
Yeah, unless someone posted this and has other ideas here. Um, the next step I guess. Sure. 

Tim Beiko: 
Yeah, it makes sense to submit the PR and I think also maybe get this uh, in front of the consensus layer teams just looking uh at the conversation. I guess it doesn't seem like any of them have engaged and obviously they're not on this call. So I think once we have a PR just kind of shares it in the consensus uh Dev channel so that they're aware and can give feedback. 

Micah Zoltu: 
I do have one other question after reading through the comments. So um, it sounds like the plan is to boot up your execution client and it would print out a key and then go over to your consistent client and start the consistent client with that key. 

It seems um, like there is value in allowing the user to generate the key first and then start simultaneously with that key. 

Martin Holst Swende: 
So I think you missed the last part of the first government versus key distribution. The El and clients must accept the SEO config parameter JWT secrets. 

Micah Zoltu: 
Okay, yeah, I missed that. 

Tim Beiko: 
Anything else on this? 

Peter Szilagyi: 
I have a question. I'm not familiar with how JWT works internally, but am I, uh, right, assuming that there is no encryption involved here? 

Martin Holst Swende: 
Um, yeah, you are right. There is no encryption per se, aside from generating signatures. But they said that is passed, um, on JWT. It generates signatures for the JWT, um message that was passed, which in this case will only, um, be a claim. Uh, which is the IAT claim issued App claim. 

So the JWT will contain a JSON struct that contains information about when it was generated. That is just so, uh, we have some basic non-replayability. But we won't sign the entire JSON payload, uh, as the engine fault. 

Lukas Rozmej: 
One thing for me. Good thing you're mentioning that it will be this IIT when it was generated. 
Because I think without it we would be very vulnerable to someone spoofing this message and replaying it. 

Martin Holst Swende: 
Yes. In some sense, if, um, you want to protect against the tax vector that someone can redo traffic, then maybe, uh, we should do something more robust. 

Lukas Rozmej: 
Um, yeah, like randomly generated. Right. 

Martin Holst Swende: 
We might not even want to use symmetric keys. Um, we might want to, uh, sign the payload loads. Generally be more do something else. 

Peter Szilagyi: 
Uh, can't we just use DLS? Uh, just use Https for the whole thing with stuff. 

Martin Holst Swende: 
So then you would need a client certificate on the CLI. 

Peter Szilagyi: 
You, uh, could actually even do a share, so it's fine. Uh, it derives a server key. So, uh, essentially you would take the same. In your case, you had a symmetric key which was shared and you could just share this and just generate both the size of the keys and just cross authenticate the two clients with each other. I mean, they will be able to impersonate each other if you use a single lead, but that must be the problem we want to avoid. 

Martin Holst Swende: 
Yeah, we could definitely do that. Sure. 

I don't know, that might be problematic. If you want to host your El client behind an actual SSL Terminator, then you'd have SSL or SSL or something like that. But otherwise. 

Micah Zoltu: 
Having um, a little bit with both implementing JWT stuff is very simple, whereas implementing TLS is very complicated. And the nice thing about doing something like a JWT thing is you can just throw TLS, like a reverse proxy on the machine and you're done. Basically, anyone at the infrastructure level can add TLS pretty easily and the JWT part gives you that shared secret functionality. And then if someone wants to actually encrypt the traffic, that's generally, um, a solved problem in the operational space. I don't think the clients need to solve that problem. 

Martin Holst Swende: 
Yeah. In general also, uh, I think it would be easier to use an, uh, existing tool like, for example, curl, or maybe even using the browser to interact and use JWT tokens. But if you also need to add client certificates, um, it might be more problematic. But I don't know, I'm open to either suggesting really, um. 

Peter Szilagyi: 
It's safer to leave SSL to some other infrastructure. I kind of agree with that. Even when we have a lot of clients, SSL is not hard. Most modern languages have a proper library, so that one should really be an issue. Still, I can accept that maybe, uh, using some, uh, other wrappers or other infrastructure could be easier or more. 

I mean, everybody could get a puzzle together how they want. However, what I wanted to mention is that from a security perspective, I think it's important to emphasize that if you are hosting your clients on different machines, if you are actually legitimately going over the network and without encryption, I'm not sure that, for example, if you have, I really wouldn't condone using non encrypted network connections over the line. 

Martin Holst Swende: 
I think in practice most of these are going to be sitting inside, um, closed off network partitionings, um, CL and on the same place, not the same machine. 

Peter Szilagyi: 
Maybe if I have something really bad that I want to say, I can just bring it up again. It should be fine, uh, uh, because, uh, if you can misuse it, people tend to misuse it even though you really tell them not to.

Martin Holst Swende: 
Yeah, definitely. 

Tim Beiko: 
Anything else on the authentication? 

Martin Holst Swende: 
Not from my side. 

Micah Zoltu: 
Okay, there's a couple of comments that we can discuss offline. 

Tim Beiko: 
Yeah, I guess that's also, um, something that we can hopefully have resolved by the consensus layer call next week. Um, cool. 

## Tooling support for DIFFICULTY to RANDOM change
***Highlights***
- ***Comment on EIP 4399 proposing to have duplicate opcodes for easier tooling support for pre- and post-merge***
- ***Agreed to no current change to EIP 4399 and continue discussion on Ethereum Magicians***
- ***There are workarounds for tooling support with the current EIP 4399 proposal***

Tim Beiko: 
Next up we have to talk about, uh, some potential, uh, issues with regards to tooling that arise from changing the random opcode to difficulty. Um, do you want to give context to that?

Harry Altman: 
Sure things I wanted to talk about and said 4399, which proposes part of the merge, uh, to replace, uh, difficulty opcode with random. And, uh, basically my concern here is about. Okay, I had originally intended to come here saying, do we really need to replace an existing opcode rather than using a new one? Now that I've looked at it more, I understand why it's replacing the existing one, but this does raise some problems for tooling purposes for like, um, disassemblers and debuggers and anything that wants to report on there have been opcode renames before, certainly. Right. 

And those aren't really a problem because if an opcode just changes its name, you can handle that. But the problem here is that this isn't just changing the name, but it's also corresponding with changing the function. And so we have this problem that if you look at a chunk of Byte code and you don't know whether it was intended for pre merge or post merge and we want to disassemble it and report on it, do we say this is difficult or do we say this is random? And this maybe seems like a silly thing because, I mean, it's the same Opcode, but there's a reason that the name is changing and it is because that the meaning is changing and we would like to be able to do it as a purpose. Sorry, I'm kind, um, of repeating myself at this point. 

This introduces this problem of difficulty or that is the awkward solution. Uh, so the thing I wanted to suggest actually, and I would have put this, I'm sorry, um, I would have put this in my comments on EIP 4399 earlier, but I didn't because I only thought of it like an hour ago or so. 

I understand why difficulty needs to change random, but maybe what if, uh, there could be a second duplicate opcode for it? Like you could have difficulty changes to random, but also have a new one which is also random, and then we could just always call the old one difficulty and always call the new one random. 

I'll go actually add that comment later. Of course. Like I said, I, um, didn't mention this earlier because I only just thought of it. But yeah, I um, just wanted to bring up these difficulties and also that suggestion. 

Greg Colvin: 
That would seem like a better approach to me. I don't like seeing an Opcode change its semantics. It's, um, necessary, but it's still unfortunate. It would be better to deprecate it, but we can't do that either for some reason. 

Micah Zoltu: 
There's value in clarifying that within a given client, at a given, uh, point in time, the Opcode does have a well defined meaning. So in Nethermind version X, where version X is after the merge, where we're after the merge happening, the Opcode, um, does return random now, so we know from in that context. Within that context, we know exactly what return is, either returning random or difficulty, but never either or. I think the confusion for naming is primarily when you're working with tools outside of the clients. 

Harry Altman: 
Yes, exactly. Yes. Thank you for that Clarification. That is exactly the case. The difficulty, no pun intended, comes from working in context where you do not have that contextual information available about. 

Martin Holst Swende: 
Isn'T this thing also, uh, like a double wammy? Because not only do we have this opcode, which is now either one or the other, we also have this header field that's different. It's like the mix has mhm carries correct. 

Micah Zoltu: 
All of my types for my blocks are now going to be mix hash or random or whatever it is. 

Lightclient: 
Uh, not set as random, that's just set to zero after the transition. So it's probably okay to generally omit no. 

Micah Zoltu: 
Positionally, it's in the same spot, I think, as mix. Right, like the night or the 15th or whatever item in the block is used to be in the mixed hash. And it's now random. I'm taking numbers off. I don't know what it actually is. 

Lightclient: 
Uh, I thought it was set out 0.

Micah Zoltu: 
Anyone have a post merge block in front of them? 

Mikhail Kalinin: 
What do you mean? The mixed hash? Yeah, it's deprecated, but it's replaced with the random. Um, in this EIP. 

Mikhail Kalinin: 
Yeah. From structural point of view, it looks like it's just Renee and the content has changed. Um, but semantically has changed, but not like physically. I have a question too. Harry, thanks a lot for bringing this up, but um, what I'm wondering is, is there, um, an issue for assemblers and other tooling to represent this random value, um, or isn't it an issue at all and it's just an issue with respect to semantics, how to treat this up code, um, in the context?

Harry Altman: 
I don't know of any issue like the one you're talking about. I don't expect it to be. 

I, um, haven't looked into lots of detail about, uh, how exactly the randomness works, but based on what I know, I wouldn't expect that to be a problem. 

Mikhail Kalinin: 
Yeah. From this perspective, randomness is just a huge number. Much bigger than difficulty. Uh, say difficulty is bounded by the power of 64. Random, uh, is bounded to 256. 

So it's a number. It's still a number, right? 

Harry Altman: 
Anything happens to deal with Ethereum stuff has to deal with large numbers anyway. 

Mikhail Kalinin: 
Yes. As I understand the current semantics or difficulty of code, uh, it's allowed to, uh, return these large numbers if difficulty would hit these large numbers. 

So there should be no artificial restrictions, um, on the size of the number of uh, buyers in the response to difficulty of code and return value. 

I am just trying to understand the issue. So the issue is that, um, for the user who is using tooling, it will not be clear whether it's difficult or it's random. 

Rai: 
When, um, are you dissembling code without knowing the regime under which it was created?

Martin Holst Swende: 
But that doesn't actually matter because if you decode a contract, it doesn't matter when it was deployed. If you run it now, post merch is going to be give you random. But if you run it back in the day, it was going to give you the difficulty. There's no right way to do it really. I think we should just let it be.

Rai: 
Well, I think there's still a use case for disabling something in the regime under which it was created to recover the intent of it. Because maybe you want to understand how it works, but yeah, it's true. It's completely unambiguous how it's going to run now you just disassemble it under with the new semantics. 

Mikhail Kalinin: 
I should also say that you may actually distinguish whether it's randomness or whether it's randomness output or difficulty based on the value. Uh, because for the uh, mainnet and uh, for other networks, we assume that the um, main ad has the highest difficulty that is possible. This, um number is down to the power of two to 64. 

And for randomness out to fall into this range, into this lower range, there is a very, very low probability. So it's negligible. So basically, if that need be, probably two tools these assemblers make good from the value the uh, size of December. Whether, uh it's random or difficult, I don't know whether it's helpful or not. 

Martin Holst Swende: 
One more thing that I just came to my mind would be good to cross. The trick, as far as I know, with the change uh in Geth is we replace one of code with another uh, so the resulting trace will say random, it won't say difficulty. If we hit this code post merge, which is. Yeah, that might cause um, those positives uh in the processing. Unless other clients do the same, we can fix it. It's not a big thing. Just want to, um, put it out there. So our tracing, uh, will be correct. 

Harry Altman: 
Yes, for tracing when you have that information, it's not a big problem. 

Mikhail Kalinin: 
Yeah. One thing, uh, just came to my mind. These EIPS, uh, are currently in scope for um, the merge. And this is going to be may not change and other things changed if we decided to turn that um, test into proof of stake. So there will be like uh, one of the hard work and I don't think that who uh, may make assumptions on this or that goes without knowing the context, without knowing that this block is like from the mainnet or another testnets. 

But I haven't used the December and I don't know how do they work. So I would assume that there is a uh, context for the exact block and for the exact transaction that provide some information on um, payload execution. 

Yeah, finished. Just the point that I don't know if the context is provided for disassemblers. 

I mean the context for the EVM, uh and uh change that uh, and the EIPS that uh um, are taking uh effect for the blog that is being disassembled. If it's not the case, then. 

Harry Altman: 
Yeah, sometimes you have that information. Not always. 

Mikhail Kalinin: 
And so if you don't have this information, I would assume that you're uh, in the version that um is from the yellow paper, the original version of EVM without any change. 

Harry Altman: 
That is not an assumption I would make. 

Mikhail Kalinin: 
Yeah. I mean, how does other change to the EVM, uh are handled by this tool if there is no context? 

Harry Altman: 
Well, for the most part at least. So, speaking for truffles disassembler, like the way we handle it is mostly just to assume that until now this is basically this has never come up in a practical sense, obviously, technically every time you add an opcode you are changing an old Invalid opcode to a new function. But since we don't expect to encounter Invalid Opcodes, uh, other than the designated one at zero XFE, this is just not, um, really a problem and we just assume everything is the most recent version and that all opcodes that have ever been created exist. This is the um, first time that a Opcode would have its functionality and name changed in a way that is not from Invalid to valid. 

Rai: 
I still don't understand. When do you not know how you want to disassemble this? Either you're disassembling it how it was created to see what they intended, or you're disassembling it with the current rules to see how it'll execute. When is there an ambiguity for how to disassemble it? 

Someone is giving you bytecode and saying this was deployed at some point and you don't know the address of it? ..So you don't know what role said it was deployed under? Because if you're finding it from a deployed contract, um, then you can just see what the block is. 

Harry Altman: 
Wait, I mean, yes, sometimes you are disassembling bytecode that has not necessarily been deployed and just sort of exists independently of assuming it was compiled, which is usually the case. You can say what it was compiled for perhaps if you have the compiler settings, but um, you can't say what it was deployed to because maybe it wasn't deployed. 

Rai: 
So then you run into other issues, which is different, opcodes have been implemented throughout time and so if you don't know when, uh, it was deployed that your disassembler also could be redeemed Opcodes that are now valid and disassembling them into something that they were actually Invalid at the time of appointment. So this problem is not anything new. 

It seems like this, uh, doesn't make things worse unless I miss it from it. 

Harry Altman: 
This is not new in a technical sense. It is new in a practical sense. 
As you say, these cases exist previously with Invalid Opcodes, but I don't consider those practical cases, so I never worried about it before. 

Rai: 
Right. I guess I'm wondering, are there any practical cases even here when you add in the fact that usually you know what rule set under which you want to assemble this? 

Harry Altman: 
Well, I'm not sure I agree with that latter part. 

Rai: 
Okay, yeah, that's what I was curious about. 
Maybe there's something missing because I don't use this assembler ever really. 

Harry Altman: 
You may want to do this with a contract that has not been deployed and therefore the EVM version, uh, is not defined in that sense, although it could be defined in the sense of what it was compiled for, assuming you have that compiler information which you may or you may not. 

Andrew Ashikhmin: 
Um, so if you are investigating a code to be deployed, um, and uh, you don't know what is the EVM revision, then most, um, likely there is a high probability that it will be deployed later so I guess if you don't have, uh, an EVM revision, you can assume the latest EVM revision, assume post merge and say that it's Random, right? To my mind, it's like, oh, uh, you can be completely accurate. You can rename this if it's only about the name renaming its Difficulty or Random and let the user figure it out. So, to my mind, I don't see any practical problems apart from some confusing about the name. 

Harry Altman: 
Sorry, I'm trying to be a discussion going on in the text chat also. 

Martin Holst Swende: 
Yeah, I can say on the call I was just wondering if there's anything like practical we should decide on as an all core dev group or if, uh, we should just move on. I don't know if they're in the season. 

Harry Altman: 
I think that's the right question to ask. Um. 

Like I said, I made my suggestion before about perhaps introducing a duplicate Opcode for Random and that one would be the, um, designated new Random and the old one would continue to function as Random, but to keep the old name. And so I don't know if that's something that needs to be signed on right now, but I think that is the thing to decide whether to do that or whether to just go ahead with 4399 as it currently exists. 

Martin Holst Swende: 
So I would think that the current proposal is better because if there exists contracts which today in some way, shape or form rely on Difficulty to provide some kind of entropy, then, uh, they are better served with getting the new Random, uh, rather than getting old zeros or getting, uh, some, I don't know, Invalid Opcode error. Because we want to add to as little extent as possible screw up the existing contracts, which makes some use of Difficulty. 

Tim Beiko: 
Yeah, it seems like there's not a ton of desire to add a second upcode from what I'm getting. And, um, obviously anything more complex than that displayed in kind of the development process seems like it would delay things for not like a major fix. 

I'm kind of inclined to not make a change based on the conversation here. Um, yeah, we can obviously discuss this, discuss this, uh, more offline. But yeah, it seems like at least at the consensus layer, we probably don't want to change teams and obviously at the tooling, there's a few kind of workarounds it seems like you can do. 

Harry Altman: 
Yeah, I mean, we can come up with something, sure. But I came here, but since I work on this stuff, I have to come here to make the suggestion that will make my job easier, right? 

Tim Beiko: 
Yeah, fair enough. 

Harry Altman: 
Anyway, the comment that I said I should have written, I have now actually written. So that is now actually there on the Ethereum magician discussion for 4399. So that suggestion is recorded. What people will do with it, I don't know, but I wanted to at least come here to say this. I should have written that comments earlier, but I only thought of that particular implementation like 2 hours ago. 

So yeah, I think I've basically said what I want to say. 

Tim Beiko: 
Cool. Definitely. I guess, um, we can continue to thread on Ethereum magicians if people want to suggest more ideas there. But I think for now we can leave things as is and plan to deal with this at the tooling level. 

Yeah, and I guess on that note, we'll probably be organizing another merge community call in the next couple of weeks. So um, I'll make sure that that's something uh, we just mentioned in the agenda so that other teams are aware of this. Uh, cool. 

## Post-merge testnets
***Highlights***
- ***Discussion on which testnets are expected to stay running post-merge***
- ***Ropsten is large and will likely be deprecated after the merge***
- ***Goerli and Sepolia will likely continue and transition post-merge***
- ***An issue on Github was created to continue discussion on this topic***

Tim Beiko: 
So the next thing I had on the agenda ready to the merge is there's a few people starting to ask in discord what test nets, uh, if they're looking to deploy on that are expected to stay on post merge. 

Not necessarily looking for a full list and all decisions on them. But I'm curious just generally what people think. If there's one or two testnets, we do expect to be continued on after the merge and transition to proof of stake just so that we can point people in those directions as they're asking the coming months. 

Maris has a comment about the shadow for Goerli. I'm not sure if that implies we're keeping Goerli or not, but yeah, just curious, um, about people's general thoughts about that, like which Tesla should applications be using if they want to be like merge proof? 

Martin Holst Swende: 
So I have a question. As core devs, really is there anything from our perspective to be kind of gained from having testnets that are not following going out onto mainnet? 

Tim Beiko: 
What do you mean? I'm not sure I understand. 

Martin Holst Swende: 
So, I mean, is there any reason for us not to go full proof of stake on all testnets? 

Tim Beiko: 
Right. I think that the point is more we've discussed in the past, like say, deprecating Ropsten and I think we probably should run the transition on every testnet. But if we say want to stop maintaining Ropsten afterwards, we probably shouldn't be pointing people in that direction. But yeah, I do think there's not a big running to transition on all of them. 

Micah Zoltu: 
Um, I agree with Martin that I don't think we should be running proof of work testnets anymore. But correct me wrong, but um, running like a Goerli network is way easier than running a full multi client proof of stake network. So it seems like there is value still in having the simpler ones. 

Tim Beiko: 
Oh, you mean running? 

Micah Zoltu: 
I guess. Maybe not. Yeah. So Goerli is POA, which is simpler than POS, so it feels like it's value there, but maybe not. Maybe since these are public test nets we should be doing the whole thing and not half assing it. 

Peter Szilagyi: 
Uh, so the problem with keeping your functionality is um, that you need to keep for example, uh, certain legacy codes like legacy binding or legacy synchronization. All these code needs to be kept and maintained in the clients. 

Tim Beiko: 
Uh, yeah. Also there's stuff like the difficulty opcodes and whatnot that are just going to be weird. Oh, go ahead, Micah.

Micah Zoltu: 
The other argument here would be that Ropsten um, is our most bulky and problem ridden testing, which has value for testing specifically. If we clear it out and have a Greenfield, um, test net only then we lose that kind of ancient crusty thing that has potential to show up bugs that a clean green field test net would not. This is purely hypothetical, but if none of our testnets actually went through proof of work and then transitioned, maybe there's some bug in the future that only shows up on a network that went through the transition. And so it does seem like there's a little value, at least in keeping Ropsten. But I'm not married to it.

Peter Szilagyi: 
I don't think the proposal was to kill the oldest, rather just to transition them and does not support, uh, new uh, empty tests. 

Tim Beiko: 
No, sorry, it's not necessarily a proposal, but I guess people want to know which test nets will be alive, say six months after the merge. Right? I think it's pretty clear we should run the merge on all of them in case each of them kind of increases the odds we find an issue. 

But do we want to maintain the full validator set on Ropsten, Rinkeby and Goerli? And if that's the case, then great. We can just tell people the existing test nets are not going away. But I know we've discussed in the past potentially sunsetting Ropsten specifically and potentially other testnets. 

Peter Szilagyi: 
We discussed that, uh, Ropsten became a, uh, monster and at least in Greece, and said it was that we should launch uh, new testnets, but there is actually a new Pro testnets just I think there. 

Uh, idea was that Ropsten would be kept alive, uh, until the merge. We can also emerge just for the test, but afterwards it would be deprecated since it's just this huge file, uh, of Ropsten. The size is huge. 

I think the search is very hard for synchronized. There are only a few peers and it's not really useful for anything. So our idea was to just take this and switch to it because in essence it would be kind of like Ropsten just without all that crust. 

And at the end of the day, the question is what do you we can definitely keep the roster history just so that clients could use it as a benchmark for them to synchronize though maybe make that is suitable for that. Uh. 

Tim Beiko: 
That seems sufficient to answer people's concern. Goerli has a lot of activity and it seems like there's no reason to shut it down, so it's probably pretty safe. Ropsten might be replaced by Sepolia, uh, over time and uh, we maybe don't want people to assume it's going to be there forever. I guess the other one is like Rinkeby. Is that something you would plan to keep long term after the merge? 

Peter Szilagyi: 
It's hard to answer that question because it was managed by the Geth team. Uh, but I don't really want to be the person, uh, deciding whether to kill it or not. 

I think in general, um, I think in Bitcoin world, uh, they have some high regular tests and I think we could do uh, something similar just to, let's say every year start a new test and then uh, just start eventually start applications. Uh, because at the point where they just reach a huge size, it doesn't make any sense. 

Martin Holst Swende: 
Isn't the case also that reach all these testnets we need a corresponding Beacon chain. 
Do we have those?

Tim Beiko: 
We're going to need to set them up if we want to test the merge, right?

Peter Szilagyi: 
For Rinkeby and Ropsten, we would definitely need to set up their corresponding beacon chains. But after the merge is done, I would guess that if we ever uh, want to launch any business, uh, we have to have some appropriate tooling ready. 

Micah Zoltu: 
Can all the proof of authority networks reasonably go through the transition even though they don't really have difficulty? 

Peter Szilagyi: 
Well difficulty they do have because they have one or two difficulty on the blocks so the TDD can be used or transitioned. I am unsure about the mix I guess because uh, maybe click user. 

Marius Van Der Wijden: 
So we tested the transition yesterday on Goerli. Basically we deployed a beacon deposit contract and went through the transition and everything went fine. So we have now a network that is parallel to Goerli. And if we were to shut down the Goerli validators, then we would be able. It's shadowing the normal chain right now. 

Martin Holst Swende: 
One thing that might be problematic is currently if you want to use Ropsten and no one is finding it, you can just spin up a miner and mine your box and help out with it. As for the PoA testnets, there are various organizations that are dedicated running nodes in the Goerli and Rinkeby. If we switch to Proof of Stake and beacon, it's going to be harder to have them continuously work because if people want to test something they might deposit, they do their testing and then they stop running the node the test has become and after a while that's all dead validators. 

Micah Zoltu: 
We'll get lots of testing of bleeding people out. 

Martin Holst Swende: 
Yeah. 

Gary Schulte: 
Lack of finality. 

Pari: 
So currently with products we just make sure that the majority of the validators are on the entities we know. So all the time teams, EF. And if there are some operators from Lead, um, or other providers, um, then they run a bunch of validators. It hasn't been an issue that regular users are just running off their validators. And the general recommendation is once you've done finish your testing, you should exit your validator. 

Um, if you don't plan on running it, it hasn't been an issue on Plotter, but um, we can't guarantee that it won't be one in the future. 

Martin Holst Swende: 
I guess we'll see. Maybe it'll work. 

Peter Szilagyi: 
Either. You could have some special deposit contracts where essentially average users are not allowed to deposit. So you cannot add new validated, essentially just locking in the current one. That would be one solution. Um, a bit of a changing consensus. Uh, the other solution is that, yes, you could just say, okay, uh, if there are currently ten signers, and each of those ten signers will get 10,000 validators, and then, uh, average users will be able to create their own validators, but they won't be able to obtain so much to be able to make the tenant on the...

Marius Van Der Wijden: 
We can also modify the deposit contract so that it cannot be deposited into after the deployment. So we deployed with a set of validators and that cannot be changed. 

Gary Schulte: 
Uh, there would be a testnet where you could practice. There's a lot of folks who want to practice at home staking on something where there's not as much ETH on the line. 

Peter Szilagyi: 
A screen router deposit contract would a bit simpler, but it has a few risks. For example, if for some reason one of the signers or signers managers, uh, to get themselves slashed, they, uh, themselves cannot come back, uh, so that runs the risk of actually swallowing the network very long term. From that perspective, I think it's simpler to just go with the other approach, where you just create enough validators so that average users can still screw around, but they cannot impact. 

Micah Zoltu: 
Mhm so if we had to pick which of let's say we wanted to have, um, one public one "private" test that were private here just means limited validator um set. Which of the two, um Goerli or Segolia would be the public one? Which one would be the private one? 

Peter Szilagyi: 
Uh, you just create a large enough validator for, uh, your authorized signers, so that unauthorized signers won't be able to break that. 

Micah Zoltu: 
I see. Uh, I do have a medium strength opinion that we should have at least one testnet that actually does regularly suffer from failure to finalize and failure to come to consensus and reorgs and Forks and all the bad things. I think there's a significant value in seeing that in the wild, and a great way to do that is to not have well known validators let anyone who wants to validate validate, and people will disconnect and it will slowly get blood dry and it'll eventually fall out. All this stuff needs to be exercised, and I think should be regularly exercised. 

And so I would prefer if one of those test sets was not guaranteed up, so to speak. 

Peter Szilagyi: 
So I definitely agree that it would be super nice to have one of those testnets, but then that particular testnet that would be more like developer consent assessment, and would not be that developer testnet. And currently Goerli uh and Rinkeby, dapp developers rely on it. So Rinkeby goes down and 2 hours later. I've already uh, mentioned a lot of tweets that people aren't able to test their whatever. I think if you don't really want to mess around with a testnet that is actively live used to test that, you don't want to keep breaking that because then it just. 

Micah Zoltu: 
Is there any reason not to have one of them be that? And just the one that has the authorized stakers is the one we um, recommend to people for. If you want something that's always up, use this. If you want something that's going to battle test your UI and make sure it can handle reorgs and failures. Because I think there is value in Dapp developers being able to battle test their UI against things like lack of finality. 

Peter Szilagyi: 
So you have certain teams building on certain teams. It will be kind of like a rough pool if you're going to say that okay, now this network that you've been using for five years is going to be on schedule. 

Micah Zoltu: 
Okay, so how about Goerli and Rinkeby transition over and they continue to be authorized-ish like you described and then they do. Sepolia is our real world example of tire fire. 

Peter Szilagyi: 
I’m not against that because uh, that would work. But uh, then you don't really have that deprecation path of creating a new stable that's not so that eventually you can sunset the older ones. So I think it would be still uh, important to have a new empty stable set up so that eventually we can. 

Micah Zoltu: 
Got you. So ideally we would have at least at any given point in time, we'd have at least two of each one, which is the new one that's coming in kind of got started recently and then the old one of that type. So authorized users or whatever that is still running it'll run for a couple of years, but eventually we're going to phase it out. And then similarly you have two of the public tire fire test nets that kind of rotates every year or two or not at the time. 

Tim Beiko: 
Yeah, I guess we are kind of closing uh, in on time so we can maybe continue this. I'll uh, open an issue on GitHub, uh, and we can continue this async but um, it does seem like Goerli is already used by Prater. That seems pretty likely to keep going on it's. Sepolia is likely to stick around and I think we can figure out kind of the rest and like the broader strategy I think a bit and discuss it together on a vertical call. 

Peter Szilagyi: 
Personally, I would say that uh, it would have been nice to sunset Rinkeby in favor of Goerli at this point in time. For example during the Merge, it would have been nice to say okay, Rinkeby will stop or will not get merged just to reduce the burden of having to spin up a decent chain for it to be. I think the only problem is that it's a bit late in the game for that. So it's just telling people that, hey all your stuff needs to be ported over to Goerli ASAP. It kind of sounds nasty.

Micah Zoltu: 
We can just not merge it. People can still use it for testing most things. I just won't be able to test new functionality that comes with merge, which I think is acceptable. 

Peter Szilagyi: 
Yeah, perhaps. Either way, I think before we make any final decision on killing off any of the testnets or application them, we need a solid strategy on how to spin up a new post-merge testnet.

Tim Beiko: 
Yeah, that makes sense. 

## Shanghai Planning
***Highlights***
- ***Several external components of EIP 4444 have been, or is being, worked on such as developing standard format for scoring epoch blocks, archive nodes and methods for sharing information (not included in EIP 4444 itself)***
- ***Status on EIP 2537 will be continued on ethereum/pm repo in issues thread about including it in Shanghai***
- ***Introduced new EIP regarding EVM and strong desire to improve it***

Tim Beiko: 
Okay, we only have seven minutes left. There were two comments about people wanting to champion EIP 2537 and 2315. It doesn't, um, seem like there's I guess. Yeah, the two of them wanted to discuss this, but then there was also kind of a big question around 4444. So I think it maybe makes sense to just do EIP 4444 first. And then if we have time, we can kind of also touch on the two other ones briefly. Uh, but we've discussed those two other ones quite a fair amount in the past, so, uh, it's probably less blocking than 4444. Martin, you have kind of a comment about basically 4444 being a prerequisite for 4488. 

Martin Holst Swende: 
Yes. I'm sure everyone has read it. I just think that it's leaving a lot of details vague, and I think if we actually want to do 4444, the nitty gritty details are not an option. 

Tim Beiko: 
Yeah, there's a few people on the call who have been working on 4444. So I don't know if anyone wants to kind, uh, of share an update of where things are at then. 

Lightclient: 
I was just going mhm to say we totally agree. The actual is relatively simple, but there's a lot of external things that have to be worked on and are being worked on. So we are working right now with a contributor to develop some, uh, sort of standard format for scoring these sort of, like, epochs of blocks that will be provided over various methods. Right now, the main mechanism we're looking at is using BitTorrent to share that information, but I think there's obviously other ways, like the portal network, and we can potentially have mirrors set up. 

And then in terms of the archive node, that's something that we plan to work on in the next couple of months as well. So these are definitely the things that we're looking at. It's just not included in the EIP itself. 

Martin Holst Swende: 
Okay. I wasn't aware that they were in a group actively working on it. So from my perspective, we don't actually have to hash out all the details of this call. I just wanted to raise it, and I'm happy with that. 

Lightclient: 
Okay, we can try and be a little bit more public with these things. So it's, um, clear to everyone what's been working yeah. 

Tim Beiko: 
I think as soon as you have updates on the progress to uh, basically enable, uh, it would be great to share them on this call and uh, get feedback from client teams. 

Lightclient: 
Will do. 

Tim Beiko: 
Well, that was quicker than I expected. Alex, are you still on the call? Yes, you are. 

Alex Stokes: 
I'm here. 

Tim Beiko: 
I have some questions about the uh, BLS pre compile that you wanted to ask also time teams because you're looking at championing that. 

Alex Stokes: 
Yeah, that's about it. I just wanted to ask client teams on the uh, call sort of where their status is. For context, I think most of us are aware, but we had this EIP 2537 for BLS pre-compiles, and it essentially almost went into London, but then was deprioritized because it's 1559 and then now the merge has been pushed to after the merge. And yeah, we'd like to consider it for sharing high inclusion. 

And the first step I think is just getting a sense of where it's at. Things may have gone a little stale since people were lost actively looking at it. So if anyone knows of anything blocking or any potential issues, it would be good to know about them sooner rather than later. 

Tim Beiko: 
Cool. And I guess the best place for that would be there is an issue on the ethereum/pm repo about including 2537 in Shanghai. So it might make sense to just if clients have issues or concerns to just share them in that thread. 

I'll post a link in GitHub and it was a comment by Danny and that thread as well that um, a lot of the libraries have been tested and are being used in production on the consensus layer side. So we do have more data on that since the Beacon chain has been live for a while. 

Marius Van Der Wijden: 
Um, there were two things that I remember from the last debate that were still open. And the one thing was this EVM 384. I think that's not coming, so I would be fine with 2537. 

But the other thing was it introduces nine pre-compilers, I think, and there was some discussion that we might not need all of those nine pre-compilers. And so it would be really cool if someone could describe why we absolutely need these pre compiled for each one of the pre compilers. Or if it makes sense to just, I don't know, do the three most important ones that we actually need for building stuff on them. That's it. 

Alex Stokes: 
Yeah. Unfortunately you kind of do need all nine. There are a lot of different operations. 

Tim Beiko: 
Okay. 1 minute to go. Greg, you also had a comment about the EIP. Are you still here, Greg? 

Greg Colvin: 
We're out of time. But that and the whole set of EVM changes is there and I'd like to keep it on the table and discuss it because I and I think the other people never want to go through years of work to have the whole thing fall apart on the day of shipping. 

Tim Beiko: 
Right. And you had a comment on one of the open issues about the different EIPS for the EVM and how they relate. 

Greg Colvin: 
Yeah, there's basically an order in which there's an order of dependencies there. 
And for 2315, there's specific changes to answer criticisms that did come up literally at the last minute. So I've made changes to answer those and introduced a new EIP to answer some of those. 

And, the EIP that the other people on the foundations EVM team are also related. So, I just like to see some commitment early on that we're moving on with improving the EVM or after six years deciding that no, we do not actually want to fix the EVM unless quit wasting time on it. 

Tim Beiko: 
Right. 

Greg Colvin: 
I'm serious. I'm pissed off. I'm sorry. We put many years into this to make no progress. 

Tim Beiko: 
Yeah. And I think there is that desire that's been mentioned by many people to improve it. I just think your comment helps kind of untangle the different proposals and sort through them. It's probably unrealistic to have all of them go in the next upgrade, obviously. But hopefully this can help us prioritize. 

Greg Colvin: 
Yeah, um, that's the point of getting them in the order of dependencies. 

Tim Beiko: 
Cool. Anything else anyone wants to share? Oh Mikhail, you have your hand up. 

Mikhail Kalinin: 
Yeah, I have a very quick announcement. The Engine API authentication exchange and optimistic syncs back. Other major things that will be in the next merge stack release. We are aiming to iron this out during the next week and do a release after that. We will have, like, a time for engineering and then DevNet and then replace the new one. Correct me if I'm wrong. 

Martin Holst Swende: 
I don't see any problem for one month longer or whatever. One release, we still serve it on the old Port to reduce any problems with deployment. 

Tim Beiko: 
Yeah, uh, and I think once the new specs are out, then we can't probably discuss a more specific testnet plan on the consensus layer call next week. Short term testnet plan. 

## Open Discussion
***Highlights***
- ***Ethereum Cat Herders’ 3rd Year Anniversary***

Tim Beiko: 
Cool. Anything else before we go?

Pooja Ranjan: 
I would like to take a moment to thank the community. Ethereum Cat Herders are celebrating the third anniversary with Ethereum blockchain. And, yes, of course. We would like to take this opportunity to thank the community. And, we look forward to continuing supporting the Ethereum ecosystem. Thank you. 

And one more thing. We have published a blog with all the tasks that were done by the cat herders in terms of protocol support and education and everything else. So please check out cat herders' Twitter. 

Tim Beiko: 
Cool. Thank you for sharing. 

Thanks, everyone, for coming on. And I will see some of you the consensus layer call next week and everyone else, two weeks from now. Right. Have a nice weekend.

-- End of Transcript -- 


## Attendees (32)
- Mikhail Kalinin
- Tim Beiko
- Rai
- Lightclient
- Pooja Ranjan
- Marek Moraczynski
- Greg Colvin
- Trenton Van Epps
- Harry Altman
- Peter Szilagyi
- Lukasz Rozmej
- Martin Holst Swende
- Bhargava
- Jiri Peinlich
- Sajida Zouarhi
- Marius Van Der Wijden
- Vorot93
- Gary Schulte
- Andrew Ashikhmin
- Fabio Di Fabio
- Fredrik
- SasaWebUp
- Alex Beregszaszi
- Guillaume
- Danno Ferrin
- Protolambda
- Pari
- Micah Zoltu
- Sam Wilson
- Alex Stokes
- Appleyard Vincent
- Henri DF
