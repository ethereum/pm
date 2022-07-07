# All Core Devs Meeting 136
### Date/Time: April 15, 2022, 14:00 UTC
### Duration: 90 minutes
### [Recording](https://youtu.be/JXbOeiPN_uE)
### [Agenda](https://github.com/ethereum/pm/issues/508)
### Moderator: Tim Beiko
### Notes: Alen (Santhosh)

## Decisions Made
| Decision Item | Description                                                              | Video ref |
| ------------- | ------------------------------------------------------------------------ | ------------- |
| 136.1 | I'll share this, explicitly, just to be clear, we had discussed a few times that like ring could be won't run through the merge. so just for people listening, this ring could be, will not, I don't think the network will be like shut down right at the merge | [48:05](https://youtu.be/JXbOeiPN_uE?t=2926) |

**Tim Beiko**
* Good morning, everyone. Welcome to AEV. 1 36. I appreciate people coming on the call on what is a holiday in a lot of places. so yeah, thanks for coming in. Hopefully we can wrap this up, within time, basically, all of, lot of merged stuff, on the agenda today and, couple Shanghai updates, mostly on stuff that's already, been included. and yeah, to start on the main net stuff we did have, or on a merged stuff, sorry, we did have our first main net shadow, this week, unfortunately, both Perry and Danny are in transit dev connect. so they can't give the high level summary. but I'll, I'll try and then it'll be helpful to get client teams to chime in. but as I understand it, the mainnet fork, had some issues across, across a bunch of clients, but we managed to finalize, on, on the other side of it, on the shadow fork. 

* So, you know, from a like high level network point of view, it, it went well, but it obviously uncovered a bunch of, smaller issues across, several clients, which, we, we then need to fix, we're planning to have a Gordy shadow fork next Tuesday, and another main net shadow fork next Saturday, Perrys posted the, a configs for all of these in the discord already. and then for the main net one, obviously if folks wanna participate in that, you need to sync your main net node, which might take a couple days. so just be mindful of that. but yeah, I don't know, if any of the client teams kind of want to just share some of the issues they, they ran into, during, during the shuttle for, 

**Marek**
* I can start. Thanks. Yeah. so we had problems during, the transition. Most of our nodes expect Nimbus are recovered now and they are working fine at shadow fork. I would say that the main reason was that our sync is, is not ready and we are aware of it, but of course we don't want to miss any, merge testing. So, even if we are not, fully, ready, we, we are trying to participate in every merge of that. I hope that in new shadow work, we won't have the same problem during the transition, but on the other hand, I have to say that we are still working on, sync, to give you more details. It was connected to, peer refreshing. We had wrong peer information, and also we had to run condition in our beacon header sync. And because of that, the sync was stuck, about if stats, it is probably only reporting to if stats back because I don't see delay when I'm observe nodes, they are, just producing, blocks and, sorry, processing blocks in, correct. right. So yeah, that, that itself from my side. 

**Tim Beiko**
* Thank you for sharing. anyone else? 

## Besu
**Justin Florentine**
* Hello, this is be Sue here. we had a couple of issues, with, with the shadow fork. a couple of 'em were configuration issues that were quickly sorted out. Two of those were concerning and are being worked actively right now. One of them was forgetting, syncing. we had an issue where we had a fast sync that pivoted across TTD and, ended up using the incorrect validation rules. and that's, that's been addressed. There's been a whole lot of, attention being, spent on our, our synchronous. so there's a number of PRS in flight for that. the more concerning one is still being investigated right now, we had a receipt through mismatch. that would be a consensus break on our side. We stopped validating and we're basically hung up, maybe, you know, 10 or 15 blocks after, TTD hit on the shadow fork. So, we're still investigating it. we're pulling traces and, we're comparing them and trying to figure out how that happened. 

**Martin**
* So was that just one note that displayed that? Or was it something that, which was experienced across all nodes? They receive proof. 

**Justin Florentine**
* So, yeah, so there's only two nodes running and they, we expect both of them to have the receipts roots, mismatch problem. the other one just didn't hit it for a synchronization issue. 

**Martin**
* So, but do you not, when you download the blocks and you sync, do you not verify their secrets of these? 

**Justin Florentine**
* No, we, we do verify them and unfortunately we came up with a different answer, so we treated it as a bad block, 

**Martin**
* But how could they not both hit the issue then? 

**Justin Florentine**
* Oh, because the other one didn't get that far. It was hung up for a synchronization issue later. Yeah. Earlier in the 

**Tim Beiko**
* Right. So you only know that got that of point got the receipt mismatched, but if you had a second one, you think, obviously you can't know for sure. Cuz you haven't found the issue, but you think it's likely it would also hit the same thing. Right. 

**Gary Schulte**
* I believe we did have a non, EF node that had the exact same receipt root issue. Got it. it's just that the two nodes we're talking about were the ones party were sorting. Got it. 

**Mikhail Kalini**
* And I guess it's not related to pre code because there were no, such transactions submitted on the main net, 

**Justin Florentine**
* You know, that's the first thing that I looked for and I didn't find any evidence of that, so yeah. 

**Tim Beiko**
* Got it. yeah. Thanks for sharing and really keep us posted, once you find out what the, the, she was, argon Geth anything on, on your end? 

**Martin**
* I might be the only one guest team here and I can't say lot. I been, I've been on vacation for a week. as the week before that I spent trying to, to find issues that were on covered in when we did the, the curly shuttle for, two nodes. Some I got corrupted, state data or Snapchat data. and we were, we have still not yeah. With a hundred percent certainty rooted out what the cost of that is. So, yeah, I'm looking forward to more, more of these shadow of works and garish shadow of forks and see if we can repro it again. that's it, 

**Tim Beiko**
* Got it. Andrew, 

**Andrew**
* Yeah, I, I think, I, I haven't been involved heavily involved in the shadow of work testing, but I think, it went, alright. One issue though. the, I think both lighthouse and prism, call net methods on the engine API port, but we, we only expose E methods, not net methods. So I would like to clarify can lighthouse and prism stop calling net methods on the engine API port, or otherwise let's standardize it because in this spec it only mentions methods. So I'm not right now. I, I would rather not expose net methods on the engine API port. Anybody from lighthouse prism, 

**Terrance** 
* Hey, Terrance here from prism. So yeah, I think that's a bug that we will fix. I don't see why we have to use name method. I think everything could be under the, everything could be under the E method. So yeah, we'll fix that. That's that that's where bring that to my attention. 

