# Ethereum Core Devs Meeting 40 Notes
### Meeting Date/Time: Fri, June 15, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/44)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=8-AZys80RrU)

# Agenda
* Testing
* Client Updates
* Research Updates
* EIP 1087: Net gas metering for SSTORE operations
* Skinny CREATE2.
* EIP 210: Blockhash refactoring still needs to be updated
    a. clarify that it does not change the current semantics when invoked via BLOCKHASH -- does not deliver older blocks
    b. possibly be fixed to be able to return the genesis hash
    c. have a nicer abi signature)
* Constantinople hard fork timing and what to include (continuing conversation from last call).
    a. EIP 145: Bitwise shifting instructions in EVM: pretty well-formed, but not 100% implemented or tested.
    b. EIP 210: Blockhash refactoring.
    c. EIP859: account abstraction.
    d. EIP 1052: EXTCODEHASH Opcode.
    e. EIP 1087: Net gas metering for SSTORE operations.
    f. EIP 1014: Skinny CREATE2.

# Notes

Video starts at [[5:32](https://youtu.be/8-AZys80RrU?t=5m32s)].

## Testing
* Dimitry update
    * Started discussion about genesis.json format
    * We have a scheme that's taking the formats and declaring how the fields should look
    * Please see the link and discussion on test repo

## Client/research updates
* Geth (Peter)
    * Focusing mostly on performance
    * Released updates last week, 20-30% faster and lighter
    * Benchmarking and working on a lot of ideas
* Parity (Fred)
    * No major update
    * Thanks to everyone who helped fix the recent issue
* Harmony/EthereumJ (Mikhail)
    * Just released
    * Rocksdb tuning, some memory improvements
    * Plan to update casper implementation
    * Can try it in parity test network
* cpp-ethereum (Dimitry)
    * I have a testing branch that's WIP
    * Runs tests via rpc methods
    * Successful execution of state tests
    * Takes 10 min to execute all tests but it's mostly because cpp codebase not optimized to run RPC requests - this is my main blocker
    * Could be executed without PoW check
    * Andrei is working on cpp client optimization and improvements
* Trinity (Piper)
    * Pushed out first alpha ~2 weeks ago
    * Had someone fully sync and they ended up on ETC chain
    * Working on a bunch of performance fixes, bug fixes, lots of scrambling
    * Looking to do another named release next week with a lot of new features
* No one present/no updates from:
    * PegaSys
    * Nimbus
    * Exthereum
    * Mana
* Whisper
    * Working on experiment to get libp2p to work with Whisper
    * Goal to see if we can ditch devp2p
    * Over the summer I'll do a security audit of Whisper with Martin's help, then release will be complete
* TurboGeth (Alexey)
    * Latest version syncing in about five days
    * Currently on block 5.07
    * Database size ~210gb, I'll be able to get this down even more
    * I'm not satisfied with the performance but I'm going to stop here and prepare for the release
    * Currently working on ethtester
    * Only cpp-ethereum is directly tested by state tests, for other clients there are no direct tests, clients tested indirectly via Hive/cpp-ethereum
    * Tool that can communicate with node via P2P protocol, feed whatever blocks it wants, generate arbitrary chain re-orgs. Hopefully I'll be able to get some state tests there as well
    * If I succeed I'll clean up some RPC implementation and do the first release
    * Difference with testeth/retesteth? RPC method which requires implementation in every client, whereas what I'm doing doesn't require any client changes
    * Running on Google cloud, Spec is 4 CPUs, 26GB memory, 500gb SSD or HDD, and I compare with each other
        * Doesn't consume more than 6gb memory for heap allocation
        * Uses memmap files so OS probably uses more but heap doesn't go above
        * HDD falls behind but not too much, can see graph in my blog post
        * When they both sync to the end I'll publish another updated comparison
        * Also published disk breakdown because the DB I'm using (boltDB) makes it easy to breakdown what's consuming the 210gb (account, contract, preimages, receipts, etc.)
* Prysmatic sharding client on geth (Raul)
    * Finished minimal sharding
    * Proposers and notaries interacting with shard manager contract
    * Holding off on latest research on random beacons, these things are in flux and we're trying to be as scrappy as possible
    * First release will be a containerized system, anyone can clone the repo and run Docker/Kubernetes config and see the various nodes performing their role, observe state of shard network on local computer
    * PoC release
    * Also exploring P2P networking through go-libp2p
    * Vitalik: I'll talk about latest beacon chain and shard research which does change the roadmap significantly esp. factoring in Casper
        * But it's all still work that's on the same track
        * Have you done anything regarding sharding the P2P network or is everything being gossiped through the mainnnet?
        * A: all gossiped
        * Focused on workflow of proposers and notaries interacting with each other
        * Haven't figured out reorgs, will work on this next
        * Don't want to do anything that will be disrupted by research changes
* ewasm (Casey)
    * We've been mostly focused on making a block explorer that's ewasm friendly for the impending testnet launch
    * Also Jake has been working on abstraction around Hera so we can swap out Binaryen (WASM interpreter) for WAVM (JIT engine)
    * We should be faster than parity if we can do that
    * Working on WAVM integration and benchmarking for Hera to test performance of different interpreters and JITs, and bytecode that can cause the JIT to blow up (JIT bombs) - not worried about those for the testnet launch
* K-EVM/K-WASM (Everett)
    * Working on tech side of integrating EVM/ewasm
    * Trying to allow as much flexibility on K spec side as possible
    * Taken all blockchain level update functions/opcodes from EVM (CALL, CREATE, BLOCKHASH, etc.) and pulled them out into their own file called K-EEI (Ethereum Environment Interface) and define abstract updates that happen on blockchain side/queries that have to happen to implement this functionality
    * K allows you to mash together two definitions, I'll take K-EVM and remove that functionality and mash together to make sure existing functionality still passes the tests
    * Then it should be straightforward to use this to get a model of K-EWASM
    * We've had a lot of discussion of what is EEI?
        * State changes
        * VM should only handle execution details
        * EVM: stack, local memory, pretty much nothing else
        * So things like ADD call into VM not EEI
        * Whereas something like SELFDESTRUCT falls on EEI side
    * Also, there are some sticky opcodes with EVM like CALLCODE, historically not great things, we'd like to limit their use in ewasm
        * It would be nice to say there's a set of abstract state update fns that clients can implement
        * Each execution engine e.g. ewasm can choose a subset of that to expose to contracts
        * Right now the "subset" is everything, it's exposed to EVM
        * But e.g. we'd break up SELFDESTRUCT into two ops, one that does the destruct and one that transfers funds
        * We want a "transfer funds" primitive, could be exposed to ewasm, but both that and destruct would have to be called together for SELFDESTRUCT
        * Mostly discussion, occasional updates to the EEI spec at github.com/ewasm/design
* Research updates
    * Casper/sharding updates (Vitalik)
        * Substantial reworking of roadmap but not final product: https://notes.ethereum.org/SCIg8AH5SA-O4C1G1LYZHQ?view
        * It's a beacon chain that's a PoS chain
        * Hangs off main chain so it's like a shard chain
        * Implements Casper FFG validation
        * Voting, etc. implemented like Casper FFG
        * Also implements basic shard management, though some parts aren't specified here
        * Main difference is that this roadmap means that for hybrid casper FFG part, we don't go with the version that had Casper FFG as a contract on the main chain
        * Instead to deploy hybrid PoS as a prelude to full PoS and sharding, we can just run the beacon chain
        * Because it implicitly links to the main chain it can be used to finalize the main chain but does so without being directly inside the main chain
        * Only contract written in Vyper or whatever in the roadmap is a contract that lets you call a fn to send 32 ETH with some arguments, burns the ETH and creates a log
        * Everything else processed by the rest of the system
        * The functionality this provides, in the short term, is very similar to functionality of Casper FFG as contract had
        * But this mechanism is one way, if someone deposits 32 ETH, it's there until a future hard fork implements the part that allows it to be withdrawn into a shard and where shard state transition fn is more fully-enabled
        * Main advantages
            1. Casper component more separate from main chain, so it can be developed less intrusively, as separate chain, own rules about passing vote messages and blocks around network, how blocks are included etc., don't worry about interactions between Casper and non-Casper tx, what happens in parallel etc. since clearer wall between two systems
                * Beacon chain is a full PoS system, has block proposal mechanism
                * But every block references a block in the main chain
                * So it "hangs off" the main chain
                * Whatever PoS block gets finalized also points to a main chain block so indirect finalization
            2. Removes need to develop a lot of infrastructure around two separate PoS games (Casper and sharding), here there is only one validator set, only one way to get into the validator set, etc. right from the start
            3. Development of one system will be much more directly on the way to dev. of later-stage sharding system
                * Once Beacon chain is fully operating, has substantial deposits, once sharding part is enabled (shard state transition fn), then that Beacon chain would already be the main chain of the sharding system
                * Not much work would need to be redone to move from partial Casper to full Casper+sharding
                * Linked spec (https://github.com/ethereum/research/tree/master/beacon_chain_impl) describes blocks in beacon chain, fields, state, different parts of state, fork choice rule, state transition fn, partial Python implementation that implements most of the core logic
            4. In this chain, deposit size drops to 32 ETH
                * Uses BLS signatures for signature aggregation which means that even 1000 validators signing same message, verified using a single signature verification operation plus one elliptic curve addition per participant, cost of this is pretty tiny
                * Longer-term we want something quantum proof and hash-based, we are exploring replacing BLS-based system with STARKs
                * There's reason to believe that if we use the right hash fn then using STARKs to validate aggregate sig. not so bad once tech is developed
        * To resummarize:
            * This is roughly current direction for sharding roadmap and replacement of roadmap for Casper FFG
            * Keeps FFG algorithm (voting, justification, finalization, dynasty changes, etc.) the same but it's implemented in native code rather than in Vyper
            * Beacon chain also pushes us much further along the way towards a final product sharded system
            * Because things are written natively, optimizations around bitmasks and signature aggregation that aren't available in EVM, can scale to theoretical maximum (10M ETH, 300k validators), can survive even in absolute practical max (4M validators, "absolutely everyone participating")
            * Average and worst-case behavior is substantially more feasible than under the old roadmap
            * Two weaknesses
                * Loses ability to deposit into Casper and withdraw without future hard forks
                    * If required we can add a gadget where contract can verify BLS signature, not sure if this makes sense
                * Loses signature abstraction
                    * But does reduce need for some of the fancier schemes because minimum staking amount goes down from 1000 -> 32 ETH
        * Danny: we're deprecating EIP-1011 in favor of new design
            * Took a while to digest and be comfortable with but I think this is great, gets us where we want to be sooner rather than later
        * Raul: can you discuss roles of proposer in system?
            * V: you have a separate chain for each shard, progressing in parallel
            * Once in a while a block from every shard would be attested to by randomly-sampled committee of validators on main chain
            * Come together, say, we've all verified the portion of the shard chains since last cross link up to this block, here's the hash of a block and we've all signed it
            * This aggregate sig. would get published and verified on main chain, that updates to being the main chain's current view of the latest block on a particular shard
            * One epoch every 500s (~8m), down from previous epoch length of ~15m
            * Every epoch, there's a cross-link made from some number of shards, e.g. if 10% of validators deposited it's 10% of all shards
            * Meaning every given shard has a new cross-link added every hour
            * We could crank up number of cross-links at some overhead cost
            * Might be something like every hour for a shard
            * But even in between you can generally trust the shard chain's own growth to be good at not reverting in the short range
            * If a block gets 2-3 confirmations in a shard chain it's already a pretty good level of security
            * This is a long-term goal
            * If we want quadratic sharding ASAP, we just want 5-10k TPS, cross-links are just blobs that are connected to a shard, some proposer connected to a shard that has ability to create a cross-link
            * Every validator randomly assigned to some shard for a long time to be a proposer
            * Every time a crosslink is created, new proposer selected, can propose new crosslink
            * But in longer-term model the set of proposers in the shard would between themselves create and push fwd the chain until some block in the chain would get included in a cross-link
            * These two perspectives are similar, chain just a device that proposers use to coordinate amongst themselves which blob to include as a crosslink
            * Long-term goal that crosslinks just link from shard chains to main chain
        * Justin: Design is merged but from release standpoint it's possible for Casper to come before sharding even though they both live in beacon chain
            * More likely that Casper comes before sharding at this point
    * Justin:
        * Some other things to share
        * One advantage is more security since it's not possible to do withdrawal until there's state in the shards so deposits will be frozen for quite some time, we can launch with more confidence, experiment and move faster
        * All native code in beacon chain, no EVM, no worries about gas and more future-proof since endgame is to deprecate EVM 1.0 and much closer to final design as V said
        * Allows us to unlock new functionality esp. BLS signatures which radically changes performance properties of the design
        * Beacon chain will have possibly 5s blocks, faster and less variance
        * More unity between Casper and sharding, teams developing these two projects
        * Lots of reused infrastructure between Casper and sharding all the way from capital deposited to messages, gossip channels, signatures, aggregation points, accounting
        * Lots of Casper come for free given sharding, subset of the infrastructure we want to build for sharding
        * Once we start merging the validator roles of Casper and sharding we get better security since atomicity of roles, you can't be a Casper validator without being a sharding validator and vv.
        * If we mess up incentives and it's profitable to be one and not the other, well, if you want to be one you have to be the other
        * Custody bonds
            * In sharding validators vote on availability on some piece of data like a shard block
            * We can have an honesty assumption, trust the votes that are being made
            * Custody bond: when you make a vote there's a cryptoeconomic scheme which incentivizes you to have custody of the data you're voting availability for
            * Can have enhanced voting mechanism where validator has custody of the data at the same cost of making a plain vote with a signature
            * All works really nicely with BLS aggregation

# EIP 1087: Net gas metering for SSTORE operations
* Nick Johnson
    * Lots of cases where contract execution results in making change in storage value then changing it back
        * So no change is none
        * E.g. authorizations in ERC-20 tokens
        * Useful to do this but cost prohibitive because of cost of SSTORE
    * This proposal changes cost of SSTORE, charged in end based on actual changes to disk, if you reset to your original value you don't get charged
    * Improves usefulness of SSTORE and reduces cost of operations that are currently penalized for this sort of behavior
    * Could be included in Constantinople, relatively straightforward and lots of use cases
    * Peter: Nice, easy
    * Dimitry: we need consensus on which changes go into the next HF since we need time to prepare the tests

# Constantinople hard fork timing and what to include (continuing conversation from last call).
* Things we might like to include (details follow)
    1. EIP 145: Bitwise shifting instructions in EVM: pretty well-formed, but not 100% implemented or tested.
    1. EIP 210: Blockhash refactoring.
    1. EIP 859: account abstraction.
    1. EIP 1052: EXTCODEHASH Opcode.
    1. EIP 1087: Net gas metering for SSTORE operations.
    1. EIP 1014: Skinny CREATE2.
* Thoughts on timing?
    * Nick: Given research report it seems unlikely we'll have anything Casper-related ready to go in originally-planned timeframe
        * So maybe we can move forward with the existing, proposed list of EIPs, we probably have enough
    * Keeping in mind we need a lot of time for testing, we won't rush things like we have in the past
    * Danny: Before or after Devcon?
        * Last year there was a fork shortly before Devcon, people were concerned that if something happened we would all be at Devcon
    * Hudson: Still 4-5 months out, should be doable before Devcon, EIPs are fairly straightforward so bottleneck probably testing
    * Nick: Should we consider all proposals and approve them on next call?
    * Hudson: Let's go over them now and do approvals next time
* EIP 145: Bitwise shifting instructions in EVM: pretty well-formed, but not 100% implemented or tested.
    * Dimitry: test coverage should be pretty easy
        * We have unit test for bitwise implemented already, could make this into a blockchain test
* EIP 210: Blockhash refactoring
    * Nick: Still some concerns about robustness of this code
        * Let's include it if we can but figure out how it's going to function
    * Clients don't have to implement it by making it a call, that's an alternate way of implementing it
    * Vitalik to follow up, reference item in this agenda
* EIP 859: account abstraction
    * Hudson: Tabled permanently because too complicated
    * Main thing in abstraction category that's relevant is Skinny CREATE2 since it makes state channels easier
    * Tabling for now, no one advocating for this
* EIP 1052: EXTCODEHASH Opcode
    * Nick: We currently have a way to fetch code, though we have precomputed code hash there's no way to fix that inside the VM
    * Lots of situations where it'd be useful to do so, should not cost as much as it does
    * Add a very simple opcode that fetches code hash without requiring EVM code to fetch all the code and perform the hashing
    * E.g., I wrote a smart contact that's able to check another contract's bytecode for disallowed opcodes e.g. store, call
    * Can have multiple contracts with the same bytecode
    * Could efficiently recall which contracts you've seen in the past
    * Or any other case where you want to check whether a contract's code corresponds to some whitelist
    * Nick: there are bad reasons you'd want to do this but also some good reasons
    * There's a thread with some people asking for some clarification in the [Magicians forum thread](https://ethereum-magicians.org/t/eip-1052-extcodehash-opcode/262?u=lrettig)
* EIP 1087: Net gas metering for SSTORE operations
    * Should this go into Constantinople?
* V: do any of these EIPs have impact on scalability or sharding?
    * Sharding, no, roadmap starting with this separate beacon chain
    * Skinny CREATE2 (EIP 1014) makes state channels easier, and they are a viable scaling solution
    * Improve privacy by adding an EIP that dramatically reduces cost of ECADD, ECMUL, pairings, make sure all major implementations have optimized implementations of these so as not to add DoS vulnerabilities
    * If we can knock the cost of these ring sig ops down from 200k gas per participant to e.g. 30k gas per participant we'll see more ethereum-based privacy solutions and zk-SNARKs in the short-term which can help with scaling
    * Zooko wanted BLAKE2 in there, there are implementations floating around
    * Alexey: Storage costs overwhelm elliptic curve sigs
        * Possible to aggregate many operations into one but you cannot aggregate storage
        * Main cost not sig functions but storage, a register to make sure people can't spend funds again
        * Actual signatures insignificant compared to that
        * V: cost of storage slot 20k gas, if just indices, can cut down cost to 7-10k gas
            * Cost of verifying a SNARK even with more recent SNARK protocols still > 100k
            * For sake of example let's say we cut SNARK cost from 700k to 200k
                * 10% scalability gain since gas limit of 8M
                * Improves usability, need to wait for a smaller number of things before you can aggregate all of them and publish a SNARK
                * Reduces latency of app
                * At any acceptable fee level latency of app could go down by a factor of 3
                * Not just SNARKs, other tech where EC dominates
                * E.g. BLS signatures, aggregated signatures, ring signatures, Peterson commitments, range proofs, etc., lots of other fancy stuff you can do with EC
    * Hudson: we previously tabled BLAKE2 proposal since we were waiting for ewasm and didn't want to add a lot of precompiles
    * V
        * the roadmap by which ewasm definitely going into new sharding land and not EVM 1.0 main chain which realistically will delay its availability
        * most of the work is already done, in some ways it is lower complexity than a lot of the other EIPs since fairly contained
        * BLAKE is legitimately a very fast hash fn
        * Elliptic curve stuff, work already done on integrating a faster library for this into geth so this is a no-brainer
        * V to do an EIP to reduce gas costs
    * Hudson: We'll put this on the agenda for next week and I'll let Zooko and Jay know that this is back on the agenda for the next HF
        * Zooko's team may be willing to put some work into implementations for different platforms, already some work done for Go, Rust, Python
* Nick: Other EC curves such as P256, useful for verifying non-blockchain stuff
    * My particular use case is DNSSEC where cloudflare and others are starting to make P256 widely used
    * Curve of choice for a lot of asymmetric curve apps outside of blockchain
    * Would be nice to be able to do ECVERIFY for those curves as well
    * Alexey
        * We used to have processors with really complex instructions, some people said let's do simple things cheaply
        * Maybe there's a way to generalize in a small set of instructions that can implement any EC
    * Nick: looked into this, got feedback that you can't have a generic EC library
    * Alexey: what about generic field arithmetic library?
    * V: We already have MODADD, MODMUL, I don't think finite field arithmetic is the bottleneck even for EC, it's more the glue around the finite field arith.
        * E.g. ECMUL requires avg. 384 ECADDs
        * ECADD is 10 field operations
        * So many thousand units of glue even within one ECMUL, if each is 5 opcodes that's already > 500k gas
        * Part of it is pushing and popping and calling add inside while loops
    * Nick: I'm talking about adding precompiles not new opcodes
        * Clients could implement multiple curves using the same underlying libraries
        * Additional complexity per curve is fairly minimum, more like standard libraries than new opcodes
    * Hudson: is there an EIP for this?
    * Nick: Not yet, wanted to take temperature before writing something up
    * V: we're most of the way there to having precompiles for finite field operations, look through some of the contracts I wrote that implemented EC in Serpent
        * If we want to increase the efficiency of doing EC ops we need a precompile
    * Peter: For BN256 we have multiple precompiles, any actual zkSNARK will use multiple calls to same precompile
        * Each verifies that curve point is valid
        * It's insanely expensive
        * Because we have multiple precompiles to create complex behavior we repeat the same verification over and over again
        * It may be something we need to pay attention to
    * V: If we try to compute how much BLAKE verification costs it's just verification of equation y^2=x^3+b, similar to ECADD, ECMUL much bigger
    * Nick: Should we reduce gas cost for calling precompiles? Right now it has the same gas cost as any other account
        * Alexey: I think there is already an EIP for that written by Jordi Baylina
    * Casey: I'm against creating new precompiles but adjusting gas cost of existing ones is easier
        * It's a slippery slope
        * One of the promises of ewasm is that users can deploy their own precompiles
        * So if it's not one but 3-5 more precompiles it may be worth looking at deploying ewasm on the main chain
    * Nick: But nothing we can do here can speed up deployment of ewasm
    * Casey: But more precompiles would potentially slow adoption of ewasm on the main chain
        * It's a matter of coordinating what's the next thing adopted on the main chain
    * Everett: We could add precompiles implemented in ewasm and transition to using them as ordinary contracts, as a stepping stone
        * You need to implement the precompiles in some language anyway
        * Smoothly transition to being a normal wasm contract in the future
        * If you add precompiles now, then when ewasm comes online, they'd be implemented as wasm contracts
        * So comparable amount of work and a bit smoother to implement in wasm
    * Nick: but then every client needs a wasm interpreter now, and could even change between now and when ewasm is finalized
    * Everett: wasm intepreters fairly standard but ewasm isn't completely nailed down
    * One of the design goals of ewasm is to use vanilla wasm interpeters
    * Casey: every client would need a wasm interpreter or JIT engine if gas costs low enough but then you wouldn't need implementations of all the precompiles, just the wasm interpreters
    * Alexey: semantics of opcodes simple relative to precompiles, precompiles introduce risk of consensus failures if different clients use different libraries
        * As V mentioned, part of the glue used has gas cost, we might see whether it's overpriced, in geth there's a lot of cost for memory, stack allocation, etc.
        * Might lower cost of arbitrary EC math on EVM
    * Everett: in terms of consensus failures, precompiles implemented in WASM are way better than external code since everyone has to agree on how to execute WASM anyway
    * Nick: Agree but don't think it makes sense to introduce this now, not reasonable to ask clients to embed a WASM interpreter
    * Everett: We don't need to say clients need this, WASM can be compiled to LLVM
        * Can compile to binary linked into C implementation
        * We're not losing any flexibility
        * We have a _single contract_ in a language that we all agree on execution for
    * Nick: Linking into go is non-trivial
    * Everett: Not sure of implementation cost, just arguing for benefits of precompiles in ewasm
        * Also easier to decide on gas cost of precompiles
        * Just look at consensus implementation of it, just meter it and see gas cost
    * Hudson: We have a few options here, we'll discuss more on the next call

# Skinny CREATE2
* [EIP-1014](https://github.com/ethereum/EIPs/pull/1014)
* Hudson: Seems to have universal support for e.g. better state channels
    * Hopefully EIP further along so we can talk about it next time
    * Is this pretty much done?
* V: Probably not much more to do with this

# Next call

* Hudson: we'll continue conversation about Constantinople hard fork on next call in two weeks.

## Attendees
* Hudson Jameson (EF)
* Lane Rettig (ewasm)
* Mikhail Kalanin (Harmony/EthereumJ)
* Peter Szilagyi (EF/geth)
* Alexey Akhunov (turbogeth)
* Jake Lang (ewasm)
* Daniel Ellison (Consensys/LLL)
* Frederik Harryson (Parity)
* Justin Drake (EF/research)
* Guillaume Ballet (EF)
* Danny Ryan (EF/research)
* Casey Detrio (ewasm)
* Raul Jordan (Prysmatic)
* Vitalik Buterin (EF/research)
* Dimitry Khokhlov (EF: cpp-ethereum, testing)
* Paul Dworzanski (ewasm)
* Everett Hildenbrandt (ewasm)
* Lefteris Karapetsas (Raiden)
* Nick Johnson (EF/ENS)
* Tope Alabi
* Alex Van de Sande (EF/Mist/Ethereum Wallet)
