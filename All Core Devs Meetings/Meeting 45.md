# Ethereum Core Devs Meeting 45 Notes
### Meeting Date/Time: Fri, August 24, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/54)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=6CZ1uO_WxVk)

# Agenda

1. Testing
2. Client Updates
3. Research Updates
4. [Constantinople](https://github.com/ethereum/pm/issues/53)
    a. EIP 1014 Issues
    b. [EIP 1218: Simpler blockhash refactoring](https://github.com/ethereum/EIPs/issues/1218). Looks like we are dropping this one unless someone speaks up, like, immediately.
    c. [EIP 1283](https://eips.ethereum.org/EIPS/eip-1283): 1283 is moving forward per discussions on the previous call and the core devs chat room.
5. Three competing EIPs to delay the difficulty bomb and reduce/maintain the block reward:
    a. [EIP-858](https://github.com/ethereum/EIPs/pull/858) - Delay bomb and reduce block reward to 1 ETH per block.
    b. [EIP-1234](https://github.com/ethereum/EIPs/pull/1234) - Delay bomb and reduce block reward to 2 ETH.
    c. [EIP-1295](https://eips.ethereum.org/EIPS/eip-1295) - Delay bomb, keep rewards to 3 ETH, change other factors such as POW incentive structure.
There is renewed interest from miners to implement [ProgPoW](https://github.com/ifdefelse/ProgPOW#progpow---a-programmatic-proof-of-work).

Different articles/links regarding potential issuance reduction conversation:
- [A Case for Ethereum Block Reward Reduction to 2 ETH in Constantinople (EIP-1234)](https://medium.com/@eric.conner/a-case-for-ethereum-block-reward-reduction-in-constantinople-eip-1234-25732431fc77)
- [Reddit discussion of the above article](https://www.reddit.com/r/ethereum/comments/92g404/a_case_for_ethereum_block_reward_reduction_in/?st=JK4MT60F&sh=257437dd)
- [Coinvote (79 participants): What should be done regarding proof-of-work issuance until Casper is ready?](https://www.etherchain.org/coinvote/poll/298)
- [FEM Forum: EIP-1234 vs EIP-1227: Constantinople Difficulty Bomb & Block reward](https://ethereum-magicians.org/t/eip-1234-vs-eip-1227-constantinople-difficulty-bomb-block-reward/807/)
- [Bitfly Twitter Post on Miner Opinion](https://twitter.com/etherchain_org/status/1031443277118144513)
- [FEM Forum: Final Request From the GPU Mining Community](https://ethereum-magicians.org/t/final-request-from-the-gpu-mining-community/1050)
- [EIP 1295 Presentation](https://drive.google.com/file/d/15n7Vur8wwlfDK6ZXwohUc95rXOUIXo7j/view)
- [Ethereum’s Economic Breakpoint: An Analysis](https://crypto.omnianalytics.io/2018/08/23/ethereums-economic-breakpoint-an-analysis/)

Call starts at []

# Testing update
* Dimitry update
    * Working on new test cases for CREATE2
    * Figuring out how to process no proof blockchain tests
    * Last time I introduced a roadmap for the test cases, asked for your ideas and comments, but haven't seen any comments in the google doc about this
    * There are many test cases to cover, don't assume we can release anytime soon, we need better test coverage for new opcodes, etc.
    * Or we might end up to an uncovered test case and potential consensus issue
    * EXTCODEHASH and CREATE2 test cases available, anyone can try now on tests repo (as PRs)
        * Will be adding to Hive as well soon
    * We should adjust schedule, might not make it before DevCon
* Martin update
    * Doing some revamp of fuzz testing
    * Preparing production environment around fuzzer, hoping to start soon

# Client updates
* Parity (Fred)
    * No major updates
* geth (Peter)
    * Did a major miner rewrite
    * Mining concurrently on multiple blocks, streaming uncles and tx while mining
    * Push notifications, local account prioritizations
    * Huge shout out to Peter Fletcher (?) who was pushing us towards this release
    * Will probably push out another release on Monday
* aleth (Pawel)
    * Some tweaks for Ewasm testnet
* Harmony/EthereumJ (Dmitrii)
    * Bugfixes, dev API improvements, working on Constantinople
* Trinity (Piper)
    * One EIP away from having all Constantinople stuff done
    * Trinity does now sync full mainnet and keeps up with the chain
* EthereumJS
    * No one present
* PegaSys (Matt)
    * Syncing full archive through 4.85M
    * Wrapping up JSON-RPC and mining works
    * Working on storage and stability
* Igor (Mana)
    * Passing 100% VM tests
    * 67% [??] tests passing
    * Expect to be passing all tests within three weeks
* Jacek (Nimbus)
    * EVM is nearing stability
    * Exploring using it through EVMC with geth running the chain but our EVM
    * Working on light clients
    * Have a track going for the beacon chain
* Ewasm (Alex)
    * Just finished two week long sprint
    * Testnet is running with aleth and geth independently (not together yet)
    * Block explorer up
    * Can deploy metered contracts
    * Next focus is language support, toolkit to interact with Wasm contracts

# Research updates
* Danny update
    * Work on RNG for beacon chain
    * Lots of implementations of the beacon chain
    * Spec has been tightening up
    * Formal verification of epochless Casper, modification of FFG, can find this on https://ethresear.ch

# Constantinople
* [Progress tracker](https://github.com/ethereum/pm/issues/53)
* EIP 1014 Issues
    * Pawel: proposed renaming SHA3 to KECCAK256 for clarity
    * L4, Spankchain weighed in on EIP
* [EIP 1218: Simpler blockhash refactoring](https://github.com/ethereum/EIPs/issues/1218). Looks like we are dropping this one unless someone speaks up, like, immediately.
    * Zsolt
        * I've been thinking about this for a long time, it would be very useful
        * I want to do trustless checkpoint syncing for LES, light client
        * We are really missing some way to prove with realistic resource requirements that a certain blockhash is in the chain
        * Even proposed a small extension of this EIP
        * I'm willing to do the implementation in geth
    * Fred
        * We've looked at this, think it's a good improvement
        * We currently have hardcoded CHC checkpoints
        * May not be able to remove them entirely with this change
        * Main question, is it included in Constantinople or not?
    * Skinny version: Not heavy requirement, requires only log no. of steps
    * Dimitry
        * Creating test specifically for new blockhash would be a new topic
        * Could this be done if you get more help?
        * That would take some time to onboard new people, it's a bit too late to onboard before this release
        * If we have time then happy to have new people working on tests
    * Hudson: We might need a second hardfork after Constantinople for ProgPoW anyway
    * Dimitry: Do we want more changes in one fork or less changes in many hardforks?
    * Piper: I'd prefer to stay on schedule rather than to increase scope and push out timelines since we can always do subsequent hardforks later, I don't see a reason to fasttrack something into this hardfork
    * Peter: With Constantinople we wanted to do this at the beginning of the year, now it's th end of the year
        * It's fine to postpone certain changes but then realistically they might not happen for a year
        * We can drop features but anything we drop will probably not get included for a long time
    * Greg: At some point you have to ship, so you have to prioritize
    * Piper: Rather than discussing how long things might take, I'd rather discuss improving our process to make the timeline shorter for later hardforks
    * Greg: Almost all of our teams operate on CI so we're always ready to ship
        * we have a lot of independent features, but we insist on acting like a big corporation, rolling out releases with a ton of features all at once, which gets delayed when we can't get all features to work at the same time
        * We are afraid of hard forks
    * Martin: Problem with hardforks is not only implementation
        * It's difficult to reach agreement about when an EIP is finalized
        * Continued discussion on it, should we modify it?, etc.
        * Confusion about specifications
        * This is the big time sink
    * Jacek: Would it help to fix a time for the next hard fork now?
    * Martin: At the last Devcon we decided to do hard forks every ~8 mos.
        * There was general consensus but it didn't really work out
    * Nick: We should be scheduling them, putting in whatever's ready
        * Rather than scheduling them around features
    * Hudson: So we can drop a few EIPs and schedule them for the following hard fork
        * The EIPs that are e.g. hard to do testing for like 1218
    * Piper: If we push the blockhash and skinny CREATE2 (as they might delay Constantinople), is it realistic to get Constantinople out on the original timeline?
        * EIP-145 Bitwise shifting, 1052 EXTCODEHASH, 1283 net gas metering (without dirty maps) would remain
    * Dimitry
        * Yoichi wrote test for bitwise shifting
        * Review rodemap, maybe add more tests for this
    * Hudson: Others can help with adding test cases
    * Dimitry: Just writing idea of what test case needs to do would be helpful, I or Jared can write the actual test
    * Hudson: Can we get testing done for these three EIPs in the next month, to leave a month of testing before Devcon?
        * Dimitry: I already started writing tests for CREATE2
        * Hudson: so the only one we'd delay is EIP-1218 blockhash refactoring
        * ProgPoW wouldn't make it into Constantinople either
        * But then instead of an eight month timeline we could do six months to the next one
    * Piper: I'd prefer to stick to the eight month timeline
        * Other EIPs will show up that will be added to that
    * Any other opinions on six vs. eight months?
        * Danny: let's discuss in context of delaying the difficulty bomb
        * add 50% buffer time, so we'd need to fork within 12 mos.
        * Piper, Martin agree
    * Peter: I'd oppose six month timeline because if fork frequency too high, it puts huge pressure on geth and parity teams
        * In addition to forks, we have to maintain the network
        * Takes a ton of effort to maintain current network, do minor tweaks
        * You don't want to put even more strain on the teams
        * So I prefer eight months
    * Zsolt: What does this mean for 1218?
        * Hudson: It would be eight months later
    * Constantinople progress link describes which EIPs are going in (https://github.com/ethereum/pm/issues/53)
        * Other than issuance reduction, difficulty bomb delay

# Issuance reduction
* Hudson: last meeting we decided on an issuance reduction but there are several proposals on the table
    * EIP-1295 a bit more complex, not a reduction but changes incentive structure
* Intros to guests
    * Andrea: EthMiner developer, EIP1218 interesting from miner PoV, we should discuss economic implications
        * given conditions of market, I don't think a reduction of the reward would help
    * Brian Venturo - CEO, Atlantic Crypto, large GPU mining org in US
        * Representing mining community and sophisticated investor community
        * support EIP-1295, this is our EIP
    * Carl Larson
        * Started /r/ethtrader
        * Web developer
        * Authored EIP-858 in January: look at environmental impact that mining has
    * Eric Conner
        * Supporting EIP-1234
        * Representing investor community
        * I think the network is overpaying for security
        * https://medium.com/@eric.conner/a-case-for-ethereum-block-reward-reduction-in-constantinople-eip-1234-25732431fc77
    * Matthew Light
        * Did original EIP for reduction from 5ETH to 3ETH
        * In support of additional reduction
        * From 3 to 2 feels like the most prudent response (EIP-1234 by Afri)
    * Alex Thorn
        * we aren't ready to take a firm stand on these EIPs, but in general we favor EIP 1295.
    * Tim Coulter
        * Founder of Truffle
        * Represent small to medium miners
        * Now I have about a dozen machines, ~ 100 GPUs
        * Also have a bitmain miner, bought as an experiment, so I have firsthand experience with it
        * I'm in favor of a reduction, don't have a preference which one
        * I'll most likely continue mining either way
        * Depending on price fluctuation I might decide to buy at market instead of spending the money on electicity
        * Most of our electricity in WA state comes from renewable energy
    * Xin Xu (CEO, Sparkpool)
        * One of the largest mining pools
        * Support more than 20% of the hash rate
        * Around 300k rigs connected to our pool every day
        * Sparkpool originally from EthFans, one of the largest Ethereum fan communities
        * Business started as a side project
        * I support delay of ice age difficulty bomb
        * We prefer EIP-1295 if I have to choose one of the three
    * Peter, Ethermine, ~30% hashpower
        * [Copy quote]
        * Prefer a PoW change
    * Jean M. Cyr, Ethminer dev
        * Neither a holder nor a miner, purely interested in tech and development
        * My motivation is not financial
        * Favor 1295, slight reduction on uncles, leave the rest as-is
        * Long-term viability of ETH is predicated on the success of scaling, that's the bottom line, the only thing that will decouple ETH from BTC
    * EIP-1295 (Brian)
        * 11.4% issuance reduction
        * Addresses this by fixing incentive misalignment: they are currently incentivized to maximize uncle rate
        * The higher the uncle rate, the higher overall issuance
        * Currently 14% (?) of all issuance goes to ancillary rewards
        * This EIP adjusts in favor of decentralized mining
        * Increasing work package sent to miners increases the uncle rate
        * Reduce uncle rewards by 75%, and only first two levels
        * We shouldn't be rewarding sub par infrastructure
        * Sub 6% inflation by 2019
        * Minimize security risks to network going forward
        * We suggest adopting EIP-1295 now, in line with Casper FFG EIP proposal, close to issuance schedule there for year one
        * Provides natural issuance reduction, with reduced uncle rate we can get it down to 5-10%, pre-Metropolis
        * Other steps: commit to change in PoW, target Q1 2019 rollout
        * After this is done, we believe the community needs to come together to commit to a monetary policy with a set roadmap for issuance reduction
        * We'd like to delay not defuse the difficulty bomb
    * EIP-858 (Marius)
        * Made a PR to also include delay of difficulty bomb to 12 mos
        * To reduce block reward to 1 ETH per block
        * Use lower issuance to reduce environmental costs for mining
    * EIP-1234
        * Delay difficulty bomb 2 M blocks so ~ 1.5 years
        * Reduce issuance to 2 ETH
        * Keep current PoW as stable as possible
    * Danny: Having a long term monetary policy is really hard until we've transitioned to PoS
        * It radically changes what we pay validators compared to miners
        * So these are stopgap fixes to keep the network secure, keep people happy until we get to that point
        * So we can't talk about longterm monetary policy yet, until we're talking about PoS and sharding
        * considering hash-rate is similar to when this was written, a lot of these numbers are still ball park relevant — https://gist.github.com/djrtwo/bc864c0d0a275170183803814b207b9a
    * Brian: We believe there should be a hard cap of issuance before PoS transition
    * Xin: https://www.crypto51.app/ , some background info about network security
    * Pawel: some EthMiner devs said they would prefer a hard cap on supply vs. manipulating the block reward
    * Nick: There's a paper on instability of block rewards, it becomes costly [cost efficient?] for miners to mine alternate chains, same will apply to Ethereum, research shows we can't reduce block reward below a certain level and expect current incentives to hold
        * http://randomwalker.info/publications/mining_CCS.pdf
    * Brian: Reduction in emissions going from 3 -> 1 ETH is around zero
        * Incentives to build new hardware may not exist but not there now either
        * 4.2M tons per year current emission rate
        * Can be powered by one combined cycle NG plant in the USA
        * Environmental impacts of network today are minimal
    * Carl
        * By my calculation Ethereum is 65% of GPU mining
        * Market cap of ETH dwarfs market cap of other GPU minable coins
        * I'd expect some mining to drop off totally, reduce total mining supply
        * Electrical consumption attributable to that mining would also go away
        * I don't buy that renewable energy is always used to power miners
        * Even if it were the case, the miners are consuming power that could be used for other things, which are now probably burning fossil fuels
    * Nick: Let's not argue about where the energy is coming from, let's focus on the protocol
        * If we can reduce miner incentive without affecting security we should do so
        * If we can't, we can't
        * Regardless of whether or not it's good energy-wise
    * Eric
        * Used BTC as benchmark, level set market caps
        * Looked at what ETH is paying out in mining rewards
        * It's currently paying 2.5x
        * If we drop it down from 3 to 2, it comes more into line
        * This is my argument for EIP-1234
    * Danny: 2ETH seems like a reasonable compromise to me
        * Also a commitment to do ProgPoW in 8 months seems like a reasonable compromise
    * Brian
        * Community wants PoW algo to shift to something less ASIC friendly
        * Reducing from 3 to 2 ETH will force GPU miners off the network
        * Only thing left behind would be ASICs
        * EIP-1295 was drafted with that in mind: keep top line incentives in place, continue allowing that composition to exist as it does
        * I'm all for an issuance reduction when we understand what ASIC participation was as part of idea behind monetary policy roadmap
        * But without putting security at risk, reducing to 2 is probably the wrong move
        * Network would be incentivized to have highest uncle rate possible without this change
    * Carl: Do people have data on A10 ASIC? Claims 2x improved efficiency
    * Tim: No data on A10, I have an E3
        * My GPU rigs are all 8 GPUs each
        * Rough cost for a total machine is ~$2500
        * Price for E3 was $800 in first round, around $2000 now
        * Efficiency after tweaking GPU rigs to work as they should, is about the same, esp. if you get GPUs you can overclock
        * So hash rate is about the same
        * What E3 has over GPU rig is that GPU rig has 47 moving parts, so management of that hardware is much harder than just plugging in the E3 machine
        * Don't believe you'll shut out GPU miners, major difference is management headache
    * Brian
        * Top of the line model will do 453 MH at 850 watts [?], 3x [?] as efficient as current GPU rigs
        * We have ~3000 GPU rigs
        * Our hardware has many alternative use cases going forward in the "AI economy": machine learning, AI
        * Those use cases are just beginning to show up
        * ASICs are not usable for other things
    * Xin
        * Environmental angle:
            * Environmental angle: I don't believe cutting out some type of miners would improve the environmental impact
            * Chinese miners are using non-renewable energy but it's energy that would be produced anyway, i.e., using wasted energy
        * Network security:
            * https://www.crypto51.app/ , some background info about network security
            * Cost of 51% attack
            * It's not so expensive for Ethereum, but there haven't been any attacks, why?
            * No hash rate available in market that you can use to attack Ethereum
            * Network has been safe up to now, not because attacks are too expensive, but rather because all available hash power is mining the network
            * No one has extra hash rate to attack the network
            * And if some miners leave, then that hash rate may be available for hire to attack the network
    * Carl
        * Not desirable to continue to grow the hash rate
        * We want to be discouraging investment in new equipment
        * Lowering block reward accomplishes this
    * Jean
        * I don't understand the rationale for building ASIC or GPU mining rigs at this point
        * For E3 it would take roughly 2 years to pay for itself unless something extraordinary happens to the valuation
    * Tim: all the numbers are completely speculative, tied to the price
    * Jean: even at 5x the price it's still hard to make an argument for it
    * Xin
        * Siacoin posted study, comprehensive article about why ASIC miners exist, how manufacturers make money
        * ASIC manufacturers not responsible to miner post-sale
        * All profit and cost will be paid off
        * Collect all profits before ASICs start mining
        * So they are incentivized to manufacture
        * Future of mining doesn't affect them
    * Matthew
        * We did a reduction from 5ETH to 3ETH, most people agree that reduced issuance had no negative effect, paying less for security
        * Moderate reduction from 3 to 2 would have a similar impact, we'd reduce $bn per year we're paying for PoW mining which is not where Ethereum wants to be anyway
        * In mid-2017 Vitalik said likelihood was that we'd have PoS by end of 2017, now roadmap says 2019
        * Getting issuance down to level comparable to other chains will have good effects for price, good for developers and projects
        * At margin will reduce incentive to buy more mining equipment
        * We're currently way overpaying the miners, 7.5% per year of Eth market cap is being paid to miners
        * Bitcoin is paying a lot less
        * In a bear market like now, a lot of that from miners is going straight to the exchanges and getting dumped which has a negative effect on everyone's ability to keep working in this space
    * Hudson: miners have expressed their desire to change PoW, would moving from Ethash to something like ProgPoW be a good idea?
        * Brian: in favor of issuance reduction with change to PoW algorithm, caveat is that 1295 is a great stopgap before PoW change happens, we don't understand extent of ASIC participation at the moment, 1295 today, PoW change at later date with incremental reduction in block reward
        * Xin: in favor of anti-ASIC for sure, this conversation is nice but we cannot use simple math to calculate network security. There is a tipping point beyond which everything breaks instantly.
            * Issuance reduction will have a big impact on security
            * Impossible to simply calculate what will happen in the future
            * Carl: we can look historically
    * Jason: In 2017 there weren't many ASICs so reducing issuance reward was an even playing field for all, whereas now only the most profitable miners would survive
    * Carl: but at the moment no one has demonstrated that ASICs have a signifcant running cost improvement over GPUs
        * https://docs.google.com/spreadsheets/d/e/2PACX-1vS2upHFNeRF1zRpQzve00Da6HtuQz9co06eoxPU5DAxRtfxlmW1qqNuFQvIhHF7wBwZrQruti7tlqUk/pubchart?oid=874847247&format=interactive
    * Jason: they're on par with the top of the line GPU rigs but significantly more efficient than older rigs, 1 year+ older
    * Jean: real issue with Eth is memory bandwidth
        * ProgPoW reduces DAG size, tries to exploit more of circuitry that exists on current GPUs
        * Dev cycle for ASICs is ~3 mos, that's not a very long time, I don't think it would take them much time to catch up with that
        * I'm concerned about the introduction of a new algorithm
        * ProgPoW (https://github.com/ifdefelse/ProgPOW) is unoptimized
        * So we'd be in an arms race with the miners
        * I'm in favor of open source so I prefer leaving things as they are
    * Nick
        * I'm also skeptical of ProgPoW
        * List of randomly selected operations, many are simple bitwise operations which don't require many gates, shifts require no gates
        * Only some require gates
        * Jean: I agree
    * Peter
        * Miners benchmark GPUs and pick ones with highest memory bandwidth, highest hashrate
        * Some GPUs that were optimal before may have high mem bandwidth but crappy computation
        * Seems a bit naive to think that moving from Ethash to ProgPoW would keep all GPU miners happy, need to investigate this more
    * Marius
        * We should wait for benchmarks on some emerging hardware
    * Hudson: Does anyone think there is an optimal way to determine sentiment and make a decision?
        * Would any of the miners here leave if we did an issuance reduction?
        * Brian: at 1 ETH, we're probably not economic
        * At 2 ETH, we'll explore every other use case that we can
        * And this depends on the price of ether
    * Andrea
        * Is PoS coming?
        * If we let ASICs enter freely in security of the network and let small miners leave due to decreased efficiency, we will have a network in the hands of the ASICs
        * Not a problem per se, but it will be very difficult to change PoW algorithm later, because if you do that, all the ASICs will be unavailable for a quick change
        * So you might end with a very insecure network
    * Eric
        * We're at 7.5% inflation
        * Consensus was that we'd cap it at around 100M, we are already past this
    * Xin
        * I don't think ASICs are a major issue for security but issuance reduction could be
        * Top five pools have around 75% of hashrate
        * Once issuance changes, they won't still have that much power. Miners will leave the pool to do something else. Anyone with anough capital would have the money to purchase them and attack the network.
        * This function is not linear
    * Marius
        * Maybe we should just wait and evaluate how ProgPoW works
        * Look into it more, come back and decide
    * Peter
        * We kind of need to make a decision for Constantinople hardfork
    * Martin: I propose that we should have more technical meetings every two weeks, and higher level talks on the off weeks
        * Work out quirks that we don't really have time to talk about on these calls
        * Dig into EIPs, read them again, talk about it again next Friday and make the call then
    * Hudson: We'll do another meeting next Friday
        * More community content on reddit, twitter, FEM forum about the EIPs and these perspectives

# Attendees
* Hudson Jameson (EF)
* Lane Rettig (Ewasm)
* Andrea Lanfranchi
* Greg
* Brian Venturo
* Piper Merriam
* Fredrik Harryson
* Zsolt Felfoldi
* Matt Halpern
* Dmitrii (Harmony)
* Nick Johnson
* Jason Carver
* Jean M. Cyr
* Antoine
* Peter
* Martin Holst Swende
* Eric Conner
* Xin Xu
* Tim Coulter
* Danny Ryan
* Carl Larson (/r/ethtrader subreddit moderator, EIP-858 author)
* Marius Van Der Wijden
* Jacek Sieka
* Alex Beregszaszi
* Afri
* Pawel
* Igor Barinov (PoA/Mana client)
* hacktar
* Bob Summerwill
* Jason Temple (observer)
* Alex van de Sande
