# Execution Layer Meeting #176
### Meeting Date/Time: Dec 7, 2023, 14:00-15:30 UTC
### Meeting Duration: 1hour 
### [GitHub Agenda](https://github.com/ethereum/pm/issues/910)
### [Video of the meeting](https://youtu.be/5KMvtxiSbow)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 176.1 | **Devnet #12 Updates** Testing for the Cancun/Deneb upgrade is well underway on Devnet #12. Parithosh Jayanthi, a DevOps Engineer at the Foundation, said that bugs have been discovered in two clients, Reth and Lighthouse, so far. Both client teams are in the process of patching. The DevOps team is focusing more testing efforts on the MEV workflow by activating MEV-Boost software across more validators on Devnet #12. Jayanthi said that his team has found at least one bug in the Flashbots’ MEV relay implementation. Danny Ryan, an Ethereum Foundation researcher, stressed that additional tests will be needed to check the fallback mechanisms for validators to local block building in the event of relay failures.
| 176.2 | **Devnet #12 Updates** Moving on to client team specific upgrades, Terence Tsao, a developer for the Prysm client, said that his team is working on the revamped design for blob propagation discussed on ACDC #122. Tsao affirmed that the Prysm client will be ready to join Devnet #12 for testing next week, potentially the week after next. Justin Florentine, a developer for the Besu client, said that Besu is ready to move on from Devnet #12. Representatives from the Nethermind, Erigon, Lodestar, and Teku client teams echoed the same readiness to move ahead to testing the upgrade on public Ethereum testnets
| 176.3 | **Devnet #12 Updates** Based on client readiness, Beiko recommended coordinating a hard fork date as soon as developers return from the holiday break. Assuming no major bugs are discovered in clients on Devnet #12 in the coming weeks after the addition of the Prysm client, Beiko said Cancun/Deneb activation on Goerli could tentatively happen some time by mid-January. Ben Edgington from the Teku team asked developers whether they were confident about the change to target blob count per block from two blobs to three. Ryan suggested additional testing for the increased blob target on a large-scale shadow fork and during Cancun/Deneb activation on Goerli. Beiko affirmed that upgrade activation on Goerli would be “the last significant test” for the three blob per block target. Assuming no issues are discovered, developers will move ahead with the increased blob count for mainnet activation.
| 176.4 | **Builder Override Flag** Tsao asked the status of client teams on their implementation of the builder override flag. The builder override flag is a new Boolean field in the Cancun upgrade that execution layer clients can use to indicate to consensus layer clients that validators should fall back on local block production instead of a third-party builder due to the detection of censoring activity by builders. As highlighted by Tsao, the implementation details for how to detect censoring activity by builders is subjective and intentionally left up to client teams to design.
| 176.5 | **Builder Override Flag** pseudonymous developer for the Geth client team by the screen name “Lightclient” said that his team had implemented to the flag but would not be merging it in an official release any time “in the near future.” Representatives from the Besu and Nethermind teams indicated that they had not implemented the optional flag within their clients. Tsao highlighted that the flag could be a useful tool to implement sooner rather than later to dissuade and discourage staking pools or large validator node operators from engaging in certain “timing games.”
| 176.6 | **Process Items** Beiko has created a Meta EIP document for the Cancun/Deneb upgrade, which lists all of the Ethereum Improvement Proposals (EIPs) that have been included in Cancun/Deneb. It has been created on GitHub with an EIP number of 7569. Additionally, Beiko has created EIP 7568 as the Meta EIP documents for all prior upgrades for which developers did not create a dedicated document tracking the list of EIPs included in an upgrade. EIP 7568 will link to upgrade code specifications.
| 176.7 | **Process Items** Beiko announced that he has created a new discussion thread on the Ethereum Magicians site to scope out the next network upgrade, Prague/Electra. He asked that developers think critically about whether to couple the EL and CL upgrades together as they have for the last two hard forks. The activation of certain code changes such as EIP 7002 will require changes on both the EL and CL and thus, will require coordinating Prague and Electra upgrades at the same time. However, for other code changes such as Verkle trees, there are ways to re-work the implementation to only require an upgrade to the CL.
| 176.8 | **Process Items** Beiko announced that he has created a new discussion thread on the Ethereum Magicians site to scope out the next network upgrade, Prague/Electra. He asked that developers think critically about whether to couple the EL and CL upgrades together as they have for the last two hard forks. The activation of certain code changes such as EIP 7002 will require changes on both the EL and CL and thus, will require coordinating Prague and Electra upgrades at the same time. However, for other code changes such as Verkle trees, there are ways to re-work the implementation to only require an upgrade to the CL.

