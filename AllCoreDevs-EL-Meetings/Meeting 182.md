# Execution Layer Meeting #182
### Meeting Date/Time: Feb 29, 2024, 14:00-15:30 UTC
### Meeting Duration: 1hour 30 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/961)
### [Video of the meeting](https://youtu.be/4ioJwNPe6RU)
### Moderator: Danny
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 182.1 | **Dencun Updates** Barnabas Busa shared an update on final testing for the Dencun upgrade. The EF announced on Tuesday, February 27 that the upgrade is now officially scheduled to activate on Ethereum mainnet on March 13, 2024. As discussed on last week’s ACD call, developers are testing the final versions of client software on a mainnet shadow fork, which is a type of testnet that mirrors the blockchain state and activity of Ethereum mainnet. Busa said developers have conducted different types of “spam tests” on the mainnet shadow fork. Nodes have remained extremely resilient through these tests and network participation rates have held steady at close to 100% participation. Though there were no issues, Busa noted that the spam tests did strain nodes heavily in terms of computer resources, specifically RAM and CPU overhead
| 182.2 | **Dencun Update** Busa then reminded everyone on the call that the Goerli test network (testnet) will soon be deprecated. Anyone using the test network should move over their operations to a different Ethereum testnet by April 17. Busa said that he had already noticed that a few large validator node operators on Goerli have already retired their machines. This caused delays to network finality on Goerli on February 28 but the Goerli network appears to have since recovered. Ryan noted that the network participation rate on Goerli is already quite low, hovering at roughly 70%. “I don’t expect [the participation rate] to last till the 17 of April to be honest,” said Busa. “It’s something interesting to watch nonetheless.”
| 182.3 | **Dencun Update** Busa asked when his team should expect to retire Devnet 12, a dedicated test network launched last November for client teams to test their Dencun upgrade implementations. In case there are any last-minute client releases that need to be tested for Dencun, developers agreed to shut down Devnet 12 shortly after the Dencun upgrade goes live on Ethereum mainnet.
| 182.4 | **Retroactive EIPs for Pectra** Retroactive EIPs are code changes that retroactively add constraints to the Ethereum protocol that largely already exist but require clarification to account for specific edge cases. The first retroactive EIP, EIP 7610, extends a rule restricting smart contract creation to addresses with pre-existing storage. For more background on this code change.
| 182.5 | **Retroactive EIPs for Pectra** One of the concerns regarding EIP 7610 was on whether the code change would impact Verkle, which is a code change that developers are preparing for an upgrade after Pectra. Geth developer Gary Rong explained how EIP 7610 would not pose any issue to the Verkle upgrade in the future. Hedera Hashgraph engineer and Besu client maintainer Danno Ferrin expressed a few outstanding concerns about how EIP 7610 may impact Verkle that he said he would share in writing on the EIP 7610 Ethereum Magicians thread.
| 182.6 | **Retroactive EIPs for Pectra** The second retroactive EIP that developers discussed was EIP 7523, which would formalize the rule banning empty accounts from the state of Ethereum and Ethereum testnets. Ryan said that he would double check who was doing the analysis to ensure that no accounts on any Ethereum network, mainnet or testnet, would be impacted from this rule if implemented and resurface this discussion again on the next ACDE call.
| 182.7 | **Account Abstraction EIPs for Pectra** Discussed potential account abstraction EIPs for inclusion in Pectra. On February 28, a subset of developers gathered for a dedicated meeting on AA where they discussed the broad objectives for the initiative and the various EIPs that could be implemented in the short vs. long-term to achieve these goals. Speaking to the goals of AA, cofounder of Ethereum Vitalik Buterin said, “So the longer term [goal is] this fundamental desire that eventually we have to have some kind of account system that is one, allows key rotations and [two], key deprecations, to allow us quantum resistance. Three, allows batching … [and] allows sponsor transactions and a couple of other smaller things and out of those of course, the first two goals are very clearly not satisfiable with EOAS and so presents a pretty clear case for moving the ecosystem to a place where it's beyond EOA centric, but then this brought the discussion to what are actually the means to get there and what are some of the specific details that are less resolved and what actually is a shorter term roadmap that gets us goals that people want in the short term, but is at the same time compatible with those longer term [goals].
| 182.8 | **EIP 7623, increase calldata cost** he proposal recommends increasing the cost for regular transactions on Ethereum that primarily use the blockchain for data availability. By adjusting the gas cost for calldata on Ethereum, the EIP reduces the number of call data transactions that can feasibly fit into one block and thereby reduces the maximum size of blocks. A reduction in block size could allow for a higher number of blob transactions instead. Danny Ryan recommended that developers on the call review the EIP over the coming weeks.
| 182.9 | **EIP 2537, precompile for BLS12-381 curve operations** This proposal which introduces new cryptographic signature schemes to Ethereum has already been approved for inclusion in the Pectra upgrade. One of the authors of the proposal, Antonio Sanso, raised a question about its implementation. Danny Ryan recommended that the question be put down in writing and circulated to developers for further discussion outside of the call.
| 182.10 | **EIP 5920, PAY opcode** This proposal creates a new operation that would allow users to send ETH to an address without triggering any of the address’ functions. Geth developer Marius van der Wijden said that from further discussion about this EIP with other teams, the testing for the proposal is more complicated than expected. Van der Wijden also noted that the proposal is underspecified. Ferrin added that the PAY opcode is currently specified to use the same code number as a different opcode, the AUTH opcode, so that will need to be rectified by its authors.
| 182.11 | **EIP 7609, reduce transient storage pricing** This proposal recommends reducing the price of the transient storage opcodes for common use cases by smart contracts such as maintaining a reentrancy log. Van der Wijden and Ryan were in favor of first collecting data on how transient storage opcodes are used after the Dencun upgrade goes live and then resurfacing the discussion on its pricing.
| 182.12 | **EIP 7639, cease serving history before proof-of-stake** This proposal creates a timeline for EL clients to stop serving historical data from before the Merge upgrade. The motivation for this code change is to reduce the amount of data Ethereum nodes need to store in perpetuity. The proposal also commits to a standardized way for nodes to structure historical pre-Merge data and retrieve it from an external source. Teku developer Mikhail Kalinin noted that this EIP has a dependency on another EIP, EIP 6110, which was approved for inclusion in the Pectra upgrade on a prior ACD call. Developers agreed to review EIP 7639 over the next few weeks in more detail.
| 182.13 | **Engine API & JSON RPC Changes** Kalinin raised a few questions related to the implementation of the confirmation rule, which is a CL mechanism that confirms over the period of one slot, roughly 12 seconds, whether a block under certain assumptions will remain in the canonical chain and be finalized. This is a powerful feature as many applications built on Ethereum could utilize the information of early block confirmations in their operations. However, to expose the data about early block confirmations, there needs to be a few changes made to the Ethereum Engine API and JSON RPC. Due to a lack of time on the call, Ryan recommended going over these changes in more detail either on next week’s ACD call or the one the week thereafter.
| 182.14 | **Light Clients Breakout Room** Ryan reminded developers that next Wednesday, March 6, there will be a dedicated meeting to discuss the light client roadmap for the Pectra upgrade. For background on the discussion about light clients, refer to prior call notes here.
| 182.15 | **Light Clients Breakout Room** Van der Wijden raised a proposal to build a new Ethereum client version to save nodes 550GB of bandwidth during an initial sync. Van der Wijden said that he is preparing a formal EIP for the new version, but a draft of his specifications can be found here. Ryan encouraged developers to review the draft and follow-up with any questions on Discord.


