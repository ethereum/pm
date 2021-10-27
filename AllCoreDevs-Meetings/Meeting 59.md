# Ethereum Core Devs Meeting 59 Notes
### Meeting Date/Time: Friday, April 12, 2019 14:00 UTC
### Meeting Duration: 1 hours 30 minutes
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/93)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=gfC92gQKKnI)
### Moderator: Tim Beiko

# Summary

### DECISIONS MADE

**DECISION 58.1**: Stop ProgPoW Carbon Vote.
Status: ProgPoW Carbon voting is closed.

**DECISION 58.2**: Clients status update will be provided as comments in the agenda.
**Status**: Done

**DECISION 58.3**: Reseach will be updated in the comments in the agenda.
**Status**: Done

### ACTIONS REQUIRED

**ACTION 58.1**: Cat Herders to look at updating EIP1.
Status: WIP

**ACTION 58.2** Smaller hardfork vs. larger hardforks
To be discussed in the Berlin next week in the Istanbul meetings.
Status: WIP

**ACTION 58.3**: Vitalik to format the currently proposed EIP-1559
Status: WIP

**ACTION 58.5**: Discuss if ProgPoW should continue to be implemented if the Technical Audit is not funded in Ethereum Magicians or here or here.
The action item was to continue discussions on ProgPOW and whether or not we want to go forward if the technical audit is not funded. ProgPOW will also be talked in the Berlin meeting.
Status: WIP

### Roadmap
For now we can keep this EIP list as a reference for Istanbul. We will discuss this after a month or so.

### EIPs

- Item 3a. Refer to Roadmap link for list
Alternatively, Istanbul EIPs at ECH GitHub

- Item 3b. Please add more EIPs to the agenda
EIP 1344 - call for feedback
Discussion hardfork meta EIP - WIP 
ISTANBUL EIP LAST CALL -  May 17th
Client implementation deadline right now is the 19th of July.

- Item 4. Working Group Updates

- Item 4a. State Fees
Updates

- Item 7b. Parity Ethereum
update Just wanted to add Parity Ethereum recently added quick consensus. SO full support for Gorli testnet is in. That is in 2.5 beta.

- Item 7h. Turbo Geth
No updates on Turbo-Geth.

# Notes

**Tim**: I welcome everyone on Core Dev Meeting # 59 I'm Tim not Hudson and I will be facilitating.
# 1. [Review previous decisions made and action items](https://github.com/ethereum/pm/issues/93)
**Tim**: Let's go through previous decisions and action items. Going through agenda.

