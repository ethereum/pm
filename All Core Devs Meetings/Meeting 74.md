# All Core Devs Meeting #

### Date/Time: Friday 1 November 2019, 14:00 UTC
### Duration: 1.5 hours
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=aZ0S_oLSwhE)

# Agenda

- [Decisions](#decisions)   
- [1. Istanbul updates](#1-istanbul-updates)   
- [2. Berlin](#2-berlin)   
  - [2.1 Ice Age](#21-ice-age)   
  - [2.2 Tentatively Accepted EIPs](#22-tentatively-accepted-eips)   
     - [2.2.1 EIP-663](#221-eip-663)   
     - [2.2.2 EIP-1380](#222-eip-1380)   
     - [2.2.3 EIP-1702](#223-eip-1702)   
     - [2.2.4 EIP-1962](#224-eip-1962)   
     - [2.2.5 EIP-1985](#225-eip-1985)   
     - [2.2.6 EIP-2045](#226-eip-2045)   
     - [2.2.7 EIP-2046](#227-eip-2046)   
     - [2.2.8 EIP-1057](#228-eip-1057)   
     - [2.2.9 EIP-1559](#229-eip-1559)   
  - [2.3 Process & Scheduling Discussion](#23-process-scheduling-discussion)   
- [3. Testing updates](#3-testing-updates)   
- [Attendance](#attendance)   

<!-- /MDTOC -->

# Decisions


| Topic | Decision |
|-------|----------|
| Istanbul Block Number | 9,069,000 |
| Berlin EIP Deadline | 3rd Wednesday of March |
| EIP-1679 | `Accepted & Final` |
| EIP-1679 | `Accepted & Final` |
| EIP-152 | `Accepted & Final` |
| EIP-1108 | `Accepted & Final` |
| EIP-1344 | `Accepted & Final` |
| EIP-1884 | `Accepted & Final` |
| EIP-2028 | `Accepted & Final` |
| EIP-2200 | `Accepted & Final` |
| EIP-1702 | `Eligible for Inclusion` Pending Champion. Not accepted into Berlin |
| EIP-663 | May not be ready. Currently depends on EIP-1702 |
| EIP-1962 | Requires more Specification. Contact Champion |
| EIP-1380 | `Eligible for Inclusion` |
| EIP-1985 | Decision required around needing a Hard Fork |
| EIP-2046 | `Eligible for Inclusion` |
| EIP-1985 | `Eligible for Inclusion` |
| EIP-1559 | `Eligible for Inclusion` |

Miscellaneous:
- Further discussion on EIPs discussed should be postponed until an implementation is brought forward
- `Blessed` status changed to `Eligible for Inclusion`.
- Create dedicated list/directory for `Eligible for Inclusion` EIPs, in addition to listing EIPs undergoing the new EIP process
- Create a new Information EIP covering these new stages, possibly under EIP-1
- A section for EIP decisions should be included in meeting notes for quick access to address outstanding PRs by EIP editors.

# Notes

Video: [[4:59]](https://youtu.be/aZ0S_oLSwhE?t=299)

**Hudson Jameson:** Welcome to core developer meeting #74. We'll talk about the Istanbul block number that was accepted, the Berlin hard fork, tentatively accepted EIPs, and some testing updates.


## 1. Istanbul updates

Links: [Istanbul Meta EIP](https://eips.ethereum.org/EIPS/eip-1679) | [Istanbul EIP Implementation Tracker by @holiman](https://notes.ethereum.org/@holiman/SyT_rGjNr)

Video: [[5:32]](https://youtu.be/aZ0S_oLSwhE?t=332)


**Hudson Jameson:** A block number for Istanbul was chosen. Coindesk corrected their article.

- **Istanbul Block Number:** 9,069,000

When are clients releasing an update with the [Istanbul] block number attached?

**Tim Beiko:** For phase 2, within the next two weeks, mid-November.

**Danno Ferrin:** We'll have it out next week. 

**Hudson Jameson:** The Ethereum Foundation and/or Ethereum Cat Herders are publishing a blog on the block number and what software to upgrade around when most clients update their download links.


Video: [[10:24]](https://youtu.be/aZ0S_oLSwhE?t=624)

**Danno Ferrin:** Should we formally make 1671 accepted?

- [EIP 1679](https://eips.ethereum.org/EIPS/eip-1679 )

**Hudson Jameson:** That sounds good.

**James Hancock:** EIPs are to be moved to accepted and final for integration in Istanbul which has begun for the client. The included EIPs:
- EIP 152
- EIP 1108
- EIP 1344
- EIP 1884
- EIP 2028
- EIP 2200


**Hudson Jameson:** I second that. We should probably have motions.

**Danno Ferrin:** Agreed.


## 2. Berlin

Links: [Berlin Meta EIP](https://eips.ethereum.org/EIPS/eip-2070)


### 2.1 Ice Age

Video: [[7:55]](https://youtu.be/aZ0S_oLSwhE)

**Tim Beiko:** A couple calls ago we said that the Ice Age would start kicking in next summer, please correct me if I'm wrong. We probably want an EIP in Berlin that kicks back the Ice Age.

**Hudson Jameson:** James Hancock decided to write that. Not a huge rush. We delay it the same time each time.

**Danno Ferrin:** That gives us a little over a year each time.


### 2.2 Tentatively Accepted EIPs


#### 2.2.1 EIP-663
[**Unlimited SWAP and DUP instructions**](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-663.md )

Video: [[44:51]](https://youtu.be/aZ0S_oLSwhE?t=2691)

**Hudson Jameson:**  So there has been a lot of comments in the Ethereum Magicians forum on this.

- [Ethereum Magicians Thread](https://ethereum-magicians.org/t/eip-663-unlimited-swap-and-dup-instructions/3346)


**Greg:** I don't think SWAP DUP should be here without basic decisions on the Spec. I don't consider it blessed, but there's not large mountain of work needed.

**Alex Beregszaszi:** Blessed means no objection from Core Devs for the idea. I don't believe any of the Core Devs objected on the idea.

**Greg:** Ok. I still don't think an EIP should come to us without consensus in other discussion that it is a design which will work. It looked to me that it wasn't ready, and there was disagreement among the community, including some Core Devs.

#### 2.2.2 EIP-1380
[**Reduced gas cost for call to self**](https://eips.ethereum.org/EIPS/eip-1380)

Video: [[56:00]](https://youtu.be/aZ0S_oLSwhE?t=3358)

**Alex Beregszaszi:** Benchmarks show some reduction can be made, but not to the degree of the original proposal. 

#### 2.2.3 EIP-1702
[**Generalized account versioning scheme**](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1702.md)

Video: [[34:57]](https://youtu.be/aZ0S_oLSwhE?t=2097)

**James Hancock:** Several EIPs are gated by account versioning.

**Wie Tang:** New specification for account versioning made. 

- https://that.world/~essay/nevm/

**Hudson Jameson:** Pass new specification to new Champion, once one is found.

**Danno Ferrin:** Finishing account versioning for Berlin is unreasonable.

**Wie Tang:** A separate hardfork may be better.

**Hudson Jameson:** Scrap it for Berlin.

#### 2.2.4 EIP-1962
[**EC arithmetic and pairings with runtime definitions replaces EIP-1829**](https://eips.ethereum.org/EIPS/eip-1962)

Video: [[54:11]](https://youtu.be/aZ0S_oLSwhE?t=3251)


**Danno Ferrin:** Earnst and Young (EY) want this EIP for their nightfall. It is good, but requires more specification, and depends on a single implementation. 

#### 2.2.5 EIP-1985
[**Sane limits for certain EVM parameters**](https://eips.ethereum.org/EIPS/eip-1985)

Video: [[57:46]](https://youtu.be/aZ0S_oLSwhE?t=3466)

**Alex Beregszaszi:** May not need a hard fork. 

[Join the discussion on Ethereum Magicians.](https://ethereum-magicians.org/t/eip-1985-sane-limits-for-certain-evm-parameters/3224)


#### 2.2.6 EIP-2045
[**Particle gas costs for EVM opcodes**](https://eips.ethereum.org/EIPS/eip-2045)
#### 2.2.7 EIP-2046
[**Reduced gas cost for static calls made to precompiles**](https://eips.ethereum.org/EIPS/eip-2046)

Video: [[1:00:26]](https://youtu.be/aZ0S_oLSwhE?t=3626)

**Alex Beregszaszi:** Discussed as a part of EIP-1380 discussion.

#### 2.2.8 EIP-1057
[**ProgPoW, a Programmatic Proof-of-Work**](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1057.md)

Video: [[1:00:56]](https://youtu.be/aZ0S_oLSwhE?t=3655)

**Hudson Jameson:** Hard to tell community push-back is a few loud voices, or a community majority. Already in  `Blessed`  state in my opinion.

**Tim Beiko:** 
- Is this something we want the community to signal through their nodes whether or not they want it?
- Do we do a single ProgPoW hard fork?
If it raises risk of the network splitting, do we value keeping the network together?
- Do we not give it special treatment and group it with the other EIPs hoping nodes commit a full upgrade?

**Hudson Jameson:** I say we don't change it, unless high probability of a controversial hard fork where people choose. 

**James Hancock:** Don't treat it differently than any other EIP.

**Piper Merriam:** I'm willing to implement this in our client, if others want. Otherwise, other tasks are higher priority.

If miners really want this, I suggest for shifting a portion of miner rewards towards core protocol development. Something also controversial.

**Greg:** We looked and haven't found technical problems.  We've said yes more than once.

**Hudson Jameson:** Has blessing for sure.

**Tim Beiko:** We can leave it blessed. But there is some distance to go live, as most concerns are non-technical.


#### 2.2.9 EIP-1559
[**Transaction Fee Upgrade**](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1559.md)

Video: [[1:09:01]](https://youtu.be/aZ0S_oLSwhE?t=4141)

**James Hancock:** Blessed.

**Hudson Jameson:** Looks good to me.

**Danno Ferrin:** This is the posterchild for the EIP centric process. It gets blessed. An implementation is made and returned to us. We look at it from there.

**Hudson Jameson:** We should keep in mind Vitalik released Slim 1559, a less complex implementation of it. Both the improvements it provides and the complexity would lessen.

**Danno Ferrin:** Blessings are good, as it's approved as an idea, and through building it, improvements are discovered before final approval. We get a prototype which reflects the best idea, and we test it.

**James Hancock:** Agreed, since its been blessed it's been happening.

### 2.3 Process & Scheduling Discussion


Links: [EIP Centric fork](https://notes.ethereum.org/@holiman/S1ELAYY7S?type=view)

Video: [[7:55]](https://youtu.be/aZ0S_oLSwhE)

**Alex Beregszaszi:** For every EIP change, record a decision in the meeting notes so EIP editors can execute on the meeting notes, for outstanding PRs.

**Hudson Jameson:** Yes, let's do that.

---

Video: [[16:01]](https://youtu.be/aZ0S_oLSwhE?t=961)


Discussion occured around setting timeframes keeping in mind the hard fork. In an EIP-centric model, the proposal was not to set times in advance. However, considering the incoming Ice Age, deadlines for EIP completion before inclusion in the Hard Fork may have use. The third Wednesday of March was chosen for Istanbul.

**James Hancock:** Two conversations are happening. Among Core Devs: When are we going to fork. Core Devs to the Community: There's a realistic deadline of June where completion is required. Then there's a preparation period of 3 months needed for testnets to be live. With those two dates, April, May, and June is available for Istanbul. Keeping forks to a third Wednesday of the month, there are 3 third Wednesdays to select from.

One needs to have the update for the Ice Age. All other EIPs, we don't want to decide a date. By keeping inclusions once a month, we can decide whether to postpone an EIP for it to go with another which goes together. We want to avoid one fork per EIP, as well as waiting significant time to include several EIPs, as both limit implementations, testing, etc.

**Piper Merriam:** I would propose the soonest, as we are just starting this new process.

**James Hancock:** March?

**Piper Merriam:** That is reasonable.

**Hudson Jameson:** For most EIPs, we can decide, implement, and do tests for an EIP within a 3-4 week period. We also decided the champion of an EIP will be the coordinator for testing, right?

**James Hancock:** Yes.

**Hudson Jameson:** Wei said they wanted to remove their name from some they have been championing. 

**Wie Tang:** I won't be able to champion as I won't have enough time to do all the coordination. I don't have a replacement Champion. 

**Hudson Jameson:** For the next two weeks, I propose we keep them to see if there are replacement Champions.

---

Video: [[38:49]](https://youtu.be/aZ0S_oLSwhE?t=2329)


EIPs are no longer categorized by forks. Discussion was around having an EIP status on each EIP website, or keeping a list of `Blessed` EIPs, for organizaion. 

---

Video: [[44:51]](https://youtu.be/aZ0S_oLSwhE?t=2691)

Some discussion occurred on what constituted `Blessed` status. Conclusion was, `Blessed` indicated an idea has been greenlit for continued work, before the final reassesment for inclusion. Furthermore, concern was brought forward for Core Devs reviewing each EIP individually.

**Greg:** If you need to push it to our level, fine, but in most cases I don't think we need to.

---

Video: [[1:10:53]](https://youtu.be/aZ0S_oLSwhE?t=4253)

**Alex Beregszaszi:** Further discussions on those EIPs should stop until further spec and an implementation.

**Tim Beiko:** Unless a Champion joins and starts a discussion, we discuss, otherwise, we don't discuss specific EIPs?

**Tim Beiko:** That would make things easier.

**Danno Ferrin:** Can we take a more neutral name for blessed (ie. preliminary approval)?

**Hudson Jameson:** Jason Carver suggested  `Eligible for Inclusion` instead of Blessed.  

**Danno Ferrin:** In addition to `Eligible for Inclusion` list, we should list new EIPs live on the new EIP process. When a Champion has a prototype ready, they should upload it there. In addition to security reviews. Also, an informational EIP covering this new model.

**Hudson Jameson:** Let's hold discussion to where the `Eligible for Inclusion` list is listed in another call.

**Pooja Ranjan:** The Ethereum Cat Herders can start the list, then we can decide where to put it.

**Hudson Jameson:** That sounds good.

## 3. Testing updates

Video: [[1:21:04]](https://youtu.be/aZ0S_oLSwhE?t=4864)

**Danno Ferrin:** I published a test for EIP-2200

**Trentonvanepps:** Updates on Istanbul should go on the Ethereum.org blog. Additionally, there should be weekly tweets on the Ethereum account on what to do.

**Hudson Jameson:** Sounds good. I think there may be a more detailed blog post in the Ethereum Cat Herders linked in the Ethereum blog.

That's it. Thanks everyone for coming. We'll have our next meeting in 2 weeks.



## Attendance

- Trentonvanepps
- Pooja Ranjan
- James Hancock
- Dominic Letz
- Ratan (Rai) Sur
- Tim Beiko
- Danno Ferrin
- Hudson Jameson
- Piper Merriam
- Daneil Ellison
- Wei Tang
- Greg
- Alex Beregszaszi (axic)
- Jason Carver
- Bob Summerwill
- Greg
- Edson Ayllon (notes)
