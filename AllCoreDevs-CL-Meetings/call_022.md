# Ethereum 2.0 Implementers Call 22 Notes

### Meeting Date/Time: Thursday July 25, 2019 at [14:00 GMT](http://www.timebie.com/std/gmt.php?q=14)
### Meeting Duration: 45 min
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/64)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=ReSiB2940AE)
### Moderator: Danny Ryan
### Scribe: Brent Allsop

## Agenda

- [1. Testing Updates](#1-testing-updates)
- [2. Client Updates](#2-client-updates)
- [3. Research Updates](#3-research-updates)
- [4. Network](#4-network)
- [5. Spec Discussion](#5-spec-discussion)
- [6. Open Discussion/Closing Remarks](#6-open-discussionclosing-remarks)


## 1. [Testing Updates](https://www.youtube.com/watch?v=ReSiB2940AE&t=65)

**Diederik Loerakker(@protolambda)** started looking into testing problems. There are memory problems for some clients who can't handle the bigger mainnet tests, so they're splitting them up. He posted the issue and a survey with results here: https://github.com/ethereum/eth2.0-specs/issues/1311#issuecomment-515015182 He's hoping to have solutions implemented by the end of this week.

## 2. [Client Updates](https://www.youtube.com/watch?v=ReSiB2940AE&t=180)

**Terence Tsao (Prysmatic Labs, @terenc3t)** We're getting runtime to align with the spec-freeze version. Getting to run single client with a single beacon node with 64 validators smoothly. Debugging sync-related issues. Optimizing SSZ communication that is currently slow. Implemented a  an Eth1 data mach server. Can run without changing Prysm code.  

**[Wei Tang (Parity)](https://www.youtube.com/watch?v=ReSiB2940AE&t=238)** Passed all the tests for 0.8. Have a node that is able to send attestations and proposed blocks. Now doing some refactoring.

**[Joseph DeLong (Artemis)](https://www.youtube.com/watch?v=ReSiB2940AE&t=276)** Completed 0.8 update. Patching to 0.8.1. Working on reference tests. Working with Whiteblock at Prysm to make sure their Eth1 Mach RPC client is able to generate deposits that can output to YAML and then we'll intake those YAML deposits to generate a genesis state that's the same as Prysmatic.  

**[Mikhail Kalinin (Harmony)](https://www.youtube.com/watch?v=ReSiB2940AE&t=323)** Have completed their update to 0.8 spec. Biggest problem was with SSZ with bit lease and bit vector and sparse Merkle trees. Passed all tests. Making progress on libp2p. Continuing research on attestation aggregation because of potential issues with attestation delivery. Hiring a QA engineer.

**[Mamy Ratsimbazafy (Nimbus)](https://www.youtube.com/watch?v=ReSiB2940AE&t=432)** Implemented most of 0.8.1 except SSZ. Completed most of the testing of state transition functions. Found some issues with justification and finalization. They have an open PR currently being reviewed to bootstrap genesis through Web3.

Libp2p test stand has been running for two weeks. Updated the build so you can now run mage and have automated installation of the go-lib2p2-daemon. Developing support library to focus on metrics for Ethereum 2. Can sync about 400,000 blocks per hour until blockshare 1.3 million and then we have some issues.

Hired Andre Lim, who has been working as a long-time bounty contributor for a year, to maintain Ethereum 1.  

**[Hsiao-Wei Wang (Trinity)](https://www.youtube.com/watch?v=ReSiB2940AE&t=550)** Close to passing minimal test vector for 0.8.1. Mainnet test vector still pending. Still working on Python libp2p implementation. Making progress on discv5 implementation.

**[Greg Markou (Lodestar)](https://www.youtube.com/watch?v=ReSiB2940AE&t=627)** Everything is passing for 0.8.1 at this point. Prepping for moving forward with more tooling. By the end of the week, they'll be able to NPM install SSZ types and config params.

Also possible to individually import all the early material to help for dev tooling. Doing refactors on codebase to make it more modular and easier to import.

**[Luke Anderson (Lighthouse)](https://www.youtube.com/watch?v=ReSiB2940AE&t=693)** Up to date with 0.8.1 tests except for genesis (no runner yet). May have found an issue in the spec about get start shards - posted [issue 1315](https://github.com/ethereum/eth2.0-specs/issues/1315) about that.

Introduced chaos monkey and have seen good results in network stability.

Libp2p implementation updated to the latest proposal.

Working on implementation details and getting ready for Interop, Have a new resource that just started working full time. Making efficiency gains in data storage. Fleshed out API spec to be similar with other clients, working towards Interop. Working to make sure our rust-libp2p works well with the go-libp2p implementation. Reviewing PR submitted by Quilt team re: issue with SSZ.

**[Yeeth (not present)](https://www.youtube.com/watch?v=ReSiB2940AE&t=800)**

**[Musab Alturki (K Team Formal)](https://www.youtube.com/watch?v=ReSiB2940AE&t=815)** Still working on doing the translation of the specification in K - now looking into specifying the merkleization operation in K as well. Nothing fundamentally difficult there.

## 3. [Research Updates](https://www.youtube.com/watch?v=ReSiB2940AE&t=929)

**Vitalik Buterin(EF/Research)** Working a lot on Phase 1 specification. Nailing down the persistent committee structure. Settled on an approach where the entire persistent committee signs every block and has a size that's capped at 128 and that we show holds in a staggering pattern once every day. This is stable and consistent with persistent committee design.

Also looked at crosslink data structure with all of the fix-sized headers first, with variable-sized block bodies next. Advantage is that you can still access shard block data from inside the header.  

Updating the light client protocol. Making it efficient and secure and improving performance. Download one period committee that is merklehashed into the header. Those blocks point to beacon blocks to figure out updates to the state of any particular shard.

SSZ partials - made a proposal for canonical ordering for hashes in an SSZ partial object

How rewards and penalties work is the last thing to work on.

**[Wei Tang](https://www.youtube.com/watch?v=ReSiB2940AE&t=1222)** asked if it would be possible to make the tree hash root of the merkle partial be the same as the full merkle root?

**Vitalik Buterin** said it is theoretically possible by making a custom SSZ type, but so far he hasn't moved into that direction because it would be more difficult and would add more complexity.

**[Wei Tang]** has a Rust data structure that could potentially accomplish that. Both agreed it was worth further consideration.

**[Matt Garrett](https://www.youtube.com/watch?v=ReSiB2940AE&t=1372)** asked how are you currently storing general indices, especially those larger than U256?

**Vitalik Buterin** said we shouldn't be storing indices when they are part of the partial itself because that's not what we do for merkle proofs, and there are a lot of cases where you should not need to be serializing the set of indices because they can be calculated in real time based on the path.

### 3.1 [Other Research Updates](https://www.youtube.com/watch?v=ReSiB2940AE&t=1531)

**Diederik Loerakker(@protolambda)** mentioned a gap in the Phase 0 research that potentially reduces the size from 70 gigs to 2.5 gigs for 8 months of data.

**[Mikhail Kalinin](https://www.youtube.com/watch?v=ReSiB2940AE&t=1579)** asked about finality of crosslinks in Phase 0.

**Danny Ryan** said we will address this when we simplify the mechanism in the next couple of months. Because this data is stubbed in Phase 0, this is not a pressing issue.

**[Matt Garrett](https://www.youtube.com/watch?v=ReSiB2940AE&t=1637)** provided updates from Quilt. John Adler [posted a document](https://ethresear.ch/t/open-research-questions-for-phases-0-to-2/5871) to ethresearch compiling questions that need to be researched for Eth 2.0.

Just completed implementation of SSZ partials in Rust.

They've come up with a plan for for implementing a harnessed single shard phase 1 and 2 engine on top of Lighthouse that will implemented in the next few weeks. Bringing someone in to address questions that are lingering about relays and b markets.

**[Carl Beekhulzen](https://www.youtube.com/watch?v=ReSiB2940AE&t=1735)** has been working on deposits. If EF will do this in a more centralized manner it will give everyone a common set of tools to use. Client software will have to ingest validator keys. Trying to come up common standards. Using what works in Eth 1. More complexities arise for how to do deterministic auths to get the keys out of the key tree. Has some new proposals he's working on.

## 4 [Networking](https://www.youtube.com/watch?v=ReSiB2940AE&t=1871)

**Danny Ryan** There is an open standardization PR. Hope to get it locked down within the next 5 days. Lighthouse still working on that.

**[Raúl Kripalani (Protocol Lab)](https://www.youtube.com/watch?v=ReSiB2940AE&t=1923)** Noting major of note. Approved new grants for Nim-libp2p. Helping teams as needed.

**[Antoine Toulme](https://www.youtube.com/watch?v=ReSiB2940AE&t=1923)** Artemis is in Los Angeles working with Prysm on a cold start simple script to simulate the genesis event. Agreed on a simple set of tests they are developing.

## 5 [Spec Discussion]((https://www.youtube.com/watch?v=ReSiB2940AE&t=2078))

**Danny Ryan** mentioned the possibility of an update with minor fixes next week and asked people to push additional questions upstream to the [eth2.0-pm repository](https://github.com/ethereum/eth2.0-pm).

## 6 [Open Discussion]((https://www.youtube.com/watch?v=ReSiB2940AE&t=2173))

**Danny Ryan** discussed [a proposal for Lodestar funding](https://molochdao.com/proposals/81) that would give Lodestar three months of runway. Solicited Moloch support.

# Attendees

- [Adrian Manning (Lighthouse/Sigma Prime)](https://github.com/AgeManning)
- [Alex Stokes (Lighthouse/Sigma Prime)](https://github.com/ralexstokes)
- [Antoine Toulme](https://github.com/atoulme)
- [Benjamin Burns](https://github.com/benjamincburns)
- [Brent Allsop (Canonizer)](https://github.com/BrentAllsop)
- [Carl Beekhuizen (EF/Research)](https://github.com/CarlBeek)
- [Chih-Cheng Lia](https://github.com/ChihChengLiang)
- [Daejun Park (RV)](https://github.com/daejunpark)
- [Daniel Ellison(Consensys)](https://github.com/zigguratt)
- [Danny Ryan](https://github.com/djrtwo)
- [Diederik Loerakker (EF)](https://github.com/protolambda)
- [Greg Markou](https://github.com/GregTheGreek)
- Guillaume
- [Hsiao-Wei Wang (Trinity)](https://github.com/hwwhww)
- [Jacek Sieka](https://github.com/arnetheduck)
- [Jannik Luhn](https://github.com/jannikluhn)
- [John Adler](https://media.consensys.net/@adlerjohn)
- [Joseph Delong](https://github.com/dangerousfood)
- [Kevin Main-Hsuan Chia](https://github.com/mhchia)
- [Luke Anderson (Lighthouse/Sigma Prime)](https://github.com/spble)
- [Mamy Ratsimbazafy (Nimbus/Status)](https://github.com/mratsim)
- [Marin Petrunic](https://github.com/mpetrunic)
- [Matt Garnett](https://github.com/c-o-l-o-r)
- Mehdi | Sigma P
- [Mikerah](https://github.com/Mikerah)
- [Mikhail Kalinin (Harmony)](https://github.com/mkalinin)
- [Musab Alturki](https://github.com/malturki)
- [Nicholas Lin](https://www.linkedin.com/in/nicholas-lin-50267ba3/)
- [Nishant Das](https://github.com/nisdas)
- [Paul Hauner](https://github.com/paulhauner)
- [Raul Jordan](https://github.com/rauljordan)
- [Raúl Kripalani](https://github.com/raulk)
- [Shahan Khatchadourian](https://github.com/shahankhatch)
- Terence Tsao (Prysmatic Labs, @terenc3t)
- [Trenton Van Epps](https://medium.com/@trenton.v)
- [Vitalik Buterin(EF/Research)](https://vitalik.ca/)
- [Wei Tang (Parity)](https://github.com/sorpaas)
