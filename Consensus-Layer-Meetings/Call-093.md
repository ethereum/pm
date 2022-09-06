# Consensus Layer Call 93

### Meeting Date/Time: Thursday 2022/8/11 at 14:00 UTC
### Meeting Duration: 1.5 hour  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/594) 
### [Audio/Video of the meeting](https://youtu.be/CIAGQMUKEZ4) 
### Moderator: Danny Ryan
### Notes: Alen (Santhosh)


---


## Intro [6.20](https://youtu.be/CIAGQMUKEZ4?t=396)
**Danny**
* Hello, welcome Consensus Layer call 93, Issue five, nine, four on the PM. Repo. And yes, now we have a six by six grid. This is very aesthetically pleasing. okay. So today we are going to go over merge related items, including* the recent quarterly merge, a number of, minor discussion points. And, there are some documents circulating for may not Bellatrix POC, N T D D, which we had pre-committed last week to talk about this week. So we will do that. and then a couple of issues related to MEV boosts, maybe also a general update. and then there are some discussion points for 4844 that came out of, a recent community call. If we don't get to it, we will certainly get to it at the next call. we we'll see how time plays. Okay, let us get started. 

## Merge

**Danny**
* We had m*erge, it happened approximately 12 hours ago. The network currently looks healthy, although there was much in the interim, Perry, would you give us the high level and then maybe we can go, as you're, as you're giving the high *level, if there are additional points on any of the points from a particular client team, please client team jump in at that point. So we can discuss those points. just so we can kind of all get on the same page and understand how to move forward. Peri. 

**Parithosh Jayathi**
* Yeah, heavy one. so like any said, we had a much on the belly network about 12 hours ago. one of the things that was peculiar about the much this time was that we had two terminal blocks. So essentially one block that was produced with the difficulty of one and another one with a difficulty of two and some amount of chaos is that related to that? essentially we did have some, so we were looking at about 90% participation before the March, and then we dropped to roughly 70% and for a couple of eBooks below seven, below the required 66%. 
* So I think we didn't finalize for four or five epochs. essentially a couple of notes had gone into their own forks or were offline for another reason. I elaborated those under, in the, in the issue tracker, LinkedIn chat. yeah, besides that, one of the biggest things that helped with participation over the last 12 hours is that there were, a couple of numbers nodes, as well as Lodestar nodes that had wrong conflicts either they were an updated, executionally or nodes, or they were, they weren't configured with the required JWT token. 
* Once that was fixed, we noticed participation rate increase up to the present 81 to 84%. That means if we were to remove conflict issues, it would have potentially been a 90% to 84% drop, which is actually not that bad at all. yeah. And besides that we have, two or three client issues that we've noticed. So the first one being in another mind issue shortly post TTD, and that had to do with Netherlands processing of pre-emergent post budge blocks differently. 
* Essentially they, they had a bug where if there were multiple terminal blocks, it was hard to hard to fix. The fix was known. We had the fixed deployed on a couple of notes as, as a test and I think it will be included in the next release. And one thing we noted was that we already do have a test for this on hive tests. So if the hive tests are all passing, then we wouldn't have noticed this bug. we had an arrogance tall before itself healed and essentially Aragon had built a, transition block on top of a site for, and once it got stuck on that sidewalk and once 1 28 slots were done, it kicked into optimistic sync and fix itself. We had a, issue with a rocket pool note using an invalid block and the node was, lighthouse Aragon, if I'm not wrong. And we're still investigating that one, but potentially updating to the latest development fixes that I'd let the client team talk more about that. And there was an issue with, basil incorrectly invalidate, incorrectly applying to the canonical chain to take her. but I would let the, the team elaborate on that one as well. if you look at the issue tracker, there's also a status for most of the issues that we've mentioned and yeah, I guess that would be updated over the span of the next day. Yeah, I think that's about it for me. 

**Danny**
* Thank you. And, the Nimbus and Lodestar nodes are online as well are online. Now, those are the Nimbus team and Lodestar team nodes. 

**Parithosh Jayathi**
* Yes. The numbers team and Lord Stanley not online. And we knew it wasn't necessarily a client in compatibility because the EDF was also running those clan combinations and we didn't notice any issues on on us. 

**Danny**
* Got it. Okay. are there other, would any client team like to go deeper into some of the issues that they solve? you know, the steps that are taking, being taken to resolve them, if there's additional tests that need to be *brought in here? just any other comments? 

**Andrew Ashikhmin**
* Yeah. I'd like her to talk about the issues in Aragon. So, we did have a bug, the, in our previous version, we as their transaction and indexing, but, I'm still not sure what happened with rocket pool because, the person, the operator says that he actually uses our latest version and we saw in the log that transaction made it into our transaction pool. So still not sure what exactly happened there and, whether the, this, bad in better blog was due to that bug or something else. So still investigating. And I would also, I'd like to ask about this, 110, 28 block maybe Micah or somebody could explain, Ruthie to me what, what, why this needs to wait 128 spots. 

**Mikhail Kalinin**
* Shortly, this is like the protection from the folk choice poisoning that cannot cure if you're, trying to import the block with a parent that that is not available. Like, yeah, the, the merchant position block built on top of, a parent that is not available or just random degenerated parent hash. In this case, it will, the sync in responsible, never resolved and cl will just cl switch to such a block. It will get stuck there. And if like, if like a lot of cl nodes and where their nose get stuck and sync, and they will not be able to do them well, there is you just build the honest chain. This is why we weighed in for 188 blocks before optimistically switching to, to these, block this, if this should give enough time or on this chain to progress. 

**Danny**
* And Yeah, and no, these are for actual unavailable chains. I think the Aragon issue is that it was not executing, the, these side chains that were available. and if the side chains that are available during the are executed, then this issue is, would not happen. it's primarily to avoid the case of someone's for choice being poisoned for it, with unavailable box, if the blocks are available and they are executed, then this doesn't happen. So I believe that there was a PR up in Aragon to do this partially, but if it had any sort of, parent depth into the PR work chain, it was not actually, executing and was returning either accepted or syncing and thus getting into this deadlock state for 128 blocks. 

**Andrew Ashikhmin**
* Okay. I need to take a look at how is this, take a, look more into the larger curve around their terminal pow block. 

**Danny**
* That's right. I guess it's, it's after the merge transition, if you don't execute side chains immediately and just return, except that even if they're available, that can be handled in is fine. It's worth the additional load during that transition to actually execute these, to not enter into this status. 

**Andrew Ashikhmin**
* Right. I see. 

**Mikhail Kalinin**
* Yeah. And this is only for the transition block wants it's important. this timeout is not applicable anymore. 

