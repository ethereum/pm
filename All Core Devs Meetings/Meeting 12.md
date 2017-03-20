# All Core Devs: Meeting 12
## Time: 3/17/2017 14:00PM UTC
## [Audio/Video of Meeting](https://youtu.be/g2gsYRlThD4)

### Agenda:
1. EIP signaling and voting system update [Facilitator: Hudson]
2. https://github.com/ethereum/EIPs/issues/225: Clique PoA protocol & Rinkeby PoA testnet [Facilitator: Peter]
3. https://github.com/ethereum/EIPs/pull/214#issuecomment-279423401: In STATICCALL Opcode should state-changing operations should actually throw, or just be reverted after the call returns? [Facilitator: Nick and/or Martin]
4. [EIP 161](https://github.com/ethereum/EIPs/issues/161) Clarification and Proposal to update the YP to say that built-in accounts (pre-compiles) are never empty and update implementations based on that. [Facilitator: Arkadiy and Yoichi]
5. Metropolis updates and finding a central location to document which EIPs are going into Metro.

# Notes
## 1. EIP Signaling/Voting System [Hudson]
There is a group from the Ethereum Foundation, Boardroom, Carbonvote, Metamask, and community volunteers who are creating the voting/signaling system for EIPs. It is going well. cdetrio has started making a compatibility table with a similar style of [this one](https://kangax.github.io/compat-table/es6/) used for ECMAScript. This table can be used to visually see compatibility across Ethereum clients and other specs (like RPC standards).

## 2. https://github.com/ethereum/EIPs/issues/225 Clique PoA protocol & Rinkeby PoA testnet [Peter]
Dapp devs need a simple way to test their dapps and most don't care about the underlying consensus mechanism approving their transactions. Clique is a simplified proof-of-authority protocol that is designed to be able to be easily implemented in multiple clients and block syncing systems (warp sync, fast sync, light clients, etc.). 500 lines of code total and should be able to be easily plugged into existing clients, which will help with adoption. See EIP for more technical info. Clients that agreed to implement Clique: Parity (Arkadiy - "We can support multiple consensus algos. No time frame for implementation."), ruby-ethereum/pyethereum (Jan - "Once standard is finalized, it should be easy to implement."), cpp-ethereum (Christian: "We are fine with this. It may take longer for us to implement due to other priorities for Metro.").
Next steps: Peter will finish expanding on his EIP in the issue and submit a formal PR for EIP acceptance.

## 3. In STATICCALL Opcode should state-changing operations should actually throw, or just be reverted after the call returns? [Martin]
Discussion on the potential security issues with implementing REVERT opcode, its effects on static analyzers, and other potential unwanted side effects.
Martin: As soon as we implement revert, it may be possible to abuse revert functionality to artificially create provably pure calls. Do we want these different mechanisms?

REVERT, STATIC_CALL, RETURNDATASIZE and RETURNDATACOPY opcode proposals have some interconnections that will be further discussed. They are somewhat cross-referenced in the EIP repositories README page.

Full conversation happens 12:27-29:17.

## 4. [EIP 161](https://github.com/ethereum/EIPs/issues/161) Clarification and Proposal to update the YP to say that built-in accounts (pre-compiles) are never empty and update implementations based on that. [Yoichi]
Yoichi: Yellow paper metropolis updates look fine, but Spurious Dragon changes have been reverted and are unclear. Yoichi visited Gavin's office which provided a better picture of how the Yellow Paper should be amended to update it to the latest. Yoichi will continue to work on it. Gavin and Yoichi are going to meet more frequently to help get the Yellow Paper updated. Yoichi has concerns on the copyright of the Yellow Paper and will work with Gavin on that.
Arkadiy: EIP 161 allows to delete empty accounts, but it does not specify a 
EIP-161 defines an empty account as "has no code and zero nonce and zero balance." By this definition precompiled contracts are never empty because they do have native code. Parity and go-ethereum afaict still would treat built-in account as basic and potentially empty. This is not an issue for the current mainnet, as all the built-ins have some balance, but may become an issue for Metropolis and private networks. Should we update the YP to say that built-in accounts are never empty and update implementations according to that?
Yoichi: Wrt to the Yellow Paper: The Spurious Dragon pull request specified that the pre-compiles could be empty, but we can easily change that to say pre-compiles cannot be empty. There would need to be an in-client mechanism to distinguish empty user accounts and empty pre-compiles.
Arkadiy: The de-facto standard appears to be that the pre-compiles can be empty, so we can just keep that standard. Just want a confirmation from others.
Pawel: That was the case before the Spurious Dragon HF. I don't see any reason for a change.
Peter: At some point, there was a bug in both parity/go clients that caused a mini-fork. The issue was that geth did not delete pre-compiles because it had a rule that pre-compiles could not be deleted, but parity did not have that rule. I agree with Arkadiy that this is a weird corner case and we need to specify this to prevent things like this to happen again.
Yoichi: YP currently has an exception for pre-compiles that even when an OOG call happens they are touched and the state is created.
Martin: How can this be a problem on private networks?
Yoichi: This is only a problem if they create private networks with homestead rules. People can start networks with pre-Spurious Dragon rules with empty accounts. That is the only case.
Vitalik: Imo over time we should be supporting old features for people making private networks for people with pre-Spurious Dragon rules.
Martin: Should it be assumed that hard forks are dependent on each other?
Peter: There have been discussions on this and the potential for people to be able to jump around various soft forks to implement certain features from different forks, but this could cause major complications and unforeseen dependencies between hard forks.
Christian: Yeah, cpp-ethereum is designed with the assumption of strictly ascending hard forks.
Hudson: This seems to not require an EIP, because this was dealt with during a previous HF. So everyone seems in agreement that it is not worth it to have backwards compatibility that is independent of incremental HFs to avoid overcomplications.
Arkidy: I agree, but the YP needs to be updated to clarify that.
Peter: Yeah I agree we don't need to support that.
Yoichi: I will clarify this point in my Spurious Dragon PR.

## 5. Metropolis Update
We are now going to put the most updated potential EIPs for metropolis in the EIPs Under Consideration section of the [EIP repo] (https://github.com/ethereum/EIPs).
Parity (https://github.com/paritytech/parity/issues/4833) and geth (https://github.com/ethereum/go-ethereum/pull/3757) are maintaining Metropolis PRs which track implementation progress.

[Quick tangent to Agenda Item 3]
Christain prefers EIP 5 be replaced with EIP 211 RETURNDATACOPY and RETURNDATASIZE EIP. Vitalik had a different opinion on that in a previous call. He feels that 5 is simpler and more ideal than 211. He is willing to go with 211 if it also means we can get rid of STATIC_CALL. There may be a cleaner way to implement EIP 5 and implement STATIC_CALL in another way. Main concern is to minimize opcode inflation to keep things simpler. Greg doesn't think the opcode inflation matters per say, but he thinks this collection of opcodes proposed is logically consistent and minimal. Vitalik clarifies that he shouldn't call it opcode inflation, but complexity added by data structures added by ocodes (like RETURNDATASIZE). Greg counters that it can simply other things if we pull it all together with the proposals. Vitalik agrees and thinks we should look for alternatives. This is still under discussion using an ongoing Skype chat with interested parties and potential research calls. We will try to come to consensus by next AllCoreDevs meeting.

[Back to Metropolis]
Hudson: Vitalik, you mentioned that the price increase has affected the timing of when block times are adjusted due to the difficulty bomb.
Vitalik: Yes.
Vitalik ran calculations based on statistics on the blockchain during the meeting.
End of June: Blocktime will be around 19.5s
End of August: around 28.5s.
Vitalik: Imo it would be great to get it out before the end of June, but a hard deadline would be end of August. Recommendation: End of June as a normal case target and end of Aug. as worst case deadline. The conditions that normal users will have live through for either case continue to get better and better which is dependent by price. Blockchain difficulty is a lagging moving average of the price. Imo probably is < 10% that difficulty will ever go down again, will almost certainly be above 200.

Vitalik elaborates more on this in 56:30 on the call.

Vitalik: Practical thing to do is to keep our heads down and try to complete this before end of June.

## Test Cases for EIPs [Martin]
Martin: I want to mention that anyone implementing Metropolis changes and other EIPs need to submit their test cases to tackle weird edge cases. The things learned when implementing these changes will benefit all clients and prevent consensus issues.

There is currently not a formal process to submit these test cases. Informal process is to talk to Martin or Dimitry about submitting the test cases.
Peter: One of the issues for devs is that it is complicated and messy to create tests that no one bothers. Long term solution suggestion: tool that allows a simple way to create tests. A way to more automatically create test cases.
Martin: I complete agree. For now, it is valuable for devs to write up descriptions and submit their test cases to send to Dimitry or others.
Hudson: I will talk to Dimitry about a cleaner process in the future and formalizing a way to submit test cases.

## Attendance

Alex Beregszaszi (EWASM), Andrei Maiboroda (cpp-ethereum), Arkadiy Paronyan (Parity), Casey Detrio (Volunteer), Christian Reitwiessner (cpp-ethereum/Solidity), Greg Colvin (EVM), Hudson Jameson (Ethereum Foundation), Jan Xie (ruby-ethereum & pyethereum), Martin Holst Swende (geth/security), Paweł Bylica (cpp-ethereum), Péter Szilágyi (geth), Vitalik Buterin (Research & pyethereum), Yoichi Hirai (EVM)
