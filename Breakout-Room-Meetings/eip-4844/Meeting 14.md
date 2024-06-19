# EIP-4844 Implementers' Call #14 

## Meeting Details
### [Agenda](https://github.com/ethereum/pm/issues/718)
### Date: Feb 7, 2023	
### [Video Link](https://youtu.be/vQGk9FDs_CM) 
## Notes: Orignally Documented [here](https://docs.google.com/document/d/15EatedrJanNxBZGPVASvwq9xgbTs5UxjsDfjpM6ppSY/edit#heading=h.tyz3rvf5q08q)

### Notes 

* [Introduce Deneb to remove EIP-4844 references beacon-APIs#289](https://github.com/ethereum/beacon-APIs/pull/289)
    * Clients should already have this implemented in order to participate on Devnet
    * Just about getting the spec updated, so we can work on top of it with other beacon API changes that will be necessary for block and blob decoupling
    * This PR just need a rubber stamp to merge
    * After that, can work to add the more information re: decoupling
        * For signatures
        * For validator behavior
        * Sean @ Lighthouse will implement today / early this week
* [Add API to retrieve blobs sidecar beacon-APIs#298](https://github.com/ethereum/beacon-APIs/pull/298)
    * Need to come to consensus, but not blocking interop (this is user facing)
    * Terence @ Prysm is going to follow up with this to merge
* [EIP-4844: Free the blobs consensus-specs#3244](https://github.com/ethereum/consensus-specs/pull/3244)
    * During interop week, there was rough consensus to decouple block and blob
    * Have been iterating on the design doc and are now moving from design doc to PR
    * Asking folks for review on the PR, so we can come to consensus
    * This is the biggest blocker before Devnet-5
    * Client teams will need 2-3 weeks to implement
        * Jesse: is this strictly necessary to do the decoupling work now?
        * Going to be easier to productionize decoupled design then start with a coupled design and then move to a decoupled design
        * Decoupled design is also more flexible, which helps us with the fact that it’s hard to gather information about what this looks like on mainnet
            * Hard to model what a dynamic and diverse network looks like when we’re making 
        * Answer: at the current blob sizes, could ship without this, but once we ship it, there will be more challenges in modifying it
    * Blob decoupling is a lot of consensus layer work and the SSZ is a lot of the execution layer work, so not generally overlapping
    * EF clients are working on the blob mempool - can use this time for decoupling
    * Tim: does anyone on the client teams feel strongly they shouldn’t decouple?
        * Roberto: If consensus teams are comfortable with it, we should be comfortable
    * Re: SSZ, will be some consensus layer changes
    * Discussion about verification of KZG proof with cryptography library
        * Have solved the changes on the KZG cryptography library side
        * Getting more data on the verification costs and whether we can move forward 
        * LIkely that we will be able to move forward
    * We won’t be able to do aggregated proof on the mempool
    * Likely that the difference between the two is very minor
    * Transaction pool discussion
        * Do we want to have a limitation on single blob per transaction?
        * Started here thinking about aggregated proofs for max one blob per transaction
        * Originally introduced aggregated proof technique just for the mempool to be faster
        * If we are switching to one blob per transaction on the mempool, we less likely need aggregated proof
        * Tim going to follow up with Geth on the transaction pool design
        * Given the number of blobs is smaller than the number of cores, should be able to be parallelized well with multithreading and doing on multiple cores
            * Shouldn’t be a part of the spec, but do think that if libraries can multithread something, they should
* Devnet-4 - how are clients tracking?
    * Besu
        * Now following devnet-4 chain correctly
        * Locally they are now able to build blocks without any blob transactions
        * Still having issues validating blob transactions that they are working on 
        * Should be the last issue before they can fully join devnet-4 as a supported client
    * Lighthouse
        * Just merged a fix for serving finalized blocks that have blob transactions
        * Previously couldn’t sync by a lighthouse node by range
    * Prysm
        * Working on decoupling, doing implementation
    * Nethermind
        * Good devnet-4 implementation
        * Just synchronized with lighthouse which was the last CL client we’re trying to synchronize
* Etan

