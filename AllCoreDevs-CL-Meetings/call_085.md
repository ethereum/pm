### Meeting Date/Time: Thursday 2022/4/7 at 14:00 UTC
### Meeting Duration:  1 hour 23 minutes 33 seconds.
### [GitHub Agenda](https://github.com/ethereum/pm/issues/510) 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=rYWF7N8tS0g)
### Moderator:  Mikhail Khalinin
### Notes: Metago

## Kiln office hours

**Mikhail**
It’s so cool. Let us get started. Yeah, it’s an honor for me to run the call. Okay, so welcome to the Consensus Layer call number 85. Thanks, for the agenda. Let’s start with the first item, which is the kiln office hours. And I will start from testing updates, testnet and shadowforks. Pari, do you want to give an update on that front?

**Pari**
Sure. The last shadow fork we had was on Monday, that's Goerli shadow fork 3. Actually, since the last week, we had Goerli shadow fork 2 and shadow fork 3. Shadow fork 2 just had an equal client split, and we didn’t notice any major issues. I think Nethermind was able to figure out a few issues and Besu as well, and maybe one or two other clients, but in general, things went ok. Goerli shadow fork 3 was on Monday and we replicated mainnet client split. Since then, I think the geth team has been debugging a specific issue but it’s just affecting a subset of nodes, the network is still finalizing and people can try all sorts of sync tests against Goerli shadow fork 3. And just as a general announcement, shadow fork 1 and 2 will be deprecated later today, so please migrate to shadow fork 3 as soon as possible.

**Mikhail**
And what about the mainnet shadow fork?

**Pari**
Yeah. So I sent the configs for mainnet shadow fork yesterday on chat. The shadow fork is planned for Monday. I am currently syncing the nodes, and the corresponding beacon chain will be launched tomorrow. Config for everything is already on Github. There are group nodes, and genesis configs, etc. 

**Mikhail**
Cool. And is anybody welcome to take part in this shadow fork?

**Pari**
Yeah. Feel free to join. Because it is limited to genesis validators, I am running all the validators, but the main purpose of these tests are to test sync, so anyone can sync up nodes and join in. 

**Mikhail**
Great, and yeah. Just a reminder that this is the mainnet, so the disk space requirements are much higher than on Goerli, right?

**Pari**
Yeah. Definitely. You have to sync up a complete mainnet node. So I do suggest if anyone wants to join, you start now, so that you have a couple of days to sync.

**Terence**
Do you know how big of a disk space is required for a minimum, at this stage? 

**Pari**
I think about 5 / 600 gigs is enough? I have provisioned a 1 terabyte machine just to be safe. 

**Terence**
Got it. 

**Micah**
I mean, that depends on what node and what settings we are running, right? Nethermind, fully pruned, is under a 100 gigabyte? Maybe? I mean its kinda rude for the network to run that way, but if you just need to run something and you don’t have much space, that can work. 

**Pari**
Yeah.

**Mikhail**
Agreed. Very excited to see the first mainnet shadow fork. Is there any comments on the Goerli shadow fork that core developers wanna make or anybody else?

**Marius**
Yeah, so we are still investigating an issue on geth that happened on the last shadow fork and yeah, but it only happened on a small subset of nodes so if you see a bad block happening, then it might be likely because of the issue. 

**Mikhail**
Yeah, is it like a...the issue is about the bad block production, or any other relations to...?

**Marius**
No. Its…a valid block group is seen as bad and yeah.

**Mikhail**
Yeah.Probably tricky to debug. Ok, got it. Yeah, any other testing updates?

**Pari**
I just had one more tiny note about the mainnet shadow fork. Just be wary when using the mainnet chain id, so if anyone's trying weird transactions etc, they might gossip to the actual mainnet and you will be wasting mainnet ether, so please be careful. By default, there will be no transactions other running on this. I don't think anyone is reimbursing me for that. 

**Mikhail**
Yeah, thats a very good note. Thanks Pari. So be aware that basically the shadow fork shares like a state with the mainnet so transaction on there may also be included in a block on the mainnet, so it may accordingly change what the runtime time of this transaction will be. Okay, cool. I have a small testing update. I have been working on test coverage document. Just dropped the link into the chat. There is transition section that I have been mostly focused on, in recent days, and yeah, this is like kind of the shape of the document, what it would look like. This is just an example. This transition section has like raw checks parsed from the engine APIs back and like more appropriate testing scenarios that you might want to implement and via our testing tools. So, with respect to transition checklist, the work will still need to be done on other specs, so going to parse all the specs and also include the information from them into these scenarios, but you might take a look. 