# Intro
**Danny**
* Let's go for it. I didn't know what DOJ meant. Done. Excellent.  well, I'm subbing in for Tim today on the execution layer call. This is the execution layer meeting 182. That's issue 961 in the PM repo. we'll spend as much time as we need on Dencun as that's coming up. We have a couple of touch points on these retroactive EIPs. I think there was some diligence that people wanted to do before they were put in. 
* Then moving on to a number of Prague electoral proposals. A quick discussion around engine API, json, PRC changes from Mikhail and then,  note about like clients breakout room on the sixth. Okay, well, we have an upgrade coming. Hard fork coming, Dencun There is, blog post out on the EFF's blog with all the latest releases I believe. If you do have updates, let us know and we'll get it in there.
* I've also seen on release newsletters and things from client teams, information coming out that way. So. Great. Are there any other updates related to testing related to releases related to anything unexpected? 

**Barnabas**
* Yeah. so I can conclude what happened with the mainnet fork. Last week, we tried to run, with everyone's, latest release. There was a couple of clients that had an RC release, that have since made a releases. During the test, we did a different kind of spam, transactions, and everything was handled, very, very, very well.
* We had very close to 100% participation, but the machines are very much overpowered. So each of the machines had 64 gigs of Ram and, plenty of CPU overhead just to be able to run the minute, we had to choose a bigger instances. 

**Danny**
* The was that across the board on a particular client combos that required 64 gigs? Or is that just firmly to get you to the desk? 

**Barnabas**
* So the primary reason is the desk requirement. So in order to get, 1.5TB of NVMe disc, we had to pick up bigger instance. That's why we just had a few nodes with very big CPU. 

**Danny**
* Gotcha. Any questions about the mainnet fork?

**Barnabas**
* There's one more thing I would like to mention that, Goerli is going to be deprecated very, very soon or it's already deprecated, but it's going to be shut down and clients can make their exits three months after the Dencun activation or one month after the Dencun activation, whichever comes later. That was the sentence we put out in the blog post.
* So the Goerli Fork was on the 17th of January and mainnet work will be on the 13th of March, which means Goerli is going to pretty much die on the 17th of April. About it. So everybody had a date in mind. 

**Danny**
* And is it? I'm looking at it right now. It seems to have participation on the order of like 70%. So fluctuating right around the finale threshold. Did it? Did people already begin exiting or turning the machines off? 

**Barnabas**
* Yeah, we have seen some large node operators that have decided to exit their validators and, discuss some, finality issues. last night, starting from last night. They seem to have recovered since then, but, yeah, the participation rate is still quite low. I do not expect it to even last till the 17th of April, to be honest, but. That's that's right. 

**Danny**
* And something interesting to watch nonetheless a network kind of floating in that. Thank you. Other Denkun related items. 

**Barnabas**
* We could possibly also discuss Devnet and when we want to shut it off, maybe a few days after mainnet fork. 

**Danny**
* Is anyone using Devnet 12? 

**Barnabas**
* It's basically just a place where we can quickly roll out some new client releases if anyone needs to test something. So it's nice to have around. Gotcha. 

**Danny**
* Yeah. Deprecation after soon after maintenance. Yeah, just. I'll echo Justin's comment.  just overpowered machine. Seems like a repeat of the mistake we made in Paris. Can we kick around some ideas to, in subsequent versions of this type of testing, get to more types of resource machines that we expect.
* Obviously there are probably extremely high powered resource machines on the network, but seeing some sort of distribution there,  might be good. Is that because of the cloud infra that we're using? 

**Barnabas**
* Yeah. So the cloud infra basically offers us two different options. If you want NVMe we have to go with a bigger machine. They don't offer large disclosed CPU and RAM machines. Alternatively, what we could do is attach volumes to the different machines and think that way. But it's possible that the IOPs of those, mounted volumes are not high enough for mainnet to able to think it's something we are testing right now. And, possibly we could encounter going forward in the, in the future shawdow fork.

# "Retroactive" EIPs [13:17](https://youtu.be/4ioJwNPe6RU?t=797)
**Danny**
* All right. Okay. Yeah. It's definitely worth investigating something here.  We can pick it up down the line. Anything else related to the upcoming upgrade. Cool. Well, in past few weeks it will have happened. So we can talk about it then. and of course, in one week,  there's anything else to discuss? We'll discuss it then. Thank you everyone. Okay. There are a couple of retroactive EIPS that were discussed two weeks ago. Let me look at my notes.
* I believe 7610. there was going to be an investigation just to sanity check. There would be no verkle issues. Did anyone look into that? This is revert creation in case of non-empty storage. 

**Gary Rong**
* I think the the blocker of this, this ape is, whenever we switch to verkle, there is no easy way to determine if the account has the empty storage or not. And, Martin has this idea that, actually, we can. So whenever we switch to the verkle and during the transition, we can, whenever we encounter a account has zero nonce, empty runtime code and the empty storage, we can just discard the storage, which means we will not move the leftover storage from the merkle to verkle. And, in this way, after the transition, we can make sure that, in the extreme state, this kind of accounts will no longer exist.
* And we can then deprecate this APE.  the idea is that, because for this storage, it is impossible to access them and also impossible to modify them because of the empty runtime code. So, it is totally safe to discard them. And, also,  for this account, they all have non-zero balance, so they will still be kept in the state even after discarding the storage. So,  if we discard the storage, then it will not be a blocker for verkle. So maybe Guillaume, you have something to add or want to mention. 

**Guillaume**
* Not really.  yeah. Whatever.  it seems, it seems like it will, it will deactivate itself. and it's not going to tamper or destroy anything during the transition or impact anything during the transition. So I think, I think this is the right, the right approach. 

**Danno**
* They taken the potential of EIP?  it's not committed yet, but it's on the table, and that's where you can do a delegate transaction. Those might gain storage. How would that interact with that? It might not we might not do the EIP, but it's something that's been discussed in the EOA circles. 

**Guillaume**
* So I don't know if Adrian is here, but, if he's not, I can just, add that I've been thinking about that as well. Oh. He's here. Okay. Go ahead. 

**Adrian**
* No, no, I'm leaving you. 

**Guillaume**
* Yeah. Thanks. so what, my understanding is that those accounts have no code, so you cannot delegate. Call them. And they were created as the result of a of a contract. So there's no private key controlling them. So you cannot use, EIP 5806. yeah. They are not affecting 5806. At least that's my that's my point of view. 

**Danno**
* But 5806 would be fine for verkle if we put if regular end user accounts gain storage. 

**Guillaume**
* Right. You mean in that sense?  Yeah. I mean, regular end user would gain storage. Yes.  but so you would not be able to create. Yeah. You should be able to create a contract to deploy code at this time. Right. This is exactly what,  Gary was saying, we forbid this all the way to verkle. 

**Danno**
* I'll follow up on ethe magicians or somewhere. I'm still a little concerned. 

**Danny**
* Okay, so,  there might be a couple more things to talk about here. if those are resolved, then the intention is to, add this to spectra and with a note that in the event of verkle, it's deprecated, or it would be an additional EIP at the point of verkle to deprecate. Or does it auto deprecate? Can someone clarify? 

**Guillaume**
* In its current definition, its auto deprecate.  

**Danny**
* Okay.  so it seems like there's at least a couple things that people want to still mull over.  this will likely show up again in two weeks. just bat around those hopefully final couple issues. 

# EIP-7523 [18:07](https://youtu.be/4ioJwNPe6RU?t=1087)
**Danny**
* Okay. the next one was 7523. Which,  I believe there wanted to be a final validation. There were no more empty counts on mainnet, because I think there was some unexpected ones found,  previously that were handled. But just a final check. Did anyone do that? Final check? I'm also not 100% sure who was going to do that. Okay, we'll kick this two weeks, Tim. We'll be able to carry the thread better than I. Apologies. All right. 

# Prague/Electra EL Proposals [19:01](https://youtu.be/4ioJwNPe6RU?t=1141)
**Danny**
* On to Prague, Elektra.  there was an a kind of traction feature of a breakout room yesterday.  I think there's two things we want to touch on here. One is if one or maybe two people can give a recap, if one person gives a recap, and if anyone wants to fill in the gaps, that'd be great.  also, Yoav was not able to join the call yesterday, so if you have can help give some additional context on 437 or I can't remember the number, but the native version of that.
* And open up for any follow up questions from yesterday's discussion, that'd be great. So let's start with that recap. Does anybody want to take that? 

