# Consensus Layer Call 106

### Meeting Date/Time: Thursday 2023/4/6 at 14:00 UTC
### Meeting Duration: 45 minutes  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/752) 
### [Audio/Video of the meeting](https://youtu.be/MrHh_jS4lZY) 
### Moderator: Danny Ryan
### Notes: Alen (Santhosh)

## Intro
**Danny**
* Okay we should be live. this is issue #752 on PM repo. This is our call 106 relatively light scheduled agenda. 
* Obviously if you have points to bring up in different categories by all means we'll get started off with Capella which I believe is just a little bit over one week from now. What's the precise date? 

## Capella [3.38](https://youtu.be/MrHh_jS4lZY?t=218)
**Tim Beiko**
* April 12th. 

**Danny** 
* Less than a week. 

**Tim Beiko**
* 22 / 27 UTC.I forget what the epoch number is. 

**Danny**
* Cool. If you were listening and you run infrastructure or nodes or validators now's the time upgrade.  Perry we had main shadow four three this morning right? Any anything to report here? 

**Pari**
* Yeah it's been looking really great so far. We had two builders on the network this time. I haven't heard back from one but the other one is producing blocks.  
* We are noticing a couple of unable to verify signatures but still looking into why besides that healthy block production or client combinations made it through. And we use main net releases for everything. We also tried a couple of the standard procedures like deposits were made. A couple of withdrawals were done with 0x0 potentials a couple with 0x1 and yeah just playing around with that sequence and everything looks good so far. 

**Danny**
* Cool. The signatures that you can't verify those are blocks. 

**Pari** 
* Those are mabu stuff. Mabus signatures I think. 

**Danny**
* Okay. Interesting. Cool. Anything else on this? Any questions for Perry? Okay thank you. And anything else on Capella before next week? Great. good work. Everyone excited to see it go through.Dan there are no scheduled discussion points for DAB this week. 

**Marius**
* There's been I something that wanted to put on the agenda but forgot.  I would like to the notify transaction type from 052,  I think it was was chosen in that way cause there were some different transaction types on some layer twos or something.  I don't think we should create the expectation that mainnet care about transaction types on other networks and  I would yeah I would like to modify the transaction type. 

**Danny**
* Yeah I on this I think it would be good to have like maybe a high bit set for non mainnet so that there's like just a different space that people could use as a standard. but yeah I see the point Ansgar. 

**Ansgar Dietrichs**
* Yeah I mean I was basically gonna echo similar sentiment. I feel like this is something where we should probably sooner than later start some sort of standardization procedure. 
* I mean ideally there should also be like non conflicting between layers but maybe we don't care so much. But  yeah it does seem like a bad precedent to set to just skip versions on main net because I mean we we can't really keep doing that so but still we should we should look into standard sanitizing this. 

**Danny**
* Yeah there is a little bit of precedent here at least in the consensus layer.  I just shared a link to domain types from phase zero. There is domain application mask which essentially just says if you're gonna use the application layer and you're gonna utilize the same signing scheme set this bit and you won't run into main net conflicts. 
* So you're not I don't does that surfaces an EIP, I'm not exactly sure but I think it'd be nice Just to send check. 

**Ansgar Dietrichs**
* Do we have specific feedback by any either letters or wallets on whether this would cause massive problems or anything in this specific case? 

**Marius**
* I have no feedback but I'm I also don't know why this was chosen this way exactly what this was chosen this way. I think it was it was some code in so maybe the everyone can team can come. 

**Protolambda**
* Yeah just the call out to any all two chain similar to the chain IDs that we are pretty much that are pretty much standardized. 
* We should do a better effort at standardizing transaction types and domains and whatnot.  I think optimism uses one transaction type soon and so those  or at least I think they use it to seven transaction types. Some more values since I'll have to check and yes on current also pre compulse. 

**Danny**
* Right.  is this this something Maurice does have a EIP PR as well? 

**Marius**
* Oh yes. It has a a a spec PR and an EIP PR.

