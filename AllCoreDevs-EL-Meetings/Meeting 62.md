# Ethereum Core Devs Meeting 62 Notes
### Meeting Date/Time: Friday, May 24, 2019 14:00 UTC
### Meeting Duration: ~1.5 hrs
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/99)
### [Audio/Video of the meeting](https://youtu.be/lF_XxqxgVuA)
### Moderator: Hudson Jameson 

# Summary

### DECISIONS MADE

None

### ACTIONS REQUIRED

**ACTION 62.1:** Reach out to the Authors of EIP-615 to discuss the questions around the EIP especially the option of splitting the EIP into smaller more digestable components and try make a decision.

**ACTION 62.2:** Have an indepth discussion on how EIP-663 can be improved.

**ACTION 62.3:** Perform a full benchmark for EIP-1108.

**ACTION 62.4:** Discussion required with Jordi Baylina and Alex Bergszaszi around the options between EIP-1109 and EIP-2046.

**ACTION 62.5:** James Hancock to update the [Wiki](https://en.ethereum.wiki/roadmap/istanbul) and Meta [EIP-1962](https://eips.ethereum.org/EIPS/eip-1679) with decisions around the EIPs.

**ACTION 62.6:** EIP-1283 requires a new EIP number and a section discussing the difference between the original EIP-1283 which was removed from Constantinople and this new EIP.

**ACTION 62.7:** Engage with Ronan Sandford and Bryant Eisenbach to discuss which EIP; EIP-1344, EIP-1959 or EIP-1965 should be implemented.

**ACTION 62.8:** EIP-1352 needs more work done to answer the questions posed by the All Core Devs.

**ACTION 62.9:** EIP-2045 needs further discussion.

**ACTION 62.10:** EIP-2024 discussion required between James Prestwich, Casey Detrio and Zachary Williamson.

**ACTION 61.1**: [Ganache/spec compliance issue at go-ethereum](https://github.com/ethereum/pm/issues/97#issuecomment-489660359)
**Status**: Will look at this in the next meeting.

**ACTION 58.1**: Cat Herders to look at updating EIP1. 
**Status**: [PR-1991](https://github.com/ethereum/EIPs/pull/1991) to be merged.

# 1. [Review previous decisions made and action items](https://github.com/ethereum/pm/blob/master/AllCoreDevs-Meetings/Meeting%2061.md#summary) 
[Timestamp: 1:47](https://youtu.be/lF_XxqxgVuA?t=107)

## Actions: 

**ACTION 61.1**: [Ganache/spec compliance issue at go-ethereum](https://github.com/ethereum/pm/issues/97#issuecomment-489660359)
**Status**: Will look at this in the [next meeting](https://github.com/ethereum/pm/issues/102).

**ACTION 60.1**: Review timeframe for hardforks in June to refresh memories.
**Status**: Completed as per Roadmap [below](https://github.com/ethereum/pm/blob/master/AllCoreDevs-Meetings/Meeting%2062.md#2-roadmap).

**ACTION 60.2**: Danno Ferrin to add 9 month out Hardfork kickoff to [timeframes](https://ethereum-magicians.org/t/more-frequent-smaller-hardforks-vs-less-frequent-larger-ones/2929/28).
**Status**: Completed

**ACTION 60.6**:  Martin Holste Swende and Alex Beregszaszi to confirm whether [EIP 689](https://eips.ethereum.org/EIPS/eip-689) needs to be implemented.
**Status**: Completed. Exists in Clients and is in tests as it has already been accepted but is not in the yellow paper. No one available to write it into the Yellow Paper.

**Action 60.7**: Parity to comment on Libraries for [Precompiles](https://github.com/ethereum/pm/issues/95#issuecomment-486879991)
**Status**: Complete. Parity has no objection to using shared libraries for the precompiles. NOTE: There is an acknowledgement of a loss of some benefits of multiple implementations.

**ACTION 58.1**: Cat Herders to look at updating EIP1. 
**Status**: [PR-1991](https://github.com/ethereum/EIPs/pull/1991) has been approved by 2 or 3 EIP reviewers but has yet to be merged. Once merged it will be complete.

**DECISION 61.3**: Confirmation that EIPS still in draft form but submitted before the EIP acceptance hard deadline of the 17th May 2019 have been accepted for review to be included in the implementation into Istanbul.

# 2. [Roadmap](https://en.ethereum.wiki/roadmap/istanbul)

[Timestamp 10:13](https://youtu.be/lF_XxqxgVuA?t=613)

**Hudson:** NOTE: Soft deadline for client implementations is the 19th July 2019.

**Hudson:** NOTE: Hardfork is happening after DevCon5 projected date: 16 October 2019.

**Hudson:** Rough plan is next hardfork take place in April 2020, see link in heading above.

# 3. [EIPS](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1679.md) for Istanbul:

[Timestamp 13:23](https://youtu.be/lF_XxqxgVuA?t=803)

## 3.1 [EIP-615](https://eips.ethereum.org/EIPS/eip-615): Subroutines and Static Jumps for the EVM

[Timestamp 13:41](https://youtu.be/lF_XxqxgVuA?t=841)

### STATUS: UNDECIDED

**Martin Holst Swende:** Objection raised as per the reasons in the [Magicians discussion](https://ethereum-magicians.org/t/eip-615-subroutines-and-static-jumps-for-the-evm/2728). The complexity is too great for the benefits given.

**Hudson:** There is also an argument that this EIP should be split up into multiple EIPs.

**Hudson:** Process question: Should the EIP Champion be on the call for the EIP to be approved?

**Martin Holst Swende:** Approvals do not require the EIP Champion to be on the call but we cannot decline the EIP unless someone from the EIP is on the call to defend their EIP.

**Rick Dudley:** Don't think we should make a decision on this now but to respect process the champion should be on the call to discuss their EIP.

**Zachary Williamson:** Can't speak to the complexity of the EIP as it is ambitious in scope. One the biggest issues at the moment is the difficulty in writing efficient smart contracts and write efficient EVM code. Having some abstractions in particular with subroutine calls and particularly local variables would go enormously towards bridging the gap towards what you can do on the EVM and what you end up doing practically. Rule of thumb writing EVM code is 30x more efficient that writing it in solidity. This is primarily due to the complexity of the stack inspection. This could potentially having established languages complied to EVM code. This does solve some serious problems and would be quite a win if this EIP was in the standard from the developer perspective.

**Paweł Bylica:** If we improve the EVM over time that would be the right direction to go. Agree with the idea of splitting this EIP. There are proposals on how to do this on the practical level. There are two small features from the EIP that can be implemented up front. Agree with Martin versioning, I am not sure about deploying this before we can verify a deploy time. I also however have concerns about versioning implemented if it is never used in the future if this EIP will be delayed or for other reasons.

**Danno Ferrin:** There are EIPs with proposed opcodes so a versioning EIP would be useful.

**Alex Bergszaszi:** We could also remove core code if versioning is enabled.

**Martin Holst Swende:** Agree, versioning is a pretty strong construct and could stand on its own, even if EIP-615 is not implemented in the end. Note there are two types of versioning. One is a versioning where the contract says I want to play by these new cool rules cause of these new cool opcodes. The other type of versioning which is basically for Ewasm and EIP-615 is a version stamp where by the EVM says yes this contract has gone through the scrutiny and is certified to not do illegal jobs. What ever versioning protocol we have it should have opt in versioning and seal of approval type of versioning.

**Hudson Jameson:** Looks like this EIP will need to be split and as a result will not be implemented in Istanbul but will instead have elements of these split EIPs implemented in April's Hard Fork.

**Péter Szilágyi:** EIP says that one of the benefits is performance. Do we know what performance improvements there are, can we have some numbers around this?

**Paweł Bylica:** Not aware of any numbers. There is not actively managed implementation of this but we could do a side implementation to get some numbers.

**Péter Szilágyi:** People are weary of the size of the EIP but if we can demonstrate via some numbers that it is good then we may be more willing to accept it.

**Martin Holst Swende:** From discussions the raw speed improvements is not the primary reason for this EIP.

**Danno Ferrin:** Primary benefit would be the ease of mapping stuff to Wasm.

**Péter Szilágyi:** Accept these benefits but then lets perhaps get rid of the performance argument from the EIP.

** **
**ACTION 62.1:** Reach out to the Authors of EIP-615 via the All Core Devs Gitter Channel and Magicians Discussion to discuss the questions around the EIP especially the option of splitting the EIP into smaller more digestable components and try make a decision.
** **

## 3.2 [EIP-663](https://eips.ethereum.org/EIPS/eip-663): Unlimited SWAP and DUP instructions

[Timestamp 29:00](https://youtu.be/lF_XxqxgVuA?t=1740)

### STATUS: UNDECIDED

**Alex Bergszaszi** Potentially one of the ways to split up EIP-615.

**Martin Holst Swende:** What are the benefits of this EIP?

**Alex Bergszaszi** Solving a similar problem that EIP-615 is solving with subroutines. In EIP-615 subroutines you would be able to access multiple stack items and they achieve that by introducing the get local. You would have two ways to access items from the stack and that means you will beable to access 16 items from the stack without moving items back and forth to memory. EIP-663 extends the stack access to be able to access more than 16 items. This should be well discussed. I don't think that this EIP in its current form should be accepted. Perhaps some limitations should be put in and some considerations should be made so that this can be a precursor to EIP-615. The main benefit for accessing more stack items would be making it similar for compilers such as Solidity to support bigger functions where people can experience issues for example like messages from the compiler stack to deep where they use to many variables or variables in input arguments. The only solution that developers have currently is to split those up into multiple functions.

**Martin Holst Swende:** Are SWAP and DUP 2 byte constructions like the Push.1? 

**Alex Bergszaszi** There are three options listed in the EIP. One is having an immediate value whikst another requires a push upfront.

**Péter Szilágyi:** Pricing wise how does this arbitary duplication compare to memory accesses? Why is doing DUP better than pushing it into a memory slot?

**Alex Bergszaszi** It is cheaper because you don't pay for the number slots in the stack but you do pay for memory extension.

**Danno Ferrin:** It is also stack based which is good for recursive calls.

**Péter Szilágyi:** Our stack limit is currently 1k. I am unclear as to why we have limited these items to only 16 words. We are storing the whole thing in memory anyway. We don't have any specialised CPUs for Ethereum that could benefit from having this 16 word limit. I would suggest that removing this limit would be a good extension even if it is not too valuable. It just seems like an arbitary chosen limit that does not make sense.

**Martin Holst Swende:** It makes sense from the perspective that there are a limited number of pulls on the push instructions have data sections. If we do option A then it screws a bit with dump test analysis.

**Alex Bergszaszi:** Option A should only be introduced with account versioning or EVM versioning.

** **
**ACTION 62.2:** Have an indepth discussion on how EIP-663 can be improved.
** **

## 3.3 [EIP-1057](https://eips.ethereum.org/EIPS/eip-1057): ProgPoW, a Programmatic Proof-of-Work

[Timestamp 38:31](https://youtu.be/lF_XxqxgVuA?t=2311)

### STATUS: UNDECIDED

EIP is still pending audit, above and beyond standard security considerations, that should be evaluated prior to inclusion.

**Hudson Jameson:** As mentioned in Twitter, Gitter and Ethereum Magicians, the original hardware auditor is no longer able to do the audit anymore. We have in the meantime found another hardware auditor who has no conflict of interest. This however means that the chances of the entire audit (software and hardware) being completed before Istanbul is now very unlikely, which ultimately means that EIP-1057 will not be implemented in Istanbul. If this changes between now and the next All Core Dev meeting then we will change this advice however the likelihood that this EIP will now form part of the April Hard Fork is very high.

**Danno Ferrin** As Champion for the EIP I would not recommend the current EIP go forward until there is a change and I will be recommending that the audit look at this and recommend this change before I would be comfortable with letting this EIP go forward. I will detail this in the Ethereum Magicians discussion.

## 3.4 [EIP-1108](https://eips.ethereum.org/EIPS/eip-1108): Reduce alt_bn128 precompile gas costs

[Timestamp 44:13](https://youtu.be/lF_XxqxgVuA?t=2653)

### STATUS: UNDECIDED

**Zachary Williamson:** At the moment the precompile gas schedule is quite a strong bottleneck to deploying more advanced privacy mechanisms. This EIP will would significantly reduce gas fees. The implementation work for this EIP should also be extremely light.

**Martin Holst Swende:** From the benchmarkings of the 211 Beta Release the benchmarks after the pairing optimisations you are listing the same test vectors and I am curious for the second benchmarks did you take the exact same ones or did you take the ones that performed the worst?

**Zachary Williamson:** Took a clone of the same benchmarks.

**Martin Holst Swende:** Would be interesting to run the benchmarks for the full set.

**Zachary Williamson:** Happy to do that and update them. 

**James Prestwich:** The reason they were priced so high in the first place was to prevent DOS attacks for a relatively new onchain primitive. We have no evidence that DOS attacks are forthcoming. The actual compute time costs of these are much lower than the gas costs would imply. A lot of developers are excited about these judging from discussion and hackathons. We have a lot of reasons to stop pricing them high and a lot more reasons to start pricing them more reasonably.

**Martin Holst Swende:** If we can make these cheaper then we definitely should. We went to a lot of trouble to put them in and if no one is using them then it is wasted effort. It is extremely easy to just lower the price. We just need to ensure we are not opening ourselves up to DOS attacks.

**Hudson Jameson:** EIP-1108 is approved in principle, pending a benchmark which will be reviewed at the next meeting.

** **
**ACTION 62.3:** Perform a full benchmark for EIP-1108.
** **

## 3.5 [EIP-1109](https://eips.ethereum.org/EIPS/eip-1109): PRECOMPILEDCALL opcode (Remove CALL costs for precompiled contracts)

requirement of EIP-1962

[Timestamp 51:54](https://youtu.be/lF_XxqxgVuA?t=3114)

### STATUS: UNDECIDED

**Alex Bergszaszi** Initially this proposal was very different. It was about changing the existing calls to behave differently if they are targeting a precompile. But that was changed into proposing a specific opcode but due to Jordi not responding for a couple of months I created a new EIP-2046 which is doing the original proposal only changing STATICCALL to behave differently.

**Péter Szilágyi:** Prefer to make the original proposal as well. Much better to make the original calls smarter than introduce a new opcode that does almost the exact same thing.

**Hudson Jameson:** We will discuss this and if Jordi does not provide any feedback we will go with EIP-2046.

** **
**ACTION 62.4:** Discussion required with Jordi Baylina and Alex Bergszaszi around the options between EIP-1109 and EIP-2046.
** **

** **
**ACTION 62.5:** James Hancock to update the [Wiki](https://en.ethereum.wiki/roadmap/istanbul) and Meta [EIP-1962](https://eips.ethereum.org/EIPS/eip-1679) with decisions around the EIPs.
** **

## 3.6 [EIP-1283](https://eips.ethereum.org/EIPS/eip-1283): Net gas metering for SSTORE without dirty maps
[Timestamp 55:57](https://youtu.be/lF_XxqxgVuA?t=3357)

### STATUS: UNDECIDED

**Péter Szilágyi:** This was the same EIP we removed from Constantinople. Not sure what the difference is between this one and the one we removed.

**Alex Bergszaszi** There is no difference. Want this together with account versioning and only enable the change on accounts that follow the newer version.

** **
**ACTION 62.6:** EIP-1283 requires a new EIP number and a section discussing the difference between the original EIP-1283 which was removed from Constantinople and this new EIP.
** ** 

## 3.7 [EIP-1344](https://eips.ethereum.org/EIPS/eip-1344): Add ChainID opcode
[Timestamp 1:00:00](https://youtu.be/lF_XxqxgVuA?t=3600)

### STATUS: ACCEPT

**Martin Holst Swende:** Believe someone has filed a competing EIP.

**Alex Beregszaszi:** EIP-1959 and EIP-1965.

** **
**ACTION 62.7:** Engage with Ronan Sandford and Bryant Eisenbach to discuss which EIP; EIP-1344, EIP-1959 or EIP-1965 should be implemented.
** ** 

## 3.8 [EIP-1352](https://eips.ethereum.org/EIPS/eip-1352): Specify restricted address range for precompiles/system contracts
[Timestamp 1:08:14](https://youtu.be/lF_XxqxgVuA?t=4094)

### STATUS: UNDECIDED

**Alex Beregszaszi:** May not require a hardfork. Should just be accepted and made final. Tests may need to be added to the test suite?

**Danno Ferrin:** How does this affect EVM runtime?

**Alex Beregszaszi:** It should not.

**Jason Carver:** Was there any intention on refusing contract creation through these addresses?

**Martin Holst Swende:** In private networks at genesis you create contract controlling services. This EIP needs to explain to clients how we manage these?

**Alex Beregszaszi:** It is a prerequisite to several EIPs which don't want to list every single precompile when making precompiles cheaper.

**Martin Holst Swende:** If there is an existing network that has EVM code on these services what will happen to those future EIPs which lower the cost of the precompile calls, how should they handle that? 

**Péter Szilágyi:** Geth has a list of precompiles and the hardcoded addresses. In my opinion if you want to make precompiles "free" when calling them then they should not rely on the address but should rely on how the chain is configured. If the chain lists 8 free precompiles then those 8 get the free waver and the rest of the precompiles have to pay. In my opinion that would be the logical behaviour.

**Martin Holst Swende:** Agreed.

** **
**ACTION 62.8:** EIP-1352 needs further discussion to answer the questions posed by the All Core Devs.
** ** 

## 3.9 [EIP-1380](https://eips.ethereum.org/EIPS/eip-1380): Reduced gas cost for call to self

### STATUS: DID NOT REVIEW

## 3.10 [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559): Fee market change for ETH 1.0 chain
[Timestamp 1:13:19](https://youtu.be/lF_XxqxgVuA?t=4399)

### STATUS: UNDECIDED

**Rick Dudley:** Very unlikely to make it into Istanbul. 

**Péter Szilágyi:** Please provide further detail in the EIP on how this change affects networking for example transaction propogation. The transaction pool logic is heavily tied into how miners accept different transactions and if we start changing that logic then maybe the network layers also requires some patches.

**Rick Dudley:** Please raise this as an issue and we will look to address this in the EIP.

## 3.11 [EIP-1965](https://eips.ethereum.org/EIPS/eip-1965): Method to check if a chainID is valid at a specific block number

[Timestamp 1:00:00](https://youtu.be/lF_XxqxgVuA?t=3600)

### STATUS: UNDECIDED

**Danno Ferrin:** Same as EIP-1959 - except this is a precompile whilst EIP-1965 is an opcode. I would advocate for the precompile to save opcode space. The choice is really between EIP-1965 and EIP-1344. Believe both can go in independently of each other.

See EIP-1344 notes above.

## 3.12 [EIP-1702](https://eips.ethereum.org/EIPS/eip-1702): Generalized account versioning scheme

### STATUS: DID NOT REVIEW

## 3.13 [EIP-1706](https://eips.ethereum.org/EIPS/eip-1706): Disable SSTORE with gasleft lower than call stipend

### STATUS: DID NOT REVIEW

## 3.14 [EIP-1803](https://eips.ethereum.org/EIPS/eip-1803): Rename opcodes for clarity

### STATUS: DID NOT REVIEW

## 3.15 [EIP-1829](https://eips.ethereum.org/EIPS/eip-1829): Precompile for Elliptic Curve Linear Combinations

### STATUS: DID NOT REVIEW

## 3.16 [EIP-1884](https://eips.ethereum.org/EIPS/eip-1884): Repricing for trie-size-dependent opcodes

### STATUS: DID NOT REVIEW

## 3.17 [EIP-1930](https://eips.ethereum.org/EIPS/eip-1930): CALLs with strict gas semantic. Revert if not enough gas available.

### STATUS: DID NOT REVIEW

## 3.18 [EIP-1985](https://eips.ethereum.org/EIPS/eip-1985): Sane limits for certain EVM parameters

### STATUS: DID NOT REVIEW

## 3.19 [EIP-1959](https://eips.ethereum.org/EIPS/eip-1959): New Opcode to check if a chainID is part of the history of chainIDs

[Timestamp 1:00:00](https://youtu.be/lF_XxqxgVuA?t=3600)

### STATUS: UNDECIDED

See EIP-1344 notes above.

## 3.20 [EIP-1962](https://eips.ethereum.org/EIPS/eip-1962): EC arithmetic and pairings with runtime definitions
replaces EIP-1829


## 3.21 [EIP-2014](https://eips.ethereum.org/EIPS/eip-2014): Extended State Oracle

[Timestamp 1:23:10](https://youtu.be/lF_XxqxgVuA?t=4988)

## 3.22 [EIP-2026](https://eips.ethereum.org/EIPS/eip-2026): State Rent H - Fixed Prepayment for accounts

### STATUS: DID NOT REVIEW

## 3.23 [EIP-2027](https://eips.ethereum.org/EIPS/eip-2027): State Rent C - Net contract size accounting

### STATUS: DID NOT REVIEW

## 3.24 [EIP-2028](https://eips.ethereum.org/EIPS/eip-2028): Calldata gas cost reduction

### STATUS: DID NOT REVIEW

## 3.25 [EIP-2029](https://eips.ethereum.org/EIPS/eip-2029): State Rent A - State counters contract requirement of EIP-2031

### STATUS: DID NOT REVIEW

## 3.26 [EIP-203](https://eips.ethereum.org/EIPS/eip-203)1: State Rent B - Net transaction counter

### STATUS: DID NOT REVIEW

## 3.27 [EIP-2035](https://eips.ethereum.org/EIPS/eip-2035): Stateless Clients - Repricing SLOAD and SSTORE to pay for block proofs

### STATUS: DID NOT REVIEW

## 3.28 [EIP-2045](https://eips.ethereum.org/EIPS/eip-2045): Fractional gas costs, and the EVM benchmarks referenced within (cdetrio)
[Timestamp 1:15:33](https://youtu.be/lF_XxqxgVuA?t=4533)

### STATUS: UNDECIDED

**Casey Detrio:** Gas prices are balancing three seperate items: disk I/O, network I/O and computate. Currently disk I/O is overutilised and is the bottleneck in the network and network I/O and compuate are underutilised because they are overpriced.

There is the EIP that will reduce the price of call data which will help underutilised network I/O. There is an EIP to increase the price of SLOAD which will help rebalance disk I/O. There is an EIP to increase the price of SSTORE and CREATE2 etc. and that makes it possible to boost the block gas limit while maintaining the same rate of state growth.

If we boost the gas limit while similtaneously increasing the price of state growth that is effectively the same as keeping the gas limit the same but reducing the price of all other operations for the non-state expanding operations; computation and network I/O, which is reading the price of transaction data and calldata. How much we can reduce the price of transaction data depends on when bandwidth becomes the bottleneck. How much we reduce the price of computation depends on when computational opcodes become the bottleneck. So currently computational opcodes are not the bottleneck even in unoptimised clients.

Martin Swende's recent benchmarks showed that `SLOAD` is the major bottleneck and so the EIP to increase the price of `SLOAD` proposes taking it from a gas cost of 200 to a gas cost of 800. Even after that 4x increase in the cost of `SLOAD` it would still be the bottleneck according the Martin's benchmarks. Note that these benchmarks were done on Geth. So just using the speed of computation on Geth the benchmark shows that either the cost of disk I/O needs to be raised substantially or the cost of computation should be reduced. OR a combination of both. Because the costs are all relative. So reducing one is the same as raising the other.

What is crazy is that if you benchmark Geth against an EVM implementation that is optimised for compuational speed like EVM1 which is what we did and the graphs of those are linked in the agenda and in the EIP. They show that we can get a 10x speedup just from optimising the EVM. So the proof of concept the fast EVM implementation that does this is called [`evmone`](https://github.com/chfast/evmone) written by Paweł. 

There are two signicant speed ups from the low hanging fruit right now. The first is just the rebalancing the cost to the current Geth and Parity speeds. And then the second speed up is optimising Geth and Parity to get the same speed up as evmone or you can just use evmone.

The thing to try is to take evmone and benchmark some of the most optimised EVM contracts. We did this with the contract that Zach Williamson wrote called Weierstrudel. It implements ECMUL which has the eliptical curve multiplication (the precompile that was out at Byzantium) and it beat the precompile in gas costs. In computation time evmone executes ECMUL in 500 micro seconds and that is compared to native rust which Parity uses for their precompile which executes in 300 microseconds and Geth is more optimised which it's native Go in assembly runs in 100 microseconds. The fact that the EVM bytecode does the same thing as a native precompile in 500 microseconds compared to 300 or 100 microseconds - I think those results are pretty shocking.

That optimised interpreter, executing optimised bytecode can achieve speed not a lot slower. I would almost say it is near native. And even that result of 500 microseconds is not the best we can do. There is more optimisations remaining there. A well known one for elipical curve is Montgomery multiplication. That was not done on Weierstrudel because it was optimised for gas costs and not speed and the price of MUL vs MODMUL is not really accurate to the runtime. The more optimised Weierstrudel may be even faster if we were to benchmark it. Although it would cost more gas due to the gas right now.

**Casey Detrio:** Those benchmarks for Weierstrudel, they could be optimised to make them even faster?

**Zachary Williamson:** Yes it could. Montgomery multiplication may speed it up by a factor of 2. 

**Casey Detrio:** Conclusion: there is room for substantially reducing the gas costs of computation and we need fractional opcode pricing so that it is below the current limit of 1 unit gas.

** **
**ACTION 62.9:** EIP-2045 needs further discussion.
** ** 

## 3.29 [EIP-2046](https://eips.ethereum.org/EIPS/eip-2046): Reduced gas cost for static calls made to precompiles
[Timestamp 51:54](https://youtu.be/lF_XxqxgVuA?t=3114)

### STATUS: UNDECIDED

See EIP-1109 notes above.

## 3.30 [EIP-2024](https://github.com/ethereum/EIPs/pull/2024/files): Proposal for supporting Blake2b
[Timestamp 1:23:08](https://youtu.be/lF_XxqxgVuA?t=4988)

### STATUS: UNDECIDED

**James Prestwich:** Ethereum supports SHA-2 and Keccak-256. The ZCash Foundation and the IPFS team work with different hash functions like Blake2 and it would be nice to have access to these on chain.

Some benefits include Equihash evaluation efficiency. At the moment it takes 16 million gas to evaluate one equihash at low security parameters. High security parameters would require 32 or 64 million gas.

I have a use can today that I could implement with just the Blake2 precompile.

**Casey Detrio:** The benchmarks I just referred to - there is even a more optimised Blake2b byte code that Zach did that resulted in a significant gas cost reduction. When you benchmark it in evmone and a best EVM implementation it would be plenty cheap enough without a precompile.

**James Prestwich:** The thing is with Equihash is that you have to do 32 invocations. So even if you reduce it by an order of magnitude you are still looking at 1.6 million gas per invocation. In order to verify that ZCash header is for example you would need to do somewhere in the order of 30-40 invocations depending on how much security you want.

**Casey Detrio:** The reduction is more than an order of magnitude. 

**James Prestwich:** How much are we talking about onchain gas costs today?

**Zachary Williamson:** Happy to share the source code with you. But basically it is about 30x less.

**Casey Detrio:** Then you get a 10x on top of that because of the optimised EVM.

**James Prestwich:** Does anyone use an optimised gas cost EVM in production?

**Casey Detrio:** That is what the proposal is. Reprice the gas costs so that we don't need more precompiles. 

**James Prestwich:** For those hoping to implement things this EIP is essential. Without it we are left stranded potentially for a year.

**Martin Holst Swende:** Use cases?

**James Prestwich:** Tokenized assets and using IPFS you can do a lot more verification of off chain data using Blake2. You can also use it for Decred cross chain inter-operability. Blake2 is uncommon but normal hash function. 

**Martin Holst Swende:** We have had for a long time BTC Relay where we do cross chain swaps with Bitcoin. 

**James Prestwich:** I have written a few articles on the lack of use of BTC Relay. One of the really cool things where this differs from BTC relay is that the ZCash team is considering Flight Clients Merkle Mountain Range commitments for their next hard fork which will be about 6 months from now. So getting in a Blake2 precompile into Ethereum on a slightly longer timeframe would allow you to do not only a ZCash relay which would be prohibitively expensive but the ideal minimal flight client relay which is orders of magnitude more efficient than relaying every header. So this is really a unique opportunity here because the ZCash team is looking at hardforking for features specifically to this as well.

**Péter Szilágyi:** EIP-2045 seems like it may be almost impossible to implement as it would require everyone to use a specific optimised version of the EVM. EIP-2024 seems trivial to implement and Blake2 is a fairly popular Hash function. It is implemented in almost every single language out there. So integrating that would be perhaps 30 minutes worth of work. So if there is a specific use case then adding a precompile like this seems a no brainer.

**Casey Detrio:** Does this include Blake2s? 

**James Prestwich:** No

**Péter Szilágyi:** We could make a list of hash functions we would like to see implemented and go from there as they would probably take the same amount of effort. Testing may require more effort but it is not really an effort to supprt new hash functions.

** **
**ACTION 62.10:** EIP-2024 discussion required between James Prestwich, Casey Detrio and Zachary Williamson.
** ** 

# Date for next meeting
June 21, 2019 at 14:00 UTC (postponed two weeks due to Scaling Ethereum event, and to allow time to asynchronously discuss EIPs proposed for Istanbul)

# Attendees
* Alex Beregszaszi
* Alex Stokes
* Bradley Miller
* Brett Robertson
* Casey Detrio
* Daniel Ellison
* Danno Ferrin
* Danny Ryan
* David Murdoch
* James Prestwich
* James Hancock
* Jason Carver
* Lane Rettig
* Martin Holst Swende
* Matt Garnett
* Paweł Bylica
* Phil Lucsok
* Péter Szilágyi
* Pooja Ranjan
* Rick Dudley
* Tim Beiko
* Zachary Williamson
* Zak Cole