**Andrew**
* Okay. Thank you. And I don't think we have anyone from my lighthouse, is that right? 

**Mikhail Kalini**
* Yeah, but we don't need net methods on the engineer. Definitely. So it should be removed, as I understand that method, which requests a version of network, which is network ID, in E status message. So it's like if chain ID should be a good replacement of that or as, from tech, post in this discord, we can use, to exchange, transition configuration method to verify that we are on the right chain because terminal, total difficulty said for the main net, for example, will, will never be, messed up with any testnet. 

**Gary**
* Cool. Is that a, an execution spec chain to include, network ID chain ID on, on that engine API? Or is that, is that already in there? 

**Mikhail Kalini**
* It's already in the spec if chain ID and we will not add any, any method from that, namespace. Yeah. So EO client that follows the spec should expose all the EMA that's included ad. 

**Gary**
* Right. I thought we were talking about adding that to exchange ation exchange, transition 

**Tim Beiko**
* I see. Yeah, we have at least, Matic here. yeah. Do you wanna give an update from the, the cl side, how the shuttle fork went for you? 

**Terrance** 
* I can give update on the prison side. Yeah. Yeah. And I think everything went relatively well. We discover a few, bad cases, but there are not consensus, so people doesn't necessarily see it. So there's definitely like, things that we can improve on in terms of performance. And then, and then we are also working on the UX as well, because like I'm monitoring out score channels and there's a lot of peoples, they don't necessarily know like still dunno how to bunch a node between cl and the El. So we're working on the, we're working on the us side to make it more, smoother for the end users and yeah, that's pretty much it. 

## Shadow Fork Updates
**Tim Beiko**
* Awesome. Thanks. Anyone else from one of the consensus layer flying teams? Sorry, I don't recognize the names as easily. Okay. I guess not. so yeah, thanks. Thanks everyone for, for sharing these. And like I said earlier, like we'll have two more shadow forks next week, which, you know, hopefully give us, no new issues. And, if some of the current issues we have are fixed, we can, we can test them in production. next thing on the agenda, Mikhail, you had, you spent some more time this week digging into the latest valid hash. you, you shared your analysis on, on, the agenda, but maybe it's worth it for you to take just like two, three minutes to walk us through, your thoughts and, yeah, the hack of the, that just was shared in the, in the chat. You can either share your screen or just talk whatever, works best. 

**Mikhail Kalini**
* Yeah. Okay. So Yeah, I'll share this screen. Thanks then. So Can you see my screen? Yes. Yep. Okay. So cool. a brief background on it. So we have latest valid hash and the engine APIs back. And, basically what the spec says is that, while El clients is syncing, it may encounter in invalid payload, invalid block. And,since cl is, since we have like unidirectional, communication channel where cl post send a method call and get a response, El will have to store, an information about inva chain, to later respond with this information if, cl requests and do any, do any method call, with the information from this inva chain. So that's actually what stated in the spec. and, yeah, this discussion started from, like, yeah, this discussion started because, apparently it's currently, currently EO clients doesn't store require information. Some of EO clients do store, if you recent invalid blocks, but that's not enough to serve this, data correctly. so here is the like implementation how it could be implemented, like the kind of implementation tips. And then we just, we're wondering, whether we can't just meet support in this urine, El client at thinking. And I was just, you know, thinking about it more about possible attack scenarios and this, this attack scenario seems like, it has, it may have a big impact on the network and, it's, it's likelihood is not that, you know, it's not that high, it may have happens during the period of no finality, where this period class for like more blocks than, we have a states for. So if like period of no finality lasts for more than, 128 blocks and, clients doesn't have a, doesn't have a state to execute, a submitted block if it branched, from the, like an Oracle chain more than this number of blocks, which is like, which, which, which may occur. 
* So, we are risking to have, all, all S which will try to process this block in an infinite loop of trying to sync with incorrect, with a valid chain. So it's like an, line failure, which will require manual intervention. Yeah, this, this is my, these are my conclusions. So you may take a look. yeah, you may just take a look at this. and, based on this analysis, based on this attacks matters, I can conclude that we have to support, have to support, this functionality as it stated currently in this spec. So we will likely have, test errors that will discover this kind of stuff. So that's all from my answer on this topic. Happy to answer any questions. 

**Andrew Ashikhmin**
* I have a question. So, if, a block is missing, so the El tries to download a block, but, then it, it can't, and it times out, we first like we, so if, if, if there is a gap on the side chain that we don't know the exact, latest valid ancestor, and also that timeout, perhaps it's transitory it, it's difficult in that if you kind of, you, you, you have, you've downloaded, a block and you've, you you've found how that, something is wrong with that, with that block, then, then it's fine. You, you, you can go through, through the ancestors and, find the, the last valid one. 

**Mikhail Kalini**
* But if you have a gap then kind of a bit lost, if you have a gap, you will not be able to, oh, you mean, okay. So if, if, if like you're yes, see, so it, it may be that, like first block in this, fork, and this site site, site chain, this site fork will have, will be inva, right. then, then you have a gap you miss are missing second block, and then you have a, you have third block and the consensus, the client just admits like the fourth block is this kind of situation. 

**Andrew Ashikhmin**
* I mean, by, by gap, I mean, you like, you don't have, you, you, you, the El doesn't have, the, the missing blocks locally. It has to download them, but the download from, from its peers, but the download fails, right? 

**Mikhail Kalini**
* Yeah. Because, because it's invalid, right? 

**Andrew Ashikhmin**
* Yes. For instance, because it's invalid or, but then, so one question is it might fail because it's embedded or might be the network is temporarily down. Right. And then at some point it's, the connectivity is restored. 

**Mikhail Kalini**
* Yes. And, in this case, yeah. That's interesting case because if you have this kind of issue, like, so it's like a data availability problem on the outside, right. I mean, we will be in the data availability, data and availability issue. Right. We have it. 

**Andrew Ashikhmin**
* So this is what we mean because there will be there two Issues. So first there's data availability issue so that you can, I guess, never be certain, or you, you, you might approach certainty, but not be 100% sure that whether it's a data availability issue or the block is embedded. yes. And on the other, the, the, the second problem is that if you don't have, the block, then you cannot establish, the latest valid, a, 

