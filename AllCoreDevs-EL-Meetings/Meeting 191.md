

# Execution Layer Meeting 191 [2024-07-04]
## Meeting Date/Time: July 4, 2024, 14:00-15:30 UTC
### Meeting Duration: 99 Mins
### Moderator: Tim Beiko
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1080)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=58_bJD_dmm0)
### Meeting Notes: Meenakshi Singh
___

## Summary

| S No | Agenda | Summary |
| -------- | -------- | -------- |
| 191.1    | Pectra Update | Clients are progressing with devnet-1 implementations. |
| | | The launch is expected within the next week or tw.|
|191.2 | EIP -7702| Updates on EIP-7702 were provided, with plans to merge it into devnet-2 soon.|
|191.3| EIP-7212|This proposal, which improves key/wallet management, was discussed. A decision on its inclusion in Pectra will be made in the next meeting.|
|191.4| Events in predeploys for 7002 and 7251| Predeploy system contracts for cross-layer communication with EIP-7002 and EIP-7251. Consensus was that this change makes sense and the corresponding contracts will be updated.|
|191.5| Deactivate EIP-158| Simplify the effects of deploying EIP-7702 and the Verkle migration. In light of the latest updates to 7702 they no longer need this proposal and decided to ignore it.|
|191.6| Updates of EIP 4444's| There was a call for more regular updates on EIP-4444’s progress, and a call out to various things both rollups and clients can do to more intelligently handle the pipeline from blob producer to blob inclusion on-chain.|

## Pectra Updates