**Tim**
* Welcome everyone to, ACDE 176. so main thing today, is the Dencun Updates. So, you get to get some updates on the devnet from the different client teams and also to try and figure out, what we want to do over the next couple of weeks and potentially over the holidays. as we have an ACDE scheduled next week, ACDE two weeks from now. and then I don't know if we'll have ACDC over the holidays and, around sort of New Year's. So, the last couple calls, we have to, sort of coordinate. and then after that, I just have a couple small process things around, meetings, which we discuss last time and then starting the discussion around the next upgrade. but, yeah, to kick it off, I know we launched Devnet 12. we've been running some tests on it, so maybe we can start with just a status update on Devnet 12 and then go into the various client teams, and where they're at, I don't know, Perry. Or if Barnabas either of them is on the call. Nice. 

**Parithosh**
* I can go. Yeah. so we've had devnet, 12 up since last week. It's been finalizing, during regular operation. We did find a red spark that's been patched. Now, on Friday, we launched Mario's Blob tool, along with a new action it can perform that triggers slashing. So that's the new, equivocation condition. And via the test we found, I think, 1 or 2 Lighthouse Slasher related bugs. on Monday, those bugs were patched. And now we do have slashings on chain, so if you go to Dora, there's a section there where you can see some nodes are slashed. once we did have, once we did confirm that slashing works, we turned on MeV on more nodes. And we did find at least one, MeV relay related bug that's also been patched now, and we've rolled out MeV to a lot more nodes. You can see that there's a healthy distribution of delivered payloads. we're still seeing like on off errors on the relay. So nothing's fundamentally broken, but there's still something broken. that would probably be dug deeper by the Fleshpots team. and I see there's some chatter on interop now with Jim posting a potential map bug with lighthouse, I think. I think that's, pretty much everything we have on devnet networks. 

**Tim**
* What can you just clarify what's an on off error? 

**Parithosh**
* We're noticing, like, a few, error logs on the relay. Got it. Not necessarily sure why. there's something about slots in the past. I think Shana from Flash bots mentioned it could happen when there are no transactions that the builder would be potentially building a block with. But that doesn't happen very often. 

**Tim**
* Got it. Thank you. and then there's a comment from Danny about trying to test the fallback, to the relays by shutting them off from time to time. Have we done that or. 

**Parithosh**
* We haven't yet. We need to still test the circuit breaker, but. Yeah. 

**Tim**
* Awesome. yeah. Any client team want to share some, more granular detail from from their end? 

**Terence**
* Still working on, revamping some of our original design with regards to, like, blobs catching a verification layer. So I think we're, we should be able to join that network maybe next week. If not, if not in two weeks. So that's just an update from our end. 

**Tim**
* Got it. Thanks. Hey. 

**Danny**
* And I know,  I think David was talking to Casey yesterday, but essentially in a lot of the security researchers are like super eager to help do reviews. you know, the testing team and DevOps team are super eager to integrate you. Also, if there's anything you know that people can do to help support y'all, to get you to the finish line, just make sure to reach out. 

**Terence**
* Yeah, thanks. We have got, a bunch of good feedback from Justin, from the from the security team already. So thank you so much. 