**Danny**
* Yeah I mean I agree with not trying to deal with conflicts because we're not gonna be able to resolve it and that setting the precedent here that we just do sequential and mainet makes sense.  
* Maybe it's merge these PRs shouting to the void and see if it's gonna cause a deeper issue than they expect rather than I think merging the PR is a stronger signal than trying to just knock on some doors and see what's up. Especially considering we still have some lead time on this. 

**Marius**
* Yeah I think the only thing about merging these tiers the question like what's the status of the test nodes is is it fine to just merge it right now or should should we wait for another round of like I dunno changes? 

**Danny**
* Yeah I mean on cuz this later side we do we'd have to do a release  and pretty much the testnet we target either the current release which has GX five or than actually switch GX three as for the test net on the EIP, EL side you know I think it's more targeting to commit or targeting head so we just have to send a signal but it seems easy enough to change unless except for maybe Aragon or others that have other types of transactions that would conflict and we don't know the complexity there. 

**Marius**
* So the way I understood it from Roberto is that even Argon removed this code the remove the transaction type three that they had in their code base. So maybe it's not even an issue anymore. 

**Danny**
* Okay. So there's like potentially a little bit of coordination effort to like circle back with the that's not schedule on the side if these could go into next or the following but  seems like general agreement to plan a flag here and merge these.Anything else on this one? Thank you Marius. Other than a related discussions I apologize.
* I was traveling on Monday. I'm curious just like general state of blob decoupling networking work if that's becoming relatively feature complete or if that's still like a very active R&D for team.s

**Terence**
* I Can give a quick update. Go ahead. Sorry. Terrance - Oh okay. Sorry And  yeah I can give a quick update on the side of things. So  we were able to  implement all the gossip features. We have been working on blocks by range and blocks by route and we have successfully tested that yesterday. So that seems to be working. 
* The only thing that we don't have is back filling but I don't think that's like a test net blocker that's not take us a few weeks if not months to implement back filling. So I think like Prism can probably pair with any client right now to start testing that. So that's where we are. 

**Sean**
* Lighthouse right now we're working on like the single blob lookups and integrating that with like our pre-processing functionality and like generally in block processing. 
* I see that's the big remaining feature for us. In parallel we're trying to work on like just a testable version of Lighthouse that  could run on a local Testnet. So we'd start like actually testing some stuff. That's generally where we're at. 

**Danny**
* Cool. Was the complexity generally as expected or were there unknowns and and continued worries here? 

**Sean**
* I would say as expected so far where it's like a bit of a pain but it's not it's nothing unsolvable. 

**Gajinder**
* Load side is sort of ready to interrupt with any other client and if your MGS on the yield side is also sort of ready and what I'm currently changing in Load Star is the signing communication between Beacon and the validator to changing into block contents from the earlier independent blob and block signing. So that should anyway be ready by end of this week. 
* But anyway it's not really a blocker to participate in any definite since it's internal between load Star and validator no.w

**Ansgar Dietrichs**
* From Teku, Update from we are still in developing phase we are concentrating in the mostly on the API side for for signing plus the logic for caching and looking up mis gossip to deconstructed bundles of blob  and blocks. while we are seeing we are following the head so all the complexity of handling caching and pools of objects and then complete the blocking part. 
* Yeah we are have still work to do so we are not ready for any interrupt at the moment. 

**Danny**
* Thanks. regarding mainet any other items to discuss? Easy enough?  actually there's something on my mind on Capella. with the historic roots revamp we essentially have historic roots lists that starts at Capella.  we don't have it full and we were talking about once that it becomes fixed essentially once you finalize the shepella update you could in a future pork  have a fixed list that you can insert and essentially utilize  the new historic roots mechanism fully from Genesis.  
* That that was mentioned as a potential future item that does seem like a pretty low hanging fruit. Is there an appetite for specifying that getting that into mainnet?  it's a bit of a question as well cause I think he was eager to do so.  but is there any gauge of sentiment on that? Essentially like Left is a to-do from the last upgrade. I'm wondering we should tackle that to-do here. Okay. I'll circle back with yeah and maybe just put it up as a feature spec for discussion and then we can once it's complete decide where to insert it. Anything else on as 

