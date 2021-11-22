# Ethereum 2.0 Implementers Call 60 Notes 

### Meeting Date/Time: Thursday 2021/03/25 at 14:00 UTC 
### Meeting Duration:  30 min 
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/210) 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=Q0EbnFViJFk) 
### Moderator: Danny Ryan 
### Notes: Pedro Rivera 
### [Previous Call (59)](#NotInRepoYet) <!-- not in repo yet -->

-----------------------------
## Action Items

| Action Item | Description |
| ------------| ----------- |
| **60.1**    | Promote users to move from Pyrmont to Prater (through blog post, ETHStaker community) |
-----------------------------

## Intro ([1:50](https://youtu.be/Q0EbnFViJFk?t=110))
* **Danny Ryan** kicks the meeting off by briefly stating the agenda: Client updates, some Altair discussion, then Prater. He then shares the invitation to The Merge meeting taking place bi-weekly on Thursdays (next one on April 1st).

## Client Updates

### Teku (Anton Nashatyrev) ([3:04](https://youtu.be/Q0EbnFViJFk?t=184))
* Working on Altair adoption, most data structures almost ready, spec functions are on the way, and we can start to progress API changes.
* Updates into the latest reference test version are underway. Also support for choice tests was implemented.
* Started Prater, now looking for optimizations to make it run better.

### Nimbus (Mamy) ([4:22](https://youtu.be/Q0EbnFViJFk?t=262))
* We released this week v1.0.12 which adds Prater support. So users can try Prater with this release.
* Preparing major release with several performance improvements that were prepared for Prater but were not strictly needed.
* Peer management fixes took place.
* Have been testing slashing database refactoring. Quite satisfied after a month of testing; so, it will be enabled by default in the next release (coming in \~2 weeks).
* Phasing out `-dinsecure` flag. Reworking to use secure API by default.
* Started to work for Altair patches. We have a guide for a Nimbus Rocketpool out. Completing our API so we are aligned with the Eth2 API spec.

### Prysm (Terence) ([6:24](https://youtu.be/Q0EbnFViJFk?t=384))
* We released v1.3.4 on Monday. It added embedded genesis state, so users don't need to sync. Also added Prater support.
* In parallel working on a slasher design which is more efficient.
* Working on Eth2 API.
* On the hardfork... we are adding datastructures and config. We are trying to figure out the best path forward due to different of beacon state without too much addition of code.
* Looking into the merge effort to see how we can best integrate while studying the Lighthouse approach.

### Lighthouse (Adrian Manning) ([7:15](https://youtu.be/Q0EbnFViJFk?t=435))
* Playing with the merge effort. Managed to get a merge chain running with Lighthouse and kjashdf-us and verified our first transaction. 
* Last week a new release was done with big improvements to block production times, which hopefully will have an impact on the nubmer of lightblocks seen on Mainnet. Should be doing an analysis in 1-2 weeks, once enough users have updated to this latest release.
* Prater got lauched and seems to be doing well. 
* Doing decent progress on our fork handling logic. Not yet running the test vectors.
* Building out the Altair networking changes. Will have a release in the next week or so to improve handling of the time discrepancies between the beacon and the validating client.

### Lodestar (Cayman Nava) ([8:50](https://youtu.be/Q0EbnFViJFk?t=530))
* Got a new release 0.18 with Prater support. Found a whole host of issues to tackle.
* Still working on Altair-compatible beacon node to support multiple versions of the beacon state.
* While profiling, found another memory leak. This time in our remerklable style ssc lib. We found that subtrees can retain a reference to the parent tree, not letting the parent tree get garbage-collected, which is causing us to store a bunch of beacon states in memory.

## Altair ([10:24](https://youtu.be/Q0EbnFViJFk?t=624))

* **Danny** shares, for Altair there is an alpha.1 release and a small alpha.2, which cleaned up some naming and primarily fixed the test generators.
* **Barnabé** from RIG (Robust Incentives Group) at the EF did some analysis of the rewards and realized that the invariant that we are going for implies a base reward that's off (2% off target). So, there is some refactoring in the queue.
* Expecting an alpha.3 release probably around next week.
* With regards to planning, **Danny**'s opinion is we can't plan dates much until getting feedback from engineers. Will check-in async to see where we stand.

