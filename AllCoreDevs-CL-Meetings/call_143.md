# Consensus Layer Call 143

### Meeting Date/Time:  Thursday 2024/10/3 at 14:00 UTC
### Meeting Duration: 1 hour
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1158) 
### [Audio/Video of the meeting](https://youtu.be/dplciLdQTM0) 
### Moderator: Stokes
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
143.1  |**Pectra Devnet 3 Updates** EF Developers Operations Engineer Parithosh Jayanthi said debugging efforts on Pectra Devnet 3 are still underway. Network participation rates on Pectra Devnet 3 have fallen, according to Stokes. Jayanthi said that this is due to a bug in the Besu client that the Besu team is working to fix. He added that there is also an issue with Lighthouse/Nethermind nodes that he is currently investigating.
143.2  |**Pectra Devnet 4 Readiness** Stokes shared a post by the EF DevOps team about the list of open pull requests (PRs) pending for Pectra Devnet 4. One of the main outstanding PRs for the upcoming devnet launch is about the execution requests structure. As discussed on ACDE #197, developers are pursuing a new strategy to simplify the communication of execution layer (EL) triggerable requests such as EL triggerable validator consolidations, withdrawals, and deposits. Geth developer Felix Lange shared that there are open questions related to the formatting of the requests. Developers debated on whether to send a custom hash of the requests over the Engine API or the full request objects. “Potuz” from the Prysm team was in favor of the former for efficiency reasons. He wrote in the Zoom chat, “Not agreeing on a simple hashing system is really a failure of communication, choosing a manifestly less efficient algorithm over just picking essentially any other option seems childish to me.” Other developers on the call such as “Arnetheduck” from the Nimbus team disagreed. Without a clear consensus on the matter, Stokes recommended continuing the discussion on Discord over the next few days and coming to a resolution on it by next week’s ACD call.
143.3  |**Pectra Devnet 4 Readiness** Stokes noted that CL specifications for Devnet 4 will likely be based on the “alpha.7” release, which is in the process of being finalized by his team. Stokes also highlighted that PR 3918 in the consensus specs repository has undergone review and will be merged shortly. Additionally, PR 3818 is ready for review. (This is a PR that creates a queue for the processing of validator deposit requests.) Stokes encouraged developers on the call to review the changes.
143.4  |**Pectra Devnet 4 Readiness** Then, developers moved on to discussing two PRs related to how CL clients handle validator attestations. Arnetheduck who is championing both noted that one has more benefit for implementing in the immediate hard fork, Pectra, while the other can wait for implementation in a separate upgrade. Stokes agreed that developers could then drop PR 3787 and focus their attention on PR 3900. He recommended “soft” including PR 3900 to Pectra Devnet 5 to give client teams more time to review the PR and work on its implementation over the next few weeks.
143.5  |**PeerDAS Devnet Updates** EF DevOps Engineer Barnabas Busa said the latest PeerDAS devnet is struggling to reach finalization. Developers may have to relaunch the devnet with fixed client implementations. Busa said there is “lots of debugging” work happening on the PeerDAS devnet and developers will have a breakout meeting on Tuesday to discuss bug fixes.
143.6  |**“engine_getBlobsV1” Implementation Updates** There is a new execution API method called “engine_getBlobsV1”. It is designed to assist validators operating with low bandwidth to propose blocks in a timely manner. Representatives from Prysm, Lodestar, and Teku said they are in the process of implementing the method and Stokes stressed that this should be a “top priority” for client teams. The benefits from this change will be analyzed by developers in the coming weeks to better assess whether a blob target increase in Pectra can safely be added without the risk of negatively impacting network decentralization.
143.7  |**“engine_getBlobsV1” Implementation Updates** Developers discussed outstanding questions related to the method, one of which was raised by Teku developer Enrico del Fante. He created PR 3864 which suggests various clarifications in the P2P spec in the event of specific edge cases. Stokes encouraged developers to continue discussing these clarifications and others related to engine_getBlobsV1 outside of the call.
143.8  |**Blob Throughput Increase Discussion** Stokes asked developers about their views on the strategy to scale blob throughput discussed on last week’s ACD call. Developers had agreed to gather more data about block reorg rates and home staking activity before moving forward with the inclusion of a blob target increase in Pectra. EF Researcher Toni Wahrstätter said that he has done more empirical analysis since then on block reorg rates for validators building blocks locally versus validators that rely on a third-party block builder. Developers discussed how best to go about doing an empirical analysis of node syncing capabilities in the event the network cannot reach finality. Potuz highlighted fundamental differences between re-syncing nodes to the head of the chain on devnets versus public testnets, saying that the former does not inform the behavior of nodes on the latter due to differences in P2P architecture.
143.9  |**Blob Throughput Increase Discussion** EF Researcher Ansgar Dietrichs suggested including a blob target increase in Pectra now and if further analysis shows that this is not safe for the network, removing it later so that developers do not have to scramble to include this code change last minute. Potuz pushed back on this suggestion, saying that in his view removing a change to the blob target increase is just as much work as including. Jayanthi chimed in to say that a blob target increase is not a simple change for many client teams to implement, especially if developers are also thinking of coupling the increase with EIP 7742, uncoupling blob count between CL and EL. Stokes said, “My read is most people, or if not everyone, is in favor of 7742, so I think that's going to happen.
143.10  |**Pectra Testnet for Devcon** Devcon, an annual Ethereum developer conference, Jayanthi said that his team would like to launch a dedicated Pectra testnet that attendees of the conference can build on and test their integrations with new code changes like EIP 7702. Jayanthi asked client teams to create a duplicate release for this testnet that is a stable version of what will be released for Pectra Devnet 4. Stokes was skeptical about whether Devnet 4 would be stable by Devcon, which will start on November 12.