Also, thanks a lot, Marius for the input on that, made some checkboxes marked already, and with the corresponding links to…that covers them, and for just the background, who haven’t noticed this, it’s been announced in the previous ACD call, I mean this effort, this is literally going through all the stacks and just parsing all the statements, and putting all the checks that need to be done to test the merge and software and then make it in a good shape and then go and cover these checkboxes with what already implemented via testing tools and yeah, work on what happens next. 

**Terence**
I guess I can also give a quick update. I am also working on certain set of manual test cases for complex issues. So these are like the issues I thought of, they are like harder to trigger in a way that it’s not unitestable, it’s not really end to end testable, we don’t have them today…so yeah, looking for feedback if I am missing anything here if there is anything I should be adding and, yeah, please take a look and give us feedback. Thank you. 

**Mikhail**
Yeah, great. Thanks Terence. You want to share insight or whatever else you have on testing? 

**Terence**
Yeah, so besides that we have end to end test case, that we are actually implementing a proxy that’s sitting in the middle between the beacon node and the EE, and the proxy is able to manipulate the payload, it gets passed through, so it’s kinda similar to the test case that you mentioned but this allows us to easily get the syncing status back and forth so that we can test optimistic sync more smoothly for our end to end test. We have that. We are happy to share the progress on that a little later once we finish it. I am really excited for all this testing stuff.

**Mikhail**
Cool. Any other testing related items? Okay, so I guess we can start with the client updates. Who wants to go first?

## Other Client Updates

**Paul**
I can go from Lighthouse. We are working on the merge obviously. We have a full time person working on the testing now and kinda dealing with mostly little tidying up issues and just making sure that everything is locked down we can’t produce…when things are optimistic and also trying to make sure that our logs kinda make sense after the merge cause we are used to kind of complaining when F1 node is not synced but we need to do that less now because it’s kinda our job to sync it so just probably in the tidying stage and also testing. We have also cut a release a couple of days ago that enables to propose a boost on mainnet so Lighthouse uses to propose a boost on mainnet and production and other clients are well aware of this and looking at also running it as well. That’s about it from me.

**Mikhail**
And this F1 client syncing or yeah, this complaining things…its just logs right? Its not like anything is deadlocked or whatever? I mean the sync process?

**Paul**
Yeah, its just logs. Its one of the things where its just logs but it turns out to be very difficult to solve…but just logs.

**Mikhail**
Okay, I see. Thanks for the update. And about the proposal boost, I mean, it works now? On the mainnet?

**Paul**
Seems to be going there. I guess we will see as probably as more clients start to use it...an effect on mainnet, may be interesting.

**Mikhail**
Definitely. Great. Okay, next, I have Teku…

**Enrico**
Yup. Hi. We also have a new hire, which is Stefan Bratanov. We can see now he is connected to the call, welcome. We are working on the MEV-Boosting integration during these last two weeks and in terms of merge, we may be worth mentioning that we implemented another check in the terminal block difficulty detection actually, because we were not taking into account the block time stamp coming from the proof of work and in some cases, running some test nets, we’ve got a terminal block, but with a future timestamp and also due to a similar bugging in Besu in our testing…together…we were getting a block, where we are actually considering that terminal block to be good and we were then building next block in proof of stake with the timestamp which was before the timestamp of the terminal block, so we actually added a check, we discard potential terminal blocks that have timestamps in the future. Other things, yeah, that’s it.

**Mikhail**
What is the decision on the blocks that have timestamps in the future?

**Enrico**
We simply don’t care about that and wait maybe another block that has a timestamp which is in the past with regard with our consensus client time.

**Mikhail**
I see. Yeah, that’s an interesting case.

**Enrico**
Maybe worth to mention in your document as a transition test, maybe kinda weird but we hit that case.

