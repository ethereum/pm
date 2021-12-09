# Merge: Merge Community Call #2
### Meeting Date/Time: Dec 3 at 14:00 UTC (9:00 ET)
### Meeting Duration: 60 minutes
### [Github Agenda](https://github.com/ethereum/pm/issues/419)
### [Video of the meeting](https://youtu.be/iPw7ixSgA_w)
### Moderator: Trent
### Notes: Alen (Santhosh)

## Summary
| Summary Item | Description | Video ref |
| ------------- | ----------- | --------- |
|2.1 | The merger should have a significant impact on Ethereum-based applications, but there are some changes to be aware of. After the merge, there will be no more proof of work block. The content that is currently at the core of a proof of work block. So all of the transactions and metadata surrounding the Block hash to base fee and so on will be included in that beacon chain block. | [5.15](https://youtu.be/iPw7ixSgA_w?t=315)|
|2.2 | All references to proof of work, uncle blocks, or over blocks will be set to zero. We're not going to remove those fields from the block header just to avoid breaking any tooling or anything, but there's a high difficulty than answer at the top of the owner's list. I'll be reset to zero. | [6.05](https://youtu.be/iPw7ixSgA_w?t=365)|
|2.3 | The difficulty opcode, which is opcodes 0X44, will no longer point to the difficulty sought. But it will point to the mix hash slots, and we will simply rename the mixed hash random and the outcome to random. So, if you're a smart contract that's using difficulty from pseudo randomness, nothing should go wrong. and, yes, you should avoid using this for actual randomness. | [6.45](https://youtu.be/iPw7ixSgA_w?t=406)|
|2.4 | Beacon node being referred to as the consensus layer and the execution engine as the execution layer. And those are basically the equivalent of what's an Eth1 and Eth2 node are today | [15.18](https://youtu.be/iPw7ixSgA_w?t=918)|
|2.5 | Devnet 3 that would come out next Tuesday and for public testnet, that's coming up on the 13th and 14th Dec| [25.38](https://youtu.be/iPw7ixSgA_w?t=1538)|


# Intro
**Trenton Van Epps**
* Welcome everybody As per usual, we'll give everybody a minute or two to trickle in and then get started. 

**Micah Zoltu**
* Are you aware that the event in discord does not have a link to this zoom call? 

**Trenton Van Epps**
* Oh, you mean the, like the discord native ones? 

**Micah Zoltu**
* Yeah. And this coordinated event, doesn't like, if you click on an event details, it does not actually have a link just as link to the, Ethereum PM repo. 

**Trenton Van Epps**
* Okay. Well, I just it's in the ALlcoredev of channel, so anybody should be able to join their, And maybe another 30 seconds one minute while people join. 
* Okay. We can probably get started. hello everyone. Welcome to the second merge community call. Trent, I worked with the Ethereum foundation doing ecosystem work, talking to stakeholders, running things like this. I'm very glad to see all these new faces and some familiar ones. So welcome to the call. Tim's going to be doing most of the talking and then I'll probably add tap in a couple other people, maybe Marius, if he wants to talk about, people helping with testnets, or, I'm sure there'll be other people I asked to share something. but yeah, let's get started. I put the agenda in the chat and I'll add it again. I don't know if new joiners can see it, but, yeah, we're just gonna go through this and if questions come up, please, just, I think you can raise your hand in zoom and then I'll, unmute you actually, I think everybody should have the ability to unmute, which shouldn't be the case, but, yeah. Tim, is there anything you want to start with or I'll just jump into the agenda. 

**Tim Beiko**
* I know I can jump into the agenda. 

**Trenton Van Epps**
* Yeah, go ahead. 

**Tim Beiko**
* Cool. does that on here? Trenton did a great job posting, like some pre-call links. so I, I strongly recommend people kind of read those if they haven't, yet just because we tried to make it clear, you know, what's going to change, at the application layer, what's going to change running a node and whatnot, related to the merge. I'll go over them pretty quickly. But, yeah, 
 
**Trenton Van Epps**
* Those are three links under a pre-call resources. Everyone should read them ideally ahead of this, but you know, now we're here. So add that to your list of tabs. And Tim, we'll give you a quick, overview right now. 

**Tim Beiko**
* Yeah. And I guess hopefully I can use this as a way to like highlight what's it at. And then you, you all can kind of dive deep into what, what happens to your specific project, at a high level, you know, the merger should impact applications built on Ethereum too much, but there are some changes you want to be aware of. you know, first of all, kind of obvious, but after the merge, there will be no more proof of work box. So, basically the content that's currently kind of the core of a proof of work box. So all of the transactions and the metadata around the Block hash to base fee and, and whatnot, all of that will be part of that be beacon chain block. so that's kind of the first big change, related to the, all the fields in the proof of work of block that, that basically relate to proof of work or to uncle blocks or over blocks are going to be set to zero. we're not going to remove those fields from the block header, just to not break any tooling or whatnot, but, basically over the owner's highest at the owner's list though, there's high difficulty than answer. I'm going to be set to zero. and the one thing that, is not being set to zero, but is actually changing in value is, the mix hash value. and the reason for this is bit complex. So bear with me for a second, but, at a high level, we have this upcode on a theory of today called difficulty, which returns the difficulty of a block. It's a pseudo randomness, value that people can use. And a lot of smart contracts use for different reasons. it is not like perfect randomness, it's it's by a small by, by the miners. but obviously if we, if we went from setting that to like some pseudo random value to zero all the time, a bunch of applications would probably break. 
* So what we're doing instead after the merge is we're selling this value to add a Randell out, the Randell value. So basically, the difficulty opcode, which is opcodes 0X44 is not going to point to the difficulty sought anymore. but it's going to point to the mix hash slots, and we're just going to rename mixed hash random and also renamed the outcome to random. so if you're a smart contract kind of using difficulty from pseudo randomness, you know, nothing should break. and, yes, you know, you shouldn't use this for actual randomness, but people do. yeah. So, you know, we just want to minimize the damage there. and one thing that's neat about that too, is, the size of the opcode will change. so basically, you know, if, if the value is greater than two to 64, you can kind of query that on the block and note that the merge has happened. 
* So that's kind of a neat trick. that's exposed to an upcode. yeah. So if you want to know in your contract clear emergence happened again, you know, the set it's a more complicated, hopefully the article itself, explains a bit better. other, other kind of notoriously change is the block time will change after the merge. and we, we saw that last community call that this would affect some contracts. So basically right now, block blocks come in on average every 13 seconds. There's a lot of variance, on that because of proof of work after proof of stake, they come in every 12 seconds. Exactly. Except in the cases when the validator who has to propose a block is offline. So then you basically miss a block can go all the way up to the next one. So this currently happens less than 1% of the time and in practice, it's still kind of comes to about once one second reduction in average block time. and so the, the use cases we've seen, the use cases we've seen for this is like stuff like staking, a reward, or sorry, like the quiddity mining, rework contracts and whatnot stuff, like try to the, the, the send-out tokens, every block, or, you know, kinda make an allocation. Every block those tokens were going to be are going to be kind of streaming out. It's likely quicker. assuming the contracts are upgradable last but not least, last but not least, safe head. So right now, under proof of work and just in RPC, when you ask for the ahead of the chain, you get basically the, or if you want to get the head of the chain, sorry, you can ask for this latest block. and it's, it's expected that like this block can reorg under proof of work. so you know, like applications relying on that, you kind of assume that there's, there's going to be a reorg and in practice, the way they do that is they use the concept of confirmations. 
* They'll kind of get a block and then wait, you know, six blocks or something, 30 blocks or something. And once those blocks have passed, those assume that whichever kind of latest mock, which has had those confirmation is unlikely to be reorg on their proof of stake. We can actually get some slightly better guarantees. So we have this concept of a safe head, which, there's a full presentation here that explains the entire theory behind how the safe head is calculated, but at a high level, it's a block that we expect not to be reorg under, normal network circumstances. So the circumstances under which it would be reorg is if there was like an attack on the network or a large network delay. so it gives you kind of slightly better assurances than basically the, the head of the head of the chain. 
* We're going to be changing kind of the JSON RPC response for, the latest block to point to this safe head, which in practice should come within like four seconds of this sort of a slot. So it's not going to delay things too much. if you still want to use the absolute tip of the chain for some use cases, we've created this new label called unsafe to make it care. So this will return you the last scene lock on the other beacon chain, regardless of how many at the stations and whatnot there is. so, you know, you should expect this is, is somewhat likely to reorg. And then finally, because, with the beacon chain, we have the concept of finalization. we're also going to be able to return to the last finalized block, other just than RBC, which can serve as a nice and stronger kind of substitute for confirmations. 
* So if you're saying like a crypto exchange or something that just, you know, usually has this logic where like you're waiting, you know, and the confirmations, you can probably move to using like the finalized block, and, and basically the condition there would be like a major attack on the network where you'd have two-thirds of validators, you know, trying to finalize a competing chain. and that would put a third or more of this state at risk of being slashed, which is over $10 billion today. so, so yeah, that's, you know, kind of, a useful way to get kind of a high security guarantee for that to work on a certain block. 
* So, sorry. I lost the agenda now, cause I think I just clicked through it. so I think it's probably worth pausing there. Oh, and sorry. Yeah, there's one more thing. okay. Yeah. It's probably been worth pausing there and just discussing, I don't know if people have questions or thoughts about like the application layer and then, you know, there's a couple more things we can say about like more on the like running nodes sides, what changes. but yeah, maybe it's just pause and see if people have like questions or concerns about the application layer before we move on to like the actual node architecture. 

**Trenton Van Epps**
* Yeah. Anybody, if you want to talk, raise your hand and that can I can unmute you. 

**Tim Beiko**
* Okay. Micah, you have your hand up, is that a question or 

**Micah Zoltu**
* I, yes, one of the, as a brief comments, if you are going to use the random op code, make sure you understand the attack factors against it. It is not a perfectly random thing. So just don't don't think that just because we're giving you a random upcode and you can now, you know, write a dice game naively, you really need to make sure you understand the caveats and the restrictions and the constraints. 

**Tim Beiko**
* Right. That's a good point.  

**Marius**
* Also, also the,  the random upcode, like if you, if you right now call difficulty or in solidity, then you will get the randomness problem is at least for gas, if you call it in a few function, then it would still return, the difficulty as, so it's, it's only implemented, correctly. if you, like, if you like use it on chain, but calling a view function does not trigger transaction. And so we don't have the correct, randomness there. it's just a bucket geth right now, but we, we, should be,  I should, like I'm going to fix it. So 

**Tim Beiko**
* Thanks for sharing Marius. Okay. Yeah. I think a couple of minutes then talk about like how the architecture of things changes post merge. and yeah, there's a note here. I just want to make sure I don't forget. you know, we'll cover it, once we turn post. Oh, I'll try to, I think it'll make more sense there. I'm so sorry, but just stuff at the beginning. Nope, Nope. This is actually the wrong thing the right now. Okay. So high level, at the merge, basically running an Ethereum clients, changes. And so what the full Ethereum look like looks like is the combination of a beacon node and execution engine. you'll often hear the beacon node being referred to as the consensus layer and the execution engine as the execution layer. And those are basically the equivalent of what's an Eth1 and Eth2 node are today. and, so that means if you are kind of running a node on the proof of work network today, you're going to have to add a beacon node in order to keep track of head the, after the merge. And similarly, if you are running a beacon node today or, and, or a validator node, you're going to have to run alongside that and execution layer node in order to validate blocks. One thing that's also worth highlighting is right now, a lot of stakers are able to depend on infra because they only need to basically look at the deposit contracts. and, and they can return return that data when they're validated on the beacon chain, post-merger, this is not going to be possible anymore because once you receive a block from the beacon chain, you actually want to execute the block, make sure that it's valid and, you know, important, as part of your database. And even more importantly, if you are a validator and you need to propose a block, you're going to have to have an execution engine in order to put together a block based on the transaction pool, and then send that out to the network and gets rewarded. two interesting, notes there, I guess, is, one, obviously, you know, doing that as a validator means you kind of get the block reward. but it also means that you get to decide where the transaction fees go, which is really interesting. the transaction fees on blocks will still be sensed to call them like legacy Ethereum addresses. So not your validators address, but any kind of address on the Etheremum. and what that means, you know, in, I guess in, in like beacon chain language, is there kind of immediately withdraw bubble, right? 
* Like they're not locked alongside your validator or rewards. so, you know, that's kind of a nice, nice property of the system, where if you've added that a proposals, a block, you get to keep the transactions, also worth noting both the beacon and execution layers will maintain their peer to peer networks and their set of API. So, what are you using JSON an RPC on the, on the execution layer or you're using the beacon APIs, you know, none of those change a module, you know, what we just went to with the head stuff. but you can still query your node, run tracing and whatnot, or where you can still kind of get your information about the consensus, level. And then both nodes will also maintain their peer to peer network where, you know, the beacon though will be connected to a set of beacon nodes and the execution engine will be connected to instead of, of execution engines. the only thing that changes at the gossip level is the block gossip will happen at the beacon layer rather than the execution later. because basically, the blocks, you know, are, are kind of sealed by the beacon node and then propagated on the network. and transactions will still be gossip though, the execution layer so that your nodes can kind of run it as it Geth it finally, obviously we need a, a way for those two days to communicate. So there's an engine API that's been put together, which just kind of always one directional pain from the beacon node to the execution engine. and they're, at a high level at the beginning of that will provide information to the execution engine about, kind of what the latest the head, the latest finalized blocks is. and also ask it to create blocks and request blocks. 
* You know, when it's your turn to propose one, and sorry, why don't I send you, ask it to about a day block? So once you get a block from the network, you get it up at the beacon level, you just send it what we call it, execution payloads. So this is the contents which has all of the transactions or the east one block, send that down to the execution engine, run into the EVM. Then the execution engine will return whether it's an audit or an invalid block. it's a very high level. This is how it works. again, we went over this picture, but you know, you're going to be the spots where, all of the kind of consensus data is, is one of the beacon shape. And it contains this execution layer payload, which contains the transactions as well as some, some other data that's in the current Eth 1 block header. Trenton, we kind of go into detail of like the different calls of the engine API. I'd read. This has been written in like a month or so ago. I'd recommend looking at the spec and obviously anything in the spec takes precedence over this, but I still think the general architecture is, is, is the same. and this, basically gives you an idea of how the merge actually happens. so it's, it's quite similar to the picture, we had above, but high level, you know, right now we have blocks on the beacon chain, which don't have any, anything except kind of this consensus metadata that we have these blocks on proof of work, which obviously you have some data about proof of work and then have all of the transactions. And the merger is triggered by a total difficulty on the proof of work chain. 
* So once we hit the certain total difficulty, which we call the terminal total difficulty, we basically say that the block after the one who's, equal to exceeded this terminal, total difficulty will be proposed by a valid that are under the beacon chain predicated on proof of work. So you can imagine this image, you know, you have these blocks in parallel, then you have the next one, the block, the second proof of work block is the one which would have hit the terminal total difficulty. And that means that afterwards, the next block is, is fully produced by the beacon chain. so you can see that there's no more proof of work. and then, all this kind of contents, which has the transactions and whatnot becomes part of the beacon chain blocks. And then, it's possible that, at this point there are several competing blocks that are like the last proof of work blocks. 
* So, because, you know, they all hit, they all need to hit this terminal total difficulty. If they do, their children cannot be valid blocks. So we'll get, you know, possibly a set of competing blocks, but the depth of that tree will be kind of depth of one. And then the beacon chain will kind of, choose which one is the canonical block. And at some point we'll finalize one. so if you're running, you know, say like, an exchange or against something, that's like a reliant on, on the, sorry on the confirmations and making sure reorgs don't happen, then you basically want to wait for the first finalized, block after the merger, you know, and at that point, reorgs are extremely unlikely again, except in the case of like a major attack on the network. and, and by then the merchants basically over we're fully on the beacon chain, we already covered this. yeah, I think that's pretty much it again, we'll highlight, you know, outsourcing, your, your, execution engine to infra are another similar provider will not be possible after the merge. so it won't be possible mainly because you just can't produce blocks. If you do that. And over time, we'll also have proof of custody. That's additive to the design, which penalize you if, if you did this site to do it. So, this is really the right time to kind of get through running on, on, basically your own execution layer. 

## EIP 4399

**Tim Beiko**
* And I think that's all I had EIP 4399, we covered, basically this is just the one that changes the difficulty to, the difficulty of random. there is a merge spec and the execution layer folder. so we have a full spec now, which only has two EIPs, but if there are any other EIPs's that come up or whatnot, there'll be added here, but just like any other kind of network upgrades, there's a, there's a spec. and yeah, I guess I can kind of get on this. Like, what we've been doing the past month is trying to spin up devnets every week, with kind of the latest specs and get the different, clients to communicate with each other. we're hoping that we spin up one more next week. And then the second week of December, that's, we can spin up a more permanent one, which we leave up and running throughout the holidays and maybe early January. 
* So that folks who want to like, understand, you know, and play with this, have, have something that's relatively stable to, to use. yeah, so that's kind of, the goal is expect in the next two weeks, just having kind of a consumer network that's, up and running and, Marius who's on the call has, has put together a great guide about, you know, trying to get, nodes running on the network. And if you do want to help with testing, some type of things that that would be helpful, to try and test. And I guess just generally also, if you run an application infrastructure tooling, you know, telling us what's breaks, is, is, is really helpful feedback. the earlier the better, I think one thing that's, that's our kind of stating is, you know, when we have these network upgrades, we obviously try to leave time for people to upgrade their nodes. 
*  and, you know, typically that's like one to two months, we understand that the merge is, is much more, I guess, very different from regular network upgrades. And, and I think one part is where like the community can, can really help is by trying stuff early. We can hopefully minimize the kind of delay between when all the code is done clients. And like when this goes live on main net, you know, I think in the world where like nobody tries anything until we have like a final, proper release, it might be, you know, several months, of people trying and figuring out what breaks and getting comfortable with it. but hopefully by having these steps, that's where both accelerate that a little bit. And, yeah, we've got the, a bit quicker. Marius, is there anything you want to add there about the devnets? I think Perry is here as well. Yeah. 

**Perry**
* Yeah. So just to give you guys a bit of, scope about the devnet, so devnet tool, instead of mentor introduced testing slash running loads to the wider community and a lot of clients are still figuring out small bugs or differences. So don't expect it to be extremely stable. like Tim mentioned, we'd have Devnet 3 that would come out next Tuesday and for public testnet, that's coming up on the 13th and 14th. So if you're an infrastructure provider or if you're running any sort of, and Ethereum based tooling, please do start testing now and figure out how, where all the tooling lies, etc, I will post the the link in the chat thats compilation of all the tools we have right now. So there's a beacon Explorer, regular, blogs scout, so you can check transactions, there's faucet, so Eth deploy smart contracts, there's also an RPC to sync your own node, but we do recommend that you think your own, not just to get to know how things work. yeah. Please let us know if something breaks and let Mario stop all the testing doc, I guess that's a good transition to that. 

**Marius**
* Yeah. So, I would, I would, like to encourage all of you to start testing, start testing early, we created, some documents, about how to set up some of the clients. not all of them are there. So if you, if you're really interested in like running a particular client combination or something, do that, test it and put it in the document. And, if you have any questions about testing, then just DM Me, either on discord on, on, on Twitter, you'll probably find me because of my really unique, last name and, yeah, happy like we already have. I already have, like the M's from over 400 people right now that are interested in doing it. And, we also set up a, a page of ideas, what, people could work on if they wanted to. And, if you have other ideas that we should really test before for the merge, then you could just add them to this document. That's it.

**Trenton Van Epps**
* Thank you, Perry and Marius, not just for talking about your work, but actually doing it. That's the important part. let's see if there's anything else left on the agenda. I think we've, we've covered everything so we can open it up to anybody else who has questions. we've still got quite a bit of time, so if you're shy or unsure of how to phrase your question, don't be, yeah, go ahead, Omar. 

**Omar ceja**
* Hey,a quick question on the diagram of the execution layer and the consensus layer, there seems to be a one-to-one relationship between the engine API. Is that something that's true or just kind of a limitation of diagram? Can you run one beacon node and have multiple execution layers? Talk to that beacon node? 

**Trenton Van Epps**
* Yes. I believe that is the case. Tim, do you want to pull that diagram back up if you can, or I can try to do that. 

**Marius VanDer Wijden**
* Yeah. So, you can do that. You can not run multiple beacon nodes with the same execution layer. That's that's not working with the, with the current. 

**Trenton Van Epps**
* Sorry, did I, did I miss hear it? I thought he asked about validator clients. 

**Marius VanDer Wijden**
* Yeah, you can, you can run one beacon node with multiple execution layers and take the majority vote of them, for example. So Peter has been working, in his free time on a client that does exactly this take the majority of voets of like three or four different, consensus, execution their clients for, for one consensus layer client. Is that, the minority client quote-unquote? Yes, it's called minority.

**Trenton Van Epps**
* Okay. Did that answer your question? Oh, Tim's back. Go ahead. 

**Tim Beiko**
* I was going to say, I don't, I think of our question was about validator clients, right? So it's like, could you run? And the validators are the one execution engine, Is that all right. 

**Omar ceja**
* It was actually, can you run, yeah, one beacon node in multiple, execution layer nodes, for that one beacon node. 

**Tim Beiko**
* Okay. Yeah. That's not possible.

**Marius VanDer Wijden**
* And you can, you can always run multiple validators on one beacon mode, but I guess, you know that 

**Mikhal Kalinin**
* Yeah. just a few, a bit of comment here. Yes. You can, like guides, multiple execution layer clients with one beacon node. So it's just will, it's just a matter of propagating all the messages for them via beacon node to wire engine API to all this extremely  clients as possible. 

**Omar ceja**
* Sweet. Awesome. Thanks. 

**Trenton Van Epps**
* But the opposite case, when you want to run like one execution client to serve for multiple beacon nodes, it's not a supported by the engine API spec, and it will not supported it, but in theory, you can, like if you're, there is like one thing that can go into conflict here is the update of the fork state for that come in from multiple beacon nodes to one execution rate of clients. And in theory, if you're like, no, if you have like a kind of a master beacon node, because that just sends these structures, abated messages and the only one, but others do not update the fork choice in theory, it's possible to do this kind of set up, but yeah, it's more complicated and there are implications. So this is why it's not supported by default by the engine API aspect. 
So that's it, 

**Micah Zoltu**
* Which, which means you'd have to run a custom client. So not off the shelf. 

**Omar ceja**
* I see. So the execution engine both reads from the beacon node and writes to the beaker or communicates with the beak node. So it's not just strictly reading from the beacon node. 

**Trenton Van Epps**
* It stopped like writting to the beacon node. Imagine you have like two beacon node, think that, there are two different hats on the chain at some point in time. It's possible, like, because of the, as such, because of the network, your way and the other factors. So the execution layer were quiet will, like, yeah, it, it will receive two conflict and pictures of data from the two big nodes. And it's difficult to decide what to do in this case. that's why this, set up is not supported by default. 

**Marius**
* So just to add a comment, so we are nevermind, we're actually thinking about the use case like that. And generally we think it might be possible to, to add that kind of functionality, that one an angel will, be able to work with multiple beacon nodes. you need to kind of like a separate block, pointer for, pointers for each of them. So you need to have like this many, two to one relationship. And, so the thing that is not in that spec, you need to somehow differentiate, which messages come from, which, beacon nodes. And so we might experiment with this at some point, but, we don't have capacity right now. 
So maybe closer to, to release 

**Micah Zoltu**
* Another thing to keep in mind for anyone wanting to go down this path is that at some point in the future, it is likely that we will start requiring proof of that. I wouldn't producing blocks, I believe. And so, I just wanna recommend caution, like don't sink a huge amount of engineering effort because there may be changes to the protocols that critically break this, that sort of set up where you have, lots of beacon clients talking to one execution client. 

**Marius**
* Yeah. It was like this for, with this for now, but we'll see 

**Micah Zoltu**
* Yea, I am not too Worried about Nethermind just for third parties who don't know what they're getting themselves into. 

**Royboystudios**
* All right. I think we covered that. Thanks for the question. Omar, anybody else with a question otherwise, maybe we could talk about what Raul was talking about. Maybe a little tangential, but it's interesting discussion. Yeah, go ahead Noam. 

**Noam**
* Hey, wanted circle back to the devnet discussion, two questions here. one during the last community call, you guys mentioned that difficulty bombs go off on existing testnets that's like Robson. I think the timeline there was slated for around January. Is that still the case? 

**Tim**
* Possibly we haven't made a call out that yet. I think it depends just on how far on the client patients are. but I think, yeah, we ideally we'd like to merge drops in before, before the difficulty bomb goes off on, 

**Trenton Van Epps**
* Is it true?  I believe the Geth team is going to propose a new Testnet to replace the proof-of-work testnets. 

**Marius VanDer Wijden**
* Yes. Supporting you. It has already volume, which has already been started, but, there were some issues with, like I don't know, setting up the service so we haven't publicly announced it yet, but yes, we plan to create a new proof-of-work Testnet since our, the, other proof of work test nets, Robson, is pretty, big already and like really suitable for testing. So we would like to create another one. 

**Royboystudios**
* Gotcha. Thanks. And then somewhat related to this, has there been any thought given there's kind of two use cases for the testnets that's right now, one is for like each core devs to experiment on the protocol. And then the other is for application developers to sandbox developed applications. Has there been any, give any thought to having like two distinct testnets for these two or like not two but multiple testnets and it's for these multiple use cases with redundancy pick the, obviously 

**Marius VanDer Wijden**
* I think we will spin up testnets that are not open to the public. 

**Noam Hurwitz**
* That's what you guys primarily use for development. If that makes sense. 

**Marius VanDer Wijden**
* Yes. 

**Trenton Van Epps**
* Anyone else? Hendrick, go ahead. 

**Hendrik**
* Yeah.I have a question about where the block data is stored after the merge. So is that still in the execution client data store? 

**Mikhal Kalinin**
* That's a good question. So, the block data, you mean the layer, existing layer blocks right? 

**Hendrik**
* Yes. 

**Mikhal Kalinin**
* And, you mean the history or? Okay. So the execution way of blocks will be still stored on the execution on the client's side and they will be accessible indexation layer, network. and there is like, the question is, yeah, because the beacon will contain the execution payloads as well. and, there will be kind of duplication between the layers in terms of data storage, but we are, looking for, duplication techniques, like, like, the, beacon blocks and, consistently Aquinas for, the execution payable of hitters and fetch blocks on demand from the exhibition requirements. This is one of potential solutions for that application, both in terms of, like, accessibility of blocks and the execution layer client side from the network and why JSON RPC see this is not broken and it's the stays on the fact that by the merge. 

**Hendrik**
* So in the short-term, there will be some duplication and eventually it will be optimized to, to have, less storage. 

**Mikhal Kalinin**
* Yes. Thank you. 

**Trenton Van Epps**
* Anyone else? Yeah, sure. 

**Jeremias Grenzebach**
* Hi. my question is, is there any change in, if it makes sense to have consensus and execution day on the same machine, performance wise or bandwidth wise, or any recommendation yet 

**Trenton Van Epps**
* You mean existing as the same, like monolithic piece of software or 

**Jeremias Grenzebach**
* Piece of hardware? 

**Trenton Van Epps**
* I mean, oh, I feel like that should be the default. I feel like most people already do that. 

**Micah Zoltu**
* I don't believe it's necessary. I don't, you don't need to have a crazy high bandwidth connection between the execution and convince client you'd want it to be low bandwidth. Like you don't want to like go to the moon and back, because there is a time constraints on validators doing work. And some of that work requires talking to execution client. but if you have like, you know, two hosts in the same data center, that's not a problem. If you have two hosts on the same side of the country, that's probably not a problem. You have, one of your hosts is in Asia and one of your hosts is in the U S maybe you start noticing you fail on occasion to do things in time that Mikhail may have more thoughts on this. 

**Mikhal Kalinin**
* Yeah. I think you have described this, just like, I think the question is about, how many what's,what will be requirements for running the client after the merge rights, with respect to hardware bandwidth, since of course, how many consensus clients does require right. In addition to extremely. 

**Micah Zoltu**
* Yeah. So do you need specific, like, what are the requirements for the connection between the execution client and this client? Do they need to be like, you know, sub one millisecond latency or is, you know, a hundred millisecond latency fine between the two 

**Mikhal Kalinin**
* I see, of course the lower the better, but I think that's probably under a hundred milliseconds is okay. But it depends of course, on a lot of things, but Thank you, 

**Trenton Van Epps**
* Anybody else? 

**Marius VanDer Wijden**
* I think we should try this by the way, We should test that. 

**Mikhal Kalinin**
* I agree. Yeah. Right. That's that's true. I I'm, I'm also just, you know, trying to understand whether it makes even, even makes sense to run them on different machines. I'm not sure days. So if you, if you're on in both, so the, the optimal solution would be to run them on one machine or, or like Michael had said in like the same, that data center. 

**Trenton Van Epps**
* Okay. It sounds like we've covered most everything. I guess just generally to wrap up, we got pretty into the technical weeds, but if you're smart contract developer, we're trying to make it as simple as possible. basically you shouldn't have to do anything. There's no migration. You don't have to redeploy your contracts. if you're a user listening to the call or watching this afterwards, you won't have to, you know, move any tokens that you own. All of this stuff will happen in the background. You shouldn't even notice, that the merger has happened other than people saying yes, it's happened or a proof-of-work has gone. but there's no migration. oh, right. Sorry. Yeah. Tim, Tim points out that if you are a smart contract developer and you have a strong dependence on block time in your, in the way you've set up your lending functions or how you calculate time for, lending rates or something like that, then you may need to redeploy, but by default, if you're, you know, most users shouldn't have to worry about things, most users or developers. 

**Micah Zoltu**
* Yeah. If you were our developer who isn't in a situation where your contract depends on block time, you should not just update it to be 12 seconds. You should remove the dependence on block time. You should not assume that we will keep the block time and seconds may change to 10 seconds in the future. May change 20 seconds to may change the five seconds like contract should not assume block time is stable over time. Like you should just use the timestamp field on the block if that's what you care about. If you care about time, who's the timestamp, 

**Tim Beiko**
* Right.It's worth noting that post-merger, those timestamps are also more reliable than they are on proof-of-work. 

**Trenton Van Epps**
* Right. So the recommendation is don't use block times use timestamps. All right. I think we covered everything and there are no more questions, last chance for anybody to jump in or ask a question, otherwise we'll wrap up. Okay. thanks to everybody who showed up, Marius, Macau, Perry, Micah. this is really helpful to have people to answer questions. So I appreciate that. and then we can go a little bit deeper technically to people who have questions about that stuff. so yeah, we'll wrap up here. This will be uploaded sometime today or before the weekend. And, if anybody wants to, listen to it again, it'll be uploaded to the ethereum-cat-herders YouTube. that's it. Thanks everybody. Appreciate it. oh yeah. And we will probably, depending on the need or how many questions come up, we'll probably host another one maybe in another month. I don't anticipate there being huge changes or, you know, a ton of new information that we need to relay other than what's already been prepared, in the agenda. But yeah. Tim, do you have any final thoughts? 

**Tim Beiko**
* Yeah, it probably makes sense to host one of these sometime in January, once, like consumer is out then probably once we have a better view of what's going to happen with drops then, yeah, but definitely not before the holidays and yeah. Keep an eye on the blog of ethereum.org page. we're going to have a post there when the actual, like, I guess final iteration of the consumer definites is up. I'll make sure to post something there. 

**Trenton Van Epps**
* Tim, you, you indicated that you were going to come back to the discussion point number two on the agenda, but you never did. Was that intentional? 

**Tim Beiko**
* Which one transaction feeds 

**Micah Zoltu**
* The transaction fee is going to validator. 

**Tim Beiko**
* Yeah, I thought I had mentioned that. I thought I mentioned it, but in case, in case I guess to reiterate it, if I did them. Yeah. So post-merger transaction fees go to the adult, go to a validator address. They keep going to like an Ether call it like EVM address. so that means if you run validators, you know, you can capture those transaction fees basically as they come in, they're not going to be or anything. This is also true of obviously the MEV fees. So any fees basically that are paid to the block producer like that, I guess in, today would go to like the Coinbase address, get captured by valor. There's post-merger directly. No, they're not locked or anything. Hopefully this scare. 

**Trenton Van Epps**
* Yeah. And that's, that's pretty significant, especially if you've been validating since, Genesis to be can change Genesis last year. the unlock for funds, hopefully it will come in the upgrade after sorry, unlock for steak teeth or, you know, being able to transfer it to the execution layer, use it in smart contracts, use it like you typically do, that will hopefully be in the upgrade after the merge. But until then, like Tim said, you will, if you're a validator, you'll be able to use, you know, priority fees that miners currently get that will be directed to validators or a validator control to address, on the execution layer as well as any MEV. And I know there's a lot of people working on, how to integrate NBD into post-marriage clients. specifically the flashbacks team is working on that stuff and I'm sure they'll have more releases and, and, you know, as we get closer, there'll be a better picture of what that actually is to look like. Okay. I think we've squeezed all the questions out of people. It as always, myself, Tim, anybody who answered questions on here is more than happy to answer further questions that come up. if you're not already in the ether and D discord, that's where a lot of this discussion and testing planning takes place. So feel free. We we'd love to have you join there and contribute or observe, learn alongside us. anything else? 

**Tim Beiko**
* Nope, not true. 

**Trenton Van Epps**
* All right. Thanks everybody. Yeah, we'll have a, another one in about a month, maybe at the beginning of January. Thanks everybody for joining and asking your questions. This is great. 

**JeremiasR**
* Thank you. 

**Tim Beiko**
* Thanks, 

**Trenton Van Epps**
* bye. 

-------------------------------------------
## Attendees
* Trenton Van Epps  
* Mikhail Kalinin
* Micah Zoltu  
* Tim Beiko  
* JeremiasR
* Jeremias Grenzebach
* Hendrik
* Marius VanDer Wijden
* Noam
* Royboystudios
* Perry