**Stokes**
* Okay. We should be live. Cool. Hi, everyone. This is consensus layer. Call 143. There's the agenda here. And the chat. It is issue 1158 on the PM repo. And yeah, we have a number of things to talk about today.  both with Electra and then also, scaling the box. So let's go ahead and get started. So first up, I think it'd be helpful just to touch on Devnet 3. I think the last time we checked in it was going pretty well. But in the meantime, I think there have been a few bugs pop up. And, the last time I looked for participation wasn't, super good. Are there any updates on Devnet three? Anyone would like to give? 

**Parithosh**
* Yeah. So I think the best teams identified what the issue is, and they're currently working on a fixed image. Daniel mentioned that it should be ready by tomorrow so we can deploy the fix tomorrow. He's on the call. I guess he'll expand on that. 

**Daniel**
* Yeah, in the end. Just what Paris said. So,  we had a bug where we did not warm up the two address at the beginning of a transaction for, 772 accounts. So accounts with delegated code.  this led to a wrong gas calculation on our side.  so this this issue, I've created a PR. I need to add,  a bit more of tests, but yeah, as I said, by tomorrow we should be ready. 

**Stokes**
* Okay, cool. And that was the only outstanding thing on the devnet three that we were tracking. 

**Parithosh**
* Yeah, there was one lighthouse, Nethermind node that had an issue. I think right now we've basically chalked it down to a hardware issue on the VM we got on the cloud provider.  so we've started rsync and I have to look at, I have to check up if it's fine now. But besides that, I don't think we found anything specific. 

**Stokes**
* Okay, cool. Okay. that sounds like we're good devnet three. Then we'll wrap up those items and hopefully things restore to normal. Then we can move on to Devnet four. So yeah, there's a number of things here. I think the first thing to kick us off, I'll just call out this document from Panda Ops. 

# Good summary of outstanding work here: https://notes.ethereum.org/@ethpandaops/pectra-devnet-4#Open-PRs [2:51](https://youtu.be/dplciLdQTM0?t=171)
* The net four specs. There's a section here on open PRS. I think this is the best spot just to see what remains before we can get to net four on this side. I think the main thing is that it says here listed Alpha six for the specs release. I think it will end up being alpha seven, but if someone feels differently, let's discuss.  there are a number of PRs since Alpha six that again I think will go into alpha seven. And yeah, from here it'd be nice to sync on some of them. So I think the biggest thing at this point is this execution request structure and how we're handling them.
* So it'd be good to resolve that.  I think there was some work on discord around how to handle this. From what I saw, there were like a number of issues around,  yeah, a number of different things. Would anyone here be able to give us an update on that?  I do think there is a Resolution to get to at least a design that we like, so it'd be good to agree on that particular design. 

**Felix**
* I mean, I can't give the update. So basically the the open issues that popped up were that,  well, we the main thing is that some of the CLs decided that it's a bad idea to like having to compute the request hash on the CL side, and they want to leave this to the EL.  and a response to that, we are changing the engine API,  to pass the request instead of the request hash calculated by the CL, so the EL will calculate it. We have also changed the commitment to resolve like the request commitment and L we have changed it to resolve a potential hash collision. And,  the commitment is very simple.
* So even if the seals don't have to compute it, it is absolutely possible for them to compute it because it's just sha256 of some bytes which they have. So it's not like anything complicated. There's no RLP, there is no NPT in that commitment. So that should be okay if they want to compute it, but they don't have to with the spec changes. And then finally there was some we are still kind of debating if we should make the system contracts behave one way or the other, but it's irrelevant for the CLS. And I think this is basically the result.  today, from prism has raised,  some concerns regarding the ordering of requests, but these are in fact already resolved in the latest specification,  at least the one that we are targeting right now. So I think we are basically done with the design right now.
* It's just all very messy because. The specs are still being updated and the whole thing is just a bit like. In the air right now because of the last minute changes that everyone wanted. 
* But it's basically good now from my perspective. 

**Stokes**
* Okay. Thanks, Felix.  the one thing with the contracts, like we did have an RFP. For an audit. And so, like, I think we should resolve that as soon as possible.  was there one direction you were leaning? Because I know there's an issue with. Like the Typekit either being emitted from the contract or is it handled somewhere else? 

**Felix**
* Yeah. I mean, the changes to the contract are very small.  it's not like a big change to. The contracts at all to, to put this bite and,  we don't have to put it either. And I think the officially, we are just soliciting proposals right now and the proposals will be in by mid or end October. And then the work on the audit will actually start. I don't think people will really seriously start to audit before they have been selected as an auditor. So I think we. 

**Felix**
* A couple of days left to add these OP codes or potentially I have personally have some plans to make some refactorings in the in the contract, but just to try it out if it's like a better approach. But it's not. Again, it doesn't really affect the state of things like the functionality of the contracts at this point is kind of locked in. We just have to make the final call, and it doesn't change the output from the EL at all. This is just internal stuff, basically. 

**Stokes**
* Right.  Potuz us do you have something to say? 

**Potuz**
* Yeah. Just, the abstract problem on this API changes. And by the way, yes, as Felix said, I mean, we were already implementing, and I was reviewing a PR for Prism without knowing that there was a commit of today changing completely how the commit was. So so this is this is what drove that discussion.  so after this latest changes of today, it seems that the CL is receiving the requests in the same ordering, the canonical ordering that the beacon block has them and the CL can return no the CL and the EL will be speaking the same ordering, which is what was bugging me. And the only thing that I would, try to come up with an agreement, which I don't really understand why we are disagreeing on, is on the way of sending a hash.
* I think it shouldn't be a problem for us to compute a hash in whatever mechanisms, helps the EL if it's only like hashing Sha 256 bytes that we already have. and we already have the ordering, and it doesn't require to include new encoding like RLP. I don't see why we wouldn't do this. I mean, over the JSON. 

**Felix**
* No, the main difference is that instead of the like on the on the on the CL side in the CL block, we are using the hash tree route to create the commitment for the requests. While on the EL side we compute the request hash, which is not quite the hash tree route, but it's kind of similar to the hash route. It doesn't I mean, there could an argument could be made for just using hashtag route on the EL. And this is what Matt has also alluded to at one point, but I think is not necessary because there is no need to create proofs about requests, because the requests are just an output that follows exactly the transactions in the block.
* So basically, the request hash on the EL side is just a checksum of the activity that happened within the block, which is fully triggered by the transactions. So it's just this the the value of this commitment for the EL is very low because it's literally just an identifier for like something happened or nothing happened. 

