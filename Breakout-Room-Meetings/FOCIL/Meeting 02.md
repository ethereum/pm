# FOCIL Breakout Room #02

Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1238#issuecomment-2590169551)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1238

**Date & Time**: [January 14, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://youtu.be/8s4XUc8bg8A

## Meeting notes:
### Intro Topics

- Discussion about IL boost / IL market. Check discord/telegram for more info

### Implementation Notes from Terrence

- Block Processing / Syncing a non-current slot block lacks an inclusion list
- Block Processing / Node remembrance of unsatisfied inclusion list block root
- Block Processing / Unsatisfied inclusion list block root filters the head root
- Block Building / Integrate inclusion lists into block building
- Syncing / Gossip Validation Pipeline
- Syncing / Inclusion list cache
- Validator API / Inclusion list duty retrieval
- Validator API / Inclusion list retrieval for validator signing
- Validator API / Validator Client Changes

### Implementation Note from Jacob

- plan to shift most focus to reth
- plan to launch reth on kurtosis devnet with prysm
- initial testing plan based on custom mempool logic to filter based on e.g. calldata
- transaction spammer would be configured to broadcast “censorable” transactions
- reuse forkChoiceUpdated or new engine API
- updateBlockWithInclusionList
- work required to add new engine API to reth and wire up block production

### Implementation Notes from Jihoon

- Gave notes about how to run Prysm and Geth in Kurtosis
- github.com/jihoonsong/local-devnet-focil
- can check out info for running repo at https://hackmd.io/@jihoonsong/Skidf4ePye

### Implementation Notes from Lodestar
- Making progress and should be feature complete in a week
- Worked on engine_api specs

### Call Links

- https://docs.google.com/presentation/d/1i31wpJpI5B9hb4RE55-eDg1fI3yIoa2T8hj7pNqHQjw/edit?usp=sharing
- https://hackmd.io/@ttsao/focil-implementation-notes
- https://github.com/ensi321/beacon-APIs/pull/1
- https://notes.ethereum.org/@jacobkaufmann/HJzQ1eEDkg
- https://github.com/jihoonsong/local-devnet-focil/
- https://hackmd.io/@jihoonsong/Skidf4ePye
- https://docs.google.com/presentation/d/1cQCafsRKyojl2oQBxK79Xu7AVqQkRywX0Tbut4KNu48/edit#slide=id.p
- https://github.com/ChainSafe/lodestar/pull/7342
- https://github.com/NethermindEth/nethermind/pull/8003
- https://github.com/Consensys/teku/tree/focil
