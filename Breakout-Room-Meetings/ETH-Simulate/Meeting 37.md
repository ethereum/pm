# Eth_Simulate Meeting Meeting 37

Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1278#issuecomment-2650875573)

### Meeting Info

- Agenda: [ethereum#1278](https://github.com/ethereum/pm/issues/1278)
- Date & Time: February 10, 2025, 12:00 UTC
- Recording: [here](https://youtu.be/YgU7S01PUZc)
## Notes
# Eth_Simulate Implementers Call Summary  

## Main Outcome  
The primary outcome of the meeting was the agreement to add support for type 4 transactions (EIP-7702) across various blockchain client methods. The team discussed and outlined a rough design for implementing this support, focusing on addressing the challenges related to transaction signature validation and authentication.  

## Key Decisions and Design Proposals  

### Type 4 Transaction Support  
- The team agreed to add support for type 4 transactions (EIP-7702) in methods like `eth_call`, `eth_simulate`, and `eth_estimateGas`.  
- A transaction can have either an **authority** field, **signature fields** (`r`, `s`, `yParity`), or both.  
- If it contains an **authority** field, its value must be an address.  
- If it contains both an **authority** field and **signature fields**, the address recovered from the signature must match the address in the authority field.  


### Flexible Authentication Mechanism  
- A new **Authority** field will be added to the transaction object to support flexible authentication methods.  
- The **Authority** field can contain:  
  - An **address** (for lightweight authentication).  
  - A **signature** (for cryptographic verification).  
  - A **mixed list of addresses and signatures** (for maximum flexibility).  

### Validation Rules  
- If both **Authority** and **signature** are provided, they must match; otherwise, an error will be thrown.  
- This ensures users can validate their transactions and catch potential issues early.  

### Cross-Client Consistency  
- The team emphasized the need for a **consistent API** across all blockchain clients to handle type 4 transactions uniformly.  
- All clients will need to implement the proposed **Authority** field and validation logic.  

### Testing and Simulation  
- Testing type 4 transactions will require simulating transactions with the new **Authority** field.  
- The team discussed using **EXTCODE operations** (e.g., EXTCODEHASH) to verify authority settings, as direct pulling of authority values from the chain is not possible.  

## Next Steps  

### Finalize Design  
- Confirm the design with all stakeholders, including **Besu** and other client implementers.  
- Ensure the proposed **Authority** field and validation rules are acceptable across all clients.  

### Implementation  
- Develop a PR against the execution-apis [repo]( https://github.com/ethereum/execution-apis) at the **Authority** field and type 4 transaction support.  
- Address any client-specific implementation challenges, particularly in **Geth** and other clients.  

### Testing  
- Conduct thorough testing to validate the new functionality, especially for `eth_simulate` and `eth_call`.  
- Use **EXTCODE operations** to verify authority settings and ensure correctness.  

### Coordination  
- Collaborate with all clients to ensure **consistent implementation** and approval of the changes.  

## Conclusion  
The meeting concluded with a clear direction to **add type 4 transaction support** and a rough design for implementing it. The proposed **Authority** field will provide a flexible and robust way to handle authentication for these transactions. The next steps involve finalizing the design, implementing the changes, and coordinating with all clients to ensure a **consistent and reliable solution**.  
