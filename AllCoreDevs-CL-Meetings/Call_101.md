# Consensus Layer Call 101

### Meeting Date/Time: Thursday 2022/12/1 at 14:00 UTC
### Meeting Duration: 1.5 hour  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/702) 
### [Audio/Video of the meeting](https://youtu.be/Z-0z5-7hGvo) 
### Moderator: Danny Ryan
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
101.1  |**pre-interop testnets update:** Withdrawal devnet 2 was released yesterday. A couple of bad blocks (possibly EthereumJS), but otherwise everything looks good. A larger, public version will be available next week. The first withdrawal shadow fork - forked Sepolia - went well earlier today, but only with a small subset of clients. In a few weeks, we hope to shadow fork mainnet.|
101.2  |**CL/EL TX and withdrawals commitment to better support light clients:** Alex Stokes will spec the Gwei change by Monday so that it can be discussed at ACD next week. There does not appear to be sufficient consensus today on changing withdrawal commitments to SSZ, but it would be good if someone could specify it - I believe Alex also volunteered for this.
101.3  |**Fork version gossip boundary issues Use Capella fork version for BLSToExecution consensus-specs#3176:** Potuz to create PR describing Prysm’s approach. A full spec release candidate due mid/late tomorrow.
101.4  |**Engine API:Engine API: unify failure mode for mismatched structure versions execution-apis#337:** This has been merged into the spec.
101.5  |**Engine API:Engine API: a bunch of cleanups execution-apis#338: Informational:** This has been merged into the spec.
101.6  |**Engine API: define payload bodies requests execution-apis#352**: Danny suggests we Merge it into Shaghai spec. Will remove it later if any issues occur.
101.7  |**4844: d-star name Consensus-layer Call 101 #702 (comment):** No objections. Decision The next CL fork after Capella will be Deneb.
101.8  |**Research, spec, etc: Add block/state multiproof request/subscription feature (WIP) beacon-APIs#267:**  Access to Merkle proofs about the consensus layer, preferably the execution payload header, is required. Nonetheless, a general-purpose API would be extremely useful.
101.9  |**Research, spec, etc: Add /eth/v0/beacon/light_client/instant_update beacon-APIs#270:** Less complicated. Allows for faster access to information about the chain's leader by delivering light client committee aggregates as soon as possible.
101.10 |**Open Discussion/Closing Remark: Shanghai/Capella Community Call #1 #708:** Next Friday at 1500 UTC. Q&A about withdrawals etc. Can post questions on the agenda in advance.

-------

## Intro [0.20](https://youtu.be/Z-0z5-7hGvo?t=33)
**Danny**
* Welcome to Consensus-layer Call 101. This is issue 702 on the PM repo. A lot of minor Capella discussion points. Some, status update, name discussion for 4844, and then some, lightclient end points for the Beacon API to discuss.
* I just before we get into technical discussion, as we approach interop in a couple of weeks, what's our Capella testnet status update? Harry or Barnabas? 

**Pari**
* Hey, yeah, so we had, withdrawal net tool launched yesterday. There's a couple of bad blocks that need to be figured out, but I think they're mainly from T M Gs, but otherwise we seem to be doing good. we're testing withdrawals, et cetera, and everything looks okay so far. 
* We're gonna be launching a bigger, more public version of today's devnet next week, and the idea is that general public can also start getting involved trying out withdrawal tooling and hopefully we have some documentation and some deposit guides, etc, up there in time. 
* And another testing update is that we got the first withdrawal shadow fork working earlier today. So I was able to shadow for Sepolia into a mini, withdrawal test net. 
* Everything looks stable and good so far. thank you for AG and Mario for some debug support there. I still have to try it with all the clients, so I just tried it in a small amount so that I could test the tooling. Tooling seems to be good. So now I'll try something a bit bigger. So we should be good for a main night shadow fork in a couple of weeks. I think that's all the test net updates we have. 

**Marius**
* So quickly going over the, issues on, on devnet two today. I started sending some transactions, like handwritten transactions that should trigger stuff on Shanghai. And, there were two bad blocks created by, Ethereum JS One contained a transaction with, that that triggered like the warm Coinbase and the other one, the other block contained transaction that had, a huge amount of internet data, in IT code.
* And, so yeah, if JS should look into that. another thing that I wanted to talk about is on the fog monitor. Be so on the fog monitor, we have these, these bad blocks. right. we like some of the notes collect bad blocks and we can display them on the fog monitor. what's really interesting to me is that there are four bad blocks seen by, BISO notes that are not seen by any other notes. 
* And so it would be really interesting for, really important for the Biso team to look into why they see those, those bad plots, that no one else, saw. And apparently I have no idea they are not part of the economical chain. and so, that's why we don't have a a consensus issue there. 
* So they might be reed out, beforehand, but, yeah, it would be good to investigate from the Visa team and then the Ethereum js team is, already working on, on the stuff. yeah. Thank you. 

**Danny**
* Thank you Marius. Any questions for Perry or Marius? Okay, great, thank you. I know there's been some discussion about this both on the CL layer call two weeks ago on, all core devs last week and on the chat. essentially the way that the commitments routes work across the consensus layer and the execution layer for both transactions and now withdrawals, do not allow for simple support of, the consensus layer, like client kind of inserting a block or block header into an execution layer without additional information, without downloading essentially the header, to get that information.
* So I'm not caught up on where people wanna land on this compromise. I do, you know, I, one making the withdrawals commitment and SSC commitment on the execution layer is one thing. I do think that it would be quite hasty to change the transactions commitment, given that tooling and or smart contracts might be relying on that and we don't have a good handle on what we would be breaking. 
* But that's my take without having dug deep into the conversation. does anybody else want to provide information or where kind of the, the decision point seems to be standing at this point? 