**Marek Moraczynski**
* I want to rise one more thing because we, not, this it on our internal node undermined TECO, and we started discussing it with other. And the issue is that we are returning that we are in sync, us Nethermind, but, our logic *is, that we are downloading the history. we are trying to reach the hat and we are returning that we know we are in sync, but we are still downloading a history of the chain. So all the blocks of receipts. And, it seems like teku, is, shut down because of that. and, and we are wondering with other and what we can do, because the solution could be to change if syncing logic or, or adjust cl client. 

**Danny**
* That's a question for Adrian from Teku. 

**Marius**
* Yeah. So, what's what's the, what's the issue? What, what, why is this breaking stuff? Is it because teku is asking some old blocks because they say, okay, you're, 

**Marek Moraczynski**
* Yes, I'm, I'm wondering you are returning syncing, or only if you have all history or, or how, how is this working okay. 

**Paul Hauner**
*Than Paul With lighthouse we were tracking using is syncing on the L's to try and, help us understand when the ELL is syncing, but we just found that, it wasn't reliable enough for us. We found that there's a few clunky occasions where guests will tell us that it's, like he is, or isn't thinking, I can't remember what it was. So we just decided to, to give up on it. And we don't, we don't track that anymore. 

**Marius**
* Yeah. The issue is we, we returned on not syncing if we didn't stop a sync yet, I think, and that's like some, some corner case kind of really rely on, on this. So I think the more correct way to say is if you don't have all the history and the state, then you ask them and you shouldn't return sync. 

**Lukasz**
* Yeah. So that's a very good question about the semantics, because what we are doing is, if the thinking is a question as if we have the hat, we can, we can process the next block. So we return syncing through when we don't *yet cut up the hat when we have some head that we can rely on. And we, we know that the network is in further, then we return syncing holes while we still, I can download ancient blocks innovation. So that's the current, Nethermind. Potentially we might want to change that based on this discussion. 

**Andrian Sutton**
* So who needs this historic blocks for other historic receipts for, for the, for the deposit contract, but Yeah, in this, this particular issue that we're hitting is slightly different to adjust the deposit receipts. 
* I suspect the next thing we'd hit is that we'd be searching what grinders for log events. And I think get adjacent RPC era back if Nethermind doesn't have blocks for the range we asked for. so I think we can handle that, and we'll just kind of re keep retrying that, but that the code that's causing problems is our search for the minimum Genesis block, the first block that meets the conditions. it's probably not, but it's required now that we have mainnet Genesis so we can pull it out. it's just really complex and we haven't disabled the ability to run and actually calculate Genesis from the execution layer yet. 

**Andrian Sutton**
* Yeah. Beacon changed Genesis. And it's, it's the first block that could have triggered that if there were enough deposits, which on my net, I think was the block that triggered it. Yeah, part of it, I think, is that a while back, like way back, we actually added code to handle, I think probably nevermind that didn't have all the blocks back to Genesis. And so as we were kind of doing a binary search to find this block, we'd get blocks that just didn't exist in history. And so we assume, well, it must be after that because you didn't bother syncing those old blocks. but when you are still in the process of syncing, that's now leading us astray, because they're trying to find a block that's weighted recent. and then it's filing the check when we try and confirm it really was the right block. So there's a few tweaks we can do. It sounds like it's only affecting TECO as well. So all the clients by the skipped that logic or,  at a slightly different way, or for whatever reason, we will be able to work around it. but it is probably, oh, no, it'll be all right. If the request for deposit logs are rejected, we then fall back to a different node anyway, or that post merge doesn't matter as much. Anyway, it's a really interesting case because saying you're in sync and we take you so users that we kind of expect that you've, you've got that history. and I suspect there'll be some other surprises in different cases from people getting black history in that case. 

**Danny**
* Yeah. I do think the semantics here are much more about, I have the state with respect to the head and can process blocks built upon it. and that extending the assumption beyond that probably dangerous because everyone can have all sorts of different like historic nodes and stuff, and, or even pruning, obviously there's not a lot of like most blocks are kept. but even 4444 could like change the pruning depth and stuff like that. So like the assumptions there shouldn't, shouldn't be about the depth should only be about the head, I think. 

**Andrian Sutton**
* Yeah. I think there needs to be some indication there though that, you know, how far back do you have, because we're kind of changing some of these semantics now. 

**Danny**
* It's Yeah, but I would, I don't know if I'd couple, these heads semantics with depth semantics, you know, we're using the Eth APIs are much more reliable with respect to that. there might be rules about how deep you should have. but I don't think that like syncing versus valid in the head should in the engine API should dictate those steps to as logic premises. 

**Andrian Sutton**
* Yeah. So the problem, I think then we're getting is just that where we're asking for block, and we can't tell, I don't have this yet versus I'm never going to get this. That's a way of handling it as in, we're never going to get, this is that's what it used to be. So the syncing is kind of, it would patch over it if you were still saying syncing. Cause we would just treat the node as offline, but we might be the other option here might be that if you are intending to download a book, but don't have it yet, JSON RPC  instead of empty, then I know how you're just node ready for that. That would also fix technical, but I suspect we'll change. Take it as a result of this. it's just, I can certainly imagine a bunch of other applications. I mean, surprises. Yeah. Someone like in bureau would see the notice thinking they wouldn't go and check all the old blocks. So there's gotta be some indication to say, actually this node is not ready for this yet. otherwise it kind of gets thrown into the JSON RPC. Our people are people and does all kinds of weird things. 

**Danny**
* Right. And I agree with that. I just, I think the conflating of the engine API semantics is not going to give us what we want here. do we have enough information to move forward and can move on to the next issue? Any other points on this one? 

**Mikhail Kalinin**
* Yeah. Just wanted to point out that it's very important for, from cl perspective, when ELL, validates and processes, the emergency transition block. If the terminal block is, has been received previously by the cl. So all data that are required to execute this block are available. otherwise if it's returned and syncing or accepted the, cl roles stall for 128 blocks also, there was like, from what I understand, there was a bug in the test that checks this particular scenario, and we are going to fix it. And this is what is important to be fixed, in the EL clients, before the mainnet merge, if it's not already implemented as expected. 

**Lukasz Rozmej**
* So they will like to ask other, engine, clients to how they are implementing the CTH syncing in terms of that, can be offline, sorry, neither, but I'm really interested if we should change it or not. 

**Andrew Ashikhmin**
* In Aragon we say that too, like if we have anything missing, we reply with a syncing. We like, we don't download anything in the background. If we do that, I was syncing, 

**Lukasz Rozmej**
* Yeah, because you don't have the states in, right. You'd have to have all the blogs books. That's fairly obvious for your, for your, syncing methods. 

**Fabio Di Fabio**
* What sort of Besu, the laws, everything before in the backward sync before say that sync. 

