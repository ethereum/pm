# Consensus Layer Call 136

### Meeting Date/Time: Thursday 2024/6/27 at 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1084) 
### [Audio/Video of the meeting](https://youtu.be/T-w5dzte36c) 
### Moderator: Stokes
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
136.1  | **New Research**: orge Arce-Garro, a researcher at Nethermind, shared a presentation on his team’s latest efforts to improve the way data about client diversity is reported by node operators. The research was funded through a grant from the EF. It offers three different approaches to facilitate the communication of client type by a validator node operator and assesses each approach based on complexity, security, and ability to protect the anonymity of node operators. Arce-Garro requested feedback on his team’s research, which is posted on Ethresearch.
136.2  | **New Research**: Geth developer Péter Szilágyi shared updates on his team’s work to support EL cross-validation. This was an idea first raised by Szilágyi in November 2023 to improve the resiliency of Ethereum in the event of a catastrophic bug in a majority client. EL cross-validation is aimed at enabling the verification of blocks with multiple clients. This way if the results of block verification with one client differs from another, node operators can refuse to accept or attest to the block and thereby prevent a potential chain split in the event of one client failure.
136.3  | **Electra Updates**: EF DevOps Engineer Parithosh Jayanthi said that his team is waiting on EL client teams to launch Pectra Devnet 1. Teku developer Mikhail Kalinin said that he has finalized specifications changes to EIP 6110, which adds a queuing mechanism for processing new validator deposit requests from the EL on the CL. Kalinin requested feedback from developers on his proposed changes.
136.4  | **Electra Updates**: Barnabas Busa shared an update on PeerDAS development. He noted that the second devnet for PeerDAS is live with three different CL client implementation. Busa added that his team has begun stress testing the devnet and already discovered a few issues in client implementations, which client teams are working on fixing.
136.5  | **Electra Updates**: Stokes noted that there are outstanding open-ended questions about PeerDAS implementation that include how the blob gas limit should be communicated between the EL and CL, as well as how the blob base fee calculation should be similarly handled. There are multiple proposals developers are weighing to address these issues. Stokes asked that developers review these proposals more closely over the next few weeks so that they can come to an agreement about them on a future call.
136.6  | **Electra Updates**: Nimbus developer Etan Kissling shared updates on implementation work for EIP 7688 and EIP 6493. These are two code changes related to upgrading Ethereum’s data serialization methods that have not yet been formally accepted into the Pectra upgrade but that certain developers are keen on including posthaste. Kissling said that he would like to see EIP 7688 included in Pectra Devnet 2, which drew some concern from client team representatives and the EF DevOps team. Stokes suggested that developers reassess the readiness of EIP 7688 for inclusion in a Pectra devnet at a later date.
136.7  | **Electra Updates**: On EIP 6493 progress, Kissling shared that the EthereumJS EL client has a working implementation of the code change and he is working towards making a client demo for the proposal as well.

**Stokes**
* Hi, everyone. This is. Oh, wow. My computer is not happy. There we go. Sorry about that. Call # 136. And, yeah, there are some things to do first, before we get into, Electra. So let's just hop in. The first one, let's see, is Yoram here the handle or. Yeah, maybe this is where. Hey. Yeah. Hey, if you'd like to, give us an update on your work, that'd be great. 

**Jorge**
* Absolutely. Thank you. is there any chance I can share my screen? 

**Stokes**
* You should be able to. 

**Jorge**
* Oh, I can, I can, yeah, I see the I see the I see it now. Thank you. Sorry. Let me do this differently. Okay. Can everyone see my full screen? 

**Stokes**
* I can yep. 