**Terence**
* I think an overview view from Chris side, although we client, maybe we don't have much pay this, but like I think our general consensus is just like, if this delay will draw, then our will be a no just like I don't feel like we don't feel like it's right. 
* Just keep adding future towards the end, which like delays withdraw and that's just our point of view. 

**Danny**
* Gotcha. does anybody else wanna weigh in? I mean obviously there can be to resolve this in a, for in general the work can either be, changing the consensus structures to include the execution layer commitments or to change the execution layer commitments to be that of the native consensus layer commitments, or some combination of those. 
* I did catch when that there was some eagerness to change the withdrawals commitment to SSZ. Does anybody else have a status update or read on that? I'm sorry. There's some hands up please if your hands up go. 

**Andrew**
* Yeah. So, on behalf of Aragon, we I agree Danny, that we shouldn't, tackle transactional route in in this release, but I think for withdrawal route we should switch to this exactly the same route, as NCL. 
* So that probably entails, switching Gwei and also to, SSZ commitment instead of RPL plus, Merkel. 
* So that makes sense to my mind. And in Argon we've already started working on, some CL code. We have, light client CL embedded into Aragon. So, and we have some SSZ code, that code. So for us it should be relatively easy code wise. 

**Danny**
* Got it. Mark? 

**Marek Moraczynski**
* I think it's generally a bit too late for changing the coding, cuz we are passing all hi test. Now we have working data net. Basically all or almost all the pairs of clients are working fine and with those are much anticipated feature by community. 
* I don't think that technical debt that will, will introduce is worth delay withdrawal and about we, we have, SSZ library developed by us, but the main risk for us is,  it wasn't battle tested. On the contrary, other libraries are used by CL clients. it was developed a few years ago and we, we just started touching it again. 
* I think like moving to SS Z in 4844, give us time to verify, this library correctly and check with existing test and give us better confidence about the code. 

**Danny**
* Got it. Thank you. And Matt? 

**Matt Nelson**
* Yeah, so from the basic side, you know, we we're weekly in favor in terms of kind of delaying, in terms of putting the SSE and coding in. 
* We, we feel like we can have it ready for the iop. We, again, weekly in favor of being forward-looking and reducing kind of the tech data around this for this short term because, you known we're not sure that we won't be making the changes again anyway in Cancun. 
* So focusing on the withdrawal route to reduce that kind of, the need to support that weird piece of history between the two forks kind of what we're, we're looking at on our side. you know, we're not, again to echo the other point, we're not thrilled that it's kind of the week before interrupt that we have and invalidation of the, all the prior testing and a lot of this other stuff.
* But we're not too concerned about a, what we see as a small delay, but we're only weekly in favor of adding the SSE encoding for the withdrawal route, to match. 

**Danny**
* Got it. Do we have a specification that works here? Because it's not only way, but it's also, I apologize, has anyone actually kind of like gone through the specification work or worked through what this looks like in terms of the encoding? 
* Just copying Micah, you sound very far away. I believe it was you speaking, you have your hand up, 

**Mikhail Kalinin**
* It's just a copy of the ECL spec, right? Nothing special. 

**Danny**
* Correct. I mean it's using, using the SSC encoding. 

**Mikhail Kalinin**
* I just, yeah, I just wanna pay attention to one detail. If we are considering switching EL to great and we are not doing it action high, but trying to do it later, then it might be more difficult to do because everyone will represent them as everyone will read those amounts as ways and yeah, that's gonna be a bigger change then, of now, Well, and there's two, I mean everyone, but 

**Danny**
* One is to encode the withdrawals as and the other is to encode just the representation of the withdrawals in the commitment as way and I don't know if there's consensus on which to do there. 
* One requires more changes than the consensus layer to send it in that way. 

**Mikhail Kalinin**
* Yeah. Having any, different representation of withdrawal just for commitment purpose sounds like really dirty, but I dunno, Right. Can't say that it's really bad or Yeah. 

**Potuz**
* Sure. I just wanted to point out that this is not really an implementation issue. it may sound that it's easy and it's exactly, but there're design decisions to make, like you, you just mentioned this issue of like, like having weight or weight at different layers. 
* This involves salts on the CL side, whether or not we are going to change the encoding because we change from way to, to wade to send it and Indianness descended and this going be, have to be changed. 
* So depending on which design decision you have, then you're gonna have changes on both sides or only on the EL side. And this has to be tested. 
* I believe that this, if we switch to thinking of this as a design problem, not as an implementation problem, this should be taken out of Shanghai because we're not at a stage, we're, we're designing the fourth, we're implementing the portal already. 

**Danny**
* Right. And I am, I'm sympathetic to that. Given the different edge cases and things you can think through here, I'm not convinced that we have kind of a end to end sound design. Andrew, your, your hands still up? 

**Andrew Ashikhmin**
* Yeah, I think, actually think that, we should at least switch to wayI because, then, as noted, the other way around, if we say, okay, it's it's way in Shanghai, then switching the other way around is hecker. Cause the, then, we, I guess, so there, there will be tools that we will expect, withdrawals to be in wayI and switching them  is as, as a nightmare. 
* So I would at at least if we don't, go, if we don't do, SSE, I would at least switch to, Gwei. it's a very, simple change, technically is the only complexity synchronization across, like tests, tests and CL and EL and so on. So it's true that it requires changes both on CL and EL and in the, to the engine api. 
* But it's a trivial change and it ensures that we in Shanghai, we both on both sides here CL and EL we have a encoding of withdrawal in goerli. 

**Danny**
* Mark. 

**Mark Moraacz**
* I'm okay with switching to Gwei. For us, the main risk that we see is s e z encoding. So makes, that makes sense. 

