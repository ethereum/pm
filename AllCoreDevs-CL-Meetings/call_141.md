# Consensus Layer Call 141

### Meeting Date/Time: Thursday 2024/9/5 at 14:00 UTC
### Meeting Duration: 1 hour
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1140) 
### [Audio/Video of the meeting](https://youtu.be/XMPupRyEBk0) 
### Moderator: Stokes
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
141.1  |**Pectra Devnet 2** Debugging efforts on Pectra Devnet 2 are nearing completion. Prysm developer Terence Tsao said that his team has resolved a non-finality bug identified on the devnet and they have not seen any issues with their client since. EF Developer Operations Engineer Parithosh Jayanthi said that with the Prysm bug fixed, Pectra Devnet 2 can be deprecated.
141.2  |**Pectra Devnet 2** Regarding Pectra Devnet 3, Jayanthi reiterated that not all client teams need to be ready with their implementations to launch the next devnet. The devnet can go live with a few implementations and the rest can be added later. Stokes noted that there are outstanding issues with EIP 7702 that may need to be addressed in execution layer (EL) clients before they can be added to the devnet. These issues will likely be unpacked in more detail on the next All Core Developers Execution (ACDE) call.
141.3  |**Pectra Specification Updates** The first was an update to EIP 7251. As explained on the last ACDC call, the update resolves an edge case where the correlation penalty applied to validators with a high amount of staked ETH is incorrectly computed. Stokes said that the fix is in its final call for review by developers and will be merged into Pectra CL specifications shortly.
141.4  |**Pectra Specification Updates** The second was an update to the Beacon block body to improve the efficiency by which CL clients can access and store certain components of the EL payload. The rationale for this update was also shared in more detail on the last ACDC call. Stokes confirmed that aside from a minor outstanding fix, this change to the Pectra CL specifications will be finalized and ready for implementation by CL clients.
141.5  |**Pectra Specification Updates** Third, Geth developer Felix Lange proposed a new strategy for improving the communication of validator withdrawals and consolidation requests from the EL to the CL. The issues regarding unnecessary overhead to EL and CL clients for parsing these requests have been raised on multiple calls. The initial proposal by Geth developer “Lightclient” was to unify all requests into a single list and leave it up to the CL parse. The proposal by Lange suggests encoding the data as “opaque hex bytes” like how transactions are encoded by the EL already. According to Lange, this would remove significant amounts of code from the EL and reduce complexity in CL clients. Stokes said that he generally agreed with Lange’s approach. Lange said that his proposal is contingent on a few changes that would require the buy-in from EL client teams. So, Lange said that he will resurface his ideas on the next ACDE call to get feedback from EL developers as well.
141.6  |**Pectra Specification Updates** Fourth, developers discussed the creation of a deposit requests queue as detailed by Teku developer Mikhail Kalinin. Currently, there is no rate limiting for validator deposits by the EL deposits smart contract. However, with the activation of EIP 6110, a queue may be necessary to avoid unnecessary load on CL clients in the event of a sudden spike in deposits activity. Kalinin added that the queue is important to prevent a frontrunning attack on withdrawals. With the addition of a queue, any new deposit requests must wait until all existing deposits have been processed. Nimbus developer Jacek Sieka wrote in the Zoom chat that the queue will also make deposit caching in CL clients “less error prone.” Based on the support for Kalinin’s design, Stokes said that the changes should be finalized “soon” and encouraged CL client team to chime in with any final thoughts posthaste.
141.7  |**Pectra Specification Updates** Finally, developers discussed various refinements of Ethereum’s networking layer based on EIP 7549, “Move committee index outside Attestation”. The refinements are detailed on GitHub here and here. Sieka, who authored the proposals, highlighted that these changes would offer an improvement to CL clients hash computation and bandwidth. Prysm developer “Potuz” expressed his support for the refinements, as did Teku developer Enrico Del Fante. Stokes said that developers should be ready to finalize these changes by the next ACDC call.
141.8  |**PeerDAS Devnet 2** The latest implementation of PeerDAS is being tested locally by clients, according to Jayanthi. Both the Lodestar and Nimbus teams are running a new Kurtosis configuration that spins up a private testnet. It does not appear that developers have yet launched PeerDAS Devnet 2, a multi-client, developer-focused testnet for PeerDAS. PeerDAS Devnet 2 is expected to be rebased on top of the Pectra upgrade, as opposed to Deneb. On the topic of stress testing PeerDAS implementations, Stokes recommended reutilizing the stress tests used for the Deneb upgrade on PeerDAS testnets that are rebased on Deneb and for future testnets that are rebased on Pectra, attempt increases to the blob count based on the design set forth in EIP 7742.
141.9  |**Research Discussion** Nimbus developer “Dustin” has created a proposal to remove all mentions of SSZ unions from CL specifications. This does not impact any client implementations as SSZ unions have never been used in CL clients. Dustin said that his motivation for proposing the removal is to better align CL specifications with existing CL client implementations. Stokes noted that the mentions of SSZ unions in the specifications were initially in reference to early sharding designs for the Beacon Chain. Given that these early designs have since been abandoned by developers, Stokes agreed that references to SSZ unions can be removed. However, he recommended that a note should be made in their place that points to where details about the use of SSZ unions in CL specifications can be found in case they are ever needed or useful again.

# Intro
**Stokes**
* So this is Consensus-layer Call 141 . Let me grab the agenda. I'll drop it in the zoom chat here. And yeah, there's quite a number of things on the agenda today. So let's just dive in. first up is Pectra, and we have Devnet two and three. I think mainly we're focusing on three at the moment. Is there anything we want to quickly address with Devnet two? 

**Parithosh**
* Yeah. I think Prism found a bug that they were tracing down last week with non finality. I don't know. I see Nishanth is just joining in, but I don't know if they want to talk about it quickly. 

**Terence**
* So the bug was fixed over the weekend. The PR was merged. The TLDR is that we had a basically we forgot to copy something. In this example, to validate the balance. So the state replay was wrong. But yeah it fits. And then. Yeah. So I haven't seen any issue since then. 