**Mikhail**
I see. Okay, lets have a more look into this. Thanks a lot Enrico. Welcome Stefan. Okay, next one is Lodestar.																			
**Lion**
Hey everyone, Lion here. We continue with our merge work, all going well now, no substantial issues. We also have merge, substantial updates to our gossip and necessary libraries and hope to have them released soon and we have also keep iterating on like client proof of concepts, and we got a technical demo where we close the loop on the kiln testnet going from consensus all the way to showing execution data and we showed that in EthDubai, so fun stuff. That’s it, thank you.

**Mikhail**
Yeah, great. Congratulations on that achievement. Thank you. Next is Prismatic.

**Terence**
Oh, hey guys. We also have a release coming next week and that should enable propose a boost, really excited to see that happening on mainnet. Regarding the merge we have the soft r kiln branch, so everything lives in our main branch …so that’s very nice. We are mainly tidying up and adding more test cases. We are fixing the last few things in optimistic syncing, such as pruning, validating nodes,…from the db, and also just making sure when the ee goes offline or when the ee goes offline or ee times out, our beacon nodes handles it gracefully and we are also working on web3signer, that’s a pretty big one, that’s taking up some of our time, and yeah, thats it. Thank you. 

**Mikhail**
Okay. Thanks Terence. Next one is Nimbus. 

**Zahary**
We are also in the process of integrating our merge call into the mainnet branch. We are also looking into integrating MEV-Boost, we are also doing light client experiments. Nimbus currently implements system peer to peer protocol for obtaining light client updates and we are testing light client syncing in the… testnet our server is actually compatible with lodestar so you can also try this setup if you wish. We are also working on support for threshold signatures in the remote signup setup such that you can configure…with multiple remote signers in which remote signer is configured to operate with a partial key. And something quite interesting, starting from this week, the nimbus execution layer is successful in participating in the kiln testnet.

**Mikhail**
Oh, congratulations on that. Thanks, Zahary, and Grandin?

**Saulius**
We worked mainly on the small fixes for the merge and also work on the new feature which we didn’t have for a long time, just remote web3 signup…so that’s…main things…thanks. 

**Mikhail**
Thanks Saulius, great. Okay, so we also have el client developers on the call…spread the updates…?

**Marius**
Sure, I can start. We’ve been debugging the issue that I already mentioned and not much, that has been very hands on. 

**Mikhail**
Okay anything that can help you with the debugging? Probably enabling some tracing or whatever?

**Marius**
Not really. We don’t know how, so yeah, we are still looking into it, working on it.

**Mikhail**
Yeah, the worst kind of bugs are which are nondeterministic, right? So yeah, good luck with that. Any other client updates? Probably I have missed, some, anyone? Okay, since we are done with client updates, and yeah, as we are still on the merge topic, Tim, could you please give us like a quick brief walkthrough of the decision-making process? We have touched on it in ACD but it also makes sense to share it on this call as well.

## Merge Timeline Decision Process

**Tim**
The decision process for?

**Mikhail**
For where we are in forking testnets…

**Tim**
Yeah, roughly speaking, like there is a difficulty bomb on mainnet which is set to start sometime in May and at some point we want to decide whether or not we think the merge can happen before the difficulty bomb becomes too pronounced on mainnet, and just to give some background in case it’s not clear to everybody on the call, how the difficulty bomb works exactly, but it’s like an exponential increase which kicks in every 100,000 blocks, basically the amount of difficulty on the proof of work network gets like, there’s a fake difficulty that’s added by the difficulty bomb, making it harder to mine, so basically every 100,000 blocks or two weeks, like that amount gets an extra chunk added to it and that grows exponentially. 

Its very hard to predict, once its kicked in, once we go to a spot where the difficulty bomb goes from negligible to non-negligible addition to proof of work, its quite difficult to predict how long it takes because you then need to make estimates like how much the hash rate grows or shrink in that period and in the case of the merge, it might be the most complicated one because we might expect the hashrate would drop as we get closer to the merge. 

That said, we can do some rough ballpark calculations and last I checked, which was about a week ago, it’s likely we hit roughly 15, 15 and a half second block times sometime in July, and that by the end of July we would be up to like 17 sec block times if we did nothing. Personally and have been talking with a bunch different people, it seems like 15 second is like the maximum that’s like that we can tolerate before doing something if we go to 17 then the one after is 20 and then I think is 25, and its going pretty quickly and that gets noticed a lot on the network. So if we are hitting like 17 by the end of July, the one little buffer that we have is we might be able to bundle the execution client releases with a small pushback with the difficulty bomb so if we needed like a couple of extra weeks for the merge so you can have like a mini fork that happens on mainnet which just pushes back the difficulty bomb before we hit TTD.