**Marius**
* And also because the history is a way easier to sync then state, at the moment, you should already have these three when you've been finished. 

**Lukasz Rozmej**
* I will, No, I would've snapped thing can take like three hours while double the old receipts can take a long time. 

**Marek Moraczynski**
* Okay. We should work on all the snips and Yeah, we are always a syncing state faster than all history. 

**Lukasz Rozmej**
* So It's way faster. Maybe we should work on our recent sync. 

**Danny**
* Okay. I think we should move on to the next, discussion points. And if there's additional discussion here, let's take it the discord. Okay. other discussion points from Perry's summary that. 

## Goerli merge [29.12](https://youtu.be/CIAGQMUKEZ4?t=1759)

**Danny**
* Other discussion points from Perry's summary that client teams would like to go into, you know, discussing an issue that, that arose that is going to be patched. maybe some additional tests, factors that should be put in *anything else on the Goerli discussion. 

**Paul hauner**
* I just wanted to say that I had a good dig through, full choice just before we finalized, the merge transition. there were a few faults floating around, I found nothing, none of them to be particularly interesting. so yeah, I didn't didn't really find anything to be concerned about regarding consensus layer fork choice. Just look like a kind of, bit of an unhappy network trying to sort itself out. And it did. 

**Marius**
* So one thing I saw was that some of our notes, lost a lot of peers. like most of them states didn't lose any or stayed mostly the same. And then a couple of node that went off probably went up on the wrong. I think it was nethermind from the nations. they almost lost all of their peers. I think, I think it was on the, on the consensus layer. So maybe the peer scoring it's a bit, yes. 

**Danny**
* Peri some of the, nethermind was restarted, so they had to repair. I'm just gonna, Perry said that I'm saying that out loud. 

**Dankrad Feist**
* Nethermind execution had a problem, right? 

**Marek Morcazynski**
* Yeah, Yeah. Which we've discussed, but, if the Myers of the, the node restarts was actually in line with also the peer drops, be good to know. 

**Marius**
* I think at least from the time that I looked at it, it was more a gradual decline. 

**Paithosh Jayanthi**
* Yeah. I'm just looking at the grass now. I think they went from 50 PS to about 30. And then, 

**Marius**
* So when I looked at it, it was more like 50 to like five and that's why I was like, I'm not really concerned, but I think that this scoring might not really Know it's, it's good to know. 

**Danny**
* And that, I mean, if the peer scoring is aggressive, that could also account why some of these forks were three, four blocks instead of just one and quickly resolved if there's like kind of, transient network partitioning going on there. let's like on the consensus side, can investigate that a bit. Okay. Other Goerli items, 

## tbh update [32.46](https://youtu.be/CIAGQMUKEZ4?t=1966)

**Mikhail Kalinin**
* Yeah. does any ELL clients team wants to share their progress on the terminal block, hash overrides segmentation? 

**Andrew Ashikhmin**
* Yeah, we still don't have it. it's, we, we only have the, the overwrite on the networking layer. but, that will make us only peer with peers that have this specific block. And so we should, I'm not, I'm not 100% sure how it was like, if we specified this, then you are guaranteed. 

**Danny**
* Right. I had, I mean, at this point, I think having a credible path to do this in an emergency is more important than having it top-down fully implemented. that's my, my take Andrew, you had a comment. 

**Andrew Ashikhmin**
* We haven't implemented it either. 

**Marek Morcazynski**
* For us it's still, NPR because, we want to focus on, today's tissue and, if syncing, probably, we will review it later a bit because it could potentially introduce some regressions. So we need to be careful with managing 

**Danny**
* I, back to my previous comment, I might not even merge it. I might have it there, proof of concept and ready to use, you know, in an emergency, not effecting the code base at this point. Okay. Thanks for the update. Mikhail. Anything else on that one? 

**Mikhail Kalinin**
* Oh, thanks everyone. And agree with Danny comments, the placeholder TTD in engine API. 

## spec-ing placeholder ttd in engine API [35.03](https://youtu.be/CIAGQMUKEZ4?t=2103)

**Paul Hauner**
* Yeah. So, when, when the T day is not specified yet, we still want the EL, CL to be able to exchange transition config, and do that successfully just so that users can set up that stuff before the merge and see that it takes work. that is a standard for this on the consensus layer about the value that we use when not as defined, it's a very high value. it doesn't seem to be anything on the ELL side. It seems that I think Geth returns and on, and I've seen Nethermind for 10 zero. My proposal is that we take the standard that already applies to CLS and also apply to ELs. So basically, yells you copy and paste is very large number from, my PR and then we're in your code base. And if you don't know what the TTD is, then you just return this high number. yeah, I think it should be fairly easy to implement. I think we've already got a bit of buy-in from people, just wanting to raise it and see if there's any objections. 

**Danny**
* So there's a bit of a race at this point, Paul, depending on the next discussion point, as to whether there will even be client releases between now and when we have a TTD, does that affect your desire to get this merge? 

**Paul Hauner**
* Yeah. So it might be that we figure out the main intensity before this, before, you know, before people get around to implanting this, I would, I don't know, I'd be tempted to just implement this. it's not a big deal if you don't, but it's kind of helpful because you know, there's other people running other tests that Salesforce like gnosis and stuff that haven't decided this yet. And it just makes life a little bit easier. but yeah, no, no, one's going to die. I don't think it's going to happen if, if you don't have the mindset fit, if you can stay the cycles, I would, I would try to do it just food cleanliness to show sanity. 

**Marius**
*I think we already, I already implemented something that showed it's much or not, Right because of the agreement. 

**Danny**
* Last time we brought this up was it wasn't necessarily going to be spec, but people were going to do it. I know that if something's not specked, it's less likely to be done. but let's, I could go either way on the spec, but, if people get this out, that would be great other comments. Okay. If this issue is relevant to you and you care, please go to the, engine API, API is PR that was linked and comment. if we're going to do this, probably makes sense to complete it by maybe end of the day tomorrow. So if you feel strongly when my other please chime in. 

## Mainnet Bellatrix epoch and TTD [38.50](https://youtu.be/CIAGQMUKEZ4?t=2331)

**Danny**
* Okay. on the last All core dev call, we had discussed picking a main net Bellatrix you pocket today and a tentative TTD today to then potentially be overwritten next week in the event that, we see a precipitous drop due to the five gigabyte threshold on minors on the dag size, and to do client releases shortly after. can we trying to hear, yeah, Tim, why don't you give an update on dag size? just so that we can understand the timing there. 

**Tim**
* Yeah. So, I don't have like a perfect other setting of this, but I think it's good enough for our purposes, as I understand it when the, when, we say the dag exceeds five gigs next week, it's actually the dag plus the size of the block hash, that exceeds it. so it's, it's, it's right under five gigs. And then, which means that if you sort of block hash elsewhere, you can keep using, you know, those, those miners. And you can, you can kind of fix that through a firmware update. even when the dag exceeds five gigs, it seems like there's at least some ways where people can use, 5g cards, and like probate probabilistically, get like a, a valid badge if the only query kind of the subset that they have in grandma. and the more I dig the, this, the more, it seems like there's a, a long tail of strategies of increasing complexity that you can do if you want to maintain that hardware. which leads me to think that, like the odds we see an extremely high drop, right, when this hits are low, historically we haven't seen kind of really big drops when we've had a trash holds. We've seen some drops, but, you know, they they're like on the order of noise and hash rates. so I think, you know, we, it's fine that the biggest TTD and we can permit next week. but I, and it's probably safe to like, you know, wait until we hit that and see, you know, due to like, what share of the hash rate did the network who just run like the middle of firmware and do no optimizations or present, is there a fall off there? But I suspect like after that, you know, there's an increasingly complex amount of tricks you can do to keep maintaining that hardware. And so, different actors, will be able to do that. yeah, so I, I guess all this to say is like, we should probably wait to just to be like extra safe, or at least probably reconfirm next week, just to be extra safe. but I don't think like even if next week is when we hit it, or when we, when the dag actually exceeds five gigs at excluding the block hash, we'll see like a massive drop. 

**Danny**
* Thank you, Tim. So potential information in about a week, but actually unclear food. See like a discreet drop, if depending on how people are programming their hardware and how the hardware is actually constructed. Good to know, in such a timeline, we would be aiming to on probably Tuesday, the latest, not this coming Tuesday, but the following to do, a blog post with client releases, thus client releases would need to go out Thursday, Friday, Saturday, Sunday, or Monday. quick turnaround helps us make sure that we kind of keep the timeline rolling and some of these more exotic attacks around, accelerating TDD, and we've kind of have our eye on and kind of can keep things tight. Tim, do you, should we go over the Bellatrix doc and the, quarterly, I'm sorry, in the, in the TD doc, or do we want to have other types of discussions around strategy first? 

**Tim**
* I guess, you know, I build the ELL and cl side, like, are people comfortable with that timeline? Right. Like that's probably the main thing then we can, it's like, yeah. Is, are people comfortable with those timelines? And if so, we can look at, you know, a specific key ephoc in TTD and base them off that, but it's yeah. 

**Terence**
* I just want to confirm, so we're looking at the week of August 22nd, is that right? 

**Tim**
* Correct. 

**Terence**
* Yeah. So, so, this is prism, so I spoke to the team and majority of them no issue, really seen before August 22nd. Yeah. And that's from our side,

**Danny**
* Terrence, you do sound like a robot, but we could understand you. Thank you. Yes. 

**Tim**
* Yeah, I guess, yeah. Curious to hear from other teams as well. I guess maybe if people don't think this is possible, this is kind of the time to step up. 

**Andrew Ashikhmin**
* Yeah. I think for Aragon, we would like more time because, we kind of, we still need some work to do around to terminal pow blogs, potentially optimize, unwind three wines, especially with, I think it's the case where the tech Kobach maybe with other CLS as well. So from my point of view, I would like more time. 

**Danny**
* So I think one strategy in getting more time is to actually do the releases then, but to also set the expectation that there might be ELL strongly suggested ELL update releases after Bellatrix, in which we'd have a followup blog post, and kind of thus emails are feature complete and ready to go. if I didn't, if you don't have your grade, your notes probably fine. But in the event that, there are Charlotte suggested releases you to do kind of another wave rather to Bellatrix to say, Hey, these are the releases that client teams recommend. I think that allows us to have a little bit more flexibility in play in getting final releases out, but also at the same time, it gets us positioned, in the coming week and a half on score. 

**Ansgar Dietrichs**
* Yeah, it was just on that front. I was just wondering, my understanding would be that from eNett basically the minimum time between having your releases out and being confident that everyone upgraded to something like two, two and a half weeks or something. So wouldn't that mean that we basically have to have this minimum two weeks, two and a half week period after Bellatrix. Before we do as much? 

**Danny**
* No. What I'm suggesting is that client releases come out in that plus one half a week from now and there may not ready. You know, they work, they work as they did on, Goerli today, if not better. but in the event that there are additional releases, we would do a wave after Bellatrix to say, Hey, these are the recommended releases upgrade. If you can, thus, you don't necessarily have lead this sufficiently time for everyone to upgrade, but if people do want to patch with the hardened releases, they can map. 

**Ansgar Dietrichs**
* Okay, that's reasonable. 

**Matt Nelson**
* Yeah, no, I think the act is cool with that timeline, especially given that we could, again, put out another release. My question is when do we anticipate the, I know Mikhail mentioned some bugs with high pets community anticipate those sometimes too, just to make sure that if we have extra time to like double check and button, everything up before the releases on the 22nd would be ideal. But if we need to push some of that back, I'm presuming that the tech, we understand the bugs and the test, and they'll be updated pretty shortly 

**Danny**
* Mario or Mikhail, what's the status here, 

**Mikhail**
* From my understanding is, should be like an easy fix, but it's better to ask Mario about it. 

**Danny**
* Do you mean the, the gossip testing or The recent wave of the tests? I believe that found a few bugs in corner cases. 

**Mario Vega**
* Oh yes. There were some on Nethermind. But, I think they were already working on it. The new release for this, this is very much so, there's not a substantial increase for all the, the other clients. I think one test for geth. And that's it, I think, but there, there was no not obsession 

**Danny**
* And these are merged and in public hive and teams presumably have seen them in are working on them. 

**Mario Vega**
* Yeah, yeah, yeah. It's it was more just today actually. So the day they lead us run should reflect the current status. 

**Mikhail**
* So the test has been fixed right. And already, if it was even buggy, that was my impression, Which specific Test when there is the terminal block, from, from a site work and, client response, seeing can, Some Issue with this test and other mind past it, but, it didn't work on the Gordy. 

**Mario Vega**
* Yeah, definitely. That, that once it's fixed, I think that was that specific since the last release, so that shouldn't be working, even now without the latest update.

**Danny**
* Thank you, Maria Lucas. 

**Lukasz**
* So, I think we are passing most of those new tests. I think I have two right now finding that my pipeline, bought apart about those general pasts in, in the, this transition test. So I, I gave them Mario feedback. That would be good that the block and hives tests that we are using for, for those tests would have some unique stage changes each one of them, because this is what we have issue with that, on the hive that all the blocks have same state routes, but it will be good for all the block to have unique state through some hive tests. Like, you know, all the tests probably. 