**Mikhail Kalini**
* Okay. So the first data availability problem is where, will not be, should not be an issue on the outside, because in this case, you will be what we are like, what this attack scenario is about the right online notes that are the, it have been synced with the network. And, they are important, received, blocks from the network in a lockstep node. And there is the possibility to make them, like to turn them into this infinite sync and loop with invalid chain. But, yeah, but they will receive all the beacon blocks, from the malicious chain before. So they will, there will be no data availability issue in this attack. So it's like, you know, when you are fullest team, data availability becomes the responsibility of, consensus layer. And if you don't have a beacon block, so you will not, you will never, follow this chain. So yeah, there is an assumption, that we have all blocks here and we can't, exactly understand which one is invalid. 

**Andrew Ashikhmin**
Okay, cool. Thank you. 

**Mikhail Kalini**
* Yeah. But yeah, the case, what you, what you had described it may, may happen. Node is syncing and it pulls blocks from, execution way and network. I was also like a kind of thinking of this scenario and then just understood that it's not, the online node, that are fully, fully synced before they just not affected. And yeah, it's okay. And they will just drive all this syncing node to, through this period of instability. And, yeah, they will just rework, this is the, yeah, this is the second attack, you know, so with the Sy yeah. This, yeah. The second scenario, which is not that impactful, like this first one. 

**Martin Holst Swende**
* So I'll just about this first attack. What is the special thing about, you said 128, 

**Mikhail Kalini**
* That's just, you know, this because the number, yeah. This is where, this is the default number of, most recent state versions that, clients are stored. Right. That get for example. Yeah. So that's about it. Yep. Yep. So that's, that's the, this attack, my cure brand, adverse virus admits a block, which is invalid, but, you don't have a state anymore to execute, this block and, execution where a client will have to pull it from, from the network. yeah. 

**Martin Holst Swende**
* And, and we Case in that particular case, if the state availability thing is, is what you're thinking about. I don't think so. We at least forget we still have the block, we just don't have the state. So we just have to go back somewhere where we do have the state and then regenerate the state, but it's not a something we need to put from the network in this case. 

**Mikhail Kalini** 
* Okay. So, yeah, but like, this state, missing state issues, just, because we need adversary would like to make the, notes in, into sync and state, that's it. And then in during sync, they will just encounter that this payload is invalid. If they just drop this chain and never say back to cl that there isn't invalid payload, just please invalidate this chain and never send it me again, cl will, try to, to, to stay on this chain and try to induce the sync once again and so forth and so forth. So El must report back in this case, I like just assume that this common ancestor with, canonical chain and this common ancestor, yeah. Post state of this common ancestor is the requirement to execute this, first invalid payload, yeah. The condition for this attack to happen, that we don't have this post state it's been proven. And yes, El, have to, pull this, state first and to make, to, to, to pull this state induc SIM process and response sinking.  that's that's this scenario, 

**Tim Beiko**
* Martin, did that make sense? Is there anything you wanted to add? 

**Martin Holst Swende**
* I don't have, I can say that I fully understand totally everything about this attack, but I don't have any further questions. Yeah. 

**Tim Beiko**
* Fair enough. any anyone else? Yeah, I looks like came off mute and went back 

**Gary**
* On. I was just wondering how, what, what's the, what's the size of, I mean, do we just need one malicious proposal in this case or how, how coordinated with this type of attack need to be? 

**Mikhail Kalini** 
* Yeah, that's a good question. We, we may have like couple of proposers, I guess, because in the proof of stake, yeah. And, we, we also yeah. Need some, we need the ability of, we need enough of stake to, to game, to, to game with the LMD ghost, for choice rule. So we have you, yeah, that's also a condition like to make this attack happen if Atari owns, an amount of stake that make, cl clients, which are staying on the canonical chains somehow to reward to, to these like malicious chain And how much yeah, Probably it's yeah, probably it's invisible, taken in a account that there is the 128 blocks, in the canonical chain already, to, to make this happen. But we also have like shallow state clients. So the, yeah, this probably the, like the likelihood of this attack is like pretty low, but we would just want to prevent this, this. And I, oh, sorry, go ahead. 
* Yeah, go ahead. 

**Tim Beiko**
* I was gonna say like for, by shadow state clients, I think like argon is probably my example here. Like, I'm curious to understand just like, just from a, I don't know, engineering perspective, like, is it feasible? Cause I, I, I know we, we changed kind of the requirements around the spec because it was really hard for, for argon and maybe another client to like support it as is, but like yeah. How I, I'd be curious to just hear, you know, from them, like how complex is it to like mitigate this issue? 

**Andrew Ashikhmin**
* And, you know, I've already day started, ive introduced, kind of, a basic level of, of protection, this, cash over in, in valid blocks. but, it might be not Bulletproof yet, so I I'll revisit the ill review, the Miha at tech scenarios and I'll revisit argon code, but, I think we should be able to mitigate against such text. 

**Tim Beiko**
* Okay, awesome. it does feel like, I dunno my, my, like, you know, people need time to digest this and, and, and think through it a bit more. So we should Def discuss this. I mean, both in person next week with whoever's there, but, yeah, on, on the next call, based on, you know, people having, having spent more time digesting it. 

**Mikhail Kalini** 
* Yeah. It would be great. if you take a look, if more engineering eyes will be on it, probably I'm like overestimated and the, 

**Tim Beiko**
* Yeah, I think one thing that, yeah, beyond just like, El engineers also having folks like from the proof of stake side, like if this does require, you know, say a third of the stake or two thirds of the stake, are there, I guess is like, are there worse attacks you can already do with one third of the stake, if that's what you require here? 

**Mikhail Kalini**
* Yeah. Fair that's fair. Yeah. 

**Tim Beiko**
* But yeah, I think just like from those two angles, if we can look from like how easy it is to mitigate, and then is this actually the worst thing or like one of the worst things you can do with that level of stake at that can probably inform us about how, how much to prioritize, fixing this and, and changing the spec. Any other questions, thoughts about this? Okay. thanks  Mikhail for, for putting this together and, and Cherry put us. Thank you. 

