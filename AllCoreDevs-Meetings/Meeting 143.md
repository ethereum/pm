# All Core Devs Meeting 143
### Meeting Date/Time: July 21, 2022, 14:00 UTC
### Meeting Duration: 1 hour 30 min
### [Github Agenda](https://github.com/ethereum/pm/issues/572)
### [Video of the meeting](https://youtu.be/N80PgxELDYg)
### Moderator: Tim Beiko
### Notes: Alen (Santhosh)

## Decisions Made / Action items
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
|143.1 | So, based solely on Goerli's.  So the next releases from client teams, such as the Goerli fork, would be available next week. We've had Bell tricks since the first week of August. I believe we said August 4th, then TTD on Goerli happens around the second week of August. And I believe it's now estimated to be between the 8th and the 10th. And then maybe the TTD the week after that, is the merge strip block happening on the Sepolia. - Tim| [07.24](https://youtu.be/N80PgxELDYg?t=443)|

 
## Intro [3.16](https://youtu.be/N80PgxELDYg?t=195)
**Tim Beiko**
* So hello everyone. Welcome to All core dev. Devs number 143.
*  First one on a Thursday. a couple of things today. on the merge side, we wanted to discuss, setting the merge nets split blocks, for some Sepolia. and then on the cl call last week, we, this, clients activating, the authenticator ports before the merge and wanted to continue this conversation some more. then on the Goerli side, we we've kind of agreed on the Bellatrix, epoch, heightened and TTD, but we can check it on that. 
*  There was also the Goerli shadow fork it happening, little minutes ago. and then some updates on MEV boosts, beyond that, we also have some updates on EIP 4444, which, we've been kind of punting from call to call recently. There's been some work done on that and, yeah, that's, that's pretty much it, I guess to kick it off, on the, the Sepolia. So on the last call we discussed the idea of setting this in Sepolia, and Rosbten merged Smith blocks who decided not to do it for upstate because Rosbten is considered deprecated already. and, for we had, I believe  the idea of combining this Sepolia with the Goerli merge releases. and I know Marius, I think you were the one who wanted to discuss that last call, but you, you couldn't make it. So, yeah, maybe you want to just share your thoughts about this and how you think we should, should go forward. 


## Merge Updates [4.45](https://youtu.be/N80PgxELDYg?t=284)
**Marius**
* I don't really, I don't remember that I wanted to discuss this, but, I, I also don't have any particular, opinion either way, but I think if we're going to have a release, we can also specify the Sepolia net split block. I think it's, it just makes sense to have, have it in the same release because then we're not wasting, more time. yeah, it should just be a small change. Everyone should have already implemented the merge net split block, in the code. And so it should just be setting the parameter for the Sepolia. Yeah, Danny. 

**Danny**
* Yeah. I just wanted to say in terms of, I think it's valuable to do just so that we go through all the motions before mainnet, not that we do soon. And so, you know, on that, on that release timeframe, and then maybe because it's also easy to coordinate because of the fixed validator set and then deal with Gorley after main net and deal with mainnet after mainnet.

**Marius**
* Any opposition to specifying the Sepolia merge block in the next releases for clients. 
* Okay. then we'll, we'll, make some calculations what we want to merge net split block to be. And we can probably just, or we don't, we don't need to have a big discussion about it. We make the calculations and update everyone on the Allcoredev about it, and everyone puts their, on discord about it. Everyone puts the thumbs up and then we can put it in the mix with this, with the Goerli TTD. 

**Tim Beiko**
* Yeah. So, just based on Goerli's on Goerli, on Danny's chat comment. so that means we would have the next releases going out from client teams, like next week for the Goerli fork. We have Bella tricks happening on like the first week of August. I think we said August 4th, then we have TTD on Goerli happening on like the second week of August. And I think it's like now estimated between like the eighth and the 10th or something. And then maybe the week after that we have to do, do you have the, are the merge strip block happening on the polio? So like yeah. On the week of like the 15th or something like that, does that seem reasonable to people? 

**Marius**
* I think we can, we could also just put it in the same week as one of the other things. 

