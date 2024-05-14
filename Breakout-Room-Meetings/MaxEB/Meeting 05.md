# EIP-7251 MaxEB Breakout Call 05 

Note: This file is copied from [here](https://hackmd.io/@philknows/S1JbLXmlA)

### Meeting Info

**Agenda**: https://hackmd.io/@wmoBhF17RAOH2NZ5bNXJVg/B1TYJOw0a

**Date & Time**: April 09, 2024; 16:00-17:00 UTC

**Recording**: https://www.youtube.com/watch?v=7F2io3c9NQc

EIP-7251 MaxEB Breakout Call #5 - Apr 9, 2024

Next call: Tuesday Apr 16 @ 1200 UTC.
See PM issue for details: https://github.com/ethereum/pm/issues/1012

**Please reach out to all stakeholders to participate in these calls to voice any concerns and clarify specification for downstream staking pools/entities!**

Reference: https://github.com/ethereum/pm/issues/1008
Previous Notes: https://hackmd.io/@philknows/Sy2kQAq1C

## Consolidations
Debate continues between beacon chain operation vs. execution initiated.

### Additional notes from Lido

- Current design is not ready for consolidation. Multiple places where healthy validators are assumed to be near 32 ETH effective balance.
- Validators are not actually fungible, even under the same withdrawal key
- If we do beacon chain operation for consolidations (no gatekeeping or initiations from execution layer), we will need to upgrade in two steps:
  - Step 1: Safeguard accounting to prevent breaking if there are accidental consolidations.
  - Step 2: Architectural upgrade in include maxEB.
- If we do execution initiated operation for consolidations, we can do the upgrade all at once with everything complete to support.
- No Consolidation Option: Not a problem if no consolidations are not included with maxEB. They would lose out on some useful features like balancing ETH between operators
- Lido would prefer that if we cannot ship EL initiated consolidations, it would be preferred that there's no consolidation until Lido is ready for Step 2 in their 2-step upgrade.

### Feedback from Mikhail

- Not sure if we can do execution initiated consolidations in this hard fork.
  - We would need to extend EIP-7002, adding more fields: `signature`, `target`, `source`
  - Or have another smart contract
- Having no consolidations at all is also an option.


### Rocketpool Notes

- Consolidations don't necessarily break Rocketpool.
  - Minipools are never shared between validators Each pool as its own withdrawal credential.
  - Each withdrawal credential matches 1:1 with each validator
  - Case: Node operator may consolidate minipool to ourside validator. Funds would be safe, metadata would be wrong. Cost of 16 ETH.
- Today RP would be safe with current consolidation spec
- Would prefer execution initiated consolidations to limit attack surface
  - CL update is out of protocol.
  - Would probably need outside stuff like oracles to deal with this.
  - EL messages are easier for RP to engage with.
- Rocketpool minipools will likely not consolidate
- Median number of validators per node operator is low (2).
- In the case of top-ups (depositing out of band) it would be seen as a gift to rETH holders because it's all treated as rewards from beacon chain, then splits them between rETH holders and node operators
- Smart contracts today wouldn't be able to use maxEB properly.
- Looking to support in next version
- Compounding is good for rETH holders to bring up yield
- Deposit flow for changing validators to 0x02 compounding is not ideal. Out of protocol and RP would see it as a reward for rETH holders.
- No Consolidation Option: Rocketpool indicated this would not affect them. Unlikely validators there will use this feature.


### Decision

- It's widely agreed upon that for adoption of EIP-7251, consolidations need to be included.
- Note that it will require more work on some of these staking protocols (e.g. Lido), so adoption may be slower.
- Pending additional feedback from other stakeholders, beacon chain operation (as current in spec) is going forward at least for devnet-0 until more feedback is considered.


## Custom Ceilings
- None of the pools yet have a strong opinion on this
- Helps solo stakers mostly
- Leaving this feature out would reduce complexity
- Concern: Using the EL withdraw request heavily if we don't implement.
  - Target requests = 2 requests per block
  - Functions similarly to EIP-1559 dynamics
  - Fee would grow quite quickly with a large number of requests
  - **How heavily will EL partial withdrawal queues be used by staking pools?**


### Decision
As of right now, there is not a lot of demand for including this as the benefits are minimal and increases complexity of implementation. Please speak up (solo validators!) if this is important to you.

## Weak Subjectivity in Top-Ups
Please see Francesco's PR: https://github.com/ethereum/consensus-specs/pull/3650

### Decision
Under reviews, will likely get merged.

## Preparation for pectra-devnet-0

- There is agreement amongst teams to implement EIP-7251 as is currently in the spec, while in parallel getting more feedback to above design changes.
- We will need be more firm as there is a timeline of 1 month to prepare for devnet.
- **Please speak up if you have opinions!**
- **Please share and see explanations we require the staking community to provide feedback on! EIP-7251 for Staking Pool Operators**
