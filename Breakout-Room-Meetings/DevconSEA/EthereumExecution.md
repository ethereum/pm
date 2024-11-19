# [CLS] Ethereum Magicians Infinite Endgames: Ethereum Execution

## [Ethereum Magicians Infinite Endgames Sessions 2](https://app.devcon.org/schedule/S8NCDC)

## Summary: 
A fishbowl-style discussion with core Ethereum contributors and community to publicly discuss the "endgame" of execution on Ethereum. We will discuss what the evolution of Ethereum’s execution layer will look like, L1 vs. L2, settlement vs. execution, enshrined rollups, consensus changes vs. client performance improvements, etc.

## Video: https://www.youtube.com/watch?v=63w7kHh737w

## Panelists: 
lightclient, Alexi (Reth), Dan (EOF), Guillaume (Geth and stateless consensus), Jared (Geth), x

## Devcon SEA - Nov 15, 2024

lightclient: What is the endgame for execution in Ethereum? We often think incrementally fork to fork, but what could the world look like?

Alexi: Lower block time; higher gas limits; optimized EVM where you can pack more into one transaction/block; higher performance of nodes themselves; stateless of lightnodes; anonymous state
For me, these are the most important questions and there are a lot of things that L2s can do with experimentation on the EVM, but with L1 these are my top.

Dan: I tend to take user perspective; who is using computer environment? In the future, I see standardization and specialization depending on the ream fo the chain your settling on.

lightclient: My own answer is slightly less developer or user-centric. We want these as well, but when I think about end game I think of Vitalik's vision of how people should consume the chain. Every 12 sec you receive a small proof, verify the proof, and use that to confirm the chain. Simplify the process of creating a trustless connection with the chain. Many questions down the path, but the core is that you can efficiently verify that you are head of the chain. We want people to be able to fully validate the chain, which currently requires high amounts of storage and hardware capability. Would like to see more zkEVM development and how we can make the huge leap to zkEVM and stateless.

Guillaume: The promise has always been the world computer, and I want that. Siloing between L2s but I want to be able to call contracts at the execution layer across L2s. Need integrated interoperability and diverse execution environments.

lightclient: Do you have thoughts on what needs to happen on L1 in next 5-10 years to get toward zkEVM / what type of things need to be done to move us toward that path?

Guillaume: Proving technology will be probably so efficient that nothing will need to change. We could imagine a future in which everyone is able to prove things on their own machines; rollups enshrined into shards; what needs to happen? a lot more research, a lot more discovery. Need pace of zk to keep churning ideas. 

Dan: Need to increase ways to isolate and execute transactions

lightclient: We are talked about native shards, isolation of execution, but I wanted to ask-- is zkEVM the right path?

Guillaume: It makes no sense *not* to zk the EVM. We need privacy and will need something to replace zcash. Privacy will be a big topic in the coming years and cannot *not* do zk. It is the necessary step we need.

lightclient: Do you feel it is necessary to do that on the L1?

Guillaume: I believe that rollups are basically shards on trial periods; it will need to happen on L1 bc it will create a division between L1s and L2s, resulting in L1s being the least private. 

When we say zk, what we are really looking at is starks/snarks.

Jared: Does the EVM currently lend itself to be able to be efficiently metered from the perspective of a prover being able to see a block and know the cost of proving certain code?

EVM max - proposal to bring more modular arthmetic to base layer; if we can express precompiles more efficiently on the base layer so we can see from prover perspective what is actually being done, that would lend itself to zkevm

Dan: Getting rid of gas introspection > changing gas schedule > gas metering is important
//so fast; watch recording 

Guillaume: In a snark future, do we need gas metering?

lightclient: If someone is going to create the proof for you, yes, but not if you're creating the proof.

x: In future we will see greater split of builders and verifiers

lightclient: I think we mostly agree, we want succinct verification and privacy on L1; of course tech is advancing rapidly and we'll have to see where the tech is in 5-10 years.

Jumping back to native sharding, maybe you could pitch it to the community?

Guillaume: There was always this plan. The biggest problem with rollups is that they can disappear so long as they are backed by only one company. The reason we want to create the space for people to experiment, but at the same time we need to make things (infrastructure) official for the communtiy to take over and maintain it.