**Tim**
* Awesome. Thanks, Terrence. And the other team. So if there's no specific updates.  I guess what the teams feel like. The right next step is at this point. Once, you know, Prism joins the deep nets and obviously, you know, we find if we find any issues there, we fix them. do teams feel comfortable moving to test nets? or at least the first one, like Goerli? Do we want to do potentially a shadow fork in the next couple of weeks as well to to see if we get more data out of that? yeah. Other people feel we should be moving forward at this point. 

**Victor**
* Besu ready. Full team ahead. 

**Marek**
* Same with Nethermind

**Andrew**
* Aragon is ready. 

**Gajinder**
* A lodestar is also ready. 

**Ben**
* No concerns on Turkey side yet. Happy to move forward. 

**Tim**
* And I guess, is there any team aside from Prism who's like, feels like there's something big or significant that they still need to work on? Obviously, every team probably has some bugs and, some small, small things to fix. But is there anything else that people are concerned with?  And Perry has a comment about testing the slashers. Are there other clients which have slashers that's ready that we could test on the Devnet right now? 

**Danny**
* I'm pretty sure that's just Prism and Lighthouse feature support. 

**Tim**
* Okay, so we can test prism as soon as we have it. so. I think we. If, prism needs a couple more weeks and, you know, potentially we find some issues, and, you know, fix them. and also not wanting to fork like, a test net over the holidays.  I feel like we might be in a spot where we can aim to coordinate a fork on Goerli as soon as people get back from holidays.  Again, assuming we don't find some other crazy issues that you know, or something that delays things by a few weeks. but generally, does that seem reasonable to people that like, you know, I don't know when would be the first 2024 call, but. Using that as a time to, set the fork date. and then potentially having the fork, you know, two weeks outside from that. so  if the first call is, you know, on the first or second week of January, this means we'd, this means we'd we'd be forking gaudy sometime mid-January, you know, something like that. Does that seem. Reasonable to people. at this point and again pending like obviously I know prism has some, you know, some changes we need to test on the devnet. And like that could still reveal an issue. But assuming that after a couple of weeks it's integrated and it's also tested. yeah. 

**Danny**
* Yeah, I'm pretty pro conditionally doing that. Assuming we can get prism integrated in and battle tested. Got it. 

**Tim**
* And then. So if we. If we're aiming for that. Oh, sorry. Ben, please. 

**Ben**
* Just wanted to check status on something. So one of our concerns moving from targeting 2 to 3 blobs per block was around network propagation. Are we now satisfied that this is going to be fine on main net? Have we done the the have we gathered enough data or is that something we need to do on test nets. And where do we fit this into the the program and the planning? 

**Danny**
* So from my understanding, both the main net big block experiments, as well as the organic big blocks on the order of even 1.5, sometimes near two megabytes that we've seen on main net, were really solid and test nets and continue to be solid. And shadow forks may not. Shadow forks would be telling. at least to some degree. Although all of those test net related items are on the order of small I would be supportive of between now and mid-January. Trying to do some multi-region, pretty large node, experiments on the, either with like, potentially even on main net shadow fork level, just to really get a view on it. Let's see, what does this say? Yeah. So, Perry, you said 300 nodes. 

**Parithosh**
* Yeah. The, plan is that once every client's ready for, devnet 12, we're going to do one really big shadow box. So something like 300 nodes. and we have the tooling mostly ready for that. Well, we'll find out once that shadow fork is up. and what's the issue? Sorry. Go ahead. 

**Danny**
* The cost differential on going on, doing that same thing on main net  is on the order of many multiples. 

**Parithosh**
* Surprisingly, not that much. Goerli is really, really big right now. 

**Danny**
* Okay. interesting. Yeah, I guess the main thing, the main thing that we'd want because I, you know, in the gossip flow is not really execution against the maintenance state. but the big thing is the gossip kind of competing with main net level, probably transaction gossip is the main other thing that would be kind of telling and probably switching from Goerli to main net, although we could potentially. Make sure that a Goerli mainnet fork had a lot of transaction gossip. But anyway, I would be supportive of 300 or even ramping up to more if it's reasonable in terms of man hours and costs, even if it's like an hour long test. 

