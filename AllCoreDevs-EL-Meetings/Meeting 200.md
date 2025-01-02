# Ethereum Core Devs Meeting #200
### Meeting Date/Time: Nov 7, 2024, 14:00-15:30 UTC
### Meeting Duration: 1 hour 30 mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1190)
### [Video of the meeting](https://youtu.be/DqdmqDtm2wM)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | Video ref |
| ------------- | ------------------------------------------------------------------------ | ------------- |
| 200.1 | **Pectra Devnet 4 & Mekong Updates:**  EF Developers Operations Engineer Parithosh Jayanthi said the official blog post announcing the Mekong testnet has gone live on the Ethereum Foundation website. The blog post details the ways that application and tooling developers can join the testnet and start experimenting with the EIPs in Pectra.
| 200.2 | **Pectra Devnet 4 & Mekong Updates:**  Jayanthi also said that his team plans on deprecating Pectra Devnet 4 soon. Geth developer Marius van der Wijden said he had planned on doing some testing on Devnet 4 over Devcon, an Ethereum developer conference starting on November 12. So, Jayanthi said his team could keep Devnet 4 running during Devcon and reconnect with developers on an appropriate time after the conference to shut down the devnet.
| 200.3 | **Pectra Devnet 4 & Mekong Updates:**  Mekong, Jayanthi said there was an incident on the testnet where the head vote percentage was “extremely low”. Jayanthi asked if any developers on the call investigated this issue. It did not appear that any developer had. Jayanthi said that his team would debug the issue over the next few days.
| 200.4 | **Pectra Devnet 5 Preparations:**  The proposed changes to EIP 7702 discussed on ACDE 199 have been implemented by a developer with the screen name “Frangio”. Beiko asked if there were any objections to these changes. Given no objections, Beiko confirmed these changes will be added to the specifications for Pectra Devnet 5.
| 200.5 | **Pectra Devnet 5 Preparations:**  Geth developer Felix Lange proposed refinements to the fee logic of the withdrawals contract detailed in EIP 7002 (Execution layer triggerable withdrawals). Lange’s proposal raised some concerns from other developers on the call. Beiko recommended that developers continue the discussion about the refinements asynchronously and aim to come to a final decision about them on before the next ACDE meeting.
| 200.6 | **Individual EIP Activations:**  Ethereum Foundation Researcher Alex Stokes raised questions about how developers could test PeerDAS on a “Fusaka” devnet without activating other code changes that have been included in the Fusaka upgrade like EOF. For more background on this topic, refer to prior call notes or the podcast summary on ACDC #145.
| 200.7 | **Individual EIP Activations:**  Nethermind developer Łukasz Rozmej said that his client by default offers fine grained control over the EIPs activated at a specific epoch. “So, we don't generally have a concept of hard fork [in our client]. We generally set all the EIPs separately to the same number activation. We don't have the ‘Osaka’ parameter. We set those EIPs [individually] and that's it,” said Rozmej.
| 200.8 | **Individual EIP Activations:**  Lange said the reason Geth does not have this fine tuned control over EIPs is due to the concern that activating EIPs individually may introduce additional complications in code. “For example, when we load the chain configuration in Geth, we also check that the forks are not activated out of order. So basically, you cannot have a fork without a previous one or something. These features because they are meant to be activated on top of each other, if we had the ability to selectively disable certain EIPs or only enable some of them, it could create these weird situations that the client isn't designed to handle, and we do not test these configurations either, so the outcome is basically undefined,” explained Lange.
| 200.9 | **Individual EIP Activations:**  Rozmej said the reason the Nethermind team opted for such fine tuned control of EIP activation in their client is because their users wanted to repurpose their client for use on different blockchains where certain EIPs are activated, but not the whole suite of EIPs. Rozmej said to address Lange’s concerns, they can add labels to the EIPs such that EIPs with the same label can be activated at once by default.
| 200.10 | **eth/70, Sharded Blocks Protocol:**  Erigon developer Giulio Rebuffo proposed a new EIP to extend the functionality of the Ethereum wire protocol and offer a short term solution to the problem of history growth. Rebuffo said that based on his research, validators will be required to operate hardware with at least 4TB of disc by mid-2025 due to the growth of history data. He said the alternative solution for pruning history data, EIP 4444 and the Portal Network, will not likely be ready in time to prevent validator node operators from having to update their machines in roughly 6 months.
| 200.11 | **eth/70, Sharded Blocks Protocol:**  Rozmej pushed back on Rebuffo’s proposal asking what aspects exactly about the Portal Network were not ready in his view for clients to start utilizing it to prune history data on Ethereum nodes. Beiko said that he could follow up directly with the Portal Network team to get more information. Jayanthi added that he would like to see updates about the security audits of the Portal Network first before considering it as ready for implementation and use by all clients. Lange posited that integrations with Portal have not started in earnest due to the fact EIP 4444 is not “on the critical path”, meaning it is not a required EIP for an immediate hard fork.
| 200.12 | **eth/70, Sharded Blocks Protocol:**  Rebuffo said that in his view management of history should be determined individually by client teams rather than standardized through a protocol like Portal. “We are not keen to support Portal Network over the long-term,” said Rebuffo. EF Researcher Ansgar Dietrichs agreed with Rebuffo’s sentiment saying that there was “no inherent reason to standardize” how clients prune history data, as history data is not required for nodes to reach consensus. Rebuffo and Beiko recommended continuing the discussion on paths forward for history expiry in-person at the upcoming Ethereum developer conference Devcon.
| 200.13 | **EIP 7610 Potential Removal:**  On ACDE #182, developers agreed to include two retroactive EIPs in Pectra that do not introduce any new features to Ethereum but rather constrain and formalize rules of the protocol to avoid specific edge cases. Paweł Bylica, an Ethereum Foundation developer working on the EVM, shared concerns about EIP 7610 related to unexpected difficulties in its implementation among clients like Erigon. Before removing the EIP from Pectra, as suggested by Beiko, van der Wijden recommended reaching out to the authors of the EIP to get their thoughts on Bylica’s concerns. Van der Wijden also asked if a counter proposal to EIP 7610 could be created to compare alternative solutions to addressing specific edge cases in the Ethereum protocol. Bylica agreed to write down what he had in mind as an alternative and discuss the matter asynchronously with EIP 7610 authors.
| 200.14 | **ACD Call Schedule:**  Next week’s ACDC call will be cancelled. There will be an in-person gathering of Ethereum developers at the Devcon conference. The last day of the conference will be dedicated to breakout discussions about important topics in Ethereum’s development roadmap. More information about the schedule for this day, November 15, can be found here. Finally, Beiko announced that the Monday testing call on November 18 will be cancelled and held on Thursday, November 21 instead. There will be no ACDE call on November 21.

