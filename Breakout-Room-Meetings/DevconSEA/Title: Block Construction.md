# Block Construction
Ethereum Magicians Infinite Endgames Sessions 3
Summary: Once again, Devcon will host Ethereum Magicians gatherings for the community to come together and discuss the most important topics in Ethereum’s roadmap. Join us here to discuss the “infinite endgame” for block construction. We'll cover PBS, MEV, role of validators vs. builders, centralization risks, and more!
Video: https://www.youtube.com/watch?v=Ycf0Vwz7aFE
Panelists: Alex Stokes
Devcon SEA - Nov 15, 2024

Purpose of this session is to have a conversation with people here in this room about block construction. I can tell you about the state of things with mev-boost, PBS, etc. and we can go from there.

Has everyone here heard from mev-boost? 
Start from the beginning -- Ethereum is cool because it lets you send transactions on decentralized applications. It turns out you can craft the blocks of Ethereum in a certain way, and in doing so a builder can maximize revenue or profit.

This poses a concern for the protocol because if you're better at mev than someone else, then you now have a fly wheel where you can reinvest in your operations and you get bigger and bigger. A risk here is that this could look like better returns to validators, but all the stake ends up with you and is no longer decentralized.

This is bad. The way we generally think about this in terms of protocol research is with PBS--proposer-builder separation. It separates off the building role with these valuable execution payloads from the validators. Imagine a light layer of validators attesting to the validity of the network but then you entirely file off the concerns of mev.

Even if you do end up in a centralized builder or block leader world, professionalized and operationalized "transaction supply chain", with PBS we could still have a very robust validator set that could still attest to the truth of the chain.

For PBS there's a question of implementation
- could do on-chain v. off-chain
    - on-chain would require a protocol change and consensus
    - still big open questions about best way to do PBS on-chain
- we can do PBS off-chain in the meantime, best option to do so is mev-boost

mev-boost provides a rendevous service between builders and proposers
- as validators go to validate the chain, they have the opportunity every so often to propose a block, building a consensus block and execution payload
- where pbs comes in is in carving off the execution payload where all the juicy mev is and handing it off to someone else
- mev-boost is a protocol and software stack that implements this

a high-level way to think about mev-boost today is that it is a commit-reveal protocol
- commit to something and once committed, then builder is free to release block
- protects builders from proposer taking their work and network rewards, resulting in an unsound network
- need a way for the proposer to commit to the block with a blinded payload; proposer signs over block in a compatible way with thing that ends up on chain, show builders proof that they've committed and then builder releases. 
- without this commit-reveal step built into the protocol, then builders are not protected and the validator set is not protected from threats of centralization

This has been live since the Merge and it's grown more complicated with new parties added to the transaction supply chain (solvers, bundlers with 4337)
What it looks like currently: 
validators talk to different relays > relays interact with builders > relay acts as trusted broker between proposers and builders 
- relays cause additional issues: single point of failure, potential censorship, bugs, etc.

mev-boost dash
- over 90% of blocks going through the system; it's cool and works, people like it and use it <3
- 12 relays and 31 builders registered and observed, which is good for decentralization

