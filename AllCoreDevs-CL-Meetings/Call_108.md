# Consensus Layer Meeting 108 
### Meeting Date/Time: Thursday 2023/5/4 at 14:00 UTC
### Meeting Duration:  40 mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/771) 
### [Audio/Video of the meeting](youtube.com/watch?v=RZnf3K1i3NM)
### Moderator:  Danny Ryan 
### Notes: darkfire_rain 
# Contents  
## 3. Deneb
## 4. Research, spec, etc
## 5.  Open discussion/closing remarks
### Next Meeting Date/Time: Thursday 2023/5/18 at 14:00 UTC

-----------------------------------------------

## 3. Deneb 
Danny: 
Okay, we should be live. This is Consensus Layer call AC DC 108, issue 771 on the PM repo. We're starting at number 3. Deneb, then some general spec discussions and then some time for any other discussion points people have. Let's see. so last call, both in the execution layer call and the Consensus Layer call. We're kind of like trying to shuffle towards a final feature set for Deneb. Seems like we're getting close on this end. So a couple of updates and a couple of discussion points. Alex is not on the call today, but 4788 is CFI’d on the execution layer. There's a lot CFI, so it's not 100% clear exactly what's going to make It into the final list. But I think we will be moving forward with the 4788 building into the Deneb fork given that signal. So we'll have testing and other things like that. It is on the consensus layer on the minor range, but we'll work on getting that built into the fork and released relatively soon. Let's see, if we had a summary. Let me scan real quick to see if there's any relevant stuff. Okay? So there's a little bit of discussion on the execution layer, how that actually shows up, but he also comments that it's pretty straightforward. Any questions or comments on that or on the process or how things are moving forward here? 
## Not allow slashed validator to become a proposer consensus-specs#3175
Great. Okay. The other item that two weeks ago there was general consensus on this call. This is not a cross layer feature to get into Deneb is that validators cannot be proposers, which is a minor change to the proposer shuffling function. We were able to greatly reduce the diff with a slightly different place on where this was being called. That is in that PR 3175. Mikhail did open up a corresponding EIP that's still like in a pretty early draft status, but it now has a number 6987. Mikhail, do you have any other comments on this one?
Mikhail Kalinin: 

Yeah, the PR. I think that we should settle this down into the features in directory to make it a proper change to the CL. Mentioned this in the EIP as well and as you mentioned the footprint, the diff of the changes has been reduced, which is great suggestion on the way to do it. Testing is also kind of ready, so it's just about more shaping the spec in the best way. Now what's left to my observation.
 
Danny:
Sounds good both on this and 4788 will keep things moving such that it gets into the Deneb full fork build and tests soon. Any questions on these two items?
## Update MAX_BLOBS_PER_BLOCK to a higher bound consensus-specs#3338
 Okay, great. There's an open PR that's had some active discussion. This is 3338 on the consensus specs repo. Essentially techniques for potentially allowing additional slack in the Blob constants on the consensus layer such that you don't have to do a cross layer fork when updating the gas limit on the execution layer. Does anybody want to give an update on the status of this conversation? It's been a lot of back and forth.
Gajinder:
Yeah, I can give a little bit of update.
Danny:
Great.
Gajinder: 
So the original proposal was that we keep max Blobs per block a little higher on the execution API so that EL clients can basically increase their data gas independently and henceforth increase the throughput of the Blobs. So, Basically over the conversation it was discussed that putting it to a much higher bound like 1024 was not a good idea. So maybe 16 Blobs, **16 Blobs per block** was okay, so even over there we have some discussion going on. But one other thing that has come out on it is that we should have another variable like max commitments per block, which basically and keep it to a high level like 1024. Which basically means that the Merkle proofs that are generated even now would be valid to a point when, for example, we kick up the Blobs per block to a high number in Sharding. So basically the block, inside the block we have the list of commitments based upon this high value. But we still basically have four or 16 Blobs right now that the CL can handle. And depending upon what we feel like, maybe we want to kick up the current max Blobs to 16.
I mean that that is an independent question from max commitments per block. So these are the two discussion points being discussed in that PR.

DANNY:
 Okay, so we get proposed an additional variable that gives us the shape of the block, shape of the Merkle tree with respect to the block that would be forward compatible and then an additional constant to bound the actual amount that we're willing to accept currently and that could be synonymous with the value that’s in the execution layer or that could have some growth baked-in, like upto 16, upto 2 Megabytes. If we wanted to give a little bit of elasticity to the execution layer without the Consensus Layer needing a fork, that’s where we’re at.
