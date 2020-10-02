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
    - Discussed in the [AllCoreDevs call #77](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2077.md#eip-1559), EIP-1559's elastic block size effectively doubles the potential effect of a DoS attack on mainnet. 
- [ ] Transaction pool management 
    - It is unclear how to best manage both legacy and 1559-style transactions in the client transaction pools. Transaction pools are not under consensus so their behavior is typically not specified in an EIP, but it still needs to be implemented. A [recent PR to the EIP](https://github.com/ethereum/EIPs/pull/2924) aims to simplify this by converting legacy transactions to 1559-style ones. 
- [ ] Transaction Encoding/Decoding
    - How 1559-style transactions are encoded and decoded is still an open question. [EIP-2718](https://eips.ethereum.org/EIPS/eip-2718) would help here by providing a simple interface to add 1559-style transactions as a new type of transaction. 
- [ ] Transition Period 
    - Whether to have a transition period and for how long is still an open question. The current spec specifies a transition period of 800 000 blocks (4-5 months), where upon the fork block 1559-style transactions would get 50% of the blockspace and the amount of space for legacy transactions would drop to 0 over that period. The transition period could be removed if there was a way to convert legacy-transactions to 1559-style transactions that worked for all cases.

### Testing 

#### EIP Tests 

- [ ] Reference / Consensus Tests 

#### Community testing

- [ ] JSON-RPC or equivalent commands that applications and tooling can use to interact with EIP-1559 
- [ ] Public testnet that applications and tooling can use to test EIP-1559

### Testnets 

- [x] Tooling to generate usage spikes on testnets;
    - [WIP by the Besu team](https://github.com/PegaSysEng/eip1559-tx-sender/) 
- [x] Multi-client PoA testnet to ensure spec can be implemented;
    - WIP between Geth, Besu & Nethermind teams 
- [ ] Multi-client PoW testnet to ensure all code paths are tested; 

### Other Testing

- [x] Nethermind is using EIP-1559 as part of a client's network
- [x] [Filecoin](https://filecoin.io/blog/roadmap-update-august-2020/) and [Celo](https://docs.celo.org/celo-codebase/protocol/transactions/gas-pricing) have implementations of EIP-1559 in their networks 

## R&D 

### Theoretical Analysis 

- [ ] Analysis of whether EIP-1559 is game-theoretically sound, and potential improvements
    - [WIP by Tim Roughgarden](https://d24n.org/tim-roughgarden-will-work-on-eip-1559/)
- [ ] Comparison of EIP-1559 with alternatives (e.g. [Escalator Fees](https://eips.ethereum.org/EIPS/eip-2593))
    - [WIP by Tim Roughgarden](https://d24n.org/tim-roughgarden-will-work-on-eip-1559/)
    - [Analysis by Deribit](https://insights.deribit.com/market-research/analysis-of-eip-2593-escalator/)

### Simulations

- [ ] TBA 

## Community Outreach

- [ ] Community outreach to projects to gather feedback on EIP-1559 
    - WIP by the Ethereum Cat Herders. Feedback can be shared [here](https://forms.gle/bsdgBtG8g7KYnQL48). A report on the results will be shared once enough projects have been contacted. 