**Potuz**
* I sort of understand, but so the thing is the, the current status I think is the worst of both words because we're sending data over the hot path, which is block validation. We're sending data over JSON over hot path, which is block validation. And I would want to just send 32 bytes instead of this. Of course, for us a hash tree route would be trivial because it's already implemented for us and it would mean work for the EL, but if it takes us to like computing a Sha 256 of bytes that we have already. Ah, yeah, I would be willing to do that work to save the sending the full request. I think we should. I mean, I'm in agreement with this. 
* This, but sending the full data I think is the worst possible outcome of this. Yeah. 

**Felix**
* I mean, this is where where this is something that has to be resolved between the CLS. So the there were some people who were who did not like the fact that they would have to compute two different hashes, even though the hashes are pretty trivial, but they still wouldn't want to compute like two different commitments. On the CLS side, hashes are microseconds. 

**Potuz**
* Sending bytes over JSON is milliseconds. I think this is just a no brainer that we don't want to increase the JSON side. 

**Felix**
* I don't know. It's I'm fine with either. It doesn't change the implementation all that much. If we receive the request, we compute it over the request. If we receive the hash, we just put the hash. It doesn't matter to us in the end. Like how it's sent. This is either way totally works. And it's a very cheap operation. If you feel very strongly about sending the hash and, well, it has to be computed on the CL side. It's a trivial thing to compute honestly. It's just you take the SSZ lists of the requests that are in the beacon block, and you have to write them one by one,  into the Sha 256 and collect the upcoming hashes, and then basically hash the concatenation of these hashes again. So it's like a two level tree kind of thing. it's very trivial and all the bytes exist.
* So it's not like it doesn't require any encoding. I don't know, I can look into the hash tree route as well, but I think the hash route will be more complex. It will be more operations. Maybe it's fine to make a definition for the ELs. I don't know if this is really, really something that you guys must have. Then I will look into it and figure out how to specify it in a way that doesn't require introducing like. We don't want to introduce SSZ in the EL with this change. We are basically walking a very fine line here between like dealing with SSZ, but also not dealing with SSZ too much because it doesn't appear to be time yet to change it. It's not for this fork to introduce SSZ into the EL. 

**Potuz**
* And I think, I think just of each list and just of that would be trivial for us to implement. It would be three hashes. This is I presume collision resistant. And that's it. Yeah, it's actually four hashes. I'm sorry. And four hashes is much better than sending this over JSON. 

**Felix**
* Just let let's okay. This part of the spec is really not that complicated. I think the main stuff we have is It's just like the design is pretty much locked in right now. It's just that with this thing, maybe we can give it another two days or something to resolve it in chat, because I don't think we will resolve it today. Or can we maybe quickly get a show of hands from the other class? What they think about this issue I'm seeing in the chat? Some people writing just send the stuff in JSON. It's fast. Also, like not everyone seems to believe it's a problem to send the full requests in new payload. 

**Stokes**
* Yeah, the concern for me is just having like yet another. It's more conceptual where it's like you have to then think about a new way to compute the commitment. And granted, in this case it is very small. So if this is the best thing we can do, then let's do that.  but yeah, I think it'd be nice to avoid like, yeah, another bespoke commitment scheme. Mikhail. 

**Mikhil**
* I just wanted to add that I think it's nice. Separation of concerns. The concerns, the data and the outcome. The commitment. This was already mentioned. I also want to add that if for some reason we decide that this is not optimal for I mean, like data transmission takes too much time, we can switch from in the next version of new payload, we can switch from the entire data to the commitment. I would not just do the preliminary optimization here. 

**Stokes**
* Okay. I mean, to Felix's point, it seems like from the CLs so far, they're leaning towards flat request, meaning just sending the data over with no hashing on the call other than maybe prism. How do other CL clients feel about this? Or it's fine if you haven't had time to take a look, but an update would be nice. Okay. I'll assume that means no one's had time to look.  okay. Yeah. Thanks for the input, everyone. Oh. Go ahead. 

**Mikhil**
* One last bit. the parts that are to the consensus spec and to the engine API, they are now updated with sending the entire data. And also, there was previously this byte prepend in each list the type byte. It's now dropped as well. So there is no type byte. And the type should be derived from the index of each request each byte sequence. So if it's zero then the type is zero and so forth. 

**Stokes**
* Okay, Thanks.  okay. I wanted to make a decision on this today. I sounds like we won't. We'll resolve every question, which is okay. I think we should try really, really, really hard to have this completely settled by next week's call. So, yeah. What's the right place to continue the discussion? There was like a very long thread on the R&D discord. Is that the right place? Felix or Mikhail? You guys were. Yeah. Okay.  I think it was the JSON rpc api channel, if I'm not mistaken. so. Yeah, please weigh in there. Otherwise some decision will be made and. Yeah,  you know, maybe just for, like, broader context, like, I think at this point we should aim to have, like, texture specs frozen by devcon. That's like a month.  if we can do it sooner, that's great. But yeah, I think at this point we should be very focused on on that goal.
* I can message you after eth dreamer about about it.  okay. So that was, I think, the biggest thing. There's also a number of, like, downstream things to how we answer this question. So yeah, it is quite important to resolve as soon as possible otherwise. Okay. So there were a few other things for Petra. So in particular, there was this one I think it's actually let me just double check the number here. Right. So 3918. This was an update to how we handle requests for validators to switch to compounding. And we're going to leverage the, execution layer consolidation request sort of mechanism for that. I put a link to the PR here. I think it's in a pretty good place.  I think we're in a place to merge it later today, but, yeah, if there's any final feedback or comments, now would be the time. 
* Okay. I'll assume that, so yeah, I'll take a final look after, but I think we can merge that one today, which would be nice.  great. Yeah, Michael's just saying everything's been addressed, and. Yeah, I took a look the other day. I think we're in a good place with that one. Downstream of that. There were then some implications for. I think this is for three. Oh, no, that was something else. Sorry. Let me grab the number. It was 3818. let me grab this link here. And again this was handling  how request how deposit requests are queued now, particularly in the beacon state. There were some performance issues there.
* So this is like, really important to resolve. I say it's downstream of 3918 because, some of this is touching on like consolidations and deposits and their interplay and all of this.  yeah. I guess I'd have a question for Mikael. Do you feel like, this is moving along pretty well? And do you agree with my assessment that, yeah. I mean, my redesign needs a few updates after 3819. Sorry. 3918. 

