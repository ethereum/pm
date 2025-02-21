## Eth_Simulate Meeting Meeting 38

Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1293#issuecomment-2664759485)

### Meeting Info

- Agenda: [ethereum#1293](https://github.com/ethereum/pm/issues/1293)
- Date & Time: February 17, 2025, 12:00 UTC
- Recording: [here](https://www.youtube.com/watch?v=Yer5Rue4M5s)
## Notes
## Eth_Simulate Implementers Call Summary  

## Main Outcome  
The primary focus of the meeting was to debug and resolve issues with the Hive test pipeline, specifically addressing why one test was failing in the test suite despite working on the mainnet. Additionally, the team discussed the development and testing of new API endpoints for simulation and tracing, as well as potential improvements to the `eth_simulate` and `eth_trace` methods.

## Key Discussion Points

### Hive Test Pipeline Debugging
- **Issue Identification**: One test was failing in the test suite but worked on the mainnet. The issue might be related to changes in the test chain, where 10 additional blocks were added, potentially breaking some tests.
- **Test Chain Consistency**: The test in question does not depend on the underlying chain, but the changes to the test chain (used universally across all tests) may have caused the failure. The team emphasized the importance of maintaining consistency in the test chain to avoid such issues in the future. If new blocks are added, the corresponding tests should be updated accordingly.

### Development of Simulation and Tracing Endpoints
- **New Endpoints**: Deeptanshu, an intern, has been working on two new endpoints: `debug_simulate` and `trace_simulate`, which perform simulations using Geth-like and Parity-like block tracers.
- **Testing and Refactoring**: The endpoints are not yet deployed to the mainnet but are being tested internally. Deeptanshu is addressing PR comments and refactoring the code, aiming to merge the changes within the week.
- **Standardization**: The team emphasized the need for standardization across clients for these endpoints. Killary suggested documenting the API schema and sharing it with the team for coordination.

### API Design and Standardization
- **Consistency Across Clients**: The team discussed the importance of ensuring that the new APIs (`debug_simulate` and `trace_simulate`) are consistent across different Ethereum clients.
- **Documentation**: Deeptanshu agreed to document the sample payloads and endpoints and share them on Telegram for feedback and testing.
- **Additional Fields**: The team debated whether to include additional fields like withdrawals in the simulation results but decided to maintain compatibility with the existing RPC interface for blocks.

### Gas Estimation in `eth_simulate`
- **Integration Options**: The team explored whether gas estimation should be integrated into `eth_simulate` as a parameter or as a separate method (`eth_simulate_estimate`).
- **Operational Cost**: Concern was raised about the operational cost of running gas estimation multiple times, as it could significantly increase the computational load on nodes.
- **Implementation Options**:
  - Adding a parameter to `eth_simulate` to enable gas estimation.
  - Creating a separate method for gas estimation.
  - Using a global flag to estimate gas for all transactions in a block.
- **Decision**: No final decision was made, but the team leaned towards adding a parameter to `eth_simulate` for simplicity, with the option to revisit the design before finalizing the implementation.

### Trace API Enhancements
- **Block-Level Information**: The team discussed whether the `eth_trace` API should return block-level information (e.g., block hash, gas used) in addition to transaction traces.
- **State Root Inclusion**: There was a suggestion to include the state root between transactions for debugging purposes, but concerns were raised about the additional complexity and performance impact.
- **Decision**: The team agreed that including block information in the trace results would be useful, as it aligns with the data structure returned by `eth_simulate` and provides more context for debugging.

### Withdrawals and System Calls in `eth_simulate`
- **Processing Withdrawals**: The team addressed an issue related to processing withdrawals and new system calls (introduced in the Prague hard fork) during block simulation.
- **Inclusion in Block Hash**: It was noted that withdrawals need to be processed after running a block, and their inclusion in the block hash could affect simulation results.
- **Next Steps**: The team decided to raise this issue in the RPC channel on the ETH R&D Discord for further discussion.

## Future Work and Next Steps
- **Deeptanshu**:
  - Refine the `debug_simulate` and `trace_simulate` endpoints.
  - Share documentation with the team.
  - Prepare a demo of the trace API for the next meeting.
- **Team**:
  - Test the new endpoints and provide feedback on the API design.
  - Decide on the implementation approach for gas estimation in `eth_simulate`.
  - Discuss and finalize the inclusion of block information in the `eth_trace` API.
- **Rohit**: Raise the issue of withdrawals and system calls in `eth_simulate` on the ETH R&D Discord.
- **Tony**: Gather feedback from Infura on the operational impact of integrating gas estimation into `eth_simulate`.

## Action Items
### Gas Estimation Options for `eth_simulate`
- **Options**:
  - `gasLimit: string | number`
  - `gasLimit: number, estimate: true; error if both provided`
  - `gasLimit: number, estimate: true; start estimating with gasLimit`
  - `gasLimit: number, estimate: true; max gas estimated is gasLimit`
  - `gasLimit: number; global flag estimates all missing transactions`

### Deeptanshu
- Refactor and merge the PR for `debug_simulate` and `trace_simulate` endpoints.
- Document the API schema and share it with the team on Telegram.
- Prepare a demo of the trace API for the next meeting.

### Team
- Test the new endpoints and provide feedback on the API design.
- Decide on the implementation approach for gas estimation in `eth_simulate`.
- Discuss and finalize the inclusion of block information in the `eth_trace` API.

### Rohit
- Raise the issue of withdrawals and system calls in `eth_simulate` on the ETH R&D Discord.

### Tony
- Gather feedback from Infura on the operational impact of integrating gas estimation into `eth_simulate`.

## Conclusion
The meeting highlighted the team's progress in debugging the Hive test pipeline and developing new simulation and tracing endpoints. While several design decisions remain unresolved, the team is committed to ensuring consistency and efficiency across Ethereum clients. The next steps involve refining the APIs, addressing technical challenges, and coordinating with other client teams to finalize the implementation.