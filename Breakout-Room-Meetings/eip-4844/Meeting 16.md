# EIP-4844 Implementers' Call #16 

## Meeting Details
### [Agenda](https://github.com/ethereum/pm/issues/726)
### Date: Feb 21, 2023	
### [Video Link](https://youtu.be/hWcpSlwNTBU) 
## Notes: Orignally Documented [here](https://docs.google.com/document/d/15EatedrJanNxBZGPVASvwq9xgbTs5UxjsDfjpM6ppSY/edit#heading=h.ngbel4ohs4ye)

### Notes 

* Spec updates
    * [New CL spec release](https://github.com/ethereum/consensus-specs/releases/tag/v1.3.0-rc.3)
        * Primary inclusion is the free the blobs change (go Jasik)
        * Some cryptography modifications 
        * Breaking change: excess data gas field is moved to end of transaction data
        * Spec tests are out, so anyone can test it
        * Beacon APIs need an update for signing blobs
            * [Active PR](https://github.com/ethereum/beacon-APIs/pull/302) that will be discussed on Thursday
        * Jesse: how are you feeling about spec?
            * On consensus layer, feeling good
            * Only big question is whether we need to change the engine APIs to handle the mempool stuff
                * Danny is a strong “no” on this
    * [KZG library refactor](https://github.com/ethereum/c-kzg-4844/pull/123)
        * Moves library to doing isolated proofs rather than aggregated proofs
        * Now we can verify blobs with individual proofs OR batch verify blobs with slightly faster verification
        * After merging the spec, we started working on this on the implementation
        * Base code of c-kzg now implements the new spec
        * Python, Golang, and Java bindings updates
        * Still work to be done on C#, Nodejs, and Rust bindings
        * In particular, there is work that needs to be done on the Nodejs side for c-kzg
        * Terence: are there spec tests for these bindings?
            * Want to implement tests for each functions
            * Likely going to have them in the spec tests
            * George agrees that doing this in spec tests would be nice but py-acc will be very slow, so need a new library for BST
            * Can’t use Milagro because it doesn’t have the group functions
            * Kev is working on getting an API for arkworks and then we’ll have it
        * Jesse: Dan is transitioning out so need someone to maintain bindings
            * Dapplion from Lodestar is looking into it and will likely be able to take care of it
    * Zero blob
        * Ansgar going to land PR on EIP in time for ACDC on Thursday
        * Ongoing discussion in the Etheruem Magicians thread [here](https://ethereum-magicians.org/t/eip-4844-shard-blob-transactions/8430/28?u=true&=true)
        * Tim’s feeling is makes sense to apply the restrictions Roberto suggested 
            * Replace only w/ equal or > # of blobs, plus data gas & regular gas bump.
            * Blob-holding txs should only be replaced by blob txs consuming at least as much datagas
            * There can only be one blob-containing tx per account. 
        * Roberto: feels like we need to make this somewhat formal to make progress
    * Client updates
        * Prysm
            * Focused on implementing the free the blobs PR - pretty significant change
        * Lighthouse
            * Working on the free the blobs PR, same as Prysm - considerable change
            * Two weeks seems OK, but wouldn’t promise it
        * Teku
            * Started working on the decoupling - don’t have a timeline yet
        * Lodestar
            * Has also started working on decoupling as well
            * Will handle the node bindings now that the implementation is complete
        * EthereumJS
            * No major updates
            * Merged branch and synced devnet-4
            * Hoping to work more on rust-kzg and implementation over the next couple weeks
        * Nethermind
            * Still on devnet-4, no major updates
            * Plan to update KZG bindings
