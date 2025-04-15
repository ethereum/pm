# Consensus Layer Call 119

### Meeting Date/Time: Thursday 2023/10/5 at 14:00 UTC
### Meeting Duration: 44:18
### [GitHub Agenda](https://github.com/ethereum/pm/issues/874) 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=US-aOBVsN6w) 
### Moderator: Danny
### Notes: Metago

## Agenda

### Introduction

**Danny**
Okay I think we're live. Great thanks. Welcome to all core dev consensus layer. This is call 119, this is issue 874 in the PM repo, just shared the link. Seems like we have a light agenda today. No one added anything so I made sure to add a couple of things. So on Deneb, if there's any devnet updates, any testnet updates, or discussion, these are kind of the things on the critical path to continue moving forward on this stuff. Actually and we might have quick discussion on timing with respect to forking public testnets because that was discussed on ACDE last week, and it' be good to see if there's any additional people here that want to echo or add some input then we can talk about research spec Etc if there are items and then open discussion on Deneb.

### Deneb

#### Devnet updates [5:31]( https://www.youtube.com/live/US-aOBVsN6w?si=HNFfWy7Y3aDYwEj6&t=331) 

Are there any updates regarding devnets? 

**Barnabus** 
I can give a quick recap of devnet 9. So devnet 9 is now running for six days. We launched it last week, Friday, and we've been quite good at participating. We have 90% participation rate now. We found a bug this morning with r? it was producing in blocks and Besu also has a issue that they're working on right now and there was some latency issues with Nethermind regarding max blob counts, maybe these teams can give an update and bit more details.

**Marcin**
Yes today I performed a spamming experiment like with sending large amount of six block transactions to the theet 9 and in Nethermind we had a back with block building like we were doing too many reads from theb like unnecessary ones. It's already fixed and right now we are building blocks perfectly fine, and yes this experiment with spamming is not finished, like it's about five SK transactions to be sent more so we will see if there will be some more issues. 

**Marius**
So I also did some like manual transaction work for all of the EIPs so I sent some transactions to called the pre-compile, some transactions for the blob P up code 1155 5656 75 15 so all of the everything that is kind of within the EVM, so all of those transactions should be on devnet 9.

So yeah, if you can sync devnet 9, then you should be able to like, it kind of verifies that you have all of these features enabled in it. 

**Danny**
Nice, anything else on Devnet 9?