**Jorge**
* Hello, everyone. It's a great honor for us to be here. my name is Jorge Arce. I am a blockchain and cryptography researcher at NetherMind. And today we're going to be talking about our work allowing validators to provide client information privately. This is a work supported by a grant by the Ethereum Foundation. first, a little bit of background that we're going to be assuming in the interest of time and because I'm sure the agenda is backed. Also looking at the at the audience. we are going to be, sort of like assuming the following, points are familiar.
* If not, I would, if there's anything you would like a quick refresher on regarding the things I'm about to say, we are going to be posting a link in the chat to the full, research deliverable, which goes into more detail into these things.
* We're also going to have a QR code at the end for those watching this in, in the form of a recording or on YouTube. So we will assume you have heard about the current client diversity estimation methods, things like block print, ether nodes and services such as supermajority info, or so we assume you have some familiarity with their current limitations and weaknesses. Also, you might have heard of, Proposal by Dreamer, which I think is also on this call, by the way, to provide the necessary changes to the protocol to allow validators to post their client diversity data on the graffiti field.
* This is a solution that has already been discussed by the community, and sort of like a lightweight approach to getting having us get more client diversity data. And so that one is also part of the background.
* Cool. So in in light of those things, especially if you have heard about them before and you have heard about some of their limitations, it might come as not surprise to you that we're interested in modifying the Ethereum protocol to allow validators to report this data in a way that is, that's a more canonical, more direct, of course, without compromising the the core functionality of the protocol, the performance of the protocol and so on. Moreover, we explored the possibility of making such mechanism anonymous, that is, making it so that the data is shared in a way that, is decoupled from the validator index.
* And if we're able to pull this off, can we maintain accuracy, security, privacy and performance? And how much? So this is what we're looking into today. the results of the of the research. And once again, we'll be having the link to the deliverable in the in the chat will be sharing a QR code at the end for you to read this and more, like more carefully. This is more of if you're interested, this is more of a sneak peek into the main ideas. So for a method one client diversity data on the graffiti field where each block proposer writes an encoding of the L plus n combination on the graffiti field by default. We're not going to discuss a lot about this.
* Here we refer you to the relevant research discussion. We will say that at least for the goals as we define them before. One challenge that this method has is it becomes quite difficult to anonymize such gravity field reports, because they are coupled to the identity of the validator. And it's very hard to work around this using any kind of cryptographic building blocks, because you just have very little, size or very little space in the gravity field to work with. 
* So one of the first things we came to realize is that in order to use any of the, let's say, standard techniques for privacy or anonymity, that would come to mind, you would need a channel where you can, share data that is, allows for sharing for larger data blocks than just the graffiti field. So how could that look like? Let's go into our second method. 
* Calling this share data through the Gossip network. Plus, use Nullifiers for privacy. What we're going to do here, what we're going to propose here is a generalized crawler method of sorts. So instead of using the request response domain of peer to peer, which is how crawlers currently work, they query nodes and they get back information from them. We're looking into flipping that on its head and using Publish-subscribe. we'll see some advantages to this, but how would that work? Like how would that look like? And how do we make sure we're not just breaking the network by proposing something like that? Well, consider the following first iteration.
* Have validators and code their client, or be able to encode their client diversity data into a client data object. right now, for this first iteration, we won't consider privacy. We will add it in the a few slides. From now, we will explain how the privacy comes into the picture and have the protocol periodically and randomly select a sample of validators that will be published in their client data. Much like how the protocol currently chooses a sample of validators periodically for security duties or for attestation aggregator duties, let's have the validators in the sample gossip this client diversity data on a dedicated client diversity topic through gossip sub.
* If they happen to not be subscribed to the topic at the time, they can use the Fanout mechanism to share the the data. And so for the nodes that are subscribed to the client diversity topic, they can gather this reports. They can verify them independently, aggregate them and publish them on their own. Similar to how crawlers work nowadays in the sense that every single crawler can provide, sort of like their own, own dashboard, their own visualization of the results. 
* And anyone else can also play the role of a caller and verify the the accuracy of this information. So the object that we're looking to share, this client data container. So it would have this lot number, the encoded client data. Let's say we're encoding the client data in 32 bytes, similar to the, client data on the graffiti field proposal. We're going to have a signature for the validator in order to see whether it actually belonged to the sample at the time or not, and the validator index. If we do it like this, the container size is roughly 144 bytes, which is about 50% of the current Ethereum attestation. So by itself it's not a terribly large data object that it's being sent.
* But we need to think about how many of those are flying around the network at a given time. And we definitely want to use samples to avoid network overload. We don't want to have the entire validator set be sending these, objects at a time. We want to be working with samples. Now, how large should that sample be? And this is a general observation that applies to, we made in early in the research and hope it would apply to all the methods for assessing client diversity.
* So if you consider, in order to consider the statistical significance behind this, if you use the standard statistical theory for a service like this is essentially where we're running a survey on the on the validators, we find out that with a confidence level of 95%, which is standard to these kinds of applications, the following error rates are going to hold our error margins.
* If you choose a 9.6 K validator sample, then your estimations of client diversity are expected within a 95% confidence level to have up to a 1% error rate. 
* If you multiply that by four, that is, if you run with a 38 K validator sample, then the error rate goes down to 0.5%, which, is not too shabby. Now, if we, let's say, gather one client data object per slot, following in the footsteps of the client diversity on the graffiti field method. Or you could, rearrange it to be 32 per epoch, like, sort of like batch like this to allow the clients or the validators time to prepare the data, send it, so on and so forth. Then you would be reaching these targets for sample size in 1.33 and 5.33 days, respectively. So this might be a bit counterintuitive until you run the numbers, but thankfully the you can get to statistical significance pretty quickly, and you don't need your samples to be huge to do that. further supporting the point that we can do this without, like, imposing unreasonable demands on the peer to peer network.
*  Now let's talk about the privacy behind this all, which we said we were going to leave for later. let's go into how we're going to use Nullifiers for privacy. And as a general observation, if we want to make our data client diversity data private, you can go about it in one of two ways. You could hide the client data itself without touching the identity of the validator in the, let's say client data object. Or you could hide the identity, but keep the the client data itself public. If you do any of these two things, you would be able to break this connection right between identity and the data that is being shared. The thing is to do this, to follow either of those two approaches, you're going to be looking at different cryptographic primitives.
* So if you want to hide the client data, you will require some kind of homomorphic encryption scheme, such as the one used by private voting protocols that are known. Uh. However, using homomorphic encryption requires a trusted decryption authority or trusted decryption committee for that matter. The appeal behind going about it the second way, which is hiding the identity instead of a plain BLS signature that you use to identify the, validator, you can use a zero knowledge proof of the validators identity plus a nullifier to prevent double counting of these client data reports. If you choose the latter, you would have a zero knowledge proof where you're essentially showing that the validator belongs to the sample that was chosen by the protocol, without revealing the identity of the validator itself and the sample can also be kept.
* The sample itself can also be kept private and not just be a list of validators, similar to how happens with attestation aggregators nowadays. This anonymous client data object would be slightly bigger because of the zero knowledge. Proof would be roughly the size of an Ethereum attestation, like 296 bytes if we're assuming a 16 proof. Still, given the number of of these anonymous client data objects that would be flying around the peer to peer network at a time, we think that the, requirements on the network would be, minimal. Now, to disclose a challenge about using this technique, it has similar weaknesses to many to those of many privacy, blockchain privacy, cryptocurrency projects in the sense that if a sufficiently motivated attacker is listening to the peer to peer network and conducting traffic correlation analysis, then they can use these heuristics to get IP addresses for the node and sort of like triangulate and match a validator index to the client data. 
* If you want to address this at the protocol design layer, you require. Further, we would require further research into mixed layer approaches or specialized specialized routing strategies such as dandelion plus plus. We know such initiatives have been undertaken before and have been discussed in research and such. Some have also been adopted by other privacy cryptocurrency projects. But going too deeply into this direction would be out of the scope of the of the current project. This is more of a follow up that would be interested in looking into. Also it. I think it, begs the question of whether we expect these kinds of attacks to happen in the first place for client diversity data. That's a point where we would actually be very interested in hearing what the what the community has to say, like, how much of a concern would that be? For method three.
* Three dedicated voting scheme for client data collection. Let's take the other road in the crossroads. High percentage you guys. A while some slides ago, instead of hiding the identity, let's hide the client data itself and think about this like as a generalization or a stronger alternative to the survey approach. You're going to be leveraging a blockchain to publish votes in a censorship resistant and publicly auditable fashion. You're going to be needing a homomorphic encryption scheme and a committee of decryption trusted encryption authorities for decentralization. And you can choose these building blocks in a variety of ways. An example that could be pretty lightweight and leveraging existing infrastructure and design choices would be, well, we need a blockchain that is low cost in order to be published in these votes. We don't want people to be paying gas for publishing these votes.
* So a proposal would be using a proof of authority blockchain for dissent. 
* Ideally, something already existing like Cholesky testnet could be a good solution here. And as for a committee of decryption authorities that would be in charge of gathering, aggregating and publishing the end result, we're going to need some parties that are, trusted, by the by the community at large or by the, by the protocol. So we could propose, for example, to have the Ethereum client teams themselves, running nodes for these encryption authorities, with the understanding that this design would require collusion of, supermajority of these encryption authorities in order for any data to be privately leaked. Now, here's a rough diagram of the process we're We're still going to be using peer to peer for validators to publish this data, through a dedicated gossip sub topic.
* The reason for that is more direct alternatives, such as like using an RPC channel to send the data to the decryption authorities we think are not acceptable because they could lead to, IP leaking of the validators. So if we have the validators gossip their data through the peer to peer network, as before, the decryption authorities gather these votes and publish them, and do the whole aggregation and encryption or decryption process on a voting smart contract on a low cost blockchain, where here we propose the example of testnet for that. Now, the object that you're going to be dealing with, as it turns out, is going to be a lot heavier than the one we were working with before, because at least on a naive implementation, let's consider that.
* First, you would require a homomorphic encryption ciphertext for each of the different client choices that the validator can make. Each of the different execution client software choices, each of the different consensus clients, the software choices, if you were to do it like that and you imagine you have 20 client choices in total, then the ciphertext would add up to two kilobytes.
* The voting data will add up to 2.4kB. However, we can use compression. We can fit up to three plain client data objects into one ciphertext such that when you add up the the votes, when you do the voting aggregation, you don't run into out of bounds or overflow issues. If you do it like this, then this brings the data needs down. Let's say to roughly the data objects are going to be 1000 bytes one kilobyte. And the smart contract itself will be looking at storing something like ten megabytes of storage. We're running out of time. Unfortunately for our comparative analysis of the solution with regards to privacy, trust, assumptions and adding complexity, I will refer, you guys to the full report where we attempted. 
* Like rank the considerations we have just made in terms of severity or, or in terms of how easy they could be addressed with further work. So, for example, for the dedicated voting protocol, there's no way we can see to remove the trust assumptions. You're always going to be needing a trusted party to take care of the aggregation and decryption, which is why it's highlighted in red. And as a conclusion, we can see a trade off between the highest degree of privacy guarantees in which not even a party that is listening to a peer to peer network can de-anonymize the client data. This is the case of the dedicated voting scheme, but it requires, the trust assumptions on a, on a decryption community. So there's this trade off, sort of like between the highest possible privacy guarantees and the need for trusted parties to come in.
* Okay, so let's wrap it up. here's the. The QR code leading to the research, link, where you guys are more than welcome to post any comments, concerns, observations about what we have discussed working on this project. We have, and in no particular order, we have atom avatar and Ethereum core developer who is here in the in the in the call as well. And Ahmed Ramazan, blockchain and cryptography researcher and yours truly. So that would be it. thank you very much for your time and attention. We are now in my research, not sure if we have time for any questions or comments. If we don't, we can bring it over to ETH research where we will be very happy to continue the discussion. If yes, we're more than welcome to, talk about those. Thank you. 

