# Ethereum Core Devs Meeting 65 Notes
### Meeting Date/Time: Thursday 18 July 2019 at 22:00 UTC 
### Meeting Duration: 1hr 40mins
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/111)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=41kiRf1E-jI)
### Moderator: Tim Beiko

----

# Summary

### DECISIONS MADE

**DECISION 65.1.** Every EIP without a reference implementation except the few exceptions which are 1352, 1845, 1985, 2027 and 2046 will be dropped for this upgrade.

**DECISION 65.2.** Not having EIP 615 as part of Istanbul.

**DECISION 65.3.** EIP 1965, 1707, 1712, 1959, 2014 dropped from Istanbul.

**DECISION 65.4.** EIP 2028 accepted for Istanbul.

**DECISION 65.5.** EIP 2200 tentative accepted.

**DECISION 65.6.** ProgPOW out of the Istanbul and the hardfork as soon as the audit is ready.

### ACTIONS REQUIRED

**ACTION 65.1.** 1283 / 1706 - Overall functionality will be the part of Istanbul and we will review Pawel's proposal.

**ACTION 65.2.** Next ACD call will be out of cycle on July 26th at 1400 UTC.

**ACTION 65.3.** Figure 1344 issue out and then potentially except it in the next call if we have consensus.

**ACTION 65.4.** EIP 1962 continue to be part of the discussion on the next call.

-----

**Tim**: Welcome everyone! As we discussed in last ACD, this is the chopping block call for Istanbul. Hope we get to agreement over EIPs in Istanbul upgrade. 

# 1. Istanbul EIPs Chopping Block


**James**: As we discussed last week, we are going to use the core dev call to **look at which one have reference clients** and which one don't. In case they don't see if there is someone here on the call to defend why they should not one or why they should be exempt from this cut, then this is the time to make that defense. I'd like to keep this conversation pretty focused because we have a lot to get through. The format is going to be, I say the status.  I read through all of the EIPs and looked at their their implementation inside the EIP.  So if I'm out of date on any of the information then I'll say that if it has a reference or not and I'll ask if anyone here will fight to keep that EIP. And if there isn't anyone that steps up then I'll move on to the next EIP.

**Tim**: Sounds good.

**James**: I'll start from the [top]( https://docs.google.com/spreadsheets/d/1Mgo7mJ6b6wimUwafsMo1l-b44uec28E_Hq8EQ7YdeEM/edit#gid=0) and then after that we'll go through the list that you have of once you go in deeper conversation. I want to keep this really moving along so it will be quick.


* **615: Subroutines and Static Jumps** - has a reference comment.

* **663: Unlimited SWAP and DUP** - doesn't have a reference client. 
**Pawel**: I have a implementation of it.
**James**: Okay, I'll add that.

* **1057: ProgPOW** - has reference client or reference implementation.

* **1108: Reprice alt_bn128**  - has reference client or reference implementation.

* **1109: PRECOMPILEDCALL Opcode** - doesn't have a reference client. If no one has a defense for that then I will leave that one is not having one.

* **1283: SStore Net Gas Metering** - does have a reference client.

* **1344: Chain ID Opcode** - has a reference client.

* **1352 Restricted Precompile Range** - does not have a reference client.

**Pawel**: I think the last one **doesn't require any implementation** changes at this stage.
**James**: Okay so then I can also mark that one as as not needing it.

* **1380: Self Call Gas Costs** - does not have a reference client. does anyone have a defense for that?

**Louis**: Can you repeat?
**James**: 1380 ?
**Louis**: Not mine, I won't talk.

* **1559 Fee Market** - that one doesn't have a reference client and it's not close enough. I can get an update on that later but I won't do that part of as part of this discussion.

* **1702 Account Versioning** - has a reference client.

* **1706 SStore Diable below GasLeft** - does have a reference client.

* **1707 Use Version Byte Prefix for Contract Account Versioning** - does not have a reference implementation.

**Wei**: That should be **dropped**. 

* **1712: Disallow Deployment of Unused Opcodes** - does not have a reference implementation,  does anyone have a defense for that ?

**Wei**: It's not in the meta HF 1679.

**James**: It hasn't been merged at yet but it was submitted in time so that's why I kept it on the list. If it has a reference, then we say it has a reference and then we can come back to that as another discussion or it doesn't have one?

**Wei**: Okay it doesn't have one. I will **drop** this. 


* **1803: Opcode Rename** - that has a reference client.

* **1845: Fork Name Standards** - No reference client. **Not needing one**.


* **1884: Trie Dependant Repricing** - has a reference client.


* **1891: Contract-based Account Versioning**- No ref client. 
**Danno**: I think 1702 is preferred solution over that.


* **1930: CALL with strict gas** - No ref client. 


* **1959: Method to check if a chainID is part of the history of chainIDs** - No ref client. It needs one.  
**Tim**: In last call, it was advised to be **dropped**.
**James**: I will put that I will also note that too.



