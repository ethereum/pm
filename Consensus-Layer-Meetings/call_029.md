# Ethereum 2.0 Implementers Call 29 Notes

### Meeting Date/Time: Thursday 2019/12/5 at 14:00 GMT
### Meeting Duration: ~ 53 mins
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/108)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=MxeEWmEdb5E)
### Moderator: Danny Ryan
### Notes: Sachin Mittal
 ----------

 **Danny**: Welcome everyone!

 ## 1. Testing and Release Updates

 ### Removal of signing root

 **Danny**: Being executed by protolamda, feedback so far is overwhelmingly positive. Need a decision on this call. No objections, so plan to merge it today unless any objections noted on PR 1491.

 ### Fixes to fork-choice

**Danny**: Plan to merge soon, but looking for better ways to test and specify fork-choice behaviour. I suggest, we do unit testing for specific functions and Integration test by throwing a bunch of blocks and add few stations at a client and getting a result. 	

**Mammy**: I'm just thinking for multi-threading testing. Though it's very hard because we have to like test interleaving of four or five phrases in different order and there are ways to do that so maybe we can reuse the same.
Easiest would be to have a lot of SSE objects, and then test values interleaving and they also use State Reduction to handle “exponential explosion of the states”.

**Danny**: We need to merge these PR’s before the release, also since some of the initial testnets will be on the Uni too. Just specify your testnets.

### Integration of modified BLS spec

**Danny**: There are a couple of PRs on this which are a priority too. Expect a release right after New Year. It will include BLS modifications such that Testnets during December will have old BLS but Testnets after the New Year will be expected to have the new signature spec.Also, Any tests net that is long running and gives us signals to move to main net would have to have the correct signature scheme. Any changes on this PR?

**Carl**: It is adopting the new hash to curve version, as mentioned in my PR #1499. It basically tries to separate Eth 2.0 specs from the BLS specs to help teams using 3rd party libraries. Onto updating the test vectors.

**Danny**: We might put it into dev, but cut of the test vectors so that when we’ll begin to work on the BLS implementations, we can generate the vectors.

* Fuzzing (BeaconFuzz) is making progress.


 ## 2. Client Updates

 ### NimBus

**Mammy**:

* We finished the last SSZ bugs, so you can use CLI again.
* Regarding Optimizations, we have removed last quadratic behaviours, now OCI time has been reduced from 50 minutes to less than 20 minutes.
* Final bottlenecks are SHA256 and BLS, but not blocking for having the state transition under 6 seconds.
* On testnet, we are debugging syncing. It is working but we have some edge test cases. Also, we have done a lot of polish on the instructions for Joining.
* For the test and CI, we are in the process of setting up Jenkins so to test Nimbus on controlled hardware, especially Android and ARM. Also, we are now auto tracking running tests especially state transitions to make sure we don't have any regression.
* No more git-LFS or the EF. On the phasing prop, we now have something similar to NCLI called NFS (fuzzing endpoints) and we have PR pending on CPE on becoming the phase repo with shuffling as a proof of concept.
* For networking, ready to integrate libp2p and remove daemon. Next is discv5.


### Trinity


**Alex Stokes**:
* Up to spec 0.9.2. We have done a lot of fork choice updates, refactoring and bug fixes.
* Converting Pylibp2p to Trio library. Bugfixes and prep for public testnet. Open PR for attestation aggregation.



### Loadster


**Cayman**:

* We swapped our BLS implementation with WASM build of Herumi, and it speeded up 40x across the board.
* Implemented BLS EIP 2333-2335 for future use.
* Still updating to 0.9.x. discv5 in progress.

### Artemis

**Ben Edgington**:

* Up to date with 0.9.2 including naive aggregation.
* Req/Resp is done and being tested against Prysm and Lighthouse.
* Focus remains on getting ready to join public Testnets: syncing and importing deposit receipts.
* Completing discv5 integration.

### Prysm

**Terence**:

* Testnet has been running smoothly, except a couple of finality reversions which have now been debugged.
* Beacon chain explorer has necessitated some work on RPC endpoint. And it is up and running, so people can build some other cool stuff on the top of it.
* Primary focus is 0.9.2 testnet relaunch.
* Raul spent a lot of time optimising SSZ with a functional cache for the custom state SSZ resulting in 50x speedup in syncing.

### Lighthouse

**Adrian Manning**:

* Public testnet target release this week.
* Database optimisations have been made. New schema makes the DB very small. It doesn’t duplicate any states and use checkpoints to make the DB small.
* Speedups in SSZ decoding - remove BLS checking when reading state from the DB, big performance gain.
* Rebuilding syncing algorithms to support multiple peers over a longer lasting testnet.  Tied up logging to make it more user friendly,  Validator onboarding docs written and are in the PR.
* Metrics and monitoring for the testnets up and running.
* We pulled our testnet down today because one of our major bootnodes often booted the other nodes, so we used to ban them but now we have kept it lenient and will kick them only for 30 seconds.

**Danny**: Thanks! What were the optimizations from LS, and SSZ?

**Adrian**: We used to read states from the database for verifying BLS case, but we have stopped doing that. And it has resulted in 99.9% gains in reading rate.

**Mammy**: It was a bottleneck in Nimbus, but now with new unsigned and signed block headers, we will try to implement it.

**Danny**: Premise being once I've saved these keys to my database I've already verified them so don't do it again.

**Mammy**: Idea is only check them just before use so lazily checking them instead of when you load the database for example on reboot doing all the BLS stuff and loading
everything in memory and then using them because that makes a great latency drink.


### Harmony

**Mikhail**
* At 0.9.2, excluding aggregation stuff.
* Working on integration tests for the fork choice. Almost ready to push fork choice tests to community test suite.
* Discv5 has been merged and now we are looking at simulations.
* Also made some progress on gossipsub simulations. Shared during the yesterday’s network call.

### Parity

**Wei Tang**:
* Some updates to Substrate.
* Still on 0.9.0; trying to join Prysm testnet, but there is an issue in BLS verification (all the spec tests pass, but real sigs fail which is weird).

**Danny**: Great, Thanks!! We have Tomasz onboard to share their research.

### Nethermind

**Tomasz**: Has started implementing 0.9.2, expect to have 0.9.2 done in about a month. Passing BLS, SSZ, container tests. Working on networking, remainder of spec implementation.


 ## 3. Research Updates

**Vitalik**:
* Working with Justin on increasing the efficiency of STARK proving.
* Working on more application level things this week - blog post coming.
* Discussing how Phase 2 cross-shard Txs will work: to be enshrined in protocol, or done with receipts in the application layer? Is Eth2 a fat protocol or just a data-availability and computation layer?