**Tim**
* Okay. And we are live. Welcome, everyone to Execution Layer Meeting number 200 today. Woo! Okay. There's a bunch of us already in Thailand. Other people are on their way, but we have a few things on the agenda to cover. updates on Pectra, couple spec, discussions around seven, oh two and 7702. new testnet that just launched, Mekong. And then if there's any spec updates for Devnet five will cover them. then a couple other topics around EIP activation. New proposal for an ETH protocol and an update on EIP 7610. yeah. I guess to kick us off, we have, Perry on the call. Do you want to give a quick update on the devnet? 

**Parithosh**
* Yes. So to start off with, we have a new, devnet that's been announced today. It's called the Mekong Devnet, testnet. And the idea is that it's a test net that's meant to be used around Devcon, as well as by wallet developers, etc. over the next weeks, or potentially even a month or two to test out all the features that we want to ship in Pectra. It relies on the Devnet for spec, considering that we're still modifying some things on Devnet 5. So it's live. Please have a look at the landing page. You can find faucets. There's a guide for how to run a node. There's already a FAQ. So the FAQ is something we're going to carry on for Pectra as well. So if you're questioning how it's going to affect you as a validator or how it's going to affect you as a node operator or anything like that, please have a look at the FAQ and take part.
* We're hoping that over the Devcon week, people use this testnet for a lot of experimentation and hackathons. So that's the first big upgrade. Our first big announcement and I guess the I don't know, you want to say something about Mekong or should I continue with that for updates? 

# devnet-4 [18:40](https://youtu.be/DqdmqDtm2wM?t=1120)
**Tim**
* No, please go for devnet four. 

**Parithosh**
* Okay. Yeah. So Devnet four is something we want to deprecate soon. the question is just do we still, need to keep it up for some debugging, or could we delete the devnet, considering it's the same spec as Mekong? I guess we could reproduce whatever we need on Mekong. Okay, if there's no objection, then we will delete the. Sorry. Go ahead. 

**Marius**
* I'm kind of wondering. I would like to do some experimentation over Defcon, but. And, like, I'm wondering whether it would make sense for me to do that on Mekong, given that it might introduce instability. 

**Tim**
* Yeah. If we do want to do makes sense that maybe keeping them for a week or two so that we can yeah, spam it and stuff like that. 

**Marius**
* Yeah. So that would be ideal. 

**Parithosh**
* Okay. Yeah. We can leave it up for the next couple of weeks and then I guess discuss it again once that is over. the only other topic was that in Mekong, we noticed that for a couple of epochs, the, head vote was head vote percentage was extremely low. we still haven't started properly debugging what's happened? I know that Zattoo captured a lot of attestation, so we people are kind of on route, so we haven't, dug into who's working wrong and why. but in general, the network is stable. So I'm wondering if anyone else has had a chance to look into what's going on there. Okay, then I guess we'll figure it out over the next days and weeks. An update for that. I think that's all the updates from our side. 

**Tim**
* Sweet. Thanks. any client team have updates they want to share about Devnet 4 for Mekong? Okay. if not, there were two pectra spec, changes that people wanted to discuss. We should chat about those and then see if and how they affect the Devnet five spec. first one was, actually. Sorry. Let's do a 7702 first. Frangio, had a PR up, I believe, since the last all core devs, that's been, discussed on Eth magicians. I don't know, is Frangio on the Ncall. Do you want to give a bit of background and. Yeah. 

**Frangio**
* Yeah. Not much has happened, honestly. I updated it according to what we discussed, which was, that the ext code copied, just for example, returns only the prefix, not including the delegation target, which is more similar to EOF. that's all. I don't know what would be the next steps for this, or if there's like consensus on accepting this and it could be merged, but I don't have the ability to merge it, so need to be mad I think. 

**Speaker F** 
* Yeah. Thanks for the update. on the last call, I felt like it was a generally okay thing and was hoping to give people some more time to review this change, but I'm pretty happy to merge it today unless someone has a concern or question about it. 

**Tim**
* Oh, okay. Nethermind. Seems in favor. Okay. I think yeah. If there's no objections, we should go ahead and merge it. Add it to the Devnet five spec, and if there's any issues with the change that comes up, we can open another PR in the future. But hopefully, yeah, we can move forward with 7702. Any other comments on the EIP? Okay. Frangio we're merging the PR. I'll comment in the chat as well. okay. Sweet. Anyone on the agenda? Felix had a PR update the contract in EIP 7002. Felix, do you want to give a bit of background on yours? Yeah. 

# Update EIP-7002: return fee from getter and add usage example EIPs#9024 [23:26](https://youtu.be/DqdmqDtm2wM?t=1406)

