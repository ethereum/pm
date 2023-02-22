# Execution Layer Meeting #155
### Meeting Date/Time: Feb 16, 2023, 14:00-15:30 UTC
### Meeting Duration: 1hour 30 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/720)
### [Video of the meeting](https://www.youtube.com/live/GmwEa_HI2lE?feature=share)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)


| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 155.1 | **Sepolia Upgrade** We're on track for February 28th, and if you're actually listening, you can expect releases from the various client teams at the various, master branch, commits that support Sepolia, in the coming days. Expect a blog post about this early or mid next week, and keep an eye on the various client reposts as they put out releases or announcements.
| 155.2 | **EIP-4844: 0-blob transactions** In terms of next steps, could one of the 4844 authors simply change the EIP to state that type five transactions require a blob - Angsar promises to do it in the chat.
| 155.3 | **Minimal presets** Dustin to create PR for minimal presets (context) as there is no objection 


## Intro [0.30](https://youtu.be/GmwEa_HI2lE?t=30)
**Tim Beiko**
* Okay, we are actually live now. welcome everyone to ACDE 155, Bunch of things today. So, we'll cover some Shanghai stuff and I think, Marius, you have some testing updates from there. then Cancun, we had a bunch of discussions, about zero blob transactions, in the 4844 call this week. 
* And, I think it made sense for some of those to be bubbled up here, so we can hopefully move forward on them. and then there were a few other Cancun related, topics. So, one regarding, minimal presets of the beacon chain, which, EL clients, I believe need to start caring about with Cancun because of the engine API changes. we also had a breakout about SSE transaction format. 
* So we can sort of recap what happened there in the next steps. and then there was, there was another SSE EIP about, the withdrawal route. and then finally, something, regarding the transaction pool API. 

## Shanghai Updates [1.42](https://youtu.be/GmwEa_HI2lE?t=102)
**Tim Beiko**
* So I guess the start, on Shanghai. So we have Sepolia planned for, February 28th. ideally we denounced that early next week. 
* And, and thus assumed client put releases out for it. that's said. yeah, I know various, you ran into some issues, when testing on, on the latest test net. You wanna maybe give us a quick overview of, of what happened? 

**Marius**
* Yes. So, full notes were not, full sync notes. were not able to, to correctly sync to the test net. ho horribly butchering this, this, so I'm just going to paper over it. basically the, the issue is if we got a block that was empty, so it had no transactions, and no withdrawals, then we would actually, set the, the withdrawal hash to nil instead of empty withdrawal, sorry, the, not the withdrawal hash the with withdrawals. 
* And, we wouldn't download the, we wouldn't download the block because the block is the, we wouldn't download the block body because the block body is empty. And, we, we would ju but we also wouldn't correctly initialize it. this problem, we had a similar problem in the past already. the thing is, we, like, we can only figure out these issues if we have empty blocks and, so fully empty blocks that don't need anything to be downloaded. and, and we are full syncing, so it doesn't happen on snap sync. 
* It doesn't happen when you, when you're not syncing, when you're following the chain. So, yeah, it's, it's, it's kind of a weird edge, edge case, but given that we had already two issues there with, with Geth, it might make sense to, have this as a test, as a sync test, just syncing a full chain, like  full syncing a chain from another client that has empty fully empty plugs. 
* And, yeah, it's, it's fixed now. it's not in the release, but we are planning to do another release, with this fix and another fix, basically today or soon. 
* And, yeah, so people on sep people on Sepolia can just use the normal version, but if you want to sync up, after the fork happened, then you should use current master. That's, that's, that's basically it. 

**Tim Beiko**
* Thanks. I guess I'd be curious, are we aware of other clients teams having this issue? 

**Marek**
* So I, haven't noticed any issue during this sync. but I will check all the edge cases. Would be nice to have high test. Of course. yeah. 

**Tim Beiko**
* Anyone else? 

**Marius**
* So this is this, this issue, these issues arise because of one optimization that we do. If a block has no body, we are not requesting the block body. Cause we know from, just from looking at the header that the body is empty. And so we are not asking the network for it. I'm not sure if other clients have the same optimization, but yeah. 

**Andrew**
* Yeah, we might have this optimization. We probably do have it in, Argon, so I need to double check our code and see whether we suffer from the same issue or not. 

**Tim Beiko**
* Okay. Mikhail?

**Mikhail**
* Mikhail, Yeah, quick call comment on not having a body for empty, block, is may have these payload methods in engine api. So just to be sure that those are handled correctly, even if body is empty, you are not storing it. 

**Marius**
* Yes, Those are, those are handled correctly and we have tests for it. So yeah, this is not a problem. It's, it's really only during sync. 
* And also like if, if someone like gives us a, a malforms block, either we are now also via the Eth protocol, but before, before that, via the engine a api, we would just reject it. But now we also reject it on if someone gives us a block on the, on the eth protocol. 

**Tim Beiko**
* Okay. And Mario in the chat said he can add, sorry, he can add an a hive test for this. So we currently had hive tests for both empty like blocks without transactions, blocks without withdrawals, but not the combination of fully empty blocks. I guess I'm curious, just to hear from teams, do you feel this should change sort of the timeline for Sepolia or given we already have a fixed in Geth. and you know, it seems like it's, a pretty easy edge case to describe, you know, our client's still confident in having a, a release, for Sepolia or at least, you know, pointing to master for this bug fix. in, in the coming days, 

**Justin**
* This is based, I think we'd be more comfortable with that second option there. We're planning our release for Monday. 

**Tim Beiko**
* Okay. And, and, and the Monday release would, would make sure to not have this issue, is that right? 

**Justin**
* Well, we'll try to get it in there, but if we're open to the option of someone doing a build off of Main instead, that would make us a little bit more confident that we can sort it out. 

**Tim Beiko**
* Okay. sounds good. Any other clients? 

**Andrew**
* Yeah, I think we can do a release early next week. 

**Tim Beiko**
* Okay. Yeah, the same. Okay. perfect. So what I'll do is , I'll follow up with, all the EL teams offline, and see, you know, whether they have a release or, and or, you know, recommend pointing to Master branch. 
* And, and we can use that for Sepolia. But I guess, does anyone feel like we, we should delay Sepolia over this? Okay. So yeah, I guess, we're still on track for, February 28th, and if you're listening, you should expect releases, from the various client teams are at the various, master branch, commits that supports Sepolia, in the next few days. 
* Anything else regarding Shanghai Capella that people wanted to discuss? Oh, Barnabas, yes. 