**Mikhail Kalinin**
* We are with some to-do list, I am recalling something that about slash validator and the geth Beacon proposer and probably some other menos things that at some point in time we have decided probably to put into dinner. I'm just wondering I was still going to do that at least for the this get beacon proposer thing 

**Danny**
* Was Geth Beacon proposer essentially filters out slash validators in the selection process so that you end up with yeah. More full selection of blocks.  
* Yeah I mean I think there's there's probably room for a couple of small non cross layer items but they would probably need to be bubbled up very quickly.you know next time active discussion decisions soon. 

**Mikhail Kalinin**
* Yeah like probably it's not super critical thing right? So we can do it after before after the so I'm just wondering if makes sense to work concurrently or just you know make sense make more sense you know to defer it to the next one. That's my kind of question. 

**Danny**
* Yeah I mean my general answer is probably along with a major feature. If there are cleanups and minor items especially when they're not cross layer there's probably room for a couple.  
* And that we can't always push them off or we're never gonna do them. So we should refine those specs and have the conversation and if not make a more stronger commitment to them being in the network. Okay.  other discussion points on Deneb? 

## Research, spec, etc -- validator index reuse Reuse indexes with full sweep consensus-specs#3307 [21.41](https://youtu.be/MrHh_jS4lZY?t=1301)
**Danny**
* Okay.  on research spec et cetera. I did toss up a PR from Dapplion general design that he and I were discussing on validator index reuse. I brought it up not as a necessary point to decide where it goes into a fork or not but to gauge general sentiment here I've heard two argument. one is it is really nice to reuse indices and not have big gaps  or not have gaps form and from an engineering perspective but also that you know the counter-argument is you can probably handle this with some engineering complexity and not necessarily put it into the spec. 
* I just wanted to get some eyes on this and get a general feeling on if this which is a relatively minor feature  is worthwhile from the perspective of client engineers. And if you don't have comments today I just wanna bubble it up to actually leave comments in the PR. Nonetheless this will probably emerge soon. It's under like underscore features so it's not slated for but it's at least we're good at future complete for discussion. No comments. Okay. We're kind of getting to the end of the list of our agenda. Does anyone have anything else to talk about? 


## Open Discussion [23.38](https://youtu.be/MrHh_jS4lZY?t=1418)
**Chris Hager**
* I can give a quick update about what happened in 50 meth boost are relay early this week. 

**Danny**
* Yeah that'd be great. 

**Chris Hager**
* All right so let me post the postmortem here that we posted. two days ago on Monday a proposal attacker tried to steal a block from a really to unbundle and then change the transactions and propose that to make a of money. It  took slashing into account obviously and they managed to do this by standing an invalid beacon block because zero state route and at this point the beacon the CL clients they used to broadcast before volatil validate. So they really sent this block to the beacon node but the beacon node found it to be invalid so the proposal could receive the response from the relay and didn't have to raise a second block cause that was invalid and for some reason not propagated quickly enough because actually it should have been in the end they managed to re-steal a ton of money and then they turned off their validators and that was it. as a response of that we changed two things on the release in coordination with the other release as well.
* There is a get payload cut of time that is around like four seconds now that if proposers try to request late into the slot the payload won't be returned. And more importantly now the CL client that we use they use to validate before broadcasting.yeah because standard CL behavior is broadcast and then validate but for the real we really need to the cl client to validate the payload before broadcasting. But this introduces additional latency of course about 300 to 700 milliseconds for the validation before it gets broadcast. And this pushes the broadcast time of the block further out.on top of this proposal.

**Danny**
* Are you Doing full validation including the execution layer?

**Chris Hager**
* I think the CL clients do that. our really at least already validate the execution when we receive the pillar submission. I think CL clients also do that. I'm not a hundred percent sure.  but this all together and that okay. Terrance, Potuz, maybe you kept chime here. 

**Terence**
* Yeah So  since then we have provided a patch such that we don't have to do EL validation in particular the method that we are using to validate before broadcast is rather slow because it touches for choice is statements the state and the block to the db. We don't need to do that.
* So since then we have provided a patch that just does feel consensus rule validation only and that is going to be much faster. I think.  this is going to be tested right now and get installed before  before the layer is willing to just use that validation. 

