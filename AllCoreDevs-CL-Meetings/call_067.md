# Ethereum 2.0 Implementers Call 67 Notes
### Meeting Date/Time: Thursday 2021/07/01 at 14:00 GMT
### Meeting Duration: 45 mins
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/224)
### [Audio/Video of the meeting](https://youtu.be/FNXk4ScqHn0)
### Moderator: Danny Ryan
### Notes: Santhosh (Alen)


## Decisions Made / Action items
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
| **67.1**   | Target forking Pyrmont by end of month, with a full decision to made in our next call. | [19.42](https://youtu.be/FNXk4ScqHn0?t=1182) |
| **67.2**   | Perry, Proto and Danny will discuss and propose like a configuration for a Devnet launch at the end of next week. We will propose it soon for the end of next week.| [23.05](https://youtu.be/FNXk4ScqHn0?t=1390) |



**Terence**

* Welcome to Call number 67, Altair Focus. Obviously, let's do a client updates with focus on Altair's status. Then we will discuss the bit about Altair planning and then general research updates and open discussion from there today. Let's go ahead and get started with Prysm.

## Client Updates [2.57](https://youtu.be/FNXk4ScqHn0?t=175)

* Yes, so the  here, we have been mostly working on a Altair so we align with the latest fag. We implemented all the internal node and the validate interactions. We are almost done with the networking side of things but we have started interrupt internally already so that is pretty much working. There's a few bugs to I have here and there. They're so we very soon will beinterop with the Teku devnet that a dream set up. So thank you for that. So yeah, that's pretty much it and other than that, just keep seen P0. Many parts here and there. But yeah, most of our efforts on the Altair front, thank you.

**Terence**

* Lighthouse.

**Adrian Manning**
* Hi Everyone similar to Prysm, we've been working on Altair. So I think we've recently finished all the validated client features we're increasing testing at fault boundaries and I hang out bugs. And in the they say that we've done all the Alpha 8 changes Altair changes. So they've all been implemented. So we have, we've been compatible with Teku which has been compared on the on the dev app that take a setup. So we're ready for multi-client Altair test. That when The other clients are ready to do that. We've also been upgrading a number of some of our sub networking components. So, Discovery and gossip said, I've got a big networking refactor, which should come out and next release, which will be 1.5 as a fair amount of testing to do on that. So that's pretty much it from us. 

**Danny**
* Great. Thanks, Adrian. Teku!

**Adrian Sutton**
* Yeah, we're ready for Altair as well. Are we actually haven't had too much more to do on that. The latest gossip trend is from Alpha 8 changes and seem to be working very well. Big stuff has been we've added in batch signature verification for attestation gossip which is reduce CPU, usage, quite a lot. So that's in that. Twenty one point, six point one release, it was out yesterday or the day before. We've also enabled, I think I mentioned it. Last called the time-based equine head-tracking. It's just a line, this with spec correctly. It didn't doesn't make much difference on Main that is 2048 blocks in the time. Allotted anyway, the box come faster than we expected. We've been doing a bunch of work on Discovery and search for pointing out that we weren't weren't filling our buckets as well as we could there. So, there's been a few improvements there. We kind of continuing testing that it'll take a little while to roll out, but that's coming. And we're finally actually going to switch over to using the dependent Roots. We added to the standard API taken quite a while to work out, why there was a very small production in Ward's and for them. And it came down to the particular timing of, when the full four choices run and making sure that because the second node and ballet the point where not as much in sync going to make sure that that ties together. Well, so it's there are, there's been actually wrote some code which is nice and patching of the G2 check. So, that's another performance Improvement and has been actually the auto work. We have been doing is getting Quick 3 signer ready for that. So the external sign owes under way, I think it should be pretty close to ready to support out there. 

* Yeah, so the one bit of sad news, I'll take a moment to thank Meredith. She's actually moved on from seeing as she's supposed to be a CTO. It's hard to argue with Billy's really great opportunity for but that leaves a hole for us, and Meredith has been a huge, huge asset for our team and a lot to push things forward. So, I want to thank her and we're hiring in one's.

**Danny**
* Thank you. And thank you Meredith. Good luck on the next Ernie. Lodestar. 

**Cayman Nava**
* Hey everybody on the Altair front. We're on Alpha 7 and we are updating to Alpha 8 right now. At least I'll Alpha 7, I think everything is implemented and looking stable on our depth Nets. Other than that, we've not are related. We updated our logo and branding refreshed that looks pretty nice. I think and we've also made a benchmark tracking tool for our CI to track benchmarks across convinced and tell us when we have regressions in things been really helpful even so just few days we've had so far. Also adding any more metrics data database metrics, and for Choice metrics, try to get a better handle on what's actually going on. And we've improved performance and our gossip at this station validation. It's not the about the batching, the signatures were going to look at that next, but it's just fixing up some stupid things we are doing. The last thing is we're trying to get together a little demo or like client work. That we have been working that we've done so far or figuring out like client initialization and how to cash and serve. The proof is necessary to initialize the like client with the sync committees and Genesis information. It depends verify the rest of this very thing. And that's it for us. 

**Danny**
* That's you came in Cayman, regressions and performance and see eyelids. It's a good idea. Nimbus!

**Mamu Ratsimbazafy**
* Hi, so we're getting out Altair here. We are passing the Alpha 8 tests. We are a teaching or fizzing interface that my Prime can plug numbers into them. Fizzing framework with Altair changes. Otherwise we released 10 days ago, Nimbus 1.4. So it has a couple of Improvements regarding anticipation, Effectiveness, and CPU usage. Mostly coming from Improvement in database, and caches, and we are also a bit hit or added rest API endpoints, and fixed a doppelganger detection. When we restart Nimbus last, and that's it for us.

**Danny**
* Got it, thank you. And Sally hasn't joined us, who is on the team that just dropped the client. What is the name Grand in? So if you want to just do a quick intro and let us know what's going on there.

**Saulius**
* Yeah. Hi everyone Saulius from Lithuania, Estonia Lithuania. So yeah, it was a bit of a rough start with a binary release that we have. Now, I hope that people tried it a bit and if you have some feedback then let us know. Well, the key things are see. You probably seen the read me. That we have some cross-platform support for currently for Windows, and Linux and Mac OS. So we actually test on Linux, only, and if you find the, if you should test on other platforms, there are high chance that something doesn't work Billy. So this report if you should, we should have some time to test it and check it. Then Appear, some, some other things that there is a basic user interface which was very helpful for me personally, special for debugging the artist, Staters performance. So it's nice to have a fisherman was comfortable. For me was very helpful, so you only try to check that too. So probably that's all for now. As You probably know it's at the moment, it's on the binary version, but, but we are looking for ways to to open source code. So if you have any question, feel free to ask it now. Thank you. 

**Danny**
* Quick update on testing for review Altair planning, we are going through. I'll Altair test with a fine tooth comb to make sure that we have. Complete coverage xiaowei is also looking to continue to enhance the fork choice test as an open PR. We're doing some review on right now so generally we might see some like small non-feature modification releases that just continued enhanced testing and someone asked on the Eth Discord if when we have to Beta. I think once we have all clients interrupting on it a devnet, we can call We can call the, the subsequent release of beta until then still some blind spots. It's a cool to any other testing updates, 

**Mehdi Zerouali**	
* It's not really not much that I can share, really. We've been reaching out to client teams that for which we've identified potential vulnerabilities and yeah, got some good feedback there. Things are going quite well, we will be kicking off. Actual differential, part of the fuzzing effort in the next couple of days. Really we're just waiting for most clients to stabilize and be up to offer seven author eight which has been the case for the last few days and you can definitely see that the consensus code has been there almost stable. Yeah going well hoping to get a bunch more fuzzing Cycles before we start forking a test Nets but I'm hopeful that we'll be able to fit those in. 

**Danny**
* Great. Any other testing related updates before I move on? Okay. 

## Altair Planning [15.04](https://youtu.be/FNXk4ScqHn0?t=904)

**Danny**
Planning, we are on the cusp. I know everyone's kind of really just getting the pieces together. The final pieces of Altair together. Thank you Adrian again for standing up that small DevNet has been really useful. I think the next two major things to do are to do a probably slightly larger more coordinated. Devnet. I and the There would be two probably Fork Pyrmont to give us an idea of working. One of these tests that's in production pair, not is slated for to be Pyrmont after our Sunset. I don't know after the Altair fork and so if we break, it's not too too bad, my current thoughts on both of those. And I will ultimately defer to your judgment on timing is to do a coordinated small but more distributed in terms of validator count node, count Deb net at the end of next week and Perry can help us. Give us a hand with that and then Set a fork date for for Pyrmont, in that like three to four week time Horizon. And then that we can use that as a Target to really iron out and get things ready for that. And then the success of that we can then Define a parameter and and Main that date, if that of course is successful, is that all saying in terms of timelines or are we jumping the gun? I'd love some feedback. 

**Saulius**
* So you would like to Fork Pyrmont first. 

**Danny**
* Yes, Pyrmont's the smaller one, correct? 

**Saulius**
* Okay this is great post as we run on nephew what the dates of validating some pigment and we are not ready for out there. Yeah. So yeah. So this will be very good for us. 

**Danny**
* Yes appear. Mama is I think the last thing we'll do is Pyrmont other than maybe some like leave some notes on for a really long time and see what happens, even things are not finalizing the last Want to do is do an Altair Fork if it breaks if we kill it. That's, that's fine because it is planning on dying. So that'll be the fourth, the first one and kind of dictate, I think prouder and may not depend on it goes. 

**Adrian Manning**
* So that's your plan for the first multi-client testnet for Altair on to do it on payment. 

**Danny**
* No. So in I suggest that we do a smaller Devnet in a week's time. but to set a date today for Pyrmont, To keep things rolling. 

**Mehdi Zerouali**
* My take would be to wait another two weeks before setting it down payment. just to see how the clients, behave on the actual Devnet.

**Danny**
* Any other input on that one? 

**Adrian Sutton**
* And it smells like go ahead. Let's get sounds like most clients of have tried at least thinking young Filly. So we've got a pretty good chance of this working so I'd be inclined to to set a fork date, but p.m. on very optimistically and we should be okay. It's only been a month. 

**Terence**
* Yeah, same here. 

**Danny**
* Okay.

**Jacek Sieka**
* So weak what we can do is set a tentative date and then, as long as it's after the next meeting, during the next few can confirm it. 

**Danny**
* How, what percentage of the network do we control and pyrmont? Is it? 

**Jacek Sieka**
* It's over 2/3, still Yeah, significant okay. So even if we give people not that great of lead time the network and can still carry itself, 

**Danny**
* Okay? So I would, I would suggest that we do the pyrmont fork. Pretty much three weeks from today and we will do a final confirmation. We'll do a confirmation of that two weeks from today and pick a precise Epoch number. Assuming that Dev net or DevNets have gone well between now and then.

**Mehdi Zerouali**	
* Okay. From the conversations we've had with the team. Yeah, I do think it's too short. 

**Danny**
* Too short, because 

**Mehdi Zerouali**	
* Because it'd be great to just have one. They've met with all four clients first and see how that behaves and set up a bit later on. I anticipate a fair bit of issues. Once we have all four clients on the same network but you know that's just me might be wrong. 

**Danny**
* Fair. But given that we plan, I think having a having a Target week. We'll keep keep things moving. And so next in two weeks we can kind of confirm that, I think that if we fail to get a definite standing up or we have many issues than in two weeks time, we'll say, you know what Pyrmont needs to be pushed back this amount of time. I just I do think that we need to at least have some Targets in place, not that we're cutting Epoch numbers and to release this currently. And that Target. But yeah.

**Jacek Sieka**
* Yeah, sorry, so one thing to consider is that EthCC is coming up that's in three weeks time, 

**Danny**
* Exactly. That the 22nd.

**Jacek Sieka**
* Yeah, I think 20 to 20 seconds right now, might not be the best week for upgrading their Pyrmont. Okay. So let's do this. So I would aim for the week after that, which, which helps Both have time to rehearse, this and also avoids. Forking when people are traveling, okay? 

**Danny**
* So, let's say this. I think that we should Target doing the Pyrmont upgrade at the end of by the end of this month, Target, and that the devnets. Over the next two weeks will inform, whether that Target is actually realistic. And then on the 15th on this call, we can take some time to discuss. What's happened in the prior two weeks and reassess that Target if not nail it down. 

**Mehdi Zerouali**	
* That sounds very reasonable. 

**Danny**
* Great. And what happens over the school course of this month will inform what we do with prouder and may not. Obviously, I think there is a lot of testing to do is a lot of fuzzing to do a lot of ironing out to do. I don't want to do this. To quickly. But I do want to begin to kind of move into that production version of Altair. Okay. Perry, Proto and I will discuss and propose like a configuration for a definite launch at the end of next week. We will propose it soon for the end of next week. That's all I had on Altair planning we can just open the discussion for if anyone has any other points to discuss with respect to Altair planning out their testing Altair features or other issues that we want to bring up anything on Altair today. 

## Open discussion [23.49](https://youtu.be/FNXk4ScqHn0?t=1429)

**Saulius**
* Maybe a question for me is so this is a first for the hot Park and maybe teams could share the biggest lessons that they learned in terms of odor organization. Did you figure out something that, you know, something that's extremely valuable that you would like to share 

**Danny**
* And if not here, we can take it to some async conversation, he's Hardy Adrian Journey thing to sure. 

**Saulius**
* There are statistics, I think about nothing different but each client is different languages have different capabilities that. Yeah. Well down to that a lot.

**Adrian Sutton**
* Yeah. We leverage what we've done in place a lot. So probably wouldn't think that thing that 

**Saulius**
* We are exploring now is how completely separated runtimes actually not completed but it Summer isolation between it. So as it looks like next to hardcore, may be more complex and it's always a bit complicated to support to branch code basically and support the old version, basically support all the works there and there was just thinking maybe somebody else also had this idea to go to to try to do. Something like the different. So almost separate on times for each for lives together. As long as it's needed. Later, switched to the new Fork. I'm just sort of in wondering, was this idea? Explore it. And if somebody explored it, maybe, maybe already know that it doesn't work. 

**Jacek Sieka**
* I think what most of us is done in general, is actually look at the code of the other kinds and so we judge that for ourselves. I mean, we've learned a lot from Well, the other times ready? Looking at the PRs that implements particular features, and those PR's represent, what works in different languages and Designs, right? That's probably the best-looking, which is nice with the open source model that were using 

**Saulius**
* Okay, thanks. 

**Adrian Manning**
* We haven't considered running having to be different runtimes and switching over. I think that the fork changes allow you to I guess seamlessly move through the fork on a single run time. So I think that's the path we're going. 

**Danny**
* Yeah, I haven't seen that done. On the Eth, one side Ether. Although I've I've contemplated it before but I'm not a client engineer. 

**Adrian Sutton**
* It's true. Everything was Branch by abstraction, so it just kind of fits naturally with the way we develop anyway.

**Micah Zoltu**
 * Okay, thanks, it's late. Just like the engine, but isn't there a bug that was introduced recently? The because it wasn't a consents failure because everybody copied the code rather than the spec this is discussed and I think Eth2 and on Eth2and R&D Discord earlier tonight. 

**Danny**
* That was a an edge case on the fork Choice implementation, Yes. 

**Micah Zoltu**
* Yes. Yeah, so just a comment on like one of the big things that Ethereum makes a great as the multi-client idea and everybody building the client independently, you're more likely to notice when someone introduces a bug if everybody is just copying an apartment or whatever it was thing first we lose some of that benefit because we don't have independent implementations anymore. I'm just only think about I mean, obviously the strategy that actually gets code written as the best one? Just keep that in mind. 

**Saulius**
* Do you apply this to my question or this is a it was a different, 

 **Micah Zoltu**
 * I know. That's right. It is really not for your question. This was one of the answers, just think about it. 

**Saulius**
* Okay. I mean this this if it's actually relates somehow to my question then, I mean these these run times, let's say, let's just call this separate runtimes. I don't think this introduces anymore clapping because if you have one runtime, then You'll heal them food, the code. That is not different between the heart works. Then you still have the same code or on. This is a copied code, the code, in case of the Run pipes or prefer to separate times, so just mine. Oh yeah. 

**Danny**
* And I certainly see the desired relax and you can keep your single kind of code base relatively clean and just refer to Old releases. I think some issues you might run into our cross Fork, boundary API, calls and other types of things like that where you ultimately would probably need some sort of like, meta, orchestration between, run times that are maybe running at the same time in perpetuity. 

**Saulius**
* Yeah. Definitely would be some type of routers or something like this, which, which is common for for these multiple run times. 

**Danny**
* Yeah, yeah. I mean, I'd be really interested to see that method of working explored 

**Saulius**
* Okay, cool. 

**Danny**
* But I cannot claim if there are any critical pitfalls that you're going to run into.

**Saulius**
* Yeah, this time that this is experiment that may lead to register. Wasted resources could be some, okay? 

**Micah Zoltu**
* Let me be great to like, read a blog post whether it works or not. I've also thought about that model and wondered why no one did it.

**Danny**
* Okay, thank you. Anything, other Altair related. Okay, let's move on to research updates,

## Research updates [31.36](https://youtu.be/FNXk4ScqHn0?t=1896)

**Danny**
 we had the emerge call an hour prior to this call. That has been recorded and will be shared sure relatively. Soon the I think in terms of things that are related to this call, there will be the merge code will be re based on Altair sometime in the coming weeks now that Altair stable and they're beginning to be robust implementations there. And the execution payload I believe needs to be modified partially with the for London. So both of those changes will happen. Sometime the next month, we will also be continually expanding test vectors on the merge and figure out how to just better test it in general. Those are the probably irrelevant merge updates here again. Check out the call, check out the notes. If you want to dig in deeper what happen, there are there any other research updates that people like to share today? 

**Leo(BSC)**
* Just comment on the metrics standardization. We finally got some set of standard of metrics to standardize across all the clients. I think party has already PR ready to be merged and yeah, so thank you to all the people that work on this. And this could be that just the first set of metrics. And then we are after we implement this. We plan to move on to two different ones that are not implemented by all clients at this point, but and we would go on those slowly return. That's all.

**Danny**
* Thank you. And remind me, Leo, where, where is this standardization happening? Which repo?

**Leo(BSC)**
* Parithosh. Did you have this? 

**Parithosh**
* Yeah, it's on the Eth2.0 Matrix repo(https://github.com/ethereum/eth2.0-metrics). I think, I think I still need access to push their. 

**Danny**
* Okay, cool. I can do that right after the call. Can you drop a link in the chat? Just for Refresher. Any other research updates, any other updates at all? Okay, General open discussion, anything speculated closing remarks, anything on anyone's mind.

# General open discussion [34.04](https://youtu.be/FNXk4ScqHn0?t=2044)

**Adrian Sutton**
* Put a PR for to change the default vote, for, for each one beta that the honest validator spec sets currently, it says to, to use the EQ on data from the state, which most clients don't actually do and it causes problems, because it leads everyone to vote for no change. Basically a new waster of voting period. So, the two options are basically either vote for, thank you either vote for a random block, which means you can't tell whether you just didn't have that block or whether that's just they didn't have any blocks for anyone, not at all. I've suggested setting it to zero so it becomes very obvious, but it does then mean that we've got to add a check in to the state transition to make sure that we don't have a actually vote that in if nobody has on data. We can do it as a soft Fork, but that's slightly more complex and I was kind of hoping for so to be good to get people's thoughts on that. I could go either way, to be honest, I do find it very useful to be able to tell the difference between unknown block and Snorting basic 

**Danny**
* Gotcha. Yeah, I saw that right. When I woke up this morning, but haven't had a chance to dig in. I'm happy to review but I don't have much to comment on before I take a deeper look.

**Adrian Sutton**
* Yeah, yeah. I don't expect I'll be much to say now, but it'll be good to get people's important thoughts on it, and it would be a song. I'm just trying to push it forward. It's been hanging around with the while.

**Danny**
* The conditional could be a soft work because we haven't actually ever had a voting period that votes for zeros.

**Adrian Sutton**
* Yes, we should double-check that, 

**Danny**
* Okay, well, please review, Adrian's, PR, and let's have some conversation there. Okay. Anything else today before we close? 

**Jacek Sieka**
* I'm sorry you mention, it's useful for? 

**Adrian Sutton**
* To debugging, So for instance, we Have always had a bug in the way we track ich one head and so which is the lightest block will consider. And you can't tell because if we don't have the last few blocks in a period, it just looks like the other node didn't know what they were talking about. So it's really useful to be able to have a metric that says hey we have this number of votes that we just don't recognize they look like invalid. And that probably should be zero normally versus we have this many default bug. You just can't distinguish them at the moment so you can't tell whether your node is. Is actually seeing the signing contract or whether there's just a lot of people out there with no Adventure 

**Danny**
* Is, those are the big deal is voting on the previous youth. One data does that give just as much information and there's a problem is people just don't follow that rule or is there a distinct value and voting 0 rather than just voting status quo? Oh, you said so too many people voting status quo at the beginning can lead to entrenchment of status quo, such that it is.

**Adrian Sutton**
* Yeah, so it's so with the way the spec is currently the status quo is considered a valid. So if the first block in the voting period, doesn't have any fun chain everyone, winds up. Following that and votes for no change, which is kind of problem. We've seen a couple of cases, the other issue is that you lose visibility of it. Once you get a block actually has 50% of the votes because it then becomes the current state even in the middle of the period. And so then everyone is just waiting for that. Just fine, it's not a big deal but it just adds a little complication there. In terms of you can't rule out. You can't say, don't vote the default. But you also need to, that makes sense. Like at the start of the period, you need to say that, but the default but once it's got 50% of Oats you should keep voting for the default, right? 

**Danny**
* Just one single vote for status quo at the beginning of the period And I need to go. Look at the logic here. Does that end? Does all honest votes after that, would that be to vote the status quo, or is that just something lazy? That's happening.

**Adrian Sutton**
* I'm not that should be what the spec says to be the honest votes would follow that because it's now the majority vote and it is a valid candidate. So you follow Is it a valid candidate? 

**Danny**
* Because it's within that the period. The period. That's yes, I think so. But if the period was restricted by half or something that it would no longer be a valid vote, unless there were no votes unless there were no blocks of. 

**Adrian Sutton**
* Oh yeah. I mean that, that probably is the simple thing of 

**Danny**
* Make sure status is no longer in voting period. I'm just thinking out loud. No. Oh, Colette logic.

**Adrian Sutton**
* Yeah. Yeah. I mean if there's a simple solution I'd be all for it. 

**Danny**
*  Yeah. Yeah. The fact that there's overlap makes it unclear if somebody is voting nothing or voting For status quo. But if there were no overlap that might that might help. Let's, I need to look at the logic. 

**Jacek Sieka**
* Alright, one more question then what if a majority votes for zero? I don't know, dear, I can respond to that.

**Adrian Sutton**
* That was what I realized when I was writing up with you this evening. So that's why there is a soft folk required to actually in the state transition. Ignore that case. So, you never set the econ data in state to 0, basically, And it's a, it's a very annoying complication that I was didn't. I didn't know about when I was thinking, this is the perfect solution and it's, it's not a perfect solution anymore. 

**Danny**
* That's why I think that's why, at least status quo was used as kind of the default there because it's not dangerous. If it because that just means no our bun on deposit pressing. But, Okay. 

**Adrian Sutton**
* I yeah I think I'd lean towards random as the other option, it would kind of be my second pick and it's very very much on par. And it's been working. So, I think the majority of clients actually do that. 

**Jacek Sieka**
* Now, I mean, you could do random with know if you bite zero if you really want to get down to it.

**Adrian Sutton**
* Yeah, or even the setting the deposit count is a very deliberately not be way to pick it around. I'm just doing a note block cache, as well. Anyway, I think I've no it's not enough  offline. 

**Danny**
* Thanks. And anything else for today? 

**Pooja(ECH)**
* I just want to share something last weekly recorded an episode on Adrian S on Teku’s Altair update work and in the past month we did a couple of more episodes on Altair's passion. Here is a playlist for Peep an EIP. These are good, like, introductory material for our Altair, for people who are trying to understand.

**Danny**
* Great. Thank you Pooja. I will drop that in the YouTube chat. Okay, anything else? Great. Thank you. We will coordinate over this coming week on that, Devnet and keep things moving. Thank you, everyone. Talk to you soon.

-------------------------------------------
## Attendees

* Danny
* Ansgar Dietrichs
* Adrian Sutton
* Ansgar Dietrichs  
* Mehdi Z
* Zahary Karadjov
* Adrian Manning
* terence(prysmaticlabs)
* Parithosh Jayanthi
* Pooja – ECH
* Dankrad Feist
* Jacek Sieka
* Leo (BSC)
* Trenton Van Epps
* Mamy R
* Micah Z
* Ben Edgingtom
* Protoambda
* Nishanth
* Lion dappLion
* Alex Stokes
* Hsiao-Wei-Wang
* Cayman Nava
* Carl Beekhuien
---------------------------------------

## Zoom Chat

From Lion dappLion to Everyone: 03:24 PM
Should we do a long non-finality experiment on Pyrmont after forking? Or setup a new devnet just for that

From danny to Everyone: 03:24 PM
yeah, I think it would make sense to leave half of our nodes/validators on for a while

From Lion dappLion to Everyone: 03:29 PM
Is any client testing non-finality in CI or has manually test it on an own devnet in the last 3-6 months?

From Adrian Sutton to Everyone: 03:30 PM
I split Yeerongpilly 50/50 accidentally for a few days a couple of times but that’s only small and it’s a relatively short period of time so not a great test. Was a very long reorg though.

From Lion dappLion to Everyone: 03:31 PM
Other clients have compared block processing + epoch transition times, phase0 vs altair. Same, faster or slower?

From Jacek Sieka to Everyone: 03:32 PM
There are new inefficient quadratic calls that need optimization

From parithosh to Everyone: 03:32 PM
https://github.com/ethereum/eth2.0-metrics

From Hsiao-Wei Wang to Everyone: 03:33 PM
Default to “zero” Eth1Data instead of current state PR: https://github.com/ethereum/eth2.0-specs/pull/2501

From Pooja |ECH to Everyone: 03:41 PM
https://www.youtube.com/playlist?list=PL4cwHXAawZxoEw29YmqJtNoFaENUUAREn

---------------------------------------
## Next Meeting
July 15th, 2021
