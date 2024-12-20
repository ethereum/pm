
# (e)PBS Breakout Room #14

Note: This file is copied from [here](https://hackmd.io/@ttsao/epbs-breakout-14)

## Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1222

**Date & Time**: [Dec 20, 2024, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://youtu.be/a5k7dg_d42I

# Notes

- **Attendance**: Smaller group due to holidays. Representatives from:
  - Prysm: Potuz & Terence
  - Teku: Stefan
  - Nimbus: Kira contributing to Nimbus for ePBS

- **Fork Choice Simplification**:
  - Potuz will open a spec PR for the latest fork choice simplification based on Francesco's "all-in-one" design.

- **Bug Issue**:
  - Current bug: Proposers building on an empty block cannot deterministically retrieve withdrawals from the beacon state.
  - Will be problematic if interop begins before a pending spec fix.

- **Devnet Updates**:
  - Teku: Rebasing ePBS on top of Devnet5 spec.
  - Prysm: Finishing Devnet5 spec first, then rebasing ePBS.

- **Interop Target**: 3rd or 4th week of January, approximately two meetings away.

- **Genesis Transition**:
  - No major concerns with starting genesis from Electra and transitioning to ePBS.
