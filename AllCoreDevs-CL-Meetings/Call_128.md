# Consensus Layer Meeting 128 [2024-2-22]


### Meeting Date/Time: Thursday 2024/22 at 14:00 UTC
### Meeting Duration: 47 Mins
#### Moderator: Danny
### [GitHub Agenda](https://github.com/ethereum/pm/issues/966)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=FgOuUEgguN0) 
### Meeting Notes: Meenakshi Singh
### Next Meeting: Thursday 2024/3/7 at 14:00 UTC

___

## Summary


| S.no: | Summary: | 
| -------- | -------- | 
| 128.1       | All client teams, except lodestar, have released final software versions for the dencun upgrade   | 
|128.2| These versions plus the dencun-ready candidate client for lodestar are currently being tested on one last testnet, a mainnet shadow fork|
|128.3| Devs plan on doing more testing on the shadow fork over the next few days|
|128.4| Flashbots plans on releasing dencun ready MEV-Boost software early next week.|
|128.5| Reminder dencun mainnet activation is scheduled for march 13, validator node operators upgrade your EL,CL, AND MEV-Boost software before then!|
|128.6| Electra --devs agreed to start working on electra which for now includes: EIP 6110, Supply validator deposits on chain, EIP 7002, Execution layer triggerable exits, and EIP 7549, Move committee index outside attestation.
|128.7| Devs will do further work on inclusion lists and see if it is easy enough to add to electra without delaying the other three code changes|
|128.8| Lowering staking rewards -- First of what will be many discussions on whether to lower eth issuance given the rising amount of staked eth|

---