Yes, Okay Great Thank you.
Yeah.
I just want to bring this to people’s attention. This is something that has had active discussion and might have tiny changes with respect to constants and how they’re configured. Are there other discussion points on this or questions on this topic? Please jump into this PR . I think this is one of those minor details, but one that we should get ironed out maybe by the next call and may be the next release that might include some of these other minor features that are going to get in. Okay, check it out #338.
Great. So those are our General Deneb discussion points.Are there any other items that we want to discuss with respect to any ongoing issues or any updates with the testnets? Anything Devnet?

Barnabas Busa:
Basically this morning when Mario started we saw some problems unfold.Erigon is crashing with some very massive print statements and the Netherminds “nodes” were  unable to propose blocks. We had a short period of non-finalisation also 

Danny: and this was a transaction fuzzer, you said? 

Barnabas: It was but it was not working correctly , as far as i understood. 

MariusVanDerWijden: Yeah. So, I have no idea what I did.
I basically, just started the Fuzzer and because I was not using my own node, I don’t know how many transactions I sent.
I don’t know what transactions I sent . And I’m also not sure if this is actually me causing chaos. I’m going to setup my own node so, I can better see what’s happening and what I’m actually doing sorry It’s very fuzzy at the moment, but I’m glad that there have been some issues uncovered already. 

Danny: Are you Okay, Marius?

Marius: Kind of, but Yeah, Great.

Danny: Okay Cool. That’s Exciting. Good to see that stuff now rather than later.

Okay.Any other on the Devnet?

Barnabas: Not right now. Okay.

Danny: Tim did threaten to hijack a  this call to talk about SSZ.Tim do you want to give a status update or any time on that?

Tim Beiko : Sure, so Basically the status with SSZ and #4844 is that as I think the EL client teams have started to implement this. There’s been questions around. Is the amount of SSD we're introducing with #4844 actually helpful to getting us towards full SSD on the EL and if it isn't, then does introducing sort of partial SSD now and not being able to fully leverage it. Actually make things worse than simply sticking with RLP to encode the #484 type three transactions? And I know that Light client Roberto and Etan have been discussing this a lot on the discord, so I Don't know if either of them have an update.

Danny: Yeah.Right now, SSD kind of like flat #, is kind of in the worst of both worlds.Like we add a new dependency and don't really make it look like it's going to look in the future.So then the question becomes, try to make it look like it looks in the future or move to ROP to not be in this unhappy medium. 

Tim Beiko: Right, and I think Etan had changed his EIP 6493,I believe, based on part of that feedback.But yeah, Matt, I saw you came off mute.

Danny: Yeah, please.

Matt: I was going to say, I think this is one of those things where it's hard to make it look like what we think it should look in the future without having an extremely clear idea of what the future should is going to look like.And I think in the past we've done this thing where we think we're being forward compatible with the world,but then the way we understand the world, the world changes a lot in the one to three or four years it takes to complete the thing.So it's just really hard for us to actually put SSD here in a way that we know is going to be forward compatible. And I think the reality is that it's almost certain that we'll either constrain the design space in the future or we just have to straight up change what we choose today. 

Danny: And I will make a quick comment that this does primarily affect, the execution layer. So we don't have kind of a full consensus of people that might be interested in making discussions.This is a bit more of a status update, but we can have more discussion if anyone has additional points.

Tim Beiko: Actually, one thing I'd be curious to understand better, shall we? You made a comment in the chat about how this would affect the CL specs if we move completely to RLP. Do you mind maybe just sharing a bit more on that?

H:  Yes. So in the we have a function to SSZ, the block version hashes.So right now it's SSD and we use the SSD logic to pass the bytes and to found the version hashes.So that function has to be changed if we use the full IOP transaction. 

Matt: I had one idea.I'm not sure this is possible, but if we're able to have the version Blob hashes of the transaction in two places whenever it's being propagated among CL’s, where we have it represented in the RLP transaction, and then we have it outside of the RLP transaction in a structure that the CL can understand. And what we could do is then we could verify the Blobs and all the information against the version hashes that are outside the ROP transaction. Once all the checks are complete, we give the ROP transactions and those hashes to the execution layer over the engine API. And the first thing that the execution layer does is it just checks to see if the #’s in the ROP transaction match the #’s that were provided outside of the ROP transaction.That way you don't actually need to do any kind of ROP work on the CL, 

Danny: and an upgrade  to the encoding would be opaque to the CL at that point, or transparent, wherever the word that is meaningful there.But we wouldn't have to do anything.

Matt: Yeah, it's slightly more complicated, but it seems like that would allow you to avoid having RLP on the CL.

Arnatheduck: 
With regards to the forwards compatibility argument, I mean, two things.First of all, with RLP,we're definitely not forwards compatible.And the second thing is that SSZ kind of brings features today already, right? You can build nice merkle proofs over them and stuff like this.So it's not like 

Matt: Not in the way that we're using it now. We're only sterilizing SSE. There's no hash tree roots.I mean,
Dankrad Feist:  Why are we doing that anyway? Why are we just doing the hash tree route?The arguments for that seem rather weak to me.We can use the hash free route.

