# Ethereum Core Devs Meeting 43 Notes
### Meeting Date/Time: Fri, July 27, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/51)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=6I7SRa58-9M)

NOTE: The order of these notes is different than the order in the Youtube recording since we skipped around a lot on the call to accommodate people's schedules.

# Agenda

* Testing
* Client Updates
* Research Updates
* Four competing EIPs to delay the difficulty bomb and/or reduce the block reward:
    a. EIP-858 - Reduce block reward to 1 ETH per block.
    b. EIP-1227 - Delay bomb and change rewards to 5 ETH.
    c. EIP-1234 - Delay bomb and change rewards to 2 ETH.
    d. EIP-1240 - Remove the difficulty bomb entirely.
* Constantinople hard fork timing and what to include (continuing conversation from last call).
    a. EIP 145: Bitwise shifting instructions in EVM: pretty well-formed, but not 100% implemented or tested.
    b. EIP 210: Blockhash refactoring.
    d. EIP 1052: EXTCODEHASH Opcode.
    e. EIP 1087: Net gas metering for SSTORE operations.
    f. EIP 1014: Skinny CREATE2.
* Potentially lowering the cost of pre-compiles (bnAdd?, bnMul?)
* Fellowship of Ethereum Magicians Update

Call starts at [[5:37](https://youtu.be/6I7SRa58-9M?t=5m37s)]

# Testing
* Dimitry update
    * not enough to write tests for new opcodes manually
    * last year Casey discovered a lot of new bugs than could be found manually
    * CREATE2 opcode is about to be added to cpp-ethereum, I will start writing some tests
    * EXTCODEHASH seems to be pretty easy to implement
    * Hudson: we're considering 1087 net gas metering for SSTORE
        * Nick: a bit more substantial than just changing the gas price
        * if you write e.g. five times to the same slot, you only get charged for a single storage write
    * Suggest we implement blockchain test without PoW
        * Just disable PoW
* Martin
    * We start fuzz testing again soon
    * To make sure we get new opcodes
    * Requires differential testing, implemented in at least two clients, e.g., geth and parity
    * Intend to get started soon after clients merge PRs
* Mikhail
    * Guido started to fuzz ethereumj

# Client updates
* Parity (Afri)
    * Released parity ethereum 2.0, finally concludes what we've been working on for a while, to have a pure blockchain client for EVM and Wasm
    * Stripped out UI, wallet, etc.
    * Slightly rebranded to "Parity ethereum" (to distinguish from other software we're building)
    * Constantinople hard fork implementation update: Implemented bitwise shifting, 1052 EXTCODEHASH
* geth (Peter)
    * Constantinople hard fork implementation update
        * bitwise shift merged for a few months already
        * EXTCODEHASH, skinny CREATE2 - both implemented and merged
        * storage metering PR (net sstore) - implemented but not merged yet, will wait to merge until we're sure it's in
        * testing pending
        * blockhash EIP (210) - would be good to know whether we go with original blockhash EIP or simplified version that V suggested
            * introduces a new type of account, superuser stuff, mucks with gas allowances, etc.
            * not especially hard but let's confirm which one before implementing
    * Ice age stuff
        * nothing to add, we'll go with whatever's decided
* Harmony (Mikhail)
    * Last two weeks worked mostly on sharding research
    * Will start working on Constantinople within two weeks
* Trinity (Piper)
    * Published second major release this week
    * Still waiting for client to finish, think we have a client that syncs with the mainnet now, need another ~ day
    * Performance, syncing reliability
    * Coming along nicely
    * Haven't started on Constantinople EIPs but we have issues open and will work on it soon
* cpp-ethereum (Pawel)
    * Constantinople hard fork implementation update
        * Bitwise shifting implemented
        * CREATE2 implemented
        * EXTCODEHASH in progress
            * In current spec, empty accounts distinguished from non-existing accounts since empty account has nonzero hash of empty string, non-existing account would output no hash for this opcode
            * Are core devs aware of this? Is it a good idea?
            * This is new information available to contracts, not previously exposed
            * Before they could only see different call cost, whether or not account existed
            * Now there's more direct access to this info if they want to check whether an account is empty or exists at all
            * But definition of existing account may not be very specific within Ethereum spec
            * Peter: We had some back and forth on existing/nonexisting accounts, precompiles, etc., if it doesn't exist we return zero, otherwise empty code hash
                * If the account exists but has no code, return empty code hash, also for precompiles
                * But if precompile does not exist, has balance, then we return zero
                * This is good behavior, otherwise it needs to be aware of whether or not something is a precompile
                * But this is an interesting corner case
                * We had weird corner case regarding 160 precompile, RIPEMD in the yellow paper -- did we delete this or not?
                * parity and geth implemented differently, and we ended up with parity's "bug" since it was easier to reproduce this
                * Pawel: in the end we followed an inconsistent rule
                * Peter: Did we or did we not delete this contract?
                * Pawel: I think we did, then recreated it by manually sending some balance there
                    * Cases for precompile listed in test cases in spec
* Matt: we can find out about specific tx at block 2.67M in the yellow paper
    * But is actual behavior specified in an EIP? Finalized?
    * For Constantinople can we get closure on this?
    * Clients could handle other edge cases differently
    * Martin: Yoichi and I spent a lot of time on finding common ground on how cpp, parity, and geth can handle this case the same
        * It's really a mess
        * There's an open ticket on this
        * It's a long discussion, let's take it offline
    * Hudson: There's a gist somewhere that has the whole story and explains why the yellow paper is written the way it is
* Pantheon (Matt)
    * Hudson: is Pantheon closed source?
    * Matt: yes, until Devcon release date
	* At point where we can connect to mainnet
	* Can perform full syncs
	* Not optimized but well past 4.8M, past attack segment
	* Still a few precompiles to do for Byzantium, not thinking about Constantinople yet
* Nethermind
    * https://github.com/tkstanczak/nethermind
	* Full dot not Ethereum client (unlike Nethereum which is an integration library https://nethereum.com/)
	* Will invite to meetings, have been unable to get a hold of them so far
	* Their Github activity seems to have dropped off for the past month
* Ewasm (Alex)
	* Testing of precompile implementations is ongoing
	* Discussing a couple of design issues in depth
* EthereumJS (Holger posted comment)
    * https://github.com/ethereum/pm/issues/51#issuecomment-408140132
	* We have now a first release series v2.4.x out where we introduced partial support for Constantinople (bitwise shifting instructions, EIP 145), see the according announcement post on Reddit.
	* Work on other EIPs hasn't started yet though. I will make a follow-up Reddit call for participation tomorrow, since we currently don't have the people power to implement all ourself.
	* If anyone is interested in helping head over to our VM repository. I'll also write up issues tomorrow on the Constantinople EIPs with some instructions on where to start.
	* Reddit followup call for participation, don't have enough people to implement it all

# Research updates
* Shasper v 2.1 (Danny)
    * Working spec getting close to complete
    * Combines crosslinks and attestations
    * Introduces new fork choice rule
    * Vitalik posted proposed epoch-less Casper on forum, pending more peer review
    * First sharding implementers call soon
    * Some security params (how much advantage an attacker can gain with dedicated hardware) - getting some real world info from HW manufacturer
* Vitalik
    * Epoch-less casper
        * Allows any epoch to be justified and finalized
        * Was 25% above optimal, takes TTF down to optimal
        * Don't need to worry about what happens in vs across epochs
    * Recursive proximity to justification (fancy name for fork choice rule)
        * Only needs one component now instead of two
        * Did a quick implementation of this, kind of in the category of GHOST algorithms
        * Manages to justify and finalize things even with high network latency
    * Next step: to formally prove some properties of this and epoch-less Casper
    * Separate line of research from Justin's VDF work - purpose to make algorithm resistant even against VDF failing horribly - against long sequences of bad proposers
        * Seems to get the job done but need some more work to get some formal verification of certain properties

# Constantinople hard fork timing and what to include (continuing conversation from last call)

* EIP 1087: Net gas metering for SSTORE operations.
    * Peter update on geth implementation
        * See PRs listed here: https://github.com/ethereum/pm/issues/51#issuecomment-407366399
        * Crux of the EIP: Instead of charging a lot, we only charge a small amount for each operation, and only charge a large amount if we end up modifying the state
        * Need to track original value, whether slot is "dirty" or "not dirty"
            * e.g. overriding slot with exact same value is not dirty
        * Relatively straightforward in geth since we already had dirty tracking done for optimization reasons - only update the trie if a value changes
        * Need rules for Constantinople where we don't charge based on zero/nonzero, more complex logic involving four IFs or a switch
        * When retrieving refund amount, we iterate over all dirty accounts/touched accounts and over their fee items, to determine how much to charge or recover due to overwriting with the same thing
        * Overall pretty straightforward in geth (but already had dirty tracking)
    * Martin: Are there weird edge cases such as a contract that calls SSTORE then suicides?
    * Nick: In this case and other edge cases I'm okay with leaving gas costs unchanged
    * Martin: I'm worried about quirky behaviors which can cause implementation difficulties, things we fail to foresee in our testing, and could lead to consensus issues
        * e.g. post-transaction you delete entire account from storage trie, but also have some dirty mappings which do or do not get deleted? clients can implement this differently.
        * I'm wondering what are the edge cases and how complex are they
    * Nick: all the new state is scoped to a call just like existing state tracking, so all of the effects should also be scoped to the call that it's in. There should not be edge cases around destroying stuff like that. At least no obvious association between selfdestruct and how you charge for sstore.
    * Peter: need to test:
        * suiciding contract - do storage slots refund gas or not? I would say no but either behavior is valid as long as it's specified
        * what happens with REVERT?
            * if I e.g. modify a storage slot, make it dirty, then call REVERT
            * does this revert the dirtiness?
            * optimal: should not, but might be better scoped if we do revert the dirtiness
        * can reevaluate after a second implementation
    * Parity (Fred): haven't looked at it in enough detail to have comments
    * Harmony: no comments on implementation, don't see any real problems
    * Hudson: can we ask Parity/Harmony to implement it by the next call to see how easy or hard this will be? yes (both agree)
        * Can't officially put on Constantinople roadmap but I think we should try
        * Peter: geth implementation is pretty clear, it may be useful to review it as a reference for your codebase (https://github.com/ethereum/go-ethereum/pull/17208)
    * Hudson: I'll try to track which implementations have finished which features for the meta EIP
    * Is anyone opposed to putting this into Constantinople, modulo any implementation issues?
        * (No objections)
        * Let's implement on Parity and Harmony to see if we're missing anything
    * Dimitry, any opinion from testing perspective?
        * Need to look at it more
        * Martin: Won't need many explicit tests since existing tests should cover most cases
        * Nick: I added a list of suggested test cases to the EIP
    * Peter: Regarding dirty tracking, in geth it's more like an optimization, track whether a storage slot was modified and if so at the end of the tx we update the storage trie, but we don't care about unmarking a dirty field after a revert
        * Must pay attention now to correctly tracking and reverting dirtiness -- if any clients already have optimizations for dirtiness tracking
        * If you have journalling in place it should be fairly straightforward to unjournal

* Blockhash refactoring (EIP210)
    * Martin
        * Vitalik made a simpler proposal last time
        * So we have an old and a new proposal
        * There were some concerns about EVM features around e.g. genesis
        * In both cases there were some discussions around how to use it
        * May be a bit difficult to make a smart contract rely on earlier block hashes
        * At a given point, you can't tell which blockhashes will be there
    * Peter
        * Before going ahead with this EIP it would be nice to have a reason for going ahead with it
        * Vitalik gave some uses cases where it might be useful
        * But I'm wondering if it's truly useful
        * Would be good to understand a bit better how it's useful (purpose, what it aims to solve) given the complexity
    * Vitalik
        * [poor audio]
        * If we're not going to have EVM calls at protocol level but instead Wasm
        * Then it probably makes sense to use native code which is what 1218 does (rather than 210)
    * Martin: What about the fact that we overwrite block hashes, at which point are we certain which numbers are still available?
        * In a real practical use case it might be difficult to use this information
    * Vitalik
        * Overwriting necessary or it would have O(N) overhead
        * If you want a use case that has larger range, you'd use a block number that has a larger number of zeroes than its binary representation so you have a larger span of time during which you can submit blockhash
        * Martin: You may have to wait a year from Constantinople
        * V: Yes
        * If you want certainty that you'll be able to use the same blockhash for a year, then you have to wait a year
        * Or have contract that calls that particular blockhash once and stores it separately
    * Martin: Would be nice to have example of benefits
    * V: I can add examples to the EIP
    * Hudson: Let's discuss more about 1218 at the next meeting, not going in for now until we have more info

# Potentially lowering the cost of pre-compiles (bnAdd?, bnMul?)
* See Martin's analysis: https://github.com/ethereum/benchmarking/blob/master/constantinople/analysis2.md
* Martin
    * Some suggestions about lowering cost of precompiles
    * I did some benchmarking, you can see the results
    * Right now, we could lower the cost of ECADD, ECMUL though not drastically
    * MODEX, PAIRING - cannot lower costs
        * Geth could but Parity would have some problems
        * Fred: Parity has looked into feasibility of improving this
            * Andrei's been working on it for a week
            * Have a PR that gives us a 2x speedup, not close to 10x that we'd need
            * Problem is geth relies on cloudflare library that has super specialized assembly for 64 bit arch. on BN128 and 256
            * Looking into whether we can use this or integrate it, but very involved
            * This implementation says it's for non-commercial use only, so we can't copy-paste it
            * Needs low-level expertise that we don't have right now to get 10x speedup (pairing is the hard bit)
            * If someone could port the cloudflare lib to rust we'd be good but it's harder than it sounds
    * So we could halve costs if parity is able to impove this, cannot do anything with pairing at all
* Piper
    * Our implementation (Python, trinity) are extremely slow
    * Done in pure python
    * There were no other options that I could find
    * Don't know what other language ecosystems look like
    * I'm wary of dropping these gas costs, thus introducing DDoS vectors for new clients coming online
* Martin: I'm not championing this, I just did a feasibility study
* Hudson: No champion right now
* V: I did write an EIP for reducing gas costs, small and simple
* EIP1187, 1108 (see this update: https://github.com/ethereum/pm/issues/51#issuecomment-408383462)
    * https://github.com/ethereum/EIPs/issues/1187
    * https://github.com/ethereum/EIPs/issues/1108
        * Merged as a draft
        * "Reduce ALTBN128 gas cost"
    * Hudson: it looks like there are champions for this but they're not as loud
    * Martin: We cannot reduce the cost of pairing
* Nick
    * [bad audio]
* Martin
    * Would affect ADD and MUL but pairing is 900k at least
* Fred: If we get 10x improvement for pairings what's the possibility?
* Martin: for geth, what today costs 900k gas, could cut down by a factor of 4 safely to 220-250k
* Fred: it's theoretically possible to do that but we'd need to get the right person
* Do we want to depend on these hyperoptimized assembly implementations for all pairings in future?
* Piper: it's slow in Python, already close to a DDoS factor for us, so dropping gas costs here would impact us a lot
* Matt: Similar for Pantheon, we're not sure how it would impact us
* Pawel: Will happen again for other cryptography
    * All clients use same implementation for segp256k1 (code from Bitcoin)
        * Maybe we should try this approach
        * Coordinated effort to have a single, well-performing implementation available to new clients, new teams
    * Matt: but from security perspective you have language bindings (interfaces) which may not be as secure, may be attack vectors
    * Pawel: But we're using that already
        * I don't think it's better having different implementations of the same cryptography
* Martin: would an implementation of just ECADD/ECMUL help?
    * V: maybe:
        * Halving for ECMUL would make ring signatures more viable.
        * Halving for ECADD would make BLS aggregate signatures more viable.
* Mikhail: For java we can try to create a JINI for this Cloudflare library but it would take a while
* Fred: It has a tight integration with Go and its bigint library, so breaking out the assembly parts not as easy as copy and paste
* Mikhail: We can just compile it right?
* Pawel: Go has its own runtime that you'd have to include
* Fred: Also, this library cannot be used for commercial purposes, so we couldn't use it directly
* Pawel: A solution (C/C++/Rust) without GC would be better than Java
* Matt: We've been using Bouncy Castle in Pantheon codebase
* Mikhail: For pairing etc. we use our own implementation ported from libsnark, so not super efficient
* Matt: We want to encourage a variety of clients, so introducing gas costs that bias for particular implementations could be a problem
* Hudson: Champion is Vitalik, who doesn't feel strongly about this, so for now we'll leave it out

# Delay/remove difficulty bomb / reduce block reward
* Four EIPs to delay or remove difficulty bomb/reduce block reward
    a. EIP-858 - Reduce block reward to 1 ETH per block.
    b. EIP-1227 - Delay bomb and change rewards to 5 ETH.
    c. EIP-1234 - Delay bomb and change rewards to 2 ETH.
    d. EIP-1240 - Remove the difficulty bomb entirely.
* Does anyone want to remove difficulty bomb completely?
    * Proposal put forward by Micah Zoltu for philosophical reasons
    * Dimitry: I don't think it was a good idea in the first place
    * Initially implemented for switch to PoS
    * We're not there yet, we keep moving it, requires additional tests about difficulty being calculated in a weird way, this is not good
    * Hudson: What's the purpose of the difficulty bomb _today_ (vs. when first implemented)
        * Is it about forcing miners to participate in hard forks?
        * Piper: Makes inaction infeasible
        * Nick: Corollary is that it lessens the default effect of inaction being the most attractive option
        * Piper: Not applicable to miners or anyone specific, everyone must do something to keep the network up and running every so often, which is a good thing
        * Lane: Is it just general? Do we want to keep this forever?
        * V: After Shasper it would probably make sense to have it exist on much longer timescales
            * Rate of change will be much slower
            * Not sure if I have a strong opinion about whether it should be kept forever
    * Hudson: We have consensus we don't want to remove it entirely
        * But we need to delay it or else block times will get very high starting in 2019
        * EIPs do a combination of delaying the bomb and reducing the block reward
        * I think we should decouple them: one is economic/technical, the other is pure technical
    * Hudson: re: reducing reward, proposals to reduce to 1 ETH, 2 ETH, 5 ETH (it's 3 right now)
        * What are the reasons to change the reward?
        * V: The chain is overpaying for security.
    * Lane
        * If we delay bomb without reducing issuance, it increases overall ETH issuance
        * So it begs the question, what is the "intended" issuance schedule?
    * Danny: original intent of bomb was to move to PoS, which would ultimately reduce issuance
        * This is a good argument in favor of reducing issuance
        * EIP1011: I put out an analysis of Ethereum mining reward relative to other blockchains e.g. Bitcoin, Bitcoin cash -- suggests we are overpaying and would still be extremely competitive PoW blockchain even with reduction
        * With assumption we gain security from PoS overlay
        * So they need to be talked about at the same time
        * If there are a lot of ASICs and you decrease block reward, it might increase proportion of ASIC mining
        * https://gist.github.com/djrtwo/bc864c0d0a275170183803814b207b9a
    * Lane: Since these issues are in fact both economic, maybe the two should not be decoupled
    * Afri
        * Attempted proposal based on 649 which we used for Byzantium fork, same mechanics
        * delay by 3M blocks, reduce block reward by ~35%
        * Strong preference to not separate the two as Lane said
        * In case we decide only to do one of these two things, it means we significantly change Ethereum issuance/inflation model
        * I'm not super convinced that the numbers in this proposal are perfect but it's a start for discussion
    * Alex
        * As Piper mentioned the bomb forces us to do something every so often
        * In Afri proposal, timelines shifted out to mid-2020
        * If any change is made should it only give us 12 extra months? I.e. forcing a hard fork every 12 months
    * Hudson: We usually just pick a time for a hard fork, there wasn't so much discussion over it before, we should discuss the timeline further
    * Piper: There was a discussion at Devcon last year, we discussed 9-18 mos. (9 too short, 18 sometimes too long), so one year is something I'd support
    * Danny: We're currently discussing a fork roughly one year from the previous one
    * Afri: These are two separate topics, we don't want to be forced to delay the bomb with every hard fork, so maybe it should be ~ 18 mos out to give us some buffer
    * Piper: So we could e.g. do a fork every year and always push the difficulty bomb out 18 months
    * Hudson: Everyone please review and comment on the various EIPs discussed here

# Fellowship of Ethereum Magicians Update
* Let's have Jamie, Greg, or someone discuss Fellowship of Ethereum Magicians and what came out of the Berlin gathering on the next call
* Lane: We're planning another FEM gathering in Prague post-Web3 summit, pre-Devcon, and would love if core devs could join

# Attendees
* Guillaume Ballet (EF)
* Alex Beregszaszi (EF/Ewasm)
* Vitalik Buterin (EF/Research)
* Pawel Bylica (EF/cpp-ethereum)
* Daniel Ellison (Consensys/LLL)
* Matt Halpern (Pantheon/PegaSys)
* Fredrik Harrysson (Parity)
* Hudson Jameson (EF)
* Nick Johnson (EF/ENS)
* Mikhail Kalinin (Harmony/EthereumJ)
* Piper Merriam (EF/Trinity)
* Lane Rettig (Ewasm)
* Danny Ryan (EF/Research)
* Afri Schoeden (Parity)
* Martin Holst Swende (EF/geth/security)
* Peter Szilagyi (EF/geth)
* Eric Tang (Livepeer streaming)
