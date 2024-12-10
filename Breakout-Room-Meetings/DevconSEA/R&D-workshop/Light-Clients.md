# Verifying light clients / SSZ

**Summary:** Adding correctness proofs to transaction details, receipts, and historical logs, so that wallets no longer have to rely on a trusted centralized data provider and can improve security and privacy.

**Facilitator:** Etan Kissling (@etan-status), Gajinder Singh (@g11tech)

**Note Taker:** Phil Ngo (@philknows)

**Pre-Reads:**

- [Part 5: The Purge - Feature cleanup](https://vitalik.eth.limo/general/2024/10/26/futures5.html)
- [Light client concept overview (25min video)](https://www.youtube.com/watch?v=ZHNrAXf3RDE)
- [EIP list](https://fusaka-light.box) (no detailed prior knowledge needed)

**Slides:** https://purified-web3.box/slides.pdf

## Agenda 

* (25min) Presentation
  * Wallet's point of view (current situation)
  * eth_getLogs improvements
  * SSZ transactions / receipts
  * Synergies with other efforts
* (45min) Open discussion with goals:
  * Common understanding about what problems verifying wallets are facing
  * Roughly understand scope of improvements
  * Agree on a coarse timeline on if / when to include this
  * Identify interactions / synergies with other features
  * Addressing technical questions

## Notes & Action Items 

TBD - Will be added during the session.

*Breakout sessions will **not** be recorded.* 

*Good notes will help everyone who could not be in the room get up to speed on what happened. Unless instructed otherwise by a participant, please default to using [Chatham House Rules](https://en.wikipedia.org/wiki/Chatham_House_Rule#the_rule).* 

*This will make the process easier, but in cases where there is value in specifying a specific individual (e.g. they are championing a proposal, taking on an action item, etc.), you can mention them. Similarly, nothing should be "off the record", but if someone is uncomfortable with a statement being part of the notes, please respect this.* 

*As a calibration point, see the [ACD recaps](https://ethereum-magicians.org/t/all-core-devs-execution-acde-198-october-10-2024/21314/2?u=timbeiko)*


## Meeting Notes:

Wallet (balance):
- We can't just use p2p for data, especially if you're a phone
- Needs a server via Web3 API
    - eth_getbalance -> Returns balance
    - But server can lie
- Problem: IP correlation to wallets by provider and can be shared with authorities

How:
`eth/v1/beacon/lightclient` to the Beacon API provider
Returns latest root hash

Then use `eth_getProof` to the web3 API to return merkle proof

Goal: Talk to multiple servers. There's a concept of a web3 purifier you can put in before the API that lives as a library. We want to get rid of Infura, Alchemy dependence.

This portion of getting balance is pretty good as-is.

---

Wallet (Tokens/NFTs)

- Problem: Token balance requires eth_call, different API. We have to go to the contract, call a function it it called getBalance to return the balance of that token. To execute you need to download the code and run that code in EVM everytime it accesses a state. 
- Helios: Web3 Purifier. Point your wallet to this RPC. 
    - Problem: Too many round trips, inefficient especially for slower network
- Access lists are best effort for now

Wallet (History)
- Problem: tx_hash is not part of the chain
    - There's an additional MPT type header, which is different from tx_hash
    - You need to hash for tx_hash, then check it's part of the block with a second hash
    - Then you use Type, TxData for the sig_hash
    - Verification takes too long

You need the full tx, hash it 3 times and use ecrecover. Very slow.
Then hashing to SSZ = 4 times it is hashed

On an embedded device, it could take 2.5s to verify your NFT!

Receipts: 

- Receipts contain a transaction type, status code (success or failure), cumulative gas used, and logs.
- The cumulative gas used field requires obtaining the previous receipt to calculate the actual gas used for a specific transaction.
- Receipts include all log data, which may be unnecessary for many wallet operations.

Incomplete Transaction History:

- Some operations, like account abstraction and self-destruct, don't emit logs but still change balances.
- This makes it impossible for light clients to maintain an accurate history of all balance changes without running a full node.

Inefficient Log Retrieval:

- The current eth_getLogs API returns all logs matching a filter, but doesn't provide a way to verify if logs are missing.
- To ensure no logs are withheld, clients must download all block headers and use the logs bloom filter.
- The logs bloom filter has a high false positive rate (around 50%), requiring downloading of many unnecessary transactions and receipts.
Storage and Bandwidth Inefficiency:
- Clients often need to download full block headers, many transactions, and receipts to verify log integrity.
- This process is bandwidth-intensive and storage-heavy for light clients and wallets.

Missing Information for Certain Operations:
- ETH transfers in certain scenarios (e.g., self-destruct) don't emit logs, making it difficult to track all balance changes.
- Staking rewards and withdrawals also lack log emissions, complicating the tracking of these operations for light clients.

Solutions:

EIP 7708:
- Introduces new log types for ETH transfers and fee payments.
- Ensures all balance-changing operations emit logs, improving traceability for light clients.

Removal of Bloom Filters:
- Proposes removing bloom filters from receipts to save space (about 256 bytes per receipt).
- The saved space can be used for the new log types introduced in EIP 7708.

EIP for Verifiable Logs:
- Introduces an accumulator-based system for log verification.
- Allows clients to verify log completeness without downloading all block headers.
= Current implementation uses separate accumulators for each address, topic, and address-topic combination.

EIP 7745:
- Proposes a more efficient log filter structure.
- Aims to reduce the data needed for log history searches to about 20-30 megabytes for 9 years of history.
- Enables local log searching within seconds on light clients.

Additional Log Types:
- Proposes new log types for staking rewards (priority fees) and withdrawals.
- Ensures all balance-changing operations are traceable through logs.

## Discussion and Questions

Privacy and Server Trust

- A key question was raised about how the proposed changes improve privacy. 
- Users no longer have to trust a single server, as they can verify data from any source.
- This allows the use of de-anonymizing networks and distributed networks without loading policies.
- Users can use different servers for each wallet, enhancing privacy.

Node Access and Public RPCs

- Concerns were raised about node operators allowing random requests. 
- There are many public RPCs available, though they can be unreliable.
- Users can send requests to multiple RPCs, increasing the chance of getting a response.
- Data can be fetched using methods intended for this purpose, like distributed networks.

State Subnet Authentication
- A question was asked about the authentication of the state subnet in the program. 
- It would be authenticated using a hash-based Merkle-Patricia tree.
- Users running their own portal node would have validated data.
- Different models for storing state are being implemented, with the current one using a content-addressable key-value store for each tree node.

Data Size and Structure

- The 20 megabytes mentioned refers to a query for 20 million blocks of block history in the EIP 7745 structure.
- The current experimental implementation for 15 billion addresses and topics is about 63 gigabytes, which is significantly smaller than the current block receipts.
- The data structure allows for efficient log searches without accessing most of the data.

Accumulators and Data Design

- There was discussion about the different designs and EIPs related to accumulators:
- EIP 7792 involves separate accumulator lists with one hash per stored item.
- EIP 7745 is a different design referenced for the 20 megabyte structure.
- Concerns were raised about the efficiency of storing and accessing accumulators in the state.
- A proposal to move accumulators to an external system with ZK-SNARK proofs was mentioned.
- The possibility of adding a new filter to block headers that commits to a new data structure was discussed, potentially requiring only 10-15% extra data.

Implementation Challenges

- The potential for long lists when dealing with frequently occurring addresses or topics.
- The issue of unique log topics leading to a tree with billions of entries, similar to current state problems.
- The temporary nature of some solutions, such as writing to state, which is described as a "hack" for the devnet.
- The discussion highlighted the complexity of the proposed changes and the ongoing work to optimize data structures and improve efficiency in Ethereum's light client and wallet functionality.

### Timelines?

- A lot of EL changes, some CL. 
- G* Fork??
- Cleanup fork? We need some meme brainstorm.

Order of changes?
- We should ship everything at the same time
- Spreading it out makes it hard to convince
- As a fork, it'll create meaningful value to the user
- Implemented in EthereumJS and it took 1 person, one and a half months of work.
- It took less than a week for Noah to implement his changes in Helios
