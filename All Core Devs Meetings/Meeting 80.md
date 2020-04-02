# Ethereum Core Devs Meeting 80 Notes
### Meeting Date/Time: Friday 7 Feb 2020, 14:00 UTC
### Meeting Duration: 1 hr 35 mins
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/150)
### [Video of the meeting](https://www.youtube.com/watch?v=535tJTI0c58&feature=youtu.be)
### Moderator: Hudson Jameson
### Notes: Sanchay Mittal

----
	
# Summary
    
## EIP Status 
| Status | EIP |
|-------|----------|
| Discussed under EFI. Discussion to be continued in EthMagician thread | EIP-1559, EIP-1962  |
| Under review for EFI. Decision required around needing a Hard Fork | EIP-2315 |
| Eligible for Inclusion Pending. | EIP-2046 |
|Not included | EIP-1930	|


## DECISIONS
	
**DECISIONS 80.1**: EIP 1930 will not be included. 

**DECISIONS 80.2**: EIP 2315 - Discussion to be continued in EthMagician thread.

**DECISIONS 80.3**: EIP 1962 - Discussion to be continued in EthMagician thread. 

**DECISIONS 80.4**: EIP 2046 - Discussion to be continued in EthMagician thread. To be included in the next call.

**DECISIONS 80.5**: EIP 1559 - Discussion to be continued in EthMagician thread. 


## ACTION ITEMS

**ACTION 80.1**: Wei and others will look into the implication of metatransactions on UNGAS.

**Action Item 80.2:** Creating a process, where people can know what previously happened, basically to leverage the experience. 

**Action Item 80.3:** Alex can bring few more experts on this topic, and greg will get carl and others involved too as EIP 1962 will be a major topic in the next call. 
 

-----

**Hudson**: Hello everyone and welcome to the Ethereum core devs meeting # 80.


# 1. [Eligibility for Inclusion (EFI) EIP Review](https://github.com/ethereum/EIPs/pull/2378)

**Hudson**: We're at the eligibility for inclusion (EFI) EIP review. The first one is going to be EIP 1930.

## [EIP-1930](https://eips.ethereum.org/EIPS/eip-1930): CALLs with strict gas semantic. Revert if not enough gas available

