# (e)PBS Breakout Room #1

Note: This file is copied from [here](https://gist.github.com/terencechain/1f883342b99a910e979805bb034043f9)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/953

**Date & Time**: [Feb 13, 2024, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://youtu.be/63juNVzd1P4


### Meeting notes:

- Alex gave an overview of what PBS is. Auction to facilitate the exchange between builder & proposer. The current design is mev-boost based which introduces an additional actor: relayer that facilitates the auction. Concerns lately about censorship and not clear is sustainable in the long term.

- Alex raised 3 open design challenges
    - Proposer splits view to grief the builder
    - P2P gossip is slower and latency matters (Potuz commented on this below)
    - Builder payment to the proposer. In consensus or execution?

- Danny mentioned it’s not clear what the right optimizations are here. What is builder safety? We should design the parameters first and specify them more cleanly before we all agree on and go deeper

- Potuz raised another open design challenge 
   - Slot duration. Will like to keep everything as 12s or worry about breaking downstream usages? This means no additional round of gossip

- Potuz gave an overview on the balance attack. TLDR: The builder faces a dilemma if the proposer releases block close to the attestation deadline. If it reveals the payload but the block is non-canonical then it faces the next slot unbundling attack. If it doesn’t reveal the payload and the block is canonical then the builder has to pay

- Potuz brought up potential mitigation by letting the proposer boost be random and hidden until builder reveals it. Danny brought up a concern about random distribution which can be modeled as a repeated game. Also if we let builder choose the value then the builder will always grind the proposer boost to 0 anyway

- Some fork choice changes were brought up like block slot voting becomes a most so proposer boost value will be adjusted anyway. There might be an interesting research project here. Something to follow up

- Dankard brought up why not Vitalik’s original design by giving the builder fork choice weight. There were concerns about double proposer boost but given proposer boost will likely be changed anyway. One of the main concerns with Vitalik’s design is it’s hard to fit everything under 12s

- Another question was why payment on the CL. The main reason is to reduce spec and code complexity. Proposers can’t select themselves as a builder. The downside is inclusion list is required

- With bids over p2p, it is mostly a protocol fallback. It’s expected builder to enshrine the relayer role and offer relayer features like cancellations

- Then the rest of the meetings discussed how proposer can just bypass the system by selecting the 0 value bid header and handling payment out of band. Potuz argued this is not an issue. There seems to be agreement that there’s a profound difference here because to enter the market you dont need trust. The market can be more competitive but there’s a trade-off cost on whether it’s worth it. It’s noted client default is import there, ppl who want to maintain the same status will have to maintain a forked client

#### Next step. 
- Will have another ePBS break-out call to follow up on the splitting attack. But in this call, we established that:
    - Builder safety is a necessary condition.
    - Slot time being 12 seconds is a necessary condition.