**Vub**
* Yeah. I mean, I can just start by summarizing some of what we talked about. Basically, yeah, I think one of the big, topics then was, just, making sure we were aligned on longer tum goals of, account abstraction. basically. Yeah. Like the, so the longer just fundamental desire that, at eventually we have to have, some kind of account system that is,  like one allows a key rotations and, key deprecations, to allow us quantum resistance.  three allows, batching,  you know, for allows us allows sponsored transactions and, a couple of other smaller things. And out of those, of course, the first two goals are like very clearly not satisfiable with, iOS and, so present a pretty clear case for, for moving beyond the, or moving the ecosystem to a place where it's beyond eccentric.
* But, then this, brought the discussion to like, what is,  what are actually the means to get there and, like what? Like what are some of the specific details that are,  less, resolved here and, like what actually is a shorter term roadmap that is, like gets us goals that people want in the short term.  but is, at the same time, compatible with, the this a longer tum future.  so like one of the questions is basically like trade offs between like 2983 style design and for 4337 style design.  questions around like short terms trade offs between 3074 and I think it was 5806 which is basically yeah EOS is being able to delegate call use of. 
* From my inside of a transaction and which would essentially let them execute code. So I don't think we came to a particular conclusions on that, though. I think there is a general agreement that the longer terms stuff is something where there's a lot some kind of medium urgent need for or to try to like actually align on that and like, and sort of figure out the remaining misalignments. And then at the same time for kind of there is this short term need to improve functionality for existing users.  and that's something that has more urgency because there's a there's upcoming hard forks.  so I'm going to let, other people continue from there.
* 
**Danny**
* Yeah. Before we move on to Andrew, does anybody else want to add unless Andrew, you want to add a bit more to the recap or provide any sort of competing view on on what went down yesterday? Andrew. 

**Andrew**
* So if somebody wants to add something to the recap, please go on. 

**Danny**
* Yeah. Go for it, Andrew. Thanks. 

**Andrew**
* Okay. Yeah, I was thinking about because my worry about, 3074, is that it? Just, you use you can sign a blank cheque forever. But then I think it was, that concern was addressed recently, and now it's it's revocable.  so and lightclient during the breakout, lightclient, raised, an issue that, that raised the question that if we want to do something in the short run, then between, 3074 and the delegate transaction, 5806, we should choose 3074 because it's more generic. It allows sponsored transactions. So I kind of think if we make if we consider 3074 for Prague and, if we have confidence, then it doesn't prevent us from the end game. Vitalik.  the two talked about then. Yeah, if we have  and the 3774 is a reasonably complex proposal, but it's also it will bring substantial benefits.
* So yeah, if there is confidence, then it will not break things in the future or like prevent things in the future.
* I think we should do it in Prague. or at least consider it for inclusion. 

**Danny**
* All right. Vitalik, do you have a response to that before we move on? 

**Vub**
* Yeah. No, I mean, I think that's, like one, like, good, set of, like. Yeah. The security concern issue is definitely one of the big sticking points. And I think it's like, good that we're talking about, that we're talking about. And it made a lot of progress. I think, the other one that I feel like has been brought up less is basically that, like one thing that would be good to avoid is essentially creating two totally separate developer ecosystems for smart contract wallets and for EOS,  and like 3074 bit bytes, like the auth opcode is in its current form, fairly EOF specific. And, like I, looked at it yesterday and it feels like there's a pretty, a pretty natural path to be eventually extending it to be a smart contract, focused as well.
* But then there's basically the long terme issue then, which is like 5 or 10 years from now, there is going to be a lot of applications that have this like extra entrenched workflow where things happen using the auth opcode. And are we, like, does it feel right to have that, to have that kind of, workflow just continue to exist and be part of the EVM in the long Right? Basically, yeah. A long there's a long stream of complexity concern. And then there is it's like not an argument against 3074, but just like a thing that needs to be kept in mind, which is like the POS, the question of whether or not it should be extended to also cover smart contract wallets at some point. 

**Ahmad**
* Yeah.  so just one thing, that I think wasn't clear from the last call. I think there was a notion that, in the call,  that EOS are not, to be continued to be supported, kind of,  and I feel like this is not the way to go. This is something I wrote in the comments, but I wanted to voice it clearly that I believe that EOAS,  needs to be supported up until smart contract accounts are. Properly usable. And right now, we're not there. We need to,  if we need to keep supporting EOAS and making their user experience better, up until smart contract accounts or catch up to become user normal. User usable.  that's just what I'm what I want to. 

**Vub**
* Yeah. I mean I think there's a a lot of support for that. And I think like that's exactly why both 34 and 506 are being discussed.  and then I think one other thing that's so and that's short term. Right. I think one other thing that's important for just people listening to this to keep in mind, is that in the long term,  monologue based, if there is an end game where like literally EOAS's get removed as a protocol feature, then like that does not, that will not mean any kind of, like forced wallet change for users, right? Like if that gets done, the way that that would have to get done is basically that the eoas would, get, automatically replaced by, smart contract wallets that have equivalent functionality. 

**Arc**
* Thank you.  so, yeah, I think yesterday was a very interesting conversation and a lot of good concerns came up.  coming from the wallet side, I think one of the important things for us to say is that sponsored transactions is a very important capability. And for us at least, this is one of the big differentiating factors, between 3074 and 5806.  although they both bring value. but I think so, kind of one of the main things that came up yesterday is how could we possibly align the roadmap between 3074 and 4337 We've been thinking about this today. We came up with some suggestions.  I'm not sure they're by definition the solution, but it does feel like there could be like Vitalik mentioned, there could be good alignment between 3074 and 4337 if we make the effort to make this alignment.  and so that makes me a lot more positive about this. 

**Danny**
* A couple more comments and then I want to give you all some time to talk.  Ansgar and then Vitalik. 

**Ansgar**
* Yeah. I just want to briefly mention that,  like when we kind of first talked about 3074, three years ago, that,  at some point, of course, we kind of gave up pushing for it. But basically this kind of forward compatibility with smart contract wallet was kind of the last thing we did think about and we basically were thinking back then that we could have invokers become the de facto standards for new features across smart contact wallets and, and, EOAS. So basically like, say, if there's a batching invoke right for batching multiple transactions,  then that could also we can structure it in a way where that same invoker can also be used by smart contract wallet But that does mean
* I mean, Vitalik already kind of touched on it a little bit that we would have to be okay with the future, where for all of these features forever, we are fine with smart contract worlds having to make this extra call to the specific invoker that then does that for them or something. It seems not necessarily like a very natural flow like it. Basically it adds extra overhead forever to the smart contract world, and it's very opinionated on that side. But it does give us this kind of interoperability, and it does kind of keep keep us from fracturing these two paths. So if we want to go with 3074, I think it should really come with us with the understanding that that would mean on the smart contract world side, we also start using Invokers for for standardization for these of these features. 

**Danny**
* Vitalik, did you have anything to add before we give you a minute? 

**Vub**
* No, I did not. 

**Danny**
* Yeah, okay. 

**Danny**
* Give you a chance to add some more context around both for 37 as well as the native version and where you see this fitting into,  either the short or even the long term, in game, of a kind of abstraction yourself. 

**Yoav**
* So, yeah, I'll give a yeah, I'll give a brief overview of, and give overview, for those who are not familiar. And then we can talk about what we can do now. So we can I share my screen? 

**Danny**
* Yes. 

**Yoav**
* Okay, so. 

**Danny**
* We can see that. Sorry. Can you see it? 