**Barnabas**
* Yes. I could give, an update regarding the withdrawal DevNet seven that we have just launched on Tuesday. So this, DevNet seven was basically, a very heavy stress test and the mental test for worst case scenario, on the main net, what did is a 600,000 validator set with, 360,000 BLS key change, happening during, Sepolia with, deposits and withdrawal walls happening all at the same time, with, field queues. 
* And, Sepolia was, this morning at, 9:00 AM utc and, we saw a huge, fluctuation in CPN re usage during the for, transition, which was expected due to the extremely high number of, BLS messages. Got it. 
* In the, within a few days we will see exactly how many messages have been lost or get a better estimation. And, what we also noticed is, we realized that there was a bug in Besu and Prism where, this payer did not discover a new deposit, and we haven't noticed this issue before because we didn't make, this amount of deposits in other networks, but maybe someone from can explain this bug a bit better. 

**Tim Beiko**
* And this, sorry, is the issue they could not see when they were overwhelmed with deposits, they, they missed a large share of them or they stopped processing them altogether, 

**Barnabas**
* So they stopped processing.  And, also there was some blocks missed, block proposals missed, and, we figured that it was possibly due to, some, RPC batch size issue. 

**Tim Beiko**
* Got it. Anyone on the besu u or prism team have more context? 

**Terence**
* I'm not aware of this issue, so, so that, so that, I will follow up right now. 

**Tim Beiko**
* Cool. 

**Matt Nelson**
* Yeah, I can, this is Matt, I can provide some more context. we recently limited this, RPC method intentionally to a small value to kind of avoid, some DOS vectors stuff. but we realize that, you know, in the case of Prism, they expect around a, a batch size of a thousand. 
* So, you know, we're providing a much, much smaller batch size. I'm not sure why it would completely stop the process. We need to probably investigate that, but we will reevaluate this, this value, and  we're aware of the issue specifically. 

**Tim Beiko**
* Got it. thanks. Anything else on Sepolia?

**Barnabas**
* We, we have lost, one epoch. We went down to 62%, during, for transition due to the extremely high RAM and CPU usage. But we recovered within, three epoc approx afterwards. 
* And, I think it's expected to have a lot, smaller case and mainnet because we don't expect this amount of BLS goes depending. And we we're gonna have a lot more nodes, so this is really just the worst case scenario. 

**Tim Beiko**
* And then what, what was the split of the different, validator combos on, the DevNet? Was it like matching mainnet or was it, like an equal split? 

**Barnabas**
* It's not equal and it also doesn't match.  I can get you the, the number. 

**Tim Beiko**
* Sure, yeah. If you wanna post it in the chat when, if you don't have it off the top of your head. Yeah, that'd be great. 

**Danny**
* And will we run the, maus circuit breaker test on this testnet  as well? 

**Pari**
* No. We'd be running that on, withdraw may net shadow fork two. 

**Danny**
* Okay, cool. That's still in progress though. 

**Pari**
* Yeah, I had some issues syncing up the nodes before starting the shadow fork, so it's a bit delayed, but we get to that soon. and map post has been deployed on Shahan as well, but I think for now it's just returning 204 as builders are coming online, but the relay is set up so we could do a circuit breaker test on Shahan as well, but I think the idea is that we don't because we want to keep it stable for public testing. 

**Danny**
* Yeah, that's fine. 

**Enrico**
* Pari, which version are you running for, for these tests? 

**Pari**
* For CL clients?

**Enrico**
* Yes. 

**Pari**
* Your clients, at the moment it's the latest releases, so there's, it's still waiting for the relays to come online before I go asking around for which version to update. 

**Enrico**
* Okay. So you, you, you were not planning to use the upcoming CL release? 

**Pari**
* I will once the releases are done, but we haven't started the Shadow Fork yet. So once it's done, then I would reach out to get the latest images to run there. 

**Enrico**
* Cool. Thanks. 

**Pari**
* Yeah. 

**Tim Beiko**
* Okay. Anything else on Sepolia? 

**Lukasz**
* I want to say that we just, I just confirmed that we already handled this, empty body issue correctly - Nethermind.

**Tim Beiko**
* Nice. Okay. And yeah, for people listening, so expect a blog post, early, mid next week with this and also keep an eye on the different client reposts, as they put out releases or announcements, for the Sepolia, Chappelle versions. and again, this fork is scheduled for February 28th, which is, Tuesday about, 10 ish days from now. yeah. Anything else? 

## Cancun Updates [16.20](https://youtu.be/GmwEa_HI2lE?t=1007)
**Tim Beiko**
* Okay. otherwise, let's move on to Cancun. so we had, a 4844 call this week. And I think one of the big, I think things to agree on to move forward is what to do with zero blob transactions. so there were a bunch of PLE designs that relied on the ability to discriminate, between blob and non blob transactions. 
* And an assumption there is that, the sort of EIP4844 type five transactions have blobs and therefore are bigger, and the other ones don't. and so there was discussions about whether we should allow zero blobs transaction, in protocol, but ban them from the me pool so that if blobs are created with them, it's fine, but, clients don't process them in the PLE directly, whether we should just straight up ban them in protocol as well, at least to start. and if we do allow these zero blob, transactions, then what's the right way to discriminate, you know, between, blob and blob less transactions? 
* Do we want to look, at basically the length of the blob list at the transaction type? Do we want to gossip this information in something like Eth68? and basically I think aligning on all of this allows us to get to a transaction pool design, which, hopefully is more efficient and can, can handle the actual blobs in a way that's different from transactions that, don't have any blobs.
* So I don't know if anyone, I guess from the EL side wants to maybe start and chime in here. My feeling is most of the EL folks were leaning on the, the not allowing zero blobs, but different sort of, variations of that.yeah, Lukaz

**Lukasz Rozmej**
* So I was thinking about this quite a lot and, while  I settled out that I don't like  any solution, but what I'm leaning to now is, either having some additional metadata for transaction, for example, transmitted into ETA 68 or just using the size of transaction to determine the rules of, how we behave with this transaction. So for example, if we have a big size transaction, even if it's like whatever, if it's a blob transaction or not, it will go into this large, transaction pool, right? 
* And this also resembles to me a bit how, for example, some managed languages like devnet or Java handle, big objects that, for garbage collection, they have separate object heap for that with special rules. So it kind of makes sense for me and it's like it is the elegant solution from the design perspective and you know, from implementation perspective, like trying to think about that. It's not about type of transaction, but the size of transaction also makes some sense to me. 
* So I'm not entirely convinced, like I said, I don't like any of them. All of those things kind of like crip issues into implementation make it more complex, but maybe that's what I would suggest. 

**Tim Beiko**
* Got it. okay. Peter, why do you disagree? 

