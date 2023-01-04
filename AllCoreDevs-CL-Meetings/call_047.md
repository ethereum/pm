# Ethereum 2.0 Implementers Call 47 Notes

### Meeting Date/Time: Thursday 2020/9/3 at 14:00 UTC
### Meeting Duration:  1 hr
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/178)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=FhFIog9D0II)
### Moderator: Danny Ryan
### Notes: Edson Ayllon


-----------------------------

# Contents

- [1. Testing and Release Updates](#1-testing-and-release-updates)   
- [2. Client Updates](#2-client-updates)   
   - [Prysm](#prysm)   
   - [Lodestar](#lodestar)   
   - [Teku](#teku)   
   - [Nimbus](#nimbus)   
   - [Lighthouse](#lighthouse)   
   - [Trinity](#trinity)   
- [3. Research Updates](#3-research-updates)   
- [4. weak subjectivity sync](#4-weak-subjectivity-sync)   
- [5. Networking](#5-networking)   
- [6. Spec discussion](#6-spec-discussion)   
- [7. Open Discussion/Closing Remarks](#7-open-discussionclosing-remarks)   



-----------------------------

# 1. Testing and Release Updates

Video | [1:18](https://youtu.be/FhFIog9D0II?t=78)
-|-

Spent a lot of time on Phase 1 testing. Honing in on a version 1 release. Doing work on scoring parameters for gossip sub. Using protocol labs testground simulator to pick this parameters. Should be completed by the next week and a half or so.

Wednesday, in six days, we'll have a networking call.

On testnets, Medalla looks good, getting good refinements. Based on feedback, we intend to do a dress rehersal of a testnet launch, so people can run through the motions before a mainnet deposit contract launch.

A bottleneck is getting some refinements and fixes in launchpad, which is persistently being worked on.

The intention is, in the second to last week of September, post the deposit contract. Put out the configuration parameters and launchpad during the week of the 21st of September. And do dress rehersal of launch one week later.

This gives a chance for block explorers, and other tool providers, to try their tools again.

As for practicing fork launches, we could do it before mainnet launch, or do it before we have a fork on mainnet.

Given there's friction for anything that delays mainnet launch, there's a preference to only do it long before we need to have a fork on mainnet. Regardless, there should be a write up for how forks on Eth2 will work.

When there is a need for a hardfork on mainnet, there will be practice on a testnet. But whether that practice is a priority now is unclear.

Practicing a hardfork would be changing some parameter, keeping it simple.

The testnet has shown a few problems in specops. Two clients are not finalizing on participation. Working on reconnecting clients.


# 2. Client Updates

Video | [10:43](https://youtu.be/FhFIog9D0II?t=643)
-|-

## Prysm

- Recieving good feedback on DOS vectors
- Applying feedback from the Quantstamp audit, in preparation for the official audit
- Started implementing Eth2 API. Intent is to have this supported for mainnet
- Started researching on weak subjectivity sync
- Fixing slashing bugs
- Implementing UX for validator client end to end workflow
- Fixing a few things for interop mode

## Lodestar

- Fixed a big memory issue preventing sync on Medalla
- Fixed separate bug also preventing syncing, related to fork-choice
- Looking at replacing the fork-choice entirely with something more modular
- Working on adding Phase 1 types and parameters, to start making proofs
- Working on Medalla to get in sync and propose a block

## Teku

- Along with some several minor bugs, fixed user reported block proposal letters, caused from missing deposits from Eth1 nodes, and inclusion of attestation from different forks
- Huge improvements in attestation effectiveness. Almost there.
- Thinking of fluid publishing locally produced attestations
- Implemented unicode password normalization rules of EIP-2335
- Up-to-date with v3 of slashing protection interchange format

## Nimbus

- Had 2 audits, one on consensus, and other on cryptography
- Reduced log file
- Working on database pruning
- RAM issue. Still in progress.
- Still maintaining multinet script. Now able to test a very small network with a split of 8*64 Nimbus and Prysm node to check finality.

## Lighthouse

- Fixed a deadlock that's been there for quite a while. Write up on the blog.
- Fixed bug in pruning
- Implemented http API
- Looking into attestation inclusion metrics
- Making UX easier to use
- New team member next week
- Gossip 1.1 in master
- Slasher found unique slashings
- Working on defining slashing protection interchange format
- Two audits starting October, trying to get everything in before then.

## Trinity

- Moving forward tabling Eth2 resources for Trinity. Those resources can go into imminent mainnet launch. Project is still open for open source contribution.

# 3. Research Updates

Video | [23:11](https://youtu.be/FhFIog9D0II?t=1391)
-|-

Phase 1: Couple PRs open for allowing crosslinking in non-optimal case. Revamped how attestations are accounted over time. Although it's a divergence from phase 0, it's much cleaner.

In terms of the optimal validator case, it's the same, if not simplified.

State size savings are negligible compared to validator set size. The driving factor was simplying how cross-links are tracked.

Trying to build a crawler using Rumor. Have a first implementation. Not doing gossip, but that's the next step.



# 4. weak subjectivity sync

Video | [27:33](https://youtu.be/FhFIog9D0II?t=1653)
-|-

Having something in place for weak subjectivity link at or soon after mainnet launch is a requirement. Not having it will be an annoyance at sync. An attacker can cheaply make syncing a nightmare.

The easiest thing to do is have a finalized root, and reject chains not having that finalized root.

Starting from a state would be a better UX. If one client does it, all clients may end up needing to do it.

In terms of documentation in P2P spec, we can document the security requirement, without specifying how it's handled.

It's low priority but high reward.

It's being treated as a client side tool/utility, not a network level spec, at least in the current version. Until it is, it may be better to treat it outside the P2P spec.

Leaning towards doing checkpoint states, to get into mainnet, then get the full version in later.

Clients may get together to standardize it, to make switching clients easier.

# 5. Networking

Video | [33:10](https://youtu.be/FhFIog9D0II?t=1990)
-|-

There will be a call on Wednesday. There's a number of things to discuss:
- Potential DOS vectors
- Networking monitoring tools
- Param choices
- v1.1 updates

# 6. Spec discussion

Video | [34:00](https://youtu.be/FhFIog9D0II?t=2040)
-|-

No spec discussion.

# 7. Open Discussion/Closing Remarks

Video | [34:20](https://youtu.be/FhFIog9D0II?t=2060)
-|-

No discussion. Keep up the great work.

------

# Annex


## Attendees

- Aditya Asgaonkar
- Afr Schoe
- Alex Stokes
- Ansgar Dietrichs
- Ben Edgington
- Carl Beekhuizen
- Cayman Nava
- Cem Ozer
- Dankrad
- Danny Ryan
- Grant Wuerker
- Guillaume
- Herman Junge
- Hsiao-Wei Wang
- Jonathan Rhea
- Joseph Delonng
- Justin Drake
- Lakshman Sankar
- Leo BSC
- Lightclient
- Mamy
- Paul Hauner
- Protolambda
- Raul Jordan (Prysmatic)
- Sam Wilson
- Terence (Prysmatic)
- Vitalik Buterin

## Next Meeting Date/Time

Thursday, September 17, 2020.
