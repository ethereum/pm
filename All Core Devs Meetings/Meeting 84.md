# All Core Devs Meeting 84 Notes
### Meeting Date/Time: Friday 3 April 2020, 14:00 UTC
### Meeting Duration: 1.5 hrs
### [Github Agenda](https://github.com/ethereum/pm/issues/162)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=JqxVvJBhTxo)
### [Reddit thread](https://www.reddit.com/r/ethereum/comments/fu1fzg/live_ethereum_core_devs_meeting_84_20200403_1400/)
### Moderator: Hudson Jameson
### Notes: Edson Ayllon

---

# Summary

## EIP Status

EIP | Status
---|---
EIP-1057, EIP-1803 | `Accepted & Final`
EIP-2537, EIP-2315 | `Accepted` Targetting Berlin
EIP-1559 | `Accepted`
EIP-2464 | `Last Call`
EIP-1380, EIP-2046,  EIP-2456, EIP-2315, EIP-2541, EIP-2539, EIP-1985, EIP-1702, EIP-1380, EIP-663 | `Eligible for Inclusion`
EIP-1702 | `Eligible for Inclusion` Pending Champion. Not scheduled for Berlin
EIP-663, EIP-2348, UNGAS | Depends on EIP-1702
EIP-1962,  EIP 2456, EIP 2515 | Discussed under `EFI`. Discussion to be continued in EthMagician thread |
EIP-2515 | Discussed under `EFI`. Decision required around needing a Hard Fork

*Note—Removed EIPs included in Muir Glacier.*

## Decisions Made

Decision Item | Description
--|--
84.1 | EIP-2537 moved to `Accepted`, targetting Berlin.
84.2 | EIP-2315 moved to `Accepted`, targetting Berlin.


## Actions Needed

