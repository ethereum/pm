# Consensus Layer Call 109

### Meeting Date/Time: Thursday 2023/5/18 at 14:00 UTC
### Meeting Duration: 1 hour
### [GitHub Agenda](https://github.com/ethereum/pm/issues/783) 
### [Audio/Video of the meeting](https://youtu.be/Iy5zTJIXhQU) 
### Moderator: Danny
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
109.1  | Consensus specifications, PR #3338: Gajinder Singh, a developer for the Lodestar (CL) client, introduced this pull request (PR) on ACDC #108. The PR introduces a “max_blob_commitments_per_block” field on the execution layer (EL) for changing the maximum number of blobs that can be attached in a block. Blobs are the new transaction type that will be introduced through EIP 4844 and used by Layer-2 rollups for cost-savings. PR #3338 introduces greater flexibility to the protocol so that only the EL needs to be updated, rather than both the CL and EL, for making changes to the maximum number of blobs per block.
109.2  | Consensus specifications, PR #3359, requires Execution APIs, PR #407 and EIP 6985: During ACDE #161, developers agreed to remove SSZ encoding from the EL implementation of EIP 4844. To support this, there are a few changes that need to be made on the CL. Namely, checks of KZG commitments attached to blobs must be added to the preprocessing work of nodes alongside the usual checks of block hashes. 
109.3  | Consensus specifications PR #3346: Related to PR #3338, this PR specifies the number of subnets for propagating blobs as equal to “blob_sidecar_subnet_count,” instead of “max_blobs_per_block.” This ensures that changes to the maximum number of blobs per block does not impact or requires changes to the peer to peer network structure and blob subnets.
109.4  | Consensus specifications #3354: As discussed during ACDE #161, there is a input and out mismatch for the EIP 4844 precompile. Developers agreed to harmonize the output to rely on big-endian ordering, instead of little-endian and reconfirmed on this week’s call that in all cases went it comes to EIP 4844, the default data storage ordering should be big-endian. Hsiao-Wei Wang, a researcher for the Ethereum Foundation said that tests for this change have been fixed.
109.5  | Developers discussed updates on EIP 4788, which allows smart contract applications on the EL to verify proofs of CL state. This is beneficial for improving the trust assumptions of decentralized staking pools, restaking protocols, MEV applications, and more. During ACDC #108, developers agreed to start working on EIP 4788 for inclusion in the Deneb upgrade. Marius van der Wijden, a developer for the Geth (EL) client, raised concerns around the EIP’s use of the current slot number to expose Beacon Chain block roots in the Ethereum Virtual Machine (EVM) as opposed to a timestamp.
109.6  | The confirmation rule: Developers gave updates on PR #3339 under the Consensus specifications repository. Also known as the confirmation rule, the PR introduces a new algorithm for nodes to calculate whether a block is confirmed, that is never to be changed or replaced with another block, based on certain assumptions such as network synchrony and the percentage of honest validators. The confirmation rule primarily improves the user experience as it could help provide confirmation of Ethereum blocks in under a minute, as opposed to 12.8 minutes, which is the time it takes for Ethereum to reach chain finality. While the confirmation rule would not be used to replace finality guarantees, it could be used for network stakeholders to more closely and accurately track the head of the Ethereum blockchain. The PR is in the process of review and performance checks.



**Danny**
## Intro
* Okay, we should be live on YouTube. Let us know if you're there. this is consensus layer call number 109. this is issue 783 in the PM repo, which you're following along. Great. 
* I know that there was a maintenance incident, fortunately chain stayed alive and kept going, and resolved itself. I know that there have been a couple of client releases and there is also a postmortem out, by Prism. Is there anything that we want to discuss about that today? I know there's ongoing testing and analysis. Okay. if you're listening in check out Prism's postmortem, it's good. I think there will be continued work on this for a while. Thanks. All right. 

