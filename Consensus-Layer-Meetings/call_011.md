# Ethereum 2.0 Implementers Call 11 Notes

### Meeting Date/Time: Thursday 2019/1/31 at [14:00 GMT](https://savvytime.com/converter/gmt-to-germany-berlin-united-kingdom-london-ny-new-york-city-ca-san-francisco-china-shanghai-japan-tokyo-australia-sydney/jan-31-2019/2pm)
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/27)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=wS3sOB_hfgk)

# Agenda
1. Client Updates [_(4:17)_](https://youtu.be/wS3sOB_hfgk?t=257)
2. Research Updates [_(26:30)_](https://youtu.be/wS3sOB_hfgk?t=1590) 
3. Number theoretic shuffling [Link](ethereum/eth2.0-specs#323) [_(56:15)_](https://youtu.be/wS3sOB_hfgk?t=3375)
4. Any followup to [@ledgerwatch](https://github.com/ledgerwatch) comments from last meeting [Link](https://github.com/ethereum/eth2.0-pm/issues/23#issuecomment-453925393)  [_(1:00:04)_](https://youtu.be/wS3sOB_hfgk?t=3604) 
5. General spec discussion [_(1:01:34)_](https://youtu.be/wS3sOB_hfgk?t=3694)
6. Open Discussion/Closing Remarks [_(1:14:08)_](https://youtu.be/wS3sOB_hfgk?t=4448)

# Brief Highlights from the Call: Compliments of Ben Edgington's [What's New in ETH2](https://notes.ethereum.org/c/Sk8Zs--CQ/https%3A%2F%2Fbenjaminion.xyz%2Fnewineth2%2F20190201.html)
* [Phase 0 spec](https://github.com/ethereum/eth2.0-specs/releases/tag/v0.1) has been released 
* Grigore of [Runtime Verification](https://runtimeverification.com/) is looking at implementing Ethereum 2.0's semantics in the K framework to make it amenable to formal verification. [Zak Cole of [Whiteblock](https://www.whiteblock.io/) is also looking at [formal methods](https://twitter.com/0xzak/status/1090304646613131264).]
* Phase 1 update from Vitalik:
  * Now that Phase 0 is fairly stable, effort on Phase 1 (shard chains) is ramping up.
  * One big topic of research is the "proof of custody game". [What data](https://github.com/ethereum/eth2.0-specs/issues/529) goes into the proof? Optimising the rules of the game to minimise DoS vectors on innocent validators. Erasure codings.
  * Phase 1 is primarily a P2P networking engineering challenge. Nothing on this scale has been built before in the blockchain world.
  * The Research challenges are relatively minor by comparison.
* Phase 2 update from Vitalik:
  * Phase 2 (state execution) remains primarily a research challenge.
  * Vitalik is working on a document to flesh out the ideas.
  * Key topics are: account abstraction, rent model, wasm.
* Other things he is working on are,
  * looking at how to incorporate Casper CBC in due course, and
  * finding a good [number-theoretic shuffling](https://github.com/ethereum/eth2.0-specs/issues/323) algorithm to replace the current Fisher–Yates shuffle.
* What Justin is working on:
  * Looking into standardising the use of the BLS12-381 elliptic curve among the blockchains that are using it (e.g. Ethereum 2.0, ZCash, Chia and others). This means agreeing common hashing algorithms, serialisation, generators, etc.
  * Thinking about improving the liquidity of beacon chain Ether (BETH). Perhaps a mechanism to transfer entire stakes between validators; perhaps the ability to transfer more granular amounts between validators.
  * Also working on the number-theoretic shuffling. [This paper](https://www.iacr.org/archive/fse2007/45930457/45930457.pdf) is an interesting candidate.

# Client Updates
* Lodestar - Greg Markou [_(4:30)_](https://youtu.be/wS3sOB_hfgk?t=270)
  * Decided to use wasm to get bls from another library and then slowly just start working on it themselves on the side so they can start using it inside the beacon chain.
  * Audio breakdown
* Harmony - Mikhail [_(5:43)_](https://youtu.be/wS3sOB_hfgk?t=343)
  * Decided on the conception of initial release. Will be a beacon chain emulator, where parameters can be changed.
    * going to be a single machine and have thousands of validator instances
* Prysmatic - Terence [_(7:36)_](https://youtu.be/wS3sOB_hfgk?t=456)
  * Audio breakdown. Updates gathered from Prysmatic's [bi-weekly updates](https://medium.com/prysmatic-labs/ethereum-2-0-development-update-21-prysmatic-labs-1a32fac4b6d7)
  * 3 members of the Prysmatic Labs team attended both Aracon and Goerlicon in Berlin.
  * Prysmatic Labs to support the Goerli testnet with 3 Proof of Authority nodes. They plan on using the Goerli testETH to create a faucet that will onboard validators onto their ETH2.0 Prysm testnet.
  * Now that the Validator Deposit Contract has stabilized in the spec, they have been focusing on getting the validator client’s runtime to work well. 
    * Now, you can create a validator client account, which will create 2 private keys: one for signing frequent data as a validator, and the other for withdrawing validator rewards into a shard in the future.  
    * Using Geth’s powerful keystore to store this data, and will be adding support for hardware wallets in the future.
  * With regards to waiting for ChainStart and kickstarting the Beacon Chain:
    * Implemented the entire listening logic and now have the ability to start the beacon node + all connected validator clients once the ChainStart deposit log is fired.
      * This is critical to test in every way as it is how the real, production system will begin and give the green light to validator clients to begin performing their responsibilities as proposers or attesters.
  * Upcoming work: 
    * Waiting for validator activation
    * Complete proposer/attester functionality via RPC
    * Syncing the Beacon Block Operations Pool via P2P
* Parity - Wei Tang [_(8:45)_](https://youtu.be/wS3sOB_hfgk?t=525)
  * Mostly working on housekeeping (e.g refactoring, making the code cleaner) 
  * Working on migrating code base into Rust, edition 2018
  * Working on refactoring of aura substrate engine so they can reuse more code 
  * Worked on refactoring to get the fork-choice per slot 
* Py-EVM - Hsiao-Wei [_(10:36)_](https://youtu.be/wS3sOB_hfgk?t=636)
  * Working on integrating the beacon chain into the client side for Trinity
  * py-ssz ready 
  * Test generator to be moved to another repository: [Link](https://github.com/ethereum/eth2.0-test-generators)
* Lighthouse - Paul Hauner [_(11:51)_](https://youtu.be/wS3sOB_hfgk?t=711)
  * Rust libp2p gossipsub PR was put in by Adrian. Waiting for review from repository maintaners
  * Going to start the syncing logic in Py-EVM
  * State transition and sub-optimial fork-choice up to date
  * Benchmarking framework and testing framework created. Trying to get it to work at scale with 100's of thousands of validators.
  * Going to start doing benchmarking for fork-choice next. Trying to shrink down epoch-transition times
    * Team's got a new Rust developer starting in March
* Yeeth - Dean Eigenmann [_(15:43)_](https://youtu.be/wS3sOB_hfgk?t=943)
  * Working on reimplementing the entire spec
  * Once done with that, going to continue ssz and look into how best to do the libp2p components in Swift
    * Further look needed by Dean to just use the Go library there, or consider something else
* PegaSys - Joseph Delong [_(16:22)_](https://youtu.be/wS3sOB_hfgk?t=982)
  * Completed epoch processing
  * Block processing in progress
  * Approaching being up to date with the spec
  * Brought in a bls library (couldn't recall the exact name of the library)
  * Collaborating with Harmony, and currently working through some licensing issues
  * Preparing for Eth222.0 workshop [Link to livestream](https://www.youtube.com/watch?v=W9ztDeqlv40)
* Nimbus - Mamy [_(18:48)_](https://youtu.be/wS3sOB_hfgk?t=1128)
  * Pushed the latest bls tests about one week ago
  * Found out Milagro passed the same tests as the one of Py-EVM. So there is consistency between the implementations
  * Simulation is out, so you can simulate with plenty of validators
    * doesn't work on Windows as of now though
  * May have an issue on bls on bls on 32 bit platforms. The team is unsure if it's Milagro or something else, but 64 bit seems to be working perfectly
  * In sync with latest spec, except for light client changes
  * Progressing on deposit contract
  
# Introductions
* [_(23:50)_](https://youtu.be/wS3sOB_hfgk?t=1430) Grigori, of [Runtime Verification](https://runtimeverification.com/) is looking at implementing Ethereum 2.0's semantics in the K framework to make it amenable to formal verification. [Zak Cole of [Whiteblock](https://www.whiteblock.io/) is also looking at [formal methods](https://twitter.com/0xzak/status/1090304646613131264).] 
* [_(54:54)_](https://youtu.be/wS3sOB_hfgk?t=3294) Protolambda (Diederik Loerakker) [released](https://twitter.com/protolambda) his extraordinary [beacon chain schematic](https://github.com/protolambda/beacon-schematic/blob/master/beacon_chain.svg)

# 2. Research Updates  
* Vitalik [_(26:39)_](https://youtu.be/wS3sOB_hfgk?t=1599) 
    * Now that phase0 is entering a mode of small changes and bug fixes, it's important to keep the momentum and have everything for phase1 ready by the time clients are ready to develop that.
    * Main spec level issue remains to be bls signatures. So we don't necessarily need to worry about mechanisms for how seeds get updated and so forth, but we still need to have some kind of proof-of-custody game. Two components to that challenge.
        * One is figuring out what is the actual hash that goes into the proof-of-custody. Currently,in the crosslink, we're calling it a 'shard_block_hash' but that could be a suboptimal thing to put in for that field. Some alternative proposals were presented in [Issue #529](https://github.com/ethereum/eth2.0-specs/issues/529) for basically having a merkle tree of all the data containing block headers and block bodies. Some of the advantages there would be having fraud proof conditions to verify correctness of an entire chain of blocks in a cross-link so the clients don't need to worry about the shard chains if they don't need to. And just stick to the beacon chain. 
        * Second challenge is actually figuring out the proof-of-custody game. Latest update on that, which is currently in phase1, has the weakness that "if the data _is_ available", then you calculate the proof-of-custody and then you calculate out the bit that someone should have made, and if it turns out that that bit is wrong - then you need to do something, like 16 rounds of asking for a merkle branch before determining if they _actually_ did something wrong. WHich means you would need to extend someone's withdrawal by 16 rounds, of whatever the blockchain messaging delay is.
            * 16 rounds have now been reduced to 4 rounds, while still retaining the same amount of data going on chain (to be written up soon)
            * Another thing to think about is the game theoretic issues. The main challenge with proofs-of-custody is that it is a different kind of game than all the other challenges we have. Because for all of the other slashing conditions, if you slash someone, then the beacon chain can immediately figure out if you're right or wrong. And if you're right then - _yay_ - and if you're wrong then the message is not even valid. But here we are talking about forcing burdens of responding to challenges even on _innocent_ validators. And we're also talking about the possibility of DoS attacks around that, as well as the possibility of DoS attacks around malicious validators making fake, answerable, proofs-of-custody challenges for themselves and trying to push out challenges made by someone that actually knows they are being malicious. 
    * Unlike the p2p networking challenges in phase1, phase2 is not a very significant networking challenge (once you've already done the first phase). But, on the other hand, phase2 has more research challenges.
        * As far as what phase2 actually contians, a doc is to be written at some point. Still a bit too early to start writing a spec, as there is still room for idea refinement and multiple proposals are still out there. (e.g. account abstraction, CBC, how hibernation and waking work, state rent, components around wasm, etc.)
* Justin Drake [_(34:03)_](https://youtu.be/wS3sOB_hfgk?t=2043)
    * Going to try and focus on getting phase0 spec finalized as soon as possible. Still thinks there are a few non-trivial bugs floating around.
    * Been thinking about trying to standardize the bls12-381 curve across multiple blockchains. Have approached other blockchains, such as ZCash and Chia, who are interested in implementing bls12-381. 
        * Learned that Dfinity and Filecoin are also interested in the bls12-381 curve. And interested, specifically, in standardization. (Standardization includes hash to G1, hash to G2, serialization, generators, etc.)   
    * Discussed with the room the fact that there hasn't really been any dicussion on the networking topology for phase0 yet. Especially when it comes to how we would handle the aggregation for attestations. One idea that looks simple, is to have a monolithic gossipsub channel for everyone. And, if there aren't too many validators in phase0, that may actually be a workable solution. If not, we could also consider having feedback from an AMA in making beacon eth somewhat more transferrable/liquid/fungible. One idea is for validators to be able to change their withdrawal credentials. Doing so would mean that they sell their whole balance to some other third party, such as a centralized exchange. Another thing being considered is having a mechanism to transfer more granular amounts of beacon eth to other validator addresses.           
* Barcelona Supercomputing Center - Leo [_(38:09)_](https://youtu.be/wS3sOB_hfgk?t=2289)
    * Simulation for 256 nodes in the p2p network
    * Colors mean the number of peers (green == nodes with many peers, dark colors == nodes with a few number of peers)
    * Minimum number of peers for this simulation is 4
    * Average number of peers for each node is ~8
    * Simulation can be changed and is flexible. Can be configured to be simulated for nodes with 2 peers, 20 peers, etc.
    * One that thing was changed was the number of messages that are sent at every broadcast. So, for example, if you have 14 peers, you can limit the number of messages in a broadcast to (e.g 10) 
        * noticed that when the parameters for this is set low, the simulation manages to create partitions in the network. Meaning that there are parts of the network that get isolated. And in some extremes, there is a node in the network that doesn't receive any information from the whole entire network.
    * Simulation also produces block production time. Saw a variation in block production time from 2 seconds to 79 seconds. (To note: these are main chain blocks. And not beacon chain blocks)
    * Can also set a parameter in the simulation of what percentage of nodes in the network are miners/what percentage are not
    * Danny chimed in to ask Leo: [_(52:35)_](https://youtu.be/wS3sOB_hfgk?t=3155) if the simulation is of just the PoW network?
        * Leo: Yes, with beacon chain simulations, but they have not been released yet.
* PegaSys [53:10](https://youtu.be/wS3sOB_hfgk?t=3190)
    * No research update, as the team is preparing to give a talk at the Stanford Blockchain Conference
    * [Eth 222.0 Livestream Link](https://www.youtube.com/watch?v=W9ztDeqlv40) 
# 3. Number theoretic shuffling [Link](ethereum/eth2.0-specs#323)
* Vitalik Buterin [_(56:25)_](https://youtu.be/wS3sOB_hfgk?t=3385)
    * [Issue #529](https://github.com/ethereum/eth2.0-specs/issues/529)
    * One possible alternative number-theoretic shuffling algorithm [(Issue#323)](https://github.com/ethereum/eth2.0-specs/issues/323) uses the x --> x**power plus K permutation, where we have random K values that get selected based off of the hash that comes through the seed.
    * The second possible alternative is the Fiestal shuffling (see link above for more info found in comments section) 
    * The third possible alternative came from Stanford academics, and they told us about some provably optimal design. Desinged to be uniform, even in the case of very small sets.   
    * Ran some tests on the prime shuffle and the Fiestal shuffle, and it turns out the Fiestal shuffle is basically broken. Reason being that, its proof-of-correctness works well when you're operating over very large sets, but much less when you're operating over small sets which is what we were doing here. 
    * According to Vitalik's statistical tests (test being that he tried running a shuffle with nine elements, and then shuffled 10 million times and checked the statistical distribution and how uniform it is. And it seemed to match a random distribution. Albeit this is just one test. Further talk with academics to take place.) 
    * https://www.iacr.org/archive/fse2007/45930457/45930457.pdf
# 4. Any followup to [@ledgerwatch](https://github.com/ledgerwatch) comments from last meeting [Link](https://github.com/ethereum/eth2.0-pm/issues/23#issuecomment-453925393)
* To note: Alexey couldn't make the meeting
* Question was open regarding if we upped the threshold for the chain start or not. Alexey's concern was that you could have a majority takeover attack happen with 500k ether. But if we up it from 500k to 2million before the chain starts, then that mitigates it without requiring any particular major changes. And if we can't get 2million eth to sign up (62,500 validators), then we can just change the terms of what we're building anyway.
    * Discussion to be continued over time
# 5. General spec discussions
* As stated in the beginning of the call, the first version of Phase0 of the specification was released. It is generally feature complete, with a few notes still open with the point-wise shuffling, standardization of the bls, and some other minor things. But it is approaching its final form with respect to features and stability. Going to do one release per week through February as we continue to find bugs and clean up the delivery. And then plan on slowing down the release cycle in March. 
* Don't expect significant timelines for releases. This should probably be done internally within each team and have networking internally within the clients.
* Danny imagines the release today would have some critical bugs. And knowing that it's too early too give any kind of timeline specifically.
* Formal analysis to be done on the software side and algorithmic theoretical side. Teams should be doing their share of auditing as well. With respect to any type of audits beyond that, we need to get to a more stable spec and iron out networking etc before we bring anyone in for audits. 
# 6. Open Discussion/Closing Remarks
* Perhaps it would be good to start looking bookings/dates for possible meetings in April. 
    * EF and Lighthouse will be in Sydney
    * Signals to be had from the rest of the teams and their plans for Sydney or not
    * Danny to add a new agenda item to future meetings called: Testing
# Links shared during meeting
* https://github.com/ethereum/eth2.0-pm/issues/27
* https://github.com/ethereum/eth2.0-specs/releases/tag/v0.1
* https://github.com/ethereum/eth2.0-test-generators
* https://hackmd.io/kyptAIG6RK6Gv02IOKyQ6A?view
* https://hackmd.io/kyptAIG6RK6Gv02IOKyQ6A?view
* https://www.youtube.com/watch?v=W9ztDeqlv40
* https://www.eventbrite.com/e/ethereum-2220-workshop-tickets-55130474734
* https://github.com/ethereum/eth2.0-tests/pull/13
* https://github.com/ethereum/eth2.0-tests/blob/bls-vectors/test_vectors/test_bls.yml
* https://github.com/ethereum/eth2.0-tests/tree/bls-vectors/test_vectors
* https://github.com/ethereum/eth2.0-specs/issues/529
* http://leobago.com/static/shardSim/data/2019-01-31_11-48-45/index.html
* https://livestream.com/accounts/1973198/Blockchain2019
* https://github.com/ethereum/eth2.0-specs/issues/323
* https://www.iacr.org/archive/fse2007/45930457/45930457.pdf
* https://github.com/ethereum/eth2.0-pm/issues/23#issuecomment-453925393
* https://github.com/ethereum/eth2.0-tests/pull/16

# Attendees
* Visual stream was down. Therefore, no official list of attendees could be taken. Meeting notes were written by Peter Gallagher 