**Stokes**
* Great. Thank you. do you mind dropping a link to the Eth search post and the zoom chat? 

**Jorge**
* Yes. Oh, I'm very sorry. I thought it was already dropped. 

**Stokes**
* I might have missed it, so. But either way, just a place to continue the conversation. 

**Jorge**
* Absolutely. Let me. Let me do it again. Or maybe Ahmed can. Oh, there you go, Ahmed. 

**Stokes**
* Thank you. That's Yeah. Very interesting research. yeah, there were some questions in the chat. but. Yeah, maybe just looking at the time, we'll move on to the next agenda. Unless there are any comments, right now. 

**Jorge**
* Thank you. We'll look at the chat and we can continue the conversation on ETH research. Thank you everyone. 

**Stokes**
* Sounds great. Thanks. Next up, Peter has an update he would like to give us. I think Peter's on the call. 

**Enrico**
* Yes. Great. Hey. 

**Peter**
* So I don't really want to drag this out. so basically the reason I kind of posted the my proposal and the summary on the chat is that you guys are aware of it. It's something that we've worked on, but, so just to do a very, very tldr. TLDR, we've been on the guest theme. We've been investigating, a possibility of, creating execution layer witnesses and using them to cross validate executions. Basically, what we are trying to figure out is, whether it would be feasible, possible, etc. to have one client run an Ethereum block. Create a witness out of it and then have other clients cross validate the execution. So the idea, my original idea where I started from was this, uh. client diversity issue, not necessarily the client diversity, rather the slashing conditions that way back in, I think end of last year get had a much larger market share. And, there were these these really loud horror stories that if Gath were to do something bad, meaning have a consensus fault,
* Then it could have dire consequences, which are all true. And, back then, what I was thinking about is, how could we solve this issue without necessarily forcing everybody to switch away to some other client? And this isn't, basically my problem isn't necessarily people switching away from Geth rather, this whole client landscape is pretty dynamic. I mean, we have clients. For example, RAF is the hotshot upcoming new client, and, but people have I kind of feel that people have weird incentives of choosing one client over the other client. For example, people might want to run Roth. However, since it's new you, the risk of a consensus fault is higher. 
* So depending on if you're a validator or you want to run it in production, it's like, yeah, are you willing to foot that risk or not? What happens if basically you run an archive node and it just goes off consensus and you act upon bad data, or there are a lot of different scenarios, or if you're a validator and all of a sudden you start attesting and validating bad blocks, etc., whether it's Geth, wrath or whatever other client and basically what I, what the idea was that obviously all such instances require a full node which runs the consensus and runs everything. But what if we were to actually also create a witness while running a block and have other execution clients just stateless validated? Because in theory, our hunch was that it should be very, very cheap. So once one of your nodes runs a block and produces a witness, it should be relatively cheap for to validate it with another client or basically validate it with all the other clients.
* And the document that I posted is basically a summary of, of our basically what, what we arrived at specifically that we've implemented this whole witness creation in Geth, which is fairly optimized. I can tell you a number that it's about a 20% performance hit to block import. So if if you're block imports is about, 100 milliseconds, then aggregate creating the witnesses, maybe another 20 milliseconds extra. So I think that's very, very cheap. and that's kind of the only component that we have optimized heavily because it's something we need elsewhere, too. But we've also implemented, running these witnesses through Geth and basically having stateless, having coding that is stateless to validate the witness. And that code actually runs the exact same code that a live validation runs. 
* So there's no special black magic to, to have witnesses run specially. So basically we can guarantee that it's the same code. And that part is currently basically takes the same amount of time. So running a witness takes maybe again 100, 120 milliseconds. That is not something that we have optimized. the reason why it matters is because it's the witnesses are fairly dumb format. And, so it's, it's it's a lot less optimal than what Jeff has at it's, basically what that can do either way. What we've, what the document kind of details on the L side is how to create these witnesses and, and how and that it is actually feasible to create these witnesses fast and that it is feasible to run these witnesses relatively fast. We haven't optimized it. I'm hoping we can make it even faster. And then the question is that if iOS can create witnesses and LS can stateless to verify witnesses, then what can we do with them?
* And the first thing that came to my mind, and basically that was my starting point, is to allow multiple iOS to cross validate each other or a validator, or for a production node. And the question is then where do we integrate this? And I mean this infrastructure. Where do we take our witness and give it to other clients to cross validate? And there's a lot of possibility for custom infrastructure and pluggability everywhere. But one place that kind of, looked interesting to me is to move these whole witnesses and cross validation into the engine API. The reason I kind of thought about that is because what the engine API currently does is that you have the payload method, which basically gives you a block and it says whether it's correct or not. 
* So we could extend that method to also return a witness, not just the response. And then you have the fork trace update, which asks guests to or L to create a new block in case you're the next validator. So you're the next block producer there. You can easily also add a flag saying that well get me the next block plus its witness. So it kind of naturally fits in creating these witnesses really elegantly fits into how the engine API works currently. And then you would have one more method on the engine API, which kind of would be similar to new payload, but instead of actually integrating that payload locally, it would be like, I don't know, a stateless payload where you just get the payload and the witness run it and we can reply whether it, it is valid or invalid without actually doing any modification. Anyway, the TLDR you have the details written on the both in my doc and on the on the GitHub issue too.
* So I don't really want to go into very much detail, but the idea was that the engine API seemed very, very elegant for two reasons. One of them is that, this way we don't need to invent new infrastructure. So all we have already had, the communication between L and CL is done. Chris Mannix support talking to multiple URLs at the same time. So it would be fairly trivial to to just extend it so that the, the CL sense, uses one execution layer client as the main driver and uses others as, the verification ones. So it's fairly simple. So to do the cross validation logic and the other thing that this kind of allows us to do is a very, very big step towards, stateless Ethereum. 
* Because if we think in a virtual world where you have virtual trees and, some block producer generates, not just the Verkle block, but also the Verkle witness. Then you would have to use again a similar API where the block producer needs to somehow give the witness whether it's empty or Verkle, witness to the claim. The claim is to propagate it in the network. And then on the other side, when the KR gets the block and the Verkle witness, and it would need to deliver it to those down to the L to verify. So the infrastructure proposed for modifying engine, I mean, my proposal for the engine API would be useful. I would say probably 100% as as a stepping stone towards the stateless, Ethereum. So that's why I was, kind of, proposing this change to see how much against you guys are on modifying the engine API.
* My proposal that I, wrote up, added new methods to the engine API, simply because that way we can actually merge this code into Geth, and anyone can play with it without touching the production endpoints so that we don't mess with anybody's code. And then any, any execute any consensus layer client can actually try it out with Geth and see if it makes sense or not. If it makes sense then we can think about a more proper integration. one thing that we did notice is that, the engine API is encoding currently is JSON, and we have huge hex blobs in it, which for the witnesses, the problem is that witnesses are quite large and the JSON encoding and hex encoding is slow. this doesn't necessarily relate only to witnesses. So the same issue happens for blocks too when you transfer the blobs.
* Currently we have one megabyte worth of blobs. If we want to raise the number of blobs available, then that number goes up and eventually the blobs themselves will hit latency issues due to JSON and hex encoding. So one thing that, in my proposal is is not covered, but we should think about is also, and that's independent of my proposal. So whether my proposal is accepted or not, I do think another issue is we should change the, the, the transfer protocol for the engine API from JSON to probably SSZ or anything binary really, I don't care. And that would probably completely eliminate the the encoding latency for for the engine API by the way. So basically that was just a really rough rundown of what we've, worked on. It's actually functional in GAF. That's why I brought it up. Now, the question now is whether there's an appetite to to have it included in one way or another.
* As for the performance numbers, as I said, witness creation is kind of final ish. As in, we probably can't really make it a lot faster, but, propagate. I mean, encoding, decoding the witnesses on the engine API and witness verification will probably. I'm hoping we can make that faster. So when looking at the numbers, do consider them in that respect too. By the way, so that's you will find a lot more data and numbers and everything in my documentation. It's just an overarching overview of this thing. Yeah. So that was a breakdown. I didn't really prepare too much for it, so hope it was kind of understandable. 

