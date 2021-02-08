# Ethereum Core Devs Meeting 81 Notes
### Meeting Date/Time: Friday 21 February 2020, 14:00 UTC
### Meeting Duration: 2 hrs.
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/152)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=zSRzlC_dCx8&feature=youtu.be)
### Moderator: Hudson Jameson
### Notes: Pooja Ranjan

----
	
# Summary
    
## EIP Status 
EIP | Status
---|---
EIP-2464 | `Last Call`
EIP-1057, EIP-1803, EIP-2384, EIP-2387 | `Accepted`
EIP-1380, EIP-2046, EIP-2315 | `Eligible for Inclusion` 
EIP-1702 | `Eligible for Inclusion` Pending Champion. Not scheduled for Berlin 
EIP-663, EIP-2348, UNGAS | Depends on EIP-1702 
EIP-1962, EIP-1559, EIP 2456, EIP 2515 | Discussed under `EFI`. Discussion to be continued in EthMagician thread | 
EIP-1985 | Discussed under `EFI`. Decision required around needing a Hard Fork 

*Note: Removed EIPs accepted in Istanbul.*


## DECISIONS
	
**DECISIONS 81.1**: EIP 2315 is moving to EFI.

**DECISIONS 81.2**: Revisit EIP 2456 as EFI. 

**DECISIONS 81.3**: James to discuss more around EIP 2515 

**DECISIONS 81.4**: There is no way can to confirm the EIP 1962 is going in, clients have serious concerns implementing. They may coordinate something in ETH Paris. 

**DECISIONS 81.5**: Berlin would happen when the BLS pre-compile is ready, ProgPOW would happen the next third Wednesday after that.


## ACTION ITEMS

**ACTION 81.1**: Ethereum blog to announce officially that ProgPOW is being adopted because of the decision of all core devs.

**ACTION 81.2**: Zach will share better communication methods to interact with the Open RPC team. 

**ACTION 81.3**: Hudson will merge PR to change the state to Accepted for EIP 778 and EIP 868. 



-----

**Hudson**: Hello everyone and welcome to the Ethereum core devs meeting # 81. This is Hudson.Let's go ahead and start with this. This is going to be a super packed agenda today so let's try to be cognizant of getting through your topic really quickly and with like minimal interruption and not too much off topic discussion when it comes to the technical aspects of it. It can be talked about it in Gitter or The Magician's just make sure to keep that in mind.  Thank you all very much.

We were going to start with EFI but is anyone here for open RPC cuz I remember from last meeting we said that we would start with that. Is anyone here for that? Okay, we can skip that for now. 

# 1. [Eligibility for Inclusion (EFI) EIP Review](https://eips.ethereum.org/EIPS/eip-2378)

**Hudson**: Let's start with the EFI stuff and I'll just tag team this with James, is that okay with you James?

**James**: Yeah I would actually discuss any of the EFI or EIPs that are looking to be in Berlin and then have general EFI discussion happen after.

**Hudson**: Okay, do you want to just take it away?

**James**: Yeah I can do that 

**Hudson**: Thanks!

