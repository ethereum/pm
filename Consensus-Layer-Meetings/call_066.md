# Ethereum 2.0 Implementers Call 66 Notes
### Meeting Date/Time: Thursday 2021/06/17 at 14:00 GMT
### Meeting Duration: 47 mins
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/222)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=ZSMrxG1LAck&ab_channel=EthereumFoundation)
### Moderator: Danny Ryan
### Notes: David Schirmer
## Action items
| Action Item | Description | Video ref |
| ------------- | ----------- | --------- |
| **1**   | Client Updates | [1:00](https://youtu.be/ZSMrxG1LAck?t=55) |
| **2**   | Altair Planning | [9:55](https://youtu.be/ZSMrxG1LAck?t=589) |
| **3**   | Spec discussion | [17:32](https://youtu.be/ZSMrxG1LAck?t=1056) |
| **4**   | Research Updates | [33:59](https://youtu.be/ZSMrxG1LAck?t=2039) |

## Decisions Made
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
| **1**   | Testnet Fork TBD | [34:54](https://youtu.be/cgH8OsCg9tY?t=2101) |

   
## Client Updates

**Danny** 
- let's go ahead and get started thank you alex for recording locally, sorry that i am tethered to my phone. here's the agenda nothing crazy client updates with a focus on altair um we will discuss the point brought up by Adrian today on some of the subtleties on um gossiping sync signatures we'll talk about altair planning um thank you for perry for joining uh to help us discuss and coordinate that and then general discussion uh the merge call was right before so i think we got all of that out of our system but i think proto might have a quick update on sharding on the research and uh we'll leave other stuff there at that point let's go ahead and get started how about teku kick us off.

**Teku** 
- sure so we've updated to the alpha 7 release with the new gossip message id changes and the new rewards for sync committees that's all up and running we've kicked off euronpili testnet with that so the details are in the ETH2 test nets repo. Prefixes to the node health API to make it work a bit better in particular for us we now say we're syncing on that api right after startup until we found peers previously we had no peers so we had nothing to sync say hey we're in sync because we don't know anybody yet um so we're actually exposing that startup mode now through that api. Tthat is the main thing we've got a lot of fixes for discovery that have come out and a few tweaks to our gossip stuff  mostly that's just particularly specific stuff but a lot of learnings out of the previous devnet's variety i think that's us.

**Danny** 
- Thank you and thanks for putting up the new devnet, prism.

 **Prism**
- Hey guys Terence here so um we aligned to alpha seven passing spec tests we're working on the new validated rpc endpoints mainly for the sync community stuff and uh almost done with that and then we're also working on the networking spec and that's almost done as well so we're almost there i think we're on track to start a local interruption test net to test the for transition um by end of this week or early next week and if that goes well we will um jump into the multi-client test net with you guys as well and uh on the maintenance front um we are planning to release our e2 API support by nextrelease so that's very exciting and uh other than that just bug fixes and then yep that's it thank you.

**Danny** 
- Great i'll hear the progress nimbus.

**Nimbus**
- Hi Mabi here so on the altar front we also updated to alpha 7. besides that we still continue working on optimizing nimbus and we made a contribution to significantly accelerate everything that requires public keys from the database by not compressing the public keys and we also improved state cache besides that we are working on the validator client we have a PR sitting there and we manage to control lighthouse with numbers validator client so we are in good shape and in parallel to that we are also adding more and more api endpoints to be in line with the f2 API requirements.

**Danny** 
- Great thank you, load star.

**LoadStar**
- Hey so on the alter front we are still on alpha six we're in the process of upgrading to seven but we've been fixing various performance issues and stability issues that we have come up just either during our own internal ephemeral test nets or trying to interrupt with techus devnet as of right now it looks pretty good locally we need to upgrade this alpha seven and see see what it looks like other than that um i've been doing some other optimizations and things we we're going to delete our pending at the station cache because we've found out it's not very dos-resistant and looking for feedback or ideas how to actually implement something like that we stopped updating our fork choice head on every call and now instead we're caching that result and then updating it only after processing every block and then as far as like publishing load star we've we pulled out our api client into a separate package which is pretty nice just to be able to you know query a needs to endpoint pulled that into a package and published it and also pulled out our liteclient prototype into a package and we started releasing nightly builds and integrated all that into our docker system so yeah.

**Danny** 
- Nice and on the lite client has the prototype primarily on the server or on the client itself? 

**Loadstar**
- It's a client that talks to a beacon node he's over like the rest api with a few additional pieces for sending over updates and proofs.

**Danny** 
- Gotcha, thank you and lighthouse.

**Lighthouse**
- Hello everyone Paul here so with regard to altair we've got alpha 7 merged into our altair branch it's working well passing tests we're following euronpili we seem to be getting sync committee messages we had a couple of issues with the new configs but we sorted those out and kind of yeah it seems to be working out we're looking into it to try and find some bugs and weirdness which i'm sure we'll find we're also without today we're patching an issue with our bc we had some some problems about signing just around the fork boundary so we're going to fix that we're still finishing some committee caching stuff and then we'll be working on merging our alter branch into our primary branch at some point out of altair now last week we released version 1.4.0 and it went quite well which was nice we dropped our memory from like six gig to like 1.5 gig dropped calls to f1 nodes by about 80 and the users seem very happy so which makes us happy and moving forward we're going to be pushing forward with altair and hopefully cutting a version 1.5.0 release maybe end of this month starting next month we should have some cpu savings and a bunch of other features.

**Danny** 
 - Excellent thank you on this recent devnet adrian did it do the transition or did it start from altair?

**Lighthouse**
- I did the transition there was some of the confusion i caused for lighthouse it's an epoch 20 because i forgot to enable it as we pass through epoch 10 when it's first going to happen features are great until you forget to set them.

**Danny** 
-Okay so you missed where you intended and then switched it to 20. 

**Lighthouse**
- Yeah so that's that's gone through the transition um which the previous ones did as well for just a deep octane.

**Danny** 
- Okay great good to hear that let's actually do planning and then we can talk about the sync committee signature broadcast time in cache okay so we're making progress adrian thank you i think posting these devnets up and doing some initial interop is invaluable um i think that most of you have met peritosh perry who is at the ef um who does primarily e2 DevOps related tasks so you've probably run into them with test nets and other things perry's going to be joining our calls here and getting his hands dirty with um various test net things so helping set dates helping pick and host configs and that kind of stuff and then
maybe uh working through problems if they arise like hitting epoch 10 and forgetting and then uh changing its epoch 20. uh perry do you want to do a quick intro to yourself.

**Perry**
- Yeah hi like danny said my name is just call me perry and i'm just looking forward to working with all of you. 

## Altair Planning

**Danny** 
- I think the the steps obviously look like short-lived devnets some longer live devnets and then picking dates on our two test nets and picking a date aka epoch on mainnet in terms of i think we'll do iteration on the short-lived devnets Adrian and or Perry you can maybe pick and host another one or two over the next week or two if that seems valuable and then what's the current temperature on earliest for one of our large test net forks is that a two week target is that a four week target.

**Adrian**
 - Is in something like pm on or prada yeah i would i would think that two weeks is probably too early just looking broadly i'd be definitely more in a four-week kind of bracket given those two options.

**Danny** 
 - Okay so and i think that's where i would fall on that as well Terence did i see you on mute.

**Terence**
 - I share the same sentiment as paul i would say between two to four weeks likely didn't was worry because i prefer more like local interrupt testing or small scale testing before that.

**Danny** 
 - Okay so we are two weeks puts us at the first july four weeks puts us at the 15th of july so let's state the intention of continued interrupt short-lived devnets and maybe keep on running once a bunch of people have joined it and do some testing just centering random transactions and things like that on the first which is two weeks the intention would be to set a fork date for one of our large test nets maybe in the two-week time rise and after that so heading towards the 15th of july and maybe if we're comfortable at that point setting some targets for a main net fork it very well we might get to the first be comfortable setting a test net fork but then wanting to regroup on the 15th which would be another call before we actually maybe we'll the intention would be to fork one of those then to get to the 15th and then set fork targets for if things had gone well forked targets for the other test not in for maine at that point i think definitely in the august early mid-august horizon for an earliest main network does that all sound about what we're thinking in terms of this is reasonable targets this isn't too aggressive but will keep us moving.

 **Adrian**
- Yeah i think that sounds about right i think the the key thing we need to get onto now in terms of talking test nets is getting users used to the fact that it's coming and coming fairly soon and they will have relatively short notice to upgrade because otherwise it's going to go very badly when the chain splits.

**Danny** 
- Yeah and we can i guess once once we pick a main net target i think we'll probably do a minimum from announcing that to the main net launch of four weeks i think is is what is the minimum given often on forks on the other side of this thing i will write a blog post for target release monday making it very clear that this is coming and also talk with some of the easttaker folk to make this is that to make sure that they've begun discussing that within their community as well.

**Medi**
 - Sorry just a quick question to everyone here is every team comfortable with us starting to report bugs crashes that are related to the consensus state transitions of altair? so i'll ask the question differently perhaps who's not ready yet to receive crash reports?

**Unknown**
- That they would be confidentially confidentially disclosed is that right midi?

**Medi**
 - Yeah absolutely absolutely we'll usually pick one or two people from each team and the us with them directly and disclose those five things directly also usually inform danny and paul proto of those.

**Danny** 
 - Right because there's a chance that something that crashes altair might be able to at least in a similar vein crash mainnet?

**Medi**
 - Potentially yeah exactly that's all right i'll take it as uh you guys are happy for us to disclose some of those bugs so yeah might get a message for me over the next few days.
  
**Unknown**
 - I had another question are teams thinking about doing like a quick audit just for the date that you guys have for altair?

**Adrian**
- This is something that i've thought about but haven't formally made a decision on so i don't i'm thinking about it i'm thinking about thinking about.

**Danny** 
 - It's not that this is correct but it's certainly not done on a per fork basis for most eth1 mainnet clients and that's not saying again that it is correct but they rely heavily on testing and test nets and assume that their architecture is generally correct and that they and those processes are the things that are going to best find consensus bugs which is probably true from a two week audit perspective but extra eyes is never a bad thing. if you do intend to do that you need to knock on somebody's door immediately as you're all probably well aware auditors are extremely backlogged.

**Unkown**
- Yeah fair you it's just a thought.

**Adrian**
- Yeah realistically i don't think it'll probably happen before the target thing.

**Danny** 
- On that front we've actually oh go.

**unknown**
- I was gonna have to respect an audit.

**Danny** 
- On yeah you've been looking at it right?

**Unknown**
- I have I love spending bugs and things.

## Spec Updates

**Danny** 
- The spec is not up and audited the spec was audited to some extent quite a long time ago at the phase zero spec freeze i will note that about 10 maybe 20 times the amount of issues and bugs were reported outside of that audit process than from that audit process. Okay adrian would you mind discussing the introducing the issue that you brought up this morning?

**Adrian**
- Yeah so uh in the earlier test nets we found that we were losing gossip messages basically the inclusion rate for sync committee signatures has been really low with the message id changes that jumped up to about 70% inclusion rate but we were still missing a bunch and it turned out that it's because the network was functioning really well so we were producing a block every slot and then immediately producing a sync signature and for both nodes actually in the network they were managing to process the sync signature before they actually imported the block and so they wound up ignoring most of the signatures and it's just the same race condition we've seen with attestations if you publish them when you first receive a block and other nodes don't have any caching say for later type behavior you get this race condition between the block and the the sync committee signature or the app station actually being ready causing causing you to drop some i've run an experiment this evening with delaying producing sync committee signatures to the four second mark in the slot and we're not getting 100% participation yet but we're missing entire subnets at a time so i think what's happening is that we're randomly not getting an aggregator and to do one more log message to prove that but i'm pretty sure that we're actually getting perfect inclusion rate of signatures now and we just sometimes don't aggregate. So essentially that that delay solves the problem and we now just need to have a choice between whether i think there are three proposals on the table one is just don't publish signatures early when you get a block always wait for the four second mark the other was that we introduce a cache so you hold on to signatures if you don't have the block they're pointing to until the end of the slot and the third was yes x suggestion that there's a random delay after you get the block between i think a quarter of a second and a second. There's a bunch of arguing over semantics but i think i think we just picked one of those really and many of them are probably.

**Danny** 
- My gut would be to go with the second and introduce a short-lived cache so that you can kind of have the dispersal of attestation messages not all being blasted exactly the same time and reuse the mechanism that protects attestations from from having the same issue obviously the cache i think should be much more short-lived on the order of slot rather than i think on the order of an epoch and we get to ideally reuse kind of the the similar logic from that structure.

**Adrian**
- Yeah i mean that's the way i lean as well partly because i already have the attestation case so i can plug it in relatively easily for any client who doesn't do that yet that's obviously more work so that's a consideration and it just feels it's a deterministic solution you are never going to reject a signature because you don't have the block yet 

Is it possible to build a dos resistant case? 

**Adrian**
- Well i think so because you've got at most you're going to hold it for 12 seconds and at most you're going to hold 512 signatures because you ignore anything that's not from this slot and you ignore anything that you've already seen from that validator

**Unkown**
- But you can get can't you get non you can't always verify the signatures of the things that you put into that case is that is that true?

**Adrian**
- That is probably true. 

**Danny** 
- Why can’t you verify the signatures?

**Adrian**
- You may not have that before 

**Unkown**
- Well if you don't have the block you don't have anything yeah that's right yeah so you the block roots you in in a fork and therefore shuffling.

**Danny** 
- Right but there's shuffling i mean the shuffling's on the order of a day.

**Adrian**
- That's true you could just try and verify it against your head and you'd be right 99.9 percent of the time yeah.

**Danny** 
- I mean if you're rejected on a sync committee shuffling you're like on a way different fork and you can probably drop it.

**Unknown**
- Yeah i'm not saying the case is like definitely a bad idea i think the delay is also a good idea because i mean i get somewhere else but if if we know that we're going to have to cache these things then why make every node on the network k-ship rather than just the sender hold it for a little bit more that's that's one argument and then another argument is that if we just have some delay then you can get by without a cache and if the cache isn't a perfect case like in this case we can't always verify the signatures going into it then there's like you know the case isn't a perfect deterministic solution and we already have this problem with attestations like i think most times at the start  of it how do you make the attestation case DOS resistant you can't same with this one you can't so i think i'm not saying the cache is a bad idea but i'd probably say delay it and cache it.

**Danny** 
- Um so i'd argue that the this cache is a lot more dust resistant than the attestation cache because of the way the mean the current committee's been known for like an entire day before it becomes the same committee so it's almost certainly finalized but the then the randomness i why does the randomness look much different than this because if i wait 0.25 seconds or on a random stretch between that like what does that actually buy me because i can still end up sending a signature to somebody who hasn't seen their block yet.

**Unknown**
- I guess i mean it's probably not thinking that it's only 512 it probably doesn't earn you a whole lot but just i guess looking from like a broader network perspective you know if you're gonna you've got a message right do you does the send and you know that that every the receivers all need like half a second before they can process it to you do you hold it on the sender side or does every receiver hold it until they get it yeah i'm not sure that that's the strongest start you know but that's that's where i was going with it.

**Danny** 
- I guess but i'm also it's also network latency it's not just like the processing of the block into into the into the actual state which unless you're telling me it's like almost that's almost always the dominant factor.

**Unknown**
- Yes it's an ever-present factor.

**Unknown**
- I would add one more question which is basically that losing an attestation by and large doesn't matter i mean it'll get included somebody will have seen it and then is likely to get included anyway. how bad is it to lose this sync committee?

**Adrian**
- It's certainly a lot less forgiving you've only got one slot to get in there are fewer aggregators that might be around that kind of thing.

**Unkown**
- Would it be worse to introduce some sort of forgiveness mechanism in general i mean this was during the attestation discussions we were discussing whether the attestation inclusion delay should be increased in order to allow for more leniency on block versus attestation timing would that be an option here?

**Danny** 
- I mean it's an option it's a trade-off in terms of the optimal latency to follow the chain as a light client if you if you added a minimum inclusion delay by if it was it followed two slots instead of one slot then you'd have 24 seconds for your node to be able to follow the head rather than 12.

**Adrian**
- I think one of the things the bits of data we're missing in this is that we don't have a decent sized network that we're seeing how this actually behaves in the real world so i've got two nodes that are you know right next to each other in aws it's not really surprising they're getting the block all at the same time it's all happening very fast whereas even on piermont and prada we're seeing a much bigger distribution of when blocks arrive and you know take your publishers at a station straight away lighthouse currently drops them if it doesn't know the block it doesn't seem to be a problem our attestation inclusion rates are pretty good so on a bigger network how big a problem this is and and you know so you're not necessarily always needing to catch the signature and a lot of these questions about how likely it is to get dropped are still unknowns effectively.

**Danny** 
- I'd say if possible i'd like to solve this in the qp spec which can be done with minimal damage to moving towards spec freeze especially on the state transition side networks that have slightly different nodes on the same network that have slightly different agreement on how they're handling this case would still be able to hang out and chat with each other so if possible i'd like to solve it with one of the two or one of the suggestions that just touches the p2p rather than adding some sort of induced delay on the on the state transition side. If we want to gather more data that's i don't think it's critical that we canform on the solution immediately right now but we should probably pick something in the next five days.

**Unknown**
- So is the reason that we're not going to send them all the four second mark so that we don't pump the network and if that is the case it's only 512 messages right so and it just seems appealing to me to say just send them all four seconds and implement a cache if you want as well. 

**Danny** 
- There's multiple reasons there one would be there is this you do want attestations well propagated so that aggregation can happen at that eight second mark and so if you have the information that you need to send your message the idea is that it's an optimization to send your message when it's available like when the correctness is available and then that also is so that you can potentially get aggregated at a higher success rate but then that is also a does help stagger so you don't have message blast.

**Unknown**
- Yeah okay that's a good point so going back to the case again saying that the shuffling is known a day ahead i guess the problem that we're gonna have is if we get forks more than a day if the network goes unstable then we're going to i guess the worst thing that happens is that cache is going to fill up we're going to start dropping sync committee messages which is not too bad right ?

**Danny** 
- It is not too bad and you've entered into somewhat of an extreme scenario and lightclients might have issues then but even then even if you're not finalizing for an entire day the assuming that there was actually two forks that are deep of an entire day and that those networks are actually those partitions the network are actually communicating and not resolving that fork is like a more extremist issue in and of itself.

**Adrian**
- I think the other thing to note is that the signature has the actual validator index so you don't actually need the shuffling to be able to verify the signature anyway you do need to to do all of the validations like checking if they're in the sync committee so right you're at worst bounded on the number of validators and

**Unkown**
- Oh yeah yeah proof as well isn't it yeah yeah you're right so that does make it much easier to verify.

**Adrian**
- Yeah i mean it's still a much bigger bound but i yeah i think if you just checked yeah if you assume you're within a day that your head sync committee is the same and they don't modification get if they're not on the one your head is on.

**Danny** 
- I mean is there not a condition that says drop the message if they're not in the committee i think there might be?

**Adrian**
- Yeah there is but you can't validate that without the shuffling um but i think it would be.

**Danny** 
- Where you have a shuffling?

**Adrian**
- Yeah if you don't have the block just use your head shuffling and case  if they're in the committee and then check properly once you get their block but i think you're going to be fine yeah i mean as you say it's a extreme case.
  
**Danny** 
- I'm going to go look at how that condition is written but i think the condition is should be written with respect to what you think the head is not with respect to the message that was sent in my opinion.

**Adrian**
- That's true because it has to match your head doesn't it once you've got the block on either you don't know the parent but yeah that would be that would imply that it has to match the shuffling in your head.

**Danny** 
- Okay this issue was just uncovered a few hours ago or at least since i was awake let's continue chatting about it offline and try to aim for a p2p related solution in the next few days otherwise if we needed to get some better data on larger networks then we can take it there adrian you mentioned something as an aside that was interesting that you were not getting aggregators you weren't always getting aggregators on different subnets i believe the number of aggregators was the target number aggregator which is actually reduced and that might be an error not an error but it might not be a good thing so do you have any other data on that or should we i can look at that number that target number and probabilities and we can chat offline if you don't have any other information.

**Adrian**
- I think the key thing is to try it with a bigger set of validators i've only got two thousand four hundred so i'm seeing duplicates in the same which we're not expecting and that makes it less likely if you get an aggregator.

**Danny** 
- Okay that makes sense. 

**Adrian**
- Yeah it is definitely worth reviewing those numbers yeah. 

## Research Updates

**Danny** 
- Okay we'll flag that. Okay many other altar discussion points cool. let's remain pretty in active communication i know everyone's slightly staggered on where they're at on this but hopefully mid to late next week more and more of us are communicating on some of these small devnets let's shift into research updates does anybody have anything to share.

**Proto**
- I can share something about sharding already just that this merged call so i'm not sure if we have like research updates between altair and sharding?

**Danny** 
- No i think um sharding is probably the main thing to share.

**Proto**
- Right okay. so where are currently at is this updated sharding spec with a new state format so this makes it easier to track confirmation data and keeps it all in one place to make a merkle proof to the commitment easier um generally happy with that piece of refactoring where there is more so we're thinking of changing the way shard proposers are tasked with their their proposals. currently we split shard proposers up or we split validators up in shard committees and then out of these committees we select the proposers to keep the proposers pair shard separate for a time window of about a day and so this helps the network player but within the spec there's not really much to it and the problem though is that it adds this caching complexity and that we can these incentives on a network layer to stay on a topic for that long are relatively big and then meanwhile we have this discussion about mfe and how we should organize the the mainnet chain and we have this concept of separation of block builders and block proposers and we could do something similar on the sharding layer where it's the block builder that pays a fee for the proposal for the to get the data there and then the proposer selects a data transaction and they can select one without seeing the complete data. So we may even end up with a model where the proposers can select data can grab data they don't have to learn all the layer tools they don't have to specialize as much and then it's the builder that after paying the fee is then incentivized to make the data available by publishing it on the shard topic and so we're looking into this changing incentives how that could work. It all fits in with regard to network timing and it does clean up various things but of course by changing this incentive we need to carefully look at the change and see if it actually works and then cut already noticed one possible issue and with a possible fix and we'll just create a PR to the specs repository to further discuss these sharding chains.

**Danny** 
- Yeah another thing i really like about moving in this type of direction is that shard data transactions don't actually need to have the payload and so there's not an excess of data being gossiped around pre-selection for inclusion just kind of like the commitment to that data and proof that you can pay a fee and so i think that would actually greatly reduce the bandwidth requirements even in the event there's a competitive fee market or competitive landscape for getting data into the shards.

**Proto**
- Right then there is this discussion about firewalling mfe so making it open like flashbots i think is really good is we should try and encourage every every fellow director to participate in a way that all these incentives are even there's no validator with a lot more mfe or that has to do a lot of extra steps to specialize if there is this market of builders then those can specialize and we can firebound away from the protocol and then it's basically the data trans the data transaction that first offers the data and then later the builder publishes the data so we shift this availability problem towards the builder and so this is good for privacy since we don't have to, so it's like if we have this very critical part of publishing the data like and this is a larger piece of data on the charts if he moved it away from the validator from the consensus identity and i mean it can still be the same person but if a builder can publish this and has incentive to do this then we can just separate it out and then also we remove this the specialization need of validators so whenever there is a new layer 2 or whenever there is a new kind of depth that wants to use shard data they can just participate in this builder market instead and the proposers these are shard preposers can just keep doing their task and don't have to worry about these these kind of niche changes.

**Danny** 
- Cool proto is going to be working on a PR that highlights some of these changes soon.

 **Unknown**
- i'm thinking about the after the merge so this is like sounds like this separate block builders sounds like an alternative to the execution services right so they will just prepare the payload the entire payload for the proposer and will need to be to sign off on it right?

**Proto**
- Basically yes so there there is no combination of multiple data pieces of data on the proposer side we could try and fit at the end of it i don't think we should go into that direction as it's just much much simpler it's more minimal to this to do it this way and then the builder can still combine different tabs they can still combine data and fit it together in one block and then we're thinking of like a standard outside of the protocol but something that devs would use think of it like the erc20 like which kind of layer this lives on and we basically just need users of shard data to recognize which part of the chart block is being used for which protocol or for which application and so we need some kind of small header to say where to find data of specific tabs so it's basically a combination of offsets and some kind of ID we can figure this out at a later time we are not quite there yet.

**Unknown**
- Yeah okay so yeah for the execution service now it will not be an alternative because it just allows for building blocks but testers will have to execute the payload anyway so yeah.

**Danny** 
- This is for shard data so there's no execution

**Unknown**
- Right yeah that's a proto was just this mentioned in this separation that was recently published.

**Proto**
- Right so it is similar to the mainnet separation in a way that we do have builders like this data still has meaning it's just that the base parts called layer one doesn't execute the data but the builders will still want to execute their rollup data and sequence transactions whatever they want to do and this is separate it's a separate process from the shard proposal rule which just needs to select data and then we shift this incentive from of the availability towards the builder and meanwhile this it cleans up some of the networking some of the concerns around specialization of block building and whatnot and yeah i think we'll just start with a PR and then we can discuss more.

**Danny** 
- Sounds good other research updates.

**Unknown**
- Yes just a quick comment the the work that i showed a couple of months ago about the resource consumption of the different clients will be published at the blockchain research conference in paris in september and there will be also a poster about the network crawlers that we have been working on and talking about the new crawler we developed a new version of the crawler that can run 24/7 and gather data continuously and changing a dashboard so we are trying to release this dashboard in the coming weeks and another thing is that with paritos we finally have a first minimal set of metrics that are already existing across all the clients and we are just in the process of deciding the best nomenclature for the best names for these metrics so that we can have some first standard for the metrics across clients and that's it on my site.

**Danny** 
- Got it thanks okay any other research updates great anything else related to spec or any discussion points in general that we'd like to discuss before we close today? okay we will aim to get this p2p sync committee issue resolved in the coming days um and we also are continuing to increase test coverage for altair so we will expect a new very iterative release next week with additional tests then thank you really appreciate all the hard work and excited to see altair moving talk soon bye thank you.


-------------------------------------------
## Attendees

* Danny
* Paul Hauner
* Mehdi Z
* Protolambda
* lightclient
* Adrian Manning
* Terence(prysmaticlabs)
* Rest unknown due to recording 
---------------------------------------
## Next Meeting
TBD