**Felix**
* So sorry again for adding this in the very last minute. so basically this has been ongoing in discussions for a while. So it's one of the basic things in the  7002 contract, but also the 7251 consolidations that when you basically the fee that is required to add requests into the system contract is a dynamic one. So this means, the users may overpay fees, unless they use the specific mechanism in the contract to, query the fee before they add their request. And I felt that, it would be kind of important. First of all, to give an example of this in the in the EIP, because it's kind of hard to use actually. And also just to clarify that like there are certain like certain conditions have to be met for this to work at all. And then while working on this example, I also realized that the contract could be changed to make it easier to perform this operation.
* So, basically, I'm proposing to change the contract to directly return the required fee. that needed to add, a request versus before where it was returning, like some other value that you could then use to compute the fee yourself. This is like a kind of a detailed change, but I felt that it's a change nonetheless, so it may be required to discuss it here. I honestly don't know why it was, I mean, why it was done the way it was done before. but. Yeah. 

**Tim**
* Okay. Yeah. Thanks, Felix. Anyone have thoughts? Comments on the PR? I guess, and yet, not that this is like the most important thing, but we do have audits on these contracts that have begun. And so we should consider this as we're, you know, thinking about making potential changes. 

**Felix**
* But yeah. Yeah. So there are some the audits are ongoing, but there will be changes resulting from the audits as well. So it's not like the contracts are final anyways. So that's I was also more generally interested to, to hear like just to make people aware that like these kinds of complications exist with the contract. It may not be obvious to everyone like that these contracts behave sort of in the way that they do. also when it comes to, for example, selecting the caller address and stuff. So yeah, this is just why I propose it here. I guess it's a bit too late. Like maybe we could discuss it the next time or something. I don't know, it's maybe a bit late to bring this in anyway, seems there are no comments so we can just move on. 

**Tim**
* Yeah, I guess last call if anyone has had the chance to review this. otherwise I would also try to get people to review it async and not wait, you know, entire ACDC cycle to make a decision here.

**Speaker F**
* I will say I'm supportive of it and reviewed it. I think it makes sense. but if other client teams want to weigh in, please do. 

**Tim**
* Okay. yeah. Let's keep discussing this async and then maybe track the PR for both this one and 7251 devnet 5 If we decide to move forward with it.  Mario asked, what's the ASM branch with the source? 

**Felix**
* Yeah, I link it in the PR. Basically it's in the it's in the pull request. It's not actually a yeah, it's more like a proposal. I also feel like maybe it's kind of weird, like for client teams to make decisions on contracts, but we have to figure this out another time anyway. Yeah. 

**Tim**
* Anyone else have comments? Questions on this? Okay. yeah. So if people can review this async. and yeah, we can potentially come to a decision before the next call. those were the two only spec changes proposed. Was there anything else on actual implementations or dev notes that people wanted to talk about? 
* Okay. And then I guess, aside from these two changes that we discussed. So we'll move forward with the 7021. we'll review the two changes to contracts. Is there anything else around Devnet five specs that anyone wanted to bring up? 
* I guess that's everything for Pectra. next up on the agenda. So there was a discussion point on the last ACDC, about Fujisaka testing to see whether Els could have the flexibility to unset features even when there's a hard fork encoded. Alex, you put this on the agenda. Give some context. 

**Speaker J**
* Sure. Yeah. So this kind of came up, thinking about PeerDAS and testing it in the context of Osaka. And I'd like to give a concrete example. Let's imagine that we have Osaka nets that have both pure DOS and EOF. It'd be nice to be able to like, test pure dos things without any complications from  EOF. It'd be nice to test EOF things without any complications from pure DOS. So I was wanting to get a temperature check from ELs around feasibility here. Like ideally there would be some way to, say unset like a fork epoch or fork timestamp, for a particular set of features. And from the last call, like CL clients I think were pretty okay with this. And I wanted to see what ELs thought around feasibility here. 

**Tim**
* Oh, yeah. Danno. 

**Danno**
* Would this be a separate line for each IP, or would it be like some combo activation? 

**Speaker J**
* I think whatever. Like the simpler thing would just be to basically say only a self work or only an elf work. And so if that's like easier to implement, I would say that I think what we care about most is just isolating L from CL changes. so yeah, we don't. 

**Parithosh**
* Need like I think one example could be to use something like eof time. so it doesn't matter if we actually set up, the time, but you are basically activating on EOF time. 

**Speaker J**
* Okay. Like it's already possible is what you're saying. 

**Parithosh**
* No, that that's our proposal. Yeah. 

**Danno**
* Yeah. We've been doing that special purpose for special EIP. I'm wondering if we're going to do this, if we should get a formal, more extensible, purpose for this. So, like, we could say, Osaka plus 79. No. No. -7692. + 6603. So we could get some sort of a long definition for that fork. for a couple of reasons. One of them is what if there is a what if we do Osaka, add one and then turn on EOF at another one for longer standing devnet or testnet. But also this is something that's a pattern that I think might be useful. in layer twos. So layer twos might say, well, we want to do Osaka, but we want to turn on this layer two specific feature and maybe turn it off later. And it's done by an EIP or a rip. There's a rip. They want to activate like native accounting a so they want to say Osaka plus native accounting. So I think if we're going to do this, this is the right time to do a generalized notation.
* I know years ago geth had proposed fork plus EIP where you do plus EIP to add extra EIPS. so if we do this I would like it to be a generalized solution. So we know as client devs to just build that pattern in everywhere that we need to, know. There's a subset of ones we could do some support of via chain spec. Get support to via specific EIPS. but if we could get it in general, it would just solve a lot of problems beyond simple testing. 

**Tim**
* Lucas says Nethermind supports this out of the box. I guess Lucas does. Never mind support. Like, the most general version of this is what Daniel was describing. I we can't hear you if you're speaking. 

**Lukasz**
* Can you hear me now? 

