# Consensus Layer Call 100

### Meeting Date/Time: Thursday 2022/12/15 at 14:00 UTC
### Meeting Duration: 1 hour  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/688) 
### [Audio/Video of the meeting](https://youtu.be/UazJO0fQ3Ho) 
### Moderator: Danny Ryan
### Notes: Rory Arredondo

--------- 

## [Summary and quick contemporaneous notes from Ben Edgington](https://hackmd.io/@benjaminion/Bk9cIjuus)


## Intro


## [Goat Star](https://github.com/ethereum/pm/issues/688)

**Danny Ryan (1:50) -** Okay, welcome to the call. This is Consensus Layer Call 100, also known as ACDC 100 for those consensus. Issue 688 on the PM repo we have some Capella items, which is primarily our withdrawals upgrade and then 4844 items which is our add some data upgrade. This will be the last call of the year. We'll pick it up, I think it's the second week of January. Getting into it, there is a release was made yesterday in Consensus specs. This is named Goat Star. Check it out. I know a number of people were looking into test vectors and I believe there were a couple of problems or there were these tests vector release problems? I didn't get to catch up this morning or they were this little client issues or configuration issues? Hsiao-Wei or anybody familiar with this? Is Potuz on the call? Okay, well if we don't have anything to talk about on those, I will circle back with the (inaudible) people after and make sure that we're in a good spot. Anything else on this release? Pari wanted to discuss the what would be the first Shanghai testnet. I know there's been some withdrawals testnet but this will bring in kind of unification of the larger feature set. Pari?

## [Shanghai testnet](https://github.com/ethereum/pm/issues/688#issuecomment-1351488898)

**Pari (3:47) -** Yes. Hi. I've just posted a link in chat with what would I guess be spec for joining testnet. And there's a couple of discussion points there. But let's start with what what's already settled. So it's going to be a testnet that includes timestamp based forking withdrawals, one coinbase procedural limit and meta init code. The testnet will start post Genesis and the two spec versions for joining, so the EL spec as well as say the CL spec and the withdrawal spec version, or the commit has been listed in the document. There's a couple of discussion points. For example, what do we want included in the Engine API? Do we want a version release? Or do we not want to include it? We can start with that when it doesn't make our way down the list.

**Danny Ryan (4:43) -** There are a couple of things pending in the Engine API that could or could not go in. Lightclient or (inaudible) have any perspective on that. And if we can maybe cut a pre release on this soon

**Lightclient (4:59) -** I'm happy to kind of pre release. I'm sorry I haven't been keeping a close eye on been focused on the EOF stuff lately, but happy to redo some stuff today, tomorrow and make a release.

**Danny Ryan (5:24) -** Okay.

**Pari (5:26) -** So that would also include, I guess, EIP, sorry, PR 314, which is getpayloadV2.

**Danny Ryan (5:39) -** Hey somebody's not muted.

**Pari (5:44) -** Would that also include 314 which is getpayloadv2 and block value format. I know that it was posted about in the interop channel yesterday and I think it (inaudible) from Teku said he has no issue with it but it would be nice to get consensus from the other CL teams as well.

**Danny Ryan (6:09) -** The block value comes from the execution layer correct? That's a return value?

**Pari (6:14) -** Yes, as far as I know, Marek posted more verbose message about it last week.

**Danny Ryan (6:20) -** Ok. But there's this induces more work on their side than the consensus layer? Yes?

**Ben Edgington (6:28) -** I think Adrian's point was we could just stop that so that they return zero to us all the time just so that the plumbing is in place, but it doesn't involve actually returning the real value from the from the execution engine. So it would be work because they have to put the plumbing in but they don't need to do all the work.

**Danny Ryan (6:44) -** Understood. Yeah, I think this is a pretty important component. So I would I would like to see it get in there. I don't know if anyone else has an opinion to echo here. I guess the zero the zero is works fine because if you're not using MEV boost, then it will be the highest value thing and if you are using MEV boost, you would default to anything that came in from MEV boost as you already are today, so it's doesn't change anything until you get the actual value coming in.

**Arnetheduck (7:23) -** I think the earlier the better. And like, the zero idea for whoever doesn't have time to implement it.

**Danny Ryan (7:41) -** Okay, are there any? I'm not I'm calling this issue are there any like major unknowns other than the zero value being okay here and getting this merge?

