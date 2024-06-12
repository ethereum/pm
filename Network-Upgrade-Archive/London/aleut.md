# Client Integration Testnet Specification - Aleut

**Disclaimer: This network will soon be shut down in favor of [Baikal](/network-upgrades/client-integration-testnets/baikal.md).**

The specification for the Aleut Client Integration Tesnet. Clients who wish to sync need to implement the following features into their client. It is for testing basic infrastructure and will be deprecated.

## Specification

**Name:** Aleut

**ID:** `Aleut`

**ChainId:** `7822` # The deepest part of the Aleutian trench has been measured at 7,822 metres

**Genesis File:**

<details>
  <summary>aleut.json</summary>

  ```json
  {
   "config":{
      "chainId":7822,
      "homesteadBlock":0,
      "daoForkSupport":false,
      "eip150Block":0,
      "eip155Block":0,
      "eip158Block":0,
      "byzantiumBlock":0,
      "constantinopleBlock":0,
      "petersburgBlock":0,
      "istanbulBlock":0,
      "muirGlacierBlock":0,
      "berlinBlock":0,
      "aleutBlock":10,
      "clique":{
         "blockperiodseconds":15,
         "epochlength":30000
      }
   },
   "difficulty":"0x400",
   "extraData":"0x000000000000000000000000000000000000000000000000000000000000000036267c845cc42b57ccb869d655e5d5fb620cc69a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
   "gasLimit":"0x1312D00",
   "alloc":{
      "fe3b557e8fb62b89f4916b721be55ceb828dbd73":{
         "balance":"90000000000000000000000"
      },
      "627306090abaB3A6e1400e9345bC60c78a8BEf57":{
         "balance":"90000000000000000000000"
      },
      "f17f52151EbEF6C7334FAD080c5704D77216b732":{
         "balance":"90000000000000000000000"
      },
      "b8c3bfFb71F76BeE2B2f81bdBC53Ad4C43e3f58E":{
         "balance":"90000000000000000000000"
      },
      "0x60AdC0F89a41AF237ce73554EDe170D733ec14E0":{
         "balance":"90000000000000000000000"
      }
   }
}

  ```
</details>

**Static Nodes:**

<details>
  <summary>static-nodes.json</summary>

  ```json
  [
    "enode://0c72e2b7873e4342d725b5990c17adb2b159aad2ff5853de7e4910b25522a1f9e78f9cd802a8a3225b8fae4e994e522b50d6bd5a163eb3a7b49a0a73ca9a1c7e@3.12.166.199:30303",
    "enode://aec88fd902744bf67705c098bf532b01017ccc3a156395508e2d9c4e7c22699ecccae1e7316614f8a2d4c5698a9be3fe6151ee25b9ed4aa052f88e112c65387a@164.90.171.157:31559",
    "enode://8e6788508278e514268307f27528ffabd6c86e755b0abd5ef170502b6444b35231dd0c7183e902c6a566c650104fdcfa58c6de28b54533f3dc243af444a60f51@quilt.link:30308"
  ]
  ```
</details>

**Included EIPs:**
  - [x] [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559) Commit Hash - [79f4fe6cbe0d323dfac7412270c6e8cf33e62af3](https://github.com/ethereum/EIPs/commit/79f4fe6cbe0d323dfac7412270c6e8cf33e62af3)
  - [x] [EIP-3198](https://eips.ethereum.org/EIPS/eip-3198) Commit Hash - [081db1a6614e523dd791691cff7016e32c369912](https://github.com/ethereum/EIPs/commit/081db1a6614e523dd791691cff7016e32c369912)

## Client Consensus -> Implementation

| **Client**   | Repo                     | Signal | Spec | Merged | Syncing |
|--------------|--------------------------|--------|------|--------|---------|
| Besu         | [URL][besu-repo]         | x      | x    | x      | x       |
| Geth         | [URL][geth-repo]         | x      | x    |        | x       |
| Nethermind   | [URL][nethermind-repo]   | x      | x    | x      | x       |
| OpenEthereum | [URL][openethereum-repo] | x      | x    |        |         |
| EthereumJS   | [URL][ethereumjs-repo]   | x      | x    |        |         |
| TurboGeth    | [URL][turbogeth-repo]    | x      | x    | x      | x       |


**Signal** -
Client intends to participate. *(You are on the bus)*

**Spec** -
Client is satisfied with the proposed specification. *(You agree with the direction)*

**Merge** -
Changes are implemented in the client and configurable for the network. *(You are ready to hit the gas and go)*

**Syncing**
Client syncs with the network

## Syncing Instructions:

TBA

## Copyright
Copyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).


[besu-repo]: https://github.com/hyperledger/besu
[geth-repo]: https://github.com/ethereum/go-ethereum
[nethermind-repo]: https://github.com/NethermindEth/nethermind
[openethereum-repo]: https://github.com/openethereum/openethereum
[ethereumjs-repo]: https://github.com/ethereumjs/ethereumjs-monorepo/tree/master/packages/client
[turbogeth-repo]: https://github.com/ledgerwatch/turbo-geth