**Parithosh**
* Yep. so that's about it with Devnet two. I think at some point the explorer couldn't handle the non finality, so it's dead. So considering no one else is really debugging on it, I'd push for deleting the network today. Devnet three work is ongoing. there's a kurtosis config that I've pinned in the interop channel.
* I tested the nodes are able to stay with each other and special shout out and thanks to the testing team, because they were able to convert their tests into a format that I can run them against live devnet's and Mario's already created, as well as addressed, the failing test, with that in mind, and there is one more, failing test with Eragon that I've created a thread for, and everything is in interrupt, so please have a look there. And just a side note, I also tested consolidations, and the spec issue from the last dev has been fixed.
* So we have the first successful consolidation on a dev net with an effective balance over 32, which is really, really nice to see. yeah. And I guess the next question is adding more CLs to the mix. I've only gotten the CL branch and version to use from Nimbus as well as lighthouse, so it would be great if other client teams can just drop a message on interop as to which branch we should use, and we will expand our testing accordingly. once once we figured out the spec issues, I think with three clients, we're kind of okay to already launch that devnet three, unless there's some reason to hold off and launch that devnet three with all clients. 

**Stokes**
* Great. Thanks. yeah. Any other clients want to chime in on Devnet three? Readiness? It sounds like we could go ahead and kick it off. even if not everyone's ready. 

**Loadstar**
* Loadstar should be ready. So maybe unstable branch on nodestar devnet three can be used. 

**Parithosh**
* Awesome. And also, if client teams aren't ready at the launch, that's still fine. We can make deposits and add you guys later. So. Not that anyone feels left out. 

**Stokes**
* Anything else with Devnet three? Sounds like it's moving along pretty well. yeah, I know that on the EL side, there are some things with 7702. I don't know if it's worth touching on that now. Otherwise. We have a number of Prectra PR to discuss. Okay, let's move to that then. 

# EIP-7251: Update correlation penalty computation consensus-specs#3882 [5.21](https://youtu.be/XMPupRyEBk0?t=321)
* So first up we looked at this 1 or 2 calls ago, but it's essentially handing handling an edge case in the correlated penalty calculation with slashing. there was essentially an overflow with maxdb at high amounts of stake, and this PR fixes it. So this PR has been up for a little while now. It's 3882 on the consensus specs repo. 
* And yeah, I think it's pretty much ready to merge. we got a thumbs up from a few different people. So yeah, I guess this is, the final call. Anyone opposed to merging it? Okay. If your client team and you have a few minutes, please take a look. Otherwise, sometime later today or tomorrow, I'll go ahead and merge that in. 

# Moving requests out of execution_payload into beacon_block.body consensus-specs#3875 [6:15](https://youtu.be/XMPupRyEBk0?t=374)
* Next we have another PR. We also looked at this one in the past as well. So this was refactoring how the requests are structured in the beacon block. This is PR 3875. And yeah a number of people here have been working on this PR. I believe it's ready to go. So again last call. anyone think we should not merge this in. Okay. Mikhail says there's a small thing to be fixed. Okay. I can take a look. I'm not sure. Okay. Yeah, there's a comment here I see. Okay. I can take a look at this and, yeah, we can get that fixed. Otherwise, anyone opposed to, like, the general direction? There's been pretty good support so far. 
* So. Looks like we just fixed that thing and we are ready to go. 

# engine: unified list of opaque requests  execution-apis#577 [7:40](https://youtu.be/XMPupRyEBk0?t=460)
* Okay, next up then we have another PR to the execution APIs. So this one it's another pass at structuring the request, passing them from EL to CL. And essentially this is a slightly different approach. I forget the number, but there is the PR we've discussed before to essentially have the engine API structure in a way that the EL can just sort of copy paste the way they represent requests on their side, as they then are ferried across to the CL. This is a slightly different approach. And let's see, Felix, is that you that says yeah. 

**Felix**
* Yeah. So basically this the first one, the first PR, which you mentioned also the it was number 565. So there, Matt proposed the, this approach where we would just instead of returning the request as JSON as we do right now. And also it's. Oh, no, sorry. Instead of returning the request as like separate lists, we to the CL. So like one list per request type, we would just return the like unified list of all requests and leave it to the CL to actually figure like split them up into the types for inclusion into the CL block. 
* Because as far as I understand, inside of the CL block structure, the each request type has its own list. however, this was not universally liked because I don't know, it's just I think it has some problems on its own, like picking apart the request type from the JSON and so on is maybe not where I come in with my PR. 
* So I personally think that the purpose of the whole request mechanism in EIP 7685 is just that it should be generic, like these requests originate within the chain and their destination is the consensus layer. So ideally the execution layer would not really know anything about these requests. I mean, it has to extract them from the chain, but it doesn't even really have to know what's contained like the format of these requests. Unfortunately, right now it does have to know the format, because we have to convert the format within the L like three times. So actually two like. Yeah.
* So we have three different formats for these requests implemented within the L. And they are like specific to each request type. So it means we have to have a lot of code within the EL to handle three different types. 
* And I feel like it's unnecessary. And so an important observation we made is that for the newer types, for consolidation requests and withdrawal requests, the data which is returned by the contract is basically valid as Z. And it's not 100% valid as I'm working on a patch right now to the contracts to actually make it that. But, basically what they return could just be possible to CL directly, and would probably be more convenient for the CL to parse it like more convenient than parsing the JSON anyways.
* And the for the deposit contract obviously doesn't return valid CL because we kind of gathered the data from the logs and it's ABI encoded. But the transformation to like going from the log data to valid SZ is a very simple one, and it doesn't really require any kind of SSZ handling. It just means we have to shift the bytes to a different position, basically. And it's something that we can define and we have to do that anyways because we have to parse the ABI encoded data already. So I don't think we're it's not going to add code right now.
* So in total this change is if we go through with this, it's going to remove a significant amount of code from the ELS. And I also believe it will remove some complexity in the CLs. 

**Stokes**
* Cool. Thanks. Yeah, I've taken a look at these and generally agree with everything you're saying. this does simplify. I think both things on the EL and CL, which is really nice. yeah. Thoughts? 

**Felix**
* I have to note that it's all a bit contingent on a bunch of changes to EIPs which have not been made yet. So there's this is more me just proposing this general mechanism, but it has to be said that next week on ACDE, I will also be presenting the changes to all of the EIPs so that, yeah, I mean, it requires cooperation from the, EL developer group as well. 

