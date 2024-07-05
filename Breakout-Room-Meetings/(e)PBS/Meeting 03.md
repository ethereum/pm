# (e)PBS Breakout Room #3

Note: This file is copied from [here](https://hackmd.io/@ttsao/epbs-breakout3)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/1067

**Date & Time**: [June 21, 2024, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: https://youtu.be/J1e5iUvcTDU


### Meeting notes:

#### Highlights:

1. A new version of the consensus specification, rebased on top of Electra, will be opened soon.
2. We reviewed changes to the beacon block and state structure, considering whether it makes sense to use header.block_root instead of header.block_hash.
3. We discussed using the SSZ option for the payload withheld message.
4. We believe the slot auction is feasible and preferable in the current EPBS design and worth exploring.
5. Finally, we discussed pre conf and EPBS, including potential contentions and the long-term winning design of pre conf on top of EPBS, as well as how EPBS can improve pre conf.

#### Summary:

- We began the call by reviewing the latest progress on the consensus specification. Efforts are focused on rebasing to the latest Electra release, including moving consolidation out of the block body to the execution payload. Additional time is required to audit changes to attesting indices, ensuring they do not return PTC indices. Currently, no inclusion list is needed as validators can self-build. The specification will be opened soon with the following priorities:
    1. Open the consensus spec first, which includes beacon chain, validator, builder, P2P, and fork choice components.
    2. Follow with the EIP and engine API. Minimal changes are expected to the engine API specification.
    3. No changes are anticipated for the execution specification.
- We debated the potential benefits of changing header.block_hash to header.block_root. This change could simplify proving processes, assuming relevant use cases arise. Currently, the block hash is used for its simplicity and because the EL already tracks it.
- We agreed to remove state.latest_execution_payload_header, a field necessary during the pre-merge phase but largely redundant post-merge. Instead, tracking the parent block hash would have sufficed. In EPB, this field is updated to execution_payload_header to monitor the builder’s header.
- We discussed using SSZ optional for the withheld status. There was consensus that the optional approach is preferable to the current withheld status. The key question is the timeline for implementing optional and targeting it for future forks. The current specification can proceed as is, switching to optional once it gains full popularity and a target fork is defined.
- It was clarified that if a payload is invalid but the consensus block and header are valid, the consensus block remains valid.
- We explored scenarios where a proposer sees a withheld message, but PTC has not. If the proposer sees the payload and PTC does not vote on it, an honest proposer can import the payload. Even without reorg or boost, the payload will extend the head.
- We noted that there cannot be an attack on equivocation from the builder's side, which is significant for moving towards slot auction-based designs.
- We clarified the lack of rewards for PTC. PTC is a subset of the beacon committee and receives attestation rewards, but cannot earn additional beacon attestation rewards. It’s crucial that honest validators prevent PTC members from attesting.

The call concluded with a discussion on EPBS and pre-confirmation:

- Processing in-contention payloads during beacon block processing is problematic for EPBS.
- Large inclusion lists are detrimental to EPBS and other applications like DVT because they require simultaneous validation by both the execution and consensus layer clients.
- EPBS benefits from having a staked builder. Once staked, the builder is compatible with some pre-confirmation designs. Designs requiring a restaked builder complement EPBS and perform better within EPBS.
- If MEV-Boost is discontinued, any necessary functions can be redefined under the beacon API and engine API.

In summary, EPBS implementors should assess how pre-confirmation transactions are handled in every design, particularly whether they must be included in the consensus block or can be enforced at the builder level. Ideally, all enforcement should be on the execution side. Long-term, pre-confirmation designs are more suitable within the EPBS framework because staked builder.
