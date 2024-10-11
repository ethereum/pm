# (e)PBS Breakout Room #11

Note: This file is copied from [here](https://hackmd.io/@ttsao/epbs-breakout-11)

## Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1173

**Date & Time**: [Oct 11, 2024, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://youtu.be/Oo8c37ZfV3A

## Meeting notes:

This was a brief and focused meeting, covering client updates and the direction of Francesco's work.

### Client Updates:
* **Prysm** has opened the first PR for fork choice. This is a challenging PR as it changes the way we call GetHead and Insert, requiring handling for both blocks and new payloads. Compatibility with the previous fork adds complexity. Additionally, the same PR involves modifying blockchain logic.

* **Lighthouse** is currently reviewing the fork choice specification and rebasing changes from devnet4.

* **Teku** is focused on block production and rebasing changes from the current master to ensure compatibility with devnet4.

* Prysm is optimistic about launching a devnet in two weeks.

### Francesco's Proposal:
Francesco was not in attendance, but Potuz provided an overview of the proposal. It explores the trade-off of keeping fork choice changes minimal while adding additional vote tracking in beacon state for builder payment safety.

Currently, if a builder sends a message to withhold, the fork choice mechanism triggers block slot voting. In Francesco's proposal, the builder counts attestations and, if < 40%, the builder doesn't need to pay as the block won't reach the chain due to proposer boost. If the missing percentage falls between 40% and a certain threshold (N), the builder still doesn't have to pay, but this is managed in the later epoch processing state + vote accounting to ensure builder payment safety.

Tracking votes for payment in beacon state could be complex, and we hope to see the proposal soon. In the meantime, we'll continue with the current ePBS fork choice rule, which can be rolled back if Francesco's proposal proves to be a better approach.
