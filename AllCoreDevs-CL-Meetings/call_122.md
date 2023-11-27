# Consensus Layer Call 122

### Meeting Date/Time: Thursday 2023/11/16 at 14:00 UTC
### Meeting Duration: 1.5 hour  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/900) 
### [Audio/Video of the meeting](https://youtu.be/wSE8e9MZz3k) 
### Moderator: Danny Ryan
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
122.1  |**Blob Sidecar Networking Updates:** Lighthouse: Pretty much done development. Will need until the end of next week to review and test the new code.
122.2  |**Blob Sidecar Networking Updates:** Teku: New gossip validation implemented. Working on builder workflow.
122.3  |**Blob Sidecar Networking Updates:** Lodestar: On track to finish implementation by end of this week.
122.4  |**Blob Sidecar Networking Updates:** Prysm: On track to finish implementation by the end of next week. Will need another week thereafter to put together the builder workflow.
122.5  |**CL client updates**: Ryan suggested planning the launch of Devnet #12 during the next ACD call. Barnabas Busa, a DevOps Engineer at the Ethereum Foundation (EF), said a “reasonable” target launch date for the next Cancun/Deneb devnet would be November 29th or 30th. Parithosh Jayanthi, also a DevOps Engineer at the EF, asked for an update on hive tests. Mario Vega, on the testing team at the EF, confirmed that the basic hive tests for the upgrade are ready to go. His team will be adding new test cases for the builder and “blobber” workflows to the hive test suite over the next few weeks.
122.6  |**CL client updates** Teku developer Enrico Del Fante raised a question about the proper conditions that should provoke CL clients to use the “byRoot” RPC request to retrieve missing blocks and blobs post-Cancun/Deneb. Del Fante’s questions about these conditions are explained in detail here. Other developers on the call were supportive about adding clarity to CL specifications as to when blobs and blocks should be received by a client through an import via an RPC request if the client has not received them through gossip. Developers also discussed the conditions that need to be met for other clients to answer RPC requests for blocks and blobs. Prysm developer Terence Tsao highlighted that there are essentially “three levels” to these conditions. A client may have received a blob or block through the peer-to-peer networking layer of Ethereum. The second layer is the client receiving this blob or block through gossip and verifying the message through the state transition function. The third and final layer is the client receiving all necessary information about a block and its associated blobs. Developers debated which level is necessary to meet in Cancun specifications regarding Del Fante’s question.
122.7  |**Addressing EL Client Diversity Concerns**  Szilágyi’s “Making EL Diversity Moot” proposal. Geth developer Marius van der Wijden shared a summary of the proposal on the call, explaining that the “worst case scenario” that this proposal seeks to address is if a majority client has a bug that causes most validators on Ethereum to get slashed and forcefully exited from the network. Instead of encouraging users running a majority client to switch to a minority client, Szilágyi’s proposal suggests encouraging users to cross-validate their existing client with other minority clients.
122.8  |**Addressing EL Client Diversity Concerns:** Nethermind developer Łukasz Rozmej said that he was not favorable to the proposal because the additional work for EL clients to cross-validate their blocks with other clients would introduce latency to the block production process. In addition, Rozmej said that he would prefer the work to build production ready stateless Ethereum clients come after the Verkle Trie upgrade. Rozmej also asked how clients would handle block production if cross-validation with other clients fails. To solve for this, Ryan suggests an “n of m” approach. If cross-validation of a block is successful with at least 3 out of 6 clients, the validators will continue to attest to blocks, otherwise, attestations will be halte


**Danny**
* Okay. Welcome to Consensus Layer Meeting 122. this is issue 900 in the PM repo. hopefully short and sweet, but we shall see. so first and foremost, usually we have, you know, testing slash dev nets, but instead we have blob sidecar networking updates, slash status because testing and dev nets and other things are generally blocked on the consensus layer rework that is currently underway.
* So I'd love to get like a general status update. And then we have one issue posted by Enrico around when to serve certain messages that we can talk about. most core devs, that's the name of somebody on the zoom,  which teams are behind there, just so we know. 

**Most Core devs**
* All teams. Okay. 

**Danny**
* A lot of teams. 

**Most Core devs**
* Yeah, like 40 people here think. Oh, shit. 

**Danny**
* Hello? 

**Most Core devs**
* Hello. 

**Danny**
* Do you have a video? Yeah. Your depth of field is very short. 

**Most Core devs**
* That's probably just. 

**Danny**
* A nice. 

**Most Core devs**
* Cool. 

**Danny**
* So I would really like to hear from the various Consensus teams on just a status update on the rework, the networking rework with respect to the spec changes. A couple of weeks ago. who wants to get us started? 

**Speaker C**
* So we're pretty. Much done with development. I think we would need to the end of next week in order to get through review and finish up testing, but yeah, that's about it. 

**Danny**
* Next. 

**Enrico Del Fante**
* From the tech team. work is in progress. We implemented the new gossip, validation. We are migrating all the data structure that are needed to be migrated out. We are working on the builder flow and. Yeah, working progress on track with timings. 

**Gajinder**
* Our LOBSTR. Aim to complete this in this week. Hopefully next week. Lots should be ready. 

**Terence**
* For Prism. I think for the normal path, which is without builder, I think end of next week which is fairly doable, but with the builder probably need one more week, which is probably fine because like builder takes a while to set up anyway. 

**Danny**
* Enrico real quick. When you said on track with timings, did you generally mean kind of. 

**Enrico Del Fante**
* Yeah, I think I guess a couple of weeks seems like reasonable. 

**Most Core devs**
* And anyone from the embassy. I guess we got no one from Nimbus. Yeah, I don't think so. Okay, cool. 

**Danny**
* So it sounds like we are not ready to plan Devnet, but we're ready to kind of pre plan talking about it again. so at least let's bring it up on next week, get another status update. And that'll inform whether we're kind of. No. Working on some proto devnet the following week or maybe the week after. Obviously, DevOps folks, if you want to have keep a closer eye on the pulse, maybe you can do some some pre-work.
* You know, if a team or two want to start experimenting at the end of next week, but I'll leave that up to you all. 

**Most Core devs**
* That sounds good. Ideally, I think it would be very good if we could launch something next week like dev net 12 next week, but if we're not going to have more than two clients ready, then maybe a week after that. And but like end of November is probably like 29th to 30th November is probably more reasonable for what's the. 

**Speaker I**
* Status on test. We already have them updated and other clients that are ready already testing on that. 

**Mario Vega**
* Hey. Yes. So we're basically ready on the Mac Builder and on the blubber side. So we are ready to start testing the builder. I mean, the normal flow, the builder and the blubber and stuff. I've added some interesting test cases on the blubber. I will try to share them as soon as possible on the R&D. basically just equivocating, block headers and all that stuff.
* Should be should be ready to go. so yeah, we are basically ready just adding more test cases. That would be ideal over the course of the next week. But the basic stuff is ready. 

**Most Core devs**
* Sounds good. So if we can have like a some client branches ready to go by end of next week, then we can do a test a week after that on Monday, Tuesday, then we can launch on Wednesday around the 28th. And if that goes smoothly, maybe we can forge early and mid December. Sounds right. 

**Danny**
* I'm not going to commit to a date, but I do think that certainly next week we can start preparing for Devnet 12, whether that's all clients or a couple. Okay. Anything else related to this item. Okay, cool. So the next one is kind of related, at least to some of the edge cases that come up in this. Enrico did just toss a comment on there, but can you give the. Quick on this and we can discuss. 

## Serving blocks and blob_sidecars in RPC byRoot right after they passed gossip validation consensus-specs#3547 [11.30](https://youtu.be/wSE8e9MZz3k?t=697)
**Enrico Del Fante**
* Yeah, sure. So I was thinking about highlighting a difference that will be introduced by the NAB in terms of usage of block by root and blocks by root requests. Because before the NAB, what happens is that if a if a node misses a block sent by gossip, the moment in which he the node will start using RPC is when first it receives an attestation, voting on that block, or even if the receiver if he receives the the next block building on top of it.
* In both cases, the most of the network probably has already imported that block. So if the all the clients actually serves only blocks that are fully imported, it's most likely that that node will be successful in in retrieving the block by root. But. With Deneb, a node, we will be able to be aware of that something of an of a block or a block that he missed by via gossip. Way before then, that this is because we can receive a bunch of set of messages that are related to the same block route. 

**Danny**
* There's a native a native race condition rather than like an accidental, sometimes race condition. 

**Enrico Del Fante**
* What do you mean by that? 

**Danny**
* Like built into the protocols. We're sending messages that have linked dependencies at the same exact time. Yeah. Yeah. 

**Enrico Del Fante**
* Exactly. So that this is this is perfectly a consequence of splitting and decoupling blobs and blobs, blobs and block, which means that potentially the node could decide to do a by root request booth on blobs and two blocks a little bit before that. But if the client still serves those RPC requests only. For blobs and blobs that are fully imported. There is a high chance that those early blocks. Those early by root request probably fails.
* So this is related to a logic that we already implemented in Teco, which is a logic that tries to recover when something is missing and the attestation due is coming. And now it's time to to attest. So we still give some time to the gossip layer to receive the, the missed message. But at some point we try immediately to do by request. So I was thinking if, clients could start serving messages that has been validated via gossip and not fully imported yet.
* I think this the Teko behavior could could receive some benefits on doing that. So it will be some early recovery and give them more chance to nodes  to attest to the right thing. from a security perspective, I think like receiving things that are validated via gossip or actively requesting for a particular message. Doesn't think to me, doesn't feel to me that this this any particular different. 

**Terence**
* I guess I have a question. So do clients wait until they have all the blocks and the blobs? Assuming there's blobs for the block and before everything, then start running the state transition function because like theoretically you can do everything in parallel like a pipeline, right? Because you can do the consensus first, and then the execution can also be in parallel of the consensus. And then after that, you just wait until you have all the blobs, because that will save you at least like a couple hundred milliseconds least. That's yeah, this is what Prism does. 

**Enrico Del Fante**
* Teko does that as well. So at some point you could have three actually three pipelines in parallel. One is the state transition because we start doing the block import as soon as we receive the block. Then there is this pool of of blob sidecars that are building up gradually. And then at some point we also engage the execution layer. So there will be blobs block validation with three transition and execution layer that does the payload validation. But it doesn't mean that at some point you really need those blobs to fully import the block.
* So if you have the blob and three of out of four blobs. And you're still waiting. But you could have some time to to to get the missing blob earlier and actually import everything before attestation. You. 

**Danny**
* I mean, my intuition here is that like. Being able to request the message and the responder. The message sending it to you upon the same conditions that they would have forwarded on. Gossip is not increasingly attack vector and then potentially removing it from such message responses in the event that it failed full validation. I think it's worth that optimization to keep the network kind of lubricated here.

**Enrico Del Fante**
* I also think that with blobs number rising, maybe the chance that one of those are missed maybe rises. And but this is also valid for from the block perspective. So we received all the blobs but we missed the block. And we can do an RPC by route. for the block itself. 

**Speaker C**
* We think we already do have this behavior where we start serving blobs or the block prior to import the RPC, but from the when we were requesting, we actually are delaying our by rich request to sort of like optimistically listen on gossip, because we've noticed that it's more likely that we just end up receiving it on gossip later than we complete an RPC request in time to actually test. So generally, like I support this sort of, I guess, clarity and how we should behave in RPC.
* But yeah, I'm not sure how necessary it is in terms of like attesting to time, but it seems better to try to like seed the network more quickly. I guess. even if we don't have blocks and blobs fully verified together. 

