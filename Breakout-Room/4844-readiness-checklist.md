# EIP-4844 Readiness Checklist

This document is meant to capture various tasks that need to be completed before EIP-4844 is ready to be scheduled for mainnet deployement. Github handles for owners of various tasks are indicated between parentheses beside the task. If are working on something not listed here, please open a PR against this file to indicate it. 

## Specs

- [Meta Spec & Resources](https://hackmd.io/@protolambda/eip4844-meta)
- [EL: EIP-4844](https://eips.ethereum.org/EIPS/eip-4844)
- [CL: consensus-specs](https://github.com/ethereum/consensus-specs/tree/dev/specs/eip4844)

## Implementation

### Client Implementation Status 

#### Execution Layer 

| Client | Status | Link | 
| ------ | ------ | ---- | 
| go-ethereum | WIP Prototype | [Link](https://github.com/mdehoog/go-ethereum/tree/eip-4844) | 
| Nethermind | Issue Opened | [Link](https://github.com/NethermindEth/nethermind/issues/4558) | 
| Erigon | N/A | 
| Besu | N/A | 

#### Consensus Layer 

| Client | Status | Link | 
| ------ | ------ | ---- | 
| Prysm | WIP prototype & production implementations | [devnet prototype](https://github.com/Inphi/prysm/tree/eip-4844), [prysm production](https://github.com/terencechain/prysm/tree/eip4844) |
| Teku | Issue Opened | [Link](https://github.com/ConsenSys/teku/issues/5681) 
| Lighthouse | WIP implementation | [Link](https://github.com/sigp/lighthouse/tree/eip4844)  
| Lodestar | N/A |  
| Nimbus | N/A |  

#### Resources 
 - [CL Implementation Considerations](https://hackmd.io/@terencechain/ByH4cbMfi) 

### Spec-level Open Issues 

- [ ] Fee Market design ([@adietrichs](https://github.com/adietrichs)) 
    - [x] **[Fixed in [PR#5707](https://github.com/ethereum/EIPs/pull/5353#issuecomment-1199277606)]** The current fee market for blob tracks the long-run average of blobs, which is different from EIP-1559 that tracks the short-term gas usage. This has implications on the most optimal way for blobs to be sent, i.e. whether there are many short bursts of blobs or a constant "stream" of them. See [here](https://github.com/ethereum/EIPs/pull/5353#issuecomment-1199277606) for more context. 
    - [ ] A minimum gas price for blobs needs to be determined, see [PR#5862](https://github.com/ethereum/EIPs/pull/5862)
- [ ] **WIP**: Exposing the Modulus in precompile
    - See [this comment](https://github.com/ethereum/EIPs/pull/5864#issuecomment-1298528724)
- [ ] **WIP**: KZG Ceremony ([@tvanepps](https://github.com/tvanepps) & [@CarlBeek](https://github.com/CarlBeek))
    - EIP-4844 requires a Powers of Tau ceremony to provide its cryptographic foundation. Resources relevant to the ceremony are available [here](https://github.com/ethereum/KZG-Ceremony) 
- [x] Blob Retention Period
    - **[Resolved by [PR#3047](https://github.com/ethereum/consensus-specs/pull/3047)]** The longer blobs are stored, the higher the storage cost imposed on network nodes. The retention period needs to be set taking into account blob size [blocker], node sync time, and optimistic rollup fraud proof windows.


### Client-level Open Issues

- [ ] KZG support in Library
    - Need efficient library support for the cryptographic operations required to verify and interact with blobs, compatible with all clients' programming language. 
    - **WIP**: [c-kzg](https://github.com/dankrad/c-kzg/tree/lagrange_form), an implementation in C based on BLST ([@dankrad](https://github.com/dankrad))
    - **WIP**: [BLST](https://github.com/supranational/blst) support for this ([@asn-d6](https://github.com/asn-d6))
- [ ] Networking Overhead Analysis
    - As per the current spec, blobs can be up to 2MB in size. This adds to the bandwidth requirements of the CL gossip network. Analysis about whether this value acceptable given current bandwidth and hardware constraints is missing. Discussed in [Breakout Room #4](https://docs.google.com/document/d/1KgKZnb5P07rdLBb_nRCaXhzG_4PBoZXtFQNzKO2mrvc/edit#heading=h.t7yop7yz4l6m). 
    - **WIP** [Proposed experiment](https://notes.ethereum.org/lQ_75o64R9q8ddt3M9M3tg?view) ([@djrtwo](https://github.com/djrtwo), [@terencechain](https://github.com/terencechain)) 
    - Results from this can inform both the blob size and blob retention period. 
- [x] Gossiping of blob transactions ([@MariusVanDerWijden](https://github.com/MariusVanDerWijden))
    - **[Resolved by introducing [`eth/68`](https://github.com/ethereum/EIPs/pull/5793)]** Large blob transactions are expensive to gossip over the network. Solution: enable node to announce & request specific transactions rather than gossip them by default.
- [x] Sync Strategy ([@djrtwo](https://github.com/djrtwo), [@terencechain](https://github.com/terencechain)) 
    - **[Resolved with [PR#3046](https://github.com/ethereum/consensus-specs/pull/3046)]** Blobs can either be synced coupled to CL blocks, or independently from them. The tradeoffs to each approach are explained [here](https://hackmd.io/_3lpo0FzRNa1l7XB0ELH7Q?view) and [here](https://notes.ethereum.org/RLOGb1hYQ0aWt3hcVgzhgQ?view). **For gossip, block and blobs will be coupled. For historical sync, they will be decoupled.** 

### APIs
- [ ] **WIP**: [Blob Sidecar Beacon API](https://github.com/Inphi/prysm/pull/21) ([@mdehoog](https://github.com/mdehoog))
- [ ] **WIP**: [Engine API support](https://github.com/ethereum/execution-apis/pull/197)

## Testing 

- [ ] Simple JSON test vectors (example from [early merge devnets](https://notes.ethereum.org/@MariusVanDerWijden/rkwW3ceVY))
- [ ] Node performance monitoring ([@booklearner](https://github.com/booklearner)) 
- [ ] [Transaction fuzzing](https://github.com/MariusVanDerWijden/tx-fuzz) ([@MariusVanDerWijden](https://github.com/MariusVanDerWijden))
- [ ] Differential fuzzing 

#### Consensus Layer 
- [ ] [consensus-specs tests](https://github.com/ethereum/consensus-specs/tree/dev/tests/core/pyspec)
    - See the [`eip4844`](https://github.com/ethereum/consensus-specs/tree/dev/tests/core/pyspec/eth2spec/test/eip4844) folder

#### Execution Layer
- [ ] [State/blockchain](https://github.com/ethereum/tests) tests 
    - [ ] Block Header changes
    - [ ] Transaction format 
    - [ ] `DATAHASH` opcode
    - [ ] Point evaluation precompile
- [ ] [Hive](https://github.com/ethereum/hive) tests
    - [ ] Docker resource constraints
    - [ ] CL mocker update 
- [ ] Transaction Pool
    - [ ] Spam transactions
    - [ ] Invalid transactions
    - [ ] Fee market 


#### Other
- [ ] [Network impact of large blobs](https://notes.ethereum.org/@djrtwo/rkgZs-YVMi) (Prysm looking into it, but other NOs welcome to join) 

#### Tooling 

- [x] [Devnet Faucet](https://eip4844-faucet.vercel.app/) ([@0xGabi](https://github.com/0xGabi))
- [x] [`blob-utils`](https://github.com/Inphi/blob-utils) 
- [x] **WIP** [Explorer to visualize blobs](https://github.com/blossomlabs/blobscan) ([@0xGabi](https://github.com/0xGabi))

### Devnets 

- [x] [Devnet v1](https://hackmd.io/@inphi/SJMXL1P6c)
- [x] [Devnet v2](https://hackmd.io/@inphi/SJKLtgJXs) 


  
