# All Core Devs Meeting 124

### Meeting Date/Time: Oct 15, 2021, 14:00 UTC

### Meeting Duration: 1 hour 30 min

### [Github Agenda](https://github.com/ethereum/pm/issues/396)

### [Video of the meeting](https://www.youtube.com/watch?v=BTtwbvZZpfs)

### Moderator: Tim Beiko

### Notes: Joshua Douglas

## Decisions Made / Action items

| Decision Item | Description                                     | Video ref                                      |
| ------------- | ----------------------------------------------- | ---------------------------------------------- |
| 124.1         | Difficulty bomb pushed back to 10.7 million     | [58.09](https://youtu.be/BTtwbvZZpfs?t=3488)   |
| 124.2         | Arrow glacier goes live on block 13.773 million | [1.00.28](https://youtu.be/BTtwbvZZpfs?t=3628) |
| 124.3         | EIP-3607 moved to final                         | [1.01.30](https://youtu.be/BTtwbvZZpfs?t=3690) |

# [Merge Interopt Updates](https://youtu.be/BTtwbvZZpfs?t=287)

**Tim Beiko 04:48**

Okay we are live! Welcome to All Core Devs number 124. Let me post the agenda in the chat here. So basically two big things on the agenda: one updates on the merge. And then second is decisions about Arrow Glacier and the difficulty bomb pushback. To start, I guess, with updates on the merge - we had a face to face meeting last week with most of the client teams in person to work on the merge. I'm not sure if someone wants to give a recap? I know it all of the people on the call were here. Yeah, I can give a very high level one but I think a dev would be better.

**Micah Zoltu 06:00**

Nominate someone.

**Tim Beiko 06:02**

I'll give a high level and people can fill in the technical details. But basically, the goal of the event was to try and get the different teams on the consensus and execution layer to interoperate with each other. And to iron out any remaining issues in the spec. The consensus spec execution as well as the API between both layers. We do this through a series of milestones. So basically, they went from just simply implement the spec in your client and pass a set of reference tests, all the way to build a multiclient proof-of-work to proof-of-stake devnet, which runs through the entire transition. And we managed to get most teams through most of the milestones. So we set up several devnets during the week, basically starting one to one. So, one consensus clients to one execution client, and then kind of growing many to many or passing multiple one on ones. And like I mentioned, towards the end of the week, we were able to set up temporary dev net, which had, I believe, 100 nodes would ran 10,000 validators across a different set of clients. And it started on a proof-of-work network, I went through kind of the transition to proof-of-take and then managed to finalise on the other side. So it was a really good success in that it showed that we could get all these clients interoperating with each other. That we could get the spec mostly ironed out. And that we had a clear set of things we needed to fix going forward. Talking about that, I guess, we've launched just a more stable version of this, this final devnet called Pithos which people can join it if they want to really experiment with what the post merge infrastructure would look like. There's still some spec changes to be done so this is probably not the final version. But I suspect towards the end of this month, we should be done with those. And I think that's it at aof high level. Anything else that I missed that people wanted to add?

**Diederik Loerakker 08:26**

Yes, so about Pithos. We started with Amphora during the interop event. This was on a minimal configuration in Ethereum 2.0, which turns out to be actually more stressful, and then the Mainnet configuration because of the sheer amount of validators. The mainnet configuration is built for this type of node. So we decided to launch Pithos, which is also an Amphora, just a larger one. Hence the name. Thanks again for helping of the DevOps here. If you need nodes or needs keys to validate on this network, let us know and we'll try to facilitate that. We're trying to stabilise the remaining clients. So far we have three consensus clients running really stable on the network, and Geth on execution side. We're working on getting Besu and Nethermind running aswell..

**Tim Beiko 09:25**

Thanks for sharing Anything else?

**Micah Zoltu 09:33**

What is the appropriate coordination channel for the Pithos testnet? Would those be the interop channel in the merge category on discord?

**Diederik Loerakker 09:41**

Yes, that's works. Cool.

**Tim Beiko 09:54**

Any final things about the workshop that people want to share

**Marius Van Der Wijden 10:01**

I just wanted to say that I finished a differential fuzzer for the Engine API. So if execution data teams are interested, they can pass their implementations against Geth.

**Tim Beiko 10:22**

Can you share it? Do you have a public repo for it already? Or?

**Marius Van Der Wijden 10:26**

Yes, okay, I can share a link.

**Tim Beiko 10:29**

Awesome. Thanks. Um, cool. Anything else on the face to face?

**Diederik Loerakker 10:49**

So one thing I'd like to share where I think part of the success with the face to face is that we had these clear milestones as coordination points, so we could get clients in the same boat and figure out how to test with each other. I think we should keep this thing up where we have points of coordination on which spec version are we and these types of things, because the spec will keep changing. We're changing the API a little bit. This is what's really helped, I think,

**Tim Beiko 11:20**

Yeah, that's a really good point. I was talking with Danny and Mikhail, yesterday, I think there's at least one more large round of changes, or they want to fix a bunch of small things. Once that's up, we should probably make that the next milestone for people to aim for and make it clear that this is the point where we head towards. And there's other changes, we can kind of implement that off afterwards. Cool. Anything else? One thing I'll ask, I know there was some progress on this sync at the face to face and that the implementation is quite different from what Felix had proposed a while back, Is there like a repo or a spec or something that documents that there is basically the Geth PR?

**Peter Szilaygyi 12:30**

No, there isn't yet a spec. We do want to update it. But I kind of there are actually two steps towards that. One - I need to have a long chat with Felix to be aware of all the details and whatnot. And the other thing is that we were also trying to figure out one or two open questions before committing to writing it down. We'll get it up somewhere ASAP. But there's no updated docs yet.

# [Merge Interopt Updates](https://youtu.be/BTtwbvZZpfs?t=781)

**Tim Beiko 13:01**

Okay, got it. Thanks. Any other just thoughts, comments, questions about the merge in general? Okay. And yeah, one final thing, we put out a blog post on blog.ethereum.org today also going over the face to face. So if people are interested in kind of seeing all the details there. Yeah, I recommend just reading the blog post. So the other thing we need to go over today is the difficulty bomb pushback. So as we know, the difficulty bomb is is going to go live sometime in December. And so if we want to agree to how far we push it back, and when we do so, and put out client releases, and that needs to happen kind of soon. So I put together a bunch of different options and shared them on GitHub. And basically, there's two decisions we need to make. One is, when do we want to push the difficulty bomb back to and when do we actually want to have that upgrade. So for the actual Ice Age offset, I'd first proposed a value that would push it around basically mid April of next year, you would start to see some noticeable increase in the block times and then around mid May, you would see second or more increase in block time, which seems to be kind of the point where we absolutely agree have to push back. And then I also kind of got TJ rush to check these numbers. He's done a lot of work on the difficulty-bomb before. And he agreed that this, you know, this would have these numbers were right. But he suggested we should probably push it back a little bit farther. So his proposal was, we push it back instead of 10.5 million we do 10.7 million which means the bomb starts to show around mid May, and then we would have to push it back around mid June. Yeah. And then there's a middle value there, where if, if you don't want to do 10.5, or 10.7, you could do 10.6, which means early May, the bomb starts to show and then late May the bomb would have to be pushed back. Yeah, I'm curious. What do people think about this generally?

**Martin Holst Swende 16:11**

This should be the last push back of the bomb. We should not push it back too little. And run the risk of having the bomb disturb and interfere with the scheduling of the merge. So I think we should rather aim towards the summer when hopefully we should be done with with the merge.

**Tim Beiko 16:58**

Got it. Andrew, you have your hand up?

**Andrew Ashikhmin 17:05**

Unforuntately in Erigon we haven't been able to concentrate on the merge yet. So from our perspective, it probably makes more sense to push it to a later date. Out of the the options, I would choose the longest.

**Tim Beiko 17:32**

Does anyone have a opposition to the 10.7? Which would mean around mid May, which is kind of the farthest we had there. Would people want to go we could obviously do 11 million also. Every 100,000 blocks is like very roughly two weeks. Are people okay with, say, 10.7? Or would we want to go even even further, to make sure we don't have to push it back again?

**Peter Szilaygyi 18:12**

Personally, I think pushing back again, is still the better option versus just putting it out way into the future. Pushing it out is an unfavourable thing that nobody wants to do. But it's still the better option that requires developers actively doing something. My hope is to push it, but don't push too far.

**Tim Beiko 18:47**

Got it. Micah, you have your hand up?

**Micah Zoltu 18:53**

Ansgar was first.

**Tim Beiko 18:54**

Oh, sorry. Yeah, go ahead Ansgar.

**Ansgar Dietrichs 18:56**

I think I just generally agree with Peter in that. I mean, the whole point of the difficulty-bomb is to have some incentive to do to try and do things as quickly as safely possible, right? Otherwise, we could just completely remove the difficultly bomb and we do the merge whenever it's ready. And so if we wanted to keep it around at least as some token of our promise to do this as fast as a safe merge can be then I think it only makes sense if it has like a meaningful timeline attached to it and say, it only starts to come into effect in the summer. I think last all core devs there was still we were still saying that we couldn't 100% say that we wouldn't do it this year. And now like this will be like if we already extend this by six months, it just I think it becomes mostly meaningless. At that point, I'd prefer just removing the difficulty-bomb altogether. So my weak preference would be to go with the April timeline. And then and then that already gives us room to the end of May or something, and then if we really like can't get much done by the end of May, which is definitely an option. But then I feel like it's more honest in the sense to then have like a another chosen delay, instead of just, yeah, effectively, I think everything else just makes the difficulty bomb, kind of meaning meaningless, which is also okay, but I think we should be honest about that.

**Micah Zoltu 20:31**

So difficulty-bomb has two purposes. One is to make sure that we are regularly exercising our release process and getting things out on a regular cadence, etc. And the other one is to make sure that when the merge happens, if you want to run a fork of Ethereum, you need to have a release pipeline. I think pushing it out till summer addresses the any competitor or any fork needs a release pipeline, it still addresses that because even if you do run your run your fork of Ethereum without proof of stake, it is only gonna last you for you know, three months. So it doesn't do anybody any good. You need a release pipeline, and you get an extra free three months to get there at least pipeline out, but you still need it. And so I think pretty much any day we choose in 2022 solves that second problem. As far as the cadence problem, that one I think the argument favours doing it sooner because like, as Ansgar just said it forces us to behave on a cadence.

**Matt Garnett 21:29**

I think it also might be helpful to work backwards a little bit. How much time between the final release of the execution clients do we need but for the fork goes live? Because just saying mid April, that kind of almost implies that the merge is ready in the code bases by the beginning of March?

**Tim Beiko 21:51**

Yeah, I would plus one that like I think, at the very least, you need a month, right? And people have complained in the past that like where those delays could be longer. So if you take say that the farthest option right now, which is like, which is mid May, that basically means mid April, we need like a client release on the execution layer side.

**Matt Garnett 22:19**

But also for test nets, like how long is each testnet going to run properly? What is our thinking on these things?

**Tim Beiko 22:26**

Yeah, Peter.

**Peter Szilaygyi 22:30**

So I would argue that the merge kind of requires much longer timeline than just a one month thing. Because generally when we say that we want to give people one month to upgrade, that upgrading is mostly just download the new code and swap out your old instances. And of course, for operators to run multiple instances, that kind of means that okay, you need to upgrade one node, see if it works, just spin down another node, upgrade it, etc, etc. And we essentially without them that we expect this to take one month worth of effort so that they can find the time to do this, which is rather simple task. Versus with the merge. All of a sudden, you need everybody to figure out how to beacon clients work. To figure out how to set on one and the other. To figure out how to make them communicate between each other. So essentially all of a sudden of all your beacon users that are just on the Ethereum 2.0 chain now need to learn how to run a testnet and all the people who are on Ethereum 1.0 now need to learn how to run a Beacon Chain. And I think you don't want to rush that.

**Tim Beiko 23:42**

Right? Yeah, I definitely agree don't want to rush it. I think one thing we're planning to do is also when we start having these dev net, hopefully, start to get people running on the dev nets before so that if they are a large infrastructure provider, they don't learn about this and start setting up their infrastructure when the mainnet releases are out. But I do agree, we probably want a longer delay. And there's a comment in the cht, why do we have to pick a block number now? So the reason for that is based on the bomb going off in December, depending on when we want to push it back. We also need client releases to be available at least a couple of weeks before the upgrade. We can probably fork anytime in December. later December will be a bit harder because the bomb might actually start to show and also it's the holidays which is just not a great time. So that means that you know if say we wanted to fork December 1st, that means you probably want client releases around November 1st, which is two weeks from now. And similarly if we wanted to fork say the week after that, you probably want releases, the second of November, which is like three weeks from now already. So I think basically making that decision today means we then have a few weeks for clients to actually implement that change and write tests for it. And make sure that we're in a good spot. Whereas if we wait much longer then it'll just be a very last minute upgrade. Lightclient, you have your hand up?

**Matt Garnett 25:34**

It seems like there's two parts of work that needs to be done before the merge goes live. And one is kind of a dynamic amount of work. And that's actually finishing all of the things that need to go into a code release. And then there's a fixed portion of work that needs to be done to allow for people to upgrade and to upgrade all the testnets. And it's not clear to me how long that fixed portion is. And I think that it would be easier if we defined exactly what this fixed portion is, and then we target how long we want to spend on the dynamic portion of work.

**Tim Beiko 26:16**

Off the top of my head say you have the merge at date x - say you add some buffers, it means you probably want some like Mainet client releases two months before, say we do twice as much as as as we usually do. That means you probably also want like some test net releases a month before that. And so that's three months before the actual merge. And that means that you basically want to have the code mostly ready and in a spot where you can shift it again, say like a month. That's four months before the actual merge on Main net very roughy.

**Matt Garnett 26:53**

Yeah, so that basically means if we're gonna ship in mid April or so that we need to launch these code bases by the beginning of January, which I don't think is reasonable.

**Tim Beiko 27:05**

Yeah, I would agree there. I think Micah? You said something.

**Micah Zoltu 27:14**

I was just trolling. But I do have something to say. What was the final decision on the total terminal difficulty strategy that we're gonna go with? Last I heard, but it was still up in the air. I'm guessing you guys decided that off site? Are we releasing multiple doing multiple client releases, first with the TTD? And then another one, or sorry, first with all the code and then another one with the TTD? Or what was the decision on that?

**Peter Szilaygyi 27:47**

Well, I guess that's how we also get over that is that you have the code and then you just ship it a TDD for it. And you just ship some fixes. For another tesnet, eventually, you just put that the TDD into mainnet.

**Micah Zoltu 28:06**

So will all clients have some way of providing that via config, or will people need to download a new version, once the TDD is decided.

**Peter Szilaygyi 28:18**

I mean, I guess both. So at least currency what Geth does is that informal forks that we've had the fork block number, and it's not set for Mainnet, but you can just we have a flag override. For example, we override London - the point of the flag was to postpone the fork if something goes wrong, but you could also enable it if everything goes right. So my guess would be that we could do something similar for TTD, where it's part of the Genesis back, but you can control it with a flag.

**Marius Van Der Wijden 28:59**

We already have the flag override.

**Micah Zoltu 29:05**

So the concern is, again, maybe I'm a little out of date, because I haven't followed super closely in the last two weeks. Back when you're talking about this previously, the idea was, we want to choose the TTD a week or two before it happens, because we didn't want to wait too long, because we're worried that could like the further in advance we try to guess it, the more uncertainty we get and so we wanted to wait until like a week or two before before to choose the TTD. And then the idea was is that we would just announce to everybody, you know, two weeks prior to that date, whatever that is. Okay, this is the exact TTD which in the discussion was, does that mean we have another release two weeks before the actual merge? Or do we have like config override, or is there some other strategy that we're going with and it sounds like, We're going it's like the mix between new release and config override.

**Peter Szilaygyi 29:59**

Well, my best guess it would be both. So whenever TTD is announced clients will do their releases, because for most people, it's a lot simpler to just update them to mess with my command line flags. But I would definitely say the CLI flags would also be available, because it's always a good backup if something happens.

**Micah Zoltu 30:22**

Okay, I just the reason I bring it up in this context of this conversation is just because it does add complexity to the entire merge process for integrators, and so for people and infrastructure providers, etc. So when they are getting their stuff up, even if we release the clients two months, before, there will still be chaos near the merge, as people have to do that last minute upgrade or config change or whatever. So just keep that in mind. The merge is going to be significant more complicated for everybody then previous things.

**Tim Beiko 31:06**

I'm not sure that's something where even if we added an extra month of buffer, it actually helps people because it's like, you just need to do this thing close to the merge, right?

**Micah Zoltu 31:20**

Yeah, it's just like in terms of messaging and stuff, like the the kind of the more we drag it out and spread it out. It's just easier to make it clear, like: okay, do this one thing this week. And then next week, we'll have another thing to do versus: okay, do this today, do this tomorrow. It's more complicated for people as well.

**Matt Garnett 31:41**

So four months seems like a pretty generous amount of time to allow people to upgrade and do all of the testnets. What is what do client teams think of reasonable targets to have the merge code ready to release for testnets would be?

**Tim Beiko 32:08**

The hard question.

**Gary Schulte 32:10**

Still have spec changes, right?

**Tim Beiko 32:15**

Yeah, so as I understand it there's still some work on the spec that hopefully should be wrapped up by like the end of this month. Then we basically have all of November, probably like half of December before people start going away. And if we also have kind of the Arrow Glacier fork in December that also eats away at it's kind of the time there. So we have one to one and a half months prior to the holidays. And then people come and we we have some more time in the year.

**Danny Ryan 33:06**

Hello.

**Tim Beiko 33:07**

Hi, Danny. We're just asking, when is the merge gonna be done? Yeah, maybe something we could maybe confirm is: when do you expect the specs to start settling down? You mentioned the towards the end of October to me is that still reasonable?

**Danny Ryan 33:30**

Yeah, we had a number of spec changes that came out of the interopt. Most of them were actually simplifications, and most of them had to do with the Engine API. And we're working on those right now. I'm doing most of that Mikhail is on vacation this week. But we'll be picking that up. And the target is to be done with all those changes by the end of the month. And the general agreed upon target by client teams, to get an next version of like a persistent testnet up would be a month following. So the end of November. And then there's a lot of security and testing work and hardening of engineering to do. So then as we get into the new year after the holidays. We make decisions there.

**Micah Zoltu 34:22**

We were trying to decide on the ice age, which means we have to make some guesses today.

**Danny Ryan 34:26**

Right? The optimistic launch if everything goes well was end of March. And so iceage in April makes sense. But we could debate that I'm sure.

**Micah Zoltu 34:42**

Is it up to optimistic code complete or optimistic code complete and gone through all the testnets and a couple of months for infrastructure providers to upgrade and download and messaging?

**Danny Ryan 34:57**

No, not optimistic code. Optimistic - we do the launch at the end of March realistic is probably...

**Micah Zoltu 35:11**

What's your guess on code complete - ignoring all the other stuff that comes after code complete?

**Danny Ryan 35:17**

I'm not building the code so if we have if we have specs at the end of October what is code complete look like based off of people's experience on the work that needs to be done? Also knowing that pretty much everything is the same except for ensuring some issues in Engine API fixing some edge cases and things like that. And I think adding the random opcode which supersedes difficulty. Lukasz?

**Łukasz Rozmej 35:58**

So from my side -- the hardest part of saying when we will be code complete ready from the implementers point of view is all those disaster recovery edge cases which like even though there's maybe we do know but we might miss some etc and that those will just come in testing. The specs are you can more or less tell how much it might take but those edge cases will be extremely hard to pinpoint and fix all the things there.

**Tim Beiko 36:49**

Got it. There's a couple comments in the chat about like what's worse? Is it you know pushing back the bombs two times or what like alienates the community my opinion there is like a bad merge is what alienates the community by far the most. People will take a good merge with two difficulty-bomb push backs over a bad merge with one because we had to get it out two weeks earlier. I think we kind of saw that also with London where some people were a bit like unhappy with how quickly we went the mainnet after we found that last issue and then obviously people want the merge and like they wanted as quick as possible but there's no there's no way to expedite it beyond just doing the work and making sure that it's safe. Based on all of this it does seem like trying to get a date that's far enough in the future to give us some buffer ideally not far enough that it's like completely irrelevant and that that we we kind of forget about the difficulty bomb and I don't think it would be the end of the world to push back the difficulty bomb a second time from like the community point of view. Anyways at that point it's like if we pick in a reasonable delay for the difficulty-bomb and we push it back it kind of means that the merge is late and people will be upset about that not about the fact that we're pushing the difficulty-bomb back so yeah. I guess the second long winded way of saying I think I kind of agree with what Peter said at the very beginning that like something that's like far off but not completely far off based on this if you want like a rough four months from like the code quality to like actually going on Mainnet it seems like probably somewhere around like June-ish to have the bomb goes off make sense which means you kind of need the code done around February ish and obviously if we get there and we realised that's just not going to be the case then we push back the bomb again. The expectation we said is around the merge not around like the difficulty bomb and if we have to push it again, that's less worse than having like shipped the merge too quickly or something like that. Yeah. Andrew?

**Andrew Ashikhmin 39:40**

Right. So I would like to say that if we commit to this long delay doesn't mean that we are we are postponing the merge. Because as was discussed, if the bomb goes off in say August, it doesn't mean that we have to wait with the merge August or something like that. So my preference would be to have it move it to mid-summer. So something like a nice number like 11 million would move to mid summer. And we can if we are happy with the merge, and everything goes smooth with the merge, we can do it earlier than midsummer, by all means. So the bomb doesn't force us force us to do the merge late.

**Tim Beiko 40:33**

Right? Yeah. And then 11 million would mean the bomb starts be noticeable early July, basically.

**Andrew Ashikhmin 40:41**

Yeah, sounds good.

**Danny Ryan 40:47**

I want to piggyback on that. They're certainly a week ago, there was a lot of optimism as to timelines. And so I don't want to making a longer wait on the bomb shift our expectations on like what we're trying to deliver here.

**Tim Beiko 41:06**

Yeah, so I think there's like two ways, like one it's either you go with say, I don't think it matters if it's like late June or July because it's kind of far in a way you call it like the generous bomb, or you have like a very aggressive one, that there's like a high chance we push back if we don't meet the optimistic timeline. There is kind of no use debating between like mid June and July. It's like, if we go into summer, we might as well do it. And then the other option is like, do we do kind of more like April or May, right? And then, assuming we don't meet kind of optimistic to realistic timelines, then we'll have to push it back again, one more time. One thing also worth noting is - right before you came Danny, we were talking about how, like, what's the delay you want between having the actual code done, and then going live on Mainnet. So ideally, say you go live on Main net on date x you probably want something close to two months of like having the releases out so that people can actually upgrade their clients and like run an execution client for the first time and, and run their consensus client for the first time on the execution layer. If you do that, that means you probably want to fork the testnets and like the month before, and that means you probably need to put out the releases a few weeks to a month before that. So you have like a kind of generous four months between like the code is done, and we go on Mainnet. We might be able to do like slightly less than that. But that's kind of the Yeah, the buffer timeline that makes sense.

**Ansgar Dietrichs 42:57**

I just wanted to say one more time that I think it makes total sense to basically on the on the code complete side that we think there's no way we could try and crush this. This just takes the time it takes but then I just don't think the four months, that doesn't seem necessary to me. Like, for one, once we have to testnet releases, that's already at the moment where people can actually start getting used to running both clients, and everything at that point will basically be frozen. And you already know what steps to go through. So I don't understand why we basically have to wait until a fork before people could even start with their two months of time that we think they need. So I think that's just like another extra month that just doesn't need to be there. And then, even on the two months side, as Michael was saying, right, like if we only choose the total difficulty, relatively close to the merge anyway, and there's like the need for another update anyway, very close to the merge. Maybe like in the two months don't don't really make a lot of sense. So I just feel like the four months, at least a month, if not two is too much.

**Danny Ryan 44:24**

Also something that came up in conversations is that running certainly running a test net for a certain amount of time is very valuable. But one of the most critical elements of this is likely the transition process itself. And so having nightly builds in hive and throughout running it through the transition through the ringer multiple times is as much you know... equally of importance, if not higher importance for me on being being ready.

**Tim Beiko 45:09**

Just to kind of eliminate some options like Are any of the client team is like comfortable with the bomb starting to show around mid April? It does seem like from what everyone has been saying, mid April is probably too soon, unless we go with like the most optimistic timeline.

**Peter Szilaygyi 45:35**

So one thing to keep in mind is that the difficulty-bomb... we expect the merge to go cleanly then we might also see miners dropping off earlier, simply, maybe you just want to get rid of your hardware, I don't know. So that is just an option that we might want to keep open that we might see some hash rate drop before the merge. And if there is a hash rate drop, then the effect of the difficulty bomb is much more pronounced. So you could actually speed it up. So that's also I have absolutely no idea how to take this into consideration is just something we should consider.

**Tim Beiko 46:38**

I think, yeah, that's true. And somebody else had mentioned that on the all core devs discord also. So it's almost like, and I think the good thing there is if we do need to, we can coordinate another push for the bomb very quickly, like we did with Muir Glacier. So like, we probably don't need to assume if it started showing up, it would take us months to fix. But we probably want like, at least a couple weeks of like hash rate buffer in whatever number we choose. So that if the hash rate drops, and we kind of move through the bomb quicker.

**Danny Ryan 47:35**

I'm a bit more pro putting the bomb in May, rather than June or July, I think there was a lot of general agreement last week that a moderately aggressive timeline could be achieved. And I don't want to take that momentum out. I think if we set the bomb to June or July I think that's the earliest the merge is going to happen, just because that's the way things go.

**Matt Garnett 48:07**

So that means roughly code complete by the end of January, beginning of February. Is something that client teams feel is reasonable?

**Danny Ryan 48:26**

I got a lot of head nods of something of a persistent testnet at the end of November for current specifications. I know that doesn't mean code complete. And I know we have holidays then after so then it's - is it realistic to come up come back in January and harden things such that you're feeling like the code is relatively complete at the end of January, beginning of February?

**Gary Schulte 48:56**

From from a basic perspective, I think what we're most concerned about is adversarial conditions at transition. We I think we could be code complete, or think we're code complete fairly easily and not necessarily account for all the adversarial conditions, I think this that plays into our what we think is readiness more so than having code complete.

**Tim Beiko 49:20**

Right.

**Tomasz Stańczak 49:25**

Like possibly it might be more about the ecosystem testing and integrations testing and is testing everything rather than us only. So now maybe maybe a bit later bomb is reasonable already. because even even if this November testnet. This would leave just four months like end of March or February which is the three or four months for everyone else to test how it behaves. It seems tricky.

**Tim Beiko 50:01**

Yeah, and for sure, that's something we're gonna be proactive about. So I guess so in the next couple of weeks, we're already starting to reach out to like large infrastructure providers and try to get them using Pithos and see what like their feedback is, and you know, what breaks when they're using it and whatnot. So it seems there's like proposals from around April, all the way to like July, and being mindful of the impact that like a lowering hash rate might have.

**Micah Zoltu 50:44**

Is anyone willing to die on this hill? Like, or would everybody here be satisfied with whatever vote turns out?

**Gary Schulte 50:59**

I was saying we can always push it further. So it doesn't seem like this hill that needs to be died on.

**Danny Ryan 51:03**

I'm on the edge of dying on the hill now. But I also am not writing the software so...

**Tim Beiko 51:12**

My proposal would be to follow what TJ rush proposed, which is 10.7 million, it means the bomb starts to show around mid May, there's a world in which the hash rate drops, and it starts to show around mid April, and we need to coordinate either pushing the bomb back, or releasing the merge. And if we're really close to the merge and whatnot, we might be able to wait until to not push it back and have the merge happen in June and still be okay. So it seems to me like a sort of average of the different opinions, it's obviously something we can push back. I'll stress that like, the most important thing is actually getting the merge done well and out and no one will care about the difficulty-bomb if the merge go poorly, and no one will remember that we pushed it back twice a year from now if the merge goes well. Does anyone feel very strongly against 10.7?

**Matt Garnett 52:20**

How distracting would it be to have discussions about defusing the bomb in March to the merge work? Because if we get into a situation where we're like not super comfortable about hitting the target and we need to start discussing like okay, what is our backup plan to defusing a bomb? Is this something that we're going to be wasting time that is really important moment of working on the merge and we spending all core devs talking about timelines rather than issues at hand?

**Danny Ryan 52:52**

I think regardless, that's what we're going to be discussing as timelines at that point. You know, are we ready Are we not? And the merge the difficulty bomb being there is going to force our hand and having those conversations but we're gonna have to have those conversations anyway.

**Tomasz Stańczak 53:09**

I think to some extent, I'll repeat what Danny said in this conversation now is particularly important it gives them lots of information to how confident teams are. What are they afraid. What their timelines are. Give insight into for the community to understand.

**Tim Beiko 53:32**

I feel you're concerned about like spending all the time on all core devs discussing the bomb. I think that's something that's also kind of easy to discuss out of band and you know for me to come back on these calls and summarise you know, hey I talk all the time teams and like half of them think this makes sense and the other half is not ready or something like that. And I also don't want to spend several all core devs just discussing the difficulty bomb. And then there's a comment about having 10.8 instead of 10.7 so that it's like a clean month and we could have code complete date of February 1st. So 10.7 Danny maps to mid May the bomb starts to show so think less than point five seconds extra per block. So 10.7 million means we start to see the bomb in May. 10.8 million we start to see it early June again assuming a relatively constant hash rate if the hash rate drops we might see it before that. And it takes about a month from the bomb starting to show to the to the delay being like around the second or more which starts to be very negative.

**Ansgar Dietrichs 55:36**

Yeah, just just as a clarification question so basically as you're saying if the hash rate drops then there it would be earlier but my understanding is that if it's triggered by a block height then that would be later right? Because it would take longer time to get that block and then once we hit it, the effects would be is more severe sooner but basically the actual the moment of status the difficulty one would actually be further out not sooner. Is that right?

**Tim Beiko 56:02**

Not necessarily because the difficulty will readjust right the the hash rate so like I there's probably a point at which both effects cancel each other out I'm not sure where that is.

**Ansgar Dietrichs 56:18**

Right but the adjustments are always like they always lay him behind so basically just this right now we have like the 14 seconds or something right roughly block time instead of 15 seconds so then we would have like a 16 seconds approaching the the merge so i don't i don't think it makes a big difference.

**Tim Beiko 56:53**

Some comments in the chat between 10.7 and like 11. Do any of the client teams feel strongly that like 11 would be much better for them?

**Andrew Ashikhmin 57:19**

Well I think for Erigon 11 would be better but we can live with 10.7 probably.

**Tim Beiko 57:26**

Got it. So yeah, just because there's like a pretty wide range of opinions here I'm kind of tempted to go in the middle with 10.7 and that means that basically in February we need to have a conversation about how ready are we and do we think we want to push this back? Or do we think we're on the right track to not push it back? And you know, ideally the best of worlds we obviously are ready by February does that seem reasonable to people?

**Danny Ryan 58:05**

I personally want to keep this train moving.

**Tim Beiko 58:09**

Great so that he will make sure we are ready by February. So will I. Cool. Let's do 10.7 I doubt we're gonna get a cleaner consensus than this and now the other kind of big decision to make is when do we actually have this upgrade? So the bomb is scheduled to start showing sometime in December we probably need a month between the client releases and the actual upgrade on Mainnet because that means kind of probably three weeks by the time we announced them and the fork happens. So maybe starting backwards like given that we have the number to push back the bomb for today how quickly can client teams have a release out that has the bomb number and obviously we also have tests for it?

**Danny Ryan 59:25**

Is this a one week project? Two week project? Four week project?

**Tim Beiko 59:32**

I can start with my preference. So as the non client, I think December 8 would probably be like the nice sweet spot where like we're not just rushing all this in the next two weeks. We have like an extra week of buffer. And that means we basically we need releases out three weeks from now, roughly. And the fourth block for that would be 13.773 million. Does anyone disagree with that one? Okay, last chance for disagreements. Otherwise, we're going for 10.7 million delay to the bomb and having Arrow glacier go live on block 13.773 million which should be midweek on due on December 8th. But obviously these things are hard to predict. Cool. That was easy.

# [EIP-3607](https://youtu.be/BTtwbvZZpfs?t=3664)

Those were the two big things on the agenda today as the last small thing was EIP-3607. On the last call, we said we wanted to move at the final. But we wanted to wait to make sure that all the clients had implemented it. So I don't know do any client teams has had an update for this? Any client team have an issue with moving the EIP to final? The one with like the reject transactions from senders if there's already code the deployed at the address. Andrew, anything else you want to add on that? Or we're just going to move it?

**Andrew Ashikhmin 1:02:09**

No, we have implemented it in Erigon. And we are cool with it.

**Marius Van Der Wijden 1:02:19**

Also, there should be some tests much pretty soon that will require it in the clients. So if you haven't implemented it in your client, and the tests break in the next test release and you know that you should do it. It's it's three lines in Geth code.

**Tim Beiko 1:02:50**

Okay, um, yeah, that's all I had on the agenda. Anything else? anybody wanted to bring up?

**Danny Ryan 1:02:57**

I would just say sorry, I was 30 minutes late. But if there was any additional questions on merge interop updates, I'm happy to answer those. But you can also take it offline.

**Yuga Cohler 1:03:11**

And one quick question about the December upgrade. So obviously it's a small upgrade, just changing the difficulty-bomb block. I know there are still like 20% of open Ethereum nodes operating and open Ethereum has been deprecated. Do you think that open Ethereum would be upgraded for this purpose? Or is the expectation that anyone depending on open Ethereum would switch by then?

**Marius Van Der Wijden 1:03:38**

The expectation is that you should have already switched by now. But I think it's it's it's not a big change to update open Ethereum. And I think someone from the community will probably do it. But that shouldn't mean that you should run open Ethereum, you should have switched by now.

**Tim Beiko 1:03:59**

Yeah, I wouldn't be surprised if somebody just made the PR to open Ethereum. But the client is no longer officially maintained. I don't think there's anyone on the call who's still a maintainer of open Ethereum, who could like give more cutter. Yeah, and we can ask in all core devs after if there is someone who's like, willing to do that, but yeah, generally. Yeah, the client doesn't have a full time team working on it anymore. Any other questions, comments? I guess that was it then. Thanks, everybody. And I'll make a PR to the EIP for the difficulty-bomb and the Arrow Glacier spec today so that we have the updated numbers in them. Yeah, thanks a lot for joining.

## Zoom Chat

15:00:31 From Tim Beiko to Everyone:
Going to give people another couple minutes to roll in
15:03:05 From Micah Zoltu to Everyone:
Those conversations were more productive than some ACD discussions in the past...
15:03:10 From Tim Beiko to Everyone:
https://github.com/ethereum/pm/issues/396
15:03:13 From lightclient to Everyone:
pew pew
15:03:21 From Micah Zoltu to Everyone:
🔫
15:08:56 From MariusVanDerWijden to Everyone:
https://github.com/MariusVanDerWijden/merge-fuzz
15:11:48 From Trenton Van Epps to Everyone:
https://blog.ethereum.org/2021/10/15/amphora-merge-milestone/
15:12:24 From Tim Beiko to Everyone:
https://github.com/ethereum/pm/issues/397
15:13:25 From Micah Zoltu to Everyone:
My vote: Target difficulty bomb at April 1st. 😬
15:14:00 From Ansgar Dietrichs to Everyone:
I‘d prefer 10.5
15:14:46 From MariusVanDerWijden to Everyone:
I think it would not be good to push it back twice
15:14:58 From MariusVanDerWijden to Everyone:
So I would rather go for a later date
15:15:50 From Micah Zoltu to Everyone:
I am compelled by a "summer" argument.
15:18:56 From MariusVanDerWijden to Everyone:
I don't think mid may would make the bomb meaningless
15:19:06 From lightclient to Everyone:
+1
15:22:13 From Łukasz Rozmej to Everyone:
Why do we have to pick a block number now?
15:22:24 From lightclient to Everyone:
because difficulty bomb
15:23:07 From Micah Zoltu to Everyone:
I find peter's point quite compelling. I feel like we should have like 2 months between mainnet block chosen and The Merge.
15:23:11 From Ansgar Dietrichs to Everyone:
I think regarding learning to use the clients it is very much a "whatever timeline we pick, people will start looking into it a few weeks before" kind of situation
15:23:18 From MariusVanDerWijden to Everyone:
November is 2 weeks from now :O
15:23:24 From lightclient to Everyone:
:o
15:23:26 From Łukasz Rozmej to Everyone:
Push it back far, merge will be more eventfull than how much we postpone difficulty bomb, one the other hand who wants to fork will fork
15:24:43 From Yuga (Coinbase) to Everyone:
Is the current thinking that Consensus and Execution clients will remain separate, and therefore everyone who relies on e.g. Geth will have to spin up new Execution clients? Or is there any possibility of Execution clients acting as proxies/pass-throughs to Consensus clients?
15:25:10 From Yuga (Coinbase) to Everyone:
*new Consensus
15:29:09 From MariusVanDerWijden to Everyone:
Yes all node operators will need to spin up cl clients
15:29:11 From Łukasz Rozmej to Everyone:
I though chaos was part of the plan ;)
15:29:22 From lightclient to Everyone:
*always has been*
15:29:24 From Micah Zoltu to Everyone:
😆
15:30:05 From MariusVanDerWijden to Everyone:
There might be a way to run a full el node with a cl light client though
15:30:27 From Yuga (Coinbase) to Everyone:
Cool got it, ty
15:30:39 From Micah Zoltu to Everyone:
My gut says "code complete" is end of May.
15:30:58 From Ansgar Dietrichs to Everyone:
4 months indeed seems generous, and not sure if generous is the correct approach for our target of a "minimum viable merge"
15:31:09 From Micah Zoltu to Everyone:
Which puts me soundly in the "summer ice age" camp.
15:31:25 From Łukasz Rozmej to Everyone:
so basically "when its done"
15:32:02 From MariusVanDerWijden to Everyone:
@ansgar I disagree, we should have as much testing as possible, even for the "minimum" merge
15:32:13 From MariusVanDerWijden to Everyone:
*time for testing
15:32:27 From Micah Zoltu to Everyone:
As much as possible == infinite. We have to constrain it to some extent.
15:32:40 From Ansgar Dietrichs to Everyone:
I am just worried we are risking community alienation. Like, even with a smaller delay, we can always extend it later
15:33:34 From Justin Florentine (besu) to Everyone:
I can’t decide if I think community alienation is soothed more by multiple pushbacks or 1 longer one
15:33:36 From MariusVanDerWijden to Everyone:
I think that would alienate the community even more than moving the bomb a bit later and merging earlier
15:35:14 From Ansgar Dietrichs to Everyone:
I just don’t think code complete by end of January and mainnet fork by mid April is completely unrealistic, and the slow bomb rampup would already give us another month of buffer with that
15:35:54 From danny to Everyone:
are we live?
15:36:02 From Gary Schulte to Everyone:
yes
15:36:04 From danny to Everyone:
lol
15:36:09 From danny to Everyone:
I didn’t know
15:36:22 From Ansgar Dietrichs to Everyone:
haha
15:36:26 From danny to Everyone:
ah shit. I”m 30 minutes late
15:36:33 From lightclient to Everyone:
lol
15:36:34 From danny to Everyone:
I thought it was on the half hour....
15:36:36 From danny to Everyone:
wtf
15:36:41 From Trenton Van Epps to Everyone:
I've done that too
15:36:41 From lightclient to Everyone:
gm
15:37:46 From Ansgar Dietrichs to Everyone:
Wait, weren’t we deciding between April and May? Why June now?
15:37:59 From lightclient to Everyone:
because we didn't realize we need ~4 months pre fork
15:38:18 From Ansgar Dietrichs to Everyone:
But we really don’t
15:38:37 From lightclient to Everyone:
we just discussed that we do?
15:38:59 From Ansgar Dietrichs to Everyone:
No, you were saying that would be a generous choice
15:39:29 From lightclient to Everyone:
i think 3.5 months is probably the lower bound
15:40:22 From MariusVanDerWijden to Everyone:
It also depends on when we start counting, do we start from geth having the code in or all el clients or all cl and el clients
15:40:34 From lightclient to Everyone:
probably all el and cl
15:40:57 From MariusVanDerWijden to Everyone:
I think 2 months of final releases + 2 months for testnets would be good
15:42:25 From Micah Zoltu to Everyone:
I think the reason we want a long upgrade is because people won't upgrade until they see the testnets all succeed.
15:46:17 From Tomasz Stańczak to Everyone:
I am favour of the end of March bomb
15:47:12 From MariusVanDerWijden to Everyone:
I am in favor of Mid-May
15:48:27 From Ansgar Dietrichs to Everyone:
I actually think a longer time between code complete and merge increases the risk for adversarial conditions, as it gives adversaries more time to coordinate
15:48:36 From Ansgar Dietrichs to Everyone:
Mid-May sounds reasonable though
15:49:25 From danny to Everyone:
dead at the foot of the hill
15:49:31 From Micah Zoltu to Everyone:
Already dead?
15:49:35 From danny to Everyone:
might me
15:49:37 From Łukasz Rozmej to Everyone:
we can propose anything, reality will verify it
15:49:47 From MariusVanDerWijden to Everyone:
10.7 SGTM
15:49:53 From 0xnako to Everyone:
early to mid may!
15:50:27 From danny to Everyone:
5 times\* or something like that
15:51:17 From MariusVanDerWijden to Everyone:
I think we'll probably spend one ACD max on it
15:51:25 From lightclient to Everyone:
makes sense
15:51:38 From Tim Beiko to Everyone:
I’m happy to also have as many of these convos off the call as possible and summarize here again
15:52:30 From lightclient to Everyone:
i feel more comfortable with 10.8 and set an agressive code complete date of feb 1
15:52:52 From danny to Everyone:
what does 10.7 and 10.8 map to in our best guess?
15:52:59 From danny to Everyone:
is 0.1 a month?
15:53:04 From lightclient to Everyone:
10.8 to me is beginning of june
15:53:06 From Micah Zoltu to Everyone:
0.1 ~= 2 weeks
15:54:26 From lightclient to Everyone:
i'm also be happy with 11m but continue with the agressive timeline to try and merge before june
15:54:30 From Micah Zoltu to Everyone:
The difficulty is continuous, it is always happening.
15:54:43 From lightclient to Everyone:
10.7-10.8 == not much room for error
15:56:23 From Ansgar Dietrichs to Everyone:
10.7, but okay with pushing back further seems okay
15:58:21 From Micah Zoltu to Everyone:
13,773,000
15:58:31 From Tim Beiko to Everyone:
https://etherscan.io/block/countdown/13773000
15:58:46 From Ansgar Dietrichs to Everyone:
Sorry about raised hand, different zoom client
15:58:47 From lightclient to Everyone:
13,337,000?
15:58:54 From lightclient to Everyone:
haha
15:59:27 From Micah Zoltu to Everyone:
The trick is to wear everyone down with the harder conversation first, so the rest go quickly. :P
15:59:51 From lightclient to Everyone:
should use this tactic more
16:00:06 From lightclient to Everyone:
can we discuss 3074 now?
16:00:34 From Micah Zoltu to Everyone:
😆

## Attendees

- 0xnako
- Andrew Ashikhmin
- Ansgar Dietrichs
- Danny Ryan
- Diederik Loerakker (protolambda)
- Gary Schulte
- Joshua Douglas
- Justin Florentine
- Łukasz Rozmej
- Marek Moraczyński
- Marius Van Der Wijden
- Martin Holst Swende
- Matt Garnett (lightclient)
- Micah Zoltu
- Paweł Bylica
- Péter Szilágyi
- Pooja Ranjan
- Sajida Zourahi
- Sam Wilson
- SasaWebUp
- Tim Beiko

---

## Next meeting on: October 29, 2021, 14:00 UTC
