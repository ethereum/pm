# Consensus Layer Call 84
### Meeting Date/Time: Thursday 2022/3/24 at 14:00 UTC
### Meeting Duration: 1 hour
### [Agenda](https://github.com/ethereum/pm/issues/501)
### [Recording](https://youtu.be/ThoT6-eLTN0)
### Moderator: Danny Ryan
### Notes: George Hervey

*** ***Additional notes, summary and chat highlights of this meeting can be [found here on HackMD](https://hackmd.io/@benjaminion/SybzPe5f5), courtesy of Ben Edgington. Thank you, Ben.*** ***

## Kiln Office Hours

Danny:
Transferred over. Okay. Welcome to the call. Consensus layer call 84. The first half, or really however long we need, will be dedicated to Kiln merge, et cetera, et cetera. Then if any client updates would like to share research spec, et cetera, I can give you all an update on the withdrawals stuff that you're working on, maybe some other stuff and close from there. So on Kiln, I believe that many of you attended the call on Monday, which is kind of a testing and security related call as we lead up into the merge. The major sentiment from that is this is super critical at this phase for the next three or four weeks. I mean, and beyond the next three or four weeks, really, we need to prove to ourselves that we are ready. And so that involves productionizing obviously, but also involves a lot of these shared testing efforts. So, if you don't have anyone on your team that is involved in that, or taking a look at high or digging into kurtosis or following along, I would suggest that we do that. Pari. 

Marius Van Der Wijden: 
And following up and looking into hive. 

Danny: 
Yeah. And, and, and, yes, yeah, it's just, it's a shared effort. There's some people that are carrying that on their shoulders. and the more hands we can get in that, I think the better Pari, do we have a shadow fork? 

Pari: 
Yes. So the shadow conflicts have been released and the nodes are up and running. I think we hit TTD in another hour or something like that where, 200, 300 blocks away, I guess. 

Danny: 
Nice and you're running all of the notes this time? 

Pari: 
yeah, at the moment, I think it's just me. 

Danny: 
Nice. And is there any way to follow along? 

Pari: 
Yes, I can link some explorers links. there's no landing page system because it isn't really a public thing. but one thing to notice where following mainnet distribution now, so there's setting 60 something percent prism, 20 something, 15%, whatever. I just looked at one of the reasons reports and then split them up accordingly. 

Danny: 
Cool. great. 

Marius Van Der Wijden: 
which execution layer clients are you running until they split? 

Pari: 
Currently Goerli, Nethermind, and Besu. And I've also tried to follow mainnet split, so I just multiply the two splits. So if it's 80% Geth and 60% Prism, then I just multiply the two and whatever number in that is how many Geth clients that exists. 

Danny: 
Cool. Great. So this is shadow forking Goerli. Ideally the transition goes off without a hitch. we're following a number of metrics and, the transactions we pipe into it. So we'll have some organic activity. Is the base fee on Goerli above 255? Does anybody know? 

Tim Beiko: 
I'm looking now, but I doubt it. Oh, base fee is nine way. so what we can do if somebody wants to, when would we want to stand Goerli? So I can, I guess Pari has a ton of ETH as well, but like we, we could spend Goerli either during or before or after the transition. I'm not sure. 

Danny: 
Yeah. I mean, leading, leading into it and right after it would be, I think the most interesting spot. Yeah. But any place in there, I mean, the Prism bug would be caught at any time the base fee exceeds 255. That style of bug. But there's any number of other bugs in my short. 

Tim Beiko: 
Yeah. So we say basically the next hour is when we expect this to happen? 

Pari: 
Yeah. I can just read all the math, but I think it should be in the next hour. 

Tim Beiko: 
Is it easy to start a transaction buzzers fiber now? Or... 

Marius Van Der Wijden: 
I can start one. Yes. I might need some more funds, but ping you if I, if I need more. 

Tim Beiko: 
Okay. Don't lose them. 

Danny: 
And you never going to live that one down? I'm sorry, Ben, what was that? 

Ben Edgington:
Don't sell them. 

Danny: 
Yeah, there is a, Goerli ETH proposal right now to fork like 10 trillion ETH into it. So that's, the signal about buying Goerli. ETH is it goes away, but that's another conversation. Okay. And then there was some discussion around doing, either another shadow fork or stepping up and shadow forking mainnet, but to do a bit more of an all hands, you know, have more people involved, actually watch it, make sure it goes well. Triage it, if there are issues. Pari or Tim, is there, is this just an idea at this point or is there a plan here? 

Pari: 
at least the current plan for this is that we do the mainnet shadow fork two weeks from now. So we wanted to do dev net six next week, and then based on how the, Goerli shoadow fork goes plus devnet six, then we would discuss the mainnet shadow fork the week after. 

Danny: 
Okay. And dev net six would be a bit more participatory. 

Pari:
Yeah. Whoever would want to join can join there. 

Danny: 
Okay, cool. And we'd maybe not write a blog post, but we would invite even that want to jump in and run, validator set ups through that transition. 

Pari: 
Yeah, exactly. Okay. 

Danny: 
Okay. Cool. and target is a week from today, so configs on Monday. 

Pari: 
Yeah, that sounds about right. 

Danny: 
Great. And I guess what we would like if possible is, client teams to have their eye on it and if something goes wrong, treat it like a fire drill. 

Tim Beiko: 
Yeah. And I guess even more than that, like what you did there in 1559, which I think was useful is just having client teams also like straight up like monitor node. Like the make sure even if, you know, does it crash like is like memory usage, block, processing time, you know, like just like our, like, you know, metrics kind of tracking what you'd expect them to be during the transition. 

Danny: 
The shadow forking main net, it says, do we need to deploy deposit contract? So yeah, we could reuse the existing deposit housing contract and change the Genesis fork ID, but that's not going to allow us to actually add any deposits. I would suggest that we use the ERC 20 variant of the deposit contract, where there's an owner that can issue ERC 20 tokens. and by default you just, pre-populate the Genesis of validators. So, you know, you don't actually need to be sending main net transactions, but we can send a few to get some deposits in after the fact. 

Marius Van Der Wijden: 
Wouldn't reusing the, at the mainnet deposit contract, the existing one, be really, really dangerous because basically you would like to have to sign with your life keys on the shadow fork. 

Danny: 
Yeah. There'd be a lot of reasons. And we'd also don't control like any of those validators. 

Marius Van Der Wijden: 
Yes. 

Pari: 
No, but if we use some mainnet deposit contract and chance to deposit it, then all the validators is invalid. Exactly. So it's just our Genesis set, but then you need 32 ETH. 

Danny: 
And you'd, you'd be burning that ETH. No, no one would own that for you. I, if possible, I recommend we just use the ERC 20 one, so we at least get a few deposits in there. 

Pari: 
Yeah. 

Danny: 
I had a dream that the gas prices were three Gwei. I just realized, is that true? Is that... Sorry. 

Tim Beiko: 
On Goerli, they are. 

Danny: 
Okay. 35. Okay. I had, okay, A man can dream. okay. So let's do that for the mainnet shadow fork in a couple of weeks. I think one of the very important things is to monitor all those metrics, the network wide metrics that we want to see, no missed slots, that kind of stuff, make sure that it's actually, you know, the main activities being ported over. cause this is beginning to look like a very real load test. but we also not just the, the metrics, but I think we, the network wide metrics, but I think it be really important to monitor, system usage of different client pairs. you know, I think we have, we can estimate that it's going to look like the, some of mainnet today. but it's good to see if anything unexpected shows up there, weird CPU processing or memory book, that we hadn't seen on some of these smaller testnets. Okay. Other Kiln merge testing related items? 

Pari: 
Yeah. We have a nightly CI with catharsis now where every single client pair is a majority time. there are naturally a lot of combinations and it's getting a bit hard to keep track of what's broken where, so it will be great client teams could also look in and just have a look at your branch and see what's broken. If someone needs access to rerun the job or something, I can add you to three, four. 

Terence (Prysm):
If the client, release a new commit or a new Docker image, what's the best way to push that to the 90 Butte? Do we just commit it? 

Pari: 
Yeah. That can be one way. You can make a PR or, if you're always going to push from the same branch, I can just have a tag slash nightly build like colon nightly build or something. And then it'll just pick up the latest version from that tag, whichever way you guys prefer. 

Terence: 
Yeah, that sounds awesome. I will DM you offline. 

Pari: 
Perfect. And the same thing applies for every client team. I think I sent a list of which strategy I'm using for which client team, just sanity check it. And if you want to change it, then like a couple of you have pinned versions, a couple of you have latest, a couple master. Just have a look and let me know what you guys think. 

Danny: 
Cool. And, that has been running for a few, at least a few days. Right? 

Pari: 
Yep. 

Danny: 
And how does it look? 

Pari: 
I think it's happened around three times, like three nights so far. the first day was just completely broken, but because we had to get up to speed the second day, I think we had all green on Geth and Nethermind was clean, but two out of the five. and I think the Besu kurtosis mix still has some issues. So I don't think it's a client team issue. and today's, I haven't checked it. 

Danny: 
Great, great work. Thank you. 

Pari: 
And also, I just want to mention Mario's working on getting some more analytics in so that we can actually see some participation, et cetera. And I think over the next week, we'll integrate that into ketosis as well. So we'd have a better idea of when a Testnet dramas a pass and when not to fail. 

Danny: 
Yeah. One thing Mario was doing was trying to get the head correct and target correct percentages. and that's why I was asking in another channel about the, you know, if there's an end point for this and I know lighthouse has one. Do other client teams have a script that they use based off of the common end points? Or how do they get that data? Or is it only coming off of as permethies metrics? 

Terence: 
We use matrix. 

Danny: 
Got it. Okay. Other emerge related items? 

Mikhail Kalinin: 
Just wanted to give a quick update on where we are, the block tags. so we have, on, on, on the previous ACD call, we have discussed, whether to add justified block tag into the, list that we already have. and, we decided not to do this because it would require breaking change into the engine API. And also it has a dubious value of it in this stack as we already have finalized and safe. so, by the end of the day, we are going to have, earliest, finalized, safe, which will be temporarily set to a justified block as a stop gap and unsafe, latest, which is going to be an alias for unsafe and Bandon. So, yeah, there is a PR to the execution. API is, are both story. 

So if people want to discuss anything or propose their own fag or whatever, we also discussed the description of this tags there. Please chime in. Comment in and comment out. Also one contentious thing there. this for me, is there is a suggestion to remove latest, from the list of tags about to keep supporting it in clients. what worries may be it is that clients at the merge might just decide to remove it from the code base and stop supporting it, if it will not be in the list and in the description field, there is the latest with which is marked as deprecated. so yeah, I'm not sure that's how it should be quite good at the end. Probably Micah want to champion on that, small conventions change. So that's, that's it on this topic. 

Micah Zoltu: 
Yeah, I think, that describes it well, I'm I'm of the opinion that I would rather people, you end users who are looking at the docs, I'd rather them not see latest and therefore not start using it rather than see latest and not read further and realize it's deprecated. And so by not putting it on the list, the only people that will use it with people that already know about it, or, you know, read the whole list and then see that it's part, I read the description and see what's deprecated, and then she was doing it anyway. I feel like it's much easier to just make it clear to the eight dev teams that, Hey, please don't move latest yet, rather than trying to communicate to the thousands of dapp developers. 

Danny: 
I'm going to jump in on that issue. I try to think it's early in terms of a deprecation warning, but I, we can have this conversation on a, I mean, not for deprecation warning, but for the actual deprecation, but I'll jump in there. Was I just muted? Did anyone hear what I just said? 

Tim Beiko: 
After "I jump in there", you got mute. 

Danny: 
Okay. Whoops. yeah, it was an oversight, the justified, when we thought we were going to add justified, it was an oversight that we didn't realize we were making a breaking API change. So, anyway, Okay. API changes coming, testing in full force, productionizing clients. Is there anything else people would like to discuss with respect to the merge? any unexpected hiccups, any design questions, people would like to share any optimistic sync design issues that people would like to bring up? 

Arnetheduck: 
Well, there is one thing I can mention for Nimbus, which is that parallel to the optimistic sync, we've been playing around a little bit, light client sync. And, unless anybody feels it's very wrong to do so, we thought that we actually launched the libp2p protocol, server and gossip, like request response and gossip on Kiln and going forward with our own nodes, at least. So what that'll mean is basically that, the light client updates will be available on, on, on Kiln for anybody that wants to experiment with light clients or in like Lansing. 

Danny: 
Are you gossiping those? Or are those only request response? 

Arnetheduck: 
There's gossip and request response. So there's, there's this back, there's a PRF in the consensus spec repo that defines the protocol. What we've done is that we've added the V zero to the topic name for gossip and likewise for the request response protocols. So we've done this obviously, because we don't want to pollute the official namespace with pre-release code, basically. The spike is still up for comments and changes. And so unlike it's 

Danny: 
Did we start with V1 on our gossip topics? 

Arnetheduck: 
We stick the fork ID in there. And then we kind of hope that we won't change between forks, but, but in this particular case, there's both fork and V0 because we felt that the protocol is not yet sufficiently nailed down. 

Danny: 
Great. That's exciting. 

Arnetheduck: 
It's actually pretty cool. Like we're trying to have a client as well. It crashes a little bit, but, it's kind of promising to be syncing this way. 

Danny: 
Excellent. and this will prime as well for the light client workshop happening in Amsterdam. yeah, I, at the tip of my tongue is to jump in and review a lot of the depending light client stuff. we want to get that a bit cleaned up before the workshop next month and have a clear direction from there that thanks for pushing all that. 

Arnetheduck: 
Yeah. There's a question about the PR. I'll dump it maybe in discord in the bit. I'm not in front of a keyboard right now. 

Danny: 
Okay. Merge related items, Merge related concerns, any merged related topics? 

Terence: 
I guess I had a question. Is anyone implementing some way to retrospectively verifying terminal block? So I'm asking this because that you could sync through the terminal transition block using optimistic sync, right. But after you send to the head, you actually go back and verify the total terminal, the difficulty. Is anyone working on that or planning to work on that? 

Seananderson: 
Yeah, I think in, in lighthouse we have a PR for that right now. 

Terence: 
Okay, awesome. 

Enrico Del Fante: 
Yeah. Teku is already doing that. So if we will throw the, that terminal while optimistic sync, once we are fully synced, we go back and, and check the terminal conditions. 

Terence: 
Alright. If that fell, I suppose you just panic, right? 

Enrico Del Fante: 
yeah, I think so. I would need to double check, but yeah, it's something that you cannot recover at that point. 

Terence: 
Thank you. 

Gajinder (Lodestar): 
So in that case, the folk dries should start giving in valleys. And, we, the other reason that it is an inverted terminal block, I think this is what the expected behavior should be. 

## Other client updates (if any)

Danny: 
Thank you. Anything else on the merge? Okay. any client updates, like in the past handful of weeks. We don't have to do a full round, but if you have some interesting things you'd like to share by all means. 

Ben Edgington: 
I should mention that our, I don't call it a post-mortem cause nothing died, but, our post incident review for, the Teku performance issues last week is up. I stuck it in the chat if you want to link through to that. so last Tuesday, what nine days ago around 5:00 PM GMT about 10% of the network vanished. and I think Teku can take the blame for that. Puts a lower bound on our network participation, in any case. So, it was related to deposit processing. there was also knock on effects to garbage collection and another knock on effect to caching of states and state regeneration. So, yeah, precedent called it very nice. so, you can read all the gory detail if you wish in that, review. we took, it took time to diagnose, the, the tip of not withstanding. and we also, we didn't want to just get out of hot fix for the immediate issue because it seemed to be under control. We could see the kind of deposit, flows coming in and so forth. So we, we took time to kind of dig down deep into the, garbage collection issues and, and fix everything all the way down. So, that is a great improvement. 22.3.2 is out and fixes that issue now. 

Danny: 
Thank you. Upgrade your notes. Okay. 

Mamy: 
Do you have any, kind of specific tests to make sure that your cash, our concurrently introducing the regression? 

Ben Edgington: 
I'll defer to Enrico, if you have anything to say on that? 

Enrico Del Fante: 
so say it again. So we'll, you've seen...

Mamy: 
so yeah, any kind of tests to make sure you don't introduce any regression when you do you're caches because we also have a similar kind of, caches and we had in the past as, mentioned in the, in the chat, something similar with a GC and we just want to share logs and good practices for regression and supporting those kind of issues. 

Enrico Del Fante: 
Yeah. Thanks. I don't have in mind at the moment, all the tests we implemented around that. Thanks for the heads-up. We will have a double check on that and maybe reach you out if something needs to be shared. 

Danny: 
Right. And the fundamental question being caches are critical, but your cache not working correctly still looks correct from. So from like a CI standpoint, it's hard to actually know if your cache is running properly. 

Ben Edgington: 
Right. Cause we, it doesn't give wrong results. It just forces extra work because we regenerate the states. So it would be a performance issue rather than a kind of cache-y, you know, wrong results from the cache issue. 

Danny: 
Thank you, Ben. Any other client updates people would like to share today? 

Arnetheduck: 
I can just briefly share two little things that are up in the PR queue on the consensus spec. One is that, we offered a big back and forth about how to reduce aggregate bandwidth. Once we reverted back to the old aggregate behavior of ignoring certain aggregates, we found a way to make that a little bit more efficient. So there is the PR 2847 up, which expands on the aggregates that we are allowed to ignore by looking at pure subsets, basically. So the client has seen an aggregate that is better than the current aggregate that is being gossiped. We can just drop the worst one because the client will already have sent the better aggregate to all its neighbors. 

I recently extended that to contributions as well on the suggestion from from Edmund Sutton, Teku as so that's, that would be nice to get in it. It gives quite a nice improvement. We've tested it a little bit here and there. the other one is our beacon blocks by range request. It has a step parameter, The step parameter was thought to be used as kind of like, when downloading from multiple clients, you'd sort of interleave the blocks and then, apply them to your states in this interleaved fashion, but nobody's really taking advantage of it. What does happen is that in code in pretty much everywhere we have to, bounds check this and, yeah, there's like multiplication going on and it's just annoying if nobody's using that stuff, we might as well get rid of it. 

and there's two reasons for getting rid of it. One is to simplify the code base. Obviously the other reason is that we're discussing for the merge, a request between execution and consensus layer, where the consensus layer can fetch execution data from, from the execution client in order to save space, significant amounts of space, gigabytes of space on the drive. And in an ideal world, we would actually mirror both the range and the route request on the JSON RPC level. So I thought about writing a PR for the API and in writing that PR I would really want to not include the step. so take a look at that. I don't know if there's any more to say about those. 

Danny: 
Was there, so on, on PR 2847 I have reviewed this and I think it makes sense. I was kind of waiting on, a bit more engineering to chime in on, in case that was inducing, weird engineering, tough engineering requirements on the caches at which I don't think it is. on the 2856, was anyone using, does anyone use step right now? Let's see. 

Arnetheduck: 
So looking through the comments, it was only Teku that responded that they use it in some kind of exceptional case. I think this was discussed out of band, not in the PR. But my understanding was that they were willing to remove that functionality because it wasn't critical and what's nice is that, it's actually possible to deprecate the step in the backwards compatible fashion. So the protocol allows clients to respond with an incomplete, response. Basically somebody requests 10 blocks, the client is loved to respond with just one, right? So any step larger than one, the way to deal with that would be to just return one block and that's it, right. That's a correct response. So it's still, it doesn't break those existing clients. It's just that there will be less efficient in those exceptional cases, but I'd really encourage everybody to take a look at this PR, and think about how your clients, like how existing versions of your clients would react to such a backwards compatibility hack so that we don't break any user stories here. 

Nishant: 
Yeah. On our Prisms and, we do use the step parameter in the case of, extended period of without finality. And, you know, there are a lot of skipped slots, but, I've looked at the code and I think, we can, fix it to handle the case where, the step values only one. Just makes it slightly more inefficient. 

Danny: 
Thank you, Nishant. I suggest y'all take a look at these. they're pretty simple. I think we just need to kind of have some quick consensus on whether we want to get them in. so please do. And I'll make the rounds asked for and put again probably in about a week, and no input at that point all assume is generally being okay with it. Okay. Any other client updates? Great.

## Research, Spec, etc.

Danny: 
I wanted to give you all a quick update on withdrawals from the consensus perspective. I believe this may have been shared. This is Alex Stokes' meta spec that kind of stitches together what's going on with the engine API, the execution layer and the consensus layer. On the consensus layer, there are three kind of the core features. One is, under 2836, which is, withdrawals manages the withdrawals queue and does full withdrawals essentially once you're exited and drawable, the other is 2855, which is a new operation, which changes, 0x00 to 0x01 credentials. And this is a prerequisite for doing a withdrawal, because you need to have a place on the execution layer for your value to land on the other side. And then I do have, I meant to push it up before I have a branch locally. That is the third feature, which is a partial withdrawals mechanism. 

We've gone back and forth on how we might design this one was to do an election optional election or when you make a block. but after discussing some of the advantages and disadvantages here, what I have in a PR coming up today for review is a essentially just rotating through any, anyone that has an effective balance of 32 and has balances in excess of 32 and also has a 0x01 credential on some interval, just get swept. and for these balances to go into the, into a push style withdraw, I think this is cleaner. This allows you to do it, on an interval faster than block proposal, which is, is nice. and also allows for those that have a split between the or sorry, the active credentials and the withdrawal credentials, to ensure that they do get their partial withdrawal and that their partial draws are not held hostage by the act of QI, which makes the proposal. anyway, I, we're definitely the core of that. The 2836 will probably be merged today. the credential change operation we merged soon and we'll have this other PR up for review. By merging, I just mean they're, they've been reviewed, they have tests they're future complete from a certain perspective, but I would like to get some more eyes on this stuff soon. 

Any question or comment on how we're doing withdrawals on the consensus layer side in these specs currently? 

Mikhail Kalinin: 
Is there already a PR somewhere? Or a proposal on the excess balance scheming? 

Danny: 
I have a, I have it on a local branch. I was developing yesterday. I did not get the PR up yet, but right after this call, I'm going to push it up. it's still needs some more tests, but it has the kind of the, it shows the functionality. Okay. And on, I think one of the other things is in active development, although it's probably set aside a bit right now or productionizing the merge, but, any updates on 4844 proof of concepts or specs or anything people would like to share there? 

Seananderson: 
I haven't made any progress on our end, but I'm hoping to soon in the next couple of weeks. Just as far as like a proof of concept. 

Terence: 
From our end, I have a branch I am pointed to, Protolambda's branch as well, which allows, which has the right, photographer, which has a ride case digital library. So right now I'm just playing around with the library, getting myself familiar with the case that operation, and when it comes to implementation, I am working on the networking side of things basically at the end, the new drop sync subnet and, also doing some testing around it. 

## Open Discussion/Closing Remarks

Danny: 
Thanks. Okay. Any other spec related or research related updates for today or discussion points? 

Tim Beiko: 
So one quick thing, if nobody has anything, we, we have this proposal on all core devs last week about, trying to unify the EIP process across both the execution layer and consensus layer. we're working on an executable spec on the, execution layer. and one thing that would be nice is eventually to have also EIPs to propose changes to the consensus layer so that the community can kind of follow this a bit better. And we're in this weird, awkward spot now for like withdrawals and 4844, where we're like, we have like these meta specs, which doesn't point to both sides. so we're trying to like harmonize all that. I have a thread in each visit missions and we're discussing this and the EIP editing channel on discord if people have had thoughts. 

Danny: 
Yeah. I mean, I think from our perspective, from my perspective, it enhances our process, you know, allows us to have a bit more exposition and stitch the things together, and leverages the executable spec that we know and love and write a lot of tests with. So, I think I'm fine with it. I think it's, it's much of a more difficult change on the other side of the aisle. 

Tim Beiko: 
Yeah. For consensus layer people, it basically just means writing up a bit more English bits and putting those into the EIP. 

Danny: 
Yeah. I will point out, I think something that, is emerging with 4844 and is, it's kind of how withdrawals are working as well, is this notion of using a feature directory rather than a fork directory? While a proposal is independent, within the consensus specs, and only when proposals are decided on, as these are going to go into a, an upgrade or fork together, would we then probably merge into a single fork directory? Capella that's the directory with the withdrawals for, for practical purposes is the withdrawals directory. and 4844 is its own directory. You know, and if those were to go into the same fork at that point, I think it makes sense to merge, rather than the way we did with Altaira, which was, we had a grab bag of different features that were all intertwined during development and discussion. And it's kind of hard to parse and look at, I think, emerging down and when you get closer to fork is probably also difficult. but I think it's more sane from a feature perspective and allows decisions to be made a bit more, independently from each other during the design and governance process. 

Lightclient: 
What are your thoughts on just maintaining a PR against the report? Like for example, for 4844, I feel like that is something that could do just exist as a diff yeah. And then rebasing against like new things that change. And then when you have high confidence that it's going to the fork and it's at a place that's acceptable, you merge? 

Danny: 
One of the valuable things of, so there's a couple of things that are one of the valuable things emerging is, to actually be able to generate tests, vectors on normal releases. Although you could go into that PR branch and generate the test vectors, if you wanted to release them early. you know, I merged that after discussions with Proto because there are iterative things to do there, but there's like at that point, the conversation was huge. There were lots of different, changes, and it just becomes hard to kind of track at that point. And I guess to piggyback on that, withdrawals are these like three features together. And so they really I'm developing them in three PRS that piggyback on top of each other. and I guess that works in terms of keeping them as separate PRS, but then I'm having like three different places on rebasing and stuff and they, they kind of intertwined a bit. So from a development perspective, merging earlier is nicer, but I see from like a separation of concerns perspective that could also work well. Is that being considered on the execution side? 

Tim Beiko: 
It's being debated. 

Danny: 
Okay. 

Tim Beiko: 
I think, yeah, I think that there's one of the trade-offs is like, most the IPS on the execution side, don't actually make it up the main net. And I suspect over time as more people might propose stuff for the consensus layer, that that'll be true as well. So it's like, there's a trade off between like making sure we actually save the historical record of it. but then not cluttered the stack itself with like spam. yeah. 'cause if you, if you do save stuff just to PRS, I mean, it literally only lives on GitHub and that's not great. and I mean, we've seen literally for Shanghai, EIP 1153 has been like proposed again, which is just based on the number several years old. So you can imagine a world where like, that spec would just be gone if maybe it wasn't part of like the EIP repo itself are much harder to retrieve. so yeah, I think, Yeah, we do want to keep a copy of like, and I think there's probably something similar to like when an EIP before the EIP gets merged as a draft, it's also just a PR on GitHub or like in somebody for it. And that's probably fine. But then once the EIP is actually merged and has a number, then it becomes like a markdown file and the EIP repo, and like at least that's part of the gift repository. 

Micah Zoltu: 
I believe the tentative plan from what I understand from Sam's plan at least, is that once someone gets an EIP to some threshold like draft or whatever it, the intent is to keep it as a branch forever or indefinitely, or until some extreme circumstances are reached, we would not delete them or move them. 

Tim Beiko: 
Right. And then you could just say, you could just pull the master branch or like your own branch if that's what you care about, but at least it's part of the overall git repository. 

Danny: 
Right. But he's saying you would leave it as a separate branch. 

Tim Beiko: 
Right. Yeah, yeah, exactly. So it's like, it doesn't clutter the spec on master, but if somebody just wants to pull the whole repo and make like an archived copy of it, like with all the branches, then it's manageable. Like it's still a branch part of the main report rather than on somebody sports. 

Danny: 
I see. I see. I guess what we often see on the consensus layer side is the, it gets written, it gets merged. And then you do over time, see an iterative, small proposal change or an iterative small bug fix change, or adding a bunch of tests. I guess you could always do that off of a PR of a PR rather than off of a what we call dev. 

Micah Zoltu: 
Yeah, I think, I think it may be some confusion here. The idea is that the PRs would still be short-lived. The branches are what is, are long lived. And so, yeah, there's like canonical naming system for branches and, you know, it's, you know, got a hierarchy, do it or whatever, but the idea is, is that the, again, this is of trying to have in Sam's proposal, here. The idea is, is that the, all the texts would exist, you know, in the, this executable specs, repo. but if it's not yet live in production, then it's just going to be in a branch on that, which is a branch off of master, which is what's in production. 

Danny: 
Or scheduled for production. 

Micah Zoltu: 
Yes. I think for scheduled for production, there is a special set of branches that are like London and Berlin and whatnot. And so once we have Berlin nailed down and when there'll be a Berlin branch that gets all the EIPs that are in Berlin, all merged into one, and then eventually that will then turn into master once it launches. 

Tim Beiko:
Yeah, basically. Yeah. The, the, the for the time, well, I guess the, the Berlin branch would like grow, right? Like, cause we might choose to include like two EIPs to start. and then, you know, we add the third one. And so for that period of time where we're like adding stuff, it's, it's changing and like master is still with the main net. And then once we, I guess once we have the actual upgrade on main net, then we merge burden and the master and into parallel does probably London that's already been opened because we've already started adding stuff to it. 

Danny: 
I see. I see. Yeah. I mean, we can be amenable to such a process 

Tim Beiko: 
Yeah. To be clear, none of this is like this identity itself up for discussion yet. So like getting feedback from, from you all and you know, how this would help or hinder what your current process, it's really valuable. 

Danny: 
Anyone else have any other comments on this proposal? 

Danny: 
Any other discussion points for today? Okay, great. Thank you. Happy shadow fork later today. Please testing, testing, testing. It is critical. I know you all know that, but it's worth saying out loud. Talk to you all soon. Take care. 

Everyone: 
Thank you. Thanks. 

-- End of Transcript --

## Attendees

- Mikhail Kalinin
- Danny Ryan
- Marius Van Der Wijden
- Pooja Ranjan
- Trenton Van Epps
- Ben Edgington
- Saulius Grigaitis
- Gajinder (Lodestar)
- Carl Beek
- Terence (Prysmatic Labs)
- Pari
- Marek Moraczynski
- Alex Stokes
- Enrico Del Fante
- Preston Van Leon
- Protolambda
- Hsiao-Wei Wang
- Andrew Ashikhmin
- Dankrad Feist
- Tim Beiko
- Mamy
- Ansgar Dietrichs
- Dustin Brody
- Leonardo Bautista
- Sean Anderson
- Caspar Schwarz-Schilling
- Nishant
- Arnetheduck
- Lightclient
- Jame He