**Marius Van Der Wijden (7:59) -** Can we just return the number value if we have already? 

**Danny Ryan (8:03) -** Certainly. 

**Marius Van Der Wijden (8:04) -** Okay. Then I'm fine.

**Danny Ryan (8:14) -** I'll circle back on this, see if Mikhail is around to do a final review and put this in whatever ends up being that pre release the next day or two.

**Pari (8:27) -** Awesome. The next one was PR 146 and PR 218. That's getpayload payload bodies method and getpayload bodies by rangev1. At least rough consensus seems to be the CL teams don't need this right now. So we could just leave it out, unless there's a contrarian opinion here?

**Danny Ryan (8:58) -** Okay, so yeah, the deduplication is being done by some clients through I believe the API. I potentially deduplication might be elevated as important with 4844 so maybe it's good to consider this in conjunction with 4844 and keep withdrawals.

**Pari (9:20) -** So shouldn't be important for this. The next one is we wanted to have just some consensus from the EL side, that the Genesis JSON has Shanghai time as the field just so everyone's using the same key, but doesn't really matter but just nice to have. And I guess a bigger discussion topic is do we want to include the fork ID logic or not? As far as I know Marius wrote up the EIP for that, but I'm not sure if the teams want to have it or not? For this testnet of course.

**Danny Ryan (10:00) -** I put it as a nice to have but we don't need to put it as a dependency here.

**Pari (10:12) -** Yeah, the remaining things are just aligning on validator set size. So Jim from a testnet vouch was seeing that spec limits sweep to a limit at 128k validators. So it probably makes sense to have a testnet that's bigger than that. So we can test this assumption.

**Danny Ryan (10:34) -** The limit is at 16,000.

**Pari (10:38) -** Okay, so is anyone has a preference on how big the testnet should be?

**Barnabas Busa (10:51) -** Larger than 60.

**Danny Ryan (10:56) -** Yeah. 

**Pari (11:00) -** I guess we'll just try to aim for the same size as Kintsugi so roughly like 100k validators and 50 to 60 nodes.

**Danny Ryan (11:08) -** To that end I would recommend once we do have a stable testnet to turn off 40% of the validators, 50% of the validators to put everyone into a leak such that balances go below 33 ETH across the board such that that maximum sweep does happen. That will be an interesting edge case that will be hard to hit on our public testnets and would maybe never be hit on mainnet but that we want to test.

**Pari (11:43) -** Okay, that should be doable. The next one is we're planning on just setting all validators is 0x0 withdrawal potentials at Genesis and then we just do the PLS change for how many of them we want to 0x or 1. The main limitation is that the Genesis tool right now can either do it's an either or so all validators at Genesis have to be 0x0 or 0x1 and it makes more sense to do 0x0. Does that okay?

**Danny Ryan (12:19) -** Yes, if we do in the future, it would be nice to have a test set that has some mixed but even managed shadow ports and stuff will do that by default. So 00 and being able to test the change operations makes sense.

**Pari (12:34) -** Perfect. And the last one is PLS change as an array versus individual. I know that there was some discussion on the Discord channel about this but I don't think there was a final decision.

**Danny Ryan (12:50) -** Array in what context?

**Pari (12:53) -** I will have to tag Barnabas on that one.

**Ben Edgington (12:55) -** This is on the API, I guess, right. We've been discussing whether we because the spec until recently has been you can pass just a single message chain execution credential change message to the API. And there's been a lot of discussion about being able to pass an array, largely because ETH do will output an array of JSON and then you can feed it straight in. And I think that's been adopted in the API spec now, but correct me if I'm wrong, but I think that has now been adopted as the standard so we should all have it at some point.

**Danny Ryan (13:27) -** I guess is the beacon API so that you can give a beacon node. The message to put into your mempool and gossiped? 

**Ben Edgington (13:36) -** Correct.

**Pari (13:41) -** I guess, has the API change been implemented any client yet? Or I guess there's also something not all plans have to align on right, like even if one client accepts it, it's enough.

**Gajinder (13:57) -** Yeah, Lodestar has implemented this change so our new mate will have it.

**Pari (14:03) -** Awesome, so we can just submit our arrays to Lodestar.

**Barnabas Busa (14:10) -** Because if you can also just submit it through the (inaudible) beacon. So even without any plans supported would work. 