**Tim Beiko**
* Yes. So we don't know when Goerli's going to happen though. Right. Cause the POA, rest with Sepolia kind of know about the block time are fixed now or at least we can know the earliest, it could happen. Marius, do you want to explain to Paul 

**Marius**
* So much net split block is basically just an empty folk on the execution data? that does nothing. It's just the hard fork and, we don't really need it needed. but it makes, makes P2P discovery way easier because we will, verify the fork ID. Basically every node tells us on which fork it is, pretty early in the protocol. And so we can, we can verify that the other node is on the same focus we are and if they are not, then we can drop them. So from my point of view, we can, we can just have this fork happening, one week after the release. 

**Tim Beiko**
* Well, I guess he had just from a communications perspective, it's probably easier to just focus on the Goerli merge because the Goerli Bellatrix forks will happen one week after the release. so it's probably just easier to tell people Goerli's happening. And then after that Sepolia is doing that, and that would also match what would happen for Gordian for main nets where we'd do the Goerli. split block kind of in the same release as the main that merged the targeted for later after, like the mainnet merge. And then, and then for my mainnet, obviously we do that just after emergent and separate previous. 

**Marius**
* Yep. 

**Tim Beiko**
* Cool. Any objections or thoughts from other teams or does that sound good for everyone? Okay. Okay. YWeou got that. thumpup's up. cool.

## EL clients auth ports activation [11.00](https://youtu.be/N80PgxELDYg?t=664)

**Tim Beiko**
* And then, then the next thing, we wanted to chat about, Paul, I think you started this conversation on the, on the cl call last week, but the idea of having email clients activate the authenticated forward before the merge happens, do you want to get some clear conflicts there? 

**Paul Hauner**
* Yeah, sure. So the, the idea is having, you know, clients open all thought before them, parameters specified. So, for instance, on main net, turning on allowing us to use the old port now, even though it, the badge parameters is not being decided yet for main net, that means that users can start setting up the AL and see how exactly as it should be run for the merge. now rather than having to wait for the nodes for MSPs you've specified, this is particularly useful because we've just put in a bunch of stuff, about nudge readiness, so that we'll start logging to use this. We wanted to do two weeks, but if we can't do it now, cause the ELL teams on I've seen that port, but, we're doing it one week now before port, we'll start logging warnings. If you're not set up properly for the merge, we want to have that a long time before the real nudge. so yeah, hopefully that's enough information. 

**Marius**
* Thank you. Yeah. So we have, we have a PR open for that for guests for a long time. And we also talked about it and agreed that this what we want to do. So we just need someone to push the button. 

**Paul Hauner**
* Other clients either sign it. 

**Marek**
* So we're there maybe, we are working in this way already, so it's not a problem for Nethermind.

**Micah Zoltu**
* Nice. Is there a reason geth hasn't pushed the button yet Marius or is it just the one hitting the button? 

**Marius**
* No one has gotten around to hitting the button. I can not. I made the PR so I cannot push the button myself. 

**Guillaume**
* Well, you can, if you have approval, I don't think so. 

**Marius**
* It doesn't matter. We don't. Yeah. 

**Tim Beiko**
* Okay. But this, this will be part of the, I guess you can have this as part of the Goerli merger next week, right.Besu?

**Gary Schulte**
* Basically, to be honest, I didn't a hundred percent follow that. Other than that, we were going to, have a, a warning if the CL is not, get an engine API for the execution layer up to some, some portion ahead of the fork. Is that right? 

**Paul Hauner**
* Yeah. So the idea is that, we want to be able to have the, consensus of talking to the execution through the old port. We want to be able to do that basically from now and not waiting until the merge parameters are defined, you to, does that make sense? 

**Gary Schulte**
* So, yeah, That makes sense. One of the, one of the current configurations of basically is that if we don't have a terminal total difficulty, we don't enable the engine API. we could probably change that behavior so that if we don't have a TTD, we can go ahead and have the engine API active. 

**Paul Hauner**
* Yeah. Cool. That'd be super handy. yeah, it helps self users up there. configurations,  the dev ops, Ellie. 

