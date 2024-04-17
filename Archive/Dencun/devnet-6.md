# 4844-devnet-6 specs
note: this file was copied from [here](https://notes.ethereum.org/@bbusa/dencun-devnet-6) for reference.

`4844 requires a trusted setup file, Please ensure that there is a way for us to specify the file through a runtime flag such as --trusted-setup-file (or similar). If the file is baked in during compile, please ensure that the flag would indeed override the file. This is a MUST requirement for devnet 6. If your client does not support the override, we can’t include it in the devnet.`

`The c-kzg trusted setup file has been updated since devnet 5. Please make sure you use the correct values. This can be found [here](https://github.com/ethereum/c-kzg-4844/blob/main/src/trusted_setup.txt).`

### Consensus Specs @ Commit [0682b22](https://github.com/ethereum/consensus-specs/commit/0682b2231773574b5bdda39c5cc7481ab9a471a3) aka [v1.4.0-alpha.3](https://github.com/ethereum/consensus-specs/releases/tag/v1.4.0-alpha.3) :heavy_check_mark:

- [PR-3444 - Update blob side car subnet count to 6 in line with max blobs limit update](https://github.com/ethereum/consensus-specs/pull/3416) - Merged :heavy_check_mark:
- [PR-3410 - Update MAX_BLOBS_PER_BLOCK to 6 and add Deneb networking configs to yaml files](https://github.com/ethereum/consensus-specs/pull/3410) - Merged :heavy_check_mark:
- [PR-3392 - Change ExecutionPayload.excess_data_gas type from uint256 to uint64](https://github.com/ethereum/consensus-specs/pull/3392) - Merged :heavy_check_mark:
- [PR-3391 - Add data_gas_used field to ExecutionPayload](https://github.com/ethereum/consensus-specs/pull/3391) - Merged :heavy_check_mark:
- [PR-3359 - Use engine_newPayloadV3 to pass versioned_hashes to EL for validation](https://github.com/ethereum/consensus-specs/pull/3359) - Merged :heavy_check_mark:
- [PR-3354 - Update the endianness of the polynomial commitments to be big endian](https://github.com/ethereum/consensus-specs/pull/3354) - Merged :heavy_check_mark:
- [PR-3338 - Update block’s blob_kzg_commitments size limit to MAX_BLOB_COMMITMENTS_PER_BLOCK (4096)](https://github.com/ethereum/consensus-specs/pull/3338) - Merged :heavy_check_mark:
- [PR-3317 - Switch blob tx type to 0x03](https://github.com/ethereum/consensus-specs/pull/3317) - Merged :heavy_check_mark: - Already part of devnet 5
- [PR-3244 - Free the blobs](https://github.com/ethereum/consensus-specs/pull/3244) - Merged :heavy_check_mark: - Already part of devnet 5
- 

### Execution EIPs @ Commit [e9a4295](https://github.com/ethereum/EIPs/commit/e9a4295fe7661d2ab31183563087f9073272ccc1) :heavy_check_mark:

- [PR-7154 - Increase Blob Throughput](https://github.com/ethereum/EIPs/pull/7154) - Merged :heavy_check_mark:
- [PR-7123 - Update EIP-4844: clarify transaction payload body](https://github.com/ethereum/EIPs/pull/7123) - Merged :heavy_check_mark:
- [PR-7100 - clarify to must be non-nil](https://github.com/ethereum/EIPs/pull/7100) - Merged :heavy_check_mark:
- [PR-7095 - reduce size of excess_data_gas to 64 bit](https://github.com/ethereum/EIPs/pull/7095) - Merged :heavy_check_mark:
- [PR-7062 - add data_gas_used to header](https://github.com/ethereum/EIPs/pull/7062) - Merged :heavy_check_mark:
- [PR-7038 - Cleanup transaction network payload references](https://github.com/ethereum/EIPs/pull/7038) - Merged :heavy_check_mark:
- [PR-7020 - Specify precompile input’s z and y to be encoded as big endian](https://github.com/ethereum/EIPs/pull/7020) - Merged :heavy_check_mark:
- [PR-6985 - de-sszify spec](https://github.com/ethereum/EIPs/pull/6985) - Merged :heavy_check_mark:
- [PR-6863 - Ban Zero Blob Transactions](https://github.com/ethereum/EIPs/pull/6863) - Merged :heavy_check_mark: - Already part of devnet 5
- [PR-6832 - Blob Transaction Type changed to 0x03](https://github.com/ethereum/EIPs/pull/6832) - Merged :heavy_check_mark: - Already part of devnet 5
- [PR-6610 - Decouple Blobs](https://github.com/ethereum/EIPs/pull/6610) - Merged :heavy_check_mark: - Already part of devnet 5

### Engine API @ Commit [3c49c03](https://github.com/ethereum/execution-apis/commit/3c49c03fc6f8187c7576c0447c14950918e5eb1f) :heavy_check_mark:

- [PR-417 - Update PayloadV3 with data gas use](https://github.com/ethereum/execution-apis/pull/417) - Merged :heavy_check_mark:
- [PR-407 - Engine API: validate blob versioned hashes](https://github.com/ethereum/execution-apis/pull/407) - Merged :heavy_check_mark:
- [PR-404 - Assert array items in BlobsBundleV1 to be of same length](https://github.com/ethereum/execution-apis/pull/404) - Merged :heavy_check_mark:
- [PR-402 - Merge getPayloadV3 and getBlobsBundleV1](https://github.com/ethereum/execution-apis/pull/402) - Merged :heavy_check_mark: - Already part of Devnet 5
- [PR-401 - State that payloadId should be unique for each PayloadAttributes instance](https://github.com/ethereum/execution-apis/pull/401) - Merged :heavy_check_mark:
- [PR-392 - Add corresponding proofs to BlobsBundleV1](https://github.com/ethereum/execution-apis/pull/392) - Merged :heavy_check_mark: - Already part of Devnet 5

### Beacon API @ Commit [f65d774](https://github.com/ethereum/beacon-APIs/commit/f65d774fe8abfb7773fc6f7c05d5453479b971ed) aka [v2.4.1](https://github.com/ethereum/beacon-APIs/releases/tag/v2.4.1):heavy_check_mark:

- [PR-321 - Update publishBlindedBlockV2 request schema for Deneb ](https://github.com/ethereum/beacon-APIs/pull/321)- Merged :heavy_check_mark:
- [PR-302 - Add blob signing endpoints](https://github.com/ethereum/beacon-APIs/pull/302) - Merged :heavy_check_mark: - Already part of Devnet 5 as optional spec
- [PR-286 - Add blob download endpoint (getBlobs)](https://github.com/ethereum/beacon-APIs/pull/286) - Merged :heavy_check_mark:
- 

## Possible PR candidates for dencun-devnet-7 (not only 4844 PRs):
### Execution EIPs

- [PR-7037 - Send current slot from CL to avoid timestamp conversions](https://github.com/ethereum/EIPs/pull/7037) - Merged :heavy_check_mark:

### Engine API

- [PR-420 - Cancun specification](https://github.com/ethereum/execution-apis/pull/420) - Open :exclamation:
- [PR-418 - Employ one method one structure approach for V3](https://github.com/ethereum/execution-apis/pull/418) - Merged :heavy_check_mark:
- [PR-398 - Add dataGasUsed and dataGasPrice to receipts for 4844 txs](https://github.com/ethereum/execution-apis/pull/398) - Open :exclamation:

### Beacon API

- [PR-317 - Add broadcast_validation to block publishing](https://github.com/ethereum/beacon-APIs/pull/317) - Merged :heavy_check_mark:
