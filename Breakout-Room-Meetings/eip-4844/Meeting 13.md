

# EIP-4844 Implementers' Call #13 

## Meeting Details
### [Agenda](https://github.com/ethereum/pm/issues/716)
### Date: Jan 31, 2023	
### [Video Link](https://youtu.be/O1LLyKIMHUM) 
## Notes: Orignally Documented [here](https://docs.google.com/document/d/15EatedrJanNxBZGPVASvwq9xgbTs5UxjsDfjpM6ppSY/edit#heading=h.yo0u0frgagsa)

### Notes 

* Updates from interop
    * Had participation from every client except for Nimbus
    * Client interop with all sorts of combinations
    * Did some spamming of the devnet as an appetizer 🙂
    * Lighthouse had a couple sync related bugs that they made fixes to
    * Besu is connected externally to Devnet and are progressing
        * Have some problems with some blocks that they are addressing and hope to fully join the devnet in the next few days
    * Teku joined on the very last day and are following the chain correctly, but they were accidentally deleting the blobs that were being finalized (now fixed)
    * Nethermind is still working to sync with lighthouse as their primary priority
* KZG Ceremony Output format for clients
    * Hex-encoded with newlines
    * Believe this is the same format that c-kzg already uses
* KZG Libraries status update
    * Decision: Changing APIs so that clients just pass in bytes and the KZG library takes care of everything
    * Decision: switching go-kzg to use Gnark backend for the library, given Gnark has been audited 
    * Have some audits coming up, so going to gradually slow down the pace of changes
* [Transaction Pool updates](https://gist.github.com/karalabe/e1c4e4c2a226926498cc9816d383cecb)
    * A number of open questions and it would be good to have this ironed out AND have some tests that implement attack vectors to ensure we have some levle of compatibility
    * Agreed that the transaction pool will not contain zero blob transactions but not for it to be a consensus pool change
    * Should we bring up the issue of zero blob transactions on ACDE?
        * Yes
    * Discuss on ACD - what is the right way to test this?
* adding dataGasConsumed to the tx receipt format
    * Perspective is that we should return this as part of the receipt, but not planning to change the consensus objects
    * Open a PR on the json-rpc spec
* Blob/block sync decoupling
    * Terrence reviewed and left some comments
    * Yasick will come back to it soon
    * This affects the cryptography layer quite a bit - have we decided we’re fully going for this?
    * Decision: reached consensus at Interop
    * Dankrad / Roberto
        * Both feel like this is somewhat unnecessary
        * Will only provide incremental gains 
        * All based on people’s intuitions
    * Decision: we should talk about this on the call on Thursday
    * Could have intermediate solution where the proposer would sign the fragments of the blobs, which wouldn’t require us to change the cryptography
        * Dankrad: if we do this chang, we might as well change the cryptography so we get a bunch of nice cryptography things
    * Even if we do change the crypto, not going to make the crypto more complicated
* Bandwidth/networking considerations
    * No real input here
* Multiclient Sync
    * Lighthouse was trying to sync with Teku but they had an issues there; Lighthouse seems to be ratelimiting Prysm - seanis still trying to dig in there
* Blob Transaction hashing
    * There is a broader conversation going on around moving the EL over to SSZ entirely - some discussions and proposals that have popped up on the discord
    * Proposal are around moving all the transactions within a block
    * https://notes.ethereum.org/@vbuterin/transaction_ssz_refactoring
* Devnet transaction spamming
* Breaking Spec changes & devnet 5
    * Goal is to get breaking spec changes in over the next two weeks (before mid-Feb)
    * Then aim to get a devnet-5 two weeks after that
* Client & testing updates
