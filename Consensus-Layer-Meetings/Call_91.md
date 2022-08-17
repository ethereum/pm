# Consensus Layer Call 91

### Meeting Date/Time: Thursday 2022/7/14 at 14:00 UTC
### Meeting Duration: 1.5 hour  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/566) 
### [Audio/Video of the meeting](https://youtu.be/yBEPzzeo1a4) 
### Moderator: Danny Ryan
### Notes: Alen (Santhosh)


---

## Intro [2:18](https://youtu.be/yBEPzzeo1a4?t=138)

**Danny**
* The stream is transferred over. If you are in the YouTube chat, please let me know that you can see in here us issue 566 consensus layer, call 91. First order of business. We're going to do these every twice a week for a while to catch up with the allcoredev call and then supersede them in numbering. Sorry, a bad joke. today we'll look at merge stuff. So many of you boost stuff, which is related to the merge and then general updates and discussion points from there. If there are any on the merge, there are a few things, and then we can leave room for anything else that you want to talk about first, Perry, can you let us know what happened to or happened with and how it is going of M S F nine so we had men that shuttle for nine much earlier today. 

## Merge updates [2.28](https://youtu.be/yBEPzzeo1a4?t=147)

**Pari**
* I'm not actually sure why the estimation was so off system, but the TTD estimation we did last week was hit pretty much like a day and a half earlier. And the estimate I ran yesterday was still like eight hours or eight or nine hours the unexpected. So it caught us, a little bit by surprise, but either way is, we are finalizing on the network, but just barely, and I'll go through the list of reasons why. so the first issue we noticed was, there was, there was a problem with a lighthouse modes where they would ever so slightly followed a sink and they wouldn't start synching again until the next epoch where they catch up. the lighthouse team already had an open PR and I think it was almost ready too much. So all was able to give me like a fixed image for that, really quickly. And that was dispatched, the besu nodes, I think four out of five of them hit an invalid block. I think it's still related to their world state issue. Nethermind, is offline on purpose though. they ran into this issue on Ropsten and I think, thing mark, we'll talk about it a bit later, but they ran into this issue on Ropsten and they thought they had fixed it, but they ran into the issue again on may not shadow folk eat, but after like 12 days of running without a problem. so I think they wanted to track it down. So they purposefully than like 25% of the Nitrox on Nethermind on like clearly weird configurations. So each of the node was configured differently with I think, different cash rules. so that there a, figure out the issue on our key, some of them, and I think they did. so hopefully that helps them figure out the problem. Eric Kahn had not sync up to head or some of the Aragon notes had not seen it yet. I'm not particularly sure why it's taking so long to sync. So from next time I'm just going to be using a snapshot that we have created. So we should be able to make sure that they're sync before the, four kids, but they are relatively close. So I can give you an update on that later. And the Nimbus notes was an issue on my conference. I've been merging, like a lot of changes we had temporarily for different shadowbox and on one of them I had, check for, if it's Nethermind note, it wouldn't run the G it's not PC snowball because now the Nimbus, Nope, we wouldn't run the GS and RBC snowball because Nimbus was using WebSockets and we didn't need it. But in the meantime, I had shifted to HTTP, but the check was still there. So basically all the numbers not we're sending the request into the void. so spinning up the RPC, super fixed that. And I think most, if not all of them node them. yeah, I think that's a list of all the issues that we had, all in all, I think like 30% of the network is offline, but I guess if the Nethermind nodes come back online, then much higher percentage would be back on that. 

**Danny**
* Got it. Is there anything in particular that we learned from this, either in how to do things or, you know, new issues surfacing? 

**Pari**
* I think on my side it helps validate all the conflicts changes that had been margin, and that I'd be using a different method to send Eric on in the future. Those are the two from my side, but I'd let the client teams talk about the rest. 

**Danny**
* Mark, I, we can barely hear you. Can you get closer to the mic or try a different mic Right now better? 

**Marek Moraczynski**
* Yeah, So, we had a weird, rare issue with three exceptions and I noticed it before on the ropes then, I think it was the same issue. and, we fixed a few things, and we never noticed this issue again, for a long time. And yesterday after I think 12 days, we noticed it on, mainnet, fork eight, we start preparing a very different configuration to get to know what's going on and maybe to trigger it fast a bit faster. And it seems like, reducing burning cash, three guarantee the issue faster, and maybe we have potential fix also bot we are exploring it a bit more. So, yeah. 

**Danny**
* Got it. Is this related to merge code paths or is the 91 issue? 

**Marek Moraczynski**
* I think it is, it is related to pruning called, but it could be on, it could be triggered also on mainnet, not my mainnet, not much pre-merge, but it is very, very hard to trigger this issue, pretty much. And it is easier, for shadow forks, especially, that this, the problem. Right. So I think it is very hard to notice this issue pre-merge.

**Lukasz Rozmej**
* So, it's a bit related to how, because we process some new payloads if we can a block to validate it. And it's related to, that we had quite random, distribution of, new payloads, like going back X blocks, like having payload that is, older in terms of block number, quite a lot, or having multiple payloads at the same level on the shuttle forks. So, yeah, it's, it's a bit more random here and more like frantic, so that helps trigger easier. 

**Danny**
* Have you all been looking at the antithesis results because they also, their platform, I think often has get some of these like weird weirder scenarios coming forward. Did y'all see anything there? No. Okay. any other client teams specific reflections on mainnet of forknet? 

**Marek Moraczynski**
* Wow. Why? I think I shared, probably the reason, and we see that, we are receiving payloads, in order and we, when we received one payload out of the order and that probably triggered the issue in nethermind nodes, but I think generally unhealthy network, we shouldn't have, this, I mean, it is possible of course, but, when we are running all the nodes, it shouldn't happen. So maybe it is also connected to besu issue that trigger this new payload out of the order. 

