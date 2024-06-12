# Execution Layer Meeting #187
### Meeting Date/Time: May 9, 2024, 14:00-15:30 UTC
### Meeting Duration: 1hour 30 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1029)
### [Video of the meeting](https://youtu.be/yYfzpSme7Cg)
### Moderator: Tim
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 187.1 | **Pectra Devnet-0 Updates** EF Developer Operations Engineer Barnabas Busa said that his team is in the process of testing client configurations for the first Pectra developer-focused test network and will aim to have a stable configuration for the launch of Pecra Devnet 0 by Monday, May 13. Based on the Pectra Devnet 0 readiness tracker, the Geth, Nethermind, and EthereumJS client teams have fully implemented Pectra code specifications.
| 187.2 | **Pectra Devnet-0 Updates** Besu developer Justine Florentine said that all Pectra EIPs have been implemented for Besu but his team is still working on debugging the code. Erigon developer Andrew Ashikhmin said his team has started work on all EIPs except EIP 7002, EL triggerable withdrawals. The Reth team posted a link to their implementation tracker in the Zoom chat, which indicates that their work on EIP 7002 like the Erigon team is also pending.
| 187.3 | **Pectra Devnet-0 Updates** CL clients side, Grandine developer Saulius Grigaitis said all EIPs have been implemented but his team is running into bugs when running the client alongside an EL client. A representative from the Lighthouse team said they are close to having a full implementation ready for Pectra Devnet 0 and noted that specifications in the Engine API need updating. Teku developer Mikhail Kalinin said that he is working to get these updates added to the Engine API specifications.
| 187.4 | **EIP-3074 Updates** EIP 3074 in Pectra specifications for Devnet 0, there has been discussion about an alternative EIP to replace it, EIP 7702. Geth developer “Lightclient” summarized the latest breakout meeting for EIP 3074 in which participants discussed what changes related to improving the programmability of user-controlled accounts should be prioritized in the Pectra upgrade. According to Lightclient, all participants agreed that full native account abstraction is a few years away from being ready to implement on Ethereum. However, there was division on whether this meant prioritizing changes to the functionality of externally owned accounts (EOAs) or the migration of EOAs to smart contract wallets. A day prior to this ACD call, on May 8, co-founder of Ethereum Vitalik Buterin proposed a new EIP, EIP 7702, that would enable a new transaction type on Ethereum to support EOAs functioning like a smart contract wallet for the duration of a single transaction. Lightclient said that sentiment among participants from the EIP 3074 break out call was generally positive about EIP 7702. However, he added later that there are important details about EIP 7702 that still need to be worked out. For example, details on how to revoke EIP 7702 transactions and how to scale the gas costs for these types of transactions remain unclear.
| 187.5 | **EIP-3074 Updates** EIP 7702 is accepted into the Pectra upgrade, the idea would be to replace EIP 3074 with this one as EIP 7702 accomplishes similar outcomes as EIP 3074 but with the benefits of not creating new opcodes on Ethereum and improving the ease of static analysis on new EOA behaviors. EF Researcher Ansgar Dietrichs recommended in the Zoom chat considering EIP 7702 for inclusion in Pectra and waiting roughly 2 to 4 weeks before making a formal decision on replacing EIP 3074 with 7702. It was clear from the discussion among developers on the call about EIP 7702 that further work needed to be done on the proposal before it could be considered ready for implementation by client teams. Nethermind developer Ahmad Mazen Bitar noted that the work already done for EIP 3074 would not likely be reusable for implementing 7702. Beiko confirmed that developers should still move forward with an implementation of EIP 3074 for Devnet 0 and re-discuss specifications for Devnet-1 later.
| 187.6 | **EIP-7685, SSZ, and EIP-6110** Nimbus developer Etan Kissling about EIP 7685, general purpose EL requests. In a GitHub comment under this week’s call agenda, Kissling asked whether the proposed design for general purpose EL requests was needed and if the opportunity could be better used to switch to SSZ, a serialization format that developers have been meaning to update on the EL since the Merge upgrade. Most EL client teams on the call were supportive of keeping EIP 7685 in Pectra and if any blockers emerge from the inclusion of the EIP on operations like a client’s optimistic sync to then revisit the design.
| 187.7 | **EIP-7685, SSZ, and EIP-6110** SSZ, Kissling explained that the new design format for general purpose EL requests is based on the legacy serialization format, MPT and RLP, and thus will have to be updated when developers make the transition to SSZ. He noted that delaying the move to SSZ only creates more work for developers if they continue to create new MPT/RLP data structures. However, there was not a strong voice of support from EL client teams for including EIP 7495, the SSZ stable container, in Pectra. A developer by the name of “Dustin” wrote in the Zoom chat that the decision to delay the SSZ transition was “crazy” and that the issue of poorly working SSZ libraries for the EL was “a serious issue.”
| 187.8 | **EOF Updates** Independent Ethereum protocol developer Danno Ferrin and EF Solidity Research Lead Alex Beregszaszi shared updates on implementation work for EOF. As background, EOF is a bundle of code changes improving the Ethereum Virtual Machine (EVM) that is being considered by developers for inclusion in the Pectra upgrade. The Meta EIP for EOF has been finalized. Developers have also simplified the transaction creation process in EOF, and progress is being made on client implementations for EOF.
| 187.9 | **EIP-7623 Updates** William Morris” presented concerns about the gas cost changes to calldata storage in EIP 7623. He explained that the changes would allow some users to transact at reduced rates by combining their transactions and thereby encourage the creation of secondary market for gas discounts that Layer-2 rollups (L2s) and other participants may use for transacting more cheaply on the network. He recommended an alternative EIP, EIP 7703, that increases calldata costs at a flat rate to address these issues.
| 187.10 | **New Alternative to EIP 7609** “Charles C” presented a new EIP to prevent reentrancy attacks in smart contracts. Charles said that the proposal which creates two new opcodes to protect smart contracts was an alternative to an earlier proposal that he submitted, EIP 7609, decrease base cost of TLOAD/TSTORE, for Pectra. Charles said that he was not sure why EIP 7609 was not considered for inclusion in Pectra and is still sourcing feedback from developers about a way to prevent reentracy in a cost-effective way. He noted that the current solutions like OpenZeppelin’s Reentrancy Guard and TLOAD/TSTORE opcodes are too expensive for decentralized application developers to use by default. Beiko recommended that developers offer Charles feedback on these the new EIP on Ethereum Magicians.

**Tim**
# Intro
* Okay. Take two. Now we are live with audio from me as well. I'm welcome to ACDE number 187. basically the only thing on the agenda today is stuff related, to Pectra. we'll talk about,  devnet. Zero progress from teams. Then there was a breakout around EIP 3074 and the broader account abstraction roadmap that happened earlier this week that will cover, continuing the conversation from last call. After that, Ethan had a bunch of comments around, basically the messaging around, EIP 6110 and the generalized message bus we introduced recently.
* So we'll go into that and then, yeah, a couple more, EIPS to discuss if we have time. I guess first, Devnet zero. I don't know, Barnabas or Perry. are either of you on the call? 

# devnet-0 updates [3:35](https://youtu.be/yYfzpSme7Cg?t=215)
**Barnabas**
* Yeah. I'm around. so we are preparing some configuration files in kurtosis and trying to test them. we still had some hotfixes coming in this morning, and, probably we can be fully up and running by Monday with like a somewhat stable ish configuration. But we were missing some config files from the near-term, change spec, but that should be fixed now. And we made a new, Genesis generator image. So we are testing that right now. 