**Mikhil**
* Yeah, it's I mean, like the updates on the client side, right? 

**Stokes**
* Okay. I guess then is the ready to review or. No. 

**Mikhil**
* PR is ready to review. there are a couple of things from recently.  many kind of inputs. Couple of inputs in the PR.  I would say that they are not significant. So I will review them and apply some suggestions. Yeah, it's ready to be reviewed. It's ready to be merged, after these recent things are addressed. 

**Stokes**
* Okay. Thanks. 

**Mikhil**
* And yeah, and I think that we need this to, to get merged sooner because it entails engineering work on consensus layer, client side. One place for a developer. 

**Stokes**
* Right? Yeah, definitely. I mean, we did a test here and it caused issues with like a high deposit count. So this should be the PR that resolves that. And yeah, I would agree. It's definitely uh very important for Petra. So okay, maybe we'll leave that there for now then. And Let me just see if there are anything else. We covered the request thing. Okay. Anything else anyone sees on? Like,  at least for Devnet. For Petra. Otherwise, we'll move to a few other PRS that might go into Petra, but I think need more broad discussion. Okay, so then I think the really only remaining things up for discussion for Petra would be these two PRS on the specs repo. There's 3900 and 3787. So these are both touching the attestation format of various parts of the stack.
* Let me just grab links here in case that's helpful for anyone.  but yeah, this is, I think, kind of the biggest open question for Pectra at this point. So it'd be good to go ahead and make a decision today.  ultimately, yeah. So these are refinements of how we're handling the attestations following the attestation. EIP and Petra already, I think it was I always get this number wrong, but I think it's 7549.  in any case. Yeah. I guess we'll start again with another temperature check.  maybe on the doc. I think you're kind of pushing for these if you want to, make a case for them. 

**Arnetheduck**
* I can just summarize some of the discussion. So,  I think there are three options. Basically, we can delay everything till the next hard fork.  there exists something which I would call, like a complete conversion. This includes,  Changing the symbol at the single attestation format. The attestation format and possibly any downstream APIs.  personally, I'm not that afraid of this option because it's kind of a limited option. It's kind of a well known option.  but the feedback has been that this would cause a lot of engineering effort in, in many clients. so the third option that I, that I think is maybe the most reasonable to pursue right now is to, is to go for a limited implementation that addresses specifically only,  the security advantage on the gossip channel of the single attestation and then leave other changes for the next hard fork. because of two things.
* First of all, the difference that the full set of changes brings can kind of be implemented in code. They don't really depend on the spec that much. Like if you want two types for, you know, unchanged attestations and network aggregates, then that's perfectly fine to code your client this way. And then in the future, if we decide to do the full thing in the spec as well, all that really changes is a constant, which is the size of the list.  so, if we focus only on single attestation, the benefit that it brings is this idea that we can check the signature, before computing a shuffling and based on experience from past outages, both on mainnet and on testnet, every time we run into a case where a shuffling has to be computed, we've kind of seen instability. 
* And my suggestion is thus that anybody that or the way that we would introduce these changes to really keep it tight and focused on the gossip channel, so that if clients want to implement it in such a way that they just translate to attestation and then change nothing else, that would be an entirely minimal change also to client code bases like it should be at least. For Nimbus, we're fine with both option. I think it would be sad to delay the single attestation change to a hard fork in the future, because this is this is like a thing just waiting to happen. And when it happens, we'll we would regret it. 

**Stokes**
* Yeah. Thanks. Yeah. Thanks for the update.  right. So what I think that would mean then is going ahead and closing 3787 for now and then focus on. Yeah, like you said, just these like networking level concerns of 3900. So yeah I think there's been some other input across different client teams. how do we feel about this approach.  I'm not sure if there's a refinement of the 3900 PR to make it clear to like just scope it to the the gossip layer. Maybe just like a note on the PR would be helpful.  but yeah, like I hear the security argument,  around again this DOS vector. And I think that one has a lot of weight. So I lean towards doing that for Pectra. But I would love to hear other clients input. yeah. If you had your hand up first. So. 

**Mark**
* Yeah. So lighthouse's opinion. We've had, time working on this, and, I mean, he said that we could have a spec compliant,  version pretty quickly, at least, like on the networking level, but we wouldn't necessarily have all the changes propagated through the client. And I guess we could push that to a later time.  and I guess it just depends on timing. If we're trying to ship Pectra as fast as possible, then he would like, slightly lean towards. No,  but,  I feel like if I feel personally like if that I agree.  with with that I think it's worth doing even, if we can have a spec compliant version and propagate the changes later. But to get it, to get the fork done and deal with the gossip or deal with the DOS attack, I would feel it's worth doing. 

**Stokes**
* Yeah, that makes sense. Enrico? 

**Enrico**
* Yeah.  so we were discussing about this for a long time, and,  internally we are. We're still, leaving the door open for the single attestation, super minimal, implementation. And I haven't had the time to complete my first spike over, over the simple approach. We think that it should be a minimal, even if not super clean. Might be ugly, but we could have something that is, good to go in relatively quickly, but with, we'd like to confirm that later. 

**Stokes**
* Okay, parents. 