So if we want to be in that world where we either don’t push back the bomb or maybe push it back only slightly but in the same release as the merge and don’t need like a whole separate network upgrade to do that, we need to be in a spot where by the last all core devs in April, which is like in three weeks from now, we are deciding about forking testnets. We don’t need to have like the exact testnet blocks and everything on that call three weeks from now, but we would wanna be in a spot where we are like, we are comfortable that in the next two weeks we are gonna sort that out and that you know, around mid May, we start forking testnets. 

This assumes probably something like we fork testnets every 2 weeks, and so the first one gets like 6 to 8 weeks of being forked, and the last gets around the order of 2 to 4, and there was some kind of contentious on all core devs about if that’s enough so that’s something that we also need to check in parallel. Long story short, late April is when we need to make a call about, do we think we are ready to now move to testnets, and we are not, then its probably the better approach to just have a small upgrade on the execution layer side, which kicks back the bomb a few months and we can debate how much we wanna kick it back for. 

**Mikhail**
Thanks Tim. And if I understand you correctly, if we wanna fork testnets in May then we probably want to have production ready clients in the beginning of May?

**Tim**
Right. Yeah, in our calls three weeks from now, what you would hope clients are like ready for testnets, and what still need to figure out is pulling out the release that supports the testnet and maybe some small, you know, say there is like a small tweak adjacent rpc, or something like that, that’s not the end of the world but like we should’nt be changing consensus related code at that point, yeah. 

**Mikhail**
I see. Any comments on that? Okay, the silence, wow, okay, just curious what does it mean. Okay. So, we are getting back to this in 3 weeks, right? To this, to the decision on what we do next and when?

**Tim**
Well, I mean hopefully yeah, the mainnet shadow fork will be a really strong indicator. Personally if we have the mainnet shadow fork and things go roughly the same as it did on Goerli, that’s good, and if we discover a whole host of new issues then I think it is unlikely that we are in a good spot to be ready, but I don’t want to just table this for the next 3 weeks, I think that we are gonna have a lot of extra information that comes in the next two weeks and on the call next week and in devconnect 2 weeks from now and whatnot like and we can evaluate how we feel about things.

**Micah**
You are basically saying that in three weeks all clients should be basically prepared to be able to answer the question, are you feature complete.

**Tim**
Yeah, and if we are not in that space, like and if we are 95% feature complete then there’s like maybe some wiggle room whether do you want to do the first testnet…if we want to…if you are like 85% feature complete I think in 3 weeks and if that’s the case across several clients then I think it makes more sense to delay the bomb. And its obviously not just my decision, but assuming that we want the same deployment schedule and we don’t wanna rush them for the merge, yeah.

**Mikhail**
Yup. Makes sense. On the mainnet shadow fork, we are expecting to have one fork pretty soon, and we are expecting to have another one, on a weekly basis, or whatever, probably Pari can answer that. Pari, what do you think on the shadow fork on the mainnet?



**Pari**
Yeah, the plan is to have one every second week so we would have one on Monday and the one after that would be I think devconnect week Friday, so we would have atleast two mainnet shadow forks and we can still talk about another Goerli shadow fork if you wanted, I think doing three mainnet shadow forks at some point it’s a point of diminishing returns, like doing it two times a week might not bring us much. Its actually…mainnet nodes take a long time to sync. Its just…yeah

**Mikhail**
Yeah, I see. 

**Pari**
Not bring us much
**Mikhail**
Right, yeah. Okay. Anything else on the merge release timeline and related comments, what has been discussed and shared? Okay, let’s move on.

## Timeout on engine API calls

There is a pr by Danny. The timeouts on the engine API calls. So it’s basically said the timeout on the calls with pretty big enough amount of seconds for the calls that have the execution semantics in it which is the new payload of the fork_just_updated…also much less timeout and the requirement is that the consensus layer must just expire the call by timeout, yeah, so that’s it and there is a like a reasoning about it in the comment in the pr, so please take a look and we are expecting input on that. Do you want to discuss this engine APIs timeout right now? Okay, so let’s just then move to the…