**Stokes**
* Right? And to your point, there are changes, but they're not anything too massive. So, this seems like it simplifies things quite a bit with a pretty low lift. So, yeah, I mean, we will need EL nine as well. So I guess for now, any clues? Have you had a chance to take a look or have any thoughts about this approach? Any feedback? 

**Mark**
* I like it, but I'm just a little unclear on what the CL will be receiving like. I think it's a bit under specified at the moment. 

**Felix**
* Yeah. So there's no example in the spec. So the the pull request, has a long description, but it also has the content of the PR. So and in the content you can kind of see that literally. basically, at the moment in the current spec for Prague, for the engine API Prague, we return three separate lists, which are called deposit requests, withdrawal requests and consolidation requests. And these are arrays of JSON objects. So there's basically one array for every request type. And our change here is to return a single array called Requests and it will be in JSON array of hex strings.
* And these hex strings will then contain the encoded requests. And the encoded requests have a single request type byte in the beginning. So it's like a zero, 1 or 2. And as the first byte. And then the remaining bytes will just be the SSD structure of the request. And this structure is defined in the CL specification. So it's identical to what is already defined for these request types within the consensus layer specs. It's yeah I agree we could specify more. 

**Mark**
* Well I don't know that the byte the distinguishing byte is specified. Right. That that's new right. Or am I wrong? 

**Felix**
* I mean, yeah, it's kind of I mean, it is if you look into the into the PR, you kind of see that. Yeah. I mean it has, it has this array of. Yeah, I mean, I guess I should know. 

**Mark**
* I mean, I'm just clarifying. 

**Stokes**
* So that this vibe comes from the different EIPs, and again, I forget the number, but lightclient also had a PR that basically gives sort of a general structure for this request type and request data. So Felix is saying is the request data is essentially SSZ. You would just cut off the first byte, deserialize the remainder and you're good to go. 

**Felix**
* Yeah I mean I don't want to say the word, but I mean this is like a union basically. I mean, so the main thing is that it's not a we were debating if it makes. But I mean, since the union was being removed, we didn't want to call it the union. But I mean, honestly, we gotta put this information somewhere for the CL to distinguish the request. And yeah. So basically that's why it's has this bite. We it I want to note that we have we have this bite already in the EL level encoding. So at the moment in the current specs for the EL, we do use this type of encoding with the with the initial bite for the request type.
* And it's in all the EIPs. It's just that with this change the CL will have to handle that as well. Anyway, I'm happy to answer a question from Potuz's right now. 

**Potuz**
* Yeah, it's just a comment. It's the same comment that I that that I told Matt. so it seems that someone would have to do this, this work, which is, we have this list of, requests and each request, we need to put it in a bucket. And what you're suggesting now is to to send this list with this extra data that we don't care about, or we only care about to to deciding which bucket we're going to put it, and then the CL needs to arrange these things in different buckets and then get the corresponding SSZ object, which is the list of requests that we care about.
* On the other hand, the same work could be done by the EL. You could in principle send a list of lists to a list of list of hex strings which is ordered, and then you put all the request type one first, then all the request type two then. And it's exactly the same work that you would be doing. Or we would be doing without having this, this byte that it's non-existent today in the CL. So again, I don't really oppose I don't have any any strong opinion as to who should be doing this work. It's just that it's clear that this work has to be done by either the CL if you give us if you give it as one list, we will make this nested list of lists.
* Or if you give us a nested list of lists, then we can already consume it and the same amount of work on one or the other one. So I don't really see why the push to have this, this separation of the first bite on the SQL side when you can because it's way easier. A simple change it is. 

**Felix**
* It is way easier for us though, because then it just means that we don't have to care about basically in EL implementation, it means when we are processing block, we will just go through the system calls, append it all to a list, and then just basically send it off to the to the to the CL. We don't have to think. And I think this is quite important for me because this mechanism is like defined for the benefit of the of the consensus layer. Like the execution layer does not care about these requests at all, and it should not really have to think about it too hard.
* So from my point of view, it makes more sense for us like this. It kind of sidesteps a bunch of these issues as well that were mentioned in the earlier PR. This is kind of where we're I don't want to get too deep into this discussion because there were a bunch of things like, yeah, can't you do it like this or whatever? This is not I mean, we've come up with this approach because we think it will be something that is the easiest to implement for everyone. Like mostly for the ELs and splitting it in into the separate lists for the purpose of putting it in the beacon block. I think it's okay to have the CL do it, in my view. 

**Potuz**
* I also think it's not that much of a work for us. I think the, the biggest complaint concern that, that, Dustin from, from, from Nimbus had was that eventually if we moved to having Z, then this list that you're proposing will have to be encoded in a Away, and it would be very different if you had a list of lists, if you had a list of lists is something that we can handle it today with our, as I said, libraries. But if you only have one list, we would have to come up with this new type, which either is a necessary union or whatever, whatever new type is. And it's just going to be a list of. 

**Felix**
* I mean, it's just going to be a list of, of like byte vectors or something. I think honestly, that's basically what it's going to be. I mean, it is kind of a list of byte vectors right now in the JSON here. So I don't think it's going to be inherently a problem to. Oh, so. 

**Potuz**
* You're suggesting that we take it as a list of byte slices. Yeah. That's, that's a that actually would work if, if the object that you would be sending is not going to be the user object that we expect. that that should be fine for us. Yeah. 

**Felix**
* So basically the whole proposal is just sending like an array of like bytes objects. We encode them as hex because it's a JSON RPC. But then basically. Yeah. So I mean, if we ever convert this stuff into a set, and I don't know, this will be handled in some way. I mean, we handle this. It's the same for transactions right now. I mean, for transactions, we send these like opaque hex objects and they have the first byte containing the transaction type. And then the remainder is this data, which is totally opaque and specific to the type. And I mean, it's you could say it's a kind of union, but honestly it's just because, you know, that's what you got to know which object it is.
*  And I don't know. Yeah. This like list of listing it has some disadvantages as well. It's yeah. I mean, let's see. Okay. How about this. We won't really make the final decision today. Anyways, next week is actually is ACDE I will be presenting this change also there from the perspective of the ELs. I guess you will also be there. assuming and then you can listen in again and think again. And I mean yeah, that's it doesn't have to be decided today. I really just wanted to bring it up. 

