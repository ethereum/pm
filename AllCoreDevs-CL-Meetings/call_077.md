# Consensus Layer Call #77 Notes
### Meeting Date/Time: Thursday 2021/12/02 at 14:00 UTC
### Meeting Duration: 1 hour
### [Agenda](https://github.com/ethereum/pm/issues/429)
### [Recording](https://youtu.be/1fIg_t6hZ8U)
### Moderator: Alex Stokes
### Notes: George Hervey

***Summaries and highlights were curated and modified from [Quick Notes](https://hackmd.io/@benjaminion/S1trJ8UFK). Shout out to Ben Edgington. Thanks.***

## Intro
***Summary***
- ***Arrow Glacier hard fork on Eth1 next Wednesday: update your Eth1 nodes!!***
- ***Updates to consensus layer specs: v1.1.6 - fork choice fixes are in.***

Alex Stokes:
Test test, test. 

Tim Beiko:
We are good. The audio is working. Sorry about that guys. That was my fault. 

Alex Stokes:
Yeah, if you want to just, oh, that's okay. Yeah. Yeah. I'll take it from here. Great. Cool. Okay. Thanks Tim. Everyone. Let's see all, reposts. Oh wait, sorry. It's lagging. there we go. Okay. I had the YouTube open and it was right. My systems, okay, good. Okay. So everyone, there was some technical difficulties as well. We are not going to kick off the, the consensus layer call 77 and let's see what is going on today. The first thing I wanted to say, I was just to call the Arrow glacier hard fork. So this should go live next Wednesday. And it's important for everyone listening and everyone here to upgrade your ETH1 nodes, especially if you're validating. So I'm sure you've, I mean, at least, hopefully by now you've heard this many, many times, but, very important that we all upgrade. 

The next big thing would be updates to the consensus layer specs. I was going to call these out really briefly and then we'll move to Kintsugi so in terms of the consensus layer specs, we have these new updates. 116. I know pari, and again, we'll get into the merge stuff in a second, but, it brings fork choice updates, definitely including this proposer score boosting, which helps mitigate a reorg attack. So that was really cool to see. And I just wanted to give a quick shout out to the Stanford team at David's say's lab because they've been helping with a lot of the fork choice analysis there. 

## Kintsugi office hours
***Summary***
- ***v3 of the Merge specs just released. Validation errors are more expressive. Minor updates to Eth1 EIPs. Engine API update to alpha.5. Devnet-3 will target these specs.***
- ***Marius has been organizing mass Merge testing.***

Stokes:
And then from here, I think we'll officially transition into the Kintsugi office hours. I think there's probably a lot to talk about today. Let's see. I'll just briefly touch on the specs and then we'll talk about dev nets and updates there and then, kind of move into a more open discussion. I think Mikhail had some stuff you wanted to talk about that we can get to in a second. Oh, I see. Okay. Sorry. right. So Kintsugi, so important here, we have the version three of the specs that were just released. Actually let me post a link in chat. 

But essentially each of these specs are mirroring Devnets that we've been doing. So it's very exciting to see the progress there. there's a link to the spec and yeah, so V3 a number of things, updated this notion of a validation error. So that basically, when the execution layer doesn't like a block for some reason, the consensus layer now, like has a much clearer idea of like what's going on or at least that error is now like a lot more expressive, some minor updates to the EIPs, both for the transition process itself and for how we're handling the randoms off code. So it's 3675 and 4399 that cause this X themselves recreated 216 that I just mentioned a minute ago. And then last we have the engine API that was updated to version one alpha five. So, lots of fun stuff there. And we should have a dev net three for next week. That's going to target those specs. And we can probably talk about it a bit more in a second before I move into devnets. I did want to say, one more shout out to merge testing. Marius has been rallying the troops. So thanks for that. I think there's been a lot of inbound interest, for testing, which is super important and it's again, just really exciting to see, see that set up. Yeah, zoom claps.

### Merge-devnet-2
***Summary***
- ***Devnet-0 was broken by running two sister blocks with TTD. Half of consensus clients chose one; half the other. We need to be able to handle this, and be able to override the terminal PoW block hash as well on the consensus layer. [Mikhail] The first PoS block proposer should sort this out - the network should not split over this. However, something went wrong… It’s still running and is available for a post-mortem.***
- ***Devnet-1 had a bug in Geth.***
- ***Devnet-2 is running well. Hit TTD and switched to PoS 2 days ago. Making deposits for new validators is fine, and lots of testers are sending Txs. Things are looking fine. Teku joined and is proposing as of yesterday. Lighthouse has a majority, other clients allocated 5% each for now. No blocker to making this equal between clients.***
- ***Marius got all 5 consensus clients working with Geth to follow the chain.***
- ***Teku–Nethermind is not working currently - Nethermind to investigate.***
- ***Devnet-3 next week will target v3 specs.***
- ***Kintsugi testnet launch targeted for the 14th, and plan is to run it for a longer period of time.***

Stokes:
Okay. So from here we can move to devnets. We've had two devnets so far with a third one planned for next week. dev net one, I believe was broken again by Marius. I think he ran two fighters. I don't know if you wanted to give her an update as to what happened there, or if anyone here on the call does. 

Marius Van Der Wijden:
So we already have three devnets, I think. We started with zero, which was brought in pretty quickly. And, then we had devnet one, which was broken by, mining food terminal difficult, two blocks, two sister blocks with terminal difficulty, half of the consensus layer clients, that was one block and the other half crossed the other block. And so it was not possible for the execution layer clients to move to the other block. And, so I think the way I see it, this is something that the consensus layer clients should, should take care of. and they also should implement some methods to at least manually specify which block hash they want to be for proof of work block, so that we can mitigate these issues a lot more easily. 

Alex Stokes:
Right. I definitely want to see, you know, testnets with multiple miners, especially as we get closer and closer to the merge, but I think for now we're just, ensuring there's only one miner for merge transition. Is that right? 

Marius:
Yes. So that's what we did for the third test net. I like that we have two miners running and I stopped mine right before the transition, so that transition will not be affected by it. but yeah, we should, we should definitely, talk about this at some point and, and test this in the future. 

Mikhail Kalinin:
What would be the case you think that the term “ELblock hash” will be useful for? 

Marius:
if we, if we, if we reached a terminal total difficulty on our note, we were w w the, consensus layer note, we'll see, okay, this is, this is the, terminal proof of work block. And it would say, okay, if he's built on top of this terminal, and, the, the issue is that it's the consensus layer in two groups, one group that builds on this one block and the other group that builds on the other block. And, it, it's not possible for them, for the consensus layer clients to switch the chain that they're working on, or at least, I don't know if this is like, so from, from what I see, there's no way to tell the consensus of layer client, “Hey, you should be following this chain.” And I think that would be, the use case for the terminal proof of work, hash would be to say, Hey, we, we, we just merged. 

And we, we all agree that this is the hash of the terminal, proof of work block. Now I can go to my, to my node, that is on a different chain and say, no, please take this, another, another, another idea would be to not, to not immediately build on top of the terminal proof of work but to wait, eh, like couple of seconds until, the, the, the execution layer stabilizes and one proof of work. But, I think, that's just a hacky solution and we should definitely create a way for the consensus layer to pin a certain blockhash. 

Mikhail:
Yeah. But yeah, I see. So there are two terminal blocks, right? And the first group is, or the proposer of the emergency physician block, is about to, peak, the one, right. If it's not, if it's accepted by the network, then everything is okay. And the next walk should be built on top of this merge transition block, but it's not accepted. Then the next proposer will try to produce an ever pros and out of one there's a transition block on which you may use it, it may use another terminal block as well. So it's not, it should not be like, she knows it goes and displayed in the consensus at block. So I'm just trying to understand why this has happened.

Marius:
I see. Yeah.

Mikhail:
Yeah. When we do, we may go offline and discuss this. 

Marius:
Yeah. I agree that it should, it should not happen, but it did. So some things from, 

Mikhail:
Yeah. Then I would like to hear from consensus layer implementers. And for that, there is, well, the test happens, but the let's do this offline, 

Parithosh:
Just so you just get information that hadn't done that and that zero and that devnet is still running. So if someone wants to figure out what actually happened, I can give you all the details and access if you're in.

Marius:
I just showed zero. I think it was one that we rescued.

Parithosh
One. We had the issue that there was the wrong EIP. 

Marius:
I thought we had, we had, no, yeah, sure. 

Parithosh:
One was to get and two have no issues. 

Stokes:
Okay. So either way, the intention, I think we all agree is a reorg and this be possible. And then right, you end up with a financial externalization through the merge, and then that gives you, you the one chain. So definitely something we should track down, here's your test, something to keep, keep, keep it, you know, aware of. And Pari, so that's, devnet two is going well?

Parithosh:
yeah, just to pick up on that thread. and that was going well, we switched, we hit TTD, already two days ago, I think, it should appeal as expected. We have random users making deposits. I've been able to make deposits and get validators active. So everything looks good, we seem to have a lot of people from, from the testing efforts using the chain now. And so far nothing's broken, so that's a good sign. And I think it will also joined, in proposing and testing yesterday. So we should have a higher participation rate, so that everything's looking good for my seven actual 

Marius:
Quick question. Did you change the amount of, clients from each team between devnet 

Parithosh:
Then, what I've done is lighthouse gets maturity so that we at least would find the nice and everyone else gets an equal amount. So I think currently it's 5% each or something like that. I can send you the transmitter, But I'd like to slowly take that away right now with getting that security, that that is one stable base, but in maybe already in the next step, and I won't have a majority client and just to, two clients that are majority together or something like that, 

Marius:
I also managed to get all five consensus layer clients working together with, Geth on, on, on validating, on following the chain. 

And, so, so we're, we're pretty good. And on that side, 

Parithosh:
Yeah. I don't see any big blocker and just having everyone on the run, an equal number of validators right now, like a checkbook. 

Adam Sutton:
Yeah. I see. Tickled and geth has been working well since we got that. So did this morning. I haven't been able to revive the check, you know, Nethermind typically sends, excuse me, which is from the canonical training should be valid and out of mine keeps saying it's invalid, or I'm not quite sure why I need to optimize to get the actual responses, I guess. 

Marek Moraczynski:
Yeah, I can take a look. Mikhail, we can talk about it after the call. 

Alex Sutton:
I will probably be asleep after the call. If you can take a look during your day, I'll pick up on it. 

Stokes:
Cool. So things are on, yeah. And then just looking forward to the intention, and I think Pari's the main driver here. So hop in if, if some exchange that I believe the intention is that three, for next week, which will target version three of the specs. I mentioned, incorporating the learnings from all the previous test sites and, yeah, maybe we'll, change the value distribution and move closer and closer to Kintsugi. Which speaking of, that would be the next testnet plan would be the week after on the 14th. And, yeah, that one would be this longer standing public test. That's, hopefully more stable than the dead that's so far. And, yeah, a great opportunity for us to demonstrate merge readiness. So everyone, I'm sure, is looking forward to that. 

## Client Updates
***Summary***
- ***Nethermind: Devops team is writing some docs on how to run with various consensus clients. Also testing merge MEV plug-in. Fixing interop with Teku and Nimbus.***
- ***Lighthouse: Merged Kintsugi into “unstable” branch today; should migrate to “stable” in a couple of weeks.***

Stokes:
From here, we could do client updates. If anyone from the client's team, sorry, this is his team. Our execution team wants to give us an update. We could do kind of a round Robin thing. there might not be anything beyond what we've discussed previously, so no pressure. 

Marek:
Okay. So Nethermind, our dev ops teams working under the document, which describes how to run different combinations of clients with another mind. We are cleaning up our cart and doing some fixtures. We need to investigate, issue with Teku. and I think the same is with Nimbus. and we are going to adjust Nethermind to the new version of spec.  In the meantime, we are also testing our EMV blocking with the Merge. It will require some fixes from us and yeah, and that is everything from us. 

Stokes:
Thanks. and that actually does bring out important points, everyone here, like, please, please, please document how to run your respective clients on these house nights. Cause, yeah, the intention with Kintsugi, that is to get more community involvement. And so, you know, if you need to go to a particular branch and like to have a, you know, different sort of a command line interface and all of this, that's fine. but docs will help that process along. 

Age Manning:
Yes, I guess that's a point for Lighthouse. Today, we had all our code in a separate Kintsugi branch that we measured it down into our unstable branch, in probably like a week or two we're planning on doing a proper release. So Kintsugi should be introduced in April. So at the moment, all, all of the merge code is in “unstable”, which is a small change. 

Stokes:
Great. Any other client updates? just to give everyone a few seconds, otherwise we could hop into a more open discussion. Mikhail, you had some questions here. Would it be a good time to discuss those? 

Mikhail:
Sure, if there are no more client updates, we can go through these items quickly. 

## Other Updates/Discussion
***Summary***
- ***Proposal to add engine_getBlockBodies bodies to API.***
- ***If the execution client is offline, you would be unable to serve blocks to other clients (might result in being downscored in gossip).***
- ***Optimistic sync: what should a validator do while the sync is in progress? Is it allowed to attest while syncing? Probably should not be attesting in this case. Need to analyze how it affects safety and liveness if we allow it.***
- ***Transition edge case scenario. Some execution clients might have changed their fork choice to PoS. Please review the issue and add any thoughts. Mikhail plans to close it next week.***
- ***Optimistic sync specs: Proposal for a cleaner separation of concerns around: (1) explanatory material, (2) spec requirements, and (3) implementation details.***
- ***Noticed when switching between consensus clients, they all try to import all the blocks again (leading to re-execution on the execution layer). Optimistic sync should fix this. Please test opt syncing not only from beginning, but also when switching consensus clients.***

Stokes:
Sounds like we're good. 

Mikhail:
Okay. Yeah. So first thing, this proposal to add bodies or bad to say, get payload bodies to engineer, it allows for pruning or, transactions from, from, execution payloads on the sales side and request them at hook, on credit amount, on demand from execution left side, it's pretty cheap to do it to, yeah, so the basic idea is to just, at least have a list of block hashes, and to execution with clients and it's will respond with, a list of transactions, in the format, which is used by consensus layer to store those transactions. So this is basically the idea and to utilize this method to consists our clients will have to, like when, for instance, certain blocks or their network, they will have to, yeah, a bunch of bigs then iterate, through all this big and blocks, grab, block hashes from bigs. 

You should pay a lot of structure and send it to execution layer clients, get back with, transactions, like add these transactions to, or replace the transaction routes, with, the actual transactions in the execution, a very long structure. And, yeah, sir, send this back to the PA did their metadata has requested this, this big inbox. So that's the idea. And my question, my main question is, like, does this beneficial, this particular implementation of pruning, as it's beneficial for, is this for clients, if it does, then I will open a PR next week. So if it's not, it doesn't make sense to do anything. And, yes. And also, for instance, yeah, the concern, that like we use block hash as then the execution layer, will not be able to use some optimizations, like if, blocks at a store leading narratively. 

So it will be a much less intensive in terms of this access is to, request two to query blocks from it's execution where by block numbers. so this was one of the concerns, which is in the threads. So you could see it and yeah, why, why it's wise to be down this way, because these methods in engine API, their logic is basically well, math maps on the existing ad block bodies matters, in DTH sub protocol. So if you have any concerns and you don't think that it's beneficial, just chime in and drop, and like, let's say this in the discussion threads, otherwise it will just open a PR. Anything to discuss here right now? 

Adam Sutton:
Sorry, I haven't seen the issue, but has there been thought put into what the consensus lite client do if it's EL is offline and blocks are requested of the network? 

So an obviously request comes in this that's kind of a new way that you don't have bodies available anymore. Comp services obviously, requests if we normally get, right?

Mikhail:
Right. So it will mean that you don't have blocks that you have been announced, right? Like you haven't announced that you are, you are it's a lot. 

Sutton:
Yeah. 

Mikhail:
See, yeah. That's great. 

Sutton:
And you are at fault, so it's not the end of the world, but I don't know. 

Mikhail:
Yeah. So if, if your EL is applying, you probably will have more server issues, than this one. 

Sutton:
Yeah. That's, that's true. it just means that you'd be likely to those peers and possibly, and for a period 

Makes it hard to recover when it comes back. 

Mikhail:
Okay. So yeah. Any, any opinions? Yeah, just welcome to this issue. Let's continue it there. Good. And the next item is the, is about the optimistic sync. the question is what should validator what should not, or should validator do, when the optimistic sync is in progress. So, the particular thing is a test and should a validator attest, while the sync is the optimistic sync is in progress. And it's not yet finished, like imagine the case when, the optimistic Hab yeah. There was the optimistic and everybody's voting for it and the, you can receive, receive and process those that attestation simply works well. but, you have also be like fully verified has, which is, the block, prompts the canonical chain. The latest, the most recent block run pick a canonical chain that you have verified the execution for. 

and like say optimistic cat is 10 blocks after this one. So what to do here, can be should the validator attests to fully verified block or should or should know the desk. there are a couple of like related issues to this problem because there is also an edge case during the transition, but in general, I think that, at best, and in this case shouldn't be done because, this fully verified hash is by a, is dictated by the optimistic heads, the ability to do, which is not yet approved. So, yeah, just wanted to highlight the thing and, let me draw the issue here. Everyone is welcome to comment as well. So this was like one of the tricky questions. If people have any strong opinion, let's discuss it now here. 

Stokes:
It feels like to me, validators should wait until they're fully synced. Otherwise it kind of opens the door to this, almost like lasered out there, lazy validator setting where you're just kind of almost blindly signing or you don't quite know, what, what actually is going on. and it also, yeah, it would let you have a node that is not fully synced to the specs execution layer, and that's definitely not what we want. So, my gut says to forbid this. 

Mikhail:
Yeah. Yeah. I think that's, first of all, it's, if the blog is fully verified, it might make sense to invest it, it contributes to the Kintsugi probably, but, my opinion, again, open some, it can increase them attacking surveys. I'm not sure that any disaster can happen if there's the test to, while the optimistic seems is still in progress, but this is definitely a change of the status quo. And, yeah. if we, if we do this change, we'll need to reason about it. How does it affect the security and bindness safety environment? So this is my gut. 

Okay. It's not that nobody wants to share. That's the last one. The last one is the last item. This is the, yeah, this is the edge case scenario, around the transition. And let me just try to give a context on it. So there is the first the merge transition block, geared into the network and it signifies some terminal block. So some, some specific terminal block and, yeah, it's been, it's transitioned block has been created, sent to the network, but eventually it's been, it has been not accepted by the network participants for some reason. So it hasn't become to have, all the chain and, and another proposer, like, let's say that it, it proposes some top of the, parents of these transition block and, like it may propose like, it is blocked with an empty payload, which will delay a legal case. 

So, and then, yeah, the issue here is that part of the, of the nodes can receive this transition block and switch their fork choice, rule to do the proof of stake fork choice rule.  The fork choice rule of execution layer clients, via proof of stake fork choice rule, and the question actually other, do we want to like revert the switch if, the next block after the merge transition block is coming with the empty payload? So this is very much of an edge case, and I think that we should not do anything. So once the fork choice rule has switched, it should stay there. the implication of doing it, of doing nothing in this case is that, some proposer it's the terminal proof of work block and it's like kind of dictates this terminal before block by sending this merge transition block and other nodes that, have attest this transition block will just let's say that, well, we'll just set their terminal log to a specific log that has been picked by this proposer. I'm not sure that if this like really quick explanation, so yeah, just merge this issue and probably read the thread before I understand the context and then the aim close this issue, like, early next week, if, often will happen. So be it will just stay there. A logic will stay for now currently in this stack. 

Stokes:
Yeah. That's all I have. Thanks for listening today. Yeah, thanks. I'll have to look up the specific issue and get caught up to speed. it's seems like we don't want to kind of roll back, going from proof of stake to proof of work fork choice, with, I guess the only caveat being, if there is a reorg, around them transition point, but, yeah, I'll take a look and anyone else who's interested on a call should do the same. 

Okay. I think that might be everything I had on the list for Kintsugi. Is there anything else anyone else would like to discuss, bring up, talk about while we're here, anything with dev nets or the testnet . 

Dustin Brody:
Yeah. I'm, interested in and sort of aspects of actually optimistic sync. and so I've been looking at the, the current, I don't know, specifications such as they are kind of mix a specific implementation, have a goal with, various ways of achieving that with a specific or with a goal itself with a broader goal. So, the broader goal of separating the EL from the CL head know granted, the specific optimistic sync homepage and the network of hackMD pages around it discuss a really specific implementation and the Kintsugi specs are written to mandate that specific implementation. and to give a specific example of what I mean, the yeah, okay. Link here. This is just one of the, the implement. The agent gets eight implementation requirements of which the first four, are pretty, I would say, broadly applied to anything that can call itself optimistic sync. 

The last four are really specific to, one approach to implementing optimistic sync. This wouldn't be a problem except that the optimistic sync documents all combined this several aspects, how to implement that specific, version, approach, the, what is the sort of an explanatory aspect of what the purpose of optimistic sync is? What is the design space of optimistic syncs on the discussion that was just had about, can you attest based on an optimistic hat, what are the useful points in the design space? What are, and what is useful or reasonable to require in the spec? And so those are, and those are all kind of semi randomly intermixed. And so what I would be what I would like to see, I guess, as an outcome is for some as it moves to being a little bit more finalized, you know, to contribute this back to the merge spec, to the, for this to be separated out a little bit more cleanly so that there's a specification, so that there's extended splendid standalone explanatory part. there's a, what does a spec require, in a way that is a little bit more separate or independent and implementation, and sure. If one wants to implement a specific type of optimistic sync, well, what, what are some hazards one might look for? So that's what I'd like to see. 

Stokes:
Okay. Yeah, I hear that. That makes sense. I think Paul wrote this document and I'll think he's here today, but yeah. Especially if we upstream this Kintsugi specs or any, you know, further merge specs, we can definitely keep that in mind. And, yeah, if you see something in the future, I'm, I probably would be greatly appreciated if you see a way to approve that. 

Dustin:
Alright. and so I have final point, related to this and add to motivate this a little bit and to like, why should one care potentially about like, this is aside from sort of inference civil, that the aesthetics of specifications, is that there's .5 in this, list that I linked, add the ability to allow us to explode if a finalized block has an invalid execution payload and elsewhere talks about this kind of situation requiring a social consensus and the like, well, that's a specific artifact of that particular sort of, optimistic sync where the chain itself, where you're fully import a block. One can talk about an optimistic sync where the fork choice is allowed to run ahead, but the justification and finalization in spec terms is not in the same way. and so, just as, as one example, and that would size up the particular hazard there. but it would simply never finalize on those blocks, so couldn't happen. So yeah, that's it. 

Stokes:
Okay. I guess I'm a little confused, cause I feel like you're like the fork choice is rooted in finality and then by justification. And so I feel like as you're processing the chain that you received, you would always see that. but yeah, maybe I just didn't follow what you're saying. 

Dustin:
Okay. Yeah. So it was not super clear. Okay. So the notion of having, the notion of, of one can, okay, how maybe put it this way, what can imagine it an optimistic sync implementation, which does not ever fully trust, in it's most that only in some sense fully finalized this, in, in the sense that it's willing to, that ever would have to be back rollback back or could ever interfere, a verified block. I'm not saying as well, you know, we consider and how to articulate this, but, at, at another point, but essentially this assumes that you kind of mix kind of fully trusted and not fully trusted walks, and that the client really commits at any, in any real way to not fully what's to call the verified blocks. And there's no strong reason for that to happen. And I can tell. 

Stokes:
Right. Okay. Yeah. I mean, I'm happy to keep chatting, but perhaps we should take it offline just to check everyone's time here. And, yeah, but definitely I think, you know, I think we all strive for aesthetics and specs. I do think aesthetics are important. and yeah, if we can refine this and separate the layers very cleanly, I think that's a great idea. 

Mikhail:
Yeah. To add that we work on the optimistic sync spec is in progress. So it should be like the minimal set of requirements, for CL to do it in a safe way. So it's basically going to be based on the idea. So from this document that you have, that Dustin has just shared is written by Paul. 

Stokes:
Great. Hsiao-Wei, I saw you have a link here to talk about the issue #430 on PM. Okay. So right. If we want a B starting in, should we open up this conversation right now? 

Hsaio-Wei:
Yes. So then let me send you the link to follow up our previous discussions about, 

Marius:
Sorry, can we, I have one quick topic before we go back sharing about, about naming the merge. 

One thing that I noticed, it's right now, when I, when I, switch between clients with the same consensus layer with the same execution other clients, actually try to, import all the products again. I think that that's something that will change with optimistic sync. I just want to make sure that if you guys boost optimistic sync, you should also test just, not only optimistic syncing from, like the beginning, but also from like an existing, so you shut down your notes, and you, you rerun the same execution after one hour or something. And also you have a pair execution layer consensus layer client. You shutdown the consensus layer client and you start up a different consensus layer client. And I think that that should be something that we should really look at to make sure that these use cases, sufficiently supported. 

Mikhail:
Yeah. There is, by the way, I think it's fine because you can just, this client doesn't know, the state of the exhibition where clients, like, if it's, close to the hat of clients while consensus layer client is not. So it will just keep syncing and send all the same blocks  if, if this is the case he has described. So I think it's okay. 

Marius:
The problem is that, like, if you, if you input, I don't know, like a, a day worth, of blocks that is like, I don't know, 15 minutes of, of, replaying blocks. 

Mikhail:
But you should apply it. We'll just quickly respond with a war--. Well, it'll just quickly respond invalid if the block has been redefined before, or will it add once again 

Marius:
Right now… I think we executed again. And, I'm, I'm, I'm pretty sure there was something why we, why we did this. I can't, I can't quite, quite get it. I think it's because you have, like, different blocks with the same state route. but we could just cache the, the number to hash, in the database and see if, if, if we already have this block at this block height and then not execute it. 

Mikhail:
Yeah. See, it's pretty anyway. is this like, why doing this? if it does not have the same hash, like if it's behind the L I think it's fine. 

Stokes:
And, in the chat that some cl clients don't process the, on unfinalized part of the chain, so you could be saying that. 

Marius:
Yeah, but what I saw was, was more, it was more than the last, last 6-4 blocks. It was, was more like, I don't know, since, since I like shut down the node and then 

Stokes:
Right. Yeah. And I assume that there's some way in the API to communicate us, or there will be eventually, right. 

Marius:
I'm not sure what, what do you mean? 

Stokes:
Oh, just, how to communicate, to the cl like what's the state of things. 

Marius:
Oh, the CL can always ask for, for, for current block or something to see, see, see what our current head is. like it cannot do that for non, for non, you know, non non-canonical products. So for example, if we, like, if we, if we start sinking, we, we just shove the blocks into the database and don't actually set the hash. And so they are not non-canonical once we get, the, the thing from the setup, from the, from the consensus layer the function is updated from the consensus layer we actually is set ahead. And the staple that, well, it does, it doesn't matter. I think it's all right. 

Stokes:
Yeah. Either way, sounds like something to keep track of. Okay. I guess I'll ask him then if we're going to move to any other client updates or final updates, and then, yeah, we can jump back into the naming of the fork if no one has anything else. 

## Spec discussion and AOB
***Summary***
- ***There has been a fix to the proposer boost score. This will be in the next spec release (not in the recent one).***
- ***Seeking to increase the number of standard metrics across clients. Currently eight are well supported. Will continue discussions with client teams.***
- ***Call next week around MEV in Eth2 - review of FlashBots’ proposal.***
- ***PEEPanEIP planning to have a call to explain Merge testnet setup (December 15th @ 18:30 UTC), and another with Mikhail on RANDOM opcode EIP (December 21st @ 1400 UTC).***
- ***Naming! Opened an issue. Consensus on consensus upgrades is star names; uncertain for execution upgrades. Looking for a name starting with “B”. Please nominate candidates in the issue. Deadline Dec 13th. Multiple suggestions on how to vote.***

Hsiao-Wei:
So it's not the client updates, it's a consensus spec update. So there is a fix to the, the poster boost score. And it was your that's. So, there was a part that in the calculation of the proposal boost score and things to shine, like how they found this blog, and we will include this or address this issue or in the next release, consensus spec release. Yeah. 

Stokes:
Great. So, yeah, that'll be important for everyone to keep track of, but it sounds like it won't be, deployed for some time. Any other updates? 

Leo:
This is not an update adjustment, as mentioned that, we would like to continue increasing the number of metrics that are standard across our clients. so we started with eight metrics and most of them are already implemented in appliances. So there are a couple of the museum, but, we're going to move on with the next set. so we will be communicating with you guys to continue this, standardization effort that we'll get. 

Stokes:
Great. Thanks. Anyone else? 

Tim Beiko:
I have just a quick shout out, but next week, we're going to have an MEV call with regards to, basically how to implement that on the consensus layer clients at the flashbots team has been working with, lighthouse to get it set up. And so, yeah, basically we could just get to have a breakout room call where we go over kind of the spec and what's been implemented so far and, and get feedback from the other consensus layer teams. It's a week from now at 20 UTC, to accommodate Australian time zones a bit better, a bit late for Europe. apologies. But I would just be great to have representatives from the different CL teams call and I posted the link in the chat. 

Stokes:
Great. Thanks Tim. Yeah, everyone, please try to send representatives from your clients if possible. I think it's all. oh yeah. I would hope you all agree that it's very important that, we treated this issue very carefully and a lot of the work that flashbots have been doing, is going down to this top for the merge. So, definitely important to attend if you can. 

Pooja:
On a similar note, I have a bit of an announcement with this merge test net. We are planning to organize an event on December 15th at 18:30 UTC, and I'm assuming that they would be explaining about the merge testnet set up. So that's one for people who are interested in participating in this merge testnet. And the other one is with Mikhail Kalinin on December 21 at 1400 UTC. That is for 84399 south Atlanta. 

So if any devs are interested, please feel free to join us. Thank you. 

Stokes:
Cool. Thanks, Pooja. Yeah, this should both be very exciting. And it just to call it out, Trent posted a link to merge community call tomorrow, 1400 UTC. So a lot going on. Everyone has lots of calls. you know, you can see we're all getting very ready for the merge. Okay. final call and then we'll jump into naming. 

Stokes:
Hsiao-Wei, do you want to take over? 

Hsiao-Wei:
Yes, thanks Alex. I'll repost the issue again on the thread. So just to follow up with our previous discussions about the naming for the merge fork, I open these issues to propose what we can do for the next steps. So, I think the rough consensus we have is that we're going to name still upgrades with the science things, and it's still a bit uncertain about if, the, the EL client updates will go with, the seediness or starkness or maybe others. But, so this proposal is that we, if, if we can at least choose one starting with, starting with "B" since the last upgrade was Altair. So this time we sat with B, so the action proposal is that, maybe we can start to nominate some stanchions candidates, at this rate. And then the deadline will be like December 13th. It's just, for example, then we can choose the top four popular names, and then if we want to, perhaps with more involvement from the community, we can have another pop vote, elections. We had one for the other naming election that last time, or option two is that if we want to make the decision as soon as possible, then maybe we can have another discussion in the call two weeks later. It will be December 16th. So this is my proposal and the keypad situation. So opinions and come to nature now. Thanks everyone. 

Yeah, so I wished we could maybe have some decision about number one, if we are going to vote, we are going to propose with bestanion four by for the CL clients. And number two, is that, how will the election be the format of the lecture? Like we just discussed in the context, in the next call or go community vote? Yeah. Two things I wish we can discuss today. Thanks. 

Stokes:
Thank you. yeah, I think where your outline makes a lot of sense, personally, I would say, yeah, we can collect ideas and the strategy and the issue that you posted and yeah. Either it'll be obvious, which is the most popular, or we can decide again, well, we'll decide for the first time, but on the next, let's see this, the next maybe CL call two weeks from now? 

Tim Beiko:
Either that, or we can maybe, if it does feel like we need a call to discuss, maybe you have like a separate breakout room to not take up half these calls with it. 

And also to just like, be more inviting to folks who might not join like these calls. I don't know. I don't have a strong opinion, but I think if we do need an hour to discuss just like trying to isolate it and having a special purpose call might make sense. 

Stokes:
Yeah. That makes a lot of sense. I would hope that we can do most of the back and forth asynchronously. So perhaps to get started, maybe we'll just start in the issue. And, we can just sort of coordinate asynchronously if it looks like there's a bunch of contention and we need a call for that, then I'm happy to organize one then. Yeah. I think the breakout format makes a lot of sense. 

Hsiao-Wei:
Yeah. I agree that the breakout room ideas make sense. 

Stokes:
Okay. Any final or closing thoughts, anything anyone has been dying to bring up and hasn't yet? Otherwise we can go ahead and wrap up early. 

Tim Beiko:
Thanks Alex for running this. 

Stokes:
You're welcome. 

Mikhail:
Thanks everyone. 

Stokes:
Okay. Yep. We'll call it then. Thanks. Bye.

– End of Transcript –

## Chat highlights
- **From stokes to Everyone 02:07 PM:**
https://hackmd.io/@n0ble/kintsugi-spec
- **From parithosh to Everyone 02:19 PM:**
If anyone wants to start validating from genesis in devnet-3, please do let me know
- **From Mikhail Kalinin to Everyone 02:22 PM:**
https://github.com/ethereum/execution-apis/issues/137
- **From Mikhail Kalinin to Everyone 02:30 PM:**
https://github.com/ethereum/consensus-specs/issues/2735
https://github.com/ethereum/consensus-specs/issues/2636#issuecomment-960647404
- **From Dustin Brody to Everyone 02:37 PM:**
https://hackmd.io/Ic7VpkY3SkKGgYLg2p9pMg#Implementation-requirements
- **From Hsiao-Wei Wang to Everyone 02:44 PM:**
naming discussion: https://github.com/ethereum/pm/issues/430
- **From protolambda to Everyone 02:47 PM:**
@Marius The replay of blocks you are seeing on start-up might just be the last 2 epochs, some CLs don’t persist the unfinalized part in their state db, and instead apply the blocks again.
- **From Hsiao-Wei Wang to Everyone 02:50 PM:**
https://github.com/ethereum/consensus-specs/pull/2760
^^^^ fork-choice proposer boost score bugfix
- **From Tim Beiko to Everyone 02:53 PM:**
https://github.com/ethereum/pm/issues/423
- **From Trenton Van Epps to Everyone 02:53 PM:**
tomorrow is the Merge Community call
https://github.com/ethereum/pm/issues/419
1400 UTC, 9 EST
- **From Mikhail Kalinin to Everyone 03:00 PM:**
CL-EL = Star-City after the merge makes sense to me, as there could be pure CL and pure EL upgrades. Having different naming conventions to distinguish the two is good


## Attendees (30)
- Marius Van Der Wijden
- Tim Beiko
- Mikhail Kalinin
- Micah Zoltu
- Alex Stokes
- Saulius Grigaitis
- Age Manning | SigP
- Pooja Ranjan
- Trenton Van Epps
- Enrico Del Fante
- Ben Edgington
- Adrian Sutton
- Carlbeek
- Dustin Brody
- Raul Jordan
- Lion Dapplion
- Parithosh
- Protolambda
- Lightclient
- Hsiao-Wei Wang
- Marek Moraczynski
- Cayman Nava
- Leo (BSC)
- Ansgar Dietrichs
- Dankrad Feist
- Zahary Karadjov
- Zahoor (Prysm)
- Tomasz Stanczak
- Justin Drake
- George Hervey
