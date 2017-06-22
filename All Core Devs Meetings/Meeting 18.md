# All Core Devs Meeting 18
### Meeting Date/Time: Friday 6/16/17 at 14:00 UTC
### Meeting Duration 1.5 hours
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=8jWhPylWros)
# Agenda


#### Metropolis updates/EIPs.

**[[5:10](https://youtu.be/8jWhPylWros?t=310)] a. Any "subtleties" or questions we need to work out.**

1. [[1:10:16](https://youtu.be/8jWhPylWros?t=4216)] [EIP 206 REVERT Opcode : The "Specification" section in the EIP does not specify that REVERT can return data to the caller. Neither does it specify how the caller can access the returned data.](https://github.com/ethereum/EIPs/pull/206#issuecomment-308324622) [Yoichi]
2. [[6:32](https://youtu.be/8jWhPylWros?t=392)] [EIP 208 Abstraction of transaction origin and signature: Atomicity over an ECDSA's accounts operations](https://github.com/ethereum/EIPs/pull/208#issuecomment-307681408) [Jeff Coleman]
3. [[29:54](https://youtu.be/8jWhPylWros?t=1794)] EIP 208: ethereum/EIPs#208 Concerns [Martin H.S]
    
    i. A transaction hash no longer uniquely identifies an execution, since a transaction at least theoretically can be included in multiple blocks, or multiple times in a block.
    
    ii. Do we need to modify RPC-call which assumes hash = unique execution, to return a list of transactions instead of a single element?
    
    iii. What side-effects does the breaking of this invariant have on the clients?
4. [[44:20](https://youtu.be/8jWhPylWros?t=2660)] [EIP 211 RETURNDATACOPY and RETURNDATASIZE: This is complete right?](https://github.com/ethereum/EIPs/pull/211) [Hudson]

5. [[46:43](https://youtu.be/8jWhPylWros?t=2803)] [EIP 213 zk-SNARK verification primitives: Gas costs for additional and mult. on EC](https://github.com/ethereum/EIPs/pull/213#issuecomment-305423098) [Christian or someone]

6. [[57:05](https://youtu.be/8jWhPylWros?t=3425)] [EIP 214 STATICCALL: Various potential errors](https://github.com/ethereum/EIPs/pull/214#issuecomment-306800891) [Vitalik]

**b. Updates to testing.**
- [[55:38-57:04](https://youtu.be/8jWhPylWros?t=3338)] & [[59:08](https://youtu.be/8jWhPylWros?t=3548)] Documentation and other updates

**c. Details and implementations of EIPs.**
  
- [[1:02:05](https://youtu.be/8jWhPylWros?t=3725)] Updates from client teams.
    - geth - https://github.com/ethereum/go-ethereum/pull/14337
    - Parity - https://github.com/paritytech/parity/issues/4833
    - cpp-ethereum - https://github.com/ethereum/cpp-ethereum/issues/4050
    - yellowpaper -  https://github.com/ethereum/yellowpaper/issues/229
    - pyethapp
    - Other clients
    
**d. [[1:08:38](https://youtu.be/8jWhPylWros?t=4118)] Review time estimate for testing/release.**

#### Other Topics
- [[1:11:323](https://youtu.be/8jWhPylWros?t=4283)] [EIP 156: Reclaiming stuck ether](https://github.com/ethereum/EIPs/issues/156) [Vlad Z.]
- [[1:18:13](https://youtu.be/8jWhPylWros?t=4693)] Address calculation changes post-Metropolis [Christian]

# Notes

## a. Any "subtleties" or questions we need to work out.

### 1. [EIP 206 REVERT Opcode : The "Specification" section in the EIP does not specify that REVERT can return data to the caller. Neither does it specify how the caller can access the returned data.](https://github.com/ethereum/EIPs/pull/206#issuecomment-308324622) [Yoichi]
Yoichi: One sentence is missing from EIP specification. I will work with Alex B. to fix that.

### 2. [EIP 208 Abstraction of transaction origin and signature: Atomicity over an ECDSA's accounts operations](https://github.com/ethereum/EIPs/pull/208#issuecomment-307681408) [Jeff Coleman]
Jeff: Do we expect everyone to move over to contract based ECDSA accounts? Otherwise we need to deal with the atomicity issue.
Vitalik: I think we should move people over to it eventually, but do it carefully and slowly over time.
Vitalik: Long term: I think every account should eventually be contract based to make the protocol less complex.
Vitalik: Main issue you raised is that it will break `tx.origin`.
Jeff: You asked about a solid use case, and currently `tx.origin` is the only way to attribute the difference between who published a response in a state channel and who signed a response. Since we expect there to be third party tx transaction publishing services for state channels it is important.
Vitalik: Why do we need to know who published it?
Jeff: To pay rewards and bounties for people who publish tx's while you are offline and so you can differentiate between a publicly claimed bounty vs something that is coming in through a forwarding contract. `tx.origin` is the only way to validate this.
Vitalik: 2 things we can do. Do nothing and let the opcode deprecate itself or do a change where if `tx.sender` is a null sender then we switch the exit origin to be the tx.to account. I am happy with both methods and if we decide there is enough value with it I am fine doing this.
Robert: Setting it to the `to` account isn't quite enough if you have contracts that manage multiple accounts, verifying other signature schemes. Rather you can have the contract set `tx.origin` as it prefers as long as it is the first call in the chain to do that.
Vitalik: If the goal you are trying to meet is to have generic contracts to verify signature algos, you want a different mechanism.

Discussion continues between multiple people until [29:53](https://youtu.be/8jWhPylWros?t=1793). We tabled this item for the time being in order to move onto other agenda items during the call and the conversations continue on. It will likely be brought up in a future meeting. Please view the EIP for more details.

### 3. EIP 208: ethereum/EIPs#208 Concerns [Martin H.S]
Martin H.S: Curious about side effects of a transaction being included in multiple blocks, or multiple times in a block.
Vlad Z.: Example of side effect?
Martin H.S: RPC interface would need to be changed to handle this. Also how tx's are stored internally within clients and how we have designed the data structures to assume 1 tx has 1 receipt can cause inconsistencies. Other RPC methods can be affected as well.
Christian: This is not relevant for the hard fork itself because the feature won't be active, right? We won't activate these types of transactions at the hard fork, only later.
Martin H.S: They will?
Vitalik: There is a possibility that a malicious miner will include 5 copies of the same tx. That is a good argument to not care about interfaces accessing multiple transactions very convenient. We can have users needing to access this to build their own systems to manage this.
Nick: Are there straightforward changes we can make to restore the invariant of unique tx's?
Vitalik: It would create unending state bloat. We could have tx deadlines, but that would have a substantial state load and an in-state garbage collection mechanism.
Nick: Depends on how we do it. The simplest way to reinstate nonces as the one required part of a transaction and the sig verification is up to you. Or have a more generalized block scheme where tx's are restricted to apply some transformation nonce.
Vitalik: In the long term there are legitimate uses for making anti-reply completely over realized, or even just accepting the same hunk of data multiple times. Example: If you have some particular thing that needs to get poked, the tx that pokes it should be a minimal thing with no sig. It would be added complexity for something like that to require nonces. I'd also say there will be benefits to eventually moving the protocol to this regime where transactions are if tx's are correctly formatted they are valid no matter what. This less us do weird stuff like agreeing on blocks and state roots out of order.
Nick: I agree nonces are suboptimal. Sometimes you want ordering and sometimes you don't. I worry this may be a more pervasive invariant than we think.
Vlad Z.: Maybe we can rely on logs for that?
Vitalik: In general we should be relying more on logs for things.
Nick: Yes, but transactions are still a fundamental component of the system. Where do we stand on transaction pruning(or timing?). I remember use discussing before that with the new system you can no longer rely on true transactions being executed in the same order because miners can exclude certain tx's and your code can reject it.
Vitalik: One thing you can do is, for regular users, they can use a whitelisted account with a nonce scheme. If miners process tx's out of order you can tell.
Nick: Issue is you can't queue up 5 tx's before sending them and the miners can keep including them out of order.
Vitalik: Including a transaction out of order is equivalent to a no-op except for wasting gas.
Nick: That's bad because a no-op can force me to waste gas arbitrarily.
Vitalik: Miner's can already waste their own gas arbitrarily. The mechanism that pays for gas does not auto-deduct from your balance. If your tx gets included out of order, it gets included, then hits an error and reverts. It reverts the transactions including the user gas.
Nick: I'm still in a position where I can't reliable queue stuff up or have to remain online.
Vitalik: I fail to see why the ability to include no-op transactions make this any better.
Nick: Before I could queue up 5 tx's and be sure they make it into the chain.
Conversation goes on until [44:00](https://youtu.be/8jWhPylWros?t=2640) and the conversation will continue on the EIP with Martin H.S summarizing the issue in the EIP.

### 4. [EIP 211 RETURNDATACOPY and RETURNDATASIZE: This is complete right?](https://github.com/ethereum/EIPs/pull/211) [Hudson]
Hudson: Is this good to go? Can I merge the PR and finalize?
Vitalik: Did we agree on what to do with data that goes beyond boundaries. Is it 0's or a throw?
Hudson: We are going with the throwing approach.
Vitalik: Sounds good.
Vitalik: Another clarification: does the return data get reset by a CALLCODE, DELEGATECALL, or STATICCALL, but not CREATE because they have no return data.
Christian: It is reset every time a new stack frame is created.
Yoichi: It includes CREATE because it returns data when it fails.
Vitalik: Sounds good.
Hudson: Great. Christian is this done?
Christian: Yeah it can be merged.

### 5. [EIP 213 zk-SNARK verification primitives: Gas costs for additional and mult. on EC](https://github.com/ethereum/EIPs/pull/213#issuecomment-305423098) [Christian or someone]
Hudson: How are we deciding gas costs?

Summary: To decide on gas costs we need to run benchmarks on the gas per second values across all major clients and collect them in a document. We will be working on this in the core developers channel and potentially the testing channel.

### 6. [EIP 214 STATICCALL: Various potential errors](https://github.com/ethereum/EIPs/pull/214#issuecomment-306800891) [Vitalik]
Vitalik: Neither of these seems controversial, but some minor errors from outdated opcodes in the EIP. Also a sentence that references a DELEGATECALL non-zero value which would never exists. Another line says "its values are always copied to sub call or sub-create", but there is no such thing as a sub call in a STATIC call. No major changes, just minor fixes.
Christian: I will look at the context and make changes.

## b. Updates to testing: Documentation and other updates
Yoichi: I joined the testing team many months ago and ran into issues so I am creating a guide for testeth. Documentation is in review stage. Also am changing testeth so it causes errors when incorrect commands happen.
Dimitry: I created a docker image of testeth so new contributors can use the docker images instead of building clients and compilers for test generation. I am making newer documentation for using testest.
Martin H.S: Any estimate on how much metro. test coverage we have?
Dimitry: I can give a rough estimate. 55%
Martin: Okay.
Hudson: I just posted [a documentation summary document that acts as a getting started guide for helping to test Metropolis](https://www.reddit.com/r/ethereum/comments/6hnej0/update_metropolis_qatesting_guide/).

## c. Details and implementations of EIPs.


### Updates from client teams.
#### geth - https://github.com/ethereum/go-ethereum/pull/14337
Peter: Discussion with Jeff yesterday. Most of the EIPs are done. Pull request has details. One EIP that was missed that I am going to work on is EIP 96, the block hash stuff. Jeff is also still tweaking EIP 86 regarding CREATE. Other than this, Felix wants to revamp internal testing system. In theory it is mostly done, in practice we will see after the test.

#### Parity - https://github.com/paritytech/parity/issues/4833
Arkadiy: We completed the implementation a while ago, but we have made small tweaks the past few weeks. We are waiting on the tests.
Robert: For MODEXP there's new gas cost calculations, but there may be more updates to them soon.

#### cpp-ethereum - https://github.com/ethereum/cpp-ethereum/issues/4050
Andrei: During last 2 weeks we merged blockhash implementation and all the pre-compiles. Some minor fixes on other EIPs. What's left is CREATE2 Opcode support.

#### yellowpaper -  https://github.com/ethereum/yellowpaper/issues/229
Yoichi: It is finished, but the main focus right now is how to get spurious dragon changes.

#### pyethapp
Hudson: Jan had to drop off it seems, Vitalik can you update?
Vitalik: We don't have a PR with a list like the others, but I can list some of what I know is implemented. All precompiles, STATICCALL, REVERT, RETURNDATA (without change for out of bounds stuff), EIP 86, and REVERT. Not done: EIP 96, 98. Basically all the ones that deal with transactions until we have tests for them.
Hudson: Are you primary or Jan?
Vitalik: I've been primary on EIPs.

#### Other clients
No other clients were present for the meeting. etherumJ appears to be abandoned and no changes have happened in the repos in months.

## d. [[1:08:38](https://youtu.be/8jWhPylWros?t=4118)] Review time estimate for testing/release.
Hudson: Last time estimate we had was between August and September for testing/release period. Anyone have a comment on if this should be changed?
No comments.
Hudson: Sounds like we may know more next meeting as we get new testers onboarded.
Yoichi: I'm excited to see the contributors joining, however, the first few weeks will be slow due to onboarding the new people, but it will be faster in the long run after the initial slowdown.
Hudson: I agree, we can also have the new people help update documentation with their issues they ran into.

## Other Topics
https://youtu.be/8jWhPylWros?t=4283

### [EIP 156: Reclaiming stuck ether](https://github.com/ethereum/EIPs/issues/156) [Vlad Z.]
Vlad Z.: I want to be caught up on any conversations regarding EIP 156 about stuck funds.
Hudson: That was brought up by a group of exchanges and interested parties recently in a Skype chat who asked for advice on how to get this done. I let them know the process about making an EIP, getting community support, formalizing the EIP, getting developer buy in, etc. It appears the conclusion they came to (they will need to answer for themselves) is that they don't want to pursue that EIP right now because it would be too controversial and at this point we have locked down the metropolis EIPs, not enough time to test and figuring out a process of who qualifies for getting stuck ether returned. Vitalik any updates on your end since it is your EIP?
Vitalik: The challenge is with Quadriga's situation is that EIP 156 works well when an entire class of situations where you have an account where money is not accessible and second where you can identify a party that money reasonably belongs to. One very natural case is if money goes into an empty contract, sending the money to a creator is not that bad to do. Challenge with Quadriga case is that it is stuck in a splitter contract. We can mathematically reason and show that the money is stuck, but it's much harder to turn that into a principled rule that would make sense at a protocol level. The other thing is identifying who sent the money and who to refund it to. In general, I would avoid making contorted rules that apply to one specific case because those kinds of things set bad precedents and should only be done in the most extreme situations. If you can come up with a class of users, like when a few thousand people lost money in the same way and we have a clear, unambiguous way to figure out who a reasonable owner is.
Hudson: That would be the case of something like the implementation error in ethereumjs.utils. Can that be entirely proven technically it was lost due to that error?
Vitalik: Yes, section 2 of my EIP covers that and it would apply.
Hudson: Sounds like the people who are the most vocal about it do not fall in a category that can be easily checked.
Vitalik: I know a few major categories of losses: Empty contract - someone sends ether to an account and they think that the account has code but it doesn't, a contract creation failed, and now they have no way of getting it back. Another case is where people send ether to an address with a contract that is only on the ETC chain. Also the javascript bug. Last case, people accidently sending money to junk addresses or the 0 address because they chopped off some characters at the end. 0 address is harder to deal with though. There is also weird special cases. Quadriga is unfortunately a weird special case.
Hudson: Vlad thoughts?
Vlad: That sounds reasonable.

### Address calculation changes post-Metropolis.
Christian: Am I correct in thinking that metropolis will change the way addresses are calculated?
Vitalik: Yes.
Christian: Is the community appropriately aware of that? There are use cases that could be disrupted due to this.
Vitalik: The community should definitely be made very aware of that. Once way to make this change totally safe is only to apply it to EIP 156 transactions, so we make it apply only to transactions where the sender is the null sender.
Christian: It also applies to the CREATE opcode?
Vitalik: No, that is why we created the CREATE2 opcode.
Christian: Ah, right.
Hudson: The concern is the community not realizing the breaking change? Would it be considered a breaking change from the POV of most dapp devs?
Vitalik: I don't think there are many users relying on contracts that send to addresses that will not exist for a year. If you told me that guy X lost money because of this, then I would bet that there is a more than 80% chance that it happened because of this + another bug they have. Example: Someone accidently sends ether to an account and that account exists on the ETC chain and not ETH chain and if we had not done this they could have recovered by generating the contract address on the ETH chain, but not they won't have that ability anymore. This change would increase the risk of losing money in combination with other mistakes that have a large probability of losing money regardless of what we do.
Vitalik: I see two routes here: One of them is slightly higher risk, which is to be loud about it and try to let everyone know it will break those types of contracts. The low risk thing would be to make it only apply to EIP 86 transactions. I'm totally cool with making it only apply to EIP 186 tx's. Basically, only making the change to the limit contract that just created it if the sender is a null sender, but I'm fine with both ways.
Hudson: Can you put a summary on the EIP in a comment? We can decide on it on the EIP.
Hudson: We determined last meeting that 156 cannot go in metropolis because we don't have the time, but if it goes in the future, but would it be a harder to put 156 in the future (for specific cases applying to part 1 and 2 of the EIP).
Vitalik: Like would it be harder to do it in Serenity vs Metropolis?
Hudson: Correct.
Vitalik: I expect not.
Hudson: I was thinking the same thing. For the ones that are special case that we are leaning towards not doing will be harder to get consensus on over time, but the other 2 situations can be easily brought up in later meetings.
Christian: Perhaps we should reach out directly to the community and ask if they are aware of the change and work from that response.
Hudson: I can send out something in the next week on social media channels and some Gitter channels.

## Attendance

Alex Beregszaszi (EWASM), Alex Van de Sande (Mist/Ethereum Wallet), Andrei Maiboroda (cpp-ethereum), Arkadiy Paronyan (Parity), Casey Detrio (Volunteer), Christian Reitwiessner (cpp-ethereum/Solidity), Dimitry Khokhlov (cpp-ethereum), Hudson Jameson (Ethereum Foundation), Jan Xie (pyethereum), Jeff Coleman (Ledger Labs), Lefteris Karapetsas (Raiden), Martin Holst Swende (geth/security), Nick Johnson (geth/SWARM), Péter Szilágyi (geth), Robert Habermeier (parity), Vitalik Buterin (Research & pyethereum), Vlad Zamfir (research), Yoichi Hirai (EVM)
