# Ethereum Core Devs Meeting 57 Notes
### Meeting Date/Time: Friday, March 15, 2019 14:00 UTC
### Meeting Duration:  1 hours 45 minutes
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/83)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=GQ0kbH0iSfI)

# 1. Roadmap

## 1.1 Istanbul Hardfork Roadmap

**Hudson**: Welcome everyone! Let's start with Istanbul Hardfork Roadmap. When Afri was release manager, he came up with a roadmap that had a cut off date in May and sometime around October is the actual HF date. People are liking that model so far. I don't know if it meant completely agreed upon but it sounded more like it has consensus around it. I don't see why we we shouldn't go with that.

## 1.2 Release manager

**Hudson**: What we are doing is getting a group of release managers. Boris, you have been taking some steps to put release manager organizational stuff together.

**Boris**: Yeah, I considered that Afri's plans are good one, starting to communicate that and to ask questions about what need to be done for that.

Joseph Delong working with Cat Herders has stuck up his hand and offered to help from ECH perspective. He can be the POC for whatever need to be doing. We are using [Ethereum Wiki](https://en.ethereum.wiki/) to flush things out and have a spot for things to work on.

I also volunteer here to work with Alex on updating [EIP 233](https://eips.ethereum.org/EIPS/eip-233) so that we can keep the EIPs proposed in the EIP repo up to date.

**Hudson**: Great, which Alex?

**Boris**:  Axic (Alex Beregszaszi)

**Hudson**: Okay, sounds good. What I will do, I will get chat room get ready for release manager stuff for Joseph and others.

**Boris**: Cat Herders have the chat room set up already. It's private for now. I will check for your access.

**Hudson**: Cool, are you in it?

**Boris**: I am.

**Hudson**: Perfect, I will look at that.

**Hudson**: That's the latest on the roadmap. All that being said, lets start getting some EIPs together to propose through May. We only have about a month and a half to get down on the proposal period. Lets start making decisions on which EIPs are going in. So, anyone who has EIP that really wanted to go in the last fork, this is the good opportunity to get them into the next fork.

The way to start discussing those is to put them in core dev meeting agendas and then I will add them in the agenda and bring them up during the meetings.  

**Martin**: Will someone keep track of EIPs that are suggested for the HF where we can pull up and know the status?

**Hudson**: Yes, I am going to put them together. 

**Martin**: These are to discuss, these are decided and that kind of. 

**Boris**: This is already on [Ethereum Wiki](https://en.ethereum.wiki/roadmap/istanbul/tracker) and the change that Alex and I have suggested is that we actually make them as pull requests into the Hardfork meta [EIP 1679](https://eips.ethereum.org/EIPS/eip-1679). This is just following the suggestion in process that Afri has started with a tweak that let's use PR so that we can actively track things. And Hudson and others don't have to manually maintain things in a doc. 

**Martin**: Okay, so you will create a new meta EIP and the process to get something discussed, you just make a PR to that meta EIP.

**Boris**: Exactly, just in a proposed section and then it can move through, still suggested for core dev calls for discussions. In terms of tracking [EIP 1679](https://eips.ethereum.org/EIPS/eip-1679) is the existing Istanbul HF meta.

**Fredrik**: The EIPs people propose should be HF related EIPs because the majority of them are not. As far as I know, they are not for the HF, then they really don't need to be in the roadmap.

**Boris**: That is it the exact thing that we need to do with the formailty of the actually adding it to 1679. Obviously the Wiki is editable right now. 1679 I am proposing should be canonical. If it's not on there its not going to be considered and I will track down. I think, the author of 778 might be on the call today.

**Hudson**: Yeah, is that Felix? He is here. Cool,  will talk about that more then. Good point Fred, we will watch on for only those are required for the HF. 

**Fredrik**: It would be educational and getting the word out for people should propose EIPs that they want to be included in the HF.

**Hudson**: Yup, sounds good.

## 1.3 ProgPoW Update

**Hudson**:  Next is ProgPOW update. As I discussed last time there are 2 components of the progpog audit - Benchmarking, How efficient the ProgPOW would be compared to a graphics card wrt the efficiency gains would be. 
There is a proposal that have been submitted and another one submitted hopefully today from another group. Cat Herders are looking at both proposals and evaluate and make a decision next week on which one we want to try to get funding for.

**Martin**: If I understand correctly, there is no work done on this yet?

**Hudson**: Yes, there has no work done on this. I should say there has been no work done on the audit itself. 
Something you asked Martin in the comments. Here is the questions that 2nd audit will answer, then I will approach the first Benchmarking audits because I have new developments on that too. 

Deliverables are 
* **constraint analysis on ProgPOW** to look over the overview on constraints on how efficient the progPOW Asic would be in compared to graphics card because there are claims that you wouldn't get that much of increase so that would detour people from building the ProgPOW Asic in first place.
So, a HW constraint analysis.
* then there would be an analysis on the **proposed ASIC architecture**
* **manufacturing assessment** that includes expert interviews. That something else in the deliverables for 1st proposal we received
* potentially an **Economic analysis** on the impact that ProgPOW would have on the economics of the Ethereum protocol.

That is kind of what we are looking for. Because of budget constraint, we might not be able to do all of that but we will try to do as much as we can.

Some people have been asking about :

**How is Benchmarking going?**
I have talked to WhiteBlock. They are  on the fence about what the next steps are because they haven't secured funding for the audit. There also been a lot of community participants who have done their benchmarking which although is not as scientific as WB would do and their analysis. It's still something that we can look at and evaluate. Since variety of people have been doing and in particular one person actually live streamed the audits over the series of graphics cards and proof that they are actually used in the graphic cards and then ran the numbers, which I thought was pretty impressive.
What might happen is that we may not be doing the benchmarking part at all because that is less important of the two pieces of the audits. We may only try to pursue funding only for the second piece.

Big question is even if audit doesn't get funded, are we still going forward with the ProgPOW and I think the answer to that is I am not positive but it looks like more and more consensus is going towards putting ProgPOW into the next HF. In my opinion, that is something that we need to discuss on here between now and May. Because the audit might not be done by then. I think the path that we could go down is that if we decide to go with ProgPOw as one of the EIPs going to Istanbul. We can set it by May - Yeah it is going in and when the audit is done, we can choose to throw it out if anything major is found in the audit like any problem or something would eliminate the reasons why we initially considered to put the ProgPOW in the first place. I think that is a good path to go down but I want to hear peoples opinion  on the path forward. Since this is still a political topic, I want some insight from anybody here about what they feel like on the consensus going towards and what we should do. 

**Danno**: I was surprise how uniform the  coinvote and extra data vote wasn't in favor of it. That was a bit of the surprise, so I think that does change some of the calculus as far as what the audits have to deliver. What I heard some community contribution would be in it for an analysis on security; because there are some changes to hash. Some of the real cryptography experience might be useful to go over them to make sure that it is done right. To my look, it is but I am not a trained cryptographer.

**Hudson**:  Okay, that is something that we can consider. Any other comments?

**Tim**: I spent some time with ECH over the past couple of weeks trying to understand the ProgPOW community, where they are at? One thing that they seem frustrated about the lack of clarity about next step. This came up in a couple of forums. I think this idea of conditional acceptance is something that would at least help people interested in ProgPOW gain clarity about - okay, this is the only missing piece. If the audit is the only green flag then its going in because I think there is a fear that the work on the audit has not started, and if would be too late by the time it get ready for Istanbul then it will take another 6-9 months for next HF. 

**Martin**: My thoughts on that matter - if there is an EIP that we accept for HF and if later that comes up as could be horribly wrong and its better to pull it. So, it's going to be conditional acceptance. In my understanding at one point we may have to make it conditional acceptance of this EIP. Now we see signals from miners accepting ProgPOW so I think we consider it to be accepted. Obviously, if audits turns out to be something wrong, we can remove it.

I think ProgPOW is going to be historically simplest things to be pulled out of a HF because we don't have to re-write test cases.

**Hudson**:  Okay, the one question that I have related to that is when something goes horribly wrong, are we talking about like figuring out that it is that something like hash function is broken? Or would it be something like it turns out that ASIC manufacturer can make something in a month that would have 20x increase in efficiency, so really would not make a difference in the first place.

**Martin**: Either of those. We may discuss this when audit results may come out. But if it turns out that something could go wrong then why would we switch?

**Hudson**: Yes, that is kind of feeling I am getting from others too.

**Alexey**: Can I comment as well? I just wanted to remind people who didn't remember what we did actually in it when there was tentative agreement about ProgPOW. I don't know if we agreed on this specific thing, but I suggested that ProgPOW should be activated in a separate HF. But now we seem to come like the old back ways, to bundle things out. I suggested in the last call that we should consider restructuring the delivery so that we at least make to possibilities of exploring not making huge changes at once but it seems that in the first part of the call we again went back in the old ways of doing things. 

**Martin**: I agree with Alexey. I am also in favor of rolling out ProgPOW and more of other things separately.

**Hudson**: Okay, what do other people think? 

**VB**: It does sound like a lot of advantages because there are other things to worry about. But also there will be two different strands of work happening in parallel basically finalizing and rolling out ProgPOW at the same time as implementing the other HF. Step might require to write the test cases and so forth. 

**Greg**: How long will it take for ASIC manufacturer to actually roll out the chip? If we got the evidence that an ASIC manufacturer could actually be pogW, how long will it actually take to a ASIC manufacturer to deliver; does anyone know?

**Danno**: They can do it between 6-9 months. That takes up to another question - is it economically viable? They need to use really expensive memory and they can really do it in six months and it costs say ten times as much it makes for the miner as it with ETH hash miner even though they get same improvement, that would just be the economic impact on it.

**Greg**: ok, it seems to be irrelevant to the consensus we already made.

**Hudson**:  What would be irrelevant to the consensus, you are saying?

**Greg**: we already decided, we're moving unless there is technical issues with implementing. SO, being told by someone - oh we can do an ASIC after all, it will take months and months, kind of shrug and go, well put your money where your mouth is.

**Hudson**: That is what is audit for. It is for basically go through the explanation of expenses of creating that ASICs without making the ASICs. SO that we get to now what the efficiency gain would be without actually building it. 

**Greg**: This is a separate audit from the security audit?

**Hudson**: Define the security audit.

**Greg**: We made consensus to move forward unless technical issues arose, so I am rolling all of that into a security audit. For us, if there is something wrong technically, it's going to affect the security of our system. If an ASIC manufacturer claims that they can beat it, its not a security issue.

**Martin**: For what it's worth, I would argue that it is.

**FJL**: There are two different issues:

1. Is ProgPOW a good POW algorithm in general? This would be the security audit that you are referring to determine whether if it is a suitable POW algorithm at all? I think we are reasonably sure about that.
2. Other thing that has to be determined is it economically sensible

**Greg**: No, we are going back to stuff that we were tired of talking about months ago. We decided that the only issue is whether there are errors in the algorithm, backdoors in the algorithm or anything like that. Not our arguments between the GPU people and ASIC people.

**Hudson**: That's not the argument about the GPU and ASIC people it's about the reason we will put this in is to prevent or highly discourage ASICs from entering the ecosystem. Additionally to make sure that the ASICs that would enter the ecosystem would not have more than x improvements on previous ASICs or compared to GPUs, was my understanding.

**Greg**: We already have this discussion. I will not believe any such numbers till the ASIC chips actually hit the market.

**Hudson**: Even if there is an audit that would determine that?

**Greg**: Yes.

**Boris**: Hudson, I think, what I have seen it from what Tim said, this is all of the pain and suffering from the mining side. There has been three audits. Whats the point of them? Why do we need to get it done? I don't think that we are testing whether or not an ASIC might be created. Thats up to the market and we can't know that ahead of time. Can we meet reasonable security guarantees ahead of time, is I believe the point of it. And if this isn't written down, lets just table this and say where is the single written down things and what are the purpose of the audit is?

**Hudson**: Okay, I think its fair and we should get that organized.

**Boris**: Are you the point person on this, Hudson?

**Hudson**: I think the ECH are, and within the group of five persons are in the chat room who are organizing this.

**Boris**: Let me be very direct and I've said this before to the ECH already, regardless of decentralized, from a responsibility and planning perspective, there needs to be at least one human whose responsibility it is. That is the other action as well to figure out who that is?

**Hudson**: I agree, I think that is a good step forward and I will see who can take that up and announce it. I think the magician forum would be the best to clear out both issues that you brought up - Point person who can make the announcement and what the audit is actually covering?

**Alexey**: Another comment I want to make following to what Greg has said. I don't think we can do things just because we decided to do things knowingly that we don't think we should do it. If we discover the change is useless, we should totally go back and cancel it. 

**Hudson**: I agree with that personally. To discover the changes are going to be useless is under what conditions, because it will help write down the deliverables for the audit.

**Alexey**: This is what I complaint about the last time as we were discussing it again is that it was very difficult for me to pin down and I was trying to actually figure it out - What is the goal? What is the criteria for success? So far I have not been able to track this from people who are suggesting ProgPOW. It's vague. If it's vague on one side, it's vague on the other side.

**Hudson**: My understanding of the goal was to discover that to discourage or entirely prevent ASICs from entering the network and kick off the current ASICS on the network, in order to prevent network centralization risk. This is something like super official but in my mind it was to appease the miners who said that they want it. 

**Alexey**: Well, this is very loose description of it, if you start working from this then I wouldn't be surprised what you expect from audit will also be vague and loose. Basically reminding that the audit should deliver very factual results. It is unfair because before you can do that you also have to define the goal of the actual changes. If you want to have the numbers on one side you have to put numbers on the other. That is what Boris and Tim said. 

**Martin**: I would say, people are currently against ProgPOW are the ones that should define what questions do we want to answer.

**Boris**: I think what you are trying to say is basically this is going in unless there is security issue, or number x or number y and frame it in such a way that the audit must prove those things. Is that the direct way of saying it?

**Danno**: Maybe those don't want it, the burden of proof is on them.

**Alexey**: Why is that? Because basically two people in January said in the call and I was one of this people. I remember how the consensus has been made. I said we should make some decision and Hudson said lets make decision and that's it. I also said that the change has to be in different HF. If you call this as the consensus made by me and Hudson and that is going to shift the burden of proof on the other side then I don't know what to say.

**Danno**: We also have coin vote and also have support from the ProgPOW community and lot other forums. I think that consensus is not whats pushing the burden of proof on the other. The miners have large stake and they have spoken it fairly uniformly.

**Greg**: The consensus was not just two people it was every body on the call and was months of discussion leading into it. So that anyone that who cared should have been on the call. If you don't object on the consensus that is part of the consensus. Nobody objected, many agreed, nobody blocked it had a consensus that we are moving forward unless there is a technical issue. Not whether GPU miners liked it or whether some ASIC people came up and say - well we can beat it, none of that. I am fine with saying that it doesn't have to go into a particular HF and I remember Martin in a previous round saying we really should have a separate HF just for it is not a good idea, I think. It takes the pressure of finding the technical issue but I just object a lot bringing back up any of these non technical issues. I don't particularly believe anything miners have to say about it until they actually deliver specially because if they really can, they would keep their mouth shut and just make some money. Otherwise, its just doesn't mean a damn thing.

**Alexey**: I want to comment on the very first thing you said which is not a common understanding. You said that, if somebody is on the call and do not say anything it means they agree to the decision.

**VB**: Guys, just to interrupt, in the interest of keep everything moving, can we take a five minute time out on the ProgPOW discussion?

**Alexey**: Okay I understand. I just wanted to say that its against my understanding that everybody who joins the call and does not say a thing agrees with the decision. In this case a lot of people will refuse to join the call.

**Greg**: Consensus is not about every agrees its about nobody is blocking the consensus.

**Hudson**: Okay, so lets move on to the next thing. Good idea Vitalik we put a pause on the ProgPOW discussion and will come back on it at the end of the call.


# 2. EIPs

**Hudson**: Next thing is Felix's EIP 778.
## 2.1 [EIP 778: Ethereum Node Records (ENR)](https://eips.ethereum.org/EIPS/eip-778) [Felix's Comment](https://github.com/ethereum/pm/issues/83#issuecomment-469677340)

**Hudson**: Felix would you fill us in what that is and your proposal is? And it doesn't involve a HF.

**FJL**: I think I submitted the EIP in late 2017. 
**What is it?**
It is a definition of a data structure that can be put in any network protocol but the specific enhancement is to put in current node discovery protocol and in the next version of that. Intention behind making it a separate EIP is because its data structure is kind of universal and is very useful to agree on a common format for the node agreement regardless of the system it is relayed in. I hope that some people have read the EIP because it tries to be in details and give more examples. That's what it is.
To **answer second question** - no, it doesn't require a HF. Because it is basically a data structure that isn't involved with Ethereum consensus in any way.

The other EIP that I am not bringing up for the discussion today; it would be sensible to include at the same time as the ENR extension. It would make a lot of sense to activate it at the same time because it would help to use this format. Use the format also, doesn't buy you much. You actually have to relayed over the network for this to be actually useful.

I think it answers both of your questions. The way I would like this discussion to go is to just, if anyone has any question, I am happy to answer them just now

**Alexey**: I read the EIP and it's long overdue. Qn - what is the upgrade path that you are thinking about? Does it require everybody to upgrade simultaneously or can be done over some period of time?

**FJL**: Just with this EIP, because it is just the data format, the way like the magician consensus will be achieved, people will have to just implement it. We can then compare with the record generated by the one implementation to the other by unit test or something. We would know that all of this can generate these records correctly and they are actually valid. When it comes to integrating it to the discovery, this is something that doesn't require any specific cut over date. We can make this change in a backward compatible way such that nodes that do support it will or can use it and those that do not support it will just ignore it.

**Alexy**: I would recommend to include this comment that you just made.

**FJL**: It is in the [other EIP](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-868.md) that uses the format. Again, it is just about the format. The thing I wanted to get for a long time was someone to look at it and sign off on it. And say, I am a client implementer, I read this EIP. I think it is good way to represent arbitrary node information. This is really all I wanted.

In the mean time, I've integrated it in Go Ethereum. It is pretty core to the Go Ethereum network now because basically any time any code deals with any kind of node is represented internally as one of these things. I think it is a good way to represent node information. Just as I said, we don't actually use it over the network just now.

The upgrade path would be to implement the other EIP that actually uses it in the existing protocol or to implement in the DNS discovery EIP. Both of these can be done without a specific cut over date. 

**Jacek**: In terms of implementation effort, how would you score?

**FJL**: The basic format is really simple. I have a python implementation. It is like 80 lines or 100 maybe including some convenience code. Just the code is very simple, it's a RLP list of variable link containing alternating key value pairs. There is some crypto involved for verifying the signature but that's it.

The hard part about ENR is actually generating it properly. It is something that take a bit more code in Go Ethereum because one of the key changes with the ENR is the node information is signed.

In clients, anytime you want to tell someone else about your IP address you have to give them a signed representation of IP address. You better be pretty sure about your own IP address.

In Go Ethereum, we have a prediction mechanism that continuously monitor the UDP traffic and detects when a local internet facing IP changes and then it generates a new version of the node records signs it and makes it available. This is something that is not in the EIP, because the EIP is just a format of creating signed records of information. You don't have to go through these lengths and you can totally implement in a simple way. But if you want it to be really well you might have to add couple more hundred lines to add the infrastructure to figure out when you should make a new record.

Did that answer your question?

**Jacek**: This is exactly the code that I was looking for, thanks. 

**Alexey**: You are mentioning other EIP that logically fall from this. I think it will be useful to actually have the bigger picture. It looks like a good way to proceed but may be it is also good to show what is the big picture like?

**FJL**: Absolutely, the big picture is in terms of peer discovery, we have this long term problem of you don't know much about the node just from the information available. All you know is the IP address and the port to connect on. From that information, the system is reasonably secure at the moment. The downside of this is it is the index of all the nodes that exists including any swarm nodes on the other blockchain. Any time Go Ethereum fork to create a spin off the Ethereum, couple of participant that don't actually belong to the network would actually want to connect to. Basically the current discovery system is index of all the node but it is like every node ever. The thing that we wanted for a long time to distinguish the node that were before we ever connect to them. We want to disconnect the nodes that are not interesting to us. This is the one use case for it.

The other use case for it is to allow client implementers to go forward with alternate transport. The big topic for long time has been to remove their RLP implementation in ETH 1.x and way forward for that in backwards compatible way would be to announce the support as alternate transport. You would want to announce that before others connect to you so that they connect to you with this knowledge that you are going to support the thing they want.

This is the big picture of it. How to integrate with that - the various mechanism and place fr the discoveries and the roadmap is to sneak into the existing discovery protocol as an extension so that you can use it if you want. Most of the nodes aren't going to use it. The upcoming version 5 of DHT is natively going to support it. If you are going with the next version of DHT you definitely going to need them.

The other EIP out there is for the DNS discovery. That is like a different discovery that doesn't rely on DHT and would be useful for people using private network. We need signed nodes record for that because you need to get your node listed. I wanted to make it transparent who can see your nodes. With DNS discovery, node listed are signed and entities publishing the node list cannot change information about the participants inside of the list because they are all signed by the participants themselves.

There are a lot of things that we can do once we have shared format in place. If we have this basic infrastructure in place, we can actually negotiate these extensions to the regular protocol.

Does that answer questions about the future?

**Matthew**: Yeah, I am in favor of the ENR.  

**FJL**: With the current implementation, I wouldn't want to get too deep into this discussion because we are not quite ready for it yet. One problem with adding too much into the existing system is that there are always going to be a lot of participants that will not support the EIP because they are old software. And, we don't want to fragment the DHT. The security of mainnet is higher with more participants we have and we don't want to loose anyone now.

**Matthew**: Right, it is really more of keeping the existing DHT with augmenting with some additional meta data for some set of the peers that would be in the DHT.

**FJL**: Lets have this discussion. I keep this EIP in networking category and there aren't too many proposal. Just open an issue for question and suggestions.

I will be happy to discuss any idea about future of networking in that repo.

**Hudson**: Sounds great, anyone opposed to this? Otherwise we can go forward. 

**Boris**: From the process perspectives and may be this also solves the problem if people not looking at it, is there something that we do about last call - signaling.

**Hudson**: I think that is a separate conversation following EIP 1.

**Boris**: I will take it there when we do some work with 1233 as well.

**Hudson**: Okay.

**Fredrik**: I think the part of the problem is too granular for the data record. Without the greater context, it would be just another data structure that looks as good as any other data structure. I think getting the context in is actually necessary to make decision on this.

I would actually suggest to implement it in just one client.

**FJL**: Is there anything that I could do to make it easier for you?

**Fredrik**: At this point, I understand it and agree with it completely.

**FJL**: Because I want to do it right, is there any one else who has objection? I will take this as a 'No'. I have a quick question related to it. I am sorry that I didn't put this on the agenda.

Over the past weeks, we have revamps the network specifications one more time. I think they are complete now, I am very happy that we have fully specified network spec now.

Other thing that I have done is that I've copied over the specification of the Ethereum wire protocol from the Wiki to the repo and made it tiny bit nicer - added some more concept and description.

What I would like to request is that IP allowed to replace the spec on the Wiki with a link to that actual specification in the repo. From now on if anyone has to add anything to the spec, they have to open a pull request, would that be okay for everyone?

**Alexey**: I think this is a great idea. To improve the specification, we need this.

**Boris**: The same thing happened in JSON-RPC spec got merged into an EIP. Bunch of interested people have tunneled into a repo. I think this nicely falls out on working groups of certain areas of the stack. Essentially having an EIP and knowing who is responsible - super useful.

**FJL**: I agree. other thing that we've done is that we moved the light clients specification there, so it is just alongside the EIP specification. It is similarly good and might be interesting for people because most people actually have hard time finding the specification for light client because it is on someone's private wiki page.

There is now an official page. I had discussion with Afri about copying Parity specific protocol for the repo but may be not making the official source for them. I still think that this is something that I could do because there are no legal restriction but it will be nice to hear back from Parity team.

**Fredrik**: That sounds good.

**FJL**: I will do it next week.

**Alexey**: We could make a follow up in the next call and you can comment how it went.

**FJL**: I think its time for us to have the official source of spec that isn't the wiki. Because I just keep seeing people like adding random parts of it all the time and I think it's actually much better to have a decent record.

**Danno**: Can we add discovery version 5 in the wishlist for this?

**FJL**: The original plan was to submit it as two different EIPs but it's kind of weird. Actually, now it turns out to be weird to actually have this like super large EIPs specifying the entire protocol because there are just too many things there that you know we need to come so I think the the process for old discovery protocol has been so far that we've just committed a draft to the repo now. So there is a draft now for the wire protocol. But the way we want to move ahead with this is we're just going to keep editing that draft until it's fine and if anyone wants to participate in a development process you are free to come over to the repo and add your suggestions, open issues, whatever.  I think at some point we're going to do is maybe we're just going to write an EIP  that says this is a new protocol here's the link and do we want to schedule it for because it doesn't really make sense to copy the entire spec into a EIP it's just too big and adding rational content for every single thing. It's better to do that way.

**Boris**: Pointers, that's the thing. Describe it briefly and then a pointer to where the spec is maintained. Maybe an additional thing again in the who are the humans, if the EIP can get updated for who's the point of contact? That would be really useful.

**FJL**: It's too early for the EIP now because we haven't actually fully finished. I mean there are so many interested parties in discovery revive; I mean we're also discussing it separately in the Ethereum 2 discussions and with IPFS people who are also sort of interested in it. So it's just that there are too many of people interested in it right now to just make the EIP now and sort of finalize it, we just have to finish it first.

**Hudson**: Sounds good.

**Matthew**: I also wanted to add that if we include a link to any sort of repos, we should also include the commit that's being reference to.

**Hudson**: All right, thanks so much for all that Felix I think it's going to be very helpful.

# 3. Eth1x Working Group Updates

So, next up we have the Eth1x working group updates.

**Hudson**: So let's start with Alexey. What's the latest on the State Fees?

## 3.1 State Fees

**Alexey**: Yes we still call it State Fees. It now may be moving in the hybrid territory between State Fees and something Stateless. Last meeting I mentioned to do data analysis on the viability of Stateless clients. So what I did since then I have a coded up at the port side which is essentially producing the block proof in some serialized format and also in the other side if it is actually part of the block proofs then tries to execute the blocks using those block proofs verifying all the hashes. That way I am sure that the number I am getting is pretty accurate, how many bytes do I need. So far I've been able to run this through to about block 4 million and there are some issues on the way but I solved them but then there's still more. I give you some preliminary data but it doesn't mean a lot because the interesting things are actually starting after the block for 4 million. So let's give you a quick overview of what I found. So essentially first of all the block proofs in this Stateless client idea comprised of several things.

The first of all it's the hashes which are basically the components of the proofs of the Merkle proofs. Then there are the keys and values and so essentially these are the leaps of the state trie. So the keys are essentially like a hash of the accounts and bodies are the serialization of the account. These needs to be present for the cases where for example the transaction reads out the account.

Then there is the code of the contract. So if the transaction accesses certain contract I need to run something, these block proof has to provide the code of the contract, otherwise there is no way to execute it.

Finally there's also something I called masks in this way. Essentially, this is the way to describe the structure of the proof. Because the proof is essentially kind of the portion of the tree starting from the root and you have to describe the structure somehow to be able to reconstitute this little stop tree from all the hashes and short keys and values. 

I also split the analysis in two parts. I do separate analysis for the main trie which contains all the accounts and separate analysis for the contracts. The reason why I do it just because you weren't you to evaluate whether we wants to do stateless client for everything or we just want to do stateless clients for a contract storage and do the state fees for everything else for date for the actual account. So far up to the block of 4000 the rough numbers are - so let's say that first for the hashes. So the masks that describe the structure of the insignificant to the structure, let's say for about block 4 million the size of the hash no proof or about 130 kb per block but I but I expect this number to rise. This is only for the non contract storage or it's just going for the account.

For the contract storage the number is about 60 kb. So, in total it is going to be 200 kb. These are only for hash that constitute the proofs. As I said, structure is insignificant. For keys and values, which are not in contract, they are about 12kb per block and the contract keys and values 4-5 kb per blocks. Then the codes of the contracts are about the 50-60 kb per block. As you could see the biggest part of the whole thing is so far is the proofs and hashes. As I said, the activity of the contract will increase and we will probably see the big explosion of this. I will keep running the analysis and I hope for as soon as I get some interesting numbers for block 5 million, 6 million then publish in a blog post. Thats the update.

I hope to include this into the next version of State Fee proposal 

**Hudson**: Okay, sounds good. Thanks for the update.

## 3.2 Ewasm or Simulation

**Hudson**: Is there anyone here who wants to talk about Ewasm or simulation?

**Guillaume**: Actually I was just looking for that. There has been some conversations and some work on the benchmarks. I am told that they should be right around next week. When it comes to Eth 1.x, I've got the prototypes that runs ahead of time compilation so we take wasm file to compile x86. And we just run it's like we just want to the conference this way so that's what's up and coming but it needs to be stabilized. It was the Ewasm update as I have it.

**Hudson**: Awesome, thank you.

## 3.3 State Pruning/Sync (ETH V64 Call for Proposals & Stopgaps for cleaning up discovery peers pre-Discovery v5)

**Hudson**: The other piece we have for the working group updates ETH V64 call for proposals and stopgaps, that was Matthew Halpern and Jason Carver. So if you could explain what that is and they updates on that?

**Matthew**: Yeah absolutely so I think the motivation is that there hasn't been any sort of upgrade to Eth wire protocols for some time. I think even so far back as 2015 so the idea was just to open a ring on [Eth magicians](https://ethereum-magicians.org/t/forming-a-ring-eth-v64-wire-protocol-ring/2857) to see your what ideas were out there what were people thinking. That's where thing and I'll post the link in Zoom, but there's actually been a lot of good discussion going on there. We have good proposals spanning multiple client implementers, the changes have ranged from simple thing to more complex things like supporting client-side full control. At this stage I think I'll leave the call open for another week but then starting to get a key stakeholders are people that are interested in moving forward with there proposals and getting them into EIPs and starting to the client developers who would actually be interested in supporting that and then of course getting reference.

**Fredrik**: I would want to say that what you are talking about is something broader but when it comes to syncing algorithms both Geth and Parity are working on one and both have POC ad implementation. We focus on those and try to say this is not good about this algorithm and this is good about it. There are literally thousands of proposals and we don't have to go through them.

**Matthew**: Yeah, I don't think we have to go through the formalities too much especially for your fasting syncing and things like that. I assume that everyone working on this Jason, Alexey and you are all talking and agreeing on what primitives need to be there. I don't imagine that too many external parties we trying to interfere with what you have in mind in there specially if you have something working. I would let Jason also speak on that.

**Jason**: Yes I guess that's a good segue in addition to the prototypes from the Geth and Parity teams, there are some other team that I have been talking to TurboGeth, Swarm about some of the things they might be able to support here. From Trinity perspective,  I've been trying to write up the draft proposal for tries to incorporate. Some of them are still early on so or anyone else wants to get involved it is a great time to do that.

There's still more to do on a syncing up with Parity. Feel free to reach out if you're another client or have other ideas about where fast syncing should go.

**Fredrik**: When it comes to thinking specifically there is also a gitter channel that you could join.

**Jason**: Reach out to me at gitter. And we will sync up with the group.

**Matthew**: Just for my understanding how this joints are the efforts for the next fast sync proposed? Are there multiple independent groups working on this or is everyone collaborating together?

**Jason**: There's conversation but there's still a fairly disparate ideas right now about how it should go. So yeah, it hasn't called us yet.

**Fredrik**: We are in bike shedding territory here, where we just will never reach any consensus because everyone is married to their particular solution.

**Tim**: I would say for sure implementations win over ideas right. That's that's like a quick way to whittle down from ideas to final solution. I do think it is important to talk to different groups and figure out solution for implementation. We should iterate on the ideas for implementation for sure.

**Alexey**: I wanted to add to this, the reason why there is no convergence of fire in these ideas is because as far as I know that most of the groups are trying to actually make some kind of implementation or modeling. Because the subject itself is not so simple as that you can just figure it out in your head. You actually have to do some code, modeling and stuff like that. So once we've done going to get further in that we can actually see the other ideas converge, that's what I would expect. It's a bit early so I was going to suggest that, in this situation where there's a lot of activities on some topic; you should not try to constrain yourself with some sort of deadlines - like okay, by May we have to do everything because that kind of makes us cut corners. We only need to have a deadlines when we actually when there's not much activity going on. If people are genuinely writing code and trying to make things work, then I think we will have to give them the the runway.

**Matthew**: Sure, so we can see if there are any v64 enhancements that can be separated and don't interfere with this is perfectly fine.  

**Hudson**: Okay cool, that all sounds good.

## 3.5 [Istanbul & ETH1x Roadmap Planning Meeting - April 17th & 18th in Berlin](https://ethereum-magicians.org/t/istanbul-eth1x-roadmap-planning-meeting-april-17th-18th-in-berlin/2899)

**Hudson**: So the next thing, Boris has organized Istanbul and Eth1.x roadmap planning meeting in Berlin April 17-18. Boris if you want to go over that quickly?

**Boris**: Sure once again apologies that it's somewhat tight timing. I decided to go ahead and plan it. Alexey is available and is going to be there and we've got a number of other people who committed to being there. Basically the point is to sit down and actually look ahead at Istanbul, review the EIPs, have anybody who's proposing EIPs go over those. Essentially very similar to the Stanford meeting and ideally we can get some more work done in person around looking out further ahead. I think Alexey has done a great job of having areas or related EIPs in multi hard fork planning. So the goal is just to go over that and in general see where Eth 1.x is heading and work together with implementation teams and get feedback on that and really just get our act together for for this hard fork. Roughly, it's almost exactly a month before the hard deadline to accept proposals. Ideally we then know exactly which EIPs are most likely to be proposed, inclined teams can make plans and/or give feedback on what resources they have available to actually get this done. Eth magicians has a post with all of the details and piece to get in [here](https://ethereum-magicians.org/t/istanbul-eth1x-roadmap-planning-meeting-april-17th-18th-in-berlin/2899). If you can, let us know. If you are coming there's a link in there just do a little [Google form](https://goo.gl/forms/AZv018Cgd2B3YzuZ2) or just contact me directly and I will be working on agenda and presenters and another thing like that. It will likely be at full node in Berlin because I know some people have started asking me where they should book hotels and so just the Gnosis team volunteered full node, so likely that end of the city.

**VB**: I probably won't be able to show up but and I know that there is interest in EIP 1559 which is the Fee Market change. So if people want to discuss that would there be room if you remotely.

**Boris**: Absolutely. Ideally, lots of value to meet in person and doing whiteboards but we absolutely want to support the dial in especially for proposers.

**VB**: In person there are a lot of EDCON and Hackathon that are happening around, it won't cover everyone but is a great place to finally chat with a lot of people.

**Hudson**: Yeah that sounds good. I won't be able to make it either because I'm going to a giant Star Wars event. But yeah I'm looking forward to the remote connection so I can tune in. Was that it Boris?

**Boris**: Yeah links are in the chat here and I'll tweet about it again so it's on top of everyone's feeds.

**Hudson**: Okay thanks. Okay we're making good time actually.  


# 4. Testing Updates 

**Hudson**: Let's go to testing updates with Dimitry.

**Dimitry**: Okay hello. The main agenda for me right now is to make all of the state test to make RPC protocol. Some Titan team also working on the same kind of thing. We think to develop generic genesis file format mandatory for every client to implement. Actually suggest to open an EIP for every client to implement this protocol for genesis file. Overall, I think we still need to support EIP in CPP client because its stable and it works. 
How you think about this genesis format for every client? Any comments from client developers? 

**FJL**: I think it would be really great. We wanted this for long time.

**Dimitry**: One year already. What does a proper way to open an EIP for that?

**FJL**: The usual way will be you write a draft,  you just copy one of the existing EIP and fill out the sections and then bring it up here. Is that the current process just bring it up on this forum?

**Hudson**: For calling on, it be a good idea to make an Ethereum magicians form post and then link that in the EIP as there's a section called discussion side and you can put the theory of magicians link in there. Yeah let's bring it up, let's do a follow-up on this call to see after people look at the EIP, what their thoughts are on it?

**Dimitry**: Let me prepare this EIP. In the next developer call we could discuss it. I will send you the link.

**Hudson**: Thank you very much. Any other testing updates fussing or otherwise?

**Martin**: So we are progressing on the fuzzing regarding we are adding some new tests and doing some general changes to the framework sometime betweeen now and for the next hard fork. So it's going through some changes.

**Hudson**: Great.

# 5. Client Updates 

**Hudson**: Let's run through client updates real quick.

## 5.1 Geth

**Peter**: As for the client update one interesting thing that we have been working on for about 1 month is levelDB optimization. Actually over the past month we kind of managed to speed up levelDB (for huge databases meaning archive nodes, the big scary one) by about a factor of seven. Which means that we haven't really run too conclusive tests but it kind of seems that with compared to our current stable release which does an archive syncing in many weeks, 6 weeks? I haven't actually ever did one of those but based on our latest benchmark let's do that in 7 to 10 days currently with the latest Geth code. I am really really happy about that and apart from that, currently working a lot on the slimming down Geth memory consumption wise. Some kind of works around the data storage. So perhaps we can move more data. Thats about it.

**Hudson**: Wow so that's 8 weeks to 7-10 days you said?

**Peter**: I think 6 weeks to 7-10 days. Yes. 

**Danno**: It fast sync and all?

**Peter**: No this is archive node full sync.

**Martin**: I probably improves passing quite a bit as well.

**Hudson**: Cool.


## 5.2 Parity Ethereum

**Hudson**: Alright Parity?

**Fredrick**: No significant update we're also working on some database improvements and other things but nothing is shaped yet.

## 5.3 Aleth/eth

**Hudson**: Aleth?
 

## 5.4 Trinity/PyEVM

**Hudson**: okay Trinity? 

**Jason**: I don't think anyone's here last time we had an alpha released before the last all core dev call with Constantinople support as well as performance stability. Masters continuing to improve pretty quickly so look out for her next update about a week.


## 5.5 EthereumJS

**Hudson**: Great, anyone from Ethereum JS here? 


## 5.6 EthereumJ/Harmony

**Hudson**: So Harmony couldn't make it but they said that demonstrated 1.5 months worth of stable run time with no consensus breaks, memory leaks, space issues or performance segregation detected during that period. The version they have right now looks pretty reliable. That's exciting.


## 5.7 Pantheon

**Hudson**: Pantheon?

**Tim**: No major updates on our end.


## 5.8 Turbo Geth

**Hudson**: Turbo Geth? 

**Alexey**: No updates from me apart from the fact that I started to do this for the prototype of stateless client.


## 5.9 Nimbus

**Hudson**: Okay, Nimbus?

**Jacek**: It is running a full sync all the way through. We're going to take a moment and celebrate that by doing some refactoring on some of the issues that we were working so far.

**Hudson**: Cool, congrats. 


## 5.10 Web3j

**Hudson**: Web3J?

**Ivaylo**: We drafted the release of 4.2 this morning. I think the most interesting thing is that we have ERC 20 interface baked in. It allow you to write your ERC 20 tokens in Java using Solidity. I'm off to this 4.2 release is finalized and basically unless people's computers blow up, Web3J will be back burner for us. Our focus right now is JVM instrumentation.


## 5.11 Mana/Exthereum

**Hudson**: Mana?


## 5.12 Mantis


## 5.13 Nethereum

**Hudson**: Nethereum? Is there any other clients that I missed?


# 6. EWASM & Research Updates 

**Hudson**: Research updates, Danny and Vitalik?

**Danny**: We just released the spec [v0.5.0](https://github.com/ethereum/eth2.0-specs/releases/tag/v0.5.0). Primarily the phase 0 beacon chain protocol and some stuff from phase 1. The major thing here is that we made the entire spec executable and have a series of State tests which is a big win. In Sydney we're going to be doing some sort of like 2.0 Workshop before EDCON  and we're looking into setting up remote participation. So I'll be sharing information on that if you're not going to be there. Vitalik, anything else? 

**VB**: I mentioned in the call yesterday that we get and I made a lot of progress on the [Light client protocol](https://ethereum-magicians.org/t/eth2-in-eth1-light-clients/2880). We are looking at how it makes sense to start implementing. Aside from that I would guess the main thing is probably busy roll, stabilizing and the phase 1 game of custody improving quite a bit. Also want to repate that we want the feedback on the phase 2 in general.

**Danny**: I think there's a magician's link recently read kind of dumped the things. I remember you have already checked this out at least some of the networking people. But there is a basic networking protocol up for review in the beacon chain , [ETH 2.0 spec repo](https://github.com/ethereum/eth2.0-specs/pull/763). So if you haven't taken a look and you have some interest in digging into the networking protocol and help me out there please do.

**Hudson**: Any other researchers have any updates, I think that there's a few others in here if you have anything. 

**Danny**: Oh I don't think there's any EIP written yet, but something that we want to write up soon and push forward in the next hardfork is a BLS 12381 precompile in the EVM that would open up possibilities of utilizing the 2.0 things from 2.0 inside the context. Vitalik you want to add anything?

**VB**: I opened up a [magicians thread](https://ethereum-magicians.org/t/things-to-decide-for-phase-2-copy-from-eth2-0-specs-github-issues/2895) about the light client materials. The Eth2 light client inside eth 1 would require precompile and it would very significantly benefit from all data gas cost reduction. And that's probably also something that would give us a one-liner that seems to be in line. 

**Boris**:  I think one thing to bring up on the topic of precompile so there's another precompile proposal by Remco would like to see it in Istanbul. So I suggest one of the things to go over in person is if there's an opportunity to work together on precompiles rather than be every client implements their own. so not for discussion just right now but just bringing it up and to put it in people's minds.

**VB**: And I also saw the generic elliptic curve precompile idea which is interesting the one thing to point out is. That's not a replacement for a BLS 381 precompile because you cann't do pairings over a generic elliptical curve precomplie and we are doing for BLS 381 generic support.

**Boris**: Yeah I think all of these obviously we don't want to do any infinite pre compiles but get help from Remco and yourself another cryptographers and see what are the logical ones to get into the ETH 1.x line.

**VB**: Agreed, and it's also not just a question of cryptography is also a question of what our priorities are. For example BLS 381 is nice because that improves interoperability with zcash and other blockchains. But additionally does this like extra big thing of making it viable to have it use to light clients. Whereas for other hash function might have like different value in is not a kind of cryptographic liability as it is about what concrete things do we go through in and want to achieve.

**Alexey**: Yeah I definitely agree that today that the link between 1.x and 2.0 should be one of the the priority because eventually we want to do this finality gadget at some point.

**Hudson**: Anything else? Awesome! We have one minute left and I think we'll wrap it up. We didn't come back to ProgPOW so I guess want to do that next week. Boris do we have a discussion on magicians about ProgPOW that is like a central one?

**Boris**: Lane cross posted that, yes. Action items and I think Tim's on the call taking notes as well, is mainly just point of contact and audit details. I don't think we need to discuss it again like if we want to have a call right now, is there anyone who's saying, you know progpow Over My Dead Body, otherwise it's over to audit and we only need to bring it up again if there's an update from essentially the audit working group. Does that make sense?

**Hudson**: That sounds good to me. Thanks so much Boris, you've close the issue.

**Tim**: One thing we started talking about but didn't quite wrap up with the idea of smaller hard forks versus larger hard forks? I'm not sure if we want to do that or bring it up on the next call? What's think about it and bring it up on the next call? 

**Danno**: Do we put time box of some of these request to the next call to?

**Hudson**: Just like things on the agenda in general?

**Danno**: Yeah, timeboxing because apart from ProgPOW there are some of the other issues they've been spoken for the next meeting also could turn into alcohol consumed discussions.

**Hudson**: Okay, good idea. I'll try to estimate how much time you should get I guess or people can give suggestions.

**Danno**: Yeah we can hash it out in the thread.

**Hudson**: Alright, sounds great. Alright, thanks everybody have a great day!

# Date for next meeting
March 29, 2019

# Attendees
* Alexey Akhunov
* Boris Mann
* Brett Robertson
* Daniel Ellison (ConsenSys)
* Dankrad Feist
* Danno Ferrin
* Danny Ryan
* Dimitry Khoklov
* Eric Kellstrand 
* Felix Lange
* Fredrik Harrysson
* Greg Colvin
* Guillaume Ballet
* Hudson Jameson
* Ivaylo (Web3Labs)
* Jacek Sieka
* Jason Carver
* Jon Stevens 
* Martin Holst
* Matthew Halpern
* Meredith Baxter
* Peter Szilagyi
* Pooja Ranjan
* Tim Beiko
* Trenton Van Epps
* Vitalik Buterin