**Ben Edgington (14:21) -** Yeah, that's correct. Teku Teku also supports an array now as well.

**Pari (14:26) -** So I think that's all the points about the testnet. I guess you guys can expect some more Genesis information etc later this week and we'll try and aim for Genesis sometime next week. Is there some timeline on when clients feel like they're more ready for this? Or do you think you guys think pre Christmas is okay?


## Spec Items 



**Danny Ryan (15:02) -** So the big thing was to get this sweep, bounded sweep feature in order, which I think I've seen a couple had already implemented before this has emerged and then there's PRs open across the board. So what's the status or is that going to be relatively done in the next few days it was longer? Does anyone think they can't hit a testnet build next week? Okay, let Pari know in the event when they're doing this if your client is not ready, but it sounds like I think we're generally a good spot. Okay, thank you, Pari. Thank you. I was moving on. There are a couple of spec items. These aren't necessarily Capella spec items. They're not related to withdrawals but they are items that could potentially go in here and there were a little bit in the late zone, but both of them are relatively small. The historical batch revamp proposed by Jacek, now over a year ago. Jacek can you give us the quick on this and discuss the kind of relative complexity here.


## [Historical batch revamps](https://github.com/ethereum/consensus-specs/pull/2649)


**Arnetheduck (16:50) -** Yeah, I think we had a brief discussion, like month ago and there were no real objections raised against the current version, but there weren't any strong supporters either, I'd say. Since then, I've had a few comments about it, which were which were supportive. The complexity is minimal. I'd say like the biggest impact is that we change the beacon state shape so if we want to stick this into the current test, it's kind of messy. Or we have to scramble. On the other hand, changing the logic is ridiculously simple because it just moves one history function to another place, more or less, or maybe something like this. I don't really know what else to say it's a good time to put it in there. It was a good time here. I think we've sorted out the complexity of the upgrade by saying that maybe we'll maybe we'll provide a backwards compatibility patch in the next hard fork or maybe not that this PR is completely independent of whether we want to do that or not. Other than that, it's it's a nice PR.

**Danny Ryan (18:25) -** Okay, so if this did go in, this would be a release in the next couple of weeks, and this would be an additional change that would go into testnets in January. It is very small. It has been pending. The remind me the primary is to just this reduces the proof length to get into either state or block or provides direct access?

**Arnetheduck (19:01) -** Yeah, so the the most important thing it does is that when you have a block, or rather than when you have a 1000 blocks and you want to be able to tell whether they belong to a state that you have or not. Currently, you need to compute the state routes. And you need to compute the state routes because we might have empty slots and those empty slots have unique state routes that are not present anywhere else in the protocol. So in order to verify blocks today that they belong to a state you have to basically run the state transition function and advance the state one by one on the off chance that you itd an empty slot. With this change, you can just take a dozen blocks, hash them together and you can verify that they belong to a state all the way back to Genesis. So this is great for you know, archive nodes that just store the data long term. They can quickly prove that a block was part of the state and therefore, they can decide to store the data and that alone without any more processing.

**Danny Ryan (20:33) -** Okay, I need some engineering perspective on getting this over the line.

**Ben Edgington (20:45) -** Think Teku view is slight caution about the unbounded state growth but it just on principle I mean it is small.

**Danny Ryan (20:57) -** Is that that's that's that exists today. 

**Ben Edgington (21:00) -** It does exist today. But yeah, it doesn't. I don't know if this adds more or if it's replaces the existing stay growth but just on principle caution about that. But I don't think we see any any difficulty in implementing it. And if we were to decide today to implement it, it could go into Shanghai Capella as far as we're concerned. We like the kind of two phase start the new scheme at the the upgrade and then later come back and potentially make it backward compatible by converting the existing state just freeze the existing for now and later in a further upgrade. Convert that to the new format. But yeah, decoupling that is good in our view. 

**Arnetheduck (21:43) -** So the state growth, the state growth today from the historical root fields is 10 kilobytes per year. After the change, it's 20 kilobytes per year. It's double because we store, yeah, both block root root and State Route route.

**Danny Ryan (22:07) -** Right and the, you know, this is what's called like a double batch Merkel accumulator, which is does grow unbound but very small and at least years ago decidable decided as find a way for the axises that it provides. But yes, I don't think it changes the fundamental assumption here by that 2x.

