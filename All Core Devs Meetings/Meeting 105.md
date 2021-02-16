# 1. YOLO V3 & Berlin Client Updates

Video | [3:38](https://www.youtube.com/watch?v=ju92hAKzKcg&t=218s)

**Hudson** - Hello, everyone, and welcome to a theory and core developer, meaning No one of five, I'm your host, Hudson, and today we're going to start off with YOLO V three Anberlin client updates. So I think he'll of three launch. But let's get the latest from James.

**James** - It did launch. I saw messages from Vesu and geth bobbing around was everyone. Any updates on that or on status for singing for the clients?

**Tomasz** - So we just started syncing at the end in mind, we went to the some of the first Bloxwich transactions in town, fixing some of the decoders, have it syncing very soon because all the IPPs out there and it's just the serialisation things for the network.

**Dragan** - We start from the beginning. Yeah, seems fine.

**James** - and that's open etherial? 

**Rai** - Yeah. Mm hmm. And then Besu's in sync.

**James** - That's great. So that went up last Friday. And so now while that's syncing. Micah asked a question, is besu production ready?

**Martin** - I just like to make a note, though. Oh, yeah, yeah, I mean, there's been some transactions in the beginning, but I'm not sure if there's actually been any. Yeah, any transaction allowed to speak of. So it's really nice that the clients are syncing. But I suspect that if we don't really have a lot of coverage from it. Right. From the basic kind of basic coverage.

**James** - And then is that at a point the first testing work can kind of start?

**Martin** - Yes, it's at that point, but it hasn't really started OK?

**James** - I mean, that's good four updates from YOLO. That's good. So upcoming art is doing actually using it for testing and then also doing fuzz testing for testing. The clients are all syncing. We talked a little bit in all core devs this morning for those who aren't there about the possibility of timing for what's next. Meaning scheduling testnet fork blocks and main net fork blocks. And I don't want to, like, really rush into it, but I wanted to open up the conversation so we could start getting an idea of getting some of these things out and about for the for the network.

**Hudson** - While that's happening, we can continue with the conversation. So basically, yeah, we're going to just discuss some of the timing for the fork blocks on testnet and may not. It looks like this morning a few clients chimed in and specifically we were looking like. Test at four blocks, potentially first week of March and the main net last week of March as something we threw out there, do people have any initial thoughts on that? And I can just repeat what Martin said and chat that if the last week of March was the aim for main net, that I'd rather do the test that's even earlier. I'd rather Rush and bork test net than have to sort of test that time and Bork main net. Good point.

**Micah** - What's different between YOLO V3 and roland test net?

**Martin** - Only the transaction I mean, the lope. did I understand the question? 

**Micah** - I think that that answers it. Yeah, we don't have any intention of changing anything or adding anything or moving anything, right? [no]

**Hudson** - Yeah, that's that's for sure. OK, let's see how James back there.

**James** - I'm back. But you asked what I was going to ask so that we can just keep going.

**Hudson** - Cool. And you got some blocks for the midweek first week of March. But if we were to do it earlier, that would be, what, last week of February then?

**Tim** - I guess maybe it makes more sense to go the opposite approach, like how much time do people think we need to just send out a release for test net that I'm just concerned like if we say it's like the last week of February, you know, like, is that enough? Because we still need to every client. We need to ship a release with the blocks sending them, and then every user needs to adopt those. So I I don't know what's like the right kind of amount of time we need for that first step and then however much time we want to see to see it on testnet's before it goes on not. Yeah. So I'm curious that people's thoughts are on that.

**Martin** - Peter, didn't you once publish the suggestion on the rough times for the networks. 

**Peter** - what did I publish?

**Martin** - like the stepping stone towards rolling out the network and like hardfork specification, this is how we should do it.

**Peter** - Yeah, but we never actually follow that. My only suggestion was that's that's different from from the current approach was that we could. As an initial step, we could shadowfax crops then or something, essentially just to create a private network that is attached to Robstein and then just place all the network and I mean all the transactions from Robstein, just minding its own site chain side fork. And then the idea would be that that way, at least we would have some transaction throughput and some actual use case and actual test load be for actually working up some potentially. But that was my most of my view on how to do things.

**Tim** - It feels like we might get we might already be doing some of that with the YOLO networks, right? It's not exactly the same thing, but it's..

**Peter** - So essentially what you're doing is just mining empty blocks. So it's not really testing anything currently.

**Tim** - Oh, yeah. Yeah. But I mean, the previous versions where we did we did some transactions on them right away, but those aren't real life transactions.

**Peter** - That's the problem is that these are kind of some synthetic transactions that somebody dreamed up, but they aren't really stress testing. Maybe just running some. Yeah, so essentially it's just some synthetic thing, the only true test comes when when you start running large transactions and at that point if you for crops then and then realize that there's something wrong, then that means Robstein needs to be rewound or something or uncorked. Versus if you are to create one of these shadow shadowcorx, at least if it goes to be Robstein but it doesn't damage to them. But we don't really have the infrastructure ready to to bridge the two networks and just the transitions and transactions across them, so. I don't think it would be too hard to pull off, but. So it won't be it probably requires some minimal effort that somebody would have to do that.

**James** - Would that be something other than you guys can do?

**Peter** - I mean, probably any client do they just you just need to make a custom client that works on these networks.

**James** - Yeah. Which is we're already doing that for Robstein.

**Micah** - I think this is similar to what we talked to previously about having a fork testnet that we're going to be testing against real state load and you basically need to just fork off, may not have an EIP or something like git on the fourth block decreases difficulty by, you know, many orders of magnitude and maybe change the chain. And if I can just get on with it, I don't think you want change chain id you want to continue to be the same. So that way you replay transactions from Main net on this shadow network so you can or perhaps or whatever you're forking so you can get real transactions like the main net transactions would be playing on this shadow chain, which is just running a slightly different set of rules that in this case.

**Peter** - So come to think of it, probably what you could do is essentially just launch a private network with a different network id that should be so essentially just Robstein Genesis with a network. So that would ensure that clients who want to join in on this hacking network, they are separated off from from the Life Network. And at the networking layer, because that's kind of important, so that we don't start screwing with each other synchronization. And if you can get that done, then what you only need is one single node that is relaying transactions and. Yeah, I mean, we could probably hack that together just to have had a node running on ROPS and then just somehow stream it across to another node, not running across. Maybe just for every transaction that happens on Robstein, just call some transaction Robstein other side. So. That's probably fairly easily hackable together, if you want to do that.

**Micah** - And that can be done by someone other than a client dev. Sorry, I mean, the 4D node transaction, so you wouldn't change chain ID you can only change the network ID and so the network ID would be different on different networks, but the chain ID would be the same so that way all the transaction can be replayed. 

**Danno** - But clients are set up to reject transactions that don't match the chain ID.

**Micah** - That's right, and so the chain chain I.D. match for Robstein and Shadow Robstein but Network I.D. do not match for Robstein and shadow Robstein.

**James** - In general, that sounds like a better direction to go to. Is that something we could do in the next in the next two weeks is how could that be done? And then look at forking Robstein the week after that.

**Martin** - So I think I think doing doing this might work pretty well, but it will be kind of like a. Since since probably some transactions would fail, that's 16 or Robstein. Which will affect the state and the state changes will. Kind of snowball and eventually nothing would work.

**Tim** - Is there a way we could test something like this, even if it was not for Berlin like. As kind of the equivalent of the YOLO networks on and on the next time around, so instead of launching empty networks, we basically launch Shadow forks. Because it just feels like it might work in two weeks if, like, everything goes right the first time, but given we've never done this, I can see it pretty likely scenario where it just doesn't work like we expect it and it ends up taking much longer. And I'm wondering if instead of maybe doing these YOLO networks next time around, something like this might be more helpful.

**Peter** - Well, I guess the thing is that Martin also mentioned that probably the networks would eventually diverge simply because you have a different miner on some transactions to get included in front order. And that means that we create one of these shadow forks then fairly quick. So I don't know how how fast, but eventually the networks will be so much diverged that the shadow fork could just be reverting transactions because. It would have just a different state than all the transactions would be doing stupid things.

**Micah** - That's my hunch, but I do. And I think the hunch is correct. I don't know. I also don't know on the how long that will take, but I think if we can make the process of creating a shadowfax easy enough, then we just run it for two weeks or a week or however long it takes to kind of diverge sufficiently and just reset. So we reset to the head of then redo the whole thing and we're back on track. And you're back to synced basically.

**Peter** - That could be done. The only annoying part is doing the initial sync, so synchronising Robstein or. Even girlie starts to have weight, so. If you have to reset every two weeks, it gets annoying.

**Micah** - And so definitely much easier for people or teams who already have, like Robstein running because you can just copy old folder basically or your whole database and then just change that. We're ready and move on. It's much harder if you're not syncing Robstein already for any reason.

**James** - It would be nice if we could if the next YOLO could be. So is the problem that currently YOLO is great for testing clients, but it isn't great for testing what's actually happens with data? So the shadow forking Robstein is would be able to test like real live data. Is there something we can do to Yolo that would also have that thinking and thinking forward? Is there something we could do to YOLO would have that same property? [no] So I would need to be either one of those to, like, not doing you a little.. you were goin to say something, keep going

**Peter** - The issue here is that you need. That's all the all the networks, even the test network, it's constantly evolving and the transactions are constantly changing. And even if we somehow try to build some. Some pool of transactions to test things with, probably it will get outdated fairly quickly. So that's why I was saying that usually just latching onto a live network is always getting the juiciest stuff. So we've I think there was a time when I'm not entirely sure which hard fork, but there was a hard fork where everything went perfectly for Robstein when we forked mainnet it blew up. And I don't remember which one. Or maybe maybe we realized that it could blow up and it never did blow up, but there was some issue that even in the past where some fork wasn't properly tested by not even Robstein. So that's why we're kind of reluctant at YOLO is it's kind of cute just to test out the synthetic tests, for example, tests that are included with EIPs just to make sure everybody seems to handle the forks OK? But the real test starts the with the test nets. Which we previously broke. We can try not to break.

**James** - So doing the Shadow fork could make it less likely that we break Robstein.

**Peter** - well, I think will be one more data point that things seem OK.

**James** - Yeah, yeah, it wouldn't be conclusive. So is it worth trying to hack together the Shadow fork thing this time or just moving forward with doing a block on Robstein and saying, OK, let's fork.

**Micah** - if the client teams think they have the bandwidth for it, I would say it is worth it to do it sooner rather than later, because I think the same technique can be applied to shadow forking mainnet, and being able to test real main net that state real main net transactions, even if it gets out of sync in a week that is hugely valuable for reducing risk for final launch. So I think this general avenue of testing gives us a massive gains, in my opinion, in terms of real world testing that we're never going to get from Robstein or Cofan or Garley or any Yolo network, like we're not going to achieve that. And so I think this is a path that we should try to do. And the sooner we can do that, the better, because risk mitigation is good. But that being said, I'm not a clint dev and I don't know if you guys have the bandwidth actually do that in parallel with the current plan.

**Martin** - Yeah, I mean, I, I agree with. With the assessment that we have bandwidth, uh, it would definitely would be preferable, um, but then I also think that maybe we should just. Yeah, yeah, I'm usually not very careful about the testnet, and I think we should use them for testing, um, and if they bork, so be it. And so I would prefer we just go ahead with it, but that's just I can see that other people may think otherwise.

**Peter** - Well, just to give you an example of why I think it's problematic is because, for example, currently I'm not entirely sure whether the project is still or not, but reddit was doing a pilot project of this community tokin or whatever they called it, on top of rikavik, and essentially this means that reddit was actually running production systems, even if just by the production pilot project on Winkerbean. Which I think is somewhat forcing or pushing the limits of winkerbean, I kind of think it's somewhat still within the realm of acceptable use.

**Hudson** - Even if it wasn't if they were using test nets more than test nets, we can't really stop people from doing that if They're going to do it.

**Peter** - Of course, if somebody is running some full production thing and we have to break it, then I won't have sleepless nights. But that doesn't mean we shouldn't read carefully so that we don't. Break it to two easily.

**Hudson** - Yeah, I think that it would be good if we try the new Shadow fork approach and then push the test net for block one week out from the last week of February date. So it's the first week of March for the first week of March for test net for Shadow fork one to two weeks before that. When it gets done is how I think it would be pretty cool unless what would we be able to get that done and the next Two weeks.

Decision 1 | Video | [~24:57](https://youtu.be/ju92hAKzKcg?t=1497)

    Don't do shadow fork approach, make note to revist next fork as it's a better testing method but would require too much time right now and that time is better spent elsewhere

**James** - If it's something we had bad moment for for doing by the next call, then I'm like, okay, it might be a good idea, otherwise, I'd say it's worth doing it for the next, like realizing that this is a model we should implement for the next fork.And I built that into that process.

**Peter** - My guess is that we could have something together here. The catch is that you want the Shadow fork, Robstein or Main net, then we need a special fork flag to be able to nuke the difficulty out, obviously, because if we shadow fork main net, we don't want to have a mining boom behind it. So that's that's an extra feature, so besides changing that work on somebody implementing the breach, we also need all kinds to support this new kind of the difficulty. And if you want to show for the Winkerbean for Girdling, then again, we need a special flag in the clients to forcefully replace the authorized signers.

**Tim** - Which I feel like that will take much more than two weeks, like it'll take, you know, maybe it's easy to implement, but we need to test that the different clients do it right together.

**Peter** - Yeah, so so Robstein and main net. It's probably easier because changing the essentially it's just an extra fork rule which just drops the difficulty. The rinkiby and girly nets might be a bit interesting because you have voting because they have some problem with the votes across this vote threshhold.

**James** - Would it would it be OK if I'm like I'm envisioning the coordination of getting all the clients on to this would kind of be hard, but if we had just even one client or so go through the process so that we could set up the process for all the clients to join next time. Is that's still valuable.

**Micah** - I think so, was about to say the exact same thing There is any of the clients feel like they have lots of breathing room compared to the others. Maybe is the real question. Is anyone out there like, man, I really wish I had more work to do, or maybe it's it would that be?

**James** - So if like the geth team would want to do that with someone else, want to join them on that, or would it be OK if 

**Martin** - I guess for me personally, I would rather spend the next couple of weeks on the whole thing and then setting up to actually..

**Hudson** - Yeah, and I'm not hearing a lot of other clients talk about their love for the idea, I guess. 

**James** - So if someone wants to do it, then they should speak about this and speak up now. Otherwise, I'd say we should move forward with the fork Robstein and then realize that this is the better thing we should do next time.

**Dragan** - Then I'll be quiet, if you could, the idea is good, but we don't know by how much time we will need to properly do it. There is a lot unknowns this plan and bring this subject to. Maybe it's better to leave shadow fork for the next hard fork that comes.

**Hudson** - Ok, I mean, that sounds good to me personally.

Decision 2 | Video | [~29:38](https://youtu.be/ju92hAKzKcg?t=1778)

    All clients should be ready for testing by the goal date of February 24th; clients ready next ACD for fork of test nets; choose block 24th and clients can choose accordingly how to handle that

**Tim** - So I guess then we're back to the original question, like, what's the timeline we want? What's the delay? We want to give people to have a block on testnet's, you know, what's like an acceptable delay. And this is what I guess first week of March is what was originally proposed, and I thought like four weeks gives all of the client teams one or two weeks to ship a release which has a block, and then it gets, you know, two to three weeks for everybody to upgrade. Do people feel like we should do quicker or slower than that, or is that generally fine and then we can. I think it's fine that we can set the main block. Know if we want to have four weeks or six weeks of testing that we can just set the main net block farther in the future. And it's not like we're going to be blocked by working, but of working on anything else in the meantime. Right. Like the testnet that there's just going to go along. We'll see it happen. Those issues will fix them. But I think I'm just a bit cautious of like us also breaking the test. If we set a block that's like in two weeks and then half the people haven't upgraded.

**Tomasz** - From our perspective, it's fine to rush it a with more.

**James** - Rather rush, so would it would rushing mean that we do the testing..

**Tomasz** - Yes, doing Robstein testing but not mainnet. So if you if you want to push for February, then we are totally fine with the.

**Hudson** - Yeah, I'm feeling like there's more value in having more testing time rather than waiting while worrying about the risk of a Borked test that. Or that people don't get on fast enough because. Yeah, I think there's more value in more testing time, but I'm feeling like.

**James** - So could the could all the clients be ready to fork Robstein and all the other ones in two weeks, so like next all core devs call, we have all the releases ready. So then we could have it be the middle of the week after that. [agreement]

**Tim** - So we're aiming for like the 24th. That would be like to say it's like midweek, it would be February 24th is when we'd want to target the fork block for the various testnets. [agreement] And I guess we can hash out the specific blocks, I think, on the chart, find some nice blocks on every network. [agreement] And do we want to so I guess do we want the release to also have the main locks, the main blocks in it? And if so, it would be helpful to just have like a tentative date for which we can also find a block.

**James** - The block. Twelve hundred and twenty one and what number is that, 12 million? One hundred and eleven thousand is Wednesday, March twenty fourth.

**Tim** - So that would give us a month, a full month, literally day for day of testnet being live.

/////////// 33:25

**Dragan** - One question, the block, the test, that's how the client users want to go to the older version. It would be more safe to to have two versions of the clients wanted the blocks be tested, not the one Whitlock's feet Meinhardt. I'm not sure how he's coming to pasta dishes done, but. If you have problem with testnet then it'll probably propogate to mainnet.

**Hudson** - And someone else had something, was that was it, Micah, or are you 

**Micah** - I was just saying that this is a decision each client make individually and we have a tentative date for May not a client can decide whether to release that in their production and clients or not. It sounds that people don't want to, but we don't need consensus.

**James** - Yeah, we can we can wait on the line, but if we do the for the 20, what was the date we just said the 24th, the twenty fourth then last week of March is pretty realistic. We don't need to really set up for block date now. But that as like a target makes sense.

**Tim** - So that's I guess it's it's then a question like how how early in advance do you want to have the releases out with the block? Because I know, you know, there's a lot of folks we talked to that would rather not, like, upgrade their mainnet for client a week before to Fort. So that's just kind of the only thing to consider, because there's not only just the consensus changes that go into the client list, all the other updates. And so having a version that they're somewhat. That they've run for a few weeks to know that there's not like another issue is important. So, you know, it's not like the end of the world, but I think we we it's a bit unrealistic to say we fork the testnets on the twenty fourth of February, then on the next call two weeks later or whatever, we decide the main net block and then we expect everybody to be ready for a main net fork two weeks after that.

**James** - If we did the main network in two weeks, is that still?

**Tim** - Yeah, I think that's definitely better. Yeah, and it's fine then if it's two different versions of the clients or one, like Michael said, you know, different teams can make the trade off there. But yeah, if I think two weeks from now is fine, but like four weeks from now is probably cutting it very close if we want to to have a release and have people have enough time to actually update.

**James** - So then that would that just summarizing for no take her and the rest of the call on the we would have clients be clients, be ready next. Operatives call for a fork of the tests and then the twenty fourth we would choose a block for the twenty fourth and we'd also choose a that block that day. And then clients could decide accordingly how they handled it.

**Hudson** - That sounds good to me. 

**Tim** - Yeah, so we should choose the that blocks before the next call, though, right? Like we know it's four and we can choose the blocks, you know, basically today on the job. But then on the next call, we can choose the main block.

**Hudson** - Unless clients want to bundle both into one release. But does anyone want to do that or like I should put it this way. And does anyone need the block number before the dates we just proposed? Yeah, I didn't I didn't think so, I was just going to check.

**James** - Then I'd say that's good for now on that. And we can move on to the other things, unless someone has less thoughts on it or wants to share, let's say we've taken a good amount of time today.

# 2. Finalize ETH/66 Specification
Video | [37:44](https://youtu.be/ju92hAKzKcg?t=2264)

**Hudoson** - OK, thanks so much. All right, finalizing the ethe sixty six network specification that was discussed a little bit in chat and it looks like some clients had opinions on. When to when to finalize it, I think I was getting at or can someone summarize the discussion?

**Martin** - So you six or six request like these two messages need to apply, not all of them, because there are also things like announcements which are not requested, but all the things which are on the form request reply. And of those messages, all of them except one, are currently you make a request and the response is a list of things, but one is a bit special and it's to get block headers, which is a request which has a four or five parameters, um, and the current specification and wrapping thing, so that all the new messages are already being coded as requested and then a wrapping of the previous format. And the observation was made by Peter that we don't actually have I mean, for the things which are just the list, we we do have to kind of do this wrapping. But for this block headers, it would be nice to just add the request id alongside or before the other existing fields. Um, yeah, because the reasoning being that it was lower on network traffic and a bit smaller and and that's kind of the discussion. 

**Danno** - So my concern is I think we're overfitting for a little bit of network traffic overhead, the pattern of the with the IP came in initially was you take it 65 packet and you wrap it in a list, which is being done with all the other lists. And for that one packet there, it's an overhead of like one or two by one or three bytes at most. The impact comes into the clean implementations. If you're streaming from the ERP data, you'll be fine because you just read if you're in 66, just read the header and then read the rest. But I see that there's other clients that do an index based read of that particular packet and they're going to have to write significant fork code for that to read the packet twice or two different ways. So from a from a design perspective, keeping it consistent is good. And it's also going to have more of it, less of an impact on the client code if we keep it as specified so that the author has a preference for this. I have a preference for this. It's not a whole I'm going to die on, but I really don't see the need to to make a special case for one packet.

**Martin** - Right. Let me just add to that, actually, so people go there and we don't have the streaming of the original implementation of the spec was slightly cleaner and the implementation where we have to marshal it so marshal it differently is actually slightly uglier because we have to create a new type of message and marshland and stuff. Um, so, I mean, we didn't go this, uh, we didn't don't prefer the smaller network because it's particularly nice for our client. But we and yeah, it was worth it anyway. But I think, Peter, you're the you're the main proponent for the. Do you want to speak on it.

**Peter** - So my main issue is that it seems we're kind of designing the spec backwards. So we just look at how clients implement certain things and then we make a network protocol that tries to adhere to the existing code as much as possible. And my biggest problem is that that is a very slippery slope on the long term, because then it means that instead of having clean network protocols are not what protocols will be full of interesting quirks just because at some point or another there was one client that implemented it this way or that way. So from that perspective, we want to add that. So currently the eth packet. I mean, we have a bunch of requests. And for example, there was a time when we wanted to add a new fields to the eth handshake. That was the fork id and that was just simply added as an extra field. And so my question is that if we just added it as an extra field there and now we want to add the request id, I mean, why is the request id more special and why should all of a sudden we add extra wrapping just because. So if the for id didn't require wrapping, then adding the request id seems. I mean, it just seems that we're not catering preimplantation instead of.

**Artem** - Actually, it is much cleaner, cold to add, requested as like a separate field and like the rest of the contents of the packet as a separate list, because, like, I'm just imagining this in glass terms, it is much, much easier to guess much, much easier to implement because I can make like a wrapper structure with two fields with, like request ID and some generic request, basically. So this just does separate separating request IDs out of the general list. It is. It leads to a much cleaner implementation. And I think that that should be the way forward.

**Peter** - But why would you want to separate them implantation away from everything else?

**Artem** - Like I said, because it is simply a much cleaner code, 

**Peter** - but if the code, that process of the request we are required to request, by the way, then what did you say? By adding an extra wrapper in its envelope?

**Danno** - separation of concerns when you're matching up packets that separate code from processing the specific package. So if we unwrap the envelope and we have the list of whatever we don't care about in the request, that we match it up with existing and coming up and packet, that has nothing to do with whether requesting hashad I.D. ranges on transactions, the process that matched that up at that further down and we isolate it. This is the sort of envelope and that's in another protocols. The concern of what the other custardy matching up or not is, is disconnected from what the actual content of the packet is now about. For Guidewire, different Forcades was put at the end of the list, not at the beginning of the list. So the request was the end of the list. There would be less resistance from me. But putting at the beginning of the list doesn't match existing pattern when we provide what our packets look like.

**Peter** - So, yeah, my only difference I can say is that the peer to peer and we do not have a notion of headers or or non-headers that would, for example, that they should be brought all the other protocols, explicitly layouts that you have, the metadata fields in the headers and then you have the content. There's no such notion of that. And essentially this debate is introducing it. But we are not really naming header, but kind of treating it as a header, so it just seems we're making a design decision and being unaware of it 

**Dragan** - It's easier to separate its request I.D. and rest of package, because we want to check device ID, you would check it in the first layer of your application and just sent rest of your package. It'd be easier, we wouldn't say I'd  model my code to handle both cases, but to wrap up everything.

**Peter** - All right, so I just wanted to add this, that this is exactly my problem, that none of us are approaching this, that what does it make sense? How does it make sense for this stuff to look like? What we're approaching it from the direction of, hey, I have I will implement it like this to let's make the network Beckert. Easiest tool in the process to consume with the code I would write it with, and that's not necessarily a bad idea to keep that in mind. But I'm not a fan of designing with a foundation in mind for. But maybe I'm wrong here, so.

**Micah** - So so I started out on the side of most of you guys here, and I was convinced by one particular argument that I think Peter or Martin made, which is that by the time you get down to the request I.D., you've already narrowed what you're going to handle and to exactly one packet. That is to say the actual header is higher up the stack. Like You get you get in a payload off the wire and you find out what the message type is. And but once you read that message, then you know, the exact thing you're going to do here is that there is no more like like these are not actually like packets to go together like that are coming in through like one funnel. These are already dispatched, like you've already dispatched them to their final destination. There's no more like, OK, I've got four different packets coming in through a channel that's, you know, I know to dispatch. You've already dispatched them by the time you receive it, by the time you get that request. And so that was the convincing thing, is that it's just the key there is that you've already dispatched this down to a single handler. Like you do not have multiple handlers at this point anymore. And if the request ID you higher up the stack like before that message type, then I would agree with everybody else here that we should be, you know, having an envelope type thing where you have the request ID and then some arbitrary payload. But we have to have a message type and an arbitrary payload message type to our payload is a one to one mapping. There is it's not a one to minute.

**Martin** - I think that's a pretty good observation, and I think we've heard from all the client devs with the exception of nethermind, do you guys have any thoughts or opinion?

**Tomasz** - I'm quite and I was looking at the request of these approaches, changes, various changes. Everything seems to be all right. And I'm OK for you to design this one.

**Hudson** - What other opinions are there on this, because I'm I guess I'm I think are there are two concerns right now. I'm a little lost.

**Martin** - I mean, you know. Well, I mean, it's just the decision that needs to be made. I think no one is ready to buy on any deal. Um, I guess geth, we're ready for one approach. It sounds like nethermind is ready for etiher. I think that that sums it up.

**Hudson** - Yeah, does anyone disagree with that one. Or with Martin's assessment? All right, this is when we pull out our coin and flip it. No, I'm just kidding. We're not going to flip a coin to decide this.

**James** - Is there someone from network design philosophy we could ask or like reach out to.

**Martin** - No, I was just trying to decide something here and now so we can just skip it.

**Hudson** - Yeah, it's an implementation issue more than any kind of network design issue, right. Or like per per client implementation, how they've handled it in the past, 

**Micah** - I think I think that's exactly the debate. Is this an application question or is this a design question?

**Peter** - But and that's a problem because a network design question at the foundation of it.

**Hudson** - I guess I meant because of how people have designed it and their client implementations before it's turned into that, is that not true?

**Micah** - I think it's more how people have designed it in their heads, sort of, oh, OK, what do the people who has a mental model that has X and so people has a mental model that is Y, and those two mental models have different desires because in order to change sides, you have to change your mental model to match the other side and set requirements, of course, much harder to do. So neither side, of course, wants to change about the model because now thinking becomes harder.

**James** - And your reference, Micha, was the other one, like if you were to have one, I just read that light-client said he preferred Peter's proposal.

**Micah** - I originally was against Peter. And then I was convinced by the equal one to one mapping that occurs higher up the stack. So this is not one of many mapping which like the current way, the EIP as written, makes it look like it's the sort of situation or one of the many mapping. But in reality, if you look at the broader protocol, it's not actually. And so, again, that was what convinced me.

**Danno** - Then are we putting this in the wrong place with the payload, should it be up with the message?

**Micah** - So we talked about this. The feeling I got from the conversation was that everybody kind of wishes that it was more like that. But it's a much bigger change. 

**Peter** - But if we're arguing correctness, that's the correct answer. I mentioned we had this discussion on all core devs channel two that you cannot really moving higher up the stack because so the the naive idea or I wouldn't call it naive because that was also my first impression. And the first impression idea would be that, hey, we can just move it up into a stack and then problem solved. The request that these are handled at the higher level or deeper level already preferred by the peer 2 peer itself. The problem is that then you end up with a really, really bad can of worms because on one side request, that is one for request packets, but because network packets which do not follow the request reply packets, for example, transaction propagations, those are just not directional packets. So you don't have the request ids. And the other thing is that if you essentially the whole point of request I.D. is that you make a request and then when a reply comes, you can funnel it back to the original piece of code that made that request. But that also means that you need this multiplex at the multiplex to constantly track all the currently active requests. Now, if you move this request tracking up into the p2p, it means that you have some B player tracking mechanism which needs to be aware that, hey, this sub, this program module is waiting for a reply. But what happens if the reply never arrives? Then all of a sudden it needs to start caring about cancellations and timeouts and whatnot. And that's why I'm saying that that is a huge can of worms to dump onto the devs.

**Danno** - So we're back to having implementation without the actual details.

Decision 3 | Video | [55:12](https://youtu.be/ju92hAKzKcg?t=3312)

    Keep EIP 2481 as it is on EIPs Ethereum org -- not accepting Peter's proposed changes

**Martin** - Yeah, in that case, unless anyone has changed their mind, I would consider this being I mean, that we let the specific case as it is and not change the thing that we agreed upon back in the day. How does that sound to you, Peter?

**Peter** - Yeah, I can always make my eth/66. 

[Alex Vlasov speaks russian, lol]

**Hudson** - OK, so what is the other clients think about Martin's proposal. Is that something people can live with, is that something that people want to try to find other ways to come to a conclusion or Vito?

**Artem Vorotsinkov** - So the proposal is EIP 2481 as it is on EIPs Ethereum org (repo) right now.

**Martin** - Yeah, well, I'm saying is that we propose to make a change and we're getting some pushback and I guess we'll consider the proposal to change it and not accept and yeah, so.

**Artem Vorotsinkov** - The current the current EIP looks good to me, I say we should take it and implement it.

**Danno** - Agreed. I could take it any way as long as there's a firm decision on it.

**James** - so that's not do not accepting Peter's proposed changes.

**Peter** - Yeah, I can live with. no, so actually, so what I was saying is that essentially this whole these protocols are not set in stone. And if we want to involve them in the future, if it turns out that this was a bad decision, we can always go back and just do it another way.

**Hudson** - Oh, that's nice, then. Cool. All right, I think we've come to a decision on that for the note taker, let me say the decision and then someone correct me when I'm wrong. We are going with up to four eight one as it is written today without any modifications to the PR.

**Peter** - I have one slight request for a modification; the EIP mentions that this particular spec is consistent with the request of pairs in LES and that statement is not entirely true because LES has some different methods. And my suggestion would be not to refer to at least one thing. I mean, in the discussion and the rationale session. Sure. But once that's specking it out, the spec should not refer to other specs because then the whole thing is clear. So let's just drop that single line.

Action 1 | Video | [58:15](https://youtu.be/ju92hAKzKcg?t=3495)

    Martin to drop comparison with LES in EIP 2481

**Martin** - Yeah, I also I mean, I have an open door to modify the spec and I'll change that before so it doesn't change the specs. But just as a test case for the publication.

**Hudson** - Does that sound good to everyone? Is there anyone opposed to dropping that line and maybe Martin cleaning it up a bit but having the same content?

**Artem Vorotnikov** - I don't think it needs to be discussed, really, let's just move on.

# 3.1 EVM 384 Update

Video | [58:34](https://youtu.be/ju92hAKzKcg?t=3517)

**Hudson** - Sounds good. All right. What we got next is EVM 384 update. That'd be Axic, I'm guessing.

**Paul** - Axic can maybe do a better job than me, I put the post up, so maybe I was prepared to give up, so maybe I should, but it's exec wants to give it. He can get it, either one. I will give it the I'm giving an even three to four updates. I will talk about our gas cost documents and then an up research post. That I'm trying to bring attention to a recall ABM Treaty for proposes three new codes which cover bottlenecks of a large class of crypto. And it will allow user deployed fast crypto systems, the word fest means if we remove the overhead of the system, namely the interpreter loop and things like this. We would approach speed records and limitations, but we do have some overhead in the system and things like that, so we're doing the best fast. I mean, we're doing the best we can given the system and there are ways to improve the system itself. So there's potential. So first I will talk about.

The gas cost update's jointly authored by Povo exec Casey Jordan de. In case you haven't read it, I'll just read the main points. I won't go into too much detail. By the way, the links are in the issues for this meeting. So we give a background guess. Yes. Has some inherent limitations. Gas's attackable. So these sort of play into our design decisions, for example, that we want simple consequence, gas costs. We propose to guest cost models, oh, by the way, the gas cost model is a systemic way to assign gas costs to an upgrade. There's a model which has some machinery, maybe includes some heuristics, security analysis. And in the end, there are some maybe systematic way to to drive the gas cost for giving up growth and our proposed costs for even three to four upwards, which are EDMAR three to four. So much for more than three to four hour. We have to muddle the aggressive model costs are one one three, respectively, and the conservative model gives cost two to six respectively for those three outcomes. So based on these these proposed costs, based on these models, we do that experiments just to see what they mean in practice. So we apply these gas costs to metering heavy cryptography, but they are a baseline implementation by baseline, I mean not optimized. And the design decision is if if this optimization brings too much complexity, don't do it. So we noticed bottlenecks in our experiments.

And for example, the implementation optimizations that I mentioned, but also some of codes are used very much and they become one of the bottlenecks, for example, push and dupe as well. But in particular, push those. I'll talk about some ways we can get around those bottlenecks. Also not very notable as memory manipulation, mem copies. We copy Buffer's from one place to another. We do it naively with a modem store. There are other ways we can do it. So there are there are ways to fix these Uptons these these bottlenecks, for example.

And a new company or McAfee would save thousands or tens of thousands of guests, maybe another hour maybe.

I'm just giving some examples. You can read details. Imbursement three four would be a candidate for a new. Because there are three output's plus minus times and inverse sort of corresponds with division, so maybe there would be some it would be sort of justified and nice because we have we have four operations, but I'm not convinced we need it yet. So but but there are many options. There are more sort of aggressive options to remove these bottlenecks. One of the main ones is repricing. Now there are simple reprices and more more involved, replacing the involved ones will require, of course, a model many Benchmark's arguments, security analysis. But the major reprices would benefit everyone a lot, even the minor reprices that are not controversial, which will benefit people. And there are other things we can do, including major changes. But these are more sort of significant and risky concepts. And we're not dependent on these changes. But but we we're exploring them to only two of them. One is using immediately. Right now, the only good with the media are the push of codes. And if we had immediate to even three for our codes, we would remove the overhead for setting up the the, I guess, execution context of each upload.

But this could require this could break some old contracts that were implemented naively, but they were still implemented. So it might break semantics. So we might need versioning to IBM, which we don't have yet. That's a that might be a big discussion and a huge topic. Maybe we're doing, maybe not. That's up to other people to decide. Another one that I will mention is called particle gas costs. Maybe other people call it fractional gas cost. That gives us a higher resolution. I think of it more as gas rescaling. So maybe multiply gas times 10. So we have a finer resolution within the execution context. And then when we leave, we sort of round down or whatever, or we divide by 10 and round through the floor. Something like this is again a major change. Clients have to be very careful, of course, about security. But these are there's a lot of potential to remove these sort of system overhead bottlenecks.

Hey, Paul, real quick, I think we had a hand raised from Martin, if we could just get that question in. And then we have about five more minutes on this topic till the next one.

That's my how I raised my hand, because I didn't want to interrupt, really. You do want to finish just one of them? Oh, yeah, sure, we're done.

I don't have much left. So we have figures based on all of these sort of various options. We don't want to be aggressive and say we must do this. We're dependent on this. But this is open for discussion. Some of these more aggressive ones, certainly we wouldn't we wouldn't want to want to even.

We want to have a big discussion with everyone involved and we can come together to a conclusion. And I want to bring attention, so I mentioned fast crypto systems before, but I want to I'm sort of re-evaluating this because I have I'm trying to bring attention to other research post called Serving for Free Competition Methods and Cryptography for Help. And I think we can design new algorithms. So right now we sort of adopt algorithms that we use locally and just put them on changeups word for word. We just translate them to IBM and we and we do the operation, actually. But in fact, we can perhaps come up with new algorithms. There are different constraints. So we notice that unchanged we have different constraints than local. And what I call computational methods take advantage of this, that we can take some more time to sort of set up the computation unchained and then we leave just the very minimal parts unchanged. So we partition algorithms into two parts. And I gave a bunch of examples, one of them just to give an idea, we have a five if we versus on chain or off chain, just by designing the algorithm in a way that we just do the hard part off chain and just leave the unchanged parts of just the smallest possible. And I'm trying to bring attention to to this other research post. And we will move to Questions Hudson and.

Yeah. Thanks.

So what I was wondering, so I have been positive towards even three to four because it was my, uh, I understood it as being a more secure and minimalistic approach to letting the lower to do crypto stuff. But I kind of get the impression now that that. May not be the case because it would go with even three to four. There will be lots of other things that we also want this kind of repricing of fractional gas prices and like localized fractional gas prices and like large changes, which like in the end, the will when we reach there, we might have a lot more complex system than if we just went for the pre comp.. So what I'm wondering is. Are there any other dimensions where you think that even three to four is a better brings more than going with the pick apart approach and it sounds like you do think the new systems. Yes, just wondering, aside from this simplistic thing, is that what the benefits are that use the advantage for over six decompiled?

So I don't know much about three compilers, I'll just talk about even three to four user deployed innovation. I mean, who can who could have foreseen crypto kiddie's and. Sort of when you give users the opportunity to or the ability to commission permission to innovate, I think some some surprising things can happen. So, Martin, there's a if you build it, they will come element to it, but there is already potential in my research post to design new algorithms and things like this. What will where will we be, Martin? You can ask other questions, know what is the world look like with Ethem three, four and without even three to four, where will we be in ten years? What will be obsolete in five years? These kinds of questions. And I think that even three to four will not be obsolete in 10 years and it could create a renaissance. We already have interest from photographers that want to want to implement their crypto systems. And even so, there is potential. But I don't want this to be overpowering. The system is itself. The stability is very important. So the court does know what's best. I can only say that there is there is potential, but I don't know what the decision should be. I'm just here to get some ideas.

I think I can make a like a proper comment to Martin.

I have one very specific case in mind when not even strictly ready for this inability to work on the elements, which are roughly like two hundred fifty eight, maybe two hundred sixty beats like daughter may be handy in the future.

Others in this, I think in ten years everything which is which we have now will be obsolete anyway. And. It may be handy, but it still doesn't neglect the fact that hyper optimized, especially for your list of three to one curve in the recompile, which will be de facto standard for E 1.0 and 2.0 later on, based on maybe a single celebrity is still a great case. But I believe that in 10 years. Events three differ in its current form, will be useful, but not for building such a complex krypto systems which we have right now, not like trying to make it very primitive in the US, a smart contract, but for more like simple cases when you actually just need to do more to take over the modules, which is a little bit larger than 256 bits. And you will need to do maybe like of operations like this in order for Perec, which is potentially thousands like Townsends for them.

So this is more or less my point. And at this point in 10 years, there must be discussion like, well, guess how we implement an efficient, for example, latest based algorithms, which models we choose to make it hyper optimized because everyone will want it. So it would be good to have it, but not like, well, let's wait for another two years to implement fractional to no other optimization gas changes and everything to make it even viable compared to at least one or two specific recompile.

One quick comment by when I say even three to four, I mean the ABM Treaty for family of codes. So there's already interest from cryptographers for EVM seven sixty eight, which would be just precisely modeled on IBM.

It for the same reason of like one specific recursive case.

Yes, you can have it would be great to have. But such approach I still believe, I believe will be obsolete in 10 years.

Ok, so we've got to wrap up this piece so the two oh, could I just get one question, Alex, when you say it's you need replacing to make it feasible, I don't really get that. The repricing and all those, you know, other work items are useful, but they are not necessary. And that work, if any of that work is, it just depends what you take feasible.

I don't think a feasible at times difference compared to such hyper optimized pre. Compile your demise 100 times. Sorry about the I don't think it's a hundred times. I just think the country is divided at three points over arbitrary points is exactly at least ten times.

It's like even in the hyper like optimistic price case when you had your oldest limitation, maybe less optimized, but you had one for every multiplication which I tested by myself and which I presented in the previous results. So this is compared to the pure naive execution time of your test routine, which I had accessible in the go repository years ago for the guesswork story compared to what I was able to run for last implementation.

So just being conscious, what Hudson said, you know, that over time, you know, when you say it's ten times, if you look at these prices and if you compare it to the suggested price of the pre comp., it's not a 10x difference. So I'm not sure what exactly you're talking about. But what I want just to chase the cost is not get. Could I just finish, please? So what I wanted to say is that if you do any of these repricing so many of these extra proposals, that wouldn't just benefit even been treated for but would benefit even in general.

Well, two hands up for repricing of everything, which is not properly priced and potentially inflates the gas cost by users, but it seems like people are overly skeptical about having multiple implementation of the same recompile. And in principle, there is a precedent set. Well, there is a celebrity for a signature education. If everyone agrees to use the same library for like three to one as a reference for for an EVM to avoid forks have the same behavior, even if it may be inconsistent to the end of the day. Well, that's an exception, but we can live with it then. If you compare it to this one to the one which is hyper optimized, not for generic case, not like a legacy of nineteen sixty to collect the proper special one for this curve, which is a part of the frequent flyer proposal, single curve, then it's ten times compared to my like. Kind of pessimistic estimates which are written right now, and it's a pretty simple proposal with aspect. Well, we don't take only this closest one or two hostage libraries, but we take any from these in the least that will not be 10 times and still will be two times.

So, yeah, we've got to take this to the forums. I'm sorry, guys, but thanks so much, Paul, for bringing this and everyone for commenting. The two links are in the agenda and it's under Paul's comment. I don't know how many down there. Yeah, Paul's comment has both links, so. Yeah. Next up is 15, 16, nine performance test updates. I think that's Tim.

Yeah, I have a quick update. Can I share my screen actually? Yeah, sure. So just to give some background, one of the concerns about fifty fifty nine that was raised, if you times on this call, is whether we could actually process blocks that were up to 200 percent full. So 50 that allows blocks to go over twice whatever the the myth is.

And so we wanted to test this out. And the way to do that was not shallow 14 minute.

So we took a slightly different approach where we built the tool that can generate a new network from scratch with an arbitrary state size. And the way we do that is we just specify how many accounts and how. And we create a new smart contract and we specify how many storage slots we want to fill in it. And then we also built a tool that basically spans the network, which a large amount of transactions.

So to get roughly the that size, we set up a test net that had about a hundred million accounts and one hundred billion storage slots and the smart contract. And then we think for base you forget nodes running fifty nine on it and basically span the network for almost two hours using one second blocks and each block having 20 to 80 million gaspare block. This was kind of our first dry run of the test we were happy to see Basswood get did not crash I. I've linked the actual data in the hack and if anyone wants to have a look. But next week, next week, we're going to do a more proper test. We'll have met the mine along and try to monitor the node as we're going. So I guess my one question was like, is there any specific metrics or data that people would like to see from this? Yeah. To just assess kind of general network stability, as will be kind of monitoring it a bit more closely that the next time around.

Can it be a little bit related to the discussion with the amount of empty blocks, because if you have a very large box and potentially like you still have a probability that you will mind an empty one during processing the previous one. So can it affect your results a little bit?

I mean, you can, but to what what would you like to see, like whether the fact that we have big blocks?

I will decrease the amount of like if you have a big box, then you will have like more empty blocks, which on average will decrease, like it should decrease. I guess that much to some like stable level or.

But are you saying this is about the block processing or with regards to the transaction fee. So are you saying because we have big blocks, they propagate slower and like we start building just on the header and then that's resulted more empty blocks? Or are you saying you want to test? Like when we have big blocks, it raises the fee and that means that there's like a lack of transactions that are willing to pay that fee, which means we get an empty block.

The Lord, if you know my comment is not related to the fee model, it's just like a naive execution time. Like while you process and receive the data for a previous block, not just whether you still have to like mine, yours will mine on the empty block and well, it will kind of decrease an average bandwidth in some sense.

What do you think is the way. So I catch this real quick.

Go ahead if you want to.

So if you want nine introduces a new way for like two blocks where they can incrementally see, we actually should see if we want this. We should see actually reduce the reduction in empty block by because you can start a block at one transaction and because your block is not going to be full, you just add them in in order. And then as you see new things, you don't have to only block. And so you can do this kind of incremental block production and so you can start mining a block as one transaction and then just update to one that just might be two and then just update the three, update one until you go to a full block. And so I suspect that if clients implement that feature, we should see a reduction.

Yeah, I mean, is it a hard requirement or like if it's like a recommendation, I think it depends on the business or its minus and the difficulty of implementing it.

I mean.

Yes, certainly. So this is going to be a potentially competitive future for clients to compete on. So if you can provide miners with slightly increased revenue, they're more likely to run your client. And so it may be another fight if it wants more people running as clients, that it might think about the future. Well, whereas Geth may decide as too much work. So this is definitely not a consensus issue. This is just how miners mine. And you may even see some miner themselves and just run it secretly and you just notice that they have less empty blocks.

Yeah, but I mean, miners can even do it right now.

Like, they still like a small amount of fees by doing this like very small, maybe one percent, but there is nothing in existing clients yet. So I think this topic wasn't taken as a as a serious issue in successful implementation.

So, like, maybe Marty can answer, like, why it was never considered because no one asked ask for this.

I don't know, going into that necessarily is still still on the thing, but like something that it's come up previously, Tim is like if the network latency between the nodes, so you if you have four highly connected nodes versus if the nodes are a few seconds apart because one was mined in Russia and one was mine in the US or whatever.

Yeah, so we can definitely, I think for this test, all of the nodes were running in the same instance, but we can definitely for the next test, have different regions because then if they that would simulate more what Maintenant would probably be like. Yeah, to a very small degree, don't like to be clear, like we're not trying to stimulate the whole network networking stuck here. Yeah, but that's yeah, that's good feedback. We'll definitely try and have notes in separate regions for the next.

To clarify with regard to this, really, we are concerned about empty boxes that we are more concerned about, there may be an increase in Anchorites because the interesting thing about this is that like the like an increase or a slight increase in empty rate would not in any way affect the like the throughput of the system just because that's what the whole mechanism is about to kind of balance that out. It would, of course, kind of increase the variance. And that's probably an issue in itself.

But I'm just wondering if, like, the empty bulk rate is the important one or if it's more about like an uptick in Anchorites, for instance, think?

Well, it's more about what quantity of such empty or under filled block will be at the end of the day, taking into account potential network latencies and processing time.

You know, it's not like the snow doesn't crush and keep up with a network eventually, but that it doesn't affect Meiners, which are like a huge part of the system.

But to be clear, though, for most blocks, that won't change. So the reason we're concerned about this scenario is that most blocks under 15, 59 will be basically the same size as they are today, except when there's like a large spike in demand. And that will happen like a small minority of the time. And what we don't want is a tiny amount of time to crash nodes because they were really at their max throughput already.

And B, we don't want an attacker to be able to spend significant resources to then to then dorst the chain because or even have nodes drop off because they can't process blocks like under normal operations. There's not like it's uncommon for blocks to be two hundred percent full because the price basically goes up 10x every five minutes. So the amount of sustained demand you need for that is incredibly high. Yeah. So, so which are just the average propagation and whatnot that shouldn't change too much.

Although just to be clear, I don't think that it will be uncommon to see for like two two times four blocks, it's just uncommon to see like a long streak of those. Exactly. Just because with group work, they kind of have so much variability in both times anyway. So it's that like let's say you have a block that comes in four seconds after the last book, then that will almost be empty at night because it will have like a very small set of transactions to include. And so and likewise, if you have a book after 40 seconds, then that will be over. So it's just about these streaks that are very, very rarely.

Yeah, just to make sure, you know, does anyone else have anything they wanted to see or any feedback on how we can do the tests so that it's a bit more realistic?

Micah has his hand up, but I don't know if that's from earlier.

What are you.

Ok, where do they go if they want to give more feedback, just the IP channel and R&D?

Yeah, that's the best with. Cool.

All right, next up is all Khordad feedback, if you click on that, it has a handy file that Tim made with some really good information on feedback he got. Go ahead, Tim.

Sure, I can share my screen again, do this quick. So over the last two or three weeks, I tried to talk to basically every fine team to understand, you know, what they like, what they don't like about our core devs, how we can make it better. I have this long document with a bunch of feedback, tried to summarize it to reduce bandwidth. But on a high level, you know, I think people generally like it's not inefficient, it's not very efficient, but people feel that it works. I think the other thing that came up a lot is that we there's like this desire to spend more time discussing technical matters on some of the calls and stuff that client developers care about. But at the same time, this is basically the only place where we can get consensus on controversial decisions. So we really need to balance those two things. Another bit of feedback that came up a lot is people feel that it's it's kind of the bar to bring up on the call and bring them up repeatedly is sometimes too low. And that tends to take up a lot of bandwidth on these calls. And finally, another bit of feedback that was that was pretty common is that we tend to be very focused on like the next release and the each that are right in front of us right now, but that it would be good to have just like a higher level roadmap with regards to stuff like say that to merge and just generally all the long term things we want to do.

I had a whole bunch of different suggestions, but I think, you know, three things that are fairly easy to do that would have probably a high impact are like a just having one or two calls right after Berlin to discuss the roadmap at a higher level and try to think through not only the next hard for it, but realistically, we probably only have two or three 1/2 weeks before the merge. So what are the most important things to shipping those and how do we how do we think about the dependencies between them and with regards to this point about wanting to discuss technical things, but also needing to have controversial decisions or important decisions happen on the call? One thing that can help is just having like a longer term agenda. So instead of having just the next two weeks having like three months so that we can schedule stuff like Artim, you posted something about the transaction fees, right? That's the type of things that like right now, you can argue it's urgent, but most of the time it's not like the most urgent thing on our agenda.

So if we can schedule it in advance and say, look, we want to spend the call discussing this problem, people can prep for it. And similarly, if we're planning to take decisions on a call, we can also make that clear. And anybody who wants to be there can show up people who don't want to. I don't have to come. And then there's like basically three things I think probably makes sense to have, like a longer discussion probably on the chat. But just, you know, what's exactly the process. We want to have the IP on the call. The idea of having a code of conduct came up a bunch of times. So this was a simple one that was proposed. And finally and with time, the you know, I think a lot of the core developers I spoke to were. I had a hard time articulating exactly where the bridge between, like what decision devs make and what decisions the community should own is. And I think one thing that could help there is just trying to explicitly clarify, you know, what our core developers optimizing for.