**Dustin**
* It's interesting for sure. I would note one difference from the transaction case is the sales mostly don't care about the details of transactions. I mean, I can't speak for every obviously, case here, but generally speaking, transactions are a black box. So whatever, you know, union like structure they might have internally is is typically not that relevant for this purpose. I mean, beyond what whatever the E:s want to do with that. And but the but but it has no bearing. The engine API aspect has no bearing on this one way or the other. But in any case, that said, this is definitely an interesting, proposal. 

**Stokes**
* Yeah. And to Felix's point, the requests are kind of black box for the EL, so it's just kind of the inverse here. So. Yeah Thanks, Felix. everyone, please take a look. And it sounds like we will touch on it next ACDE. Cool.

# eip6110: Queue deposit requests and apply them during epoch processing consensus-specs#3818 [22:45](https://youtu.be/XMPupRyEBk0?t=1365)
**Stokes**
* So the next thing we had on the agenda was PR 3818. So let's throw a spot in the chat. There we go. There's a link in the chat. And so this PR is kind of big but it's important. It's a follow up to 6110. I think the core issue really, as far as I see, is that there's no sort of rate limiting in the deposit contract just because of how it's written. And so what that means is that there could be a necessary load on the CL or like unacceptable load on the CL if someone went and made a bunch of deposits, say, in one block with the request structure under 6010, and this PR essentially adds some queuing to mitigate any issues with too much load. And yeah, Mikhail, I think you're here. Would you like to say more? 

**Mikhail**
* Yeah. Quick overview. this was kind of, while there, opened, we were working on tests, so now it's kind of ready to get merged from the testing perspective as a good test coverage. yeah. The overview of changes is, as Alex said, it limits the deposit processing per epoch to set it to 16, which actually the purpose of that is to limit the signature verification operations. also, for the transition from Eth1 bridge, for the Eth1 bridge deprecation. This. This queue is also important because it allows to prevent the front run attack, where the raw credentials can be front end, by the new deposit requests. So it actually sets the strict order of, the deposits being processed.
* So the first, yeah, the new deposit request will be, will wait for until the Eth1 bridge deposits are fully processed that established this strict order and prevents the front run attack. And, yeah, there are some other things, like finalizing deposit requests position before applying the deposit. we have been discussing that this is not super important. but just nice to have since we introduced the queue, it would be nice to have this functionality as well. and one thing I would like to pay attention to is the switch to compounding validator call, which is introduced by max effective balance increase.
*  And yeah, there is the new feature where one can top up its validator and switch to compounding credentials this operation requires signature verification.
*  So the signature should be valid in order to do the switch And this PR actually moves this switch to compound into process deposit request, which actually means that every deposit request, yeah, that has this operation is not going to be is to be like on top of the limit of, signature verification that we have for epoch processing. 
* So it's kind of like not rate limited. And if we think about it, probably it's not that bad. The purpose why it's done this way is just because somebody will have to wait for the entire deposit. If it's large enough to switch to compounding credentials, which is kind of like not that good UX, but probably it's not. Yeah. If we highly want to also make the signature verification, put it under the limit that we have for processing, or this operation, then we can move it to the queue as well. I mean, the switch to compounding operation. So that's probably one thing, that is questionable with respect to the design proposed by this PR. 

**Stokes**
* Thanks. so this came out ofLot of discussion at interop. although we were already getting some plus ones in the chat. anyone have any questions? Around this PR? Okay. I mean, it does seem like we need the rate limiting for the deposits for the request, so. Yeah, I looked at the some and I think this is pretty much the cleanest solution. yeah, I guess it'd be nice. CL teams, if you could approve the PR just to give it a thumbs up. But I guess we can take these in the chat as a signal, and. Yeah. Otherwise, we'll look to merge this pretty soon. I guess one question I know we had discussed having, like more sophisticated queue management sort of downstream to this PR. Are we still thinking that that's useful? Desirable? 

**Mikhail**
* Yeah. The main the main reason for that was the performance. So probably it's still important. 

**Stokes**
* Yeah. I wonder if this is a thing where we can just actually get numbers on the next devnet and see how it shapes up. That was definitely everyone's intuition that there would be a bottleneck there. but that all being said, if we do want to do that, it'd be nice to do it sooner rather than later, just so we can get the core stuff stable. Okay. Cool. 

# Temperature check on further attestation refinement: Separate type for onchain attestation aggregates consensus-specs#3787, Separate type for unaggregated network attestations consensus-specs#3900 [29:39](https://youtu.be/XMPupRyEBk0?t=1779)
**Stokes**
* So yeah, take a look at that and then I'll move on to the next agenda item. So let's see that one. Okay I did want to get a temperature check. So again there were there's another stream of PRS um to further work with the attestation refinement that we have. Let me just grab links here. So there was this first 13787 and this next one. And they essentially just rework the attestation types in various places, with the claim being that it's just simpler and easier for clients to manage things, whether that's attestations from the network, attestations on chain. They've kind of been sitting for a little while.
* Has anyone had a chance here to look at them? And yeah, again, I'm kind of I'd like to get to a place where again, these like core EIPs are pretty final sooner rather than later. So I'd like to push these along if we're serious about these pills. 

