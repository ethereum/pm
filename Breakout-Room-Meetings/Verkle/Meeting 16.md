# Verkle Meeting 16

### Meeting Info

April 8, 14:00 UTC

Recording: https://youtu.be/R-Jo2Lci0zc

Original Notes: https://x.com/rudolf6_/status/1778087343611884011

## This week’s agenda:
1. Client team updates
2. Testing updates
3. Witness explorer demo
4. Gas model updates
5. EIP-2935 and EIP-7545
6. Testnet relaunch
7. Blockhash gas corner case


# 1. Client team updates

@0xagnish
 for 
@ethnimbus
: finished implementing EIP-6800, tested it against Geth for correctness, and all looks good. Also making nice progress on the Nimbus full in-memory implementation, and almost reached full statelessness.

@gballet
 and 
@ignaciohagopian
 for 
@go_ethereum
: working on tooling, and helping with the testnet interop. Got a few PRs merged into Geth. And gave a presentation on Verkle to the EPF study group (organized by 
@TMIYChao
 and 
@joshdavislight
). Full recording here: http://youtube.com/live/H_M9bjwtMhU. Also working on syncing post-Shanghai blocks, so we can gather more accurate metrics around things like avg. proof size, gas consumption, etc. Lastly, Ignacio has been working on the witness explorer, and will give a demo here (note: read more about the EPF study group: https://x.com/TMIYChao/status/1755572713073078761)

@gajpower
 for 
@EFJavaScript
: ran through the test vectors to make sure we pass and debugged some of the issues that came through. Almost able to completely sync with the testnet. Just working on resolving mismatching gas issues on selfdestruct. Also working on building out the transition logic with 
@GabRocheleau
, to be able to convert all historical MPT state over to Verkle.

@jasoriatanishq
 for 
@nethermindeth
: syncing with the testnet. Found a few issues in the Nethermind implementation around the gas cost of selfdestruct. Also working on the transition as well, and in a few days will be able to start testing it out.

@kt2am1990
 for 
@HyperledgerBesu
: working on some key performance improvements. Adding batching for generation of the trie key, and for the commitment hash. Also finished some refactoring around merging with the main branch. Waiting for the new testnet to test the gas cost implementation.



# 2. Testing updates

Just a quick update on the testing side here: 
@gballet
 added a tool where you can pass an address and slot number on the command line, and it will compute the key value. Still need to build something to provide the mapping from the hash to the preimage. Once this part is complete, we should have the tooling necessary to test a full transition.



# 3. Witness explorer demo

@ignaciohagopian
 took some time to share a complete walkthrough of the brand new “witness explorer” he’s been working on (for more general background on witnesses in Verkle, see https://ihagopian.com/posts/anatomy-of-a-verkle-proof#905274f526674a82ba7985a8779b5474)

So, what is this new “witness explorer” and why is it helpful? As Ignacio explains, with Verkle the code for executing contracts will be part of the witness and the witness size will vary on how much code is executed. This all adds a new layer to gas accounting, and it will of course be important for app devs to understand this impact.

The new witness explorer allows you to look at any individual transaction, and quickly and easily understand the gas cost breakdown of the transaction. This will be super helpful for anyone debugging, or just looking to better understand gas accounting with Verkle as we get more and more clients and contracts deployed on the Verkle testnet. Highly recommend checking out the recording to see the full demo.



# 4. Gas model updates

@gballet
 shared a few thoughts on how the spec around gas cost modifications, EIP-4762, may continue to evolve over the coming months. Again for those interested in better understanding some of these potential changes and providing input, I’d recommend watching the recording and/or hopping into the R&D Discord.

# 5. EIP-2935 and EIP-7545

For EIP-2935, there has been some feedback from Vitalik and others around increasing the ring buffer size to 8,192 (~day's worth of blocks). This will help give enough time for something like a zk rollup to verify their proof.

For EIP-7545, seeming less likely that this will get prioritized, as it is less apparent that it’s a priority for the L2 teams we've been in discussions with. We will continue to chat with other L2 teams, bridges etc and gather feedback on this. And if no one has a clear case for pushing for 7545 in Electra then it will probably get dropped.



# 6. Testnet relaunch

Changes in the upcoming testnet: extended version of EIP-2935, the witness explorer from Ignacio, and also the fix for the recently identified selfdestruct bug. We've been chatting with some folks from Aave about deploying their contracts on the testnet, and want to make sure we can get all of this done beforehand 💜



# 7. Blockhash gas corner case

Ignacio shared a few quick thoughts on a potential corner case with blockhash and gas cost accounting.

tldr: if a contract is using the blockhash opcode to ask for the hash of the previous block, technically it doesn't need to be charged any gas for doing that because of how we are building the hash history in the latest version of EIP-2935. If we don’t charge anything, however, then we are tying things somewhat to the specific implementation of EIP-2935. 
@gajpower
 weighed in that he agrees we shouldn't be charging extra in this situation because it could just be served out of memory. 
@gballet
 and 
@gajpower
 to continue the conversation offline as we were running low on time.