**Terence**
* If it's minimum like now, I wonder if we even should have the validator changes because I was originally the proponent of that. It just naturally feels right to have the validator set up the single attestation. But that of course is more embedded. That of course, is more invasive in a way. So I guess the question to everyone here is that, would it be better if today we take out the validator set changes? I am personally in favor of it, but I'm also open to not having that as well. But but I guess one way or another, I think the security thing is quite important. And I am personally supportive of this change. 

**Stokes**
* Right. So how do you see it perhaps even just in prison if we have the validator guide changes, does that imply you need to touch your validator clients and all of those APIs? Or can you just still limit it to gossip? 

**Terence**
* If there is a validator change, then yes, validator client will change and then the API will also have to support that. Right. 

**Stokes**
* Okay. Arnetheduck. 

**Arnetheduck**
* Like this is more of a point of order, but in theory, we can keep that change and still keep the API because the two formats are interchangeable in the sense that the full attestation is a superset of the simple and the single attestation. So we could actually get away with not changing the, you know, BN and VC communication protocol, even if the spec reasons in terms of, you know, single attestation it to me that mainly sends a signal, Whether we want to pursue the full change in the future as well. And and in that case, I would leave the language as it is. If like, let's say that today we decide that we do 3787 for the next hard fork as well. We aim towards it at least. Then,  when we introduce those changes, we could also discuss changing the beacon API.
* But again, like,  I'm happy to change the beacon API today as well. Or, you know, for the next Devnet or whatever. To me, that is a kind of a separate discussion. Like we can we can decide on these two things separately in the spirit of not ballooning this change beyond where it absolutely has to go to solve the security issue. 

**Stokes**
* Right. So yeah, I mean, I think that makes sense in theory. And then my question would be, yeah, how to handle this in practice because there's not going to be some like extra spec communication that people will need to be aware of. I'm open to ideas on how to handle that. 

**Arnetheduck**
* I mean. One way, like I'm happy to propose, like, make a PR for the beacon API as well. And then we can concretely see what it will entail if we today agree on on shipping simple attestation on the gossip network.  I think that's also an important step for clients to see like how much, change it, like how much work it would be to,  Expand that change to the beacon API as well.  and I'm happy to make that PR to the beacon API as well, so that we can see how much it changes the language of the beacon API so that we can decide that, you know, in two weeks or four weeks or whatever it will be for a future. somebody says some this is already on, on the beacon API spec. Great. I haven't been following there. To me, like, I really think about this change from the point of view of the network and to me, single attestation and the proposed,  aggregate attestations.
* Those are envelopes. And just like, you know, aggregates on the gossip channel today, they have an envelope already, which is called I don't remember what it's called. It's called something weird, which is why I don't remember it. But this is all like just for the purpose of simplifying communication between clients on the P2P layer. And we shouldn't, you know. Force that into context where it doesn't belong. 

**Stokes**
* Righh, Enrico?

**Enrico**
* Just a comment on the PR of the about the API changes. So that specific PR, I think is not just something that is impacting the communication between VC and VN, because it's also considering changing the event of the event stream, which I think could have some other downstream effect outside VC and VN. I might be wrong here, but I just raising the flag that if we go down that path, maybe someone else could say, hey, you're changing something else here. 

**Stokes**
* Right? I mean, there's at least tooling and stuff that would use those channels, so it would break them if there's a breaking change.  yeah. Arnetheduck

**Arnetheduck**
* Personal opinion would be to not change the event API, actually, because imposing this change on, you know,  third parties that just observe,  the event stream, I think that's completely unnecessary. I feel there is a week or a small argument for updating the beacon API. It's not as strong as updating the gossip channel, but,  the thing is that, you know, when you have a list, you have to compute that list and you have to verify that it's correct that it only contains one element, that the element is in the right spot, and so on.  so if we change the beacon API to speak this same language when signing attestations back and forth?  I think we'll just end up with a simpler API that has fewer, ways to fail. So it's just one less thing to check for. So and in the bcv and communication and because,  the bcv, the BN VC communication is something limited to, you know, client implementers and not passive observers or tooling.
* I feel that that's kind of different than changing the event stream. 

**Stokes**
* Okay.  so to move forward,  it sounds like we think 3900 is like in a good enough state.  if that's not the case, we should discuss that now, but okay, so we have that one,  I guess. Yeah. on the Arnetheduck, if you want to review this for 72 PR on the beacon API, just to make sure it aligns with what you're thinking, that'd be helpful. And then what I would suggest to move forward here is that we sort of, you know, soft include, 3900 for Devnet five, not Devnet four. That gives people a bit more time to implement. Just the very, like, strictly scoped gossip, you know, layer implementation. And so we'll have a little more time to understand, like if that's actually like a pretty, you know, well scoped change that given the security considerations, pulls its weight.  then yeah, we have like another ACDC cycle to, to think about, you know, formally putting it into Devnet five.
* Does that sound like a good path forward for everyone?
* We have a plus one and a thumbs up.
* Does everyone feel like they understand what they need to do here with respect to their client implementation? Because I think that's like my biggest concern at the moment is just like, there's not like a super direct way, I think, to make it super clear just from the spec what we're talking about. Okay. There's general agreement on this. So let's, move ahead with that. And also, yeah, just to be clear, it sounds like we're going to,  ignore three, seven, eight, seven for Petra, which should get us to spec freeze sooner, which is very good. Cool. So, okay. I think that was everything on Pectra. 

# PeerDAS / Blob scaling [39:45](https://youtu.be/dplciLdQTM0?t=2385)
**Stokes**
* Is there anything else anyone would like to discuss? Otherwise we can move to,  talking about some blobs. Okay, great. So for the blobs,  I keep asking and the situation doesn't change too much. But I will ask one more time. are there any updates for the PeerDAS? 

**Barnabas**
* We are still working on it. 

**Stokes**
* Yeah. Okay. Thanks, I think, yeah, people have been working on it, and. Yeah, it's just moving along as fast as I can. 

**Barnabas**
* Yeah. So basically, we launched the Devnet and, we have been on finalized for well over a week at this point and today it's been turning for the worse, and we're considering to do a relaunch with exactly the same spec. We had a bunch of different client fixes for, different bugs. We we have a lot of debugging going on, and we had a good call, just on Tuesday in the breakout room. So I think we are on track. 