**Danny**
* Yeah. I think dropping that in a, just so that we can see if it's related to one specific client type would be good. And is that, are you seeing that on all of your different cl client pairs or is that from a particular Yes. 

**Marek Moraczynski**
* Yes. 

**Danny**
* I guess it seems network-related rather than, okay. Yeah, if you can put that in a, just with some notes, let's dig into it. 

**Pairthosh Jayanthi**
* Another thing to mention is we haven't really had network-wide non finality tests on me in shadow yet, but for a period of time, I think 60 E-box the network wasn't finalizing until like some conflict changes were made, for example, fixing the numbers nodes. And once that was done, all the numbers, nodes recovered as expected and the network finalize, and it seems like we didn't have any hiccups there. So that's good news. 

**Danny**
* Good to know. I'm looking at the screen and want to ask lots of questions, but I don't think we should live debug this. okay. 
* Any other,  discussion points and if not, what's the next plan on shadow fork?

**Pairthosh Jayanthi**
* I was thinking considering we'd want to go, as the next Testnet, we should have a Gordy shadow folk next, and that should also make it a lot easier to have a bigger network if you want, or spin it up more on more short notice, we wouldn't have to wait like a week for the shadow fork, for example. Yeah, exactly. 

**Danny**
* Got it. Okay. And I, I suppose we should, double down on our, the estimation that we used here, to understand, was it, this was, the CT do was selected like a week ago. So we were off by like half a day and half a day, seven days, not half a day in the context of a day. 

**Pairthosh Jayanthi**
* I actually know. so the one we selected a week ago was off by a day and a half. And the one we selected yesterday was off by about half a day In the, earlier direction on both. Exactly. So at least looking at ether scan and it does seem like hash rate has gone up, but not by such an insane amount of yet. 

**Danny**
* So Perry on Gorly shadow fork, that would be this coming week. And that would be mid week. Yeah, I'd say Wednesday just to keep it easy for everyone Configs out Monday nodes up around the same time and Wednesday target, something like that. 

**Pairthosh Jayanthi**
* Okay. Okay. 

**Danny**
* Great. Well, if you have, particular builds or config changes or anything like that, please, please, please let Perry know. 

**Pairthosh Jayanthi**
* And I also wanted to ask people if they still want me in that shadow form for debugging, or that can be torn down, at which I will know one or two day because we updated. 

**Marek Moraczynski**
* Now it's just to see something, with three exceptions. Of course, if it is a problem or we can switch to, number nine, No couple is fine. 

**Pairthosh Jayanthi**
* I think it's more useful having it around for you to deeper. 

**Danny**
* Okay. Any other questions or comments on prior or future shadow forks? Okay. Perry, you have a discussion of naming I'd like to bring up as we approach the goerli merge. 

## prater vs goerli naming moving forward discussion [16.00](https://youtu.be/yBEPzzeo1a4?t=998)

**Pairthosh Jayanthi**
* Yes. I think people, eventually going to start asking about documentation, etc, for what we, how we want to treat the future much goerli Prato network. I don't know, early on, there was some consensus I'm just calling it a goerli, but that still implies there needs to be like a breaking change or if every client wants to support goerli and Prato flags, and that's what we use in documentation. And then eventually there's a, taking change where Trotter's removed. I'm not sure if the approach or even if we want to go down that route, but I wanted to bring it up for discussion. 

**Danny**
* And this is because on the consensus layer, we have particular flags, like if you were doing a network configuration dash dash network. 

**Pairthosh Jayanthi**
* Exactly. Exactly. And it's just easier to communicate to people if, if we have like a decision made now. So all the documentation written follows those decisions, versus having to change it in that way. 

**Tim**
* Would it make sense to, deprecate the Prater flag, leave it, like, leave it work in clients, but market, you know, market as deprecated and, and introduce the goerli flag and then, you know, you, you keep, you keep, yeah, you keep both as like an alias for, I dunno, like the next six months or something. And then eventually you just separate the predo flag or remove the Prater flag, but you have like a deprecation announcement when the goerli merge happens, basically. 

**Hsiao-Wel Wang***
* Well, I even deprecated, I mean, we could just leave it there, right? 

**Tim**
* Oh yeah. I mean, if you want to leave it there for a brochure.

**Andrian Sutton**
* I think, I think the first key question is, clients are happy, have an alias, which particular, I think it's really trivial and it's a no brainer. if that's the case and it will be in the release that we're saying you need to upgrade to for compatibility anyway, then the instructions usability and clients decide to how long they want to support product. I think is really only an issue if there's a client that doesn't want to add the goerli alias for some reason, then obviously the instructions would have to be tailored to that client. Just keep seeing product. There's no real reason we need to coordinate the removal of the product. That's just part of the client UI UI, but user UX. 

**Paul Hauner**
* Yes, a lot house. I think it should be pretty easy for us to add an alias. I'd probably also tend towards leaving Prada there as well. Just for people that already have dev ops setups, like a dev ops set up already calls it Prada everywhere and figuring out how to change. Just the network flag name would just be kind of painful. 

**Terence**
* Same with the Prism, 

**Danny**
* Anyone from Nimbus, I'm here? 

**Zhary**
* But I didn't hear what those means. 

**Danny**
* That's all right. The, it might be easier to communicate to users to use a Goerli alias in consensus layer configs. So maybe dash dash network quarterly and just keep prater there as well. That's so easy To go. Okay, great. 

**Pairthosh Jayanthi**
* Perfect. So documentation, we'll focus on just using the golly flag and the expectations that, merge-ready releases. This would have that flag of visible. 

**Andrian Sutton**
* The only thing I'd probably add is in the docs, we should note that you don't need to resync if you use product. Like we don't want to cause users a lot of confusion to, I think they're actually switching between modes. So they kind of, if there's a note that Goerli is just the new name for Prada and it's an idea that would be very useful. 

**Pairthosh Jayanthi**
* Yep. Makes sense. We'll make sure that. 