**Tim**
* Yeah, we can actually. 

**Lukasz**
* Nethermind, supports with chain spec. as if the EIPS are not related to each other, right? We can. We can have them separately activated if there are related to each other. either you need to activate. You need to activate both of them. Right. If they are somehow related. But if they are not, you can activate each one. Each one separately. through chain spec? Yes. 

**Danno**
* Does it support deactivation like deactivate PeerDas well? 

**Lukasz**
* You wouldn't activate it, right. And that's deactivation. 

**Parithosh**
* You just set it to infinity usually. 

**Lukasz**
* Yeah. 

**Danno**
* So you would you could set Osaka which would be default have PeerDas. But you could separately set PeerDas as activation and set it to ridiculously high number. 

**Felix**
* No that's not how it works. 

**Lukasz**
* So we don't generally have a concept of hard fork. So we generally set all the EIPs separately to the same number activation. Right? We don't have Osaka as a parameter. We set those the EIPs and that's it that are in Osaka. So we have fine grained control over EIPs. 

**Speaker J**
* Okay. So it sounds like ELs are on board with the possibility and then it's just figuring out different functionalities. Yeah. It's like yeah. Any other eels are here and could chime in to what they support today. It'd be nice to know. 

**Tim**
* Yeah. Felix. 

**Felix**
* Yeah. So I just wanted to mention. So this has been a long standing issue in general that there are, two conflicting formats for specifying the configuration.  configuration of the ELs. there used to be more than two, but now it's sort of settled down where most EL now. Use this format, that also uses where we have to fork names and their activations and then. Nethermind. I believe maybe Reth as well has the. I mean, I think Reth supports both. Kind of. I'm not sure. but anyway, so the chain spec is a more general format that was invented, way back by parity to allow very fine grained configuration. And it's great, but I feel like from a usability point of view, it is kind of overly flexible. And it also requires the client to be able to actually activate all these features separately, which may not be possible.
* So or maybe it's like it just adds an additional complication in the code. Whereas with the with the simple like fork named activations is much clearer. 

**Felix**
* What can be activated together and there cannot be unintended code paths. So for example, when when we load the chain configuration in Geth, we also check that the forks are not activated out of order and they are not. So basically you cannot have a fork without a previous one or something. So these features, because they are meant to be, activated on top of each other, if we had the ability to selectively disable certain EIPs or only enable some of them, it could create these weird situations that the client isn't designed to handle. And we do not test these configurations either, so the outcome is basically undefined. and for this reason, I think we've always learned more leaning towards just having this simple fork based configuration. So personally I would not support in death having these very fine grained EIP based activations.
* However, I know it can be frustrating if you want to test some features or maybe  some other standard needs to be developed. I wouldn't necessarily be against having this for the duration of the development cycle of the fork. For example, like if we had some feature where it's like during this time where we are still actively exploring certain features, maybe we could have a list of like certain extra feature flags that are supposed to be enabled or something, but then it wouldn't necessarily be possible to apply this forever. Like this. These features would not be available. Like, let's say once a fork is shipped, we would basically remove this visibility. 

**Lukasz**
* So one thing why we won't be removing this ability is that sometimes some people want to use Nethermind on different, on different networks. And they want to activate only some of the EIPs there. So this is where the fine grained, part helps us. What we can add potentially is, for example, like labels that you could label, for example, Cancun or Prague, and it will activate all the EIPs like by default on the same. So kind of labeling, that does it. But we won't remove, fine grained by itself. 

**Felix**
* Yeah. I'm not asking you to remove it. It's just more about like when you guys basically have the most general version and you have been supporting it. So I'm not saying it should be removed. It's just that for the other clients, it's basically going to lead to some situation where they then have to consider how to like in which like they basically have to undo their existing configuration mechanism and it introduces like fine grained thing underneath. And then the question is also, yeah, is this going to work or does it make sense. So I think it's a it's kind of a broad topic actually trying to figure this out how how to do this best. 

**Speaker J**
* Yeah I think for at least for like testing for Osaka with like the context of PeerDAS, we can get away with the Osaka grained thing. So then the question would just be like do you today support this Osaka grained. I mean, I guess you would just set the Osaka timestamp to again some huge number. And it sounds like that would do what we want. I don't think we need to get into this can of worms of like the final grained resolution, even if it's nice in other scenarEOF. 

**Felix**
* Now, I think for certain features it does definitely make sense. For example, we also have, like a setting for, for activating Vercal even now because it's not defined in a fork yet, but it's under development. So you can basically already kind of activate it as under this name. And it's kind of treated as like a fork. So at a certain beyond a certain size, like a feature will basically be like a fork. So for example, EOF is kind of same like I'm not sure 100%, but I think it also allows activating EOF separately just for the purpose of testing it. But I wouldn't want to be able to activate like individual EOF EIPs Eth for example. 

**Speaker J**
* Yeah, that makes sense. 

**Tim**
* And so what we could do then is if we want to have a dev net that's testing EOF but not PDAs is we have the EOF timestamp before PeerDas and then vice versa. If we want to just test periods without EOF. Is there any client team for whom that would be problematic? 

**Danno**
* In testing, you always had all sorts of bugs. So we have multiple activation targets for EOF. It's really, honestly, it's hurt the progress of EOF to have multiple forks that it activates on. And we've always had problems with tests targeting multiple things, client supporting multiple things. If there's multiple targets for you to activate, it's going to cause problems similar for PeerDas

**Tim**
* We couldn't just have a if we want to do a PeerDas devnet, we just do it and not activate the EL side of the fork and vice versa. So instead of having like two times, you just run a Devnet where effectively the full loop part, but not the Osaka part of the fork has activated or vice versa. Is there any issues with doing that? 