Action Item | Description
---|---
84.1 | Fuzzing to start for EIP-2537.
84.2 | [Proposed changes to EIP-2315](https://github.com/ethereum/EIPs/pull/2576) to be merged.
84.3 | Address `fork_id` in EIP-2456.
84.4 | Other clients to do measurements/testing for EIP-2046.
84.5 | Audit proxy contract used by EIP-1962 for the Eth2.0 deposit contract
84.6 | Organize a call among Core Developers to see how testing can be improved. 


---

# Agenda



1. [Eligibility for Inclusion (EFI) EIP Review](#1-eligibility-for-inclusion-efi-eip-review)   
2. [Berlin Timing](#2-berlin-timing)   
3. [EIP-2583 Penalty for account trie misses](#3-eip-2583-penalty-for-account-trie-misses)   
4. [Testing updates](#4-testing-updates)   
5. [EIPIP Survey](#5-eipip-survey)   
6. [Review previous meeting](#6-review-previous-meeting)   


---


# 1. Eligibility for Inclusion (EFI) EIP Review

Video | [4:15](https://youtu.be/JqxVvJBhTxo?t=255)
-|-

> As part of an EIP centric forking model, this EIP tracks the first step in the approval process for any EIP to be included in a fork or upgrade. Specifically, the stage where the Core Developers vet the concept of an EIP and give a “green light” sufficient for EIP authors to move forward in development.
>
>—[EIPs Eligible for Inclusion](https://eips.ethereum.org/EIPS/eip-2378)

## 1.1—EIP-1962 and BLS-Signature working group updates (EIP-2537)

EIP-1962 and BLS-Signature working group updates has a good amount of comments [in the Agenda](https://github.com/ethereum/pm/issues/152).

[EIP-1962](https://eips.ethereum.org/EIPS/eip-1962) is considered `EFI`, however inclusion is not considered anytime soon. What is considered in the short term is the narrowed down pre-compile version in [EIP-2537](https://github.com/ethereum/EIPs/pull/2537).

EIP-2537 would work to create a proxy contract for the Eth2.0 deposit contract that verifies inputs to the deposit contract. From [Alex Stoke's Medium article](https://medium.com/@ralexstokes/what-eth2-needs-from-eth1-over-the-next-six-months-86b01863746 ): 

>  The initial way to become a validator of eth2’s beacon chain will be via the deposit of ETH on a smart contract on eth1 known as the “deposit contract”. To save on gas costs and minimize complexity, this smart contract does not do much more than cryptographically commit to a given deposit (in a Merkle tree) which then allows a proof to be consumed on the beacon chain. Importantly, the BLS signature required to validate a deposit is not verified on the eth1 chain. This fact has already resulted in loss of testnet ETH when a series of BLS signatures were incorrectly computed due to a bug. By enabling verification of BLS signatures on the eth1 chain (enabled by EIP-2537), we can write a “forwarding” smart contract that takes the deposit data, verifies the signature and only then sends the deposit data to the deposit contract. This capability is not required for the deposit contract to work in a secure fashion but does add some extra peace-of-mind for developers interfacing with the deposit contract.


The proxy contract for the deposit contract should go through auditing, as the deposit contract has. A proxy contract can be audited before EIP-1962 is implemented. 

For [EIP-2537](https://github.com/ethereum/EIPs/pull/2537), the Rust implementation passes all tests for basic arithmetic properties and test specs on the test vectors from the IETF spec, which can be used as a reference and be considered as completed. 

The Go implementation may also be close to final. Alex Vlasov will talk to the Go implementor to start fuzzing. 

There should be an Eth2.0 implementation for BLS in Java for Hyperledger Besu. 

Nethermind already has the Eth2.0 BLS bindings. 

EIP-2537 motioned to accepted for Berlin. 

## 1.2—EIP-2515 Difficulty Bomb

James Hancock could not attend the call, so discussion of EIP-2515 will be pushed to a future call. 

## 1.3—EIP-2315 Simple Subroutines for the EVM

[Proposed changes to EIP-2315](https://github.com/ethereum/EIPs/pull/2576) included:
- A stricter definition of opcodes
- Spec-level introduction of`return_stack`
- More examples
- Removal of that `end-of-stack` prefilled item on the `return_stack`

In the first version, the `return_stack` was not well articulated. If too many returns were made, it would return to a stop opcode. Doing so now throws an error instead. As of now, the spec allows walking into a subroutine. 

No previous implementation contradicts  these changes. Walking into a subroutine can be useful for multiple entry points. No point in forbidding them. Putting a stop statement before each subroutine is available for those wanting to forbid walking into a subroutine. 

The spec is currently implemented in Go. OpenEthereum has a small work in progress, but no implementation yet. Hyperledger Besu hasn't started work on it either, but also should not be a problem. Nethermind will also work on implementation. Aleth is unsure if it will upgrade to the next hardfork. 

EIP-2315 motioned to accepted for Berlin. 

## 1.4—EIP-2456 Time Based Upgrades

One issue that hasn't been solved is `fork_id`. That may be one potential blocker, namely for testnets.

The spec of `fork_id` can also be changed. `fork_id` should be resolved before inclusion in Berlin. 

## 1.5—EIP-2046

[2046 update in the agenda](https://github.com/ethereum/pm/issues/162#issuecomment-607975445 )

EIP-2046 if implemented would reduce the gas cost of using precompiled contracts.

EIP-2046 was decided on the previous call to reduce measurements. Measurement reductions were done in OpenEthereum, and was found safe. Discussion can be opened to reprising all existing precompiles, possibly in a separate proposal. Changing the cost to call precompiles from 700 to 40 seems to be safe. For BN precompiles, the cost was very low. For many other precompiles, the cost was much higher than the computation time it takes. Reprising from 700 to 40 gas was also found safe for `modx` on OpenEthereum. 

These measurements were only done in OpenEthereum. Other clients also need measurements. 

Loosely related, the BLAKE2 cost is higher than keccak. Improving gas costs for BLAKE2 may help the move to stateless Ethereum. As BLAKE2 has to be called several times, it's unlikely to be cheaper than keccak if it is a precompile. An opcode can be created for Blake2 to reduce gas costs. 

Discussion to be continued next meeting.

Discussion on BLAKE2 can be continued on Gitter. 

## 1.6—Other items

- [ HF meta for Berlin needs update](https://eips.ethereum.org/EIPS/eip-2070)
- [Account abstraction](https://ethereum-magicians.org/t/implementing-account-abstraction-as-part-of-eth1-x/4020)

## Decisions

- **84.1**—EIP-2537 moved to `Accepted`, targetting Berlin.
- **84.2**—EIP-2315 moved to `Accepted`, targetting Berlin.

## Actions

- **84.1**—Fuzzing to start for EIP-2537.
- **84.2**—[Proposed changes to EIP-2315](https://github.com/ethereum/EIPs/pull/2576) to be merged.
- **84.3**—Address `fork_id` in EIP-2456.
- **84.4**—Other clients to do measurements/testing for EIP-2046.
- **84.5**—Audit proxy contract used by EIP-1962 for the Eth2.0 deposit contract

# 2. Berlin Timing

Video | [23:32](https://youtu.be/JqxVvJBhTxo?t=1412)
-|-

EIPs targetting Berlin include: 
- EIP-2537
- EIP-2315
- EIP-2515 maybe
- EIP-2046 maybe


Considering timing by hard fork phases:
- April: implementation
- May: testing
- June: testnets

The end of June is more realistic for Berlin to go live.

The hardfork won't be scheduled until the EIPs are completed. 

It may be good to set some priorities for what implementors will work on to be ready for Berlin. 

EIP-2537 is the highest priority. 

For EIP-2537, implementors can use parts of the EIP-1962 codebase that apply. The EIP-1962 codebase can be downgraded for use in EIP-2537. Other specialized BLS implementations could also be used. 

EIP-2315 is mostly spec'd out, ready to be implemented, can be the second priority. 


# 3. EIP-2583 Penalty for account trie misses

Video | [1:07:55](https://youtu.be/JqxVvJBhTxo?t=4075)
-|-

[Penalty for account trie misses](https://github.com/ethereum/EIPs/blob/db1e389aae4e05654703d24862b0db91040bf745/EIPS/eip-draft-trie-penalty.md) addresses shortcomings in current implementations of nodes as state trie has grown over the years. Previous efforts to address trie included raising certain gas costs (EIP-1884, EIP-150). The path of raising gas cost won't work, as gas costs, in worst-case scenarios, would need to be raised by a couple of orders of magnitude. 

EIP-2583 adds a penalty for opcodes that access the account for trie accounts that don't exist. This penalty would be post-operation. This also affects call-derivatives, only when calling something that doesn't exist in the trie and does not transfer value.

EIP-2583 would not disrupt existing contracts. There's seldom a reason to call something that doesn't exist, not sending it Ether, and not expecting it to go badly.

Today, on a 10 million gas block, it is possible to do 13k trie lookups. If we add a penalty of a thousand, we can reduce that by 41%. Having a higher penalty than that would not make sense, as it can be bypassed for another gas cost. 

This EIP is one proposal to deal with state attacks. The upside is that it doesn't disrupt current contracts. The downside is it can be partially bypassed, and raising the penalty would not increase its efficiency. 

There are talks to having a global penalty counter, stopping a transaction when the penalty counter passes the gas cost. These kinds of schemes may be implemented, however, may have side-effects on layer2. 

# 4. Testing updates

Video | [1:17:16](https://youtu.be/JqxVvJBhTxo?t=4636)
-|-

Code that generates blockchain tests reworked. Now retesteth can generate all blockchain tests. Testing is now not dependant on Aleth. Any client that supports RPC can be used to generate tests. 

VM tests were added to blockchain tests, and can now be run on Hive. 

 [retesteth.ethdevops.io]( http://retesteth.ethdevops.io/) was launched with statistics. Displays tests executed on supported clients like Geth, Aleth, and Besu. Anyone can contact Dimitry to have their client added to that statistics site. 

Nethermind is not happy with the testing protocol. Possibly organize a call among Core Developers to see how testing can be improved. 

Here is the discussion link for the testing channel:  https://gitter.im/ethereum/tests. Dimitry can be found there, and coordination for the test call can be done there. 

## Actions

- **84.6**—Organize a call among Core Developers to see how testing can be improved. 


# 5. EIPIP Survey

Video | [1:20:41](https://youtu.be/JqxVvJBhTxo?t=4841)
-|-

The EIPIP group [has a survey out](https://docs.google.com/forms/d/e/1FAIpQLSeadXscoQgrKznUOAEB_jSzNNFKHWDEFJxKH1LpDsDsC6mXpw/viewform) collecting feedback on the current EIP process from stakeholders. It's six questions, really easy to complete. 

- [EIPIP Survey](https://docs.google.com/forms/d/e/1FAIpQLSeadXscoQgrKznUOAEB_jSzNNFKHWDEFJxKH1LpDsDsC6mXpw/viewform)

Currently, the group is working on EIP-1 and fixing the EIP bot. Also, the EIP page will be made on [ethereum.org](http://ethereum.org/).


# 6. Review previous meeting

Video | [1:24:22](https://youtu.be/JqxVvJBhTxo?t=5062)
-|-

Most of the EIPs on the previous call were restatements of the current decision status. 

EIP-2046. Alex stepped up and did benchmarking. Other clients also may be doing benchmarking. Probably won't need a bounty. 

---

# Annex


## Attendance

- Alex Beregszaszi
- Alex Vlasov
- Artem Vorotnikov
- Daniel Ellison
- David Mechler
- Dimitry
- Edson Ayllon
- Greg Colvin
- Guillaume
- Hudson Jameson
- Ian Norden
- Jason Carver
- JosephC
- Karim Taam
- Louis Guthmann
- Mariano Conti
- Pawel Bylica
- Peter Szilagyi
- Pooja Ranjan
- Rai
- Tim Beiko
- Tomasz Stanczak
- Trenton Van Epps
- Wei Tang

## Links Mentioned

- [Proposed changes to EIP-2315](https://github.com/ethereum/EIPs/pull/2576) 
- [Alex Stoke's Medium article on EIP-2537](https://medium.com/@ralexstokes/what-eth2-needs-from-eth1-over-the-next-six-months-86b01863746 )
- [2046 update in the agenda](https://github.com/ethereum/pm/issues/162#issuecomment-607975445 )
- [ HF meta for Berlin needs update](https://eips.ethereum.org/EIPS/eip-2070)
- [Account abstraction](https://ethereum-magicians.org/t/implementing-account-abstraction-as-part-of-eth1-x/4020)
- https://gitter.im/ethereum/tests
-  [retesteth.ethdevops.io]( http://retesteth.ethdevops.io/)
- [Penalty for account trie misses](https://github.com/ethereum/EIPs/blob/db1e389aae4e05654703d24862b0db91040bf745/EIPS/eip-draft-trie-penalty.md)
- [EIPIP Survey](https://docs.google.com/forms/d/e/1FAIpQLSeadXscoQgrKznUOAEB_jSzNNFKHWDEFJxKH1LpDsDsC6mXpw/viewform)


## Next Meeting Date/Time

Friday 17 April 2020, 14:00 UTC
