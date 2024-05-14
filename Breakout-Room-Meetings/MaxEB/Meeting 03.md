
# EIP-7251 MaxEB Breakout Call 03 

Note: This file is copied from [here](https://hackmd.io/@philknows/BJCaLJf1A)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/993

**Date & Time**: March 26, 2024, 12:00-13:00 UTC

**Recording**: https://www.youtube.com/watch?v=cGcjxna5HSg 

## Problems Discussed

- How are validators consolidated?
- How do individual validators update to 0x02?
- Custom ceilings (this meeting did not lead to a conclusion)

## How are validators consolidated?
### Option 1: Beacon Chain Operation
- Must add gossip topic to this
  - Not more complexity than the `BLStoExecution` logic which was thoroughly tested from Shapella.
- Requires spam mitigation
  - Logic for preventing spam shortly before the fork can be reused
  - Some clients also just stopped listening to topics X epochs after the fork
- If we just don't listen to the new topic until the fork, we can reduce complexity.
  - There should be no reason why people are speed running consolidations, unlike `BLStoExecution`
- Pro: Adding a gossip is not a consensus change
- Pro: We also can remove this gossip topic easily in the future without a fork (less technical debt)
- Con: Requires client team coordination to remove topic later to prevent peering issues and network partitions (simpler than consensus change or other options)
- **Gossip topic is the tentative plan for consolidations**


### Option 2: Block Proposal Consolidation Message Change

- Con: Disadvantage for stakers with few validators
- Con: Takes a long time for small/solo operators to propose a block with the change
- Con: There would need to be some initiative/sidecar to help disadvantaged stakers broadcast their consolidation change, similar to the [ConsensusLayerWithdrawalProtection group for broadcasting BLStoExecution changes upon fork time](https://github.com/benjaminchodroff/ConsensusLayerWithdrawalProtection)
- Not sure why we would build a whole infrastructure outside of the system for a one-time change
- Worse UX
- We don't see pools (e.g. Lido, Rocketpool, Coinbase, etc.) building out infrastructure to help users get their messages in.


### Option 3: Execution Layer Initiated

- Con: Needs general buffer and separate contract to handle messages
- Con: Gas costs
- Con: Cannot guarantee inclusion
- Con: Will have to change block structure (more tech debt)
- Pro: Signature/Auth validated by the execution layer

### Consolidation Additional Notes:

- Assumption: Most larger pools will have the same withdrawal credentials
- Assumption: Most Rocketpool node operators will consolidate their minipools
- We should be careful not to accumulate more technical debt from this operation (e.g. Merge code is technical debt now)
- Point not highlighted in the spec: If you are a pool and you want to minimize the amount of time in the queue, **do not get slashed** or the inactivity period will extend. Normally it is 27 hours between exit and withdrawable epoch.

## How do individual validators update to 0x02 compounding?
This feature can be tied in with custom ceilings (stil in discussion).

This is an important feature as half the EIP is to help solo stakers auto-compound their ETH.

### Option 1 of 1: Deposit 1 ETH to deposit contract for `0x02` auto-compounding

- Con: Requires 1 ETH (but you need >=33 ETH anyway for compounding to be viable)
- Con: Option not in the spec currently
- There are 2 types of deposits you can make to the deposit contract:
- Compounding deposit
- Non-compounding deposit
- Top-ups via deposit do not automatically trigger to compounding
  - e.g. Any `0x00` credentials do not compound
- 0x02 deactivates the partial withdrawal sweep for you
- Minimal complexity: Purely a state transition function. We have to modify applyDeposit function anyway (~+4 line addition)
- You will not be able to go from 0x02 back to 0x01

### Proposed Deposit Flow:

1. Deposit
2. Check signature is correct
3. Signalling BLS pubkey is in the state?
  - If no, attach validator record
  - If yes, top up validator

#### Top Up Validator Path:

- Question: Do any staking setups break if someone changes the address?
- We only check the signature if they want to do an address change, otherwise it's just additive

## Custom celings (To be continued in next meeting)

- Do we want to allow this at all? Still need to come to an agreement on whether or not we need this feature.
- If yes, do we want to specify this on deposit?
- If changing your withdrawal metadata, can you change your custom ceiling?
- If we have custom ceilings, which ceilings do we switch to?
- We don't think that you can ever decrease your ceiling. Users would just exit and re-deposit to a new validator
- Consolidation: If you consolidate X validators, we should just sum the consolidation sources and use that as the maxEB.
- Consolidation: Considered allowing consolidation message to identify the maxEB setting. Must be greater than the sum of all consolidated validators (4 validators = 3 consolidations = maxEB cannot be less than 128 ETH)
- Does decreasing the maxEB cause withdrawals to go through any queue?

#### Technicals for Discussion

- Define a ceiling at deposit time
- Instantiate a new validator with 0x02 and some number of the padded bytes in the withdrawal credential that define the ceiling between 32-2048 ETH.
  - `0x02` `XXXXXXXXXXX` `0123456789abcdef0123456789abde`
- Pro: Simpler to implement
- We need to have some logic to control what happens when you deposit at random
- EIP-6110 allows for more deposits within a block, but we have a max limitation for deposits per block so no computational attack is possible.
- We have to validate signature on 0x02 credential change
