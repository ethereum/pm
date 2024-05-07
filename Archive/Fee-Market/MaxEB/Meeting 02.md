# EIP-7251 MaxEB Breakout Call 02 

Note: This file is copied from [here](https://hackmd.io/@philknows/BkEL0Fu0p)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/989

**Date & Time**: March 20, 2024; 16:00-17:00 UTC

**Recording**: https://youtu.be/UZ8iv3OFaOM



## MaxEB Electra Priority

Discussions about priority of this feature over others is subjective in terms of value and complexity. This document will outline questions remaining about the feature, some proposed design choices and the state of completeness for inclusion consideration.

This document is to float conversation and the current state of the maxEB implementation to give developers an idea of where this feature fits within the Electra fork alongside other EIPs for consideration.

### Update from Preston (Prysm)

* Not a super complex integration after spec review
* Identifies priorities for Electra from highest impact (largest feature demand) in order as Max Effective Balance (MaxEB), Inclusion Lists (IL) and then PeerDAS.
* Able to potentially do both MaxEB and IL.
* Committed to including for Electra

### Update from Lighthouse
* MaxEB is a priority for Lighthouse
* Has resources to work on both MaxEB and Inclusion Lists, but no timeline commitments
* Important to consider maxEB for inclusion because we don't know where the first bottlenecks are going to come up if data set grows too large.
* This change benefits all clients

### Clarity required about Electra + F-star hard fork timings
* Agreed that we need some clarity on timing expectations for a "small hard fork" in 2024 which will help determine ability to include maxEB and/or inclusion lists.
* Lodestar signaled ability to include both inclusion lists and maxEB for end of 2024.
* Parallel work can be done for PeerDAS alongside these two features

### Complexity of MaxEB
* MaxEB has a lot less moving parts comparatively to blobs (e.g. No new cryptography, simple single signature verification, etc.)
* Lodestar signaled the idea of separating these two large features (maxEB + IL) into separate forks to reduce complexity and risks, with maxEB potentially first
* Mike Neuder stopped pushing as hard on this EIP since January due to poor sentiment at the time
* There is a weak proposal to try and get the following Proof of Concept together within the next month to target EOY 2024:
  * EIP 6110: Supply validator deposits on chain
  * EIP 7002: Execution layer triggerable exits
  * EIP 7549: Move committee index outside Attestation
  * EIP 7251 Increase the MAX_EFFECTIVE_BALANCE

## Outstanding Decisions

#### 1. How do we handle changing to the compounding withdrawal prefix?

* Option 1: Inside processPendingDeposits
  * Add new deposit to a validator queue, which adds to the balance, then automatically changes to `0x02` by making the deposit
* Option 2: Inside processConsolidation
  * Publish consolidation message to consolidate value
  * Simple UX, similar to BLStoExecution. Users are familiar with this workflow
  * Not as much engineering because this type of infrastructure already exists with BLStoExecution
* Option 3: Execution Layer initiated 0x02 consolidation upgrade
  * Mike proposed an idea to change the prefix via 0x01 execution address and to bundle it with consolidation
  * Less complexity for CL clients
  * If we are ok with allowing the authority to come from 0x01 withdrawal credential, we can have a similar model to EIP-7002.
    * EL + Validator credential: Consolidate `pubkey/validatorIndices`
    * Propagate to CL optimistically
    * CL checks the list and validates consolidation
    * Then, `processConsolidation` (EL has already authorized and checked authenticity of operation)

#### 2. The spec does not specify how we actually get these signed consolidation operations into blocks.

* Option 1: Beacon chain operation
  * Complex:
    * Must broadcast signed consolidation messages
    * Gossip topic = dealing with spam
* Option 2: Wait for block proposal
   * Once you get a block proposal, it'll pack your consolidation message into a block
   * Not an issue for large staking pools (target of proposal) because of their block proposal frequency. They could even help pack consolidation messages from others.
* Option 3: Execution Layer initiated 0x02 consolidation upgrade.
   * See operation above.

## Additional Ideas
Additional ideas which were floated during the meeting for consideration.

### Improved light client security
Referencing the [light client breakout call](https://hackmd.io/@philknows/ryMFFQUpT) to implement light client slashing.

* Improved economic security with the same number of validators in the committee with consolidated stake
* Could consider having a higher minimum effective balance of >32 ETH for sync committee participation