Dan: Huge risk

lightclient: Native sharding doesn't feel like a critical path when we think about *end game*; I don't see an innate reason fro shards native to the protocol, especially if we move to zk.

x: I feel we should leave things to the rollups to do their own things, but I don't want to force a specific way to do things. Solution improvements will happen on their own.

Alexi: I agree, if we believe rollups will evolve at the rate of ethereum, then that's fine, but they can go faster.
Some form of a rollup can be a trend.

Guillaume: What I'm worried about with a rollup becoming enshrined is the worst case scenario. I want everything to be great but life is not always perfect and I'm worried about how things degrade when they don't work. Need the communtiy to take things over rather than trusting that everything will be fine.

Alexi: Users won't agree that we should have worse UX for higher security assumptions; people today use Optimism and Arb bc they care less about having censorship resistance, etc.

Guillaume: Ultimately this is a philosophical debate; yes most users are hoping to get rich, but we have a responsibility to make the Ethereum experience better than any bank; want to give guarantees but those folks should use banks

Alexi: I disagree, we should do better than web2 and traditional banks. Better UX, better performance, etc without having to jeopardize our values.

lightclient: We want to make sure that Ethereum is going to be around and correct with good UX for a long time. The way we pivoted to doing this is the rollup centric roadmap. What do you need to see / hear to think that the rollup model is not the right path?

Alexi: Ethereum L1 is not just for rollups. Some say we shouldn't focus on improving L1 bc it's good enough for roll ups. I would argue we need good experience for defi on L1 so it's not fully rollup centric. Need censorship resistance and good performance for Defi users.

Jared: Making L1 better and more expressive is directly beneficial for rollups.

lightclient: To reframe the question, what are the metrics we need to see to know that the rollup-centric roadmap was successful / the right path?

Dan: 1. How many roll ups leave the ecosystem? gained escape velocity and can stand on their own or aren't getting support 2. How are rollups differentiatign themselves and what impact does that have on the ecosystem as a whole? Trying to judge success or failure of rollups is difficult; these companies/teams would be doing this without L1s blessings-- the real question is the relationship of L1 teams and L2s and what we provide for each other / how we support each other.

Jared: Measurement of success if use cases that aren't financial or gimmicks. EVOnline as an example.

Dan: Need to judge use cases by use value on chain. 

Eric: To bring the discussion back to native / enshrined roll ups, are there lessons we can learn from other ecosystems that have gone down this path? i.e. Tezos?

Dan: Seen Cosmos and Adam2.0 comparisons

lightclient: In Cosmos, there are some similarities in terms of cross-chain APIs. But thinking about native execution for Ethereum and enshrined exeuction environments; homogeneous sharding; doing this creates a coordination problem that has been sort of solved by the rollup-centric roadmap. maybe heterogenous sharding is possible on L1 but too far away.

What becomes possible if the L1 does this versus a smart contract? There's possibility with cross-chain interoperability that doesn't necessarily have to be within the L1 execution environment.

Dan: Personally excited about multiparty proposers and building multiparty systems rather than creating hard sharding lanes; how can we facilitate more organic sharding to occur.

lightclient: What types of things would you like to see happen on L1? 

Dan: When it comes to storage slots, we need better ways to handle slot collisions. Whatever we can do to reduce collisions increases the possibility of combined proposals. Future of communal proposal and one person combines to make sure all are compatible.

Audience1: Diversity of L2s is great, but we are already seeing fragmentation; EVM is standard which is reliable. If it starts changing, it gets harder to build and we lose cohesion.

Guillaume: // see recording [12:20 pm]

Alexi: Agree, we should work on better tooling for interoperability across L2s but also across L1 and L2s.

x: It is inevitable for the L2s to iterate and evolve, but it's important for us to make it possible for them to change as they need to.

lightclient: You guys want to talk about the beam change? 
Audience question: How does bean proposal play into these ideal futures? Is beam the right way forward?

Guillaume: I am currently helping beam chain project on feasibility. It's actually an interesting idea. The intent is good and the spec is still developing; it looks ambitious and promising; we will get a much more palatable and simpler version of beam chain.