**Danny**
* Yeah. Mean. Guess there's two things here. One is like how a node should heuristically kind of decide when to switch from. I'm going to rely on the gossip to actually I should go find these messages and I'm not certain if we should that should land in the spec, but the clarity on is it okay to serve messages that have. Past the gossip validations, only to potentially remove them from things you might serve in the event that it fails. Full validation. Think that that is definitely my opinion is that's the way to go. And if we want to make sure it's clear in the spec,
* I'm definitely cool with that. Does anybody dissent from that opinion that like if it passes gossip validation while you're doing full validation, it's okay to serve. 

**Most Core devs**
* So I will say it is more complicated to implement, but I do think it's better. 

**Mario Vega**
* And Mikhail is here. 

**Mikhail**
* I just have a question. Which case we try to optimize. So as, as far as I understand, a know a remote peer sent you a block and you assume that it has also this peer has also received a block. Right. And this block passes gossip validation. But then this peer must have sent you this block as well. So we are optimizing for the case when this push from that peer push of the block has failed. And we are requesting it by root. Right. Am I understanding this correctly? So the peer tried to send you this block via gossip, but did not but fail to do this. Only in this case this pirate request will make any difference in my opinion. 

**Enrico Del Fante**
* Yeah, I was also thinking about doing that. Yeah. Yeah, that's that's the optimization. So if for some reason you got some kind of, uh, networking glitch that. That prevents you to get those messages. One of those. 

**Danny**
* These are different message. Like it's not. I didn't understand like the push versus pull thing here, but like if receive message A and B on the message I'm expecting and then they have a dependency which is message C and didn't get message C, it's a matter of who's going to respond to my query for message C, is it people that have only fully validated message C, or is it people that have validated the gossip conditions of message C? 

**Terence**
* I think there is a difference, right? Because you can pass gossip, but you don't verify the state transition function. Right. So I think there is three levels to it. The first level is you pass gossip. The second level is you pass state transition function. And then the third level is that you have everything right. And I think it's probably better to serve only if you pass state transition function. Because say if today like an attestation is bad in a blog, you will still serve it versus you actually verify it. 

**Danny**
* So I mean, we definitely can't gate on the third because then it would be very difficult to recover because only nodes that have seen everything would be able to actually respond. I'm arguing we should only gate on the first, because arguably those conditions made it safe from an anti-ddos perspective to forward the message to your peers on gossip. So it's arguably safe if somebody requests it from you. obviously. Like. You could add the additional full validation, but I don't think it really buys you anything with respect to security. And just takes more time. 

**Terence**
* It's also easier to implement if it's just the first guess from Prism perspective. 

**Danny**
* Sean said the other ways. 

**Enrico Del Fante**
* Well, okay. For tech, it's the same though. So if we we have this pool of things that has been validated and passed the Gossip validation. So we only have the first. And I was thinking about serving only that set of data. 

**Most Core devs**
* So for prism the. Problem is where they are stored. So if we if we go to an an approach where the things that haven't been completely seen and validated are stored differently, that those that were already seen and validated, then when you're getting a request by route, it becomes a little trickier to be looking into different places for blobs to serve. 

**Terence**
* But what I don't understand is that if today you pass gossip, you should be able to run state transition function right after, right? So there is not that big of a difference. And then and then the state transition function is quite fast anyway. 

**Danny**
* Yeah, but if you're talking about like 200 milliseconds to run it and you're talking about a network that's trying to heal or repair itself, like in these four second windows, it could be meaningful. Obviously, that's just kind of an intuition. And I don't totally know the impact of those on those requests, but. 

**Terence**
* Yeah, that's a fair point. 