**Tim**
One thing on the timeout is, does anyone feel like a 120 seconds is too quick and maybe this is more a question like for the el side, but like the idea of like a 10X difference in execution between the high end hardware and the low end hardware is kind of what the120 seconds is predicated on and so that would be helpful, is like, is there a case for like, actually this should be 10X, or this should be 15X for something, something that is kind of easy to change as well, but yeah, I think if people have that kind of feedback, it would be really good to get it now. 

**Mikhail**
Yeah, sure. Thanks Tim. Yeah, also to add from my end, on the timeout stuff, as Danny stated in the comment to the pr, there is a point when waiting for a block to be executed by execution layer client is not valuable after some point in time, so and probably it makes sense to have like timeouts as huge as the number of seconds in the block because in this way so the chain will be able to still making progress, in terms of consensus layer blocks…but its still theoretically possible for the chain to make progress so we can take a look at the timeouts from this standpoint as well, also another thought that I had on them, on the timeouts, is that there are two operation modes that el clients have. It’s basically syncing and blockstamping, when the N node is in sync with the network and to receive a block via gossip and sends it to the payload to the el, probably in these two different cases, timeout should be managed in 2 different ways so there are things to consider on this topic, so please take a look. It’s very important because so recently these timeouts have been mentioned many times in discord and in many discussions, so it’s gonna be an issue if we are not being able to specify them correctly. 

## LatestValidHash

Okay, the next thing to discuss and to remind people about is the LatestValidHash stuff. So we have touched base in ACD and yeah, this big thing is, it is gonna be like resolved sooner than later because we need to be sure that we are on the same page with respect to this requirement, and this spec. So there is the LatestValidHash that the el client has to respond with, when it has been syncing for example and found that some payload in the chain that it has been catching up with is invalid so it should respond with the latest valid and sister hash on the next cl call, so el would have to store some information about this chain until it receives the subsequent call from cl to be able to share this information. This is important for consensus level clients so it can invalidate not only the most recent payload on this chain but also all the invalid payloads, which starts after the LatestValidHash that is provided. Also, yeah, the problem here is that the execution layer clients doesn’t store this kind of information today and it needs to be added and kept in memory and returned back to cl. 

What I have just shared is just my initial thoughts on how it could be implemented and the main question is whether we want to support this or whether we would like to explore like yeah, to reason about whether it is important for el client to respond with this information, while its been syncing, or it could be kinda of, you know optional stuff, because it’s gonna be there, the semantics will stay there, and the request format will not be changed because there are clients like Aragon which may execute payloads, have multiple payloads on fork_choice_updated and they need these semantics to respond accordingly if the real work is happening and multiple payloads are being executed while this payload is invalid then this client may immediately respond with the LatestValidHash information and this is valuable and important for cl clients in this case. Yeah, but for the syncing case, there is a question on that topic. So please reach us out me out in discord, comment on this document, so we are about to make decision over the next week on that. Any questions or comments with that regard? 

Okay, lets move on. So we have, yeah, as long as we are on the merge topic still and the MEV-Boost has been mentioned here by several developers, Lightclient, would you like to make an update on your recent work on the spec?

## Builder API / MEV-Boost 

**Lightclient**
Yeah, thank you. So for context for people who have not been following much with the builder API or MEV-Boost, this is the interface for cl cl blocks for external builders and it was changed from a middleware design sometime in the past few months where MEV-Boost would sit between the cl and el and route force_choice_updated and get payload calls to the builder network to a separate service that can provide blocks to the cl and as far as I know this was originally proposed by Paul, and so a lot of the latest pieces of the spec have been derived from his ideas. 

