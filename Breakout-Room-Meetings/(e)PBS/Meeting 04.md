# (e)PBS Breakout Room #4

Note: This file is copied from [here](https://hackmd.io/@ttsao/epbs-breakout4)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1083

**Date & Time**: [July 05, 2024, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://youtu.be/WC9XsungamU


### Meeting notes:
#### Highlight:

1. EIP is here : [EIP-7732](https://eips.ethereum.org/EIPS/eip-7732)
2. Consensus spec pull request is here: [PR-3828](https://github.com/ethereum/consensus-specs/pull/3828)
3. Processing withdrawals as part of the execution payload has additional complications, such as engine API fcu+payload_attribute withdrawals being fresh.
4. Bid gossip P2P is vulnerable to DoS if we don't constrain bid values.

#### Summary:

- We have an EIP number! ePBS as we know it today specific to block auction, will now be referred to as EIP-7732.
- Potuz is wrestling with the consensus layer spec unit tests. Given the structural changes and 700+ failed tests post-ePBS, this will be the main focus for the coming week. The current PR could be merged as is, with subsequent PRs to specifically address the failing tests.
- We brought up the first agenda item: Advantages/Disadvantages for builders/proposers not using the in-protocol auction. No one had anything to say on this topic, so we moved forward.
- We discussed processing withdrawals as part of the execution payload. This shifts the withdrawal to the payload itself, making it cleaner and similar to how Electra processes deposit/withdrawal requests today. We considered edge cases, such as empty slots where withdrawals are not honored in the EVM. The following execution proposer would then have to honor it, but by that time, the validator's balance could be lower. Another main tradeoff discussed was the execution-API change where we call FCU and payload attribute to the local execution client, ensuring the withdrawals in the payload attribute are "fresh," meaning the head state should be processed to the latest slot.
- We talked about PTC equivocations. A malicious builder could split the PTC votes to half reveal and half withhold, using the last PTC vote to equivocate and split the network under two views. It's unclear what advantage a builder could gain from this attack, other than causing network issues. A potential solution is to change the threshold from 50% to 66%, requiring a builder to cause this attack with 33%. However, it's uncertain if this is worth pursuing.
- We discussed the gas limit. A proposer could use a bid from RPC or P2P. For RPC, we could update get header to include a gas limit field, where builders may already cache different bids by different gas limits based on validator preferences. We don't need a registration RPC call like today. For P2P, we talked about the current P2P DoS concern since any validator could gossip a low-value bid. We could change the DoS pipeline to top N bids or use a simple heuristic.
- Finally, we discussed pre-confirmation and the inclusion list. Nothing major was noted, so I won't include them here, but feel free to watch the recording if you want more details.
