# Ethereum Core Devs Meeting 49 Notes
### Meeting Date/Time: Fri, November 9, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/60)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=DUUOCDxvKbw)

# Agenda

1. Testing
1. Client Updates
1. Research Updates
1. [Görli PoA-testnet progress](https://github.com/ethereum/pm/issues/60#issuecomment-436588176) (@5chdn)
1. [Constantinople/Ropsten HF](https://github.com/ethereum/pm/issues/53)
   - hardfork timing [1](https://github.com/ethereum/pm/issues/60#issuecomment-436926864), [2](https://github.com/ethereum/pm/issues/60#issuecomment-437300192)
   - difficulty bomb
1. On the Yellow Paper/Jello Paper spec
1. [ProgPoW update](https://github.com/ethereum/pm/issues/60#issuecomment-437321761)
    - Ethereum stratum/mining pool support
    - [EthereumStratum 2.0.0 draft](https://github.com/ethereum/pm/issues/60#issuecomment-437343594) (@chfast)
3. updating the eth_getWork RPC API with a 4th return value for the block number
4. Conversations about setting up a few processes at DevCon

Call starts at [[9:08](https://youtu.be/DUUOCDxvKbw?t=548)]

# Testing update
- Martin update
    - Fuzz testing has continued and become a lot more stable
    - We have two machines up with different fuzzing strategies
    - It's done 5M test cases since Oct. 25
    - Has found one consensus issue in one client, which is being fixed

# Client updates
- Parity (Fred)
    - We forked Kovan to the latest changes and it's working
    - Working on block propagation issue reported during DevCon
    - Talking to WhiteBlock simulation tool to see if we can simulate the effects of fixing it
    - Shipping alpha for light client wallet today, Parity Feather
- Geth (Peter)
    - Have a lot of PRs piled up due to DevCon, we are crunching through them
- EthereumJ (Mikhail)
    - Preparing release with fixes for issues discovered during Ropsten Const. hard fork
    - Continuing to work on ETH 2.0 implementation
- Aleth (Pawel)
    - Slowly preparing v1.5 which will contain Const. changes
    - EVMC v6 released
- EthereumJS (Holger)
    - Made good progress on Const.
        - Merged CREATE2
        - EXTCODEHASH in progress
    - Will do release in 1-2 weeks on Const.
- Nimbus (Jacek)
    - Just catching up on DevCon stuff
- TurboGeth
    - Fixing bug discovered on Ropsten HF, to do with rewinding
    - Working on [?] database announced at DevCon
    - Trying to extract some datasets, using efficiency of TurboGeth in extracting different sets of data from DB, looking pretty good
- Pantheon (Danno)
    - Had offsite all week in Prague
    - PRs, issue queues open for Pantheon on [Github](https://github.com/PegaSysEng/pantheon)
    - Going to contribute back to EXTCODEHASH [??]
- Trinity (Piper)
    - In theory Const. ready
    - Need to get all the tests passing

# Research update
- Research team - no one present
- Ewasm (Lane)
    - Public launch of testnet at DevCon (ewasm.ethereum.org), still only on geth
    - Still some outstanding EVMC, etc. changes being worked on, will publish latest genesis data to make it easier for others to add nodes
    - Discussing some outstanding design questions such as static/dynamic linking with an eye towards a mainnet launch in 2019

# Goerli testnet
- Is this one of testnets that we can test Constantinople on?
- Afri update
    - Born at ETHBerlin hackathon
    - Wanted to have a cross-client PoA network
    - Two people working on implementing clique PoA engine in Parity
    - With Pantheon too we have 2.5 clients that support clique
    - With Pantheon and geth validator - working smoothly
    - Clique is simple and "just works"
    - We have pre-testnet for Goerli testnet, waiting for parity code to be ready
    - Parity allows mode to skip validation, possible to sync chain using parity client insecurely
    - So far we have two validating clients on Goerli, one not validating
    - Goal is to have testnet for all clients
    - Not ready yet for Const., will be ready after Const.
    - Activated all Const. changes in Goerli genesis
    - Will be fully working once clients have clique support
- Peter: Seems Goerli testnet is stuck, all clients forked away?
- Afri: yes, we had our first consensus issue yesterday
    - Need some work
    - Github landing page, goerli
- Jared
    - Working on clique support in parity but technically on vacation 🤷‍♂️
- Hudson questions
    - Parity, Geth, Pantheon: these are the "2.5" clients working; parity is the 0.5 for now
    - Is clique what rinkeby runs on? Yes

# Constantinople
- Timing
    - Afri, Holger proposals for timing (see agenda)
- Holger's proposal: https://github.com/ethereum/pm/issues/60#issuecomment-437300192
    - From software engineering perspective and my intuition, this would be a good plan, i.e. a bit more conservative
- Hudson: we discussed on the last call, there's work to start a new testnet, and we like that Ropsten is heavily used and has lots of data
    - These are the arguments in favor of keeping Ropsten
- Peter
    - From Rinkeby perspective, after we launched it, it took at least half a year until Rinkeby actually saw "real world, day to day" use
    - If we launch a new testnet before Christmas I don't think people will use it
    - Huge inertia already on Ropsten and it takes a lot of time to switch over
    - I think it would be valuable to kill Ropsten and start a new testnet but it won't help us test Const.
    - Could be used for the next hard fork
- Martin: I agree with Peter
    - Comment that there should be at least one successful fork on a testnet
    - I don't understand what's so particular about successful, real-time fork, I don't see any value in this
    - Hudson: it broke really quickly; makes sure that we find bugs
- Danno: We need dress rehearsals to find bugs
- Martin: Any client that successfully did a fork managed to pass the fork, right? So we have tested that
    - We can test fork transition easily by doing a full sync through the fork
    - I don't see the value of doing it _in real time_ vs. on historical data, fork that already happened
- Alexey
    - There is a difference
    - Different parts of code being activated during the realtime transition vs. syncing
    - E.g. when doing it live there are uncles coming from pre-fork
    - If there was so much noise during the fork on Ropsten we might not have noticed some minor issues, but because we were overwhelmed with big things we might not have noticed
    - I would feel more comfortable if there were a successful realtime fork
- Peter: Ropsten is already forked, and you won't be able to spin up a new testnet with decent traffic
- Alexey: Probably too late to roll it back now
- Martin: If we keep Ropsten for testing actual tx/stuff happening on chain, and if a group wants to do a live transition, we can spin up a new testnet
- Alexey: Yes, test transition, even with no usage
- Martin: EthereumJ, TurboGeth, geth, parity, whomever else wants to join - don't need a huge coordinated effort
    - Let it spin for an epoch or two, transition, then continue for another epoch or two
- Alexey: On a new testnet, can repeat until we get a smooth transition
- Holger: Will this be PoW? Should we use for ongoing Const. testing in semi-public and then enlarge it to a new PoW testnet?
- Alexey: No, this is a "throwaway chain"
- Martin: Must be PoW since it's the only thing every chain implements
    - We can keep it or throw it away
- Piper: We don't need to decide that part today
- Hudson: Let's figure out rest of timeline then timeline for the testnet
- Martin: I'll take lead, spin up a couple of machines. Send me your SSH keys and I'll spin up machines for us to use.

- Hudson, on timing:
    - Afri proposed Jan. 16
    - Holger suggested forking on the 12th
    - We've forked on Ropsten, had issues, they were resolved, no major ongoing issues
    - Starting up a new PoW testnet, Martin leading, will happen before EOY
    - Is mid-January too much time? Good timing since it's post-holidays?
- Update on difficulty bomb (Lane)
    - Worked on this with Ed Mazurek, T. Jay Rush, James Hancock, Casey Detrio, Vitalik
    - Block times will begin to increase in Jan
    - Expected to reach 30s block times in May
    - Could be as early as early April if hashpower declines ~20-25%
    - Will hit faster than last year

# On the Yellow Paper/Jello Paper spec
- Alexey: yellow paper/jello paper spec
    - It does contain some elements of Const., has it been updated for e.g. CREATE2?
    - Hudson: We haven't adopted the jello paper as official yet
    - Yoichi is no longer at EF, no longer updating the yellow paper
    - Jello paper based on K, can generate tests using it
    - It's a lot more formal
- Martin: Formalizes EVM execution part
    - Block, header validation, state transition, etc. from YP still relevant
    - Still need to be added to the jello paper
- Peter
    - Community has been telling us that YP is dense, hard to follow
    - Only a handful of people have experience and knowledge to modify it
    - How many ppl in the world can properly update it?
- Martin
    - This is written in K which is a language so the spec is also an implementation
    - you can take it and subject it to tests and execute the spec, see the results of txs/state transitions, which is really powerful
    - Can do formal verification
- Fred: Seems confusing to have two different efforts in two directions
- Peter: Idea is to completely replace YP with something new, that's the long-term goal
- Hudson: goal to add things to JP that YP doesn't have and v.v.
    - Would have goal of YP (common spec for clients to follow), but be more modern and up to date with current standards
- Afri
    - Team that built a client from scratch - had to compile different versions of the paper (Frontier, Homestead, Byza., etc.) to build client
    - We have no proper versioning on it
- Alexey
    - Looked at JP, it has elements for all the forks, that might be a solution
- Hudson: is anyone in favor of keeping the YP?
    - Peter: let's wait until JP is in a usable state and decide after
    - Fred: there's value in both
        - want a mathematical spec someone can review and verify
        - also want something implementers can use
    - Piper: I think JP checks both of those boxes
- Alexey: Is anyone working on JP? It's been suggested as the spec
    - Hudson: Yes, Everett said someone from Runtime Verification will be dedicated to this and will join our calls
    - Martin: They plan to build an Eth client - there is already an implementation which uses K engine - and put it through hive tests, lib fuzzer, etc.

# Const. timing
- Danno: can we launch it a couple of weeks before ETHDenver in case things go poorly?
    - Martin: I'd rather aim for mid-Jan assuming we don't find another consensus issue
    - Last one was found 16 days ago, since then nothing
- Piper: original plan was forking mid-Jan, is there an advocate for moving things out past Jan?
    - Holger: My suggestion is to set up a new testnet
        - Makes sense to keep Jan. date, I'll drop the Feb. suggestion
    - Mikhail: Seems fine if we get tests ready at least a month before
        - Hudson: Dimitry said most are done, only a few to go, on track to finish at least a month before
- Holger: I took on some additional resp. to help Dimitry with tests
    - Today we merged EXTCODEHASH tests
    - Other tests now in the works
    - [?] from Pantheon, Hugo from Ewasm have joined
    - We are on track to get these tests done
    - We introduced releases for tests, starting with v6.0.0 beta 1
    - So clients can sync testing efforts and compare test results
    - Should go to main 6.0 release in next two weeks or so
- Peter: Cannot rely on test suites covering all corner cases
    - In some cases in geth we reorganized VM code, tests passed but sycning mainnet failed
    - So tests are not bulletproof
    - We need to support fuzzers, if client is compatible with them, we can run for a month against your client; most consensus issues these days found by fuzzers
- Martin: short description of what's needed for fuzzing
    - Needs to be an executable which takes a state test as input and outputs for every opcode a JSON line object that details the operation that's happening in a format called standard JSON output, this is documented on EVM lab
    - Contains things like OPCODE number, name as string, gas, stack contents, etc.
    - Needs to output state root after executing state test
    - That's it!
    - Preferable if clients spit out JSON line by line
    - If it's done in one big chunk afterwards it would blow up the python framework that runs the tests in parallel
    - Currently geth and parity support this
    - Aleth has capability to spit out common format but cannot execute on raw state test; can run in testeth but that spits out a big blob, doesn't work well with lots of output
    - Framework is evmlab, github.com/ethereum/evmlab
    - Production fuzzers running on server
    - This is the framework that runs the fuzzers: https://github.com/ethereum/evmlab
    - This is a little nugget of info about the output format: https://github.com/ethereum/evmlab/wiki/howto-evm#output
- Peter: Passing manual tests isn't enough, fuzzers can catch a whole bunch of other things
- Hudson
    - So looks like we'll stick with mid-Jan
    - Let's discuss further on next call and see if any other issues arise
- Peter: It doesn't make a difference, we can always postpone
- Piper: Let's set a date today, can always push back if necessary
- Hudson: How's Jan. 16? Anybody opposed?
- Peter: If we're going with Jan. 16 then ideally all clients should release stable version with baked-in block number before Christmas

# ProgPoW update
- Pawel update
    - We have three devs from parity, geth, and myself working on implementing CPU part of progpow
    - In agreement about results
    - Sync not finalized yet
    - Some changes, tweaks and tuning, so we are not directly where the spec is
    - Other infrastructure updates
        - Spec written for stratum protocol
        - Including data needed for hard fork and supporting ProgPoW
- Alexey: There was a DevCon presentation about ProgPoW
    - Included saturation numbers
    - I think they were pretty high
- Martin: Yes, numbers presented during workshop are also in a Medium post that was published a week or two earlier, so the numbers can be found publicly there
    - https://medium.com/@ifdefelse/understanding-progpow-performance-and-tuning-d72713898db3 
- Hudson: I'm working on uploading the videos but having ISP issues

# eth_getWork RPC API
- Peter: currently returns three parameters
    - https://github.com/ethereum/pm/issues/60#issuecomment-436588176
    - Been approached by mining pools, they say this is a problem
    - Sometimes when mining a block they recreate a block even though nothing mined
    - Can happen if new oracle arrives of if you receive a ton of new tx
    - For miners, helps to know whether this is a new round of work and should abort or whether it's the same round
    - Parity for a long time has had a fourth parameter, a block number, seems to work fine, easy enough
    - We want to add this to geth
    - Shall we update JSON-RPC spec so it requires returning a fourth param? (Wiki RPC thing)
- Piper: Sounds good to me, let's make sure this goes to inflight EIP for properly specing JSON-RPC APIs

# Conversations about setting up a few processes at DevCon
- We currently have no process on setting up forks
    - We're doing this ad hoc in chats right now
- Would be nice to define processes around important, repeatable actions e.g. deploying a hard fork
- I wrote up a small doc
    - https://github.com/karalabe/eee
    - https://github.com/karalabe/eee/blob/master/eeps/eep-1.md
- E.g. in case of hard fork, would be good to do a simple hard fork on a private testnet first
- Instead of doing a live fork, do a shadow fork where we set up forking clients that fork away while leaving real testnet on its original path
    - This allows testing a few good things like whether clients can cleanly separate
- Please read this doc, see whether other clients and ecosystem participants would follow this playbook
- If traction we can work out all the kinks and expand to whatever level of detail we need
- People asked why there's a need for a separate process, apart from EIP?
    - It's debatable, let's get the doc done first and see whether it fits into an EIP
    - An EIP is more of a functionality spec, doesn't tell you how to do it
    - Whereas EEP is more of a checklist
- Martin: If we want to use this workflow wouldn't it be good to have an appointed "fork director"?
- Peter: That's part of this process; if we decide we need a coordinator (I think we should) then it should go into the doc; step zero is to appoint someone willing to coordinate
    - If we agree in advance to a doc on how hard forks work then everyone is on the same page and things will go smoother
    - What happens in what order at what point in time; clear timeline with clear steps
- Lane
    - I like the coordinator idea, we discussed this during the ETH2 gathering in Prague and there was consensus around this
    - I think EEP should be separate from EIPs (also maybe ERCs)
    - Meta-hard fork planning is a great idea
- Piper: companies in this space have knowledable managers on staff
    - If you have someone on staff who would be good at this and would be willing to help, let us know
- Peter: Can't we create a doc which just tells you what to do?
- Piper: Someone who is coordinating, keeping track of what comes next, etc.
- Lane: Several people reached out and offered their time, let's discuss this on a separate call
- Hudson: JSON-RPC wiki spec
    - Fred: It's publicly editable by anyone
        - Do we need due process to propose and accept changes?
        - Doesn't fit within EIP framework
    - Pawel: ProgPoW takes block number as input to hash function so this is almost a requirement for that
        - Block number is more useful than seed hash
        - More aggressive approach would be to replace seed hash with block number but this could cause more backwards compatibility issues
        - I fully support this change
- Hudson: People seem positive about EEP, let's give it a shot
- Hudson: Lane, Piper and I will discuss PM help
- Hudson: Separating ERCs from EIPs
    - Lane: In brief, I support separating consensus changes from ERCs
        - It's not at all clear to me that these should be in the same repo or part of the same process, they are for historical reasons
    - Hudson: Okay, in the future let's discuss separating them

# Attendees
- Alexey Akhunov (TurboGeth)
- Paweł Bylica (EF/aleth/Ewasm)
- Holger Drewes (EF/EthereumJS)
- Tomasz Drwiega
- Daniel Ellison (Pegasys/Pantheon)
- Danno Ferrin (Pegasys/Pantheon)
- Fredrik Harrysson (Parity)
- Hudson Jameson (EF)
- Mikhail Kalinin (EF/EthereumJ)
- Piper Merriam (EF/Trinity)
- Lane Rettig (Ewasm)
- Adam Schmideg
- Afri Schoeden (Parity)
- Jacek Sieka (Nimbus)
- Martin Holst Swende (EF/geth/security)
- Péter Szilágyi (EF/geth)
- Jared Wasinger (Ewasm)
