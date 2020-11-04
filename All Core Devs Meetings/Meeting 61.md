# Ethereum Core Devs Meeting 61 Notes
### Meeting Date/Time: Friday, May 10, 2019 14:00 UTC
### Meeting Duration:  1 hours 30 minutes
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/97)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=CNcBuJ6wivE)


# **Summary:**

## **ACTIONS REQUIRED**

**ACTION 61.1**: [Ganache/spec compliance issue at go-ethereum](https://github.com/ethereum/pm/issues/97#issuecomment-489660359)
**Status**: Will come back on it in one or two meetings.

**ACTION 60.1**: Review timeframe for hardforks in June to refresh memories.

**ACTION 60.2**: Danno Ferrin to add 9 month out Hardfork kickoff to [timeframes](https://ethereum-magicians.org/t/more-frequent-smaller-hardforks-vs-less-frequent-larger-ones/2929/28).

**ACTION 60.3**: [EIP 615](https://eips.ethereum.org/EIPS/eip-615) decision discussion at next meeting.
**Status**: PR will be made.

**ACTION 60.6**:  Martin Holste Swende and Alex Beregszaszi to confirm whether [EIP 689](https://eips.ethereum.org/EIPS/eip-689) needs to be implemented.
**Status**: WIP

**Action 60.7**: Parity to comment on Libraries for Precompiles (https://github.com/ethereum/pm/issues/95#issuecomment-486879991)

**ACTION 58.1**: Cat Herders to look at updating EIP1. 
**Status**: Work in Progress

## **DECISIONS MADE**

**Decision 61.1**: that there is value in hardfork deadlines.

**Decision 61.2**: that this first deadline should serve as an upper bound for the maximum number of changes that might go and do a subsequent hardfork into Istanbul. But of course not everything that is proposed by that deadline will necessarily make it into the hard fork. 

**Decision 61.3**: And furthermore that as of this particular deadline 7 days from today, these EIPs today may still be in draft form; they're not expected necessarily to be thorough and complete, nor in Accepted state. And of course not expected to have implementations ready.

**Decision 61.4**: [EIP 615](https://eips.ethereum.org/EIPS/eip-615) -  PR will be made to list it.

## SUGGESTIONS

**Suggestion 61.1**: More than one EIP documents are needed to address three things: 
a. quality specification
b. high-level proposal
c. intention to get your change into the next hardfork

**Suggestion 61.2**: [Ganache/spec compliance issue at go-ethereum](https://github.com/ethereum/pm/issues/97#issuecomment-489660359) - it will be helpful to spin out into separate repos.





# 1. [Review previous decisions made and action items](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2060.md#summary)

**Lane** : Reviewing [Meeting 60 notes](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2060.md#summary). 

**ACTION 58.1**: Cat Herders to look at updating EIP1. 
Status: Work in Progress

Tim: I've a [PR](https://github.com/ethereum/EIPs/pull/1991) open, anyone wants to give feedback are welcome.

**ACTION 60.1**: Review timeframe for hardforks in June to refresh memories.

**Boris**: In June, we will re-examine the timing.

**ACTION 60.2**: Danno Ferrin to add 9 month out Hardfork kickoff to [timeframes](https://ethereum-magicians.org/t/more-frequent-smaller-hardforks-vs-less-frequent-larger-ones/2929/28).

**ACTION 60.3**: [EIP 615](https://eips.ethereum.org/EIPS/eip-615) decision discussion at next meeting.
**Lane**: I'll add it to the agenda for this meeting. 

**ACTION 60.4**: Danno Ferrin to add list of conditions for implementation and Pull Request [EIP 1057](https://eips.ethereum.org/EIPS/eip-1057) into the Hardfork Meta EIP [1679](https://eips.ethereum.org/EIPS/eip-1679).

**Danno**: It is now in the EIP 1679. I just put it there to say that it is above and beyond. The Standard Security audit requirements should be considered before inclusion. I didn't list any exclusive reason because we don't know what the audit is going to come back. Basically, discussion needs to happen when the audit comes back.

**Lane**: It is listed under proposed EIP under 1679 which is meta Istanbul.

**Rick**: I mean in addition to the code audit is there discussions around simulations and all this other stuff  - testnet, deployments and all that stuff with progPOW as well? Is that all in the same ? Are we thinking about all those things at the same time?

**Boris**: I think that's a separate item in the sense that I just added to the to the comments for this thing is that there is no point of contact for testing,  testnet coordination or anything other than Dimitry's work.  So, I am proposing that the needs to be for at least one human who coordinates and cares about all of those things. Let's cover it when we get back to agenda. 

**Lane**: Added to this agenda - Testing, testnets, and road to Istanbul. 

**ACTION 60.5**: Martin Holste Swende to confirm that [EIP 1884](https://eips.ethereum.org/EIPS/eip-1884) has merged into the Hardfork Meta EIP 1679.
**Martin**: It is in meta.
Status: Done.

**ACTION 60.6**:  Martin Holste Swende and Alex Beregszaszi to confirm whether [EIP 689](https://eips.ethereum.org/EIPS/eip-689) needs to be implemented.

**Martin**: My take is that we can slip it because [EIP 684](https://github.com/ethereum/EIPs/issues/684) is already implemented and are basically the same thing.

**Alex**: I think you mentioned that 382 is in conflict with it.

**Martin**: No.  Long time ago we decide on 684 and 689 are roughly the same thing.

**Alex**: I would suggest we take it offline.

**Lane**: I'm going to go back to the last one here if you guys are comfortable with that.

Status: WIP

**ACTION 60.7**: Parity to comment on Libraries for Precompiles (https://github.com/ethereum/pm/issues/95#issuecomment-486879991)

Scrolling through this thread, I don't see any comment from the Parity here yet. 

**Phil**: Yeah, it's still there. I will get some people on the next call. 

Status: WIP

**Boris**: Just to fill in, is the Parity Ethereum client team are comfortable for using libraries for shared precompile? Or thet only want to have native implementation in their in their core client? Ping me if you have questions about that. I think that I've said it correctly.

**Phil**: Okay, will follow up.


# 2. [Roadmap](https://en.ethereum.wiki/roadmap/istanbul)

**Lane**: We're coming up now very close to the first deadline we have a hard deadline one week from today May 17th to accept proposals for Istanbul. Anyone opposed or anyone think this deadline needs to changed, speak up now.

**Alexey**: Yeah! I said it that this deadline shouldn't really be there but it's only my personal opinion. Because as I said many times before, that just putting something as a placeholder there doesn't really help too much. Because the EIP is ready when its ready.  So I don't know there's I just write a bunch of EIP and put it there. If it is not specified, it is waste of time to put it in core dev call.

**Danno**: So, I would like to **defend the notion of consideration deadline**. We are moving to a train based model. An EIP is ready when it is ready and it can move on the next train which is at stations every six months. And if we're going to do that we need to have some sort of a roadmap it says you really need to be ready by this point or you're going to miss the train. And that's really what this is. It's not strictly a if you miss this by one minute then you're going to get 10% off. It is something that people should be working towards trying to make it ready or tip the call that this is not ready for the release in five months.

**Alexey**: Well I understand this. The intention is clear to me, but I do not think that the EIP is the correct thing to be putting in. Because as far as I understand the EIP is the specification of the change. The specification of the change, from my point of view, cannot be produced in a high quality.

**Boris**: Alexey, let me cut you off there. So, I understand that you have a particular hang up about not putting an EIP until its perfect. In part this is signaling to understand and plan. I personally, if you put an EIP up,  it says ALexey will fill it later with high-quality but I intend to get in the Istanbul, that would be awesome from a signaling perspective. Is that ideal, that like 30 different people; all put in things that basically said the same thing  - not useful. But what we have got today, I think that if you want to bring it an EIP past the deadline it will be considered because that's what ACD can do but in the meantime we'd like to push anyone else not named Alexey get there EIP set. Is that a fair thing that?

**Alexey**: Well, yes! Maybe I'm just too hung up on this. we probably need to redifine, we need an EIP or just like a couple of lines saying that this is what I think should be happening.

**Rick**: I think we are talking about **three things currently being addressed with one document**. We need to decide on how many documents we need to address these things:

* One is a **quality specification** which I think Alexey wants and that's something I would appreciate. EIPs do not provide that today. 
* The EIP that exists today is a sort of a **high-level proposal** which is fine.
*  Then there's also the third thing that has come up with just the **intention to get your change into the next hardfork**. Those are three different things I don't want to blow up the complexity. But I think the intention of inclusion as a statement has top be made somewhere and we need a formal Spec made somewhere and we need these other things in between. I'm open to changing the names of things or making new things or whatever but those three parts of the process still need to be covered. Whether we cover them in two documents or three documents, we probably shouldn't be covering them in one document that probably should be revised three times. I think that's a little confusing.

**Suggestion 61.1**: More than one EIP document needed to address three things: 
a. quality specification
b. high-level proposal
c. intention to get your change into the next hardfork
  
**Greg**: The purpose of last call process was to get a fairly high level quality in the EIPs, obviously client implementation problem will be found eventually but  the purpose of that process has to say this thing looks pretty good and lets go. Right now we don't have that and getting it would be probably a good idea.

**Lane**: Any additional comments on road map or the possibility for multiple EIP tracks? I know Alex posted a comment here. Do you want to expand on your comment here Alex, about not having been categories?

**Alex**: Yes. I don't think it sends a nice signal to that side, that they're different people trying to propose stuff even if it was made as a joke. I think we just have to ensure people don't mistake it.

**Boris**: I will not be prevented from joking :) I hear you Alex.  So I personally would prefer if Alexey could signal which EIPs or categories of EIPs he thinks he can get ready for Istanbul. I think that would be a super useful signal and I don't care if it uses a smoke signal but it would be useful unless we're going to change our process in the next 7 days. 

**Alexey**: Yes, so I can do that. I can describe what I would like to get there but I can't write EIP because from what I understand EIP, it has to be formal specification. So if we were agree that the EIP is basically not formal specification I'm going to do this. Or tell me what are the things I need to produce ?

**Boris**: You and I dis updates to EIP 233. What if we say EIP XXX Alexey TBD but here is the name of it. Then at least we have a record in the same spot , in 1679.  We would actually have that listed.

**Alex**: My **understanding of the EIP process** was that, that the first deadline lists EIPs which are in draft mode and we don't really have a concrete specification of what draft mode means, even for core EIPs. But I would assume the draft signals that it may not be fully specified, it has a general idea and it is likely to improve for the process. Probably the draft mode doesn't mean that it is fully formally specified.  It has an intention that it will be and where the first deadline my assumption was that whatever is proposed by the first deadline is the list of EIPs which are going to be deliberated on and it's very few exceptions new EIPs should not be possible to be proposed because that may just lengthen the process.

**Boris**: That be in proposed for the next hardfork.

**Alexey**: Yeah. I understand that the people wanted to have these very firm procedures. But I would like to ask what is the purpose of the of these, having this list defined before the 17th of May ? Is it this list that we going to keep discussing for the next  say four months? Is that the purpose ?

**Martin**: Well Alexey!  It does help. I mean if there's a list for me then, these are the things that I should focus on and  to weed out. Even if it is not finished,  it's a list of good things that's if I want to help out, I can dive in that these are the list that I should look into. 

**Alexey**: Thats a good idea. Thank you. 

**Tim**: It maybe  worth highlighting on the client-side, it puts an upper bound that the changes we have to plan for, like more than all of the EIPs that make it into the hardfork and thats probably good to know.  

**Rick**: Just to echo that, that's the whole point. Wec need to figure out what code is going to go. What code actually goes into the fork and we need to know that some time in it advance and if we just say okay here's the gate and you know if you missed the gate you're not getting in this fork within the next fork I think that simplifies things overall.

**Tom**: It is generally good to have this deadline. I was worried why they areen't included yet, now I know. It will be helpful if Alexey just suggest which EIPs are they. I think 17th will be great to have to see the upper bound as it was mentioned before.

**Alexey**: Ok, I would make a rough list of the things that I would like to be included, but that won't be EIP essentially in my understanding. 

**Boris**:  I suggested it's okay if it's not EIPs. But Alexey I think Alex is correct is that likely what would be good is if you created a draft EIPs that indicate what those are and then those can be PRed  into 1679.  Draft EIP means that it basically filled out, that there are bunch of section that are TBD but we have a number assigned and we know the name of it and basically a rough abstract that says this is the one. So we know what we're talking about.

**Alexey**: Ok

**Decision 61.1**
**Lane**: I'm trying to kind of tie a bow on things and it sounds like we are agreeing:
1. that there is value in these deadlines.
2. that this first deadline should serve as an upper bound. The idea here is that this is the maximum number of changes that might go into Istanbul in this case. But of course not everything that is proposed by that deadline will make it necessarily  into the hard fork.
3. And furthermore that as of this particular deadline 7 days from today, these EIPs today may still be in draft form they're not expected necessarily to be thorough and complete. And of course not expected to have implementations ready because there's two months following that, until July, I believe, for that to happen.
Anyone opposed to those that summary otherwise we can keep moving.

**Greg**: I'd like to volunteer but I'm too busy as an EIP editor Alex is an EIP editor.  Can someone volunteered just help very busy Alexey with the mechanics of what an EIP is very well defined and someone just said,  get them going get an abstract get them in, so we have numbers to refers to what Alexey wants to do. It so important that it gets done. It helps a lot to have numbers to point at and say these things.

**Boris**: I'm fine to help you with the mechanics of it, but the other side, we need people in ACD that you can merge them.

**Alexey**: It's okay. I think basically my resistance was mostly about the the forming of the EIPs because my previous assumption was that EIP is  supposed to be a formal spec and then I wasn't prepared to provide smokes for the specs. If that isn't the case, I am fine with that. 

**Lane**: Alexey, are you happy with that, that EIP when draft may not be a formal spec but at the time when it is merged/accepted, it must be a formal spec. Does that help?

**Alexey**: I am not sure. I didn't have time to think about it yet. So I am willing to think about that. 

**Alex**: I guess the goal is the EIP  should be very high quality specification changes. I don't think that can be said about all the pastEIPs that has been merged. There is a  big varience between quality across them.

**Alexey**: Yes, exactly. I wanted to come out of this broken window. We had bad EIPs before, therefore we should keep doing it. My idea was lets start doing things in a good way. But lot of process are still going into the old way. So, if we decide that we are going to relax this for now, then we are keeping them.

**Greg**: EIP process is made solid for a while now. Just put a draft in the system, it only needs to meet the form of the draft. Then there' s a long process of getting the draft into the the formal specification quality that you mention. If we just need something at the beginning of the pipeline, the very beginning; it only has to meet the form. There's a program which will merge it automatically, if there's no problem.

**Lane**: I think we're probably on the same page wrt draft and Alexey has offered to create those placeholder EIPs. Boris has offered to help him with that process. Lets keep moving.

**Alex**: Can I add one final addition? I think the list of proposed EIPs, kind of just state the scope of changes. But they don't necessarily have a final list of the EIP numbers. By that I mean,  maybe some of the even current proposals and maybe be split into multiple EIPs. And same can apply to State rent related EIPs. Maybe it is enough to have a single state rent related EIP merged by the 17th which defines the scope of changes. And maybe throughout the process of defining those properly, we can end up multiple EIPs. I think that should be fine,  as long as we have at least one which defines the scope broadly.

**Greg**: Alex, are you volunteering to help Alexey later and hope we get this going?

**Alexey**: Actually, Greg, I think I am okay. I don't have any problem writing those things, I am absolutely fine with them. 

**Lane**: All right thanks folks. Alex thank you for adding that commentary. This is clearly the first time we've done this with the hardfork. So let's see how it goes and I think there's definitely scope to learn from this process to figure out whether they can be split etc.
Do we want to review the list of the ideas currently scheduled for Istanbul are there any more EIPs to add?
I believe the canonical listed  EIPs is in EIP 1679 that are scheduled for Istanbul. 

**Boris**: Yeah. [615](https://eips.ethereum.org/EIPS/eip-615) is still something that we'd like to get in. Those are the ones that are already fully in. The [wiki link](https://en.ethereum.wiki/roadmap/istanbul) there  have an extended list of other ones, that are people are like yes we're going to get this ready and PR them in as well. Trenton I have been teaming up on keeping wiki up to date, so that we can get even more review on the train of other EIPs that may still be proposed.

**Danno**: EIP 1965 is waiting on editors approval. There is some debate as to how the EPI 1344 and one I just meant and should be implemented. The author of EIP 1965 is trying to get attention of these people. SO, there's some contention with these EIPs right now.

**Boris**: There's contention with EIP 1344 and essentially an opposing EIP.

**Danno**: Yes, and that is not listed in 1679.



# 3. EIPs


## a) Refer to Roadmap link for list

[EIP 1679](https://eips.ethereum.org/EIPS/eip-1679) - Istanbul canonical list

**Lane**: Are there any additional EIPs already on the agenda and not in 1679 and if people want to discuss right now actually? My understanding of the status to be Hudson reached out to Zooko and Zcash would like to see this as well. But they're looking for a champion and Virgil has also offered some funding and Gitcoin has offered some funding but unless anyone has heard otherwise I'm not aware that this is currently being worked on. And therefore is not going to make it into Istanbul unless that changes in the next 7 days.

**Alexey**: So there's another EIP which is not listed but there is a working group going on this one. It is the generalized electric curved precompile, I think. I think I'm almost to make sure that it will be included as essentially the generalization of the previous one [1829](https://eips.ethereum.org/EIPS/eip-1829).

**Alex**: Alexey, there is a waiting to finish his PR which proposes that for 1679. 

**Alexey**: Oh so he's going to do that?

**Alex**: yeah 

**Alexey**: There was a to do in the EIP about the modulus so the original EIP was saying that the modulars will be less than 2 to the power 256 which means that large amount of this wouldn't be supported. Now ther is work on the extended group variance which actually will have modulars  more 2 to the power 512 or even like 1024. So this is probably going to be extended in the EIP or something like that.

**Alex**: As a second note, I think there are probably 4, 5 maybe after 10 draft EIPs which haven't been merged but they are there as a pull request and I'm seeing that people want to propose them as the part of Hardfork. Maybe we have to allow merging the proposed list without the truck being merged. But I'm not sure what's the best approach. I think we have some predefined rules what basic quality in EIP should have at a time it is merged as a draft. Before that it only appears as a pull request. Some of these proposals may not be up to the the quality requirements of being merge as a draft. We have set that only those which are merged as a draft, only those can make it into the 1679 list. So, **this is a question we need to answer whether this is a good approach or we should change it**?

**Alexey**: Well but this is what already starts coming back to what I was saying, is that what is the quality?  We just decided that it needs to be formatted properly and that's it and now we're talking about the quality?

**Alex**: Even the formatting is off in some of those.

**Danno**: Just 'cuz it's deadline it doesent makes it included as well.  This is the first gateway if you don't make this you're going to be on the next boat. So we still need a vet make sure they're good.

**Alex**: The next big challenge will be, I kind of expect that we will end up with a list of like 15 EIPs proposed, by the looks of it, by the next week. **The Big Challenge will be to actually discuss those 15 and how to reduce that set of 15 into the more manageable set?** 

**Alexey**: This is why I was asking what is the purpose of having this list? Probably, it is not the purpose of the list to keep discussing all the 15 things every single time. When something is really actually happened then you should be discussing. Otherwise every time going through  the same list will be super boring. 

**Boris**: The next thing that people need to do is to get things into an accepted state. So they need to sign up to an ACD. Say I would like to review EIP XXX and propose it for acceptance. that is the next step. If people don't get it through acceptance, all of this also essentially relies on Champions to keep pushing it. So we're actively trying to weed out the things that people aren't going to work on. It's not arbitrary.


## b) Please add more EIPs to the agenda


**Lane**: Okay that's great. I think we talk to this topic in depth. I think that we should continue conversation on magicians. Maybe on future agenda item calls as well.

# 4. [Eth 1.x Blog by Alexey on changing processes](https://medium.com/@akhounov/ethereum-1x-as-an-attempt-to-change-the-process-783efa23cf60)

**Lane**: Alexey, would you like to briefly share this?

**Alexey**: What I think the process should be is written there.
I wasn't actually planning to write it but what's happening in my head about like what I think Ethereum process should be was just in my head and other people think otherwise. And I realized after listening to one of these community calls when they decided or proposed I would say, that to **drop the Ethereum 1X name**. The augmentation there was that it's just a list of items on the roadmap and why should it be having this name? To me it was more than just a list of items. It's actually the attempt to change the process. I described it in the blog post so you can read it. The biggest thing is that it's not something that I could have meditated like from the start. It's actually something which sort of organically fell out of what we are trying to do. eg. we work and try to organize working groups around the certain changes. 
And then the next question was where who's going to pay for this work?
Then another question was like, I realize that a lot of people who are coming in trying to do the work they already doing something else and we have a very limited pool of people who actually think they can work on stuff. So then I started to think if they're going to work in parallel like how they going to get things in because we have a few bottlenecks in the current process. Example, **testing is huge bottleneck** as we repeated many times, has to be opened up. We also have some sort of a bottleneck in the past that most of the prototyping was actually done by one of the three implementation teams.
That's also a bottleneck because they were busy with the optimisation of the clients. It is kind of unrealistic to expect that they would also be working on the implementattion of all these EIPs.  We want to remove bottleneck on the client implementation team, bottleneck on the testing. So therefore basically just push this idea of the working groups working in parallel getting the proposal still high quality and basically making approach those who much more inclusive instead of waiting for somebody to pick up a change this. Like you form a working group to start working as an end once you get some good quality stuff, then you can just push it in. 
So I haven't covered testnets and stuff like this because it also requires a little description and I also didn't even go into EIP process. Because for me, if you want to confuse somebody you just basically start talking by the EIP process. So that's why I wanted to avoid most of that and I just showed to people from my point of view how these things actually work and not how they work on paper. I'm interested to see what you think about it, whether it's realistic or not and I want to make it happen but I understand that might not.

**Boris**: I think it's great you and me discussed a bunch of this stuff live in Berlin and I think it's great to have this point in to be documented. I think the EthHub call, one of the things that was happening there is, that there's a group of people there that want to help tell the story of Ethereum. I think that's where the context of some of this stuff comes from. I'm happy that basically have other people to help tell the story of what's going on and hopefully people can look at the blog post that you've written and take that in and help us as a community tell the story, better. The one point that I will make is that, if you haven't already, there's the concept of the Osborne effect. Basically it was a PC in England where they had a current version that was selling really well and then they announce the new version and sales on the current version totally dropped off and killed the company. That is relevant context for exactly what we're working on here. I don't know how to fix it other than I think part of it is absolutely that we need to improve our process. But the other half that just got like basically call for help or again is please help us tell the story of how Ethereum is evolving.

**Alexey**: Thank you Boris. Another thing I wanted to propose the monopoly on the changes in the Ethereum. Essentially say okay so we have we're going to just do like really really critical changes and everything else basically has to just go away. Because we're just trying to fix the chain so it doesn't really breakdown, right? I realized that this doesn't really work. People want more changes. So once you allow one change, your people want more changes. It then started to shape up into the process for all kind of changes that people want to put in. Lot of Ethereum 1.x changes started happening in like a couple of people's heads. Nothing like we weren't really talking about these kind of changes. So I hope that now it's a bit more in the open so it was my kind of presume that everybody is following me on this mental journey. But actually I realize no no no this is not like that and they haven't really moved on. So its my mistake that I assumed that everybody is moving along.

**Boris**: Yes and we have a ton of other stuff to do like testing if we expect any of this to get in.


# 5 [Working Group Updates](https://en.ethereum.wiki/eth1)


**Lane**: I got to keep moving through the agenda. I did just make a couple of updates please refresh if you're looking at it. The next item is working group updates. Alexey or anyone else do you have updates?

##  State rent 

**Alexey**: Yeah. I'm currently still trying to test on the **semi-stateless client approach** which is basically the evolution of the Stateless client where each block is accompanied by blockproof, which allows to execute the block without any access to the state. We realize that the penality on block proof is quite large. On average it's going to be about 300 kilobytes or 1 megabytes for blockproof or block as it stands now. If we just do it for the the contract storage, it  would be about 300kb but this is it possible to reduce this by essentially making the status client slightly more stateful. By setting how statefull you want to be, can actually reduce the blockproof size further. At the moment, it is to try to figure out that what is the safe spot, how much state rule we want to be and how much of the block proof is going to reduce? The general idea that if you have a peer to peer network like Ethereum and so each peer would define what their statefullness Level would be? That mean somebody decides that they were going to store 1024 previous block proofs in aggregated format. So that means that if something has been accessed within the last of 1024 blocks or something has been created within these blocks, you don't need the proofs for that anymore because you have seen that already. They only give me the new stuff which hasn't been changed in the blocks. Well hopefully the data will show that they dramatically reduces the overhead in the bandwidth. But also it means it appears to have a bigger statefulness. Let's say that you have a big peer block memory that they would say I would keep 16000 blocks. Lets say this peer is surrounded by the smaller peer and only want to store 256 blocks then the big peer  would actually be able to generate the proofs for the smaller peers which is going to be larger. So this is what I'm trying to try at the moment. The data structure which allows you too flexibly generate the proof of any level of state. So that the peers essentially agree with each other. Like I'm going to be this stateful and I'm going to be that stateful and depending on how the like what is the what is the meaning of statefulness, they will exchange different block. This is very tricky and that I'm still working through some cases but hopefully that will finish soon. Then this week I'll put in the first EIPs in the state rent. It's essentially only deal with the some accounting of the state and also they will put the groundwork for introduction of some of the penalties for the state extension or state expansion like **creation of the new accounts will become more expensive** and the **creation of new storage items will become more expensive** in the first hardfork, according to my plan. But the biggest change in the state rent proposal for, would be that as it is very likely that we will **not charge the rent proportional to the size of the contract but simply proportional to the code of contract**. It means that we will not have a vulnerability to the dust griefing attack and we will use the approach to mitigate this. 


##  Fee market and Transaction change 

**Rick**: Yeah, I'm happy to turn in with the fee market stuff and transaction change stuff. I forget name of working group right now, but basically we're still talking with different groups, looking for funding. We have some devs lined up, but we would like more. We're constructing a budget, having a pool of devs available and interested in doing the work, would help.  Its a fairly complex change, and the changes in transactions of price. I've some concerns around testing deployment, testnet deployment. I think that we should build a reference wallet to show wallet developers on how to interact different transaction types effectively. There are also technical requirement discussion and features. Which part of the proposal we are going to implement  exactly, there's a lot of it. It is pretty clear to me that it is not possible to get into the Istanbul, given the scope of change. Like I said we're forming the group now and I'm looking for developers who are interested.

**Lane**: Thanks. Relevant to you and other Eth1.x working groups as well. I am just curious if any particular channel where you're communicating about the post budgeting as well as about need for developers? Like wiki page where everything is all laid out.

**Rick**: I'll just be frank. In my professional experience, we don't solicit the public for these sorts of things. So I don't have any experience myself nor does anyone in my staff really do that sort of thing. one of my staff might do it in future but we're not quite there yet. I want to make sure that we have at least one commitment for funding before we start spending time going out and at trashes the bushes.

**Boris**: To your meta question Lane, Alexey has been coordinating the budget proposals for the working group to look at funding. He is quarterbacking at and keeping everyone updated. On our case with the EVM evolution we've been feeding Alexey updates. So we're working on 615 to the level that we can and if emergent we can talk about that in the in the next section with that. Light work on coordinating in the sense that the pre compiles, the big question related to EVM evolution is other will be certain things including the the Blake precompile that may not need to be a precompile if we can get core clients EVM implementations tuned. We know that we either have the people who could do the work or can easily get some people to make time available if funding is available but currently funding is not available.

**Lane**: Thank you. Any other Eth1.x working group updates?

**Zak**: I'm planning on putting together the **testing working group** but I think I'm going to talk about that in testing section.


# 6. [Do people want to meet in July? (Boris)](https://ethereum-magicians.org/t/coredevs-eth1x-istanbul-meeting-july-poll-feedback/3197)

**Boris**: I'm harping on this to try and do the time lining thing because if you want to meet in July that are Late July that is now only kind of 10 weeks away and I'd really like to give people at least a week's heads up and so just trying to get a basic temperature from the room should gather together volunteers and plan to meet in July or do people want to get the work done just online?

**Rick**: I have a couple questions one are we expecting similar group I mean I guess I'm interested in meeting some 30 people minimizing the travel distance in different parts of the world.

**Boris**: My assumption is that, it be working groups and others need to coordinate that this may be an opportunity to do that together or people to meet separately. I'll make sure to add the [link](https://ethereum-magicians.org/t/coredevs-eth1x-istanbul-meeting-july-poll-feedback/3197) actually again to the voting there's the thread in Ethereum magicians so I'd really appreciate if everyone has a look at leaves a comment and just start of yay or nay has like nine lives to be online that's totally cool then I don't need to keep bringing it up but if people do want to meet we should decide soon. 
Two leading places are Seattle and somewhere in Canada. 

**Lane**: I thank you Boris. I posted the link to The Magicians thread in all the channels and all due respect to Canada, New York is currently tied with Canada in second place.

**Greg**: I mentioned it, it would be good if people didn't just have a preference but also a possibility. You could prefer one but if it's I can go to one I can't go to the other, that helps.

**Lane**: Thank you folks. Boris, thanks for putting that together, again the link is in all the channels take a look.



# 7. [Ganache/spec compliance issue at go-ethereum](https://github.com/ethereum/pm/issues/97#issuecomment-489660359)
**Lane**: Next item is by David. 

**David**: This is the issue with geth or ganache or other clients maybe. where the V and R and S what one of those for JSON RPC return. For Geth says it should be quantity but the spec says it should be data. Ganache is complient to spec, the testing against Ganache that crash there. I wanted to figure which way things should go there? **Spec should be updated**.

**Tom**: The number is generally treated as the quantity across most of the clients.

**Peter**: The complexity here is that the spec indeed says that V,R,S are just blobs, in reality they are actually numbers. SO all three values are numbers. We can fix it.

**Tom**: Because we started using it as a chain id number and that's why it is treated differently. 

**David**: I honestly am fine with any way it goes.

**Peter**: I guess the question is whether we consider these numbers as binary blobs or most of the clients accepted as binary blobs then, we've a change of a behavior. That's not a problem.

**David**: I'll go and check Parity and update the issue.

**Peter**: We should decide on the behavior of what it should have been instead of what one or the other client is doing. I think we had this debate is Felix a while back and he was the one who was saying that he doesn't really want to change it because all these three things are numbers. The question is do you want to challenge the spec or not? 

**David**: One things keep my mind that Parity handle the data both ways. Ganache doesn't care if data is quantity type, will fix it internally. But Geth is much more strict on that. 

**Peter** : We deliberately are strict on everything because based on my experience safe if you tend to accept various different things then you end up similar cases like JS. You have wiered things, if you are too permissive.
 
**Alexey**: I think JSON RPC thing have grown organically. In the begining there was no standard and now its quite hard to force the standard upon the clients. If you want to do the standard, then the way to do it actually do it non JSON standard and put JSON as an adapt to it. We also realise JSON is not optimize for everything. What I am suggesting is that we have half spec that would be in protocol EIP 63, which is basically RLP based. I am thinking that  why don't we just created a similar one with their similar kind of flavor of commands which would reach out to the note and that would be the the standardized way to get data out like about transactions blocks have you like storage and then we put the essential little layer of JSON on top of that, kind of module kind of thing. We keep the standard really tight on the RLP.

**Peter**: What you are proposing is an interface which is just a huge pain. 

**Boris**: I think there's a couple of things going on. So we are in midst of having components with specs that are spinning out and having there own repos. I know the EEA is interested in this. Oasis is looking at potentially json-rpc the other thing that I have to say is that there's many more stakeholders around the JSON RPC layers like wallet providers and other middleware . I think we should encourage those people to form around it and create specs and work with clients including how to do vendor extensions or client extensions. As far as I know those efforts are ongoing so that is happening right now and they're going to do PR's against clients if there's issues that are found. And the other thing is this is a layer that doesn't break consensus for the most part and it means there's no reason to tie at the hardforks. so that anyone who wants to work on this can work on it and improve it without any blockers. There's some coordination factors, in the sense that if clients randomly change json-rpc at different times then the higher-level middleware gets into a bunch of issues. 

**Rick**: I am in favor of stakeholders deciding amongst themselves. But I would like to get any EIP or something, I don't know to unify this this back as one of these middleware providers. The difference between the clients is like really frustrating. So if someone start some sort of project to unify that would be appreciated. I'm happy to do that for certain things but not for everything.

**Boris**: Is there an EIP already? The next step is ideally just like devp2p has been spun out into a separate repo . that the json RPC spec gets spun out  into a separate repo and people work on specifying it and the Eip then references certain versions of the spec.

**Peter**: I kind of like the idea but that one thing that was actually the testcase. We need to have the manpower to keep maintaining thing. **I think it will be helpful to spin out into separate repo**.

**Action 61.1**: Will come back on it in one or two meetings.

From [comments](https://github.com/ethereum/pm/issues/97#issuecomment-491333940) - regarding the JSON-RPC spec there seems to be on already: https://eips.ethereum.org/EIPS/eip-1474. 

# 8. [EIP 615](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2060.md#eip-615-status-draft) (from last meeting)

**Lane**: Discussed [in last meeting](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2060.md#eip-615-status-draft) and also in Berlin. Some concerns were raised about complexity.

**Brooklyn**: I think the author are happy with how it is done right now. We are looking to push it towards Istanbul. 

**Greg**: The complexity things keep coming up and the desire to split it up. And backwards compatibility. I got one last idea but I think we'll probably take care of the backwards compatibility problem that could be brought up somewhere else but **it's pretty much been ready to go for for almost 2 years now**. I think recent discussions have hammered out what problems there were in the spec so I don't see breaking it up as any help. it would stand together as one piece and when you go to implement it, it really doesn't take very much code and watch the poor things are done the little things people want to split it out or just not that hard to implement. I can't push things on to the solidity another compiler authors and then they start into that work, will probably wish we hadn't split those out.

**Lane**: I don't currently see this listed under hardfork meta 1679, so are you guys still planning to PR that in there next week? 

**Boris**: Yeah, we will PR that in. We were trying to figure out if we were going to do a last call in between but we'll just PR it in and make sure that it's been officially listed.

**Decision 61.4**: PR will be made to list it.

# 9. Testing, testnets, and road to Istanbul

**Lane**: okay we've got a couple more items left. The next item is one that we added earlier  - testing, testnets and the road to Istanbul. Boris, you want to speak to this at all?

**Boris**: I left it in so that Zak could talk about it. I just keep asking who is pushing is long since I know nothing about testing. Zak are you going to volunteer as tribute?

**Zak**: We are working on the same testing initiative with the EEA. I am trying to create a bridge between those two. Currently, I am drafting a roadmap and the list of requirements including pre and post hardfork testing. Coordination or collaboration on this from anybody who's interested or has a any strong opinions on the matter. So I can coordinate with people like Dimitry and others who have been working on testing and we had an initial call and we want to know we're going to set up another call. So  on the last call I talked about hiring a developer to help augment a lot of these and I think I found a pretty good guy so we're going to put the ball on roll. We also released an open source testing framework so check it out we're incorporating a lot of those tests into it. Another thing I need is like I'd like input from each team, we need to know who identify who the testing lead is going to be, so that we should coordinate.  I think that we should have kick-off call like next Thursday around this time and I'll share the link in the chat that a day prior and so please ping me if you'd like to coordinate all this stuff and I'll post the summary and started working group meeting on Ethereum magicians.

**Lane**: Awesome. Excited to hear that testing moving forward.

**Danno**: Is it some named testnet like Ropsten, Goerli or Kovan or is that out of the scope of the call?

**Zak**: I think that would be appropriate. So I reached out to the Goerli guys, might have called them 2 weeks ago. So I'm going to try to get them on the call as well, so we can cover that those starts too. I think its better to have a bridge between EEA and public Ethereum community, thts what I am trying to navigate.

**Lane**: Just looking at that proposed agenda. It lists August 14th as our current target date for upgrading the testnet - Ropsten, Goerli or adhoc testnet.

**Rick**: What sort of testnet EEA is looking to deploy?

**Zak**: They want to launch a testnet to confirm to EEA spec. But from my understanding EEA spec is really going to be pretty much the same thing as the public test that's back except they have an additional privacy later. So from the privacy layer down everything is the exact system. So I think that it'd be great if we collaborated on that and holding on the resources rather then implementing all this somewhere else and somewhere else. I think we should just have more coordinated efforts or not duplicating our work and we're making the most of the time spent as well.
I think the benifit of this is that EEA people have been doing it for long time. And I think that it would be great to understand what their processes are in standardizing a lot of the things that we use currently on the internet. Like for instance Charles was the guy that laid a lot of standardization for different processes and understanding. They will allow us to create a more coherent and cohesive community and ensure the adoption of this technology. 

**Ricky**: Yeah I definitely suck in that. My next question is when you talk about the privacy layer, so it is just Quorum or something else? what is it how's that being realized ?

**Zak**: The difference between what Quorum does in terms of privacy so quorum just have geth and then they have like an enclave which access like somewhat of an intermediary between these two points to similar architecture to Pantheon's. Daniel could probably speak more on that.

**Rick**: A testnet that met the spec vs a normal Geth testnet, what is the actual? I assume there's some additional code.

**Zak**: The additional code is generally some sort of privacy on plate. Something that I hear people are talking about adding different op code. I think that's really kind of like a not a very good thing to do because if they implement something that's supposed to be specific to EEA, then  they're going to have to fork that in maintaining that which is just a huge pain. I think everything will be done much more effectively and there should be a lot more coordination and cooperation between the exact same thing.

**Lane**: since we're getting very close to time, I suggest we take it to Eth magician forum.


# 10. Testing Updates 


**Lane**: Martin, is there anything on testing regarding Istanbul?

**Martin**: No.

**Alexey**: I have been talking to Dimitry quite a lot. One of part of my blog is that testing is definitely a bottleneck. Aleth is the only that allows generation of the consensus testing that is not good. You should be able to generate consensus testing out of any reference implementation. Dimitry has been working on this thing called `retesteth` which is basically talks to JSON RPC client and it tries to generate those tests and at the moment it does work on Aleth and not all the test work. So this is where I stumbled upon non-standard JSON and JSON being really bad for this anyway, because eg, if you do with over ipc then you cannot predict how long the messages and I know that Go-ethereum deals with that and Aleth doesn't. There are a lot of stuff and that's why I said not using JSON on the standard layers or something like this. I'm getting through this and so I just wanted to comment to the other bits about potentially bringing some stuff from EEA or anything. So, after observing for this for a long time I would say that if you want something to be used for testing it either has to be like a super robust high quality like AWS  or Google cloud or it has to be substituted everything open source because we have to have a ability for anybody to run this stuff. So if it requires some kind of whatever something as a service but it's not very robust and it's no go. Despite how much you want to collaborate if you don't have everything at your disposal it doesn't really work.

**Lane**: Are there any action items?

**Alexey**: At the moment, I am trying to figure out how difficult it is to integrate the test net into Go Ethereum and there are some unexpected issues to figure out. Once, done this exercise, will probably spin out some work for other clients. That would get the idea like how hard it is. 

**Danno**: We haven't done implementation yet.

**Lane**: Does anyone wants to share any other update?

**Peter**: I do have one update but that is not the client update. About one week ago, the Rinkeby testnet was upgraded to the St. Petersberg fork. I see that a lot of people have not updated their Rinkeby nodes. So, just a public shout out that you might want to update otherwise your node be just there hanging in the network. Please update people.
 
**Alexey**: I mention in the agenda. I'm going to try to prepare like a little workshop for the Dappcon in Berlin in August. The idea is to try to teach people how to become core developers. It is super experimental and would be looking out for some help. First workshop will be based on Go etherum and testing infrastructure and I hope Dimitry will be helping me as well. I will be reaching to some of the Go Ethereum team for help. I hope the people likes this idea.

**Lane**: Thanks Alexey, I like the idea a lot. I am happy to help.

**Peter**: We can also help. If anything is missing, I am sure, it can be arranged.

**Alexey**: Thank you very much.

**Lane**: Alright, thanks everyone. I think that's all we got for today.


# Date for next meeting
May 24, 2019

# Attendees

* Alex Beregszaszi
* Alexey Akhunov
* Brooklyn Zelenka
* Boris Mann
* Charles St. Louis
* Daniel Ellison
* Danno Ferrin
* David Murdoch
* Greg Colvin
* James (madeoftin)
* Karalabe (Peter Szilagyi)
* Lane Rettig
* Martin Holst Swende
* Paweł Bylica
* Phil Lucsak
* Pooja Ranjan
* Rick Dudley
* Trenton van Epps
* Tim Beiko
* Zak Cole




