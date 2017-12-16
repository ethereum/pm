# Ethereum Core Devs Meeting 29 Agenda
### Meeting Date/Time: Friday 12/01/17 at 14:00 UTC
### Meeting Duration: 1 hour
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/27)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=1GulA7iA-O0)

# Agenda

1. Testing Updates
  a. Fuzzer updates.
  b. [New transaction tests folder structure.](https://github.com/ethereum/tests/tree/gentransact/TransactionTests)
2. [Shall we require CC0 notices in EIPs?](https://github.com/ethereum/pm/issues/27#issuecomment-348181284)
3. New Project: JSON RPC Proxy / eth-agent
  a. Discussion: https://github.com/ethereum/cpp-ethereum/issues/4563
  b. Proof of Concept: https://github.com/chfast/json-rpc-proxy/releases/tag/v0.1.0a1
4. [Does it remain the case that the Yellow Paper is intended to be Ethereum's formal specification?](https://github.com/ethereum/pm/issues/27#issuecomment-347997598)
5. POA Testnet unification [Update]
6. Core team updates.

# Notes
Video starts at [4:03](https://youtu.be/1GulA7iA-O0?t=243)

## [[6:05](https://youtu.be/1GulA7iA-O0?t=365)] 1. Testing Updates

### a. Fuzzer updates
Go and Rust clients can work with it and Guido is working on integrating cpp-ethereum. Guido is also working on a bignum fuzzer to make sure bignum libraries are aligned across the clients. Smart contract fuzzing has been discussed, as has fuzzing the network stack, but it has not started yet.

### [[8:56](https://youtu.be/1GulA7iA-O0?t=536)]  b. [New transaction tests folder structure.](https://github.com/ethereum/tests/tree/gentransact/TransactionTests)
There have been changes to the transaction tests to help organize it better and be more representative of the different categories. More technical detail in the call.

## [[11:00](https://youtu.be/1GulA7iA-O0?t=660)] 2. [Shall we require CC0 notices in EIPs?](https://github.com/ethereum/pm/issues/27#issuecomment-348181284)
We agreed that the requirement for CC0 notice should be made going forward. Yoichi made a pull request on EIP 1 to change that. Existing EIPs that do not have the copyright will need to change and we can create PRs for them that they just have to give written permission to change.

## [[35:10](https://youtu.be/1GulA7iA-O0?t=2110)] 3. New Project: JSON RPC Proxy / eth-agent
  a. Discussion: https://github.com/ethereum/cpp-ethereum/issues/4563
  b. Proof of Concept: https://github.com/chfast/json-rpc-proxy/releases/tag/v0.1.0a1
cpp-ethereum components are being separated into separate projects. Components that are not required to run an Ethereum node may be split from the core cpp-ethereum code. The first component to be split off are the HTTP server that is in the client. The JSON RPC proxy can sign transactions for you which acts like an account management component in a way. An update to EthStats which moves it to the shared tooling projects may also be in the works soon.

Separating the account management from the client will help lessen the security overhead of the Ethereum node operators. geth is planning on slowly moving away from account management and Martin is working on an account management tool with a public API that doesn't take passwords. It instead requires interaction with a custom UI and sending remote transactions to the tool.

## [[14:56](https://youtu.be/1GulA7iA-O0?t=896)] 4. [Does it remain the case that the Yellow Paper is intended to be Ethereum's formal specification?](https://github.com/ethereum/pm/issues/27#issuecomment-347997598)
Ben brought up some questions (linked in the title) about the future of the Yellow Paper and it's place as the official specification for clients.

Ben's questions:
> Question: does it remain the case that the YP is intended to be Ethereum's formal specification?
> 
> If yes, then it should be noted that the YP is currently significantly out of date.
> 
> a. What is the plan for bringing the YP up to date post-Byzantium?
> 
> b. What is the process and ownership for maintaining the YP going forward?
> 
> c. Should updating the YP be made part of the EIP finalization process?
> 
> d. To facilitate c., Should EIPs be required to include a pull request to the Yellow Paper (if relevant) before they are accepted?
> 
> e. When consensus failures are discovered (e.g. during the recent fuzz testing), how can we make sure that the YP is updated where necessary?
> 
> If no,
> 
> a. What replaces the YP as the authoritative specification of Ethereum?
> 
> b. Is the YP worth maintaining as a resource that is descriptive rather than prescriptive? If so, the questions above still stand.

Having changes to the Yellow Paper or other formal spec. be merged before certain EIPs are accepted is a good idea.

Gavin Wood maintains the [Yellow Paper](https://github.com/ethereum/yellowpaper) and there are a list of contributors to the Yellow Paper on GitHub. The Yellow Paper doesn't have a copyright which opens up some confusing legal issues for those wanting to fork the Yellow Paper or make unofficial changes that are not merged by Gav. Biggest concern is it is unclear who can legally merge pull requests without legal concerns being attached. There are currently pull requests for the Yellow Paper to bring it up to date.
The Yellow Paper isn't a complete specification of everything needed to build a client and some expressed opinions that the Yellow Paper is difficult to read. [KEVM](https://github.com/kframework/evm-semantics) is a formal specification written in K that can be execute test cases that may be a candidate to replace the Yellow Paper. KEVM is licensed under UIUC/NCSA License. Afri is going to reach out to Gavin to ask about updating and licensing the Yellow Paper include him in this conversation.

Piper suggested having a developer grant for a group that keeps the Yellow Paper or other formal spec. up to date. Currently Dev Grants (Ethereum Foundation grants program) is not active, but may be active in the future.

## [[43:24](https://youtu.be/1GulA7iA-O0?t=2604)] 5. POA Testnet unification [Update]
No updates.

## [[43:51](https://youtu.be/1GulA7iA-O0?t=2631)] 6. Core team updates.
- Parity - Working on release 1.5. No major new features. Mostly working on stabilizing stuff. Improvements on database layer are also happening, specifically replacing the database layer with a new type of database. They are working on Parity multi-sig issue and preparing a list of different approaches on how we can address the problem. They will present a list of proposals at the next core dev meeting. "We will discuss them with the community and see where it goes from there."
- geth - New release with no major changes. Working on improving the block tracing.
- cpp-ethereum - Still is post-Mexico mode from Devcon3. Mostly cleaning up some stuff from the Byzantium hard fork. Yoichi has been going through and updating EIPs. Discussion is ongoing with Pawel and Andrei about a roadmap for features. Dimitry has been updating the testing framework. Shout out to Martin H.S, cdetrio, Guido, and other who are contributing to the fuzzer framework
- Harmony - Migrated client to RocksDB. Work is basically complete on making Harmony compatible.
- ethereum-js - No updates.
- pyEVM - Big GitHub migration from Piper's GitHub to Ethereum Foundation's GitHub. Repos have been re-named to make it more clear what each one does. Pretty far along with implementing the light client protocol. Early alpha release of the client (currently called Trinity) expected in the next month. Integration with Hive and JSON-RPC specs are still left to do. The research team is working on moving their Casper implementation to pyEVM.
- pyethapp - There is Casper research testnet utilizing pyethereum.
- EWASM - Roadmap has been created. Aim to launch a preliminary testnet by the end of January.
- Solidity - Release made the day before that had some improvements including fully implemented ABI encoding/decoding (will require specifying experimental release in the header). Really focusing on the SMT solver in Solidity for the next release.

Martin H.S mentioned that there is someone working on a C# Ethereum client that is passing almost all state tests and VM tests. Estimates are that it will be complete in a couple of months. At this point it is still in a private repository, but if people want to help out reach out to Martin and he will connect you.

## Attendance

Afri Schoedon (Parity), Alex Beregszaszi (EWASM/Solidity), Anton Nashatyrev (ethereumJ), Christian Reitwiessner (cpp-ethereum/Solidity), Dimitry Khokhlov (cpp-ethereum), Hudson Jameson (Ethereum Foundation), Lefteris Karapetsas (Raiden), Marek Kotewicz (Parity), Martin Holst Swende (geth/security), Nick Johnson (geth), Paweł Bylica (cpp-ethereum), Piper Merriam (pyEVM), Yoichi Hirai (EVM)