**Most Core devs**
* So one one idea that we had a long time back, was like, you guys are like, making a kind of binary whether to run the checks or not. And when deal with B2B, not make this binary, but say, okay, every second request, we run the state transition function before we distribute the block or not. And if we we can do some like we can use the peer scoring and say, okay, for peers where we have a higher confidence that those are good peers, we run the  forward the block directly or we forward their block directly without checking it.
* And for peers that are lower scored, the probability like you will the way we implemented it back in the day, it was not on Ethereit was on a different project. Was that you? I don't know. You took a normal pill. Would have like a 50% chance. And on every on every block you will you receive  you would evaluate it whether like you would generate a random number between 1 and 2 or whatever, one and 50. And if it's below 50 then  you would evaluate it before you send it out.
* And the more confident you became in that peer, the higher the  probability is to send the block out without verifying it. So that might and  that would what this would give us is basically in the happy scenario. If there's no bad blocks on the network, no bad attestations. We are in this fast mode where we just like we just propagate everything that the without checking it. And if we start seeing attestations, we will check stuff and, and kind of prevent the propagation of, of those bad things. 

**Enrico Del Fante**
* Will apply on the, on, on, on the gossip side for us because I think we, we decide t to gossip thing only when we pass it  the validation of the gossip. But we don't try to do the state transition and then after that to say, okay, let's, let's disseminate the message. It will be too slow. 

**Danny**
* Yeah. I mean, to be fair, like on gossip, we do, we do have anti dose checks and those are primarily around the proposer signature. And so I just think it's okay to revamp that to the request response here I do I do like the design space that you're talking about with respect to gossip here. Marius because it's certainly very interesting. But I don't think that we need to hoist that into the gossip here. So, I mean, this could this could show up in a spec in spec as should or may respond to queries. you know, rather than a must.
* But I do think that it makes sense to clarify this one way or the other. Enrico, would you be willing to open up a PR against the Beirut to. At least. Show a version of this, and then we can try to land it in spec next week. 

**Enrico Del Fante**
* Sorry. Danny you're saying to me. 

**Danny**
* Yeah. Said would do it?

**Enrico Del Fante**
* Yeah, sure. 

**Danny**
* That is the last item on the agenda. Does anyone else have anything they want to talk about today? 

**Most Core Devs**
* And if there's nothing else on the consensus layer, there was a proposal from Peter yesterday about building stateless clients on the on the execution layer in order to help with client diversity. If we have still some time left, it would be nice to just get this thought out there. 

**Danny**
* Yeah. Does somebody want to give the tldr? I'm happy to. If not. 

**Most Core devs**
* I can I Can give the basically the worst case scenario is if a majority client. It has some bug and we finalized this bug, and everyone who runs this majority client will get slashed and cannot participate in the network anymore. 
* The idea behind this proposal is basically you don't. You not only run one client, but you run all of the clients, but you run most of the clients in a stateless mode. So whenever you receive a block, you will have one client that you run in a stateful mode. And you will execute this client in the stateful mode. And executing the block on it will generate a witness. And you take this witness, you put it somewhere memory map file or whatever, and then you call all of the other clients in stateless mode with this witness and verify that they also execute the same block correctly.
* And if they execute the same block the same way, or if, like  and out of executed the block correctly. And then, and only then would you attest to it.
* And this stateless execution is very easy to implement in in execution layer clients. You basically just need to have a different database that you can feed this witness to. And EVM Just take the take the state out of this this different state database. And yeah that's basically it. And so. We because all of this can be done in memory. This this this witness database can be can be a memory database. The witness data itself can be a memory mapped file. doing this would, should be extremely quick and it would just require some additional CPU time.
* And what this would give us is that every client would, would execute the block on all different implement execution layer implementations before attesting to it, which would prevent us from finalizing a block in a bad block in a minority in a majority client. That's basically the proposal. And so what we would need to do for that is for every execution layer client to implement a way to get the witness for a block and a way to execute a block in stateless mode with the with a given a witness. 
* And the cool thing about it is stateless execution is something that we sorry, that we want to target with, with virtual anyway. And so if we were to build this right now, as I said, it's not it's not hard to build. But most of this code can also be used for for worker. And so we would already have stateless clients, the stateless clients. They are not really feasible for thinking the chain or these kind of things. Because the witnesses in Merkle, Patricia tries are kind of big or can be big in these in some, in some cases.
* But because we are not sending the data over the network, we only have it, within our node, within our computer. It's not a big problem. So yeah, that would be the proposal. I think we are going to implement it. I think visa was also already looking into it, and I think some other clients are also convinced now hopefully to, to also join. 