**Yoav**
* So, first,  what we're trying to build in the long term is full account abstraction. And so what are we? What are we actually trying to abstract sometimes in the, in some conversations it's not clear to everyone. So our definition is, we abstract all the aspects of the account, which means authentication, meaning proving who you are, proving your identity, to the account. Then we have a authorization, which is something that usually there is a separation in every security system except the blockchain. There is a separation between authentication, authorization, like who you are and what are you allowed to do. So in EOA this is implicit. If you have the if you prove that you are the owner, you can do anything.
* Otherwise you cannot do anything. So,  it's so authorization, we have a replay protection. We want to enable parallel transactions when the order doesn't matter, for example. And we have in some multi-tenant use cases, there is a gas payment. Of course, we want to be able  to pay with ERC 20. We want to do gas sponsorship. This is a very popular feature and execution abstraction, which is execution abstraction, which means allowing things like, like batching and, like batching delegation.
* That's, the kind of thing that 3074, for example does. So we want to abstract all of this problem is that this is a this is a hard problem because,  we have to, I mean, doing a state, I think state dependent validation means that there are many ways to invalidate, to do mass invalidation and therefore to do denial of service attacks against the against the system. And the easiest way to solve it, of course, is by using a centralized relay. But that's not what we're here for. 
* So instead we need to have a complex mempool protection, something that, that allows us to have, to have a permissionless mempool and, the first, the first meaningful work in this space was, 2938, which really paved the way  to this line of thinking. And, we learned a lot. we learned a lot from it. But we also noticed that, we it hit a certain, dead end because some basic, basic account abstraction features are broken by requiring the, requiring the a prefix, which is really a must if you if you don't have this protection, then, block builders can be easily can be easily attacked by transactions that invalidate each other.
* And, the validation rules are also far more restrictive than in a more recent proposals, which actually preclude most of the, most of the use cases that we've already seen live in some 4337 accounts. So the goal of ELC 43 seven and, and later, RIP 7560 is to solve this problem. And it does so by separating validation execution. So that and since we have a separate validation stage, we can avoid many of the of the DDoS vectors without being too restrictive. 
* So 4367 was never meant to be enshrined. It's an ELC. It's an it's meant to be a test, that it's an experimental a it allows us to experiment with without obstruction or different EVM chains, without having to reach consensus on how a count obstruction works. And the focus is decentralization. So there are no centralized, there are no centralized components, anywhere in the system.
* And of course, it has some it has some limitations because it's not a native it's less gas efficient. We have to waste some gas on some on overhead that could have been avoided with the native obstruction. It cannot it cannot migrate your existing eoas. It cannot add codes. So we need a separate EIP for that. And there are already a few good proposals and, one big issue since we really care about censorship resistance is that, it's harder to support with inclusion lists if the protocol is not aware of is not aware of this. is launched, actually, here at the Eth Denver. if Denver exactly one year ago. And since then, it's been getting, it's been getting a nice, some nice traction. last time I checked, there were 3 million deployed accounts, like 11 or 12, actually 12 million user ops.
* And we see, many great projects, many new wallets being built and many projects, that use it. So it's an interesting experiment to work on. 
* What is the RIP-7560. This one is a bit, like a it's a it seems like a like like an odd animal because it's not meant for, I mean, we're not we are not, fully sure yet about how abstraction, how abstraction should work at the protocol level. 
* And yet we went ahead and wrote it. So why did we do that? It turns out that some layer tools were not willing to wait and actually wanted to have native account abstraction, a native account abstraction already. For example, ZK had it from day one starting. It also did. And the problem is that each of these, they all took ERC 1457, but they created an enshrined version of it in different ways, which in which, first of all, caused a lot of wallet fragmentation. Suddenly you have wallets like Argent that only support one chain, and you cannot use the same wallet on any other, which is of course not a great UX for users.
* And in some cases it introduced attack vectors because we did spend a lot of time on a lot of time on preventing the service vectors. And not everyone is and not everyone identifies every such case. So the solution we came up with is to standardize, like to, to have a standard version that all layer tools can use. And then, wallets only have to be written once and can work anywhere. And we can, and we can help ensure that it's, secure. So in short, it's something that's going to happen with or without us. So we might as well, help them get it right now. It's going to be it's going to be ELC 457 compatible. So on chains that they choose not to implement this EIP or on mainnet.
* It's you can use the same account. You'll be able to switch,To deploy the same account on a different networks. In some cases it will work more efficiently with the wrap.
* In others it will use the EIP. And this is all still early work. 
* So it's it's work in progress and we are seeking feedback from code devs and from layer twos. We are getting a lot of great feedback. Now all of all of this I think, is out of scope for the current discussion, because right now we're talking about what can we do for the next fork, what can we how how can we improve things? 
* And there is strong demand for the strong demand from the for some EOA improvements, the most common, the most common requirement I've seen is batching in order to remove things like the approve and transfer from air flow. So that's something that that's something that I think is a welfare addressing. And there's also things like gas abstraction, which is actually much harder to do in a decentralized way, but it's also something that is a strong demand and we should be thinking about. 
* So I think that, in this context, it's a I mean, if we ignore the really hard stuff like validation because that's where all the, with the, that's where all the, those vectors lie. So if we ignore it and we only focus on these two, then we right now we have this, we have these options. 
* We're discussing the 3074 route and the, and the 5806. So I'm trying to look at them and I see, I mean, what do they give us and what risks do we take? And so as I so as I said, the most common case is batching. And with batching is with batching, both of them can support batching. 
* Although I think that the latter, the latter is more is a more natural way to support batching because the 3074, if you have a batching invoker, the transaction actually has to contain two signatures. 
* You have a signature for the EOF transaction and, and the signature for the auth. And of course and then there's the and also the commit that is a part of the transaction. So the transaction becomes bigger which may be a cost issue on the on wallet. But more importantly who is going to sign these two transaction, these two signatures. 
* It's not reasonable to ask the user to sign the batch twice in order to submit it. So it's more likely that it will be used with a relay. So like a centralized relay is going to sign the transaction and it has to be centralized because otherwise there are a easy ways to grief it. So it will have to be permissioned in some way. And then the relay submits the transaction that submits the batch on your behalf. With a 5806. It works. It works naturally. It's just that you just delegate this. I see this is a way to run a script in your account, so the user just signs the signs, the normal transaction only once, and it runs a script that does the batching. That sponsorship is something that 3074 can do natively. Unlike a real. 

**Danny**
* Quick on on the batch call, an 3074 be used trustlessly with 4337  or does that, they at odds with each other in that. 

**Yoav**
* So I wrote a post about the synergy between 3024 and 437. They are not mutually exclusive in any way. And that's actually that's an important something. I should have said earlier that, we we need to make sure that no proposals we introduce now, no current EIPs, make it make it hard for us to do account obstruction later. And both of these EIPs are fine in that sense. They are not, nothing here to preclude us from doing a transaction later. So you can use, so you can use, an ELC 4337 account on top of it in order to do batching. But then you're basically using 4337. You're just using a you're using an invoker, but it's still going to be a 4057. Yeah. If you just want to do batching, like, you know, you have an EOA, you don't want it to become a 437 account.
* You just want to send a batch. Most likely you're going to use a relay because it's not reasonable to ask users to sign twice. Does it make sense? 

**Lightclient**
* But you can use 3074 with 437. So it's not centralized gas sponsorship. 

**Yoav**
* Actually I'm not sure I'm other than other than making it a full 427 account, which means you're no longer using it as an EOA. I'm not really sure how you're going to use, how you're going to use it for batching. I mean, if you have an EOA and you're using you're using a 437, you want to do batching. How what does it look like? I mean, what is the I mean. 

**Lightclient**
* Does the invoker not just implement implement the interface of A4337 wallet? 

**Yoav**
* You could delegate to a you could delegate to an invoker that is essentially. Yeah, essentially, like that, but it's, um. 
* Need to think about it some more, but it's, . But I remember when when I thought about it. it's not as trivial as it may sound, but it may be. It may be possible to do that. 

