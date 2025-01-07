# Consensus Layer Call 145

### Meeting Date/Time: Thursday 2024/10/31 at 14:00 UTC
### Meeting Duration: 1 hour
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1185) 
### [Audio/Video of the meeting](https://youtu.be/KMLqv60xg9w) 
### Moderator: Stokes
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
145.1  |**Pectra Devnet 4 Updates** EF DevOps Engineer Barnabas Busa said there were no major problems with Pectra Devnet 4. Client teams have implemented various fixes such that all clients are able to propose blocks on the devnet. Busa said that based on Pectra Devnet 4 specifications, his team launched a public Pectra testnet called Mekong earlier in the day on October 31, 2024. His team is working on creating a dedicated blog post and FAQ documented detailing how users can join the public Pectra testnet and try out the new features of the network. Busa said he foresees Mekong running for a few months for the benefit of the broader Ethereum ecosystem and will potentially shut it down before the end of the year. It is a large testnet supported by 110 nodes and approximately 100,000 active validators. Because it is based on Pectra Devnet 4 specifications, the testnet lacks certain features such as EIP 7742 (Uncouple blob count between CL and EL).
145.2  |**Consensus specifications, PR #3900:** This PR introduces a new attestation type for formatting validator and committee indices to simplify how attestations are processed. Developers agreed to move forward with this change and include it in Pectra Devnet 5 specifications.
145.3  |**Consensus specifications, PR #3767:** This PR removes certain time out responses when nodes handle data requests from peers and replaces them with a rate limiting recommendation. This is a backwards compatible change. Developers agreed to move forward with it and include it in Pectra Devnet 5 specifications.
145.4  |**Consensus specifications, PRs TBD:** Stokes said there are a few PRs in the works implementing tweaks to the way execution layer requests are handled on the consensus layer. There were no objections to this comment and Stokes said that developers will move forward with these PRs in Devnet 5 once they are ready.
145.5  |**EIPs, PR #8994:** Lodestar developer Gajinder Singh has recommended updates to the EL headers and gas fee mechanism under EIP 7742 (Uncouple blob count between CL and EL) such that the base fee calculation can respond more accurately to changes in the blob gas target. There are deeper revisions that developers could implement to ensure accuracy in the base fee calculation. However, based on the discussion, developers agreed to opt for the simpler changes suggested by Singh and delay deeper revisions to the base fee calculation to another upgrade.
145.6  |**Consensus specifications, PR #4000** Teku developer Mikhail Kalinin has proposed a PR to add missing checks to validator consolidation requests. Kalinin requested a review of this PR so that it can be finalized for Pectra Devnet 5.
145.7  |**PeerDAS Devnet Updates** PeerDAS Devnet 3 has been shut down after a reported 100,000 slot reorganization. Busa said that it was “unfeasible” for his team to try and recover the network after the incident. He could not share further details about the cause of the reorg. He mentioned that the Prysm team is in the process of investigating the matter.
145.8  |**New EIP: Withdrawal Credential Update** Lucas Saldanha, a Lead Blockchain Protocol Engineer for Consensys, has proposed an EIP to allow validators to update their withdrawal credentials without having to fully exit their validators. Since many new validator operations such as deposits, withdrawals, and consolidations, will be triggerable through a smart contract after Pectra, validator node operators may wish to update their withdrawal credentials such that they are managed through a smart contract. However, there is no way for withdrawals credentials to be updated unless the validator is exited. To avoid the need to cycle validators for the purposes of updating withdrawals credentials, EIP 7800 offers a mechanism for validators to update their withdrawal credentials through a new execution request type, "0x03". Prysm developer “Potuz” and Kalinin expressed their support for the EIP. While it will not be included in Pectra, it may be in EIP for consideration in a future upgrade.


**Stokes**
* Okay. We should be live there. And yeah, let's go ahead and get into things. So hey everyone, this is consensus layer. Call 145. I'll drop the agenda here in the chat. And yeah, a number of things for Pectra 
* PeerDAS and a couple of other questions. So let's go ahead and get started 
* To begin let's look at Pectra Devnet 4 is there any updates there worth going over, any open issues or questions we should discuss at the moment

  
**Barnabas**
* So as of the last week, there has been multiple different client fixes for those clients that were missing slots.in the last weeks. And it seems like everyone is able to now propose blocks. There are still a few, questions that we have open, but everything is, under discussion 