**Felix**
* Yeah, that wouldn't work because of the engine API. Like it's kind of a this is also an untested path, kind of because the engine API versioning kind of goes along with the forks. So then you'd have to there would be special logic in the client. 

**Tim**
* Engine API version though. Like what? because I don't know. This PeerDas does change the engine API. EOF doesn't change the engine API. 

**Marius**
* Any at the. 

**Parithosh**
* Moment it's fine, but eventually we will be changing it. So I guess for now, kind of our plan has been for the world. We just use legacy versions like latest master Geth, which doesn't have any changes for full anyway. And for EOF we just use legacy versions of the CL. that kind of achieves the same thing. And then we deal with the problem when we want to integrate the two. 

**Danno**
* Yeah, EOF is zero dependencies on CL changes, so that would actually work. 

**Parithosh**
* Yeah, that was kind of our plan for now, in case we could figure out some sort of shared activation strategy then we would love that. But it sounds like it's something we can also talk about in the testing session. But for now I think we have like a plan. 

**Tim**
* Okay. Anyone have concerns with that? Otherwise, yeah. We can bring this up in a testing call, but it seems like a path forward, at least for this fork. Okay, sweet. next up, 

# eth/70 - Sharded Blocks Protocol [42:05](https://youtu.be/DqdmqDtm2wM?t=2585)
**Tim**
* We had, I believe, Julio and another team wanting to present h70, which is a new, ETH protocol to allow nodes to communicate a subset of blocks that they have locally. are either of the authors on the call right now? Oh, yeah. Oh, both of them are. Yeah. 
* Do you want to give a quick overview of the EIP? 

**Giulio**
* Yes. So basically it's it's mostly so that you can basically. So this is the rationale just to just to clarify the version of the EIP is just actually to, to define a framework that is already already in use in consensus layers to basically shard the history across nodes. So this is kind of a short term solution to a P for force. so as, as already talked to some people recently, soon to run a validator comfortably, you will need four terabytes of disk because you will exceed the needing to terabytes. And the hardware requires power of two. And this is going to and it's taker told me this is going to happen approximately mid 2025. Almost first half of mid 20 of Q2 2025 approximately. So there. So I talked to some people and there seems to be some urgency. So this is basically a short term solution for a short term alternative to portal, which seems to be a bit more far away than, than than six months.
* Last time I talked to them unless I misunderstood. so the what is the EIP. So now I can explain the rationale. What is the EIP actually does? Is it basically advertise, a basically divided the chain into chunks of set sized chunks. And each node, when it's first bootstrapped, selects random a bunch of random chunks, which then backfills, which then basically syncs, by just verifying it against the other chain. So you still keep the other chain, but you keep only a small section of the transactions chain. And what then happens is that they advertise through a bit list or a bitmask as the, as some people from the Besu team suggested,  which shards they have so that when a node wants a specific block, they just, cycle through the shards.
* What's actually cool is that since we have support for inner in P2P, we can just put in the inner. And just by looking at the Eth note without even connecting, you can just discard the PeerDas and move to the next one. And the other cool thing is that if you choose a sane shard size, you can have really  big shards and very few shards, and it's actually very easy to rotate. rotate the PeerDas discovery  to find nodes that have the blocks you want. you, you probably don't even need the something like the meta even for something like that, because it's just rookies numbers of shards. So yeah, this is kind of the proposal. It's just a shards solution just to the problem, if anything. but yeah. That's it. 

**Tim**
* Okay. Thank you. there's some comments in the chat saying, you know, why do we want to work this in if Porto is going to be there and that maybe it's significantly simpler? Yeah. Anyone have thoughts or comments? Okay. I mean, if not, yeah, I guess people can review this. 

**Lukasz**
* I have a comment because okay, this is fine, let's say. But what is the incentive of people to keeping any, of this? Why wouldn't someone delete all its history? There was. 

**Marius**
* But there was never an incentive in the first place for people to keep all the history. So I don't know why this matters. 

**Lukasz**
* Well, it would have to. Mhm. Go ahead. 

**Felix**
* So maybe just a quick comment about this. So this solution  definitely makes it a bit better because compared to the  to just having to keep all of the history because I mean you are not incentivized to, to, to, to keep any of the history. But if you have to keep less by default, you're maybe less incentivized to turn it off. 

**Giulio**
* And and just I just want to clarify again, like it's very unlikely that portal I think will be ready by the time we will need four terabytes. So I mean, I don't know, that's that's at least what I heard from people that it's probably not going to be ready by then. So this is just kind of the all the this is the way you can probably avoid having people having to stock up on you on more drives. But yeah, that's kind of it. 

**Lukasz**
* Well I'm not I'm like it's not the first hand information. But from what I said the receipts and blocks networks are ready. The history network. And as far as I know Ashraf from our Ashraf is from our team is working on integration and he was able to download them without a problem. So not sure what's not ready about portal. 

**Marius**
* Yeah, but that's just another word. 

**Ahmad**
* What other. Portal. Supporter. 

**Lukasz**
* Yeah. Working on portal, supporting other teams might be harder. I'm not sure if some of the teams can leverage, existing portal clients because they are, for example, in the same language. We couldn't really but yeah. So not sure if that's the, the readiness was about portal or was it about, integrating portal into the clients? And I would if there's something about portal, I would love to hear it. So. 

**Tim**
* Yeah. I don't think there's anyone. Oh, Felix. Actually. Yeah, sorry, I don't think there's anyone on, portal or from portal on the call. but we definitely should follow up async with them on this. And then. Yeah. Felix, you had your hands up. 