**Ansgar**
* Well, you couldn't have a decentralized mempool then, basically. Right? So you're still in the same position that you have to point it out. Even if you did have the same on chain logic, you'd basically have to also replicate the same mempool logic for these otherwise same problem, not decentralized. 

**Ahmed**
* I would like to address two things that I noticed on the table. First batch call. I think, the signatures can be aggregated by the wallet. So instead of having the user sign multiple times, the wallet can, make the user press a single button to aggregate and sign all of the, all of the,  all of the signatures at once. That's one thing. The second thing is

**Yoav**
* Wait, wait, wait. how if it's two one. One has to be a signature on the commit on the auth commit. And the other one is is a transaction signature. It's not even the same signature format. 

**Ahmed**
* Sir, I understand, but the the the wallet can take care of that. 

**Yoav**
* But the user. Let's say you are using a ledger using a hardware wallet. You will be prompted to a to sign twice on your ledger, right? 

**Ahmed**
* I mean, the ledger needs to start upping their like instead of like when you're pushing this to ledger to sign their needs. Ledger needs to support this new, approach, and it needs to, or it will fall behind, like, instead of having to press multiple times. Approve on ledger. Ledger needs to, batch this information in a single go and have you sign the whole thing in one go, or what's the point? That's that's one thing. the other thing that I wanted to say about the stable is the authorization is irrevocable and replayable. which is not true with the nonce, suggestion that, is going to be applied soon. 

**Yoav**
* Yeah, we can get to. That in a minute. But regarding the so regarding batching, I think what you're proposing is not that ledger will support 3074 in general, because it's hard to do it. Generally. We do not know about invokers. It means that ledger needs to be aware of a specific batching invoker, because it needs to show the user what I mean. What are you signing? So it's okay. It's okay if ledger prompts the user to sign only once and actually produces two signatures. If it knows what it's what it's signing, what to present to the user. 
* I'm not sure that every hardware wallet will want to, will want to do that, but maybe they will. It's definitely worth exploring. 
* So  regarding revocation, yes. It says if it's only valid for the next nonce, which is what, Matt just, just proposed in the chat earlier. Then there it is much easier to it is much easier to revoke all authorizations by, by just signing, by just submitting one EOA transaction. 
* Of course, there are some downsides, but it's, but it does solve it does solve this problem. It's replayable.  And it's actually a feature, not a bug in a, in the 5074 design. Some use cases, you want them to be replayable, but as soon but you but it is revocable. 
* So that's so that's correct. And  it's and in 5806 it's one time by definition, for better or worse, it's just a matter of, you know, just a just a transaction. So you have no way of making it replayable whether you want it or not. And it's and you don't have anything to revoke because it's a transaction. 
* And our sponsorship is something that, 3074 Can 3074 solves natively, but again requires again requires using a centralized relay because it's really hard to do to do to do it in a way that cannot be where the relay cannot be grieved. 
* So it's a it will require a lot of design and with and 5806 doesn't allow  doesn't allow sponsorship uh in itself. So it would need  it would need the new EIP draft, the new EIP draft. we've seen the 7949, which adds a sponsorship, but it would need since it's a transaction type, it means that, it would actually have to be merged into a 5806, which adds some complexity, but can. But then it will be able to have a gas abstraction as well. 
* So,  now there's a another use case that, that people like to talk about is, of course, is of course, a recovery. Now, a. Recovery can be the case of a lost keys or stolen keys, and 3074 does give us a way to does give us a way to recover from a from a lost key disaster. 
* If my key got destroyed, I can have if I sign the if I signed an invoker that can move the assets out of my account, I'll be able to do that as long as I haven't used the the next nonce as a. I mean, if I'm going to use the EOA as an EOA and send a transaction from it, then of course it's going to break this lost key recovery. 5806 does not enable any form of lost key for lost key recovery, but none of the proposals solve the case of a stolen key. 
* Or in some cases, you don't even know whether I mean, you no longer have the key and you don't know whether someone has access to it or not. So this one. So this this requires this requires full account abstraction. There's no way to solve it with a by improving eoas. 
* And now this is something that we sometimes, they don't pay attention to is the principle of least astonishment. It's a principle in in user experience where you want to make things as intuitive as possible to the user. And since I'm looking at I'm looking at delegation, which both proposals do as a way to run a script in your account, then what's what's 3074 asks the user to do is to sign an authorization to to authorize a script to run any time in the future or now, anytime in the future, as long as you haven't sent a transaction from the EOA, which burns the nonce. So that's, and, 5806 means just I want to run this script in my account right now. I'm going to send a transaction that runs the script.
*  And I think that the latter is much easier for users to grasp than the former, where you are saying, I'm allowing this script to run in my account now or in the future, as long as they don't say otherwise. 
* Can surprise users in some way. Now there's, another thing is complexity. And I think that, on all core devs, we often only look at, at the complexity of the client itself, which makes sense since, I mean, if that's what you're building, you want it to be simple. But I think that we have to look at the total,  the entire system, the complexity, like in a 374. 
* The implementation is really simple, which is great. It's a much better for the network, but it does. It does add complexity in other components. For example, wallets will have to whitelist, it will have to whitelist certain evokers. These, invokers are not, I mean, every wallet will have to like, audit, decide which invokers it support and keep maintaining this list. Whereas I think with the 5806, because there is a because there is no future exposure, it's much easier to, it's much easier. You don't need to maintain, to maintain this whitelist, I think. But anyway, that's the I think both proposals are both proposals can add a lot of benefits to a lot of benefit to erase. So and anyone has any questions about what we talked here. 

**Danny**
* Yeah. Any other comments for Yoav? There's a lot in the chat. Does anybody want to surface anything from there? 

**Yoav**
* Have to stop sharing it and I'll see. 

**Danny**
* Andrew. 

**Andrew**
* Yeah, I just had a thought. so in in if 3074, it says that,  a precompile was considered initially, but that as a means to prevent replace or whatnot. But it was decided against, because there is no precedent of,  precompile, with storage. But I think in, in Cancun. Oh, sorry. Not in Cancun. In Prague, EIP 30s, 7002 actually introduces a stateless stateful precompile. So I was thinking if we actually entertain this idea of a stateful precompile, can it replace Invokers?

**Danny**
* Quick, 7002 is going to be migrated to look more like, the beacon root opcode EIP such that it would be a pre-deploy, essentially a system smart contract. 

**Andrew**
* So it won't be a stateful precompile. I see, but say like, if the concern is that we that smart wallets have to whitelist invokers, so can 3074 be redesigned, perhaps with a state for precompile so that we don't like we have a kind of a standard invoker. Or maybe there is no need for an invoker at all. 

**Danny**
* Like Lightclient or anyone an author on that one. Want to take that? 

**Lightclient**
* Yeah, I mean, it's definitely a possible avenue, and that's the only way that we can improve. It was maybe it's something to discuss, but I think it just goes against my philosophy and probably some other people's philosophy about what we're trying to provide to developers, which is a powerful framework for building applications. If we have a pre-deploy, which is the only context that ought an auth call or available to be used, and it's something that the the all core devs group is dictating, then I think that we're going to miss out on some innovation that could happen,  at this layer. But again, like if that's what we have to do, then maybe that's what we have to do. I just personally don't think that's the best path to go down for 3074. 

**Danny**
* Gary. 

**Gary**
* Yeah. I'm wondering.  since you've didn't really speak to, 7377,  it seems to me that 7377 is a much lighter touch approach for enabling account abstraction and kind of getting users from EOAS  to a smart contract, account abstraction, you know, future. And it allows, you know, for 4337 can develop in parallel. And this doesn't have to be enshrined, early. You know, it's what we're trying to target for Prague is light fork. And it seems to me that at least 3074, and 5003 in combo would, that create a lot of test, and kind of attack surface that we need to, be careful about and that starts to grow. The fork starts to grow the Prague fork.
* It seems like, in my opinion, 7337 is really the the approach that is,  you know, light touch enough and still future forward. but also includable in Prague without making this into a larger feature fork that is kind of against the the principles of what we set out for having a small feature fork before verkle. 