**Mario Vega**
* Yes, Definitely. Definitely. We need, I need to pick, some of the, the test cases to include marginal sections in the most, in just the mesh marshmallow. So we can have a different state route and yeah, but that, yeah, that's a, that's, that's a work in progress. 

**Danny**
* Okay. other input on these suggested timelines on the suggested release strategy. 

**Nishant**
* Oh, what's the expected date for Bellatrix, That's what we would get into now. 

**Danny**
* Actually, Adrian, can you Adrian and I believe Tim was a couple of additional estimates this morning. Can y'all talk us through and share the document? 

**Adrian**
* Yeah, let me just get the document shed. so there's a few options. I shared a document I can share my screen if that's helpful, or if you wanna share yours. Yep. Just trying to move things on to the right screen so I can not *have it all to be Eight screens over there. Yeah. That's the only way to monitor to find it. Right. So, this is working on the basis of essentially what we just talked about, that these dates become in range. with the idea that we'd have releases out set around August 19th, we tweaking what kind of sounds like we want to have that weekend stage as well. So it probably looking at the lighter range for these dates. first September would be just less than two weeks away from the thing. Now it gets to more like week and a half. so I'd say we're kind of looking at the Monday Tuesday type timeframe. I think the first thing to set is, are we happy with these kinds of dates? Like we can pick specific numbers easily and we can make them pretty, and I can show you the spot picker and that kind of thing. But, I'd be thinking either Monday, fifth or sixth about activating Bellatrix based on these conversations. 

**Danny**
* I believe someone commented on the fifth that that is a national holiday in the U S and that even, corporations might be off. So pushing into the sixth, I think does make sense, as for consensus layer teams, just in some conversations over the past day that I believe that there's no objection to moving forward on that. but please correct me if I'm wrong. Yeah. Agreed 14500. It's really easy to eyeball that you got that right. Instead of like having a copy paste error or something, 

**Adrian**
* And if we're going to probably a good one, it is very late. It's 10:00 PM. It's not 4:00 AM, right. That's that's probably 11 or 12. Oh yeah. I did fudge that one. 

**Arnetheduck**
* A little, Any of these airports on a, what is it? 8192 slot boundaries such that we get, such that when we get an even multiple for the block roads table to be fresh for the merge, those two are not, if somebody wants to find one, they can, I think, let's see, Sorry, what's the benefit of that? Well, we have these, block routes and state routes and he's above all historical state historical roots tables, lists in the beacon state and they rotate every 8192 blocks. 

**DAnny**
* So, Then you can have like the rule set, be the same for all bachelor it. the next one I think is 1, 4, 7, 4, 5, 6, which I think is moderately substantially later. 

**Tim**
* If, so The one before that would be one for it, she wish. So I do think it is either too early or we delay by another couple of days just to hit that, which would basically be two days, right. Or, more like five days. Cause like between 1, 4, 3 and 1, 4, 5, you get about five days. and so between 1, 4, 5, and 1, 4 7, you'll get another five days. which seems, Yeah. 

**Arnetheduck**
* Ah, that sounds strange. It's 27 hours per Oh, slots. 

**Danny**
* Sorry. I was doing, I did POC math, which is wrong. someone, someone could, yeah, it's easy. It's easy to bump. I, my apologies on that, let's redo that. 

**Tim**
* So is there is a further for the beak and chain is a multiple of that better than a knee. 

**Danny**
* I, you know, I would, I think I would rather keep with that for the potential use cases there for the cleanliness there, then keeping around slot. I could be convinced otherwise, but I, I don't see a reason not to have my apologies on getting that math totally wrong, but let's run a quick couple of numbers on that, I guess, which, I'm Sorry, please go ahead. 

**Arnetheduck**
* So it's 256 epcho that we need to be around two. 

**Tim**
* Okay. So we can, we can figure out which of these inbox we like the most and then find the closest, multiple from the there, right? 

**Arnetheduck**
* Yeah, exactly. And it's actually quite convenient when they line up. I mean, it's kind of like a clean slate where, we get this unique number for the state that corresponds to the Purely one rule side of the other. Yeah. And not only that, but it actually ends up in all historical beacon states for, for, for the future because of the historical roots things. So we'll get like that particular hash will be in the beacon state forever. 

**Mikhail**
* Does it make that much sense? given that the TTD is unpredictable and we will not be able to, So the it's the Bellatrix rule set. 

**Danny**
* Right. But then you have a transition during the Bellatrix  tool set, but it's, it's the same code whether TTD has been hit or not, there's just conditionals on the code, whether you're doing X or Y. So I, I see what you're saying, but I think that from like a consensus layer perspective, that's when the upgrade happened and that's when you're running the new logic, even though the TTD isn't happening yet. 

**Paul**
* Yeah. I would be, cautious of fulfilling that 8 1 9 2 rule, though, if it's going to land the update at some really awkward time for a majority of users, I would think that if we want this to go smoothly, I'm doing it when *users are online to update their nodes is probably the most important thing. not necessarily, you know, making it so it's nice round number of 10 or, or even fulfilling that eight one on two goal, but that's nice to have both. 

**Danny**
* Can we sanity check the 8 1 9 2 just real quick then? 

**Arnetheduck**
* So I think we'd be looking at 1.4 8, 9, 6, which is that time that hope you can see and it's highlighted there. so it's still on six. That's pretty reasonable for everyone except LA. 

**Danny**
* The us was that plus how much time from the previous, So that it's a little minus or the nice round number. 

**Arnetheduck**
* Okay. Okay. So that was like minus 10 hours. Okay. And what does Las at four 30?

**Danny**
* We've definitely had forks at four 30 on west coast. Cause I know Terrence has been on them pounding coffee. 

**Adrian Sutton**
* It's 1:00 AM here now. So I'm not entirely sympathetic. 

**Danny**
* Yeah, I hear you. I'm I don't think that that's like bad for users. I'm fine with saying that is a good tentative number and that we will kind of circulate it in a PR and put thumbs ups on it Sounds good to me. 

** Adrian Sutton**
*Okay. Sounds good to me. 

## TTD [59.14](https://youtu.be/CIAGQMUKEZ4?t=3554)
**Danny**
* Great. Moving on to, TTD, which Mario  has, been working on a doc here on predictions, Mario. 

