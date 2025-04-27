# Eth_Simulate Meeting Meeting 45
Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1436)

### Meeting Info

- Agenda: [ethereum#1436](https://github.com/ethereum/pm/issues/1436#issue-2976941492)
- Date & Time: April 07, 2025, 12:00 UTC
- Recording: [here](https://www.youtube.com/watch?v=ruOlBWpCxig)
## Notes
## Eth_Simulate Implementers Call Summary  

## Progress Updates

Kilari opened the discussion by stating they had no progress updates to share. Sina similarly mentioned that they had nothing new to report from their side and suggested that Rohit might have updates.

## 2. Rohit’s Technical Updates

Rohit provided a detailed breakdown of his recent work, focusing on two key issues: hash mismatches and gas limit behavior.

### Hash Mismatch Resolution

Rohit explained that he had identified and fixed an issue where an extra byte was causing hash mismatches in transactions. After applying the fix, the hashes now matched correctly. However, this led to a secondary issue with gas limit discrepancies.

### Gas Limit Behavior Discussion

- **Current Implementation in Nethermind**:  
  The team had previously agreed on a static allocation approach, where the remaining block gas is divided equally among all transactions at the start. This method allows for pre-computation of transaction details, simplifying certain aspects of transaction processing.

- **Geth’s Dynamic Approach**:  
  In contrast, Geth processes transactions sequentially, assigning each transaction the maximum available gas from the remaining block gas after previous transactions have been executed. This dynamic allocation provides more flexibility but requires runtime adjustments.

- **Discrepancy Identified**:  
  Rohit noted that while Nethermind’s static method aligns with the current spec, Geth’s dynamic behavior is more flexible, particularly in scenarios where gas usage is unpredictable.

- **Team Consensus**:  
  After deliberation, the team acknowledged that both methods have merits. However, given the need for dynamic nonce handling (discussed next), they leaned toward adopting Geth’s dynamic gas allocation for consistency and improved user experience.

## 3. Nonce Handling Challenges

A significant portion of the discussion revolved around nonce handling, particularly in edge cases involving contract creation and subsequent calls.

### Problem Identification

- **Default Nonce Behavior**:  
  Nethermind had hardcoded a default nonce of 1 for unspecified transactions, while Geth expects the first nonce to be 0. This mismatch caused failures in Nethermind’s test cases.

- **Contract Creation Edge Case**:  
  The team highlighted a critical scenario where a transaction deploys a contract, and a subsequent transaction calls that newly created contract. In such cases, the nonce must be dynamically adjusted, as the contract’s address and state are unknown until the first transaction is processed.

### Dynamic Nonce Resolution

- **Geth’s Approach**:  
  Geth dynamically assigns nonces during transaction processing, ensuring correctness even in complex scenarios like contract creation.

- **Nethermind’s Adjustment**:  
  The team agreed that Nethermind should adopt dynamic nonce handling to match Geth’s behavior. This change would require updates to ensure nonces are correctly assigned during runtime, particularly for transactions involving newly created contracts.

- **Test Case Development**:  
  Rohit emphasized the need for a dedicated test case to validate dynamic nonce handling, ensuring that transactions from newly created contracts are processed correctly.

## 4. Validation Mode and Spec Clarifications

The conversation shifted to broader questions about validation mode behavior and spec alignment.

### Validation Mode Rules

- **Required Fields**:  
  The team debated whether transactions in validation mode must include all fields (e.g., nonce, gas limit) or if clients should fill in defaults. While the spec suggests that validation mode should closely mirror mainnet behavior (where fields like nonce and gas limit are mandatory), practical implementations like Geth allow some flexibility.

- **Eth_sendTransaction Deprecation**:  
  The team agreed that `eth_sendTransaction` should be deprecated for simulation purposes, as it is more suited for wallet operations rather than client debugging.

### Spec Updates

- **Dynamic Gas and Nonce Handling**:  
  Given the consensus on dynamic allocation, the team proposed updating the spec to reflect this behavior, ensuring consistency across clients.

- **Edge Case Considerations**:  
  The discussion underscored the importance of addressing edge cases (e.g., contract creation mid-block) in the spec to prevent future discrepancies.

## 5. Debug Tracing and Tooling

Sina inquired about tools for converting debug trace outputs into more human-readable formats, specifically for tracking function calls.

### Available Tracers

- **Call Tracer and Four-Byte Tracer**:  
  Rohit recommended using Geth’s built-in tracers, which simplify debug outputs by focusing on high-level call structures rather than low-level opcodes. These tracers are particularly useful for analyzing transaction flows in complex scenarios.

- **Nethermind’s Status**:  
  Sina noted that Nethermind’s implementation of these tracers is pending release, limiting immediate testing options.

## Action Items and Next Steps

### Rohit’s Tasks:

- Verify Geth’s nonce behavior (zero vs. one) and share detailed transaction examples.
- Implement dynamic gas allocation in Nethermind and test against edge cases.

### Team Tasks:

- Develop a test case for dynamic nonce validation, focusing on contract creation and subsequent calls.
- Finalize spec updates to reflect dynamic gas and nonce handling, ensuring cross-client compatibility.

Related Links: https://docs.chainstack.com/reference/ethereum-tracecall