The new approach does require some migration on behalf of the cl teams. So I am curious to know how far people are on integrating those things, but the things that appear to need to be implemented with the newer spec is that you need to implement the builder API which right now has 3 methods, the BuilderGetHeader, BuilderGetPayload, BuilderSetFeerecipients, and then there are 2 types of signing that the cls need to support, one is blind block signing so they will need to be able to sign over blocks that don’t expose the full list of transactions. I’m not clear on exactly how that is communicated to the validator clients, if the entire data object is sent over or just the signing route is sent over, but that’s something that would need to be supported, and then they would need to able to support a fee recipient announcement and we tried to make it so that fee recipient is not something on the critical path for building blocks for a few reasons, one reason is that we are trying to move to a world where this more of a gossip based approach rather than a request response approach over rpc, so the validator client needs to be able to support signing a fee recipient announcement attesting that this is the fee recipient that they wish to accept funds at, and that would be on a different domain than normal block production and attestation signatures and then of course there would need to be some modifications on cl block production codes to try and get a block from the external builder if the external builder functionality is enabled. So the latest changes to the API and the…MEV-Boost and I will post the link here. I would appreciate any feedback on this. We will try to move it to the execution API repository sometime in the near future, but right now we are content to just develop it there. That’s the main update. If anybody has some feedback on that immediately, that would be great. 

**Paul**
But I do think that the idea of changing the names to not conflict with the engine method is a really good idea.

**Lightclient**
Great. We have also tried to just simplify before there was any concept of builder methods and relay methods, and we are trying to just simplify, more so that MEV-Boost is a piece of software that exists out there but design isn’t really built around it, it’s just built around the concept of retrieving external blocks and MEV-Boost is already a candidate for utilizing that functionality but you could directly connect to a builder that supports the API, other people can implement software, its less bound to certain you know existing implementation.

**Paul**
Yeah, nice. I saw there was a little bit of chatting in one of the merge discords about other MEV people getting involved, I haven’t really had many other people reaching out to me, I think Blocks reached out to me, certainly might wanna consider maybe moving the API away from flashbots and into perhaps a neutral repository, its maybe not an immediately a problem but just maybe a long term goal to consider.

**Lightclient**
No, that’s a short term goal for me, I think, you know, in the next few weeks, we will try to move it to the ethereum repository. There is a different way that we need to be approaching and this. I feel like the Block building API spec is something that has sort of just lived external to a lot of the discussions around the merge and to me it feels like this is something that should be an important part of these discussions because in all likelihood you know, most validators are going to be using this software and so you know, we as people in the consensus and execution layer should also be spending time that that is as robust as the other pieces of software that we are working on.

**Arnetheduck**
I mean, this raises an interesting question, right, which is that I mean, this basically becomes another part of the attack surface on Ethereum. I mean the networks are not able to produce blocks and clients rely exclusively on them as sources, we have a problem, right? So I think would almost require that clients implementing this feature would also implement the fall back where they make sure to have a block ready from traditional sources as well. And this is important both for censorship reasons and yeah, just network boundaries, right?

**Lightclient**
I agree. 

**Paul**
Yeah, I think its critical that if the builder gives you a payload you use your ee to verify it, you don’t just assume its valid, so that is a kind of a bit of a correctness guarantee and then like you said you have to, if they don’t give us anything, or its invalid, we do have another block to pick up, probably 2 key safeguards we can use here, it won’t stop the builders from causing havoc and hopefully keep the chain correct and live.

**Arnetheduck**
We can’t verify a blinded block, like the transaction whether the transaction therein are valid

**Paul**
Builder is a separate entity, so you would have…

**Mikhail**
Paul, you are muted…

**Micah**
I think he disconnected.

**Mikhail**
Yeah, I also agree with that. It makes sense to have an…document with cl clients…with the fallbacks and the other stuff, what Paul has mentioned and …also yeah, if there is a builder who produces bad blocks that are invalid, I guess they are gonna be on a reputation system so we quickly sort this out and just this kind of disconnect from these kind of builders, am I right?

**Arnetheduck**
I don’t think a reputation system necessarily works. Reputation system blocks are problems because you are reputable until you are not, and I think that the attack here….yeah…

**Lightclient**
I was just gonna say, it only works if you can attribute a fault to a builder like if I can create some sort of proof that they told a validator that for some slot they produced a block based on one input and they built a block based on a different input then we can attribute to the builder and we could say like…other validators to disconnect from them and removing them from that and that could protect from some instances but the worst case is if the builder simply withholds the block that they were gonna release and there is no way of attributing that fault to the builder.

**Arnetheduck**
Yeah, indeed. There are a number of these, like liveness issues, right, where a couple of invalid blocks get produced in a row with no way for the validator to really, validate or not before signing us on. 