**James**: Let me grab the agenda so I have the list of the number of EIPs. For a Berlin coming up, there's been a couple EIPs that are almost ready to get in and then there has recently been the Eth2 deposit contract is looking to use a precompile so they can validate the BLS curves within the contract a self which they can't do in Solidity so that gives us a schedule to schedule around. so the EIPs that are close to being ready and then that the EIP should be at a scheduling window. the ones I have seen at that stage would be Greg's EIP,  Greg Colvin [EIP-2315](https://ethereum-magicians.org/t/eip-2315-simple-subroutines-for-the-evm/3941), 1962 or the BLS one that the Eth2 team has created a proposal for a simplified version that only has that curves that they need so we can talk about that at the time that happens. we can do that as the last EIP and that list, then there's Danno's EIP which is about scheduling but with block time for the forks and just making you so it's easier so we can predict when those happen. then there is the difficulty bomb EIP that I wrote for updating the difficulty bomb changes, the algorithm and that one is [2515](https://ethereum-magicians.org/t/eip-2515-replace-the-difficulty-bomb-with-a-difficulty-freeze/3995). So let's first go into, Greg are you here? 

### **[EIP-2315](https://ethereum-magicians.org/t/eip-2315-simple-subroutines-for-the-evm/3941)**

**Greg**: Yeah I'm here.

**James**: So we can talk about that one first as possibly for inclusion for Berlin and then after this discussion we can  talk about scheduling and then we also can talk about ProgPOW, which is on the agenda today as well. 

**Martin**: Sorry, if I may,  I think it's wrong to say to talk about inclusion for Berlin, I think we should talk about Elligible for Inclusion. When the test cases exists and implementations work, we can see what upgrade window it goes. I don't we should do that we've done previously and say this goes for Berlin and then hold everything just something that doesn't make it. 

**Greg**: I agree, we need to get the implementation much closer to ready and then say let's go!

**Martin**: I do agree that we could make call today and say yes we're all for this EIP or some other EIP, go for it. 

**James**: That was more of what I was intending. As far as the scheduling goes, the only one to really figure out when it could happen is the  signature for the contract and then whatever ends up is ready by that time can also be. It's just really helpful for me to get an idea of who wants to kind of hit that timeline and if and then as a group are getting the general okay for that, not saying it will or will not good. 

**Greg**: Could you remind us what the timeline is?

**James**: Greg, the other Greg are you here, from the Eth2 team? The Eth2 deposit contract was it supposed to be July I believe, July 29?

**Tim**: I thought, maybe I'm wrong here but I thought that the Eth2 Beacon chain launch was suppose to happen around July, which means deposit contract would probably be weeks to months before that. I think June is probably right.

**Alex**: Yeah I should mention that 1962 else has a complete implementation, it's not a show stopper.

**James**: Yes, so, the bigger conversation is by June which of those could be ready so that the deposit contract could be made and then which of the EIPs could would be what we accept as an EFI for that kind of before for that so the authors of the EIPs can either get ready and make it for this window or make it in the next window, well as the next Fork happens. Is that kind of feel alright, Martin, the way I said that?

**Martin**: Yeah!

**James**: So then for Greg's EIP, is there any updates and do we have the sentiment that if it was ready at that time that it would be able to go in.

**Greg**: It's fine by me but I'm not currently implementing a client. so I say Martin, Allen who else Danno here.

**Hudson**: Yeah, Danno is here. Greg, can you like provide a 2 sentence overview of what you're EIP again, just as a reminder. I see there's a lot of new people here today.

**Greg**: Okay, the proposal is out there. essentially it adds 3 opcodes at this point possibly to, just to begin, subopcode to mark the begening of a subroutine. Martin I've been discussing that maybe just a jump test would do but you have to have something to go to and then two opcodes, one of them is just jumpsub or subroutine and the other one is return sub back for most implementations you would simply have a return stack so when you jump to a subroutine, you push the current PC onto the stack and when you return from the subroutine you pop the stack and resume execution where you jump from. and so it's really just that simple. It's a two stack design, so it's basically getting EVM
up to 1970 standards.

**Alan**: Just want to add something to Greg's comment. I think that's pretty standard. Also, we're going to support (?) with some modification. So I think this is a good EIP.

**Peter**: One thing we've been discussing Martin about is that on the surface, it looks really nice, we're wondering how much time would it be to hack Solidity, so that I actually can use this, so that we might try and run some benchmarks against existing contract. because it will be really nice to see the actual number of what this would mean. 

**Alan**: Yes but it's up to the solidarity compiler to do the changes and it has nothing to do with any Solidity language level modifications basically just a compiler change and the EVM change. 

**Peter**: I know, my question is, it seems that the whole point of the subroutines are to make the ? of code faster. But, it would be really nice to actually confirm that it doesn't make it faster before shipping it.

**Greg**: Is anyone here from Solidity? 

**FJL**: Doesn't sound like.

**Alan**: From the perspective of the compiler, I think, a (?) based compiler can support it very easily.

**FJL**: The request was not to have all the compiler changes ready just before the hardfork including the EIP but the idea was that it is unclear if it provides an actual benefit to the performance of let's say Solidity smart contract. I think it will be very good to validate this EIP before deploying it in a hardfork by basically just trying out the changes, the EVM changes are implemented at this time so it is possible to actually spin up a small laptop network, use a modified complier and then run some benchmarks. This is basically we were thinking on the geth side would be the next step for this EIP. because it is such a low-level change and I think it desrerves to be evaluated before inclusion.

**Greg**: Okay it's unfortunate the solidity people haven't come.

**James**: I can help connect with them. I am assuming  that we have this the Solidity benchmarks is there any opposition to having this in or strong feelings?

**Martin**: We discuss this in the Geth team and I think the whole support of this is prove it to be eligible for inclusion. one other thing though, Greg mentioned, another stack, part of stack, is kind of big change and is another showstopper in our opinion. another thing worth pointing out is that if we do have the beginning data, sorry, begins sub opcode, it means that when doing the jump test analysis, we also need to Mark out  begin subs, for geth this is easy, we do a ? pass and mark code sections and data section but for the other implementation which specifically look to jusmp test opcode, they would have to either convert to our style or would have to do one more jump test analysis, basically begin sub analysis. 

**Greg**: At the end of the EIP there's an example laying out, how subroutines are going to show up in the assembly code but I think it's pretty clear there the the difference in gas count, actual measure performance. I think would have to be better but that would have to be measured but certainly it's going to save on gas substantially.

**FJL**: Yes, We're expecting the same thing, **it would be just nice to have a number to confirm the same thing before we ship this EIP**. 

**Greg**: Of course 

**James**: Let's add that as the next step for the EIP and consider that good?

**Hudson**: Sounds good to me. 

**Peter**: I've a quick question though, I think there should also be an implementation of the EIP in the Geth code base?

**Greg**: There's a PR.

**Peter**: The EIP mentions 3 opcodes where the implementation does 2?

**Greg**: Yeah, the implementation is earlier.

**Peter**: That's fine, I was worndering which one is the canonical version, then the EIP.

**Greg**: Yes I did the PR earlier just to be sure that things would actually work going into Geth.

**James**: Great!

### [EIP 2456](https://ethereum-magicians.org/t/eip-2456-time-based-upgrade-transitions/3902/11) 

**James**: Danno, do you have any updates on your EIP? I'm not remembering the number right now.

**Danno**: 2456. One thing I was thinking of the possible change. I don't think Jason Carver is on the call. We think of going back to 1000 blocks to check if we might have too much load for lighter client that don't shows that many blocks. What didn't occur to my mind is we don't have to go back to 1000 blocks to check the trigger, we could go back to 10 blocks to check the trigger. 10 blocks can be far enough for the owners to trigger the upgrade. That is one change of consideration. I haven't gotten any feedback on on that particular suggestion. Whoever is hovering over far to look back is and whether it's good to be 0, 10, 10000, probably this discussion can be on the Eth Magician than on the call.

**James**: Assuming that number gets worked out and then you have that conversation with Jason, Dano, is there any strong feelings about having this be included or not included after that point from the group; that's more of what I would like to get out of this conversation?

**Danno**: I think we need some testing. The current testing structures for these activation that don't think provide the support we are looking at. So,  I would support some updates to the reference test styles. I'd also like to see some live transition before we go to a testnet. There is more of a testing burden on it than it looks like.

**Martin**: Maybe in particular because testing scenario we going to run into problems but we have to use synthetic time, right?

**Danno**: Yeah, I think it's long time.

**James**: I think, he means that you have to do fake times in order to test of the time is actually happening, right?

**Martin**: Yes.

**Danno**: I think of focused testnet where have people come on, have a few miners, kind of ? to fork and show at the other testnet for sure ( recording is unclear).

**Martin**: Yeah I was thinking more about the actual test cases. Maybe that's no problem because that can just ignore the system and use the old timestamps, for all blocks so that's not a problem.

**Danno**: Yes, the time stamp is not actual not a block centric. We control the set up of data to validate as well.

**James**: So for testing in the live transition things, is that something you see as could be done in the next month and a half ? or that you would be wanting to pursue for hitting a June window ?

**Danno**: I think we can come back in two weeks and make sure what kind of support we have.

**James**: Okay!

**Martin**: A question for me, I can't really make it how it does? Is it with EIP 2315, So far only I am from the Geth team who gives a thumbs up, would that be sufficient? I would assume no?

**Hudson**: I think Danno said good. I've a question for Wei or  anyone who was on the parity team like Parity Ethereum client team, what is your involvement right now in the open Ethereum initiative? Is that something that we should consider you guys having a up-down opinion on this cuz what I heard was the parityTechnologies won't be supporting parity Ethereum / open Ethereum after Q2?

**Wei**: We will still provide support for open Ethereum for at least the next Hardfork and there are lot of other teams for example Gnosis, they are takinf a lot of development job over. so I think **Open Ethereum should be considered to be a usable implementation for Ethereum**.

**Hudson**: The question wasn't as much that cuz I knew it was going to continue as more can I turn to like you or someone else from the team ? ask for and up or down on certain questions like if EIP 2315 is okay for the client? I think you're the only one from Parity here so you might be the one to given up or down, if you're comfortable with that?

**Wei**:  Yeah you mean the EIP for the..

**Hudson**: The simple subroutine, the one Greg has? 

**Wei**: Yes, I assume that should be fine for us, that require act for stack. I don't see any problem.

**Hudson**: Awesome! and then I don't know if Nethermind is here today that would be the only other really active client, except C++ who doesn't always come to these meetings? Am I right James or whom am I missing?

**James**: That's right. Trinity?

**Hudson**: Oh that's right. sorry, Trinity that's another good one. they've been focusing so much on being syncing 1X. I forget when they come to the calls.  who's from the Trinity here? most of the time they're good with stuff so they're not here I think we have enough teams saying that it's okay to move ahead  with Greg's EIP as an EFI.

**Martin**: Cool! Sorry for interrupting James, you can continue.

**James**: Oh! that's perfect. So **Greg's 
EIP which is the number 2315 is moving to EFI**. Dannos EIP, did we move it. I believe we had like a general thumbs up but you wanted to talk to Jason. Could we move it at that time or do we say we're going to move it after that time.

**Martin**: I'm not sure we did officially thumbs it up, did we?

**Hudson**: I think we did last time. I thouht we officially said, it's an EFI meaning we've given a thumbs up for it being a good idea. You know what actually you're right. I don't know if we did or not. Danna do you remember? 

**Danno**: I didn't think we give it a EFI.

**Hudson**: Okay, sounds good. we can continue to not have it in that status as as long as you haven't talked to Jason.

**Danno**: I think it's such a fundamental change that it shouldn't be considered. 

**James**: So then let's wait for that [conversation](https://ethereum-magicians.org/t/eip-2456-time-based-upgrade-transitions/3902/10) to happen and then we can revisit this as EFI.

**Danno**: Exactly, we come back in two weeks and I'll try to get a hold of Jason.

**James**: Okay, so that is it for that EIP.

### [EIP 2515](https://ethereum-magicians.org/t/eip-2515-replace-the-difficulty-bomb-with-a-difficulty-freeze/3995)

**James**: The next one, I wrote a proposal for this one, 2515 which is an EIP to address the difficulty bomb or update it. I wrote the proposal last week and send it out and had a lot of good feedback from the core devs and people on Twitter and the general idea is to have a have a block activation number where the difficulty freezes and after that point increase the difficulty at a consistent rate and so we so there is an eventual that leads off until eventually the network can't support, the block times becomes too big for the network. I'm not exactly sure how to run a conversation on an EIP that I'm doing so maybe that should be you Hudson.

**Hudson**: Sure!
The EIP 2515, is it even in draft right? now it looks like it's just written.

**James**: It's in a PR, hasn't been merged.

**Hudson**:  Perfect! I was just making sure that I'm on the right page. All right there's a few things, my assumption is you're not a client dev so you wouldn't be able to put this in, but I think that's as far as implementation and testing goes. let's just talk about, just a paragraph or two, the general idea of how this is laid out and then we'll get some opinion and then after that we'll see if there's a lot of support, some support, no support, that kind of thing.

**James**: So that the general layout is the difficulty bomb has gone off a few times. Sometimes due to moving a chain by having to delay of fork,  so it goes off for a while and then most recently it went off because I had miscalculated it and then it wasn't double-checked; we weren't sure when it happens and that's primarily because the difficulty bomb adjust is affected by the network. there's the adjustment factor that happens within the the block by trying to make sure it is between **10 and 20 seconds** and when the difficulty bomb is unsurmountable by that adjustment period depends on the current difficulty on the network. Because we don't know what the difficulty be will be the future, we can estimate it and there was a great calculator from Ethermine.

**Hudson**: Ethermine or they have like three names bitfly, Ethermine, Etherchain. 

**James**: They made a great calculator for predicting the difficulty bomb as it is now. It still relies on assuming what the difficulty will be at a certain time, and over time that will be more accurate. and I think it would just be a lot easier if we removed if we split those two abstractions and kept the difficulty bomb because as I've heard from the community there's a lot of people who have strong feelings about keeping it but we can at least make it more usable for knowing when it will happen and have in its effect and so it's easier if we can address it easier as core devs. 

**Hudson**: So any questions on that, anybody have comments?

**Martin**: As I understood first, we would freeze the difficulty. You're also talking about some linear increase? 

**James**: yes the original proposal was to freeze the  difficulty and leave it at that. but after feedback from the community it made sense to have it freeze and it linearly increase at that point. At block  10500000 the parent difficulty equals the block difficulty, the block difficulty equals the parent difficulty + 10% or + 1% and that will just continue to increase. 

**Martin**: Is that reflected in the actual and specification on the Ethereum magicians  or anywhere else?

**James**: It's in the PR. I just need to read it, it's in the PR,  yes. I need to write that the PR has been updated on The EthMagicians. This is also after talking with TJ for a long time at Denver, who was one of the big critics of my approach. 

**Martin**: Yeah as for my part, I think this is kind of a good trade-off between removing it's entirely and having it in this current form which obviously isn't that great. I 'm tentively positive but I'd love hear other people's take on it.

**Hudson**: There might be a situation where people need a little more time to read it and if that's the case, I'd say it's a good idea James to just shop it around to the different teams in the all core devs gitter or just people you talked to individually and then if it's in draft status by next meeting that would be good to do.

**Tim**: I have a question maybe this is a dumb question but wouldn't like freezing the difficulty and then linearly increasing it make, it kind of goes against the whole difficulty adjustment so I am not sure I haven't read the whole EIP but maybe just trying to clarify how those two mechanisms would like to interact. SO, what's like the trade-off of not having the difficulty adjustment and the potential security implications?

**James**: The difficulty adjustment would be removed after the point, back to block activation.

**Tim**: Yeah, that's what I mean. It's kind of a toy scenario, say you freeze the difficulty and then 2X the amount of miners start mining on Ethereum, you know are we going to have 7 second blocks instead of 15 second block because our difficulty is kind of Frozen. I understand over the time, it will grow but if the amount of hash power kind of grows quicker than the rate at which the difficulty bomb slows the network, we have like a quicker network. 

**James**: You're totally right and once it's frozen there is an incentive for miners to jump upon assuming that the main chain is the one we're talking about right now. to jump on and increase the hash rate in because the difficulties now adjusting up slowly but it would like block times would increase quite a bit for a short amount of time they would accelerate their Pace into the linear increase and the risk there is that if blocked times are too fast the uncle rate could be high enough to result in sort of a fracturing of the network. Just block time becoming very very quickly for a short time until eventually there is enough miners 

**Tim**: I think the mining reward would also paying for that, right? like how profitable is it for them and what not. but to me I think that's like one one thing right like to see someone who understands is much better than me, like the various incentive and talk through to the possible cases like what happens if  there's like fifty percent more miners, there's like half of miners. Because we kind of lose this like by  dynamically adusting parameter.

**James**: I wrote a little bit about that in the EIP as well. 

**Tim**: Okay cool.

**James**: Is there any other thoughts on that before we can decide more on it in the next week, next two weeks?

**Martin**: I'm curious as to **why freeze at all** and not just the linear increase from certain point in time ?

**James**: Freeze to me is removing the difficulty adjustment piece and then they will just linearly increase and that's right. is that what you mean ?

**Martin**: No, not quite. I meant. Why not instead keep the adjustment and also add not an exploding bomb but linear increase bomb which has less chaotic effect. 
ex. once we hit this new soft bomb it starts to target 15 second time block time and then 16 second block time and then 18 sceond block time, but doing so in large hopes. 

**James**: The reason that I think that would have the same problem is not really being able to predict effectively when that first increase would happen ?because as long as the difficulty of pieces in there and the increase is some static function that can adapt to it then there is this requirement to guess or to predict what the difficulty of the network is. In other words to be able to predict the effect of the bomb.

**Martin**: I think what I'm proposing would be to instead just change the desired block time, remove the bomb and modify the desired block time.

**James**: **Because the adjustment algorithm only adjusts up and down depending on if it's between a 10 and 20 sec block window**. we don't really have a capacity to target a block time, as far as my understanding. we have an equilibrium that happens because of how the mechanism. if it's below 10 seconds then and then it increases the difficulty, if it's above 20 seconds then increases the difficulty for every 10 seconds above that. so I don't know, how we could we can move that window? the other concern I would have with that approach is the people that are most affected by this going off at work for us for it going off is the miners in there and that isn't that never was really the intention of the difficulty bomb was to make it to minirs are less able to pay for their electricity that month. so wallet is less impactful for us we are also not if it's really an impacted by having block times increase in the same way as other stakeholders on the network so making it so it is more real to us what the consequences are as in visceral for us and in this room, then we who are the ones who can address it will also be more likely to address it, in a timely manner. 

**Hudson**: Any other comments? we can probably just go to the next one and **just shop it around some more**, I guess. James, that sounds like a good idea to me.

**James**: Yup, I can do that and if there's a way to Target like that Martin I would definitely be open to how to make adjust the mechanism to be targeted around that. I just wanted to figure out how that works how that would work.

### **[EIP-1962 Updates](https://github.com/ethereum/pm/issues/152#issuecomment-586653678)**

**James**: Then the next EIP is Alex Vlasov, you're here, correct?

**Alex**: Yes. Just following the discussion which was on the last call. Peple want to get someone outside of this call and implementation EIP every time. so I have invited a few people. Zac and Kobi are here. Unfortunately, Joseph from EY couldn't join due to personal reasons. I got an email from him an hour ago. Also, unfortunately, this week wasn't the best one to get more people because it's time for blockchain conference and it's 6 a.m. in here. We've two people who are actually interested in getting something new in terms of elliptic curve and cryptography are here. In general, a gas price is calculated  to increase of constants of gas per second. Now it's 30, even it's way above what my laptop press beyond precompiles. Current implementation is beyond precompile...In principal all implementation are ready in Rust, C++ and Go. I think Zac or Koby can say something.

**Zac**: Yeah, I had a couple of thoughts. I wanted to give external viewpoint on the value of this EIP, quite a big company working in this space. The current pre-compile situation means that it's difficult to deploy the state of the art for cutting-edge cryptography to Ethereum. Especially given the amount like there's been a lot of new development units that have come out in the past year that we can't currently leverage because of the limited pre-compile support. I see this EIP as way the future proofing Ethereum. It can become a test bed for the advanced cryptographic techniques. That one should provide a lot of values to the community, to the wider ecosystem particularly in the form of roll-ups and for more using stocks and snacks for proof of date availability and the scaling. There's also been some research lately that highlight the facts that if you want 128 bits of security for snarks through a lot skin incisions that kind of things. The BLS 1238 curve is not really sufficient. So while stay, it would be a big improvement for Ethereum to support to. With BLS 1238 precompile, the ability to use more secure caps, I see this EIP would be extreemly valuable. When it come to implementation, I am having a few thoughts. I just echo what Alex said, it is a complicated EIp and there is lot of potential attackes that needs to be fleshed of, but fundamentally it's new cryptography that's being deployed or new techniques and also the teams that would be using this precompile as part of the tech stack, they will have quite a significance and they would also be providing auditing, validating the codes, they wouldn't be treating it like a blackbox.. 

**James**: I can see the value of it I think all here agree the value of it. the concern is how do we do it in a way that is secure, given previous experience. so if your organizations are others could not audit in the formal way but can look at the implementation and look at the specification and just say yes, both of these things yes both of the things are lining up as a vote of confidence for those things that would be very helpful for us.

**Zac**: Yeah we would be happy to do that.

**Martin**: I would like to **voice some opposition** here. I've done it before. I'm opposed to this EIP because it's so broad and sorry maybe the wrong wording. it is very huge, it's generic precompile. It's basically virtual machine for modern crypto which I don't think suitable for Ethereum. I think we should add pre-compiles for well-defined use cases and if we need some particular precompile for some well defined use case such as ZCash interoperability, or Eth2.0, then we can add a precompile for that. I think, its too large stuff to take to add this big generic precompile. There're **several concerns** 
1. is the actual crypto correctness and there I can only trust the cryptographers that know what they're doing. 
2. the other large concern is that these are extreemly large codes. Even crypto is right, there may still be mistakes in the implementation. 
I briefly looked at the code the golang codebase, and 12 days ago there was a commit which fix a simple mistake that said "copied value into the wrong destination in one edge case". it's like these things happen but if they slip into production they will have consensus issue on our hands. When we have 10-20 thousand lines of codes, ther's quite a high chance that these kind of busg exists in the code bases.

**Alex**: Well, I think I should care a little bit to explain both why the pre-compile was made universal it's the first place because it was actually to eliminate ever a discussion about how many people wants this feature, how many people want this curve and who is to decide whether it will increase it or not.
Second for code base size and similar saying, this is the reason we run fuzzing testing to find such mistakes. If you look into the implementation of it for example if you every want to add BLS12 that's really 81 bits is the base field and if you ever after this would want you add BLS 12 curve 377, it's different one gives you like huge as a set of capabilities which people will potentially want. They will have end section in the code base of around 90% just because the most of it  will take, filled arithmetics and cured which is the same on every curve. In this precompile this common part is much easier to solve and which actually has no edge case. This is not 80 % as my previous example but most likely 75%. I can little bit explain how it works. ... explaining (worth listening to the audio).

At the end this precompile wants to eliminate any form of centralized decision to which curves goes in / does not go in, you want to implement in a set of specialized precompile. This is the state of some modern cryptography and certifications.  Now with recent discoveries around more choices, which gives you a lot of different features, are not even talking about whether to use SNARKS / STARKS, it's a separate discussion. **This is why it is universal, this is why you call it a virtual machine**. I call it a calculator which is much simpler if you ever implemented it at least once. 

**Louis**: I understand the logic of all crypto and be done with them. At the same time you can not ignore the attack. I am going back to one specific mistake that happened with Windows we have variout throughout the crypto team that happened just a month ago. My concern here is we dont have known figure doing the implementation and saying that this spec is enough for anyone to implement according to spec. How woul dyou address this concern? 

**Alex**: We can not ask someone specifically if he does not want to implementor do the duplicate work. C++ implementation exists. If someone wants to find unit, for it, just fork it for own interest, you're. free to do so. Butif no one volunteers to make alternative implementation according to the spec because of the set of languages which it's already implemented, it's wide enough and most usable, we can not force anyone. 
About the Window that you mentioned, as far as they know, the problem was not cryptography itself, it was in parsing format and this is equivalent to API part of this pre-compile which is much simpler that their encoding format in usual certificates. I mean, attack surfaces chapter is also covered in the documentation so there were only three main parts and I spent a few pages to explain how they are addressed. I mean precompile documentation and VB document was updated quite a lot over the past week. I can not force people to look at it. 

**Martin**: I think that is a bit of strong argument. I've read the attack service description, I just don't agree with the conclusions. I mean, what can I say there is this one little paragraph about it being consensus breaking where somehow you say that it cannot be consensus breaking because of conventions. I don't agree, sorry.

**FJL**: I would like to expand on theat. With this EIp our main concern is really with the complexity of this of this particular precompile and this definitely would also be my concern. it is definitely possible to create a large programs which behave correctly and are in consensus across multiple implementations as Ethereum implementation shows. but especially with this precompile I think it might be stretching the limit a little bit as to how big a pre-compile can be. and I do understand that it is quite important for applications today to have access to these kinds of cryptographic features but I do disagree with the notion that the process of adding a pre-compiled is like too complicated right now to make it happen. so As client implementers,  I don't think there's any problem with adding any particular pre compile as long as it is reasonably simple and there is a use case for it.  with this particular EIP, there is definitely use case for it but it is not simple; and I think of such as it **doesn't really meet the criteria for a good pre-compile**.

**Hudson**: I don't want to spend too much time on it.  Alex go ahead and rebuttal.

**Alex**: I want to answer this question. It's stuck broder. There is a list of Jurors which would be potentially and of interest to use. Unfortunately, this is quite large, so it would, at the end of the day woul dend up making 8 different EIPs. Each of those will take 3-6 pre-compile addresses and I can  definitely split this pre-compile but  by doing calculations for a particular set of parameters and even by using simple bases as a reference to, let's say, let's include these 8 curves. All of these curves are usable. People want to use them for one or another application. What woul dbe the chance to actually get this included in a time frame for a few months. this is what I wanted to avoid with this pre-compile for this specific decision for every time,  what would be secondary chances for this case? 

**Kobi**: Is it okay, if I give my view as well. I know you want to move on but, I want to give my views.

**Hudson**: Sure!

**Kobi**: I just want to comment on something that happened. so I won't to go again into saying the value of the EIP. I think we all understand it's valuable and we have a bunch of use cases that we would use it for.
I will say to metal up what Alex said. This EIP  has explicit formulas how to implement the specific crypto features that are needed, which is quite unusual. usually people Implement from papers and the papers are scattered and so I think having these explicit formulas is super helpful to make independent implementation.
So this is a very good positive point about this EIP. one thing that I don't completely understand yet or I can't internalize yet is calculations. I understand that idea but it's hard for me to internalize it. I think this is somewhat related to how people percieve the complexity of this EIP  because it feels like it's a big vunit which you must take as all or nothing. that is kind of scary. This makes you look at these 20,000 or whatever lines codebase and say, this is very big and I can't say I disagree with it. I think it might come down and maybe we could discuss that at some point how to make this a lighter. so like Alex mentioned yeah you could divide this so. you won't have like five sixty precompile for all the different terms that we want. Maybeeven EIP 1960 would be the underline implementation. Then you could havespecific gas formulas for each curve and so on. but that would also mean that you would require a part for every time you want to care, which to be honest, I am totally against.

**FJL**: You'd still need a hardfork everytime you add a curve even with this particular EIP.

**Alex**: Not with this one. You don't need a fork. 

**Martin**: That's kind of like it such a pain to push an EIP through the process. We will clum it all together and pretend it is one. 

**Kobi**: Acually, I was building a point, may be I will finish that. You could divide it into 60 pre-compiles, then you would require hardfork every time which is maybe fine. We could discuss for example we go through the process of adding 6-8 precompile per term and if the underlining implementation is 1962, does this improve the complexity worries? for example even including one curve is already scary and even that should be really evaluated further, these are things we could discuss as to how we connect to move this forward.  Because I totally understand the worries and complexities of what it introduces. The discussion about how can we modularize it so it is not pereceived as complex.

**Peter**: So just to add some things. Our biggest concern with regards to it is the complexity. because I am almost certain that there are bugs in it. I don't believe that three times 20000 lines of code is bugless. so from my perspective there will be a consensus issue, that's for sure. the question is that Parity is currently being maintained by two people and in the progress of being switched over to OpenEthereum with God knows what Governance model, who will be actually maintaining it? Geth is maintained by a handful of people, and if it hits the fan, who is going to fix it. 

**Hudson**: That's what I was going to address actually, real quick Peter. I was wanting to get like buy-in from some of the cryptographers in the community including people on this call, who either build or support the EIP to be in a Gitter or telegram or something Bridge channel so that it hits the fan we can call on you all to jump in and within a very reasonable amount of time, fix it. when I say fix things, more identify the problem that kind of thing. so Peter what about that idea?

**Peter**: To jump in within a reasonable amount of time, I'd like to mention the time when doing a Shanghai attack, you called me at 4 a.m. in the morning to get up and solve some issues. Is a group of cryptographer is willing to be called at 4 am in the morning and fix it at 4 a.m. because if not then that's a huge problem because we can not fix it. 

**Hudson**: I think with the time zones, probably is what I am guessing. But I want to hear from them. What do you think Alex, Kobi?

**Zac**: If this EIP will continue, I will definetly be **very happy to fix** it say if it hits the fan.

**James**: If we could **collect those people who are willing to be**?

**Alex**: I mean I saw this as a bold responsibility. I mean I didn't know that it existed but I thought it comes by default so **Yes** from my side. Can't say it for Sayeed.

**Hudson**: And I take responsibility for keeping this channel up to date as far as people on it and then Alex if you continue to run this type of fuzz testing or someone runs this fuzz testing at think that'll also be something that'll help. It's not going to fix the concerns that the geth team has for sure, but if this goes through, anything that we can have a addition to just putting it in and everybody leaving like having this supported until well after Eth2 becomes a thing. I think it's going to help some concerns not all concerned. Peter, you can continue cuz I interrupted you earlier.

**Peter**: Oh I'm not sure where I want to get that but now I wanted something make something clear is that  if this EIP goes in the Geth team will take absolutely zero responsibility for it. I mean we don't have the knowledge to do this.

**Hudson**: What you're saying is that's not by choice as much as you don't have the knowledge, right?

**Peter**: Yeah, I mean I'd gladly fix something and obviously if it hits the fan, I'd be super pissed and I would be staying there but it's something that I don't understand. I think it's also really important to consider what are the consequences on network of the whole thing.The implementation is huge. There can be two types of issues. One is **Consensus issue** -  for example, if there's bug in the Go implantation and 80% of that goes off in a different direction or whatever like suppose 80% of the miners go in the direction which has the bug, then the only way to solve it is to roll back the chain or pause the  chain like Iota style. Are we willing to do that?  probably not! even if the whole implantation are in consensus and there is a bug in the cryptography itself, I can not verify it. I can say that the five different implantation do the same thing but that makes sense or not is beyond me. but if something like that happens, it's a catastrophic failure for Ethereum. These are the risks that we are talking about and the reason why Martin is against this and was suggesting that individual EIPs that introduced curves one by one can help because it's much easier to say that yes you're beyond 256 or whatever is BLS signature. Evene adding that one curve could be dangerous. I mean it's a tiny surface compared to enabling a turing complete cryptography machine. 

**Alex**: It kind of gets us back to ideas like we can roll it out gradually but not by making individual chirps and send pre-compiles and addresses or other things so people don't really know what's under tthe hood.  we can just whitelist as occurs by still.

**Louis**: Can we have proposal for this? Could we imagine that this EIP has beta testing where we can offer a bounty to be sure to display an attack on this EIP.

**FJL**: It maybe problematic because then they would wait for it to go mainnet.

**Louis**: There are people from universities who find fun hacking and breaking cryptography.
As Martin said that 99% probability that here would be bug there. Having this sort of thing probably could help limited attack victory in the first phase. Maybe run for like 6 months till we get trust enough.

**Tim**: Maybe this is like a separate conversation but I feel like with this EIP and what you're mentioning Louis and having longer testing, it kind of reminds me of what we were talking about EIP 1559 on a previous call. where it's like we maybe want something more than you know activated on a test net for 6 weeks and then fork the mainnet. I'm not sure how we do this I don't think the 17 minutes we have left is enough to discuss like that. but maybe it's worth thinking about, what's the better way to test these complex EIPs because ther're more coming down the pipeline. so that's where we're kind of you confidant with them. I know we've to talk about ProgPOW today as well that's another one of those, I feel the UNGAS will have the same exact conversation. so how do we test I?

**James**: I want to time boxes a little bit.

**Louis**: I want to ask who among the cryptograpgher community will be in Paris? Beacuse I think in-face discussion will help solving a lot of concern here.

**Zac**: I'll be there. 

**Louis**: That should be great. Let's **coordinate something in ETH Paris** on Gitter.

**Hudson**: Yeah I think that's a great idea. just before we end this just as quick as you can. we know geth position but I haven't heard from Besu or from Parity. There is particular concern over Parity not being kept up, with so I just want you all's perspectives. We can go to Danno's first.

**Danno**: I am in a bad position to discuss it. 

**Hudson**: No problem will save that for next time.
Wei?

**Wei**: I believe this is 1962. The implementation is there that's good for us.  we are slightly against implementing.

**Hudson**: This is something that is why we have this type of governmenance system and I think having in-person meetings at EthCC with where it could be longer Forum discussion and individual discussion is going to help clear some things up but in **no way can we confirm the EIP is going in**. because at this point there are clients who would know not want to implement it right now or what I should say **clients have serious concerns implementing** it so as unfortunate as that is for people who want to use these curves but this is just how the process goes. But I do thank everybody for coming here to discuss this especially the people who took their time on the west coast during Stanford blockchain week to discuss this particular EIPs and the cryptographers who were offering to lend support given if this goes in. Peter do you have one last thing?

**Peter**: Yes, so I don't want to say that the Geth team opposes the features itself.  We have nothing against adding cryptography is deemed useful and necessary.  we just want to make sure that it's added in a way where you can more or less guarantee that things don't go horribly wrong.

**Hudson**: Is that something you can guarantee with anything, though? I guess you're saying minimize it.

**FJL**: Yeah minimize it. Ethereum has large amount of complexity already. we have been pretty good at slowly expanding the complexity and not adding like a whole bunch of complexity all at once. I think this is something that you know over time as Ethereum 1 evolves, it will be more and more and more and more complexity in the execution because this is where all of the interestig features are and there are many many things that could be done to improve what you can do in a smart contract but this also kind of I think there are certain things were like we really have to like slow down and then reading check okay so like what is the thing we really need right now that will like add the most value and then maybe we go for the next thing and then for the next thing and I think doing it this way will be basically allow us to vet each feature, more or less completely, like I mean the last few times we added cryphotographic pre-compile, there was a lot of exhaustive testing done and I see that has been exhaustive testing on this particular EIP fuzzing has been going on 32 core server that is mentioned in the readme. I believe a hundred percent that you know like everything that could be done has been done to verify that you know the implementation is secure and everything and you know it well behave under consensus. However you know just adding this large chunk of complexity all at once it's just a really scary thing and maybe we'll all going to be able to absorb. That scaring like in a couple weeks or whatever we all going to say you know what were you thinking about, this is the best idea ever. but at this time it just feels like this is too much all at once.

**Hudson**: Okay, let's move on.

**Alex**: Closing words- 20k lines will go in is not the right estimate. If Martin has a counter example why there will be no consensus breaking, if implementation is done correctly, I'd like to see this example. It's my semi formal analysis that it was correct. 


**[EIP-2242](https://github.com/ethereum/EIPs/commit/ee60f5a504cac00ae2713b11362bc160d977edaf)**

Could not discuss.


**@adlerjohn's [other topics](https://github.com/ethereum/pm/issues/152#issuecomment-589154306)**

Could not discuss.

**[EIP-1057](https://eips.ethereum.org/EIPS/eip-1057): ProgPoW**

**Hudson**: On to **ProgPOW**. Thanks for staying everybody. 
We can have James go ahead with it or Martin you put it on the agenda so maybe it's better to hear what you wanted to do with it today and then go to James.


**Martin**: My idea was we should have another discussion on ProgPOW and see what the next step is. I would propose that we **launch a new testnet** with the updatedimplementation. yeah I really want to know where we're at in this discussion or in the decision-making process. I seem to recall that we've decided it for implementation.

**Hudson**: Andrea, I'm really sorry for not pronounce your name correctly. Where do you see where we are in the process? if you have an opinion it all? just kind of put you on the spot there :)
we can't hear you if you're talking.
Okay while you fix your mic I think James had something to say.

**James**: They have an 093 testnet. I think I can hear you now. You're very quiet.
So there are the readiness, some testnets and they are mining on their 093 spec and it's in my opinion the closest EIP to being ready to launch. So as far as status of application they're pretty much ready to go unless Andrea has an opposing opinion to that. I do have a proposal for a hardfork scheduling proposal for this, which is the BLS precompile getting in some time for June having a fork scheduled for that, weather it's with the 181 whitelisted or if it's in the specific as if it's a specific precompiled there the Eth2 team is working on that right now. it's important that we get that done before the deposit contract so things can be validated on-chain. then for progpow and its inclusion I would suggest that it is a contentious upgrade but I as I have done research in and around that the likelihood of a network split is very low cuz I haven't actually seen someone willing to be on the other side of that, but I do agree that it is a contentious upgrade. So,  my **proposal** is that **we have a fork for the BLS precompile** and **then the next 3rd Wednesday after that we have a fork that includes only progpow** and that's the suggestion.  There's a lot of things going on why I don't think we have a lot of more time to really go over that.

**Hudson**: My main question is, we say three weeks, is that we're testing them at the same time but we're just including them in Forks at different times in order to make sure people have the opportunity to fork-off if they want to?

**James**: Yes, so **Berlin would happen in when the BLS pre-compile is ready** and then a **ProgPOW would happen the next third Wednesday after that**.

**Hudson**: Any other anybody have comments concerns Etc ?

**Tim**: I am concerned, it is much too close.  I think from a community perspective and people opposing, ProgPOW, I feel like putting Eth2 precompile and ProgPOW a month apart, is kind of conceptually weird, for some reason. If you told me like 3 months or 2 months between the two, sure.  I know we've had a lot of of discussions around like if people want power or not and what not, and given how contentious it is, I'm in personally be a bit uneasy about including yet. I think kind of decided through a network split is far from ideal. I am a bit uneasy about ProgPOW in general but I'm especially uneasy about having it very close to Eth2 related upgrade just because of the potential confusion.

**James**: As far as the releases go, we could have the release for Berlin, as soon as that's ready. And we can release the ProgPOW1 shortly afterwards. If we wait another three months then progpow eats up 6 months of our development cycle where really ProgPOW is actually the most ready to go out of any EIP right now but the reason we aren't scheduling it is because of it we don't want to just do the only progpow on 1st. As far as timing goes getting the the BLS signature precompile in is more important than having progpow come in first. Having multiple releases before and then having people to upgrade to the one that they want, that has already worked. So it isn't like okay once Berlin is done then we'll release the version 4 progpow, it's more of will release everything for Berlin soon as it's ready and then we can release up a ProgPOW one shortly after and have people also operate that as as the next one but as far as act Fork activation happens it would happen at that amount of time.

**Martin**: 3 weeks is not like we're just trying to slip in ProgPOW the day after nobody noticed. I think 3 weeksis fine.

**Hudson**: What about giving exchanges and other network service providers time to upgrade their clients twice? Is 3 weeks enough for that?

**Martin**: We do not actually have to do that. Codewise we could bundle, it could all be implemented and activate the pull or deactivate all by our switches. so if we just code it right, you don't actually have to update the software twice.

**Hudson**: So what I remember from the Dow is that there was a lot of pushback on a switch because that implies a default to the switch, whereas running an entire client where the default is one or the other is a much more explicit switch then having a software enables switch that you have to like manually go in and do.

**Martin**: I mean, yeah! The default obviously would be pro progPow because that's what we kind of decided, right?

**Hudson**: Yeah!

**James**: If exchanges and things seem they like to upgrade the moment before and there are already have been shown to be capable with that and I'm in a much shorter and crazier timeline which was Muir Glacier. if we did a release of Berlin and then release and ProgPOW, people could just go to the release the day they choose and would be supporting going to the ProgPOW release.

**Tim**: I think one thing that is also worth considering is the exchange have the biggest incentives to support two coins, right? Like if Ethereum splits, it is bad for everybody except exchange fees. it is worth being mindful this is basically how ETC came into existence. Once the first exchanges is like we'll let users decide will run both ETHProgPOW and ETHHash, then it's almost like a you know every other exchange has to do it because the end up competing for the fees and we've kind of split the network. This is kind of why I am personally uneasy.

**James**: As I understand from the community, that there are people who opposed progpow but their stands is that we would all go to the non progpow chain and if that is actually the case then there is no network split, there is just we go on with the one without ProgPOW or we go on the one with. I have not seen any evidence that there is an ideological or people willing to step up to actually have a network split and if I'm wrong about that I'll resign as Hardfork coordinator.

**Hudson**: Yeah, that probably wouldn't be necessary but I'd say is I've seen very little, the only person I can just call it out I'd say Ameen is the only one who said they'd step up and I'm not sure if they still have that position today and even if they did but just kind of seem like. I don't know I'm skeptical of that happening but again I don't want to be proven wrong but if I am then that's just how things go.

**James**: I am serious. If I'm wrong I would quit my job.

**Hudson**: Please don't, because I'd really like you to stay.

**Tim**: Another ProgPOW critic is the Gnosis team and Martin specifically. I think, it might  be worth on getting their thoughts on it on a core dev call especially because they're going to be maintainers of OpenEthereum. I personally would feel much more comfortable with this plan, if you know Gnosis as maintainers of parity ethereum are openEthereum say they're kind of okay with this. Martin is not Gnosis.

**James**: He's talking about the right one and I have gone back and forth with him a lot. He said ProgPOW would be nothing if we'd all be on the other side. so those are the two big objectors and neither of them are saying, yes I will move forward with the network split. 

**Tim**: I'd be much more comfortable if Martin K from Gnosis agrees that  openEthereum will implement that and kind of be okay with it even though he's personally somewhat opposed to it. cuz I think that's the other kind of credible. 

**Martin**: I don't know. We've had discussion but for everything that's going to said has already been said. I think, we kind of just need to go forward, that's my view. 

**James**: I agree.

**Hudson**: I agree with the view, however Tim if you want to ask them and make sure they're aware of it or at least the Stefan from gnosis. Feel free to ping them and let's make sure that they know this is happening cuz the thing that got me last time was people saying this is being snuck in. so I'm going to make a effort to make sure that's not the case this time. As I'm sure James and others will do as well and they'll be plenty of time for open dissent that won't really change the decision necessarily because we've already gone back and forth and approved it twice but at least they'll be aware. so people want to do that they can. it's that's what that's why forking off is the ultimate consensus mechanism.

**Tim**: Sure.

**Trenton**:  Quick question, is there a better way to advertise then through your Twitter account I can more official venue?

**Hudson**: Good call. I'd say I can't think of one, what about you?

**Trenton**: The Ethereum blog, I mean if you were really serious about this ? 

**Hudson**: There are trade-offs to doing that and when I say that what I mean is, it looks like it's an endorsement by the EF which it really isn't. Because Geth acts autonomously from the EF although it is funded by the EF, with as far as their decisions. As in no one outside the geth's team influences any or has ever influenced any decision for what goes into a network upgrade, within the EF. Aya and anyone doesn't go like you have to put this in and so that would be one misconception. The other one would be kind of Fanning the Flames of something that like is not really needed to be fanned but I'm open to other suggestions. If enough people want that to happen I'm perfectly comfortable bringing that up to the other blog editors.

**Trenton**: No, that's true, good perspective.

**James**: Mine would be, if you've grievances, come to me, I am taking responsibility for this as much as I can in my role and I do listen and I have had many of these conversations and I look forward to having more of them. I am essentially putting my reputation on the line for this decision.

**FJL**: I do think the official announcement of the decision. It's like all core devs deciding the way forward is to include ProgPOW is kind of something that I feel like is newsworthy and that is something that can be announced on Ethereum blog even without seeing it is an endorsement because this is basically documenting the fact that "All core devs have collectively decided that ProgPOW is the way to go" and if community doesn't accept ProgPOW and we all turn around, okay, maybe it wasn't such a good idea and then we just go with the other chain, that's fine as well but at least having like an explanatory write-up the blog that actually **explains why ProgPOW is adopted** and like **that it is being adopted because of the decision of all core devs**. I think, these things can just be included in the blog and is not an endorsement. 

**Hudson**: There's a happy medium we can definitely approach once things get closer. Especially if we very early put a blog out there rather than like 2 weeks before like I've been prone to doing.

**Tim**: I think we should probably do it now. I don't know if now is the right time or like after the next core devs call.

**James**: We should have it after next core dev call.

**Hudson**: I think we should do it after whatever BLS EIP is going in is decided, so we can make both announcements. So I'm not doing it the EIP by the EIP.

**FJL**: No, it's not that. It's not about hardfork announcement. It is more about the decision that **the official decision is now for ProgPOW will happen** and that doesn't really a hardfork announcement that's just an informational post.

**James**: And when it will happen, will be after this the third week. If we don't say when it will happen,  I don't think it will happen. So having it be the third Wednesday after the BLS recompile is a way of saying,  this is it, is happening, when it will happen.

**Hudson**: Okay, we'll discuss this more next meeting cuz it's not going to happen before next meeting and I could definitely draft something up just so that we don't keep everyone here all day.  

**Hudson**: Artem makes a good point that we should definitely invite Stefan and Ameen if they want to come on and give their perspective of why they would like that they're splitting just so people are aware.  I'm going to talk to Ameen just to see what his position is now? I think he knows any way if he wants to but I don't want to create drama for the sake of drama so I'm avoiding that as much as possible, while still making sure people are aware of what's going on and giving them voice. That's a hard thing to balance and I think James is doing a good job of that and I'm going to try to also do a good job with that. 



**[EIP-2200 Change](https://github.com/ethereum/EIPs/pull/2514)**

Couldn't discuss.

# 2. Next Upgrade Timing

Berlin would happen when the BLS pre-compile is ready, ProgPOW would happen the next third Wednesday after that.

# 3. Open RPC

**James**: there is a precompile that we want to look into individually to getting in and I can see that this is something that will take longer a longer amount of time for everyone to be comfortable with I don't want to continue the conversation on that.

**Hudson**: Also, we don't have Eth2 people here that we can see. 

**James**: I've been talking with him. I'm here at Stanford, as well I'm just representing them at this moment because it's very early for them. Alex has an EIP written and I put it in the [chat](https://hackmd.io/@ralexstokes/rJegpNo7I) for the BLS signature and then having a target for June so that it can be used in the Eth2 deposit contract. as far as Hardfork scheduling, that I think is important to target.

**Hudson**: So yeah I agree that we need to figure that out would there be an appetite for meeting in one week and fleshing out specifically this EIP after discussion on gitter and magicians, who would be able to come to that?

**Martin**: Not me.

**Hudson**: Yeah I actually have a conflict too. this might have to wait for 2 weeks and given the tech stuff. that's unfortunate because of the timing of that might put off some of the other discussions but I guess this is the process now if it doesn't get in at Berlin it doesn't get it in Berlin! we can only do so much with time we have. James if it's okay with you I was wanting to get the open RPC discussion going if that person is still here cuz we promised last time that they be able to have a little bit of time and we're at the end of the meeting again with like 8 minutes left  if that person is here.

**James**: I think it's okay. Then we should discuss ProgPOW. I know it might go over. I think it's important to talk about with Berlin going in.

**Hudson**: Will do light discussion on ProgPOW. that won't be anything binding if people have to leave. Let's start with Zach they'll go right ahead. 

**Zach**: Thanks for having me. I just want to take quickly maybe start by saying a little bit about what open RPC is? **Open RPC** is what is called a service description specification, a way of describing a service. There are othe ones that exists, open API is definetly the most popular one. That's the one that I've used a lot in the past. I found that there was some particular challenges when using open API with Json RPC services because Open API is structured as a individual route that's based on HTTP. It has a lot of features that are specific to Rust based APIs and so that's why we may need an Open RPC which we started out as a fork of open API and work with the guys that main that to figure out how to set this thing up. It started deleting all the stuff and only pertain to Rust and the beauty of Json RPC is really a Simplicity. You can really tell that by like how much stuff we are able to be able to remove from open API. We also worked a lot on tooling around it as well. The motivation behind this is really we wanted the same sort of tooling that we get from open API but specific to Json RPC. there's a couple of things that we added in there as well like the concept of service Discovery Maps really well on to Json RPC whereas for the open API stuff, they have ways of doing it but it's a little bit different. Ex-  we have a RPC.discover which is a method that you can add to your json-rpc service RPCdot being a reserved prefix for Json RPC and the idea there is that, that method would return the service description for itself. so you can sort of ask a service hey what methods do you have and what parameters they take. What do they return? 
Fundamentally we built the stuff for Json RPC not for any particular one technology just json-rpc in general. Of course it has specific applications of blockchain cuz most blockchain clients used Json RPC but also there's a lot of within Ethereum, Ethereum classic whichever there's multiple client implementation, all trying to hopefully adhere to some common base set of methods and interface, right? And maybe some clients add certain functionality but having a way to communicate these differences is really important. so yeah that's pretty much the gist. we've put together 1 specification for Ethereum, I was like the base level set of methods for Ethereum. Haven't had too many eyes on it really but we're using inside of multigeth. Multigeth is supporting those methods and implementing the service discoveries as well. yeah there's also like a lot of interests outside of blockchain as well. happy to answer any questions that you have and also really happy to help out, hopefully make this tooling stuff work for you guys.

**Hudson**: Just to make sure, I understand is they asked to **implement this at the client level** and for those who might not be familiar this is **not a consensus breaking change**, right? This is just like something at the high-level?

**Zach**: Yeah, totally! Yeah, this is at the client level. I have a couple examples I don't have the links handy right now but one example of a way that could be used is when proposing an EIP, if the EIP include the new Json RPC method or a change to the existing json-rpc methods, it can be specified as a structured format. You can include the open RPC definition of the method. Aside from that each clients, it's up to them to implement this stuff or not; like you said it's not consensus breaking or anything like that. It's just something, ex- with multigeth whenever the specification changes we just rerun the generator and we get new clients for JavaScript and Rust right now working towards go and Python and the near future. But these are generic, right? so of course you can for any json-rpc.  Same with documentation. The idea is to save time and not really like force it on to anyone that guesses a good way to put it so like there's no need for anyone to implement anything if you don't want to, it's just a tool. 

**Hudson**: Anyone has questions?  Peter?

**Peter**: I have a small reaction. Generally, the problem with the generated API is, before Ethereum I used quite a lot and hacked quite a lot on google APIs. They have this API descriptors, they are super complex and they have API generator for pretty much everything. I was using the Go APIs. The problem is, Yes you do get these APIs generated but they are more or less useless on themselves because after API reaches a certain complexity, the generated code is just a maps functions calls to API calls to you. You just translate them to your language but most often the user doesn't really want to code due to low level code individually and assemble and passing all the configuration. So at the end of the day, you will need to write proper client that was my experience.

**Zac**: I mean,  agreed, there are some cases where the complexity is too great for generator client to really fit the bill but similar to an open API World, there's  many rests sort of pattern. There are many patterns that people use that don't necessarily fit rust or open API. In that case you either accommodate with by adding like plug-in interfaces to the generators or like  as you said, you just you're stuck with having to write your own. I mean if that is the case, that is the case. Certainly ther's a lot of cases where what you want is very lights wrapped interface to your methods that includes static typing. if it's a j s or JavaScript generate client then you won't like js talk annoted functions. so that you know in your editor when you're calling like Eth.call or whatever, you don't have to go look up the docs to know how to use it.

**Hudson**: If this is already in multi geth, would that mean it works for Geth, already?

**Zach**: Yeah, certainly. It should be the base level set of methods.

**FJL**: I think we're happy to add the server side of this. I doubt that we will change in mainline Geth. we won't necessarily change the client based on this because we do have handwritten client, which I think basically includes the functionality that you would need to interact with the chain. we do add to it from time to time, but it's not in general, we more trying to provide a stable to go API instead of providing like even if the if the underlying mechanism changes that is used by this particular Go API. And we do strive for stable API on the client side also. So, we don't be using the generator but super happy to add the RPC.discover endpoint and return whatever stuff needs to be returned there.

**Zach**: The intent is for this stuff I guess is to highlight differences between clients, reall.

**FJL**: Don't know what Multigeth uses.

**Zach**: Same as Go, the same as Geth.

**FJL**: The server implementation is like we basically need to have a way to auto generate schema from the provided methods. That's something we're not doing right now. 

**Zach**: Very good point.  I'll start by saying that we have a fella on our team named Isaac who is working on this stuff exactly. what he's trying to do is infer from the code what the what the service description document ought to look like. That is in the realm of like document introspection, which is definitely one avenue. Another one being like starting from the document and then updating the typed interfaces in your code which brakes compliation you go and fix it and now everything's happy, you've implemented the change to. the interface. 
so they're sort of two different schools of thought I suppose.

**FJL**: There is a big benefit to it. If we go down the path where basically we would define official Ethereum RPC interface as you have done, as a scheme like that. then loading it into the server we'd also be able to provide canonical parameter name switch or something that we can do right now. At this time all of the interim methods are by position and that can actually be a bit of hurdle, because you actually have to remember which  thing goes into which place. Some of the methods work around it by just taking objects as a parameter but it's kind of a hack. I do feel that this is something that could provide a big benefit to the users of the RPC interface because they woul dbe able to use named parameters, finally. People have been requesting this feature for a long time. 

**Zach**: Yeah, definetly.

**Hudson**: I want to time box this. But Zach, if you could just tell us how to get in touch with you or your team if people are interested in this?

**Zach**: GitHub is definitely the best place to chat about the stuff, if it's related to the specification there's this open RPC / spec repo. Happy to chat there and entertain any questions, otherwise I'm on telegram Discord Twitter all that stuff.

**Hudson**: Gitter is mostly used for this type of things, are you on there?

**Zach**: Yeah.
so actually we've been talking about this. Sort of having the need to maybe start a gitter for these exact reason, so maybe I'll get to that this week or today and get back to you, perhaps.

**Hudson**: Feel free to come back and give any announcements of better communication methods if you'd like even if it's not talking about the whole thing y'all are always welcome here.

**Zach**: Well thank you very much for your time and it was nice to meet some of you at EthDenver last weekend.

# 4. Testing updates

Couldn't discuss.

# 5. EIPIP Meeting No. 3 Updates

**i. [EIP-1 PR #1](https://github.com/ethereum/EIPs/pull/2508)**

**ii. [EIP-1 PR #2](https://github.com/ethereum/EIPs/pull/2516)**

**iii. Adding a section of 'Motivation' to Meta EIP of upgrade**


Couldn't discuss.


# 6. Review previous decisions made and action items (if notes available)

Couldn't discuss.

# 7. Next call: Mar 6, 2020 14:00 UTC


**Hudson**: Any other final comments before we close out the meeting and what we'll do is for the next meeting let's look at what we miss this meeting and try to prioritize that along with the BLS curve stuff obviously. It sounds like Eth Paris is going to be a big place where that's discussed but if we can have an Eth2 person next time; James I know you were representing them so actually that might be sufficient.

**James**: Yeah by next time I will have someone and the actual EIP will be written and finish.

**Hudson**: Okay great that'll help a lot. So yeah let's reprioritize EIPs next time so we're not leaving stuff out and other than that any other final comments?

**FJL**: I have a quick request. It's been quite a while since we've had the EIP 778 and 868 merged. This is something that to refresh you guys. This thing have been live for quite some time and there is implementation in Trinity and Geth and in Aleth but we are but we're not really seeing any other implementations on that. It would be very useful to have these things because we've just rolled another critical piece of infrastructure that will depricate the bootstrap nodes in the long term that is DNS discovery and that would really watch for people specially client implementers to go ahead to add these features to the discovery implementations, it would not take time but will be very helpful for the network. 

**Artem**: If I may, just finished working on Eth 64 implementation for Open Ethereum, just hit the Master and I will also be working on Ethereum Note records and integrating it into the OpenEthereum network.

**FJL**: That is very nice. So, do note that basically just close contact me if you have any questions regarding that and I'm very happy that this is finally happening. I can really recommend that you look into Rust libP2P repo because they have already implemented all that stuff is part of the discovery version 5 draft work. so you can just use the implementation from there. you don't have to implement it again.

**Artem**: In fact I have been in contact with Sigma Prime and today they've split their implementation of ENR into a separate, and we will use it. 

**FJL**: Very well.

**Hudson**: Felix, if you could get on the all core dev gitter, put where your specification and ways to contact you and then tag nethermind and Besu, that sounds like those are the ones that we are not accounted for if they have done or not. if you could do that today or Monday maybe, Monday might be better so people are like not ending their day, that would be helpful.

**FJL**: The situation is a bit unclear anyway because we have approved them on all core devs a long time ago but the status in the EIP was never updated. so they're all still in draft. but actually you know like we've discussed this EIPs two or three times on the all core devs even more than a year ago. It was proposed in November 2017, right? so that is like more than 2 years ago. I've been like moving these things around to final would be great but I don't really know what's the process is for all those Networking things. 

**Hudson**: There is a process being changed in the EIP right now to make it more clear. There is EIPIP meeting and you're welcome to come every other Wednesday but basically right now the next step as the current system stands would be to put it in the "Final Call" or last call.

**FJL**: There's a PR for that already.

**James**: I made the PR.

**FJL**: We're currently in the waiting for merge stage. 

**Hudson**: Just ping me, I can merge it. Any other final stuff? We went over exactly half an hour, not bad all right, thanks everybody, thank you for your time. Thank you Artem for your update. Artem just for the record you are on  OpenEthereum are you with Parity Technologies?

**Artem**: I am with Gnosis. I am employed by Gnosis to work on Open Ethereum. I am the first of the hires and we're currently expanding so we're looking for more people to work on this.

**James**: Welcome!

**Hudson**: Welcome to the call. 

See you all in 2 weeks. Thank you so much. Bye everybody!

# Attendance

* Alan Li

* Alex Gluchowski

* Alex Vlasov 

* Andrea Lanfranchi

* Artem Vorotnikov

* Bob Summerwill

* Daniel Ellison

* Danno Ferrin

* Duncan Westland

* FJL 

* Greg 

* Hudson Jameson

* James Hancock

* John

* Kobi Gurkan

* Louis

* Mariano Conti

* Martin Holst Swende

* Milan Patel

* Peter Szilagyi

* Pooja Ranjan

* Tim Beiko

* Trenton Van Epps

* Wei Tang

* Zac Williamson

* Zachary Belford

* Zane Starr 


## Zoom chat:

**Bob Summerwill**: For what it is worth, ETC Cooperative are supportive of 2315 Simple Subroutines.  I would love to see it deployed on ETC and we would not necessarily wait for ETH. Wherever it can land first!

**Tim**: https://ethereum-magicians.org/t/eip-2515-replace-the-difficulty-bomb-with-a-difficulty-freeze/3995

**Tim**: @Zachary, how much time do you think you would need? I think we can maybe block off that amount at the end?

Trenton: https://www.etherchain.org/tools/difficultyBomb

**Zachary**: Thank you very much. Im not too sure how much time is needed, as I'd love to entertain any questions, but otherwise I think 5-10 minutes is plenty

**Tim**: Great! @Hudson, WDYT of blocking off 10 mins at the end for this?

**Hudson**: I say we just do it after the EFI section. So roughly middle of the call.

**Duncan**: Youssef sent his colleagues+1 from EY to that!

**James**: https://hackmd.io/@ralexstokes/rJegpNo7I

**Trenton**: a long but productive discussion. would it make sense to have an extra meeting next week to keep the cadence of discussions for other EIPs?

**Tim**: +1 on an EIP-only meeting next week if champions + client devs can attend. Probably worth going 15-ish over to cover ProgPow if people are free

**Kobi** (on ACD Gitter):  I didn't want to take more time from the call, so to clarify my view - if individual EIPs for each curve are the way to modularize it and gruadally roll things out, I definitely think it's a viable way to move forward.
want to hear more opinions if this solves anything :)

**Hudson**: Tim: You said you can help organize at EthCC about the BLS curves discussion. I won't be at EthCC so could you and James maybe team up to facilitate? Would be awesome if client teams and cryptographers can come together.

**James**: +1

**Zane**: example of ethereum spec https://playground.open-rpc.org/?schemaUrl=https://services.jade.builders/multi-geth/ethereum/1.9.9
general specification docs: https://open-rpc.org/getting-started
ethereum open-rpc spec: https://github.com/etclabscore/ethereum-json-rpc-specification

**Andrea**: Sorry my mic doesnt work. A new testnet is already launched and running and free to join. On spec 0.9.3. Geth has implemented it in Holiman's branch while Parity is already merged

**Trenton**: well that’s the definition of a network split, no?Martin is not Gnosis thomartin doesn’t make the entire organisation is what I meant. I agree with MHS

**Andrea**: What about Kialo ?

**Artem**: Can we come back to this on the next meeting? Maybe invite Stefan next time to it? Not to second guess what he thinks

**Tim**: A good template: https://blog.ethereum.org/2016/06/17/critical-update-re-dao-vulnerability/