**Micah Zoltu (22:34) -** Is that 10 kilobytes/20 kilobytes, including all of the structure data, like, like in practice, it's 10 or 20 kilobytes or is it just in theory?

**Arnetheduck (22:43) -** In practice, I mean, there's a real relevant there are two relevant developments here, right? One is portal network and they will be very happy when this goes in. The every portal node that runs as a seed node needs to know that blocks belong to data to a chain that it's allowing onto the network so that we don't get spam. The other thing is that both Teku and Nimbus at least will start pruning blocks very soon. So the block history will not be available from the PTP anymore. As per the spec, what do we need to keep what is it five months of block data around? So since these features are going in having a way of verifying this archival data is is very nice, like there are other ways as well, but they're just more expensive, messy, slow and so on. So this is this is a cheap change for a nice enabling feature for those use cases.

**Danny Ryan (24:09) -** Yeah, I don't I don't want to block this given the we kind of wanted a year ago and we pushed it out. And I would kind of want to know, or more than kind of one out especially with the use cases here but so I'm leaving it to others to push back if this is not, should not go in now. Hsiao-Wei, on the order of what do you expect the kind of testing overhead to get this PR in order? Are you speaking I can't hear you. Can anyone Hsiao-Wei?

**Ben Edgington (25:06) -** No. Another mic down situation.

**Danny Ryan (25:29) -** Two days, she says. Right. Okay, then what we're going to do is spend some time the next five working days to kind of clean up the two days. Add the tests, ensure the existing tests work and circle around with client teams for final thumbs up. If we generally do I have any sense at that point. We'll put this in the next release and the January testnets. But we will give teams this next week to speak up if there's issues about complexity or anything else. Great I do have this next item also under Capella because I believe that's the spec that it's built off of right now. Although it could go anywhere depending on what's decided. So, Etan,there's, can you give us the download on this item, the EL block header versus the CL execution payload header fields and the issue at hand?


## [EL block header vs CL ExecutionPayloadHeader fields](https://github.com/ethereum/pm/issues/688#issuecomment-1346986847)


**Etan (Nimbus) (27:11) -** Yes, can you hear me? 

**Danny Ryan (27:15) -** Yes. 

**Etan (Nimbus) (27:16) -** Okay. So I just I have one slide I can try to put it in into the doesn't seem that it works. But I have linked it. So that's alright. In the execution layer, we have a structure called the block header. And in the consensus layer, we have a sort of matching structure called the execution payload header and most of the EL block header can be reconstructed from the execution payload header, that there are two fields that are encoded in a different way. And that's for the two fields where the CL keeps separate structures for the transactions and for the withdrawals and then puts them into a list because for those on the CL we have SSZ format, and on the execution layer, we have the hexary trie format. So use case here is for light clients such as wallets, smart contracts, if they want to, for example, prove that a certain transaction exists or that a certain withdrawal exists, they get the proof from the ETH API, the execution API, but they don't have the matching hexary trie root so they cannot verify those roots. Right now those two use cases are not that popular. The most popular one is using the statute which is luckily in the correct format, but we will have this problem every time there is a new field that is sort of a list so it's sort of important that we decide how we want to tackle them. And I see two options basically. One of them could be that we extend the Engine API, so that we get those hexary trie roots from the EL for transactions and withdrawals and also store them as part of the header the same way how we already store the stage we tend to receive through. Or the other way around that we change the EL so that it stores SSZ trie roots instead of the hexary trie roots for transactions and withdrawals. Both of these approaches would make the same data available in the same encoding for both EL and CL. And there are also some mixed approaches. For example, instead of exposing the hexary roots inside the execution payload header they could be recomputed by the CL. If they are not using split block storage, they still have to transactions and withdrawal. So technically they got they could reconstruct them. But overall the trend seems to be to move away from hexary tries and RLP format so it would be a big step backwards if we require every CL to support verifying and creating those legacy formats again, so yeah, that's what I wanted to bring up to discussion here. 

**Danny Ryan (30:58) -** And the light clients, essentially having proofs to enter the execution header, does that is that not sufficient?

