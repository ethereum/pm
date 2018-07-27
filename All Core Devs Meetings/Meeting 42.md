# Ethereum Core Devs Meeting 42 Notes
### Meeting Date/Time: Fri, July 13, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/50)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=TWL6QaCsl1I)

# Agenda

* Ewasm: going to mainnet?
* Testing
* Client Updates
* Research Updates
* Joint testnet to replace Ropsten?
* Constantinople hard fork timing and what to include (continuing conversation from last call).
    a. EIP 145: Bitwise shifting instructions in EVM: pretty well-formed, but not 100% implemented or tested.
    b. EIP 210: Blockhash refactoring.
    c. EIP859: account abstraction.
    d. EIP 1052: EXTCODEHASH Opcode.
    e. EIP 1087: Net gas metering for SSTORE operations.
    f. EIP 1014: Skinny CREATE2.

# Notes

Video starts at [[5:46](https://youtu.be/TWL6QaCsl1I?t=5m46s)].

## Should ewasm go to mainnet?
* Axic update
    * Working on testnet
    * Proposal in progress to offer a subset of ewasm for the mainnet which could be used for precompiles
    * This could be an intermediate step
    * Should Ewasm have its own metering rules?
        * Clients can use single code in Wasm or write their own rules
        * Haven't made a decision yet on which one makes more sense
    * Already have issue on ewasm design repo to discuss this, please check it out (https://github.com/ewasm/design/issues/104)

## Testing
* No update

## Client updates
* geth
    * Trying to figure out a way for light clients to be able to sync the chain faster
        * Mostly hacking on light client and discovery stuff
* Parity (Afri)
    * Planning a major release soon, not much to announce now
* Harmony (Mikhail)
    * Began working on beacon chain on Monday
    * Pretty excited about upcoming sharding research
* Trinity (Piper)
    * Working on next major release
    * Arch. for plugins to host third-party functionality
    * Working on syncing logic, core functionality
* Pantheon/PegaSys (Shahan, Ben Edgington, Matt Halpern)
    * Planning to release Pantheon client at DevCon IV
    * Will meet requirements of well-behaved peer
    * Sync entire chain, mine blocks, propagate txs
    * Will support truffle, web3, deployment use cases
    * JSON-RPC as used by popular clients
    * More updates soon, will be more active in the community
    * Written in Java
* TurboGeth (Alexey)
    * Final tests for reorgs
    * Re-synced everything again
    * Testing on mainnet
    * Started some conceptual rearchitecture on the database
    * Doing DB research on this topic, found some data structures, will do in a blog post later
    * Getting close!
* Ewasm (Axic)
    * Plan to release testnet, no final date yet, hopefully before DevCon
    * WRC-20 challenge (subset of ERC-20) which can be implemented in any language that compiles to Wasm
        * C, Rust, AssemblyScript, one handwritten WAST
* pyethapp
    * Martin: becoming officially deprecated very soon
* Mist (Peter)
    * Did a release a while ago, now connects to Infura at startup then switches over when done syncing

## Research update
* Vitalik update
    * Vlad, Nate, and Vitalik arguing about beacon fork choice rules
    * Every random beacon scheme has its flaws
        * Randao: more explotability
        * Threshold VRFs: hard threshold online requirement
        * VDF: have to worry about ASICs, high chance of being monopolized
    * Can we make the beacon chain algo. more resistant to a higher level of manipulation of proposal selection
    * Because attester sets very large, it's statistically infeasible to really manipulate even one attester set, but no. of proposers is 100 per epoch which is totally manipulable if you can perfectly manipulate randomness
    * So can we modify the algo. to be more robust against proposers being really unreliable?
    * Worst case imagine in one epoch only 1-2 proposers are honest
    * We think we can but it requires some fork choice rule modifications
    * Problem with old fork choice rule is that it was very proposer-centric in that it counted by heights
    * Proposers have power to cause heights not to increment
    * Could move partially to something GHOST-like
    * If proposers stop showing up on Chain A, you have dangling attestations, can we make them keep contributing to the head score?
    * Trying to see how that fits into the finality gadget, justification
    * Making progress but still things to think about
    * Exploring design space between FFG and CBC algorithms
* Danny: We'll do a sharding implementers' call soon

## Joint testnet
* Is there still interest in having a joint testnet, Ropsten successor?
    * V: Short term we should have a testnet for Wasm
        * Longer term joint testnet for beacon chain would be cool
    * Afri: Parity began implementing EIP-1011, halfway through, began testing
        * Curious if we should have a joint testnet to replace Ropsten (not really related to Casper, just about testnet effort)
    * Peter: Would be good to have a successor to Ropsten
        * It's getting heavy, doesn't make sense to keep it alive
        * Ewasm would be a really nice addition, fairly easy to add
        * Casper: Reluctant if we don't have a final spec, final casper will be different from spec
    * V: we can differentiate between Casper and Casper+sharding
        * Beacon chain by itself can be used as single chain Casper setup
    * Hudson: No shared Casper testnet for now
    * We are interested in a successor to Ropsten, this is more of a temporary thing
    * Peter: Ewasm testnet has two quirks
        * Removed code size limit, this is a DoS vector on tx pool, cannot allow arbitrarily large txs
    * Axic
        * Removed code size limit but also don't discount zero bytes anymore
        * Network traffic, storage on disk compressed
        * Zero bytes also an attack vector, whether compressed or not is an implementation detail
    * Peter: We should be wary of changes that don't add too much value
        * Because they can sometimes make it to mainnet
        * I'm worried about these tiny tweaks that don't necessarily add value
    * What's the current status of Ropsten?
    * What's the minimum level of client support we need?
        * Only cpp-ethereum now, will have geth soon
        * Would be nice to target two majority clients at the same time
    * Axic
        * We have a single VM on cpp-ethereum
        * Will add support on geth soon
        * Working on a native interpreter
        * One problem we're having is that cpp-ethereum only supports PoW, not PoA
        * Do we want both cpp-ethereum and geth? If so we need PoW.
        * Peter: PoW is the only thing that all clients support. If we want a cross-client testnet then it has to be PoW.
        * Code size limit: We'll use this testnet for pure Ewasm testnet but open for discussion for shared testnet
    * Peter: geth tx pool already filters out tx larger than 25k
        * Geth stores 6000 tx, multiply by 25k and memory usage gets too large, 10x tx size already takes memory usage into GBs
    * Axic: timeline for "pure Ewasm testnet"
        * Before DevCon
* What steps should we take in the meantime while Casper + sharding are still being developed?

## Changing network ID in Constantinople
* Alexey
    * Noticed multiple places in geth where we still check for clean separation from ETC
    * In most places it doesn't matter but after handshake every client asks about DAO hardfork block, checks extra data, allows you to separate yourself from ETC even though they use same network ID and same handshake messages
    * I suggest changing network ID and changing it again after every hardfork for clean separation from previous network
    * Can remove most of the DAO-specific code from networking layer
    * If we change net ID after hardfork then we have to disconnect from all peers and reform the network
* Peter: If I'm a new node and I just join, then while syncing I need to observe the network IDs, what happens when switching from one hardfork to the next?
    * devp2p supports extending handshake with arbitrary fields
    * Can extend it to support arbitrary random data so peers know whether they are on the same fork or not
    * Don't need to change net ID, just add extra metadata
* Alexey: let's think about it a bit more, it would be really nice to make the code simpler, have cleaner forks

## Constantinople hard fork and timing
* Hudson: I'd like to get certain EIPs to accepted state
    * At least agree to put them into Constantinople and agree on a timeframe
* EIP-145 Bitwise shifting
    * Approved weeks ago, definitely going in
* EIP-210: Blockhash refactoring
    * Definitely going in
* EIP-1052: EXTCODEHASH
    * Not sure
    * Alexey: appeared recently
    * Danny: simple and useful
    * Hudson: straightforward, seems like people want it, let's put this in unless someone comes up with objections
* EIP-1087: Net gas metering for SSTORE operations
    * Martin: EIP says client implementation must maintain dirty map, what was touched during current tx
        * Don't think this is efficient
        * [bad audio]
        * There may be hidden complexities here
    * V: need to maintain a journal for the dirty map, what happens if stuff gets reverted?
        * We had to fight with these issues a bunch two years ago
        * Might reintroduce a lot of trouble if we're not careful
        * Increases complexity of a minimum implementation considerably
    * Peter: Makes blocks heavier
        * Will be heavier on hardware
    * V: With normal usage, yes
        * Would be good to have metrics on what contributes to the uncle rate
        * Seems weird blocks are being processed in ~200 ms but uncle rate still 20%
        * If block contents are closer to being simple tx when uncle rate went to 40% with same gas level
        * Nice to do more analysis and see what's contributing the most
        * Maybe it's not at the client level, maybe it's at the [MISSED] level
        * Necessary to inform any short-term scalability improvements we want to make
    * Peter: I have a hunch that block propagation is a significant component of the uncle rate
        * Could try to spin up 4-5 VMs around the world and see how fast they get the blocks, are there significant delays between them?
    * Alexey: I created a version of geth called geth-downloader
        * Checks PoW but does not execute txs
        * Relays blocks
        * Essentially just downloads the blockchain
        * Can sync in 1-1.5 days, starts propagating blocks around the network
        * Would be quite cheap because it can run on e.g. HDD
        * Can have lots of those rather than running a full node
        * Still useful to the network, have useful function since they relay blocks
* EIP-1014: Skinny CREATE2
    * Hudson: I think everyone was in favor of this one
    * Is it ready? V: I think so
    * Needs a discussion URL, otherwise good
    * Christian R. had a question: what happens in a collision?
        * Alexey: CREATE2 would only create a contract if it doesn't exist already
        * V: we fleshed out these edge cases already a couple of years ago
    * Peter: geth already has a clause for this use case
    * V: there are also test cases.
* delaying the difficulty bomb and/or reducing the block reward
    * V: Going by etherscan data on block time previously, if we say it starts when block time reaches 16s, would be ~ block 6.7m, would become noticable, in ~ 6 mos, after that it would take ~ 8 mos until it becomes really serious
* Timeline
    * Hudson: a proposed, very optimistic timeline
        * Finalize EIPs that are being implemented: July 13th
        * Client implementation: July 16th - August 13th
        * Testing: August 13th - September 10th
        * Testnet: September 10th - October 1st
        * Launch: October 8th (~20 days before devcon starts)
    * Alexey: alternative proposed timeline
        * based on fact that we need conformance tests for each EIP
        * might help find and eliminate issues
        * timeline
            * Finalize EIPs that are being implemented: July 13th
            * All clients have retesteth interface: Aug 13th
            * Each EIP has at least 1 reference implementation: Sep 13th
            * Conformance tests are ready for every EIP: Oct 13th
            * Specification is finalised for every EIP: Oct 27th
            * Client implementations and testing: Nov 27th
            * Testnet: Dec 13th
            * Launch: Jan 27th
        * Martin: Isn't that how we've always done it? Using cpp-ethereum as reference to write tests
        * A: Just want it to be formalized in a timeline
        * Peter: Up to now, implementing and writing tests have been done concurrently
        * A: Client devs very busy now, need full spec with very little chance of it being unimplementable before starting implementation
        * Hudson: In the past we've implemented while writing tests, and we implemented cpp-ethereum first, people copied this reference implementation
            * More agile timeline than waterfall might make more sense, can do things concurrently
        * A: Can do things concurrently, can also kick things out later if necessary
    * Alex: Could we prioritize EIPs, reevaluate as we go depending on progress?
        * Peter: bitwise shift, extcodehash, skinny create2 are all trivial
    * Hudson: We have less high-profile, high-risk changes
    * EIP-210
        * V: 210 is sort of new territory - first privilged EVM contract that gets called as part of block processing
            * But still just a surface-level change, not a deep change to EVM
            * Martin: EIP still not finalized
                * We decided a couple of calls ago to add genesis information
            * Alexey: Are we writing contracts in EVM bytecode or in HLL?
                * V: Published EVM and LLL for it, LLL is the appropriate level, doesn't introduce compiler risk, still readable
        * Pawel
            * Current code in serpent
            * I reported some issues
            * Every time I propose a change it waits forever, not able to queue them up
            * One or two PRs
            * Thinking about using lower level implementation, LLL or solc assembly, close to EVM opcodes
        * V: Do we have test cases for this?
        * Pawel: I wrote some unit tests but may not be included in EIP, should be in a PR
        * Martin: If you try to enable it at block zero it will wind up in a recursive loop storing block hashes, hinders it from being used
* Lowering gas cost for new EC precompiles
    * V: Is it just geth that added optimized libraries?
    * Peter: Trivial to inject into hive and run against all clients
    * V: We did the analysis for Byzantium, set 80k gas cost since we wanted to target 20M gas per second
    * Martin: Not same benchmark on geth and parity
        * How much effort should we put into this? How badly do we want this in Constantinople?
        * Doing it the way Peter suggested makes it easier to automate for all clients that are hive-compatible
        * Don't need things to be clearer, I can do it, just need to know how badly we want it
    * Peter: zk snarks are part of [unclear], hard to measure weight
* Hudson: timeline for release will probably be post-DevCon
    * Should delay Ice Age since we'll start seeing some effects in 2019
    * Alexey: Perhaps we shouldn't bundle everything into Constantinople but just release things as they are ready
    * Peter: Huge coordination problem, making sure everyone updates -- exchanges, etc.
    * V: If we want to guarantee a hardfork before DevCon then I'd recommend kicking out 210 (Blockhash refactoring) and 1087 (Net gas metering for SSTORE operations) (Bitwise shift, EXTCODEHASH which seem fairly simple)
    * Hudson: This could be a little hard fork
    * Peter: Everyone who proposes an EIP should at least have a reference implementation so it's easy to argue about
        * Could we ask Nick to implement it?
        * Hudson: might be a good future requirement
    * Pawel: I'm okay moving 210 (Blockhash refactoring) to end of queue, don't see any pressure to implement it
        * V: Use case: enabling light clients to sync without seeing every block header - would be nice to allow a light client to sync trustlessly in log time
        * Achieving it might not be worth it, can rely on existing approach until we have PoS light client functionality
    * Alexey: Or add an opcode instead of going with contract-based approach
        * Add a BLOCKHASH2 which can read block hashes all the way back to genesis
        * V: Entire historical set of blockchains become part of the state, tough for light clients
        * Nullifies benefits of blocks having links to blocks that are much older
        * Primary benefit is that you have a storage tree that contains some subset of previous block hashes
    * H: 145, 1052, 1014 should be priority
        * Let's start implementing these and writing tests for them
        * Discuss the others further on next meeting
        * We've been at a standstill for months on Constantinople, let's move forward
    * Danny: We could do Constantinople soon with these, then plan another fork for early 2019 to delay the ice age
    * Pawel: Can enable constantinople tests, these are already in repo
        * As Dimitriy explained it's easier to decide on the order
        * Can add another hardfork option to test config
        * Much easier to coordinate this way rather than trying to dump tests for all EIPs at once
        * Just specify which EIP will go next in terms of writing tests
        * Bitwise shifts, some tests already there, then next I'd pick CREATE2, can focus in cpp-ethereum to finalize the implementation and start writing tests next week
    * Peter: Let's start with these three easy PRs
        * While people implement them and write tests we can ask Nick to write a PoC for the next call to see what it would take to do EIP 1087: Net gas metering for SSTORE operations
    * Hudson: Looks like we have consensus on 145, 1052, 1014 these are low hanging fruit, and implementation already started, we can start with these.
        * V: maybe a simpler version of 210 (https://github.com/ethereum/EIPs/issues/1218)
            * Could probably be upgraded to full form over time
        * Hudson: Let's look at this and discuss it on the next meeting
* Timeframe
    * Hudson: Aiming for DevCon but not final yet
    * If aiming for DevCon let's just do these three
    * Let's see if Nick can implement his SSTORE stuff

## Attendees

* Alexey Akhunov (TurboGeth)
* Alex Beregszaszi (EF/Ewasm)
* Pawel Bylica (EF/cpp-ethereum)
* Jason Carver (EF/Trinity)
* Ben Edgington (Consensys/Pegasys)
* Daniel Ellison (Consensys/LLL)
* Matt Halpern (Pantheon/PegaSys)
* Hudson Jameson (EF)
* Mikhail Kalanin (Harmony/EthereumJ)
* Shahan Khatchadourian (Pantheon/PegaSys)
* Piper Merriam (EF/Trinity)
* Rachel Rose OLeary
* Lane Rettig (Ewasm)
* Danny Ryan (EF/research)
* Afri Schoeden (Parity)
* Martin Holst Swende (EF/geth/security)
* Peter Szilagyi (EF/geth)
