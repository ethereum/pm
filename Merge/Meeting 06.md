# Merge Implementers' Call #6 Notes

### Meeting Date/Time: Thursday 2021/6/17 at 13:00 UTC
### Meeting Duration: 35 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/340)
### [Audio/Video of the meeting](https://youtu.be/b5gh0Mw2oPU)
### Moderator: Mikhail Kalinin
### Notes: Santhosh(Alen)

# Agenda
- Implementation updates
- Research updates
  - Polish merge/beacon-chain.md, ethereum/eth2.0-specs#2472
  - Add randao to execution payload, ethereum/eth2.0-specs#2479
- Spec discussion
  - Location of execution-layer specs
- Open discussions

# Intro
**Mikhail Kalinin**
* Let's just get started yeah welcome to the Merge Implementers' Call #6 today is going to be pretty straightforward I guess so we'll start from implementation updates as usual there is yeah there is update from my side i'm working on the transition process implementation attacker because the pr has been merged into the into this big repo so I feel like i'll finish this implementation like t the end of this week or early next week and we'll try to.
* Yeah, the next challenge will be to set up the proof of work chain locally around the beacon chain, do all the steps that we did on the mainnet already, and finish it with the merge transition process, so probably I'll just you yeah yeah likely reuse the scripts that we have from after rayonism, which is great, and yeah we'll use the Gary PR, which already contains everything.
* The transition logic and in gaf so we'll see this is my update does anyone else have an implementation update yep I believe it makes sense everyone is working on the corresponding hard forks so okay cool any questions here.
* Okay, let's go on to the research updates. We have a couple of things to highlight and possibly discuss, and we have Justin on the line I guess 

# [Research Discussion](https://youtu.be/b5gh0Mw2oPU&t=70s)

**Danny**
* I can provide some context. I'm talking about PR [2472](ethereum/eth2.0-specs#2472). Justin is known for going through polishing and merging making sure that the specs conform in terms of naming conventions and structure and all that kind of stuff, so he's done that on the recent merge specs has been about a bunch of reviews I just did it's now passing ci and and has incorporated the feedback so I gave it a plus one this morning if anyone wants to take a look at it.

**Mikhail Kalinin**
* Yep cool yep so i'll just drop this the pr just in case so yeah there are some renamings and reordering of the fields in the execution payload this is one of the like not substantial but the biggest change I guess right so in some renaming some of the methods yep okay cool so then yeah yeah the next one is the randall pr so there is a pr which adds the randow to the execution payload as Yeah, as the difficulty is already present in the evm context and can be used by the difficulty of code to yeah, and this is the way the randall will be exposed in the evm for the applications we will support, or better said, will not break the existing applications that use difficulty as the source of randomness by this change, and potentially, like after the merge in the cleanup fork, we will probably annotate The counter-argument is that we don't want to change the evm, as we did in the initial merge iteration, but how big of a deal do you think it will be to directly and badly run down into the evm context?
* and can be used by code difficulty to yeah and this is how the randall will be exposed in the evm for the applications we will support or better to say will not break the existing applications that use difficulty as the source of randomness by this change and potentially like after the merge in the cleanup fork we will probably and we will likely and we want to do it in the following way.
* So there and there will be sent directly to the evm context and will not be embedded in the execution payload so and the reasonable question here is what if we do this like at the point of merge and it's the minimal version the counter argument to this is that we don't want to change the we don't want any changes in the evm like in this first merge iteration but anyway what do you think how significant it will be to directly and negatively run down into the evm context.

**Danny**
* I mean, my point is that we have to modify difficulty since it requires the new context, and so defining it as a constant or taking it as the value off of that rpc uh has probably small complexity difference, so we might as well do it at all.

**Mikhail Kalinin**
* At this point, the question Yes, that is the question, so is it a huge concern that you have to transmit it directly to the evm without any intermediate steps?

**Danny**
* Yeah, the execution layer gets context and directives, so I don't think it's a major concern, but I'm not in charge of the program on that side.

**Mikhail Kalinin**
* yeah, this is the question, particularly for net client monitors, how tough is it to adjust the.

