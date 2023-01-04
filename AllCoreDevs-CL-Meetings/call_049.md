# **Ethereum 2.0 Implementers Call 49 Notes**

### **Meeting Date/Time: Thursday 2020/10/1 at 14:00 UTC**

### **Meeting Duration: 1 hr**

### [**GitHub Agenda**](https://github.com/ethereum/eth2.0-pm/issues/184)

### [**Audio/Video of the meeting**](https://youtu.be/IRWQUQfq7yQ)

### **Moderator: Danny Ryan**

### **Notes: William Schwab**

--------------------


# **Contents**

- [1. Testing and Release Updates](#1-testing-and-release-updates)
- [2. Spadina post mortem](#2-spadina-post-mortem)
- [3. Client Updates](#3-client-updates)
  - [3.1 Prysm](#33-prysm-terence)
  - [3.2 Nimbus](#34-nimbus-mamy)
  - [3.3 Lodestar](#36-lodestar-cayman)
  - [3.4 Lighthouse](#31-lighthouse-mehdi)
  - [3.5 Teku](#32-teku-ben-edgington)
- [4. Research Updates](#4-research-updates)
- [5. Networking](#5-networking)
- [6. Spec Discussion (none)](#6-spec-discussion)
- [7. Open Discussion/Closing Remarks](#7-open-discussion-closing-remarks)

## Action Items

Action Item | Description
--|--

- **49.1**: Breakout room conversation about best practices and stable release to happen Monday or Tuesday

------------------------------

#
# **1. Testing and Release Updates**

| **Video** | [1:40](https://youtu.be/IRWQUQfq7yQ?t=100) |
| --- | --- |

**Danny Ryan**: I am personally working on a v1.0 candidate, branch WIP PR including BLSv4 update some of the networking things. I believe **protolambda** has been continuing on the networking test stack, but interrupted by other higher priority items. As for the fork choice tests, still sitting in the repo.

**protolambda**: A little bit ago was working on YAML files define different clients and setup and have integration testing, but will stop due to other higher priorities. This will take more time and will go through disclosures.

**Mehdi**: Just pushed a blog post with latest updates in Beacon Fuzz. Doing some BLS differential fuzzing, can now disclose bugs that have been found since they've been patched. We identified two critical bugs in Blst, which effectively allowed signature malleability (_notetaker's note_: may have heard incorrectly), they've been patched, we're all good. So far we've only focsused on Rust bindings, hope be moving on to other languages in the next few weeks.

We've been running in a dedicated AWS instance. Caught two minor discrepencies between clients on slashing processing. They are not directly exploitable per se, but very interesting, see blog post. We're seeing less and less exploitable vulnerabilities, so good job everyone.

We've also added Teku to Beacon Fuzz v2, not straightforward, but got there in the end. Thanks Nat and thanks to the Teku team.

We plan on starting work on our own fuzzing engine.

**Danny**: What's the advantage of a custom engine?

**Mehdi**: It allows us to rotate and cycle through beacon states. The way iut works at the moment with libfuzz and AFL iswe're only mutating the SSZ container that we're processing, so if you're fuzzing the process attestion functionss for example, you're effectively mutatuing an attestation container, and by having our own engine we can dictate how often we want to rotate and swap beacon state. Another advantage is speed, we'll be able to load in memory and not have to perform I/O for each operation, and will be able to have structural fuzzing and mutatable based fuzzing in the same structure. Will be working on this for the next few weeks.

**Jacek**: Which implementations can be used?

**Mehdi**: We're going to focus on Blst, seems to be the most accepted across clients, the idea is to make sure the bindings are the same across all languages. The current fuzzers that we have exercise Apache Milagro, Blst, and the ZCash library.

**Mamy**: I think Lodestar is using MCL **Mehdi** wants to add Heroumi, didn't have time yet, hope they get to it.

# **2. Spadina post mortem**

| **Video** | [7:29](https://youtu.be/IRWQUQfq7yQ?t=449) |
| --- | --- |

**Danny**: Started looking very stable starting 70 epochs in, but we all know that there was 1/3 participation in genesis through the compounding of a number of errors in the outer configuration and release process. I don't know if we need to belabour the point right now, but the result is that we will do this again, Zinken. Blog post soon, launchpad should be up today, intended genesis on Monday the 12th. There's always the chance validators won't turn on, don't think that's what we're looking for, we're looking for a lack of errors reported, and with Spadina if you were monitoring Discord channels, there were a number of validators who had difficulties (not from personal issues). Afri, you had thoughts for a call outside this, could you give a quick rundown if you're available?

**Afri**: A couple of weeks ago I mentioned that clients need stable release management so we can have code freeze and work towards hardeining, and thought of talking best practices, work towards stable releases, wanted to suggest a breakout room.

**Danny** concurs, suggests early next week, and coordinating to see when the best time is.

**Afri**: We saw that two day genesis delays is short, and wondered if there were thoughts about increasing the default genesis delay in future networks.

**Danny**: In Zinken will do 4 day, partially to have a longer delay, partially not to keep things moving and not have a 7-day delay. The 1.0 candidate branch based on experience is going to move towards 7-day delay, any rehearsels between now and genesis I would suspect 7. The two day scramble is not great.

**Mamy**: There's also user confusion about the delay. **Danny** agrees that this needs good comms, says blog post hopes to clarify, has dates noted explicitly.

**Dankrad**: Maybe client teams need to think about how they stay in touch with users in case there is a problem, and can notify users to update if they need to.

**Danny**: In a few different conversations with staking providers on different chains, they've mentioned that there is a lot of noise (GitHub, Discord, Twitter), but that email is often very monitored, so maybe email is a good way to communicate issues.

**Dankrad**: Maybe display the list on startup of the client, to remind that it's essential if you're serious about staking.

**Hsaio**: I collected some feedback from the Spadina launch, linked below, thanks for giving feedback and input to improve the proces, feel free to edit. Also thanks to ? and the Ethstaker Discord that suggested a checklist for stakers to check what they have to do before genesis is generated and/or after genesis is generated. The EF researchers are drafting the checklist and hope to share with the client teams maybe next week.

**Action Items**
**49.1**: plan on breakout call Monday/Tuesday to talk about best practices

#
# **3. Client Updates**

| **Video** | [15:20](https://youtu.be/IRWQUQfq7yQ?t=920) |
| --- | --- |

## **3.1 Prysm (Terence)**

We put out a postmortem on Spadina and we shared it, can check for the link on Discord thought we could have been more prepared in terms of docs, better comms, more vocal to stakers, so we created a general readiness checklist, shared with client teams. Updated spec to 12.3, running on master, added weak subjectivity checkpoint support, import block root and epoch, when the node syncs to that point, and say the block was different, it will fail right away. The voluntary exit feature is ready, feel free to try that out. Also got into our second round of audits, getting feedback, fixing bugs, and you can see our test suite. So just general bug fixes.

## **3.2 Nimbus (Mamy)**

Last audit phase, now we have the fix review scheduled in 2 weeks. Significantly improved stability, and according to ethstats.io, Nimbus is using the least memory on average. We're also in a heavy round of polish so that UX is significantly approved,  getting into logging and disk space. Like Prysm weak subjectivity is a work in process, living in a PR. We also updated the collaborative repo with some Medalla checkpoints so that it can be tested.

## **3.3 Lodestar (Cayman)**

We tried to participate in a small way on Spadina (4 nodes) and our progress is that the node isn't stable, so we weren't able. Created genesis properly, but couldn't stay up to the head. We added weak subjectivity chain start where you can pass in a finalized state and start from there. Finished standard API, doing a lot of refactoring, adding custom errors and cleaning things up, and moving forward still in progress are gossipsub 1.1 integration, not done, almost there, slashing protection interchange, and dist v5.1 upgrade.

**Danny**: Do you have an intuition about the bottlenecks in syncing Spadina?

Yes, our syncing strategy hasn't been too great. We haven't really known what was happening to the blocks as we were feeding them in. Now that we're getting proper errors, it should be easier to know, okay we don't actually have a parent, can try to do a parent sync backwards, before we didn't have enough information to make a smart syncing algorithm, but now there are errors, rough peer scoring, should be easier to revisit the whole algorithm.


## **3.4 Lighthouse (Mehdi)**

Spadina went well, you can see from dashboard, only hiccup is that at least one user didn't setup their datadir correctly, and was still using the Medalla setup. We are working towards pre-mainnet audits from Trails of Bits and NCC, both starting next week. We're planning a v0.3.0 release, includes standard API, partial implementation is ready, Paul is working towards the full implementation. It will also include the validator client API consumed by web user interface. We'll incorporate a new directory structure which should mitigate the hiccup mentioned earlier. Also will include the slasher interchange format that Michael has been working on. Herman has been working on a remote signoff hoping to integrate that as well. Same as other clients we've been working on weak subjectivity verification, and some caching for validator keys to mitigate the extensive script loading times with high validator counts. Networking: 0.2.3 Age has implemented v0.5.1 up to the changes made today. We want to do more interop testing before. We've been testing gossipsub 1.1 scoring parameters on Medalla and Spadina. Age also finished UPNP support a few hours ago, and have been fixing spme sync bugs.


## **3.5 Teku (Ben Edgington)**

We've been working on discovery v5.1, nearly done, almost there. Lots of work on weak subjectivity, hidden CLI options to handle the checkpoints. We have internal weak subjectivity checks in place, we check the sync against a checkpoint, check that our peers are consistent with the checkpoint, handle the case that he last finalized state is outside the weak subjectivity period. Next step is to sync from a given checkpoint state itself. We've been implementing validator performance metrics in our console for immidiate feedback. Also Spadina launch prep. Got audit report from Quantstamp yesterday, still digesting, nothing too scary. Next steps are to finish the standard API and finish up having our validtors split out, and bring it up to production level . Our Australians seem to be on holiday, so we've been alittle less productive than usual.


#
# **4. Research Updates**

| **Video** | [24:27](https://youtu.be/IRWQUQfq7yQ?t=1467) |
| --- | --- |

**Danny**: On Phase 1 spec, there's still a PR, we're going to leave it out of dev and master until a 1.0 release, but are now generating Phase 1 tests, out in last release, check if you're following progress.

**Mamy**: About Phase 1 tests, they made us an issue on Azure since they take 3GB, and it sends us over budget. So if you want to use Phase 1 tests, maybe it's better to separate from Phase 1.

**Danny**: This highlights a fundamental issue about the structure of the tests, about how especially with start states there's a lot of duplicaiton, and we're hitting the point where it becomes a problem. We may spend time after Phase 0 launch considering structure, maybe having a library and reference start states instead of dumping them in every test. Won't happen in next two months.

**protolambda**: An immediate solution is to compress the states since they contain a lot of zeroes.

**Leo BSC**: We continued work on a network crawler based on Rumor, link posted below. We get a number of peers and get deserialized messages from topics. We've found a couple of small bugs, already commented to proto, already fixed. We also proposed some features in gossip messages, we are working on that currently.

**Danny**: On Eth1/Eth2 merge have like a 3- or 4-week hiatus, but we've identified the next 5-6 items to dig into in R&D, will probably write in ethresear.ch.

#
# **5. Networking**

| **Video** | [28:45](https://youtu.be/IRWQUQfq7yQ?t=1728) |
| --- | --- |

**Danny**: Still movement around the 5.1 spec, I know that they're trying to get it merged and the wire format completed, keep your eye on there so you can give feedback and do interop testing.

#
# **6. Spec Discussion**

| **Video** |
| --- | --- |


No discussion.

#
# **7. Open Discussion/Closing Remarks**

| **Video** | [29:45](https://youtu.be/IRWQUQfq7yQ?t=1785) |
 |
| --- | --- |

**Danny**: I'm going to put out a blog post about Zinken today, and we'll plan things next week, and plan on a genesis the following Monday, the 12th.

--------------------------------------

# **Appendix**

## **Resources Mentioned**
- https://github.com/ethereum/eth2.0-pm/issues/184 
- https://blog.sigmaprime.io/beacon-fuzz-08.html
- https://notes.ethereum.org/w4E0FB4nSzWPRj9pEeguhQ 
- https://github.com/leobago/BSC-ETH2/tree/master/rumor/medalla-crawler 


## **Attendees**

- Aditya Asgaonkar
- Afr Schoe
- Alex Stokes
- Ben Edgington
- Cayman Nava
- Dankrad Feist
- Danny Ryan
- Hsiao-Wei Wang
- Jacek Sieka
- Justin Drake
- Leo BSC
- lightclient
- Mamy
- Mehdi Zerouali
- Nishant
- Protolambda
- Raul Jordan
- Sacha Saint-Leger
- Shayz
- Terence (prysmatic)
- Vitalik Buterin
- William Schwab

## **Next Meeting Date/Time**

Thursday, October 12, 2020, UTC 1400