**Tim**
* Awesome. and last I checked, I believe every single client team obviously has has their work in progress. It seems like Geth and Ethereum JS are the two clients with everything implemented. anyone on the client teams want to share updates or concerns? Oh Nethermind has everything implemented as well. It seems nice. 

**Justin Florentine**
* Besu has everything in flight at the moment. They're all being tested and about to be merged. So I would say that we're development complete, but they're still being debugged and need to be merged into main. Got it. 

**Tim**
* And the other team have updates. 

**Andrew**
* Yeah. In Aragon we have, most of the things, as work in progress, except for 7002. yeah. So it's still maybe a week or two away. 

**Tim**
* Got it. Yeah. And then. Yeah. Wrath still also working on it and shared the tracker in the chat. And. I guess. Yeah. On the CL side, scanning the dev net zero spec, it looks like everyone is still in various stages of in progress, but any CL have everything implemented. 

**Saulius**
* So Grandini thinks, that, that it has, everything. And we started to to do interrup, I think yesterday. yeah. And, well, none of, of, else that we tested works. So we tested. NEtermind. Ethereum JS. And, Geth . And guess so. We were not able to. To essentially we are not able to finalize. So and in this quarter I reported a few issues and we keep working on that with some EL teams. 

**Tim**
* Got it. Thanks. Any other CL teams have updates or have everything implemented. 

**Sean**
* So on Lighthouse, we don't have everything yet, but everything's, pretty close. We're hoping to pull it together tomorrow. One thing we ran into was, I think the Geth payload bodies endpoint and the execution engine APIs needs an update. And I don't think that's specked out yet. I'm not sure if ELs have made changes there, but. Yeah, we ran into that yesterday. 

**Tim**
* Anyone on the EL side. Look up that call. Yeah. Marek. 

**Marek**
* What changes do you mean in Geth payload, adding deposits and withdraw requests or something else? 

**Sean**
* Yeah, just those two. 

**Marek**
* Yeah. So we added them on our side. so I'm not sure if Barnabas finished the kurtosis config. We can try. 

**Tim**
* Okay. 

**Sean**
* Yeah. We just didn't see changes in the spec, but we haven't tested against any yet. 

**Marek**
* So I think in the spec it is mentioned in execution payload and Geth payload returns execution payload. And in this way it was mentioned. 

**Sean**
* Okay. Awesome. Thanks. 

**Tim**
* And Mikhail said in the chat that, they're updating, Geth blog bodies in the spec, which should be done soon. Any other comments questions concerns from the CL side? Okay. and then, yeah. I don't know if I'm the on the testing team on the EL any updates there? I know last week, we had all the tests ready except 3074. Is that still the state we're in? 

**Mario Vega**
* Hey. Yes. we still have. We do have a PR for 274 tests, but it's not, filled yet.  I'll try to get an update in the coming days, but so far yesterday the tests were updated to include more tests for 2925. . 

**Tim**
* Got it. Thank you. Anything else on Devnet zero before we move on. Okay. next up, so we had an AA breakout at, sort of continue the conversation around 3074 and potential other EIP earlier this week. I don't know, light client. I believe you were on you maybe want to start with a quick recap and then we can we can take it from there. 

# EIP-3074 / AA Breakout updates [9:55](https://youtu.be/yYfzpSme7Cg?t=595)

**Lightclient**
* Yeah, I can try and take a stab at it. I know a lot of people on this call were on the call Tuesday, so feel free to jump in after and add some things I might have missed. Basically, the call was separated into two two parts. The first part I wanted to try and have a conversation with all of the relevant parties about what are we building towards? What are what do we think is a realistic timeline for what we're building towards? And given that, like how, what should we be prioritizing on L1 right now? And I don't think that we walked away with a perfect picture for every single party.
* But I think one thing that we did agree on is native accounts. Abstraction on L1 is still a few years away, and so there's definitely a reason to do something on L1 in the next hard fork if we can come up with something. And we talked a little bit about what those things could be, should we be focusing on improving EOS? Should we be focusing on trying to let EOS migrate to smart contract wallets? And there was some proponents for both sides. It felt like the louder side was the side to just improve EOS today, because there are some things that we still need to think about and figure out how to resolve with respect to actually migrating EOS.
* And part of this might be due to this proposal that Vitalik had had published just a bit before the call, and so people were very excited about improving the OS. So that was the main thing we wanted to like get a picture from all the different sides. Where are we trying to go? And it felt like we came away from the call and people were okay with improving EOS if it made sense in the longer term roadmap. 
* And then we went to the next part of the call, which was supposed to be really focused on talking about 3074 and some answering some of the questions that had been bubbling up about 3074 over the past few weeks. But we ended up mostly talking about a new proposal, 7702, which I think Vitalik will talk more about on this call. But basically it's a different proposal for how to improve EOS. And overall, it seems like there's a lot of nice benefits of it over 3074. It fits into the 4337 account abstraction world very cleanly. And, you know, for me most importantly, it lets us reason about.
* How it lets us reason about more statically, about what types of accounts might be drained in the transaction pool. So I think that that was like a big question mark with 3074 that we had to answer during deep net zero.
* So we talked about 7702 generally felt positive on that.
* And afterwards we talked about some more generic questions about the authorization of 3074 or 7702 from the perspective of the user, like, should the user be signing a message with the nonce, should they be signing with a chain ID or just some like arguments that we had had in the past few months? But with now with many more participants who have actually been developing smart contracts, that would work under the three 3074, 7702 world. And I don't think that we necessarily made too much progress there. It's just an ongoing discussion. but yeah, I think, yeah, that's pretty much the recap.
* If anyone else has something that I might have missed, I think we came out of the call pretty happy with the direction with 7702, but I think we should have open that discussion up here at some point. 

**Tim**
* I guess. Yeah. Before we go. Oh, yeah, I gave Vitalik. You want to cover 7702? 

**Vitalik**
* Yeah, yeah. so the the basic idea behind 7702 is that it's an EIPs that, basically allows a trans and EO owner to assign over a piece of code. And if that piece of code and that signature gets included in a new transaction type, then the EOU basically turns into a smart contract that has that piece of code for the duration of that transaction.
* And the reason why this is interesting is because it satisfies, a lot of, use cases in a way that's very similar to how 3074 satisfies them in the sense that, you have some outer transaction which could be called by the owner themselves, or it could just be called by some other actor, like a pastor or a sponsor, and then it does some other, it calls into the user account, it does some authorization logic, and then it does some execution logic.
* And the users, like the EOU gets activated and it starts doing things, from the inside of the transaction. And so there's a very natural way to convert any, 3074 workflow into a 7702 workflow. The big benefits that it has are that it removes the the need to introduce new opcodes. So instead of doing an auth and post call, you basically just do a call into the account. It's as like I mentioned, it's very, static analysis friendly because the accounts that are affected just get, statically declared in the transaction and it's, very forward compatible with, not just for 337, but also potentially.
* Yeah. any kind of, smart contract, wallet based account abstraction strategy that we might do in the future, basically because, the, the code that a user needs to assign over is just is a smart contract wallet. 
* And so you can literally use smart contract wallets that exist today. and so workflows in this scheme just very naturally carry over into workflows that would also make sense in a full, full smart contract wallet world.
* And so that's the core idea right. Basically, yeah. Like you can think of it as being 3074 esque from the perspective of, how some like application developers might interact with it today, but then at the same time, kind of borrowing a lot of elements of style from, some of the other and, more, more conservative account abstraction proposals. And, so we brought that up yesterday and we, discussed both the EIB itself as well as some ongoing corner cases that are being discussed on the magicians thread. and, in,
* And in other places, like basically pigs around. How do you, like what's what are the specific bits that you sign over or what what particular features do you, add for safety reasons? What particular codes do you, disable? And, there's a lot of, like, a lot of similar considerations to what's been debated within 3074, in that sense, a couple of new ones as well. And so there's definitely yeah, a lot of, you know, discussion on those points happening in, both on the PR and, on Ethereum magicians. 
* So, highly encourage people to look at those and, participate and, you know, if they're interested, start, you know, like, figuring out how this, might make sense for, like, their piece of infrastructure or their use case. 

