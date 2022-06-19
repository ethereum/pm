# Ethereum Core Devs Meeting #140
### Meeting Date/Time: June 10, 2022, 14:00 UTC
### Meeting Duration: 1 hour 45 mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/538)
### [Video of the meeting](https://youtu.be/dByC5Bw8DvU?t=467)
### Moderator: Tim Bieko
### Notes: Viktor Shepelin (@modernman.eth)

### Summary
## Decisions Made
|Action/ Decision Item | Description | Video Reference |
| ------------- | ----------- |----------- |
| **140.1**   | 
| **140.2**   | 

# Contents <!-- omit in toc -->

- [1. Merge Updates](#1-merge-updates)
- [a. Intro and Ropsten](#a-intro-and-ropsten)
- [b. Concurrency Issue](#b-concurrency-issue)
- [c. Web Sockets Issue](#c-web-sockets-issue)
- [d. Block Gossip](#d-block-gossip)
- [e. Zero Transaction Blocks](#e-zero-transaction-blocks)
- [f. Infrastructure Provider Testing](#f-infrastructure-provider-testing)
- [g. Insufficient time between prepare and get block requests from CLs](#g-insufficient-time-between-prepare-and-get-block-requests-from-cls)
- [h. Adding gas limit to payload attributes](#h-adding-gas-limit-to-payload-attributes)
- [i. Launching Sepolia Beacon Chain](#i-launching-sepolia-beacon-chain)
- [j. Client teams readiness and plans for future testnet merges](#j-client-teams-readiness-and-plan-for-future-testnet-merges)
- [k. Sequencing of future testnet merges](#k-sequencing-of-future-testnet-merges)
- [l. Delaying difficulty bomb](#l-delaying-difficulty-bomb)

- [2. EIP Discussions](#2-eip-discussions) - deferred to future meetings

---
# 1. Merge Updates

# a. Intro and Ropsten
Video | [7:50](https://youtu.be/dByC5Bw8DvU?t=471)
-|-

**Tim Beiko**: Good morning, afternoon everyone. This is All Core Devs 140. We have a bunch of things on the agenda today. First going through, obviously, the merge that happened on Ropsten, talking through kind of any issues there and next steps. And there were also a couple different little merger related items. So there was one issue we discussed on the Discord this week about the responsiveness of EL clients when getting payload requests from CL teams. Then there was something in the engine API to allow builders to set the gas limit or to allow sorry validators to keep control over gas limit. And then talk about the next two testnets, Sepolia and Göerli. How do we go through those. And continuing the conversation on the difficulty bomb – there’s been EIP that's been proposed for that. And then, there were two more EIPs on which we had updates – 4444 and 5027. So hopefully we get through all that. But I guess to start does anyone want to walk through what happened on Ropsten?

**danny**: I synced with Pari before. He is not I believe he's not in this call, so I can share his notes. With Ropsten, pre merge, some of the consensus layer teams were having deposit tracking issues. Essentially validators couldn’t come to consensus on the state of the proof of work execution layer to import new deposits. This was due to some engineering assumptions about block times which were not holding in Ropsten and it has been patched by all teams. It's not something expected to be seen on Mainnet. Then we move toward TDD. Post TDD we had about a 14% participation drop. 9% of this was from the Nimbus team nodes which were configured improperly with the jwtsecret. About 1.8% was from another mind concurrency bug required reboot. And then about 2.5 to 3% was from Nimbus-Besu nodes that were attempting to use web sockets which surfaced a bug in the web sockets implementation. They changed their configuration to use http so all that came back online. And we see 99.5% participation right now. The mind concurrency bug is still being looked at a bit more. If it occurs during the transition, a restart fixes it. The zero transaction blocks caused by timeouts have largely been fixed by Aragon. They can expand a bit more. About two to 3% of blocks are being proposed with zero transactions. But we're still going. Pari has not yet isolated the combination and is going to be looking into it. Looks like Nimbus-Besu who might be one of the affected combos. And Marius’ transaction buzzer has been started on the network to a very healthy transaction load - more full blocks and fewer zero transaction ones. Let's see. Zero transactions have largely been handled. Obviously, we should dig in a bit more here if we can. So the shift is now into sync tests and dapp testing. ETH stakers been running some sync tests. And Sam from E F is also going to launch a number of sync tests on Ropsten as well and we'll have data on these next week. So like turning EL off, turning CL and more exotic scenarios. That is the TL;DR from Pari.

# b. Concurrency Issue
Video | [12:00](https://youtu.be/dByC5Bw8DvU?t=721)
-|-

**Tim Beiko**: Thank you um. Yeah there's a couple of things I guess to begin there, and so the Nimbus was just a config on the jwt. Do you want to walk through kind of the issue, sorry the issue that you're having and what the status is there.

**Marek Moraczyński**: So we had one but that occurred on transition and it affected only a few nodes. And it is connected with concurrency - how we are processing block. We found this bug our card. But it hasn't been fixed yet, but we should resolve it soon. That is all I think.

**Łukasz Rozmej**: If I can give more details. We have a problem when we got a block from the network and from the CL client at the same time during the transition. And so we wanted to process them both at the same time. When we cannot do that with our block processor, we should schedule them one by one and that's really it.

**Tim Beiko**: And when you say processing it's like you receive a new block from the network and you get like a block from the CL at the same time, so it's like an external and internal ping to the execution layer?

**Łukasz Rozmej**: Yes, yes, yes, yes. That was the problem and the problem was on the on the Ropsten because there was a lot of blocks of the same height going on the same time and that’s why because. Some percent of the, some small percentage of the nodes got that, at the same time and that's why they failed. And to fix it will just add the correct scheduling of this and that's pretty much that. It's a fixed that we will do next week.

**Tim Beiko**: And when you say there were many blocks that's, I guess, because on Ropsten when we were we were mining, we were creating a bunch of oncalls just because I was a bit of a sketchy situation to get all the hash rate at the same time. Is that right? Like just because yeah when you say all these blocks. 
Łukasz Rozmej: Yeah I asked about it and there was mining, Geth was mining on two cores cars and it I think it was overwhelmed and it didn't process the block and it made the second one, or third one, sometimes with the same block number before it managed to process the previous one, so that's why that was, I think the case, but I got from someone as an explanation and yeah that's actually great that happened because it showed our bug.

# c. Web Sockets Issue
Video | [14:55](https://youtu.be/dByC5Bw8DvU?t=900)
-|-

**Tim Beiko**: Yeah, good yeah. Very cool thanks for sharing. And then the Nimbus web sockets. Does anyone want to just give a quick update there? Something from the Besu or Nimbus side.

Fabio Di Fabio: Yeah sure. Okay, so what we saw is that, using web socket, Nimbus was not able to fetch the data that it needs. After checking with the Nimbus team, they sent us option to make things work, but then we had another problem and we had to disable also jwt authentication. So now the setup that is working, at least for us, for our 2% of Besu validators that are configured with Nimbus is to have web socket with a special flag and jwt authentication disabled.

Gary Schulte: Specifically, we have eth subscribe and eth unsubscribe are not getting added to the execution engine endpoint. It's just I think it's an oversight on our part, when we combined the json rpc and web socket onto the same port, we're not adding those two end points to that the engine endpoint. So I think it's going to be a quick fix but like Fabio mentioned, we have to have a workaround for the moment for that combination.

Tim Beiko: Got it. Is the is the issue with the jwt kind of independent of that or is it like.

Gary Schulte: yeah we only see that problem when we're using the force polling features, I think I suspect any way that the force polling work around and Nimbus is not sending a token we haven't we haven't investigated that whether it's actually in the header or whether it's just expired, or something to that effect, but for that particular workaround to work, we had to disable child authentication.

# d. Block Gossip
Video | [17:20](https://youtu.be/dByC5Bw8DvU?t=1040)
-|-

**Tim Beiko**: Got it. And there's a question in the chat about EIP-3675 trigger merge and like disabling the block gossip and we discussed this on like one of the testing calls I think last week. It seems that, if we did this basically we couldn't do shadow forks and I believe that there weren't any clients that disabled block gossip after the merger. I don't know if anyone who is on the testing call wants to give more complex on this. Mikhail I saw you come off mute.

**Mikhail Kalinin**: I was just going to say that disabling gossip should not like affect shadow forks from what I understand. If there is another requirement in this EIP to disconnect peers that send you block gossip after transition gets finalized, and this, what can break.

# e. Zero Transaction Blocks
Video | [18:35](https://youtu.be/dByC5Bw8DvU?t=1115)
-|-

**Tim Beiko**: Right does that answer your question proto? Okay, it was about terminal blocks. Okay yeah, cool. Okay, so yeah that was a Besu, Nethermind. Erigon, do you want to chat about the zero transaction blocks a bit.

**Andrew Ashikhmin**: Yeah sure. So our mining has been experimental because we don't support the gpu mining so, but after the merge we're going to support proof of stake mining. Still, the code is kind of it's not as mature as we would like it to be. So we made some quick fixes, but we still need time to make the  mining or proof of stake block building code more robust yes. 

**Tim Beiko**: Yeah that makes sense. Okay um. And then yeah one last thing I guess on Ropsten, so now that we have Marius’ transaction buzzer running it means basically every block should have transactions in it, correct? Because it was mentioned is like 2-3% of blocks without transactions, I suspect that's something we would see on Ropsten like under normal operations. But given that the transaction buzzer is running we probably don't want to see that. And the empty blocks we're seeing are results of an issue. Is that is that right?

**danny**: I mean it depends on the how dynamic the gas is set on that transaction buzzer, because you could imagine the base fee going up above what it is willing to pay and then having some zero blocks, but I would at this point be monitoring if there a particular client pairs that are consistently are having zero transaction blocks. And Marius can comment on the dynamic nature basically and his transaction buzzer.

**Tim Beiko**: Marius is not with us.

# f. Infrastructure Provider Testing
Video | [21:20](https://youtu.be/dByC5Bw8DvU?t=1280)
-|-

**danny**: About just you know I think we pulled more infrastructure providers through this transition than we had in previous testnets. Is there any update on how that went?

**Tim Beiko**: So. I didn't hear from anyone that things were breaking I actually well I didn't confirm and I didn't get confirmation that anything broke so. At first it was some people thought that some smart contracts had issues but it turned out there was just a user spamming weird transactions to it and that's like coincided with the Ropsten merge. And the other thing is, it seemed for a while, like the rate of failed transactions was higher but I don't think that's that's quite the case. I’m talking with the etherscan people to get some better data on that. The challenge with getting data around the Ropsten merge is because there were so many oncalls and empty blocks around the merge, and the mining was like so weird that even etherscan had a harder time like getting a nice data dump than they usually to do. But it doesn't seem, at least like very high level, that like there's an increase in like the error rate the smart contract transactions on the network, which is, which is good. But yeah I’ll look into that some more um. But yeah aside from like this, this stuff no one, no one has at least complained loud enough that that their product is broken so that's that's pretty good. Good. um. Anything else anyone wanted to mention about the Ropsten transition?

# g. Insufficient time between prepare and get block requests from CLs
Video | [21:20](https://youtu.be/dByC5Bw8DvU?t=1400)
-|-

**Tim Beiko**: Okay um so there's two other merge related issues that we wanted to discuss. I think it makes sense to go over those before we start talking about testnets like more of like coordination. Because it will obviously influence when and how we're ready. But the first was this idea of like the EL responsiveness to CL sending you getPayload requests. I know earlier this week, I believe we talked about that a Discord where some CLs were sending like too many requests to ELs and Els are kind of working around that. But there are still CLs sending requests for blocks too quickly for ELs to property respond and I know there were some fixes on the EL side to better accommodate that, but there was still sort of an issue on the CL itself itself. I don't know if anyone has an update about that?

**Micah Zoltu**: So, just to clarify a little bit, I think the EL should, I think, in general, this is like a broad, broadly speaking. If there's bugs in the consensus layer clients, the execution layer clients should not be writing code that covers up those bugs we should get them fixed in the consensus client and so in this case the bug is that. when the consensus layer client sends a request for getPayload, I think it's called getPayload. So if the execution layer receives it a getPayload request it needs to send a block as soon as it can. It should not wait, or should not delay if it has no blockers, just send empty blocks. It should not stop and go fetch things like it should have a block by now. If the CL is sending you that, and you don't have enough time to actually prepare a block, then that is CL bug and you should not cover it up by then, you know saying, oh I'm gonna take my time and actually do the thing that CL wants and you really need to be sending block right away. On the CL side, if the CLs are sending you a prepare, followed by a get let's like 10 milliseconds apart, that is a bug in the CL or it does happen in the real world, sometimes but it's very rare and it shouldn't happen often. And again, you should send immediately whatever block you've got. If you don't have a block, send an empty block. Like send something as fast as possible, there should be no delay in this response.

**danny**: Right. I generally agree with this and just for some additional context - in 99.99% of scenarios, with lead times of seconds, you can send a prepare and almost certainly when it's actually time to get that prepare will be correct. You could potentially have some sort of reorg that might cause you to do a different prepare or which the other one should be aborted and maybe there'd be insufficient time at that point to do the get with a non zero transactions, but I think we should be generally not masking that bug and providing you know, having CL provide the adequate time in 99.99% of these scenarios.

**Tim Beiko**: Lucas and Adrian both have their hand up I don't know who was first.

**Łukasz Rozmej**: Okay, let me go first. So we implemented this workaround this was partly because we wanted to track our block production better and partly because this bug is very long standing, I think we were trying to make a look at it for a few months now, so we wanted to have some code differently. We will revert that but it also gives us some good information on Ropsten. We made it I think more or less same as Geth, so we are waiting potentially up to 500 milliseconds right now. But I agree that it's something contrary to the spec and we will drop it.

**Tim Beiko**: Thanks. Adrian?

**Adrian Sutton**: So I think there's a couple of things here is it's worth being clear that this shouldn't be all well this definitely isn't all CL clients. Yeah I think it's only nimbus now. So we should be pretty clear that most of the time, this should be working and if we're seeing it seeing those really short time periods with other CLs, then we've got more of a design problem we're seeing late blocks coming up. I'm also not as sure it's entirely clear cut that we shouldn't add a delay, maybe we should add it on the CL side, because it tries to wait 500 mil if it knows it's been a long time, and those kind of things. But right now, if we get a late block, we will, you know, a block right at the end of one slot will give you no time at all when actually we've got you know a total of four seconds to play with. We could actually spare 500 milliseconds to create a block with transactions. But there's no way to communicate that kind of trade off to EL currently we're just trying to get a block right at the start of the slot every time.

**Micah Zoltu**: The CL should make that decision and just send.

**Tim Beiko**: Yeah finish up Micah, and then Andrew.

**danny**: You can send the get later.

**Andrew Ashikhmin**: um so yeah about Erigon’s implementation. Right now it's really simplistic and doesn't have any hacks. So when we receive requests for to build a new payload we start building it on the side and we when we receive our getPayload, if that building process is finished then return the built block. Otherwise we return a pre-populated empty block. But that's probably too simplistic and what I’m currently thinking about doing is that when we receive getPayload, and we still haven't finished building the block, what I want to do is to stop adding more transactions into the block. But then we will need some time to actually finish sealing the block, calculating this stage root and like finalizing the block. So, to my mind, there won't be any artificial waiting period, but it won't be like super instantaneous it won't be a microsecond. It will be I don't know, maybe, 10s of milliseconds in some cases, to finalize the block. That's my current thinking.

**Micah Zoltu**: My gut. Personally, is that if you've got a block and you're kind of iterating through the transactions and you get getPayload and you need to cut off iterating transactions and you just start your sealing process, and then you send. To me that feels like it fits the bill of as soon as possible. I don't know how other feel but I don't personally have a problem with the strategies described.

**Tim Beiko**: Yeah I would agree anyone else anyone have an objection to that to that?

**Adrian Sutton**: On the CL side we've got to build a block anyway, so there is always going to be a bit of time and we were probably calling, hopefully calling getPayload right at the start of our block build process so tapping into in parallel degree. It's not hundreds of milliseconds to create a block but it's not free, either on our side, so it kind of balances out pretty well. 

**Micah Zoltu**: Yeah, I think the main thing here is you shouldn't be like going and requesting a block from a remote server or a builder or you shouldn't be like starting to collect your transactions and execute them when you get the getPayload. If you haven't executed transactions by now it's too late. Whereas if you need to do like little bit of cleanup or finalization or whatever it is, you know internal stuff I think that that's okay. To adrian's point - you bring up a good point Adrian I think that the EL knows about how long is the it needs to build a block and that information may differ between execution layer clients right, so Nethermind may build a block faster or slower than Geth, which may go faster or slower than Erigon. And so, how much time you need to give them in those situations where you've got a prepare and it's going to be followed very closely by it gets, I appreciate the point you're making where it's not obvious like you want to get as soon as possible, and you don't know how long the EL needs between a getting and prepare to reasonably prepare a block. Does anyone have any ideas on, you know how we can resolve that like?

**Adrian Sutton**: So, to my mind, I think the current process is fine and the vast majority of the time it should work out where the EL has many seconds to work. So I don't think we need to do anything quickly. And you can kind of see how it plays out when we go through the merge on mainnet. It'd be fine under current design. But if we were to optimize it my suggestion would be that the CL can simply provide a kind of maximum time frame to the EL when it sends it getPayload request, so it can say yeah I’m running behind I need it just now I’ll give you zero or you can have a second. It may be as simple as saying you can take a small amount of time or not, and maybe that’s specified milliseconds or we do specify milliseconds and CLs to kind of try and be smart. But I think it is something like that, if the CL can just signal to the EL - I’m right at the start of the slot I’m on track, I have some milliseconds to spare or I don't and I’m already on the cusp of my block being late.

**Micah Zoltu**: yeah I wish we had versioning in the engine API so it didn't hurt me so much until after the merge.

**Adrian Sutton**: We do.

**Tim Beiko**: Yeah and we'll need to make changes to the engine API after the merge, so this is not the only time we will have to think through this. Just because we're already like a third of the call through it seems like we're roughly in agreement here like Nimbus seems to be the main CL which has an issue where we need to address this. And Dan just posted in the chat that they are working on it and prioritizing it. But beyond that, basically, assuming Nimbus fixes this that we can probably just leave things as is.

**Micah Zoltu**: The reason I want to bring this up on AllCoreDevs instead of the CL call is because we do need Geth to fix their cover up. So Geth currently delays 500 milliseconds. So they can go the long block and they need to stop doing that. Like Nethermind copied that behavior and that's bad behavior that we need to get fixed.

**Tim Beiko**: Right. Anyone from the Geth team want to chime in? We can see that there's like five of you on camera so. There's like 10 of them, and none of us like you know what I bet I bet the one person on the MIC is the one person that has like a broken leg.

**danny**: It might have like a 10 second delay because they're on the moon.

**Tim Beiko**: Okay. So we'll follow up on this offline. Okay yeah so moving on from this, just to summarize -  It seems like most CLs already have it fixed, Nimbus needs to fix it and Nethermind and Geth have workarounds that they need to basically revert. Nethermind will do that and we need to talk with Geth offline.

# h. Adding gas limit to payload attributes
Video | [36:20](https://youtu.be/dByC5Bw8DvU?t=2180)
-|-

**Tim Beiko**: The next thing we had was by Alex Stokes. I don't know if he's on the call. And Mikhail you had some input after this. oh yes Alex is here. Alex do you want to give us some background on the builder spec?

**stokes**: Yeah, so essentially, so yeah Tim dropped this issue in the chat and basically it suggests that we add the gas limit as a parameter to the payload attributes. So right now, it is not. And the reason we want it to be is because it gives proposers more [autonomy] over setting the gas limit during the build process. And I think this pilots like adding a V2 message. But if we do this, and the EL clients support it, then it means that you can use off the shelf software for external builders much more easily. Danny.

**danny**: Okay, I think your last point was the at least the the rebuttal to what I’m about to say, which I think Micah said in the chat and that validators presumably control their execution layer and so can set their config there. 

**stokes**: Well, right, so they do for the local clients, but this is if you're using the builder network. Then you might not be able to know, like a builder wouldn’t necessarily know for this proposer

**danny**: Builder would have to like dynamically adjust some config or see.
stokes: Right.

**Micah Zoltu**: What is this scenario where the… I thought, even with the builder network, you still had an execution client that was under your control and you received a block from builder network, which you then validated and executed with your execution plan is that not correct?

**stokes**: Right but, so this is just a way to signal… So let's say I’m using like stopped Geth to help build there's no way to tell Geth right now, like hey for this next slot you should use this limit versus that one.

**danny**: This is for the builder who's servicing many validators who might have different configuration values.

**Micah Zoltu**: We want to make it so users only have to configure one of their two clients like so they don't have to configure Geth at all, they can just double click it, so to speak or am I missing something?

**danny**: No, this is not a UX thing. This is to help facilitate a builder who's a separate entity in the network, who services probably many different validators who have potentially many different gas limits. And so, if they would be able to reuse this engine API to service others more easily if they could dynamically specify that gas limit. Otherwise they're going to have to modify the Geth software. Again this is for builders.

**Micah Zoltu**: Perhaps I’m missing something. I apologize if I am. I thought the design was a given validator would have a execution client and a consensus client that's under their control. The consensus client would send some stuff to the execution client saying, hey prepare a block for me, the execution client would then send that details about that off to the builder network to say, hey I need a block from somebody, and then those people will then send it back. I didn't think the builders were talking directly to some validator’s consensus client.

**danny**: The builders talk to relays who talk to consensus clients. Consensus clients can either get a block locally or from this network. When getting it from the network, there are a couple of parameters that might be specific to a certain validator, gas limit that they want being one. And so, for the job of these external builders, to be able to reuse EL software and this API to service many validators, they want to be able to set some of these parameters, gas limit being that one parameter right now.

**Micah Zoltu**: Gotcha Okay, so I think the piece that I was missing, just to make sure that it was, is that the builder network talks to the consensus layer and does not talk to the execution layer. And then, when the consensus layer gets a block from the builder network it then asks its own execution layer client, hey can you verify this is good for me. But this whole process happens between consensus client and builder network, execution clients are not involved in that communication protocol at all, correct? 

**danny**: Yes. The validator can get a block locally or maybe externally and then it always asked locally to import and make sure things are good. 

**Micah Zoltu**: In that case, I'm on board.

**Tim Beiko**: Well I guess the trade off is we are changing the semantics of the engine API really late. Is that correct?

**stokes**: Well, I think I think this is why we make it V2 rather than a V1. If everyone is on board, we can change the V1, but I think it's a bit too late for that yeah.

**Tim Beiko**: But I guess the question I would have is, is there like a security thing here where like builders have control over the gas limit.

**stokes**: What we want to make it so that they don't.

**Tim Beiko**: Right. But currently using the payload V1, so say the gas at this 30 million, if we're using the current API and the builder sends me a block that like raises it as much as possible, but the validator…

**stokes**: Builder software could still respect the validator’s preferences, it's just having this makes it easier to reuse a bunch of software, so it lowers the barrier to entry.

**danny**: So for now, builders will have to modify the software. If we add to V2, the builders could go back to using much more less modified solver.

**Bordel**: Is this the only thing that's stopping us from having software that works for external builder ELs, or are there other rough edges in the API?

**stokes**: I think you're asking if there's other rough edges to the engineer API for this use case. I haven't found any. Another parameter that might be worth thinking about is the extra data and the EL block. It would kind of be the same deal with the gas limit, but I think that one's less critical. 

**Bordel**: These are strictly improvements for the relationship between the EL and an external builder, this is not needed for the relationship between the local El and local CL.

**stokes**: Great well. I mean, assuming that you can set your local El to have the gas limit all of your validators want. But that's probably fine.

**Tim Beiko**: Ansgar, you have your hand up.

**Ansgar Dietrichs**: Yeah, I just wanted to briefly asked if we all agree in the first place, that it is desirable for validators using an external network to basically have the gas limit set by the validator. Because I mean the gas limit is this somewhat weird parameter, where I think we kind of agree that it is theoretically under consensus control. We just for now put it under miner / validator control to be able to react quicker not just with hard folks. So just if really the only reason is to react quick in case something goes wrong, it might actually be desirable to have fewer parties to adjust the parameter. And, in case anyone misbehaves and you know increases the gas limits too much, this is already, in a sense, a network attacks that we would have to manually intervene for. So I’m just wondering like probably, the answer is, we want validators to control this but I’m not sure that this is like an obvious thing.

**stokes**: I think, the danger of having just a few builders have control over it is greater than you know any risk we would incur by needing to suddenly change it, and not being able to.

**danny**: I agree. We also did talk about this a few weeks ago and generally agree that, although validators’ / miners’ interests aren't always necessarily totally aligned with users’ interests, the short term, the shorter term profit interests of builders are likely less aligned than validators and miners would be, and thus we decided that it makes sense for validators akin to miners to retain control for this. There are probably notes and stuff in the previous call we talked with them. It's also more attributable in the sense that we can react in all sorts of social ways if there's an attacker.

**Ansgar Dietrichs**: That makes sense, thanks.

**Tim Beiko**: Okay, just to summarize. I don't think anyone is advocating to have this part like to have this override the current view on endpoints and if that's the case this is your chance. Okay. If not, does anyone disagree with making that like a V2 or, I guess, maybe another way to frame this is like Alex for this to be useful, I suspect this V2 endpoint would need to go live before the mainnet merge.

**stokes**: So here's the thing I mean like this, like builders will still exist and they will do the job as the spec dictates. It's just this would make it a lot easier for like other builders to come online so. You know, we definitely shouldn't block the merge for this it's not like critical or urgent in that sense, but you know, the sooner the better.

**Tim Beiko**: And is this something all clients need to add support for, at the same time, I guess, obviously, like if you added first more builders might use you, but like is there a…. I don't think there's a hard requirement that it gets activated at the same time, is that correct.

**stokes**: I mean like theoretically no, but I think there's network effects if everyone does it, we can kind of just be like okay, this is what we use now.

**Tim Beiko**: Mikhail, you have your hand up.

**Mikhail Kalinin**: Yeah I just would like to add that if we have a V2 with this field, I would like, I think that we should make it optional for those cases where home stakers or other stakers that just don't want to mess with the configuration and probably don't understand the gas limit implications. Like the implications of changing gas limits on the network. They all just not do this and use like default values that we have currently in EL clients, in the binary distributions of EL clients. That's just like to add on this topic. So, if the value of this field is not provided or zero whatever the default will be, then EL should just set its own.

**Tim Beiko**: It seems like there's like some agreement to do this but some details to figure out. Is it fine to just continue this conversation over the next couple weeks?

**stokes**: Yeah can start some PRs.

**Tim Beiko**: Awesome. But yeah not changing the V1 and we'll see what comes through. 

# i. Launching Sepolia Beacon Chain
Video | [49:00](https://youtu.be/dByC5Bw8DvU?t=2940)
-|-

**Tim Beiko**: I think actually there's one more like pretty independent topic, and then it all gets pretty intertwined. The next thing I just wanted to chat about is the Sepolia Beacon Chain. I know we've mentioned like we wanted to launch it as soon as possible, I think there's been some progress around like selecting the validator sets and unfortunately I know Pari is not here, but does anyone have an update on the launch of the Sepolia Beacon Chain?

**danny**: Yeah. The current config is slated for the launch to happen on the June 20th and for it to go through a couple of Altair and then Bellatrix over the next 24 hours. I believe that Pari is also generally locked down who's going to be participating in this. It will be a gated contract. And we’ll be using a kind of an ERC-20 version of the deposit contract. So we can add validators but people can't just get Sepolia and create their own validators. Additionally, they're looking into when you create the beacon chain out of thin air for this type of testnet that you can actually inflate supply so there's a bit of talk about inflating the supply on a few validators. So that there's a lot of supply just in the background in case there ends up Sepolia ETH hoarding. So that's the last kind of thing that they're sorting through over the next few days before the configs are probably finalized around Monday. Please take a look, there is a link with the configs in terms of distribution of validator set and the timing. If you want to take a look and give your thumbs up on that.

**Tim Beiko**: And just one thing, so you mentioned it's going to run through Bellatrix basically soon after launch, so I assume this means that even though it's like a restricted validator set we're just going to do TTD override on Sepolia when we're ready to actually merge it.

**danny**: Correct the TTD in the original configured is set to a very high number, similar to Ropsten. But we are planning the Bellatrix to just happen because we're not inviting lots of the community members to test in this arena.

**Tim Beiko**: Okay. Thanks. Any questions or comments on the launch of the beacon chain there? 

# j. Client teams readiness and plan for future testnet merges
Video | [51:40](https://youtu.be/dByC5Bw8DvU?t=3100)
-|-

**Tim Beiko**: If not, yeah so it seems like there's a couple interrelated things. First, now that we've seen Ropsten merge, what do we want to see and what state do we want to be in before we move to other testnets. And, second, is what the ordering of testnet should be. So there we mentioned earlier that we wanted to potentially do Göerli and then Sepolia, and then this week there's been more chat about maybe flipping them so that we actually go through, we actually go through Sepolia first. And then the kind of third related topic is the difficulty bombed and all that. And, obviously, if we want to delay the difficulty bomb, that might change kind not only the ordering but obviously the timing around which we do all of this. And I think it probably makes sense to just start to like hear from client teams, especially on the EL side but also CL teams have given that some of them are here. What are you kind of looking for to be ready to move to the next testnets like what would you like to see in your software and testing suites and whatnot. Marek,  think you are first yeah.

**Marek Moraczyński**: So for me a hive test be passing in all clients. Block proposals, of course. We are missing, I think, terminal block hash override. We discussed it, but not sure if all EL teams have implemented.

**Tim Beiko**: Yeah on that last point, I think we, we decided that not all ELs would implement it, because Geth already had equivalent functionality that people could use. So I think yeah we had decided against making it a must have for all the clients.

**danny**: There needs to be a credible path to implement on ELs, but we do not expect to necessarily have to use it. It has been deprioritized if people don’t have the time.

**Tim Beiko**: But then any client that already has the ability to set a specific head in the chain, it's quite similar to the TBH override. But beyond the TDH, the hive test and Kurtosis passing, this block proposal issue and then Thomas also added in the chat fixing this concurrency bug which we talked about it earlier. That all that all make sense. Łukasz?

**Łukasz Rozmej**: Optimally, I would like to have code that we consider finished all the required things for the merge. Which current ETA, we have currently very high velocity on that is around four to five weeks. But we can go earlier if that be the consensus for the other devs, but we would like to have at least one testnet after we finalize the code.

**Tim Beiko**: Right yeah. That makes perfect sense. Andrew?

**Andrew Ashikhmin**: For Erigon, we still have to fix a lot of hive tests. It's like we are failing at eighty-eight out of 110. Probably there is a limited number of underlying issues but still it's a lot of work to fix all the tests and also to improve the robustness of our block building code. And just more testing, more code stabilization. And we're still discussing how to tackle this issue when the latest block in the RPC request should wait for factories update head block confirmation. But it means that you kind of you before you have a new block added to the state, but you are supposed to point to the the prior block. In Erigon we only have a single state. How we handle that is not fully decided yet. So quite a lot of things. But I am not sure we'll be able to resolve all of them 100%. But I wouldn't say that we are couple of weeks away from being super ready, we need more time with. 

**Tim Beiko**: Got it. Thanks. Anyone from Besu or Geth?

**Gary Schulte**: I can say from the Besu perspective, I want to echo what others have said about across the board execution clients passing all of the engine hive tests, specifically. I think testing and expectations around post merge sync need to be ironed out. I think that there's just a little bit of maybe scenarios and expectations that we should set. Specifically for fast sync or snap sync post merge basically requires a consensus layer and I’m not sure that that's an expectation across the board. So just kind of buttoning up what we think post merge sync should look like.

**Tim Beiko**: So, when you say Besu requires a consensus layer, you mean like to basically run on the network is that right?

**Gary Schulte**: Well, in order to choose a pivot block. Post merge, we won't choose a pivot block unless we get direction from a consensus client and I think that some of the solo stakers have had questions about why Besu is not sinking when they don't have a consensus client on networks that have already merged.

**danny**: That's for any client combination. That's entirely why the whole optimistic thing exists in the consensus layer. So that good heads, reasonably good heads, can continue to be given to the execution layer. So it's requisite.

**Gary Schulte**: Okay, I saw some the war gaming that was talked about around sync and post merge sync, and one of the scenarios was execution layer sync without a consensus layer client.

**Tim Beiko**: But you can’t know the head of the chain.

**Gary Schulte**: I completely agree. I can't choose a good pivot.

**Tim Beiko**: Yeah, I don't know if that would be or should be possible basically.

**danny**: It’s not. There might be test cases where the execution layer is synced and the consensus layer is not, and then the consensus layer comes online and syncs. But I don't know exactly what you're referring to.

**Gary Schulte**: The execution API spec that I’ve seen leaves sink as a topic to be implemented by whatever method. It'd be nice to see this like a spec for post merge sink to just baseline our expectations.

**Tim Beiko**: I guess more from the EL perspective, right?

**Gary Schult**e: Yes, yeah, exactly. There's just generally more lead time for an execution sync than there is an optimistic sync on the consensus side.

**Łukasz Rozmej**: Okay, so, Nethermind is able to sync to the terminal block. But it doesn't sync any further without the consensus layer and it doesn't sync the state. So it only syncs blocks and headers. Actually, maybe not, because we have something called another pivot that we baked into our configs, which is a block we trust, a block from like few weeks ago, a week ago from the current head that we trust, and we can sync to. So we up it on every release. So that's how Nethermind works. I'm not entirely sure if Geth doesn't have some hacky way of syncing further, but I might be wrong. 

**danny**: I think they generally retain their sync methods, because the consensus layer just gives them heads and they do snap sync from there.

**Łukasz Rozmej**: So if they don't have consensus layer, what happens?

**danny**: They do not. They are out of sync, which I think is fundamental there.

**Bordel**: So essentially what happens in Geth is that currently we just try to sync to some… so once the merge happens everybody will propose the same total difficulty, so we can actually pick someone with that. Currently, what happens is that we just synchronize to some random person reporting the most the highest total difficulty. But obviously that isn't very good and we will only do this during the transition. And what we will do is we will add to the chain config that states that, yes, this chain has already successful merged. We would wait for the merge to happen and then flip it a week after. And after that Geth will simply stop doing legacy sync at all. So if that value is set when you start up Geth, it will just say that I don't have a beacon client, the chain config says that this is a merged network so until you attach a beacon client, I will not be compliant. Once the beacon client tells us what the head is then we can just snap sync.

**danny**: Having a beacon node here is akin to being able to do all the header chain and get what is the highest difficulty from what you can see from there and being able to sync from there. If you don't have the beacon node client, then you can’t follow any of those strategies.

**Adrian Sutton**: With the actual confusion that people expected to not have a consensus client or expected that the EL would be starting and making progress on sync, while the CL was thinking. So I’ve seen the ladder in conversations and that's just because we don't have a way to checkpoint sync on Ropsten because there isn't a place to get state currently. So that kind of solves itself on mainnet when it's much more common to checkpoint sync and your CL is in sync straight away.

**Bordel**: So one thing that may be worth noting, is that the consensus client, beacon client, doesn't need to be fully in sync. If the consensus client tells me that the latest block is something that may be one month old that's already enough for Geth to start syncing because we already have one potential target. And while the beacon client is just progressing with sync and finding new and new headers, we will just keep switching to the same target. But the only thing we need is one starting point, so that we can actually start sync. Syncing mainnet will take six hours, so I have six hours to figure out what the latest status.

**Adrian Sutton**: Yeah I mean syncing from genesis, you'll take at least six hours on mainnet for the blockchain before you even get to the merge block before you get any heads from us at all. But that's not normal right. The right way to sync the consensus layer is with checkpoint sync. We're just in this difficult place the moment with particularly Ropsten, which is a shorter chain, but you can't get a state from Infura. We're missing sources to go and get that checkpoint state so always syncing from Genesis. And it's taking the consensus layer some time to even get to the merge block, which I’m not sure how long that is on Ropsten. But then to get fully in sync as well it's just taking you know it may only be an hour or two and you'll start getting data from us, and then we'll be tracking the head. But I think that's causing confusion for users, because they're seeing the two clients start up and the CL is syncing and the EL is just sitting there doing nothing it doesn't know anything about the post merge chain yet.

**Bordel**: So one thing that, though, for example in Geth, we would you say is bothering us is that right before the merge, before the transition happens, you have beacon client connected to the execution client, but both sides are kind of just silent. So you don't really know what's happening. And I think if we could just make it a tiny bit verbose in that user has a clue that OK, now the execution client, although it is waiting for the consensus client, from that tag you get a sign of life that is actually doing something and it is actually progressing. It would be nice to have some form of minimal feedback that something is happening.

**Gary Schulte**: I think that makes sense. To add just something from the sync process that's going to regularly inform the user that it is waiting on a consensus layer direction. I think that would that would solve a lot of the confusion.

**Bordel**: So the Geth interface has a similar mechanism. If we are actually waiting for the beacon client that, as far as I know, periodically, we will print out the message that, yes, we are still waiting for beacon client to tell us something so that the user doesn't think that the client just died. The question is whether it would make sense to expose just a tiny bit of more information, so that we can see that, yes, we are waiting for the beacon client and that the beacon client is at this block. That might be worth considering, but it's not necessary.

**Tim Beiko**: What's the right place we should be discussing that? We can use the merge channel, but you know sync specifically for ELs. I guess, we have the execution dev channel. So I think it's probably worth just continuing that conversation there. 

**Bordel**: So I don't think there's much to discuss here, I guess. We can check out what it looks like. What, for example, the logs look like when you try to synchronize Ropsten currently with the current setup. And we can just figure out that it would be nice to have this or that extra information and we can just figure out how to add it. I feel like it makes sense to standardize how to sync.

**Tim Beiko**: Besu, you mentioned that it would be nice to have a bit more in this respect. Are you happy with this?

**Gary Schulte**: Yeah I think it's reasonable. Setting that baseline expectation, I think we're all on the same page about post merge sync it sounds like, at least with the implementations. Setting that expectation for the community is probably helpful and logging might be sufficient for that.

**Tim Beiko**: Got it. Okay, and Justin you had your hand up. Did you have a comment the sync?

**Justin Drake**: I guess my main comment was that shouldn’t we be having different expectations based on which testnet we want to target? So maybe the last testnet that we do if it's Göerli, for example, we will have very high expectations, maybe passing all the hive tests. But maybe we could have lowered expectations for the next testnet which could be Sepolia. I tend to agree with Danny that just commented Sepolia first. Maybe we can keep the ball rolling and try and do that first with no expectations.

**Tim Beiko**: Right. So I think that kind of leads us to the next bit, but just to make sure on the sync issue, it seems like there was nothing else there. And then, like just taking a bit of a step back, Nethermind, Erigon, Besu chimed in about where they’d like to be at, but Geth did you have anything else you wanted to add on that front? 

**Bordel**: No. So regarding the hive test. I’ve been working on that. Progress was a bit slow this week. It should be the possible next week to have to have the missing hive tests fixed so that it can be passed by all the clients.

**Tim Beiko**: Got it. Thanks. Łukasz?

**Łukasz Rozmej**: Oh I’m not entirely convinced that the tests are broken. Actually, I think that the test might test a decent scenario. It might not be easily passable on every class and because it might be hard to implement. But I will get up to you with that in a few days because I need to prove it that we can pass it and I’m not entirely sure. I need to do more investigation.

**Bordel**: It's possible to pass it but it's just way different than the spec that we have, so we need to implement something completely new, completely different than what we have already just to pass this one test, that is, this is not, not a real scenario.

**Łukasz Rozmej**: So the test is that network has correct blocks and our CL send us incorrect block?

**Bordel**: Yes, but our CL send us an incorrect block in the past that we have to stop and so that introduces a new caching mechanism that we have to cache all the new payloads which is nowhere in spec before that.

**Mikhail Kalinin**: Guys sorry for interrupting you, but I would take the discussion to the testing call.

**Łukasz Rozmej**: Agree.

**Tim Beiko**: Anything else on the Geth side with regards to just general merge readiness. I don't think there was

**Bordel**: So the thing missing in Geth right now is the safe block hash in the JSON RPC is missing. We have to finalize the JSON RPC. But other than we should be pretty good. I think there might be one or two hive tests that we are still failing.

**Tim Beiko**: Got it. For JSON RPC, it seems like having finalized is obviously a must have? Or at least a very, very nice to have? Do all teams have finalized implemented?

**Bordel**: We are.

**Tim Beiko**: Does anyone not have finalized? You have what's her.

**Marek Moraczyński**: Safe and finalized.

**Andrew Ashikhmin**: We haven't implemented it yet, but we’ll implement it so it's not it's not a big deal.

**Gary Schulte**: Yeah, Besu has safe and finalized in PR form right now. Not yet merged.

**Fabio Di Fabio**: It’s merged and passing the hive tests.

**Tim Beiko**: There's a couple CL teams here as well. So I don't know beyond everything we discussed. Is there anything on the CL side that you all are like looking for or want to see before moving to at least one more testnet. Terence?

**terence(prysmaticlabs)**: I think we are pretty much ready to go. We do have a few UX related issues that we want to deal with, but they're not blockers. On top of that, we are spending a lot of time working on MEV boost. That's not blocked as well, but that's a nice to have, to have that ready-ish. But that can always be brought in later.

**Tim Beiko**: got it.

**Ben Edgington**: No blockers for Teku I think. We're in testing with MEV boost stuff. So yeah, that's not blocker either.

**Tim Beiko**: Okay.

**seananderson**: Yeah, Lighthouse is on the same page where it's mostly UX and MEV boost testing.

**Tim Beiko**: Got it okay. Sorry was there another CL team?

**Mateusz Morusiewicz**: Okay hey. There’s actually some reservations on MEV boost. And need some guidance and help around this/ And they also should be ready for the merge.

**Tim Beiko**: Sorry. I missed I missed the first part of your sentence. Can you repeat that? Actually, can you just repeat that the sentence before they need to be ready for the merge?

**Mateusz Morusiewicz**: Sure, so we have some reservations from validator pools. In particular, around monitoring of the extraction of MEV. And then from the sole validators, they still don't know how to run MEV boost and they also have to be have to be ready.

**Tim Beiko**: Danny, did you have your hand up as well?

**danny**: I was just gonna say that MEV boost should continue to be developed in parallel. I would even argue that it's potentially a good thing if it’s rolled out right after the merge, rather than right before. Although just to reduce the potential attack surface and issues there. So I wouldn't necessarily put it as a blocker. I think that it should come out very soon after, if not during. 

**Mateusz Morusiewicz**: MEV can be really dangerous to what happens on the chain, and then we both actually can mitigate some of the attacks that can happen. So I would actually consider looking at the research and trying to answer this question - should we be releasing MEV boost before the merge, or should we wait. It's not that clear cut that MEV boost is an attack vector and I would argue that it actually tries to mitigate some of risks.

**danny**: I meant that it’s an attack vector from protocol construction. I just mean as an additional piece of software and a very complicated upgrade.

# k. Sequencing of future testnet merges
Video | [1:18:14](https://youtu.be/dByC5Bw8DvU?t=4694)
-|-

**Tim Beiko**: Yeah, just to not dive down the MEV rabbit hole for the rest of the call… I guess I’m generally curious to hear from just CL client teams. Given, like all of this, I feel like there's like a few options forward. One is we move to Sepolia as the next testnet and use that as a better run than Göerli, probably not with the software that that will end up on mainnet. And we keep Göerli as the final testnet for that to happen. Or the other way around, we wait until we have something pretty stable and then shipped out on Göerli first because there's more users and then Sepolia is just kind of a quick sanity check at the end that can happen quickly after. So I guess generally people prefer to have the next testnet happen sooner to get us another round when we have some confidence that we've addressed these issues, but we're maybe not quite at mainnet code or do people prefer to wait longer and then maybe you just have Sepolia happen like really quickly near the merge but Göerli being the testnet to basically deploy closer to production ready code. 

**Bordel**: Okay, so. When we start working the testnets, it would be nice to finish with actually forking mainnet. Otherwise it'd be just for the testnet and we never reach mainnet and we just have a two month gap in between them then by the time we reach mainnet...

**Tim Beiko**: So you broke up a bit, but I think beyond the momentum bit, there's also the idea that if we fork testnet and then wait two months to do mainnet then there's a bunch of other PRs that get in the clients and that would go directly to mainnet.

**danny**: Yeah I was just going to say on the consensus layer call, consensus layer teams want to do Sepolia first, so that we can kind of keep moving in a moderate stakes environment and then ramp up and make the decision on Göerli.

**Tim Beiko**: Any EL teams have anything to add here?

**Gary Schulte**: I was going to say was the June 20 genesis for the Sepolia beacon chain in line with the somewhat accelerated or the Sepolia first timeline or would that change?

**danny**: That works for Sepolia first. Assuming that in two weeks we've circulated the TTD or we’re picking it for div

**Tim Beiko**: It's like the minimum duration right? We could have Bellatrix and then TTD two weeks after that.

**danny**: Right right I just mean if it lines up with TTD soon-ish. and getting it done. I don't think we're going to do Sepolia in a week so. You can do Sepolia beacon chain in 10 days and doing Sepolia shortly after first works with the timeline.

**Tim Beiko**: Okay, that makes sense. Lucas?

**Łukasz Rozmej**: So I would like to have a bit of time to progress with the all the things we mentioned. You know it all depends on the details of the timeline really so maybe let's discuss propositions on that.

# l. Delaying difficulty bomb 
Video | [1:23:45](https://youtu.be/dByC5Bw8DvU?t=5025)
-|-

**Tim Beiko**: Okay, and I guess. TJ Rush, I was gonna mention the bomb. Do you want to give a quick update there?

**Thomas Jay Rush**: If you don't mind I’ll share my screen. It'll kind of set the stage for what I think we can. Are you seeing that? Yes, okay so just to get you where we're at we're at like 14.7 second blocks here and, if you look over here. You can see it's going to probably be down around 18 to 20 seconnd blocks, I think, by the middle of July, maybe the end of July. I’m conservative so I’m going to say the middle of July you're going to be at 17 or 18 second blocks. This is another view of the same data just so we get 14.7 is the current time. There's a couple of scripts out there that are actually inaccurate. They're underestimating the effect of the bomb, so this is accurate data as of this moment. So I think there's basically three things we could do. We could delay, remove or just do nothing. Each of these has different good and bad points. Delaying it gives you time. Obviously it's hard to delay to an accurate place and it looks bad to the community. But there's nothing you can do about that. Removing  it is also looks bad. It's actually good, I think, because you could make an argument that we no longer need it because this merge is going to happen and it's kind of a sign of confidence in the fact that it's going to happen. But it might also be interpreted really badly by the community. The third thing is to do nothing, and that obviously has the very bad outcome that you have 20 or 30 second blocks by August. But I think it's actually maybe a good thing, because the community I think of it as hitting the community on top of the head with a stick and saying hey you know, the core dams are great group of people, but the community has to pay attention to the fact that the core devs has the power to make this decision. We can use that to say, you, community have to become more involved in these kinds of decisions. It can also be interpreted as a threat, so that's a really bad outcome as well. So what I would do, and nobody asked me, but this is what I would do I would simply remove it. The next thing I would do after that is do nothing at all and the last thing I would do is delay it. Now, I know that's probably not how it's going to happen, it's probably going to be delayed. If you delay it, what I would do is I would absolutely make a decision now. I would delay it for a longer time than you think you need. I would make a very loud, very public announcement of a date when you're committing to make the merge. That gives you like, if you do miss the date, if you do this in three months, you have some flexibility. So the same exact thing happens if you remove it, you can make a very loud announcement, but I think you need to make an announcement now and I wouldn't try to delay it to a precise place.

**Tim Beiko**: Thanks for sharing. I do have a couple like high level thoughts. First, I don't think we should make a merge date announcements. I think that will just backfire. I don't think announcing the merge date is in any way a possible option. I think it might make sense to just here… I know, Tomasz put together and EIP based on the discussions on the previous call so it might make sense for Thomas to take a couple of minutes to walk us through that as well. And, like the reasoning there for a delay. And then I see there's already a bunch of people with their hands up.

**Thomas Jay Rush**: Let me make one quick point. By making a delay you're definitely creating a merge date because that's what the entire world will think that is.

**Tim Beiko**: Sure, I'm not as concerned with like the perception of it. Like if we delayed a bomb two months, four months, six months, whatever. And, whatever the commitments we make like I don't care if there's some articles that say that the merge is delayed till the end of year. I do think that us announcing the merge date is really bad because it's actually us announcing a emerge date. Tomasz?

**Tomasz Stańczak**: Hi so EIP-5133 was proposed and the calculation is based on the discussion from our last session. It proposes 500,000 blocks delay which picks a mid August for the for the bomb to activate. So as we know, the bomb is already activated and I think it looks worse than some people thought it was based on what TJ mentioned a moment ago. The value is calculated based on the scripts that we have show around 0.1 seconds delay by mid August, with these numbers. Around 0.6 seconds so around 40 seconds blocks again in November and then very, very steep decrease. So it actually is all based on we wants to have a stable network behaving as expected that degrades when we think more or less the merge should happen and mid August was that target for now. So please have a look at EIP-5133. I agree also that's we shouldn't really announce the date of the merge until we know exactly the terminal total difficulty because people will make a lot of decisions and preparations based on that date. So we have to be absolutely sure of at least that like days or a week when it happens before announcing. We are not sure yet. To remove all of the bomb, I think that puts us at some risks in case some particularly unexpected event happens where the delay is significant, and then we lost the bomb that so far, I believe, always worked for having everyone prepared for releases and for acting. So once again I don't think that delaying the bomb delays the merge. I think it's simply says that the bomb already started happening, we already missed the previous estimate in June. This one simply moves it to our current plans of mid August.

**Tim Beiko**: Andrew?

**Andrew Ashikhmin**: yeah sure, so I think that delaying the bomb is the best option. I don't think that it sends a bad signal, it actually sends a good signal that we are doing the responsible thing, that we don't want to rush the merge with the code that that is not ready. So we kind of move in the bomb to a realistic date. And it synchronizes our share do with the bomb and doing nothing would actually be irresponsible, because then it'll hurt the throughput of the network and I don't see a point in some silly political game. I don't get it, so I would delay the bomb.

**Tim Beiko**: Ben?

**Ben Edgington**: Ieah, I disagree with your point Tim and others have made about not announcing a date. Let me explain why. What I think we need is a sense of urgency. I’m not really receiving a sense of urgency about getting this done. There are very real costs associated with not doing the merge. 130,000 tons of carbon dioxide every day. That’s nearly a million tons a week. Every week we twiddle our thumbs that's a megaton of carbon dioxide that we're emitting. This is a very serious issue. Where do we get a sense of urgency from? Well, the bomb is very powerful sense of urgency currently. Though, the timing may not be ideal. But I think we owe it to ourselves, and we benefit strongly as a distributed community to set some other mechanism by which it gives us a target. So things happen in this community when we have a target to work to. This is my observation. This inculcates a sense of urgency that may get gets things done and I’ve seen it so many times in Ethereum world. So I would propose if we do delay the bomb, we also commit at that point to a timeframe for delivering the same.

**Tim Beiko**: That makes sense. The challenge is, if we commit to like a timeframe, we can't like set a specific date because there are unknown unknowns. like if we have an issue show up two weeks before, we want to fix the issue rather than having a Ethereum go down, even though there's a cost to, obviously, staying on proof of work and delaying the bomb. My opinion is like if we do delay the bomb, we should implicitly target some realistic delay which I think is what Tomasz’s EIP was attempting to do. We can discuss whether 500,000 blocks is the right amount – it should be there, it should be four, it should be six. But, for example, if we delayed the bomb by like 12 months, I agree that would be really bad. I think on the sense of urgency, it's worth noting on the last call and privately to me client teams have mentioned that you feel pretty stressed and urgent. I think there's a fine balance between having a sense of urgency, but just having people be so under pressure that the quality starts to drop. I guess to summarize, if we do delay this I think it should be a realistic delay like to still maintain this sense of urgency. But I also want to point out there is a point where too much pressure just pushes teams to burnout or make worse decisions and that's also not the situation you want to be in. Tomasz and then TJ, and then if anyone has any final comments please raise your hand now and we'll do a final round and then wrap up because we're already at time.

**Bordel**: Like we kind of discussed a bit just now, and we can all agree that delaying the bomb is the way to go. And we should do some calculation that pushes the bond by roughly two months. And also, we can we can push off the boat delay today if we want to. Like scheduled for as soon as possible.

**Tim Beiko**: So on that note, there are some comments in the chat about that. Ansgar you have a comment that we should make the decision today. But I think it was a year ago, Ansgar, you made the comment that we should probably not like include EIPs in hard forks on the first call that they're presented to give people time to think through them and think through the values. So I would be pretty against setting the hard fork and making this delay official right now. For sure on the next call, we can. And we can discuss exactly what the number is, what the right approach, if that's what time teams want to do. That’s my opinion 

**Thomas Jay Rush**: I’ll just go real quick. I totally agree and understand everything everyone said in response to what I said and obviously, whatever happens happens. I think what I’ll do is just go back to reporting on what the timing looks like as far as how long the blocks are taking. I do think it's getting a little urgent to make a decision on when to do this fork no matter what we do. So thanks for listening.

**Tomasz Stańczak**: I would like to suggest this urgency, or even like vote now to announce the fork date on the clients when this would be implemented. That we already see like the 17-18 seconds blocks at the time the fork would be activated if we announce it for like three weeks from now, let's say. I don't think we should be waiting for the next AllCoreDevs. And this 500,000 blocks calculation is based on the suggestions from the last call, so it actually is two and a half months. Just to address what Marius was saying, if there is some miscalculation, please let me know, but just posting here that we have around 6.5 thousand blocks per day, which is around 190,000 blocks per month and 500,000 blocks is around two months 18 days or two months 20 days.

**Thomas Jay Rush**: yeah I always say 100,000 blocks is two weeks so 500 would be about two and a half months.

**Bordel**: Sorry too Thomas, we weren't trying to pick on you. We were just going up by the comment that Ansgar made that longer block times that we see right now would only happen in November. And I think that's a bit too much.

**Tomasz Stańczak**: I do believe that what’s happening now it's already a problem. I mean, in 1, 2, 3 weeks we'll have real degradation of the network. It's already affecting the mining pools. The users of the network know, base fee is going up so.

**Tim Beiko**: yeah I do think we should just review the numbers offline and to make sure we're all on the same page. I’m curious to hear from EL client teams, do you think this is a decision to take now? Obviously Nethermind does. Geth seems to be on board, but the I just want to make sure. And then, if the decision is we do delay the bomb by some amount that's roughly two months, obviously we need to figure out what those things are. What the exact block number of the delay. I don't know that we would want to choose the block height today. I think we can probably get that done async as well and not just rush it. and. I think we can make a decision about like the general like we do want to delay the bomb by some small amount of months, but I just want to make sure we don't like rush figuring out the exact details on this call. And actually take time to like think through how much, and when we want it to go off. 

**Bordel**: Yes, exactly this. We decide today that we want to delay the bomb and we do a sync to do some calculations and we decide on what to delay the bomb now as soon as possible. And we should maybe already do the timing for the next delay fork. We also need block numbers for that.

**Tim Beiko**: I just don't want us to come up with a block number in 30 seconds and it turns out to be wrong.

**Micah Zoltu**: We don't we don't need a block number, we need a date. I think we pick a date like say you know, in three weeks that. We can figure out what the number is for that later, but we can just choose a date.

**Tim Beiko**: I think that's that's helpful. Does Besu and Erigon generally agree with that? I just thought I'd make sure that.

**Andrew Ashikhmin**: Yes, I think we should delay the bone and I think something in a hard fork something through three weeks would be good. And that we can discuss the exact block number offline. But I do think that we should we should decide to delay it now.

**Tim Beiko**: Okay. And Besu?

**Gary Schulte**: Yeah that sounds reasonable to commit to a time and then back into the block height. And the delay sounds quite reasonable, especially if we do the off-cycle ACD call time for that.

**Tim Beiko**: I wouldn't do an offcycle ACD call, just to be clear. We have the CL calls next week and EL client teams can show up to that as well if we really need to. But I think if we have the decision now and we agree to the block number, the block number both for the fork and for the delay async, we can just communicate that both async and on the CL call. But I wouldn't have another AllCoreDevs a week from now just for this. Then the other part is when does the delay happen. I heard like three weeks. The thing I would want is at least two weeks from releases being out to the fork happening. Does that mean that client teams, assuming that today or Monday we get a block number and block height, Next week you can have a release that's ready for that? Is that is that reasonable?

**Łukasz Rozmej**: No problem for Nethermind.

**Tim Beiko**: I think if we have releases out next week, it means we can announce them early the week after.

**Tomasz Stańczak**: I suggest 29th of June, which is Wednesday. Usually the Wednesday releases were the safest. For the fork. Which means that now offline we can confirm the numbers, but everyone can start implementing EIP configuration to switch it on. Then we can confirm the number offline and in two weeks on the AllCoreDevs we can just confirm that everyone is ready, accept and then the Wednesday after the AllCoreDevs on the 29th this would hit in.

**Tim Beiko**: Yeah I think we're going to need confirmation that teams are ready for that. So my hope would be to have a blog post for this by Thursday or Friday next week with all the client releases. And then one other thing that we need is some amount of testing for this, which is not huge, but we also need this to happen, obviously.

**Bordel**: So I think Tomasz said we need to have a confirmation in two weeks that everybody is ready. That would be three days before the fourth. That is definitely way too late, so yeah if you want to fork in three weeks, my expectation is that Wednesday, this Wednesday, we have a confirmation from everybody that releases are out.

**Tim Beiko**: I agree we need to have the releases out by this Wednesday. Actually, yes the releases should be out and we should announce them by the consensus layer call on Thursday, which is at 14:00UTC on Thursday. 

**Andrew Ashikhmin**: That’s fine for Erigon, but we need a name. 

**Tim Beiko**: Yeah, we’ll do names on the CL call as well.

**Łukasz Rozmej**: “Merge is close” as the name.

**Tim Beiko**: Thomas you still have your hand up. D id you have a final comment there or just up from last time.

**Bordel**: So one thing to reiterate for everyone listening, this does not mean that we will delay the merge. The merge will not be delayed, we are only delaying the difficulty bomb and it will also take no capacity away from working on the merge. This is like a five line change and we can put it out in 10 minutes and this does not impact the merge at all. 

**Tim Beiko**: Okay we're already about 15 minutes over. There were some EIPs that I wanted to give updates. I think it makes more sense to move them to the next call so they have proper time. I would encourage people to check the links in the agenda for EIP-4444 and the EIP-5027. There's also a quick announcement. So next Friday, basically a week from now at the AllCoreDevs time there's a EIP-4844  call because there's already a couple teams prototyping it. So if you're interested in that, the links to the agenda are available. And then similarly to that, for EIP-4844, there's a bunch of people working on that and we're having public calls I believe every two weeks now. So if people just want to join or watch the recordings, those are going to be in the agenda as well. Just to reiterate, the decision about the bomb is, we're in agreement that basically include Tomasz’s EIP, still some bikeshedding to do about the exact number to make sure that it's correct. The activation number which should probably be about three weeks from now roughly around June 29. There are some comments on the chat about, we need to keep the testnets merging as well. I think that's that's correct, but obviously, like a bunch of client teams have mentioned, they do need more than two weeks before they're ready to fill out a release for these. So I suspect within the next few weeks, we this release sort of the bomb that happens. In parallel, we keep working on Sepolia, and that will merge sometime probably right after or close to the difficulty bomb being pushed back on mainnet. Any closing? Oh yeah, there's another comment about continuing shadow forks. We can discuss that on the testing call next week.

**Bordel**: So one quick thing. We still have shadow fork manager for to running around, and we would like to deprecate it. But before that, we would like to run sync test or I would like to run sync tests. I'm doing the sync tests for Geth. And I think it would be really nice if all the other clients could also run their sync test on manager for to. That would probably be interesting.

**Tim Beiko**: Okay. Let's wrap up here. We're already 15 minutes over. Appreciate everyone staying on. And again, apologies to the folks who had a piece to present. I'll make sure to get to those on the next call. Thanks everyone.


------------------------------------------
## Attendees
* Tim Beiko


---------------------------------------
## Next Meeting
June 10, 2022, 14:00 UTC

## Zoom Chat 
