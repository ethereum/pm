# Verkle Meeting 17

## Meeting Info

April 22, 14:00 UTC

Duration: 60 minutes

Meet link: shared in #verkle-trie-migration Eth R&D Discord right before the call

Recording: https://youtu.be/dbz6UPOT01U

Thread recap: https://x.com/rudolf6_/status/1783449448590541016

## Agenda

1. Client team updates
2. Testing updates
3. Kaustinen v6 status and Kaustinen v7 wishlist
4. Portal Network presentation
5. 32-byte chunking ideas for Verkle
6. EOF + Verkle presentation+discussion

# 1. Client team updates
@ignaciohagopian
 for 
@go_ethereum
: found and fixed a Geth bug, thanks to the Verkle witness explorer (see http://explorer.ihagopian.com). 
@gballet
 synced a new geth node to have more recent state so we can get updated replay benchmarks, and also get insight into things like performance bottlenecks, witness sizes, etc. 

@gajpower
 and 
@GabRocheleau
 for 
@EFJavaScript
: Attempted to do a stateless sync with the kaustinen6 testnet. Able to sync most of the blocks, but ran into issues in a few blocks related to blockhash handling. EthJS has also fully migrated to the Wasm cryptography for Verkle. This paves the way for an actual Verkle trie implementation that will be able to provide a stateful sync.

@jasoriatanishq
 for 
@nethermindeth
: on the Kaustinen testnet, ran into an issue at around block 30,000. Think we know what the issue is and will probably debug this week! In addition to that we are working on the transition, and more testing around Verkle sync.

Daniel for 
@ethnimbus
: Made progress with implementing Verkle in our execution layer client. Hit an issue with our existing database setup, so decided to circumvent the current database and come up with something basic for Kaustinen integration. Also started implementing a brand new database that will support both Verkle and Merkle. Ongoing effort, but will be much more storage efficient. Next up is continuing the work towards integrating with Kaustinen.

@kt2am1990
 for 
@HyperledgerBesu
: Started to join the testnet. Hit a gas cost issue in block 645. Also 
@DoctZed
 is working on some optimizations. New people are joining the team and will help work on the gas cost updates, as well as the proof implementation with 
@DoctZed
.

# 2. Testing updates
The transition tool works with the changes requested from 
@gballet
. Next up is to continue getting the generated fixture to work within Hive using the Geth devnet branch. The goal is to have fixtures ready in the next few weeks.

# 3. Testnets: Kaustinen v6 status and Kaustinen v7 wishlist
Kaustinen v6 launched without any major problems. Working to get Aave and Uniswap deployed as part of ongoing testing efforts on Kaustinen v6. For Kaustinen v7: would like to implement fill_cost, so that we can have a more accurate estimate of what the gas cost will look like.

# 4. Portal Network presentation
Milos from the Portal Network team joined to share some recent work around how the complete Verkle state can potentially be stored within the Portal Network. (see writeup here: https://ethresear.ch/t/portal-network-verkle/19339) For those not familiar, the Portal Network is a collection of decentralized p2p networks which provides access to Ethereum data that users would normally have to get either from a full archive node, or from a centralized 3rd party RPC provider. The goal of this is to make it easier for anyone to run trustless light clients. Recommend watching the full presentation from Milos for those who want to better understand the great work being done by the Portal Network team 💜

# 5. 32-byte chunking ideas for Verkle
@gballet
 shared some thoughts around implementing this idea and potential optimization benefits. In this model, rather than putting the bytes at the beginning of each chunk, it would be put in a buffer somewhere. But the question is where should this live? Either it gets put at the beginning in the first 128 leaves, or in the reserved leaves of the header group. 
@ignaciohagopian
 shared his thoughts that we probably will need to test the two ideas, and it likely depends on each contract and how many chunks the contract has. 
@gballet
 to start by trying to put it in the account header and will see how it goes.

# 6. EOF + Verkle presentation
Last up, 
@ignaciohagopian
 presented a brief overview of potential ways in which EOF and Verkle may interact in non-obvious ways.

TLDR is that in a Verkle world, the smart contract code will be included as part of the state tree. This is different from today, where smart contract code is simply in the client’s db. The most obvious follow-on consideration of this is that the bigger your contract is, the more gas you will have to pay (because you had to write all this code into the tree). The other related consideration here with Verkle is that whenever you execute a transaction, the more bytecodes that your transaction execution needs the more gas you will have to pay (because you have to include this in the execution witness).

Danno joined to share a few thoughts and some helpful framing around how EOF at its core is just a container format. It should not fundamentally change how the EVM works. Danno also shared that there was a prototype compiler previously written by solidity, and in previous tests he saw between 1-3% opcode size reductions of bytes. The biggest open questions here perhaps won’t truly get answered until we are further along with implementations from Solidity and Vyper. But Danno doesn't expect it to be anything outside of the 1-3% range. Should not be any big changes to gas cost and will mostly be a wash. Conversations will continue as we get further along with EOF testing and compiler implementations.