**Felix**
* Yeah. I just quickly wanted to make a comment about it. So my own personal opinion is that the portal is fundamentally a better solution to this problem because it requires it requires you to store even less history. So it's more of a dynamic system. Whereas this IP, as Julio presented it, is a short term solution that is kind of yeah, I mean, it does something, but it's not very configurable. So I don't think it's like the ultimate solution to the to the history distribution issue. However, like if we can get it implemented and test it, then it may be a good candidate for just, you know, shipping. But in order to ship this, I don't think it's so easy as to just make a quick decision. And yeah, we're going to have this and done, but we need to integrate this into the sort of testing process that we have as we have it for other features as well. So for example, we would have to kind of, I don't know, create a dev net with this, for example. And then the issue may arise that this is a solution that is kind of specific to the main net. Like, yeah, technically we can also shot the history of the test net, but the test net only will have a very short history.
* And usually now even for testing, we only create these very small networks. So we would have to figure out how to set the parameters, for example for the test net. So they make sense. Or maybe this feature should never be enabled in any test net. But then we we basically only have to test it via the managed shadow fork or something. So I think before we fully commit to this solution, it's not a bad solution. 
* We have to figure out how this can even realistically be deployed. I wouldn't want to just turn it on. I think we would have to agree in the clients on the implementation and stuff like that, and we do have to test it as well. And when it comes to portal, I think the portal network itself, the specification and the clients, they are kind of ready. They have been following the mainnet for some time with their history storage. So it is in a way a already tested solution. And as Luca said, it's mostly the question of integrating into the clients, which may be an issue because, yeah, it's basically this integration has not happened because portal right now is not on the critical path, but the protocol itself is a pretty solid one when it comes to the history. And I can attest that, yeah, it is absolutely their goal to have something that is ready. And from their perspective, it is kind of ready now. So yeah, this is something to be considered as well. 

**Tim**
* Thanks, Felix. and there was a question as well in the chat about whether, this there's been like a security review on, I assume the new, the new proposal, um. 

**Parithosh**
* Given that there was about portal in general, because if we're assuming that portal is ready, then I think it also needs to go through the security stuff. 

**Tim**
* Yeah, yeah, as. 

**Felix**
* Far as I know, it is on the it is on the path to basically getting reviewed by all kinds of security focused people, but I have personally don't know how how far along it is on that path. yeah. 

**Parithosh**
* I mean, we need an implementation first, right? My main concern is, say you have a portal node. Chances are it's on the same host as the EL and CL, and if there's a DOS vector in portal, you can essentially take down the rest of the host for free. 

**Felix**
* I mean, the clients do exist, so it's not like they don't exist. They can be tested now. It's not like a like portal is an implemented system, but it is kind of separate right now from, from the main clients. 

**Giulio**
* Yeah. But I think that the main question so I agree with everything, all all people are saying in the comments and everything, you guys are all saying that portal is the final solution. so it's just about whether people will be ready by then, because at least when I talk to some people. I'm not going to make names, but I think that there are differing opinions, even even within teams. But some people I spoke to were very skeptical of portal, and even portal guys told me that at least, at least some weeks ago that, unless I misunderstood, is that they were planning on trying to get some test nets into actual production in six months, and by then we will need four terabytes. and by the way, the four terabytes are uncomfortable, are validated. Right? So, yeah, I mean, you can ask for those numbers. I'm not definitely that sure about the validity of that claim either, but I think it comes from a reliable source. 

**Lukasz**
* But this is about history network because portal is also working on the state network and state. 

**Giulio**
* Yeah, the state, I think it's I think the state network though, it's. No, no, I'm talking about. Yeah. I mean the requirement is history plus state. Of course that's the two tier where the four terabytes comes in. Um then whether whether Porter is working on the state. I don't I don't I don't think it's very relevant because state is not the biggest thing in the pipeline. 

**Lukasz**
* But. Well, they are working on the archive state. So it is. Yeah. I mean. 

**Giulio**
* Yes, that's that's cool. I'm just I was just saying that it's it's 80% of the stuff is in history. That's what I was saying. 

**Felix**
* Yeah. I'm just going to come in now. so basically the another important question for this is if we can just live with basically removing the pre-merger history like this would be a simpler change to make. And when we are talking about sort of like emergency solutions to remove some of the history from the nodes, then this would also be an obvious one. I suspect that very few nodes actually require the pre-merger History and if they need it, they can get it with portal or they can download it in some other way. This is something that famously, Aragorn has had a solution for this for a long time, where basically, if you want the history, you can get it outside of the Ethereum P2P network. And I think this is something that will persist even in the future. So if we just want to make a quick change, we should maybe create an alternative EIP as well that just says you are not required to store the pre-merger history anymore. And this would then go with this previous proposal for the ETH protocol where we would announce, I don't know, the cut off for the data that we have or something. And yeah, I mean, it would remove kind of the same storage. 

**Lukasz**
* History, smaller and smaller. It's not that big at the moment, and it will get even smaller in proportion to the rest of the history. So yeah, I don't see this as a at least it can be a stopgap, very stopgap solution, but it's not a final solution at all. 

**Felix**
* The other thing as well, right? I mean, it's kind of. 

**Giulio**
* I think this is kind of a a conversation that should be had in person. I mean, another thing maybe is that we should just say, because there are some kinds of solution to this. Like if everyone has that, neither man is close to death, as far as I understand from the call. So maybe the actual thing is to just say to everyone, just drop this story now and and everyone can just catch up later or something like that. That's also probably could incentivize people to work on it, but that's probably a conversation to have in person. That's also controversial. 

**Felix**
* Yeah, I mean, I would personally this has the the sort of argument there has always been that before we announce, before we make the collective decision to drop history, we need to be kind of sure what will be the way. 

**Felix**
* Get it back. And if we can all agree that, like portal is the long term thing, then. 

