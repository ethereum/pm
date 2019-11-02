# Ethereum Core Devs Meeting 73 Notes
### Meeting Date/Time: Friday 25 October 2019 at 14:00 UTC
### Meeting Duration: 1.5 hrs scheduled, 1 hour 5 minutes actual
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/133)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=zT4TzlXQ6wA)
### Moderator: Hudson Jameson
### Notes: Jim Bennett

----

# Previous Decisions

**DECISION 72.1**: The Ice Age EIP will not be included in Istanbul. This gives enough time to plan for another fork and not delay Istanbul.

**DECISION 72.2**: Bring your objections to the AllCoreDevs in two weeks if anyone is opposing the Geth team defining Eth64 as the fork ID thing and rolling it out from EIP 2124.

**DECISION 72.3**: CatHerders are going to reach out to the Gorley team to make sure that there is clear communication about node upgrades for Istanbul.

**DECISION 72.4**: Wei has confirmed to David and other core developers that 2200 is self-contained.

## ACTION ITEMS

**ACTION 73.1**:  James Hancock volunteered to write an EIP for the Ice Age postponement.

## AGENDA

## 1. Istanbul
##Testnet Status Updates##

**Hudson**
Nobody has seen any issues. We can probably look for a mainnet block number now. Are we going to decide that in Gitter? What's a rough date for that?

**Piper**
Let's pick a week, and then a block number can figured out at the end.

**Danno**
My thinking is we want to pick either the 4th or 11th of December, and not do the 18th, 25th, or 1st or 8th of January.

**Tim**
That gives us six weeks to get ready.

**Hudson**
It seems we're agreed on December 4th.

**Piper**
If we shoot for December 4th and get shut down, we potentially push out the four weeks to the January mark so that we're not running up against holiday weeks.

**Tim**
By "shut down," do you mean if there is an issue found with Istanbul?

**Piper**
Just some unforeseen thing that causes us to want to push back. We should still shoot for the first week of December, but if that doesn't work, we fall back four weeks.

**Danno**
I like having a fixed fallback date, because it sets a standard for how critical the issue needs to be if we're going to push back a month.

**Hudson**
We'll figure out the block number in the Gitter chat. Let's set a goal for figuring it out today.

**James**
What is the reasoning for not having it be sooner than December 4th?

**Danno**
All the clients need to put the block number into their code, and then they need to ship the code, and then all the exchanges and node operators need to download that code and install that code. So I think four weeks at a minimum is what we should budget for that.

**Tim**
So this gives the clients two weeks to implement the change and four weeks to everyone to upgrade.

**Danno**
CLients could update in an hour. It's just getting it through the release process that tends to take a longer time.

**James**
My only worry about that is that by having the backstop date be in January, it's pushing Berlin too far back. The next one may get into problems with the Ice Age. I would rather have it be for weeks out with a backstop be the December date so it isn't pushed into January.

**Hudson**
But if we do that, we might not be giving exchanges enough time to upgrade.

**Piper**
There's nothing that says we can't use second week of December. We just want to set some easy backstops here, and we can change our minds later if the situation calls for it.  

**Danno**
The thing about backstop dates is there's also the same process if we're going to ship and change the time. We have to build a new client, ship it out, and get everyone to install it. That's why I think at least four weeks is necessary.

**Hudson**
So we're decided on December 4th, with January 8th as a backstop.

## 2. [EIP 2124(https://youtu.be/zT4TzlXQ6wA?t=569)]##

**Hudson**
This is the new fork identifier.

**karalabe**
The idea with fork ID is that we published that a long time ago, somewhere around March or May. People generally said that it's fine. We didn't push it harder because it's mostly just a specification of how this fork identification would look like, but it wasn't actually a specification that was included anywhere. The reason we brought it up again is that we had an issue with Rockstone where there was a miner pushing the non-forked chain quite a lot. Generally, clients have a hard time following a non-majority chain. These issues can be fixed by including the fork ID and protocol handshakes. That's the reason the fork ID was created.

We brought this EIP up again because we have a proposal to include it in the handshake of the Eth protocol, replacing the genesis hash field with this fork ID field. It's a tiny, beyond-trivial change, but since its an ecosystem change, we thought we owe the ecosystem the chance to give it a thumbs up and not just roll it out. Does anyone have any opposition to using it?

**Piper**
No opposition to using it, but I'm curious as to the motivation for replacing the genesis hash with it. Why not just add it as a new field?

