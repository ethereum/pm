# Ethereum Core Devs Meeting 39 Notes
### Meeting Date/Time: Fri, June 1, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/43)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=7FNRWEQ_H7w)

# Agenda

1. Testing & EIP 1085: Common genesis.json format scheme across all client implementations
1. Client Updates
1. Research Updates
1. EIP 1087: Net gas metering for SSTORE operations
1. Concerns that using native browser VMs for running eWasm is not DoS hardened. See this comment and this comment.
1. Constantinople hard fork timing and what to include (continuing conversation from last call).
1. Testnet rent. See this comment.

# Notes

Video starts at [[]()].

## Testing
* EIP 1085
    * We need a dedicated person to work on this
    * Everett to contribute as he's been doing similar work lately
    * I'll go with schema in PR and it can be modified as we go
    * Everett to start with schema and PR and we'll iterate on it in Gitter
    * Question about gas costs and filling tests per client
* Started working on blockchain tests via RPC
    * eth_get block by hash method
    * Needs block sig and tx sig
    * Currently methods export tx without those signatures
* First goal is the genesis standard

## Client updates
* Parity (Fred)
    * No real update, no major release
    * Casper testnet in the works, not permanent, just something to play around with
    * Reach out if you want to check that out
* Geth (Martin)
    * Latest two releases fix issues around tx
    * Memory bloat and races which made the client lock up
    * Peter is doing some interesting work re: his memory pruning of the state, implemented streaming memory pruner which performs a lot better, really tangential to other work he's doing, new protocol for fast sync that he's experimenting with, we have high hopes for that
    * Hoping to make good progress in the next month or so
* cpp-ethereum (no one present)
* Harmony (Mikhail Kalanin)
    * Prepared RC version, now working on new release to occur in ~2 weeks
    * Reads faster by 5-10x
    * Stability: we had to protect against eclipse attacks happening on the main network
    * Reduced memory footprint
    * This version is more stable, able to run on mainnet without needing restarts
    * Martin: have you seen evidence of eclipse attacks on mainnet?
    * Mikhail: yes, many connections from same IP, 50 addresses I've noticed with connections from a lot of different ports, they do nothing, no handshake, this looks like a primitive eclipse attack
    * We didn't count bytes in RLP before allocating memory, could've had an array of length 10gb, this is another kind of attack
* PegaSys: no one present
* Trinity (Danny)
    * Released an alpha
    * Focused on performance, fixing bugs causing crashes
    * Expect nodes syncing to 
* Nimbus (Jacek)
    * Need to develop bigint support, cryptography
    * Networking
    * Enjoying enthusiastic support from nim community
    * Produced a number of libraries that supply base components
    * Working on EVM, appreciating test suites
    * Working on devp2p framework, starting to implement wire protocols to enable us to start syncing the chain soon

## Research updates

* Research (Danny)
    * Casper
        * Iterating, working through some finer details around executing tx in parallel, handling tx queue
        * Opening up some more helper functions to allow client to get more info
        * Hopefull getitng a testnet with more than just parity in next few weeks
    * Sharding
        * Justin Drake and Vitalik have a series of posts around signatures and beacons on https://ethresear.ch
        * Some exciting new developments, check it out
* ewasm (Alex)
    * Shifting focus from evm2wasm to parts more important for a testnet
    * Brand new testnet, with both EVM and ewasm enabled with cpp-ethereum
    * Changing existing testnets would mean updating all existing clients
    * Ropsten, Rinkeby mostly on geth, and we don't support geth yet
    * Hopefully shortly after that we can add geth as well
    * Fred: curious to hear what it would take for Parity to join that testnet
    * Danny: what's `evm2wasm`?
        * Alex: Can be fed with EVM bytecode and outputs ewasm bytecode
        * Is that an attempt to port entire EVM over to ewasm?
        * Alex: That's one possible use. We've mainly been using it to run ethereum state tests. Also, if someone implements a client from scratch and make it a native ewasm client, they wouldn't need an EVM implementation, they could use this tool to translate contracts before execution.
        * It's a big project and passing quite a few tests
        * Was written two years ago, 90% passing Frontier tests but the network has evolved a lot
        * Plan to open it to the public and let them help with passing state tests
    * Jacek: Question about using this in a new client like ours--if we wanted to go ewasm only what sort of problems could arise?
        * Alex: evm2wasm tool isn't finished yet, cannot just use it to run all contracts. It can run a subset of contracts and we do plan to get it to a point where you can run many types of contracts.
        * We need a lot of help in finishing it up, don't see any other main issues
    * Jacek: What about attack vectors/security concerns?
        * Alex: Compiler is like x86 output
        * As of today, follows EVM gas costs 100% same as EVM
        * This tool itself should be compiled into WASM and metered so when you execute it you would have an upper bound of time to run translation
    * Greg: Does evm2wasm intend to be an optimizing compiler that can take the end code down to 32 and 64 bit registers or whether it will keep doing everything with multi precision?
        * Alex: It does everything as current EVM requires, so uses 256 bit stack items
        * Greg: So optimization is pushed down to the WASM compiler
        * Alex: We can do optimiziations, and it should be possible to implemented SIMD extensions and EVM 1.5 as well
        * If it can detect EVM input it can optimize entire output to 64 bits, interesting idea to explore in the future