**Peter Szilagyi**
* I think it's a horrible idea. Okay. so, the series super nice, super elegant and insanely complicated. So the fact is, in order to differentiate, so the whole point of block transactions is that you have behavioral limits on it. It simply behaves completely different than large transactions. You can have a lot of block transactions in a block, but you can only have one or two block transactions in the block. 
* That's a huge behavioral differentiation. And if all of sudden I can have zero block transactions and it's gone, hacking Eth 68 to transmit the block size that for the transaction size, that's completely moved because I still can have really huge, i, I can have a two megabyte transaction, plain transaction that would be transmitted to one mechanism and block transactions would be smaller. 
* And I think it's just the whole point is with block transactions, it's something very, very specific that we can, we can use those specifics to make optimizations. And I get it that from a research perspective, it's super nice to make everything completely generic and then the whole thing will go all apart. Just like the Merkel, Patricia tried all apart it's piece of shit, and same thing will happen. 
* Transactions, we just make this matter transaction and then we'll just say, okay, screw it. we sure hope that a MEV boost and all the others can handle it because clients sure as I won't be able to, sorry Peter, you're delegating everything out to somebody else who has the infrastructure to handle all that crap. 

**Dankrad Feist**
* I didn't get your argument there. You said like you can have a two megabyte bit transaction and a block transaction and what, what's the problem there? 

**Peter Szilagyi**
* My point is that I cannot differentiated. So the currently the idea about the block transactions, we transmit the transaction IV in the transaction announcements, some networks, so I know what, which ones are block transactions and which ones are not. Yeah, the new suggestion was to forget that and just transmit the size, but then I just get one big soup off transactions again. 

**Dankrad Feist**
* Right. 

**Peter Szilagyi**
* But how, like I Still don't Understand Lucas, only the transaction IDs in data. 

**Tim Beiko**
* Alexa, you had your hand up. 

**Alexey**
* Yeah. thanks. another, idea would be, to, encapsulate all this, separate logic for handling big transactions or block transactions or whatever, because it's just, one or two cases maybe we will have more in in the future and, we can announce not size or type of transaction or we can just, share a flag that says, you would not like to download this transaction or like that. 
* I mean, Transactions will be, well, different of different, I mean, if you, will know the transaction and the size is not, like, is not, past, the correct size is not passed, you will verify it that it is too big and you reject this peer, probably, you want it, you want to reject peers that, send you big block transactions or just big transactions, at the end. And so instead of, sending some details about the transaction, we can just send, like admiration that says Eth it is a big transaction, that's why you don't want to load it, or it is block transaction, so on and add more reasons why you should not download it. and, it can be like the solution. 

**Tim Beiko**
* Got it.Andrew,  

**Andrew Ashikhmin**
* I think, for simplicity's sake, I agree with, Peter, I think the simplest thing to do is just, to introduce, a new transaction type for the, non global SSZ transactions. and it already chimes in nicely with, Eth 68, it, has nice, semantics. I think like four total simplicities to my mind's the best solution. I don't actually see what are the drawbacks 

**Tim Beiko**
* And the reason for adding this extra type, of transaction is so that you can only using like SSZ supporting infrastructure sign both blob and non blob transactions. Is that right? 

**Andrew Ashikhmin**
* Well, and going forward, I mean, I think going forward we want to move to SSZ, but so the new, the new type SSZ without blocks will probably be our preferred transaction type for not only for L2 solutions, but potentially for, for, for everything. Yeah. and this like clear differentiation between non block transactions and block transactions by their type. 
* I think it plays nicely with the semantics because, the, you, yeah, you kind of, they serve different purposes, rather like as you run of the new transaction or B or carry blobs. So, got it. I don't see a problem with the, with two types. I think it's, it's a benefit that just highlights this semantical difference. 

**Tim Beiko**
* Yeah. But we don't, yeah. And, and so, So this means that we'd have like effectively five transaction types, right? Like, or maybe six with the pre EIP151 or whatever. But you would, you would keep the existing legacy transaction types introduced blob transaction and then, blob transactions, which require a blob. 
* And we can have this hard limit there and also kind of separately introduced an SSZ zero blog transaction. And this means that, like Marius is saying in the chat,we can do things like, add more restrictions to blob transactions. Like for example, not having access list, not allowing contract creation and so on. 

**Andrew Ashikhmin**
* Right. Yeah, that makes sense. 

**Tim Beiko**
* And I guess, you know, with regards to the transaction pool, we don't actually need all the clients to have the exact same implementation. Like this is not the case today. 
* So say we went down this route of having two new transaction types, ones that is like both of them being SSZ transaction types, one of them being a blob transaction, which requires having a blob, and potentially, has some other, other restrictions. And then another that is, SSZ no blob transaction, which is effectively the equivalent of like, type two transaction today. how did people feel about that? Lucas? 

**Lukasz Rozmej**
* So, while we don't have to have the same transaction Iiplementation. historically I've seen that we converge on the very similar implementations due to security results. And second thing, we still need to agree on Eth 68 if there, if, what's, how it should look like, because this is what we all need to be support. 

**Tim Beiko**
* Right. That makes sense. Yeah. 

**Danny**
* Danny, I was gonna say, there's gonna have to be conditional logic somewhere around number of blobs, around size of transactions, etc. And I think ultimately, you know, if engineers think that is in embedded in the type is going reduce complexity, then that's probably just what we should do, and, and move forward with that. 

**Tim Beiko**
* Lukasz 

**Lukasz Rozmej**
* The one, the one, good argument, that I heard about allowing zero block transactions is that when, if we want to upgrade our transactions to, I dunno, have a new field, and this new field will be for blob and not blob transactions, then we have to create two transactions, right? And this kind of, complexity might increase if we like introduce, something else that will have a separate transaction type. 
* So this kind of is some kind of metadata if this transaction has blobs or not. It doesn't have to be a transaction type. but yeah, we need to, we need to have this logic somewhere. So I agree, but not sure if the transaction type is the best thing I was thinking about. think, thinking about transaction type as a, like some of it's last bits as flags, for example, but then we only reserved 127 transaction types, which is a bit, not enough. So for example, if last, if it was like 32 bit, if the last bit is set, then it's, it has blobs. 
* If it's not set, it doesn't have blobs, et cetera. But, we can probably either just, just do the duplication, right? So in this case, or have a separate metadata filled with some flags. But, yeah, that's it. 