**Etan (Nimbus) (31:12) -** Yes, but it doesn't like currently, the execution header cannot be reconstructed from the execution payload header. And what you'll get over the CL light client protocol is the execution payload header because that's the only thing that is signed by the sync committee. So if you only get that one, you would have to query the network a second time to get the EL block header and basically doubling the amount of network traffic by hitting the notes again, while before you could just follow the gossip and get the latest execution payload header like passively you don't need to request anything actively. And then other use cases. If you if you want to confirm that two execution payloads, or EL blocks, are part of the same linear history, you need to be able to compute their block hashes so that you can see that one of the block hashes is referred to by a different parent hash and right now you cannot verify those block hashes either. I mean, that's a minor problem because lightclient protocol trusts the sync committee, but it's another issue is is this used in different contexts.

**Danny Ryan (32:58) -** This is specifically this is to this adds two fields to the execution execution payload header and the execution payload. So they retain the same root, the same shape and

**Etan (Nimbus) (33:13) -** Or bytes to each block. It's about 150 megabytes a year of extra data.

**Danny Ryan (33:22) -** And the Engine API would need to respond but these two fields additional to the a couple of like the, the block hash that I think is also responded in there, you know. So it's a change both to the structure of the seal data and the Engine API, which puts a little bit of a requirement on the execution layer to return those but it has those values regardless.

**Etan (Nimbus) (33:58) -** Yes, getpayload would provide those two additional fields and new payload would then verify that the computed values match those that are provided. Or, alternatively, in the EL, we could also use the SSZ format and it would also be the same data in both versions.

**Danny Ryan (34:24) -** Which will be a much deeper change to the application layer tooling and other things that use this right?

**Etan (Nimbus) (34:32) -** I mean, as I said, transactions withdrawals, they are not the most important use cases because the challenge there is knowing if a transaction is actually in a block that's relevant for you, then we will have this exact same problem with every single array that is being added. So the change on the application would be that it needs to do the extra network to hit the network again, to fetch the EL block header. For like, a reason that's not really technical.

**Danny Ryan (35:17) -** Any input from teams on this both in the context of doing it in general and also doing it in the next upgrade?

**Ben Edgington (35:36) -** We decided which one we're doing, either to change the execution side to SSZ or change the Engine API to return these things? I wasn't clear that we're certain on what.

**Danny Ryan (35:52) -** My my intuition is it's a deeper rippling change change in the execution layer. But we will probably need more input there. I mean, my gut is that we're not in a place to make this decision for Capella. Even though it might be nice to have and that seems to be a deeper conversation across the layers to find the right solution here. But I am willing to hear otherwise. Where is this conversation happening? And where where's like a succinct place for it to happen? After this call?

**Etan (Nimbus) (36:51) -** The PR 3078 currently has the proposal to put it into the payload and I think that's the most canonical one to proceed discussions.


## 4844

## [Protocol upgrade name](https://github.com/ethereum/pm/issues/688#issuecomment-1351704592)


**Danny Ryan (37:08) -** Okay, and so far, seems like there's been some good back and forth between you and Alex, but not a lot of other input here. Just a couple of people. I think this is something to get right. We need to be talking to the execution layer as well. So it'd be good to get some input weighed in there and the next call early is not until January. So I think we should pick it up then. Okay, anything else on this one? 4844. Hsiao-Wei protocol upgrade name and suggestions. Your mic might not work. Okay. So seems to be generally agreed upon on All Core Devs and I believe, on this call, as well, that 4844 would be going into the next upgrade after Shanghai Capella, Shapella. We haven't unified naming yet. And 4844 right now is just a kind of like feature inside of the consensus specs, and it's probably time to begin constructing the next upgrade holistically as a set of features. So this would need a a name. We need to star name. We need to star name that starts with D. Proto did suggest Dubhe, D U B H E. This is my strong preference for the star name after Capella. It's the traditional/formal name of Alpha Ursae Majoris, also known as the Big Dipper and Great Bear, the ideal name to close, to Proto's opinion, a bear market. Last for the A and B names, I think we did a public poll for C. I put a placeholder and that seems to be the name. Hsiao-Wei, should we do a poll? Is this something you can do in the next couple of weeks? We can't hear you. I apologize. But if you speak in the chat, I will say what you say. Hsiao-Wei: "I feel that people generally agree, agreed to keep doing Devcon city names for EL and star names CL. But we might need to choose a better name to describe the hard fork when we're talking to the media." Right. Agreed, media and otherwise, I think in Tim Beiko's Magician thread, there's a number of proposals I believe on how to handle the fact that we have two names. There's some people or or someone trying to talk? Maybe smashing names together when the forks are but TBD. Barnabas, I do not know nor will I claim to have a good proposal, but in terms of what do we do when Devcon city names run up. Host more Devcons. But check out the Magician's thread I do think barring some great realization and change we will need a D name regardless. So let's maybe pop up a community call like we did in the past and anchor on that D name. Okay, so Hsiao-Wei: "Would like to check one are CL people happy with star name? With the specific star name or any ideas other than Dubhe, if not, I can see for community feedback after the call. Any other suggestions? Deneb is that a star name? Okay, Hsiao-Wei if you can handle, Łukasz?

