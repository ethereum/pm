# Verkle Call #24
## Info
Note: This file was copied from here: https://notes.ethereum.org/@rudolf/sic-notes#Call-24-September-9-2024

Date: September 9, 2024

Recording: www.youtube.com/watch?v=TTqikpo4R7g

Agenda: https://github.com/ethereum/pm/issues/1149

## Notes

## 1. Team updates

Gary for @HyperledgerBesu: continuing work on stem-based flat database, and have a working implementation. Will simplify sync for Besu. Also making progress on gas cost changes and witness updates (EIP-4762). And planning on getting back to work on the transition stuff soon.

@ignaciohagopian and @gballet for @go_ethereum: last week, discussed sync with the Geth team, and would like to figure out how performant it is to compute all of the leaves as they are needed (reading SLOAD + building a snapshot based on those leaves). Interested to understand Besu’s performance in this regard. Also completed a bunch of work on the testing framework. Gas costs are ready to go. Should be ready for new testnet in next few days.

@GabRocheleau for @EFJavaScript: continued work to prepare for the upcoming testnet. Running the actual tests this week. Also made some upgrades to the WASM cryptography library so can begin creating proofs, and allows for stateful verkle state manager. Previously could only run blocks statelessly.

@jasoriatanishq for @nethermindeth: mostly been working on getting the Hive test running. Found and fixed a few bugs. One change in the spec around gas costs, and continuing work on the transition. Working on some cryptography improvements as well.

Somnath for @ErigonEth: integrating the gas cost changes and the witness calculation changes. Noticed some issues with the state management, but hopeful can resolve it in next week. Erigon has already started migrating everything to Erigon 3, but current verkle work is based on Erigon 2. Will try to join devnet-7 soon after it launches.

@g11tech for @lodestar_eth: rebasing on latest from lodestar, which should provide a more stable base for testnet because of improved performance.

@techbro_ccoli for the testing team: we have the witness assertions now within the framework when filling tests. Can write a test, and assert that a balance is what you expect. More of a sanity check. Now have similar for witness-specific values. Next step is to optimize how the tests are filled, and improve the transition tool runtime.

## 2. Devnet Readiness

There’s a couple updates to the specs that are still open. Quickly reviewed with Guillaume 3 PRs to merge in asap for the testnet:

https://github.com/ethereum/EIPs/pull/8867
https://github.com/ethereum/EIPs/pull/8707
https://github.com/ethereum/EIPs/pull/8697

^ Leaving open for comments, but no objections raised during the call on these PRs.

## 3. Verkle, Binary, & Tree-agnostic development


Quick recap of recent conversations we’ve had around the tradeoffs of Binary vs. Verkle:

This is a topic that has come up often over the past few years, and even going all the way back to 2019/2020 – when @gballet was an author of EIP-3102: an initial proposal to migrate to a binary trie structure.

More recently, as many teams have made strong progress on the ZK proving side, there’s been renewed discussion around whether a ZK-based solution could be ready in a similar timeframe to Verkle (or soon thereafter), and allow us to skip straight to a fully SNARKed L1.

In this scenario, a binary trie structure is arguably preferable, in that it’s a friendlier option to current ZK proving systems, despite Verkle’s advantages in other dimensions (such as smaller tree/proof size and slower state growth). While Verkle is closer to “mainnet ready” today, it’s possible the gap closes over the next 1-2 years.

The challenge and discussion now is mostly centered around how we can optimize forward progress on R&D efforts, solve problems facing users today, while also making sure we properly evaluate other viable/evolving technologies to ensure we land on the best long-term path for the protocol + users.

TLDR:
it’s safe to say we plan on doing a bit more of at least two things over the next ~3-6 months:

(1) evaluate binary: invest meaningful bandwidth into exploring / benchmarking a binary tree structure, while collaborating closely with zk teams. Make sure we understand where we are today in terms of performance, hardware requirements (with which hash function etc.), and where things need to be in order to be viable on L1.

(2) tree-agnostic development: continue building the infrastucture and tooling necessary for statelessness, but lean into a tree-agnostic approach to optimize for reusability. This will give us flexibility to land on the best solution, whether it’s Verkle, Binary, or anything else. In any case, much of what has already been built (e.g. for state migration) will be a valuable and necessary component since it’s unlikely we stick with the current MPT for long.

If you are excited about making progress on statelessness and scaling the L1, you can join the conversation in our biweekly implementers call 🚀

## 4. Deletions in Verkle
Discussion around whether not having deletions in Verkle will bloat the state. There are also downsides to deletions though, as it may make the conversion process a bit more complicated. TBD on final decision, but no strong objections raised to supporting deletions in Verkle. Recommend watching the recording for anyone interested in better understanding the full picture on this topic.

## 5. Pectra Impact (7702, EOF, etc.)
Ignacio gave an overview of some work he’s done to better understand the potential impact of EOF on Verkle. He created a draft PR with the changes required. Guillaume also shared some thoughts on things we need to be mindful of with 7702. Namely around making sure that when you add something to the witness, you add the contract that the operation is delegated to instead of the account itself (otherwise the witness wil be empty).

## 6. Verkle Sync
Geth team recently had a discussion on the topic of sync, and came away with a few potential suggestions.

(1) around witness validation: full nodes can validate witnesses and make sure that no extra data is being passed as a way to prevent bloating of the witness. (e.g. flag a block that has too many leaves as invalid). Note: if we do introduce this rule, then we have to make the witness itself part of the block.

(2) snapshot per stem, rather than by hash like it currently is.

(3) how long to save the witness on disk: if we save it for something like a month or so, then it makes it a bit simpler for nodes who have been offline for a short period of time (e.g. 2-3 weeks) to rejoin the network. The tradeoff is it would add around 60GB.