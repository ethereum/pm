# EIP-7251 MaxEB Breakout Call 06 

Note: This file is copied from [here](https://hackmd.io/@philknows/Hywht12eR)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1012

**Date & Time**: April 16, 2024; 16:00-17:00 UTC

**Recording**: https://www.youtube.com/watch?v=J1i3WtLE-6o 

EIP-7251 MaxEB Breakout Call #6 - Apr 16, 2024

Next call: Tuesday Apr 23 @ 1200 UTC.
See PM issue for details: https://github.com/ethereum/pm/issues/1018

**Please reach out to all stakeholders to participate in these calls to voice any concerns and clarify specification for downstream staking pools/entities!**

Reference: https://github.com/ethereum/pm/issues/1012
Previous Notes: https://hackmd.io/@philknows/S1JbLXmlA

## EL vs CL Consolidations
BlockDaemon

- Preference slightly on for EL triggered
- Needs consolidation feature

[Rocketpool](https://discord.com/channels/595666850260713488/1215700233741275217/1229740173068337244)

- Each validator in Rocket Pool has its own withdrawal credential smart contract
- We would not be able to consolidate our validators using the consolidation feature
- We will use 0x02 validators in our next release
- But for our current node operators to take advantage, they will have to exit and reenter
- Rocket Pool has a median node to validator count of 2 so we wouldn't make much difference anyway
- There will be an incentive for large operators to migrate and consolidate but we would expect them to do it gradually

Eigenlayer

- Preference for EL triggered

Lido

- Preference for EL triggered, will minimize upgrade roadmap (1 upgrade instead of 2 separate)
- Able to adopt faster

Figment

- Suspect EL triggered will be preferred also

Liquid Collective
- Leaning towards EL triggered
- Having more control will lead to smoother transition

P2P (represented by Vasilly at Lido)
- Best option is to gate both CL and EL to prevent surprise consolidations
- Not a final opinion from them officially

### Consideration to move towards EL initiated

- Argued by Mark that CL vs EL complexity is generally the same. We re-use a lot of same patterns from EIP-7002. See https://hackmd.io/@wmoBhF17RAOH2NZ5bNXJVg/SJKPf6reR
- Plan as proposed by "lightclients" is to generalize the EIP-7002 contract regardless of whether or not we use it for consolidations. See [proposed EIP-7685 for General purpose execution layer requests](https://github.com/ethereum/EIPs/pull/8432)
- Mikhail will further review the EIP-7685 proposal

### Decision

- Agreed to move forward with execution triggered consolidations
- Will be left out of Pectra-devnet-0 (see further below)

## Custom Ceilings

- Not many staking pools have spoken up about the need for this feature
- [Idea was brought up by Jim at Attestant](https://github.com/ethereum/pm/issues/1012#issuecomment-2056432366) for "A more flexible approach would be a range (0,100) for each validator which defines the percentage of rewards earned to be returned. This gives flexibility to suit all requirements (0 == full consolidation, 100 == all rewards returned) when it comes to selection, and can be altered if required."
  - Opens up the idea of other methods to enable/manage custom ceilings

###  Decision

- Due to the time sensitivity of pectra-devnet-0 and lack of how we want to technically implement custom ceilings, this feature should be pushed to another EIP with a solid approach.
- Can still potentially be implemented later in Electra development if community consensus largely pushes for it.
- Technical complexity for this feature increases the risk of this already risky EIP

## EIP-7002: TARGET_EXITS_PER_BLOCK
Context from Lido:

- Skimmed partial withdrawals are used to firstly, facilitate withdrawals
- If there are no withdrawals, it gets staked to smaller node operators to evenly distribute ETH staked between node operators.
- In 0x02, operators (big and small) grow indefinitely and require one of two options to deal with stake distribution:
  - Exits
  - Partial withdrawals
- For partial withdrawals, estimated to be 400 operations per day combined with other withdrawals done by others.
- Depending on UX and prices, this queue can get crowded quickly

To minimize the crowded, expensive queue, we considered:

Include EIP-7685 so that:

- Multiple operations with a separate contract implementing the queue with maximum parameters for each type operation to allow for configuration tweaks in future hard forks.
- Make target maximums a parameter of the system contract that calls the queue.
- Allows for future tuning, similar to MAX_BLOBS_PER_BLOCK.
- Needs to be part of the spec, not the contract
- All operations get put into the same array with a byte in front of it to indicate which type of operation it is.

Gajinder (Lodestar) also supports this idea to push all EL to CL operations into one single execution payload field.

TO-DO: Is there a way we can change parameters like TARGET and MAX to get the behavior that we want without having an irregular state change to update the code or storage?

### Decision
No decision needs to be made right now. Needs more analysis and this parameter can be tweaked in the future with more data on usage.

Mikhail:

- Current setting of 2 was chosen before EIP-7002 was considered to also handle partial withdrawals.
- If we include EIP-7685, we should set it at 8 equally to max partial withdrawal per payload in the current spec.

## EIP-7251: Stricter bound for consolidation queue

- Francesco in favour of the idea
  - Probably should make it a parameter
  - Amount of epochs we allow the queue to grow to
  - Might just be easier to set the smaller limit for the list - Paul Harris also in support
  - Either solution is fine

### Slashing Risks
References:

- https://hackmd.io/@dapplion/maxeb_slashing_risks#MaxEB-slashing-risks
- https://hackmd.io/@5wamg-wlRCCzGh0aoCqR0w/r1aYbH8x0

Paul:

- With EIP-7251 the quotient is reduced
- Whistleblower reward had to be adjusted to to prevent minting extra ETH
- Given that the quotient is pretty low, making tweaks to implement a curve will be added, unnecessary complexity.

## Pectra-Devnet-0 Spec
Spec Issue Tracker: https://github.com/ethereum/consensus-specs/issues/3673

### Decisions

- We plan to leave consolidations out of the first devnet
- We need to get remaining PRs merged ideally by the next consensus call on Thursday Apr 18.
