# Execution Layer P2P Breakout #3

Note: This file is copied from [here](https://github.com/ethereum/pm/issues/858#issuecomment-1708403774)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/858

**Date & Time**: [September 6, 2023, 13:00 UTC](https://savvytime.com/converter/utc-to-germany-berlin-united-kingdom-london-ny-new-york-city-ca-san-francisco-china-shanghai-japan-tokyo-australia-sydney/aug-9-2023/13-00)

**Recording**:


### Meeting notes:

- EIP draft was presented: [eth/69: available-blocks-extended protocol handshake](https://hackmd.io/@smartprogrammer/rkqC8y42n)
- @lightclient expressed concern around this EIP signaling client teams to prune older legacy blocks (which Nethermind is already doing through AncientBodiesBarrier and AncientReceiptBarrier. @jflo mentioned that Besu is also doing that with CheckpointSync). @lightclient was concerned about how this would affect the chain where only a handful of nodes have all the blocks and finding the node with all the blocks would be harder through discovery.
- I discussed another concern from @holgerd77 that nodes could start disconnecting peers that do not have the block range they need. This would result in the nodes possibly trying to sync being disconnected since they dont have the needed range by others. This can be addressed in the EIP by explicitly mentioning that nodes must not disconnect peers that do not have the range they need.
- @lightclient and @jflo will ask people from their team to review the draft and comment with any concerns they have.
