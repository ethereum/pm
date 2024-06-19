# EIP-4844 Implementers' Call #15 #722

## Meeting Details
### [Agenda](https://github.com/ethereum/pm/issues/722)
### Date: Feb 14, 2023	
### [Video Link](https://youtu.be/poTKRryqrzU) 
## Notes: Orignally Documented [here](https://docs.google.com/document/d/15EatedrJanNxBZGPVASvwq9xgbTs5UxjsDfjpM6ppSY/edit#heading=h.451zbopl8rnb)

### Notes 
* 
* Spec updates
    * [EIP-4844: Free the blobs consensus-specs#3244](https://github.com/ethereum/consensus-specs/pull/3244)
        * Network tests looked really good
        * Goal is to have this fully done by Thursday so we can get any final notes on ACDE
        * Plan is to ship this in the consensus-specs release on Friday
        * Going to flag on the ACDE to let folks know and “ask for any problems”
        * Basically exactly on the schedule set on interop
        * Do any clients have this implemented?
            * Prysm started, but stopped as final tweaks were getting done
            * Terence is going to pick it up this week again
        * Going to do another old vs. new simulation with additional framework
    * 0-blob transactions and how it relates to [ETH68](https://ethereum-magicians.org/t/eip-5793-eth-68-add-transaction-type-to-tx-announcement/11364/2)
        * Right now, when we use a type 4 transaction, we always require it to have a blob when it enters the mempool, but don’t require this in consensus
        * Should we add the number of blobs to the announcement
            * Not sure we need to include the transaction type - only needed for ETH66
            * May be able to include just the number of blobs
        * Lukas: don’t like having the number of blobs because it’s now starting to leak out everywhere - could we instead use size?
            * Mofi: point of using size was brought up at Bogota and decision to use the transaction type was because the cost of verifying the transactions could be incorporated (not just the size). For instance, if you have a large transaction that wasn’t a blob, then you’d you wouldn’t know this.
            * Tim: does anyone see an issue with using size instead of type or data gas?
            * Dankrad: geth won’t broadcast transactions over a certain size 
                * Dankrad: set rule to be don’t broadcast transactions >128kb
            * Marius: we should disallow 0 blob transactions
                * Enables us to have much better structure in the code
                * Don’t have all these types that do the same things
                * Dankrad: does this still exist if we also want SSZ transactions?
                    * Dankrad pushes for filtering transactions based on size vs. by the type
    * Observation: transaction pool and transaction types are hard to get everyone on the same page about
    * Recommendation from Tim: fully ban zero blob transactions
        * Proto: for adding it as a tx-pool only rule,
        * Marius: supportive, but wants it as a consensus rule if we have the restriction
    * Decision: Adding this to ACDE agenda
        * If you disallow zero blob transactions, do we do that
            * In TX Pool
            * In consensus
        * If you do allow them, how you discriminate between 0 blob and 1+ blob transactions in mempool, validation, broadcasting, etc
    * [SSZ List[T, 1] / Optional for Address: Update EIP-4844: Use SSZ Optional for Address EIPs#6495](https://github.com/ethereum/EIPs/pull/6495)
        * SSZ unions are not standardized right now / unclear whether they will be
        * Proposal from Etan is to replace the union with a list or optional type
        * This avoids introducing the union discussion and getting blocked on that
        * Dankrad: pushing back on the whether union is not standardized right now
        * Sean: in favor of justing using what’s in the SSZ spec, seems as likely to change as doing something else and is already implemented
        * Decision: discuss on PR and make a final decision next week
    * 16 million blobs capacity: Would like to understand the design space
        * Dankrad: for serialization, doesn’t matter, only matters for merkle proof
        * Etan: theoretical limit is very unlikely to be met
        * Decision: Dankrad going to tune this to an upper limit
    * [HTR based signatures: 4844: use hash_tree_root for tx hash EIPs#6385(https://github.com/ethereum/EIPs/pull/6385)
        * Right now, we are using keccack of transaction that is being signed for hash 
        * Mostly a discussion for SSZ tomorrow
        * Goal is to optimize the tranasction to be a part of the SSZ transaction tree
    * [Add blob signing endpoints #302](https://github.com/ethereum/beacon-APIs/pull/302)
        * Adds core components to engine API
        * Generally looking for feedback and would love folks to take a look
* Client progress
    * Besu
        * We are now feature complete
        * Asking to join devnet-4 testnet
    * Lighthouse
        * Working on decoupling
    * Prysm
        * Working on decoupling and making their DBs more reasonable
    * Teku
        * Released the new image on Friday for devnet-4 with some fixes around sync and blob handling on DB
        * So far so good, synced from genesis
        * Starting to work on decoupling
    * Nethermind
        * Waiting for the SSZ discussion tomorrow