**Gary Schulte**
* Okay. Yeah. We'll get a ticket for that. 

**Tim Beiko**
* And Aragon, 

**Andrew**
* I think you already have, the engine api available, even if there is no TTD. 

## Goerli updates [15.00](https://youtu.be/N80PgxELDYg?t=914)

**Tim Beiko**
* Yeah. That's that's we get to hear, any other comments, thoughts on this? Okay. I guess next step, just to give a quick update on Goerli. So, we, we kind of chose the blocks, or the height and TTD earlier this week. so, for anyone listening, the Prater epoch, which will activate Bellatrix and kind of ready Prater to merge with Goerli is epoch, 1, 1, 2, 2 6 0, which is expected on, August 4th at, 1224 UTC. and then the TTD that we're going to use for the transition on Goerli is, 1 0 7 9 0 0 0 0, which we expect to happen the week after. so th th the difficulty on, on proof of authority, which word to use varies at odds, but it should happen, sometime between the sixth and the 12th, and more likely between the eighth and the 10th. and I, yeah, so that's when the Goerli merge is happening. So people should, should be on the lookout for an analysis, clinched it up. and then for the announcement, if it's possible to have clients for DCS out, in the first half of next week, that'd be ideal. So we can just, yeah. Communicate those by the end of next week. does that sound reasonable to everyone? Okay. Okay. No one complaining. so that's good. and yeah, if you're a Staker or, listening, running through kind of the merge on Goerli is the last chance you're going to get to test everything before maintenance. so if, if you're, if you want to ensure that, you know, everything works through the tire process, now's the time to do it. if you don't want to wait for the Goerli merge, the Robson network has a public validator set as well. So you can stand up a node on Robsten and basically set up all of your configurations and it's the exact same process as it will be. So even though you don't run through the merge, kind of setting up everything to upgrade post-merger is the same. so that's something that people can do, if they don't want to wait for the Goerli merge, but to run through the entire transition. this is, the last time, yeah, you go, And 

**Micah Zoltu**
* This, this isn't just for stakers, everyone who is running a clients should it's your last chance to test the merge. And if you're an adjusted yield right now, you will need to install and set up access to their clients before the merge, otherwise your node will stop working.

**Tim Beiko**
* Yes. Thank you. yeah, so, yeah, not just stakers, and, but obviously if you just run a node and turn it off and turn it on after the merge, there's no economic penalties, but, if you want to stay up through the entire process, you need to have the same infrastructure. yes. And if you're an exchange, hopefully you're already well aware of all this. And, but yeah, please start looking into it now. and, the blog post next week, we'll have all the Goerli specific trine versions, but all the times that are out today, support robsten. Then if you want to try that out before the announcement, anything else? I'm Goerli. Okay. 

**Danny**
* This is a good time to talk about the Shadow fork is happening right now or does it 

**Tim Beiko**
* Oh yeah, actually it is. 

**Parithosh**
* Yeah. Give us an update on that one. so yeah, the shadow fork happened roughly an hour ago. We did have a TTD override earlier today. I think we were around 98% participation rate before, shortly before we hit TTD and notice the numbers based node ran out of space, we have two of them, so it's not a big deal, but, yeah, so that we're paying down the maximum possible collect 95%. And I think currently we're about 86, 87%. We're looking into the missing clients where it looks like prism that nethermind's returning an error for a fork test update. And there's one teku nethermind that might need some help on some other fund. And I think prism Aragon is stuck, but it might have actually continued. Now I need to still look into that ELLs posts like a complete update. Once client teams have had time to look into it. but because we've run more than one node of each client pair, the issues also don't seem like inherent to one client, but there are two prism, nethermind notes. One is fine. One isn't. So it might not be a, client issue. It might just be the sync state. The client was in when TTD was hit, et cetera. nonetheless, we still look into it and report that

**Tim Beiko**
* Nice. So we've gone from like issues with clients, the issues with client pairs there now issues with specific instances of client pairs 

**Danny**
* Is the approximate number of block proposals equivalent to the approximate number of stations is something like 85%. 