**Danny**
* Is the Indianness in the way the encodings work here a problem? Like would it need to Gwei and little Indian to actually be relevant? 

**Andrew Ashikhmin**
* We should keep, I think we should into, in the engine api, we should keep the, the encoding what is, required for, what, what is the case for other fields like base fee? I think it's, it is big engine in, in in json, isn't it? In, in the engine api. I don't think we should change that. 

**Etan (Nimbus)**
* Yes. engine API is JSON, so it's an SK string and the only thing that would change is before, sending with trials to the engine api, the CL would no longer have to multiply by that billion for the amount. 

**Danny**
* But on the, on how things actually land in the block header, it would be In the block header. 

**Etan (Nimbus)**
* It's just a commitment like, Sorry,  in the block, it would be RLP with the current spec. So it's a big Indian on the EL, like nothing there would change, it's just the amounts that would be larger. 

**arnethduck**
* I would push back a little bit against the fact that this is design work. If we go with only with withdrawals, because the withdrawals are already well defined in the, on the CL side, and we're just replicating that in the, EL. 
* So,either way this goes anyway, on the Nibus side we do have a branch that implements the necessary changes if anybody wants to look at the size of that diff and on the CL side, it's really small. 

**Micah Zoltu**
* Micah, I'm gonna say the same thing I always say, which is that I think we should be prioritizing the long-term health of the ecosystem and clients over the short-term gratification of users today. 
* I think that we should be thinking about do we want to deal with the tech debt of having this weird transitionary phase for the next five years versus just telling people to wait two months for the withdrawals.I really don't think we should be prioritizing,you know,rushing anything Mihail. 

**Mikhail Kalinin**
* I just wanted to say that probably we can try to do something about it during the interrupt, and if we're satisfied by the result, we can make, like by the result of design and phase and by the result of implementing, investing this, particular piece, we can, you know, make the change to this spec after that once accommodations already, like having this like a stretched ball or interrupt just as an idea. 

**Danny**
* Right. Given the multiple design points here and given what seems to be a lack of consensus, I have a trouble synthesizing this into something reasonable to move forward from the call today. 
* Unless I'm reading this incorrectly and everyone's on board with something and I am not parsing that, I think you're correct. 

**Potuz**
* I think perhaps to advance we can probably agree on something on whether or not we want to have SSZ in the future or at some point and try to commit to that, and then we can decide when this happens, Right. 

**Andrew Ashikhmin**
* I would still advocate, switching to Gwei because if we don't do it now, then later it'll be a much harder change. It's,  like right now it's a technic it's a trivial change, technically but later because, some tools will be with Shanghai with the, with the release, some tools will be enshrined, heading way instead of way and it'll be a nightmare to switch. 
* So I advocate doing that bit material technically. Now, Does that only touch the engine api, the engine API and the execution layer? So in the, in the EL how I see it there, there will be only two places when we actually, add withdrawals to the beneficiary. We have to multiply it by 10 to the ninth. and also, in, peer to peer when we serialize withdrawals. 
* I would also, when we exchange blocks, I would also have withdrawal amounts in Gwei. So maybe a couple, just a couple of trivial changes. So actually for if we keep the amounts Gwei, then the peer-to-peer will be an o change and only one, one line of code. When we add the amount to the balance. 

**Danny**
* Is anyone willing to handle the specification proposal for Gwei change so that it can be discussed starting next week and into the execution layer call on Thursday? 

**stokes**
* Yeah, I can do that. 

**Danny**
* Okay. If we can have that on Monday so that we can begin discussing it and talk about it on Thursday, I think that's a reasonable compromise given the status here. 
* If anyone wants to do the full specification of switching everything to SSZ so that we also have that up for discussion, and in a like end to end bound well designed way, I think that's also probably worthwhile if anybody wants to take that on at the moment. 

**Micah Zoltu**
* Is anyone against the Gwei way change?  I think it sounded like most people were in favor of that one at least, Right? 

**Tim Beiko**
* But there's no specs. I think Yeah, assuming people are roughly in favor. If Alex can have a spec by, next Thursday's call, we can yeah, agree to an actual spec and ideally debate it.
* You know, if we have the spect next week that we come on the call, everybody's reviewed it on the same page and, and agree to that. yeah. 

**Danny**
* Yeah, I've definitely, if we can have it Monday or Tuesday, if that would much help the conversation. I'm not following the chat very closely. is there anything that people wanna surface from there? 

**Etan (Nimbus)**
* Just, is it a separate spec or is this part of 4895? Like the withdrawal EIP? 

**Danny**
* I think this will be a diff 4895. And any other relevant components like the engine API and to bundle, you know, a couple of PRs, or discussion. 

**Etan (Nimbus)**
* Okay. So it's this spec change to Gwei way and antenna a separate one to change, withdrawals commitment, transactions commitment and to receive commitment to SSZ. Right. 

**Danny**
* I do not believe that, we're in a good spot to even discuss changing the transactions commitment, given that we don't know what it would break. so I think this is more, are we gonna do the extended spec would be changing the withdrawals. there's also, this is gonna have to touch in the engine api and as someone said.
* I believe the networking a spec. Okay. So both are with Alex then, I guess? Yep. Okay, cool and Alex, I'm very happy to, discuss interview as you're working on this. Great. Okay, thank you. any, any final comments on this? Thank you.it's good. Good discussion. 

## Fork version gossip boundary issues Use Capella fork version for BLSToExecution consensus-specs#3176 [23.51](https://youtu.be/Z-0z5-7hGvo?t=1431)