**karalabe**
Because the genesis hash is already hashed into the fork ID.

**Piper**
But it's opaque, which makes it non-inspectable if it isn't what you have, which means that you lose data there when it isn't a known value.

**karalabe**
But even now, you can't differentiate between Ethereum Classic and Ethereum.

**Piper**
But you can differentiate between, "Oh, that is Rockstone," or something like that. I guess you can, in theory, do that with fork ID, but if they mix in different block numbers, then you've lost that, too.

**karalabe**
If it is based on the Rockstone genesis hash, but it forked away into a completely different direction, then it's not really Rockstone anymore, so does it matter that you don't account it as a Rockstone node if you know that it's not Rockstone?

**Piper**
I'm just starting to think about this, but the bit is that you lose that information as an easy classifier for who you're talking to. That's my only objection. Since it's 4 bytes and a one-time message, it seems simple to keep both genesis hash and fork ID.

**karalabe**
I'm not really married to either way. One thing we can do is in Eth63 or 64 we can add the fork ID as a new field. Essentially they will draw on side by side, and later on if we decide there's no point to have the genesis hash, we can always drop it later.

**Piper**
I have a much easier time saying yes to that.

**Trenton**
Just to confirm, since this is not touching the EVM or anything internal, this go into Geth by itself.

**karalabe**
Yes. This is just a networking thing. If Geth rolls out Eth64 with this extension, we will still support the old protocols, so every client will still be able to talk to Geth like nothing happened. It is fully backward compatible. The reason why it would be nice to have a consensus that this is a good idea is because Eth is actually the Ethereum namespace. We don't want to turn it into a Geth namespace.

**Hudson**
Let's also hear from the Besu, Parity, maybe the eWASM team or anyone else for their concerns.

**Danno**
This is Besu. I like it going in. Whether it's with the separate field or genesis, I'm neutral. But something like this going in I view as a net positive.

**Wei**
Parity is cool with it.

**Tomasz (Nethermind)**
I just joined, but I assume this is the discussion on the improvement on the history of forks in the synchronization mechanism? I'm totally in favor of this change. I've been reviewing it, and it looks good.

**Hudson**
It's good to go, then.

**karalabe**
I'll make the minor modification that Piper suggested to keep the genesis hash. I'll open up a tiny EIP to spec it, so that there's something written.

**James**
I have a meta question about that. I know that these kind of changes don't require hard forks, but is there still value in having them go through the same EIP-centric process or that same funnel?

**karalabe**
Definitely yes.  

**Piper**
I think that question may have been misunderstood. Do you mean actually having coordination and block numbers?

**James**
No, I mean the proposal that Martin gave that there's an initial green light, and then there's work done, and then there's testing, and then final approval and implementation.

**Piper**
I don't think that makes sense, since this isn't a consensus issue. This is completely orthogonal from the consensus part. You're referring to the EIP-centric forking and signaling mechanisms, right?

**James**
Yeah. In general, should it go through that same kind of process, or should it have its own process?

**Martin**
I would agree with Piper.

**Piper**
Yeah, because we have mechanisms in the networking protocol for negotiating "I'm on version 63" or "I'm on version 64" or "I support both," that sort of thing. This isn't a thing where everyone has to agree on it, so it's fine for any client to roll it out today if they wanted to, and it wouldn't affect the network.

**Alex**
Side question regarding these EIPs, because we do have a networking category. 2124 is there, and so are a couple of other no-discovery EIPs or ERCs. They are in draft status right now, and I question whether we should have EIPs for all of these. Should we move them to final if they are adopted?

**karalabe**
They should have EIPs, because EIPs act as documentation. Essentially, it's a spec. If you're wondering what EIP 64 was, you can immediately pull up the spec and see what the dif was compared to a previous one. Even without documentation, it's good to have a nice spec of the change. As for draft vs. final, I think, yes, if we agree that we want to roll it out, then when we roll it out we should probably mark it as final. For example, with the fork idea, that were some minor cases where somebody suggested we can do it cleaner. But otherwise, it's more or less final, in my opinion.
There are quite a few EIPs that are independent from one another.

**Hudson**
We need to fix the EIP process in the future so this is clearer. Just to avoid doing process for the sake of process and slowing down any implementation, I think we can say this is final and agreed upon.

