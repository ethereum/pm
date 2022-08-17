# Consensus Layer Call #89 Notes 

### Meeting Date/Time:  Thursday 2022/6/16 at 14:00 UTC
### Meeting Duration: 1 hour
### [GitHub Agenda](https://github.com/ethereum/pm/issues/549) 
### [Audio/Video of the meeting]https://youtu.be/WHOZ_2tlTqk) 
### Moderator:  Danny Ryan
### Notes: Alen (Santhosh)

## Decisions Made / Action items
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
|89.1 | Someone has the bandwidth to write a quick hackmd of the, like reusing your Ropsten clients for the sepolia fork, so that in practice, someone could set it up today. and, you know, you effectively get an extra week of lead time. - Tim.| [13.15](https://youtu.be/WHOZ_2tlTqk?t=795)|
|89.2 | For anyone listening, the execution layer, the proof of work chain is having a hard fork very soon to delay the bomb. if you are a Staker, your eth1 end point needs to be updated to this and keep an eye on releases coming.| [25.33](https://youtu.be/WHOZ_2tlTqk?t=1533)|

**Danny**
* Hello, welcome to consensus layer call formerly known as the Eth2 #89. This is issue 549 on the PM repo. Here you go. Here you go. We will talk about anything and everything merger related, and then do our general updates and discussion points. If anybody has anything,on the agenda I did I put Ropsten question mark. We did go over a bit of like the post-mortem Allcoredevs one week ago.  

**Pari**
* We are been doing some sync tests and I've been just posted a quick rundown of what your extent about it. Simon, Silicon confirmed, all of these.but we should have like a proper report by next Allcoredev. 

**Danny**
* Okay, great. Thank you for that.Anything else on Ropsten? Okay, great.main net shadow fork. s it seven is happening next week? Is there anything that we need to know about that Perry or other people involved? 

**Pari**
* Yeah, the conflicts are out and everything's in the same place. It usually is. there should be an announcement message on the topic and in, in the interrupt channel and we do a TTD override throws up to date, the main idea to and see if we can replicate any of the issues we found in still Ropsten. Hopefully none of them are replicatable by now. 

**Danny**
* Gotcha. And are we going, do we have the ability to perform some of those sync tests while the transition is happening or we're not doing that? 

**Pari**
* Yeah, we're definitely going to do that as well. we've done it, I think every alternate or every third shadow folk. 

**Danny**
* Okay, cool. Great.anything on the coming shadow fork? Any questions for Perry or thoughts here? Excellent.Alex wanted to bring up sepolia genesis and TTD.There's probably two things here. One is the Genesis.The other is TTD. sepolia will be a permissioned beacon chain,which gives us kind of similar soup clique properties.And that we can decide who is in that,and can actually kind of give them a weight as well, which we don't get to do in clique.and I believe Perry that these configs are ready to go and that everyone kind of has the information on Genesis. 

**Pari**
* Exactly all the Genesis valid data should have received the mnemonic from me and the conflicts are in the Eth client slash mage test that's people.In case you wanted to be a validated genesis valid data and having received the mnemonic piece to reach out there have been some people who reached out after the Genesis date was created.we just do token deposits with them and have them onboarded later. 

**Danny**
* Perfect. Thank you.Any questions about supported Genesis? 

**Pari**
* Not yet TTD, there's one other,oddity that where we opted for and supplier,while creating the Genesis state, we set the balance to be about a million per validator and essentially using this chance to inflate the supplier.Eth supply such that whenever withdrawals withdrawals are enabled, we can just withdraw a bunch of validators and inflates a player Eth up time.there's so there's like three different ways we can inflate the supply on supplier now and we just use whichever manner,based on how critical it is.There's a bigger writeup in the, in the GitHub issue. 

**Danny**
* Great. And I think perhaps to light client for realizing this is a great time to generate Ethan,not have to manage an irregular state transition on the execution layer.Okay,now for TTD based off of Allcoredev of last week, based off of some of the conversations I and others have had,I don't believe today is the right day to do set the TTD and instead,probably one week from tomorrow after the, after, at that point, sepolia beacon chain will have launched and will have run through the main net shadow fork seven to make sure that any of the raps and issues are no longer standing.and then at that point can make a call.I think so we don't need as much community lead time because this is more of a controlled test.I think that it's maybe worth talking about,is that plus one week or plus visit plus five days from that point at which we're comfortable doing a TTD or a week and a half, is there any technical or coordination reason for one or the other from this group? So pretty much tomorrow's Friday plus one week probably decide TTD , mainnet 7 went well,and then is something like four or five days lead time sufficient.So that we'd have the fork in the middle of that following week or, is it, does it need to be more something like 10 days? So that's the middle of the following week after that? 

**Tim Beiko**
* So the Ropsten then TTD override, we published five days or so before the fort.so it feels like maybe that's also a sufficient and,this is maybe a weird question, but,is it if somebody really wants to like, get ready for this, is it possible for them to run a cl version, which has the high support sepolia TTD then like a Ropsten EL version and simply do a TTD override on the Ropsten or like whatever laley EL client version that they have. I feel like that would work. You might still hit some of the bugs on Ropsten. Didn't like, obviously there were bugs in their clients on the ELL and you didn't upgrade, but like, 

**Danny**
* So in terms of releases, not like that, you sync drops and gotcha. 

**Tim Beiko**
* Yeah, exactly. It's like, I think, cause the sepolia thinks like less than an hour at the sync. So yeah, it might be 

**Danny**
* There's no, there's been no breaking changes with respect to the spec. So, you know, you could probably even use a client from four weeks ago.yeah. So I think client releases today should work, but you know, there's rapid iteration on fixing. 

**Tim Beiko**
* Yeah. That'd be cured. That's the EL client where the CLS you'll need to download a specific version, which has the TTD, which has the Bellatrix forks activated. 

**Danny**
* Correct. But that can probably also be handled in a config. 

**Tim Beiko**
* Right. Okay. 

**Pari**
* I think some people who are setting up their nodes have just opted to use the custom network stuff. So you just pass a testnet and pass the Genesis data to each other.and in their scenario they would just change the TTD override flagging that could. 

**Tim Beiko**
* Okay. So I feel like, you know, if we do do this just five day delay,I don't know if someone has the bandwidth to write that quick hackmd of the, of like reusing your Ropsten clients for disappears for it.so that in practice it's like somebody could like set it up today.and, and, and, you know, effectively get like an extra week of, of lead time. 

**Pari**
* Yeah. I think we have a TTD overnight drill document that Mario said made a long time ago.I guess it goes repurpose that that should be it. 

**Danny**
* And our sepolia beacon chain releases. Are those out? Are those still like coming in Monday,Tuesday? Like those cut proper into clients. 

**Pari**
* I'm not sure if all the time team's capabilities, but I know some of them do, Chris, some  with this in the next few hours, so yes, we'll read this to You tomorrow. 

**Danny**
* Right. So Tim did, to your point, even by tomorrow, they might not even have to do anything except that TTD override and not doing any of the custom can fix stuff. 

**Tim Beiko**
* Yeah. So we could probably like put together a hack MD tomorrow and like share it either tomorrow or Monday. And that gives people who are really interested,like an extra four or five days. 

**Danny**
* Yeah. I think that's a good call.okay. So it looks like no technical or coordination reason to do more,to do a longer delay than five days from Allcore devs next week from this group.I guess it's probably B if there's any sort of technical reason to block that, but I think that timeline makes sense. Okay.anything on sepolia Genesis supply TTD,before we move on to talking about MEV builder network testing.
* Great.okay.Alex, you have an issue up in the builder specs and want to talk about testing,whether it be on sepolia Gourley shadow forks, or otherwise, can you give us a quick on that? 

**Stokes**
* Yeah, definitely. So, yeah, I was talking with some of the flashlights team and they're obviously looking to like tests, you know, their software, as we do the different merge testnet.So I guess the first thing is, yeah, immediately.I was wondering how people feel about doing this on sepolia.I know there's like different amounts of, you know, different teams are in different places in terms of implementing, there required parts of the specification.So I'm wondering if anyone has any thoughts that,separately there is this issue of, cause we'll want to actually agree on, basically delaying through the transition and, just having consensus around how long we do that. 

**Danny**
* So do you have a particular question,is, is the question if clients are ready to do so, or I can give an update on the prism side of things. 

**terence(prysmaticlabs)**
* So,we, so we have been working on, but the progress has been slightly slower just due to like the coming parts with the current,local Yi and stuff like that. So yeah. So all this progress is that we're able to use the roughs and relate and we're able to simulate like an end to end workflow with registration to, to register with the registration who,gave a load and, and the, to the same block. So, yeah. So,I think we're still like one to two weeks away from like putting this into the, put, putting this into a release because we do want to test it as a story as possible before like with these stats, with the public. 

**Stokes**
* Yeah. That makes sense. So might be hard to ship for some sepolia is what it sounds like. 

**terence(prysmaticlabs)**
* Yeah.That's true for prism, but I'm not sure if that holds for other clients 

**Ben Edgington**
* Sounds like we're in a very similar place with, take, Enrico can probably,give, 

**Enrico Del Fante**
* Yeah, we, we are, we are not yet testing Ropsten, but, the, from the implementation point of view is done and he's ready working for the keel network.so,so we are still in testing, but the, the, the flow has been, has been tested already and it's supposed to work Deployed on Kim. 

**Lion dapplion**
* So the little being an external dependency,would it be even possible to test that with something like so that all clients can benefit from that testing infrastructure there's, like, open source implementation of a builder and a relay that clients can run locally as well. 

**Danny**
* Does that mean,it sounds like in terms of sepolia like, we're not gonna be running this on the bulk of machines, but that maybe there's some experimental or, not quite merged branches that maybe we can run on a very small number of nodes if there's interest. 

**Stokes**
* Yeah. That sounds like the way for sepolia. Yeah. 

**thegostep**
* Yeah. I'd say any of the client teams that have something that they want to test. I think there's huge benefit of trying it out during some sepolia and having a couple of validators running it, even if that's not necessarily deployed to merge on their master branch or anything like that.I see, like from the far far perspective, there's two things that we're worried about.One of them is making sure validators get the chance to,and particularly the validators that are going to be running the main net merge, get a chance to set this up and run it at least once on like a live test net merged simulation.and then the second, which has,I think what we can achieve for polio is just confidence for the,the consensus client teams that, that they're able to run it.so, you know, ideally it would be some sepolia consensus, client teams running my boost and connecting to relay and sort of getting a chance to test their infrastructure there.And then for Gordy then we have,like actual third parties running this. 

**Stokes**
* Okay.So that brings me to my next point, which was the issue that Danny dropped in the chat. So we had talked about this, some, I think over discord connect with some of you different parties. And basically the idea is that, you know, med students does add this like extra sort of, operational surface to what we're doing.And so in terms of keeping the complexity of the merge down, like the actual, you know, running your software through the transition,we decided to delay running med boosts. Like it would essentially be hard-coded into clients to not use that software sometime after the transition was finalized. So, I kind of have the very beginning of PR and this issue,or I just said, you know, we'll delay for 16 E-box we can decide what that number is.I suppose I want to know if anyone thinks we should not do this. And then if we do do this, you know, is this a good number? Should it be longer?I think 16 is like around an hour or so six starting point 

**Dankrad Feist**
* Who enforces this? Like,what if I, what if someone manually disabled that will they, I mean, can't, Can't stop. Yeah, sure.I'm just wondering in order not to create this race to the bottom, if it would be possible to set us, tell flash pots not to serve any,blocks during that time so that people.

**Danny**
* By the local software.not necessarily respecting it, your intro, you introduced the live testing of an alternative case where the relay looks down rather than it, just going locally.So I think it's good for the clients to also respect just kind of bypassing the flow, even if a relay is not serving. 

**Dankrad Feist**
* Sure, sure, sure. I don't disagree with that. I'm just saying that like, I'm worried that many people might be tempted to disable us,because they think, oh, like that's probably when they will be, I mean, you can literally hit the jackpot during that time. Right.so if you could someone, do we have currently any other Relias other than,flash pots in there, whatever. 

**thegostep**
* Yeah. I mean, answer a couple of questions here and maybe provide some context.I think it's definitely possible for flash balls to just like turn off really for,an hour after the merge, but there are going to be implications, right? Like whatever MEV that is not going to be attracted to like boost around the merge will be extracted through PGA. And I've already talked to a few funds are inquiring about like how long this delay will be to like measure how much they want to prepare it and invest into like things like the network through, through PGA.so there are the delaying,Referred guests auctions. 

**Dankrad Feist**
* I see. Yeah. I mean, like basically, but I mean, my, my thinking is that for one hour, like for the vast majority of people, or even staking pools or whatever, it won't be worth like implementing their own, special MEV solution. Right. So if we get some sort of a voluntary moratorium of relay us during that time to say, we don't serve any blocks,then I think that would be a fairly stable equilibrium for people to just not voice too much about that time. And yes, like maybe you get that. Yeah. I don't know. 

**thegostep**
* Yeah. I agree. I don't think I don't expect any of the validators to try run custom software, but I do expect the operators to prepare for the merge,through the transaction. 

**Dankrad Feist**
* That's fine. Right. Because that is, that is out of consensus layer. 

**Paul Hauner**
* So that's in a way, much less risky for us would be my feeling Paul, from lighthouse here, I'm generally in support of,I've just trying to disable this while we get through the match. I we've got a lot on our hands and just removing variables from it.could, could pay dividends. 

**Stokes**
* Okay. I can turn a, I can make like a formal PR to the builder spec and yeah, we can go from there. 

**Danny**
* Thank you.and on the sepolia people running this on a small number of validators, if prepared is the ball in the court of client teams to carve off a few validators and do a sequestered node to do so, or,is flashed bots or somebody else's wanna help support this, any, any feeling one way or the other. 

**Paul Hauner**
* So what was the question again, Denny,

**Danny**
* Testing during the transition?  I don't, I don't know if anyone's gonna be running us in the bulk of validators, but there was some desire to run maybe experimental branches on a very small number of validators. Would you handle that yourself? Paul or we're looking for somebody else to handle that? 

**Paul Hauner**
* Yeah, we'd probably just run it on the valid as the way I located, I would say. Okay. 

**Danny**
* Okay. Anything else on sepolia builder testing? Great. Okay.anything else on the merge in general? Okay. For anyone listening, the execution layer, the proof of work chain is having a hard fork very soon to delay the bomb. if you are a Staker, your eth1 point needs to be updated to this. so keep an eye out for releases coming, I believe, at the beginning of this coming week. 

**Tim Beiko**
* And they're, yeah, so They're coming out sooner,Everyone except besu, you already has a release and bases release will be out today.so three out of the four yells have a release and we'll have a blog post live, as soon as, as the basic releases out, they're having some CI issues, but,yeah, today or tomorrow at the latest. Okay. Yup. 

**Danny**
* Okay. So upgrade your proof of work node. If you are a Staker upgrade your proof of work node period. Okay, great. moving on. Any client updates would like to share. Cool. And yes, I did say youth one because it's literally called that in terms of the CLI parameters.great.No other client updates,research spec, other technical points of discussion today. 

**Mikhail Kalinin**
* I have a small update on deposits processing post-merge, yep.Yeah. So there is a document, the proposal that they have been recently looking into and working on with Danny,I can briefly share my screen and go through it if you have a time for it now. Great. Okay.I'm sharing my screen.Can you see my screen? 

**Danny**
* Yes. 

**Mikhail Kalinin**
* Okay, cool.deposit process in post-merge.So there is a lot of things.There is a lot of,a lot of space to improve on it after the merge, because we don't need to have this bridge between the two blockchains anymore.and yeah, just go in briefly through the key things of this proposal,sorry.on the executional side, the idea is to surface deposits data into the execution layer block. So basically the execution of their client will go through the receipts that it got from the block execution, filter them out by the,by the address by the contract address. And then, filter out, deposits out of this queue of receipts and add them as deposit operations to the block body.additionally,there are a couple of, validation rules.one is to like basically the consistency between deposits and deposits fruit in the block header. The other one is to verify that the actual deposit, the, the actual list of deposits matches the one that was, grabbed from the block execution,and, the address of deposit contracts and this, set up, moves to the L side. So it becomes a network configuration banter on the L side on the consensus there basically we'll have the deposits now,it's called deposit received to avoid confusion between deposits structure that we already have, and this new one. So what we may call a deposit by the end of the day,there is the, deposit queue in the beacon state. yeah, first of all, there are deposits, in the execution paywall that we get from the execution layer.there is the queue in the beacon state that cues, these deposits from a log and the attempts to process them, in the block after. so yeah, here is the, persistent in deposit methods. It's basically, similar to what we have currently. we don't have to verify the Merkel proof anymore, because we don't need at all to proof anything. the validation happens on the EL side.yeah. And yeah, that's basically it. Yeah, there is the process block. we can still rate limit, if we want to rate limits, the computational complexity per block, we're still getting ready to limit the process in this queue,by a max deposits, but I don't think it's necessary because, the computational complexity has already reduced by removing the Merkel prefer verification.So this, like one of the things that can be removed,the, the queue, 

**Dannny**
* Even if you do process them all, is still valuable so that you delay them by one slot. So that execution and, and consensus layer can be run in parallel for given slot. Correct. Or is that Yes. 

**Mikhail Kalinin**
* Yeah, yeah, exactly. And we could pre process the,them in the same block. Right. But we can process them in advanced, but, like, optimistically process deposits. the problem here is requires BLS verification, which is having, and it may affect the, proposal,flow, right? So we get deposits, but get the execution bailout first from the,from the, then we have the deposit, we'll have to purchase deposits before the computer in this state route, the state route of, after, upon a beacon block. And here we have this VOF B BLS verification, which is hot and heavy operation. That's like seems to be the only reason to have this, you know,to have this delay between processing and induce ed in them to be,to, to the begin state they are there. yeah, so that's basically the mechanics, the missionary, after, after the merge, after, how this, of this new mechanism, but we also have to, handover from the, to the new one. And here we have this, like a kind of transition period. the idea of this transition period is to stop doing one data call, when we have, induced all, when we have processed all the deposits from,from, from the previous, from the, history, before this, the missionary started work. So there will be a time, the period of time where we'll have both, things happening, but then once the one day appall starts to overlap, the new, blocks, featured with the deposits on the execution side. So it will just stop here is the logic that may work for this transition.and then we may, like, after this transition is done, we made the pre-K all the logic it's one day to Paul and, that, that sentence supports. So like, there is a question of data complexity here. So it's obviously, deposits on your side, will increase the, the execution block size and we'll increase the history and we'll, and we'll increase the,max amount of data to gossip, as a part of free block gossip. so if, yeah, if we take of, of, overall size of deposits that we gather until today, it's like 75 megabytes. So in terms of like historical date, it's like really marginal increase. but what we would like to look at is the, how much, how many data, in addition, we, have to heat on the network, if we use this machinery instead of the previous one. So it's like, yeah, I,I used to like put a meter on gassed as a limit. If we like have a full block of deposits, it's going to be like 95 kilobytes of data in addition, on, on the El side. So, but, we have this, you know, currently we have like, have to go sip, of the,the amount of deposit data we have to go say, like it's 90 kilobyte at max. So the increases can be computed here, easily.but I don't think like it's a big issue, because,we have, we can have like temporal increase and somebody may try to,abuse this and attack the network with like, throwing a lot of deposits and making like a block full of deposits just to delay block, but it told just be one block or probably two,one thing, whereas, mentioned here is that we have one Eth as a minimal deposit announce, which is a big limits, big restriction to these kind of attacks.and also, yeah, worth mentioned here that, since we don't have this miracle, proof anymore in a block, over, like the complexity of the data complexity per deposits is reduced by a one kilobytes. So this kind of thing. So what, thinking on the deposits, on like data complexity side, we would have a deposit queue, on inside of ELL state parts. It will need probably, more, work and to add would add more implementation complexity. We haven't done anything like that yet, to the Allstate.so that's kind of it's, yeah, but overall, what, advantages this proposal has is there is no deposit cash and it's one day then voting and other things that are really,implementation complex and requires sophisticated innovation of deposit to queue and managing this queue and agreeing on a block and supports also, which is nice deposit separatists, like literally in the next block.so which require a special transition logic and the data complexity, but I don't think that data, the complexity is like a big issue,from, from, from, from the perspective of this, proposal, yeah. It's well, the required transitional logic, but, that's where it's doing it's and yeah, some work on the El side, so that's kind of it,yeah, and, we're not, the other way to like improve on the deposit processing flow is to reuse the existing it's one day the machinery.but, if we reduce the,follow distance a lot, like say to one block or two like 10 blocks of a tablet to one ephoc,then clients will have to manage reworks and, managing reorgs, in a deposit cash is kind of like pretty calm sounds, pretty complicated from implementation standpoint, could be a source of like new box and,we are not considering. 

**Dannny**
* Yeah, I, I was, I kind of liked the idea of making Ethan data just to validity condition that was, and you just do it every block and you can just update things every block, but then Mick out pointed out that then you'd have to handle, we assume no reorgs and that deposit cash implementation that deposit cash implementation has been buggy and source of issues in the past. And so having to re-engineer that to assume reorgs would be probably not the preferred path. 

**Mikhail Kalinin**
* Yeah. That's kind of it, I'm happy to answer any questions. 

**Lion dapplion**
* Anybody does have them The extent of what we're saying. I think I'd leave lost out in other implementations, do the assumption that index number and would always, and always correspond to the same public key Validate or index. Yes. Because so the, the cash for keys and uncompressed case is handled separately and is a global instance, at that store, the states. So not having that assumption. Yeah. It would require a definitely a huge engineering efforts and definitely higher memory costs. 

**Dannny**
* Does this change that assumption? I'm sorry. 

**Lion dapplion**
* I think so. So if I understand if you're person, if you processes the deposit on the next block and does that mean that that can get reorged and then another deposit could take that specific index in the processing model. 

**Mikhail Kalinin**
* Oh, I see what you mean. So yeah, I get it. So there is the cash. Yeah.that's a good point. It's like pretty similar to deposits. So,there is a cash of whether public keys.

**Dannny**
* Yeah,right.I see. 

**Mikhail Kalinin**
* Yeah. That's a really good point. 

**Dannny**
* And either of these, any method that does quicker,processing would have the ability to invalidate that cache because you had every orgs on the execution layer within even a few block steps that could reorder deposits. 

**Lion dapplion**
* Yeah. And also that it's another optimization regarding exactly this, that we are going to implement that mingles have, that they consider the, so the section of the state of the violators that only includes the echop key that we throw planning cells is strictly up and only list. 

**Dannny**
* Yeah. Good to know.I suppose there could, you could instead,have the deep queuing of the deposit queue based upon finality.if that greatly changed the engineering requirements here, in a good way,something like that could be explored. 

**Mikhail Kalinin**
* Yeah. But you have to look for pub public key, not so that's the main point of this,optimization, I guess, the main use of this cash. So you have to like, I have to update it and keep it up to date,even posting analogy. 

**Dannny**
* Right. Right. But if you don't, if you only DQ deposits that have been finalized in the execution layer, then you're only adding a pending keys that are not going to be reordered, which I think is the point. 

**Mikhail Kalinin**
* Oh yeah. I see.So it's like, is it easier to,the size of a while there's that are like of deposits, which process is not yet finalized as much less than the size of all the, 

**Dannny**
* Okay.Thanks Mikko.does anybody have any questions or thoughts, Miguel? Can you, is, did you share the link? Okay.You did. Okay.if anyone has a chance to review it, McConnell and myself would be happy to chat about it and the discord. And if there are further questions about the proposal,as it evolves in the next couple weeks, we can chat about it again in two weeks.Okay.Any other research spec or other technical discussions for today? 

**Saulius Grigaitis**
* I have a question.Maybe somebody can recommend some, some improving to simulate forks off after the ,merge.So prefer to have a little bit different clients.Is there something like that? 

**Dannny**
* I mean, to set up, Sorry, these are proof of workforce right before the merge or, oh, I missed it. Sorry. 

**Saulius Grigaitis**
* I mean, you are looking for some tooling that would allow me to set up a network post merge network, that would allow it to simulate the deep forks after the merge and  with the behavior of defiance. I mean, some, so maybe somebody's already, there is available setups. 

**Ametheduck**
* The easy way is to just, you know, generate a network with a bunch of validators, run two nodes and shut one of them down, which has, you know, more than one third of the validators and the other guy will not finalize. 

**Saulius Grigaitis**
* Yeah. Maybe some scripts or, or some configurations with, within some tooling

**Dannny**
* Great. So, you know, there's the ability to do, to do these types of maybe partitions and then resolving partitions in hive, but that's a more of manually writing these tests and then,can, kurtosis be configured to have a partition for some amount of time and then be resolved. Cause that would, that would also be allowed to have a deep port. 

**Pari**
* I think you can't do it right now, but it's on their,on their agenda to add networking stuff to it. Right now you could start a kurtosis run and just do a Docker stop. So essentially you have half the network offline.but that's the best you can do. 

**Dannny**
* Yeah. So that's not, but that doesn't end up with a fork that ends up with a large resolution.Thanks.Okay. Oh, they're technical discussions for today. 

**Tim Beiko**
* We have a 4844 for a breakout room tomorrow. If anyone here is interested,post the link in the chat. 

**Dannny**
* Okay. Any other discussion points on anything at all? Great.I mean, not shut off work seven,I believe next week.And then,towards the end of the week, we'll be discussing potential TTD number and have to update clients with you and override,targeting the following week.Assuming things are going well.Thank you everyone.Talk to you soon. 

* Thanks everybody. 


----------------------------------------------------------------
## Attendance

- Danny
- Leo BSC
- Vitalik
- Grandine
- Paul Hauner
- Jacek Sieka
- Mamy
- Adrian Sutton
- Lion dappLion
- Patricio Worthalter
- Carl Beekhuizen
-  Lightclient
- Nishant
- Dankrad Feist
- Justin Drake
- Cayman Nava
- Mehdi Zerouali 
- Cem Ozer
- Terence
- Hsiao-wei wang
- Aditya Asgaonkar
- Alex Stokes
- Mikhail Kalinin
- Barnabe Monnot
- Zahary
- Pooja Ranjan
- Ansgar Dietrichs
- Proto Lambda
- Ben Edginton
- Leonardo Bautista
- Arnetheduck










