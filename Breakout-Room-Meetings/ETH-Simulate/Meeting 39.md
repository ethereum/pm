# Eth_Simulate Meeting Meeting 39
Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1302)

### Meeting Info

- Agenda: [ethereum#1293](https://github.com/ethereum/pm/issues/1302#issue-2859240773)
- Date & Time: February 24, 2025, 12:00 UTC
- Recording: [here](https://youtu.be/4hvX2CyQW8g)
## Notes
## Eth_Simulate Implementers Call Summary  

## Overview  
The meeting focused on resolving test case issues, progressing the tracing PR, and finalizing the approach for gas estimation. The team emphasized aligning implementations with user needs and gathering stakeholder feedback to ensure a robust and user-friendly solution.  

## Key Discussion Points  

### Test Case Updates  
- **Killari** reported that several test cases related to Geth and other areas have been fixed, and tests are now running successfully.  
- **Sina** confirmed that Geth has merged their PR (Pull Request) to fix parent block hashes, resolving some test case issues.  

### Tracing PR Progress  
- **Lukasz** mentioned the need to sync with **Deeptanshu** regarding the tracing PR but faced timing issues. The PR is in a good state but needs some polishing.  
- **Killari** was invited to review the tracing PR to understand its workings.  
- Noted discrepancies in how tracing is invoked compared to eth_simulate; a preferred approach would align its input and output structure to eth_simulate while incorporating tracing functionality.
- **Lukasz** shared the PR in Telegram for further review, and **Killari** suggested **Sina** should also evaluate it.  
- Nethermind and Geth tracing implementations were analyzed for alignment, with minor differences noted primarily in error messages rather than codes.

### Gas Estimation Discussion  
- The discussion revisited ongoing deliberations regarding gas estimation methodologies.
- Previous meetings had yielded tentative options, but a final decision had yet to be reached.
- Differing perspectives emerged regarding global gas flag usage, with concerns over potential overestimation in specific use cases, particularly in the Interceptor framework.
- The need for selective transaction estimation was emphasized, advocating for an approach that allows developers to specify which transactions require estimation while ensuring efficiency in gas calculations.
- A proposal was put forward to limit estimation within a predefined gas limit, with behavior ensuring that transactions would not exceed the user-defined cap.
- The proposed method involves executing a transaction with the set gas limit and, upon failure, ceasing further estimation; if successful, further refinements would be applied within the limit.
- A structured approach to decision-making was suggested, including drafting a proposal for broader community input, particularly from Nethermind and other relevant providers.
- Concerns were raised regarding potential developer confusion if gas limit adjustments yielded widely varying estimates, prompting further discussion on ensuring predictability and usability.  

### Implementation Preferences  
- **Killari** and **Sina** discussed different approaches:  
  - **Killari** preferred allowing users to specify which transactions to estimate.  
  - **Sina** leaned towards a simpler global flag.  
- The team debated whether the gas limit should be a **hard cap** or a **starting point** for estimation.  
- **Micah** raised concerns about inconsistencies between implementations (e.g., Geth vs. Nethermind), emphasizing the need for consistency and usability.  

## Next Steps  
The team agreed to finalize a proposal for gas estimation, focusing on two main options:  
1. **A per-transaction flag** to specify which transactions should be estimated.  
2. **A global flag** to enable or disable gas estimation across all transactions.  

**Kilari and Sina** will collaborate on drafting the proposal and share it with users, including **Infura and other providers**, for feedback.  
Additionally, the team plans to reach out to a developer who previously used `eth_simulate` in a library for insights.  

## Action Items  

### **Killari and Sina**  
- Finalize the gas estimation proposal and share it with stakeholders for feedback.  
- Review the tracing PR and provide feedback on its alignment with `eth_simulate`.  

### **Lukasz**  
- Sync with **Deeptanshu** to finalize the tracing PR.  
- Reach out to **Infura** and other providers to gather feedback on the gas estimation proposal.  

### **Team**  
- Continue testing and refining the fixed test cases.  
- Prepare for the next meeting to review stakeholder feedback and finalize the gas estimation approach.  