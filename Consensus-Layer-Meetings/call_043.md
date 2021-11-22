# Ethereum 2.0 Implementers Call 43 Notes

### Meeting Date/Time: Thursday 2020/6/9 at 14:00 UTC
### Meeting Duration:  1 hr
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/165)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=4IooxDX_GfU)
### Moderator: Danny Ryan
### Notes: Edson Ayllon


-----------------------------

# Contents

- [1. Testing and Release Updates](#1-testing-and-release-updates)   
   - [1.1 Rumor](#11-rumor)   
   - [1.2 Beacon Fuzz](#12-beacon-fuzz)   
- [2. Testnets](#2-testnets)   
- [3. Client Updates](#3-client-updates)   
   - [3.1 Lodestar](#31-lodestar)   
   - [3.2 Trinity](#32-trinity)   
   - [3.3 Nethermind](#33-nethermind)   
   - [3.4 Nimbus](#34-nimbus)   
   - [3.5 Prysm](#35-prysm)   
   - [3.6 Lighthouse](#36-lighthouse)   
   - [3.7 Teku](#37-teku)   
- [4. Incident response](#4-incident-response)   
- [5. Weak subjectivity as it pertains to client security and UX](#5-weak-subjectivity-as-it-pertains-to-client-security-and-ux)   
- [6. Research Updates](#6-research-updates)   
   - [6.1 TXRX](#61-txrx)   
   - [6.2 Vitalik](#62-vitalik)   
- [7. Networking](#7-networking)   
- [8. Spec Discussion](#8-spec-discussion)   
- [7. Open Discussion/Closing Remarks](#7-open-discussionclosing-remarks)   

-----------------------------

# 1. Testing and Release Updates

Video | [0:50](https://youtu.be/4IooxDX_GfU?t=50)
-|-

## 1.1 Rumor

Rumor updated.
- Scripting improved
- New commands
- RPC test work done.

Sync still needs work. Test generation has started being enabled. Python Eth2 (pyspec) progress.

Fork-choice handling with Rumor a more tractable approach. The TXRX fork-choice tests can be used for additional testing.

A tutorial for Rumor will be released. Integrating another set of interfaces cross client injecting blocks and attestations. Scripts can be defined for which blocks to import and which blocks to serve, minimal.

## 1.2 Beacon Fuzz

Update on Beacon Fuzz.

The idea is to enable community fuzzing. A detailed set of instructions are available, available for all clients. Fuzzing can be done for an hour before moving onto the next.

Discord channels are created for people to report bugs as they find.

High severity vulnerabilities found, on Lodestar and Nimbus. Nimbus is an index error. Was fixed quickly. Lodestar is a memory exhaustion vulnerability when passing invalid ENRs.

Snappy crate has been patched. PR was sent 2 months ago, and the maintainer recently merged it.

Now that state transition spec is finalyzed, attention will be on differential part of beacon fuzz. Eth2fuzz and eth2diff are close to complete. 26 unique bugs found across all major implementations.


# 2. Testnets

Video | [8:54](https://youtu.be/4IooxDX_GfU?t=534)
-|-

Altona has been running. A bit of non-finality due to an appearance of a whale who didn't run their node. Generally things are good.

Reached out to client teams to talk about what's on their plates before moving onto a large-scale multiclient testnet.

Couple clients working on stability issues. People are hardening UX.

Playing with Proto's nodes to run an attack net.

# 3. Client Updates

Video | [10:45](https://youtu.be/4IooxDX_GfU?t=645)
-|-

## 3.1 Lodestar

- Merged v0.12 branch to master
- Gossipsub v1.1 not merged yet
- Started connecting chrome debugger for profiling
- Optimized some pieces of state transition
- A few blockers on stability
- Closing in on minimal viable client
- Validator and account CLI available
- Did not make it to Altona head. A few bottlenecks in syncing.

## 3.2 Trinity

- Working on getting to sync altona
- Refactoring fork-choice
- Working on syncing. Connected to Lighthouse
- Next task is performance optimization (sync speed)

## 3.3 Nethermind

- Focus has been Ethereum 1 client
- 10-20% increase in Eth1 users
- Article published on how to use Nethermind as an Eth1 deposit provider for Eth2
- "logs extraction in Nethermind is super fast - we created a hierarchy of bloom filters for logs based on something that Parity had but with some additional heuristic around the fill ratio of blooms. So if you want to get all the deposits at once you should see nice results"

## 3.4 Nimbus

- A lot of work done fixing bugs found in Altona
- Working on bugs for missed attestations
- Audits start Monday
- Working on [auditor handbook](https://status-im.github.io/nim-beacon-chain/auditors-book/) to facilitate the programming language
- Lots of work done [to onboard validators](https://status-im.github.io/nim-beacon-chain/)
- Ongoing effort to document and debug codebase
- Working on proper fix for attestation stability. Expected fix in next few days

## 3.5 Prysm

- Revamping accounts key management
- New features: creating new account, listing new account
- Working on remote key store
- Started reference remote signer repo
- Working on integrating supernational BLS library into runtime. Working on cross compiling with the build
- Significant improvements to sync speed (2-3x improvement)
- Still addressing audit feedbacks
- Bug fixes
- UX support

## 3.6 Lighthouse

- Work on REST API
- Work on UI
- Integrating Blst, 65% speed increase
- Finalizing peer scoring system. Intoduced in different stages
- Reports of deadlock from Altona.
- Observed issue with attestation efficiency (high priority)
- Started work on slasher
- Refining database access atomicity
- Completed response to ToB audit. Will be public after applying fixes.
- Recieved proposals for second security review.

## 3.7 Teku

- Finished improvements on memory management. Memory usage is much more stable
- Now persisting protoarray to disk. Faster startup.
- Additionally made some peer management improvement for establishing connections
- Now prioritizing connections to get even exposure across attestation subnets
- Released small fixes to jvm libp2p
- Fixed issue with attestation gossip publishing
- [Fixed bug with producing invalid attestations](https://www.symphonious.net/2020/07/06/exploring-ethereum-2-the-curious-case-of-the-invisible-fork/)

# 4. Incident response

Video | [23:00](https://youtu.be/4IooxDX_GfU?t=1380)
-|-

A bug found in the spec. Which caused an incident.

Will be formalizing an incident response procedure, in the case something goes wrong when things go live.

- Emergency contact list
- Troubleshooting steps
- Etc.

Will start by making a working group. And learning from Eth1.

# 5. Weak subjectivity as it pertains to client security and UX

Video | [25:44](https://youtu.be/4IooxDX_GfU?t=1544)
-|-

- https://notes.ethereum.org/@adiasg/weak-subjectvity-eth2

Piece explaining how it works, in context of the spec and how it scales. Some recommendations on there on UX.

Weak subjectivity is required on Proof of Stake chains to prevent double spending.

The document is an introduction, and not a specification on what to do. It's what may go wrong, and how to prevent it.

1. Client side fork-choice handling of weak subjectivity
2. How we distribute these weak subjective states

New states are updated. When new clients go online, they download these states from somewhere. How this download happens, and where this download happens from.

4 possible paths were presented.

Regardless of the method, having the user be able to override may be important.

When we start achieving realistic adoption, the one week range may be a target for releases. Once 300-400 thousand validators, that period can be pushed to 2 weeks.

A user must get a recent checkpoint to the chain they want to sync in. What's the viable UX?

Concerns were brought up in terms of liabilities if a client were to sign-off on state.

One solution brought up was requiring multiple signatures across clients and the EF, creating a web of trust. This format would need standardization.

A first step may be a CL parameter which accepts the weak subjectivity checkpoint.

The goal is to start from a state, rather then from genesis.

This conversation will be continued in a new working group.


# 6. Research Updates

Video | [41:11](https://youtu.be/4IooxDX_GfU?t=2471)
-|-

## 6.1 TXRX

Onotole spec transpiler is being worked into Teku. Made a fully fledged simulator. 2 shards at 16 validators. Blocks and attestations are being produced on time. 320 epochs on the minimal config.

## 6.2 Vitalik

Thinking about if we can change the spec to allow easier verification of state transitions.

The challenge is looking at what is taking the most computing resources. The biggest are signature verification and the epoch processing. Can it work reduced or as a SNARK? Can you take, instead of a merkle tree, instead use Kate commitment to store validator balances? Every balance update becomes an eleptic curve addition. What level of efficiency can we get out of that.

A few routes are possible. The goal is to reduce complexity and make state transitions cheaper.


# 7. Networking

Video | [49:27](https://youtu.be/4IooxDX_GfU?t=2967)
-|-

There was an issue brought up. Do we need non-snappy request/response domainn? Seems people are leaning towards no. The decision is to not touch non-snappy until we recieve efficiency numbers. After then, a decision on non-snappy can be made.

Working on refining gossipsub parameters. Open PR.
- https://github.com/ethereum/eth2.0-specs/pull/1958

There is a modification to the GOODBYE message, to notify a message for why a disconnection happened. Wondering if to make a PR to the spec. PR to be made for client teams to comment. Adding a code will be useless if no one uses it.

Getting more visibility in gossip is going to be important. If someone is available to improve gossip. This could also be brought to a hackathon.


# 8. Spec Discussion

Video | [53:38](https://youtu.be/4IooxDX_GfU?t=3370)
-|-

Version 9 of hash to curve. For Eth2, if you support hash to curve 7, you support hash to curve 9.  

# 7. Open Discussion/Closing Remarks

Video | [57:14](https://youtu.be/4IooxDX_GfU?t=3434)
-|-

Eth2 Launchpad. Getting closer on standards for keystores and how to integrate it.
- https://github.com/ethereum/eth2.0-pm/issues/161

Client teams should be a run through of the Launchpad to check how it fits with client's workflow. This plans to be launched with the next testnet.

Also, on the client side, how it will be supported in their docs. On launchpad side, an outline and pointing to client docs.

------

# Annex


## Attendees


- Aditya Asgaonkar
- Alex Stokes
- Ansgar Dietrichs
- Ben Edgington
- Carl Beekhuizen
- Cayman
- Danny Ryan
- Edson Ayllon
- Grant Wuerker
- Hsiao-Wei Wang
- Jacob Sieka
- Jonathan Rhea
- Joseph Delonng
- Lakshiman Sankar
- Lion dappLion
- Mamy
- Martin Petrunic
- Mehdi (Sigma Prime)
- Meredith Baxter
- Nishant
- Protolambda
- Raul Jordan (Prysmatic)
- Sacha Saint-Leger
- Terence (Prysmatic)
- Vitalik Buterin
- Will Villanueva
- Zahary Karadjov



## Next Meeting Date/Time

Thursday, July 23, 2020.