**Tim**
* Thank you. Anyone else have? Yeah. Comments. Questions? Oh, sorry. yeah. Andrew first. Yeah, I guess if if you do, please raise your hand and zoom in. I'll go and order. 

**Andrew**
* You know, I think I like the idea of 7702. I think it's more elegant than 3074. But my big concern is revocability because right now it doesn't specify revocability in any like at all. And that's a big security concern. 

**Vitalik**
* Yeah. Very valid. Revocability is, one of the items that's, being discussed right now. So there's, a couple of strategies that have to do with either assigning over the nonce or signing over the nonce divided by some number that are being talked about at the moment. 

**Tim**
* Got it. Nassim. 

**Nassim**
* Yeah. So, I have a I think I have, like, a few questions and and thoughts. The first one, I just wanted to, emphasize that, in some, in many use cases, gas costs are probably going to be can you guys hear me? I have like, yes, someone literally just destroying the apartment right above. Awesome. so yeah, I think that the on the gas cost side, I would love to to hear a little bit more there because like 3070 for steamed, I need to I need to run some modeling. Obviously this is like 7702 is just very new. Need to do some modeling. that's my first question.
* In terms of actual gas cost per transaction, how did we think about, that versus having a transaction, where the cost actually scale out with the size of the contracts that we approve? and with that, generally the contract is, you know, the more features and the more, safety features, the more expensive the transaction is going to be. Sorry. Whereas, signing over, for example, an address, that you may have checked, you know, as a user verified the code, independently and separately. 

**Vitalik**
* Yeah. Also a very good point. I think a couple of answers there. So one is that even if we do assign over code, one option that is always available is you get the code that you sign over, can be a delegate call forwarder and delegate call forwarders can be, you know, only 44 bytes. And so that's so that's one approach for making it very affordable, even for very large contracts. And then again, I like I personally am totally okay with both the like code in the transaction version and the code address in the transaction version.
* And one of the considerations that sometimes gets, talked about in the other direction is basically cross-chain, support. Like if you want to assign over something and, have it work on multiple chains, then, a yeah, a hash gives you a somewhat stronger guarantee, as though obviously those guarantees go away if you if you end up using a delegate forwarder. So there's a couple of, different, ways of, handling that. But this is, again, this is like one of those, finer points that's still being. 

**Ben Adams**
* I originally thought, signing over the code address would be better, but I've come around to the idea of putting init code in instead because there's two separate signatures. So you've got the signature where you're approving, you know, here's the contract, I want you to use it. And then there's a separate signature outside, which is here's the data I'm passing in. If you want that inner signature to also approve some data, then you need you need an extra. So you could do here's my proxy contract. Press send data. And then the outer contract could sorry, the outer signature, which could be, you know, sponsor, could add extra data, which isn't dependent on your signature.
* So it's a more flexible. 

**Tim**
* Got it. There's another. Okay, so there's a couple of questions in the chat or comments anyways that sort of go at the same idea of like implementation work around this. and whether, you know, we could reuse some or part of the 3074 work or how much more work it would be to implement this from scratch. And then also, Justin had a comment around, should we consider running both on like the same devnet, so that we can actually test them, in production? But yeah, I guess I'd be curious to hear from some of the EL folks like, and I don't know how many have reviewed the EIP, but just in terms of the scope of the work, like how big of a change is 7702 relative to 3074? yeah. Ahmad, I don't know. 

**Ahmad**
* My personal opinion. I've read both, and I've, we've already worked on 3070 for another Nethermind. My personal opinion is that the work will not be the same. most of the work needs, needs re like other implementation for 7702.  Not sure about the idea of running them both and how that that interaction could be because like, I don't I'm not sure how they would interact with each other, but 7702 is is definitely different and implementation wise in my opinion. 

**Tim**
* Got it. And I guess. Yeah. generally, I think it probably makes sense to give people a bit of time to review this before we make a decision about whether to include it in, like the next dev nets. And also, given teams are still not like done implementing devnet zero, we do have a bit of time. So And yeah, skimming through Eth magicians. skimming through each magicians, you know, does seem like there's a bunch of conversation happening around 7702. But, um. Yeah. Does anyone feel like there's something we should sort of decide today about it or, like an issue we should resolve, or does it make sense to continue the discussion?
* I think, and then, on the next call, make a decision about whether we want, effectively devnet one to have both, only 7702or, yeah, potentially something else. Charles, you say you have a new draft EIP. Is this related to 3074 or 7702? 

**Tim**
* Okay, okay. didn't mean to interrupt. Okay. So definitely. Okay. So there's definitely some concerns about having both in the devnet, but, yeah, given we're already, you know, pretty much done with Devnet zero, it's probably more work to change the spec now and say, you know, remove 3074 or anything like that. So I think it probably makes sense to move forward with devnet zero and then make a decision about 7702 on the next call. Does anyone have an objection to that? Okay. So yeah, definitely encourage everyone on the EL side to review the ETH magicians thread.
* And then it would be great if in the next two weeks, we can flesh out, these issues around just revocability gas costs and, yeah, all these other, smaller details. And, if people still think this is, you know, the best proposal to move forward, then maybe we can add an indefinite one and remove 3074. but, yeah, gonna make that decision in a couple of weeks.  Anything else on a 3074. 

**Nassim**
* Sorry, Tim. I just wanted to emphasize that, you know, I want to kind of take a pragmatic approach for I know that it's not a case of everyone in this call, but like, a lot of, companies have been kind of like, you know, wallet providers and so on have been building pretty large scale, 2771, you know, bundle, sorry, meta transaction providers and just wanted to emphasize that 3070 for us, I mean, like, we're included in this category, you know, is a lot easier as kind of like a next step.
* And so I just wanted to emphasize the need for, kind of either some kind of considering, 3074 as kind of an incremental step for everyone who has right now, 2771, you know, infrastructure to, sponsor gas cost for all the smart contracts that do support kind of what is there for orders or having some form of joint efforts from everyone to standardize, an implementation of, you know, 4337 bundler that would really help every single wallet provider, essentially, offer table stakes, table stakes features. Because at the end of the day, 99.9% of of our user base just pretty large. Now, is really just asking for gas sponsorship and transaction batching, on every single contract and both satisfy that.
* But one of them is a lot easier because of the infrastructure that we already have in place. Definitely understand kind of the concerns on on all sides, but just wanted to to throw that out there. 

**Tim**
* Thanks. Joe. Are you looking to respond to this? 

**Dror**
* Yes. Just one clarification. We are still looking into 7702. It seems like, there is some, the accounts that using it will be almost, like standard, accounts using the EOA and with minimal change to the bundlers and no change to the entry point. But, again, this is very preliminary. We didn't it's still hand-waving, but it looks promising and a quite easy to get with. 

**Tim**
* Got it. And just sorry, I'm not super familiar with the details here, but the 2771 EIP or ERC. Is this effectively what can be like? Is this the 437 bundler? Are they like the same interface or are they two different things? 