**Danny**
* Great. Anything else on this one? 

**Pairthosh Jayanthi**
* Nope. That's that's the whole topic. 

**Danny**
* Okay. Tim, will you give us the TLDR on your document on the one verse two phase merge deployment? I believe most people are pretty familiar with it. so maybe just get the high level. 

**Tim**
* Yes. yeah, so I high-level is, what we want to avoid for the merge is, the TTD being hit before, Bellatrix is live on the beacon chain, because it causes a whole bunch of issues. and there's three ways we can achieve this, with different pros and cons. the first is we have a single release outfit merge, which combines both Bellatrix and the TTD, like the actual TTV. And because on the main net, we can fairly well, estimate, difficulty, you know, we can, we can plan it such that like it's, it's, it's quite unlikely that the TTD would be hit before Bellatrix. and the pushback against that on the Allcoredev call was that, well, you know, a lot of, the security assumptions we make usually revolve around, like, what if a state level actor wanted to mess with the process and with like the declining hash rates on mainnet that there might be a small chance that like, this would be possible. if you had a massive, massive amount of hash rates, so, you know, you would get like a simpler UX for end users, but like introducing potentially some, like security, I wouldn't say like a security issue, but like the potential risk of an issue. and, and very kind of very, I guess, extreme edge cases. So the other approach you can take is instead of doing that, you do like we've been doing for, for some of the testnets where you have a first release go out with like a huge TTD. And then, and then once the electrics is live, you have a second release, which has the actual TTD. And then, you know, for a fact that, that's the second release, the TTD for the second release will never hit before black Trix, because electrical is already live. And then the third option you can do is what we've also done like on Robsten is you just do a TTD override. so you know, you, you, same thing you have the first release with a high TTB, once Bellatrix is hit, you just have an override. And the, the, the, the kind of trade-off there is like, you might be able to coordinate an override quicker, then you coordinate the new release for downloading, because you don't, you know, you know what the flags are in advance, and you can communicate them to users in advance, and you just tell them, plug this value in the flag. Once you've selected the TTD, rather than waiting on like 10 clients releases. the outside is you're like asking users to do some more like command line interactions, that they may not have to do if they're just, that will be in the release. so those are the three options. I think if we were to take like the dual release, kind of approach, I guess. Yeah. Regardless of what your, we would take, it would be good to take the same approach across the main nets and Goerli such that users know kind of what they're getting, what would the flow will be like on main net? but if, yeah, if, if, if we could decide this today, I think it would be really good because yeah, the new means we can start like coordinating things for Gordy. yeah. So I'll, I'll, I'll pause you. 

**Dankrad Feist**
* Yeah. Just one comment. It doesn't feel like we need on our main to consider someone literally that someone has that the best that they can do accelerating to merge to that. 

**Danny**
* Yeah. And Donka, we can't hear you very well, but we, I think we get the point. I think this is, this has been brought up a number of times, and I also agree, and I'm going to meet you cause you have a lot of noise in the background. yeah, it's not only if, if such an adversary exists, such an adversary could potentially do other worst things. And if such that various adversary exists and wants to do this, they can't do it overnight. They have to do it in a very, obvious way once these numbers are released. And so there's also on the order of a week or more to react, but I think so I think that's definitely the, the, the strong argument in saying that this doesn't really change our, the adversary that we're considering here. it maybe gives them one other thing that they could do in this discreet event. but that it's very unlikely. They could even do it without us noticing and fixing, Andrew. 

**Andrew**
* Yeah, I think we should go for a single release because the merge is complicated enough already. And like we, as developers, we can deal with it, but to a lot of users, it will be very, very confusing just to, to realize that you need an el client, I see cl client, you need to, ensure communication between the two and so on. And if on top of that, we complicated by a need for another release in our, flag override. Or it's just like, it's, it's an unnecessary complication that will cause a lot of headache. The simpler, the better it's it's like the merge is already super complicated. 

**Danny**
* Got it. Thanks, Andrew. 

**Paul Hauner**
* Adriana is a thumbs up. 
* Oh, sorry. Yeah. Yeah. Thumbs up for me. I prefer a one release, a one, a single release. I think a downside of the July. 
* This is the it's going to take us more time, cause we need to give more notice between atrial lace, which either means that the merge happens later, or it means that we force things to happen earlier that could have happened later whilst the merge happens at the same time. If that makes sense. 

**Andrian Sutton**
* Yeah. I think that the key in this is that we want to be setting at TTD, which I mean, hitting it before, before Bellatrix is activated, requires a 51% attack. Like if you got a double, the mainnet hash, right. Then, that's, that's not feasible in our security model by anyone. if you can do that, your host, you know, if we're, if we're able to do that, I don't think there's any real question that like, we're not introducing new security risks and we shouldn't be concerned about that. If we're reducing that threshold somewhat, then we can talk about it. But I'd like to like to see some clarification that we would be reducing that from a 51% attack to something lesser, less a percentage before we worry. 

**Tim**
* Yeah, I think so. Say, okay. As long as the cap, so basically, you know, if you think of the gap between choosing these values, hitting Bellatrix and hitting TTD, as long as it's like an equity distance, like gap between choosing in announcing the values, then hitting Bellatrix and then hitting TTD, then you would need to double the hash rate if you started mining, like on the second that the announcement is out, that to make it happen before. And then as you get closer to Bellatrix, that proportion changes, right. If you're like a week away from Bellatrix and like two weeks away or three weeks away from TTD, we would need the like more than double the hash rates. so I think in practice, what if we wanted to go with this, like 50%, hash rate assumption, what it looks like is like you choose you, you like announced the releases. two weeks later you have Bellatrix and two weeks after that you target TTD. And that means that like, if you doubled the hash. 
* If you doubled the highest rate from the time of the announcement, you know, you might, get TTD before, but, and then every day that passes where that isn't the case. you, you need an even greater share of passwords. 

