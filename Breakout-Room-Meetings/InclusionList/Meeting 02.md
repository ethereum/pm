# Inclusion List Breakout Room #2

Note: This file is copied from [here](https://hackmd.io/@ttsao/Bkg53AHAT)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/981

**Date & Time**: March 18, 2024, 14:00-15:00 UTC

**Recording**: https://youtube.com/live/GVdkDXZTtnw

# Inclusion List Breakout Room #2

Monday, March 18, 2024

## Objective
The purpose of this break out room was to reach a consensus on the PoC spec details, enabling client teams to start implementation and decide on the IL for Pectra hard fork in the coming weeks.

## Key Decisions for PoC Specifications:

1. Conditional vs. Unconditional IL for next slot proposer
2. IL tx placement in the next block
3. IL gas limit considerations
4. Bundle vs. Unbundle over p2p

## Discussion on Bundle vs. Unbundle
We explored the bundle vs unbundle approach. The primary advantage of bundling was to prevent issues similar to the blob scenario, where block validity was tied to IL availability. However, this concern is mitigated by the ability of clients to track the fork choice status of the IL availability. If the IL is unavailable, the leaf block cannot be considered the head or attested to (find your own meaning!), this simplifies the implementation and original concern. A potential risk here is collusion between current slot proposer and the next slot builder, including a very late IL at 11s mark. To address this, adjustments to the late block reorg strategy might be necessary. Another solution is including the ability for p2p to recover the IL and allow blocks to include summaries, but we have to agree to include the summaries in block body which we don't today. The decision was to proceed with the unbundle approach.

## Syncing Block By Range
It was discussed that IL is not needed for syncing by range, as execution API's newPayload will handle the validity checking of IL summaries vs. IL transactions as node sync to head.

## In-protocol vs. Out-of-protocol IL designs
The conversation shifted to out-of-protocol versus in-protocol design. Opposition to out-of-protocol design focused on two main points: the timing of slots (same slot vs. next slot) and concerns over expanding the scope of MEV-boost technology. The current direction is to continue with in-protocol design, pending interest in alternative approaches.

## Gas Limit for IL
The current proposal is a 3M gas limit for IL. Concerns were raised about increased duplicated bandwidth from raising the limit. Also currently, IL transactions do not impact the gas for the next slot, though this is an open question and not a blocker for the PoC. From the follow up convos, the IL should affect gas of the next slot block.

## Committing to Previous Summary vs. Using Attestations
Discussion on moving away from committing the previous summary on-chain in favor of using attestations. This approach requires fewer consensus changes but could expose nodes to DoS attacks, as the attesters would need to track every IL, which is not ideal.

## Nonce Checking on the EL Instead of Parent Transactions
G11 raised a good proposal to eliminate the contract that tracks previous blocks' transactions, tying the validation of the payload for block N+1 to nonces. The summary would consist of addresses and nonces, with the proposer of block N+1 including the signed summary and payload. The EL would verify each entry in the summary against transactions in the payload or check the current state's nonce for the account against the summary's nonce.

## Next step
The meeting concluded with plans to finalize the IL PoC specs. Client teams will begin PoC implementations and try interop on a devnet, followed by another breakout session in a few weeks.

