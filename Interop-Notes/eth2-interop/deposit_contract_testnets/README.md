# Guidelines for Eth2 testnets using a deposit contract

This document provides a set of implementation guidelines for clients, aiming to simplify the interoperability testing in Eth2 phase 0 testnets using an Eth1 validator deposit contract.

## Client-operated testnets

An Eth2 testnet can be identified by an address of a deployed validator deposit contract, running on the Görli network. Multiple testnets can be running at the same time and all client teams are encouraged to deploy as many contracts as they see fit. 

To facilitate discovering and connecting to existing testnets, all client teams are encouraged to publish metadata files for their active testnets in the following repository:

https://github.com/eth-clients/eth2-testnets

Please create a sub-folder for your team, where each active testnet will be stored as a nested sub-folder with a descriptive name. For example: 

```
trinity/1000_validators_testnet/bootstrap_nodes.txt
trinity/1000_validators_testnet/deposit_contract.txt
trinity/1000_validators_testnet/config.yaml
trinity/1000_validators_testnet/genesis.ssz
```

The `config.yaml` file is optional and it specifies the [Eth2 constants parameters](https://github.com/ethereum/eth2.0-specs/tree/dev/configs) used by the testnet. When no config file is present, it should be assumed that the testnet is using the `minimal` config. Users are expected to check each client's documentation for instructions regarding the usage of config preset files. Config presets are usually specified either at build-time or at run-time depending on the client.

`bootstrap_nodes.txt` is a line-delimited text file with [multiaddr](https://github.com/multiformats/multiaddr) records for the bootstrap nodes of the testnet. For example:

```
/ip4/10.20.30.40/tcp/9100/p2p/16Uiu2HAmEAmp4FdpPzypKwTMmsbCdnUafDvXZCpFrUDbYJZNk7hX
/ip4/10.20.30.50/tcp/9100/p2p/16Uiu2HAmV5SpcmrEymmaj1mymSHkbMpMVUXFRiXRxpHkfWdQ7bi3
```

To connect to the testnet, the user should either pass the entire file as a command-line parameter named `--bootstrap-file` or she should specify the individual entries with a repeatable command-line parameter named `--bootstrap-node`.

`deposit_contract.txt` is a single-line text file with the address of the testnet's deposit contract on the Görli network. To connect to the testnet, the user should specify the address as a command-line parameter named `--deposit-contract`. If the used constants preset specifies a non-empty value for the `DEPOSIT_CONTRACT_ADDRESS` constant, it should be used as the default value for this parameter. The supplied address consists of 20 bytes encoded in hex form and prefixed with "0x".

The `genesis.ssz` represents the genesis state snapshot. The user should specify the path to this file with a command-line parameter named `--state-snapshot`.

Any additional information and instructions for interacting with the specific testnet can be provided in a README file in the same folder.

### Making deposits

To obtain the 32 GöETH required for making a deposit, please use the social faucet at https://faucet.goerli.mudit.blog/

It's expected that the users will use a web-site or a command-line command provided by the client to make a deposit.

### Creating testnets

Please note that a testnet genesis file can feature a pre-populated validator set. The monitoring of Eth1 deposit events should start from the Eth1 block referenced in the `.eth1_data.eth1_block_hash` field of the genesis state. Thus, to create a testnet, you need to deploy a new deposit contract and then generate a genesis state that references a recent Görli block hash.

The client teams may choose any of the following options when generating a new testnet:

* **Start with a empty validator set**
  This mimics the future mainnet setup. The genesis event will be triggered when `MIN_GENESIS_ACTIVE_VALIDATOR_COUNT` deposits are made (according the used config).

* **Start with randomly generated keys**
  The randomly generated keys can be distributed to nodes operated by the client team. The testnet can start immediately and the users can use the deposit contract to become validators.
  
* **Start with a mix of random and mock start keys**
  The secret random keys can be used by the client team, while the mock start keys can be freely used by the users (yes, this will give us a chance to test the slashing conditions).

To facilitate the reuse of GöETH, the client teams may choose to modify the deposit contract by adding additional features such as the ability to [drain the accumulated funds](https://github.com/prysmaticlabs/prysm/blob/master/contracts/deposit-contract/depositContract.v.py#L121).


## Official multi-client testnet

After significant progress is reached in client-operated testnets, the EF will deploy an official multi-client testnet. Metadata files will be published in the following folder:

https://github.com/eth-clients/eth2-testnets/serenity-phase0