**Barnabus**
Yes, MEV testing has begun so I have deployed now MEV flood, which will spam some juicy transactions that could be basically harvested by MEV boost and currently it's running on lodestar, but we still don't really see any MEV transactions. There's a relayer run by flashbots now for de night. Here's the URL for it. (https://boost-relay.flashbots.net/) There's still some bugs here and there and hopefully we can resolve it by the end of this week.

**Danny**
Great, what percentage of the network is actually connected to MEV boost right now? 

**Barnabus**
265 out of 1,325.

**Danny**
Cool. 

**Barnabus**
About 20%. I also plan to update the EL bad block generator and to also produce used bad blocks on the execution layer with bad blobs.

**Danny**
Great. Anything else on dev9? 

**Marius**
Is anyone from Besu here by chance?

**Danny**
Doesn't seem like it is. 

**Marius**
Anyone from Ethereum JS here? 

**Danny**
Does not seem like it.

**Marius**
So there's also some issue with Ethereum JS. Sometimes encountering a bad branch in just being stuck on a bad branch but I think they said that they're working on it.

**Danny**
Got it. Fabio?

**Fabio**
Yes talking for Besu since Justin that is following devnet 9 is not here, but yesterday he found a problem with the production of blocks that contain block transaction that after RoR so the problem should now be fixed and but I don't think is deployed in devnet. So this is the status update for Besu. 

**Danny**
Thanks. On the consensus layer side, anything of note going on? Things stable? 

Cool, is there a intended timeline on doing the limited run devet 10 to that'll test 7514, the max inbound activation VI?

**Paritosh**
I think it would be nice to try and do that next week if we have all the fixes for devnet 9 in by then. We can also deploy the B Block generator by then.

**Barnabus**
I would like to see all clients being able to participate and no more bugs really found for devnet 9 before we proceed with the larger test so we should have a very stable like 100% participation before we move on.

**Danny**
Are any of the issues and participation related to layer teams?

**Barnabus**
Please repeat?

**Danny**
Are any of the issues in participation consensus layer issues at this point or is it execution layer?

**Barbanabus**
I'm fairly certain most of it is execution layer yeah.

**Danny**
Okay cool yeah I mean I guess if the purpose of devnet 10 time was solely to test the the queue then it'd be okay to move forward, but I agree that just it tests the queue and does just you know an interesting load test so we might as well if we can, have everyone on both sides.

Okay anything else related to devnets? Mario?

**Mario**
So we added a single test case for the evil Teku scenario, but we are also working on expanding this idea into more test cases. We're planning on writing a tool that will probably help us reach more of the coverage and with the timing of the blobs but this is work in progress, but just wanted to let people know. 
**Danny**
Cool yeah testing updates was the next thing so thank you for the update and Terrence?

**Terrence**
Yeah so I know Sam from Lighthouse brought this up, have we started testing equation block, meaning that a Blob to have multiple blobs on the same index they're equating but they're not slash but we definitely have seen some issues if that plays out that way? So we're working on some features to mitigate this issue but you will be good to test it. I can also help testing it but I don't want to like step on someone's toe, if people are doing that already.

**Danny**
So is this in relation to recovery when there was a bad one or is it's in relation to like dos or both?

**Terrence**
It's in relation to Dos so say today you have a block and then it points the KZG commitment to a block blob but someone send like a duplication of blobs with the same index but the kg commitment is different so the P2P validation filter will filter the second block and in that case you should use RPC request to request it but I guess like some clients don't do that today.

**Danny**
Gotcha. Yeah I do think that some of the stuff Mario's attempting to do in Hive is directionally like this, but more about, you know do you get the messages that you need rather than did you do the Dos mitigations that are going to make you safe. So there might be some complimentary work to do in relation to getting some of these messages on a devnet. Point being is I wouldn't not do some testing here that you think is valuable because I think Mario they're trying to capture some of it but I don't think they're going to capture all of it in. Enrico?

**Enrico**
Yeah I just want to say that the a tle that was I implemented a couple of days ago was just in that direction trying to produce these heavy equivocation blobs so the first block sent over the gossip was the one that is kind of malicious and then just after a half a second the tech web will publish all the blobs side cars and blobs that are correct so in case your client is not able to recover from that is because the first blob that have a bad key a bad proof in it kind of hide the good one coming later and you're not able to recover even by RPC call just later.

So we fixed a thing on our site and Teku now is able to request and recover from that but yeah I don't know how easy is to actually implement and include this in a testnet because I don't know if there are clients that suddenly downcore the a for some reason and simply disconnect from it and since this is the will this will be the only one having the good blobs, you're not able to recover in any case so yeah. That's my…
**Danny**
Yeah so hopefully we can capture the like I see all these messages and I'm able to follow the fork on hive, but yeah I guess in terms of like spamming the network the options would probably be to hardcode this as a pier that can't be Downscored which maybe I think some clients are able to do, but maybe I don't know if that's valuable to put on devnet 9 or in more of an isolated environment.

**Enrico**
Yeah I was thinking also expanding on that I think I realized that while we were doing the validation of the blobs we were not checking that the KZG commitment inside the blob side car was actually matching the one inside the block so while doing the validation we were keeping the commitment from the block and the proof and the blob from the blobs side car effectively ignoring what was inside the blobs side car so everything was going fine, so we should maybe try to build some fuzzy logic spamming with weird blobs that are to capture if clients are correctly discarding these weird blobs because the gossip rules doesn't cover all the cases because the block is not is not available at that point.

**Danny**
Right Mario?

**Mario**
So yeah one nice thing about adding this to hi is that we can probably just keep a like a list of the every single bad blob that we are sending to the network and then we can just go through every single CL client connected to the testnet just to verify that we don't have the bad blob in in any of the responses from the beacon API. I think that should suffice to test what you're saying the yeah the first thing is to get us a way to send actually send these bad blobs into the clients. Once we are able to do that we can we can just simply make the verifications of the bad blops not being available anywhere in the clients. 

**Enrico**
Yeah sounds good to me because in our case I think we could have stored in our database a blob side car with the wrong commitment at the end so by requesting via beacon API those blobs you should be able to get those weird blobs from the DB.

**Danny**
Yeah I was just checking to make sure like blob side car by rout you're requesting by the block rout so you wouldn't actually be able to respond to request unless you actually got the block and then verified that your blobs are correct in relation to it on the blob side car by range. Will you respond to such a request if you haven't gotten the block yet to validate those blob side cars, I would imagine not, but if you could then that might be like a weird accidental send invalid messages around path?

**Enrico**
At least I know we don't serve any of those blobs that are completely in a separated area so it's kind of in a cache and not served at all.

**Danny**
Yeah I would assume that I'm just going to scan this and make sure that we make a note that the availability of the side car in relation to the block need to be satisfied but yeah I would imagine that just the engineering path through most clients would dictate that. Sean?

**Sean**
Yeah so Michael from our team is also working on I guess similar to evil Teku, like an evil Lighthouse implementation, and the idea with it would be that it would like when it's proposing be able to create things that are like mostly valid but maybe invalid in these exact ways we're talking about which would be like a blob whose kg KCG commitments don't match blocks or whatever so yeah just letting people know work on a similar sort of tool that we could maybe use as a node that's proposing so if we deployed it like to a decent amount of the validator set on like a devnet or attack net or whatever that could be pretty useful to like get to a lot of scenarios pretty quick where it's like partially valid? Yeah.

**Danny**
Got it. Yeah just a quick I did look at the blobs by range spec and that it mentions that the side cars must come from their view of the current fork choice and blobs don't enter into the fork choice unless they've been matched up with a block so I it's good. Okay anything else regarding testing? Mario?

**Mario**
Yeah I think I will just share the link to the document that I'm repairing for the blobs here too so everyone can take a look. So the idea is just to keep on adding tests to this document so please just jump in, read what we have written and if you have more suggestions please just comment on it, so we can consider them if we end up adding this to Hive. When we end up adding this to Hive but yeah the main ingredient of those test is basically just having a tool which capacity is to interject blobs and then just send that blobs to the network so we're working on that we have possible solution but nothing is definitive but yeah in the meantime please just add your comments if you have more ideas.

**Danny**
Thanks Mario, can you drop that in, I guess, the all core devs or the consensus layer channel on the Discord with a quick comment just so that people have it out of this transient chat?

**Mario**
Yeah of course.

**Danny**
Thanks. Tim,  so last week we did you were talking about tentative timelines with respect to beginning to for public testnets. I believe there were a number of consensus layer devs there. Do you want to give a quick recap of that, just in case there are additional people in this call?

**Tim**
Yeah so I think last week it seemed like we wanted to do devet 10 and then move to forking Goerli and ideally do that before devconnect so that we can have at least one testnet and potentially some time seeing it live before it happens. So I guess if you know based on what Barnabas was saying a bit earlier around wanting to see the clients run clean on devnet 9 and then launch devnet 10, I don't know how realistic it is to do all of that next week, if we could get it sorry if we could get it done before all core devs, I mean we could then figure out when we want to fork Goerli on all core devs and then I think pretty much if we can't do that then the next CL call. So on the 19th is when we really need to have done it if we want this to happen before devconnect because you know if we picked a time on the next all core devs, then it could happen you know sometime late October like you know two weeks or so after that and then the sale call after that starts pushing into like early November and we probably want to get this done before people start heading out for devconnect.

So I guess I don't know like how the people feel about potentially being ready to move to Goerli and say like a week or two and I think a question as well is like how close to like having everything on master and put, you know packageable all in a release our different clients because ideally if we pick a date you know say on the Thursday then we can have the blog post out on like the Monday or Tuesday so like you know give a couple days to clients to put out of release but it would be it would be ideal for that like stuff is already in master and it's more a question of what we put out then trying to bring a bunch of separate branches back into master and potentially having to spend a lot of time on that. Yeah.

**Danny**
Andrew? 

**Andrew**
Yeah in terms of Aragon Readiness, everything is merged into our development branch so we could release reasonably quickly. I have a question about the key KZG ceremony. Is it complete for production and what do we want to have our proper final KZG set up for devnet 10? If not at least I suggest to do it for Goerli? 

**Danny**
Yeah I think we certainly want it on Goerli. Does anybody Carl's not on the call does anybody have a view into where we're out on that?

**Trent**
Yeah I know Carl's working on it he had hoped to get it into the  previous devnet but had some issues that needed to be resolved and is still working on it with the intent of getting it into devnet 10.

I believe I think maybe Alex was also working on some of it or helping him so if there's anything else Alex please add.

**Alex**
Me Alex?

**Trent**
That sounds like you were not involved? Yeah thought you 

**Alex**
No I was yeah well very tangentially but yeah as far as I know that's on the way. I thought that he had sorted it out but is he on the call? I guess not. Yeah, I can follow up even later today and see what's going on there. 

**Danny**
Yeah I just pinged him too. Terrence?

**Terrence**
Yeah I think my naive intuition is that like I think we're a bit early in talking about like forking testnet or even a testnet schedule like timeline aside, I think like what I would want to see in the devnet before I put confidence since working on testnet is that like we test more like relay infrastructure, which is good today we have a relayer that set up 20% using the relayer but I would like to bump up the number and test that slightly longer and another thing I would like to see play out more on the devnet, it's just the blob scenario testing that Mario was sharing that if we can like run more test through that we'll have more confidence, then again like clients still have bugs today, so I think it's like personally take is that we're still too early talking about like forking testnet. 

**Danny**
Are these things that if you saw over the next week and a half that and things look stable then then it's time to have that conversation or do you think that it's a time horizon that is longer than that in terms of like seeing spam instability around that?

**Terrence**
I think like one to two weeks maybe too soon my take is like two to three weeks each that we should see like improvement but yeah I don't 

**Danny**
Because you suspect that there is going to be stuff that falls out of it you're see bugs in it okay. So I guess we're in the phase where we need to be revisiting this on each of our calls to kind of get the updated status on testing and subsequent bugs so that we don't let it slip but that you have low confidence that especially next week that you're going to be ready to do so and potentially in the two week time horizon we're beginning to get some clarity, but no commitment yet. Enrico?

**Enrico**
And just want to echo what terrence said and also add the fact that I don't think we have tested any interop between clients considering the fact that we have a new block V3 API and Teku is not has not completed the implementation of that yet so

**Danny**
This is beacon node to validator client interop?

**Enrico**
Yeah so if there are out there guys that are having using mixed deployment to run Goerli and well whatever test that we decide to go to, we should have all the use cases so more test on the Builder flow Plus or all the API the CBN API tested has everyone implemented V3. I know a couple weeks ago that was not 100% clarity on that. Has any team not implemented the new methods? Sean?

**Sean**
Oh yeah so for Lighthouse we have an implementation that's unmerged it's like far along but it's not in yet and just to give like a broader Lighthouse status update we're in the process of getting didn't have merged into our unstable Branch but I think we still need like another week to get it in and then after that we'd like to have a decent amount of time before we actually cut a release to do regression testing on that because it's just like a massive set of changes so similar timeline with other teams out there.

**Danny**
Got it. Thanks. Would it be valuable to do a bnbc interop related short-term devnet once people have all of those changes merged? Is that something we've done in the past? How do we usually test that? Have we ever tested that?

**Mario**
So sorry

**Danny** 
Yeah go on.

**Mario**
So Hive is using beacon GL validator setup everywhere so is this something else that we are talking about or?

 **Danny**
Well it's mixing the two, it's mixing two so there's a common API between the two, so I could have Teku be an lighthouse validator and some people presumably do so on mainnet, at least. 

**Paritosh**
In the past we haven't really tested that on devnets, but if there was an issue, it usually spills out when we fork the first testnet because there's like yeah but there's also like a million different combinations you can run everything in, so there's only so much you can test.

**Danny**
Well there’s a very finite amount of combinations. 

**Paritosh**
Yeah once you start adding all the externals as well.

**Danny**
Yeah.

**Paritosh**
Yeah but now we also have the Builder API directly connecting to the relays without MEV boost and we have third party softwares like vouch, so there's kind of the matrix keeps expanding. 

**Danny**
Yeah. Is it worthwhile at least doing some sanity tests around bnbc combos on Hive or is that not a path we should open?

**Mario**
I think it's possible. Right now, its hardcoded so if you start a Teku beacon node, it will automatically start a Teku validator client but we can make that configurable and I think should be easy just to do all the combinations, but given that we are focusing on blobs right now, I'm not sure if we can do this in the next couple of weeks.

But yeah it's doable in Hive. 

**Paritosh**
Actually if we want we can just do this in devnet 9 right now. I don't think it would be overly difficult to change our annual setup. We can just add a bunch of validators and spin up more instances, which clients claim to be ready so that we know who to test for interop?

**Sean**
So all clients still support the block V2 end point right? with Deneb types, DB types? Because we don't have the V3 endpoint in Lighthouse, our validators will only call it V2 though.

**Gajinder**
Lodestar has with three.

**Dankrad**
We have one and we have implementing three. 

**Sean**
Okay we'll work on getting V3 in pretty soon so we can test interop with other consensus teams. 

**Danny**
Yeah and Mario in terms of like the criticality of this getting into Hive I'd say agreed there are much higher and more important things to get in there. I do think in the long run having a few sanity tests that do test these different configurations of bmbc would be valuable. I wouldn't I mean I don't know the load and run times on Hive necessarily but like I wouldn't necessarily run them through like all the tests.

I would run them through like you know Can a ? station be made can a block be made and like call it a day maybe a few others.

**Mario**
Yeah there's one perfect test which is basically just the sanity just starting the N you start sending blobs you see everything works just wait for final session and that's it. So I think there should be that should be the ideal yeah okay ideal one um yeah the problem right now is that is very there are a lot of assumptions in the way that the clients are respond so there are a couple of important changes to be made if you want to do like the combinations, but once we do that, it should be easy enough to prepare this combination testing. 

**Danny**
Yeah let's in terms of Hive let's put this on ice and pick it up in a couple weeks and see if it's can be prioritized at that point. Okay any other comments with respect to testnet planning in relation to testing in relation readiness.

**Zahary**
I would second the opinion that the Builder infrastructure is kind of the most lacking aspect right now.

**Danny**
Okay so we definitely want to wrap that up over the next week or so and to begin to see a lot of messages channeling through their anything else on this one? Anything else related to Deneb? 

Okay, any other discussion points for today regarding research specification or anything else? Okay, great. Thank you everyone, keep give the good work um we'll sync many of us will sync in a week on the execution.

Everyone says bye and leaves. 

## Attendees

* Danny

* Marius VanDerWijden

* Paritosh

* Daniel Lehrner

* Barnabus Busa

* Enrico Del Fante

* Preston Van Loon

* Mehdi Aouadi

* maintainer.eth

* lightclient

* Lukasz Rozmej

* Marcus Edwards

* Marek

* Roberto B

* Spencer

* Saulius Grigalitis

* Matt Nelson

* Phil Ngo

* Ansgar Dietrichs

* Ahmad Bitar

* Gajinder

* Zahary Karadjov

* Potuz

* Mathew Keil

* Dankrad Feist

* Justin Florentine

* Ben Edgington 

* pk910

* Mikeneuder

* Terence

* Pooja Ranjan

* Mikhail Kalinin

* Mario Vega

* Toni Wahrstaetter

* Fabio Di Fabio

* Stokes

* Andrew Ashikhmin

* Marcin Sobczak

* Sean
