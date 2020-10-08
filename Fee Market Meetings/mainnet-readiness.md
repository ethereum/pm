# EIP-1559 Mainnet Readiness Checklist

This document is meant to capture various tasks that need to be completed before EIP-1559 is ready to be considered for mainnet deployement. This list is a work in progress and tries to aggregate known requirements. More things may be added in the future and checking every box is not a guarantee of mainnet deployement. 

Tasks that are normally part of the "AllCoreDevs process" are not listed. In other words, this list is what should ideally be done _before_ moving EIP-1559 through the regular network upgrade process. 

## Implementation

### Client Implementation Status 
- [ ] **Geth**
    - [WIP implementation led by Vulcanize](https://github.com/vulcanize/go-ethereum-EIP1559/tree/eip1559_rebase)
- [ ] **Besu**
    - [WIP implementation](https://github.com/hyperledger/besu/labels/EIP-1559)
- [ ] **Nethermind** :star2: [**Hiring an implementer**](https://justjoin.it/offers/nethermind-ethereum-engineer) :star2:
    - [WIP implementation](https://github.com/NethermindEth/nethermind/pull/2341)
- [ ] **Open Ethereum**
    - N/A
- [ ] **TurboGeth**
    - N/A 

### Client-level Open Issues

- [ ] DoS risk on the Ethereum mainnet
    - Discussed in the [AllCoreDevs call #77](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2077.md#eip-1559) and [#97](https://github.com/ethereum/pm/pull/214/files?short_path=4d89329#diff-4d893291250cf226c77e67ad708be6f2) EIP-1559's elastic block size effectively doubles the potential effect of a DoS attack on mainnet. Solutions to this are outside the scope of this EIP and include things like [snapshot sync](https://blog.ethereum.org/2020/07/17/ask-about-geth-snapshot-acceleration/) and [EIP-2929](https://eips.ethereum.org/EIPS/eip-2929). 
- [ ] Transaction Encoding/Decoding
    - How 1559-style transactions are encoded and decoded is still an open question. [EIP-2718](https://eips.ethereum.org/EIPS/eip-2718) would help here by providing a simple interface to add 1559-style transactions as a new type of transaction. 
- [X] Transaction pool management 
    - Solved by a [recent change to the EIP](https://github.com/ethereum/EIPs/pull/2924) which removes the need for two transaction pools by interpreting legacy transactions as 1559-styles transactions where the `feecap` is set to the `gas price` and the `tip` is set to `feecap - base fee`. 
- [X] Transition Period 
    - Solved by a [recent change to the EIP](https://github.com/ethereum/EIPs/pull/2924) which removes the need for a transition period by interpreting legacy transactions as 1559-styles transactions. This means legacy transactions will be supported until an explicit change to the protocol is made to deprecate them. 

### Testing 

#### EIP Tests 

- [ ] Reference / Consensus Tests 
  - While the EIP isn't ready for a full suite of reference tests yet, some parts of it are well defined enough to begin testing (e.g. the base fee calculation
)

#### Community testing

- [ ] JSON-RPC or equivalent commands that applications and tooling can use to interact with EIP-1559 
  - EIPs need to be done to update `eth_getTransactionByHash`, `eth_getBlockByHash`, `eth_getBlockByNumber` and `eth_sendTransaction` to support EIP-1559-style transactions. 
- [ ] Public testnet that applications and tooling can use to test EIP-1559. 

### Testnets 

- [x] Tooling to generate usage spikes on testnets;
    - [WIP by the Besu team](https://github.com/PegaSysEng/eip1559-tx-sender/) 
- [x] Multi-client PoA testnet to ensure spec can be implemented;
    - WIP between Geth, Besu & Nethermind teams. 
- [ ] Single-client PoW testnet to ensure the spec works with PoW
    - Besu team to start 🔜 
- [ ] Multi-client PoW testnet to ensure all code paths are tested; 

### Other Testing

- [x] Nethermind is using EIP-1559 as part of a client's network
- [x] [Filecoin](https://filecoin.io/blog/roadmap-update-august-2020/) and [Celo](https://docs.celo.org/celo-codebase/protocol/transactions/gas-pricing) have implementations of EIP-1559 in their networks 

## R&D 

### Theoretical Analysis 

- [ ] Analysis of whether EIP-1559 is game-theoretically sound, and potential improvements
    - [Blockchain Resource Pricing by Vitalik Buterin](https://github.com/ethereum/research/blob/master/papers/pricing/ethpricing.pdf) 
    - [WIP by Tim Roughgarden](https://d24n.org/tim-roughgarden-will-work-on-eip-1559/)
- [ ] Comparison of EIP-1559 with alternatives (e.g. [Escalator Fees](https://eips.ethereum.org/EIPS/eip-2593))
    - [WIP by Tim Roughgarden](https://d24n.org/tim-roughgarden-will-work-on-eip-1559/)
    - [Analysis by Deribit](https://insights.deribit.com/market-research/analysis-of-eip-2593-escalator/)

### Simulations

- [X] [Stationary Users](https://nbviewer.jupyter.org/github/barnabemonnot/abm1559/blob/master/notebooks/stationary1559.ipynb)
- [X] [Strategic Users](https://nbviewer.jupyter.org/github/barnabemonnot/abm1559/blob/master/notebooks/strategicUser.ipynb) 
- [ ] Legacy transaction simulations to model the transition period and the "tax" of interpreting legacy transactions as 1559-style transactions
- [ ] "Floating escalator" simulation to model using the [escalator fees](https://eips.ethereum.org/EIPS/eip-2593) approach to the EIP-1559 tip parameter
- [ ] "UX improvement" simulations to model what agents learn to do over time when submitting 1559-style transaction and what the impact is on them 
- [ ] "Wallet defaults" simulations to model what defaults wallet should propose and when to shift them

## Community Outreach

- [X] Community outreach to projects to gather feedback on EIP-1559 
    - [Initial report published by the Ethereum Cat Herders](https://medium.com/ethereum-cat-herders/eip-1559-community-outreach-report-aa18be0666b5). Feedback still can be shared [here](https://forms.gle/bsdgBtG8g7KYnQL48). More wallet and exchange feedback is still needed. An update to the report may be published once more feedback has been gathered.  