**Yoav**
* Agree. I agree this, this is something that is orthogonal to the other two proposals. Maybe I should have talked about it separately. And it's, because 4337 or even 756, we currently don't talk about migrating and existing EOA and adding code to it. And the end game for account abstraction does require a solving this problem as well. So yeah, if it's possible to include an account migration EIP, then then I think we should consider it. 

**Guillaume**
* I only have a side note for something that had been said before. Maybe, if Vitalik wants to talk to address what Gary said, he should go first. 

**Vub**
* Yeah. I mean, I think, just the kind of response to the general idea of, like, why not? Basically, yeah, give up on, eoa improvements entirely and, try to fast track, making,  like, making it easy for, existing airways to participate in four, three, three, seven.  I think,. Probably the biggest objections to this are,  I mean, one is I mean, of course, there's,  kind of like general,  you know, like fear of new things,  and, but that's something that's just like, so continues to be being, being de-risked with, with every passing year. But another, a really substantial one is, higher gas costs. Right so 437 does have significantly higher gas costs than EOS always do.
*  And this is something that's sort of in some sense in principle should not be true, because you could have a 4237 account that's like literally running the same workflow as, in EDSA based EOA. but, in practice, like basically, yeah, EOA gas pricing is, cheaper than,  the storage operations of 437 does and I think, as I mentioned, in the chat, the this is something that can be fixed by, like basically overhauling the gas cost system and replacing it with something more principled that, charges for storage accesses in a neutral way. And the Verkle tree EIP actually does have a component which does exactly that. And so that's, I mean, that so that so that's one big thing.  but like the ver but that kind of, goes against the idea of like doing something that gives users functionality that becomes available pretty quickly. And, before Verkle trees do. 
* And then of course, the other one is just like cross layer two stuff, right? Like whatever. You know, if, L1 has, amazing,4337, but like but layer two is did not done that. That's also an issue. And like also a thing that's going to contribute to like time delaying any attempts at like very rapid, attempts to get everyone over to smart contracts. 

**Danny**
* Guillaume. 

**Guillaume**
* Yeah. So just a side note on what you said earlier, that there was another contract that was going to be deployed.  the 4788, I think way

**Danny**
* 7002. 

**Guillaume**
* 7002. Yeah. Right. Exactly.  the the issue with this, that might not be clear to everyone, but it's going to have a huge impact, okay. At least to have an impact in Verkle mode is that if you start deploying contracts that are part of regular block execution,  you find yourself adding code chunks to the witness. and so the choice actually no longer exists whether you want to, use the to solid or the EVM bytecode compiled version, or if you want to take the shortcut and go right directly into the the contracts memory.  I don't think we should discuss this right now. I'm just pointing out you might want to hold, hold off your horses on this one. on. Because I think, for 788 should be, I mean, the contract should still exist, but the execution, the bytecode execution should actually be removed so that,  so that the the witness gets smaller. 

**Danny**
* I guess I kind of see that as a feature. Like when you put anything into the EVM here, then you just get. You get it by default, but, um. 

**Lightclient**
* It does just kind of suck to send the exact same bytes around the network every single block, you know? Like if people are interacting with that contract. Yeah, it makes sense. But if it's something that we as the developers of the protocol just sort of enshrine this shackle on our witness, it's a little unfortunate.  I mean, 4788 contracts is 86 bytes or something, so it's not a huge deal. It's just a weird thing. 

**Danny**
* Sure, but if you don't, then you're now it just becomes an additional input to the state transition, right? That you have to be carrying around. I mean, maybe blocks rather than just one? 

**Lightclient**
* Well, it's not a function of passed blocks. It's just enshrined in the client. Like the code just lives in the client. 

**Danny**
* Okay.  we can pick that up another time. So we are at the hour.  There is a desire potentially to get small versions that iterate us towards,  improvements here. It's very unlikely that in the next fork that we're going to hit some sort of I think it's maybe I'll change that from very unlikely to impossible to hit our kind of final construction goals.  I do think in the next couple of calls, we do need to hone in on if there's going to be 1 or 2. I won't even some amount of small,  EIPs. So we're going to have to pick up the conversation again.
*  I think also in parallel, there's a renewed vigor to try to hone in on on what does the short, medium and long terme look like, and to make sure that both the EIPs that we might consider today, as well as we want to layer in over time,  do help us get there. So let's keep the conversation going.  I don't think we're going to schedule another breakout at this point, but it does seem like there might be an appetite to be regularly touching on this outside of all core devs.  so,  we'll throw this on the agenda in plus two weeks to at least think a bit more about the strategy and to consider a couple of discrete EIPs. Thank you everyone.  we do have half an hour. We'll try to get to what we can.  

# EIP-7623 [1:04:58](https://youtu.be/4ioJwNPe6RU?t=3898)
**Danny**
* Next up was EIP 7623. Tony was going to give us a view on this increase call data cost. 

**Toni**
* Yeah. Hi, everyone. Thanks, Danny.  I will be very quickly. 

**Danny**
* So your mic was really bad. I think maybe it's a little bit better, but make sure you're talking into it. 

**Toni**
* Okay, let's I hope it's gonna. It's better now. 

**Danny**
* It's worse now. 

**Toni**
* Let me check. 

**Danny**
* Maybe you're going through your computer instead of your headphones or something like that. 

**Toni**
* Better know. 

**Danny**
* Seems pretty bad. Pretty bad. 

**Toni**
* Test. Test. 

**Danny**
* Crunchy, but much louder. It might be doable. 

**Toni**
* Okay, let's try it.  yeah. So basically is the goal of the ERP is to reduce the maximum possible block size by increasing the cost of call data.  particularly for non-zero call data bytes.  it does so by increasing the cost for call data for those transactions that are mainly using Ethereum for data availability. And you can you can look into the ERP. It has this conditional formula. So with a floor and a standard token cost. And if you spend basically enough, gas on EVM operations then the call data cost will be yeah, it will remain at 16 gas per call data byte. And otherwise it will be at 68.  
* Yeah currently, the maximum possible block size is around 2.5MB, something like that. And with that EIP, one could reduce it to around 0.5MB. I just posted a link into the chat so you can see a lot of more details, some analysis which accounts are affected, but basically,  normal regular users wouldn't be affected at all, so they would just continue paying 16 gas per call data byte while the data availability users would pay 68 gas per call data byte. And I did some quick analysis for,  the last 12 days. And it looks like that around 96% of the transactions would have remained unaffected, which means only 4% of them would have paid the 68,  gas call data, and most of them are data availability or users writing comments in their call data. And those 4% that will be affected.
* It's basically 1% of the users, and the large chunk of them is using call data for data availability. 

**Danny**
* Are there any clever ways to try to get around this, threshold, like batching across multiple transactions or just the 21,000 hit break, break such strategies? Or are there any other things like that under consideration? 

**Toni**
* I've actually not thought about,  batching. I don't think you should be.  you should be,  there should be a possibility  to get around that. So the only way to get to the cheaper price would be to spend money on EVM operations, which is then. Yeah. Counterintuitive. 

**Danny**
* Great answer. 