**Danny**
* Okay. Yeah that's what I was gonna get at is that there's probably a lot you can carve out there to you need to do some validation only. 

**Chris Hager**
* Yeah totally. And I definitely want to have code that is as performance as it can get here to reduce latency before broadcasting.  but all things together that the proposal can request the payload a bit into the slot. Like this is like one second more and a half second sometimes even. And then the validation delay before broadcasting it pushes us the broadcast timing kind of into the slot further and we are seeing now additional amount of unusual amounts of orphan blocks.
* Tight now it's about I think for an hour up from like I think 10 a day or so because multiple releases have the issue that with validation latency and and other latencies and more aggressive orphan behavior by sale clients too that yeah the blocks they're just getting out solid that they're more that we're seeing a lot more orphaning right now. 

**Danny**
* Yeah. Question are we seeing are these because people are beginning to make their one second. 

**Chris Hager**
* I make a moment. 

**Danny**
* Sorry Chris did you say you'd be back in one moment? I apologize I missed that Yeah I'm very sorry. 

**Chris Hager**
* My kids just had an accident and started screaming. 

**Danny**
* Got it. Are you back and available or are you taking a moment? 

**Chris Hager**
* Yeah I would say I'm back Okay. 

**Danny**
* Are these due to proposers beginning the MEV Boost dance late into the slot are these often happening in relation to people who are actually beginning the MEV boost at the start of the slot? My worry is that people who have deviated from honest behavior sending a block at the start of the slot  into more rational behavior waiting to try to get more MEV are the ones that are being volunteering here. 
* And that such actors who are rational and modify their behavior will modify their behavior and make the calls earlier in the slot. So I'm just wondering if this is like an issue promise validators or for rational deviant validators?  because if it's the latter I wouldn't worry too much and they're gonna change their behavior. 

**Chris Hager**
* Can you repeat the question real quick? 

**Danny**
* Yes.  is this a problem for honest validators that are making the calls to MEV boost at the start of the slot or is this a call for rational deviant validators that are calling you know Mebu at two seconds into the slot to try to get more MEV? If it's the latter I wouldn't necessarily tune I wouldn't necessarily worry too much cuz they will tune their behavior to call earlier. 
* But if it's the former I would worry because now essentially that's showing that there is a too much latency in the comms. 

**Chris Hager**
* Yeah we are still monitoring and investigating.  yeah we will follow up with more data. I think  even for like also our clients are configured to start the flow at equals zero but there can be a numbers of reasons for additional latency. 
* Zero just bad network connection can make the get header quite slow and then already start late and then by randomness validation is a bit lower than usual. Right. And suddenly things get pushed back really far out. 

**Danny**
* Yeah yeah I understood Right? 

**Potuz**
* So perhaps you can say a little bit about this. the thing with delays even before this incident we were tracking re-orgs because not only Lighthouse but now Prism is also trying to reorg light blocks and we've been mostly successful. we'd seen some problems on slot one so where when the second slot of the Epoch tries to reorg the first block on the epoch because the first block was late then Prism has an issue in that particular situation which does happen a little bit often because the first slot of the Epoch the first block of Epoch oftentimes is late. 
* After the relay started posting this patches we are seeing much more reorgs. I mean it's it's clear now we have more more missing slots and I do suspect that unless this is changed the situation is gonna get worse and worse and the the delays they're talking about is over a second to two seconds.
* So this is essentially like a a coin flop on each block. The relayer is sending whether or not it's going to be reorg or not. I strongly advise to look in this patch that Terence say that that they're soaking because the difference seems to be between one to two seconds currently on the validation to just a hundred milliseconds afterwards. And with a hundred milliseconds I think we're absolutely safe. 

**Danny**
* Got it. And Chris you're claiming four to 600 milliseconds. Is that's just the do you have very highly resourced machines? Like when we say one to two seconds are we talking about two different types of machines here? 

**Chris Hager**
* I think it depends on what type of but general like our we seeing like four 600 milliseconds validation delay on the ultrasound maybe a bit less even but if you can get that down for 100 that would be that would be amazing. 