**Dror**
* No, it's a different thing. It's a way to put code inside an account, to make it look like it is a smart contract. And it can be used with a the on chain contract, the entry point contract of a 437. You do need a slight modification to the bundler okay. In order to use this transaction type. 

**Tim**
* Okay. Got it. Okay. yeah. This definitely feels like something that, you know, we should figure out in the next few weeks at least, even though we may not have, like, a full and final implementation. if we can at least sanity check that there is no sort of blocking concern here. yeah, that'd be really good.  Anything else on the EIP. Okay. Great. yeah. Thanks, everyone for sharing.  Moving on Ethan, you had posted, a fair bit around, 6110 and the whole messaging scheme there are. Is Ethan on the call? 

**Ethan**
* I am. Yeah. 

**Tim**
* Nice. Do you want to give a bit of context? yeah. 

**Ethan**
* Sure. So for, the deposits, the withdrawals and the consolidations, there is this new scheme, I think it's 7685 EIP. And there is a problem with that optimistic thing that I noticed, right now in Nimbus, what we do is to accelerate the sync that we, only send every X blocks to the EL like we do, like, breaks in between during sync so that we don't continuously interrupt the EL while syncing. 
* And we can do that because the CL can, check that. The chain is consistent with regard to the block cache, like when there is a new payload FCO. The EL does. At the very least it does this block cache check, and we sort of integrated this into the CL so that we don't have to send all the payloads. So one problem here is that with 7685, it seems that this is no longer possible because there are now fields in the EL block header that are not in the CL execution payload anymore, namely this 7685 requests. Three. So. It like it is no longer possible to compute the block cache from CL payload. so which. 

**Lightclient**
* Part is not available? 

**Ethan**
* This requests tree, but. 

**Lightclient**
* You can compute you can compute the request tree like you have all of the requests in the execution payload header and body. All it is, is a matter of if you're going to implement the optimistic sync, you need to understand 7685 because 7685 only comes into play when you're computing the execution layer block cache. So once you know that you can compute the request header by doing the typed ROP encoding. 

**Ethan**
* So in the like for the consolidation, they are not even in there, but for deposits and and withdrawals, they are there as separate lists. And it would be. Possible to reconstruct. maybe I'm not even sure. Like, they could be interleaved. Like, I'm not sure they. 

**Lightclient**
* Can't 7685 defines the ordering. So the ordering is based on type. So if you have a type-0 7685 request it would be the first thing. And then within the type zero request, whatever type zero is can define its ordering like intra type. Then you'd have type one, type two etc.. 

**Ethan**
* So why do we have separate lists in the payload and and not like why do we combine them in the EL but not in the CL. 

**Lightclient**
* I propose 7685 Because on the EL it feels a lot more cumbersome to continuously extend the header and the body. And if we're going to be adding 3456 plus types of CL requests, it feels much simpler on our side to do it this way. Any L's that don't agree with that? Feel free to like mention this. But that was like how I felt and what the feedback I was getting while we were implementing 6110 and 7002 was I didn't specify to use requests on the CL, because I got a little bit different feedback that the CL would prefer to have the list flat within the payload, and that's fine. I don't think that there's a reason to enforce the exact same format across the layers. We can do it and something to discuss, but that's why 7685 was created. 

**Ethan**
* Okay. That's that at least explains the motivation. Thanks for that. So. Is there? Like, is this still the preferred design overall, or is there, a way to explore, like just to keep it separate lists or like how much of how far down are we in here? 

**Lightclient**
* On the EL or CL. 

**Ethan**
* On the EL. 

**Lightclient**
* I think most people prefer the single request list. I'm like open to removing 7685, but it seems on the EL word we were not really built as well to continue extending our header and body. Each time we do this. Like we have to plumb a lot of code through, and for us this makes. The request much simpler. 

**Ethan**
* Okay, I'm not sure if that's only guess or alter the others, but, another proposal that could simplify it is if we just align them completely and do the SSZ transition of the block header to match the payload header. Then it's one data structure. For both of them. Like we have discussed this, when withdrawals came up. And I think SSZ is still, like, long term goal to do as a transition. And I think it would be a good timing to use, like these three new trees that are being added. As well as the 7702 transaction type to. Like it's all additional stuff that would benefit from SSZ and simplification. Less data conversion, no more endian back and forth. We could also switch to engine API to SSZ like it would unlock a lot of things, and I think getting it away before Verkal is a good timing.
* I know that you have mentioned that in Geth that. There is no good SSZ library yet for go, so that's indeed a bit of a. Work that would be required, but I think it's better than having to redo all the plumbing over and over again, because in SSZ it's trivial to add a new list to a to a container like we do this with every fork. It's no problem. 

**Tim**
* To be clear, these I guess these are like two different concerns, right? The first is, the the information you get and the payload is not sort of easily allow you  to skip blocks during optimistic sync. and then the second is, you know, if we're going to add all this information, maybe we should add is using SSZ. That is. Yes. Okay. I guess just maybe just to finish on the first one before we discuss SSZ. My sense just skimming through the chat is like. Most of the ELs, if not all of them do like 7685 a lot. And, it does seem like based on what client was saying, that you would be able to reconstruct the tree on the CL side, even though the information is not like the block header. Like. Yeah, I guess. Is there a reason why this is not a viable solution for Nimbus? 

**Ethan**
* I mean, I would have to check how much work it would be, like, in the CL. Right now we have, separate lists for the deposits and the withdrawals. There is no list for the consolidations, but maybe they can be extracted from the state transition function or something. right. 

**Lightclient**
* Now consolidations are not in the EL requests because right now we don't have EL triggered consolidations. 

**Ethan**
* Okay. I mean, I don't know the details there, but I saw this type two request somewhere. But if they are not there, then even better. so what we would have to do is to convert the deposit receipt and the withdrawal request. back to RLP. To little endian. Right. And then create attempts in that 7685. To. Re-obtain the root of the tree. Right. And then we can continue to compute the block hash. Is that what you are suggesting or. 

**Lightclient**
* And this is about the same work you would have needed to do if we were extending the list. Like we are still going to encode it with big. We're still going to empty it. Now it's just instead of having in mp2's we just have one. And when you encode you put the type prefix on it. 

**Ethan**
* Sure. Yeah. It's, the same amount of compute, but it's conceptually still a divergence between the two, layers. Right? 

**Lightclient**
* Right. 

**Ethan**
* So. Yeah, I think this first, Request to like that. It's not possible anymore like that. It struggled with the optimistic thing. I think with that conversion, it's no longer a primary concern. I still think it's a bit ugly to diverge there, but that's more like for the other, point with moving to SSZ, but that's no longer a blocker for optimistic sync. 

**Tim**
* Okay, so I guess. Yeah. for this specific syncing issue, if, let's assume that this works and if it's not the case, obviously, obviously we can discuss on a future call for SSZ itself. this is obviously like a fairly substantial change. So  I guess I'd be curious to hear from, you know, EL teams like, given all the other stuff that is being considered right now. you know, there's like EOF there's 762, three that we were going to talk about a bit later. and then, this, this bunch of other EIPs as well. You know, do any EL teams feel like converting some of the objects that SE is like a something they would like to prioritize in this fork? 

**Ethan**
* I mean that the question is also has anyone actually looked into it? 

**Tim**
* Because, I mean, I think people have generally looked into SSZ over the years in like different contexts. So obviously. Yeah, like obviously the specifics of the implementation matter. But I think. Yes. My sense is we probably have a general feel of like what it implies to us and also what it implies to maintain both SSZ and RLP on the EL