**Stokes** [0:35](https://www.youtube.com/watch?v=58_bJD_dmm0&t=35s): Hey everyone! This is ACDE #191. Tim is out today so I will be filling in for him. And yeah I dropped the agenda in the chat here. It’s issue # 1080 on the PM repo and lets get started. So first up let’s jump into Pectra and in particular if there are any updates for devnet 1.  There's a link to a spec here with the latest in greatest EIPs. Yeah would anyone like to give an update on their client's progress or anything like that?

**Paritosh** [1:22](https://www.youtube.com/watch?v=58_bJD_dmm0&t=82s): I think, I can maybe start with some overarching progress update. So we do have local testing done for two ELs and 3 CLs and there's a bunch of happy case scenarios and the Client seem to all agree on the happy case scenarios which is great news. I've posted the kurtosis config link to reproduce that. So in case someone wants to test if they're following along the chain then you can have two clients be the producers and you can just check if your client is forking  off based on the happy case tests and the open question right now is do we want to wait for more clients to be ready before we launch Devnet 1 or do we want to just launch Devnet 1 and retroactively add clients as and when they're ready.


**Stokes** [2:21](https://www.youtube.com/watch?v=58_bJD_dmm0&t=141s): Andrew?

**Andrew** [2:23](https://www.youtube.com/watch?v=58_bJD_dmm0&t=143s): Yeah I can talk about Erigon’s progress. We are still working on 7702. That's work in progress but I think launching devnet 1 now might be the timing might been a bit unfortunate because next week is STC and a lot of people will be there. So I'm not sure whether we will be able to work because of the ECC on Devnet 1.

**Stokes** [2:55](https://www.youtube.com/watch?v=58_bJD_dmm0&t=175s): Daniel?

**Daniel** [2:58](https://www.youtube.com/watch?v=58_bJD_dmm0&t=178s): I can give an update for Besu. So we were running the execution tests that were released last Friday we are still fixing some bugs that we found with the test I think we will be a bit slowed down because part of the team now is on holidays because of July 4th. So I would guess we would be ready around mid to end of next week. But I think for us it would not matter so much if we start Devnet 1 already now or not. So if not we would just Join later. 

**Stokes** [3:46](https://www.youtube.com/watch?v=58_bJD_dmm0&t=226s): Okay thanks Mehdi?

**Mehdi** [3:48](https://www.youtube.com/watch?v=58_bJD_dmm0&t=228s): An update from Teku. We are ready for Devnet 1. We have all the reference test passing. So yeah.

**Stokes** [4:00](https://www.youtube.com/watch?v=58_bJD_dmm0&t=240s): Okay great Mark?

**Marek** [4:03](https://www.youtube.com/watch?v=58_bJD_dmm0&t=243s): Yeah we are working on this Happy Case scenarios bar mentioned we will update image before devnet 1 because we have one bug in 7702. But we should be ready pretty soon with this fix as well. 

**Stokes** [4:28](https://www.youtube.com/watch?v=58_bJD_dmm0&t=268s): Okay cool kind of sounding like to me we could wait another cycle of ACD to launch. I don't know if Barnabas or Pari feel differently?

**Paritosh** [4:45](https://www.youtube.com/watch?v=58_bJD_dmm0&t=285s): Yeah I mean we're fine to wait. We still are missing a couple of happy case asserter tests. So we'll probably just be working on those in the meantime. 


## [7702 updates](https://github.com/ethereum/pm/issues/1080#issuecomment-2207359475)

**Stokes** [4:55](https://www.youtube.com/watch?v=58_bJD_dmm0&t=295s): Okay cool but it does sound like soon we will be ready with Devnet 1 which is super cool. Anything else on devnet 1 there for pectra. There was a call out on the agenda for 7702. So we'll move to that next unless there's anything else more broadly with Pectra that anyone would like to discuss? Okay so let's move to 7702. So I think Tim had this on the agenda just to ask for General updates. I think the there were still some open questions around the EIP that would kind of be blocking its inclusion in Petra that being said. I think we have some updates on those open questions maybe lightclient if you'd like to call out this PR that you had linked to.

**Lightclient** [6:16](https://www.youtube.com/watch?v=58_bJD_dmm0&t=376s): Okay I just posted the link to this PR in the chat basically this is something that we've talked about offline and in the last breakout call. People were mostly supportive of this change both on the wallet side and the client side the tldr for those who haven't had a chance to review. We're essentially changing 7702 to be less of a ephemeral deployment of contract and more of a deploying a contract permanently more permanently into the EOA's code. And it allows the EOA to continue operating as an EOA because the code that's deployed in their account isn't exactly the code which the user wants to delegate to. It's a a designator that has a prefix and then an address to the code which the user would like to delegate to. So that sort of gives us the ability to see that EOA is a special type of account that can both originate transactions and act as a contract this lets us get around the Restriction in 3607. I think where we banned EOA’s with code from originating transactions. It also helps us get around if fundamental problem that we've had since 3074 which is dealing with these permanent authorizations and replay protection and Authorizations. The fundamental problem there was that to get the functionality that which we felt was really important, which was things like signing one message. And then reusing the authorization over and over again required us not having replaced function replay protection functionality in the authorization. This circumvents that by instead of the permanency of the authorization coming from the message it's being stored in a place in the account. And that feels like the ideal path. So now not only do the message do the authorizations get to have the nonce and get to be only single use but potentially tools like other wallets that are interested in acting as the EOA because maybe the user has put their private key or their neonic into multiple wallets they can then just look on the chain and see if the account has already delegated to a specific to a specific piece of code. So I think that this is addressing most of the concerns that were outstanding if I'm missing something someone please chime in. But I'm curious how people feel about this. And if people feel that it would be okay to move towards the merge this and move towards this for devnet too. 

**Stokes** [9:12](https://www.youtube.com/watch?v=58_bJD_dmm0&t=552s): Ansgar?

**Ansgar** [9:14](https://www.youtube.com/watch?v=58_bJD_dmm0&t=554s): Yeah I just wanted to to briefly expand on what Matt just said because on the breakout call we discussed with at least the people present there in general feeling there was that indeed this PR would be a really good candidate for basically Devnet 2 with the one caveat just being that just everyone should be aware should understand this as like given that 7702 is so new. We're still iterating towards the final spec like I don't think it's very likely that this PR will get us quite to a final spec yet for pectra. And so smaller changes might still be coming. We already discussed potential ones. It's just that we all agree that it's likely that basically this PR gets us significantly closer. So it's seems like a better Target for a devnet 2 than the old spec. But just for people's expectation that there will be future small changes by in know likelihood to the EIP. 

**Stokes** [10:18](https://www.youtube.com/watch?v=58_bJD_dmm0&t=618s): Okay. There was a question in the chat. It looks like the chat is there Daniel? 

**Daniel** [10:29](https://www.youtube.com/watch?v=58_bJD_dmm0&t=629s): Yeah I was just wondering because we said that we are going to move Devnet 1 maybe one or two weeks in the future. Does it make sense that we Implement directly the latest version of 7702? So the one that is proposed right now or should we still go with the original one?


**Stokes** [10:52](https://www.youtube.com/watch?v=58_bJD_dmm0&t=652s): I would say to keep it as is just because this latest PR is not merged yet and there could be some last minute feedback. Let me go see what was in here. So yeah the Devnet 1 specs just link directly to the EIP. So I would just target that as unless anyone else would like to argue for something differently right now? 

**Lightclient** [11:16](https://www.youtube.com/watch?v=58_bJD_dmm0&t=676s): I feel we should have devnet 1 ASAP but I don't think we should change devnet 1 necessarily. 

**Stokes** [11:25](https://www.youtube.com/watch?v=58_bJD_dmm0&t=685s): Yeah that makes sense to me.

**Lightclient** [11:27](https://www.youtube.com/watch?v=58_bJD_dmm0&t=687s): I think like most most clients have already implemented everything more or less. So it's not like clients haven't implemented 7702 at all. 

**Stokes** [11:39](https://www.youtube.com/watch?v=58_bJD_dmm0&t=699s): Right okay. Jochem? 

**Jochem** [11:43](https://www.youtube.com/watch?v=58_bJD_dmm0&t=703s): I hink yes. Has actually implemented it. So we have it.

**Stokes** [11:52](https://www.youtube.com/watch?v=58_bJD_dmm0&t=712s): Great!


**Lightclient** [11:54](https://www.youtube.com/watch?v=58_bJD_dmm0&t=714s): So is there any feedback on including this in devnet 2 like seems like we're talking a bit about about timing but it feels that most people are generally positive on accepting this for devnet 2 whenever that ends up being.

**Stokes** [12:22](https://www.youtube.com/watch?v=58_bJD_dmm0&t=742s): Yeah I would lean towards just getting it merged first and then we can discuss scheduling. 

**Lightclient** [12:28](https://www.youtube.com/watch?v=58_bJD_dmm0&t=748s): But I mean it's because we're waiting to include in Devnet 2.  Like I can merge it right now. All right unless someone feels strongly or says something in the next six to 12 hours. I'll merge it at the end of today and we should plan on doing that for devnet 2. 

**Stokes** [13:05](https://www.youtube.com/watch?v=58_bJD_dmm0&t=785s): Okay yeah sounds good and there doesn't seem to be any negative feedback. So let's move ahead with that plan.

**Danno Ferrin** [13:13](https://www.youtube.com/watch?v=58_bJD_dmm0&t=793s): Consider for a moment the most Americans out are on vacation should give a couple days for people to reply in chat before proceeding but I think a couple days is fair.

**LightClient** [13:21](https://www.youtube.com/watch?v=58_bJD_dmm0&t=801s): They've had a week and a half. 

**Danno Ferrin** [13:26](https://www.youtube.com/watch?v=58_bJD_dmm0&t=806s): True but you're actually pulling the trigger here couple days would be nice.

**Stokes** [13:35](https://www.youtube.com/watch?v=58_bJD_dmm0&t=815s): Yeah I don't think we discuss this on the last ACD. So you know process wise it would make sense to give people some time a reasonable amount of time after say announcing on the call but generally I think moving towards Devnet 2 makes a lot of sense. Cool. So I think that was it on Pectra. Oh maybe this do up the next thing actually. But yeah is there anything on 7702  otherwise we will go to the next EIP 7212 which I think is the R1 curve.


**Lightclient** [14:21](https://www.youtube.com/watch?v=58_bJD_dmm0&t=861s): I think the last thing on 7702 is that if we're moving towards changing this spec for devnet 2. I'm curious what people think about our testing strategy for 7702 and devnet 1. Like we do have some tests but I'm not sure if we're planning to build out more or if people are comfortable sort of leaving testing where it is for devnet 1 on 7702. 

**Stokes** [14:51](https://www.youtube.com/watch?v=58_bJD_dmm0&t=891s): Can we just test common subsets like whatever would apply to devnet 1 and also devnet 2. We could just focus on for devnet 1. 

**Lightclient** [15:04](https://www.youtube.com/watch?v=58_bJD_dmm0&t=904s): I don't think that there's as much common subsets like there is still a transaction tip. We are still setting these authorizations. I'm just not really sure like what test would work in both cases. 

**Stokes** [15:23](https://www.youtube.com/watch?v=58_bJD_dmm0&t=923s): Gotcha! So yeah I mean if it's going to change and kind of be breaking in that way. I would probably say just to test like whatever test we have now we'll use for Devnet 1 and then otherwise we'll focus on devnet 2 for Dvenet 2. Okay. Thank you for that. Everyone please take a look at the PR 47702. 

## [EIP-7212 inclusion and differences to RIP](https://github.com/ethereum/pm/issues/1080#issuecomment-2182270744) 

Next we had a topic for EIP 7212, So this is adding a precompile for the “secp256r1” Curve. And I think there's a few questions here. Let's see is Andrew on the call you had theComment. Looks like you are would you like to give us a little  context there? 

**Andrew** [16:36](https://www.youtube.com/watch?v=58_bJD_dmm0&t=996s): Yeah I think there was a discussion on on Discord and that EIP was CFI’ed and it's also used on polygon already. And because it's CFI basically we need to decide soon sooner rather than later whether we deliver it in pectra or not. And if we do like, do we actually take what's already on polygon or do we Implement a slightly different version of it using because on polygon say the precompile address is like  256 or something. And so it's not, it's in the range reserved for L2s. As far as I understand, yeah and the question is whether we keep that or modify it somehow for ethereum.

**Stokes** [17:37](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1057s): Right is that the only difference between the RIP and the EIP? Is just it's at a different precompile address?

**Andrew** [17:43](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1063s): I think somebody had a comment that the return value is unorthodox like it's not aligned with what the other pre compiles do but I don't remember who that was.

**Stokes** [17:56](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1076s): Okay. Yeah how do clients feel? This would pretty much be a purely EL change. So how do any clients feel about this EIP? Daniel? 

**Daniel** [18:19](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1099s): Yeah so for best we are definitely in favor of including it. I mean it's in the end every mobile phone is  supporting this EC curve. So it's like every most user already have like a built-in Hardware wallet for us. It definitely makes sense to to allow them to to use that instead of a traditional one. So I think for ux it would be great to have it. 

**Stokes** [18:48](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1128s): Lightclient?


**Lightclient** [18:51](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1131s): I think on geth we're generally pretty positive like adding the R1 curve is pretty easy since we already have the K1 curve. I think in general there's just still questions like why at another  cryptographic pre-compile is this the right cryptographic pre-compiled to add. I think we would feel a little bit better if there was more work towards something to allow people to write their own efficient cryptography in EVM. That's something that hasn't seen a lot of progress in the last year or two. And there's still questions about like what address to use we sort of carved out an address space for rollups and now we need to figure out are we going to use their the rollup address space for pre-compile on mainnet or are we going to deploy it at the regular address. And there's reasons to do both.

**Stokes** [19:47](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1187s): Marek?

**Marek** [19:48](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1188s): We are in favor of including this EIP.

**Stokes** [19:54](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1194s): Great! Danno?

**Danno Ferrin** [19:57](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1197s): So to address the why not do generally in the EVM. There's a proposal called EVM Max and that's not shipping until at least Amsterdam. So if we want the r curve anything sooner in a year and a half to two years to three years out we just need to ship it as a pre-compile. So that's why I support it even though I think the correct solution is move it all to EVM it's not going to ship in reasonable time frame. 

**Lightclient** [20:21](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1221s): Right but even if it's not going to ship in a reasonable time frame is the R1 curve the right curve to be shipping. Like some people are saying that the R1 curve is already starting to be replaced with Edwards curve. 


**Danno Ferrin** [20:35](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1235s): There's broad support for the r curve in a lot of places like Pass key from Google. So I'm satisfied there's always going to be new curves and when Edwards curve is ready. I mean there's been a proposal for Edwards pre-compiled but we could probably do an EVM 1 Max. It'll probably be relevant then when Max is ready.

**Stokes** [20:57](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1257s): Yeah personally I think there's enough value around this curve given its broad deployment in all these different contexts that it wouldn't quite make sense to block on something like EVM Max. Although generally there is value in EVM Max. But yeah it's unclear what those timelines will look like it looks like the EIP has the pre-compile address at you know the typical one meaning like the next lowest address for on ethereum in  EVM. And that does sound like something we need to resolve if we want to keep that or mere what is used stay on L2s. There was a comment in the chat to please please please please keep the same address in both places. Matt Lightclient you have something else to say or was your hand up.

**Lightclient** [21:48](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1308s): Yeah I mean separately from the specific concerns about R1. I get it's not a difficult thing to implement but Pectra is already Mega And at some point we need to ship Pectra and stop adding things and it feels like we're already way past that point so I feel a little bit weird that we're trying to add things where when we're like talking about when to ship the second devnet of this Fork. Again it's not again it's not like a big feature but eventually we have to just stop and ship and there's a lot of other things that we want to do that aren't in the hard Fork that aren't really being encoded like doing history expiry. Maybe improving the situation with the public mempool for blobs that we just have no bandwidth to do because we are spending a lot of time figuring these Forks out so R1 is kind of a I don't know a little bit of a different thing since it is very easy. But generally I would prefer to reduce the scope of pectra and focus on some of this other stuff including like not accepting R1.

**Stokes** [23:01](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1381s): Ansgar? 

**Ansgar** [23:05](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1385s): Yeah I just wanted to briefly clarify with the address. So in general because this is the very first time that we shipped as a pre-compile as an RIP. There was a little bit of confusion on the procedural parts. So specifically because this was first created as an EIP. Right now we just copied it over as an RIP. So the RIP has the exact same number in normally we basically don't want like those should be this should be one  yeah address bace EIP RIP address space. So basically the idea was to just delete the EIP and then create create one with a new number if we ever want to bring it to mainnet. We just never ended up doing this but  this now means that we we in this weird position where basically the EIP that still exists at the same number is now in an outdated version. So if you go to the RIP with the same number 7212. It actually for example had is now at a different address because that's the address where it was actually shipped on layer 2 which is the the first available address in the layer 2 specific address space that we reserved a couple months ago. I decided to reserve for l two use a couple months ago on All Core Devs. So yeah I think we should basically just ideally if we if we decide to add this to Spector we should use it as an opportunity to really make a general decisions around how we want to handle these Layer 2 trust feature in the future. If we may decide to make any spec changes to to the IP whatsoever so for example there have been some concerns about the return value of the pre-compiled that it doesn't give a return value instead of giving a 0 return value in terms of in the case of a verification failure. So for example if we wanted to make that change then we should definitely ship it at a different address because it would deviate from the layer 2 version if we want to ship it completely unchanged I think we should make a general decision whether we want to always in these cases retain the layer 2 specific address or ship it at the layer 1 specific address. And then also in that connection should make a final choice on how we handle this IP EIP situation. I think my preference would be to just completely delete the EIP because it's outdated anyway and has the weird numbering collision. And then create a new EIP that at a new higher number whatever the first available is today and just copy over the spec. But yeah so just to flag that there are these these open questions that we would have to solve.

**Stokes** [25:30](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1530s): Right Hadrien looks like he I maybe disconnected.. Yeah please go ahead.

**Hadrien** [25:48](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1548s): Yeah so sorry. I wanted to give a user perspective here for the record I work at open zeppin and we just  merged a library that supports the verification and the recovery of R1 signatures. The demand for that comes from the account abstraction word where people want to be able to use 4337 and other Account abstraction systems using smartphone as Hardware wallet basically. And the way we implemented it is we have a solidity implementation and we also have a version that checks the precompile from RIP 7212. The solidity implementation is way more expensive and if people could avoid pending that code that cost that would be better. So far our implementation tries to go to the pre-combine and if that is not successful then we go on to the solidity implementation. We have big concern about this feature being available on multiple chain at different addresses in terms of precompile because we think that for User it's better to not have to write code specifically depending on which Target chain you are targeting and changing the pre-compile address depending on what you're targeting. It should be better to have one sing version that works on as many chain as possible and unless this code start checking multiple precompile one after the other before then falling back to solid implementation it it would just be better for all the user if there was one address that Library could go to. I understand that from a client perspective it may feel they may feel differently but from a user's perspective people that are going to write code that use this precompile it that functionality is better if all chain provide it in a similar way.


**Lightclient** [27:48](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1668s): Yeah I think I generally agree with that. I think maybe the only argument I could see against it which is probably not the best argument for R1 because it's so simple. But there is a possibility that we get into a world where we need to change the precompile and if we have the rollups pre-compile that they've decided upon and on Mainnet we end up needing to change it whether it's in the fork that we originally Ship it or in a later Fork. Now we have maybe even a worse problem which is the same address being used for two different precompiles.

**Stokesr** [28:33](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1713s): Yeah iPhone you had a comment. 


**iPhone** [28:39](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1719s): Yeah I was just going to ask about the Readiness of R1 in the client libraries.

**Stokes** [28:53](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1733s): I think most. Oh yeah go ahead. Yeah Jochem.

**Jochem** [28:58](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1738s): Oh yeah sorry  like I've just been searching but we do not have it implemented  and it also does not seem that there's a quick JavaScript banging so I'm not really sure how long this will take. 


**Stokes** [29:12](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1752s): Marius.

**Marius* [29:15](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1755s): For us it's part of the go standard Library. So the implementation is really easy just add the gas costs and that's it and we also have a PR for already from someone who proposed it for the for the RIPs. In general I'm in favor of it's just yeah I think there's an argument to be had that we like it's nice that the the rollups did this first. And so I don't know if we actually need it that much on mainnet. No one is really doing these kind of things on mainnet anymore using like  smart contract Wallets on mainnet and it's not because it's impossible or anything just because it's too expensive anyway. So I don't think that adding this precompile will really change that. In my opinion I think it's great that we have this on rollups and people can use it on rollups. It feels again like one of these things where I don't know in my view we should focus on getting functionality and stuff onto rollups. And focus L1 on blob scalability and these kind of things and not focus too much on the like EVMfeature set on everyone. But I would be fine either way. 


**Stokes** [31:27](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1887s): Okay okay
Richard  Richard you have your hand up but you're not unmuting. 

**Richard** [31:49](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1909s): Sorry forget to unmute. I wanted to say from the standpoint of safe right like since we are one of these smart contract wallet projects that we would like to do stuffs like this on L1 right. Like because at least currently a lot of liquidity a lot of teams are still on L1 they are still there and this is where in the at least in the current state L1 is not perceived as this we want to move away from L1. If we as an ecosystem agree on this I think this would be a little bit of a mind set shift which I'm not generally against but it's at least not the agreement of everybody in the ecosystem. We had this discussion actually in one of the AA breakout rooms where it was not that clear that everybody agrees to yes. Let's move away from L1 where L1 is just basically this Blob space layer like this rollup Shain right. Like and this is where and unless we agree to this there is still a lot of Values where a lot of teams are still on L1 and a lot of teams do prefer also to have better UX and R1 will Pro will just enable this just as a general context there. 

**Stokes** [33:00](https://www.youtube.com/watch?v=58_bJD_dmm0&t=1980s): Okay thanks. So Ansgar has a proposal to move forward on this point. It sounds like there's like a few things we'd want to do so then I would suggest doing those things and deferring the actual inclusion decision to the next ACDE. Just to Echo some other comments in the chat because I have the same view like Pectra is already very very big. And we should really be deliberate about including more at this point. Okay let's move on then so. Oh actually Andrew had one other comment here let's just knock this out quickly. The question was if we can Sunset Goerli. So I'm not sure  he had the question if we had like a Blog announcement or something like this. I don't know if Tim was planning to do anything there in terms of following up. But generally my understanding is that clients already have started to deprecate Goerli support. So yeah should be fine to drop from your client and we will wave goodbye. 


**Andrew** [34:31](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2071s): And click is not used anywhere like for Hive testing or anything like that because goerly use just click and with goerli going with can potentially remove click as well.


**Lightcliet** [34:50](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2090s): Yeah I think the testing is.

**Marius** [34:54](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2094s): Yeah we already started removing click from geth code. please . 

## [Events in predeploys for 7002 and 7251](https://github.com/ethereum/pm/issues/1080#issuecomment-2200199789)

**Stokes** [35:11](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2111s): Okay no more Goerli no more click. Great. So then the next agenda item was a proposal to change the predeploys. We have these like system contracts or various functionality in this case that goes from  when we want to move information from the EL into the CL.There's two EIPs that uses type of functionality in pectra 7002 and 7251. Let's see I don't know if PK is on the call. Yeah would you like to  give us a summary of your proposal. 


**Pk910** [35:57](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2157s): Yeah hi everyone. As said I would like to suggest a small change to these both contracts. Because  right now both of these contracts do not trigger any event on successful invocation and the problem is while this is technically not required for the new functionality to to transfer this to process the information it makes. It really hard for external toolings like explorers to track back the origin of these execution there triggered operations. So if something  appears on  consensus layer we would like to trace back where this  operation comes from. So which transaction hash basically triggered that  operation and for that it would be really helpful if both contracts could trigger an event that the Explorers or external toolings can simply follow on. So yeah that's basically the request there. 

**Stokes** [37:07](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2227s): Thanks. Let's see are any of the authors of this contracts on the call. Maybe they could Chime in.

**Mikhail Kalinin** [37:17](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2237s): Yeah I think we have discussed this before and this change makes sense and it should not result in a big spike of in gas cost for the smart contract call. So makes sense to do and I've been discussed this with Lightclient previously and planning to have this change. One of the concerns might be that they will produce logs for just more chain date historical chain data. But it should not be a problem soon and it will be expired soon.

**PK910* [37:58](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2278s): But it would also align it a bit with the deposit contract because we have to lock there. And we are basically introducing new operations that are triggered on execution day without that doc event. So yeah it aligns it a bit to both contracts.

**MIkhail Kalinin** [38:27](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2307s): Right I mean I think we should just work on it if there is no other opinion and opposition to. 

**Stokes** [38:39](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2319s): The only thing I would ask is just like you know again if we keep changing Pectra. Pectra will never ship. So there's some argument for leaving it as is just because it's not critical. And invariably it will delay other things. Yeah I do think this is like a pretty small change in scope. So it's not the end of the world.

**Mikhail Kalinin** [39:01](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2341s): Yeah  fortunately this is handled by the smart contract itself. So we just need to modify smart contracts and then deploy a new code to the next devnet. So it should be quite opaque to client development process. The only one thing probably it's going to be a regular call where and client will handle those log messages as usual log messages. 

### [EIP-158 deactivation](https://github.com/ethereum/pm/issues/1080#issuecomment-2204191782)

**Stokes** [39:53](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2393s): Right. Okay so then we need to update the predeployment. But generally sounds like we're all on alignment here. Cool so next up on the agenda we have EIP 158 deactivation. I think Guillaume has an EIP or at least let's see this might just be a PR to 158. Yeah would you like to give us an overview? 

**Guillaume** [40:26](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2426s): So yeah a couple comments before because people started giving me feedback. So as it turns out it's referred to as 158 inside the the gas code but it's actually EIP 161. So thanks for catching that. And yeah the as a quick reminder we already had a conversation about it on ACD a couple months back  the one of the things that was being said is I should create EIP to support this so I did it's EIP 7733. And it's  about deactivating yes EIP 158/161. So it's actually not the whole EIP that needs to be to be deactivated it's only the deletion of an account if it's code hash well if it's the empty code hash if the balance is zero and if the nonce is zero. That is impossible to do in verkle simply because an EOA could have some storage slots. And in verkle you cannot figure out where an account slots are? So that needs to go. It's the same reason why self-destruct was removed or nerfed. We have the same problem that can happen in the context with 7702 in which  an account has funds. So a nonce-zero balance and EOA has a nonce-zero balance. So it has an empty code hash and  it's got an empty nonce. So it's just the result of a transfer. Then with 7702 someone can call into this account execute some code and the code transfers all the funds to a different account in which case the EIP 161. I have to get used to it. The EIP 161 rules say you have to delete the account which is not possible because like I said and just to clarify to make sure it's clear. If you execute the some code you could potentially create some storage slots. So there will be potentially State and you will not be able to find it. So yeah the simplest way would be either to to set the nonce of that account to one or to deactivate the EIP 161. The proposal is about deactivating EIP 161. And yeah that's pretty much it. Oh yeah there's one extra remark about it. It's that why am I talking about it in the context of Prague. We already had a conversation about it and initially I thought well we probably don't need it for Prague but there's one reason  to to include it in prague is. And that is if people want to give some push back against the overlay method in the future. T that means you will be able you will have to replay like to do the conversion at a given block height and replay blocks in a what I call a counterfactual history until that replay chain becomes the official chain. If during that period between the conversion and the replay and the and the Fork one of those things happen  one account gets deleted that means you do have  the existence of a deletion happening in a in verkle mode. That is going to be  what that's a potential bug that's a potential that's potentially breaking the conversion and so I think it's safer to it deactivate at the fork before if we want to do well if we want to give some push back on the overlay method. I am a proponent of the overlay method so personally I don't care but I want to make sure that everybody knows that if you don't include this EIP in Prague you're effectively cancelling this like removing this possibility. Yeah that's pretty much it. 



**Stokes** [44:55](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2695s): Okay thanks. Yeah Lightclient?

**Lightclient** [45:00](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2700s): I was just going to say this isn't really a problem with 7702 after the spec change. So I think we should focus on this for its merits of verkle since it's not related to 7702 now.

**Guillaume** [45:17](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2717s): Okay. So I'm not aware of the change in the spec but that means this could no longer
Happened. 

**Lightclient** [45:23](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2723s): Yes.

**GUillaume** [45:26](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2726s): And what was the for my personal logification.

**Lightclient** [45:33](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2733s): Now with the new PR for 7702 the Auth message is consumed by updating the accounts nonce. So the Auth message is only valid for the nonce it's signed and then once it's consumed account nonce bumped. So you can't have zero nonce accounts with code. 

**Guillaume** [45:48](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2748s): Okay cool yeah that works.

**Jochem** [45:55](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2755s): I think in general we can accept this EIP right. Because currently this whole situation of deleting these accounts is not really like empty accounts with storage that's not really possible anymore right. 

**Guillaume** [46:10](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2770s): It's not currently possible yes and in fact come to think of it if the 7702 EIP no longer leaves the nonce as zero then there there's no problem to begin with. So we can even withdraw the EIP all together which is fine by me. 

**Stokes** [46:43](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2803s): Okay so then we do not need 7733?

**Guillaume** [46:48](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2808s): Nope.

**Stokes** [46:51](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2811s): Okay great okay that was easy. That was it on the agenda for today. Is there anything else we'd like to discuss otherwise we'll go ahead and wrap up a bit early today. Potus? 

**Potuz** [47:17](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2837s): I just wanted to Shield that we have a breakout room tomorrow for 7732. This is the number 4 and the agenda is kind of packed. So if you're working on epbs  come tomorrow and if you're not take a look at 7732 that is already open and the CL repo has is an only CL EIP and the repo has the PR. 

**Stokes** [47:41](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2861s): Great thanks! Yeah I dropped the issue for the breakout call in the chat it's 1083. If you are interested please attend. Lightclient has a question did Guillaume have more to discuss on system Contract. 

**Guillaume** [48:08](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2888s): Yeah good question not really I mean maybe just announce that we reached an agreement. So yeah  there is an update to the EIP I made an update PR to the EIP to say in Prague everything behaves like everything in 2935 behaves exactly like 4788. And then there's another EIP to talk about how things change but once verkle is activated. So that is  that is a bridge that we have to cross when we get there. Yeah no need to to hold prague for this.

**Stokes** [49:00](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2940s): Okay and there's a little more discussion in the chat are we 100% certain there are no mainnet accounts which are empty but which have storage.

**Guillaume** [49:15](https://www.youtube.com/watch?v=58_bJD_dmm0&t=2955s): I'm not sure if that is going to impact 7733. So there's actually a few that were created before before EIP 161  but we agreed on some call sometime ago that during the conversion those accounts will be deleted. So yes then we will be sure unless a new mechanism gets introduced of course that will be able to create those new accounts. My understanding is that no we cannot  we cannot create new empty Accounts at this time or in prague. 

**Stokes** [50:01](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3001s): Okay Lightclient would you have do you have some things you'd like to bring up around Pectra scoping.

**Lightclient** [50:11](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3011s): Yeah I mean I feel like we are we go through phases of being heads down focused on forks focused on devnets but there are these things that don't have strict like devnet deadlines. That don't have the strict hard Fork deadlines which are important. And we aren't discussing them that much and I'm just like hoping to maybe get some more clarity from other client teams about where these things stack up in our priority list. I think history expiry is something that is super important and we talked about it at the interop and it felt like we wanted to move forward with it and I haven't really seen a lot of work or thoughts or progress on that since then. So do we need to like start implementing a portal like what's the next step here should we have a call where we have updates about what we're doing and try to do some Devnets like. I really don't know. And another thing that I think is not being talked about really at all that is important is that if we're going to be doing peerDAS and increasing the blob count and pectra some Fork soon after. Then we need to have a better idea of how to deal with blobs in the public transaction pool because we don't want to just two or three x the total blob count and do nothing for the public MemPool because then the public mempool will eat away all the bandwidth improvements that we got from peerDAS. So these are things that I think we need to yeah and Marius right we also need to revamp some things if 7702 goes in as it is. So there's a lot of stuff that we need to be working on and we're just talking about like surface level EIP is going into pectra. And so it would be good to hear when people want to start talking about these other things and when we might expect some of these things to be updated. I see everyone is very excited to talk about these topics.

**Lukasz** [52:36](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3156s): So Lightclient we  are experimenting with portal Network integration. We have a developer working on it at the moment but we'll see how it goes it's like a experimental research right now.

**Marek** [52:55](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3175s):  Okay I'm about Ira exports import we are working on it as well. So generally we are working on History expire. 

**Lightclient** [53:07](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3187s): Sweet how can we like surface more of the work how can we I like I feel like this is an important priority
and I think most other people agree it's an important priority but I don't think that it's receiving the same attention at least on this call as if it were going into a hard fork. What's a better way to make sure that the progress is being surfaced and that the progress is like sort of being forced for better or worse. We do have a bit of a call driven development cycle and maybe that just means that we need to talk about our progress on History expiry every All Core Devs. I'm not sure if people have other suggestions. 


**Marius** [54:01](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3241s): I think my so my biggest problem was that we don't have the scope of Pectra tied down. And since we don't have this we cannot really focus on other things. Because we're still working on stuff that might go into Petra or might not and maybe it would be nice to say we stop now. We go with this spec that we have right now. We ship it on devnet 1, 2, 3 whatever and this gives us a bit bit of PR breathing room to work on other stuff as well. Once the stuff is on the Devnets it's not that much time anymore that we have to spend. 

**Stokes** [54:52](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3292s): Potus? 

**Potuz** [54:54](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3294s): So regarding blob transaction propagating  I have a general comment which is goes a little bit beyond ACD but I think it's probably a mistake to try to start looking into changes to the protocol without having all the information at hand. I sat down at a war room on a rollup of a major rollup and I saw how the gas price was spiking even though the base fee was still at one way. And this happens when you have a series of builders for example that are averaging 3 blobs per block and home stakers that are actually committing the 6 blocks transactions and we have data for that. We have data that home stakers are sending more blobs and Builders. This breaks the 1559 Market that we have for the gas that that price. So if we don't have really good data onto how this Market is working? How are the transactions are propagating?  And even how the miners are calculating the tips because we see transactions with lower tips that are getting included before transactions with higher tips then it's very hard to try to think that we're going to solve this here at the protocol level. We probably need to have more data on how the market is actually working today?

**Stokes** [56:19](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3379s):  Marek? Do you have a comment?

**Marek** [56:25](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3385s):  I want to just ask Lightclient did you guys start working on something related to blob takes pool for peerDAS or not yet? We are not working on that right now but we will start if you are exploring. 

**Lightclient** [56:45](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3405s): Yeah we haven't started any development of anything I've basically just been having some conversations with mostly with Piper since he has looked into this idea of propagating transaction within the portal Network and like as you know in the portal Network you have very light nodes who only have a very specific view of the network. And so he sort of come up with an idea of having an over basically an overlay that says where to propagate certain transactions to. And that feels like the right path at least for blob transactions where you sort of based on your node ID you know where you know  like what transactions you're going to need to keep track of. And it's I don't see a necessarily a blocker for it. I think it's something that we just have to implement and see how if it works okay. But I just don't really know like when to do it because you know we have a pretty high Cadence of pectra Devnets and adding things. And it would be good if we had a way to make room to work on this stuff that isn't specifically Fork correlated that needs to be done. And that's kind of what I'm like trying to figure out is like what is that thing because it's really nice with the EIPs because we got the devnets, the EIP numbers, the testing team, makes some tests and then we can just run it in kurtosis or we can run it on the devnet and that's like forcing us forward but a lot of this other stuff. We just these are just ideas and we just keep saying this is important but we don't make a lot of progress on them because there isn't the forcing function.

**Stokes** [58:45](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3525s): So is the answer more breakouts.

**Lightclient** [58:49](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3529s):  I mean I don't think it's just a more breakouts like I think that we need to have something at the all core dev's level. Like I think we need to be sharing updates on how things are progressing yeah probably we need more breakouts to discuss and move things forward. But I also feel like I mean it needs to basically be a requirement it needs to be something that is part of the devnets like clients are implementing the old version of 7702 because it's in the devnet 1 spec. And if we didn't have these things if it was just more free flow like we probably wouldn't have started implementing 7702. And you know we would just like start looking at this new version. And yeah you know there's a little bit of extra work that's done there but it like it is forcing us to like move things forward and it is forcing people to get the context they need to like make more informed decisions. I think right now everybody is saying these all sound great but we don't have enough context to make like really good decisions and have technical debates whether it's in a breakout here or Eth magicians. And so we need to like be building that up so I kind of feel like if we really truly want to make progress on this stuff then we need to start saying like okay here's a devnet Target that's going to have this functionality. Let's start working on some tests to make sure that functionality is working. And you know not move forward until those things happen. And I think part of it is you know even if we do have those things there's just like a finite number of people and time to do this stuff and we're like pretty saturated with pectra. So I would I would like to maybe to talk about either if not capping pectra then even reducing the scope with Petra from what it currently is. Because at this rate Pectra will not ship this year. And if it doesn't ship this year then it will ship sometime next year probably without these things like history expiry. And you know improved blob transaction propagation. So then that stuff will only start bubbling up like mid to late next year. 


**Stokes** [1:01:04](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3664s):  Yeah iPhone? 

**iPhone** [1:01:08](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3668s):  Yeah so I agree but with history expiry if it's not a hard fork. It doesn't seem like there is any pressure to get it done. 

**Stokes** [1:01:19](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3679s):  I mean yeah with history expiry like it is an eth wire upgrade. So it feels like something that we should be doing in a hard Fork like no we can do it without a hard Fork. But because we are going to bump these wire for the requests anyways we might as well bundle these things together is has been my opinion. And you know part of it is like me not pushing forward these things and like updating these specs and making them happen  but like Again part of the reason is because there's been a lot of work comp pectra instead. 

**iPhone** [1:01:53](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3713s):  Okay yeah I think given that you said that it probably would make sense to have another breakout room because I thought it would just be sort of a add-on to the nodes at least that's one of the ideas that has been going about. So it wouldn't actually affect anything to do with the normal P2P network. 

**Lightclient** [1:02:23](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3743s):  Is anybody interested in capping this per Petra or reducing the scope or up only? 

**Guillaume** [1:02:33](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3753s):  Well it's not do up I am interested in.

**Stokes** [1:02:47](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3767s):  Andrew? 

**Andrew** [1:02:49](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3769s):  Yeah  I think if we start revisiting our decisions like for no good reason then that's a bad practice. So we we've been discussing the scope of pectra quite a lot. And I don't think it's a good thing to regurgitate the same discussions again and again. I am fine with not  increasing the scope of pectra but I'm totally not fine with kind of revisiting and reducing it for all good reason.


**Stokes** [1:03:25](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3805s):  Guillaume?

**Guillaume** [1:03:28](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3808s): Yeah quick question if we don't need a fork for  EIP 4844. Why not just let people Implement like what's preventing us from letting just clients implement it on their own time like some clients might be able to have it right off the back will take years but that's fine. Is there something blocking us from?

**LIghtclient** [1:03:51](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3831s):  Well I think we need to have a eth wire protocol that says I'm not going to have that historical data because if we were to just ship it in the current eth wire protocol you're going to have very heterogeneous set of nodes where some nodes have the history and some nodes don't. But there's not an identifier in the handshake that sort of says do I have the history or not. And there's been proposals about like having an identifier this says how much history I have I would prefer to just say whether or not you have the like one year of history as like this binary thing. But yeah I think that we have to have some way of saying that. So you know it doesn't have to go into a hard Fork but like yeah if some node if geth implements it and no one else does then it's going to be harder for those nodes that are still full sinking the history to go and find that history. Because you know there will be less nodes on the network to serve it to them. 

**iPhone** [1:04:44](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3884s):  Wait I thought that if you didn't have the history you just proxy to the portal Network. So nothing really changes. 

**Lightclient** [1:04:51](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3891s):  I mean you can't really proxy to the portal Network for Network queries because the portal network isn't really designed for these range queries that the the P2P would request. It's more for if the RPC receives a request for like oneoff blocks then it could go and get that one-off block but if you're if the node request for like 10,000 headers. You're not going to want to download 10,000 headers from Portal. 

**Stokes** [1:05:31](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3931s): Marius? 

**Marius** [1:05:34](https://www.youtube.com/watch?v=58_bJD_dmm0&t=3934s): Yes this is unrelated to  the discussion that Guillaume and Matt just had but related to the discussion that we were having in the chat around the blob transaction. One thing we noticed basically today is that the there are some issues around the order in which we propagate block transactions. So what we need to do is we need to propagate the block like if block transactions arrive at our node in a wrong order. We might actually throw some of them away. And that leads to issues if a rollup sends multiple blob transactions. We operated under the assumption that rollups don't need to send multiple blob transactions per block but apparently some of them are still doing it if it might be out of bugs or out of necessity. Anyway we need to make sure that we are sending and receiving blob transactions in the same order in Months order. So that we don't throw them away in the blob transaction Port. Just an FYI to and and we are not doing that in Geth there's a bug right now where we are not receiving them in order. And so we might actually throw some of them away. So yeah this is something that we're going to fix. And it would be good if other clients also took note of this and and checked their block pool implementations to make sure that they are also only sending transactions and receiving block transactions in nonce order. And this will make block propagation quite a bit less painful because you don't need to resend block transactions all the time. 


**Stokes** [1:08:01](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4081s): Okay so there's a client issue to be aware of but then also block users should be careful about how they send the transactions as well. 

**Lightclient** [1:08:13](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4093s): Yes they  should be aware that if they are sending multiple transactions that these transactions might arrive at the at other nodes in the wrong order. And so some of them might be thrown away because we only allow nonce ordered transactions and not un geth transactions in the block pool. So that there we only allow transactions that have no nonce cap. In the block pool not in the normal transaction pool it's fine but in the block pool it's not. 

**Stokes** [1:08:57](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4137s): Right I mean I guess how would you know as a roll up or like you know let's say I'm making a blob like I might not necessarily know that there's a nonce cap somewhere else. 

**Marius** [1:9:11](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4151s): Right. You should know it because you know which which nonce to put into your block transaction. So you know that there was a nonce cap to the current state if you have.

**Stokes** [1:09:28](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4168s): Okay but that kind of implies I need to either only make one transaction at a time like I essentially have to wait for if I make a transaction I have to wait for it to be included right. I can't make like 3/4/5.

**Peter** [1:9:41](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4181s): You can actually make multiple transactions just that. So what people kind of tended to do is basically wait a couple hundred millisecs between sending them out. So that the previous one has time to propagate in the case of blob transaction it might take a bit more it's definitely something that we will attempt to fix in geth but it's still. So the problem is that the transaction announcement protocol is very dumb it just says that hey here's a hash and you do whatever you want with it. So what we can do in geth we can make sure that we download a nounced hashes in the order that we have received those announcements but we have absolutely no idea what those hashes belong to so we don't know what order we should download if we have I know 3,000 hashes which one of them are I mean okay we know which one of them are blob transactions because we also include that but we don't have the nonce we don't have the accounts. So we can't actually prioritize or sort downloading the blob transactions in order. So even if we we take care to do a better job in keeping the the a announcement orders that we see the hashes in there's still no guarantee if some other client announces them in a bit yolu way so Geth does take care not to announce them gapped or out of ordered but we can't really rely on other clients doing the same thing. So there's always there can always be some weirdness there. But that's a that's a whole new
can of worms as to what could be done with the transaction propagation to make it more stable. 

**Stokes** [1:11:30](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4290s): Right yeah I wonder if you could just include the nonce along with the transaction announcement.

**Peter** [1:11:36](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4296s): I mean the thing is you need to include nonce and then you need to include the account but the problem is that you cannot really verify it until you download it. So I mean it's still somebody can still feed you feed basically I can just watch what kind of accounts are announced on the network. And just try to clash with fake announces and fake addresses. So it's like it's kind of hard to make anything that's really robust. 

**Stokes** [1:12:05](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4325s): Yeah that makes sense. Potus do you have your hand up from earlier or was that resolved.

**Potuz** [1:12:16](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4336s): Just wanted to mention that that batch posting on a roll up is quite complicated and you change tactics on the run as other rollups also are changing their tactics. If you're posting batches at six blobs per transaction and you see that none of your batches are being posted because some rollup is posting and paying more and posting only one blob. And then the Builder cannot include a transaction with six blobs because they already have that one blob there  then rollups start like resending batches with less blobs. So I'm not saying that geth should do this or do that but definitely there aren't that many users of blob transactions today. Okay and those are the guys that are being affected and rollups are being forced to try to talk to the relays to see how are they going to get their transactions to the Builder because the mempool, the public mempool is not getting those transactions to the Builder. So this conversation should be happening with the rollups and not among ourselves only. I feel like there's this thing that geth is doing something to protect the mempool and I understand I mean there's a Dos attack there but then on the other hand there's the users they darn that many users and they have their own problems into and they they try to adapt to whatever geth the size of the mempool should be. And this conversation should be happening with them.

**Peter** [1:13:40](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4420s):  Yeah it is fair. I think we would be curious to know how rollups operate I mean how they send their transactions and what they would like support and not supported. So I think that's a perfectly valid. We're open to that. But again I don't think it's fair to say that  Geth needs to do this. I think basically all ELs needs to be aware of these and do it properly.

**Marius** [1:14:15](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4455s): I also don't necessarily agree that we  we need to talk to the rollups. I think it's kind of we are not providing the service that we are claiming and so we need to fix it it's not really yeah like we  should do something about it and we are going to do something about it but I just wanted to mention that that there is some issues there.

**Peter** [1:14:46](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4486s): Yeah for sure so this is something that that affects the the normal transaction pool too in a bit so it's
it's an issue we're going to fix it but I'm not entirely sure that it's going to make too big of a difference but we can definitely see.

**Stokesr** [1:15:23](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4523s):  Ansgar, let's go ahead comment in the chat that essentially Rollups should think about how many blobs they put per transaction. If you have a transaction with six blobs it becomes this like very bulky thing to pack in alongside other blob transactions and if you go. 


**Potuz** [1:15:39](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4539s): There's a lot of literature to this this is not something that rollups have been thinking about this way before we shipped 4844. They have a lot of literature as to what is the optimum strategy. And also like depending if there's two three players posting at the time rollups know much  more than we know about how to post batches. The thing is that there's also this external constraint which is how the public mempool actually acts and that breaks the assumptions of that  body of literature. But I would say that the rollups they know much more what are the better strategies for batch posting than what we know. 

**Stokes** [1:16:22](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4582s): Maybe I mean if you if I make a six blob transaction and then there's some like Mempool issue that means I don't see it in time. You know like another rollups transaction then I just wouldn't know
right and I think if you take this to the Limit like you should actually only put one blob per transaction because that's the most flexible way to pack.

**Peter** [1:16:45](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4605s): So another thing that I think people need to be aware of is that six blobs means 1 Megabyte of data what is it one megabyte but maybe a little less. But essentially that's a huge latency to to propagate over the entire network. So yeah it's kind of we're entering in this weird territory and there's also this talk that people would like to even further increase the capacity of block transactions. And blocks but yeah I mean it's probably not really super healthy to create transactions that are that heavy because they just strain everything through the entire Pipeline and then weird things start happening. 

**Marius** [1:17:43](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4663s): So your suggestion would be to increase the maximum number of blobs in a block while keeping the limit of blocks per transaction the same or something like this?

**Peter** [1:17:58](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4678s): No I'm not suggesting anything I'm just saying that it's it's another dimension that people everybody needs to be aware of that latency starts to play a role here. 

**Marius** [1:18:12](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4692s): Yeah but I'm suggesting this now that we should think about whether we want to limit the number of Blobs per transaction with a different limit the number of blobs per block. 

**Peter** [1:18:31](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4711s): I like a limit of one. Okay Alex? 

**Stokes** [1:19:06](https://www.youtube.com/watch?v=58_bJD_dmm0&t=4746s): No. What? Yeah I just going to say that. Yeah it looks like there are plenty of open issues with Blobs. So yeah everyone keep thinking about it generally the the feature and Market is immature. So you know we'll work out these Kinks as time goes on. Is there anything else we have a few minutes left on the call. I don't think there are any other agenda items for the day. Okay let's go ahead and wrap up then. Thank you everyone. 
  

 

## Attendees 
* Jochem  (EthJS)
* Stokes
* Mikhail kalinin
* Marius
* Iphone
* Ansgar Dietrichs
* Toni
* Pk910
* Guillaume
* Pooja Ranjan
* Marek
* Mario Vega
* Hadrien
* Ignacio
* Andrew
* Barnabas
* Mercy Boma
* Somnath (Erigon)
* Zarathustra
* Katya Riazantseva
* LightClient
* Daniel Lehrner
* Enrico Del Fante (tbenr)
* Hasiao-Wei Wang
* Trent
* Ignacio 
* Andrew Ashikhmin
* Frangio
* Mehdi Aouadi
* Karim T.
* MERCY Boma Naps-Nkari
* Lukasz Rozmez
* Julian Rachman
* Francesco
* Amirulashraf
* Zarathustra
* Gazinder
* Dave
* Tomasz Stanczak
* Ayman
* Roman
* DANNO Ferrin
* Fireflies.ai Notetaker
* Owanikin
* Peter Szilagyi(Karalabe)
* Ahmad Mazen Bitar
* Terence
* Dmytro B.
* Elias Tazartes
* Hangleang

## Next Meeting: Thursday July 18, 2024, 14:00-15:30 UTC









