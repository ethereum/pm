# pectra-devnet-0 specs

> [!NOTE]
> This spec was originally published at https://notes.ethereum.org/@ethpandaops/pectra-devnet-0

> [!NOTE]
> 📣 Devnet-0 starts on TBD and it will be terminated at TBD.

## EIP List for pectra-devnet-0
[EIP-2537: Precompile for BLS12-381 curve operations](https://eips.ethereum.org/EIPS/eip-2537)
[EIP-6110: Supply validator deposits on chain](https://eips.ethereum.org/EIPS/eip-6110)
[EIP-7002: Execution layer triggerable exits](https://eips.ethereum.org/EIPS/eip-7002)
[EIP-7251: Increase the MAX_EFFECTIVE_BALANCE](https://eips.ethereum.org/EIPS/eip-7251)
[EIP-7549: Move committee index outside Attestation](https://eips.ethereum.org/EIPS/eip-7549)


## Client implementation tracker
| Client/EIP|[EIP-6110](https://eips.ethereum.org/EIPS/eip-6110)|[EIP-7002](https://eips.ethereum.org/EIPS/eip-7002)|[EIP-7251](https://eips.ethereum.org/EIPS/eip-7251)| [EIP-7549](https://eips.ethereum.org/EIPS/eip-7549)|[EIP-2537](https://eips.ethereum.org/EIPS/eip-2537)|
|-|-|-|-|-|-|
|Lighthouse|:heavy_check_mark:|:eyes:|:hammer_and_wrench: |:hammer_and_wrench: | N/A |
|[Teku](https://github.com/Consensys/teku/labels/Epic%20Electra)|:heavy_check_mark:|:heavy_check_mark:|:eyes:|:hammer_and_wrench:| N/A |
|[Lodestar](https://github.com/ChainSafe/lodestar/issues/6341)  |:heavy_check_mark:|:hammer_and_wrench:|:heavy_check_mark:|:hammer_and_wrench:| N/A |
|[Prysm](https://github.com/prysmaticlabs/prysm/issues/13849)|:eyes:|:eyes:|:hammer_and_wrench: |:eyes:|N/A |
|Nimbus    |:eyes:|:eyes:|:eyes:|:eyes:| N/A |
|Grandine  |:eyes:|:eyes:|:eyes:|:eyes:| N/A |
|Geth      |:hammer_and_wrench:|:hammer_and_wrench:|N/A|N/A|:hammer_and_wrench:|
|[Nethermind](https://github.com/NethermindEth/nethermind/issues/6867)|:hammer_and_wrench:|:hammer_and_wrench:|N/A|N/A|:heavy_check_mark:|
|Besu      |:question:|:question:|N/A|N/A|:question:|
|Erigon    |:hammer_and_wrench:|:question:|N/A|N/A|:heavy_check_mark:|
|[Reth](https://github.com/paradigmxyz/reth/issues/7363)|:eyes:|:eyes:|:eyes:|N/A|:eyes:|

## [Docker images](https://github.com/ethpandaops/pectra-testnet/blob/master/ansible/inventories/devnet-0/group_vars/all/images.yaml) for devnet 0

### Open issues

N/A

### Spec changes for pectra-devnet-0

**Consensus Spec** 

[PR-3615 - Init Electra (EIP6110 + EIP7002)](https://github.com/ethereum/consensus-specs/pull/3615)- Open :exclamation:

#### EIP-6110
[PR-3629 - EIP-6110: rename get_eth1_deposit_count function](https://github.com/ethereum/consensus-specs/pull/3629) - Open :exclamation: 

#### EIP-7549
[PR-3628 - EIP-7549: Clarify network vs on chain aggregation](https://github.com/ethereum/consensus-specs/pull/3628)- Merged :heavy_check_mark:

#### EIP-7251
[PR-3647 - EIP-7251: Use MIN_ACTIVATION_BALANCE instead of MAX_EFFECTIVE..](https://github.com/ethereum/consensus-specs/pull/3647) - Merged :heavy_check_mark:

[PR-3636 - EIP-7251: misc changes](https://github.com/ethereum/consensus-specs/pull/3636) - Open :exclamation: 

**Execution EIPs**

[PR-8310 - Update EIP-2537](https://github.com/ethereum/EIPs/pull/8310) - Open :exclamation:

**Engine API**
[PR-528 - EIP-7002: Added engine_getPayloadV4 and engine_newPayloadV4 for Prague](https://github.com/ethereum/execution-apis/pull/528) - Open :exclamation:

[PR-531 - Add EIP-6110 to Prague](https://github.com/ethereum/execution-apis/pull/531) - Merged :heavy_check_mark:

[PR-532 - Add EIP-7251 to Prague](https://github.com/ethereum/execution-apis/pull/532) - Open :exclamation:

**Beacon API** 

N/A

**Builder Spec**

N/A
