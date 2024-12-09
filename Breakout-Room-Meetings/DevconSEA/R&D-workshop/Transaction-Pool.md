# Future of the Transaction Pool

**Summary:** With the recent rise in MEV, private mempools, blob txs, AA, the role of the public mempool changes. In this session we discuss what the issues are and what we might be able to about it.

**Facilitator:** Marius

**Note Taker:** TBD, lemme know if you want to take notes!

**Pre-Reads:** 
- https://eips.ethereum.org/EIPS/eip-7702#backwards-compatibility
- https://github.com/erigontech/erigon/wiki/Transaction-Pool-Design
- https://hackmd.io/@s_Mu6_nBRDOLzvR4GG5tjw/BkF08Wjc2
- https://notes.ethereum.org/wcg_u2qORiqpyZ7KbPjRAA?view#Vertically-sharded-mempool
- https://www.notion.so/probelab/Probelab-s-Shared-Blob-Mempool-Proposal-Draft-Shared-135eaf461d47804e8e04d36d3c443dd2

**[*Optional*] Slides:** TBD 

## Agenda 

With 4844 and the blob increases in the future, we need to scale the transaction pool and thus the DA layer significantly. In this session we will go over some of the issues with the transaction pool today and discuss some proposals on how to improve it.

- Transaction pool today
- 7702 ready transaction pool designs
- Blob transaction increase
- Sharded mempool designs and blob tickets
- Shared mempool design
- Transaction pools in a stateless world

## Notes & Action Items 

### Future of the tx pool

- currently in geth there's a tx mempool and a blob mempool
  - for an account, it only allows one tx across both pools
- whether to treat 7702 txs (delegate txs) as separate txs and a separate mempool
- someone else can pay the gas for the 7702 gas tx delegation

#### blob transaction increase
- limit the number of blobs per transaction
  - easier to pack e.g. if max is 4, can more easily fill up a block
    - e.g. 17 blobs in a tx will make it hard to fit other blob txs in a block of max 30 blobs
- Arbitrum has expensive validation at execution, would want to have more blobs per tx (to reduce evm overheads)

#### sharded mempool design
- not great automated testing for tx mempool
- sampling blob shards is deep research
  - DAS into the mempool
  - area of active research
- dos resistance
  - not clear
- vertical sharding is easier but less good long term

#### shared mempool design
- research area
- use dht instead of gossiping
- change the way we propagate blob transactions

#### tx pools in a stateless world

- static chacks
  - validating sig and blob hashes are expensive
- stateful checks
  - nonce too high/low
  - balance check
  - 7702: does it interfere with other txs
- portal network has a sharded tx pool design
  - distributed store of the state
  - loose design
  - overlay tx pool on top of this, mapping tx to sender
  - a stateless node holds onto part of the account state, and can do the stateful validation for txs associated with their accounts
  - block builders run nodes all over the dht to have a global view of the tx
  - lots of denial of service vectors to think about, especially with passing around validity proofs
  - doesn't think about 7702
- need epbs to solve stateless pools?
- sender to repeatedly provide state proofs

#### general discussion

attackers: a builder emptying a mempool of another builder
- deliberately trying to churn the tx pool?
talking about a bounty incentive to help get more visibility
- but need to first build the tx pool
- bug bounty 2mil payout for geth
- about making all the client teams aware of the issues of 7702
- how do other EL clients handle blob txs?
  - erigon drops blob txs and doesn't resurrect?
  - do clients have different churn costs?
  - not clearly consistent across EL clients
  - not currently much load on mainnet, so any issues are not pronounced
- also this doesn't think about private mempools
  - issues with private order flow
- how does EPBS affect this?
  - blob propagation
  - submit a block, arrives to node in 2s, have 2-4s to check for data availability
  - epbs - see block after 2s, have 3s into the *next slot* to validate the block
  - epbs doesn't change EL or mempool in any way
- for inclusion lists, they need to be about txs that are in the mempool
- whether to allow stacking txs on top of eachother (multiple pending txs per account)
  - not necessarily a guarantee
  - it can break Arbitrum sequencer
  - mitigation to only stack until there's no funds left?
  - only keep track of txs that are immediately includeable?
- tx pool is where vals should push the txs to force include them
  - inclusion list design space is still open
  - potentially a problem if it can't be included due to small changes to base fee
- heuristic to detecting a censoring block builder
  - on reorg, if you see a tx being reorged out but it could have been included
  - if there was space in the block and the builder did not include it, paid enough + 1559
- what about private mempools invalidating the public one?
- no specification of the tx pool
  - want clients to figure out for themselves
    - good for client diversity
  - increasing complexity could mean it's worth having recommendations or test cases

