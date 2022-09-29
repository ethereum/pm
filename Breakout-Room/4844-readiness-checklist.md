# EIP-4844 Readiness Checklist

This document is meant to capture various tasks that need to be completed before EIP-4844 is ready to be scheduled for mainnet deployement. 

## Implementation

### Client Implementation Status 

#### Execution Layer 

| Client | Status | Link | 
| ------ | ------ | ---- | 
| go-ethereum | WIP Prototype | [Link](https://github.com/mdehoog/go-ethereum/tree/eip-4844) | 
| Nethermind | Issue Opened | [Link](https://github.com/NethermindEth/nethermind/issues/4558) | 
| Erigon | Not Started | 
| Besu | Not Started | 

#### Consensus Layer 

| Client | Status | Link | 
| ------ | ------ | ---- | 
| Prysm | WIP prototype | [Link](https://github.com/Inphi/prysm/tree/eip-4844) |
| Teku | Issue Opened | [Link](https://github.com/ConsenSys/teku/issues/5681) 
| Lighthouse | N/A | N/A 
| Lodestar | N/A | N/A 
| Nimbus | N/A | N/A 

### Spec-level Open Issues 

- [ ] Fee Market design 
    - The current fee market for blob tracks the long-run average of blobs, which is different from EIP-1559 that tracks the short-term gas usage. This has implications on the most optimal way for blobs to be sent, i.e. whether there are many short bursts of blobs or a constant "stream" of them. See [here](https://github.com/ethereum/EIPs/pull/5353#issuecomment-1199277606) for more context. 
    - WIP: [PR: changes to fee market to address the above and other issues](https://github.com/ethereum/EIPs/pull/5707)
- [ ] WIP: KZG Ceremony (@tvanepps & @CarlBeek leading)
    - EIP-4844 requires a Powers of Tau ceremony to provide its cryptographic foundation. Resources relevant to the ceremony are available [here](https://github.com/ethereum/KZG-Ceremony) 

### Client-level Open Issues

- [ ] KZG support in Library
    - No efficient library supports the cryptographic operations required to verify and interact with blobs. 
    - WIP: [BLST](https://github.com/supranational/blst) support for this (@asn-d6 tracking)
    - WIP: [c-kzg](https://github.com/dankrad/c-kzg/tree/lagrange_form), an implementation in C based on BLST (@dankrad leading)
- [ ] Sync Strategy
    - Blobs can either be synced coupled to CL blocks, or independently from them. The tradeoffs to each approach are explained [here](https://hackmd.io/_3lpo0FzRNa1l7XB0ELH7Q?view)    
- [ ] Networking Overhead Analysis
    - As per the current spec, blobs can be up to 2MB in size. This adds to the bandwidth requirements of the CL gossip network. Analysis about whether this value acceptable given current bandwidth and hardware constraints is missing. 

### APIs

- [ ] WIP: [Blob Sidecar Beacon API](https://github.com/Inphi/prysm/pull/16)


## Testing 

#### Consensus Layer 
- [ ] WIP: [consensus-specs tests](https://github.com/ethereum/consensus-specs/tree/dev/tests/core/pyspec)
    - See the [`eip4844`](https://github.com/ethereum/consensus-specs/tree/dev/tests/core/pyspec/eth2spec/test/eip4844) folder

#### Execution Layer
- [ ] [State/blockchain](https://github.com/ethereum/tests) tests 
- [ ] [Hive](https://github.com/ethereum/hive) tests

#### Tooling 

- [x] [Devnet Faucet](https://eip4844-faucet.vercel.app/) (owner: @0xGabi)
- [x] [`blob-utils`](https://github.com/Inphi/blob-utils) 

### Devnets 

- [x] [Devnet v1](https://hackmd.io/@inphi/SJMXL1P6c)
- [ ] Devnet v2 
    - TODO: 
        - [ ] Fee Market changes merged  


  
