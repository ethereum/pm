# Verkle Meeting 11

## Meeting Info

January 29, 2023, 14:00 UTC

Recording: https://youtu.be/YTwUc38GiUI

Original notes: https://twitter.com/rudolf6_/status/1752966751254618547


## Agenda

1. Client team updates
2. Testnet
3. Gas schedule changes
4. Account header group
5. The transition

# 1. Client team updates

@0xadvaita
 for 
@ethnimbus
: continuing to work on our Verkle library. Initial testing is complete. We are now computing the root commitment correctly. Starting with integration into the Nimbus client, and support for statelessness.

@kt2am1990
 and 
@DoctZed
 for 
@HyperledgerBesu
: improvements on the Besu native side, and significant speedup on the time it takes to generate the state root of the genesis block (15s -> less than 1s). Not yet able to produce new blocks, but can follow the chain successfully. For block production, need to finish up a bit more of the cryptography part.

@Gajpower
 and 
@GabRocheleau
 for 
@EFJavaScript
: some house cleaning, and waiting for relaunch of latest testnet so we can try out stateless executions. Also looking at how to incorporate the proving library to verify preState and postState. 
@GabRocheleau
 added: there is a smaller sister repro for WASM typescript implementation of the Verkle crypto. Implementing Pedersen hash in typescript natively, using the underlying Rust compiled to WASM from 
@kevaundray
. And Kev added that he’s made a few changes to the rust-verkle library, which have been upstreamed to Besu native.

@gballet
 for 
@go_ethereum
: continued progress on the shadowfork, and other updates needed for testnet. Once we resolve a few last merge issues, we’ll be able to restart the testnet and unblock the other client teams. Also 
@ignaciohagopian
 has been working on fixing the replay benchmark, which is useful to answer questions around things like avg proof size etc. 

@jasoriatanishq
 for 
@nethermindeth
: implemented EIP-2935 (blockhash). The current implementation works for the Kaustinen testnet, but some potential issues for mainnet. Continuing work on performance improvements in the crypto library.

Somnath for 
@ErigonEth
: waiting for testnet fixes, and in the meantime tried to generate some preimages through the plainstate DB in Erigon. Came out to around 37gb.

# 2. Testnet

Relaunching the testnet, and all of the PR’s discussed on the last call have been merged. The gas model is the same, except that we aren’t charging gas for the `to` and `from`. Also not including the coinbase in the witness if it’s zero. So if the block is empty, then it’s really empty.

A version of EIP-2935 is active on the testnet, but it’s a bit different than the one described in the EIP. There will be 2 locations added to the witness: first one is the location of the block you are interested in, and then also the location of the block that is 256 blocks ahead of the current block. Check out the recording for further convo on this topic between 
@gballet
 and 
@jasoriatanishq
 💪

# 3. Gas schedule changes

@gballet
 and 
@dankrad
 had an extended discussion reviewing some of the nuances of the gas schedule spec in EIP-4762. Few points touched on: chunk_fill_cost (charged every time the leaf is initialized), witness_chunk_cost and witness_branch_cost (everything that is charged for adding values to the witness), and chunk_edit_cost.

Guillaume pushed up an update for EIP-4762 here: https://github.com/ethereum/EIPs/pull/8138

Recommend checking out the full recording for those interested in this topic ⛽️


# 4. Account header group

The current spec says the first 64 slots of an account are going to be in the account header group, and if not then it’s stored in the main storage. Result is that the first 64 slots of the second group are actually unreachable.

Guillaume suggested we leave it as-is, and just make sure it’s documented.

Ignacio added that the only drawback is that if you store stuff in slots 65, 66, etc there’s a branch in the tree that is only 50% fillable. Maybe not a huge problem, but gas cost of storing stuff in that branch might actually be more expensive.


# 5. The transition

Started off getting feedback from Reth on the proposed “overlay transition”. There was a bit of clarification on whether reads to the MPT (Merkle Patricia Tree) would also trigger conversion of those values over to Verkle, which Reth was not in favor of. But since we are no longer planning on doing that (no conversion on reads of Merkle, only direct writes to Verkle), it’s not an issue. Reth has no issues at the moment with the current transition proposal and seems doable from first glance.

Next up, Guillaume shared a proposal for a simplification of the overall transition strategy. The previous strategy we’ve been discussing over the past several months has been to freeze the MPT (it becomes “read only”), and all writes go to Verkle. In addition, each block, an iterator would go over the leaves of the MPT and move a set number of leaves over to Verkle (e.g. each block, 10k leaves get converted from MPT to Verkle).

The simplified proposal: the initial part is the same (where the MPT is frozen and we start fresh with an “overlay” Verkle Tree). However, we hold off on doing any of the actual conversion of MPT leaves over to Verkle. (No iterator, and no conversion of X number of leaves per block).

Benefits of this approach: simpler, and allows us to make a partial transition over to Verkle potentially much sooner than we’d otherwise be able to. Some of the more complex parts (e.g. gas cost changes) could get pushed to a future fork. Another advantage is that we’d stop the growth of the MPT much sooner.

Cons of this approach: can’t have proofs in blocks, so would delay in-protocol statelessness. If we try to ship this simpler approach in Prague, it would almost certainly delay Prague to some extent.

@jasoriatanishq
 asked if it would make sense to do this simplified proposal, but add the gas cost changes and witnesses. So we at least get some partial version of stateless client support. This way you can download the MPT, and if you have the witnesses in the block, then you can act as a stateless client.

There were some comments from Dankrad and others noting that although Verkle is high priority, it’s unlikely there will be agreement to ship a fork that leaves things in an intermediate state that has to be fixed in the future. And that it doesn’t seem like the value we’d get from this proposal is worth the effort and potential delay to Prague.

Discussion on this topic to be continued..