**Danny** [4:06](https://www.youtube.com/watch?v=FgOuUEgguN0&t=246s): Welcome to All Core Devs Consensus Layer Call 2 to the 7. This is issue 966 in the PM repo. We will spend as much time as we need on Deneb today as we are in kind of final launch preparation. I'm not sure if there's anything outstanding other than quick recap.   Moving on to Electra, I will attempt to give an editorialised outstanding EIP discussion recap, which will certainly be wrong, but maybe we'll start some discussion. There is a proposed issuance Curve Adjustment research post that is out that we also discuss. Then beyond that, generally, Etan, go over light client roadmap possibility. I believe we are closing in on releases and attempting to do a Mainnet Shadow Fork and get a bug post out at the very start of this week. How are we on the releases? Are there any outstanding releases? Or any release that hasn't been put out yet?

## Deneb Launch Preparations

**Terence** [5:39](https://www.youtube.com/watch?v=FgOuUEgguN0&t=339s): As soon as we’re releasing V5, just right after this meeting, we have a V5 release candidate one. And that's yeah, and basically what Promote that to the five.

**Gajinder** [5:55](https://www.youtube.com/watch?v=FgOuUEgguN0&t=355s): Same for Loadstar now we also have the 1.16 RC1 release candidate, which is likely to be promoted to V 1.16. Maybe today or by tomorrow. 

**Danny** [6:12](https://www.youtube.com/watch?v=FgOuUEgguN0&t=372s): Okay. On both of those are there? Can the people that are running the Mainnet Shadow fork? Can they use the release candidate and begin doing their work now?

**Terence** [6:26](https://www.youtube.com/watch?v=FgOuUEgguN0&t=386s): Yeah. This is  exactly the same.

**Gajinder** [6:30](https://www.youtube.com/watch?v=FgOuUEgguN0&t=390s):  I believe
it is being used in our case as well. 

**Danny** [6:40](https://www.youtube.com/watch?v=FgOuUEgguN0&t=400s): Are those the only two outstanding releases? I'll take that as a yes. And prysm was right after the call. And loadstar is doing the same, but ended today or what's the timeline recorded?

**Gajinder** [7:01](https://www.youtube.com/watch?v=FgOuUEgguN0&t=421s): Yeah, I think our CI is running maybe in couple of hours. It should be out. It could be sooner.

**Danny** [7:13](https://www.youtube.com/watch?v=FgOuUEgguN0&t=433s): Great. Any updates on mainnet shadow Fork? Anything that we should know any issues? Any early even just the expected timing?

**Paritosh** [7:24](https://www.youtube.com/watch?v=FgOuUEgguN0&t=444s): Yeah, I have give an update on that. So we had the mainnet fork go live today. We checked with both prysm as well as loadstar that we could use the Aussie releases instead of waiting and we got okay from them. We have Genesis about an hour ago and then Dencun as live about half an hour ago. There was a conflict generation issue where the nethermind, the IG said total difficulty instead of total terminal difficulty as a result, the Nethermind the nodes offline, but it's been fixed now. And if you look at the last epochs, the stakes we should be inching closer towards perfection shadow fork. We haven't started spamming blobs yet, were mainly waiting for exiting one or two values so that we have the funds to spend Shadow fork to begin with. And once that's done, we'll probably put an update in that we have Xatu running as well. But so far, it looks like all the releases are good. And there's no there's no report. 

**Danny** [8:30](https://www.youtube.com/watch?v=FgOuUEgguN0&t=510s): So, we’ll have blobs being attempted to be pushed around the network prior to the fork. 

**Paritosh** [8:37](https://www.youtube.com/watch?v=FgOuUEgguN0&t=517s): And no, we weren't able to we weren't able to exit any validator in time for having funds that would be double spent on mainnet. 

**Danny** [8:51](https://www.youtube.com/watch?v=FgOuUEgguN0&t=531s): Got it any questions for the DevOps team? 

**Terence** [8:56](https://www.youtube.com/watch?v=FgOuUEgguN0&t=536s): I have a quick question. For my understanding, typically for shadow fork builder, relayer MEV boost are not tested. Right. Is that a correct statement?

**Paritosh** [9:09](https://www.youtube.com/watch?v=FgOuUEgguN0&t=549s): Usually Yes. But this time, because the relay up as well. We have the validators that are just there as well. But we're having the same problem as with blob spam. And we normally like there's just not much traffic. So locally blocked blocks are, there's no point for the bids to be higher. So we need the validator experts to happen so that we can run this tool called MEV flood, and that will create the juicy builder transactions and after that point, data is picked by the network.

**Terence** [9:42](https://www.youtube.com/watch?v=FgOuUEgguN0&t=582s): Thank you.

**Danny** [9:48](https://www.youtube.com/watch?v=FgOuUEgguN0&t=588s): Any other questions about the shadow of work?

**Paritosh** [9:54](https://www.youtube.com/watch?v=FgOuUEgguN0&t=594s): Just one point about the releases. I think the flash bots team hasn't made a release for MEV Boost yet. As far as I know, they wanted to wait to see how they Shadow fork goes before they make the release, but they should be making one soon. 

**Chris Hager** [10:12](https://www.youtube.com/watch?v=FgOuUEgguN0&t=612s): Yeah, that's pretty much it. We have an alpha release that's running since a couple of testnet upgrades. And we wanted to test it on Mainnet, but couldn't get the feedback from LIDAR or so we were waiting for the shadow fork. And if that goes well, we take a1.7 release by Monday.

## Electra Outstanding EIP discussion recap


**Danny** [10:36](https://www.youtube.com/watch?v=FgOuUEgguN0&t=636s): Great. Any other updates from the DevOps team? Or testing in general? Cool. Anything else related to Deneb? Okay, I believe Tim is looking to publish blog posts on Monday. So we'll be monitoring for those final releases and keep an eye on the shadow fork between now and then. Great work everyone. Okay, I'm going to attempt to do an editorialized EIP outsanding EIP discussion recap, I will get it wrong. And we can go from there. Obviously, we're kind of at this juncture where we do have some baseline EIPs that we’re eager see a couple of those across layer and have some agreement on there. We certainly wants to begin building those into a single build and getting some tests out so we can move forward. There are a number of things that have been a bit of sticking points of the past month or so. We had a couple of breakout calls. I'll start with what I think is an easy one. My read on Potuz is that it is an regardless of the fork, a major R&D item that a number of people across most of not all, the teams do want to be digging deep into specifications or getting into a reasonable place as our guest on some R&D and as lighthouses begin to get him to pick up from there. So the intention there would be to parallelized, this does not need to be launched with a hard fork, but it does need to be launched added an epoch coordination point, unless we did some additional work. I'm not 100% sure that we could do it in a non-breaking way, but there have some ideas there. Anyway, probably coordinate an epoch and the question becomes when to introduce a data gas limit increase EIP. If this was done far before lecture, then we could be talking about it in relation to Electra. If not, we can be talking about it, either in relation to an isolated single fork this does has to be cross-layer and the way it's specified, or you know, and then in the next one, but essentially, this can be a heavy parallelized R&D item. We did have a breakout around ePBS. My read from that breakout is that although we continue to hold this as a high item that we're given timing constraints and given where the state of research specifications are, it's not ready to be put in for Electra. But there is a lot of appetite to dig deeper on here. I know there are some people on the spectrum of it's just a matter of putting the pieces together. There's some people on the spectrum of we need to do more fundamental research in Design and understanding. So this can also be a major R&D item.But we need to be hitting it. You know, I think that there is a kind of steady flow on the periodized stuff on the ePBS stuff. There is not just kind of fits and spurts. There's some people that are trying to keep it moving. It could be a target, upcoming interop, it could be a continued kind of series of calls, but we do need to kind of if that's going to move out of where it is right now. It needs to have more consistent work done on it. On the inclusions list stuff, my understanding is that it is less complex than I expected. I think some others expected. It is cross layer. So it's not just a decision that we can make here. And it does have the potential for more unknowns or gotchas surfacing than some of the other stuff that is currently in Electra. Just given the EIPs that are in Electra, it's just a matter of making sure specs are sound and writing good tests. We've done this kind of stuff before. I also close to that. But I have a little bit of, I think it could, unknowns could surface in relation to potential networking in relation to the complexities of passing things between layers. I'm not certain. But it could be something that gets out to Electra, depending on appetite. It could also be something that could be ripped from Electra, in the event that we do hit unexpected complexities. And then maxEB, that conversation, I think there's a lot of agreement that it's very valuable and important. I think there's enough concern around complexity in the context of the current work, that it's not currently being pushed actively, and likely, unless it gets rekindled very soon, we put on ice for now. That's my read on those things. I think the biggest question mark would be ILs, and getting a temperature gauge based of what happened in that prior in that call. Last week, I saw, you know,  Gajinder, in the chat saying +1 for Electra, but I don't have a read beyond that. Dapplion,  does a maxEB is not that complex in the chat. My read is that that ends up being a bit architecture dependent in some of the assumptions that are making based in architecture. So maybe that is true, with lodestar, but there's at least concern from the prysm side that it is. And Potuz wants to agree on the scope of a lecture, I believe that's probably with respect to timing. My read on scope, intended scope almost across the board is that people want to push for a 2024 fork 2024, that doesn't necessarily mean that it launches in 2024. Or, as we know, but pushing, having a intended target will help keep things moving. That is why when I mentioned ILs that they could potentially be you know, there's an intuition that maybe they're not that complex, but that we could rip out in the event that they are and that's why I did specify it and kind of that conditional manner. I think no one wants to open up the same with the periodized stuff. We get the ability to kind of work on it, not integrated. But then think about how to launch it when it's ready. A bit of a different strategy than what I proposed for the ILs. But nonetheless, I do believe that on both EL and CL there's a desire to scope things in a way that 2024 is at least realistic. And thus potential strategy is ripping something out if that doesn't be allow us to target. Okay, so I do see I'm catching up on Gajinder agrees on the rip out. Include IL rip out conditionally.
Enrico says if you want to target 2024 the 3 EIPs that are currently in there with a tentative IL. I put starting work on some things potentially ripping it out is equivalent scoping for 2025. I'm not certain I agree I the given the EIPs that are currently scoped. Obviously, production grade quality is one thing. But these are likely features that with good tests. Could be written on the order of 2 -4  to 6 weeks. As Dapplion said volunteer working groups can speed around POCs by ACDC. ILs. So a lot of that, given depending on where engineering resources that like, can be done very quickly, and then it's a matter of honing ILs are a bit of more of a question mark, but intuitively don't seem like that much complexity. And so I think the base could be written very quickly, not including ILs and then there can be some upside spent on POCs in that domain. To see so I don't. I don't necessarily agree that the ripping out strategy does mean that we end up in 2025. I do see that If it's not handled with care, or that we don't acknowledge the complexity when we hit it soon enough that could become the case. I do think the dependency on the EL and EL also quickly being done with a lot of this stuff would hold us a bit more to honesty here. Potuz? 

**POtuz** [21:32](https://www.youtube.com/watch?v=FgOuUEgguN0&t=1292s): Yeah, I don't mean that Fork is going to be its equivalent to scoping the Fork for 2025. It's just that it will start working on some features, and we're going to divert some of our people. We aren't large teams. At Prysm I think currently, there's less than 8 people that are actually going to be coding, you're going to divert some people to work on some of these features. And these features have chances of having trouble and beam being ripped, then those features, I consider that those features are equivalent to been scoping them for 2025, with the hope of getting them into a Forkt for 2024 report, if that's if that's the actual status of what we're going to be doing, then I would rather have a different discussion of what are the large R&D objects that we might want to see in this forum or not. I wasn't the impression that the broad consensus was that this form should be small without any large R&D objects.

**Danny** [22:38](https://www.youtube.com/watch?v=FgOuUEgguN0&t=1358s): I agree with that. to certain extent, I think the sticking point is our ILs actually a large R&D object. The read from a number is that they're not quite in that domain. But that we can be careful nonetheless. There's another component of the ILs discussion, which is their cross layer. And I don't believe that we have brought this to the Execution Layer at all in terms of the discussion unless I miss something, or do we have much read on that? Mike, do you have it? 

**Mikeneuder** [23:22](https://www.youtube.com/watch?v=FgOuUEgguN0&t=1402s): Yeah, I was just gonna say we've talked a good bit to the execution layer teams. Yeah, I think in general, the, vibe there is that the complexity is not too high. I think if we wanted to prototype with someone, like ref will be interested in kind of trying to Speedrun something too. Yeah. Also, I guess, the Besu team, or I mix up teku and Besu. But yeah, the consensus team that does execution client is also involved in discussions. So I wouldn't say they're flying blind, for sure. 

**Danny** [24:02](https://www.youtube.com/watch?v=FgOuUEgguN0&t=1442s): Right. So one strategy is to begin the Electra build with the three EIPs that we currently have. And two, as has been stated by Mike and others in the chat, speed run POCs to do complexity, sanity check, such that at plus 2 or 4 weeks from now. We can make a very clear and conscious decision whether this is an R&D item with unknowns or if this is a easier bread and butter fork, that we can just write a better feature that we can integrate into Electra.
## 
Does anyone against that strategy? I mean, this would the onus would be on probably Mike and a handful of others. To coordinate that speed run and to report on that speed run. Yes, affirmative. Right. I appreciate the dynamic verbal feedback I'm getting. Okay, I do think it's time to begin to build what will look like an Electra Fork with the features that exist that are agreed upon. So we'll begin working on that and in the event that in the next month we have reports back from a POC speedrunning group. Then we can see where ILs fit into that build. Yeah, so Terence asking if we need a another call like working group. I do think for coordination purposes if there's not a good explicit place in the discord yet let's do that let's add a kind of an ILs Working Group Chat maybe there is something already and then that Speedrunning group can and should coordinate whatever calls are unnecessary to do so. They should probably lean towards the public. You know, like dropping a call link into discord and scheduling. I don't know if they because it's more of a kind of engineering sprint. I don't think they need to be recorded or they can be recorded. You can do everyone. They don't seem to up most importance to surfaces are report a call. Okay, I will let you all coordinate in the chat or in discord. And we'll go from there. Are there other discussion points related to these 4 EIPs that I attempted to summarize? Cool Ansgar or Casper. Are you here to discuss this ethMagician post? 

## Issuance Curve Adjustment Proposal


**Asngar** [28:04](https://www.youtube.com/watch?v=FgOuUEgguN0&t=1684s): Yeah, sure. Hi, everyone. And so basically, we just wanted to briefly kind of mentioned Casper and I will also briefly talked about it already, I think two calls ago. And we've been working, we're looking into kind of the current insurance policy on Ethereum. Looking at the trends there, the long term consequences, and we just published two posts, and one of them has, at least it's relevant collectors, we want to briefly mention them. So the first post Casper is putting them in the chat right now. Is just some more general kind of look at the current insurance policy and looking at what happens if we basically don't, like do nothing and stay on it forever. And the argument that we make basically, is that with the advent of LSTs, kind of the way to say this physical supply curve per state has been flattening a lot. So more, more and more eth holders are now potentially willing to participate in staking because it's so much easier with LSTs. And because that kind of issuance curve, still plays out significant rewards are the way kind of to potentially like up to a 100% stake. That means that in the long term, it's not clear where exactly kind of they would be in equilibrium in terms of stake. And indeed, you know, since the beginning of the beacon chain, we've seen a continuous inflow of stake and we have to predict that this will not stop anytime soon. And we then looked a little bit into what would be the consequences of basically like more and more and at some point, maybe say 60, 70, 80, 90% of all eth stake. And we have several reasons why we think that would be pretty bad for the network. It's probably too much detail to go into them watching right now. But basically, just the intuitions being that for one, it harms source viability because LSTs just have economies of scale, but the kind of the more and more percentage wise, or in absolute terms, they have under management that the basically the more lean and efficient they get, and the harder it is to compete, they also become intubated, specifically, their liquidity that LSTs give users becomes more valuable as those entities are more widely adopted, which they would be as, as basically they become the dominant kind of money token on Ethereum. And also, just for kind of, for the general protocol, it basically would mean that over time, most currency holders would basically do this via these intermediated entities, which means it just adds a governance trust layer, it adds a risk factor, at some point, they could be kind of too big to fail bailout kind of considerations, it just, you can go through the document, we will,  be laid out kind of why we, we think that that would be a bad outcome, pretty much in detail. And then we have a proposal, obviously, what the end game. Could look like for visions policies, like basically something that we could, we could go through that then could be sustainable for the long term future, we call the targeting. So basically, the idea is we would specify some sort of, we would, we will take some sort of range of the stake participation that we think is acceptable, you know, that could be something like I don't know, Could they become the dominant kind of money token on etherium. And also, just for kind of for the general protocol, it basically would mean that over time, most most currency holders would basically do this via these intermediated entities, which means it just adds a governance trust layer, it adds a risk factor. At some point, that could be kind of too big to fail bailout kind of considerations, it just, you can go to the document, we have, like, we laid out kind of why we, we think that that would be a bad outcome, and pretty much a detail. And then we have a proposal, obviously, what the the end game could look like for questions policies, like basically something that we could, we could go through that then could could be sustainable for the long term future, we call the targeting. So basically, the idea is we would specify some sort of, we would, we would take some sort of range of basic participation that we think is acceptable, you know, that could be something like I don't know, 20 to 30%, or like something, you know, 10 to 40%, Some basically, some broad range that we pick that we think is acceptable. And then we just pick an issuance curve that, you know, you can think of it like today, where as we as participation drops a lot, you know, issuance roads shoot up a lot, because we really want to make sure that not everyone leaves, right. And we could do the same thing on the right side as well. But basically, if we, go too far beyond that maximum range that we like, basically, issuance rewards go all the way down to zero, or maybe even to below zero. And that way, we could really use the auto guarantee a hard stop. So that's kind of that was the broad research post. And then we looked at this kind of this long term solution we proposed and it is still has some open questions, it's very unlikely that we could kind of get there, for electra that require the big spent on this seems like people already have that focus on other things. And so we then looked at what happens if we basically don't do anything about this intellectual, you know, of course it's not quite clear what Osaka the next book would come but could easily be, say, two years from now or like a year and a half to two years. And if you do nothing for two more years, basically, with the current kind of maximum inflow, that we also can have we, of course, within that we ship this kind of maximum rate of new inflow. But even with that maximum rate, we could have up to say 40 million additional eth coming in, over the next two years, of course, it's not guaranteed that will actually be 40 million, but it could be up quite a bit. And so that would already be quite unfortunate in our views, especially because also, once we would want to move to targeting afterwards, if we are like way beyond the range, we would end up on the new target, it's quite painful to come back down because you basically have to set a tentative so low that people literally are pushed back out of the staking set, which is not ideal. So then we looked at like, what could we do in electra that basically, just is absolute, like minimal, kind of overhead for in terms of the fork, I mean, we've already talked to you about how there's limited room in the fork. And we came, we basically, we came across this, curve, that Anders came up with, he also presented this 2 calls ago, if you remember, and the nice thing about his curve is that on a technical side, it's trivial. Like we are not sure Casper, Casper also released the spec change, it's literally one line change. So it would be completely trivial on the technical side would not be a blocker for electra anything, we could easily do this. And so now it becomes really more of a social consensus thing. Of course, any issuance policy change always is very contentious. 
And so we are fully aware of this. So we're proposing it now hoping that we could have kind of enough of a broad conversation both here and of course, the broader community to to make a decision whether to include this in electra or not in time. And, of course, we could go into more detail, like the exact properties have kind of this proposed curve and everything. I don't know, that seems maybe a bit much for now. But we are happy. So maybe if you want to add something to what I just said, but otherwise, we also just happy to answer questions now or maybe give people time and then on the next ACDC kind of talk about it more in detail. Casper do you have anything to add? 


**Casparr** [34:39](https://www.youtube.com/watch?v=FgOuUEgguN0&t=2079s): No Sounds good.

**Vasilly** [34:44](https://www.youtube.com/watch?v=FgOuUEgguN0&t=2084s): Yeah. Hey, folks, I'm Vasilly from Lido. The thing I wanted to talk about here is in response to this. I think that one there is like a barrier for like, there needs to be more research on how this impacts the actual Octus and staking their research on like how this impact profitability and like issuance, etc, is solid. But what would happen, like how would people behave? How All those actors and staking will be saved when these changes happen is pretty important, because I think that like this is reducing the decentralization wallet for Ethereum. And this might like if this change happens right now, it's basically a reuse of the staking rewards by 30%. And as like, I think about like 70 to 80% of other in staking right now is on delegators. It's directly cutting into, like not operators budget by 30%, like the calculation about expected value of like, how much are they is costing, etc, it's not going to play into these, the budget is like, if on staking rewards. And these means that the octus that have the best ability to cut costs on marginl, which means a lot of Octus, and the octus have the ability to vertical integrate and increase the margin by like, external ways, this is a changes this is a mistaken this is potentially some, like, more involved MEV capture than it is right now. Like private MEV things and stuff. Will have like a major upper hand in this world. And I don't think that like limited stake. And stake wise sufficient
outweighs the like was your validator dataset. Yeah.



Okay.



**Ansgar** [37:22](https://www.youtube.com/watch?v=FgOuUEgguN0&t=2242s):Yeah, thanks for the comment. And I actually think there was a lot in there that I do agree with. And, of course, overall, the argument was, we should not do this. But still, I think a lot of these problems are very much real. But the problem really is that is it's not that we are, we have to make the decision between making this been used and doing something or not doing something if we decide not to include anything in electra we implicitly also make a decision, right. And that's really important to understand, because the concentration for staking is great. I agree if we could just freeze that in time. Perfect. We can't. So if we don't make a decision, we implicitly basically just allow for, for this purpose to at first to just keep sliding on this existing curve. And then basically two years from now a year from now, we are also in a place where yields have come down just as much because again, kind of like that, that's kind of how the curve works today as well. So we have the exact same problems, right. And that's exactly kind of what motivated us in the first place. If we don't do anything by just sliding and further and further up the curve, we ran into the exact same problems that there's less and less profitability, more and more centralization pressures. And so the main point here to understand is that we are comparing the kind of the dynamic endgame is situations, not just the situation today. And so if we do nothing, then we will end up with a equilibrium amount of each state that's much higher than if we do the adjustment. If we do the adjustment, yes, there's a one time reduction. But then basically, you stay at a lower level. And so if you compare that to the outcome of doing nothing, it's not actually that the yield will go down it actually in our in our post, we make the argument that we think it's very likely that even with the latest curve adjustment, the equilibrium outcome yield would be higher. But I also agree. Just a second comment, you said that we should not rush into this. And I totally agree. And that's why I think we just wanted to basically start the conversation here. Because the technical setup, this is a trivial, I think this could be added to Electra, basically, up to the last moment of when we still have like to open team to small changes. And we should definitely take the time for this decision until then. And this is not something where we should brush it. Include or not include decision anytime soon.

**Danny** [39:36](https://www.youtube.com/watch?v=FgOuUEgguN0&t=2376s): Potuz, did you have a comment? 

**Potuz** [39:38](https://www.youtube.com/watch?v=FgOuUEgguN0&t=2378s): Ansgar just made my comment. This is just a trivial implementation. It's just a one liner. So why aren't we pragmatic and just keep research. Currently, there's only research by Ansgar and Caspar, why don't we just keep researching this problem until we see I've done enough maths. We can just in the last very last minute just implemented is a one liner.


**Danny** [39:59](https://www.youtube.com/watch?v=FgOuUEgguN0&t=2399s): Yeah, and I think that's probably reasonable, but to prime the pump so that we can have that conversation and not a crazy rush seemingly way at the end. Now is a good time to prime the pump and to decide what other research should be done and how to go about potentially making such a decision. 
All right. Thank you Ansgar. Thank you Casper. Thank you others for comments. This is not I mean, this is an misunderstand, this is not even an EIP at this point. But this is a set of research and a dialogue that can play out over the coming months. Assuming that more research happens, more discussion happens. And we can bring it up here as that does. Any other comments for today on that one. Thanks, Chris. Anything else on Electra? 

### Lightclient roadmap possibility https://hackmd.io/@etan-status/electra-lc

Okay, Etan has a light client road map possibility document. That is in the chat, I'll share the link Etan, Do you want to go over new components of this?


**Etan** [41:55](https://www.youtube.com/watch?v=FgOuUEgguN0&t=2515s): Sure. I mean, it's a document that describes more or less the context in which those SSZ EIPs and also the light client development itself fits in. Right now, if you just look at one of the EIPs, it's very technical. Doesn't really explain on its own where it could fit in a larger roadmap. And I think there are two important points there. The first one is, like they said, this entire SSZ fication thing, which enables the proofs on the execution side and further down the road also leads to decentralization of JSON RPC. Because that needs proof if you don't have a trusted server anymore. And I also added to this document a similar thing for the beacon state where we can decentralize the checkpointing sync over time, with something called Beacon states and app sync Sahari presented an idea last year in Austria about that as well. And that one also needs tiny change to the beacon state as the proposal is right now for enabling backfilling of live client data in a canonical way. So the two things that could be done in Electra to enable all of this are these backfill enabling on the consensus side, and also the SSZ proposals for transactions receipts. And the three roots like those Merkel contribution tries. So I'm inviting everyone to just read this document and see if this vision is something that aligns with where Eetherium should go. And also, if someone wants to hack along, I think creating a demo that actually is based on these ideas would be interesting as well, and could be a small shadow fork with like one EL or so just to see how these SSZ transactions would work in practice. I mean, right now I have the website a slight XYZ. It works by locally converting everything from the mainnet, but it would be nice to have it intellectual as well. Yeah, that's what this document is about.

**Danny** [44:57](https://www.youtube.com/watch?v=FgOuUEgguN0&t=2697s): Thank you. Yeah, I mean, my take years that my clients, unfortunately, are the seven to 10 party on everyone's list all the time. So I appreciate you putting the stacking together. And I would encourage, you know, the person on each team that is paying attention to like clients, to please take a look at this and comment any questions for your time today? Okay, any other comments on this? Okay, any other discussion points for today? Great, we'll keep our eye on that mainnet shadow fork and keep moving forward this mainnet launch. Congrats everyone. Thanks. Talk to y'all soon.



## Attendees

* Danny
* Pooja Ranjan
* Ansgar 
* Dapplion
* Francesco
* Vasilly
* Bayram
* Sergei Lakovlev
* Joshua Rudolff
* Etan (Nimbus)
* Echo
* Justin Traglia
* Pk910 
* Barnabas Busa
* Stokes
* Alto 
* Paritosh
* Potuz
* Peter
* Terence
* Radek
* Guillaume
* Gajinder
* Javier
* Nflaig
* Mehndi Aouadi
* Enrico Del Fante
* Mikeneuder
* Kolby Moroz Liebl
* Matt Nelson
* Saulius Grigaitis
* Hasio-Wei Wang
* Steven Quinn
* Toni Wahrstaetter
* Justin Florentine
* Paulyashin
* Pawan Dhananjay
* Mikhail Kalinin
* Ben Edgington
* Carl Beekhuizen
* Stefan Bratanov
* Caspar Schwarz-Schilling
* Trent
* Nikita Tumanov
* Danyal Hanif
* Ansgar Dietrichs
* Spencer-tb
* NC



