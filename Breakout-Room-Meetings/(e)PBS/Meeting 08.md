# (e)PBS Breakout Room #8

Note: This file is copied from [here](https://hackmd.io/@ttsao/epbs-breakout-8)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1135

**Date & Time**: [Aug 30, 2024, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://youtu.be/BZhYP-JRS7U

### Meeting notes:
#### Highlight: 
- Teku, Nimbus, and Lodestar all support moving to a slot auction, preferably sooner rather than later.

#### Client Updates
##### Teku

- Updating validator client code
- Adjusting events based on ePBS intervals
- Adding PTC utilities and helpers
- Updating state transition function
- Adding new p2p gossip rules (Stefan has feedback, notes and feedback will be shared)

##### Lodestar
- Working on state changes
- Developing block proposal path

##### Nimbus
- Collaborating with EPF on new block and state structure

##### Prysm

- Implementing new RPC endpoints
- Updating execution payload state transition function

#### Free DA Problem / Slot Auction

- We reviewed the free DA problem again. Everyone understood the issue, so there wasn’t much more to discuss.
- We discussed why we haven't started the slot auction yet. The previous decision was to wait for more consensus before moving forward. Teku, Lodestar, and Nimbus expressed support for the slot auction during the call, so it might be a good time to proceed before more client code changes are made, even if the changes are relatively small.
- We talked about the downside of the slot auction, such as making local value forecasts more difficult. Everyone understood the problem.

#### Research Updates

- Julian presented two pieces:
  - [A Note on Equivocation in Slot Auction ePBS](https://ethresear.ch/t/a-note-on-equivocation-in-slot-auction-epbs/20331)
  - [The Role of the P2P Market in ePBS](https://ethresear.ch/t/the-role-of-the-p2p-market-in-epbs/20330)
- There was no feedback on these pieces. Any feedback can be sent to Julian or posted on Discord.
- I presented [Block Proposal in ePBS Block Auction](https://hackmd.io/@ttsao/epbs-block-proposal), focusing mainly on optimizing the API to reduce proposal time with extra header signing. Dustin emphasized the importance of giving the proposer the sovereignty to choose between a local block and a builder block.

#### Final Notes

- We discussed testing, with less emphasis on consensus spec tests and more on client implementations and setting up a local devnet. More implementations are needed to find spec bugs and gaps. We hope to have a devnet ready before Devcon.
- Dustin mentioned it would be nice to have a milestone page, similar to how we track previous hard forks, for local devnet with solo proposers (M0), local devnet using p2p bids (M1), multi-client devnet (M2), etc.

That's it for this week. See you all in two weeks!
