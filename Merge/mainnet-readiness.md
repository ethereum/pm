# The Merge Mainnet Readiness Checklist

This document outlines various tasks to work through to make the Merge ready for Mainnet release.

*Note*: The set of items is not final and will be aligned with ongoing R&D and implementation work.

## Table of contents

<!-- TOC -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Specification](#specification)
  - [Consensus layer](#consensus-layer)
  - [Execution layer](#execution-layer)
  - [Consensus API](#consensus-api)
  - [Public facing documents](#public-facing-documents)
- [Testing](#testing)
  - [Unit tests](#unit-tests)
  - [Integration tests](#integration-tests)
  - [Stress tests](#stress-tests)
  - [Fuzzing](#fuzzing)
- [Testnets](#testnets)
- [R&D](#rd)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- /TOC -->

## Specification

### Consensus layer

* [x] Specs feature complete
* [x] Transition process specified [#2462](https://github.com/ethereum/eth2.0-specs/pull/2462)
* [x] Ensure structural conformance with existing specs [#2472](https://github.com/ethereum/eth2.0-specs/pull/2472) 
* [x] Rebase with Altair [#2530](https://github.com/ethereum/eth2.0-specs/pull/2530)
* [x] Rebase with London (update `ExecutionPayload`) [#2533](https://github.com/ethereum/eth2.0-specs/pull/2533)
* [ ] Consider weak subjectivity period implications
* [ ] P2P spec (primarily just version bumping topics for new types)
* [ ] Upgrade [`eth2.0-apis`](https://github.com/ethereum/eth2.0-apis) to handle new types
* [ ] [BONUS] Annotated specs

### Execution layer

* [x] High level [design doc](https://hackmd.io/@n0ble/ethereum_consensus_upgrade_mainnet_perspective)
* [x] [Rayonism spec](https://github.com/ethereum/rayonism/blob/master/specs/merge.md)
* [ ] EIPs
    * [ ] EVM `DIFFICULTY` -> `RANDOM`
    * [ ] EVM `BLOCKHASH` [unchanged but weaker randomness documented in PoW -> PoS transition EIP]
    * [ ] [IN PROGRESS] Transition process (Draft EIP -- [#3675](https://github.com/ethereum/EIPs/pull/3675))
* [ ] Network -- devp2p
    * [ ] Block gossip deprecation
    * [ ] State sync post-merge
    * [ ] Block sync post-merge
    * [ ] Discovery
* [ ] Upgrade JSON-RPC ([`eth1.0-apis`](https://github.com/ethereum/eth1.0-apis)) with new methods and deprecations
* [ ] [BONUS] Executable [`eth1.0-specs`](https://github.com/ethereum/eth1.0-specs/pull/219) and testing through the Merge

### Consensus API

* [x] Basic JSON-RPC extension, [link](https://github.com/ethereum/rayonism/blob/master/specs/merge.md#consensus-json-rpc) (used in rayonism)
* [ ] Production refinements
    * [ ] Support execution-layer state sync
    * [ ] Support async block insert
    * [ ] Consider support for `Consensus <-> Execution` consistency (e.g. recover from crash or bad insert on execution layer)
    * [ ] Consider bi-directional communication
    * [ ] ...
* [ ] Discuss JSON-RPC vs websockets vs restful http
* [ ] Migrate to [eth1.0-specs](https://github.com/ethereum/eth1.0-specs) or other permanent home
* [ ] Test vectors?

### Public facing documents

* [ ] Merge architecture design document
* [ ] Infrastructure provider guide
* [ ] Rename eth1/eth2 to execution/consensus across repos and documentation
* [ ] [BONUS] Consider relationship between execution and consensus spec/API repos and build processes

## Testing

### Unit tests

* [ ] Consensus
    * [x] Inherit all prior unit tests and generators
    * [ ] [IN [PROGRESS](https://github.com/ethereum/eth2.0-specs/tree/dev/tests/core/pyspec/eth2spec/test/merge)] Merge specific tests with mocked execution-layer
    * [ ] Fork and fork-choice tests across merge boundary
* [ ] Execution
    * [ ] Reuse existing framework for most prior EVM unit tests
    * [ ] New `DIFFICULTY` opcode tests

### Integration tests

* [ ] Transition process tests with fully enabled consensus and execution layer
* [ ] Consensus-layer vectors with fully enabled execution-layer
* [ ] Hive with all client combos
* [ ] Hive or something else for suite of consensus+execution integration tests

### Stress tests

* [ ] Single client load/metrics
* [ ] Network load testing

### Fuzzing

* [ ] Beacon-fuzz applied to merge ready consensus clients
* [ ] Existing EVM fuzzing infra applied to merge ready execution engines

## Testnets

* [ ] Short-lived devnets without transition process
* [ ] Short-lived devnets *with* transition process
* [ ] Long-lived devnets
* [ ] Fork public testnets

## R&D

Most research has been completed. Only listing things still left to dig deeper into

* [ ] Transition process analysis
    * [ ] Simulate PoW network partitioning
    * [ ] Evaluate precision of TD computation on historic data
* [ ] Execution-layer sync
    * [x] Historic block sync (reverse header then forward body)
    * [ ] Historic state sync
    * [ ] Sync during transition period
* [ ] Discovery [is there actually anything to do here?]
* [ ] Execution-layer proof of custody
* [ ] Further threat analysis
    * [ ] Miner attacks
    * [ ] Resource exhaustion post-merge
