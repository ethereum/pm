# Ethereum 2.0 Implementers Call 48 Notes
### Meeting Date/Time: Thu, Septemebr 17, 2018 14:00 GMT
### Meeting Duration: 0.75 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/181)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=5GYF6gCIbGE&feature=youtu.be)

# Agenda
1. Testing and Release Updates (2:20)
2. [Spadina](https://github.com/goerli/medalla/tree/master/spadina) (8:45)
3. Client Updates (10:16)
4. Research Updates (19:35)
5. BLSv4 (22:20)
6. API status (31:39)
7. Networking (32:59)
8. Spec discussion (34:25)
9. Open Discussion/Closing Remarks (38:45)

# 1. Testing and Release Updates (2:20)
* v0.123 release, which includes much of the minor and iterative work that has been done on the p2p spec. That will be released a couple of hours after this call.
  * Danny alluded that, one of the main things he wants people to take a look at is the modifications of message ID and gossip sub. Danny to discuss more on that in the release notes, however.
* Proto has been working on something in the direction of Hive, but for eth2. That allows for easily spinning up testnets (a bit like automated multi-net stuff, but controlled by local containers & can specify unit test and things)
  * close to be usable. Should hear more by next week
* Terence asked if there were any plans on merging the forkchoice spec test into the official repo? Below notes are a discussion on the pros/cons on testing the forkchoice through network test vs. unit test.
  * Danny - Current plan is to leave those as is. And to use the testing framework that Proto's been working on to run forkchoice test through the network interface. Rather than inserting blocks through a non-standard method.
    * easier to specify
    * easier to test
  * Mamy - The issue with a full test net is that some of the testing edge cases, when you have a chain reorg, you invalidate almost one epoch. How would you induce that into Proto's framework for example?
    * Danny responded - If you have one producer and one consumer, then you essentially get to decide exactly what the other node sees.
      * So for example, if you spin up a Nimbus node and you have a rumor that's producing all of the blocks and attestations. Then that Nimbus node sees exactly what you feed to the network.
    * Mamy further alluded his main concern is that it is easier to test just a function, because a network test you also bring lost attestations or messages into the fold. With the changes to gossip discovery, it may be better to test in isolation what we can.
    * Proto - Forkchoice is not just an algorithm but matters in integration as well. Forkchoice 
      * In Forkchoice, you keep track of this pool of attestations, the latest attestation, and you need to fetch them from the gossip. It's not just a state machine. Most of these bugs happen regarding information on which attestations get inserted and at what time. 
        * And we already have unit test per client for just forkchoice state. 
        
# 2. [Spadina](https://github.com/goerli/medalla/tree/master/spadina) (8:45)
* Genesis planned to be on September 29, 2020.
* Danny - Intention is to have a Goerli launch testnet
  * 3 day end of life
    * We can **not** do whatever we want with it after that point
* The configuration and plan on launching the launchpad along with the configuration so that user's can deposit the minimum deposit account.
  * Minimum active validator account is 1,024 so that we don't have any worry of when that number is going to be hit. We can just artificially hit that ourselves.
  
# 3. Client Updates (10:16)
* Nimbus (10:20)
  * Mamy - Past two weeks have been very busy. With several network fixes.
    * One regarding libp2p and specifically with isync. 
    * Still have some others to hunt down
    * Had gossip on 1.1 and being tested using the multi-net script
    * Merged slashing protection 
    * Made progress on attestation aggregation w/ valdiator clients and beacon node split case
    * Started last phase of audit. 
      * This one if focused on everything related to validators:
        * secrets
        * key stores
        * block proposal and slashing protection
    * Gossip sub is in scope
    * Asked auditors to review user instructions just to make sure everything makes sense and is not confusing that could make them lose money or privacy.
* Teku (12:45)
  * Anton - Working on validator influence, rest API
    * Some work is ongoing to weak subjectivity
    * Added support for Rust library 
    * Discv5 side - Fixed vulnerabilities and started to implement v5.1
* Lodestar (13:55)
  * Cayman Nava - Dormant on medalla for a while. Having mostly memory issues.
    * Seems like a lot of that has been fixed. It used to be that all state was stored in memory, now they've broken up their block processing by checkpoint. And now they store those checkpoint states in a separate cache and it helps prune and they can prune the state a lot more intelligently. It also gives them a chance for other tasks to happen, such a network requests. When they had long skip slot periods, they would be hogging the CPU because the block processing was synchronous. Now they will wait after every epoch. And now they also have state regeneration because of the pruning. And can regenerate based off of whatever states are already in memory.
    * Re-wrote Forkchoice is now in a separate package. There were some bugs previously. Not using the write balances for attestations. 
    * Refactored eth1 data fetching for block production. 
    * In progress - Gossipsub 1.1 integration. In the next week they are trying to get everything merged to hopefully be ready for Spadina
* Prysm (16:10)
  * Raul Jordan - Improvements recently
    * Fixed up a few DDos vectors brought up by Proto
    * Integrated validator exits and are end to end tested in the master branch
    * Integrated bslt and merged it into the master branch
    * Only a few issues with fuzz testing
    * Started going full speed on eth2 api implementation and integration
    * All of protbuff implementations are done
    * Weak subjectivity sync intregation currently being worked on after reviewing the spec.
    * Some improvements being done on peer scoring and fixed up the ipv6 integration
* Lighthouse (17:14)
  * Herman Junge - A few things to report
    * Two new team members have joined (Herman being one of them. A fellow named Sean being the other)
    * Progress being done on the standard http api 
    * With new api, 256 validators currently running and doing well
    * Will be a code freeze for audits in the first week of October
    * Intend to refactor and support more user friendly backward syncing
    * Remote signer implementation (which will allow a central server to hold all keys and peform sign-off functions. This is useful for performing Staking as a Service platforms)
    * Updating discv5.1 and that will be ready soon
    * Improving sync protocol speeds
* Nethermind 
  * no one in attendance
  
# 4. Research Updates (19:35)
* Aditya Asgaonkar (19:43)
  * Update on weak subjectivity guide 
  * In terms of implementation - should first start implementing a basic version of the weak subjectivity sync. Which is taking comman lane input of a checkpoint and making sure the checkpoint is in the path of the sync.
    * If you want to provide some advanced safety features for your users. May be able to input the state, and make sure the current slot tick is going to be within the safe weak subjectivity period of your input weak subjectivity check point. 
    * Most teams already started working on this.
* Phase 1 updated by Danny (20:45)
  * Been spending a lot of time on reward accounting (mechanisms inside that track what's going on in the epoch). As well as design and incentives around Phase 1
  * Vitalik (21:15) - Basically a simplification on how rewards are calculated. Coming on the heels of the other change in Phase 1 of a simplification of the accounting process. So we don't have to keep track of pending attestation objects and stuff.
* Leo BSC (21:55)
  * Moving forward with gossip sub updates

# 5. BLSv4 (22:40)
 * Bumped to a version 4, which is incompatible with the current version
 * Banning of the zero (0) private key, which doesn't really change much for folks other than the disallowment of the zero (0) private key
 * Danny - After some discussions internally and discussions with BLSt library maintainers, he believes that the release for the main net will be this BLSv4
  * If you're usuing the BLSt library, folks over there are working on an update now
 * Should be a simple modification
 * Mamy (23:45) - If everyone agrees to adopt v4, we won't need that much changes in wrapping
  * Danny - Draft PR is up right now with all of these wrappers to modify the v4 to allow for the zero (0) public key
    * After some discussion it was ultimately decided to just use v4 and not have to deal with all of these wrappers
 * Mamy's second question (23:43) - It seems like there is a need for zero (0) public keys and signatures for Phase 1, but not for Phase 2. Which scenario requires this?
  * Danny (25:07) - So there is a difference between the zero (0) public private key being valid and the empty aggregates being valid. Empty aggregates are banned in Phase 0 because of the way the attestation processing is handled. But there currenty *is* a use case for having an empty aggregate w/ the way light client signatures are handled in Phase 1. This is a **much** more simple wrapper than actually allowing for the zero (0) public key. 
 * Ben Edginton (25:55) - To confirm, there will be a spec update, and then we will agree what to hardfork to implement this on Medalla? Or we implement for mainnet? He goes on to say that it is technically breaking so we should have a v0.13 
  * Danny - Right now leaving it as a PR, with the intention of getting it in the v0.01 mainnet release. Can further discuss how we want to treat this on Medalla. Should moonlight probably around launch of mainnet.
 * Danny to write some quick notes on what upgrading Medalla would look like
 
# 6. API status (31:39)
* Danny - Client teams have generall given updates on this during their respective updates. So all set
* Proto (32:15) - Beacon chain explorer is moving to a new api
  * Lots of focus on validator api. In the future may extend this usage to block explorers and/or performance reporting as well. And account for this in the future.

# 7. Networking (32:59)
* Danny - Had a networking call the week prior. And asked if there were any items that one would like to bring up and dicuss. 
  * Proto (33:20) - Been working on a test runner that spins up test nets. Shorter lived testnets. A bit like Hive, with the goal of to run different programs and get the eth2 details right. 
    * Maybe try a run and merge it into eth1 Hive at some point

# 8. Spec dicussion (34:25)
* Vitalik (34:50) - Asked if we should talk about the paramter changes to mainnet. Or if that was done and decided on
  * Danny - Released a Phase 0 EIP with Vitalik a couple of days prior. Discusses the following:
    * Punitiveness of the initial launch
    * Suggestion to have a reduced punitiveness on the tail risk scenarios. This is because if something does happen there in the first few months, it is likely not an attack.
      * This is specifically a reduction of the 3x multiplier on proportional slashings to just 1. 
      * An increase of the late penalty quotient by a factor of 4. Meaning that it takes 4x longer to leak to what it previously was. (e.g. the Medalla incident)
      * Minimum slashing penalty quotient is increased by a factor 4. Which makes the minimum slashing more around 2.5eth instead of 1. With the stated intention of upgrading to the full punitive parameters on the approximate five month time horizon after launch. This will give us a chance to practice a hard fork before Phase 1. And, at the same time, reduce the stakes a little bit for early risk takers.
   * Ben Edgington (37:09) - We should probably run this in some sort of network before going live with it. Just to make sure all implementations are consistent. (potentially use Proto's stuff for help in dry runs?)
   
# 9. Open Discussion/Closing Remarks (38:45)
* Not much to note. Danny recommended prepping the Spidena configuration that has been merged
 
# Attendees
* Herman Junge
* danny
* JosephC
* Hsiao-Wei Wang
* Ben Edgington
* Cayman Nava
* Zahary Karadjov
* Sacha Saint-Leger
* Carl Beekhuizen
* Justin Drake
* Anton
* Mamy
* Raul Jordan
* Dankrad
* Afr Schoe
* Vitalik
* Alex Stokes
* Jacek Sieka
* lightclient
* Cem Ozer
* Lakshman Sankar
* Leo BSC
* Protolambda
* Jonathan Rhea
* Sam Wilson
* Aditya Asgaonkar
* Terence
* Peter Gallagher (Meeting Notes) 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


