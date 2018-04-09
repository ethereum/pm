# Ethereum Core Devs Meeting 36 Notes
### Meeting Date/Time: Fri, April 6, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/36)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=SoPfoNpqG0k)

# Agenda
1. Testing
2. [EIP 712: Add eth_signTypedData as a standard for machine-verifiable and human-readable typed data signing with Ethereum keys](https://github.com/ethereum/pm/issues/33#issuecomment-374174501).
3. [EIP 665: Add precompiled contract for Ed25519 signature verification](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-665.md).
4. [EIP 958: Modify block mining to be ASIC resistant](https://github.com/ethereum/EIPs/issues/958).
5. [EIP 960: Cap total ether supply at ~120 million](https://github.com/ethereum/EIPs/issues/960).
6. [EIP process updates](http://eips.ethereum.org/).
7. Research Updates.
8. Metropolis.
9. Client updates.

# Notes

Video starts at [[6:20](https://youtu.be/SoPfoNpqG0k?t=6m20s)].

## Testing update from Dimitry [[6:54](https://youtu.be/SoPfoNpqG0k?t=6m54s)].
* I have First results of test execution via RPC on my local branch of cpp-ethereum client - managed to exec all state tests within seven minutes
* Now working with cpp-ethereum team to integrating my changes
* If someone can provide me a client that can execute those tests in under seven minutes that would be great
* The issue is that there's no consensus about test RPC methods
* I'm still struggling with one method, how to add a new account
* Discussion with Yoichi around executing a tx with a secret key via RPC or registering a new account with a private key that could be used to sign those tx
* Which is better, new RPC method to register new account with private key or a new method which provides transaction with private key to sign it
* What's wrong with send raw tx? Requires account to be registered in keystore.
* Piper: you want an RPC method standardized to import an account but what’s wrong with signing tx and sending over sendrawtx?
* D: you’d need to implement math needed to sign the tx, signing should be done on the client side
* Dimitry to summarize and post to ACD channel so clients can review, and to post link to discussion, to discuss more at next meeting
* [string test_addTransaction(string _jsonTransaction)](https://github.com/ethereum/retesteth/issues/6)
## [EIP 712: Add eth_signTypedData as a standard for machine-verifiable and human-readable typed data signing with Ethereum keys](https://github.com/ethereum/pm/issues/33#issuecomment-374174501) [[11:07](https://youtu.be/SoPfoNpqG0k?t=11m7s)]
* discussed last meeting, lots of support but also need to make sure everyone in ecosystem is on board since we discussed not keeping backwards compatibility
* Remco - took over ownership of EIP 712
    * originally was a way to communicate interpretation of data to be signed to the user agent, user to be presented with a more elaborate view with an understanding of what’s to be signed
    * solves a number of problems with singing arbitrary messages through user agents
	* hashing of arbitrary messages
	* domain separation, when messages do collide but you still want to make the sig incompatible
	* nonces - preventing replay attacks (currently we require each implementation to come up with their own solution for this)
	* original issue of how do we present all of this in a user friendly way such that ppl who are new to cryptographic signing schemes can still use them securely and in a trusted manner
    * this is a lot for one standard! narrowed scope down to just defining a hashing mechanism, able to hash messages into bytes32 in a safe way so that devs can hash anything they want and be safe
    * touches on domain separation as well
* Hudson: still getting feedback, have you seen other groups come onboard and supporting this? any HW wallets?
* R: early EIP had some early uptake, people waiting for things to converge before investing in reimplementing things, Nick Johnson quite active
* Nick what’s your take?
    * Skeptical of original idea of enabling UI display of this
    * Just did a review of the revised EIP and I think it's very promising
* R: read through comments, noticed these issues, i’ll address them
    * I know this is more complex than e.g. ABI encoding
* Martin: is this standard generalized enough or should there be another level such as EIP 191 and have this as a subgroup? does this accommodate all use cases?
* R: made it really generic, supports things not even supported in solidity, should be future proof
* N: i suggested making it a subtype of 191, can cover other data formats as well
* only difference between this and other standard is one byte 0x19 that I turned into 0x1 - we can have larger differentiators
* M: so this is already compliant to EIP191 if you have a version number right?
* N: needs a slight tweak, let’s take this offline
* Hudson: sounds like a lot of support, needs to be polished a bit, let’s get as many wallet teams etc. onboard so this can be accepted, seems like it has good momentum
* R: right now the scope is limited to hashing arbitrary messages, touches on domain separation but doesn’t fully address this, ongoing discussion, but doesn’t touch upon nonces and preventing replay attacks - is this something we want to address in a future EIP?
* it’s a separate issue but might affect how singing standards are implemented at this low level
## [EIP 665: Add precompiled contract for Ed25519 signature verification](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-665.md) [[20:14](https://youtu.be/SoPfoNpqG0k?t=20m14s)]
* Tobias Oberstein introduces this topic
    * proposing adding a precompile for this particular curve procedure
    * a lot of protocols and projects are using it
    * e.g. SSH
    * motivation is to bind ETH addresses and keys to xxxx public keys or verify signatures signed by those keys
    * bind identity on ETH to an ID on an external system
    * can program in EVM bytecode but it costs too much gas
* Fredrik
    * some companies have requested this feature from Parity
    * some say the BN precompile is too slow and maybe ED would be faster, they’re trying to do some on-chain crypto stuff
    * either they want the ED curve specifically or else they’re trying to find a way to do it cheaply
* Vitalik
    * BN128 as a curve not much slower to execute, nothing inherently mathematical that make sit slower than SECP
    * implementation slow because there seem to be more optimized libraries for SECP than for BN128
* F: used BN implementation from cloud flare which is fast on 64 bit platforms but could be slow elsewhere
* V: how much do we need to care about 32 bit platforms? we’ve already kind of made a decision not to care about older hw because of how hard it is to run ETH on an HDD
    * so my inclination is finding and supporting and subsidizing more optimized implementations of SECP stuff since that doesn’t require protocol changes
* F: I don't know of any use cases that specifically require ED
* V: BN has some benefits such as being more efficient for verifying, has batch verification, has good cryptographic properties, the signing process doesn't have branch conditions that make it easily vulnerable to side channels
    * but does this make it worth a new precompile? probably not
    * gains seem marginal
* Hudson: in the past we talked about not adding any precompiles because ewasm will make them unnecessary
* V: I agree, ewasm is fast enough to implement the crypto in ewasm
    * I’d consider precompiles for a cryptographic operation but only if they bring substantial value
    * we have hashes, sig algorithms, pairings, bigint arithmetic
    * at this point if we want to do more work on precompiles then my preference would be to focus on making existing precompiles more efficient, cut down gas cost of this and of bigint arithmetic
    * Zcoin people complained about gas costs of zcoin verification being very high
* H: so we would need wider support for this to go in
* T: how would you verify the BD curve?
* Nick: support for this would be useful for DNS in ENS
* Martin: is it possible to somehow quantify that? how much more useful?
* N: grepping DNS root zone to get some figures
* H: let’s come back to this later on the call
* M: V mentioned lowering gas costs for arith operations for precompiles, can probably be cheaper than they are with some dedicated libraries and optimizations, at least with geth
    * disk access takes most of the time, needs heavy gas cost
    * whereas arith could be cheaper
    * we should discuss changing the gas costs
* Fredrik: I can reach out to the people that asked for ED curve and find out their use case
* H: so let’s collect some use cases and add them to the EIP
## [EIP 958: Modify block mining to be ASIC resistant](https://github.com/ethereum/EIPs/issues/958) [[32:06](https://youtu.be/SoPfoNpqG0k)]
* Piper update
    * I decided to facilitate this discussion
    * I’m not an expert, so I’m acting more as a facilitator
    * We have an EIP that was merged as a draft that proposes some very low touch changes to ethhash algo, which if I understand correctly should be easy for clients to modify internal block sealing to accommodate without any significant changes
    * the idea is not to improve ASIC resistance as much as an attempt to break existing hardware, from my perspective that is intended to be a short term fix
    * assuming we agree that ASICs are a problem and we don’t want them on the network, we’d push them out far enough to get to PoS - also assuming PoS is still far enough out that ASICs being on the network now will be a problem
    * or we could do nothing, and sit back and focus on permanent fixes - tough not knowing what the timeline looks like for PoS
    * I’m hoping that people with more expertise and knowledge chime in so we can reach consensus
    * I’ve had one piece of back channel communication that we can expect current ASICs in production not to be programmable, but no way to verify this
* Vitalik
    * Repeating comments I made in Gitter
    * E3, released a few days ago, efficiency gains relatively limited
    * 180 MH for $800, 2.5x factor improvement over GPUs
    * that plus when we built ethhash we did an analysis and showed that the algo is IO bound
    * speed increase still limited since bottleneck would be RAM, up to some point
    * if compute module really fast then it could do light verification process but I don’t think they’re close to doing that
    * those things together imply it’s likely that ASIC is just a regular computer with better RAM with anything nonessential in GPU/RAM stripped out
    * I heard ASICs are using some sort of new RAM that’s otherwise pretty hard to get, that would imply that it’s just a better computer optimized for IO hard algorithms
    * meaning: there’s nothing we can do
    * even if we replace ethash entirely with equihash or whatever monero uses then the ASIC would still be able to do it
    * Maybe that’s not true, but we have no idea right now what specific protocol change would actually make a difference
    * Only thing that would reliably stop these ASICs is switching PoW to something that’s not IO bound at all e.g. SHA3
    * But I’m inclined not to make a change that drastic, it’s less ASIC resistant so we’d only be buying 6-12 mos, also development effort and getting everyone to upgrade would be chaotic and detract from more important things
    * At this point I lean towards no action
    * Other reason: look at the worst case scenario, Bitmain would control a large portion of the ETH network for some period of time
	* This is not Bitcoin
	* Miners are not in control here
	* If they have majority hash power and try to use it for evil, it would just speed up casper development, to hell with any remaining bugs, we’d launch the thing within a week and mining rewards would go down by 90%
	* I don’t see a game for them where they act in ways that reveal they have 20-25% of ETH hash power 
* Piper: what’s timeline for us to get casper in place?
* V: Danny in progress of finalizing code for second stage of test net, one of our goals for second stage is an algo freeze and full spec of the algo
    * Totally ready for geth and parity to theoretically start implementing
    * Formal verification and multiple academic groups are still checking it
    * If 51% attack concerns demand it then we can skip the auditing and verification stages
    * If geth and parity make it higher priority to implement casper FFG then that by itself gives us some degree of insurance
* P: Formal verification is how far out?
* Danny: they have 4.5 months budgeted, started halfway through March, making really solid progress daily and working closely with Yoichi
* Casper update: Danny
    * Runtime verification guys received a grant, doing formal verification of casper contract
    * I released the implementation guide with some of the updates we’d made and contacted some of the clients
    * It’s a little underspecified still
    * Working on writing formal EIP that specifies exactly what clients need to do at fork
    * Finalizing smaller implementation utils, expect to have EIP ready for review next week
    * plan: have RV formally verify, relaunch testnet with EIP specs, relaunch contract on testnet
* questions
    * where do C++ tests, yellow paper, and kevm come into this?
    * does this stuff happen for any EIP?
    * yellow paper/K specs etc. - are these updated prior to the fork?
* Hudson: EIP gives motivation, implementation details
    * Then yellow paper, kevm team submit PRs to keep up with EIP as it’s being developed
* Nick: that’s reasonable
* testing - Dimitry - when should testing start discussing tests with casper?
    * Currently too focused on test RPC stuff
    * Danny to check back in with Dimitry when EIP is formalized
    * Danny: casper EIP to be a single EIP, unclear whether we’ll put anything else in that fork, it might just be Casper
* H: usually tests are prepared well before announcement of hard fork, get finalized as we’re announcing dates, timeline
    * Byzantium: we had test cases made
* D: a new test implemented via RPC would require a couple of major clients to support it, still haven’t finished protocol, so if you want to start casper tests, we should work on old format with hive and testeth in cpp-ethereum, implement changes in cpp as we did for byzantium
    * And i’ll freeze my current work on RPC stuff and focus on casper testnet
* Danny: continue your work for now, we can shift after formalizing the EIP if we need to
* Dimitry: maybe I can finish in time before casper, then every client could work with the new test
    * Just a couple of RPC methods to be implemented
    * I'm going to do a new general test format for the ethereum tests since state and blockchain tests now have common elements, it's reasonable to develop a new, single, general test format executable via RPC
* H: we're trying to coordinate between testing and research but we should not be rushing the research efforts unless there's an emergency to avoid breakage
* Ben Edgington, Pegasys
    * On yellow paper remark
    * I raised the idea that EIPs ought to contain a PR against the YP before being merged or accepted, has that been thought about? Need not be written by author of EIP but would help with rigor of formulating EIPs
    * Hudson: brought up multiple meetings ago, won’t discuss today but let’s bring it up by next meeting at the latest
* does anyone else have a strong opinion about whether or not we should implement this ASIC resistance?
* Nick: proposed changes relatively straightforward but I don't think the current situation necessitaties this being its own hard fork, we can roll it into a future hard fork
* V: I agree with that. even if we want to hard fork, this is not an emergency situation that would require speeding up the next fork ahead of schedule
* Piper: would be good to know we’re breaking something as opposed to probabilistically breaking something
* Hudson: from community perspective, I’ve been seeing a lot of discussion back and forth, many ppl think it’s a security risk but they’re not sure how, some ppl think we should do nothing, some people are very opposed to Bitmain, not sure where that comes from but a bit of crossover from Bitcoinc community , 
    * For those listening in who are not core devs, you can do a carbon vote, you can do stuff in forums or your own EIP, if the community truly wants this to happen and has a good enough reason
    * But as of now it sounds like consensus of core devs is that we should not do anything at this time
* Daniel Nagy: can we elevate the question one meta level up and agree on conditions, what kind of development would require an emergency response?
    * These ASICs are ~2.5x more efficient, so maybe not that much of an issue
    * But an interesting question is, what kind of development would require an emergency response?
* V: any ASIC manufacturer has an incentive to downplay how much influence they have over the network because the more they have the more pressure there is to hard fork them away
    * So Bitmain, eth2pool, north korean government, some people in Iceland, whomever, even if they have 51%, the chance we’d find out before they began a 51% attack is quite low
    * for that reason I don’t think we are going to see flags that are redder than actually seeing an ASIC and someone being able to buy it but less red than a 51% attack already happening
    * It seem to me that just seeing someone able to buy an ASIC is not a sufficient condition, and a real 51% is a sufficient condition, but I don’t see any likely flags in between
* Nick: signals we can look for such as someone promising to sell an ASIC that’s orders of magnitude more efficient than gPU or sudden uptick by one particular pool
* Martin: should we try to prepare by defining an alternate hash algo and implement that, have it ready to go on short notice?
* V: my intuition is that if we can farm it off to someone to create a GPU version of simple SHA3 or any hash algo, then that would make the most sense since it’s not IO bound and it’s very different and would confer temporary benefit of making block headers much faster to sync
* Ideally make sure to find ways to do that in parallel to all of our other work so it doesn’t slow down client optimizations, DoS resistance, etc.
* Piper: I have what I need to go back to the EIP and post a follow up, we have a decent picture of how everybody else feels about this issue
* Danny: say we have FFG on top of a mined network with ASICs, do we consider this a problem?
* V: in that case, a 51% attack can effectively prevent finalization of new blocks but it cannot break finality
    * one simple fix that could mitigate power of a 51% attack is adding to fork choice rule that head should be preferred if it has a larger number of casper votes for current epoch
    * if there are two chains, one with votes and one without, it would favor ones with, should render 51% attacks weaker
* H: We'll let Piper update the EIP, community discussion will continue and if it's still an important topic to the community we can bring it up again in the next meeting
## [EIP 960: Cap total ether supply at ~120 million](https://github.com/ethereum/EIPs/issues/960) [[1:00:06](https://youtu.be/SoPfoNpqG0k?t=1h6s)]
* Vitalik could you explain your April Fool's joke which everyone took seriously?
    * decide on some maximum supply cap, i recommended 120.4 M
    * makes all rewards, PoW and commitment to future rewards e.g. sharding and PoS rewards all proportional to the max supply minus the current supply
    * ETH supply instead of going up linearly , would exponentially decay and converge towards maximum
    * at least until we introduce things like rent and partial theory claiming at which point we’ll have a balance where supply will end up being constant below max, coins getting burnt and created would match
* Daniel: up to now contracts have been burning ETH by locking it up, but there would be a way to burn so that it’s removed
* V: one way of burning that exists in the casper contract is if a validator gets slashed then their penalty is it stays inside casper contract as contract balance
* if this contract were the only thing issuing rewards then easy to calculate, it could be assigned 120M ETH and set rewards proportional to balance remaining inside the contract, could standardize by sending to zero address, rewards could be paid out of zero address proportional to money there
* Nick: I think capping supply is a bad idea because you can fund security through either inflation or tx fees, and funding through tx fees encourages holding and discourages an active ecosystem
    * bad idea in general
    * can lead to deflationary spiral
* V: worth noting that tx costs in ETH in the long run are not proportional to ETH fees, they’re proportional to supply and demand
    * seems like they go up when ETH goes up but really if the price of ETH were to go up for some exogenous reason which in general is likely to happen if any proposal reducing supply is implemented
    * would lead to reductions in tx fee that ppl actually pay
    * I don’t see a reason to expect long run for there to be a hard link there
    * deflationary spiral question, from macroeconomic view
	* tends to apply when the thing that’s deflationary is the unit of account for an entire economy, long-term sticky prices being set in this unit
	* in the past ETH gas prices were sticky but now we have dynamic fee calc. for nearly everything
	* I don’t expect prices to be sticky and ETH is hyper volatile so I don’t think we’ll even notice differences in price movements
* Nick: Don’t mean deflationary spiral in the traditional economic sense, instead I mean assume people adjust tx volume based on tx cost and there are some minimal fees we need to pay to secure the network
    * higher fees -> lower tx -> higher costs
* V: I’m not suggesting higher tx costs
    * main place in long run the money would come from is lower revenue paid to participants who provide security
    * short term: miners, long term: casper validators
    * long term: casper validator revenue should be roughly equal to amount ppl pay in tx fees
* Nick: but there’s no closed loop there, there’s some level of incentivization/staking we need to secure the network, nothing ensures that tx fees will match up
* V: there’s no minimum, there’s a level
    * if we have a smaller reward then maybe rather than 20M ETH staked we might have 10M ETH
    * OTOH if we have a cryptocurrency that’s inflationary that could lead to its ratio dropping meaning less capital securing the network
    * kind of hard to figure all of this out in the long run but I personally think there’s evidence that tx fee levels are capable of providing enough revenue to secure a blockchain
    * in the long run if they’re not then there’s a question of, how valuable is the system we’re building in the first place?
* N: I don’t think tx fees have to be the thing that supports the blockchain
    * If we need some amount of money to incentivize miners or stakers you can take that from inflation, better since it imposes the cost on everyone invested in system not just those transacting, encourages transacting
* V: I used to think this way but as Vlad keeps pointing out if you do this then every ERC20 token becomes a better SOV
    * if ETH is the one token that gets inflated to pay for security, and you can print out ERC20 tokens on top of ETH and market them and they don’t have this disadvantage then eventually there may be a tragedy of the commons where even though ETH is necessary for security no one wants to support it
* N: sounds a bit of a stretch for 2% pa inflation
* V: that’s a lot, long term ppl expect to be able to earn ~4% pa from stock market, if you take 2% off of that then you’re saying the amount of money someone needs to retire goes up by 2x
    * in context of financial market returns 2% is a huge deal
* H: does anyone have an idea of community sentiment?
    * I haven’t been able to pick up on this much
* Nick: seems broadly in favor of a supply cap
    * H: seems this way on EIP, Twitter, Reddit
* N: we currently have no constraints
* V: my preference for implementation is we just premine max cap minus current ETH supply into some particular address eg address zero
    * when paying rewards we subtract from that account
    * Nick: that’s much simpler than what I was thinking which sounds good
* Danny: adds complexity to casper FFG contract to calculate what pct coming from reward rather than from base but not too complex
* H: might this go into Metropolis?
* V: if the community really wants it then could do it in metropolis phase II, or could wait and implement as part of casper FFG change, I’m kind of waiting to see more community feedback
* H: let’s bring this up again on the next call when we have a little more community feedback
## EIP process updates [[1:14:02](https://youtu.be/SoPfoNpqG0k?t=1h14m2s)]
* Nick set up http://eips.ethereum.org/ auto-generated using Jekkyl
* Nick overview
    * takes all MD files, indexes by type and category and generates individual packages for them, as soon as an EIP is added it gets updated with auto page build
    * continuous page build using travis that checks EIPs and PRs for syntactic validity, can take some load off editors and make sure everything is valid
    * in general I’m trying to work towards a set up where editors merge drafts sooner and quicker and make it easier for authors of drafts to keep working on changes until ready to take to all core devs or standardize
    * so I’ve also written a bot that watches EIP PRs and when it sees one that’s an edit to existing EIP drafts it allows it to be merged if one of the authors of the draft submitted it or approved it using a PR review
    * for trivial changes or change to draft, no longer require manual approval, can be automatic
    * my goal is to get to a point where a submitter can get an EIP draft number immediately for their EIP, and it doesn't require any additional work by the editors
* Origin: [EIP 956: Proposing a revised process for handling of EIP drafts](https://github.com/ethereum/EIPs/pull/956)
    * making EIPs less ambiguous with how drafts are handled
    * one point of contention: taking out the words “consistent with ethereum philosophy"
* Nick and Greg colvin: should we number EIPs immediately or only after they get past the draft stage?
    * Feedback appreciated
    * For anyone who wants to keep the “in keeping with the ethereum philosophy bit” - if you can describe it, I’m happy to keep it
## Research updates [[1:17:44](https://youtu.be/SoPfoNpqG0k?t=1h17m44s)]
* Sharding: Vitalik's update
    * We’ve been looking at more ways to make the entire setup of collations - how they work and get verified - how to make this simpler to implement, but we’re in the idea phase
    * I expect implementation algo to become simpler at the end of all this
* Prysmatic Labs
    * Adding sharding to geth
    * Began recording meetings and releasing blog posts
* James Ray
    * Working on Drops of diamond - rust implementation of sharding - working on SMC in vyper
    * someone else working on proposer and collator
* Pegasys (Ben)
    * Working on sharding
    * Put up a post on ethresarch today on current proposal around validators and collators
    * Waiting to find out what new model looks like
## Metropolis Part 2 (Constantinople) [[1:20:06](https://youtu.be/SoPfoNpqG0k?t=1h20m5s)]]
* Hudson: Have some more things that could be EIPs, esp. if we do ETH supply cap
    * If we did that before casper we could include some other smaller EIPs we want to include
    * Should it happen before Casper?
    * Don’t have much of an updated opinion, but some community members feel that we are getting behind/not implementing fast enough since we don’t have another HF planned, whereas really we are just shifting priorities e.g. around research topics
* Danny: Casper, sharding are the most important things to focus on, we are working on the most important things
* H: We could cancel Constantinople, but there were some EIPs that we wanted to get in which could go into the Casper hard fork.
## Client/team updates [[1:22:16](https://youtu.be/SoPfoNpqG0k?t=1h22m16s)]
* geth (Martin)
    * made a release ten days ago containing some DoS fixes
    * some updates to improve block processing times up to 50%
* Parity (Afri)
    * we forked Kovan to enable WASM smart contracts, went smoothly, now there are a few contracts deployed
    * had some issues with warp sync, clients can configure a minimum block to warp too, there are many outdated snapshots, ppl warp to e.g. block 4M and then still have to sync through another million blocks
    * Fred: doesn’t sync normally, forces a warp sync
	* you try to warp sync, it fails or cannot pair with a snapshot, reverts back to normal sync then takes a week to sync
	* so now you can force a warp sync by setting this "warp barrier"
* cpp-ethereum (Pawel)
    * separate client connector code, adding support to cpp-ethereum, hera, evm-jit
    * Andrei working on some network stack improvements inside the client
* Harmony (mkalanin)
    * No major updates since last release
    * Working on casper, planning next release
    * Will definitely include proxy fine tuning, noticed that DB reads are taking 40% processing, pretty confident that it could be improved
* ewasm (Lane)
    * evm2wasm - Started running first state tests via evm2wasm, getting state tests to pass
    * EVM-C, cpp-ethereum, Hera fixes and improvements
    * eWASM engine abstraction
    * Everett Hildenbrandt update: going back and forth with Yoichi about removing some tests from the VMTests to make it only test core VM infrastructure. I think it's a good step in the direction of "separating the ethereum specific stuff out of the EVM", the same way that the "e" is separate from the "wasm" in ewasm.
* Turbo geth (Alexey Akhunov, full update [posted in agenda](https://github.com/ethereum/pm/issues/36#issuecomment-379047053)
    * Posted update in GitHub agenda
    * rebased geth as of Apr 2
    * Will be talking about turbo geth at devon
* Pegasys (Ben)
    * development continuing apace
    * relatively soon we’ll have more updates
* Trinity (Piper)
    * No major updates
## [EIP 908: Reward for clients and full nodes validating transactions](https://github.com/ethereum/EIPs/pull/908)
* We're out of time, let's discuss at the next meeting
* Please read this to prepare for next meeting

## Attendees
- Afri Schoedon (Parity)
- Chris
- Daniel Nagy (Swarm)
- Daniel Ellison (Consensys/LLL)
- Danny Ryan (EF: Research)
- Paweł Bylica (EF: cpp-ethereum/ewasm)
- Martin Holst Swende (EF: geth/security)
- Nick Johnson (EF: geth)
- Thibaut Sardan (Parity)
- Mikhail Kalanin (Harmony/EthereumJ)
- Fredrik Harryson (Parity)
- Vitalik Buterin (EF: Research)
- Chih-Cheng Liang (EF: Research)
- Hsiao-Wei Wang (EF: Research)
- Karl Floersch (EF: Research)
- Piper Merriam (EF: Python/py-evm/Harmony)
- Tobias Oberstein (Crossbar.io/XBR)
- Remco
- Hudson Jameson (EF)
- Lane Rettig (ewasm)