## Testnet Plans
**Tim Beiko**
* Cool. So the, the next thing, I wanted to make sure we cover, so on, on the last all cord devs, I think we were, we were short on time and we like briefly to touched on like test nets. And I know there were like some differing opinions about like how we might want to approach rolling out, on test nets obviously once, like the shadow forks have stabilized and, and we're in a better spot generally. but I think, you know, there were some comments about like, maybe we should, spend more time on Testnet than we usually do. and, and, and trying to figure out like, what's, what's, what's the sweet spot and, and what, and, and, you know, based on that, I think that kind of affects, you know, how the, the time it takes to go from the first test that the may not, meek you shared some comments in the agenda. do you wanna take like a minute or two to, to just go overdose? 

**Marek Moraczynski**
* Yeah, sure. so we had a conversation with team, why we think that it is it'll be valuable to, have longer Testnet and we discussed a few risk. One of them is obvious client backs, and I believe that the sooner we start working public Testnet the longer time we should it. And there is tomorrow, let me start with, I think, less important. So, all our dev nets are controlled by our, we art hero par. So it seems to be big step if we move, to network, from network to control by, controlled by one, person to controlled by many people and team proposed that maybe we should try staffing closer, to public Testnet in terms of validators control. And I don't know, what do you all think about it? should we do it, or should we try it on a real Testnet like, Sapia what do you think? 

**Martin Holst Swende**
* So, one thing that I, I think, I mean is that it might be difficult to get people, to actually actually go through with this. And in the end we just be, yeah, the same teams. So the, the dev teams that are doing it. 

**Tim Beiko**
* But I think right now with America saying, is like, Perry is running like most of the nodes, even on behalf of a lot of the, the client team. So like, I'm not sure how many, and, and I might be wrong here, but I'm not sure how many of the actual client teams are like setting up and running their nodes with all the, say all the ELs running with each cl, and, and vice versa, on the current shadow forks. Yeah. 

**Marek Moraczynski**
* I think client teams are running nodes, but still finalization is all, depend on para notes. 

**Tim Beiko**
* Oh, got it. 

**Marek Moraczynski**
* Yeah. So, yeah, network, will work without, client team notes, but, not work without Paran notes. 

**Martin Holst Swende** 
* But, but how would you rather see them? 

**Marek Moraczynski**
* Mm, so maybe, it was like, proposition only, if we should, do something here. So what, what, my question is a bit who will control the Testnet, nodes that, that not validators, 

**Tim Beiko**
* Right? Yeah, yeah. Yeah. We, I don't think we ever agreed to like specifically who, but there was, we, we wanted to have like two, basically two Testnet, one, which is controlled mostly by the EF and client teams. so it's like a bit more stable and maybe some infrastructure providers and then the other one, which has a bit more of an open validator set, where anybody can join. And on that one, you might expect some, you know, some non-ideal and, and things like that. Would it, oh, sorry, go ahead. 
* Sorry, Gary, you kind of broke up. Oh, if you're speaking, Gary, we can't hear you anymore. Okay. well, if you get your audio back, Gary, please chime in. So I guess, you know, we do have two shadow forks coming, one Tuesday, and it's probably a bit late to, to change teams that too much on that one, but we have one also scheduled for like next Saturday. would it be helpful to distribute more of the validators to client teams? So that finalization doesn't depend just on, on Gary? is that like too quick to do it? Would we wanna do some, like, maybe in the week after that, which are set up that way? 

**Marek Moraczynski**
* I think we, can, talk about it with Barry, cause he will be the best person for that. I, I'm not sure if, the notes are in internal networks, so, Barry should, say about it more. okay. so maybe the second point, so misconfiguration, so in every hardware we observed some amounts of notes that were forgotten to upgrade and all previous hardwares were significantly less demand for note runners. it was just download the version of the client. now note operator need to do a few things, upgrade cl upgrade El configure, secret between clients, make sure that there is connection between clients so entire people can train it on K and we can mitigate it with correct announcements and documentation. However, in practice, I believe that the longer Testnet the longer public Testnet will reduce the number of misconfigured notes for the next Testnet. And later for, for my net, people need to get used to running notes, with two applications. And that was my arguments for longer tests. That's Yeah. And that that's still for my side, team. 

**Tim Beiko**
* I have thoughts, but anyone else from other client teams, wanna chime in first, if not, I, I, I agree with you on the configuration issue. I, I do think like this is kind of a higher, or, or more complex change than like we've we've had with previous upgrades. and hopefully ke has helped a little bit move the needle clarity, a lot of people and the vast majority of people are not on kiln. so I guess it, it does seem like, you know, you probably want to give people more of a heads up for at least the first one so that they get the configuration rights, but then once they've done it, I think you can probably, you know, assume that they can do it right the next time. Again, assuming things, things go smooth, clear on the fork. 
* So my view there, it's almost like you would wanna separate, like, you know, if we're gonna fork three, Testnet like, if we're gonna fork as Sapia goly and Robson, you might want to like have the first one happen and leave it running for a bit long, like give a bit more of a heads up for people to configure their node, leave it run for a bit longer, but then, you know, as soon as like, the fork happens and, and, and if you, if people have configured things correctly and it didn't blow up, then like you can probably have the two other ones, you know, fairly close apart. Like, I don't think, because people are gonna have to run through the process a few more times, but it's like the first time with definitely be the hardest. so my general approach would probably be like, fork something like Rob's. More times, but it's like the first time will definitely be the hardest. so my general approach would probably be like fork something like Robson first, because it does have like pretty significant usage. but we don't intend to keep it around much. So if it, if it doesn't go super smoothly, not the end of the world, one, you know, Robson is, is forked and like stable. Then like you then schedule kind of Def forks for say Gorian Sapia. And then you also kind of get that, say, you know, say you like fork Roston and like two, three weeks after that, you for Goria Sapia by the time you're fork Gordy, and then Sapia, you've, you've already had robs that be live for a month. So I think you, you get this kind of longer, duration on a Testnet and we can do things like obviously syncing new notes, make sure that still works. 
* Robson has a pretty big state in history, so it's, it's, you know, it's a good kind of proxy. so, and, and then obviously we'll want to see all the Testnet stable before we move to main, but like, it would probably look something like, I don't know, Robson has had like a month, a month and a half, and then like, maybe you do Gordi second, cuz there's a ton of activity on that as well. and you, you get like longer data on that and then maybe Sapia will only have for, for a few weeks. but if we have like kind of long term data on, on robs medium term on Gordi, then that's probably sufficient. and just, I guess to bring it back to also one thing you said at the very beginning, you know, like the, the, the earlier in, the earlier in the process that we for Testnet the longer we wanna see the them run fine. 
* But I do think like with the amount of shadow forks we're doing and we're gonna keep doing my expectation is like we would only move to test nets once the shadow forks out of say main net are going really smoothly. So like, to me, it's like, if we're, if we've managed the, for the shadow fork, main nets smoothly, the test nets should be kind of a easier than that. yeah, so I don't know, like, I guess, yeah, the recaps, like I would probably do Robson first, wait, wait a while. Make sure it works, then probably bundle Gorian Sapia and then once that's all set, you, you go to main net, and then Martin had a question in the chat, about, paired with cl Testnet. the answer is no, the only one. So Gordy has a long lived cl Testnet, which will kind of transition after, but for ston, for, for Lia, we'd have to, to launch new cl Testnet. Yeah. Andrew. 