**Stokes**
* Good to hear 

**Stokes**
* I guess a related point, do we want to discuss the, public devnet that we were talking about based off devnet 4 

**Barnabas**
* Yes. so we were gonna announce this, maybe at the end of the call, but I guess we can already announce it right now. So we have launched a public testnet, which is going to be available for everyone to make deposits and exits and consolidations and everything. We had Genesis just three hours ago, and we have Electra getting triggered on it tomorrow on epoch 256
* Client teams can decide if they want to include this as a flag in their client. we are writing right now a frequently asked question documentation where we're going to explain how to run a node on this network. But yeah, if any of the clients are up to adding this as a default chain configuration, they are welcome.
* But it's going to run approximately three months or till possibly till, we can fork mainnet We expect it to be shut down by the end of the year. So it's it's not like a must have. It's it's a nice to have 

**Stokes**
* Cool. Yeah. 

**Barnabas**
* Yeah. We have 100,000 validators and, we have approximately 1000 validator per client, so it's about 100, 110 nodes. So it's a pretty it's a fairly big network It's also nice to do some stress tests here And yes, this is based on Pectra for spec. So it doesn't have 7742 requirements yet. And everything that is running on Pectra four should be also working on this, this name testnet. I mean 

**Stokes**
* Cool. And we went with for the name. It looks like 

**Barnabas**
* Yes 

**Barnabas**
* So we decided to use this name because the alternatives had, uh 

**Barnabas**
* Some, some coins already running on it, so we didn't want to be affiliated with that. 

**Stokes**
* And you said there'll be, like, some documentation coming, for, you know, the community to engage with it. 

**Barnabas**
* Yes. we have one that's working in progress right now, so I didn't want to link that, but 

**Barnabas**
* It's coming. Okay. And we have a general URL as usual to find all the links 

**Stokes**
* Cool. Thanks 

**Stokes**
* Great. Then. Yeah, it sounds like we're good on devnet 4 we can move on. Anything else 
* Okay, cool great. Yeah. So we can move on, then to Devnet five. Oh, sorry. 

**Barnabas**
* Yeah, there's one more thing. So, we have been working in the background a bit, to introduce the new tool that will be able to submit deposits and consolidation requests. Kind of like what launchpad does. But you can actually, do a bigger deposit now that supports more than 32 . And the consolidation request will also be part of this. So you will be able to test out, how you can consolidate two validators.
* So this is going to help the community  To run a test basically even without needing to run a validator 

**Stokes**
* Gotcha Cool. Yeah. It'll be really nice to see it all come together. 

**Barnabas**
* Yeah. This is still a work in progress. So we have something. Maybe by next week 

**Stokes**
* Okay, then onto Devnet five. So there are a number of open items here. And yeah, I think a few of these I think we can get through pretty quickly the first one is essentially just a last call on PR 3900. We had said, a few calls ago that we would target Devnet five for this. And, yeah, there's a little more discussion after that point, but it sounds like at this point that's all been settled. And yeah, I think everyone is generally in agreement to go ahead and merge this.
*  So yeah, last call And unless someone opposes I think we'll move ahead with this. we could even merge it after the call today I assume this plus one from Prism is for this PR so yep. In that case, cool and yeah, I guess just like one one caveat there is, to like, limit the scope of implementation changes. We were focusing on this change sort of just at the networking layer so that you didn't have to go through and change a bunch of other stuff in different layers of the client. So just be aware of that. cool.
*  Yeah, I've got some plus ones, so we're good on that next up, I did want to bring this, question up. This was refactoring kind of how we do timeouts and like managing peers again, in the past there was support for this. My understanding is that, we don't necessarily need, like, even a hard fork to coordinate this. I mean, I believe it's backwards compatible can someone speak to that point who's a little who's been closer to this PR like, especially if it's backwards compatible, then I think we're good to go ahead and merge it now 

**Pop**
* I think it's backward compatible 