**Parithosh**
* Usually that's also, I just quickly don't eth2. And it looks like it's about that. We still of course, have to look into how many transactions are being included and, Sync period participation rates. It actually looks really good. We're at 90% for the entire hour almost. So that's nice. 

**Tim Beiko**
* Anything else on the shadow fork? 

**Parithosh**
* Yeah, we will be having the mainnet shadow fork next week. I think it's shut your for the fifth conflict should be out. And the other thing is we will be testing MEB boost on Goerli shadow fork tomorrow. as far as I know the release is up, but we wanted to wait until tomorrow to have enough eyes on it so we can set them up manually and have a look at it with both teams first. Cool. We'll report back on how that goes. 

**Tim Beiko**
* Thanks Pari. Anyone else have anything on their shadow fork?

## mev-boost failures & liveness [22.26](https://youtu.be/N80PgxELDYg?t=1346)

**Tim Beiko**
* Okay. okay then, next up, we have Leo with an update on, MEV boost and preventing LifeNet, failures, even though he does have some issues. yeah. Do you want to give a quick, made there? 

**Elopio**
* Sure. I will be short this time. so our main priority is not to break the blockchain, right. we currently have, these good enough set up that relies on a trusted relay and, we are figuring out what comes next to make things permissionless. but we want to make sure that, we test the conditions that could break the network. So this is just to get some eyes on this issue that I linked on the MEV books repository. We will be making a brainstorming of the things that could affect, the likeness of the network. the most basic case like this, I will incidence. This is already better to what we have on propor because of this sidecar design that we agreed to, which I think, enables us to do a lot of experimentation without a lot of risks. So in the case where there's one trusted, really, and things start to become weird, the solution is just to put upline that relay, and then the consensus clients will just switch to local building. so our point there is to make sure that this mechanism is in place and while the consensus clients, we are not relying on this, and well then more conditions. What happens if, last what's becomes evil and it has a lot of, usage and well, the basic case, the not so, strong case, the people who have permission to monitor and put the relay upline are like four or five. So this is not just a person going, this requires like a coordinated effort, that alleviates some of the pressure, but still, not good enough. Right. So let's think about all the possible conditions. we have the issue open about designing our relay monitor, in the case that there are multiple relays that get, a lot of pitch, a lot of usage, but then we need to figure out what we are monitoring and, how this translates on an evaluation of risk for the proposers and what they are willing to sacrifice in order to get more reward, or maybe this should be just like a binary. this is, suspicious really. don't use it for now and we'll get more, permissionless this science. so if you have ideas, if you have concerns you should to, to, to, and, now that we are testing Goerli and preparing on, on the test nets, we, with relevant data, it would be, I think, required to test this conditions. So once we have, a good amount of validator, some Goerli using maybe boost and using the relay, then we shoved the relay for an hour and see what happens. or we try some other like more extreme conditions that will shape the network. And that will inform us like, where are the holes, what things are vulnerable. And I think we will be more confident, to put this production on maintenance at the merge, and any thoughts?
* Alright, so I insist this, take a look at the issue. We will be bringing this to the next week's call to, talk to the consensus clients, make sure that everybody's aligned and see what kind of, checks can be implemented on the relay or maybe posts or on the client implementations. Thank you, Tim.

## EIP Discussions [27.47](https://youtu.be/N80PgxELDYg?t=1664)

**Tim Beiko**
* Cool. Yeah. Thank you for, do you update and I shared the issue in the chat, for people, anything else on the merge generally? Okay. then next up, we have, an evade from Henry who's been working on EIP for the past couple of months. And we've had to move this update to like across the past three or four Allcore devs called because we were so busy. so yeah, now we have the time to go over it, but, yeah, Henry, you want to give a quick kind of recap on what you've been doing and then, kind of the, the draft EIP that you have. 

