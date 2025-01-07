# FOCIL Breakout Room #01

Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1210#issuecomment-2541647674)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1210

**Date & Time**: [Dec 13, 2024, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://youtu.be/SOt-rNDlsRU

## Meeting notes:
### Spec Stability

- CL spec is relatively stable
- EL spec will be formalized with a PR to EELS

### Spec Questions

- Fork-Choice slot/block enforcement via proposer-boost reorging. This might/should need to be a separate EIP

### Inclusions/Exclusions for First Round

- Blobs will not be included
- Maybe not verify IL's for first round of integration testing

### Rough Timeline

- Shoot for first week of January for next meeting
- Hope that by that meeting we can have at least 1 CL and 1 EL ready to test with
- Shoot for attempting to set up a basic Kurtosis/Hive network between the first clients on the next call

### Spec Test Goals

- Engage with Testing group to figure out timeline for work on spec tests

### Active Branches

- Geth: https://github.com/jihoonsong/go-ethereum/tree/focil
- Lodestar: https://github.com/ChainSafe/lodestar/tree/focil

### Implementation Notes
Goal should be to keep discussion strictly in Discord and on the website https://meetfocil.eth.limo/. Telegram and Twitter should be avoided to help corral the discussion to a single (or two) places.

There are two cases in the execution case. When sync'd and before sync. Should the CL be notifying the EL to check the IL's? This will be different cases for when syncing and after sync is complete. A PR will be opened to the spec to dial this in.

EL will look at specifying that if an IL is passed in then the IL should be checked, if not then the IL's will not need to be verified to check the block. Terrence requested for @Jihoon to open a pr here? https://github.com/ethereum/execution-apis/pulls

### References Posted During Call

- https://meetfocil.eth.limo/
- https://notes.ethereum.org/@jacobkaufmann/Sy7sNHKVye
- https://hackmd.io/@jihoonsong/BJUVIsY4ye
- geth prototype: https://github.com/jihoonsong/go-ethereum/tree/focil
- https://github.com/ChainSafe/lodestar/tree/focil
- https://github.com/ethereum/execution-apis/pulls
- https://hackmd.io/@potuz/BkpzmOgK6