**Danny**
* There is an open PR 3176 on the consensus specs repo from mikhail. This is I believe, round two or three. And, a proposal on how to handle a gossip edge case for BLS execution changes around the EPOCH boundary. 
* I think it's relatively minimal change, I'd a UX improvement for Stakers. and I wanted to get people's read on whether we're willing to get this in there and mikhail, if you wanna give us a quick, tltr on it. 

**Mikhail Kalinin**
* Yeah, basically the idea is, using Capella work, version for, before Capella, and yeah, and, fall back, to the normal logic after Capella fork. 
* The Capella Fork, ebook is, taken according to the system clock, to the local system clock. And yeah, so that prevents through messages from being rejected. yeah, if they're sent, on the gossip subtopic that is not related to Capella, so it's, it kind of like stock cap, Right? 

**Potuz**
* So Prism already implements this. if you send us, a change, we will put it in our pool before Capella hits, but we are struggling to see when we are going to broadcast these changes. there's a race against hackers, I guess some people are pushing to, to, to try to broadcast these messages early, and it's not really clear to me what is the right, point to broadcast. 
* I would've guessed that is at the port, but then this hits the problem that other nodes might not have their head stake or their wall clock at the fork. So what I want is a commitment from clients that we will not broadcast before the port perhaps, or I don't know any scheme would work. I just don't want to be penalized if we broadcast and work too early. 

**Danny**
* Right. Do you assess this change as simple enough and meeting your requirements? 

**Potuz**
* We, so what, what, what Misha is proposing, we already implemented it, and it's fine for us that this, this was the most natural choice for us. what is still up to, it's up to discussion and I haven't heard from other clients is whether or not, we're gonna be penalized or anyone is gonna be penalized peers if they receive these messages before Capella hits. 
* We are not penalizing those messages, we're just ignoring them before the court. 

**Seananderson**
* I don't know what we have in Lighthouse, but, I can bring it back to the team and make sure that we don't penalize if these messages are sent early

**Terence**
* I wonder if it's better to include this special behavior in the stack itself and then with certain time involved Just so that we're clear

**Danny**
* Because, oh, does this, this PR if I understand correctly, allows for the broadcast at any time before Capella? As long as the fork versions are Correct? 

**Potuz**
* Right. So the, the issue is more on the that than on the p2p. This PR as far as I understand it is the way we validate them when you, your local node you send to your local node, changes to be included in the pool. So that's one thing that users would want to do to have this, these changes in their pool before the fork. 
* And then there's these other component, which is the P2P network.I suspect that the easiest for all of us to do would be to just ignore any message that come over the wire until the fork and then at the fork broadcast all of our pool and start taking messages. I think this is the easiest for implement to us. I suspect that it would be the same for every client that I don't know. 

**Danny**
* So on this PR if system clock epoch below Capella call epoch, it'd just be a simple ignore, Right? 

**Potuz**
* So. Right, right. 

**Danny**
* Okay. I believe there's consensus to put something minimal in to the gospel conditions to handle this appropriately. Do you want to make a PR that represents the logic that y'all already have? If we think that that logic's sufficient, that would require less Changes? 

**Potuz**
* I can take care of it. I'll, most broadly what I'll do is just either have it reviewing it or having him writing it, but yeah, I can take care of it tomorrow. 

**Danny**
* Okay. and we're trying to get an additional candidate out, I guess it's looking like mid to late tomorrow at this point. so we'll try to get that in there. and I'll circulate that amongst teams. 

**Mikhail kalinin**
* Mikhail, Yeah, there is also a suggestion by a salway, which might also make sounds, to always use Genesis work version for, this message type to verify signature. So it'll be just unconditional thing. it probably, which is probably less back from, if it's also easy to implement, of course,

**Danny**
* I'm less inclined to go that way. You know, if the network forks and there are two representations of reality, this would not allow you to do key management in a different way across those forks. it's not a huge sticking point for me, but, that's at least the, the logic essentially you would forego replay protection on this message. 

**Hsiao-Wei Wang**
* And also I think it would be helpful when we are entering the future folks, like, when we are passing from Capella to EIP4444. People for fall, then the old, operations in the pool, they might have to be like clear or something else, and then the user added the four boundary. They might have to send another message.

**Danny**
* They do Work Yeah.Across one four boundary, correct? 

**Hsiao-Wei Wang**
* Yeah, I mean the new, if we use Genesis Folk version, because right now they have to use the new folk version. 

**Potuz**
* I mean, yeah, No, they don't, they don't work across, across  than now. And, yeah, so the, the what Hsiao are suggesting is, is actually what we implemented. We're just gonna wipe out the pool completely at the it's not going to be a problem in futures because there's not going to be many changes in future forks. 

**Danny**
* I see. Okay. I'm inclined to just change the networking spec at this point rather than to change the consensus back around the fourth version of this message. are there, is there any strong opinion against that? 

**arnetheduck**
* Okay. will we, sorry, a question. Will we run into the same issue where a message created, you know, to forks back might be useful, 

**Potuz**
* But if you create the message to forks back, it depends on how you sign it, right? I said, so you wanna submit a BLS change sign it now, but you wanna submit it to courts in, in the future? 

**arnetheduck**
* Yeah. I, I'm asking if that's a use case, right? 

**Potuz**
* No so I think what we're suggesting is now only for the Capella. So it's, it can only happen right now, bellatrix to Capella. I mean, it will never happen again. 
* This special behavior, so just to be clear again, so if you sign a message with Capella and you submit this message at the next fork the same, the sharpen fork, then it will be invalid. 

**Hsiao-Wei Wang**
* Sorry, thats the new proposal 

**Potuz**
* So that is the current status, and we are su we are proposing to maintain that status for the next fors. 
* The only for that is very important is because we're gonna have hundreds of thousands of changes is people signing in Bellatrix and submitting a Capella. 

