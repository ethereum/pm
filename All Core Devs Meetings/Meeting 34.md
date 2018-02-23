# Ethereum Core Devs Meeting 34 Notes
### Meeting Date/Time: Fri, February 23, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/32)
### Audio/Video of the meeting (WIP)

# Agenda
1. EIP process improvements
1. Constantinople (What to include, timing)
1. Test RPC protocol discussion
1. Easy parallelizability (EIP648)
1. BLOCKHASH opcode (EIP96/EIP210)
1. Client/research updates
1. Timing of next call

## EIP process improvements
- Want a channel where it's easy for people to communicate about what changes they want to happen
- There is a group called Fellowship of Ethereum Magicians (Hudson to post link), self-organizing group to maximize technical opportunities
  - Like IETF for Ethereum, self-organized group of engineers, scientists, technologists who "keep things running" - make sure all of our equipment speaks the same protocol, etc.
  - Will do a workshop at EthCC
  - Jamie Pitts, Greg Colvin have organized
- Will Yoichi be a part of the governance process going forward? A chance he will join again in the future.
- Nick: We need to distinguish between writing a standard and adopting it
  - IETF: Consensus is not about majority votes
  - Hard fork is the final option
  - Can we publish things and let people choose whether to support them or not?
  - Firm up the process of what is considered merged, and the technical requirements of EIP editors
  - Make it clear to everyone involved that EIP writing is a technical process, and that if something is merged it does not mean that it will ever be adopted
  - In short, if something is technically well written, it should be merged but may never be adopted
- Greg: we don't have a good way to keep technical issues separate from policy issues
  - It's difficult to move forward with proposals if we're overwhelmed with debate about the wisdom of a proposal before editing, drafting, merging complete
  - There should not be huge debates about whether this EIP should be assigned a number, it should not be so contentious