**Andrew Ashikhmin** 
* Yeah. Can we also agree that, before we, migrate a public as not, we abandoned the unauthenticated port, so we leave only the JWT port. That would be, I think, 8551 by default. Right. So we leave on that port, If that's all right with everybody, 

**Martin Holst Swende** 
* Wouldn't that be kinda an implementation choice? 

**Andrew Ashikhmin** 
* I think, we wanted for security reason not to take was that the, unauthenticated port was only for com kind of for ease of testing rather than, working solution. 

**Martin Holst Swende** 
* So if I understand you, what you're proposing is that we should not serve engine under the unauthenticated 

**Andrew Ashikhmin** 
* Yeah, to not to serve the unauthenticated port before, before switching public task net. 

**Martin Holst Swende** 
* But are you proposing that RPC services should not be available under the legacy port or are you proposing that the engine API should not be exposed? 

**Andrew Ashikhmin** 
* That, well, in, how we have it, we three ports, or even four, maybe. So one for like non engine API port for Ethan and everything else. And for engine API, there is, there are two ports, 8550 unauthenticated and 8551, JBT authenticated. So I proposed to stop solving completely the unauthenticated, engine API port. Right. Okay. Yes. Then I'm with you and I, nothing against it. 

**Tim Beiko**
* Yeah. And it does seem like it, especially based on the configuration stuff we were just talking about, we definitely want to force people. If, if on main net, the engine API will only be available through an authenticated port, then we wanna force people to make sure that works on the very first test net, because if it breaks for some reason we wanna know then, and not when we're working main. Yeah. Any other thoughts? Comments just on Testnet generally. Okay. So I guess to recap, just to make sure there's no objection, like moving with Robson first, giving people a bit more heads up so that they can set up their, their nodes, making sure that goes, goes smoothly and then once it has, then going through Gordi and then Sapia at the end, so that we get kind of the most data on Robson, then Gordi then, a bit less on Sapia. Gary. 

**Gary Schulte**
* Yeah. I was thinking, it seems to me that Sapia might be a safer target given that there's not as as much, infrastructure that are, if we, we wanted to migrate Sapia first, but for example, I don't think that there's, either scan support for Sapia yet. I mean, we're basically gonna force, Robson, users to have a consensus client set up in order to continue to participate. And I, I think since Sapia is really most only, I've only ever seen, you know, like, you know, core devs and folks on that network, I think it might be an easier target, for the first migration. 

**Tim Beiko**
* Right. I, it depends what you're optimizing for. Right. Like, so if you're optimizing for the, for going smoothly, I, I agree, but I think Merrick's comments was like, if you wanna optimize for people already running nodes, having to figure out how to set up an El and cl combo, then having them do it on Sapia, like people might just not do it on Sapia. So that's just a risk is like, say we did Sapia Robson Gordy, then Sapia goes well, but then on Robson, everything breaks because like the node operator and the folks like say ether scan, or like exchanges or infra providers that just support Robson, they, they just didn't do anything on Selia. that might slow us down more. So I, yeah, 

**Gary Schulte**
* Yeah. That makes sense. I had an internet cut out, when, when Merick was talking. So I, I missed the point that we're optimizing for break it, But yeah. 

**Tim Beiko**
* So basically I think it's optimizing for forcing people to, to think through the configurations and make sure that they work. and then that basically leaves us with like goly and, and Roston, and of those two, I think breaking Roston is less worse because we don't expect the support at long term after the merge. So I don't think we should go ahead and break goly even though it probably has the most usage, so it's like, Roston is like a, a medium test run. And then if that goes, well, we can move to goly and then sip Olia should be really easy to do after, after those. 

**Gary Schulte**
* Cool. That makes sense. 

**Tim Beiko**
* Cool. And I guess as a heads up, this is kind of implicit, but, I'll share this, explicitly, just to be clear, we had discussed a few times that like ring could be won't run through the merge. so just for people listening, this ring could be, will not, I don't think the network will be like shut down right at the merge, but from as soon as the merge happened, ring could be just stops being, replica of, of what's running on main net. so people should be aware of that and, and start migrating away from ring. anything else on Testnet? 

## Shanghai

**Tim Beiko**
* Anything else about, the merge generally? Okay. so next thing we had was, a couple things related to Shanghai. So we already have accepted the E O F E I P in Shanghai, EIP 3540. And, there were two proposals, about how we might be able to, to, to tweak, I guess, EEO F to either ban self destruct or, lay groundwork for, for code chunking for vocal tries. I know Andrew, you had, left a couple comments about this. do you wanna maybe just give some context here on, you know, what you, what you're thinking is, yeah. 

**Andrew**
* I think, everyone's team preference is to disable self-destruct high, but if we don't do that, if we do it later, then my initial thinking, then maybe we should disable it, in for a E O F code, but then, X has made a good point that, maybe it's counterproductive because if say we change self-destructing to send all some something useful, then it doesn't make sense to disable it in E F code. So I think, I revoke my suggestion. I don't think it makes sense to disable self desc specifically for E F code. 
yeah. And the second point is about code chunking. I think code chunking is kind of, it looks rather hairy code chunking for, for the vocal tree. Right. So, and, it kind of looks ugly because then when you, you contaminate EDM code with, vehicle code three commitment logic. So kind of maybe I I'm hoping for a more elegant solution. I don't have any the ideas, but if somebody comes up with a more elegant solution for code chunking, that would be terrific. my concern is that let's try to think carefully about E F and coun, so that the E F changes, that we introduce in Shanghai don't make, don't make, the introduction of, the vehicle three harder specifically in the area of code chunking. so again, I don't have any ideas. I just want people to think carefully that we don't yeah. Introduce changes in Shanghai that would make vocal trees more difficult. 

