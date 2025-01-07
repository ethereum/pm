# Verkle Call #23
## Info
Note: This file was copied from here: https://notes.ethereum.org/@rudolf/sic-notes#Call-23-August-26-2024

Date: August 26, 2024

Recording: https://www.youtube.com/watch?v=VD0P3RkhIjY

Agenda: https://github.com/ethereum/pm/issues/1121

## Notes

## 1. Team updates

ignaciohagopian and gballet for go_ethereum: making solid progress on testing and the upcoming testnet. Managed to get the branch with latest gas schedule working with tests.

jasoriatanishq for nethermindeth: have implemented everything for the testnet. Also working on a few cryptography improvements, and a big refactor to implement the transition. Might be able to implement test transition in next few weeks.

kt2am1990 for HyperledgerBesu: working on modifying how we save data in the DB, to implement a flat DB based on the stem of the tree. Also working on gas cost implementation and the transition.

GabRocheleau for EFJavaScript: ready with all the gas cost updates, likewise just waiting for test vectors to confirm.

Somnath for ErigonEth: getting caught up with the changes up to the most recent testnet. Had an issue when trying to connect to peers on testnet-6, not getting any replies. Will debug with ops.

techbro_ccoli for the testing team: have released latest fixtures, can be found here.

## 2. Testing Verkle overview

Next up, we had a brief presentation from @ignaciohagopian to walk through latest overall progress on the test framework for Verkle. The main branch for the test vectors can be found here in the execution spec tests repo. And to look at existing tests you can find them here in the tests/verkle folder, where all the tests are separated by EIP. Encourage anyone interested to poke around, ask questions, and eventually open up new test cases :)

Ignacio also gave an overview of the changes that were made in geth to support the test framework, how the CI pipeline works, and a summary of all the test fixtures that exist today. The fixtures can be separated into 3 groups:

(1) Verkle-genesis, where everything happens in a post-merkle patricia tree (MPT) world,

(2) overlay-tree, which is running tests with a “frozen” MPT, and doing the block execution in the Verkle tree,

(3) consuming tests from previous forks, to check pre-Verkle execution isn’t broken



## 3. Testnet readiness check

Next up, we went through and double checked each team’s readiness for the next testnet. Geth, Nethermind, and EthJS are ready as far as we can tell at this point, while Besu is still finishing up gas cost updates.

## 4. Binary Tree Exploration

Last up, Guillaume shared a presentation which summarizes some recent discussions we’ve had, as there’s been a bit of a renewed push by some in the community to explore binary trees as a potential alternative to Verkle. Some of this push has been motivated by recent progress made in ZK proving performance, and a desire to provide something that is even more zk-friendly than Verkle to help accelerate the move towards an eventual fully SNARK-ified L1.

Highly recommend watching the recording to view Guillaume’s full presentation, but to give a rough TLDR: the main advantage of Verkle (apart from the fact that progress on Verkle is much further along today compared to a binary tree alternative) is that Verkle gives us small proofs (~400kb). And these proofs can enable stateless clients pretty much as soon as we ship Verkle.

On the other hand, the advantages of binary trees is that hashing performance / commitment computation are much faster in general. And are also more compatible with current ZK proving schemes. The other advantage is around quantum resistance, though of course still much debate around timelines for quantum, and there are several other areas of the protocol that will need to be upgraded as part of any post-quantum push.

The good news is: in either case, much of the work we’ve already done with Verkle is reusable in a binary tree design: (1) gas cost changes, (2) the single-tree structure, (3) the conversion & preimage distribution, and (4) (potentially) sync.

What would change with binary trees though include: (1) the proof system, and (2) the cryptography (replacing polynomial commitments/pedersen with hashes)