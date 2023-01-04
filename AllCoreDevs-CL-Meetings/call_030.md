# Ethereum 2.0 Implementers Call 30 Notes

### Meeting Date/Time: Thursday 2019/12/19 at [14:00 UTC](https://savvytime.com/converter/utc-to-germany-berlin-united-kingdom-london-ny-new-york-city-ca-san-francisco-china-shanghai-japan-tokyo-australia-sydney/dec-19-2019/2pm)
### Meeting Duration:  1 hr
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/112)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=LYLiqpj-wiE)
### Moderator: Danny Ryan
### Notes: Edson Ayllon


-----------------------------

# Summary

## ACTIONS NEEDED

Action Item | Description
--|--
**30.1** | Complete fork-choice test.
**30.2** | Use Muskoka to log failed SSZ blobs.
**30.3** | Decide solution for ETH transfer between execution environments and shards, while being read by block producers
**30.4** | Create full specifications for the Eth1-Eth2 bridge.
**30.5** | Decide on new caching specification proposal.
**30.6** | Create a script that reads and delivers the genesis state to the client.

-----------------------------

# Agenda

- [1. Testing and Release Updates](#1-testing-and-release-updates)   
- [2. Client Updates](#2-client-updates)   
- [3. Research Updates](#3-research-updates)   
- [4. Highlights from Client Survey](#4-highlights-from-client-survey)   
- [5. Networking](#5-networking)   
- [6. Spec discussion](#6-spec-discussion)   
- [7. Open Discussion/Closing Remarks](#7-open-discussionclosing-remarks)   

-----------------------------


# 1. Testing and Release Updates

**Video:** [`[0:46]`](https://youtu.be/LYLiqpj-wiE?t=46)

`v0.9.3`released which includes changes to State Transition and Networking. Missing in the Networking PR, adding attestation subnet bitfield to ENR, will be added.

BLS standards integration has gone through iterations. A good PR has been reviewed and will be merged. Release for the first week of January.

Phase 0 is undergoing a comprehensive audit. An official announcement will be released today. `v0.10`  will be the target.

## 1.1 Fork-Choice

Still awaiting completion of the fork-choice test. Harmony has finished beacon data processor implementation, close to spec, handling delayed attestations. The beacon data processor can be used to generate comprehensive scenarios for fork-choice. Harmony is prioritizing an integration test approach for fork-choice.

- [**@harmony-dev/beacon-chain-java#213** fork choice implementation/updates](https://github.com/harmony-dev/beacon-chain-java/pull/213)

## 1.2 Fuzzing

Lighthouse team fuzzers are matching `v0.9.1` of spec. Will be upgrading to `v0.9.3` or `v0.9.4` following three existing client implementations. Additionally, Python sub-interpreters integrated to keep Python implementations isolated. Nimbus integrated to multiple fuzzers. Beacon fuzz has potentially identified its first crash due to a failed assertion. More information provided tomorrow. Some fuzzers were published on [Fuzzit](https://fuzzit.dev/). The plan is to submit a request to Google to use their infrastructure for fuzzing, expected end of January.

Lighthouse has started looking at a library that allows random mutation of photo-buffers. This can be used with guided fuzzing engines, such as lib-fuzzer. Works similar to fuzzing done with Solidity compiler.

[**@cryptomental**](https://github.com/cryptomental), from the Eth1 fuzzing team, has joined the Lighthouse Beacon Fuzz team, working primarily on onboarding Prysm. Blog post detailing challenges and progress on Beacon Fuzz will be published.

RPC fuzzer for Lighthouse has been implemented, which has been running about a week. Won't be integrated to Beacon fuzz, but other clients are encouraged to do something similar.

[Muskoka](https://github.com/protolambda/muskoka-client) can log failed SSZ blobs.

## Actions
- **30.1**—Complete fork-choice test.
- **30.2**—Use [Muskoka](https://github.com/protolambda/muskoka-client) to log failed SSZ blobs.

# 2. Client Updates

**Video:** [`[13:41]`](https://youtu.be/LYLiqpj-wiE?t=821)

## 2.1 Trinity

Working towards testnets. [Merged PR](https://github.com/ethereum/trinity/pull/1311) for the first pass at attestation aggregation. [Py-ssz PR merged](https://github.com/ethereum/trinity/pull/1394) handling hash root calculations. Microbenchmarks indicated significant performance speed.

Other items:
- Progress made on separating validator client.
- Progress on syncing stability.
- Further work on Eth1 data component.

## 2.2 Artemis

Progress made on initiating minimal viable sync algorithm. Hoping to join a testnet soon. Refactored storage layer to increase reliability, to support queries needed on P2P. Continuing to integrate Harmony's Discovery v5.

## 2.3 Prysmatic Labs

Sixteen thousand validators ran on a single Beacon node locally. Several optimizations made. Working towards testnet restart with spec `v0.9.2`. A few core components will be redesigned. Fixing bugs on testnet as reported by users.

For networking, adding pubsub validator to stop automated propagation of pubsub message


## 2.4 Nimbus

Started on attestation aggregation, one PR merged. Started on benchmarking tool.

Researching on managing a fleet of Nimbus nodes, having kill switch reporting, etc. Researching including stacked traces with less overhead, as stacked traces are slowing down processes significantly.

For libp2p and networking, starting next week will have mixed libp2p daemon and libp2p pure Nim testnet.

Mostly implemented `v0.9.3` spec. Waiting for zcli or pyspec Trinity state to ensure alignment.

Research for Phase 2 includes EE, language, and generating WASM.

For Eth1, looking to sync with Geth, Parity Eth1 chain. There is a bottleneck in storage.

Started research on EVMC to investigate adding Nimbus as a backend.

## 2.5 Lodestar

`v0.9.2` spec branch merged in the next few days. Working on SSZ caching. Will upgrade and refactor libp2p, helping with validating incoming messages.

## 2.6 Lighthouse

Started mainnet 16k validator testnet, which ran for a week, containing 4 nodes running 4k validators on AWS. Ran and stopped seeing finality. As a result, now targeting 0.1.2 release which includes a fix for gossip nodes.

State was being stored before blocks, resulting in database error if the client crashed. Fixed by reversing the storage order.

Added [fix to Eth1 caching](https://github.com/sigp/lighthouse/pull/709). `deposit_root` and `deposit_count` now come from the logs instead of contract calls.

Made API upgrades.

For Networking, updated Rust gossip sub for content addressed messages. Started implementing naive attestation aggregation strategy.

New testnet may be launched tomorrow and made public next week.

Also hiring Rust developers, [see Twitter](https://twitter.com/sigp_io/status/1207080033254166528).

## 2.7 Shasper

Testing testnet against Prysmatic, ensuring the connection is reliable. The goal is to enter as many testnets as possible.

## 2.8 Nethermind

Still in Phase 0. Working on a validator of basic block creation. Still on spec `v0.9.1`. No Phase 1 yet.

For networking, deciding what algorithm to use for libp2p stack. The first stage will be on Go daemon.

## 2.9 Harmony

Working on fork-choice. More simulations are done.
- [Gossip pubsub simulation for Beacon Chain](https://hackmd.io/ZMBsjqdqSAK026iFFu_2JQ)

ns-3 simulator tested concluding insufficient support for Python. May move to something else.

Filed issues found on naive aggregation attestation.

# 3. Research Updates

**Video:** [`[33:08]`](https://youtu.be/LYLiqpj-wiE?t=1988)

TXRX consists of members from Artemis and Harmony are merged to focus on Phase 1, Phase 2 research.

Research areas include discovering the right short term availability scheme. STARKing a merkle root may be the best long term option, but depends on having a reliable STARK compatible hash function. Until then, options include the 2-dimensional scheme, using FRY as a fraud-proof mechanism.

Researching how ETH transfers will operate in Phase 2. Ether is used to pay transaction fees, which must be seen by block producers. The challenge is to transfer ETH between execution environments, between shards, and be read by block producers. Solution options include guaranteed cross-shard messaging. Here, the ETH execution environment would be the only one block producers would be required to understand.

Phase 2 call is scheduled for mid-January. Will focus on cross-shard transactions, and flea market.

Quilt is performing work on tooling for the contract EE to run. These tools will imitate Truffle, to ease developer onboarding.

Eth2 resource book first chapter will be released within 1-2 weeks.

Write-up being done on [EthResearch](https://ethresear.ch/) to help make a decision on state provider relayer questions, around block producers and state.

Quilt collaboration started with TXRX.

Research should be done to full spec Eth1-Eth2 bridge.

TXRX will be doing research on Eth bridge, among other things. Workshop will be done outside Stanford blockchain conference focusing on Phase 2.

EthBarcelona will be organized for May 15 as a one-day event. Will present updates on Eth2.0.
- [Eth Barcelona](https://ethbarcelona.github.io/)

For zero-knowledge proofs, need an optimal prover and optimal verifier. Currently in possession of an optimal prover, but the verifier is no longer optimal.

## Actions
- **30.3**—Decide solution for ETH transfer between execution environments and shards, while being read by block producers
- **30.4**—Create full specifications for the Eth1-Eth2 bridge.


# 4. Highlights from Client Survey

**Video:** [`[56:16]`](https://youtu.be/LYLiqpj-wiE?t=3376)

The survey is to aid in planning and identifying help for resources or bottlenecks.

Initial look, noise libp2p implementations needed. Will need to review further.

# 5. Networking

**Video:** [`[57:16]`](https://youtu.be/LYLiqpj-wiE?t=3436)

Most of this section has been done in a separate networking call. Another networking call schedule for the second week of January.

- [Networking call notes](https://hackmd.io/@benjaminion/SJ3W0qwAH)

# 6. Spec discussion

**Video:** [`[57:54]`](https://youtu.be/LYLiqpj-wiE?t=3474)

A proposal made to use timestamps instead of block depth to reduce overhead of caching, and issues handling re-orgs locally. Removes Beacon state read done when loading.
- [**eth2.0-specs#1537** Concerns about Eth1 Voting in Context of Caching](https://github.com/ethereum/eth2.0-specs/issues/1537)

## Actions

- **30.5**—Decide on new caching specification proposal.
- **30.6**—Create a script that reads and delivers the genesis state to the client.


# 7. Open Discussion/Closing Remarks

**Video:** [`[1:09:30]`](https://youtu.be/LYLiqpj-wiE?t=4170)

Happy Holidays. Next call week after new years.

------

# Annex

## Next Meeting Date/Time

Thursday January 9, 2020.

## Attendees

- Alex Stokes
- Ben Edgington
- Carl Beekhuizen
- Cayman
- Chih-Cheng Liang
- Dankrad
- Danny Ryan
- Hsiao Wei Wang
- Jared Wasinger
- John Adler
- Jonny Rhea
- Joseph Delong
- JosephC
- Justin Drake
- Kevin Chia
- Leo BSC
- Mamy
- Marin Petrunic
- Mehdi
- Meredith Baxter
- Mikerah
- Mikhail Kalinin
- Nicholas (Hsiu-Ping) Lin
- Nishant Das
- Paul Haauner
- Protolambda
- Raul Jordan
- Shahan Khatchadourian
- Sly Gryphon
- Terence
- Tomasz Stanczak
- Trenton Van Epps
- Vitalik Buterin
- Wei Tang
- Will Villanueva

## Links Mentioned

- [**@harmony-dev/beacon-chain-java#213** fork choice implementation/updates](https://github.com/harmony-dev/beacon-chain-java/pull/213)
- [Eth Barcelona](https://ethbarcelona.github.io/)
- [Networking call notes](https://hackmd.io/@benjaminion/SJ3W0qwAH)
- [**eth2.0-specs#1537** Concerns about Eth1 Voting in Context of Caching](https://github.com/ethereum/eth2.0-specs/issues/1537)
- [Call notes](https://hackmd.io/@benjaminion/SJ3W0qwAH) by [**@benjaminion**](https://github.com/benjaminion)
- [Gossip pubsub simulation for Beacon Chain](https://hackmd.io/ZMBsjqdqSAK026iFFu_2JQ)