**Stokes**
* Cool. Yeah, that's my understanding right. Okay. So then in that case, I think we go ahead and also just roll this into Devnet five and great we have those. So next up there are a number of well, maybe I'll start here. So my understanding is that there is some demand to refactor the requests coming from the execution layer. a bit further for Devnet five. And there are some PRS that are tracking that and the consensus specs, and we can go ahead and get them, I think in the next release or two pretty easily. But first I just wanted to kind of do a temperature check.
* And this is maybe even more a question for the ELs, because I think some of the changes touched the execution layer a bit more do we have anything to address there? Do we feel like that changes moving forward? Well I know Felix was driving a lot of this. I'm not sure he's here, though 

**James He**
* For the execution requests, I think the big thing is, just documenting all of the edge cases, the PR itself. And this descriptions don't fully document all of the different I think edge cases that we have to deal with, like, if we get, like a type and then we don't get the list or, checking for the max range of the requests, like how many you can include for the decoding or if it's empty, or if it's out of order, those things should be added somehow, especially because there's no spec tests for this 

**Stokes**
* Right. so the consensus specs PR that I saw for this did have these checks, and it was, I think, pretty, pretty well handled. But yeah, it does sound then like things are moving forward. And yeah, I guess no one has any questions or points to raise about that at the Then we'll assume that's moving forward. So next up then 7742. just to remind everyone, this is the EIP to uncouple how we handle the blob counts between the CL and EL and. Right. So this this EIP has been included.
* It'll lay the groundwork for us to more easily make changes to the blob counts in Pectra, which I think there's plenty of demand to do that the question that has come up in the last week or two, is that as written, 7742 is kind of missing a piece, at least potentially missing a piece around changing the base fee calculation. So right now it's essentially a function of the target blob count. And especially if we change the target. That could have implications for the blob base fee and how it responds to these changes once we started getting into this, there's like a number of other questions that came up.
* And I think now we kind of have this question to answer of how invasive do we want to change this? Like, do we sort of aim for sort of a more elegant thing right now, or maybe do something a little more practical that is simpler to move forward and think about this work at a later date. So I guess I can go ahead and grab this update to the EIP I'll put this here in the chat. So there are a couple options here. one of them is to basically just do nothing and not worry about how the target would impact the base fee here. although even moving to, say, four and six would have some implications. The I think next sort of simplest step would be to just go ahead and update 7742 so that the base fee scales with the target. This is what I'd call kind of the quick and dirty solution.
* I think it would work well for Pectra and is like pretty, you know, it's not like a super invasive change. Then from there, there were some questions around revisiting how we again compute the base fee. so it's kind of tolerance to any max or target change. And that has implications for again, sort of like the symmetry of how the base fee scales either coming up or coming down from wherever we're at at the moment. So yeah, I know, let's see. I don't know if Tony's on the call. I think he should be somewhere 
* I don't see him. But anyway, so he had a more, sort of elaborated take on this. And yeah, I guess the question for today is just trying to get a sense of like how much we want to do now. I would say the, the EIP, PR that I linked here and what is it, 8994. that one is like, I think a pretty good balance of like, you know, addressing some of these concerns for Pectra without being like too much of a big lift. So that 7742 becomes this, like, very complicated EIP.  Gajender 

**Gajinder**
* Yeah. Hello. is the audio okay? 

**Stokes**
* Yeah. That's great 

**Gajinder**
* All right. So yes. So, for, for the symmetry, I mean, it's a very small change to include. And if we actually want the symmetry of gas changes while going up or down, I think we should include it. So the main and it wouldn't really make sense for to any more complicated than it already is. but it will introduce the max, blob count to the header, because then it would be required to make sure that there is symmetry. And, yeah, I think that's it 

**Stokes**
* Right. And so I think what I linked doesn't have the max. Right? I think that's where we landed on that 

**Gajinder**
* Yeah. We basically right now removed the max and only we have target blob count right now. 

**Stokes**
* Right. And then yeah, to get to like a sort of more nice solution, we would also need the max being sent over. So that's a question for CL devs right now. And also EL devs, whoever's here. yeah. Do we feel strongly about adding this field to the header or passing it through the engine API and all the different places it needs to be 

**Stokes**
* Ansgar

