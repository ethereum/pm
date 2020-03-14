#  Ethereum Core Devs Meeting 82 Notes
##  Meeting Date/Time: Friday 6 March at 14:00 UTC
### Meeting Duration: 2 hour scheduled, 3 hour actual
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/155)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=kham8c0qhmw)
### Moderator: Hudson Jameson
### Notes: Brent Allsop, Jim Bennett, Sachin Mittal

----

## AGENDA

**Hudson:**
First hour is dedicated to BLS curve signature stuff. We need to get readyfor Eth 2.0. Second hour is for collecting technical updates, community updates and next steps for prog pow.

**Hudson:**
Starting the discussion on BLS signature curve implementation, James Hancock will take over me.

**James:**
For some context on this, the EIP centric model - When an EIP is ready, we ship it, decide a schedule. Coming up is the phase Zero, and the deposit contract for the phase zero of Eth2 and it uses BLS. This is helping us to address some concerns with EIP 1962, and there has been precompiled work by the group on Elliptic curve cryptography.

**Alex Vlasov:**
We made 3 PRs in EIP repos, for [BLS12-381](https://github.com/ethereum/EIPs/pull/2537), [BLS12-377](https://github.com/ethereum/EIPs/pull/2539) and [Zexe Curve](https://github.com/ethereum/EIPs/pull/2541).
So these drafts are largely based on EIP 1962, following the same budget. But are bit more specific. Since there is only one principal difference and implementation of these three is not difficult. I would suggest we accept all three together.

**Martin:**
Does EIP-2537 cover everything needed for Eth 2.0, does it add un-necessary complexity?

**Alex Stokes:**
Yeah, we can add another pre-compile to run more sophisticated applications on Eth 2.0, which will add to the security of deposit contract. Speaking in context of usability, the deposit contract is secure.

**James Hancock:**
So implementing these 3 EIPs will take 1 week, right?

**Alex Vlasov:**
Yes.

**Martin:**
I would like to hear the suggestions of people with more experience in ethereum and cryptography.

**Vub:**
People are really interested in these curves, because so that they can efficiently prove over snarks. And this is useful for bunch of applications as if you want to use zero-knowledge proofs for both privacy and scalability, then your setup will need one layer of recursive snarking.

* TLDR (19:00 - 24:40); Vub, Alex Vlasov, Kobi explains the need for these curves.
* It won't be fatal for the ethereum network in the long term, also it will be very helpful to the developers.

**Martin:**
Just to clarify, the last two EIPs are not related to Eth 2.0?

**Kobi:**
Yes, they are not related to Eth 2.0

**Martin:**
I have two questions, will this be more complex?

**Alex Vlasov:**
In principle, this is less complex than EIP 1962 implementation.

**Louis:**
Reacting to the discussion so far, my concern with EIP 1962 is too complex snd broad to implement. Regarding specific curve, I don't have any concern.

**Martin:**
We have a kind of deadline for BLS12-381, as far as I can understand, the other two curves doesn't. So, I will suggest prioritizing it, and then picking the others later.

**Alex Vlasov:**
Is there any formal deadline? Because the implementation is not very different and I can wrap this up within a week.

**Vub:**
Meanwhile, I have another question on BLS12-381, so if we want to make a Eth2 light client inside Eth 1, the thing you mentioned which is not there is point to map construction?

**James Hancock:**
I think berlin can include just one precompile and others can be included in the upcoming forks.

**Alex Vlasov:**
So what is the deadline for Berlin fork?

**James Hancock:**
It is supposed to be aligned with Eth 2 roadmap. Alex stokes can tell us about it.

**Alex stokes:** T
here is no strict timeline, but we should get it done quickly.

* Discussion about action on these EIPs, refer video for more information provided by Alex Vlasov (30:00 - 40:00)

**James Hancock:**
Thanks a lot for the info. So, 2537, 2539, 2541. Are we comfortable moving them to EFI?

**Tim (Besu):**
We agree with it. Moving all of them to EFI, and focusing on the first.

**Tomasz (Nethermind):**
Thumbs up.

**Artem:**
No Objections.

**Martin (Geth):**
Yes, but we can make EIP 2537 a priority.

**Louis:**
Can we treat the EIP - 2537 as a testground on how we accept crypto into the network. Which means, we will require some crypto people to reply to integration issues.

**James Hancock:**
That sounds great.

**Tim:**
What will be the status of EIP 1962, will it be out of EFI?

**Tim:**
What will be the status of EIP 1962, will it be out of EFI?

**Alex Vlaslov:**
I think EIP 1962, is minimum viable proposal of what people want. So we can let it stay there.

**James Hancock:**
If I am understanding this right, preference is that possible usability difficulty isn't worth possible security vulnerability for having such a large surface for things to go wrong and that when weighing those two, core dev will favours more precompiles overtime as they are needed.

**fjl:**
There has been a lot of design choices, and different implementations for BLS curve. Due to this many alternatives, it can create a lot of discrepancies. So having a fallback base from where developers can choose between options is always nice. So, we should sustain EIP 1962.

**James Hancock:**
Having these new set of EIPs superseed EIP 1962, in an efficient capacity. We are focusing on the first one, BLS since it is part of berlin and essential for eth 2.

* All three EIPs are moved to EFI.

* James - Few updates for the community.

**James:**
Just keeping everyone updated on what is being considered for berlin or what could be possible? EIP 2315 simple subroutine for the EVM, do you have any quick updates on that Greg?

**Greg:**
We are just implementing the code, going over.

**James:**
Okay. Danno isn't here to talk over EIP 2456, which is the time-based upgrade. And then I made a post about upgrading Difficulty bomb, EIP 2515.


**Hudson:**

The **ProgPoW** discussion is to discuss, primarily:

1. Technical updates on ProgPoW.
2. Community approval/dissent of ProgPoW.
3. Next steps for ProgPoW.


* Pro-ProgPoW Representatives:

1. Kristy-Leigh Minehan
2. Michael Carter (a.k.a Bits Be Trippin)

* Anti-ProgPoW Representatives:

1. Martin Köppelmann
2. Matt Luongo


* Representing His Compromise Idea:
1. Ben DiFrancesco


**Hudson:**
We will start with the introduction of the people I mentioned above.

**Kristy:** R
epresenting Ifdefelse here. I am one of the proposers of EIP 1057, my work is both in software and hardware.

**Michael Carter:**
I have hosted a channel on mining since 2013. And I will be representing the community i.e. progpow on gpu mining.

**Martin Köppelmann:**
I have one of the voices against progpow. I am one of the cofounders of Gnosis. And I have been in ethereum space since the beginning.

**Ben DiFrancesco:**
I run a small software consultancy scopelift. We are focused on crypto, I am a software engineer myself. I don't have any strong opinions on progpow myself. I just posted my proposal on Eth Magicians, and here to talk about it.

**Matt Luongo:**
I have been involved in bitcoin 2013, 2014 and with ethereum 2017. I myself has an engineer background, and now I am CEO of thesis. I am on the side of not pushing the progpow.

**Hudson:**
Since the two audits were released, I don't we had a core dev update from ifdevelse on the updates from audits, and an exploit that was released by someone in the community. And the things outlined in the least authority of Bobrao audit, the ECH got going.

**Kristy:**
In the [least authority audit](https://leastauthority.com/static/publications/Least%20Authority%20-%20ProgPow%20Algorithm%20Final%20Audit%20Report.pdf), there were two suggestions. To increase the dag items from 256 to 2512, data item set generated. That we will have a PR hopefully by end of today. There was some work done on how it would affect light verification as well.

The other concern is in relation to keccak implementation, especially the padding around our keccak. So, for our keccak finalisation, the value in the keccak specification. It clearly states we have not added anything extra. So, how we handled the keccak is in scope of the official keccak.

And other suggestions of least authority, were to create extra documentations which is being worked on. And one is to establish a security framework for evaluating ASIC resistance as well as monitoring hardware industry advances is not within the scope of the proposed EIP.

Going through the recent proposed [exploit](https://www.reddit.com/r/ethereum/comments/fe40gq/httpsgithubcomkikprogpowexploit/) by someone on twitter,
Specifically this exploit said that if you have 64 bit in the seed function, you would be able to do a reverse guess on what your proposed node is going to be, and then you will be able to change the extra data field to change the headers and produce extra guesses. It is the exact thing in bitcoin. Kik method doesn’t go through the light evaluation method. Basically, his method has three assumptions,
1. It requires you to have your own node implementation, that differs from the public mining infrastructure.
2. It requires you to have each block’s header hash modifiable - something not provided by mining infra today
3. Need to be able to generate enough keccak to bypass those memory accesses within the block time of ethereum - currently between 12 and 14 seconds (depending on the network state)
None of the above was expected beforehand, specially 2.

Proposed fix:

Current hash mix to consume all 256 bits of the seed produced by the initial keccak round
Having final keccak consume only 64 bits of the seed
Ensures: 256 bits security throughout all stages of the hash
Expected this to be a minimal fix and not affect hashing performance
Alternate solution in works: no need to increase the hash mix to 256 bits and instead ensure the first round keccak not be static and continuously require other inputs

For feedback: reached out on Gitter, a PR on ifdefelse repository, soar designer and other people working on ProgPOW

How the light evaluation method works:

Feasible only if you are able to generate enough dataset items on a tiny ASIC connected to RAM
(according to least authority) as long as dataset items are above 256, this would not be possible
Requires 100 MB of S-RAM - accessible quite fast and in very few cycles
ASICs need to specifically be built just to generate these dataset items
Two possible attacks:
Custom mining pool infrastructure, custom ASIC design - brute force the search space
Generate a bunch of DAG items

**Greg**
appreciation for the quick fix of the exploit

**Martin**
in april, the DAG is going to go over 4GB - which will cause a drop in hash power. ASICs won't be able to cope with that. 40% expected loss. Wants it to be raised
[Louis] adding to Martin’s question: people imagining mining on ethereum is exactly the same as mining on bitcoin - requests Kristy’s opinion on: if limitation of mining power from ASICs on ethereum (in contrast to bitcoin) a good or bad reason to choose ProgPOW

**Kristy**
DAG was designed with the hope that there was continuous pressing need to phase out infrastructure and gently transitioning to Proof of Stake
Keeping the DAG as is is important
Belief that most of the current GPU system in Ethereum is slowly phasing out regardless - simply because of availability of better equipment in the market
Devices;
E3 : specifically designed with 4GB of low profile DDR3, not GPU VRAM, uses a different kind of memory controller. No confirmation if a firmware fix is possible, to actually ensure if it could stay till October. The only confirmation of it dropping off in April is an email confirmation from Bitmain support
A10: uses GDDR6 memory - has a different kind of memory controller. Confirmed, will hash until October, will fall off post that. Have also been collecting orders for a 4.5 GB version device

Concerns:
How many ASICs are on the network: Ethereum could suffer a drastic drop in hash power - not ideal for our block time

This infrastructure continues to be rebuilt and put up in Eth1.0 ecosystem

**Alex**

Questions:

It just requires about 100 mb of SRAM to make such DAG attacks feasible
But conclusion was this amount of memory is not available
Doesn't look like its not available from tech perspective
(referring to Least Authority Light evaluation method)
This amount doesnt look high for tech to be implemented - easy to make such hardware - and make that hack

**Kristy**
SRAM is quite expensive - not only transistor cost dependent, but also company dependent and the current supply time and supply chain
SRAM is about 20x the cost per bit as DRAM

The biggest concern is that it is not as accessible as you would think.
1. Due to those supply chains, S-Ram is mostly used in other kind of configurations they have preference.
2. It’s not about having the memory, but having to do it at a low voltage and with power efficiency because S-RAM is quite power hungry. And it is more feasible for ASIC manufacturers to ignore S-RAM and go for GDDR5/ GDDR6 since it is cost effective.

My main concern is S-RAM is not available to broader community, and is in very specific places. Due to the lack of supply, and high price. Also, S-RAM doesn’t support GPU. So, it creates a difference between ASIC and GPU miners.

**Alex Vlasov:**
I think it is possible to make custom ASIC chips for mining, explains how TL;DR

**Kristy:**
I agree that it is technically possible, but it is not economically viable because the cost of your ethereum ASIC is not just that S-RAM with 100 MB. There are a lot of other parts required to build it. However, ASIC manufacturers doesn’t have much experience working with S-RAM. We only have two who are experienced in ethereum mining space, which is bitmain, and innosilicon.

**Kristy:**
When it comes to DAG. So, when it came two years ago I strongly believed that DAG should be kept in place because we want that gentle transition over to casper FFT. Most of the ethereum mining infrastructure is on 4gb GPUs. But miners have slowly upgraded to 6gb GPUs due to surge of different applications. BBT, how does things look on your advantage point?

**Michael Carter aka BBT:**
The community has been progressing from 4gb to 6gb to 8gb. And I would not like to disrupt it with a science project. Since it is tied very close to the point of implementation would be at a point where the current block is. The block refers to the DAG size, any science project would not be more successful than the current mining scene is, from an upgradation point of view. Now, on the AMD side, it is from 8gb to 16b for the miners. So, from an implementation point of view, we are good on the mining scene. I think most people are expecting things by fall of october.

**Trenton:**
With DAG going above 4gb, exceeding the miner’s 4gb hardware. So, progpow doesn’t do anything for that?

**Kristy:**
Correct, it doesn’t affect the DAG size at all.

**Ameen:**
Which hashpowers are going offline, GPUs or ASICs?

**Kristy:**
Yeah, we are working on the report for the same. Essentially, 40% of the network will go offline which is tied to the E3.

**Ameen:**
And E3 is 4gb ASICs?

**Hudson Jameson**
Let's go ahead and wrap up the technical discussion. Greg, you had a comment on the process, and I want to make sure you were heard on that since you've been vocal in the comments of the agenda on that.

**Greg**
I don't think that's relevant until after we've heard from these people.

**Hudson Jameson**
OK, sounds good to me. We'll reorder that then. So let's go ahead and get to the part where we talk about community approval on dissent. So how this has worked before was in January of 2019, ProgPoW was put into accepted state, and that was an indication from the core developers that it would be included in a future hard fork. It would move to final state once it is implemented on the network, using a hard fork network upgrade. And since then, there's been the Istanbul hard fork and Muir Glacier that did not include ProgPoW. And then recently it was brought up that because ProgPoW is in Accepted state, it would need to be included in a future hard fork. So since then, there has been dissent from the community because they felt like this was kind of sprung upon them. So I wanted to hear from the anti ProgPoW side as to what your perspective on this dissent is and how you would formulate it as a summary. And we can start with Martin if you have that opinion, - if not, we'll go to Matt.

[**Martin Koppelmann**](https://youtu.be/kham8c0qhmw?t=5651)
Sure. So I would start with why I personally was and am against it, and then provide a community perspective on the governance process.

I was against it and vocally against it from the very beginning. It was never a technical opposition. I just thought that the proposal himself, the goals of the proposal, are nothing of what I want. Basically, my view on things is that the core promise of Ethereum is reducing the platform risks. So whatever people want to build on top of Ethereum or around Ethereum, they can do it. And they can have extremely high guarantees that what they build will not be made worthless by the platform making an arbitrary change.

So I personally never had any investment with ASICs whatsoever. I'm not invested in any form. But if I would have done that, I could totally see that three years ago I would have made a decision to build an ASIC for Ethereum, and I would definitely not have felt that I was doing something wrong or illegal. So if now the platform decides to kick me off, I would totally feel screwed. So in my view, there can be exceptions or situations where Ethereum has to make a change that effects users negatively if it's an extremely clear advantage for Ethereum or if it's a situation where the survival of the network is at stake. But in my view, as long as those things are not the case, then those types of changes that badly affect some people should not be made.

And with ProgPoW, it's not even clear to me why ASIC resistance is a good thing. So there are a bunch of arguments that ASICs are in a way even closer to Proof of Stake, the thing that we all want in the long term because ASICs requires an upfront capital investment. There are those arguments. Then there is the argument that it's not even clear whether ProgPoW would guarantee ASICs, so do we even want ASIC resistance, and it's not clear if ProgPoW achieves ASIC resistance.

And as this recent exploit that was published yesterday shows, it's quite likely that it was possible until recently to build an ASIC even under ProgPoW, and it would make the situation much worse. Because now, if ProgPoW would have been implemented the way it was proposed until two days ago, the incentives, if you can then manage to build an ASIC, to not publish it and to have kind of this monopoly that we're afraid of, are much higher, because you would never want to share it, because you would know if you if you share it and it becomes public that an ASIC exists, Ethereum would fork again. And basically, this guy who released this report said something like, "I finally decided to release it,"" so he was clearly indicating that he or she was aware of it for a long time. And to me, it seems like the only reason why he now released it was because they were thinking, "Well, ProgPoW is dead, anyhow, and so now I can say it."

Those are some of my personal reasons to be against ProgPoW, but the current state doesn't matter. That's not the critical thing. The critical thing is that from where I sit, the majority of the community is against it. So there was this letter, and just to name a few projects where our founders and many of the people behind the project all came out against ProgPoW. And I'm currently not aware of a single project building on Ethereum that says "we want ProgPoW." So from where I'm sitting, the majority is against it, even if that's not even the majority and just kind of a large minority. Even that would be enough for me to say what we can't do ProgPoW. There's not consensus to do it.

The other question is, "Is the governance process broken?" And to me, it's all perfectly fine. So to me, the criticism of Ethereum was sometimes that a small committee is unilaterally making decisions. And my view is that the small committee exists, it is this call we are now on, and it usually makes a decision, and people in the community very much trust those decisions, and so far, they have always kind of accepted it. And to me, it's a very positive thing that we actually see there's not a blind trust, but there is still this second step that after this committee makes it suggestion that there's still this community approval. And so far, it always happens, and I expect it to happen most of the time in the future, but if once in a while, stuff is rejected, then I think it should just be rejected, and we should move on.

**Hudson Jameson**
Okay. Just so that we can get through everyone speaking, I'm going to have Matt add on to that to wrap up this portion of the anti side to give an overview, and then I'll get to Christy and BitsBeTrippin on their perspective on why it should go in and any kind of quick rebuttal they have on that. So, Matt, do you want to add on any of the thoughts that maybe were missed?

[**Matt Luongo**](https://youtu.be/kham8c0qhmw?t=6074)
Sure. Thanks.  So I have a slightly different take.

I'm actually not technically against ProgPoW. What I'm against is this kind of governance mishap of what felt like a closed issue to the community not actually being closed. I know it doesn't feel like it to you guys who have worked on this for years, but it feel like we're moving way too quickly. I do not think that the upside of ProgPoW, which to me is unclear, is worth the downside of a community split. That's really the crux of my argument, outside of tech and outside of whether or not we think ASIC resistance is viable. I think that this is really showing us the cracks in governance.

I don't blame any dev for being frustrated that there are random Twitter mobs that appeared, but these things happen because there's not a great place to have these conversations, because many people in the community don't feel heard, and because, frankly, a lot of us who do pay attention to these calls and who have been on these calls in the past were still surprised ProgPoW was still a thing and still moving forward and still a topic of discussion.

So what I see here is a lot of parallels to what I saw in Bitcoin in 2016/2017. I saw a group of entrenched developers who were doing their best and trying to serve a project. I saw a bunch of unhappy companies who wanted something that may or may not have been better for the chain, and as well as a split with miners. And what I don't want to see is that this will fall back to how crypto governance always falls back, which is voice or exit. Right now, we have community members who are trying to voice. We're being told that this isn't the right platform everywhere we tried to talk. There's not a right place. We're being denigrated and called just influencers. There's an assumption that none of us are technical or not, in my case, a professional engineer, so there's this real split, and I'd like to see us step back from that and reconsider whether the social split is worth pushing an uncertain technical improvement, or if we want to go the other way, which is exit. I do know that there are at least two teams who are ready to support clients that do not include ProgPoW. I do think that it shouldn't go that way.

My last point is that in the past, on a chain like Bitcoin, we had a bunch of communities try to come together and sort of force a hard fork, and it didn't work. And for Bitcoin, that was great, where in Ethereum, we have a ton of incredibly stateful projects that I believe will actually be the ones to decide the majority chain. I believe that Tether, Maker, any security token, all of these folks have a huge economic incentive to be on the right chain. And if they decide that is that is a no-ProgPoW chain, it's going to be painful. So, personally, I think that we should avoid the issue. I think that we should either work on a much smaller tweak if we believe that ASIC resistance needs to happen - it could even be something that happened semi-annually - or spend the next year actually educating the community and consider rebranding ProgPoW and convince the stakeholders that feel like they've been cut out of this process that this is the right move. And maybe we can heal the rift. So that's my thing.

**Hudson Jameson**
Okay. We'll start with a BBT and get your perspective, and then Christy and whoever else on the call wants to speak.

**BitsBeTrippin**
Yeah. No, that sounds good. I want to actually echo some of what you were just saying there at the end, Matt. I think at the end of the day, it comes down to the health of a network. And I think, as an outsider from the technological side of it, initially being very skeptical of it two years ago, doing my own testing on this particular algorithm, trying to deep dive in to some of the other ancillary effects that would happen with changing from EthHash. At the end of the day, it comes down to the community understanding from a platform side what's worth the risk. And being in this space, and being in mining since 2011, seeing the different phases of GPUs, ASICS, FPGAs, it comes down to the stability of the network and what's best for the transition when things go to Eth2.0.

Everything in my space is telling me from my experience that if you create an environment that limits the exposure, the risk of an infraction or a split is far greater. So I look at it from a participation standpoint, the ability to participate on this network or not - nothing more, nothing less. Taking a more conditioned approach that involves the community members, they've said what they're concerned with from a stability standpoint, this being kind of dark for a little bit and then just being reintroduced. Even for myself not tracking,I thought it was essentially dead in the water, and then we talked that, "Hey, it's gonna go forward."  I understand the perspective, and I respect the concern that the community is talking about. I think, on the other hand, we have a situation where we have a high confidence that a majority of the network are not a majority - let's say 40%. At the end of the day in April, we're going to know the impact of the ASICs that were on there. At that point in time, if there was a decision to move forward with any fork when you're looking at one community, ironically, that's the time to do it, because now you don't have the the infiltration of anybody else that's involved in this at that time. You don't have that contention of one hardware versus another of splitting.

I would say that we take the next month and really break down the concerns for Maker and everybody else that's on there from a participant developer on this network to understand at the end of the day, as we're still holding proof of work, it is still Eth1.0, that a rebranding of making something like ProgPoW plus all the fixes that we're talking about, the kick discovery, all inclusive of an EthHash 2.0,  and, you continue to pound on it and make sure that it's the right thing for everybody. We need to get everybody on the same page.

Bottom line, this thing is not going to go forward if you have a majority of your contributing ecosystem on this platform against it. But I want to make sure that everybody has a clear and concise understanding of what happens if you've centralized, or allowed the centralization due to the supply chains. That's nothing against ASICs. I have nothing personally against ASICs. I've said this for years on my videos. But it is the fact of the matter of a limiting the participation, and then you're gonna have a huge economic incentive to not move to something like Eth2.0

Everything that I have related to this subject, I'll put it on a Medium. We can have a more civil discussion. But I kind of echo Matt's piece with regards to let's make sure we can answer some of the growing concerns. But I think for the health of Ethereum, and for the ability for individuals to be able to participate in this space as they've done since 2015 that understand the vision of 2.0, that it's a healthier narrative to move towards the ability to participate. I'll let Christie take it over.

**Hudson Jameson**
And then Ben can discuss real quick what he's written up and get the feeling of the room among the participants in the CoreDevs what we're feeling here.

So, Christy, go ahead.

[**Kristy Leigh-Minehan**](https://youtu.be/kham8c0qhmw?t=6638)
Sure. I want to start by stating that ProgPoW was really developed due to the ecosystem that was around in 2018. There were numerous EIP proposals around ASIC resistance when the E3 had first been leaked by a CNBC analyst. And we were a little frustrated by each proposal because they were short-term bandaids on a much longer-term problem. Most mining algorithms have not being correctly designed for hardware, and thus coin networks often get decimated by these devices, and then they lose their their community and a lot of their value.

Ethereum was a different beast in 2018. In 2020, we have a significant portion of gaps that are now dependent on a stable network, and the last thing we want to do is actually have a chain split. My biggest concern is ensuring that we're at a time right now where new investment is going into the 1.0 chain. Based upon my vantage point in the community, and I do some work on some research projects right now - 2.0 related. We know that 1.0 needs to be as secure as it can possibly for the foreseeable future. I don't see it suddenly disappearing in six months. And so I would like to see a very secure 1.0 chain.

I would also like to see in the 1.0 chant chain be something that all sorts of devices and all participants can use, given that mining is very much a user on-boarding experience into cryptocurrency. And there have been multiple videos and content produced in the last two weeks, with miners telling their stories of how they discovered Ethereum. Mining often acts as a gateway drug for that. So the intention of ProgPoW -  and, agreed Matt, we should have just called it EthHash 2.0 - the intention is number one to strengthen EthHash is an algorithm to help ensure that the original goals stated in the yellow paper are met, and to help ensure that the playing field is level between a fixed function mining ASIC and a GPU ASIC. And so eventually, if people do build mining ASICs, it does not push off your GPU community. It doesn't block miners coming into the ecosystem and new participants coming in and earning Ether and ensure it remains an on-boarding experience for the ecosystem.

I will state that right now, ProgPoW is in its proposal period. It needs to go through implementation and testing after implementation. It needs more eyes on it. And I think the last two years, a lot of the people that have worked on ProgPoW have simply gotten burned out because as SolarDesigner summarized it best when he was working on reviewing ProgPow, he said that he's losing motivation, because if you don't know whether your work will be seen or adopted, you slowly lose a lot of motivation to keep spending time on it. I do think if a path is put forward where we say, "Hey, we want to strengthen the 1.0 chain," we can get a lot more community feedback. We can get a lot
more people working towards solving this problem, and we can get a lot more eyes on the proposals as well. And nothing is ever perfect.

Finally, I do not believe that ProgPoW should be treated like any other technical upgrade, but it needs to be done in a way where all participants in the ecosystem are comfortable and understand what the repercussions may be and how it works. And again, have not done a very good job on educating people on the mining community as a whole and how mining really does strengthen an ecosystem for a coin.

**Hudson Jameson**
Okay. And then finally, Ben, let's get your quick summary on what your proposal was.

[**Ben DiFrancesco**](https://youtu.be/kham8c0qhmw?t=6939)
Okay, great. I'll try to be quick on the proposal and the motivation behind the proposal.

As I mentioned awhile back in my intro, I really don't have a strong opinion about ProgPoW. I can see both sides of the issue, and I think there's an argument to be made on each side. I think a lot of considerations are unsettled or open research questions in terms of what the impact of ASICs are on the long-term health of the network on the transition to Eth2.0, and I really think it's kind of a toss up, and I think that's why this split has occurred. If there was a clear answer one way or the other, I think the community would come to consensus around that. Since there's not, we've seen this kind of divide.

Given that this divide exists, though, and the people on each side are very convinced, I don't think the path forward anymore is to simply expect that one side is going to convince the other, at least not in the short term or at least without new information becoming available in terms of effect on the network or impact or new ASICs being developed, or things along those lines.

So given that, I think that the way forward is, it sounds like everybody wants to avoid a chain split. And I think it's also clear that everybody wants to have the best outcome for Ethereum, the best security for the network, and the clearest path to a transition to Ethereum 2.0. So given those common grounds, even though we disagree on some of the details on what the best path forward is and we're unlikely to convince each other, then a compromise solution where no one is particularly happy but we focus in on those shared goals seems like the best possible path forward.

Given that, the proposal that I put forward is basically one where ProgPoW should be fully implemented and tested across all the major clients, but that it should not be included as part of the Berlin or any other future upgrade hardboard. Instead, the client should be implemented such that there's a command line switch which enables ProgPoW to be enabled by the operator of the node at a specific block height specified by that operator. In addition, a ProgPoW enabled hard fork of the Ropsten test network should be created and maintained using that switch, so we would have a full blown Ethereum testnet using ProgPoW that all clients would have to support and function properly with henceforth.

And then the final point here is that a strong shelling point should be encouraged in the Ethereum community that if there was ever clear evidence of an ASIC-led attack on the network that Ethereum stakeholders would coordinate to activate an emergency hard fork at an agreed-upon block height using the switch that was implemented.

So the reason I'm here is, again, because we share those goals to secure the network and keep it decentralized and transition successfully to Ethereum 2.0, we focus on achieving that and using ProgPoW and recognizing all the work that's gone into ProgPoW and its goals, but instead of using it as the active mining algorithm on the network which right now is possibly risky and doesn't have clear upside, to the point that several people have made, instead, we use it more as a kind of Sword of Damocles, or a sort of insurance policy. So essentially, if ASIC miners do attempt to fork Ethereum 2.0, or if there is any other kind of clear attack on the network, we have a very ready option to hard fork the network quickly and with the coordination of the community and coalescing around the idea that that would be necessary.

Now, a couple of points. Folks have brought up weaknesses in this proposal. One is, what is that clear signal? How do we recognize when a so-called attack is happening on the network and when a split needs to occur? I think that it would be valuable to have more conversation around this. That said, I don't think there is any way to fully lay out exact criteria ahead of time for what that would entail. If there was, we could just write the code to do that ourselves. It is, almost by definition, a value judgment.

And so, in some sense, this doesn't completely end the debate around ProgPoW. It attempts to push off ever needing to use it on the network by adjusting the incentives of would-be ASIC attackers. But it does leave open the door to the possibility that continued debate and discussion will occur around if a hard fork should occur due to what is perceived by some as an attack but perhaps by others as not.

I don't think there's any way around this. At the end of the day, we're either going to have a chain split, or we're going to coalesce as a community around around a clear need to do one thing or the other, And so what this does is hopefully avoid that future ever taking place, but at least gives us a path forward right now that recognizes the work of ProgPoW and attempts to leverage it in a way that better secures the network and the future of the network and then allows us to continue the messy process of decentralized governance down the road.

So that's the summary. And I'm happy to take any questions.

**Martin Holst Swende**
Yeah, I have a comment on that. One thing that I think is an underlying assumption with this compromise model is that in the event over an activation of ProgPoW on short notice, there will be GPU hash power standing by ready to take over the mining. And I think that may not be true. I think they will be slower to actually reestablish themselves for Ethereum mining if some time goes by.

**Ben DiFrancesco**
I think that's a fair point and an open question. I guess the the worst case is that the difficulty drops very low and so the reward is a clear incentive for GPU miners to to come online and come back onto the chain. Obviously, there would have to be some degree of coordination around this anyway. So I imagine that large, GPU mining pools would be aware of it ahead of time, but we wouldn't know until it happens. Again, the intention of the proposal is that this option would never have to be used, but that it would be used in the case of a clear emergency where the downside risk to the network due to an attack of some kind was so clear that these kinds of risks in terms of no available GPU hash power were worth taking as opposed to dealing with the status quo.

**Martin Koppelmann**
Martin, where's this concern coming from? So my current understanding is that currently, the assumption is that right now, today, 60% are GPUs and 40% are ASICs, and it's quite likely that actually the ASICs won't work in two months anymore, so we will then have a significantly higher share of GPUs. So where does the concern come from that there are no GPUs available?

**Martin Holst Swende**
I guess the concern is not in two months time, but more like maybe a year from now. Obviously, there will be new developments happening.  

**Martin Koppelmann**
That brings me to another point that I was saying we should focus on Proof of Stake, and we should focus on starting to communicate the transition period to Proof of Stake, where mining rewards decreased over over time, because that alone would prevent people from now doing large investments in six or eight gigabyte ASICs. So as long as there is a somewhat clear path within the next one or one and 1/2 years there's at least a transition or the decrease of mining rewards starts towards Proof of Stake. And then I think that's a much more effective way to mitigate ASIC dominance.

**Greg**
Do we have a solid engineering plan for that transition? It could be two years. It could be four years. We don't know.

**Martin Koppelmann**
Well, that's why we should spend time on that one and not on ProgPoW.

**Artem Vorotnikov**
Actually, the same could be said about implementing ProgPoW as an option for the mainnet because the proposal is that it already assumes that all the developers of all the clients are willing to actually implement the readiness for the switch because there are a lot of other EIPs that need attention right now, and I'm not sure if ProgPoW is the most important to the network.

**Ben DiFrancesco**
I just want to weigh in briefly there. As a software engineer, I'm not deeply embedded in the development of any of the clients, Eth 1.0 or 2.0, but just as a software engineer, I don't think you can just assume that the development time is fungible like that. Just not how it works. So I think that's a little bit of a non sequitur or not as critical as a point as some might think.

**Hudson Jameson**
And I believe that ProgPoW is coded and go. It's pretty far along. I think we got estimates before that it would take about a month for the current ProgPoW to be coded. Could anyone remember if that's right? For every client.

**James Hancock**
For some context, the Geth PR is 40 lines. As far as clients go, it's a trivial change to make.

**Artem Vorotnikov**
Fixing ProgPoW bugs, is that a trivial change, too?

**Hudson Jameson**
The ones we have currently, yeah.

**Kristy Leigh-Minehan**
As bugs are discovered, as you saw with our response to this one, that takes roughly six hours. And then it's a lot of careful testing. Yes, they're trivial to fix. Again,ProgPoW is actually not that many lines of code. It's just tweaks to the EthHash algorithm. And Martin Swende is probably the best person to talk about the work required to put it into a client since he implemented it in Geth. Martin, are you able to comment on how long that roughly took you?

**Martin Holst Swende**
I think I did it in a couple days. A week. But I was also basing it of off the [unclear]() implementation that you guys had.

**Kristy Leigh-Minehan**
Which was not ideal. It was pretty bad. That was my work. Sorry.

**Martin Koppelmann**
I just want to remind people that hard fork is clearly not just a technical process. Hard fork basically means creating a narrative around it and convincing roughly 20,000 people at the same time that this is the best thing to do right now. In that sense, every hard fork costs that kind of community attention. And said in those terms, I think this attention should be spent on many other EIPs like Geth changing the Geth pricing switch to Proof of Stake. And that's where we should direct resources and community attention.

**Kristy Leigh-Minehan**
Correct me if I'm wrong, but, for instance, in Istanbul or Berlin, aren't those bundled EIPs that then become technical upgrades, which is technically a hard fork?

**Hudson Jameson**
Yeah. You're defining it correctly, in my opinion.

**Louis Guthmann**
Can I just add a question for for the no-ProgPoW part of the discussion? Coming from the drop we're going to see in a month, I'm neutral on the topic and kind of worried in the future if ProgPoW doesn't get accepted or if we drop ASIC resistance. We are going to see, according to Kristy's numbers, 40% of the hash power. And because of the way hashing works in Ethereum, it means that somewhere in the future we're going to kick out the entire GPU's former ecosystem. And we are going to be dependent on ASIC makers to keep making ASICs. Aren't we putting the network at risk that at some point the price of that is not interesting enough for those makers for those constructors to make those machine to have the network stop.

**Martin Koppelmann**
So your first concern is 40% will drop, and then your next concern is the 40% drop is ASICs dropping out?

**Louis Guthmann**
No. One kind of ASIC.

**Hudson Jameson**
No, the other one's GPUs are dropping out, too, Martin.

**Louis Guthmann**
Yeah, here's my concern. In April, we're going to see Eth3 dropping. Which means, according to Kristy's, numbers, 40% of the network. If we go this way and I don't know if Kristy can give us GPU [unclear]. If we leave it that way, it means that probably we're going to kick out all the remaining GPUs by -

**Martin Koppelmann**
Wait, wait, wait. So a 40% drop out of some ASICs will, first of all, mean higher profitability for GPUs, so it will mean GPUs can run longer and more of them can run. So that will, first of all, be a good thing for GPU miners.

**Louis Guthmann**
Great. But that's not my point. It also means that the other ASICs are going to be also more profitable, so they're going to produce more. And at some point, GPUs because they're less efficient will be not as profitable as running an ASIC. Do you agree with me on this one?

**Martin Koppelmann**
No. I really don't see why we wouldn't have any GPUs anymore.

**fjl**
So the main reason why ASIC resistance might be important to Ethereum is because we do not want to become 100% dependent on ASICs to do all the mining. And as far as I understand ProgPoW, it is mostly that by leveling the playing field between GPUs and ASICs in a certain way, it means that we will basically continue to have GPU-based mining on Ethereum. If, in the long run, GPU mining becomes way less efficient than mining with an ASIC because the ASICs keep getting better or whatever, and basically we'll be a bit screwed, because people won't deploy the GPUs on Ethereum anymore.

**Martin Koppelmann**
In the long run, we just switch to Proof of Stake.

**Louis Guthmann**
Martin can I just comment on one point you say about moving to Proof of Stake. As I'm working on Eth1.X, in my day to day, Eth1.x should be a contingency plan for if anything goes wrong with 2.0, and we should think about Eth1, day to day, independently of Eth2.0, because we are going to do any change to make the transition happen, but in the meantime, Eth1.x should still exist until proven that we don't need it anymore. My concern that I'm expressing is if we are killing the GPU economy by not moving to different algorithm - I don't care about ProgPoW - then aren't we going to be dependent on the supply chain of a small number of ASIC makers, which can, and at the position of Bitcoin, because ASIC can go obsolete technically, shouldn't we either just stop the growth of the DAG or do an another algorithm? That's basically my question.

**BitsBeTrippin (Michael Carter)**
Louis is actually correct. And to talk specifically to the four gigabytes that are about to knock off the current Eth3s on the network, your best time right now, or our best time, is to get these fixes in, propose EthHash 2.0, and change before more capital investment is invested into creating those ASICs, because the incentive is there when nothing is done, and more ASIC will be created. And we'll have a situation where we're going to be re-talking about this with some of the - I wouldn't even call it anti ProgPoW, just forking off people's capital hardware, right? Because people are making investments where you have a natural attrition right now about to occur where you're gonna have a majority of GPUs on the network not having ASICs on the network. But the longer we wait, we're gonna have ASICs on the network, and then we're gonna be right back in that circular argument of, "Well, we don't want to reduce these people's capital investment."

So I hear the argument of saying, "Well, GPUs are gonna become more profitable." It's not about that. The incentives are built in, and the equilibrium gets created around power costs around either ASICs or GPUs. The bottom line is we have a known event that is going to occur here in the next month, where you're gonna have a majority of one particular capital investment that's gonna fall off the network. So I think the discussion should be if we're gonna move forward with having some algorithm adjustment, we shouldn't start moving to de-incentivize that activity of, "Hey, we're moving forward with an algorithm change, and it's probably not gonna be economically incentive do this particular algorithm with the ASIC via EthHash 1.0. but EthHash 2.0, here's the spec and standard we're moving to, if you're gonna make any capital investment, you should start planning for that." And now you have a level playing field, and you have ASIC makers that can start making particular pieces of hardware for EthHash 2.0.

[**Ameen Soleimani**](https://youtu.be/kham8c0qhmw?t=8161)
That's the same thing three times. I'd just like to jump in here and state some opinions, some of which just seem so obvious, it's kind of gut wrenching that I even have to. First of all, pro-ProgPoW people are a bunch of profit seeking miners lobbying the CoreDev political committee to get what they want. Right. Full stop. That's what this is.

Second thing. As a Proof of Stake maximalist, I'm very excited by the prospect of miners becoming stakers, but I have absolutely no sympathy for miners of the GPU or ASIC variety. In the long term, the intention has always been to show them the door. I don't really see why they feel entitled to a say in governance.

The CoreDevs that have so far been trigger-happy with ProgPoW have not accurately taken into account the risk of bugs. I no longer believe they are to be trusted, especially given the exploit that was revealed recently only when you the person thought that ProgPoW wasn't going to move forward. Anybody who thinks that code change is trivial is not taking this seriously.

Another point is, last year, when I was responding to ProgPoW, the claim from the CoreDevs was it's just me, me personally, me and a handful of Twitter people, this is not what they would categorize as contentious. But now there are far more people outspoken against it, including the CEOs of both Synthetics and Compound, not to mention Koppelmann's comment that not a single DAP team has come out pro-ProgPoW. And it's like, What have you guys been doing for a year? If you haven't been able to convince a single DAP team to come out and say, yes, we we want this.

All right, and then further, it seems like a really silly to risk a chain split in the short term by implementing ProgPoW in order to avoid the risk of a chain split later from ASICs. When we transition to Proof of Stake, it's sort of madness.

**Hudson Jameson**
I think to your third point, there's no one's suggesting that we do it any time soon. In fact, people are suggesting more compromise toward figuring things out.

**Ameen Soleimani**
Right. Just a minute. One more point is that I actually support Ben's compromise, despite having him blocked on Twitter. I don't know, probably said something and pissed me off awhile ago, but I support the compromiseto keep ProgPoW in our back pocket and and use it eventually, because for me - irrespective of really the the 40% of Eth3s going offline, that actually makes this argument stronger - is that there's no good reason to do ProgPoW right now.

There's really no good reason why you should do it right now because the main argument for putting it in place is really that it'll fuck with the ROI calculations of ASIC miners, right? If it's not worth it for me to deploy an ASIC right now because I believe that ProgPoW's going to go in in six months or nine months or one year, then it's as good as doing it today. So anybody who is pro-ProgPoW should  have the opinion of, "Let's do this in six months or nine months or 12 months because that's actually the best for network security." But because they are profit-interested miners, they're saying, "No, let's get this done as soon as possible." They wanted to get this done last year before they even realized that there was a bug in it.

It's like all of these positions, not necessarily the people, but the positions are sort of insane if you actually try to align them with the stated goals, but they make a ton of sense if you just assume these are profit-interested people.

**Louis Guthmann**
In that case, would you agree on freezing the DAG size?

**Ameen Soleimani**
I don't know. I haven't given that too much thought.

**Artem Vorotnikov**
If I may, I have a question. Is anyone from the pro-ProgPoW camp, are they willing to fund development of ProgPoW in other clients, for example, Open Ethereum? Because there has been a lot of talk about what other clients are supposed to do...

**Martin Koppelmann**
Funding is not the problem.  

**Hudson Jameson**
It's already it's already in /OpenEthereum. Just to be clear.

**Artem Vorotnikov**
Yes, but if any bugs pop up, who's going to fix that?

**Hudson Jameson**
The Open Ethereum team, unless..

**Martin Koppelmann**
Will do that. We can do it. It's not a technical problem. It's a funding problem.

**Tim Beiko**
The one problem, I think at that comes up a lot is, yes, working on ProgPow is not mutually exclusive with working on Eth2. But one thing that it is mutually exclusive on is, you know, time on these calls and significant mental energy from a lot of people in the community. And if we spend another year trying to debate this and coming up with EthHash 2.0 or ProgPoW 1.1 or whatever, I think that's one thing we want to try and do better. And personally, I think this is why I would almost be more in favor of something like Ben's proposal. Because at least it gets us to commit to something fairly quickly, and we can reduce just the argument time so that we don't spend half the CoreDev call for the next year discussing ProgPoW.

**fjl**
It sounds like everyone is in favour of the flag, right? So can't we all just agree to implement the flag?

**Matt Luongo**
There's the other part where we actually come up with some sort of agreement as to when we think that we should trigger the flag. Otherwise, we're just going to make it really, really, really, really, really easy for anyone to organize a chain split.

**Martin Koppelmann**
For the record, I also think I'm having it available in case of an ASIC attack, there's nothing that hurts with that. But implementing it as a flag definitely makes the likelihood of a split higher because there are definitely entities, including exchanges, that have an incentive in splits and kind of a new coin.

**fjl**
So in that case, it is basically going to remain in the exact same state it is in right now, where we have implementations which are kind of ready to deploy. There might be some some more work that could go into that. But we basically have, like in most clients, there is an implementation that could be included at any time behind a flag or not, to make ProgPoW work. We are already at the stage where we basically have it. We just don't officially have it.

**Peter Szilagyi**
So just merging some version of ProgPow into every client and then waiting for some event to trigger it, I think that's a bit dangerous, because what's the guarantee that ProgPoW still works in five years time? So if we want to go down that path, and I would probably, possibly, maybe suggest running a testnet with PogPoW just so that the code is actually live somewhere, otherwise somebody will just accidentally re-factor something, break it, and nobody will notice until we want to use it.

**Ben DiFrancesco**
That's part of my proposal, and that's specifically why it's part of my proposal. So I think we should have a fork of the Ropsten testnet that implements ProgPoW, and that all clients should have support for that testnet moving forward.

[**James Hancock**](https://youtu.be/kham8c0qhmw?t=8658)
So there's a lot of talk about ProgPoW or not ProgPoW,  but something t we haven't talked about and I'd like to hear from the anti-ProgPow team is the EthHash vulnerability, which is the light hash evaluation method, wasn't known, and it is now known, and to that camp, is that something that's worth addressing? Is having a patch that vulnerability as part of EthHash something that they're interested in without actually separate from the issue of ProgPoW?

**Trenton Van Epps**
The key first step here is that this was released, if I'm correct with the audit last year, and it kind of just sat there. Some people knew about it and were aware of it. But it hasn't been communicated in any depth to the general public why they should care about this, why this is a significant concern. If we are going to move forward with EthHash patch, that would be the first step. I don't think we're anywhere near that, and it's going to seem like a kind of a bait and switch at the last minute that actually, there's an EthHash vulnerability that has to be patched.

**James Hancock**
Well, I've been trying to have this conversation, but it gets very smashed down by ProgPoW and then a whole bunch of things. So that's why I'd like to specifically address this.

**Hudson Jameson**
Yeah, what's the chance of that becoming an issue? If anyone can comment on that from a technical level, or has it already been implemented?

**James Hancock**
And the willingness of the anti-ProgPoW team, that is that a valuable Proof of Work change? Because I can hear from them that it isn't, that ProgPoW isn't a valuable change, but is patching EthHash's vulnerability valuable?

**Matt Luongo**
I just want to be clear. I don't necessarily think ProgPoW isn't a valuable change. It's just that I'm weighing how valuable it is relative to a community split, how valuable it is relative to the education campaign that needs to happen, and the additional diligence that needs to happen before we do it. So I do think that it's a lot more palatable to have a tweak to EthHash. I'm not proud that something like that would be easier than maybe it's something that we think is better and more forward looking, but I don't know if I would support it. Obviously, details matter a lot, but I'm I'm not against smaller EthHash tweaks to fix faults.

**Trenton Van Epps**
James, the only point I would make is this light evaluation method, correct me if I'm wrong, it basically removes the memory hardness or it allows ASICs to bypass the memory hardness of EthHash, which means there could be ASICs on the network, which a lot of the anti-ProgPoW side isn't necessarily opposed to. Is that correct?
**James Hancock**
This is a very different brand of ASICs. And a 10x more powerful ASIC is very different than a 1.2 or 1.5 or a 2x, which is what we've seen. So is that a concern? I'd just really like to hear from Martin if a Proof of Work change that patches a vulnerability of EthHash is a palatable thing for him and the community he represents.

**Martin Koppelmann**
I don't represent any community, and I can't make an opinion about something I haven't heard about, and I have. I don't have an opinion about it.

**Hudson Jameson**
So we'll have to ask the broader community through EthMagicians. And actually, a lot of what we're talking about today will probably culminate on Ben's EthMagicians post and other posts that'll pop up. So I highly encourage people to jump on there and avoid trolls, because the magician's forum is generally avoided by trolls because it's dense.

So, yes, at this point we've gone well over time. So to wrap it up, we don't have a process in place for putting an EIP on hold for the accepted state that it's in right now or reverting it. I don't think we have a process for that that's super clear. So because of that, we need to discuss that process today, and what the core developers want to do, because despite anything the community wants to do, the EIP process currently dictates that the core developers decide what state a core EIP is in. So obviously they need to take perspective from the community. The community does have a say in this from a collaborative perspective, but they don't change the status of the I. P. So is there anyone with an appetite to try to pragmatically change the state of the EIP or, pragmatically, not change the state of the EIP?

**Greg**
All I would say about it, no pro or con, just that it's in the accepted state. If we want to move it to another state, we need a consensus of the CoreDevs to do that.

**Ameen Soleimani**
I'll do it.

**Hudson Jameson**
Ameen, you're not a CoreDev.

**Ameen Soleimani**
Can I be a CoreDev?

**Greg**
No, you're not a CoreDev.

[**Lane Rettig**](https://www.youtube.com/watch?v=kham8c0qhmw&feature=youtu.be&t=8984)
The EIP is in an accepted state.  Is there anything in the current EIP process that specifies a timeframe within which an EIP must be accepted into a hard fork?

**Hudson Jameson**
No there is not.

**Lane Rettig**
One option here is what we in the US call a “Pocket Veto” where it is in an accepted state, but we choose to never move it out of that state.

**Hudson Jameson**
From a process perspective, that sounds palatable to me.


**James Hancock (and Hudson):**
We could supersede ProgPOW with a new EIP that would be the updated version that Kristy is refusing in conjunction with Ben’s proposal.  We could possibly call it Ethash2 and work towards coalescing and answering questions with that.

**Hudson Jameson**
As far as wasting time in core dev meetings, core devs don’t have time to spend on social stuff, like many of us do.  A lot of people have been talking about maybe having a seperate community governance call to help with miss-communication and lack of community involvement to make sure the community is heard and give things legitimacy.  This will be developed over the next few months to a year.  With that amendment we will be able to better discuss this and answer these types of unknowns.

[**Hudson Jameson**](https://www.youtube.com/watch?v=kham8c0qhmw&feature=youtu.be&t=9135)
Are there any other comments, not to solve everything, but to achieve some agreement from both sides?

**Tim Beiko and Hudson Jameson**
A conversation about the fact that the EIP is still in draft.  The fact that EIP hasn’t been updated to what the core devs agreed on is just a procedural issue due to champions dropping out.   BitsBeTrippin is slated to complete this update.  

Ameen Soleimani asked about what is required to become a core dev.  Hudson indicated we can talk about this off line.

Tim Beiko and others again asked for clarification of the current state of the EIP.

Hudson Jameson replied: “It is currently in accepted state and nothing has been changed on that.  There has been a suggestion to make this what is known in the US as a “pocket veto” and then to supersede it with another EIP, possibly called Ethash2, that are improved, memory hard, etc.  These are only suggestions, and there is no further movement on the EIP status, today.

Martin Holst Swende commented that there were “core dev code of conduct” violations, and that this is not acceptable.  Hudson Jameson agreed.  He will be talking to Ameen and putting in more things to prevent this in the future.  Armeen commented that he wanted to better understand, as he thought he was showing restraint.

Matt Lounge thanked everyone for having this discussion in this call.

**Kristy-Leigh Minehan**
I just have a few questions to ask, anyone can answer via twitter or eth-magicians.  I want to know what the pro ProgPow community needs to do so we can be more helpful.  Guidelines on what education would be helpful to the broader community as a whole would help.  The whole point of ProgPOW is ASIC resistance.  I would like to have more of a discussion on whether we want ASIC resistance or not, which stems back to the principle in the original yellow paper.  This needs to be answered by the community before more investment.

**Martin Koppelmann**
I would like to flip this question and ask what the community needs to do to get the ProgPOW people to no longer push it.

**Stefan George**
I would like to add to this, that you may be underestimating the community a bit.  There has already been a lot of education in the last weeks.  People signing the petition are well aware of all arguments that have been made.  It really comes down to the question of whether we want to be ASIC resistant or not.  The people signing the petition are willing to take the risk.  I am worried that this could go on for a very long time and be a waste of time.

**Kristy-Leigh Minehan**
The [“EIP 2538” letter](https://github.com/MidnightOnMars/EIPs/blob/master/EIPS/eip-2538.md) (not a real EIP) missed a lot of the arguments.  It’s not about favoring anyone, it’s about leveling.  There hasn’t been enough education...

**James Hancock**
I clarified that part Kristy.  Trent was saying there hasn’t been education on the vulnerability of Ethash.

**Kristy-Leigh Minehan**
Got it.

**Hudson Jameson**
Thanks everyone for the stuff that has been said, I think there needs to be more discussion.  We’ve made progress since the beginning of the meeting.  For everyone that has just joined, there is agreement that ProgPow Isn’t going in any time soon (within the next 3 to 6 months).

Greg Colvin was concerned about this “agreement” thinking it was still “on track”.  Hudson, Fiji and James Hancock clarified that: “It was absolutely not going into a hard fork any time soon.  Being accepted is very different from being scheduled.”

[**Hudson Jameson**](https://www.youtube.com/watch?v=kham8c0qhmw&feature=youtu.be&t=9595)
As far as the core devs go: Where do you think we’ve come to?
Martin (especially), Vitalik, Peter, Felix, Thomas


**Felix Lange (fjl)**
We've come to the conclusion that the community really, really, really doesn't want it. And for me personally, this is a very strong sign. There is a technical argument to be made for ProgPOW. There is a social argument to be made against power. If we cannot reach consensus on all sides about what the change should be, it cannot go in.  I’m not willing to put in the change with so much community resistance, regardless of where it is coming from.

**Hudson and fji**
Community resistance is outside of the process, but it is important to listen to pushback.

**Hudson Jamison**
Kristy and BBT have said, Actually, this is summarized well in the group chat.  Accept EIP 1057 and ProgPOW gets deprecated for adjustments of the kick fix, plus adjustments included in 0.9.4. This transition to Ethash 2.0 as a new EIP that has yet to be written which will supersede ProgPOW EIP 1057.

That's what has been suggested. Do we have any core Devs that are saying that's a good idea? Because I was kind of getting that impression earlier, but I don't want to be speaking out of term or saying, you know it is when it isn't.

**Felix Lange (fjl)**
I would say it is a good idea to rethink it and start a new EIP, maybe call it Ethash2, at least after the revelations about these two attacks, they definitely have to be addressed on a technical level before we can move forward with any new algorithm.  These things have to be taken care of anyway. So. of that new EIP is going to be called Ethash2, maybe it sounds better.

**Hudson Jameson**
Yeah. I mean, like, that's not entirely the point of it. Just sounding better. But I would say I think the core developers need to speak up more personally because otherwise this is gonna get rehashed. And you all are the ones who are deciding if this goes in on a technical level.

**Felix Lange (fjl)**
From a technical point of view, we have implementations of this. There has been a test net. A lot of the research has been done.  ProgPOW is not causing anyone to do technical work and in Ethereum clients right now. All the work is basically on Christie's and If Def Else’s side, so they are more less actively working on it.  People should not get the impression that core devs are prioritizing work on ProgPOW over anything else.

[**Hudson Jameson**](https://www.youtube.com/watch?v=kham8c0qhmw&feature=youtu.be&t=9784)
Okay. Any other comments?

**Tomasz Stanczak**                 
Maybe I'll give a summary from Meta mind. So it's quite clear or at least it’s my standing. And so one question comes from the ProgPOW proposal. This is not about the ProgPOW itself, but about the notion of an ASIC resistance. In general I'm in favor of basic resistance. As for ProgPOW definitely we want to deprecate the EIP that was not addressing the recently discovered issues with ProgPOW and should replace it with a not properly fixed version and then wait for the next series of reviews. Also I would encourage anybody who wants to push ProgPOW to just spawn a fork for a new testament based on ProgPOW so people can actually play with it.  We have the existing client limitations, which I believe are Go ethereum and Parity.  Nethermind does not have at the moment support for ProgPOW. However, I believe that the ProgPOW support in Nethermind can be added without much effort. On the short notice in case the decision is made. The fact that we do not have ProgPOW support does not imply that  we do not support it, that is just because we believe that technically, it's not a big effort. But we've seen so far that it was  unlikely for the ProgPOW to be implemented in a very short time frame. So We're not privatizing this. Thanks.

**Hudson Jameson**
Thank you. Anyone from Geth wanna comment before we go or open ethereum, actually, that would also be a...

**Martin Koppelmann**
Yeah. I mean, from open ethereum, I guess I would comment that we will try to develop for the needs of the community.  From where we sit the needs of the ethereum community are not ProgPOW, but other things. So we would develop other things.

**Hudson Jameson**
Okay, Geth, if you don't have one. That's fine.

**Peter Szilagyi**
I don't think I can pick a side at this point.  Honestly, if the community really doesn't want to do this then as Filix said we don't really want to shove it down anyone's throat. However, I kind of do stand on the point that if we figure as core devs, tech leads, what have you, that   ProgPOW may be useful in the future, and I still think we should pursue just getting the implantation done properly. So either we should say that ProgPOW is dead.  We don't care about ASICs go for it. In that case, we can drop ProgPOW and be done with it. But then let's accept that and publicly say that: Yes, we know ASICS will come and we don't mind them, the more the better. Or if we say that we don't want ASICS long term and if ASICs cause an issue then we should definitely step up against them.  I do think that we should at least take the code seriously and make sure that it works.  So that if there's a need then there's a way to to actually do something meaningful. So that's kind of my personal opinion on this. But I don't want to speak in the name of the team because I know that Mark and the team might have a bit of a different opinion.

[**Felix  Lange**](https://www.youtube.com/watch?v=kham8c0qhmw&feature=youtu.be&t=10031)
I think that the decision as to whether or not ASIC resistance is important for Ethereum is  purely a social decision with a lot of social factors.  So it would definitely help to have more opinions on ASIC resistance from everyone. And that includes the much, much wider community.

**Hudson Jameson**
Okay, anyone else have final stuff before we go?

**Ben Di**
I just wanted to make one quick comment on I think for the last number of minutes here on this call, or at least at some point during the call, we were kind of falling back into the trap of trying to convince each other and, um, either two sides trying to convince the other side on guy. Really, I just feel as if we're past that point and no one is likely. There's there some portion on each side of the debate that is very unlikely to be convinced by any just argument barring some kind of new information were changed to the state of the network on, So I really think that to move forward as a community, we just have to accept that, even if it may be frustrating on some of on some sides, except that there are two sides that are unlikely to be convinced without some dramatic new information and then consider pats forward, that makes sense given that leave, that is the baseline. And I say that not just with regards to ProgPOW specifically, but with what's just been being discussed over the last few minutes, which is that we have this kind of, uh, you know, what the right word is maybe a philosophical issue about whether or not we want ASICs on the network. Andi, I think part of the reason, as I mentioned earlier, part of the reason why There is no clear why there are two sides on this issue is because there aren't clear answers to this. I mean, the whole space is only 10 years old. We've only seen a few major networks evolve like the coin that has become completely a sick dominated. We don't really know what the long term game theory is, and it's completely changed by a bunch of specific details with regards to Ethereum, the DAG, the transition to Eth 2.0. So we're not going to solve that problem. We're never gonna come to a consensus on that. Um, unless again there's dramatic new information and I think we just need to take that as a given and move forward, knowing that we're not going to convince each other on that point.

**Hudson Jameson**
Okay, Tim.

**Tim Beiko**
Yeah, I was just going to say, and this kind of echoes what you just said, Ben, Like, I agreed that there's like, some fundamental kind of philosophical differences. It's probably kind of pointless to try and resolve them, and I think maybe one concrete thing that can be done. That kind of signal that, like there is a move forward, is if there is like a new proposal, like I would really kind of favor having a separate EIP.   It might sound superficial, but I think having like a separate EIP, that's kind of started to do some of this that has, like, a eventually different name. I don't have a strong opinion on that, but like, Yeah, it seems like we discussed a lot of, like, really interesting changes and that seemed to have some buy in from a lot of people during the call. And I don't think adding those on top of the current ProgPOW proposal, socially makes a lot of sense.

**Hudson Jameson**
Okay, let's wrap it up. It's already over. Gonna apologize for the time going over and also for earlier, when I was trying to do a recap of everything, I don't think that's my role. I don't think I need to say what's been decided or what hasn't been decided. Necessarily. Every call. I think everyone's heard everything today and can come up with their own conclusions, just like the community should do with this rough consensus model. I should just be here for process primarily and for organization of the calls. So yeah. Great talk, everybody. Thank you all so much for being here. Really, It's been super important. I feel like and I think there will come a fruitfulness from this. Things will be fruitful from here on out. Hopefully, and, uh, we'll see you in two weeks. Thanks, everybody.


# Attendees

* Alex Stokes
* Alex Vlasov
* Ameen Soleimani
* Artem Vorotnikov
* Ben DiFrancesco
* BitsBeTrippin (Michael Carter)
* Brent Allsop
* Daniel Ellison
* Felix Lange (fjl)
* Greg  Colvin
* Hudson Jameson
* Ian Norden
* James Hancock
* Jim Bennett
* Kobi Gurkan
* Kristy-Leigh Minehan
* Lane Rettig
* Louis Guthmann
* Martin Holst Swende
* Martin Koppelmann
* Matt Luongo
* Peter Szilagyi
* Stefan George
* Snakethe4xor
* Tim Beiko
* vub

# Date for Next Meeting: 20 March 2020 at 1400 UTC.
