# Ethereum Core Devs Meeting 38 Notes
### Meeting Date/Time: Fri, May 18, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/38)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=1WBuF8cMKUk)

# Agenda

1. Testing
1. Client Updates
1. Research Updates
1. EIP 908: Reward full nodes and clients for a sustainable network - When each transaction is validated, give a reward to clients for developing the client and provide a reward to full nodes for validating the transaction (Ethereum Magicians thread).
1. EIP 1057: ProgPOW, a programmatic Proof-of-Work - an alternate proof-of-work algorithm - “ProgPoW” - tuned for commodity hardware in order to close the efficiency gap available to specialized ASICs. Technical details.
1. EIP 210: Blockhash refactoring - @holiman wants to finalize a few points:
    a. the original intent (no semantic changes to BLOCKHASH -- only gas changes) versus the current spec (semantic changes), and
    b. whether to make it nicer to ABI-call it, and
    c. whether to add genesis lookup in there.
1. EIP 1051: Overflow checking for the EVM
1. EIP 1052: EXTCODEHASH Opcode
1. EIP 1087: Net gas metering for SSTORE operations
1. Concerns that using native browser VMs for running eWasm is not DoS hardened. See this comment.
1. Constantinople hard fork timing and what to include (continuing conversation from last call).
1. Core dev meeting discussion & changes - scope of agenda items, role of participants, etc.

# Notes

Video starts at [[]()].

## Testing
* Dimitry: common `genesis.json` format
    * Each client currently has its own format, we should come to some agreement
    * Martin: I agree. Currently the structure and semantic meaning differs. Some clients have fork block nums, Parity has divided by features rather than forks.
    * Fred: When you change the spec file how do you migrate from one to the other? We need a discussion about migration framework. What happens if there's breaking changes?
    * M: Let's put together a group to work on this. I notice immediately when something changes since e.g. Hive goes down. Would like buy-in from Parity and Geth.
    * D: This is why I introduced a field called version in the proposal. We can agree on a schema.
    * Hudson: Let's make a Gitter channel and bring the stakeholders together. Folks should comment on the issue.

## Client updates
* Decided to move these to the beginning of the meeting so we don't have to rush through them.
* Parity (Fred)
    * 111.1 Release
        * C-live for whisper
        * Complete refactoring of tx queue
            * Verification happening in parallel
            * Now much more performant for inserting
            * we split out the tx pool to have scoring and readiness which makes it easier for miners to view the pool and do more with it
