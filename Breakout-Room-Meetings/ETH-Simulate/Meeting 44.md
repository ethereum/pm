# Eth_Simulate Meeting Meeting 44
Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1405)

### Meeting Info

- Agenda: [ethereum#1405](https://github.com/ethereum/pm/issues/1405#issue-2943334088)
- Date & Time: March 31, 2025, 12:00 UTC
- Recording: [here](https://youtu.be/O6fHpZlVLcs?si=oyz2tWwBrgLs3F0D)
## Notes
## Eth_Simulate Implementers Call Summary  

## Key Discussion Points

## Geth Transaction Sender Fix
- Sina submitted a fix for the issue where the transaction sender appears as zero in Geth.
- The solution is considered "hacky" but is the best available option for now.
- The fix is pending merge and is targeted for the next release.

## Block Timestamp Handling
- Sina observed that Geth still complains when two blocks have the same timestamp, despite previous discussions allowing timestamps to remain the same or increase.
- This flexibility was agreed upon to support chains with sub-second block times.
- **Action Item:** Check if Nethermind also accepts identical timestamps (to be tested).

## Base Fee Encoding Mismatch (Geth vs. Nethermind)
- A hash mismatch issue was identified due to differences in RLP encoding of block headers, specifically concerning the `baseFee` field.

### Geth Behavior:
- Encodes an extra `0x00` byte when `baseFee` is zero.
- Distinguishes between `null` (pre-EIP-1559) and non-null (post-EIP-1559) `baseFee` values.

### Nethermind Behavior:
- Does not encode `baseFee` at all if it is zero (treats zero as equivalent to null).
- Does not support null values in its internal model.

### Root Cause:
- The edge case arises in `eth_simulate`, where `baseFee = 0` is allowed (unlike in consensus, where `baseFee` cannot be below 7).

### Proposed Solution:
- Use a separate RLP encoder for `eth_simulate` to ensure consistency between clients.
- Sina will test if removing the extra byte resolves the hash mismatch.

## State Root Mismatch Fix
- A minor fix related to the spec was implemented, and state roots now match between clients.

## Tracing & Interns
- Sina has not yet worked on tracing improvements but suggested onboarding an intern to assist.
- Nethermind’s core team has limited interns, as most work on non-core projects (e.g., PhD-related research).
- Past interns were rarely assigned to core development due to complexity.

## Action Items

### Sina:
- Test if the `baseFee` RLP encoding adjustment resolves the hash mismatch.
- Follow up on merging the transaction sender fix.

### Team:
- Verify Nethermind’s handling of identical block timestamps.
- Document the `eth_simulate`-specific RLP encoding approach for `baseFee = 0`.

## Next Steps
- Confirm block hash alignment after the `baseFee` fix.
- Discuss intern resource allocation for tracing work if needed.