## Deneb
## Update block's blob_kzg_commitments size limit to MAX_BLOB_COMMITMENTS_PER_BLOCK (4096) consensus-specs#3338 [5.06](https://youtu.be/Iy5zTJIXhQU?t=305)
**Danny** 
* Moving on. we're gonna look at we have a number of issues. I think a lot of these are updates and things that we're trying to make final decisions on. and we will begin to go through them. So there's this open PR 3, 3 38, which is to, make it so that the KCG commitments are, or the, the blob commitments can be much larger than the actual gas limit. It seems like the consensus now is to, have it at a pretty large number on the order of thousands, but to keep there to be a restrictive content that's in the around of the gas limit, such that this number, the smaller number, can be increased, without changing the shape of the Merkel tree, which is a property of sse given the max English size. is there any update on this? I it seems like we're on the order, on the, the verge of consensus and that we just need to, do a final cleanup and review. 
* Okay. Is anybody against the two value strategy where we have, a large value that helps us shape the Merkel tree in a small value, which is in the order of what we can actually handle? Okay. I believe this PR was by Is there anything that we need to do to get this cleaned up? or are we in a good spot to just do a final review and merge? 

**Gajinder**
* I think, we should be good for the final review because there is one comment and, regarding the site car validation. So I can, remove the extra validation comment that I added, while validating the site car that it should be, the index should be less than, max blobs per limit. So since the subnets, anyway, are going to be open, then max BLS per limit. So it's sort of a redundant validation that I added. I can remove that. 

**Danny** 
* Okay, great. Other than that, we'll put some finalize on it and get this in. just for context, you know, this is probably one of about four things that we're trying to get finalized for, a release for new testnet. So this is on the list and we'll get that done. 

## Engine API: validate blob versioned hashes execution-apis#407 and Use engine_newPayloadV3 to pass versioned_hashes to EL for validation consensus-specs#3359 [8.15](https://youtu.be/Iy5zTJIXhQU?t=494)
* Okay. the next is there are a couple of prs, about this ongoing conversation. I believe decision made to, pass the version hashes into the engine API to do the validation against the transaction so that we don't have to do the, transaction peaking on the consensus layer. there's the engine API and there is the, consensus spec change. are there any comments here other than just needing to review and get these merged Basically? 

**Mikhail Kalinin**
* Yeah. I would just like to say that the PR is kind of ready to get the engine API and, one, not a big question, but just, would like to attract client developers to this thing. Is that how to pass this version currently PR suggest do this by, introducing a second printer to new payload call, which obviously breaks some extractions that, we had before on log. but the other option would be to introduce an to pass payload and as one object, but that's as well some. 
* So it's, the, what what's done currently is just, you know, try, try to avoid, do some new, data structures to engine api, but probably, it's easier for some clients to implement it as it was the inside of an envelope. So that's basically one of the things that, I'd like to, to people to take a look at. And yeah, any if that's fine as is, then yeah, we're ready to go. yeah, to address and gars comments, yeah, so, and yeah, so that's basically this, PR just what it does is just first this check the el it does not, you know, change this, trust assumption in any way. Then passing a list of hatches, then we need to decide, which, yeah, we could do hash probably, but doesn't bias that much. 

**Danny** 
* Yeah, I mean if, if the data transfer was a problem, then we would consider that, but by compressing it, we just reduced the ability to communicate error messages and, and other things. So I, unless there's a strong reason I wouldn't do it. 

**Mikhail Kalinin**
* Right. That's, yeah, follow off the chat. So yes, it's not about the availability. so, but I really, I don't understand what's broken by just different this chat 


**Danny** 
* Because the check only happens when you're synchronously communicating over the engine api. So in the event that the, execution layer is syncing, it doesn't actually ever, it can't ever verify these Merkel commitments, for the past components because, it doesn't have them. Right? And so it only happens when you're doing this synchronous check. 
* There is a precedent for a value that's done in the synchronous check, and that's the block hash, which is also passed in from the, there's a block hash embedded in the execution payload and the consensus layer, and that's passed in, and that's only checked, you know, the consistency between what's shown up in the execution there and, and the, whether that hash is correct, in when you're synchronously communicating. 
* So Anka, there is a precedent for this. and the assumption is that, this type of synchronous check, even though it's only happening when it's synchronous, you can only really potentially fool a, sinking node. And so yes, that exists. It already exists with the block hash. You can fool sinking nodes about this validation, but it's very difficult to pull the network. does that make sense on Anskar? 