## Prater Status ([12:45](https://youtu.be/Q0EbnFViJFk?t=765))
* **Danny** mentions the lauch seems to be doing well. The most eventful item was probably the Nimbus protection that kicked in during genesis without doing nothing during a couple of epochs. Asks the group if there is anything the want to discuss around Prater.
* **Mamy Ratsimbazafy** suggests some sort of blog post must be made to clear up Pyrmont/Prater because maybe the communication wasn't clear enough. Pyrmont is meant for Devs mainly but users may be asking themselves what's happening to Pyrmont (e.g. if you want to test in your Raspi or PC). We need to tell them where they need to go. **Danny** voices his understanding that Prater is first and foremost for Devs but would become the defacto tesnet and it's also the desire not to keep two test nets running in the long term, which would imply a deprecation of Premont. **Mamy** comments that he would still like using Pyrmont in around 2 months to test. 
* **Danny** suggests to use Pyrmont  to test a live fork so if things go wrong it's not the worst thing because we're planning on killing it anyway. Then after we do that fork, we can do a test of non-finallity and have no more user guarantees. **Mamy** agrees. 
* **Danny** mentions one downside to the previous idea: the cost of running a bunch of servers. **Jacek Sieka** points out more downside: if users want to stake on Mainnet, where should they test their setup Today? To that, **Dany** suggests they move to Prater and that we talk with the ETHStaker folks to maybe push their community to begin doing that. He commits in the next blog post to mention that and also contact the ETHStaker folks and see if they can get that out in their channels. 
* It's softly agreed a couple of months of Pyrmont support is desired before deprecation.
* **Ben Edgington** emphasizes we should encourage people to exit "nicely" of Pyrmont if we want to have a stable enough period to test the fork. This brings him to share the fact that currently there are sporadic failures to finalize in the network. **Danny** supposes it could be happening in times when Client Teams are doing updates (since the network is assumed to have Client Teams majority). **Preston Van Loon** (Prismatic) mentions they can be influencing that, as sometimes they end up taking validators offline due to problems.  

## Research Updates ([20:08](https://youtu.be/Q0EbnFViJFk?t=1208))
* **Danny** re-iterates invitation to The Merge call. **Mikhail Kalinin** will anounce the merge call in the merge channel of Discord.
* **Mikhail** gives updates about the spec. There is a new PR that substitutes the "executable beacon chain" proposal. It's about making the consensus upgrade on the Mainnet and does not involve EVM interaction. Main difference is that instead of having an RLP stream in the beacon block body that represents the application block, we have the same stuff but represented by cc(?) structures. He invites to [take a look at it.](https://github.com/ethereum/eth2.0-specs/pull/2257)
* **Vitalik** shares updates on proof of custody. He mentions Yesterday we were talking about the possibility to MVC it. Might want to do a couple of days of DD first to make sure it's something that works much better in that dimension. He added he has another proposal to publish soon for how to limit the number of active validators to 2^19 or 2^20 or whatever we choose, and do it in a way that's just simpler than the existing proposals. [A doc exists](https://notes.ethereum.org/@vbuterin/validator_rotation_proposal).

## General Spec Discussion ([24:40](https://youtu.be/Q0EbnFViJFk?t=1480))
* **Vitalik** asks what the status is on the fork-choice-side changes. **Aditya Asgaonkar** comments they have a better proposal to fix the attacks found last year. He'll be sharing a proposal. It's in the outer fork choice only, so it can be rolled out at any point rather than having to couple it with the Altair hardfork (i.e. without rush)

## Closing
* Danny announces that **Protolambda** is organizing an effort in ETH global hackathon (mid-April to mid-May) to sprint on getting the merge proposal and maybe even launching a testnet, with the stretch goal of building sharding in. Invites any Team member to participate if interested. 

-----------------

## Attendees 

- Aditya Asgoaonkar
- Alex Stokes
- Ansgar Dietrichs
- Ben Edgington
- Cayman Nava
- Dankrad Feist
- Danny Ryan
- Hsiao-Wei Wang
- Jacek Sieka
- Justin Drake
- Leo (BSC)
- Mamy Ratsimbazafy
- Matt (Lightclient)
- Mikah Zoltu
- Mikhail Kalinin
- Nishant
- Preston Van Loon
- Protolambda
- Terence (Prysmatic)
- Trent Van Epps
- Vitalik Buterin
- Zahary

## Next Meeting Date/Time

Thursday, April 8, 2021, UTC 14:00.
