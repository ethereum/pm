# Ethereum 2.0 Implementers Call 15 Notes

### Meeting Date/Time: Thursday 2019/3/28 at [14:00 GMT](https://savvytime.com/converter/gmt-to-germany-berlin-united-kingdom-london-ny-new-york-city-ca-san-francisco-china-shanghai-japan-tokyo-australia-sydney/mar-28-2019/2pm)
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/35)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=bC4v_a-gcrs)

# Agenda
1. Testing Updates [_(1:05)_](https://youtu.be/bC4v_a-gcrs?t=65)
2. Client Updates [_(2:40)_](https://youtu.be/bC4v_a-gcrs?t=160)
3. Research Updates [_(16:49)_](https://youtu.be/bC4v_a-gcrs?t=1009) 
4. Network Updates [_(19:10)_](https://youtu.be/bC4v_a-gcrs?t=1150)
5. SSZ/SOS update from Piper [_(24:34)_](https://youtu.be/bC4v_a-gcrs?t=1474)
    * [ethereum/eth2.0-specs#787](https://github.com/ethereum/eth2.0-specs/pull/787)
6. Testnets progress,roadmap,PM [_(31:26)_](https://youtu.be/bC4v_a-gcrs?t=1886)
7. Spec discussion [_(51:26)_](https://youtu.be/bC4v_a-gcrs?t=3086)
8. Open Discussion/Closing Remarks [_(56:00)_](https://youtu.be/bC4v_a-gcrs?t=3360)

# 1. Testing Updates
* _Notes:_
  * On the PY tests of the executable spec, continuing to fix bugs, updating the spec. Most of the new bug fixing will make it into the next release. 
  * Protolambda for the next chunk of time working full-time on testing, testing infrastructure, fuzzing, more randomized inputs, etc. And expect a lot of little bugs to be flexed out in the next couple of weeks. 
* Jannik [_14:48_](https://youtu.be/bC4v_a-gcrs?t=888): Working on getting the ssz and hash tree vectors up. SSZ tests should be up to date now.
# 2. Client Updates
* Parity - Wei Tang [_(2:46)_](https://youtu.be/bC4v_a-gcrs?t=166)
  * Passed all the state tests from the repo 
  * Right now, trying to do the factoring and trying to integrate continuing runtime back to the old existing runtime to do the integration
  * (Spec 0.5.0 tests) 
* Lighthouse/Sigma Prime - Paul Hauner [_(3:49)_](https://youtu.be/bC4v_a-gcrs?t=229)
  * Been syncing blocks across the network using Rust libp2p
  * On spec 0.5.0
  * Doing block propagation by gossip sub
  * Using a slightly modified version of Matthew Slippers protocol
  * Will be running  a short-lived, private, single client testnet in the next couple of days.
  * Looking to swap from [GPL2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) to [Apache2](https://httpd.apache.org/)
* Lodestar - Greg Markou [_(4:58)_](https://youtu.be/bC4v_a-gcrs?t=298)
  * About to PRN their first rough plumbing of validator client, and hoping to spin up what would be like a single client situation processing blocks. And get that spun up on multiple Lodestar clients
* Pegasys - Akhila [_(5:45)_](https://youtu.be/bC4v_a-gcrs?t=346)
  * Beacon chain visualizer is talking live to the Artemis client
  * Protesting attestations correctly during both block and epoch processing and thus finalizing blocks and epochs. 
  * Artemis is up to date with version 0.4 of the spec and version 0.2 of the Hobbits wire protocol. 
  * Currently working on implementing RPC methods for [request block routes], [request block headers], and [request block bodies]
  * Hoping to be running on a WhiteBlock testnet in the next week or so.
* PyEVM/Trinity - Hsiao-Wei Wang [_(6:37)_](https://youtu.be/bC4v_a-gcrs?t=401)
  * Deposit contracts version 0.5.1
  * beacon chain testnet devp2p layer is having progress
  * Deposit contract repo. Will now have releases out simultaneously with the main release, so if the API or anything changes on that end you can more sanely version those together.
* Nimbus - Mamy [_(7:38)_](https://youtu.be/bC4v_a-gcrs?t=458)
  * Updated to the latest BLS and test vectors from last week.
  * Implemented 0.5.1 spec
  * More logging to help debugging
  * state pruning pending
  * Optimizing low-hanging fruits (too long processing that didn’t fit into a slot, we even switched to 30sec slots for testnet)
  * Starting to integrate state tests:
      * first step loading the YAML validator config and generating a genesis state from it
      * second step (not done) loading the beacon state from the YAML files
      * third step: hash our genesis state and compare the hash with the YAML beacon state
  * Several bug fixes in networking and underflows (raised a potential spec bug in the specs repo)
  * Implementing monotonic timers in our async framework to avoid clock drift
  * Libp2p IP utilities and architecture research
  * For now we use RLPx
  * With regards to the Nimbus testnet status:
      * development testnet on AWS this week with instructions in a blog post and our repo. We reached out to non-Nimbus Status colleagues and a couple people in the Nimbus Gitter channel, that manage to install, run the client, connect and sync successfully.
* Harmony - Mikhail [_(10:31)_](https://youtu.be/bC4v_a-gcrs?t=631)
  * Issues with crosslinks processing: rework needed, will open up a PR
  * Worked on some consensus layer optimizations
  * Been working up updating the spec to version 0.5.1. This work is almost done
* Prysmatic - Raul [_(12:18)_](https://youtu.be/bC4v_a-gcrs?t=738)
  * Lots of work regarding testnet
  * monitoring tools
  * can survive restarts
  * people can connect from the outside
  * https://medium.com/prysmatic-labs/ethereum-2-0-serenity-testnet-update-closer-than-ever-259cace9a1b1
* Yeeth - (Not Available)
# 3. Research Updates
* Justin Drake - [_(17:00)_](https://youtu.be/bC4v_a-gcrs?t=1020)
  * Have been tons of simplifications of the spec. Specifically a bunch in phase0
      * Latest one is regarding the withdrawal process, which is both a better design and simpler
      * also a better and more simple design by removing the exponential back-off mechanism that we had in phase0
   * Other good news, is there is progress being made on phase1. Phase1 as a spec will be split into two parts:
      * Part number one will specify the shard blocks and the structure of the blocks and the structure of the attestations of the shard and the fork choice rule. 
      * Part two, in a separate document, there will basically be updates to the beacon chain regarding the custody game. 
      * going through edge cases now
   * Guess is we'll be able to finalize the phase1 spec not too long after finalizing the phase0 spec.
* Vitalik - [_(18:35)_](https://youtu.be/bC4v_a-gcrs?t=1115)
  * Justin mostly alluded to most of it. Vitalik has been working with simplifications. Just recently put up a PR for replacing the withdrawal queue with an exit queue.
* Research team will be in EDCON, and it's probable that they will have a draft ready of handled protocol data.
# 4. Networking updates
* Felix: [_19:12_](https://youtu.be/bC4v_a-gcrs?t=1152)
    * ENR spec was accepted in the last All Core Devs meeting, so the spec is being moved over to the devp2p repo. 
    * On the discv5 side, they solved the packet signature problem discussed in the last meeting. As a brief recap, there is this issue that if you have multiple nodes using different crypto systems for their node indentity, then there was a big question about how they could authenticate each other's packets. And in the github issue, there is now a pretty good solution using [HMAC](https://en.wikipedia.org/wiki/HMAC). That is being implemented right now. So no code to share as of yet, but it is progressing.    
    * RLPx v6
* Matthew Slipper: [_21:39_](https://youtu.be/bC4v_a-gcrs?t=1299)
* Zak (Whiteblock): [_22:07_](https://youtu.be/bC4v_a-gcrs?t=1327)
    * Been working with Artemis, and also working with Lodestar. Been focusing on getting the clients to talk to one another before working on any interoperability type of tests. So that's kind of what we've been focusing on. 
    * Matthew Elder: [_22:50_](https://youtu.be/bC4v_a-gcrs?t=1370) talked about he and and Antoine had finalized the Hobbit 0.2 spec. Stripped down to an envelope format so it's agnostic to anything else that's going on in the community. Scoffold until libp2p is there
* Raul (Protocol Labs): [_23:23_](https://youtu.be/bC4v_a-gcrs?t=1404) 
    * Creating an area for implementers and contributors. So that discussions can engage and better serve any questions 
# 5. SSZ/SOS update from Piper
* PR [#787](https://github.com/ethereum/eth2.0-specs/pull/787) in eth2.0 specs repo. 
* Updating the ssz serialization spec to include an offset based mechanism that was originally proposed by Peter of the Geth team.
* This makes essentially, dynamically, looking up data within a serialized object have it's constantly fast. (log-in) for indexed look ups. And reduces the overall serialized size of ssz objects by a small amount by ditching the length prefix.
* In general, makes the format more useful to reason about objects within context like the EVM or other resource constrained areas.
* Piper's intuition says that this also works as a viable ABI encoding, or smart contracts. Which would give us a unified coding format for how we send objects across the network. How we encode objects for consensus data, and how we communicate objects into things like smart contracts. 
* In general, there seems to be some consensus around adopting this as the update to what ssz serialization looks like. Would be interested in getting other people's feedback.
* Plan would be for this to effect in 1 or 2 releases of the eth2.0 spec. Not something that would be dropped in immediately.
* One thing that was proposed, and that we generally have rejected, is including a linked prefix and the intent behind that is to have some sort of foraerds compatibility, in the ability to have extra fields to be added to objects and still have them be somewhat backwards compatible. And this was rejected because it adds ambiguity to the serialized representation of these things. Opting/leaning towards a very strict set of rules for serialization objects.
* And for any context, it took Piper about a day to update the python implementation of ssz to this spec. 
# 6. Testnets progress,roadmap,PM
* Mikerah proposed bringing in the cat herders to potentially help with PM, as we move towards more public testnets. 
  * Danny discussed that he is of the opinion that there are no two teams that are ready to target interoperability with another client and that it will be a waste of time and resources to do so before (1) the clients in question have a long standing single testnet, (2) the clients in question target the same exact release of the spec, and (3) the clients in question pass all consensus test vectors related the release.
  * He is also of the mind that these early interop experiments should not be a large organized effort and should instead be teams one on one working with each other. Only once we have ironed out some more isolated 1 on 1 client testnets should we begin to target a general purpose, long-standing, multi-client testnet.
* Some of the cat herders joined the meeting. Since they have some learning to do, Mikerah invited them to the call. And everyone is excited to have them. They have begun to do some work on the 1.0 chain stuff.
* Pooja Ranjan timed in, saying that they would be happy to help with any requirements teams may have.
* Ultimately, the idea is to have a multi-client test net long-lived that targets a single specific version that we invite people in the community to participate in. 
* As an aside, people should check out Cosmos' Game of Sigs, where people came and tried to break some of the economic considerations of the testnets. In an attempt to gamify the testnets.
* Lane reached out and discussed that, if any teams feel like they (even internally) could use a hand at project management or with organization, to reach out to the cat herders at any time.
* Jacek asked [_37:40_](https://youtu.be/bC4v_a-gcrs?t=2260) if it was meaningful to have a testnet before libp2p?
  * Danny: Think one would run into some issues when gossiping large amounts of data. Especially when you hit a reasonable amount of validators. Lean in the direction of getting libp2p before we have multiclient testnets. Although he continued to describe that that is defintiely debatable. 
# 7. General spec discussion
* Danny: Found a bug related to some genesis stuff. Over the past week, have been leaning back in the direction of genesis slot 0. And putting in explicit boundary conditions. 
  * This became a little more appealing now with testing and with an executable spec. So this becomes a little bit simpler to integrate into the spec. So Danny is going to do an exploratory PR to see a change in complexity from moving back to genesis slot 0. 
* Justin: We might/probably will split off the fork choice rule for phase 0 in a separate document. 
# 8. Open Discussion/Closing Remarks
* Danny discussed that a number of them will be meeting in person in Sydney on April 9th. 
* There will be 3 breakouts in the morning and 2 in the afternoon (would like to make that 3). General topics:
  * Phase 2/WASM/state execution 
  * Networking (networking protocols in the morning. Afternoon perhaps network aggregation strategies)
  * Testing
  * Lightclients
  * Testnets
* Mamy chimed in, saying that for those that can't go to Australia, if it would be possible to film the breakouts.
  * Danny: Yes, attempting to figure out a good remote participation strategy. Where these breakouts will have some sort of call-out capability. 

# Links shared during meeting
* https://gist.github.com/jannikluhn/92cbc8bf18e65672a91fc0c1ec322d66
* https://www.github.com/ethereum/eth2.0-specs/pull/787
* https://docs.libp2p.io/
* https://notes.ethereum.org/oGP2JMPpTZC7h0GW3InPLA#

# Attendees
* Danny Ryan (EF/Research)
* Ameen Soleimani (Spankchain)
* Adrian Manning (Lighthouse/Sigma Prime)
* Akhila Raju (Pegasys)
* Alex Stokes (Lighthouse/Sigma Prime)
* Antoine Toulme (ConsenSys)
* Anton Nashatyrev (Harmony)
* Vitalik Buterin (EF/Research)
* Ben Edgington (PegaSys)
* Carl Beekhuizen (EF/Research)
* Cem Ozer (PegaSys)
* Chih-Cheng Liang (EF/Research)
* Daniel Ellison (ConsenSys)
* Diederik Loerakker (Independent)
* Felix Lange (fjl) (EF/geth)
* Fredrick Harrysson (Parity)
* Greg Markou (ChainSafe)
* Hsiao-Wei Wang (EF/Research)
* Ivaylo Kirilov (Web3 Labs)
* Jacek Sieka (Status/Nimbus)
* Jannik Luhn (Brainbot/Research)
* Jarrad Hope (Status)
* John Adler (ConsenSys)
* Jonny Rhea (Pegasys)
* Justin Drake (EF/Research)
* Kevin Mai-Hsuan (EF/Research)
* Lane Rettig (EF/Research)
* Leo (BSC)
* Mike Goelzer (Protocol Labs)
* Luke Anderson (Lighthouse/Sigma Prime)
* Mamy Ratsimbazafy (Nimbus/Status)
* Matthew Elder (Whiteblock)
* Matthew Slipper (Kyokan)
* Mikerah (ChainSafe)
* Mikhail Kalinan (Harmony)
* Nicholas (Hsiu-Ping) Lin (EF/Research)
* Nicolas Gailly (PegaSys)
* Nishant Das (Prysmatic)
* Olivier Begassat (ConsenSys)
* Patrick MacKay (Runtime Verification)
* Paul Hauner (Lighthouse/Sigma Prime)
* Piper Merriam (Trinity/Py-EVM)
* Pooja Ranjan (Ethereum Cat Herders)
* Preston (Prysmatic)
* Raúl Jordan (Prysmatic)
* Raúl Kripalani (Libp2p)
* Trenton Van Epps (Ethereum Cat Herders)
* Steven Schroeder (PegaSys)
* Terence Tsao (Prymatic)
* Wei Tang (Parity)
* Zak Cole (Whiteblock)
* Meeting notes by: Peter Gallagher























