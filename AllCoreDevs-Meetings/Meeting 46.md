# Ethereum Core Devs Meeting 46 Notes
### Meeting Date/Time: Fri, September 14, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/56)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=TafZui-DnV0)

# Agenda

1. Testing
1. Client Updates
1. Research Updates
1. [Constantinople](https://github.com/ethereum/pm/issues/53)
    a. Client progress.
    b. Ropsten block number.
    c. Can we do it before Devcon?
1. EIP-1380: Reduced gas cost for call to self
1. EIP-1108: Reduce alt_bn128 precompile gas costs
1. EIP-1057 (ProgPoW) and EIP-1355 (Ethash1a)

Call starts at [[1:36](https://youtu.be/TafZui-DnV0?t=1m36s)]

# Client updates
* Parity (Afri)
    * Constantinople: all EIPs implemented and merged, have tests
        * We can flip over in Parity and start testing
    * Considering replacing warp sync with hybrid client mode
    * Considering two- or three-stage client
        * Instead of starting to sync from genesis, you start immediately with a light client
        * Full sync in background
        * Or light -> warp sync -> then to full sync
        * All just ideas for now
        * We need to think about alternatives since the state is so big, even warp sync takes two hours
        * Also want to address removing ancient block sync, checking PoW, would like to see it replaced with a fully verifying sync node
    * Need to stabilize light client first
    * We have a light ETH wallet called Feather to do ETH or token transactions, in early alpha
        * Very light electron app
        * Desktop, web, phone
* geth (Martin)
    * Constantinople: Missing mining reward reduction, net SSTORE changes
        * Hoping we get these in the next couple of days
        * Otherwise ready, have run state tests in Constantinople mode
* Trinity (Piper)
    * Constantinople: Two outstanding issues
        * Issuance reduction, net SSTORE
    * Doing internal refactor to speed up sync process, looking at notable improvements
    * Improving performance numbers to allow syncing in a reasonable time
* aleth (Andrei)
    * Constantinople: finished all EIPs
        * Ready for Dimitry to generate tests
    * Fixed issue reported by Martin re: address collision when account is considered empty, zero nonce and no code, but still has non-empty storage (a theoretical case)
* Harmony/EthereumJ (Mikhail)
    * Constantinople
        * Net SSTORE
        * Skinny CREATE2 - implemented but not all tests passing
        * Difficulty bomb delay - will have by next week
        * Next step is testing
        * We'll be ready for the fork in the next 1-2 weeks
* Nimbus (Mamy)
    * Enabled general state tests, passing > 500
        * Several assume gas is UINT256 even though geth and py-evm use int64
    * Started working on some precompiles
        * For cryptography, looking into more test vectors for ALTBN128 curve
    * P2P: Now have better block downloads
    * Eth 2.0: We've implemented fork choice rule (old one), looking into integrating it into Beacon chain 2.1
* TurboGeth (Alexey)
    * Combined Net gas metering PRs into TurboGeth
    * Changed layout to support pruning in non-trivial way
    * When writing RPCs, been writing records in history with some duplication
    * Net gas metering helped me remove duplicates, which led to ~100G reduction in storage (archive mode)
    * Changed records to be reverse rather than forward diffs so I can easily implemement pruning (throwing away old history)
    * Looking into supporting warp sync, might want to make it Parity-compatible
    * Fixed most of RPC APIs: tx tracing, storage introspection, balances
    * Can see a big performance difference, e.g. tx tracing 10x faster than geth; storage introspection 100x faster
    * Tried to remove storage receipts to reclaim ~40G, at the moment it works on same OOM as geth restoring receipts from storage but a lot of time spent re-recovering sender from sig
    * TurboGeth is pretty much ready but needs some polishing
    * First real-life testing on Infura to begin in 1-2 weeks
* Ewasm (Alex)
    * Swappable VM called Hera, runs through EVMC interface, works with aleth
        * Also a fork of geth that works with this
        * Made significant progress in discussing this with geth team, hopefully will make it into geth soon
        * Supports multiple engines for executing Wasm: two interpreters, one JIT
        * Allows us to focus more on benchmarking, our next big focus, to benchmark precompiles
            * Benchmark all mainnet precompiles in Wasm against these three engines
            * Want understanding of performance between JIT and non-JIT engine
* EthereumJS
    * No update
* PegaSys
    * No update

# Research updates
* Vitalik update
    * Slow progress on polishing and refining Casper 2.1 spec and implementation
    * Considerable progress on Plasma but less related to core client dev
* Danny update
    * Eth 2.0 implementers' call
        * Done every two weeks on Thursdays, had one yesterday
        * Core devs are welcome to join
        * An effort to begin implementing beacon chain, developed in parallel to Eth 1.0 for the time being
    * Spec is solidifying, we are doing minor refinements and additions, no core rewrites
        * Now is a good time to familiarize yourself with the spec and make an informed decision on whether it's time for your team to begin looking at it
        * Happy to discuss architecture and design decisions with you if it would be helpful

# Testing update
* Hudson: Want to fork Ropsten to start Constantinople testing
* Geth, Parity, Harmony should be ready soon
* Dimitry update
    * Posted earlier today which test cases still missing
    * More coverage around extcodehash, storage changes
    * Don't have transition tests in the form of blockchain or difficulty tests for bomb delay
    * Fast eth converted into state test
    * Finished skinny CREATE2 tests
    * In repo, executing in Hive, found issues and discussed with Martin
        * All clients pass
    * If you have ideas please add new test cases
    * Regenerating all tests for Constantinople version, have to do this before each HF
    * Don't know how long it will take
* Martin update on Hive
    * It's running on geth, parity, aleth
    * There are quite a lot of failures
    * Emerick is looking at it on Parity, I'm looking at why geth is failing CREATE2
    * Not sure whether tests were generated correctly
        * 52 failures for geth
    * Fast testing: we have a large corpus from fuzz tester that are being implemented as state tests, will check into repo later
    * Dimitry: which format are these?
        * M: ready-to-run format, not generalized
    * Don't have lib fuzzer running but have EVM labs fuzzer running
        * Not switched over to Constantinople yet
        * I'm open to have fuzzer running early next week

# Constantinople
* [Progress tracker](https://github.com/ethereum/pm/issues/53)
* Constantinople testnet HF
    * Hudson: We wanted to launch Constantinople before DevCon
    * Could still be possible but don't want to push people too hard / be unsafe
    * Dimitry, how much more testing do we need before forking to Ropsten?
    * D: a couple of months at least, I still have a lot of tests to implement
    * Martin: Do we care if there's a consensus issue on Ropsten?
    * V: Consensus issues happening on ropsten from time to time is good, trains ecosystem how to react to them
    * Mamy: what if we break the workflow of Dapp developers building on Ropsten for DevCon?
    * Martin: they are more likely to use Kovan or Rinkeby, or a private net, as Ropsten has had issues for a long time
    * Piper: Should we retire the testnet and do the fork on a new testnet?
    * Hudson: For testing purposes do we care how many blocks come before the fork?
    * V: Benefit to forking on a chain with a bunch of activity
    * Alexey: it's a balancing act, we want some stability so users are happy and keep using your testnet
    * Afri: do we really want another PoW testnet?
        * I think we should test the new hard fork on Ropsten
    * Hudson: let's fork Ropsten in early October
    * Afri: block time on Ropsten is a little unstable so hard to target a specific day
    * Martin: Let's target Oct. 9 and set block number in two weeks
    * On mainnet block times
        * Average block time now steady under 15 s (https://etherscan.io/chart/blocktime)
        * We have at least half a year; could theoretically be 4-5 months before increasing block time starts to bite
        * When increasing, it would double roughly every 17 days
        * So fork could be November-December and we'd be fine

# EIP-1380: Reduced gas cost for call to self
* Axic update: this was a collaboration between Jacques (from Vyper team) and me
    * Vyper uses CALL for self-referential methods
    * A bit more costly than doing jumps
    * So people suggesting that Vyper switch to jumps
    * This EIP created as a response to that, since the way Vyper does it now is beneficial
    * With jumps, puts more work for memory safety on the compiler; this is not an issue with CALLs
    * Proposal: any kind of call (including delegate call, static call), if it goes to originating contract, then we charge less
    * Motivation described in EIP
    * What would be a rational gas cost?
    * Going back to before spurious dragon, 40 with 700 for any other case
    * But assumes spurious dragon increase was attributed to IO cost (which we're saving here)
    * Client still needs to create new context but IO cost is saved
* V: intuitively it seems a finer idea
    * Spurious Dragon de facto reduced max stack depth from 1024 to ~300
    * Incidentally I'd favor vyper not doing jumps because I feel there's value in having a language that values simplicity even at the cost of optimality
    * Idea of having languages where you have to have two distinct ways of calling contracts seems fairly suboptimal, seems a fine approach for mitigating it
* Piper: Seems inline with EIP for net SSTORE gas reduction
* V: Was there an EIP for reducing gas cost of CALL specifically for precompiles? For Constantinople
    * Alex: There are two EIPs for this but haven't been on the agenda for the past few calls
    * V: For simplicity it might make sense to merge these two at the same time
* Alex: Another proposal needs to be written up, Chris on Solc team suggested we can propose a way similar to net SSTORE metering that there'd be a map of contracts originating from a contract, no extra charge for loading an already-loaded contract
    * Yet to be designed or written but along the same lines
* Piper: I can see a lot of value in genericizing it
    * Concept of solc libraries is nice for some things but they do incur higher gas costs
* V: This could be genericized even further
    * Going as far as saying, gas cost for accessing an account already accessed in same block goes down from 700 to 40, potential to do this in the long term
* Hudson: these won't go into Constantinople but would go into the following HF, Istanbul
* Martin: Did you ever consider having a SELFCALL opcode? Why do this instead?
* Danny: let's discuss EIPs that could go into a future fork so we have some momentum towards it

# EIP-1108: Reduce alt_bn128 precompile gas costs
* Hudson: because geth reference implementation had large performance gains, it should be reflected in cheaper gas costs
    * But some issues where these gains weren't realized in other clients
    * Martin: a lot of ppl want these precompiles to have lower gas costs
        * We could lower it a bit

# EIP-1057 (ProgPoW) and EIP-1355 (Ethash1a)
* Hudson
    * Pawel and I have been looking at ProgPoW
    * Getting feedback on it from engineers at different companies, finding out about viability and whether it would make ASICs obsolete
    * We haven't decided to implement it but we want to have all the info we can before deciding
    * Miners care more about ASIC resistance than about the issuance reduction so I think of these as a "package deal"
    * Biggest question is, is there a threat if there are ASICs on the network?
    * Any opinions on the centralization risk? (No opinions)
    * Any change to POW wouldn't happen until after Constantinople, so earliest, eight months after it
* Danny
    * If we were not intending to move to POS, you could argue they're a centralization risk
    * But this conversation is always in the context of moving to POS
    * I'm hoping by the time we're discussing the next fork, we have some exciting developments in the beacon chain and POS that will give the conversation more context
* Hudson: No reason to commit to anything today
    * Will discuss post-Constantinople, we'll have more context then

# Attendees
* Alexey Akhunov (TurboGeth)
* Alex Beregszaszi (EF/Ewasm)
* Vitalik Buterin (EF/research)
* Jason Carver (EF/Python)
* Dmitrii (Harmony)
* Daniel Ellison (ConsenSys/LLL)
* Hudson Jameson (EF)
* Mikhail Kalinin (EF/EthereumJ)
* Dimitry Khokhlov (EF/Testing)
* Andrei Maiboroda (EF)
* Mamy Ratsimbazafy (Status/Nimbus)
* Piper Merriam (EF/Python)
* Lane Rettig (Ewasm)
* Danny Ryan (EF/Research)
* Afri Schoeden (Parity)
* Martin Holst Swende (EF/Security/Geth)