**Danny**
* Yeah. So it's primarily in the, if you shift the ratio, like if you went to one, on that split, then you're, you know, you needed to add plus 50%. and so that's, you're changing your assumption a bit. but also not necessarily in a incredibly detrimental way also because it's extremely observable. but nonetheless also there's always two types of 51% attacks. One is the existing hash rate, colludes and 51% attack and others, a new amount of hash rate shows up. new amount of hash rates showing up is, is a much more difficult thing from a world resource perspective, but not theoretically impossible. Okay. Did any other engineering team want to chime in? Does anybody want to take the counter to this? 

**Micah Zoltu**
* I still favor their most robust solution, but I don't have anything new with it's not already in Tim's document. I think he did a good job about lining all the options and the pros and cons. 

**Marius Van Der**
* I think we should have just like made Bellatrix a bit differently so that it doesn't need to TTD to be specified at the four point. Oh it doesn't. Okay. 

**Danny**
* So it's not like it gets baked into the chain or anything like that. It's, it's a configuration parameter, either being said or not. I guess you could have done Bellatrix in a way that it doesn't need to be talking to execution layer, to be pinging and then you upgraded it, but that's still kind of the same thing. That's still kind of like unknown or infinite TTD, but then it's primarily error log thing that maybe changes, which I think is some of the argument here. 

**Marius Van Der**
* Yeah. It just kind of feels weird to me that we have two folks that are somehow connected to each other. No, we're doing specify to folks, but it's fine. I'm not going to argue. 

**Danny**
* Okay. I do believe based off of here and conversations with engineering teams, that there is a strong desire to do a one phase approach, based off of the assumptions around the attacker and the engineering simplicities. So I would suggest that that's what we do with Goerli. 
* Anything else on this point, This isn't for Goerli,

**Tim**
* But I think for maintenance, it would be really valuable if within like 24 hours of choosing the TGV and the Bellatrix height, clients are like able to schedule a release. so I am like, I'm not sure what's the best way to do that, that it was, we can discuss it offline, but yeah, basically we don't want to like have a week ago between like choosing this value and announcing yet, we'll with client releases. So I think that's the only thing it's like, it would be neat if clients were like ready to release just before we choose it. And then they plug in those two values and then within like the next day, that can be, a release that we can announce. 

**Andrian Sutton**
* Yeah. One of the things to be aware of is that until we have a TTD, whether it's a ridiculously high one or the real one, uses constant updating their conflict because the execution engine on the number of el doesn't stop listening. and you know, the conflict checks don't happen. 
* So if we're making that tight timeline challenged for users to have that in time,

**Fabio Di Fabio**
* We're in the process of changing that so that when you start up geth will already start up the engine API. 

**Andrian Sutton**
* That's awesome. I think the conflict checks will still be an issue because you want them to be in sync, but, yeah, definitely useful to change that. 

##  Other merge related discussion points [34.59](https://youtu.be/yBEPzzeo1a4?t=2097)
**Danny** 
* Let us move on other merge related discussion points, anything that we want to bring up either to notify this group or ask them questions, anything like that. 

**Paul Hauner**
* I did want to, just touch again on what, Marius and Adrian were talking about then about just trying to get, make sure that all the execution engines we'll start there off RPC ports kind of from now, before the merge, before the merge parameters have been announced, that allows people to set up the DevOps environments as if the merge is already happened. so yeah, it's very important. So at the moment, is it don't open that orthopedist report, before the merge parameter, it means that people can't future-proof the, setups, but I think, it sounds like we're people are already moving towards that. Just wanted to raise at this point. 

**Danny**
* And Tim, can we make a note just to bring that up on Allcoredev call as well? 

**Tim**
* Yes. 

**Danny**
* Although I think we have good execution there, your attendance today. okay, great. 

**Pairthosh Jayanthi**
* Do we want to talk abou the progress/ status update on the Goerli?

**Danny**
* Yes. Do you have a status update or does Tim have some ideas on when we can or should be picking numbers? 

**Pairthosh Jayanthi**
* So the only thing that I have that could have as this website from fi, says estimate TTD on Goerli call is really stable to estimate. I think even if we were to pick one, now that's three or four weeks in the future, we'd still be able to get it down to within a few hours. yeah, and the website lists like a bunch of options, but that's what I think depend completely on the client teams and  when they want to change, or even if we want to make a decision today.

**Danny**
* Tim, based on recent discussions, is that something you want to do today?

**Tim**
* I'd just be curious to hear from client who's like, I know the last off Allcore devs last week, you know, a bunch of them are looking at this and recent issues, especially on the EL side. and if we can pick it, you know, far in the future, is, is it valuable to pick it today if it's a month out or is it better to like, it gets closer? I'll have a strong in there, but yeah, I guess do client teams feel like they're, they're ready to move forward? And if so, when would they want to see the before cabin? 

**Lukasz Rozmaj**
* So from Nethermind site, I think generally it's good to have a plan ahead. We can like modify it if something goes terribly wrong. And it terms of like the dates four weeks is reasonable freeze a bit, stretching it with, with the issue we uncovered that we want to explore more, that we would like to have this fixed before. 

**Tim**
* You said that's it Four weeks would be reasonable. Sorry?

**Lukasz Rozmaj**
* Yes. Yes. 

**Tim**
* Okay. So four weeks that would be like August 10th or so. 1, 2, 3, 4, yeah. Counted correctly. I guess, and then obviously we'd want Bellatrix to happen before that, as we were all okay about, I think it could actually be interesting to like try and try and like estimate it four weeks out because, that's basically what we'd want to do for mainnet. we can't have Bellatrix happen closer. Like we don't need this, like equidistance gap, like we do on amendments of the hash rate, but, 

**Danny**
* Yeah, Monday, a Monday Bellatrix might make sense in this type of network. 

