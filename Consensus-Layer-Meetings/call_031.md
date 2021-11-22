# Ethereum 2.0 Implementers Call 31 Notes

### Meeting Date/Time: Thursday 2020/01/09 at [14:00 UTC](https://savvytime.com/converter/utc-to-germany-berlin-united-kingdom-london-ny-new-york-city-ca-san-francisco-china-shanghai-japan-tokyo-australia-sydney/dec-19-2019/2pm)
### Meeting Duration:  45 minutes
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/118)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=u2w4EO9YepI)
### Moderator: Danny Ryan
### Notes: Brett Robertson


-----------------------------

# Summary

## ACTIONS NEEDED

Action Item | Description
--|--
**31.1** | Review [Fork-Choice Testing update](https://github.com/ethereum/eth2.0-spec-tests/issues/17) for integration into the standard testing distro.
**31.2** | Danny to advise on the time of the next Networking call.

-----------------------------

# Agenda

- [1. Testing and Release Updates](#1-testing-and-release-updates)   
- [2. Client Updates](#2-client-updates)   
- [3. Research Updates](#3-research-updates)   
- [4. Networking](#4-networking)   
- [5. Spec discussion](#5-spec-discussion)   
- [6. Open Discussion/Closing Remarks](#6-open-discussionclosing-remarks)   

-----------------------------


# 1. Testing and Release Updates

**Video:** [`[1:47]`](https://youtu.be/u2w4EO9YepI?t=107)

Been working on [v.0.10.0](https://notes.ethereum.org/@djrtwo/Bkn3zpwxB?type=view) this intended to be a stable release for testnets and for audits that are being conducted. This is to be released 10 January 2020. Other than the BLS changes, these are mostly non-breaking changes.

General thank you from Danny to everyone involved in getting the BLS changes across the line.

For further information on BLS go the [post](https://hackmd.io/@benjaminion/H1lkISO3JU) published by Ben Edgington.

On the testing side there is a couple of extra tests for deposit processing.

## 1.1 Fork-Choice Testing

Mikhail shared Alex’s update on [github](https://github.com/ethereum/eth2.0-spec-tests/issues/17) for people to review and provide feedback. 

This is an integration test and not a unit test.

## Actions
- **31.1**— Review [Fork-Choice Testing update](https://github.com/ethereum/eth2.0-spec-tests/issues/17) for integration into the standard testing distro.


# 2. Client Updates

**Video:** [`[7:16]`](https://youtu.be/u2w4EO9YepI?t=436)

## 2.1 Nimbus

Mamy advised that Nimbus is now in sync with core spec v0.9.4. For Fuzzing purposes they are keeping a separate branch with v.0.9.3. They are focused on Networking. They have their first PR on discovery 5 so it is halfway done and that is the major blocker before they can join the Prysm and Lighthouse testnets. They are also verify interop with Go LibP2P.  On the tooling side we are planning an RPC endpoint for Beacon node.

## 2.2 Artemis
Shahan advised that they have been working on Eth1 data management including polling the Eth1 client for block data. They are also working on syncing Artemis clients. They have also down some work with integrating the Discovery module - this is almost complete. They have also been working on integrating Artemis into the Beacon Fuzz project - this is almost complete. Ben’s java implementation of IEBTF standard hash to curve method for Ethereum 2.0 has been merged into Artemis.

Questions raised by Shahan for response:

Question 1: Are there any resources that the Artemis team can look at to see how they are syncing the Eth1 data to the chain? Is it 1 peer that they are polling or more. 

Requested a DM to Shahan out of call.

Danny advised there were two approaches broadly, one is that the beacon node is talking to some Eth1 RPC endpoint caching this data. Or there is a second side module that is doing the work. He believes the majority are talking to 1 RPC endpoint with the assumption that this is a node that is being run by the validator or a node that the validator is connecting to which they have some sort of trust relationship with.

There is a change in v.0.10.0 that uses timestamping rather than block height to cast votes which has some benefits in terms of caching. This is generally considered backwards compatible because even if a handful of people were doing the votes differently at the end of the period they would agree on votes in 99% of the time. This appears in the [issue](https://github.com/ethereum/eth2.0-specs/issues/1431) that Paul raised pushing for this change. 

Question 2: For the Beacon Fuzz, the project is currently at the v.0.9.1 spec, what are the plans to update the spec? 

Danny believes that the Beacon Fuzz will upgrade to v.0.10.0 but Lighthouse need to confirm.


## 2.3 Trinity

Hsiao-Wei advised that they have been working on the data and Beacon Node separation this will include data chronological implementation and data API implementation. Trinity has a Eth1 voting handler currently located in the Beacon Node side. They are currently working to integrate it with an Eth1 web3 provider. They are currently testing this with the test provider. With regards to spec they are working on the v.0.9.3 and they have a standing PR which is almost done. After this they will move on to v.0.9.4. 

## 2.4 Prysmatic Labs
Terence advised that Prysmatic is relaunching their testnet. The Genesis time is 4pm PST, 9 January 2020. It presents everything up to the v0.9.3 spec but they use the v.0.9.4 spec test though. It is something they will work on over the next coming weeks. There were a couple optimisations that went into the v.0.9.3 spec such as proper handling of the deposits and how Eth1 data is managed. They had to refactor some of the validator assignment and committee logic for the validator of this response to be as efficient as possible. Raul also worked on implementing a custom version of SSC tree hash state. 

Terence [invited](https://prylabs.net/participate) anyone who is interested in being a Prysm validator.

Danny confirmed that after talking to Preston that Prysmatic will be the first to have the aggregation strategy on a testnet. 

## 2.5 Lighthouse

Adrian advised that Lighthouse have been running a testnet since the 22nd December 2019. There has been no public announcements but that should be done in the next few days. It is on a mainnet spec that has pretty stable so he suggested it was probably time to get the public on to try and break it. Lighthouse have been focused on the stability of the testnet and performance in particular block processing times because syncing takes some time to process all the blocks. He advised that they had made significant gains in this area. They have also been looking at Networking specifically around bug fixing and stability for their testnet. The Bitfly team also found a lock in the Lighthouse API which has helped them debug that. They are close to a v1.1 release which adds all the stability fixes and block processing updates. This is expected to be released in the next few days along with the new testnet. They have removed the requirements for a full Eth1 node so a fast sync node will be all they need. So they will probably remove all the public Goerli notes for their docs to encourage any participants to run their own Eth1 nodes. We built some compose stuff which allows one in a single command to spin up a node and node validator and join the network relatively easily. They have added BLS Harumi we saw about 2x gains using that which is passing all the tests but it has not yet been put into master yet. They are also in the process of adding the naive aggregation strategy which should be soon and should be released in an entirely new testnet. 

Danny confirmed that Shigeo Mutsinari, the maintainer of the Harumi Library, has been working on it to update it to support the new ITF standards. 

## 2.6 Harmony

Mikhail has confirmed that Harmony have updated the spec to v.0.9.4 and Alex has generated the test vectors into this spec version. Medri has been working on the this quify (SP?) simulation. Anton has been helping him to extend this simulator that he created for gossip sub simulation. They have also discussed time consensus now Alex is working on a write up to describe some basic ideas. They are starting to work on some new stuff as part of TX RX.

Danny confirmed that going forward that in future meetings Harmony updates will form part of TX RX updates and research updates. 

## 2.7 Lodestar

Cayman confirmed they are in the final stages of merging the 0.9 branch into master and at that point they will be at v.0.9.3. They have been working on refactoring their SSC library to allow for something like Protolambda’s [remerkleable library](https://github.com/protolambda/remerkleable). This is to allow for something that can abstract over a merkle tree backed structure and give an interface the way a normal object would. As part of that the code is better and even for our naive cases and looks like their stabilisation and hash tree root is for most cases 2x as fast. They hope in the next few weeks to have a remerkleable for their library to plug into. 

Protolambda gave a brief description of remerkleable. He advise that more examples and documentation are to follow as it was still in an early stage.

## 2.8 Nethermind

Sly advised that they have just got the validator block assigning working. Nethermind is still on v.0.9.1. So the validator speaks to the Beacon Nodes and you can actually run both and generate an ongoing chain. There are however still no attestations and they are still using mock Eth1 data. They are also about to start peering to publish the block - this remains in research with no code yet. Most of the team has been busy with Eth1 work. They are hoping to grow their team and catch up with the rest of the Eth2 clients. 


# 3. Research Updates

**Video:** [`[24.48]`](https://youtu.be/u2w4EO9YepI?t=1488)

Vitalik advised that most research work has been on Phase 1 and Phase 2. They have figured out some improvements to data availability roots that makes the constructions slightly cleaner. They spent quite a bit of time looking into alternatives to the data availability 2D construction and the general consensus was whilst the ideas were great they would not be available immediately. So it was concluded that they would start with 3D coding and move onto something else later. 

On the Phase 2 front there were also some ideas on how to do execution environments. 

Probably the most recent publication is the [proposal](https://ethresear.ch/t/alternative-proposal-for-early-eth1-eth2-merge/6666) to move Eth1 into Eth2 in an earlier schedule than before. The idea would be that they would figure out the stateless client verifier and then include that in the Eth2 system and then come up a mechanism where Eth1 validators can declare themselves as being Eth2 friendly. And all Eth2 friendly validators would then form a pool from which proposers could be selected and proposers would need to have the Eth1 state but the committee members that validate will still be taken from the global set and they would still validate statelessly.

In terms of prerequisites the main one is getting stateless clients working correctly.  

Danny suggested reviewing this in comparison to the finality gadget over the next few months would be a good idea.

Another thing to consider is to actually verify that the network can handle blocks of somewhat larger sizes, that is stateless client witnesses of around 4MB or an average case of 600KB. It just so happens that 625KB is the max size for an Eth1 chain block. So Vitalik suggested that they repeat the tests that Whiteblock did previously of 200KB but this time with 600KB blocks. 

The other thing that could be done is network tests using Eth2 tooling just to verify that MB chunks of data can be passed around. 

Danny wanted to confirm that the main success criteria here was the lack of increase of Uncle rate. Vitalik agreed.

Justin advised that Supranational, the team that is working on an VDF ASIC, independently as a side project, starting thinking of accelerating BLS12-381. They are working with a collaborator that is working on an implementation from scratch. He advised that they have already implemented point addition and point doubling and that this is currently faster than Herumi. They advised they are 10% faster for these two operations. They will start implementing milli-loops and pairings. In addition to the performance improvements which are nice. The collaborator is also a formal verification expert. He had a look a the Herumi code and his impression was that formally verifying the Herumi code would be difficult and part of the reason is that the code base was quite complicated. His approach is very clean code focused on performance. Even though this won’t be production ready for the launch of Phase 0 I guess that is something that may be worth investing in for Phase 1 or Phase 2.

Other than than Justin is still working on the acceleration of snarks. He has had a look at Pipinger and he has also started a technical viability study for building a multi-exponentiation for ASIC and it looks like there could be a 1000x improvement on performance. So you could imagine a small PCI card or box that is attached to your computer and it would do 1 billion exponentiations in something like 2 seconds. 

Justin advised that whilst it was still very early days he was excited.

Justin has also been working on VDF Day. So there will be a VDF day, one day prior to the San Francisco blockchain conference on February 18th, 2020. 

William advised that there is a Phase 2 call on Tuesday, January 13, 2020. There are several updates on previously advised work. They can run a ganache type tool that can run on multiple shards. They hope to release a roadmap and readme on this, next week. They are now also focused on TX RX. They are collaborating to build an end to end testing suite. The idea here is that it is library based so that you can choose your proof backend and memory backend and this connects the various pieces and then you can run the EE on top of that. So a roadmap doc is coming soon on that as well. There is overlap with some of the Eth1.x stateless work so they are going to release a write up today that nails down the scope for three different directions for the state provider side and gives rationale for each of them. They will be recommending one particular direction called the pole model and they are starting a prototype on this. They will hope to bring on some Eth 1 data to validate this end to end.

William was hoping to get some feedback on that so was hoping for people to look at it before the call. He is also continuing to look at cross-shard schemes, Vitalik recently did an interesting write up on a netting format recently which seems to allow for the removal of nonces and bit fields. William advised that he has been playing around with some ideas around that.

There are a couple of write ups coming, one is on the EE upgradability and the other is on the fee market discussion for Phase 1, laying out the different options. They are also looking at some interim plans for Phase 2 such as the idea of starting with a minimalist Phase 2 and then battle test it before building on top of it.

Joseph confirmed for TX RX that Consensys have been working with the Quilt team quite a bit. They are collaborating on a cross-shard transaction simulator and that should be out sometime in the next two weeks. Jonny Rhea has also been working on an ML (Machine Learning) EE called Anomaly. He also suggested people look at https://ethsear.ch/ - created by Jonny Rhea over Christmas it indexes ethresear.ch, pertinent people on twitter and what is new on Eth2, so if you are looking for a research topic on Eth2 one can look there and it is all indexed. 

Leo gave a quick update on [Eth Barcelona](https://ethbarcelona.github.io/) and advised that they are gathering speakers for the conference. He invited participants to speak and suggested that if people were interested to (email)[ethbarcelona@gmail.com) him.


# 4. Networking

**Video:** [`[40:17]`](https://youtu.be/u2w4EO9YepI?t=2417)

Danny advised that in the last call there was discussion around allowing empty responses and streamed responses in the block RPC requests. This has now been included in v.0.10.0.

There will be another Networking call either a week or two from today’s call - Danny will make a decision after the Ethereum 2.0 call.

## Actions
- **31.2**— Danny to advise on the time of the next Networking call.

# 6. Spec discussion

**Video:** [`[41:14]`](https://youtu.be/u2w4EO9YepI?t=2474)

Vitalik asked what people felt about an accelerated Eth1 & Eth2 merge. The general consensus was very positive. Mikhail did question the timing of this and raised that whilst he liked it technically he felt some may be concerned about the stability and security of this change. Danny agreed and suggested that this may only take place post Phase 0 and Phase 1. Joseph felt that the sooner we could bring better functionality to Eth2 the better. 

Danny asked Vitalik if he saw this as being in lieu of a finality gadget. Vitalik suggested that he was not sure but if we were prepared to do a finality gadget then why would we not want to do full merge.

Danny suggested that there was still significant work required to prepare Eth1.x with regards specifically to the stateless operations. Vitalik agreed that Eth1.x statelessness was going to be a huge priority this year.

Danny also suggested that this was a much cleaner way for Eth1 to use the scalable data layer of Eth2 Phase 1. It would be a more direct way rather than using a bridge and exposing state roots.

Vitalik noted there was no descent. 

# 7. Open Discussion/Closing Remarks

**Video:** [`[45:54]`](https://youtu.be/u2w4EO9YepI?t=2754)

Danny ran through the list of things discussed and taking place in the next period. 

Danny also advised that there was an [article](https://blog.ethereum.org/2020/01/08/update-on-the-vyper-compiler/) on the Ethereum Foundation blog that some of the members of the Ethereum Foundation have taken a new direction with the vyper compiler due to issues with the python vyper compiler. There will be a write up that will address the concerns and methods used in the formal verification of the deposit contract to remove the compiler from the picture. 

He also asked all Eth2 teams attending Eth Denver to let him know so that he can arrange coworking days before the hackathon.

------

# Annex

## Next Meeting Date/Time

Thursday January 23, 2020.

## Attendees

- Adrian Manning
- Ben Edgington
- Brett Robertson
- Cayman
- Chih-Cheng Liang
- Danny Ryan
- Hsiao Wei Wang
- Jacek Sieka
- Jannik Luhn
- Joseph Delong
- Justin Drake
- Kevin Chia
- Leo BSC
- Mamy
- Matt Garnett
- Meredith Baxter
- Nishant Das
- Preston Van Loon
- Protolambda
- Shahan Khatchadourian
- Sly Gryphon
- Steven Schroeder
- Svante
- Terence
- Tomasz Stanczak
- Trenton Van Epps
- Vitalik Buterin
- Will Villanueva
- Zahary Karadjov