**Parithosh**
* Yeah, I think we'd have to keep the text really small for sure. but at least one thing we've noticed in the past is none or all the Shadow Fox, etc. that we've done are too pristine. we're only going to get any real data for a P to P related upgrade from natural test net. So at some point we're going to have to bite the bullet and do Goerli. And I would make the case that we spend any extra money we were going to spend on better monitoring setup for Goerli and do it earlier. 

**Danny**
* Do we have an estimate of how many nodes are on Goerli proper? 

**Parithosh**
* A crawler. I don't have that at hand, but I can find that out. 

**Danny**
* Yeah, it'd be really interesting to get like, just even order of magnitude crawler data, because if we're on the order of like a thousand, I think that that would be very valuable data. If we're on the order of 300, then it's like not much different than what we're gonna get. 

**Tim**
* The newest crawler has about 3k on Goerli versus almost  9K on main net. So I don't know how reliable the numbers are, but if if the ratio between them is is is good, then it's like still a third of main net, which is just pretty decent. 

**Danny**
* That's really good, especially with the way gossip should scale. Obviously you can have degenerate cases, but it should scale with the log of the size. So it's not actually terribly different in terms of hops. Yeah. 

**Tim**
* Oh, actually. Sorry. So if, uh. And. Okay. No, no. Yeah. It's about A3X ratio. yeah. so. Okay, so we can aim to do at least one Goerli shadow fork, by the end of the month, then trying to fork Goerli next, early in January and then,  That'll be probably the time where we would, change the blob count, basically. Like if we saw something going wrong on Goerli that was sort of attributable to that. But aside from that, there isn't really. I mean, you know, we might see something on Sepolia as well, but all of those networks have like a smaller, like if it works on on Goerli, it should probably work on Sepolia and and on Holesky. but Goerli is probably the last significant test where we learn something that makes us change the blob count before we go to make that. 

**Danny**
* Yeah. Makes sense. It's our. We're sacrificing it. 

**Tim**
* Hopefully not. But. Yeah. Anyway. 

**Danny**
* It's okay if it is sacrifice. Yeah. Yeah.  

**Tim**
* Ben, does that, satisfy your question? 

**Ben**
* Yeah, I think so. So I mean, to, to summarize, Goerli network is is likely where we'll get the best data on this. so as long as we've got the tooling and the kind of time  to do that analysis at that point, I think that's fine. 

**Danny**
* And knowing that a Goerli shadow fork before we will be spamming and monitoring for this condition specifically. so that, you know, if it fails there, we know it's probably going to almost certainly fail. Like really. 

**Tim**
* Sweet.  Okay. So I guess. Yeah. So in terms of next steps, yeah. Let's  get some more testing on on Devnet 12, get, a Goerli shadow fork up and running. As soon as we're back next year, we can, finalize the Goerli fork date. potentially we can also have some proposals async on the discord. And, you know, use the call only to, like, finalize things. But, we'll know a bit better over the next couple of weeks how things are looking. but the aim would be that in January, Goerli gets forked.  I see, Terrence, you have a PR in the chat about, an execution API change. And do you want to bring that up now, or is there anything else that people feel is more urgent with regards to. 

**Danny**
* I have one more question on the Goerli stuff. 

**Tim**
* Let's. Yeah. 

**Danny**
* Is the node distribution similar to main net? Not necessarily the validator but the node the. 

**Tim**
* Yeah. I mean, I'm just looking at this ethernet's, crawler. So, I mean. 

**Danny**
* If it were way out of whack. 

**Tim**
* It doesn't feel. 

**Danny**
* Like necessarily perform like. 

**Tim**
* Yeah, but it doesn't feel crazy different. But this is for EL not  CL so I don't know what the CL looks like. yeah. Okay. 

**Danny**
* And then if we can find something. 

**Tim**
* Yeah. In terms of the countries, it also feels roughly similar. So like. Yeah, it feels like of the three test nets, by far the closest.  see anything else on Goerli or Shadow Forks? 
* Terrence? yeah. You want to talk about the execution APIs? 


