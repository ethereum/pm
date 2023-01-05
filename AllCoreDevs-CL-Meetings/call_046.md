# **Ethereum 2.0 Implementers Call 46 Notes**

### **Meeting Date/Time: Thursday 2020/8/20 at 14:00 UTC**

### **Meeting Duration: 1 hr**

### [**GitHub Agenda**](https://github.com/ethereum/eth2.0-pm/issues/173)

### [**Audio/Video of the meeting**](https://youtu.be/g3fKTfBXArU)

### **Moderator: Danny Ryan**

### **Notes: William Schwab**

--------------------


# **Contents**

- [1. Medalla](#1-medalla)
- [2. Testing and Release Updates](#2-testing-and-release-updates)
- [3. Client Updates](#3-client-updates)
  - [3.1 Lighthouse](#31-lighthouse-age)
  - [3.2 Teku](#32-trinity-meredith-baxter)
  - [3.3 Prysm](#33-prysm-raul-jordan)
  - [3.4 Nimbus](#34-nimbus-mamy)
  - [3.5 Trinity](#35-trinity-grant-wuerker)
  - [3.6 Lodestar](#36-lodestar-cayman)
  - [3.7 Nethermind](#37-nethermind-tomasz-stanczak)
- [4. Research Updates](#4-research-updates)
- [5. Networking](#5-networking)
- [6. Spec Discussion](#6-spec-discussion)
- [7. Open Discussion/Closing Remarks (none)](#7-open-discussion-closing-remarks)

- [Summary of Action Items](#summary-of-action-items)

------------------------------

#
# **1. Medalla**

| **Video** | [4:55](https://youtu.be/g3fKTfBXArU?t=295) |
| --- | --- |

**Danny Ryan**: Prysm has a very good writeup of what caused the incident that caused all the other incidents. The really good part of this is that it might even be hard to simulate the stresses we created before forking and craziness, and now I think we can say all the clients are stronger than they were last week. It was also painful for us and the stakers involved, a lot of requests to update nodes, and I'm sure the operators are a little burnt out, hopefully we can see more stability.

On our list has been to client stress tests on cloud instances distributed across the world, hope to see in coming few weeks, but Medalla beat us to it, bt still hope to see more from the external tests.

I'm for keeping Medalla moving forward, but am open to other opinions.

(No one has anything specific to ask.) We've been in very active communication. I plan on writing a blog post, I'm sure Ben will keep us updated in his posts. If you are a validator listening to this, thank you. In this testnet, and probably in early mainnet you're going to need to keep your ear to the ground, watch what's going on and being active, thank you for updating your nodes.

# **2. Testing and Release Updates**

| **Video** | [7:52](https://youtu.be/g3fKTfBXArU) |
| --- | --- |

We do have a minor release coming up, the Solidity contract has been integrated into the repo and will be released. I believe that there are also two additional gossip validations that were added that took two very cheap validations from the fork choice that were elevated to these gossip conditions.

There is still work being done on network unit testing, there's a few clients integrated into this, and we're working on adding more tests.. Something that I'm keen to get into there is block range requests with complicated databases, saw some issues last week, beyond that testing ? on phase 1, fork choice testing does not exist in official format, although it has been updated in specs test repo (_notetaker's note_: may have misunderstood previous).

**Mehdi Zerouali**: We ran a community fuzzing initiative, got members to run dockers with fuzzing targets for omst implementations. Four people from community found bugs, 3 on Lodestar including memory exhaustion, now all passing, one overflow in proposer/slashing on Nimbus, and on Teku a crash that identified a lack of checks in the attestor slashing processor function.

Also made great progress on the structural differnetial fuzzing side of things, revamped the differential part of beacon fuzz that we call Beacon Fuzz v2 in Rust, managed to identify a consensus-related bug affecting the verification of attestations on Prysm, basically that particular code path didn't check for empty attestation indices. Spoke with Prysmatic Labs, and they were super, super quick on producing a fix.

Next steps are integrating Teku into v2, already have Prysm, Lighthouse, and Nimbus, hope to integrate Teku next week, we're going to deploy the state transition fuzzers on a dedicated cloud infrastruycture next week or the week after next week, and will start attacking the network side of things starting with Lighthouse.

**Danny Ryan**: In terms of 0 to complete, how would you say those structural mutators are?

**Mehdi**: After Teku and deploying the fuzzers is building custom mutators. Right now the way it works is that we're leveraging a trite (_notetaker's note_: may have misunderstood previous word) in Rust called the arbitrary trite which produces smart inputs and instructs the fuzzing engines to basically convert raw bytes into proper structs, the kind we use in Eth2, and it's been a huge help instead of having to deal with the raw bytes. So the next step for us will be to write custom mutators, basically write our own fuzzing engines. This means ditching libfuzz, homfuzz, afl, and writing our own. This will happen in parallel, we'll keep on running on our own fuzzers, so I think there's some room there to write our own. So to answer your question, hard to say, since I don't really see a completion threshold, it's more of an ongoing process. (**Mamy** asks for blog post link.) I know a lot of you are in the process of getting security reviews, some of your auditors may want to run their own fuzzing tests, feel free to link them to us, and we can point to the work we've done so there's no duplication of effort.


#
# **3. Client Updates**

| **Video** | [14:26](https://youtu.be/g3fKTfBXArU) |
| --- | --- |

## **3.1 Lighthouse (Age)**

Skipping Medalla, main improvements are:
- syncing from such a long finalized slot, increased stability, algorithms, and efficiency
now more robust. One of the main issues we had is if we had a lot of blocks and attestations causing a lot of processing, we had some processing happening on our core executor which kind of slowed and stopped the whole process, and Lighthouse would sometimes deadlock, made a queue system to pull it off the core executor, significantly more stable and runs smoother, especially in terms of the netwroking where we can handle all the messages and send them out.
- fork handling while running at head, especially in Medalla with a lot of clients at a lot of heads. Used to try and download from the head all the way back to the previous chains up to a specific rate and keep on doing a switch clause (_notetaker's note_: may have misunderstood previous word), now found a way to cache the fouled ones to prevent his happening in the future
- Added support to be able to import Prysm key stores for easier switching between clients
- various interop improvements with various clients came up which are now being addressed
- attestation inclusion rate, looks like none of the clients are at 100%, hard to figure out what cause is, will have conversations
- finished implementing gossipsub 1.1, looking to do simulations to check implementation and come up with scoring paramters, can publish afterwards for general use, the network should become more stable if the same scoring params are used by all.

## **3.2 Teku (Meredith Baxter)**

Main issues from Medalla (link below for mega issue being used to track everything):
- state regeneration: hadn't been persisting hot states, just keep in-memory cache and when states drop out regenerating as necessary by replaying blocks on top of latest block in cache, problem was that there were not controls for limiting regneration, which caused large number of requests for states, causing excessive memory and CPU usage, in some cases creating the same state in parallel across multiple threads, created a state regenration queue to mitigate number of states being regenerated at any one time and deduplicates requests. Relatedly, we found there were places in cache where should've been checking before regenrating states but weren't.
- Startup was taking too long. At startup we were walking through the block trie reprocessing states and blocks for caches, taking too long on Medalla. Skipping this regeneration at startup works ok, but still sometimes need to regenerate state and replay it a bunch of blocks, which took time, added logic to persist hot states periodically, which allows pulling rcent states to avoid processing long chains so we're no longer doing this expensive process at startup, block replay should be kept to a reasonable number of blocks.
- We found a race coniditon in fork choice processing which could corrupt fork choice data. The race condition occured when we calculated the chain hit at the same time as processing an attestation, if the order of events was just right, now fixed.
- We updated sync processing, big fix on how to decide which blocks to download. Our sync algo has been pick a peer, download blocks from the latest finalized block after chain head, problem is that if the peer drops away or returns an error, the next peer starts from finalized again, wastes a lot of time not actually downloading blocks, added a step in finding a common ancestor from which to start rerquest, makes sync more efficient.
- when test chain did finalize, ran into deadlock in block import logic which would only happen if the new block finalized would drop out of cache, now fixed

**Danny Ryan**: We don't usually asks questions here in client updates, but due to Medalla we're all learning alot, and solving similar problems, so let's open to quesitons, if anyone has.

**Mamy**: Not a question, but we did have the same problem, for example state regenration, in Nimbus, and had to fix it two weeks ago, and I suppose that some of the updates would be useful to others, maybe we can have a HackMD where we have tips and tricks for how to improve stability and speed. **Danny** agrees.

## **3.3 Prysm (Raul Jordan)**


Probably more improvements over the last week than the last 6 months.
- the thing that really helped us sync to the head and saved a lot of validators were assumptions regarding peers and determining the best branches from peers. we had some flawed assumptions around fork branches and network partitions, refactoring caches a bit, changing the structure of the cache keys helped alot. Overall the peer scoring improvements that we had were assumptions like are you requesting form good peers, if most of the netwrok is junk are you just getting junk data, that helped us get over a lot of the hurdles.
- like Teku once there was finalization ran into a deadlock issue with an order of operations where we were saving all the states upon finality, but it happened before saving the finalized root, but it should've been concurrently, leadd to people having to restart nodes since there was a context timeout in that operation that was expensive (_notetaker's note_: may have misunderstood previous). Overall seems like participation is on the edge but trending upwarsd. Community is extremely supposrtive, everyone understands implications, realizes how big of an event it was, but how great that teams could coordinate and reach finality again.

Lots of other specific details about the code that we won't get into, but now feel much more confident in our codebase than we have in months

**Mamy**: Does your bug explain why after finality where there were 67% of validators, but only 20% participants?

**Raul Jordan**: Yes. Basically people were regenrating states, and that routine ended when it hit a timeout, and we never saved the finalized root to disk, and nodes were stuck and validators couldn't really do much. It was fixed by a restart where finalized root was saved, and a fix was deployed. As well a lot of peers were droppped at the time which cause chaos, by end of the day was still at 60% participation though.

**Danny**: That was due to the long stretch without finality the cleanup operation at finality took much longer than expected?

**Raul**: Yes, it took longer than expected, and we should've been saving the finalized root concurrently.

We've also been in touch with Cloudflare. The rough time bug is what catalyzed this whole situation. Essentially we're using six different time servers for the time, and one of them was reporting a 24 hour offset, since the rough time was taking a mean (_notetaker's note_: corrected from 'median' based on clarification later) of the responses it was reporting four hour offset, which caused all the craziness and mass slasings. The team is aware of this, and Cloudflare is working on it changing to be a median or be more robust to these kinds of failures. Since then we're using system time and giving them an fyi that their clock might be off, still giving feedback but not adjusting in their interest. (Clarification with **Danny**)

**Dankrad**: If anyone is writing a guide, the good behavior for a validator whenever they query sources is not to do any automatic adjustment if there's a big difference in time. 

**Jacek Sieka** Not even small time changes. 

**Dankrad**: Small changes aren't a good attack vector since they'll be noticed long before at 1 sec/day. Since real-time clocks and computers aren't that good typically, no adjustments is probably also a problem. (**Jacek** asks for a definition of small.) Small changes in this case are probably sub-second.

**Danny**: Rough time stands to be an interesting protocol, and could be used maybe as a backup or secondary information. It's a different protocol from ntp (_notetaker's note_: may have misunderstood previous word) so it's a natural fallback, and it's also encrypted so it might not have the same issues as ntp, but my understanding of basic ntp configs from conversations with Aditya is that you generall are using a nerarby ntp server, so even if someone is attacking that it's hard to attack the whole global network. There's clearly a can of timing worms which can be opened.

## **3.4 Nimbus (Mamy)**

3 issues: losing peers, syncing performance, and high memory usage.
- Losing Peers: When Nimbus is started it subscribes to gossip, but during sync it can't verify and ? propogate the latest attestations and blocks, so we're ejected by other clients, and lose connectivity. 
- Syncing Performance: This also impacts syncing because when we subscribe and add all those blocks thousands of epochs in the fututre to our current time system which causes extra processing during the sync. Have a pr in progress, first part has already been merged, to not subscribe to gossip too early, hope it significantly improves stability and syncing speeds
- High Memory Usage: We have heard reports reaching up to 12 gb of memory in Nimbus. This is due to 2 aggressive optimization for epoch cache, which caches validators' public keys, and had many of them running at the same time, this was consolidated to not have duplicates. The other was about fork choice and votes caching. We use a proto array like everyone else, pruning every 256 epochs, but in periods of non-finality this grows and grows, maybe at epoch 250 we have 100s of epochs without finality, and cache isn't pruned, we are changing this using another optimization that protolambda suggested a couple of months ago by keeping enough sets in the ? so that you can  prune at each finalized epoch without having to wait too long for the pruning to be worth it
- Besides those, we are also keeping maintainence of the old multinet scripts, the ones that were used in the old interop event, in order to create small testnets, right now Lighthouse and Nimbus to debug specific gossip issues, looking to add Prysm in fututre. Besides that, we are setting up a fallback so that if we have a critical Nimbus bug, we can cahnge validators to other clients, so that we do our part keeping up to the 66% of validators.

**Danny**: confirms that Nimbus is following the head and reasonably attesting.

**Zahary Karadjov**: confirms that personal node made last 10 attestations.

**Age**: We (Lighthouse) don't kick you if you're subscribed to any gossip sub topics while syncing, we do the same thing. This suggests that the subscrition to gossip might not be the problem. 

**Zahary**: Investigation found it is the cause for disconnection from peers, for relatively severe reasons. We considered timeouts, by spending significant time processing something. (_notetaker's note_: may have misunderstood previous sentence)

## **3.5 Trinity (grant wuerker)**

- Past couple of weeks working on node operation, added the ability to restore the fork choice context from the database, made simplifications to node configuraiton, working on fixing some things in network layer, like getting noise to work with other libp2p implementations, working on sync performance , also splitting out Trinity components of eth2 to a separate repo.

## **3.6 Lodestar (Cayman)**

- We put out an update on Medium discussing Medalla. Generally speaking, we weren't able to sync to head during the Medalla incident. I think our syncing algos and code need a deeper look, we would love any HackMD that gets put together, we will also be looking at other clients to see what they do with syncing, will refactor with that.
- gossipsub 1.1 is on ice, needs to be integrated into the js libp2p ecosystem, looks like end of this week or beginning of next can make a new release with new libp2p release for js. Lots of interop tests and test in general.
-  Fixed a bug in discv5 that was probably source of some peering issue, sending nodes to the wrong distance.
- Moving forward - looking at blst, ideally would have something to swtich between native code and a wasm-built pure C implementation, don't think there is a pure C implementation yet, but said that's a direction they're thinking of going, will look at when put out.

## **3.7 Nethermind (Tomasz Stanczak)**

- Added another full-time senior dev, should catch up faster, has been working on deposits. Should catch up quickly

#
# **4. Research Updates**

| **Video** | [38:51](https://youtu.be/g3fKTfBXArU?t=2331) |
| --- | --- |

**Danny Ryan**: Hsaio-Wei has been working on a doc for must-haves and nice-to-haves between now and mainnet, shared it with most client teams, we will put it on GitHub.

**Afr Schoe**: Some points about how to move forward, and learnings from Medalla and other testnets. One thing is that with Medalla being main testnet, clients should consider moving to a stable or better release track for the public testnets or upcoming mainnets, and have other branches for other features and optimizations. I don't have a recipe for this, there are probably many ways to approach, but what I believe is really important is that we're moving towards a potential mainnet launch, client teams need to come up with strategies for stabilizing their codebase, how to prevent breaking things that were working so that we're not in an endless loop of optimizing and breaking things.

We always had in mind that if something goes wrong in mainnet we could always basically restart with the same contract and just a different genesis time, thinking of taking a step backwards and calling it a mainnet candidate instead of calling it a mainnet launch, that it could be mainnet and use real ether, but if something goes wrong then oops. Anyone making early deposits should be aware that spending time maintaining validators is at their own risk, they could lose money to infrastructure and time, but won't lose deposits on restart, though.

What happens if we are like half a year into mainnet and there's a lot of slashing due to a bug in the spec or a client. I don't have an answer, but we need strategies tp deal with this.

Lastly, I was surprised that there was no Prysm lauchpad, I would encourage all clients to have a launchpad in the name of decentralization. In case one fails or one is better than the other, or different tooling preferences, why not have multiple launchpads instead of having an official launchpad.

**Danny**: Some of this is a larger conversatoin, but are there immediate points?

**Dankrad**: We don't want people to think that we'll turn it back whenver there's a mass slashing - that leads to complacency. For example with regards to distribution of validators. I think it would be better to raise the stake somehwat, and if there is a massive bug in one client and lots of people get slashed for using the same client, then, well, they shouldn't've done that.

**Danny**: It's a tough balance. We have network restart in our back pocket in the early stages, especially because there's no transfers in the early phase. The public framing in terms of that is certainly... debatable.

**Carl Beekhuizen**: Tracked down launchpad bug that caused some people to have double deposits, stuck waiting for available dev time, should be fixed as we speak, should have movement soon. In terms of launchpad decentralization, certainly keen on it and in the long run it's a smart move, but in the short term might be better for client teams not to have to worry about it, maybe we can come up with standards and fill in whatever tooling people feel like they need supported in the launchpad.

**Danny**: More tha clients having their own launchpads, I also expect other entities like MyEtherWallet and MyCrypto might very well support flows like that, I don't want to put that ectra requirement on them (_notetaker's note_: sound like intent is to the client teams) today. **Carl** agrees. **JospehC** makes point in chat about watching out for scammer laucnhpads, **Danny** agrees, adds scammer deposit contracts. 

**Danny**: I think maybe the main issue in promoting that is that Prysm has a pretty sophisticated launchpad, other clients do not, we might see some additional client assymmetries if we go that path.

**Raul Jordan**: I'd like to make a quick point. There's been discussion regarding migrating keys between clients and how it's important, but it's also important to discuss migrating slasher prevention information between clients, can we talk about that now?

**Danny**: Yes, this is criticial. In most scenarios if you turn client A off, wait a few epochs, then turn in client B, you wouldn't be doing anything wrong, but in the incident on Friday though, this property probably didn't hold with the time skews, since one was in future and the other in the past. Michael Sprow (spelling?) put out a doc for minimal interchange format, and has done some dev work in Lighthouse, if you haven't seent this document and you're working on this, you should. I'm encouraging this type of standard to be elevated to EIP/ERC zone, like some of the wallet keystore standards we've had. Also putting some effort into documenting is also a priority, will see if the EF can spend some time on putting out standard docs once some of the interchange format has been worked on, working on going from client A to client B and documenting our experiences. If we can agree on some stuff, these docs won;t become outdated.

**Carl**: In Prysm at the moment, to what extent are wallet stores being used?

**Raul**: We utilize the derivation path, account index, withdrawal key, validating key, we don't allow for multiple wallets encoded in the derivation path by design. We are still using wallet stores with next account in a JSON, use that to keep track of the next account to be created.

**Carl**: Over time these standards have drifted together and are very close, but use different decryption methods, due to Unicode support in keystores, but asides from that and next account, I think these are the only two differences between the standards. and that we should try to collapse them into one. **Raul** agrees to be in touch on Telegram.

#
# **5. Networking**

| **Video** | [52:56](https://youtu.be/g3fKTfBXArU?t=3176) |
| --- | --- |

**Danny**: Age and proto met with some of the Protocol Labs guys about tuning the gossip sub v1.1 params, some of that will be maybe some wise defaults, ideally we can some of these clients working in simulation framework and tune these a little bit more.

**Age**: In the design of these scoring parameters, something we need to discuss comes up which is subscribing to topics while syncing, particularly on subnets. If we're subscribed while syncing we can't verify the messages, the client ends up acting as a sink or censoring node, and stops propogating messages, which degrades the network, would be optimal not to subscribe while syncing, or to modify the scoring paramters to allow it. Curious which clients are subscribing during sync and if it's necessary.

**Nishant**: Prysm subscribes, but usually ignores, so it might look like censoring. Probbaly could subscribe after, but complicates logic, for example on resync, and need to unsubscribe and subscribe. **Age** confirms a similar issue, asks if they subscribe on subnets. **Nishant** confirms no subnet subscription until sync.

**Jacek**: The other question is how do you decide you're fully synced?

**Danny**: You can know that you have all branches from all different reported peerss, you can know something recent was finalized. These things are at play, like the difference between syncing and not syncing, between intial sync and chasing some bracnh you found. It's definitely blurry.

**Jacek**: Also, when you're close to end, and might start producing on a slightly different branch, those blocks might not propogate as well, might get censored, it's a little bit of a death-spiral as well.

**Age**: At head if you miss three or four slots, that's fine, it's not that strict.

**Jacek**: But then in an event like Medalla, three of four slots seemed reasonable, perhpas in order to recover from an event like Medalla automatically, makes it a really hard one when policies are too strict.

**Danny**: Try to use networking channel on Eth R&D channel for v1.1 stuff just so it doesn't get lost.

#
# **6. Spec Discussion**

| **Video** | [58:16](https://youtu.be/g3fKTfBXArU?t=3496) |
| --- | --- |

**Hsiao-Wei Wang**: Quick update: a second version of the Solidity deposit contract has been released and been ported back to the spec repo, the only change is metadata of the contract, the contract bytecode remains the same. First release has been used for Medalla, but if you want to initiate a local testnet, please use latest bytecode (link below). This should be final version before phase 0 launch. Would be nice if you do a sanity check against a local testnet.

**Danny**: The functional bytecode is the same, just the metadata has been changed a bit, formal verifications have been run on this slightly modified version.

Please keep information shring high, we're solving the same issues, thank you and congrats on stabilizing.

#
# **7. Open Discussion/Closing Remarks**

| **Video** |
 |
| --- | --- |

No discussion.

--------------------------------------

# **Appendix**

## **Resources Mentioned**

- https://medium.com/prysmatic-labs/eth2-medalla-testnet-incident-f7fbc3cc934a 
- https://blog.sigmaprime.io/beacon-fuzz-07.html 
- https://github.com/PegaSysEng/teku/issues/2596 
- https://github.com/ethereum/eth2.0-specs/tree/dev/solidity_deposit_contract 

## **Attendees**

- Afr Schoe
- Age
- Alex Stokes 
- Ansgar Dietrichs 
- Ben Edgington
- Carl Beekhuizen 
- Cayman
- Dankrad
- Danny Ryan
- Grant Wuerker
- Herman Junge
- Hsiao-Wei Wang 
- Ivan M
- Jacek Sieka 
- Joseph Delong 
- JosephC
- Justin Drake
- Lakhsman Sankar
- Leo BSC
- lightclient
- Mamy 
- Mehdi Zerouali
- Meredith Baxter
- Nishant 
- Protolambda
- Raul Jordan
- Sacha Saint-Leger
- Terence (prysmatic)
- Tomasz Stanczak 
- Vitalik Buterin
- Zahary Karadjov

## **Next Meeting Date/Time**

Thursday, September 3, 2020.