**Martin Holst Swende** 
* Do you have any, any like more concrete example of what you think is yeah. What part of it is bothering you? 

**Andrew**
* Well, because E O F it's, with the, before E all there was no structure in the code and, the only, difficulty was to differentiate push data versus non push data. Right. So, but basically it was just a string without no, no structure. And you can chunking, you could con count the chunks of that string with E F you introduce some extra structure. Right. And, so you, you have sections with E I, how do those sections align with ch chunks? Right? That's that's my worry. 

**Tim Beiko**
* Pawel, you have you hand it for a while though? 

**Pawel Bylica**
* Yeah, actually I, I wanted to, to go back to the, to the service track, but I can start with this, this chunking. so we were thinking about that a bit in, in context of E F. So the, there is one bite wasted, in the, in the chunks currently to encode the, the service track. no, the, the, the EST locations. so we we're thinking how to actually, if we can mitigate that, with E F and one of the ideas was to have separate section that encodes the, the EST locations outside of the code. so we kind of have mixed feelings about that. there was some, some working into this direction, but, it wasn't so, so much smooth in the sense that in coding that in a separate part of that, I, as I remember it, wasn't like so great. 
* We wanted to push it as a first thing. and kind of, I like I'm personally thinking about for the future, that there might be a way to, to remove the, the jumps as they work currently with something else that will not need to have the jump test at all, that would kind of solve the problem. but that's also nothing that is ready as of now. So I think it kind of also depends of the timings. I think in the case we would have that ready, the specification for such features ready before the migration to, to broker happens, then we can consider that. but as, as of now, it looks, it would be some future version on of E O F because we don't ship with that straight away. 

**Tim Beiko**
* You also wanted to say something about self destruct, so maybe, 

**Pawel Bylica**
* Yeah. Yeah. I have two comments to that. So, well first I think, the, the, the most important question is if this sent all is, is useful in the sense that we want to have it, or is just the, the minimal way not to break lot of existing contracts. So I'm sure, like, what's, what's your opinion about that? but like technically, like disabled self, during EOF validation is, is, is very easy to do. And that also means the, the EVM will not have to be, I mean, it will not have to modify how self construct works, because it'll just, this instruction will just not show up in the EIF code. So, yeah, it will not be just be, it will not be able physically, physically place that instruction in the code. So we don't really have to switch EVM in the sense that it'll have to different behaviors for EOF and different behaviors for whatever the service destructure for legacy code will work. So that's one thing. And secondly, UF has some, let's say forward, compatibility properties. And even if we start, when it's, it's, it's much better to start with disabled safe tract, because later we can actually assign, even if we decide to like, enable send all in, in this op code, that will not break previously deployed UF contracts. So like, one of the properties of this forward compatibility is that you can say if we assigned unassigned codes, so let's say we, if we start with self <inaudible> code unassigned in the, in the E F, then it is it's easy, to enable it later. Yeah, that, that obviously that, that requires hard work. but we have guarantees that will not break kind of thing. 

**Tim Beiko**
* Got it. Alex, you have your hands up as well. 

**Alex**
* Yeah. I had a, something to say about the, the, the vertical three called chunking. Yep. even before the us, we actually worked on a, with, with Cena, we worked on like an earlier code chunking proposal, and I think the, the vertical three, one still in essence worked similarly, because it has like this first instruction offset bite. And so when we, we started working on EOF, we actually kept this code chunking in mind, compatibility with it. And EOF is compatible with the, the, this vertical spec. the only, the only not thing is that, the EUF headers they're small, so they always fit a single chunk. but in practice, for UF contracts, you would need to always provide the first code chunk, as part of the proof, because that's where the, the headers are situated. and in fact, when we had a decision to be made, whether the, the, the entire EOF headers upfront, or whether we have like a streaming version, this was one of the reasons we decided to have it upfront, because that would be a single code chunk in terms of code chunking. 
and secondly, while it works, without any issues with the current, work with respect, it could be made more optimal. If, if the Oracle spec is aware of UF, then you could, potentially remove this, first instruction offset in case of the UF contracts. you would say one by per chunk. but I mean, it doesn't need to be done. It would be just an optimization. 

**Tim Beiko**
* Got it. Thank, Andrew. 

**Andrew**
* Yeah, it is great that, you have that, compatibility in mind, I guess that was my primary worry. also about, I have a question in E E F in general, like other incentives, for people to move to E O F and any kind of gas reductions, anything like that. 

**Alex**
* Well, not, not directly in the, not, not on its own, but we do have a, a bunch of other proposals, which are not yet slated for Shanghai, but the, the biggest one, the most relevant one for now would be the, the static relative jumps, which I think is, is, would be ready to be considered for Shanghai. But obviously, that discussion is now paused. but that is only possible to be introduced with the NAS, because it depends on immediate values and that reduces, gas costs regarding control flows significantly. because at least looking at some contracts, which are the majority of the contracts on chain, over like 90% of the jumps are static jumps in a solidity contract. And basically it would benefit from the static relative jump quite significantly. We don't have, actual concrete numbers about the reduction, but we do plan to, to create some statistics about, some major contracts, like UN swap, typical comparison between, you know, the current gas runtime gas cost, or like a swap versus, after using this Thanks. 

**Tim Beiko**
* Anything else on EOF 

**Greg Colvin**
* Excuse me, I still can't find the hand on here. no worries. Just, just in general EEO F lets us make a break and say, we're moving forward with some new stuff and we need some way to say this is the new code, and to be able to say these old codes no longer work. So it's just a break we need to make going forward. Getting immediate data is the most important thing right now. Push push is the only thing that has anything resembling immediate data. so it's, we just have to have, going forward. That's all. 

**Tim Beiko**
* Thanks for sharing anyone else on EOF 

**Andrew**
* Yeah, just, I kind of, I'm still on the, on the fence, regarding disabling self-destruct and, and say cold cold because, Pavel's argument also makes, good sense that it can be enabled later if self drug becomes some something useful, but if we, disable it straight away in Shanghai, that's kind of a good, nudge for, for that developers not to use self destruct and maybe not to use Coco. So maybe it's good to disable them straight away. No, yeah. I'm still kind of not sure. 

