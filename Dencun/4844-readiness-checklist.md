# EIP-4844 Readiness Checklist

This document is meant to capture various tasks that need to be completed before EIP-4844 is ready to be scheduled for mainnet deployment. **Last updated Sept 8, 2023**. 

## Specs

- [Execution Layer: EIP-4844](https://eips.ethereum.org/EIPS/eip-4844)
- [Consensus Layer: consensus-specs `deneb` folder](https://github.com/ethereum/consensus-specs/tree/dev/specs/deneb)
- [Engine API: `blob-extension.md`](https://github.com/ethereum/execution-apis/blob/main/src/engine/experimental/blob-extension.md)

## Implementation

### Client Implementation Status 

#### Execution Layer 

### Implementation Progresss

Implementation status of Included EIPs across participating clients.

|                | [1153](https://eips.ethereum.org/EIPS/eip-1153) | [4788](https://eips.ethereum.org/EIPS/eip-4788) | [4844](https://eips.ethereum.org/EIPS/eip-4844) | [5656](https://eips.ethereum.org/EIPS/eip-5656) | [6780](https://eips.ethereum.org/EIPS/eip-6780) | [7516](https://eips.ethereum.org/EIPS/eip-7516) |
|----------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|
| **Geth**       | [Merged](https://github.com/ethereum/go-ethereum/pull/26003) + [Merged](https://github.com/ethereum/go-ethereum/pull/27663)| - | [Merged](https://github.com/ethereum/go-ethereum/pull/26940) | [Merged](https://github.com/ethereum/go-ethereum/pull/26181) | [Not merged](https://github.com/ethereum/go-ethereum/pull/27189) | |
| **Besu**       | [Merged](https://github.com/hyperledger/besu/pull/4118) | - | [Merged]([https://github.com/hyperledger/besu/tree/eip-4844-interop](https://github.com/hyperledger/besu/pull/5724)) | [Merged](https://github.com/hyperledger/besu/pull/5493) | [Merged](https://github.com/hyperledger/besu/pull/4118) | |
| **Nethermind** | [Merged](https://github.com/NethermindEth/nethermind/pull/4126) | [Not merged](https://github.com/NethermindEth/nethermind/pull/5476) | [Not merged (many PRs)](https://github.com/NethermindEth/nethermind/pull/5671) | [Not merged](https://github.com/NethermindEth/nethermind/pull/5791) | [Not merged](https://github.com/NethermindEth/nethermind/pull/4704) | |
| **Erigon**     | [Merged](https://github.com/ledgerwatch/erigon/pull/7405) + [Merged](https://github.com/ledgerwatch/erigon/pull/7885) | [Merged (many PRs)](https://github.com/ledgerwatch/erigon/pulls?q=is%3Apr+4788) | [Merged (many PRs)](https://github.com/ledgerwatch/erigon/pulls?q=is%3Apr+4844) | [Merged](https://github.com/ledgerwatch/erigon/pull/7887) | [Merged](https://github.com/ledgerwatch/erigon/pull/7976) | [Merged](https://github.com/ledgerwatch/erigon/pull/8231) |
| **EthereumJS** | [Merged](https://github.com/ethereumjs/ethereumjs-monorepo/pull/1860) | [Merged](https://github.com/ethereumjs/ethereumjs-monorepo/pull/2810) | [Merged (many PRs)](https://github.com/ethereumjs/ethereumjs-monorepo/pulls?q=is%3Apr+4844) | [Merged](https://github.com/ethereumjs/ethereumjs-monorepo/pull/2808) | [Merged](https://github.com/ethereumjs/ethereumjs-monorepo/pull/2771) | |

#### Consensus Layer 

See the latest [devnet configs](https://github.com/ethpandaops/dencun-testnet/blob/master/ansible/inventories/devnet-8/group_vars/all/images.yaml#L2)


### Spec-level Open Issues 

- [x] SSZ vs. RLP encoding of transactions
    - EIP-4844 transactions will maintain RLP encoding, see: https://github.com/ethereum/EIPs/pull/6985
- [x] Big vs. Little endian precompile inputs
    - See https://github.com/ethereum/EIPs/pull/7020
- [x] Returning the modulus as an output for the precompile, see [#PR5864](https://github.com/ethereum/EIPs/pull/5864)
- [x] Fee Market design
    - [x] **[Solved by [PR#5707](https://github.com/ethereum/EIPs/pull/5353#issuecomment-1199277606)]** The current fee market for blob tracks the long-run average of blobs, which is different from EIP-1559 that tracks the short-term gas usage. This has implications on the most optimal way for blobs to be sent, i.e. whether there are many short bursts of blobs or a constant "stream" of them. See [here](https://github.com/ethereum/EIPs/pull/5353#issuecomment-1199277606) for more context. 
- [x] Blob Retention Period
    - **[Solved by [PR#3047](https://github.com/ethereum/consensus-specs/pull/3047)]** The longer blobs are stored, the higher the storage cost imposed on network nodes. The retention period needs to be set taking into account blob size [blocker], node sync time, and optimistic rollup fraud proof windows.
- [x] **Optional** Setting the minimum gas price for blobs >1 wei, see [PR#5862](https://github.com/ethereum/EIPs/pull/5862)
    - Decided against this in [Implementers' Call 5](https://github.com/ethereum/pm/issues/670)  

### Client-level Open Issues

- [ ] Re-orgs & Reintroduction of Externally Built Blob Transactions 
    - When a re-org happens, if a blob transaction was included via an externally built block, it currently is not possible to re-introduce it in the mempool for re-inclusion in a block. Either this is fine (and builders must manually re-submit such transactions), or CL clients must be modified to provide the blobs in the `newPayload` API calls
    - June 23 update: https://hackmd.io/aVek93y-QmSv1mz2Agc9iQ#Client-Implementations 
- [x] KZG support in Library
    - Need efficient library support for the cryptographic [operations](https://github.com/ethereum/consensus-specs/blob/dev/specs/eip4844/polynomial-commitments.md) required to verify and interact with blobs, compatible with all clients' programming language. 
        - [x] [Open issue in BLST](https://github.com/supranational/blst/issues/10)
- [x] Gossiping of blob transactions ([@MariusVanDerWijden](https://github.com/MariusVanDerWijden))
    - **[Resolved by introducing [`eth/68`](https://github.com/ethereum/EIPs/pull/5793)]** Large blob transactions are expensive to gossip over the network. Solution: enable node to announce & request specific transactions rather than gossip them by default.
    - [PR#5930](https://github.com/ethereum/EIPs/pull/5930)m makes `eth/68` a dependency of EIP-4844. 
- [x] Sync Strategy ([@djrtwo](https://github.com/djrtwo), [@terencechain](https://github.com/terencechain)) 
    - **[Resolved with [PR#3046](https://github.com/ethereum/consensus-specs/pull/3046)]** Blobs can either be synced coupled to CL blocks, or independently from them. The tradeoffs to each approach are explained [here](https://hackmd.io/_3lpo0FzRNa1l7XB0ELH7Q?view) and [here](https://notes.ethereum.org/RLOGb1hYQ0aWt3hcVgzhgQ?view). For both gossip and historical sync, blocks and blobs were decoupled.

### KZG Ceremony 
- [x] EIP-4844 requires a Powers of Tau ceremony to provide its cryptographic foundation. Resources relevant to the ceremony are available [here](https://github.com/ethereum/KZG-Ceremony). 
    - The KZG ceremony is now complete. It gathered more than 100,000 contributions, making it the largest such ceremony to date. 

### APIs
- [x] [Merge `getPayloadV3` and `getBlobsBundleV1`](https://github.com/ethereum/execution-apis/pull/402)
- [x] [Blob Sidecar Beacon API](https://github.com/Inphi/prysm/pull/21) ([@mdehoog](https://github.com/mdehoog))
- [x] [Engine API support](https://github.com/ethereum/execution-apis/pull/197)

## Testing 

**Note:** [this document](https://notes.ethereum.org/@ethpandaops/dencun-testing-overview) is currently being used to track testing efforts. The sections below may be out of date. 

### Consensus Layer 
- [x] [consensus-specs tests](https://github.com/ethereum/consensus-specs/tree/dev/tests/core/pyspec)
    - See the [`deneb`](https://github.com/ethereum/consensus-specs/tree/dev/tests/core/pyspec/eth2spec/test/deneb) folder
- [x] Networking Overhead Analysis
    - Blobs add to the bandwidth requirements of the CL gossip network. Analysis on how many blobs should be included per block to maintain acceptable bandwidth and hardware constraints is required. Discussed in [Breakout Room #4](https://docs.google.com/document/d/1KgKZnb5P07rdLBb_nRCaXhzG_4PBoZXtFQNzKO2mrvc/edit#heading=h.t7yop7yz4l6m). [Proposed experiment](https://notes.ethereum.org/lQ_75o64R9q8ddt3M9M3tg?view) ([@djrtwo](https://github.com/djrtwo), [@terencechain](https://github.com/terencechain)) 
    - [x] [PR#5863](https://github.com/ethereum/EIPs/pull/5863) reduced the number of targetted blobs to 2, for a target of 0.25mb per block. 
- [ ] [Hive](https://github.com/ethereum/hive) tests
    - [ ] Beacon API Simulator

### Execution Layer
- [ ] [execution-spec-tests](https://github.com/ethereum/execution-spec-tests/tree/main/fillers/eips/eip4844#-execution-specification-test-cases), [tracker](https://github.com/ethereum/execution-spec-tests/issues/130)
    - [ ] RLP Blob Transactions
    - [x] [ExcessDataGas Header Field/Gas Accounting](https://github.com/ethereum/execution-spec-tests/blob/main/fillers/eips/eip4844/excess_data_gas.py)
    - [x] [DATAHASH Opcode](https://github.com/ethereum/execution-spec-tests/blob/main/fillers/eips/eip4844/datahash_opcode.py)
    - [ ] [Point Evaluation Precompile](https://github.com/ethereum/execution-spec-tests/pull/104/files)
- [ ] [Hive](https://github.com/ethereum/hive) tests
    - [ ] Docker resource constraints
    - [x] [Engine API Tests](https://github.com/ethereum/hive/pull/759)
        - [x] `engine_getPayloadV3`
        - [x] `engine_newPayloadV3`
        - [ ] Transaction Pool
            - [ ] Spam transactions
            - [ ] Invalid transactions
            - [ ] Fee market 
    - [ ] [Pyspec Update](https://github.com/ethereum/hive/pull/765)


### End-to-End
- [ ] [Hive](https://github.com/ethereum/hive) tests
    - [ ] Cancun Fork Simulator
    - [ ] Blob Expiry Tests
    - [ ] Builder API
        - [ ] Builder-Relayer Mock Tests
        - [ ] Real MEV-Boost Simulator
- [ ] [Sync tests](https://github.com/samcm/ethereum-sync-testing)
- [ ] Shadow forks 
    - [ ] Sepolia shadowfork
    - [ ] Goerli shadowfork
    - [ ] Mainnet shadowfork
    - [ ] Shadowfork with mock builder/relays
    - [ ] Shadowfork with public builders/relays
    - [ ] Non-finality tests
    
### Tooling 

- [x] [Devnet Faucet](https://eip4844-faucet.vercel.app/) ([@0xGabi](https://github.com/0xGabi))
- [x] [`blob-utils`](https://github.com/Inphi/blob-utils) 
- [x] [Explorer to visualize blobs](https://github.com/blossomlabs/blobscan) ([@0xGabi](https://github.com/0xGabi))

## Devnets 

See https://github.com/ethpandaops/dencun-testnet
