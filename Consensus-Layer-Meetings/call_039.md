# Ethereum 2.0 Implementers Call 39 Notes

### Meeting Date/Time: Thursday 2020/5/14 at 14:00 UTC
### Meeting Duration:  1 hr
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/149)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=7uZtEy0nNbw)
### Moderator: Danny Ryan
### Notes: Edson Ayllon


-----------------------------

# Contents

- [1. Testing and Release Updates](#1-testing-and-release-updates)   
- [2. Client Updates](#2-client-updates)   
   - [2.1 Teku](#21-teku)   
   - [2.2 Lodestar](#22-lodestar)   
   - [2.3 Nimbus](#23-nimbus)   
   - [2.4 Trinity](#24-trinity)   
   - [2.5 Nethermind](#25-nethermind)   
   - [2.6 Prysm](#26-prysm)   
   - [2.7 Lighthouse](#27-lighthouse)   
- [3. Testnets](#3-testnets)   
- [4. Research Updates](#4-research-updates)   
   - [4.1 EWASM](#41-ewasm)   
   - [4.2 Vitalik](#42-vitalik)   
   - [4.3 TXRX](#43-txrx)   
   - [4.4 Geth](#44-geth)   
- [5. Networking](#5-networking)   
- [6. Spec discussion](#6-spec-discussion)   
- [7. Open Discussion/Closing Remarks](#7-open-discussionclosing-remarks)   


-----------------------------

# 1. Testing and Release Updates

Video | [0:00](https://www.youtube.com/watch?v=7uZtEy0nNbw)
-|-

The focus has been on `v0.12`. The last task is including the upgraded BLS. Will be released in the next couple of days.

There are several networking updates and modifications that came out of the network call.

Some increased testing will be released. There were some corner cases around modifying states in state transitions.

Beacon fuzz pushed a blog post.

- https://blog.sigmaprime.io/beacon-fuzz-04.html

A lot of progress made on structural fuzzing. Implemented arbitrary tripe on Eth2 types. It can now provide well-formed instances of custom types, greatly improving fuzzing coverage. An overflow has already been identified from this.

The last few weeks found a few issues collaborating with Teku. An infinite loop. And a segfault in Nimubs due to stack overflow.

Updated trophies list of beacon fuzz. Up to 18 now.

Good progress on Go integrations. This was in response to trouble integrating Serenity and Prysm. We will have a call with Prysm in a few hours.

A new architecture is being proposed in Beacon Fuzz. Moving away from C++ and applying bindings from Rust.

Breaking down Beacon Fuzzing to 3 separate tools:
- Eth2Fuzz - Coverage, leverage, structural
- Eth2Diff - Sample replay
- FFI Bindings - Core differential fuzzing

Full information in the blog post.

- https://blog.sigmaprime.io/beacon-fuzz-04.html

Also pushing Docker images for the community to find bugs.

Starting playing with Lodestar. We found a few type errors possibly. We will discuss this further outside the call.

There was a discussion a week ago on a beacon state that shouldn't be trusted.

This is the reason things will be split, to avoid this confusion.

We will need to sync off the beacon state at some point. Found a couple of overflows on Lighthouse. The spec has been clarified a few weeks ago. If overflow happens in the state transition, it's invalid.

The structural fuzzing helps mutate beacons states better. Allows valid SSZ containers, and beacon stats per spec.

One of the issues that came up was hitting the utility's state transition, bypassing the check performed at the network layer.

There are 2 ways to sync a network safely after running for more than 3 weeks.

1. Have checkpoint sync from genesis
2. Start from a trusted state

The second option has better UX but has the threat of the trusted source is unreliable.

# 2. Client Updates

Video | [9:29](https://youtu.be/7uZtEy0nNbw?t=569)
-|-

## 2.1 Teku

- Added snappy compression.
- Added support for Ping and getMetadata
- Improved memory usage during sync
- Support for Schlesi network


## 2.2 Lodestar

- Starting to be able to sync, stable on Schlesi, haven't reached the head, still not stable
- Discv5 still isn't running

## 2.3 Nimbus

- Multiple sync fixes in the past few weeks, including Snappy.
- Single make Schlesi target. Sync is working slowly by stable
- Working on performance, namely on Windows
- Fixing memory leaks. Some from libp2p, some form block caching.
- Focusing on bug-fixing. New tools to debug discovery.

Once we have fast state transitions, the next target is memory usage.

## 2.4 Trinity

- Continuing port to an async framework
- Updates to API
- Added more full-time contributors

## 2.5 Nethermind

- Updated to the specification
- Tested synchronizations. Had some problems with Mothra networking.

## 2.6 Prysm

- Working on Topaz maintenance
- Fixing network bugs
- Aligned to spec v0.11.2
- 100 blocks/s sync. Still can do more optimizations
- Work on slashing detection. The backend slashing service is working.
- Running client production tests (stress tests, inactivity finality tests)
- No issue running 16,000 validators
- 1 second slot times on stress tests. Seeing 85% participations instead of 99% due to timeout from RPC

## 2.7 Lighthouse

- Implementing hierarchy key derivation for BLS
- Kicking off external security review.
- Improved slashing detection.
- 16k validator testnets for 2 weeks
- Improvements in memory usage (300 MB RAM on 16k testnet)
- Working to fix state transition bugs
- Finished implementing full gossip sub implementation logic. Looking forward to how it runs on Schlesi
- Moved discv5 to standalone repo
- Updated stable futures, and dependencies ahead of security review
- Working on RPC error handling as well



# 3. Testnets

Video | [19:35](https://youtu.be/7uZtEy0nNbw?t=1175)
-|-

Multiple attempts for multiclient testnets that failed due to network fragmentation, and beacon nodes disconnecting and rejecting other peers, or rate-limiting. Different genesis times were calculated.

A multiclient testnet was launched. Now Schlesi has almost perfect finality for more than a week. Everyone's surprised by how stable the network is running.

Teku joined, syncing and validating.

Nimbus is also synchronizing. Experiencing sync issues, but the team is close to fixing it.

Lodestar managed to connect, but haven't tested it yet.

Given the current stability, interested in starting a coordinated multiclient testnet for v0.12 with 16k genesis validators, with 3 different clients at genesis.

After, we can try a dry run of the deposit contract on the testnet.

Target is June for v0.12 testnet, but unsure how long implementations will take.

Lodestar and Nimbus are new to Schlesi. Lodestar is syncing many epochs. Nimbus is close to the head of the chain, 100 epoch distance. Added their support to Eth2Stats.

A diff will be put up into what is going into v0.12. Coordinated testnets starting in June makes sense, with some smaller test runs in the weeks before.


# 4. Research Updates

Video | [26:48](https://youtu.be/7uZtEy0nNbw?t=1608)
-|-

## 4.1 EWASM

- https://ethresear.ch/t/the-eth1x64-experiment/7195
- https://ethresear.ch/t/eth1x64-variant-1-apostille/7365
- https://github.com/ewasm/eth1x64/blob/c09ed1bf84a72308cececa8a78fd1df30b95d1da/variant1.md

This article is on designing a cross-shard protocol between Eth1 shards with trying to be non-invasive to the EVM and dApp best practices.

The first variant uses receipts generated on the descending shard and submitted on the receiving shard.

The simple examples are wrapped tokens. This will allow having DAI on each shard.

Then other varients are being looked into. One is yanking.
- https://ethresear.ch/t/cross-shard-contract-yanking/1450

Rich transactions can create another iteration of yanking. Will look into yanking next, or something based on Eth transfer objects.

The main reason was to have a smaller scale to experiment and engage current dApp developers, preparing them for sharding.

Eventually, more useful designs mean larger changes in the EVM. If we do radical EVM changes, we lose the benefits of existing tooling. Because of this, it may be better to switch completely to WASM.

Past few months looking into new engines. These have been performing better, but are more complicated.

Looked at another EWASM compatible engine, but brings no speed benefits.

Fizzy v0.1 released. Passes official tests, but doesn't implement floating points. v0.2 has optimizations. v0.1 will be the baseline against the optimizations.

As part of benchmarking, looking at the different precompiles. Elliptic curve precompiles shows promising results. But requires big integer host functions.

Looking into BLS 12. Reaching speeds close to native speeds, in interpreters. Looking at BLS implementation in Rust, but didn't introduce the expected speeds. Rust was 5ms, and Wasm was 500ms. Then we reached out to Wasm-Snark. They implemented support for BLS12. With optimizations on Big Integer, moved to close to 14 ms. With more optimizations, may approach 8ms, half the speed of native.

We looking to replicate these findings on EVM. Added 3 opcodes to the EVM. Implemented 1 building block of the pairing operation, making a synthetic benchmark. With the synthetic implementation, got close to the Wasm numbers.

May be able to get rid of the BLS12 precompiles.


## 4.2 Vitalik

Looking into homomorphic encryptions. There's a use case for it in private information retrieval.

Published a post to cryptographers to see if they can solve polynomial commitment problems.

Looking into simplifications on proof of custody.

- https://ethresear.ch/t/a-0-001-bit-proof-of-custody/7409

Vitalik has a followup on dankrad's post.

The complexity of proof of custody can be reduced by 1/2 to 3/4.

An unsuccessful attempt to self-verified proof of custody using K commitments.

## 4.3 TXRX

Eth1-Eth2 merge research post just released.

- https://ethresear.ch/t/the-scope-of-eth1-eth2-merger/7362

Working on draft Eth1-Eth2 communication protocol. Working on PSE for phase 1 as well.

Network monitor. Lighthouse is sending unsolicited UDP packets. Opened PR for that.

Fork Choice tests. Generating tests using Alex's transpiler. Found a bug in Teku. Made improvements to high spec transpiler. Can translate Phase 1 spec. Three PRs opened based on those results.

Implemented gossip v1.1 on JVM libp2p.

## 4.4 Geth

Working on PR for Eth1-Eth2 RPC implementation based on RPC calls. Looking for input after the call. The outline is there, need to iron out a few points.

# 5. Networking

Video | [43:22](https://youtu.be/7uZtEy0nNbw?t=2602)
-|-

Call 8 days before this call. Debugging and other updates.

- https://hackmd.io/@benjaminion/rJkuZ4e5I

Still working on new spec updates on discv5 spec. It will improve the performance slightly and resolve one error message. Sometimes you can get packets that have seemingly wrong encoding, but just a spec bug. We will publish a new version.

Something for feedback will be in the next couple of days.

Looking for the path of least resistance to upgrading. Considering a soft update. It's complicated with live networks.

Due to the v0.12 spec update, maybe best to combine these updates, as the testnets need to be restarted regardless.

It will take approximately 1 more week, at least, to get the new spec done. Then will assist with the implementation.


# 6. Spec discussion

Video | [47:37](https://youtu.be/7uZtEy0nNbw?t=2857)
-|-

Phase 1 PRs with bugs seen. Testing on Phase 1 has been minimal. We have been prioritizing v0.12.

The fork-choice test reads the pyspec and transpiles.

We will see if tests are added with the next release.

Check on BLS phase 1 PR so tests can be generated.

- https://github.com/ethereum/eth2.0-specs/pull/1812

# 7. Open Discussion/Closing Remarks

Video | [50:37](https://youtu.be/7uZtEy0nNbw?t=3037)
-|-

No discussion. Next meeting in two weeks.

------

# Annex

## Resource Mentioned

- https://github.com/ethereum/eth2.0-pm/issues/149
- https://blog.sigmaprime.io/beacon-fuzz-04.html
- https://ethresear.ch/t/the-eth1x64-experiment/7195
https://ethresear.ch/t/eth1x64-variant-1-apostille/7365
- https://ethresear.ch/t/a-0-001-bit-proof-of-custody/7409
- https://ethresear.ch/t/the-scope-of-eth1-eth2-merger/7362
- https://github.com/ethereum/eth2.0-specs/pull/1812


## Next Meeting Date/Time

Thursday, May 28, 2020.
