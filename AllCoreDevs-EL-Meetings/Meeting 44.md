# Ethereum Core Devs Meeting 44 Notes
### Meeting Date/Time: Fri, August 10, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/52)
### [Audio/Video of the meeting](https://youtu.be/0Lyn5OryooA)

# Agenda

* Testing
* Client Updates
* Research Updates
* Three competing EIPs to delay the difficulty bomb and/or reduce the block reward:
    a. EIP-858 - Reduce block reward to 1 ETH per block.
    b. EIP-1227 - Delay bomb and change rewards to 5 ETH.
    c. EIP-1234 - Delay bomb and change rewards to 2 ETH.
* Constantinople
    a. EIP 1014 Issues
    b. EIP 1218: Simpler blockhash refactoring. We are looking for a reason to implement this or anyone who will champion this. Otherwise we will drop it.
    c. EIP 1283/EIP 1087: Net gas metering for SSTORE operations: 1283 is an alternative to 1087 created due to issues Parity was having implementing 1087. Read 1283's motivation seciton of the EIP.
    d. EIP-1109: Remove call costs for precompiled contracts.
Fellowship of Ethereum Magicians Update (didn't get to this on the last call)

Call starts at [[8:04](https://youtu.be/0Lyn5OryooA?t=8m4s)]

# Testing update
* [Dimitry's update](https://github.com/ethereum/pm/issues/52#issuecomment-412042587)
* Hudson will add these to [Constantinople progress tracker](https://github.com/ethereum/pm/issues/53)
* Dimitry asked for comments
* Martin: re: EIP-1014 Skinny CREATE2
    * we haven't finalized the address format, there are two options in the EIP
        * Do we want to include init code or hash of init code?
        * Argument in favor of hash of init code: in many situations it's easier to use the hash
        * Easier to calculate on chain, maybe easier for hardware wallets
    * Do we want to use an RLP format? Prepend with 0xff?
        * Option 1 preimage may collide
        * Prepend with 0xff or use an alternative RLP
* Hudson: I'll add to tracker that this is not finalized
* retesteth update - see link to Dimitry's update above
* Also suggests we drop blockhash refactoring since we already have a lot of changes going into the hard fork
* Martin: We're getting ready to do fuzz testing but need PRs to be equally implemented in geth and parity
    * Hive: recently integrated aleth (cpp-ethereum)

# Client updates
* Parity (Fred)
    * Last week we imnplemented 1087, 1014
    * Remaining question: we'd give 1087 a shot, we did, ran into some issues, Wei will describe this in more detail later on this call, we have an alternative proposal
    * Otherwise we can have full Constantinople compatibility within 1-2 weeks
* geth (Martin)
    * No major changes recently
    * Peter still working on pruning which is pretty complex
* aleth (Pawel)
    * Working mostly on Constantinople changes
    * Better specified ones are implemented
    * Releasing 1.4, we have an RC, binary available on Github, if no issues found we'll release final version
* EthereumJ/Harmony (Mikhail)
    * Started working on Constantinople
    * 1087 relatively straightforward to implement but waiting for a final decision on 1087 vs. 1283
* Trinity - no one
* ethereumjs - no one
* nimbus (Jacek)
    * implementing crypto primitives
    * passing all VM tests
    * splitting dev resources into two parts
        * core ethereum 1.0 chain
        * sharding chain, getting a beacon chain going as soon as primitives are built
    * opened status.im/nimbus Gitter channel, bridged to Riot channel
    * https://gitter.im/status-im/nimbus
    * ECDC videos out, posted on Twitter and AllCoreDevs channels
* mana - no one
* nethermind - no one
* PegaSys (Matt)
    * still working on mainnet sync
    * were at 2.8mm, now up to 4.46mm
    * still implementing zk-snarks precompiles
    * stabilizing networking code
    * JSON-RPC support
    * nothing on cons
* ewasm (Lane)
    * Continuing to work on Rust, AssemblyScript tooling
    * precompiles in Rust
    * work continues on testnet devops
    * EEI design and versioning, we've got a tentative versioning system, sealing off current version and beginning to add some EEI methods that deviate a bit more from EVM compatibility
* TurboGeth (Alexey)
    * latest instance has been following the tip of the chain for about a week now, seems stable
    * currently testing and fixing RPC API
    * after this is done it will be functional
    * planning to test with Infura first, since they'll be among those who will benefit most from this
    * I'll benchmark against geth, think there will be some advantage
* Research update - no one

# Difficulty bomb, reduction/increase in block reward
* Everyone agreed on difficulty bomb delay
* But we're stuck on what to do about the block reward
* We should invite miners to this call to give their opinion
* This is technically easy so no time pressure to get this into Constantinople
    * Alexey: Didn't Casey say something about this being difficult to test on a testnet?
    * Martin: In order to test the difficulty calculation formula, we can't run the regular block tests because we need millions of blocks
        * So for the last fork we implemented a new kind of test, in standard test case repo
        * Doesn't resemble existing state/blockchain tests, so required client implementers to add new test harnesses
        * This time around it should be easier since hopefully all client implementers already have that
* There are a bunch of competing EIPs on this but none of the authors/champions are on this call
* Let's invite them to the next call
* This is less of a technical question and more of a philosophical/economic question
    * What's the right channel for discussing this and similar issues?
    * Fellowship of Ethereum Magicians?
    * #EIP0?
    * All Core Devs call?
* Jordi: We should try to keep the same asymptotic supply over time constant
    * So we should decrease total reward at the time the bomb begins
    * So we have the same total supply
    * This is what was done last time
* FYI: Afri posted a bunch of useful links/resources on the options here
    * https://github.com/ethereum/pm/issues/52#issuecomment-408807120
* Martin: Problem isn't that people aren't aware of discussions/haven't read, it may be more about how we make the decision - e.g., should there be some sort of voting on this call?
* The risk here if we go too far in the reduction direction is that we lose miners, that they switch to mine another chain
* Greg: Maybe the EIP authors should debate the various EIPs on the Magicians forum
* Boris: A call may be better than "more text"
* Should we do a debate, should it be more or less formal?

# Constantinople
* Progress chart shows where people are implementation-wise
* Skinny CREATE2
    * Parity has been having issues with implementation
        * Wei: Spec not compatible with EIP-86
        * We also support EIP-86 in our plan right now
        * Minor issues
        * Stack order different, creation address format is different
        * CREATE2 opcode is different
    * What needs to be decided for Martin's issue?
        * Should we include the init code or SHA of the init code?
        * EIP-86 uses the SHA of the init code
        * Sergio also thinks this is a good idea
        * Has nice property that input to final SHA function has fixed length which is nice
    * Wei: Our problem is that EIP-86 is not compatible with Skinny CREATE2
        * So for us any solution is probably okay and we want to make the two specs compatible
    * Alexey: I was trying to make sure whether this EIP would work for the people doing state channels
        * It's designed for them
        * Didn't get any reply from them
        * Counterfactual: they asked for this
        * Wanted to make sure they're happy with it
        * I don't see a big difference
        * Agree that prepending 0xff is a good idea (option two in EIP)
        * Hashing of init code: agree it could be okay
        * Seems like Parity already has code to implement another EIP, so there's a conundrum about writing new code or throwing away their code
    * Martin: I suggest we prepend 0xff
        * To do calculation on chain, it's a big hassle to do RLP encoding on chain
        * Propose we accept #2
    * Wei: What's the problem if we continue to use RLP encoding?
        * Martin: If you do it on chain you need to take the nonce into account
        * If it's larger than 0x80 then you need to RLP store it differently
    * Alexey: Important to be able to do it on chain because main goal of this CREATE2 is counterfactual instantiation; in most cases when state channels are created then CREATE2 will never actually go on chain
        * But in case of arbitration they have to be able to compute addresses of contracts on chain
    * Hudson: Sergio's option 2 seems easier
    * Martin: I agree
    * Hudson: Seems like people don't care how it's implemented as long as it's done
    * Alexey: I'd still like to hear the opinion of the potential users, maybe for them it does matter
        * The idea is to make counterfactual instantiation more efficient
        * So we want to make sure that this makes it more efficient
    * Lane to reach out to Spankchain and L4 teams on these to see if they're happy with the EIP or if not, to join call to discuss, see if they have an opinion on this
    * Parity issue
        * EIP-86 and Skinny CREATE2 - can these be made compatible?
        * Martin: I'd ignore EIP-86 (account abstraction) for now, even if it does come back it will need to come back in a completely different, revised form, can we not mix this in for now?
        * Skinny CREATE2 was pulled out of 86 since it was too complex
    * Fred: Does it make sense to close 86 or indicate that this won't be implemented and then we can extract parts like Skinny CREATE2?
        * Hudson: We don't have a process for rejection or withdrawn yet
* EIP-1218 Simple blockhash refactoring (successor to EIP-210)
    * Hudson: we keep going back and forth on this
    * We were looking last time for someone to champion this
    * Alexey: main reason for this one is light client support
        * So we need to ask the people who implement light clients
        * Fred: Parity has 4-5 ppl working on this
        * Fred to get feedback from them on this one
        * Hudson: we'll reach out to Zsolt
        * Nimbus team to take a look
    * Hudson: chances of this getting into Constantinople rapidly decreasing
        * Don't want to make changes too last minute
        * But still good to get opinions
        * Dimitry said we should include it, so let's not kill it if there's a major reason to put it in
        * But as of now we haven't heard enough people speak up and support it
* EIP-1087: Storage cost refactoring 
    * No one fully implemented yet
    * Geth having no problems
    * EthereumJ also no problems
    * Wei: Parity having issues, they've written EIP-1283 as an alternative
        * EIP658 optimization conflicts with some requirements of EIP-1087
        * We can't get dirty map efficiently
        * Either needs to cost more memory or we need to do a full diff of the state trie which is expensive and makes the tx that executes later on the block slower
        * So it's a performance issue for us
        * We had different opinions on how big of an issue this is but it's definitely a concern
        * In future if other clients implement this optimization this may also become an issue for them
        * So we drafted EIP-1283, two versions provided there
        * It treats the tuple of storage (orig value, current val, new value) as a state machine and you don't need any dirty maps or anything, just use it as a state machine and issue gas use or refund
        * In this case (version two of 1283), Alexey found that it covers all use cases for EIP-1087
        * So we think it may be a good replacement but it needs more reviews
        * If your client has no issue implementing 1087 then you will also have no problem implementing 1283 v2
    * Alexey: I examined the two EIPs
        * I believe they might actually be equivalent in terms of final gas consumption
        * Only difference is that gas usage at any given point might be slightly different
        * 1283 might sometimes require you to post more gas upfront than 1087
        * If we formally prove they're equivalent then the issue is much more trivial since it's not about which is better
        * If this is true then we should do 1283 since it has less performance impact
    * Nick counterargued this point in AllCoreDevs channel
    * Martin: 1283 seems to be the better of the two, let's see if we can implement it in geth
    * Alexey: I will coordinate with Wei and see if we can find a way to prove it
    * Mikhail
        * Both EIPs look straightforward as far as EthereumJ implementation is concerned
        * But I prefer 1283: it's more elegant technically
        * We should ask Nick if 1283 addresses the same issue that he has addressed in 1087
        * If so, I'm for 1283
* EIP-1109 Remove call cost for precompiled contracts
    * Jordi overview
        * Very easy EIP
        * Remove gas cost of calls to precompiled contracts
        * SHA256 costs only 60 (16?) gas but calling it costs several hundred, this makes no sense
        * When you're calling a precompile you don't actually have to "load" anything as it's already in the client code
        * Proposal is to remove 700 gas cost for these calls
    * Martin: Removing it completely is a bit too much, we should be more careful
    * Matt: Alternative approach: leave precompile semantics the same but add a 'CALL PRECOMPILE' opcode
        * Could be easier depending on implementation
    * Jordi: Okay for me to have a different opcode
        * All precompiles already have a cost
        * We can set a minimum but it should be added to the gas cost of the specific precompile
    * Matt: Put precompile address on stack, if it's there it uses existing precompile gas calc mechanism, if too large it halts, otherwise if contract not there there's zero gas cost and executes as a NOP
    * Hudson: this would require a hard fork right?
    * Matt: Would require adding an EVM opcode, doing this is slightly easier than modifying semantics of CALL to do that
    * Hudson: sounds like it would be hard on testing to put this into Constantinople
        * Pawel: Breaks EVM abstraction
            * Currently EVM doesn't need to know which contracts are precompiles
            * I like idea of adding a new opcode, sounds better
            * Alternative: allow precompiles to refund some of the gas, refund counter is mostly handled per tx so it's on the boundary between EVM and the client, EVM is not strictly responsible
            * From implementation perspective it might be easier to add some gas, get it back at end of tx
        * Martin: As EIP is written it doesn't care what's a precompile, valid for calling anything < 256
        * Jordi: precompiles already have a different cost
            * On adding then removing gas: there are some intensive ops such as checking a long Merkle proof on chain, intensive SHA256 call, so for this you would have to add a lot of upfront gas, so I'm not sure if this is a good idea
            * Same as e.g. SHA3, only 13 (30?) gas
            * SHA256: 760 if you add it all together
            * I will update 1109 to add this opcode
# Fellowship of Ethereum Magicians update
* Greg on vision of the group
    * I'm happy it's moved on without me, that we have a forum now, people are organizing, enjoying having a forum, ability to meet in person, slightly more structured forum
    * People seem to be working out the ideas
* Jamie on basic mission and principles
    * We want to nurture community consensus and technical direction of Ethereum
    * We do that through producing high quality EIPs, especially ERCs
    * We want to facilitate this work, allow working groups ("rings") to form
    * Principles: open process, how to make decisions on things ("rough consensus and running code")
    * Focus on in-person meetings, that's why we had the councils of Paris and Berlin
    * We have our [wiki](https://github.com/ethereum-magicians/scrolls/wiki), and the forum (ethereum-magicians.org)
        * Forum is threaded, contains discussion on EIPs and other issues in the community
        * It's a better place to discuss things than Github issues have been, since it's a multi-threaded forum
* Boris on our most recent meeting in Berlin
    * I met a lot of you at the #WalletConf UXUnConf in Toronto and volunteered to help organize this in Berlin
    * It went well, we had about 70 people over two days at C-Base
    * Lots of things hashed out, esp.: people have a desire to contribute more
    * Lots of non-technical people showed up
    * Lots of people want to get involved and help out
    * FEM is a forum and a domain
    * As Greg has indicated: everyone is welcome, no one is in charge, people just do work
    * Rainbow gatherings / Rainbow family: largest gathering of "non members" in the world - we are "non members"
    * We stick to the principles of decentralization
    * We have a [GitHub repo](https://github.com/ethereum-magicians/scrolls), a [wiki](https://github.com/ethereum-magicians/scrolls/wiki) that was formed in Berlin, some "rings"
    * Can potentially scale technical improvements by having people interested in certain areas to come together, come to consensus; we have a set of experts who have hashed through these things already
    * We're doing this again in Prague
        * Will actually do work and progress on EIPs
    * Hope we can help scale Ethereum technical governance
* Hudson: Was there consensus in Berlin about all core devs call / how it interacts with the rest of the ecosystem / how we can make it better?
    * Boris: Questions such as who owns the roadmap? How is it decided? How do core devs make decisions? How do EIPs get decided? EIPs vs. ERCs
        * It would be helpful if this was written down somewhere - there were more questions than answers, and an offer to help figure some of this stuff out
        * E.g. "rejected" in EIP process
    * Jamie: There was a session on "Core EIPs vs. implementation"
        * Discussion about how working groups would come to consensus and how that would be recognized by core devs / client teams
        * The work performed in these rings, if there's e.g. a ring focused on a particular EIP - will their decisions be recognized and implemented? Recognized as "authoritative"?
        * The consensus they reach _is_ the community consensus so long as the process is open
        * Wallet implementers involved, the process is open
        * Their flow might be very similar to the EIP editors process for reaching final on an EIP
        * Big component is educating people on these processes, facilitating these rings so they can start to govern their domains
* Lane: How do the core devs contribute or get involved?
    * Jamie: Core devs is like a ring -- the first ring before Magicians or anyone else existed
    * Core devs describing its process through articles or documentation would be very helpful so community can see what core devs is, how it works
    * EIP editors have done better with this with e.g. EIP1
    * Showing up to the open process, help everyone see why it's working and spreading that to the other rings
    * Greg: Decentralization is crucial, SEC decision recently was largely based on this fact
        * Core devs simply participate in the rings as developers, for EIPs that are relevant for them
        * By the time things reach the core devs, a lot of stuff has been hashed out
        * Core devs won't have to face controversial issues as often
        * EIP editors got some very controversial proposals, so we had to clean up our process so we could handle those, and to some extent the magicians took on handling that sort of controversy
        * Tried to draw lines saying we're only handling technical controversy

# Attendees
* Alexey Akhunov (TurboGeth)
* Tope Alabi
* Jordi Baylina (Giveth/Dappnode/WHG)
* Paweł Bylica (EF/aleth/Ewasm)
* Greg Colvin (Fellowship of Ethereum Magicians)
* Daniel Ellison (ConsenSys/LLL)
* Matt Halpern (Pantheon/PegaSys)
* Fredrik Harryson (Parity)
* Hudson Jameson (EF)
* Mikhail Kalanin (EthereumJ)
* Boris Mann (Fellowship of Ethereum Magicians)
* Jamie Pitts (EF/Fellowship of Ethereum Magicians)
* Lane Rettig (Ewasm)
* Jacek Sieka (Status/Nimbus)
* Tim Siwula
* Martin Holst Swende (EF/geth/security)
* Wei Tang (Parity)
