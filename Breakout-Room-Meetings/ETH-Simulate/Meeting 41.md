# Eth_Simulate Meeting Meeting 41
Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1352)

### Meeting Info

- Agenda: [ethereum#1352](https://github.com/ethereum/pm/issues/1352#issue-2898141594)
- Date & Time: March 10, 2025, 12:00 UTC
- Recording: [here](https://youtu.be/aTvdYmrZwi0)
## Notes
## Eth_Simulate Implementers Call Summary  

## Estimate Gas Alternatives Document Update  

- A document detailing estimated gas alternatives has been prepared and shared with two teams.  
- Currently awaiting feedback from these teams; no significant updates to report at this time.  

## Issue Raised: Beacon Route and Withdrawals Override  

**Issue Overview:**  
- A request was raised on a repository to enable overriding the beacon block root and withdrawals for a given block.  

**Purpose:**  
- The enhancement aims to improve the functionality of `eth_simulate`, allowing it to simulate the chain more comprehensively.  
- This would enable users to test execution and consensus clients more effectively, essentially supporting a full fork of mainnet in memory.  

**Current Status:**  
- The feature is close to being fully functional, requiring only the addition of these two parameters.  

## Discussion on Implementation  

- **Consensus:** The team agreed that adding these parameters would be a non-breaking change and could be incorporated into version 1 (v1) of the software, as it is purely additive.  
- **Client Alignment:** To ensure consistency, buy-in from all relevant clients is required. The identified clients are **Reth** and **Besu**.  

**Next Steps:**  
- Confirm awareness and agreement from **Reth** and **Besu** regarding the proposed changes.  
- Ensure that both clients are comfortable with implementing the new parameters.  
- Avoid scenarios where some clients support the feature while others do not, which could lead to inconsistencies in RPC method usage.  

## Besu Testing Concerns  

**Current Status:**  
- The **Besu** team has not yet responded regarding the implementation of the proposed changes.  

**Previous Issue:**  
- Tests were failing due to a **parent hash issue in Geth**, which has since been resolved.  

**Action Items:**  
- Follow up with **Gabriel (from Besu)** via Telegram to confirm their current status and willingness to proceed with the changes.  
- Verify if the fixed parent hash issue has allowed Besu to pass the previously failing tests.  

## NetherMind Testing Update  

**Reported Issues:**  
- **Rohit** highlighted ongoing challenges with address endpoints, particularly a persistent **parent hash mismatch issue**.  

**Recent Fixes:**  
- Although the parent hash issue in Geth has been resolved and tests regenerated, the problem persists, suggesting a potential **secondary bug** in the same area.  
  

**Recommendation:**  
- Engage a **third client (e.g., Reth)** in the testing process to provide additional validation and help pinpoint issues more effectively.  
- Ensure that at least two out of three clients are aligned to facilitate better debugging and issue resolution.  

## Next Steps and Action Items  

### **Beacon Route and Withdrawals Override:**  
- Confirm buy-in from **Reth** and **Besu** for the proposed changes.  
- Ensure all clients are aligned to avoid inconsistencies in implementation.  

### **Besu Testing Follow-Up:**  
- Contact **Gabriel (Besu)** to confirm their status and willingness to proceed.  
- Verify if the fixed parent hash issue has resolved their test failures.  

### **NetherMind Testing:**  
- Continue monitoring and debugging the **parent hash mismatch issue**.  
- Encourage a **third client (e.g., Reth)** to participate in testing to improve reliability and issue diagnosis.  