**Mario Havel**
* Thank you, Danny. So yeah, sure. so, yeah, thanks for sharing the doc. So should I share my screen as well? Please Let me know if you can see it. Yeah. Thank you. Good. So, yeah, so I, I, I would love to present, the *proposed TTD value for the merge, which, are this dark explains the strategy behind our choosing the number and, I'd like to get feedback on that and prism develops itself. So, just to give you a quick overview on how the number for the TTD speakers, first it's, using polar Miller regression, from past few weeks. So basically data on difficulty in the network from past few weeks, extrapolated in next two weeks to predict, what value after two difficulty will be reached at the given time it's done using the prediction tool, which you might, might notice if you are followed, what eligibility of it's a fishing. it was, it was, used for predicting the distance mergers before. So, we established what is, what is roughly the difficulty, the difficulty to expect at a given date, but the problem is that, the accuracy of this, is purely, purely depends on, how the hash rate will evolve on the vote total penetrate. So, we have to understand, what historic levels are we working with are looking at the current, trends in the hash rate. we saw in may that it peaked at all-time high and then in June dropped significantly. And currently we are under 900 terahash on average, it's like 880 hash, of course price has a certain influence on this because, the hash rate depends on the profitability of mining. So, here is charged since January on, where just the pricing and the hash rate is put together. So we can see that, the hash rates somewhat reacts to the, price changes as well. And, wait, look at the history. so we can, because the total difficulty is basically just their commodity difficulty though. We can, we can exactly calculate how, how, what is the irritation rate in the network needed to achieve a TTD at a given time? So, here it's visualized over a bigger timeframe with an example of, the total difficulty value, which, would be reached during September with current numbers. And what this shows is that like to achieve this, total difficulty like during, during August, for example, you see, it's, it's a huge number, like up to five and a hash, and then it comes, drops fast, and then it declined slowly. So it is the trend that we are working with and the red part is the September. So, this is where we are on the curve, and, what using this script, you can generate the I'm gonna run it just with, TTD value or the total difficulty value to, to generate, the charts with and, and, and, even created charts which are below. but, so, so, why do, would we consider here with this Rudy strand, is that what you can see that in the first days and the first part of the month, basically it takes, more, more history to achieve devalue and then it declines more slowly. So we have like better protection against the uptrend rather than the downtrend. And, so I was, I was a bit pessimistic with, with the estimates because, of also the deck size issue and, and, I wrote it down the numbers is if you will see. So the first, the first scenario is counting on the Bellatrix is happening on 31st August, or maybe, maybe first September, which would, which if we need like two other two more weeks to achieve TTD, we would be around 15 September. So first here we, get roughly the number still to difficulty, which will be reached on 15 September. And I rounded down, this, this, also we want to have a nice number, which is a bit easier to remember. And, this number is however, it's, it's not much difference to be like less than 1200 difference with recurrent history. So, and these, these are charts, which you can produce with this script above, and, these show us, basically how much his rate is needed to achieve the TCD over the timeframe over the period of September. So, with this, with this TTD devalue, you see the red line is the currently something under 900, terahash where the current current hash rate it will be hit around the 15th of September. And, if the history goes up up to let's say that wasn't here, it would be, it would be like 10, the 10th of September. And if it drops to 600, there has, should, would be kind of the, beginning of the August. And here we can see as in percentage. So like what percentage change of the hash rate we can, we can expect. And this is a people, some raising good and comparing it to a all time high, history all-time high, and, and the current value. So we can see that to achieve this immediately after Bellatrix in the first days, it would take a lot of hash rate, which is probably the possible adult. And then, by the end of September, even if, the hash rate, for comparing to current number could go down 30%, we would achieve it by the end of September, and here, our other, examples of TTD value, which, give us more space for, history, to be achieved by, this, this, drop by numbers is meant as a 15th of September. So, in frustrate drops by 5%, this value would be achieved under 15. And, you can, you can use these values with a script to produce these charts, if you are interested in details. and the second scenario is, we would September 20, where the TTD values are a bit higher. So, here I rounded down the number again, just a bit more. It doesn't make much difference, but, the fingers that we have, maybe less room to achieve for the TTD here before the, before difficult. So, here, you can hear I'm here. I'm, I'm counting, by the, video October seven. So the numbers are here and, yeah, it's a bit less it'll maybe, but it's still reasonable. yeah, so I guess it's it, if you saw the drop, if you have any comments and feedback, please let me know. 

**Danny**
* Would you think approach When we say I'm all to him, needs to be reached, obviously it's for the entire time period, is that time period is starting today or in plus one week from today? 

**Mario Havel**
* I'm sorry, what do you mean the old time height? 

**Danny**
* Yeah. For, yeah. To hit those, like, in that chart, is that saying all time high from starting today or all time high, starting in plus one week, this, this has meant, so does this just compare to the old time high, which *was, ever achieved on the internet work? 

**Mario Havel**
* So like, that's like the maximum uptrend we can, But it's saying, it's saying if like, literally now we hit all time, high hash tray, this is the date the TTD would be hits, correct? Yes, yes, yes. 

**Tim**
* Literally now, or literally one week from now when that would start When I did a doc. 

**Mario Havel**
* Yeah, yeah. It's from Monday. So the numbers now would be even higher. Yeah. 

**Danny**
*And, you know, the next week being kind of the defensive selection of TTD when probably an attack would actually occur because we would observe and adjust between now and then, that makes the number even higher. 

**Mario Havel**
*Ah, right. Yes. Okay. Yeah. Yeah. Basically the charge would stretch and you can, you can generate the chart and see by yourself, to, to get to the exit number for the current moment, because, we heard update this all the time, but, yeah. basically the, the, the closer we are, the more it takes to achieve. 

**Danny**
*Okay. So one of the things we'd also be observing over the next seven days would be an increase in hash rate, such that one of these, that kind of, timing attack scenarios might occur. And if we didn't, then we're in an even better position with respect to the timing attack scenarios and what it would require starting a week from today. so Mario, none of those, so, there's been a bunch of chat going on. it seems like there's certainly a compromise and a bit of a debate as to how far after you do this. with respect to what is likely a September 6th Bellatrix, we see two weeks, we see someone arguing for even less than a week. and, but we also see at least from the people who've have been participating in that, something like a 10 day compromise, which I think adjusting for the numbers that Mario gave us, knowing that we would have good, really good visibility on them, on such an attack on plus one week from now, 10 days is probably in that safe spot with respect to all time high, which we can crunch those numbers a bit more. that's at least the synopsis from what's going on the chat, I'd now open it up to discussion points on plus X days from Bellatrix on square. 

## Bellatrix x days discussion [1.10.00](https://youtu.be/CIAGQMUKEZ4?t=4213)

**Ansgar Dietrichs**
* Right. so I just wanted to basically say that just because like any such attack, we would see like, well in advance, as you're saying, basically, I mean, some of these calculations say like, would have to have spiked since *Monday, already, over spike is Digiday or whatnot. So, so we would see this well in advance. So I don't, I think physically kind of talking too much about the specific kind of delay in days kind of gives this impression as if that would be a time period in which we would have to react, which is the, at that time it's, it's already too late, right? So like the, the time period to react would be between now or whenever the kind of the third attack would start. Right. And Bellatrix, and so I personally would be very calm, comfortable with even like a relatively small, kind of delay in days between Bellatrix and TTT, just because that's not the time period that would have to, to allow us to react. 