**Ethan**
* RLP is fine. It's about the Verkal tries. Right? 

**Tim**
* Right. Sorry. Okay, so, yeah, Rhett seems to have looked into it. Would like to avoid Baozou as well. Um. Anyone feel strongly? In favor of doing it. 

**Guillaume**
* I'd rather do it now than do it in Osaka. 

**Tim**
* Right. 

**Ethan**
* Like. One thing that we have as well is there is this EIP 4788 that put the beacon route into the state and. Now with electro, there are a couple containers that already start to break, like, if you have something that consumes a proof based on EIP 4788, after a Electra, that verifier stops working because the shape of the proof changes. Right? And. Now with Electra. When we break them anyway, it's another opportunity to like just do the timing. I know that it's a lot of work. It's a lot of mechanical work that does not primarily benefit us developers. But, there are two questions like one is, do we ever want to do it? And if we ever want to do it, then. Do we gain anything from delaying it like. Right now. The new fork. It adds another empty to the EL like this 7685 requests three.
* It adds a new transaction type with 7702, and it breaks all the generalized indices in Beacon State. And I think also execution payload header. So like every fork, it's more work that needs to be converted. 

**Tim**
* Right, I guess. Yeah, the trade off there is. The more we wait, the more stuff there is to convert to SSZ when we finally do it. And then if we delay doing it, it means we get to do everything else slightly quicker because, yeah. Or we get to do more things in the same amount of time. Yeah. My sense is, yeah, there's not really any support from the EL side to. Do this in this fork. And obviously if this changes, we can reconsider it. But, Yeah. It really doesn't seem like, any of the Yale teams want to include this within Pectra. I don't know if anyone else. 

**Ethan**
* They're like, how are we on the state of school libraries? Is it only go that doesn't have one? Or is it the same problem for the other, teams? 

**Garry**
* On the basic side, we have, a moderate, moderately complete SSD implementation, but we really only have, exercised a subset of it. So, it would we would probably need some more work and attention, but I don't think we have the same level of, blocking as Geth does currently. 

**Marek**
* So another mine site. We written our own SSZ library, which is not, used on production. So we will see on Devnet how it works, etc.. 

**Tim**
* Any other comments? Questions from anyone else on SSZ? 

**Piper Merriam**
* Yeah. If we don't do this now, aren't we going to just run into the same problem next time when this comes around and the work hasn't been prioritized to get everybody to have good SSZ libraries? Like, isn't this just the same problem later as it is now? 

**Tim**
* Yes. And it's a question of what our priorities are now versus later. 

**Piper Merriam**
* And and if doing now makes us faster later, doesn't that make a pretty strong case for doing it now, even though we're not ready? 

**Tim**
* Well, you know, it depends on like what's what's the value of getting it done, what's the value of getting everything else done. Like, you know, say that this took 3-6 months extra. Do we think it's more valuable to do this now or to do, you know, Verkal or 4444  or EOF? And yeah, that's effectively the trade off.  Yeah. just because we have other stuff on the agenda. Any other questions? Concerns about this SSZ? Otherwise, I think, yeah, it probably makes sense to continue the discussion, I think, but it seems unlikely we would we would consider it for this fork. Okay. then moving on, I guess. Ethan. Yeah, the two, the two issues was the sinking and then, changing stuff to SSZ while we are doing it. 
 
**Ethan**
* Yeah. I had some  6110 related specifics as well regarding ordering of deposits. Like there are two parallel deposit mechanisms and deposits may get reordered, but we don't have to discuss it with everyone. And the third one in the, GitHub comment was consensus related regarding attestation. Type, so it's not relevant to this call either. yeah. So I think that covers it for me. I will personally try and get Zack onto a devnet.. With Nimbus EL, I guess. And maybe that could extend that could help us gauge the exact scope that's needed, because I don't think it's a six month thing that. 

**Tim**
* Yeah, I think that would actually be it. Would be useful to see like what the implementation was like, what you know, what things were harder than you thought they would be, what things were easier than you thought? so yeah, there's definitely value in that. Michael, you have your hand up. 

**Mikhail**
* Yeah. I just wanted to add on the 6110 stuff and, not the, all the, the processing, deposit order, not in the order they had been submitted to the contract. this is really a fair concern. I think we need to do more investigation and talk to, Rockefeller and probably other staking pool is if it breaks anything on their side. but basically, the situation can be as follows. During the transition period, this one data pole will, . We'll be onboarding. We'll be filling the gap between like, the last processed, deposit before the fork activation and the first deposit that had been processed according to the new 6110 logic.
* And, those gap is like deposits that were submitted to the deposit contract before the new ones, obviously. and, yeah, the old deposit can be finalized already, and then someone can submit a new deposit that will, create a validator with the different withdrawal credentials, and then the when it one data pool fills the gap, the one that had been submitted before the elder one, will be a top up to a new withdrawal credentials. So probably the brakes some so some stake in some stake in pool design breaks the security. So, yeah, that's a fair concern. I just wanted to highlight that and. Oh, yeah. 

**Tim**
* Thanks will be investigated. Thank you.  Anything else on this before we move on? Okay. next up, so two EIPS that we had CFI, sets of EIPs with CFI for fork, have some updates. So, first EOF, then, there were some potential issues around 763, so we'll do EOF first. I know there's been a couple breakouts, since our last since our last call, but yeah. Any notable updates to share? 

**Speaker V**
* Not too many. The first breakout we had on May 1st, it wasn't too well attended because of a major European holiday. if anyone wants to learn about more about EOF, you're always welcome to show up. And, maybe not necessarily during the meeting if we got a large agenda, but you could ping me or any of the other people involved in EOF. You're trying to, you know, get a tighter grasp on it. but as far as yesterday's meeting, we're just, sewing up the very final, states of the spec, there, as opposed to the, EVM channel in the discord where, the big the big thing that's been, working out for the past month is we're formally removing the HT create and the init code transaction from the first revision of EOF, is not essential to it. And we're going to rely on the existing create transactions.
* And there's a specification there for how we're going to handle EOF without requiring a new transaction type or in a regular state change. Those are no longer required for EOF v1. but, you know, just cutting up the corner cases that everyone, discovers as they do the final, pieces of implementations in their clients. as far as testing, I'm writing a lot of the, execution spec tests for it, using the various clients to guide where I get the appropriate coverage to make sure I cover all the pieces in the clients that I'm available to see. so, yeah, that's that's an update from my perspective. Alex probably has more to add. 

**Alex**
* Yes, please. Alex. Hmm. I also posted the links, but three updates. So there's a meta EIP which has been merged and which lists the all the relevant EIPS. that's 7692. And Daniel mentioned the removal of TX create. for those unaware, the TX create was the way to create contracts and that relied on a creator contract basically, which needs to exist in the state. instead of this, we came up with a more simplified approach which doesn't require new transaction type, doesn't require the special contract. it uses the existing, creation process used in legacy. but the design is forward compatible. So we could introduce TX create in the future. but this definitely removes, the transaction changing aspect of implementation and testing.
* So basically testing, really has to deal with, the EVM level and it doesn't need any new special rules for transactions. and this new transaction EIP or like this new contract creation EIP is 7698. and the last update I wanted to highlight is, we always had, or at least for the past couple of months, we had an implementation matrix, which lists, the EIPS, the tests, as well as the client implementations and language, solidity and wiper implementations. This has been updated, this week. And if you take a look at it, it seems that there is an EOF implementation in almost every single, client, with the exception of Aragon.  But in some of them it's kind of a stale implementation. so in Ethereum JS, it is definitely a stale older version of EOF. and the wiper implementation is also old. but the implementation in solidity is being worked on as of, the past two weeks.
* And I think Ethereum and Nethermind those are listed as work in progress. it seems there's active work going on in both of those. and those are using the, the latest specs. So those are not really stale, pieces of work. I think that's my addition. 