**Ronan**: TLDR; The desc of EIP is in this [link](https://eips.ethereum.org/EIPS/eip-1930).

09:24

**Martin**: Still not clear about the motivation behind it? What are the actual use cases? Why can't this just be solved by checking opcode?

**Ronan**: There are two issues: 1. Its opcode pricing dependent. 2. It's a waste because you are computing something which EVM has already computed. 

* Especially the use case of metatransactions, Gnosis safe tackled that issue by making changes in the UI. Which pushed the security out of contracts and made it vulnerable. 

**Martin**: I think it is a niche problem, and it is solvable today. But then, amount of work needed to solve is not that rewarding. And it is going in other direction, where we are trying to remove the gas visibility. 


**James:** On behalf of Alexey, who is working on UNGAS. Have you looked at ungas, and its proposal? 

**Ronan:** I looked at it, but I think implementing this proposal won't affect the path we need to follow when implementing UNGAS.

**Martin:** If we implement UNGAS, we will have to unimplement this. 

**Hudson:** I have looked at the proposal, and I can not find any security considerations that you are mentioning. I think you are using an Old EIP template, please add more details and use the new EIP template. Also, I would suggest talking to Alexey (UNGAS). 

**Martin:** I think we have Wei from UNGAS.

**Wei:** I agree with what Martin said, and implementing this will add more complexity when implementing UNGAS. 

**Ronan:** I think we decision is made on this, I will stop working on it. But just to specify, I don't see how this is adding complexity to the UNGAS proposal.

26:00

* Also, a thing about UNGAS. I think ungas implementation goes against the concept of metatransactions. 


**Wei:** This is a news to me, can you post reference links on gitter. So that, we can look into it further?

**Hudson:** Because even if this doesn't go forward as an EIP. Every other EIP need to understand the implications of metatransactions. To make things easier for users, and not adding complications to overall client-implementation. 

**Hudson:** Even if this doesn't go forward, thanks for bringing it up. We will connect you with Alexey and feel free to bring back more work on this and work with Alexey, and Wei ahead. Thank you Ronan!

**Ronan:** Alright, Thank you!

EIP 1930, will not go forward.

## [EIP-2315](https://eips.ethereum.org/EIPS/eip-2315): Simple Subroutines for the EVM 

**Hudson:** Brought by greg, also there is Ethereum magician [link](https://ethereum-magicians.org/t/eip-2315-simple-subroutines-for-the-evm/3941). 

**Gandalf:** Yeah, you can follow the discussion in the link above. Basically, this is a total strip down of EIP-615, no validation just providing mechanism of call & Return, and any validation has moved up a layer for the time being. Just the mechanism that says, I am making a subroutine call, so  I take the current construction pointer and push it on a second stack just like forth and when I need to return I pop the stack and go back to where I was.

**Gandalf:** Martin reviewed the code for the test cases.

**Hudson:** I think test cases are written once an EFI is accepted to avoid extra efforts on a thing which has not been blessed (accepted as EFI) yet. 

**Gandalf:** No, there are 3 pre test cases in the proposal. I didn't tried implementing them as code for test cases was hard enough but Martin reviewed that code, so I would like to hear from Martin. 

**Martin:** Regarding the test cases, I am not sure if these are traces or programs? It will be easier to understand, if you separate them. One thing, I am wondering about is the return sub, in the first test case you have not filled the return stack, and the return sub. 

* Should the return sub continue its execution after jump sub. Is that the intension?


**Gandalf:** Yes, its pretty much simillar to jump desk.

**Martin:** No, it is not. It's like you have a virtual jump desk after the jump sub. Though it looks much simpler than the previous one, I have to give you that. Technically it can be done, it will add one new stack. Though, I want to understand how big is this as an improvement. 

**James:** I think this was appreciated as an idea, we should take other's opinion on this. 

**Danno(Besu):** I support it, EIP 615 was too much at once, but this a great first step. 

**Hudson:** Great, anyone else?

**Martin:** I would like to revisit this, and ask from peter. 

**Hudson:** We don't need to push it to EFI, so we will wait for review of peter, and nethermind, and Alex. And if all feel comfortable, we can make it an EFI. 

* Thanks for that greg. This will continue to be under review. Let's move to the next one. 


## [EIP-1962](https://eips.ethereum.org/EIPS/eip-1962)

**Alex Vlasov**: Updates are mostly internal, changed binary interface to remove some restriction for the users. Also, made some checks in the pre-compile optional. What's left now is integration, and alternative implementation in Go which doesn't use assembly. My teammate is listening from youtube, and he told me that it will take 2-3 weeks. Right now, there are three implementations in "", C++ 17, and go in assembly x86 64 and these are consistent between each other in terms of acid testing. 

**Hudson**: Do you remember the feedback was given to halt this from EFI.

**Louis Guthmann:** I am just gonna come by, because I feel strongly about this EIP. After talking to the community offline, we have concerns about the process being used to implement this. 

**Martin & Hudson:** At this point, it is not eligible for inclusion, right?

**James:** It is already in the list. 

**Louis:** I think you did a terrific job on this, Alex. But my concern is if for window client there is a bug. And this is a gigantic curve, and you are only a single team working on this. 

**Alex V:** Yes, that's why we have been doing fuzzy testing. And have been running this from the beginning and after some minor changes. We now have suite dependent implementations.

**Louis Guttmann:** I think implementing such a big pre-compile with a tremendous assumption, by an independent team. I think it needs really careful handling. 

**Alex V:** It is done by independent developer, I only provided him help with faucet tester. This curve is very specific, it is only for caching and doesn't give a lot of benefits. It just allows you to use algebraic caches in the stream for just a bit cheap, to allow broader scope. 

**Louis Guttmann:** I am not against the ide of EIP, I am just concerned about the situation where there is a dDoS attack, then it makes you the attack victim. 

**Hudson:** Martin, can you shed some light on the event there is a dDoS attack?

**Martin:** Yeah, so in this case we get on a call with core dev to sort it out. But these kind of pre-compiles are not in our domain, so if something was to happen, we will keep scratching our heads. Yeah, so this EIP scares me a lot. Cryptography is not that scary, but incase of a DDoS attack, or consensus issue. Or a pre-compile calculates something erroneously. It will be really bad.

**Alex V:** Incase of DDoS, there are no infinite loops. And I have fixed value of 1.5 for security measures, so miscalculation of gas is not possible. My only concern is consensus between different implementations but the errors we founds in the testing were not in the formula or arithmetic. They were in the binary interface.

**Hudson:** So, when we are kind of doing risk versus rewards, this is going to unable a lot more use cases and enable lot more different curves that can be used for some of the new Stark and Stark stuff. So, the concern of Martin and louis tell us that we need a response team incase of bugs and errors down the road. 

* Alex Vlasov,Louis, and hudson discuss about including other people in the call and maybe merging it with other EPIs. (50:00 - 57:00)

**James:** I can see there is a value in implementation, but also we don't have process to implement something like this, especially on a security front. 

**Hudson:** Sure, we can come up with a process for it offline. Any final comments?

**Martin:** I think, this is a wide implementation, and will jam ethereum. Hence, I am against it. 

**Tim:** Doing the whitelist process Alex told, and having calls from 10 people about this. Would it change your mind?

**Martin:** Yes, Likely! When I browsed around on this, the gas schedule explainer is a lot of text and mathematics, and I have never seen this in EIPs before. And its code implementation doesn't seem possible. Essentially, I am not comfortable with the formatting. For eg, for complex model evaluation rules, there are two pages of text.

**Alex Vlasov:** I tried to be more expressive, but you can tell me the issue on gitter or on DM. 

**James:** Martin, I have shared the georgie valina EIP, does this format looks good to you? Maybe Alex could converge with georgie on this.

**Hudson:** That sounds like a good idea, because if
the formatting that they're using for the baby Jubjub curve (Georgie Valina EIP) is more clear then yeah if you could converge on that style, that'd be nice.

**Alex V:** I am looking at georgie's EIP, and I think it has same level of difficulty. 

**Louis:** I have a question on the previous process of accepting the EFI, getting it to the end, and pushing it. Talking about the current implementation of the pre-compile in ethereum.

**Hudson:** It was a collaboration between Electric coin company, and EF to implement the same curve that was used in Zcash. That was basically engineers coordinated with C++ team. Fuzzy about rest of it. 

**Martin:** I can't recall the details. But it was a lot of work, more than a year. And it was simpler than this.

**Louis:** Can we get it attested by someone who writes code, and understand the crytography as well. 

**Hudson:** Yeah, sure. We can dicuss this offline. I don't want to take further time on this. And don't want this amount of work to go in abyss. 

**James:** Eth 2.0 *deposit contract* was planning to use this EIP. 

**Hudson:** Are they using the new BLS curve, which filecoin is using?

**Greg:** Yeah, we need the new standard because the current implementation we have won't suffice the need and I believe it is because of the curve. And EIP 1962 covers our requirements. 

* The current coversation about EIP 1962, seems like a lot of work. So, to support the requirements should I create a standalone EIP for BLS verification. Simply, because deposit contract mainly has four main checks. And one check we don't have is the verification. 

**Alex V:** From this perspective, to really make your life simpler. I can focus on one simple interface of one single curve. If you really really really want a simple separate pre-compile that's only BLS curve.

**Hudson:** Can you get some people who have worked on this, like Carl. To shed some colour on this?

**Greg:** Yeah, I will. The contract is already in audit, and if it gets late. We will have to get it reaudited. 

**Hudson:** Okay, let's move on to the next point. 


**Action Item 80.1:** Creating a process, where people can know what previously happened, basically to leverage the experience. 

**Action Item 80.2:** Alex can bring few more experts on this topic, and greg will get carl and others involved too as EIP 1962 will be a major topic in the next call. 


## [EIP-2046](https://eips.ethereum.org/EIPS/eip-2046)

**Hudson:** Alex is not on the call, so maybe we can skip that. 

**Danno:** I would like to raise some concerns about that. First we need to get clear on what pre-compiles are?

**Martin:** It has a reference in the EIP. 

**Danno:** Second, we need to reprice the existing pre-compiles because they are all based on 700 call as far as the impact on the rest of the VM. So, I want to see some stats on what those re-pricings are ought to be. 

* Alex asks a really good counter question. (76th min)

From 77th min,

**Danno:** I will feel more comfortable with the stats, I just want to show that we are not gonna break the meter if we just get rid of the call. 

**Martin:** Yeah, having more benchmarks is definitely better. 

**Louis Guttmann:** I have a question, I know that we went from 700 to 40, but what stopped us from going to zero. As it was in the starting. 

**Martin:** Currently, the only thing which costs us zero are jump test, and stop. And doing a pre-compile is more work than nothing. 

**Alex Vlasov:** Consider the fact that it needs gas measurement and then subtract this price. 

**Louis Guttmann:** In that case, it was more into pricing the pre-compile itself.

**Martin:** Yes, but then you need to do the actual gas calculation. So you need to enter the gas calculation of that pre-compile and before doing so, you have an upfront cost, in this case 40 and currently 700 but you need to offset the cost of doing the gas cost calculation at the minimum, we need to cover that. Makes sense?

**Louis Guttmann:** Just for instance, in case of Blake which is supposed to be cheaper and faster than keccak make its mechanically pretty irrelevant to use except for Zcash purposes.

**Danno:** One round of blake, should be cheaper than addition. 

* Louis explains his concerns, and james asks this to timebox. Hudson agrees, as lots of history is being lost in this. And we should take this to gitter to have more voices along with Louis's Question

# 2. Next Upgrade Timing (based on EFI list)

**James:** One of the reason of this, was to estimate which EIPs can be included in the hard fork. 

**Hudson:** Yeah, looking at it. If EIP 2315 gets into EFI, it looks easy. And the EIP 1962 will make a bigger difference for Eth 2.0, so we should focus our next meeting on EIP 1962. Figuring out, how much time will it take for implementing and testing considering that fuzz testing has already started. Danno, would you like to give some views on it. 

**Danno:** Yeah, EIP 2315 is relatively simple. Just one-two week tops, need to write simple record tests. But EIP 1962 is a wild card, and it include deep builder issues which gives me a spinball. And down the road, we may get request from Hyperledger ursa to use their encryption. So there are a lot of moving parts. 

**James:** Any other EIPs, what about the one Danno is working on, EIP- 2456.

**Danno:** Implementation wise it is doable, but specs wise to make everyone happy. It is going to need a bit more time. So, I don't think we can include it in berlin.

**Hudson:** So, I don't think we have anything else in the EFI list. Other than progpow, if it gets pushed and happens. 

**Tim:** I think, in community it's a given that we are going to include EIP-1559, but we haven't discussed it much. So, I will need some thoughts on that. 

**James:** So they made it so it's one fork but then has two activations but it you don't need to happen so they
they so it wouldn't be like a multiple you need multiple force implemented they've changed at where for me this more complex. Something like this in ecosystem.Longer I think it should be on a testnet and so I don't normally
six weeks okay cool great for a test that but I think something like EIP 1559 would need to be on Ropsten for a longer period of time to make sure that gas and all of those things works as intended.

**Tim:** I think we discuss if we should test it on ropsten at the time of fork, or delay it a little. 

**Danno:** We can also do an alternative of ropsten, and split up a new testnet just for the fee market. Only challenge will be bringing traffic to test those smart contracts.

**hudson:** hey Trent does white box new testing
framework simulates smart contract data once a test Nets spun up so we can like simulate that crap.

**Trent:** It will definitely, in the future. I'd have to double check to see what our current future studies but that's definitely something we've been thinking about actively and and kind of trying to integrate into the platform.

**Hudson:** Okay thanks! I feel bad that we were not able to cover Open RPC standards that Zach brought in. Zach, if you want to talk about it in a min, people will have something to think about. And I promise, it will on the top of the agenda list next time.

# 3. Open RPC


**Zachary:** Since I only have about 10 seconds I'd suggest just having a look at what we have that open- RPC org and that's probably a good place to start but the general idea isthat we're building a service specification language based around JSON RPC.

**Hudson:** We will include it in the next call. Sorry for not being able to cover the rest. 

**Tim:** One last quick thing, james has made the PR on EIP 1.

**James:** The list of EFI came up because on 2378 the eligible for inclusion it has some information about how the process works and after some discussion with Alex I
realized that all of that kind of meta information about how things work should all be in ther so people have a
consistent way to find it and this should be a single source. Hence, I made a pull request to the EIP-1 that includes a table of contents that also includes part of the eligiblity for inclusion and piece is and then it also has some of the Alex had a meta data of EIP 233 which is the formal process of our Forks I took the
meta information from that and also added it.

**Hudson:** Great, this is part of agenda item 4. (i), if people wants to discuss or add comments on it. Also, there will be a EIPIP meeting next wednesday. Interested can ping me, and I will add you to it.


# Attendees

* Alex Vlasov
* Artem
* Daniel Ellison
* Danno Ferris
* Gandalf
* Gichiba
* Greg Markou
* Hudson Jameson
* James Hancock
* Louis Guthmann
* Martin Holst Swende
* Pooja Ranjan
* Shane Jonas
* Tim Beiko
* Trenton Van Epps
* Wei Tang
* Zachary Belford