**Łukasz Rozmej (41:53) -** Yes, it's a star name.

**Danny Ryan (41:55) -** Ok, well we have two contenders now. Hsiao-Wei if you can take charge on this one and figure out what this D name will be with the help of devs and community, that would be excellent.

**Barnabas Busa (42:08) -** Hey, is it just possible to have one instead of two?

**Danny Ryan (42:12) -** One star name or one name?

**Barnabas Busa (42:15) -** Yeah, just just one because right now it's also a bit confusing for the community that Shanghai and then there's a Cappella.

**Danny Ryan (42:22) -** Yea I don't want to.

**Marius Van Der Wijden (42:24) -** I would also like to go into what the (inaudible) between EL and CL. My suggestion would be to drop the EL name and only go with the CL names. But I think that's a discussion for a different day.

**Danny Ryan (42:43) -** Yeah, I would please ask you to check out the Magician's thread thread and if you have a proposal to, put it there. The fact that these things can upgrade and might upgrade independently is definitely argument to do names. Although often they might be upgraded together (inaudible) one name. Maybe there's a compromise here. Nonetheless, we do need something on our end. And let's keep moving forward with the stars until something else is yelled about on this Magician's thread.

**Arnetheduck (43:35) -** Thinking about that, did we decide what to do with the sharding fork? Because we do have some constant (inaudible) running something or at least we did a few weeks ago. And they happen to coincide with EIP 4844 in the first attempt which made a mess. Not not a big mess, a small mess.

**Danny Ryan (43:58) -** Are you talking about.

**Arnetheduck (44:01) -** Like sharding fork (inaudible) and something like this? 

**Danny Ryan (44:06) -** Right, which is would be kind of an experimental feature.

**Arnetheduck (44:13) -** Yeah, exactly. And it had like fork version four, which is pretty close.

**Danny Ryan (44:24) -** Everything placeholder and experimental and shouldn't have an impact on what we're doing here. But it would definitely that's kind of like 4844 and then it's just a feature name rather than a fork name. But do you have a puzzle on what to do with that kind of experimental feature name.

**Arnetheduck (44:43) -** We could just give them high versions. I mean, the thing that happens is that they end up in some databases and then when people upgrade and forget to wipe their databases you get like this funky errors whatever getting them. It's just a support issue. It's not a serious issue. It's just if they have like I versions 4844 could have as it's version 4844 until it's actually included somewhere. 

**Danny Ryan (45:17) -** Right. Particularly features that are not scheduled for forks shouldn't have certain configuration values that makes sure that they are not dangerous or conflict with real things in the future.

**Arnetheduck (45:33) -** Exactly.


## [DA on historic blocks](https://github.com/ethereum/consensus-specs/pull/3141)