**Hsiao-Wei Wang**
* No I mean, but in the EIP 4444, then you folk then you have to use Gwei folk version to sign a message, Correct? 

**Potuz**
* Correct. And, and this is the current status. So it's fine. The current status says if you're past the fork of Capella, then you have to use the current fork, and if you're before Capella, then you can use Capella. 

**arnetheduck**
* Yeah. But somebody was suggesting that we would simply sign with the Genesis fork always. 

**Potuz**
* Oh yeah. This is a suggestion of Hsiao  I'm not against that. 

**arnetheduck**
* I don't know if there's consensus Because if we do, then we don't have this problem and people can sign their messages now and store them in some, some place and then send them in whenever they want. I don't know if that's a use case, but Right. 

**Danny**
* And the main issue that we run into is replay protection in the event that there is some sort of chain split. 

**Hsiao-Wei Wang**
* And I agree, yeah, I mean the, you just using Genesis fork version will reduce some UX problem. for example, the, if we want to sign a message offline and we don't have to choose which ephoc which folk version to use. 

**Danny**
* Right. And I find that, I find that compelling. 

**Potuz**
* Yeah, I think it's, it's a minor change to us to move from Capella to generic to Genesis support version. So it's fine for us. 

**Gajinder**
* I'm sorry, I didn't get, why shouldn't the default version be Capella? Because it starts at Capella.I mean, we can always sign for the, with the feature fork,I don't understand what is the opposition to that, because that seems to me the better solution than I think it's because it gets rid of the edge case and it ensures offline signing. 

**Danny**
* UX can be simple and, you know, the tool that you installed two years ago would still work rather than having to bring in extra information about the current network. 

**Hsiao-Wei Wang**
* Also like, I think it depends on how the CL clients to, manage their preset and can fix, like if we are at, Bellatrix, do they have top for or not? because if it is in the, the price bake, then when you are at Bellatrix, we don't have any concrete accessible, if we don't do some tricks, if we want to access the Capella corporation, it's just a little bit more how to manage.But, so using Genesis could be easier.

**Gajinder**
* But the tools should, anyway, have some mainnet conflict baked in them, right? 

**Danny**
* Yeah. I mean, not they should, they could, but also when you're talking about offline cold setup,you don't necessarily want to update them frequently. so you might have some sort of stale config that if it was just Genesis, it would still work fine. 

**Gajinder**
* So then Genesis, signed version will and post Capella, then it'll be normal flow. That's what we are talking about. 

**Danny**
* I missed that. Can you repeat yourself? 

**Gajinder**
* I'm asking that the genesis sign, withdrawal will be valid till and on Capella and post Capella, for example, on charting, it needs to be signed fresh, right? 

**Danny**
* No, the intention would be essentially by signing Genesis, version. It works for all forks. 

**Hsiao-Wei Wang**
* It is just like the how we de handle the deposit operations, Right? 

**Danny**
* There's a bit less of an issue on like, again, the only thing that is an issue here is repay protection, but I don't know if repay protection is that valuable. The deposits, you know, get native kind of replay production because they come from an execution layer that has a transaction that has that. 

**protolambda**
* Can I add that it's not just works like deposits. Deposits can be signed offline and then can, there can be like these like trustless validator schemes built around them where something that science will al always be valid. 
* And if a withdrawal is restricted to a single fork, they cannot really pre-sign withdrawals for ventilators anymore. And then you have to resign and you have to basically stay connected to the, to whatever service you might be using. If you're if you're trying to agree on like Withdrawns, right? 

**Danny**
* That's will Be the alternative is to just use the execution address from the start, if that's your scheme that you're using today. But I'm slightly in favor of using Genesis work version. 
* If no one's opposed, I think that it does simplify the UX quite a bit and is very minimal and gets rid of our, networking issues. 

**Gajinder**
* So would, would the, others, folks signed versions would be, would be coming invalid, for example, Capella sign or they would still be valid? 

**Danny**
* They must be in that scheme. They must be Genesis fork version. 

**Ben Edgington**
* Just to clarify the scope of this, we're talking about the BLS credentials change message, right? Not, yes. not voluntary withdrawals, which then become a bit of an anomaly cuz they are not signed Correct. 
* With Genesis. Right. But for the scope of this conversation, we're just talking about the, BLS ls change. 

**Danny**
* Yes. Shall we, can you open a PR with the suggested change? 

**Hsiao-Wei Wang**
* Yes, of course.Thank you.And, by the way, we might have a standard release tomorrow or, and, we can try to make it included to use. How do you guys feel about, making it ready pre ready? 

**Danny**
* I mean at this point I hope that we're only making extremely minor changes and that we get them in as soon as possible. So whether that be a release tomorrow or if we need a delay till Monday, that'd be my preference to get in whatever we putting on, getting in. 
* Okay. Good. Okay. Mikhail, you have a number of engine api, prs that you put into the agenda. Couple of them are now merged. Can you give us tdlr? 

## Engine API [41.41](https://youtu.be/Z-0z5-7hGvo?t=2501)
## Engine API: unify failure mode for mismatched structure versions execution-apis#337

