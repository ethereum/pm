# All Core Devs Meeting 137

### Meeting Date/Time: April 29, 2022, 14:00 UTC
### Duration: 90 minutes
### [Agenda](https://github.com/ethereum/pm/issues/514)
### [Recording](https://youtu.be/SWWoniO6rZc)
### Moderator: Tim Beiko
### Notes: George Hervey

## Decision Items

| Decision Item | Description | Video Ref |
| -------- | -------- | -------- |
| 137.1     | Keep running Goerli shadow forks because of one unknown issue. | [31:11](https://youtu.be/SWWoniO6rZc?t=1871) |
| 137.2     | Focus on weird edge cases rather than automating more shadow forks due to limited manpower. | [33:49](https://youtu.be/SWWoniO6rZc?t=2029) |
| 137.3     | Have proposers target block gas limits rather than builders. | [48:15](https://youtu.be/SWWoniO6rZc?t=2895) |


## Merge Updates

**Tim Beiko**: Hey everyone. Sorry, I joined at such last minute. Let's set us up. And okay. Let me share the agenda in the chat room here. Wow bad morning from Micah. Good.

Micah Zoltu: morning works too.

Tim Beiko: bad morning is really good. You can tell after less than a week you'd be back on. Twitter it's already started affecting your brain.

Micah Zoltu: Oh man, it took me like him first day I got like seven or eight replies that were out of like 10 that were just like people just hating on me just like you know attacking my character and a great welcome back. Wow that's right, I remember this is like how.

Tim Beiko: Who would dare to do that on Twitter.

Micah Zoltu: That's right.

Tim Beiko: No one who wants a EIP group.

Micah Zoltu: problem is I have everybody knows I have such a strong stance of non discrimination that i'll probably still approve their EIP is even after the call me names on Twitter.

Tim Beiko: Okay, we're almost ready here it's probably gonna be the shortest AllCoreDevs intro on YouTube and it's actually already streaming or it's me, yes, so.

Péter Szilágyi: The thinking you're going to say is going to be the shortest AllCoreDevs meeting and was getting my hopes up.

Tim Beiko: Hahaha no. I remember a few years ago, there was like 30 minutes one. And I think that was that was the best over there. Unfortunately, not today. Let me move this over.

Micah Zoltu: that's some foreshadowing right there.

### Shadow Fork Updates

Tim Beiko: So Rachel research theory. Micah with the comments. Welcome everyone to AllCoreDevs number 137 today. So i've posted the agenda in the chat. We have a bunch of merge related updates and frankly that's probably all we have time for um yeah. And yeah I guess you know to kick us off. Do we have Pari here, yes Okay, so we have Pari. Pari do you want to walk us through like the two shadow forks that happened last week and we're yeah what will happen there?

pari: So we had two shadow forks last week when during DevConnect. The first one was a Goerli shadow fork. Goerli shadow fork four, and this was, I think the first shadow fork where we had multiple clients staking on. And I think everyone made it through the transition, but Besu and Aragon post transition had issues and stop working, but during the week the teams pushed a bunch of fixes and we had mainnet shadow fork two on Saturday so that's about six days ago. And mainnet shadow fork two was like it worked a lot better we didn't have any major issues it's in that all clients take hold through the transition and also well after.

We did uncover a couple of issues with deposit processing and we were looking at more ways on how we can harden that. We didn't have an issue with late blocks being proposed by prism there was a fixed push like relatively soon after it was discovered and the net has been quite good, since then. The other issues, we found through the week was some proposal related in compatibility between Nimbus-Nethermind that's been fixed, now we had one, I think we had two issues with Besu-Prism. But I think that's also been fixed right now and Aragon-Prism is to undergoing triage. I don't think we know what's going on there yet, but there are other Aeragon nodes about in sync so. It could just be some incompatibility, we have to figure out. But, in general, the network is stable I think we're looking at like 96 ish percent participation and we're hunting down the rest.

Tim Beiko: Awesome. Thanks for sharing. Anyone from any of the client teams want to add some comment there?

Andrew Ashikhmin: Yes, i'd like to add that occasionally I hear reports of Aragon nodes being stuck, especially when people try to sync mainnet shadow for some some time afterwards, so I have to investigate the sync stock issue and also like fixing hive tests it's something on my plate so still a lot of things to fix in Aragon for the merge.

Tim Beiko: Got it. Any other client team?

Péter Szilágyi: Yes. I have one i've been discussing with. A bit with Barry after the shadow fork. And I guess, this also ties into this Aragon comment just before, that as so the shadow forks are kind of nice to test the transition. They always testing it with perfect clients so to say. Mainly all the clients both the beacon clients and the execution clients are in sync so everybody's just going in lockstep and waiting for the thing to it. And I mean was that is nice, I think it would be also interesting to somehow create some tests where separate client combinations are out of sync or of wack essentially, and so I probably setting this up would be quite messy or complicated. Maybe some API endpoints would be needed to actually test this scenarios will be super nice if we could have, for example, some nodes that are let's say the Beacon client is in sync but the execution client is just syncing, whether that's initial snaps in or just behind a few blocks and doing forcing. And it would be nice to have the other way around, where the execution client is actually following the tdd but or start following the chain progression, but the beacon client is out of sync. And the reason we're kind of seeing is that I assume that people will try to re-sync around the merge and it would be nice to at least confirm that kind of works Okay, even if there's quirks here and there.

Tim Beiko: Is there yeah I can imagine how setting that up automatically would be tricky but is there a way that we can maybe have client teams like manually test out on one of the shadow forks?

Péter Szilágyi: I guess the problem here is how do you. So manual testing it out is probably that's not reproducible. So. Nothing goes wrong, you have no idea what happened. And I don't know. so at least speaking from Geth's perspective, we have a API call at set HEAD. So what we could do is right before TDD hits maybe just set the head back I don't know 60 blocks, or something and see what happens. I don't know if something like that is available on on the compliance, but I think it would be nice to be able to some even if not a very exhaustive list of corner case checking at least some some basics, because the problem is that. So what we did test with the shadow forks is that the whole thing can just transition through it and that the conditioning is just the beacon client is feeding execution clients blocks one by one.

But if let's say your node is offline for, for whatever reason you just install geth because it wasn't ready for the merge, and you restart it. And all of a sudden and nothing works, because there's some synchronization issue then it's going it's going to get messy because eventually all nodes will. It will happen that you miss a block, for whatever reason, and then you need to actually fall back to proper sync and that needs to be tested.

Tim Beiko: got it um. Anyone on the testing side have any comments?

Tim Beiko: I think we...

Tim Beiko: yeah.

Tim Beiko: Oh okay so Marius has done some manual test for sstopping and resyncing geth nodes. You want to take a minute, maybe to walk through which which you did?

Tim Beiko: You have audio. yeah.

Marius: Sorry. I might have caught something in Amsterdam. I did a bunch of tests were stopped the beacon nodes so to geth so the execution layer nodes would just stand there and not be fed any new blocks and then restarted the beacon nodes, so that the beacon nodes sync up and feed us the blocks one by one.

Marius: I also wanted to do a bunch of tests, where we did it one or the other databases.

Marius: So I have a synced node, deleted the consensus layer database,  resynced the consensus layer with the execution layer running and the other way around.

Marius: But those, I haven't done those yet and it's not that easy to.

Marius: Well, you can like pretty easily register for it.

Marius: But, yeah I think you need some manual like looking at, to see if it actually works.

Marius: that's it. Oh, I also did a bunch of setup tests of the mainnet shadow fork two.

Marius: Where I set HEAD a couple of Blocks prior also a couple blocks before the merge so once the merge to happen, I set HEAD on the geth node before the merge and that went super, synced up fine.

Tim Beiko: awesome.

Tim Beiko: Peter just to make sure I understand exactly what you're saying is like you want to make sure that we can have kind of these imperfect clients like.

Tim Beiko: All unsynced states, when the merge is happening right like the fear is not that like after the merge they can't get into sync but it's like as we're actually going from TDD to finalizing on the other side, that's when we want to at least see what happens with with clients. Is that right?

Péter Szilágyi: On my Geth nodes here during the transition is... so transition, some of our clients handle the transition code and yet there's quite a lot going on.

Péter Szilágyi: Because there was a up until the point you could just use legacy sync to sync up until the tdd, then if you reach the tdd, then you need to wait for a beacon clients to do pop up if there's nobody listening.

Péter Szilágyi: This is a bit different for full sync than snap sync, so there are these weird scenarios that we try, I mean I tested them quite a lot on on the various testnet, so we do try to extensively test it.

Péter Szilágyi: And just saying that I don't know if other clients did some the tests around these issues and it might be worthwhile to make sure that it's there are kind of okay with these hiccups.

Tim Beiko: Right. Yeah i'm curious to hear from other teams if anyone has anything they want to share.

Marek Moraczyński: So for us it's like we are still a bit working on these cases.

Marek Moraczyński: And we are our have some problems so.

Marek Moraczyński: We need to test it on the kiln and shadow forks.

Tim Beiko: Got it.

Tim Beiko: Anyone else?

Tim Beiko: Okay um and then i'm curiously how... 

Tim Beiko: is it a possibility to also kind of tell people that they should have a synced node when the actual merge happens and, if not basically sync it on the other side, or something like that, like where.

Tim Beiko: yeah if you know, like I think if they're in in step and sync like pre merge, they should obviously be fine, but then, and then, if they sync once the merge happened, they should obviously be fine there as well, but like.

Tim Beiko: yeah it's.

Tim Beiko: Is it like also possible to just tell people like you know you can...

danny: An announcement blog posts and stuff we would definitely recommend people are synced but you know someone will be syncing during the merge.

Tim Beiko: Right, yes, yes, but as soon as the difference if it's like 1% the validators or 35%, right?

danny: Yeah absolutely. I mean we generally assume that most validators are in sync and if you had 35% out of sync you wouldn't finalize much you know that's fine, but then they have to get up and sync.

Mikhail Kalinin: Yeah just wanted to echo what Danny just said, to those who are syncing probably not that important during the transition what's what's more important is that clients, will be able to sync up after the transition is finalized like from scratch, or from like different peers.

Martin Holst Swende: One thing that might be worth highlighting. So previously, it was fully possible to sync up your geth node or Nethermind node without touching your validator and without them communicating.

Martin Holst Swende: Post merge lives can be more problematic right.

danny: What do you mean?

Martin Holst Swende: I mean that we don't see the head. So for example, if you tried to start Geth without the validator, Geth will...

danny: yeah without the beacon node is what you mean.

Martin Holst Swende: yeah yeah it cannot reasonably sync to the head.

Martin Holst Swende: Is I don't know if it would try to latch on the latest proof of work block or something, but then it wouldn't be possible to obtain state from anywhere.

Péter Szilágyi: And that is what it does so, it will try to sync up onto the TDD enforcing it will just stop at the TDD and just print the warning that...

Martin Holst Swende: kind of very what i'm putting my node, people don't use those.

Péter Szilágyi: Yeah and with snap sync, it will track to I mean the chain itself will be sync up on the TDD which ones will stop and for the state, it will just try to sync the head, which will be the latest head will be TDD or something.

Péter Szilágyi: So that will go to the big screen So if you try to sync at that point, somebody actually feeds you some stale data, because they are also stuck on the TDD.

Péter Szilágyi: Then you will end up syncing to some weird state and, at which point healing even if you attach a beacon client healing will take forever because we just fall back to the classical.

Martin Holst Swende: yeah.

Martin Holst Swende: yeah and you might actually kind of wind up in a worse situation than if you just synced.

Martin Holst Swende: Because they would have just stuck entire sync over snap sync, so we should whenever we issue some documentation about this, the syncing and merge we try to highlight.

Martin Holst Swende: Because I guess the same thing that needs needs to be true for other clients as well, presumably that.

Martin Holst Swende: yeah and it needs to get on with beacon.

Tim Beiko: yeah and the kiln blog post already highlighted that like basically if you run a node post merge, you are running two pieces of software right like the consensus layer and the execution layer.

Tim Beiko: And I think we're gonna yeah and the first like testnet announcement posts are going to try and even expand that more to you know yeah just for stakers, for non-stakers, for people who are running a node on the execution later today.

Tim Beiko: So that it's very clear what what they need to do.

Tim Beiko: Because yeah if you're if you're running kind of just geth without a consensus layer post merged and kind of not running the full Ethereum chain.

danny: there's also the ability to surface warnings and errors to the user, because exchange transition configuration would not be happening so you wouldn't be getting any paying essentially on the engine API.

danny: That also.

danny: yeah I mean you could do a lot of that information, but at the bare minimum could expose some big warning to users.

Micah Zoltu: I feel like it should be more than a warning. I feel like the client should not try to sync in that scenario. Like if the execution client knows that we're in post merge, it should just say, "hey, I don't have a beacon client. I can't sync."

danny: Oh yeah.

danny: You might not know it's post merge, it might just know that it's been released as a merge client.

Micah Zoltu: Well, but it knows the ttd has been hit, right? Because it's going to talk to the network and see TTD blocks.

Micah Zoltu: And then it'll know, "hey I know that we're, at least at ttd. Like maybe we're at ttd exactly." But...

Péter Szilágyi: You cannot verify that the TTD until you actually reach the point, so I cannot feed you hey here's the TTD you already passed it and I will just get started, because it think that we're at network merge.

Péter Szilágyi: seeing this thing up onto TTD would be able to realize that whether you want to get TTD to it.

Micah Zoltu: So that's for if you're doing a traditional sync. If you're doing like snaps sync how does that work?

Péter Szilágyi: exactly the same way, you need to validate the proof of work up from one TTD to the other. Otherwise it's not trusted.

Martin Holst Swende: I mean the blocks in the headers up to TTD, those are still valuable so that's that's kind of fine.

Péter Szilágyi: So one one thing I wanted to propose, we have it open as a PR in geth for a month now, we just haven't merged it because I wanted to talk it over in an ACD is that.

Péter Szilágyi: And we've been discussing that after the merge clients would release we would make a new release in which it is actually marked at this network transition essentially just come field in the in the genesis spec.

Péter Szilágyi: And that would be super helpful exactly to circumvent this scenario from causing troubles long term, because we can say that okay,

Péter Szilágyi: there was on field, which was the ttd, but we can also add a second field is no total terminal difficult to reach the boolean or whatever,

Péter Szilágyi: which actually signals that the network has already successfully merged, and from that point onward the execution of client can very well at genesis block say,

Péter Szilágyi: "Yes, I seen blocks in the network i'm not going to touch anything until I have beacon client that's giving me something meaningful."

Péter Szilágyi: And I think that's the long term solution.

Micah Zoltu: Is there a reason we can't include that in the before merge release? Like is there a reason that people should be able to run a proof of like the latest release that we put out right before the merge without a beacon client?

Péter Szilágyi: This flag essentially disables from sync. You will not be processing blocks from that point.

Tim Beiko: But maybe Micah what one thing is there might be a world where like some peers don't upgrade their clients like pre merge, and we just lose them, so I don't know how much it affects things yeah.

Micah Zoltu: I assume that we'd still be able to communicate and like you'd still be able to communicate with people who haven't upgraded up until the merge.

Tim Beiko: Right.

Micah Zoltu: Right so its not until the merge actually happens, you lose communication, and so, if if you're running a merged client and the merge has not happened yet, 

Micah Zoltu: It feels like i'm sure i'm missing something everyone but it feels like we should just say hey if you don't have beacon client at that point, your execution client will start like.

Micah Zoltu: It feels like I can't think of a good reason why we would want execution clients to start up without a consensus client paired with them once they're running a merged client.

danny: I do think that that's not totally unreasonable, I mean there's two options here one is you do huge warning, the other is you say this looks bad you need to actually make sure there's other things synced i'm not going to do anything until you do so.

Micah Zoltu: Right.

Péter Szilágyi: That seems like a very surprising way to lose half of the network.

Péter Szilágyi: that nobody accepts that they need to have a beacon client up onto the merge, and all of a sudden, a month earlier half the network stops.

danny: Well, this is only people that have been when they run the like Geth that is released for the merge, and so they're either gonna fall off if they don't run the other side, these are going to fall off a month before the merge, and hopefully fix it or they're gonna fall off after merge.

Péter Szilágyi: Well yeah but I mean.

Péter Szilágyi: If you have a merge upgrade and the make sure the communication works, whereas if I.

Péter Szilágyi: add this featuring a lot of sudden, it's not about making sure you have correct setup at the merge, rather you need to make sure that you have the correct set up at exactly the point of upgrade of Geth, but since you haven't updated Geth, you don't even know what that is yet.

Micah Zoltu: I see your concern here, if I understand correctly, is that a user who upgrades to their their geth, you want them to be able to upgrade and have downtime of like you know, a minute, however long it takes them to upgrade and then they can iterate on.

Micah Zoltu: Connecting to a beacon client yada yada yada and they have a month to do that, whereas if Geth refused to start without a beacon client, then when they go to upgrade they're offline, for you know, a week, while they figure out how do I run a consensus client.

Péter Szilágyi: yeah that'd be my main concern when using that during the merge.

Tim Beiko: Wouldn't that be kind of good, though? Because, like, I mean they can still run the old version of Geth, you know, like they're offline in that like they're not online on the new version but isn't it good if we have clients who are not like all messed up on the network, because they struggle to set it up and if there instead kind of forced to do that than stay on the old version until they figure it out.

Micah Zoltu: I think if you want be careful that the execution client does not do any sort of like database upgrades or anything like that internally.

Micah Zoltu: until after it has established communication properly because, so you can downgrade basically makes.

Micah Zoltu: If you want to do that, you have to make sure that the downgrade path is very, very clean.

Micah Zoltu: like this, so people will you know upgrade to the latest version and then find oh I needed ta consensus client to make this work, and so, then they go to downgrade you want to make sure that downgrade works very, very well.

Micah Zoltu: Which there could be other individual clients that may be easier or maybe hard on design I don't know.

Péter Szilágyi: Someone issue that.

Péter Szilágyi: I don't think it's always super clear as what the downward path is, for example, if you're installing why you want to deviate and there's essentially no downgrade path you're just it is just up so that might be a problem in with docker. If you're just using you're just putting the latest stable than again in some army to start poking around your deploy scripts which may or may not be a problem.

Péter Szilágyi: Ideally you're running a production setup it shouldn't be a problem, but hey. So.

Péter Szilágyi: Plus, though, the other potential question is that, how do you even tell the user that geth is out. Like telling that you need to do something, for example, if I just get with users to start.

Péter Szilágyi: Maybe just go into some boot loop were some key opportunities manager keeps trying to start it and we keep refusing to start so Somebody needs to somehow dig up a log.

Péter Szilágyi: It where you have a downtime of I don't know half an hour into our system and actually figured out what's wrong with it. I don't know it just seemed a lot of things go wrong.

Sam Wilson: I don't think many people automatically upgrade Geth, so I think if somebody knows like is manually upgrading Geth then they're going to notice if it isn't starting right away.

danny: I guess the counter to that is if it starts and it just works and they don't look the logs which are warning them that they're beacon nodes not synced then they're going to fail the merge.

danny: But, again, I think that this can be left to clients, it seems like a user you know user experience decision that each client can make.

Tim Beiko: yeah and on the communication side like we will kind of communicate loudly and already have started that you need to run both parts, I think this is probably the most anticipated upgrade in Ethereum. Like no one who is running like an infrastructure level production of nodes like does not know that the merge is happening.

Tim Beiko: So yeah, I think, as long as like it's it's clearly explained like in clients like what what the behavior is and that we clearly explain in the announcements like what is required of different stakeholders and like how you know how should we set up their infrastructure and.

Tim Beiko: yeah it seems unlikely that like you know, most people are a large part of infrastructure will do this wrong like there will be someone somewhere who messes this up.

Tim Beiko: Like we see every single network upgrade, but I think you know, the vast majority should be very well aware that this is happening, and as long as we have good communication, they should be able to set up.

Tim Beiko: And Mikhail to deliver a bunch of miners who messed up London and yeah I spent a couple days after London reaching out to the people who had messed it up, so there will be some but that's that's expected every time.

Péter Szilágyi: So, I know it's amazing that this approach is opening up with a bit of can of worms I mean every client is has their own cross to bear, but.

Péter Szilágyi: One issue that I can see, it is that let's suppose you do have a proper setup already you do have the big inclined, you do have.

Péter Szilágyi: Geth properly upgraded and then you just want to restart your system and.

Péter Szilágyi: While you're Geth noticed started off faster than the beacon client and boom it just says refusing to start because there's no beacon client yeah because it's just starting.

Péter Szilágyi: Or what happens if the beacon client just drops off because we update to restart it now, I think it can be, I mean depends on how how aggressive this mechanism is, but you can end up with weird scenarios.

Péter Szilágyi: Even after the merge, for example.

Péter Szilágyi: I think it's a bit dangerous to refuse the startup because something that should be there isn't yet there, for whatever reason.

Tim Beiko: Got it.

Tim Beiko: And yeah earlier on in the chat Pari said he can try and manually set up some of these like out of sync instance, so we can actually you know run a bunch of of manual tests, on them at least.

Tim Beiko: Yeah i'll be on that is there anything else people feel we should be doing.

Tim Beiko: and, obviously, having all the client teams kind of test their own software.

Tim Beiko: You know and and the various combinations of other clients and making sure that they walk through the edge cases.

Tim Beiko: But beyond that I'm not sure what else we can do.

Marius: So in Amsterdam, we discussed a lot.

Marius: about some testing tools that we need, or that we could implement.

Marius: and see now from the Geth team has already started implementing some of them in geth, but it might be really, really good for other client teams to also implement some of the rpc calls, so that we can at least make debugging issues if they may arise way easier.

Tim Beiko: Is there yeah that sounds pretty reasonable, is there a PR or like expect somewhere where of what's they're implementing?

Marius: I think we have an issue to collect all of these things and i'm going to find it at Lincoln.

Tim Beiko: Thanks.

Tim Beiko: Any other thoughts comments on this?

Tim Beiko: Any other thoughts on just the shadow forks in general?

Tim Beiko: Okay, and there is another shadow for Goerli plan for this Thursday that's correct?

pari: Yep, exactly next shadow fork is next Thursday. My nodes are already thinking, I just have to upload the conflicts to github and as channeling soon.

Tim Beiko: Okay.

Marius: Sorry, is that mainnet shadow fork?

pari: yeah that's main net shadow fork.

Marius: Okay, good.

pari: Actually that's a good question does anyone see value in Goerli shadow forks anymore? Or do we just keep the last couple around and just do main net shadow forks?

Marius: I think.

Marius: If we were to like if we were to automate a process somewhere.

Marius: Like a bit more than we could have gone, forks every like two days or three days.

Marius: I would, I would see value in that otherwise if we're going to only manually do shadow forks I don't see see the value in doing to Goerli shadow forks.

pari: Okay sounds good.

pari: And another thing is that, like to deprecate mainnet shadow fork one and we keep mainnet shadow fork two around, so the one that happened last week.

pari: Unless someone's testing anything on one. If not, I'd like to deprecate it later today.

Tim Beiko: Okay. No objections.

Tim Beiko: Anything else on shadow folks generally? Okay.

Marius: Oh umm because Jamie just just wrote and we had we saw one issue that we only saw on the Goerli shadow fork.

Marius: So.

Marius: yeah I have to think about if it might make sense to have another one or two Goerli shadow forks.

danny: Was there what was particular about Goerli that made this thing happen?

Marius: Probably... we don't really know yet.

danny: I see.

Tim Beiko: Okay, so if we can automate them, we definitely should try and have them running regularly and and then yeah we can do the mainnet one this Thursday.

Tim Beiko: Last call for shadow forks.

pari: One more point on the automation front. When we were talking in Amsterdam Lewis, so the automation for shadow forks could easily fit into ketosis.

pari: But when we were talking about it and Amsterdam, we said that we'd rather use the Dev time allocated to current process for testing like weirder edge cases, for example, pausing docker containers around transition or i'm not sure we have to figure out what other weird cases we want to toss in there.

pari: Do we still want to go down that route, or do we want to focus dev efforts on having Goerli shadow fork in kertosis. I don't think we have enough manpower to do both.

Marius: I think the the weird stuff is more important than then having just like more often shadow forks.

pari: Okay. Sounds good.

Marius: Maybe someone else could take over and do it in parallel.

Marius: I don't know if we can onboard someone into ketosis.

pari: yeah.

pari: I think the ketosis team itself is willing to help us with this, but they just have enough manpower for one of the two. I don't think they have enough for both.

pari: But yeah maybe someone from us, I can do the other one.

pari: And i'd also be more on the side of having weird edge cases in ketosis mainly because we're doing so many shadow folks regularly that it might not bring us too much to have it in the ci.

Tim Beiko: yeah we, I mean.

danny: Structured weirdness you know the shadow forks live are supposed to try to find weirdness but anytime we can structure and make sure we hit the weirdness over and over again, is very good.

### lastestValidHash issues

Tim Beiko: Okay. Next thing we had, on the last call we discuss kind of the latest valid hash issues.

Tim Beiko: Mikhail, I know there's been like a lot of conversations about that, over the past two weeks, you want to just give us a quick recap of where we ended with that?

Mikhail Kalinin: yeah in Amsterdam, we had decided that the engine API spec stays the same and you know client will just adhere to the spec. Also will cover this with the tests so yeah basically that's it.

Mikhail Kalinin: It means that the EL will respond with the most recent valid transaction hash in case if invalid block is found on the chain which EL is syncing with until it may use this information to remove invalid sub chain from its Block tree.

Mikhail Kalinin: So that's basically it.

Tim Beiko: Okay got it and first off, anyone have thoughts or comments on that?

Justin Florentine: yeah hey, this is Besu here. We're currently looking at our latest valid ancestor code and it looks pretty much doable for what Mikhail is talking about, but I could personally use a better definition of what the latest valid block is real quick. Our understanding right now is that it is the common ancestor that has been validated as it's been considered valid. Is that the simplest definition we've come up with?

danny: Yeah I mean if you have some block you're validating, it's the earliest block in that chain defined by that block that is valid.

Justin Florentine: Got it. Right. I think we're clear on it, thank you.

Tim Beiko: Anyone else have questions comments about that?

### RFC: Engine API response status when merge transition block is INVALID

Tim Beiko: Okay, next up. Mikhail, this morning you also posted another kind of request for comments about an engine API response status. Do you want to go over it?

Mikhail Kalinin: Oh yeah this is related to latest valid hash, and this is a kind of blind spot in the spec currently. So the problem is that if literally the first proof of stake block in the chain is invalid,

Mikhail Kalinin: At what EL should return as a latest valid hash. It may return, like the proof of work block, that is, the current.

Mikhail Kalinin: Of this first proof of stake block, but this information isn't relevant for cl it doesn't have this proof of work block which is basically the terminal for PoW block in block tree. So this request for performance data take a look into this, we may do when we do nothing, with that, but see I will have to stop triggers in their Block tree if they found that there is an empty execution payload in the block, so I would just mean that.

Mikhail Kalinin: This way to relate transition block is invalidated and that's it or we can be more specific about it and more explicit about it, to avoid some edge cases potential which case that so just take a look and comment on this issue.

Mikhail Kalinin: yeah thi is like an engagement for El on CL client developers.

Mikhail Kalinin: it's yeah it's kind of in the middle of...

Tim Beiko: yeah I think he posted this literally yeah five hours ago, so I don't know if anyone's reviewed it already, but if so, put a comment here.

Mikhail Kalinin: yeah.

Justin Florentine: Basically, reviewed it we didn't have any concerns.

Okay.

Tim Beiko: cool so by no concerns, I guess, your mean you're fine with any of the options?

Justin Florentine: Oh right. I think we liked Option 3 but I don't think we have a strong opinion on it.

Mikhail Kalinin: Okay, thank you.

Tim Beiko: Okay anyone else?

Tim Beiko: Okay.

### JSON-RPC: Add finalized, safe and unsafe blocks

Tim Beiko: Next up. This is something that's been open for a while, I just wanted to bring it up because we are getting close to being done with the consensus level changes. We still have some open questions around json rpc and how to go about basically finalized safe and unsafe. I don't want to take too much time on the call to like go over this, but it would be good to get this PR merged in the next couple weeks so that i've clients like can agree on what what we're implementing. and so I don't know. I know like Danny, Mikhail, like the three of you seem to feel the strongest about this. Do you want to kind of take a minute to to share your your thoughts and how we should move this forward?

danny: yeah I mean there's two.

danny: there's two ways to kind of think about what these words mean. One is the algorithm that defined that derived them and the other is like the actual status and state of the the item. I think that developers and people reading the API reading, this would generally think the latter so like if something says unsafe they'll literally think it's unsafe, not that it was derived from an algorithm that is unsafe and I think that.

danny: the problem is, you can have a safe algorithm that also gives you the head and unsafe algorithm that gives you the head and thus, you could have something that you could have unsafe and safe being the same block which I think is very confusing for end users. Thus, I think latest is, I think anchoring on the latter and actually it being like a property of that block is better. So I would say you leave latest. I would say you define safe. And you hope that you get a better algorithm over time and you do finalize.

danny: I think justified is like a nice to have, but it would require a change to the engine API, which I don't think it's valuable enough to do breaking change at this point.

danny: So my argument would be here yeah.

danny: yeah.

Micah Zoltu: I agree with everything Danny said, except for his conclusion.

Micah Zoltu: I think that when a developer asks for unsafe they're not likely to begin asking for unsafe and safe and then comparing the two. They're just saying "the thing I need is whatever is safe, give me that. Or, the thing I need is whatever is unsafe, give me that."

Micah Zoltu: I don't think the user actually cares what they get back, nor do I think they're going to be looking and comparing that to the other options they're just going to.

Micah Zoltu: Like just say hey I need something that's I need something that's safe because i'm doing off like i'm taking this off chain like i'm an exchange or I need something that's unsafe, because I am running a mvp extracting client and I need the latest absolutely I don't care if it's going to go away and get re-org'ed.

danny: yeah but the semantics of.

Tim Beiko: But yeah.

danny: I think latest does represent that very well, and that people understand that when they're using latest today. I know the argument that maybe it's forgotten and should be renamed but I don't know if I want to debate this too much.

Tim Beiko: Okay. I see Peter and Andrew have their hands up. Peter do you want to go first?

Péter Szilágyi: Good question. Where are these things actually used.

Micah Zoltu: json rpc API.

Péter Szilágyi: Yeah, within that.

Tim Beiko: So by latest block.

Micah Zoltu: Block by number for example that's for a block tag.

Péter Szilágyi: So I guess meaning the execution clients should be returning these.

Micah Zoltu: Yeah so as of the merge, we want user should be able to.., or before the march realistically, but as of the merge at least user should be able to do get block by number and pass in safe as a block tag instead of. So currently they can do pending, latest, earliest, and one other, but anyways we want to add finalized and safe to that list of things they can request.

danny: And then the main question is whether you alias and latest unsafe and deprecate latest.

Fredrik: I mean if you do that deprecate latest, I think a lot of applications will break.

danny: Like a deprecation warning. Not to really get rid of it.

Micah Zoltu: It's like in the docs do we say, please don't use this or we say, please use this.

Tim Beiko: And Andrew you had your hand up as well.

Andrew Ashikhmin: um yeah maybe we just call it not answer, but something like bleeding edge, edge of fringe so...

Tim Beiko: latest.

Someone: Latest is not bad.

Tim Beiko: Okay, so I guess yeah this can kind of pick up the rest of the call if we let it and I would rather not.

Tim Beiko: It would be good if, like people who have strong opinions can go on that PR and share them, and it would be even better if, like by the next ACD, we could have some consensus on this and have that PR merged, in one way or another.

Tim Beiko: Because yeah it just feels like at the end of the day, like in the next couple weeks is when clients are going to want to start implementing this just because we're going to want this before we we have releases out for public testnets.

And so I think the most important thing is just for kind of being done with arguing over what the options are, and I have very weak preferences for what, for what the actual outcome should be but just that we should try to wrap this up in the next couple weeks.

Péter Szilágyi: My two cents on that is unless there's a very good reason to change to deprecate tag, and I think that's something that should be just that.

Péter Szilágyi: If, for whatever reason, these two runs on appropriate appropriate and maybe but.

Péter Szilágyi: I don't really see that big of a difference with safe and unsafe. Even on latest is half unsafe, you can have a side, you can have a re-org, block-to-block...

Péter Szilágyi: So it is not like it's safe currently.

Tim Beiko: Right. Yeah I think yeah i've reached out the application and to the developers I think they are aware of that, than like they they're not confused by what it is.

Tim Beiko: um.

### Gas Limit & Block Builders

Tim Beiko: Okay yeah moving on from this um but yeah please comment in in in the the PR. light client you had some comments about basically the block gas limits when we move to a proposer-builder world. Do you want to kind of give some context there?

lightclient: Right so.

lightclient: In today's world, there's these mining pools that have a lot of control over what the gas limit actually is, and we have touted this in some ways as a benefit because if we needed to lower the gas limits quickly due to some situation in the network, we could coordinate with those pools and make that happen.

lightclient: And post merge, the mining pools sort of go away and we have a very similar type of actor, which are these block builders and they will again have this similar power of being able to set what the target limit is and move towards that.

lightclient: I'm trying to understand if we expect to these actors these builders to be you know, to also be good custodians of this power.

lightclient: And if we want to confer that power into this new system, because we have the opportunity, right now, to add some different configuration parameters to the block building the external block building protocols that will be available post merge to make us the individual validators can choose their gas target.

lightclient: And I wanted to ask this here because it feels like a bit of a departure from where we currently set where we can coordinate with a fairly small group of people to change the gas limit, if needed, and if we allow individual validators to choose that I think that increases by maybe an order of magnitude.

lightclient: And so i'm just curious what people's take is.

danny: I mean well, you want to coordinate with that argument.

danny: That argument is just that, like there should be a lever that developers or a small set of people have and that we currently kind of do.

danny: I don't know if having more players have to be involved in this decision is necessarily a bad thing.

danny: I also think that you know validators incentives aren't the same as end users incentives, but I do think that builders incentives diverged even more, and so, putting this inside of builders, you know MEV searchers hands is not a good equilibrium in my opinion.

lightclient: Right and that's currently my opinion, I would like to build it into a system where that's not the case, but I just wanted to see if there was anybody who felt differently about that.

Micah Zoltu: In the various proposals for builder-proposer separation, can we put the block estimate in the proposers hands instead of the builders hands easily or is that we're over the complicated?

Vitalik: I don't see why that would be complicated. Like there's always a level that like there's always some signature that the proposer has to make, and so you can just like add to the I guess little bit into the container not the proposer signs.

danny: So in L1 PBS and you know when there's a larger redesign here, certainly it's it's easier, with the with sort of like stopgap measures where you try to simulate that and an extra outside of.

danny: In the protocol that people are designing with MEV boost it's a little it's certainly more complicated, but it's not impossible and it's not that much more complicated let's say.

Micah Zoltu: Do we trust proposers more than builders?

Vitalik: I would say yes, because, like you can win and dominate the builder auction for a pretty long period of time just by being willing to spend more money than other people, whereas that doing that for proposers is much harder, so yeah like builders like a very mature builder can force this like very easily accessible elections like is more vulnerable than other proposers choosing it.

danny: Right a builder could essentially by the gas limit to increase by just out bidding all of the builders.

Vitalik: yeah exactly like, unlike the censorship case where you have to win every auction, if you're just trying to manipulate the gas limits, you have to win 51% of the auctions.

Micah Zoltu: Right and if you're a good builder otherwise that may not even be that expensive because you're only paying the difference between you and the next best person or the best person.

Micah Zoltu: Yeah okay, I think I personally i'm convinced that we should probably do something.

Micah Zoltu: i'm okay with either just removing the ability for the gas limit to increase or decrease from be a blockers or moving it to proposers i'd be happy to either personally.

Vitalik: moving into proposers would be a significant change that's like way too late for the merge itself at this point right so that would be a Shanghai thing.

danny: You don't need L1 support here.

Vitalik: Oh, I see because you make it like forkchoice.

Tim Beiko: Lightclient you're breaking up.

Tim Beiko: We didn't hear anything.

Vitalik: Oh, but basically the like you could have the validator enforce that by having the validator only accept bids with a particular gas limit, right?

lightclient: Exactly. They targeted at the beginning of some epoch what their target is and the builders are just aware that that during their proposal slot they should build towards that their preferred target.

danny: yeah it's similar there's a registration mechanism to say what you want your fee recipient to be for a validator so essentially be piggybacking on that.

Tim Beiko: yeah it seems like it would be much better if it's under validators control rather than builders and if we can do that as part of MEV boost that seems like a good way to do it now.

lightclient: Okay.

Tim Beiko: yeah.

Tim Beiko: Anyone have a strong counterposition to that?

Micah Zoltu: I do.

Micah Zoltu: So the only the only thing question would be is.

Micah Zoltu: If this turns out to be incredibly difficult to integrate them, because only we're not thinking about here, should we bring this back up for removing this from block headers with the merge, or should we just accept this builders get to control the block and gas limit?

Vitalik: It would really be hard very hard to make any consensus changes at this point right, so the easier thing to do if we decide that we're lazy is to basically add I can add a like one line of rule that just says that proposer is only accept a header if the header contains a gas limit of exactly 30 million.

Vitalik: Right.

Tim Beiko: Right, then you can do that an MEV boost, not even like layer one right.

danny: yeah I mean I think yeah.

danny: I think the likelihood here is it if it is complex than a version of MEV boost can be released at the merge, that does not support it and it can be layered on, and if it is abused in that time frame, a software can be added to to reduce or eliminate the abuse.

Micah Zoltu: Yeah it's fair.

Tim Beiko: cool.

Tim Beiko: Anything else on that?

### Post-Merge testnets

Tim Beiko: Okay, so next thing I had basically two things related to testnets. So first, there was discussion in Amsterdam about like the kind of future of the testnets. There are free posted a comment on the On the agenda which links to it and I don't know did is anyone on the call, who was at that session in person? I wasn't.

Marius: I was there.

Tim Beiko: Yeah. Do you want to give a quick recap, or anything that's like new that came out of there?

Marius: I only attended the first half a session after what I had to go to the should we break up the core dev oligarchy session, which was way more interesting. I think the big takeaway is that no one actually really wants to deprecate the testnets and there are some companies that want to take them over because they have stuff running on them.

Yeah so the current plan, as far as I understood, is to bring Ropsten through the transition, Goerli through the transition into polio through the transition, deprecate Rinkeby at the point of the transition. And maybe transfer the ownership of the Rinkeby validators to some other entity, if they want to keep this testnet. And deprecate Ropsten after the transition probably either before Shanghai or after applying the Shanghai focus on it. That's the TL;DR.

Tim Beiko: Got it. And I guess just from like our perspective. I assume, nothing changes and that we're still happy with just running officially Ropsten, Georli, Somalia through the merge, so if if some other company wants to like maintain Rinkeby and may or may not run it through to merge.

Tim Beiko: You know, they obviously can, but then yeah just in terms of like the data that we want from the assessments, these three are self sufficient and we're happy with that right?

Marius: Yes, exactly, and so to danny's comment, taking them over means that we deprecate them in our software, we don't maintain them in our software anymore, and they can either have their own version of geth or just use an old version where where we still have support for these testnets.

danny: Okay, so still deprecating in a sense, just kind of. Or from our perspective.

Tim Beiko: Deprecated from Geth's perspective, not from the application, who has their testing infrastructure on Rinkeby, right? Yeah.

Marius: users to move over to some testnets where the software that runs the testnets actually runs and get updates and stuff like this and runs with the latest channels.

Tim Beiko: That makes sense.

## Shanghai Planning

Tim Beiko: OK, so I guess yeah The other thing I wanted to talk about testnets is basically how, how do we get from from where we are today to there. So, like we have this shadow fork in DevConnect which was, which was smoother than the ones we've had before. We have another one plan for this week. I guess you know, I guess, I'm curious from different client teams like you know, what do we want to see in terms of like success on shadow forks before we're comfortable like moving to upgrading their public testnets and is there stuff also like outside of the shadow forks themselves that you know we still want to fit the test before you being comfortable moving to the even the first public testnets?

Marius: So for me, seeing a bunch of successful shadow forks is is really good sign. And the only other thing that I would say is The live tests should be at least for a majority of them a pass by every client basis currently not on the half test instance, but I think they're looking into fixing that quickly Geth us only failing two test. And that there's an open issue, whether this is an issue with assumptions of the tests or with Geth. But every goodness, for example, is heading 28 tests and be really important to get all of those tests fixed so that we have good confidence with that.

Tim Beiko: Ah Marek.

Marek Moraczyński: You could should also have doing good balance, of course, and for every client and I just need to cover most of the spec and what is more, maybe fasting because right now correct me mercy on me, Nethermind and Geth that our Nethermind-Geth is working on your fasting infrastructure.

Marius: Yes, Nethermind and Geth was running. Nethermind and Besu had some issues. But I stop the puzzle, I think, and I need to set it up again. And I want to add. Aragon to it and Besu. And and run them on all of them. It's a differential puzzle, so I also find differences between.

Tim Beiko: got it. Anyone else have thoughts here? Andrew yeah.

Andrew Ashikhmin: I have a question why so like the number of tests is different between Aragon and Geth and Nethermind? I think like the total number of tests for for Aragon is 46 for nethermind is 47 and for geth is 54.

Marek Moraczyński: yeah.

Tim Beiko: Okay, so definitely looking in.

Marius: I'm going to look into it.

Tim Beiko: yeah awesome. And then justin had a comment in the chat about like the mid-sync situations being a compelling and if we want to like run something like that and run something like that on on shadow fork. Even though we don't have the infrastructure to do it, is this something that like client teams can manually try on the forge this Thursday and see we might be able to reproduce everything if we find bugs but we might be able to see like does everything break or do things generally work and recover or fail and kind of predictable ways. So I don't know is is it worthwhile to try and get people to manually run those when the shadow fork happens this week.

Justin Florentine: I don't think that should be up too much of a problem for Besu.

Tim Beiko: Then yeah Pari has a comment about two times mainnet shadow forks with no flash pretty minor issues. And i'm curious Pari, like do you think our previous shadow fork was at that level or kind of right on there because we did find these issues, but the deposit processing and stuff?

pari: i'd say it was right under like we're almost there, but it was just not perfect enough.

Tim Beiko: Yeah got it. So obviously you know, we have one scheduled this week we have one scheduled next week or I assume we'll have one scheduled next week. I don't know. Or sorry next week and then two weeks from now, and I assume we can we can we can do those. I guess if we you know if we had those kind of work smoothly and then obviously spent some time on hive in the next two weeks to make sure that that the different teams passed the test and.

Our people you know the people feel like at that point we generally be the good spot to start looking at upgrading test nets and, obviously, you know there's always a delay by the time like we need to set the block and then like put up the software and then like there's a few weeks until we actually get the actual upgrades but um yeah.

Assuming I guess assuming the shadow forks went smoothly and that hype support was there, is it realistic that the think we might start like yep that's that's like two weeks, or do we feel we need like yeah We need much more time than that? And I guess no one wants to answer this.

Martin Holst Swende: I think it sounds reasonable.

Tim Beiko: Thank you, Martin. Awesome um so yeah I think that makes sense. One thing i'll also share from discussions at dev connect is yeah we had some chats about like difficulty bomb and like once you actually make a call about pushing back or not. And if it seems, and this stuff is really hard to estimate, so please don't quote me on this in two months if i'm wrong. But it seems like you know we can probably get to like late May, June-ish before we really feel the impact of it and then, from that point, you know, in the past we've we've managed to like ship difficulty bomb upgrades in weeks when needed.

And so my my feeling from talking with like different client teams at Amsterdam was like it seems like it would be better to like wait you know try to say you know move forward and move to the testnets and so for any through them without necessarily doing anything about the bomb and then, if if we get the late late May, June so like to three calls from now, and we see that, like we're not moving forward on the testnets either because we found some issues or things are slower than expected, we can coordinate a bomb push back pretty quickly, then, but not. Basically, not even thinking about it and being able to move a bit quicker in the short run, would be better on.

Anyone like strongly opposed that?

Thomas Jay Rush: This is Jay rush.

Tim Beiko: hey yeah.

Thomas Jay Rush: hey how you doing?

Tim Beiko: Good yeah you wanna you want to share your screen and walk us through your charts so like i've been using it, I think it's yeah.

Thomas Jay Rush: Well, I was gonna say I think that it would be unfortunate to make a mistake there as far as getting into a situation where you have to force yourself to delay the bomb. I'm sure everybody understands that, but let me just share this one chart and I think you can see pretty clearly from the chart how quickly the bomb goes off once it goes off. So is everybody seeing this?

Tim Beiko: Yeah I can see it, yeah.

Thomas Jay Rush: So I mean we're here. I was concerned last week that it wouldn't show up because the hash rate was higher, but it is starting to show up this is as of now as about an hour ago.

Thomas Jay Rush: So it is starting to show up. These are the last two bombs here and we delayed them in plenty of time for them to actually affect the block time. So here's 14 second blocks.

Thomas Jay Rush: But this one was the one where we've kind of forgot to set it.

Thomas Jay Rush: And we kind of had to react really quickly here, because there was too hard forks right after each other, but I think there were about a month apart.

Thomas Jay Rush: So this is about a month and it just literally drops off the, off the cliff so and here you can see, it just drops off the cliff, and this is exactly what the bomb does.

Thomas Jay Rush: So this red line is June 15 which was when we thought we were setting it back here in December and it looks to me like it's going to.

Thomas Jay Rush: it's getting ready to drop off the cliff to me i'm just looking at this now, I never wanted to predict the future because predicting the future of this thing is hard.

Thomas Jay Rush: But I can see that we're getting to the point where it might start dropping off the cliff so I want to just say that out loud and I want you to be careful, I would rather see you guys at least pick a date to say we are going to make a decision about picking a date.

Thomas Jay Rush: By this date, you know say may 15 we're definitely going to have a decision about whether we're going to delay it or not, because you don't want to get to the place where you're forced to delay it because it went from 18 second blocks to 22 second blocks in a two week period. That's what I would say.

Tim Beiko: Right, did I think yeah I think we probably make that call much before we hit like 18 seconds I think yeah I yeah that's actually pretty low, but I guess, because there is kind of this this chance that we might actually be able to ship the entire upgrade without moving back the bomb. Probably waiting until we're like 14-ish second range maybe 15 to see like how we're feeling about this. And then, and then that means you know, by the time we coordinate it takes, you know, maybe a period or two and we end up like maybe under like 17ish 18 second range, by the time we push it back. yeah um so yeah that's my rough gauge for it, I don't know if that feels reasonable sweater like yeah.

Thomas Jay Rush: yeah I think I think if you set a date by which you're going to set a date, you know you say we're going to make a decision by the third week of May, or something like that.

Tim Beiko: yeah and I think the risk is just a I just don't want to paint us into a corner we're like we're then forced to act if say the bomb is not actually showing up as like you'd expect, so I if if we you know, say, we can get like an extra four weeks without having to make a decision. yeah or an extra six like I think every week where we can delay making that call is is valuable to us because it gives us more information on the readiness of the merge. So I, I guess, the best thing we can try to say is like today we're far enough from the bomb being an impact that you could actually use this conversation to another two weeks, and then and, obviously, it will keep kind of looking at it, but yeah that that would be my preference. Yeah Lucas, I see you have your hands up as well.

Łukasz Rozmej: Just based on this graph I would say that we have four weeks. In four weeks, we should decide if we should move the bomb or not. That looks reasonable for me.

Thomas Jay Rush: yeah so the third or fourth week of May, or something, yes, like.

Tim Beiko: yeah that would be two calls the yeah.

Vitalik: yeah I mean, I think the more difficulty bomb is not a chaotic system right like I you can analyze it mathematically to our scripts that have predicted it pretty pretty accurately and like we do know how it progresses right that's like every hundred thousand blocks, so the difference between the discrepancy between the actual block time and the ideal block time doubles. And that's basically how it just keeps going right so it's. Like it is, it is something that we that we can model, the main unknown variable is basically like hash rate, but even hash rate like it's not an unknown by. Some crazy factor of like more than two or whatever.

Thomas Jay Rush: It is predict it's predictable but it's much easier, just to say. I would argue that I would argue that here it wasn't very well predicted here but. This year, where it recovers, so it goes off and then the hash rate recovers. That that is dependent on the hash rate. But I agree with you it's predictable, I always just predicted the first time that you know when it really starts going off. I'm saying this is where we're going to start seeing it go off by the time we get here.

Vitalik: yeah I mean basically like when it breaks 50 and then it's you know pretty clear that it's 100,000 blocks away from breaking 17 and then another hundred thousand away from breaking 21 and so far. Yeah so it's like there's like it is a kind of multi variable problem because, like you know we all we have to evaluate you know the pain of doing an extra delay hard fork versus the pain of like living with 21 or 25 second blocks for a while, which is you know something that we have done in the world demand so.

Thomas Jay Rush: Right right. And I even I even said to Danny Ryan.

Vitalik: That.

Thomas Jay Rush: You should let it get long just to let the world understand that these things can get bail.

Thomas Jay Rush: me, and I wish to change to the code.

Vitalik: want to make right there you know, ultimately, like this is the last time that the block time is going to be anything other than 12 seconds so yeah i'm just highlighting that kind of these uh these trade offs exists there's and there's like scripts that can help us actually measure exactly what the what the trade off the is but I definitely agree with you, and like new need to make a decision now sort of position my.

Tim Beiko: Micah I think you're next.

Micah Zoltu: So we could instead of trying to project forward why don't we just pick a block time that we consider unreasonable and then as Vitalik mentioned, we can calculate backwards, when we would need to have a you know if we know that it's going to take us three weeks get a really solid and we know we we definitely don't want 30 seconds, and we can calculate at any given point in time, what is three weeks before 30 seconds of trying to calculate forward.

Tim Beiko: I think that's hard, because what block time we're willing to tolerate probably increases as we get closer to the merge.

Micah Zoltu: it's not a very fixed variable?

Tim Beiko: Right, like, I think, for me, maybe, like others, disagree, but for me it's like you know if we have 2o second block times today, I would consider that tolerable. If we have 3o second block times, but then we can ship the merge two weeks later than like that's maybe worth it, you know i'm not saying this, but it's like yeah what we could tolerate the thing goes up as we get closer to the merge.

Micah Zoltu: yeah that's that's fair.

Tim Beiko: Lucas?

Łukasz Rozmej: So, two things one thing we can have this unpredictability enhanced. Our unpredictability based on hash rate leaving so I expect the close close to the merge hash rate would be going down because people will just sell their hardware before anyone else, like before before ours.

And the second thing I would really like the dream to be a reliable be considered reliable network and something that goes from 14 seconds to like 20-25 seconds blocks, or whatever. So I would really like the decision to be, we can make it as late as possible, but not before, not after we are seeing time increases increases, but before that, so I would prefer doing that. 

And third thing, moving difficulty bomb is like easiest hard fork ever, so I don't think it will take a lot of efforts from pushing the merge to move difficulty bomb as very easy thing to do so, those three points for me.

Tim Beiko: And the first one yeah and how how quickly, does the difficulty algorithm readjust the following hash rate basically?

Vitalik: I think like basically close to immediately right because of the it like it can adjust by I think it's like a factor of e in one Charles and the end 24 blocks either attend 24 2048 or something like that so much it does adjust very quickly.

danny: it's not like the big adjustment times.

Tim Beiko: Right, so that means, even if the hash rate goes down. It doesn't make the bomb worse because then overall difficulty for the network goes down.

Vitalik: Well, so like if the hash rate goes down by a factor of two, then we basically lose one whole period until we get the sandbox.

Tim Beiko: Right right. Yeah but that's by a factor of two in like a two week period.

Vitalik: Right. I mean if people wants to open betting polls on how much hash rate will drop before the merge, I mean i'm definitely betting that it will drop by less than a factor of two probably significantly less.

Thomas Jay Rush: This is why I never predicted the future I only predict when it first comes.

Vitalik: Hmm totally.

Thomas Jay Rush: And I think I think I think that the, the world will tell us exactly what it thinks about 2o second blocks very loudly.

Micah Zoltu: Less coming from me before a walk away from this conversation, so I don't care much. Is the anxiety and effort we're putting into having these discussions. Just that alone. Is it worth just pushing back the bomb just we can stop worrying about it? Like this isn't we've spent a very non trivial amount of time and there's a lot of anxiety around it. I would say, maybe value just getting rid of things it and even if we just don't make it, you know in by June just don't have that anxiety along the way, maybe valuable in itself.

Thomas Jay Rush: I would vote yes.

Martin Holst Swende: I probably would too.

Andrew Ashikhmin: yeah I think it makes sense, we can postpone it to whatever like the end of the year doesn't mean that the merge is postponed to the end of the year.

Martin Holst Swende: No. No, it doesn't but, but the thing is yes, as Micah said it's trivial for us make these hard fork such a hard fork was possible. But it's not trivial people to to mean the whole coordinating the update. But it might be easier if we just early on do plan for for bomb update and not to know that the merge at all. Or, as little as possible.

Tim Beiko: So the idea is, if you can, if you can push it back. Yeah if you get pushed back then obviously it's not like a ton of work there's some coordination work, but it does kind of make it smoother and then you have a comment about proof of work.

danny: yeah I mean, We might see some proof of work forks here, but the. If the chain is actively degrading at the time they're performing the work fork they have to do two things at to do an upgrade and convince exchanges to list them. At the same time, whereas it's very easy to do the proof of work fork and if you have months to potentially defuse the bomb and that's months to do potentially damage to users. Obviously i'm very biased in what I consider damage here, but I I think it's actually a good thing for the bomb to be moving kind of inward as the merge.

Martin Holst Swende: Yeah I can see, I can see your point sure. Yeah. I definitely don't think we should like postpone it, for a very long time. I don't really have a strong opinions either way.

Tim Beiko: And yeah I mean we have basically a few minutes to the end of the call. Does it like makes sense, based on just the conversations we had earlier that you know spend the next two weeks, obviously, focused on the shadow forks on hive see how we're feeling two weeks from now, we can see also how the bombs progress than we can you know. I think we do have like much more than two weeks to make this decision and, like the the chain is not being affected today and it's not going to be noticeably affected in like two weeks realistically We probably have maybe be like even like for like that call so like yeah I think.

Yeah it's worth at least like kind of moving forward on the testing seeing how far we feel we are in the process, two weeks from now and looking at it then. And if we choose to remove it or postpone it yeah we can we can do that in two weeks and obviously continue this conversation about like the pros and cons just running like proof of work side in the discord.

We have two minutes anything else people wanted to bring up.

Okay well well finished already, for the first time in a long time, and thanks everyone for coming on. And yeah talk to you all in two weeks.

Micah Zoltu: It was promised a long meeting.

## Chat Highlights

00:06:13	danny:	prater to subsume goerli

00:06:13	danny:	https://prater.beaconcha.in/
00:07:06	Tim Beiko:	https://github.com/ethereum/pm/issues/514
00:11:32	Micah Zoltu:	Core Dev Call 137 Fun Fact: 137 is a prime number.
00:13:50	Marius:	https://www.google.com/search?q=is+137+a+prime&ei=NvFrYt_mNNLTkwWL057oBw&ved=0ahUKEwjf2Y2Lubn3AhXS6aQKHYupB30Q4dUDCA4&uact=5&oq=is+137+a+prime&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIICAAQBxAKEB4yBAgAEA0yCAgAEAgQBxAeMggIABAIEAcQHjoHCAAQRxCwAzoHCAAQsAMQQzoFCAAQkQI6BQgAEIAEOgYIABAKEB46BggAEAgQHjoICAAQBxAFEB5KBAhBGABKBAhGGABQhgVY0Bpg1h9oAXABeACAAXqIAZwDkgEDNC4xmAEAoAEByAEKwAEB&sclient=gws-wiz
00:16:16	Marius:	I did some manual tests for stopping and resyncing geth nodes
00:16:35	Micah Zoltu:	Paste into browser console:
for (let i = 2; i < 138/2; ++i) { if (137/i === Math.round(137/i)) console.log('not prime!') }
00:16:35	danny:	but not *during* the transition
00:20:30	pari:	I’ll add a few more nodes to test CL out of sync/EL out of sync for the next shadow fork, Not sure how to automate it yet - so it’d be relatively manual
00:20:37	pari:	Or scripted rather
00:21:35	Jamie Lokier:	A risk is that nodes in sync just prior to the merge may desync during it just because of the unusual activity.
00:25:45	Trenton Van Epps:	oneClick node from Nethermind if anyone hasn't seen this

https://github.com/NethermindEth/1click
00:25:46	Jamie Lokier:	(As in sudden changes of CPU activity etc resulting in nodes that lose a few blocks and need to recover, and people who set up nodes at the last minute out of necessity, who don’t actually have quite enough resources for it but don’t find out until the transition)
00:29:15	Danno Ferrin:	Won’t the forkID for Paris cause those clients to drop off?
00:29:35	Mikhail Kalinin:	Won’t snap sync be reset once CL starts communicate to EL?
00:32:00	danny:	I see argument either way. I think it’s fine to leave this to each EL to decide for their users
00:32:20	Trenton Van Epps:	martin pls mute
00:32:31	Sam Wilson:	Is there precendent for "I'm aware an upgrade is coming CLI flag"?
00:32:50	Tim Beiko:	—support-dao-fork
00:33:04	Sam Wilson:	So a flag that says "I know the merge is coming, run without a conensus client"
00:36:42	danny:	or geth can wait for `exchangeTransitionConfiguraion` ping
00:37:02	pari:	^ some clients do log `exchangeTransitionConfiguraion` hasn’t been called for x seconds quite aggressively
00:37:11	danny:	you read logs?
00:37:43	pari:	But your client stalling + checking logs would go quite a long way to help users debug it
00:37:45	Micah Zoltu:	Spin early in startup until consensus client is up before opening up JSON-RPC and whatnot.  Alternatively, leave the retry to whatever individual's are using for running stuff (like systemd or docker or `while(true) geth` or whatever.
00:38:41	Jamie Lokier:	Are there “big” test scenarios that could be added to Hive (such as deleting one or the other database, breaking sync, artificial network or RPC delays, etc)?
00:39:05	pari:	Next shadow fork Thursday (5th May(
00:39:05	Marius:	https://github.com/ethereum/go-ethereum/issues/24720
00:39:47	Micah Zoltu:	I feel like we are close to fully automated back-to-back shadow forks.  "Who is participating in the 5:00 mainnet shadow fork?" "Not me, I'm going to the 6:00 one."
00:40:39	Jamie Lokier:	I think there are more junk/weird nodes sending odd stuff on Goerli for stressing clients’ self defences, and Goerli is faster to sync of course.  Not sure if either of those things add value at the moment.
00:42:42	Marius:	BTW prysm currently breaks on kurtosis https://github.com/parithosh/nightly-kurtosis-test/runs/6222613873?check_suite_focus=true
00:45:05	Marius:	(nimbus too, but that is more expected)
00:45:20	danny:	we also had some discussion around timeout on engine api endpoints. I’ll put up a PR for review based on that shortly
00:45:26	pari:	^ nimbus pushed a potential fix earlier today, so it might not break tomorrow
00:46:33	Mikhail Kalinin:	https://github.com/ethereum/execution-apis/issues/212
00:46:34	Tim Beiko:	https://github.com/ethereum/execution-apis/issues/212
00:48:41	Marius:	We should get Besu up hive asap
00:48:55	Marius:	https://hivetests2.ethdevops.io/
00:49:26	Tim Beiko:	https://github.com/ethereum/execution-apis/pull/200
00:50:08	Micah Zoltu:	Reading...
00:50:29	Justin Florentine:	We have a dev dedicated to passing Hive
00:50:52	Marius:	Very good! 
00:51:03	Tim Beiko:	+1 to defining safe/unsafe as a safe/unsafe block
00:51:05	Łukasz Rozmej:	Would it also a good opportunity to remove 'pending'?
00:52:23	Marius:	Removing "pending" will break a lot of users, I would slightly prefer to remove it post-merge (less load for us, less things to break for users,...)
00:53:00	Sam Wilson:	confident and fast? What makes the unsafe one unsafe?
00:53:09	Tim Beiko:	It can be re-orged
00:54:29	danny:	lol latest
00:55:24	Mikhail Kalinin:	I like “latest” because it somehow may be read as “head” while replacing latest with unsafe looses this semantics
00:55:31	Vitalik:	there's 3 levels of confirmation:
00:55:35	Łukasz Rozmej:	stable/unstable? ;)
00:55:47	Vitalik:	Latest - winner of fork choice, potentially unstable
00:55:57	Micah Zoltu:	Finalized, Justified, Safe, Latest/Unsafe
00:56:14	Micah Zoltu:	Where "Safe" is not yet fully defined.
00:56:24	Mikhail Kalinin:	Safe is Justified for now
00:56:26	Vitalik:	Safe - cannot be reorged assuming network is synchronous and >= 75% honest (roughly)
00:56:33	Mikhail Kalinin:	but Safe will evolve
00:56:50	Vitalik:	Finalized - cannot be reorged unless millions of eth get slashed
00:57:10	danny:	even then, it can’ b re-orged automatically
00:57:23	danny:	it just means some nodes will see a different version of reality until manual intervntion
00:58:07	Micah Zoltu:	There is also Justified, which is between "Safe" and "Finalized".
01:02:45	Ansgar Dietrichs:	so with mev boost the default is that it is set by builders without constraint
01:02:52	stokes:	yes
01:02:56	Ansgar Dietrichs:	so we have to actively choose to bring it back under proposer control
01:05:17	Tim Beiko:	https://ethereum-magicians.org/t/og-council-post-merge-testnets/9034
01:06:28	danny:	“take them over” still means they need client software support in some capacity
01:12:09	Justin Florentine:	I found Peters point about testing mid-sync situations compelling. I’d like to see those spec’d out, standardized and run on a shadowfork
01:12:57	pari:	Metric I’d like to aim for: 2x main net shadow fork with no/really minor issues
01:15:22	Micah Zoltu:	Unrelated to current discussion: Have me made any progress on getting better client diversity among validators?
01:15:49	Micah Zoltu:	Any up-to-date pie charts floating around?
01:16:36	danny:	https://clientdiversity.org/
01:16:45	danny:	sigp block print is what you want on the CL side
01:16:51	pari:	https://twitter.com/superphiz/status/1513938761968726016
01:16:52	Thomas Jay Rush:	https://ethresear.ch/t/blocks-per-week-as-an-indicator-of-the-difficulty-bomb/12120/16
01:16:56	danny:	“miga labs” is a crawler so not by stakeweight
01:17:02	Thomas Jay Rush:	The latest weekly chart ^
01:17:31	Péter Szilágyi:	But wen merge?
01:17:35	danny:	soon
01:24:12	Tim Beiko:	Every ~100k blocks is ~2 weeks
01:24:21	Tim Beiko:	So at worse we wait until the next period before making a call
01:24:38	Marius:	longer blocktimes >> another fork
01:24:57	Trenton Van Epps:	if anyone wants to see blocktimes live updated here: https://dune.com/yulesa/Blocks-per-Week
01:26:46	Tim Beiko:	How quickly does the difficulty adjust?
01:29:03	Tim Beiko:	You can go to Vitalik for your merge hashrate bets!
01:31:11	Micah Zoltu:	I weakly favor just pushing it back so we can reduce anxiety.
01:31:13	danny:	bomb going off during merge actually reduces the likelihood of a pow fork pump and dump.
01:31:15	Łukasz Rozmej:	Reliable systems have backup plans
01:31:28	Justin Florentine:	Does this mean we don’t really value the bomb as a forcing function if we’re looking at end of year for it to go off, but merging on our own schedule?
01:32:05	Trenton Van Epps:	echoing Danny's comment - there should be some minimum threshold for people who want to maintain PoW
01:33:24	Micah Zoltu:	1. Reduce core dev anxiety.
2. Protect users.
<sweating person deciding which button to press>
01:33:29	Ansgar Dietrichs:	realistically the bomb was meant as a forcing function to merge at all. now that we are committed on doing that at the earliest reasonable time anyway, we might as well remove the bomb instead of moving it
01:33:44	Ansgar Dietrichs:	I feel like keeping it or completely removing it are the most reasonable options
01:34:27	danny:	thanks!
01:34:30	Thomas Jay Rush:	Glad to be here for the first time ever. Cheers.
    
## Attendees
* Terence
* Tim Beiko
* Zuerlein
* Micah Zoltu
* Justin Florentine
* Pooja Ranjan
* Danno Ferrin
* Mikhail Kalinin
* protolambda
* HP
* Marcin Sobczak
* Karim T.
* Trenton Van Epps
* Casey Gardiner
* Marek Moraczyński
* danny
* Péter Szilágyi
* Martin Holst Swende
* lightclient
* Tomasz Stanczak
* Leo Arias
* Daniel Lehrner
* Alex Stokes
* Matt Nelson
* Pari
* Łukasz Rozmej
* Phil Ngo
* Vadim Arasev
* Jamie Lokier
* Fredrik
* Andrew Ashikhmin
* Vitalik
* Mateusz Morus
* Jose