**Terence**
* Yeah, So little background in Cancun. when you, try to get a payload from the CL to the El, there is this optional parameter. It's called override, meaning that as an El client, you can trigger CL client by telling there if there's some sort of like, censorship going on  the network. So censorship is a very, subjective here. This is CL client has sorry EL client may have like different design implementation.  how to observe this sort of censorship. Like, for example, like a transaction that's been paying higher than normal priority fee, but it has been stuck in the main pool for a while and the builders are not including it,. Right. So, so since this is available in, Cancun, I wonder if any EL client has looked into this and and implementing this sort of override feature. And the reason I am asking this is that because like us,  we have seen over the last few weeks. Right. there are there are staking pools, there are actively discussing, delaying block,  propagation just to its more MeV. And this may become a problem once we have blob a blob transaction because blob transaction also delay the block gossip. Right. So imagine today we have a blob transaction that is in the main pool. But it doesn't really like make that much money because they are cheap blob transaction. They are boring. And then as the staking pool I will have the decision whether to include blockchain session or whether to or whether to not include it, instead of just wait a little bit longer and get more MeV. So there's some sort of this kind of game that are  staking pool can play and it's not ideal. 
* So I think having some sort of like, censorship or override, with some sort of respect on blob transaction could be fairly useful. So I wonder if any client team has, thinking about this or. Yeah, thinking about implementing this. 
* Like so like Hyun has the comment saying that Mario's implemented it, but but then they don't think they will merge it in the near future. Yeah. I wonder if anyone has any more like feedback comments on this. 

**Marek**
* So we haven't implemented it yet in EL. 

**Terence**
* Derek thanks I don't yeah. I can also add another comment on discord later. Just to reiterate what I said. Yeah, I still think it's very important to have this early on because like 95% of the blobs today are built by builders and builder has a lot of power on just like including like blob transaction and choosing not to include it. And I suspect in the beginning, blob transactions are going to be, very cheap such that the builders may not even care. And yeah, so there may be some weird information asymmetry there. 

**Danny**
* Yeah. And I guess to be fair, as Rohan mentioned, like on the local setup, if a pool really wants to be playing these games, they can just override. but I guess also if we do see this, the equilibrium of what the priority fee in the normal case for L2's, is probably going to shift to much higher. so hopefully we can find some sort of balance. But I agree, some of these dynamics are pretty concerning. 

**Tim**
* Oh, Potuz. 

**Potuz**
* So I was thinking along the lines of what Danny just said, that, that it just might be market. this blobs transactions will have to pay enough so as to offset whatever the fee is required so that they the proposal actually includes them, because also it's something that that risks their blobs to be to be rewarded more. But I think it's different than with usual transactions because this is now playing with these pools that are either publicly or privately delaying blobs production as much as possible. So now blobs not only need to compete with fees, but they also need to compete with that delay itself and all of the MeV that you can get out of delaying your blobs. I mean, this this is a market that I think this wasn't prevented. This wasn't thought of when when the fee mechanism for blobs was designed. 

**Dankrad**
* But, blobs can use the same chip as normal transactions, you know, to compensate for the, increased opening risk. 

**Tim**
* I guess what's the best place to continue conversation on this? obviously the PR is, like, closed, but is there? okay. Yeah. Terrance will bring you up on discord.  Yeah. Which channel do you think makes sense, or was there already a conversation on the discord in one of the channels? Okay. We'll use ACDE 

**Danny**
* There's also a good post, recently by. Mike and Casper on Eth research. Kind of digging deeper into the time game stuff going on in general. if people want to take a look there to put some more brainpower towards it. 