Matt: I think there's just like, more strange things that start end up happening.Like if we use the hash tree route,then what goes into the Merco patricia trie.Is it the type transaction prefix with the hash tree route?Is it the SSD route?Like the transaction hash comes out of the fact that it's like the hash of the transaction that goes into the merkle Patricia Trie and so we start opening the box of all these weird things that we have to figure out.

Danny: and the why.It's a flat hash.I think if I remember correctly, it was an attempt to get SSD in there in a very minimal way.But again, in retrospect, or maybe it should have been clear at the time, it's kinda the worst of both worlds.We can continue to discuss this.I think it's maybe more appropriate that now we've just kind of highlighted that this issue exists and to engage the conversation between now and leading up into the execution layer. Call next week where we'll have more of the relevant parties.Any other comments on this one today?

Tim Beiko: Yeah, hopefully, we can resolve this in the next week or so.It does feel like on the el side, it's like the biggest spec issue with regards to 424.

MariusVanDerWijden: So one thing that kind of like we have to change the transaction types at some point anyway,and I think it would be better to have them all RLP until that point and then figure out something where we can convert all of them.And one thing that if we were to go this route of having the block transactions in RLP, one thing that I Would really like us to do is to create this conception that this transaction type will not be there forever and we are going to drop it at some point in favour of the full SSE block transaction type. Once we have the SSC transaction route, so because we suspect only roll ups are going to use this transaction type,it will most likely see very little usage.And so if we go this route of having it RLP, I would like to state from the beginning that this is like a temporary solution and we are going to drop this transaction type fully at some point.

Danny: Essentially a deprecation notice at the creation.

MariusVanDerWijden:  Yes.Well, we are going to like this is the thing, right?This transaction type will only live for a very limited amount of time either way, if we do the SSE stuff or if we do the RRP stuff, once we go to the full SSC transaction route, this transaction type will be changed anyway. In my opinion, it would be way easier to make it as close to the current transaction types. that we have, so we don't have to have another special case when we do the transition to full SS. 

Danny: I have a question. When we plan on for any transaction type that exists, if we're going to migrate from RLP to SSD, would that be actually the deprecation of a transaction type fully or a mutation of the transaction type? So we take type one and then kill it and make type four?Or would type one mutate?This might not be satisfied. I realise I haven't thought of the answer before. 

MariusVanDerWijden: So, With the other transaction types, we don't want to fully deprecate them because we still want to allow for this use case that you signed a transaction at some point in the past, and this transaction should still be valid. 

Danny: So using the creation of new types.

MariusVanDerWijden: yes. Maybe we can get rid of them. If we provide, for example, a pre compile that you can send this transaction to then executes the transaction for you.Something like this? There are workarounds around it, but yeah, that's the basic idea.

Danny: Thank you.Okay, I propose that this active conversation continues the next week and we get all the relevant parties on the executionary discuss in one week's time.Thank you. Other deneb related discussion points for today? Okay, great. We have a number of items in the specification not related to NAB that we'll go through now.Just a heads up.The Atnet revamp that's been spearheaded by Age that was discussed two weeks ago will be merged soon after this call and we'll make it into a release.This is backwards compatible.This does not include the down scoring so that people can roll it out over time, and we would add the option for down scoring at a hard fork in the future. Any final points on that? Cool, thank you Age and others that have kept this one moving.Okay.  Is Michael Sprout on the call?I don't think so. Michael Sprout brought up the beacon APIs #317. This is add broadcast validation to block publishing. I think we've discussed this. Now there is APR. This essentially allows for relays todo a full verification before broadcasting light of the unbundling attacks. This helps prevent relays from having to use a forked version of a client, which would help plu client diversity for this use case, I believe there's not been much contention around this, but open it up for discussion now if you have discussion points. Otherwise please take a look at this PR and we will probably aim to get ironed out and merged relatively soon. Any thoughts here?

Terence: So we have some thoughts, right?So let's just take a step back on why we are doing this, right? Because the first thing is that having client Fort is not ideal, right? Because now Prism has its own Fort, Lahore has its own fork and then the second thing is that fully importing the block is not ideal either because the currently broadcast and we fully import the block. By fully import, I mean, you also do execution check.You import the block to the DB, and then you import the state to DB, and that's pretty slow.And then the whole idea is the relayer wants this out as fast as possible. So we find out that, hey, we can actually skip all those steps.We can just verify the consensus site only.And as it turns out, we were able to reduce 80% of the latency by doing that.And therefore, it does make the builder and the relayer very happy. Right? But the downside with this is that we're kind of like working with the relayer versus working on insurance.PBS first, because now it kind of becomes this whiteboard game that we're just like keep adding this feature to support MVV Boost or PBS that's out of bed.And that's probably the biggest concern here, for example, because now if they want some sort of equivocation check to check for slashing and then we probably have to provide that blah blah blah, that is another angle to it.So from our end we're pretty torn because we can be like yeah, this is a nice to have but at the same time we kind of like we're slightly worried that we may be moving away from just doing HTML but then I can see the argument of having both working on both at the same time.So yeah, this is just some two cent from our side.

