# EVMMAX Breakout - Devcon SEA L1 R&D Workshop 

**Summary:** Plans for EVMMAX (EVM Modular Arithmetic Extension)

**Facilitator:** Paweł Bylica

**Note Taker:** Alex Beregszaszi

**Pre-Reads:** 

Without EOF:
- [EIP-6601 discussion](https://ethereum-magicians.org/t/eip-6601-evm-modular-arithmetic-extensions-evmmax/13168)
- [EIP-6601 spec draft](https://github.com/ethereum/EIPs/pull/6601)

With EOF: https://github.com/ethereum/EIPs/pull/8743/files

**Slides:** https://docs.google.com/presentation/d/1eDuamV2ZbdQme_bAg-2-Ih1dgiFAXc2yk6rmZ04hg54/edit?usp=sharing

## Agenda 

- (20 mins) Intro to EVMMAX
- (10 mins) EVMMAX - EOF relation
- (15 mins) Use cases beyond ECC
- (30 mins) Extensions - INV, EXP, SIMD
- (15 mins) Summary + action items

## Notes & Action Items 

*Breakout sessions will **not** be recorded.* 

*Good notes will help everyone who could not be in the room get up to speed on what happened. Unless instructed otherwise by a participant, please default to using [Chatham House Rules](https://en.wikipedia.org/wiki/Chatham_House_Rule#the_rule).* 

*This will make the process easier, but in cases where there is value in specifying a specific individual (e.g. they are championing a proposal, taking on an action item, etc.), you can mention them. Similarly, nothing should be "off the record", but if someone is uncomfortable with a statement being part of the notes, please respect this.* 

*As a calibration point, see the [ACD recaps](https://ethereum-magicians.org/t/all-core-devs-execution-acde-198-october-10-2024/21314/2?u=timbeiko)*

### Intro

- **Please read the slides, mostly readable without comments**
- Precompiles are mostly crytographic helpers
- Motivation:
    1. Make creation of new "precompiles" easier (without making them precompiles), think about BLS12
    2. Replace existing precompile implementations (some are more mature than others)
    3. Helps bootstrapping new client implementations (including zkEVMs), if evmmax implementations of precompiles can be taken as is
- Question: are many precompiles proposed?
    - Slide includes ~10, but maybe the speed of proposals is slowing down?
- Argument: shouldnt precompiles really have discounted cost (as today)?
- Question: is pricing a big problem for precompiles?
- Most instructions are mispraced in the EVM. EVMMAX pricing seems realistic (and is much lower than existing instructions).
- Note: some zk chains (like zksync) implement precompiles in Solidity to avoid writing circuits.
- Current team (Ipsilon) is not yet ready to champion this on ACD, due to lack of time. External champions would be welcome. Ipsilon is happy/willing to work on specs, implementation, testing.
- Question: what is the timeline to champion/deploy this?
    - Depends on the EOF relation question, see below.
- Suggestion: frame EVMMAX as "It allows users to build precompiles".
    - It allows "progressive precompiles".
    - Could deploy an evmmax contract, keep it as the spec, and later introduce a special gas costing function for it, if we want to discount it.
- Beyond existing precompiles, there is a MiMC implementation in evmmax, which costs 1/10th that of the Solidity implementation Tornado cash uses. It was estimated it would cut a Tornado transaction by half (this work was done before Tornado was banned). However, MiMC/Posiedon applies to many other zk proving systems on L1 which evmmax could improve.

### EOF relation

- Instructions encoding would differ
    - With EOF we can have immediate values for the indexes
    - On legacy one needs a workaround ("fake PUSH instructions"), resulting in larger bytecode
- With EOF it is possible to
    - Have a setup section with upper bounds and can preallocate memory (SETUPX would operate within these bounds)
    - Validate instruction indexes to be always valid, this avoid out of bounds checks at runtime and reduces gas costs
- Feedback from group: **highly prefer EVMMAX to depend on EOF** as it simplifies it, and EOF deployment is likely.

### Summary

- What is the maturity of the spec? Are we confident the instruction set is capable of serving existing and new precompiles?
    - point addition/muliplication is feasible (needs one context)
    - secp256 precompiles are feasible (more complex, needs two contexts, only change once)
- **Next step: propose EXPMOD upper bounds.**
- **Suggestion: create Impact Analysis, don't focus on existing precompiles, but newly suggested ones.**
    - "Don't see a future if we focus on existing precompiles."