# EIP-4844 Implementers' Call #18

## Meeting Details
### [Agenda](https://github.com/ethereum/pm/issues/739)
### Date: Mar 20, 2023	
### [Video Link](https://youtu.be/gdy5svsnFrM) 
## Notes: Orignally Documented [here](https://docs.google.com/document/d/15EatedrJanNxBZGPVASvwq9xgbTs5UxjsDfjpM6ppSY/edit#heading=h.cj7cnyhygaz0)

### Notes 
* Stuff to discuss: Spec stuff, fee market, where teams are at.
* SSZ: From ACD seems unlikely to have SSZ migration alongside 4844 in cancun, so probably makes sense to split those up. That said we are introducing SSZ into 4844 so we still have the question of which format to use. Optimize for storage size of tx or for proof verification of transactions?  These result in different encodings. Did not reach agreement on ACD, but that’s roughly where things are at. Would like whatever we do be forward-compatible with the broader roadmap.
    * Does changing the ssz layout involve a lot of work if we change it in a month? Probably not, biggest change would be if we require merkelization in EL as the current spec doesn’t require it. 
    * Let’s leave the tx type as specified for now, we can make the change after we have broader SSZ consensus.
    * https://eips.ethereum.org/EIPS/eip-4844#new-transaction-type
* Fee market analysis: https://ethresear.ch/t/eip-4844-fee-market-analysis/15078
    * Good post, and something we will want to get right as early as possible. Terence Summary: Given the spec today, it would take 1 - 1.5 years for usage to reach the target to reach threshold. Even without that we would want to deter spamming, so do we want to raise the min price?  Post assumes gas is inelastic but would argue it’s more elastic than indicated.
    * Re: pricing what to do when more blobs than space in block: Mofi: The priority fee from 1559 serves the same purpose.
    * Proto: Strong statement that blocks won’t be full. Today the only reason they use as much as they do is they are already maxing out gas in ethereum. Rollups are paying well over 90% of fees towards data already, so we know users are ready to pay a premium for data.  No reason to think that those fees wouldn’t go towards using all those resources.  Will be unstable for a week or longer, but not >1 year.  Prefer not biasing fee markets too much with things like minimums..   Tim: Wonder if there’s a way to figure out true economic cost of this data.  But this is hard since we don’t control eth/usd minimum exchange rate.
    * Is there any strong opinions on whether there should be a higher minimum?  Proto: I think a higher one is fine if it’s well justified and accounts for costs.  But even if there is a spike in throughput it will pay for it in price adjustments. If consistently below target, sure blobs are cheap but it’s within our ability to handle it and in 18 days it’s gone again.
    * From the chat comments, Mofi noted that Ansgar had a strong view that there should be no minimum because users shouldn’t have to pay for data gas that the network “already has”.
    * Jesse: Are we worried we’ll be either at the minimum or hit the max, e.g. the 1559 rules might not work?  Proto: curve will adjust to the blob throughput. The adjustment doesn’t account for removal of blobs but if you look beyond 18 days it is just a small change in price due to excess blocks.  This discussion has been had before in original EIP that changed it from base fee like mechanism.
    * Tim: Most worrisome thing the post is if it goes for >1 year at min price.
    * Proto: Another thing to think of is the Shanghai DoS attacks; there is this persistent problem with syncing because of it. But because blobs are pruned after 18 days there’s no more obligation to ethereum today.  It’s a very different long term cost than regular gas usage.
    * Saulius: We might be worried someone will spam at full capacity of what the network will handle.  But personally don’t see how there would be too much damage from fees too low. Network will adjust.
    * Tim/Roberto: Based on discussion no need to take any action on min fee for now, but let’s continue discussion on the fee market analysis post. Please add your thoughts there.
* Client dev progress
    * Terence: Still running tests on decoupling blocks and blobs.  But majority of resources are still in Shapella right now. In one week we’ll have more resources, multi-client testnet for 4844 might be ready in 2 weeks from now. 
    * Lodestar: Ready in the sense that without including changes in blob signing endpoints. We are independently fetching & signing the blobs.  So ready for multiclient devnet.
    * Lighthouse: Made a lot of progress on decoupling but still don’t have something fully workable. Our goal is to get that ready this week, something that is ready for testing locally.
    * Nethermind: Have something ready that can work with lodestar
    * C-KZG work has gone well, asking client teams to finalize code before April 5.
    * Teku: Are not yet full speed on 4844, but we are progressing a bit. Will get back to full speed this week. 
    * Tim: Should we prioritize a longerlived devnet?  Maybe that ends up serving for a Cancun devnet where we can potentially add other stuff.

See everyone in 2 weeks!