**Atd**
* I mean, I can just say two words about them. the first one now, there are there were also discussed at interrupt where they're coming from. And basically, the EIP that they reference, they kind of introduced a refactoring of the attestation type. And then piggybacked that refactoring onto the network types that could actually have remained the same. so what one of them does is retain the old format for, aggregates on the network. And then this gets translated into a new type for the on chain thing for the on chain attestation. And we have to do this work anyway. So like the format there doesn't really matter. but for the network it's easy.
*  It's like more secure to use the previous type because it's more tightly defined to match what, what's going on the network, with the committee size. then the second part is actually even more interesting from a security perspective, because it allows validating the signature of the attestation before computing a shuffling. and this is actually one of the bigger selling points of this PR. what happens right now is that you can just connect a client and maintain good reputation with your peers. And then when you want to introduce some instability in your in your neighbors, you just send them an attestation for which they don't have a shuffling.
*  And there is no signature check on single vote attestations that is possible without performing, without computing the shuffling. And as any client that knows, like computing, shuffling is very expensive. So clients have a few options and they're all bad. one is dropping the attestation and just kind of dumb because this typically happens, when the network is, not very stable. 
* That's the best time to exploit this thing. And dropping attestations at that point, just like delays getting back to, nice, stable finality, they can kind of process them. And this eats up Resources for computing the shuffling and then for holding. Lots of shuffling in memory, which can typically do. and they can delay processing it, which is also bad because it introduces these cascading delays in the propagation. So, the PR kind of narrows doesn't eliminate this possibility that you'll have to compute a shuffling, but it narrows it down. So the only validators, can cause others to have to propose to compute shuffling. And this is definitely an improvement versus, you know, just any random on the network being able to do this.
*  I like them, and they're certainly simplifying the Nimbus code base when we implemented them. So. Or when I implemented them. I'm kind of hoping that this story will be the same for the other CLs. 

**Stokes**
* Cool, thanks. Has any other CL team had a chance to look at these?  Potuz? 

**Potuz**
* Yeah. Just repeating what is in the chat. We've looked into this. It seems to me that it's trivial to implement, but last time that we dealt with it attestations and we said the same thing. Well, we know we are where we are. This one does seem to be much simpler, because it's only a little change on the subscriber and on the P2P side. I like the change. I'm in favor of that. 

**Stokes**
* I mean, timing is hard, but, like, if we could get to a place where we feel like these are ready to merge by the next CL call, that'd be really nice. otherwise, yeah. Client teams, please take a look and chime in on the PRS, and. Yeah, I'll do what I can to move these along, and yeah, we'll get that get that sorted. Okay, so that was it for Pectra before we moved to PeerDAS. Are there any other Pectra things we want to touch on? Okay. PeerDAS then, I could start by asking for any implementation updates. I think we are looking at. Let's see. PeerDAS Devnet two. But I don't think it's live yet. anything anyone would like to share on that front. 

**Parithosh**
* Yeah, just a brief local testing upgrade update. There's a pinned Kurtosis config if someone wants to try it out. There are three supernodes as well as three like normal nodes in the config that seems to be going well. I think Lodestar said that they would try it out locally and get back if it works, and Nimbus will get back to us on Monday with potentially something that works. 

**Stokes**
* Okay, awesome. So things are moving along there. great. 

**Parithosh**
* So I guess one quick question I had on the topic. Is there some way to actually stress this thing? Because, I mean, right now it's just it's running, but it's not doing much else, I guess, besides blobs. 

**Stokes**
* Right. and it's still on Denenr, right? 

**Parithosh**
* Yeah. And the rebase on top of Pectra is for the next fork for the next. 

**Stokes**
* Right. Yeah. I mean, one option would be to, like, run our stress testing on the PeerDAS devnet just to see what happens. Otherwise, I mean, we could try bumping up the blob count. 

**Parithosh**
* Yeah. Sounds good. Yeah. 

**Stokes**
* Which actually does call to mind. But go ahead. 

**Parithosh**
* Yeah. I think we kind of having the same thought. How do we increase the blob count? 

**Stokes**
* Yeah. Well, and I was going to ask about 7742. the PR to the various specs are all still open. I wasn't sure. It might have been discussed on the breakout this week. but I guess if clients have that, it does help simplify raising the limits. Okay. is coordination for this mainly in the PeerDAS testing channel? On the R&D discord, Perry. 

**Parithosh**
* Yeah, exactly. 

# PeerDAS: move cell computation during local block building into the EL? [38:49](https://youtu.be/XMPupRyEBk0?t=2329)
**Stokes**
* Okay. So, yeah, we can just take it there and we'll push this along. Async. Cool. So thanks everyone for that. Next up. So this question came up from the breakout. And essentially I think even already we've seen some problems around computing the PeerDAS proofs. especially if you have like a sort of under-resourced node or a low resource node. I think you can take something like up to a second, and maybe even a little bit more to compute all the proofs that we need. and especially as we move to like a higher blob count. So like, for example, I think there's even discussion of, say, 1632 as like a target and max limit for us. That's great because then we have more data throughput.
* But if it's going to take so much longer to make these proofs on the CL, then we have an issue, because let's say you build up until pretty much your proposal deadline and then it takes you another, you know, second plus of blocking work to actually get the block out. So this came up and yeah, let's see I have a link here to the docs notes with PeerDAS little more context. But there was a question around how to handle this. there are a few different options. I don't have the link, but, Amazon actually had like a nice summary somewhere on the discord. And some of this will be dependent on what the ELs want to do. Let's see if I can remember the options here. I mean, the first one is just keep it as is.
* You can imagine maybe the validator then knows and the CL to like start block building or like when it goes to fetch the block that's been built, it does that a little bit earlier to offer time. 
* Another idea would be to move this proof generation to the EL just sort of like to pipeline it, and then we gain some, you know, time there. This is kind of a violation. Well, it's definitely a violation of separation of concerns between the EL and CL, which is not nice even if it is, say like a pretty straightforward option. So that then takes us up to a third proposal, which is essentially to have like richer communication between CL and EL so that, you know, one way to think about this is like, the EL would essentially post to the CL through the engine API for every blob.
* The CL can then start working on these proofs in parallel to the build on process. and then we go about it that way. So that was this sort of high level overview of the problem and some of the solutions that have been proposed.
* Does anyone here have any contacts I'd like to add or do any of these feel like promising path forward for PeerDAS right now? Sean. 

**Sean**
* Yeah. So I talked to Jimmy about this yesterday. He said this, change that Michael's proposed to allow the CL to get blobs from the ELs mempool could help to some degree. this is because you can. You don't have to wait on blobs over gossip, necessarily, if you already have them in your mempool. So it's kind of an optimization there. Another thing we talked about was, and I don't know the exact details of this, but like another more, I guess radical option is to have like a decentralized sort of, proof generation. So, like, have nodes across the network generate proofs with some sort of like, responsibility, division. But yeah, again I don't know too much the details there that's just another option we talked about. I think that's it. 