* Geth (Peter)
    * Working on peformance improvements
    * Txs on mainnet including spam tx went up, tracking down issues, esp. around memory usage
    * Want to work on resource accounting which will help with decentralizing full nodes
    * Separate light client resource counting and monetary layer so anyone can monetize their node however they like, geth will just count it and make sure you adhere to your own quotas
    * Don't have numbers yet but hope that by next call I can give you guys some hard numbers on whether the new fast-sync protocol seems worth it or not, i.e. let's POC before we EIP (per @holiman's clarification)
* cpp-ethereum (Pawel)
    * Sent binaries to Github releases, now have a development snapshot and we'll make a stable release soon
    * Some RPC improvements and fixes
    * All the tools accept dynamic loaded EVM-C interpretations
    * Can load e.g. ewasm backend as a shared library
* Harmony (Dmitrii)
    * Finished everything we wanted, have a release candidate now
    * Mainly a performance release, improved performance 5-10x
    * Was previously hard for us to keep up with the head of the chain, still behind geth but a big improvement for us
    * Plan another release in 1-2 weeks
* PegaSys: no one present
* Trinity (Piper)
    * In roughly the same place as Harmony
    * Been working on low-level performance issues for couple of weeks
    * Have a viable alpha right around the corner
    * Mainnet, full and fast sync functional, also functional light client
    * Working on getting RPC endpoints working against those
    * Knocking off a short checklist towards a public alpha
* Ex-thereum (Geoff)
    * New elixir client
    * Started about six months ago
    * Focus has been to diversify the community
    * Also having elixir libraries would be helpful for people
    * Work on getting to a v1 client
    * PoA has a fork called Mana which is to have a full-synced first-class client
* Nimbus: no one present

## Research updates

* Research (Danny)
    * Casper: working on EIP spec
        * Live, changelog in discussions issue
        * Some concerns about parallelization of vote transactions
        * We might put all vote tx in a separate transaction that's guaranteed not to be modified aside from those votes
        * Working on decentralized pool concepts
        * This made it onto the grant wishlist, if anyone out there is interested in getting involved
* Drops of Diamond (James)
    * Working on blob serialization
    * Developing P2P network with libp2p
* ewasm (Casey)
    * Focus on `evm2wasm` which transpiles evm bytecode to WASM bytecode
    * Would allow a client that only has a WASM VM to run on the mainnet and execute EVM contracts
    * Main reason we've been working on it is to get greater test coverage over the tests via EEI
    * This allows us to translate all of the multi-client tests and check a lot of edge cases
    * So we're discovering and fixing bugs in Hera and `evm2wasm`

## EIP 908: Reward full nodes and clients for a sustainable network
* [EIP link](https://eips.ethereum.org/EIPS/eip-908)
* [Ethereum Magicians Thread](https://ethereum-magicians.org/t/eip-908-reward-full-nodes-and-clients-for-a-sustainable-network/)
* James update
    * The EIP is pretty long but the spec is pretty short
    * Add an arbitrary byte array to each block which is previous block verifications
    * Can add a blockhash of previous block verifications with the address of the client that verified the transaction
    * In order to make sure that the client is legit, they could be included in an access list and you can check that the address provided is in that access list
    * There are some complications around managing this list, it can be done but it's not ideal
    * The proposal initially included rewards for _running_ a full node but this is less of a concern with Casper
    * There still won't be any incentivizes for relaying and bandwidth, storing state, etc. so we still need proposals around this
    * More details in EIP
* Peter: If you're including metadata in blocks that isn't part of consensus
    * If a block has metadata that Parity verified
    * But I release a version of geth that strips these out before forwarding to the network, what happens?
* J: The spec for validity would be specified in the yellow paper
* P: But there's no incentive for other clients to forward these blocks without stripping out this data
* Piper: If I'm a Trinity node, and I'm the first person that a newly-mined block from a geth node is broadcast to, can I strip out their metadata and forward it on and would it still be a valid block?
* Peter: Relies on miners' goodwill.
* J: Not sure
* Martin: The EIP is thin on technical details, mostly discussion. Need more info on what is hashed and who does what.
* Peter: Running a full node without light clients, you're wasting your bandwidth.
    * It's hard to solve this problem because it's hard to fake that you verified a block or indeed uploaded 1gb of traffic but maybe swarm is the direction we want to take this.
    * If the point of swarm is to share data and run a tit-for-tat protocol, it might be a nice approach to solve this problem altogether - without needing to reinvent swarm on top of the ethereum protocol.
* Hudson: Let's continue conversation on the Fellowship forum.

## EIP 1057: ProgPOW, a programmatic Proof-of-Work
* [EIP link](https://eips.ethereum.org/EIPS/eip-1057)
* [Technical details](https://github.com/ifdefelse/ProgPOW)
* If, Def, Else (three people) have joined us on the call
* Goal of this topic is not to make a final decision but to consider replacing the current PoW scheme or to have a backup scheme
* If: New PoW algorithm designed to close the efficiency gap available to specialized ASICs
    * In current algo, ASIC can get 2x speedup
    * This is because large portion of GPU hardware is not used
    * So what this algo does it utilize more of the GPU card, engages more of the core
    * In doing so, specialized hardware is not able to have such a large efficiency speedup
    * We've gone to great lengths to ensure that implementation is as easy as possible
    * Miner implementation is on our Github and ready for review
    * Goal is to ensure that we have an implementation for all clients so that the core devs do not have to do any implementation, just testing
* Else (hardware engineer)
    * Current ethhash isn't so much a proof of work as a proof of DRAM bandwidth
    * Only requires a large amount of DRAM to store the DAG and high bandwidth access to the DAG
    * So an ASIC can be made by removing majority of ASIC and only leaving frame buffer interface
    * Algo we developed takes Ethhash as the base but adds using the register file high throughput math and caches
    * So any ASIC that implements these also needs to implement those, and once you've done that you've basically implemented a full GPU
* If: what barriers do you see for prog PoW?
    * Major arguments
        * Not seeing enough adoption by both stakeholders and developers
            * I believe this is an educational issue, we need to educate the public more on why this is so important for the gentle transition of Casper FFG into the hybrid model
        * It would add too much work for the developers
            * We address this by making sure the implementation is already done
* Peter: Ethhash on cpp-ethereum is a little-endian implementation and we had to reimplement the whole thing in Go to run on big-endian systems like MIPS
    * This is something you need to take care of
    * Also, how will your algo scale to mobile use?
        * Currently you generate 1-2gb DAG
        * Verification requires only 40mb cache
        * It's insanely expensive already on mobile, takes a phone a few minutes to generate it
        * If you introduce a new PoW algo that adds CPU overhead, how does it impact verification performance especially on low power devices?
* If: We're working on the geth implementation next
    * We're making sure the developers don't need to do too much work
* Else: On verification, calculating which DAG entries need to be used is expensive
    * We're adding only around 30 instructions per loop, this is tiny compared to work you already need to do
    * We can do tuning to make sure that verification times will be approx. the same
* Pawel: I started fixing endianness on cpp implementation
    * Also I wanted to optimize backend loading
    * Turned into a separate project, has endianness correct
* Peter: Generating cache is really fast but takes ~3 mins on a mobile phone
* Pawel: I'll work on mobile benchmarking
* Alex: I like the PoW approach but its validity is outside my area of expertise
    * I believe that the light client DAG generation is actually somewhat redundant
    * Property of this protocol is maxing out the DRAM on the CPU
    * Fewer cycles are required for the light client DAG and the effect is the same
    * Protocol can be tuned so that light client has ~128 less cycles
    * I encourage looking into this since reducing it might compensate for the addition of the math operations
* Else: The basic structure is the same as for Ethereum
    * There's an array of register file elements that are calculated
    * One acts exactly like the existing ethhash implementation
    * Loads a random value from the DAG, updates it, then goes onto the next one
    * But there is a bunch more happening in parallel
    * So even if you have a security weakness, the main one will give you the same security guarantees as today's ethhash
* Alex: On the redundant DAG generation cycles, everything was ready to go and we'd already launched Olympic and were ready to launch the mainnet
    * So no one wanted to refactor that
    * I'd be curious if you post on Github somewhere if that small bit of redundancy was optimized
    * It's a useful protocol for general use cases
* Else: We'll look into how the light client protocol is done
* Casey: We have efficient ways to verify ethhash block headers, this enables e.g. cross-chain tx, relays, bridges etc.
    * In contrast to dogecoin, lightcoin etc. SSCRYPT there's no way to do this efficiently
    * If another algo were adopted on mainnet it would break all existing apps that do such relays
    * So I'd suggest a solidity implementation of verifying headers from this algo
* If: We were not aware that PoW would break the relay contracts
    * We can work on a solidity implementation to fix this
* Hudson: Look up Loi Luu's peace relay as a PoC example of an ethereum-to-ethereum relay
    * Doge relay is another example
* If: We're pushing this and we're motivated for this since while we still have PoW in Casper FFG there are certain attacks that ASICs can do which can all be mitigated by PoW
    * Later today we'll have a more complete, detailed explanation of this attack vector
    * We want to ensure that PoS has its best chance of adoption by giving this transition period a fighting chance
* Def: The attack is a general PoW weakness that relates to what happens when the block rewards are reduced and you reduce the security of PoW
    * Not specific to ASICs, anyone who knows more hash rate could perform the same attack
* Danny: That attack ends up being a lot more limited by the finality
    * Personally I think if there's an easy switch to make things more ASIC resistant, I'm in favor of it
* Else: we look forward to Casper being adopted ASAP, we need to be careful what happens when PoW rewards are reduced
    * In terms of attack, censoring means you can hold the network hostage with 51% and don't allow any tx through except the attacker's blocks

## EIP 1051: Overflow checking for the EVM
* [EIP link](https://eips.ethereum.org/EIPS/eip-1051)
* Nick Johnson: This is fairly straightforward in principle and it's been raised before
    * Some discussion on Magicians forum about whether this should be flag-and-trap or a flag that's cleared
    * Added to agenda to get the gist of what client implementers think of overflow checking in general
    * I think the vast majority of client applications want this protection
    * But most people are working with the assumptions that they need to code around these with additional implementation cost
    * So let's add a backwards-compatible way that lowers cost to clients and makes it easier to have this protection
* Fred: Personally I think this is a good change and something that helps protect developers
* Does this negate the need for safe math? Nick: Assuming solidity added support for this, then yes.
    * To be clear, solidity could implement this protection now but it would be doing the same thing safe math does and there would be a performance hit.
* Danny: Vyper has this now, would move to native implementation if that existed.
* Piper: For solidity or Vyper to take advantage of this it would add some complexity
* Nick: Depends how your implementation is doing 256 bit math at the moment
    * Some could detect it trivially
    * Others would have to do extra work
* Piper: In order to do a check on an operation, the previous check has to have happened to make sure the flag has been reset
* Nick: Yes, each arith op you'd have to register with the flags for that op
* P: Could we get rid of that overhead by changing add, subtract, multiply opcodes to reset the flag on entrance?
* N: If you use a trap mechanism then you just jump to trap address on overflow, but with flag mechanism, wouldn't be more efficient to reset flag on entrance and would defeat purpose of having a flag since you should be able to do a block of operations and check
* Pawel: Quite easy for unsigned, not sure about signed overflow, how would you distinguish in EVM where it's not so obvious which operation is meant to be for signed vs. unsigned addition.
* N: EVM signed ops set signed overflow flag, and implementation chooses whether they care about that flag or not.
* Pawel: Does it mean you have two flags for signed and unsigned overflow? (Yes.) If you do regular arbitrary precision implementation you mostly do it using unsigned numbers then try to incorporate sign later on, so I'm not sure it's so easy to get signed overflow information this way. Maybe there's a way to transfor the result afterwards.
* N: If your number is represented in twos complement then there are simple rules for checking sign bit to see whether overflow occurred.
* James: ewasm has built-in metering, does that negate the need for these kinds of changes?
* N: I wouldn't add instructions to ewasm specifically, if it already has them we can use them.
* J: I'm speaking more generally about gas cost changes, if we have ewasm that can do gas metering.
* N: Thoughts on implementing this in Geth?
* Peter: I'd have to investigate that. There are some slight challenges with e.g. exponentiation, based on some special algo that assumes you can randomly cut off anything above 2^256.
* Greg: It seems a significant amount of extra work, extra code added to every arithmetic operation.
* Alex: Also doubles or triples the cost relative to the others.
* N: Arbitrary precision library you're using has no overflow flag? How big are the individual words?
* G: As big as you want, so I can use a 512-bit word to overflow into and then check whether it got too big.
* N: Most bignum libraries are smaller than that.
* G: This is multiplication - for addition you only need a little bit more.
* N: How are you currently multiplying the 256 bit output?
* G: I'd have to look inside but I think the library just masks off the overflow.
* N: So library masks it off but no way of getting at it without modifying it?
* G: So isn't it already doing that multiplication work?
* H: We need to test cost in each client.
* G: We have a lot of different clients using a lot of different libraries. Via testing.
* James: Let's find out if ewasm with metering would help.
* N: Where does metering come into it? This change is irrelevant to ewasm since we'd be using their opcodes not ours.
* J: You can use metering to meter how much computation is done so you don't need to play around with EVM gas costs so much for optimization.
* Piper: Can't multiplication overflow checking just be done with division rather than dealing with higher order numbers?
* N: Big number division is also very expensive.
* P: Either way this seems positive, and while we might be concerned about the overhead it adds to some common opcodes, it seems like it might be worth adding, esp. since languages are adding these things already and adding overhead to their contract code.
* H: Can testing be accomplished for some of the main clients?
* N: Best initial step would be to ask someone from each client to have a quick look and say on the next call whether they think it would be an undue burden to implement in terms of efficiency and developer time. As Greg pointed out the implementations of bignum math differ client to client.
* Pawel: I started working on custom bignum impementation for cpp, Go team has as well, so I'll take a look.

## EIP 1052: EXTCODEHASH Opcode
* [EIP link](https://eips.ethereum.org/EIPS/eip-1052)
* Nick
    * Increasing number of use cases where, on chain a contract wants to know whether the code of another contract matches a known template in order to do things such as trusting implementations
    * Currently they have to fetch the entire code into memory and hash it and then throw it away which is a waste of gas
    * And we already have this information
    * So I'm proposing a simple opcode to push this info onto the stack
* Piper: On the surface this seems good
* Alex: I agree, would be great if someone could do some asking around as to why this wasn't there to begin with
    * Doing this uses a ton of gas and seems like a useful operator for some of the projects that I've seen people working on recently
* Nick: Probably just an oversight that it wasn't included initially, I'm not sure
* Pawel: From VM perspective, also very useful information
    * Used to have unique ID for executed code
    * E.g. in evm-c this information is already available to VMs so not very problematic to expose it to contracts as well
* Alex: It's fresh, already loaded in storage if you've hit the code so almost no cost to actually implement
    * Probably only a couple of extra lines of code in most of the clients
* N: We should price same as base code copy since cost higher if you haven't already hit the code, I believe it has a base cost then additional cost per byte
* A: Should be same cost as checking the balance or slightly less
    * xcodecopy 700 + 3*number of words
    * xcodesize which is 700
* What are next steps, Nick?
    * It's well-specified, reasonably straightforward
    * Are clients happy to implement and can we move to accept it?
    * Would have to be a hard fork since it introduces a new opcode
* Alex: Would be good to do together with EIP-210, that also adds an opcode
* Martin: actually it does not add an opcode

## EIP 210: Blockhash refactoring
* [EIP link](https://eips.ethereum.org/EIPS/eip-210)
* [Details](https://notes.ethereum.org/s/HJXvL-h0f#)
* Couple of problems with how this is written right now
    * Would have been good if Vitalik was on the call
    * The intent was to not change the semantics of the opcode blockhash
    * Would still return only the last 256 hashes
    * However contract doesn't care if you only ask about most recent or older
    * If I do blockhash on a very old block or call the contract way back
    * So one alternative is to do it as V originally intended, when you do the blockhash opcode you only get the latest 256
        * In that version it does not change anything on blockhash opcode semantics, no client changes required, just need to increase gas cost
        * But to get more useful info people would have to call it so we could add ABI encoding or decoding so you could just call it nicely
    * Second alternative is to have the EIP as written, would change blockhash semantics since you could reach further back
        * Who would ever call it if the blockhash exists like that?
    * Question: Should we add support to obtain the genesis hash from this contract? It complicates things a little bit but probably nice to have.
    * If you invoke this at block one, you go into an endless loop, this affects test cases that execute it.
* Pawel: The current contract is implemented in serpent which only has signed integers. Some comparison in the code that accounted for it so you can overflow the comparison and you get unspecified results. Need another check in serpent to check that argument from call is not negative.
    * There's a PR that fixes these two issues, I plan to continue working on writing unit tests. Not clear if the unit tests should go to EIPs repo or elsewhere.
    * I want to add more unit tests to make sure it works as specified.
    * Then I'd think about optimizing the contract using maybe solidity assembly or something.
    * I'd go with the first of Martin's suggested versions, not modifying blockhash opcode. Seems safer.
    * About genesis blockhash, this issue at block one means you wanted to insert the hash of the genesis, I believe there is a generic solution which is a bit complicated to explain on this call. So instead of replacing stored value you can keep all info all the time about specific blocks and the block number zero meets all these requirements.
    * You can change the logic about how you store info in this way so if it runs from block zero or one, you'd always have info about block zero. Abstract solution.
    * Second part of the solution is to also insert info at deploy time so we have this info also on mainnet. This would solve genesis hash problem but it's quite complex compared with what we have right now in the contract.
    * I haven't finished prototype of implementation, seems like it requires recursive functions, can be flattened down later.
    * Also a bit problematic to insert block hashes at time of hard fork.
    * In smart contracts you can assume info about historic blocks are already there according to the spec, no need to account hard fork number to actually compensate the lack of info because this change was introduced in the middle of the mainnet.
* [PR for Pawel's fixes](https://github.com/ethereum/EIPs/pull/1094)
* Martin: I'm fine with going with original intent, I'd like better ABI and genesis block lookup.

## EIP 1087: Net gas metering for SSTORE operations
* [EIP link](https://eips.ethereum.org/EIPS/eip-1087)
* Moved to next core devs meeting since we ran out of time.

## Concerns that using native browser VMs for running eWasm is not DoS hardened
* [Greg's comment](https://github.com/ethereum/pm/issues/40#issuecomment-390006104)
* Moved to next core devs meeting since we ran out of time.

## Constantinople hard fork timing and what to include (continuing conversation from last call)
* Moved to next core devs meeting since we ran out of time.

## Core dev meeting discussion & changes - scope of agenda items, role of participants, etc.
* Hudson did a write up about this in PMs repo and will elaborate in blog posts about some of the changes that are coming, in particular how they'l be more technical in nature and less philosophical, to save time, and to make sure core devs aren't deciding everything. Our focus here should be low level protocol issues not high level issues and contentious debate.

## Attendees
* Alex (last name unclear)
* Dmitrii (EthereumJ)
* Paweł Bylica (EF: cpp-ethereum/ewasm)
* Greg Colvin
* Casey Detrio (ewasm)
* Paul Dworzanski (ewasm)
* Daniel Ellison (Consensys/LLL)
* Frederik Harrysson (Parity)
* Geoff Hayes
* Greg (last name unclear)
* Hudson Jameson (EF)
* Nick Johnson (EF/ENS)
* Dimitry Khokhlov (EF: cpp-ethereum, testing)
* Piper Merriam (EF/trinity)
* James Ray (Drops of Diamond)
* Lane Rettig (ewasm)
* Danny Ryan (EF: Research)
* Martin Holst Swende (EF: geth/security)
* Tim Siwula
* Péter Szilágyi (EF: geth)
* Phil (last name unclear)
* Alex Van de Sande
* Guests (presenting on new PoW idea)
    * Ms. If
    * Mr. Def
    * Mr. Else
