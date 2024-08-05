# (e)PBS Breakout Room #6

Note: This file is copied from [here](https://hackmd.io/@ttsao/epbs-breakout6)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1120

**Date & Time**: [August 02, 2024, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://www.youtube.com/watch?v=Otxw1uXxFCI

### Meeting notes:

- EIP-7732 spec remains stable and opened: https://github.com/ethereum/consensus-specs/pull/3854

- Prysm team is moving full steam ahead with implementation, and Lodestar is joining.

- The Engine API new payload has previously required the parent root as a parameter for EIP-4788. It's harder to get this parent root since block.payload changes to block.header as the canonical object. It's not a hard blocker as the client team can work around this either by getting it from the fork choice store. If needed, we can extend the parent root to the header envelope itself. 

- The rest of the call focused on discussing slot auctions. Self-building comes with a disadvantage as the local EL client does not provide a good estimate of the block value 6 seconds later compared to a sophisticated builder. There could exist some estimator functions to help self-builders estimate, and whether that is sufficient remains an offline question, which we will continue to discuss on Discord. We also discussed if it's possible for local block value to decrease from 0s to 6s. Given that the local node acts honestly, transaction replacement and account abstraction could potentially make the local block value lower, which further complicates things.

- That's it for this week. Expect a lot more progress with client implementations in two weeks.
