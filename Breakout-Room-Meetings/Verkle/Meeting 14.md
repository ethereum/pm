# Verkle Meeting 14

## Meeting Info

March 11, 14:00 UTC

Recording: https://youtu.be/0Zd4zK2Zupg

Thread recap: https://twitter.com/rudolf6_/status/1767565116101525567

## Agenda:

1. Client team updates
2. Testing updates
3. DoS vector discussion
4. Testnet relaunch


# 1. Client team updates

@jasoriatanishq
 for 
@nethermindeth
: last two weeks focused on stateless execution on the current testnet. Identifying the problematic blocks, and working through any issues.

@DoctZed
 for 
@HyperledgerBesu
: managed to get further along following the testnet to a later block number. Currently waiting for relaunch of new testnet. Meanwhile working on perf optimizations.

@gballet
 and 
@ignaciohagopian
 for 
@go_ethereum
: 
Guillaume: Spent some time working with other teams to track down and understand bugs when syncing with the testnet. Also some code cleanup, and started on Dencun rebase. Working on the gas accounting layer bc the gas model isn't currently following the spec. Hopefully next testnet to use the standard gas accounting.
Ignacio: The replay tool is now working again on the rebase branch. Allowed us to discover two issues that will be fixed in the geth implementation.

@gajpower
 for 
@EFJavaScript
: wanted to sync the Kaustinen testnet in a way that lets us hop over the invalid blocks that we see. And we were able to achieve that. Now waiting for the new testnet so we can test the latest fixes.

@kevaundray
: reminder to teams that still need to modify the Pedersen hash function in their crypto libraries. See the geth change here for more info: https://github.com/gballet/go-ethereum/pull/401 and also https://github.com/ethereum/EIPs/pull/8302


# 2. Testing updates

@elbuenmayini
 from the testing team joined to share latest updates and info on Verkle testing:

There are some changes to the way that we fill tests and the way that all clients will consume tests in the post-Verkle world. The main change that we’ve been working on is that since Verkle can no longer output the post-alloc, we have to make some changes to how we get this info from Verkle from the transition tool. And also how we process it internally while filling tests. For those not familiar with the transition tool: it’s a tool that in this case Geth provides to be able to do the transition function and get the output allocation.

We will have to make some larger changes in the way we write our tests, because now we have to check the Pedersen hash to get the actual position of the storage keys that we need to check in every single one of our tests. Working on some refactoring to make this easier. Changes to the transition tool shouldn’t impact the clients, but the output of the tests will change too and this affects how the clients consume them.

For more info on the testing updates please check out the full recording (linked in the GitHub agenda), or reach out to 
@elbuenmayini



# 3. DoS vector discussion

@GottfriedHerold
 shared some thoughts on a topic brought up on the previous call by 
@ignaciohagopian
 around a potential DoS vector. (Note: see Ignacio’s initial writeup here for more context: https://hackmd.io/@jsign/vkt-tree-branch-attack)

The tldr here involves exploring a potential DoS vector that an attacker could exploit by making tree branches much deeper than expected, and thus making nodes do more costly work (since accessing data that is stored at a high depth in the trie is more expensive in various ways).

If an attacker has a budget where they are willing to spend a few million USD, and assuming the attack is ASIC friendly, in theory this would allow an attacker to create a branch that has a depth of 14 or so. In fact, the attacker may be able to create not just one of these deep branches, but a large number of them. Conclusion is that clients should be able to comfortably handle a depth in the range of 14 to 16.

Gottfried put together a doc that walks through all of this in greater detail here: https://notes.ethereum.org/hmqCk1tiTq6TdrxO_CKhuw

# 4. Testnet relaunch

@gballet
 shared a presentation to give a brief overview on recent testnet developments, as well as plans for the upcoming testnet launch (Kaustinen-5).


Over the past few weeks/months, we’ve been able to make solid progress through client teams attempting to sync the testnet, and uncover bugs/issues along the way.

We also had a network split that happened a couple weeks ago. Suspicion is this was caused by the test contracts that were deployed to the testnet with the assistance of OpenZeppelin. Looks like Geth got overwhelmed and some of the machines missed slots. We then relaunched everything and appears to be back to normal.

Status of current testnet can be found here with list of all known bugs to be fixed: https://notes.ethereum.org/@ethpandaops/verkle-gen-devnet-4

Other items going into the next testnet include: circular buffer implementation for blockhash (EIP-2935), gas model refinements to no longer inflate gas costs, and the Pedersen hash change to use map to field instead of serialization. The testnet won’t have the Dencun rebase yet, but hopefully in the next one. 

Lastly, 
@jasoriatanishq
 and 
@gajpower
 discussed if we could try to track down any issues with stateless syncing as early as possible, fix those issues, and relaunch the testnet. Rather than having such a long-lived testnet as we’ve done in the past. Decision: try to get it turned around at least every 2 weeks.
