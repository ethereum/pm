# L1 R&D session: Proposer-Builder Separation

**[*Required*] Summary:** *We will provide an update on the state of the research on Proposer-Builder Separation (PBS). The session will be divided between high-level design space discussions as well as specifics of EIP-7732.* 

**[*Required*] Facilitator:** *Terence and Mike.*

**[*Required*] Note Taker:** *Terence and Mike.* 

**[*Required*] Pre-Reads:** 
- [EIP-7732](https://eips.ethereum.org/EIPS/eip-7732)
- [Why Enshrine PBS](https://ethresear.ch/t/why-enshrine-proposer-builder-separation-a-viable-path-to-epbs/15710)
- [Relays in a post-ePBS world](https://ethresear.ch/t/relays-in-a-post-epbs-world/16278)
- [PTC](https://ethresear.ch/t/payload-timeliness-committee-ptc-an-epbs-design/16054)

**[*Optional*] Slides:** 
- [Terence's Slides](https://docs.google.com/presentation/d/1XUTsw98hprHSNnpzCkRUgSU9nuQiq5wkpHGon3Nw7wU/edit#slide=id.g31207e378c5_2_86)
- [Mike's Slides](https://github.com/michaelneuder/talks/blob/main/devcon2024/l1rand.pdf)

## Agenda 

- **15 min high-level intro:** Mike
- **15 min EIP discussion:** Terence
- **45 min open session.**
- **15 min wrap up.**

## Notes & Action Items 

_These are Julian’s notes on the ePBS session. They cover only the discussion in the room and not the content presented by Mike and Terence during their presentation._

**Mike Presentation**

- Is there still an incentive for timing games if ePBS were implemented with slot auctions?
    - Preliminary results suggest that slot auctions still offer the incentive to time games qualitatively. Quantitatively, the incentives are likely smaller in slot auction ePBS than in block auction ePBS, keeping all other factors constant.
- Why does FOCIL not enforce a specific ordering of transactions to prevent MEV extraction, for example, by letting the transactions from FOCIL fill the top-of-the-block?
    - If inclusion lists were set at the top of the block, inclusion list creators would have a valuable right to construct them. Inclusion list committee members would then be more likely to outsource inclusion list construction via an MEV-Boost-like system, which would defeat the purpose of inclusion lists.
- Do proposers who want to self-build need to bid to themselves in an auction?
    - No, this is not necessary in EIP-7732. This would only be necessary with MEV-Burn, which is not part of EIP-7732.
- “How risky is the DoS vector resulting from proposers IP leaking through sending a direct request to the builder during their slot?”
    - DoS attacks are already easily possible. First, validators register with relays, which provides enough information to do a DoS attack on them. Second, it is possible by monitoring the p2p layer.
- Why would validators still want to use relays?
    - There is some stickiness to the current setup since proposers are already connected to relays.
        - If ePBS were implemented, clients could remove the MEV-Boost support, ensuring that builders need to use ePBS to access proposers.
        - If a small percentage of validators do not want to use MEV-Boost, this could force builders to use ePBS, especially because builders do not want to risk losing an extremely high-value block.
    - Builders could use their market power and not support ePBS, forcing proposers to use ePBS.

**Terence Presentation**

- Can the separation between consensus and execution validation be done without ePBS?
    - Yes, this is possible
- What is the value of consensus liveness without execution layer liveness?
    - Unclear what the value is. Perhaps it is better for economic finality if there are still consensus blocks even when execution payloads are missing.
- With ePBS, there is accountability of who caused execution liveness failures because headers are signed and on-chain.
    - The accountability can then be leveraged by using a builder circuit breaker.
    - However, since there are only two builders, it is unclear whether using a builder circuit breaker is incentive compatible with being a proposer. Perhaps proposers only care about the unconditional payment and want to avoid blocking a builder.
        - Validators would have to fork clients to obtain this feature if clients do implement a builder circuit breaker.
            - Implementing client code that is not incentive-compatible for the proposer is a slippery slope, and it could cause the proposer to miss out on large rewards.
- How does ePBS interact with faster slot times?
    - There are multiple proposers to obtain faster slot times.
    - Block auction ePBS is challenging to rhyme with faster slot times. If ePBS were changed to something like slot auctions, then perhaps ePBS could be compatible with faster slot times.
- A year ago, it was a big problem that neutral relays needed funding. Perhaps ePBS can help with this issue, as there may be no need to fund a neutral relay because the protocol functions as a relay.
- Could the protocol implement a gossipsub for the auction?
    - Yes, EIP-7732 implements a gossip-based market next to the direction connection market.
- Every future block construction setup has a split between the beacon block and the execution payload. EIP-7732 is a first step towards this future block construction setup.
    - Is it possible to make this separation without facilitating the fair exchange problem between the proposer and builder?
- Does ePBS introduce problems in the fork-choice?
    - Francesco’s new design might solve the fork-choice issues with the Payload-Timeliness Committee (PTC) in EIP-7732.
    - Still, in the past, fork-choice issues were only raised when attacks were possible on the mainnet. Changing the fork choice is risky.
- What is the minimal pipelining implementation?
    - Potuz believes EIP-7732 is a minimal pipelining implementation. Given this, it is better to implement EIP-7732 with the auction since the auction is not on-chain. Perhaps later, it can be written out why EIP-7732 is the minimal pipelining implementation.