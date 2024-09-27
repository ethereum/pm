# (e)PBS Breakout Room #10

Note: This file is copied from [here](https://hackmd.io/@ttsao/epbs-breakout-10)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1157

**Date & Time**: [Sep 27, 2024, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://youtu.be/s5Bx_CWf5yg

### Meeting notes:

We thought it was going to be a 5-minute meeting, but it ended up lasting over an hour. I didn’t capture the open-ended discussions, only the actual action items. For open-ended discussions, please refer to the recording. The action items are the following:

- Process withdrawals will continue to be on the consensus layer. If we move process withdrawals to the execution layer, verifiers would use the post-beacon state (or pre-execution state) to verify withdrawals, causing asymmetry. The builder commits withdrawals using the pre-beacon state, but the verifier uses the post-beacon state. There’s no clean solution to this unless we move to a slot auction.
- Clients provided their updates with steady progress. Teku is completing the beacon chain spec, Lighthouse is getting to the fork choice spec. Most of us are waiting to implement fork choice last, and we are just now focusing on it. Fork choice remains the critical component and the most non-trivial change in this EIP, so more attention is needed.
- There were open-ended questions about why payment has to be done on the consensus layer and why builders have to be staked. A simple answer was reduced complexity. Currently, ePBS is only scoped for CL changes, with no engine API or EL changes. Moving payment to EL without staked builders would significantly increase complexity, alongside fork choice and other open questions.
- There were open questions about what benefits ePBS brings, which are documented in these posts. Feedback is welcome:
  - https://eips.ethereum.org/EIPS/eip-7732
  - https://hackmd.io/@ttsao/bypassing-relayer
  - https://hackmd.io/@potuz/rJ9GCnT1C#Extra-benefits
- There were open questions about having some sort of ePBS office hours instead of breakout calls to allow more open-ended discussions. Potuz and I are totally open to this, just let us know.
- We talked about making significant development strides to have a devnet before Devcon. The next few weeks will be crucial as we progress toward this goal. More updates in two weeks.