**Tim**
* Yeah, exactly. So we could do, basically targets the 10th of August for Goerli and then target the 8th of August for Bellatrix. 

**Pairthosh Jayanthi**
* I think that still keep like few days, more apart, just because worst case all the signers then bring up their nodes and they realize they've been offline and suddenly the difficulty average equals. 

**Danny**
* So more of a, maybe a Thursday prior to that Wednesday, Actually four days is probably. Well, then you have the weekend. 

**Pairthosh Jayanthi**
* So then you want to buy for the weekend Or are we do, Thursday to The TD on Thursday and Monday until six, Right? Yeah. 

**Andrian Sutton**
* Yeah. I mean, the only concern I have is that if we push out the merge for Goerli prouder is the main network where validators are testing. so the later that is in the close to that is the main net, the less, the community less time the community actually has to really prepare and is forced into preparing for this. So I worry that we push it back so that we can get the final little details of final bug fixes gold-plated release that we actually shoot ourselves in the foot. Cause we're trying to wet where we're giving less time for the community testing in the, in the biggest environment that we have in the place where most people will be affected. 

**Tim**
* How long do you think people should have to test? 

**Andrian Sutton**
* I think, I don't think there's a clear time. but just to me it's more, let's let's for GoLean product earlier, rather than later. even if we know that, you know, a couple of clients who've got, got some bugs, as long as the user experience is set, then that preps people really well. otherwise we're drilling out thumbs and they're not, not twiddling our thumbs. We're taking up more time towards the merge than we need really. And that's being taken out of the community testing budget basically. And I don't think that that's a reasonable thing to get the community on board as, as soon as possible. 

**Danny**
* So given that where you're July 14th right now, do you have, are you making a recommendation on a particular date or week? 

**Andrian Sutton**
* I mean, how quickly can we get client releases out basically? 

**Danny**
* So in one week we'll have the Goerli shadow for, so I believe we shouldn't do it next week and that we should do a shadow for before. So then if not the 10th, we're looking at more like the 27th or the third. it sounds like you'd be pro 27th. 

**Andrian Sutton**
* Yeah, I said, I think, I think we need to give a reasonable amount of time between announcement and update as well. because again, we've got a lot of people I'm proud of that, that we'll need to actually make changes and they won't be paying attention too much. So 27th probably works. 

**Danny**
* Phil, you mentioned the community call tomorrow is, those that have been on and have been running these calls. Is that actually a good place to like, get and put on this Casey I'm getting here. 

**Tim**
* I don't, I think we can get some inputs for sure. probably by like the more professional side and like infrastructure provider, like I don't think there's going to be a lot of like individual random stakers who show up, 

**Danny**
* But I also don't suspect that well, I would suspect that people want more testing time. so that, yeah, I would estimate that's the response. 

**Tim**
* I think, yeah. One thing I do agree with Adrian though, is having like some amount of gap between like announcing and release. That's like at least a week and not like a couple of days. so it means like, you know, if we're not sitting on the 27th that we would fork on the third basically, but like that's requires clients to be ready on the 27th. Right. you know, and more or less a couple of days by they'll take, we want like twin that's on a Monday and fork on a Thursday, for example. if we're expecting like most stakers that actually, have to take time and update their conflicts there. 

**Danny**
* Right. And implicit in announcing is we want to have releases out. So it's like deciding today, you wouldn't announce today. You would announce in some amount of lead time before the fork, when we had releases. 

**Tim**
* So I guess, yeah, it's, it seems like either we would announce something on the week of the 27th and fork on the week of the third or announce something on the weekend, the third and fourth on the week of the 10th. like I, I doubt that like client teams, unless yeah. Client teams could have a release out next week and then we've worked on the weekends, like the 27th, but last week. I think that was a bit quick. so yeah, 

**Pairthosh Jayanthi**
* I mean, I Also question if one week notice is enough because we ideally also want the community tools to have enough time to update. For example, the Ethereum  arm guys would have to release their image that would rely on the, CL releases. That one would probably have to make a release and we'd probably want a few community videos and guides up and running. I'm sure we can already start working on that stuff with like placeholder releases, but the say it has no devastate. There's probably, it's probably good to have a higher buffer period than just releases that are expected to update. 

**Tim**
* So in that case, if we think we want even more than a week, I would, I feel like releasing on the week of the 27th and like announcing there and then maybe doing the fork, like, Bellatrix on like the Monday and then, and TTD on, on the Thursday. So like on the eighth and the 11th. So that gives like 10 days before Bellatrix and like 15 days before, or a bit more than 10 days actually before Bellatrix like more like 11 days before Bellatrix and like 15 days before TTB onboarding from the releases. does that seem reasonable to people? So these kinds releases should be out like on the 27th or 28th, ideally, so that we can announce this on the 28th and 29th and then, yeah, for fork on the 8th and the 11th. 

**Danny**
* Can you contextualize that in terms of, a mainnet timeline? 

**Tim**
* I mean, look like, if we, if we forked it, I guess, you know, imagine we forked Goerli on the 11th of August. everything goes well, everyone's super happy. it probably won't cop it like, you know, imagine like, yeah, we, we, we, we said, oh, well we want to see it like stable for obviously a couple of days to a week. It means on the 18th of August for all core devs, we can probably decide if on like, when do we fork mainnet? and, you know, imagine that like we have the release releases out to the week after it up. or like, yeah. So that means that the two week after that that's like early September, early September, and then like mid, late September, we would hit TTD. so I think it it's well, like, yeah, The release. 

**MariusVanDerWijden**
* If we have to release this out early September, then I don't think we can fork with?

