Gav Wood edited this page on Nov 25, 2015

The fields in the header currently have no sensible ordering, having been arrived at primarily through arbitrary historical evolution. This EIP aims to reorganise them to maximise clarity and reuse of the header format even for derivative blockchains that do not use the full consensus algorithm.

Furthermore, extra data is increased to be of arbitrary length (but conforms to gas costs) and placed in a separate, 4th, portion of the block. Only the hash is stored in the header.

# New Order

#### Section 1: Block meta-data
- `parentHash`: The hash of the parent block's header.
- `timestamp`: The timestamp (Unix time) of the current block.
- `number`: The number of the current block.
- `author`: The account responsible for authoring the current block (the rewarded account in a PoW chain, a more general name for _coinbase_).

#### Section 2: Data references
- `transactionsRoot`: The root hash of the transactions trie.
- `unclesHash`: The hash of the uncles segment of the block.
- `extraDataHash`: The hash of the extradata segment of the block.

#### Section 3: Transaction execution information
- `stateRoot`: The root hash of the final state after executing this block.
- `receiptsRoot`: The root hash of the receipts trie corresponding to the transactions.
- `logBloom`: The accumulated bloom filter for each of the transactions' receipts' blooms.
- `gasUsed`: The amount of gas used through each of the transactions.
- `gasLimit`: The maximum amount of gas that this block may utilise.

#### Section 4: Consensus-subsystem information
- `difficulty`: The difficulty limit for this block.
- `nonce`: The nonce for the PoW of this block.
- `mixHash`: The mix hash for the PoW of this block.

The block header format `BlockHeader` is:

```
[parentHash, timestamp, number, author, transactionsRoot, unclesHash, extraDataHash, stateRoot, receiptsRoot, logBloom, gasUsed, gasLimit, difficulty, nonce, mixHash]
```

# New Block

The new block format is:

```
[ BlockHeader, TransactionsList, UnclesList, extraData ]
```

`extraData` is assumed to be pure data, charged at the same amount of gas as that of transactions' data.
