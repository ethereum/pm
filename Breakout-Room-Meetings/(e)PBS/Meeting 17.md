# (e)PBS Breakout Room #17

**Note**: This file is copied from [here](https://hackmd.io/@ttsao/epbs-breakout-18)
PS: There’s an inconsistency between the meeting number listed on the agenda and the notes. Also, please note that this meeting note was sourced from [Discord](https://discord.com/channels/595666850260713488/874767108809031740/1346135244780077117).

## Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1292

**Date & Time**: [Feb 28, 2025, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://youtu.be/gKzKY9IWZ0E

# Notes

## Key Decisions & Updates
### 1. Current Devnet Status

- Devnet is stable without additional features
- Prysm still lacks inclusion proofs for blobs
- PTC attestation is working fine with the current design.

### 2. Proposed Spec Updates

- Slot in Payload Envelope: Already implemented in devnet.
- Removing Payload Withheld from Payload Envelope: Need to be updated in the spec.
- Payload Attestation Format: Convert to a Boolean value instead of uint8.
- Random Mix Bug Fix: Cache the last random mix before updating it.
- Handling Empty Block Proposal & Withdrawals: Should be managed at the client level via caching, but need to explicit this in the validator spec.
- New Prefix for Staking Pool Transfers: Builders must originate from a designated prefix.

### 3. Forkchoice & Payment Mechanism

- Francesco’s fork choice proposal introduces complexity in handling payments.
- Suggestion to defer payment mechanism changes until a comprehensive audit is completed.

### 4. Action Items

- Review & Merge Justin’s PR to align with older forks.
- Open a PR for the small changes (slot addition, payload attestation Boolean conversion, random mix caching).
- Investigate the forkchoice model & payment mechanism:
  - If Francesco’s model is used, introduce an additional queue for payments.
  - If current boosts are retained, further evaluation is needed.
- Plan next devnet between Prysm & Teku after PRs are merged.