**Tim**
* Awesome. Thanks for the update. we've been waiting on the Meta Eth for a couple of weeks. I know there was some delays in getting it merged and. But given EOF is CFI, does anyone object to CFI being the meta EIP? which lists all of the sort of individuals EIPS just so it's easier for people to reference? and if we do that, does it make sense to also include the creation transaction EIP 7698? I guess. Any objections to this? Otherwise? I'll do it. So at least it's up to date with the latest spec. Okay. And any other questions comments concerns about EOF. Okay. Well, yeah. Thanks, Daniel. And, Isaac for the update. Next up, for EIP 7623. I believe we have William on the call who had some concerns that he wanted to raise.
* So, yeah. William, do you want to take a couple minutes and, . Yeah, walk through those. Oh. Oh, William, are you on the call? We can't hear you. Yeah, I have.
* Some issue, a meeting, I'm trying to present this, slides. 

**Tim**
* Yeah. We can see everything. 

**William**
* Okay. All right. so I'm trying to discourage a pattern of, metering gas. So I have some examples. first, consider a taco stand that charged the maximum of $3 per taco and $5 for salads. People that want to buy tacos and people that want to buy salads can work together to save money. similarly, if there was a discount where we charged less for combining tacos and salads, there'd be a way to make money again by combining where one person buys the discount and sells their unwanted, components to the people that need them. and so, this brings us to EIP 7623, which charges us, gas according to call data. So there's a maximum function in the gas used to try to, split out the call data gas so that it's worse for some people and the same for everyone else. this has some a problem called gas sheltering, which I call.
* It's because it's similar to tax sheltering, in that you can offset, the costs by, combining, for example, gains and losses and tax sheltering and call data and execution in gas sheltering.
* So, because, the gas is no longer marginally priced, which means that each incremental units of computation, doesn't cost additional gas. It causes some economic problems with the way, with the market and incentivizes some strange behaviors. first, consider the case where the call data gas is greater for a transaction. So a user's gas would be determined by call data referring back to this formula. this means that they would pay 12 gas per token. and so, such a user, they can add execution gas to their transaction and it would not increase their gas use, and therefore they can sell that gas, to someone else that would like to buy it. 
* And there's no price at which that, . Cost is ineffective, that it's always a profitable sale. and so, this combination has some, dangers to it, which I'll discuss later. but there's another kind of combination. The kind of combination when the execution gas is greater. In this case, you would like to pair up with someone who is using a lot of call data. So this would allow you to save two thirds of your call data cost. so effectively, you're arbitraging, to save gas. and, this results in a lower effective gas price for users that combine than users that don't combine. because you can consider the gas that they would have paid without unlocking the gas. in the world of MeV, MeV is execution dominance.
* So searchers would want to batch with call data users. so they would be looking to increase the number of call data users and centralize them so that they can win the gas auction. another topic is that L2's who post large amounts of call data, would want to batch with searcher transactions, and this can cause centralization in the gas market.
* And other kinds of problems, as that's a rather monopolistic power that they would have. the free gas. so I also compare this to gas tokens. for gas tokens, there was an efficiency of one half, which is also possible. In the first case I discussed, there's incentives,  for creating and destroying, accounts for gas tokens, but, for gas sheltering, the incentive is for additional call data. So this means larger blocks than would have happened in the organic market. just due to the incentives of attracting the call data users, into the sheltering scheme. 
* So, this means higher gas prices, for people that aren't participating in gas sheltering and, a lower block gas limit. Therefore, because of the possibility of two x, one difference from gas tokens is that gas tokens. gas can be used on anything, whereas unlocked gas must be complimentary. Vitalik released a blog post discussing this today. and, so I reiterate that the reason the 50% gas fund was removed is that, it allowed larger blocks, than should be possible. and so, I recommend set a much simpler solution to just increase the call data gas for everybody. I've written this as EIP 7703. so it keeps the regular gas use formula, thereby not introducing gas sheltering. the largest potential block size is reduced by the same amount. So the worst case is the same,
* But everyone pays the same rate, regardless of how much execution gas they're using. so, as Vitalik mentioned in his blog post, a better scheme in the long term would be to separate these different components, into different gas markets, similar to block gas, and that would preserve marginal pricing. that's all for my presentation. . Thank you. 

**Tim**
* Thanks, William. yeah. Vitalik. You want to go next? 

**Vitalik**
* Yeah. So thank you very much for that, William. so I think, a couple of, points that response. Right. So one is that, all of these downsides do need to, as usual, be weighed against the upsides. And, the upside here is the pretty large upside of, being able to, decrease the theoretical maximum data size of a block from 1.9MB all the way down to 0.6MB, all not including blobs, while keeping almost all applications the same price as they are today, with extremely few exceptions. So it's, important. Like, there are basically, you know, we we keep in mind costs. It's also important to always keep in mind what the benefits are in the background. I think, more specifically, yeah, with regard to these, secondary market concerns.
* I mean, I actually, fully agree that this, is, a valid, problem in theory and that, if secondary markets like that happened, that would be a bad consequence. But I think, the main reason why I'm not concerned in practice is that basically the total addressable market for this, kind of coincidence of wants is extremely tiny. Right? And the reason why I'm confident about this is because, Tony and I or actually just Tony in this case, did some, analysis of, which transactions actually are called data dominance and by how much? And, the answer turned out to be like, especially with the 1248 pricing as opposed to the earlier 1768 version. very few. Right. So, starkware proofs, stark proofs increased by, I believe, around 1.3 x and then, layer two protocols that have not moved over to blobs. So things like, inscriptions and scroll, go up by like two x or somewhere between 2 and 3 x. 
* So I think, as a very recently scroll has, switched to blobs. And basically I think all of these, call data used a dominant use cases are switching to blobs. And, the number of remaining exceptions is like basically darknet and a couple of, Verkle proof users. And, like, it is totally true that they could, make some profit by auctioning off a tiny amount of extra execution space that they have in theory. But in practice, just, like if you actually look at the numbers and if you actually, like, divide this by the the total amount of, gas that's happening, like the market is just, not large. Right? And that's not something that was true with the, gas token market, because gas token markets were just like they did not require this kind of two sided coincidence of wants. Right?
* They just required people who are willing to save up gas when gas prices are high, whereas in this case, like, you actually need to have this.
* Two way agreement between an execution dominant user and a call data dominant user, and the constants in this EIPs were chosen such that the number of call data dominant users is like actually extremely small. So that's the reason why like I'm actually not particularly worried for the short term, but like I do, I do accept that this is a valid downside of this EIP. And like I do, definitely favor moving to a multi-dimensional model eventually. I think the reason why.
* Yeah, we ended up moving away from just like a raw forex bump in, call data prices, which actually was Tony's in mind, idea of, like about a month or two ago is basically because, that was like that actually would be extremely punitive for both Starkware and a lot of like layer one, layer two to layer one, bridging, Verkle proof verification, use cases, and a lot of other things it would like.It would bump up stuff that's like pretty critical to the layer two ecosystems, ongoing decentralization by a factor of four. And so that could actually be a. 

**Tim**
* Okay. I think zoom crashed. For everyone. Okay. Are we back? Okay. Yeah, I think zoom crashed. Sorry about that. . Oh. okay. So, Vitalik, you were talking when, when it crashed, but, I'm not quite sure exactly where. Okay. you had your hand up. 

