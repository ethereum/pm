# FOCIL Breakout Room #04

Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1291)

## Meeting Info

**Agenda**: [ethereum#1291](https://github.com/ethereum/pm/issues/1291#issue-2844917923)

**Date & Time**: [ February 11th, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240213T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: [here](https://www.youtube.com/live/2MkoP6BDNro)

## Meeting notes:
### Research  

#### Privacy  
George, Benedict, and Thomas published **zkFOCIL**, which introduces an approach that allows includers to propose inclusion lists without revealing their identity. We really want to push this further and encourage anyone interested to reach out—either by applying to the academic grants round or implementing a prototype.  

#### Compatibilities with Other Proposals  

### FOCIL and Delayed Execution  
Thomas reviewed how **FOCIL** can work with **Delayed Execution** by Toni and Francesco and identified potential inherent incompatibilities. In **Delayed Execution**, blocks are validated while transactions are executed asynchronously. However, in **FOCIL**, if any IL transaction is missing in a payload, attesters should execute the payload to determine whether the missing transaction is invalid.  

Several possible solutions have been proposed, but further research is needed.  

### FOCIL and ePBS  
Terence reviewed how **FOCIL** can work with **ePBS**. There are different flavors of "delayed execution":  

1. **Toni and Francesco's approach**:  
   - The block includes the previous state root instead of the current one.  

2. **Alternative approach**:  
   - Decouples execution from the block, treating it as a separate object.  
   - Divides each slot into two parts:  
     - First half → Consensus block  
     - Second half → Execution payload  

While this strategy is adopted by **ePBS**, it introduces trade-offs for **FOCIL**:  
- **Reduces** the time available for the IL committee to construct ILs.  
- **Modifies** the rules to enforce IL in the next slot rather than within the same slot.  

Both approaches have different trade-offs:  
- **Delayed Execution**: Primary concern is enforcing IL constraints.  
- **ePBS**: The focus is more on timing.  

Further research is needed to analyze these trade-offs.  

## FOCIL Progress Tracker  
Jihoon and Thomas created a **progress tracker** for all clients, allowing everyone to check the current status. They will update it frequently, so reach out if you'd like your progress reflected.  

### Implementation Updates  
- **Nethermind** is working on interop with **Prysm**.  
- **Lodestar**:  
  - Finished basic implementation, reviewed code internally, and tried interop with **Geth**.  
  - Found a **bug in Geth**, which has been fixed.  
  - Lodestar <> Geth local devenet works fine.  
  - However, **a state root mismatch issue** occurs when Prysm is added to the local devnet—both Prysm and Lodestar reject each other's blocks.  
- **Prysm**:  
  - Tested the happy case.  
  - Encountered the same issue with **Geth**, which has been fixed.  
  - Currently undergoing **refactoring and testing**.  
- **Reth <> Lodestar**:  
  - Works in the **happy case**.  
  - Additional test cases are in progress.  
  - Running a local devnet of **Reth <> Lodestar** and **Reth <> Prysm** suffers from the **state root issue**.  
- **Lighthouse**:  
  - Working on interop with **Geth**.  
  - Expects to join **Prysm** and **Lodestar** by the end of the week.  
- **Teku**:  
  - Still under development.  
  - After implementing **fork-choice** and **beacon APIs**, Teku is **ready for interop**.  

### Issue with Dora  
**Dora** doesn't recognize **EIP-7805** blocks, so CLs had to hard-code the beacon block's version to **Electra**. This was due to miscommunication, but **Dora will alias EIP-7805 as Electra** moving forward.  

### PEEPanEIP  
**Thomas and Julian** had a podcast with **Pooja**. A recording should be published this week.  

## Questions  

**Is zkFOCIL going to change EIP-7805?**  
No, it's still in the early research phase and won't hold FOCIL back. It's part of the **FOCIL endgame**.  

## Links  
- [FOCIL Progress Tracker](https://meetfocil.eth.limo/)  
- [zkFOCIL: Inclusion List Privacy using Linkable Ring Signatures](https://ethresear.ch/t/zkfocil-inclusion-list-privacy-using-linkable-ring-signatures/21688)  
- [Call for participation for privacy research—academic](https://x.com/asn_d6/status/1887442959445926333)  
- [Call for participation for privacy research—implementation](https://x.com/asn_d6/status/1887442961459233130)  
- [FOCIL meets Delayed Execution](https://hackmd.io/Ntn30DbJQV-HEiKxBsPKEw)  
- [FOCIL with Delayed Execution under EPBS (EIP-7732)](https://hackmd.io/@ttsao/focil-delayed-exec-under-epbs)  
- [PEEPanEIP recording](https://youtu.be/cUGyLx-mf6I)