**Anskar** 
* Right. I mean, I'm not super familiar with the, with the block cash situation. I would then consider this an issue as well, but, I don't think it's a good idea to, once we recognize there's an issue to basically say, well, you know, this property's gone further now, so now we might as well just stop caring about it. my question then would be, if we stop care about this, why do we even still have, why do we even still store the EL head other than of course the values that we want to make accessible via the block hashes from inside the EVM I mean, that's a reason. But for integrity checks, then we might as well just completely never store anything and just treat everything ephemeral information. 

**Danny** 
* No, like I don't follow that, nor do I necessarily agree, but the block hash or somebody familiar with the engine engine api, even if you're syncing is block hash checked 

**Marius**
* The you mean the execution layer block block hash? 

**Danny** 
* No, the, the block hash. So there's a block hash that's explicitly in the, okay. Block hash is always checked by the engine api. So these could also always be checked by the engine API vote add overhead during sync. 

**Marius**
* Oh, you mean, you mean during the, the consensus layer sync, not the execution layers. Yeah, during the consensus layer. During the execution layer, I think we, we always check the block cause we have to start chain, No, sorry, we're talking about two different things. Yes. 

**Danny** 
* The, because during the, The engine API has an additional field where the consensus layer says block hash. 

**Marius**
* Yes. We check that on every, No matter what. 

**Danny** 
Y* eah. Even when you're in like a sync status and doing other stuff, if somebody gives you a new payload, you check that. Yes, yes, yes. Okay. So to not change the assumption, the sync assumption here, this field, this list of kvd commitments would also have to be checked at the same time, like block hash is checked no matter what. Even if execution layer is syncing, is that something that we're willing to do otherwise? 

**Mikhail**
* We do change the assumption It specified in the way we discuss now do disregarding and so to block check. 

**Danny** 
* Okay. So then as long as clients can and are willing to do that, this does not change the security assumption at all. 

**Mikhail**
* Yeah, and I thought that by default it's possible, as we have discussed it. Yeah. So if it's not, please your concern in the PR. 

**Danny** 
* So on, just to be explicit, in the execution payload, which is a consensus layer data structure, there's a couple, there's an ex thing called extra. There's just an extra field called the block hash, which is the execution layer block hash of the rest of the payload contents. This is passed into the engine api and  before the executioner does anything, it checks to make sure this, that that hash is consistent with the rest of the, the payload fields. And so it, it does this kind of like synchronous check. and it does that independent of syncing. 
* And so these KVD commitments being, correct against the transactions would also be done kind of in that pre-processing before returning anything related to syncing or or otherwise. And so they're precedent for doing this. 

**Marius**
* How how costly is the block is very cheap for us. 

**Danny** 
* This is, you have to look into, so you have to des theorize transactions and pull out a field and check the field against it Huffy today, that's fine. 

Speaker: 10
* We already have to des serialize them and alize them. 

**Danny** 
* Right. So this is cheap we can talk about, I can explain it again or we can talk about it outside, but it's, it's exactly the same thing. It's not these block, the block ashes are not guaranteed to be self-consistent here because this is an extra field in the consensus layer. It's kind of like how the KVB commitments are an extra field in the con in the consensus layer. 
* And we have to ask the execution layer now to make sure that they're, they're equivalent to what's in the transaction similarly than extra field called block hash and the consensus layer that we ask to make sure is consistent with the rest of the fields in the execution layer. but yeah, I'm confident that this is very, very similar and we can talk about it outside the call. 

Speaker: 10
* When do CL start sending new payloads while the EL is thinking The CL does? 

**Danny** 
* Is it CL? Yes. 

Speaker: 10
* Is it, is it from the like weak subjectivity checkpoint? It's from wherever you're syncing from And that point that you're seeing from is the weak subjectivity checkpoint that you've chosen? 