**Stokes**
* Cool. Thanks for the update. Okay. another relevant, really exciting thing is that we did finally merge this engine, get Bob's v1 PR. So what this does is essentially lets the CL query their local mempool for blobs, and it unlocks a lot of cool use cases. In particular,  very likely supporting blob propagation. You can imagine if I am a proposer and I don't have the best uplink.  I can essentially leverage my peers mempools to do the availability check for me. So really cool to see this merged. And yeah, I think immediately I'm just curious about implementation status. Are there any CLS who have not implemented this yet? 

**Terence**
* We are implementing it, but we have not completed yet. I see there is a Geth open PR, so I'm looking forward to testing that. 

**Enrico**
* For Teku who we we merged yesterday and it will be part of the next release going out soon. 

**Stokes**
* Cool. So yeah, I mean I wanted to bring it up because I think it's especially in light of last week's conversation. I think it's like a really critical thing to, at least make it easier for all network participants to handle the blobs as soon as possible. So yeah, I would consider this a top priority to get merged into your clients. My understanding is that there's kind of a couple phases of this. Like the first one is just implementing it and being able to like, read. And then separately, there might be another phase for the right path. Or like when you go to propose,  maybe it's a bit early then to like discuss all of that, but I guess just something to get on your radar. I believe this is something we can do even without a hard fork. Right? So, you know, if we get this together, even in, like, the next few months, there might already start to be impacts on reorgs. And, you know,  all sorts of things like that. So, yeah, consider this, super exciting and very important to implement ASAP.
*  There was a related suspects PR. I don't know if we want to discuss this now. I think the main open question, I was going to have something about this or this other PR. 

**Ansgar**
* I'm not 100% familiar with the other. I more like to the. General topic, I just wanted to briefly remark that it's not super urgent, but once this is rolled out, I think we should at least look into the possibility of explicitly prioritizing and broadcasting the block over the blobs, because,  for now, what we will still do both for the local builder itself, but then also the individual nodes as they receive blob the block and the blobs that they will rebroadcast, those kind of with equal priority. And so they all kind of compete for upload bandwidth, which, especially for the local builder often is the crucial bottleneck in terms of timing. And given that basically with the Mempool, we expect that in most cases, basically all the blobs will actually already be known across the network. And really, the block itself is the only kind of crucial missing piece of information.
*  And so I personally think that there is at least a good case to be made to, to explore whether we might want to put a small delay on the blob broadcasting so that, like the block itself, usually is basically already fully submitted by the time we start clogging up the upload bandwidth with blobs. 

**Stokes**
* Yeah. Thanks. Yeah. And this is what I meant a second ago. And I said, like the second phase to this.  I my understanding at least, is that that's directly the intention.  because again, that directly helps again, say solar stickers or, you know, nodes that are under-resourced relative to others on the network. So again, I think that's super important to to figure out as soon as possible. And related to that, there was this, again, related PR this is 3864 on the specs repo. And  right. I think the question here is essentially like it's almost like a may or must around node behavior if you. Let's see. Let me just double check. Actually, I don't know. Enrico, you opened this. Yeah, I can I. 

**Enrico**
* I can summarize very quickly. So essentially is the PR saying that in the on the spec we are saying there is a new way of getting the blobs. And if the client wants to leverage that new way of getting data, what should do essentially there are two things that that PR, focus on is one is the mast around the publishing, the reconstructed blob sidecar based on the blobs received by from the L, which seems like something that has been discussed over, several, several channels and we all agreed on. And so this is saying that if you rebuild the blob sidecar, You have to publish over the over the P2P gossip.  this is one thing. The other thing is more an annoyance over the interaction between these publish and the gossip rules. We were arguing that the client should take care of updating the equivocating caches, while when we do that to close the door of eventually additional blob sidecar coming over the P2P. That was essentially equivocating.
* The blob that you reconstructed and sent over the network.
* So it was kind of,  making sense to us to say, client, just make sure that you update those so you don't have, you close the door over these additional blobs. 

**Stokes**
* Yeah. Thanks.  The gender in the chat says that it should be a may rather than a must. Any other clients have a take on this? 

**Enrico**
* Well, to really help the network, I think you you really should do that.  so. 

**Stokes**
* Yeah, as anything, it should be required to be broadcast. Okay. I'll. Okay. I mean, timing. Oh, sorry. 

**Mikhil**
* There is no actual way to enforce the mask, but, yeah, I mean, language wise, may or must, it doesn't really matter because most of the clients will do that. 

**Enrico**
* But you cannot even enforce the, the the,  the dissemination of the of the things that you receive. I mean, it's not enforceable. You're just participating as a good actor into the into the network like is a must that you should disseminate messages that you that you receive. The same way you should publish this at the same at the same level of of of criticalness to to me. 

**Stokes**
* Right. I mean, the spec here is for like the honest behavior. So if we think it's better for this to be honest, which I think it is, then that's how we handle this.  but yeah, maybe zooming out just a bit,  I think this is something we should resolve soon, but I think there's a little less time pressure.  especially given implementations are in progress.  yeah. So anything else for this PR we should discuss right now? I think that was some helpful Feedback otherwise. Yeah. There are a few more things on the agenda. Okay.  yeah. I kind of just wanted to leave some space to discuss, again, you know, our strategy for raising the blobs. my understanding from the call last week was essentially that we have, you know, the core chips there, a batch of, say, like 3 or 4 EIPs that we were considering,  to include to address the blob count and how we implement that. So, yeah, I mean, there's a lot of discussion, I think, around, you know, solar stickers and, you know, nodes on the network and what we should really be supporting.  one option.
* Well, yeah. So I think there were like kind of two immediate things we could do to like start to address the concern again of these under-resourced resource nodes. One of them is this engine. Get Bob's v1, which is why, again, it's really exciting to see that moving along. Another one would be essentially having a way for a node to specify when they go to build a block, essentially like a node local block Max. And I either didn't see or I missed a conversation of this route last week, so I wanted to leave some room for that now. 
* I think there was some conversation in other channels, and it seems like people were kind of divided.  yeah. I don't know if there's any anything to update there. My sense, I think, was people generally kind of prefer this get Bob's route and then kind of see what that buys us in terms of headroom before thinking about other options. Okay. Ansgar has an interesting proposal. custom and priority fee, which could kind of start to get at the same thing. Everyone is very quiet on this topic. I guess everyone said their piece. Other places. Mm. Okay. Yeah. I mean, I think ultimately there's, you know, we're going to need more data to actually make decisions here. And we haven't really quite had time for that. So yeah, that's fine. And in that case that was everything on the agenda today. final call for anything else we would like to discuss. sure. Perry is asking what data we would need.  