**Speaker N**
* An interesting add here is that although haven't been about all the eels. It's possible, but. It's possible that eels is fast. Is fast enough that you could do this sort of verification against eels. So potentially you could actually check how valid data is checked as well as the proper execution. Clients thinking like invalid. The the occasion think of the block is valid, which could be another layer of protection. 

**Speaker M**
* And it might also work with Ethereum JS actually. So like even the clients that cannot sync it right now because the state is so big and as loads and stores are so heavy, and we can still use the EVM to to verify, verify the state transition on the execution areas. 

**Speaker O**
* Can I can I ask a question. So I'm not super familiar with the statelessness stuff, but do you prove the validity of the inputs with respect to the pre state hash. Because I'm thinking this this stateless client doesn't have any continuity. So it will just verify anything. Like if you could give it inputs with valid execution and it would say yeah that's fine. So how does it know. That it's executing a block that is really part of the chain. 

**Speaker M**
* So you, you you execute the you execute the state transition and you mark all of the trie nodes that you touched or that have been modified. Yeah. During the state transition. And you prove all of them to the state of the state. Yeah. And that's it. And you give them both state route. 

**Speaker K**
* But it's running on your machine as well. Like the client that generates the witness. Yeah. All other clients running on the same machine. I mean, like in terms of security. 

**Speaker O**
* I mean, like if, say, if Geth has the bug in its database, can that break the guarantee somehow? Like, if it generates a valid proof from no corrupt data. 

**Speaker M**
* Then it wouldn't be able to generate the value to the old state route. 

**Speaker O**
* But not one stateless client doesn't do what the old state route is though. So it could just generate it could generate a proof to an old invalid state. Right now the stateless. 

**Speaker M**
* Client would need to have the have the old state route. 

**Speaker O**
* So the stateless does keep track of something between each execution. 

**Speaker M**
* The state could. 

**Speaker G**
* Yeah keep track of and. 

**Speaker P**
* You could just say, hey, the state route for the last block was right. It needs a chain of state routes. 

**Speaker G**
* Okay, but wait. 

**Speaker O**
* But then we're sort of still that's part of the trusted input, right? Like you have to trust that that is not going to pass as bad state. Or you. 

**Speaker G**
* Could. Yeah I think that's a it's not a real issue. 

**Speaker O**
* It's more of a yeah. 

**Speaker G**
* Yeah. 

**Danny**
* I mean for me I'm. 

**Speaker P**
* Still trying to understand, is it possible to do this without the state witness because it's like you already trust your clients to get the right things and send it over. So you need to it's kind of important to do the verification because you want to make sure you're running the code that's going to calculate the state routes at the end of the block. Yeah. So if there is something wrong there, but it's not quite the same code because you are reading and writing to a different backend for the data. And so it's, there's, there's some more overlap than having the zero state proof data.
* But it's not, you know, 100% like there are bugs that can happen on real clients that wouldn't have this. 

**Speaker N**
* I would say think that like, we could you could consider like not actually doing the like state verification and just like telling the client this was the state. This is all the accounts and storage fees we have and what their values were. And here is the post value of every account that you wrote. And that would that wouldn't catch a bug if there was a bug in like the vertical or vertical tree, but it would catch any bug in the end. And like I suspect in practice, I feel like almost all of the attack surface and like the scope for bugs is actually in the oven.
* So if we implement this in a way that like it doesn't catch like a small category of bugs, like bugs in the implementation of the Merkle tree, or bugs like in some of the block building, like catches as much as reasonably possible. We could cut some corners and probably say or. 

**Danny**
* Bugs in like stateful caches and things like that. Hey, just want to interject and give Lukas a second. 