Alexi: pls tldr on beam chain

Guillaume: Currently, nothing. It is just an idea. In the next 6-months hopefully it will be a fully spec. It's about doing a merge again / replacing the consensus layer, redesign everything with inclusion lists, make everything quantum secure, a fresh start. Get rid of Beacon Chain and replace with everything we learned from Beacon.

lightclient: Would you say the Merge was a research project?

Guillaume: Yes, and we should keep improving.

Dan: Do you think there will continue to be revisions?

Guillaume: Of course there will be another revision. Continual improvement is really a governance question and a decentralized governance problem. As an ecosystem we've gotten more conservative, need a big change, and Beam has the potential to be a significant change.

Alexi: ZK is a big part of the beam change and increased dependency on EL to have zk. The Beam change is about ZK. Also single slot and faster finality

Guillaume: zk has so much innovation right now that it's too early to jump
- faster finality would be nice to have, this is a great usability change
- francesco (EF) doing lots of work on this

Alexi: Question about wallet transactions and censorship resistance; beam chain does not currently have censorship resistance in the proposal.

Guillaume: This is exactly what happened with eth2.0; concern about complications caused delays 

lightclient: This is probably my number 1 concern. There are two classes of big projects: things we know how to do but are difficult given the legacy environment and things we don't know how to do yet. Beam chain contains both of these. There are things we *can* change but are very difficult to do while the airplane is in the air. Need full confidence before we can ship.

x: Move discussion more to execution-- 1, 2. how to improve execution for evm 3. state proofs 4. the state
For end game there are two paths we should think about: UX and performance (how many transactions we can execute). 

Jared: I agree, we need to find these targeted changes that will have broad impacts, i.e. figure out how to extend proliferation of precompiles.
If we look at explosion of complexity on cryptographic side, it's a nightmare to try to coalesce around new precompiles. We need to find a way to allow users to implement contracts with close to precompiles cost.

x: How many new cryptographic primitives do we need inside the evm? 

Audience question: What self-contained change to EL unlocks the path and optionality to a large set of 'other' changes?

Alexi: EOF allows you to have custom byte code and it would be amazing if we could ship EOF. 

Guillaume: We need to be prepared for future contracts in multiple languages.

Also, I want statelessness. This has the potential to be really changing, a whole new Ethereum.

Dan: Account versioning could also unlock optionality. The key to optionality is having places and hooks that say 'I'm doing something different' and directs to rollups for doing specific functions.

lightclient: One thing we talk about in the EL is backwards compatibility; what would you need to see to de-enshrine the current execution environment? is this what we should continue to carry on?

Jared: If we can take a parallel to when we tried to remove self-destruct and broke a bunch of contracts, the transpolation of EOF to EVM is similar and to do it properly we have to force upgrades in specific time frame.

lightclient: I feel like there's a bit of a spectrum here, not just one day shutting off EVM. We could have new environemnt with much more performance and keep legacy world that only communicates once an epoch and has limited functionality.

x: This depends on when analysis starts and we see the numbers.

Guillaume: When we had this debate around verkle and EOF, the argument is that if we can compile at the same time as legacy and eof. 

Dan: Because of the some of things we're banning, we can't. A more realistic plan is that we won't be able to ban all old legacy opcodes

x: It's not just transition from legacy to EOF, it's a different logic. Some of these things we want removed by design.

lightclient: At a higher level, we have a social contract to ensure the environment keeps running. Is that a contract that's breakable?

x: It depends on the costs and to figure out the costs, we need analysis.

Dan: Whoever designs breaking the contract, they need to be willing to be a pariah.

Guillaume: There should be a guiding principle for not touching the state, if it's working, then we shouldn't touch it.

Dan: Maybe there's a legacy state layer 1 roll up that transacts once an hour.

Audience: How do you incentivize node operators to propogate transactions?

lightclient: As we change the behavior of the transaction pool, we need to be cognizant that node operators are altruistic. 

Guillaume: There is something called rainbow staking people are looking into; you could force and reward people to pick transactions at random

Audience: I want to see unstoppable transaction in the future.

Call for closing comments.
Final thought: execution need to be about improving UX and the usage of Ethereum. 