**Danny**
* Well, that will have to be adjusted again. It could be something like if post-merge difficulty equals one um or if post-merge difficulty equals this value that has been passed on.

**Micah Zoltu**
* Would appreciate hearing from Tommaso or Ryan.

**Rai**
* Because we're already changing, I think it's fine to do it at the same time.

**Mikhail Kalinin**
*  Well, the difference is that by utilizing this or that route, you don't need to update the vm at all by just embedding the randall into the difficulty field right uh, I don't think it's a lot of effort either definitely some testing to cover this situation.

**Danny**
* Dragged a mouse into the chat, so it sounds fine, but I'm not sure if I mentioned the video.

**Rai**
* Why is this a workaround? I'm confused. Also, why is this not the final version?

**Mikhail Kalinin**
* No, it's not the end point, so this is only to avoid having to deal with the evm in the first place. This is more of a workaround than a permanent solution.

**Rai**
* Why is this a workaround? I'm perplexed. Also, why is this not the final version?

**Mikhail Kalinin**
* Do you mean "difficulty"?

**Rai**
* I meant to use random in my query, thus the final thought in my head was randall in the place of difficulty in the payload.

**Micah Zoltu**
* Is there any reason why we would wish to disclose the randow in the evm via a mechanism other than that opcode?

**Mikhail Kalinin**
* does it make sense?

**Micah Zoltu**
*  Yeah, is there any reason why we would ever have to return to this? For example, if we set I forget what opcode difficulty is but that opcode now just returns render value, are we done forever and never have to return to this because the evm now has a random number generator at the end?

**Danny**
* Yeah, if the value was hardened, like, with a pdf or something, it would be substituted for that fresh new heart and value, but.

**Mikhail Kalinin**
* Yes, it's 256 bits, but it's not cut like the fuller and the amex.
* Yeah, we're just talking about how the random makes this boot into the edm is revealed by the evm the source of it is is it going to be part of the execution payload or is it going to be um like a side value but it's used by the evm um without being placed into into.

**Danny**
*  I believe it makes sense to include it in the payload, and I don't see any problems with doing so even as a final destination.

**Jacek Sieka**
* I mean, the problem is that people used to start relying on the randall and not a random value because the randow is a specified source of randomness. Is it a problem? Can we use a different source later on?

**Mikhail Kalinin**
*  No, I don't think it's this problem, so we can name it rendao and use another source of randomness if we like, so rendao is a type of abstract thing here.

**Jacek Sieka**
* Because if we just want a random number, we could take the hash of the render or something, but if we state it is the render out, people will start utilizing it for other correlations as well as just a random value.

**Dankrad Feist**
*  wait, you can't do anything else with it right now, can you?

**Danny**
* It's already the random mix, so it's already hashed next sword, so it's not truly like the signature, so it couldn't be used for signature verification or anything else, uh but if that's the case,

**Dankrad Feist**
*  I don't see that as a threat, because even if it were the signature, there's nothing in there in my opinion; it's simply the signature of the slot that people might occupy.

**Micah Zoltu**
* Do some form of validation against yeah\slike on chain validation of stuff\sand then you take it away and you're\slike oh the rando is now this other\srandom number they're\slike oh my contracts broke because I was\susing that to verify blocks\syeah I mean clearly that's pretty.

**Dankrad Feist**
*  I'd be amazed if you could do any on-chain valuation validation because it didn't contain anything important.

**Danny**
* If it were the signature, you could put your entire contract in there and if Randall checks it, then all the logic after that, and we'd have a really stupid mechanism.

**Rai**
* It's not a signature.

**Danny**
* so okay right so it's the xor of the hash uh with the previous randomic so there's no odd well someone can always try to find out something weird to do but um it's not weird.

**Dankrad Feist**
* I just don't understand why you'd do it because there's nothing useful you can do with it it's not a signature of a block it doesn't sign any meaningful data and it's not even a signature the value today is not even a signature right you can't you can trace it back to a signature if you want you could make a proof that back to signatures but they signed something completely useless so yeah.

**Danny**
* We might call it random.

**Jacek Sieka**
* well, I believe that's the point a little bit, the fact that we can't figure out what people would use it for in five minutes on a call doesn't mean that it won't get used that way if we say it's the run now that's all I'm saying okay.