**Potuz**
* And You also need  to recall that I mean the the the time that makes the cut for us to reorg is not the time that we receive the block is the time when we put it in portraits which happens after our own validation. So and that's the validation on the computer of the validators not on a might not be a large computer. So even if you send the block at three seconds that takes over a second to execute. That's that's a coin flow a contest. 

**Danny**
* I do think  the providing more visibility into honest late reorgs would be valuable because I do think that a nber of entities might have begun trying to modify behavior to to get and broadcast late and that this combined with modified relay behavior is maybe amplifying the problem. 
* And so these actors will probably figure out themselves but just making clear that essentially there's a modification that is utilized by the majority of the network I think would help. 

**Chris Hager**
* Yeah I totally agree. This is certainly something that is pretty interesting and important to monitor and to keep an eye out and to think about possible ways to to mitigate them that have also as little as possible negative impact on on solar stickers by increasing just regular mis slot. 
* For instance we are if the other release I know ultrasound release also very active on monitoring their numbers and their performance and the mid slot and everything and we are working together with the other release to improve the parameters in the situation over time to collect more data and keep an eye on it.  
* There will also be more data coming out from this. Yeah. And we are working on antra hardening MEV boost flow overall and analyzing potential tech vectors that that could be possible. By the way one more thing here is that there it would be really interesting to get more security research on Boost really code based.
* There was an audited and there were a bunch of people looking at it but yeah there is maybe interest in having a more coordinated wider bug bounty program that is not not solely funded by a Flash pot but more of an industry-wide thing maybe 

**Danny**
* On specification of the proposal boost reorgs that's landed in a PR in limbo for quite a while but now you know something like 70% of the network will be utilizing it.  Any opposition to shifting that into spec even if there is a node that it's optional behavior? 

**Marius**
* It's Yeah so I'm not opposed to shifting Meth boost into the spec but I would like to make clear that this bug  wasn't an issue with Meth Boost but it was with a relayer and so it kind of fits like I don't know flash bots or the the Relay service providers have hit their users the builders and I kind of trying to pond this on everyone else. 
* So I would like to make sure  like I don't oppose doing Meth like putting the the the Meth Boost software into like the general bug bounty program. but I very much opposed painting this as something that was like in Ethereum fault or something. This was definitely an issue of these service providers and and lot of like the general ecosystem. 

**Danny**
* Yeah. Thank you. Just to clarify I was asking there's a specification point in the fork choice that's land hang out a PR that has not been merged for quite a while even though most now the majority of the network is utilizing it. So I guess there's two discussion points there. 
* One is  how to provide MEV boost with a better bug bounty  and then also secondary questions of relay bounties and other things like that.  and the other is the the for fork choice, and reorgs into specification. 

**Marius**
* Yeah again some. I think this part is like Meth is part of the core and it should be specified. 

**Chris Hager**
* And inspect out Is somewhat spec 50 specs already. What kind of like different spec would you be Thinking about? 

**Danny**
* Yeah just to make it clear Marice the builder specs are under the slash ethereum org and are well specified and well standardized and those are the maybe poorly named as I looked at it. but those are the communications with how to deal with talk to Meth Boost. So  I think that is well specified at this point. 
* Okay. On ish on Polar Press 3034 which is the late reorg specified by Michael it again seems strange that is not part of the spec at this point if that's the behavior  even if it is optional behavior. So let's do a pass on that and make consideration over the next week or two on if and how to finally put that into the spec. Okay. 
* Yeah does this is other there's a number of active conversations around my Meth boost around safe relay behavior around equivocations and other things.  so I don't think this is necessarily done but it'd be good to get the optimization in that helps with latencies and to continue to monitor.is there any any other discussion points related to this incident or MEV Boost in general? 

**Potuz**
* Yeah so there was a question that perhaps it's good to gauge here. one of the options was for clients to provide an endpoint that you would submit a blinded block and it would just tell you if it's valid or not. just by checking the consensus validity of the block. And this was our first reaction of something that we would want to to have because having the relays forking CL clients and having a prism fork and a lighthouse fork is not a good status quo and I myself am divided about this. 
* I'm not really sure if this is something that we want to have if it has to be specified or not. I initially disagreed on having this thing specified. Paul, I don't know if Paul is here but Paul seemed to agree that this should be something that we would want to have and I just want to have this discussion here. 