**Tim Beiko**
* Yeah. We could definitely discuss that in, in more detail, but I, yeah, I guess both, Yeah, both, both, in person last week in person next week and, on the discord, any final comments on EOF 
* Okay. I guess next thing, just like really quick on the agenda. So on the last call, there were a bunch of like new CFI, EIP and discussions about that. And, we, we ran out of time, but, I, I then asked on the discord to see if you wanted to pause kind of considering new EIP for Shanghai until we're much farther along with the current merge work. cuz we've already kind of made a lot of them CFI and all of the client teams seemed in, in favor of that. so, you know, I think it, we can still kind of discuss things, but, it makes sense to just not kind of commit to anything else, until we're, we're much farther along in the implementation process. anyone have comments or just thoughts on that on okay. that said, yeah, Engar wanted to just take a few minutes to chat about, in EIP. We, we, we mentioned, we discussed a while back, so EIP 4396, which changes how the base fee works, after the merge. yeah, I think he just had some questions about how, if, and how we should approach. so, and 

**Ansgar**
* hi. so, so basically, the situation with, with AAP is just that, I think it was originally proposed to possibly be combined with merge itself, because it's more like a security peaks then new feature. then it was decided that was not important enough to, to be bundle with the merge. And there hasn't really been work on it since, there's still several different, alternative versions. So there would still need to be some work put in to, to figure out what exactly what exact version to, to move forward with. I just wanted to basically get a little bit of a temperature check. if this is something that people generally still paying, is important. so I, I don't know, just in case, you don't, you don't remember the details. It's basically just about adjusting the way the base fee, works whenever there's a missed slot. 
* So that, basically for one, you don't have this incentive anymore to dos individual, proposes to basically, the, the trooper of the, and then also, as a separate second thing to basically, keep the constant throughput, even if some portion of the network drops line in case there's like some issue with the client or something. so, so basically I just, I, I was just curious, now that people are like that way closer to the merge, people are affect kind of work more with, with, with the merge architect, architecture is something where people feel like this is important and really should, should be, like more work should be put towards this, or is this something where it's more like we can, we can put it on like, keep it on hold, just wait and see after the merge, maybe if there are any real world issues that that would need something like require something like this. We brought to main net, I dunno. It's just for example, like the, the, the last chat of work we did, I think there was like, right there, there, there was some, some portion of the clients that weren't initially able to, to box, so sort of actually propel behind, main net. And, so, so there's just like one of these example of things that basically the CIP P would address. So know, just, just wondering if, if any clients have, have any thoughts around that, 

**Martin Holst Swende** 
* Yeah. So, I just, I just wanted to get clarified. So you, so could you clarify, are there two main security issues that you see with this one being that there is an incentive to dose other or block proposals and two, the second secure issues would be that due to, or events the throughputs of the chain down? Is that kind of the essence of the security issues that you see or did I miss it? 

**Ansgar**
* Right, right. So I would say the first one is more for security concern just because it actually gives an incentive for dalicious sectors to do <inaudible> things. Although again, the, the would only be that you can, you can try and bring the throughput of the API network down and temporarily before we then get, raise the cast limit. So it's, it's not like a big incentive, but people have brought that up occasionally. And then the other one I would say is less of a security concern and more of just like a network performance degradation concern, where like, if we have any consensus issues and portion of network drops offline, usually we would have to dig a difficulty adjustment to basically get us back to normal put, and now after the merge, we don't have an automatic mechanism like that anymore. So you would stay at reduced throughput until we manually change the gas limit. yeah, but again, that's, that's less of a security concern, I would say. 

**Martin Holst Swende** 
* And for the second part there, Canada, it could not actually be, a positive of thing. I'm thinking if they, if some node go down because some, our resource intensive transaction, those transactions are with 40% of all the nodes keep up then knowing the through, but in that case would actually be beneficial for the network. right. I'm not saying like it's always like that, but it could be. 

**Ansgar**
* Yeah, yeah. AB absolutely. So, I I'm, I personally am somewhat uncomfortable kind of relying on these, just basically accidents to like, like, because I would feel much more comfort, comfortable with, with designing and mechanism specifically around this. If, if people feel like this is a good idea, because that would actually cause us to commit on it being a good idea. I think often times it's more like, yeah, couldn't also have cause of, but, we, we could of course have something right where we just look at the last slots and if there's a certain percentage threshold kind of that, that we kind of go be below or something, then the gas limit is automatically decreased or so something like that, we, we could have, have a mechanism like that, but I, I just, I'm a somewhat uncomfortable basically just having it be implicitly baked in the network, because as you were saying yourself, like a lot of circumstances, if, if there's just a sink issue and you just you're kicked off the network, it doesn't help, to, to reduce the guest limit. So it's, I think in, in normal circumstances, it's, more of an is performance issue, then something helpful. But, again, if, if we use the about it, that's fine. It's just something I think we should not just, yeah. 
 
**Carlbeek** 
* To add to that, I think it's, it gets worse for the, the cl if, if you're unable to follow the cl then, and, and many people are doing this, then we're probably failing to aggregate and all sorts of things, which means we are starting to blow up on a memory footprint and that kind of thing. So I think it's harder to follow on, on the seal, but helps on the El, 

**Martin Holst Swende** 
* Sorry, Carl. So the, the, and what's the conclusion of what you were saying is that, is that you are in favor of the, 

**Carlbeek** 
* No, I just, just to comment on the simplicity, assumption about it, allowing us to sort of catch up as, I'm just trying to argue that it, it only allows us to catch up if we're falling behind on the, the, the El, but if we're falling behind on the cl, then it's probably like there sort of a cascading effect where it probably gets worse. 

**Ansgar**
* It doesn't get worse because the, the, execution air box are less fault. Right. So, so when you say it gets worse, like the will not help there either, right? 

**Carlbeek** 
* No, no. The, the app doesn't affect that agreed. 

**Ansgar**
* Right. So basically, not having the AP could be helpful in relatively narrow subset of El issues, and only if El issues happen to be in range where that exactly the, kind of the small amount of throughput, loss that you get on the network work ends up, being just enough, to, to get you back to sync, which seems unlikely that this would ever happen. But of course, yeah, you can, you can a scenario in which not handling the EIP would actually help the network. 

**Rai**
* I would say, I remember there was a stub in the IP about thinking about incentive for changing timestamps, was more thought put into that. 