**Paul Hauner**
* yeah six point what if I made a contract and the purpose of the contract was just to upload little bits of beacon blocks and states to it just to add the information in there and I said oh you know what don't worry about uploading the brand out because we already have that because it's exactly what the op code is like it's a contrived example but there's anything yeah no that's not the case.

**Danny**
* That's certainly accurate; I'd call it random.

**Mikhail Kalinin**
* You mean the up code, or if difficulty is going to change on a daily basis, I'd call it random okay okay so what I'm a little concerned about here is that we're changing difficulty, which was like much less than 30 bytes before the merge, but it will be 32 bytes after the merge, so it will need to be checked whether there are no overflows in the execution clients.

**Micah Zoltu**
* I believe, but I believe the execution clients after the last call and I believe all of them got back and said it's 256 bits and I can go verify that, but no one mentioned anything.

**Danny**
*  However, if they're running a total difficulty calculation and summing it for some reason, they might have strange overflows even though they shouldn't be using total difficulty after that point or anywhere meaningful after that point.

**Micah Zoltu**
* Oh, I see you're saying there's a potential source of bugs during the merge that we should keep an eye out for.

**Mikhail Kalinin**
* Right, this is a potential source of bags, and if we set the difficulty to zero or one, there will be no such source of bags, and we will have to pass run down a side of the execution page, but that's the only thing.

**Danny**
* Also, if you set difficulty to one, you might inadvertently use the longest chain rule and be correct part of the time, and you don't want to be correct some of the time since then you have an attack. vector.

**Mikhail Kalinin**
* Right, you can set it to zero anyway good so this is the PR that just replaces difficulty with uh the random or rendau value and we can rename the op code after the merging okay.

**Micah Zoltu**
* I instance, changing the upcode is purely social; it has nothing to do with the code, and you could just write a variable name and code someplace.

**Danny**
* So I would and then solute it to april I just want to stress that anything like this uh probably would need to find its way into becoming an eip um but that's probably a whole different topic as to how this shows up in that process.

**Mikhail Kalinin**
* Okay, here is the next item on the agenda.

**Tim Beiko**
* how do we keep track of all these changes?

**Mikhail Kalinin**
* So if we finished with the rendao um if anyone um like wants to look in dpr it will be very much appreciated so um I think if there are no blockers we can merge it like on the next week so please take your time if you have it take a look yep I think we can move on to do the execution layer stacks so yep Tim like us uh raised like very reasonable question.

# [Spec discussion](https://youtu.be/b5gh0Mw2oPU&t=930s)

**Tim Beiko**
* Yeah so now yeah I guess one thing is figuring out where we want to have the specs for this I think currently eips is the best place there's some work happening on an e2 style spec for each one but you know it's not ready yet and I I wouldn't necessarily want the block on that I feel like that even more basic than that though we probably need just a sort of list of Like changes or open questions that we need to answer for each one, I think that would be useful like obviously for us to have a broad picture of like this is all the stuff we need to do, and I think it's also something that will become increasingly useful as the community asks one merge to have some list of like well these are the things we need to solve, so I'm happy to help put that together, but I'm curious what folks think is the ideal approach for this, and does that make sense in general?

**Danny**
* yep yeah I mean right now the ethere specs are kind of a smation of the yellow paper and eips and stuff and I think that's been attempted to be captured in that ethonos specs repo so even if there is an executableness there maybe that should still be kind of where the execution layer specs ultimately go so yeah I I think assumin we don't have some sort of executable spec on that side. It's certainly easier said than done, and it might be fairly messy. We did an informational eip for the beacon chain launch, and it might make sense to have an informational eip that just kind of explains and locks down versions and stuff, but I'm speaking outside of my domain at that point.

**Tim Beiko**
* Yeah, I think we could have an informational or meta eip that's kind of a description, and I think the one thing that distinguishes this from a regular hard fork is that there's a lot of non-consensus changes that I think are important to docent like you know all the stuff around syncing for example if it's obviously like a massive part of the merge but it's not like something that's actable.
* That's actually a hard fork, so I think those are the types of things we want to make sure we have a list for, and I think those can all be eips as well, right like it's fine we have eips for some of the syncing protocols definitely not everything but we can open networking eips for this stuff yeah so I don't know if that's the format people want to use it that we have.