**Peter Szilagyi**
* So one thing that and I wanted to add is that I, we very, very often fell into that, I don't know, fault error, whatever. We try to make things super insanely generic from the get-go and we have absolutely no idea why. And from my perspective, that feels like a bad thing to do. For example, saying that, well, we shouldn't introduce spec specialized transactions because we're going to run out of 128 transactions. I mean, that's a very, very big a very, strong argument. 
* So it, it's, I mean, we have absolutely no idea if we will ever introduce another transaction mark or transaction with another field. So it, it, I mean, can, in my opinion, I personally prefer to go with the simple solutions and, try to figure out or try to make it more generic for when, when there's actually a genuine need for it. 
* And yeah, that does mean that we, it might happen that in the future, currently we make a decision that's not the best in the future and the future will join a bit of complexity. But the problem is that if we make it super generic just for reasons, and then we have to tiptoe around that forever and there will never be actually another field ever added, it just feels weird.
* Also, this kind of ties into what Murray's suggestion was that he suggested that we could even cut down more features onto the block transactions. And I don't know, personally, I prefer to have transactions that are, have very, very dedicated use cases. So this whole 4484 has a very, very strong design, a very, very strong use case. And in my opinion, we should try to just focus on that use case and not make this super set of everything. 
* I mean, for sure it's elegant to make the super set of everything, but is there any legitimate reason to do so? Because currently, apart from saying that it's elegant from a theoretical perspective, there's no reason whatsoever that anybody can come up with. 

**Tim Beiko**
* So trying to think what's like the best way forward here. I does feel like, I don't know from the EL side, like having this be like, yeah, having this be more tailored around the current use case seems like it's simpler. there's like some value both in terms of like making a generic framework and, yeah,  and also like ease of use for like L twos if, if we allow zero blob transactions, but it seems kind of marginal. 
* So yeah, I guess, you know, does anyone on the EL side feel like we should like push forward for like a zero blob and sort of more flexible 4844 transaction type, otherwise we can at least make the call that like zero blob transactions shouldn't shunt like be possible. and then, you know, there's this whole other SCC discussion about how we want to approach that.We can go to that after. 
* But I think if, if we all agree that like we shouldn't do zero blob transactions, I think the other thing, the, the other thing to figure out is like, do you ban those in the ME pool only or do you ban them in protocol as well? And Daniel has a question about like what wallets and, chain infrastructure tooling projects thinks. I don't have a great view. Does anyone on the call have one? 

**Danny**
* I would suspect this is currently a very, domain specific debate that most people don't have a perspective on. 

**Tim Beiko**
* And I think the optimism folks seem to like, think this was fine. And generally on the L2 side, my feeling is that whatever gets 4844 shipped the quickest, assuming it, you know, is like a small technical change, like they would probably prefer to work around that and have 4844 a month, 30 or than, you don't have 4844 be delayed because, yeah, because we're not, sort of aligned on the transaction types. 
* And yeah, Alexa has a comment in the chat as well, like, you know, there's also a world where like say we just shipped this and only L2  use this, and we sort of don't have the whole SSZ move happen in Shanghai. so that, sorry, in Cancun, so that's, that's possible as well. and if you went down that route, it's basically only L2 s that have to deal with this new SSZ transaction type maybe is very limited, and then maybe, you know, in the fork after we can like come up with a, with a broader SSZ scheme. 
* So it's, yeah, it doesn't have to, to all happen at once, So unless someone wants to make like a strong case for zero blog transactions, now I feel like we should ban them. and then the question is, you know, should we ban them just in the MEV pool or in the me pool and in protocol for now? does it make life easier if, you know, we just assume they never happen versus we just assume they don't show up in the MEV pool. 

**Danny**
* I believe the zero blob transaction camp generally is assuming those two things happening simultaneously, especially due to the reorg considerations. 

**Tim Beiko**
* Okay. Andrew,

**Andrew Ashikhmin**
* I think we should ban them in the protocol. and it's easier to start with a, with some restricted, functionality and, I agree with Peter that we should, move in, the direction of, more, generality, actually driven by concrete use cases rather than just some, some philosophizing and also bending them both in the protocol and the makes, things consistent and easier to reason about. 

**Tim Beiko**
* Okay. Does that, yeah, that would be my assumption as well. And it's easier to relax that constraint in the future than to start without it then want to add it afterwards. 

**Ansgar Dietrichs**
* Yeah, just very brief wanted to say, just because I think in general I would've preferred to basically not bend them in the protocol. I think it's fine, but I think we can go ahead and, and bend them in for now. But just kind of philosophically, I would say that over time, at least, maybe not at the time, but over time, we should be willing to move more and more towards a world of, specialized MEV pools where basically not having all the functionality offered at all times by the kind of incline MEV would be fine. So for example, kind of every reorgs not being able to reinsert some transactions into the MEV and whatnot, these kind of, considerations I, and I know that are kinda hesitant with that. I think philosophically of long term we could move more towards being willing to have more specialized, out of protocol pools, but for now, I think just banning zero vol transactions everywhere, I think that's the pragmatic chance. 

**Tim Beiko**
* Okay. Does anyone disagree on zero blob transactions, across the entire protocol? 

**Peter Szilagyi**
* So both on chain and in the, Hmm, perhaps one note, that span four but banning is that, I do agree again that it would be an elegant portal  to say that, well, if you use some weird combination of the transaction, then your transactions will not get rein included and you have to go through whatever route you went through the first time to get it to included. 
* But I think that kind of, that sets a strange, precedence, at least for me, that essentially the only way to include such a transaction is to go through some, mining pool or some, some, flash box bundling service. And essentially the only way to re-add it is to monitor the chain and then go through the same bundling service once more. And it, it kind of gets into this weird place where people will just not use normal clients. 
* Everybody will use the bundling service service because it can bundle stuff that the normal client cannot or will not. So I'm not sure that it's, a path that's very, very helpful for the network to go down with. 
* I mean, even nowadays you can see that people are using, all these, works of gap and I'm assuming other clients do that because you can, get some MEV funds, I mean  bonuses for mining, and I think it'll just, every single opportunity where they can make more money, they will just, more and more people will switch over and I mean, that's kind of fine if you have a good enough and fair enough infrastructure built out, but I don't think we have it yet. So I don't think we should push too many people the, that bad.Well, basically every validator having to run flash bots because otherwise it's just not avoid, Right. 

**Tim Beiko**
* And I guess by banning them at the protocol level today, we keep this a bit more fair, with regards to like the public web pool where you, you just don't get this functionality by rallying around Geth  or nevermind. 

**Peter Szilagyi**
* I think it's, it's more of a generic note that, right. so what, what I wanted to say is that, this, reasoning that there will always be some operator which will be able to re-include something that clients cannot, is a dangerous, line of thought. 

**Tim Beiko**
* It's, Yeah. 

**Peter Szilagyi**
* So that's the only thing I would like to, I would like us to keep this in mind to that, for sure we can outsource certain functionality to other actors in the system, but we should, we need to think it over carefully as to what the implications will be. 