**Ansgar**
From our perspective, the important question should be like where do we draw the line between responsibilities for like the MEV systems flashbots or whatever system. They are like small issues we should not be concerned with…that’s not really our concern but of course it becomes our concern if there is like a big area where we really want to be able to notice that and switch over manually maybe even just disregard the MEV-Boost or something…and where this emergency, disregard MEV fallback kick in I think. Because otherwise it shouldn’t been our concern.

**Lightclient**
Right, I think like a reasonable expectation is one for cl clients to implement a fall mechanism where they do continue requesting their local el to build a block and that would protect from whatever the fault is attributable and you can see that there is an issue with the block that you are trying to propose and you could just propose a local one that you built and then the fallback mechanism for these other types of liveness issues could be is if we haven’t seen a beacon block come with an execution payload in n number of blocks to just disregard builder blocks until some threshold is met again just so that we avoid these like really bad situations where we are going epox without any actual block being produced.

**Ansgar**
Right, but even that aside, because but you don’t actually see, if you just look at the beacon chain like you don’t know whether payload you are looking at actually came from the MEV network or not so you decide a threshold of saying if there hasn’t been a valid payload in 10 blocks then sure, after10 blocks of no payload …one valid payload but then manually trigger the next ten blocks to just try to use MEV again which would work and so it would always oscillate whether blocks are coming from the MEV bnetwork or just from people manually using their clients, so its not easy to

**Lightclient**
Right. I mean yeah, these are all hacks to maintain liveness and not an optimal system for dealing with the fact that we have centralized block producers and that we need to continue working towards having n protocol mechanisms for dealing with these situations.

**Ansgar**
As long as we have these specs…as well as possible…is there any way to atleast whenever we see payload see whether that was produced by an external block builder or by a validator himself or something?

**Lightclient**
Hopefully we would be able to get more information whenever we switch to more of a gossip approach to external block builders, rather than right now directly connecting to them. That way you as a member of a gossip network could potentially see that these payloads were coming from a builder, but again it doesn’t protect from if the builder is withholding

**Micah**
We could request all clients put something in the graffiti, if they are using a builder versus local. It’s not enforceable, but defaults are powerful. We could get 99% of people to go along, it’s just default.

**Lightclient**
Sure. I don’t know how deep we wanna go into this discussion right here but I do feel like that this something we might wanna consider talking about more..more conscious about situation…

**Terence**
I also find like there is no one from Flashbot here, I feel like that this would better, a better place for this discussion would probably be biweekly having a sync up with the flashbot team and just go over the spec.

**Tim**
What do you think is a best format for that? Is this like a call that’s hosted by flashbots?


**Terence**
Right. Last week, we had one in the MEV / Flashbot group in discord and Neal from flashbots hosted it…Im not sure when the next one is but I think they are planning to do this quite frequently.

**Micah**
I think if our goal is to be less flashbots centric and be more open to flashbots competitors we should perhaps start by just having someone else host the meeting, like the Ethereum foundation or…

**Tim**
Right, and I guess the reason I am asking this is because is this a flashbots meeting or is this like a general block builder meeting, because I think that one of the reasons why flashbots doesn’t send people to all core devs and stuff, aside from maybe having better things to do there is like this fear that they take up the time and space in the core protocol stuff with their private stuff, but it does overlap, I think that they’ve been mindful about like how to manage this interaction but if it makes more sense, then have it like an EF thing, we can do that, the question is also like, how do you make sure we don’t just overload people with meetings because there is like all core devs consensus layer, flasbots call or MEV call, yeah

**Lightclient**
I don’t know if it make sense to have something similar to what we’ve been doing with ACDs having those breakout room calls for more specific topics, because if it’s something that is important to all cls but there is usually one person from a cl who is representing and working on a area. 

**Tim**
Yeah, I think that makes a lot of sense and it doesn’t have to be like a recurring thing for forever as well. We can have a couple…and we see…yeah…want more frequent…yeah

**Lightclient**
I have been working very closely with Flashbots on this the past few weeks, and like I have generally been pushing to avoid in tying anything related to Flashbots into these concepts including removing the term MEV from any of these APIs, like I don’t think that any of these things should be that opiniated, we are just working with an external block building protocol, not flashbots itself, and that should be done in an open arena.