**Danny**
* I mean my intuition is that if we don't then there will be a subset of clients that are used by relays instead of a diversity of clients that support the behavior.  and the behavior will not necessarily be standardized or will be de facto standardized.  whereas the RPC endpoint would certainly standardize it. 
* So I it doesn't seem it seems like one of those things that if we don't do we end up in a like a worse spot.  and if we do then we're kind of like adding this very specific behavior for this use case but knowing which is a bit strange but knowing that it prevents the actualization of a bunch of strange modified behavior. 

**Potuz**
* Right. So my worry is that like by adding things that make make the situation to continue on sort like diverting us from realizing that we need PBS and protocol and facilitating the the continuation of the status quo is not something that I'm happy about. but I also agree that like having relays fork in Prism and and and trying trying on production testing on production the Prism patches or lighthouse patches is not good either. 

**Danny**
* Yeah. I guess to counter argument to that is Malbus exists and it's not gonna go away tomorrow. So there are leaving the issues to just stand there you know leads to the system in a more fragile place because that is the  practical nature of the system today and if this were a matter of like okay are we gonna do in three months because we're not gonna shore up the system then sure maybe but that's I don't think anyone's discussing timelines like that. 

**Sean**
* Wouldn't we need something like this blinded block consensus verification? I'm fine. 

**Potuz**
* If we had pbs yeah you wouldn't necessarily have It as this this would be probably some something needed for PBS So for PBS probably we will need some sort of valid validation of the block which is pure consensus anyways. So this endpoint would be Needed. 

**Danny**
* You'd need the workflow you wouldn't necessarily be using the endpoint right? Cuz you'd get that message from gossip and you'd be doing consensus things on it to decide if you need to do an attestation to that like sub-component of the block. so yes you'd need the workflow. No I don't think it would you'd need the RPC but even then that's a reasonable additional argument. 

**Sean**
* Yeah I don't know. It's like I kinda like the idea of having a separate endpoint but it's also kind of for a pretty specialized purpose then for like everyone to have to support it. Yeah I dunno. 

**Ansgar Dietrichs**
* And if I mean even if all the clients implement implemented I don't know if it is there will be only any case some super specialized logic to super optimize that endpoint because since that every millisecond matter here so does this prevent in any case having specialized fork for super optimize that one? 

**Danny**
* Yeah. Hard to say.but it at least allows the default relay behavior to pick up a client and just do it rather than having to port something.  obviously hard to say what these highly incentivized actors will ultimately do. Is anybody willing to specify the endpoint in the PR for for the discussion? 

**Sean**
* I can like in the like in the next couple weeks probably but right now I feel like I got a lot of the network on my plate. It almost seems like this should be a part of the builder specs even though at that point it sort of becomes like the builder specs are half execution have consensus. 

**Danny**
* Why is this part of the builder specs? Because this is the functionality presably a relay would be pooling 

**Sean**
* Yeah like a relay implements to build their specs to be like yeah I guess it's more of like an internal API for the relay. 

**Danny**
* Yeah I meanI think the consensus APIs is the place because it's just a it's a functionality that a particular user needs one particular use case needs. 
* You could obviously in the builder specs have some notes about the things they relay could or should be doing in between ver places in the communications. But I don't think that's where you'd actually specify the RPC. 

**Chris Hager**
* I think we should maybe consider this conversation in next week again or so because there may be additional checks that we've wanted as part of this flow too. 

**Danny**
* Yeah that sounds good. 

**Chris Hager**
* I just wanted to say thanks for everybody involved in chime in into the analysis mitigation helping chart the path forward and and keeping an of data. It was a huge team effort. And yeah also  I'm thanks for keeping this room here and I apologize that I just had a little small between unfocused. 

**Danny**
* Okay. Thank you very much.we will bubble up at least that discussion point for next week and can discuss any other updates that have come since then.let's see nothing else on the agenda today.Any other items people would like to discuss before we close? Okay, thank you!


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
* Stokes
* Sammy
* Protolambda
* Saulius
* Marek
* James
* Dankrad
* Kevaundray
* Radek
* Dhruv