**Tim Beiko**
* Yeah, I think that, that sense. Okay. Anything else on the zero blob transactions? if not, then I guess in terms of next steps, could one of the 4844 authors just make, the change to the EIP  to say that, basically type five transactions need a blob? Okay. Angar says he'll do it in the chat. 
* So thank you. and then obviously the, the sort of ripple effect of that is like, as we're continuing like implementing these, these transaction pool designs, we can now take for granted that, blob transactions or type five transactions will come, will a blob and separate those, from the rest of transactions. yeah. okay. 
* And I guess on a like similar note, it might be worth, going into the broader SSZ conversation. So we had a call about this, I think it was literally yesterday. Etan, do you maybe want to give a quick recap of the SSZ call? 

**Etan(Nimbus)**
* Sure. so we still have, like first of all, this is not about the blob SSZ transaction and also not about the zero blob transaction. yesterday's call was, for the representation of transactions as part of the transactions route in the block header. so there are two approaches there. One is based on using a union that is, using the transaction type, to create separate objects underneath depending on that type. 
* The other one is the super set approach, where we use the same, structure as you have on JSON and RPC, where you, essentially have a generalized transaction that can be used to represent all of the transaction types. And yesterday, we could not really decide which one, is better. Both of them have advantages and disadvantages. So we decided that we, simply, create a couple prototypes so that we can actually see in practice on concrete examples how big are the differences between them when they are actually used. 
* Like is a union really that ugly to implement in a serial knowledge circuit, stuff like that. so I will be working on creating those prototypes and, benchmarking them against each other, to be included, in about two weeks. 
* So then we will, take another session to decide whether you want to use the union approach or the, normalized transaction approach to represent those on transactions route. there was also a discussion about dev p2p networking, whether we want to upgrade those as well so that when historic blocks are, historic blocks are downloaded, whether this produced the original encoding based on R LP or whether this produced, union or normalized transaction, that, that was also an open discussion point, but, still undecided as well. yeah, that's a summary from yesterday. 

**Tim Beiko**
* Thank you. any questions, comments? 

**Lukasz Rozmej**
* I have like a time timeline question. is this being considered, in Cancun, right, because it makes sense to be considered in Cancun because we are already adding, SSD transactions so we can like have a form move to SSZ. On the other hand, if it will be considered in Cancun, it will definitely, take longer time, right? 

**Etan(Nimbus)**
* So, yes, the idea was to including it, into Cancun and also to, if it makes sense to align, the common parts of 4844 with it. but, complex parts, like adding the SSZ support to the ELs is already done as part of 4844. So, regardless of whether this is a union type or a normalized type that will go into the transactions route, it is the same complexity. 
* I mean, right now we are just having RLP there. That also works fine. but, yeah. and about bankrupt question, to benchmark, there are things like, when you, when you get approved from based on this tree, how we expensive is to run a verification of a proof in, in a smart contract, for example, how big is the call data? How, how expensive is it to deploy, deploy such a contract, mainly focused on consumers of the proofs. Exactly. 

**Dankrad Feist**
* And so it's about about gas cost of verifying, like proofs, oon a union field or a, an optional field, 

**Etan(Nimbus)**
* Of the union transaction or the, normalized transaction essentially. And also about the different networking codings. just a bite length for those, Right? 

**Tim Beiko**
* Yeah. So what, and so yeah, we have the breakout for this, two weeks from now. And, we're using the typed transaction channel to chat about it in the meantime. I think also on the question of like Cancun, it would be good to consider this alongside like all the other potential things we can do for Cancun. So we haven't quite like made a call for people to come and, and share their various, proposals, for the upgrade yet. 
* So I think  we probably want to do something like that, just so that we have sort of a full picture of what, you know, what we're trading, off against. so I suspect in the next couple calls it probably makes sense to, to try and get a list of like, what are the things people would like to see in Cancun? And then, this, this will be one of those items, but yeah, at least we'll have a full picture for making that decision. and if people, I guess if you, for people listening, if, you already want to start sort of signaling what you'd like, included in Cancun, there's a tag on Eth magicians, Cancun candidates. 
* So if you have your EIP there, you can just add the tag. And then there's also like  a thread about the entire upgrade, for folks, even like if client teams, you know, you have already strong preferences of stuff you'd like to see, it makes sense to just, share those there and we can start, discussing that in the next, couple calls. any, any other questions about, SSE transaction types? if there, there's a comment about the theater magician's being done. It's not down for me. that's weird. 
* We can look into that, offline. okay, next up, I believe Etan, and Mikel, you had another SSE related topic. So basically, moving the withdrawal route from, from the npt commitment to SSZ. do either of you want to give a quick overview of this? 

## SSZ Transactions Breakout Room  #721 [52.38](https://youtu.be/GmwEa_HI2lE?t=3158)
**Etan**
* I can do that as, as well, so thank you. that's mainly the follow up from what we discussed for Shanghai, and also postponed explicitly so that, we can make sure that these withdrawals will follow a similar scheme that we have for transactions and receipts. but conceptually the withdrawals are separate, so it could be that we want, for example, the withdrawals and the deposits from another EIP, to, to be included earlier than the transactions and receipts. So that's why I'm bringing them up separately. 
* And the other thing that I noticed, when I wrote the EIP piece, that the dev P2P specs for how withdrawals are exchanged, I couldn't find them, so maybe that spec is still missing or I didn't check at the correct place, but I wasn't sure if right now with Shanghai, we are exchanging withdrawal in MPL or in RLP orin SSC format on the wire. And if it's RLP, I'm not sure if it has a version by in it. Yes, it's in the bodies and in, in the blockhead there is also root. 

**Tim Beiko**
* Okay. any thoughts, comments on this? 

**Andrew**
* We exchange withdrawals, as a ROP in block bodies, in, EL peer-to-peer. 

**Etan**
* Okay. So just at least no version bite or anything? 

**Andrew**
* No, no version there. 

**Etan**
* Okay. is there a problem when we later transition to SSC or can we like just bump the ETH protocol version, for example, ETH 69 and then use SSC and if it's like Eth 68, then it's RLP or how should this work? 

**Andrew**
* Well, I guess it has to be, doesn't strictly have to be, but, and it's nice if it's consistent with, transactions. And currently for block boards, we use, RLP for both, transactions and withdrawals. 
* So I would actually, if, if we are changing that, then we should change that, like the, the, the marshaling for transactions as well. 

**Etan**
* Yeah, for transaction, it's a mix. It's RLP for everything, but type five. And if it's type five, it's, SSE actually, Yeah, that, that's for the other question, whether this should be bundled or whether we should transition withdrawals earlier. 
* There is one thing to gain with withdrawals, namely that right now there are, there is no single client that depends on this RLP, based M Root in the header. And the longer we wait, the higher, it may become probable that someone is actually starting to use that route for example, rocket Pool could use it for, some rewards computation or something. So not sure if that is a point that we should also consider. Not sure. 

