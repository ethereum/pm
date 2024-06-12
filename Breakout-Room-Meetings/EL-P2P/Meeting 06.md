# Execution Layer P2P Breakout #6

Note: This file is copied from [here](https://github.com/ethereum/pm/issues/915#issuecomment-1832032520)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/915

**Date & Time**: [November 29, 2023, 13:00 UTC](https://savvytime.com/converter/utc-to-germany-berlin-united-kingdom-london-ny-new-york-city-ca-san-francisco-china-shanghai-japan-tokyo-australia-sydney/nov-1-2023/13-00)

**Recording**:


### Meeting notes:

- We discussed blockers to migrate to discv5. Felix said they are kind of waiting on Nethermind to have an implementation ready.
  - during the discussion about this we discussed how there will be a transitory stage where we would have both discv5 and discv4 enabled on the same port.
- We also discussed hole punching mechanisms and Felix pointed to this [PR](https://github.com/ethereum/devp2p/pull/227/files#diff-0d4a1b70973df7b61b5a379499df260230a79e31f3d05c9d2762619f51a1e227)
- Last there was a discussion from light client that we need to think how to support more blobs on the p2p network as there is a direction to do so in a year or so.
  - We discussed a mempool sharding mechanism and how we can use different identifiers to identify which peer is a member of which shard
    - One is nodeId (easiest solution)
    - Another is Discv5 topic (requires Discv5 implementation to be done in all clients)