**Danny** 
* It certainly could be. It also could be since a day ago when you turn your note off. It also could be that you use a weak subjectivity hash and eugen sync and, and check that those hashes are correct when you get to the head. So it, it just depends on your model. Got it. Okay. So there's a few things here.
* One, I'm pretty confident this is the same type of thing as block hash. And if we're doing the validity check up front independent of syncing, then we're in an okay validity check mode that looks exactly like we've done something in the past. we do need to validate that this is not put induced, unprecedented load, in the pre-processing check. which we're pretty confident is the case because you have to do the sterilization to do the commercialization anyway. 
* And so we should Sandy check both of those things and if anybody has issue with the way this is done, they should jump into the engine api, PR very soon. Like this is something that we've pretty much decided and we need to make sure Sandy checked that this is correct and Okay. cuz we're looking to do a release this coming week to get this on set test notes. Okay. and Anskar, you and I can sync on, the validity of this and convince each other that this is either okay or not. anything else on this one? 

**Terence**
* Yeah, so, one thing to notice, I don't have a good answer to this, but I want whoever is working on the builder that is like to be aware of, it's that now before, given that the CL can verify SSZ block transaction, you can actually verify that before, but now that CL can no longer verify that we have to relay the EL to verify that. 
* So I'm not quite sure how the relay will be able to verify that. This is kinda like an open question, so I what you think about that? I don't, I don't have a good solution to this, but Yeah. 

**Danny** 
* I don't know if I follow because the relayer can also ask their execution  client, correct? 

**Terence**
* Yeah. Basically relayer needs to code a new pay, right? But it does, me might not want to do that because it's slow, right? It's basically they wanna reduce latency, but they just wanna verify the alignment between the block transaction Russian hash with commitment. But,  then instead of verifying the whole thing, they just want to verify that. But but then you cannot do that anymore. 

**Danny** 
* Yeah. I suppose if a relay is being lazy or optimistic and they're not running all the transactions, then they're already taking an assumption that their builder is giving them correct values. So I don't know if not doing this consistency check is really changing their model too much. 

**Terence**
* Yeah. Fair. That's, that's a fair point. 

**Danny** 
* But I mean, agreed. Something to think about, if that's how you realized constructed. Okay, great. this is on the list of things that's going into release early this week for next test nets. Please take a look at this if you have, concern or if you have, if you want to kind of weigh in on, on this strategy. 
* Okay. I believe we have a relatively non contentious PR that is adding a variable to kind of make the number of blob sidecar subnets, look and how those are specified look like how attestation subnets are specified, which is with its own variable so that it can be tuned up and down independent of the actual number of blobs. pop do you want to give us a quick on this one? 

**Prop**
* Yes. currently in  the current spec, the, the number of psycho cause it's a public is equal to Max Bob, blob. but it's not good because, because if you want to, if you want change  the, the number of something is changed, right? 
* So I hear a new stand,  how the sub the So if we have like the, the, the the max blob get and the the subject cart, that will be some subject that, that, that will be used for to blob. So it's like if we, in this,  we can change the max blob, like even in independently, like without changing the number of subnets, Right? 

**Danny** 
* And this is the, this is parallels how application subnets are done independent to max committees. I do think it's a no-brainer to have these as two configurable values rather than just one. I think we were, we had some build issues due to some CI cash problems, but this is likely be merged later today unless anybody has, an issue. 

**Gajinder**
* I have a confusion over this in the sense that in the first PR that we discussed, we introduced a variable max commitments per block, which was set to be 4096. Now we have max blobs per block, which is currently set to four, and then we have another for subnet. So I think the, the new variable for subnet and max block per block, they are doing the same thing as of now because we rejected max block per block to be independent from what CL can handle in the subnet. 

**Danny** 
* So Right, so they're not doing the same exact thing. so if you had max blobs per block is four and you changed the sub or to eight and you changed the subnet count to, you kept the subnet count at four, you would then have two blobs being distributed per subnet. and this is kind of a, this allows you to tune the, essentially the gas limit independent to how it's delivered on the P2P mesh. 
* This essentially allows, yeah, allows for reuse of, subnets, for additional blobs instead of always making new subnets. All right, cool. 


## Update the endianness of the polynomial commitments to be big endian consensus-specs#3354 [26.22](https://youtu.be/Iy5zTJIXhQU?t=1582)
**Danny** 
* Okay. next up, 3354 the endianness of the polynomial commitments to be big endian. this has been an ongoing discussion. I believe that there's general agreement to swap over to big endian. I, in discussions it was maybe unclear if that's to do for everything or rather just one interface. 
* Can anybody give an update on where this stands in relation to what's gonna happen in the libraries and, and everything and if this is ready to go in? 