**Ansgar**
* Yeah, that's that ended up turned, turned out to only be an issue, an approved of work because in the very early days of the, there was an idea of even bringing this to, to main it before, before, the merge, but after the merge, timestamps are fixed. So there's no control and by the block proposals about the, the time stamps anymore. So this is not an issue, 
* But yeah, so just, just basically say like, I think my default here would be to, maybe only work a little bit on it to bring it to a point where we have it in our back pocket, in case we do the merchants at some issues kind of occur that where it, it becomes obvious that something like this would be helpful, and not actively push for it for Shanghai. If basically there are people strongly feeling strongly in either way, like either, like we should really bring this to Shanghai, no matter what, or like this will probably never be useful anyway. then like, please do let me know, but for now I, this would be basically my default. 

**Martin Holst Swende** 
* Yeah. So, sorry, I, I dropped off cause I fell off the, the network. so I missed a little bit, but I would kind of agree with you and say that I'm currently not yet, not really convinced that there's security concerns needs this to go into Shanghai, but on the other hand, I, I think maybe for correctness, we should do it at some point. And so that's yeah. Kinda what you said, I think. 

**Ansgar**
* Yeah. And it's definitely also, that's why I never even brought that up because I don't think that would warrant like really trying to push for it. But, it's definitely like usability improvement because it stabilizes the base fee. So we have less wo over the, but that's, that's not an important aspect. So it's, it's nice to have at some point. 

**Tim Beiko**
* Cool. Any other thoughts or comments on the EIP okay, well, we might be finishing already for the first time in several months. so, yeah. Anything, anything more anybody wanted to discuss? 

**Greg Colvin**
* I just had a quick question, for Martin and Alex, I think, I, for some reason just noticed that the size of the in code is twice the max code size. That is the in codes at 49152. so it fits in 16 bits as an absolute jump value, but the relative jump proposal is using 16 bits, I think so that it can job positive or negative to cover the max code size of the contract. So I'm not, I'm not sure how that's gonna work Silence. 

**Alex B** 
* Yeah, I was gonna, I'm Not sure I was able to, to follow, but in terms of like in code, the likely use cases that the, the trailing bys are data, containing the return bite code. so you don't really need to jump that far in, you know, in it code use case 

**Martin Holst Swende** 
* And it, it doesn't, you can always do change jumps if you want to.  I mean, it's inconvenient, but it just mean it can't be done. 

**Greg Colvin**
* Okay. It seems this would be easier with EEO F so we can separate the code from the data. and that it's, it's fairly clear that you're copying, copying a piece of code, that happens to be data. but we can discuss that later. Thanks. 

**Tim Beiko**
* Of course. Anyone else? Okay. Well, thank you everyone for joining. and yes. See you out of you next week in Amsterdam. See ya have a nice weekend. 

------------------------------------------------------------------------------------------
## Zoom chat
	Justin Florentine:	Rai we should talk about submarine games at Amst
	terence(prysmaticlabs):	gm
	Rai:	Goddamnit Justin, you’re giving me fomo
	Micah Zoltu:	And my mice is broken.  Gogogo!
	Micah Zoltu:	*mic
	lightclient:	does my mic work
	Gary Schulte:	🚢
	Micah Zoltu:	"If we have time at the end of the call we can discuss X..."           
	Tim Beiko:	https://github.com/ethereum/pm/issues/508
	lightclient:	what net method? sorry if it was said and i missed
	lightclient:	thank you
	terence(prysmaticlabs):	yep, we could just use engine_exchangeTransitionConfigurationV1
	Mikhail Kalinin:	https://hackmd.io/GDc0maGsQeKfP8o2C7L52w
	Justin Florentine:	Besus receipts root mismatch issue is being worked here. We are currently focused on tx 30, around pc 5331
	Justin Florentine:	https://github.com/hyperledger/besu/issues/3725
	Jamie Lokier:	(IIRC one of the ELs keeps 64 recent states.)
	Micah Zoltu:	IIUC, the idea is to have a testnet merge where the validators aren't all on an internal network with each other.
	Micah Zoltu:	So we see things like latency, offline, etc. between nodes.
	Jamie Lokier:	A “dirty network” simulator to create latency, offline etc conditions might not be a bad idea on that internal network.  Seems like a lot of work to set up but could reveal new consistency issues.
	Martin Holst Swende:	are all EL-testnets 'paired' with a CL testnet already?
	Gary Schulte:	Just goerli has a long lived CL testate afaik
	Gary Schulte:	*testnet
	terence(prysmaticlabs):	great idea!
	Justin Florentine:	Besu does this, we prevent Engine on a non-auth port, but today that auth can be disabled.
	Micah Zoltu:	IIUC: The suggestion is to shutdown the unauthenticated engine API.  This is unrelated to the execution engine's 8545/8546 JSON-RPC API.
	Micah Zoltu:	It has always been the plan to do this, just needs to get done.
	Tim Beiko:	Paweł, feel free to go after
	Jamie Lokier:	When code is split for hashing/storage purposes, splitting at data-dependent boundaries (similar to rsync rolling hash, etc), in addition to “natural” stucture, may improve the amount of  .
	Jamie Lokier:	I worry with `SELFDESTRUCT` removal that it means pruned state size will have to increase more than it currently does.  With statelessness that goes away, but _until_ statelessness, it doesn't.
	protolambda:	see you all at devconnect hopefully :)
	lightclient:	w00t
	Danno Ferrin:	Signed 16 bit?
	Tim Beiko:	devconeeeeeeeeeeect
	lightclient:	how much to bribe tim to do bitconnecc reenactment but s/bitconnect/devconnect
	Tim Beiko:	1 eth


## Attendees 
- Tim Beiko
- Mikhail Kalinin
- Rai
- Lightclient
- Pooja Ranjan
- Marek Moraczynski
- Greg Colvin
- Trenton Van Epps
- Harry Altman
- Peter Szilagyi
- Lukasz Rozmej
- Martin Holst Swende
- Bhargava
- Jiri Peinlich
- Sajida Zouarhi
- Marius Van Der Wijden
- Vorot93
- Gary Schulte
- Andrew Ashikhmin
- Fabio Di Fabio
- Fredrik
- SasaWebUp
- Alex Beregszaszi
- Guillaume
- Danno Ferrin
- Protolambda
- Pari
- Micah Zoltu
- Sam Wilson
- Alex Stokes
- Appleyard Vincent
- Henri DF

------------------------------------------------------------------------------------------
### Next meeting on: April 29, 2022, 14:00 UTC