**Ansgar**
* Yeah. I just want to say that I'm strongly in favor of shipping a,  kind of call that a price increase in general. in the next fork,  so that we can limit the, the kind of maxim worst case block size. And in this case, this would be does this,  very well by really by going down from three megabyte maximum to 0.5MB, which of course is a huge improvement.  and that way it would give us also room to include an EIP to increase the quota for throughput, like I think, I mean, ideally, I don't know, depending on how stable. Then it turns out after we ship Tennekoon, ideally, I think something like 8616 or so would be a good target, which still would increase, would result in a lower maximum throughput than than we have today.
* I do think kind of this question around this, this, this mechanism for, for basically rebating, I mean, I know it's a bad word, but Rebating basically kind of the cost, the cost for call data if transactions also consume more normal.
* I think, I think it's interesting. I could imagine that this is a bit more contentious. So maybe like this is in a way like an optional part of the in my mind at least.  but but it's actually a very clever mechanism. And just to give a little bit more context, right. Like so in the past we've looked into multi-dimensional resource pricing, and the idea is that it's kind of unfortunate that we always price things for the worst case. And the worst case is that the block only consists of a single like only consists of using that one resource. Right. So basically we price compute for the worst case block processing times. 
* If you only use compute operations and we price data for if you only have a block that's full of data and we price storage for if you only access storage like multiple times in a row. Right. And the beautiful thing here is that basically now it it still has this high price for, for that bad case, for the attack case basically. But it gives you lower prices if you actually have a much more realistic mixed usage block. And this is actually a mechanism we might be look, look into applying even for other types of resource mixes as well. Basically, it's a way of kind of elegantly, making, making the total kind of resource usage in a more efficient. So, so I personally like that part of the mechanism as well.
*  But I feel like basically, even if people might take issue with that part, I think shipping any form of call data price increases is very important for the next four. 

**Danny**
* Any other comments or questions? I'm not sure if client's  team had a chance to look at this before any initial reactions for consideration in the next work. 

**Marius**
* And so I've implemented in Geth and it was like a five line implementation. I did make some mistakes. Thank you, Vitalik, for pointing them out, but. Yeah, I fixed it now. 

**Danny**
* Glad we have good code reviews.  any other initial reactions?  if not, we'll probably give everyone a couple of weeks to chew on it and bring it up for more reactions. And plus two weeks from. Okay. Thank you. Tony.  

# EIP-2537 [1:12:36](https://youtu.be/4ioJwNPe6RU?t=4356)
**Danny**
* Next on the agenda. Antonio did put, uh. EIP 2537 on up for discussion. I'm not certain if he had seen that it was already slated for inclusion in the EIP.  Was there anything else we wanted to discuss on 2537, or was that a. 

**Antonio**
* Yeah. can you hear me, actually? It was. 

**Danny**
* You sound like you're in an echoey, far away room, but. Okay. 

**Antonio**
* One second. 

**Danny**
* And if you can't get the mic working, is there anything else you want to discuss other than just see if it was going to be included? 

**Antonio**
* Yeah. Is it better by chance? Yes. 

**Danny**
* Yes. Great. 

**Antonio**
* Yeah, actually, yeah. I mean, finally this, this, EIP seems to be like getting traction and, actually, I will have a some folks, meet, me and some other people started to look at the this, text more in depth. And actually, I will have a question, if you guys have an opinion on kind of, not an issue, but an implementation choice, basically like, this, specification is pretty different than, EIP 196 in a way. because like, we have operation like Add and scalar multiplication like the BN curve, but that the BN curve is a prime order curve. 
* And this one instead is not so it's cofactor, so now while it's clear that for pairing, we want to do the operation on the magic subgroup, the one that we are using, in the consensus layer, it's not clear what we want to do for the scalar multiplication and the addition, for this EIP, if you want to stay on the on the magic group or acting on the full order of the curve, and if we choose to stay in the group, we have to pay a bit the price of the validating the points. So this is pretty actually, I've been writing start to read the test for this, specification, and it's not clear at all what would what we want to do here. And I was wondering if anyone has an opinion.
* Just like to give another perspective in the in the consensus layer, we don't have this issue because we are using only the BLS, signature scheme. But here we have as well adding points and scalar multiplication. 

**Danny**
* If no one has any any comments here, maybe it's best to write this down and see if we can get some view on it in the next couple weeks. so, Antonio. 

**Marius**
* Right now, we're right now, all of the libraries are using the AI are doing the subgroup check. Right? At least that's as far as I saw for for pairing. 

**Antonio**
* Yes. For for like the, the operation of adding and scalar multiplication. Not all. And for sure it's not specified by the spec at the moment. But I agree with Danny that we can talk about it offline. So maybe I will open an issue on the repository. 

**Danny**
* Okay, that'd be great. Marc has his hand raised as well. 

**Marc**
* Yeah. I just wanted to add one thing on this EIP,  that I felt that maybe,  it was missing the op, the ability to do operations in the result of the parent group. So at the moment, you can do operations in G1 and G2, but then you can't and you can verify,  the result of two pairings are equal, but it doesn't let you do, to get the pairing result and do a further arithmetic on it,  which is useful, I think, primarily for verifying some like aggregated snarks. So I felt that this would be an improvement to the EIP. 

**Antonio**
* All right.  yeah. I will suggest as well to, like, maybe discuss this on the, on the GitHub and, we'll follow up there. 

**Danny**
* Okay. Yeah. I think to get the right set of eyes on this, a written version of it will be helpful. Thank you.  before we move on. Charles wanted to bring up both EIP 5920 and EIP 7609. Both these were discussed on a previous call. but we're looking for, a revised kind of temperature check if anyone, client teams had, given them more thought or, wanted to bring in any comments on those. so EIP 5920 is pay opcode. Any any comments or further thoughts on that since it was brought up? 

**Marius**
* Yes, we kind of, had a team meeting with, the ELs team and the East team, the execution executable execution layer specs and the executable tests, no spec tests. And, one of the things that we did was sit down and talk through a random EIP, and we picked the pay, opcode and kind of discussed all of the. All of the implications it has and, all of the contexts that it can be,  that we need to think about, that we need to test when, when, when doing this EIP.  and it turns out it's quite complex the testing, the ERP itself,  was underspecified, but I don't know if Peter is here, but he wanted to add some more specification to the EIP.
* And  and yeah, in theory, I think the EIP is okay.  it's just a lot of stuff to test for it. 

**Danny**
* Okay, and is does Peter intend to do the revisions? in a PR. 

**Marius**
* I think. 

**Danny**
* Danno. 

**Danno**
* One minor thing is that,  the pay op code and the auth op code are currently slotted for the same OP code number, so that needs to be resolved. Got it. 

**Danny**
* Any other temperature checks on this one? 

**Marius**
* For the transient storage pricing. I don't think we should do it. we should even think about it before we have the transient opcode in the chain and see how it's used. And then we can start having a debate whether it's mispriced. Well, we should have the debate whether it's priced too high right now, too low right now. But,  I think this, this, EIP actually wants to  price it down. 

**Danny**
* Okay, well, we will begin to have data in 14 days. 

**Charles**
* I think. Please. Sorry. Yeah, I think,  it's good to wait for data.  but the data won't be complete in the sense that there's use cases that revising the pricing down enables, which you won't see in the data. So I mean, you can kind of get some benchmarks or some ideas how much,  resource usage you get, but you won't get clear idea of like how it will be used after the pricing change vs before. And one very important use case is re-entrancy locks. So, Viper would like to enable non re-entrancy locks by default.  It's like kind of iffy whether that makes sense if t-store is 100 guess. But if tstore is cheaper than it's pretty much a no brainer. And I think that's a big step forward for,  smart contract development UX on Ethereum. 

**Danny**
* Were there any other thoughts or comments on 7609? I guess one we can get data on usage. Yes, that will be incomplete with respect to potentially not unlocked, use cases, but also I'm. I'd rather tend to be here,  on either of these to kind of. Better gauge consensus. But but any any other comments on this before we move on today? 

**Charles**
* Sorry again, but I'd like to also point out that the EIP actually improves resource usage,  in that for small number of slots the pricing is cheaper, but it actually caps the amount the number of transient slots that can be used at a at a much lower number. So you go from being able to use like I think ten megabytes with the current pricing to under one megabyte after the after the pricing change. 

**Danny**
* Sorry. And this is just a function of the pricing change or is there another change? 

**Charles**
* It's a function of the pricing change because the pricing is super linear, so it's cheaper for small numbers of slots and more expensive for large numbers of slots. 