**Gajinder**
* So, I maybe can say something on this that, for the, on this EL side, now that we have RLP transactions, basically it will anyway, all the data will anyway be encoded in big endian and, so, and if the pre compiles are also big endian, so that basically solves a problem of el but that means that library will have to take inputs also in the big endian form.
* So either the library fully shifts to big endian or, particular, pre-compiled verification function, which verifies blob version hashes, sorry, which verifies commitment version hashes on approves. Basically it can just take big endian as input and library can do whatever it wants to do in inside. 

**Marius**
* Yeah. So it, it's really not an issue for us. We can, before we call the, the library, we can just turn, turn the inputs around. So like the library, like the library should do what they want. And the preco like as long as like there's a shim anyway between the pre-com pile and the library, so we can, turn the bots around. 

**Danny** 
* I believe there was a desire to change the limited interfaces in the library, right? 

**Marius**
* Yeah, yeah. We definitely want to change the libraries because it doesn't make any sense for them to be the endian now. Like the only reason was because we expected the consumers to belittle endian, but now it seems all the consumers will be big endians, so there's no point in keeping the library little endian because all the backend BLS libraries also be big endian. 

**Danny** 
* Got it. with respect to the PR that's in the consensus layer, is this ready to go for final review or is there, are there additional changes that need to be made? Does anybody know?

**Danny** 
* Okay. So this is on the list of the handful of things that are going into the next release, and this is likely to be merged in the next few days. if you have any position, desire to review or comment, please do so immediately. Okay, great. Let's see. Alex, I believe you wanted to give us some 4788, updates. 