**Danny**
* So I personally think the very weakest, So there are two, I think, two things to, to balance here. One would be in the event that something with belchers goes wrong, a sufficient amount of time to resolve those issues. and then another is, if we're going through the strategy that we will make it very clear that there will likely be hardened ELL releases after Bellatrix some sufficient lead time in posting that blog post. 

**Tim**
* And, We can also have you happy I'll releases Like before, right? Yeah. So that does. 

**Danny**
* So, you know, at least I don't think I would go less than a week. I think a week with the error on TDD means it could even be five days, four days, just on my gut. so yeah, other takes on the plus X days from Bellatrix, I'm for 10, 10 days, at least. 

**Marius**
* And I think we also have to consider that a lot of people, did not follow the discussions. They need to have time to set it up and they would set it up in the last possible moment. So if we give them a couple more days to, to set it up, That is a good point. 

**Danny**
* There are two types of, well, there are many types of users. There are validators who will have this setup before. Bellatrix almost all of them. someone will forget, but then there's actually all other types of users, which some of them actually seeing Bellatrix happen might be the prompt actually setting up their nodes because they wouldn't, they wouldn't actually be knocked off the network before then. So there is a bit of an argument that there is a type of user that would be actually waiting until that last window to really be kicked into gear. 

**Micah**
* I would put, argue that type of user is likely very common. because if you, if you only want to upgrade once and you don't want to do anything, you're gonna wait until the like, you know, day before or two days before, you *know, in enough time you can make sure your node syncs and turns on. But if, you know, like the hardened releases are going to come out later, you don't want to deal with that anyway, you want to do with it all at once. And so I suspect there'll be some users who wait until a very large portion of users. Wait until the last minute we are last minute, those harden releases the stable and everything looks like it's healthy. 

**Arnetheduck**
* So other, other weighing ins on this, one question is on the TTD built in into clients. Do we expect clients to have the TTD built in, or do we force users to set a TTD flag? 

**Tim**
* Just, No, we would want the releases. We would want the releases to be ready with the TTD. And this is why we would, you know, at tentatively choose it today. Client teams can pull out a PR, you know, with that value doesn't need to be merged and it'll be reconfirm on Alcor devs next week. And then you can merge that number. so users don't need to use a flag except in like the emergency scenario where, when we do a, the override for a reason or another, well, we'd be doing main net shadow forks after Bellatrix and we need extra time for those. 

**Danny**
* I think the main net shadow forks will continue until the merchant will have definitely have them before. And, shoving one in or two in the middle also does not sound like a bad idea, especially if a client releases are still rolling out. 

**Parithosh Jayanthi**
* Yeah. The plan is to have them every week with the latest state manager uses. 

**Micah**
* And, so if we want at least one, so that means if we do them once a week, really take like, is there a minimum amount of time we need in order to get at least one shot of working after Bellatrix Oh wow. 

**Danny**
* Because the old clients might have hardened releases around them, additional releases around them. 

**Andrian**
* I mean, I, I just think, think of us setting it TTD, we're making the decision to ship. So shadow box are useful to keep testing out, but I don't think we need to condition on it because we've made the decision to ship By. Now We shouldn't be sending this. 

**Danny**
* I wouldn't be suggesting conditioning on them, but, they are valuable tests. And if somebody has a regression last minute, they can, we want our users to be ready and willing to ship an upgrade. and if we found a regression and patch something, then it will be good to find the regression and it'd be good to patch it. 

**Tim**
* And then in, in practice, like, you know, we usually have the midweek, we have the Bellatrix happening on a, on a Tuesday, north American days. Usually shadow forks have been on a Wednesday or Thursday, and then we'd have another week from like that shadow fork before hitting TTD on main that we could literally have a shadow for a good day before maybe that if we really want to. yeah. So I think we have plenty of time to like, have a shadow for fixed massive, like last minute issues from it. do a TTD override if we found something absolutely terrible and that shuttle forge and still not be hitting. 

**Danny**
* Okay. So, it does seem like people are generally okay. Converging on a compromise. there's a bit of a call for a September 15th number, which I think, was advertised in Morrow's document. 10 days would be that September 16th. are there other things we need to discuss right at this point? Or can this show up in a PR and a suggestion and we can circulate, yeas or nays there. We'll be sending you a mic. 

**Micah**
* Marinez Micah. Sometimes I feel like, I feel like Thursday is better than Friday for if we're thinking between them two. 

**Tim**
* Yeah. We're not though. We're picking the illusion of the Sure. 

**Micah**
* Like if we target Thursday, we're more likely to hit not the weekend than if we target it Friday. We talk Fridays. It's very likely we'll hit a weekend. Yeah. We can try to not hit the weekend. 

**Tim**
* Oh yeah, I agree. Yep. Okay. So yeah, it seems like in the chats, the original numbers suggested by Mario of, 5, 8, 7, 5, and zeros all the way to the end, as rough consensus. So we can, I can open a PR on the execution specs, I guess a little bit of PR for Bellatrix as well on the cl specs, and can probably merge that PR on the cl specs and just reconfirm on all core devs. this number in case we see something funky, on the network or if, for whatever reason the calculations are wrong. So people basically have a week to just, send it to check that Thumper. but the assumption is if, if it is actually the right estimation and we don't see anything, weird under the network with regards to hash rate, we would merge that and expect client for nieces pretty quickly after. 

## mev-boost status update [1.19.00](https://youtu.be/CIAGQMUKEZ4?t=4778)

**Danny**
* Okay. Any other comments here before I move on? Great. We have about 15 minutes left. I don't think that we're going to get to the 4844 discussion today. I would, I think Emmy boost stuff is a bit more pressing with respect to shipping the merge. first of all, is there a general kind of MEV, maybe boost status update, and then we can get into these two items of discussion and it's okay if there's not, I don't know if I have anything to add. 

**Elopio**
* Sure. by the world, the general status update is the same as this week testing and focusing on lifeness issues for mitigating extreme cases and working on the really monitor. So I think just talking about the monitor seems *appropriate here on this. You have questions. 

**Danny**
* Okay, great. so the first point which was brought up by Alex is clarify, local buildings should happen in parallel. Alex, and you talk about this please. 

**Alex (Stokes)**
* Yup. Yeah. So, there's two PRS that I'd like to discuss. The first one should be pretty straightforward. Let's see. I'm going to try, yeah, let me drop it in the chat. So this is really just a clarification and the builder's *facts and it concerns how proposers should be using this external builder network that exists BMF boost. And, the way the spec was written is I think you could interpret it as, so basically there's this timeout where if you call to get an external block or a remote block, you basically give that network, like, let's say a second before you say, okay, they're not going to like help me now. And I should build locally, without this PR I think you could read it as I should not do anything until I know that decision, whereas it's much better to have started building ahead of time. and that's all this PR does is that you should do both things in parallel, 

