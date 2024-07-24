# Meeting Info

June 17, 15:00 UTC

Duration: 60 minutes

Meet link: shared in #verkle-trie-migration Eth R&D Discord right before the call

Recording: https://youtu.be/fwBCbA-28H0

Thread recap: https://twitter.com/rudolf6_/status/1803684902996451797

## Agenda

1. Client team updates
2. Testing updates
3. Code size in Verkle
4. Testnet relaunch
5. Preimage distribution (background reads here and here)

# 1. Client updates

Starting things off with updates from client teams:

@GabRocheleau for 
@EFJavaScript
: working on our own verkle trie implementation for ethJS (to expand beyond a stateless client). Ready for the next testnet with gas cost updates.

@DoctZed
 for 
@HyperledgerBesu
: waiting on test framework for gas cost changes, and meanwhile doing planning around the migration, the sync, and how we can retain the flat DB while doing the migration. 

@gballet
 for 
@go_ethereum
: working on the test framework with 
@ignaciohagopian
 and the testing team. Also collecting/analyzing data to better understand some questions that we’ve been looking at over the past few months. E.g. gas cost overhead, better witness size estimates, total migration time, etc. Should be able to share this analysis in the next 2 weeks or so.

@ignaciohagopian
 for 
@go_ethereum
: finished test vectors for the relevant Verkle EIPs (4762, 6800, 7709). Still some library changes we need to do for them to be filled. After the tests are filled and all the fixtures are generated will share with other clients to run. Regarding the analysis we are preparing: we’ve been collecting around 1 million mainnet transactions from the tip of the chain (last few days) using the geth live tracer. Idea is to use this to simulate gas overhead.

@jasoriatanishq
 for 
@nethermindeth
: still working on improving the cryptography performance, and getting the sync to work. Should have some more updates in the next 2 weeks.

====

# 2. Testing updates

@techbro_ccoli
 from the testing team with a nice update from the testing side of things:

Over past few weeks been able to resolve some bugs, and we are now filling and executing the transition tests on Geth with only a very small number of failures. Once these transitions tests are all passing on Geth, the plan is to make a release of these tests for every client to be able to utilize.

@techbro_ccoli
 also shared a brief presentation which gave an overview of the transition tests, and the 3 types of tests: the pre-fork transition tests, the mid-fork, and the post-fork. The pre-fork ones are tests we already have to test many things on all forks previously, and will also be utilizing to help test Verkle. For example, with the pre-fork transition test we will use it to execute all the test blocks before the Verkle transition, and then after the transition we add some dummy blocks to verify everything has executed properly. Once we are finished with the transition tests, we will then switch focus over to the test vectors that 
@ignaciohagopian
 has been working on for the verkle-specific EIPs.

Recommend watching the call recording to get the full testing summary!

====

# 3. Code size in Verkle

@shemnon
 joined to discuss an idea around raising code size in Verkle to 2GB, to help with smart contract devs who would like to deploy larger contracts in the near future (2-5 year window). There’s been a good bit of pressure from the solidity community to raise this number. But one of the reasons we havent yet raised it was concerns around jumpdest analysis, and having to do this analysis every time you load code from memory.

Rationale from 
@shemnon
 is that with Verkle, we charge for init code now when you deploy a contract. So if you’re doing the jumpdest analysis when you’re deploying the contract, you get charged gas for that. So the size of the analysis now at create time really shouldn’t impact things because it scales with the gas cost. Also with Verkle we will store and cache some of this analysis in with the code, so when you load it from the tree you don’t have to do the analysis. And with code chunking in Verkle, you actually _can’t_ do the analysis. So based on all that, it would seem to be reasonable to increase the size limit (or uncap it).

Assuming that contracts probably won’t get larger than 2GB in the next 5 five years, but should be larger than 64k. So the proposal is that we reserve more than 2 bytes for code size. 3 bytes would be better as that would give us 16mb.

Decision made on the call: agreed to bump it to 3 bytes (16mb), and Guillaume to update the EIP to reflect this.

====

# 4. Testnet Relaunch

We had a brief discussion around making sure we get everything included that we want to be included in the next testnet relaunch. Current plan is to launch the new testnet with all the latest updates sometime in July. This would include the latest bug fixes, the new gas model, as well as the pre-state root being included in the execution witness (just to name a few). We will continue this discussion async and on the next call to make sure we don’t miss anything in the next testnet.

====

# 5. Preimage distribution

Last up, we spent the remainder of the call discussing preimage distribution. @GabRocheleau shared an idea for using the execution witness in Verkle to distibute preimages just-in-time. You can read a bit more about this idea here: https://notes.ethereum.org/QUOsJN2mTQOqEtUQMsBUlw, and also a more detailed summary of the preimage distribution problem in general here: https://hackmd.io/@jsign/vkt-preimage-generation-and-distribution.

The tldr is that during the transition period (converting state from Merkle to Verkle), some of the state will be accessed from the frozen (read-only) Merkle Patricia Tree while all writes will go to the new Verkle trie. At the same time, each block we will convert a set number of values over from Merkle to Verkle. But in order to do this, because we are changing how everything is hashed, we will need all of the historical preimages. For anyone that does not have these preimages, they would not be able to sync the network. (Because they can’t access the state that is necessary to execute the blocks).

So the problem is how do we make sure that everyone who needs the preimages is able to get them in time. The idea here is to use the execution witness to provide all of the preimages which have been converted. 

The main shortcoming with this solution is that it does not solve the issue for anyone who wants to build blocks. It would only help with validating of blocks, because we still require someone to have the preimages locally-accessible in order to build a block and provide these preimages in the first place. It reduces the scope of the problem (to only builders), but it does not solve it completely. Basically we’d still need a way to make sure anyone who wants to build blocks is able to get preimages from someplace other than this execution witness.

@gballet
 brought up a question of whether validators that do not have the preimages locally can still delegate block building to mev-boost builders. Due to how the conversion works, we may need to make sure the execution witness contains the preimages to convert for the _next_ block.

We also briefly flagged an idea from 
@parithosh_j
 to use torrents to help with EIP-4444, and whether part of this could be reused for Verkle preimage distribution. See Pari’s post here: https://ethresear.ch/t/torrents-and-eip-4444/19788.
