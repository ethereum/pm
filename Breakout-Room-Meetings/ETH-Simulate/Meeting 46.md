# Eth_Simulate Meeting Meeting 446
Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1437)

### Meeting Info

- Agenda: [ethereum#1437](https://github.com/ethereum/pm/issues/1437#issue-2976941666)
- Date & Time: April 14, 2025, 12:00 UTC
- Recording: [here](https://youtu.be/NP4DJISEs1Q)
## Notes
## Eth_Simulate Implementers Call Summary  

### Rohit - Weekly Update

- **Gas Limit Logic for Transactions**
- **Dynamic Nonce Calculation**
  - Rohit confirmed that he has not yet started on the nonce calculation, but it is planned for this week.

---

### Discussion on Gas Estimation

The team briefly revisited the topic of gas estimation, which had not been discussed in detail recently.

#### Key Points:

- There is currently **no finalized strategy** for handling gas estimation.
- A suggested approach is to **mirror Geth’s method**, where transactions dynamically estimate gas instead of using predefined limits.
- It was acknowledged that even **Geth does not have a complete solution** for this yet.

#### Clarifications:

- **Gas estimation** (e.g., binary search to determine required gas) is distinct from **dynamic gas calculation**.
- Current simulation tools **do not support multiple queries** needed for accurate gas estimation, making it an open issue for further development.

---

### Next Steps

- Proceed with the **implementation of gas limit logic** and **dynamic nonce calculation** this week.
- Address **outstanding specifications** as soon as possible.
- Continue discussions and alignment on a strategy for **handling gas estimation** moving forward.
  