**James**
I agree. I'm just trying to suss out what are things that go through that funnel and what are things that don't, and what we should do about the EIP process in the future to improve the whole system.  

**karalabe**
One of the reasons these networking changes are a bit problematic in the EIP process itself is because it's quite a few steps. There's an EIP for each step. Honestly, these all should be individual EIPs, because these are completely independent in scope, tiny submodules or sub-protocols. However, the problem is that most people don't care about networking at all, or a lot of teams don't have the capacity to work on networking. The only way to prove that these things are useful is to spec them out and implementing, and then start demonstrating that they work. So we can't really get stuck on each individual EIP and have big discussions, because most people want to see that the whole system actually works, and only in that way will they invest the effort. Which is fine, but this makes it a bit weird in the EIP process.

**Hudson**
That's good to know. We should correct the EIP process to take that into account.

**Alex**
At minimum, it would be nice to have final documentation of each of these networking features or changes. It seems like the EIP repo may be a good place to have them.

**karalabe**
Yes. And I will open a new one for the Eth64 proposal.

## 3. [Berlin(https://youtu.be/zT4TzlXQ6wA?t=1464)]

**Hudson**
This is going to be a fork that is post-Istanbul. We need to talk about process and scheduling discussions, the Ice Age, and the tentatively accepted EIPs, which we'll talk about at the end. I'm trying to decide if we should talk about process and scheduling of Ice Age first, because one is dependent on the other. I guess it depends on when the Ice Age is supposed to happen. Does it have an estimate for that?

**karalabe**
If we down go with the EIP-centric thing, then the Ice Age is just another EIP-centric thing that gets solved.

**Piper**
Which I would second and advocate to do.

**Martin**
And I would third.

**Tim**
I have a bit of a different perspective there. I agree that the EIP-centric process is something you want to aim towards, but given historically how slow hard forks have been, going from year-long hard forks with a bunch of EIPs to months in between hard forks and one EIP per hard fork might be too much, too soon.

So I was wondering if there were a middle ground we could do here, like committing to upgrading in six months with whatever is ready then. We could use the EIP process proposed by Martin but not necessarily going live with each EIP, just agreeing on the date and shipping whatever is ready by that point. That would be much quicker than the current one-year cycle without going all the way to having one upgrade per EIP.

**karalabe**
I don't think we necessarily want to go with one upgrade per EIP. We can say we know an EIP is ready, but we know that there are two other EIPs that are almost ready so it makes sense to bundle them together. So we don't necessarily have to do "cowboy style, as soon as it's ready, shoot."

We tried to do half year or eight month hard forks originally. So Istanbul and even Constantinople were supposed to be eight month things. The result was to make additions as we go along, because people feel that if they missed the hard fork, God knows when the next one will be.

**Tim**
On that last point about people who miss the hard fork, saying that there will be a hard fork in six months and pre-committing to another on six months after that provides visibility to the community, saying that these things are going to happen on a regular schedule.

**James**
Looking backwards on the state of the fork process and how some things have been slower than we've wanted, my view is the reason is because it hasn't been EIP-centric, and that the solution is that the scheduling will be a lot easier when we're working with things that are ready to be shipped.

**Tomasz**
I wanted to come out in favor of the EIP-centric approach. As Peter says, maybe sometimes it will be easy to bundle them. There is one interesting consequence of this. If there is any EIP that is particularly divisive, the "One-EIP-per-release" model gives the community a better opportunity to reject it.

**karalabe**
That's a fair point, but I think that might actually be a drawback.

**Tomasz**
There are problems with that as well. I think it might sometimes be easier to push important changes with the community if they are bundled, but I'm not necessarily sure if this is fair.

