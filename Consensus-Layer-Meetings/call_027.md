# Ethereum 2.0 Implementers Call 27 Notes

### Meeting Date/Time: Thursday, November 7 at 1400 UTC
### Meeting Duration: 38 minutes
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/95 )
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=4_EGNG-Yek4)
### Moderator: Daniel Ellison
### Notes: Jim Bennett

---

# 1. [Testnet and Release Updates](https://youtu.be/4_EGNG-Yek4?t=264)

**Danny**
0.9.0 came out about a week and a half ago. There will be a few more PRs released as 0.9 releases - expect one this weekend. There are additional cleanups of pulling the custody bits out of attestations, as well as a few fork choice post-audit fixes. A Japanese researcher has found a couple of attacks on FFG and some pretty simple fixes that will be integrated. I'm working on getting these out as soon as possible, because I know this is the delaying component on moving towards larger testnets.

Clarification on the tests: we did have a number of ad-hoc interop test cases that we found while debugging multi-client testnets on the wire. These were for 0.8.3, and some had integrated them into their testing flows. Since then, we have built out handwritten tests that hit these test cases, so if you're passing 0.8.4 and 0.9, you are passing those tests, so you don't need to integrate those into your client anymore.

**protolambda**
Muskoka is up. We now need clients to consume thse inputs. In the process of deploying GO specs. The main goal is to be able to run the state transition on all the clients, so that arbitrary test cases can be run easily against all clients at once.

# 2. Client Updates

# A. [Nimbus](https://youtu.be/4_EGNG-Yek4?t=540)
**Mamy(Nimbus)**
This week, Nimbus is moving from 0.8.3 to 0.9.0, so depending on the commit you use, the genesis state might change due to the change in the beacon state, so Nimbus is not in consensus. Don't rely on the state during the migration from 0.8.3 to 0.9.0. Have updated docs with build instructions for Raspberry Pi. For the public testnet, we have a [common repository for Eth2 clients.](https://github.com/eth2-clients/eth2-testnets) and [guidelines for use.](https://github.com/ethereum/eth2.0-pm/blob/f1faca34b712b21602437b7627192cb9ba64edff/interop/deposit_contract_testnets/README.md) We are setting up infrastructures for public monitoring. A private Grafana dashboard will be open within the next few weeks.

Over the past two weeks, we have struggled with timeouts in CI. We solved that yesterday by resolving caching issues and moved from Appveyor to Azure pipelines for Windows testing. We also now have testing on ARM devices. Lastly, we moved completely to tarballs - we now only use LFS for our own files. We also resolved some bugs migrating to Nim 1.0, which was released last September. On the libP2p front, we had some updates on pubsub and gossipsubs. We will start to integrate native libP2p into the codebase and replace the GO libP2p daemon.

**Danny**
On those testnet standards under the Eth PM, is there a place for specifying the spec version that the testnet is targeting?

**Zahary**
Each testnet exists in a subfolder, and each subfolder has a README file in which you can describe which spec you are targeting.

# B. [Lodestar](https://youtu.be/4_EGNG-Yek4?t=788)

**Cayman**
For the past few weeks, we finished pulling out our state transition into a separate package, which is going to help people use it independently of Lodestar. We are almost done with a more robust initial syncing. We're in the process of moving from 0.8 spec to 0.9 and pretty close to finishing on that. We are refactoring our gossipsub because JS libP2p is going through a very large refactor from an older style of Javascript using callbacks to a newer style using promises. Hope that can be merged soon.

**Danny**
If you didn't see, there are a number of Eth2-related bounties at Eth Wateroo coming up. If you have any ideas for these, we will run them generally at the Eth Global Hackathons.

# C. [Parity](https://youtu.be/4_EGNG-Yek4?t=888)

**Wei Tang**
We fixed the interop issue we had since last time, and we also finished upgrading our beacon implementation to 0.9, and we just passed all the other tests.

# D. [Trinity](https://youtu.be/4_EGNG-Yek4?t=921)

