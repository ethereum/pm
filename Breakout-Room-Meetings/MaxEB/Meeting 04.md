# EIP-7251 MaxEB Breakout Call 04 

Note: This file is copied from [here](https://hackmd.io/@philknows/Sy2kQAq1C)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/996

**Date & Time**: Apr 03, 2024; 16:00-17:00 UTC

**Recording**:  https://youtu.be/aXXd6zwf0cg

EIP-7251 MaxEB Breakout Call #4 - Apr 3, 2024
 
Reference: https://github.com/ethereum/pm/issues/996
Previous Notes: https://hackmd.io/@philknows/BJCaLJf1A

## Custom Ceilings

- Previously on Call #3, there was no consensus on this feature and is technically optional
- Mikhail: If we don't have custom ceilings:
  - 0x02 stakers will need to skim balances, causing a partial withdrawal queue on EL with spam protection under EIP-1559 fee rules.
  - Likely to be used by large staking pools, bloating UX for solo stakers.
  - EIP-7002 was implemented to allow these pools to exit via execution layer (EL)
  - Makes sense to have custom ceilings
- Must understand users like Lido: How often will they skim balances with no custom ceilings?
  - Lido: Nice feature but not important on its own. Two advantages:
    - Compounding (depending on deposit queue size)
    - Could help with rebalancing stake across node operators by setting max upper limit per node operator and skimming for distribution to other smaller node operators
  - Lido: Guessing it won't be often that node operators will be skimming if there's no custom ceilings
  - Lido: We would do an initial rollout with a limit, probably 128 per validator
  - Lido: Skim would probably happen when withdrawals are requested or when validator balance grows… maybe over 135? But happens rarely.
  - Answer: Not often.
- We need to understand if/how consolidations in current design will break other staking platforms like Rocketpool.
  - Are any parts of a minipool bond unwithdrawable post-consolidation?
- No decisions made on custom ceilings.

# `MIN_ACTIVATION_BALANCE` vs `MAX_EFFECTIVE_BALANCE`

- Mikhail: We should use one constant?
  - Spec currently has both
  - Francesco made a comment on why we should not use `MAX_EFFECTIVE_BALANCE` to prevent confusion.
- Lion: Do we want to collapse `MIN_ACTIVATION_BALANCE` and `MAX_EFFECTIVE_BALANCE` retroactively for previous forks?
  - Depends what we want to do with previous forks
  - We can collapse them. Have legacy `MIN_ACTIVATION_BALANCE` and `MAX_EFFECTIVE_BALANCE` into same variable going forward from Electra

## Weak Subjectivity Issues

Problem: Bypassing exit churn with pending deposits queue. How does this change weak subjectivity? Do we need to do something about this? And what can be done if there is an issue?

- Simple case: 32 ETH validator gets exit epoch, then topped up by 2000 ETH. Topped up ETH exits and bypasses exit queue.
  - Could reset active epoch? Which will reset withdrawal epoch, leading to issues
- There are edge cases here that haven't been investigated. We need to think more about this. Mikhail to write up document on thoughts here.

## Concerns from Lido
### Consolidations
Reference: https://hackmd.io/@lido/ryxfTIRFkC

Problem: Lido accounting (on-chain and off-chain) is broken on current consolidation design

- Stake and rewards are based on number of effective validators (fixed at 32 ETH always), not balance.
- Accounting doesn't check for deposits outside Lido protocol deposits
- If node operator can deposit own validator and consolidate it with a Lido validator, it breaks accounting.
- Implementation risks (minor, but many touchpoints increasing risk)
  - Minor issues with skimming, counting total balance on consensus layer, etc.
  - Timeline of Pectra
 
Problem: We need a way to "greenlight" consolidations with our withdrawal credentials

- Any kind of control to approve or prevent consolidation from withdrawal credentials work would
- If we can just set it all to 32 ETH to begin with, it will give us time to adapt to changes even post-Electra
- Trivial to consolidate validators from the same node operator, but also allows other node operators to consolidate with other node operators which is a violation. We could mitigate this with 7002 and eject them for this violation though

Problem: We should also consult other pools such as Rocketpool and Stakewise

- Need to understand if they have additional compatibility issues with current consolidation design
- Rocketpool may have minipool consolidation issues due to the bonds tied to one concrete validator in the pool. Consolidation may forfeit ETH from other minipools (unconfirmed!) and unknown what that means for RPL bonds.
- Lion: We made an incorrect assumption that all validators sharing the same withdrawal credentials is fungible with another when it's not true. **We should now consider execution initiated consolidations to mitigate the risk.**

### Deposit exploit mitigation
Reference: https://hackmd.io/@lido/S1gtK9q1C

Problem: We need to figure out how to mitigate front-running deposits on trustless pools

- Example: Node operator deposits with their own withdrawal credential. Second deposit "tops up" the same validator and node operator steals the second deposit funds

Solution: If there is a deposit and it has different withdrawal credentials than the first, tax it and make withdrawal right away

- Doesn't work with 0x00 credentials
- We would need unbounded withdrawals, need to check with EL. That would be the biggest hurdle.
- Could be independent EIP for inclusion separate from maxEB scope

Big issue for trustless pools

- This might be out of scope and a new EIP will be created for this
- 2 competiting things:
  - Partial Withdrawals
     - Bounded by exit churn
  - Full Exits
    - Unbounded?
    - Maybe 16 withdrawals is a very low bound
 
Need more analysis.

### Other Items
Please review PR for misc changes to the spec:
https://github.com/ethereum/consensus-specs/pull/3636
