# Ethereum 2.0 Implementers Call 12 Notes

### Meeting Date/Time: Thursday 2019/2/14 at [14:00 GMT](https://savvytime.com/converter/gmt-to-germany-berlin-united-kingdom-london-ny-new-york-city-ca-san-francisco-china-shanghai-japan-tokyo-australia-sydney/feb-14-2019/2pm)
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/29)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=p1qHM2B8cGc)

# Agenda
1. Testing Updates [_(00:01)_](https://youtu.be/p1qHM2B8cGc)
2. Client Updates [_(2:40)_](https://youtu.be/p1qHM2B8cGc?t=160)
3. Research Updates [_(34:54)_](https://youtu.be/p1qHM2B8cGc?t=2094) 
4. discv5 update/discussion [Link](ethereum/eth2.0-specs#323) [_(24:11)_](https://youtu.be/p1qHM2B8cGc?t=1451)
5. Quick note on light clients [_(21:52)_](https://youtu.be/p1qHM2B8cGc?t=1313)
6. [Minimal phase 0 wire api](https://github.com/ethereum/eth2.0-specs/issues/593) [_(47:26)_](https://youtu.be/p1qHM2B8cGc?t=2846)
7. [Path to testnets](https://github.com/ethereum/eth2.0-pm/issues/29#issuecomment-461823647) [_(56:18)_](https://youtu.be/p1qHM2B8cGc?t=3378) 
    * suggest reading: https://lighthouse.sigmaprime.io/update-07.html
8. Genesis slot number & signed vs unisgned ints [_(1:20:48)_](https://youtu.be/p1qHM2B8cGc?t=4848)
9. Spec discussion [_(1:34:08)_](https://youtu.be/p1qHM2B8cGc?t=5648)
10. Open Discussion/Closing Remarks 

# 1. Testing Updates
* _Note:_ Live stream started towards the end of testing updates:
* Jannik:
  * new test generator repo. Started to migrate existing generator. (bls and shuffling tests, as well as ssz tests)
  * test repo will be updated by the generators during CI (it can be submoduled by implementers)
* Next test to be state tests. But still catching up on things on py-evm side 
# 2. Client Updates
* Lighthouse - Paul Hauner [_(2:50)_](https://youtu.be/p1qHM2B8cGc?t=170)
  * implemented Vitalik's optimized LMD Ghost
  * in sync, will use Prysmatic config for network test
  * working with reviewers to get Rust gossipsub merged
  * released new shuffling test generator in the eth2.0 test repo
  * created unit test
  * refactoring to monorepo
  * next steps: networking and syncing
* Prysmatic - Terence [_(3:46)_](https://youtu.be/p1qHM2B8cGc?t=226)
  * Dev Update #22: https://medium.com/prysmatic-labs/ethereum-2-0-development-update-22-prysmatic-labs-b5b88ace0441
  * focus on validator runtime and fixing bugs
  * Opened tracking issues for aligning with [v0.2](https://github.com/prysmaticlabs/prysm/issues/1541) and future spec [releases](https://github.com/prysmaticlabs/prysm/issues/1542)
  * able to get v0.1 beacon chain successfully running with 8 validators locally, deploying the deposit contract into the Goerli testnet, waiting for it to fill up with deposits, and getting the chainstart log fired into validators clients who were then assigned to propose or attest on beacon blocks.
    * As a result of this process, they encountered tons of bugs that required feature fixes to get this to work seamlessly. The team outlined all of these problems in their tracking issue for our runtime [here](https://github.com/prysmaticlabs/prysm/issues/1565)
  * implemented a preliminary deposit pool as a simple key/value store in memory which is populated from deposit logs received from the deposit contract on the proof of work chain.
  * started deploying and testing the eth2.0 deposit contract on the goerli testnet. And were able to simulate how their client would function in a production environment in anticipation for their testnet. The beacon node would listen for logs from the contract and once it receives the requisite chain start log, it would kick-start the beacon chain and correspondingly allow the validator clients to start performing their duties.
  * proposer/attestor code restructuring:
    * simplified and abstracted the validator logic to less than 50 lines of core logic. This main routine is easier to understand, follow, and debug than having multiple routines handling different responsibilities of a validator.
    * Check out the simplified validator logic here: https://gist.github.com/terenc3t/991465f3c54d8d22a380e2c5abc89e7a
  * validator account credentials creation process complete
  * misc: etherscan added support for verifying Vyper contracts
  * If interested in helping out, check out the [contributing guidelines](https://github.com/prysmaticlabs/prysm#contribution-guidelines) and [open projects](https://github.com/prysmaticlabs/prysm/projects)
* Harmony - Mikhail Kalinin [_(5:06)_](https://youtu.be/p1qHM2B8cGc?t=306)
  * working on emulator
  * working on doing some functional testing
  * need to add logs and current line interface
* Chainsafe - Greg Markou [_(6:25)_](https://youtu.be/p1qHM2B8cGc?t=385)
  * mock simulation for next week
  * coverage is up pretty high on custom tests
  * focusing on getting the eth1.0 contract stuff going
  * been making some headway on the libp2p side of things. Mikerah has been getting the javascript implementation up to spec
* Parity - Wei Tang [_(7:31)_](https://youtu.be/p1qHM2B8cGc?t=451)
  * updating run time to v0.2
  * been making things more generic and modular so it makes it easier to test and be able to reuse code 
  * finished most of the Casper FFG parts, as well as RANDAO and rewards/penalty parts
  * working on upgrading rest of the spec
* Geth - Péter Szilágyi [_(8:45)_]
  * marathon meeting sessions in the last 3 days
  * nothing technical to report
  * will experiment in a separate repo to experiment with and start hacking on something
  * will challenge some critical part (e.g serialization format)
* Pegasys - Jonny Rhea [_(11:03)_](https://youtu.be/p1qHM2B8cGc?t=663)
  * completed a service adaptor that allows to deploy a monolith or broken into micro-services (translates event from event list in grpc calls automatically)
  * integration test
  * middle of updating to spec v0.1
  * half about 2/3 of block processing to do
  * ssz tested and integrated into the library
  * next steps: integration of p2p implementation in Java
* Nimbus - Mamy [_(12:47)_](https://youtu.be/p1qHM2B8cGc?t=767)
  * Meet and hack in Brussels from Feb 2 to Feb 8 (+ FOSDEM)
    * Presentation on how to build an Eth client: https://fosdem.org/2019/schedule/event/nimbus/
    * Fixes on our simulation (state+block processing with multiple validators but without fork choice).
    * Identified critical path to deliver testnet MVP in march: https://github.com/status-im/nim-beacon-chain/issues/96
    * refactoring and renaming towards monorepo for pure Eth libraries
  * Sync to latest specs
  * BLS speed improvements
  * testnet MVP decisions:
    * Linux/Mac as primary target. Windows as a secondary target.
       * dependencies management (RocksDB)
       * compiler and environment issues (gcc, clang, vcc)
       * libp2p on windows, we need to adapt our config
    * Freeze the specs to 0.2 or 0.3
       * We had and still have several simulation breakages in our prototype when syncing to 0.2
    * testnet focus:
       * state sync when client is behind
       * broadcasting attestations and proposers
       * switch from RLPx to libp2p
       * fork choice (currently not activated in our simulation)
         * unit test would help
       * devops
 * Yeeth - Dean Eigenmann [_(16:20)_]
   * got bls working 
   * code has been updated to v0.2
   * next steps: implementing more uint tests and getting a running simulator going
 * Py-EVM - Hsiao-Wei Wang [_(17:02)_] (https://youtu.be/p1qHM2B8cGc?t=1022)
   * working on syncing the current spec
   * p2p side, python daemon libp2p binding module is ready. Breaking it in with Trinity node
   * researching and supporting common modules (e.g. deposit contract)
 * Diederick [_(19:06)_](https://youtu.be/p1qHM2B8cGc?t=1146)
   * stopped working on dart client 
   * continued to work on other projects related to eth2.0 (all in Go)
   * LMD Ghost simulation
   * shuffling algorithm 
   * considering jumping on the upcoming project from Geth (Firefly)
    
 
 * **Reminder from Danny:** as spec stabilizes please don't follow all of these helpers exactly. Make design decisions appropriate to your language and codebase. We will not be providing consensus tests for all the granular helpers (e.g no test vectors for “get_current_epoch”).
 
 
# 3. Research Updates
* Vitalik - [_(35:16)_](https://youtu.be/p1qHM2B8cGc?t=2116)
  * Been doing some work to get the Phase 1 spec up to a point where there's something viable ready for phase 1 by the end of February
  * Already merged dev structure of shard blocks and what gets committed to the shard block roots
    * commitments are somewhat more complicated, but it's basically putting a bunch of shard blocks into a merkle tree
    * the thing that is still sitting in a PR is, basically everything that has to do with proofs of custody (but not including the proof of custody interactive game)
       * that includes things like the mechanism for how sub-keys work, penalties for revealing them early, the rules for when you have to reveal sub-keys that you used, challenging for data, etc.
  * Haven't started writing it up, but wants to write up the interactive proof of custody game itself. This would be what happens if some validator committed to some custody bit. Then some other validator computed the custody bit themselves and saw that it doesn't match, and wanted to start the interactive "true-bit" game in order to figure out who's actually at fault.  
        * In general, doesn't expect too many serious difficulties in that. Mostly a spec writing exercise. However, there is one exception. And, albeit not mandatory, if we want to phase 1 be fully multiparty compute friendly in the same way that phase 0 is. If we want that to be the case, then we need to replace XOR with something more complicated. But that's a very discrete and separate component the same way the shuffling algorithm was. (pretty much changing one operation w/i this algorithm, no matter how complex the black box is)
        * So, when we get around to writing up the PoC game, it'll be written just using the hash of the data leaf and sub-key. And then we'll swap in a different hash function (which could be some fancy thing we can MPC in 5 rounds because it mixes different binary fields in weird ways. It could also be elliptic curve multiplication, or some other possibilities still needed to be gone through).
  * The idea behind keeping these things MPC friendly is so that staking pools have options that can be more decentralized. 
* Justin - [_(39:51)_](https://youtu.be/p1qHM2B8cGc?t=2391)
  * Committed to phase 0. Still work to be done in terms of bugs and design issues.
  * One of the things he has been looking at is with serialization entry hashing. So expect some changes in v0.3 
  * Pleased that Peter and Geth are trying to break the spec. And would encourage all implementers to keep an eye trying to break things. As there are a bunch of things that can still be broken. 
  * One cool thing to expect soon is a unified signature handling mechanism. And will be a nice simplification and clean-up
     * this signature handling with potentially be a part of the ssz spec. So it could be used outside as a standard. 
     * With regards to standards, Justin has been trying to find strategies to standardize cryptographic primatives (bls 12-381)
      * contacted a bunch of chains to see what their plans were. The great majority of next-gen blockchains are looking to use bls aggregation in some way or another. And there seems to be consensus that bls 12-381 will be the way forward. There also seems to be an effort to standardize as much as possible on the fine details to have more interoperability. 
      * the other cryptographic primative is the hash function. The good news is that SHA-256 is an option on the table. Because we have an existing pre compile in Eth1.0 And it looks like the great majority of chains use SHA-256. So that is looking like a good option to replace keccak256. 
  * One thing added recently is transfers. So that you can send BETH within the beacon chain. That was prompted by the AMA where people had a lot of questions around that. Fungibilty around BETH was also been a topic of discussion, and they are still seeing what options are there.
  * Earlier in February was VDF day. Made lots of progress, new ideas, and one of the good news is that the RSA MPC does look viable and has been reviewed by several MPC experts that were there. 
    * good news here is that anyone using RSA accumulators will be able to benefit from that
* BSC - Leo [_(44:19)_](https://youtu.be/p1qHM2B8cGc?t=2659)
  * Integrated part of the beacon chain on the simulator
  * Did a couple of runs with thousands of nodes simulator
    * had some problems with communication (messaging explodes when there are uncle blocks on the beacon chain)
  * Some latency issues between the different nodes
* Nicolas Liochon: Aggregation protocol
  * https://docs.google.com/presentation/d/1fL0mBF5At4ojW0HhbvBQ2yJHA3_q8q8kiioC6WvY9g4/edit#slide=id.p
  * https://github.com/ConsenSys/wittgenstein/issues/35
  * https://github.com/ConsenSys/handel
# 4. discv5 update/discussion
* Felix:
    * https://docs.google.com/document/d/1Rd4yNw1TNQBvfRrKeEMSTseb6fvPzS-C--obOn0nul8/edit#heading=h.bbb5kq80e8n
    * priority to implemention in & listen to feedback on wire protocol
    * if any teams wanted to get their hands dirty and help out, they could look into the ENR format. Has similar role to ssz for the beacon chain, in that it's a standard format that can be tested independently w/o talking to another node. ANd you get an n epoch look ahead.
    * https://eips.ethereum.org/EIPS/eip-778
* Danny discussed ideas around networking on the research side specifically: [_(26:57)_](https://youtu.be/p1qHM2B8cGc?t=1617)
    * general path forward is to use libp2p
    * integrate discv5 into libp2p
    * major requirements are that nodes can (in a relatively short time) join a shard topic/subnet and begin syncing. Joining on the order of < 1 minute. And syncing some amount of the chain over the next 5 minutes or so.
    * beyond that, in the beginning, we expect to map multiple shards to one topic (to reduce complexity and to increase stability in these topics and the amount of peers in each topic). Topics are used to broadcast attestations, which are then aggregated and passed to a main topic, which is the beacon node. Which all peers will be joined to. 
# 5. Quick note on light clients
* suggest reading: https://lighthouse.sigmaprime.io/update-07.html
* Looking for one or two teams to drive the path forward on making a light client
* Specifically, the sooner we get a viable light client to mainnet, the sooner that we can do some of the things that allow us to upgrade ETH1.0 
    * finality of the chain on 1.0
    * exposing a state root from 2.0 --> 1.0, so that the data layer in Phase 1 can be pulled in via witnesses into 1.0 contracts
* If interested in paving that path forward for light clients, reach out to Danny or other on the EF research team
    * Link to light client proposal: https://github.com/ethereum/eth2.0-specs/issues/459
# 6. [Minimal phase 0 wire api](https://github.com/ethereum/eth2.0-specs/issues/593)
* Some of the components are heavily drawn from the 1.0 wire protocol. Mainly this is specifying the minimal messages, blocks, attestations, exits, etc. that are passed around & the expected topics to be passed around.
* One of the more interesting things to discuss is sync protocol. And how that is a little bit different in the context of a PoS network with weak subjectivity. Weak subjectivity being the length of time from when you last synced that you can remain synced. Or when you bring something to the protocol (like a recent finalized block) how old that can be in order to safely sync.
  * so this complicated things in a certain sense in that it requires a slightly changed user experience in that one would have to have this piece of extra, recent, protcol information about the network. 
  * however, it actually simplifies the user experience in another way. With regards to the weak subjectivity period, and how it acts as a natural cut-off in the expectation of how long a node is expected to serve past blocks.
  * If you're syncing, the expectation is either that you have the state associated with the weak subjectivity hash that you're bringing (that you got from a snapshot or a previous sync), or the expectation is that you show up with the latest finalized epoch checkpoint, and it is safe within the weak subjectivity period. And, from that point, you would perform something similar to a fast sync of the state relative to 1.0
  * Danny alluded to the room to take a look at the document as it relates to syncing 1.0. Once the group gets a generalized thumb up, this will turn into a more formalized spec so that we can move forward with networking. This, as well as unified test vectors, are some of the biggest blockers in interoperability as of right now.
* https://github.com/ethereum/eth2.0-specs/issues/593 
* This is something we should get user feedback on. Jonny talked about the scenario in which the user doesn't have a checkpoint to provide, it would be interesting if the client could default to looking up some kind of a IPFS multi-address. One that's been voted on as being a known good checkpoint. 
  * large design space here. And clients could do different things for this. 
  * going to be up to each individual client to provide a sane user experience. Although, we could come around and explore some standards as well.
# 7. [Path to testnets](https://github.com/ethereum/eth2.0-pm/issues/29#issuecomment-461823647)
* Three-fold path:
  * continuing to iron out bugs and solidify phase 0 spec (and as Justin said, please read the spec with active eyes. There _are_ bugs still in there.)
  * getting these cross-client test vectors together. Doesn't make any sense for people to have interop cross-client testing on the network level w/o these test vectors in place.
  * networking specification stuff. Being the wire protocol and discv5
    * on small testnets, we don't need a topic discovery and everything can operate on one channel. That's definitelty a viable option, especially on a low number of validators
  * If you don't have someone on your team taking a look at networking stuff, you probably should
  * Networking in Serenity (ETH2.0) article by Mikerah: https://medium.com/@mikerahqc/networking-in-serenity-eth2-0-8bbdb5bd6dd4
# 8. Genesis slot number & signed vs unisgned ints 
* Due to some subtractions very early in the specs (in early epochs. If we start at slot 0, we get some negative numbers that pop up. And you have to write in some conditional logic for the first few epochs into the spec). One way to fix this is to just not start at slot 0. This brought up some issues:
  * 1: it's not very elegant
  * 2: starting at something like 2**63 (which is currently in the spec) has some issues with overlapping with signed integers in certain languages.)
* Some people are arguing lets just have signed ints. Some people say, let's have unsigned ints because these values should never be negative and we should specify the ranges to be expected and to start at slot 0 and have some confitional logic in there. 
* Danny pointed out that, just because we are exposing (via these serialization formats) unsigned ints, the spec and the protocol don't really care - as long as you're coming up with the same state transitions and the same serialized and hash formats. 
  * with that said, if we do start at slot 0, there is some stuff needed to be worked through there. 
* Diederick chimed in, discussing that the main thing we have to keep in mind is that there are 3 classes of integers. And all three may require different solutions. 
  * 1. slot numbers
  * 2. validator indexes
  * 3. balances
* Temp. fix seems to be to not start at 2 ** 63 and start at 2 ** 10
* More input to be had by the teams in order to make a decision
# 9. Spec discussion
* Call began running a bit late: Quick rundown at [_(1:34:08)_](https://youtu.be/p1qHM2B8cGc?t=5648)
# 10. Open Discussion/Closing Remarks
* Danny talked about setting something up for EDCON in April. Possibly the day before it starts. Agenda not yet set

# Links shared during meeting
* https://github.com/ethereum/eth2.0-pm/issues/29
* https://www.youtube.com/live_chat?v=p1qHM2B8cGc&is_popout=1
* https://github.com/ethereum/eth2.0-test-generators/issues
* https://github.com/ethereum/eth2.0-test-generators/issues/12
* https://github.com/prysmaticlabs/prysm/issues/1565
* https://fosdem.org/2019/schedule/event/nimbus/
* https://github.com/status-im/nim-beacon-chain/issues/96
* https://notes.ethereum.org/9xwEMJ9dSFWqvuqr5bh4QQ?view
* https://github.com/ethereum/eth2.0-specs/issues/459
* https://eips.ethereum.org/EIPS/eip-778
* https://github.com/ethereum/devp2p/wiki/Discovery-Overview
* https://github.com/libp2p/go-libp2p-daemon/blob/master/README.md#language-bindings
* https://github.com/ethereum/eth2.0-specs/issues/568
* https://github.com/ethereum/eth2.0-specs/pull/587
* https://github.com/ethereum/eth2.0-specs/pull/625
* https://github.com/ethereum/eth2.0-specs/pull/625
* https://github.com/ethereum/eth2.0-specs/issues/605
* https://github.com/ethereum/eth2.0-specs/issues/612
* https://docs.google.com/presentation/d/1fL0mBF5At4ojW0HhbvBQ2yJHA3_q8q8kiioC6WvY9g4/edit#slide=id.p
* https://github.com/ConsenSys/wittgenstein/issues/35
* https://github.com/ethereum/eth2.0-specs/issues/593
* https://github.com/libp2p/interop
* https://github.com/libp2p/go-libp2p-daemon
* https://github.com/libp2p/js-libp2p-daemon
* https://github.com/libp2p/interop
* https://gitter.im/ethresearch/p2p
* https://ethresear.ch/c/p2p
* https://github.com/ethereum/eth2.0-pm/issues/29#issuecomment-463640711
* https://github.com/ethereum/eth2.0-specs/issues
* https://github.com/ethereum/eth2.0-specs/issues/503
* https://notes.ethereum.org/s/rkhCgQteN#SSZ
* https://github.com/ethereum/beacon_chain/issues?q=is%3Aissue+ssz+is%3Aclosed

# Attendees
* Danny Ryan (EF/Research)
* Péter Szilágyi (EF/Geth)
* Adrian Manning (Lighthouse/Sigma Prime)
* Afri Schoeden (Parity)
* Alex Stokes (Lighthouse/Sigma Prime)
* Vitalik Buterin (EF/Research)
* Ben Edgington (PegaSys)
* Blazj Kolad (Pegasys)
* Carl Beekhuizen (Decentralized staking pools)
* Chih-Cheng Liang (EF/Research)
* Daniel Ellison (ConsenSys)
* Dean Eigenmann (Yeeth)
* Diederik Loerakker (Independent)
* Felix Lange (EF/geth)
* Fredrick Harrysson (Parity)
* Greg Markou (ChainSafe)
* Hsiao-Wei Wang (EF/Research)
* Jacek Sieka (Status/Nimbus)
* Jannik Luhn (Brainbot/Research)
* Jonny Rhea (Pegasys)
* Kevin Mai-Hsuan (EF/Research)
* Leo (BSC)
* Nicolas Liochon (PegaSys)
* Luke Anderson (Lighthouse/Sigma Prime)
* Mamy Ratsimbazafy (Nimbus/Status)
* Martin Holst Swende (EF/geth/testing)
* Matthew Slipper (Kyokan)
* Mikerah (ChainSafe)
* Mikhail Kalinan (Harmony)
* Nicholas Lin (EF/Research)
* Nishant Das (Prysmatic)
* Olivier Begassat (ConsenSys)
* Paul Hauner (Lighthouse/Sigma Prime)
* Preston (Prysmatic)
* Raúl Kripalani (Libp2p)
* Stan Drozd (Lighthouse/Sigma Prime)
* Steven Schroeder (PegaSys)
* Wei Tang (Parity)
* Zahary Karadjov (Status/Nimbus)
* Meeting notes by: Peter Gallagher
























