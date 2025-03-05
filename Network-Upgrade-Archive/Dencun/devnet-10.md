# dencun-devnet-10 specs

**note**: this file was copied from [here](https://notes.ethereum.org/@ethpandaops/dencun-devnet-10#) for reference.

`Devnet-10 will be short lived (sub one week), it will be mainly used to test the new churn limit EIP (EIP-7514). If you are a CL dev, you have to make sure that MAX_PER_EPOCH_ACTIVATION_CHURN_LIMIT config variable is configurable, and we should be able to override it! `

`Devnet-10 will be the first multi arch devnet, please make sure the images that you provide will work for x86 as well as for arm.`

`Devnet-10 will be using the updated (mainnet) kzg trusted setup file!`

`Devnet-10 will be shut down on 30th Oct 2023 at 10:00AM UTC.`

## EIP List for Dencun

- [EIP-1153: Transient storage opcodes](https://eips.ethereum.org/EIPS/eip-1153)
- [EIP-4844: Shard Blob Transactions](https://eips.ethereum.org/EIPS/eip-4844)
- [EIP-4788: Beacon block root in the EVM](https://eips.ethereum.org/EIPS/eip-4788)
- [EIP-5656: MCOPY - Memory copying instruction](https://eips.ethereum.org/EIPS/eip-5656)
- [EIP-6780: SELFDESTRUCT only in same transaction](https://eips.ethereum.org/EIPS/eip-6780)
- [EIP-7044: Perpetually Valid Signed Voluntary Exits](https://eips.ethereum.org/EIPS/eip-7044)
- [EIP-7045: Increase Max Attestation Inclusion Slot](https://eips.ethereum.org/EIPS/eip-7045)
- [EIP-7516: BLOBBASEFEE opcode](https://eips.ethereum.org/EIPS/eip-7516)
- [EIP-7514: Add max epoch activation churn limit](https://eips.ethereum.org/EIPS/eip-7514)

## [Docker images](https://github.com/ethpandaops/dencun-testnet/blob/master/ansible/inventories/devnet-10/group_vars/all/images.yaml) for devnet 10

### Open issues
[Prysm-13097](https://github.com/prysmaticlabs/prysm/issues/13097) - triggered by the accidental non finality event at epoch 32-35 - Closed
[Teku-7626](https://github.com/Consensys/teku/issues/7626) - triggered by mass deposits - Closed
MEV-Boost - timestamp too early issue (no open issue yet)
MEV-Relay - Error: BLOCK_ERROR_INVALID_STATE_ROOT (no open issue yet)

### Spec changes for dencun-devnet-10
**Consensus Spec** [v1.4.0-beta.3](https://github.com/ethereum/consensus-specs/releases/tag/v1.4.0-beta.3) :heavy_check_mark:

* [PR-3499 - Add max epoch activation churn limit (EIP-7514)](https://github.com/ethereum/consensus-specs/pull/3499) - Merged :heavy_check_mark:
Issue to consider: [3261](https://github.com/ethereum/consensus-specs/issues/3261)

**Beacon API** - [v2.4.2](https://github.com/ethereum/beacon-APIs/releases/tag/v2.4.2) :heavy_check_mark:

* [PR-339 - Add block v3 endpoint](https://github.com/ethereum/beacon-APIs/pull/339) - Merged :heavy_check_mark:

**Builder Spec**

* [PR-87 - RFC: Use MAX_BLOB_COMMITMENTS_PER_BLOCK as max length for BlindedBlobsBundle SSZ lists](https://github.com/ethereum/builder-specs/pull/87) - Merged :heavy_check_mark:
Spec changes for older 4844-devnet-6,7 and dencun-devnet-8,9 devnets

**Consensus Specs** - [v1.4.0-beta.1](https://github.com/ethereum/consensus-specs/releases/tag/v1.4.0-beta.1) :heavy_check_mark:

- [PR-3461 - Rename “data gas” to “blob gas”](https://github.com/ethereum/consensus-specs/pull/3461) - Merged :heavy_check_mark:
- [PR-3421 - Move move 4788 to deneb](https://github.com/ethereum/consensus-specs/pull/3421) - Merged :heavy_check_mark:
- [PR-3444 - Update blob side car subnet count to 6 in line with max blobs limit update](https://github.com/ethereum/consensus-specs/pull/3416) - Merged :heavy_check_mark:
- [PR-3410 - Update MAX_BLOBS_PER_BLOCK to 6 and add Deneb networking configs to yaml files](https://github.com/ethereum/consensus-specs/pull/3410) - Merged :heavy_check_mark:
- [PR-3392 - Change ExecutionPayload.excess_data_gas type from uint256 to uint64](https://github.com/ethereum/consensus-specs/pull/3392) - Merged :heavy_check_mark:
- [PR-3391 - Add data_gas_used field to ExecutionPayload](https://github.com/ethereum/consensus-specs/pull/3391) - Merged :heavy_check_mark:
- [PR-3359 - Use engine_newPayloadV3 to pass versioned_hashes to EL for validation](https://github.com/ethereum/consensus-specs/pull/3359) - Merged :heavy_check_mark:
- [PR-3354 - Update the endianness of the polynomial commitments to be big endian](https://github.com/ethereum/consensus-specs/pull/3354) - Merged :heavy_check_mark:
- [PR-3338 - Update block’s blob_kzg_commitments size limit to MAX_BLOB_COMMITMENTS_PER_BLOCK (4096)](https://github.com/ethereum/consensus-specs/pull/3338) - Merged :heavy_check_mark:
- [PR-3317 - Switch blob tx type to 0x03](https://github.com/ethereum/consensus-specs/pull/3317) - Merged :heavy_check_mark:
- [PR-3244 - Free the blobs](https://github.com/ethereum/consensus-specs/pull/3244) - Merged :heavy_check_mark:

**Execution EIPs**

- [PR-7672 - Update EIP-4788: post audit tweaks](https://github.com/ethereum/EIPs/pull/7672/files) - Merged :heavy_check_mark:
- [PR-7456 - Update EIP-4788: initial stab at v2](https://github.com/ethereum/EIPs/pull/7456) - Merged :heavy_check_mark:
- [PR-7354 - Rename “data gas” to “blob gas”](https://github.com/ethereum/EIPs/pull/7354) - Merged :heavy_check_mark:
- [PR-7172 - Update precompile address for 4844](https://github.com/ethereum/EIPs/pull/7172) - Merged :heavy_check_mark:
- [PR-7154 - Increase Blob Throughput](https://github.com/ethereum/EIPs/pull/7154) - Merged :heavy_check_mark:
- [PR-7123 - Update EIP-4844: clarify transaction payload body](https://github.com/ethereum/EIPs/pull/7123) - Merged :heavy_check_mark:
- [PR-7100 - clarify to must be non-nil](https://github.com/ethereum/EIPs/pull/7100) - Merged :heavy_check_mark:
- [PR-7095 - reduce size of excess_data_gas to 64 bit](https://github.com/ethereum/EIPs/pull/7095) - Merged :heavy_check_mark:
- [PR-7062 - add data_gas_used to header](https://github.com/ethereum/EIPs/pull/7062) - Merged :heavy_check_mark:
- [PR-7038 - Cleanup transaction network payload references](https://github.com/ethereum/EIPs/pull/7038) - Merged :heavy_check_mark:
- [PR-7020 - Specify precompile input’s z and y to be encoded as big endian](https://github.com/ethereum/EIPs/pull/7020) - Merged :heavy_check_mark:
- [PR-6985 - de-sszify spec](https://github.com/ethereum/EIPs/pull/6985) - Merged :heavy_check_mark:
- [PR-6863 - Ban Zero Blob Transactions](https://github.com/ethereum/EIPs/pull/6863) - Merged :heavy_check_mark:
- [PR-6832 - Blob Transaction Type changed to 0x03](https://github.com/ethereum/EIPs/pull/6832) - Merged :heavy_check_mark:
- [PR-6610 - Decouple Blobs](https://github.com/ethereum/EIPs/pull/6610) - Merged :heavy_check_mark:

**Engine API**

- [PR-398 - Add dataGasUsed and dataGasPrice to receipts for 4844 txs](https://github.com/ethereum/execution-apis/pull/398) - Merged :heavy_check_mark:
- [PR-451 - Rename “data gas” to “blob gas”](https://github.com/ethereum/execution-apis/pull/451) - Merged :heavy_check_mark:
- [PR-426 - Clarify Cancun payloads handling by earlier APIs; reorder checks](https://github.com/ethereum/execution-apis/pull/426) - Merged :heavy_check_mark:
- [PR-425 - Scope shouldOverrideBuilder flag for Cancun](https://github.com/ethereum/execution-apis/pull/425) - Merged :heavy_check_mark:
- [PR-420 - Cancun specification](https://github.com/ethereum/execution-apis/pull/420) - Merged :heavy_check_mark:
- [PR-418 - Employ one method one structure approach for V3](https://github.com/ethereum/execution-apis/pull/418) - Merged :heavy_check_mark:
- [PR-417 - Update PayloadV3 with data gas use](https://github.com/ethereum/execution-apis/pull/417) - Merged :heavy_check_mark:
- [PR-407 - Engine API: validate blob versioned hashes](https://github.com/ethereum/execution-apis/pull/407) - Merged :heavy_check_mark:
- [PR-404 - Assert array items in BlobsBundleV1 to be of same length](https://github.com/ethereum/execution-apis/pull/404) - Merged :heavy_check_mark:
- [PR-402 - Merge getPayloadV3 and getBlobsBundleV1](https://github.com/ethereum/execution-apis/pull/402) - Merged :heavy_check_mark:
- [PR-401 - State that payloadId should be unique for each PayloadAttributes instance](https://github.com/ethereum/execution-apis/pull/401) - Merged :heavy_check_mark:
- [PR-392 - Add corresponding proofs to BlobsBundleV1](https://github.com/ethereum/execution-apis/pull/392) - Merged :heavy_check_mark:

**Beacon API** - [v2.4.2](https://github.com/ethereum/beacon-APIs/releases/tag/v2.4.2) :heavy_check_mark:

- [PR-339 - Add block v3 endpoint](https://github.com/ethereum/beacon-APIs/pull/339) - Merged :heavy_check_mark:
- [PR-317 - Add broadcast_validation to block publishing](https://github.com/ethereum/beacon-APIs/pull/317) - Merged :heavy_check_mark:
- [PR-321 - Update publishBlindedBlockV2 request schema for Deneb ](https://github.com/ethereum/beacon-APIs/pull/321)- Merged :heavy_check_mark:
- [PR-302 - Add blob signing endpoints](https://github.com/ethereum/beacon-APIs/pull/302) - Merged :heavy_check_mark:
- [PR-286 - Add blob download endpoint (getBlobs)](https://github.com/ethereum/beacon-APIs/pull/286) - Merged :heavy_check_mark:

