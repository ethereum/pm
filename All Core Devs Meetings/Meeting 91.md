# All Core Devs Meeting 91 Notes
### Meeting Date/Time:  Friday 10 July 2020, 14:00 UTC
### Meeting Duration: ~ 1hr 40 mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/192)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=RUZ3eJ81c0k)
### Moderator: Hudson Jameson, James Hancock
### Notes: Pooja Ranjan

---

# Summary

## EIP Status

EIP | Status
--|--
EIP-2718| Discussion to be continued.
EIP-2711|Discussion to be continued.

## Decisions Made

Decision Item | Description
--|--
**91.1** | EIP-2718: Discussion to be continued on discussion forums.
**91.2** | EIP 2711: Matt and Jason to continue the discussion on timestamp version.
**91.3** | Network health: Discuss strategies on the adoption of client diversity. Discussion to be continued in the next meeting. 

---

**Hudson**: Hello everyone and welcome to meeting 91. Today we're going to have James Hancock running the meeting so he'll be the host. So I'm going to just be recording today and with that I will pass it over to James.

**James**: Thank you, Hudson welcome everybody! We have a little bit of EIPs discussion  that we're going to have in the beginning and then will continue the discussion on Network health and I would encourage everyone to go and listen to cuz it's an important meeting for the network.
# 1. EIP Discussions
## EIP-1559 Updates

