# Execution Layer Meeting 168
### Meeting Date/Time: August 17, 2023, 14:00-15:30 UTC
### Meeting Duration: 60 Mins
#### Moderator: Danny
###  [GitHub Agenda]( https://github.com/ethereum/pm/issues/845)

### [Audio Video of the Meeting](https://www.youtube.com/watch?v=DyAtbK2MQG4) 

## Summary

**168.1**:	Devnet 8 launched, with some infra support (https://dencun-devnet-8.ethpandaops.io/): bugs were found in a few clients but many have already been fixed + other fixes are on the way: network is finalizing.

**168.2**:	EIP-4788: we agreed to use a regular transaction to deploy the contract - we may revisit this if we feel that it was a bad decision, but it was the quickest option for now and seems ~half of people were in favor of it.

**168.3**:	Holesky: we agreed to launch the testnet with 1.6B ETH supply - ETA Sept 15!

**168.4**:	EIP/ERC split: we're moving forward with the split, and EIP editors are formalizing their governance process going forward. Expect a proper doc soon! Will keep being discussed in EIPIP calls.

**168.5**:	We agreed to renumber the EL fork spec files to prefix them with numbers to make the sequence clearer.

**168.6**:	EIP-7212 was presented (secp256r1 precompile) - this may be an EIP that L2s adopt before L1!

## Agenda
          
**Tim Beiko** [0:51](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=51s): We are live welcome everyone to ACDE #168. So some updates on Dencun today on Devnet #8. Like I mentioned in the chat, it'd be good to have a conversation around the deployment of the #4788 contract. Then we have some more updates on Holesky and the testing has been done there, some updates on the whole EIP/ ERC repo split and then two other things to discuss, one just around Naming the fork specs so that they're easier to reason about. Then we have someone to discuss a new EIP -7212. I guess to start Pari, do you want to give an update on devnet #8, you posted about it on the agenda?

 # Dencun Updates
 ## Devnet 8 spec

**Paritosh**[1:47](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=107s): I can give you a brief update on Devnet #8. So we have the chances yesterday and since then changes been mostly fine. We did hit a couple of issues overnight where prysm got stuck as well as Lighthouse and ethereum JS. Lighthouse and EthereumJS have been fixed in the meantime and I think prysm already has a PR but are waiting for it to be checked and merged. In the meantime we've just reallocated a couple of validators and we're finalizing and people can use the chain as expected. You can expect the blob scan and some other additional tooling to come up shortly but the beacon chain Explorer is already live.
 
**Danny** [2:29](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=149s): What was the domain of the problem?
 
**Paritosh** [2:34](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=154s): I actually haven't looked into either of them currently. So I need to maybe the client teams can talk about that.
 
**Danny** [2:40](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=160s): There's a new one from prysm Lighthouse ethereumJS or any of the other team want to give a quick update.
 
**Sean** [2:29](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=149s):  Sofar Lighthouse I think the issue is because we removed mplex support in a recent update and that caused us not be able to connect to some clients. So we just added it back in and it's like more impacts on small networks which is why we saw it here.
 
**Gajinder** [3:11](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=191s): For EthereumJS the issue with lighthouse was that on every slot Lighthouse sends around two FCU’s one with the old head and one with the new head. And when we were generating payload ID we were basically not doing unique Mess by the parent beacon block root. So basically the payload ID that was finally being provided was belonging to the old head and that was causing the block hash mismatch and once it's fixed now the correct payload the new Flash payload ID is generated and refresh period is built for the latest FCU.

**Tim Beiko** [3:53](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=233s): Got it. And this is the first time that this was triggered; it feels like something that would have showed up previously no.

**Barnabas Busa** [4:04](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=244s): We didn't have version three before I think.

**Tim Beiko** [4:06](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=246s): Okay Got it.

**Gajinder** [4:12](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=252s): Basically I think these are these best are not in the hive where basically two kind of FCU’s to an old FCU and FCU’s has been sent and checked whether the payload is generated or the new FCU but yes I mean it was for this particular new parameter it was for the first time.

**Tim Beiko** [4:31](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=271s): Got it.

**Paritosh** [4:33](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=277s): We ran through a couple of the V3 related errors earlier this week. It is used a couple of local testing toolset Kurtosis and we were able to get them patched relatively quite a bit faster than we usually would have. And I think we also caught an issue where an atomized and get would have been forked and that was also fixed with some local testing which may be good I know the nethermind Fork had a few stuff they wanted to bring up and have potentially fixed by now.
 
**Barnabas Busa** [5:04](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=304s): I would also highlight that kurtosis have been working very well for us. So it would be pretty good if different paintings could also begin into looking into it. And possibly giving it a try to check basic interrupt not like a full Matrix of all kinds combos but just some basic big ones. I think it would be very nice.

**Paritosh** [5:27](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=327s): To give you guys an idea on how we use it we kind of once we had an EL ready, we just made a list of the CL set already and just did that combination. And then once the second EL was ready, we just separated that combination. So we knew that all the CL’s worked with one particular EL and then we just combine the EL networks together to get completely interrupted. And I've listened to the document there in case anyone wants to try it out.
 
**Danny** [5:57](https://www.youtube.com/watch?v=DyAtbK2MQG4&t= 357s): And so this has been valuable just like literally just running local Nets, like you're not even doing or partitions or anything.

**Paritosh** [6:04](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=364s): Nothing at all we're kind of just running these tests and when we find something we can just send the Json config along with the command to the client team. And they're able to reproduce it almost immediately saving us a bunch of debug time there. And one thing I want to also mention in the end I'll be bringing up in the next call which is Mev related. But we also have the entire Mev workflow now. So we should be able to do a lot of Mev testing there as well.
 
**Barnabas Busa** [6:41](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=401s):
MEV doesn't support the fork yet though, so it's kind of the chicken and egg problem. We need the network is supported before the relays can support it and we need you get it.
 
**Tim Beiko** [6:55](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=415s): But I guess does this mean we're now like we're now ready to get relays to support this.

**Barnabas Busa** [7:04](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=424s): Yes okay so this is what we're blocked on is relay support for the fork. Yes Okay and they can test on kurtosis also so that's going to be very very useful.
 
**Tim Beiko** [7:15](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=435s): Nice. Andrew I saw you had your hand up briefly and then it went down to John ads.
 
**Andrews** [7:23](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=443s): I was curious about some talk about kurtosis but now parentage has sent one.
 
**Barnabas Busa** [7:31](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=451s): We are planning to write a very proper documentation about how to get started but the small doc that put together it's really enough to get started. But there's like a bunch of new features that we had recently added that can even do like high scale testing with multiple nodes on kubernetes so it's even it's even good for bigger tests also. 

**Andrews** [7:57](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=477s) : If you could when ready if you would share that one that will be great.

**Barnabas Busa** [8:02](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=482s): Yeah sure.
 
**Tim Beiko** [8:08](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=488s): Nice! Did any of the other client teams want to share thoughts about the devnet #8,  how it's been going?
 
 ## 4788 deployment

**Andrews** [7:31](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=451s): Yeah I would like to give an update on erigon so we haven't joined the devnet #8 yet. We've been mostly looking at fixing the hive test for Dencun. So like literally five minutes ago, I've checked in a patched Auto Branch bring down the number of hive test failures Pro like two just two failures out of 38 tests. So that there is progress there. We need to improve our like the security of our transaction pool for blob transactions. We need to implement EIP #4788 version two. So it would be nice if that one gets finalized. And then join devnet #8 but we're getting there slowly but not steadily.
 
**Tim Beiko** [9:11](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=551s): Got it thanks. Anyone else want to share updates?
 
**Marek** [9:23](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=563s): Some from our site everything is working as expected we another mind passes Hive test. We have a couple of issue but we managed to fix them before the devnet #8 started. One maybe interesting one was that Nethermind doesn't have implementation of #4844 based on system transaction. We have still direct rights to State TB but it turns out that we had some Edge case encoding actually three encoding issue but now it's fixed and we will we plan to move to system transaction.
 
**Tim Beiko** [10:16](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=616s): Got it thanks. Justin you want to give them a bit from besu.
 
**Justin** [10:23](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=623s): So, we're still working on being ready for devnet #8. #4788 is still in Flight. The Hive tests are not passing yet and we do need to break apart our #4788 Branch, so that we can include the beacon route in Genesis. Right now we're experiencing a lot of failures because those are like I said #4788 branch is not merged in yet. So we need to separate those and we'll move #4844. We're still working on passing all of the Hive tests.
 
**Tim Beiko** [11:00](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=660s): Any other team want to share updates or where they're at. Okay if not I guess the last big spec question we had was figuring out how we approached deploying the smart contract that's part of EIP #4788 and we discussed this on last call but I don't think we had strong consensus either way and at this point it's probably the main just blocker the finalizing the Cancun spec. So I'm curious if anyone has a strong opinion on like how we should approach this or if anyone has a change their thoughts on this since the last call. Danny?
 
**Danny** [12:05](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=725s): I will make my case once more but also acknowledge that either methods work. It's a bit of an aesthetic decision and I'd rather this be unblocked than push this Kick the Can down the curb again. But essentially you know I think that this is a system contract. This can be elevated as such and live at a particular address and given that we have the opportunity for the EIP just to be like entirely self-contained you know. It deploys its own code and then utilizes and exposes it via just on the fork conditionally placing code at what becomes kind of a system contract address. I think this makes Downstream tooling easier I think this makes test Nets easier. I think this makes all sorts of things simpler you know it's a matter of just turning the EIP on for a given Network rather than also considering you know if the contractor is actually deployed.  It's likely that this will be precedent setting in other things where we might want to have some sort of system type contract for example EIP - 7002 is something that I think is pretty important which is execution layer triggerable exits to enable certain types of validator activity but I think it's likely that once we kind of experiment with this type of system contract that we do see more of them. And so I you know instead of having n of these where we're making sure that for a given test net a given side net or given mainnet have the contract deployed. We just have them be able to deploy them themselves. Again I think that's the simpler more elegant more self-contained solution. But I both work and I am ready to unblock however y'all please.

**Tim Beiko** [14:08](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=848s): Okay thank you.

**LightClient** [14:12](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=852s): I guess I can argue the other I really don't think that we should just enshrine code onto mainnet. I think it's maybe simpler for some other networks to utilize this Beacon root contract concept. Because they can just turn it on but it doesn't make mainnet simpler. It actually makes the code more complicated because now we have to write something that says if we're at this Fork then we need to try this code into this address. And it needs to be hashed into the state root and so there's just like another branch of logic that needs to exist there then we set the precedent that if we need to do more of these. We possibly end up with like some file that has a bunch of different functions that says if this Fork to play this code if that worked deploy that code Etc. It just doesn't seem necessary because we have a good system for deploying contracts and this is an EVM contract. And I think we should use the system that exists for deploying those things and we should be kind of a normal citizen on there. It almost feels like that's a little bit more of a generic approach for other networks who want to use different types of system contracts because then it's more of a configuration thing where in their Genesis file they can say you know this is the address I want to call my system I want to do my system calls to. And they can decide what code actually ends up going there. Possibly do something different than what 4788 specifies and you know if it's like really a problem for people it's on new networks to deploy this thing like we can have some automatic setup with the Genesis allocation, where if you say this 4788 EIP is turned on then it just automatically adds it to the Genesis allocation like a lot of this stuff can be done behind the scenes. So, I think that putting the code again trying the code is a little bit more complicated and this is just this is a simpler thing and it utilizes the contract deployment infrastructure that already exists.

**Danny** [16:18](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=978s): I guess my one pushback is like this isn't just code that gets to be a good citizen this is code that has like very special system logic around it with like an exceptional color. And so I think we end up mixing two things. We like to enable a system activity we have to have some user perform an action otherwise it's not there and I think you do end up with conditional logic the other way as well because now I have to handle what is a reality where this EIP is turned on but the code's not actually there, and then we have the test.

**Lightclient** [17:02](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1022s): That's very easy to handle. Like the call already needs to handle EVM failures because it's just a normal EVM call so you kind of just discard whatever error comes back.

**Danny** [17:12](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1032s): So there'd be no additional tests in hive.

**Lightclient** [17:18](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1038s): I mean we can have an additional tested Hive that's probably good. But I would rather have an additional test in Hive than more code in the clients. So I don't know, I mean, I see the thought in the chat saying what if we forget to deploy it I mean we'll just deploy it.

**Stokes** [17:51](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1071s): If you're on some other network and like you forget to deploy on like the test net or like some roll up like it just seems so like one of us here is not going to go and make sure this contract's deployed for every other network that's going to exist ever so it's easier just to like have it as part of the fork project I think.

**Lightclient** [18:09](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1089s): I feel like a lot of networks don't need #4788 or they need a specialized version of #4788. They need to think about how it's going to look. So I'm not really worried about it being a little bit more complicated for them. I also don't think we should complicate mainnet to make it slightly easier for l2’s to have a feature.
 
**Tim Beiko** [18:38](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1118s): Okay I guess I'm curious you have to hear from more of the client teams. I guess is there another client team aside from get who is like in favor of the pre-deploy through a regular transaction. Okay so does this mean all the other teams are in favor of having it combined as part of the Forklogic.
 
**Andrews** [19:16](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1156s): I don't have a strong position okay
 
**Marek** [19:19](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1159s): Same Same assembly.
 
**Tim Beiko** [19:29](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1169s): And I guess yeah so to the point of like feature compatibility. Yeah Ansgar can go before.

**Ansgar** [19:39](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1179s): Yeah I wanted to just mentioned that in case we basically want to do this for all future. Could be that in the future there might be an instance where as part of the initial deployment we want to set, maybe exceptionally, set some initial storage slot or something and we can't do that out of a normal transaction. So in that case we would have to have basically deployment as some sort of Special Operations. So if we wanted to have a standard, the standard could only be that we do it in a special transaction. Of course if we just do one-off solutions for every such type then this would be fine.

**Danny** [20:18](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1218s): Yeah it's an interesting argument meaning like if you had to initialize the memory to non-zero you'd have to do something additionally exceptional.
 
**Ansgar** [20:34 ](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1234s): Could be that you just deploy a normal contract and then as part of the fork only set a few storage slots there would still be a smaller at the point of fork Change.

**Tim Beiko** [20:54](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1254s): So I guess like clearly there's still some like diverging opinions. The people feel like it's better to debate this and discuss this for another week or that we're sort of blocked on this and we should make a decision now In order to move forward as with the whole Fork as quickly as possible.

**Lightclient** [21:25](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1285s): It doesn't feel like it's blocking right. Now but I would rather decide sooner than later because all the test networks we just didn't try to mention this is.
 
**Tim Beiko** [21:50](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1310s): Yeah okay, so does it matter if public testnets have different addresses. We can use create two right.
 
**Lightclient** [21:59](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1319s): Well we can use a generated create address Martin and the PR has a transaction that deploys it's to any network that supports pre 155 transactions with the same address.
 
**Tim Beiko** [22:19](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1339s): Yeah I don't know it feels like it's pretty split. Feel like and I guess. So, Netherminds is also against any approach besides the system transaction right he's part of the team. And does anyone else have strong opinions? So in terms of like just the code paths how big like is it a significant change to do like in Fork deployment? If not I don't know I would lean towards the inFork deployment because it seems like there's slightly more support there and we can always revert it even though that's not ideal if people feel strongly the other way later. But I think I think we probably, so there's more people who prefer the transactional process not there. I don't know I feel like we'd probably be better off to agree to a direction and start working on that for like devnet #9. Or I guess you know maybe we defer it to like one week but I don't know it doesn't feel like we're gonna get new information in a week. Or I guess maybe this is the right question like does anyone feel like an extra week of debating this will be valuable?

**Lightclient** [24:22](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1462s): We have to actually debate it because I don't think that a lot was discussed between now and the last call we discussed on.

**Tim Beiko** [24:31](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1471s): Okay so I mean shall we discuss?

**Lightclient** [24:35](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1475s): I would like to see what like when is the system deployment like the deployment by a fork really going to be useful on other networks. Because I think a lot of networks won't use 4788 or if they do they'll do it slightly differently. And any new network like for a new network it doesn't really matter which approach we take. Because it can just be in China Genesis that's very simple so it's really a matter of networks that want to use 4788 that exist today.

**Ahmad Bitar** [25:06](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1506s): Yeah I just wanted to say that regardless of the approach that we follow here I would like to emphasize the importance of finalizing the spec. In general before going into trying to deploy another devnet. So before going to like at least two weeks before divnet #9. We should have a spec finalized with tests ready to have enough time to run our tests and be ready for the next devnet.

**Tim Beiko** [25:43](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1543s): Yeah I could agree like I'd rather make it call on this now and be able to move forward and I guess so if we do the bundled transaction approach like it doesn't necessarily preclude us from not doing that in the Futures like just deploying a contract. Naturally whereas I guess what we're saying is if we don't bundle them together, then it starts to become awkward because we then have a list of contracts, that we need to consider each time. And then yes okay so Daniel's saying also that there may not be that many.
 
**Danno Ferrin** [26:47](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1607s): This contract is only a mainnet focused contract with the EL/CL pairing. Not many L2’s do that I'm not aware of any they might maybe they'll repurpose it for L1 root. Which means they'll do their own thing. I don't think we need to make much space for this other than just for how mainnet going to use it.
 
**Danny** [27:08](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1628s):
Yeah exactly I mean there is genesis. Also I think this is precedent setting for this type of deployment which the fact that we're talking about uniquely something that is CL/EL is interesting here but like on the appointment it's like a generic word.
 
**Tim Beiko** [27:26](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1646s): Yeah do you maybe want to give a bit of context on the EL triggered exits and like roughly wide I would use a certain design.

**Danny** [27:35](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1655s): That's also that's also probably exceptional although.

**Tim Beiko** [27:41](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1661s): If we're just thinking about mainnet right it's not clear to me how much context everyone has around like how EL triggered exits would work? And it might be helpful to just understand that a bit better to like make sense at this.

**Danny** [27:59](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1679s): I mean similarly right now 7002 is specified as a staple pre-compile which we kind of got into the Zone on this. One that maybe stateful pre-compiles don't make sense and instead we should be deploying code. So if this is precedent setting then if we did something like 7002. Then similarly we would have a contract or some byte code living somewhere that users can hit and then the system does something with respect to that. So on this case instead of preloading the state with something like #4788 to use users are triggering actions inside of this contract. And then the system is picking up stuff. So like users trigger as it exits  that are valid upon some Logic the then the system picks these up and pulls them into the consensus layer. So kind of similar Concepts going on there but  other things you could think about were like the example of removing #1256 historical roots that are implicitly part of the state transition function. Right now and put it writing them into State that's not cross layer that ends up being useful kind of in any EVM deployment. And is a definitely a nice to have especially in the context of statelessness to make things much more contained on that front.  But there's just there's a lot of examples you can think of that we might end up going down that path Consensus layers and we're not.

**Ahmad Bitar** [29:39](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1779s): One of the other reasons that I also support system transactions is that I feel like. I don't want to have a change in the state that is not like justified by a certain like transaction usually in ethereum when there is a change in the state there is a transaction that made that change. That's most of the cases that I know of so I would like to keep that up. Even if it's deploying a system contract it should be like done by a transaction changing the state.

**Danny** [30:16](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1816s): So I can think of many examples where that's not the case withdrawals are those transactions I don't know um the other component of 4788 is actually that the system updates the state every slot every block. And so coinbase and all there's all sorts of like system operations that update the state. If we're going to be bound to that then we can't do a lot of things and just because this is I don't know like to compare this to an irregular State change. I think is a bit dishonest with respect to the other things that we do to the system. But I'm gonna stop debating this because we're at half an hour already and I don't want to be the only person
that's holding this up because at the end of the day both methods work and I  don't really want to block this anymore.
 
**Tim Beiko** [31:14](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1874s): Yeah it does seem like it's pretty split so in terms of just the code implementations if we go with just the pre is it easier to go from we've like just a regular transaction flow to then adding the special deployment flow or is it easier to go the other way around. I assume it's easier if we go with the like normal transaction that gets deployed that deploys the contract and then decide to make that into like a special transaction during the fork that's probably simpler for clients is that is that correct?

**Lightclient** [32:07](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1927s): Yeah I think right now we're kind of compatible with the just deployed in a  transaction yeah and if we want to support the deploy by Fork we would have to add that code and then have some tests.
 
**Tim Beiko** [32:21](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=1841s): So I would lean towards deploying it in a separate transaction for now. If people want to keep discussing it and feel strongly about it  you know we can bring it up in two weeks like and if people implement it and feel like it's actually a terrible approach and the other way is better you know we can revisit that and then add the extra code path in two weeks. But I think for now given it's like pretty split. I would just go for the simplest option. And so we can have it you know tentatively finalized spec move forward with this. And revisit it if we feel a strong need to does anyone object to that. So there's the last question about the regular transaction is like it requires a transaction. It doesn't require transaction key Matt do you want to explain how that would work?
 
**Lightclient** [33:20](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2000s): Yeah I mean I kind of want to keep this debate mostly focused on whether we deploy with a transaction or whether we enshrine it because I think once we get into wants to play with the transaction. There's a couple ways that it's possible to do it there's a way that you can just arbitrarily pick a signature which kind of creates a synthetic signature. You recover the address and then that address is like a one-time use address for a specific operation. So if we wanted to deploy the same address at any EVM network that supports pre-155 transactions we could do something like that. I think that's the best approach but if people are not as enthusiastic about that then we can't just have someone deploy it with a key there's really nothing wrong with that either.

**Danny** [34:05](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2045s): You fund that address once you pick it.

**Lightclient** [34:08](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2048s): Right yeah exactly

**Danno Ferrin** [34:12](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2052s): This was used extensively in Shanghai attack recovery there's a lot of transactions with that online.

**Danny** [34:20](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2060s): You're gonna fund it like that?

**Tim Beiko** [34:25](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2065s): Is that what it takes I guess yeah just because I do want to make sure we like all agree on this spec like this probably the most important thing. So does anyone disagree with like client's approach to deploy the transaction. Okay so let's do that like time do you want to open a PR to the EIP or I don't know if your PR already had this?

**Lightclient** [35:09](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2109s): It has it. 

## Holesky updates

**Tim Beiko** [35:10](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2110s): Okay perfect! So we should go ahead and merge this if it's not already done then. Okay anything else on 4788. Okay next up testnet updates so there's been some more testing on the Holesky? Pari do you wanna give an update on this as well?
 
**Paritosh** [35:53](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2153s): Yeah so we've the last tests last week and I think I also brought it up in the last call but we tested essentially 1.4 million validators. And we were able to get finalizing that Network. So we went with recommending that as the starting size for Holesky. There's an onboarding document and a telegram group for some entities to share their pub keys. And then we'll be generating the Genesis State using those pub Keys. The info is also available on the GitHub repository. The only thing that's still kind of open and that we also wanted to test was in the earlier course we did we to limit the overall issuance of Holesky or roughly the same order of magnitude as mainnet. But the commitments we've received total up to something like 1.6 billion. We initially thought okay maybe that's too much but while looking at the test net code we've kind of been starting every test match for the past year with like 10 billion. And that's been fine so we also tried a couple transactions moving around like 9 billion ether or something and nothing Epoch on devnet #8. So the question to the room is do you just take the allocation as is IE holesky would have roughly 1.6 billion ether? Or do we just slash it down until we hit roughly mean that mainnet size?
 
**Tim Beiko** [37:22](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2242s): So it's going from 1.6 I thought you said 36 billion?
 
**Paritosh** [37:27](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2247s): No 1.6 that's what we have committed but if we were to Splash it down to mainnet levels that would be like I don't know 10 times lower at least.
 
**Tim Beiko** [37:39](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2259s): Is there a reason to not do 1.6 billion if we've seen it work on the devnets.
 
**Paritosh** [37:45](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2265s): I think the earlier field was just that we thought we hadn't tested that but apparently we have been this whole time.

**Tim Beiko** [37:53](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2273s): Cut it yeah there's any client team feel like 1.6 is not doable or would cause a risk.
Okay let's do 1.6 then.
 
**Paritosh** [38:11](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2291s): Sounds good then we should have a chance to stay ready around Monday and we'll put it up on the GitHub repo and hopefully Client teams have a chance to make the uses before September 15th that's the date we're aiming for Genesis so much Dave.

## ERP/ ERC Repo Split

**Tim Beiko** [38:27](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2307s): Nice anything else on holesky? Okay thanks Pari next up Sam I believe had an update on the ERP/ ERC repo split. Sam are you on the call?

**Sam** [38:57](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2337s): I am yes my area is working great so very brief update three points so one we're going ahead with the split we'll be removing ERC’s from all the other types of EIP’s first and then we may be dividing it up further we'll see. Second we're working on making our governance process more transparent and actually writing it down into a document. Reach out to me on Discord if you're curious otherwise it doesn't really affect you guys directly. So just mentioning it here for fun. And third Greg was going to make it explicit that we're staying like one group or one organization. So that's pretty much it for the updates on the EIP and governance side of things. Thanks.

**Tim Beiko** [39:45](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2385s): Thank you! Does anyone have thoughts questions comments?

**Gcolvin** [39:53](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2393s): I'd like to add that the governance will be such that the editors should never be in the way of making an upgrade never

**Tim Beiko** [40:12](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2412s): Got it thanks. Anything else on that specifically.

**Gcolvin** [40:23](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2423s): There'll be documents soon enough, we're working on that.

**Tim Beiko** [40:26](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2426s): Yes Sam ,I know you had your you had a PR up with some of your proposed change do you mind just sharing either to PR or the doc in the chat if people want to review.

**Gcolvin** [40:37](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2437s): They're really not ready for some of you it'll probably take a few days to a week and then the next EIP meeting we should come to consensus on that. And then we'll bring them back to the to this meeting and we need to open up some communication with the consensus layer and see if we can find a way to serve them.

**Tim Beiko** [41:03](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2463s): Okay cool then we'll wait till the darks are in a better state. Anything else on this? Okay then Andrew you had just a quick ask so we have all these Fork specs on the EL Side and their name just using their Fork name so Cancun.MD, london.md and you were mentioning that it's a bit awkward to navigate if you don't know the actual ordering of the fork. So should we just rename everything to use numbers so you know 01 that 01- the first fork , 02-second Fork that seems reasonable. I guess you want to add more context around that.

**Andrews** [42:02](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2522s): Well it's a minor thing it's but it might be a slide to usability Improvement and I think with the SEO folks they are named alphabetically. So with those it's easier to navigate 

**Tim Beiko** [42:20](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2540s): Cool! There's so I can make that change in this pack if there's no objection there concerns. 

## EIP Discussion EIP-7212

**Tim Beiko** : Okay then last thing we had someone wanting to present EIP-7212. Please go ahead okay.

**Ulas Erdogan** [42:52](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2572s): I'm Ulas, I'm one of the authors of EIP-7212 and I'm here to present the proposal to request some reviews and feedback from the core developer community. The Proposal creates a new pre-compile contract similar to EC recovery which allows the signature verifications for sec P262. 56 R1 elliptical which is one of the most Mass adapted Curves in the internet ecosystem. Allowing an efficient use of this curving the EVM provides utilization of the products using this curve in the application such as signature abstraction by secure elements of the mobile device and dynastic operation for web 2 domains in DNS Etc. And I think that this is pre-compiled contract can onboard lots of new users and solutions which connect web 2 to web 3 especially in the account abstraction wallets. And we would love to hear any comments and recommendations for the EIP and I also have a few questions. And I will ask them here the first is the EIP specifies. The curve operation for the verification but it's a bit different from the common use case that we are familiar in ECI cover which is recovery. My design Choice are coming from in the ECI recovered. The recovered address is the accounts public address. So it makes sense but in the  in the R1 curve it's not a meaningful data for the accounts. And the products implementing this curve is not giving the signature values. So it's not possible to make recovery directly,  without trying different values to recover so my question is it makes sense to keep verification process going as the verification. So the implementation is also becoming more adapted in the applications or I had some feedback to change the proposal to recovery from the verification. These are my questions. And again I would love to hear any comments and recommendations.

**Tim Beiko** [45:14](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2714s): Thank you, anyone have thoughts comments Danno!

**Danno Ferrin** [45:30](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2730s): So one trend that's happening it's it's not ready yet is we're um the Epsilon team I'm watching them build this thing called EVM Max which is a modular map  extension to the EVM with the intent that a lot of these things that might be precomposed could be done in EVM for reasonable costs. Is the R1 curve something that might be usable? For that because judging by some of the experiences I've had in the past couple of years with performance and not just performance but Corner case issues with pre-compiles. They're kind of high risk to put in. It seems simple but the corner case is an attack service they exposed tend to be problematic. And it'll be a lot better if we could you know I used to be in the camp that yeah let's do all these pre-compiled let's bring automobile lessons but now I'm more of the camp that we should try and do as much fine tuning as possible and with this EVM MAX be able to record the R1 curves. I guess it's a big question? 

**Jared wasinger** [46:30](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2790s): I can actually answer that because I did a bit of Investigation on that so the answer is yes. And based on the cost model that I had originally proposed in EIP #5843 U Wasm it would cost around 70000 gas to do like EC recover or to do EC recovery with SEC p with this curve. So I mean it's quite a bit more expensive than the pre-compile but it's
I think the best implementation we have in EVM right now is around or I was told is around 600000 gas so yeah I think something like EVMMAX would bring us closer to pre-compile like costs but it's still quite a ways off. But 70000 gas versus I think what is it 2000 I don't I mean yeah perspective that's a lot less relevant than 600000 versus 70000 right. So right.

**Danno Ferrin** [47:53](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2873s): But then there's also some design issues like it doesn't have the recovery key and a lot of the signatures the initial signature said here's a public key here's a signature try and match it out which might resultin you know one or two typically uh tests to see if it works. So it allows it would allow the end user to customize their use of the R1 is one advantage but I don't know if that'll overcome the 20x. So that's good measure that you have the number that we know that is like 20x that's very useful.

**Jared wasinger** [48:19](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2899s):  Yeah I mean it.  I don't have a benchmark but I think it should be around there at conservatively I mean I think it could be potentially better but yeah.

**Ansgar** [48:44](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=2924s): Well on that point first I just wonder if you mentioned that I think even if we end up at a 60- 70k gas cost Point that's not ideal just because if we expect that a big proportion of future the kind of abstraction contracts use this car then this would immediately still be the the dominant portion of the overall overhead of sending a transaction which just not not ideal given that you would expect like high usage of this pre-compiled slash EVM Max. But my original comment was was going to be more a bit more abstract. So just to give context for people who haven't paid attention to the EIP yet why it's an interesting EAP’s that there's a lot of interests by layer 2's. To also add this functionality so we're basically in the process talking with layers who's it might be that they are interested in adopting this EIP relatively soon whereas of course if this ever reaches mainnet it will take a little bit. So it might be just an interesting first candidate in basically just seeing in the standardisation process and kind of like there's the interacting between layers and layer 2’s and so basically us paying attention relatively early on in the process would still be valuable. Just so that we don't end up with in a world where we bring a version of this to layer 2’s and then six months later bring a slightly different version of this to layer 1. So one super basically just mentioned that this is like the EIP here is in an interesting place. 

**Mikhail Kalinin** [50:28](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=3028s): Thanks for the comments. Also I heard that the casing fell an artistic are implementing the pre-compile contract in some way. And also I have another recommendation that's implements this pre-compile as a progressive pre-compile idea which creates future pre-compiles as smart contracts implementing the same pre-compile interface in a deterministic address in Every Chain by create two so that different chains can implement the EIP independently in the same address.  I think it's matched with unscar's comments and usable.

**Tim Beiko** [51:15](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=3075s): Okay does anyone else have thoughts comments on this? if not then yeah so there's a discussion link and I was shared in the chat here we can continue the conversation there and it's definitely interesting to explore the angle of L2’s potentially adopting this prior to L1 that was the last thing we had on the agenda anything else anyone wanted to share before we wrap up. Okay well thanks everyone and talk to you all soon and have a good day.

**Stokes** [51:59](https://www.youtube.com/watch?v=DyAtbK2MQG4&t=3119s):  Thanks everyone. 


# Attendees

* Ansgar Dietrichs
* Maintainer
* Dogan
* Alex Stokes
* Danno Ferrin
* Pooja Ranjan
* Marcello
* Pat Stiles
* Joshua Rudolf
* Marek
* Ayman
* Alexey
* Mikhail kalinin
* Anshal
* Mario Vega
* OxTylerHolmes
* Amirul Ashraf
* Jamie Lokier
* Andrew
* Tomasz
* Yoav
* Danny
* Marius
* Dankrad Fiest
* Fabio
* Barnabas Busa
* Kasey
* Marcin
* Charles
* Ben Edginton
* Roberto B
* Ahmad Bitar
* Sean
* Parithosh
* Tim Bieko
* Mikeneuder
* Lightclient
* Matt Nelson
* EthDreamer
* Fabio Di Fabio
* Jamie Lokier
* Abhishek Kumar
* Estimcmxci
* Roman Krasiuk

### Next meeting 31ST AUG,2023, 14:00-15:30 UTC