**DECISION 58.1**: Stop [ProgPoW Carbon Vote](http://www.progpowcarbonvote.com).

**Tim** :  Last block number for that is 7504000. If people want to vote on the carbon votes, they needed to leave there Ether in whatever address to use to vote until that block. And then their will be a snapshot taken and then people can withdraw there Ether. Does anyone have anything to add there?
**Pooja**:  Yeah I think the last date was a 10th of April only and is closed now says the website.

**Status**: ProgPoW Carbon voting is closed. 

**DECISION 58.2**: Clients status update will be provided as comments in the agenda.

**Tim**: I'm going to go over every single client to research group and if people have questions, add them on the agenda and we'll make sure that it stays for people that asked question.

**Status**: Done

**DECISION 58.3**: Reseach will be updated in the comments in the agenda.

**Status**: Done

**ACTION 58.1** Cat Herders to look at updating EIP1.

**Tim**: I know there's been some stuff happening I've personally spent a lot of time there trying to describe the process and sort of gather all the various conversations that have happened around this. I don't know if anyone has anything to add. The associated GH issue is [ethereum-cat-herders/PM#19](https://github.com/ethereum-cat-herders/PM/issues/19)

**Status**: WIP

**ACTION 58.2**: [Smaller hardfork vs. larger hardforks](https://ethereum-magicians.org/t/more-frequent-smaller-hardforks-vs-less-frequent-larger-ones/2929)

**Tim**: Okay next one was just about reviewing the roadmaps and [Ethereum Magicians](https://ethereum-magicians.org/t/more-frequent-smaller-hardforks-vs-less-frequent-larger-ones/2929) forum to decide if going forward, the Core Devs will adopt smaller hardforks rather than larger hardforks. I know this is going to be discussed in the Berlin next week in the Istanbul meetings but if anyone wants to sort of comment on that you could just say that could be used as input for those discussions.

**Boris**: Quick question on that, basically I've heard Alexey in particular said like a 3-month hard fork. On this call, are people open to hardfork as short as 3 months? 

**Joseph**: I will object on that. I think it's too quick turnaround. Difficult to mantain two maintenance. Complexity comes in with frequent hardforks.

**Peter**: Essentially, if you're client developer and your only job is to do the hardfork 3 months, then its fine. But usually clients require a lot of maintenance. So if we move to 3 months hardfork then we essentially take away all the time from general maintenance and performance.

**Martin**: I would object. It would be a bad thing if we say we want to do hardfork every 3 months but if there are some simple things to roll out, is implemented quickly to which everyone thinks this is finished, we can roll this out, then doesn't have to be longer than 3 months in those particular cases.

**Peter**: Can't imagine. Currently, we are working on our major next release for next 4 months from now. If we want to do hardfork in between, then we maintain 2 versions - unreleased version and ready released version.

**Brooklyn**: Isin't the idea of frequent hardfok was about the less per version?

**Martin**: Yes

**Peter**: Oh yeah, but I am just saying complexities comes with client maintenance.

**Martin**: The idea is not to schedule hardfork every 3 months but to speed to finish. If there are access test cases in clients then we can't pretty soon. 

**Joseph**: Let me try to ask the question of who is having more information of Alexey's idea. Is it the possibility of windows open for hardfork every 3 months?

**Boris**: It was me who was putting words in Alexey's mouth. The context was he was having this multi hardfork plan and he is going to be anxious thinking about certain features are waiting for 6-9 months for implementation. I wanted to just jump in Joseph story for stepping  because there has been a suggestion to what you're saying "hardfork window". I think other people are saying including Martin is let's ship stuff when it's ready. So I'm not saying things need to be every 3 months but more frequent and it sounds like 3 months is like lower end of event that people say that's really tight and then 6 months. I have to look up but discussion around this where somewhere between 3-6 months shipping smaller features on a regular basis and coordinating among client. So that they shooting their process to support that is okay as long as it doesn't impact client maintenance.

**Martin**: Agreed.

**Fredrik** - Not sure. If there are only couple of things to improve then yes we can do 6 months but there's a couple of things that would probably be needed to automate that goes around the hardfork.

**Greg**:  I don't think we have the right person to handle a lot of this stuff. So developers wind-up setting up testnets, running test cases, doing testing, jobs that people are good at and enjoy doing it. What it takes to just get those people wanted rolling hard fork to so that development just not prevent hardfok from happening. 

**Fredrik**: We don't have money to hire them. 

**Greg**: I think there's a few rock and roll songs about that.

**Jacek**: Having schedule gives us the visibility. Just like Joseph said, we have the window to do the hardfork.

**Boris**: I think definitely something that we're going to discuss next week and to Fred's point. I think everybody is sort of agreed that we essentially aim for Istanbul as kind of a test case to go faster. What I would also say is that, in many ways we should start planning the next hard fork, sooner rather than later just to just train ourselves to take things more often. Ideally Istanbul as getting onto this will let us shake out any of the things that we need to scale, automate and collaborate on. And I would say maybe just a Greg's point and Fred's point to know which of those are big challenges specially when we add more clients what things can we do across client, this is just the obvious point to know how do we work together.

**Tim**: So maybe for your next steps here, is if we could just try and make sure that the output of those discussions get to put back into the Ethmagician thread that was linked in the agenda.

**Fredrik**: It would be interesting to see how we move about the hardfork.

**Tim**:  Anyone else have anything on the subject?

**Status**: WIP

**ACTION 58.3** Vitalik to format the currently proposed EIP-1559 

**Tim**:  Okay next action item was for Vitalik to format EIP 1559 because I don't think it has been properly formatted as per the template. He isn't here, so I guess we can just leave that one there. I'm not sure if anyone has comments on this . 

**Status**: WIP

**ACTION 58.4** Lane to provide a block number for when the ProgPoW Carbon Vote will be shutdown.

**Status**: Done

**ACTION 58.5** Discuss if ProgPoW should continue to be implemented if the Technical Audit is not funded in [Ethereum Magicians](https://ethereum-magicians.org/tags/progpow) or [here](https://ethereum-magicians.org/t/what-has-to-be-done-to-get-progpow-on-ethereum/1361) or [here](https://ethereum-magicians.org/t/motion-to-not-include-progpow-without-audit/3027).

**Tim**: The action item was to continue discussions on ProgPOW and whether or not we want to go forward if the technical audit is not funded. I think the goal was to find free discussions outside of CoreDevs call into the links that were put in the air in the notes. So unless anyone has anything for the new, noteworthy, or urgent; I think it probably makes sense to keep the discussion there.

**Danno**: Agree.

**Tim**: ProgPOW will also be talked in the Berlin meet.

**Status**: WIP

**ACTION 58.6** Clients should provide updates for future Core Dev Calls in the comments of the agenda and request an update to the agenda if they wish to discuss anything specific.

**Tim**: I'm okay.

**Status**: Done

**ACTION 58.7** Research should provide updates for future Core Dev Calls in the comments of the agenda and request an update to the agenda if they wish to discuss anything specific.

**Tim**: Next action items is similar. Basically just not providing updates during the call with providing them in the comments and letting people ask questions about them.

**Status**: Done

**ACTION 58.8** Alexey to create a Beacon Chain Finality Gadget initiative working group and find someone to lead it, for context please see discussion in [Ethereum Magicians](https://ethereum-magicians.org/t/eth2-in-eth1-light-clients/2880).

**Tim**: Alexey is not on the call, anyone has any comments? 

**Status**: WIP
 
# 2. [Roadmap](https://en.ethereum.wiki/roadmap/istanbul)
**Tim**: I kind of touch that already but anyone would want to add anything about roadmap in general or Istanbul specifically ?

**Pooja**: I just wanted to talk a little bit about it. Like about this roadmap for Istanbul do we agree to go by the time, October 16th, our target date or is it a possibility that we may not be going by that?

**Martin**: So yeah one thing that's has been discussed, if we do ProPOW, do it in separate fork, stand alone fork.
 
**Pooja**: Okay in that case like we have 8 EIPs proposed so far. If you want to  take ProgPOW EIP separately then still we do have 7 EIPs proposed. So if we considered these 7 together, are we hoping to be ready by October?

**Danno**: Can we step back? Why would we take ProgPOW separately? It has to be done earlier or later?

**Martin**: Initially, the proposal was to be done earlier and then it was considered a controversial EIP and then for some other reasons.

**Pooja**: Well I'm not saying that it is being pulled out of that. That's not my say, it depends on core devs. I just have shared the [list of the EIPs](https://github.com/ethereum-cat-herders/PM/blob/ca6a01c1d0a45419a55f7e79688e28ea6e0c8482/Hard%20Fork%20Planning%20and%20Coordination/IstanbulHFEIPs.md) that have been proposed so far. So if we can discuss that how many have been like considered to be moving ahead?

**Brooklyn**: Pooja, this is not the right time for this. So they're just proposed. The deadline is in roughly a month from now to see which of them are actually more than just proposed. But right now the schedule is as in previous core dev calls we've agreed upon. So, people have a month to propose more EIPs and for getting ready if they want to get them ready. And as far as I can tell from previous core dev calls - yes we are locked on the schedule as it had been previously agreed.

**Pooja**: Thank you so much.

**Martin**: About these proposals I assume that now is not the time to discuss them, is that correct?

**Tim**: This specific EIPs?

**Martin**: Yeah this specific EIPs?

**Tim**: That was our next agenda item actually, yeah.

**Danno**: Before, we go there just a plug, good test cases belong in EIPs so we can reduce the burden on the developing the test cases there.

**Pooja**: Okay for now we can keep this [EIP list](https://github.com/ethereum-cat-herders/PM/blob/ca6a01c1d0a45419a55f7e79688e28ea6e0c8482/Hard%20Fork%20Planning%20and%20Coordination/IstanbulHFEIPs.md) as a reference for Istanbul and we will keep on collecting EIPs and will share with you guys as we go. We will discuss this after a month or so. May be Berlin meeting will give us more insight and after that we can discuss.

# 3. EIPs

## 3a) Refer to Roadmap link for list

Alternatively, Istanbul EIPs at [ECH GitHub](https://github.com/ethereum-cat-herders/PM/blob/ca6a01c1d0a45419a55f7e79688e28ea6e0c8482/Hard%20Fork%20Planning%20and%20Coordination/IstanbulHFEIPs.md)

## 3b) Please add more EIPs to the agenda

**Tim**: Talking about EIPs there were two posted in the comments of this call. But I know there's also a whole lot that's just mentioned. So perhaps we have Bryant and Pooja who proposed the comments on the call. So maybe it makes sense for them to talk about it. Bryant that he actually was first in the comments so if you want to go ahead and talk about [EIP 1344](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1344.md).

**Bryant**: Sure thing. I am not the author of this one but about like a week and a half ago I was playing around with some 712 stuff and I was like why isn't there a chain ID opcode and so I went to go look and there was a proposal for one. So I've been helping kind of format in a nicer way and get it accepted and kind of gather feedback. Its pretty simple for the most. There have been a little bit of a discussion around like what kind of data types do we represent. I want to gather more feedback, that what else do we need to add this to Istanbul?

**Alex**: I have a question. For the last two weeks I haven't really kept a good eye on everything but we discuss the option that hardfork meta EIP should have a proposed list. And I think Bryant has proposed to EIP for the hardfork meta. Is there any consensus yet, at what point whether we go for draft to merge PR to include this as a proposed EIP? 

**Boris**: It was in the discussion around.  Bryant has some stuff around audience review but I think the one you mean is around 233.  That it's using the [hardfork meta EIP](https://github.com/poojaranjan/EIPs/blob/patch-1/EIPsForHardfork.md) where people do pull request as a way that we can actually keep track and move through proposed to approved and so on in one place. So you can very easily see which EIPs are in flight to potentially making it to hardfork. Nothing else changes in the sense that proposers will still need to come on core dev call. The outcome of it just would be actively tracked in that. So I think follow-up action item from this is just to look at the PR. I think that is what you meant Alex?

**Alex**: A quick comment on that. Last time when someone commented on your PR was the time line. I think if you remove the timeline, we can merge the PR. But we can discuss this offline.
What I actually meant with the question was the PR opened yesterday by Bryant to include 1344, this Chain Id EIP in the HardFork Meta and that has been closed. But I'm wondering if it should be merged or shouldn't, what is the process now?

**Bryant**: I was just trying to follow Pooja's process suggested in [#1929](https://github.com/poojaranjan/EIPs/blob/patch-1/EIPsForHardfork.md) which she also wants to talk about in this call. We talked about, may be this doesn't make sense, may be we should open an issue instead of PR.

**Boris**: This is exactly the same thing. The one you make a pull request in meta. As we change it will read through the meta process. 

**Bryant**: I think all of us trying to do the same thing at same time.

**Alex**: This is a change to Istanbul meta and not the 233.

**Boris**: I think it is just following the 233 meta. We just went into meta loop.

**Alex**: Sorry, I may have sidetrack the conversation, will discuss this offline.

**Martin**: I have a question about 1344 Chain ID OpCode. So essentially instead of storing the Chain ID as in smat contract its in the OpCode, is that the thing?

**Bryant**: It has a few benefits. So having it as an opcode means that if a hard Fork does occur then code on one chain won't get replayed on another chain.

**Martin**: No, I think its the same chain id, it never changes the chain id. in actual contentious hardfork, where there's two communities.

**Martin**: Right.

**Bryant**: They would change their chain id and then the opcode put a different number.

**Alex**: Do we really need an opcode or having take contract to take well known address  for each chain. Will that be sufficient alternative? 

Do we really need a knock code or having a contract with real address for each chain will be a sufficient alternative?

**Bryant**: I would think an opcode would be most optimal. Because, the way I came about thinking about this is for like 712 procedure which is  like very, very context-specific operation you are doing offline signing for. So this would help in that like you would be able to do it on a chain and if the split happens then you would make sure that there is no replay attacks against the offline sign messages that use 712.

**Danno**: That was a question also on the EthMagician thread. One of the concerns was that the contract would be more expensive than an opcode by necessity of the call and query the chain ideas incredibly cheap operation.

**Bryant**: Yeah we actually specified it as the base price 02 gas. I did a small implementation in Trinity. It's about 11 lines of code and one way that we could go about doing it by taking the chain ID from the transaction context and leveraging that. I wasn't sure if there's another way of doing it, not much familiar with how clients have been dealt but it was an obvious way of doing that. Currently, it is manually managed when you deploy your contract and assure deploying. Let's say you're doing stuff on Ropsten, in  order to test it or Gorli or whatever and then if you forget to update the parameter on the mainnet contract now will have to replay that could be a mess here. Kind of human error there too.

**Peter**: I agree that any functionality that lacks the contract introspects in chain is beneficial.

**Martin**: I have another question on one of these, if it is okay to move on. That is **EIP 615**. My main concern about that it is humongous. We need to make a lot of changes in the consensus engine. I am not sure about the benefit. I don't think they'd do  much better EVM.  It will probably help you see any immediate performance improvement that exists. If there is a champion there, I would really like to hear it.

**Brooklyn**: I am sure Greg would love to jump on this too. Speed is actually that we can do. This is our first staging for improving jets for ahead of time completion. Its the first step to pull bunch of things. Its number of opcode currently that  we could potentially break it up. This has been discussed on EthMagician and GitHub thread. Not sure if much is needed in this call or just hash it out in those places. 

**Martin**: I did took part in those discussion. For the first hardfork there will not be speed effect need the validation in wrong time. And it will be much more expensive validation based on the analysis done today. Not done after until we have a second hardfork and it could do deployment check then we can skip the validation check in runtime. At that point I still think nothing proving the actual how it manage  junks with only effect the EVM speed because this will be on the disk io. That's my main concern. It needs a lot of work but may not lead to better EVM. Might be helpful to external tools for security analysis or security purposes of the contract.

**Greg**: I don't see any immediate performance improvement out of this one. The validation is very fast. In the C++ client it happens at the deploy time. so it's really not an issue. it is a better EVM from the point of view of external tools. that's where we see people saying yes please the k analysis was very much harder because it had to deal with the pattern matching looking for what its subroutine looks alike rather than just an ordinary sub instruction.

**Boris**: I think the point is that this whole thing is in part to foreward compatibility to get us tools for a variety of people building on top of the EVM, in building more features that link us up more directly to what our future execution engine is in WASM. So in some ways part of this has to be how much of this do we do in the evm sooner rather than later especially if we do hard Forks more often. versus just waiting until some future time and then they shift for anyone writing smart contracts today will be much larger because of a deficit in  features of compatibility.

**Greg**: WASM compatibility was another constrain. How hard is it to implement with several 100 lines in C++ and it took me about 2 months to implement. We haven't been through Last Call on it, that is smart to know they're still another EIP for Version Control needs to go in, so that it's possible for VMs to know which code of my running old style code, Wasm code,  new style EVM code. We need to get that in place anyway.

**Martin**: With that in mind is this EIP is actually still a proposal for Istanbul.

**Greg**: Yeah it's been sitting here for two years now. 

**Martin**: It requires a version EIP. 

**Greg**: Yes,So we've been working on that in parallel so they're both ready.

**Martin**: Yeah I guess today isn't the time to make any kind of decision on, just discuss it.

**Greg**: Yeah I guess May 17th the hard deadline but we've been working together. So if I think we have a straightforward notion of what that needs to look like.

**Martin**: I have nothing further on this on for today.

**Greg**: Yeah I'm looking that has been making changes in parallel to the discussion, and his PR is ready to go.

**Fredrik**: Something that I just wanted to bring up in here. When it comes to this stuff is, at this time Alexey making pretty long speech about not making changes that are in for the survival of the chain. Not making improvements or fixes  or whatever you want to call. Vitalik said the same thing - we shouldn't br chainging things any more we should just keep the chain alive while we work on ETH 2.0 and the new stuff goes in there.  How much do we sway outside of this, because this EIP leads into a long chain of improvement going into several years before we're seeing massive benefits from it. 

**Greg**: 2021 is two tears from now. startups like die if they don't get new technology out every year.

**Brooklyn**: yeah I have the echo that this EIP too has undetermined release dates. it's making changes like this but we have today to make it forward compatible so that it works with stuff later. SOo that smart contract developers have smooth experience. keeping things in essentially maintenance, there are other options for smart contract are out there.  We need to keep Ethereum 1.x alive and that means continuing to move.

**Greg**: Remember that these two teams know it that the main chain is going to keep on operating indefinitly. There is no value on the main chain, if there is nothing to stake.

**Fredrik**: That is not entirely true. The intention is to move thevalue from main chain to the Beacon chain. You guys are proposing EIPs pretty frequently.

**Greg**: We don't know when Eth2 is coming, firm date.

**Peter**: With regards to Eth1 vs Eth2, I think Eth 2 is suppose to solve everything whenever it arrives. I think as maintainers of Eth 1, its really important to keep it alive until Eth 2 actually arrives. whether Eth1 will die horrible death or something is up for the future. I don't think its smart to start burning Eth1 when we have no idea about what the future contains. We push Eth 1 forward as much as we can. If something better comes along then its fine but lets not kill it before that happens.

**Martin**: That wasn't the intention. May be the Eth 2.0 has also Wasm somewhere. I am skeptical about it.

**Peter**: Don't read me wrong. I wasn't actually referring that Ethereum upgrade to Ethereum 3.0 all of a sudden. I am fine with discussing all the changes. I was aiming that we shouldn't hold back from upgrade. 


**Fredrik**: We shouldn't be adjusting our roadmap based on what Eth2 may or may not be. 

**Boris**: I think a lot of this is exactly the purpose of why trying to have an in-person meeting that talks about some of these things. I'm glad that this is coming up today already. 615 aside, specially from what I heard at EthCC, there seems to be pent-up demand for all sorts of things. Again slow and considered in the sense of making sure that there's a stable healthy network. But part of that is having features that the people building on top of it and take advantage of. I would point to so it looks like there's going to be four new precompiles the people want to propose for Istanbul. And each new precompile unlocks more cryptographic produce that gives our application layer people, a ton of stuff to build on or improve or reduce the gas cost of various existing ones. That seems to be what people are still excited about seeing because we have a system that is live and people can ship on today.

**Tim**: Unless anyone has anything to add on, Danno has a question on Istanbul, when do we want EIP to go on last call? They have to have gone through the last call by May 17th or they need to move to the last call by May 17th.

**Greg**: I intend to be through with the last call by May 17th. I don't know what the requirement is?

**Tim**: In the chat is the requirement is unclear. If any one has any opinion on what should the last call point be ?

**Danno**: If you definetly want to be in the hardfork, I would think you wouldn't need be in the last call. Its like two week  window, all other people are invited to, its like an RSS feed, people listen to.  That's my thinking on it. 

**Boris**: For reference the last hardfork everything was still a draft and hadn't been moved through anything. So there was a tweak to the EIP process that directly means sticking to these dates and so on. So that's why so many uncertainties exist because we're trying to improve the process for the first time. I think people need to propose ideally between in the next five weeks. We have people actively doing PR's against the hard work meta saying that they intend to pursue getting this in the Istanbul. And then they have to pass the other checkpoint like major client implementation security and so on to actually get it in. Joesph, EIP 1 got updated recently. This is literally the new process and exactly how something should be proposed is not described in there. But I think that's part of saying that proposed means you've done a PR against the hardfork Meta for the upcoming fork.

**Bryant**: Do you think a security review should be required before that point? I thought that was may be leading into the actual. There's a lot of time between now and then. 


**Danno**: So security view is parallel to client implementation, is that I am hearing?

**Martin**: Yeah.

**Bryant**: Yeah maybe I misheard, what Borris is talking about? I heard that all this had to be done before the proposal day.

**Martin**: No, But there is a thing, that  each EIP should have section for something like security consideration. It is separate from someone actually doing it separate audit to it.

**Tim**: In that case, does it  make sense to say that **on May 17th what we expect is in merged PR that is compliant to 233**. So basically specific EIP into the hardfork meta EIP and that include some security considerations in the EIP but not a proper security audit nor a does it imply that EIP is accepted. But just merged into the meta hardfork EIP. Does that make sense?

**Bryant**: I think the security review as this thing separately, as a modification EIP. I think the real question is the last call is accepted before May 17th.

**Boris**: No, it has to be in draft PR, draft EIP and in the Hardfork Mata is I believe the line in the sand. Because all you are in, is proposed. About stage there's no guarantees that you're making it in. 

**Bryant**: You're going to work to get it in draft by May 17th 

**Boris**: and propose. 

**Tim**: By proposed, you mean merged PR in the meta EIP?

**Boris**: Yes.

**Tim**: If anyone disagree with this?

**Martin**: This is supposed to stop somewhere. I'm not sure that is included in the meta EIP.

**Tim**: From what I understand is a draft EIP, that is included in the Istanbul meta EIP hardfork. Boris PR describes the process.

**Martin**: A question regarding elliptical curve. May be I should just bring it up on the forum.

**Tim**: I don't think Ramco is on.

**Tim**: Other question in the chat from Joseph when will the three client implementations be due. for Istanbul? So I assume that the client implementation deadline right now is the 19th of July but I'm not sure it is that's what we want to use. 

**Boris**: Unless somebody wants to fights against the schedule as it is I want to go to the schedule as it is. The Istanbul hardfork planning dates are set. Unless core devs unaccept it. 

**Tim**: so let's keep the 19th.
And then Pooja you wanted to talk about #1929.

**Pooja**: Yeah, we had been discussing this in ECH about how to streamline the process of EIP submission. This [#1929](https://github.com/poojaranjan/EIPs/blob/patch-1/EIPsForHardfork.md) requested is the proposes a process that we may follow for EIP collection of any upgrade. One thing that I've received in comment from Nick Johnson at [EthMagician](https://ethereum-magicians.org/t/proposal-of-a-formal-process-of-selection-of-eips-for-hardforks-meta-eip/3115/4) is the usage of EIP GitHub. He suggests that it may create some kind of confusion that EIP editors are the one who are taking decisions on which EIP should go or not go. It may be better to take it somewhere other than EIP GitHub. If that is a problem then we may take it to [ECH GitHub](https://github.com/ethereum-cat-herders/PM/issues) and collect EIP over there, that's my suggestion. If anyone would want to comment.

**Greg**: Merging EIPs doesnot indicate that the editors approve of it. It only indicates that it meets minimum standards for form. So it's perfectly fine to merge them there and point the discussion over The Magicians or anywhere else you want to discuss it. 

**Pooja** : That is fine, we are referring magician thread where the discussion about that particular EIP is going on. But what we need to say, here is when we want to indicate that this is our EIP and I would want it to be included in next hardfork where they should submit it? My suggestion would be an issue section so that when picked up from there, issue can be closed but when it is in PR,  that needs merging and when it refers to any meta EIP, this automatically goes to the author of meta EIP. It would be going there and looking for approval.

**Greg**: Sounds like something to discuss on the EIP Channel. I don't know.

**Pooja**: I just have proposed the [EIP](https://github.com/poojaranjan/EIPs/blob/patch-1/EIPsForHardfork.md) in a PR if you guys would want to take a look at it.

**Boris**: The very specific thing here is, I think Nick's concern was that EIP are meant to  meet the  standards. And if hardfork meta, it mixes standard with Ethereum main net change. But, I think that's fuzzy anyway so #1852 that I'm about to submit by what Alex said should satisfy. And I use that one to further this discussion. 

**Greg**: Okay this is an old discussion I'm glad if we ever see it resolved.

**Bryant**: I had another point in her proposal. I think right now it does that you have to do it through EthMagician or is it like this is a choice you can make?

**Pooja**: No, I have changed it as a suggestion not as compulsion.

**Bryant**: all right. And then the second part that I brought up was, socializing the  the EIP. it was suggested to bring it up through all the other places people gather. and I made the suggestion to change it to these are places people gather, you  can socialize it through those means or whatever means you seem necessary but the official discussions to Forum is where discussion has to happen in order for it to be considered. 

**Pooja**: Has been updated accordingly. Yes your suggestion was like really relevant. If you would want to discuss it in some other forum for them to make more people aware of it, it's fine but  Ethmagician is a suggested forum where every discussion are listed at one forum, that is definetly a good start for an EIP.

**Bryant**: I more meant whatever is listed in discussions to that's where conversation has to be captured, to be considered.

**Pooja**: yes. 

**Bryant**: Like somebody might propose economics EIP, were magicians forum doesn't make sense as a place to discuss it. That's up to the author to propose an alternative forum but there has to be exactly one listed and that forum is the only place where discussion can be considered official.

**Pooja**: Yeah, I mean we can write it up. But I'm open for suggestions over here. Like if everyone agrees that Ethmagician is the only forum where it should be discussed, it can be changed accordingly.

**Bryant**:  I think it makes sense that people have said that EthMagician is going to catch all environment for discussion. Some people may view it too technical. So..

**Boris**: Hang on Bryant, let's just figure out who cares about this discussion, have the discussion and come back with a proposal in the form of an EIP. 

**Bryant**: Sure, But I guess the last thing I wanted to say is does it make sense to say the 'discussions to' is the only place for EIP conversation be captured?

**Boris**: NO

**Tim**: Okay, does anyone have anything about any of the other EIPs? If there's other questions or comments about the other proposed ones? Okay. 



# 4. Working Group Updates
## 4a) State Fees
**AlexeyAkhunov**: [Updates](https://github.com/ethereum/pm/issues/93#issuecomment-482528206)

## 4b) EWasm
No update.

## 4c) Pruning/Sync (ETH V64 Call for Proposals & Stopgaps for cleaning up discovery peers pre-Discovery v5)

**Matthew**: Just quick update. Moving discussion from EthMagician to minimal viable lightweight EIPs so that will be discussed in Berlin. then from there we'll just see what we have to want to adopt and again these are mostly going to be pretty lightweight changes and would probably land at the same time syncing proposal is made.

**Tim**: Cool.

## 4d) Simulation
No Update.

## 4e) Istanbul & ETH1x Roadmap Planning Meeting - April 17th & 18th in Berlin
**Tim**: We've already touched on it a couple times but is there,  anything else?


# 5. ProgPoW Audit Update
**Tim**: ProgPOW audit update usually done by Hudson. Does anyone else have anything?


# 6. Testing Updates

Already covered.

# 7. Client Updates (only if they are posted in the comments below)

## 7a) Geth
No update.

## 7b) Parity Ethereum
**phillux**: [update](https://github.com/ethereum/pm/issues/93)
Just wanted to add Parity Ethereum recently added Clique consensus. SO full support for Gorli testnet is in. That is in 2.5 beta.

## 7c) Aleth/eth
**chfast**: [update](https://github.com/ethereum/pm/issues/93#issuecomment-482564541)

## 7d) Trinity/PyEVM
No update.

## 7e) EthereumJS
No update.

## 7f) EthereumJ/Harmony
No update.

## 7g) Pantheon
No update.

## 7h) Turbo Geth
[No updates on Turbo-Geth](https://github.com/ethereum/pm/issues/93#issuecomment-482528206).

## 7i) Nimbus
No update.

## 7j) web3j
No update.

## 7k) Mana/Exthereum
No update.

## 7l) Mantis
No update.

## 7m) Nethereum
No update.

# 8. EWASM & Research Updates (only if they are posted in the comments below)

**Tim**: Research update - so like we said there's some of those posted on GitHub agenda. So if anyone has either a question or something that they didn't manage, feel free to share it.

Okay is there anything else in general ? Okay, then I guess that's it. Thanks everybody for your time and we'll see you in the next one of these. 
 
**Boris**: Hey Tim, Thanks for rescuing us today.

# Date for next meeting

April 26, 2019 at 14:00 UTC

# Attendees

* Alex Beregszaszi
* Borris Mann (Fellowship of Ethereum Magicians)
* Brooklyn Zelenka (SPADE)
* Danno Ferrin (PegaSys)
* Fredrik Harrysson (Parity)
* Greg Colvin (Fellowship of Ethereum Magicians)
* Jacek Sieka (Nimbus)
* Jason Carver (Trinity/PyEVM)
* Joesph Delong (Pegasys)
* John Adler
* Martin Holst (Ethereum)
* Matthew Halpern
* Mikhail Kalinin (EthereumJ/Harmony)
* Pawel Bylica
* Peter Szilagyi (Geth)
* Phil
* Pooja Ranjan (Ethereum Cat Herders)
* Tim Beiko (PegaSys)

