# All Core Devs Meeting 120
### Meeting Date/Time: Friday August 20, 2021, 14:00 UTC
### Meeting Duration: 1 hour 30 min
### [Github Agenda](https://github.com/ethereum/pm/issues/370)
### [Video of the meeting](https://youtu.be/rlIgpf2V4ks)
### Moderator: Tim Beiko
### Notes: Shane Lightowler

## Decisions Made / Action items
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
|120.1 | It would be good to get feedback from Geth focus group re: state sync post-merge. Any wider input on this doc is very much appreciated, before and after next week's call. Merge channel in R&D discord is best | [5.17](https://youtu.be/rlIgpf2V4ks?t=317)|
|120.2 | Would be useful for Ethereum Cat Herders to host/record next Thursday's Merge call | [10.57](https://youtu.be/rlIgpf2V4ks?t=657)|
|120.3 | 64 bit integer has been chosen to be the nonce limit | [38.50](https://youtu.be/rlIgpf2V4ks?t=2330)|
|120.4 | Re: json rpc spec, we need reviews from clients before we can complete this. Wed like volunteers from each client to be responsive to the issues raised. This is whatever the clients are comfortable with. Wed like at least one approval for each client.| [1.01.25](https://youtu.be/rlIgpf2V4ks?t=3685)|


## Merge Consensus API Design Space Doc

**Tim Beiko**

* Mikhail has put together a spec for the consensus API for the merge. Let's walk through it high level.

**Mikhail Kalinin**

* [This doc is not a proposal, it is the Design Space.](https://hackmd.io/@n0ble/consensus_api_design_space) This builds on previous work from Rayonism as well as other conversations eg EIP 3675 discussion. 
* We will start iterating the consensus API via this doc and the doc intends to be a starter for discussion. Pan is for a call next Thursday, before the Eth2 Dev call, engaging as many client devs as possible. 
* There may be things missed in this doc. It would be good to get feedback from Geth focus group re: state sync post-merge.
* Looking at the doc, firstly there is the 'Minimal set of methods' for node operation post-merge.
* Next section is the 'Transition process'. These methods and processes will be deprecated after the merge, unfortunately (is a lot of effort only to be deprecated). 
* Next is 'Extended set of features' section. This is sync related.
* Also there are sections on 'Asynchrony' and 'Consistency checkpoints' (ie what is critical for the transition process and also useful for recovery after software failures).
* 'Execution payload cache' section and some thoughts on the 'Shared execution client'
* Any input on this doc is very much appreciated, before and after next week's call.
* There is an idea from Protolamda to reuse the core set of methods for Layer 2 communication. L1 is priority but if we can re-use these for L2 we reduce complexity.

**Danny Ryan**

* Some of these methods map to black box testing in EIP-3675

**Mikhail**

* Will circulate invite to Thursday call
* Would be useful for Cat Herders to host/record call
* Feel free to comment in Github or in Discord on the doc if anyone has feedback.

**Martin Holst Swende**

* We at Geth have reviewed the doc internally. Pulling together a response. Will aim to finish ahead of Thursday call.

**Danny**

* Geth's synchronisation feedback will be particularly valuable.

**Tim**

* there's a Merge channel in the Eth R&D discord which people can feed back to if any comments on the doc.

## London Retro

[13.20](https://youtu.be/rlIgpf2V4ks?t=800)

**Tim**

* Last 2 weeks have been speaking with the client teams on how London went, and the upcoming roadmap heading into the merge.
* Have shared [findings doc](https://hackmd.io/@timbeiko/london-retro).
* Main takeaway: wasnt really clear what we wanted to see on testnets before we set a mainnet block. Forced by difficulty bomb. There was a desire to see criteria on how long we wanted to see testnets running smoothly, how long testnets needed to run for post-bug fixing etc. 
* It was felt there was lots of community pressure to launch London and this is expected to continue for the merge. As such it would be good to be able to point to a default timing path so that all are clear.
* People felt that there was a lot of pressure not to speak up when things went wrong. Speaking up would result in pushback. To help with this we should set timeframes and expectations up front for when things go wrong, that this is the clear path that will be taken.
* We need a common set of requirements for testnet forks. Eg forkmon, ethstats, transations that are ready to send which test edge cases.
* Be good to have automated alerts to alert for testnet issues. Eg ropsten issue took 4-5 hours to detect. We should have been pinged automatically.
* Delay between having consensus changes finalised and the community enacting them (eg JSON RPC changes were being made whilst the London blocks were being set). We want a wrap of all consensus changes prior to having a mainnet blocks.
* Trying to have a single place where we can highlight changes to APIs.
* Asked teams what their priority lists are for the next 6 months. How could this interfere with the planned Dec feature fork? All teams have work to do beyond just the merge (eg behind the scenes performance improvements, modularisation etc). All teams bar one said they would prefer not to have one. General feeling is that being able to focus on the merge would be very valuable. Dec fork should contain just difficulty bomb, not anything else significant.

**Martin**

* Re: consensus changes, it requires tooling providers to be active early on. Credit to Infura for being active in early testnets. Core devs lack knowledge of how changes affect individual tools.

**Tim**

* Trent has been setting up stakeholder calls which has helped. Will continue for the merge.
* Some teams feel they cant do much until public testnets have forked. Not as easy to support arbitrary devnets. Maybe its worth forking a testnet earlier in the process for the merge.
* For December fork, will setup a spec for the fork (incl. difficulty bomb). Other features will go into the subsequent upgrade.

**Lightclient**

* Are we actually targetting new features for the post-merge upgrade?
* There's been discussion that there's a cleanup fork post-merge. (Cancuun)

**Danny**

* One of the big things for the execution layer is enabling withdrawals of ETH from the beacon chain to the execution layer. This will be an EIP and involve modifications to the EVM. This will need to be considered as an example, for post-merge upgrade fork.

**Lightclient**

* Important to think about the post merge upgrades. We did say Shanghai would be a feature fork and we would push things out of London to go here, but now we are suggesting a sole focus on the merge.

**Danny**

* We currently have 5 major R&D projects for the sustainability of Ethereum. We may need to compromise to ensure we are making the right decisions.

**Lightclient**

* There should be a meta conversation on big R&D vs reasonable EVM changes. We should consider how best we can do more things at one time.

**Tim**

* Agree with that. We had a unique situation with London where EIP-1559 was a bigger than usual piece than everything else. The merge is also a completely idfferent type of thing. When things are more straightforward post-merge it seems reasonable to be doing things like that.
* We should have a broader convo on this in a couple of weeks. We should plan this in advance.

## Limiting account nonce: EIP 2681 vs. 3338

[26.21](https://youtu.be/rlIgpf2V4ks?t=1581)

**Tim**

* There were two proposals on this, EIP 2681 vs EIP 3338.
* It would be nice for clients to agree on what the nonce limit should be.


**Alex (axic)**

* See [comment](https://github.com/ethereum/pm/issues/370#issuecomment-902713690).
* This goes back 2 years (EIP-1985). We wanted to put upper bounds to a lot of fields in the EVM. Some of those upper bounds, if you put them in the EVM, you also would want them outside in the transactions. The nonce was one of these.
* We then split this into smaller EIPs. Nonce was first for which we chose 64 bit as it was the limit that clients (eg Geth) already had.
* Because JavaScript doesnt have 64 bit integers (it has floating point) then the actual upper bound is smaller than 64 bit. The nonce is predominantly used in transactions and transactions are predominantly created in JS, it would be nice to optimise for this.
* Reasons against this: 1- we dont optimise for JS in other cases. 2- JS actually can support 64 bit numbers through big integer libraries or big integer support in browsers. There are many other fields besides the nonce that have natural limit of 64 bits. Not sure if this is is just with the execution layer, or if there are other fields in the beacon chain that can be argued for in a similar way.
* I'm not sure if the nonce value piece looks reasonable as a one off piece, or if there are other fields that we could optimise for the JS script case.

**Danny**

* We only have 64 types generally outside of crypto on the beacon chain. We had this debate a couple of years ago to see if it made sense to restrict, and we did not. Most of the values are impractical to get up there, can be higher than that. I think there are some arithmatic operations that do exceed that. As such we have not restricted them.
* There are some restrictions natively in Java which may apply.

**Martin**

* I'm curious about the practical effects if we said yes today to restrict to 64, does that mean we'd update the whitepaper and those implementations who do not yet use it as 64 can/will do so? In practice they can already do it. 

**Micah**

* This change is just so that we can make stronger assertions. This change shouldnt effect any existing clients. If someone new starts with a client they will just be able to simply see that this number cant go above 64, they dont need to understand deeply nonces. Easier for new developers.

**Artem**

* We shouldnt bend over to JavaScript and that's it. Every single language has 2 to the power of 64 integer, this is a javascript problem, not everyone elses.

**Micah**

* While Im with you that this JS sucks and is terrible, its also the most dominant language.

**Artem**

* The idea of importing JS's words into the Ethereum protocol spec does not sit well with me.

**Martin**

* In Javascript implementation you can choose to use 2 to the power of 52 - neither of them will be hit in practice. It's fine to me.

**Dankrad Feist**

* Is it actually possible to do anything in JS without having 64 bit integer? Is it possible to do everything else with 52 bit integers, with it only being the nonce where it is needed to introduce 64 bit integers?? If this is not the case then this discussion is moot.

**Micah**

* There is an ergonomic advantage. Prior to big ints, it was way easier to work with native numbers because javascript doesnt have operator overloading, things can get ugly fast in the code. When youre sitting down writing code ergonmically its much simpler.

**Dankrad**

* I understand that case, but for the 5 other cases in the same code we already have to use big ints anyway, you are now optimising for that single case -the nonce. It feels wrong. The danger is to make coders lazy if they think oh I can use normal through floating point for nonce, they may start using it for the other types as well where it doesnt work which causes issues.

**Micah**

* that's fair. In my head, if either of these numbers are going to be hit, lets pick the smaller one. It covers more. I like to be restrictive in my assertions so if i know that this is never going to exceed a double or an integer packed into a double that seems like a bteer assertion that asserting that this will never overflow that.

**Dankrad**

* Im just saying that all of the other things that youre handling at the same time have the same problem then the dangers that you introduce here are bigger than what youre avoiding.

**Alex**

* Re: what happens next. The yellow paper has always just been following these changes, not making them. If this EIP is finalised then whoever is acting on the YP can adjust it.
* Another comment re: what could be done, I think we could add a consensus test if we want it which has just an arbitrary high nonce set in the state. But that could cause further issues down the line. Not sure if this is a good idea.
* Re: 52 bits, if youre a new client implementer and you see these fields are 64 bit, if you set it to 64 bit and you dont need to add extra code to check if you reached a random limit or not, since even if it went to 52 bit, GETH wouldnt have that extra clause in the code. Whoever is looking at Geth as an inspiration to implement a client, they wouldnt add the check. If somehow that case is reached then there would be a consensus bug. This seems to be causing more problems than answers that it provides.

**Tim**

* It seems like there is definitely fairly strong opinions against 2 to the 52. It feels like we should just go with 2 to the 64 because this has been open for 6 months.

**Martin**

* I agree with that.

**Micah**

* I wont die on this hill. This debate started back before JS had the big int native type and now they do - my arguments are weaker than they used to be.

**Tim**

* ok, lets go with 2 to the 64. Alex - please update the EIP status.

**Micah**

* As Alex mentioned there a whole bunch of these. Nonce was the canary we were using to test this process. Do teams want us to keep raising this to ACD? Or should we just be updating the yellow paper and make the assertion on our own?

**Danny**

* I think it makes sense for this to make its way in as a test vector. So maybe the next step is to enumerate a big list of them.

**Tim**

* Then we can have conversations on the test PR and once we reach consensus it makes sense to annoucne it on ACD but not debate on the call.

**Alex**

* As an indication of these other limits you can look at EIP 1985. That only focuses on the EVM currently but there are other fields outside of the EVM that are alos relevant.

##EIP-1352 Discussion

[41.22](https://youtu.be/rlIgpf2V4ks?t=2482)

**Tim**

* Daniel is next re: EIP 1352. [See comment.](https://github.com/ethereum/pm/issues/370#issuecomment-902040752)

**Daniel**

* 1352 is an even older EIP in line with what we were just talking about. The topic is the restrictive address range for precompiles and system contracts. A couple years ago when this was raised it got tables because it was a lot of work for zero impact. With Berlin that changed. The precompiled contracts are considered already warned when they come in. During the devnets both besu and nethermind still had the old bls precompiles in their list of acceptable compiles even though they werent executable. They were going up to 19 precompiles when the answer should have been nine, so there were consensus failures on that. 
* The reason this is important to nail down sooner or later is due to broader layer 2 type EVM systems. These other chains define their own precompiles for system level access, eg arbitrum. If you need to intiate an ETH transfer from L2 to L1 you need to call into an arcsys contract put at 0x100. When they go to berlin do they charge warm or cold gas for access? If we pass this EIP and make it a standard and say anything below 65000 four fs is the address its considered  a precompile for the purposes of these warmed accounts, its going to solve a lot of problems with layer 2s in the broader EVM ecosystem - a safe space to put their precompiles in without worrying about breaking consensus rules. Not as relevant then but very relevant now. Would like to see this in the next feature fork.

**Martin**

* I disagree. If someone makes a transaction which will create a contract on one of these addresses it shall be rejected. Thats the only technical consequence. You imply that any call made towards the 65000 adresses should be cheaper. I think that is an erroneous intepretation of the EIP. Its also a DoS vector because youd have 65000 address through which one could make very cheap lookups. This is not insignificant. I am in agreement with the EIP but I dont interpret that same things as Daniel does.

**Daniel**

* These are the conversations that are worth having. I hadn't thought of it from that perspective - that you would need to prohibit those from ever holding value and put special handling in for that.

**Martin**

* Its fully possible to send values to a precompiler - that is fine. I think weve already initialised these services, at least some of them.

**Daniel**

* Yes, 0 to 255 all the mainnets - someone went through and did that.

**Dankrad**

* The point was to avoid the DoS vector, just define their value to be zero so you dont ever have to look it up.

**Martin**

* You cannot delete they ~~garbled~~ the problem is it would not then exist in the state try and we would have this empty delete problem.

**Dankrad**

* Why cant we say the value is always zero, so you dont need to look up the state try. No value sent to a precompile has any meaning. Its burned so whether you store it or not doesnt matter.

**Martin**

* That would be a semantic change on how the try works. We could do it but it would be more trouble than its worth, due to edge cases. Things are easier if there is value on them and they exist in the try.

**Tim**

* It seems that Daniel you came in thinking this is a quick fix but sounds like things are more complicated than that. Prob makes sense to discuss this more async.

**Martin**

* Axic wrote this originally and Daniel and I have different interpretations of how to read this EIP. Axic - who is closest to the intent?

**Alex**

* I think the intent changed over time. Initially it was prob much closer to Daniels interpretation but after we have the access lists and other discussions its more like a reservation as opposed to doing much else. I agree that we need to examine the cases.
* We also discussed creation, there has to be a clear spec, what happens in the case of an unrealistic collision. What happens to the accounts which already exist at these addresses? Lastly, whether these should be covered under the warm case, the access list. If they do then we definitely need to do something - these shouldnt result in 3 lookups. Lastly the range was also debated, started out as 256 addresses but Nick Johnson asked to be extended to 64k. This seems interesting to discuss but too early to make a decision on this call.

**Daniel**

* I wasnt planning to get a decision on this call, just to raise the discussion. Should we move this to ethereum magicians thread? Its about 2 years dry. Or should we start a new thread.

**Alex**

* Revive the thread! Maybe a call too?

**Micah**

* Is anyone opposed to clarifying the EIP so that we dont make any claims about warming and agree just on reservation only and in the future progress warming.

**Daniel**

* Warming is where this has a mechanical impact on chains that may consider their system contracts to be precompiles or not. Within mainnet itself, youre right, it doesnt matter. Im hoping to get some more clarity as to how the other chains should treat it for the broader EVM ecosystem. I think we should carry on the discussion. We need some forethought because people are making decisions based on this before we fully understand the impacts.

**Micah**

* Is your view that this EIP is not worth championing unless we can make assertions about warm vs cold?

**Daniel**

* No, but I feel the EIP should be updated to clarify the current reality. As of today it doesnt really have much of an impact. It needs to be updated. I think this is the correct venue to talk about it. I think theres value even if we dont do warm/cold, maybe we say that non mainnet chains dont get to warm up their precompiles.

**Tim**

* Continue this on the existing eth magicians thread.

##Announcements

[53.12](https://youtu.be/rlIgpf2V4ks?t=3192)

**Tim**

* Two announcements by geth. [eth/65 deprecation](https://github.com/ethereum/go-ethereum/pull/23120) and [EIP-3607](https://github.com/ethereum/go-ethereum/pull/23303). Can someone give overview? 

**Martin**

* We are dropping eth/65. Couple of hours ago we put it back. Since were doing a hotfix release on tuesday, if we were to suddenly make the entire geth population drop eth/65 then nethermind would no longer have anyone to speak to. We reverted the drop with the emergency release we are going to drop it again. Has been on the roadmap for a long time.
* Re: the other check, yes we have added a check that an assembler must be an EOA. It must not have an encode.

**Tim**

* To clarify, the eth/65 bit - this will not be in tuesday's hotfix release. 

**Lukasz**

* Quick update on those two things. Nethermind have the implementation eth/66 in a branch. We are testing it, looks fine. We have one hive test failing and are investigating at the moment. Expect to be eth/66 ready as soon as next week.
* Re: 3607, we have initial implementation that we might release next week or week after.

**Tim**

* Any besu updates?

**Gary Schulte**

* We have an eth/66 PR thats up right now. Will be fast tracking in light of eth/65 being dropped. Havent looked at 3607 yet.

**Marius Van Der Wijden**

* Re: 3607 we noticed that... -disconnected-

**Martin**

* Think he disconnected. What i think he was going to say was we noticed that theres an edge case where a sender might not actually exists due to zero gas price. That should be taken into account with this check.

**Tim**

* is this referenced in the EIP?

**Martin**

* yes is refd in the discussion. A test will be made for this.

**Marius**

* I would add that if you implement this in the basic way without taking into account ethcall, you would break legacy gnosis wallets. You should not require the check in ethcall.

**Lukasz**

* question about 3607... are you implementing this like normal eip switch from a block number or are you assuming from block number zero?

**Martin**

* from zero.

**Lukasz**

* okay from block number zero. We need a little bit more analysis on this.

**Tim**

* thanks for sharing!
* Thats all we have for the standard agenda, further annoucnements...
* Geth has a hotfix to address a security issue on tuesday. Keep an eye on this if you are running geth.
* Secondly, Alita has been working on the [json rpc spec](https://github.com/ethereum/execution-apis/issues/56). There are a couple things where they need clients to review certain PRs. Context?

**Alita Moore**

* Jared's been doing most of the writing so I'll let him speak on this.

**Jared Doro**

* Ive a few more drafts to finish up, should have them all done today. Just need review on wording and behaviour review. Exist as individual PRs, but should I put them all in one file for easier review?

**Alita**

* currently we have a few markdown description files which contain the edge cases. We need reviews from clients before we can complete this. Wed like volunteers from each client to be responsive to the issues raised.
* This is whatever the clients are comfortable with. Wed like at least one approval for each client.

**Tomasz**

* Great work from alita and jared. Lots of effort put into prep and writing.
* Every client should review this and comment.
* These edge cases keep causing trouble for integrators.
* This is a good time for the community to step in and look at the edge cases as well. Would be great to tweak the list to see what kind of feedback we can get that would help.
* This is an important project to complete.

**Martin**

* think its great that this has been worked on, but if it gets put down into text we are losing a dimension - reference tests for json rpc. Im afraid this will wind up forgotten.

**Alita**

* the plan is to do both - to have both descriptions and unit tests. Would that address your concerns?

**Martin**

* Yes! Thats great.

**Tomasz**

* We can address the exact look of it at the end, but right now we need feedback. This has been discussed by the geth team.

**Alita**

* every edge case that you see in the PR has reference data that weve collected. Its going to be trivial to turn them into unit tests. Reviews now will help us ensure we have all of the data we need.

**Tim**

* thanks for sharing, hopefully we can get people looking at this next few weeks. I'll also link on twitter.
* We have two more announcements... over the past week weve been renaming github and discord channels - eth 1 to execution layer and eth2 to consensus layer. With the merge coming we want to get terminology consistent. This is why these may be renamed. [Doc linked](https://notes.ethereum.org/@timbeiko/great-renaming) in agenda.
* The ddob team has spent some time in past month doing an analysis of the impact of charging gas for code chunks using verkle tries will have. If use this as part of the etheruem statelessness roadmap theyve put out a report addressing impacts on current smart contracts. There also [a call next Friday](https://github.com/ethereum/pm/issues/377), 1 hr after ACD for them to share the report and for people to discuss. Reach out to me for the calendar invite.
* Any other points to raise?
* Thanks everybody!


-------------------------------------------
## Attendees

* Tim Beiko
* Mikhail Kalinin
* Danny Ryan
* Martin Holst Swende
* Lightclient
* Alex (axic)
* Danno Ferrin
* Lukusz Rozmej
* Gary Schulte 
* Marius Van Der Wijden
* Jared Doro
* Alita Moore
* Tomasz Stanczak
* Pooja Ranjan
* Ratan Sur
* Greg Colvin
* Trenton Van Epps
* Marek Moraczynski
* Ansgar Dietrichs
* Bhargavasomu
* Guillaume
* Sam Wilson
* Artem Vorotnikob
* AlexLG

---------------------------------------

## Next meeting on: September 3, 2021, 14:00 UTC
[Agenda](https://github.com/ethereum/pm/issues/379)