**Giulio**
* Need to be able to use the same method because I personally is not probably going to use port, it's just going to use torrents. Right? Because we can already do that. already. So and probably and maybe and maybe and I don't know if RAF has their own static file system. I actually don't remember if they download stuff from somewhere. but maybe they do. But I think that we should not enforce really in the longer run, like a way to enforce a way in which, you know, should get their chains. I don't think that makes much sense. But the main. 

**Tim**
* Reason why it does make sense, though, is you don't want every single client to have to effectively rebuild like a history network. And it would be nice, like say, I'm running Aragon and I want to switch to another mine. that there's like not a completely different way. So like there is value in standardizing this. Maybe we don't have to standardize on a single method. Like there can be different ways it is restrictive. 

**Giulio**
* If I have to be completely blunt. for example, portal is is is overall a better solution than portal? It's much more generalized. so I'm really not really keen on doing that because if anything, because it has its own disadvantage and it's just restrictive. I wouldn't I wouldn't force people to do it. Of course it's good to have, don't get me wrong. But I wouldn't enforce people force people to do it. Honestly, it doesn't sound like a good plan. 

**Tim**
* So you're saying we should just agree to drop history by a certain point in time and then let clients figure out whatever? Yeah. 

**Giulio**
* Yeah. And also, since and also people will actually be incentivized to implement the history expired at that point because every some other client is already doing it. So maybe people will actually start running towards it. Right? I don't know. Maybe that's better to discuss it in person. This is probably a controversial proposal. 

**Tim**
* Let's do. Okay. Let's do a couple more hands. But yeah, as you. Ansgar. 

**Ansgar**
* Yeah. I just wanted to very briefly kind of agree with Julio. And I said that in chat. I think that that, history is conceptually something that's much closer to like, the different ways that clients expose tracing capabilities or even they choose different database layouts where basically that that really very much is something where like if clients want to collaborate and coordinate and multiple clients share the same format, that's great. that's useful, but there's no inherent reason that's not part of the kind of the consensus, the sensitive parts of the protocol. So, so it really feels like that choice should be with the individual client. And I separately also think the way to ship this practically would probably be to agree on some sort of, point in time at which, I wouldn't quite go as far as to say that everyone stops, starting history at that point. It's just that, like, at that point, not every client would be expected to keep the history anymore. So at that point, it would basically then be that every client can just would be free to make their own choices. 

**Giulio**
* I mean, my opinion is that when whenever a client gets a way to get their history from somewhere else, they can just prune it by default. So the first ones will be probably never mind and arrogant because from because now I think like that is quite close and arrogant already have it and then gaffer should will follow suit probably later. And Basil too. I think that probably makes sense. Whenever some client is ready to drop it they can just drop it. I think that's my main idea. 

**Tim**
* Okay, let's do Lucas and Felix. 

**Lukasz**
* So I a bit disagree because if one client drops, history and the other client doesn't have a way of thinking. Archive. For example, you kind of break their their archive sync. So not not, happy to do that without the social consensus on that. but about the shard blocks protocol. So, I kind of the more I think I like it more, I need to read about the details a bit and, have more, maybe will have some feedback, but, I like it because it's really easy to implement. I think it could be implemented in a matter of months, let's say, in all the clients. And, yeah, it's simple. And even if we have portal network, at least for some time being, until we get, even bigger, confidence in it, it's another redundancy method. So overall I like it. And history should be redundant. So Yeah, I think it checks all the boxes for me. 

**Tim**
* Thanks, Felix. 

**Marius**
* Yeah. 

**Felix**
* So maybe some final note. It's, this is more about something that also Julio earlier said we, that there should not be clients should not be forced to implement these protocols if they have their own way, which is better? I kind of just want to say that it's not necessarily like for this topic is one and for peer to peer networking in general, it's not, supposed to be the way that, the peer to peer network, which is defined in specs, and shared by all clients is necessarily the absolute best one, but it is basically the common ground. So we would I would say that if we make the decision to take in Porto, for example, then portal will become a part of this common ground. So it's something that we expect the clients to support, even if they don't consider it to be the absolute best. And then I think treating it this way kind of changes also the requirements on the solution. So if the if the requirements are not to provide the best solution, but just some something that can reasonably be supported by all the clients, then it's.
* For example, it changes the, the, the assumption that like portal is kind of good at being this kind of common ground solution because it doesn't have a very large storage requirement. So if you have to keep some part of the history in a certain format only to satisfy portal, for example, then it's actually good if the protocol doesn't force you to store a lot. So for example, the big shots would be kind of annoying, but if you can have these like smaller shots, then as when? As with portal, where you only have to store like a couple hundred megabytes at most of history to to be like a good citizen in the network, then maybe it is way more acceptable to have portal as a solution, even if you don't totally like it. **Felix**
* It's just a way for people to basically participate in the network. on the on in terms of being like on the common ground. 

**Giulio**
* Yeah, I mean, I, I kind of agree, but on the same time, I would, I would probably I don't think, I, I don't think we, I think we need to discuss internally, but we are not really that keen to support portal network over the long term. And I'm at least maybe we can rethink it, I don't know. 

**Tim**
* Yeah, I think we probably have a good sense of people's perspectives for the moment, and we can continue the conversation both around Defcon and async. is there anything else? 

**Felix**
* This will surely be. Something that comes up at Defcon. 

**Tim**
* Is it, I guess. Is there anything else that someone feels we should bring up right now on the topic, or are we happy? Moving on. Okay. Sweet. Yeah. Thanks. yeah. Julio and Ahmad for drafting the app. And, Yeah, let's continue chatting about it on discord and around Defcon. Last one we had on the agenda today. So, months ago, we decided to,  unquote, retroactively activate EIP 7610, which, formalized some behavior around reverts for contracts creation if the account does not have empty storage. So this was effectively like an edge case that we decided to make explicit to fix. And it didn't affect any previously deployed contracts or transactions. we I guess the EL team was looking into adding support for this. we wanted to move this to final and wanted to raise on the call to check if anyone had any issues with that, and also to see if every client had actually implemented it. yeah. Pawel. 