**Potuz**
* Yeah. So on that. I do have an opinion. so I think if we still need to check if it's true and if Tony's data, that points to less reorg since then, Dencun starting with client optimizations. I think that would point to Stakers being able to handle the maximum block on regular sync. on regular gossiping. if that data, if we discriminate that data for home stakers and that data is still true and, and reorgs have not increased a lot. Although Tony posted something, that doesn't make this clear, then I think, tip I mean, syncing at the tip in gossip is not a problem. And we should be thinking on what would increase with a target increase without a maximum increase. So we already have data that proves that Stakers can handle the maximum. And if we increase the target. What will change? Effectively, change will be a transactions in the mempool. We will have more problems on the mempool at gossip, but we will also have much more time for syncing. And I think what this affects is the speed at which a node can sync in. When there is a period of known finality.
* I think this is a crucial measure that we want. We want to have a client after two weeks of no finalization, and check if it can actually catch up to head or not. I don't even know if this holds today, and it seems that it's hard to check to test this short of, like, making a not finalize. 

**Stokes**
* Right. So this isn't even really a node or like a client issue. This is more just like a particular node in their bandwidth. Right. That's what you're concerned about. 

**Potuz**
* What what I'm concerned about is if we. If is. This is the fact that there's going to be actually more blobs in each blob that we have and more blobs in the mempool floating around, more transactions with blobs in the mempool floating around. And if we are in a period of non finalization while we're syncing, a node that is trying to catch up while it's syncing is not going to fast forward to the next finalized checkpoint. It's going to request all blocks with all blobs from their peers, and it's going to execute them all. So this, I think, is the critical thing that will effectively change with a target increase. And I think we need to measure this. We need to measure whether or not we can handle this situation today. If we have some slack into handling this situation today, that would allow us to increase the target. 

**Stokes**
* Right? I mean, it seems like a target one. 

**Parithosh**
* I don't want to make one point that I also brought up in the blob metrics chat. If mainnet was had stopped finalizing two weeks ago, we would also by now have had a lot more forks. So I don't think this version of like seeing the client and it syncs to head even would exist. You would probably have a most users would just check point sync to the fork that we socially agree on is essentially the canonical. 

**Potuz**
* I don't think that's true. So on Devnet, you've seen this because clients are like experimenting with new software, but on Testnets, we've shown that if we stop finalizing because, say like a percentage of the nodes go offline, we are very good in our fortress is quite stable and we won't fork. But at any in any case, like the fork situation, it has to be strictly worse than the non fort one. So I'm I'd be happy if we at least get the data of what happens in the non fork one, and we just need to sync. I believe that our clients are like stable enough that if 33% of the network goes offline. We are not going to start working, which is simply not going to gather enough attestations to finalize, which is what did happen in Gorley. 

**Parithosh**
* Yeah, that's fair. I guess. So then the question is there any situation where we can even connect this data? I mean I guess we can coordinate non finality on but that won't be that trivial or easy I guess. 

**Stokes**
* So I know for. 

**Potuz**
* For Besu it's very hard to simulate this. It would be nice if other clients have analyzed if they could simulate a non finalization on their own clients without uh without making the actual network non finalizing. But we've tried on prism and it seems that it's incredibly invasive to change this. 

**Arnetheduck**
* I can only speak to the effects of what happens like even if the network mostly follows one fork. What tends to happen is that, more and more forks kind of appear, because, you know, somebody halfway through thinking creates a block.  and these forks, they're actually legitimate from, you know, a fortress point of view. and then the number of them kind of just keeps growing. If you're online and if you're not online, then obviously you just see the one main kind of, event. But, I know in Nimbus, we don't really have a good rule for when to call the number of forks, because there kind of exists. None. The best we have is kind of. Yeah, let's just, you know, put at least recently used cap on the number of forks that we track and that's it. And that's maybe the best thing we can do in this case of long known finality. But but it's kind of not entirely satisfactory. And we haven't really tried this, you know, since what was it that last and we tried to revive it didn't go very well. 

**Potuz**
* Yeah. This this was actually my concern that Gorley we actively tried to save it and we couldn't, clients could not sync the head. So it's not really clear to me that we are in a situation today that we're robust enough to sync. And increasing the target would make it would certainly make it harder. 

**Stokes**
* And maybe this is obvious, but we can't just have like an ephemeral devnet that we spin up because we want more realistic Networking parameters. 

**Potuz**
* Yeah. Devnet would suck for this. I think that the idea, the ideal situation would be if we could fork a client to do exactly what it would do if it wasn't finalizing, but then keep the network finalizing. If we have a solution to that, if some if this is not so hard to do for other CL clients, that would be the best scenario, I think. 

**Stokes**
* Why can't we have a devnet and just take, say, a third of the validators offline? 

**Potuz**
* Yeah, but then you don't really get the data of what it takes. I mean, we've we have done those experiments and we do finalize back on small devnet nets. We have done those experiments of attacking the network on devnet. But whenever this happened on an actual running test net, we couldn't get back to to syncing. So I think that the P2P side of like test nets is much is is It's very different than the P2P side of devnet's topology apparently affects a lot. Yeah. 

**Stokes**
* Arnetheduck

