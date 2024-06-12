# Kintsugi incident report

This post will cover the full summary of the incident, its consequences and concrete action plans moving forward before a mainnet merge.

Note: this report was originally published [here](https://notes.ethereum.org/@ExXcnR0-SJGthjz1dwkA1A/BkkdHWXTY).

## TL;DR: 
The merge testnet, Kintsugi, ran into issues with several clients. A fuzzer created an invalid block that was deemed valid by Nethermind and Besu due to a missing check. This invalid block caused the network to split into 3 parts - One part with the invalid block, One without the invalid block and One which went into an Optimistic Sync mode. While fixes were deployed, the fuzzer created another block that triggered a further issue in Geth causing nodes to fail to join the correct fork. Once the Geth issues were fixed, we were able to bring back all the nodes into the same correct fork and the chain began finalizing again.


## Summary
The merge testnet Kintsugi ran into a series of issues in the previous weeks which exposed several bugs across a multitude of clients. The issues were mainly caused by a fuzzer developed by [Marius](https://twitter.com/vdWijden), the fuzzer aims to create interesting blocks and propagate them through the network.

One such block had its `blockHash` replaced with its `parentHash`. The `engine_executePayload` has all the parameters needed to construct the block as well as construct the `blockHash` of the block. The EL client should construct the block from the parameters and verify it against the passed `blockHash`. This particular block accurately failed the check on Geth, but validated in Nethermind and Besu. The block was incorrectly validated in Nethermind due to a cache issue, while Besu did not have such a check at all. Due to this, the block was proposed by a Lighthouse-Besu node and caused the chain to split into two parts, one fork followed by all the validators connected to a Nethermind/Besu EL and another fork consisting of validators connected to a Geth EL.

*Note, the `blockHash` check for the **current** block is newly required in the Merge, thus the missing and inaccurate verifications in some clients.*

A bug in Geth was returning a JSON-RPC error instead of `INVALID` when executing the wrong payloads and a bug in Teku (fixed but not yet deployed at that time) considered those errors as a viable condition to continue in optimistic sync mode. Therefore, the Teku-Geth nodes went into optimistic sync mode as a result of hitting an invalid payload. Since the block itself was valid, the connected Geth nodes fetched it from the network instead of the engineAPI, and the Teku-Geth nodes were now building on top of the invalid forked chain. Due to the Teku nodes being on a buggier older version, the Teku-Geth nodes stayed in optimistic sync mode and refused to propose blocks during the non-finality period. We now had a scenario in which CL(lighthouse,prysm,nimbus,lodestar)-Geth(~46%) and  CL-Nethermind/Besu(~19%) were in different forks, a further number of validators running Teku-Geth(~35%) were in optimistic sync mode. 

After identifying and deploying fixes for the Nethermind and Besu nodes, we were able to get them back online. The updating of Teku-Geth nodes led us to another bug related to invalid memory access caused by an issue in Geth related to the block sequence validation. This specific bug was triggered by Marius's fuzzer as well, the fuzzer produced a block with `block_number=1` with a valid `parentRoot`. Before Geth executes a block, it needs to look up its parent to see if they need to sync or not. One way to do this is by checking the `parentHash` in the cache or by `parentHash` as well as `blockNumber` in the database. Since Teku executes all the payloads of all the forks simultaneously, the cache did not contain the `parentHash` anymore. Therefore, Geth attempted to lookup the parent by `parentHash` and `blockNumber` in its database. The database however contained no hash with this `blockNumber` (the fuzzer created this block). Geth would reason that since it has no parent, it needs to start a sync. However, this triggered sync would attempt to sync a shorter chain than the canonical chain which violated some conditions in Geth. This caused the Geth process to panic and the node shut down, causing the Teku-Geth nodes to remain in an unhealthy state.

During the debug process for the above issues, the Geth team also uncovered a race condition in the merge codebase which triggered panics. Additionally, we ran into problems with Nimbus throwing an error related to EL re-connection and Lodestar downscoring peers for block rejection. 

The client teams pushed all their fixes and all the nodes were updated. By the time all the fixes were in play, the chain had split into smaller forks with each having low participation rates. Resyncing a few nodes allowed us to reduce the number of forks. Once enough nodes had resynced, we were seeing more and more nodes re-org onto this fork, allowing us to cross the 66% threshold required for finality. 


## FAQ
### Is the testnet dead?
No. The chain eventually finalized after we deployed fixes and resync-ed some stalled nodes. Once the chain finalized it performs as it always has. Currently Kintsugi sees ~99% participation rates, indicating all the client bugs have been patched and the network is running optimally. Transactions and smart contract interactions continue to function as expected. 

## Why was the chain not finalizing for so long?
Although we identified the root cause quite early on, we wanted to leave the chain in its non-finalizing state to allow for clients to debug their code against. Additionally, we wanted to collect data about client performance during non-finality periods. 

### Did validators on the fork get slashed?
No. Each validator contains a `slashing protection` database that ensures that the validator does not sign slashable information. The validators on the "wrong" fork were simply seen as `inactive` on the "correct" fork. Once they re-orged onto the "correct" fork, the slashing database prevents them from signing slashable information. 

### How does this affect the mainnet release? Is there a new delay?
We believe this incident does not affect the mainnet launch plans. No critical bugs were found in the specification itself. The purpose of the testnet was to unearth bugs and we believe that Kintsugi has done a great job with finding edge cases in client implementations. The incident was a good stress test for various client combinations. We have a [public checklist](https://github.com/ethereum/pm/blob/master/Merge/mainnet-readiness.md) which will guide when we are ready to merge on mainnet.


### How does this affect the testing plan?
We will look into creating a couple of testnets where non-finality is enforced. Continuous testing on such non-finalizing testnets would allow us to trigger more edge cases as well as improve tooling. The bugs found in this incident will be added as static test cases to ensure that we have no regressions. 

### Important takeaways for validators, infrastructure providers and tooling developers
The non-finality period on the testnet reinforced some assumptions for worst case-hardware requirements. During periods of non-finality, validators should expect:
- Increased CPU load (100% at times) due to evaluation of various fork choices rules 
- Heightened disk usage due to the lack of pruning due to non-finality
- Marginal increase in RAM usage

This means, any additional tooling or monitoring running on the same machine would suffer from resource contention issues. The tooling for the Kintsugi testnet (block explorer, beaconchain, faucet, RPC) runs on a Kubernetes cluster with 3 nodes. This cluster also runs multiple beacon nodes which are used by the tooling. Since the beacon nodes were using much more resources than provisioned for, our tooling often ran in a degraded manner due to a lack of resources. It would be prudent for infrastructure providers to run their CL and ELs in separate machines or with strict resource use definitions. 

The merge implies that every CL will need its own EL running. ELs (on mainnet) currently require significant disk sizes. During times of non-finality, the disk usage of CLs will also balloon and it could lead to crashes due to a lack of space. All validators should ensure that they have a large enough buffer to account for such issues. 

Developers of tooling that rely on finality should account for non-finality periods. One possible manner is to display the `optimistic` information while conveying that the information could change in the UI. 








