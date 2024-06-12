# London Ecosystem Readiness Checklist
Tooling, Libraries and other Infrastructure

See the [1559 Cheatsheet for Implementers](https://hackmd.io/4YVYKxxvRZGDto7aq7rVkg?view) for the latest resources to help you along.

If you know about a status update please add a PR to this document or post on the latest [update issue](https://github.com/ethereum/eth1.0-specs/issues/198) for aggregated inclusion on a weekly basis.

## London Network Upgrade

For a list of included EIPs see the [specification](./mainnet-upgrades/london.md) document.

Tracking: `active`
⭕ - Not Started
🛠️ - In Progress
✅ - Complete

### Developer Tools

| Name | Description | Dependencies | Work | EIPs | Release | Status
|---|---|---|---|---|---|---|
| [Hardhat][hardhat-link] |Framework |EthereumJS, Ethers |  | All |[v2.5.0][hardhat-release] | ✅
| [Truffle][truffle-link] |Framework |EthereumJS, Web3.js, Ethers |  | All | | 🛠️
| [DappTools][dapptools-link] |Framework | - | [URL][dapptools-work] | All | [v0.48.0][dapptools-release] | ✅ 
| [Remix][remix-link] | IDE |EthereumJS, Web3.js, Ethers |  | All |  | 🛠️
| [Waffle][waffle-link] |Framework |Ganache, Ethers.js, Typechain |  | All | | 🛠️
| [Brownie][brownie-link] |Framework |Web3.py |  | All | [v1.16.0][brownie-release] | ✅
| [OpenZeppelin][oz-link] |Smart Contract Security |Hardhat |  | ? | | 🛠️
| [Tenderly][tenderly-link] |Contract Monitoring |Hardhat |  | 1559 |N/A | ✅
| [hardhat-deploy][hardhat-deploy-link] |Contract Deployment |Hardhat, Ethers |  | ? | | ⭕
| [solidity-coverage][solidity-coverage-link] |Contract Testing |Hardhat, Solidity |  | ? | | ⭕
| [Typechain][typechain-link] |Language Tool |Ethers, Truffle, Hardhat, Web3.js, Solidity |  | ? | [Releases][typechain-release] | ✅
| [Solidity][solidity-link] |Language | - | | 3198 | [v0.8.7][solidity-release] | ✅

[hardhat-link]: https://github.com/nomiclabs/hardhat
[hardhat-release]: https://github.com/nomiclabs/hardhat/releases/tag/hardhat-core-v2.5.0
[truffle-link]: https://github.com/trufflesuite/truffle
[dapptools-link]: https://github.com/dapphub/dapptools
[remix-link]: https://github.com/ethereum/remix-project
[waffle-link]: https://github.com/EthWorks/Waffle
[brownie-link]: https://github.com/eth-brownie/brownie
[brownie-release]: https://github.com/eth-brownie/brownie/releases/tag/v1.16.0
[oz-link]: https://github.com/OpenZeppelin
[tenderly-link]: https://github.com/Tenderly
[hardhat-deploy-link]: https://github.com/wighawag/hardhat-deploy
[solidity-coverage-link]: https://github.com/sc-forks/solidity-coverage
[typechain-link]: https://github.com/ethereum-ts/TypeChain
[typechain-release]: https://github.com/ethereum-ts/TypeChain/releases
[solidity-link]: http://soliditylang.org
[solidity-release]: https://github.com/ethereum/solidity/releases/tag/v0.8.7
[dapptools-work]:https://github.com/dapphub/dapptools/pull/688
[dapptools-release]: https://github.com/dapphub/dapptools/releases/tag/hevm%2F0.48.0


### Libraries

| Name | Description | Dependencies | Work | EIPs | Release | Status
|---|---|---|---|---|---|---|
| [Web3.js][web3js-link] |Network API (JavaScript) | EthereumJS |  |1559 |[v1.5.0][web3js-release]   |✅ 
| [Ethers.js][ethers-link] |Network API (JavaScript) |  | [URL][ethers-work] |1559 |[v5.4.1][ethers-release]  |✅ 
| [EthereumJS][ethereumjs-link] |Libraries |  | [URL][ethereumjs-work] | All |[Releases][ethereumjs-release] |✅
| [Web3.py][web3py-link] |Network API (Python) |  | [URL][web3py-work] |1559 |[v5.21.0][web3py-release] |✅
| [Web3j][web3j-link] |Network API (Java) |  | [URL][web3j-work] |1559 |[v4.8.6][web3j-release]  |✅ 
| [Nethereum][nethereum-link] |Network API (.Net) |  |  |1559 |[v4.0.0][nethereum-release]  |✅
| [KEthereum][kethereum-link] |Network API (Kotlin) | | [URL][kethereum-work] |1559 |[v0.84.9][kethereum-release]  |✅

[web3js-link]: https://github.com/ChainSafe/web3.js
[web3js-release]: https://github.com/ChainSafe/web3.js/releases/tag/v1.5.0
[ethers-link]: https://github.com/ethers-io/ethers.js
[ethers-work]: https://github.com/ethers-io/ethers.js/issues/1610
[ethers-release]: https://github.com/ethers-io/ethers.js/releases/tag/v5.4.1
[ethereumjs-link]: https://github.com/ethereumjs/ethereumjs-monorepo
[ethereumjs-work]: https://github.com/ethereumjs/ethereumjs-monorepo/issues/1211
[ethereumjs-release]: https://github.com/ethereumjs/ethereumjs-monorepo/pull/1263#issuecomment-849429331
[web3py-link]: https://github.com/ethereum/web3.py
[web3py-work]: https://github.com/ethereum/web3.py/issues/1835
[web3py-release]: https://web3py.readthedocs.io/en/latest/releases.html#v5-21-0-2021-07-12
[web3j-link]: https://github.com/web3j/web3j
[web3j-work]: https://github.com/web3j/web3j/pull/1417
[web3j-release]: https://github.com/web3j/web3j/releases/tag/v4.8.6
[nethereum-link]: https://github.com/Nethereum/Nethereum
[nethereum-release]: https://github.com/Nethereum/Nethereum/releases/tag/4.0.0
[kethereum-link]: https://github.com/komputing/KEthereum
[kethereum-work]: https://github.com/komputing/KEthereum/issues/101
[kethereum-release]: https://github.com/komputing/KEthereum/commit/8c1386853301e792f798d148677812c04ff0e434

### Infrastructure

Many of these projects may not update until much closer to the designated London block number.

| Name | Description | Dependencies | Work | EIPs | Status
|---|---|---|---|---|---|
| [Amazon Web Services][AWS-link] |managed Ethereum nodes | Geth |  | 1559 | ✅
| [Blocknative][blocknative-link] |Mempool Explorer |  |  | 1559  |✅
| [Infura][infura-link] |Ethereum APIs |  |  | 1559  |✅
| [ETHGasStation][ethgasstation-link] | Metrics for the gas market | Web3.js | | 1559 |  |🛠️  
| [POKT][pocket-link] |Request API |  |  | 1559 |⭕ 
| [Etherscan][etherscan-link] |Block Explorer |  |  | 1559 |✅
| [MetaMask][metamask-link] |Browser Extension | EthereumJS, Ethers, Web3, ? | [URL][metamask-work] | 1559 |✅
| [Ethernodes][ethernodes-link] |Node Explorer | Eth 1.0 Clients |  | ? |✅ 
| [TREZOR][trezor-link] |Hardware Wallet |  | [URL][trezor-work] | 1559 |🛠️ 
| [WallETH][walleth-link] |Wallet | KEthereum | [URL][walleth-work] | 1559 |🛠️  
| [Ledger][ledger-link] |Hardware Wallet | Ethers | | 1559 |🛠️  


[AWS-link]: https://aws.amazon.com/managed-blockchain/
[blocknative-link]: https://github.com/blocknative
[infura-link]: https://github.com/INFURA
[pocket-link]: https://pokt.network/
[etherscan-link]: https://github.com/etherscan
[metamask-link]: https://github.com/MetaMask
[metamask-work]: https://github.com/MetaMask/metamask-mobile/issues/2571
[ethernodes-link]: https://www.ethernodes.org/
[trezor-link]: https://trezor.io
[trezor-work]: https://github.com/trezor/connect/pull/874
[walleth-link]: https://walleth.org
[walleth-work]: https://github.com/walleth/walleth/issues/523
[ledger-link]: https://ledger.com
[ethgasstation-link]: https://ethgasstation.info