**Hentri DF**
* Yeah. Short-term thanks. So yeah. Hi everyone. I want to give a quick update on this work. maybe just some background I'm not going to do well, VIP is pretty EIP for force is pretty straightforward. So, an a really quick description is basically it's any IP that seeks to limit the amount of historical data specifically, not state blocks, blocks, receipts, headers that nodes need to keep. And, and it, so the goal being limit the amount of storage for historical data past some age, as well as limit the amount of P2P traffic for syncing that data, EIP for fours is quite general in that it's, you know, it addresses this in a general manner in a way that would be, that will be applicable both today. And post-merger, you know, basically it says age out data passed some certain, some certain age. the work I've been doing recently is a kind of a first step that we feel, along specifically with the EIP authors, that, that there'll be a good first step. And we have a good opportunity for this soon, which is applied EIP for fours, for pre-merger history. So soon we're going to have the merge point and, and then some time after that, we could potentially say, Hey, you don't need to keep all the blocks in the headers, unless you want to, at least you don't need to serve them. if people want to sync those blocks, they would get them out of bend. that's kind of the high level context. And, and so the work I've been doing here is, well, let's assume we were in that situation.
* We wanted to do this and we have consensus and so forth. what this, how do we distribute these blocks? What is it going to look like? and so I've got, let me post, oh, great. I see, I see Tim's posted everything in the, in the chat already. so the first link is a link to a repo that has basically, SSE specs for, for encoding a  run of blocks with, headers and receipts, into SSC. So maybe a little, kind of context here. 
* I think initially there was, there was some agreement amongst a bunch of people who discuss this, that, well, we could store this in our LP as is the current export format. but I think everyone agreed that we wanted to move on from that for a bunch of reasons. and SSE given that it's, we're using that extensively in the beacon chain, it, it felt like a good time to move this data to that format. and well, it's, of course we use this in the beacon chain extensively. some of the nice things we get for free by doing this, or the one key thing we get for free by storing this data in SSE here is that we can, we kind of get out of the box, the hash road computation and, and, and all of that. So with these block archives, we can then, provide the witness hash through just directly through the SSE machinery that, that does that for us now, the, so the, the format itself, I'm not going to walk through everything. 
* I'll just kind of describe the high level outline, but this is definitely something that I'd be interested in feedback on. well, there's kind of two levels to this. There's a general approach. And then if the general approach is, you know, is agreed on, then there's all the kind of details of the SSE specification itself, which, you know, the more eyeballs we get on this, the better and, you know, getting down to like low-level tweaks and minor changes. 
* I think that, you know, it'd be great to have some, some people scrutinizing this, at some point, but the high level idea is this borrows from the beacon chain execution, payload, layout pretty extensively, but with a few adaptations in that, you know, here with, we're talking about proof of work blocks right now. So these need to have uncles. And, you know, there's a couple of fields that were repurposed, but it's, but it's pretty close to that. unfortunately it's not identical, but it's pretty close or it's extremely close. and so that's the basis of it. And then as an archive header container, I'm looking at that, the first thing that Tim pointed, which is actually the EIP draft has the same information. There's an archive header container. an archive body is just, sorry, there's an archive body, which is just a list, an SSE list of these blocks. So we can get the, the hash tree over that list, you know, rather than say, concatenate them outside of SSE, just concatenate them, into a file.
* We put them in an SSE list that, that makes encoding, decoding a bit more, resource intensive as you need to read everything in. But, but it, it allows us to get that the hashing, and, and then as a, a little header with a version and a, and a couple of fields on, on which block range or reign yeah. Which block range is contained, following the header. So, so that's, that's pretty much it, in terms of what the, what the format is against, you know, I don't think this is the right place to go and read through every line, but, but there is quite a lot of, as I say, definitions, so feedback and, will be welcomed, in the repo that, that EIP for false dash prodo repo, the first link, there's a tool that can take input our LP and convert it to this SSE format and vice versa and, and print out hash routes and into, you know, a bunch of basic manipulation of this format. 
* Yeah, one, one caveat here is, I said it converts to, and from RLP that is RLP given that this SSE format encodes receipts as well, regular RLP exports are these, the one that I know the best are the ones from gap, they don't have receipts. So, I had a branch on get that in, through the receipts in the RLP export, that that's just a, that was a short-lived branch. so the, so you can't use those RFPs directly, but you can, as a switch and this tool to do non receipts and, and then that will work, separately, there's a PR going up on guests or that's up on gas. I think it's still in draft form that adds this together. so, you know, we'll see if it gets in, but I think there was some interest in that. 
* So ideally we'll get to a point where you'll be able to export this SSE directly from GAF, and then not tool that I just mentioned. That was my prototyping tool will still be useful for like examining files and maybe still converting them and stuff like that. But, you won't have to go through like all the gymnastics to export from geth. so yeah, that's roughly the current status. 
* I think that the next steps, well, of course getting feedback, the next steps, if I'm continuing down this path are going to be well, actually doing a full export on, on Goerli. And, and then since we have the soon, hopefully being able to see what that would look like and potentially reimport it, into a fresh node posts, post early  merge, the PR is up on geth. And, and yeah, if, you know, if there's agreement and consensus on this, then, then we'll start looking at the distribution mechanisms for these files, I guess I, should've just given a bit of context. So the idea here is, you know, if you talk about the full export of main net up to the merge, that's a pretty, it was in the 300 ish gigabytes, if I'm uncompressed, if I remembering correctly now, and so compress, maybe it's a two X, but that's, you know, that's going to be a fairly large number of files. we'll have to find out, well, there'll be, we'll want to have multiple places to host them, distribute them, and then one place to host the hash road for all of this data. but that's, you know, that'll come a little later. So, so yeah, I think that's roughly everything I wanted to, to go over on this. Again, two links to their feedback, very welcome on the repo or in, in the discord, or, and there's a history, expiry channel in the Eth R and D discord, which we can use for discussions related to this. and, and yeah, that, that's pretty much it. Any questions, comments, thoughts. 