**Ansgar**
* How it could sound to people. And that, of course, is not a very principled way of handling these things, but that there's actually like a, like a principle behind this, that and that, that's it's like a common misconception that that pricing on Ethereum is basically trying to account for the, like proportional cost and  that any compute causes for nodes in the network. But that's not actually the case. And that's you can you can kind of realize that by in two ways, right? One, those nodes don't actually get any of the money that you pay, right? Like you don't that's not distributed across all the nodes that actually need to execute the transaction. But also it doesn't depend on the gas price. If there's only one way gas price, then then all the the cost you cost for the nodes and network is basically free. And if it's like 100 gwei all of a sudden it's really expensive. It doesn't. There's no relationship.
* You're not actually paying for the for the effort you cause.
* It is a purely a congestion pricing mechanism, meaning we have fixed resources on the network. We are just saying, hey, this amount of compute, this amount of data, this amount of bandwidth we are willing to give to the network per amount of time. And so congestion pricing is just a mechanism to allocate that to the person that values it the most at any given moment of time. Right. So that's why people pay. And so actually this this one dimensional way of doing this that we do in Ethereum right now or I guess now with two dimensional but one dimensional in the normal EVM side of things, it is really inefficient in that most of the time we are only using a fraction of the available resource, right? 
* We always have to to plan for the worst case. So we have to make its price thing so that if if someone only uses compute that the block doesn't explode too much, or if someone only uses data and an entire block, it doesn't. It doesn't blow up too much. But most of the time people actually use some sort of mix of the two. And so we are way underutilizing the resource of the network. So this is just deadweight loss. It's just an inefficiency in the network. And so this basically is just a very like a small example of a class of mechanisms that start to make this more broadly available. So now basically we incent specifically incentivize behavior. And so this is why this funding in general is not a bad phenomenon. That's actually a good thing. Like we are incentivizing behavior that tries to push the usage of each individual resource closer to its theoretical limit.
* And so indeed, of course, details matter. And so I do agree actually, that these concerns to some extent apply because of course, it's a more pragmatic mechanism. It's not like a theoretically completely as a sound way of approaching this. But but I agree with Vitalik assessment that it's good enough. And again, it's not just a pragmatic fix, but it actually has like a deep underlying principle that there's this huge inefficiency right now on Ethereum. And we are basically removing this to some extent. 

**Tim**
* Thank you. Tony. 

**Toni**
* Yeah. I just wanted to add that, I do agree with William. So there is this theoretical threat, but I also agree with Vitalik that it's not very practically viable. Especially thinking of such markets would require trust among the participants and also a high degree of coordination. And imagine you as a L2. You want to post your data down to L1, and you don't know which address will post the data or where the data will eventually be. from a practicality from practicality standpoint, you would need custom indexes and all that. So I don't think it's very viable. And regarding the multi-dimensional fee market, I also agree that this might be, more close to a endgame solution than, 7623, but I think the main goal. So the main goal of 7623 was to kind of defuse this DDoS vector of big blocks, especially thinking of increasing the block count or increasing the gas limit. And at least until Pectra, I think it's the most viable thing that we can do. 

**Tim**
* Ben. 

**Ben Adams**
* Could do something simpler, which is the zero byte discount is only applied in the first n, say, 1024 bytes of call data, after which it reverts to normal. which also has an advantage that when. The EL is trying to work out the gas price of the call data. It doesn't have to re count all the zeros in the megabyte. If it's a megabyte long, it just has to do a thousand bytes and then use the length of the rest. 

**Tim**
* Yeah. And there's a couple comments in the chat around some of the EL devs who had, expressed some concerns about it. So on the Geth side, and then on Nethermind as well. . Anyone else have just comments or. Questions about 763. 

**Charles C**
* I have a question which is, has, enshrining call data compression been considered? Like if you have, like, run length encoding or maybe some very simple algorithms, you could also reduce call data by a lot, but without needing to change pricing. 

**Ben Adams**
* I'm. It inflates. 

**Tim**
* You know. 

**Vitalik**
* Yeah. I mean, I think everything is are wrapped in snappy at protocol layer already, right? 

**Charles C**
* Yeah, but is it like cheaper if it compresses? Well with snappy. I meant from a pricing perspective. 

**Vitalik**
* Right? currently, yeah. It is, not at least at, at a one. I'm not sure if any alters have started properly accounting for that. I mean, ultimately, I guess, any, like, contracts are always able to individually decompress stuff. The question is, like, does it make sense to, like, basically make snappy compression up, recompile? I mean. Instinctively, that feels like a pretty complicated thing to do. And like trying to. Enshrined that might. Proved to be something that we regret if we discover other compression algorithms. But, and I'm not against exploring it. 

**Charles C**
* Yeah, because everybody's compressing it anyways, so. Why should you? kind of punish people who are making call data that compresses. Well. 

**Vitalik**
* Right. Yeah. That's fair. And I mean, I think like the zero byte discount is in part intended precisely for that reason. Right. Because lots of zero bytes are by far the most common case of data that is big in terms of raw byte count, but that does compress very well. 

**Tim**
* Georgios. Your hand up. 

**Georgios**
* Yes. I wonder how does the group think about core data changes in relation to blob count increase or decrease? And I joined late in the call. So maybe this was discussed already, but I recall that there was a blog item that said we cannot adjust blobs if we don't do some data analysis or the impact on the network, and it seems like an increase in the call data would need to be accompanied by something like that. So I wonder how do people think about that? 

**Toni**
* Yeah, I have looked a bit into that and I think it's it's hard to tell. So if, for example, a blob increase would already be doable or not. But what you can definitely see already is that blocks that are bigger and with bigger, I just mean three times the average. So not even getting close to the max and they are much more likely to be reworked. Or you can also see that weak validators cannot attest to those blocks, or don't attest or don't see the blocks, etc.
* And you can also see that builders are already discriminating against, yeah, certain blocks that are just too big because they might want to deliver the block in the last milliseconds. So in the last milliseconds they would throw out a lot of other transactions. right. 

**Georgios**
* So I'm in agreement that the like these are all issues. I wonder, does the group think that cold data increase comes with a blob count increase, and if so, is anybody doing the research required to get very clear data driven numbers for whether we can do that? Because just doing the cold data increase in the vacuum honestly doesn't seem, you know, like it it seems like it doesn't, like, solve much of a problem in a vacuum. 

**Tim**
* I think, Perry from the DevOps team had, like a stub EIP about this and was planning to, you know, help with some of this research in the coming months. But yeah, I don't know to. Yeah. To what extent like it's been started or anything like that. Dankrad

**Dankrad**
* Yeah, I think I just wanted to say, I feel like at least we can consider increasing it so that the max stays the same if we add this EIP. because that shouldn't. Make things any worse than they are. 

**Georgios**
* Well, that's also my strawman view, right? But I wonder, like, just so that we can have a good process about going about these things. I do wonder, like if we should be coupling the two conversations and if so, if we should assign someone a dedicated individual that goes and does that research, because otherwise it seems like we could have we could be having this conversation three months from now and being like, hey, has anybody done the work? And if we think the work is important and we should prioritize it and pick a person to go and do it. 

**Tim**
* Does anyone want to volunteer for this? And yes, I guess the work would be benchmarking clients using a larger blob count, potentially. You know, ideally doing multiple different counts so that you can get a sense. 