**Alex Stokes**
We have exciting stuff in PRs that's waiting to be merged, including the state transition updates to 0.9 and the network updates from 0.8.4. We have a lot of good of work on node stability and pylibP2p stability. We had a really crazy performance improvement in PySSZ, backing persistent data structures. Work on separating out our validator client as a distinct binary. Looking forward to these testnets happening as soon as possible.

# E. [Lighthouse](https://youtu.be/4_EGNG-Yek4?t=982)

**Adrian Manning**
Working towards doing public testnets. Focusing on our Eth1 connectivity. Making changes to our CLI to make it more ergonomic so that it's easy to use when joining some of these testnets. We've been ramping up our testing on most of the aspects of Lighthouse and getting public use. We've implemented encryption for BLS keys and have a keystore for our validator keys. Passing test vectors for 0.9.0, but we still need to finish the update, which we'll do by early next week. We've been implementing slashing protection. We have a PR for slashing protection for the validator client, and we're looking to use SQLite for the database inside that.

# F. [Prysmatic](https://youtu.be/4_EGNG-Yek4?t=1064)

**Terence**
Pretty much the same update as everyone else. We fixed a few RPC-related bugs that users have been reporting. Our single client testnet is currently down as we update to 0.9. We finished 0.9 a few days ago and it looks like it will pass the spec tests for both state transition and SSZ. We're planning on relaunching our testnet by the end of the week, and in the process we are also working on aggregation. Working on slashing on both the protection and policing front.

# G. [Artemis](https://youtu.be/4_EGNG-Yek4?t=1126)

**Ben Edgington**
We've got some team changes. We're moving Artemis internally from incubation to the product side of Pegasus. I'd like to introduce Meredith, who is on the call, who did a lot of heavy lifting on our Ethereum 1 client. As far as development work goes, similar to everyone else, we're updating to 0.9. We're completing discv5 integration. We're working on REST management API, working on syncing, and the goal is to be able to hook up as soon as possible to some of these testnets that everyone is building.

# H. [Harmony](https://youtu.be/4_EGNG-Yek4?t=1186)

**Danny**
There's a unification between Harmony and Artemis in process, but Harmony is driving forward on some more research-related components.
Continuing to merge with Artemis team.

# 3. [Research Updates](https://youtu.be/4_EGNG-Yek4?t=1258)