**Stokes**
* Yeah. Thanks. it's super cool. And I like how it lays the groundwork for stateless clients. Guillaume, you had your hand up. 

**Guillaume**
* Yeah. I had a question. Because there's been a spec for witnesses in, using the execution payload, like that's been around for two years. I don't see an upgrade path from, this system to to this. And so that was my first question. And the second question is, uh. 

**Peter**
* Wait. So the witness format in this pack is completely opaque. So, I mean, it's just a binary blob of data. So you. 

**Guillaume**
* Understand that you don't. 

**Peter**
* So changing one binary blob of data when running in empty to Verkle blobs when running, when passing the fort fork point. I mean, that should be fine. 

**Guillaume**
* Yeah, but that's not what I was saying. Yes, there's indeed a format type, but there's also the way it's passed. There are some assumptions in Verkle that are, meant that, like the block should be executed, should be received at the exact same time as the as the witness. from what I see, this is this is more of band, and I don't think it can. It's future proof of Verkle is what I'm saying. 

**Peter**
* What is off band? 

**Guillaume**
* Do you have several calls? Right. So no, you could. Well, you define three calls. 

**Peter**
* Well, yes. One of them is when you produce a block, then you get the block and the witness together back or you when you. Currently in empty world. Yes. so the block production logic would be exactly the same for empty or Verkle is the same thing. Just give me a block and you get the block back and the witness so that that's covered on the other side in Verkle. You can if you want. I mean I define this I know execute status something something. If you have a stateless client then that is what you would use. And you that's that's all. And that stays the same thing. Whether you verify empty stateless you verify Verkle stateless.
* That's still the same thing. I give you the block and the witness, and you run it. Done. The third is just the new, new payload with witness. Which which is the the way.
* Well, if you have a full node where you want your own node to verify, to create a witness that you can cross validate with other client, that might be something that won't be needed for Verkle. That's the cross validation thing that we can use today. But we can't. We would just get you would just delete that. 

