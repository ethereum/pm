--
title: EIP-4844 Transaction Pool Considerations
source: https://hackmd.io/aVek93y-QmSv1mz2Agc9iQ
archived_date: 2024-01-17
author: Roberto Bayardo
date: 2023-07-23
---

# EIP-4844 Transaction Pool Considerations

[Original Document](https://hackmd.io/aVek93y-QmSv1mz2Agc9iQ)

In the last 4844 client devs sync it appeared teams were implementing different strategies for managing blob transactions in the transaction pool, or had not yet implemented any specialized strategies for blob transactions. This doc outlines some of the strategies that have been proposed in an attempt to drive some consistency among client implementations. The two areas in particular where it seems we lack consensus are transaction replacement rules for blob carrying transactions, and how to handle reorgs of blocks containing blob carrying transactions. Note that there is no requirement that implementations behave identically in these functions, but some consistency should allow for more predictable behavior and hence improved user experience.

# Transaction Replacement

A general concern around blob carrying transactions is that they are expensive both in bandwidth to propagate and in CPU for blob validation, providing new surface areas for potential denial of service attacks. One way transaction pools mitigate DoS concerns is through transaction replacement rules.  The requirement for replacing a regular Ethereum transaction is at least a 10% bump in max-fee-per-gas and max-priority-fee-per-gas.  Blob transactions involve not just regular gas but also data gas.  What should the replacement rule be for blob transactions?

**Option 1**: Treat them the same as regular transactions: min 10% increase in max-fee-per-gas and max-priority-fee-per-gas

**Option 2**: Require additionally a min 10% increase in max-fee-per-data-gas.

**Option 3**: Require a dramatically higher increase in the 3 fee values than 10% (say, 100%).

Option 3 perhaps best captures the fact that blob transactions are more expensive to process than regular transactions. One concern however is that due to 1559-style pricing, increases in max-fee-per-gas and max-priority-fee-per-gas don't necessarily incur more cost on the transaction submitter. Only max-prioriy-fee-per-gas is subject to "actual price" rules.

Suppose someone wants to DoS a node through resubmitting a blob transaction. They could start with a priority fee of 1 wei and resubmit the transaction repeatedly, bumping fees the minimum required amount each time.  At 100% minimum increase, the attacker could resubmit 33 times and pay only about 10 gwei max-priority-fee-per-gas. A 10% increase allows for ~240 resubmissions for the same cost.

Under option 1, the attacker could always keep min data fee much too low to allow for block inclusion, allowing the attack to continue almost indefinitely, and potentially without ever incurring any cost should the transaction eventually just expire from the mempool.

Requiring a bump in max-fee-per-data-gas seems important, but our attacker might still be able to avoid any data-gas fees at all by submitting a non-blob carrying replacement transaction just before the blob transaction might get included in a block. We might therefore impose an additional replacement criteria:

**Extra requirement #1**: Do not allow a blob carrying tx to be replaced by a non-blob carrying transaction.

There are more strict versions of the above extra requirement we might also consider, such as do not allow a transaction carrying N blobs to be replaced with a transaction containing less than N blobs. Taken to the extreme, we might also forbid a blob carrying transaction to be replaced by any other transaction unless it contained the exact same blob payload. This would mean the txpool wouldn't ever have to perform blob payload validation for replacement transactions, greatly reducing DoS attack surface.

Another potential DoS attack might involve an attacker who repeatedly submits a blob transaction, each with low max fee and max data fee, though bumping the nonce each time. Before the transactions could be eligible for block inclusion, the attacker could then submit a replacement for the first submitted transaction that invalidates all others, incurring only the cost of the final replacement transaction. None of the above options seem to offer much protection against this kind of attack, suggesting we might implement another requirement:

**Extra Requirement #2:** do not allow more than one blob-carrying transaction per account in the mempool.

# Blob Transactions and Reorgs

Most transaction pools will re-inject transactions that are reorganized out of earlier blocks, even though it is not mandatory that they do so.  This greatly reduces the need for users to monitor and possibly resubmit transactions that have entirely adequate fee settings for inclusion. 

In the case of blob transactions, implementing reinjection is more complicated since the execution layer does not hold onto blobs, only the blob hashes. In order to support reinjection of blob transactions, the transaction pool would have to cache blobs of recently seen blob transactions even after they were included in a block.  An open question then is the following:

**Open question**: Should transaction pool implementations be expected to cache blobs for some duration of time, or some number of blocks in order to support rebroadcasting?

The challenge here is this requirement again increases the DoS surface area.

We expect users of blob carrying transactions to be more sophisticated than most (e.g. layer 2 batch submitters). These systems could take advantage of specialized block builders that provide appropriate guarantees, so it's unclear if reinjecting should be expected of all/most transaction pools on the network. Nevertheless it seems desirable that most transaction pools at least try to rebroadcast blob transactions on a best effort basis, for example by at least maintaining a bounded size cache of blobs from recently included blob transactions.

# Client Implementations

TODO: for each client, describe how each currently handles blob transactions.

**geth:**

Geth's logic & rationale behind it are detailed here: https://github.com/ethereum/go-ethereum/pull/26940

* 100% min increase in max-fee-per-gas, max-priority-fee-per-gas, max-fee-per-data-gas.
* The minimum priority fee is 1 gwei
* A replacement blob tx cannot evict already pending ones with overdrafts
* Normal and blob txs are mutually exclusive (across the entire nonce range). If on type is pooled, the other is rejected until the pool empties. I.e. you cannot replace a blob tx with a non-blob one.
* Included blob txs are kept in limbo until finality to support resurrecting back into the pool on reorgs

**erigon:**

**nethermind:**

**besu:**

**nimbus-el:**

**eth-js:** 