**Danny Ryan (45:37) -** Yeah, I think that's pretty reasonable. Definitely on new features that are built out, we should be pushing that direction and we could do a revamp on this sharding feature, although I expect the whole thing would be will be reworked before it's actually utilized. And Hsiao-Wei says the sharding fork version was deleted from presets and configs. Which is also something we should be careful about just experimental things made into what end up being mainnet configurations. Okay, there's this issue that we want to make a decision on today. Data Availability on historic blocks, I think the name of the PRs consider old finalized data available question mark. I believe that the moderate consensus on this is to be on the pruning window. If you haven't already checked data availability on some block that you assume that is data available is false, would be the conclusion here. The this is certainly safer. This does not really change the safety or the UX assumption that it's not safe to be syncing from outside of a few weeks window due to recent activity. And I believe that this reduces the potential complexity here, certainly reduces it compared to having unbound window if things are not finalized. The alternative, two alternatives, is to have an unbound window if you're not finalizing, so you can do data availability checks, which has clear impact on node requirements and times of finality. And the alternative from there is to instead of assuming false, we assume true, which then does allow you to kind of switch between these branches but then has especially an edge case security scenarios, some issues where, for example, a malicious majority could potentially get you to switch after a time of no finality to a finalized chain that you then don't check date availability on which especially if you had collusion with an L2 or something that could have (inaudible) for security applications. I think one thing to note is that as 18 window, in almost all scenarios, we expect things weren't finalizing, it's because of some technical issue. Or even if not a technical issue, social consensus would likely jump in. So this is really like the edge case of the edge case where something could not be fixed. Or there could not be social consensus due to some reason and this window is so very important edge case but almost very unlikely to be seen in the wild. Micah?

**Micah Zoltu (49:24) -** It's missing something but isn't this thing you call an edge case? If an attacker attacks the network and is willing to just leak out because they felt the attack was more valuable, we will not step in to fix it. We wouldn't change anything. We would just let them leak out right for 18, however, however long it takes to leak out. Correct? 

**Danny Ryan (49:45) -** That does seem likely to be one of the more practical scenarios that are gonna happen. 

**Micah Zoltu (49:52) -** Yeah, so I think (inaudible) like that's the one we should be focusing on. Not the case where there's like a bug that we have to fix because like you said, in those cases, we just deal with that, you know, socially. Whereas if there actually is an attack we want to let the system self heal from it the way it's designed to. So I feel like that's the case we should be thinking about which I think is still okay in this case.

**Danny Ryan (50:14) -** Yeah. And to be clear, if your nodes online, you would on the branches that we were following have done data availability checks, you know, it's it's a matter of something, either you weren't online and are trying to check things past this value window, or something past that window adapt work is revealed past an 18 day window and known finality and you at that point would say, Well, I can't tell if that data is available. I wouldn't switch in the in the return false suggestion. I am think we should go with false. I would like to hear any opinions, else or otherwise. 

**Sean Anderson (51:19) -** I think false, may be the better option because this is such a like edge case in edge case. But I guess the other side of it would be like I don't really understand how you would like resync in this edge case? It seems like if any blocks past 18 days were unavailable if we're ever past 18 days with finality like I don't really understand what recovery would look like. So it seems like it might be more difficult. Yes, so weak subjectivity though isn't a checkpoint per weak subject to be always finalized. Like we we don't have a mechanism for like starting at an finalized point and populating like for choice backwards to finalize point. That makes sense. 

**Danny Ryan (52:15) -** Well, the the fine finality in that case, right because if I say this is this is certainly in my chronicle chain, regardless of whether any validators ever finalized in terms of like bringing in state in the block. That's essentially what you're telling the node is that this is finalized. So I would have met I'm not, Sean are you stating that if I say there was a final finality for two weeks, but I got a block from a week ago and I gave it a block and a state, and I said, Hey, this is my weak subjectivity checkpoint. Would that not be able to be processed into Lighthouse?

**Sean Anderson (52:58) -** I'm not sure maybe I announce that, see if it works. Yeah, I don't feel like against saying this is false. I'm just thinking that maybe whatever is simpler for recovering from this scenario is worth doing but I don't know. I haven't thought it through totally.

**Micah Zoltu (53:25) -** I wonder if clients should be internally tracking the block they were given as the trusted sync points as functionally final internally. Like even though it's not even if it's not final externally, like you would never rework past this thing that we didn't get from a trusted external source.

**Danny Ryan (53:41) -** I think that's, I mean, it's almost certainly what is done. Right? Pretty much the statement is this isn't my canonical chain.

**Micah Zoltu (53:54) -** I agree it's what should be done. It'd be good to verify that the clients are actually treating it that way. Because one can imagine you say, you give a block that's like, you know, very near head, like three blocks back or something like that. And you say, I want to sync to this chain. But then you connect up and maybe it's right around a fork or something like that. And you connect up and then your client decides, Oh, wait I see something else that's up here that everybody is saying is the right one, I should switch. Definitely not switch in that scenario.

**Danny Ryan (54:28) -** You're right in that it's unclear how clients would be defined in that scenario, because they would take that state that would potentially load what is read to be finalized from that state rather than loading that state into the finalities position.

