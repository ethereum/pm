# Ethereum Core Devs Meeting #139
### Meeting Date/Time: May 27, 2022, 14:00 UTC
### Meeting Duration: 1 hour 45 mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/528)
### [Video of the meeting](https://youtu.be/5mMd-XHAv2Q)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)
### Summary
## Decisions Made
|Action/ Decision Item | Description | Video Reference |
| ------------- | ----------- |----------- |
| **139.1**   | So, for Robsten specifically, you know, clients are going to put out releases with the huge TTD value in the coming days. If you've already downloaded a client's release that includes Robsten TTD support for a value like the one we hit yesterday, you must upgrade your TTD value to the new, new one. We'll make an announcement about the new Robsten clients early next week, which will have this pretty high TTV hard-coded in. And then, once Bellatrix has occurred, on June 2nd, we'll choose, I guess, a realistic TTD number, that will confirm on June 3rd, we'll probably choose that to happen, like, in theory, 10 or so days later, but then we'll try and add some hash rate for it to occur around June 8th. But those are very rough targets. We cannot absolutely guarantee it. | [36.34](https://youtu.be/5mMd-XHAv2Q?t=2194)
| **139.2**   | Tim - Launch of the Sepolia beacon chain should happen next week, as it just requires some coordination | [43.14](https://youtu.be/5mMd-XHAv2Q?t=2594)
| **139.3**   | I think it's pretty clear from the EL teams that we don't want this to be a requirement for the merge, especially if CL can kind of hack it by calling every single block by hash. But, yes, having some comments on the spec would be helpful. Yes, the general API is understandable. However, we do not intend to implement this before the merge. | [1.03.43](https://youtu.be/5mMd-XHAv2Q?t=3820)

**Mikhail Kalinin**
* Hi, Gary, How are you? 

**Gary Schulte**
* Doing all right. If I joined early, because I have a tendency to forget about the meeting until five minutes past, 

**Mikhail Kalinin**
* Have you all heard the, 

**Gary Schulte**
* I know we're doing some extended burden on,  some native library changes, but probably right after the call, we're going to cut a release. 

**Mikhail Kalinin**
* Okay.

**Gary Schulte**
* They just, out of curiosity, do we have any idea what,  our briefing,  participant on Robson is paying for that hash rate? 

**Mikhail Kalinin**
* What or how many, what was your question? 

**Gary Schulte**
* Well, I mean, just how expensive it would be. 

**Mikhail Kalinin**
* I don't know, but it's not that much expensive. 

**Gary Schulte**
* I was thinking that I'm on suppose Leo, maybe we should go ahead and, just rent some hash rate to bump the hash rate up to a point where we would, it would be easier to estimate TTD and we wouldn't be so susceptible to, you know, TTD in this way. 

**Mikhail Kalinin**
* Yes. But we don't know how much any attacker would like to spend and is ready to just spent on it. I don't know. It's a, if it's like an attacker that us, the hardware, because it's basically electricity, right? 
* Yeah.So we don't know like,Yeah. Right. Yeah. I think that the easiest ways to have the procedure that we have discussed, I mean, it's like, yeah, kind of it's in solution, but we still have a risk to hit the day before. the notes are upgraded with, with the real TGB, right. With the real to do deeper Andrew. But this risk is lower. And the plan is to have like said the to deep brand or a related way high. Then now it's nodes of upgraded and then we can accelerate the hash rate if we can increase the hash rate, if it's not enough to get down in the day that we expect it's there, the network. 

**Gary Schulte**
* Okay. Yeah. I mean, I think that the strategy I saw you outlined something sounded good. I was just wondering if we could at least make it more expensive to, to grief in the way that we had in the way that this is and why this happened on Robson. 

**Mikhail Kalinin**
* Yes. Yeah. But I just think that we don't know how much we will have to pay by the end of the day. If we would know, then we can estimate the cost. Yeah. Make a decision of that. 

**Micah Zoltu**
* Hey, pre-party people. 

**Angsgar Dietrichs**
* Hello? 

**George kadianakis**
* Hello. 

**Micah Zoltu**
* So we have the party lounge for the All core dev does after party. I feel like we need a green room as well for the pre party. 

 **Lightclient**
* Good morning. 

**Marius van der Wijden**
* Hey. 

**lightclient**
* Hi Martinez. 

**Micah Zoltu**
* Today's going to be a good day. We have two, two lake lines. 

**Lightclient**
* One of them disappeared 

**Micah Zoltu**
* Bad day 

**lightclient**
* Back to a bad day. Back to BM, BM, 

**Lightclient**
* This is a healthy number of people before the meeting. What are you all doing? 

**Marius van der Wijden**
* Not working 

**lightclient**
* Evening for you. 

**Micah Zoltu**
* I'm preparing my remarks for the meeting, getting my arguments in order. 

**Tim Beiko**
* What did I walk into? 

**Lightclient**
* People are here early. 

**Tim Beiko**
* Oh, I thought it was like some sort of mutiny. 

**lightclient**
* We have some bad news feeds. 

**Micah Zoltu**
* That's right. I have decided this is that dictatorships work. Right? The dictator decides they're in charge now.And then they are.

**Tim Beiko**
* And then they convince like clients and then yeah.
* It's downhill from there.Yeah. If you have black clients Marius, you're in, you're in a good, good spot for dictatorship. 

**Micah Zoltu**
* That's right.Let's say 

**Tomasz Stanczak**
* The Triffids Micah is just briefing everyone before they call. And then we pretend to having arguments, 

**Tim Beiko**
* Right?Yeah. 

**Micah Zoltu**
* The price is hurting. Guys. We need to spice up our all core devs calls. This is what we're going to discuss. Thomas. You take the, you take the conflict. I'll take the profile. 

**Pari**
* At what point are we yelling?outlast On money 

**lightclient**
* That comes right out to the frog pal. 

**Pari**
* So like five minutes.

**lightclient**
* Yes.Yeah. 

**Tim Beiko**
* Oh, Trent. I see you're answering the YouTube comments and people are complaining that it's boring, but these show up anywhere for the calls. Yeah. 

**Trenton Van Epps**
* Yeah. This isn't the first time people have complained. It's boring. So I don't understand why they keep coming back. 

**Tim Beiko**
* Okay. Would that be boring? Yeah, that's true. 

**lightclient**
* They were saying 

**Tomasz Stanczak**
* In the middle. 

**Tim Beiko**
* No, we talked about sponsors. The only thing I'll consider is if we can get some nice where our sponsors gets light, the light types. Did you have a computer in an Amsterdam? I think you did, but I have the computer. 

**Micah Zoltu**
* Yeah. The only sponsor I don't accept is a microphone sponsor. 

**Tim Beiko**
* Yeah. Headphone and hardware sponsor. And I'm willing to just show them in the halfway through the shop. 

**lightclient**
* Today's Allcore dev brought you by Beats by Dea.. (JK)

**Tomasz Stanczak**
* Maybe, maybe it'll March Superbowl one day. 

**Tim Beiko**
* Oh wow. Yes. We do marketing. We do marketing for all All core dev so that more people watch All core dev, And then we can get some spot in the show itself 

**Tomasz Stanczak**
* And look 30 seconds in the middle and all that everyone will be finding for. 

**Tim Beiko**
* Yup. okay. People are still rolling yet. Let's wait a minute or two. 

**Micah Zoltu**
* So today's All coreE devs. We're going to talk about,  selling EIP numbers, right? 

**Tim Beiko**
* Oh, no. I thought, yeah, that's actually a good idea. I, to go hard fat auctioning the Hartford names as well, like Yeah, yeah. I know. Yeah. If you know, numbers is actually much smarter and you just like mint them all as an FDS, we all trust Providence if he comes to them, because address. 

**Tomasz Stanczak**
* Yeah. I like the idea. It's like, I read it. I felt at the beginning it was a joke. And I saw like, well actually it works. 

**Micah Zoltu**
* Yeah. Yeah. Just as a fun exercise. I am trying to put together,  a actually legitimate auction that is not a formal auction to see if it's possible. 

**Tim Beiko**
* And I think we've 

**Micah Zoltu**
* Got Most CK proofs and everything. 

**Tim Beiko**
* It has to be like,  it's not going to be a one-time auction though. Cause it's like this weird thing where people don't want to buy the IP number. I guess people will hoard them at first. You need a really high like transfer fee though. You need like a really high, yeah. You want to get proceeds from the secondary market from this. 

**Micah Zoltu**
* I'm actually more interested in just,  I suspect that if we did a legitimate auction, we would still make enough to fund the EIP process. And I think it would be good opportunity to show the ecosystem what legitimate auction. That's not just someone marketing actually looks like, oh, a pretty good job there. They're just really legit. 

**Ansgar Dietrichs**
* I would argue though, that like in this spirit of minimal issuance, we would have an obligation to burn all the proceeds.So I leave for this position just to be clear 

**Micah Zoltu**
* For maximal maximal neutrality. 

**Tim Beiko**
* Okay. I think, I think we're going downhill fast here. I've posted that, that shot. There's enough people on the call. I'm going to move us to YouTube. one sec. Okay. We are live,  for All Core Devs number 139. we have plenty of merge things to disco today. And if there's any time left over,  we have two quick updates on an EIP that people wanted to present. first thing,  I guess is the Ropsten TTD issue that we saw yesterday. does anyone want to give a quick recap? I kind of wrote a recap, but if anyone else wants to just run through what happened, that would be, that'd be great. 

**Micah Zoltu**
* Okay.That's your job. 

**Tim Beiko**
* Okay. Okay. I guess I'll read from my document, but high level. what we saw is, the Ropsten  hash rate go up like 20, 30 X overnight.  we always kind of knew this could happen, but previously did not mess with Ropsten as much. and this kind of led,  the network to hit the terminal difficulty for emerge before the beacon chain for Ropsten was even alive. So Genesis is scheduled for May 30th, I believe. and, and this guy had just put things in a weird spot where like validators were, or sorry, upgraded nodes got into thoughts that TTD had been hit, but,  the beacon chain not exist yet. and, and, the amount of like money that it costs to raise the hash, Don Ropsten is quite trivial. So, you know, even if we raise the TTD, like twice, three times 10 X, it's quite possible that somebody might just mind enough,  might just invest enough to mess with that number as well.and so basically in order to prevent,  that we've kind of moved to,  a solution where, we override the TTD to an incredibly large number, have the beacon chain GoLive have Bellatrix happened on the beacon chain and then,  override the DTV again to a number that we expect to happen fairly soon. And so that means that like up to, up to Bellatrix being activated,it's basically impossible that we would hit the TTD. The number we chose was about twice the total difficulty on the theater main net, which on Ropsten's hash rate would take about 250 years to hit. so we're safe there, but then yeah, what's Bellatrix is hit.the, the plan is to choose another TTB, which expected to happen soon. And, upgrade this again. I guess just for people listening, you know, that this can't really happen on maintenance and the reason is that for this to happen, you know, well, this was caused because the beacon chain was basically not live yet.And because of how hard it is to predict, hash rate that's, that's how variable it is obviously on may not be contained as life. so that's not a problem. but then there's still this potential problem of like, what if PTD was hit before the Bellatrix upgrade was live on the beacon chain.and they're the reasoning is, well, we can, we can predict hash rates, you know,fairly well on my neck. And most likely to not pass rates would be going down rather than up, because we approached emerge. so the odds that like a ton of hash rate would join the network and the forced us to hit TTD much earlier than expected. This is quite low. and depending on like, you know, like basically if we saw hash rate two X overnight on main maintenance, it means there's now enough new hash rates to conduct the 51% attack and like proof of work security guarantees.We can not by that point. So we can have like pretty reasonable bounds on the TTD,  on, on main net. and the worst case it's usually like, it just happens later than we would expect. but yeah, for test nets, given that like Gordy is obviously on proof of work or sorry, Ropsten is, is obviously a proof of work and it's easy to manipulate say what's the Sepolia. It seems like what makes the most sense is just saying this very high number that Bellatrix happen and then, and then send it to another TTB that that's much slower. 

**Marius van der Wijden**
* So yeah, one question I have is why do we need the TTD? And Bellatrix why not just make the electrics, if like, if we don't specify a TTD for Bellatrix, then we will look at the look at the TTD from, from, from the or the TDF from the one chain and just ignore it because we don't have a TTD set. And so, I'm a bit confused to why we need to set the TTD for Bellatrix to happen and why we just schedule Bellatrix and then set the GTD. 

**Mikhail Kalinin**
* Do you mean that, why do we need to do, to be a part of cl clients binary? Or do you mean that why do we need to set to D  like to, to like deploy a real, to, to deal within the ballot treats?The second. 

**Marius van der Wijden**
* Yeah.Why, why do we have it have to have it in one release, and I guess we don't, 

**Micah Zoltu**
* I'm gonna throw out an answer, in the spirit of the internet and saying something wrong, someone will correct me. I believe the reason is that the clients concerns of clients as currently written, Bellatrix kind of, they expect a TTD to be available when with Bellatrix like, they need something for that value. They need to put something in there, because they have a constant somewhere in their code and they need to set it to something. And so we need some number to be in, in that spot when Bellatrix goes live over the Bellatrix clients are released, I should say, that number can be giant. It can be, you know, you hit max, that's fine.  but it needs to be something. And that's why, when we talk about, we need to TTD for debt filled tricks, I believe that is the reason, that someone can correct me. 

**Mikhail Kalinin**
* Yes. But as I understand what Maris was saying, as that we can put a placeholder then, for educated, well, you predict a large number and then wait for village bricks to happen. Then like cots release another, another, like series of releases clients with the Realty to the, is that what you mean? Marius? 

**Marius van der Wijden**
* Yes. Or like the easiest way and the way I would, like, I would have thought that clients would have implemented it as if we, if we don't specify a TTD with Bellatrix, then the Bellatrix folk will update the, make the consensus changes, but not, verify the, the, the TD from the,from the execution layer chain, against, against what we don't have.So 

**Tim Beiko**
* I guess, given that all the testing of like the past year has happened with TTB on Bellatrix, it's probably much safer, like, and that achieve the same outcome. They just have like a really high value rather than try and change the code now. And have it say, like, if there's nothing do this, is there, like, I, I'm curious to hear just a couple of cl folks on the call, like, I don't, do you feel more comfortable with one way or the other? 

**Marius van der Wijden**
* I think it's like, I actually think it's fine to set it to some really high number. but I'm just like, I think it's a bad design decision to, that has been done previously and we can like, doesn't make sense to turn it around now.It's just for, 

**Mikhail Kalinin**
* I think it's like not a big deal now. I mean, we can set it to like where a lot of Shaba,  but yeah, this is what we're going to do with, on support on the main net,  like,  what are we going to do with Paula is to set the real ticket the after bill and fix happens. Right.but yeah, for the main nets, I'm not sure about that.That's like, do we want to have to release this? 

**Micah Zoltu**
* So I, as I mentioned to 

**Mikhail Kalinin**
* Reynolds upgrades, 

**Marius van der Wijden**
* Yes.I think we would want to have two rounds of upgrades. 

**Micah Zoltu**
* Yeah. And, and the reason, the reason for that, for those listening, who don't fall discord is that having your test nets follow the exact same pattern as your production network is very valuable. it also impacts third parties. So third parties who want to be able to follow the Sepolia upgrade, and they set up the run to set up their scripts. And if your institution, you may have a big infrastructure that you need to go through and you have a checklist and all of these things, having that be exactly the same for test nets and mainnet with the only difference being like, you know, whether it runs on client a or client or host air host to be,  it was very valuable for those, those people. And so I think it is important that we should follow the exact same procedure for the mainnet launch as first fully launch. Even if it feels kind of unnecessary on main net due to difficulty be much harder to, to play with. 

**Tomasz Stanczak**
* Yeah. I feel the same as suggesting, 

**Tim Beiko**
* Oh, sorry.Go ahead. 

**Mikhail Kalinin**
* I just wanted to ask,  about how much time would it take to upgrade at the second time? Do we expect the,  like the same time to, to upgrade to users upgrading their notes in both cases? So, okay.

**Marius van der Wijden**
* Like, can someone explain like really quickly what's in Bellatrix and why should we not just schedule it right now with a really high TG and then set the TTD once?Is that what you're asking? Yeah. 

**Tim Beiko**
I guess for the same reason that we can't schedule the merge, I assume there's still some testing, 

**Marius van der Wijden**
* But like scheduling the merger is something different, right? 

**Tim Beiko**
* Oh, 

**Marius van der Wijden**
* Merge means setting the TTD and scheduling Bellatrix is, in my opinion, it should be, in my opinion, something different from scheduling numbers. 

**Tim Beiko**
* I'd be curious to hear from cl clients here, but it does feel like the, the code that like cl clients have today is not what they expect to have on mainnet. And I don't know what, like the diff is here, but yeah.I see some prism Taikoo folks, 

**Ben Edgington**
* For tech you,  it depends when we showed you a letter. I think, I mean, I, I think we are basically production ready and could, could go, but,  if we are scheduling it a month out, then you know, that that would be fine, but yet it all depends on dates. Yeah. Not, not having a date. It doesn't, it doesn't help having a date helps. 

**terrence(prysmaticlabs)**
* Yeah. That's I think that that is seven would presume as well. 

**Tim Beiko**
* Okay. But, so, so, because like, you know, I don't think anyone is arguing that like, we could run through the main merge in a month. And so if it's like realistic that like Bellatrix could be scheduled that, you know, call it a month or two and give us some time to then,  yeah. Then, then make it really easy to set the TTD. that's probably a discussion worth having a, the cl call next week. but yeah, if I think that would, because the reason.That's like Bellatrix could be scheduled that, you know, call it a month or two and give us some time to then,  yeah. Then, then make it really easy to set the DDB. that's probably a discussion worth having on the cl call next week. but yeah, if I think that would, because th th and the reason, I guess, take a step back is I think the big, the biggest downside I can see with this approach of two releases is just that, you're yeah, you're just kind of waiting around for a while at the end, right? Like where you basically upgrade your client, the Bellatrix, you know, invalid Trix happens, but kind of nothing happens on the networks because Bellatrix is just waiting. and then, and then you have to like, run through this whole upgrade cycle again. And if we're just sitting around waiting, it's basically just a waste of time, but if we can, if we can save that, I think that's the biggest downside that, that there isn't this approach. 

**Micah Zoltu**
* If all, if all the clients have ATTD override conflicts setting, I would be personally comfortable with, having a fairly short time window between the TTD announcement and the TTD going live,  because anyone who can't, you know, quickly upgrade their client, because they need to do some, some additional testing or whatever, you can simply just do it to a TTD over instead, like, you don't actually need to do a full upgrade if you don't want there's two options, TDD override, or download a client that has the TTD baked in, and both of them are reliable, and you can choose which one you want, but that makes me more comfortable that we don't need to have the usual, you know, one month between scheduling the, the hard fork and then the hardfork Catherine, because, you know, clients are already out there, they've been out there for two weeks already. We can just say in two weeks is when we're scheduling, 

**Tim Beiko**
* Right.This just a suit. Yeah. This assumes that the ELL clients are already up there, which like in this case where we scheduled Bellatrix already might not be true, 

**Micah Zoltu**
* I guess.I guess what I'm saying is I think the time between the ELL, all the clients being released with the TTD hard-coded to a giant number and the time between the merge, that's the time period that betters that the choosing the TTD, you know, it does need to be some amount of time before the merge, but I don't think it needs to be the usual, like one month before. 

**Tim Beiko**
* No, I, yeah, I, I would agree there. I'm curious if anyone disagrees with that. Okay. And I guess based on that, this could also be like different for testsnet and mainnets. so give been that for like, we've agreed that we've basically agreed to a TTD of, I think it's 10th of the 32, if, if, if I'm right, but 10 to do something, which is about twice, what's the number on main net? clients, I think are the average pieces either today or Monday with this new value. and, and we're going to publish those like early next week. and then Bellatrix is expected to hit on June 3rd. that, that the 23 is a number.So Bellatrix is expected to hit next, next Friday on June 3rd. And because it's a beacon chain,  for they happen at an actual timestamp, so it's usually quite accurate. so that means like the quickest we could choose this new TTD value is like next Friday on, on the June 3rd. how long after, you know, and then I expect we either need new client releases or not. Like we can also just tell users that run the TTD override flag. so like early in the week after, like around June six or seventh, we can probably have a blog post up with this announcement. how long after that, do we want to wait until TTD happens on Robson? Because the original plan was June 8th and obviously seems incredibly close, was to have like a blog post on June 7th and heading the on June 8th. what are people's thoughts about like that delay between, yeah, basically having chosen the TTB for Robson post Bellatrix and, having it actually hits the network. 

**Marius van der Wijden**
* I think we should try to go for the data that we already said 

**Tim Beiko**
* The 8 0 8,So that, so that means we might be in the world that is like a blog post announcements coming up. I'm like the seventh, like all the clients are set already there, but then the four happens, the TTD has hit on Robson like 24 hours later. 

**Micah Zoltu**
* Wait, we don't, am I correct understanding that we don't expect clients to be ready until the seventh? 

**Tim Beiko**
* No. Sorry. So, actually, no, that's not true. We can be ready quicker than that. So I think what we can do,is I'm not sure what time  Bellatrix is scheduled for on, on the third, on,  on Friday the third, but basically as soon as Bellatrix has happened, we can pitch a TTD value. And maybe even like before, like obviously if we know that Bellatrix is going to happen in three hours, then we pick up TTD value. That's like in three days or four days. and, and we can also pick the value that's like in Peck days and then add a hash rates to make that happen quicker. so like on the third, we can probably have like agreements on a value and then you don't need to update ELL clients. They can all just pass it at TTD override, flag it.and I suspect those just like the time for us to decide, to teach you the value and then like,  kind of announced that the community and whatnot, it means it probably happens on like the Monday that people get aware of it. and that's, and I guess we can make it quicker if we don't wait for clients to be, clients are obviously free to then release versions and like advertise them to your users, but we can have like a kind of an announcement that just focused on the flags, would a note that, you know, that maybe your client will have a,Reese Virgin out. so that means basically by Monday, you can expect like the TTD is like known and communicated, and then you kind of have 48 ish hours before the four kits on Roxanne. 

**Micah Zoltu**
* I think it's important for those listening in, to understand that we do not have fine grain control over when the merge happens. Exactly like in terms of timestamps. And this is very, very true on test nets and it is somewhat true on maintenance. normally when we schedule our forks, we can get pretty close to where we want them to be. Like we shoot for a certain time of day with the merge. Everybody should be prepared for Teslas and may not that we may get the day wrong. and for T test tests, we may get the week wrong as we saw with Robson, right? We got it wrong by like several weeks. And with maiden that I think being off by days is not unreasonable. And so all users should be prepared for that. Like when we, when we talk about scheduling things for the eighth or scheduling things for, you know, this date or that date, users need to be aware,these are best guesses for us, we're trying our best, but the way things are designed, we don't actually have control.I mean, it's a censorship resistant system that we don't actually control. We only make suggestions and the system does what it does. 

**Tim Beiko**
* Right. And, and in practice, what this means is like, say we choose something on the third, which we expect to be even, you know, like on the 13th and we can then have Ash power to like, reach it a bit quicker. there is still a world where somebody like puts a hundred extra amounts of pass rate on, on Robson and it ends up coming over the weekend. Right.like I don't think there's anything you can realistically do to prevent that. so yeah, there's on Robson and this will also be true on civility. Yeah. There's like always a chance that like, as soon as we pick the TTD value,somebody shows up and we hit it like hours instead of days later, just because the cost is so low to mine on those. 

**Micah Zoltu**
* And if you're listening, please don't troll us. 

**Tim Beiko**
* You'll be disqualified for any future. Airdrops I'm kidding. does it, does anyone, oh, sorry, go ahead. 

**Mikhail Kalinin**
* Yeah. I just wanted to clarify that we are sitting in a real on six, right? 

**Tim Beiko**
* We would send it on the third, I think, because These Are at least I would prefer sending it on the third because it gives people the weekend as well to upgrade a bit their new their nodes. and the third is when Bellatrix happens. So we can either set it a few hours before Bellatrix or a few hours after. but like probably around this time on the third, because this is when people are like generally online. and we, we might also like, there's a consensus. They are called on the second. So I think, I think on the second that,we can maybe have like candidates TTDs and like, you know, that they assume that things are stable and then assuming like, nothing goes crazy before Bellatrix we can, we could probably reuse just one of those candidates. yeah. 

**Mikhail Kalinin**
* Okay. I see. Yeah.Yeah.Maybe it makes sense. And yeah, it's for as far as I remember is going to happen, like the balance rigs going to happen, like a 10:00 PM you to see I'll just double check it's. 

**Tim Beiko**
* Okay. Okay. So that means it's like this right now is like a 2:00 PM UTC. So that mean the is happening like quite late, you know, it's happening in like six hours from now. I still think we can probably send it TTD value like around this time, but it does become a bit more risky. That's like someone could just mind a bunch and, I, I don't know how much it would cost to like bring something that's like two weeks out to happen. And my guest in six hours basically. So there's a question in the chat, like, why can't we keep it really high and reduce it the day before? It's basically, it's like the lag between, we need to communicate this, this number to people. Like we can't just like choose, I mean, in a perfect, like if we control the everything over to network, we could literally choose a DVD and having to make 20 minutes later. And it would have really high precision, but it's like, how much time did we give people to like, look at their clients,announcements, read the blog posts.and so it feels like the, on the order of a couple of days is like the, the minimum and given this as a Testnet, I think for my nets would probably want something even even longer,assuming we need to go that route, but, yeah. 

**Mikhail Kalinin**
* It's actually going to happen on June 2nd at the ambient to see from what I could see from the conflicts. 

**Tim Beiko**
* Okay. Nice. Okay. Perfect. So, yes. Okay. So that means then I think on the cl call next week, we can have a boat and did they TTDs and then at the very least, you know, people will be aware of like, what are the options we can reconfirm that number,basically 24 hours after the cl call once Bellatrix has happened.so that did like Friday 1400 UTC roughly. we have,a TTD for Robson. Does that make sense? Okay. 

**Mikhail Kalinin**
* I also have a comment or kind of an idea.  does it make sense,to shut you the Bellatrix on the main net,in this, in concert, in the same release as,  like the,  very surely where your early and said that like two weeks after Uribe, and if everything goes well, as governor bandwidth can have this kind of, I don't know, probably two weeks, three weeks or whatever we find, 

**Tim Beiko**
* And that would be basically after Gordy.And that means about tricks on my nuts what's happened roughly around the same time as like the merge on CIPO yeah. Or something. 

**Mikhail Kalinin**
* What do you mean? 

**Tim Beiko**
* So Gordy's the next test that I think I thought Robson Gordy basically, 

**Mikhail Kalinin**
* Sorry, then I just mixed them again.The last one 

**potuz**
* There's, there's one thing that,setting early,Bellatrix handbook might trigger. There's a lot of validators that are running.  they're not running a net one note and for those guys setting Bellatrix will force them to actually sync. So we need to give them time at least and advertise that they need to start sinking their, their, their engines and that they need to be saved by the time that Bellatrix hits. 

**Tim Beiko**
* Okay. That's a great point. Yeah. 

**Pari**
* Which might actually be a nice feature because by the time TTP is, then we know that people are definitely 

**Tim Beiko**
* Saying, yeah.Okay. So I think, yeah, it seems like there is like a general feeling that we can do Bellatrix earlier than may met,  the TTD on maintenance. I would move this conversation to the cl call next week, just to sure that like, we have all the seal teams timing in. and, and that is not on this call today, but I'll make sure to like also bring them up to speed on this. And,  so he's aware and we can kind of draft what that could look like. but either, yeah, just something like alongside the last test that, so that then when we moved to my net, we're just setting the TTB. We know Bellatrix has happened. And from users' perspectives, it's just like download a new ELL version and maybe the CLS have like slight improvements, but they should have like consensus changes. 

**Mikhail Kalinin**
* Yeah. We should also consider that once three weeks happens, then cl will start querying ELL, or at least,for the exchange transition to immigration. And the PO is not upgraded. We'll start implanting it with messages in the logs. So,which should also consider that, 

**Tim Beiko**
* Oh, right.So if you're querying, if you're querying and ELL that doesn't have like the Paris code basically then as well, send weird log messages, is that yeah. 

**Mikhail Kalinin**
* Yeah. It will try to connect to engine API end points. So we we'll have to really spend as well y'all's should be upgraded as well. So that's going to Be little tricks happens. Yeah. 

**Tim Beiko**
* Okay. So we need to be at least aware that there's a thing called the N GPI, which only happens in like a specific release with like EIP 36 75. Is that correct? 

**Mikhail Kalinin**
* Right. It's it's basically Paris, right? So we'll have to release, we'll have to release carousel Patrick's probate at the same time. And yeah, the upgrade should happen.The upgrade to Paris should happen before the, for skates.The main that's 

**Micah Zoltu**
* I believe someone correct me if I'm wrong, but I believe if you took, the,client today, like the Robson clients, let's say whatever client you guys are using to test execution layer on Austin, that should work through may net, as long as you set up TTD override. Is that, is that correct? Assuming we don't have to change anything between now and then thanks. Let me know. Code changes. Like a person doesn't even need to upgrade their client from now until the merge. They just need stuff to TTD. Is that accurate? Assuming they're running a Robson client today, 

**Marius van der Wijden**
* Like they can just 

**Micah Zoltu**
* Switch it over to maintenance and they're good. 

**Marius van der Wijden**
* They need to change the chain config of course. But other than that, they can be in the same. 

**Micah Zoltu**
* There's the,  as a guest, not released one client with many chain configs and it's not just like dash dash config may net like it actually. Okay. Okay. Yeah. Let's see. So yeah, so, so in theory, we'll can upgrade today, like their whole setup. They can upgrade Paris Bellatrix clients today. And so again, assuming no changes, they're good to go for the merge. Is that more or less accurate? 

**Andrew Ashikhmin**
* Well, not Herrera gone because,  as discussed, we have only prepared another quality release. We were still making fixes and improvements for the merge. 

**Tim Beiko**
* Right. And I think to be clear, like with the CALS plan was we do this when we're doing like the last test. And so we would hope that by then clients have like releases that are very close, if not exactly the same that like we'll have made that. So we don't. Yeah. 

**Mikhail Kalinin**
* Yes. The plan is simple because,  we would, I don't think we would like to have,  B Bellatrix shed mule before,  the last,  desktop is upgraded and sometimes plus on top of this upgrade, right. To, give us time to react if anything goes wrong. 

**Tim Beiko**
* Yeah. I think that, that makes sense. Thinking like, Bellatrix happens like a few weeks a month after the last test, not how to upgrade basically. and it's, but it's scheduled and at the same time 

**Mikhail Kalinin**
Yes.And yeah. And goes right. And I've ever seen these. Okay. We just don't need to cut new related. 

**Tim Beiko**
* Yeah. I think I suspect that the practice, some clients might choose to cut the new release with the updated TTD value. But, yeah, it's not like a strict requirement. Basically. 

**Mikhail Kalinin**
* I think that cluients should release,  their clients should be released with the Realty value, but users will have a choice of creating or overriding 

**Tim Beiko**
* All right.Then post, this has a comment that like the TTD override value isn't a required in the spec. So like, I guess in theory, like, you know, that this from a spec perspective, like the client releases are the way that this happens and then, but yeah, we, we would just probably list both. And if some clients just does one or the other, we could just highlight that it's not the end of the world. So I guess just to like recap all this. So for Rob specifically, you know, clients are going to put out releases,  in, in the next,  days with the huge TTD value. If you've already downloaded a client's release, by the way, that has rusted TTD support for like the value we hit yesterday, you do need to upgrade,  your TTD value to the new,the new one.we'll have an announcement that, basically we'll have an announcement about the new re-ups clients early next week, which will have this pretty high TTV hard-coded in it. And then once Bellatrix has happened,  on June 2nd, we'll, we'll choose,I guess, realistic TTD number,that will confirm on June 3rd, we will probably choose that to happen, like in, in theory 10 or so days from then, but then we'll try and add some hash rate for it to happen around June 8th.but that's like very rough,targets. We can't really guarantee that, does that generally makes sense that people for Ropsten.Okay. And then for me, NetApp will confirm this on, on the,cl call next week.but the rough idea would be that when we have the triage releases go out for suppose,  which we expected to be like,  quite final, we would also then set,  slot height, or slot for epoch. I'm not sure what the right term is for the seal side.  but basically we would set the, the epoch slot number on the beacon, Shane, where Bella trick happens on main net. meaning that then,  once that has happened, we can just choose a TTD value.  that's like a couple of weeks away and all users will have to do that is updates,  either update their clients or to the override flag to have the right value for minutes. does anyone have like strong objections, product Potuz, what do you mean about JWT stuff? 

**potuz**
* So the engine is supposed to be a secure connection.I'm not really,I'm not really following how it is, but I, I thought that, clients haven't,  execution clients are, are not really finished with that. So I'm not sure if they're actually enforcing that it's authenticated. So I'm just wondering whether or not having this finished before we set up a development for apple is a requirement or not. 

**Micah Zoltu**
* Yes. 

**Marius van der Wijden**
* So, so for geth, we have the authentication,  finished and required and on 8551, you can optionally enable the engine,  API on,  the default HTTP port. So 8545 without authentication.if you want to test something, the only issue is that if you don't,if we don't specify the, if you don't have a TTD specified,the authenticated part will not be opened. And this is something that we're thinking about changing, that we have the authenticated,port open by default, even with our TTD specified so that you can test so that you can test,your stuff without having to specify to GG. 

**Marek Moraczynski**
* We might, we also implemented authentication and we are working in this way that,  if we specify a part in any,in any board,we will authenticate it if we add engine API, but,  we need to explicitly, side that the port is not authenticated. 

**Tim Beiko**
* Thanks, Besu & Aragon. I'm curious what this is. 

**Gary Schulte**
* Yeah. basically we implemented jot authentication. We,  we actually have a flag that,  can enable or disable jot authentication the on the engine API.  currently the default is set to,  disabled for test purposes, but pretty soon probably next release. We're going to flip that flag to make a default on and you'll have to explicitly disable it. 

**Tim Beiko**
* Got it. Thanks. 

**Andrew Ashikhmin**
* In Aragon, we have implemented the JVWT authentication, and moreover we have removed to the authenticated for, to complete it. That's only possible with authentication. 

**Tim Beiko**
* So it seems from the EL side that keeps we're good. I do think that we should not be forking the last test until it's like implemented across, like, it should be the default behavior across every client. but assuming that it is that it means that we can, obviously, this is not a problem to schedule Bellatrix on May 9th as well. Does that make sense? Okay. anything else just regarding ROPs and like this kind of PTD Bellatrix timing. Okay. If not, I think the next thing I want to chat about is like the beacon chain. So the, the actual first problem we hit on Robson was not this Bellatrix scheduling, but it was like the beacon chain did not even exist.  which obviously is not the case on the Ethereum main net. so what are people's thoughts about like when and how we should launch this, the Sepolia beacon chain to make sure that we don't hit, a similar, similar issue,  on when we read you should Sepolia, 

**Micah Zoltu**
* What are the constraints that prevent us from releasing disbelief beacon chain like right now?Like, what's, what's the thing that's holding us back. 

**Tim Beiko**
* Perry, 

**pari**
* There's nothing holding us back. We could, we could launch one next week if we want, it's just a bit of coordination. That's all. 

**Micah Zoltu**
* Yeah. I feel like we should just do that then. If, if there's nothing actually preventing us from doing it soon, we should just focus on doing an explanation and making it happen. So we don't have to worry about it later. 

**pari**
* Okay. should we just launch it and leave the Bellatrix information on set? So when we then decide that at the future call, 

**Tim Beiko**
* I think, yeah, go ahead. 

**Micah Zoltu**
* My personal preference, and this is as not a client developer, so I could be totally wrong on this would just be so with the execution clients, you can set them so that like with Genesis, they already have a bunch of forks set, like right at justice block. Is there a reason we can't just launch, the beacon chain with Bellatrix already live from day one, just with a TTD of infinite, like the Bellatrix code is ready, but the TDD is far in the future, 

**Pari**
* But we can also do that.we, I think there's some clients that don't allow you to set it to happen at Genesis, but it can happen at, which isn't that different six, six minutes later. but yeah, we can do that and just set TTD to be insanely high. And at some point to stop hit the key value, if that's the approach we want to go 

**Micah Zoltu**
* That's my vote.

**Tim Beiko**
* Yeah, I think they're their arguments towards not having Bellatrix at first is like, it mirrors more what we have on mainnet. So like the current or the current beacon chain that basically has,  Altair activated, but not Bellatrix. so I can see an argument that like we would,yeah,I could see an argument that like, we would want to maybe replicate the main net conditions. 

**Micah Zoltu**
* But it's not like a super strong And maybe we just at least have it. So we have, Genesis and then reach finale. 

**Tim Beiko**
* Coordination things you want to test for Bellatrix right. Like that there might be value in selling Bellatrix at a future date so that we can like do something with it. but yeah, I don't see any views against like doing Genesis and the Altair. I guess the one thing I would maybe say, oh, sorry, Perry, you were gonna say something yeah. 

**pari**
* I agreee With the two on that take, we can have Genesis and not Altair and just leave Bellatrix as it is, because we still haven't reached a final decision on how we're going to handle mainnet. And once we know how we're going to do it on main that we can then replicate the same thing on Sepolia. 

**Tim Beiko**
* Okay. And my final question. Oh yeah.

**Mikhail Kalinin**
* No, it was just, yeah, I was just going to say the same thing. 

**Tim Beiko**
* Okay. Yeah. Sorry. My last point was just, is this just something we want to check on the cl call with the cl teams as well? Cause like they run the software for that. there's no rush to do it like this week versus next week. We just want to do it like well before it's the Sepolia forks. so is it worth just like Saturday checking this on the cl caller? a week from now? 

**Micah Zoltu**
* I personally see no problem with, Perry launching the Sepolia beacon chain over the weekend on its own. 

**Tim Beiko**
* I guess. I dunno. There are some cl folks here. How do y'all feel about this? 

**Micah Zoltu**
* I don't actually, 

**pari**
* Again, I think since it takes a little time to actually set one up, we can just wait until the next week. I think the one week defense is not going to make a change. We're not going to multiply the next week or the week after anyway. 

**Tim Beiko**
* Okay.oh messy  from Lodestar. Sorry I before. okay. Sounds good. So what we'll, we'll cover that as well next week,  on the cl call, but basically it seems like at least for the outside, we have agreement that we want to launch it as soon as possible. Run it through Altair and then wait a bit to figure out what to do for Bellatrix.anything else answer.

**Micah Zoltu**
* Quick question about Bellatrix just for my own edification and others listening, does Bellatrix contain any consensus changes that happened before TTB or is it just code that all activates on TTD? Like is there a 

**Mikhail Kalinin**
* That's consensus just to test interesting. Yes. It has changed since the book part is structured ways that,Okay, so there is sorry, 

**Micah Zoltu**
* Go ahead.I think I'm liking, so go ahead. 

**Mikhail Kalinin**
* Yeah, it's just, it, it monitors for execution. Bailouts would be non-zero and it's also looks for ELL to add square, whether it be block the terminal, a terminal block exists, but yeah, that's what it is. 

**Micah Zoltu**
* So, so if you have two clients and they do, they need to coordinate when Bellatrix happens prior to TTB, like is there a Bellatrix hard fork on the consensus layer that happens. And then at some point later TDD hits and then more changes occur or is it just, you know, you to play your clients whenever, as long as they're before TTD and it doesn't matter when, before TTD, TTD, like, is there actually wire protocol changes that will cause clients to get disconnected from the network, if they are not on Bellatrix while their peers are on Bellatrix 

**stokes**
* Yeah, it Hits,They all need to change it, the fork, and then they wait until TTD 

**Micah Zoltu**
* Number based. 

**Micah Zoltu**
* Gotcha. Okay. 

**Tim Beiko**
* Does that answer your question? 

**Micah Zoltu**
* Yes. Yes. 

**Tim Beiko**
* Okay. There's one more question about the chat it's basically,in the days before we published our options to D B, are we confident that enough of the nodes running on Ropsten will switch your configurations to prevent the long running proof of work for? I think this is hard because it's like mining Broxton is like not economically rational in a way. So like the people who minded might keep mining yet. I, I do think we can probably get like infrastructure providers and like,  basically kind of all the, the, the like large kind of tooling and projects that people depend up upon the like, updates. So that like, from an end users perspective, sending your transactions, like your transaction ends up on the Ropsten for good steak for,only, you know, even if it's only been like a few days, but, I don't, like, I will have some people standing on the wrong side for ups then. Cause like they missed the announcement. I don't know.I don't know how much more we can do for that then like how valuable it is. Like if you're just still running on your Ropsten proof of work for, cause you didn't read the memo until two weeks later, like how, how bad that is basically. yeah, I don't know that people have thoughts on that. 

**pari**
* I guess my main top there is we have been saying for awhile and props and will it be picketed and the only reason we're going through all of this effort to make it nice is for the people who want to test the most through it. So if anyone's not interested in testing the most and we don't have to really worry about them because it's an application network from their perspective. 

**Tim Beiko**
* Yeah. I think that makes sense. I, I guess how many nodes are actively involved? It's hard to know from a notes perspective. I think we can generally be reached like most infrastructure and tooling link providers quite easily on quite short notice. and especially like, I think all of them are following Ropsten now because of like issues we saw yesterday. So, I think it's, it's kind of care to people that something is happening on Ropsten, but, the long tail of people is just really hard. I, I, I don't know of a good way to do it beyond this, having many announcements. And, and that's also, I think, I guess the cost of getting it wrong is quite low. If you're just a random person running the node. And at some point you realize you're off the wrong chain and you kind of do a Google search and see that there was an upgrade on Robson. yeah. Does that make sense? Okay, cool. okay. Anything else on like there Robson beacon chains, if not, we also have,Gordy on the agenda, but I, I don't think that we've had any updates there. I dunno. Affray did you have anything you wanted to cover about Gordy specifically? 

**Afri**
* No. It's just wanted to say that fairly easy to,  come up with a total,  difficulty at a certain date because the total difficulty per block was fairly stable on girly. And whenever we come up with a date fairly easy to come up with a number, so I'm basically just waiting for, come up with the date so we can do some nice pseudo palindromes. 

**Tim Beiko**
* I know that. yeah. And I saw you registered a bunch of validators as well.  I believe for Gordy current Gordy signers. Is that right? 

**Afri**
* Yeah. I'm prepared my sign-up to also validate products or I'm on both sides of so much. 

**Tim Beiko**
* Okay. anything else just on testnet that's generally, if not, there was an engine API PR,  that Danny wanted to bring up, but any do not make the call. I don't know if anyone else had context on this. basically adding the get payload bodies by range,  par to the, to the engine API. Nicole, I saw you, you chimed in on this as well. 

**Mikhail Kalinin**
* Yeah, I can quickly describe the idea is so.So yeah, so there are two methods instead of just request and failed bias, which is a list of transactions just by hashes. There is another one,  by,bodies by range,  which, which,means that,the red suit parameters, they start renter in the number of beta to which bodies sorry, requested, from the ELL. And,  ELL is, it is optional for ELL clients to support by wrench requests.  and these wire requests is,about to leverage the leading air storage's, which are,and,and make this kind of optimal queries, over linear searches, which is not the case where a lot is by hash. And if, yeah, if, if by ranch is not supported, there is a error code. you know, Ms. PR and cl should fall back by hash, which,which is basically,called bodies by root. But yeah, I'm calling it bodies by hash because there is no roots.there is no root notion on the L side.So that's basically the idea of this proposal. 

**Marius van der Wijden**
* I'm just skimming through it. Why should we return? Like, if the middling block hash is missing and we don't have it by, where should we return the, why should we not return anything? Or why should we not return just nil, but just cut it out. I think my, like, my intuition would be if you have a, if you're requesting and, and blocks you're getting and responses, and some of the responses might be, no, 

**Mikhail Kalinin**
* I think it's better to address why PR comments. 

**Tim Beiko**
* Okay. So, yeah, I guess if y'all kind of want to chime in on this,  in the next couple of weeks, yeah, that'd be good. 

**tukasz Rozmej**
* This proposal is before the magical science or what's, what's the timelines here and why is needed 

**Mikhail Kalinin**
* If needed because,  cl clients like to do duplicate, like basically removed by this, these bodies from,  ELL,  execution bodies from their searches, which will reviews significantly at the space used. And,  I'm not, I don't think it should happen like right. That the merge, so it can be a soft work, I guess, 

**Tim Beiko**
* Does it required to be activated as a four.Like, yeah, I suspect though.

**Potuz**
* But I would like to say something about this week, we have this feature ready and we decided not to ship this release candidate with it because it may affect Robsten, but it rubs in, goes fine. We're gonna, we're gonna release it and start testing it live. I think it's actually the other way around. We would want this to be ready before the merge, because otherwise it would mean a database migration for us, for everyone. So it would be much better for all of us to actually have this before the merge,  and then don't force our users to migrate or rethink their clients. 

**Mikhail Kalinin**
* Oh, you mean, so this schema will be changed on your end. 

**Potuz**
* Yeah. So the, the, the way this works is you just don't, you don't say the bodies, and then you just request the bodies from the execution layer. If they asked you if they ask you for blocks, 

**Tim Beiko**
* Andrew. 

**Andrew Ashikhmin**
* Well, I think if we're required before the merge, then it will delay the merge because we haven't implemented it yet. So I will do it after ther merge

**Marius van der Wijden**
* I agree. 

**Mikhail Kalinin**
* Yeah. I agree. by the way, what do you use for this feature on the El side? There is no map, this kind of math that's implemented yet. Are you using Eth get blocked by hash? 

**Potuz**
* I believe so. So roll is not here in this call is the one that implemented it, but I believe, so I think is the cause is calling block by block, 

**terrence(prysmaticlabs)**
* Right.So we do have this feature implemented today. It is war. It is under test right now. So, but then he, I think, I think the API itself is a nice to have, but it's not a mandatory type by type of thing. Yeah. 

**Mikhail Kalinin**
* Yeah, I'm not sure if it's going to be safe to use these methods because you will have to compress blocks block by block. I mean, how much stress it will make on ELL clients, if it's both work sweet. 

**Micah Zoltu**
* So, similar to how we have versioning for the peer to peer layer, it feels like we're probably going to want the versioning for this. and has that been for this engine API, since it is a critical part of the infrastructure, has that been thought about or explored or already solved? 

**Mikhail Kalinin**
* We,  we decided to have like conversions,  since there are, there is, there are not many methods in there, but decided to have a version by a method, like version the entire namespace. And that's what is stated in this card. So if you update the methods or send the semantics or blocks or a structure structures, data structures, so you just like upgrade one method, sense tense version to the end. 

**Micah Zoltu**
* And if there's a new method, do you just probe it and see if you get a method not found back? 

**Mikhail Kalinin**
* Yeah, that's interesting. Yeah. I was also a bit thinking about it. How do we want to like say, okay, so this is Shanghai, this is the methods that we use for Shanghai and the versions that we use pushing high. And this is like the next release. How do we want the scope without as well?Yeah, that's a good point and question to think about, 

**Micah Zoltu**
* I feel like now that we're closing in on the merge, we should probably put deep thought into like what that whole story looks like in terms of like, how do we add methods, how to remove methods, how do we upgrade? That sounds like the upgrade methods part is kind of solved with method versioning, but we still need to deal with new methods and deprecated methods between layers. We don't have to do this on this call, but we should probably talk about that before the merge happens or at least before the first. 

**Tim Beiko**
* Yeah. Yeah, I think that, that makes sense. and just to wrap up on this specific call, I think it's pretty clear from ELL teams that we don't want to have this be requirements for the merge, obviously, especially if CLS can, kind of pack,  this functionality by just calling every single block by hash. but yeah, it would be good to just have some comments on the spec so that.  yeah, the general API makes sense.  but we're not planning to implement this before the merge. Does that make sense to everyone? Okay. okay. So the last thing I had on the merge,  Fred's was basically following up on the difficulty bomb, but, so, I checked earlier this week and I think our average block times are like at 13.7 ish, seconds.there was an update that like TJ Rush's chart posted a couple of days ago, which shows that like clearly, you know, there is seven packs from the bomb it's still kind of quite mild. but,  obviously these states kind of get,exponentially worse every,about a hundred thousand blocks. and I think last, yeah. Okay. So there is like a, another prediction on this, on this thread,  which roughly targets that like around August is when we would hit 20, this check-in blocks,that July, we would probably like second half of July, we would be around like 18 ish seconds.And like second half of June, the first half of July, we'd probably be around like 16 and a half second blocks. and then,  like very late August, early September, we'd be back to like 25 plus second blocks. I know there was like some conversation on the discord about this,  this week.  I know Thomas, you had to try about this on Twitter yesterday. but I'm curious to just hear from different time teams generally. Like where do people stand regarding the bomb? yeah, Thomas, you have your hand up, so go for it. 

**Tomasz Stanczak**
* Yeah. What ideally propose to agree today, if possible for the bomb delay by three or four months and just set the date when we introduced that to the clients. 

**Tim Beiko**
* Okay. anyone else have thoughts on this, Ben? 

**Ben Edgington**
* I, I don't want to advocate for moving the bomb because, I just want to keep the pressure up to get this thing done. However, if we are doing Paris, early, along with Bellatrix, that does give an opportunity without a separate hard fork to,  set back the bond by a small amount three, four months, I think is, is,  giving ourselves too much of an ounce. And I think we need to get the pressure on, but a couple of weeks,  at least take the heat off the block time on, our main net. 

**Tim Beiko**
* That's Andrew you're on  mute. 

**Andrew Ashikhmin**
* Oh, sorry.  sorry, Thomas. I think we should delay the bomb by three or four months and,  just to do it. And,  if the merge happens earlier than then, great, because we, we shouldn't like put pressure for the sake of pressure we should,test it thoroughly. It's a big change. The sound sound pressure is good, but not too much. Like, yeah. I would say 3-4 months. And it doesn't mean that the merge is delayed by that much long. 

**Tim Beiko**
* Got it. Anyone else have thoughts? 

**Peter Szilagyi**
* I mean, what isn't done yet for the merge 

**Tim Beiko**
*That deployment rollout has been bumpy. 

**Peter Szilagyi**
* But I mean, talk to them, it was pretty clear that there's going to be a messy situation since it can be attacked in both ways, but,I guess that's kind of on us for not launching the weekend chain before setting the TTD. 

**Tim Beiko**
* Right. I'm curious. The other thing I, though that we had,  discussed,  beyond. So like I don't Aragon mentioned that like they're buddies,they have eruptions and alpha, but I think the other big thing that we wanted to look at for this,  like hive test coverage, I know Kelly's been spending a bunch of time on that. 

**Mikhail Kalinin**
* Yeah. myself and area and yeah, they're in mirrors working on this coverage. And I think we, we have a pretty good progress on that. And from that perspective, I can say that we will not be ready by,  by like,  before four can DeLoss testnet. So it's like, I got to say that it's like definitely a no goer or a stopper. Like, that's the perspective I, you can do this. And I would not,like the way the bomb, just because of what happens with Robsten.  we're still planning to have an upgrade on June 8th as book plan before. And I don't think it should be like in how, linked to,or in how the reasoning behind like, related to fall. I'm not saying that we should not like,push, push back the ball. So,but yeah,what happened with Robson is not a reason for doing this as, from my perspective, 

**Tim Beiko**
* Thomas. 

**Tomasz Stanczak**
* Yeah. So always in favor of bomb being in. And,  actually I think it works and I always loved it. I felt that it was keeping us having to push to be ready for the, for the releases on may not always know how to preach the release if it was,  starting to extend the block time. So I think it's already hitting in. We know that it will be laying the blocks. It's actually some significant effect on the network. I think the pressure is,  is there like a, an office building only, talking about that in mind.So I felt that there's enough pressure to keep the thing going,feels like it's a bit too much pressure,to your like, desk, to all the desks. Let's one after another,get the feedback configurations, proper retesting with all the combinations, sync times,coordination of infra now,with Rob Stan, with Tim or desk, that's where some additional education and just saying, this is a stable version,we not touching it.I simply think that it will take time to do that properly and we already are in that place. So if we delay bomb by months,  it will keep the pressure and the level where it will give the pressure to the most likely time when the main net only emerged and it's not affected by the Robson at all. So was, I was thinking on this three months delay for a long time, that it's the most likely thing to happen. It's just now I think it's a good time to raise it. And because it starts to be actually like light. If we, if we decide in two weeks and we say did, then we added to the clients and do a three weeks after decision because we need to prepare to release.This was not,it will be four or five weeks from now when we were delighted a bump. And, you know, there's also additional hostile to, to prepare to release for the bump delay.so we don't want to rush it.We don't want to do that every two weeks by two weeks. * Like then we would have to do that every single quarter. 

**Tukasz Rozmej**
 * The comment maybe on, on Peter, that's my opinion a bit, what shows the readiness are hive tests. And so it's like I'm happy bus instead of what we are mostly testing in shadow forks. so yeah, looking at hypothesis,this, every client has multiple tests failing and, maybe we'll be able to fix those issues, before, before remerge, but there are just, this generates more pressure. 

**Tim Beiko**
* Anyone else have thoughts on this 

**Mikhail Kalinin**
* Who do have a time to wait at least a deal with grade and drops in and how it goes eventually before we make a decision. 

**Tim Beiko**
* Right? Like, and, and I think, you know, one thing,for sure is I would like us, I don't think we can really make a decision today, given there's like no EIP, there's no like actual proposal for people to review. It does seem that like the people who, who wanted to lay the bomb, like it's three, four months delay is like, what, what seems to be like,propose. so just to put this in perspective, it means that like, we're basically in June now, that like three months from now would be July, August, September.So it's like on September 1st, we'd be like in the same spot as we are today. basically where like blocks are starting to slow, but there's, you know, from an end user perspective, it's still doesn't make like a noticeable difference. so yeah, we'd be like roughly at that stage in September.and yeah,I guess, yeah,this is like a bunch of conversation in the, in the chat about,  about your, your point around big blocks.Do you want to take like a few seconds to just kind of tell people about your concerns there? 

**Potuz**
* Hi, I'm just worried that,  it's not something that we have been actively testing.the consensus layer is very, very sensitive to timing issues.If we get large blogs that take long to execute,would make, would affect at the stations would affect which notes, the way notes are syncing notes that are, that get these blogs close to the fork would stop sinking for a little bit until the engine catches up.if we see this situation with forks, for example, would make me very,very worried at the time of the fork and I would want to test it.so I, I actually suspect that not delaying the bomb would actually delay the merge. 
* Can you just have, the comment maybe on long Peter that's my opinion a bit, what shows the readiness, our hive tests. And so like I'm happy bus instead of what we are mostly testing in shadow forks. so yeah, looking at this, every client has multiple desks failing and, maybe we'll be able to fix those issues, before, before remerge, but there just, just generates more pressure. 

**Tim Beiko**
* Anyone else have thoughts on this 

* Who do have a time to wait at least a grade and drops in how it goes eventually before we make a decision. Right. Like, and, and I think, you know, one thing,  for sure is I would like us, I don't think we can really make a decision today, given there's like no EIP, there's no like actual proposal for people to review. It does seem that like the people who, who want to delay the bomb, like it's three, four months delay is like, what, what seems to be like,  propose. so just to put this in perspective, it means that like, we're basically in June now, that like three months from now, it would be July, August, September. So it's like on September 1st, we'd be like in the same spot as we are today. basically where like blocks are starting to slow, but there's, you know, from an end user perspective, it's still doesn't make like a noticeable difference. so yeah, we'd be like roughly at that stage in September. and yeah, I guess, yeah, this is like a bunch of conversation in the, in the chat about,  about your, your point around big blocks. Do you want to take like a few seconds to just kind of tell people here about your concerns there? 

**Potuz**
* I'm just worried that,  it's not something that we have been actively testing.  the consensus layer is very, very sensitive to timing issues. If we get large blogs that take long to execute,  would make, would affect at the stations would affect which notes, the way notes are sinking notes that are, that get these blogs close to the fork would stop sinking for little bit until the engine catches up.  if we see this situation with forks, for example, would make me very, very worried at the time of the pork and I would want to test it.  so I actually suspect that not delaying the bomb would actually delay the merge because we want to test this. 

**Tim Beiko**
* So what I guess, what I don't understand is why do you assume the blocks themselves would be bigger? basically, are you assuming that like people would raise the gas limit? They're like, why? Cause like the bottoms just means the blocks are more infrequent, but it doesn't change. 

**Potuz**
* What's the reply. This is the reply of the bunch of people arguing that we should,raise the gas limit at the same time to account for,the block being later. 

**Tim Beiko**
* Right. Okay. Yeah. So basically that if it's like, people are unhappy because like, say there's 22nd block times, then they decide to like raise the gasoline at 50% because,they, they get like roughly the same throughput, then you get much bigger blocks. Right. 

**Potuz**
* But yeah,So I think the timing difference by itself is if the blocks stay small enough and they just are delayed between the timing between themselves is not the same as the slot time that we have. Now, this, this is not an issue. This at the very worst can affect, like eat one voting. But,  I think we've tested this already. 

**Tim Beiko**
* Okay. Got it. anyone else just comments they wanted to make about this? Okay. Maybe one more thing I'll pick on from the chat,  Marius, you mentioned that like you think it's actually too early to discuss the bomb pushback. Like there's like kind of the opposite of what Thomas was saying.So yeah, if you want to elaborate on that a bit, 

**Marius van der Wijden**
* I'm not really, no,I think,there, there have been a bunch of great arguments for doing it now and there have been a bunch of ones for not doing it now. I, I really want to avoid us having to push back the bomb twice. I think that that is the, the worst thing that we can do. I think pushing back the bomb once already is really bad because we have to,  update, like we have to schedule another folk and it's not about the scheduling. It's not about the,  it's both the coordination of the, of the, of the community. And I think we might lose some people if we schedule another,  delay,BombBomb pushback. I think it's like, it's fine to do it on a, on a technical merit, but I'm not seeing a technical merit at the moment.and I think teams should really, really strive to hit the timelines and it's, yeah, it would be really good for you guys too, for us to, hit the timelines that we set ourselves.That's that's all I can say. 

**Tim Beiko**
* Okay. So, and then, yeah, there's another comment to the chapter about like combining this with Paris, realistically, you know, Paris is only going to happen after like the other testsnet that have happened,  maybe like roughly around the same time as to Sepolia. so like, you know, there's no world in which like, this is less than like a month or a month and a half away,  which would be like a mid July ish, which is,  somewhere between like 16 and 18 seconds block times if this chart this correct. It gets very hard to predict,once the bomb actually goes in. but like for the people who like wants to delay the bomb, this does that like generally make sense as a timeline, like where we make the decision about like, including at the Paris, but there's, if, if we got to do that, that means we, for sure we'll hit that the 16, probably 18, second block times.Thomas, 

**Tomasz Stanczak**
* So I'm looking at the charts that was,  those include it as a block time prediction,  by kg from 24th of May. And it's attached to the discussion already today. And I think we're planning now the merge for August, right? This is the optimistic scenario doubts.probably the biggest optimist optimists we're talking about August.And this chart is showing like 25 seconds towards the end of August. Right. So is everyone happy with a we've going towards 25 seconds box.

**Andrew Ashikhmin**
* Yeah, I think that's the big problem because,  we are artificially reducing,  the,  the capacity of the network and they said this service to the users,   I was also thinking like, maybe we can combine the notch delay with something useful, like,  because there's, this idea was surface that we said that the TTD for the main actor, something artificially large, and maybe you can do that alongside,  delaying the bomb. So it's kind of not our final minutes release or south semifinal and the notch itself is not happening yet, but we are doing something useful for the merge along with, 

**Tim Beiko**
* Right.Yeah. And that's kind of what I was suggesting is I think if, if we were to do that, we would still hit at least 16, if not like likely 18 ish, second blocks by the time the competence. so it's not like,  it's not,  25 seconds obviously, but, yeah, it,it does mean that like we do hit, 

**Andrew Ashikhmin**
* Which is already bad enough, like, like we should try to improve the capacity rather than 

**Tim Beiko**
* Yeah.Thomas

**Tomasz Stanczak**
* So better. We definitely wants to push the merge at the time when the network has stable, predictable, or people think that's okay if the merge changes by one or two days that we don't have to rush it when people will not be in the last week taking crash decisions. Because if they may say then suddenly it's 30 or 45 seconds, and it's already that causing a turmoil with what miners do. So if at the same time, as we introduced merge minors, skip voting the changes on the block sizes on the block times change. That's just a lot of additional, additional variables to take into account when calculating, when, when filling cow, how we blond. So I simply want to operate in the conditions where network is very predictable and just not additional pressure,from different sources about how we should act. 

**Tim Beiko**
* Right.  okay. And Marius, I think you had like other comments, 

**Marius van der Wijden**
* That didn't scar. I, I don't, I don't think 22nd block times are bad. And,  in Amsterdam, we, we kinda made the, like, had the overall view that,  degradated, user experience for two months is worth it. If we can shift the much faster. yeah, I think we're were looking at like, I don't know, 5, 7, 10 years, of like things. And so I don't, I don't see the point in focusing on two months of,  of,  like slightly higher block times. 

**Ansgar Dietrichs**
* Yeah, I was just curious if someone could put like a specific number of like a day or something on the delay that,  in like an additional folklore for difficulty from today, what mean? Because, I mean, I know Maria said earlier that like having, I think having more than one delay would be the worst case. I'm just wondering what, why, why they would be the case. Why can't we just have a really small delay, and then potentially have another one later if it's, unless it's like a big, big, extra that's. 

**Tim Beiko**
* Yeah, 

**Andrew Ashikhmin**
* I think, well, I think like small delay, the problem is that,  we don't want to delay it too often. Like delay it by two weeks, then we decide, oh, no two weeks is not enough. Then delay by two weeks again. And then so on that, it's kind of wasteful.  and to,  Tamara's point I disagree, I think, well, like how our priorities should be certain the users of the network,  and the nudge is on their means to that end.  and to my, to my mind, if,  like what, what's the downside of a delay in the nurse chief,  we keep paying the minus. It's not a big deal. It's much, much better than hurting their users in my thing. 

**Tim Beiko**
* Thomas, 

**Tomasz Stanczak**
* One thing that I wouldn't agree with as operating under assumption that not, not delaying the bomb speeds up to delivery.  so,  I just see all the engineers working gets and the limits now. So, you know, it starts starting productivity. So I don't, I don't think delaying the bomb is actually speeding. Sorry, not delaying the bump. It's spinning things up that, that people will magically generate additional firepower to, to heat those times. 

**Tim Beiko**
* Peter. 

**Peter Szilagyi**
* Okay. All right. But I think we're kind of debating to fairly far out the extremes.One of one is not delaying at all the bomb. The other is late like four months, which some people find excessive,  would the middle ground work, for example, what would happen if we were to delay the difficulty bomb by say two months that would maybe relieve the pressure of getting to 22nd lock times.  and we would not have to bear the burden from the community that they're starting to use. Yeah, we will just lose the, the timeline completely.So is there a specific reason why we would like to push it by four months instead of just giving, just pushing it by little to leave breathing? Obviously two weeks is pointless, but let's say I don't want two months.That's 

**Tim Beiko**
* Yeah, Andrew

**Andrew Ashikhmin**
* It sounds well to my mind, two months is reasonable. Two months is kind of a good enough time that,  to help us,  go through the testing thoroughly and,improve and grow the quality. So I would be happy with two months. 

**Tomasz Stanczak**
* My suggestion on freeform months was based on the calculations based on the schedule and assumptions around,  two months of the, of operating with the frozen code. My preparation for me not and communication with the, with the community about like the details and confirming, like what's the adoption,adoption percentage of all the new clients on both sides and so on and so on. but don't take it as a, like something that I say under 3 month or nothing, as definitely just a suggestion that I believe that three or four months as the most likely effective,delay, but yeah,I'm open to support any solution that will make us start preparing the IP and start preparing releases with the bomb, move, how exactly what, what's the exact number of blocks that we move it by. And this can be decided in the very last moment.So I want To start preparing. 

**Tim Beiko**
* Yeah,I think that, that makes sense. I guess, based on this, my, like my rough feeling is that if we were to delay it like two ish months delay, that's maybe coupled with Paris,in order to,  to like minimize the amount of client releases that go out. so it means, you know, it, this delay would, would happen like at the, towards the ends of the test nets would give us like some breathing room between the last test steps. 

**Marius van der Wijden**
* What, what, what does Paris, 

**Tim Beiko**
* So,basically if we do put 

**Tim Beiko**
* Release of, yeah, if we put out a release of,the consensus or the execution layer clients at that is, where we have like a radiator high TTD,at, around the same time as we plan,kind of the shank of the Shanghai, sorry, the Sepolia,Fork, so that we can hit Bellatrix on mainnets before,that's maybe like the right time to also have a bomb delayed,when we're releasing something that's like,basically we help to be stable, but,we also,need to run through Bellatrix before.So you can just have a hard fork with the bomb at the same time.yeah, that's kind of what I meant, 

**Peter Szilagyi**
* But I'm not really following what, so setting the DQB on mainnet and doesn't make it the hard fork. So as long as it doesn't hit, it's just completely irrelevant whether it's set or not. 

**Tim Beiko**
* So,Yes, correct. Yeah. So we send it to a really high, yeah, sorry, go ahead. 

**Marius van der Wijden**
* For the consensus layer and that's correct. 

**Tim Beiko**
* So It's like,So yes.Yeah. we need it, we discussed this like the first half of the call, but I think the idea is like, we need to put out a release,  or we would like to put out a release,  which activates the Bellatrix works on the consensus layer on main net, roughly around the same time. as we have the release for test nets, like the fork is activated at the same time, but ideally the same software. at that time it would be good if there are cl or sorry, ELL client releases, which also have the merge changes that are ready, even though they're not activated. And so what I was proposing is that this same kind of release also contains like a bomb pushback with a hard fork,in parallel basically. 

**Peter Szilagyi**
* Yeah, but what does, why does it make this Paris or, I mean, 

**Tim Beiko**
* Yeah, cause the CLLs need to know that they need to be able to query a version of the ER client, which like knows that the engine API exists. And so that's what I'm calling Paris. Yeah. 

**Andrew Ashikhmin**
* And it also may contain this fork next value for,  we can actually set it to something realistic for the marriage as a means to, and that will actually be part of the, like, you can think of it as a hard fork, so will 

**Peter Szilagyi**
* No actually do that because if we get to that before the TTB took us or may not perform 

**Tim Beiko**
* Yes.So we're, we're already over time. I do think like, obviously we're not going to make a decision about this today.I think someone who feels strongly the lane, the bond should try and draft together and EIP that we can maybe discuss on the next call a bit more. yeah. And,I'm happy to like help put you in touch with previous bonm delay, EIP authors, if someone wants to once the draft test. and I think in parallel is just where thinking about like, what's the duration of that would look like,you know,what are the right parts of the process to couple it with,but clearly we're not going to resolve this in like a minute and a half on this call. 

**Micah Zoltu**
* Real quick clarification question. When you say two months, two months, from what two months from the time we released this patch, or two months from today, or two months from the plans, maintenance, TTD, 

**Tomasz Stanczak**
* It was worth the box.So you're adding that two months for four blocks.So around 400,000 blocks, 

**Micah Zoltu**
* Oh, onto the,  TDD calculus, or, sorry, not 

**Tim Beiko**
* Onto the bomb

**Micah Zoltu**
* Calculation From the previous 

**Micah Zoltu**
* Two months from the original bomb timer. 

**Tim Beiko**
* So two months, that means that like two months from now. So now we're say we're probably for June today, that means that in July and beginning of August, you started having like 13.7 ish block times rather than having them right now. yeah. So if you, if you read the EIP is like a pretty simple EIP, right? You literally take the number that's in the last CIP and you add two months worth of blocks at like a 13, second average to it. Okay. We're already five minutes over, but I said we would stay five minutes over in the chat for the two people who had EIP updates. So if y'all can, there would be another five minutes. I think we can cover those. And,  hopefully you have like a specific bond BIP to discuss on the next call. George, you had an update on 48, 44 with some optimizations for the transaction full 

**George kadianakis**
* Hey team.So I feel a bit weird doing these like sharding, discussion after we very important like merge thing.But anyway, since,I'm supposed to talk about the EIP, I'll give it like a very sort of update.  the idea is that we want to do at some point after the merge happens. we are gonna introduce blobs into transactions with the bank sharding.  we go through reports by Peter, I think in Amsterdam that,  the current approach of like verifying the blobs and the commitments and the transactions is pretty slow in terms like, you know, when you get a transaction and the mental, it, it's pretty slow to verify, and this might cause problems like POS and stuff. So, we are at PR which, makes this process of verifying,product dunk, sharding transactions,extremely much faster by,introducing case KCGS proofs,because before,like we were using KCGS just for building commitments for the roll-ups and stuff,we were not using case proofs anywhere in it.So by using case with KCGS proofs, we're able to like verify transactions much, much faster, like from 14 milliseconds per transactions, to like 2.5 milliseconds and the same for blobs. I'm not going to go into the math of how this works. I tried to write a pretty comprehensive how to on the PR, that requires a bit of knowledge about KCGS, but not too much.and yeah, this is like the summary.let me know if you have questions and maybe we can discuss it in the next day.Cindy,I don't want to take more of your time. Thank you. 

**Tim Beiko**
* Thank you.yeah, let me, I'll post a link to the draft PR if people want to have a look and leave some feedback there. and then, okay, last one.  Peter, oh, wait, sorry. I was muted on YouTube. Okay. So I just said I'm going to post the PR in the chat in case people want to give feedback on, on it. and then last thing,  we have Peter, who's been looking in to EIP 3537, 2537, which is,  this BLS pre-compiled the IP that has long been kind of,pending. and he was also interested in, in trying to revive that and look for the current statuses.Peter, do you wanna give us a quick update? 

**Peter Chunchi Liu**
* Yeah. Thank you, Tim. Yeah.cause we're all the time and I'll be as quick as possible and,quite kind of concise. So like a scheme says, yeah,IP 2537 enables a pairing operations in the new,pre compiles.it's just a quick reminder that,  we are only one step away from the activation of this wonderful EIP. So this, you know, activating this EIP could unlock, you know, a lot of new use cases on top of Ethereum ecosystem. So the summary is that the implementation of P 2537 and is actuary completed,it's in the code base right now.It's actually only the pending activation of this functionality.And,it's, it's not really that hard. And,the activation of this, functionality,actually just,enable the pre compiles by,editing the core,slash VM slash contracts dot go file.So just so, enabled this, just like what we have done for the bison team, Eastern bull Berlin,  and, although, maybe there's another point to mention, but there could exist in other, you know,implementation that is,you know, slightly more performance,  regarding to gas consumption, running time compared to this existing implementation.But, you know, as this work has been, you know, already done merging into the code base,I believe that, you know, we activate this POS,  existing,  2537 implementation and will be the best.  it's just a reminder to, to revive this thread to the community. Thanks. 

**Micah Zoltu**
* Yeah. Thanks.Is it only implemented? In,go through him or is it also in another Nethermind basically and Aragon? 

**Kelly**
* I know it's an at least,I believe another mind and one other have implemented it. I also know that Marius is starting some fuzzing work on,that set of pre compiles and GAF versus blast.And then also, you know, basically the everything that they used to clients are using. So there,I think there is still some active work going on with regards to security for the pre compiles and on the performance.I do think there is about a two X performance gain,with the other library.So obviously still a decision to be made about whether that's worth changes. 

**Marius van der Wijden**
* So we've been fuzzing, the collision,implementation against a Monarch,consensus Canark for half a year now.And,I'm currently adding beer list T to that thing and it's on August 1st, so should be pretty good. 

**Kelly**
* Fantastic. Yeah, it'd be LSD has been closed against, Relic and, some big numb libraries as well,in OSS funds for about a year as well. 

**Tim Beiko**
* Okay, cool. Yeah. Given where it's over, I think we can wrap up here. thanks a lot, everybody. And,yeah.Talk to you all next week on a consensus they have called two weeks from now,on this call,and don't forget to upgrade your Broxton nodes in the next few days. yeah. Thanks. 

**lightclient**
* Bye. Bye. 

------------------------------------------
## Attendees
* Tim Beiko
* Terence
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

---------------------------------------
## Next Meeting
June 10, 2022, 14:00 UTC

## Zoom Chat 
renton Van Epps:	what is this situation  
Ansgar Dietrichs:	if you need me to throw in "deflationary" at some point, lmk  
Ansgar Dietrichs:	“acd brought to you by raid shadow legends”  
Tim Beiko:	https://github.com/ethereum/pm/issues/528  
Tomasz Stańczak:	hello YouTube  
Tim Beiko:	https://notes.ethereum.org/@timbeiko/ropsten-ttd-override  
lightclient:	is my audio bad?  
lightclient:	or did tim break up?  
Micah Zoltu:	No worse than usual.  
lightclient:	good now  
Micah Zoltu:	Tim sounds normal to me.  
lightclient:	okay  
Łukasz Rozmej:	we can have reverse happen on mainnet?  
Micah Zoltu:	It can be delayed on mainnet.  
Micah Zoltu:	Accelerated is less likely.  
Tomasz Stańczak:	delay on mainnet would be too costly  
Tomasz Stańczak:	attacker would give away lots of monet to others so more hashrate would jump in to replace  
Potuz:	I think it would be easy for us to decide that ttd is ^0 if it' s not set  
stokes:	uint:max means no code change  
Micah Zoltu:	Scheduling Bellatrix before The Merge would make me happy.  
Potuz:	10^23 just for the record  
Ansgar Dietrichs:	Would it make sense for the EF to run GPU miners on the PoW testnets to create a difficulty floor? would limit the uncertainty factor  
lightclient:	alpha leak  
Micah Zoltu:	🤣  
lightclient:	"there are no airdrops" - yeah i've heard a lottt of projects say that ;)  
Micah Zoltu:	😆  
HP:	why can't you keep TTD at the unrealistically high value until the day you want the Merge to occur and then reduce it that day or the day before? This would eliminate the scenario where a miner brings on hash to bring TTD forward to the weekend.  
Tomasz Stańczak:	propagation of info to operators  
Justins iPhone:	It’s a race between trolls and upgrades  
Micah Zoltu:	I would argue for *at least* two weeks for mainnet.  
Marius van der Wijden:	Yay cut the releases on friday yolo :D  
Tim Beiko:	No need for a release :-)  
Potuz:	we can do a month without trouble, setting BELLATRIX_FORK_EPOCH early is not a problem for us  
Micah Zoltu:	Last testnet merged => Bellatrix on mainnet => mainnet TTD chosen => The Merge  
Potuz:	it is a requirement in the spec  
Potuz:	it' s not a requirement to have the flag  
pari:	fork epoch  
Potuz:	I wander if the status of jwt authentication won't be a problem if Bellatrix is schedule too early  
Micah Zoltu:	"You can enable it without auth if you don't like having money." -- Marius  
Mikhail Kalinin:	Bellatrix on Ropsten: Jun 02 23:00:00 GMT — I’ve double checked and I was mistaken by 1 hour  
Potuz:	SGTM  
Tim Beiko:	I guess it would have to be epoch 2 because of Altair?  
pari:	I learnt recently that you could even do altair & bellatrix at 1, haven't tested it but someone else did  
stokes:	you can set altair and bellatrix to same epoch i believe  
Marius van der Wijden:	I would say we should schedule genesis and altair now   
stokes:	that makes sense to me  
Marius van der Wijden:	And then set bellatrix maybe next week (or next month), but way earlier than TTD  
Marius van der Wijden:	*than setting TTD  
pari:	But yes, we will have a chain probably like a month before sepolia merges.  
stokes:	it all changes at the fork and then just sits listening until TTD  
Jamie Lokier:	In the hours/days between publishing the Ropsten TTD and it being reached, are we confident enough of the nodes running on Ropsten will switch their configuration in time to prevent a long-running PoW fork of many nodes?  Put another way, are enough of the Ropsten-running people are "involved" enough to keep up to date?  Motivation: I’ve been running 3 Ropsten nodes for about a year, and I'm not sure I’m the sort of person who would be that on top of the switch in 2 days.  Doubt I'm unique.  
Jamie Lokier:	I guess I’m wondering if we know how many Ropsten nodes are actively involved, e.g. in the teams, or if it’s very dispersed.  
Jamie Lokier:	Understood, thanks 🙂  
Jamie Lokier:	Yes  
Tim Beiko:	https://github.com/ethereum/execution-apis/pull/218  
lightclient:	¡™£  
lightclient:	oops  
Micah Zoltu:	Good morning to you too.  
Marius van der Wijden:	I'm against this, we should feature freeze  
Marius van der Wijden:	Oh. if you can roll this out based on `eth_getBlock` then I would be fine with you guys doing so, don't want to implement the batched call though  
Potuz:	oh yeah it's not necessary from our perspective, in practical terms what may happen is that some nodes may be penalized by not returning a large very old batch of blocks with execution.  
Tim Beiko:	https://ethresear.ch/t/blocks-per-week-as-an-indicator-of-the-difficulty-bomb/12120/20  
seananderson:	Michael has implemented payload separation in lighthouse using per-block requests: https://github.com/sigp/lighthouse/pull/3157  
Evan Van Ness:	breaking news: people who are against the bomb are still against the bomb  
Tomasz Stańczak:	well, I was always in favour of the bomb in  
Ansgar Dietrichs:	my (unqualified) preference is not moving the bomb  
Jamie Lokier:	I thought the idea of delaying the bomb *just to reduce the stress and amount of time spent discussing it* seemed like a good enough justification.  
Zuerlein:	would prefer a bomb delay strongly.  
Micah Zoltu:	I'm in favor of whichever plan has fewer people lobbying for it.  😁  
Pooja Ranjan:	:)  
Marius van der Wijden:	I think its a bit to early to discuss bomb pushback  
Potuz:	I'd repeat here my argument: if we don't delay the bomb we should test merging with larger blocks cause large blocks do stress the CL  
Danno Ferrin:	1559 will keep the blocks at about 15Mgas over the long term.  Don't underestimate the power of economic incentives.  
Evan Van Ness:	pushing the bomb back now is going to either unnecessarily delay or make it easier for scam forks to spring up  
Jamie Lokier:	Potuz' argument makes sense to me.  Beacon chain is so timing sensitive, a doubling of processing time really ought to have at least a bit of checking.  Perhaps that should be done anyway regardless of bomb.  
Zuerlein:	a short delay isn't a big problem. scam forks won't have the economic value or incentives of the main chain. we need to deliver the merge and should do so under a stable and predictable blocktime for TTD  
Marius van der Wijden:	The issues with the hive tests not passed by geth is due to some weird missmatch between the spec and our architecture. We are correct, but we don't/can't return an error  
Justins iPhone:	Why are our mainnet shadowforks insufficient for testing large block sizes?  
Zuerlein:	yes, that stage in sept is fine tho is it not? because august merge would be 20-26 seconds  
Marius van der Wijden:	We can't spam mainnetshadowforks  
Mikhail Kalinin:	@Marius we should discuss this can’t returning an error  
Tomasz Stańczak:	the error that is weird and unexplained is always worse than something that is known to require much work  
Micah Zoltu:	@Marius Do you mean you can't return the expected error to Hive?  
Marius van der Wijden:	Since we don't have much eth on the shadowfork that we don't have on mainnet   
Marius van der Wijden:	Yes we can't return the expected error  
Micah Zoltu:	So the hive tests are overly specific and should be loosened is the general argument here?  
Mikhail Kalinin:	or the spec should be loosened?  
Micah Zoltu:	Having consistent errors across client is important.  I would hope that we can solve the underlying problem if possible.  
pari:	I think IF we push back the bomb, we should do that along with Paris to indicate some confidence that the merge is indeed close.  
Zuerlein:	the original timeline was a june merge  
Jamie Lokier:	Would a softer bomb curve help?  
pari:	Including it in Paris still means we can independently decide when TTD is hit, but at the same time reduces some pressure + shows confidence the merge is close.  
Marius van der Wijden:	I remember Tomasz saying we could merge in October 2021 :D  
Marek Moraczyński:	I think Tomasz said October :D  
Marius van der Wijden:	2021 (last year)  
Marek Moraczyński:	He didn't specify year ;)  
Micah Zoltu:	😄  
Jamie Lokier:	"could have" may not be false ;)  
Evan Van Ness:	people are going to think that the Ropsten malicious miner attack worked if we delay.  
Micah Zoltu:	I think I'm sold on pushing back the bomb with the Paris Release Candidate.  
Evan Van Ness:	which maybe incentivizes more testing!  
Potuz:	Why would defusing the bomb delay the merge? I think these two issues should be treated separately.  
Zuerlein:	doesn't degraded UX mean ~15s blocktimes? 25s blocktimes is extreme  
Łukasz Rozmej:	why its ok to have higher block times/  
Tim Beiko:	We will have to wrap up in ~5 minutes. There were 2 EIPs which wanted to give a quick update, so we can quickly cover those in the ~5ish mins after the call.  
Tim Beiko:	*after the end time, we can keep the call running another 5ish :-)  
Justin Drake:	+1 what Marius said  
Ansgar Dietrichs:	I think a 4-6 week delay now would be reasonable  
Justin Drake:	20s block times work IMO  
Ansgar Dietrichs:	I think 2 months also works from a messaging pov, “giving us time through the end of August”  
Evan Van Ness:	let's punt the decision to next call, when we'll know more  
Marius van der Wijden:	I don't like it, but I would be okay with 2 months, we should prepare and make the decision after ropsten fork  
Ansgar Dietrichs:	I think pushing to next call is starting to eat into acd productivity, we are spending a significant amount of each call debating this now  
pari:	Let's not forget that DevCon is still planned for October. Typically conferences tend to be a sinkhole in terms of async communication and we’d be better off delaying it to just  before devcon or far after.  
Jamie Lokier:	2 months would be enough, perhaps the minimum, to allow the conversations about the bomb to stop for a while and other things to have breathing room in the call.  3-4 months feels more effective to me wrt focus on other things but I see the arguments against it for community-coordination optics reasons.  
Tomasz Stańczak:	I'd rather delay the devcon :)  
Tomasz Stańczak:	;)  
Zuerlein:	a 2 month bomb delay is fine. i am praying not to hear more 2023 bomb delay from another miner group  
Tomasz Stańczak:	but good point about the DevCon Pari, did not think of it  
Zuerlein:	merge should certainly be before devcon  
Łukasz Rozmej:	I think we should target before devcon definitly, is that the boarder for difficulty bomb is another topic  
Potuz:	I think what most people would find least bothersome is that whatever the expected date of the merge is, then we want to set the bomb so that at that timeline block time is less than 20s  
lightclient:	haha  
Zuerlein:	devcon is 2nd week of october? so target a merge in late september with ~15s blocktimes?   
Tomasz Stańczak:	my target was to set the bomb so the Merge data is when the bomb starts affecting the block times  
Tomasz Stańczak:	I think the bomb explodes when blocks start to get slower, not when they are 20  
Tomasz Stańczak:	sorry, got to go unfortunately, thank you everyone  
Tim Beiko:	https://github.com/ethereum/EIPs/pull/5088  
Tim Beiko:	https://ethereum-magicians.org/t/eip-2537-bls12-precompile-discussion-thread/4187/21  
Mario Havel:	bye everyone!   