## EIP 1087
* Nick Johnson not present, skipping for now

## Concerns about wasm
* https://github.com/ethereum/pm/issues/40#issuecomment-390006104
* https://github.com/ethereum/pm/issues/40#issuecomment-390114286
* Casey update
    * https://github.com/ewasm/design/pull/99
    * Greg has been reminding the ewasm team continually while the team has been focused on building the interpreter so I opened a PR on ewasm design repo with an overview of how we understand the JIT compilation issues
    * There are two ways to execute code, AOT or JIT, interpreted vs. compiled
    * Everett feels there is no difference
    * Paul points out that there are two orders of magnitude difference in execution speed
    * The reason it's important is that if we're going to allow one use case to allow users to deploy their own precompiles - it will only work if ewasm gas costs are calibrated to native execution speed not to interpreter speeds
    * Benchmark we did is EC-pairing precompile
        * 23 seconds using interpeter
        * JIT compiler: 100ms
    * We were kind of hoping optimistically that V8 (WASM JIT engine in chrome and node)
    * Because validation pass is linear we were hoping that the JIT would also have a linear time upper bound
    * Finally a couple of weeks ago when we tried to reach out and ask various JIT experts, no one could give a confident answer on whether or not there would be a DoS attack
    * Guido Vraken hooked up a fuzz tester to V8 and found some compiler bombs, 20kb pieces of WASM, even smaller than the current maximum contract size you can deploy on the mainnet for EVM which is 32kb
    * Took about 2sec to instantiate and compile in V8
    * You can see highly nested loops and features that might trip up the JIT compiler
    * Greg you were right, so now we know for sure that it's a problem and we're thinking about potential approaches to mitigate
    * Besides using a JIT, the other solution often discussed is using an AOT compilation
    * I've been skeptical of that because to me AOT sounds like a big pain since client instead of maintaining a state tree where it pulls EVM bytecode and interpret it, it maintains a cache directory of EXE files, one per contract, that it executes when a contract is called
    * Sounded difficult to me but Paul explained how AOT might work
* Paul
    * Trained in math, working on a grant from EF on pywebassembly
    * Take LLVM, compile it to WASM
    * Use metered LLVM compiler toolchain to compile to X86 and ARM binaries, add support for others in the future
    * Meter that compilation
* Greg
    * The issue is that WASM is set up so that you can traverse it in linear time
    * So you can run compiler optimization in n log n
    * Most compilers don't do that, they go quadratic
    * So you can write a good WASM compiler that stays n log n, people not doing that since it's not a requirement for a web page, if a web page goes wonky, the web itself stays fine
    * But when a contract goes wonky it's a security hole
    * So I don't see any real answer except that someone must write bomb-proof WASM compilers that we can run AOT
    * In C++ it's a trivial change in one file to move the spot where the code is compiled by the JIT to the spot where the code is first loaded, take output of compiler and stick it into the existing state database, pull it out and run it when needed
    * The big deal is getting our hands on a bomb proof WASM compiler
    * Given that the foundation has a lot of money, I don't see why financing that effort would be a problem
* Paul
    * Firefox had a one pass compiler from WASM to binary, in the background did Ion optimization
    * Maybe we can use this, keep executing single pass version
    * Another solution, I might be interested in writing a WASM to binary compiler
* Fred
    * Parity also has great interest in writing one of these compilers
    * browser has reasons to do crazy optimization at WASM level, we can push this to the user
    * Expect people to output optimized WASM code
* Greg: When you have a smart contract that's responsible for hundreds of millions or billions of dollars and it's a tiny piece of code there's no reason not to put lots of resources into it
    * Write incredibly efficient bytecode and look for something like an old C compiler that does an almost 1-to-1 compilation
