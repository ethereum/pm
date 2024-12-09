# L1 <> L2 Collaboration

**[*Required*] Summary:** 
- How to improve 2-way dialogue, improve our inputs for L1 roadmap decisions, and better contribute to more L2-specific discussions. 
- Navigating the current and future rollup-centric landscape together 🤝

**[*Required*] Facilitator:** Nico and Ansgar and Josh

**[*Required*] Note Taker:** Josh

**[*Required*] Pre-Reads:** 
- [RIP-1](https://github.com/ethereum/RIPs/pull/41/files)
- [EVM equivalence on L2](https://docs.google.com/presentation/d/12t-7bG7bgOh02wQlmrcJrwkEuV5HI_CJux7bIepertE/edit#slide=id.g30d8dba0896_0_208)

## Agenda and Goals

**Topics**: 
- Whats actually the role of L2s (tension between "leading the way and innovating" vs. "maintaining full equivalence") 
- L2 Geth review
- How to empower L2s to provide input on L1 roadmap decisions
- How can L1 devs/researchers best fit in to more L2 conversations
- Examples of things that have been going well / poorly
- Specific things we can improve in next 3-6 months (low-hanging fruit), and longer-term goals 


## Notes & Action Items 
- RollCall overview: not meant to enforce forks, very differnet purpose from ACD. Have been discussing few low-hanging fruits to have more features available for L2s. 
- RollCall still very new. Open call for suggestions/feedback. 
- Just pushed RIP-1. Similar vibes to EIP-1. Just describes the process. 
- Can think of L1<>L2 as two separate branches: (1) EVM side and everything execution related, state DB, etc, and (2) separate branch: standards & L2 interop, things that help L2s play well with each other and broader ecosystem. 
    - RollCall focused on (1)
- new team within Nethermind: L2-centric Geth "rollup Geth"
- lot of L2s are using Geth. New team is supposed to help provide more L2-focused version of Geth. 
- Original plan: once we ship this beautiful new Eth 2.o thing, then we can retire Eth 1 
- But it turns out: when we got to the merge, we realized rollups better path as opposed to sharding. Open it up for everyone to build their own: rollup-centric roadmap
- New vision for eth1: base layer for rollups to go and scale
- L2s recognizing they need to bootstrap off of EVM, so can build off network effects 
- L2 innovations since: L2-specific things like Stylus. But inability to innovate because they dont want to lose EVM compatibility 
- L1 teams not able to provide L2 clients what they need
- New EL features mostly tailored to L1 needs: 7702, EOF, Verkle, etc 
    - Some L2 teams unsure if they would adopt Verkle
- Weird mismatch where L1 is designing and planning for L1
- Mismatch in different dimensions:
    - throughput ambitions
    - full node reqs
    - block building
    - zkEVM (not happening on L1 any time soon)
    - general difference in philsophy and risk aversion
- Today: Reth and Nethermind as a major client w/ explicit L2 focus
- But: most L2s for now still on Geth
- Two pronged vision to unlock L2 innovation:
    - (1) Rollup Geth: maintain L2-specific fork. Can implement actual consensus changes that L2s are interested in. 
    - (2) But still a problem of no one wants to break L1 EVM compatibility. give them a way to stay equivalent to each other, but not with L1 EVM. So, its an L2 EVM: 
        - Shared set of RIPs supported by all participating L2s
        - Retain network effect
        - become the standard L2 target for tooling, wallets, etc
        - shared approach for how to handle upcoming L1 changes
        - Goal: standardized, but ambitious. 
- L2 EVM common core examples:
    - basic repricing (for ZK)
    - 2d transaction type
    - native AA
    - transaction parallelization 
    - statelessness / state expiry / state rent
    - multidimensional pricing
- Existing roles: L2 coordination, RIPs, L1<>L2 connective tissue
- New roles: L2 client coordination, L2 EVM governance, L2 EVM R&D
- For L2s using Geth: decide whether to move to rollup Geth, connect with the team, figure out migration process
- Question for Geth: to what extent do L1 focused devs want to be part of the process. 
- Marius: definitely want to be involved in the effort around L2 Geth. Currently doing a lot of refactoring of the codebase. So it makes sense to share the roadmap ahead of time with Nethermind folks working on L2 Geth.  Aligned with the effort, just dont have a lot of time :) 
- Q: Does the L2-centric version of the EVM make sense to people in this room.
- Q: how can we better enable L2s to provide input on L1 roadmap decisions
- Some decisions are being made on L1 that affect L2 teams. Some affect more than others. Example: idea increasing cost of hashing precompiles. For ZKrollups. Maybe Optimistic rollups could be against this. Competing interests here. 
- Need to get better at being aware of things that impact L2s. Right now we only have L1 people in the room. 
- For increasing hashing gas prices: its not just about CPU time. EVM is multidimensional. One of the dimensions. 
- Ansgar: the "common core" can be as large or as small as makes sense for the L2s.. with Native AA: the common core is a good way to ship it. They dont want to break compatibility here. 
- Native / enshrined rollups: will this restrict rollups from innovating. By definition, they are somewhat constrained. 
- L2 Geth: when we have agreement on what is the feature set in the common core, then start implementing. Right now still a bit early on the timeline. RIght now "L2 Geth" master branch has no diff from L1 Geth. 