**Guillaume**
* But what if so. From what I understand you're not forced to produce that witness during production block production. You could use the old the old call instead of, like producing a block with a witness. 

**Peter**
* Yet the idea is that if you want to cross validation currently, then you would make a witness. If you don't want to do that, you won't make a witness because it's pointless to dump that on your node. So it just gives you an option. Maybe in Verkle if you always have to. Do you always need a witness, then in Verkle you would just say that well you will always make a witness. 

**Peter**
* So I don't think this is the methods. I think the methods will mostly stay the same thing. I don't really see them changing at all. Just maybe before Verkle it makes sense to call one method and after Verkle call that method just loses its point. But otherwise it's the same thing. 

**Guillaume**
* Yeah. Okay. I guess I have to dig a bit a bit deeper, but, yeah, in any case, it will it will require a lot of changes compared to the actual implementation of Verkle, but. Okay. Thanks. 

**Peter**
* I guess all in all, Here, the question is, whether there's anybody seeing anything super obviously wrong with trying to get it through the engine API and the way the engine API proposed methods look like. Definitely we can go with a starting point where the methods are separate the way I suggested, just so that we can merge it in and we can iterate on it.
* And then if it turns out to be valuable, we can figure out a tighter integration. If not, then not. As for the performance issues raised and the sizes, those are valid that we need to look into how we can optimize them. I think it should. Yes, we need to do, we need to see what the worst case would be and how expensive that would be. Yes. It's definitely something that needs, a bit of work, both in Geth itself to make the missing pieces fast and but still, the engine API should be, should be turned into a binary one. That's. I would say that's mandatory long term, whether this thing gets in or not. 

**Stokes**
* Mikhail you had your hand up. 

**Mikhail**
* It's just a quick comment on how the engine API spec could be handled. We used to have an experimental, folder in the spec, and, usually we just, if we need to extend if it is supposed to be an extension of, say, new payload method, then just yeah, the spec can be created in these experimental folder. And, the version of this method could be some arbitrarily high number. so not clash with the ongoing work on the, current hard fork. 
* And this probably if it's used better. So you can just by leveraging this approach, just, extend the existing methods and experimentally implement those in different clients. And after this, scoped for any hard fork, we can move this back to the hard fork stack. So that's one of the ways to handle this on the stack level. But yeah we can iterate on this in the PR the client has created. 

**Peter**
* So just to add a quick memo, none of this requires a hard fork. So basically adding, at least the way I designed it with, a couple of new methods. Those methods can be added to else whenever, and they can be used by Eth class whenever, and there's no synchronicity requirement across them. 

**Mikhail**
* Yeah I see yeah. Let's just discuss it. 

**Lukasz**
* My main concern is prioritization because Prague, we already made it very big. And there is a vehicle coming, that would kind of make this party obsolete. So the part that, were definitely worth investing is the, logic of supporting, working with multiple clients in this way. And the other part is definitely working on removing JSON from, as a, layer of transportation on any API, right, to move to something faster. But other than that, I kind of have a concern that until this is implemented in enough clients and like, have good enough tooling for people to actually run it.
* And there's also concern of increased latency that, would it be acceptable on average machine, which is not obvious. but then we will be already shipping Prague and focusing on Verkle, which should be our priority, in my opinion, bigger priority because it comes like, this this setup can be cheaper on Verkle because you don't need a leading client. You can do cross verification in parallel, which basically you avoid the additional latency. You still have to wait for the slowest client, but at least it's not, serialized, waiting on to clients.
* So that's my question. Is it important or urgent enough to focus on it as beyond parts of it? This is a stopgap solution that will be obsolete.
* And we know we will be it will be obsolete. So that's the question. 

**Peter**
* So with the obsoleteness, I kind of both agree and disagree. so the reason I kind of try to spec it to fit into the engine API was specifically to make it as make as little part of it as possible obsolete. So basically updating the engine API to binary will be needed anyway. The updates to the engine API to be able to pass witnesses back and forth will be needed anyway. clients supporting, running, stateless execution and gathering witnesses will be needed anyway. The only thing that, that would be different is what the content of those witnesses are. But you still need to be able to gather  nodes, whether they are virtual entities or not.
* Doesn't matter. And the other thing is, you still need to be able to execute a block based on a soup of trinodes, whether Verkle or empty, it doesn't matter. So I'm not so sure that there's a relevant amount of data that's going to get thrown out or work. It's. 