**Mikhail Kalinin**
* Yeah, sure. So let's go where, what has been merged into the spec already? the first one is unification of failure moded, when the structure version, is not compatible with, the actual structure content. So this PR is here. so basically, yeah, the before the merge of this PR this spec, like, had a discrepancy on how to handle this kind of situation. 
* For instance, for a new payload B2, if you pass withdrawals, say before, Shanghai, so withdrawals are new before Shanghai. in this case or vice versa, withdrawals are filled. yeah, withdrawals are new after Shanghai is enabled in this case, the invalid, payload status, had to be returned, which is abuse an inva status in the first place. 
* And yeah, the discrepancy here was with fork choice updated version,two where we had, to return the error when payload attributes are filled with withdrawals when  they don't mean to be filled with them. 
* So this PR unifies, this kind of stuff. And if the structure version doesn't match the what is expected according to, activated features, this PR particularly uses timestamp to denote this, to denote for cultivation as, yeah, this is applicable to EL side and uses timestamps. 
* And, in both, in all cases. And I think it should be like a practice for future upgrades as well. the error should be returned, as specified. the PR, so what does it mean actually,
* Currently, new payload V2 and, fork choice updated v2, they supportv1 ,v2 versions of respective structures and in the future we might, deprecate, new payload one at all and use, new payload v2 for example, for to pass, ion high and push high blocks into it and so forth. 
* So that's about it. So, the change to EL clients and to CL is, I guess is about this switching from invalid to the, error from  status in case of new pay. So take a look at this one. 

## Engine API: a bunch of cleanups execution-apis#338 [44.41](https://youtu.be/Z-0z5-7hGvo?t=2681)

* The other the next PE what was it about? let me check. Yeah, so a bunch of cleanups, it introduces some cleanups, which are, saying that, the, terminal preferred block conditions may not be verified anymore. 
* So it's just like a recommendation, an option.if clients want to, they may just remove this logic. and one of the things here is that invalid block hash status is deprecated and now invalid, just invalid status should be used instead. And this is like a must. 
* So EL clients must switch from invalid bulk hast, in new two to two invalid status. So that's like a substantial thing from these cleanups want to take care about. Okay. Questions so far or comments on what has been merged?

## Engine API: define payload bodies requests execution-apis#352 [45:50](https://youtu.be/Z-0z5-7hGvo?t=2749)
* Okay, so the other thing that we have decided to try out, to put into Shanghai scope are, these payroll  body's requests. I have just stolen the PR and rebased, filled it with, rebased, with, Shanghai and, yeah, did some refinements as well. 
* So the spec is here. and I was just going to ask, EL client developers about the status of this and, how do they see, can we do this as part of Shanghai or not, can EL clients, like, provide this functionality and implement this as it is specified? So basically it's two methods. yep. Go ahead. 

**Marek Moraczynski**
* It's about Geth payload bodies, right? And Geth payloads by range. 

**Mikhail Kalinin**
* Yeah, yeah, exactly. Two methods Geth payloads by hash by range. 

**Marek Moraczynski**
* We Already Implemented it or EL elicited, so if CL clients want to experiment with it, they can use Nethermind. 

**Danny**
* Cool Marius,

**Andrew Ashikhmin**
* In Argon, we have not implemented it yet, but it should be relatively easy to implement. So we can to do it before Shanghai.

**Justin Florentine**
* Besu - Doesn't seem too challenging. first time we're taking a look at it. 

**Danny**
* Okay. So I suggest we merge it, but also experiment and test with it over the next handful of weeks. And if we're running into issues or we can't get conformance across the board, then we'll kind of move it into an experimental place and make it a more mandatory Shanghai update. Sound reasonable. 

**Potuz**
* Oh, I'm sorry. I raised earlier.  I I want to bring back something, Can you call me in a bit? 

**Danny**
* Yep. 

**Mikhail Kalinin**
* So, we are merging this PR into dimension and if any issues we are moving it to experimental. Am I understanding correctly? 

**Danny**
* That's my understanding. 

**Mikhail Kalinin**
* Okay. Okay, great. 

**Danny**
* Thank you Michael. Potuz. 

**Potuz**
* Thanks. so if we, we go with a Gwei version, which is fine by me, like using Genesis version. I don't think, I don't see anything wrong, but, it would be good to to specify when we're broadcasting the messages, because we know that we're gonna see hack versions of people, well, we expect to see hack versions of clients broadcasting as early as possible, their changes. perhaps we could agree on just ignoring anything that comes before the Capella fork.

**Danny**
* Right? So that would look like a conditional in the gossip spec that said, if before simply ignore, right. I'm not opposed, I'm also not convinced, you know, you don't know who's the person acting really fast, the hacker or the user yeah, there, there's no, there's no easy way about this. 

**Potuz**
* It's just I don't really know what's the right, the right thing that I should implement.  if we are going to accept messages early, then I think I should be implementing that. As soon as we subscribe, then we send those messages. 

**Danny**
* Great. I guess the only name we can do here is have an even playing field, cuz we don't know if the hacker or the user is gonna be racing first. So I guess your suggestion does at least make the playing field even so shall I let, let's consider also putting that, conditional and ignore. 

**Mikhail Kalinin**
* Yeah, just small, small question related to it. if you ignore, will you receive them again? the same message? 

**Potuz**
* I mean, Yeah, so it includes some sort of like, perhaps a DOS. I don't, I'm not an expert on p2p, but yes, so if you ignore, you'll get them again and then you'll just put them in your EL pool. 

**terence**
* So just have like a hasg that you, you can see the same message, you just dropped the message even though it's Not this, but only we do have this, but only after we included in the pool. 

**Potuz**
* So if we're ignoring that, that will never hit the hash. 

**Danny**
* Okay. We'll get something like this into the PR and circulate it peer review. 

## 4844 [51.36](https://youtu.be/Z-0z5-7hGvo?t=3096)

* Okay. 4844. I was curious as we kind of lead into interop in a couple weeks, just quick status updates in terms of like passing tests. 
* I know we have some issues with the tests that are gonna roll out soon. but just where do clients stand in terms of limitation of the must updated specs? 

**seananderson**
* So for Lighthouse, we're passing the latest spec test apart from the one test that I think is bugged. so we're there with the implementation, but we haven't really tested the latest spec in like a local test net or intraop Ital. So working on that next, in the next week and a half. 

