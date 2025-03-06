# FOCIL Breakout Room #05

Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1325)

### Meeting Info

**Agenda**: [ethereum#1325](https://github.com/ethereum/pm/issues/1325#issue-2875692793)

**Date & Time**: [ February 11th, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: [here](https://www.youtube.com/watch?v=UW9vA3FIYn8)

## Meeting notes:
## Research

## FOCIL and Scaling  

There was a [thread](https://x.com/adietrichs/status/1892951240524403089) on solo stakers and censorship resistance on Twitter. We want to scale Ethereum without compromising verifiability and censorship resistance. While Ethereum’s censorship resistance relies on solo stakers who locally build blocks, they currently forgo potential profits from MEV-boost to uphold censorship resistance. FOCIL eliminates this trade-off between profits and values by allowing solo stakers to continue influencing block content decisions without sacrificing revenue. Consequently, FOCIL opens the door to more effective scaling solutions such as deeper exploration into PBS and APS.  

## Compatibilities with Other Proposals  

Francesco suggested a way to make FOCIL compatible with [Delayed Execution](https://ethresear.ch/t/delayed-execution-and-skipped-transactions/21677). It enables “dry-run” IL validation during the static validation phase. It adds a bitfield over the IL committee to a block, and a proposer marks the bits corresponding to the ILs considered during block construction. During the static validation phase, attesters check whether the ILs specified in the bitfield form a superset of the ILs they collected. They do not verify that all IL transactions are included; they focus solely on whether the bitfield matches or exceeds their own IL set.  

In the next slot, the proposer confirms whether the head block contains all valid transactions from the ILs specified in the bitfield. If it does, the proposer extends the head block; otherwise, they extend the parent block. Attesters follow the same process to determine whether to vote for the head block or its parent.  

This [approach](https://hackmd.io/UX7Vhsv8RTy8I49Uxez3Ng) is similar to the one used to make FOCIL compatible with ePBS.  

## Adding Randomness to IL Building Rules to Optimize Throughput  

Marc proposed an IL building approach that leverages randomness to reduce overlap among ILs and optimize throughput. In this approach, each IL committee member is assigned an ID from `0` to `f`, and the member with ID `a` is instructed to favor transactions whose hashes begin with `a`. More details can be found in the [Ethereum Magicians post](https://ethereum-magicians.org/t/eip-7805-committee-based-fork-choice-enforced-inclusion-lists-focil/21578/6) and this [PR](https://github.com/ethereum/EIPs/pull/9396).  

Terence suggested waiting until we have a better understanding of how client diversity plays out before making any premature optimizations. In the meantime, further study on this topic is encouraged. However, Terence also agreed that the EIP should provide clearer recommendations on the properties each client can reference when implementing IL construction.  

Marc’s proposal could be a viable solution if prioritizing throughput, but additional research is needed before making changes. In the meantime, the EIP can be updated to include clearer recommendations on which properties to consider when implementing IL construction.  

## The Interop Between Prysm and Lodestar  

Prysm and Lodestar are currently failing to interop due to an invalid signature issue, possibly related to signing over the wrong fork version or another cause. The issue is under investigation, and once resolved, the first interop between CLs is expected.  

## Implementation Updates  

- **Geth**: Fixed bugs to avoid marking non-IL-compliant blocks as invalid and allowing them to be reorged instead. Also supports the transition from Electra to Fulu and subsequently to EIP-7805 fork.  
- **Nethermind**: Opened a [PR](https://github.com/ethereum/EIPs/pull/9381) to flesh out engine API changes in the EIP. Reported a bug in Geth where non-IL-compliant blocks were marked as invalid instead of remaining valid and being reorged. Fixed the issue in Nethermind's implementation as well.  
- **Lodestar**: Rebasing from Electra to Fulu in preparation for interop with Prysm. Primarily testing and working on activating EIP-7805 fork in the same epoch as Fulu.  
- **Teku**: Working on interop between two Teku nodes using stub ELs.  
- **Prysm**: No update.  
- **Reth**: No update.  
- **Lighthouse**: Absent during the call.  
- **Metrics Dashboard**: Katya is developing a metrics dashboard with Prysm and may have it ready to share during the next breakout session.  

## Consensus Hong Kong  

Jihoon delivered an ELI5 presentation on FOCIL at Consensus Hong Kong. The recording is available [here](https://consensus-hongkong2025.coindesk.com/agenda/event/-protocol-village-52), starting at approximately 28:13.  

## Links  

- [A thread on FOCIL and Scaling](https://x.com/adietrichs/status/1892951240524403089)  
- [IL Tx Scoring Function in FOCIL](https://hackmd.io/@ttsao/il-tx-scoring)  
- [ePBS/DAS/FOCIL all-in-1 fork-choice](https://hackmd.io/UX7Vhsv8RTy8I49Uxez3Ng)  
- [FOCIL talk at Consensus Hong Kong](https://consensus-hongkong2025.coindesk.com/agenda/event/-protocol-village-52)  
- [Adding randomness to IL building rules](https://ethereum-magicians.org/t/eip-7805-committee-based-fork-choice-enforced-inclusion-lists-focil/21578/6)  
- [A PR to the EIP that expands on EL changes](https://github.com/ethereum/EIPs/pull/9381)  
- [A PR to the EIP that adds properties to consider for IL construction](https://github.com/ethereum/EIPs/pull/9396)  
