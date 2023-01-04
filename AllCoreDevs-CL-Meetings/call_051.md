# Ethereum 2.0 Implementers Call 51 Notes
### Meeting Date/Time: Thu, October 29, 2020 14:00 GMT
### Meeting Duration: 38:19
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/189)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=_4Ry2AEzXGU)

# Agenda
1. Testing and Release Updates [1:07](https://youtu.be/_4Ry2AEzXGU?t=67)
2. State of Medalla [2:35](https://youtu.be/_4Ry2AEzXGU?t=156)
3. Client Updates [3:56](https://youtu.be/_4Ry2AEzXGU?t=236)
4. Research Updates [12:43](https://youtu.be/_4Ry2AEzXGU?t=763)
5. Networking [16:47](https://youtu.be/_4Ry2AEzXGU?t=1007)
6. Spec discussion [32:30](https://youtu.be/_4Ry2AEzXGU?t=1950)
7. Open Discussion/Closing Remarks [32:48](https://youtu.be/_4Ry2AEzXGU?t=1968)

# 1. Testing and Release Updates [1:07](https://youtu.be/_4Ry2AEzXGU?t=67)
* Issue with a malform test vector that is fixed on the v1.0 candidate branch. Danny has not yet released another update to that.
* Looking into some test vector reform to reduce the overall size, amount of time to generate, and to get forkchoice test integrated and built up. 
  * More information on this within the next couple of weeks.
        
# 2. State of Medalla [2:35](https://youtu.be/_4Ry2AEzXGU?t=156) 
* No fundamental consensus errors, but it does look like there are some instabilities every 4 to 8 epochs.
* Prysm is looking into some optimizations as well. And might have found what looks like a DDos vector that is popping up as well.
* Ben Edgington (Teku) described the high resource usage they have been suffering from, which would explain the periodic drops, has been fixed.
  
# 3. Client Updates [3:56](https://youtu.be/_4Ry2AEzXGU?t=236)
* Teku [4:04](https://youtu.be/_4Ry2AEzXGU?t=244)
  * Audit is complete, will share final report when it is available
  * Pushed a few performance improvements related to Medalla not finalizing
  * To reduce memory consumption, reworked state regeneration logic so that queue tasks are no longer holding on to state references
  * Eliminated some extra processes
  * Updated to disc v5.1 
  * Working to implement the standard rest api
  * Done some work to improve ssz serialization 
  * For large beacon states they've seen a 20x speed up
* Lighthouse [6:11](https://youtu.be/_4Ry2AEzXGU?t=371)
  * Updated to v1.0 of the spec. Joining Teku on Medalla with that
  * Updated to disc 5.1 on Medalla as well
  * Finishing up some of the standard api end points, and working through those to get everything sorted
  * Been doing some performance updates with regards to reducing some memory
  * Tracking some various bug fixes that have occurred due to some libp2p updates as things have been finalized
* Lodestar [7:49](https://youtu.be/_4Ry2AEzXGU?t=469)
  * Merged in validator slashing protection interchange and refactored that tp handle all slashing cases
  * Finishing up with the standard rest api with regards to the state url
  * Trying to finish up the refactor of the core chain logic. Wanting to pull that out in to a separate package that could hopefully be used independently of Lodestar
  * Still trying to gear up for another release once all in flight PRs get merged
* Prysm [9:12](https://youtu.be/_4Ry2AEzXGU?t=552)
  * Had first beta release, promoting from alpha to beta. Able to promote features that were in v2 to default
  * Working on standard api end point by category
  * Trying to knock out as many issues as possible (had 100, now out ~70)
  * Trying to get into mainnet with as little open items as possible
  * Trail of Bits audit went pretty well and resolving those open items
* Nimbus [10:46](https://youtu.be/_4Ry2AEzXGU?t=646)
  * Deployed disc v5.1 and bls on Medalla
  * Used the current state of Medalla to test how Nimbus behaved when the situation is broken
  * Introduced some new optimizations
  * Currently running pretty stable
  * Memory usage is roughly the same as of now
  * Sees some potential on standardising end point states 
  
# 4. Research Updates [12:43](https://youtu.be/_4Ry2AEzXGU?t=763)
* Vitalik on Phase 1 data availability work:
  * Exploring an expedited data availability focused Phase 1 direction. Which will bring in shards as explicit data shards and use some tools to make sure that we can very easily do a data availability sampling.
  * Lately been looking into different subnet structures
  * Proto has been making an implementation of both the erasure coding commitment side and the subnet side
  * One of the challenges is exactly what the concrete structure will be in terms of proposals will look like. And this is as good an opportunity as any to see if we can do things like staggering to get shard block time to much less than 1 slot.
  * Goal of all of this is to move as quickly as possible towards something that we can live test in some kind of sharded p2p environment.
* Leo of BSC:
  * Able to gather a bunch of information with the light client (period ID, node ID, IP address, country, city of each client, latency of each client, etc.)

# 5. Networking [16:47](https://youtu.be/_4Ry2AEzXGU?t=1007)
 * Once you've started from weak subjectivity state - what do you do about serving blocks? Since you might be getting block requests outside since you've synced the chain. 
  * Handled ~ kind of ~ in the spec. Says that blocks by range requests should be served within the weak subjectivity sync period.
  * Intention there is that if the weak subjectivity period is 2 weeks, and you started from something 2 days ago - you should backfill the blocks through those 2 weeks and be able to serve through those 2 weeks. 
  * Could also backfill all the way to Genesis, but is not a requisite.
  * Can and should be refined and made more explicit in the spec.
  * If someone makes a request and you do not have the blocks is a question that still needs to be thought through.
  * Meredith - Planning to backfill blocks but will still have a period of time that you are in the process of doing that. So you still need to be able to figure out what is an explicit way to handle this problem.
 * Zahary had the question of - when you've done weak subjectivity sync. But you don't necessarily have the information through generis, how do you handle block production especially with regards to eth1 data  
  * One option is to discuss more offline. Zahary has started a discussion of this on the Weak Subjectivity Telegram
    * Will need to produce merkle proofs for the newly added deposits and new blocks. In order to do these merkle proofs, the spec says you need the entire set of deposits from genesis. 
    * Danny - It is exactly the state of the deposit contract. If you have a branch and you are in the trie, and you append to the right. Then you should be able to form the root. In addition to beacon state, you should also have a recent deposit and proof of that trie. So that you can always grow to the right by appending new deposits.  
 * Gossipsub v1.1: 
  * Danny - About time for more than a few of us to review it and get it into the specs
  * Adrian - Already have a few nodes that are deploying the rewards parameters
    * People get penalized if they are not sending messages when you expect them to
  * Danny - Might be worthwhile spinning up a small network before a push out to Medalla with a bunch of the clients to see if there's any bad behaviors that we're not catching right now.
  
# 6. Spec dicussion [32:30](https://youtu.be/_4Ry2AEzXGU?t=1950)
 * n/a
   
# 9. Open Discussion/Closing Remarks [32:48](https://youtu.be/_4Ry2AEzXGU?t=1968)
 * Ben Edgington (Teku) asked about progress around bls audit
  * Danny - Great, there's been a couple of minor issues in reports over the last couple of weeks and expect to have close to final report to be done next week. 
 * Dankrad - Looking at Medalla it seems like there is inactivity leak in progress. But doesn't seem to correspond to increase in participation that we'd expect.
  * Danny - Best guess is instability in Prysm. Seems as though every 2 to 8 epochs there's high resource consumption which is causing that instability. So you see the participation rate grow and then diminish. At least on Prysmatic's nodes, that high resource consumption is being investigated. Albeit - this is a best guess at the moment. 
  * Danny to spend some time poking around. Prysmatic team is working on an update to release on resource consumption issue they are seeing. Barnabe also might have some scripts that will allow us to look at the overall participation. 
 
# Attendees
* JosephC
* danny
* Raul Jordan
* Zahary Karadjov
* Meredith Baxter
* Adrian Manning
* Ben (sigp)
* Mikhail Kalinin
* Hsiao-Wei Wang
* Ben Edgington
* Sacha Saint-Leger
* Carl Beekhuizen
* Vitalik Buterin
* Protolambda
* Justin Drake
* Alex Stokes
* Ansgar Dietrichs
* Cayman Nava
* Leo BSC
* lightclient
* Dankrad Feist
* Aditya Asgaonkar
* Terence (Prysmatic)
* Shay
* Nishant
* Peter Gallagher (Meeting Notes) 