# EIP-7639 [1:23:29](https://youtu.be/4ioJwNPe6RU?t=5009)
**Danny**
* So. Okay,  we're going to move on. lightclient. I did not get this on the agenda. I didn't see it this morning. EIP-7639 serving history before EOS. can you give us some context here? 

**Lightclient**
* Hey. No worries.  yeah. So this is really a splintering of EIP 4444. I don't think that we are proposing for 4444s to be completely realized in the next hard fork, but there does seem to be quite a bit of demand from client teams to improve the situation with how much data they are required to store on disk. And since we have been working quite a bit on a standardized format for sharing Pre-merge history, I think that trying to target this next fork as a time where we can stop serving that pre-merge history over the network is a pretty good direction to begin looking.
* And I just wanted to, you know, get it on the call now and to start discussing it a bit and see if that, see what the appetite is from teams to maybe make the commitment that  in 6,9, 12 months that it's not going to be possible to get that information over P2P and you will have to use some external data source. 
* The other big piece of this EIP, which I think some people have left some comments on the PR, maybe we'll split it into a slightly different thing that I think is important to have a green light from ACD is this header accumulator. The header accumulator is really a interesting pre-merge, interesting pre merge data artifact that is inspired from the historical roots accumulator on the consensus layer. And it just gives us an efficient way to communicate about the entire pre-merge chain with just a hash tree root and then make proofs about, about  the history of the pre merge chain in log size rather than in linear size. So I want to get agreement both on. This is something that we want to do.
* We want to try and stop serving this data over the P2P in the next hard fork, and that we have been able to verify that this is what the merge chain looks like. So in a sense, we're like committing to a later,  authenticated route per se of the chain. 

**Danny**
* Sorry, and I haven't looked at the EIP. Where does this. Where would the the Pre-merge route show up? This is just baked into the client. Or is this some sort of state transition change? 

**Lightclient**
* Clients want to do with this, given that there will be other ways to access the data. If your client is going to still provide users the ability to download that historical data, then it's going to be important for client binaries to include that route hash and then verify the data that they're downloading is authenticated against that route hash. 

**Danny**
* Okay. So this just defines a canonical way to kind of come to that root hash dictates that root hash in CIP such that it can be easily included in agreed upon in binaries. 

**Lightclient**
* Yeah, exactly. 

**Lightclient**
* I don't know, this could. Possibly live outside of an EIP. It may definitely live in a different EIP, but I think it's probably important that if this is the user story we're going to provide for downloading history, we should probably, as a group, agree that that's the route that refers to the data before the merge. 

**Danny**
* Let's see. Any questions for lightclient or any,  initial comments or temperature check on this? 

**Mikhail**
* Yeah. I assume that this,  also about not just blocks, but also receipts, right? Like, all chain data before the merge. So I just wanted to say that probably this EIP is kind of, like, dependent on something like 6110. Yeah. And I mean, like, because otherwise some SEO clients will not be able to reconstruct the deposit tree,  because they will, logs will no longer be available. 

**Danny**
* That's true. Are there any other consensus on either consensus or exclusion that, requirements on logs. Was it the single? Okay. I believe that's the single thing. Okay. Anything else on this one before we move on? Seems like something that, is worth chewing on and surfacing in a call or two, to see if there's any additional consensus here. Okay Mikhail engine API and Json RPC changes. 

# Engine API & JSON RPC changes [1:28:38](https://youtu.be/4ioJwNPe6RU?t=5318)

**Mikhail**
* Yeah. So I want to quickly talk about  engine and JSON, RPC API changes,  potentially entailed by the confirmation rule. The confirmation rule, as a reminder is, a SQL construct that under certain assumptions, allows to, confirm a block within one slot, confirmed block. Yeah. It's assumed that the confirmed block will remain canonical, will remain in the canonical chain, and eventually get finalized if those assumptions are true. 
* So this is kind of like, quite, cool feature for the dapps and services that use, blockchain data, to get early block confirmations.  and, yeah, obviously we want to expose this information somehow to, to those, parties who use, who work in DApps and services and the way, that is kind of like, we can do it is to basically, take the, confirmed block hash from CL and, propagate it to EL, as we do with the safe block hash and expose these confirmed, block on the, from the outside via Json-rpc API. 
* So this basically like the default, way to do it. And, yeah. there are a few discussion points. Due to a lack of time, I think we can, go over them, later on, on some later calls. I just wanted to, say that, potentially, if we decide to you know, to propagate this information and to expose this information to users in this particular way, we'll have to do these changes to the APIs. And, considering that the confirmation rule research is being finalized and, then, we'll be able to, to finish this back work, which has already been started. 
* I anticipate that this kind of change will probably be required, as a part of our work on electro prog. And I just wanted to raise developers awareness that there is. Yeah, potentially we will have this change, alongside to other EIP. yeah. And I can answer some quick basic questions, if there is time or we can move the discussion to, you know. Right. 

**Danny**
* And there is a path where the execution layer can be not care about this at all. And it's the requirement where you just get it from the RPC on the, consensus layer and then utilize that hash,  for queries on the execution layer. 

**Mikhail**
* Yeah, exactly. But, probably, beacon API's aren't, the thing that is commonly used by that developers. Yeah, I don't know. I don't want to claim this. This is more like a question to me. So, 

**Danny**
* There are plenty of places where they're not accessible or just not commonly used. that's certainly correct. 

**Mikhail**
* Yeah. We could also, use a saved block cache, change it to expose the confirmed block, but, it was a kind of a point that the saved block cache probably is treated by people, more as a more safe, you know, block reference than the confirmation rule can provide. So this is why we would probably want to have a new thing. 

**Danny**
* And that was the intention. but I think given the use of that word safe, which was probably an abuse of terms to begin, most people are not, my temperature gauge on that has been, people are kind of afraid to to undo that also, given that this might be rolled out at variable times,  the confirmation rule, then all of a sudden, depending on the client you're using and,  the version you might end up safe might have very, very different meanings.  okay. let's pick this up either on the content of their call and the execution, their call next time.  thank you. Mikhail.
* And the final thing is there will be a lightclient breakout room on March 6th at 2 p.m. UTC. There is a link to this agenda in the PM repo. this is issue 971. Any other notes on that? Phil, you would put on the agenda? 

**Phil**
* Nope, that pretty much covers it. Thanks, Danny. 

**Danny**
* Okay, great. Well we are. Any final comment? We have 30s. 

**Marius**
* Yes.  I would like to propose a new ETH client version that, where we don't send the bloom filter in the receipts.  basically, we figured out that, no client is actually storing the bloom filters for the receipts because this data is for the 2.5 billion transactions that we have right now, or 2.2 billion transactions right now.  
* This data is roughly 550GB. And the problem is, whenever someone syncs,  we will request the receipts with the bloom filters. So the person that we're thinking from has to pull up the receipts from disk. generate the bloom filters, send it over the sinking node verifies that the bloom filter or the receipts are correct, and then deletes the bloom filters and stores everything else to disk. So instead of that, we can just send the bloom filters with the receipts without the bloom filters. 
* And the the node on the other hand, has to then generate the bloom filters themselves and not store them just to verify them.  this would, save us roughly 550GB, of bandwidth during initial sync and also a bunch of bandwidth during normal block. 
* Oh, actually, no. During normal plug production, we generated ourselves so it wouldn't save us any bandwidth there.  but yeah. So I'm preparing an EIP for a new Eth protocol version. I can send the link of the draft, and this will also remove, this will also remove to other messages and  the total difficulty from the handshake because we don't need the total difficulty in the handshake anymore. 

**Danny**
* Okay.  let we're going to keep an eye out for that. EIP. Circulate the draft. Andrew, I see you have a comment, but I have to go. I'm sure a number of others have to go. Um. Uh. Take care. Thank you. Everyone. 

**Marius**
* We can discuss on discord. See you. 


-------------------------------------
### Attendees
* Danny Ryan
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
Mar 14, 2024, 14:00-15:30 UTC





