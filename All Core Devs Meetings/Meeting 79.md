---
date: 2020-01-24 14:00:00 UTC
duration: 1h 25m
---

# All Core Devs Meeting 79
### Meeting Date/Time: Friday 24 January 2020, [14:00 UTC](https://savvytime.com/converter/utc-to-germany-berlin-united-kingdom-london-ny-new-york-city-ca-san-francisco-china-shanghai-japan-tokyo-australia-sydney/jan-24-2020/2pm)
### Meeting Duration: 1.5 hrs
### [Github Agenda](https://github.com/ethereum/pm/issues/148)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=0-Vld7GTRhQ)
### [Reddit thread](https://www.reddit.com/r/ethereum/comments/et7yyd/live_core_devs_meeting_79_2020124_1400_utc/)
### Moderator: Tim Beiko
### Notes: Edson Ayllon

---

# Summary

## EIP Status

EIP | Status
---|---
EIP-1057, EIP-1803, EIP-2384, EIP-2387 | `Accepted & Final`
EIP-2464 | `Last Call`
EIP-1380, EIP-2046 | `Eligible for Inclusion` 
EIP-1702 | `Eligible for Inclusion` Pending Champion. Not scheduled for Berlin 
EIP-663, EIP-2348, UNGAS | Depends on EIP-1702 
EIP-1962, EIP-1559 | Discussed under `EFI`. Discussion to be continued in EthMagician thread | 
EIP-1985 | Discussed under `EFI`. Decision required around needing a Hard Fork 

*Note: Removed EIPs accepted in Istanbul.*


## Decisions Made

Decision Item | Description
--|--
78.1 | UNGAS to `Eligible for Inclusion` after formal specification is made
78.2 | EIP-2464 to `Last Call`
78.3 | EIP-2348 to `Eligible for Inclusion`
78.4 | No objections from Core Devs to update RPC spec for pending blocks to return block number



## Actions Needed

Action Item | Description
---|---
78.1 | UNGAS to be formally specified into an EIP draft
78.2 | EIP-2464 draft to be merged, and updated to `Last Call`
78.3 | EIP-2348 is `Eligible for Inclusion`
78.4 | EIP-2456 discussion to continue on Ethereum Magicians
78.5 | EIP-1962 disucssion to continue on Github
78.6 | Discuss timings for Berlin, London EIPs


---

# Agenda