**Georgios**
* Basically, basically it will be a lot of work. It might not be glorious work. Somebody has to do it. Like maybe we will have capacity to do it. But like I'm pointing out that like this work must be done. And, I think having conversations around these kinds of VIPs, while we don't have any person doing the work, is kind of like, a weird use of our time on all core devs, I feel. Like we are aligned on the general like type thing, but like to move the ball forward. It seems like there is a clear blocker and I feel like we need to like align that somebody needs to go and own it. 

**Tim**
* Einziger. 

**Ansgar**
* Yeah. I just wanted to say that this is this EP is not only about making room for blob increases, but in a way patches an existing vulnerability of the network. Just because we've already seen from the blob, from the tests, tests from from last year that as we reach the current maximmaximum possible block size, the network does get, more like less stable. And so actually just getting having a better upper bound for the block sizes, even if we don't use that room for blob increases, is already, I think, very desirable from a security and stability of the network point of view. 

**Georgios**
* Right. But then you got to think who, who, who's gas prices do they make more expensive as a result of that and so on. So there's a bunch of like stakeholder analysis that should be done that, we should take into account. 

**Tim**
* I think that has been done though, like Tony, I guess. Yeah. 

**Toni**
* Yeah. I just wanted to add I will send you the link after the call, but we have actually done a lot of analysis on not only which accounts are affected, but also which functions are most affected. So what functions are the people calling that would be affected? by 76, 23. So I can I can send you a table and it so we have already done some analysis on who is affected and who not. And I can already tell you, I think it was 98% of all transactions are unaffected. So if you're doing token transfers bridging, retaking I don't know it's all unaffected. So the only the only accounts that were affected are basically those that are still using a firm for data availability.
* Then the largest part that is affected are users that are doing simple eath transfers and putting some messages in their call data, but this is very negligible and apart from that, there were big Merkle proofs and Starks that are still affected.
* But by reducing, the token cost to 12, it's yeah, the this, increasing cost would be manageable for, for all those affected parties. 

**Georgios**
* Gotcha. Thanks. 

**Tim**
* Thanks. Any other comments? Questions on the CIP? we only have five minutes left. Um. Okay. if not, Charles had an IP, that he wanted to present, non-reentrant and reentrant opcodes. Charles, are you still on? 

**Charles C**
* Yeah. Hey, so you can see here I drafted an IP for, um. An opcode to prevent re-entrancy. I checked this morning, and I was surprised to find that such a thing does not exist like an existing IP. this is kind of like a reaction to, IP 7609 not being included in Petra, because that seems like the logical way to for to give application developers the ability to, like, prevent re-entrancy cheaply. but anyways, this is the alternative. you know, it's pretty simple. We have two opcodes and it, sets the re-entrancy flag for a contract.
* I mean, it basically looks like what you would expect if you've thought about how to prevent re-entrancy in the VM, you have a flag for the contract, and it basically lasts for the lifetime of the transaction.
*  It gets cleared. and it you know, rolls back when you get a reversion or something. anyways, so if you compare this to 7609, I think EIP 7609 is a lot more elegant.
* It also solves, you know, kind of the basic problem, which is that, endian storage is way, way overpriced.
* And I'm not sure why. it was not really considered and I didn't really get any feedback or anything. So anyways, if we don't want to do that, then like. Please give me another way to prevent re-entrancy cheaply. and I'm happy to take questions about either this or IP 7609 or the payout code IP, because those are all extremely important to helping users prevent re-entrancy. 

**Georgios**
* But Charles, for the ideal people that you would love to get feedback from because the room is quite diverse. And honestly, I don't think everybody has full context on what the right thing to do here is. So if you were to point at like a category of skill set in the room, what would that be? 

**Charles C**
* Were familiar with. Um. Pricing for opcodes or like, . Re-entrancy prevention mechanisms. 

**Tim**
* I guess there's two questions in the chat. One is proposing just using Open Zeppelin's Reentrancy guard and then, like science is asking, did we not ask teh store to address this? 

**Charles C**
* We did add teh store to address it, but it's too expensive. And that's what EIP 7609 is intended to also address. But, I didn't get any feedback on it. Reentrancy guard. Same thing. It's too expensive. Reentrancy guard is a it's an abstraction. You know, you can use any implementation. You can use transient storage. You can use this Non-reentrant opcode if it exists, you can use storage. it just depends, what makes sense from an implementation perspective? Right now, T load and t store are basically too expensive for people to opt in to using it by default,
* And it's priced the same as, warm storage, which doesn't make any sense because it doesn't interact with access lists. And it has, kind of simpler semantics. 

**Tim**
* I guess. Yeah. We have two minutes left. Anyone on the client teams have feedback or questions? Concerns about this? 

**Ben Adams**
* I've seen the enemy worry on it would be, increasing the maximum memory that you could allocate in one transaction on in 1976 or 9 or, for lowering the cost of one. 

**Charles C**
* That's addressed in EP 7609, which I'm begging everybody to please read because it actually improves maximum memory consumption. it lowers the limit. By design. So it's, cheaper in the average use case in the most common use cases, and it's more effective at preventing DOS than the existing pricing schedule. 

**Tim**
* Okay. Any other questions? Comments? we have only a minute. Otherwise, I guess people can continue this on the magicians thread for the IP. Okay. anything else before we wrap up? Okay. If not, well thanks everyone. talk to you all soon, and I'll post a quick recap of the call on discord, in a few minutes. Have a good one. 

**Ahmad**
* Thank you.

  

-------------------------------------
### Attendees
* Tim
* Mikhail Kalinin
* Marius
* Wesley
* Barnabas
* Saulius
* Danno
* Lightclient
* Pari
* Ethan
* Mario
* Tomasz
* Oleg 
* Kasey
* Marek
* Crypdough
* Fabio Di
* Terence
* Andrew
* Roman
* Marcin 
* Pop
* Guilaume
* Protolambda
* Carlbeek
* Mike
* Gajinder
* Stefan
* Hsiao-Wei
* Josh
* Phil Ngo
* Alexey
* Holger Drewes
* Dankrad
* Guillaume
* Proto
* Holder Drewes
* Stokes
* Peter Szilagyi
* Sean
* Micah Zoltu
* Jiri Peinlich
* Marius Van Der Wijden
* Potuz
* Evan Van Ness
* Moody
* Tynes
* Alex Beregszaszi
* Marek Moraczyński
* Justin Florentine
* Ben Edgington
* Lion Dapplion
* Mrabino1
* Barnabas Busa
* Łukasz Rozmej
* Péter Szilágyi
* Danno Ferrin
* Andrew Ashikhmin
* Hdrewes
* Crypdough.eth
* Ameziane Hamlat
* Liam Horne
* Georgios Konstantopoulos
* Mehdi Aouadi
* Bob Summerwill
* Jesse Pollak
* Stefan Bratanov
* Sara Reynolds
* Caspar Schwarz-Schilling
* Ahmad Bitar
* Marcin Sobczak
* Kasey Kirkham
* Sean Anderson
* Saulius Grigaitis
* Ruben
* George Kadianakis
* Dankrad Feist
* Andrei Maiboroda
* Gcolvin
* Ansgar Dietrichs
* Jared Wasinger
* Diego López León
* Daniel Celeda
* Trent
* Mario Vega
* Kamil Chodoła
* Ziogaschr
* Kevaundray
* Antonio Sanso
* Oleg Jakushkin
* Leo
* Nishant Das
* Pote
* Sam
* Tomasz K. Stanczak
* Matt Nelson
* Gary Schulte
* Rory Arredondo

-------------------------------------

## Next Meeting
May 23, 2024, 14:00-15:30 UTC
