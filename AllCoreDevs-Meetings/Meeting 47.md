# Ethereum Core Devs Meeting 47 Notes
### Meeting Date/Time: Fri, September 28, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/58)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=z2mefVnZHpw)

# Agenda

1. Testing
2. Client Updates
3. Research Updates
4. [Constantinople](https://github.com/ethereum/pm/issues/53)
5. [EIP 1108: Reduce alt_bn128 precompile gas costs](https://eips.ethereum.org/EIPS/eip-1108)
6. ProgPoW

Call starts at [[6:17](https://youtu.be/z2mefVnZHpw?t=6m17s)]

# Testing update
* Martin update
    * Got last fix merged into Parity to run state tests
    * Been doing ~half a million fuzz tests last few days
    * Need to work a lot on improving state tests generator
    * No blockers in terms of the engines or false positives

# Client updates
* Geth (Martin)
    * Maintenance releases, nothing major
* Parity (not present)
* Aleth (Pawel)
    * Nothing important
    * Constantinople ready, already reported this
    * Working on some internal changes
* Trinity (not present)
    * Danny: New alpha released yesterday called Ada Lovelace
    * Might be worth downloading it and giving it a shot
* EthereumJ (Dmitrii)
    * Working on Constantinople, haven't finished tests
    * Working on sharding
* Pantheon (Matthew)
    * Now syncing to mainnet chain head
    * Check it out at DevCon
* TurboGeth (Alexey)
    * Made a blog post
    * Started working on testing such as syncing to mainnet
    * Performance tests with Infura
    * Chasing some bugs
    * TurboGeth needs special handling for Constantinople CREATE2 opcode
    * Using selfdestruct, you can replace the code in a contract in a certain way, retaining same address, but losing storage and balance - Martin posted some clarifications to the EIP
    * I want people to think about this, since many people may not realize this - wanna know if anyone sees anything potential dangerous
    * Martin: anyone present on AllCoreDevs when we first discussed CREATE2 should be aware of this already but it may not be obvious to the general public
* Nimbus (Jacek)
    * Slowly making progress through block syncing, fixing bugs
    * Up to ~48,000
    * Working on ETH 2.0, tests for simple serialize that's being proposed
* EthereumJS (not present)
* Mana (not present)
* Nethermind (not present)
* Exthereum (not present)
* Ewasm (Lane)
    * Launching public testnet
    * Did a public call last week, demoed testnet and tooling
    * Focused on documentation, preparing for public launch at DevCon

# Research updates

* Danny update
    * Clients being implemented
    * Sorting through some bugs, improving spec
    * Coming around on standards like networking and serialization
* Vitalik update
    * Trying to figure out the attack/centralization vectors
    * Spec-wise, already more verification than research
    * Also a lot of working happening on P2P protocol side - I'm more worried about this than the other parts but there's been a lot of progress
    * My impression is that the protocol is "the good kind of stable"

# Constantinople
* [Progress tracker](https://github.com/ethereum/pm/issues/53)
    * Geth, Parity, aleth, ethereumj, mana, nethermind - completed implementation of all EIPs
    * Testing still WIP
    * Hudson: we should probably pick a block number today for testnet fork
        * On last call we had chosen Oct. 9
        * How far beforehand do the clients need the block number to be set?
        * We don't need a really large window
        * Martin: If Ropsten splits and we end up with Ropsten Classic, it's not the end of the world
        * Hudson: Can we decide the block number one week before?
        * Martin: It would be nice to know the block number so we can include it in the next biweekly release which is before the next core dev call
        * Next geth release is in ~1.5 weeks
    * Let's go with Ropsten block 4.2M, that puts us at this time in 11 days, on Oct. 9
* Alexey: CREATE2
    * Discovered this a few days ago when updating TurboGeth for Constantinople
    * Because of the way the contract address is calculated in CREATE2, which includes msg.sender, some salt, and the hash of the init code, it means that as long as the init code, salt, and msg.sender stay the same, you can redeploy the contract
    * So it would only work if you first selfdestruct, it's removed from state
    * (And cannot happen in the same block)
    * Later on, after selfdestruct and it's removed from state, you can recreate it using the same init code
    * If init code loads deployed code from somewhere else, gives potential to instantiate contract with different code at same address
    * Storage and balance wiped out
    * You can upgrade a contract (modulo storage and balance)
    * Also allows you to clear out large storage easily - selfdestruct and redeploy
    * This is not possible today since there's a nonce
    * V: Way to achieve equivalent functionality to CREATE2 today is if you use a registry
        * E.g. people access your contract via a certain ENS record
        * Selfdestruct, create new one, new one takes ownership of ENS record
        * That gives you an upgrade
    * Martin: Can use a delegatecall proxy
    * Alexey: This stuff has minimal overhead, doesn't matter if you call a few thousand times, but if you call a few million times, the overhead adds up - whereas with CREATE2 there is no overhead
    * Alexey: I just want to get more people thinking about this and how it can be used
    * Pawel: If that's a feature maybe we should make it more explicit
        * Not so easy to do it now since you need additional contract
        * What would happen if we skip the hash of init code?
    * Alexey: We need init code so you can prove to counterparty that what you will deploy at this address is exactly this code, it's deterministic - then you can open a state channel and do counterfactual stuff

# EIP 1108: Reduce alt_bn128 precompile gas costs
* [EIP-1108](https://eips.ethereum.org/EIPS/eip-1108)
* One of Antonio's developers ran some benchmarks
    * geth performance improvements that 1108 based gas costs on aren't reflected in parity client
    * Ran some benchmarks since new code merged into parity since then
    * Found large improvement in parity performance as well
    * Merged some adjustments to EIP based on those improvements
    * Still not quite as dramatic as the ones in geth
    * Fairly significant, serious boost for snark and BLS verification
    * New numbers in EIP based on parity's improvements, not as good as geth but still significant
    * Benchmarks in the chat and linked from EIP
    * https://gist.github.com/pdyraga/4649b74436940a01e8221d85e80bfeef
* Martin: For easyadd you changed it to 150 gas, which is higher than what the benchmarks suggest
    * For geth a bit drastic, appears to need ~400
    * In updated gas costs for pairing check, what would formula be in benchmark?
* Antonio: Original EIP 5500 + 80k, aggressive even with geth benchmarks
    * We looked at formula that came out of benchmarks Martin did in July as well as our benchmarks against parity, 3300k - picked higher of the two
    * Also cranked up ECADD, ECMUL numbers from original EIP to reflect higher of the benchmarks
    * There's also the call price for the precompile to keep in mind when looking at these gas costs
* Martin: that only really matters for MODEXP and ADD, only 700 compared to 40k
    * For pairing, parity goes below but not by a wide margin
    * Looks awesome, I'm hoping we can reduce it, but not something for Constantinople
* Antonio: We want these to get in as soon as possible, and nine months is a long time to wait
    * Config change for parity
    * 40-50 lines of code change for geth
    * Let's get in as soon as we can manage, whether that's Constantinople or shortly thereafter
* Alexey: most important thing is testing
    * Let's work on this now but assume Constantinople will remain as-is
* Antonio: We are happy to help with testing
* Matthew: Plans to test against any other clients?
* Martin: most clients will not be as fast as geth and parity, unless they link directly to some optimized C library and assembly code
    * OTOH, geth and parity together are 99% of mainnet, should we cater for every client?
    * Clients that want to be on mainnet should link against highly optimized libraries
* Matthew: I'd be interested in evaluating performance of pantheon - Antonio volunteered to help with this
* Pawel: Is there any C library that's optimized with new code?
* Antonio: There is a C lib, done some work to see if we can integrate it into any other clients like Python, not sure yet, but will share when we've done a little more of this work
    * Specific library we're using is MCL, created by Harumi (sp?), support for several curves, BN128 (?) is one of them
* Pawel: I could replace the lib aleth is using with this new one, if that would help with testing
* Antonio: We'd love to help with that, changing the underlying lib in a client is much more dangerous than changing some params though
* Pawel: I still find the C code to be most accessible for languages like Python, we don't have good tooling yet for e.g. Rust to ship it easily to Python
    * If that lib works and we could replace ours, I'd be willing to add python bindings as well if that's something we want
    * Re: Constantinople, if a change isn't ready in time, it's just not included
    * It's a lot of pressure if we keep adding even small changes in the last minute
    * In that case I feel it should go to the next hard fork
    * Dimitry: Any change should be tested on a testnet for at least a couple of months
* Antonio: Our company is Keep Network, Clearmatics wrote some early blog posts but we've been doing a lot of the legwork
* Martin: From client perspective this is a trivial change but it means regenerating a lot of tests, will require some work on underlying test generator, semi-manual work which unfortunately we haven't automated enough yet - so it's harder than it seems
* Pawel: I'd consider additional fuzz testing, we did it before and found some issues, it's a good opportunity to tweak the fuzz tester and how it may find long-running executions
* Antonio: We do feel that the sooner the better, and nine months is a pretty long time to wait for it - we'd like to offer to do whatever we can to get it done sooner
    * We have a geth PR ready
    * We've looked into updating parity and some of the other clients
* Martin: If we lower the gas costs we might want to check, do our test vectors actually cover worst case scenarios? Are there worst case scenarios? Not sure they're fully covered
    * We're very restrictive with gas costs so probably not DoS vector but if lowered closer to limit then we should spend some more time checking that
* Antonio: Certain BLS sig. check and SNARK operations that currently can easily dominate a block, take e.g. 25% of block gas - that's the numerical context, doing one of these operations is just a huge drag on the network

# ProgPoW
* Hudson
    * Theres renewed interest in getting this into a new hardfork
    * Pawel has been doing some benchmarking
    * Martin looking into geth support
    * Afri - working on Rust side of things
* Miss If intro
    * As the public knows, not much has changed
    * The C++ client (aleth) is fully finished, geth client almost finished
    * Had a CPU verification slowdown that has been fixed
    * That's all there is to it
    * Once we see more interest from Ethereum development community to adopt ProgPoW, then we'll have developers accordingly working on all clients
    * Until that point I don't think it's worth wasting the man hours or the money on a project that might be ignored
    * I did have a wonderful meeting in person with Nick Johnson and it's come to my attention that there is a lot of misinformation on how hardware actually works, on how ProgPoW is tuned to hardware, and in general on how the algorithm remains tuned to a GPU card and balances efficiency difference betwen GPU and ASIC
    * That misinformation is our fault (If-Def-Else) because as creators of algorithm we need to make sure we're educating developers and entire community on how it works
    * So if you have questions now is the best possible time to ask, we are also available by email
    * We'll be making a Medium post along with test results, community has been doing wonderful testing
    * Bitcoin Interest - small coin, it's already implemented, many miners happily mining it in a safe production environment
* Hudson: Along with Pawel I've been communicating with some major GPU companies, it's showing promise
* Pawel
    * I must disagree with the statement that C++ client is almost ready
    * From code perspective, I tried the library, a fork of ethash library
    * There's a number of issues with this change
    * First of all, it just replaced ethash with ProgPoW, we need both of the algorithms side by side
        * Miss If: ifdefelse/cpp-ethereum - completed, ProgHash no
    * I couldn't get any benchmark from proghash
    * Took over 1sec to verify header, something is not right
    * I didn't have time to check it on this level
    * I started implementing some pieces of ProgPoW myself to get familiar with it
    * It's possible I can finish this part myself, I haven't seen any PR submitted to any project I maintain, so that's a bit worrying
    * Miss If: We've been implementing them but keeping them on our own repo, we haven't done any PRs, but it would be better to work closely with client devs because as our geth implementation has proven we are not masters in all these languages, so we're going to need some assistance
        * We can do dev grunt work
    * Pawel: I'm not worried that it can't be done
    * Re: the EIP itself:
        * The official discussion board is ethereum-magicians.org, I'm posting questions there, it's not always easy to get a response there
        * In the EIP there's many details that are not explained
            * e.g. what popcard (?) is, what CLS is
            * Obvious for some people maybe but we need more details about e.g. how rotation works, can you rotate by more than X? Edge cases
            * To implement ProgPoW I have to go to your implementation to figure out details, EIP doesn't contain enough details
        * Keccak hash function: I tried to figure out the parameters of this, it's kind of an exotic construction
        * Miss If: 32/64 bit shift? Pawel: was speaking about this before
        * Keccak hash function: it has permutation of size 800 which is different from SHA3, if I calculated correctly, the output in terms of security bits is 176, this is a bit lower than the one we used, and only 64 bits taken from this anyway
        * I don't have any cryptographic background but I want to ask if that is any concern in terms of security
    * Miss If: My background re: crypto is public, no, it's not a security concern to me
        * GPUs natively 32 bit architecture, F1600 twice as long on a GPU
        * That gives you a nice little speedup with ASICs
        * We can't consume all of those bits very efficiently, so reducing the size doesn't decrease your security at all
        * It's quite public, I can elaborate on that on EIP, there's been a public study on F1600 vs. F800
    * Pawel: I'm not worried about permutation size, I'm a bit worried about the bitrate, it's quite high compared to permutation size
        * Also no padding to this hash function at all
        * This question is also on the Eth Magicians board
        * If you can explain it, I'd be happy to have it as part of the EIP
* Martin: I haven't gone as deep as Pawel but I've implemented it in geth and done some benchmarks
    * It's a simple change, verification time doubles, not a big problem in my opinion
    * The other day I mined a bit on a CPU, even on lowest difficult, switches over from hashmult to ProgPoW at block five, first few blocks quite quick, then takes a couple of minutes to mine each block after switch over, at lowest difficulty
    * Doesn't really matter other than for generating test chains
    * I would've liked to generate a long chain with multiple epochs, turns out that's difficult to do
    * From a testing perspective, I have a feeling that we should not and cannot use existing test infrastructure
        * Because this has nothing to do with EVM semantics, block rewards, uncles, etc.
        * Only thing that's needed for testing is snippets of chains
        * Only quirky behavior is at switchover block, if ProgPoW block has uncles with Hashimoto-style PoW
    * I really think this change could be implemented in parallel with Constantinople, from tech. perspective they have nothing to do with each other, although from political PoV they might be very related
    * If the technical underpinnings are there, if Pawel thinks this is good and that people who are in the know deem it to be ASIC resistant, then I think it's a good change and I'm for including it ASAP
* Miss If: On implementation side, you mentioned something about the epoch, you'd prefer to generate a long chain, is that correct? Would you like us to make a test vector implementation of that?
* Martin: Yes please, min. 30k blocks
* Miss If: By implementation, in the implementation ProgPoW is meant to change every 25 blocks, this is actually very hard to do because you need a bridge between miner and pool requiring stratum implementation, next easiest thing to do is per epoch but this is not nice for testing
    * So we can do a test implementation where you can keep chaining it but don't put it into a production environment
    * I'll have someone work on that this week
    * We got it down to 9ms as well, any assistance with other optimization folks see would be helpful, it's meant to be 8ms in theory but go isn't our strongest language
* Martin: I'm sure it can be lowered a lot with assembly but I think the most interesting thing to do is to make sure that all the things Pawel has listed that are required for ProgPoW adoption are implemented
    * So that there's support in mining protocols and mining software
* Miss If: Most of those are clarity needed in EIP, or in code, more public reference, checking bitrate size vs. permutation size, padding, etc. - all noted and will be done, thanks for this great feedback
* Pawel
    * Some time ago I made a list of changes that in my opinion are required to do the switch
    * https://ethereum-magicians.org/t/what-has-to-be-done-to-get-progpow-on-ethereum/1361
    * It's outside of ProgPoW implementation itself
    * In my opinion we need to propose a stratum protocol that will include info in algo. used by miners, no info. about that there
    * This is the biggest one, can start work on this very soon, it's not related even to client implementations
    * I might find some ppl willing to work on this
    * I plan to propose an EIP describing this protocol and implement it in ethminer on the client side
    * Not sure about on mining pool side, if there's a chance someone will adopt that, but EIP is a good starting point anyway
    * Please take a look, leave comments, I may be wrong about some of that
    * I struggle with commenting on an EIP as complicated as ProgPoW, EIP not in review mode, it's merged as a draft, no way to leave a comment in EIP to address particular issue
        * Easier to put discussion about a single line in proposal rather than using a separate medium, as a group we should discuss if there's a way to improve this process
        * For small EIPs less of an issue since less lines to comment about
        * For this EIP I'd like to attach comments to particular lines to make it easier for the author to address
    * Hudson: I understand your concern, we can consider changing this in the future
        * The reason it's the way it is, is because you can have multiple discussion links
        * E.g. link both to FEM forum and also a link to a repo that the submitter maintains where you can line-by-line comment on the EIP and on implementation in that repo
        * That would probably be a good idea, I think Miss If has to go
* Alexey: I looked at geth code (Martin's PR)
    * 80ms verification time reported
        * gist attached to PR which contains some optimizations, mostly about avoiding extra allocations/copying
        * But these optimizations don't make any difference because biggest cost is access to data item
        * Later on, change made to reduce number of accesses
    * From reading description of algo. I get the general idea but if people really know the reason they can explain it more simply
        * A lot of ppl including me don't really know what I'm doing, I'm trusting that someone more clever than me gets this, but I don't
        * Some people privately discussing - don't feel good about this
        * Maybe someone can write down some exposition about exactly why the current ASIC tech. would not be able to handle this - so people can analyze this critically - rather than saying "I am an expert and I get this"
* Mr. Def - I understand this - would be good to get info on your specific concerns
    * We've been bad at handling FEM discussion, will be more responsive there
    * In terms of why this algo. is ASIC resistance, we should all start from the point that: the algo's goal is not to be ASIC resistant
    * We start discussion from the perspective that GPUs are ASICs
    * So we're not trying to be ASIC resistant, we're trying to be friendly/tied to a particular type of ASIC which is the GPU
    * In optimizing for a specific type of hardware the goal is to maximally utilize all the functions of that hardware: a large register space that's expensive
    * Not forgetting starting point of why ethash is strong: it's still memory bound
    * Algo starts from place where it's still predominantly memory bound
    * Also has to use additional register space that GPUs are able to provide, needed for additional math
    * On top of that, adds the programmatic aspect: exact series of math ops that you're running is changing in every epoch or as Miss If proposed with the stratum implementation, every 25 or 50 blocks to change even faster
    * When you do something like that, the problem with implementing a different or "more custom" ASIC is that you would have to design the ASIC to be flexible enough to capture all the possible variations/evolutions of the algo, or an ASIC that pre-designs for every variation/math ordering in the evolving algo
    * If you pre-design for every possible algo the ASIC just explodes
    * If you try to design for the progammability and register space/file size then you basically have something that is a very big ASIC that's also applicable to many other math problems
    * If you design a general math processor - that's the goal of this project - having more general math processors in the world is a good thing, having more flexible computation units is a good thing, at least until we have PoS
    * Leveraging existing install base of more general math units was the goal of this project
    * We're basically trying to force a custom design to be "not that custom" - you have to be flexible to varying and changing math at a very rapid pace, enough variation that you can't predesign for all of it, you have to pay additional silicon to even be able to execute the math
    * If you have specific implementation questions in terms of why ASICs can't keep up/can't be designed for these math variations we can deep dive on it, our responses would be best to be on some public forum like FEM, so everyone can see the response
* Hudson: Will be a medium post as Miss If said, explaining some of this
* Mr. Def
    * We tried to make it as optimized as possible for GPU but it's true that it's not the most optimized piece of hardware
    * GPUs have floating point paths that aren't appropriate for cryptography
    * Small part of silicon that's unused, other parts e.g. display output are also unused
    * When GPU manufacturers reviewed this algorithm the consensus was that 20% of GPU is unused, so 20% savings you could have if you stripped out all the unnecessary bits of the GPU
    * Economic analysis of savings with a more economically efficient savings, saving this silicon area, you can look at die area assessments, if you look at GPUs that are most popular in the mining world today (480, 580, some GP-106), it's roughly $50-60 for a piece of silicon, you save 20% or around $10, $200 total manufacturing cost of the board, you're saving an insignificant amount of the total board cost
    * You *can* have a more custom board design for ProgPoW than GPUs but economically speaking it's not a significant impact to the economics - wouldn't cause someone to do a custom design, especially given amount of volume GPU manufacturers have access to vs. custom design, economic structure of doing an ASIC wouldn't be worth it
    * We've also seen comments where GPUs are moving further away from doing simple math, but at least in this generation, until we get to PoS, I think this is a reasonable interim for PoW before PoS
* Alexey: I read most of the things said on Github
    * I understand that you're optimizing for GPU and introducing things that are harder for ASICs
    * When you said "we talked to the GPU manufacturer and asked them to do this and that" - is this information available?
    * Mr. Def: we reached out to manufacturers, I don't think this is public information, however, they advised that there are some very good reverse engineering analyses, existing technical analyses of this generation of silicon
        * Let me see if I can dig this up and point these out
        * I suspect GPU manufacturers would not be that excited about doing exact detailed area analyses because they have competitive concerns
    * Alexey: I've done some GPU programming myself a few years ago, you can profile it to see how much bandwidth you've consumed, how many registers consumed, etc. - could you run this and could we have some data that proves that this algo. is utilizing these resources on a GPU? E.g. 90% of bandwidth.
    * Mr. Def: I think that's possible, we'll work on this

# Testing update
* Dimitry
    * Been mostly refilling all of the tests with recent changes from cpp testeth
    * State tests are done
    * Constantinople VM tests are updated
    * Changing how hash of test is calculated
    * That's why all of the tests are refilled with different hash
    * Trying to fix python script on test repo to merge this hash and check
    * Currently working on blockchain test regeneration
    * Would like to keep some of these tests being mined with PoW, some interesting cases where blocks have many different uncles, just to see how difficulty is generated
    * Can deliberately change some parameters of some blocks
    * Some tests where blocks are getting timestamp shift, forward or backward, some interesting cases with difficulty checks in blockchain tests this way
    * If we are to implement a new way of mining, there will be some changes to blockchain tests on interface level - manually set which blocks will be mined with new vs. old difficulty algorithm
    * ProgPoW is not happening in Constantinople but eventually we'll implement different PoW so I'll work towards that
    * Refilling blockchain tests takes a lot of time with mining
    * Some errors with mining or refilling tests with cpp client, takes some time to understand how it affects test generation, will take some time to regenerate blockchain tests
* Martin: Are state tests merged or in PR?
* Dimitry: I think I can't merge until I fix python script, kind of stuck because of YAML test at the moment
    * Piper suggested some helper pattern, JSON hash, I'd appreciate that
    * I could disable check for YAML for now, could merge tests if necessary in near future, but you could just pull from PR and see how Hive is working

# Attendees
* Alexey Akhunov (TurboGeth)
* Meredith Baxter (PegaSys)
* Paweł Bylica (EF/aleth/ewasm)
* Vitalik Buterin (EF/research)
* Greg Colvin (Fellowship of Ethereum Magicians)
* Dmitrii (Harmony)
* Daniel Ellison (ConsenSys/LLL)
* Matthew English (PegaSys)
* Hudson Jameson (EF)
* Eric Kellstrand (PegaSys)
* Lane Rettig (Ewasm)
* Danny Ryan (EF/research)
* Jacek Sieka (Status/Nimbus)
* Martin Holst Swende (EF/Security/Geth)
* Special guests
    * Miss If (If-Def-Else/ProgPoW)
    * Mr. Def (If-Def-Else/ProgPoW)
    * Antonio Salazar Cardozo (Keep Network/EIP-1108)
