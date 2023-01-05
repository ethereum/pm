# Ethereum 2.0 Implementers Call 50 Notes <!-- omit in toc --> 

### Meeting Date/Time: Thursday 2020/10/15 at 14:00 UTC <!-- omit in toc --> 
### Meeting Duration:  1 hr <!-- omit in toc --> 
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/187) <!-- omit in toc --> 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=L4Dvlgxku1g) <!-- omit in toc --> 
### Moderator: Danny Ryan <!-- omit in toc --> 
### Notes: Edson Ayllon <!-- omit in toc --> 


-----------------------------

# Contents <!-- omit in toc --> 

- [1. Testing and Release Updates](#1-testing-and-release-updates)
  - [Specification Update](#specification-update)
  - [Fuzzing Updates](#fuzzing-updates)
- [2. Testnet](#2-testnet)
  - [Zinken](#zinken)
  - [Medalla](#medalla)
- [3. Client Updates](#3-client-updates)
  - [Lodestar](#lodestar)
  - [Nimbus](#nimbus)
  - [Teku](#teku)
  - [Prysm](#prysm)
  - [Lighthouse](#lighthouse)
- [4. Research Updates](#4-research-updates)
  - [Vitalik](#vitalik)
  - [TXRX](#txrx)
  - [Leo BSC](#leo-bsc)
- [5. Networking](#5-networking)
- [6. Spec discussion](#6-spec-discussion)
- [7. Open Discussion/Closing Remarks](#7-open-discussionclosing-remarks)
- [Annex](#annex)
  - [Attendees](#attendees)
  - [Next Meeting Date/Time](#next-meeting-datetime)



-----------------------------

# 1. Testing and Release Updates

Video | [2:10](https://youtu.be/L4Dvlgxku1g?t=130)
-|-

## Specification Update 

Eth2 version 1 release candidate 0 spec was released:
- https://github.com/ethereum/eth2.0-specs/releases/tag/v1.0.0-rc.0

Included changes are:
- Discv5.1
- BLSv4

Version 1.0 spec release is approaching. 

## Fuzzing Updates

Structural diferential fuzzer added. An order of magnitude in fuzzing speed lost due to JVM instantiating each run. 

Custom fuzzing engine looking to be running by next week. 

Investigating 3-4 crashes, will reach out to relevant clients. 


# 2. Testnet

Video | [4:29](https://youtu.be/L4Dvlgxku1g?t=269)
-|-

## Zinken 

Good work on Zinken. Small issue with Prysm release that blocked the block explorer. 

However, generally, users had a positive experience. Testnet started finalizing. Participation is strong.

## Medalla

Medalla is not v1.0 compliant. We expect vast majority of community users to turn off their Medalla nodes when v1.0 mainnet release. 

It may be better to replace Medalla with a longterm v1.0 compliant testnet. This will be more controlled by developers than the community, for sustained support. 

This testnet can be launched 3 weeks before or 3 weeks after mainnet launch. Regardless, we should start a number of 1.0 testnets to test the machinery. 

Preston advocates for keeping Medalla. We'll still have a month or two of syncing data around. If there is an issue for syncing a lot of epochs, we'll see it before we see it on mainnet. 

As Medalla is today, may be good to see 3 weeks stress, and look for a leak. 

The issues with keeping Medalla instead of a replacement is Disc v5.1 and BLS v4.

Prysm would like to update Medalla to include Discv5.1 and BLSv4. 

The issue is Discv5.1. Clients can do a script upgrade to transition from Discv5.0 to Discv5.1. 

Zahary and Mehdi would prefer to maintain less testnets, to have less testnet specific code.

Issue will be opened to continue conversation, as there doesn't seem to be agreement on a decision in call. 


# 3. Client Updates


Video | [14:21](https://youtu.be/L4Dvlgxku1g?t=861)
-|-

## Lodestar

- Participated in Zinken with 4 validators. Incompalibility with URLs validators requesting and nodes are serving. Beacon node is stable, which is good news.
- Zinken was first successful testnet for Lodestar
- Fixing validator interaction. Keeping tracks of reorgs and new blocks coming in. 
- Trying to get to a stable state.
- New signature policy may be the reason for the recent success, better gossiping behavior. 


## Nimbus

- Outgoing audit in final stages.
- Next step is to join public attack nets
- Upgraded to version 1.0
- Working on releasing binaries of Nimbus for Windows, Mac, and Linux
- Github repo will be renamed to Nimbus-Eth2
- Implemented from weak subjectivity checkpoints. How does everyone manage the history of deposits in this mode? We have checkpoints that stores the entire history of deposits, and other small pieces of data.
- Started doing interop tests for gossip sub 1.1 in multinet repo. Hopefully will be enabled soon
- Ongoing work on reducing database size
- Futher reducing memory usage. 

## Teku

- Enabled moderatly strict subjectivity handling.
- Addressing issues from audit
  - Added ancestry checks to networking layer
  - Deprecating validator tools
  - Removing ability to enable/disable p2p snappy compression via cli
  - Stricter handling on gossip tools
- Teku can now run as a separate process, and use standard API events
- Discv5.1 merged into own repo, ready to be introduced into Teku
- Merged PR that reduced memory consumption by half a gig.
- Looking into 1.0 changes
- All reference tests are passing

## Prysm

- Releasing betav0 software by early next week
- Cleaning up general flags
- Working on Eth2 api layer
- Working on slashing protection interchangeable format
- Working on Discv5.1, for graceful upgrade
- Working on BLSv4 and peer scoring
- Aligning with Spec v1.0 rc-0.
- Released web UI

## Lighthouse

- Smooth Zinken launch
- Released v0.3.0. Breaking release. Lots of changes
- New directory structure
- Integrated weak subjectivity checkpoint
- Implmented majority of API. Working towards full complience, only a couple of endpoints left. 
- Passing v1.0 rc0 spec tests
- Made progress on GUI
- Draft EIP-3030 for remote signer API 
- Auditors working on security assessments, least authority completed reviews


# 4. Research Updates

Video | [24:17](https://youtu.be/L4Dvlgxku1g?t=1457)
-|-

## Vitalik 

Data availablity sampling. Thinking about how to simplify Phase 1. Looking at having data on chain, and nothing else. 

Phase 1 does not support state execution, but there are a number of complexities designed for state execution. Because it's not clear what multishard execution will exist in the future, it may be better to design on what we know. 

Phase 1 will focus on having consensus over blocks of data. One of the benefits we can capture is reducing dependance on committees. Either there is a hard 2/3 requirement, more than 1/3 would cause committees to stop working. A more flexible option could see an attacker knocking a lot of nodes, turning off committees as well. 

With data sharding, for not relying on committees, then data availability sampling can be done. 

Data availability sampling has a few requirements from clients. A few calls have been made for what that structure will look like. Progress has been made there.

Realistically, shard transition candidate addition will be superceded by data availability sampling. Regardless, won't be merged until version 1.0 release. 

Another option is Kate commitments. 

## TXRX

Team is undergoing reogranization. Losing tech support. However, research keeps going. 

Alex continues work on transpiler. Looking at transpiling into Rust.

Working on withdrawal for Eth1 shard. Eth1-Eth2 transition work in progress. Will release updates soon.

## Leo BSC

Looking into different metrics into different clients. 

Looking into metrics that are identical between clients. Put them into a spreadsheet. Will see how different clients perform. 
- https://docs.google.com/spreadsheets/d/1obCGque-BMHwMlX_SuFj_jCr6MiEGxNIoyYbOYYGaaQ/edit?usp=drivesdk

Looking into making a standard for these metrics. 

# 5. Networking

Video | [35:34](https://youtu.be/L4Dvlgxku1g?t=2134)
-|-

Discv5.1 implementations are near complete. Discussion neeeded on what to do with Medalla. 

# 6. Spec discussion

Video | [36:07](https://youtu.be/L4Dvlgxku1g?t=2167)
-|-

Capturing a few more complicated scenarios for test vectors of v1.0. PR of phase 1 will stay as is until v1.0 release. 



# 7. Open Discussion/Closing Remarks

Video | [37:08](https://youtu.be/L4Dvlgxku1g?t=2228)
-|-

Keep up the great work. Meeting in 2 weeks. 


------

# Annex 


## Attendees 

- Aditya Asgaonkar
- Afr Schoe
- Alex Stokes
- Ansgar Dietrichs
- Ben (SigP)
- Ben Edgington
- Carl Beekhuizen
- Cayman Nava
- Cem Ozer
- Dankrad Feist
- Danny Ryan
- Guillaume
- Hsiao-Wei Wang
- Justin Drake
- Leo BSC
- Mehdi Zerouali
- Meredith Baxter
- Mikhail Kalinin
- Nishant
- Pooja Ranjan
- Preston (Prylabs)
- Protolambda
- Sacha Saint-Leger
- Terence (Prysmatic)
- Trent Van Epps
- Victor Farazdagi
- Vitalik Buterin
- Zahary


## Next Meeting Date/Time

Thursday, October 29, 2020.