**Cayman**
Yesterday, we had our [first meeting with the light client task force](https://youtu.be/aY4Qsk22IAE). Had a great Q&A with zsfelfoldi on the light client server incentivization framework that he's come up with. It's an hour long, so I'm going to see if we can get a bounty together to get a transcript.

**Justin Drake**
We've made some progress on the BLS standardization. There's a new hash-to-curve draft which is out, and this is the one I'm expecting to go into production with. There are also updated test suites. Herumi, the maintainer of the really fast BLS implementation, has agreed to do some work on the grant, so he'll be implementing this new hash function and helping out with Rust integration as the two first steps.

If we look into the future on Phase 2, there's been very good progress on the VDF project, and one of the big milestones is the RSA-MPC, which is hitting all performance targets. We're looking to hand over the Ligero that is implementing the MPC to auditors early next year and hope to do the MPC by mid-next year. It all seems to be working very well. Just generally, the space of groups-of-unknown-order, the cryptography seem to be blossoming. There are new groups-of-unknown-order rumored beyond the RSA groups and the class groups. Exciting stuff that's happening.

**Mamy(Nimbus)**
I have a question for Justin. Will it be integrated in Rust or in C or C++?

**Justin Drake**
I can add you to a telegram group that are helping with that integration.

**Dankrad**
We've made some efforts over the last couple of weeks to unify all bounties at [a central entry point, challenges.ethereum.org.](challenges.ethereum.org) We're expanding our programs there because we've seen some very good work come out of it.

**Greg Markou**
For the testnets coming up, I've been working on a metamask plugin that will have autodeposits built in to it to make it easier for users on the testnets. How much on the current Eth1 curve to the BLS curve?

**Carl(Ethereum Foundation)**
47-48 percent.

**Greg Markou**
Ok. Definitely not going to use it.

**Carl (Ethereum Foundation)**
I've put up three EIPS for for BLS key derivation, key path, and key stores:
(https://github.com/ethereum/EIPs/pull/2333)
(https://github.com/ethereum/EIPs/pull/2334)
(https://github.com/ethereum/EIPs/pull/2335)

# 4. [Networking](https://youtu.be/4_EGNG-Yek4?t=1805)

**Danny**
Anton from Harmony has been working on a simulator for GossipSub/FloodSub.

**Anton**
I am optimizing the code and seeing how many nodes can be simulated. For now, it looks like hundreds of thousands of nodes can be simulated. Not too fast. The work is still in progress.

**Danny**
No one from Protocol Labs is here. Any updates from Whiteblock?

**trentonvanepps**
No. Nothing too big this week that I know of. We're just continuing with adjusting our methodology for the libP2p testing.

# 5. [Spec Discussion](https://youtu.be/4_EGNG-Yek4?t=1925)
No discussion.

# 6. [Testnet Discussion](https://youtu.be/4_EGNG-Yek4?t=1953)

**Danny**
My general read on the past two weeks is that people are working on 0.9 and people are also working on getting some continued single client testnet stuff out there, and there's a lot of general intention to experiment with some multiclient behavior on different team's single client testnets in the coming two weeks. A more orchestrated testnet is not something I want to do until we have a 0.9 spec freeze.

I also posted an [issue on Eth2 PM yesterday](https://github.com/ethereum/eth2.0-pm/issues/98) that is a list of tooling and things that we want for testnets and people who say they are working on them. Please add some items to that list so we can figure out how to prioritize.

**trentonvanepps**
Does it make sense to put a testnet configuration with all the different parameters set in the specs, or is it too premature? Coul atht go with 0.9.1?

**Danny**
We had discussed isolating some of the signature domains and some of the versioning, so that might be desirable. At least in terms of shard counts, the intention is to generally to minimal and then step up to the mainnet.

**Cayman**
I think I saw in the chat someone was talking about changing the Eth1 follow distance.

**terence(Prysmatic)**
Prysm has changed this and the ejection balance. Follow distance has been changed from 1024 to 16, which is about fifteen minutes.

**Danny**
I'll look into making a modified config called small testnets that can make some of these adjustments.

**Greg MArkou**
Danny, do you want to go over the new PR with the deposit size?

**Danny**
Yeah. Long ago, the number of validators to start the chain was specified as about a half million. This was about a year ago. And then there was concern about a gatekeeper attack, in which someone with about a half million Eth quickly deposits, triggers the chain to start,
and then prevents new deposits from being processed. This attack was in the context of there only being an amount of depositers to trigger the chain start. Given that there is a genesis time, that mitigates a lot of the attack potential. Also, if a gatekeeper attack happened, it would be incredibly obvious, and it would be possible to use centralized coordination to remove an attacked from the chain. So I proposed in [PR 1467](https://github.com/ethereum/eth2.0-specs/pull/1467) how to reduce the chances that some whale could execute this kind of attack. Justin has some counter arguments in the PR.

# 7. [Open Discussion/Closing Remarks](https://www.youtube.com/watch?v=4_EGNG-Yek4)
It turns out Ben Edgington is also a Goerli whale.

## Next Meeting will be Thursday, November 21 at 1400 UTC

## Attendees

* Adrian Manning
* Alex Stokes
* Anton Nashatyrev
* Ben Edgington
* Brent Allsop
* Cem Ozer
* Carl (Ethereum Foundation)
* Cayman
* Chih-Chang Liang
* Daniel Ellison
* Danny
* Dankrad
* Greg Markou
* Herman Junge
* Hsiao-Wei Wang
* Ivan Martinez (Prysmatic)
* Jannik Luhn
* Jim Bennett
* John Adler
* Johnny Rhea
* Justin Drake
* kevin.mh.chia
* Leo BSC
* Mamy (Nimbus)
* Marin
* Mbaxter
* Mikerah Quintyne-Collins
* Nicholas Lin
* Nicolas Liochon
* protolambda
* Raul Jordan (Prylabs)
* Shahan Khatchadourian
* Terrence (Prysmatic)
* Tomasz Stanczak
* Trenton van Epps
* Wei Tang
* Zahary

## Links discussed in the call
