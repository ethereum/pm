# (e)PBS Breakout Room #9

Note: This file is copied from [here](https://hackmd.io/@ttsao/epbs-breakout-9)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1150

**Date & Time**: [Sep 13, 2024, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://youtu.be/2BUsiUnUZYc

### Meeting notes:
# EIP-7732(ePBS) Breakout #9 Notes

## Summary

- Slot auctions give an out-of-protocol trust advantage for running MEV-boost auctions at execution phase.
- New engine API for retrieving payloads by hash and by range. This could be optimized giving consensus and exectuion are pipelined.
- Process withdrawals can be moved to execution but need extra sanity checks.

## Notes
Julian presented a [new argument against slot auctions, stating that slot auctions](https://docs.google.com/presentation/d/1-MnAqDzR7JapIPpUEbScALEtY5axyRcPgJDpgaJ_qVI/edit#slide=id.p) give off-protocol a clear advantage over on-protocol. The new argument can be summarized as follows. A proposer is better off doing the following:

- Modify the client codebase to always select its own header
- Commit to its own header at second 0
- Between seconds 6 and 9, run a mev-boost auction
- The payment between Builder to the Proposer happens off chain

It's likely that the realized block value will be higher than the expected block value, and the proposer will favor the mev-boost auction. There is an out-of-protocol trusted advantage in committing to your own header and then using mev-boost. This is a strong argument in favor of block auctions over slot auctions. There are a few attacks we want to further analyze, such as same-slot unbundling, to see if they can be triggered. The current plan is to stick with block auctions and then switch to slot auctions when we feel safe to do so.

Mark presented a [new engine API methods](https://github.com/ethDreamer/execution-apis/blob/eip-7732/src/engine/eip-7732.md) to get payloads from the EL. These payloads are required to serve syncing by range nodes. Potuz questioned the necessity of getting such payloads since the EL could retrieve them themselves, and when a CL node is syncing, it only needs to verify if the block hash is valid. We will proceed with Mark's engine API changes, but in the background, we’ll continue considering how to optimize it and potentially use a simpler engine API that only checks if a block hash is valid, as this is made possible with ePBS.

Finally, we discussed withdrawals, specifically whether they should be processed in the consensus layer or execution layer. Processing in the execution layer has several unknowns that need to be carefully considered. It's recommended to watch the talk for more details. For now, we'll stick with processing in the consensus layer unless someone confidently steps up and confirms that processing in the execution layer is safe.

Side note happened in Discord, Potuz mentioned: `ePBS in the CL spec was already changed by Lucas's PR https://github.com/ethereum/consensus-specs/pull/3875. I am in the process of rebasing https://github.com/ethereum/consensus-specs/pull/3854 which will be very very painful. If you guys want to move withdrawals to the EL processing please signal this right now cause I won't make these changes twice 🙂`
