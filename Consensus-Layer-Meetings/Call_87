# Consensus Layer Call 87

### Meeting Date/Time: Thursday 2022/19/5 at 14:00 UTC
### Meeting Duration: 1.5 hour  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/527) 
### [Audio/Video of the meeting](https://youtu.be/-6dZVes6aWc) 
### Moderator: Danny Ryan
### Notes: George Hervey


---

***For additional summary and chat highlights of the call, please read the [Quick Contemporaneous Notes](https://hackmd.io/@benjaminion/HyzJna7vc) by Ben Edgington.***

## Merge Updates

**Danny**
Stream is presumably transferred over. If you are on YouTube, please let me know that you can hear us. Okay. Issue #537 on the PM repo. Consensus layer call 87. We'll go over the merge stuff. I've got a couple of agenda items. generally, if we have any other client updates, then a couple of discussions, around some, spec stuff, and then open discussion, any closing remarks. 

### [Testing and General Updates](https://youtu.be/-6dZVes6aWc?t=277)

**Danny**
So on the merge, I believe we literally just had a shadow fork, like an epoch end or something. Does anybody want to tell us what's going on here?

**Pari**
Yeah, I can. we just had the, we just hit TTD for mainnet shadow fork 5. it's too early to say anything, but in the last like epoch, I think there was one or two miss slots or it looks quite good so far. we are doing a few things differently this time around. We have an equal client split. So 25% each EL and 20% each CL. besides that we are running sync tests. So I just paused either a CL or E L and we have one of each combination running for Geth, Nethermind, Besu. I'm not doing Aragon this time because they have some other sync issues that they're figuring out. besides all of that, the ES security team is running some address sanitize or threat sanitizer or memory sanitizer, risk condition stuff. so we're gonna collect hopefully a lot of data at this time around. And I can update us call about finality. that's it for me, the shadow fork. 

**Danny**
Great. Is there a link that anyone can kind of follow what's going on here? Like we usually have with these like block explorer, et cetera. 

**Pari**
Also the, Aragon ones. They have an issue with ETH stats, so that's not really valid data. But the other ones are valid. So if some other client goes offline on ETH, please let us know. 

**Danny**
Great. Thank you. I know there are independent testing calls. I do you know enough of an important effort. Is there anything to surface there to the wider group on testing in general? Okay. All good. 

### [Ropsten TTD Discussion](https://youtu.be/-6dZVes6aWc?t=431)

**Danny**
Okay. Next up is, so on the AllCoreDevs call, which I believe everyone on this call is very likely aware at this point, wraps and it was decided to move forward on Ropsten. There were a few consensus layer teams on there giving the thumbs up as well. there was even a TTD chosen, I believe on the call, but it seems that we maybe need to reconfigure the TTD. Tim, you brought this up. Can you give us the TLDR? 

**Tim Beiko**
Yes. TLDR is we messed up choosing the TTD. slightly longer version is that, Ropsten is, is is the hardest network for rich to predict the total difficulty value because the block times and the hash rates are, are quite unstable. so we, we, we made some new estimates now and we think they're better, but then the risk is, you know, the risk with choosing the TTD is like, if we choose one that happens before Bellatrix that's really bad. so we, we, we, we were aiming if the Bellatrix is on like June 3rd, we were aiming for June 8th. That there'd be the TTD can do either. We keep this you and be like massively increased the hash rate on Ropsten a week before so that we kind of hit it quicker. it seems like that is doable, but it's still like a lot of hash rate. And then we, we kind of updated the model, which, which, which, which predicts the TTD. And so the other two things we can do is, either we, we pick a new value that's much lower that we now think is actually going to happen on June 8th. and then the risk is like, if we're wrong, again, maybe it happened sooner. Or the other idea is maybe we pick a value that we think might happen more like June 15th and then, a week before hitting it, we start adding way more hash rates to the chain so that, we, we hit this like June 15th, one on June 8th, but it's still lower than the one we currently have. So it just requires less hash rate to be added to Ropsten. 

**Danny**
What is our ability to add hash rate? Like, do we control hashes on the order of like 50% of what's on there, on that network or something? 

**Tim Beiko**
I think someone on our team checked that yesterday. Marius, do you remember? 

**Marius**
Yeah, so we can, we can add, in a hash rate, I think. So in the order of like one giga hash. 

**Micah Zoltu**
I guess, is that all we need to fix this as like one giga hash or? 

**Marius**
At least according to the calculation that I did, like some days ago, but 

**Micah Zoltu**
Over how long, like a week or a month, a day? Until TTD until, 

**Marius**
Until TTD. 

**Tim Beiko**
So from that, so right from now until TTD. 

**Marius**
Adding what sort of having Ropsten on one giga hash would hit TTD at the required point 

**Danny**
And that, so that's option one. We could also change it and then turn on the hash power a week before. 

**Tim Beiko**
And yeah, Marius, you have a comment saying the new estimates are worse. What do you mean by that? 

**Marius**
Yes. So I just ran the, the estimates, the new TTD estimates from, Mario. And, they should be hit either on the 24th. So in five days on the 28th. So in, nine days. So 

**Tim Beiko**
You saying they're too low? 

**Marius**
There w yeah, too low. 

**Tim Beiko**
Okay. 

**Danny**
The 43 numbers were too low or an updated number, 

**Danny**
The 42 one way too low. 

**Tim Beiko**
Okay. And so basically what we had was 43.5 or 4, 4, 3, 5, originally. So I mean, yeah, the option, if we, so I guess one thing that would be helpful to know is like, beyond the EF, are there other people who can contribute hash rate if we leave? might I mean, we can probably scale a lot of it. 

**Tim Beiko**
Yeah, 

**Tim Beiko**
Yeah, yeah. 

**Micah Zoltu**
Printing is super easy. Like it's a couple of clicks. You just spend some ETH a 0.015 ETH per day will get you a gigahash. If you only need a month, it feels like the amount of money spent on this call is like strip that cost. 

**Marius**
Yes. I think, I think that's the way to do it. 

**Tim Beiko**
Okay. So we keep the value, but how do we make sure we don't add too much hash rate too soon and then like, how, how do we tweak this basically? 

**Marius**
We always start, we started adding hash rate, once other clients have updated the images and then we don't care. Okay. 

**Danny**
When is the Bellatrix fork? 

**Marius**
June 3rd. 

**Danny**
Okay. So waiting, waiting a week from now or a week and a half from now, and then maybe renting more power if we need to is a bit safer than like cranking on it right now. 

**Tim Beiko**
Yeah. And one thing that would be neat, that was neat with the June 8th is like, it happens like a couple days before all core devs, so it would be neat to have the fork happen a few days, and then we can kind of see how it went and discussed what we want to do next on the calls. And it's not the end of the world if we lose a week. Cause it happens like say on the 10th, but it would be nice to not lose that week. 

**Danny**
We can also, rent four gigahashes instead of one. 

**Tim Beiko**
Yes. 

**Micah Zoltu**
Someone should double check my numbers on that. Make sure I'm correct. I am not a miner. I'm not a professional. I, I believe those numbers I might've mentioned are correct, but I might be like off the orders of magnitude. So someone double check me. 

**Tim Beiko**
Okay. I will look into it though. I, I sort of assumed you couldn't rent nice hash for testaments. That's like, I'll, I'll look into it or whatever. Yeah. I know it makes sense. 

**Marek**
I, yeah, just my brain, but yeah, I'll look into it. I think we should check block production on MSF mean a shadow fork five, because something seems to be wrong, unfortunately. 

**Pari**
Yeah. I think we're hitting the issue we had in the past where we're hitting time outs. So blocks are being produced and we're going to finalize, but transactions aren't included. 

**Marek**
Only active blocks. And we, for example, Nethermind is producing currently with, quite faint composter, lots time team was so the clients come that are seeing that they're not giving us enough time And all clients are producing empty blocks. 

**Enrico**
Yeah. So Lazzara has an ongoing PR for this store dress maybe next week. we'll be able to address and issue FCUs ahead of the time so that ELs can make blocks. 

**Danny**
we do know that Geth switched to also have the async, but I didn't, I wouldn't suspect that, The clients that we're producing blocks with Nethermind previously would not be able to produce them with Geth. So we might just be seeing a higher percentage because of the distribution now, the even distribution, but it might be just the same known issue. I guess let's get the percentage, but we can keep moving on this call by some people will, some people investigate. Okay. So we are not at least currently the people on this call think that we should not adjust the TTD?

**Mehdi Zerouali**
We're happy with all options. what house perspective. 

**Danny**
Okay. So right now we won't adjust TTD and we'll probably readdress this in one week on All Core Devs, Tim. 

**Tim Beiko**
Yeah, it sounds good. And I'll look into getting set up on nice hash and, yeah, we, we, we can also look at a bit year for about setting up some miners, on our own instances and, yeah. 

**Danny**
Cool. Thank you. Any other merge related discussions for today? 

**Pari**
Oh, when do we expect, client releases with the Ropsten update?

**Terence**
Prysm was planning to release on the weekend before that. So maybe next Thursday, Friday, we will have a release. Yeah. 

**Mehdi**
For, for Lighthouse, we'll have, we'll have this by the end of this week, early next week. We're just working on getting the, a significant measure later changes in before the actual upgrade to get as much testing as possible. I'm pretty confident we'll do this center. We'll also add our footnotes to match testnets repo. 

**Ben Edgington**
Oh, Teku will be early next week, Monday or Tuesday. 

**Pari**
Awesome. Thanks. and just to reiterate, that was one change since the PR was created. So please, to make sure that you're on the version that was merged in. Like the channel sse file and Genesis delay. 

**Arnetheduck**
Yeah. Nimbus,  same thing there. We just did a release today, but we're going to do a small point release just for Ropsten next week, sometime. 

**Danny**
Great. 

**Mikhail Kalinin**
on the same topic, we are expecting spec releases as well, right? And like engine API and consensus spec. 

**Danny**
Yeah. I believe like a release candidate on the consensus specs. and then I don't know how I know the engine API, the execution APIs have been alpha releases, so it might just be another alpha release. Yeah. I need to do a bit of cleanup. I was doing a bit yesterday. I think we're in a pretty good spot on the consensus specs and, try to get that release candidate out tomorrow. I, I, it's not necessarily meaningful other than just kind of signifying this is what's going interrupts them. I don't think there's really changes for real. Okay. Other merger related items for today, any update?

**Terence**
Beyond Ropsten, we're also working on a few blog posts on POTUS stirrups and beacon node, how to use the recipient and stuff. I'm wondering if there's like an effort for more general blog posts on just how to launch Ropsten beacon nodes so that, so that we can point our blog post to that one. 

**Danny**
Tim you've been working on a rough, some blog posts. That's going to have some of the details here, right. Or at least the high points. 

**Tim Beiko**
Yes. I was looking for something to link to for people who wanted to launch a Ropsten beacon node. So Terence, if you have that blog post ready in the next, like, I don't know, like before midweek next week, I would happily link that in the EF blog post. Like it says, it basically says like generally what people need to do, but it doesn't run through actual, like how do you do it step-by-step? So if you have like a good, like a good thing there, yeah, that, that would be really, really helpful. 

**Terence**
Awesome. Thank you. 

**Danny**
Is Ropsten blog post going to, it's going to reference the fact that you should set your favorite recipient so that people are used to that, but not like point out how to do each one. 

**Tim Beiko**
Right. Because if, yeah, exactly. That's like a good example because each client like implements, you know, few recipients differently, it says, you know, look for a fee recipient value in the configs of your clients and make sure you set that, but it doesn't go through like, here's how you do it on Nimbus and Prysm and my titles and Teku. 

**Danny**
Okay. Other merge related items? Okay. I do recommend maybe jumping, having someone on your team jumping to all core devs next week. It just seems like over the next four to six weeks, there'll be relevant conversations happening in both these calls. 

## [Other Client Updates](https://youtu.be/-6dZVes6aWc?t=1308)

**Danny**
okay. are there any other client-related updates that teams would like to share today? 

**Mamy**
So, you also mentioned, Nimbus release, we have a couple of interesting updates for the release. let me check release notes. Sorry. Yeah. So we have like in prod now, the proposal boosting we have faster, stop, you reduced to be usage as well for, when clients sync with, Nimbus. and we had some focus on web3 signer. normally, we have better compatibility with all. And, one thing that we released, is, BRS, trust hold signatures. So the idea is that now, especially staking pools can, have, signing keys that needs to be, like you need five out of eight or something. So actually sign a block on that dissertation and this, so that they don't need to give, the full keys, to where, system means, or a DevOps team, which is one of their concerns. Once they have a fleet with, millions of dollars, a disgruntled employee could, cause issues there. so that's it for Nimbus client itself and otherwise, we have, the light client protocol. We made some progress and, varies, at Dan who's working on, on the spec and implementing it at the same time. You can look at it in the, related different and repo, and also will still, trying to push, an implement MEV and MEV boosting for the consensus layer. 

**Danny**
Thank you. Any other updates? 

**Mehdi**
Yeah, I can go next for Lighthouse. we proposed the PR to the beacon API spec to prevent production of, at the stations and some contributions to optimistic blocks. So it's PR 216 on the beacon API's repo. we don't really expect this to be controversial, but, kind of want people to be aware of this, since it's a pretty significant important change that would essentially allow us to prevent finalization of invalid execution payloads. So please take a look. we've also made our discovery, IPV6 compatible. we essentially decided not to enable this until after the merge, but it's ready. we've started specking and implementing, EPI sub prototypes. So academic meshes for gossips, see as a significant upgrade to a gossip sub. we started working in implementing the fee recipients, method for the validator clients, from standard key manager API. And, that's pretty much it on the clients side, but, you've probably seen, Michael has done a bunch of work on, on block Printful client diversity metrics. check out his tweet if you haven't. 

**Danny**
Thank you. Other updates? 

**Enrico**
I can go next for Teku. So we, work the, we, we have some additions for that upcoming release for the next week. some of them are early to, to our rest API framework that becomes, we are, we are moving from, from, from, we are changing our internal framework to be our, to be a little bit more, optimized in term of memory consumption because we are now able to streaming stream JSON starkly to, to networking. So we have less memory pressure when we are dealing more, mostly with bigger APIs that, that streams, for instance, states with usually very big objects. So a big win for, for Infura for instance, and, we have some optimization on the DLS batch, very much validation for instance. And, we also have additional, optimization on the, a, on the event, a rest API events. We still on a memory pressure on that side, the greens there. And, we also implemented the ETH1 checksum. These are good, has been good, a good contribution from an external contributor. So we are now applying check sum on the ETH1 address. This applies to Infura even for instance. 

And, we are still, we are working on the builder API when today we had a very interesting results, first successful testing around builder APIs. So we are now being able to run the beacon, blinded the rest API flows, plus builder, get header and get payload APIs. They are working, and we are also falling back with our local execution client when things that goes wrong on the build side. What is missing here is, is late registration signing and builder bid validation. So you get to the validation, but yeah, we are, we are, we are close to having everything implemented on that side. And that's it. 

**Danny**
Thank you. Anyone else? 

**Terence**
I can go next. So, Prysm released a version 2.1.2 last this week which Incruse go 1.18.1 also has a few important, but fixes a few optimizations. Aside from that, we're just catching up with dispatch hinges. We are also working on saving blind block instead of saving full block, meaning that the execution halo will be header. Hopefully we'll see reductions on the DB size on that. And then I'm also working on, do their API implementation. We are done with implementation right now. We're in testing with the merge mod trying to write some sort of end-to-end tests and on the UX side, we're working on config and Clive for usage to specify, Geth did made. And then the, and then the desired, a builder fee, the builder fee recipient. And they also, we're also on the background. We we're working on EIP 4844 with the, with the, with, with the optimism team. And then we also have, two new hires they're just joined us. So, make, will be our, type a full-time, type writer. And Samantha is our new Onpro developers. So, yeah. Welcome to those guys. 

**Danny**
Great. Thank you. 

**Cayman Nava**
I can, I can speak quickly to Lodestar. Cool. Last week we released version 0.36 and a few goodies. we have validator metrics in the validator. we, I believe that also, we also include proposer boosting in this release and we also fixed a security vulnerability where someone could create, malicious, but valid slashing at a very, very high slot number and cause Lodestar to have a consensus split as that should be fixed. Upcoming, we're going to be implementing the light client, spec along with Bhutan, and, getting ready for an audit of our code base and hopefully subsequent version 1.0 release, next month. 

**Danny**
Sweet. Thank you. Anything else? Any other updates? 

**Saulius Grigaitis**
so we extended the signer support multiple signers and keys loading and things. And also we started to work on the custom task handler through blaze dairy, and that we use a call privatization, as soon as we, we optimized for eight to 16 course CPU for CPU's with just a few porous or a lot of course, like 52 or so, the performance should be better than it is now. Also we are working one on this customer and they'll also include, memory consumption, which significantly decreased. It wasn't high previously but  now it's even smaller. So that's all. 

**Danny**
What is your main net memory consumption look like if you don't mind me asking? 

**Saulius**
I don't know, actually, actually I, talked to [NAME], from a superfluid computing last week or week before, and I think they have these graphs, but, but to spread the low now, I don't know, it's like a couple of gigs or something like that, not that high. 

**Danny**
Okay. any other updates? 

## [Research, Spec, etc.](https://youtu.be/-6dZVes6aWc?t=1931)

**Danny**
Great. Moving on research spec and otherwise. I actually don't know what your name is, but our we're 13 is here to talk about, essentially exits a method to initiate exits from 0x01 credentials from the execution layer. 

**Artyom Veremeenko**
Yeah. Could we please move the discussion to the last 30 minutes of the time while my, to my head want to join and then he will be able to participate as well? 

**Danny**
We can definitely talk about step deprecation and anything else, but I don't know if we're going to make it to 30 minutes from now. but let's yeah, let's jumped into step deprecation. 

**Artyom**
Okay.

### [Step Deprecation](https://youtu.be/-6dZVes6aWc?t=1978)

**Danny**
This has been up since March 18th. I'm pretty much looking for any final feedback on this. I believe everyone was generally fine. I think maybe only one client team is utilizing step in one edge case. but it's not really utilized. And the goal here is to reduce some complexity and have a backwards compatible way to do so. I guess putting this on a final call, we don't have a process here, but, I haven't, no one said anything bad about it. I think that we're intending to just move forward. This is the specification. Is there anything else you want to discuss on this issue before we merge it and getting there release? 

**Arnetheduck**
Since I wrote it, I can note that there is a very similar PR coming up for the beacon API as well, which basically allows the consensus client to implement, both by root and by, Grange requests, with mirrored API calls in, in the JSON RPC call. And that one doesn't include, a step parameter let's say yet, because I kind of assumed that this PR will get merged since nobody complained so far, but the two things are related. So the point of simplifying this right now is that, there's an actual reason to do so. It's not like, yeah, it's not just a fun change. 

**Danny**
Right. And the I'm going to toss this other issue in the X and the engine API on, onto maybe on the All Core Devs next week, just to make sure that, execution layer clients have taken a look at it. I know that there's been a little bit of review in general positive, and it enhances, you know, a feature that Lighthouse has already built out using the standard ETH API. I think it's likely a no brainer as long as we get thumbs up all around. 

**Arnetheduck**
Yeah, I think, I was just briefly outlined, the one thing that I see as an issue or as a discussion point in that PR, and I can repeat it later in the All Core Devs. But, there is the question of whether EL should support both by hash and by range requests. And then by hash requests, they're kind of mandatory in order to grab, forks or non heads, whereas range requests are excellent for, for the canonical chain and finalized data. but strictly the range request is an optimization. So in, in the beacon API spec, it's done in a way that ELs are free to not implement the range request and then CLs should fall back on root requests. of course, if everybody just agrees that range requests are absolutely fantastic, we can remove the optionality from there and simplify the CL as well to not have this, fallback logic, right. That's, that's kind of like an open question. 

**Mikhail**
Got it. But we need this by root request as well, right? Or by hash witholden by hash requests. 

**Arnetheduck**
Yes. We do. 

**Mikhail**
Requesting non-canonical. 

**Arnetheduck**
Yes, we do. We do need both. So it's a question of, do we mandate both requests to be implemented by the EL or do we say that only by hash, which is the more powerful request is mandatory and then the range request is optional and not an optimization basically. And this is really done to, I think, the implementation effort in ELs because obviously not having this fallback logic, because it's more simple on the CL side. 

**Danny**
Great. I did just toss it on All Core Dev agenda for next week to get some visibility. You also could, you could join. That would be helpful. 

**Arnetheduck**
I will do my best. 

**Danny**
Okay. Is anyone against this step thing? I'm going to drop it in the, I'm going to drop it into consensus dev chat and ask for any final review and we're going to merge this thing and put it in the release. 

**Arnetheduck**
Yay. 

### [Shadow Fork Update](https://youtu.be/-6dZVes6aWc?t=2298)

**Danny**
Yay indeed. okay. It has, we've managed to kill five more minutes. Are there other things that people want to discuss today? How about, just a quick update on, the shadow fork? It looks like things are going well, and we were just confused by how block explorers are importing things. 

**Pari**
Yeah, exactly. So the Explorer seems to be running into some issue where it's failing to import a slot. I'm not sure why it's complaining, it's an invalid chain ID. so it's just listing every slot as zero transactions. The slots actually have transactions and you can query the note and check the slots. So in general, we have a really, really good shadow fork with an equal client split of a possible 97% participation. We're at 97%. so essentially no client combination went out of sync post-merge. So we survived the transition. the missing 3% was related to an unhealthy shutdown on Besu, and that happened far before TTD. So it's completely unrelated. we are only running Aragon with Prysm right now, but that combination is working. Yep. That would be the update from the shadow fork. Congrats, everyone. 

**Danny**
That is fantastic news. So the race conditions with the async calls, were those patch? 

**Pari**
We still need to check now, there are transactions, but we're not sure if there are transactions in every slot. We still need to check that. 

**Danny**
We would expect based off of the block service data. I think we would expect it would start to still be having the empty ones. 

**Pari**
Exactly. I think some kinds didn't patch them. So if there was before they'd likely be about after. 

**Danny**
Okay, fantastic. Excellent. Okay. We killed three more minutes. Can we discuss this? We can also discuss it on the next call. If you do need, your coworker to join then. it's up to you. Alright. And before that, any other discussion points that anyone has for this call? 

**Saulius**
Sorry. So the reason discussion, so the deficit, the deficit functionality in teams, teams would like to, to change it or kind of get it, or the current approach, is it like, is it, is it near to count something in a, in the next term, or this is just a, somewhere in the far future? 

**Danny**
We could certainly entertain entertain it for Shanghai, Capella. It's probably like if we have a low complexity path, then I don't see much issue, you know, we'd kind of be debating whether it's just kind of worth the time at that point. I do personally believe and, you know, I haven't expected out or explored it fully, but I believe you can just likely reduce the follow distance to one, and make ETH1 data of validity condition, such that you toss out blocks with bad ETH1 data, this you could use existing end points on, the ETH end point, or you could potentially EL escalate or elevate this to the engine API to reduce the dependency on ETH endpoints. obviously then you still have kind of the machinery of having to get the deposit side of the EL and stuff. you could also elevate that into an engine API end point. So there's a, there's a number of like little design considerations. My PR if we do want to prioritize getting shortening that distance, I think that the most straightforward way is to, just reduce the follow distance to one and kind of deal with the implications of that. But, you could certainly also probably do a bit deeper redesigning and get maybe a more elegant mechanism, but then it's debatable as to whether it's worth the complexity. 

**Ben Edgington**
I just to clarify, by more elegant, do you mean removing the voting process and all of that? 

**Danny**
Well, by re by eliminate, by reducing the follow distance to one, the voting process just becomes one of one and it's safe as long as there's a validity condition on the block for ETH1 data to be correct. So I think that that's, you could potentially like more tightly couple. You could probably get rid of ETH1 data. You could make the engine API returned deposits, and maybe get rid of some of the Merkle root processing. I don't know. I just there's. I imagine if you are more willing to redesign, you could probably get rid of some of that other stuff. But I think the most straightforward way is to reduce the fall distance to one, have it quote a voting of essentially just one slot and make it a validity conditional so that it's not actually voting. 

**Mikhail**
There was a good point, bad train in the chat that the dip makes it sync we probably won't be able to just very, know four, verify it's data, like since Kronos incent, Kronos hashing. 

**Danny**
So I think you'd have to add to all this optimistic as well. If you couldn't get anything, you really can't fully verify that you're depending on the execution layer for would throw it an optimistic. 

**Mikhail**
I think that you mean that's skipping the verification of deposits, like in the optimistic sync node. 

**Danny**
Right. I see how that's dangerous. 

**Mikhail**
Yeah. That's dangerous. 

**Danny**
Is that what's happening already? Yeah. I guess it's not happening because they just, they assume that the voting threshold is safe enough, so it's not throwing an optimistic. 

**Mikhail**
Right, right. So, yeah. W it's going to be easily imagined. That's an adversary. We'll just use a lot of the big deposits in recents. It's like a portion of stake. And for someone like, I dunno, sync with the chain and optimistic mode. Yeah. So it's definitely like a kind of attack and new attack vector that we will have to deal with that we ideally don't want to deal with and be, yeah. And what's possible to do is like, if we have a logical very quiet and miracle group, that links the deposit route to the stage route of the previous walk, for example, but that would require like constructing this kind of route and also verifying its own CL side. Not sure if it's something that's seal, they respond to it, but yeah. That's like, that sounds like a decent option from, from a lot of standpoints.

**Danny**
Okay. So I, yeah, I agree that it does open up an additional potential path attack or like heightened attack path. If you're an optimistic node. It's easier way to get keys in there to try to finalize the new malicious. 

**Mikhail**
Yeah. I also think that we can easily set. This is like it needs more rigorous analysis, but I think that we can use ETH1 follow business parameter to one, and preserve this, you know, walled in periods of sizes that have it now, but I'm not sure it's like a huge UX improvement that we want to make. That even worth making. 

**Danny**
I do challenge the, this actually making it much worse because you still have, because everyone's using this as a validity condition, you know, in optimistic mode, you're essentially like, you're kind of in like honest majority mode on execution layer validation, because you're following the fork choice and finality of the people that are voting. And so if this is a, that doesn't really change much, if like, if you make this a validity condition, you're still relying on everyone's attestations and finality votes. So you're still in the kind of this honest majority situation. it's just what that highest majority can do to you is slightly heightened, I suppose, Or dishonest majority, sorry. 

**Mikhail**
Yeah. But yeah, but I think that reducing the distance is we have this large ETH1 follow distance now to protect ourselves from reorg with one chain, right? And we will not have this problem post-merge? 

**Danny**
Yeah. 

**Mikhail**
Because the chain that you're so definitely options here, that's, I'm not sure that we want to dive deeper, like to, to like tightly couple ourselves to the Merkle proofs considering that there is an upcoming, Merkle tree upgrade. So think about it. 

**Danny**
I will say that if anyone's inspired and wants to kind of try to specify a minimal complexity here, option here that would, help with considering it, right. Like right now it's just a few potential ideas. and we, if we're going to consider it for Shanghai Cappela, we need to get a concrete proposal, you know, in the next some chunk of time, I don't know what chunk of time that is, but, sooner better. 

**Saulius**
Is the goal to speed up addition to validators to the state, or this is not a goal? 

**Danny**
So that would be the goal of the feature is that this follow distance does not actually potentially really bias anything now that these systems are more tightly integrated. And so we can probably eliminate the follow distance if we specify properly. 

**Saulius**
But this there, is there a kind of need for adding the validators at the higher rate? 

**Danny**
No, I think that, I think the argument is there's probably no need to do it at the slower rate technically, so you can improve UX. It's only a UX thing for onboarding new validators on the order of a day. And so I would like if this was going to get in the way, if this was going to decrease increase ship time or get in the way of something that's very critical, then, you know, I could see it not really hitting the priority list. 

### [0x01 Initiated Exits](https://youtu.be/-6dZVes6aWc?t=3026)

**Danny**
Okay. we have, I believe killed the amount of time we can kill. Do you want to talk about the 0x01 initiated exits? 

**Enrico**
Yeah. Thanks, with your list here now. So that's great. first of all, we've got a question. what do you think, but, with the withdrawals enabled, it's important to, add capability to have withdrawal credentials initiated exits. we've got some opinions on the forum, on the topic related to the withdrawal of credential exits waste on a generalized message bus. for us it seems more or less, important from the perspective for any delegated staking solutions. when, where, if, and the stakers and the pool are not, capable to withdraw the funds, that's the validators, which are ideas that are trustless are capable of holding the funds hostage. so the first question is whether somebody considered this important to try to add alongside with the withdrawals. 

**Danny**
So I, I personally do think that it is weird and potentially bad, in the construction right now that the ultimate owner of the funds, the person who has the withdrawal credentials, which often could be the same person or not the same person can not initiate an exit. so then you do certainly have in any sort of, not even on chain delegated mechanism, but, any sort of split there, you have a hostage scenarios that could happen. and so I do think that having withdrawal credential enabled exits is likely a good feature to enable. I do think that in Shanghai, Capella, that we're going to be doing this kind of like cross yell stuff to get the withdrawals enabled, and probably learn a lot as we do it. And, I don't know if we'll have the kind of complexity ability to do this other feature. But I'm happy to kind of defer to others on the engineering complexity. I do think that I questioned whether we need a generalized bus. I, I don't think, 0x01 credential rotation, actually should be handled by the, the consensus layer. I think that this, you know, we have smart contract wallets like, you can certainly rotate control over these things, in, in the mechanism rather than having to have this as a programmable mechanism. And then all of a sudden we only have one message that we need to send. unless you predict other messages that we need to send that I don't have a list of them. Are there other messages that you think that execution layer will need to send to the consensus layer over time? 

**Vasilly**
I honestly think that, right now, and like for the foreseeable future on the, the, for a withdrawal credential initiate segments other ones because like you don't meet with current proposals. You don't need messages for, for the part of withdrawals and, visit all the credential rotation is not super important. Like, even the, for we wanted it. you, you, it's, it's not the priority yet, like at all for now, and it's not clear that it's needed. So I think, there is only one message that needs to be passed, but it still needs to be passed, in some way from the execution layer to the beacon chain layer. 

**Danny**
I kind of think we should maybe do the deposit, followed us since reduction exploration and kind of keep in mind that we have another potential message to pass in and see if these mechanisms can be very similar. 

**Vasilly**
I mean, we already have one message by some mechanism. It's the deposits. so, 

**Vasilly**
Yeah, so like a GMB is designed like almost exactly like deposits, but generalized. 

**Danny**
I also think that we do need emptied DOS mechanism beyond just people having to pay fees in the execution layer, because being able to grief these mechanisms opens up, I think we can easily avoid people being able to agree for these mechanisms. And so we should, deposits are naturally rate limited to a certain extent because it costs them in the middle of one ETH. I think it would be best if these were rate limited as well, but likely the only way to rate limit them would be for the execution layer to have some view into the consensus layer. Like if you had the deposit route exposed, you could ensure that just one only one validator could submit one of these ever. but we don't have that ability yet. So without that, I don't know if we have an anti-DOS mechanism. 

**Vasilly**
Yeah. It, it can be implemented with, like basically orging the Merkel. The tree for the state tree for from beacon chain route for the validator. So like you saw the kind implemented right now. but it's going to be brittle because like, not very, not very beautiful, honestly, because, you need to assume a lot of things about internal structure and the beacon chain layer on the execution layer. And that just adds complexity. I think that, like, if we can manage this stuff with just fees, we should manage to start with just fees because it's makes, a much, much, much less complexity here. And the systems are much less tied up, like execution layer knows nothing about the beacon chain layer and that's, simpler to understand. And, the reason about, don't have to drag the changes on, on the beacon chain layer to understand the, if you, if you need to remake something on the execution layer and stuff like that. 

**Danny**
So it was just fees though. I can arbitrarily block 0x01 initiated exits?

**Vasilly**
Yeah. For like, for very high price, basically. 

**Danny**
Well, sure. High in relation to wherever the market is at the time. Yes. 

**Artyom**
For me, it seems to depend a lot on the ability to, to do, the number of checks for the related to, consensus layer clients. And for me, this is the most, mysterious part, like for, voluntary exits. There is limit 16 And it's 16 because it, because it's because it's, it's the limit, not for the amount texts buds, the limit for the amount of facts. And this is a K, but the check itself, seem to be a much, much cheaper. And as, we could make the, now 100 of them maybe more. This is maybe a question, to the client teams and, the price of the attack, depends a lot on the amount of the checks we can afford. Like maybe if there is enough room for the checks, in a block, then, it's enough to make the attack price large enough, even without, checks on execution layers, specific checks. 

**Danny**
Yeah. So the number's going to cost two things to the beacon chain. One is size of blocks and two is computational overhead. so, but yeah, I do see that if you could afford to put a ton in there, then I'll you make the, the cost of the attack to be sustained even higher. 

**Artyom**
Why, why does it influence block size? 

**Danny**
These messages are included in the block. 

**Artyom**
only the valid ones. The point is to make the checks before they are included. As far as I got it. Looking at the deposits implementation, There is a part of execution where the deposits are cast and the deposit requests, events, the deposit events are cast and preliminary checked, and all them, they get into the block structure. So the idea is to make the checks along the way. 

**Danny**
I might be wrong, but I believe all deposits including endowed ones are included, so that anyone can fully verify and to ensure that they're also processed sequentially. 

**Ben**
Yeah. 

**Danny**
Yeah. I think the tighter coupling between the execution layer and the beacon chain, you might be able to bypass that. That might be an artifact of assuming beacon chain belt people operating the beacon chain. Maybe weren't didn't have access to an execution layer or the proof of work chain, but, my intuition is you would likely want to include them all on chain. especially if somebody, if you don't include them all on chain, then you have these modes where I can't be a, I can't run a full beacon chain and a light execution client, all of a sudden or something like that. 

**Vasilly**
Yeah, so, so we, we, are out of all depths on understanding the costs, of, like implementing this on, on consensus clients. That's why we need like a lot of in the client and we have no intuition about like how costly is, checking the for example area or in the data structure and checking if the, address, in it is the same as an address from the exit, message, for example. 

**Danny**
So I think your primary costs are, again, going to come from the size of the blocks, assuming that even invalid ones need to go in the blocks and, essentially, and then computation at that point, the reads from validator structure probably going to be relatively low cost computing, Merkle proofs, if they're Merkel proofs these might be a higher cost. There would need to be any signature because the signature it's just whether it came from the 0x01 address or not. 

**Vasilly**
Yeah, there is no cryptography, they're just regen and check in and like, and place in the block. So, yeah. the, the, the, the, the block size can be priced easy enough with a like extra fee on, on the execution layer. 

**Danny**
What do you mean? 

**Vasilly**
Like, we can, we can, we can do a smart contract that like, charges, extra either the work 0.01, for example, something like that. Yeah. 

**Danny**
I save a minimum of costs regardless of gas costs. 

**Vasilly**
Yeah. It can be tied to gas price that can guess price as well. it's fairly easy to implement like the, the cost on execution layer if they are simple to calculate, we, we can use arbitrarily here. 

**Danny**
are there any engineers or other people that want to train them on this? 

**Ben**
I'm a bit concerned about how it changes existing norms. I mean, the all current staking services have been built, assuming that this functionality doesn't exist. And whilst I agree, it seems like a good idea. we don't want to break anyone's, model at least without giving them a chance to, to change things up. 

**Danny**
Yeah. I fluctuate between agreeing with you, and then also considering the current functionality as a bug. 

**Dankrad**
What, what could break? I mean, can you give an example? I can't, I just can't see it. 

**Ben**
Yeah. I don't know. I just don't want to make assumptions, so we should, we, we should do some due diligence at least, and then satisfy ourselves that actually, this, this is fine. 

**Dankrad**
I mean, the, the, like the idea to do this has been out there for probably longer than we have, even at the beacon chain. And I don't think I have seen anyone ever say that it breaks anything. I dunno, I can't see it. 

**Micah Zoltu**
How many third party staking services are there that potentially might break? Like, is it three, if so we can just reach out to them and say, Hey, we're looking at this just FYI, or is it hundreds? 

**Vasilly**
It, if we're talking about like, on chain stuff, like, like the rocket pool what stake fee does, like there is about, I think six and none of them are relying on that. and I think Lido and RocketPool, I actually rely on, on this, being, included some point, like not reliant, but, would appreciate, and for, for staff that is not public another dice, I honestly don't know, but there is, I think there is a regular, contract, stuff that like a Staker has a contract with an operator and the sort of thoughts in the, in the legal field. 

**Yoav**
Currently, all of them may seem to be upgradeable proxies. So the old reserve, they all reserve the right way to upgrade them with one contract. So that shouldn't cause an issue. 

**Danny**
Well, then I know there are some centralized staking providers that do offer this split to some of their customers. but again, I have a hard time rectifying the key like that, the customer, if they want to exit and the, their operator isn't initiating an exit and they initiated an exit on themselves by themselves. I don't. And again, that's not 0x01, but I think if you do put this for 0x01, you consider putting it for 0x00 as well. and it's hard to imagine that the ultimate owner of the funds, which is the withdrawal credentials owner, not being able to exit is a good thing. but I doing diligence is a good idea. I agree. 

**Yoav**
No, I think it's, I think, I think, we do need this capability. It does sound like a bug, if you can't initiate a withdrawal from there full withdrawal with the wallet address, but, then, but then, it exposes us to another risk, which I wrote on the chat that, since, a central contract, like the one from Lido could, could get us to, could get us through to a mass exit situation. If there's a bug, like, you know, where suddenly, if a field of the validators exit at the same time, that could become an issue. So we would need to rate limited at least. 

**Danny**
And it, it is, exits are railroaded. 

**Dankrad**
That's different from current exits. I mean, that, that's the same problem already there, right? 

**Yoav**
Yeah. Yeah. It just, it just makes this problem even, even worse because eh, a single operation in a single operation in a contract, could, could cause the same mass exit, but if it's rate limited, then there's no problem. And it's already recommended now so just to make sure that way. 

**Danny**
Yeah, I think in general, we just, it does open up the attack surface for, you know, what people can do if they, and which type of withdrawal credentials they can do things with, but ultimately if the smart contract or the way your custody of your keys is broken through withdrawal credentials, it's certainly a bad case. I, I guess I would encourage people to think about this. I think that it's probably worth thinking about as we're examining how to clean up the deposit mechanism. I personally would rather see a more natural rate limit than, than just gas fees, but I do think I do agree that a fixed fee, or maybe a fixed fee in relation to gas, that isn't just, you know, the cost of running it could also be at least a worthwhile exploration. 

**Enrico**
I was speaking about on execution layer. 

**Danny**
Yeah yeah. 

**Enrico**
Oh, it doesn't help? 

**Danny**
No, no, sorry. I don't, I mean, you're saying the fees on the execution layer are the rate limit. So if you add, if you add a fixed fee then, and you quantify the cost of including such an operation on the beacon chain, then that could potentially be a viable path. Certainly not as elegant as the natural rate limit. 

**Micah Zoltu**
This may not make sense, but, what happens if a withdrawal key and a, validator key both tried withdrawal at the same time in the same block? 

**Danny**
that doesn't matter.

**Micah Zoltu**
Possible problems? 

**Danny**
Both of these are exits that we're talking about. Exits then eventually become withdrawals after they leave the queue. One of them, So things are processed in a certain order. So if you had a voluntary withdrawal and then you had a 0x01 initiated withdrawal, one of them would need to be a no op or one of them would not be able to be included on chain. Like if you had the voluntary exit, if you had to kind of, depending on the order, but you're right, you have to kind of, we have to test for that case, but I don't think it's a problem.

**Micah Zoltu**
Like we didn't test for it, but there shouldn't be any problem with it. 

**Danny**
some edge cases there, like if a slashing is included, then you can't include a voluntary exit on chain because that person's already exited, initiated, exited from a, from a slashing. So there, this is not, it's not unique that we have to kind of think about these operations in it. Executable specs. Great. Sorry. Arnetheduck, what's up? 

**Arnetheduck**
No, I was just going to mention the slashing rate. It's funny. 

**Danny**
Yeah. And that was a, It's an important case. cause I don't think we had a test for that one for a long time, but now there's a consensus for that one. 

**Danny**
Well, part of it is unspecified, right? 

**Arnetheduck**
As long as this lives in the pool. 

**Danny**
Well, that's an even, that's a, That's a slightly different case. That's a, that's a pool management problem, a pool management and block packing problem beyond that, the state transition problem. 

**Arnetheduck**
Oh, there is an inherent imbalance in that we can accept more exits than certain kinds of slashings in the block. If I remember the block limits correctly.  

**Danny**
I believe you can put in, I believe you can put in 16 proposer slashings, but like one or two, that's attestation slashings, but attestations slashes can include quite a bit of validators. Anyway, we digress. 

**Artyom**
I'm still got a question about, doing preliminary checks. I found a place, I was thinking about in Prysm client. I've sent the link. this is, this is the function where a deposit logs are parsed. And here there is a, at least a check, okay. There are some checks, for the events and some of the events are considered invalid and on the, then they go further where they get to the part of the execution, which is described in the consensus layer specs. And my idea was to do the checks here. Am I getting something wrong or not? 

**Danny**
So if you do the check here than a someone who's only validating the beacon chain, would not be able to, it would be opaque to them. Why maybe if these were index and must be processed in order, why there'd be missing ones, if you assume every beacon chain does have an execution engine, then that is, this is probably fine to do there. if you do not, you still have to specify it somewhere though. So I don't know, my intuition is much cleaner to do it the other way. And my intuition is that if you do put it in here, then you do, you do kind of limit certain types of, lighter versions where maybe I'm only running the beacon chain and I'm not running the execution engine, which although validators shouldn't do that, that's certainly a thing that users might do for some reason or other. so it does reduce the ability to process and fully validate the beacon chain state transition, because you have to get this kind of missing component coming from the execution layer. But I don't know, I would need to think a bit more about whether that can be done in a safe way. Does anyone else have an intuition on that? 

**Artyom**
And the same problem doesn't happen for the deposits, because the checks here are My, my mail may be on the checks for, for the duplicate events, duplicated events. 

**Danny**
I would presume these checks are primarily to ensure that they kind of make sure their cache and construction of the tree is valid, but that everything that's admitted from the deposit contract going to end up as a deposit on chain here. I'm not too familiar with this. 

**Danny**
Right. Any other questions for today? Okay. We're still... By still, I mean, to do, figuring out how to make this process in the consensus layer a bit cleaner so that people can propose features beyond just the me through search. if you are interested in specking out this feature, making a feature directory inside of the consensus layer specs would be the way to do so. there's like, if you look in there, there's primarily things bundled into forks, but there is a 4844 future directory where that's specified. So it can be kind of considered independently of a fork until it's time to integrate it into a fork. So if you wanted to take it to the next level and specifying, that would probably be the place to do so. And I think once you put, If you deem it worth kind of doing, then you'll probably get more eyes at that point. But again, I think there's probably some stuff to think about as we clean up the deposit or explore cleaning up the deposit structures. 

**Artyom**
Thanks. 

## [Open Discussion/Closing Remarks](https://youtu.be/-6dZVes6aWc?t=4766)

**Danny**
Okay. Anything else for today? 

**Pari**
just a tiny note, would everyone be okay with the next shadow fork happening Monday the 30th? So there's more time for everyone to catch releases and we can hopefully test the Ropsten releases as of Monday or Tuesday. So 30th or 31st. 

**Tim Beiko**
I like the idea of having it having one happened with like Ropsten releases. and hopefully we get them all by the end of next week, so we can the blog post out. 

**Pari**
Exactly. And if a couple of the clients still haven't made the releases, that's perfectly fine, but it would be nice to test well, was it? 

**Marius**
Yeah, but you should, you should really make your releases by the 30th. 

**Tim Beiko**
Oh no, you should make your releases before that please. You shouldn't really make your releases by the 25th, ideally. So that cause like, what would be really good is if releases are out like next Wednesday, then that means like Thursday, we can publish the blog posts and like people have the whole weekend to get set up before Genesis of the beacon chain if they want. yeah. So please, before the 30th. And I guess what we're just saying here is like, we're not doing a shadow fork next week to give people that time to cut over these. 

**Pari**
Exactly. And just in general mod stuff, neat quality of life stuff, whatever you want to do. Yeah. 

**Danny**
Great. I assume the shadow forks still looks good. Okay. 

**Pari**
Yeah. Nothing has changed since the past half an hour or so. Yeah. 

**Danny**
Excellent. Okay. On that note, let's close it out. All Core Devs next week. talk to you all soon. 

**Tim Beiko**
Thanks everyone.

**Everyone**
Thank you. 

-- End of Transcript --

## Attendees
* Marius Van Der Wijden
* Danny Ryan
* Lightclient
* Pari
* Micah Zoltu
* Mikhail Kalinin
* Justin Florentine
* Marek Moraczynski
* Mamy
* Saulius Grigaitis
* Enrico Del Fante
* Terence (Prysmatic Labs)
* Mehdi Zerouali
* Trenton Van Epps
* Ben Edgington
* Gajinder
* Caspar
* Artyom Veremeenko
* Jamie Lokier
* Carl Beek
* Zidance
* Cayman Nava
* Arnetheduck
* Alex Stokes
* Mario Vega
* Stefan Bratanov
* Tim Beiko
* Hsiao-Wei Wang
* Dankrad Feist
* Pooja Ranjan
* James He
* Zahary
* Ansgar Dietrichs
* Protolambda
* Lukasz Rozmej
* Yoav
* Francesco D'Amato
* Vasilly Shapovalov