**Arnetheduck**
* I think I can articulate one thing, which is, when it would become a no brainer to increase it, which is actually that we have kind of in-flight a lot of, attempts to lower bandwidth and as we deploy them, so, for example, this is get blobs thing,  we kind of should see a decrease in general in bandwidth usage. And if we consider what we're using today, kind of an informal ceiling or informal minimum requirement of what you need to run an Ethereum node. And if we decrease from there, that is obviously room to increase blood counts. Um. In the future. So that's kind of like a way to, to to to say at least like where, where we're definitely happy to, to increase the block counts. And then of course, there exists the grey area in between where we might just do it and, hope for the best. I don't know. That depends on other concerns. More. Yeah. Non-technical concerns. 

**Stokes**
* Okay. There's a little discussion in the chat.  yeah. Any other points anyone would like to bring up for today? The answer? 

**Ansgar**
* Yeah, maybe just one last question I would have on the blob front.  it looks to me really that like, maybe we're all leaning towards kind of making this decision basically as late as reasonably possible within the kind of the fork cycle,  to get as much real world data as possible. Also on these kind of new paths that are being deployed and everything.  I do wonder, though, at what point would it make sense to try to already have a log throughput increase part of the devnet so that it would be ready to go? It seems to me like easier to revert back to not having that and removing it back out, than to basically add it rushed very late devnet process. So I'm wondering whether people might be willing to consider having like an optimistic addition to the deep nets for for blob blob throughput increase. 

**Potuz**
* I think this this changes are symmetrical. So it's just changing a couple of constants. So it's exactly as hard to add and to subtract. So I'm not involved in devnets. But I would personally avoid making a change that I might need to revert it, especially if it's the same change. But having said so, we really need to like commit to shipping these changes as soon as possible. Like have a release immediately. As soon as the get blobs V1 get gets merged. I can say that my personal note I enabled Quic and it made a huge difference already on my own bandwidth. So there are some changes that are already being shipped that that are in the in the released clients as optional, that are already. Change the bandwidth consumption. So if we sort of like start advertising our users to use those changes and we commit to shipping everything immediately, I think in two weeks, three weeks time, we might have already some data. 

**Stokes**
* Perry, you had your hand. 

**Parithosh**
* Yeah.  just to mention one thing, I don't think it is as simple a change. It's not a constant change for a lot of clients. They include the blob count at compile time, so they have to first figure out how to change how they consume the library, which is a bit of work they have to put in in the future as well. The question is, if they put it now or later. And then the second question is if we want to include 7742 and if we do, that means engine API changes and all of the stuff that that implies as well. So I do think it's important to make the decision earlier rather than later, because it isn't just a constant change that has to happen. 

**Stokes**
* Yeah. From my understanding, if people want to accelerate this for Pectra, it sounds like 7742 implementation would be the thing to target.  Let's see. Well, there's a 7623 question, but, you know, assuming we'd be okay without that, then like the most minimal thing would be 7742. And then any IP to raise the target or even consider raising the max.  so yeah, if you are keen to push bobs along 7742 think is is the place to focus for now. POTUS. 

**Potuz**
* Apologies. 

**Stokes**
* All good. I mean, I guess one question that hopefully is easy to answer. Would it be helpful to have an EIP that does actually propose bumping the target, say, to four or something like that.  because that is something where like we do talk about the set of EIPs that we would possibly put into Pectra. there isn't an EIP for an actual target increase, and that is something we'd want. Yeah. It is. 

**Barnabas**
* I think we should make a decision whether we want to actually increase the blob width 7742, or if we're going to just play around with some constant and change the constant everywhere. And if we do decide to change it with 7742, then and we're actually considering an update, of the, blob count in Pectra, then we need to include 7742 in Pectra. 

**Stokes**
* Yeah. I mean, my read is most people, or if not everyone is in favor of 7742. So I think that's going to happen. Yeah, Gajendra was asking. There was a. I believe Perry had an EIP there. There have been a couple floating around.  but. Yeah, if someone wants to, like, polish one and, start entering into the discourse, I think that could be helpful. Although it is more of a minor point. Okay, great. that is a target increase already. Yeah. I forget exactly what this EIP does.  but, yeah. Anything else? Otherwise, I think people are pretty heads down on devnet 4. And, uh. Yeah, we will keep pushing things along. Okay then. Thanks, everyone. I oh, one last thing. 

**Parithosh**
* One more thing I did want to mention. We do want to do a named testnet for Devcon.  it would be nice if clients could maybe plan a release with a release flag for the name testnet. We'll basically be reusing whatever we use for Devnet 4. So it. Does that sound okay for clients?  if not, then we can also work around it and just have custom flags. But yeah, I think having a named release would make it really easy for people to interact with it at Devcon. 

**Stokes**
* Well, Devnet 4 Be Ready by Devcon. 

**Stokes**
* I would also hope so, but I feel like there are still a number of spec things that are kind of in flight.  yeah. I mean, perhaps we can just aim for that. 

**Parithosh**
* Yeah, the the main idea is that there's a couple of EIP like seven, 7742. That would make sense for people who are at hackathons to test out. And this could be the place that they could easily test it out. 

**Stokes**
* Yeah. No, I mean, I think it makes a lot of sense. I guess my question was just if we want to look for 3 or 4 in terms of specs, Devnet four would be great.

**Barnabas**
* Yeah. Because the the contracts will change between devnet 3 and 4. So ideally we want to target Devnet four. 

**Lightclient**
* I mean, we still have five weeks. That's a long time. We could have Devnet five by then. 

**Stokes**
* Okay then. Yeah, let's plan on devnet for for a devcon testnet.  there's been no opposition, so I would say it's a thumbs up to Perry's question. Okay. Anything else? Going once. 
* Yes. Everyone keep focusing on devnet. For, as Barnabas said in the chat. Okay, cool. Then, yeah. I'll see you all around. Thank you. 

**Mikhil**
* Bye. Bye, everyone. 


---- 


### Attendees
* Stokes
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

  
### Next meeting Thursday 2024/10/17 at 14:00 UTC
