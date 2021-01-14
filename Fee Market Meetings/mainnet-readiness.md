# EIP-1559 Mainnet Readiness Checklist

This document is meant to capture various tasks that need to be completed before EIP-1559 is ready to be considered for mainnet deployement. This list is a work in progress and tries to aggregate known requirements. More things may be added in the future and checking every box is not a guarantee of mainnet deployement. 

Tasks that are normally part of the "AllCoreDevs process" are not listed. In other words, this list is what should ideally be done _before_ moving EIP-1559 through the regular network upgrade process. This list is not exhaustive. A full list of 1559 resources is available [here](https://hackmd.io/@timbeiko/1559-resources). 

## Implementation

### Client Implementation Status 
- [ ] **Geth**
    - [WIP implementation led by Vulcanize](https://github.com/vulcanize/go-ethereum/tree/1559_test)
- [ ] **Besu**
    - [WIP implementation](https://github.com/hyperledger/besu/labels/EIP-1559)
- [ ] **Nethermind** 
    - [WIP implementation](https://github.com/NethermindEth/nethermind/pull/2341)
- [ ] **Open Ethereum** 
    - ⭐️ [Hiring an implementer](https://boards.greenhouse.io/gnosis/jobs/4978262002?t=addc4e802) ⭐️
- [ ] **TurboGeth**
    - N/A 

### Client-level Open Issues

- [ ] DoS risk on the Ethereum mainnet
    - Discussed in the [AllCoreDevs call #77](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2077.md#eip-1559) and [#97](https://github.com/ethereum/pm/pull/214/files?short_path=4d89329#diff-4d893291250cf226c77e67ad708be6f2) EIP-1559's elastic block size effectively doubles the potential effect of a DoS attack on mainnet. Solutions to this are outside the scope of this EIP and include things like [snapshot sync](https://blog.ethereum.org/2020/07/17/ask-about-geth-snapshot-acceleration/) and [EIP-2929](https://eips.ethereum.org/EIPS/eip-2929). 
    - [Write up](https://notes.ethereum.org/@vbuterin/eip_1559_spikes) by Vitalik about why this is perhaps solved once EIP-2929 is live. 
- [ ] (Nice to have) Base Fee Update Rule optimizations 
    - As per Tim Roughgarden's [analysis of 1559](http://timroughgarden.org/papers/eip1559.pdf) (Section 1.2, bullet 9), the base fee update rule is somewhat arbitrary and would gain from a more formal evaluation by an expert with a background in control theory. 
- [X] Transaction Pool Management
    - Good approaches to transaction pool management have been put forward. [First write up](https://hackmd.io/@adietrichs/1559-transaction-sorting), [Second write up](https://hackmd.io/@adietrichs/1559-transaction-sorting-part2). 
- [X] (Nice to have) Base Fee Opcode - [EIP-3198](https://github.com/ethereum/EIPs/pull/3198)
    - It would be nice to have a new opcode that would return a block's `BASE FEE` when EIP-1559 is deployed on mainnet. 
- [x] Transaction Encoding/Decoding
    - EIP-1559 transactions will be encoded using [EIP-2718](https://eips.ethereum.org/EIPS/eip-2718), by adding 1559-style transactions as a new type of transaction. 
- [X] Legacy transaction management in transaction pool 
    - Solved by a [recent change to the EIP](https://github.com/ethereum/EIPs/pull/2924) which removes the need for two transaction pools by interpreting legacy transactions as 1559-styles transactions where the `feecap` is set to the `gas price` and the `tip` is set to `feecap - base fee`. 
- [X] Transition Period 
    - Solved by a [recent change to the EIP](https://github.com/ethereum/EIPs/pull/2924) which removes the need for a transition period by interpreting legacy transactions as 1559-styles transactions. This means legacy transactions will be supported until an explicit change to the protocol is made to deprecate them. 

### Testing 

#### EIPs & Reference Tests 

- [ ] Reference / Consensus Tests 
  - While the EIP isn't ready for a full suite of reference tests yet, some parts of it are well defined enough to begin testing (e.g. the base fee calculation
)
- [ ] EIPs that return block or transaction data need to be updated to support EIP-1559 style transactions, specifically: 
    - [ ] `eth_getTransactionByBlockNumberAndIndex`
    - [ ] `eth_getTransactionByBlockHashAndIndex`
    - [ ] `eth_getTransactionByHash`
    - [ ] `eth_getTransactionReceipt`
    - [ ] `eth_getUncleByBlockNumberAndIndex`
    - [x] `eth_getBlockByHash` ([EIP-3041](https://eips.ethereum.org/EIPS/eip-3041))
    - [x] `eth_getBlockByNumber` ([EIP-3044](https://eips.ethereum.org/EIPS/eip-3044))
    - [x] `eth_getUncleByBlockHashAndIndex` ([EIP-3045](https://eips.ethereum.org/EIPS/eip-3045))
    - [x] `eth_getUncleByBlockNumberAndIndex` ([EIP-3046](https://eips.ethereum.org/EIPS/eip-3046))

#### Community testing

- [ ] JSON-RPC or equivalent commands that applications and tooling can use to interact with EIP-1559 
    - [x] [EIP-1559 Toolbox](http://eip1559-tx.ops.pegasys.tech/)
- [ ] Public testnet that applications and tooling can use to test EIP-1559. 

### Testnets 

- [x] Tooling to generate usage spikes on testnets;
    - [WIP by the Besu team](https://github.com/PegaSysEng/eip1559-tx-sender/) 
- [x] Multi-client PoA testnet to ensure spec can be implemented;
    - WIP between Geth, Besu & Nethermind teams. 
- [X] Single-client PoW testnet to ensure the spec works with PoW
    - Done by Besu team.
- [ ] Multi-client PoW testnet to ensure all code paths are tested; 
- [ ] Large state testnet to analyze performance with ~100M accounts on chain. 

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

- [X] [Stationary Users](https://nbviewer.jupyter.org/github/barnabemonnot/abm1559/blob/master/notebooks/stationary1559.ipynb)
- [X] [Strategic Users](https://nbviewer.jupyter.org/github/barnabemonnot/abm1559/blob/master/notebooks/strategicUser.ipynb) 
- [X] ["Floating escalator" simulation](https://github.com/barnabemonnot/abm1559/blob/master/notebooks/floatingEscalator.ipynb) to model using the [escalator fees](https://eips.ethereum.org/EIPS/eip-2593) approach to the EIP-1559 tip parameter
- [X] [Legacy transaction simulations](https://github.com/NethermindEth/research/blob/main/legacyTransactions.ipynb)

## Community Outreach

- [ ] Outreach to miners to better understand their objections to 1559, and stance if it is to be deployed on mainnet. 
- [X] Community outreach to projects to gather feedback on EIP-1559 
    - [Initial report published by the Ethereum Cat Herders](https://medium.com/ethereum-cat-herders/eip-1559-community-outreach-report-aa18be0666b5). Feedback still can be shared [here](https://forms.gle/bsdgBtG8g7KYnQL48). More wallet and exchange feedback is still needed. An update to the report may be published once more feedback has been gathered.  