**Arnetheduck (54:44) -** We keep a separate finality slot for what the checkpoints think. What checkpoints into user loaded, and we never revert that in any direction. Or rather we update it along that history but we would never switch and it's, I think we even put it in, you know, like the rest API queries. We don't respond with the finalized epoch from within the state field. But rather use (inaudible).

**Danny Ryan (55:18) -** Right. I'd argue is correct. Sorry go on.

**Arnetheduck (55:27) -** Yeah, just like the moment that you start your client with checkpoint sync. The checkpoint is what you get in all the API's, right? It's not. It's not the finalized epoch that exists in that checkpoint state, which is presumably usually like two epochs earlier.

**Micah Zoltu (55:51) -** This year, actually, when a user, it's the RPC, you're telling them. This is the finalized thing, even though consensus doesn't say it's finalized, but this client says it's finalized. Is that accurate?

**Danny Ryan (56:04) -** It's kind of like if you were at Genesis, you hadn't finalized anything past Genesis, you would say, Genesis is finalized, regardless of what that Genesis state said.

**Micah Zoltu (56:16) -** Right. It just means. 

**Danny Ryan (56:18) -** Negative numbers. It's not quite simple.

**Micah Zoltu (56:21) -** It means hypothetically, you could have two clients that are following the same chain they have the same head, but they disagree on what the finalized block is because one of them may have a full finality block they because they checkpoint sync whereas the other one has a finality block from two epochs prior and they would agree otherwise on everything. 

**Arnetheduck (56:48) -** Yes.


## [No blob available error code](https://github.com/ethereum/consensus-specs/pull/3154)

## Research, spec, etc. and Open Discussion/Closing Remark

**Danny Ryan (56:49) -** Yea it seems so. Okay, what I would like to do is get this merged, so that we at least have the edge case resolved and in the event that this induces some sort of terrible, terrible engineering costs, or unexpected UX issue beyond what we'e been discussing, then we can continue the conversation in January as this is kind of an edge case of edge cases. So we can spend a little bit of time resolving it, but I'd like to get something into the spec and I think false is the right thing to get into the spec at this point. Okay thank you. The no blob available response code, error code, resource unavailable, in the event that you're attempting to get blocks with blobs that are passed either finality depth, the greatest of finality depth 4844 fork block or the prune window. I believe this is generally kind of agreed upon on the 4844 calls and in the issue and discussion. Dapplion does have this up. It looks good to me. This will be merged soon, unless there is an issue. 
Okay cool. Great, anything else on 4844 for discussion today? Excellent. Any general discussion points on research specifications? Open discussions in general? Okay, thank you very much. Again, we will, quick look at my calendar. No All Core Devs next week, no Consensus Layer call on the 29th. All Core Devs starts on the fifth of January and we will be meeting on this call on the 12th of January. Keep an eye peeled for the Devnet 0, we will launch into the. What is Devnet 0 Barnabas?I

**Barnabas Busa (1:00:00) -** It's for withdrawals on internal devnet basically and I'm planning to finish it today. Because right now we have a very imbalanced validator set. So I just want to have a more balanced validator set and see if we can get it working before the public testnet launches.

**Danny Ryan (1:00:21) -** Cool. So keep an eye peeled for comms from Pari, Barnabas and otheres from the team on the Shanghai Capella testnet likely next week. Other than that, everyone have great holidays. Talk to y'all soon. 

### Attendees:
* Danny Ryan
* Micah Zoltu
* Rory Arredondo
* Sean Anderson
* Pooja Ranjan
* Marius Van Der Wijden
* Barnabas Busa
* Etan (Nimbus)
* Ben Edgington
* Enrico Del Fante (tbenr)
* Stokes
* Saulius Grigaitis | Grandine
* Arnetheduck
* Mario Vega
* Gajinder
* Pari
* Hsiao-Wei Wang
* Lightclient
* La Donna Higgins
* DB
* Mike Kim
* Trent
* Phil Ngo
* Zahary
* Stefan Bratanov
* Lion Dapplion
* FDF
* Tomasz K. Stanczak
* Robert Z
* Medi Aouadi
* Damian
* Kevaundray Wedderburn
* Daniel Lehrner

## Next meeting on
Jan 12, 2022, at 14:00 UTC