* Fred: That's what we'd be looking for at Parity
* Greg: WASM was designed for fast-streaming compilers
* Casey: Then why are there vulnerabilities in standard WASM JIT engines?
* Fred: Because they're trying to do a bunch of magic optimizations to make low-performance crappy code run faster
* Casey: Would be nice from our perspective if these off the shelf compilers had a flag to do 1-to-1 compilation and not fancy stuff that opens you up to compilation bombs
* Greg: I don't trust third party code, find something open source or write it ourselves.
* Fred: I also don't think it's that massive of a job, we could have multiple implementations of this and not be too encumbered.
* Paul: As someone who is implementing the WASM spec, it's a lot of details, so I think way more than two weeks.
* Fred: We also wrote an interpreter, it was a lot of work but not that much more work than writing an EVM interpreter.
* Casey: How about compiling WAVM or LLVM to WASM and then using it as a bomb sniffer?
* Greg: Bomb sniffer is a terrible idea, there's too many ways to slip code past the sniffer, e.g. finding VMs that the sniffer doesn't do a good job on or some version you weren't aware that some client was using
* Casey: This is no different than DoS vulnerabilities if someone implements a crappy EVM on the mainnet
* Greg: These definitely exist, we're lucky a truly focused group of hackers hasn't tried to take us down yet
* Paul: Parts of the spec are left to the implementation, compilation time is one thing but there are others e.g. how the branching, control flow implemented, how to escape from a trap, I made a list
    * A lot of implementations deviate from the spec
    * Async execution which would be unusable for us
    * Resource exhaustion
    * Non-deterministic behavior
    * And that doesn't include hardware bugs when we're close to the hardware level
    * If someone knows how it will compile then they may trigger a hardware bug
* Casey: What's the easiest path to enabling users to deploy their own precompiles?
* Paul: Easiest is to use off the shelf software, safest way is to AOT/JIT compile and check all the things in the spec, all of our concerns, identify attack vectors, make sure gas is set correctly
    * Using off the shelf may have security concerns
    * https://github.com/poemm/WasmSecurityConcerns
* Greg: this requires a reasonably bomb proof system, we can't make it perfect but we can make it good and be prepared to deal with DoSes when they happen

## Constantinople hard fork timing
* Meta: https://eips.ethereum.org/EIPS/eip-1013
* Shifting
* Blockhash refactoring
* Skinny CREATE2
    * https://github.com/ethereum/EIPs/pull/1014/files
    * Allows counterfactual contracts
    * Came up two calls ago
    * There is an EIP
    * Hasn't come up since then
* Timing
    * Martin: Would like to see a hardfork this year
    * Not sure

## Testnet rent
* https://github.com/ethereum/pm/issues/43#issuecomment-390959920
* You can limit storage in one contract but user can create multiple contracts
* Need a solution for blockchain rent
* There are a couple of proposals
* Fred
    * I've spoken a lot with Phil Daian about rent topic
    * Latest model is that you set some gas amount, cost per time unit for keeping the data in state
    * Every user who makes a tx to this contract would pay to top up the contract's lifetime to five years
    * When you deploy you get five years, any user who interacts pays to top up to five years
    * If a contract is used a lot you'd pay a super small fee to top it up
    * If no one uses it for five years it gets removed from state, costs five year fee again to reinstate it
    * Low overhead on users
    * Only effect is that things cost a little more
    * One more consensus-critical dataset to maintain for client developers, whether or not something is in state
* Would be nice if this could be turned into an EIP and tested on the testnet
* Casey: Stateless clients would also solve this and might be easier to implement relative to storage rent
* Fred: Phil would argue that it doesn't solve the problem and that you're moving the cost to the witness generation procedure, that data still has to be somewhere
* Everett: storage rent would give us a way to forget old parts of the blockchain which would be nice
* With stateless clients user has to supply data of account they're calling into
* Everett: my goal would be to evolve the EVM over time and the only way to do that would be to forget old parts of the blockchain

## Attendees
* Alex Beregszaszi
* Paul Dworzanski
* Everett Hildenbrandt
* Zixuan Zhang
* Lane Rettig
* Mikhail Kalanin
* Martin Holst Swende
* Greg Colvin
* Fredrik Harrysson
* Daniel Ellison
* Jacek Sieka
* Danny Ryan
* Casey Detrio
