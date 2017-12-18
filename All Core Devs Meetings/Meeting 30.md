# Ethereum Core Devs Meeting 30 Agenda
### Meeting Date/Time: Friday 12/15/17 at 14:00 UTC
### Meeting Duration: 1 hour
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/28)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=naPA7tjrgsk)
### [Reddit thread](https://www.reddit.com/r/ethereum/comments/7jxtex/live_stream_in_8_hours_ethereum_core_devs_meeting/)

# Agenda

1. Testing Updates.
2. Digital cats caused network congestion this month. Meow.
  a. Why did this happen and what solutions are available to prevent future network congestion? See comments below for some ideas.
  b. [Stateless Clients proposal](https://github.com/ethereum/pm/issues/28#issuecomment-349676284).
  c. [Would having minimum system requirements to set up an optimal client/full node help?](https://github.com/ethereum/pm/issues/28#issuecomment-351141485)
  d. [Is the bottleneck is not just disk bandwidth, but specifically sequential disk bandwidth? ](https://github.com/ethereum/pm/issues/28#issuecomment-351350231)
  e. [Vitalik has some ideas around gas cost changes and scalability-relevant client optimizations.](https://github.com/ethereum/pm/issues/28#issuecomment-350941632)
3. [Plans on Quantum-resistant cryptography and any plans to include it in the next update?](https://github.com/ethereum/pm/issues/28#issuecomment-350954470)
4. [Introduction to K-EVM team (Everett H.)](https://github.com/kframework/evm-semantics)
5. [Does it remain the case that the Yellow Paper is intended to be Ethereum's formal specification?](https://github.com/ethereum/pm/issues/27#issuecomment-347997598)
6. [Parity stuck ether proposals](https://paritytech.io/blog/on-classes-of-stuck-ether-and-potential-solutions-2.html).
7. POA Testnet unification [Update]
8. Core team updates.

Please provide comments to add or correct agenda topics.

# Notes
Video starts at [[]()].

## [[00:33](https://youtu.be/naPA7tjrgsk?t=33)] & [[22:37](https://youtu.be/naPA7tjrgsk?t=1357)] 1. Testing Updates
Yoichi is doing some clean-up of Byzantium test cases. Dimitry is currently working on changing the test source format into YAML. Final tests will still be JSON, this only affects the test source. Those who write tests can use YAML and use multi-line contract source code and write comments.

## [[1:12](https://youtu.be/naPA7tjrgsk?t=72)] 2. Digital cats caused network congestion this month. Meow.

### [[1:22](https://youtu.be/naPA7tjrgsk?t=82)] a. Why did this happen and what solutions are available to prevent future network congestion? See comments below for some ideas.
The gas limit was 6.7 million and crypto kitties used 1-2 million gas per block worth of demand. Usage pushed the transaction fees higher due to demand. Miners upped the gas limit a bit, but usage has grown even more and we are now at an 8 million gas limit and blocks are basically full.

### [[2:20](https://youtu.be/naPA7tjrgsk?t=140)]b. [Stateless Clients proposal](https://github.com/ethereum/pm/issues/28#issuecomment-349676284).
[Alexey Akhunov](https://github.com/AlexeyAkhunov) [described a stateless protocol design](https://medium.com/@akhounov/how-to-speed-up-ethereum-in-the-face-of-crypto-kitties-7a9c901d98e9). Vitalik has [been pushing the stateless protocol paradigm](https://medium.com/@VitalikButerin/regarding-bandwidth-requirements-for-stateless-clients-i-can-give-some-precise-numbers-be357fb69b6d) a lot because it is the direction they are looking at for sharding research. Stateless clients means that instead of the client storing the entire state the client would just store the state root and it would be the responsibility of the miners or transaction senders to package up with the block or the transaction the witness blocks. Witness blocks contain merkle branches that prove that all of the parts of the state required for processing all transactions in that block, and computing the next state root. Although this is theoretically viable, it would require a lot of substantial changes to gas costs and other factors [described here](https://medium.com/@VitalikButerin/regarding-bandwidth-requirements-for-stateless-clients-i-can-give-some-precise-numbers-be357fb69b6d). Other optimizations include the making it so we can access Patricia tree nodes in parallel and bumping cache sizes.
Low effort scaling solutions could potentially be included in Constantinople.

A complete discussion on these issues is [included here](https://github.com/ethereum/pm/issues/28).

### c. [Would having minimum system requirements to set up an optimal client/full node help?](https://github.com/ethereum/pm/issues/28#issuecomment-351141485).
Discussed tangentially in subsection b.

### [[24:12](https://youtu.be/naPA7tjrgsk?t=1452)] d. [Is the bottleneck is not just disk bandwidth, but specifically sequential disk bandwidth? ](https://github.com/ethereum/pm/issues/28#issuecomment-351350231).
Vitalik asks: Are random SSD reads parallizable? Would it take less time to perform 20 random reads than doing a single read? This may help with optimization to do multiple tree reads in parallel. Although it is not fully clear, it appears to be faster, but does it help with DBs like LevelDB? In theory it is likely fast, but in practice it depends on the DB and things like pre-loading the data into a cache or performing computations while pre-loading the data. In geth it may not make a difference because of the way LevelDB works. [Alexey Akhunov volunteered to do some benchmarks to answer some of these questions](https://github.com/ethereum/pm/issues/28#issuecomment-352021812).

### [[31:07](https://youtu.be/naPA7tjrgsk?t=1867)] e. [Vitalik has some ideas around gas cost changes and scalability-relevant client optimizations.](https://github.com/ethereum/pm/issues/28#issuecomment-350941632)
Main point: Vitalik thinks state reads are underpriced and pointed out some other scalability improvements that are quick wins.

> 1. Increase the price of blockchain reads.
> 2. [EIP 648: Parallelization](https://github.com/ethereum/EIPs/issues/648).
> 3. Two account destroying/dust clearing EIPs ([168](https://github.com/ethereum/EIPs/issues/168)/[169](https://github.com/ethereum/EIPs/issues/169)).

Martin HS wondered what the impact of increasing price on blockchain reads would have on the amount of gas used per block and fill up blocks more quickly. Vitalik says that he thinks the purpose of re-pricing is to improve the worst case rather than the average case. We still need to encourage devs to write their contracts better, but the more important thing is being pro-active about risks of actual attacks on the network. Risk of attack on the network is lower this year compared to last year. An attack that fills even a third of the block gas limit would end up making TX fees rise to $2 or more and burn through a million of dollars in a few days, but is still something worth being concerned about.

State channels are something that is a non-protocol, off-chain solution for scaling that Dapp developers should be paying attention to.

## [[35:52](https://youtu.be/naPA7tjrgsk?t=2152)] 3. [Plans on Quantum-resistant cryptography and any plans to include it in the next update?](https://github.com/ethereum/pm/issues/28#issuecomment-350954470).
Account abstraction is not "necessary", but there isn't really a point on creating a single quantum proof algorithm, but using account abstraction would make it more general and what they are using for Casper. There is [an Ethereum Research thread going on talking about the tradeoffs in account abstraction that needs more commentary](https://ethresear.ch/t/tradeoffs-in-account-abstraction-proposals/263).

## [[38:32](https://youtu.be/naPA7tjrgsk?t=2312)] 4. [Introduction to KEVM team (Everett H.)](https://github.com/kframework/evm-semantics)
Everett Hildenbrandt, Daejun Park, and Phil Daian gave introductions to themselves and KEVM.

KEVM is a formalization of the EVM in the K language. K is an operational semantics framework that gives you a bunch of software dev tools once you formalize your language in K. KEVM is executable and testable so it can generate and pass state tests. It can be eventually used to generate test cases by the specification rather than by a client such as cpp-ethereum. Some experimental prototypes to extend the EVM with some high-level languages have occurred, most recently Daejun has been helping a lot on the semantics of Viper. Goal is to provide some formal tools for the Viper language which involves formalizing the Viper language on top of KEVM (translating the Python version of Viper into a mathematically definition in K). A number of tools are created from this formalization of Viper including proving compiler correctness and migration of Solidity contracts into Viper using bytecode comparison. More information is included in [this blog post](https://runtimeverification.com/blog/?p=617). Additionally there has been work on compilation from KEVM to a web based and human readable documentation of the KEVM semantics. It is meant to be like the Yellow Paper, but it can be fully compiled into a full implementation of the EVM. It is called "The Jello Paper" and [can be found here](https://thehydra.io/evm/). The KEVM project is split across two entities: The University of Illinois (U.S) and Runetime Verification Inc.

## [[47:12](https://youtu.be/naPA7tjrgsk?t=2832)] 5. [Follow-up: Does it remain the case that the Yellow Paper is intended to be Ethereum's formal specification?](https://github.com/ethereum/pm/issues/27#issuecomment-347997598).
Ben Edgington from Consensys's Pegasys protocol engineering team and Daniel Ellison from Consensys who has been working on LLL and language research introduced themselves.

Afri reached out to Gavin about the Yellow Paper and Gavin said he would be happy to place the Yellow Paper under a Creative Commons license. He hadn't done it yet because he has been busy, but will find time in 2 weeks to do it. The topic was brought up of the possibility of having more than 1 formal specification for Etheruem. KEVM is testable and executable so if there were to be another executable or testable specification you could check interoperability between two specifications, but currently there is a not a way to do this with the Yellow Paper. It would be possible to get a merge of the two specifications, combining elements, such as the English prose from the Yellow Paper with some of the elements of the KEVM. It isn't necessarily bad to have multiple specifications, but it would be bad to have it too fragmented. The first step for the Yellow Paper seems to be to apply a license so it can get up-to date. The KEVM team is interested in moving KEVM to Ethereum Foundation ownership.

## [[57:36](https://youtu.be/naPA7tjrgsk?t=3456)] 6. [Parity stuck ether proposals](https://paritytech.io/blog/on-classes-of-stuck-ether-and-potential-solutions-2.html).
No official/formal statement today, but Parity has heard the community feedback loud and clear.

## [[58:27](https://youtu.be/naPA7tjrgsk?t=3507)] 7. POA Testnet unification [Update]
No updates.

## [[9:29](https://youtu.be/naPA7tjrgsk?t=569)] 8. Core team updates.

- Parity - Parity is replacing RocksDB with a custom database layer called "ParityDB". Attempts to optimize RocksDB over the last 6 months proved to not be fruitful so they are making the switch. More information on that can be found on their GitHub. We are having some problems keeping up with mainnet, but are working to fix that.
- geth - Nick has been working some potential improvements to not write as much to disk with the idea to keep the state diffs of the last 100 or so blocks in memory (similar to Parity) which would raise memory requirements, but decreases disk I/O. geth is exploring other database solutions and so far hasn't found any silver bullet DB replacement. Although doing some optimizations like disabling the background miner would help, there are some people who rely on the "pending state" details that the miner enables for APIs.
- cpp-ethereum - No major updates. Work in progress on refactoring the database layer to easily swap databases and enable optimizations. Recently implemented a script to proxy HTTP RPC request to IPC sockets in order to get rid of the HTTP server in the client. This code can be used with other clients. Improvements have been implemented in the CLI.
- ethereum-js - No updates. Looking forward to EWASM testnet. Lots of maintencance and merging of PRs.
- Harmony - Database layer is almost done being moved from LevelDb to RocksDB. Created a new pruning mechanism. Soon will focus on the Casper testnet.
- pyEVM - No major updates. Getting closer to major alpha release.
- pyethapp - No updates.

**NOTE: The next core dev meeting will be January 12th due to the holidays. [Agenda is located here](https://github.com/ethereum/pm/issues/29).**

## Attendance

Afri Schoedon (Parity), Alex Beregszaszi (EWASM/Solidity), Alex Van de Sande (Mist/Ethereum Wallet), Andrei Maiboroda (cpp-ethereum), Anton Nashatyrev (ethereumJ), Ben Edgington (Consensys/Pegasys), Casey Detrio (Volunteer), Christian Reitwiessner (cpp-ethereum/Solidity), Daejun Park (KEVM), Daniel Ellison (Consensys/LLL), Dimitry Khokhlov (cpp-ethereum), Everett Hildenbrandt (), Hudson Jameson (Ethereum Foundation), Jared Wasinger (ethereumJS and Testing), Jutta S (), Lefteris Karapetsas (Raiden), Marek Kotewicz (Parity), Martin Holst Swende (geth/security), Mikhail Kalinin (Harmony), Nick Johnson (geth), Paweł Bylica (cpp-ethereum), Péter Szilágyi (geth), Philip Daian (), Piper Merriam (pyEVM),  Vitalik Buterin (Research), Yoichi Hirai (EVM)