**Micah Zoltu**
* So you, mentioned that this is the shape of these things are brought mostly over from the beacon blocks with a few minor modifications. looking at this there's modifications seem to be interspersed throughout it, this SSE not benefit just in terms of modularity and reuse of code from putting all the new stuff on the end. So that way you can just inherit from that you can block it or,

**Hentri DF**
* Good question. I might be missing something with SSD. So you're saying if we, if we put all the, if we had exactly the beacon block struct and we added things at the end, we could inherit. 

**Micah Zoltu**
* Yeah. So like with, with RLP, at least, if you add things to the end, it's much easier to reuse code than if you add things in the middle, just due to the nature of LP. I don't know, SSE well enough to know if that is true there as well. but if, so, it seems like a big win, just so we don't have to have like two different things. You just have one and then the extension. 

**Hentri DF**
* Yeah. I, I'm not aware of that. I'll, don't take a second. Look, I think this might also be implementation specific. I've been using the go fast SSD library, pretty much exclusively. but yeah, I, well, I agree that if we could do that, that'd be great. I'll take a, I'll take a second look to see if I missed something, but I, I don't, I'm not aware of anything like that. I don't think that's possible. 

**Tim Beiko**
* Any other questions? Comments. Okay. Well, yeah, thank you very much, Henry. and yeah, it will be super exciting. I guess, yeah, just maybe my gut feeling is it would be quite valuable to run this full export on Goerli right before the merge, or like right after the merge, whatever on the pre-merge data. And then re-import it on a fresh note after, like, does that generally seem sensible to others as well? 

**Micah Zoltu**
* I feel like at some point we should talk about whether we actually want this and we'll implement it before we go too far down the road. And I think we've, I last, I heard there was not consensus that this is a desired path for you. I'm a fan personally, but I don't want to waste people's time if we can't get consensus. 

**Marius**
* I think we don't have consensus on whether we want to drop the history from the nodes, but I think we have, at least the way I gauge it, we have consensus on that. This is something that's cool to have as a secondary mechanism. 

**Tim Beiko**
* Yeah. And I think it's almost like before we would probably feel comfortable dropping yet fully from the nodes. You want to know that the secondary mechanism works reliably. is that, does that make sense, Marius? 

**Marius**
* Yeah, that's exactly what I at least want to see before I put forward for that. 

