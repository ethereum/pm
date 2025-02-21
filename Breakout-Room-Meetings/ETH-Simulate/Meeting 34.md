## Eth_Simulate Meeting Meeting 34

Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1241#issuecomment-2590226750)

### Meeting Info

- Agenda: [ethereum#1241](https://github.com/ethereum/pm/issues/1241#issue-2772946504)
- Date & Time: January 13, 2025, 12:00 UTC
- Recording: [here](https://youtu.be/HKjT5O74lx4?si=j6qTuDzHlZxxVA9x)
## Notes
### Summary 
## Agreed Action Items and Implementation Decisions  

## Tracing Enhancements  
- Add new tracing methods and derive specifications from implementations.  
- Specify the outer trace object structure while treating block traces as a black box.  
- Align `eth_simulate` implementation across all clients.  

## Transaction and Block Tracing Strategies  
- Explore adding a `trace_simulate` method for debugging transactions.  
- Propose tracing both transactions and blocks, capturing state roots between transactions.  
- Support client-specific tracing methods.  
- Consider creating separate namespaces for Geth and Parity traces to improve organization.  
- Potentially add client-specific namespaces for enhanced tracing methods.  

## `eth_simulate` Parameter Extensions  
- Propose adding an optional RLP return parameter to `eth_simulate` for v2 documentation.  
- Suggest including a hidden parameter to return RLP data alongside the standard JSON response.  

## Test Suite and Reliability Challenges  
- Investigate issues with duplicate blocks caused by total difficulty pegged to zero.  
- Reduced failing test cases from **83** to **72**; duplicate block issues remain a significant challenge.  
- Regular updates to the Hive test suite; participants are encouraged to report any discrepancies.  
- Observed non-deterministic test failures likely linked to race conditions or shared state issues.  

## Debugging Consensus Differences  

### Methods to Obtain RLPs  
- Use `debug_getBadBlocks`: Temporary RLP dumps saved to disk.  
- Automatic dumps for RLP receipts and traces in cases of potential consensus issues.  
- Access traces via archive nodes.  

### RLP Sharing  
Exchange block and transaction RLPs between clients to identify discrepancies during consensus differences. Current practices include:  
- Retrieving temporary or on-disk RLP dumps with `debug_getBadBlocks`.  
- Auto-dumping receipts and traces for potential issues.  
- Accessing traces from archive nodes.  

## Challenges with `eth_simulate`  
- RLPs and traces aren't easily retrieved for `eth_simulate` calls since they are transient.  

### Suggestions:  
- Add a hidden parameter to `eth_simulate` to return RLPs.  
- Introduce a new method like `eth_simulateTrace` for detailed analysis.  

## Tracing Approaches  
- Clients like Geth and Parity offer tracing configurations that could include debug and parity namespaces.  
- Heavier options may suit debugging since they are not gas-accounted and require more memory.  

## Hive Tests and Non-Deterministic Failures  

### Potential Issues  
- Race conditions or shared states during parallel test runs.  
- Non-deterministic failures, especially with `eth_simulate` calls.  

### Challenges  
- Debugging Hive tests is complicated due to the transient nature of simulation calls and limitations in output retrieval.  

### Proposed Solutions:  
- Add hidden or optional parameters to `eth_simulate` to return RLPs directly.  
- Enhance RPC output or adapt Hive tests for direct access.  
- Modify client configurations to enable auto-dumping traces during specific test executions.  

## Cross-Client Consistency  
- While most clients (Erigon, Besu, etc.) support parity-like traces, Geth does not, leading to inconsistencies in tooling and debugging workflows.  
- Ensuring parity in debugging outputs across clients can streamline comparisons and troubleshooting.  

## Implementation Recommendations  

### For Debugging Enhancements  
- Add a separate, heavy trace method in the `debug` namespace, distinct from `eth_simulate`, to avoid production interference.  
- Ensure compatibility with existing client tracing standards for tools like block explorers.  

### For Persistent Debugging Output  
- Allow configuration for logging RLPs or traces to permanent locations instead of temp files for easier retrieval and analysis.  

### Short-Term  
- Add parameters to `eth_simulate` to optionally return RLP or trace data.  
- Implement temporary programmatic tracing to capture simulation-specific traces.  

### Long-Term  
- Develop a uniform method for tracing and debugging, potentially adopting shared standards across clients.  
- Address shared state or race condition issues in tests and simulations to improve consistency and reliability.  

## Communication  
- Share findings and insights with team members like Rohit and Sina to foster collaborative debugging.  
- Document procedures for enabling and utilizing new debugging features to facilitate broader adoption.  