**Stokes**
* Cool. Yeah. I mean, the thing is, I think you still need to make the proofs in any case, because, like one, you won't know for some, you know, remote peer what they have in their mempool. so you'd always need to do this. And then the issue is, say you're the home staker with like, only a little bit of hardware with this problem. then you're kind of hosed. So. Yeah, I think we need to do something. the question then, is what? 

**Dankrad Feist**
* I mean, I think, like, we should. Definitely push harder on the distributed building. I think, like, that's the most sustainable solution anyway. And like, if you have such low resources, it's also likely that your bandwidth is low. So like you'll struggle sending out those proofs anyway. So like in almost all cases, your best strategy will be to send out your block first and, bet on other people adding those proofs, which we can definitely do. Like if they're in the pool, then like accelerate things. and I think like otherwise I would. Yeah. I really don't want proof generation to leak into the execution layer because, like, we're currently trying to decouple data availability more from the execution layer.
* Like that's why, for example, we also want to, have the block limit only in the CL rather than having it set in both the CL and the EL. And I think like in that context, it only makes sense if we make sure that, like all the proof generation logic is also in the CL, because further upgrades to data availability will require us changing that. Again like we will want more samples, we want a different type of samples, for example 2D samples and so on. And we want to make those upgrades without having to change the EL as well.
* So yeah, I mean, I do think like we should find a reasonable way of like getting the blobs into the CL so that it can generate the proofs, but I think like the actually more promising avenue for home Stakers will be getting other nodes to generate the proofs for them.
* And I think like, yeah, there are many things that can be done about that. 

**Stokes**
* Right. Yeah, that makes sense. And I think this is a good point about not having things leak into the EL, because as you say down the road, it'll only get more complicated. So cool. George, put this link in the discord. So yeah, take a look there. And I guess for now, just consider this, open question we should all be thinking about. And, yeah, otherwise, I think we'll just keep thinking about this. Okay. Anything else for PeerDAS 

**Dustin**
* So I do have a question about this. I guess I'm reading the notes and it I mean it from linked here. For example, the breakout room notes is that it can take up to one second, kind of under what circumstances or what kind of hardware kind of concretely, is we're talking about running a Raspberry Pi or a I mean, an average laptop or Yeah. 

**Dankrad Feist**
* An x86 CPU that takes like 2 to 250 milliseconds to generate one proof per, like on one core. So, for example, if you had 32 proofs and four cores, then it would take two seconds. each core would generate eight. So yeah, it depends on like both the numbers of blobs we include and how many cores of what type you have. And Raspberry Pi is going to be more of a problem because that, they are even like it takes one second to generate all the proofs on one core. like ARM is just a bit slower at the moment. And I think, but I don't feel like Raspberry Pi is currently really like a common choice for stakers. Like, I think like that was like our target five years ago.
* And like, I think, we've probably moved on from that. And we have like slightly more powerful to bigger devices now. Like it feels even hard to get less than four cores nowadays. 

**Dustin**
* Sure. No, I mean, yeah, that I don't I don't mean to push particularly seriously the idea of like it must run on Raspberry Pi, but just as a getting a sense of, what? The sort of quantitatively what the numbers here were, whether we're talking about on like a relatively home servers or whether and you had had to be. Yeah. 

**Dankrad Feist**
* On a home server, like with like 16 cores, say, like you could easily get it done in a very short time, like. 

**Dustin**
* Yeah. Okay. So so this is, so this this is more of a case or as, as, as Justin posted the, like the rock file because that is that's actually a better benchmark here because the from a numbers perspective, it's not clear that the Raspberry Pi is a super viable today as a reliable node. although people might try. People do try. but the Rock five is that's definitely a yeah I agree. 

**Dankrad Feist**
* I agree and I think that is what we should. I feel like that is what we should be looking at at the lower end of the nodes. At the moment, I think Raspberry Pi is starting to look unrealistic? 

**Dustin**
* No, I make sense. 

**Nishant**
* So I just want to add that, you know, outside of benchmarks in mainnet you the node will be doing a lot of other things rather than just computing cell proofs. So whatever benchmark you do get, you know, the actual number if you're running this on main net would be higher. 

**Stokes**
* Ansgar. 

**Ansgar**
* Yeah. Just wanted to say that, as I said in chat just now, that like one super obvious thing is that the failure modes are quite different depending on how we approach this. So if we basically do the dumb thing and just have the CL compute the proofs after the block is requested from the EL, then that adds delay to the critical path. And that means that. basically, if there's any kind of issue or it takes too long, then then that means the block just won't make it in time to and will basically be angled, which is quite unfortunate and pretty bad for the case. Whereas if you were to just do it in parallel with block production.
* So if the ELs had some way to initiate the kind of proof generation while it's assembling a block, and it basically ignores block transactions until the proofs are finished for them, then basically the failure mode is much more graceful because then it would just mean that as a weak node, then maybe you just don't have all the proofs in time, and you you have to ignore some of the block transactions. And so you can't you may be missing out on some super like long tail of the of the fees, but otherwise your block is completely unaffected and the timing is completely unaffected. So I personally would very much recommend we don't do this thing of generating the proofs on the critical path. 

**Stokes**
* Yeah, it makes sense. A question I have with this sort of I mean, I think first we just have to spec out what we mean with like decentralized proof gin a little bit more. one thing is, let's say you have, you know, your rock sitting there, you push out your block with, you know, commitments to the blobs. You rely on someone else to make the proofs for you. Is there any concern there? I feel like that would be like the first problem we'd run into where if I just get a block, I don't exactly know the rest of the context of the block. maybe it's fine, but I'm not sure if anyone's thought about this. 

**Nishant**
* Well, there is no doubt concern. It's just, repeated work across all the super nodes in the network. So if you have the commitments from the block, you can look at your local mempool. And if you have the blobs, you know, you just create the self proofs from that. The issue. Doing it this way is that, yeah, it's in the critical path. 

**Stokes**
* But what if you don't have the blobs though? 

**Nishant**
* Then you can't do anything. You're stuck. 

**Dankrad Feist**
* Yeah. You do assume that some super node has all the nodes. Otherwise it doesn't work because currently you can't create any proofs if you don't have all the proofs. 

**Stokes**
* Right. Okay. 