**Tim Beiko**
* So I think in that case then, yeah, definitely running the experiments on Goerli and showing you work thing is a, is a really valuable for step. does anyone disagree with that? sweet. so I guess, yeah, that's pretty much it, there were just two quick announcements. first, there's going to be another EIP for it, for, for a breakout call, next Friday at 14 UTC. the agenda is linked, in this agenda, but basically some upgrades, some updates on implementations at the case of GSF and, some of the spec issues, as well. so yeah, if you're interested in that good job there, and then, Alex, you had also something around the, builder spec that you wanted to bring people's attention to. 

**Alex (stokes)**
* Yeah. I just wanted to call it out. This is mainly for cl clients, but in the event that some of your here you are, just please take a look. It was around essentially some kind of embargo that will have on members going through the merger transition itself. we had agreed on a particular strategy in the last cl call. I'd have to do the PR to reflect that. So if everyone could just take a look and then we'll discuss next week. 

**Tim Beiko**
* Cool. Thank you. And that's a PR 38 in the builder spec repo.

**Elopio**
* And question here, which maybe it's better to discuss next week. do you want some action from us? Like, should that relay be offline anyway, within that period approaches or are there some checks that we should do on the relay or should this be local for us by the proposals? 

**Adrian Sutton**
* My gut feel is it would be safer to let the battle later and force it to builders available because it's the battle that happens to depend on the light. It's kind of better for it to be there. but I'm not strong on that. 

**Paul Hauner**
* I would be tempted to lean towards leaving the relay on as well. it's one less thing to forget to turn back on, I guess, but so not strongly held. 

**Elopio**
* All right. well, we help them to figure out the actual process this, I think it's sensible. my ask here is like, come up with crazy ideas, like announcing this, like the first blocks will, have no immediate post really, because there was something that happened, seems very complicated. Like it's not, it's not a big window and it's going to be super hard to coordinate it, to affect it in significant ways. but still it would be good to make just the brainstorming of what could go wrong. Yeah, this makes sense. Thank you, Alex. 

**Tim Beiko**
* Oh, anything else anyone wanted to bring up? 

**Trent**
* Yeah, I can jump in My audio. Okay. yeah, just really quick. every two weeks we've been running the, an open KCCG ceremony call, for th there's the fourth call. So it's been a little over a month or two. yeah, this is the we're setting the stage for prototyping sharding, but in order to do that, we need to, design and implement this trusted setup ceremony. People are familiar with that. That's, made famous by Z cash and many other projects, to speak coordinated ceremony, to generate a number. And then the number is inputted into the protocol. So, and then prototyping starting would make use of that number, the cryptographic construction. So we're working on that. as in parallel with all the merge efforts, kind of like what Henry is doing with, for four. So if anybody is interested in engaging with this, learning more about it, we, like I said, we run regular calls and, anybody's welcome to join and we hope to see many people creating their own implementations. so if this is something that sounds interesting to you, please do put the, put the link to the latest call and that will maybe direct you to more interesting things. the specs repo is also linked there as well, but yeah, just sharing that. We just had our fourth call this morning a few hours ago, and then it'll be again in two weeks, if you want to join the next one. 

**Tim Beiko**
* And there is Pari, do you want to give some context on that? yeah. 

**Pari**
* I don't really have more context than one of them for like half an hour. we was still figuring out what's happening there and think the Nethermind team, I told me some had to be on some of the other issues. 

**Marek**
* I think one, one of the reminder self healed itself too, but, still analyzing Greek west from others. 

**Tim Beiko**
* Nice. That's really pretty good to see anything else before we wrap up. Okay. Well, thanks everyone. We'll see you in two weeks. August 4th, again on a Thursday. yeah, have a nice rest of your week. Bye Bye. We can start the weekend. No, right. Okay. 
* All right. Have a nice day. 


  ## Attendees:
