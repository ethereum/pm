# Fast Confirmation Rule 

**Summary:** 
The Fast Confirmation Rule is an algorithm that allows determining in 1-3 slots whether a block that has not been finalized yet will never be reorged out of the canonical chain, under good network conditions and an assumed ratio of dishonest stake. 
The Fast Confirmation Rule can be used to improve Ethereum UX by providing the users with a way to determine how "strong" the permanence of a block in the canonical chain is without having to wait > 13min for finalization. It can also be useful in the context of ePBS to provide builders with an indication of whether the parent of the block that they are building upon is unlikely to be reorged out, which can guide them in fine tuning their bids.


**Facilitator:** Roberto Saltini

**Note Taker:** TBD

**Pre-Reads:** 
- [Old ethresear.ch post](https://ethresear.ch/t/confirmation-rule-for-ethereum-pos/15454). A few things have changed since then, but most of the concepts introduced in this post are still relevant.
- [Paper](https://www.dropbox.com/scl/fi/qb356lkxzfljrunq2hu52/main-fc.pdf?rlkey=wsfkl4vtsp7bm4d31mynj17a5&dl=0)
- [Spec PR](https://github.com/ethereum/consensus-specs/pull/3339)
- If one has time, [long technical report](https://arxiv.org/abs/2405.00549)

**[Draft Slides](https://docs.google.com/presentation/d/1c15176RwptmmgTAZDpQUfoKUN339gOksENI_zburM6A/edit?usp=sharing)**

## Agenda 

- Interactive Presentation
    - How the Confirmation Rule algorithm works
    - Walk through of the [Spec PR](https://github.com/ethereum/consensus-specs/pull/3339) to go over some of the implementation details
- Open Discussion
    - Clarify possible concerns
    - Gather feedback and estimated implementation effort
    - Ideally, agree on rough implementation timelines

## Notes & Action Items

N/A 