**Tim**
* Oh, sorry. I meant early September, you get Bellatrix. So it's like, we work on the 11th on the 18th, we decide, we decide on like the final values. So the releases are out like, you know, like the week of the 24th or the week of the 22nd of August. And then two weeks after that you have all the Bellatrix. And then two weeks after that you have TTD, which, which gives you like the week of September 19th. and if we want it to be like slightly more aggressive, you know, like, I guess the thing, yeah. The thing that would maybe bias another week in a way is like either we don't for Goerli on the 11th, we have like a lower gap between Bellatrix and TTB or if we want to get a couple of days as well, we can also have like an off schedule call. Cause we're like waiting basically a week between Goerli fork and the next All core dev to choose the TTD. If we want to save a couple more days, we could have like an off schedule call or just move all core dev the next week, the lights, the Tuesday, for example. And then, and then you gain that much, that, that many more days. so, but yeah, I guess, I guess that's it. Yeah. The only risk is if we fork, if we try to hit TTD on a Tuesday, the, obviously the cl call happens on the Tuesday. And so it's unlikely that on that day would feel comfortable like moving the main nets because we won't, we may not have seen TTD on Goerli hit. And even if we have, it'll be at best for a couple hours, 

**Danny**
* I mean, I definitely think we're in a position where picking up two days or one week here and there, if possible is preferable. 

**Tim**
* Yeah. I agree. I'm finding moving All core dev by  your week if it means like we get the merge like a week earlier, because imagine, you know, if you had all core dev's on like the, even like the Monday, rather than the Thursday, it means for sure client teams can have a release out by them. but by the end of that week, and you, you kind of save like, you know, instead of having Bellatrix hit on the week of September 5th, maybe it hits on the week of like, the last week of August and then similary, instead of hitting a TTD on the week of the 12th at the 19th, maybe you hit it on the week of the 12th. so I think we get, you know, and we don't have to decide obviously this today, but I think if we, if we're willing to, have, the Goerli fork happen in like the week of the eighth, both the Bellatrix and CTV have clients out on the week of the 25th, it does put us in a space where it's like quite realistic emergency September, assuming again that like the Goerli fork prism, if you go up. 

**Danny**
* Okay. So based off of this conversation, obviously the conversation got anchored again onto that eight, 10 week. but there's also, more context around potential timelines and how to strategize there, Adrian or anyone else. Do you want to still argue for an earlier week? 

**Andrian Sutton**
* I mean, I, I'd still probably prefer to get client releases out next week, but the Goerli TTD, but, that is probably pushing it. I think I can live with that. I think it's a no brainer that we should schedule ALl core dev shortly after Goerli goes through, and mergers so that we can make that decision to call on mainnet and as soon as possible. 

**Danny**
* Yeah. Agreed, thank you. Anyone else? 
* Okay. so we'll have our statisticians go to the drawing board and, select some, potential on the TTD and fork epoch, for prouder or for Goerli and proud of respectively. and then Tim, is that something that we should try to get consensus on over the next few days? Or is it something you get consensus on on one week from today? 

**Tim**
* I'll share some values, I'll share some values like before the next All core dev, we just need to like tweak a bit, FreeState and put that with like, you know, we can confirm to them on All core dev does, but there's no reason for people to blocked to be blocked on that. Like, I don't know if I'll get them today or tomorrow, but at the latest on Monday, people should expect like that proposal for be, you know, the ephoc Bach is like a no-brainer to figure out obviously. but yeah, the TTD would just need to change our freeze estimates to do Thursdays instead of Wednesdays. So that shouldn't be rocket science. 

**Danny**
* Okay. Thank you. 

**Andrian Sutton**
* Any other And just decided that if we can, instead of waiting for All core dev to set a TTD, otherwise we just take another week before we even start all these processes. 

**Tim**
* Thank you. So I can, I can put, I can put it in like the, the spec for Shanghai and I'll open a PR and I'll let me get PR open for like 24 hours and somebody wants to object to it. they can there, but then I'll just, I'll just merge it. 

**Danny**
* Okay. Thank you. Any other, points on this Goerli and merge schedule?. Okay. Any other discussion points related to the merge? Okay. Thank you. 

## mev-boost updates. [54.12](https://youtu.be/yBEPzzeo1a4?t=3252)
**Chris Hager** 
* Hey everyone. Yep, sure. please interrupt me. And as a couple of points and I try to keep quick, multiple development is that prism, the beacon specs, the builder specs implementation. So it's not takeaway in prism that are, completed integration and it's merged. I think lighthouse still has a testable branch, but it's not much. And Nimbus and Lodestar are still in development. next topic is that met post, had a security audit that is now completed a bunch of minor issues with some recommendations and medium issue that is important to put in some specification for really operators there.
* Yeah. That's like some edge case is linked to the top issue, the audit PDF, yeah, releasing a new version with all the amount of access very soon. Be speeding, rolling out updates for the flashcards released at builders across Robsten and the Spolio. So have you seeing a lot improve performance? thanks everyone for your latency, measurements and reports in particular and Rico and Terrence, it's really helps. And let us know if you see any other issues with the performance. The bottleneck is mostly the signature notifications off the registrations because on the beginning of an ebook, they get a 10, 20,000 registrations and prism is currently resigning the registration on every e-book. So it needs to be re verified. yeah, so that should all be over done. We got a request from the booster to make a, one of the test nets, open to any validator. So registrations and getting the payloads are not bound to actual, validators, Spolio. what else? good to mention that As a permission network. 

**Pairthosh Jayanthi**
* So it would kind of defeat the purpose. It might be better to do that on drops 

**Chris Hager** 
* Really only needed for contents of clients development, not for actual users. 

**Pairthosh Jayanthi**
* Ah, okay. Okay. Makes sense. 

**Chris Hager** 
* Yeah. Thanks for doing what I do. So yeah, the realists, they are in a good state. if you see any additional latency, she'll speak, but go to investigate the network courses because the readings are plus now from Ireland, there's not an ongoing push on specifying the proposer Quantic file format. I know, and Rico Terrence and Stefan I've been working on that and not as a push to put it in writing, which is a public file definition, which allows proposers to choose relays fee recipients and other properties independently. So basically clients, if a bunch of elevators there, each elevator can set custom properties and then fall back on people, properties. 