**Pooja**
I have proposed a hybrid of this process, which you can read about [here(https://github.com/ethereum/pm/issues/133#issuecomment-546359045)] I would like to get your feedback on this. Basically, what I'm saying is that we can target for a biannual upgrade, but there should not be any fixed month. It would depend upon the readiness of EIPs. We could consider bundled EIPs. Big changes can be time-bound, but we don't have to rely on a fixed date. The model is a hybrid of time-bound and EIP-bound.

**Danno**
One of the things that's different from what this proposed normal is - tests are supposed to come before things are included in a block. One of the things that held back previous releases is that tests took longer to write than anticipated.

**Hudson**
So in order of things that are important, one of the things near the top is making an upgrade model that puts tests first, meaning nothing is even approved until tests are made. Is that something most of us can agree on?

**Martin**
No.

**Piper**
I like the discussion on process, but I also like trying this fundamentally different approach of EIP-centric forking on this easy candidate fork which may only include a change to the Ice Age, which is a very simple, non-controversial way to try EIP-centric forking with our training wheels on. I'd like to advocate that we try this this one time without committing to do it in the future. Once we've done it, we can talk about it and see how it went.

**Martin**
Re: testing first - the reason why testing drags its feet historically is that it's very difficult to do the testing and produce the test cases when there are no clients that have implemented. So therefore the implementation needs to come pretty soon and be activatible in the client and not just in one client.

**Hudson**
I agree with that. What I meant was we don't say "We want to do this EIP," and then we go through all the steps and say, "Oh, we don't want to do this anymore because we found this one thing during implementation." I was trying to say we should do final approval after everything's done.

I like Piper's idea. Right now, with the model that Tim and Danno suggested with two forks per year on a specific date, I like that, but we can't try that until after Berlin because of the Ice Age. So it wouldn't be two a year; it would feel like it would need to be three that year. It's not something we could do with Berlin.

Tim and Danno, is that accurate?

**Danno**
I think it's accurate. We want to be able to do a full cycle on this. Berlin already has some fixed things hanging over it.

**Tim**
I think the counterargument to that is that, aside from the Ice Age, which we said on the last call is not until next summer, so it's not super urgent, the two EIPs that have the most traction for Berlin are 1962 and ProgPoW. ProgPoW is obviously pretty controversial, and Martin already this morning put a pretty long comment around 1962, so the case can be made that we don't have that many EIPs ready for Berlin anyway. If that's the case, maybe having an open upgrade six months in the future makes sense.

**James**
I would think along the lines of Piper, and part of me worries that we're pre-optimizing for stuff and assuming a lot of things we don't know. One thing that will be different moving forward is that I'm joining the EF to help for hard fork coordination, so I'll have a lot more time and eyes on the process itself.

As far as the EIP-centric model goes for me, it's a focus on getting EIPs ready rather than a focus on "when are we going to release whatever" and then figure out what will fit. I wouldn't say let's have two forks per year, but rather a schedule that has windows available that people can know in advance, so that people can prepare for it and then work on how many upgrades we're going to get in this year. The focus shouldn't be on how many forks we'll have per year, but rather on getting as many EIPs as possible through the EIP-centric model, and setting the schedule for people so it's consistent and predictable for people to use, but having, say, six windows per year when the schedule can shift.  

**Hudson**
I think that's good. As far as what we're going to do for Berlin, it sounds like things are tending toward more of an EIP-centric model for the EIP that are done, such as the Ice Age Block One, which is so easy that it would be a really great practice, because we can it has gone through the process of the EIP being written and implemented and then scheduling it with any other EIPs that are done around it. If not, we'll just do a single hard fork for the Ice Age.

**Martin**
Does anyone volunteer to write an EIP for the Ice Age postponement?

**James Hancock**
I can do that.

**Alex**
This might be an unpopular opinion, but I feel like the EIP-centric model is actually what we have been trying to do with one exception. But the steps the EIP-centric model explains are pretty much what we have in EIP 1. However, somehow we were not successful in enforcing those steps. So EIP 1 shows that people are pretty happy with this idea, but then it would be down to the EIP proposer to do all the steps. We all have the same things in EIP 1, but we never enforced it. So I wonder, how will we enforce this now? I see a couple of problems that we've had in the past.

Number one is how do we get people to review EIPs and give their opinion? In Istanbul, one example was the Blake2. It took quite a bit until some clients could focus on giving actual low-level feedback. Because most of these low-level EIPs, especially those affecting the EVM, it's fine if you give a blessing that essentially the EIP looks good, and then let the champions implement them and create the test cases, but then how many cycles would you accept of reviews and changes to that? If you don't want this to be a never-ending process, then you need to somehow motivate people, likely from this group, to give their reviews prior to the first blessing.

**Piper**
I have some thoughts on this that I'm not necessarily ready to share in detail, but what I'm interested in us looking into is the research model with having dedicated resources on the client teams that are focused less on client maintenance and development and more on upcoming research and implementation and trying those things out. In that model, you've got people who are more invested in participating in discussions about EIPs and generating test cases, because they're collaborating with similar other teams who are focusing on these same things. I think it fixes some of the motivation and attention problems that we've continually faced for the entirety of the history of the network.

**Alex**
Piper, my second question ties into what you said. There have been a couple of EIPs which have been well-received, but it turned out that the champions never really considered implementing those changes themselves. They were only interested in sharing the idea and then expecting client developers to finish it off. I wonder what will happen with those. We just took up the work in the past. How will this work in the future?

**Hudson**
To answer both your questions, how are we going to be motivated to continue when we were trying to do the EIP-centric model before? I think the difference between Constantinople and what is Istanbul now, and even the ones before Constantinople, which was Byzantium, the reason is because now we have more resources that are in the hybrid technical/non-technical range. For example, James was just hired to have his eye specifically on the process and work with people to improve the process and formalize it and talk to the client teams and make sure that everything is being done properly. We also have people like Pooja and Tim and Brent who are behind the scenes helping with stuff. I think it's going to be different now because we have more people power now than we had before. That's going to make a huge difference.

For your second question as to how we're going to incentivize people to look at the EIPs more closely, I personally like [Alexey's working group model(https://medium.com/@akhounov/ethereum-1x-as-an-attempt-to-change-the-process-783efa23cf60)], where when you have an EIP, you have a champion who is responsible for everything. You have improvement proposals that aren't formal; you have working groups around them. Those working groups work with the client teams on reviewing and implementation and testing, and those working groups of people who have vested interest basically recruit and push for review and implementation. So if you look at what the process could be in Ethereum 1.x, it has a bunch of charts with smiley faces on them that show what the process could be like in the future.

I think we don't need to figure it out today, but we should be thinking about this model with the other ones we've talked about when considering how we can change things for the future.

**Alex**
I have one last concern. There's no way to scale the work as it is right now, because it's mostly client developers who try to do everything. Most of these proposals would mean that we would separate these concerns and try to engage more people in the work itself. In that model, the role of the client developers would be to give this initial review and reviews throughout the process, but they wouldn't be required to implement all of these changes themselves. However, a lot of EIPs are proposed by client developers themselves, because they're close to the network and they see issues, and they want to fix those issues. So will get in a potential situation where a client developer is going to propose their own EIP and only work on their own EIPs, and everything else gets neglected?

**Piper**
I don't think so, but I'm not sure which model we're talking about. In the concept I'm working towards right now, it involves a lot more close collaboration between client developers, so that we're not all working on our own solutions to the same problems at the same time, so that we collaborate more closely and work on similar things more closely and concurrently.

**Hudson**
Reading a comment from Trent:
What does the Geth team look like? Are there efforts to onboard more core members to that team? What would help shepherding EIPs?

And the same can be asked of Parity, Nethermind, Besu, and the other clients. Is there any way that we can expressly try to recruit more people to the core team. Would that help shepherd EIPs?

**karalabe**
Speaking from the Geth team's perspective, we've probaby been doing a crappy job at trying to find new people. However, back when we did have a few people join and then leave, it's not easy to find someone who would be enthusiastic about working on low-level protocols. The Geth codebase is quite complex. It's quite a lot of optimization, so there's a pretty steep learning curve to just jump in and start making modifications, and it's also really hard to review and approve ERs, for example, especially because there's quite a lot at risk, and it's a bit critical. It's hard to find people. Not many people enjoy spending a month trying to get a 25-percent speed improvement in a weird corner of the Geth codebase. I would be happy to get somebody onboard, but it has not been easy in the past.

**Tim**
I'll echo what Peter said. At Besu Pegasus, we are actively hiring engineers if anyone knows anyone with a Java background who interested in this stuff. It's funny that at intersection of the people who have the technical experience, the desire to do this, and the fair bit of non-technical work that goes into the shepherding- what if you work on the same thing for a year, and it doesn't actually make it in? - it's hard to find people. If you know anyone who is interested, we can find you a place where you can help the community.

**Danno**
And there's probably clients being written in your favorite language, so reach out to that. If Java's not yours, we'd still be interested in talking.

**Alex**
One last comment on these processes. The point that we weren't really good at in the past was reviewing EIPs and getting initial feedback. I don't know what the best solution is, but it would be nice if there were a recurring way, perhaps every two weeks, to say core EIPs have to be looked at by people attending AllCoreDevs, likely not on the call, but outside of the call.

**Martin**
So the approval going forward needs to be very explicit and needs to have the actual client developer groups present to do that approval.

**James**
I experienced this on the other end as part of the Blake2b proposal. I was begging people for feedback. Part of what happened it it took almost three months for it to be merged to draft...

(Phone breaks in and out here, something about allowing things to bubble up as to what should be looked at more closely.)

The EIP-centric process gives this gradation that says "Yeah, we should look more closely at this." I'm open to having some form of schedule and more formal way for doing that. I'm open to ideas.

**Danno**
I thought that the first one was to get the high level rather than the low level details. It was looking for the general approval of AllCoreDevs saying "yeah, this is a good idea. Go ahead and get the final specification and implementation." And then, at that point when there's a client implementing it, we can go ahead and get the details. I wasn't expecting that the first step would be full approval with a full API and all that. If it's a big change, the AllCoreDevs can say, "That's a bad idea, so don't even try." But if it's something small, they can say, "It sounds like it's a good idea, so go ahead and figure it out." That was my understanding.

**Alex**
My understanding would be similar, but I think this also depends on the change, because some changes might be small enough and contained enough that we can, if it's only an abstract, we could give a blessing, but some others could be so complex that it may have to be changed entirely, and we may end up in a couple of cycles giving feedback, with the champion changing everything. I'm not sure if we can get this right in the first round anyway, but it depends on the scope of the actual EIP. Some will be easier to deal with than others.

**Hudson**
In summary, these are all good things for us to think about, and I have hope for the future of this process improving.

## [Testing Updates(https://youtu.be/zT4TzlXQ6wA?t=3374)] ##

**Wei**
On an unrelated note, the EIP 222 0000 is still not merged yet. Someone needs to hit the merge button.

**Martin**
On 1884, I made a PR to make it final a couple of weeks ago. It's still not.

**Hudson**
Ping me and I'll make sure to make those final as long as there is nothing preventing them from going final.

**Dimitry**
There was an official test release, and part of the test were created by the goal client, and the goal client is currently passing the blockchain test and state test. Every other client should download and run through that test before the hard fork. Also, old tests are moved to the legacy test folder. You need to check if its affected by the implementation of the new hard fork, because you could break something in the implementation of the new changes with something in the previous fork. I would like to see more tests. Every client developer is welcome to write more test cases.

**Martin**
I do have one update. There's a new hive that has been deployed. It has changed its URL. I have posted it to the AllCoreDevs channel on Gitter if you wanted to check it out. It's running around the clock, also pulling the latest tests from the test repository. So far the latest are, I think, Geth and Parity clients.

**Brent**
For note-taking purposes, who is karalabe? People are referring to him as Peter.

**karalebe**
My apologies. My name is Peter; I'll write down my last name.

**Brent**
With regard to formalizing EIPs, some EIPs don't need much review, and some EIPs need lots of review, and we need to track how many people reviewed it. And when people review that and find a problem, how do you formalize that tracking?

I just wanted to mention Canonizer.com, as that is exactly what Canonizer is designed for. You can create a topic for an EIP, and you can have the description of what that topic is and a pointer to the spec of that EIP. Then, when people have reviewed it, they can basically sign that petition or join that camp. You could have a white list of people who are approved to review an EIP, and you can apply a Canonizer algorithm that would only count their vote.

Also, if someone sees a problem with an EIP, there is currently no formalized process for someone to communicate that other than go to all the forums and start yelling.

**Hudson**
Yeah, having a centralized place would be a good idea, but as far as Canonizer goes, we talked about this at DevCon, and I think what we should do is have a test vote on the Canonizer platform and put that in the Ethereum Magicians forum, specifically [on the page for the upgrade process, the process for the train station.(https://ethereum-magicians.org/t/a-train-station-model-for-network-upgrades/3721)]

**Tim**
We need to figure out how we're going to get through all the discussions brought up in this call in our next call.

**Hudson**
That will be the main topic in our meeting in a week, as we'll have the fork number by then.  

# Attendees

* Hudson Jameson
* Danno Ferrin
* James Hancock
* Alex Beregszaszi
* Brent Allsop
* Daniel Ellison
* Dimitry Khoklov
* Jim Bennett
* karalabe
* Martin Holst Swende
* Matthias (CSec)
* Peter Szilagyi
* Piper Merriam
* Pooja Ranjan
* Tim Beiko
* Tomasz Stanczak
* Trenton Van Epps
* Wei Tang

# Date for Next Meeting: 4th October 2019, at 1400 UTC.
