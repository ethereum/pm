# AA session - in-protocol full AA

**Summary:** Account Abstraction has been a long time Ethereum goal. We've built an off-protocol implementation (ERC-4337) which gained traction. This session is about the next step - an in-protocol implementation (EIP-7701) based on EOF.

**Facilitator:** Yoav Weiss

**Note Taker:** Nico Consigny

**Pre-Reads:**
- [EIP-7701](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-7701.md) and [Discussion thread](https://ethereum-magicians.org/t/eip-7701-native-account-abstraction-with-eof/19893)
- The AA [mempool](https://notes.ethereum.org/@yoav/unified-erc-4337-mempool) and rules ([ERC-7562](https://eips.ethereum.org/EIPS/eip-7562)). Not part of the EIP but a primary use case.

Optional:
- [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337).
- EOF ([EIP-3540](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-3540.md)) - this proposal uses and extends it.
- [RIP-7560](https://github.com/ethereum/RIPs/blob/master/RIPS/rip-7560.md) - non-EOF protocol AA for L2

Slides:** **[WiP]**

## Agenda 

#### Overview / background
* Account abstraction background
    * What does "full account abstraction" mean?
    * What are the minimum requirements?
    * What is ERC-4337 and why is it not enough?
* EIP-7701
    * Goals and non-goals.
    * Current design
    * Open questions

#### Points for open discussion / request for feedback
* EIP-7701 (EOF code sections) vs. using an ABI (similar to RIP-7560)
    * Pros:
        * Not introducing solidity ABI to the protocol
        * Clear separation of validation and executing at the protocol level. The validation function cannot be called in other contexts.
        * Mitigates attacks introduced by methodsig collisions.
        * User accounts easily identified as such.
    * Cons:
        * EOF dependency.
        * Requires compiler support.
        * Not compatible with previously deployed accounts.
* "Interim 7701" to support secp256r1 accounts (and other sig schemes)
    * 7701 but no paymaster and no state access during validation
    * Upgrade mechanism similar to EIP-7702 but using the account's validation
    * Should we enforce purity at deploy time, or just off-chain in the mempool?
* Prefered inputs / outputs method for validation
    * ABI encoded
    * Precompile
    * Opcode (similar to current transaction-field opcodes like CALLDATALOAD or GASPRICE, but parameterized to support new transaction types)
    * A combination of stack elements and calldata. Single-word values would be provided to the entry point directly on the stack, and variable-length values provided in calldata.

#### Goals
* Collect feedback on the points above
* Improve design
* Start converging on a path for future inclusion


## Notes & Action Items 

# Account Abstraction (AA) Session Notes

## Why Isn’t ERC-4337 Sufficient?

- **ERC-4337** is widely adopted for AA outside the Ethereum protocol, with over 20 million accounts deployed and 90 million operations performed, demonstrating significant market validation.
- **EIP-7701** aims to bring AA fully into the protocol in a way that is minimally opinionated.

**Non-Goals for EIP-7701**:
- It doesn’t enforce a specific form of AA, making it flexible for various AA protocols.
- It doesn’t impose decentralization requirements where decentralization may not be essential.

---

## How EIP-7701 Works

1. **New Transaction Type**: Introduces `AA_TX_TYPE` which uses multiple call frames.
2. **Entry Points in EOF (Ethereum Object Format)**: Adds an `entry_points` section to EOF contracts that maps `AA_TX_TYPE` call frames to specific code sections.

   - **Call Frames in AA_TX_TYPE**:
     1. **Deployment Frame**: Manages contract deployment.
     2. **Sender Validation Frame**: Validates the sender.
     3. **Paymaster Validation Frame** (optional): Verifies paymaster specifics if included.
     4. **Post-Transaction Frame** (optional): Allows for additional operations after transaction completion.

---

## Open Questions and Discussion Points

1. **Can we rely solely on the paymaster?**  
   - **Consensus**: No, relying only on the paymaster would limit flexibility and protocol inclusiveness.

2. **Should we use EOF?**
   - **Consensus**: Yes, pushing EOF forward aligns with use cases specific to account abstraction, like handling new transaction types efficiently.

3. **EOF Forwarding Proxy**  
   - **A researcher suggestion**: A proxy could forward calls to legacy accounts, which would simplify integrating AA with existing accounts.
   - **Y’s Response**: To enable this, we’d need to enshrine the proxy type in a similar manner to EIP-7702. The proxy would pass validation and could act as a bridge to legacy accounts.

4. **Singleton Forwarding Contracts**  
   - **The researcher Proposal**: Why not use a dummy account as a forwarding mechanism, creating a singleton forwarding contract for AA?
   - **Y’s Response**: Using a singleton could streamline compatibility with existing accounts, but we’d need a validation function to ensure security.

5. **Validation Section for Legacy Accounts**  
   - **A’s Insight**: A simpler approach would be to use the existing ERC-4337 ABI for validation without enshrining it in the protocol itself. By only enshrining the singleton in the mempool, we could maintain flexibility in protocol usage.

---

## Important Implementation Details for EIP-7701

- **ABI Encoded Calldata**: There was a generally favorable view toward using ABI-encoded calldata, although opinions weren’t unanimous.
  - **A geth client dev input Input**: ABI encoding aligns well with existing AA operations, though it’s not the only viable approach.

- **Precompiles and Opcodes**: Introduces new opcodes similar to transaction field opcodes (e.g., `calldataload`, `GASPRICE`) that are parameterized to support new transaction types.

- **SSZ Size Proposal**:
  - *Another researcher Proposal**: Use SSZ size (32 bytes) for data consistency across transaction types.
  
- **Collision Risks with Singleton Calls**:
  - **Concern**: Singleton calls to non-EOF accounts might risk collisions, especially with paymaster operations.
  - **Solution**: Precompiles can mitigate this risk by isolating specific operations for singleton calls.

---

## Layer 2 (L2) Considerations

- **Enshrined ABI Encoded Calldata**: This is covered in RIP-7560, establishing it as a standard for L2s.
- **Compatibility**: Implementing either EIP-7701 or RIP-7560 can simplify adoption of the other, making L2 adoption smoother for AA.

---

## Demand and Potential Adjustments

- **Demand for 256R1 Curve Support**: Rising demand for 256R1 prompts the AA team to consider a “lighter” version of EIP-7701 to meet these immediate needs.
- **Restricted 7701 Implementation**: 
  - Potential for a modified version of 7701 that restricts paymaster usage or limits the validation section.
- **Special Code Section Numbers**: Proposing special identifiers in code sections to differentiate these restricted AA accounts.

### Mempool Differences

- **Separate Mempools Needed**: Propagation rules differ between standard transactions and AA transactions, necessitating a distinct mempool using libp2p rather than devp2p.
- **Canonical Mempool Safety**:
  - **Felix’s Insight**: The canonical mempool should remain safe even if exotic mempools fail, as exotic mempools would operate with non-standard features outside protocol requirements.
  
---

## Complexity in Validation and Inclusion

- **Validation Overhead**: AA transactions require 2-3 EVM calls (deploy, validation, and paymaster frames), making them heavier than standard transactions.
- **Impact on Nodes**: Validation intensity could lead to potential denial-of-service (DoS) risks on nodes processing AA transactions, especially without optimized validation functions.

---

## Implementation Status

- **Current Client Support**: As ERC-4337 is an ERC, it has no direct client implementation, but multiple bundler implementations are available across different programming languages.

---

## Additional Topics and Feedback

1. **Profit Levels for Bundlers**: Issues of over/underpaying bundlers are mitigated in the dedicated mempool, resolving a key challenge faced with ERC-4337 in the main mempool.

2. **Encrypted Transactions**:
   - **Problem**: Validating encrypted transactions is challenging, as it requires visibility into the code for verification without full trust.
   
3. **Final Remarks from G**:
   - **Reflection**: Appreciates the discussion, noting that the full AA model isn’t yet possible with the Biconomy paymaster, as it still depends on meta-transactions.


