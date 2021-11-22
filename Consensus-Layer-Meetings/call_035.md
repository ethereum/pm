# Ethereum 2.0 Implementers Call 35 Notes

### Meeting Date/Time: Thursday 2020/3/12 at 14:00 UTC
### Meeting Duration:  0.5 hrs
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/132)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=orVYfqP_YuQ)
### Moderator: Danny Ryan
### Notes: Edson Ayllon


-----------------------------

# Contents 

1. [Testing and Release Updates](#1-testing-and-release-updates)   
2. [Client Updates](#2-client-updates)   
3. [Research Updates](#3-research-updates)   
4. [Networking](#4-networking)   
5. [Spec discussion](#5-spec-discussion)   
6. [Open Discussion/Closing Remarks](#6-open-discussionclosing-remarks)   

-----------------------------


# 1. Testing and Release Updates

Video | [9:27](https://youtu.be/orVYfqP_YuQ?t=567)
-|-

Specification (spec) `v0.11.0` released. This release includes updates to the [P2P networking specification](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/p2p-interface.md) with DOS hardening, and other changes, updates to the [state transition specification](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/beacon-chain.md) including support for isolating chains, adding proposer index blocks to increase verification usefulness, and other changes. `v0.11.0` spec is the stable multi-client specification target. There are no expectations to further update the state-transition outside of feedback from client implementors. As multi-clients are tested, minor changes are expected to be included in the networking spec in the future, with an emphasis on clarifications. 

Next testing priorities include:
- Fork-choice
- Networking

As workload transitions from creating a specification to testing, advancements in tests are expected. 

Tests have been up-to-date for `v0.10.0`. Priorities have been shifted to network testing and integration testing. 

A networking tool called [Rumor](https://github.com/protolambda/rumor) will be utilized for testing scenarios. 


# 2. Client Updates

Video | [13:25](https://youtu.be/orVYfqP_YuQ?t=805)
-|-


## 2.1—Lighthouse

- Work started towards a peer reputation system. 
- ENR pulled into an independent crate for sharing with Open Ethereum.
- Improving [Node Discovery Protocol v5 (discv5)](https://github.com/ethereum/devp2p/blob/master/discv5/discv5.md) implementation to work with the ENR crate, and allow performance improvements, and increase the speed of peer discovery.
- Building an ENR predicate query search to upgrade for the attestation aggregation scheme.
- Released a [validator UX survey](https://twitter.com/sigp_io/status/1235336791370149889) to understand staker needs
- Trialed a light implementation of [@protolambda](https://github.com/protolambda)'s [remerkleable](https://github.com/protolambda/remerkleable). Results were promising, however, the changes required to transition to remerkleable are significant.
- Experimenting optimizations with BLS signature verification. Positive results currently.
- Onboarded two new developers.

## 2.2—Prysm

- Interop with Lighthouse on their ETHDenver branch.
- Version 0.1 of the slashing service added to the Prysm testnet.
    - Successfully cut a double vote.
    - Slash was reflected in block explorers.
- New SSZ created for Prysm, resulting in significant performance improvements.
- Working on a staging service that significantly improves the memory and CPU usage.
- Working on dynamic substitutions of subnets.
- Working on noise interoperability.
- Upgrading to spec `v0.11.0`.

## 2.3—Nimbus

- New targets for March sprint
    1. Interop
    2. Initiate audit
    3. Remove libp2p daemon
- Almost to spec `v0.10.1`. Fixing BLS bugs. Progress on attestation aggregation.
- CI automatically launches a small local network and ensures finalization after 5 epochs.
- Can now interop with Geth discv5 for peer discovery.
- Testing interop with Lighthouse.
- Several improvements for libp2p stability.
- Acquired a new log analysis tool to track libp2p errors. 
- Performance bug from the previous call identified and fixed, resulting in being able to handle 5x more traffic.

## 2.4—Teku

- Discv5 merged. It can discover Lighthouse nodes, but not Teku nodes.
- Deposit processing is done.
- Sync operational.
- Good progress on RPC implementation.
- Interest in standardizing RPC interfaces across clients. Possibly led by Infura. 
- Merged PR to implement remerkleable, resulting in a 4x boost in block processing, and a 4x slow-down epoch processing. Epoch processing will be optimized.
- 98% of block processing time is now signature verification, marking the next target. 
- Working on optimizing database operations.
- `v0.10.1` to be merged to the master branch.

[A write-up for improving BLS signature performance](https://ethresear.ch/t/fast-verification-of-multiple-bls-signatures/5407) has been published by Vitalik. On normal blocks, this proposal should increase performance by approximately 20%. 

## 2.5—Trinity

- Increased stability of node and libp2p stack.
- Interoperable with Geth and Lighthouse for discv5. 
- Working towards `v0.11.0`. 

## 2.6—Lodestar

- Discv5 ready for testing interop in the next week.
- Working to improve database storage.
- Audit results returned fairly positive. 
- The next few weeks marked for syncing public testnets and improving node stability.

## 2.7—Nethermind

- Updated to `v0.10.1`, supporting the latest BLS requirements.
- Validators processes synchronizing. 


# 3. Research Updates

Video | [26:43](https://youtu.be/orVYfqP_YuQ?t=1603)
-|-


Audit results received. Some changes already included in `v0.11.0` spec. The audit will be made public soon. 

Phase 1 major PR to be merged. General structures of Phase 1 are in place. The last week of March to early April will be preferred for Phase 1 prototyping. 

## 3.1—TXRX

Two articles published.
1. [On the way to Eth1 finality](https://ethresear.ch/t/on-the-way-to-eth1-finality/7041) covering the safety of Eth1.x follow distance.
2. [Appraisal of Non-sequential Receipt Cross-shard Transactions](https://ethresear.ch/t/appraisal-of-non-sequential-receipt-cross-shard-transactions/7108) covering non-sequential receipt cross-shard transactions.

## 3.2—Vitalik

Vitalik published an article detailing [polynomial commitments to replace state roots](https://ethresear.ch/t/using-polynomial-commitments-to-replace-state-roots/7095). Instead of using Merkle trees to store state roots, polynomial commitments would be used. A polynomial commitment is a hash of a polynomial that mathematical checks can be performed on. This update kind can be performed on Eth1.x as well. This structure easily allows very short witnesses for very large amounts of keys and values. Witness size, which has been a bottleneck for stateless clients, will be reduced by over 90% with polynomial commitments. Relies on recent breakthroughs in mathematics by AZTEC team made in the past month. 

Polynomial commitments for state roots require a more long-term project. In short-term, polynomial commitments can be utilized for block bodies, and potentially receipts. Polynomial commitments may be considered for storing shard block data. 

Increased optimism in using zk-SNARKs over a full virtual machine in the medium term.

## 3.3—Quilt

Seeing where Eth2.0 research can be implemented in the current Eth1.x chain. Updates on Eth2.0 research from Quilt to be discussed on the next call.

# 4. Networking

Video | [36:36](https://youtu.be/LYLiqpj-wiE?t=3474)
-|-

[Previous networking call](https://hackmd.io/@benjaminion/rk2OEQ64L) was productive. New networking calls to be decided if to take place.

During and after EthCC testing has moved forward. Discovered discv5 issue with txids. Requesting client implementors to share their discv5 implementations for testing. 

# 5. Spec discussion

Video | [39:00](https://youtu.be/orVYfqP_YuQ?t=2340) |
-|-

Spec discussion taking place in [Eth2.0 spec repo](https://github.com/ethereum/eth2.0-specs/issues).  

March marked for multi-client experimentation and updating to `v0.11.0`. 

April marked for multi-client testnets. 


# 6. Open Discussion/Closing Remarks

Video | [40:07](https://youtu.be/orVYfqP_YuQ?t=2407) 
-|-

Client retreat for interop postponed foreseeably one or more months. Work remote currently.  

Finalizing roadmap for Phase 1 should initiate the end of March, the first week of April.

Eth1 client teams looking to prototype Eth1 immigration against Eth2-Phase 1 prototypes. 

------

# Annex

## Resource Mentioned

- [Phase 0 Networking specification](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/p2p-interface.md)
- [Phase 0 State Transition specification](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/beacon-chain.md)
- [Node Discovery Protocol v5 (discv5)](https://github.com/ethereum/devp2p/blob/master/discv5/discv5.md) 
- [Sigma Prime Validator user experience survey](https://twitter.com/sigp_io/status/1235336791370149889)
- [Remerkleable](https://github.com/protolambda/remerkleable)
- [Rumor](https://github.com/protolambda/rumor)
- [Fast verification of multiple BLS signatures](https://ethresear.ch/t/fast-verification-of-multiple-bls-signatures/5407)
-  [On the way to Eth1 finality](https://ethresear.ch/t/on-the-way-to-eth1-finality/7041) 
-  [Appraisal of Non-sequential Receipt Cross-shard Transactions](https://ethresear.ch/t/appraisal-of-non-sequential-receipt-cross-shard-transactions/7108)
- [Using polynomial commitments to replace state roots](https://ethresear.ch/t/using-polynomial-commitments-to-replace-state-roots/7095)
- [Eth2.0 Networking Call #3 Notes](https://hackmd.io/@benjaminion/rk2OEQ64L)
- [Eth2.0 spec discussions](https://github.com/ethereum/eth2.0-specs/issues)

## Attendees

- Aditya
- Alex Stokes
- Ansgar Dietrichs
- Ben Edgington
- Carl Beekhuizen
- Cayman
- Cem Ozer
- Chih-Cheng Liang
- Danny Ryan
- Dmitry Shmatko
- Evan Van Ness
- Guillaume
- Herman Junge
- Hsiao-Wei Wang
- Joseph Delong
- Leo BSC
- Mamy
- Marin Petrunic
- Meredith Baxter
- Mikhail Kalinin
- Nicolas Liochon
- Nishant Das
- Paul Hauner
- Protolambda
- Sam Wilson
- Steven Schroeder
- Terence Tsao
- Tomasz Stanczak
- Trenton Van Epps
- Vitalik Buterin

## Next Meeting Date/Time

Thursday, March 26, 2020.