**Dankrad Feist**
* I mean, one of the ideas here would be to give us better channels to notify the super nodes that they would do some work. Like, I don't think like many people running these would find it a problem because we are talking about donating a few seconds of CPU time and like there's no extra load from distributing these because you would be doing that as part of P2P anyway. So like if we have like a nice mechanism. So like one of the ideas would be what if we could, broadcast, like, block headers before we broadcast the block?
* Like, that could be much faster, and they would get a heads up and then, like, they could just do this, and possibly they would, like, even come fast enough that it would still be faster than actually sending everything. and like, I guess a more advanced version would be if Homestake has, like, announced, in the slot before that they won't be able to build, the, the, the proofs and basically asking the super nodes, hey, like, could you pre-compute it for the ones that you see in the mempool now? Like, it wouldn't be impossible to do this. but I mean, I guess like it would require more messaging because now you need a signed message from that, from the validator saying, hey, I want these proofs built. 

**Stokes**
* Right. And we do advertise. Like you could just walk the DHT to find Supernodes, right? Because that just means you have, like, all of your bits set for your custody channels. That would be the way to identify them. 

**Dankrad Feist**
* Right? I mean, I was assuming we just do it through like a gossip sub topic. but yeah, I mean, I guess you could because, like, I mean, this is very low bandwidth, right? It would only be like one tiny message per slot. but yeah, I guess you could also do it by directly contacting them. 

**Stokes**
* That's what I was thinking. But yeah, I guess you could possibly do both. cool. I mean, another. 

**Dankrad Feist**
* Way of doing this would be asking the relays to do that. It's a bit of a weird thing because you're not actually using relays in your self-builder. but, like, it could still be a service that they provide where they simply have an endpoint like, send me your blog header and I will create your proofs and send them out on peer to peer. Right. Like it would still be trivial for them to do that. And I think like if you added that to the software, they would do it. But, it's slightly weird that I. 

**Stokes**
* Yeah. Do you think there'd be any incentivization there? Like, would the proposer pay the relay or, you know, assume there's no. 

**Dankrad Feist**
* I mean, I feel like it's I feel like it's one of those things where, like, the value would be so tiny that it's really, like, not even worth paying for it. Like the the relay does most of the work by simply like the implementation is most of the work actually doing it is so trivial. It's like, how do you even pay for that? It's like worth a million or something. 

**Stokes**
* Right? Okay. 

**Dustin**
* Does this require that kind of 

**Stokes**
* Yeah. Go ahead Dustin. 

**Dustin**
* All right. Does this require that kind of infrastructure in, Devnets testnets. And because we don't. The VRA infrastructure has historically taken sometimes a little while to come online. just, I mean, once the network is running and and mainnet forks, it's it's unproblematic, but, even the first testnet sometimes doesn't have it have everything ready there. 

**Dankrad Feist**
* Right, right. I guess that is the advantage if we solve it internally. like, as part of the node software, then we don't have this external dependency. Is that like, are people keen to build this distributed thing and find some way of notifying the supernodes, then we could maybe create a group and talk about a spec for this and do it. It doesn't feel to me like it's super complicated. We just need to like, agree on something and do it. 

**Nishant**
* I mean, an easier solution would be just to have the EL communicate, which exact block transactions it has, in its current payload, it's building, and the CL could just build them in parallel. We don't need to have a separate channel for all this stuff. 

**Dankrad Feist**
* You're saying like your. I guess the risk is that, the latest, like EL block building takes much less time than the proof computation or like probably less time in most cases at least. And so like you basically doing it like this will kind of throw a little bit away of the time advantage you get by building it as soon as you receive the block. 

**Nishant**
* Yeah. So like, at least right now we send you to the EL one slot before you start building the block. And as part of client software, we could just, like, regularly poll them and ask them which block transactions, you know, are in the payload.

**Dankrad Feist**
* The problem is that this theoretically could change completely, right? You could like, basically add nine seconds into the slot, its blobs one, two, three, and then suddenly it changes completely. because of different free market structure or something. And then it's 456 and, all the work you've done is useless. And you're now like, the EL sends you a block for which you haven't prepared any proofs. 

**Nishant**
* Yeah, that'd be the worst case. Although I think in the average case it shouldn't change too much. 

**Dankrad Feist**
* I agree so sure. Like, I mean, if you are like if you're happy with it being a little bit possible, which this is, then I guess that's fine. I agree that it works. In the average case. I don't think there is a lot of, like competition like this on block markets where people are bored with each other. 

**Nishant**
* Yeah. And, you know, even if it becomes the worst case, you could just fall back on this distributed blob building and have all these super nodes do it if it becomes that much of an issue. 

**Dankrad Feist**
* But yeah, I mean, I guess like if we say like we focus on distributed block building, then we can probably say, okay, like we get away with investing less in like optimizing the local proof computation because it's not really on the critical path anymore. Like I think most of the time with good distributed block building, you're better off sending out your execution block first, because that's the only thing that really has to come from your node, and everything else can come from somewhere else. So you're using your bandwidth more efficiently if you do it that way. 

**Nishant**
* But that would always be added latency with this because you need the a block header to, you know, reach the super node and the super node needs time to reconstruct. 

**Dankrad Feist**
* It doesn't necessarily add latency because like in if you view it as a whole system, right? When you're sending out your block and samples at the same time, you might be bandwidth constrained on that. So it might actually take longer for other nodes to receive those. Whereas if you start, say, by sending out your block header first and then your execution block, then like those get sent as soon as possible. And the, that your bandwidth is not clogged up with the samples in addition. So it's not necessarily true that like sending everything in parallel is the optimal strategy. If you have others who can do that work for you, that might actually be a better strategy.
* Like even if you can, even if you have all the proofs, it can be a better strategy not to send them if other nodes can send them. 

**Nishant**
* Yeah, yeah. If you're constrained, that would be a strategy that makes sense. 

**Dankrad Feist**
* I mean, I would assume that most homesteaders are bandwidth constrained. Because that's the hardest thing to get, right. Like, I mean, getting like, yeah. A high upload bandwidth internet connection is, in most places not cheap or easy. 

