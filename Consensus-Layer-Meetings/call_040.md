# Ethereum 2.0 Implementers Call 40 Notes

### Meeting Date/Time: Thursday 2020/5/28 at 14:00 UTC
### Meeting Duration:  1 hr
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/154)
### [Audio/Video of the meeting](https://youtu.be/xvIk22HvTVE)
### Moderator: Danny Ryan
### Notes: Edson Ayllon


-----------------------------

# Contents

- [1. Testing and Release Updates](#1-testing-and-release-updates)   
- [2. Testnets](#2-testnets)   
- [3. Client Updates](#3-client-updates)   
   - [3.1 Lodestar](#31-lodestar)   
   - [3.2 Nimbus](#32-nimbus)   
   - [3.3 Teku](#33-teku)   
   - [3.4 Prysm](#34-prysm)   
   - [3.5 Lighthousee](#35-lighthousee)   
   - [3.6 Trinity](#36-trinity)   
   - [3.7 Nethermind](#37-nethermind)   
- [4. Research Updates](#4-research-updates)   
   - [4.1 TXRX](#41-txrx)   
   - [4.2 Quilt](#42-quilt)   
   - [4.3 EWASM](#43-ewasm)   
   - [4.4 Ethereum Foundation](#44-ethereum-foundation)   
- [5. Networking](#5-networking)   
- [6. Spec Discussion](#6-spec-discussion)   
- [7. Open Discussion/Closing Remarks](#7-open-discussionclosing-remarks)   

-----------------------------

# 1. Testing and Release Updates

Video | [4:18](https://youtu.be/xvIk22HvTVE?t=258)
-|-


`v0.12.0` released last week. Upgraded BLS to latest ITS standard. Fixed rewards and penalties. Some rewards and penalties modifications. Some network changes.

Large refactor to how rewards and penalties are tested. Much better coverage.

Fork-choice tests targeted for `v0.12.1`.

No update Stethoscope network testing. Two different testing paths:
- Rumor
- Stehoscope

Rumor works now. Stethoscope is a bigger effort that will take more time. Stethoscopes ties together test vectors in integrated clients.


# 2. Testnets

Video | [8:56](https://youtu.be/xvIk22HvTVE?t=536)
-|-

A couple attempts made to relaunch Schlesi testnet, revealing a couple of issues, eventually losing finality. The last Schlesi validator was shut down, making Schlesi officially shut down.

A couple of attempts made to launch a new testnet. The difference between Witti and Schlesi is 3 vs 2 clients at genesis, making Witti more difficult to launch.

The clients were Teku, Lighthouse, and Prysm with 2 validators each. There was a different genesis time for two clients. The launch was solved, and a successful launch was two nights before the call.

Witti has almost perfect liveliness on the network.

**Afr Schog:** I envision we launch as many testnets as possible whenever we see a reason to launch a new one. Let's have rather more small and fast failing testnets.

Testnet launch times may be adjusted. More concrete notes will be released on testnet plans.

- https://github.com/ethereum/eth2.0-specs/issues/1849

# 3. Client Updates

Video | [12:45](https://youtu.be/xvIk22HvTVE?t=765)
-|-

## 3.1 Lodestar

- Published new version of BLS library.
- Going through `v0.12` updates. Updating gossip subs.

## 3.2 Nimbus

- For networking, have been investigating and solving interop issues with Lighthouse.
- Published updated multinet script to the multinet repo. Can create a network from a split 50/50 Lighthouse Nimbus network.
- Realized gossip sub assumes we validate an attestation immediately when recieved, but in reality there has to be a wait for the block to be available.
- Witti added to the make file.
- Investing synching in Witti from Schlesi.
- Investigation includes few peers issue, where Nimbus only ad a couple peers while synching compared to other clients
- BLS changes merged.
- Toggle included to switch between `v0.11.3` and `v0.12` for testnet fuzzing purposes.
- Recieved audit proposals from auditing firm. Right now selecting vendors for audits.
- Unknown if running into synching bug on Witti as well.

## 3.3 Teku

- Started making official releases of Teku every 2 weeks with release notes.
- Teku updated with options to run on Witti.
- Gossip sub `v1.1` JVM libp2p implementation almost done.
- BLS updates under review
- Open API schemas updated to work easier with code generation tools.
- Updated Eth1 data handling logic to no longer need to query for world state data. Can run against fast synced Eth1 nodes without worrying about missing world state.
- Added peer filtering.
- Ongoing work to improve attestation processing.
- Fixed some JVM libp2p issues related to handling large stream packets.

## 3.4 Prysm

- Complete with `v0.12`.
- Positive results running testnets. 100% participation on different testnet configurations for `v0.12`.
- Planning a testnet restart for Topaz.
- Working on releasing memory improvements to master branch. Some experimental features with differing degrees of stability looking to be more stable to become defaults.
- Working on optimizing attestation aggregation.
- Good progress on slasher.
- Fuzz testing is going well.
- Audit from Quantstamp in progress.
- Able to look back all the way to genesis.


## 3.5 Lighthousee

- Started an audit with Trailbits on the consensus code.
- Networking code delayed, to finish underlying protocols.
- Debugging with Witti testnet launch.
- Found discv5 is chewing CPU. Started a structural rewrite of the discv5 implementation to fix.
- Still working on internal peer reputation system and updating to `v0.12`.
- Lighthouse's discv5 is from the current official libp2p library in Rust.

## 3.6 Trinity

- Added a fulltime contributor.
- Merged in a large networking PR for latest libp2p.
- Next step is working to sync Witti.
- Looking to update to `v0.12`.

## 3.7 Nethermind

- Built code for attestation.
- Code for connecting with database and merkle trees. Previously testing only using memory.
- Testing multiple validator onboarding soon with the new merkle tree code.
- Still updating code for `v0.11`.
- Moving Junior dev full-time to Eth2 for tests.
- Expanding C-sharp wrappers to have better control over connections.
- Senior dev who has experience with Rust and C sharp will be looking at improvements in June.
- Nethermind Eth1 to Nethermind Eth2 connectivity for whole flow.


# 4. Research Updates

Video | [24:29](https://youtu.be/xvIk22HvTVE?t=1469)
-|-

## 4.1 TXRX

Completed two write ups on Discv5.

- [Comparing discovery advertisement features by efficiency: ENR attributes and topic advertisement](https://ethresear.ch/t/comparing-discovery-advertisement-features-by-efficiency-enr-attributes-and-topic-advertisement/7448)
- [Discovery peer advertisement efficiency analysis](https://hackmd.io/@zilm/BJGorvHzL)

Onotole pyspec transpiler is not used for transpiling fork-choice tests, but fork-choice tests are being worked on as well separately.  Transpiles into Kotlin code.

Testnet analysis done. Results show breakdown of the Topaz network. Created a prototype tool for testnet analysis, autogenerated from CI job.

Working on upgrading network Agent to discv5 code for more efficient crawl.

Released write up on probalistic cross shard transaction simulations. Shows results on network throughput.

Working on moving to a pre-alpha cross-shard spec for the next coming weeks.

## 4.2 Quilt

Exploring account abstraction. Doing work on Geth to get into Eth1. If it doesn't move forward in Eth1, bringing it into the account model for Eth2 as a whole. Should have an MVP withinn a week or two.

Building tool to DOS the design. Looking at how the transaction and memepool can stand defensively.

## 4.3 EWASM

Continued work on Eth1.x 64. Next step is to look at the yanking. Tried implementing yanking as a layer one solution on Eth1.x 64 varient one. Searching if there is a need for protocol level support for yanking. Plans to prototype the protocol level yanking support.

For phase 2, if there is a standard witness format, there's a potential of introducing a shard committee cache. There would be a cache for transaction witnesses, a few epochs long. The block witness included by the shard blocks will always be full witnesses. The cache impact would be limited to block proposers.

This idea could be applied to Eth1.x or stateless Ethereum.

## 4.4 Ethereum Foundation

Looking at making sure Phase 1 spec is well tested, well structured, and has needed components for prototyping an implementation.


# 5. Networking

Video | [34:41](https://youtu.be/xvIk22HvTVE?t=2081)
-|-

**Jacok Sieka**: The question to decide is whether to support version 1.0. In theory they're compatible.

**Danny Ryan**: It was written in a way that v1 and v1.1 must be supported. For the time being, we'll see a mix on the testnets. There's no need to go to production without it.

Discussing change on Discv5 before finalizing the spec.
- https://github.com/ethereum/devp2p/issues/152

Looking into the proposal [Comparing discovery advertisement features by efficiency](https://ethresear.ch/t/comparing-discovery-advertisement-features-by-efficiency-enr-attributes-and-topic-advertisement/7448). The proposal may bring short term gain, but must answer the question if it is a sound proposal. Fear is an issue where you can't find 100% of nodes with this. Discovery would go down as the network grows. Looking on how to turn it into a sound proposal.

Discussion is around the use of QUIC. There's an idea to reuse the QUIC packet format.

Looking to make a decision on the Wire protocol this week.

A reason why QUIC isn't supported is because TLS 1.3 support isn't widespread. The proposal is to mask the discovery packets as QUIC so it's not blocked by a firewall for example.

Starting to work with the Geth team for a test suite on discovery.

**Age Manning**: There were other changes including having fine distances in the find node requests. Is that still considered?

**Felix**: Yes. The changes coming to the final version are:
- Complete description of session cache
- Change to version number
- Multi-distance final request
- Connection for pre-negotiation request
- Topic discovery is marked as draft, but everything else will not be
- New encoding

**Age Manning**: It looks like many are on board. We should open a PR to match that. The other question is, Eth1 is moving to Discv5. Is Eth1 connecting peers using ENRs?

**Felix**: On the command linne?

**Age Manning**: Setting boot node. Having one node connect to another node.

**Felix**: ENR isn't the most readable for humans. We mostly use the DNS based ENR mechanism for bootstraping. When moving to Discv5, will mostly be the same. Will keep the DNS. Probably going to setup a new DNS tree to find entry points. Can still use enode URL format, great, but inflexible. Not the most convenient if you want to type something in.

**Age Manning**: To connect, you actually have to have the ENR, right?

**Felix**: There is a way to connect if you have the public key, ip address, and the port. We could make another version of that if a readable representation is needed.

**Age Manning**: Unsigned, correct?

**Felix**: They can't be signed. My recommendation is to go with the multi-addr, since it's being used anyways, for the readable. But when it comes to pasting nodes to code, use the ENR, to prove to everyone there's no cheating.

**Danny Ryan**: A standard multi-header that ensures having the public key satisfies our requirements.

**Felix**: Yes, you must have the public key. I am thinking of adding an ENR identity scheme using Ed25519 as it's much faster doing the handshake.

**Zahary Karadjov**: In Nimbus we tried to implement the initial version of Discv5 to accept both multi address and enode records. This proved to be too difficult. You need the signed ENR of all the nodes you are talking with.

**Felix**: For supporting the protocol, you can't skip on ENR.

**Zahary Karadjov**: Exactly. What I envision here is that perhaps it would be neccessary when connecting to a node to ask its own ENR record, which would be signed. If you don't know the signed ENR record of any node you talk with, you cannot reply to some of the messages. If you connect with multi-address or enode, you should recieve an ENR record.

**Age Manning**: You need to know the ENR at some point, or you run into trouble.

**Felix**: You don't need to know theirs. You just need to send yours. If there is something in the spec preventing using multi addr during the initial connection, we should fix that.



# 6. Spec Discussion

Video | [53:38](https://youtu.be/xvIk22HvTVE?t=3218)
-|-

Contact Danny with any issues related to `v0.12`.

# 7. Open Discussion/Closing Remarks

Video | [54:04](https://youtu.be/xvIk22HvTVE?t=3244)
-|-

No discussion


------

# Annex

## Resource Mentioned

- https://github.com/ethereum/eth2.0-pm/issues/154
- https://github.com/ethereum/eth2.0-specs/issues/1849
- https://ethresear.ch/t/comparing-discovery-advertisement-features-by-efficiency-enr-attributes-and-topic-advertisement/7448
- https://hackmd.io/@zilm/BJGorvHzL
- https://txrx-research.github.io/prkl/testnet-analysis.html
- https://github.com/TXRX-Research/prkl
- https://twitter.com/JonnyRhea/status/1263151048199372801?s=19
- https://ethresear.ch/t/cross-shard-transaction-probabilistic-simulation/7474
- https://github.com/ethereum/devp2p/issues/152

## Attendees

- Aditya
- Age Manning
- Alex (axic)
- Alex Stokes
- Ben Edgington
- Carl Beekhuizen
- Cayman
- Chih-Chen Liang
- Danny Ryan
- Felix
- Grant Wuerker
- Hsiao-Wei Wang
- Jacob Sieka
- Jonathan Rhea
- Joseph Delonng
- Lakshiman Sankar
- Leo BSC
- Mamy
- Martin Petrunic
- Meredith Baxter
- Nishant
- Protolambda
- Raul Jordan
- Terence (prysmatic)
- Will Villanueva
- Zahary Karadjov

## Next Meeting Date/Time

Thursday, June 11, 2020.