**Danny**
* Yeah. So it can to how graffiti was done. You say you can even programmatically change the text file if you want. 

**Chris Hager** 
* Yes. And yeah. And lastly, I wanted to give a shout out to the ETF security people that have been looking into metals to build their utilities and other repositories in particular shadows to trust in it is very, was very good in fighting like edge cases around, the SSE  encodings and some types. And yeah, that's really very much appreciated. It's mostly around the goalpost repository, which is like just all the types for the pillar specs and the SSE encodings and JSON and coding the coding functions. All right. I think that's it around the most important status updates. 

**Danny**
* Great. Adequate question. The audit that you did was that on specification and implementation, or just the implementation 

**Chris Hager** 
* Mostly on the implementation, but he also looked through the specification specifically on the implementation. ?

**Danny**
* Got it. 

**Chris Hager** 
* I think he found an edge case that is, not necessarily something to change in the specification, but rather on like notes for implementers where validators quotes, if the reader does not properly verify, designed plan that we can block corresponding to the real slot and proposer, then there might be a tool to get the payload from if you're spoofing the proposer, like you can read it into a PDF link to the medium issue on our list. This is fixed, but we should put this probably in a builder specs repository in a related document. 

**Danny**
* Okay. Any other questions for Chris? 

**Pairthosh Jayanthi**
* Yeah. Would it be possible to have a up and a couple of weeks for one of the shadow Fox? We could have something that can 20% of the network relying on the, on, on MEV boost and see how it looks on a wider scale. 

**Chris Hager** 
* Yep. We can do that for sure. I think we, the internal on the timeline, we just need a little bit of a heads up to sync up some notes and to test this. 

**Pairthosh Jayanthi**
* Yeah, if we have early shadowfox next week, then I guess we would do me in a shadow for the week after. So that would be about two weeks in the future. 

**Chris Hager** 
* Okay. Yeah. I think we should be able to accommodate that. That is end of tonight. That sounds great. 

**Pairthosh Jayanthi**
* Okay, perfect. And, in case someone has opinions on how much the network has to be  MEV pools, feel free to reach out to me and then we can meet that time. 

**Danny**
* Great. Thank you, Chris and Alex, 

## Discussion about the builder specs around merger transition delay [1.01.24](https://youtu.be/yBEPzzeo1a4?t=3684)
**Danny**
* I believe brought this up on All core dev devs last week, but there is an issue or a PR up in the builder specs around merger, transition delay. Alex, are there any remaining questions or comments you have for this group today? 

**Alex**
* Yeah, I think, mainly we just wanted to talk about implementation. I think some people here on the call, wanted to discuss that as it's spectra. Now it would essentially be like an EBAC based delay. so first question is simply like, does everyone think this is a good way to, you know, sort of specify this embargo? 

**Enrico Del Fante**
* Yeah, it was, it was me, discussing, on the, on the PR issue. So the delay was initially thinking I was thinking was been, has been a very easy thing to implement by the way this being specified. It was adding a little bit of additional complexity then more than expected because actually if you are needing to add a delay based on when the first, execution payload has been finalized, if you start up a node and, not only has the latest state, you don't know, actually when, in the past this execution, Baylor has been, has been first, has been first, finalized. So you cannot count and you cannot, bring up with, with this delay, correctly, unless you are, persisting these information at runtime when it happens and then you use it later. this wasn't my point, definitely something we, we can do, why we were, we were arguing if makes sense. And then the arguments from Alex was actually convincing that makes sense for our potential clients to implement this as well. But I'm thinking if there are other clients thinking about that.

**Paul Hauner**
* It's the challenge in knowing whether the finalized block is post-merger transition or not? Is that a challenge? 

**Enrico Del Fante**
* Yeah, actually we call at least we have the only, the latest, a finalized state, right? So you mentioned that you start up the node and you have the, your latest state with execution Baylor the right there. So the chances that you have to go back in time with the canonical chain, finding out the block that was bringing the first execution payload fast, unless you have, you have started the somewhere when it happened in the bust, This feels like you're going, 

**Paul Hauner**
* Can I say, at least for the lighthouse wait. 
* So in informed choice we track, whether the execution status is enabled or not. And I, I would assume that most clients are doing it because of optimistic sync. and I don't think you need to actually find when it's a transition happened. All you need to know is whether or not the finalized block is pre or post-transition, I'm just thinking genuinely as well. I haven't read that stuff. 

**Danny**
* Yeah. I mean, there's also just the practicality of this is something of an edge case of somebody who is syncing with presumably a finalized state that's after the merge. and if it's, I would imagine that when you're in the a hundred ephoc range or something like that, that you can kind of just turn this on. or if your node is online for 16 ephoc, then you also know that you've now reached the condition because you started with a finalized state that had the execution payload in it, and now you've also weighted 16ephoc. So you know that at that point you've also hit it. So I just, I think we can probably use some sort of heuristics here for this edge case around sync. If somebody is actually starting with, a piece of, a state that's really close to the merger and there's some uncertainty, but I, I wouldn't, I don't think that we need to bring a ton of complexity in here's. 

**Potuz**
* My intuition That is, is, is the question about this, that the check for optimistic seeing whether or not we're close to the park? 

**Danny**
* The question is if you're, if you're actually at plus 16 ephoc, since the first finalized post-merger state, 

**Potuz**
* I'm not understanding why would you want to add the 16 ephoc?

**Danny**
* 16 ephoc in the builder specs on how long the delay turning on MEV boosts.

**Potuz**
* Oh, I'm sorry. This is okay. 

**Terence**
* So Yeah, so for Prism it's actually fairly easy to do since we can just look out for choice store and see the latest finalized blog has a institution pillar or not. And then we can plus minus 16 epoch what our slot from there. 

