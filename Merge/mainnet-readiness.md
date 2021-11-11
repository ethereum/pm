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
  - [Engine API](#engine-api)
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
* [x] Transition process specified [#2462](https://github.com/ethereum/consensus-specs/pull/2462)
* [x] Ensure structural conformance with existing specs [#2472](https://github.com/ethereum/consensus-specs/pull/2472) 
* [x] Rebase with Altair [#2530](https://github.com/ethereum/eth2.0-specs/pull/2530)
* [x] Rebase with London (update `ExecutionPayload`) [#2533](https://github.com/ethereum/consensus-specs/pull/2533)
* [ ] Consider weak subjectivity period implications
* [x] P2P spec (primarily just version bumping topics for new types) [#2531](https://github.com/ethereum/consensus-specs/pull/2531)
* [ ] Upgrade [`beacon-APIs`](https://github.com/ethereum/beacon-apis) to handle new types
* [x] [BONUS] Annotated specs [link](https://github.com/ethereum/annotated-spec/tree/master/merge)

### Execution layer

* [x] High level [design doc](https://hackmd.io/@n0ble/ethereum_consensus_upgrade_mainnet_perspective)
* [x] [Rayonism spec](https://github.com/ethereum/rayonism/blob/master/specs/merge.md)
* [ ] EIPs
    * [x] EVM `DIFFICULTY` -> `RANDOM` [EIP-4399](https://eips.ethereum.org/EIPS/eip-4399)
    * [x] EVM `BLOCKHASH` [unchanged but weaker randomness documented in PoW -> PoS transition EIP] [EIP-3675](https://eips.ethereum.org/EIPS/eip-3675)
    * [x] Transition process [EIP-3675](https://eips.ethereum.org/EIPS/eip-3675)
* [ ] Network -- devp2p
    * [x] Block gossip deprecation [EIP-3675](https://eips.ethereum.org/EIPS/eip-3675)
    * [ ] State sync post-merge
    * [ ] Block sync post-merge
    * [ ] Discovery
* [ ] Upgrade JSON-RPC ([`execution-apis`](https://github.com/ethereum/execution-apis)) with new methods and deprecations
* [ ] [BONUS] Executable [`execution-specs`](https://github.com/ethereum/execution-specs/pull/219) and testing through the Merge

### Engine API

* [x] Basic JSON-RPC extension, [link](https://github.com/ethereum/rayonism/blob/master/specs/merge.md#consensus-json-rpc) (used in rayonism)
* [x] Production refinements [Engine API](https://github.com/ethereum/execution-apis/blob/main/src/engine/specification.md). Previous docs: [WIP doc](https://hackmd.io/@n0ble/consensus_api_design_space), [Interop Edition](https://github.com/ethereum/execution-apis/blob/main/src/engine/interop/specification.md)
    * Support execution-layer state sync
    * Support async block insert
    * Consider support for `Consensus <-> Execution` consistency (e.g. recover from crash or bad insert on execution layer)
    * Consider bi-directional communication
    * ...
* [x] Discuss JSON-RPC vs websockets vs restful http
* [x] Migrate to [execution-APIs](https://github.com/ethereum/execution-APIs) or other permanent home, [link](https://github.com/ethereum/execution-apis/tree/main/src/engine)
* [ ] [BONUS] Test vectors

### Public facing documents

* [ ] Merge architecture design document
* [ ] Infrastructure provider guide
* [x] Rename eth1/eth2 to execution/consensus across repos and documentation -- [The Great Renaming](https://notes.ethereum.org/@timbeiko/great-renaming)
* [ ] [BONUS] Consider relationship between execution and consensus spec/API repos and build processes

## Testing

### Unit tests

* [ ] Consensus
    * [x] Inherit all prior unit tests and generators
    * [ ] [IN [PROGRESS](https://github.com/ethereum/eth2.0-specs/tree/dev/tests/core/pyspec/eth2spec/test/merge)] Merge specific tests with mocked execution-layer
    * [ ] [IN [PROGRESS](https://github.com/ethereum/consensus-specs/tree/dev/tests/core/pyspec/eth2spec/test/merge/fork_choice)] Fork and fork-choice tests across merge boundary
* [ ] Execution
    * [ ] Reuse existing framework for most prior EVM unit tests
    * [ ] New `DIFFICULTY` opcode tests

### Integration tests

* [ ] Transition process tests with fully enabled consensus and execution layer
    * [ ] Hive: scenario with PoW network partitioning
    * [ ] Hive: happy case and various edge case scenarios, e.g:
      * [ ] Re-org beyond transition block
      * [ ] EL/CL client offline or not upgraded before/during/after transition
      * [ ] PoW block propagation before/during/after transition
      * [ ] Burst of EL blocks on different forks & optimistic sync interactions
* [ ] Hive with all client combos
* [ ] Hive: consensus+execution integration tests
* [ ] Hive: Engine API tests

### Stress tests

* [ ] Single client load/metrics
* [ ] Network load testing 
  * [ ] Larger blocks
  * [ ] Shorter slot times
  * [ ] Large execution state. 

### Fuzzing

* [ ] Beacon-fuzz applied to merge ready consensus clients
* [ ] Existing EVM fuzzing infra applied to merge ready execution engines

## Testnets

* [X] Short-lived devnets without transition process
* [X] Short-lived devnets *with* transition process
* [ ] Long-lived devnets
* [ ] Fork public testnets

## R&D

Most research related to the merge has been completed. This section lists topics which are either tangentially related, or nice-to-haves, and still require R&D work.

* [ ] Transition process analysis
    * [x] Evaluate precision of TD computation on historic data
        * https://ethresear.ch/t/using-total-difficulty-threshold-for-hardfork-anchor-what-could-go-wrong/10357
* [x] Execution-layer sync
    * [x] Historic block sync (reverse header then forward body)
    * [x] Historic state sync (optimistic beacon block transition provides head data for EL sync)
    * [x] Sync during transition period (forward sync to PoW TTD, reverse sync past TTD)
* [ ] Discovery [is there actually anything to do here?]
* [ ] Execution-layer proof of custody
* [ ] Disaster recovery if invalid chain finalized
  * [x] [WIP] Client multiplexers ([link](https://github.com/karalabe/minority), note: doesn't help with DR, but can potentially prevent invalid chains being finalized)
* [ ] Further threat analysis
    * [ ] Miner attacks
    * [ ] Resource exhaustion post-merge
* [ ] Fee Market behavior changes (missed slots impact)