**Stokes**
* Right. I do want to surface Ansgar's comment here that, you know, there are several options here. it sounds like there's support for what we're calling option three in the post that George linked. So this is essentially having the CL pull or having the EL post which blobs are being considered locally. So it just has time to compute these proofs locally. That sounds like a good way to move forward. In which case, yeah, we should work on a spec just to start to get a sense of what that actually looks like in parallel. If we want to think about these more distributed proof generation tactics, that also sounds super promising. yeah. So if done right, if you want to make a group or we can use one of the discord channels. but yeah, I think we should move forward in that way. 

**Dankrad Feist**
* Yeah. Sounds good. Cool. Okay. 

# Remove unions from SSZ spec: Remove SSZ unions consensus-specs#3906 [1:02:55](https://youtu.be/XMPupRyEBk0?t=3775)
**Stokes**
* Let's move on to the next thing on the agenda. And I think it was this one. Right. So there's a PR to remove SEC unions from the spec. we were kind of joking earlier in the call about unions being a dirty word, and this PR is addressing that. so it's 3906 and the consensus specs repo, and I believe this PR just actually deletes the text itself. The rationale here is that. So yeah, today we do have unions in the spec. they're I would say a pretty experimental feature. I don't even think the production implementations of SSZ across the board have a union implementation. They're not currently used in the consensus specs.
* And so, you know, there's no reason to implement them. And because of this, it's like this kind of weird thing where it's like, okay, maybe we could use a union for this, say like the request types.
* And then it just kind of leads to a bunch of, conversations that can sometimes be bikeshedding. So, you know, to address all this, this PR basically just proposes to remove them entirely. I think this makes sense enough. I would maybe suggest leaving a note somewhere just like, hey, by the way, this was here and this commit, and it was removed there. You could imagine making, like, a features like we do for the specs themselves. Like the beacon chain specs you could have like a features folder for SSZ. There are a couple options here. but yeah, I just wanted to have some time to discuss. first off, if we want to go ahead and do this and then the best way. 

**Dustin**
* So I guess as the, author of this particular PR, I'll just say that part of I guess my perspective is I regard them as essentially as a fiction, is maybe the most blunt way of putting it like that. And this is my when, as you say, it creates these bikeshedding concerns is people treat it. I regarded as real as inventing a new SSZ feature. So when somebody proposes using unions. SSZ unions for something, it's like it's as if they to me as if they invented a new a new thing. And they're also proposing that at the same time as as whatever other feature they're proposing. And that's why, at least from my perspective, the bikeshedding me internally might happen. I can't obviously speak for anyone else here. I would certainly be happy to put a link in that, PR to have it.
* I mean, the pure deletion thing is kind of the platonic form of this PR, I think, but I'd be happy to, have it internally linked somehow to, here's the maybe the last the commit which removed it or I mean, it's kind of intertwined in the files, but somehow making it easy to, so you didn't have to manually shift through and find and get history where it is. We can use git history. That's what git is for. But but to make it easy to find and easy to, if people want to see it for sure. 

**Stokes**
* Yeah, that was my only point is just, you know, in previous iterations of the specs we have used them, say, for like early sharding designs or things like this. So it would be nice just to like be able to easily restore them in the event we need them in the future. I don't know if any portal people are here, but they did make a comment that they are using them, which is maybe a bit of a complication, but yeah, we might need to follow up with them just to see what makes sense with them, but otherwise. Does anyone oppose taking unions out or like managing them some way? Okay, I'll ask the portal folks what they think. but yeah, then we'll figure something out. If they want to keep it Somehow I would propose going with like this feature route that I was talking about.
* But otherwise, yeah, it does seem like they kind of unions themselves in the spec complicate things. like Dustin was saying, more than they really should be. So it would make sense  to address it somehow. 

**Dustin**
* Okay. And as far as, I mean, propose a couple of options I can. The two most there's a feature, so factoring it out to one of these feature branches is one one option. Another is to use git history another like and link to the like a whole file. Or if there's a remote link basically to somehow self-referentially to removal PR that can I guess be added later as a two stage thing there. various approaches is this, I guess my only slight concern. I think it would be broadly okay with the features thing, especially since they're I mean, so with the portal thing, it's that portal is strictly not Ethereum.
* And I would want to limit the I mean, this is actually a point a little bit beyond, just the this particular obviously I care about this particular PR now, but that the fact that somebody may have taken an encoding say that, that, Ethereum has a consensus spec encoding of something and that if the consensus specs don't use it, or else I would say something very similar, but somebody else decides, oh, this random feature of LP is great, and it turns out that Ethereum didn't care. I'm not sure I would regard that as Ethereum responsibility as such. I don't know, kind of maybe organizationally Or on a spec level. How that was best managed. 

**Felix**
* So I got to say that like portal is very much a part of Ethereum in it may not be a part of the critical path right now, but it's definitely a protocol which is being developed for the benefit of the Ethereum protocol. And it's very much, I don't know I mean, it's funded by EoF whole lot. So I wouldn't really put it like as a way external project with no connection. And I do think that, on that second point, just defining an encoding is something that is kind of independent of what the encoding is used for. And SSZ is very general purpose encoding, it is very useful. It has properties that are very useful to Etherebut it is a generic encoding and so changing encoding is okay and removing features is also okay.
* But I mean we do have to think a bit about like how this affects things that are using this encoding or if, I mean, if we all consider unions to be a mistake, then yeah, I mean, there's got to be some  other way to do this, but I don't think it's it's a good thing to say that, just because Ethereum is not using a certain feature of this encoding, it's like it should be deleted from the Ethereum version of the encoding. I think there's no such thing as an Ethereum specific version of SSZ. It's just an encoding that we invented. 

**Stokes**
* Yeah. And I think a nice way to square these is to just move it to some sort of feature spec. and then it's there. Okay, I will follow up with the people and just see what their take is on this, and we will figure out how to move forward. Okay. I think that was everything on the agenda. Let me just double check. Yeah, it looks like we got everything for today. any closing comments? Otherwise, we can wrap up a little bit early. Okay. Thanks, everyone. We'll go ahead and close out the call, and I'll see you on the next one. 

**Mikhail**
* Bye bye. 



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

  
### Next meeting Thursday Thursday 2024/9/19 at 14:00 UTC

