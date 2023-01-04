# Ethereum 2.0 Implementers Call 55 Notes <!-- omit in toc --> 

### Meeting Date/Time: Thursday 2021/1/14 at 14:00 UTC <!-- omit in toc --> 
### Meeting Duration:  1 hr <!-- omit in toc --> 
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/198) <!-- omit in toc --> 
### [Audio/Video of the meeting](https://youtu.be/xNt6MmEV3JI) <!-- omit in toc --> 
### Moderator: Danny Ryan <!-- omit in toc --> 
### Notes: Edson Ayllon <!-- omit in toc --> 


-----------------------------

# Contents <!-- omit in toc --> 

- [1. Client Updates](#1-client-updates)
  - [1.1 Teku](#11-teku)
  - [1.2 Nimbus](#12-nimbus)
  - [1.3 Lighthouse](#13-lighthouse)
  - [1.4 Lodestar](#14-lodestar)
  - [1.5 Prysm](#15-prysm)
- [2. Upgrade 1](#2-upgrade-1)
- [3. Q1 R&D](#3-q1-rd)
- [4. Research Updates](#4-research-updates)
- [5. Networking](#5-networking)
- [6. Spec discussion](#6-spec-discussion)
- [7. Open Discussion/Closing Remarks](#7-open-discussionclosing-remarks)
- [Annex](#annex)
  - [Attendees](#attendees)
  - [Next Meeting Date/Time](#next-meeting-datetime)

-----------------------------

# 1. Client Updates

Video | [1:49](https://youtu.be/xNt6MmEV3JI?t=109)
-|-

## 1.1 Teku

- Merged a commutiy contributed feature. The option to load graffiti dynamically from a file on runtime.
- Incorportated recent risk API updates, returns requested state as JSON or SSE depending on accept header
- Reworked validator client to optionally use dependant root fields. Currently have toggled off by default.
- Reviewed upcoming protocol upgrade changes, and have been doing refactoring to prepare for it.
- General cleanup, bug fixes, performance tests
- Hardening of P2P layer
- Code quality related refactoring.

## 1.2 Nimbus

- Released 1.0.6. 
- Reproducable builds for ARM devices
- Improved subnet walking logic. 
- Working on a new form of slashing protection. Disables a validator running if more than one validator (doppelganger) is detected to be running.
- Starting work on the REST API. 
- Have proper mailing list. Available at http://subscribe.nimubs.team.

## 1.3 Lighthouse

- Coordinating with the team to best apply to phase 0 mainnet, and sharding and merge blocks. Made blog post
- Published a few releases
- Added new system for monitoring validators, in PR now, in beacon node side
- Adding support for weak subjectivity sync. 
- Been reviewing midyear upgrade PRs
- Thinking of how to support sharding and merge experimental work

## 1.4 Lodestar

- Been working on making beacon node more stable and easy to use
- Refactor requested response code, to help revisiting syncing
- Now shifting some team to look at future hardforks. Looking at updating database to support hardforks
- Release targeting Monday

## 1.5 Prysm

- Made slasher protection on validator more performant
- Version 1.1 release Monday
- Bugfixes with new release
- Eth2 API, almost done with net working stack
- Experimenting with lightclient sync prometheus. 
- Updating test utilities for better test setups.


# 2. Upgrade 1

Video | [13:37](https://youtu.be/xNt6MmEV3JI?t=817)
-|-

Current intention is to do a minor upgrade to the Beacon chain, mid-year, early summer. Would have nice to have features and cleanups to help with maintenance, and edge cases. Currently in the form of PR proposals, in a temporary folder named lightclient.

This should make things cleaner, but might represent technical debt. A few PRs up for review: Accounting reform, and global penalty quotient. 

The other big one is adding a sync committee. Similar to a beacon committee. This adds lightclient support as a first citizen. 

There is a sync protocol file, which demonstrates how to construct a lightclient sync protocol. 

Worth discussing are new message type for reactivation, and other things like that. 

Beyond that, there are network iterations and fixes release prior this fork. A couple of security fixes to fork-choice, under internal review right now. 

Happy to open up for discussion here and in the repo. 

This serves as a warmup to forking mainnet, first in testnets. 

The target is to come into agreement on the updates within the next two weeks, by the end of January, by next call.

Conversation about epoch transition, and optimization.

Epoch reform may help with tree hashing.

From Nimbus, the slowest processing is persisting state.

# 3. Q1 R&D

Video | [27:14](https://youtu.be/xNt6MmEV3JI?t=1634)
-|-

What's happening in the next few months to solidify the upcoming upgrades in the next few years. The first is Eth1-Eth2 merge, and the second is sharding.

Specs on the sharding R&D are up in PRs right now. And the merge work is talked on EthResearch. Both are in different ranges of R&D, prototypes and local testnets.

In terms of client resourcing, there's stuff to dig in that can help the R&D effort.

The goal is by the end of Q1 have good specs on both, and make a decision on what to pursue for production. 

After the mid-year upgrade, emphasis will be placed on one of these two major upgrades.

Each team should put some time in education and digging into the R&D.

For merge, testnets will be launched on Q1. It makes sense to start work on the specs. Some work needs to be done on the Eth1 side with opcodes.

Looking to open up the working group on these upgrades, and posting information that's more digestable. 

There is a merge channel on the Discord, where people can ask questions.

Looking for someone with expertise in cryptography, diving into Kate commitements. 

Working on getting a date scheduled for a 3-4 hour session, talking about this. 

Working on a blogpost as well.

# 4. Research Updates

Video | [35:49](https://youtu.be/xNt6MmEV3JI?t=2149)
-|-

Merge and sharding work is ongoing.

Future work is divided into functionality (merge and sharding), and security features. Currently the security of beacon is good enough. We can make it better. But, maybe we should be focusing on functionality.


# 5. Networking

Video | [39:02](https://youtu.be/xNt6MmEV3JI?t=2342)
-|-

Issue open. In the way we do attestation aggregation, a nice to have optimization, that ultimately made more work on the network today.

If someone can quantify "I want I have" on mainnet, it would be useful.

The unintended consequences may show up in the case of an attack. 

Ongoing issue with error codes.

The minor updates, looking for a minor release, instead of midyear upgrade. 

# 6. Spec discussion

Video | [45:26](https://youtu.be/xNt6MmEV3JI?t=2726)
-|-

No spec discussion.


# 7. Open Discussion/Closing Remarks

Video | [45:44](https://youtu.be/xNt6MmEV3JI?t=2744)
-|-

Testnets. Scheduled to review Pyrmont towards the end of January. 

Pyrmont seems to be serving its needs. One thing we can consider, as people join, devs can join enough to have a majority, to keep the testnet stable even if validators don't properly exit. 

------

# Annex 


## Attendees 

- Aditya Asgaonkar
- Afri
- Alex Stokes
- Ansgar Dietrichs
- Ben Edgington
- Carl Beekhuizen
- Cayman Nava
- Dankrad Feist
- Danny Ryan
- Hsiao-Wei Wang
- Jacek Sieka
- JosephC
- Justin Drake
- Lakshman Sankar
- Lightclient
- Meredith Baxter
- Mikhail Kalinin
- Nishant
- Paul Hauner
- Protolambda
- Terence (Prysmatic)
- Vitalik Buterin
- Zahary


## Next Meeting Date/Time

Thursday, January 28, 2020.