**Tim**
I am mindful that there is like devconnect two weeks from now, but do we wanna schedule either next week an MEV breakout, or maybe wait to see, like I know that there is like an MEV event at devconnect and other flashbot people will be there so do we wanna like, wait and see if there is just like organic interactions that happen there and then kinda followup after Devconnect?

**Mikhail**
Probably people will be busy next week with traveling and some other stuff.

**Tim**
Yeah, but yeah, it’s definitely, we can, I can make sure that we touch on it in person there and then like after devconnect, we organize something that’s open where we can discuss this. 

**Mikhail**
Great. Yeah, before the call and devconnect please go to this pr, take a look at if this design is like, if that’s pretty optimal, separation of concerns…lightclient work on it…this is very important and it’s been mentioned, so the more eyes we have on it the better for the end goal, for the end design, so go take a look and comment out. Anything on that topic, before we move on?  Okay, anything else merge related? Cool. 

Next step is other client updates. We have a bunch of updates already but probably somebody wants to share anything else not related to the merge? Okay. The next one is research spec and other things. There is ongoing work on partial withdrawals and the withdrawals in general. Alex, do you want to give any update on that?

## Withdrawals

**Alex**
Sorry, you are asking about partial withdrawals?

**Mikhail**
Yup, I mean the withdrawals in general. 

**Alex**
Yeah, not too much other than the prs. Dave’s been looking at this from the cl perspective so he would have the most contacts here. I guess, if anyone is curious, take a look. The changes I think are not too wild and as far as I know the latest there is its just tuning some of these parameters and how frequently we go over the value set to either do full withdrawals or this case the partial withdrawals, so yeah, I would just take a look but I don’t think that there shouldn’t be like any big open questions or anything like that. 

**Mikhail**
Cool. Thanks Alex. And yeah, when is it expected to get merged?

**Alex**
I don’t know. It’s definitely not, you know, the top top priority, because we are all focused on the merge but maybe in like 2 weeks, I mean I am just making up a number, Yeah.

**Mikhail**
So its gonna be soon. Dankrad, you wanna say something?

**Dankrad**
Oh no, sorry. Just rejoined.

**Mikhail**
Okay cool. Yeah. anything on withdrawals? Questions? Comments? Okay cool. Take a look at pr…Some of the like initial pr has been already merged…as well. Nice, great, so, yeah, anything else on research and spec topics? 

## Networking prs 

Okay, I want to remind that we have a couple of prs in the networking spec and we are expecting more input from engineering side. Yeah, please take a look at these prs. It shouldn’t take like much of your time…but these are reasonable changes in the networking spec, and yeah, please take a look, comment out, and so forth. One of them is the deprecation of step rendering beacon blocks by range and another one is ignorance of subset agregates…so any comments on these two? 

Okay, cool. So it seems like we are done with the research and specs stuff. Next one is open discussion, closing remarks. Does anyone have any other updates, announcements, they wanna share here? Okay, so we are going to cancel the next consensus layer call because we will be meeting in person on the devconnect so the next one is not gonna happen. We will meet each other in this room like four weeks after. Okay, I think we are done.

**Tim**
Yeah, one quick thing though so the next cl call is 4 weeks from now but in 3 weeks, well next week there is all core devs, and 2 weeks after that, the week after devconnect, we will obviously cover all the merge stuff there too, so consensus layer folks who are working on the merge please show up to those if you can. 

**Mikhail**
Thanks Tim. And yeah from like lightclients v block production channel discord to discuss the MEV-Boost and other…stuff. Okay, thanks everyone. See you soon. 





## Attendees (30) 
- Mikhail Kalinin
- Tim Beiko
- Lightclient
- Terence
- Pooja Ranjan
- Micah Zoltu
- Lion Dapplion
- Zahary Karadjov
- Saulius Grigaitis
- Ben Edgington
- Marius
- Ansgar Dietrichs
- Paul Hauner
- James He
- Casper Schwarz-Schilling
- Hsiao-Wei Wang
- Carlbeek
- Pari & Proto
- Enrico Del Fante
- Stefan Bratanav
- Trenton Van Epps
- Cayman Nava
- Arnetheduck
- Stokes
- Dr
- Mario Vega
- Leonardo Bautista
- Marek Moraczynski
- Tukasz Rozmej
- Shana
