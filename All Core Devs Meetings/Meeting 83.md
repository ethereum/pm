# Ethereum Core Devs Meeting 83 Notes
### Meeting Date/Time: Friday 20 March 2020, 14:00 UTC
### Meeting Duration: 1 hr 43 mins
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/159)
### [Video of the meeting](https://www.youtube.com/watch?v=vDGj660uZE0&feature=youtu.be)
### Moderator: Hudson Jameson
### Notes: Sachin Mittal

----
	
# Summary
    
## EIP Status 
| Status | EIP |
|-------|----------|
| Discussed under EFI. Discussion to be continued in EthMagician thread | EIP- 2537, EIP-1962|
| Under review for EFI. Decision required around needing a Hard Fork | EIP-2315, 2515 |
| Eligible for Inclusion Pending. | EIP-2456 |


## Decision Items

**Decision Item 83.1:** Yes, on the proposal of fuzzing testing by Alexey

**Decision Item 83.2:** Work required on EIP2542, to include only one of the three opcodes proposed

## Action Items

**Action Item 83.1:** A bounty for the pre-requisite benchmarking required for EIP2046 (Hudson)

# 1. [Eligibility for Inclusion (EFI) EIP Review](https://eips.ethereum.org/EIPS/eip-2378)

**Hudson:** James, Should we start with the EIP Reviews?

## EIP - 2537
**James:** - Let's quickly review the berlin one's first. EIP-1962 was superseded by EIP-2537, the single BLS curve one. It seems like 2537 is basically final now. Alex V, can you give us a quick update?

**Alex V:** Specs are frozen, the last part that was missing was ABI update and gas schedule. 

**James:** Any updates on Hash to curve?

**Alex V:** The PR was updated with some information. So, hash to curve: there are two parts, One is hashing to the filled element which can be done in EVM. And this part has more than one choice, i.e. you can use different has functions if you want. So, we won't implement this in pre-compile. We will just leave it as a functionality in pre-compile. Just 20 lines of code.

* Second part is the mapping with the filled element, into the curve point which is non-trivial and expensive. And this is specified  as a pre-compile. 

**Hudson:** Great, thank you! This is the needed for phase 0 of eth 2.0 right?

**Alex V:** To my understanding, this is necessary to check BLS curve, because it is necessary to hash it as a curve point. 

**Vitalik:** This isn't strictly necessary for the Eth2 Phase 0, but it would allow Eth2 light clients on the Eth1 chain, which is a "very nice to have". Both BLS curves, BLS12-381, and hash to curve. It will also enable rollups that uses eth 2.0 as a data source. 

## EIP - 2515, 2315

**James:** Great, other one is EIP - 2515, Difficulty bomb freeze. I will get back after working on suggested changes by the community. 

* EIP-2315, quick updates? Last time we talked, vyper was gonna look into it. 

**Martin:** Yeah, its a thumbs up from Vyper. Also My take on this is, it is implemented as mentioned in EIP. you can generate traces, and test cases while running but I propose a small change.

**Greg:** Getting it implemented is the step, you need for people to look at it carefully. 