**terence**
* For Prism, it's very similar White House that we are passing the current spec test, which, but then there's new one coming, so that shouldn't be that hard to pass. 
* And then, we're working on some end-to-end tests basically. It's critical cool that we have, we're using multi blocking block utility that enables us to submit a block and I sync Beacon and then download the block, from the Sync Beacon node. So we're playing around with that.But yeah, I think we're fully ready for the I and, we're also very excited.

**Justin Florentine**
* Saw and ASU has a number of pieces implemented, but we still haven't really started full integration of them all. I personally could use some help, if we could maybe get, doc or maybe update the EIP for 4844, site that has the consolidated list of all the potential testing resources that are available that would help me orient the team and get that stuff delegated out. 
* So, if that already exists, just point me to it please. And if it doesn't, can Anyone own that Specifically sliced To look the resources? I'm sorry, proto. Say again? 

**Protolambda**
* I'll put together a list of the resources we have. 

**Justin Florentine**
* Okay. Thank you. 

**Protolambda**
* Thank you. 

**arnetheduck**
* Pero I think Nibua is in a similar spot. We have test passing and pieces, bits and pieces implemented. They need to be put together.
* I'm guessing we have quite a bit of UX work as well to do in terms of Yeah, there are all these little questions left to answer, which I hope we'll have time during the interrupt decide like how long blocks are stored how big they should be, whether they should be coupled or not and things like this. Like all the engineering stuff I think I feel is still a bit shaky. 

**Enrico Del fante (tbenr)**
* We are, implementing, study implementing the state launch and the block production flows are in a good shape. 
* Yesterday we did our first block production in our Interrupt global interrupts and yeah, we are still progressing. We have reference test enable, we have to double check if they're all enabled or not at the moment but we are passing definitely some of those, if not Paul, progress. 

**Danny**
* Got it. And help me understand, are we what we call these implementations on the path to what we hope to be production or, or these quick and dirty proof of concepts, that are gonna need extensive overhaul post interrupt 

**Enrico Del fante (tbenr)**
* For us we always do the clean in the master branch.So everything is, production ready in terms of quality. Definitely something to be, left out in terms of optimization, cacheing in years there, but it's, the general approach for us is still always, be less quick and dirty as possible. 

**seananderson**
* Yeah ours is also like a production implementation, but it's still gonna take us some time to like fully productionize it like a month, two months, I don't know. 

**Danny**
* Yeah. Yeah. I don't mean whether it is production quality today, but that it's on that path and that we're not working on proof of concepts. Thank you. 

**Gajinder**
* On our main branch, we really get as things move along

**Danny**
* Okay. Yeah. So am I correcting generally across the board? That's true. 

**arnetheduck**
* I mean, we have pieces that work, but I think there's a lot of user experience stuff left, like, you know, the database retention, like how do you do pruning correctly, right? 

**Danny**
* Understood. 

**arnetheduck**
* For a good user experience for the rest api

## d-star name Consensus-layer Call 101 #702 [57.52](https://youtu.be/Z-0z5-7hGvo?t=3472)
**Danny**
* Okay, cool. Thank you for the updates. we will have for, for call again next week and continue to chat about this as we approach interrupt Shawe D star name. Hey. 

**Hsiao-Wei Wang**
* So last time we had some discussion about what we need for the  next hot work in the CL and so one popular, candidate is  devnet if I pronounce this correctly. 
* And so I saw some positive, vibe about people want to use Devnet n and I just want to make sure that most people are happy with this, this choice.
* And we can move on and rename to this and break some links, but we will be happier after the big renaming. Yep. And any suggestions, feedback, objections on it? 

**Danny**
* I think it's probably time. I have no opposition, So it's, thank you. 

**Hsiao-Wei Wang**
* And so I think we can we can start with big renaming.


## Research, spec, etc [59.58](https://youtu.be/Z-0z5-7hGvo?t=3598)
**Danny**
* Sounds good. Okay. Moving on. We have a couple of PRs, the Beacon APIs open up, by Zelt. Can you give us an update here and anything that we need to agree upon to get these things moving forward? 