**Andrian Sutton**
* But if, you know, then restarted you like, so if you then finalize, so you for epoch into that period, the node restarts, you don't want to add 16 to the finalized checkpoint when you start up again, you've actually got to remember that before he pokes into that period, which there isn't anything in the state that can tell you than what Oh yeah. 

**Paul Hauner**
* I didn't realize that we were waiting like an epoch off to the finalist station happened. Yeah. That's going to be a little bit more difficult for us as well. 

**Enrico Del Fante**
* Yeah. There were thinking if you're at run time, you can do that at, if it happens at run time, you can, we can store something in our key value store just for remembering and persisting for, for the sake of our start and then, and then use it. if, if the, not the restarts, it was my, my intention to lower down the complexity. Even if at some, at some point you need to hit the store and to persist these information, which I think it was not intended in the first place when writing this, this back. This was my intention in, 

**Paul Hauner**
* I don't know if I'm just recovering things that have been discussed already, but how attached to are we to that extra ephoc past finalization? I I'll be tempted to argue that if we managed to finalize the chain, then it's time. Then we were, we're kind of out of danger zone in terms of a bunch of weird edge cases with merge and that it's okay just to turn MEV on then. 

**Danny**
* Well, and you could also do plus, and he epoch from point of merge and finalization Or is that hard to pull up to 

**Paul Hauner**
* Having just about, but just based on finalization is super easy. and a epoch is harder, 

**Danny**
* I think From point of merge, not just finalized merge. 

**Paul Hauner**
* Yeah, I think so, because finding the point of the merger is a tricky thing. Sorry, 

**Mikhail Kalinin**
* Aaron clients download the block historical blocks. I mean, like, going back beyond the checkpoint that they've got on the start-up off 16 epoch is like, yeah, it's just five regional blocks. So you may just pull them from the network if it, if it makes sense. I mean, if it doesn't, if it's used for some other things and just look at the block yeah. That boundary, 

**Paul Hauner**
* We do backfill, but the, the, the complex it is, and then saying like, oh no, hold up, don't produce a block until you backfill. That's not something that we have. And it's something that I'd be hesitant to put it in the flow of block production. 

**Mikhail Kalinin**
* No, not, not produce, but just do not use meth ghosts. I don't know. Probably it's comp it's just complicated. 

**Paul Hauner**
* Yeah. I think it's complicated for us, for us. Like backfill is like this thing that we kind of put in the thread and shove over to the side because it's very, independent, so be nice not to link it all through to everything. 

**Mikhail Kalinin**
* Also there are historical blocks in this state. Yeah. But I guess for mainnet can work. So you can just pull the blog by hash, the exact book and just block, get this block. 

**Ben Edgington**
* It seems a little bit missing the point to kind of complex solutions because the whole idea is to make things simpler for ourselves around this. 

**Danny**
* Yeah. I agreed. I I'm, if this requires increasing complexity, that's bad. so I, I would, I would error towards simpler and maybe just, Paul's suggestion. 

**Enrico Del Fante**
* Yeah. I mean, I have, I have just one very easy thing is to simply do a, delay not, not based on the, on the, on the finalization of adjust, adding a delay on the, on the Bellatrix fork, which is there may be easier, but you, then you need to find out the right value that ensure you, that you go after the TTD. And so to be sure that it means that there may be most, will be activated quite later than expected. 

**Danny**
* Yeah. I wouldn't. I think that that pushes us too far in the other direction. 

**Mikhail Kalinin**
* Yeah. I think that there will, there will not be like a huge portion of what it is who has just recently joined a merge, which means that this parameter and this trick works is like more for those or online and stand alive through the merge. So probably if you're a certain new a node from a checkpoint and it has a payloads of that, it's finalized. It's okay. If you use meth boost right. From this one of the beginning. I mean like when the node is ready. Yeah. 

**Potuz**
* The only real layers not to be on What was, that was whether the layer not to be on? There aren't that many layers. 
* And we can just start mev boost on our end, since we are finalized. And just asked to layer of chain, just don't turn on the layer, don't accept anything until 16 ephoc fork after finalization. 

**Mikhail Kalinin**
* And there is a risk of, another layer that will just not agree to follow this item. 

**Potuz**
* Yeah. But it's very minor because anyways, we're analyzing just running this after finalization. 

**Mikhail Kalinin**
* Yeah. And I think if you're a CLS starting out with the checkpoints, probably probably your ELL will be syncing like for the next few hours or whatever, I don't know. Or the nodes will and ready for producing blocks. Why would I? Yeah, my opinion is just in a simple way, if it checkpoint has finalized quite over the has has the payload in it. So just start using that boost, I'm in favor of the finalist thing. I think doing it inside the beacon note is good. The beacon note has the final last state. it's the ultimate control over whether UV boost gets used or not. So doing it, that makes sense. and doing it based only on the finalized state, is something that we know clients always have a it's simple and we don't need to add educations about, did you raise it, you think or not? 

**Enrico Del Fante**
* I do agree. We already doing that and having a finalized execution payloads in any case gives you, gives you a good hint. That network is healthy. 

**Danny**
* Okay. So it seems like there's general consensus on simplifying likely simplifying so that the consensus layer just, those clients can begin acting, we'll begin acting on MEV boost at finalization. There's an additional thing where maybe it's specified that relays relate, wait in the ephocs because they all have the same edge cases around like syncing and resyncing, that kind of stuff. is that a reasonable synopsis? And can we take that to this issue for further discussion? 

**Stokes**
* Yeah, I can update the tr and that sounds like everyone's on the same page there. 

**Danny**
* Got it. Okay. Anything else on this one? Okay. We have 15 minutes. are there any pressing updates, any pressing research spec or other discussion points for today? Okay. Any non pressing updates or discussion points? Great. Okay. Thank you. good meeting and we will be talking about Goerli and configs over the next handful of days and keep the ball rolling. Appreciate it. Talk to y'all soon. Like 

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