**Ansgar**
* Yeah, and I just wanted to very briefly explain for people. Right. Because this might sound a little complicated, but the idea is very simple, right? If you only communicate the target to the EL, then in the calculation you can you basically just don't know how much more room there is between target and Max. And so you basically look at the target. And if the target is say four, you just say, okay, what's the max for four is basically the, the, the you can have zero blobs one plus two plus 3 or 4 blobs.
* So if you have zero blobs then basically you want to go down by 12% or whatever, the maximum kind of change rate per slot you want to have, and that's fine and all, but if you don't know the max, then you don't know if the if the maximum is eight then then you're good because then on the other side you also have like this maximum of 12% per slot that you can change. But if the maximum says only six, like we had discussed for six, for example, as a potential change, then all of a sudden you only have half of that of responsible responsiveness to the upside. So now you only have 6% of a max increase in base fee per slot.
* And that means that now anytime there's a demand spike, your reactiveness is half as fast.
* Basically, you need twice as many slots to react to a new base fee level that you want to get to than you would otherwise.
* So basically, communicating the max together with the with the target would allow us to have an update rule of some sort. Kind of depends. Can be simple. Can be small. Change today can be bigger change. And but it would basically be able to take that into account. But if you only communicate the target just conceptually, there's no way of knowing how much room you have between target and Max 

**Stokes**
* Right. Yeah. Thanks. And then Oscar, do you have a sense of oh, go ahead. 

**Gajinder**
* I would just want to add in this. Basically, I want to add that, you know, the upside is basically limited because actually the upside for max blobs that can be included is also limited. I mean, it basically reflects that. So if target and Max are basically not symmetric in the sense that this is just reflecting that. And in my eyes, I think this, this is just fine we should be okay with the little bit of asymmetry, but yeah. So I mean, if this is a really desirable quality to have, then definitely we should go for it 

**Gajinder**
* Right? 

**Stokes**
* I mean, I think, you know, the ideal state is that and so it is desirable. But I would kind of bias towards, again, sort of a good enough solution for Pectra. And we can always revisit a deeper change to the fee market and pusaka along 

**Stokes**
* With paradox. So I think we have some room to be flexible here 

**Stokes**
* Right. So okay, I would lean towards moving ahead with this 8994 update here. for 7742 for Pectra and delay a more complicated change to a later fork I suppose we can give people. Well, I don't know. I'd like to go ahead and merge this to keep this moving I think what would help is maybe having either, like, some sort of spec or EIP for the more complex thing, um, to have people sort of have something more concrete to, like, think about. But yeah, I guess. Yeah. Does anyone feel strongly about this or are we happy enough with sort of the, good enough solution for Pectra Yeah okay. Ansgar said he would like the Max and then otherwise.
* Yeah. Okay.
* So then I think we'll directionally move ahead, with 894 and. Yeah. Ansgar, maybe I'll follow up with you to see if, you think we can change something simpler, like in a simple way 
* So then what that means is. Yeah, I would hope to then have 7742, sort of the spec finalized in the next week or two and then. Yeah, as soon as we can get implementations, we can start testing this out. Yeah, I guess for Devnet five, maybe some early experiments, even before then. And yeah, can keep this all moving 
* There was one more thing for Electra. If there's nothing more to say about that for now, and I just wanted to get an update on the BLS Precompiles. This is more of an EL concern, but we had kind of been discussing there was a question around, effectively the API for the Precompiles, which I think we've kind of resolved. And then now the question was, downstream of that, then doing the gas benchmarking to make everything work well, does anyone here have any updates on that and they may not, but I figured I would ask I don't see anyone on the call who has been closer to this, so okay, that's fine.
* Then we can follow up async so yeah, I think that's all we had today for, Electra. Anything else anyone wants to bring up 

**Mikhail**
* If I may, just a quick, um, thing 

**Stokes**
* Yeah, please. 

**Mikhail**
* I have, Yeah. Thank you. So I have recently submitted a PR, um, which is the PR number 4000, which is sending yeah. It's just basically this PR is about adding a couple of there is a couple of, checks that we do while processing the voluntary exit. And they, for some reason, was not included into consolidation. Processing and consolidation is basically consists of two steps. The first one is to make the other exit. And it makes sense, to preserve the same condition checks 
* For consolidation as we do for exit. And we would kind of aligned with that. But for some reason those two have been missed. And this PR just adds them. And yeah, that's the quick announcement. Please take a look. Because basically we want this to be part of Electra 

