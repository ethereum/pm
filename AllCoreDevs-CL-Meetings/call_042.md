# **Ethereum 2.0 Implementers Call 42 Notes**

### **Meeting Date/Time: Thursday 2020/6/25 at 14:00 UTC**

### **Meeting Duration: 1 hr**

### [**GitHub Agenda**](https://github.com/ethereum/eth2.0-pm/issues/162)

### [**Audio/Video of the meeting**](https://youtu.be/P1AEmUt9ltg)

### **Moderator: Danny Ryan**

### **Notes: William Schwab**

--------------------


# **Contents**

- [1. Testing and Release Updates](#1-testing-and-release-updates)
- [2. Testnets](#2-testnets)
  - [2.1. Altona](#21-altona)
  - [2.2. Attack Nets](#22-attack-nets)
- [3. Client Updates](#3-client-updates)
  - [3.1 Prysm](#31-prysm-raul-jordan)
  - [3.2 Trinity](#32-trinity-grant-wuerker)
  - [3.3 Teku](#33-teku-cem-ozer)
  - [3.4 Lighthouse](#34-lighthouse-paul-hauner)
  - [3.5 Nethermind](#35-nethermind-tomasz-stanczak)
  - [3.6 Lodestar](#36-lodestar-cayman)
  - [3.7 Nimbus](#37-nimbus-mamy)
- [4. Research Updates](#4-research-updates)
- [5. Networking](#5-networking)
  - [5.1. Removal of non-snappy RPC](#51-removal-of-non-snappy-rpc)
  - [5.2. Yamux support](#52-yamux-support)
  - [5.3. Noise support/Secio](#53-noise-testing)
  - [5.4. Maximum Clock Parity Parmeter](#54-maximum-clock-parity-parameter)
- [6. Spec Discussion (none)](#6-spec-discussion)
- [7. Open Discussion/Closing Remarks (none)](#7-open-discussion-closing-remarks)

- [Summary of Action Items](#summary-of-action-items)

------------------------------

#
# **1. Testing and Release Updates**

| **Video** | [5:40](https://youtu.be/P1AEmUt9ltg?t=340) |
| --- | --- |

**Danny Ryan:** some new tests, new methods (gossip validation without state). Minor new release expected soon, maybe by Tuesday. Nothing too crazy.

**Protolambda:** Extending Rumor to do chain testing, provide smarter high-level commands, should sync tests more easily, also should make for easier benchmarking and easier ? test. Should make for easier integration into clients. reuse tooling. ? are coming along, first results are surfacing, if you have any feedback for the spec, please get in touch.

#
# **2. Testnets**

| **Video** | [8:07](https://youtu.be/P1AEmUt9ltg?t=487) |
| --- | --- |

## **2.1 Altona**

**Afr:** Have reached minimum deposits. Reached previously agreed genesis yesterday, but some invalid deposits have pushed off, new time perhaps Friday/Saturday, some discussion to push off the weekend to Monday, but no new proposed time yet. Other than that, Altona is ready to go. Afr is off on Monday, but is confident testnet can be launched without him. Afr does not currently control any of the validators

**Danny:** Minimum genesis would've been about eight hours ago, so we're just deciding on an offset from that? **Afr** agrees. **Danny** asks if a time should be proposed, it's agreed to pursue this on Discord after the call.

## **2.2 Attack Nets**

**Danny:** Circulated document outlying an idea for attack nets. The idea is creating testnets specifically to be attacked, as attackers are a specific subset of testing. Most users don't really care about attacking, care about how things will work in production. Once Altona reaches stability, select stable clients (maybe top 4, maybe all). Probably to start, will just have the EF spin up a few does, but out a few bounties. We can also attack these, which should be fun. Should allow for faster iteration. Can also bring in client teams, but current thought is to not put the extra burden on them. Idea is to have something up within the next two weeks or so, publicize, and to see who's interested.

**Terence:** Are clients supposed to support byzantine behavior via RPC endpoint? If yes, is there a spec or standard?

**Danny:** Not currently. True that opening up RPC connections can be insecure, but might not even have deposits available on these nets, and that the scope is more like DOS and other things not related to consensus. Over time would like to open up even to consensus, but not yet. Wouldn't mind seeing burden on the attackers.

**Protonlamda:** Another idea was to release sets of keys for parties that would like to attack, so that at first can only be attacked from a network platform, but as time goes by see higher and higher levels of degradation, see if it falls over.

**Danny:** reiterates EF will take the burden for now.

#
# **3. Client Updates**

| **Video** | [16:15](https://youtu.be/P1AEmUt9ltg?t=975) |
| --- | --- |

## **3.1 Prysm (Raul Jordan)**

- Completed audit from Quantstamp, focusing on patching up.
- Onyx: stable, 20K validators of which ~15% is Prysmatic
- Further optimizations
- Improvements to Slasher, uses flatmaps for historical ?
- Planning validator account revamp
- Focusing on stream duties, handling reorg better

## **3.2 Trinity (Grant Wuerker)**

- Beacon chain components to 0.11.3, getting up to date on 0.12.1
- Preliminary refactoring before fork-choice update
- Working on beacon node
- Performance issues anticipated before will be able to connect to Altona

## **3.3 Teku (Cem Ozer)**

- Replaced blocking code in RPC with non-blocking code, adopted BLS lib
- Changed number of blocks in memory
- Started work on storage efficiency
- 12.1 merged in anticipation of Altona

## **3.4 Lighthouse (Paul Hauner)**

- Working on Altona
- Almost ready to merge 0.12
- Rewrite of a library
- Refactor of fork choice
- Upgrading PM management with scoring
- Planning authentication scheme between UI and validator
- Augmented database
- Next steps: new Blast BLS library, implement API on bc, slasher, key management, looking to shift to more analysis

## **3.5 Nethermind (Tomasz Stanczak)**

- Improvements to deposit processing, beacon node, seems to be at a pre-processing level
- Work on finalizing coming up

## **3.6 Lodestar (Cayman)**

- 0.12 updates, almost there (need gossip-sub, which is about 85% complete)
- Probably won't be ready at Altona genesis, but aiming to be compatible with Altona
- Added part-time member
- Rewriting validator CLI

## **3.7 Nimbus (Mamy)**

- Getting ready for Altona
- Startup improved 20-100x by refactoring checking crypto keys
- Memory leaks fixed
- Backwards sync now faster than forward
- Fixed some bugs detected by beacon-fuzz
- Revolution of BLS backends
- 12.1 is default
- Networking: Progress on noise and gossip
- Can finalize on Onyx, also will be duplicating nodes to Witti and Altona

#
# **4. Research Updates**

| **Video** | [25:15](https://youtu.be/P1AEmUt9ltg?t=1515) |
| --- | --- |

**Aditya:** Writing doc about how subjectivity checkpoints are handled by clients. Idea is new nodes after genesis should sync from more recent state than genesis for security reasons, seems like 14 days is a good target, so will be standard in clients to release these checkpoint times, probably every 7-10 days or something like that. We need more conversations about how to distribute these checkpoints, will release some info into Discord, and will discuss further in next call.

**Danny** asks **Carl** about keystore, EIPs, standardization (in light of call about this).

**Carl:** Much clearer now, lots of new discussions. Trying not to push through anything unnecessary. Specifically, changes around 2333 has a breaking change (BLS v2 key mapping), changes to some other EIPs, relaxed requirements on path storage and withdrawal keys, which allows paths other than those recommended in the EIP. Finally, wrote stuff on keystores, handling Unicode passwords, uses same mechanisms as mnemonic generation, dependencies should already be present. Description field added to help users and validators.

**Danny:** Keystores vs. wallets from the client standpoint - was any conclusion or standard reached?

**Carl:** Keystores are the minimum that should be supported, more than that not required, 2335-style keystore should be the standard for storing keys (at a minimum). In terms of standards, would like to add to Eth2 specs in a similar vein to just to explain what is expected at a minimum, even if not strictly a part of the spec. There has been discussion about layout, but a description would be good, spec is a good place to put it.

**Vitalik:** About using gkr to approve hashes much more quickly (has posted to ethresear.ch), seems to be a good direction. Short and medium term relevance is in witness compression looking at polynomial commitments and ? for quite some time, might make SNARk and STARK Merkle proof more efficient again than other methods described. In terms of data size, seems to be much more efficient, goes down from about 100B to almost no overhead.

( **Dankard** raises security concerns (reusing algebraic hash function), says they are the main problem, **Vitalik** agrees, **Dankard** says not sure this is a good direction, but doesn't seem to affect the overall timeline (3-5 years for witness compression), **Vitalik** says could be, but there are middle options like Petersen hashes for the Merke tree too. Some discussion about Petersen.)

**LeoBSC:** Researching gossip, different kinds of attacks, posting research. Would be good if weird behavior is reported to LeoBSC regarding gossip. Danny points any good security issues to Leo.

**Joseph Delong:** Worked on validator de-anonymization, posted to Jonathan Rhea has been writing a series of posts called packetology to ethresear.ch. Still a rough draft, and can de-anonymize to correlate pub key to IP address. Also working on a phase 1 client using Alex's transpiler research.

#
# **5. Networking**

| **Video** | [37:45](https://youtu.be/P1AEmUt9ltg?t=2266) |
| --- | --- |

## **5.1 Removal of non-snappy RPC**

**Danny:** Raul mentioned in an issue that spec currently supports snappy and non-snappy, even though non-snappy removed from gossip. Does anyone have a usecase for leaving in non-snappy support? Or remember why the intent was to support both.

**Jacek Sieka:** Thinks intent was never to support non-snappy, was just a way to give time to client implementations. Also, even if removed, clients could still choose to support it. Also, never ran numbers on snappy. Seems that general feeling is that it's nice, but haven't really tested it,

**Protolambda:** For compression one argument is the attestation format which is still in bitfill, even though on ? there's really only one bit ?, so that compresses?

**Jacek:** Then you could argue that moving quick would also help with compression. Just saying that maybe we should just look at numbers to see if it's really worth it.

**Danny:** Does single pilot quick have compression built in? **Jacek** unsure.

Action items - run sanity test compression numbers - single user attestation, relatively full attestations, series of different blocks, make sure there are reasonable compression ratios. If so, drop support, and is already removed from gossip.

**Leo** would run numbers on this. **Danny** recommends taking a client, using their tests and producing objects. Numbers to be added to the issue on the spec about non-snappy support.

## **5.2 Yamux**

**Danny:** not everyone supports yamux. Interesting issues between Prysm and Lighthouse support. Easiest thing would probably be for Lighthouse to keep yamux disabled until it can be debugged.

**Jacek:** agrees that this is the state of affairs.

## **5.3 Noise Testing**

**Jacek:** When testing on witti, hard to find nodes to connect to, probably because people running nodes not updated to latest version. **Danny** recommends pointing to a specific version.

**Paul:** recommends taking to Discord. Lighthouse can't speak noise with Prysm at this point, cause unknown currently. **Jacek** agrees.

**Danny:** Is network primarily on Secio? General answer is yes, some discussion. **Jacek** says they want to disable Secio completely, but not doable now for general compatibility.

**Danny:** Will take to networking channel. Need to figure out if changes to noise spec are versioned, should push for versioning. Prysmatic probably has the most up-to-date versions, really doesn't want Secio to be enabled on mainnet.

## **5.4 Maximum Clock Parity Parameter**

**Jonathan Rhea:** asks about clock maximum disparity parameter, does anyone know what kind of verification should be used to validate that number (currently 500ms)

**Jacek:** increasing number seemed to help with performance, but is anecdotal.

**Jonathan:** Seems then like someattestations arrive sooner than expected, can ignore them by increasing this parameter.

**Jacek:** One of the gossip criteria is that the packet isn't too recent according to local clock. Can either queue packet or be reliant on local clock. Didn't want to build queue, so they rely on the clock. **Danny** urges on queue, some back and forth with **Jacek**.

**Jonathan:** Code agnostic to clock disparity, didn't see anything come in earlier than 500ms, but with everyone respecting, not surprising, but didn't necessarily see a reason for it either. Suggests GitHub issue, **Danny** agrees.

**Danny:** Are there any other constants like this lurking around? Suggests he should look for them.

#
# **6. Spec Discussion**

| **Video** |
 |
| --- | --- |

No discussion.

#
# **7. Open Discussion/Closing Remarks**

| **Video** |
 |
| --- | --- |

No discussion.

--------------------------------------

# **Appendix**

## **Summary of Action Items**

- Further discussion of Altona genesis to occur on Altona Discord
- Ben to perform sanity checks on snappy
- Discussion of Noise spec and seico to occur on Networking Discord
- Jonny to open issue to discuss clock disparity parameter

## **Resources Mentioned**

- [https://github.com/ethereum/eth2.0-pm/issues/1](https://github.com/ethereum/eth2.0-pm/issues/154)62
- [https://etresear.ch/t/using-gkr-inside-a-snark-to-reduce-the-cost-of-hash-verification-down-to-3-constraints/7550](https://etresear.ch/t/using-gkr-inside-a-snark-to-reduce-the-cost-of-hash-verification-down-to-3-constraints/7550)
- [https://github.com/leobago/BSC-ETH2](https://github.com/leobago/BSC-ETH2)
- [https://ethresear.ch/t/packetology-validator-privacy/7547](https://ethresear.ch/t/packetology-validator-privacy/7547)
- [https://github.com/ethereum/eth2.0-specs/issues/1931]

## **Attendees**

- Aditya Asgaonkar
- Afr Schoe
- Alex Stokes
- Ansgar Dietrichs
- Ben Edgington
- Carl Beekhuizen
- Cayman
- Cem Ozer
- Dankrad
- Danny Ryan
- Grant Wuerker
- Guillaume
- Hsiao-Wei Wang
- Jacek Sieka
- Jonathan Rhea
- Joseph Delong
- Leo BSC
- Mamy
- Nishant
- Paul Hauner
- Protolambda
- Raul Jordan
- Terence (prysmatic)
- Tomasz Stanczak
- Vitalik Buterin
- Zahary Karadjov

## **Next Meeting Date/Time**

Thursday, July 9, 2020.
