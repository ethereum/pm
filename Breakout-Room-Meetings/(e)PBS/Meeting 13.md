# (e)PBS Breakout Room #13

Note: This file is copied from [here](https://hackmd.io/@ttsao/epbs-breakout-13)

## Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1198

**Date & Time**: [Nov 22, 2024, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://youtu.be/v80-9dChohM

# Notes

Short call today where we covered two topics:

## 1. Withdrawals for Proposing After an Empty Block:
Proposers building on an empty block cannot deterministically retrieve withdrawals from the beacon state. According to the Capella validator spec, one could use `get_expected_withdrawals(state)` to construct `payload_attributes`, but this fails in the case of an empty block for ePBS.

Two solutions were discussed:

- **Option 1**: Rely on client-side caching of withdrawals as an implementation detail.
- **Option 2**: Modify the beacon state to cache withdrawals instead of withdrawals_root, enabling deterministic retrieval after an empty slot.

Regardless of 1 or 2, there's an action item to update the validator spec.

> Prysm and Teku both prefer Option 1. We are awaiting feedback from other clients. Please share your thoughts in Discord if you have any!

## 2. Builders and Staking Pools:
If any validator can act as a builder, a staking pool node operator with a signing key could theoretically transfer out its balance, leading to a "nothing at stake" problem. A common solution is to give builders a distinct prefix for transfers, but this introduces centralization concerns.

We are in discussions with Lido and other CSM validators to explore decentralized options, such as allowing builders to operate with a minimal 1 ETH stake. Some potential solutions include:

- Using execution requests to specify the maximum allowed bid, though this could be complex.
- Allowing bids only for excessive balances and utilizing a "max EB" design, which would require pools to periodically submit partial withdrawal requests. This approach seems simpler.

More updates will follow as we finalize a solution. If you’re a staking pool interested in this, please reach out!