* EIP-2315 has some discussion on the eth magician [link](https://ethereum-magicians.org/t/eip-2315-simple-subroutines-for-the-evm/3941). This has been implemented in geth. Still some minor improvements to be made. You can follow that discussion on the @EthMagicians link above

# EIP - 2456

**James:** This seems to be making progress. Sounds good. EIP 2456 - Time based upgrade. I have some updates on this. 

* There were some concerns about uncles. @jasoncarver had some suggestions for improvements [link](https://ethereum-magicians.org/t/eip-2456-time-based-upgrade-transitions/3902/12).

**Vitalik:** One issue with the EIP seems that it would require including 1024 blocks in the state vs. the current 256 that are currently stored. We can't use 0 blocks (no lookback), because you could have an uncle with a lower block height but a higher timestamp, which could cause issues. If you change back the limit from 1024 to 256, there will be no issues. 

**James:** Yeah, and apparently it affected beam sync, and other things. During our discussion, jason preferred having "zero" lookback. But then you said 256 is our storage memory so...

**Alexey:** What I didn't understood is that, it is true that "1024" is just a magical number, but earlier when I read the EIP, I was wondering if it is to avoid two blocks having same timestamp.

**Vitalik:** It is illegal for two blocks to have the same timestamp.

**Alexey:** Then what is the problem?

**Martin:** So if you don't have a lookback. You may run into a problem like, it may include a uncle that has a previous number but has a later timestamp. That can later harrass the situation. 

**Jason:** I think the best way forward is a pure timestamp-based forking, and instead of having a lookback, we make uncle timestamp rules stricter. So far, it's only happened a few times that uncles were ahead of their canonical blocks. Needs more analysis.

* It's important that we are able to look at a single block header and know which rules applies to that block / which fork it is on.

* More discussion by Jason, James and Martin from (18:30   - 23:30) on the call.  Eth Magicians [link](https://ethereum-magicians.org/t/eip-2456-time-based-upgrade-transitions/3902/12)


**Hudson:** I am going to timebox this subdicussion since there are more things to discuss. Also, an ETA on Berlin hard fork timing?

**JHancock:** We probably don't need to discuss this now. We can wait to get more testing done on the BLS precompile.

## EIP-1962 fuzzing

**Alexey:** Even though this won't go into Berlin, it's worth pursuing it. We have good docs, 3 different implementations, and some fuzz testing. I have been reading about fuzzing which microsoft implements, and it has great results. 

* Our current process follows manual testing, personal inspection which misses on very important points. And there are certain assumptions around an idea, which we avoid touching. And this excludes very interesting and non-trivial changes, like this one. This one is definitely a complex change.

* If we employ some optimation here, it will reduce some cognitive requirement. And I am hoping that, we will get more confident about such changes. 

* Better automation of testing for EIPs like these (in this case, white-box fuzzing), which are very complex could make us more comfortable with them and reduce the need for expert analysis. There are more details on the call about how they are fuzzing 1962.

* One challenge with this is that fuzzing basically generates random data, most of which are just invalid inputs and only trigger the validation parts of the code vs. the arithmetics. They are iterating on it to generate valid inputs so that all the code is tested.

* So giulio, can explain what we have been doing instead. 

**Giulio:** Instead of generating a completely random piece of data, as the fuzzing is right now. We are creating random data, that actually has a meaning. 

**Alex Vlasov:** This seems like a valid approach, and can be used to test BLS12-381 precompile. 

* FYI, current fuzzing test code, it compiles the pre-compiles with a special feature which disable most of the checks. 

**Alexey:** I agree, it's a valid approach but it is not complete. So, we need three kinds of testing.

* First is the one you described, differential testing between implementation. 
* Second, We also need to test the validation, with checks enabled. 
* Third, what we are trying to do is testing algebraic properties of the arithmetic. So, we are making sure that we are generating the points properly in the domain to check arithmetic is performing perfectly.

**Ratan:** So, if you are doing more specific one that checks to make sure that all the properties are conserved then doesn't it include the arithmetic from completely random point. 

**ALex Vlasov:** Well, atleast for BLS12-381 implementation which I have made as next layer on top of EIP 1962 code. There are already test for basic arithmetic. 

* I did it manually, but if such a tooling is there, it will be a great addition. 

**Alexey:** To me, it's like an independent review. 

**Martin:** Yeah, we need that. 

**Alexey:** So, I wanted to get a general agreement of what we are doing is good?

**Martin:** So, we don't know that yet. But seeing it implement will give us more idea. 

**Alexey:** My idea was to use fuzzing on general library, and then drill down to specific curves. When we are confident enough, that we are doing goodjob on generalised curves. We will jump on specific curves. 

**Ratan:** So, which fuzzing test are we talking about using?

**Giulio:** We are gonna use black-box testing but current EIPs uses H-fuzz.

**Alexey:** I am sensing a general positive attitude towards our work?

**Hudson:** Yes, fuzz testing is not a expertise. And since people don't about it you won't find any criticism now yet though. 

**James:** I think we can leave EIP 1962 as an EFI, and not supercede it with the work happening. 

**Martin:** But it's not an EFI.

**Alexey:** I don't it matters at this point, but it has further application than BLS12-381 curve. It has a lot of potential for inclusion. For ethereum to be inclusive of other applications. Also, wanted to know if it's a good direction to go?

**Hudson:** So not as an official EFI. But just for sense of direction. Sure, Go Ahead!!


### EIP 2542

This EIP is for adding the following OPCodes

1.  Transaction Gas Limit
2.  Call Gas Limit
3.  Transaction gas refund

-  **Alex**: Current Situation in EVM 

   -  There is an OPCode for gas limit that returns block gas limit and not a transaction/call gas limit
   -  Out of all the parameters a transaction has, only gas limit is not available for a smart contract to use - which creates some limitations
      -  eg., how much gas the transacation uses - currently a workaround is implemented in code, which is not accurate

-  **Question**: How is this information useful?

   -  Book keeping - in terms of meta transactions, where a record is to be maintained for transactions with the gas used and refunded. 

-  **Cross Question**: Why not operation Gas instead?

   -  eg., in a public function taking `bytearray` variable, you'll never be able to know for sure how much gas was spent on `calldata`, and `calldata load` operations

-  **Cross Question**: You'll never be able to trust the Gas limit in a way because there are other things before they called your OPCode

   -  Right, and that is why the proposal is of a gas limit of the entire transaction and the current call frame
   -  Happy to receive any input on the implementation

-  **Feedback (reaction)**: a previous UNGAS proposal, proposed to completely hide this information from the EVM. Having worked with gas limits, realised that introspection tools of the EVM in terms of gas, or the ability of a smart contract to observe the internals of the EVM looks like a cool feature, but inevitably leads to the call that will be broken when we try to do anything with the gas schedules. In the same way, there is an opinion that the Chain ID OPCode might actually be bad, because it allows contracts to introspect the chain id and they start building the code assuming the chain id and basically that code becomes unforkable.

-  **Comment on the previous feedback**: Gas abstraction is actually a leaky abstraction. It is inherently impossible to entirely hide everything related to Gas from the EVM because after all, we can check the balance and figure out the fees of the transaction, and figure out the gas used from the transaction even if we had the UNGAS proposal.  Essentially, we need to preserve the backward compatibility. Biggest offender is the Gas parameter in all these call uncles. If we don't do UNGAS, and do a part of what the UNGAS proposes, should be sufficient. And if entirely hiding the gas information from the EVM is impossible then introducing something above the gas limit is a possible way to go.

-  **Comment on the proposed OPCode - Call Gas Limit**: 

   -  Recommended to be specified more clearly
   -  The issue in its entirety is quite complex
   -  No implementation/concept of gas limit of current execution field
   -  It is possible to implement this OPCode in different ways with different values to give the same results - therefore useful to be more detailed
   -  How exactly should the EVM extract this Call Gas Limit information

-  **Comment on the proposed OPCode - Tx Gas Refund**:

   -  Issues in implementation - gas used implementation is lock based, and implemented differently in different Ethereum implementations
   -  This particular OPCode can have different meanings in different contexts 

-  **James**: Two general schools of thought amongst developers:

   -  ETH1.x  working on removing abstraction and favouring proposals like UNGAS
   -  The meta transaction community working on proposals on how to make it easier to deal with gas.
   -  Would be interesting for these two ideations to merge

-  **Question**: What is the actual real world use case of these OPCodes? Apart from theoretical use cases pertaining to smart contracts.

   -  Possible use case:
      -  Permit functions in DAI contract. 
         -  Allow people to pay for gas in DAI, without holding any Ether using a Relayer
         -  Relayer receives compensation and pays for Eth
         -  Important to know in a transaction, how much gas does the transaction cost
         -  There are two parts to a transaction
            -  the original transaction user wanted to execute
            -  wrapped by the relay contract
         -  Currently, an approximation is made on how much the transaction actually costs
         -  With the proposed OPCode in place, this scenario would be ZeroSum, where everyone gets and pays for the exact amount of gas
      -  A singleton contract on a network and any EOA address can make a transaction to it, with a meta tx as a param, and be sure that the address will get the money of making this call. 
         -  Core concept here being: no trust between caller and the contract. 
         -  Contract needs to be "aware" of the gas limit.

-  **Feedback**: The given use case (`permit` function in DAI contract) is just a mechanism, and there exist such mechanisms in other scenarios (generalised as 'Meta Transactions'). Maybe it is better to take this automation out of the smart contract and be applied at the server where the transaction is sent. Applying most of the automation inside the smart contract is not the best way to move forward.

-  **Feedback**: If it were implemented, these would be brittle solutions. There are workarounds, eg, setting out storage slots and be paid later for these storage slots and either paid/refunded based on the storage slot and the successful transaction - these are tricks but makes the whole thing implementable instead of increasing complexity.

-  **Follow up feedback on the previous one**: Not that the proposed OPCodes are useless, but these involve quite a high effort cost to implement. These instructions - specifically the last two (Call gas limit and Transaction gas refund), are described in the yellow paper but they are not accessible from the EVM atm. So if we want to modify the EVM we can do it, because we know they are inaccessible, however if we have those OPCodes in place, it will be hard for us to do something about refunds - like change the logic. It is like putting shackles on our future ability to fix certain things in the EVM. 

-  **Critique** for Transaction Gas Limit OPCode: 

   -  Similar to Origin OPCode
   -  Snd Origin is something that probably should never have been implemented
   -  It has 99% use cases that are bad
   -  Reliability on it is for the wrong reasons
   -  The transaction generator is controlling that number
   -  An OPCode is probably not even required

-  **Comment** and refutal of previous critique: 

   -  If I want to delegate my transaction to another contract, then I want to give them the approval along with enforcing them to not use gas more than a certain amount
   -  Approval can be made currently but I, as a user, cannot enforce the fact that, "this delegated transaction must not cost me more than $0.5"
   -  And that isn't solvable without an OPCode

-  **Decision**: 

   -  Most important and easiest to implement is Transaction Gas Limit OPCode
   -  Inherent difficulty in implementing the other two OPCodes

-  **Final Comments/Questions**

   -  Missing security considerations
   -  Make the EIP well formed
   -  Alex requests for collaborations on this EIP to refine it, best way to reach out via email
   -  **Question**: is GSN possible in UNGAS scenario?
      -  Not sure about that, but seems like not.



Heading over to Item 5 from the EFI EIP Review list from the agenda - others are pre-EIP proposals

### EIP 2046

Proposed by **Alex Beregszaszi**

Proposes reduced gas cost (from 700 to 40) for static calls (`staticcall`) made to precompiled contracts

-  Pushed forward by @shamantar. 
-  **Alex**
   -  Tested the cost of invocation of precompiles on OpenEthereum ([link](https://github.com/ethereum/pm/issues/159#issuecomment-601655408))
   -  The number given for reduction is reasonable
   -  Should be eligible for inclusion and checks can be made on current precompile call gas limits in BLAKE2b
   -  Suggests that this change would help alot, as set against reasons of *not* including this
      -  eg., in scenarios which include hashing, invokes the keccak function quite alot of times
      -  eg., application involving mathematics - alot of float additions or multiplications involve payment of huge price penalty
   -  Measurements and testing have already been done on this
-  **Louis** agrees with the proposed reasons of inclusions
   -  BLAKE2b function should and must be faster and cheaper than keccak, and its not, only because its a precompile call
   -  Cannot be used apart from very specific use cases eg., verifying PoW.
-  **Clarifying question** (Hudson): Current benchmarking being done eg., for the BLS curves are potentially mispriced because of the fact that a constant 700 gas cost is taken into account for all precompiles?
   -  No. Actually, the way benchmarks are implemented is that the raw data is used without giving attention to this precompile cost because it is inherent to the EVM.
   -  Possibly, all precompile calls are priced in this way, including BLS
   -  Usually, the cost of the precompile should not, and does not include 700 in any form
   -  Therefore, its just the benchmarking and gas price of the current precompiles, and the execution time for a given input - like what is the cost of the execution time
   -  Usually, when you call them, you are paying 700 gas for nothing
-  **Martin**
   -  Agrees, in theory for the cost being too much.
   -  Not agreeing, to the fact that the cost is factored in the precompiles
   -  The precompiles were priced after an analysis, where 700 was thought to be 'good enough'
   -  And if a change is made to this value, all the calculation needs to be redone, to make sure the loss in margin doesn't hamper anything at a later stage.
   -  Not opposing the proposal, but the work is required to be put in for this analysis
   -  We need to show the numbers
-  **Alex**, in reply to the cost factoring in precompile call
   -  There was a recent reduction of price for BM Curve and the benchmarks from there.
   -  Used the same kind of benchmark to measure EIP 1962, BLS 12321, and those did not include 700 gas depend
   -  So the prices there are pure execution time
-  **Louis**, adding a question to the ongoing discussion
   -  to understand what exactly to benchmark:  what is the upper limit to block execution time today
      -  [Martin] ~200 ms
   -  Can we use a full block executing just the precompile as a way to price it? (for benchmarking)
-  **Alex** explains his method of benchmarking as a simple recipe to try out
   -  Take any Ethereum implementation (eg., Geth)
   -  Try on your own machine to run benchmarks for `ecrecover` and some other precompiles (like addition, multiplication). This way, we get some numbers on how much gas has been paid per second of execution time on your machine
   -  My machine ranges from 22 to 40 - i estimate as 35
   -  And thats how I priced EIP 1962
-  **Martin** mentions the process is motivated from `ethereum/benchmarking` repository
-  **James** giving context, 
   -  The conceptualisation of this EIP came up in Istanbul
   -  Everyone was supportive that a lower value was infact much needed
   -  But the work involved in figuring out the actual number was something pending even then, and still is
   -  Shaving off a random number isn't enough
   -  if Louis or Alex agree to put in the work, this part can be completed.
-  **Hudson** suggests,
   -  Putting together a bounty to try and get some accurate benchmarking for this. Either publicising on Twitter or using platforms like Gitcoin.
   -  Continuation of this conversation offline.
-  Another mention for EIP1962
   -  is an EFI, because it was tentatively accepted in meeting #66, before the concept of EFI was born.

### Other pre-EIP proposals

Five pre-EIPs to go through. 

All five proposed by **John Adler**, these are:

1. Transaction `postdata` (EIP 2242): A new field in transactions that cannot be read by the EVM
2. Execution over transaction postdata with precompiles - enabling multi-threaded data availability processing
3. New precompiles for Merklization and Merkle branch verification
4. Calldata gas cost reduction to 1-2 gas per byte
5. Current transaction-hash opcode - enabling further cost reduction for optimistic rollups

The intention of proposing the above EIPs in the call was to get a high level opinion if these EIPs are even worth pursuing. If there is a strong opposition or not.

High-level motivation for the above EIPs:

-  To make rollups both optimistic and zk variety have access to more data, and other helpful features
-  Generally, in a rollup construction, requirement is to have a bunch of transaction data posted on-chain as `calldata`, and an authenticated commitment to this data - happening on-chain. So two possibilities are: a simple hash, or merklizing it. Additionally, for fraud proofs in optimistic roll-ups, requirement is to do a merkle branch verification.
-  So, note that, computing authenticated commitment and doing things like verifying a merkle branch, are `pure` functions - do not write/read from the state. Since they are `pure` they can be **multithreaded**
-  Imagine a situation where a huge amount of transaction volume is moved to a roll-up, then parallely 4 nodes could create authenticated commitment in that block

Request for questions/crtiques on the proposals:

-  **karalabe**
   -  Curious about the implication of the proposals: the net total effect it would have on the chain is that we would have certain transactions that are huge in size (eg., 5mb/size). Implying we could end up with a 5mb "valid" block
      -  **James**: Yes, that is correct. Additionally, there might be a simultaneous increase in max block size. Not necessary though
   -  This does have a few practical implementations in terms of data storage. Particularly, 5mb block size might have significant issues. The Ethereum networking protocol might not be able to propagate that. If 5mb blocks were to be produced one after the other, the network might quickly choke. Which is something that needs to be thought upon.
      Other issue, having a 5mb blocks would permit the Ethereum chain in itself to grow by ~28Gb per day, which is quite a big number. Currently all the headers, receipts included are 127Gb for the best four years, and the proposal in question would allow to create about 25% of that, per day. So essentially, an year's worth of growth, created per day.
      -  **James**: That is correct. Hard drives are actually cheap. 50 bucks per 1TB. Comes out to a couple of dollars or in some cases, under a dollar per day worth of storage costs. 
      -  **Follow-up Question**: So, if I have 8,000 nodes in the network, I have $8,000 cummulative cost for the network. Current cost (without chain pruning) is like $ 100 for 100 days.
-  **James**
   -  Acknowledges the fact that few things from very different contexts have been brought up in the ongoing conversation, like, storage cost, how to improve the network layer to support this
   -  Suggests John to explain the concepts in a blog post eg., what is a roll up, and about the EIPs, the security considerations, the technical specifications
      -  idea is to boil down all the concepts in a "bloggable" post
      -  that would help the dev community to look at the proposal in a holistic perspective
      -  and would better be able to respond on parts of the proposal pertaining to different aspects and their implications (eg., network layer, storage layer, etc) 
-  **Alexey**
   -  Adding to the suggestion:
      -  The proposal does in fact expands to the demands on the Ethereum network and we are not sure what the implications might be
      -  prerequisites for that, therefore would be, to improve our status quo on the storage structure
      -  eg., working rigourously on chain pruning
      -  roll-ups is quite promising, but would like to see more investment in the infrastructure as well. to avoid having a top-heavy system, where loads of applications are trying to build on top of it but the infrastructure is unable to support any of it.
-  **Louis**
   -  there is no consensus as of now on what are the exact technical requirements and the tecnical cost of running a node over time
   -  and all improvements proposed here, depend directly on the cost of running an infrastructure
   -  so, defining the cost to run a node in ethereum network needs to be defined prior to work on this (very interesting) EIP can be started
   -  additionally, (to be taken offline), how this EIP is does help optimistic roll-ups. And, for multi-threaded processing, we're again making assumptions on the kind machines we expect the nodes to run
-  **Alex**
   -  Wouldnt a better and more usable solution be not just copy all the calldata to memory but instead map it to some chunks of memory and not pay for this allocation. so you can read it from the memory
      -  **James**: That is a good suggestion. But, the main motivation of having such data that is untouched by the EVM was to have that data, do a bunch of computation and completely evict it from memory. For things like doing pre-process transactions that have post data, and eventually discard the post-data from RAM
-  **James**
   -  suggestion to look into Stateless Ethereum
-  **Final comments**:
   -  karalube suggests looking into chain pruning, but taking care that pruning might render certain contract that depend upon logs and past events dead (eg., Augur). It is a great initiative, but likely breaks something.

## Attendees

Abdelhamid Bakhta

Alexey 

Alex Bereg. (axic)

Alex Forshtat

Alex Vlasov

Daniel Ellison

Giulio

Greg Colvin

Gullaume

Hudson Jameson

Ian Norde

James Hancock

Jason Carver

John Adler

Karim Tam

Karalabe

Louis

Mariano Conti

Martin Holst Swende

Pawel Bylica 

Pooja Ranjan

Ratan

Tim Beiko

Trenton Van Epps

Wei Tang


## Annotations from Zoom chat

Tracking EFI: https://github.com/orgs/ethereum/projects/5

EIP 2515: https://ethereum-magicians.org/t/eip-2515-replace-the-difficulty-bomb-with-a-difficulty-freeze/3995

EIP 2456: https://github.com/shemnon/EIPs/blob/d771a0d82de6975bdd0b395b35fa6675fcb0fade/EIPS/eip-2456.md

https://twitter.com/GuidoVranken/status/1236666223880024065?s=20

Tim: It is EFI: https://eips.ethereum.org/EIPS/eip-2378

Hudson: Can someone (maybe a cat herder on the call) look up the notes for 1962 in the PM repo and see when it went into EFI? I can't find it: https://github.com/ethereum/pm/search?p=1&q=1962&unscoped_q=1962

James H. https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2074.md should be this call

Tim: It was “tentatively accepted” last summer and got moved to EFI with all the others when we moved them all across https://github.com/ethereum/pm/blob/d7295a2ef399b28334ea73a3912bb6f220fcf6fd/All%20Core%20Devs%20Meetings/Meeting%2066.md

Pooja R. Entered EFI in Meetin #78 https://github.com/ethereum/pm/blob/650d4dd250fe60319f6a7ec7969e503cf55a6dd8/All%20Core%20Devs%20Meetings/Meeting%2078.md

Trent: Sharing the ETHGlobal Ethereum Developer Survey >> https://ethglobal.typeform.com/to/RxHlK8
Please share your perspectives if you have a few minutes, will be very helpful 

Alex F.: forshtat1@gmail.com

EIP 2046: https://eips.ethereum.org/EIPS/eip-2046

Pooja: FYI: DECISIONS 81.4: There is no way can to confirm the EIP 1962 is going in, clients have serious concerns implementing. They may coordinate something in ETH Paris.

Hudson: Interesting. It is in EFI so at some point we did grandfather it in it seems.

James: IT was grandafathered in before that point

Pooja: It is ‘under discussion’

Hudson: And 1962 was discussed in Paris as part of the group doing the BLS-sig curves I think under discussion doesn't preclude EFI. I could be wrong.

James: This is the meeting we moved tentatively accepted into EFI The BLS discussion happened much later

Hudson: Ah I see!

James: Last call we discussed supersceding 1962 with the BLS precompile Now with Alexeys work, I would motion to leave it in EFI, and not supersede 1962
As his work starts general and then would address specific precompiles

James: My suggestion at least.

Tim: +1 to that FYI John, our team has worked on pruning for Besu. Happy to chat with you about our approach.

Louis: John, I would be very interested to discuss directly
