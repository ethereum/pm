# Verkle meeting 1

## Meeting info

May 5, 2023, 13:30 UTC

Original Notes: https://docs.google.com/document/d/1D2GtzI3q9btZd1ZOzCsWPsvzCaA-fCLZdXDtawoPUyM/edit#heading=h.hz4l515c4h91

Recording: https://drive.google.com/file/d/1z3G5M6aaCEb91jmYjAN3Fz-ZPeK1P47k

## Agenda: 

1. High-level overview of where Verkle is today
2. Teardown of Beverly Hills
3. Overview of conversion methods
4. Preimage distribution
5. Where should client teams get started
6. Open discussion

# 1. High-level overview of where Verkle is today
- We have a testnet live with proofs in blocks (Kaustinen)
- Lighthouse & Geth combo live on Kaustinen
- Have spent past few months focused on performance optimizations (h/t Ignacio), and now only experience a 40% overhead when replaying blocks compared to MPT (tbd to use more recent blocks)
- Now we are focusing efforts on the actual MPT->Verkle migration (though Nethermind is doing work with the sync)

# 2. Teardown of Beverly Hills
	Confirmed: no one objects to the teardown. 
	TODO: make sure everyone is aware that Beverly Hills will be taken down

# 3. Overview of the conversion methods 

Guillaume: There are four methods, but in a way really two methods. Each has two sub-methods, sub approach

Quick summary of each method:
1. Overlay tree: which is a method that moves from MPT to Verkle little by little over time
2. Conversion node method: small number of very powerful computers do the work and then send the results over the network. Up to each node to then download it and catch up.
3. Local bulk: wont go into much detail. Just like conversion node, but everyone does it 
4. State expiry method: transition doesn’t really happen. Like overlay, except you don’t have a process that moves values from MPT to Verkle. When you want to read the state, you just go into the Verkle tree first, if you don’t find the data, you go to the MPT. Method is interesting if state expiry gets implemented. The data that used to be in the MPT  that was not clobbered by the Verkle tree can be downloaded by passing proofs at a later stage. All described in the state expiry EIP draft. 

More detailed walkthrough of each method:
Overlay: start with an empty overlay tree which is verkle. And you have a base tree which is read-only. As the chain progresses, you just convert leaves from both the account tree and the storage tree in storage iteration order and you move them to the overlay tree. If you want to read data, first you hit the overlay verkle tree, if you dont find it then you go to the base MPT tree. This goes on until the whole iterator has gone through the entire tree. Once its done all the data has been converted and placed into the overlay tree. And as a result the data can be deleted. Currently estimated that it should take no longer than a month to complete.

Conversion Node method: specialized nodes that do the translation. One of them just stops and does the conversion. When the conversion is done, the others can start downloading it. And then they are responsible for replaying every block between the moment the conversion starts. Advantage: no longer dependent on the slowest nodes of the network. But problem: you need some social mechanism to ensure the conversion was indeed correct. And its not really easy to handle. We’ve tried to make prototype. Difficult to implement around the fork end. A lot of people tend to download the release before the fork close to the fork. If you have to replay everything then itll prob end past the fork. If a big enough chunk of the network missed the deadline, then you have a long time without any blocks produced. So its a bit risky and a bit hacky the way it was implemented. So thats why this method is not favored. 

State Expiry: it’s basically the overlay tree except you don’t touch the base tree. You keep hitting the overlay tree first. If it fails, you go into the MPT. Eventually the MPT will be deleted from the view. 

Questions from the chat:
Karim: 
What will be the impact regarding performance to have to check the overlay every time before reading the MPT as fallback?
Guillaume: 
Assuming it will be twice as slow, but hopefully faster than that

Potuz: 
what’s the failure mode for this? you screw up at week 3 and what are the safety mechanisms to prevent starting over? is this explained in the doc (sorry should read before)
Guillaume: 
if you find a screw up 3 weeks into the conversion, you have no choice but to download a new conversion and start over. If you screw up before the finalization time, you can go back. But if you do it after finalization time, then it’s same as current MPT world you have to go through the mitigation process. 
Pari: 
@potuz, depending on the type of failure there wont be some safety, Assuming you loose your entire DB, you'd just know till where you have to convert to be considered "at head". So if you have the slowest node on the network we considered while setting the values, then you'd pretty much be 3 weeks behind. If you have a relatively fast node, you should be able to convert more than what is necessary and catch up to the rest of the network.


Łukasz Rozmej: What is an acceptable transition time? 1 month? 3 months? 6 months? Does it make sense to have Verkle Tree "snap sync", so you don't have to replay blocks, but downalod state?


