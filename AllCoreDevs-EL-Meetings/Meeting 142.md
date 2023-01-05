# Ethereum Core Devs Meeting #142
### Meeting Date/Time: July 8, 2022, 14:00 UTC
### Meeting Duration: 1 hour 45 mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/562)
### [Video of the meeting](https://youtu.be/K_Cjn74lMSY)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)

## Decisions/Action Items
|Item# | Description | Reference |
| ------------- | ----------- |----------- |
| 142.1| My suggestion is that we only do it on Sepolia to nudge people away from Ropsten. And it's a gentle nudge because, basically,  they can still use it. They might just get the worst period. And then, yes, we include that in the Gordy release. So, for people, they only need to download one release to get both the Sepolia merged block and the Gordy merge. - Peri | [26.15](https://youtu.be/K_Cjn74lMSY?t=1573) | |
| 142.1| Everyone seems to agree that in certain scenarios, allowing the option to return at all for the most recent, valid hash is a good idea. I believe we should be cautious about how it is specified and include a few hive tests to demonstrate the difference between lazy and correct behavior here.| [37.00](https://youtu.be/K_Cjn74lMSY?t=2237) | |

## Intro [11.30](https://youtu.be/K_Cjn74lMSY?t=698)

**Tim Beiko**
* Welcome to Allcoredev 142. A couple of things on the agenda today. First just going over a Gray Glacier Updates, which happened a few weeks ago already. then it kind of merged stuff around latest Sepolia Merge, Ropsten & Sepolia and MEV boost. 
* And, finally, I don't know if Henry is here, but we might have, a quick update on EIP 4444 and yeah, I think that'll get us through the hour and a half. I guess just to start, anyone want to give a quick recap on Gray Glacier Update and what we saw otherwise. 

## Gray Glacier Updates [12:00](https://youtu.be/K_Cjn74lMSY?t=719)
**Tim Beiko**
* I can just go for it. We saw the block times go back to 13 seconds. so you look at the black-eyed charts. It's just pretty clear to work, because this is, like an update that changes how the difficulty is calculated. You can see on the first block that all the times are in consensus. So like, there's no like weird potentially creeping issue, that can hit us. so it seems like everything went well. I don't know if anyone noticed any, any issues. 

**Martin Holst Swende**
* One thing I've really been paying very close attention, but I'm looking at the fourth one now and can see that there were 10 blocks mind on the old chain, the one that open a thermos arm, and the land. So the timestamp on the last of those is four days go as my exit. 

**Tim Beiko**
* I tried to reach out the exit pool. there were two, there were two entities that seem to be mining block on the old chain. One was like in a non, like a single address. So like not, like the, the extra data was like zero X. the other one was acceptable. I did some searches online for exit bull. It seems like a project that has like shut down or something. So I, it's not clear my impression after like spending 30, 40 minutes of searching on Google for it is it's like, it seems like a project that was doing a bunch of blockchain, things that shut down, then maybe someone somewhere forgot to turn off the mining breaks. so if anyone is listening and is in touch with exit pool, you still have some miners running on the, yeah, the pre Greg Glade. Great glacier. do you know Martin, if, are all the new blocks on the old chain still being mined by X a pool? Or is it still a mix of the two? 

**Martin Holst Swende**
* I do not know. I, I mean, I could just shake it out, but I don't have it at hand. 

**Tim Beiko**
* Yeah. And I also, I sent them both on chain message telling them, I'm not sure how much attention they're paying to their addresses. anything else? I think. Okay. So yeah, one, one of the, of the miners and the one who is not executable, since I've sent them an on chain message, they've mined the block on the, updated chain, which is, which is good. And then the second one, which I believe is X support, it seems like they've also mined some blocks on the, on the main chain. just, just today. Oh, I'm not sure that one is, it's a Bush. Anyways, two, two of the miners that were mining on the old chain have migrated, but yeah, it might be worth looking at the exit pool for some more, anything else? Okay. cool. So I guess, next up on the merge, we also had a forge, earlier this week after the polio, I know Perry, Danny, and a few people have been looking into it. does anyone want to give like a quick update about the Sepolia Merge? 


## Sepolia Merge updates [16.43](https://youtu.be/K_Cjn74lMSY?t=1003)
**Pari**
* Sure. I can go for that one. So Sepolia Merge yesterday day before yesterday, around, yeah, it doesn't matter. almost immediately after TTD was hit rather about two eBooks after, we noticed that a ton of participation was dropped and we were seeing a significant number miss of proposals. We chased that back down to conflict issues from a number of different validators on chain, and most of the conflict issues were patched relatively quickly. Once the conflict issues were patched, we did see proposals go back up the lake and at the station go back up to about 94, 95,  5%. the remaining 5% are missing keys. So we would never hit a hundred percent on this network until they leaked out. we did notice that there was an invalid, signature that was propagated through the network. We're still figuring out why that happened. but the network self healed as expected. And besides that, I think since then we did notice that there was, I guess the world state issue that was triggered on a couple of notes, but they already have a fixed for that. And I can link the PR and maybe someone from the besu team could talk about that. I think that's about all the issues that we saw in the network. in general, almost all of the issues were conflict related, which has paid news. but that also means that for future, for future, folks, we're going to have to work a lot more on communication. And we probably create like a diet of common pitfalls as well as maybe working on a BASIX clip that just validated if not a properly set up, if that I bought a used thrive, TTD is used to Tetra.


**Danny**
* I think that's Probably also worth just stating that the big issues resulted from us, essentially doing a strange UX is something that we've done on multiple proof of work test. That's where we essentially defensively set a very large TTD on the command line and then are supposed to remove that override or set that override to something lower. that is, you know, from my understanding that the cause of a lot of the issues here that is a strange UX, to set in an whereas on main net, it would likely be only reaction against some issue to set and not necessarily, and then not unset. so I think it's definitely a concern and there's like things to do better here and to communicate better about, but I wouldn't suspect we see this issue on mainnet. There's all sorts of things you can get wrong and how you can figure this up. Don't get me wrong, but I don't think you'd see this one. 

**Pari**
* Definitely. I also don't think we can see this issue on Cody because Cody also has a relatively predictable difficulty. So we'd likely not have to do an over that ongoing and possibly not. I mean  on mainnetthat as well, right? Yeah. 

**Danny**
* If the, if the, but if the ma if the override happened on main net, it would be not defensively. And then needing to unset, it it'd be to accelerate because hash rate was dropping. So the UX and like the experience of doing that would also not have the same type of error that could be happening here. 

**Tim**
* Got it. Anything else from? So aside from this config issue, basically, which, which was then, which was then fixed a couple lost keys, and the besu issue that we have a fixed board, there were no other client level issues that we saw. Is that, is that right? Yeah. I think those were all the issues at visa, and then we still need to dig into this a valild signature, but, yeah, that's not something that affects the overall health of the chain. oh, okay. And, yeah, Gary from besu had some mic issues, but he's saying that regarding this, this world state issue, the fix, there will be a fix for it, part of a besu piece that's out in a few hours. the besu version number is 22.44 to address that. And also just to follow up on that, I don't think that's a much related issue and also then show up around TTD, but rather, something to do with that database. And as far as I know, it was unrelated. 

**Justin Florentine**
* That's correct. Sorry, this is a, this is a rehash of the issue I spoke about last Allcoredevs.


## Ropsten & Sepolia mergeNetsplitBlocks updates [23:00](https://youtu.be/K_Cjn74lMSY?t=1380)
**Tim**
* Yeah, that's, that's really good. obviously like the configs, we do their job planning, but yeah, the fact that everything kind of went smoothly from the client side. This is really good news. anyone else have comments or on Sepolia? Okay. I guess Marius had some thing and he couldn't make the call, but, he wanted to talk about choosing, basically merge blocks for both  Ropsten & Sepolia, now that the merge has happened. I don't know if anyone else had had the context, on this. I know it was discussed at that third day of this week, as part of a testing meeting. 

**Lukasz**
* So the four blocks would be the first blog that is finalized. 

**Mikhail Kalinin**
* So, No, I, I guess now I'm because we want the 4k T to be correct. And we wanted to in the future, I mean this block, and also we would like to coordinate an upgrade. This is what I understand. 

**Lukasz**
* It's an engine needs a hard fork in order to have a fork ID in the future, the potential plants that do not okay. 

**Mikhail Kalinin**
* Exactly. I think it's just, just unpeel with the people who haven't much. 

**Tim**
* And are we, I guess, is there enough value to do that to before say Shanghai, or can we just wait the Shanghai and retroactively add like emergent Fort block there? 

**Lukasz**
* So I think it's a simplify hearing process. That's the biggest improvement, Right? 

**Tim**
* At the cost of like having another hard fork, basically. 

**Lukasz**
* Yes, yes. I think we can potentially do it after Gorly, after or after mainnet. I don't know about, we shouldn't like, take too much time with it Just testing. Okay. Yeah. Before my net. So it's okay. It can be considered as a part of a testing process for, for peering, right. It's small thing, but it's going to be considered as part of this. 

**Tim**
* And I guess the good thing is now that these, these networks run on proof of stake, when we plan a fork weekend and have like high certainty and when it happens, so what we could do is you could imagine having the release for the Gorly can pay, then you also, the merge of Ropsten & Sepolia fork blocks, and we can just like scatter them. So they, they have at each like a day apart or something like that. and because it's proof of stake, we, we have really high assurance that this happens, on that day. one thing I assume this, this would be an ELL only for, right. So it's like you still trigger it on a block number. 

**Danny**
* So you could trigger it on a block number and have pretty high assurance of when it's going to happen. Block numbers. Don't always come in every 12 seconds in the EL, But You could also trigger it on timestamp, which is, there's a debate there on future hard forks as to like how you do the coordination. I don't, I think block number is probably fine here. We don't have to get into the debate. I would, I would do Sepolia a first, well, I don't know. I would potentially do Sepolia first because it's like a very limited set of people running nodes. And so I think it'd be easy to see if it's working correctly, whereas Robson's, I think at least a bit more open. 

**Pari**
* Okay. We can also make the argument that technically Ropsten's deprecated. Now we only have to support supplier as well as, Gorld. So we don't have to go through the extra coordination effort for Ropsten. That's true, actually. Yeah, we don't need to. 

**Tim**
* Yeah. That's the aim is to just test that the heartfelt yeah, I think in that case, my suggestion would be we, we only do it on Sepolia, as a nudge for people to move away from Ropsten. And it's a very soft nudge because basically, basic plea, they, you know, they can still use it. They're just maybe get the worst period. and then yeah, we include that as part of the Gordy release. so just like for people, it's just like one release that they need to download for both this Sepolia merged block and the Gordy merge. Does that make sense to people. 
* Yeah, merge block and the Gordy merge. Does that make sense to people? Okay. No objection. As a support. I would personally prefer to do it on a block just because it, yeah, it seems like it requires no work from the cl teams to do that. And the, the, the, yeah, the uncertainty we get by, like miss slots seems quite low. so anyways, we can discuss this offline, but yeah, I think at a high level, we, we just do it for some Sepolia, combine it with the Gordy release and see how that goes. Anything else on that? Okay, Latest valid hash, McCale or POTUS do either of you want to walk us through the latest stuff in latest by the hash I'll share it that, that PR here, recommended for prefers in this change. 

## Make explicit that the child of LVH is INVALID [29.02](https://youtu.be/K_Cjn74lMSY?t=1736)

**Potuz**
* I was about writing in the chat. Please make how you do it. All right. So, I just put out a clarification, about latest by the Pash, in the spec. And it turned down into a discussion that it seemed that it wasn't really geared at clarification. So I just wanted to state something. I'm not sure if people would agree or not, but the way we're using the latest valid patch when we receive a new valid block is to prune our Hort choice, in the consensus layer style and to prune a apart, the purchase branch that is invalid, we need to know, which were all the invalid blocks. So currently, what we're requesting is that the latest value has mean two things. It's actually a valid block. It's an ancestor of the invalid block. And it's the last, Avery descendant from that valid block leading to the invalid payload is invalid. So that means that we can do two things. We can remove the by branch and declare valid, everything that is left out. Now we do understand that there's some clients that cannot comply with this. And so there's, there's, there's some caveat that we can, we can allow for a client to say, well, I just cannot give you this, but I can tell you that the last block is invalid, in some scenarios. Yeah. So that is correct. The correct. So there's some players that can tell us quickly, look, this block is invalid. I have no clue what the law, the latest value passion is. we're just asking. Okay. So give us know, but don't, don't give us the parents, because if you give us the parent, then we're going to make a wrong assumption about it. 

**Danny**
* Right? The worries is if you, if you give latest valid hash, it's just the parent you consensus layer now thinks the whole branch is valid, which is not, not the case. So it's best probably to make it clear that you don't know. 

**Martin**
* Can I just clarify? Yeah. Yeah. I'm just, I'm just, I just want to get it one more time. So the, the, what you want to avoid is that an EL for some reasons say the latest that hash is this invalid block. 

**Potuz**
* That's what The problem is that the EL might say this latest, valid hash is this thing that, is this thing that is the parent of the one that you gave me. And I don't know the validity status of this one. I haven't executed it. And this is a post Total cells. 

**Martin**
* I think that makes sense. Interesting. 

**Mikhail Kalinin**
* So, yeah, so I wanted to discuss a scenario. So for example, we are syncing, right. And we got a payload and we know that it's invalid because for example, I dunno, it's hash, does it doesn't work out or it's The header values are malformed. 

**Danny**
* Those are easy to assess. 

**Mikhail Kalinin**
* Yeah, Yeah. Or the base fee change in the way that it shouldn't compared to the parents, which we also, for example, gotten new pay load. And we have, and we know that this is wrong, but we cannot really say which one is less valid because we are still sinking. so there's no way of saying which one was less file. So this is like a problem for consensus execution layer. Yeah. So in this case, you should read your know, spare PR. 

**Danny**
* Yeah. I think that that's a reasonable scenario, reasonable fix. 

**Potuz**
* If you allow clients to do this, then there's the risk that, the ELL might be lazy and always return. And it's going to be like, So we can just add height desks for checking that. Right. 

**Lukazsz**
* So the other risk is that ELL is forced to sink an invalid branch. That's known as valid, which it might not be able to do because the network wants serve the data for it. And you have a dead look, Why? But let's say there are more invalid, ancestors in this chain. So all other clients will already like discarded those block and you won't be able to sync. 

**Mikhail**
* Yes. But I don't think it's like related to these exact. 

**Lukazsz**
* Yeah. It's kind of like, so the, the workaround would be, if you required us to give you license valid hash, that we, the only thing here we can, because we cannot give it to you. We can only say syncing, right. Then we need to try to get the latest hash. Right. That's the only way around it. if we cannot not give you the latest hash. And so, like I said, this might fail, because of it.

**Martin Holst**
* Right? Do you mean we bonded as sync? So there's no say that's not what I mean. 

**Lukazsz**
* Yes. For example, Yeah. 

**Danny**
* This brach is not available. cl should normally reward to the one that is available, just nobody will, what was for valid branch or for not available branch, You need to do the Knoll thing. 
* Cause otherwise there's a date availability problem on it. Even attempting to continue to sync the thing that you saw, this was invalid. Are you saying the date availability problem results in this chain from this change? 

**Lukazsz**
I'm not sure that was the question to me. So the problem is that we might get an invalid payload or that cannot be sent, so we cannot get Yeah. 

**Danny**
* Yeah. Okay. That was, thank you for clarifying. Yeah. 

**Justin Florentine**
* So, Well, I'm just worried about no being a little overloaded as all. It sounds like we're picking out a pretty specific use case where all the other fields that are in there, we know that they're invalid based on the state of the block and it's really the relationship to the parent. That's the problem because we're mid sync. Right. so you know, why not flag that as a specific scenario instead of just saying, okay. 

**Mikhail**
* No, I think, no, it makes sense here because it means, Well, it's the latest about hash? No, not that the whole response is no. 
* Yeah. We may argue about and code in it's in a different way, but I don't think it's like where it's to spend time here where it's better to spend time on the PR comments. 

**Tim**
* Okay, Andrew, yeah, 

**Andrew**
* I think, this change makes sense, but I would like to argue that that's, can we use days and now, or Neo not this special, like zero X value. That's my one that on the comment. 

**Danny**
* Yeah. Let's, I'm happy to take it to the, to the repo. I don't have a strong preference line coding. 

**Tim**
* Okay. And so it seems like everyone agrees that allowing the option to return at all for the latest, valid hash, In pretty pretty certain scenarios. 
* I think we need to be careful how it's specified and, make sure we have a few hive tests to kind of show the difference between lazy behavior and correct behavior here. 

**Andrew**
* Oh yeah. Sorry. And why like, but JSON has new, right. So like what what's, I mean, can we use just JSON new type? It's a minor thing, but why, like, I'm confused about this now in quotes, because it can be without quotes. 

**Danny**
* JSON knew, I think the one argument against that would be in the event that there were a few special scenarios. And you want to say that in, in named flags? otherwise, no, I think it's totally fine. 

**Tim**
* Yeah. So, regarding this, this PR can we then, assume that the latest value patch is valid? 

**Danny**
* If we get one, I mean, that's, that's the intention of the specification and I think as it should be, and we should make sure that the test scenarios cover that. I think if we clarify that and allow no in certain cases that I believe everyone can now confirm. 

**Tim**
* Okay. so aside, yeah. Aside from like Neal versus, does anyone else have concerns or about that? 

**Micah Zoltu**
* I do, but I posted them in the PR. 

**Tim**
* Thank you. and what is, I guess, is this something we can like get merged in the spec early next week? so that times can start working on, on the final, like implementations for it. So sometime next week, is that realistic? 

**Danny**
* Yeah, I think so. My unknown is how long to get a test in hive, but we can circle back on that on Monday with Mario and others, Right? 

**Tim**
* Yeah. Yeah. But yeah, but it feels like at Betty's we have this PR set and clients, the clients could start implementing, the actual behavior in parallel to, testing teams, writing tests and hive, and, you know, optimistically by end of next week, early the week after we have the behavior. Correct. And all the clients, 

**Martin**
* I think behavior wise or the code correctly, Jeff were announced the failure, the differences that we touring the column zero hash instead of, well, I don't Know. 

**Tim**
* No, unfortunately not Zero hashes for that purpose is when you have to, once, once you have to invalidate, starting from a transition block when it's something wrong with the terminal block or the transition block itself. So we use zero hash in this case. 

## Gordy [41.29](https://youtu.be/K_Cjn74lMSY?t=2488)
**Tim** 
* Okay. okay. I guess next up, I wanted to talk to you about Gordy and first, like just a quick, there was a quick question around Gordy about, from, in for a about, do active proof of authority. Signers need to do anything after the Gordy merged. the assumption was like as soon as Gordy has finalized, they, as soon as Gordy is finalized, they can basically shut down their co signers, but is there a reason why that's not the case? 

**Danny**
* So if they're, if they're running the actual merge software, so if they're running Geth or Aragon, that's merged, enabled and knows about the terminal block cash, they'll just stop producing blocks. if I understand correctly or their blocks, at least stop being gossiped, I think they'll stop producing though. and so they would just stop producing and they can turn them off. Can someone validate that if I were running a minor or clique signer against that it would stop. 

**Tim** 
* And then I guess if for whatever reason it did not stop automatically, once they have confirmation that like we finalized on the perfect state side, they can shut it down manually, but they shouldn't actually have to do that. 

**Danny**
* Right. And everyone else in the is going to be rejecting those blocks. Yeah. 

**Tim** 
* Yeah. But you can imagine there's a world where like, there's signer instances on separate feed from like other nodes that they may want to run. So like, it requires like they might basically don't need to upgrade those nodes and they could leave them on the old version up to the merge and, yeah, Right. 

**Danny**
* The network will reject them and they'll be sequestered in their own little zone and they can turn them off. 

**Tim** 
* Okay. That was my, my rough assumption, but I wanted to make sure that there wasn't a weird edge case. We, we weren't thinking about. I guess, so the second note around Gordy is, on the last couple of calls, we've talked about wanting to transition Gordy. When we have code, that's pretty much feature complete for mainnet so that it can be like a good, basically dress rehearsal for all the validators on main net and everybody else running a node. the people like, obviously there's like this change to, to the engine API we need to get in. aside from that, I'm curious from client teams, like, is that like the last day people feel that, they, they want to have in before moving to Gordy or are there other things that, are still missing that we'd like to finish before we, we started looking at merging Gordy and I'll just pick on random pine teams, I'll start with Aragon because I saw you all past the hive tests earlier this week. 

**Andrew** 
* Yeah. Thanks to Judah. We managed to fix them. 

**Tim** 
* Yeah. So is there anything on the Aragon side that you think still needs to be done again, except this like engine API changed before we moved to Gordy? 

**Andrew** 
* Well, I would like to test our sync performance, with, and especially I'd like to reiterate, I think it's, it's very important to enable checkpoint sync on the cl side and on the main net, it should be the default. Otherwise if you join as a new node and, without checkpoint soon, then it will be prohibitive as well. So yeah. More testing of same performance. 

**Giuiorebuffo** 
* Well, yeah, there isn't really much else. We then get out of bug reports lately. So I mean, the bands I'm not sure on is Okay. 

**Lukasz** 
* Another one, So I think we have still two bugs later on out to pass. might be good to actually think about scheduling the, at least one of them that will serve both, for fork ID change. yeah, so we are close, but I will, I would like to have a bit more time to finish everything. 

**Tim** 
* Besu, Yeah. 

**Justin** 
* We have one hive test left, to, to complete. So we're working towards that. We're pretty optimistic on it. We still have some concerns with our bonsai implementation and some Piering things, but nothing merged related. And so we're feeling pretty good. 

**Tim** 
* Nice. And next Geth, 

**Martin**
* So it depends on the wall. I guess the theme on this call, I've been creating through Europe for the last two weeks, so I don't really get comfortable given our status. 

**Tim** 
* No worries. yeah. Okay. I see it as like a there's I a present Teku who on the call? Nimbus like anyone else on the sales side. Yeah. 

**Terence**
* Yeah. So this is all related to, it's a execution layer, but I do think it's quite important to test, cause this is their client and B M E V Bruce, interaction, especially on a business set up, which is, this is kind of our last chance to use this before the main event. So I posted this as PR by Alex, essentially, he, he, he outlined this motion construction delay, and, I do think this is important that we merged this or we come, we come into some sort of agreement and then for them to try and code and basically tested. Yeah. 

**Tim** 
* Okay. So it would make sense. You have to test the MEV boost stuff on Gordy. yeah, so we've had to run out it before my nuts. any other cl teams have opinion they want to share? 

**Ben Edigington**
* I think we're good to go gree with Terrence. It would be good to test that transition, but other than that, all good. 

**Tim** 
* And anyone else I missed, sorry, folks on the call,

**Ethdreamer (Lighthouse)** 
* Lighthouse also wanted to test the transition, with, and maybe boost, but we had an issue. We were actually doing that during the last test, but we had an issue. but yeah, we planned to do Okay. 

**Tim** 
* Yeah, that's actually a good point. Are we running MEV boost on this shadow forks.

**Ethdreamer (Lighthouse)** 
* It's been fine, so far, but we just haven't run it during the, during the merge. 

**Perry**
* Sorry, Perry. You were going to say something as well. Yeah. we have shadow folk nine shadowed for next week. If the infrastructure's in case, then I can give you some keys and maybe we can test that next week. Yeah. I think that'd be really cool if we can do it. Yeah. 

**Danny**
* Yeah. I'd love to do it on a sub set, you know, a noticeable subset, like 10%, but not 50. 

**Tim** 
* Yeah. Okay. Yeah. That's that's that makes sense. So I guess, you know, there's still like some small about out of work that you want all the, on all the EL. and then on the sales, it seems like it's mostly just testing with MEV boosts. I guess we have this CL next week. We can see how things have gone since then. If, if we feel comfortable, picking a TTB for Gordy, then we can do it otherwise. if we need a bit more time, we can do two weeks from now, on, on this call, but it seems like we're, yeah, we're almost ready to pick something for Gordy. Does that generally make sense to people? I think this has no objections. Oh yeah. Alex. 

**Alex**
* Yeah. I are going to save since we're here. if any seal teams are listening, if you could take a look at the PR Terence mentioned 38 on the builder specs and just be prepared to discuss on the next sale call. That'd be good. 

**Tim** 
* Yep. Cool. and yeah, I'll add, like, I know I've been doing this for a while already, but yeah, just making sure that all the ELL teams have someone on the cl call next week as well. So if we make a decision for Gordy or if there's any issue with your clients, you can let us know. And worst case, if, if no one from like a CL can make the, or from an ELL team, sorry, can make the call, just leave a comment on the agenda. You have like a strong opinion or blocked or, cool. I guess, add next up, on the agenda. We have more on that. If I could just follow up on that,

**Pari** 
* Of course. in order to make communication a bit easier and give people more time to update notes, whenever we decide that Callie TTD should be also decided mainnet at the same time. And we can rather use Gordy as an abort as in, if we find something Gordy about them in that TTD and we change that or, otherwise we go ahead and we get the benefit of easier communication.

**Tim** 
* I think from a communication standpoint, it's actually more complicated. and I say this as the person who writes the blog posts for all these upgrades, that they're all, they're pretty complex. I think, I think one would simplify communication the most is if for Gordy that TTD is chosen, like the Realty EDS chosen, basically from the get-go and that's clients have a binary, which contains like everything, right? Like where there's no TTD override that has to be done. And there's no, like, you need to download the first version with the high TTD and a second version with the low TTV. I feel like if we can run through this process, and then also like do some stuff around like, the, the staking launch pad and like making sure that that's all up to date. so that it's like smooth for users. I think that's probably the best thing, like communities slash communication wise. and then shortly after that, you know, if it goes, well, we can pick the TTD for mainnet. and similarly, like, and I think for my net, we also want to pick it pretty close to when it actually happens. so if we weren't to pick them both at the same time and say, there's like, you know, two weeks before Gordy, and then two weeks before main net, you're like picking you up, you know, at least four weeks in the future. I feel like for main net, if we could pick it on the order of like three weeks or so in the future, that means that there's just a lesser chance that the hash rate changes a lot in that period. yeah. I feel like keeping them separate is better for like a community communications point of view, but maybe other people disagree. 

**Mikhail Kalinin**
* But what about glass bricks for the main net? we like, we could probably pick it, at the same time as like early, you know, 

**Tim** 
* I guess the question, yeah. The question for CLT is do you want to pick the main net, the logics, the pot before having seen MEV boost work on Gordy, which might be possible? 

**Danny**
* Well, there's also that would require also users to upgrade twice because TTD would not be baked into the cl clients. 
* Oh, right. They'll have super high D Which is not the end of the world. And that's not the same thing as them setting that manually on the CLI. So again, it's not the same like UX that might fail here, but it is two points of coordination. Instead of one, I would try to just do one if possible. 

**Tim** 
* Yeah. And I think, I think it's quite possible to do just one because basically if someone can double the hash rate on main net and like make this TTD hit twice as quick, they give them effectively 51% attacks, proof of work. which is like something we assume is, is not possible or probable today. so it seems like, yeah, if we, if we have a large enough gap between Bellatrix and TTD, you can combine it in one release's at the risk of just like hitting TTB maybe a bit later than you than you would if you thought if the hash rate starts dropping, but from a UX perspective, that does seem better. 

**Danny**
* That's my current preference. I think it would have fewer end-user errors. Yeah. 

**Pari**
* Yeah. Also makes MBO try the exact same thing on girly because the hash slash difficulties early as well, we can just have a ballot shakes happen maybe one week before TTD supposed to get off few days before. and then we can change just adjust that tolerance mainnet that yeah. Yeah. And I think on Gordy, it can be much closer, right. Like you could imagine doing like teeth, uh Bellatrix on like a Tuesday and then like Gordy on like an MTD on like a Thursday or something like an order of days. and then mainnet that you probably want like order of a couple of weeks.

**Pari**
* Yeah. I think we just have to be a bit aware, in communicating that, because that would also imply people don't have three weeks to update their note or they don't have up until TTD, but yeah. Which is actually easier to communicate because we know when Bellatrix is there's like a timestamp for Bellatrix. Yeah, definitely. Yeah. 

**Micah Zoltu**
* So while I can appreciate the UX improvement of having a single release, that includes both Bellatrix and the TTB. what makes me uncomfortable as a precedent, the sets where we're designing, switching from designing systems that are resilient against basically, you know, state sized attackers to systems that we hope work as long as no one big shows up to play. And well, I generally agree with the sentiment that is unlikely. I, I really dislike. The scenario. And now we're saying, eh, it's, it's an unlikely scenario and not an unlikely in like the cryptographic sense of finding a hash collision, like which, you know, we just put a bet, I'm fixing to address a potential hash collision with contracts and EOS. And now we're saying, you know, like that the order chances of that happening are like, you know, if someone has all the Bitcoin hash power for a year, they can do that and we fixed it. And now we're saying, well, if someone has 50% of youth hash power, they can break or Birch. And just like this direction makes me very uncomfortable. I, I agree. 

**Danny**
* It's very unlikely, but it just seems like the wrong path to whatever It's also, but contextually, this is a singular event and we're making an assumption about the adversary during a singular event and not a perpetual adversary, which I think is certainly a different, threat model than, an adversary and perpetuity in the long long-term. So I am more comfortable making an assumption that the hash rate cannot double in the next three weeks, as opposed to making an assumption that such an adversary would never exist, which I think is the difference in this scenario. I understand, I hear your argument. 

**Micah Zoltu**
* I agree. There, there is a very valid point. That's having a persistent defending against a potential future adversary versus a defendant against an adversary. It's going to show up in the next few weeks is certainly different. I'm a little bit worried that there's a, it's a very blurry line between those, and then I'll think on it. Maybe I can be convinced that there's actually a bright line there. but it just feels like this is it's, it's feels like one of the first times we're making this call where we're saying, we know there's necessary out there. That is very realistic. Like someone, you know, some government could have this much hash power. This is not out of the realm of possibility. This is very much within the realm of there potentially actors out there who could do this, and we're just kind of ignoring it. And this is the first time we're doing that. I think. And that's, that's where I'm uncomfortable with this, where we're crossing a line that we have not previously crossed and I'm uncomfortable crossing new lines without thinking really hard about, you know, is this a line that we're okay with crossing again and again, and again and again in the future? 

**Tim**
* I think, I think that's, that's reasonable, I think. yeah. And, and, you know, there's like two, you know, 2 alternatives. One is like, yeah, you just have two releases. And like we did for Ropsten, you can pre-warn users that there will be a second release. Right. So, so like from a community and UX standpoint, it's less worse to have to download two releases. If when you download the first one, they tell you, you need to them download the second one. I think the second one is like, if you want to absolutely have one release, then you can play with like the delay between like, between Bellatrix and, and, and hitting TTD, because you could imagine in the worst case, it's like that delay could be even longer than it would be with two releases. but yeah, I think, yeah, you definitely have like a valid point there and it's something we should, we should think through. 

**Micah Zoltu**
* Yeah. And to be clear, my argument here is almost entirely philosophical. Like we can set the difference, the time difference between the two so large that it's not judging a 51%, you need like, you know, 99% kind of thing. and so we, we can make that number very big. And we do have control of that by separating those two times a lot. Again, my argument here is primarily philosophical because I feel like we're crossing a line that we've not crossed before. And I want to make sure that we're very intentionally crossing that line. We understand that precedents are strong and people will look back at this and say, you know, oh, we did it before. It's okay. Now, like, I don't want to make normalize this. And you know, if we're going to across this bright line, we should set up a new line that is very clear that we don't cross in the future. 

**Tim**
* Yeah. I think, I think that's, that's a very reasonable stance. anyone else have thoughts on that? 

**Danny**
* Yeah, If we went the other route, I just want us to be extremely careful and explicit and simply maximally simply so on how the UX for users goes because it's order of magnitude more complicated. 

**Tim**
* Yeah. And I think it, there it's like saying from the very first release, like you will need to download the second release, and also probably making, making it easy to verify when you've downloaded the second release that your current TTD is actually correct. 

**Danny**
* Yeah, I guess I'm most worried. Well, I'm worried about a lot of things, but I'm worried somebody then updates the execution layer and doesn't update their consensus layer and their consensus, or it doesn't know about new TTD and, and things like that. Just those types of scenarios. 

**Micah Zoltu**
* Yeah. No, don't, we have a check between the MCL that if they're out of sync with the TTD, they'll talk to each other and notice and do something. 

**Danny**
* They said they should have an error that goes to the loss, But they'll continue running. 

**Marek**
* We are not doing anything with this. 

**Tim**
* So maybe, in the next like week or two, Danny and me can just like scope out the pros and cons of the two options and, yeah. Showed up on like the next cl call or ideally before. But, at least then Sounds good. 

**Danny**
* Yeah. I want to think through the, where the UX can fail to decide that how bad it's worth one way or the other,

**Tim**
* And then similarity. yeah, what's like the failure, like what's the attack scenario and you know how different it is than our current life. It'd be current things we're willing to tolerate basically. and I feel also that like whatever we end up using for mainnet, we should probably be used for Gordy. So that's takers have the opportunity to run through the entire process, once on, as it will be on mainnet. yup. Anything else on this? Okay. then we have, Leo from, the flash spots team to give an update on MEV boosts. 

## mev-boost updates [1.04.49](https://youtu.be/K_Cjn74lMSY?t=3889)

**Elopio**
* Yeah, I am here, and I mean a new place, so let's see how this goes. I have a bunch of things to say, so I made the agenda on the PM issue. I will go through them and then at the end, we can focus on the things that you find interesting. most of these things are linked to repositories around. So for the things that we don't discuss, there are, places to continue the discussion. 
* Interesting. and I'm planning to attend these meetings, all the time from now on. So the updates will be shorter. And if you have questions that you want to bring here, we will be around transfer them. so, well, yeah, I'm well for the ones that I haven't met and I'm coordinating things for, from flashbacks around the merge. so I will be responsible for, the things that we will be shipping. And I wanted to start with where we are. 
* So whether we have a believer is a permissionless protocol, for validators participate in MEV extraction and a lot of people participating on the specification for this.
* So thanks to all of those, this is big. This is a super big change because in proof of work, we have the allowed list of minors and that's a severe limitation.
* That's something that we wanted to avoid. That was the first internship where they're already, we have a stable relate that can connect to multiple builders that also enables another avenue of experimentation on decentralization. We have a blog peel there, that's optimized for MEV extraction. And then, the validators don't have to, focus optimized for this. 
* They can connect to the, relate to the builder and participate on the network immediately. and we have two consensus clients ready for testing and the others in progress. so this week, on our Cigniti, we were like overwhelmed by all the things that we have in the backlog and all the ideas that come. and then we step back a little and we checked on this and this is huge. we were calling this milestone merged, ready, because these were the basic things that we wanted to have, for the merge and we are already here. 
* So yeah, sometimes we just like lose the context. there's still a lot of things to do, but I would like us to step back and celebrate because so many people were involved in this. I took a look at all the work that went into the consensus clients implementing this, and it's a lot of commits, a lot of work, a lot of trials. so thank you everybody. and well, now we spend the weekend celebrating, what comes next. since we have these two, consensus clients ready, we want to publish the code for testing and start moving our communications around this to get more people, to execute the stints, provide feedback, to everything on the step. we spent the week, shaking a few issues that were there, making a list of things that are expected to be weird on the logs, reporting them.
* But I think it's now good enough for people to just give it a try. So we have got testing guides, in the Wiki. The Wiki is open. The corporate testing is in a pull request. so if you want to take a look, change some things, we are welcome, of course, that's, what's immediately next, like now in an hour or so, we will be making this public, while we were planning for the next month, goes around three areas. First is post adoption, make sure that people are using the post, a way to mitigate MEB and, super relevant.
* Make sure that the big validators that are sticking pose that, that's changes are following this protocol and not trying to solve this on their own way of Paik way. that's everybody's like openly participating on this MEV mitigation and may be spreading. so unimportant thing that we will start working on now is data transparency. Now that we have the relay in the builder working, we can start collecting numbers from what's going on there and making those numbers public public. And the idea here is also to not play this role of mediators. Like currently when, when searchers held that miners are cheating, they come to us and we do the investigation, and then we are in charge of punishing the minor somehow, or this is very uncomfortable, not, the situation that we want. so in data transparency, we will enable people to identify when somebody is deviating, exploiting a hole when something is not working as we designed it. And then everybody together can figure out a solution, not, using flash bots as the mediator in there. and we, we'll be restructuring our community around this to, the idea being that, this shouldn't be a community of searchers and miners. It has been now, this is actually in my mind, the community of researchers. so all the roles that we're playing, all the data that we're collecting, all the experiments that we're running, ultimately are for, or decentralization for other handling of MEP. 
* And we will be working on trying to, to design the workflows on everything that goes through our, our projects to be supporting that. so that's like what I will be coordinating these three months and we will be trying to do that on, in the open, welcoming everybody to participate. so that's so short term called protesting long term, like this restructuring of transparency and, community of researchers. but then on the process itself, the plan of what to do next, we currently have one relay and one builder. we want multiple builders in here. and we have this issue open to see who's interested in running a builder. and here we are careful, like we are not super sure that the builders can be permissionless, that anybody can be a builder. but the, the, specification, the protocol enables us to experiment a lot. 
* So we want to see how to approach this issue, playing with one more build there, that's independent thing with T-Mobile builders that are independent seeing what limitations we find in there. And we are writing a post that should come out next week about what are the possible conflicts in here, where the incentives break. If an organization plays a couple of roles in here, like what happens if the searcher is a builder? What happens if the validator is a builder? what happens if there really is a builder? and this is fast forward skates in this moment slash runs the relay and the builder. And it works only because it's trusted, right? we want to, to come up with a lot of ideas of what are the possible scenarios and what are the risks. 
* And then the system should be designed in a way that it incentivizes, independent parties to be running the, the roles that could be potentially in conflict. a lot to Deakin there, that I think will be the work in the next three months about who are the partners, who are the competition, who are the bursaries? How do we put all this energy into something that gets us a decentralized protocol? and, there are many, many questions to get there. So, if the merge is happening on September, like being realistic with the resources we have, whether we can achieve is a really monitor, not like permissionless builders, not like permissionless release, but some tool that will w daters will be able to connect you to, get some reputation, measure their risk when they are communicating to, to a relay. 
* Yeah, but then you see, this is like, what was overwhelming, then the monitor is centralized and we have to decentralize it. And it's wow. So many things, but we're getting there. we need a lot of ideas from this. So, on this issue for the agenda, I also put a leading to the open questions. These are like the big things that we're researching, that are, are defining how do we move the protocol forward? they take positive there. any thoughts, any ideas will be super interesting to hear, and yeah, it'd be, an interesting on decentralizing. This that's three together that's, contributes to answer those questions and then, multiple it's multiple builders without this, this mediation, but, in the issues. 
* Sorry, I just, there's a couple people that have their hands up, so I just want to make sure we can get to them. 

**Tim**
* Yeah. I don't know if do you want to quickly just wrap up, sorry. I'm just wanting to make sure we could get the, yeah, Yeah. 

**Elopio**
* I'm almost done. Just mentioning that on the issue. There are other things that are not like popping research questions, but popping practical things. some are more complicated than others. Let's take a look on the meeting last week, we talked about, sale options or open options, and that might require changes by the consensus clients. 
* So those kinds of things, we need to discuss them early to give time to all the consensus clients, to agree and implement or take, an alternative. yeah. And just to close, a question for you. Like, I want us to test my posts on Gordy, like be ready for the Gordy in the merge. but I wanted to hear your opinion. and a crazy idea came out of all this brainstorming intense work, that is my post and proof of work. And that sounds like super punk, super interesting. That could give us a lot of testing that we need, like making sure that the systems we have will be ready for the merge. but we kind of discarded it because we cannot do both. this would require work on calves and would require like some, communications with the miners. but I just wanted to throw the idea because it was fascinating for me. I got super motivated just with this possibility. it would shake things around, maybe somebody would get interested in wanting to take it, push it forward, contribute something there, or it's just a crazy idea that we will not implement because we are doing a lot of things already. yeah. And that's solely, I wanted to mention, yes. I think we have time for many questions, so that will be here. 

**Tim**
* Awesome. Yeah. Yeah. Thanks for, for the extensive update. 

**Micah Zoltu**
* Because I think your first, When you said you only have one builder, what do you mean by that? You mean there's only one person who has come forward to saying I'm going to build a block builder, or do you mean there's only one person participating in testnet? 

**Elopio**
* No, I mean that there's the flash spots builder, and the plush what's really is currently communicating to the flashcards spill there, on this issue, where we are asking people to come forward and declare their interest. There are already like three, four people interested or such for our network. We know there are more people interested in running a builder. yes, we want, we want everybody who's interested on this to, to participate openly say and contribute Is that, 

**Micah Zoltu**
* So if I understand correctly, then you're just saying that currently flash bots, the relay is permissioned and you only have one person that has permission to at the moment, is that correct? 

**Elopio**
* Yeah, that was, that was the merge ready, milestone. And now we will add more builders. 

**Ethdreamer**
* It's Hey, so in our testing of any of the boosts so far, we have this mock relay that Sean Anderson built that just like it hits the execution engine. So we don't actually have any D but we can at least touch the code pass through the consensus layer, and lighthouse. But, is it possible for you guys to build a main net relay so that we can like use, have actual MEV on the shadow forks? 

**Elopio**
* Yes, it's possible. why don't we take this shadow fork that will come next week. That's our way to see what's required. this, this lack of MEV to test is while we will be tackling now with the community and testing work streams, like, yeah, we are, we are sending, we are asking the relate for blocks and the relay is talking to the builder for blocks. And the builder is talking to the maintenance to the, to the, to the main pool for transactions. And then we are testing all the pieces, but we're not testing the central. And so we need searchers to be involved in the testing and we need sources of order flow. so the next step on this work stream is talk to our top searchers, to talk to uniswap all the main sources for, for MEV extraction and start sending some, some, significant, significant tip, transactions into this testnets. So we, the idea of doing a capture, the map, incentivize testing situation. So I dunno, we highlight the smarter MEV extraction and, this gives a reward to the searcher that did w date for that participated. this requires some coordination, but if we want to be saved by the merge, I think we need like more realistic, usage on these networks we'll be working on. 

**Terence**
* Yeah. So, thanks for the summary deal. I just had two high-level points, I think, long. I think one of the points that if we do think within the merge in like September, October, it's quite important to come into a date where we say that we are going to freeze the API spec, meaning that there's going to be no more changes to the builder and then the do their API so that we can also co freeze or into. So, yeah, just, just a point on that. The second point I have is that, we have a blogger where we sent a hundred registrations that it times out, so that is blocking us from testing on Robsten and also, but we can also take that offline. So, yeah. Thank you. 

**Elopio**
* Yeah, so, like materials increase our working on the resilience of these relate and builder. right. So we, we are starting to hit it hard now with some of these testnets and that tells us what do we need to do to, to make it responsive? I know they, they, yeah, so these problems, and I know they are working on them. I cannot comment a lot more, so I will let you talk to them. there were some strategies to, to reduce the load and to increase the capacity of the machines. and this, this is super good, experimentation to figure out what are the requirements for a relay a builder to be absolutely stable. your other point about the API? Like, yes, in my mind, the API was pressed after Amsterdam, frozen after Amsterdam, but unexpected things come. So if it worked for me, I would just phrase it now. all the things that will appear will be dealt post-merger as, as, as our plan was calling this merge ready. but that means some limitations like this open or closed, auction we will have to deal with whatever is possible now. So, I don't know, maybe insist more on taking a look at what spoke pain, what we want to happen for the merge, and come to the agreement that all the other things will not be possible because we will print the API. Then we focus on testing on resilience on this, on adoption, on measuring the numbers. and if nothing crazy happens then, okay, we're good to go for the merge. if something deadly appears on the testing, okay. We will have to think again. What does that mean? Do we have time to iterate once more on the API? will that affect the merge or not? yeah. So this is actually up to you. If it worked for me, we, we close this and, we start playing with all the other topics, but we will not make changes until the merge happens. Any other questions? 
* Alright, thanks a lot for the time. I insist. Thanks a lot for the amazing work. So many hands going on in here. So step back, celebrate, because what comes next is going to be intense again. I'm super happy with being part of this. 

**Ethdreamer**
* I guess there is something I want to bring up. I think we were thinking that it might be best to, disable, MEV during the merge until finalization. it's, I mean, it's just, it's a preference, but I thought it might be something you might want to discuss just to eliminate the things that are going on during the merge. 

**Danny**
* I believe there's a PR up for this and that it's on the agenda for the call in one week, the consensus layer. And I've not heard any, anyone against it yet. 

**Elopio**
* Yeah. We will follow whatever your preference is. we can, not answer on the relay until we should answer. So that's another safeguard. I think that's why I want to test in Gordly. we can prepare for that. We can see how that goes. We can see what are the risks by not, extracting MEV on the first blocks. How much do we want to wait? but yeah, sounds okay. 

**Micah Zoltu**
* I can give you a sneak peek of a potential argument for next week's call. 
* And that is that MEV extraction is still likely to happen. It's just going to move somewhere else. And that somewhere else may be engineered more poorly than MEV boosters. And so we're just moving people out of the light thing that's engineered and tested by people we trust over to things that are engineered by people. We don't, I think clear that is an obvious one. 

**Tim**
* Well, the, the witness there's less interaction with the, with the clients software. So it's like, you're willing to take more on chain and obviously off chain craziness. yeah. At the cost of just her, I guess her the benefit of just having less stuff,

**Danny**
* That's sort of 20% of validators decided to use some crazy system and they go offline that's that's probably okay. 

**Micah Zoltu**
* But yeah, We can talk about it. 

**Danny**
* We'll we'll we'll slot some good time to, Yeah. 

**Elopio**
* Like my purpose is to, to go live from the block. I understand the position of like, there are so many things going on the first block. but yeah, like, are we opening, like by not mitigating this upfront, are we opening the door for other crazy things to happen? we will follow you. Yeah. Happy to. 

**Ethdreamer**
* That's just a command, the command line override defaulting to disabling until after finalization. But if you want to pass dash dash enable dash that's dangerous. That's fast. Don't do this then fine Right there. 

**Elopio**
* One more thing I wanted to mention. So we have all these open questions and people are coming like wanting to implement the relays. And this is like fascinating. But when we talked to them, we realized that they don't understand MEV and they don't understand the risks or the responsibilities or the condition of like going raw, bro, if you're really becomes used. so my idea would be to insist on this people who want to run a relate to first run a builder, then get an idea of what's happening, get practice, get our support while, getting there, their build they're strong. And then, yeah, we cannot control who runs the builder and which validators go to which builders. but at least we would like them to be important. So if you know, or you want to participate on this, running a builder, running a relay, please talk to us, go to the issue, tell us, and we will be purchased part you, then also like to hold you accountable for like what will happen and ask for your collaboration and answering these questions. 

**Tim**
* Cool. Anything else around that? okay. If not, we were going to have a 44 update, today, but unfortunately Henry could, make it, there was an issue, that was in the agenda. and, I know that, Alex and lightclients, you have like a bit of context on there. I didn't know if there's anything quickie you want to share. 

**Lightclient**
* Otherwise we can just move all of this to the, to the next call I get, I can just say quickly that Henry is still working on his implementation that can import and export this data, this circle data out of gaps. And shortly he plans to take this format that we've sort of discussed in a few channels and put it into an EIP. So that'll probably happen before the next All core devs. So beyond the lookout that I'm sure we'll post it on one of the discord channels, Any questions? 

**Tim**
* Comments that's what that, okay. and then if not, there's just two quick announcements. The first is this is the last All core dev's calls on the Friday. So we re done the last call to move them to Thursdays. So the next Allcoredevs is Thursday, July 21st, if not Friday, the 22nd. so yeah, please, update your calendars. We've updated the protocol, called calendar as well. but yeah, last all core, on a Friday today, and then a final, quick announcement, next Friday we, have another merge community call. so for, application developers, infrastructure providers, and whatnot, to have questions about the merge, this is the place to come and chat about it. if, client teams want to send a couple of people to show up, it's always useful to answer much more into we'd, in, in, in the questions. yeah, so the link for that as well as a deep, agenda for allcoredevs date. and yeah, I think that's it. Anything else anyone wanted to chat about before we wrap up.

**Greg**
* Wasn't 4444 on the agenda? 

**Tim**
* Yeah, we just, that's what I like, kind of it's just covered. So, Henry was supposed to get a full update, but he's not there, but Oh, okay. Yeah. Yeah. I just, the last link in the comments is, is like the longer, I guess. 

**Greg**
* Okay. I looked at that. It, all we said is we're going to talk about it later. 

**Tim**
* Yeah, Yeah. And Henry should. Okay. Yeah. And there should be just like a proper EIP for like this specification. 

**Greg**
* Yeah. I've already studied this, so thanks. 

**Tim**
* Okay. Well, yeah. Thanks everyone. And we'll see you, in Thursday on two weeks from now. Thanks. Bye. Thanks, bye. 


------------------------------------------
## Attendees
* Tim Beiko
* Łukasz Rozmej
* Tomasz Stanczak
* Bordel
* Greg Colvin
* Vadim Arasev
* jgold
* Marek Moraczyński
* Protolambda
* Trenton Van Epps
* Andrew Ashikhmin
* Mikhail Kalinin
* danny
* Ben Edgington
* Pooja Ranjan
* terence(prysmaticlabs)
* Justin Florentine
* Daniel Lehrner
* Gary Schulte
* Justin Drake
* Matt Nelson
* Ansgar Dietrichs
* stokes
* Adrian Sutton
* Qi Zhou
* Marcin Sobczak
* Sean Anderson
* Karim T.
* Viktor Shepelin
* Fabio Di Fabio
* Jamie Lokier
* Vitalik
* Sam Wilson
* Tom
* Henri DF
* Helen George
* Thomas Jay Rush
* Micah Zoltu
* Marcus Wentz
* SasaWebUp

---------------------------------------
## Next Meeting
July 21, 2022, 14:00 UTC https://github.com/ethereum/pm/issues/572

## Zoom Chat 
00:01:43	Potuz:	not allowed to unmute myself so hello :)  
00:02:23	Zuerlein:	gm  
00:02:29	Tim Beiko:	gm!  
00:02:57	Zuerlein:	another week, another LVH discussion  
00:03:06	Tim Beiko:	the real merge was LVH  
00:07:49	Tim Beiko:	https://twitter.com/harshad_fad/status/1545346202472181761  
00:08:25	Tim Beiko:	https://twitter.com/mysticryuujin/status/1545234043213697024  
00:09:00	Gary Schulte:	lol  
00:09:55	Tim Beiko:	https://twitter.com/parithosh_j/status/1545296824893833216  
00:10:06	Gary Schulte:	lol  
00:10:24	Tim Beiko:	https://github.com/ethereum/pm/issues/562  
00:11:11	Ansgar Dietrichs:	being in a time zone where acd is at 4pm is the best, because then you look at the clock and it's 1559 and you know it is Ethereum time  
00:11:24	Mikhail Kalinin:	lol  
00:11:24	Justin Florentine:	brilliant  
00:11:32	lightclient:	haha i miss that  
00:11:32	Pooja Ranjan:	:)  
00:11:33	danny:	is anyone talking?  
00:11:37	lightclient:	no  
00:11:39	danny:	cool  
00:11:46	Potuz:	:) had the same doubt  
00:11:52	Mikhail Kalinin:	let's keep this ACD chat only  
00:12:01	lightclient:	xD  
00:12:10	Ansgar Dietrichs:	we can just have acd in the youtube comments  
00:12:21	stokes:	it would get drowned  
00:12:22	Mikhail Kalinin:	that’s the next level  
00:12:38	Justin Florentine:	<maximizes chat window>  
00:13:23	danny:	we’re going to do CL calls weekly to try to catch up on the call number  
00:16:50	Tomasz Stańczak:	you will be overtaken by shadowforks number anyway  
00:19:14	Zuerlein:	^  
00:20:16	Mikhail Kalinin:	an invalid one, was it a block signature?  
00:20:58	Tim Beiko:	Can confirm ExaPool is now mining on mainnet  
00:21:03	Tim Beiko:	https://etherscan.io/block/15093120  
00:21:10	Tim Beiko:	more recent than their last block on the old chain  
00:22:42	Gary Schulte:	my mic is not working: but regarding the besu sepolia worldstate issue, there will be a release in a few hours which has the fix.  22.4.4  
00:27:40	Micah Zoltu:	Timestamp!  
00:27:46	Micah Zoltu:	Boo.  
00:27:53	Mikhail Kalinin:	pls do not fall into this debate  
00:28:06	Micah Zoltu:	/me restrains me.  Fails.  
00:28:07	danny:	lolll  
00:28:29	danny:	I’m a timestamp maxi but for this and in the context of still in merge dev, block height works  
00:28:39	danny:	known quantity wrt dev  
00:28:43	danny:	and configs  
00:28:48	danny:	for EL  
00:29:16	Micah Zoltu:	That argument is way too nuanced for you to be considered a maxi.  
00:29:29	Micah Zoltu:	You are hereby cast out of the timestamp-maxi cult.  
00:29:30	danny:	post-mainnet-merge timestamp maxi  
00:30:00	Micah Zoltu:	You'll have to create your own new Discord server.  Won't be having none of that in Timestamp Based Hard Fork Maxis.  
00:30:19	danny:	we can merge after the merge  
00:30:25	Tim Beiko:	https://github.com/ethereum/execution-apis/pull/254  
00:30:26	Micah Zoltu:	🤔  
00:30:28	Zuerlein:	this is what i've been waiting for  
00:31:30	Mikhail Kalinin:	Illustration to LVH clarifications, are in the comment to the PR: https://github.com/ethereum/execution-apis/pull/254#issuecomment-1178797073  
00:31:51	danny:	in some scenarios*  
00:34:08	danny:	it’s when you have quick validity checks that don’t need full state/execution  
00:36:27	Justin Florentine:	would an explicit flag value instead of null be helpful?  
00:37:18	danny:	I agree  
00:37:26	Potuz:	Teku expressed preference for null. I'd say that whatever works best for the EE would be best  
00:37:26	Justin Florentine:	seems like null is overloaded  
00:38:10	Marek Moraczyński:	I would prefer null tbh  
00:38:20	danny:	I”m fine either way on  how to encode. will defer to others  
00:40:34	Andrew Ashikhmin:	json nil please  
00:42:18	Mario Vega:	I'll start working on the test changes  
00:43:28	Łukasz Rozmej:	So what is the final decision? Here? If we can't do LVH, we return 0x?  
00:43:49	stokes:	null (but also move discussion to PR)  
00:49:43	terence(prysmaticlabs):	https://github.com/ethereum/builder-specs/pull/38  
00:51:00	stokes:	it may be high overhead but we could try some kind of shadowfork /devnet situation a few times ahead of goerli  
00:51:01	Mikhail Kalinin:	We use “null” here in the spec: “{status: INVALID_BLOCK_HASH, latestValidHash: null}”. How is this encoded in JSON?  
00:51:08	stokes:	(to test mev-boost)  
00:51:24	stokes:	@mikhail as null  
00:51:39	elopio:	let's do it!  
00:51:43	Mikhail Kalinin:	I would suggest we used the same encoding of “null" for the LVH case we have just discussed  
00:52:51	Marek Moraczyński:	I agree with Mikhail - let's use the same encoding :)  
00:52:57	Mikhail Kalinin:	@stokes like { “latestValidHash”: null } ?  
00:53:11	stokes:	yes  
00:53:19	Mikhail Kalinin:	👍  
00:53:19	stokes:	if we are just talking about how to write "null" in json  
00:56:52	terence(prysmaticlabs):	+1.. one if possible : )  
00:59:16	Tomasz Stańczak:	+1  
01:01:15	Gary Schulte:	unlike the eoa collision, the merge is time boxed  
01:01:30	pari:	Is the argument that its the last oportunity to 51% attack ethereum? Because if someone had that hashrate, they could attack ethereum today for the same benefit  
01:01:49	danny:	right, they can create a liveness failure with acceleration to TTD  
01:01:53	danny:	or they could 51% attack  
01:02:16	danny:	both would cause us to immediately act, and us something like TBH to abort pow immediately  
01:03:43	danny:	or half an order of magnitude. if those exist  
01:04:13	stokes:	they should error in that situation  
01:04:23	pari:	^IF people see the logs  
01:04:27	stokes:	i hope they do!  
01:04:27	pari:	its a big IF  
01:04:40	stokes:	clients can always just fall over then  
01:05:05	pari:	I'd actually vote for clients crashing on exchange tx request failures. But i've no idea if its too late to make that call.  
01:05:14	Micah Zoltu:	I like failing to startup if EL/CL are out of sync.  That is the time the user is most likely paying attention.  
01:05:29	pari:	Exactly, a crashing client draws more attention oposed to a log error  
01:05:39	stokes:	but i do think its valid to ask if we are too far along  
01:05:45	stokes:	bc i think we are quite close if not already  
01:06:09	pari:	Yup, I don't think its worth the delay. We can expliticly tell people to check logs + create shell scripts to validate this exact issue.  
01:08:57	Mikhail Kalinin:	I can see how users don't upgrade EL, but starting their CL and doesn't pay any attention to it get crashed. Because EL is working and giving them all they need pre-Merge  
01:11:39	pari:	^ that is one of the issues we faced in sepolia. one of the config issues was missed because everything was working fine pre-merge. Whereas the exchange transition call was silently failing in the logs.  
01:12:49	stokes:	as in no one was watching the logs? or it was not being logged at all?  
01:12:55	stokes:	(just trying to understand the UX failure)  
01:13:16	pari:	No one checked the logs  
01:13:18	Marek Moraczyński:	no one was watching the logs  
01:13:39	danny:	what are logs?  
01:13:53	Mikhail Kalinin:	lol  
01:14:13	stokes:	🪵  
01:26:01	terence(prysmaticlabs):	we’ll need https://github.com/ethereum/builder-specs/pull/38 first : )  
01:29:03	danny:	lol  
01:29:08	danny:	gas price auctions!  
01:29:27	stokes:	but this is a black box wrt the merge  
01:29:36	stokes:	we are assuming the mempool will still work  
01:30:49	stokes:	keep the code surface small!  
01:30:49	danny:	—make-more-money  
01:30:59	Micah Zoltu:	😆  
01:31:40	Micah Zoltu:	I want to run a relay (so I can exploit bundle flow).  
01:32:32	Tim Beiko:	https://github.com/henridf/eip44s-proto/issues/1  
01:33:05	danny:	I have to step out early. thanks everyone!  
01:33:12	terence(prysmaticlabs):	See ya  
01:34:02	elopio:	non-meeting Friday! I appreciate this <3  
01:34:15	Greg:	4444?  

