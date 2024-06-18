# EIP-4844 Implementers' Call #26 

## Meeting Details
### [Agenda](https://github.com/ethereum/pm/issues/818)
### Date: Jul 10, 2023	
### [Video Link](https://youtu.be/vdFD5w0OIqA) 
## Notes: Orignally Documented [here](https://docs.google.com/document/d/15EatedrJanNxBZGPVASvwq9xgbTs5UxjsDfjpM6ppSY/edit#heading=h.ub6g85pp78v)

### Notes 

**Devnet 7 updates:**
https://forkmon.4844-devnet-7.ethpandaops.io

Parithosh: mainly have lighthouse / teku, with geth/nethermind sharing.  Network is stable.  Blob explorer: https://blobscan.com has been updated to spec and works. Any other blob testing can happen on this testnet.  Avoiding too much load spamming because we did trigger an issue w/ Besu and wanted to give it some time.  We are sending some blobs however.  Issue tracker 
https://notes.ethereum.org/@parithosh/dencun-issue-tracker
Some issues with deposits, will look into potential fork digest issues.

Besu status: some issue with datahash operation, think we have it covered under hive tests, so should be fixed any hour now. This was a regression (worked on previous devnet). Expect to continue with chain once resolved. 

Devnet-8: specs are out. https://notes.ethereum.org/@ethpandaops/dencun-devnet-8 Release date unknown.  

Devnet-9: no specs out but we will move to capella genesis.

**APIs for L2s.**  Had call to action around whether current beacon API is ok for layer 2 (especially get blobs).   Terence had asked Arbitrum for feedback. Suggested they would like to retrieve blobs using versioned hash, so created beacon hash issue to enable this. https://github.com/ethereum/beacon-APIs/issues/332

Not sure if this should be mandatory or optional for clients, but seems layer 2 teams should find it useful. If not implemented then you’d have to identify which block the tx made it into and you’d have to look it up that way.   Proto: block-id introduced in Feb works for Optimism as L2.  Ideally we can fetch it by something that can be identified by EL. Identification by slot, and then consistency checks of result, works. Additional endpoints would require indexing.    L2s currently follow L1 EL chain, not beacon chain.
When is L2 not aware of blocks tx made it into?   For Arbitrum only version hash is stored on chain, no block id, etc.    Additional comments please leave in the issue above.
Are arbitrum / optimism on our testnets or plan to join?  Arbitrum plans to join as soon as possible but waiting for things to stabilize a bit, e.g. devnet 8.  Should invite more teams to prototype as we get into the future devnets.   Optimism is looking to rebase prototype and join … just a matter of timing.

**Spec PR:** https://github.com/ethereum/execution-apis/pull/426 :  Helps to clarify some corner case around handling payloads v2.  Reorders some checks.  Defines order of validations for new payload / get payload methods to make it more clear in terms of testing & which errors codes we should expect in different situations connected to timestamp.  Expects v2 & v3 methods should decline requests when timestamp is not for correct fork.  Additionally if any additional fields are parsed / not parsed or contain null values it should be treated as invalid params.  This is purely clarifications, useful for hive tests. Would be good to have for next devnet.  Lucasz has approved. Will leave another day or two for eyes and then hopefully get it in.

Had time slated for CL gossip sub modifications that are under discussion.  Anton: Should disable flood/publish for blob topics. Unfortunately this is currently a global option. Another approach is to disable for messages larger than some threshold. Status of misc clients for supporting the flood/publish changes somewhat unknown. This is one of the single biggest things that might change success of these large messages. If a client or two don’t do it then it just affects the client in question, but would be best to have this across the board.

Staggered sending would also be good to have, an optimization we could enable later.

Should we have our own Libp2p version?  Would be best to work with libp2p and not have to fork, but if we run into issues it’s certainly an option.  Could also fork temporarily and merge upstream later if we are having timing issues. Would try to play in same environment if at all possible.

Replacing of blob transactions: do we have some consensus on max increases?   Are there rules on switching blob tx to non-blob tx?  Geth has 100% required bump for everything right now. Some older discussion around replacement was here: https://ethereum-magicians.org/t/eip-4844-shard-blob-transactions/8430/29?u=roberto-bayardo
Will try to bring up on ACDE with Peter.