**Lukas**
* Yeah. Can you hear me? 
* Okay, so while it's technically all this is correct,  I'm not I'm like not that favorable for this proposal because it has few things. Firstly, it increases latency. Generating the proof and then checking with other CL clients will increase latency on block validation. So we are already increasing latency with Cancun potentially, and this will increase it even more. Secondly, I agree it's very easy to implement in terms of EVM and executing EVM in the client, but all the things related to integrating this with between the clients and integrating this with CL clients will is not that easy.
* And I think it's the estimations here are too optimistic and I would prefer to put this effort to actually finalizing Verkal trees. And if someone isn't, isn't like looking into Verkal trees very carefully. There was tremendous progress in Verkal trees this year, to the point that I think it's close to completion. And Verkal trees would allow us to do it better because we will we would have this things in protocol. So we could have multiple clients like doing this at the same time without introducing any latency more than just the Verkal trees, because there might be a bit of latency just by distributing the the witnesses.
* But it's something we probably want to do regardless. So putting a lot of effort, and I think it would be a lot of effort into that just to throw it away in a few months after, I think it might be just the wrong way. And the last, last thing if I can, if I can finish, is how would the train behave if, for example, we would have a bug and one of the clients and most of validators would run this client and get, for example, and they wouldn't agree on on, would the train just stop at all, or would it just not finalize what would be the proposed solution here? 

**Most Core Dev**
* I think the proposed solution would be for the for the chain of to finalize. and people just not to not attesting to the blob. So the chain will finalize. That's a very. 

**Danny**
* There's a lot of nuance to to how to potentially do that. Mean like the safest version of this to find some balance is like doing rather than n of n do n of m where you know it's you can if one fails or something, you can still continue forward. But if you have some over some high threshold of failure, then you don't continue forward. and try to find the balance between kind of safety and available chain. But not just not a testing is a potential major security issue.  

**Most Core Dev**
* Yeah. And the, the other things that. So, as I said, I think proto said today that they already have it and they implemented it in a day. So I think it's not that much effort and it should be implementable. And that's proto.  Yeah. But we I think the Geth team is definitely going to implement it. And then we can see how much effort it is. And then we can also see how much overhead that is. Like we don't know. We don't know how much CPU it is, how big the witnesses will be collecting the witness is extremely easy. So collecting the witness because you have to go through the tree anyway.
* You it's just whenever you touch something you you also record the touch into a map. And then at the end, like you put out the map. So it's very easy to, to collect the witness. 

**Lukas**
* But no, no, proving the witness is harder if you go through the snapshot to load things. It's one call to the database. If you want to prove it, you have to go through the entire tree, so you increase latency. 

**Danny**
* Another thing to consider here is like this might there's may be a second order effect to at least keep in mind I'm going down this path is that this might help with resilience with respect to Multi-client state transition, but it might actually reinforce fragility in other portions of the stack. If, for example, you have less of a reason to switch from a majority client because you get the the kind of the EVM state transition resilience, then all of a sudden all of the other things become, you know, like potential factors with respect to database or, crashes on P2P and things like that.
* Like if there's less of an incentive to diversify on these other things, you might actually end up with more fragility in other parts of the stack. then if there were a theoretical healthy.

**Most Core Dev**
* Yeah. Diversity across. But I think it's the right thing to do for the health  of the network. and like what? I think the most important thing is that we're not going that we're not finalizing any invalid state. This is way more important than like if Geth has like 50 or 60% of the network. So this is I think this is the biggest nightmare scenario. And with this proposal, we have a good chance of making this worst night some nightmare scenario. quite significantly better. And, so, yeah, just as a heads up, it doesn't it doesn't need any. It doesn't need by bones from all of all the teams. But I think it would be really good for the whole of Ethereum that we, that we have this

**Most Core Dev**
* On the topic of latency, I think we could also just only do the proof once per epoch because mean I mean the check, the cross check because the main thing is you don't want to finalize an invalid block and that's just dependent on the target of the attestation. Right? So if that target block has already been checked with all the clients, you can sort of attest to whatever head blow you like. If that head block is invalid, it's not going to count towards the Casper FFG weight and you're not going to finalize. so this could be something that we just need to run at the beginning of the epoch on the epoch transition, which is like a 32 x reduction in the number of times it has to happen. 