- Tim Beiko
- Danny
- Andrew Ashikhmin
- Ansgar Dietrichs
- Martin Holst Swende
- Barnabe
- Daniel Lehrner
- Fabio Di Fabio
- Fredrik
- George Kadianakis
- Giuliorebuffo
- Jose
- Karim T.
- Lightclient
- Marek Moraczynski
- MariusVanDerWijden
- Micah Zoltu
- Mikhail Kalinin
- Pooja R.
- Peter Szilagyi
- Trenton Van Epps
- Tomasz Stanczak
- Somu Bhargava
- Lukasz Rozmej
- Pawel Bylica
- Dankrad Feist
- Sam Wilson
- Alex Stokes
- Justin Florentine
- SasaWebUp

---------------------------------------
## Zoom chat
Zuerlein:	no LVH on the agenda?  
Ben Edgington:	gm  
lightclient:	🤝  
Tim Beiko:	gm ben!  
stokes:	gm  
lightclient:	gm  
Tim Beiko:	https://studio.youtube.com/video/N80PgxELDYg/livestreaming  
Tim Beiko:	https://youtu.be/N80PgxELDYg  
Trent:	not hearing sound  
stokes:	no sound on thursdays  
stokes:	i just hear intro music  
elopio:	cancel and come back tomorrow? :)  
Pooja Ranjan:	intro yes  
Gary Schulte:	have music also  
Tim Beiko:	https://github.com/ethereum/pm/issues/572  
Micah Zoltu:	Just freestyle it Marius.  
danny:	and do it for ~mid august  
Paul Hauner:	What is the “mergeNetsplitBlocks”?  
danny:	a p2p segmentation thing  
danny:	and only on the p2p. doesn’t affect state transition or anything  
Paul Hauner:	Got it, thanks 🙏  
Mikhail Kalinin:	and only on EL  
MariusVanDerWijden:	CI is red, so I can't push the button even with approval (it also has no approval yet)  
Paul Hauner:	Lighthouse will do a release tomorrow with Goerli merge params that will be suitable for the merge. Then, we will do another release late next week with a few more issues/PRs we’re still working on.  
Adrian Sutton:	Teku 22.7.0 came out today with the Görli merge params included.  
danny:	unless you run an exchange or something.  
danny:	those have economic penalties  
Micah Zoltu:	Or MEV searcher.Or Payment Processor.Or Dapp Operator.  
Micah Zoltu:	Too many classes of users, we should get rid of some.  
Micah Zoltu:	Moral of the story, don't run Prysm everyone.  😁  
Gary Schulte:	or rather don't everyone run prysm  
Micah Zoltu:	👆  
elopio:	wooo  
Micah Zoltu:	I think we'll get more success if we just say "Everyone, don't run Prysm" because like 10% of people actually listen to us.  😖  
MariusVanDerWijden:	"Our main priority is not to break the blockchain" Same brother, same  
Tim Beiko:	amen  
danny:	all sounds good  
Tim Beiko:	https://github.com/flashbots/mev-boost/issues/222  
Tim Beiko:	Issue mentioned  
Tim Beiko:	https://github.com/henridf/eip44s-proto/issues/1  
Tim Beiko:	https://github.com/henridf/EIPs/blob/eip-premerge-oob/EIPS/eip-premerge-oob.md  
lightclient:	nice work Henri!  
danny:	thanks!  
Tim Beiko:	https://github.com/ethereum/builder-specs/pull/38  
lightclient:	link master  
Trent:	latest KZG Ceremony call: https://github.com/ethereum/pm/issues/569  
danny:	participation still climbing on gsf5. intervention or self healing?  
Parithosh Jayanthi:	teku-erigon was self healing  
danny:	cool  
Parithosh Jayanthi:	it just decided to come back online..  
Tomasz Stańczak:	thanks! forwarded to Nethermind crypto research team Trent  
Trent:	we had Alexey from your team join today actually =)  
danny:	shortest ACD in a long time  
Trent:	v quicj  
Gary Schulte:	wat?  thursday calls are SHORT!  
elopio:	:applause:  
lightclient:	cheers  
Parithosh Jayanthi:	another advantage  


---------------------------------------

## Next meeting on: August 4, 2022, 14:00 UTC
[Agenda](https://github.com/ethereum/pm/issues/583)



