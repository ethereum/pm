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
| Berlin Timeline | 3rd Wednesday of March |
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


**Hudson Jameson:** We did pick a block number for Istanbul. Coindesk corrected their article on that.

- **Istanbul Block Number:** 9,069,000

When are clients releasing an update with the [Istanbul] block number attached?

**Tim Beiko:** For phase 2, within the next two weeks, mid-November.

**Danno Ferrin:** We'll have it out next week. The PR is in, so clients can run the dev code, but that's not something we want exchanges to do.

**Hudson Jameson:** The Ethereum Foundation and/or Ethereum Cat Herders are publishing a blog on the block number and what software to upgrade around when most clients update their download links.


## 2. Berlin


Links: [Berlin Meta EIP](https://eips.ethereum.org/EIPS/eip-2070)



### 2.1 Ice Age

Video: [[7:55]](https://youtu.be/aZ0S_oLSwhE)

**Alex Beregszaszi:** I just wanted to ask that for every EIP change it would be nice to record a decision in the meeting notes so EIP editors can simply execute on the meeting notes. This can help for outstanding PRs without seeking again for confirmation.

**Hudson Jameson:** Excellent. Yes, let's do that for the Berlin and others we talk about today if in final state.

**Tim Beiko:** A couple calls ago we said that the Ice Age would start kicking in next summer, please correct me if I'm wrong. We probably want an EIP in Berlin that kicks back the Ice Age.

**Hudson Jameson:** James Hancock decided to write that. Not a huge rush. We delay it the same time each time.

**Danno Ferrin:** That gives us a little over a year each time.


### 2.2 Tentatively Accepted EIPs

Video: [[10:24]](https://youtu.be/aZ0S_oLSwhE?t=624)


**James Hancock:** We should go through the accepted ones, formally have them done on the call.

**Hudson Jameson:** That sounds good. Do you have that list?

**Alex Beregszaszi:** The tentatively accepted lines were copied over from the Istanbul EIP. Whatever was part of Istanbul Part 2 has been just moved over. But there was no further discussion.

**Danno Ferrin:** When I did the PR for the meta EIP, I made sure to cross reference call 68 to make sure those were the EIPs we agreed on. I did cut the rest off because I saw that they weren't Berlin. I didn't update draft to accepted. Should we formally make 1671 accepted, which is the assemble meta EIP?

- [EIP 1679](https://eips.ethereum.org/EIPS/eip-1679 )

**Hudson Jameson:** That sounds good.

**James Hancock:** I have the accepted list. So the this is the EIPs from from the Istanbul hard fork, EIP 1679 the source of truth from that.  The included EIPs:
- EIP 152
- EIP 1108
- EIP 1344
- EIP 1884
- EIP 2028
- EIP 2200

EIPs are to be moved to accepted and final for integration in Istanbul which has begun for the client.

**Hudson Jameson:** I second that. We should probably have motions.

**Danno Ferrin:** Agreed.

**Hudson Jameson:** The Berlin the hard fork meta has links to all of the tentatively accepted EIPs.  None of them are final as far. We ll just go in order by number.

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

**Danno Ferrin:** Requires benchmarking against one of the clients.

**Alex Beregszaszi:** Gave an update on Gitter. For this and EIP-2046, benchmarks show some numbers needs adjustment. Benchmarks show some reduction can be made, but not to the degree of the original proposal. Benchmarks listed in the Ethereum Magicians discussions for those EIPs.  

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

**Hudson Jameson:** There has been some community sentiment that they don't want it in. It's hard to tell if it's a few loud voices, or a community majority. This is already in blessed state in my opinion.

**Tim Beiko:** I'm curious on perspectives on:
- Is this something we want the community to signal through their nodes whether or not they want it?
- Do we do a single ProgPoW hard fork?
If it raises risk of the network splitting, do we value keeping the network together?
- Do we not give it special treatment and group it with the other EIPs hoping nodes commit a full upgrade?

**Hudson Jameson:** I say we don't change it, unless high probability of a controversial hard fork where people choose. That's my opinion though.

**James Hancock:** My opinion is to not treat it differently than any other EIP.

**Piper Merriam:** I'm torn down on this topic. I'm willing to implement this in our client, if that's what everyone else wants. Otherwise, I have no desire to put energy towards it. Other things are higher priority.

If miners really want this, for shifting a portion of miner rewards towards core protocol development. Something also controversial.

**Greg:** We looked and haven't found technical problems.  We've said yes more than once.

**Hudson Jameson:** This one has blessing for sure.

**Tim Beiko:** We can leave it blessed. But there is some distance to go live, as most concerns are not technical.


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

Video: [[16:01]](https://youtu.be/aZ0S_oLSwhE?t=961)

Links: [EIP Centric fork](https://notes.ethereum.org/@holiman/S1ELAYY7S?type=view)


Some discussion occurred on what constituted `Blessed` status. Conclusion was, `Blessed` indicates no Core Devs has rejected an EIP as an idea, serving as a first pass before reassesment after an implementation has been prototyped before final inclusion. `Blessed` indicted an idea has been greenlit for continued work. Furthermore, concern was brought forward for Core Devs reviewing each EIP individually, suggesting a solution possibly including delegation may be required.

**Greg:** If you care about something, you'll put the work in it. If you need to push it to our level, fine, but in most cases I don't think we need to.



**James Hancock:** Going until July I think is going to be too much.  As far as windows for when Berlin would work, we use the third week of the third Wednesday of the month.  We could do April, May, or June.


**Hudson Jameson:** Do we want to discuss timelines today?

**Tim Beiko:** We probably should. Then decide when EIPs need to be ready based on that date.  

**Piper Merriam:** Can I pause this for a second? In our last core devs meeting, I remember us at least talking about doing the EIP centric process.  I was under the impression that in the EIP centric process we don't select EIPs.

**James Hancock:** That was also kind of one of the points that I was bringing back to around available time slots, deciding completion deadlines. The Ethereum Core Devs community can decide which EIP is integrated by which EIPs are completed in time.

Yes this is an EIP centric model, but we do know within March to June, we're gonna have some fork to have an update for the Ice Age. We can work backwards in deciding steps from a deadline.

**Piper Merriam:** An alternate option. Clients complete for the current pending hard fork, then signal support for the Ice Age Delay EIP. By setting a date that far, it feels like we're still using the old model. Under the EIP centric model, it looks like we don't set set fork dates, but wait for client signaling before setting dates. Am I misunderstanding?

**James Hancock:** That's fair. We have an upper bound, but no lower bound on how soon we can fork again. Testnets need to be launched, then time needs to allotted for clients to update. Then keeping it the same for implementors, to no to do many or too little.

**Tim Beiko:** One objection to the pure EIP centric model is one upgrade per EIP. There's some fixed overhead and coordination for having an upgrade (node upgrades, testnet updates, etc.).  A middle ground approach could be: We want to set a date for an upgrade, but not move that date based on single EIPs not being ready. The community can then see the deadline as a signal to prepare their EIP.

**Alex Beregszaszi:** Piper, what did you mean by clients signaling for the Ice Age EIP?

**Piper Merriam:** I was pulling that from memory, not currently at my computer.

**Hudson Jameson:** What I remember, we decide it how we normally decide on an EIP, with the addition of full spec, full conversation, and implementation began.

**Alex Beregszaszi:** My understanding is similar. The All Core devs would give an opinion on new EIPs. Then give approval that they are good to work on. Then, those who propose them must complete them. Then is perhaps the signaling from clients is their implementation.

**James Hancock:** Yes, the step of the client having and accepting PRs. Then the Core Devs approve to go into the fork.

**Hudson Jameson:** Perhaps this hybrid process from the last meeting would be to reconcile that there is an Ice Age, and setting timelines for when the Ice Age hard fork happens. For other EIPs, this may be less important. We also are considering the overhead of implementation, testing, and deployment by major providers.

We may to better specify the process.

**Piper Merriam:** The suggestion of the EIP centric model is:

1. Blessing
2. Implementation
3. EIP compatible clients for a given block
4. All Core Devs finalization. Implementation is done, testing is done, a block number for the fork can be chosen.


The block number contains one or many EIPs. But dates aren't set until implementations are ready. That's my understanding. It seems picking a date is the same process we've used before.

**James Hancock:** Two conversations are happening. Among Core Devs: When are we going to fork. Core Devs to the Community: There's a realistic deadline of June where completion is required. Then there's a preparation period of 3 months needed for testnets to be live. With those two dates, April, May, and June is available for Istanbul. Keeping forks to a third Wednesday of the month, there are 3 third Wednesdays to select from.

One of them needs to have the update for the Ice Age. All other EIPs, we don't want to decide a date. By keeping inclusions once a month, we can decide whether to postpone an EIP for it to go with another which goes together. We want to avoid one fork per EIP, as well as waiting significant time to include several EIPs, as both limit implementations, testing, etc.

**Hudson Jameson:** We're not picking a date. We're being pragmatic in some of the possible dates, considering the overgead.

**Piper Merriam:** That works with me. I would propose the soonest, as we are just starting this new process.

**James Hancock:** Yes. What date is the soonest? March?

**Piper Merriam:** That is reasonable.

**Hudson Jameson:** Agreed. Realistically, for most EIPs, we can decide, implement, and do tests for an EIP within a 3-4 week period.

We also decided the champion of an EIP will be the coordinator for testing, right?

**James Hancock:** Yes.

**Hudson Jameson:** Wei said they wanted to remove their name from some they have been championing. Did you have someone in mind to take over the EIPs you were championing? The account versioning EIP is a prerequisite to other EIPs others were talking about, correct?

**Wie Tang:** I won't be able to champion as I won't have enough time to do all the coordination, and would be too political for me. I don't have a replacement Champion. It would be better to ask All Core Devs and look for a champion, or alternatively remove them from the Berlin Hard Fork.

**Hudson Jameson:** For the next two weeks, I propose we keep them to see if there are replacement Champions.


Video: [[38:49]](https://youtu.be/aZ0S_oLSwhE?t=2329)


**Danno Ferrin:** Are we tracking EIPs categorized by forks? Or are they in their own grouping separate from forks?

**Hudson Jameson:** Not scraping it completely, it's taking it off the meta. Not tentatively accepted anymore, and that's an official decision.

**Danno Ferrin:** Do we need a separate tracking process for EIPs, independent of the fork?

**Tim Beiko:** We could have a blessed section in the meta, in addition to tentatively accepted.

**James Hancock:** A way to reconcile may be not to have a fork meta list, but a list of blessed EIPs.

**Tim Beiko:** An EIP status on their website?

**James Hancock:** I don't know if its better for it to be a status, or to have a new list similar to the Hard Fork list, but as a Blessed list, which updates.

**Hudson Jameson:** I that idea. In EIP 1, there's a status and a category of EIP that it fits (informational and active).

**Greg:** I thought tentatively accepted is the same as blessed.

**James Hancock:** It is. What's missing is a list for the community to look at for what is a Blessed EIP.

**Hudson Jameson:** Blessed EIPs no longer mean an attachment to a fork with the new process.

**Greg:** I thought Tentatively Accepted list were those intended to go into a future fork when ready. I don't see a need for another category.

**Tim Beiko:** No, it's a renaming.

ç Tentatively accepted is vague without a fork attached.

**Tim Beiko:** We just came with the term this summer.

Video: [[1:10:53]](https://youtu.be/aZ0S_oLSwhE?t=4253)

**Alex Beregszaszi:** Further discussions on those EIPs should stop until further spec and an implementation.

**Tim Beiko:** Unless a Champion joins and starts a discussion, we discuss, otherwise, we don't discuss specific EIPs?

**Tim Beiko:** That would make things easier.

**James Hancock:** Should the blessed state be done in the All Core Devs call, and be linked in the notes?

**Danno Ferrin:** Can we take a more neutral name for blessed (ie. preliminary approval)?

**James Hancock:** We can do greenlight.

**Jason Carver:** Greenlit sounds too affirmative, implying it's finalized.

**Tim Beiko:** Controversial, but how about Tentatively Accepted?

**Danno Ferrin:** Provisionally Accepted?

**Tim Beiko:** Bitcoin has Concept Acknowledged.

**Hudson Jameson:** Provisionally Accepted is good. If there's a question, someone will write up the explanation.

**Alex Beregszaszi:** In addition to Provisionally Accepted the name change, we decided on forming a list?

**Danno Ferrin:** In addition to Provisionally Accepted, we should list new EIPs live on the new EIP process. When a Champion has a prototype ready, they should upload it there. In addition to security reviews. Also, an informational EIP covering this new model.

**Hudson Jameson:** Yes, possibly under EIP-1. ERC content will remain the same until updated.

**Alex Beregszaszi:** Is the decision to create a new EIP with the status of `Active`, which lists `Provisionally Accepted` EIPs?

**Tim Beiko:** The Champion of each EIP should be making PRs to update that list.

**Danno Ferrin:** I wonder how many of these should be within this new EIP, having it be one giant collection of EIPs.

**Tim Beiko:** For visibility, it may be good to have a master list. There is value without it being cluttered. At most 5-6 bullet points per EIP.

**Danno Ferrin:** Sounds reasonable.

**James Hancock:** Some have requested EIPs be sorted by most ready.

**Alex Beregszaszi:** I would be OK it being in the PM repo as well.

**Hudson Jameson:** Jason Carver suggested  `Eligible for Inclusion` instead of Blessed.  

**Danno Ferrin:** Eligible may communicate the intent better.

**Hudson Jameson:** Let's include that.

**Pooja Ranjan:** The Ethereum Cat Herders can help maintain the list of the `Eligible for Inclusion` list.

**Hudson Jameson:** Let's hold discussion to where the list is listed in another call.

**James Hancock:** I'm also unsure if it could fit in the PM repo.

**Pooja Ranjan:** We should start the list, and then think about where to put it.

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
