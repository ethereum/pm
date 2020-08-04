# All Core Devs Meeting 90 Notes
### Meeting Date/Time: Friday 26 June 2020, 14:00 UTC
### Meeting Duration: 1.5 hrs
### [Github Agenda](https://github.com/ethereum/pm/issues/189)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=IZEcukn9J0Y)
### Moderator: Hudson Jameson
### Notes: Edson Ayllon

---

# Summary

## EIP Status

EIP | Status
--|--
2315, 2537 | Accepted for Berlin and YOLOv1 testnet|
2565 | EFI, proposed for Berlin, currently not included in YOLO|
2046 | Proposed for Berlin. Under Discussion to evaluate for adding to Yolo|


## Decisions Made

Decision Item | Description
--|--
90.1 | Take July off for Berlin.
90.2 | Continue discussion for Agenda item 1 of meeting 90.


---

# Contents

- [1. Features vs. Maintenance](#1-features-vs-maintenance)   
- [2. EIP 2718: Typed Transaction Envelope](#2-eip-2718-typed-transaction-envelope)   
- [3. Review previous decisions made and action items (if notes available)](#3-review-previous-decisions-made-and-action-items-if-notes-available)   

---

# 1. Features vs. Maintenance

Video | [4:11](https://youtu.be/IZEcukn9J0Y?t=251)
-|-

*How do we balance features vs. keeping the network healthy, avoid burning out implementers, promote implementation diversity, etc.?*

**Alexey**: I wanted to bring up this conversation on this call so it's not on the fringes (Twitter, EthMagicians). The first issue we should look at is the burnout issue. Related to that is deciding what features get worked on, vs maintenance. And also reflecting on when we had more implementation diversity in the past. If we bring back diversity, do we want to remain competitive, or be more cooperative?

**Martin**: Back in 2016 the diversity was good. We want to have diversity if there's an issue with Geth, Ethereum doesn't go down. Geth has an agreement never to compare between clients. We have a focus on improving state. The research camp hasn't been participating in the ACD call to push fixing the base layer. We need to feed that back into the biweekly ACD call.

**Alexey**: Eth1.x should return back to the ACD calls. One frustration with the ACD call is the project management calls to add new features. Why do we need this now? Speaking on these calls gave me stress, so I stopped participating.

**Peter**: For client diversity, if there's an issue with Geth, it's a problem with the whole network. I am for bringing back client diversity even if it takes a slice out of Geth's pie. It's reasonable and beneficial for the entire network.

**Alexey**: I think we should make client diversity a goal, rather than hoping it will happen. We have this goal of diversity or performance or both.

**Peter**: It's nice to say that we should push towards client diversity. But apart from Geth going on vacation for a year and waiting for other clients to become more popular, I don't think there's much I can do.

**Alexey**: This goal's for everyone except you. I want people outside of the core developers to also feel like they're involved in this. People should move to new clients, even if they're not familiar.

**Martin**: I propose that until we have a desired client diversity, we shouldn't do hard-forks or add new features.

**Alexey**: That's what my proposal is. Not to us, but to everybody.

**Hudson**: I'm on the fence on having a complete freeze. But there are things we can do outside of the core developers. Such as marketing. To have people know they can run more clients.

**Alexey**: I'd like to extend the idea of community. We have businesses with individual financial interests. We can look at it more like game-theory.

**Hudson**: I think you're right. We should go in the direction you're refering to.

**Tim**: Besu is a minority client. And when you talk to a company that's building on Ethereum, if they're using a single client, their entire infrastructure is dependent on that single client. And there is a cost to them to make it client agnostic. It's easy for individual validators to switch. But not so much for an exchange.

**Alex**: I don't think client diversity will ever happen. People will run whatever is easiest to run. I don't think it's sustainable work to keep 4, 5, 6 clients. If they wouldn't switch for direct benefit, such as features or performance. I don't see client diversity going forward.

**Alexey**: I wouldn't say it's completely wrong. It's not only about client diversity. It has a secondary effect. Even if it doesn't happen, and it takes 1 year to realize this, a more performant client may enter. It's hard to catch-up if we're adding new features.

**Alex**: Having time to build more clients, but right now it's a monopoly. If there was larger competition with another blockchain, we wouldn't be stopping adding more features for the sake of client diversity.

**Martin**: I don't agree. It's easy to spin up a new blockchain with bells and whistles. But in a couple years, you run into the hard problems of managing state, and that's where we're at.

**Alex**: It's not just the technical aspect.

**James**: I think maybe we should return to talking about burnout. People want features, but they don't realize they make Core Developers uncomfortable adding new features.

**Tomasz**: I'm totally fine with adding new features. I feel like it's much harder if we stop adding new features, because other clients can keep improving. Then we'd be competing against the stability and performance of other clients. The new EIPs are 3-4 weeks of work a year. It's not that much.

**Will**: Some of us from Quilt is working on account abstraction. We've been pretty deep in the client code. But we've recognized before a new EIP is added to add more efficiency. I don't think the answer is don't discuss new feature, don't discuss new EIPs. New features is how people can become familiar with the codebase and contribute.

**Tim**: Implementing new EIPs is not a lot of work. It's maybe 10% of what we spend our time on. However, there are more complicated features in the pipeline. There, given its a risk we may never reach 0, having client diversity is a hedge against the complexity of those features.

**Tomasz**: You'll still end up with some clients being the majority of the network. Some clients will be better in some use cases than others. I can suggest a separation of research and the client development.

**Peter**: Adding EIPs is not little work, because of testing. Fuzzing was done for an EIP, which discovered 7, 8 bugs in the Go code. We also found a bug in Besu. Each of these cases would have been a very serious problem to mainnet. It's easy to delegate that to someone else. But Geth picked up this testing because we are the majority. We can't afford being wrong. Something that requires global consensus across every team, that's a tough task.

**Martin**: For YOLO, no other client implemented a state test. We actually had to do fuzzing on the test network. It took a lot of time, and was innefficient. We still managed to find some issues. Big features can be dangerous, and a lot of work isn't on the implementation side.

**Artem**: There's a contradiction between goals in a minority client and majority client. A minority client can experiment. If something goes wrong, the minority client getting kicked out won't affect the whole network. But if a majority client gets kicked out, it brings down the whole network. If we have a lot of minority clients, feature implementation can be a lot easier, and move much faster.

**Peter**: From Geth's perspective, it doesn't make sense to make a change that's not beneficial to Geth, but it to another client. Trinity had a proposal for extending the Ethereum protocol for request IDs. With request IDs, it may be easier for other clients. We can look into adding code that's not a hassle for us, but would take off a larger burdon of development to other clients.

**Tomasz**: I don't agree with Martin that it's a lot of work on testing. People will be implementing things in Geth first, testing things in Geth first, etc. I think we should we focus on what's best on the network. And that's having one super stable client. This puts a lot of burden on the Geth team. But we can maybe make testing more client agnositic to lift some of that burden. Request ID is an improvement to things already there. These things are slightly invisible. These changes which are innvisible and hard to implement may decrease client diversity.

**Alex**: Even if we do a feature freeze, all clients becoming equal doesn't provide a case for why to switch to another client.

**Tim**: Besu has tried to take more of a role in testing. It's hard looking from the outside what we can do. We'd like to contribute, but would like to knoow what's the best way we can spend our time when contributing.

**Alexey**: I think we do need to try an action to shift equilibrium. One way is to shift incentives. If we do get implementation diversity, what does it actually buy us? Ethereum clients requires a lot of expertise to utilize. If you're a company and want support, you can't get that with Geth, because it's 4 people who are very busy.

**Peter**: A lot of problems comes from Geth doing multiple things. We don't do it for pleasure. Because we are the majority, we feel it a responsibility we don't fork the network. But at the end of the day, we're Geth developers.

**Greg**: To some extent, Geth having the big majority is inevitable. It's not a game-theory issue. It's a market issue. Unless we have a plug and play standard, we can't take Geth out and put something else in if there's a problem. Given that, it's not acceptable to have 3 people implementing, maintaining and testing the client. Freezing features on the whole system I don't see really helps a lot. We don't add that many features. I see the Geth team is understaffed. Minority clients are going to compete by fitting into places that Geth doesn't fit.

**James**: The equilibrium won't change unless we do something. For client diversity, we could block an EIP from being implemented until we reach a certain number of diversity. I think I wrapped up with Eth1.x, I can shift that time commitment to client diversity.

**Martin**: Testing is one of those areas, if you don't know anything about it, you might think it's easy. But with Ethereum consensus, you need deep, low level expertise. Client impelementors are the ones with knowledge to write these tests. It's hard to add new people. We can maybe include more people from the other teams into testinng that the Foundation does.

**Hudson**: OpenEthereum and Besu said in chat they'd both be happy to contribute.

**Tomasz**: Geth team is understaffed, and still would be even if we add 20 more people. It would just be developing faster and safer. If we add more people to Geth, then we make it harder for other clients to compete. Funding will be shaping how clients operate. Although Geth is bigger, there are some responsibilities that are slowing them down.

**Alex**: Maybe it's better to take people from every team, and have them do different things.

**Alexey**: Any solution that works has to include people outside of the Core Devs. In regards to market, this inevitability I don't believe in it. There isn't a lot of market around the core developer. It's mostly subsidized. But the game theory does exist.

**James**: I want to make sure this turns into things we do somethiing about.

**Hudson**: I want to remind everyone that this will continue in the Gitter and Ethereum Magicians thread. Is there something from Eth2 that they're doing for client diversity?

**Vitalik**: One thing we did is not create a situation where one client had a head start. One thing we could do is when we integraate Eth1 into Eth2 is have individual Eth1 clients talk to Eth2 clients. One thing we're doing is not launching Phase 0 unless we have multiple clients. We're not really at the point where we're specializing the implementations.

**Martin**: One thing I wanted to suggest was shelving Berlin for the month of July.

**Hudson**: That could be helpful. Who else has an opinion on this?

**James**: I would agree. A reason being BLS is complex enough to benefit from more client diversity.

**Hudson**: I want to wrap this up in 6 mintutes to give Matt 10 minutes to talk about their EIP for EFI, as he did attend the meeting for this. Everything else can be pushed next meeting.

**Pooja**: The Cat Herders can help with coordination. ECH is a little underutilized.

**Hudson**: Although it sounds like a small thing, coordination issues can arise from issues in communication.

**Alexey**: Although we sacrificed most of the agenda, I hope it was the right thing to do.


# 2. EIP 2718: Typed Transaction Envelope

Video | [1:17:47](https://youtu.be/IZEcukn9J0Y?t=4667)
-|-


**Matt**: That was a great conversation. After that, I don't want to introduce more changes yet. But when changes are made, it may be a good thing to consider. It's currently not EFI.

**Hudson**: This is the first time this EIP is discussed. It can be motioned to EFi in future meetings.

**Matt**: This EIP is something similar to what Vitalik proposed with EIP 232. We're trying to introduce new transaction formats. This introduced issues on how we can have different transactions. We want to create some sort of ROP tuple. That's the really short description. I don't think it would make a huge difference in backwards compatibility. Having a system for more transaction types will make other EIPs more digestible.

**Hudson**: Any questions or feedback?

**Vitalik**: I like 2718.

**Martin**: If you wrap a transaction and don't sign it, what prevents someone from wrapping it differently?

**Matt**: What do you mean by that?

**Martin**: We're short on time, maybe take this discussion outside the call.

**Hudson**: There is an Ethereum Magicians link in the Agenda.


# 3. Review previous decisions made and action items (if notes available)

Video | [1:24:33](https://youtu.be/IZEcukn9J0Y?t=5073)
-|-

- Testing static call in client. James was on vacation, so this didn't happen. Left for next call.
- In regards to taking July off, OpenEthereum and Besu are OK with it, as their work for Berlin is pretty much done.
- EIP 2565 was moved to EFI. Unsure if the EIP was updated.
- Alex S. security audit for proxy Eth2 contract. Need to follow up to see if that's done.
- Kelly still hasn't shared the test vectors.




---

# Annex


## Attendance


- Alex (axic)
- Alex Vlasov
- Alexy Akhunov
- Artem Vorotnikov
- Edson Ayllon
- Greg Colvin
- Hudson Jameson
- Martin Hoist Swende
- Matt
- Peter Szilagyi
- Pooja Ranjan
- Rai
- Tim Beiko
- Tomasz Stanczak
- Vitalik Buterin
- Will Villanueva

## Chat

From Alex Vlasov to Everyone: (10:39 AM)
Peter, your argument also sounds against diversity

From Tomasz Stanczak to Everyone: (10:55 AM)
sorry, I was not aware of the 'raise hand' icons :)

From Artem Vorotnikov to Everyone: (11:01 AM)
OpenEthereum will attend such a call

From Tim Beiko to Everyone: (11:01 AM)
Besu too, happy to contribute here.

From Alex V to Everyone: (11:01 AM)
I’m also curious in general

From Rai (ratan.sur@consensys.net) to Everyone: (11:01 AM)
I'm down to join for the fuzzing call

From Tim Beiko to Everyone: (11:02 AM)
@Rai you just got the job :-)

From Rai (ratan.sur@consensys.net) to Everyone: (11:02 AM)
hahah

From Tim Beiko to Everyone: (11:03 AM)
+1 to everything Tomasz is saying

From Péter Szilágyi to Everyone: (11:03 AM)
Solution, fire the Geth team :D

From Tim Beiko to Everyone: (11:05 AM)
lol

From Rai (ratan.sur@consensys.net) to Everyone: (11:05 AM)
Noob question: is it a licensing issue that prevents the geth team from contributing to other clients or something else?

From Tim Beiko to Everyone: (11:05 AM)
What do you mean by “contributing to other clients”? Writing code directly, or having infrastructure that supports them?

From Péter Szilágyi to Everyone: (11:05 AM)
Why would we? :)
I mean working on two projects is kind of hard
And our goal is to make out client awesome :)

From Rai (ratan.sur@consensys.net) to Everyone: (11:06 AM)
Writing code directly.@Peter, because geth is too good and that's causing this dicussion

From Artem Vorotnikov to Everyone: (11:06 AM)
Other clients are structured differently, and the elephant in the room - written in a different language

From Péter Szilágyi to Everyone: (11:06 AM)
^this

From Tim Beiko to Everyone: (11:07 AM)
Yeah I don’t see why you should, personally. I think trying to make the testing & other infra client agnostic is a good step, and I also like the idea of adding EIPs that make it easier to catch up.

From Alex V to Everyone: (11:07 AM)
I don’t say it’s the solution, but may help with testing and understaffing

From Alex V to Everyone: (11:13 AM)
I’ll forward this to gitter, but does a tool exists that does something like: spin empty network, do setup stuff, snapshot, do sensitive stuff, snapshot? Without writing client-specific code (web3 style interaction)

From Tim Beiko to Everyone: (11:14 AM)
Re: pausing Berlin, I think we need a more meta conversation about the broader roadmap

From Tomasz Stanczak to Everyone: (11:15 AM)
We should totally not rush Berlin unless critical for Eth2 Phase 0 which I believe it is notGood idea from Martin

From Tomasz Stanczak to Everyone: (11:15 AM)
also gives all teams a bit easier July time

From Tim Beiko to Everyone: (11:15 AM)
Instead of “do we include EIPs X, Y and Z”, try and have a more holistic look at what are the top 3-4  things we want to get into Eth1 over the next year-ish.

From Tomasz Stanczak to Everyone: (11:15 AM)
we have implemented Berlin by the way, all merged

From Artem Vorotnikov to Everyone: (11:15 AM)
I would rather push Berlin out and *then* take the time to refactor

From James Hancock to Everyone: (11:16 AM)
That can be part of Hardfork coordination @tim

From Tomasz Stanczak to Everyone: (11:16 AM)
we have it implemented - give ourselves more time to test it

From Artem Vorotnikov to Everyone: (11:16 AM)
If we shelve Berlin now, and focus on spring cleaning, then if we break something, Berlin will be pushed much much further

From Tomasz Stanczak to Everyone: (11:17 AM)
we still need the repricing

From Tim Beiko to Everyone: (11:17 AM)
Tomasz, do you mean EIP-2046?

From Greg Colvin to Everyone: (11:18 AM)
Yes Alexey, thanks for kicking off this conversation.

From Alex V to Everyone: (11:18 AM)
I thought it was conditional on ability to implement it fast and painlessly (2046)

From Tomasz Stanczak to Everyone: (11:20 AM)
One thing - if we delay Berlin to after July then more EIPs will be added anyway :D

From Hudson Jameson to Everyone: (11:22 AM)
lol it will be up to us :P

From Vitalik Buterin to Everyone: (11:22 AM)
another benefit of 2718 is it would also remove that work from account abstractionOK you have the list 🤣

From Pooja Ranjan to Everyone: (11:24 AM)
https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2089.md

From Alex V to Everyone: (11:30 AM)
I’ll re-share from telegramfor modexp benchmarking vectors



## Next Meeting Date/Time

Friday July 10, 2020 14:00 UTC
