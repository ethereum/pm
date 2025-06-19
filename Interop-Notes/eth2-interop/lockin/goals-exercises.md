# Interop Multi-client Goals and Exercises

## Table of contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Interop Multi-client Goals and Exercises](#interop-multi-client-goals-and-exercises)
  - [Table of contents](#table-of-contents)
  - [Goals](#goals)
  - [Minimum multi-client requirements](#minimum-multi-client-requirements)
  - [1-on-1 multi-client exercise](#1-on-1-multi-client-exercise)
    - [Exercises](#exercises)
  - [Beyond](#beyond)
  - [Peripheral projects](#peripheral-projects)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Goals

* 1-on-1 testnets with all [minimum spec conformant clients](#Minimum-multi-client-requirements)
* Iron out methods for easy quickstarts
* Improve documentation for running clients (other teams are your first alpha testers!)
* Document any non-conforming issues and hurdles that arise during process and solutions
* Document any potential issues with core specs
* General network monitoring techniques and tools
* General network debugging techniques and tools

## Minimum multi-client requirements

The following are the minimum requirements a client must meet to begin multi-client testing. Clients that have not yet met these requirements should work towards doing so before pairing off. Please update the [survey results](./survey-results.md) as the answers to these questions change.

* 1.1: must target v0.8.2+
* 2.1: must support libp2p interop subset
* 2.3: must support static peering
* 2.4: must support network spec handshake
* 2.6: must support network spec wire protocol
* 2.7: must be able to run single client testnet
* 7.1: must pass all v0.8.2+ spec tests
* 13.1: must pass all v0.8.2+ ssz static tests
* 14.1: must pass bls v0.8.2+ tests
* 15.1: must support loading genesis from SSZ

## 1-on-1 multi-client exercise

Clients that have met the minimum requirements will pair off to work through 1-on-1 testnet exercises. In addition to the minimum client requirements, underlying libp2p implementations of the two clients _should_ run smoke/sanity tests.

It is incredibly important for clients to document their progress, any issues that arise during this process (non-comforming components, coordination issues, debugging nightmares, etc), and the solutions that they employ to address these issues. Each 1-on-1 pair should create markdown document entitled `"<Client-A> / <Client-B>"` for this purpose and link to it [here](https://notes.ethereum.org/b59YO_mqQJOn0FddqzWnbg). Please use this [template](https://notes.ethereum.org/UVOrrrgeT_KuEy2vWbppfQ) as a base, but expand upon as necessary. For ease of use, we'll keep the logs outside of git for now and might add after the session.

All initial interop testing is to be performed with the [`minimal`](https://github.com/ethereum/eth2.0-specs/blob/master/configs/minimal.yaml) network configuration.

### Exercises

Perform the following exercises, documenting your experience.

Exercises labeled `[single]` should first be run within a single machine and then run again on separate machines before moving on to subsequent exercises. All other exercises should be run on a minimum of 2 machines (ideally 1 machine per node).

Exercises labeled `[swap]` should be run with each participating client in each role (`A` vs `B`).

1. `A` peers and opens stream with `B` _[single]_ _[swap]_
2. Kickstart with 16 validators on a coordinated start of two nodes (one `A`, one `B`) _[single]_ _[swap]_:
    - `A` runs all validators
    - `B` listens to gossip and follows head
    - Static peer `A` to `B`
    - _Goal_: `B` sees epoch 8 as finalized
3. Kickstart with 32 validators on a coordinated start of two nodes (one `A`, one `B`) _[swap]_:
    - `A` runs all validators
    - `B` listens to gossip and follows head
    - Static peer `A` to `B`
    - _Goal_: `B` sees epoch 8 as finalized
4. Kickstart with 16 validators on a coordinated start of two nodes (one `A`, one `B`):
    - `A` runs 8 validators
    - `B` runs 8 validators
    - Static peer `A` to `B`
    - _Goal_: both `A` and `B` see epoch 8 as finalized
5. Kickstart with 16 validators on a coordinated start of four nodes (two `A`, two `B`):
    - `A-0` and `A-1` each run 4 validators
    - `B-0` and `B-1` each run 4 validators
    - Static peer `A-0` to [`A-1`, `B-1`]
    - Static peer `B-0` to [`A-1`, `B-1`]
    - _Goal_: all 4 nodes see epoch 8 as finalized
6. Kickstart with 32 validators on a coordinated start of four nodes (two `A`, two `B`):
    - `A-0` and `A-1` each run 8 validators
    - `B-0` and `B-1` each run 8 validators
    - Static peer `A-0` to [`A-1`, `B-1`]
    - Static peer `B-0` to [`A-1`, `B-1`]
    - _Goal_: all 4 nodes see epoch _128_ as finalized
    - _Bonus_: if either client supports sync from genesis in an running network, attempt to add an additional client ~10 epochs into the exercise. Success if sees epoch _128_ as finalized with the other nodes.

## Beyond

The initial 1-on-1 exercises are designed to be simple and generally achievable. _If_ clients pass these initial exercises with many clients, we will design some more exotic tests with more clients and associated goals :)

Non-exaustive list of ideas:
- More nodes, more validators, stress it out
- Test discv5 for joining
- More extensively test sync from genesis
- Have 3rd client join an already running 2 client testnet
- Test operations other than `Attestation`
- Longer-standing testnets
- How many clients can we handle?
- Induce forking
- Reduce slot times as low as we can go

## Peripheral projects

1-on-1 client tests likely won't require all resources from all teams at all times. There are many projects on the periphera worth digging into. The following is a non-exaustive list of ideas:

* Improve client documentation. Our first users (validators!) are expected to start using these soon
* Converge on misc non-consensus things like logging, for better tooling after interop
* Get [seccio-dissector](https://github.com/michaelvoronov/secio-dissector) running
* Get [the gossipsub fork of meshsim](https://github.com/valer-cara/meshsim/) listening to eth2 gossip
* Build a block explorer (ask Proto)
    * monitor forks
    * verify block transitions
* Build tools to induce interesting behavior on testnets
    * Enable partially live nodes
    * Enable late node wrt attestation broadcasting
    * Induce double signing attestations and blocks
    * etc..