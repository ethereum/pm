# Ethereum 2.0 Implementers Call 24 Notes

### Meeting Date/Time: Thursday August 29, 2019 at 14:00 GMT
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/73)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=sz87_i5Uy1I)
### Moderator: Danny Ryan
### Scribes: Ben Edgington, Mamy Ratsimbazafy & Brett Robertson

----------

## Agenda

- [1. Testing updates](#1-testing-updates)
- [2. Client updates](#2-client-updates)
- [3. Research updates](#3-research-updates)
- [4. Network](#4-network)
- [5. Open Discussion/Closing Remarks](#5-open-close)
- [6. Spec Discussion](#6-spec-discussion)

## 1. Testing Updates
[Timestamp 5:38](https://youtu.be/sz87_i5Uy1I?t=338)

**Danny**:
v0.8.3 released last week. No substantive changes from v0.8.2, but there are some more tests.

**Protolambda**: Get in touch this week if you are having any difficulty with the tests.


## 2. Client Updates
[Timestamp 7:36](https://youtu.be/sz87_i5Uy1I?t=456)

### Nimbus
[Timestamp 7:39](https://youtu.be/sz87_i5Uy1I?t=459)

**Mamy**:
Berlin news: https://our.status.im/nimbus-berlin-update/
Documentation: https://nimbus-libs.status.im/#get-started
Revamped build system, can directly use nim-beacon-chain instead of going through Nimbus
Validator deposits from Eth1 almost done
Solved most justification and finalisation issues
Merged big PR for state tests - focus on passing tests for interop
CI is very slow currently; needs optimising
Working on cryptography benchmarks
Can have 2000 validators on a single laptop
Networking: interop with Rust libp2, did gossipsub with Lighthouse. Using Go daemon.

### Artemis
[Timestamp 11:03](https://youtu.be/sz87_i5Uy1I?t=661)

**Shahan**:
Interop is primary focus
Ref tests: SSZ tests for 0.8.2/3 looking good
Networking: Mothra - wrapped Rust libp2p
Beaconchain start tooling
Productisation: Prometheus metrics adaptors etc.
Collaborations with Whiteblock, and Handel team (for network aggregation)
Currently benchmarking BLS and aggregation

### Prysmatic
[Timestamp 13:29](https://youtu.be/sz87_i5Uy1I?t=809)

**Terence**:
 New DB and new fork choice. Working nicely.
Implementing initial sync
Regular sync, gossipsub, discv5 looking good
Getting to 0.8.2 for Interop
Working on lightclient, and slashing detection algorithm

### Lighthouse
[Timestamp 14:54](https://youtu.be/sz87_i5Uy1I?t=894)

**Paul**:
- Upgraded to latest network spec
- Debugged Go/Rust libp2p compatability with Nimbus
- Implemented Vitalik’s fast BLS verification scheme
- Cold/Hot DB nearly done
- Proposal for standardising RPC APIs

### Harmony
[Timestamp 16:11](https://youtu.be/sz87_i5Uy1I?t=971)

**Dmitrii**:
- Passing all v0.8.3 tests. Updating tests was laborious; hopefully not too many more changes in future
- For interop, libp2p integration and discovery to be integrated next week
- New attestation pool implemented
- Not sure about visas for interop, but hoping at least one can attend from the team

** Danny**: Don’t worry too much about discovery, we will mostly use static links for Interop initially

### Trinity
[Timestamp 18:42](https://youtu.be/sz87_i5Uy1I?t=1122)

**Hsiao-wei Wang**:
- Interop focus again
- Updating tests to v0.8.3
- Work on interopation with Go libp2p
- Hash tree root caching optimisations



### Lodestar
[Timestamp 20:18](https://youtu.be/sz87_i5Uy1I?t=1218)

**Cayman**:
- SHA256 assembly script implementation now well optimised.
- Interop: quick-start is done; getting libp2p up to spec
- Basic Prometheus monitoring in place
- Now aggregating public keys in signature verification, which is much faster



### Parity

Not present.


### Yeth

Not present

## 3. Research Updates
[Timestamp 22:16](https://youtu.be/sz87_i5Uy1I?t=1335)

**Vitalik**:
[Timestamp 22:25](https://youtu.be/sz87_i5Uy1I?t=1345)

- Karl’s [blog post](https://medium.com/plasma-group/ethereum-smart-contracts-in-l2-optimistic-rollup-2c1cef2ec537) yesterday on roll-up semi-layer 2 protocols; V publishing [a follow-up](https://vitalik.ca/general/2019/08/28/hybrid_layer_2.html) today. Relevant to Eth2 execution environments.

[Timestamp 30:57](https://youtu.be/sz87_i5Uy1I?t=1857)
- [Issue #1340](https://github.com/ethereum/eth2.0-specs/issues/1340): simplifying epoch transitions. A possible change to the protocol to handle the case of many skip slits between block and its parents, which is currently expensive. Makes empty epochs O(1) to validate.


**Justin**:
[Timestamp 23:11](https://youtu.be/sz87_i5Uy1I?t=1391)

- Doing a detailed review of Ph1
- A couple of substantive changes to Ph0 coming out of this: fork choice fix, and universal slashing condition for equivocation.
- Ph1 spec target Sep 30 for completeness (but not frozen)
- Looking at a SNARK proof system called “plonk”. Universal and updatable trusted set-up: a single set up is usable for all the circuits. A continual ceremony: only a single person (e.g. yourself) needs to be honest for it to work. Much better performance than SONIC. Aztec is starting a ceremony in September. Might make it practical to start using SNARKs at the consensus layer: many potential applications.
- Also looking at Ph1 spec
- Thinking about “Herd immunity” on libp2p

**Jacek (Status)**:
[Timestamp 27:15](https://youtu.be/sz87_i5Uy1I?t=1635)
- Concern about not validating messages: can be an amplification DoS vector. Can nodes validate only a subset of messages?

**Nicholas**:
[Timestamp 27:53](https://youtu.be/sz87_i5Uy1I?t=1673)

- Can now prove poly-log communication complexity of Handel aggregation protocol
- Handel is designed for large committees, but will also work for small committees and brings advantages in privacy
- Privacy: would be good to break the mapping between IP address of a validator and its Public - Key (which is currently easy to discover). Published a technique yesterday on [ethresear.ch](https://ethresear.ch/t/anonymity-a-zkp-to-remove-the-mapping-ip-address-wallets-public-key-of-a-validator/6049) that uses a ZKP to obscure the mapping.

**Protolambda**:
[Timestamp 32:46](https://youtu.be/sz87_i5Uy1I?t=1966)

- Spent time at EthBerlin with Quilt team on SSZ multiproofs and partials. Invitation for anyone interested to get involved.

**Musab**:
[Timestamp 33:32](https://youtu.be/sz87_i5Uy1I?t=2012)

- Excited about prospect of proving safety and liveness properties of the protocol.
- Compiler fix to Vyper has been merged to fix the issue found by Runtime Verification.


## 4. Network
[Timestamp 35:18](https://youtu.be/sz87_i5Uy1I?t=2118)

**Raul (Protocol Labs)**:

Received some interesting contributions at EthBerlin for Eth2.0 (see chat for links)
- Wireshark dissectors (that can decrypt). Should be useful for Interop.
- Noise handshakes. Implementation in Go as reference implementation.

**Protolambda**:
- Test harnesses and benchmarking on the gossipsub Go reference implementation
- Meshsim tool for analysing gossipsub networks

### API Repo
[Timestamp 41:13](https://youtu.be/sz87_i5Uy1I?t=2473)

**Paul**:

- New [Eth2 API repo](https://github.com/ethereum/eth2.0-apis): will contain APIs that are generally agreed upon by a number of clients. These are not consensus critical, but some conformity is desirable for users. Will evolve over time.
- Input from [Lighthouse](https://github.com/ethereum/eth2.0-APIs/pull/3)
- Prysm has collected requirements from users of their testnet to guide their API. Can move spec into the ethereum repo. Like protocol buffers due to their rigid definition. Can generate documentation directly from this.
- Question as to whether protobufs can handle all the types we require (e.g. fixed length arrays). - Prysm says they have had no problems so far with protobufs. However, Danny recommends not specifying protobufs as a dependency in this repo.


## 5. Open Discussion/Closing Remarks

### Interop retreat
[Timestamp 51:35](https://youtu.be/sz87_i5Uy1I?t=3095)

- Whiteblock/Protolambda sent out a detailed survey to gauge clients’ readiness. All clients responded.

- 0.8.2 will be the target version. Some bottlenecks with networking, but everybody seems close to having functional network stack now. Secio is implemented by most/all. One issue may be network syncing. Also need to review the existing wire protocol.

- Communication between client teams: Set up groups around specific topics to help each other out. Further news to come on Monday: aggregate results of where clients are with respect to features. To be actively maintained as clients progress.

**Danny**: Half the teams don’t have the capability to gossip attestations. This may limit how interesting the tests can get. Recommend teams implement this as a priority.

- NB Beacon Chain coordinated start is also important. Should we start from Genesis only, or any arbitrary point? Genesis is minimum, however there are debug opportunities we might miss if we can’t start at a recent finalised state.

- Discussion of file formats (SSZ or YAML) for sharing the states. Noone objected to SSZ format, so going ahead with that. Facility to dump state into SSZ for debugging will be useful. https://simpleserialize.com from Chainsafe - will be updated to latest spec. A command-line version of this would be useful.

- Plenty of planning/coordination to come over the next week.

- Raul recommends all teams running 1-1 smoke tests of libp2p ahead of arriving at Interop. These will be the initial tests at Interop; getting ahead would be good. A common doc with instructions how to run each others’ clients would help.


## 6. Spec discussion
[Timestamp 1:12:53](https://youtu.be/sz87_i5Uy1I?t=4373)

- Protolambda has written up [lots of client optimisations](https://github.com/protolambda/eth2-impl-design).

## Attendees

* Alex Stokes (Lighthouse/Sigma Prime)
* Antoine Toulme
* Ben Edgington (PegaSys)
* Benjamin Bur
* Brent Allsop
* Brett Robertson
* Cayman
* Cem Ozer
* Chih-Cheng Liang
* Daniel Ellison (Consensys)
* Dankrad
* Danny Ryan (EF/Research)
* Diederik Loerakker/Protolambda (EF)
* Dmitrii (Harmony)
* Hsiao-Wei Wang
* Ivan Martinez
* Jacek Sieka (Status/Nimbus)
* Jannik Luhn (Brainbot/Research)
* Jay Welsh
* Jonny Rhea (Pegasys)
* Joseph Delong (PegaSys)
* JosephC
* Justin Drake
* Kevin Mai-Hsuan Chia
* Leo (BSC)
* Luke Anderson (Lighthouse/Sigma Prime)
* Mamy Ratsimbazafy (Nimbus/Status)
* Marin Petrunic
* Mike Goelzer (libp2p)
* Mikerah (ChainSafe)
* Musab
* Nicolas Liochon
* Paul Hauner
* Preston van Loon
* Raul Jordan (Prysmatic Labs)
* Raúl Kripalani (Protocol Labs)
* Shahan Khatchadourian
* Steven Schroeder
* Terence Tsao (Prysmatic Labs)
* Vitalik Buterin (EF/Research)
* Zak Cole (Whiteblock)