**Pawel**
* hello? can you hear me? so I actually have some, like, second thoughts about this one. so, like, first of all, I think it improves situation from what we had, at least from my perspective. And because previously I had to delete all the storage, which I was not able to iterate over. Now I just need to know if the storage there is any storage or not. So it's like one bit of information, but actually I support with, with some bigger integration of, of EVM one, I spot an issue that even finding this information, it's not so easy in some contexts. and I need to build small infrastructure that serves only this, this purpose. So, and it feels like a kind of theoretical, case that we're trying to handle. So I kind of appreciate that, but I still think it's it might be a bit too much. So what I was starting considering if if we can just ignore the storage and just assume if there is any storage, it just stays there. But I'm not sure that's possible in this, in this way. So yeah, if there is option to further improve that, I would also want it to consider this. 

**Tim**
* Does anyone have. Thoughts on this. And I guess Paul, are you saying that, you could not implement it as is in EVM one? 

**Pawel**
* So on EVM one side, it's relatively easy. I just need, either less storage storage root hash or just a bull flag that says the account has storage or not. And that's how it. It has been implemented, but now the user of EVM has to provide this information somehow. And it turns out in, in for example, in Aragon, that's not so obvious how to get this information. Because this, this, this information is not in the execution subsystem, it's in the commitment subsystem. So it's like much bigger, hide like. Struggle to, to implement that. So I think Aragon hasn't implemented it yet to my knowledge. And I wasn't sure how to implement it either. so that's, that's the difficulty we have. And, and still this, this like single bit of information, it's only to, to handle the, the specific test cases that are likely to happen on real network. That's. That's the second thing. 

**Tim**
* Got it. Thanks. Yeah, I know you had your hand up. 

**Danno**
* Yeah. I mean, I was always when I looked at this, I was wondering why storage was not considered part of the empty account standard. Empty account was always, you know, notes balance. And, it was three items notes balance. And the third, the third thing. But it wasn't storage. so so putting this in, I thought fixed that so that empty account was all items had to be empty, but I. The ways to trigger this are almost impossible because you have to make it counterfactual, and delete it and bring it back. And now that we have self-destruct basically nerfed, it's really hard to trigger. So I don't know, I. Yeah. 

**Tim**
* Okay. Dragana. 

**Dragana**
* From our Arabian side, Red side. It's similar situation that Pablo described. It's harder to do. Basically we needed if we want to support fully to support this, then we are seeing this as the very edge case. That's very hard or impossible to trigger because you need hash collision. You need to add flag inside account and type account or for for for us it's account table with storage table. For us it's not account storage or separate tables that are with this app needs to be tight for us to support this. I think probably uh I think from get client they needed, they wanted to add or remove add these restrictions so it's easier for them to support some things. But at the end as this needs hash collision and is then said it's very hard to trigger or impossible to trigger, maybe to have maybe to reframe that AP to be to allow ambiguous result. But whatever happens. 

**Tim**
* I was not really sure. And I didn't work on this EIP, but I was just curious, like, how do you compute what the leaf hash of the account is? Because do you not need the storage route for that? 

**Dragana**
* Yeah, but we did we do that separately. When we execute the section we just touch account storage tables. But for Merkle tree we have different tables that have hash versions. 

**Tim**
* Okay. So I guess clearly this is not something that can be trivially implemented by the other clients. I don't know. It doesn't seem like the most urgent thing to make a decision on. but we have already said that it's, like, included. so should we undo that previous decision? yeah. Marius. 

**Marius**
* So I don't I don't really remember why we why we why we want why we were pushing for this. So I think it would be really important for Gary and or Martin to come on the call and, give a bit, a bit of background on this. unfortunately, they're not here today. if I remember, like, there are something like 28 such contracts or something. And all of this came up in a, in a refactor that we were doing. and yeah, it's, it's kind of, it's an edge case and I think it should be handled in like it should be defined. I don't know if we need to define it in this way, or if we define it in another way that wouldn't require us or wouldn't require the clients to, to to store this or to pass this to the EVM. So, yeah, I don't know.  But I think it's important for the ERP, authors to give their opinion on this before we pull it. 

**Tim**
* Okay. Yeah we can follow up async on this. Anyone else have thoughts comments about it? Okay. this was the last. 

**Marius**
* If it would be really nice if, if, if the people who are against this could come up with a different proposal, that defines this edge case, that they can, that they can actually implement. I don't know if that would be just deploying the contract, or whatever that, whatever that would be. most like smartest way. 

**Tim**
* Does anyone want to volunteer for this? 

**Pawel**
* Yeah, I can, I can I can write down what I had in mind as an alternative. but it can take some time also to verify other implementation. It's actually doable or not. 

**Tim**
* Yeah. I think if you can. Yeah, if you can at least write your proposals, that would be that would be really helpful. Yeah. Yeah. Thanks, Paul. anything else on this topic? Okay. that was the last thing we had on the agenda, aside from some scheduling stuff. But anything else people wanted to discuss before we wrap up? Otherwise, then. Yeah, just a quick heads up. next week, ACC will be cancelled because of Defcon. That said, on next Friday. There's a whole day Ethereum magician sessions at, or a whole day of Ethereum magician sessions planned at Defcon to cover a bunch of topics ranging from account abstraction to the future of the EVM block. Construction and issuance. And next, the week after Defcon on November 21st, we won't have a formal ACDC, but we'll have a interop testing call for people who are available. So yeah, that's it for the next couple of weeks. We'll see everyone at Defcon and yeah. Thanks all. 
* Everyone. Bye. Hi, everyone.


---------------------------------------

### Attendees
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

---------------------------------------




