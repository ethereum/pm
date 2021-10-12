
# All Core Devs Meeting 123
### Meeting Date/Time: October 1, 2021, 14:00 UTC
### Meeting Duration: 60 minutes
### [Github Agenda](https://github.com/ethereum/pm/issues/391)
### [Video of the meeting](https://youtu.be/-8TSQCwITA0)
### Moderator: Tim Beiko
### Notes: Alen (Santhosh)


## Decisions Made / Action items
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
|123.1 | Tim would add a Difficulty bomb proposal for the December upgrade. The upgrade will be named "Arrow Glacier" as proposed by Axic | [16.00](https://youtu.be/-8TSQCwITA0?t=991)|



**Tim Beiko**
* Okay. Hi, everyone. Welcome to All Core devs, call to #123. I'll share the agenda in the chat here. we don't have a ton of things on the agenda today. yeah, just, some updates on the merge, updates on the December fork. And then there were a couple, EIPs that, we hadn't had time to discuss for the past couple calls. and I think we'll probably be able to get over to them today. so first on the merged side, Miguel couldn't join the call because they're both traveling. I've seen that like various client teams have started working on, implementing EIP, 3736 , as well as the, the merge, API. yeah, I don't know if teams just want to share generally where they're at right now with, with supporting, the the execution side of the merge. 

**Justin Florentine**
* Okay. Hey, this is Justin Florentine from Besu team. We are currently in testing on that. that's one of the things that's going on for our onsite folks. I believe we've had, success, interacting with Geth and Besu basically as far as tech is concerned. 

**Tim Beiko**
* So sorry. So Teku, who has interoperated with Geth and Besu, basically that's yeah. 

**Justin Florentine**
* That's yes. That's a better way to phrase that. Thanks.. 

**Marek Moraczynski** 
* Even Nethermind, we are passing those vectors provided by Marios and two, we are still have some work to do, and we want to run at  Nethermind. We've one of consensus clients. And so, yeah, that is the plan. 

**Tim Beiko**
* Cool. 

**MaruisVanDer**
* Yeah, Yeah, go ahead. I've implemented the spec and I created some test vectors for the other teams to use, helping them, implemented. I haven't started looking into, consensus layer client yet, so I don't know what's with whom we interrupt right now, but I think it's Teko and lighthouse. so, yeah, things are chugging along. 

**Guillaume**
* I don't, I don't see Peter in the, in the chat, but it seems he has also made some progress on the sync algorithm to be confirmed, but, yeah, it looks like 

**Tim Beiko**
* Cool and I think, did I see Andrew? Yeah. Andrew, has there been any update on the Aragon? 

 **Andrew**
* Sorry, what is it about, the merge? sorry, we still have to start working on it in the, you know, 

**Tim Beiko**
* Got it. and I see Peter just joined, Peter, right before you joined Meritus was, or, sorry. was saying, there might've been some progress on the sink for the merge. I don't know if you had any updates you wanted to share it there. Yes, 

**Peter**
* It's done 

**Tim Beiko**
* Love it. 

**Peter**
* No, so essentially just a very, very quick update. and we can discuss the launch, next week. I mean the same  details, but the only update is that, now Geth, I mean, it's not obvious to you and all the older or the disclaimers about bugs and whatnot, but essentially what is functional is that a Eth2 to client can announce a new had Heather arbitrary money or few or whatever, and Geth will actually do a full reverse other thing too. So from the beginning, from that anonymous, Heather, up to the Genesis and the backfilling, whether it's full sync or snap saying whatever, and the whole thing works and you can leave to fight and keep announcing, you have had, there are some Geth to adjust peep switching. And if you, if the, if the client's analysis a form and get flow switch, and pretty much yeah. 

**Tim Beiko**
* That's yeah, that's awesome. I know Felix had the sync spec, that he shared like a call or two ago. have there been any changes to that or is that basically what you implemented? 

**Peter**
* I know I basically implemented a much simpler approach that I've been working on for the past three months. so on a Felix Felix shared that, that you can essentially leave to clients. Any clients can optimize a lot of things. If you take into consideration finalizations and whatnot. For me, I went with a really simple approach where there's no assumption and there's almost no requirements from either side. I mean, if the client just gives us, then you have had their hand that's enough. We don't care about anything. If you have other API calls, maybe you can optimize it. But my goal kind of wants to make the bare bones thing works all in there. And if via a few other API calls, we can make it a bit nicer. It's okay. 

**Tim Beiko**
* Got it. Yeah. That's, that's great. there's two questions in the chat. one, do you have a PR number and two, how long does a reverse sync roughly take? 

**Peter**
* Well, okay. Yeah, er, I just opened up the PR against my  thing. the problem is that it's, it entails insane overalls of guests in terminals and request ID handling and everything. So it's a, it's a 5,000 item, as for how long it takes. I mean, I tried to mainnet that yesterday and downloading all these reverse headers to maybe 20 minutes after which you just start backfilling them like normal snap saying would do, or kind of forcing just obviously you don't need to read down the Heathers anymore because you already have them. So my expectation is that, I mean, synchronization will take the same amount of time. It takes currently does nothing but specifically in Delta to make it faster or slower. 

**Tim Beiko**
* Nice. yeah, that's, that's really cool. anyone else have questions on, on that? Okay. anyone else had just general updates. They wanted to share about the merger questions that they have or problems they've come across. 
* Okay. yeah, so I guess people can expect more progress on that in the coming weeks. but it's good to see all the teams are kind of starting to, make, make pretty serious progress. so next thing on the agenda was, basically the December fork. so on the last call, we, we discussed a bunch of smally EIPS and, because there were small and some of them kind of added a lot of value immediately. we, we wondered, you know, should we have these at a December fork alongside with the difficulty bomb? the challenge there being that if we do introduce, another fork, or sorry, another EIP in a December fork, we'll actually need the fork, all of the test nets rather than just mainnet because, the difficulty bomb is on  mainnet that, and that would add a lot of overhead and, and require client releases to be ready quite soon. 
* So I, I reached out to all the client teams, in the past two weeks to basically see what they thought about it. and basically everyone agreed or at least a three out of the four teams, you know, preferred not doing anything except from the difficulty bomb. one of the team was, was just pretty much indifferent. I know there were some issues raised about, dos vectors for 3860 with the ANet code. the teams, the teams that were most effected felt that they could kind of mitigate those issues. and, and you know, that it wasn't the end of the world, if this EIP didn't make it in until after the merge. so I guess, you know, first of all, like I just want to leave the space. Does any client team kind of has, has any kind of team, like just changed her mind on that? Or does any one, like still feel strongly? We should push for a December fork that has more than the difficulty bomb. 


**Justin Florentine (Besu)**
* Okay. Nothing's changed on the Besu team. 

**Tim Beiko** 
* Awesome. Thanks. Okay. So if anyone feels, or if no one feels really strongly about that, but I think the next step just to provide clarity to people would be to create, an upgrade, for December and name it. So, I think Yanxi had proposed Aero glacier as a name, just because, we use Muir glacier last time, for this, for the difficulty bomb only upgrade. And also because people have started associating Shanghai with a fork that will have a bunch of, of new features in it. So I think it allows us to just keep talking about Shanghai, even though the date is, is, is obviously not set. but also just highlight that there is something happening in December. so, and we should create just an EIP there to delay the difficulty bomb. 
* It's probably still early to decide by how much we want to push back the difficulty bomb. but, I think we basically need to do so in the next month. So that towards the end of October, we have a value that's been updated across all of the clients. And then, two weeks later, we can have a client release November, with the actual fork block and, and, and EIP implemented, so that people have a couple of weeks to upgrade before the bomb goes off. so I'm happy to create the, kind of the, the spec for the, for the upgrade and to also create the placeholder EIP and, and, you know, talk about different values by which we could push the difficulty bomb. I think we'll know better in the next two, three weeks, you know, how many months we want to push it by. so yeah, we can discuss that then. yeah. Does this generally make sense to people that people have strong oppositions to it otherwise? I'm happy to go ahead and do this. 
* Okay. No one objective. That's good. so okay. By the next, next call, all all, I'll have all of this so we can properly review it. and one final comment I'll highlight is, said that, if we do just the difficulty only four in difficulty bomb, only four in December, it might, help extend open the Ethereum and the life where a lot of people would be able to just add simple support for that. and because it doesn't require much additional testing and whatnot, it's, it's quite an easy change. so alone also give an extra couple of months to everyone who's still transitioning out of open Ether yeah, if we, if we go that path. 
* Cool. So, that was quick 17 minutes. The two big things on the agenda are basically done. we had, two, I guess, three other EIPs that, yeah, we, we, we've just, haven't had the time to discuss over the past couple of calls, so we can run through them now. first was EIP 3436. this is about the clique blockchain, the clique block choice rule. I think Daniel, you're on the call. Yes. I know you're on the call. do you want to give us some context and just kind of share where, where we're at with this? 

## EIP 3436 updates [19.40](https://youtu.be/-8TSQCwITA0?t=1177)

**Danno**
* Yeah. I brought this up back in March, and there was promised to take some of that, a session to the, if they're , I got only one response that our, to that reply it it's basically got quiet. but the big impact of this is, you know, earlier in the year, the Gourley network had a couple of natural halts because of the way that clients can choose, which blocks to follow when they detect a fork, that the, all the validators can split into basically two groups. So what this, EIP is doing is establishing rules. When you see two forks, a priority list of how to choose which one to go to. And right now the only, rule that is universally implemented is the first rule, which is of course pick the heaviest chain. And the second rules would be to pick the shortest chain. 
* That's a rule that gets implemented that's outside of the spec. so this EIP would have tried that in the spec, but then to ensure that when you see a series of forks, because it's possible still with that rule to have two equal link, forks that could still help the system. So that's the point of the third block, which is to look at the current epoch of the last 3000 blocks, which everyone who does click should be fully aware of and pick the one. I think I've gone back and forth on it. but basically the one that, as it's currently written, whose validator is least reasonably had an intern block assignment, and that's designed to maximize intern block assignments. And there's a formula that I think when people read it, they miss to determine what that step three means. 
* And then the last one, of course, if there's still a tie after all of that, because the most recent least recent intern lock producer produced two blocks on that chain, or how is obviously change producing blocks, is to choose the one with the lowest hash. And the hash is of course, the last step to present hash rates between different clients. So up to step three, you're narrowing on a specific validated just block as you choose. And then you pick the one with the lowest hash, any event that they're producing multiple hashes. So if the client's following click where to implement this, these natural hops would not be occurring because in the presence of a fork, the clients would have a rule as to which one to go down. If they're aware of the fork, it's a full net split. I mean, you can't solve that problem, but if this split comes back together, you're not going to stay on separate fork, simply follow this. So this is something I would like to see declines implements. and so I really need, you know, I think I've got a PR ready for basically to go at once. This is a pre so really just Eric on and Geth and, Nethermind would need to, give feedback on this before it would be adopted in the beat. My thought. 

**Tim Beiko** 
* Thanks for the context. Thomas has a comment in the chat saying that they're thinking about implementing this for the merge, because it would simplify the merchant testing clique. anyone else have thoughts? 

**Martin Holst Swende**
* Yeah. sorry. My mind hates it about this. I recall starting to implement this bomb point and there was some snag about it, which I don't recall it right now. Do you know, directly what, like, what are the hidden, if there is an, a hidden pitfall or snag, in this proposal. 

**Danno**
* So when you decide which is your fork choice detection, logic,  to have the status of the current, click epoch, of who the validators are and what their slot assignments are basically, with that, the clip, you know, the mod of the validators of the current block. So when you do that choice, you're going to need a pthat information through. And that's probably where the hard part is. That's where the hardest part of basically this is ping, that logic into the fork detection, logic. And, because basically does auditoria to, we just have multiple subclasses. So we need to switch out for plain on proof of work, because keep the proof of work one, and then we can put the fancy click for choice rules in. So if you're, if you don't have a plugable architecture there, you're gonna need to have some flags to say, well, this is a pouch. I don't do these checks. So those are only real s are gonna be. 

**Martin Holst Swende**
* So I think I Remember now that the catch was that there is no four choice rules per consensus, and then it's, there's some global pork choice rule, but with the changes that Gary made for, for the new consensus engines for the merge, I think it reflected it. So we have, you know, a pluggable consensus engine with that with its own portray through. right. So, and with that, it was a much easier to that. You're also cool. 

**Danno**
* Good to hear. So unless I'm hearing objections, I'll clean up my patch on base suit and try and get it in for the next major release. So, because another thing about this is this it's compatible with people without it, it's just, we don't get the real value until the majority of the validators implement these four choice rules. 

**Tim Beiko** 
* Cool. So I guess there's, it makes sense. does it make sense? It seems like I don't get, can implement this. you can implant it in base soon that nethermind is thinking about doing it. So, it seems like people want to implement this. I'm not sure how this gets like accepted into the clique spec because clique itself is another EIP. so I guess I'm not sure what's like the process to make this like part of the spec and, and also the type of delay around that, given that like, people could just implement it when they want, so, yeah, I know. Do you have a feeling for what you would want the next, like official step to be here? 

**Daniel**
* It's hard to say because, you know, Mike is not big on amending previous EIPs, so we could put a reference in EIPs of clicks saying, for, please use this for the four choice role, but not actually merge it into the clicky EIP. I think the people who really care about the EIP process, aren't on a call quite right now, but I think probably the thing to do is to move it into like, the final call and leave it there until we have everyone's implementations and then close it off. 

**Tim Beiko** 
* Yeah, that seems reasonable. So, okay. Let's move this to last call and, yeah. Keep track of the different clients who implement it and we'll move it to the final once. basically the, the four clients here have had implemented. 

**Pooja | ECH**
* So I would like to mention one thing he had when the proposal was originally proposed, it was under the networking type, now it has been moved from networking to core because it was believed that it's going to bring some of the consensus changes for, clique part. I'm wondering if that would be following the usual core EIP process for getting maybe a part of the upcoming upgrade. 

**Tim Beiko** 
* Well, because it's a clique it's not going to be. 

**Pooja | ECH**
* Yeah, on the mainnet. 

**Danno Ferrin**
* And it's a very compatible, it's not a hard fork. It'd be more equivalent to a soft fork because you can come onto a network and not have this implemented. And for the most part still participate. So it's, you're not going to be too surprised. You might take a while for you to figure out what the real light chain is, but eventually you'll figure it out. 

**Pooja | ECH**
* Sounds good. 

**Tim Beiko** 
* Okay. yeah, there's a question about, like, not sure if this should be a core EIP, Daniel, do you know off the top of your head, if the clique EIP itself is Core EIP? 

**Daniel**
* I know. I don't want to look it up. 

**Tim Beiko** 
* Okay. but I guess regardless of the actual stat, category, I think it makes sense to move it to fi to last call now. and then move it. The final ones clients have implemented it. Does anyone object to that? Okay. Yeah. 

**Danno Ferrin**
* Yeah. 225 is the click EIP and that is core. 

**Tim Beiko** 
* We can discuss this offline if people feel very strongly about it, but it seems like intuitively the extension, the clique should also be core if the actual clique EIP is core. but I'm not willing to die on that hell. And if people are that we should just discuss this on the discord. 

**Pooja | ECH**
* I just to get some more context, it was discussed in the last EIP meeting. So maybe that recording of that might help. we were discussing about networking proposals with Felix, Micah, and then generally it was decided that it should not be a part of networking EIP and should be moved to core EIP. So this is a recent change and we can follow the discussion there. 

## EIP 2976 updates [29.08](https://youtu.be/-8TSQCwITA0?t=1738)

**Tim Beiko** 
* Okay. thank you, Daniel. We have another one. Micah is not on the call and I think this was his, but it was around the EIP 2976, the type transactions over gossip. I dunno if anyone else had context here, otherwise we can, we can talk about it another time. 

**Pooja | ECH**
* Yeah. that is another networking proposal because in the last meeting we were discussing about cleanup, so this was a moved to last call and the last point period is ending on October 6. So if people have any questions, common concern, this is the time before it gets moved to the final status. We just wanted to let everyone know about it. This is networking proposal is going to be final soon. 

**Tim Beiko** 
* Okay. so yes, please review that. yeah. so it's about sending type transactions over to gossip back to work. Okay, great. And then, oh Andrew, sorry. 
* You have your hand raised, 

**Andrew Ashikhim**
* Oh, I have a question about a EIP 2976 gives you just a clarification of the existing practice. So is it the change? 
* Does anyone on the call? 

**Martin Holst Swende**
* I'm wondering the same thing and basically, whenever we send anything over the network, we have an RFP packet.it's it's RFP. So if we send a transaction, it's going to be inside of them or the appeal list and yeah, I don't, I don't really, I think it's just a clarification. I don't think this changes something. 

**Tim Beiko** 
* Yeah. We, we just had Micah joined so Micah. We're talking about your EIP 2976, and people are wondering, does this actually change any behavior or does it clarify the existing behavior? And if you are speaking, oh, I believe it is already implemented. Just never merged. Okay. We can give you a couple of minutes, but it seems like, yeah, Martin and Thomas, you are right with this. 
 
**Martin Holst Swende**
* But, so most of the specifications do not live in the Eth, but live in the peer-to-peer or the specification. I might be wrong about this, but, 

**Micah Zoltu**
* Yes, so the, so I wrote in the EIP for it, back when 2718 was written and, it just never made it in and it wasn't clear at the time whether we wanted to actually use the EIPs for networking specs, because they seems like they generally aren't used, other than just kind of ad hoc at the end, after everything's already merged, someone goes and writes in the EIP that just for the sake of it, I recently talked to Felix and he would like to, continue to use the EIP process and probably try to be a little bit more diligent about it. So, when in the future, when networking specs go through, it would go through the standard EIP process and we'd have it done all core devs call and talk about it and all that. but that's going forward. the EIP was before we came to that agreement. And so, it kind of just sat there and it should mirror what everybody's implemented. If it doesn't, then that's a problem we should fix it. 

**Tim Beiko** 
* Andrew 

 **Andrew Ashikhmin**
* Yeah, just, one comment, on the slightly related to the scape because, in, for type transactions, actually how it currently works, even on the consensus level, the Eth sells itself says that, transaction, that transaction should be pre-painted with the transaction type bite, and then the payload follows and that pay payload for existing exempt transactions is our ROP. And that works for, calculating transaction road, but in the block, I think it's additionally, this, this, this thing is additional wrapped, as an app ROP array. So there was this kind of gray area, which was not exactly specified by EIP 2718, whether to wrap this additionally as an ROP into an ROP array or not. and I believe there were some issues on the networking level also related to this ambiguity, whether to rapid additionally or not. So to my mind, it's good that we clarify, but we should, we should, probably describe what most clients already do rather than introduce changes, 

**Micah Zoltu**
* How it goes into a block should be specified somewhere. I'm looking right now to see if I remember where it was either in the 2718 itself or in the Type the V like 2930 and 1559. But that should be specified somewhere. I know it, we wrote it down at some point. 

**Andrew Ashikhmin**
* Well, there was just, sorry, just a moment. I think it was not, but it doesn't okay. It doesn't matter too much. I think we followed Geth's implementation. but I'm sure there was a decision somewhere by the tour to wrap it in the battery or not. 

**Micah Zoltu**
* Yeah. So in 2718 and the specification section under the transaction subheading or the receipt subheading that first sentence, specifies how the Patricia Patricia tree should be calculated. 
 
**Andrew Ashikhmin**
* Yeah, that's right there. That is specified. But when you consider block body, the, the, the, ROP, the transaction ROP prefix to buy the transaction type is additional wrapped into RLP biter rate. And that, I don't think that was specified in the four, four blog bodies. 

**Micah Zoltu**
* Yeah. That that's in 2976. You're correct. That is not in 2718. 

**Andrew Ashikhmin**
* Okay. Okay. 

**Micah Zoltu**
* Yeah, I think  2976, like I said, if the clients can just review it, make sure it matches a, your implementation as they should. I have talked to Felix about, I believe Felix thinks that matches the FM limitation. so if it just matches everybody on limitation, we get to merge it as final and be done. 

**Tim Beiko** 
* Sorry, I couldn't find the unmute button, and declines feel like that's something they can do in the next week, just because, the last call period is supposed to end on October 6th. Is it fine if we, yeah, just, just because we we've, haven't discussed this the past two or three calls, I think when it's been with the agenda, other people want more time to just look at this or is it trivial to do, 

**Martin Holst Swende**
* I think it should be sufficient, given them, this, this already the fact that, 

**Tim Beiko** 
* Okay, cool. So, yeah, let's, let's, move it to final, on October 6th, assuming nobody in the meantime has comments about it. Great. And then the last thing we had on the agenda is EIP 3607. basically this was the one, rejecting transactions from senders, which already have deployed code associated with the address. it's already been merged in, in Geth. and Andrew was asking if we can move this the final so that, we can also add it to the yellow paper and make it part of the foremost specification. 
 
**Tomasz Stanczak**
* Yeah, I believe it's also implemented in other minds already. 

**Tim Beiko** 
* Great. how about Besu, Aragon? 

**Andrew Ashikhmin**
* In that Aragon, it's not yet implemented, but we can implement it. 

**Tim Beiko** 
* It's not a problem. And Besu you.

**Justin Florentine (Besu)**
* I'm unfamiliar with this one. I'd have to get back to you. 

**Tim Beiko** 
* Okay. so it, yeah, it should be a small change. and, I have Micah in the chat saying we should move it to review. So this is, this is kind of good timing. So I think we can definitely move it to review like now. So after the call today, if, Marius or yeah, Marius should the only one on the call. So I'm going to pick on you, if you want to move it to review, then, basically we can move it to last call, on, on the next call. once everybody's implemented it, they'll go to final. So I speak in like the next couple of weeks, we can, we can get it to final. and also for the yellow paper, I feel like once it's in last call, maybe you can just open a PR against the yellow paper and we can just merge it once it's in final. Does that make sense center? 

**Andrew Ashikhmin**
* There is, already a PR, so yeah, but yeah, I had it to match it when it is in, last call. 

 **Tim Beiko**
* So I'll, I'll, I'll just add that to the agenda also on the next call. So we, we remember to, to follow up on it and that's everything we have on today's agenda. was there anything else anyone wanted to bring up? 

 **Pooja | ECH**
* Yeah. I just wanted to mention about one of the, actually two of the proposals that we discussed in the previous call that I, I suppose, that was, that, networking proposals. the  is, 2364 and 2464. these were in draft now has been moved to a stagnant by the EIP partner. Now, actually we are working towards cleanup of the repositories and a lot of proposals, which were not active for over six months period of time. They have been moved to stab in status by the bot. So I just wanted to let, all the EIP authors know that if your proposal has been moved to stagnant and you still want to pursue that, you might have to create a poll request again, but for these two particular proposals, we need to get this to move, to review status so we can move it forward. And I know this is not active right now, but that is required for proposal 2481, which is like Eth 66 and we can not make it, final it unless we move the proposals, which needs to be final before that. 
* So, if I may ask the author, to create respective pull requests?

**Tim Beiko**
* Those are the two proposals that are like stagnant, basically it's Eth 64 and Eth 65. Yeah. So what needs to be done? 

**Pooja | ECH**
* So I, I made a pull request, but in my pull request, it was proposed to move from draft to review, but now that it has already been moved to stagnant. So I, that the author has to make a new request or I am happy to create one, but it might require approval of the author. 

**Tim Beiko**
* Right. And so Peter is the author on those two. so basically what we need is a pull request that's approved by Peter to move it from stagnant to review. Is that right?

**Pooja | ECH**
* Correct. 

**Tim Beiko**
* Okay. Oh, did you say something Peter? Sorry. 
* Sorry. I didn't get that. It's like, you're very far from the mic. Nevermind. 

**Peter**
* I was just trolling with people. Okay. 

**Tim Beiko**
* Yeah. So, okay. So yeah, if you could just, either open the pull requests or Pooja, if you wanna open them and Peter just approves them. so we can move those two to review and then we can actually move. yeah, we can move Eth 66 to final. Cool. 
* Anything else anyone wanted to bring up? Okay. While short call. Thanks everybody. yeah, I will see you all in two weeks and I'm looking forward to more progress on the merge in the coming weeks. 
* Cheers. Thanks. Bye. Bye 

-------------------------------------------

## Attendees

* Tim
* Lukusz Rozmej
* YDXTY TS
* Lightclient
* William morriss
* Mikhail Kalinin
* Dusan Stanivukovic
* Gary Schulte 
* Trenton Van Epps
* Pooja | ECH
* MariusVanDer
* Ansgar Dietrichs
* Baptiste Marchand
* Martin Holst
* Jingwei
* Tomasz Stancxak
* Tyevlag
* Alex Stokes
* Crypto_Eren77
* Andrei Maiboroda
* Micah ZOltu
* Alenque
* Selvis
* Yanxi
* Charlie
* Kay
* Stag
* Thea
* Rai
* Danny
* Encryption wizard
* Artem Vorotnikov
---------------------------------------
