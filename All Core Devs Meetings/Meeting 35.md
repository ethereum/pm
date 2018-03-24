# Ethereum Core Devs Meeting 35 Notes
### Meeting Date/Time: Fri, March 23, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/33)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=HHK6xhuSyUU)

# Agenda
1. Testing
1. EIP712: Add eth_signTypedData as a standard for machine-verifiable and human-readable typed data signing with Ethereum keys
1. Governance and EIP1
1. Casper and sharding - update from Taipei retreat
1. On Constantinople - timing, what to include
1. Client/research updates

# Notes

Video starts at [[5:11](https://youtu.be/HHK6xhuSyUU?t=5m11s)].

## Testing [[6:04](https://youtu.be/HHK6xhuSyUU?t=6m4s)]
* Dimitry: continue developing RPC methods
    * Upgrading cpp-ethereum client
    * Discovered that some of the state tests are wrong, investigating the issue, refilling the broken tests
    * [PR#437 to testing repo](https://github.com/ethereum/tests/pull/437)
    * I'd like client developers to try out the updated tests, maybe I'm wrong or maybe my changes to cpp-ethereum are wrong, but I think those tests were incorrect
    * Martin: Have they been active on hive? How are the clients reacting on hive?
    * D: Some of the tests may not have made it to the hive, in some cases tx not constructed by testeth, I fixed that issue
    * M: If you fixed and pushed to master we should be able to see it no?
    * D: Won't push to hive anytime soon, I'm using this retest tool now, tests generated via RPC, and there are other issues when you execute a tx on client using RPC, sometimes post-state is different
    * I use mine block method now, coinbase account touched, appears in final state, so minor issues like this
    * M: Tests previously invalid and now fixed, could you post a list of these to AllCoreDevs channel?
    * D: I'm committing a list of these in PR #437 (linked above)
* Peter
    * We had a long chat at Taipei meetup with Piper and Frederick
    * py-evm team is using geth and parity nodes in background to test correctness of py-evm
    * This is a huge pain for them to test since it’s hard to uniformly configure a chain for different clients
    * Ties together nicely with Dimitriy’s approach - having a unified interface for setting up and running consensus tests
    * Would be a nice addition if we can set these up so they can properly test the RPC methods as there is currently no unified test suite for RPC as it’s hard to set up common state for nodes
    * Not only could it assemble chains locally and run tx to see what happens, it could also export various types of tests
    * If we have these two-way things where we can both import and export state tests it’s very powerful because suddenly we can set up a web service with a bounty page where you can configure a chain, submit solidity code and some tx and have it tested against all client implementations — this would be a useful tool for the community
    * If I’m implementing some quirk in EVM and notice a sensitive thing that may or may not be broken in other clients then rather than dig through their source code I can create a test case and immediately submit it to run against all clients
    * No one has the capacity to develop such a tool but if we have the RPC endpoints properly spec'ed out then all we need is a nice web page
    * Dimitry: What do you mean by “export a test”?
    * Peter: Be able to export the JSON, e.g., export a go test to a test fixture and run against the others without needing to manually construct it
    * P: We have testrpc, truffle, and other clients constantly opening bug issues about things that act differently—with a common interface we could have a real common test suite
    * D: That’s the plan for the RPC implementation of the tests
    * P: RPC that we spec’ed out last time was only for consensus tests whereas what we’re discussing with Piper and Frederick would also allow you to have a full RPC interface where you could poll the node for data and interact with the node e.g. trace the last transaction, this isn’t possible with current mechanism
    * D: Not yet! New mechanism relies on RPC so if we define a testrpc method for tracing a transaction it would be
    * Only useful if all the teams are implementing something useful
    * Let’s continue this conversation elsewhere
    * D: My primary objective is to get all existing tests working again
    * P: If we’re going in this direction let’s spec it out and make it useful for everyone so we don’t have to create more test RPC endpoints in the future
## EIP712: Add eth_signTypedData as a standard for machine-verifiable and human-readable typed data signing with Ethereum keys
* Lefteris: summary
    * Propose addition of an RPC method to sign arrays of any kind of arbitrary data so the signer’s UI can show them what they’re signing
    * Right now they just see a hash but don’t know what it is
    * Discussion has been going on for quite a long time
    * Recently Christian Lundqvist found a malleability issue, proposal to fix it has already been made
    * There is another EIP, 719 that is “like this EIP but on steroids”, also wants to create a provable way to show that user has seen it and the UI has shown it in a particular way
    * Discussion has drifted away a bit, I would like to ask for the opinion of people here and from the community how we can keep this EIP as limited in scope as possible and finalize it as soon as possible since many dapps including something we're working on (uRaiden) have been waiting patiently for it for a few months now
* Martin:
    * I’d like to see more people join the conversation e.g. Ligi, Nick Johnson, Dan Findlay
    * At the moment there are huge issues with the ways the clients sign test
    * Don’t know if that’s within the scope of EIP712 or if that’s only for more complex data types
    * L: no, only discussing signing an array of typed data so the user can know the type and the value that they are signing
* Hudson: alternative EIP191 suggested
    * Martin: this is an old one that I wrote a while back, I don’t think it solves the problems
    * H: seems more like a UI problem
    * M: EIP191 also suffers from some of the problems that current signed data has e.g. doesn’t say how large the total message envelope is so there’s some malleability in that
        * X19 ETH signed message then length then message but we don’t have the total message length which is a big blunder
    * H: candidate for potentially being accepted at some point, we should at least make it a draft
* Hudson: on governance and EIP1
    * Spearheaded by Nick Johnson
    * Making a really cool Jekel-Based interface where as EIPs are submitted they are collected to a website where they’re easier to read and collect the data
    * Lots of PRs going into this, editing EIPs to make their headers compatible with this
    * After this is done we’re going to look into redoing parts of EIP1 to make it clearer, e.g. separation of standard track vs. EIPs and some of the other things we discussed at previous core devs meetings
## Fellowship of Ethereum Magicians
* More info here: https://ethereum-magicians.org/
* First meeting in Paris during EthCC
* Full notes here: https://docs.google.com/document/d/1rgQnZKpNc71XUotSTVmHt9La8y3_yKi8te1bH396AWA/edit
* Initiative by Greg Colvin and Jamie Pitts
* Full room, many groups represented
* A lot of meta-discussion
  * Greg shared stories of participating in consensus-based decision making
  * High level stuff like discussion of how EIP editors are chosen, EIP review process
  * Discuss the status quo e.g. the current hard fork process and how we can do better
  * Review of how things work in other groups e.g. IETF, holocracy, humming and tension
  * What’s the role of this group? Do we need a separate body for the political side?
  * How to get more voices involved?
* Agreement that meeting in person is important for trust and having healthy conversation
* Next meeting in July, likely in Berlin, how do we fund it?
## Raul: introducing Prysmatic Labs
* Working on geth implementation of sharding
* We’re holding a meeting tomorrow
* Putting out a comprehensive roadmap of our sprint to get an e2e example of getting phase one working
## Back to EIP712
* Ligi: I like the idea but we need an upgrade path
    * Plan not to replace it but to make sure we have an upgrade path
    * There are some things in this EIP that would extend the scope too much
    * Would solve some UX problems but wouldn’t be great
    * Simpler thing that could be done first?
    * Some folks could do with simpler stuff for e.g. state channels
    * Perhaps you should finalize one of the simpler ones first then use it as a container for 712
    * Do we need backwards compatibility?
    * Issue of length field in the middle of everything
    * geth encoding in ASCII, Trezor encoding in binary
* Peter: important to know that Ledger and Trezor doing this differently so “signing is currently very freaky in the ecosystem”
    * Perhaps you should finalize one of the simpler ones first then use it as a container for 712
    * Do we need backwards compatibility?
    * Issue of length field in the middle of everything
    * geth encoding in ASCII, Trezor encoding in binary
* Peter: important to know that Ledger and Trezor doing this differently so “signing is currently very freaky in the ecosystem”
    * Not sure whether it’s worthwhile keeping backwards compatibility
    * Must remember there must be some clients depending on it
    * Reach out to community, find out who depends on it and be sure we don’t break anything
* Ligi: can do this cleaner if we don’t need backwards compatibility
    * Later we need a context to differentiate between different state channels
    * I was calling this a “prefix” but people may not like this so let’s call it “context” for what you’re signing
    * From UI perspective you can then do trust on first site things, that you know when you first interact with a state channel a user can mark that “I interacted with this” so when they interact with another we can highlight the fact that it’s different
    * At the moment there’s one prefix, Ethereum signed message, distinguishes it from a normal tx, if it has this prefix it cannot be a normal tx
    * But if you could do different prefixes you could differentiate between different state channels or use cases
    * We need use case or context as a field in there
* Lefteris: But couldn’t that just be part of the application?
* Martin: But you want to not have any malleability, so that data signed for a particular state channel cannot be parsed as data for some other contract
    * So it’s good we have a general framework like EIP191 that sets out where is the identifier for the context
    * Within that we can have 792 as one of the variants
* Martin: I’m also for not maintaining backwards compatibility
    * There are no production systems that rely on this because it’s so broken
* Lefteris: I second this
    * If we want to do what Peter suggested, ask the community if anyone depends on it, how do we do this?
* Hudson: We’re small enough, we can reach out to major projects that aren’t in the thread
    * 4-5 major hardware wallets
    * ~5 major mobile wallets
    * Multiple clients but we can cover them all pretty quickly
    * So it’s not impossible at this point to get broad consensus
    * If there’s consensus among most of them that’s good enough to get the EIP approved, changes in clients put in release notes
* Hudson: I added this to agenda for next meeting so we can discuss again in two weeks and get it moving
## Casper and sharding - Taipei retreat
* Vitalik update
  * Focused 90% on sharding
  * There was a bit of a Casper section because Vitalik, Vlad, Nate, etc. all there
  * We spent three days talking about a variety of swarding-related topics, going through the phase I spec that Justin published a week ago
  * Going through details like collator-proposer games, execution games
  * Some people brought up sub-issues with the current protocol
  * We’ll probably do another round of thinking about improvements
  * Generally got everyone there on the same page
  * Including core EF research team as well as Parity, Status, Prysmatic Labs, Pegasus (ConsenSys team) and a couple of other independent people
  * Got to know each other, talked about various theoretical crypto economic issues involved in designing sharding
  * Talked about roadmap and longer term
  * Basic roadmap is multi-stage approach
      * Stage 1: Implemented of sharding rooted inside main chain and where there is no state transition function
          * Data being included in sharded chain considered a data blob not transactions
          * That by itself is mainly useful for things like Leeroy/Twitter on the blockchain
          * In parallel, likely to come soon after that…
      * Stage 2: Finalize state transition function
          * Create a way for clients to execute state transition function for a given shard
          * Depends on account abstraction, ewasm, and new merkle tree which as of today is likely to longer be a Patricia tree it will be a sparse binary merkle tree, with a second layer that makes it as effective with one-fifth the complexity
      * Stage 3
          * Light client execution functionality
          * Cross shard functionality
      * Stage 4
          * Tight coupling: incorporate shards into main chain
          * Main chain considered invalid if any invalid shard chain gets in
          * Expect this to happen around the same time as full casper (hybrid Casper would happen somewhere in Stages 1-3 of sharding roll out)
* Karl: to add to that
  * On the third day we had a big meetupw which is recorded, anyone can check it out
  * We did two panels, one with a bunch of node implements
  * Second with researchers, Vitalik, Vlad, Jon, Justin etc.
  * Check that out on Youtube: “All Star Panel Ethereum Taipei”
  * Lots of good idea propagation!
* Hudson: will Casper be on a shard now?
* Vitalik: no
  * Sharding spec is designed so that sharding roll out is completely independent of what happens on the main chain as long as the main chain continues to work, has blocks and accepts tx
  * Casper FFG rollout will happen on main chain and will be rolled out in parallel with sharding roll out
  * Do we need a hard fork to roll this out? Yes
      * Fork choice rule change
      * One hard fork change, Casper votes included for free
      * Another: cut mining rewards, add Casper staking rules
  * Consensus changes designed to be pretty lightweight, most of heavy lifting done by Vyper contract
  * Other part of Casper implementation is voting strategy, PoS behavior that’s equivalent to mining in PoW, this needs to be implemented across clients
* Hudson: does this go into Metropolis part 2 (Constantinople)?
  * Vitalik: Depends on timing
  * If we want to, we can have Constantinople be the Casper fork and do a few other things
  * If we want to do other things faster we can do them in Constantinople and put Casper into the next hard fork
* Raul: Lots of different sharding client implementation teams
  * Deciding how to converge and work towards a test net implementation
  * There’s already a sharding repo (github.com/ethereum/sharding)
  * Want to align everyone on smart contract API
  * Should mention how sharding will be done through the contract and how that’s different from Casper contract, how to merge global validator set
* Vitalik: Goal is to merge validator sets and all functionality
  * Phases 1-3 of sharding and phase 1 of casper will both happen separately for simplicity and ease of implementation so they’re independent
  * Also self-maintained and safer
  * If casper fails during phase 1 it’s relatively easy to have people fall back to PoW
  * If sharding phases 1-3 fail, same
  * Casper phase 2, sharding phase 4 is when we might merge things and recommend that all new activity happens inside the sharding system
    * Phases 1-3 of sharding and phase 1 of casper will both happen separately for simplicity and ease of implementation so they’re independent
  * Also self-maintained and safer
  * If casper fails during phase 1 it’s relatively easy to have people fall back to PoW
  * If sharding phases 1-3 fail, same
  * Casper phase 2, sharding phase 4 is when we might merge things and recommend that all new activity happens inside the sharding system
  * Aiming for finality within 5-12 seconds
* Raul: My team is focused on a local testnet implemention in private blockchain
  * We’ll forego P2P implementation
  * One of the biggest unknowns it that the P2P networking for sharding isn’t figured out
  * Get it working end to end in a local testnet
  * And Proceed form there
* Ben Edgington
  * We have a practical bent at ConsenSys, we’re keen to have imlplementations
  * Try to accelerate some of the timelines that were discussed
  * Will require a lot of collaboration
* Peter
  * Currently P2P networking layer is not friendly to sharding
  * Assumes everyone wants to talk to everyone, “big blob of protocol”
  * If we want to split into 100 shard then all of a sudden you don’t want to talk to people outside of your shard, some nodes will want to talk to other people or jump across shards
  * These are features the current P2P protocol does not support
  * Felix has been trying to spec this out, has three concurrent EIPs, pushing forward in this direction
  * Sharding not possible without P2P overhaul, let’s not forget about this and focus only on consensus protocols
  * As long as you have two smart contracts communicating within a shard, there are various solutions
  * This is less trivial for cross-shard communication
  * When you have to access data across shards, data that might change while you’re accessing it, it becomes this distributed systems synchronization problem
  * We discussed how locks could work or could blog up
  * Interesting challenges, what happens if you run a tx and want something from other tx but then your shard suddenly reorgs
  * Thinking about message passing architecture, queuing theory, sequential communicating processes
  * Just discussing upsides and downsides, no solutions
  * It’s a hard problem to solve, need people in community thinking about it and bringing up ideas
* Raul
  * We also discussed time value of storage on the blockchain
  * Rent
  * How to interact with smart contract developers to get their voices heard
* Vitalik
  * Idea of storage rent: contract has to pay some amount of ETH per byte per block in order to stay alive
  * Reasoning: there’s an imbalance between on the one hand creating very short-lived contracts too expensive but creating ones that last forever is way too cheap
  * Many exploitability factors e.g. Gas Token which uses SSTORE filling to save up gas when it’s cheap, can be called to clear a storage key and give you the 10k unit gas refund when the price is higher
  * Entire system does a bad job of sufficiently pricing contract creation, making this pricing non-volatile
  * Correct incentives to clean up storage, right now no one really does this even despite 10k gas refund
  * Some idea of charging rent is a proposal that many people are in favor of
  * There are some different versions of this that we discussed
  * We discussed UX issues, e.g., how does having to keep contracts alive affect UX, how do we address these
  * I’m in the process of writing up a proposal based on contract resurrection
  * I feel like the research community feels that something like this is important
  * http://ethresear.ch forum best place to get involved
* Hudson: let’s save discussion of timelines for the next meeting
* Constantinople
    * EIP???
    * EIP210: Blockhash refactoring likely to happen
    * Something that reduces gas cost
    * We were initially going to finalize things over the next month or so, from community perspective everyone wants to get a hard fork out and get things done, but there aren’t many radical things going into Constantinople without Casper or Sharding so from my perspective we shouldn’t rush to pick a date
    * Vitalik: I think we should try to move away from the idea that hard forks are the only thing to get excited about
        * Community is excited about the big things
        * As far as making people feel that there’s continued real progress
        * Light client optimization, making clients work better, this will probably improve UI more in the short term than base protocol changes
    * Peter: AFAIK the only thing fixed that would be nice to ship in next hard fork is bitshifting ops
    * Vitalik: One other thing to consider, I know that in geth the elliptic curve operation became faster by about 10x, if Parity and maybe Harmony can speed theirs up as well then we can cut the gas cost of this by 3-5x or so, that would go a long way towards making ring signatures easier
    * Peter on geth
        * Addition, multiplication, pairing
        * Switched out our library for these
        * Addition was cheap, got a 2x improvement
        * Multiplication got 20-25x improvement
        * Pairing about 4x improvement
        * Problem is that these are raw benchmarks. This is important from a DoS perspective but we need some meaningful contracts that we can run as tests, use these and don’t just call the operations a gazillion times.
        * One i found is Christian’s zcash Ropsten verification contract, I turned this into a hive test, it performs really well, full zcash verification on current Ethereum takes ~25ms on my laptop
        * That contract is around 3x faster in geth than in parity, so I’m sure the same operations can go into parity to get them on par with these speedups
        * It’s still not “spectacularly fast”
        * I realized now while doing this optimized version that to verify that a point is on the official curve and respects all requirements it takes one less multiplication, just parsing a binary blob into a curve point on our curve is a lot more expensive than on the official curve - but nothing we can do about it
        * Should be benchmarked: our precompiles on elliptic curve, when I parse the pairing points, every time I need to revalidate that they are valid curve points. If we could split validation and operation itself it could make it a bit cheaper gas-wise. But maybe that’s dangerous.
    * On when to do the next hard fork
        * Hudson: Let’s continue this discussion at the next meeting and discuss Casper and Sharding
        * Martin: Do we want more, smaller forks or save up for one large hard fork?
        * Peter: We should wait until we have enough content for it to make sense, and we don’t have enough yet
        * Hudson: If we did one tomorrow we’d only have two EIPs, and one more that isn’t fully spec’ed out yet, EIP210 Blockhash refactoring.
        * Martin: personally I’d rather have more frequent hard forks with less in each one.
        * Hudson: that would help people get used to hard forks.
        * Peter: but don’t forget that hard forks are a huge strain on Dimitry and Yoichi.
        * If we decided to do a hard fork with two EIPs would that interrupt progress on Dimitry’s new test framework?
        * Hudson: If we did one tomorrow we’d only have two EIPs, and one more that isn’t fully spec’ed out yet, EIP210 Blockhash refactoring.
        * Martin: personally I’d rather have more frequent hard forks with less in each one.
        * Hudson: that would help people get used to hard forks.
        * Peter: but don’t forget that hard forks are a huge strain on Dimitry and Yoichi.
        * If we decided to do a hard fork with two EIPs would that interrupt progress on Dimitry’s new test framework?
            * Dimitry: I prefer to restore existing test functionality with existing client and new testing tool
            * But if necessary we can continue to use old testing tools
            * Bitwise shifting hard fork tests are already on the way, some of these tests already added to test pool
        * Hudson: We don’t have consensus on this. Should we do smaller or larger hard forks?
## Client and research updates
* Parity (Afri)
  * Update in Github issue
  * Just had a major release
  * Finished integrating PWASM VM, deploying to Kovan to see some more live testing
  * About to finish moving UI wallet to standalone Electron wallet
  * Light sync, CLI, completely overhauling how we deal with tx queue, refactoring for future PoS implementations
* ewasm (Lane)
  * Paris update, ewasm team met with TrueBit, Dfinity, Parity
  * Discuss differences in e.g. gas metering
  * Vitalik: Definitely happening in sharding
      * Shards will never see a single block of old-style EVM execution
* geth (Peter)
  * 1.5 months ago we did a major release, since then just polishing things, trying to choose next major feature
  * Currently most painful point is synchronization
  * Had a discussion of this in Taipei along with Parity team and Frederick
  * Converging on new sync model since both fast sync and warp sync starting to break down
  * Felix playing around with discovery protocol
  * Martin, Ligi playing around with signer ideas
  * Trying to pick a direction for next major release
* cpp-ethereum (Pawel and Andrei)
  * Update in Github issue
  * Add support for ewasm engine
  * VM, EVM-C interface
  * Andrei mostly doing bug fixes, improvements related to database, P2P, blockchain sync
  * Andrei: continuing to work on issues around sync and DB layer
  * Peter: what sync are you working on currently?
  * Andrei: full sync because it still has some bugs, warp sync
  * we use Parity’s warp protocol for that which is useful
* Harmony
  * Update in Github issue
* Ethereumjs
  * No one present
* Trinity
  * Update in Github issue
  * First trinity alpha release around the corner
  * Peter: will Python REPL be shipped inside Trinity or will it be an extension?
      * Jason: not much different than using web3.py for connecting to other clients
  * Peter: geth has always had issues with the console, it’s very legacy, go-JS interpreter, based on an old spec, it works fine as long as you don’t try to do fancy stuff and just use it as a simple UI/debugging tool, but can’t handle fancy JS
      * Don’t want to drop the console as it’s a valuable debugging tool
      * So we’re considering creating a separate Eth console that’s just a JS console based on Node and latest web3.js
      * People could connect to geth or any other node and have a nice way of interacting with it
      * Since you’re creating a REPL for Python I’m wondering whether we can make a Python console too that can attach to any node
* Turbo geth
  * Update in Github issue
* Raul, Prysmatic Labs
  * Meeting to discuss our plans for Phase I sharding
  * Link to Gitter channel
  * We’ll be releasing biweekly dev updates via Medium and our mailing list
* Ben, ConsenSys
  * No specific updates from ConsenSys
  * Moving forward on our full ethereum client development
  * This is no secret, although there’s been no formal announcement
  * Will open source client when we’re ready
  * Will be fully mainnet compatible and contain a sharding client
* Nick Johnson
  * Working on making EIPs more accessible and readable
  * Converted EIPs repo into a Jekkyl site so it will automatically build an indexed web page listing them
  * Preview at: http://arachnid.github.io/EIPs
  * There were some minor changes to header format of EIPs, must be in YAML format with double-dashes and case sensitive
  * If you have an outstanding EIP it will have to be adjusted accordingly
  * Also adding a travis script to automatically check all EIPs for validity on all open PRs
  * 198 (Vitalik), 778 (Felix) that are unmerged but referenced from merged EIPs, would be good if authors worked with me to finish these and get them merged
  * 198 lacks a copyright assignment which Vitalik himself needs to add, good to get these merged so we can fix the build and do automatic checking of all future ones
  * Half a dozen EIPs referenced from EIP1 that also aren’t merged, would be good to go over them and help merge them
  * Come to EIPs channel on Gitter
  * I’m planning on writing up a meta-EIP with some proposed changes to EIP process

## Attendees
- Vitalik Buterin (EF: Research)
- Paweł Bylica (EF: cpp-ethereum/ewasm)
- Jason Carver (EF: python)
- Jon Choi (EF: Research)
- Ben Edgington (ConsenSys)
- Karl Floersch (EF: Research)
- Hudson Jameson (EF)
- Nick Johnson (EF: geth)
- Raul Jordan (Prysmatic Labs)
- Lefteris Karapetsas (Brainbot)
- Dimitry Khokhlov (EF: cpp-ethereum, testing)
- Ligi (EF: geth)
- Andrei Maiboroda (EF: cpp-ethereum)
- Lane Rettig
- Afri Schoedon (Parity)
- Martin Holst Swende (EF: geth/security)
- Péter Szilágyi (EF: geth)