**Tim Beiko**
* And I guess what's the best place to continue this conversation? The Eth Magicians thread, or is there a channel in the Discord as well? 

**Etan**
* Eth magicians, thread exists. I think that one is all right. I'm not sure about a channel. 

**Tim Beiko**
* Okay. So let's use that and hopefully people can review it in the next couple. So that, yeah, we basically can make a call on this, as we're, as we're looking for other Cancun stuff. Anything else? 

**Tim Beiko**
## minimal presets (context) [57.30](https://youtu.be/GmwEa_HI2lE?t=3446)
* Okay. next up. so there was a comment about the minimal presets, which I believe are like the testnet configs for the consensus layer. And that, with 4844, an introduction of block, this, becomes part of the engine api and therefore, EL clients, should be aware of it. does anyone want to give the context on here at second? 

**Dustin**
* Yeah. Oh, sorry. Yeah. Yeah. So, so first I will just sort of introduce very, very briefly, the idea of the middle , yeah, probably it's meant to be used, is for testnets, also the spec test, use them for various things where, it would be infeasible or just slow to run a certain set of tests, in main net presets. functionally  they change a couple of things. They change, well, many things. one of which I'll mention, but the key thing for there is they use, six second slots and, and eight slide pox. And then there's some other segment. But, but they, you end up with 48 second pox and it's quite a bit faster. 
* So, but the relevant thing here  for the most part, these have not, affected the execution layer. and through Capella and Shanghai, that remains as far as I can tell, true. However, in Cancun, that will start changing because there, with the blobs, there is now this blob bundle V one structure, which in the engine API is currently specified is, is hard coded to, number. So the number of field elements is 4,096. This is consistent with the main net preset, but not the minimal preset, which means that, a minimal mode CL attempting to use the engine API will be just speaking in incompatible engine API protocol when it tries to use the engine, get bundle one call, sorry, be one call. 
* Now this is on the one hand you could say, well, this is a very, this is a specific call, a specific data structure, but I think it's worth bringing up here because I think it's the first time as far as I can tell, that the idea of this minimal main net preset has kind of encroached on the engine API on the ELS
* And so the question is kind of at some level what to do about it. one, and so I'm gonna present, I mean, obviously part of present presenting it here is I want, you know, to, if other people have options, that's great, but, but like some options to start with. one is we can just decide that well, it is indeed just for testing, I'll present four options to start with that are meant to be sufficiently, oh, let's say reasonable granularity, cuz subdivide or combine them is desired. One is like, so basically we decide that well the engine API is only for main net. 
* Like that's, and if the consensus back test wanna do some minimal thing, but they don't actually use the engine API cause they don't do any networking things, then that's fine. We, we allow that to break. And anybody running an actual network now runs main net regardless. I would say one downside. 
* And that has obviously upsized of, there's no, there's no, changes required at some level of the engine api. and so the status quote continues working. The downside is it effectively starts deprecating, the minimal preset for anything but pure consensus that tests and they become even more this artificial kind of thing that, that can't be used in practice. 
* So that's for due to a number of considerations would actually Capella exacerbates. So that's option one. Option two, you can have the EL somehow configured at startup because there's nothing fundamental about this number. I mean, it's specified in the engine api, but you can just say, well, the engine API specifies some kind of preset, and you can, the next most general when I'm ordering is an increased generality. 
* Or, or we specific approach is to say the engine set says, the, sorry, the ELs are given some configuration parameter that's basically very specifically this number of field elements and there, and either it's a bullion or it's an integer or, or something. And then you can just make that compatible with the CL. That's option two. 
* Option three is there's an attempt to align things more broadly, with, the sort of idea of minimal maintenance preset. So don't specify this particular field op number of field elements say that, oh, well, the EL now knows about this notion  of, a preset, a minimal maintenance preset. 
* So this is a little bit more elegant, for what it is, but at the same time, like it's something that ELs haven't had to care about and it's kind of strange in some ways that they should have to. and the fourth is a much more general purpose thing, that, and people have at some level, the argument here is this call already starts existing. 
* People are proposed for Capella, an engine API call that will sort of do a kind of a configuration exchange, essentially, not the merge one, where it was just what are, are we ready for merge? But just a more general purpose, what methods are supported and things like this. So those are support four, sort of example options and, and doing nothing is also a choice. So  that's what I wanted to bring up. 

**Tim Beiko**
* Thank you. yeah, Mikhail, you already have your hand up. 

**Mikhail**
* Yeah. For like the last option where the configuration is exchanged in run time, can, you know, create an additional complexity of changing this parameters at the run time? So basically one CL Theoretical can connect to EL and set one, number for this particular config parameter, then the other connects to it and help in Yeah. In general case have to support, you know, switching it over to a lower number or whatever. 
* So that's definitely a complexity on the engineering side. yeah, the pre like, having this as the, common line parameter, I dunno or haven't pass and full specification of, the, CL you know, chain, to, to properly doesn't make, sense because yeah, really has nothing to do with most of those parameters. And I would say that  this, particular case is rather an exception than the common thing that we would like,  we will see in the future. Because here we have block transactions on EL side, which then, included in propagated on CL side. So that's kind of like really, looks like an exceptional case for me. So if we, are about to do anything with that, as you've said, there is an option to do nothing, I would choose, less invasive and less engineering complex, solution, as possible. 
* So yeah, that's kind of like my initial opinion on that. and also I have a question  where, what kind of dev nets or test nets, are we running with a minimal preset? As far as I know, we have like all of the devnets that we have, for, I know for Shanghai and for version for other probably, upgrades, they are on with the mainnet preset, correct me if I'm wrong. 
* So kind of like minimal presets more sounds like, for the, local machine set up or a small, that, that add that, you know, have in your testing or some features and all this kind of stuff. And probably it's not that bad to have field elements, set to like, you know, a mainnet, number in, in that always, I don't know. So that's kind of like my initial opinion on that. 

**Dustin**
* Yeah. I  would broadly agree, I'll say that, certainly once we get to, yeah, I see Barnabas has indeed what, what, what Barnabas said,  also the, but it is true that by the time we get to any, certainly anything publicly visible, the public test net are all, main net figs. I will just speak with Nimbus. 
* I mean, I like anecdotally runs CL often with, with minimal, just its, you know, preset as well, main net. but the other, maybe what I'll say is just the other, aspect and, and you, another option actually is to change the, this particular field and it, I think you mentioned this as well, or this is one of the things you say, but, and to kind of pull this out, maybe least invasive slash fix is the issue in a lot of ways have the minimal presets, just say that, this, this particular parameter is the main net parameter so that we, ensure that the engine API at least is not affected. 
* This affects minimal presets to some extent, yes, it makes them a little less minimal, but it also means that this issue just goes away. and another thing this has come up, and I don't think Hyatt uses it, and this is different than what Barn mentioned, but like you mentioned type and, Hyatt is certainly looking to run, for example, six second slots when they can. 
* Now, there are different ways of doing this. One of them is you can cha take a tweaked main net, preset and just change seconds per slot to six, and that does work. But we also have a pre-existing preset, which is tested. 
* You know, the, that we have, consensus that tests and everything for it that has, is designed exactly to run quickly. And so hype has found this idea useful as well. So I think there's some utility in the minimal, presets enough to not completely not to want to get rid of that. 