**Justin**:
* Going deep on STARKs. Recent presentation on [polynomial commitment schemes](https://www.youtube.com/watch?v=bz16BURH_u8&feature=youtu.be). Some new ideas have come out of this, maybe a significant breakthrough. Write-up soon.
* There’s also a breakthrough in RSA MPC. Has now been tested with 10,000 participants. Orders of magnitude has shown big improvement, awesome job by Ligero team.

**Danny**: Proto, since you have been looking into the cross shard txs, do you have anything to share on that?

**Protolamda**: Working on cross-shard Txs. Discussion of tradeoffs on the Phase2 call this week.

**Musab (Runtime Verification)**: Abstractions of the beacon chain model. Started this week trying to prove safety and liveness.

**Danny**: Daejun (Runtime Verification) is writing up the formal analysis of the deposit contract, expected this month for public review.

**Matt Garnett (Quilt)**:

* Phase 2 call happened. Next one is targeted for mid Jan. Will has aggregated some questions regarding the stateless protocols and put it on the eth.research. Here is the [Summary](https://ethresear.ch/t/remaining-questions-on-state-providers-and-stateless-networks-in-eth2/6585).

* I’m working on some tools to improve the process of building and testing execution environments which has been one of the big pain points for both of us to explore in that area and our new hires are still working on the simulation.


## 4. Networking

**Danny**: Since we had a networking call yesterday. I have dropped two very good links, and mammy has made notes. You can check them out. Good survey of current activities. Need to identify which areas are under-resourced. Planning a follow-up in 2 weeks.

* Notes from networking call:

[Link 1](https://hackmd.io/@benjaminion/BJ3YqrSTr)

[Link 2](https://gist.github.com/mratsim/fef2b0a7c5a335ac6bc61c01592b3fea)


## 5. Discussion of persisted state size reduction

**Danny**: This is an Agenda item from Mikhail. I know, Lighthouse is working on this. Adrian, you wanna give a quick synopsis about your hot and cold scheme?

 **Adrian**: There are three parts, the hot-cold as you said. Hot is pretty much anything after finalize, then after they are moved into the cold database. So in the cold database are things that shouldn't be changing or moved. We can kind of streamline where they're actually stored on the disk. I guess, the main gains that we have is doing an a Nimbus style approach. Where we store state snapshots instead of every state and then if we need to read the state for any reason in the cold database at some stage.  You can rebuild a state or replace that by the state from the blocks that we have in the diary. So you keep the blocks and checkpoint states. Essentially we don't duplicate any of the states so if there's a state duplication it kind of just re - references. The main gains which I think are the easiest to do are the staged snapshot in the freezer DB.

**Danny**: How are you choosing, I mean what are the parameters of a snapshot?

**Adrian**: Its configurable, working on it! (We are measuring the time it will take to fill the 32 GB HDD).

**Mikhail**: Question! I believe hot storage is very big in size, I mean 100 MB+ to represent an epoch and so on… in my opinion, it requires some reduction as well?

**Adrian**: Michael from our team is working on this very problem, so maybe we can continue chatting over this after the call.

**Danny**: Follow up suggestions on the approach? Mikhail?

**Mikhail**: Thinking about incremental storage, just the diffs between states.

**Protolambda**:  Lighthouse’s approach seems ideal. Has worked on tree-state.

**Jacek Seika**: This may have an impact on state-syncing between nodes. We may wish to agree on which states are available to be synced (e.g. one every few weeks within the weak subjectivity period).

**Mikhail**: Anton from our team is planning to look into state sync design.

## 6. Spec discussion

Discussion of release of Ph1 spec! Vitalik <> Danny

**Danny**: Proto and I are going to make a plan for Phase 1, and Phase 1 testing over the next few weeks. And we are planning to release BLS update at the start of the new year.

**Vitalik**: Yeah, atleast a scaffold of Phase 1 needs to be released so that people can start building, testing over it. Also, about fraud proof part as well.

Also, We need a team looking at Eth1 - Eth2 bridge.

## 7. Testnet Discussion

**Danny**: We are still in the optimising/hardening stage. Single-client testnets are good for now - but I would like to see them scaled to very large validator numbers maybe using DevOps scripts and deploying to the cloud. Talk to me, if anyone has ideas around this.


 ## Attendees

* Alex Stokes (Lighthouse/Sigma Prime)
* Adrian Manning
* Ben Edgington (PegaSys)
* Cayman
* Carl Beekhuizen
* Chih-Cheng Liang
* Collin Myers
* Danny Ryan (EF/Research)
* Hsiao-Wei Wang
* Jacek Sieka
* Jannik Luhn
* JosephC
* Joseph Delong
* Justin Drake
* Kevin Mai-Hsuan Chia
* Mamy
* Marin Petrunic
* Matt garnett
* Mbaxter
* Mikerah
* Mikhail Kalinin
* Musab
* Nicolas Liochon
* Nishant Das
* Protolambda
* Shahan
* Terence Tsao (Prysmatic Labs)
* Tomasz Stanczak
* Trentonvanepps
* Vitalik B.
* Wei Tang
* Zahary    

 ## Chat Highlights

From danny to Everyone: 02:05 PM

https://github.com/ethereum/eth2.0-pm/issues/108
https://github.com/ethereum/eth2.0-specs/pull/1491
https://github.com/ethereum/eth2.0-specs/pull/1495

From danny to Everyone: 02:21 PM

https://github.com/ethereum/EIPs/pull/2333
https://github.com/ethereum/EIPs/pull/2334
https://github.com/ethereum/EIPs/pull/2335
beaconcha.in

From Mikhail Kalinin to Everyone: 02:31 PM

Forgot to say, during the previous call I mentioned a write up about slashing condition detection that I was going to publish. Here it is: https://hackmd.io/@sYlY_LZpQIGgFmhdv6vV-A/By897a5sH

From Justin Drake to Everyone: 02:33 PM

Polynomial commitment schemes https://www.youtube.com/watch?v=bz16BURH_u8&feature=youtu.be

From matt garnett to Everyone: 02:38 PM

https://ethresear.ch/t/remaining-questions-on-state-providers-and-stateless-networks-in-eth2/6585

From protolambda . to Everyone: 02:46 PM

https://github.com/protolambda/eth-merkle-trees/blob/master/typing_partials.md
^ Data-sharing approach: only store merkle tree modifications, represent as binary tree.
