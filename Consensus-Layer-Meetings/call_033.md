# Ethereum 2.0 Implementers Call 33 Notes

### Meeting Date/Time: Thursday 2020/02/06 at [14:00 UTC](https://savvytime.com/converter/utc-to-germany-berlin-united-kingdom-london-ny-new-york-city-ca-san-francisco-china-shanghai-japan-tokyo-australia-sydney/dec-19-2019/2pm)
### Meeting Duration: 57 minutes
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/126)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=c8BhhPfdy0A)
### Moderator: Danny Ryan
### Notes: Sachin Mittal


-----------------------------

# Summary

## ACTIONS NEEDED

Action Item | Description
--|--
**33.1** | Get required changes done with respect to the audit and networking updates (few PRs are up) and get out a release as soon as possible.
**33.2** | Danny to review per-function unit tests and follow-up on different approaches.
**33.3** | Danny to setup a call to dig deeper into the audit report from Least Authority (in 2 weeks)

-----------------------------

# Agenda

- [1. Testing and Release Updates](#1-testing-and-release-updates)   
- [2. Client Updates](#2-client-updates)   
- [3. Research Updates](#3-research-updates)   
- [4. Networking](#4-networking)   
- [5. Spec discussion](#5-spec-discussion)   
- [6. Open Discussion/Closing Remarks](#6-open-discussionclosing-remarks)   

-----------------------------


# 1. Testing and Release Updates

**Video:** [`[2:15]`](https://youtu.be/c8BhhPfdy0A?t=136)

1. Ongoing audit by Least Authority
    - Expecting initial report for internal review in a few days.
    - Will be shared soon
    - **Intention**: get required changes done with respect to the audit and networking updates (few PRs are up) and get out a release as soon as possible.
2. Fork choice tests
    - Danny working on these
    - Will be expanding upon the work done by the Harmony team, and do integration tests
    - Is there value in doing per function unit tests? 
        - Most clients use more sophisticated optimised algorithms than the spec provides; is there any interface to conveniently test them? (eg., on-block testing)
        - [Many] even if some one has a fancy implementation like a proto array we always have a reference implementation to compare. So, we can test reference one against the test vectors
        - [PaulH] proto array doesnt work for current tech. Should update the justified state. May get annoying for really low-level tests - probably best to skip all those. 
        - [Mikhail] Harmony's test format should be suitable for any arbitrary implementation of fork choice
        - By default everyone should be able to handle integration tests but the question is, is it valuable?
        - Better to have tests on full chain of blocks instead of unit tests
        - Reason of avoiding integration tests: trouble coming up with a succinct way of writing them. 
        - [Terence] Lighthouse has end-to-end tests that Prysm has also used. These are quite simple, and easy to generate. 
        - Danny to take a look
        - [Mikhail] Original intention - use integration tests for common scenarios and some complex scenarios; some checks are really difficult to implement in integration - in such cases unit tests can be used.
3. Proto, update: working on testing tool: [Eth2-lurk](https://github.com/protolambda/eth2-lurk)

## Actions
**33.1**— Get required changes done with respect to the audit and networking updates (few PRs are up) and get out a release as soon as possible.
**33.2**— Danny to review per-function unit tests and follow-up on different approaches.


# 2. Client Updates

**Video:** [`[12:25]`](https://youtu.be/c8BhhPfdy0A?t=741)

## 2.1 Teku (formerly Artemis)

- Continuing work of getting sync up and running
- Started testing against Prsym's network and working on issues as they come up
- Working on custom version of Protos back in binary merkle trees to provide hashing performance
- Completed v0.10.1 BLS implementation
- Working on general stability and scalability of the codebase
- Finishing work on processing Eth1 client deposits at follow-distance
- Issue while connecting to Prsym testnet: difficulty in understanding the structure of beacon blocks by range request
- [Jacek] Question about how to handle the case of receiving fewer blocks than requested. Follow up offline. 

## 2.2 Nimbus

- Whole team in Brussels
- Community: 
    - getting perception of the community
    - running nimbus testnet on old phones
    - beacon chain works on mobile
    - Defined a new way to communicate milestones for Nimbus publicly.
- Beacon Chain: 
    - Updated SSZ parser to better handle malformed SSZ
    - Sync refactor 90% done
- Testing: 
    - Ironing out v0.10.1 bugs
    - Fixed the fuzzing bug
- Currently Hiring: 
    - junior devs, tech writer

## 2.3 Trinity

- Currently working on
    - v0.10.1 of the spec
    - Separate out validator client from beacon node.
    - Beacon node APIs
    - Progress on Disc v5
    - Progress on Eth1 integration
- Updates:
    - Merged pilot p2p to trio which is working on concurrency stability
    - external spec updates to version 0.10.1

## 2.4 Lodestar

- Updates:
    - Integrating new SSC implementation
    - unavailability of all the APIs that are needed to fully integrate
    - required to generate some proofs if we want to use
    - found some loose ends in the typescript 'types'
    - started passing the v0.9.4 spec tests
    - pending work to update the fork choice - no test for that, yet
- Research: 
    - Updating the BLS implementation using Herumi library. Plans to test latest release
- General updates:
    - upgrading PGP implementation to new async version; taking the time to go through and add all the typescript typings that aren't there in Javascript - hoping to push alot of that upstream
    - Came across certain bugs in typescript - loose types

## 2.5 Prsym

- Testnet
    - performed first voluntary exit for the testnet
    - there exists validators slashing protection, currently it is just a DB
    - working towards including validators slashing object in the block as well
- General updates:
    - bunch of micro optimizations
    - using a new state structure
- Testing:
    -  stabilization on new fork choice - decreasing resource usage and improving sync timings


## 2.6 Lighthouse

- RFP solution deadling to the UI has passed; Several applicants - to be decided this week
- Hiring devs - 20 applicants
- General updates:
    - rearchitected concurrency logs - for better stability - less invasive
    - passing v0.10.1 tests to be merged this week
    - work on network upgrade
    - process started to test 100k validator testnet - optimizing that to make sure it comfortably runs on lower spec devices
- Troubleshooting:
    - dealt with higher RAM usage on large valued accounts - found memory fragmentation - tree hashcash made of lots of small heap allocations
    - built an abstraction to allow storing these multiple smaller lists in just one big allocation
    -  reduced memory usage by more than half - didn't affect performance

## 2.7 Nethermind

No one present.


# 3. Research Updates

**Video:** [`[27.02]`](https://youtu.be/c8BhhPfdy0A?t=1622)

## 3.1 Vitalik
- Thinking about longer term problems like 51% attack protection and 51% attack recovery
- There were a couple of insights on how to move the protocol in a direction more favourable to these kinds of things
- suggestion: include the uncle blocks - no concrete suggestive implementations on this
- Another research: Are there backwards-compatible ways to detect edge cases caused by attackers
    - eg., attacker tries to censor blocks for just long enough that they get some part of the network to think they are censoring and the other part of the network to think they are not censoring
    - some progress on this research
- How would we end up dealing with successful 51% attacks? Revert chain, or is there an alternative? Planning a post on these topics.

## 3.2 Quilt

- Eth2 general book, works as an on-ramp into phase 1 and phase 2 discussions (with Kelvin Fitcher and Ben Edgington)
- Aiming for a comprehensive guide to eth1 and eth2
- Progress: 5 chapters
- Aiming for release in 2-3 months
- There are some higher level questions in phase 2
    - Have been brainstorming with eWASM 
    - Have been putting together some end-to-end scenarios to be able to explore. E.g. dynamic vs. static state access.
        - dynamic state access - very much used in eth1
        - Proposal: switching over static state access in eth2
        - static can bring alot of benefits like bringing synchronous communication between EEs
            - simplifies state provider network drastically
        - Current progress:
            - extended the solidity compiler; added taint analysis
            - running taint analysis on current contracts using dynamic state access
        - Benefits of the approach:
            - see and analyse the different patterns that are existing in eth1
            - providing dev tooling around static state access
    - hand analysis of contracts like Uniswap - seeing how it would look like in a static state access model
- looking into on-chain queue based DeX - some patterns around it
- Suite of tools around eth development
    - Simulator - Ganache of Eth2
    - SDK around simulation server
    - Ease - truffle of Eth2
    - Library to create eth projects
    - Goal is to provide a unified workflow for developing and deploying to a simulator and then running tests 

## 3.3 TX/RX

- working on a construction for a clock-sync protocol compatible with beacon chain requirements
- looking at 2 approaches: hardening the protocol (investigation for robust clock collaboration) and relaxed adversarial model 
- working on requirements and documenting those
- helping Quilt with EE tooling
- paper for 1-way and 2-way bridge between eth1 and eth2 - out in a week with pending review
- cross shard transaction simulation in python: ongoing

[Eth222](https://www.eventbrite.com/myevent?eid=90667602239): Feb 22 after SBC.
There is also a slot for Eth2 at the Consensus 2020 conference in NYC in May.

## 3.4 Leo

Working with Proto on write-up of (an abstract) [client implementation](https://hackmd.io/Zc8wlp_LRfChQ6TyLC1kxA. Looking to get a first draft before Eth Barcelona in mid May. Invitation to client devs to contribute.

NB the Eth2 education channel exists on Telegram/discord.

# 4. Networking

**Video:** [`[42:41]`](https://youtu.be/c8BhhPfdy0A?t=2561)

- There was a call last week. Some [notes](https://hackmd.io/@benjaminion/HJTHyWyf8) available.
- continued refinement of network spec
- added conditions to reduce some of the DoS factors
- expecting changes from the Least Authority audit
- General discussion
    - Snappy compression - there is a PR in progress about how the length is specified. Using Snappy frame or block compression? Take a look if you haven’t yet.
    - Libp2p Noise protocol is now specified. The only handshake we need is the XX handshake. [Adrian] has put in a PR on this.

## Actions
- **33.2**— Danny to setup a call to dig deeper into the audit report from Least Authority (in 2 weeks)

# 6. Spec discussion

**Video:** [`[49:07]`](https://youtu.be/c8BhhPfdy0A?t=2947)

- Prsym has seen this a bunch in their testnet and it came up in an AMA the previous day
- if you miss your epoch, the effective balance goes down substantially - and you spend a lot of time working your way back up
- a modification so it is not quite so punishing
- Effective balance calculation may be modified to make it less severe if a validator loses a little bit of balance initially. There is an [issue open](https://github.com/ethereum/eth2.0-specs/issues/1609.

# 7. Open Discussion/Closing Remarks

**Video:** [`[50:41]`](https://youtu.be/c8BhhPfdy0A?t=3041)

EthDenver coming soon. Then SBC. The Eth2 discord has a conferences chat section we can use to coordinate.

------

# Annex

## Next Meeting Date/Time

Thursday February 20, 2020; 14:00 UTC

## Attendees

- Adrian Manning
- Alex Stokes
- Ben Edgington
- Cem Ozer
- Cayman
- Carl Beekhuizen
- Chih-Cheng Liang
- Danny Ryan
- Dankrad
- Herman Junge
- Hsiao Wei Wang
- Jacek Sieka
- Jannik Luhn
- Joseph Delong
- Justin Drake
- Kevin Chia
- Leo BSC
- Mamy
- Milan Patel
- Mikhail Kalinin
- Nicolas
- Paul Hauner
- Pedro Edson
- Protolambda
- Slyvian Laurent
- Terence
- Trenton Van Epps
- Vitalik Buterin
- Will Villanueva