* **1962: Generic ECC Precompile - 1829 / 1962** - has reference client. 
**Alex V**: It was posted this week like preliminary PR in Parity, was Rust implementation. C++ implementation finished, today which most likely be integrated with Go Ethereum. Up to the preference of developers. Either integrate rust into the compiler pipeline to assemble or just use native Golang compilation with C++.   



* **1965: Historical ChainID** - No reference client, does it need one?
**Danno**: it needs a reference client.


* **1985: Limit EVM Parameters**  - that one does not have a reference client.
**Pawel**: I don't believe it requires one because it's just some papers specification which is being discussed but also evmc implements most of this parameter. 
**Martin**: I don't know where that leaves us we need it or not.
**James**: tbd


* **2014: Extended State Oracle** - No ref. implementation. **Dorp it**
**Alex**: nothing happened on that front. I guess this won't be needed  right now. **Drop it**.

* **2024: Blake2b**  - has a reference implementation.


* **2025: Developer Block Reward** -  has a reference implementation for the one that it depends on. This is mine so I would need someone else to make this call. I think that it is simple enough that it's okay to not need one. And maybe we can come back to that one Tim, when I head back off to you.


* **2026: Fixed Prepayment (H)** - No reference client. 
* **Alexey**: No reference implementation done yet. 

* **2027: Net Contract Sizing (C)**- No ref client. TBD
* **Alexey**: Implemented but not in the client which can provide the conformance test, which is my defination of reference implementation. so no reference implementation yet. We will see how it goes but it might be dropped. 
**James**: Okay I'll leave it leave it in for now.


* **2028: CallData Gas Reduction** - reference implementation.


* **2029: State Counters (A)** - No reference implementation.


* **2031: Net Transaciton Counter (B)** - No reference implementation.


* **2035: Stateless contract storage** - No reference implementation.


* **2045: Fractional Gas Cost** - it does not have a reference implementation. 
**Casey**: We have one, but we havn't pushed it yet.

* **2046: Reduce gas cost for precompile call** - No reference implementation.
**Alex B**: It **doesn't need reference implementation** because it's a one line change. But there must be an agreement from Jordy.

**James**: That is all.

**Tim**: Thanks, James. In terms of next steps does it make sense to say that the ones that do not have a reference implementation and that didn't have a justification for that should be dropped for Istanbul?

**All**: Agreed. 

**Tim**: It seems like we have rough consensus that **everything without a reference implementation except the few exceptions we mentioned which were 1352, 1845, 1985, 2027 and 2046 will be dropped for this upgrade.**

**Tim**: Okay, moving on to the next section. These are EIPs that have been discussed and that may or may not be ready to make it over to the finish line to be accepted for upgrade. So now I'm back to the list on the agenda for the call. I am going to go through them sequentially. If anyone has thoughts about them, comments, please speak up. I gather this list by asking everyone who was on the previous call which EIP they thought were most important to discuss. So there's no specifics speaker assigned to any of them. 

## EIP-615

**Tim**: The first one out here is 615 which is in the last call right now.

**Danno**:  That's the one to add on about 10 different opcodes, on about three themes which is jump, subroutines and code data. There are no test in this and there's a little bit of push back by the EIP author when asked to add test he wants to be grandfathered in under the old rules. I don't think it is prepared enough to go into a hard fork in about a month or month-and-a-half. I think there's good ideas in there but I think it would be better served on a future hardfork.

**Martin**: I would be in favor of dropping it. 

**Tim**: Does anyone disagree strongly with this and wants to fight for keeping it in the hardfork? 

**Danno**: This isn't final rejection, just a not Istanbul rejection. 

**Tim**: Okay, so I think we have consensus on **not having 615 as part of Istanbul** but not fully dropping the EIP, if in the future it has more test.


## EIP-1344 vs. EIP-1965
Can we make a decision on EIP-1344 independently of EIP-1965?

**Tim**: Next one on the list is 1344 and 1965. There was a lot of discussion in Gitter in the past week. Can we make a decision on 1344 independently of 1965? Author for 1344 is not on the call. Does anyone else has anything to say?