**Tim**
* Awesome. Yeah. Thanks for bringing this up, Terrence. Any final thoughts? Comments? 
* Anything else on Dencun in general? 
* If not, I have just three quick, updates on the meta Eth stuff that we talked about, last week, but, we have a meta EIP draft for Dencun. I forget why, but there's some reason why it's not merged yet. I think it just needs an EIP editor to merge it. and then we didn't use meta EIPs for a couple years. so instead of backfilling all of the meta EIPs, I created one to, reference all of the specs for the previous hard forks. so that it doesn't look like the the meta EIPs were always there. but it's saying, like for this chunk of forks where we didn't use meta EIPs. Here's where you can find the canonical specs. it includes both the EL and CL forks. 
* So if people want to leave comments on that, I'm hoping to get it merged soon as well. And then lastly, so I created this thread on Eth magicians to start discussing the scope for the next network upgrade. I know there was also an issue on the CL side on GitHub where people could, post suggestions. but there started to be some conversation on it and I think, yeah, as we start wrapping up, Dencun, then we can spend more and more time thinking about how to scope and, prioritize things for, the next upgrade.
* And I think one thing that's probably worth it for client teams to think through, now is like, are there, proposals that would cause the upgrade to be coupled or decoupled across the EL and CL? so the past couple forks, were obviously coupled, because we ship stuff that sort of required it. 
* But it's there's at least a possibility, I think, for the next upgrade, that this is not the case. and so it's worth thinking through that, like, is this something we we. You know, we we want to to explore. And, if there are things that couple, you know, how important are they and, you know, do they risk delaying a bunch of other stuff? yeah, I think that's, that's yeah. Coupling sort of happened by default the last three times, but we should,  Yeah, l triggerable exits is probably the the the only one that I'm aware of that requires the fork to be coupled.  Okay. It seems just a. Okay, there's more popping up in the chat. Okay. 

**Danny**
* Yeah, I mean, I'd really love to see wherever Verkle goes to not be coupled, because simultaneously, I think we'll probably work on some sort of data availability sampling upgrade. and those are very independent. but obviously then there's a lot of these small things that might be. 

**Tim**
* Yeah. And one thing maybe to think through is also,  How early or late in the process do we want the couple things like, you know, say that we did Verkle and DAS and they're decoupled and then we choose the EL triggered, exits. You know, can we couple stuff later in the process? What does that look like?  Yeah. I'm. Yeah, I don't know any. Other teams or people have thoughts generally about approaching the next fork or how should we think about that? I don't think we should start discussing specific EIPs on this call, but yeah. At a higher level. Any thoughts? 
* And I guess maybe. Okay, so last question then, these past couple calls have ended a bit on the earlier side. So would people want to start discussing the next fork in more details, like in the next couple of weeks before the holidays? Or do people prefer to table that until, early next year and sort of stay focused on, on the fork? Lightclients wants to get into it. 
* Now we can do that too, if. Yeah, okay. It seems only like fine points to discuss right now.  

**Loin**
* I'm down. 

**Tim**
* I mean, okay, so yeah, I think we should probably do most of this.  after the holidays. I'm fine giving people a couple minutes now if they want to bring some stuff up, but, Potuz. 

**Potuz**
* I do agree we should probably defer this to after the holidays. but I, I very much find it unlikely that this is going to be decoupled, or at least on the CL side, there are some kind of urgent matters with the growing validator set. So I think like the few hours that or ideas that are being discussed on how to, lower the validator slice or to reuse indices or I mean, to set up the stage so that we can actually lower the validator side, we should start working towards that. 

**Danny**
* Yeah. To be to be fair on 7002 or not, on the max EV proposal, you could potentially introduce additional, CL messages to counteract the ability for needing the EL. But, there's not, like, 100%. 

**Tim**
* I'm happy with. 

**Potuz**
* The CL only fork. It's just that I don't, Yeah, I don't see I don't I'm sure there's going to be EL changes that are also important. 

**Tim**
* And to be clear, I wasn't trying to push necessarily forward decoupled one. But I just want us to. Make make that like a conscious decision, not just default to coupling, because we've gotten used to doing that the past couple of weeks. yeah.  Okay. Guillaume. 