## latest 4788 updates Consensus-layer Call 109 #783 (comment)
**Alex** [30.10](https://youtu.be/Iy5zTJIXhQU?t=1810)
* Yeah, I can do that. let's see. So 4788 is EIP to send over, let's say the beacon block route, to the EL so it can be exposed in the E V M in a trust minimized fashion. It says lots of great applications for staking pools, retaking, MEV stuff, all sorts of things. So, this might be, at this point more of a execution layer conversation to have. 
* I think it's pretty minimal on the CL, so, there might not be too much to discuss here. But that being said, on the last ACDE, we decided, so the way it was written before was that the EL would use timestamps to figure out which slots correspond to which block route. So essentially the block road be sent over.
* And the question now is which slots does it pertain to? And if we send over some, well, if the EL just has some, slot data, like for example, knowing like how to map timestamps in the slots, then it can just do the computation itself. We decided to not sort of violate the abstraction barrier between the two layers and then send over the slots along with the route. 
* And so that's what the latest changes are. I think there might have been even some pushback though about this approach. So I don't know if anyone's had a chance to look and if they have any thoughts or feelings about the direction this is going. 

**Danny** 
* Yeah, I was the one that put the comment. I didn't realize that that was the outcome of the last ACDE. it, I understand the abstraction there. It does in excessive to use, you know, the en the execution payload header as a messaging bus for the slot. But at the end of the day, I don't have a very strong opinion here. Yeah, I mean, I kind of agree or Go ahead, Maur. 

**Marius**
* Yeah, I don't, I don't, I also don't like the putting the slott in my head.  I don't fully get why we need to store, like store it by slott and not store it by, by timestamp and let the, let the smart contract figure out the slott or the other way around s store the beacon. 
* Like right now we are storing a mapping of slot to beacon route. If we would turn it around and store a mapping of beacon route to timestamp, the, the contract would need to provide the beacon route. But that's kind of fun, I'd say. And, and then get the timestamp for it because like the, I don't, I don't know if I'm wrong, but like the only really use case I would envision is, a slot trying to verify that a certain beacon route was, was, was, was there at some point. 

**Danny** 
* And I think it, Yeah, I mean it's generally to make proofs against, right? 

**Marius**
* Yeah. But like you can, like, if you provide all the data yourself, you can also make proof against it. but you need to make sure that this was, this was actually at one point in the chain, right? And so if that's the only thing we need this for, then why do we need to, return the, why do we need to return the, the beacon route if we can just like provide the beacon route and say, okay, this was at one point or at this slot, this was the beacon route, I'm sure. 

**Danny** 
* I See how the lookup can work either way. it does complicate the data structure in using a mapping, which would probably be more of unbounded in, in growth rather than, a ring buffer or a a which could be more simply bounded in growth. I think the, the UX of the mapping in that direction makes intuitively more sense to me, but I I agree that given the use case, both would work. 

**Marius**
* Yeah. So, anyway, I've, I've implemented the current spec without the slot with only the timestamp and, it's kind of not, not hard to do, it works.  what I, right now, what I don't like is that it's, it's an op code that reads a certain address and a certain, and a certain storage slots. 
* I would rather make it a precomile State Precore State precore. Yeah. It's kind of a new concept, but, anyway, we implemented, it's going to be a new concept if we, if we implemented  as something that is not in the state, it would be like a new concept. Cause  we cannot look it up, like we look up the block hashes. so we would have to have like another like part of the storage and, also I think Alex doesn't want this because it would mean that the, that the state transition function is even less pure than it already is. 
* And, so I think yeah, the, the putting it in the state, makes more sense to me. And then if we put it in the state at, at a specific address, then it kinda makes sense to make this a pre-compile. because then we, we kind of know what, what happens and we like if we, if we have this, op code that reads it, like we have to think about all of these edge cases that we don't have if we know it's a pre-comile, for example, like what if someone calls this, calls this address that, where the, like the storage lifts or what if, someone's self destruct to it or like there's a bunch of edge case that, that are figured out with PREPA that we don't have with this yet. 

**Danny** 
* Yeah, I personally think a stable, stable complete miles are actually very useful, especially in stateless where you're trying to not have as many kind of like assumed hidden inputs, to various things.  I think that it's a design pattern worth, you know, making a thing even though it's not a thing yet. 

**Marius**
* Yeah, that's kind of, that's kind of my only problem with it. It's, it's not yet a thing and, in order to make it a thing we think we kind of have to like think about it. So like if, Yeah. 

**Danny** 
* Yeah. I mean, and that, that's one of the things is, you know, engineers seeing if state four pre piles break some deep assumptions and, and their software because, from a theoretical standpoint, they seem fine and clean. I think from a engineering standpoint, it's unclear until y'all say, so, Yeah. 

**Marius**
* So in general, I think  this eth is not really yet ready yet. And, we shouldn't push too hard on it, before these things are iron out. So that's, that's kind of my take. Like, it, it's a good, it's a good eth and, and we can, we can definitely do it. but like pushing it into cancun could be hard..

**Danny** 
* Hard because you wanna, because you think it should be a staple pre-compile, but there's gonna be a lot of uncertainty when we go down that path. 

**Marius**
* Yeah. But we should make sure we have this concept of a staple pre pre-compiled down, if we make this change. 

**Danny** 
* Okay. I think it probably makes sense to do a draft PR of a state full pre-compiled version and to talk about this on an execution call in one week. 

**Alex**
* Yeah, I agree. Marius, do you feel strongly about somehow also trying to look at storing things by timestamp rather than slot and just ignore the slot at the EL? 

**Marius**
* Yes. Yes. I, I feel very strongly about not having the slot and the header. 

**Danny** 
* I feel strongly about that. Yeah, sure. But, but like we can instead just have the el compute this some other way, like the el just needs a few constants to be able to do the timestamp to slot conversion. 

**Marius**
* So that much of an ask That is kind of, that is kind of leaking the abstraction. 

**Danny** 
* And, it will Well It's also the point of the EIP  Yeah. 

**Marius**
* Yeah. It, yeah. But it means that like for every test net for every network that we set up, we have to Yeah, yeah, yeah. Kinda do do this whole dance of mm-hmm. of creating something that, that works in both sides. 

**Danny** 
* Right. okay. I'm gonna think about, timestamps and see if we can make that look nice and yeah, I can make this look like a staple pre-compile definitely in the next couple days, and then we can discuss next week. 

**Marius**
* Perfect. 

## attestation inclusion range increase EIP-7045: Increase max attestation inclusion slot consensus-specs#3360 [40.07](https://youtu.be/Iy5zTJIXhQU?t=2407)
**Danny** 
* Okay. the last thing is for Dann is 3360, which is a, we agreed on a previous call that this is something that we want to see in Cancun. this is the expanding the attestation slot range from instead of slots for epoch to be, either from epoch n can be included either in epoch or n plus one we're in is the epoch that the at station was created in. this is to improve or to allow our security proofs to work properly for guest, as well as opening up, the usage of a confirmation rule, which is in progress, in which  will talk about, talk about soon. this is two lines of change in the state transition spec, as well as the modification of gossip conditions. I guess the final to do is to get some review here, and I'll probably open up an EIP in relation to it to give it kind of a number to track it. but I would like folks that from various teams to thumb up thumbs up it, so we can keep it moving, because it's important for security has generally been agreed on. are there any questions on this PR 3360.
* Okay, we're gonna keep that moving. I'm not certain, I don't think it's gonna make it into the release like Tuesday, but it'll be in a subsequent release. Okay, great. Anything else on devnet?.  We're removing merge conditionals since Capella. 

## Remove merge conditionals since Capella Consensus-layer Call 109 #783 (comment) [42.15](https://youtu.be/Iy5zTJIXhQU?t=2535)
**Speaker: 13**
* Yes. So, in the tx we introduced some conditions checks to detective the merge, has been triggered or not, and I think this test are so, this test, this conditions are still in the top and then specs, but I think we have, again, very few benefits to different in the spec of status quo things. 
* They are just meaningless for the minute and both the future updates. So I wonder if we can just remove it from Capella. So it it will be, consensus change, but it should be compatible with mainnet. Yep. Any comments? 

**Danny** 
* Yeah, I think I'm the only one to speak out slightly against it in that it's nice in theory to be able to perform merges on other test nets at arbitrary forks post Capella. I think the actual use of that is probably minimal to zero. and there's been general agreement from client teams that keeping that complexity fork to fork, and managing that, especially in pads that we're really not testing much at all anymore is, yeah, means it's, it's much preferable to just remove from the spec, which would then remove it from various tests. 
* So yeah, I'm, I think I was the only one that was slightly against and, no one else agrees. So we'll move this forward unless others have want to chime in. Is Mario on the call? Mario Vega? do you know if we're doing hive tests on Capella and after on merge transition conditions? 

**Mario**
* Yeah, I don't, I don't see how this could break any of tests, but I really need to double check. yeah, I'm not sure. but we also want to remove the pretty much tests anyway, so, okay. Yeah. Mm-hmm. 

**Danny** 
* Okay. so this is in two PRs, 3232 and 3350. if you want to chime in before this moves forward, do so very soon. Great. Aditya, you're up next with the confirmation rule pr. 

## confirmation rule Confirmation Rule consensus-specs#3339 [45.30](https://youtu.be/Iy5zTJIXhQU?t=2730)
**Aditya**
* Hi everyone. this PR introduces a first confirmation rule in the spec. I'm pretty excited for this one because I think it's a milestone addition for ux. So at least from our current analysis, it looks like we should be able to confirm blocks within three to four slots. So under the minute on main net, the way this rule works is you input some safety thresholds. So, your assumptions about how many validators are byzantine, how many of them are willing to get slashed, stuff like that. And this rule outputs whether a certain block is confirmed or not. 
* And I guess there's, there's two main places we would use this in spec. One of them is the fork choice update to the execution layer. specifically the safe block hash. Earlier we used just the justified block route, but we can do much better now. it's gonna be much closer to the head of the chain. and the second place is, the Beacon api. This is stuff we haven't specified yet, still thinking about the best way to expose this, to CL users. So we can have a discussion about this now, but also we can wait, until people have read this and continue the discussion next time. 

**Danny** 
* Do we have, like when you on, on get block APIs on, the Beacon APIs, do we have some special keywords like head and finalized and justified? 

**Aditya**
* Yep. That's one place we could, we could insert confirmed. you also probably need to, set up your security parameters for it. so I think another place, we could do this in the Beacon API is the fork choice debugging endpoint. So it should not put the confirmation score for all the unfinalized blocks, so that way if you're running some kind of visualizer, you have the data readily available. 

**Danny** 
* And what's the, synchrony assumption here in addition to your, the safety threshold values? 

**Aditya**
* Right. The synchrony assumption is that, attestations are delivered in the same slot, which means everything that happened in a particular slot gets delivered to all the honest people by the end of it. 

**Danny** 
* Great. And before I take a deep look at this, what's your kind of estimation of complexity? Is this primarily just a lot of math, simple math, compute on values, or is there additional things that need to be stored and, and that beyond what we already have? 

**Aditya**
* I think it might take some effort to do this efficiently. for the most part it's using all the fork choice machinery. So Geth weight is being used, mostly, I can't see what a blocker for this would be, but it's mostly effort in, performance engineering. 

**Danny** 
* Okay. Yeah, thanks Aditya and others that have been working on this, this is really exciting. any questions for to chat? Okay, great. And while, we have one more issue, 3288 or PR I haven't opened up yet. can you give us a quick on this? 

**Speaker: 16**
* Yeah, this is a very simple change, which we do for the net. Please compatible, it'll allow participants to submit a valid or exit, which is valid indefinitely on the chain. Currently, if you submit an exit, well, if you produce an exit before off time, that exit is only vaild for two forks, and that's pretty value x for certain use cases, where you, where you may wanna present exits. 
* So what this would do is you will lock the epoch that you use for verifying the signature to Capella, allowing exits to be valid indefinitely. It's a very, again, it's a very simple change that has pretty nice UX benefits. So, I think this, this should be able to include it for the app. 

**Danny** 
* Does anyone else want away in here? 

**Speaker: 13**
* I think it's very close to the,BOS2 address change operation, so it makes sense to fix it as well. 

**Danny** 
* Sorry, the BOS change operation should be changed as well. 

**Speaker: 13**
* I mean, I mean, should be because the BOS address operation, the domain was also fixed. 

**Danny** 
* I see. 

**Speaker: 13**
* So I think these two are, I mean, they exist is also, one time operation. So it's fine to just, I mean I support BOS change.

**Danny** 
* Is the primary counter-argument that this was put in place to ensure that if there was some sort of sustained forking your messages across forks would not be re replayable, but that this is kind of a one-time operation and doesn't really affect your security too much. It's just an exit, but it doesn't really matter if there's replay. 

**Speaker: 16**
* If you asking me, I don't, I don't know. I don't have the history volumes here. If I had to wait, I would say it was just overlooked. 

**Mikhail**
* So even if such exit happens, you can deposit again on that report, right? 

**Danny** 
* Yeah, I don't know if it was overlooked, but I don't think the UX was considered too much about offline signing and having to bring additional information offline signing. okay. there's no tests on this PR who was, someone was gonna say something, Sorry. 

**Speaker: 13**
* I just want to chim in that, we do have, open PR on the deposited COI that we were discussing if, we can add the voluntary exceed operation feature. But right now it's sort of, stuck at the domain, the signing domain, like, to support, for offline signing, but also in the future upgrades. we have to upgrade the current version, sorry, the current folk version in every, protocol upgrades. So it doest the UX for and maintenance for the deposit tool. I mean the signing tool to me and for the test, I can fix it, after the call maybe tomorrow. 

**Danny** 
* Okay. Let's get tests in there and, our evolving process. So this should also have an accompanying EIP so we can track changes. so if we're gonna do this, we should open up an EIP with quick  justification that links to this, and get tests done and, get some thumbs up from various teams. After we do that.
* Tim, you wanna write the EIP If that's the blocker, I will you can circle back with, lion. I'm sure assistance would help keep this moving.
* Okay. anything else on deneb, on spec, on research? Anything else at all today?
* Okay. we have a lot of little things to do on all these PRs, that are going to be merged very soon. If you have any final comments or review on them, please, please do so now. we're aiming to never release early, mid this coming week, so that we can keep the test, test moving. Thank you everyone. Talk to you all soon. Thank you. Thank you. Thank. 


____

### Attendees
* Danny
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