Lukasz: I’m all for the overlay method. Better to do it in-protocol. Otherwise it’s messy. The transition time. What is acceptable? 1 month or 6 months? Etc. 
Guillaume: Upper bound you guys tell me. 1 month is ok. 3 months is ok?
Lukasz: should be configurable: how many leaf nodes are included per block. And then when we are close to our optimizations with the boundaries we should measure it. 
Guillaume: I have a machine with slow I/O, and takes roughly 20 hours to convert. This is with the older bulk conversion method. With the overlay tree, I’m still debugging it so cant give numbers yet. But I expect 1 week is reasonable expectation. 1 month is safe bet. But thats on a slow machine, but still x86. Bottleneck is i/o. 
Lukasz: what is the storage layout used?
Guillaume: we are about to change it in geth. So hard to answer. But closer to the geth layout. It’s a path-based layout. 


Guillaume: cant promise we can support raspberry pi, but targeting rock5b. 


Lukasz: if someone spins up a node during the transition period he needs to replay all the blocks
Guillaume: in the conversion node method yes.. they have to replay the blocks
Lukasz: will we have some kind of snap sync
Tanishq: im not sure we will be able to add proofs to the blocks before the conversion completes? That cant be used for healing. 
Guillaume: when you do overlay, the tree starts empty so you can already produce proofs. But just for the overlay tree.


Potuz: suppose we are past the fork and everyone is running on verkle and I want to start a new node. Whats the mechanism to back sync this node. All the way back to genesis. 
Guillaume: If you go backwards, you can indeed start backfilling the state as you go up the chain. Or you can simply download a full view of the state at a given point. And only backfill up to that point. 


Lukasz: will there be a state downloading mechanism? 
Guillaume: yes the point is to have something like snap sync, except the healing phase is replaced by the proof you found in the block 


Potuz: but now I want to see a transaction from 3 years ago on my node. How?
Guillaume: if its pre-verkle, you have to do a full sync
Tanishq: this is the same as it is today? You have to do a full sync to get the info on this transaction from 3 years ago. 


Lukasz: with verkle trees we are now bloating the blocks. How much bigger will the blocks be? 
Guillaume: Estimate is around 100% more. 


Lukasz: looking at the DB size. Blocks are about half. Verkle tree will probably expedite history/state expiry?


Guillaume: something analogous to snapsync will be provided

Barnabas Busa: Would archive nodes have to keep a pre-verkle state and a post verkle state of the whole chain post verkle transition?
Guillaume: depends on the conversion method. the pre-verkle state will be required during the transition. 


Gottfried Herold:
A quick remark (because I would forget until next meeting otherwise):
In the overlay method for MPT -> Verkle conversion, there is no reason to start the automatic, slow conversion immediately after the last valid MPT block.
Basically, from T=0 (last MPT block) to T=N_1, only all new data and all data that was touched by the new blocks gets added to the Verkle tree. The automatic conversion only starts after T=N_1 for appropriate (possibly dynamic) N_1. This has the advantage that at T= N_1, the last MPT block has finalized.
the set of preimages that needs to be distributed does not change once the last MPT block has finalized. We then have time to collect and distribute these until T=N_1.
This slows down the conversion somewhat, but since we are talking ~1 month anyway, the additional delay does not account for much. Or am I missing something here?
Guillaume: 
that's correct, we don't have to start the transfer right away, and the list of required preimages will then be known. Good points.


# 4. Preimage Distribution
Pari: as long as we can make sure it’s easy to verify, we can probably use a system of CDNs similar to checkpoint sync. We can also share this by torrenting as another example. It doesn’t matter where users get the preimage from, as long as it’s easy to verify. 
Lukasz: the problem is the preimages will already be invalid by the time you get them. 
Pari: so yes we have to rely more on CDN methods
Lukasz: why not use snap sync
Dankrad: why not make an upgrade of the client that starts recording preimages from them on? So you only have to distribute historical preimages
Lukasz: one potential problem, clients can record preimages but would have to be a hard fork. Bit problematic. 
Dankrad: Just has to be an agreed date. Sort of soft work. Certain point in time that we start running this version. 
Lukasz: there will be node that miss this. 
Dankrad: then they have to get the diff from somewhere else
Guillaume: has an EIP open for this. If the date is agreed its like a fork. Not a proper fork. Just a feature thats get added. They need to update. And if they dont update its the same as like in the merge. They would simply drop off the network. 
Lukasz: but they still need to be able to download all of the diffs when they come back online

Gottfried Herold: Do you need the preimages only for the conversion due to "touched" or due to "conversion"?
G11tech: conversion i think
Guillaume Ballet: yes, and you only need the preimages if you go for the overlay method

# 5. Where should client teams get started
Guillaume: if you want to get started. Look at the crypto. This is what the whole effort is built upon. Go to Kev or Gottfried if you want to implement the crypto. 
Try to join Beverly Hills if you are an EL dev
Try to join Kaustinen if you are CL dev (bc right now we only have Lighthouse)