**Guillaume**
* Yeah. Just, regarding the coupling, actually, Verkle is mostly an L thing, but since we're putting, like, we're distributing witnesses and so far the the decision, we. Okay, it's not the decision, but the approach we have made was to to pass this, these proofs and witnesses via the CL, so it would actually be coupled. 

**Danny**
* Is that P2P only or is that a consensus change as well? 

**Guillaume**
* No, it's, I mean, it's, an execution engine change and then, an, sorry, a peer to peer. it's not actually, I don't know how Mac and Gajendar implemented that in the States, so I don't think it's, consensus change. No, but it's,  I might be wrong. It depends on the implementation detail. I'm not, I'm not 100% sure. 

**Tim**
* Oh. Got it. Justin. 

**Justin**
* I just wanted to, uh. I posted this comment in the chat. has the ship already sailed on using meta EIPs for hardfork scheduling? Are we all firm on that? 

**Tim**
* What is the. What is the argument against it? Yeah. 

**Justin**
* Well, I just wanted to, you know, again, I apologize for not being here last session. but, it seemed a little counterintuitive since we just spent a lot of time deciding, you know, ERCs and EIps should not be in the same repo because they have different audiences. And so I was wondering, like, why not just simply create a separate EIPs for for hard forks and scheduling? I'm sorry, not an EIPs at a separate repository, rather for, hard forks and scheduling. 

**Tim**
* So maybe my practical answer to that will be because there's just one of those that happens every year or maybe two. and it's kind of weird to have this separate. Repo for like ten EIPs. That said, I'm not completely like if. I don't know it. Yeah, I'm not super against it. I do think we want them to be. Like closely coupled to EIPs, like where they were before was like randomly throughout the specs repo. And that's kind of hard for people to find versus like meta EIPs, you can just go to EIPs, dot ethereorg and search for London. And you know, there's like it pops up there. so that's like the main argument I see in favor of meta EIP's is just like they're easier to reference. whether or not they, like, live in a separate GitHub repo is maybe not super correlated with that. But, yeah, I think that's the argument for like by default, having them in the same repo.  

**Justin**
* Okay. So traditionally when I think of meta, blank, right. It's it's usually, you know, specs about specs, for instance EIP-1. Right. This is where we define the, the EIP process and how future apes are to be written, etc., etc.. So that's when we say meta EIPs. That is more along the lines of, of of what I think. Yeah. 

**Tim**
* So we've been talking about maybe renaming them, which I'm totally fine with. 

**Danny**
* To be fair, it is kind of a meta spec because it says this specification for this upgrade is these five specifications or something like that. So by referencing an EIP it is. But I don't care about the name. 

**Tim**
* Yeah I yeah I care more about the proximity than the name. And yeah, some EIP editors have made the same argument as you Justin. So if we decide to rename meta EIP to like hard I don't know fork descriptor EIP, I'm, I'm totally whatever name we come up with I think is is fine. But I think not having like first of all having a list of what's in the hard fork I think is really important. And we didn't quite have that. The past, like the list ended up being the blog.etherum.org article, which is not great, 100%. And then and then having that list be close to the actual EIPs. But I agree the name is, you know, potentially not. Uh. Not great. We can bike shed this off the call, though. 

**Justin**
* Yeah, I'm gonna drop it. I just want to. It's not so much about the name. It's about, you know, the repo, that's all. Yeah. So. All right. Thanks. 

**Gajinder**
* Just to chime in with respect to Verkle being,  consensus. fork on CL side. Yes, it will be because, execution witness is now part of the execution header, which will basically require, us to, have consensus on. 

**Danny**
* Okay. And I guess to to be clear and to be fair, like some some of these things are more like insert the new field into the data structure rather than, dealing with like a feature beyond that. and so you're right in, in a lot of decoupled forks. There might still be some of that like process upgrade that needs to happen without like a ton of effort and happen. So we should at least like keep that in mind when we're talking about decoupling. Because I could have still imagine, like Verkle could, quote, be decoupled, meaning the consensus layer makes sure to like give them a branch with this extra, extra field in it, which could take a not very long. for testing and then kind of come in together and make sure everything's locked tight at the end. 