Danny: Got it.Thanks Terence. Yeah, I guess the way I view those arguments like we live in a world where MAVBoost exists and we could see some degeneracies in client diversity and usage and other things if there are not some faculties to make it work appropriately. But I definitely sympathise the other argument.Yeah, it seems like Age on Lighthouse side kind of agrees with the issues at hand as well. Sure, okay, yeah, I guess have some discussions with your team to make some sort of opinion about whether this should or should not go in and whether this path in general should not should or should not continue to be supported. And please bring any comments you have to PR 3175 on the Beacon APIs. If so, we can continue to have this conversation.Any other points on this one ? And thanks, Michael Sprowell, for getting the PR up. Okay, Michael, you have an open PR on the consensus specs send store finalised block hash to El. Can you give us an update on this one? 
## 4. Research, spec, etc
## Attnet revamp: Subnet backbone structure based on beacon nodes consensus-specs#3312

Mikhail Kalinin: Yeah, this is a pretty old PR, and basically it states that Consensus client must use must read the finalized block hash from the store instead of. to specify this explicit statement saves us from the case where the had state might be used to read this block Hash while sending to El client, which in some very age cases can lead to finalised block Hash being, like, reverted back into the block history, which would potentially cause some UX issues. And apparently all your clients already follows this logic. So there is an intention to finish the work in this PR and I would like to just bring it for client's attention. If there are any objections, please rise them in the PR.That's basically it. So the idea is to probably work on the test if it is possible with the current testing framework that we have to test this particular thing and get it merged in the coming weeks. 

## 5. Open discussion/closing remarks

Danny: Yeah. Thank you, Mikhail. That's pretty much it. Any comments on this one? And I think there's maybe one or two people that are unmuted and I'm having trouble muting them. So if you can please mute yourself. Thanks. Okay, there's one other Deneb item that I forgot to bring up. There is not a spec for this already, but in process attestation for the security proofs around the fork choice in relation to some of the recent patches and for the very exciting confirmation rule that is in research post right now.There needs to be a slight one line modification to process attestation right now there's kind of this rolling 32 slot window for a given attestation.For a given slot to get in, the modification would be to rather than for the previous and the current epoch or for Nand N plus one where the Attestation is from N. It has just a rolling 32 slot window that it can be included. The modification would be if it's from epoch in,it could be included up to the entirety or the entirety of epoch N plus one.This modification helps with the security proofs and helps with the confirmation rule.So that is a one line change we're going to get a spec up for soon.This is probably the addition of a few tests and modification of a few tests on our end.So very small on the consensus spec.It's security related, so I think it should be expedited. But I will open it up for conversation if anybody had any discussion points today and then by the next call we'll have a stack up for further discussion. 

Arnetheduck: What about gossip? We limit by the same 32 slots if I remember it right.

Danny: Yeah, I'll have to take a look at that. But you're right, we need to probably make sure those are under the same conditions.

Enrico : In the telegram we also discussed about rewards. Are there also discussion points about making them valuable when including in the block,

Danny: do you have particular details?Is there essentially like a degradation of rewards prior to the epoch that would make them be ignored?

Enrico: Yeah. If I remember correctly, at some point those attestation actually become worthless. And since we filter out attestation that are worthless in the beginning, so we are not going to select them when we produce blocks. So I'm guessing if there are impacts also in this area to. 

Danny: Ben, you have, I think, the graph of degradation of value of attestation more at the forefront of your head. Can you explain where we're at?
Ben: Yeah, so correct target expires after 32 slots. So as Enrico said, the asset station becomes valueless.Actually, penalised after 32 slot is equivalent to missing it.

Danny:  Got you.Okay, then we'll open that up as well when we're taking a look at this P2P real quick.Yeah. Okay.It also has the 32 slot bound on the attestation propagation slot range. So yeah. Age, not one line. Nonetheless, we'll get the spec and try to get a kind of complete view of the necessary changes here.It's a pretty important security improvement, so hopefully we can figure out a simple path forward. Any further comments on this one? Great, thank you. 

Any other discussion points for today? 

Great.Okay, thank you everyone. Take care. Talk to you all soon. Thank you. Thanks, guys. Bye. Thank you.
## Attendees

* Danny
* Ben
* Enrico
* Arnetheduck
* MIkhail
* Marius
* Matt
* Barnabas
* Dankrad
* Tim
* Gajinder
