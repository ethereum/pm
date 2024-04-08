# Consensus Layer Call 126

### Meeting Date/Time: Thursday 2024/1/25 at 14:00 UTC
### Meeting Duration: 1.5 hour  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/938) 
### [Audio/Video of the meeting](https://youtu.be/_pFRJ1it608) 
### Moderator: Danny Ryan
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
126.1  |**Deneb Updates** Danny Ryan shared a brief update on the Deneb upgrade. On Wednesday, January 24, the Ethereum Foundation released a blog post containing all the latest client releases for the Deneb upgrade on Sepolia and Holesky. These two test networks will be the last testnets where the Deneb upgrade is activated before Ethereum mainnet. Sepolia is scheduled for Deneb activation on January 30 and Holesky one week thereafter on February 7.
126.2  |**Electra Discussions** The remainder of the call was spent discussing candidate EIPs for the next upgrade after Deneb dubbed Prague/Electra. Prague is the name for the upgrade on the execution layer (EL) of Ethereum, while Electra is the name for the upgrade on the CL. Last week, developers reviewed proposals for Prague, primarily impacting the EL protocol. This week, developers reviewed proposals for Electra, primarily impacting the CL protocol.
126.3  |**EIP 6110: Supply validator deposits on chain** eku developer Mikhail Kalinin presented EIP 6110 which appends validator deposits to EL blocks. The motivation for this code change is to reduce the complexity of client software design and improve validator UX. Danny Ryan called the EIP “a major security improvement” for Ethereum. Tim Beiko, Protocol Support Lead at the Ethereum Foundation and Chair of the ACDE calls, added that the EIP was one of two CL-focused EIPs that EL client teams have already signaled support for in the Prague/Electra upgrade. EIP 6110, like a few other CL-focused EIPs proposed for Electra, requires protocol-level changes to the EL. Given the support for EIP 6110 from both CL and EL client teams, developers agreed to move forward with inclusion of the code change in Prague/Electra.
126.4  |**EIP 6914: Reuse validator indices** EIP 6914 would enable the index number of fully exited validators to be reassigned to new entering validators. The motivation for this would be to prevent the unbounded growth of the validator index over time. Lighthouse developer “Dapplion” presented the EIP but noted that while this code change is important for the long-term health of Ethereum, it does not need to be prioritized in Electra. Developers agreed not to prioritize EIP 6914 in Electra.
126.5  |**EIP 7002: Execution layer triggerable exits** Danny Ryan shared background on EIP 7002. “There are two [validator] keys. There's the active key and the withdrawal credentials. Active key manages the stake. The withdrawal credentials ultimately own the funds. Since Phase Zero, there's arguably kind of a bug in this relationship in that only the active credentials can trigger exits. So, if the active key is lost, or if there's some sort of more dynamic relationship between who owns the active key and who owns withdrawal credentials, you're going to have pretty degenerate cases and degenerate outcomes.
126.6  |**EIP 7251: Increase the MAX_EFFECTIVE_BALANCE** Mike Neuder presented EIP 7251, which increases the maximum effective balance of validators from 32 ETH to 2048 ETH. For background on why this code change is needed, read this Galaxy Research Report on the issue of validator set size growth. Neuder noted that this code change is “more controversial” than others due to its complexity and dependency on other code changes such as EIP 7002. Lighthouse developer “Sean” expressed his support for the EIP but given its complexity recommended looking into ways to implement the changes over multiple hard forks, instead of all-in-one upgrade. Neuder was supportive of the idea. Lodestar developer Gajinder Singh was not in favor of breaking up the implementation of EIP 7251 across more than one fork, due to concerns that this would create more of a headache for developers in the long-term.
126.7  |**EIP 7547: Inclusion lists** EIP 7547 creates a mechanism through which validators can forcibly include certain transactions in a block. The main motivation for this is to improve the censorship resistance of Ethereum. Neuder, who authored the proposal along with several other developers, explained that 67% of block builders are already censoring transactions on Ethereum and over 90% of validators receive blocks from third-party builders. There is a clear need for stronger censorship resistance on Ethereum. However, Neuder noted that there are open design questions on the implementation of forced transaction inclusion lists, primarily regarding the precise conditions that need to be met to enforce the list.
126.8  |**EIP 7549: Move committee index outside attestation** Dapplion shared EIP 7549, which is a code change impacting only the CL. The code change would make the aggregation of consensus votes more efficient and can be implemented in a variety of ways, ranging for low to high complexity. Ethereum Foundation Researcher Dankrad Feist was in favor of choosing the simplest way to implement EIP 7549, which is simply to set the value of a particular data field in CL clients, the “index” field in “AttestationData”, to zero. Danny Ryan was also in favor of this strategy. Developers agreed to move forward with the inclusion of EIP 7549 in its simplest form in Electra.