Video | [5:25](https://youtu.be/RUZ3eJ81c0k?t=325) 
-|-

**James**:  The first is EIP-1559. 

**Tim**: I can give a quick update. There was another implementers call if people want details, can [watch](https://www.youtube.com/watch?v=2qDfW83gnDA). But in short, The two big updates are that 
- team started working on a **1559 testnet** between Geth and Besu nodes. Good progress with that. Besu part is set up and adding the geth node. It should be up in public in the next week or so.
- In parallel, we're to reach out to people to looking to get  a **formal analysis on mechanism/design** of the EIP to prove it's goal. This is something that a lot of the people in the community wanted to see given it is a pretty significant change.

Will have **next implementers call in next couple of weeks**. 

**James**: Great! Most of the discussion if people want to follow along is happening in the Eth R&D discord in the 1559 channel. 

## Account Abstraction Updates
Video | [6:50](https://youtu.be/RUZ3eJ81c0k?t=410) 
-|-

**James**: Next item on the agenda is the account abstraction updates. Is Will up here?

**Ansgar**: Will couldn’t make it, unfortunately. I’ll provide the update. Hi everyone, I am from the Quilt team. Earlier this week, we 

- [published a playground](https://github.com/quilt/account-abstraction-playground), briefly wanted to announce that. It is based on MVP, Account abstraction implementatipon in the geth implementation, on those implementation together with Solidity, example contracts and tutorials. Anyone interested can play around with it.
- Want to add some clarification, account abstraction has been around for a while and that been a valid concern in the past on performance and network stability. We do think that this simplified proposal from the earlier Vitalik's account abstraction might address these questions but we're still in the process of perfomance testing, collecting metrics. This playground is not suppose to answer these questions as it is just a byproduct of the work that we're doing there.  Once we've the result, we will have a dedicated writeup and that might hopefully be the basis of further discussion on that. 
We just think it's worth looking into what's coming from Eth2 execution, research, context and the pass that was usually phase2, but now it looks like there might be intermediary phase 1.5 situation where we will have EVM running on one of the Eth2 shards. So, we are jsut interested to see is it feasible to bring some of these features that were discussed in the Eth2 context like Account Abstraction. WOuld it be feasible to bring it to Eth1 EVM?
We are mindful of the contraint of the network and we don't want to be disruptive, we just want to help explore these questions. 
If you've and feedback and criticism, you can find us the EthR&D discord Account Abstraction channel there. That's all from my side. 

**James**: Great, where can we find the GitHub link?

**Ansgar**:There's a link on the Discord but I'll also put a link to the call notes of this call on the [GitHub](https://github.com/quilt/account-abstraction-playground).

## [EIP-2718](https://eips.ethereum.org/EIPS/eip-2718) Further Thoughts

Video | [9:50](https://youtu.be/RUZ3eJ81c0k?t=590) 
-|-

**James**: Next we have Matt with light client with the EIP 2718 further thoughts and EIP 2711 introduction.

**Matt**:  Yeah just to reintroduce 2718 real quick it's the EIP for Type transactions envelope and essentially this is going to make it easier to introduce new transaction variance into the network.  The way that we're proposing this to happen is we’re going to create an RLP  in two floors, the first element will note the transaction size and the second element is raw bites that will be decided based on what the transaction type is. We talked about it in the last call, that’s two weeks of the time period if anyone has feedback for this EIP. 

**Piper**: We have a little bit of discussion yesterday in the channel that sort of uncovered a couple of things.  Basically looking at that,  it does need a fork block because it's going to change things like the header field have a transaction route, it's going to be computed. And then I think that there's some complexity for us to dig into about supporting essentially the historical Dev P2P protocol versions because when we released this first transaction type it'll still be possible for clients to continue supporting. Essentially once the new transaction type is in place all of the Dev P2P messages will need a new deal that transactions have to be updated and that'll be fine because it means that the client can still support old versions by essentially reversing,  you can convert a type 0 when it's the Legacy transaction type. You can blindly convert it back and forth between the two formats, which means that initially will be able to still support the old Dev P2P like an old version because new transactions can be downgraded to the old format but as soon as we introduce a new transaction type beyond the initial one that's supporting the Legacy format, it'll officially deprecate all of the old Eth protocol version because it won't be possible to broadcast transactions are blocks in the old version and that's something that I just realized this morning and that we need to think about. I don't see it as a blocker at all but it's just something that wasn't initially occurred to me.

**Matt**: Okay, I am not an expert at P2P but my understanding was it is blocks and transactions, is kind of like opaque data structures that defined by the protocol and so if out of forks blocks, we decide to leave that using the transactions, the legacy transaction list of the new one would not allow all the P2P protocol to continue operating by just serializing whatever the protocol is best defined as the transaction.

**Piper**: It would mean the only way to do it would be for legacy clients to actually change what those old protocol versions mean and so you would have to essentially make like a backward-incompatible change to an existing protocol version and I think that would cause a lot of Chaos on the network.

**Matt**: Yeah.

**Piper**: I don’t see this as a blocking issue, but I do know that there are you know a lot of Eth63 clients out there still on the network. I'm not sure about clients that they're using version before Eth63 but basically, once we introduced another new transaction type it isn't compatible everybody it's on an Eth protocol version before might be Eth66 or 67, I'm not sure would no longer be able to receive new blocks or transaction pool information.

**Martin**: I don’t really understand why it would be so. If a protocol declines, the response to this message should be a list of transactions we've been modified the potential for how a transaction might be serialized. I don't see why we need to change the encompassing protocol.

**Piper**: so I guess my intuition there was that the Dev P2P specs for like Eth63 have a definition of what a transaction looks like. Actually define things like the fields and stuff that go into like the transactions message and so we would be making,  one version says okay transaction and coating looks different so this is propagated backwards through all of the dev P2P messages in historical dev P2P versions. The other version says, those versions already exist and so we can’t change the transaction format, we need a new protocol version that has this new transaction format. I’m not saying one of these is right and the other is wrong. I was leaning towards the latter if it felt like you know respecting backwards compatibility, but I'm very open to discussing either of those.

**Matt**: Is it correct to say that the DevP2P Protocols are tied to a specific transaction type? that's kind of what it sounds like they are, then that makes sense that we potentially be still breaking change to pack version but if they aren't tied to a transaction type, that’d lead me to believe that upgrading a transaction type would just be propagated old ones without a problem.

**Piper**:  I think that's the question that we need to answer and we don't have to do it here on this call. I think just the fact that like getting this in front of people is really what I wanted to do. so I think that we can **continue** figuring out what we want to do in **discussions on other forums or EthMagician forum**. 

**Matt**: Yup, thanks! Any other comments or feedback on 2718?

### Decision Items

-**91.1**- EIP 2718: Discussion to be continued on discussion forums. 

## [EIP-2711](https://eips.ethereum.org/EIPS/eip-2711) Introduction

Video | [16:46](https://youtu.be/RUZ3eJ81c0k?t=1006) 
-|-

**Matt**: 2711 is a new general transaction type that going to add a lot of functionality that people have requested in the past. This  is going to be built on the framework that 2718  is providing. 

There are  three main features that we're looking to add into this transaction type 
- the first one that spawned all these ideas was introducing something **Sponsored transactions** which allows for a transaction to be paid for by a user other than the actual user who will be represented as the call at the transaction. and this is going to allow something that is really not possible in the protocol right now. It’s going to give us a lot better Meta transaction at the protocol layer rather than meeting to do some sort of issue recover during smart contract execution.
- The second thing it’s going to provide is **Batched Transactions** and so this is going to let us have stronger guarantees about having sequential transactions, maybe if you want to do approve a transfer flow and so this is going to provide strong entries of those sequences of transactions those are being included at the same time. We also think that this is going to help improve the reintroduce the ability to make you parted calls, sub-calls and this is something that came up in Eth1x call, a couple of weeks ago. Regarding a proposal to possibly removing of the severability of gas. With the batch transactions that provide that again. And there's another EIP that's still being formulated EIP 2733 which would give a return data to pass between these transactions. So that way you pick how to build a batch of transactions that depend on some output transactions. And this is kind of similar how sub call work today but this new Batched version would work even if the batch is not executable during the EVM version. 
- The third main thing is **expiring transaction** and this is just going to allow a transaction to become invalid after some time stamp has passed. We’re just using the time stamp that are just provided it in Block headers.

These are the three main things about the EIP 2711 that's going to be introduced. I put an Eth research post a few weeks ago, just comparing some of the different approaches to the protocol by the transactions which kind of addressing the first feature of this transaction. People can take a look at that if they want to see what else is out there. I don't want to take too much time but if any feedback, definitely appreciates that. 

**Jason**: There might be interest in doing a block number and so timestamp version of expiring.

**Matt**: Yeah, definitely. Just quickly the reason that it isin’t the rationale  that the author has decided to use time-stamp instead of block number is that timestamp is easier,  easily accessible offline.

**Jason**: We can talk about it too.

**Matt**: Sure.

**James**: any other comments on this? Thanks for introducing this Matt.

**Matt**: Thanks for let me introducing this, James!

**James**: Yeah, it’s been great having you around EIP stuff. Thank you very much.

### Decision Items
-**91.2**- EIP 2711: Matt and Jason to continue the discussion on timestamp version.

# 2. Network Health
Video | [21:05](https://youtu.be/RUZ3eJ81c0k?t=1265) 
-|-

**James**: The next on the agenda is the network health and is in continuation with the last meeting. It’s the combination of how we move feature forward and some of the weight that is on the client teams and perhaps what are things you could do about it. I'd like to start by I believe Alexey is here. Alexey brought this up on the all core devs Channel, I think. I want to give you a chance to introduce and to reflect since the last two weeks if anything has come up and then Piper has written a great post that had a lot of discussion on it. so I would say to move it to him after that. 

**Alexey**:  Yeah, thank you I don't actually have a lot to say to be honest.  We kind of looked back and I think I agree with Piper that we probably talked a lot about potential Solutions without spending enough time on actually dissecting the problem. So I'll probably just going to pass the microphone to him to kind of to contribute. He wasn't unfortunately on the last call but he wanted to join this one, so I would just let him speak to what he wants to say.

**Piper**: Already, without further ado,  so let's see. Sorry for not being on this last week’s call but I did listen to it, and I do appreciate all the discussion that happened.

I spent some time trying to think through this because one of the guys who has been doing technical writing for us, Griffin posts this wonderful thing from Harry Potter and the methods of rationality, putting about groups getting too quick to focus on Solutions before digging into the real problem and when I listen to last week's call, that sort of what it felt like to me. you know I think the discussion was great I just felt like it got some of the directions that it went to didn't like lead towards what I felt more like actionable things that we could fix. So like there was talk about you know Geth having a head start on everybody and sort of like can we do supports minority clients better and help them catch up. I had a high-level seems like, okay well maybe we could do that we could get other clients on the network but when I really look at that we've had a lot of minority tiny clients in the periphery for a long time and they're not poorly supported. Some of them might be, but it's not like they're like that far off from what the Geth team is doing on their own. I think that the Besu Pegasus team is maybe two or three or four times bigger than the Geth team maybe. so like I'm not sure that support is the problem for minority client teams. I felt like this has a lot of tie in with some of the stateless Ethereum stuff that's going on and I wrote an Eth Research Forum post and and a blog post targetted more at the general public. I'm not saying that these are the only problems or that this is the only place that you could get to but my conclusion that I draw for like why don't we have more clients and that's why is it so stressful to be a client Dev, is that it's too hard to build an Ethereum client and so we need to make that easier. I guess that's my thesis which I'd be very curious to hear other people's thoughts and comments on.

**Martin**:  yeah that sounds reasonable to me. 

**Piper**:  yeah I guess that's kind of just like a generic blanket statement maybe we can get even a little more specific. I don't know if you want to actually get into like **what it is specifically that we need to fix?**

**Alexey**: I think that is exactly what we want to do. We want to eventually get to the things that we might be able to fix. cuz I do believe that we have all the people here that could do things. I don't want to walk away with we can’t do anything. That would be the worst outcome ever.

**Piper**: All right! I think I can take a stab at this and then we can see if there's a Direction that's worth digging into more deeply in the discussion. I think that we already are doing one big thing that's going to help **Stateless Ethereum** and it should put us closer to a,  it's not so much that it makes the state more manageable, but it makes it easier to ignore the state. I think that that is at least a starting point that we still don't have a solid solution for you placing economic balance and state growth or anything like that. So we can kind of tackle some of the states where we are already approaching the state problem from One Direction.

What are the other big problems they see is the **networking protocol** itself being a monolith in order to implement a client gets implemented a lot of stuff because Network protocol bundles everything together. Where realistically let’s say you’re a miner who already has all of the states, the only things that you actually need out of Gossip. Right now, you can't be an active participant of the network if you only respond to the gossip messages that are sent over the network because you'll get kicked by the clients who are asking you for data. so you won't necessarily be able to maintain healthy network connections and some of that is that the networking protocol requires clients to have access to all of the historical State and all of the historical blocks and chain data and everything like that. sorry, not all the historical State all of the current  States, all of the historical chain and block data. That alone is a pretty big requirement to put on on clients so it'd be really nice to loosen that either by loosening at or even lifting it entirely by separating the protocol out. 

Alexey presented a sort of loose **diagram of the network divided up into three pieces** and I think that they're sort of a natural dividing line to divide the network into three pieces. **one being gossip sub** which is essentially just transaction information for the current transaction pool and new block information propagating around. the **other is essentially the historical chain data**,  so all of the old blocks receipts and everything like that. The **third is state sink**. So a network that specially designed for efficiently syncing the states for clients who need to pull the whole state. I think this is where we have to have a network that was in these three different pieces and  each of those three pieces with healthy. I think it enables building more special-purpose clients or clients that just aren't required to build out all of the functionality. you could build a client that just follows along with the head of the Chain by only following the gossip part of the network, ignoring all of the other stuff. There's a bunch of problems that come up if we just naively divide the network into three pieces and not something that is probably more suitable for a discussion in a forum post or something like that. Stateless Ethereum attempting to tackle like problem clients having to manage the state. Dividing the networking protocol up into less monolithic pieces into more special purpose of functionality will allow clients to select which network they want to be a part of or things like that.  Now I'm hitting the end of my ramble. I feel like I have a third thing but I always feel like there are three things. Does anybody have thoughts on those specific topics or different things that you think needs to be attacked in order for us to simplify what it takes to build out an Ethereum client?

**Alexey**: I would like to kind of go on to something that you mentioned that saying that let's say that you gave an example of Besu. Besu is having more resources at the moment. It looked like it has got more people than Go Ethereum. yet I would like to hear what is the perceived reason **Besu** is not just simply growing.

**Tim**: I think there’s like a bit of the misconception there. When we first built the client, Besu had 20 people mostly focused on building Eth1 archive node. That was the first version of Besu.  Over time a lot of Pegasys’s Focus has been on other stuff that's not mainnet. So for example we do a lot of private network stuff. A significant portion of our engineers are focused on that. Now we also have Eth2 client, Teku which took from the same pool of engineers that we originally have working on Besu. SO, I’d say, right now, on mainnet there’s probably I don't know 4-6 people who are working on this full-time and that includes stateless Ethereum. And we also have stuff that are sometimes private network related. We have a bigger team but having it mainnet client is one of the things that we are focussed at,  3 or 4 resources. So that obviously splits the resources.

**Alexey**: I would like to ask the same kind of question to other people on the call. Tomasz maybe, can you tell us about **Nethermind**. How many resources you’ve got.  Comparable to go Ethereum. Then I will tell you about our team so I just wanted to have a sense, **Piper’s thesis about the main problem is the complexity of the protocol**. I would like to question this because **my personal intuition is that the protocol could actually be structured** in such a way that you could code, it takes a lot of effort but he can actually organize your code in such a way that the protocol is structurable. It's not like it's completely monolithic. If you have enough people, enough dedication to actually do that you will be able to come up with that kind of code which is very sort of team-friendly rather than requires a superhero to support it.  So I would like to hear from other people, what is the resource situation.

**Tomasz**: If I think about resources, two senior Engineers working on (including me) working on private networks and a few other things and this is also Ethereum 2 and some of the commercial projects that we have. But we have also 2 junior engineers working on testing. More like a developer in the test. One person is working on the project that is not related directly to Eth1. This is the team on the development side. 

**Alexey**: What about **Open Ethereum**. Can Artem tell us about your team? 

**Artem**: Right so we have three people but we are growing but hiring Rust engineers is always a problem. But, we have a team of three people, so we are currently working mostly on bug fixes. We are looking at how to simplify things in the codebase. I have my own thoughts. As per the resource, we’re 3 people and looking to expand. 

**Alexey**:  Thank you so I'm going to give you our situation and anybody who else I forgot. In **Turbo Geth** we are very close, just a few remaining things done and hopefully, we'll be announcing that it's usable. but essentially what we have currently is let me just say we have 6 people, full time. This stuff started to pay off recently because in the beginning there's a lot of fun learning going on. But I think it started to pay off a bigger team. I think it does actually matter. The size of the team doesn't matter in the beginning but it starts to matter more and more if you kind of managed to get them to stick around. I think we have a 7th person who just started as junior developer. I think it will start making a difference. Anybody else I forgot to, oh Piper, can you tell us about your situation.

**Piper**: Yeah,  it's fluctuated some. Right now we've got three people full time on Eth1 with that's not counting me cuz I'm not doing as much direct contribution anymore. Historically we have between 3-5 working on it and we've been at almost three years working on,  thriving ourselves up against trying to build an **Ethereum client on python** which it had its own difficulties. But,  I don't think that we could have gotten further with more resources.

**Alexey**: Thank you! Martin, I think we just started to look at that can you remind us what is the Geth team situation at the moment.

**Martin**:  Sure we are currently, I think five people working on coding and two are kind of new hires, something like that. 

**Alexey**: With new hires, it always takes time to bring them into the speed.

**Guillaume**: I counted 10 including 1 PM. 

**Martin**: Don’t count people who aren’t working on the codebase. 

**Alexey**: Anybody else I forgot? I’d go to the next question so that everybody could answer if it’s okay. 

**The next question goes to my assumption that Ethereum protocol is inherently monolithic and therefore very hard to implement**,  which is partially true but I think it's also true because we haven't had the time and dedication to properly structure into de-couple things from each other. It happened that the first major implementations had certainties things kind of monolithic because this is how it naturally occurs. When you want to implement something you just basically keep implementing it and you get this monolithic product. It takes quite a lot of time to actually split it up and figure out where the proper obstruction lines are and so forth. So this is what I started two and a half years ago. And very recently, actually, I started to see how to properly structure the protocol and how to decouple things. It becomes quite an amazing thing. All my previous assumptions, that it's really hard and monolithic started to fall away so that's why I wanted to hear your **perspective about what do you think about the possibility that we simply did not spend enough time in structuring the protocol and finding correct obstructions and making this more modular**. 

**Piper**: I'm not sure what the difference is between those two.  it sounds like just different words for the same thing that I at least think I was trying to say. whether or not you divide it up into three networks or whether or not you make the one network modular it feel like to anyways.

**Jason**: Is the spec inherently difficult to separate into modular pieces or do we need to spend more resources on designing the architecture so that we model the spec well in a modular way. 

**Alexey**: Basically, the question that is behind this is, do we need like superhero developers to support this?  by superhero developer, I mean that somebody who knows absolutely with the entire thing like it was a very detailed knowledge, like everybody always at the same time know how to do databases how to do networking, the Merkle tree and cryptography? Do we need this kind of people or can we split it up into pieces where you can actually have a developer working on a reasonably, sort of small defined piece where comfortably make changes without knowing that they going to break everything else? So that's what I'm coming into. Can we actually structure it so that we can basically run it almost like industry operation and rather than this kind of superhero base soap sting?

**Martin**: I think, one of the problems of trying to organize it without a superhero programmer is that it’s inherently very difficult to work on, I don't know transaction have length. If you’re not also very aware of denial-of-service issues and what can cause a crash, how can we avoid protocol, the protocol being used with Denial of service and things like that? What things are cheap and what things are expensive and I think there's a difficult thing that requires you to have more than just knowledge about one component of one bit more.

**Tim**: I think, we have seen that too at Pegasys like it's not impossible to get a non-superhero developer but it does take time to build this intuition. This is like how the system works of the Wild, these are the things that you need to be mindful of and these are all various parts. I think an understanding that maybe it takes a while to build up is just like understanding where to find information on Ethereum which is like which is a completely different problem but yeah probably not impossible but it is difficult. And there is a significant ramp-up period for someone to get an intuition of all of the things and when they do, they are much more productive. 

**Piper**: I've seen the same thing on our team. Engineers can be very productive on the client before they gained the broad understanding of the protocol however I don't feel like this but while they can be effective at implementing things on the client what they can't do is contribute back towards protocol development and research. they can only work with what’s there.

**Alexey**: Any other comments from other people, from other teams.

**Rai**: Yeah Alexey, you were mentioning that, to what extent were you saying that you know you don't need to be a superhuman?  like where you just talk about the protocol as a peer or were you imagining the superhuman person has to understand that plus the Merkle + cryptography like you said.

**Alexey**: Well essentially, I'm trying to reflect these kinds of the sentiment that I got from Twitter and from other places where essentially,  to be honest people praising certain individuals like Peter for example or being such a superhero for looking out for the network when in response to when he basically says if I'm waking up at 4 a.m. and trying to do stuff, right? In response-based praise how good you are right you are really Brave and then we're going to owe you the stuff. so I kind of see this as the not very healthy situation. I'm okay with people praising people. It’s like do we need to rely on those superheroes? It's nothing against Peter but what I want to dig into that **what makes a person such a special sort of superhero who can know everything about would you need to do to pray the client team? Secondly, is it possible to avoid that up to a certain extent?** Just answering the previous comments from Piper and others is that now I want to refine my question is that how much effort do you think needs to spend each team on maintaining optimizing the client where you can have it but developers are essentially responsible for certain modules versus the development that this is needed to go to change the protocol. Because I think both are needed and what are the proportions? You cannot assume that everybody, every single person on the team has to do some protocol improvement. A lot of them actually have to do stuff to improve the actual implementation.

**Piper**: I think **the problem now is that all of the clients that are operating on the far upper edge of like efficiency in optimizations that we've been able to figure out.** So we as the client developers end up having to spend time doing protocol developments in order to make our clients work and so we're like at the point where, it's not that you can't build a client on the protocol as exist today, that's obviously not true. But to do so is very difficult and requires a lot of careful optimization and so I think that's where some of the requirements for excellency come from is that in order to build a client, that syncs and works in a reasonable amount of time and is fast enough to keep up with a chain and everything. You have to attack things for a pretty advanced complex perspective.

**Greg**:  Why is this a problem?

**Alexey**: Sorry, what is the problem?

**Greg**:  Why is it a problem that he would very advanced protocol requires very advanced programmers to maintain and to our research and advanced it?

**Rai**: I don’t think that is the idea of the problem that Alexey was trying to bring up. I think, he was saying that whatever the problem is, it could be made easier with the structure in order to lower that.

**Greg**: The various skills need to be reflected in the structure of the software, so the teams can work on it with team members having run expertise. To write one alone is difficult to ride a very high-quality one, although you can steal one that exists and copy it and whatever environment and languages is necessary.
**Alexey**: This is exactly where I'm trying to get into I'm trying to get to the question can we do that? can we add extra structure, add extra guidance to make sure?

**Greg**:  Of course we can everybody do it.

**Alexey**: Let's talk about this, how can you do that?

**Guillaume**: Just before we go there, I have a suggestion to make. I understand the rationale for having several clients,  **does every client needs to reimplement every single piece of code**? You’ve Python, there's not there's no going around this. Maybe Python could reuse from Geth, OpenEthereum from whatever. That could be reused.  Why do we have to reimplement everything every time?

**Tim**: 1. I guess, for us, the reason was licensing and I think something that was considered at first in PegaSys. Can we build of something else, but the licensing of the client is an issue. 

**Guillaume**: okay so if you're going commercial, I can see why this is a problem.

**Piper**:  For the python clients, some other is the design Choice, some of these corners that we painted our own selves into. We did look at one point at using evmc or something like that but if we were only focused on building a client that would have been an option but he also focuses on exposing an EVM Library itself and in order to do that if we were to evmc, we would have lost a lot of functionality and features that were valuable to us. So some of it was just design decisions. I would love to have a database application that just manages the Ethereum state that we could interface with as a black box, that would be wonderful. I'd love to have Turbo Geth squat database, just as a piece of software that we could use. I think that is a great direction for us to focus on simplification is **reusable client component but to get there I think we also have to make clients more modular so that you aren't required to implement all of the things**.

**Artem**: For what it’s worth, the Dev P2P implementation, currently being written as a library so it will be pluggable  and hopefully can be used not only be used in OpenEthereum but also in other clients too.

**Axic**: Just a comment on the EVMC, and just wanted to share. I have the same impression, what Piper said, especially with EVMC. The one reason a lot of these clients choose to only have everything in the same language because debugging is much easier that way and also the delivery of the client is way easier if it's just a single language and packaged nicely. The thing that I see as a blocker against EVMC and EVM1 to be used in Go Ethereum or in other cases. And probably the same applies to you too many other components and **there was a proposal some time ago by Pablo from Aleth, to maybe separate types and components and make them interoperable on RPC protocol**.  I believe he separated the networking layer into its own part. I think there was some discussion there but it never got anywhere.

**Guillaume**: Yeah! I am aware of the Geth 1 server thing and Go argument. The thing is, **some clients are having a hard time catching up, so why not externalize some problematic components?**

**Piper**:  Well, I think that the problem is that the most problematic components are subject to the highest churn. Like, think about State Management,  the best answer that we have for State Management is the flat database layout right now. I think that there's two independent implementations of that, the TurboGeth having one and Geth I believe having the other. I'm struggling to figure out how to say what I'm trying to say but basically like depending on one of these things is essential subjects you to the development cycle of another team because these aren't mature stable pieces of software they're pieces of software that are changing at high velocity and thus that's why I think it's maybe not feasible right now to have reusable components at least in the most problematic pieces of the protocol. The reusable pieces are probably only viable in the most boring parts of the protocol, json-rpc is one of those like exposing the Json RPC API is boring and it's something that every client does and it's a pretty generic thing but it's reimplemented across every single client.

**Alexey**: What I’d say is that we did actually, we did look into EVM1 and EVMC and we did out it in master, because we could. The hope was essentially a team of higher performance and but we hit into,  we hit into these interfaces between languages. In Go,  you get high overhead interfacing with C, which is not noticeable when you do coding once in a while but if you’re running the EVMC  through block sets at the speed of a hundred blocks per second then the overhead becomes noticeable. Therefore at the moment, it’s not, the performance is still lower than the performance of the Native Go Ethereum like the EVM. But we're not stopping there, we actually started developing the kind of the bigger component which wraps around EVMC and then connects to our database which is currently lmdb, which is a C interface. That component is in C++ and that would actually connect at high speed. The problem is when you start making modular software, you’ve to watch out these interfacing points are not the ones that they're introducing too much friction.  We realized the interfacing with EVM via EVMC will reduce quite a lot of friction because of its very efficient interlanguage interface. So, we want to reduce that friction, because we know something like that P2P or RPC doesn't actually introduce that much friction and you can pretty easily separate them out SD as a module. So we actually get in the direction but I would like to sort of getting the sense if we decide this is going to be one of our strategies, I’d want to be everybody to be starting being aware of it and actually move in there,  rather than kind of moving in random directions.

**Piper**: To me, this direction doesn't feel actionable. If I understand correctly the direction you're talking about is generic reusable components, is that correct?

**Alexey**: It is the high-level goal. I agree with you, this is not immediately actionable, but one of these things called the Northern Star, the high goals. Whenever you're making your architectural decisions or your kind of Strategic decisions, you need to have those things in front of you to say these are the two options, which one would contribute to the future where we have reusable components and perhaps that would nudge you into this direction.  I completely understand we can’t simply say oh yeah let’s do everything modular. Yeah, that’s probably not actionable right now. 

**Martin**: Yeah, I would say that there are some disadvantages towards a modular approach.  When you build a monolithic thing, there are a great many opportunities to optimise everything, whereas in the states in the game now, where basically, we have to optimize everything in order to handle the massive actual state that we have. So, it’s not enough to have a class EVM,  in order to actually process both quickly,  you need to do some cheats like you maybe need to have a precursor which checks like what accounts are likely to be used? Can we pre-test them in the state cache so that once it’s executes there's speed up and if we try to just disentangle all these components from each other, then a lot of optimization goes out of the window.  So, I think it's very difficult to untangle everything because then you won't get a fast client.

**Alexey**: I had the opposite experience. 

**Tomasz**: A few things, first of all, we start talking about reusable components, I think we’re looking at everywhere possible. We looked at EVMC, I agree with Alexey, the interface with EVMC was simply not possible to integrate with Nethermind state. It might have been performed underneath but the interface was not designed for integration with clients that well. Up to the point where it was not possible to integrate with our virtual machine that was doing the iterative approach instead of recursive one, that was one example. The interface of the EVM is very simple, it just needs to access state almost to the end transaction with a very small context of the block environment, at this level, it could be possible to wrap it up. 
Then when we talk about multiple clients and we talked about the correctness and coming out of the multiple implementations. That when we start using the common component for the virtual machine, then we try to achieve the goal of diversification by introducing the single component that we all rely on, then why not having a single client then. Okay, you can have different components and different teams specializing in all of them, But then, every single of these components are implemented only once then, we didn’t really get anything from the diversification. 
As Martin said, the same in our case, most of our optimization came from the fact that the understanding of the whole architecture at all the possible levels, all we do to see is cross-module optimization.  I think, over time our code will look lots and lots nice. The way Alexey describes the architecture, nice module framework, it started like this and over time all the optimization is slowly breaking to structure, of course, we put a lot of efforts to keep the picture clean. But sometime the optimization will actually cause it to look worse. Some of the things were terrible when I joined as a new joiner, Something like RLP serialization, every new joiner will say, oh we should rewrite to look nicer, generically, but no, it’s worse than in the beginning but then they are small and small pieces that they are non allocating where specific each type is separately defined on how it serialize instead of doing that in one form. In our case, most of the complexities lie in synchronization and network like a thing that we’re locking proper comprehensive test cases for all potential networking attack, network synchronization nodes, and so on. We’ve consensus testing, so EVM be very difficult to implement. It's reasonably simple comparing to synchronization and state management.
I’d say if you want to have something that all the clients to be better we can save a lot of time in implementation by running more and more network test cases, different attack scenarios being used in these test cases, and so on. Because we have to write it ourselves now, we have to experiment with all the possible malicious peer scenario. When they send this data not really following the rules and are breaking our synchronization mode. It takes a lot of time to test. 

**James**: We have about 25 minutes left.

**Alexey**:  Anyone else wants to jump in to do comments?

**James**: You have to click the raise hand button-down,  always to have a go away, unless you have another comment. 

**Alexey**:  Cuz if nobody wants to talk right now.

**Piper**:  If you've gotten sort of a conclusion, I'm happy to hear that. But I’m not sure what exactly you're like that this this this topic seems to have wandered and I'm not sure objectively what's being sort of suggested here. 

**Alexey**: So far what I gathered from our conversation is that 
first of all, I see some agreement to the easiest that **some level of structuring** might help to improve the life of the developer in one of these teams. 
Even though there’s still an opinion that you do need a ride really knowledgeable of the super developer least one or two whatever. But there still might be some as Greg mentioned it is very common practice to structure the software to make sure that it is designed, it is optimized for the team rather than for one person.
On the other side, I can hear the arguments that the optimizations are necessarily cutting across the modularity, which actually something that I'm not ready to debate it right now but I think this could be proven false. Because I actually saw exactly the opposite effect in our latest re-architecture, which actually gave us the most performance boost. Simply splitting things out actually gave the most performance boost. 
Another thing I heard from Tomasz and Guillaume, which I wanted to fix is that is essentially the idea of having reusable components in some way cuts against the idea of having diverse implementation. Currently would say that yeah these are too so slightly disjoint but not completely disjoint approaches proven to be improving our situation.  Maybe instead of having multiple teams working on a completely different implementation, we can have some sort of hybrid situation where they would be teams working on components and then another team working assembly and you know those components and so forth.
**James**: We will go to Greg and then Artem.

**Greg**: I spent years of working in the kernel of a very high performance system and the team members were specialists in the particular areas they needed to be to get the highest performance out of. They had to be experts it in a very narrow deep way but they had to be able to communicate with each other enough to deal with any crosscutting concerns. But one of us could be responsible for just two or three files in the system spending most of our time, that specialize and then a larger set of files that we all had to understand and they got pretty damn hairy but the specification was clear and the major module structure stayed clear and aligned with the Specialties that you need for that kind of high-performance software. But getting the specification clear, so that somebody can write such a thing not the highest performance but a clear solid implementation, yeah that needs to be done then you can bum it as much as you need to but if it's not an initial clear spec you're not going to make it.

**Artem**:  So, I agree that there’s a need for team members to be specialized in Ethereum core development for the simple reason that they are not born and they come from all walks of life. Unless we are ready to train everybody. We have this experience, in OpenEthereum, we’re hired generally basically, so many of us are just learning the road still. Core developers come from all work of life, some come from Networking, some with a generic backend engineering background, some from security and cryptography backgrounds. It's unreasonable to expect that every single newcomer as a core developer in the core development to completely understand all of the yellow papers right of the back because that unreasonable. People specialize in the usual day jobs that are not related to Ethereum core development, so it makes sense to not piling them basically.
Another thing that I wanted to just mention is that (sorry this is slightly different but also to the topic of simplification) if I were building a new client today there are two things that I wouldn't want to face.
First of all this is the elaborate mechanism and syncing in networking where I have to match request,  this is basically something that Eth66 is designed to solve as far as I know. 
Another thing that I wouldn’t want to do is Ethereum archeology and re-implement all five years of changes in the yellow paper.
So this is something that I wouldn't want to go and so that should be a way for the **new clients to just start with the rules in the network that exist today not that existed a millennia ago**.

**Piper**: That sounded a lot like re-genesis, maybe that was in reference to that which Alexey proposed recently.I think that's something that we should look into very seriously because **being able to ditch the old  EVM rule like that would be great**. I think that would be a major simplification for new client developers, barrier lowering, right? Cuz yes like it is a lot easier for those of us who have gotten to implement them as they come but to try to go back and figure out what the rules were three or four or five forks ago or something like that is not an utterly trivial task to do.
I still am very skeptical about the reusable components. I think that they are a great idea but I don't think it's something that we can like it it doesn't feel like one of those things that you can actually push like it's something that will happen at some point and I think it's good to encourage people to focus on work on that but if we say that's our solution then I think that the result is that we are all going to end up having to just sit around and wait for one of those to show up and that's kind of already the case right now. So, I agree that we could gain some ground there but it doesn't feel like anything that we can actively make happen. 

**James**: It's different than the specialization or the modulization of the codebae so it's easier for Developers.

**Piper**:  They are similar, I mean that one is just on an individual client implementation, like the level of how do you structure code and can achieve good modular code. People have been able to work on the Trinity code base for a long time don't fully understand all the stuff because you know architectural modularity there.  I think we’re already doing that as teams and so I really want to move our effort into the sum of these harder things that I think are going to have just way more significant long-term impacts. Hence the carving up with the network in two maybe three may be up to three different pieces. We've already got great momentum going with stateless Ethereum and working towards having a network with Witnesses. I'd like to see that we have agency to make real improvements are on are focusing on getting more people to look at some of these other areas that aren't stateless to get ready cuz we already have a good number of people working there on things like how can we improve synch and state network. I am lately more of the opinion of like piling on Geth’s already been doing with SNAP and us really looking at what we can do either with the existing protocol or if there are things that we can even do to iterate on it and make it better. So that we can get sync completely out of the Eth protocol that into its own specialized sync protocol. I'm working right now to get a meeting scheduled to work on the other corner of that problem which is historical chain data and figuring out how we can build a network that does the job posting all of that historical chain data so that we can take the responsibility off of full nodes. I am talking about solutions now, but this is a problem that I have been thinking about for a while. I think that this is the area that we have the agency to actually make a change.

**Martin**: I think those are really good points and so the Eth66 will make things easier we haven't actively pursued it yet. It’s really nice to support the old protocols for a while, so I don’t see that is something that is going to make life easier in short term. About having the historical rules, I think that probably makes sense. I think it's totally legit to release a client who will not be able to do a full sync from zero but instead has some hard-coded hash that it syncs only to some block after, I don't know 7 million. Geth uses a canonical hash table to basically hard code the node checkpoint, if someone tries to sync us to block 500, we should not do it.  Then that team would have to solve how do we actually get to State. I mean they could bundle it, they could also have some custom Gossip network which spreads the sync on which they start or something. I think that would be a totally cool thing to do for a new client. 
Regarding what Piper said about separating up stakes, management into some other protocol or Network. As the current contract with a snap protocol works and it's not on top of Eth it's in it’s own space. In the latest design, it definitely really on the Eth node data from a protocol but instead replicate it's inside is not protocol, I think. We’re still iterating on the protocol (me and Peter) but I think, it is at a stable point right now where it is sufficiently involved but it's no longer proof of concept but actually can be used in the more production light setting where you actually sync for multiple peers. 
**Tim**: I'm wondering is if we're conflating two things.  
One is making it easier for a new client that can be written from scratch, a client team that doesn't exist today.
Two is how do you make it easier for the minority clients that exist today to how to improve the number of share on the network or make it easier to keep up.
It seems like we are going back and forth on the stuff that is going to help one or the other. I am not sure, what’s the best way to delineate between them. For example, it was mentioned having modular components for some of the common stuff it's like that would help a lot if you create a client from scratch. But obviously, Besu, Trinity, Nethermind, OpenEthereum they all have JSON RPC.  Yeah, I guess I'm just wondering like in terms of solutions like how different the two are for both new clients and minority clients, today. 

**Piper**: There's one thing about JSON-rpc that I'd love to address which is essentially it's yes we all have json-rpc implementations we intentionally have not implemented any of the logging APIs in Trinity because it's my opinion that there should actually go away. Those should be like secondary tooling that should be on top of clients. I think there are areas for reusable components that could, maybe not in the shortest term but in at least in the medium-term could reduce development overhead for existing clients, as well as new clients.

**Tomasz**: I think, it’s quite reasonable to assume that there be no new client for Ethereum in foreseeable future. I am not sure if we can change the architecture so much for a new client to be able to build. That would be interesting. I think this requires Eth research efforts maybe. Maybe in the direction that Alexey is looking at. 
For the existing clients to improve things, we feel that we spend a lot of time on the tooling things that users are used to solving. It means that we still can work with the users that do not require everything but we can not work with all the users. This will always reflect on the share in the pie, how many users are running nethermind in comparison to Geth. 
We work with some users and clients and they are really satisfied with what they get. Because they may not be using 1 of 5% of the functionality. For easier delivery of the client that provide everything is available in Ethereum now, are tests available for clients are the most useful tool and we can not really over-invest in testing components. One thing that I am looking at it recently is json rpc confirmation of all the clients behaving the same. It’s something that our users have a  bit of a problem for a long time because there is no place which will tell us how exactly the json rpc should behave in corner cases, how it should behave when errors happen, the time out and all. All of these things are closing the minor differences that a user tries to report quite funnily a big amount of time to just fix something very small to be compliant with what Geth and Parity did it in the past. I think with the proper testing and tools we can really save a lot of time here for not only the new clients that will appear but also to the teams like Trinity, Besu, Nethermind. And even like Parity and Geth to arrive at the exactly same behavior in some cases. These cases are just to give you examples what happens if you invoke if you would call, call contract, we found specifying gas price, by specifying the sender. Because the spec of json-rpc , it does describe the api but it doesn’t describe the exact behavior here, and users do have problems. Then they come to us and ask us to spend some time with famous Geth. It’s not necessary following any spec or not following any spec. Because spec is there and we do follow it. Now there is something that is not described. They can not be really valid or not valid it just implemented in some way in a majority client and you have to do that in the same way because other users are used to having it. More testing, more tools for testing network, json-rpc, consensus, and all of these components, then it’s two times faster to deliver this on the market. 

**Alexey**: Okay to the question about would be nice to forget about all the archaeology of the EVM behavior. That’s actually one of the side effects that I didn't realize it would come out to something like regenesis but even before that is what something with Martin mentioned that she could simply download the snapshot from somewhere and then download all the blocks from the snapshot, which is actually what are the things that I'm planning to do with Turbo Geth. I actually decided we not going to try to implement any of the locals in the near future and for the reason that instead, we want to try to do something much more simple. We will produce the snapshot of the states in whatever format we kind of figured out and we basically going to be distributed on let’s say bit torrent. That would be snapshot every million blocks. We are also going to be distributing the slices of the blocks and headers and whatever receipts. So they will be some kind of hardcoded content addresses and will see how it goes because TurboGeth is super useful for syncing from genesis but if it can sync from the latest whatever block 10 million or 11 million I think that would be simple still reasonable performance. The Simplicity of this solution will probably mean that we would not even need to have some kind of super complex snapshot synchronization. This is something that we can do without any hard fork. If a few think that this could be done across the multiple implementations, we could figure that out as well.

**Artem**: I want to talk about json-rpc so it was mentioned. Each client has its own implementation, I personally was surprised,  I don't know if this applies to all clients but that at least **some clients do not automatically generate json-rpc server from a schema**.  This is something that definitely be looked into by everyone and could definitely reduce the code complexity in the clients. 

**Rai**: I just wanted to put something out there. After the discussion about how there seem to be a difference between the level of skill required to implement a protocol vs. suggest tool  Improvement to it. I am a year into working on Ethereum, and I definitely feel like I don't have enough of the wholistic picture to actually think of you know improvements to the protocol whereas I feel much more confident in implementing it as it is and working on our client.
So, I was wondering if there would be any willingness to do something like in Ethereum Open Office hours or something where a few of the people who have actually had track records of suggesting improvements of protocol, we can all get into a zoom call and ask unscripted questions and things like that are implementation-specific. I think they'll be really useful for me and maybe some other Junior developers on other teams.

**James**: I like the idea. I’ll be happy to help organize something like that. We're at time, I want to give us space for perhaps a final thought from someone that's there is something. This just seems to be an ongoing conversation that we should continue in the next one. 

**Hudson**: I have a quick final thought. I think,  if we have one more of these conversations that aren’t about the EIPs, and discussions around what we talked about today I can't even sum it all up in one good word, that we should focus on actionable next steps maybe or like goals or this is what we're doing in response to this so that the end of the story can be we did X in response to Y. I think, that'd be really cool I don't really have any idea what that would be personally but if anyone wants to take up on that and has ideas and throw them into the core devs chat and into the agenda or the public discourse in general.

**James**: I’ll agree with that. 

**Alexey**: Okay so that's what's pretty good.  I would just want to summarize it for 1 minute from what I've learned and I think what we collectively learn together or something that we need to look into more details. I think there was a good discussion about 
is it possible to restructure the teams in such a way that there are some people who have a more holistic understanding and these people are going to have the necessary experience to propose protocol changes. However, they might be the case that the majority of people do not need this majority of people to be able to be productive in such a team, do not need this sort of holistic experience and they could be super productive in simply optimizing the current implementation.
There is some potential for structuring and then that's what Greg called, a  good specification structuring the protocol and what is required in such a way that people could specialize.
We talked about the reusable components which I think are slightly orthogonal or even maybe disjoined to the client diversity.
I think these are the three things that I took from today. 

**James**: Something that would be good for the next time I see are strategies on the adoption of client diversity. I don't think we talked about that today but it came up on the last one.  I think it is time. Thank you all for coming today. 

### Decision Items
-**91.3**- Discuss strategies on the adoption of client diversity. Discussion to be continued in the next meeting. 

# 3. [Review Previous Decisions and Action Items](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2090.md)
(No discussion)

# Annex
## Attendees
* Alex (axic)
* Alexey Akhunov
* Alex Vlasov
* Ansgar Dietrichs
* Artem Vorotnikov
* Daniel Ellison
* David Mechler
* Greg Colvin
* Guillaume
* Hudson Jameson
* James Hancock
* Jason Carver
* Karim Taam
* Martin Holst Swende
* Matt
* Pawel Bylica
* Piper Merriam
* Pooja Ranjan
* Rai
* Tim Beiko
* Tomasz Stanczak

## Next Meeting Date/Time

Friday, July 24 2020, 14:00 UTC

## Zoom chat
* **Matt**: https://ethresear.ch/t/native-meta-transaction-proposal-roundup/7525
* **Pipers Post**: https://ethresear.ch/t/applying-the-five-whys-to-the-client-diversity-problem/7628/6
*  **Artem**: devp2p impl - https://github.com/rust-ethereum/devp2p/tree/vorot93/wip
*  **Matt**: any timeline for integrating back into openethereum?
*  **Artem**: it’s not immediate unfortunately, we are taking some time to fix bugs inherited from Parity-Ethereum 2.7 that surfaced recently
*  **Matt**: okay thank you for the info, excited for this repo
*  **Artem**: rust-devp2p has RLPx connection pool already implemented though, only bridging eth/66 into the RLPx remains, so it could reach MVP within a week or two given enough effort