**Danny**
* Which I'm in very strong agreement of, there's a point of no return when you sign that like a blinded block. But before that, I need to be ready.Yeah. 

**Alex (Stokes)**
* Right. So yeah, this one's more informational, just be aware of this, if you have some spare cycles, which I know we all have tons of time over the next few weeks, but, if you have some spare cycles, just double check that this is the behavior that you're a beacon node and or value your clients are following. 

## circuit breaker design update [1.22.40](https://youtu.be/CIAGQMUKEZ4?t=4961)

**Danny**
* Thank you. And then Alex, I believe you have the next item as well, which is the a circuit breaker, which was discussed, I believe a couple of calls ago. any what's the status update here? 

**Alex (Stokes)**
* Yeah. So we discussed this on the last call just to refresh everyone. And this is the idea that, regardless of this external block building network or not, you know, we could still get an a case where suddenly there's a liveliness, you know, a series of I miss faults, even though I miss failure on chain, right. So things to get quite serious and the idea is, okay, it could be possible that this external network is doing this. And so the sort of most paranoid and or most sort of secure thing we can do is just stop using it, at least temporarily. So, I had this like a sort of sketch of a proposal last time. I've refined that into PR. So, yeah, I suppose I would like to get feedback on that. I'm not sure if you guys have had time to review the PR, I guess I can just at a high level go through it. And the idea is that there's some rolling window. So basically you look at, let's say an epoch of, of slots and that's the rolling window over the current Ted. Thanks Terrence. So the PRS here, 47 on the builder specs, you have this rolling window and then basically if you have some number of missing box within this window, you say, okay, circuit breaker on, and I do not use boost, when that condition reverses in the sense that within the rolling window, I don't have that many missing box, then I'm free to use it again if I want. So then the question is like, yeah, how do we pick these numbers? I have a suggestion here basically saying like, you know, if there's around half of the box missing and a given slots per you pocket number of slots, then we trigger this thing. I think we can probably talk about these numbers and, or yeah. People want to take a look. That would be nice. but yeah, I think, I guess first, are there any questions right now from what I've said or something that was unclear? 

**Danny**
* So it was probably two design points here. One is to do rolling and be able to turn it back on in which we could probably have a smaller window as you suggested 32, or we don't have rolling. And it's just, you just turned *off and needs manual intervention at which you'd want a much longer window with an assumed adversary size so that they couldn't, you know, with random shuffling, they wouldn't be able to adversary of size X wouldn't be able to do that and just, caused the shutdown. 

**Alex (Stokes)**
* Right. So I don't know if people have any of the, you know, if the seal devs have opinions here, the idea of throwing window is that it basically makes it such that there's automatic recovery. So, the thinking is that it makes it harder to gain, just because, you know, you're going to trigger this somehow and then take off the whole block building network for like, you know, half a day or something while people recover. And instead it would be this like automated recovery. 

**Danny**
* I guess there's a complexity argument. One is every time you're just querying your state because you can check empty slots from your state. And you're just, it's a dynamic quick query. The other would be, I guess, a query *along with maybe a database flag to turn it on and off. my intuition is actually the former with the rolling window is less complex. but I could definitely be wrong there. 

**Alex (Stokes)**
* Right. And so there's also kind of segues into, like, I don't know if there's a second design point that you were going to call out, but essentially, moreover, this PR suggests that clients actually randomized their values within this window. And so the idea is that if you don't know exactly what your client is going to do, then it's much harder to gain, right. And you sort of get this like herd immunity across the whole network because you know, this node is doing one thing and it's notes during another. So it becomes much harder to like find these boundaries to try and try and trigger this thing, maliciously. 

**Danny**
* I mean, you do still get like a profitability distribution, which often is enough for an attacker to do something, but, yeah, I'd have to think about it more. 

**Seanderson**
* So in lighthouse we actually have an implementation of this rolling window and we check for like, if there's been eight skips in the last epcho and it's, it was pretty simple to implement, 

**Paul Hauner**
* The diversity as well. and I think it's also useful as well, because I think that's going to be some users out there that I kind of just, you know, hardcore. I just want all my Mav and never to stop. and I'm generally of the opinion that we probably want to try and like allow them to run safely without creating forks in front of manager and repos and stuff like this. So yeah, giving users, the ability to tune that I think is, is helpful. 

**Danny**
* So we could just say in the builder spec recommended value. And, but that it's tuneable, I mean, it's not a consensus value, so you can't enforce it really anyway. 

**Alex (Stokes)**
* So we would just supply one fix, like, you know, pick a number 16 out of 32 blocks or slots. And then also say by the way, what these are configure this. 

**Danny**
* Yeah. I would pick a number that we kind of deem safe under different considerations and then, say that it can be configured locally. 

**Alex (Stokes)**
* Okay. So another consideration here is that it would be great to have this rolled up before the merge or as soon as possible. Right. So, I think taking that into consideration, this is hopefully something that's like pretty straight forward to implement and it isn't to a, to a Harry. So I guess if no one has any comments on the general design, then yeah, we could take, the specific parameterization to the PR. 

**Danny**
* Okay, great. I don't believe that starting this 4844, points of discussion, there are many went to discussion is going to be fruitful in the next four minutes. So I would suggest we defer until the next call, given that okay, Tim, please. 

**Tim**
* Oh, I'm going to say, I think that's reasonable, but there's nothing that's like urgent for today. 

**Danny**
* Great. So let's are there any other final discussion points for today? Excellent. Thank you everyone. I will talk to you very soon and, talk in on CRA devs in one week. Thanks everyone. 


---

### Attendees
* Marius Van Der Wijden
* Danny Ryan
* Mikhail Kalinin
* Stefan Bratanov
* Chris Hager
* Sean Anderson
* Pooja Ranjan
* Saulius Grigaitis
* Terence (Prysmatic Labs)
* Enrico Del Fante
* Paul Hauner
* Thegostep
* Phil Ngo
* Ben Edgington
* Carl Beek
* Hsiao- Wei Wang
* Trenton Van Epps
* Dustin
* Caspar Schwarz-Schill…
* Gajinder lodestar
* Lion Dapplion
* Andrew Ashikhmin
* Fredrik
* Mamy
* Micah Zoltu
* Pari
* Stokes
* Cayman Nava
* Mario Vega
* Arnetheduck
* elopio
* Dankrad Feist
* Viktor
* Preston Van Loon
* James He
* Marek Moraczynski
* Saulius



