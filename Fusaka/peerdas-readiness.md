# PeerDAS Readiness Checklist

This document outlines various tasks to work through to make PeerDAS ready for Mainnet release.

*Note*: The set of items is not final and will be aligned with ongoing R&D and implementation work.

## Table of contents

<!-- TOC -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Testnets & Client Implementation](#testnets--client-implementation)
- [Specification](#specification)
- [Testing](#testing)
- [R&D](#rd)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- /TOC -->

## Testnets & Client Implementation

* [x] `peerdas-devnet-4` (https://notes.ethereum.org/@ethpandaops/peerdas-devnet-4)
  * [x] PeerDAS activation at the Fulu Fork
  * [x] Subnet Decoupling (introduce Custody Groups)
  * [x] Increase blob count (9/12)
* [ ] `peerdas-devnet-5` (`peerdas-devnet-4` relaunch with new EL image)
  * [ ] Sync testing: checkpoint and genesis sync
  * [ ] Validator custody (optional)
* [ ] `peerdas-devnet-6` (**feature complete**)
  * [ ] Validator custody on all clients
  * [ ] Distributed blob ~~building~~ publishing
  * [ ] [Move proof computation to transaction sender](https://hackmd.io/@jimmygchen/HkUpFliYJx)
  * [ ] Increase blob count (?/?)
* [ ] `peerdas-devnet-7`
  * [ ] MEV flow testing
  * [ ] Adjusted blob count?
* [ ] Public testnets

## Specification

* [x] Validator Custody
* [ ] Distributed Blob Publishing
  * [ ] `consensus-spec` to specify minimum requirements for data column publishing
* [ ] Move proof computation to transaction sender
  * [ ] EIP: [Update EIP-7594: include cell proofs in network wrapper of blob txs #9378](https://github.com/ethereum/EIPs/pull/9378)
  * [ ] `execution-specs` update: does the mempool verification change need to be specified?
  * [ ] `execution-apis` update: `getPayloadV5` and `getBlobsV2` to replace blob KZG proofs with cell KZG proofs.
  * [ ] `consensus-specs` update: See [here](https://hackmd.io/@jimmygchen/HkUpFliYJx#CL-changes)
  * [ ] `beacon-API` update: `GetBlobSidecar` API may need a version bump as we replace blob KZG proofs with cell KZG proofs.
* [ ] EIP to increase target / max blob count in Fusaka

## Testing

* [ ] Tooling updates
  * [ ] `spamoor` needs updating to use the new tx format, potentially we need a way to make sure clients are indeed adhering this change
* [ ] [EELS](https://github.com/ethereum/execution-specs) Implementation
* [ ] [EEST](https://github.com/ethereum/execution-spec-tests) Tests
* [ ] Hive
* [ ] Run network limit devnets (https://notes.ethereum.org/@ethpandaops/network-limit-devnets)
* [ ] Effectiveness of distributed blob publishing
 * [ ] Gather `getBlobs` performance metrics across all ELs
 * [ ] Gather `getBlobs` hit rate and publish rate across all CLs
 * [ ] Run a devnet and disable proposer blob publishing, and use the block proposal success rate as a measure of effectiveness of distributed publishing.
* [ ] High blob throughput testing (48/64 blobs) that we can do today (before [proof computation changes](https://github.com/ethereum/EIPs/pull/9378) is implemented)
 * [ ] Stub out proof computation in the KZG lib and test CL performance with high blob count (to simulate proof computation offloaded).
 * [ ] Stress test mempool to make sure the ELs can handle high blob count.
* [ ] High blob throughput testing (48/64 blobs) on a large network that mirrors mainnet network typology (after [proof computation changes](https://github.com/ethereum/EIPs/pull/9378) implemented in at least 1 CL/EL client pair)
 
## R&D

* [ ] Anaylsis of new blob count impact on bandwidth, hardware requirements once clients are feature complete (`peerdas-devnet-6`)
* [ ] Nice to have: [BPO only forks](https://ethereum-magicians.org/t/blob-parameter-only-bpo-forks/22623)
* [ ] EL: Potential optimisation of `getBlobs` endpoint?
* [ ] Document impact to node operators (prior post with 16 blobs [here](https://blog.sigmaprime.io/peerdas-distributed-blob-building.html#impact-on-node-operators))
* [ ] Research/estimate/measure sync speed on various custody column count.