**Gajinder**
* That's correct, because state transition has not changed. on the CL side because of execution witness being added. Also, there could be a different mechanism in which execution witness can part can be part of blobs. So basically it doesn't even need to have that kind of upgrade. 

**Danny**
* Yeah. And I guess just to another point, like if we did, sorry. Like we had a date availability dominated consensus layer fork, there'd probably be an upgrade to the data gap limit. but on the execution layer. But, like, I'd still largely call that decoupled. 

**Tim**
* Okay, I think, yeah. Based based on this conversation, I think for Prague and Electro, we should probably do is then. Have people, I guess, signal now to people that if they want something, consider it's like the right time to start raising it, and that over the next month I suspect people will like bring up a bunch of proposals. If client teams can keep an eye on both the Eth magicians and GitHub thread. then we can sort of kick off the calls next year. 
* Getting your feeling from the client teams about all the different proposals, you know, their relative value and kind of go from there. that seems probably more productive than trying to start discussing random EIPs now. 
*  And I think in parallel to that, one thing we discussed in the context of dev connect is trying to do some sessions on, like, specific topics, remotely after they've dev connected, like, get people up to speed on stuff. So if things like, Verkle or potentially like a  fork on the CL are being considered and they're like pretty significant changes, it might make sense to organize a session for at least the two of those. And I don't know if there's something else. because I suspect those will take up, like, more time to go over and have like a much bigger degree of discussion than, sort of a random small EIP.  Yeah. Does that seem reasonable to people? No objections. One thumbs up and. 
* Yeah, you can try to roll with that. Okay. Anything else anyone wanted to discuss before we wrap up today? Okay. If not, well, yeah, we can, close out here. Thank you everyone. and we will see you on the testing call on Monday, and then, ACDC next Thursday. 

**Dankrad**
* Thanks. Bye. 



-------------------------------------
### Attendees
* Tim Beiko
* Danny Ryan
* Pooja Ranjan
* Mikhail Kalinin
* Marius
* Wesley
* Barnabas
* Saulius
* Danno
* Lightclient
* Pari
* Ethan
* Mario
* Tomasz
* Oleg 
* Kasey
* Marek
* Crypdough
* Fabio Di
* Terence
* Andrew
* Roman
* Marcin 
* Pop
* Guilaume
* Protolambda
* Carlbeek
* Mike
* Gajinder
* Stefan
* Hsiao-Wei
* Josh
* Phil Ngo
* Alexey
* Holger Drewes
* Dankrad
* Guillaume
* Proto
* Holder Drewes
* Stokes
* Peter Szilagyi
* Sean
* Micah Zoltu
* Jiri Peinlich
* Marius Van Der Wijden
* Potuz
* Evan Van Ness
* Moody
* Tynes
* Alex Beregszaszi
* Marek Moraczyński
* Justin Florentine
* Ben Edgington
* Lion Dapplion
* Mrabino1
* Barnabas Busa
* Łukasz Rozmej
* Péter Szilágyi
* Danno Ferrin
* Andrew Ashikhmin
* Hdrewes
* Crypdough.eth
* Ameziane Hamlat
* Liam Horne
* Georgios Konstantopoulos
* Mehdi Aouadi
* Bob Summerwill
* Jesse Pollak
* Stefan Bratanov
* Sara Reynolds
* Caspar Schwarz-Schilling
* Ahmad Bitar
* Marcin Sobczak
* Kasey Kirkham
* Sean Anderson
* Saulius Grigaitis
* Ruben
* George Kadianakis
* Dankrad Feist
* Andrei Maiboroda
* Gcolvin
* Ansgar Dietrichs
* Jared Wasinger
* Diego López León
* Daniel Celeda
* Trent
* Mario Vega
* Kamil Chodoła
* Ziogaschr
* Kevaundray
* Antonio Sanso
* Oleg Jakushkin
* Leo
* Nishant Das

-------------------------------------
Next meeting on Dec 21, 2023, 14:00-15:30 UTC




