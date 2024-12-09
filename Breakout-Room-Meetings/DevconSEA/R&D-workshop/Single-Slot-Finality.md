# SSF session - Devcon SEA R&D workshop 

**Summary:** we'll discuss state of research around shortening Ethereum's finality time, discussing some of the possible paths we might take to get there, and the (more than just technical) tradeoffs they imply. 

**Facilitator:** Francesco

**Note Taker:** Barnabe

**Pre-Reads:** 
- Main:
	- [Possible future of the protocol: merge track](https://vitalik.eth.limo/general/2024/10/14/futures1.html)
	- [Orbit SSF](https://ethresear.ch/t/orbit-ssf-solo-staking-friendly-validator-set-management-for-ssf/19928)
	- [Rainbow staking](https://ethresear.ch/t/unbundling-staking-towards-rainbow-staking/18683)
	- [Simple Single Slot finality](https://ethresear.ch/t/a-simple-single-slot-finality-protocol/14920)
	- [3SF: 3 slot finality](https://ethresear.ch/t/3-slot-finality-ssf-is-not-about-single-slot/20927)
- Optional:
	- [Horn signature aggregation scheme](https://ethresear.ch/t/horn-collecting-signatures-for-faster-finality/14219)
	- [More signature aggregation](https://ethresear.ch/t/signature-merging-for-large-scale-consensus/17386)
	- [Path to SSF](https://notes.ethereum.org/@vbuterin/single_slot_finality)

**Slides:** [here](https://docs.google.com/document/d/1pynCM25Lf6tAf-6HZX-Lri28Wgac-K3vGyukn18FAzM/edit?usp=drivesdk)
## Agenda 

### 15-25 mins: overview of state of research on paths to SSF
 
 - Track 1: path to SSF
	- Orbit-style: participate proportionally to stake
	- Rainbow staking: reduce the role of home stakers to proposing (blocks and/or ILs)
	- Brute force: just support more sigs/slot
- Track 2: consensus protocol
    - SSF protocol
    - 3SF protocol
    - Implementation questions


### 50-60 mins: breakouts or single discussion

After the overview of these different sides of SSF research, we'll decide whether to split into two groups or stay in one group, in which case we might stick to one topic or dedicate some time to both.

Possible goals:
- Get people up to speed on the state of research
- Track 1: agree on one approach and ideally an iterative roadmap to implement it
- Track 2: Surface and/or address implementation concerns with the existing protocols

### 15 mins: wrap-up, take aways



## Session notes


### Part 1: Presentation

[Slides](https://docs.google.com/presentation/d/1-fTMPXtbCgwYJ-K2CW93GGZrzRRrtPnpE8O3Zv81gyA/edit?usp=sharing)

### Part 2: Questions

* Do we still have accountable safety?  
  * Yes, minor changes to the slashing conditions but all good.  
* Does 3SF give us faster slot times?  
  * Not inherently, even today we could shave off time from parts of the slot e.g., make aggregation phase 2 seconds.  
* Does 3SF affect the mev supply chain?  
  * Not inherently, similar properties as today when it comes to reorgs/missed slots/timing games.  
* What happens if no one consolidates?  
  * In Orbit, there are incentives to consolidate.  
* Expected committee size discussion  
  * Stable committee size, but what is the distribution of the committee size given the distribution of stake across validators?  
* Amount of economic finality based on the stake among committee members  
* Question on incentives to consolidate in Orbit  
  * Explicit incentives or implied ones?  
  * Two forms:  
    * Collective incentives: everyone hurts more when people consolidate less  
    * Individual incentives: if there isn’t high consolidation, you get more rewards if you are consolidate  
  * Is there a centralisation risk if we give more power to consolidated validators?  
    * For LMD-GHOST, not really, random sampling  
    * For finality, more influence of consolidated validators, but the argument for why it’s ok is that today we have 5-10% solo stakers, they are valuable for CR but not so valuable for finality, they are not a blocking minority, they cannot force finality, so their influence on finality today is also small, but it is true that it changes the influence of solo stakers in that section. Also ties with rainbow staking, recognise that their influence is small, and separate them more fully from attestation services.  
* Networking complexity of 1-slot SSF  
  * Each voting phase looks like today’s voting phase, so same same  
* Committee size and min balance: can we do 1 ETH validators  
  * Francesco bearish on 1 ETH, \[redacted\] wants the beacon state in memory, not on disk  
* Implementation question: when we process a block, all the fork choice information is available quickly. In the happy case of 3SF, things are still fine, but with the multiple source-target possibilities, do we need to cache things longer?  
  * It’s high bar to become a source that one cares about, needs to be justified, so not expected to blow up memory  
* How big is the slashing rule change? Do we need to reimplement stuff from scratch?  
  * Francesco thinks that it’s pretty similar  
* Are specs and implementations really blocked by the lack of a decision on validator set size management?  
  * Maybe we would want to do committee-based finality if we were forced to live with a very large validator set.

# SSF session notes

[Session doc](https://hackmd.io/@fradamt/devcon-ssf-session)

## Part 1: Presentation

[Slides](https://docs.google.com/document/d/1pynCM25Lf6tAf-6HZX-Lri28Wgac-K3vGyukn18FAzM/edit?usp=drivesdk)

## Part 2: Questions

* Do we still have accountable safety?  
  * Yes, minor changes to the slashing conditions but all good.  
* Does 3SF give us faster slot times?  
  * Not inherently, even today we could shave off time from parts of the slot e.g., make aggregation phase 2 seconds.  
* Does 3SF affect the mev supply chain?  
  * Not inherently, similar properties as today when it comes to reorgs/missed slots/timing games.  
* What happens if no one consolidates?  
  * In Orbit, there are incentives to consolidate.  
* Expected committee size discussion  
  * Stable committee size, but what is the distribution of the committee size given the distribution of stake across validators?  
* Amount of economic finality based on the stake among committee members  
* Question on incentives to consolidate in Orbit  
  * Explicit incentives or implied ones?  
  * Two forms:  
    * Collective incentives: everyone hurts more when people consolidate less  
    * Individual incentives: if there isn’t high consolidation, you get more rewards if you are consolidate  
  * Is there a centralisation risk if we give more power to consolidated validators?  
    * For LMD-GHOST, not really, random sampling  
    * For finality, more influence of consolidated validators, but the argument for why it’s ok is that today we have 5-10% solo stakers, they are valuable for CR but not so valuable for finality, they are not a blocking minority, they cannot force finality, so their influence on finality today is also small, but it is true that it changes the influence of solo stakers in that section. Also ties with rainbow staking, recognise that their influence is small, and separate them more fully from attestation services.  
* Networking complexity of 1-slot SSF  
  * Each voting phase looks like today’s voting phase, so same same  
* Committee size and min balance: can we do 1 ETH validators  
  * Francesco bearish on 1 ETH, \[redacted\] wants the beacon state in memory, not on disk  
* Implementation question: when we process a block, all the fork choice information is available quickly. In the happy case of 3SF, things are still fine, but with the multiple source-target possibilities, do we need to cache things longer?  
  * It’s high bar to become a source that one cares about, needs to be justified, so not expected to blow up memory  
* How big is the slashing rule change? Do we need to reimplement stuff from scratch?  
  * Francesco thinks that it’s pretty similar  
* Are specs and implementations really blocked by the lack of a decision on validator set size management?  
  * Maybe we would want to do committee-based finality if we were forced to live with a very large validator set.