**Stokes**
* Yeah that makes a lot of sense. So yeah please take a look. I will do the same. And yeah, just from a quick scan. This makes a lot of sense. And this is also something we should do in the next month or two, is just to pass on all these things. Pectra has a lot of features. They all kind of interact in very intricate ways So, yeah, making a second pass on all of this, is super valuable Okay. Yeah. Thanks, Mikhail. So then we can move on to PeerDAS. and any blob questions I guess to kick this off, I will ask if there's any updates on the dev nets. I heard there was something like 100,000 slot reorg on net three, which is impressive 

**Barnabas**
* So we had a massive reorg like,  end of last week I think, or beginning of this week. I'm not exactly sure when it happened and we decided to shut down the industry, because it was pretty much unfeasible to recover. At that point. We had only, Prism validating at, at this point, and only, I think one super node So we decided to postpone a relaunch for after, Defcon because everybody wants to focus on rebasing on top of Pectra, and that will take some time And we we would like to discuss whether we can include, pure devs as fully named, future Fork or can we stay or should we stay at a using the EIP 45? Whatever the number is, I think it's 94. 

**Stokes**
* Yeah, yeah. do you have a sense of just on the on the reorg? Do you have a sense of like what caused it? Like did some node eventually release like some data column that triggered this huge fork choice 

**Barnabas**
* Maybe someone from prism can comment on it I think the problem is that the people that are working on this on the prism side, are on holiday right now, so. Okay, I'm not sure if we would have anyone. Yeah. All good. I'm just I'm just curious. That might be the deepest 

**Stokes**
* Okay, cool. Well yeah. So that tees us up to I think the agenda item here, which is moving ahead with this rebase. So I don't have the PR handy, but there is one to essentially. Yeah. Put the PeerDAS EIP 

**Stokes**
* Into Hulu. And yeah, there was a bit of a holding pattern with when implementers were ready to do this. And the timing there I think at this point we should just go ahead and make the merge and, go from there. Anyone feel that we should hold off for some reason 

**Stokes**
* Right. Yeah, I think it's 3.94 here. I looked at the breakout call notes from this week and it said that we had discussed on this call. So my read was that, basically people were ready to do this 

**Barnabas**
* It would be nice to get some input. We got no input on the call. So it would be nice if people have some opinion 

**Stokes**
* Yeah. I mean, the thing is we're going to have to do this eventually. So I think if we can't get an opinion, then we just bias towards where we're ultimately trying to land, which is, going ahead and putting this on top of Electra 

**Barnabas**
* I mean, the question isn't whether we want to have it on top of Electra. The question is whether we want to trigger it as full 

**Stokes**
* What how would like what would. Sure. But what's the alternative? 

**Barnabas**
* The alternative is we keep it as EIP 7594 and we trigger it under that name. And we only include it in full if we are 100% sure that PeerDas is going to make it into full 

**Stokes**
* I mean, that's generally what we've agreed via ACDE. And yeah, I don't see how that would be any different moving forward 

**Barnabas**
* And also if we activate at full, then on the other side that's going to activate Osaka, which will also activate EOF. So it would be good to be able to activate these two features separately in a way so that we don't have EOF 

**Barnabas**
* Problems in peer networks or peer desk problems in EOF networks 

**Stokes**
* Right? I mean, so content on the EL, couldn't we just set basically unset the EOF features so that they aren't responsive to Osaka, even if like there is Osaka fork logic 

**Barnabas**
* Maybe others can comment on that 

**Stokes**
* Ideally, I don't know. I don't know if they're here 

**Stokes**
* Okay. Yeah. I mean to move us forward. Like, again, I would lean towards, moving ahead with all of this, having PeerDas before you have it activate  And yeah, this is a good point about EOF and or any like Osaka EIP on the El side So we can definitely discuss this on the next ACD.but yeah, perhaps in the meantime I'll try to get some async information even in the next week and try to move things forward. But I guess what I'm hearing, at least from lack of input, is that there's no opposition to moving ahead on the CL. in this direction Okay then we'll move on to the next agenda item. let's see.
* So I think we had yeah. Lucas, I don't know if he's here, but he has an EIP for changing withdrawal credentials. I don't know if Lucas is on the call but it's here. So, yeah, I think the idea is essentially to have another type of, like, execution change message that would let you change your withdrawal credentials. We've discussed this stuff in the past, and I think generally the sort of consensus has been like, handle this within the execution layer. So, you know, have some withdrawal address that could then point to, you know, a multisig or whatever smart contract where you then have the flexibility to like, manage that policy.
* There but yeah, I guess let me grab the link to this. And I guess the ask for the moment is just to take a look he did say in his comment that basically,  he's just looking for feedback and it's very likely to be, something in the future. But if you're interested about this, you could go ahead and put it on your radar 

