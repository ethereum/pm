# 1. Team updates
@ignaciohagopian and @gballet for @go_ethereum: finishing up document on code chunking gas cost overhead in Verkle. Also working on more test vectors for the state conversion (converting state from Merkle to Verkle). And putting together first draft of the state conversion EIP, to help with coordination and act as the source of truth for test vectors. In addition, Guillaume has been collecting witness size data, preparing for the testnet relaunch, and busy merging more Verkle stuff into Geth so we can have a testnet on top of Dencun.

@DoctZed for @HyperledgerBesu: currently optimizing around storage in the DB, and moving some of the work to background threads. Also finishing up the updates to gas cost schedule.

@techbro_ccoli for testing team: continuing work on the genesis test vectors. Also discussed a bit with Guillaume about making the tests runnable by anyone, so that each client team can check prior to relaunching the next testnet. @techbro_ccoli to put together a document on how to run the tests easily. Can find the tests here: https://github.com/ethereum/execution-spec-tests/releases

# 2. Testnet readiness
We went through the main items we want to include on the next testnet, to see where client teams are in terms of readiness. Geth is still working through a few items: notably fill_cost and other gas cost updates. Nethermind has implemented everything previously discussed at the client team interop, but still need to run latest test framework to verify. Besu is not yet complete, and need to wrap up some of the DB work they are currently in process of refactoring before finishing up testnet work.



# 3. Witness size measurements
Next up, Guillaume shared some recent experiments he has been running around witness sizes, as well as some potential optimizations. Tldr: in the current version of the spec we store the state diff in a certain way with the old value and new value as optionals.



The issue with this approach is that very few SSZ libraries support optionals, and due to how other libraries handle this it makes for unnecessarily large witnesses.

So, one proposal to fix this: get rid of optionals by grouping all the suffixes together in an array of bytes, and grouping all the old values and new values likewise in their own lists.



Testing this new approach (vs. the current approach) results in significant reduction in witness size. The current approach has a median witness size of ~700kb. While the new approach has a median witness size of ~400kb. One note: we can further reduce the witness size significantly (possibly another 50%) by removing new_values, which would put witness size closer to 200kb.



Guillaume also shared a 2nd proposal for an optimization which could further reduce witness size. (Still need to implement it to get the numbers). Will come back to this discussion on a future call.

# 4. Other Misc EIP Updates
Next up, we went through a few updates to EIPs including EIP-6800 and EIP-2935. See the complete list here: https://notes.ethereum.org/@gballet/S1YEC5fOA#/5.

This is mostly relevant for client devs and other implementers, but recommend watching the recording for anyone interested!

# 5. Code-access Gas Overhead
Last up, @ignaciohagopian walked us through a document he put together, which provides a very helpful analysis of the cost of code chunking in Verkle.

For those not familiar: in order to fully support stateless clients in a post-Verkle world, we will have to add contract code to the tree (in addition to account data and contract storage). This is necessary for clients to statelessly validate blocks. This process of transforming contract bytecode into tree key-values is called “code-chunking”. But code-chunking is not free, and will add some new gas cost overhead which doesn’t exist today in a stateful world.

Ignacio’s document does a great job at summarizing, analyzing, and approximating what these costs will be with Verkle by looking at ~1 million recent mainnet transactions. The TLDR is that, on avg, we should expect around 30% gas cost overhead. The good news is there are several ways we can potentially mitigate this. Importantly, paying this extra cost will unlock stateless clients, which will allow us to significantly raise the gas limit (more than 30%) to more than offset this additional cost. See https://x.com/dankrad/status/1790721271321256214.

Highly recommend watching the recording, and also going through Ignacio’s full document here for anyone curious to learn more: https://hackmd.io/@jsign/verkle-code-mainnet-chunking-analysis.