**Micah Zoltu**
* Okay, I'll keep this brief because I believe everyone here has already heard my argents and we don't need to waste too much time on it. eips is a specifications repository, a place to keep technical specifications; it is not a docentation repository; there are far better tools for docentation that we should be using; I am a huge fan of docenting all this getting everything written down; I'm not arguing we shouldn't docent it; I'm just suggesting eip's repository is not the right place for non-technical specifications. efp is a fantastic location. other that that hackmd ethere.org similar to wiki github Anyway, I believe that's all there is to it.

**Tim Beiko**
* We can utilize the eth1 specs report to perform this broad docentation if you think it doesn't make sense to have a meta-eat or informationally like great we can put that in each specifications repo but this sort of docentation is kind of a wrapper over numerous technical modifications like what we do about.
* It's like that lit and you know do we want that list each of those technical changes that have been associated with eip and if people want to do that I think that's fine but it's just good to know kind of already because maybe we can start drafting some of these eips and putting something together in the east one specs repo that says, "Hey, this is the merge" Here are the various eips, and here are the things we still need to figure out but haven't gotten around to developing an eip for yet.

**Danny**
* As a first step, maybe ui and others should black box the functionality from the beacon chain and then enerate everything that we know is that we've already kind of specified as changing and know that we will be specifying as changing even on sync op codes and that kind of stuff and then once we've enerated everything figure out the home for the different things.

**Tim Beiko**
* Okay, that sounds good; I'll follow up with you and nikki allen; others are attempting to acquire a first draft of it.

**Danny**
* Great yeah.

**Mikhail Kalinin**
* I believe we require a timeline with checkboxes.

**Tim Beiko**
* Yeah, I'm arguing for checkboxes to avoid the timeline, and I believe we did this fairly well with 1559 where we have this checklist because there will be increasing pressure at the worst time when stuff is like 50 ready and people will start asking you know when merge and being able to say well look you know here are like 10 things we still need to figure out.
* You know, both for us, I think first and foremost, but also for the community, there's value in seeing like, oh, the consensus changes are done but sync is broken or json rpc is broken or whatever right yeah, I definitely would not put dates on that docent and kind of use it as a shield against having to provide dates.

**Mikhail Kalinin**
* okay see yeah okay as for the eip process, I don't think it makes much sense to put every different part of the execution client change into a separate dip probably we can use the approach that was taken in the click eip which just describes everything in one docent what do you think I mean once we figure out the synth process once we figure out yeah seeing process definitely will be.

**Tim Beiko**
* As we have, but as all the courses alter, perhaps one yep yeah.

**Micah Zoltu**
*  I don't have a strong view in favor of it.

**Mikhail Kalinin**
*  I agree that all of the agreed modifications should be in one place.

**Micah Zoltu**
* I guess the advantage of having a lot of small eips is that they tend to go a lot smoother because they change set as small. What happens when you have a large like monolithic eip is that you get a bunch of bike shooting on some like minor piece of it and then the entire eip gets kind of stuck in the mud. Also, because conversations tend to be centralized around like the discussions to link because there's just too much talk about that bike shedding piece and it's very difficult to find the actual discussion, so my recommendation is to try to split up into as many smaller eaps as possible just because it really does make the process go a lot smoother eips that are like a page long go through almost instantly whereas eips that are like 10 pages or so take way more than 10 times as long.

**Danny**
* Yeah, I think I'd agree, but I'd like to see what those items are that actually need to make it into an eip before we decide, for example, this difficulty change being in its own uip that makes sense it's probably like a one-pager and it's it's pretty easy but I I there's yep it's unclear to me which things are going to make it into your ip yet.

**Micah Zoltu**
* Yeah and figuring out where to draw the line is definitely an art um just a caution i've seen a lot of people try to build monolithic eips and I don't think i've ever seen it go well.

**Danny**
* We'll call on the the artist of micah to give us a hand.

**Micah Zoltu**
* starters like we'll be like make this shorter.