**Zsolt Felfoldi**
* Yeah. Hey everyone. So, yeah, these, these two open PRs, I have are, well, the, they're basically extensions of the, light client Beacon API and, yeah, for some context, yeah, I'm, I have a, like an almost finished, version of the new, light client, protocol version for Go Ethereum. So yeah, we don't have a working light client, right? 
* And now since the merge unfortunately, I, but, yeah I have a very, like current use case for these things because, but I think, they are generally valuable.so like if we have this idea that, it should be possible to, implement a light client through this,rest APIs, and I think it's generally a nice thing because there could always be like use cases that can make use of it. 
* And, like I would also need this right now and this would be very valuable. And yeah, so one of these end points, 
* Is about, the Beacon State and so currently the beacon, the light client API provides a lot of nice stuff and, and it's possible to light sync the consensus like we can sync up to the latest, beacon header and that's nice, but if, we want to prove something from the execution layer with that, then we also need some Merkel proofs. well at least through the execution block route maybe also other stuff from the bigger state can also be useful. 
* So since I want a fully functional like client, which, also can prove other blocks I also use this historical state route and whatever. So the point is that, right now it's only, I think it's only still only Lone Star that has a Beacon State endpoint. And, we discussed this a lot both with Cayman from North Star and also with other people that, exact API would not be really be practical, to, expect other, cl clients to implement because they have like different, in memory representations of the big state. Not everyone has like the last, 64, states available. 
* And, so in, so, so, instead I specified, a new API that, I think it's, close to being implemented in a low star that, only, like defines like, so it doesn't, doesn't expect, cl clients to keep all the beacon states. So it allows either requesting stuff from like the current head, whatever it is or, it has this subscribe method, which is basically just a hint to the client that, okay, I might be interested, in a this parts of the state and the near future. And as you process this box, please remember it for a little while so I can request it later. 
* So yeah, I there's the reasoning and explanation in that PR. So I don't want to go into very much detail and I believe it's, reasonably should be reasonably simple to implement. And it's, reasonably general purpose. There's a very nice, compact format for defining the,  subset of, of the Beacon state that, and the shape of this marker, multi proof that, we wanna re request. 
* So I think, this could be like a nice general purpose, beacon State, a API endpoint that, I think EL client should be able to implement. 
* And, yeah, there's also another, that's even less complex, PR about likethis instant updates, PR, which is, so now, now we have, finalized and optimistic updates in the Light Client api. And the optimistic update is they, basically the previous slot saw the slot before the head slot because that of the sync committee signatures for each, slot are included in the next, beacon block body. So, that these design.Slide. Client signatures are always available with one slot of delay. And that means that, any light client can only, have access to like, to the head with a full slot of delay. And these, instant update endpoint would allow, like, quicker access to the latest heads because,there are these partial aggregates in the available in the network.And, that's, pretty easy to, collect them and, and, and aggregate them on demand. 
* And that would only be like, I don't know, four seconds of delay instead of 12.
* Yeah so this is like just a minor optimization, and maybe less critical than the first one because like having access to the beacon state, I believe that should be part of the, beacon API at least once we have, like endpoints for beacon light syncing and everything. 
* And, yeah. And I know that, right now, people are mostly like concerned about the upcoming fork and everything, but these pro these are usually, this processes take time. So I just wanted to bring this up and yeah, I, it would be nice if, like to get more feedback on these and then move distinct forward. So yeah, basically that's it. 

**Danny**
* Any questions  in result? Okay. Etan

**Etan (Nimbus)**
* Oh, sorry. I, it's just if you could already, get unblocked with the popular use case by just having access to execution payload header, that one will be part of the, like there is a PR 3151 to extend the current Light client and data format with the execution payload header as well. 
* And it'll also get go into the rest, stuff. But it's less generic than what you described. So,but still maybe that one already helps you a bit to get unblocked. 

**Zsolt Felfoldi**
* Well I mean, so right now, if we are talking about like, so for Geth for the current get lifeline design, well that, uses multiple fields.And, so right now, I'm working with Low Star mostly.And, is also like working on these specs.
* and, so I think until others implement it, I will pro Geth will probably the Geth like client will probably use luster and more exactly the full nodes who are serving the Geth lightclients, those will probably use lost nodes because while it's provides full functionality, 
* we already have the code and everything. So I guess for now we will go with that and yeah, but still, I totally agree that for many simpler use cases, what, you said and what we yeah, this is what we talked about at the conference also, like in. So this is useful just having the execution payload headers and for some use cases, this is all you need. 
* And it's really nice to have a, this a simple API and, but I believe this general purpose API is also, not super complicated. And I think it's just, yeah, it feels like it's missing from the API. I, so we have everything as accessible through this and just not this, so like, not the Beacon State.And I think I also heard, I think Cayman also said to me, one RO means was that they have some use case for accessing the Beacon block bodies too. So maybe, maybe we can, we could also implement the same thing for the, beacon Rock bodies. I don't really need that right now, but I'm just saying that there's also possibility. But, yeah, I so this is why I am proposing this.

## Open Discussion/Closing Remark 1:10:37 https://youtu.be/Z-0z5-7hGvo?t=4236

**Danny**
* Okay. beacon API maintainers of client teams, please, take a look at these. maybe we can get them unblocked and some discussions in person, if not asynchronously, between now and then any other questions or comments on this one? Okay, great.And then the Shanghai/Capella Community Call, Tim? 

**Tim Beiko**
* Yes. so next Friday at 1500 utc, we're gonna have a first community call for Capella. basically these are useful for, developers, infrastructure providers, wallets and whatnot to come and ask questions about the upgrade. * I realized that, you know, we're still a bit early in kind of the Capella cycle, like we're not on test nets yet and whatnot, but I think it's good to just have a first call where, people can come with questions and can answer that about, you know, how withdrawals work, what they should be mindful of as this is happening, you know, not, a lot of people will be traveling, during that time, but if you're not, and you want to come on, people always appreciate it when client developers or researchers can answer questions directly. 
* Otherwise, Danny and you will be there, to answer people's questions.if you're listening to this and want to join the call, the information is on GitHub, and you can pose your questions in advance there. yeah, that's pretty much it. 

**Danny**
* Thank you, Tim. Any questions for Tim? Okay, any other discussion points for today's call, Ruben? 

**Ruben**
* Yeah, just wanted to ask what the conclusion for Withdrawal  regarding this SSZ adoption on the EL site? I don't see we come up to any consensus. 

**Danny**
* Alex Stokes is going to work on a simple proposal, that has way as the unit of account within withdrawals across the engine api, the, EIP and the networking spec, for discussion. And we will discuss it again on All core dev next week. and then I believe, we will also although I'm not a hundred percent sure who owns this one, we'll work on actually changing an additional proposal to change the commitment, to SSE, although it seemed like there was much less consensus on that path. 
* But again, both of these I things I think will come up in the call in one week time, but right now we don't really have end-to-end reasonable designs for the things that people want to see. So that is the next step. 

**Ruben**
* Thank you. 

**Danny**
* Okay. Anything else for today? Okay, cool. Thank you. I appreciate it. Talk to you all very soon. 

**Potuz**
* Byebye guys. Cheer. Bye. Bye. 


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



## Next meeting on
Thursday, 26 January 2023, 15:00 UTC

