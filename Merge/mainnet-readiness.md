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

### Meta Specs

* [x] [Rayonism](https://github.com/ethereum/rayonism/blob/master/specs/merge.md)
* [x] [Amphora](https://hackmd.io/@n0ble/merge-interop-spec)
* [x] [Kintsugi](https://hackmd.io/@n0ble/kintsugi-spec)
* [x] [Kiln](https://hackmd.io/@n0ble/kiln-spec)

### Consensus layer

* [x] Specs feature complete
* [x] Transition process specified [#2462](https://github.com/ethereum/consensus-specs/pull/2462)
* [x] Ensure structural conformance with existing specs [#2472](https://github.com/ethereum/consensus-specs/pull/2472) 
* [x] Rebase with Altair [#2530](https://github.com/ethereum/eth2.0-specs/pull/2530)
* [x] Rebase with London (update `ExecutionPayload`) [#2533](https://github.com/ethereum/consensus-specs/pull/2533)
* [x] P2P spec (primarily just version bumping topics for new types) [#2531](https://github.com/ethereum/consensus-specs/pull/2531)
* [x] [Optimistic sync spec](https://github.com/ethereum/consensus-specs/blob/dev/sync/optimistic.md) 
* [x] Upgrade [`beacon-APIs`](https://github.com/ethereum/beacon-apis) to handle new types
* [x] [BONUS] Annotated specs [link](https://github.com/ethereum/annotated-spec/tree/master/merge)

### Execution layer

* [x] High level [design doc](https://hackmd.io/@n0ble/ethereum_consensus_upgrade_mainnet_perspective)
* [x] EIPs
    * [x] EVM `DIFFICULTY` -> `RANDOM` [EIP-4399](https://eips.ethereum.org/EIPS/eip-4399)
    * [x] EVM `BLOCKHASH` [unchanged but weaker randomness documented in PoW -> PoS transition EIP] [EIP-3675](https://eips.ethereum.org/EIPS/eip-3675)
    * [x] Transition process [EIP-3675](https://eips.ethereum.org/EIPS/eip-3675)
* [x] Network -- devp2p
    * [x] Block gossip deprecation [EIP-3675](https://eips.ethereum.org/EIPS/eip-3675)
    * [x] State sync post-merge
    * [x] Block sync post-merge
    * [x] Discovery
* [x] Upgrade JSON-RPC ([`execution-apis`](https://github.com/ethereum/execution-apis)) with new methods and deprecations [#200](https://github.com/ethereum/execution-apis/pull/200)
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
* [x] Remove unauthenticated port from specification [#219](https://github.com/ethereum/execution-apis/pull/219)

### Public facing documents

* [x] Merge architecture design document
    * [Historical changes](https://tim.mirror.xyz/CHQtTJb1NDxCK41JpULL-zAJe7YOtw-m4UDw6KDju6c), [Architecture](https://tim.mirror.xyz/sR23jU02we6zXRgsF_oTUkttL83S3vyn05vJWnnp-Lc)
* [x] Application Layer Impacts 
    * [Blog post](https://blog.ethereum.org/2021/11/29/how-the-merge-impacts-app-layer/) 
* [x] Rename eth1/eth2 to execution/consensus across repos and documentation -- [The Great Renaming](https://notes.ethereum.org/@timbeiko/great-renaming)
* [x] [Mega Merge Resource List](https://notes.ethereum.org/Moiv99h9QTmI-imPL8pvQg?view)
* [ ] Infrastructure provider guide

## Testing

### Unit tests

* [x] Consensus
    * [x] Inherit all prior unit tests and generators
    * [x] Merge specific tests with mocked execution-layer
    * [x] Fork and fork-choice tests across merge boundary
* [ ] Execution
    * [x] Reuse existing framework for most prior EVM unit tests
    * [ ] [IN [PROGRESS](https://github.com/ethereum/tests/pull/1008)] New `DIFFICULTY` opcode tests
    * [ ] EIP-3675 

### Integration tests

* [x] Testnet [chaos messages](https://github.com/MariusVanDerWijden/go-ethereum/tree/merge-bad-block-creator)
* [ ] Hive
    * [X] Mocked CL for EL [engine API](https://github.com/ethereum/hive/tree/master/simulators/ethereum/engine) unit testing
    * [x] CL+EL integration ests with all client combos
    * [ ] [IN [PROGRESS](https://github.com/txrx-research/TestingTheMerge/blob/main/tests/engine-api.md)] Engine API tests
    * [ ] [IN [PROGRESS](https://github.com/txrx-research/TestingTheMerge/blob/main/tests/transition.md)] Merge transition tests
* [ ] Shadow fork Goerli on a daily or weekly basis to continuously test live transition and TX replays 
* [x] [BONUS] Additional simulation testing -- e.g. kurtosis, antithesis, etc
    * [x] [Kurtosis Merge Module](https://github.com/kurtosis-tech/eth2-merge-kurtosis-module)

### Fuzzing

* [x] [Fuzz engine API](https://github.com/MariusVanDerWijden/merge-fuzz)
* [x] [Existing EVM fuzzing](https://github.com/MariusVanDerWijden/FuzzyVM) infra applied to merge ready execution engines
* [ ] [IN PROGRESS] Beacon-fuzz applied to merge ready consensus clients


## Testnets

* [X] Short-lived devnets without transition process
* [X] Short-lived devnets *with* transition process
* [x] Long-lived devnets 
  * [x] [Kintsugi](https://blog.ethereum.org/2021/12/20/kintsugi-merge-testnet/)
  * [x] [Kiln](https://blog.ethereum.org/2022/03/14/kiln-merge-testnet/)
* [ ] Fork public testnets

## R&D

Most research related to the merge has been completed. This section lists topics which are either tangentially related, or nice-to-haves, and still require R&D work.

* [x] Transition process analysis
    * [x] Evaluate precision of TD computation on historic data
        * https://ethresear.ch/t/using-total-difficulty-threshold-for-hardfork-anchor-what-could-go-wrong/10357
* [x] Execution-layer sync
    * [x] Historic block sync (reverse header then forward body)
    * [x] Historic state sync (optimistic beacon block transition provides head data for EL sync)
    * [x] Sync during transition period (forward sync to PoW TTD, reverse sync past TTD)
* [x] Discovery [is there actually anything to do here?]
* [x] [In research, not to be included merge] Execution-layer proof of custody
* [ ] Consider weak subjectivity period implications
  * [ ] Generate accurate weak subjectivity period calculations
  * [ ] Specify standard data format & methods for weak subjectivity checkpoint distribution
* [x] Disaster recovery if invalid chain finalized
  * [x] EL will perform re-orgs beyond finality but at a potential high sync cost
  * [x] [WIP] Client multiplexers ([link](https://github.com/karalabe/minority), note: doesn't help with DR, but can potentially prevent invalid chains being finalized)
* [ ] Stress tests
  * [ ] Single client load/metrics
  * [ ] Network load testing 
    * [ ] Larger blocks
    * [ ] Shorter slot times
    * [x] Large execution state (shadow-forking mainnet)
* [ ] Further threat analysis
    * [x] Miner attacks
    * [ ] Resource exhaustion post-merge
* [x] Fee Market behavior changes (missed slots impact)
    * [EIP-4396](https://eips.ethereum.org/EIPS/eip-4396) proposed 