**Guillaume**
* Sorry, the super of tri node part. do you assume the same format of MPT? like the same storage format for MPT and verbal because we had this conversation. 

**Peter**
* No, no it doesn't. No, I'm basically what I'm saying is that basically you just have a partial subset of the tri. So in MPT you will an empty witness will contain, I don't know, 1000 tri nodes. in no particular order, because empty doesn't require it for Verkle. If Verkle does require it, then you would have it in some specific structured format, but it's still just a bunch of try nodes that the witness contains. So it's you still need to while executing the block, you still need to gather that and put it into the witness. So I don't really see that much difference. 

**Ahmad**
* Yeah. so I have like two points here. I want to say that, first, in this approach that Peter suggesting, you provide a false sense of security to the network, because like, in the case that a DDoS attack is done on a majority client, then, the liveness of the network is still affected, in a severe way. of course, my assumption was that we introduced multiple clients just to guarantee the liveness of the network. 
* So this basically goes against the whole principle of multi-client network because it just deletes it. Whereas a solution like utilizing a multiplexer, something similar to vouch or something like that would, actually guarantee that liveness, even without stateless execution. And if this is aimed for, smaller operators or solo operators, then in the chat we already, like kind of, device that the latency from this will render this, very not profitable for the solo staker, whereas large operators can easily utilize something like a multiplexer to run multiple clients concurrently, without, enduring the latency issues.
* So another thing is that when Verkle is coming up, like Lukasz said, I don't see why, we would invest time into something like this at the current stage. 

**Peter**
* So thanks for those. to answer, to try to answer them. So one of them was the DDOS. So the DOS is, relevant, but, in my opinion, Ethereum network being DDOS and losing, liveness is the smaller of the problems. consensus faults are much bigger problems. That's where the nasty stuff happens. So the fact that Ethereum doesn't finalize for half an hour or an hour is a lot less of an issue than, basically having two chains. So, for sure, if,  it does affect a bit, anyway.
* Period. so that was the DDOS issue. the latency issue, as I kind of mentioned, the problem is that basically the engine API is basically most of the latency currently in this whole cross validation is the engine API encoding. 
* So passing the witness back and forth to Geth will consume 200 milliseconds of latency just to pass the thing. Basically, it passing the witness through the engine API back and forth takes more time than running the block twice. So it's like, as long as that's not fixed, it's kind of unfair to say that the latency is too high because this is not the fault. This is not the reason why the latency is high, the engine API is the reason. And the with regard to, small versus large validators. 
* Yes. I kind of agree that if you are a large operator, then you are expected to run arbitrarily many nodes. But, if you are a smaller operator, I think being able to run one node and whatever that is your preference and cross validated with the other kind of lets people to let people choose nodes that they like. 
* For example, I can easily run a Rest archive node and know that even though it's a bit problematic because it hasn't been battle tested, if there's Netermind node cross validating it, you have much higher guarantees. Whereas if, I'm at home staker, maybe I will just be too afraid to run a rest node because, yeah, it. What happens if it goes bad? 

**Guillaume**
* Yeah. That's, I mean, I'm changing topics a bit, but not completely. in case the engine API doesn't, like this proposal does not get accepted to go through the engine API. Is there a backup solution to propagate the witnesses? somehow, like, let's say only only Geth wants to do it. Would you do you have a backup plan to propagate those witnesses? 

**Peter**
* Not that I would prefer. So basically, the this whole thing just if other ELs decide that they want don't want to do it, then I mean Geth playing by itself doesn't really make much sense. However, being able to run with stateless and generate witnesses does have a lot of potential use elsewhere too. So it's I mean, it's not really thrown out work. as for creating another channel, outside of the engine API. I that one kind of really feels like wasted effort. So I probably wouldn't do that. 

**Lukasz**
* So my suggestion would be let's start with changing engine api to binary format and see when we deliver it, see where it's Verkle if it just around the corner or further away. And I think just doing that will take us quite a long time. So that's the problem for me. 

**Peter**
* I mean, I completely agree that we can definitely focus on that, on that part. I don't know, honestly, converting the engine API to SSZ seems like somebody has to go in and define basically just annotate the those five data structures with the SSZ magic numbers that are needed there, the max sizes and whatnot. But after that's done, is there a lot of extra work? I don't know, I'm just questioning it. Basically, I'm just saying that I don't think that if there is a legitimate effort to make it happen, I don't think it should be that complicated. Trademark. 

**Etan**
* Last time that SSZ like something simple there was proposed to align the withdrawal routes in Capella. there was like more the problem that people wanted to go farther than that. So with SSZ, the problem is that, if we are changing the engine API to SSZ, don't we just also want to transform the block headers to SSZ so that we can just send them natively, like do we want this intermediate step? I guess on engine it's less of a problem because it doesn't go on chain. But yeah, that's one of the aspects that you can choose how far you want to go there. 

**Peter**
* No, don't open that can of worms. Basically keep everything as is currently. Just replace the the JSON with SSZ. Anything else basically that's how that's why the previous effort to get SSZ into EL got shot down because basically just blew up into less SSZ this and that and that and that. And then it just became a monstrous, monstrous effort. So my 2cents would be just replace the JSON itself and the binary encodings themselves with SSZ and leave the the way the headers and everything are formatted, the way they are currently changing the headers to SSZ, that's kind of a consensus change that that gets complicated. 

**Ahmad**
* One suggestion is to go gradually with something like Messagepack because, actually the Json-rpc 2.0 spec actually supports Messagepack, and Messagepack actually sends all bytes, as raw without, hex or base64 encoding that adds overhead. So, I don't know if there is any reason why not to go with something like Messagepack, which is, already has libraries to cover all programming languages. 