- [IETF article from Hudson](https://tools.ietf.org/html/draft-resnick-on-consensus-01)
- Avsa: not merging things until all objections addressed? This is very hard, same objection can be made in different language
  - We could add an obligatory section on every EIP where you list every main objection and address each one somehow
  - In practice it's hard to separate tech proposals from policy proposals as Greg suggested
  - Maybe we should not merge things that we never want to become standards
  - Greg response: things can become a draft, drafts don't have an EIP number. Once it's a draft it can be accepted, deferred, rejected, etc.
- Greg: we need a body where we can have these arguments in a civil, deliberative way; doing this esp. at the pre-draft stage in Github comments is not the right forum
- Tim: NEO voting
  - They have an electoral system
  - Some people verify their addresses and then they have more authority with their votes
- Vitalik: In general I dislike allowing coin votes for anything
  - Random people who happen to have a lot of ETH are not necessarily the people who have strong technical opinions
  - For things that don't pass developer consensus or have tradeoffs, as much as Carbon Votes are problematic, they're one of the least bad mechanisms we have, esp. in combination with other types of community polling
  - But I do also feel that rather than only invoking for very controversial stuff like the DAO fork and issuance reduction, maybe we should use it for everything
  - Carbon Voting has its flaws and should not be a sole signal but it's been used twice, and it's okay to listen to as long as you recognize that it's one of several signals
  - Avsa: 100 people responsible for 80% of the voting power, this is inevitable due to power distribution of tokens and voter apathy
  - Tim: as Ethereum becomes more popular you'll get more random feature requests
  - Vitalik: decision markets are hard because choosing a single objective function is hard--I don't believe it's ETH price
  - We can return to this in 2-3 years if Maker DAO and other projects find that it's working for them
- Vitalik: In general, our governance mechanism is really not that bad, the main flaw is not so much in the mechanism itself but in how we communicate them
  - E.g. re: standardized ETH recovery, the impression that a lot of community members got from the outside is that if it's merged, it's a lot closer to being accepted than anyone involved in the decision-making process intended to signal that it is
  - Hudson: can make this clearer, add a disclaimer: "Just because this has been merged does not mean it is any closer to being accepted, this is just a draft."
- Nick: Some people suggest we should not formalize governance because then it will be vulnerability to exploit capture, etc.
  - But I am concerned that not formalizing it could have the same outcome
  - Hudson: We need some degree of formalization, but maybe not too strict, e.g. these calls
  - Vitalik: Agree that having these calls is good, giving relative indications about status of various EIPs, etc., but then just because everyone on the call agrees an EIP is good it should not 100% necessarily be approved
- Avsa: Someone opened an EIP, was probably a joke, can you have one standard negating another? Both can be drafts!

## Constantinople
- On last call, we decided that some EIPs could definitely go in
  - [EIP 145: Bitwise shifting instructions in EVM](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-145.md): pretty well-formed, but not 100% implemented or tested
  - [EIP 210: Blockhash refactoring](https://github.com/ethereum/EIPs/pull/210)
    - Replace BLOCKHASH opcode, but also has the feature that you can invoke the contract directly to gain access to > last 6 blockhashes
    - Can access any previous block from the current block in the maximum of three merkle hops
    - Difficulty to implement? Vitalik: There is already an implementation in at least a couple of clients, just need to write a bunch of tests for it.
    - Martin: Not that difficult to implement in the client, but is the actual contract code finalized?
    - Paweł: I would like to see the spec finished, but I made some comments/amendments months ago and haven't had an answer. It should be merged as a draft so I can PR to fix some issues.
    - Hudson: Vitalik please make final changes to the EIP and merge it
    - Vitalik: Please look through it again and make sure there are no issues. I'd like someone independent to write some tests for it. Prefer not to merge until the EVM code as written is very very close to final.
    - Paweł: There is at least one bug in the contract. Would be easier if the code is merged so I can send PR rather than just discuss in the comments.
  - [EIP168](https://github.com/ethereum/EIPs/issues/168), [169](https://github.com/ethereum/EIPs/issues/169) - Killing dust accounts, replay protection for this
    - [Andrei's graph](https://github.com/ethereum/EIPs/issues/168#issuecomment-364066940)
    - [Alexey Akhunov data](https://medium.com/@akhounov/more-data-for-eip-168-kill-dust-accounts-83e8dd0938d3)
    - Alexey did some tests, ~1M accounts, roughly less than half the accounts in the state are zero balance
    - Should this go into Constantinople?
    - Vitalik: I'm not concerned about arguments about deleting people's money since this would only delete the account if at the end of a transaction it has less than gas_price x 21,000, can only increase the cost of a transaction by more than a factor of 2-epsilon
    - V: I prefer variant B
    - Nick: if someone sends a tx with a very high gas price they risk losing that amount of gas x 2
    - Martin: we should set a hard limit in the protocol, this would be less risky
    - Casey: unclear how much benefit clearing the dust accounts would have; per Andrei's post, state goes from ~9.6 to ~7.3 gb (~2.3gb savings)
    - Vitalik: state size control is important not just for saving disk size but also reducing fast sync time, also the bigger the state, the less you can keep in memory which makes DoS attacks worse
    - Nick: if we decide not to clean up existing dust accounts but set a rule going forward, we can do the dynamically-adapting thing without risking attacks
    - Hudson: good idea if we can't decide whether savings are worth it for the risk
    - Casey: nonce replay protection scheme might also make it more difficult to do later sharding approaches with nonces and merkle proofs
    - Vitalik: keep in mind that this will not apply to abstracted accounts (if we do account abstraction) anyway since they will all have code
    - If a few years from now the state space is 3x bigger due to abstracted accounts the actual gain here goes down to maybe 7-8%, in which case maybe that development time would be spent on Casper or sharding
    - Vitalik: there are intermediate versions we can consider, e.g., if at some point we upgrade tx formats, it would be a great opportunity, 2-3x simpler to implement a one time account clear of some kind, but this is a longer-term thing
    - Nick: re: EIP169, how do you sign a tx, wouldn't you need to know which block it will be included in?
      - V: an account going from non-existent to existent is not something the owner of an account can do
      - You can only send a tx from an account that already exists
    - Nick: we could do 169 without 168 initially
      - New nonce scheme, gives people a chance to adapt to that
      - In a later fork, implement dust cleanup which requires it
    - Tim: does account abstraction supercede this?
      - Vitalik: account abstraction only applies to new accounts
    - Avsa: people who have moved ETH to WETH would not be affected by this as there is no dust cleaning for tokens
      - Martin: don't think people would mind if dust is cleaned, most of it is probably from people who tried to move all ETH out of an account but didn't use Javascript bigints and didn't get the math exactly right
    - Hudson: no clear agreement on this so let's move on
  - [EIP859: account abstraction](https://github.com/ethereum/EIPs/issues/859)
    - Last time we agreed to table this and focus on things like Casper
    - Vitalik: This will happen anyway inside sharding, it will exist in some clients in some form; at some point the code will be mostly written but that's still some time away
      - It's a fairly substantial undertaking, esp. because of things like miner strategies
      - So if we try to do it very quickly (in time for next hard fork) we don't get the benefit of piggybacking on work being done on sharding side
      - Personally I would therefore lean towards not putting this into Constantinople
      - Main reason to do this would be some urgency for some particular applications that could take advantage of abstraction, but there may also be simpler kludges to provide it with off-chain protocols
    - Hudson: as discussed last time, too much work for Constantinople but should be reassessed after Constantinople esp. depending where sharding is at that point
  - [EIP232: New tx formats](https://github.com/ethereum/EIPs/issues/232)
    - Creates two new types of transactions
    - Vitalik: overview
      - Superset of earlier abstraction proposal
      - Chain ID replay protection against ETC chain
      - We had to do a series of kludges for this
      - This got a bit too complicated
      - The idea was to make a clean, new type of tx where the first number would always be a transaction version number, second value the network ID, then from there it depends on transaction version number
      - Benefit: way more forward compatible
      - Would be convenient to do at the same time as account abstraction, if not adding any new tx types then we're not getting much benefit, whereas if done at the same time, it makes sense because there is an some actual, new tx format
    - Hudson: okay, so this doesn't need to go into Constantinople either
  - Timing
    - [EIP 145: Bitwise shifting instructions in EVM](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-145.md) - agreed upon
    - [EIP 210: Blockhash refactoring](https://github.com/ethereum/EIPs/pull/210) - need to work on some more, but going in direction of being approved for the next hard fork
    - Are there other things we want to add? Or should we just continue to focus on casper and sharding?
      - Vitalik: We should consider a substantial reduction in gas costs of curves, ZK-snarks opcodes, this would be a fairly trivial EIP to put into the hard fork
        - Actual numbers are in [benchmarking repo](https://github.com/ethereum/benchmarking)
          - CPP, Geth, Parity covered
          - But not necessarily using the same test vectors in all cases
          - Geth has the most compehensive test benchmarks
        - karalabe: performance is about 18x faster than current implementation, so if we can implement that then gas costs can go down significantly
          - Go was slower of implementations
          - So if we get 16-18x faster how does that compare to other clients?
          - Dmitrii: we do not have these benchmarks for EthereumJ
    - If we can finalize this stuff over next month or so, we can lock in dates for testing Constantinople
      - Also tied to first Casper implementation
      - Would be good for clients to add this to their roadmaps
      
# Test RPC protocol discussion
  - https://github.com/ethereum/retesteth/issues/4
  - Dimitry: I started to work on this new approach which would allow us to generate consensus test from any client which implements new testrpc method
  - Clients can use this to generate new tests

# EIP648: Easy parallelizability
  - https://github.com/ethereum/EIPs/issues/648
  - Tim: Wondering if you guys think it's important enough to start considering
  - Similar to introducing a new tx type for [EIP232: New transaction formats](https://github.com/ethereum/EIPs/issues/232)? Not quite
  - Vitalik: New tx type is cosmetic whereas parallelizability requires changes to protocol guarantees and architecture
    - Pretty sure this could open us up to call stack depth attacks
    - Deep changes are the parts that include actually parallelizing contract execution
    - It's totally fine for people to try implementing but I'm curious realistically how you would test this and what info you would get from the test
  - Tim: I'm also wondering, which client would be good for making a branch for this
  - Vitalik: Use a pretty simple algorithm to retroactively assign lists to previous tx
    - Try to run in parallel and see what the speed up is
    - Call stack depth attack: when an attacker creates a tx which calls a contract, which calls itself a bunch of times and then calls a target contract, but when the target tries to call out to something else it fails because call stack depth too high
      - In current parallelizability proposals a contract has to specify a list of addresses it can call, any attempt to go outside that range leads to an immediate exception
      - So it also lets you make a tx which calls some contract, if it will call another contract then the second degree call could be outside the access list so it would fail
      - Casey: so if a contract assumes its calls always succeed, that would be the vulnerability
      - V: You cannot assume a call succeeds and need to handle the case where it fails
      - We did come up with a bunch of other countermeasures before fixing this issue
  - Hudson: need to explore this more before the next core devs meeting
  - Martin: parallelizability definitely will not go into Constantinople since it requires large changes
  - Casey: until we know bottleneck about disk I/O and how to optimize it, this EIP doesn't make it possible to increase block gas limit without some of the other disk I/O optimizations that are being explored with e.g. TurboGeth
    - TurboGeth disk I/O optimizations are therefore the most important things to work on prior to this EIP
  - Hudson: Not going into Constantinople

# BLOCKHASH opcode refactoring (EIP96/EIP210)
  - https://github.com/ethereum/EIPs/issues/96
  - https://github.com/ethereum/EIPs/pull/210
  - Paweł: already discussed on this call
  - note: 96 was abandoned and replaced by 210, we can close out the old one

# Client/research updates
  - Parity (Afri)
    - no update
  - Geth (Péter)
    - Just had major release (1.8.0, 1.8.1)
      - Happy that the light client is again seemingly functional modulo some rough edges and bugs
    - Martin implemented and we merged in bitshifting EIP
      - If anyone wants to write tests or needs a client that has this, they can use geth
  - EthereumJ/Harmony (Dmitrii)
    - We are working on the next release
      - reduced memory from 4gb to 1.5gb
      - very stable but found a bug with Windows and DB library, need to fix this bug before release
      - we expect to do this in about two weeks
    - For Casper, now debugging mining and validator
      - We can participate in this in the next week
  - CPP
    - Paweł: nothing to share, no new features
    - Dimitry: testeth tool now separated from cpp client, I've been working on retesteth repository, current version of testeth supported by Yoichi in his fork of cpp-ethereum, will remove from cpp client and make it more stable
  - EthereumJS (Casey)
    - no updates
    - Most team members working on cpp-eth and ewasm
    - ewasm: working on dockerization, planning a demo at ethcc
  - PyEVM/Trinity (Lane)
    - sharding branch merged into master
    - work continuing on networking code and async python
  - Research update (Vitalik)
    - Casper: EthereumJ close to having something testnet compatible, last round of changes to the spec before audit
    - sharding: lots of discussions past couple of weeks on sharding designs, what to do first, what's compatible with what, what right path forward re: different stages, all of this on http://ethresear.ch forum, being discussed a lot between Vitalik and Justin
  - Solidity (Christian)
    - Release recently, will have one soon
    - 0.4.21 hopefully last before 0.5.0
    - We're adding tons of breaking changes
    - I'm confident we're making great progress in last few weeks

# Timing of next call
  - Skipping meeting in two weeks due to EthCC (many participants will be there)
  - nothing especially urgent such that one week would make a difference, next call in a month, i.e. March 23

## Attendees
- Afri (Parity)
- Alex Van de Sande (Mist/Ethereum Wallet)
- Casey Detrio (Volunteer/EthereumJS/ewasm)
- Christian Reitweissner (cpp-ethereum/Solidity)
- Daniel Ellison (Consensys/LLL)
- Dimitry Khokhlov (cpp-ethereum)
- Dmitrii (EthereumJS)
- Greg Colvin (Fellowship of Ethereum Magicians)
- Hudson Jameson (Ethereum Foundation)
- Jutta Steiner (Parity)
- Jared Wasinger (EthereumJS/ewasm)
- Lane Rettig (Ethereum Foundation)
- Martin Holst Swende (geth/security)
- Nick Johnson (geth)
- Paweł Bylica (cpp-ethereum/ewasm)
- Péter Szilágyi (geth)
- Tim Siwula
- Vitalik Buterin (Research)
