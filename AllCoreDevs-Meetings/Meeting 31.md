# Ethereum Core Devs Meeting 31 Notes
### Meeting Date/Time: Friday 01/12/18 at 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/29)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=biNCOCQdjQ0)
### [Reddit thread](https://www.reddit.com/r/ethereum/comments/7pu8hr/live_1400_utc_ethereum_core_devs_meeting_31_011218/)

# Agenda

1. Testing Updates.
2. [Yellow paper update](https://twitter.com/gavofyork/status/949662885222998018).
3. EWASM update + update on the following related EIPs.
  a. EVM 2.0 - https://github.com/ethereum/EIPs/issues/48 
  b. Extend DUP1-16 / SWAP1-16 With DUPN / SWAPN - https://github.com/ethereum/EIPs/issues/174
  c. Subroutines and Static Jumps for the EVM - https://github.com/ethereum/EIPs/issues/615
4. Stateless client development.
5. Add ECADD and ECMUL precompiles for secp256k1 - https://github.com/ethereum/EIPs/issues/603 [[See this blog post for context](https://medium.com/@clearmatics/privacy-on-ethereum-is-too-expensive-fb8b9e1815b2)].
6. Introduce miner heuristic "Child pays for parent" (like in BTC) to combat the weird cases when transactions with 1000 Gwei stuck in the mempool (because they are dependent via nonce on transaction paying much less and not getting mined).
7. Creating a relay network of nodes to mitigate issues [described here](https://github.com/ethereum/pm/issues/29#issuecomment-356952590) and [other transaction propagation issues](https://github.com/ethereum/pm/issues/29#issuecomment-357151890).
8. Fork release management/Constantinople.
9. Client updates.
10. Other non-agenda issues.

# Notes
Video starts at [[4:36](https://youtu.be/biNCOCQdjQ0?t=276)].

## [[4:56](https://youtu.be/biNCOCQdjQ0?t=296)] 1. Testing Updates
No updates.

## [[5:27](https://youtu.be/biNCOCQdjQ0?t=327)] 2. [Yellow paper update](https://twitter.com/gavofyork/status/949662885222998018).
Gavin put the Yellow Paper under the Creative Commons Free Culture License CC-BY-SA. Yoichi and Nick Savers have been making progress handling the Yellow Paper PRs. There is still the somewhat unresolved issue of what should define the "formal standard" of Ethereum and should an update to the Yellow Paper or another specification be required for every new EIP. This can be discussed in more detail in future meetings when there is greater attendance.

## [[7:43](https://youtu.be/biNCOCQdjQ0?t=463)] 3. EWASM update + update on the following related EIPs.

### [[7:55](https://youtu.be/biNCOCQdjQ0?t=475)] General update
Ewasm contributors are currently meeting in person together in Lisbon. EWASM EIPs listed in the subpoints are not up to date and can be disregarded. People should use the github.com/EWASM/design repo. The design has been pretty much speced out in the last year. During the design phase there were 2 implementations done in parallel: Javascript and C++ (which can be integrated in cpp-ethereum and geth). Issues have been faced in building out EWASM including struggling with implementing synchronous code in Javascript/browser. Idea was to move to an asynchronous model. Currently there is not a full decision on using synchronous vs asynchronous, but we are leaning towards synchronous implementation in C++ to run a testnet in cpp-ethereum that can run pure Web Assembly contracts. Metering contract in Web Assembly is on the to-do list and doesn't rely on sync/async decision. Likely will take week to come to a decision on sync vs async.
More technical discussion and a funny anecdote involving the asynchronous vs synchronous decision and the affects of the recent Spectre/Meltdown attacks start at [[12:07](https://youtu.be/biNCOCQdjQ0?t=727)].

### [[15:08](https://youtu.be/biNCOCQdjQ0?t=902)] a. EVM 2.0 - https://github.com/ethereum/EIPs/issues/48 
Martin Becze will be closing this EIP. It is outdated.

### [[15:28](https://youtu.be/biNCOCQdjQ0?t=928)] b. Extend DUP1-16 / SWAP1-16 With DUPN / SWAPN - https://github.com/ethereum/EIPs/issues/174
This doesn't have to do with EWASM, it has to do with adding extra opcodes in the current EVM. It is an upgrade to EVM 1.0 which is not needed if we skip straight to EWASM. 

### [[16:47](https://youtu.be/biNCOCQdjQ0?t=1007)] c. Subroutines and Static Jumps for the EVM - https://github.com/ethereum/EIPs/issues/615
Greg has been working with Seed (Gitter tag) who is writing an ELM formalization of the EIP. Greg says that there is no formal social process for deciding things like EVM 1.5 implementation so he is not sure if/when it would be implemented. Greg has been working on cleaning up the proposal for those who want to use it. Greg has some ideas around an EVM 3.0 that pulls everything together with transpilation that he hasn't started working on yet and is not sure if he will.

## [[20:14](https://youtu.be/biNCOCQdjQ0?t=1214)] 4. Stateless client development.
Piper left some comments about some development of a stateless client for sharding, but it is very early. Alexey had [a blog post](https://medium.com/@akhounov/how-to-speed-up-ethereum-in-the-face-of-crypto-kitties-7a9c901d98e9) describing stateless clients he may re-approach later. 

## [[21:46](https://youtu.be/biNCOCQdjQ0?t=1306)] 5. Add ECADD and ECMUL pre-compiles for secp256k1 - https://github.com/ethereum/EIPs/issues/603 [[See this blog post for context](https://medium.com/@clearmatics/privacy-on-ethereum-is-too-expensive-fb8b9e1815b2)].
This topic was brought up months ago with mixed commentary. Christian R. says that ECADD and ECMUL were never intended to be used for general purpose cryptography, but rather it was suppose to be used in conjunction with the pairing pre-compiles for a specific curve that is pairing friendly. Christian says that in the past it has been discussed that there must be a very compelling reason for adding a pre-compile to Ethereum. Silur mentioned that the Monero research team is working on a new ring signature (still unnamed) that can be viewed in the Monero repository. The EWASM team may run some tests to compare native running of the pre-compiles vs EWASM. Adding a new pre-compile would only give a constant speed-up or reduction in cost, but if we achieve the same thing in new virtual machine it will give us a constant speed-up for every conceivable routine and allows for building other schemes like Casper and TrueBit. This is easier with Web Assembly because we can use existing C code. For the moment it looks like focusing energy on adding these proposed pre-compiles would not be worth it compared to just waiting for the next VM (likely EWASM) which will allow far more speed-ups across all computational routines.

## [[37:00](https://youtu.be/biNCOCQdjQ0?t=2220)] 6. Introduce miner heuristic "Child pays for parent" (like in BTC) to combat the weird cases when transactions with 1000 Gwei stuck in the mempool (because they are dependent via nonce on transaction paying much less and not getting mined).
[Note: I tried my best to cover what was discussed here, but I am not an expert in Ethereum transactions. If you find a mistake please point it out to me. Thanks!]
Agenda item brought up to get people's opinion on this topic. Currently in Ethereum there are transactions that are stuck in the mempool for a long time because of the way transaction ordering per account is handled. The nonce of a transaction must be greater than the previous mined transactions (or equal if you are trying to replace a transaction). For example you can't process transaction #27 before transaction #26 has been mined. Many of the stuck transactions are dependent on other transactions that pay a much smaller fee, but are not being mined. It seems people inadvertently send an initial transaction with too small of a fee and then more transactions at a higher nonce with a much higher fee that cannot be processed until the first small fee transaction is processed. Alexey wondered if this may pose an attack vector or if we would get a benefit from implementing "child pays for parent" like Bitcoin does. Peter explained even if you define the max amount of gas your transaction could potentially consume, there is no guarantee it will use that much and we won't know until the transaction is processed (the only guarantee is that 21,000 gas will be consumed - a plain ether transfer). The attack vector example would be someone pushing a transaction that truly consumes 3,000,000 gas and attach a transaction fee of 1 wei and then push another TX that claims to consume 3,000,000 gas but with a transaction fee of 1000gwei. From the outside it looks like I can both can be executed for profit from the miner's perspective, but in reality the 2nd transaction will be processed first and the 1st tx will be long running and indirectly punish the miner. Alexey was concerned about the mempool filling up and impact on clients due to the way nonces are handled. Peter clarified that transactions in the mempool in the go ethereum client only maintains the top 4,000 most expensive transactions. If your cheap transaction gets evicted, the expensive transactions you stacked on top of it get evicted as well because they are no longer executable due to the nonce.


## [[42:21](https://youtu.be/biNCOCQdjQ0?t=2541)] 7. Creating a relay network of nodes to mitigate issues [described here](https://github.com/ethereum/pm/issues/29#issuecomment-356952590) and [other transaction propagation issues](https://github.com/ethereum/pm/issues/29#issuecomment-357151890).
A relay network in general is a group of peers and/or miners who use a peer list to quickly connect to a group of known peers before connecting to (or instead of connecting to) random peers using network discovery. Alexey conjectured that this may create a powerful ring of network players who can share transactions very quickly and hurt the little guys on the outside (hurting the idea of this being a mesh network of peers). Clarifications were made about the issues involving transaction propagation issues with nodes with high transaction throughput such as Infura and Bittrex. Clients suddenly stop pushing transactions or cannot keep up with the blockchain when they are pushing out so many transactions. Hudson will work towards exploring this issue more and connecting the people with the issues with the devs. 

## [[49:45](https://youtu.be/biNCOCQdjQ0?t=2985)] 8. Fork release management/Constantinople.
Hudson will be working on writing up a starting plan to discuss potential release management issues. BitsBeTripping sent Hudson some good material about project management that he will review and bring to the next meeting. We need to start discussing Constantinople sooner rather than later.

## [[52:55](https://youtu.be/biNCOCQdjQ0?t=3175)] 9. Client updates.

- geth - Improved tracing APIs so people can write their own JavaScript tracers. Event and subscription Go wrappers are also coming along (they are similar to the Go wrappers you can generate for contracts when entering the Solidity code or ABI). Geth performance improvements are a major focus including a scheme to reduce disk IOIs database writes by about 60% (first proposed by Nick) which will help your disk fill up 1/3 as fast (will not help improve sync time from scratch). Also looking at some garbage collection ideas which reorganizes the database. The issue is that it may clash with fast sync. They want to design a solution that doesn't mess with, or in coordination with other clients update, fast sync. They are also fixing a memory issue that happens during sync.
- cpp-ethereum - Andrei is working on snapshot imports. Fixes and updates to EVM-C to make EWASM integration easier.
- Parity - No one available to give an update.
- Harmony - Started to work on Casper implementation and working on performance improvements. There are some unexpected difficulties. Database improvements will come first, then the next release should reduce memory footprint and improving processing speed. No estimates yet on the next release, but database improvements are #1 priority.
- ethereum-js - No updates. Entire ethereum-JS team focused on EWASM currently.
- pyEVM - No one available to give an update. Piper left a text update: Implementation of full node sync in pyEVM is under way. Stateless client work is ongoing as is implementation of a simplified ethgasstation gas estimation algorithm is in progress for web3.py. Alpha release of pyEVM client is happening soon. Sharding and research development continues.
- TurboGeth - Plan is to experiment with optimizations in geth. Analysis to decrease the state size on the disk by decreasing the repetition of hashes in the stored state in ongoing. The goal is to store as much of the state as possible in memory. [[1:00:40](https://youtu.be/biNCOCQdjQ0?t=3640)] discusses this in more detail as well as some stats on full nodes. There is a blog post update

## 10. Other non-agenda items

### [[1:05:42](https://youtu.be/biNCOCQdjQ0?t=3942)] Question: Will we see any scaling improvements from Constantinople?
Answer is no because it potentially includes the first steps of the Casper consensus protocol and some account abstraction EIPs, but both of those do not alleviate scaling issues. Sharding would alleviate some of the issues. We are currently mostly bound by database and processing speed due to the database. Short term there are a lot of client improvements that can be accomplished to improve disk I/O, but long term things like sharding will be necessary. The Eth Research site has a lot of interesting threads about sharding including merkle tree formats to be used and ideas around asynchronous accumulators

### [[1:09:57](https://youtu.be/biNCOCQdjQ0?t=4197)] Decision process for EIPs?
Needs to be improved. Hudson and others will work on updating EIP #1 and other improvements in Q1. Nick Savers has been added as an EIP editor. Yoichi has been added as an editor. Both are doing a great job.

## Attendance

Alex Beregszaszi (EWASM/Solidity/ethereumJS), Alex Van de Sande (Mist/Ethereum Wallet), Alexey Akhunov (Turbo Geth), Ben Edgington (Consensys/Pegasys), Casey Detrio (Volunteer), Christian Reitwiessner (cpp-ethereum/Solidity), Daniel Ellison (Consensys/LLL), Greg Colvin (EVM), Hudson Jameson (Ethereum Foundation), Hugo de la Cruz (ethereumJS/EWASM), Jake Lang (EWASM), Jared Wasinger (ethereumJS/EWASM), Martin Becze (EWASM), Mikhail Kalinin (Harmony), Paweł Bylica (cpp-ethereum/EWASM), Péter Szilágyi (geth), Silur (ethereumJS / EWASM)
