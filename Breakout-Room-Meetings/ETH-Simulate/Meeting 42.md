# Eth_Simulate Meeting Meeting 42
Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1387)

### Meeting Info

- Agenda: [ethereum#1387](https://github.com/ethereum/pm/issues/1387#issue-2925132165)
- Date & Time: March 17, 2025, 12:00 UTC
- Recording: [here](https://youtu.be/Lcd7_CDKV7w)
## Notes
## Eth_Simulate Implementers Call Summary  

## 1.1 Killari  
Killari did not provide any updates as they were on holiday the previous week.  

## 1.2 Sina  
Sina also had no updates to share during this meeting.  

## 1.3 Rohit  
Rohit provided several updates on his recent work:  

### Endpoint Implementations  
- He successfully implemented two pressing endpoints: one in the **Parity style** and the other in the **Geth style**.  
- These implementations are part of ongoing efforts to ensure compatibility and functionality across different Ethereum clients.  

### Hash Mismatch Issue  
- Rohit identified a potential issue related to request hashes.  
- Nethermind does not incorporate request hashes in its responses, whereas Geth does, which could lead to mismatches.  
- **Next Steps:**  
  - Rohit plans to investigate this further and will share detailed findings with the team for review.  
  - He emphasized the importance of aligning Nethermind’s behavior with Geth to avoid inconsistencies.  

---

## 2. Debug and Tracing Endpoints Discussion  

### 2.1 Debug and Tracing Endpoint Specifications  
The team discussed the specifications for debug and tracing endpoints, focusing on input and output formats.  

#### Input and Output Details  
- Rohit shared the input and output specifications for the debug and tracing endpoints.  
- The PR for this implementation is not yet merged, but the team reviewed the details to ensure alignment with expectations.  
- **Outputs include:**  
  - Structured logs  
  - Call objects (providing detailed information about transaction execution)  

### Review and Approval  
- The PR is currently under review and is expected to be approved soon.  
- **Next Steps:**  
  - **Sina** was asked to review the implementation to ensure it aligns with expected standards and practices.  
  - The team emphasized the importance of **Sina’s approval** before merging the PR due to his expertise in tracing implementations.  

### 2.2 Parity Tracing Compatibility  
The team also discussed the compatibility of **Parity tracing** with other Ethereum clients.  

#### Support in Other Nodes  
- **Geth does not support Parity tracing**, but other clients like **Reth** might have some level of compatibility.  
- **Next Steps:**  
  - The team plans to seek feedback from other client developers, such as **Gabriel**, to ensure the implementation aligns with broader standards.  

---

## 3. Debug Tracing Implementation Details  

### 3.1 Struct Logs and Call Objects  
The team discussed **struct logs** and **call objects**, key components of the debug tracing implementation.  

### Struct Logs Added to Call Objects  
Struct logs provide detailed transaction execution information, including:  
- **Program Counter (PC):** Indicates the current instruction being executed.  
- **Opcode:** The operation being performed.  
- **Gas:** The amount of gas used and remaining.  
- **Gas Call Steps:** Details about gas consumption during execution.  

### Comparison with Debug Trace  
- The format of struct logs appears consistent with **debug trace outputs**, ensuring compatibility with existing tools and practices.  

### 3.2 Pre-State Tracing  
The team discussed **pre-state tracing**, which provides insights into blockchain state before a transaction executes.  

#### Functionality  
- Pre-state tracing reveals which parts of the state are required for execution and their values before execution.  

#### Inclusion in Response  
- The team agreed to **include pre-state trace results** in the same response structure as other traces.  
- This approach reduces the need for multiple API calls and improves usability.  

### 3.3 Tracer Configuration and Parameters  
The team reviewed **configuration options** for debug tracing.  

#### Optional Parameters  
- Like Geth, the implementation allows users to specify **optional configuration objects**, such as selecting a specific tracer.  

#### Input Consistency  
- The input format for debug tracing remains consistent with standard tracing methods, ensuring **ease of use** and **compatibility**.  

---

# 4. Challenges and Considerations  

### 4.1 Payload Limits  
Debug tracing can generate **large outputs**, which may exceed payload limits.  

### Risk of Hitting Limits  
- Tracing multiple transactions within a block can result in **very large responses**, potentially exceeding RPC provider limits.  

### Mitigation Strategies  
- **Local nodes** can adjust payload limits to accommodate larger responses.  
- **Public endpoints** may need to disable or restrict debug tracing to prevent performance issues.  

### 4.2 Standardization of Tracing Formats  
The team discussed the challenges of **standardizing tracing formats** across Ethereum clients.  

### Current Inconsistencies  
- Differences in how **Geth** and **Nethermind** handle tracing outputs (e.g., request hashes) can lead to **compatibility issues**.  

### Future Efforts  
- Ongoing Efforts aim to standardize tracing formats, particularly for **EOF (Ethereum Object Format) execution**.  
- These efforts seek to create a **unified approach** to tracing across clients.  

---

## 5. Next Steps  

- **PR Review and Approval:** Sina will review the PR for the debug tracing implementation and provide feedback.  
- **Hash Mismatch Investigation:** Rohit will continue investigating the hash mismatch issue and share findings with the team.  
  
- **Feedback from Other Clients:** The team will seek feedback from other Ethereum client developers (e.g., Gabriel) to ensure compatibility.  
- **Implementation of Gas Estimation Features:**  
  - The team plans to prioritize **gas estimation features** for **Eth_Simulate V2**, as it is a high-priority task.  
