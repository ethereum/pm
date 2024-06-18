# EIP-4844 Implementers' Call #17 #732

## Meeting Details
### [Agenda](https://github.com/ethereum/pm/issues/732)
### Date: Mar 7, 2023	
### [Video Link]( https://youtu.be/8hDlg-x6MjE) 
## Notes: Orignally Documented [here](https://docs.google.com/document/d/15EatedrJanNxBZGPVASvwq9xgbTs5UxjsDfjpM6ppSY/edit#heading=h.7ln6lr3j4ti6)

### Notes 
* Spec updates
    * Decoupled blobs
        * Gajinder - what is the exact signing flow?
            * We introduced the blindness flow and realized it has the nice side effect of not sending beacon traffic
            * Plan is to continue the conversation [on the PR directly](https://github.com/ethereum/beacon-APIs/pull/302)
            * This problem doesn’t really exist if you are outsourcing the builder - only exists in a fallback scenario
            * Since people are using an outsourced builder, and long term if we have PBS, maybe this is less of an issue to go with this by default
            * If we’re only signing blinded blobs, we might want to update the consensus spec because it still says we’re still signing the whole sidecar
                * Danny: don’t think it’s necessary to include this bc the spec doesn’t know these details today
            * Having the them combined if we go to the blinded simplifies the handling of the decoupling PR
            * Trying to get this done for final discussion on Thursday or merge before Thursday
        * Danny - local heuristics on when you start requesting this new information
            * When you get the block, do you immediately request or wait some portion of the slot until you request, etc
            * Design decision around which heuristics you use to do when
            * No right answer, but something for people to be considering - main other point of uncertainty
            * Terence: not a blocker for the next devnet, will take us a while to figure out when to request and when to wait
            * **For initial version, wait patiently for gossip and hope we get it, if we don’t get it request at 2s market**
            * This isn’t something that would make it into the spec - local design decision
        * PR that [aggregates to proofs](https://github.com/ethereum/EIPs/pull/6610/files) - need a review
        * Crypto library
            * All of the bindings support the new KZG interface - in the process of polishing all bindings
            * We have an audit in a month, so planning to make final changes in next two weeks, then freeze entire codebase
            * Things are moving smoothly
    * SSZ
        * Complexity of SSZ EIPs is still growing and not finished yet
        * Wouldn’t want to make a change to transaction type, unless we agree to SSZ before
        * Should assume that 4844 is moving forward independently, then if we agree to do SSZ, we can update 4844
        * Trying to couple / keep both efforts in sync is the highest overhead and least valuable thing
        * Decision: keep them decoupled for now, if we decide to couple them, deal with it at that point
    * Transaction pool
        * Ideas we discussed last time were in ETH Magicians thread - going to assume that means they are not controversial and we can go ahead and add them
        * Nothing on the geth side
        * Goal is to get all on the same page on transaction minimalism by next week ACDEs
    * Client updates
        * Prysm
            * Shanghai is priority
            * Terence is implementing free the blobs and then will launch a Prysm only devnet, then we will be ready to launch a multi-client testnet
        * Lighthouse
            * Have a few people working on 4844 even while we’re doing Capella
            * Still have work to do on the implementation before we have someting working
            * Over the next month, working on a local devnet, then focus on interop
        * Nimbus
            * Henri is continuing to work on 4844 and has been making progress on the decoupled blobs implementation - coming along
            * All leads to a much nicer implementation as a side benefit
            * Targeting pairing up with other clients sometime this month
        * Teku
            * Already started the decoupling PR
            * Not currently at full speed, but planning to get back to full speed soon
            * Makes sense to have something by end of month to start playing with other clients
        * Lodestar
            * Likely to be ready for a devnet at the end of this week
        * Geth
            * Working on getting a tool for SSZ - lot of other stuff going on
            * Want to have more specialized transaction types
            * Not sure if people agree with the assumption that transaction types should be getting more specialized
        * Nethermind
            * Haven’t started work on the transaction pool yet
    * Cadence
        * Should we switch to bi-weekly for the next while?
        * Two weeks from today, we can meet together and check where the implementations are at / decide if we want to move to a multiclient devnet
        * Decision: moving to bi-weekly
