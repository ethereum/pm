# EIP-4844 Implementers' Call #20 

## Meeting Details
### [Agenda](https://github.com/ethereum/pm/issues/755)
### Date: Apr 17, 2023	
### [Video Link](https://youtu.be/oCqfxb5CWAI) 
## Notes: Orignally Documented [here](https://docs.google.com/document/d/15EatedrJanNxBZGPVASvwq9xgbTs5UxjsDfjpM6ppSY/edit#heading=h.h6sis7kl7ys4)


### Notes 

* Spec updates:
    * Small one-value change by Mikhail in error code fixing small discrepancy: https://github.com/ethereum/execution-apis/pull/399/files
    * getPayloadV3 & getBlobsBundleV1 merge.  Mikhail: these were introduced separately because easier to prototype, but since we’re heading towards spacing out engine API changes for cancun this is one of the outstanding questions to resolve, & question was raised in discord recently. This is basically same process as obtaining payload & blobs, and at first glance it seems there’s no need to keep separate (get payload can return both).  If we merge we would have to more extensively test, so not clear if it’s in scope for devnet.    Gajinder: don’t see need to keep separate. (Nobody advocating to keep them separate).  Tim: my preference is to not include it in next devnet but have PR open for it to do multiclient testing.  Roberto: that might work against having devnet be persistent.  Tim/Gajinder: we might have better chance of next devnet being persistent.
        * Tentatively in scope for devnet 5 (though need more feedback from CL devs, not many are on call today)
    * Gajinder has 3 PRs to highlight 
        * https://github.com/ethereum/execution-apis/pull/392 add proofs to transaction wrapper. 
            * Mofi: Had something like this before free the blobs where proofs generated on CL side, but got rid of it to minimize time for block building.  Is this still a concern / would it lengthen time to build the blocks?   Gajinder: Proofs are coming through tx wrapper and come in the serialized tx so no need to compute on the EL side.  Mofi: Main issue before was aggregated proof computation which is no more. Flcl42: do we still need to verify proofs on execution layer side or can we just send to CL to spend less time on tx verification?   Gajinder: since EL broadcasts better to have checks on EL side. 
            * Mofi: Adding proofs is required to decouple the blobs so we should make this change for devnet v5.  
            * Should add for devnet 5.
        * https://github.com/ethereum/EIPs/pull/6610
            * Updates to remove aggregated proof & other minor updates, already implemented in geth.   In scope for devnet 5.
        * https://github.com/ethereum/beacon-APIs/pull/302  Extend current endpoints to prove & publish
            * Extrends produce/publish APi endpoints to use block contents rather than the block. It is sort of an optional thing for devnet 5 to push the implementation forward.  Optional communication between beacon node & validator. (Lodestar has implemented it, Teku started implementing it. )
            * Optional for devnet 5.
    * These are in scope for devnet 5, but not yet implemented in geth, should be easy to add.
 

    Tim: Should we then just merge getpayloadv3/blobsbundlev1?  Gajinder: change on the CL side is not a big deal I am OK with doing merge before V5.  EL side would be caching all the data anyway so could return the full content in getPayloadV3.  Any other CL client thoughts?   Terence is not on the call but we should ping him. 

* Devnet 5:
    * https://hackmd.io/@inphi/HJZo4vQGn
    * Nimbus: have sync working, finishing up gossip. Last PR probably going out today/tomorrow and then some tying up loose ends. Guessing 1-2 weeks.
    * Lighthouse: 
    * Nethermind: 2 weeks timeframe hopefully. Join after devnet 5 launch.
    * Ethereumjs should be able to join in
    * Besu needs a week or so to be in part for devnet 4.
    * Tim: Stand up by CL call?
        * Mofi: Probably not, next monday or tuesday would be a better date.
        * Tim: Blockers to figure out this week or is it just implementing? 
        * Mofi: It’s implementing and availability of devs here to do the interop.
        * Tim: In that case let’s check in on this in the CL call and aim for early next week going live.
    * Let’s keep 4844 devs only call for 2 weeks, will discuss whether to shut down devnet5 and go to devnet6

* Testing:
    * Lukasz	: Question about testing, are there hive tests? 
    * Mario: Working on them, for engine API we still have to work on it.  PRobably next week we’ll have something to test changes on hive.
 

* Mempool:  
    * We have been punting on making a decision on rebuilding blob txs on reorg. Danny: wanted to make sure we haven’t dropped this.
    * 
    * Peter would like to have quality of service so that blob txs could be put back in mempool upon reorg, same as normal txs. To make that happen you have to break barrier between EL/CL a bit more, new payload would have to have access to rebuild full transactions.  Danny/Peter spoke about this and if you bypass mempool you don’t have blobs available to rebuild the txs. This does seem like an unknown point around whether there is a change here that should happen.  Don’t have discussion points beyond that.
    * Peter’s solution was to implement blobs via newpayload
    * But, could we instead guarantee only that all blob txs that hit the mempool should be rebuilt? EL can choose to rebuild those txs since it can cache the blobs.   Danny: Do think this is a very reasonable quality of service, especially if you think about full sharding design.
    * Once you put it in new payload can rebuild if you feel like it, but have broken abstraction a bit.
    * **We should loop in Peter / geth team & see if he feels strongly one way or the other.  We can potentially cover this on the CL call, especially in the case if the opinion is we should change this.**
    * Mikhail: Probably CL can do something about it since it keeps blobs anyway, and could fill the gaps.  Not sure what the edge cases / complexity of that will be.  Danny: Worry that makes too much of a stateful assumption between layers.  E.g. if you come online during the reorg you won’t have the blobs. 
    * Danny: my opinion is rebuild only if in mempool is simplest and doesn’t make new assumptions required for full sharding.
 
