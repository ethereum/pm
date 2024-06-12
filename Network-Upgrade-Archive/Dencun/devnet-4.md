# EIP-4844 devnet-4 Spec
**note**: this file was copied from [here](https://notes.ethereum.org/@timbeiko/4844-devnet-4) for reference.

## CL: Use [v1.3.0-rc.1](https://github.com/ethereum/consensus-specs/releases/tag/v1.3.0-rc.1), including:

- gwei for withdrawal amounts for engine api
- historical summaries
- genesis fork version for bls changes

## EL: build on top of [Shanghai](https://github.com/ethereum/execution-specs/blob/master/network-upgrades/mainnet-upgrades/shanghai.md), including:

- [EIP-6122 : Forkid checks based on timestamps](https://github.com/ethereum/EIPs/pull/6122)
- [EIP-4895 update: CL-EL withdrawals harmonization: using units of Gwei](https://github.com/ethereum/EIPs/commit/b56a299fbad4ee701e6d4cea025096effaf301fa)
- [EIP-4844 update: clarify datahash return value](https://github.com/ethereum/EIPs/commit/739e75c93b94fc49e8005943d052fa4e1ac1be80)

## Engine API @ [Commit 59a369a](https://github.com/ethereum/execution-apis/tree/59a369a7b9d9c05e37c53aacac7ac6ea23fc62f6), including:

- [make engine_getPayloadVN fork agnostic](https://github.com/ethereum/execution-apis/pull/355)
- [CL-EL withdrawals harmonization: using units of Gwei](https://github.com/ethereum/execution-apis/pull/354)