**Tim Beiko**
* Oh, and yeah, Gajinder has a comment in the chat about, the KCG libraries have hard coded values, for main net. I guess from this EL teams, does anyone have a strong opinion about this 

**Justin**
* For Besu, it's actually a little less work for us to only support the 4096. Anyone else? 

**Alexey**
* I used to think that it is a fixed number and, we will probably change only block count, possible in a block. so, no stating for that and Right? 

**Tim Beiko**
* Yeah, I don't know, maybe Dankard or proto, is that a right correct assumption that like will only ever grow the number of blobs per blocks, but this, the 4096 field elements per block blob will stay constant? 

**Proto**
* Yes. That's pretty accurate. I, I would not that, that, that's, I mean, what do you mean? Like forever? 

**Dankard**
* Is my forever.

**Tim Beiko**
* Say, two years Right? . 

**Dankard**
* In This case, I mean, I would not want to make this commitment. I mean, it's certainly like an option to long term also grow the, grow the block size. I mean, that's why we are doing four different version of the ceremony so that we can increase the block size. 

**Tim Beiko**
* Okay. So I guess, and there's some comments on the chats now about just saying we can change the minimal preset value of just this for now. there seems to be agreement on that. So does anyone disagree for this specific preset value, to just use the same as mainnet?

**Dustin**
* I mean, I'd be okay with that personally. 

**Tim Beiko**
* Okay. great. So let's, let's do that. if someone can do a PR on the CL specs to update this, it'd be great. 

**Dustin**
* Okay. I'll make that PR Awesome. 

**Tim Beiko**
## Standardize 'txpool' namespace execution-apis#353 [1.11.00](https://youtu.be/GmwEa_HI2lE?t=4264)
* Thank you. okay, next up, there was, discussion around, standardizing the transaction pool name space. Wesley, are you on the call? 

**Wesley**
* Yes. Yeah, I'm here. 

**Tim Beiko**
* Thank you. Yes. Do you want give some context about that? 

**Wesley**
* Sure, yeah. I draft some proposal for standardized TX pool API or execution clients, or spoke to some folks at each of the client teams as most already have some endpoints and custom some implementations for it. But, proposals a way to hopefully find an agreement on a more, common subset, which will be great for interoperability, obviously, but also allows hopefully for more reliable integrations, for example, CR or inclusion that are being discussed at MV Boost, for example. not too familiar with how this process work or how to best approach it, but, you sh I think you shared a link already in the chat. It's also in the, agenda from today's calls. 

**Tim Beiko**
* I'm, yeah, I guess has any EL client dev looked at this and have any opinions they wanna share? 

**Marek**
* I like all standardization efforts. However, I'm wondering if it is worth to change method names, probably people who got used to previous methods names and we could potentially break lots of tool link because of remaining. 

**Wesley**
* Yeah, the rational for, for changing it was actually four backward compatibility because each client currently has their own implementation. changing that would more likely change existing integrations, but just setting up something new would at least avoid, those issues. 

**Tim Beiko**
* Can we do something like just deprecating the Yeah, we can like mark the old names as deprecated, have the clients alias, you know, both behind the scenes and then eventually just remove the old ones from the spec. and I think there is precedent. I think there were some Jason RPC calls. We did Mark as deprecated in the past. I'm not quite sure which ones, but I remember having this conversation a while back. 
* I guess, probably in terms of next steps, if client teams just want to review that PR and, you know, leave any comments or leave like a thumbs up on it, that would be great. And then yeah, maybe we make this change just to deprecate the old APIs, and or mark them as deprecated in the spec. yeah, does that make sense to people? Any objections or other thoughts? Okay. So yeah, let's do that. anything else, Wesley? 

**Wesley**
* No, that was it. 

**Tim Beiko**
* Cool. Thanks. Thank you. and then, okay, so that's what we had already on the agenda, but, Jared, you said you wanted to chat about self-destruct? 

## self-destruct [1.14.00](https://youtu.be/GmwEa_HI2lE?t=4481)
**Jared**
* Yeah. Hi, can you hear me? Yes. Great. hey. Yeah, so, yeah, so we had, I guess where I left off, on self-destruct was, a last piece of analysis around, the potential impact of EIP 4758, which was the approach to just, turn self-destruct into send all and, kind of the, the nuclear option, if you will. that would, potentially, well not even potentially, that would have backwards compatibility or, or would cause, contracts to break. and since then, it kind of seems like there hasn't really been, a proposal that's come forward that has seemed, seemed, or to me at least, seemed actionable to pursue. 
* So I think that, what I'm wondering, to get a read on from people in this call, is whether we think it would be valuable to, put more resources towards analyzing, contracts that would be broken with, for EIP-4758, under the understanding that we probably won't be able to find every broken contract, but, uncovering more could be valuable. I'm just not sure if we have decided that 4758 is completely untenable and to, not pursue it, or it just is not very clear what the, what direction to take here. So I just wanted to get a read from the community here, if anybody has any opinions. 

**Tim Beiko**
* Yeah, thanks. Andrew has his hand up. 

**Andrew**
* Yeah, I think there was another development. there is this EIP 6048, proposed by exec, which might be less, backwards, much not, not as much, backwards breaking. So yeah, it's more backwards compatible than the nuclear option 4758. So I would, I don't know the details, but I think we should contrast that two and, yeah, have a deeper look,  we haven't exhausted the, all the design options yet. 

**Tim Beiko**
* Right? So I've posted the e I p, it's 60 46, I've posted it in the chat, and the idea was that,when you sell this de self-destruct contract, you just change the nos to basically the, the upper, like the max nos value. we don't delete the storage keys would transfer out the funds, which is basically, like sendal. and, and then there was this, I guess the biggest, addition was that you would modify create two.you would modify create two so that, you can actually redeploy a self-constructed contract, but at the same address with different code. but basically, the check you do there is checking that the nos is equal to this, like max nos value.
* So yeah, I guess, and there's a couple comments in the chats about like, we do have to disable self-destruct, and we've sort of announced as part of Shanghai we're gonna do it. So I, yeah, I don't know if people have thoughts about this, 6046 approach or otherwise we could maybe discuss that in more detail on, on the next call. 