**Peter**
* I just don't see the reason why that's a good idea. it's probably a bit simpler than SSE, but long term, I mean, we want EL to speak SSZ says long term. If we want to switch, if we want to move more air consensus types to SSZ, we need to leak SSZ somehow into URLs. And this seems like, doing the engine API seems like a very trivial thing because it's it's a very simple just a few things. And then that's, that's a nice gateway to have your start speaking it. Whereas if we go with Messagepack,
* I mean, you still need to add Messagepack and all the encodings and whatnot to ELs, so SSZ or Messagepack doesn't really lower the effort, but it doesn't get you further. It doesn't get you further to, having consensus SSZ stuff. 

**Stokes**
* Cool. Thanks for that, Peter. is there a place people should go to continue their conversation? I see you linked to just from the GitHub comment. 

**Peter**
* So I would probably, I in that, GitHub comment, there's the proposal, and I would probably go there as a starting point. Or if somebody wants to do a more live discussion, then we can maybe do discuss one aspect or the other on discord or wherever. So probably to just do a brain dump of ideas I would dump it belonged, below the proposal just so that it's kind of there and to go back and forth and wherever you guys prefer. 

**Stokes**
* Okay. Yeah. Discord sounds like a good place for that. Great. Thank you. Okay, so next up, we will turn to Electra. And the main thing here is Devnet one. I believe it's targeting alpha three of the specs which has been cut. And yeah, I guess I'll just open it up. Is there anything anyone would like to discuss with respect to Devnet one, I think people mainly are heads down implementing the spec. is there anything anyone would like to discuss in particular? Otherwise, we'll move to a few other updates for future dev nets. Okay. Perry has a comment that they're waiting on L readiness.
* So great. I assume that means everything's progressing smoothly. Okay. Mikhail had a PR. I believe this was to follow up from some changes to IP 6110, following the work at interop. Mikhail, do you want to give a few words about this? 

**Mikhail**
* Yeah. Thanks, Alex. Yeah. So this is the follow up to the breakout session we had during the interwar. and yeah, this PR basically. implements the logic we discussed there. and yeah, just just go quickly through the mechanics. So the if one bridge deposits remain the same, so they are processed instantly. And if there is new order, it created instantly. and yeah, the balance is queue skewed to be processed later and to be passed through the activation churn. on the opposite, the deposit requests, which are new deposit, which a new way to actually deliver deposits to the consensus layer, they are, added to the pending deposit skew. they are not processed anyhow. And then these this skew is being processed on the processing. this actually done for the main reason was to rate limit, the deposit processing during the um epoch.
* So we can put a limit, which this PR does. There is the max band and deposit script processing. and if number of deposits exceed this, limit, it just, you know, breaks awards and yeah, the rest will be processed. during the other epoch transition, it also ensures, the logic implemented in this PR ensures that it won't breach deposits will be processed before deposit requests. So, no, no withdrawal credentials from Tron attack as possible. So there is a strict order of, well, new layers, that are created. and yeah, it also waits for deposit requests position to be finalized in the queue. As we discussed, this would be easy to implement if we already have a queue. And yeah, to prevent some complexity and potential bugs around managing the Pubkey cache, in the implementations. **Mikhail**
* So what else? Yeah, it refactors do the refactor, of the process spend and deposits, method because it gets more complicated. and what it, this, this refactor actually adds, one computational inefficiency. the look up of a validator index in the validator set is happening twice for each deposit. this is done for, spec readability to improve the spec readability. But yeah, if if it is going to be a concern, we can do something about it and do it once and, yeah, do some work around. But I just thought that probably, all clients will use the cash, to do this lookup, so it will be really cheap. also, the other thing to probably think about is whether we need max lending deposits per epoch processing to be even to, to even exist because we have a natural limitation which is the churn limit. yeah. And there is the potential worst case scenario attack that is described in this, in the description to PR.
* So just if you want to take a look, please take a look at it. And yeah, probably it would be great to not just introduce another, constraint. and leverage on the churn limit. yeah, that's basically it about, the, the logic that this PR introduces, and, it would be great to, to get as much feedback, till the next week, probably because, I'd like to start working on tests. and. Yeah, if anyone wants to help with the writing, test, this, functionality, this new stuff. So. Yeah. Please. Welcome. Yeah, that's basically it. 

**Stokes**
* Okay. we'll move on to the next agenda item, then. thank you for that, Nicole. So. Right. yeah. If anything, we will timebox this. But I was going to ask if anyone wanted to review the blob based spike that I believe happened last week. I think it led to some turbulence, with roll ups. And kind of touched many layers of the stack. I'm not sure if there's anything we want to discuss now. If not, we'll handle that in other places. Okay. Sounds like. No. In that case, let's move to Piraeus. So, I guess first off, I don't know if anyone here was, on the breakout. I'm not sure if there are any updates from that call that are worth sharing with the group here. Okay, awesome. Does the network look healthy? 

**Mikhail**
* Sort of. 

**Barnabas**
* We had some blob spamming. and some nodes were unable to, produce blocks. All the blocks that they produce were orphaned. So I think they're already taking a look. 

**Stokes**
* Okay, great. There was a comment to look at essentially these two PRs. Let's see. Let me grab the link. So essentially this was to uncouple how we communicate the global mid between the EL and CL. There is a PR that I opened that would basically have the CL drive the max bob count for example over the engine API. I think one open item there was to consider, including the max bob count and the EL header to facilitate optimistic sync. I haven't added that to that PR yet or added it anywhere else, but that was an open item that I think we kind of agreed we needed. Another thing was, this PR 3813 to the consensus specs repo. I don't know if Dankard on the call. I don't see him. but essentially this was going to go even a step further and take the essentially the the base fee calculation, away from the EL and have it handled all in the CL.
* I think this encapsulates things quite nicely. yeah. So I guess for now I'll just call those two out. I think ultimately I want to do something like this for Pectra. So yeah, please take a look if you haven't. And. Yeah, just consider this a a call for review. Mikhail. 