**Mikhail Kalinin**
* Okay, so for the time being, when it makes sense to start writing those eips, I believe we should first figure out the transition process to ensure that nothing too significant changes. It would also be great to get the sync process figured out as well, and then we can just put everything together that uh changed all the changes and the consensus for the execution side.
* And put them together to see what could be decomposed and put in a separate ap and what could not be decomposed like, and yes, this is just my ideas on Glenn, and hell, probably we can start like not waiting for a sin process figure it out and alter anything like in the eip drafts later on.

**Tim Beiko**
* Yeah, I believe so, like he said, figuring out what all the key sort of themes are in a manner, and that'll give us a good image of like the ordering and when it's the ideal moment to actually uh formalize uh different sections of it.

**Mikhail Kalinin**
*  Well, we're starting, and we can get these check boxes right now, right?

**Danny**
* Yep i mean.

**Mikhail Kalinin**
* Okay, so we'd want to get the paper with checkboxes in a short period of time.

**Tim Beiko**
* then add links to the medium's checkboxes.

**Mikhail Kalinin**
* Yeah, and you already have some links underneath them, so those checkboxes will probably be ticked okay, and then once the transition process is like a prototype prototype, we can start thinking about eips right? I had this like research doc that I gave up to keep up with the list of leftovers. This challenging thing was one of the final remaining leftovers.
* I can double-check, but I believe that the transition and sync are all that is required, but I'll double-check it. We can use it as a source for this type of page with checkboxes, okay?

**ProtoLamda**
* Don't forget the api.

**Mikhail Kalinin** 
* You're correct, API. Cool, so if we're okay with that.

**Danny**
* Another big item is definitely um testing and how test generation looks in this unified front and if everything is sort of divided into these layers um for more unit testing and then what things like hive and other integration type tests look like, but let's not solve that today.

**Mikhail Kalinin**
* Yes, when I said that this hard issue is the final or possibly the last one, I was referring to the research open questions, which we don't appear to have, so if we're done here, we'll go on to the open discussions By the way, did I forget to ask if anyone has any other research updates? If not, I've started writing the consensus api improvement proposal, which is about enhancing the communication protocol. I'm hoping to finish it next week and share it with everyone, but it will most likely take longer.
* so we'll see how this goes okay any other conversations anything else any pro announcements probably okay thanks everyone for coming it was really quick ok that's nice

# [Open discussion](https://youtu.be/b5gh0Mw2oPU&t=1738s)

**Protolambda**
* So, we have Altair coming up, and I'd just like to highlight that we will need to rebase upon out there at some point. This will effect people who are implementing the, such we should attempt to time it so that we can move in sync.

**Mikhail Kalinin**
* Yes, thank you, brother. Yes, there will be some other changes such as cleanups and probably a new consensus api to catch up with after health here. Also, regarding testing, I have a plan to finish the transition process um and then get back to work in this back and um tests in particular we will need some kind of tests for the transition process which will involve both consensus and executables.

**Danny**
* Yep, we have some fork integration tests for altair from phaser altair, so we can at least use some of that as a basis, but we'll have to work out how we exactly integrate and or stub the execution side in those tests.

**Mikhail Kalinin**
* Oh okay thanks everyone i'll see you in 25 minutes thanks everyone thank you what's this the call that we were talking over um api last week two weeks ago or is that e2 call if you call good.

-------------------------------------------
## Speaking Attendees

**Lukasz Rozmej**  
**Pooja | ECH**  
**Gary Schulte**  
**Mikhail Kalinin**  
**Micah Zoltu**  
**Dustin Brody**  
**Terence**  
**Danny**  
**Jacek Sieka**  
**Paul Hauner**  
**Alex stokes**  
**Vitalik**  
**Dankrad Feist Kevaundray Wedderburn**  
**DCinvestor**  
**Ben Edgington**  
**Protolambda**  
**Sajida Zouarhi**  
**Hsiao-Wei Wang**  
**Karim T**  
**Kristof Gazso**  
**Adrian Sutton**  
**Bhargavasomu**  
**Tim Beiko**  
**Trenton Van Epps**  
**Mamy**  
**Tomasz Stanczak**  
**Ansgar Dietrichs**  

---------------------------------------