1. [EIP Review](#1-eip-review) 
2. [Testing Updates](#2-testing-updates) 
3. [EIP Improvement Process Meeting](#3-eip-improvement-process-meeting) 
4. [RPC Spec](#4-rpc-spec) 
5. [Review Previous Decisions](#5-review-previous-decisions) 

---

# 1. EIP Review

**`video`** [`7:25`](https://youtu.be/0-Vld7GTRhQ?t=445)

## 1.1 UNGAS

**`video`** [`7:25`](https://youtu.be/0-Vld7GTRhQ?t=445)

UNGAS was introduced by Wei Tang, to be combined with Account Versioning and Reprising. UNGAS was introduced to make stateless Ethereum gas reprising easier. The proposal is to remove smart contracts, and any EVM code, to observe gas. We know this is currently possible through 3 mechanisms—with opcode GAS, in CALL-like instructions, and when hitting the "out of gas" exception.

UNGAS would bring three main changes. First, disable instruction gas. Second, stop CALL-like instructions from forwarding gas, instead forward all gas every time. Third, change the semantics of the "out of gas" exception by reverting all frames and the entire transaction.

This change would be very disruptive. Because of this, Wei proposes account versioning—before UNGAS `version 1`, and after UNGAS `version 2`. Legacy smart contracts without UNGAS would still work. 

Once version 2 is introduced, all opcodes will be reprised. Legacy version 1 smart contracts will be more expensive than version 2 smart contracts. This gas price difference is to migrate usage away from legacy contracts resulting from the economic advantages of version 2 contracts. 

Once these changes are introduced, we could meter the witness size separate from everything else. 

If usage remains only on version 1, stateless Ethereum would need to be designed considering version 1, not leading to any benefits. If usage of version 1 becomes negligible, stateless Ethereum pricing logic can ignore version 1, and use version 2 pricing logic. 

Questions about UNGAS. If an origin contract calls an external contract that has a bug and always throws "out of gas," how can we make sure the origin contract finishes running, as all gas is being forwarded? And what happens when version 1 contract calls a version 2 contract that runs out of gas? What happens to reprise if a version 2 contract calls a version 1 contract? For delegate calls, does account version matter for cross contract calls?

While the description of UNGAS is very short, the change is complex. The likelihood something is not covered is very high, so rigorous analysis is needed.

Account versioning was postponed past Istanbul and Berlin hard forks as nothing critical used it at their deployment, and would instead introduce complexity without functionality. 

UNGAS is currently unspecified under an EIP.

- [Remove Gas Observables and Better Error Handling](https://corepaper.org/ethereum/compatibility/forward/#remove-gas-observables-and-better-error-handling)
- [Blog - (un)gas](https://blog.ethereum.org/2020/01/17/eth1x-files-digest-no-2/)

## 1.2 EIP-2464 (eth/65)

**`video`** [`33:51`](https://youtu.be/0-Vld7GTRhQ?t=2032)

EIP-2464 addresses making transaction propagation more optimally in the network. When blocks propagate, 25-50 peers connect, depending on the client. When a new block is found, that entire block is sent a few peers and announced to the rest. For the peers receiving the announcement, they recreate the block after a short wait. 

Observing Ethereum's network bandwidth usage, a large chapter is caused by transaction propagation. Contrasted to block propagation, transaction propagation does not include announcements and requests. One megabyte/second upload-download is used to shuffle transactions. Each transaction is sent to all peers, and each peer receives that same transaction from all other peers, creating wasted bandwidth. 

This EIP introduces transaction announcements and retrieval requests to significantly reduce network bandwidth by imitating block propagation. 

This EIP does not require a hard-fork. It is backward compatible and can be implemented gradually. 

EIP motioned to be merged as a draft, and moved to `Last Call`. 

- [EIP-2464 PR](https://github.com/ethereum/EIPs/pull/2464)

## 1.3 EIP-2348 (Validated EVM contracts)

**`video`** [`44:37`](https://youtu.be/0-Vld7GTRhQ?t=2676)

A few changes have been added to EIP-2348 addressing concerns brought up. A rule was added to validation, limiting the size of a code segment to the contract size stored on-chain. The second change is in regards to the header. 

Validation would add new multi-byte instructions. New opcodes will be easier to add. 

For validation to run, the header must be included in the code, and account versioning must be set to version `1` account (assumes account versioning starts at version `0`). 

A concern was brought up stating that the current validation implemented is less complex than this EIP. Another concern was brought up involving static jumps and allowing undefined opcodes. 

EIP-2348 is `Eligible for Inclusion` and awaiting implementation and reference tests. EIP targetted for the London fork. 

- [Validated EVM Contracts PR](https://github.com/ethereum/EIPs/pull/2348)


## 1.4 EIP-2456 (Time Based Upgrade Transitions)

**`video`** [`1:02:25`](https://youtu.be/0-Vld7GTRhQ?t=3745)

This EIP is to use a timestamp and block number, instead of only a block number, for upgrades. A counter EIP, made by Jason, does exist but hasn't been formally made. The counter EIP is simpler and easier to implement. Instead of looking back on blocks to confirm activation, that time is used as confirmation. 

Future discussions tabled to Ethereum Magicians. 

- [Time Based Upgrade Transitions PR](https://github.com/ethereum/EIPs/pull/2456)

## 1.5 EIP-1962 (EC arithmetic and pairings with runtime definitions)

**`video`** [`1:10:32`](https://youtu.be/0-Vld7GTRhQ?t=4232)

All progress, updates, and optimizations posted to Github. A concern was brought up regarding assembly, in that assembly would be difficult to review. The part that is assembly is simple arithmetic, and the rest is code that can be reviewed. No external audit had been planned. 

- [EIP-1962 Go Repo](https://github.com/saitima/eip1962)

## 1.6 EIP-1559 (Fee market change for ETH 1.0 chain)

**`video`** [`1:16:53`](https://youtu.be/0-Vld7GTRhQ?t=4613)

A concern for deployment is minor collusion, and manipulating the fee in some way. James proposes to deploy ProgPoW first, then deploy EIP-1559 after. 

## Actions

- **78.1**—UNGAS to be formally specified into an EIP draft
- **78.2**—EIP-2464 draft to be merged, and updated to `Last Call`
- **78.3**—EIP-2348 is `Eligible for Inclusion`
- **78.4**—EIP-2456 discussion to continue on Ethereum Magicians
- **78.5**—EIP-1962 disucssion to continue on Github

## Decisions

- **78.1**—UNGAS to `Eligible for Inclusion` after formal specification is made
- **78.2**—EIP-2464 to `Last Call`
- **78.3**—EIP-2348 to `Eligible for Inclusion`


# 2. Testing Updates

**`video`** [`1:20:47`](https://youtu.be/0-Vld7GTRhQ?t=4847)

No testing updates.

# 3. EIP Improvement Process Meeting

**`video`** [`1:21:09`](https://youtu.be/0-Vld7GTRhQ?t=4869)

Next meeting scheduled for January 29. EIP-IP meetings are documented in an Ethereum Cat Herders Github repo. 

- [EIPIP Repo](https://github.com/ethereum-cat-herders/EIPIP)

# 4. RPC Spec

**`video`** [`1:23:23`](https://youtu.be/0-Vld7GTRhQ?t=5000)

When a block is retrieved on the RPC, if the block is pending the result is null. For the miner, it makes sense to be null, as for the hash. However, if there is a parent block, we will know what the block number will be, and transactions executing within do have access to that block number. The change is adding to spec to respond with a block number for pending blocks instead of returning null.

There were no objections to the change. 

## Decisions

- **78.4**—No objections from Core Devs to update RPC spec for pending blocks to return block number

# 5. Review Previous Decisions

**`video`** [`1:30:00`](https://youtu.be/0-Vld7GTRhQ?t=5400)

It may be good to discuss how early or late are the proposals for Berlin and London.

## Actions

- **78.6**—Discuss timings for Berlin, London EIPs

---

# Annex

## Next Meeting Date/Time

Friday, February 7, 2020.

## Attendance

- Alex Beregszaszi
- Alex Viasov
- Alexey Akhunov
- Daniel Ellison
- Danno Ferrin
- David Palm
- Gandalf
- Guillaume
- James Hancock
- Louis Guthmann
- Martin Holst Swende
- Pawel Bylica
- Peter Szilagyi
- Pooja Kanjan
- Stefen George
- Tim Beiko
- Tomasz Stanczak
- Trenton Van Epps

## Links Mentioned

- [Remove Gas Observables and Better Error Handling](https://corepaper.org/ethereum/compatibility/forward/#remove-gas-observables-and-better-error-handling)
- [Blog - (un)gas](https://blog.ethereum.org/2020/01/17/eth1x-files-digest-no-2/)
- [EIP-2464 PR](https://github.com/ethereum/EIPs/pull/2464)
- [Validated EVM Contracts PR](https://github.com/ethereum/EIPs/pull/2348)
- [Time Based Upgrade Transitions PR](https://github.com/ethereum/EIPs/pull/2456)
- [EIP-1962 Go Repo](https://github.com/saitima/eip1962)
- [EIPIP Repo](https://github.com/ethereum-cat-herders/EIPIP)