**Mikhail**
* I think that, for both parties, whatever we do, on the CL side, in terms of that effects the EL block validation. we will have to include this into the EL block because, as you've said, because of the optimistic sync, because it's not always the case where every where a payload is sent by the CL payload. So, yeah  we'll need to be self-contained in terms of validating the block. and the other thing is that, we have this target parameter as well. And, if we don't want to make this target parameter a product of max, like, say target is, half of a max. then we would need to include it as well into the block header. And if it is the case then probably it is better to. Yeah. In my opinion, it would be better to have a couple of parameters, like in the Dankard PR, having these base fee computed by the CL and validated by the CL,
* And the basically blow up, gas limit. one one potential problem here is that EL will not be able to compute the, the base fee for blog gas. And if this is required by EL, like, for, you know, to filter out transactions in the mempool, then it could be a problem, but you could use this parameter from from the block, from the parent block of the block. It is, yeah. From basic the block. It has the head. So probably it's not that bad. It's not a problem. Yeah. That's just. my my thoughts on those two years. 

**Gajinder**
* Yeah. My opinion is, that solution one is, more simple in terms of, it is keeping, you know, it's keeping safe maintaining separation of concerns in the sense that CL is only telling what the blob limit is and the pricing is calculated by EL, and now in future we can have, for example, a contract like 7702 which to which transactions can be sent and that can itself decide what the pricing is. So there are many ways you can, enhance this, further, using EL rather than having these calculations being done at EL and for rather than these calculations being done in CL and also updating the formula in EL is not really difficult. and the only thing, only thing that, that is relevant is that, okay, target will have to assume is half the maximum blob limit.
* But I actually don't see that you know how fancy we are going to go with respect to target and the max limit. And most probably, you know, things are good to be kept simple and straightforward. 

**Stokes**
* Yeah, I tend to agree. I think I will wait until Democrats here and he can maybe motivate his PR a bit more. but yeah, I do. I definitely see this, like, violation of separation of concerns across the layers, which I don't like. I do think his thinking was essentially that, there's like at the fork boundary, say, if we change the blog count, there's like this weird discontinuity in the base of calculation and like the CL then would have more context to be able to like, you know, compute the fee change smoothly. So I think that was one important point there. But yeah, that all being said, this will be an ongoing point of development. So yeah, please take a look and we will revisit in the future. Let's see anything else on pier Dos. Otherwise, we'll move to an SOC update. Okay. Ethan, I think this is you. Would you like to give us an update on Sion's work? 

**Etan**
* Sure. so there are still these two EIPs. One is on the consensus side to update all the SSZ container definitions that frequently change, such as beacon state, beacon block body, and these to a format where the generalized indices no longer change for a for any given field across future forks. just for context, this is used by smart contracts that rely on EIP for 4788 and beacon data. Right now they need a redeployment whenever a index g-index changes, and with the EIP it's no longer necessary. And we have full implementations from Lodestar, Nimbus and Teku that have a definite running in Kurtosis, Lighthouse and Prism are still implementing it, but there is no no real opposition at this time to give it a try for inclusion into Electra. So I would just like to, ask one more time if there is any opposition still against EIP 7688 in picture Devnet2. 

**Stokes**
* Well, I think right off the bat at least I can say picture is quite big. So we need to very seriously consider making it even bigger. but yeah. Enrico. 

**Enrico**
* Yeah. Just one. Tech readiness. so we took a short path to be able to be compatible with the dev net, just essentially be compatible with profile definition, but being fully compatible with the entire new SSZ spec of the stable container turned out to be a bit more complex. Still working on it on full compatibility. And yeah, just say that one thing is being compatible with the Devnet, for switching to profiles. And another thing is to have a full, implementation of the SSZ library fully compatible with the specs. 

**Etan**
* Sure. Yeah. I mean, for this EIP, like the stable gene, datasets for the beacon state struck for the consensus structures, only profile support is necessary. So, like what you did for the Devnet? I'm talking about including this scope only this scope into the Devnet two. 

**Enrico**
* But include all including only that it will be in any way a little tricky for us because the implementation is still undergoing and we normally go with the master branch with Devnet. So I'm it will force me to, merge to master an incomplete implementation which is still working on. So my preference at least will be to complete the implementation and then then have have everything ready for full support. 

**Etan**
* What is the timeline on Devnet to like? we are still ahead of them at one. So for Devnet one, it's definitely too early. Right. So 2 or 3, would it like, could it be a good target? 

**Enrico**
* Yeah, that's a good point. I don't have an idea, but yeah. So maybe devnet two could be good. Devnet 3 will be safer. 

**Stokes**
* Okay. In in any case I think people are mainly focused on Devnet one Devnet two will probably be some time off. so yeah, again, this is a nice update. it sounds like we can make a call on a future ACDC

**Etan**
* Okay, yeah. And, for the SSZ transactions, like, that's the flip. Ethereum JS has a prototype now, and we are working on making a client demo as well. that consumes that data so that it verifies, for example, transaction inclusion proofs. so that if you have a wallet and it shows you a transaction history, that you know, that it's accurate. that one I posted into the Light Clients channel on discord, it's still early access. 

**Stokes**
* Okay, thanks. Okay, cool. I think that was everything on the agenda for today. Is there anything else that we would like to discuss? Otherwise we'll go ahead and wrap up. Okay, cool. Thanks everyone. let's go ahead and call it. 

**Ahmad**
* Thanks. Bye. Thank you. 

__

### Attendees
* Terence
* Tim
* Trent
* Pooja
* Barnabas
* Terence
* Pari
* Ethdreamer
* Mikhail Kalini
* Mike Kim
* Zahary
* Pawan
* Chris Hager
* Gajinder
* Andrew
* Mario
* Shana
* Carlbeek
* Roberto
* Sammy
* Protolambda
* Saulius
* Marek
* James
* Dankrad
* Kevaundray
* Radek
* Fabio

____

### Next meeting
Thursday 2024/7/11 at 14:00 UTC