[fubuloubu](https://github.com/ethereum/pm/issues/111#issuecomment-512301640): Re: EIP-1344 vs. EIP-1965, as I said before I won't be able to make the meeting until almost 1.5 hours into the call. Calls usually go this long, so if I am needed to make a decision on EIP-1344 I will try to attend. If not, if someone could inform me via Gitter when that decision is made, it would help me out immensely so I am not rushing to join the call to find out everyone had already left. Thanks!

**Wei**: Why do we need a new chain id opcode?

**Danno**: This is a fork protection. 

**Martin**: There is also an another one. There is acontract that says what is the canonical hash of a blockchain. If I have to deploy that contract on Ropstan, Rinkeby and Mainnet. It is nice to have same set of signer keys for the test networks. When signatures is validated onchain, its nice that the signature also says the chain id. SO, now I can just take the signature and submit it. One who validates it can understand the signature is for Rinkeby or Ropstan without ctually knowing address.

**Wei**: Okay, I do agree it has uses. I don't think its possible to define the chain id of a block but it is possible to define the chain id of the transaction. 

: How could you change a chain id within a block?

**Martin**: In practice, it is exactly the same thing. yeah I agree with what you're saying. Any code that is executed in is always in reference of a transaction.

**Wei**: It is not always the same because we can still send transaction risks no chain id that is replay protected. In that case, it will be different for those two definitions. 

**Martin**: Why do you prefer, can you explain us?

**Wei**: There is not a clear way to define what is blockchain chain id and also the issue is that it might change. It may not be good for forward compatibility.

**Martin**: One possible drawback is that if someone forks Ethereum, having the chain id opcode will actually discourage them from changing the chain id because it might break things?

**Wei**: Yes. It depends on how chain id opcode is used. We have a lot other opcode that are dependent on the transaction. I think if we don't define chain id as a property of the blockchain. Chain id can change in future.  

**Adrain**: I think it would be the property of the current block, so it would be which chain id is accepted. You see that change in the hardfork later. The only difference in practice, if weather or not chain id returns zero now. 

**Martin**: I would kind of agree. 

**Tim**: Given the uncertainty, is this something, that can be resolved for Istanbul or it has to go to the next upgrade?

**Wei**: I don't think it is an inherent property of a block rather is a property of a transaction.

**Martin**: I would kind of agree.

**Tim**: Given the uncertainty, is this something, that can be resolved for Istanbul or it has to go to the next upgrade?

**Martin**: There may be security implications aside from the actual implementation thing.

**Danno**: We can keep conversation rolling into Eth magician thread.

**Alexey**: I just reread the initial preposition for this change. Essentially the reason why it was proposed smart contract wanted to ensure that a transaction which was given to it will actually replay protect it for the current blockchain.  So in this case it does make sense the chain id returns the id of the current chain rather than the idea of the current transaction because otherwise you can trick the smart contract into accepting something that it didn't really want to accept. At the moment, the chain id had to be hard coded into the smart contract, but the idea was that it would be more generic. 

**Wei**: I think you can just check weather the chain id return zero?

**Alexey**: You could but it's basically like what you suggest is Define the original purpose of this change.

**Wei**: Maybe we can discuss this later

**Tim**: Yes, to be mindful of time. Given how small of a change is this do we want to put it on hold for the next call; resolve those issues and then potentially still include it or do we want to push it for the next upgrade?

**Alexey**: There was quite a lot of discussion about it already in the Gitter and in The Magicians. Now we go around in circles; so I would just basically implemented as we agreed. 

**Wei**: What is the agreed version?

**Alexey**: The agreed version is the opcode to return the current change on the blockchain. Because I understand that you might have some kind of statical issues with it but I think they're just pure statistical from my point of view. 

**Wei**: I don't quite agree with that. I still think that using the chain id of the blockchain will have a lot of potential  backward compatibility issues in future. Its not future compatible. Which I see is probably not a good idea.

**Danno**: What are those features going to happen are we going to have lunch and you have multiple checking IDs in the same block . That seems like a new concern. 

**Tim**: And just to be mindful what time we're almost halfway through to call and we have a lot of EIPs to get through so is it worth pushing back this discussion to Eth magicians and following up on the next call, unless you can get resolution in like nex minute or so? I think it's probably more productive to go through all the other EIPs.
No one seems to disagree vocally, so given how small of a change it is let's just go back in and figure this issue out and then **potentially except it in the next call if we have consensus**. 


## EIP 1965

**Tim**: Another one that's related to this is 1965 does anyone have thoughts on that one?

**Danno**: I don't think we should facilitate minority forks but yeah but we put in mainnet. If you want to do that they can proposed changes. I think it's more work than needed and I think they both can go in it's not an either-or.

**Martin**: I agree. We could drop it.

**Tim**: Does anyone disagree with dropping this? 
So let's agree **it's dropped from Istanbul** on the very least.


## EIP-1283 / 1706
There was [an AMA](https://ethereum-magicians.org/t/eip-1283-1706-ama/3467) with no further questions about the EIP.

**Tim**: For some context there,  we wanted to move the conversation on this and tried to organize an [AMA](https://ethereum-magicians.org/t/eip-1283-1706-ama/3467) on Eth Magician. No one seemed to had concerns that they brought up there. Hayden from Uniswap came in just to say they supported this. I don't know if anyone has opinions about 1283?

**Wei**: I think its just the documentation issue.

**Danno**: Is it the one in ACD Gitter discussion about merging and context to another EIP?

**Wei**: Yes to EIP 2200 . It is just to facilitate 1884 also 1283 a little bit. 2200 does combine 1283 and 1706.

**Tim**: Does anyone disagree to accept 2200 as a replacement for 1283 and 1706 in Istanbul? 

**Alex B**: I want to make a note - it was discussed a few times that there should be new EIP for 1283 and the reasoning against it in the last call was that there are a lot of the clients have 1283 implemented SS, which was enables for Constantinople and then disabled for Petersburg. This clients would want to keep this behavior and have to switch toggled again to enable it and there was a reason for not renaming and if you were having a New EIP. 

**Danno**: Is it that 2200 resolving some conflicts between another proposed EIP , it's not a direct a implementation? 

**Alex**: It does have a  full spec.

**Wei**: What was the question again? Is it about reference implementation?

**Danno**: What percipitated the need for 2200? Was it because it conflicted with EIP that need some clarity?

**Wei**: It is actually 1884 which change the gas price of log. In that case 1283 has hard dependency on the old log gas cost. Itis hard coded there. We need to change the spec of 1283  a little bit. In that case we need a new EIP for that, that is 2200.

**Alex B**: Can we clarify what 2200 is? This was discussed just  5 minutes before the call. My understanding is that 1884 changes to cost of a s-load and 1283 isn't changing that.

**Wei**: I can explain, 2200 does not change anything regarding s-load.  It's only change s star gas cost. There is no logic change, nothing else changes. 

**Danno**: So, it's basically the same as 1283? 

**Adrian**: It sounds like we are in agreement that we want the functionality of 1283 and 1706 and it's just a question of how we document it at this point.

**Martin**: 2200 seems like the summary of the entire thing.

**Adrian**: Yeah, I like the clarity since it seems to be interacting with other EIPs are likely to accept. 

**Casey**: So I don't think 1706 should be bundled with what's 2200 / 1283,  just because versioning is a huge change that would apply to many EIP is going forward.

**Danno**: 1702 or 1706 ?

**Casey**: 1706 

**Tim**: Casey, just to be clear are you objecting just on like the documentation / bundling?

**Casey**: Just the bundling.

**Tim**: Just to be mindful of time, does it make sense to go forward with all the functionality described in 2200 for Istanbul and we sort out the documentation outside this call?

**Wei**: This also means we apply net gas metering leaves out account versioning.  

**Danno**:  1706 usually bundle with 1283. 1706 is s store, so that doesn't need to be bundled anymore. 1702, I think in last call, we also decided not to bundle it 1283 and 1706 across all versions. 

**Casey**: Just to be clear, if you do not test or metering weather 2200 or 1283 without versioning then are we in the same situation before Constantinople.

**Wei**: 1706 is a fix.

**Tim**: So does it make sense to **move forward with 2200 in functionality and then sort out the the naming a thing**, does anyone disagree with this? 

**Alex B**: Can we clarify that we want to bundle with 1706 to fix for s store or we don't ?

**Wei**: 2200 contains the calls in 1706.

**Tim**: We do everything in 2200 and we determine whether we call it 1283 + 1706 or 2200,  does that make sense?

**Martin**: I don't object it but I don't follow either.

**Tim**: To the functionality or documentation?

**Martin**: The whole thing.

**Pawel**: I propose a different approach to 1706 and now its bundle to something else.

**Martin**: What was your idea?

**Pawel**: It was to disallow any states when you enter a call with low gas a fraud. 

**Martin**: Will that lead to log operation?

**Pawel**: No, logs will be allowed.

**Martin**: I think that's an elegant approach.

**Pawel**: Its not the time to go into detail, but I would like to get feedback on it.

**Wei**: I just think it might actually be more complicated.  

**Pawel**: I put some reasons why it is better from my perspective. Let's read it first and then you can discuss offline?

**Wei**: Are we not making a decision on 1283 1706 and by extension 2200?

**Alex**: Can we agree that it's tentatively agreed until this proposal by Pawell will be reviewed by the next call?

**Tim**: This **overall functionality will be the part of Istanbul and we will review Pawel's proposal** and also at the same time how we bundled it all but there's general agreement on the functionality.




## EIP-1962

**Tim**: Okay next one on the list is 1962. Does anyone has opinions on it ?

**Alex V**: Since the last developers call, it's much easier to integrate a C implementation into the Geth client at least. So right now it's a C implementation which will be integrated. Or as an alternative we can all suggest to integrate building Rust implementation. It is actually up to developers for which option is better . But right  now, it has two implementation which are I quite independent.

**Martrin**: Since it's fairly complex cryptography, in my opinion, I would like to see both of these libraries finished and publicly out there for a couple of months. 

**Alex V**: It is largely finished.

**Danno**: I think what Martin is trying to say is he will feel better if Istanbul wasn't hard enough. It's a big change and it needs more review time. 

**Martin**: Yes, that's what I am trying to say.

**Alex V**: If we use the same code base in principal and continue to review it and improves the quality but for hardfork, we just give a set of 6-8 curves which are more likely is most interesting for developers for next year or half a year and take it into next hardfork, it will be allowed to use the generic frictional.

**Danno**: But this is already the most complex precompile I've seen specified.It has  four direct branches, based on the first parameter with different gas metering rules. It's deceptive to call a precompile. It is at least four different things. And you are adding on more possible curves in the future. I'm not comfortable getting it in this this one, right now.

**Martin**: We had consensus issues on per compiles which is most trivial fix. Define and trying to fix it, is very devious because when you submit the patch to a library in crypto, it's pretty obvious that you're touching in a way it could be exploited in a second. I am very weary of these nights, would like to have  2 or 3 implementations differential. I assume they won't crash but differential for a long time. It's too soon.

**Alex V**: Differential testing is the testing that we are doing right now.  Just from the implantation perspective it's actually one precompile because as soon as you implement one curve,  you get all other for free. It's it's not that difficult.

**Danno**: Pairing check is completely different syntax on the parameters that comes after that parameter.

**Alex V**: Oh well! It just depends on what you define, as a totally different zip binary interface is different but those are for developers and most likely those will be just hard coded. The first part will be hard coded by developers and well in a smart contract. In terms of arithmetic, it's not that different altogether. We will test for complete. Any discrepancy in completed kind of universal and generic mode of using is the existing codebase. We don't need user to allow users to poke the contact list all the available parameters, which  in principle will give you universality. But we can just limit those parameters to be  released which will respond to instantiation of 6-8 curves. It would exponentially reduce the scope of precompile for next fork.  And then if we requested testing then maybe at some point we get one more alternative of implementation in some other language may be. In this case, this restriction can be lifted and then users won't cap. In principle the same code base with the same rules for gas metering which is still quite Universal but not too complex but then they will be kind of marshmallows chance of there was some natural problem which wasn't seen. To  Implement something just for a set of specific curve specialist for, in two separate languages which are not direct relatives from one another. It's actually not as difficult.

**Alexey**: I wanted to suggest something. I want to suggest for now the optimistic approach. To me it look really are a very attractive change. Also, I can see that the guys working on it seems to very productive doing a lot of stuff in very short time. So I think we should just wait and see what happens in, that show us instead of being a super defensive.

**Alex V**: I also second that in context of looking at all the EIPs,  there's a handful of that are the furthest along as far as testing and fines and being reviewed and this is one of those. 

**Danno**: Another questions I asked on Eth Magician wasn't answer.As a developer I would have a nightmare trying to have to cram all of parameters in binary string. And I would like to hear what do you solidity invite things about the usability of the interface. Cryptography sounds great in everything, I have concerns about its usability as a developer.

**Tim**: Just to be mindfulness of time again and based on what Alexy  and James had previously said, does it make sense to deal with those questions offline and come back to this EIP on the next call similarly to 1344?

**Danno**: Yes, I asked my question 11 days ago. We can keep discussion on Eth Magician.

**Alex V**: Didn't spend too much time on there, sorry. Only question I would like to clarify from the core developers what is the suggested time for fuzzing  testing  in terms of  CPU days in a multiple core system,  or like what was their previous experience for this purpose?

**Martin**: That's hard to say I don't have a good answer to that. But, generally may be weeks or months. 

**Alex G**:  If we can define some criteria by next call or during Eth magician then will help. If we don't have them we never be able to get there. If we have them, It will be best indicators. 

**Martin**: I can't give them such figure, but if all the codes are published and steps for doing testing helps setup. So that anyone else can take it for spin. I can't give hard matrix.

**Alex V**: OKay, I will write a manual about this. 

**James**: I think they are connecting the Solidity team or the Vyper team to have the feedback on UI. It's a good Action Item for the Cat Herders.

**Tim**: Will follow up on that offline.

**Alex B**: Just a quick question, why there an opinion needed from the Vyper or Solidity team ? Is it expected to like language level support for this?

**Danno**: They require end user to create a binary blob and cram it in. As a  developer, I feel that's a bad experience and should be improved.

**Alex G**: Provide a convenient library for it which is very straight forward.

**Alex B**: I would believe it has to be some kind of the library and it doesn't need language support. If the question is about the the overhead of crafting the message then it doesn't really matter if that's single first bite is there because the rest of the encoding might have been over head anyway in EVM.

**Danno**: My concern is reading it. We  have to have a library. There is  something I would expect from the name of the function not at the value of the first parameter of the function. I think we should move this discussion to Eth Magician because it's not gonna get solved on this call. 

**Tim**: I would agree with that. Let's **have this a part of the discussion on the next call**. 


[shamatar](https://github.com/ethereum/pm/issues/111#issuecomment-510432038): Initial PR for **EIP1962 into Parity is complete** ([link](https://github.com/paritytech/parity-ethereum/pull/10874)). For Geth two options will be provided over the next two weeks:

Add building of Rust code into the pipeline and use Rust implementation
Alternative C++11 self-contained implementation for use with CGO
Plans:

Complete gas metering procedure (1 week)
Generate more initial vectors for fuzzy-testing (1 week, along with gas metering)
16+ CPU-months of fuzzy testing using libfuzzer and honggfuzz




## EIP-2028

**Louis**: About EIP 2028, we released 2 reference implementation are available on GitHub. Today we released the analysis to find the new price. So we found a price wear for which we're comfortable which is 16 gas per byte. Core Dev have any opinion and so we can make into Istanbul?

**Martin**: I think it looks good. I have no objections. 

**Tim**: You have no objections to include this in Istanbul, is that what you're saying?

**Martin**: yeah I'll be glad to hear other opinions.

**Tim**: Does anyone object with included in 2028 ? Do we have consensus for 2028 that's part of Istanbul?

**Danno**: Let's do it.

**Alex**: There were some comments to decrease the cost even further and is there any chance that the numbers could direct into that direction?

**Louis**: The reason why we came to 16 is because there was a short time before Istanbul, so we came up with very conservative numbers and there was discussion about the EIP 1559 which would want to use further reduction for identity for the new IP. We don't have any objection, our take on the matter would be go with this reduction for this hard fork and may be push it for the next one.

**Martin**: From a conservative perspective, it would be better to lower by 2x instead of 4x. Now that I see this, may be I can agree that 4x is reasonable.

**Louis**: Agreed for the same reason. That the same reason we came up to that number.


**Tim**: 4x is currently the number in 2028?

**Louis**: 4x is currently the number. The main impact of 2028 will be  security. 2028 is about Network propagation. We came up with blocks that are 20 times bigger than the average block size in Ethereum which would not even create any Uncle. 4x is very reasonable based on the output that we provide. 

**Martin**: This is on mainnet?

**Louis**: Yes, **This is on mainnet**. There is all the link, there is address for you, the day we use. We made the biggest day in the history of Ethereum.

**Alex**: Did you say, that you used 0 bytes?

**Louis**: I am going to explain the process to create the packet. For compression algorithm, the worst case scenario is a random byte, everyone agrees?  Random byte,  no pattern, no one can compress. So what we did was treating a random string of bites replace all the zeros in that random string  with other random bites from from 0 to 2055 and then what we did is randomly choose an index, add a 0 and add 16 zeros at the end of the string and shift for the whole thing.  

**Caseo**: Clarifying question. So it does not specify an explicit maximum block size.

**Louis**: Since blocks are defined by block limit. What we say is that we should reduce the size of the code. We are being conservative for very simple reason that this EIP is need by every layer 2 and we are looking for the most conservative numbers we could find is already - 4. 4 is very conservative, based on our experiment. 

**Casey**: Great! but reducing the cost of a call data by 4X,  the thing is when on the mainnet that experiment using a lot of 0 bytes because it keeps referring in the post in Eth Magicians to the uncompressed size and people are using non zero byte than you get compressed sizes which are much larger than we have seen in your experiment.

**Louis**: Compression algorithm look for pattern, they don't even care about the exact byte. I could show you the snappy compression for our strings and they are exactly same ratio. The address in the post, you can look at any transaction there is extra data fee on the blocks we can try to compress it. You see will be the same ratio. once again the pricing of zero doesn't seem to make a lot of sense and that was already discussed last time on the core dev call.  We don't want to change it for compatibility and existing contract. We actually use that fact to do the analysis so this is completely  like Independence. If you look there,  and we managed to make like windows which are 7.5 times bigger than the average size. that's why we took 4 because basically half of it and it is pretty conservative. 

**Casey**: I guess it just explain doing even more aggressive cost-reduction it's only been proposed in the context of also having an explicit maximum blocksize which will be conservative. 

**Louis**: As Martin suggested, -2 dimension, data proving -4 being conservative, I think we should all go for it and go further if needed in the next hardfork.

**Tim**: Great, does anyone disagree with that? So,  **2028 accepted for Istanbul**. 


##  EIP-2024


**Tim**: Other one on the list is 2024. I think this was an issue around the gas cost.

**Danno**: Gas cost isn't specified now in the EIP and also in the Eth magician about byte ordering. I haven't seen much resolution on there. Not sure, if anyone on the call is championing that EIP?

**Tim**: Okay 

**Martin**: Yeah, it landed on 1 per round.

**Danno**: Is that in the discussion forum or do they plan to make it into the EIP?

**Martin**: I don't know if they plan to make it into the EIP, I thought it had. I am not the author but taking part in discussion. And that by the benchmarks by them and by me. 1 per round seems pretty reasonable. 

**Danno**: Did we get resolution on the ?

**Martin**: Not that I am aware of.

**Danno**: That's a bigger consensus concern than actually the gas. 

**James**: There's a part of discussion on it but I don't think it's worth, trying to make a decision on it without them being here.

**Martin**: I think that will be resolved.




### State Rent EIPs

**Tim**: Other EIPs that people brought up was State Rent and general.  So, to get a feel for any specific ones that will contribute in Istanbul?

**Alexey**: There was only one which basically was kind of implemented out of five that I have written.  I'm **not really pushing very hard for them to be included given the amount of things that are already in**. Basically at the moment and I don't have a lot to show to chester some implementation to do.

**Danno**: Do you need a cargo space in next hard fork specially reserved for  state and stuff?

**Alexey**: Not sure. I think I want to first finish the fourth version of the State rent proposal which is basically depend on how the data from the stateless client is going to go. Because this is what further drives more changes in it. I don't think you need to reserve something yet. Potentially, it will go to the next. We don't know when the next one's going to be either. 

**Tim**: Yeah that sounds like a good topic for the next call. Okay and so 5 from state rents.


### ProgPow

**Tim**: The next big one was ProgPOW. Hudson being away, I pinged him and Charles he's also been working out on the audit and they wanted to discuss the idea of including ProgPOW in Istanbul with the condition that if something negative comes out of the audit, we pull it out. So they were both curious about people's thoughts on that.  

**Martin**: Is it not something that we decided already? 

**Tim**: Yeah it seems like this conversation seems to be rehashed over and over, as to make it a final call on this.

**Danno**: So, a few core dev calls ago I raised **a chain halting attack that could be done at 1/3rd power**. I posted something on Eth magicians on the discussion thread I haven't heard back from anyone on that. That's one of the things that I put into, to have the auditors look at and that's something I'm actually concerned about because we implemented it as is without change. There are some mitigations, we can do. That's why we hope to get the audit back before we fully commit to it to see if we need to do any of these mitigations.  I am very skeptical it's going to come back with the audit with a zero mitigations.

**James**: Either way, don't we wait till the audit?


**Tim**: So if we wait till the audit to implement, this very likely means that it won't be ready for Istanbul.

**Danno**: Will it be in poll results today?

**Tim**: Does anyone feel like we should go ahead and Implement ProgPOW tentatively and then pull it out to the last minute if there is an issue in the audit? Otherwise we can have the ProgPOW for the next hardfork. It's obviously still assuming that the audit come back positive. 

**Danno**: Is the last moment before we do a  test network or before we do a mainnet fork? 

**Martin**: Yeah I think it would be, I mean if we go ahead with ProgPOW which I think we should, I do a think, it's better to have it safe then very late.

**Tim**: Quickly for context, **the dates that was set for the test Network upgrades is August 14th**, so this is less then a month from now. 

**Danno**: So I do think that ProgPOW should go in I am skeptical that it would be irresponsible to do it in Istanbul without the audit findings.  If we let the fork into the testnet, that will permanently got it coated in. So if we're going to put up in last minute and it be testnet and then I'm concerned you're going to put flag to fork or not fork,  I think we're adding unnecessary complexity plus I still would like to get feedback on my concern about the mitigation of the chain attack.I would even support an out of cycles fork, for the record. 

**Tim**: So just because we're coming up on an hour and a half do we have the consensus on what to do with ProgPOW? It seems that Martin you're thinking we should go ahead and implement it. 

**Martin**: Actually, I agree. I was trying to push this earlier, out of the cycle fork for ProgPOW. So if other people are also involve with that, that would be a good choice.

**Tim**: So meaning, we wait for the audit, based on that, assuming it's positive we then scheduled a hard fork for ProgPOW. Is that correct?

**Danno**: Basically that yes. And I think we make a lot of other people happy to  have a **single-purpose hardfork** as well **on ProgPOW**, it is so contentious.

**Tim**: I guess that's the other question about this  Does it risks splitting the network? Is it contentious enough? Is that something that we've time to discuss right now?

**Alexey**: And also I would say that this problem of precommiting  to the testnet was also very troublesome. When once something is done in the Ropsten, it has to be included in the mainnet. 

**Martin**: Yeah but that thing will go away at some point from Ropsten ?

**Tim**: So reading that chat here  does it makes sense to leave ProgPOW out for this fork. Based on potentially having a future fork specifically for ProgPOW? Is this something we have consensus on does anyone feel strongly we should push for ProgPOW for Istanbul?

**Danno**: I feel strongly that we should push it out of Istanbul but I'm Not Over My Dead Body if other people want to push for it.  But my preference is out of Istanbul?

**Tim**: Does anyone disagree with that?

**Danno**: Out of the Istanbul and the hardfork as soon as the audit is ready.

**Tim**: So, **out of the Istanbul and the hardfork as soon as the audit is ready**.  I think we'll probably need a discussion about whether or not this is a special single EIP a hard fork or not. 

So we're at an hour and a half we've made it basically through on the agenda. To be mindful of people's time is there anything else especially related to Istanbul that someone wants to discuss that he feels very important we talk about now otherwise I don't think we have time to address any of the other items on the agenda in any reasonable way, unless people want to stay longer.



### Others

**Danno**: I motion **we do some out of cycle All Core Dev calls** leading to the testnetwork.

**Tim**: Would anyone oppose to the next core dev's call next week rather than two weeks from now, if that's the case.

**Danno**: We need to haggle over time. We keep the same schedule so whenever the next rotation should be, we do that.

**Louis**: Just a quick question what is the core center around ? Like so bright nights to its 2:30 am. Where I am going to be next week? 

**Danno**: The original time which would be 4 in the afternoon Berlin time.


**Alexey**: It's going to be 2 p.m. UTC, I think.

**Tim**: Do we have a consensus to have the next call next week probably along with two weeks from now and we can review the agenda but probably mostly pick up from where we left off this one?

**All**: Agreed.

**Alex B**: What are the **discussion topics next week**?

**Tim**: We had on the agenda today on some concerns around EIP refactoring. So given that there are some dependencies between some of the EIPs for Istanbul, trying to sort that out, conformance testing. So I assume this is around testnet and stuff like that. Then next week we also have follow-ups on 1344 which we talked about and 2200 and then potentially 1962 as well. As well as any other EIP that needs to be discussed for Istanbul. Potentially, we still have time talking about special fork for ProgPOW would look like?


**Bryant**: For 1344 I am on the call to talk about it. It seems like we're closing the meeting here. I don't know what was discussed about today?

**Tim**: So there was some concern about weather the chain ID should be in the transaction or in the block? I think that was the biggest convention point. We agreed to take that conversation offline. Still keep this as a consideration for Istanbul considering how simple of a change it is, but just sorth this issue out.

**Bryant**: If the issue sorted then acceptance?

**Tim**:  I guess yeah, lets have that conversation on the next call but it seem to be the big issue.


**Martin**: Just a quick one, the security considerations is also a very short one but we can also do this in the next week.

**Tim**: Very shorts mean like one minute or 15 minutes?

**Martin**: I would say like 2 minutes it's just about adding a mandatory security considerations section to the EIP requiring to be filled out. This intention of being very relax so that we can slow start being more security into the process and that's what it is meant to be. At some point it will be filled up like guideline and that currently we are gathering some information about that. So that will also be someone of us at the meet up in Montreal in a few days. Maybe how to get more Security in such a similar process. Just something to mention P P & R C or AFT section and we're following the same thing that they are doing right now.

**Tim**: My only comment will be, we probably don't want this to be a consideration for any of the current EIPs for Istanbul. Right now we don't want to have this extra stuff and stuff that's already moved along. 


**Martin**: yeah that's the idea.

**Tim**: Anyone have comments on this? Okay great. So we'll see you all next Friday at 14 UTC. Thanks everybody.





***Rest of agenda topics couldn't be covered*.**



## Everything else gets pushed from Istanbul?


##  Update EIP-1679: Istanbul Meta



# 2. EIP Refactoring

## Given EIP-1702: Which of the Istanbul EIPs live only in version 1 code? Which live in version 0 and version 1 code?

[sorpaas](https://github.com/ethereum/pm/issues/111#issuecomment-512971466): Regarding this, in the call we'll basically want to discuss two options:

1. Treat old versions as "immutable" -- define a new version each time we do a hard fork. This will be really good to ensure backward compatibility. And because older versions are not changed, clients may be able to make more assumption of the versions to simplify the design. The drawback is that we'll get 2 new versions per year.
2. Treat versions the same as how we do semantic versioning. Deploy a new version when a feature qualify as a "major release", and only change existing versions when a feature is "minor release" or "patch release". I'm okay with this, but I have worries about all the gas reduction EIPs for Istanbul -- I cannot convince myself that they won't have backward compatibility issues.

If we decide on (2), then we may not have a new version this time, because most Istanbul EIPs (except EIP-615 and state rents) are minor changes. However, I do want to propose that we ensure account versioning is implemented in all the clients and include it in Istanbul testing, because it allows people to write EIPs with the assumptions that we have account versioning, which in many situations will greatly simplify things (for example, state rent EIPs' new account RLP fields).

## Proactive refactoring of the client implementations to make EIPs more simple, and reduce their conflicts.

# 3. Conformance Testing
# 4. Review previous decisions made and action items
# 5. Adding "Security Considerations" to EIP-1
# 6. [Working Group Updates](https://eth.wiki/eth1)
# 7. Testing Updates
# 8. Client Updates 
# 9. EWASM & Research Updates (only if they are posted in the comments below)



# Date for Next Meeting: 
Friday 26 July 1400 UTC. 


# Attendees
* Adrian Sutton
* Alex Beregszaszi
* Alex Vlasov
* Alex G
* Alexey Akhunov
* Bryant Eisenbach
* Casey Detrio
* Danno Ferrin
* James H.
* Lane Rettig
* Louis Guthmann
* Martin Holst Swende
* Martin Ortner
* Nick
* Paweł Bylica
* Pooja Ranjan
* Tim Beiko
* Trenton Van Epps
* Wei Tang


## Links shared in the call 

* https://docs.google.com/spreadsheets/d/1Mgo7mJ6b6wimUwafsMo1l-b44uec28E_Hq8EQ7YdeEM/edit#gid=0