**Stokes**
* Put it says it'd be nice to have them on the same side Okay 

**Mikhail**
* Just a quick comment on that. So I it this proposal is actually yet another request that we used to introduce Used to have now part of Electra will have the protocol. So it should be pretty straightforward thing I guess. 

**Potuz**
* Yeah it is a really trivial change on the CL side as well. And I suspect on the EL it should be simple 

**Mikhail**
* Yep. Because the complexity will be handled by the yet another system smart contract as long as our request design is kind of good for and yeah, good for extending it. Like for from the EL perspective and yeah 

**Stokes**
* Yeah I gotcha. Yeah that makes sense Cool. Well that was pretty much it on the agenda. Is there anything else, that anyone would like to bring up 

**Stokes**
* Yeah. Yannis 

**Yiannis**
* Hello? It's Yannis from problem. One issue that relates to the blob scaling. part. as you might know, a problem with crawling the, consensus layer network and then using that information where
* We have put together a tool that is probing basically all the different nodes to see what bandwidth availability they have. So that might be we're going to have results soon, but that could be helpful to see, you know, what is the ideal blob increase that should be targeted for the next upgrade or perhaps the one after that if we're too late to have that. Again, I don't we don't have results right now, so I cannot share anything. But, hopefully next week and before the before devcon, we are going to have something so could be some, topic to be discussed there 

**Stokes**
* Great. so you're crawling disk v5 at this link here is to disk V5. And then I'd just be curious, like are you looking at latencies or trying to infer bandwidth or something else 

**Yiannis**
* Sorry. The yeah. The infrastructure bandwidth. Yeah 

**Stokes**
* Okay. Gotcha Cool. Well, yeah. I'll be looking forward to, the results there 

**Yiannis**
* Yeah. I guess there is not going to be a call in two weeks, but, at some point in the devcon week, we could discuss about that Relevant meetings 

**Stokes**
* Sounds good 

**Yiannis**
* Thank you 

**Stokes**
* Anything else 

**Toni**
* Yeah. Very quickly. I missed my turn at translate, but I think you mentioned it already. I just want to put it here in the chat and so that it's, that everyone knows about it. It's basically, I quickly drafted it as an EIP, but I think we we could add it to 7742, but we decided we wanted to keep it as simple as possible. This is fine. It's just a change that would allow us to move away from the from having the target of the blobs always be half of the max.
* So kind of if we want to do, 46 instead of 36, then what we might end up with is some asymmetry when it comes to blob based scaling, because currently the base fee can scale and 12.5% in both directions.
* And I just wanted to yeah, paste that EIP or this draft into the chat so that everyone can see it 

**Stokes**
* Thank you. yeah. We covered this a bit earlier and we kind of decided to move ahead with the simpler thing for Pectra, but I think sort of more, you know complex revisiting of this. And Pusaka is definitely in bounce 

**Toni**
* Yeah. This is this is fine.  I'm fine with that 

**Stokes**
* Okay. Well, if there's nothing else we can wrap a bit early. I guess two things to note then. One of them is that. Yes, the call What is it on the 14th. So essentially the next ACDC, we're going to cancel. Everyone will will most of us will be in Devcon, so we'll have plenty of conversations there and otherwise. Yeah. If you're listening, we do have the launch of this, testnet Mekon that is sort of a preview of Petra that's open to the public. And. Yeah, be on the lookout for that. And, yeah, I think that's it. So we can go ahead and wrap up a bit early today. write blog posts for blog post. 

**Barnabas**
* Yep 

**Stokes**
* Yeah. The blog post for Mekong will be coming next week. So 

**Stokes**
* Keep an eye out for that. Otherwise yeah, we'll go ahead and close and yeah, I'll see a lot of you at Devcon. Very excited 
Thanks. Bye everyone. Thank you




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