**Danny**
* All right. We should be live. Welcome to Consensus Layer Meeting 126. This is issue 938 and the PM repo. first off, we will have, any discussions related to Deneb, testing, test nets, etc. then we will begin our discussions around Electra. Next planned upgrade hard fork on the consensus layer. and then a quick,  Discussion or note around, some research around state participation targeting.
* Cool so we can go ahead and get started. there was a blog post yesterday containing releases for, I believe, all main net clients. For the the next. Deneb. Dencun testnet any notes on that other than the existence? All right. 
( Great. if you are running validators, please upgrade. If you run nodes only sustenance, please upgrade. If you plan on using, blobs, it is time to test them. any other discussion points around testing test nets or anything related to Deneb for today? Okay. Great. Next up. Electra. 

# Electra discussions [5.39](https://youtu.be/_pFRJ1it608?t=339)
* So there is an issue in the spec repo. this is 3449 and the specs repo is the specs repo. Here's the link. Okay. Thank you, this is going to be we're going to move through this list. we may or may not get to everything today. and the general format will be quick one of the authors should give a quick, high level description of the EIP.
* And then just some notes on relative complexity, you know, in general, maybe some comparisons to prior work. the components it touches and if it's cross-layer. and then, open for general discussion. I do appreciate the teams that did, have some brief posts on what they are eager to support and not support for the fork. 
* But please also do elevate that here, either as individuals or as a team. Just so that everyone gets on the same page. Cool. any questions or thoughts before we get started here? Okay. this is the beginning of this process. this doesn't necessarily mean that,
* All decisions will be made today. and especially as kind of specifications become refined and packaged and people do some initial prototyping, obviously like this conversation will continue as it has in the past. okay. Cool. So looking at that list, the first EIP on there is EIP 6110. Is Mikhail here? 

# EIP-6110 [7:33](https://youtu.be/_pFRJ1it608?t=453)
**Mikhail**
* Yeah. I'm here. You can speak on it. Yeah. Cool. Okay. So, yeah. This the EIP, basically. Uh deprecates. F1 breach, that we still have today, to bring new deposits, into the Beacon chain. So it,  Yeah. And with the deprecating Eth1 bridge, we deprecate, also, if one data voting, and, the things related to it, like dependency of, CL on the Json-rpc API, because currently today, deposits are being fetched via json, RPC API, from execution layer clients, which is kind of maybe stressful for our execution layer clients. sometimes.
* And also it creates some problems. 
* So with the configurations, from time to time, of for node operators and developers have to solve those problems. Also, it's ever growing, data complexity because all those deposits, are required to reconstruct the depository to process new deposits. And this is done by CL clients today when they are, syncing with the chain. yet, it will be fair to say that there is an alternative proposal to cut this, complexity, which is basically deposits can deposit contract, depository snapshots, which is, yeah, there is an EIP for that. 
* Yeah. But this is kind of ultimate solution for getting rid of this Eth1 bridge. Also, related thing is the security of the protocol. there is a design flaw, that,  yeah, we know for several years already. And. Yeah, for a mainnet this is not an issue. But yeah, for general, the protocol practically it's not an issue because it requires a lot of, adversarial stake. Yeah. And, it requires CL, EL work as well. It requires CL change, but on the other side, it is very well scoped and the change is really minimal. 
* Pretty, kind of isolated. And in terms of testing and in terms of, implementation, and, well, there is already a prototype, in Lighthouse and Besu and I know that, other teams are working on prototyping this EIP. We ran, several devnets during the prototyping phase to see how it works, how it plays out. 
* Yeah so and I would say that the specifications are pretty mature. Yeah. And, we did some fixes after prototyping phase. Also, I would like to say that, on the activation, like when this EIPs, is activated in the network, when the change is activated, it does not require any further, coordination on the transition period. from if one data breach to this new mechanism. 
* So it will it's pretty deterministic and will happen automatically. And, if one data breach will be able to, be deprecated, thereafter after this transition period finishes, which is like several hours, and yeah, it can be done in an uncoordinated fashion. So that's mainly sorry for being hectic on it. I did not prepare a presentation, but that's the kind of summary on this EIP

**Danny**
* No that's perfect. I think most people for most of these EIPs have pretty deep context. So just a brief overview is really great. I guess I think almost everyone's call understands like the security of what you could call this ETH1 bridge or the deposit bridge, you know, has this, honesty assumption on proposers over a certain time horizon, rather than just a straight validation of these two systems that are now connected and related to each other. And so it's certainly like a major security improvement, although an unlikely.
* In normal circumstances place for an attack to happen. Are there any questions around this EIP? both security feature set complexity and you can hear. Okay. I believe that there has been general signal for support, on the execution layer. Was that time would you call that, like, unanimous? Meaning, in the event that the consensus layer wants to do this, you know, and no further issues or, having to prune things due to complexity like that, this would be moving forward as of now. 

**Tim**
* Yeah. So I think 6110 and 7002 are the two where if we have to start working on a devnet tomorrow, along with another one that doesn't impact the CL, it seems like all EL teams would, start working on. So. Yeah. 

**Danny**
* Yeah. Cool. Is there any are there any CL teams that are not supportive of this in, Electra as of their understanding of the fork today? I say not because I've seen a lot of signals for support in both some of these blog posts as well as, in the chat. Okay. generally very positive signal on this on both layers. I don't know if we have like. Terminology. Official terminology to use here. But, as of now, 6110. Move forward in Electra.. Next. EIP 6914.  Reusing validator indices. Dapplion, do you want to take this one? 

# EIP-6914 [14:16](https://youtu.be/_pFRJ1it608?t=856)

**Dapplion**
* Sure. So I can. Quickly say that this EIP is useful in the long term, but it's not the time to. Roll it out. So very briefly, I would say we should skip it for the fork. I'm not sure if any team wants to include it for the fork, but I don't. I'm not sure if that is wise. I did write a hackmd. I can link it on the notes, but that would be all for now. 

**Danny**
* Okay. does anyone want further detail on what this EIPs entails, or does anybody want to make the case for inclusion? Okay. And I'm seeing From a couple of different teams. Kind of a general agreement that. No need to prioritize this in the upcoming fork. Cool. Thank you. 

# EIP-7002 [15:30](https://youtu.be/_pFRJ1it608?t=930)
**Danny**
* EIP 7002. I can give a. Click on this one this is execution layer trigger will exits. essentially, just for some context, there are two keys. There's the active key and the withdrawal credentials. the active key manages the stake. The withdrawal credentials ultimately own the funds. Since phase zero, there's arguably kind of a bug in this relationship and that only the active credentials can trigger exits. 
* And so if the active key is lost or if there's some sort of more dynamic relationship between who owns the active key and who owns the withdrawal credentials, you can have pretty degenerate cases and degenerate outcomes. additionally, with execution layer withdrawal credentials. Zero one introduce a couple of weeks ago, or a week ago,. The ownership of the stake can be controlled by a smart contract, which is really exciting for trustless pools and all sorts of other more dynamic relationships in staking. But these cannot trigger exits.
* And so again, you have this pretty degenerate relationship in existing kind of across the board in this exciting design landscape. that makes the barrier to entry in these kind of trustless pools designs much higher because you then need some sort of committee construction to be able to, like, hold pre-signed exits and use them and things like that. Whereas if you're a big entrenched player, that might be a sufficient solution, at least for the time being. 
* Whereas if you're a new entrant, that's like a one of those. Semi-major things you have to accomplish. 7002 adds a what is right now written as a stateful precompile. Although, after. the way we've done the beacon route in Deneb. Dencun, it is, going to be changed to just deployed, EVM bytecode. which lightclient does have some assembly written for this? that is under review and will make its way into the EIP. That's just a note. this is Cross-layer. this is relatively straightforward on the consensus layer in that it, you know, is it a.
* A new. Operation type, but that triggers very well known kind of exit code paths. it's relatively straightforward as well on the execution layer. a lot of the complexity being able to be masked in the EVM code. and at kind of on a per block basis. doing some stuff in relation to the state that is in that EVM code and hoisting. Some messages into the, the block. As of new validity condition. Yeah. So, nothing crazy here cross being cross layers really probably the biggest complexity component. and I will say that.
* In relation to things that might happen with Max EV now, or even in the future some of the logic on the message being passed around might be future proofed for potential partial withdrawals not that that really. 
* Without changes to the validate, it doesn't really make sense today, but, that's a pending potential change in there. Yeah. I think this is very important in relation to, Just like fixing the ownership story of staking. and very importantly, I think in enabling much more trustless designs in on chain pools. 
* Any questions? anybody want to signal support or, against I guess, as, Tim mentioned, this is generally conditionally included on the execution side. and so in terms of cross layer support, we have that. Okay. Seeing general positive support. I think we saw general positive support in, the blog post that teams released. and it even notes of top priority from Prism is anyone against the inclusion of this in Electra. Great. we will, as of now, include it in Electra. please keep your eyes on, this assembly that Lightclients working on.
* That's the kind of thing that it's very nice that we get to kind of capture a lot of complexity in one place, rather than having to implement it across many client teams.
* But it's something we, definitely need to get. Right. So, EVM wizards want to do some review in the coming month or two, please? Anything else on this one? Great. Moving on to EP 7251. Mike. 

# EIP-7251 [21:20](https://youtu.be/_pFRJ1it608?t=1280)

**Mike**
* Hey, Danny. Hey, everyone. yeah. So we'll do a quick run through on 7251 and 7547. starting with 7251. I think most people in the call are are probably familiar. but to give a quick, high level overview, this this proposal is to 32th the max effective balance. currently this is set at 32 ETH and represents both the the minimum balance to become a validator and the maximum balance of a validator. So anything above that balance gets, gets swept off. So this proposal has has a number of features that that kind of make sense of it because it, it seems simple, but there's kind of a decent amount that goes into it.
* The current list of features, a link in the chat. just to run through them quickly. First is increasing the max effective balance to to 2048. Second is custom ceilings, which lets validators specify at what level they want the sweep to kick in. the third is, a consolidation mechanism by which validators can consolidate multiple validators into a single validator. Fourth would be execution layer triggered partial withdrawals. So this is kind of piggybacking on 7002, which is what Danny was talking about. And the last one is the initial slashing penalty. making that zero.
* So I guess the the high level reason for doing this EIP is. To allow some consolidation of the total number of validators we have, we're currently at around like 900,000. but many of those are representing like single entities because many entities have much, much, much, much more than 32 ETH to stake. So Coinbase, for example, runs around 140,000 validators right now. And each of those, each of those validators has to sign an attestation that has to be, aggregated and then the signature verified  for each epoch.
* So yeah, just trying to cut down on the both the network traffic and also improve some of the UX around solo staking. so I have a short like super high level list of pros and cons. that'll link here. In terms of complexity. The the reason this EIP, I think is, is a little more, controversial or has kind of been a little more uncertain is because there's kind of a lot that goes into making it, effective. One of the most important parts here is this, in protocol consolidation. And we just wrote a doc on this recently. I'll link that.
* And the, the high level takeaway here is that without an in protocol consolidation mechanism, the only way big sticking. Be able to to merge validators would be to fully exit that stake and redeploy it as larger validators, which would be a big hit in terms of of their rewards. So. That's that's kind of the incentive for the in protocol consolidation mechanism. yeah. I think in general there's lots being, that there's lots that has been written on this. I'll link the kind of general related work doc, in terms of reducing the complexity to, to get the, the scope down,
* I think. Yeah. If, if there's appetite for that, would it be happy to discuss, generally have been kind of working under the assumption that in order for it to be worth doing, it makes sense to like, kind of do it right, just because, like, if we did it and it didn't gain any adoption, then it wouldn't be as valuable. but this has led to like, yeah, some, some extra features, I guess. So, yeah. Happy to keep discussing. 
* I think that's, that's the, the high level summary I wanted to give there. 

**Danny**
* Yeah. Any questions for Mike? There is certainly some support in the chat, but also some kind of questions and pushback. Sean. 

**Sean**
* Hey, so I generally support this. I think it's really important to increase, like, the networking load for consensus messages, because then we can increase the networking load for things like increasing blob count. but with regards to like the question on. Like, how big of a scope do we want in order to like how like attractive of a feature? Or how can we get people to actually use this feature? could we also potentially do this in stages where we do like the minimum secure amount to increase maxev while also keeping like, the other consensus properties like secure unchanged.
* And then in later forks, potentially add things like in protocol consolidation or other other like of the extended features, to sort of like not have this feature be too complex. If we have too many other changes in this fork and also enable some of the nicer features, like the compounding to happen for new deposits, potentially allow people to like deposit aggregated validators as new deposits. 

**Mike**
* Yeah. So to respond to your first question, I don't think any of the features that we've described change the security properties at all, actually. Like that's a big. especially in terms of the consolidation. Like that's the main design constraint. It's like we don't want to change either the weak subjectivity or the like amount of churn. that the that the protocol can like handle. So yeah, but I definitely do agree that like maybe it does make sense to consider kind of like a mini max effective balance change. it's funny because mini Max is like an algorithm, but so yeah, happy to happy to kind of like brainstorm on what exactly that minimum feature set would be.
* I think it would probably not include the in protocol consolidation, and it probably would not include, well, I don't know. We'd have to decide about execution later. Partial withdrawals.
* But, Yeah. Thanks for thanks for bringing that up, Sean. Definitely happy to maybe chat more offline and come back next week or in a couple of weeks with, with a counter proposal. Sean. Do you mean if you.

**Danny**
* Just protocol security, or do you mean just kind of security in relation to complexity of rolling out a fork? 

**Sean**
* So what was the question? 

**Danny**
* You you mentioned security. Did you mean security, as in, like, how to make sure this protocol is secure or security in relation to just managing a complex work and reducing complexity? 

**Sean**
* So my understanding was there were some changes related to like, how we have to I think wait, exit churn for example, and changes to slashing to keep the security properties the same. And I sort of meant like there is work involved in the consensus changes related to that. So a minimum change would have to include those along with raising Maxdb and  I'm not sure exactly what else, but something like that. and just to be clear, my right now, my stance generally I think, is to like do a fully fleshed out version of this if possible.
*  But if the there's too much in the fork, then maybe there there's still a way to do a minimum version of this. 

**Danny**
* Good gender. 

**Gajinder**
* Yeah. Loadstar is of the view that we would not want to divide it across two forks. And if we want to implement it, we should basically just do it, in the single fork, because, the context division is more complex. And I think, you know, if we can sort of finalize the spec in terms of, how we are going to maintain the security basically right now, as per spec, it says that, okay, you know, the validator exits, exit churn will be respected. but then there is a certain period in which the operators will not earn revenue.
* So if we have done the temperature check with the operators that they are okay with that, and then the consolidation can actually happen so that we can see the benefit on the beacon State. then I would say that we should do it in the single fork. 

**Mike**
* Just to clarify one point on the, on the revenue thing. So, yeah, in the consolidation doc, we talked about this, the only time that the consolidating validators won't earn the, the revenue for what we're calling the source validator, which is the one that's merging into the target, is during the time between the exit epoch for the source validator and the withdrawable epoch for the source validator. So it's it's not based on the exit queue, it's just that 256 epoch delay. So in that regard like yes they'll lose a little bit of revenue. but it's, it's kind of always bounded and always constant, which is good. but yeah, thanks again for bringing all that up. Very good context. 

**Gajinder**
* Yeah. So the thing with that regard is that have are the operators have with whom we have done the temperature check with, are they okay with this little loss of revenue on there. Because the console if the consolidation doesn't happen then we don't see any benefit. So. 

**Mike**
* Yeah. We've been, working super closely  with the large operators and generally have, have kind of tailored the feature set based on not only like what we think will be good for solo stakers, but also  what they would actually make use of. So I guess both both Lido and Coinbase have have been really involved in this process and talked talked to figment last week and they're also kind of keen to continue learning more as we as we finalize the design. But yeah, I guess all the temperature  checks so far, especially once we kind of settled on the initial slashing penalty reduction, which was most of their concern. all the temperature checks have been quite good. 

**Danny**
* Terence. 

**Terence**
* Yeah. So, I've, I've, us, you guys have seen from the blog post, you know, no support. And, we all agree that we need, we need this EIP at some point. Right. But the fundamental reason is that, like, I haven't heard much voice is that do we want, like, a smaller fork in 2024 or do we want to wait until 2025 to do a bigger fork. And I and we do think that a small fork is very beneficial. So therefore we just think this EIP has too much complexity to fit in a small fork, assuming it's coming in October and November. 

**Mike**
* Thank you Terry. Yeah. And circling back to to Sean's point, maybe. Yeah, maybe if there's an appetite for that small fork thing, then thinking through what a mini version of the EIP could look like might be extra useful in that, in that regard. So happy to talk to you offline about that too, Terrance. 

**Danny**
* Let us. 

**Potez**
* Yeah. Just with regard to this PR, I just wanted to mention that, there is no mini version in terms of complexity for us. Just changing the max effective balance, is not just changing a constant. This, and the fact that we can fork into something that changes the max effective balance, even if we didn't do anything else, even if we didn't change the validator structure to have this slashing being a bit a bit mask would be very large complexity, at least on Prism's code base. It'd be very hard to test.
* We do support the EIP, so certainly we do support it. We actually want it. We prioritize Kpbs and we think this is necessary for that. But, I don't see how this can be scoped in any form for 2024.

**Danny**
* Does it exist, a prototype in any client? 

**Potez**
* I'm working on Prism for a reason because I'm working on EIPs. That includes this. And, this is the last change that I'll add because, this touches everything. So I don't have a prototype, but I but I started thinking in how I would implement it in prism, and I just my head blows up immediately. 

**Danny**
* Gotcha. does anybody else want to echo? The discussion of complexity or push back or provide any more color here. 

**Gajinder**
* I think the consideration of this might also be taken in context with the other feature, heavy EIP, which is PDAs. So depending upon the PDAs or Macs be, we would want the inclusion of at least one of these things. 

**Danny**
* Got it. So there is there's a bunch of discussion just happening in the chat around. Small versus big fork. and what that means and what the intended timelines are. and how that couples with, the execution layer intentions. I do believe that the execution layer quote is angling towards small fork, with a 2024 target. knowing that timelines are hard to predict until you get into the meet. this also, given the feature set that we're discussing, looks almost certainly like a cross layer fork.
* And so the intention, unless we kind of open up a broader conversation, probably be try to couple complexity in a way that like, we're kind of hitting a similar intention in terms of when to ship, unless something in here emerges as like. You know, worth the complexity and worth the time in the discussion. So I that's just to kind of contextually frame this, but that doesn't mean that we can't debate that Potez. 

**Potez**
* Yeah. So we didn't start this meeting, trying to get an agreement on how to scope this fork. I don't really care about what, when it actually happens, but what is the scope that we're going to have and what's what are the dates that we have in mind? So I am under the assumption that in the previous meeting, there was some sort of loose agreement that we should scope it for the end of this year. If this changes and this is not a reality, then Prism would have a completely different fork in mind. If we had an agreement that we want to fork, we want to scope the fork for 2025, then we would be pushing for not only Max EV, but also inclusion list and Epb's in it.
* We would want to have a larger fork. But we're we're very, very conservative because we know that we haven't fought ever twice in a in a year, not in the CL. And I think it's it's not a, it's not realistic to try to put this many EIP if we're scoping for this year. 

**Danny**
* Got it, and I just. We can challenge that notion of scoping for the year. but I think that is the intention as of now, unless it becomes challenging me and we open up that conversation again. So I do think that's the correct framing as we move through this. Okay. So there's but no one is against a max EV type feature. To make it onto main net at some point. People generally agree on  the value here and the necessity here. There is disagreement as to the relative complexity, especially contextualized in how this next fork is being framed. 

**Speaker J**
* And I will also say that it's also a matter of balancing the complexity with the, expected outcome, because there has been also some debates about how this feature will be used at the end by big, big operators. So we got a very high complexity and not certain outcome on the benefits that has been designed here. So. There's also the. There is also an unknown behind the scene. 

**Danny**
* Right. And as as Mike said, there's been a lot of attempt to kind of proactively mitigate that and ensure that, something's being built that will be used. obviously, when push comes to shove, how people choose to run their businesses is not up to this group. and the timeline in which this kind of thing might be adopted is not up to this group. So there is there is uncertainty, although it's been attempted to be mitigated. would anyone like to continue the conversation on this, or would we? Is the preference to look at the next handful of EIPs?
* To wrap our heads a bit more around the fork, the complexity, the intention of the rest. and to come back to this in further discussion. Okay. That's what we're going to do. Next up EIP 7547 inclusion lists. Is this also you Mike. 

# EIP-7547 [40:00](https://youtu.be/_pFRJ1it608?t=2409)

**Mike**
* Yeah. 

**Danny**
* Cool. 

**Mike**
* This maybe a shorter kind of list of things, but. yeah. I guess starting with the kind of motivation here, Tony made this awesome dashboard called Censorship Picks. it shows the relative censorship for for different operators in the, in the block production pipeline. I guess the one that has changed recently, that is, kind of very relevant is the amount of builders that are censoring. So currently 67% of builder blocks are censored and about 95% of Ethereum blocks, 90 to 95% of Ethereum blocks are meta boost blocks generally.
* So, yeah, I guess a large chunk of of Ethereum's blocks are censored. so motivating the need for inclusion lists, I think is, just getting getting some kind of version of a forced transaction inclusion mechanism on chain to increase the censorship resistance and kind of make it more robust to these types of weak censorship, attacks. So, yeah, I guess in terms of complexity, I think this this EIP is much less complex than 7251. There is one kind of major design decision that I want to bring up, which is this kind of, unconditional vs conditional enforcement of the inclusion list.
*  This is a doc that is in draft. We're kind of just working out the details right now. There's been a lot of conversations over the past few days, but, yeah, so kind of making sure we have have the design of exactly what it, what it means to enforce the inclusion list is super important. But I guess generally the design, looks something like this. No free lunch version. and yeah, I guess this inclusion list stuff has been discussed for a long time, like Vitalik and, and Francesco have been talking about it since, I guess, 2021, 2022. 
* So kind of just taking a lot of this research and trying to to get it closer to, to fully ready to go on chain, I think is, is the general push, Shalloway has been shall we? Terrence and Potez have all kind of poked around at different parts of the inclusion list spec. I'll just send a link to the current pull request that that was opened six hours ago. yeah. I guess in terms of complexity on the EL side, there's there's not as much. because most of the validation happens when you check the enforcement of the inclusion list  as a precondition. Precondition of block validity.
* And also there's some amount of work that needs to be done on the peer to peer layer to make sure that like when a block is gossiped, there's a corresponding inclusion list, gossiped with it before you consider the block. for the head candidate. So yeah, there's there's a little less written on this, but I'm also compiling a related work document in this gist here. So happy to, happy to share that. And definitely, you know, this, I guess this is a relatively, newer EIP, but I think the ideas are very well established and, important for kind of one of the core properties of Ethereum is that censorship resistance.
* So would be super excited to kind of keep keep jamming on this and keep prioritizing this in the near tum. if that's, what there's appetite for. 

**Danny**
* Yeah. 

**Terence**
* Yeah I can give a quick like brief background on this. So this was essentially derived as part of the Epbs project with the EPF, sorry, Epbs project with the EPF last year. And as you guys have heard, that police and I have been working on Epbs spec for the last few months and the this inclusion, this, is basically part of it. So essentially, I mean, we think this is too small to be included in 2024, right? And then if and then if and then if it comes out to 2025, I think from our end we will push heavily for Epbs because this is part of Epbs already and which which, we will have more to share in the next coming month. 

**Mike**
* Yeah. Just just wanted to point out one tiny thing is that. You. You don't need epbs to do inclusion lists just to make sure everyone's on the same page. At some point I think we did think that was the case, but now we do feel confident that the design would work with or without Epbs. but yeah, I do think the. The relationship there, and the work you guys did with the EPF was super valuable. So thanks for that. 

**Danny**
* Other questions or comments. I have much less of a read on, how client teams are thinking about this right now. So some some verbal discussion around. Support or questions if you don't have a good understanding of this, would be great, Shawn. 

**Sean**
* So, yeah, this, seems cool. I'd want to do something like this. I would support something like this. it this one does strike me as pretty complicated, though. From what I was going through the ERP, it seems like, there are changes to sync, for example, and gossip and. This would probably require changes in the engine API and the beacon API. So it's like similarly touching a lot of parts of the client. to what it was like making the changes. on the other hand, though, we now have some experience with passing around data like blob data. so maybe it won't be as complicated, but. But yeah, generally struck me as like. Relatively heavy complexity, but is. 

**Lotuz**
* Yeah. Since, I have this design very fresh in my mind. And, I just want to confirm, with Sean. still, this is much smaller scope, at least in Prism's code base than maxdb. so it's much easier to implement for prism than maxdb. But, it's true. You require to have new sidecars, for the inclusion lists. Exactly like just the blobs you require to have new endpoints on the beacon. On the engine API so that you get an inclusion list from the El and you get, a new send the inclusion list to validate from to the El. The there are already PR some of the EPF fellows on some of the fellows that worked with us already, worked out the code, the list validation and the list production on Geth.
* So there's some some code already to be seen for EL on the other side. On the CL side, the heaviest core changes are around gossiping because you need to gossip these new objects and on for fork choice because you need to validate, this block this, this sidecars to to even say that this these blocks are valid, to even put them in purchase. 

**Sean**
* Okay, cool. Thank you. 

**Danny**
* Yeah. Anybody any other team want to kind of discuss how they're feeling in relation to EIP right now. 

**Gajinder**
* Yes. Speaking for Lodestar. we are basically, not I mean, we support the EIP, but we don't strongly feel about it because we feel that not all options have been exhausted. There is should override builder flag in the EL, and, using that, a lot of censorship can be dealt with if, this particular flag is actually implemented in the EL code base and is shaped and it does not require any consensus artwork. So, for Lodestar, that path is a bit preferable because, again, if we want to keep the scope of the force small, then we would basically, vote in favor of some feature EIP. then basically this one. 

**Danny**
* This is the general understanding of the should override builder as kind of a band aid that will help for a while? Or is there an understanding that that might be like a long terme viable solution? . 

**Potuz**
* I don't share the lodestar reading of this. this, an inclusion list is something that the Yale is, suggesting the proposer to to first include. it's it's kind of too strong to guess that the transactions, I mean, we are seeing 90% of blocks already, censored. So if says particular contracts have transactions that are outstanding, then we're going to be not taking any builder's block with this, flag instead of like, trying to choose builders that are non censoring. I think use overriding this overblowing this flag is just too much of a leap. 

**Gajinder**
* But we haven't even seen this flag in action, so we don't even know that. How how useful this flag is. 

**Potuz**
* Definitely. And we need to see what are the heuristics that are going to be implemented on the ELs. Hopefully this is going to be implemented soon because there are some simple heuristics and hopefully it's going to be against like strong censorships, but not something that would just disrupt the network by trying to override every single block or like because we currently have statistically 90% of blocks produced by, well, many blocks produced by censoring builders. 

**Gajinder**
* But if this flag is actually implemented, then it would achieve the same purpose that inclusion list would do in the sense that if. 

**Potuz**
* No, it can't because the proposer sends it before you get the block from the builder. So this flag does not allow you to see the block from the builder. With this flag, the the builder, the EL is going to signal there is already censorship censorship on the network. You should not even ask for the builders block in the next slot. You should not even consider the builders block on the next slot. This is because the way we have met boost we. You don't get to choose after you see the block.
* So this is very different than inclusion list where an inclusion list you're going to say to the builder, give me a block that has these transactions, and then you're going to filter out every sensory builder with this flag. You filter out every builder. 

**Gajinder**
* No. I understand that inclusion list is a stronger way to prevent censorship. but,  Yeah, I mean. Also note there could be a first step that can be taken to see whether we can have whether this flag can have effect and prevent censorship. 

**Danny**
* All right. And. I guess the consensus layer also gets to add their own heuristic in relation to that flag. you know, so 100% return value of it doesn't necessarily mean 100% usage of it. I know that's not necessarily the point here.  Does any consensus teams making the case for inclusion of 7547 in Electra? Given the, the knowns, the unknowns, and the kind of general intention of scoping of the work. That was asking anyone making the case any positive. Anybody wants to. Say yes, this is this should be included. This should be prioritized for this fork. All right, we're gonna set this aside for now. again, the conversation will continue.
* So it's not necessarily a death sentence, but this is not currently being prioritized or included. Potez. 

**Potuz**
* Just a quick note. again, the same. The same node as before. If this fork happens to change the scope for next year, this would be a very top priority for Prism. We believe this is strongly needed and we can do it in the next few months. We can have a proof of concept at least of this. 

# EIP-7549 [53:30](https://youtu.be/_pFRJ1it608?t=3210)
**Danny**
* Thank you. Okay. ERP 7549 move Committee index outside attestation Dapollon. 

**Dapploin**
* Hey. So this gap clears technical depth from the previous roadmap where we were going to execution charts. There is no reason now to sign over this bit of data signing over it. It means that we cannot. Aggregate equal votes in terms of FFG and LMD ghost. This has very significant implications, not to our own clients, but to any other application that tries to prove finality outside of the clients. For example, breaches that want to develop a zero knowledge prover they would immensely benefit from verifying, much less pairings. With this optimization, it can significantly accelerate the delivery of translation solutions for yeah, basically, bridging from consensus networks to other networks.
*  So it's not as important to ourselves to improve the efficiency as our clients, but to other consumers that want to prove consensus in some restrain, execution environment. 

**Danny**
* Is there a marginal difference in beacon block verification at layer one? Or is I mean. 

**Dapploin**
* Yeah, we would we would benefit. But we I think clients are already kind of optimal sized. There would be no like like a significant difference. Maybe CPU would go from 25% to 20%. But it's not a game changer. It is a game changer for these scenarios that I'm talking about. Like, these sorts of applications. 

**Danny**
* And from a complexity standpoint, this is a very minimal of the way you specified it. kind of leveraging a helper in phase zero. This ends up being a very minimal change. really changing just a couple of data structures. and ensuring that we kind of get the tests ripple through the tests that way. 

**Dapploin**
* Yeah. So there are different ways that we can deprecate the existing community index. the most basic one where we just keep everything as is and just set it to zero. It should be, really trivial change. we can go more crazy about it and scope creep the hell out of this. But if we keep it tiny, it should be really, really painless. 

**Dankrad**
* Yeah. I mean, I think like because the current draft mentions all three options. I think like for a small fork, only setting it to zero is realistic. I think like, realistically, given all the, all the infrastructure that has been built around signing things like, like protection and, this would validate us and so on. I think it's a major change to change the format of attestations, but if we set it to zero, then it can be a very small one. 

**Danny**
* Yeah, I echo that. All right. I believe we've seen, like, very positive sentiment from all client teams. and no dissent. Does anybody, want to bring up any reason not to include this in electron? And it probably goes without saying this is not cross-layer. Okay. as of now. We will include some five, four, nine. Oh, that's what's funny. The next EP 7594. is, pure does. I can give a quick overview on that. this so data availability sampling is in some form is the method to go from for, for four levels of scale where everyone's downloading all blobs to, extended scale beyond that.
* Call it folding sharding. by not having enabling nodes to be able to ensure that data is available without downloading all data. this has been very high R&D task. Um. For quite a while now. and almost all of the complexity, although a very elegant mathematical construction, ends up being in the networking layer and kind of the practical instantiation of doing this in a distributed context. here, Das here, data availability sampling, is a, an attempt to utilize known, very well tried and true known networking components.
* And to to get a kind of basic data availability sampling out the gate, utilizing discovering peers in a similar way that you discover peers for at nets, utilizing gossip and subnets and utilizing, a diversity of peers for sampling. It also does attempt to, leverage a notion of data availability sampling providers, by allowing peers to custody more than the honesty requirement. and let that known to peers such that if there are um funded or altruistic nodes or whatever that that want to serve the network, that can kind of naturally slot into this, this is something that has a specification. 
* This is something that, multiple people are working on prototypes of, but it's also, something that, you know, compared to seven, five, four, nine has quite a bit of complexity and quite a bit of things, to work through. That's not to say that it isn't. Everything that it utilizes is very well known. but putting the pieces together, um. Certainly on these networking things can be a challenge. Cool. Terrence. 

**Terence**
* I mostly have questions. So my first question is are we increasing the target and match count? If yes, then like I feel like maybe we probably should wait until our ERP 4844 for is to see if there's sufficient demand and if today we are not increasing the target count. Is this like a backwards compatible changes in a way that if we just apply, like the data sampling network on top of the current 4844, do we even need like a hard fork? I understand we probably need like an epoch such that the PS can pay attention to the subnets, but besides that is are there like consensus changes? 

**Danny**
* As it is specified right now, there are no consensus changes. Yes, you're right in that if you're going to leverage these new gossip topics and things, you would want to premise it upon an epoch. That is not to say that, pirates should not be coupled with a data gas limit, increase. I just personally think that that would likely look like a separate, very self-contained EIP that just looks like essentially a gas limit increase EIP, at which I guess in the event that people want to move forward with 7594, I would argue that it's the an open question as to whether, and to what value you would you would do that at an initial fork. 

**Dankrad**
* Yeah. So in terms of. Yes, what Tyron said about the demand, I think what is important, to realize is that, yeah. I mean, I don't think there will be a question about demand 4844 like right now, like we see roll ups are already using about. Next, but this has grown by a factor of ten over the last year. So the growth is said. 

**Danny**
* The data amount it grown. 

**Dankrad**
* Right. So the amount right now is on the order of one blob per block. and but this has, this has grown by a factor of ten over the last year. I'm going to share this graph in the chat, but it's Yeah, it's I think it's very important to realize that this will very quickly become an urgent thing. I think because we will run quickly into the regime where roll ups will also question, why are we using 4844 at all if it's not cheaper than, than call data? so yeah, like, I mean, I think like the demand is like the smallest worry I have about this. I think like that will be very obvious very quickly after for it 4844

**Danny**
* Other comments questions, how people are feeling about this. That one. 

**Tim**
* Yeah, I think. 

**Dapploin**
* Every every other ERP has merit, but scaling remains the best investment in terms of time and output. That is a very clear return on investment investing in this field. So it seems very unwise to not have this as the top priority, basically constant and. Still we delivered food and scharding provided with that. We do all the other good things on the back as it allows. 

**Pawan**
* One. Yeah, I was curious about the crypto side of things for this, but mainly like the efficiency of verification of large amount of, the greater amount of blobs here. Like, so what is the state of the cryptography libraries basically for us. 

**Danny**
* Is Justin Traglia or George here? Or maybe Dankard. If you have context. 

**Dankrad**
* Yeah, I will. I don't have the numbers in my head, I. So what you're asking about would not be the the blobs, because we wouldn't be verifying for blobs anymore. Instead, we would be verifying samples. And, I do not have the numbers in my head. I am pretty confident that it's not going to be a problem, but I will quickly look. I think Justin compiled something, and I will. Find those numbers. 

**Danny**
* And Justin has no Mike. But, can maybe provide a resource or, some quick data for us. if possible. And there's also the question of not only efficiency, but just the state of these libraries. and I know that there's been work done, but I can't make a claim as to what that work looks like in relation to production. 

**Dankrad**
* Yeah. I mean, I think like the complexity is not like enormous. So I'm fairly confident that, like, we will be able to finish all the work on the libraries Valentine. Like we already have a C implementation and I think we have every like everything we need to do that very quickly. 

**Danny**
* Is this more would you call it iterative or fundamental? in relation to what exists 4844

**Dankrad**
* I mean, there are some fundamentally new things. Yeah. I think like. Yeah. 

**Dankrad**
* Yeah it's it's very it's mostly very similar to what exists already. The one big piece that changes will be the computations of the samples which like which you don't have to do unless you produce blocks. so that will be on a slightly different. yeah. That, that will have not much higher complexity than like the other things we've done. But like the verification, all stays very simple and the additions are quite small I would say. 

**Potuz**
* Voters. Yeah, I'm going to sound like a broken record, but, yeah, I'm not worried about the cryptography nor all of these changes that are on software. That is, they're isolated changes. I mean, they can be worked in parallel from everything else, and they can be self tested and they can be unit tested and they can be self audited. we've we've learned something from the NAB is that, testing, networking changes, gossiping, new object change, testing, changes to gossip is complicated and it takes time. And we were under the assumption that we did. We were going to prioritize.
* This is what what led all of our decisions that we were going to prioritize vertical on 2025. By scoping this in 2024, I don't see how can we test this on vertical in parallel and ship something like this by this year? That's the reason why we were not supporting this for this year, for this small work, if we scope it for this year. 

**Danny**
* Let me clarify something you just said. you say you don't see how you can test this in Verkle? In parallel. I, in the event that this were not included in what is attempted to be scope this year, it seems like a very obvious thing to work on in parallel to Verkle, because it is. very independent. yeah. 

**Potuz**
* Definitely. But but but then we'll have, like a year, I understand, but then it will have the double the time to test this instead of just test this, vertically in parallel and ship this by this year. So we're going to have to, like, have this ready and be tested in a period of like the next five months, six months, probably max. 

**Sean**
* John. so my perspective sort of that Deneb actually helped us get a lot better at testing these types of changes. So I would. I would be more confident that we could test peer desk more quickly. Like I feel like the tooling has got better. DevOps has been putting in tons of work. yeah. 

**Danny**
* Yeah. Also say the like. Promising for fork choice, inclusion and things based upon, alternative network messages is was probably like a major hurdle.in Working on 4844, whereas this is leveraging the same logic. Obviously, it's can be very different in many ways. but maybe that also reduces the complexity, I would hope, and I do agree, Sean, we have gotten better and even, from here hope to get much better. Perry. 

**Pawan**
* Yeah. I want to mention two things. I think the first one is that, like a lot of people have said, we didn't have a lot of the testing tools we needed for effectively testing network upgrades. And I feel like now the gotten to a stage where we actually can do that quite reliably, and we've kind of been spending time testing, working in parallel already. And one thing we've learned is that most of the Verkle changes would benefit greatly from Shadow Fox. So we have a way to do Shadow Fox, but in an automated manner such that you don't actually need to call someone from DevOps to do them.
*  You can just run them in like a CI test. And I at least our working assumption is that if we can deliver that, over the next month or two, then most of the El teams can, in a siloed manner, test transmission at least, and they only need us at the point when we're talking about doing the transition with the network communications, which would most likely be later in the year, at which point we've gotten further ahead with PR does. So we're trying to, like, parallelize at least our time such that we're not blocking either party. 

**Danny**
* Yeah, I, even if it were not included, intended to be included for Electra, I would still make the case for spending quite a bit of cycles on it. in parallel, assuming that Electra was kind of a bread and butter fork with respect to, you know, very well scoped and understood consensus changes, I think that. Hopefully would, keep some resources available to to work pretty hard on this in parallel. and if that is the case. You could make an argument for sensitive inclusion and Electra as like a kind of the, parallel R&D track, but that does not hold up what would otherwise be a bread and butter fork in the event that we hit unknowns.
* Maybe that's a reasonable compromise. I don't know if we need to or will have the time. To make, fully make this call today. we have 20 minutes left. We have the sec of vacation, set of of EIPs. and we also will save you, six minutes at the end, for quick research. Update. Do we want to table this and think about where it may sit and if there are R&D compromises here. Or do we want to continue this conversation right now? Does anyone else have anything to add additionally to this conversation right now?
* Okay. I think that likely in plus two weeks, we'll kind of pick up the conversation around some of these more complex things and where we sit in relation to them in relation to Electra or potential future talks. this being one of them, Maxdb being the other obvious one. Okay. It's on, certification. 

**Etan**
* Hey, hey. So it's a couple different types EIPs, but they all have a shared motivation, namely that right now every application that builds on top of Ethereum use this json, RPC, API, and normally they have to use a trusted server for that because there are many responses in that API where there is no efficient way to verify that the response is correct. 
* For state balances, NFT ownerships, we have Ethe geth proof, and Verkle will make those proofs more compact. So there it's solved but there are three other trees, namely transactions, withdrawals and receipts, where additional changes are necessary to make it viable to use those, to create proofs that we can put into those Json RPC responses why is it important that there are proofs there right now?
* The big providers of Json RPC, such as Infura, they have privacy policies where they log your user data, they tie together, your EIP with all the wallets that you are accessing. So there is like a privacy concern there. And there is also a security concern because you're trusting a server for providing the correct response. So with those proofs, it becomes possible to verify that the response is correct.
* They can still censor you, but you can just ask the decentralized network of servers like they cannot, send incorrect data anymore. so one key, for transactions that is necessary to introduce is a commitment to the transaction ID right now, transactions have an ID, but it doesn't exist anywhere in the Merkle Patricia tree.
* So in in the blockchain the transaction ID doesn't exist. So any request by transaction ID such as obtaining its receipt or its transaction data, it takes an ID and you cannot even verify that that transaction actually exists on chain. 
* You have to download all the transactions and all the receipts to verify that the transaction actually is part of a block right now. It could be optimized a little more with a Verkle Patricia tree proof, but it's not efficient. that's also one thing that Proto Lambda brought up. 
* Just, a couple like maybe an hour ago in this EIP, for receipts that it's important for breaches, because the receipt can be multiple megabytes. So it can even be that, like, a fraud proof doesn't even fit into a transaction. So having a standardized way on how to localize, a receipt and a transaction would, would help with layer two as well. So, what is being added is this transaction route concept. So we can have Verkle proof that a particular transaction route is included on chain. And that would also help simplify the inclusion list, because it is no longer necessary to include the full transaction in every block multiple times. So we can just include the transaction route there.
* And it also includes the from address of who is signing the transaction right now that is also not on chain data. you actually need the full transaction right now and then hash it to obtain the signer from the signature and the transaction hash, which is quite an expensive operation for embedded devices. And it is also opening up, for example, EIP 8102, which proposes the TLS signature scheme, but without, from address commitment, it becomes impossible to efficiently, deploy such an EIP. So it fixes that. It adds the from address and the transaction route. for receipts we are adding the contract address. If someone is deploying a new contract right now that is also not part of on chain data. 
* So adding that there is important and also there is a slight change to the gas used right now in the receipt, there is a field called cumulative gas used. So if you want to know how much. This was used by a particular transaction to compute the correct gas usage. you need to download multiple receipts and then compute the difference to see how much an individual transaction actually used. so changing this to actual gas used by just a single transaction, simplifies that, that. Well, so you can download a single receipt.
* You know how much that transaction used by not including cumulative gas used anymore. It also opens up future parallelization in execution because you can now, process multiple transactions at the same time, as long as they do not touch the same storage slots and accounts. this cumulative gas used is the final, part that right now prevents that, I think. yeah. So those are the three different routes. There is also this signature scheme proposal. the three other rips, they could be implemented by simply converting all the existing transactions and receipts from new blocks onwards. So this this only applies to new blocks anyway.
* And we could, while building the block, convert the transactions from RLP to ZK to gain those advantages. In 6493. There is also a scheme to create transactions directly like this. So MetaMask could directly sign an SEC transaction, to avoid the conversion step. And SEC is also about 30% smaller than RLP when stored on disk because it uses a compressed format. it's called snappy. It's the same one as, as is used on consensus, because there are a lot of zero bytes in receipts especially. 
* It saves a lot of data as well. pushing out the 4444 a little bit more, like giving it more time. It's still an important EIP. And yeah, the final EIP is 7495. It essentially defines how we want to represent transactions, receipts, withdrawals. it is a format that is forward compatible, to avoid a situation like we have right now in consensus layer. The problem there is, for example, rocket pool. They query the beacon state and to see whether a validator is slashed. And right now, every time that the number of fields, reaches a new power of two in the beacon state or in the execution payload, that proof format changes.
* So they have to, update all of their, proof edification logic to consume the new, formats. with 7495, this is no longer necessary because any proof, will continue to work, even if future. Additions or removals. like. Yeah, change the actual data. So if you just care about slashing, as long as slashings are a concept, you can write a verifier right now. I mean, after 7495 is deployed and it will continue to work until slashings are no longer a thing conceptually, regardless of other changes. yeah. But it's different. Like we can choose to use a different approach. Of course, if we say that it's fine for clients to have to update the code continuously. yes. what is. 

**Danny**
* This shifting.  To a stable container? Change the virtualization at a once it changes once. 

**Etan**
* Yeah, yeah. So any container that is touched changes it once. I have proposed to just do it for where it's necessary for transactions and receipts, but it could also be done for other structures, of course. one thing to keep in mind is that 7495 also introduces a way to represent optional values. So right now in the Verkle consensus specs, there is an optional value. I'm not sure if the final design will still include it, but if we are going with a Verkle design that uses optionals, we should decide how we want to represent optionals. So at least the 7495 must be decided before Verkle, and the transactions encoding needs to be decided before inclusion lists.
* Those are the two dependencies. Yeah. I have also created a demo where you can explore how a transaction looks. after this EIP for example, here I just picked a random one and put it in the chat. The first link is the transaction SSZ. The second link is the. Receipt sack. And if you want to look it into RLP, you just delete the SSZ part from the link. If someone wants to explore it, it's. It works. 

**Danny**
* We're almost all of this. The high complexity component ends up being on the execution layer, whereas, it's more of kind of bookkeeping on the consensus layer. It's up to potentially, use using stable containers. You know, if you stable container the whole beacon state or something, that might be a reasonably higher complexity change. 

**Etan**
* Yes. And of course, the transaction representation in CL and El, it would be aligned to be the same. So right now the CL and DL use a different transaction container. 

**Danny**
* And do we before we move on to questions? was this brought up on the executioner call? And is there any, signaling over there that we should know about before we begin this discussion? 

**Etan**
* I didn't bring it up, for a while now. I just joined this one because I saw Electra being discussed. but, yeah, SSZ proposals are there for a while now. 

**Danny**
* Gotcha. we are going to shift gears in about a minute. Guillaume, let's do the question. And then, the SSZ vacation, we can continue in subsequent call. Cool. 

**Guillaume**
* Yeah. not really a question. Just, a remark. So, yeah, the Verkle spec could change. That's not a problem. Especially if we don't, guarantee that proofs will be available right at the first Verkle fork. They might be activated later. So, yeah, there's no there's no dependency there. Just what I wanted to specify. 

**Danny**
* Got it. given that a lot of the complexity of this does lie on the execution layer, I do think that we should punch a bit to, getting some more signal from them. and we can, depending on how that goes, we can put this on the agenda for the next time on the call. And also, even if that doesn't go well and people have questions and further comments from the other side, we can also discuss in plus two weeks. I do want to. Okay.
* So in two weeks, we are going to bring up discussion of, Maxdb and again, in terms of complexity, in terms of priorities, in terms of, fork or not, in terms of even if not fork, how to think about them as, as R&D items to help accomplish our goals over time. in plus two weeks, and for the last five minutes, we do have some time for kind of an R&D update slash discussion, or at least the beginnings of such, Ansgar and Anders. 

**Ansgar**
* Yeah. So basically, I just wanted to briefly flag a topic that could potentially contribute, like one more candidate, electron EIP. and that's kind of the stake staking reward. and mechanism. So supposedly the way to think about it is that, the original kind of staking reward curve was, was chosen to kind of pragmatically to, to kind of get the beacon chain off the ground. And then we haven't really looked at it in in much detail since. And then of course, by now we have, a lot of experience looking at the real world kind of usage of the for the beacon chain and for staking and, a lot of interesting mechanisms like LSTMs.
* And now, of course, staking and popping up, which are great to see. But of course, kind of were hard to predict. So, over the last few months, kind of on the research side, we've started  to, to look a bit more,  into that, mechanism again. Of course, the idea is to, to kind of make sure we, we have, we have a situation in place where Ethereum is just long time stable and needs no further changes. I don't think it's certain necessarily, to us that that we do need changes from, from, from currently. But but basically, the idea is to, to, to project forward. what what if we basically don't touch this, the staking mechanism, where will we be in in 12 months, 18 months, 24 months, right. Like three, 4 or 5 years from now?
* So basically what path are we on? what properties does that have and do we like that? What alternatives could there be or these this, this kind of exploration. but we basically, in terms of communication of, of our thoughts we'll have have some kind of articles and writeups out on that, in over the next couple of weeks. and then, a decision that we might want to make is around, are we comfortable with the path we are on if we at least kind of not sure we're comfortable with that. There could be a small ERP we might want to to to get into lecture to basically just calm down the, the robots a little bit, to basically slow down any potential kind of future and staking ratio kind of creep up and that, that that could happen.
* That would also, by the way, alleviate a little bit of the of the constant pressure on total total validator and  count. but again, this is all kind of I mean,  no, we're at the end of the call. So this is not the idea is not to have a discussion. Now it's just to, to flag the topic and say that kind of by the next call, we'll have  some kind of material out and then we can kind of start to have that conversation and. Yeah, and that's all for now. I think. and this was basically the first one that already has has a writeup out that he published yesterday. So unless you maybe very briefly want to to say what, what you've looked at. 

**Anders**
* Yeah. So you say that, yeah. I posted yesterday evening on Eth research and I just write a link here. And so basically what I'm looking at is sort of what can be done to the  level and what happens to various important features such as consensus incentives and reward variability for settled status if we are to change the issuance level. And so the conclusion is essentially that if we wish to temper issuance, we would like to do it with a rather moderate approach. So because if you do it too aggressively, we would sort of unbalance the different economic forces we have, you know, MeV and issuance.
* And this could then render the micro incentives of the consensus mechanism a little bit, you know, ineffective, because if we push down, we push down rewards so much that the stake is only received map, then there's a lot of sort of bad things that happens under the equilibrium. And so then I used to review sort of what can be done and what cannot be done in terms of different reward curves that that could be explored. And I showed some Vitalik does quite a nice summary also of this in a comment on that post. So you could read that if you want some sort of quick overview. 

**Danny**
* Great. so do check out the post. I think the intention is to, there's some subsequent, posts and research to come out, and, the conversation will be furthered at plus two weeks or plus four weeks time. but this is just kind of setting the stage that there is, intended to be a conversation around some of these forces. yeah. Any single one question we have time for. Yeah. Okay. take a look at the post. hopefully be some other stuff between now and a couple weeks from now. and, towards the latter component of, the next call, we can dig a bit deeper into some of the research concepts and potential things to do.  Thank you. That was a really productive call. we got through a lot more than I expected. talk to you all on the executioner.
* Call in a week, and then we'll pick up this conversation in two weeks. 


---- 


### Attendees
* Danny
* Tim
* Arnetheduck
* Marek
* Lance
* Micah
* Paul Hauner
* Ben Edgington
* Loin Dapplion
* Terence
* Enrico Del Fante
* Pooja Ranjan
* Hsiao-Wei Wang
* Saulius Grigaitis 
* Roberto B
* Olegjakushkin
* Chris Hager
* Stokes
* Dankrad Feist
* Caspar Schwarz
* Seananderson
* Andrew
* Crypdough.eth
* Zahary
* Matt Nelson
* George Avsetsin
* James HE
* Marius
* Ansgar Dietrichs
* Lightclient
* Stefan Bratanov
* Afri 
* Ahmad Bitar
* Lightclient
* Nishant
* Gabi
* Pari
* Jimmy Chen
* Gajinder
* Ruben
* Mikhail
* Zahary
* Daniel Lehrner
* Andrew
* Daniel Lehrner
* Fredrik
* Kasey Kirkham
* Protolambda
* Cayman Nava
* Stefan Bratanov
* Ziad Ghali
* Barnabas Busa
* Potuz
* Trent
* Jesse Pollak
* Carlbeek
