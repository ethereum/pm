# Inclusion List Breakout Room #3

Note: This file is copied from [here](https://hackmd.io/3sgYIucATMafLjj4l5S3JQ?view)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1000

**Date & Time**: April 5, 2024, 14:00-15:00 UTC

**Recording**: 

# Inclusion List Breakout Room 3 Notes
**Agenda**: https://github.com/ethereum/pm/issues/1000
**Goal**: Review the latest issue with IL regarding EIP3074

### Problem statement:

- IL in n specifies address `0xa`.
- Payload in `n` from a different address changes `0xa`'s balance.
- Payload in `n+1` lacks a tx from `0xa`, yet needs to confirm the summary condition is met for both validity and availability conditions.

### General problem can be broken down into two parts:

- Validity Issue
- Availability (Head Vote) Issue

### Discussed solutions to validity

- Commit balance changes (or general AA modifications) to the EL, as seen in EIP3074. Specifically, at slot n, commit all addresses that experienced balance changes. This commitment doesn't need to be in the state, that's just a simplification, since no proof is required, it can be managed out-of-band, provided it enables the client to invalidate the transaction if necessary.

  - Only committing balance changes in the summary is ineffective, as the honesty of the next slot proposer, responsible for including the correct summary, cannot be guaranteed.

### Discussed solutions to availability

- Ensure blocks are only imported into the fork choice if the IL is available.
- IL reconstruction based on EIP3074 or general AA rules. There is high complexity and difficulty of full IL recovery.
- Include the current slot summary (n) in the block body for n. Currently, slot summaries are not committed within block body. This brings back a long discussion about trustless selling of inclusion in the IL and secondary markets that opens.

---

We briefly discussed what free DA means, noting the variety of definitions. It was generally agreed that for DA to be considered "free," it must meet the following criteria:

- It is stored on-chain.
- Its availability can be proven and guaranteed.

We then discussed how ePBS addresses this issue. In ePBS, due to its inherent (block, slot) voting mechanism, concerns about network splitting—where one-half of the nodes have to request data from the other half—are mitigated. It enables a validator to import a block without necessarily voting for it. The current IL design does not offer this flexibility without integrating (block, slot) voting.

We then discussed how to move forward and what the plan for PoC is. It was suggested to treat the availability as a black box since we could either maintain the IL for recovery or simply not import the block. For the validity condition, the solution seems more straightforward for the PoC. (EL devs pushed this back towards the end of the call.)

Additionally, we noted that attacks on the fork choice can be quickly identified and attributed socially, and the community can respond swiftly to such attacks. The current goal is to address the validity condition and tackle the availability issue later.

We dedicated more time to discussing AA, emphasizing the need for a more generalized approach to address the validity condition in relation to AA. This would allow the EL to store various validation conditions, such as those involving Uniswap txs. The implication is that any change would need to be stored somewhere. The general workflow involves receiving a block at n+1 that references a summary for txs for address A, even if there's no tx from address A in the payload. This requires looking back at the state and various elements from the previous block. The STF processes the current state and the block, and if no previous tx and state indicate changes, another factor altering the balance is identified, confirming that the entry requirement is satisfied.

We also discussed questions regarding reorg: what happens if a reorg is necessary and how the state handle reorg for both verification and proposal. This area remains somewhat uncertain in the EL land.

To summarize the call, we acknowledged potential solutions for both validity and availability issues, with some participants confident in the approaches proposed. The idea of prioritizing solutions for validity, possibly by treating availability concerns separately, was supported. Suggestions included using RPC requests for availability in case of a head split or committing summaries to blocks, and considering any state change in an account in the parent state as sufficient for IL entry satisfaction. Finally, there's a call for EL devs to investigate the limitations of current validation conditions.