**Most Core Dev**
* Don't think that latency will actually be an issue at all, because this is just a few. And most of the Geth least in most of the latency comes from like like fetching data from the disk. Yeah, I think the best way forward is to. While some teams to implement it that have the capacity to do it and then just just to benchmark it and see the numbers and see if like the full approach with proving everything and being as secure as possible. If that is not feasible, then we can we can reduce the security of it. Yeah. 

**Andrew**
* When I think in general, I agree with Lukasz. I think that in general, well, I think in general it's a good idea, but I would do it with Verkal because then we can agree on the standard and we don't have a custom built just for that. 

**Lukas**
* But you. Like I said, for generating the proofs, you need to. You throw out the the snapshots. You need to traverse the tree all the time. So for each read. So that increases latency in itself. So that's basically the event. The first processing is increased latency a lot. And then depending on how the proofs are moved and distributed which will have some latency. And then there will be some execution on the other, uh, verifying clients. And for example, if we have a very compute heavy block which can be attacked vector, again it might be a problem. Right. But again, feel free to benchmark.
* I'm just stating my concerns and that I think, yeah, the effort is underestimated to make it actually happen on the production level because it's very easy to prototype it. We have it, we had it in beam sync. We have it on vertical trees right now. And I agree that just the EVM part is simple. You just need to substitute the data source. But I disagree that it's like easy on the protocol level  to deploy it on the network. Okay. It's not protocol even, but you know what I mean. 

**Most Core Dev**
* Yeah I think we go consensus. 

**Most Core Dev**
* So it was someone else trying to talk? Like if we want to, if we want to have the situation where we can continue producing blocks but just stop at testing. The CEO currently has no way of understanding that from the. We just have an idea of whether or not it's valid or not. And if a block is valid, then we're producing blocks and attestations for that block. We almost need like a concept in the engine of like this block is sinking or like unsafe for testing, but go ahead and produce something on top of it if you want to. 

**Danny**
* But then the I mean the implications there of having like an attestation list for choices. Something to think about. I would motion to the fact that I think we all at least understand the proposal and can think about it, and Geth and others can do R&D and bring back to All core devs what they learn, rather than spending another 45 minutes talking about it here. Is that reasonable? 

**Most Core devs**
* Yeah. 

**Speaker G**
* Cool. Thank you. Maurice. 

**Danny**
* Other items for today. Where's the outfit party? I'm currently in a hotel bathroom, so it's definitely not here. anyway, hope you all are all well. If you are in person, enjoy. And if not, see you all very soon. Take care. Bye, guys. There is the All core dev execution there called tomorrow. Next week during Thanksgiving, us Thanksgiving. All right. 



---- 


### Attendees
* Danny
* Tim
* Arnetheduck
* Marek
* Lance
* Micah
* Paul Hauner
* Ben Edgington
* Loin Dapplion
* Terence
* Enrico Del Fante
* Pooja Ranjan
* Hsiao-Wei Wang
* Saulius Grigaitis 
* Roberto B
* Olegjakushkin
* Chris Hager
* Stokes
* Dankrad Feist
* Caspar Schwarz
* Seananderson
* Andrew
* Crypdough.eth
* Zahary
* Matt Nelson
* George Avsetsin
* James HE
* Marius
* Ansgar Dietrichs
* Lightclient
* Stefan Bratanov
* Afri 
* Ahmad Bitar
* Lightclient
* Nishant
* Gabi
* Pari
* Jimmy Chen
* Gajinder
* Ruben
* Mikhail
* Zahary
* Daniel Lehrner
* Andrew
* Daniel Lehrner
* Fredrik
* Kasey Kirkham
* Protolambda
* Cayman Nava
* Stefan Bratanov
* Ziad Ghali
* Barnabas Busa
* Potuz
* Trent
* Jesse Pollak
* Carlbeek




