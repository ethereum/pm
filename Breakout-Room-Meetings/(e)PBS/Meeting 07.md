# (e)PBS Breakout Room #7

Note: This file is copied from [here](https://hackmd.io/@potuz/ByZVEya5A)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1133

**Date & Time**: [Aug 16, 2024, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://youtu.be/fQx_UbaPX-E


### Meeting notes:
#### Highlight:
This meeting had very low attendance. Essentially all conversation was between @g11tech from Lodestar and @potuz from Prysm, therefore decisions during this meeting are temporary and require further discussion with the ePBS community involved in the EIP.
Comment
Suggest edit

As a first point @potuz gave an update on the EIP status, no changes since last meeting, the first PR to the consensus-spec repo has been merged.

After this exposition we moved to implementation status. Prysm has a somewhat advanced implementation, with types, many core processing helpers, database and sync/RPC changes already developed or under way. Lodestar already implemented types and is ramping up implementation with two devs in charge.

@g11tech raised a discussion on how the block production workflow would be at the Beacon API and Engine API level and how does it change from block auctions to slot auctions. The validator <-> Beacon communication over the Beacon API changes as it requires now two separate calls at the beginning of the slot, one to get the `ExecutionPayloadHeader` to sign in case of local building, and another to get the `BeaconBlock` to sign. The communications the Beacon <-> EL over the engine API **do not change** on block auctions. The beacon requests a payload at the start of the slot and produces both the `ExecutionPayloadHeader` and the `ExecutionPayloadEnvelope` for the validator to sign. On Slot auctions however the engine API may change, in principle clients could implement local block production as-is without any changes, but it would be more profitable to have a new Engine API endpoint that gives an oracle of what the current value of the current block is, and continue building the block until it's requested on `get_newPayload`.

After this we discussed the situation of free DA under block auctions described [here](https://x.com/potuz_eth/status/1824417162808729869). It was signaled that moving to slot auctions sooner rather than later is the safest approach. @potuz offered to open the consensus-spec PR relative to this.

Finally @potuz requested researchers to investigate the possibility of processing withdrawals with the payload rather than the beacon block as it is done today. The design is simpler and requires no changes in the withdrawals pipeline.
