# Eth_Simulate Meeting Meeting 43
Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1388)

### Meeting Info

- Agenda: [ethereum#1388](https://github.com/ethereum/pm/issues/1388#issue-2925145935)
- Date & Time: March 24, 2025, 12:00 UTC
- Recording: [here](https://youtu.be/1I5962Rnp0g)
## Notes
## Eth_Simulate Implementers Call Summary  

## 1. Status of Tracing and Simulation
- The newly merged tracing functionality is not yet released.
- Participants need to align on its specifications and possibly draft an execution spec.

## 2. Beacon Root & Withdrawals in Block Overrides
- A participant plans to merge a PR today to add beacon root and withdrawals fields to block overrides.
- Other clients are encouraged to review and adopt similar changes.
- A previous temperature check raised no objections.

## 3. Handling Withdrawals in EVM
- Withdrawals can be passed into the EVM, which processes them as part of block execution.
- The execution layer (EL) directly deposits ETH into accounts based on the consensus layer’s (CL) request.
- ETH transfers from withdrawals generate no transaction logs, making tracking difficult.
- The lack of a dedicated logging structure for block-level ETH transfers was acknowledged as a long-standing issue in Ethereum.
- Options considered:
  - **Introducing a phantom transaction** (viewed as hacky).
  - **Creating a new field to log ETH transfers** (preferred approach).

## 4. Specification and Compatibility Considerations
- The proposal to add beacon root and withdrawals fields to block overrides is considered a **backward-compatible change**, making it suitable for **V1 rather than V2**.
- The block header must also be updated accordingly.
- Participants discussed whether additional overrides are needed to support replaying old blocks.
- **Nethermind and Besu’s stance** on the changes is unclear; a follow-up is required.

## 5. Writing a Specification for the Change
- There is **no formal execution spec** yet for these changes.
- A **basic spec should be written**, particularly for naming fields and defining their purpose.
- A participant offered to share their current implementation, which is not yet merged.

## 6. Request for a New `createAccessList` Method
- A proposal was introduced to add a **batch version of `createAccessList`**, similar to `estimateGas`, for **V2**.
- This would allow multiple transactions to be analyzed in a single request.
- Concerns were raised about inefficiency since access lists depend on gas usage, which could lead to redundant transaction executions.
- The general consensus was that **access lists should be included in V2** to avoid modifying the current spec further.

## 7. Decision on Withdrawals in Spec Versions
- **Withdrawals should remain in V1**, as it is a minor backward-compatible change.
- Other new feature requests should be **pushed to V2** to prevent continuous modifications to V1.

## Next Steps
- Write a **basic execution spec** for the beacon root and withdrawals update.
- Gather **feedback from Besu and Nethermind** teams.
- **Finalize V1 changes and freeze the spec** to move new features to V2.
- Continue discussions on **how to improve logging for ETH transfers**.
