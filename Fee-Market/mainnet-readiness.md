# EIP-1559 Mainnet Readiness Checklist

This document was originally meant to capture various tasks that need to be completed before EIP-1559 is ready to be considered for mainnet deployement. EIP-1559 is now included in the London upgrade, so this document should serve as a historical reference. Sections may be updated if they are still the main source of truth for the efforts. 

## Implementation

### Client Implementation Status 

- See the [London specification](https://github.com/ethereum/eth1.0-specs/blob/master/network-upgrades/mainnet-upgrades/london.md#client-readiness-checklist).

### Client-level Open Issues

- [x] DoS risk on the Ethereum mainnet
    - Discussed in the [AllCoreDevs call #77](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2077.md#eip-1559) and [#97](https://github.com/ethereum/pm/pull/214/files?short_path=4d89329#diff-4d893291250cf226c77e67ad708be6f2) EIP-1559's elastic block size effectively doubles the potential effect of a DoS attack on mainnet. Solutions to this are outside the scope of this EIP and include things like [snapshot sync](https://blog.ethereum.org/2020/07/17/ask-about-geth-snapshot-acceleration/) and [EIP-2929](https://eips.ethereum.org/EIPS/eip-2929), which was deployed in Berlin. 
    - [Write up](https://notes.ethereum.org/@vbuterin/eip_1559_spikes) by Vitalik about why this is perhaps solved once EIP-2929 is live. 
    - Because EIP-1559's `BASE FEE` rises based on block gas utilisation, a DoS on the network would either have an exponentially increasing cost (assuming no collaboration from miners and other transactions are allowed to go through), compared to a constant cost today, or it would be costly to miners (who would need to pay the `BASE FEE` or censor the chain long enough to drop it to 0), compared to effectively free today. 
- [X] Performance overhead for clients 
    - It is unclear that Ethereum clients can handle "200% full" blocks for a modest amount of time without their performance being significantly affected. To test this, we are running simulations on testnets with a similar state size to the Ethereum mainnet. 
    - [Preliminary testing results](https://hackmd.io/@timbeiko/1559-prelim-perf)
    - [Large State Performance Testing](https://hackmd.io/@timbeiko/1559-perf-test)
- [X] Transaction Pool Management
    - Good approaches to transaction pool management have been put forward. [First write up](https://hackmd.io/@adietrichs/1559-transaction-sorting), [Second write up](https://hackmd.io/@adietrichs/1559-transaction-sorting-part2). 
    - [Alternative approach suggested by @zsfelfoldi](https://gist.github.com/zsfelfoldi/9607ad248707a925b701f49787904fd6)
- [x] Transaction Encoding/Decoding
    - EIP-1559 transactions will be encoded using [EIP-2718](https://eips.ethereum.org/EIPS/eip-2718), by adding 1559-style transactions as a new type of transaction. 
- [X] Legacy transaction management in transaction pool 
    - Solved by a [recent change to the EIP](https://github.com/ethereum/EIPs/pull/2924) which removes the need for two transaction pools by interpreting legacy transactions as 1559-styles transactions where the `feecap` is set to the `gas price` and the `tip` is set to `feecap - base fee`. 
- [X] Transition Period 
    - Solved by a [recent change to the EIP](https://github.com/ethereum/EIPs/pull/2924) which removes the need for a transition period by interpreting legacy transactions as 1559-styles transactions. This means legacy transactions will be supported until an explicit change to the protocol is made to deprecate them. 
- [X] `BASE FEE` Opcode - [EIP-3198](https://github.com/ethereum/EIPs/pull/3198)
    - A `BASE FEE` opcode will allow smart contracts to retrieve it directly.

### Testing 

#### Reference Tests 

- [x] Reference / Consensus Tests 
  - https://github.com/ethereum/tests/tree/develop/BlockchainTests/ValidBlocks/bcEIP1559
  - https://github.com/ethereum/tests/tree/develop/BlockchainTests/InvalidBlocks/bcEIP1559
  - https://github.com/ethereum/tests/tree/develop/BlockchainTests/GeneralStateTests/stEIP1559
  - (Nethereum) https://gist.github.com/juanfranblanco/4cc998247aecd822d6088e382d94a6f1

#### JSON RPC Support 

- [x] EIPs that return block or transaction data need to be updated to support EIP-1559/2718 style transactions. Updates are being made to the JSON RPC specification [here](https://github.com/ethereum/eth1.0-specs/pull/47). 

#### Community testing

- [x] JSON-RPC or equivalent commands that applications and tooling can use to interact with EIP-1559 
    - [x] [EIP-1559 Toolbox](http://eip1559-tx.ops.pegasys.tech/)
- [x] Public testnet that applications and tooling can use to test EIP-1559. 
    - [x] See the [Baikal devnet](https://github.com/ethereum/eth1.0-specs/blob/master/network-upgrades/client-integration-testnets/baikal.md) 

### Testnets 

- [x] Tooling to generate usage spikes on testnets;
    - [WIP by the Besu team](https://github.com/PegaSysEng/eip1559-tx-sender/) 
- [x] Multi-client PoA testnet to ensure spec can be implemented;
    - WIP between Geth, Besu & Nethermind teams. 
- [X] Single-client PoW testnet to ensure the spec works with PoW
    - Done by Besu team.
- [X] Multi-client PoW testnet to ensure all code paths are tested; 
    - The Rhoades testnet is a multi-client PoW testnet ([link](https://hackmd.io/@timbeiko/1559-perf-test))
- [X] Large state testnet to analyze performance with ~100M accounts on chain. 
    - The Rhoades testnet has 100m accounts and contract storage slots ([link](https://hackmd.io/@timbeiko/1559-perf-test))

### Other Testing

- [x] Nethermind is using EIP-1559 as part of a client's network
- [x] [Filecoin](https://filecoin.io/blog/roadmap-update-august-2020/), [Celo](https://docs.celo.org/celo-codebase/protocol/transactions/gas-pricing) and [NEAR](https://insights.deribit.com/market-research/transaction-fee-economics-in-near/) have implementations of EIP-1559 in their networks 

## R&D 

### Theoretical Analysis 

- [x] Analysis of whether EIP-1559 is game-theoretically sound, and potential improvements
    - ["Transaction Fee Mechanism Design for the Ethereum Blockchain:
An Economic Analysis of EIP-1559" by Tim Roughgarden](http://timroughgarden.org/papers/eip1559.pdf)
    - [EIP-1559 slides by Vitalik Buterin](https://vitalik.ca/files/misc_files/EIP_1559_Fee_Structure.pdf) 
    - [Blockchain Resource Pricing by Vitalik Buterin](https://github.com/ethereum/research/blob/master/papers/pricing/ethpricing.pdf) 
- [x] Comparison of EIP-1559 with alternatives (e.g. [Escalator Fees](https://eips.ethereum.org/EIPS/eip-2593))
    - ["Transaction Fee Mechanism Design for the Ethereum Blockchain:
An Economic Analysis of EIP-1559" by Tim Roughgarden](http://timroughgarden.org/papers/eip1559.pdf)
    - [Analysis by Deribit](https://insights.deribit.com/market-research/analysis-of-eip-2593-escalator/)
    - ["Floating escalator" simulation](https://github.com/barnabemonnot/abm1559/blob/master/notebooks/floatingEscalator.ipynb) to model using the [escalator fees](https://eips.ethereum.org/EIPS/eip-2593) approach to the EIP-1559 tip parameter.

### Simulations

- [X] [Agent-Based Simulations of EIP-1559](https://github.com/barnabemonnot/abm1559#abm1559)
- [X] [Legacy vs EIP 1559 users in post EIP 1559 world](https://github.com/NethermindEth/research/blob/main/legacyTransactions.ipynb)
- [X] [Manipulation of the basefee in the context of EIP-1559](https://medium.com/nethermind-eth/the-manipulation-of-the-basefee-in-the-context-of-eip-1559-4b082898271c)

## Community Outreach

- [X] Community outreach to projects to gather feedback on EIP-1559 
    - [Initial report published by the Ethereum Cat Herders](https://medium.com/ethereum-cat-herders/eip-1559-community-outreach-report-aa18be0666b5). Feedback still can be shared [here](https://forms.gle/bsdgBtG8g7KYnQL48). More wallet and exchange feedback is still needed. An update to the report may be published once more feedback has been gathered.  
    - [Second outreach round, where projects can now signal their support](https://github.com/ethereum-cat-herders/1559-outreach)
- [X] Outreach to miners to better understand their objections to 1559, and stance if it is to be deployed on mainnet. 
    - A discord channel has been created for miners to voice their concerns about EIP-1559
    - A community call has been organized for miners and other stakeholders to discuss EIP-1559's impact 