**Jared**
* Yeah, I, it, it's been a bit since I looked at 6046, but I wrote in the chat, that I, at least as I recall last time there, or last I read, there were some concerns around, by not re removing storage slots, you're creating, avenues for malicious behavior. And I think the example cited in the thread was, Gino is safe. but yeah, I'll have to look back into that to remind myself Right then this is different in self destruct now, which clears all the storage. 

**Tim Beiko**
* So it's like you're resetting exactly. New, new code with the old data and yeah, that could, Yeah. Any other thoughts? And I guess, yeah, and back to maybe Jared's original question, is it worthwhile to try and like do a extremely thorough analysis of all the contracts that would break on chain with like the 4758 proposal? given we already know there are, you know, several that would break and they're, you know, not trivial. it's not like two random contracts with less than one Eth. It is, you know, there's a fair amount of contracts that that would stop working. I'm not sure what the exact number is, but it's, more than just a handful. Okay. 
* So I guess, not a ton of demand for the more thorough analysis. so maybe, yeah, if in the next like few weeks, client team can look at 6046, or potentially, you know, think about different ways to approach this, we can continue the conversation, in the next call or two. but yeah, I think it's finding what's the least worse, what's the least worse, option Okay. anything else anyone wanted to bring up? Okay, well, shall I, hello? 

**Hsiao**
* Yeah, Just want to comment in on the, oh, that Change? 

**Tim Beiko**
* Yes, please. Yeah. Yeah. 

**Hsiao**
* So I think we've discussed it in the, the 484 4 breakup before. The reason why we have this preset is because the and Python information is very slow compared to the production point. So yeah, so we have, for example, we have, a basic polynomial, proof generation and verification test. And it took like less than one minute to, with minimal preset, but it takes like 28 seconds to run this test case. So that was why I really want to keep the minimal precinct and Right. 

**Tim Beiko**
* Yeah, so it's like a 30x difference. 

**Mikhail**
* Is this 28 seconds just for one test case or there are like hundred test cases, 

**Hsiao**
* So it's only for this test case, but it's the pie test, wrong. So, the test generator will be faster than this, but still, we, currently have the, we use the minimal preset in our CI So you will take this 28 seconds in the CI minutes, right? It and minutes, not seconds. 

**Tim Beiko**
* No, I think it's seconds. So it goes from less than one seconds to 30 seconds? Yeah. 

**Hsiao**
* Yes. And that's only one test case. Yeah, one block, 

**Mikhail**
* To be honest. 30 seconds running once, I mean, like even if it's run on CI, 30 seconds doesn't sound terrible. I don't know if, if we have like a hundred test cases, which yeah, and multiple times 30 if we are jumping from minimum to mainnet recept, yeah, that's something to worry about. But 30 seconds, I don't know. 

**Hsiao**
* Yeah, to be fair, we don't have many test cases. I think probably less than 10 test cases, take the full proof generation and the verification, but I do expect that we will add more test cases after the iterations and, yeah. 

**Tim Beiko**
* Okay. So I guess given the small number of tests, should we just keep it this way or do we wanna discuss this more maybe async or on the consensus specs, on the CL call or I'm not quite sure yet. What's the best approach. 

**Dustin**
* I mean, I'm happy to discuss it in general elsewhere. I guess we'll note without trying two, I mean sort respecting this of the execution like that just in, in general, the fact that this, this occurred, how much, I guess one question would be, for how much of this is an artifact for particularly slow, kcg implementation in, in the test runners and, and how much is it really intrinsic to KZG to say how much is it fixable on a purely engineering side as opposed to a spec like 

**Dankrad**
* This is purely due to a slow implementation, like this is because PA is like a hundred times slower than like efficient implementations. 

**Dustin**
* Right. I think this is an ugly enough problem to, to, to shunt into because, they both, because it would immediately become both an engine and an, execution layer problem or immediately, you know, during testing. if it's, if it's a question of this can be optimized in some way on the test runner side, I, that seems like a better overall investment in for the ecosystem. 

**Mikhail**
* I think that we should start from setting the minimal to mainnet value as discussed before and see if it becomes really annoying, then reiterate on that and think again. Probably we'll see some opposition in the PR which would change. 

**Tim Beiko**
* Okay. Yeah, I think that makes sense. We can just, yeah, we, we can just make the PR for it and continue the discussion there. Oh, and Dustin already has a PR amazingly. great. Anything else to cover before we wrap up? Okay, well thanks everyone. and yeah, talk to you all soon. 
* Thank you. Bye-bye. Thanks. 


### Attendees
* Tim Beiko
* Danny Ryan
* Pooja Ranjan
* Mikhail Kalinin
* Marius
* Wesley
* Barnabas
* Saulius
* Danno
* Lightclient
* Pari
* Ethan
* Mario
* Tomasz
* Oleg 
* Kasey
* Marek
* Crypdough
* Fabio Di
* Terence
* Andrew
* Roman
* Marcin 
* Pop
* Guilaume
* Protolambda
* Carlbeek
* Mike
* Gajinder
* Stefan
* Hsiao-Wei
* Josh
* Phil Ngo
* Alexey
* Holger Drewes
* Dankrad
* Guillaume
* Proto
* Holder Drewes
* Stokes
* Peter Szilagyi
* Sean
* Micah Zoltu
* Jiri Peinlich
* Marius Van Der Wijden
* Potuz
* Evan Van Ness
* Moody
* Tynes
* Alex Beregszaszi
* Marek Moraczyński
* Justin Florentine
* Ben Edgington
* Lion Dapplion
* Mrabino1
* Barnabas Busa
* Łukasz Rozmej
* Péter Szilágyi
* Danno Ferrin
* Andrew Ashikhmin
* Hdrewes
* Crypdough.eth
* Ameziane Hamlat
* Liam Horne
* Georgios Konstantopoulos
* Mehdi Aouadi
* Bob Summerwill
* Jesse Pollak
* Stefan Bratanov
* Sara Reynolds
* Caspar Schwarz-Schilling
* Ahmad Bitar
* Marcin Sobczak
* Kasey Kirkham
* Sean Anderson
* Saulius Grigaitis
* Ruben
* George Kadianakis
* Dankrad Feist
* Andrei Maiboroda
* Gcolvin
* Ansgar Dietrichs
* Jared Wasinger
* Diego López León
* Daniel Celeda
* Trent
* Mario Vega
* Kamil Chodoła
* Ziogaschr
* Kevaundray
* Antonio Sanso
* Oleg Jakushkin
* Leo
* Nishant Das
* Pote
* Sam
* Tomasz K. Stanczak
* Matt Nelson
* Gary Schulte
* Rory Arredondo

-------------------------------------

## Next Meeting
Mar 2, 2023, 14:00-15:30 UTC

