# Ethereum Core Devs Meeting 51 Notes
### Meeting Date/Time: Fri, December 7, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/64)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=V4sAl-B8yZU)

# Agenda
1. Testing
1. Client Updates
1. Research Updates
1. Working Group Updates
1. [Constantinople HF](https://github.com/ethereum/pm/issues/53)
1. Openness of meetings
1. ProgPoW update 
1. Quick announcement re: coordinator roles
1. Date for next meeting?

# Testing
- Brian intro
    - Recently hired to work full time on making testing better
    - Not sure what that means yet - easy to generate and use tests
    - I've talked to Trinity, have an idea what they want
    - Please reach out and tell me what you'd like to see improved
- Dimitry
    - Finishing EXTCODEHASH implementation
    - Discovered that every EXTCODEHASH test can be used to test *SIZE, *COPY, and *CALL
        - Not related to Const.
        - Each could be enhanced like that
        - Received a lot of help writing these tests from [Andrei?] and Hugo
    - Finishing things still on list
    - Still waiting for contribution on bitshift test review
    - Waiting for hive results to see if there are any issues we need to fix, or new tests we need to write
    - Martin said Hive has some maintenance
    - CREATE2, SSTORE tests ready, bitshift ready but needs review, EXTCODEHASH mostly covered
- Martin
    - We're in process of rewriting Hive and making it more robust
    - In the meantime it's kind of flakey
    - Will also see some additional tests, P2P stuff I mentioned previously
    - Regarding tests
        - Updated all tests for geth less than two weeks ago
        - All tests pass
        - Kind of expected client devs to import and run tests in native settings, despite having Hive
        - But hoping to have Hive up and running again within next couple of days
        - No new failures on fuzz testers running for at least last couple of weeks
        - So I'm fairly confidence in code in geth and parity

# Client updates
- Harmony/EthereumJ (Mikhail)
    - No major updates
    - Mostly working on Beacon chain impl., been major spec changes lately, still catching up over next couple of weeks
- Parity (Fred)
    - Released 2.2.2 with new improvements, some exciting stuff
    - Improves sync performance
    - Pairing stability, fixed pairing issues where it now finds a lot of pairs but fluctuation in pair counts
    - Block propagation fixed - waiting to see effect on network
    - Other minor things
    - Decided to move jsonrpc APIs not yet accepted in an EIP but implemented anyway (eth.person or web3 namespaces) - now disabled by default, enable with flag `-jsonrpc-experimental`
- Geth (Peter)
    - Database optimizations
    - Just trying out ideas and looking at charts
- Turbogeth (Alexey)
    - Fixed bugs found with Ropsten sync, syncs now
    - Started to work on test suite
    - Never run tests, have issues, fixing them
    - In order to make it work, had to modify boltDB
    - Now can run boltDB in in-memory mode, nothing on disk, wanted to try this for a long time
    - Client still not ready for Const., CREATE2 revival still not addressed, will address this
    - Found myself using turbogeth a lot recently as it's useful for extracting data I used for state rent proposal
    - 300gb database on external DB, made some copies of it and running data analysis
- Aleth (Pawel)
    - Fixes and improvements to network code
    - Probably today will have a new tool that will work as a bootnode, can be used similarly to geth bootnode, want to put somewhere on mainnet or testnet as alternate implementation
- Nimbus (Jacek)
    - Been focusing on parts of VM related to DevEx, e.g. debug and tracing
    - Let us know if you have any ideas, this is a good time to discuss
    - First Eth 2.0 testing framework and PoC things are landing right now, discussion on gitter
    - Good time to influence direction of Eth 2.0 testing
    - https://gitter.im/eth2-0-tests/Lobby - Ethereum 2 testing working group looking for feedback on the first proof-of-concept test vectors - now is a good time to join :)
- Pantheon (Danno)
    - Planning on minor release next week
    - Includes contribs from external contributors
    - Including Goerli support
    - Looking into [missed this]
    - Beacon chain impl.
- Mana (Andrew)
    - Syncing Const. blocks on Ropsten, anticipating full sync shortly
- Adam (Swarm)
    - Swarm is a part of geth, in same repo with own semantic versioning
    - Last geth release contains swarm improvements such as access control on feeds
    - Will be announced with a blog post coming with next major release of geth
    - Last two weeks, introduced user perception tests [?] and benchmarks
- Ewasm (Lane)
    - Working towards testnet spec v3
    - Released #Eth1x proposal, working towards this

# Research
- Danny update
    - Revisions of phase 0 - Serenity beacon chain spec
    - Readability, reorg., polishing data structures - major edits of spec
    - Tough to keep up, homing in on first version of release candidate
    - Phase 1 - sharded data chain algo. - data structures forming there
        - General algorithms known
        - Being specified
    - State execution, account structures - lots of thought going into this
    - Handful of proposals on ethresear.ch that V posted that we're looking for feedback on
    - Justin and VFD alliance: increasing number of blockchains interested in adding VFDs in various ways
    - Begun to do Beacon chain implementation in py-evm
- Justin did talk on VDFs at Devcon, video online
- Other DevCon IV talks should be online today

# Working group updates
- Whiteblocks (Zak)
    - Putting together specs for testnet
    - Working with 1x in simulation group
    - Relevant for testers as well
    - Will schedule separate call today that I'll post in issue that I opened
    - Please join and provide feedback, we can start getting specs for testnet and building it out
    - Will be powered by Whiteblock framework
- Alexey
    - I have a writeup on state rent - first version of proposal published, received a lot of feedback
    - Most interesting one: V suggested using CREATE2 opcode and some other things to implement something I proposed to do with linear cross-contract storage
    - I managed to implement ERC-20 contract based on these ideas
    - It actually works, can mint and transfer tokens
    - Interesting to get feel of how you'd use CREATE2
    - Commented on issue in solidity, created thread on EthMagicians for ppl interested in creating new primitives to make it easier to work with CREATE2
    - Right now you have to copy and paste bytecode into source code
    - Linear cross-contract storage will most likely be dropped from next version of proposal
        - Priority queue too
        - But I'll still look into linear storage elsewhere e.g. Ewasm integration
    - I've asked PegaSys team to help with PoC, Adrian Sutton created first prototype, reviewing and hope to get my prototype running as well - so this is based on pantheon for now
    - Done a lot of data analysis, not all included in proposal
        - Trying to run heuristics to identify all ERC20 tokens in state
        - Looking for successful token transfers
        - Around 71k contracts
        - Take around 53% of all contract storage
        - Cryptokitties is also ERC-20 - has both this and 721
        - Very important class of contract, that's why I did sample implementation using V's ideas
    - Next step will be to look into on-chain order books
    - Put some ideas about how to identify them
    - Will do some analysis about token nexus contracts - tokens go in and out - likely will be on-chain order books
    - Might be able to compress state using generations
        - Looking into how we can have a very compact representation of current state
        - E.g. all contracts that GasToken creates could be generated using minimal seed data
        - So it would not take a lot of space in the snapshot
        - Not sure how well suited other clients are for data analysis - but someone could look at Google Ethereum dataset - see if it's possible to reproduce the data analysis I did, some in state rent proposal, plus this ERC20 analysis
        - If someone gets the hang of this, might be a good way to split up this work, there's so much to do in this workstream and I can't do it all alone
        - So trying to enlist people to do PoC, data analysis, maybe mods to Solidity and Vyper to make all this easier
- Ewasm
    - See proposal and FEM thread
- Peter "working group" on state pruning
    - FEM thread: https://ethereum-magicians.org/t/ethereum-chain-pruning-for-long-term-1-0-scalability-and-viability/2074
    - Long Github gist about two weeks ago (proposal)
    - In blog post I mentioned that I think there are two viable approaches we should experiment with
        - IPFS and Bittorrent
        - But both kinda of suck
        - Want to experiment with Felix's ENR work
        - Tiny extension to discovery protocol, really elegant
        - Nodes can advertise certain capabilities
        - Most infra. in place already
        - Want to play around with it where nodes advertise that they're a light or full node with certain datasets available
        - Trying to figure out whether we could do the whole historical state retrieval in protocol without needing to hack another decentralized protocol for it
        - Not sure if it's possible, but this is a third direction that may be valuable, need it anyway for light servers
    - Q: is this discovery V5?
    - A: depends how you define it, it's different, but Felix wants this ENR work to become new discovery v5
    - Problem is that it was hacked into protocol but not scalable
    - ENR approach is clear, there are a few EIPs open, quite a lot of published material
    - Danny: We are discussing using mature version of Dv5 for advertising which shards you're participating in
    - Peter: Considering putting historical state on top of that mechanism
    - Can't yet see single proposal that will work

# Constantinople hard fork
- Afri [block time proposals](https://github.com/ethereum/pm/issues/64#issuecomment-445170201)
    - Last time we decided to talk about a block number at this meeting
    - I just put down some numbers
    - Did calculations to see how much it could vary if we target a Weds - would most likely fall on a weekday
    - Afri proposed block 7080042
    - Lane: have we always used even numbers ending in -0000 in the past?
    - Alexey: We don't think someone will start super mining to speed up the fork do we?
    - Danny: Would be very expensive on mainnet
    - Afri: very unlikely because of high difficulty of mainnet. Worst case scenario, if price of Eth continues dropping fast and a lot of miners stop mining then it could slow us down
    - Block times have been stable recently so this is not a concern
    - Martin: We'll put block number into next release with possible commandline option to delay it
        - Only reason to change block number again would be if we find another consensus bug
    - Hudson: All previous ones have been -000
    - Hudson: Do people prefer the palindrome or sticking with -000?
    - Peter: palindromes could be hard in the future
        - Easy if block numbers still in the millions'
    - Greg: four zeroes, keep it easy
    - Palindromes for testnet, four zeroes for mainnet - let's do this
    - So let's use 7080000
- Stireby update
    - [missed a bit]
    - Alexey
        - Failure was that there was a GPU miner, we fell prey to this because spec was public
        - Plan was to have a bit more mining, didn't happen
        - Not going to push to have another one
        - I think this was worth doing
    - Martin: Suggestion for new PoW testnet called Gangnam with more genesis alloc, can deprecate Ropsten
        - For dapp testing
    - Peter: Good time to bring up a few discussions
        - We agreed we don't want to continue Ropsten
        - But do we want to relaunch a PoW or instead do a PoA network?
        - Afri & co. have been working on Goerli testnet
        - Would mean we don't have a public PoW testnet but we could always do public PoW testnet forks just to verify PoW and difficulties when we need to do a hard fork
        - Not too much point in running a PoW replacement for Ropsten
    - Martin: We'd drop all Trinity, aleth, and those that haven't yet implemented clique yet
    - Afri: This can be done
        - With all devs out there we can do this
        - Agree with Peter that going fwd with PoW not feasible, this Stirby experience showed how unfeasible PoW testnets are
        - Esp. having one for apps not for consensus needs
    - Mikhail: Fresh test networks not good for testing difficulty bomb delays - block numbers too low, not yet activated
    - Zak: join this testnet call since we can create testnets with relative ease that are provisioned and controlled
    - Peter: We can create purpose-built testnets to test difficulty adjustment - for everything else PoA is a saner approach from dapp developer perspective
    - Zak: Will probably want different consensus algos in different testnets for different reasons - purpose built
        - Provisioning, ensuring adequate activity is the hard part
    - Peter: if we want a purpose-built testnet to test difficult adjustment then we don't need any activity
        - For other stuff PoA works fine
    - Mikhail: Could add configuration for difficult bomb and delays
    - Peter: Don't need to make a decision about this here
        - If we want to replace Ropsten it might be a good idea to do a PoA testnet
        - Everyone please think about it, if someone has a good reason why it's a horrible idea we'll consider that
    - Zak: Activity, background traffic will affect consensus and various metrics within the network
    - Peter: This is the point of having a public testnet, have traffic etc.
    - Alexey: Let's explore option of purpose-built PoW network with Zac and then come back and discuss more on next call, whether this is feasible, PoW for specific things and PoA for everything else
    - Zak: These testnets can be ephemeral, not entirely public, will be permissioned, activity and behavior will be automated with our tools
    - Hudson: This is a good topic for the next meeting
        - Will Goerli be compatible with ETC? Is that a problem?
        - Afri: No, it will not have ETC compatibility
        - But we work on something similar for ETC

# Openness for meetings
- Hudson: Enough people who said "over my dead body" re: any type of closed meetings
    - So we will have open meetings for now
    - Less inclination to do this for these calls
    - Not sure about in person yet - technical feasibility is different
    - Won't have any more "Eth1x" / mainnet improvement calls as WG all created now
    - So we'll just keep doing what we've been doing
    - If anyone has a differing opinion speak now or speak to me privately later
- Martin: There are WG, we will talk within them
    - Is that frowned upon?
- Hudson: That can be private or public, it's not a core dev meeting
    - There was some confusion around that
- Greg: There was useful discussion on where to make the call about what you open up and how much
    - It's a matter of judgment
    - From chat: While we worry about not feeling free to speak our minds in public in the face of a clueless press, I used to help organize anti-war actions with FBI infiltrators at our open meetings, and a press that would accuse us of violence when the cops had finished beating us.
    - When I did war demonstrations, we had FBI and CIA infiltrators and a press who would accuse us of violence after the police beat us up
    - So I shrug and say, this is important but we don't really have that much on the line, it just isn't that hard

# ProgPoW update
- Pawel: Last two weeks, there's one reported issue left, reported at beginning of this week, need to resolve
    - Solution is decided but requires some small changes to implementation to mitigate small flaw in algorithm
- Martin: Had implementations in C++, ethhash, verifiers for geth and parity, then spec changed, geth and cpp updated, parity hasn't yet implemented latest changes
    - Some more discussion about potentially changing spec
    - Two clients in sync 
    - If parity implements most recent changes then we could launch a testnet
- Martin: We had discussion with various people in crypto communities
    - One is David Warwick (?), creator of Zia
    - Got his approval to quote him
    - ProgPoW, if we were to replace hashimoto S/ethhash with this, it would probably keep ASICs away for 1-1.5 years
    - If we increase the resistance towards ASICs then that could itself increase centralization because only a very advanced ASIC manufacturer could afford to R&D such an ASIC that would get efficiency gains
    - So he believes it would buy us 1-2 yrs, but another approach is to use an algo which is extremely ASIC-friendly
    - We could adopt ProgPoW now and if a year from now we still don't have PoS, we might consider switching to something very ASIC friendly which even a small manufacturer can produce
    - Regarding prevalence of ASICs on network today, it's very hard to find numbers
    - Have been reported from various sources but none can be taken as fact
    - No records on units manufactured or sold so it's hard to take that into account
    - Some people think the fact that we're implementing ProgPoW is already decided, this is not the case, we are open to other options
- Alexey: I started to think about ProgPoW more because of eth1x proposals, elephant in room is what are other things slated for eth1.0
    - ProgPoW which will take some amount of work
    - Second, Justin's interview for Epicenter, he said the reason they want to develop a VDF ASIC so that no one else can get a major advantage by creating something much much better
    - I'm glad Martin mentioned as well that there is a potential downside (re: centralization)
    - I want people to explore both
- Hudson: Reminder that these eth1x roadmap working groups are still not finalized
- Lane: Would it make sense for the new app testnet to be a ProgPoW POW testnet?
    - A: Not really
    - Martin: Just envelope of blocks, doesn't matter whether they are full or empty
    - Pawel: We want a testnet with a switch from one algo to the other, so not pure ProgPoW, or switching back and forth, let's keep them separate
    - Martin: Try different configs with a series of testnets

# Quick announcement re: coordinator roles
- Hudson, Danny, Lane, Afri, Piper, Casey, Jamie Pitts have been getting people together to discuss coordinator role
    - Person/people in thids role could help out with hard forks with Hudson and Afri
    - Also EIPs and core devs calls
    - Will be announcing them over the next few months, starting in January
    - You'll start seeing more of that
    - Main goal is to lighten load for Hudson, Lane, Afri and others who have been handling coordination for things like core devs calls
    - Also to train people as future PMs for teams
    - We'll work hard to get them more integrated into these calls, do it in a way that supports the core devs
    - Idea to make it as easy and stress-free as possible for core devs

# Date for next meeting
- Anyone opposed to skipping next call for holidays?
- No opposition
- Next call will be Jan. 4

# Attendees
- Hudson
- Lane
- Alexey
- Pawel
- Peter
- Fred
- Mikhail
- Zak Cole
- Fred Harryson
- Dimitry Khoklov
- Brian
- Jacek
- Danny
- Danno
- Andrew Gross
- Daniel Ellison
- Afri
- Martin Holst Swende
- Greg
- Adam Schmideg
- Shahan Khatchadourian