downsides:
- censorship quickly entered the chat; directly harms Ethereum and counters its values; need to think about ways to improve it
- security concern if relays cannot facilitate the exchange and we miss a slot (bugs, accidents, malicious attacks, e.g. "low carb crusader" attack: https://x.com/samczsun/status/1642848556590723075)
- relay sustainability and monopoloies: it's a competitive market and three relays pretty much dominate the market: https://mevboost.pics > relays
- builder monopolies: primarily just two builders (even if they're aligned, it's not great because of potential for unaligned actors to jump in) https://mevboost.pics > builders

Given all of this, you may be wondering why we did this because it sounds bad. It's not great, but now the question is: what can we do via the protocol that would remove some of these trust assumptions? Can we add protocol features that could play into this, e.g. inclusion lists that may fix the censorship problems?

The rabbit hole goes deep: design differences and concerns touching all parts of the protocol from fork choice to block production to the incentives around block construction and attestations. 

One way to start: eliminate relay and replace relay function with protocol.
- enshrine relay responsibilities into the protocol
- improve trust assumptions by removing relays

ePBS - v4 of optimistic roadmap
ePBS-PTC [[EIP7732](https://eips.ethereum.org/EIPS/eip-7732)]
Proposal to implement "payload-timeliness committee" design
- needs trustless builder payments otherwise the proposer could steal builders work
- protocol works in a way where you have this money locked up and it can be used to pay out regardless of what builder or proposer does/doesn't do
- interesting part of the design is that builders <> proposers directly talk to each other; more assurances in the protocol
- number of things relays can still do: providing low-latency as a service, additional features e.g. cancellation
-- still an open question to how this will solve current issues with relays

Open to audience for questions, concerns, contributions

Q: Removing relayers, each validator will have to discover and manage the builders they connect to, won't this cause "just connect the two biggest ones and forget about it" attitude, entrenching them?
- to add context, this question is thinking about the latest ePBS design 7732, and the idea is that the benefit is you don't need the relays and proposer and connect to builder
- primary issue: privacy and security concerns, builders have IP of validators and can manipulate  
- This other thing this question is asking re: entrenchment-- this is a valid point. It's hard for new relays to get adoptions by validators. Validators may just continue using relays they know / are familiar with.

Q: In early discussion of Max-EB, it was said that collapsing the validator set was a prerequisite for ePBS (and SSF) is that still considered to be the case?
- Not sure about ePBS but definitely for SSF 
- single-slot finality: once enough validators have voted on block in the chain, protocol design allows many validatorsa to come to the table for consensys, at odds with quick finality > ssf is a research direction that asks if we can have finality in a single slot
- max-EB ([EIP-7251](https://eips.ethereum.org/EIPS/eip-7251) coming in Pectra) allows a validator to be represented with much higher stake; changes against how today in the protocol where every validator looks the same with a fixed stake; makes it easier to reason about, but artificially inflates the validator set and is at odds with SSF
- better representation in protocol: single entity validators with higher stake be represented as 1 (e.g. if a single entity staked 64 ETH it should show as 1 validator, not 2)
- validator consolidation: fewer validators in the protocol makes SSF easier

Q: What happens internally within relays? Do they just relay the best block?
- Relays do a lot and keep doing more over time. Simply: they are running an auction between builders and proposers. - Builders build blocks and need to be watching the chain to anticipate future blocks and try to maximize their profits. > Builder makes block out of revenue they happen to find and make payment in a particular way that pays the proposers some amount; that amount is essentially their bid in the auction > Submits to relay; relayers receive and do a bunch of stuff:
1. validate the block locally with respect to the protocol
2. extract what looks to the proposer as a bid (contains metadata as block)
    q: how will the builder know the address of the proposer?
    a: when you launch your node, you tell your CL and EL to run mev-boost; you tell your consensus client to use this external network and it sends registration messages to relays you configure to mev-boost that includes proposer payment address.
3. proposer accepts bid
4. as proposer prepares slot, they call all the relays they've configured and picks the highest bid 
5. play commit-reveal game
6. once proposer has signed message, they send that to relay which validates the signature and the block can be validated
7. everybody gossips everything

In the last year, we've seen more optimization. There is a very sophisticated supply chain of actors. Every millisecond is valuable and actors need to be able to react quickly; entire process has become latency optimized.
- top relayers do aggressive latency optimizations e.g. builders and relays co-locating, which isn't great for vertical integration
- concern of competition and commercialization; initially we assumed relays would be public goods and providing this service
- relay sustainability is strained
- timing games concern - you have up until a 4 second deadline and proposers can be more or less aggressive with how much time they take up to try to maximize value.
 Reference Note: See research article "Time is Money: Strategic Timing Games in Proof-of-Stake Protocols" https://arxiv.org/abs/2305.09032

Q: Some builders have their own searches or something like non-public agreement between them. What's the additional value that comes from that 'agreement'?
- this is a question about "exclusive order flow"
- the ideal is that these are all independent entities in competition with open APIs and there's a level playing field; but what we see is that people maximize profit by creating exclusive agreements
- there are ways we could think about removing the desire for these backroom deals through mechanism designs, cryptography, etc.

Q: What about moving from English (or 'first-priced open') auction to first-price sealed auction? What's the history behind the auction?
- There are multiple auction theories and mechanisms with different ways to process the bids
- Consider in a scenario where Builder A bids 3x and builder B bids 2x, but Builder A does not bid, then 2x would win as the second highest bid. By setting the second bid as the floor/ceiling of the auction, then relay can rebate builder and retain reward in relay-builder system. No revenue in relay to some revenue 

Q: Regarding the first-priced sealed auction, what about when the proposer interacting with only one relay? Does it make sense to switch to first-priced sealed to increase rewards? In the English auction, the builders are looking at each others and can outbid.
If moving to first priced seals, we have to suppose there is only one relay because it doesn't make sense to have different auction times amongst relays. It is a good way to increase the winners curse; some market makers really want blocks and are willing to pay more than what they're actually paying at the moment.
- Making any small change like this has significant implications for how everyone shows up to this game and engages in bidding practices
- Key difference is whether bids are sealed or not
- Concern about general observability of the system; if everything is sealed we can't see what builders are bidding and how they're acting
- We currently have rich data APIs that enable everyone to look deeply into what is happening

Q: Do we know about network performance of ePBS?
- ePBS is somewhat agnostic; [EIP-7732](https://eips.ethereum.org/EIPS/eip-7732) is fairly agnostic to how bids are produced. 
- You could imagine a gossip layer, but it would cause bids to propogate more slowly and builders wouldn't use it and talk directly to validators

Q: Is there evidence of colocation?
- There may have been some research, but not sure of anything public. Hard to assess with public data. Both builders and relays have APIs exposed so you could theoretically ping and geolocate them.
- Relays want to be close to proposer. If relays is close, they can also delay things a bit more.
- Most relays have geodistribution baked in just to reduce latency to proposers and validators

Q: Do relays get paid for their tasks?
- Short answer is no. Most public thing we've seen is builder-rebate mechanism.
- Mostly reliant on altruistic actors providing as a public good
- PBS foundation is trying to help and provide tools for sustainability
- We can imagine that there builders are paying for special treatment, which only motivated ePBS and solutions through cryptography, code economics, and other tools within the protocol

Q: What are the trust assumptions between builders and searchers?
- Users making transcations rely on application or wallet > transaction goes into mempool > searchers then look at mempool and know very sophisticated strategies for mev extraction (e.g.sandwiching) > searchers with specialized mev strategies may not be builders, so they need to find a builder who would work with proposers via ePBS.
- lots of on-going research on builder<>searcher vertical integration; in an ideal world you can imagine them as separate, mutually distrustful entities
- concern about privacy and sensitive data
- in practice, there are many trust assumptions throughout the 'transaction supply chain'

Q: Thoughts on EIP-7732?
- There are other flavors of ePBS and there is ongoing and developing ideas for how this could look within the protocol. It's not settled that this is the 'right' or 'only' direction to go in.
- PTC has had the most work of formally specifying this design
- Re: inclusion on mainnet-- it gets us toward even more forward-looking designs (execution auctions, execution tickets)
- Adds a notion of pipelining to the protocol that makes things more resilient; decouples EL and CL blocks
- Not convinced it will get rid of relayers today, may lower barriers to entry and we may see new actors enter market but doesn't necessarily mean people will use new/different relays

Q: Any changes on how dapps / intent networks are sending transactions to builders? Is everything still going through mempool or going directly to builders?
- 4337 introduced notion of bundlers so whole pipeline is not just for transactions but also for user ops
- lately we've seen the rise of intents and solvers and other ways to think about state transitions on chain
- seen a rise in private order flow (txts that never touch the public mempool); not great for censorship resistance

f/u: How do solvers on intent networks create blocks; where do those intents go?
- it depends. today, everything would go directly to builders. otherwise it would just be gossiped in the public mempool

Potus: What are you thoughts on things that are off-protocol and not envisioned to be on protocol, e.g. preconfirmations? We run the risk of being too late.
- Not sure we'll ever be too late, but it is a legitimate concern that off-chain systems become so entrenched that as a community we can't change the protocol in a way that matters.
- Mixed feelings about preconfirmations because most designs are just copying builder-relayer-proposer dynamic; run into the problem of centralization 
- Claim is that we will do progressive decentralization over time so we will need to just keep an eye on it

Q: Compared to how transactions were structured over a year ago wherein proposer payments were usually last transaction of the block, but we've seen a change in pattern. Do you know why they do this and if it's why Titan Builder is so successful? Do we have alternative structures?
- One reason for changing payment options to proposers is often that it's cheaper than having an added transaction.
- There is a spec from the last hard fork-- this question came up in relation to withdrawals. Payment schemes specified in specs: https://github.com/ethereum/builder-specs
