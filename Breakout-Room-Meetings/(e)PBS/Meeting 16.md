# (e)PBS Breakout Room #16

**Note**: This file is copied from [here](https://hackmd.io/@ttsao/epbs-breakout-17)
PS: There’s an inconsistency between the meeting number listed on the agenda and the notes. Also, please note that this meeting note was sourced from [Discord](https://discord.com/channels/595666850260713488/874767108809031740/1339970681030312007).

## Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1292

**Date & Time**: [Feb 14, 2025, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://youtube.com/live/MkGsy3UeJv0

# Notes
## Current Status:
- **Happy Case**: Prysm and Teku are finalizing the ePBS devnet successfully.
- **Edge Case Under Investigation**:
  - Prysm does not receive the payload from Teku over gossip.
  - Ensuring that the payload can be requested through a sync RPC request and processed in a timely manner.
  - This issue is more challenging with a **6-second slot time**.

## Next Steps / Updates to the Spec:
- Planned Changes (to be done within a week):
  - Add `slot` to the **payload envelope**.
  - Remove **payload withheld** for payload attestation.
  - Switch to **Francesco's all-in-one fork-choice design**.
  
## Edge Cases Discussed:
1. Receiving a beacon block but the corresponding execution block is unknown, while the parent beacon block is known.
2. Receiving an execution block without knowing the associated beacon block.
3. After receiving a beacon block, the execution block never arrives within 8 seconds.
4. Syncing a parent block that reorgs the previous block's full status, which has been a source of bugs.

## Open Questions:
- Payload Request: Should the payload request use block hash instead of block root for easier lookup?

## Client Participation:
- **Nimbus** contributor will start work next week.
- **Lighthouse, Lodestar, and Grandine** are currently missing from participation.
