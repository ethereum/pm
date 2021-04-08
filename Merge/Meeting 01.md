# Merge Implementers' Call 1
### Meeting Date/Time: Thursday, April 1st, 2021 14:00 UTC
### Meeting Duration: 1 hour 30 min
### [Agenda](https://github.com/ethereum/pm/issues/290)
### [Video of the meeting](https://www.youtube.com/watch?v=b3hfgLa_GHw&t=3s)
### Moderator: Mikhail Kalinin
### Notes: Shane Lightowler

# Intro

**Mikhail Kalinin**

* Welcome everyone to the first Merge Implementers' call. 
* This call is technical discussion on the merge. Governance discussion occurs on the All Core Devs call.
* Today's discussion is focussed on the application layer. Consensus layer is covered in different calls.

## Discussion on Rayonism

**Protolambda**

* This Tuesday just gone we announced Rayonism - ETH Global scaling hackathon in two weeks time. 2 targets... First - run a testnet with Eth2 nodes that utilise Eth1 nodes for the application layer as per current Merge spec. Second target is to development additions eg Shard data.
* Value proposition is getting everyone involved in development for a multi-client Merge testnet.
* On the Eth1 side a new API will be implemented - 4 new routes that have been discussed at length already. We want to iterate these.
* On Eth2, take existing phase 0 implementations, modify them and put them to use on Goerli. When running, take our time with the prototype, think about the transition, implement different block types, do the implementation work for the fork.
* If we can get this running quickly, using the EVM on PoS, we will have a working implementation with more complete clients to test against. Stabilise essentials eg RPC and in-block sharding prototype.
* Next week we will plan in an early bird call to run through early organisational things.

**Mikhail Kalinin**

* We'll work on the spec for Rayonism over the next two weeks. Stay tuned!
* Any questions?

**Vitalik Buterin**

* To confirm, the goal of Rayonism is to make a prototype of a post-Merge combined application/consensus layer application, not to do transition?

**Protolambda**

* Yes, that's right.

**Danny Ryan**

* The primary metagoal is to have teams just dig in, understand specs and the project complexity, how things fit together and how things feed back into the process of specifications. Come mid/end-May we want an ironed out spec and roadmap.

**Dmitry Shmatko**

* I'm working on withdrawals - I have modified catalyst, solidity and teku and couldn't deploy to any testnet - only itself. Can I still work on this?

**Protolambda**

* Tentative yes. I know your prototype requires additional opcodes...

**Dmitry Shmatko**

* Yes it's not on spec, there are several modifications including RPC...

**Protolambda**

* I think we can get the testnet running early, but it's up for discussion which opcodes go into the testnet. So if you do include these opcodes we can prototype the withdrawals process as well.

**Danny Ryan**

* And even if it doesn't go into a shared testnet or spec for now, we can run some transient testnets in isolation.

**Dmitry Shmatko**
 
* Cool, I will participate with withdrawals.

# Application Layer Discussion
 
## Design Doc

**Mikhail Kalinin**
 
* We will now go through the main sections of [this high level design document](https://hackmd.io/@n0ble/ethereum_consensus_upgrade_mainnet_perspective).
 
**Vitalik Buterin**
 
* Is there an intention to create a parallel doc from the consensus layer perspective?

**Danny Ryan**

* Eth2 specs are very beacon chain centric. Eth2 implementers are very familiar with that. Could add additional notes but ddont think there is immense value in this.

**Vitalik Buterin**

* We don't want an imbalance in the levels of specificity between application/consensus layer.

Right now what is there for the consensus lawyer perspective that covers like say the transition condition and beacon block changes and those things?

**Danny Ryan**

* You're right you're right in that yeah right now there's only really the the consensus perspective which really doesn't get into like the design document where it's saying like you actually use these methods to communicate throughout the application layer so i think there's a parallel but i think it's probably a quarter of the length so we could probably write it up and has more to do with like these methods 

**Vitalik Buterin**

* Okay makes sense

**Mikhail Kalinin**

* I also think that the transition process should be described like for both parties like in details so what one party is doing then what the expectation from the application layer and what consensus there is doing at this moment so that would make a lot of sense to give the and the understanding of the whole process so yeah but rather than the spec in the beacon. In the Eth2 specs repo i think we like don't have anything more recent in regards to that. 

## New block format

**Mikhail Kalinin**

* Yeah okay so yeah i think we can start with like new block format yeah there is like the interaction between the consensus and application layers it has like four messages. But i would start from the we can get back to this like interaction i would just start from the new blog format because it looks like a simple thing so yeah there could be debates about extra data and so forth but what was proposed is to just set a bunch of fields that are related to the proof-of-work consensus to the Eth hash just set to some constants and keep them on entirely on the application layer in the application block and what will what is going to be exposed to the consensus to the beacon block body is the like the actual block the actual main net block with all these fields just thrown away. So and what will be on top of that is the block hash is the hash of this block 
* so it implies that the application layer once it gets the new application payload from the consensus part will assemble a block and check that this block is assembled correctly with regard to these constants by checking the the hash of this block is equal to the one that is given by the consensus part. Also worth mentioned that the consensus and application block trees are has a one one to one mapping so every like beacon block has the reflection in the application chain and all the forks of the like beacon beacon chain are reflected in the application chain as well. But the beacon chain is the primary one here and the application chain is secondary. 

**Micah Zoltu**

* Why does the application layer have to hash it? Isn't it receiving it and through a trusted channel? Doesn't the application layer trust the consensus layer to give it a valid block, in terms of things like hashing the block.

**Mikhail Kalinin**

* It trusts but you don't trust other peers that send you a block so. This is a part of block validity process so this is one of the validity conditions.

**Danny Ryan** 

* The hash included in the payload but the the consensus layer doesn't actually check the consistency of that hash with the payload and it's actually asking for the application layer to check the consistency of that.

**Micah Zoltu**

* I see, out of curiosity why is it that direction since the consensus layer receives the block first is that correct?

**Mikhail Kalinin**

* Yeah that's right .

**Micah Zoltu**

* So wouldn't that create a dos vector sort of in the sense that the consensus layer is doing work to pass the block onto the application layer before doing a very simple check to make sure it's reasonable?

**Mikhail Kalinin**

* It does not create a dos vector because before this part starts to work i mean this application block processing part, the signature that is on the beacon chain, the validator signature under the required...

**Micah Zoltu**

* Okay so the condensed layer receives a block verifies the signature which means we have someone to slash if it's bad and then it sends the block down to application layer and the application layer does the actual validation of the block itself is that accurate?

**Mikhail Kalinin**

* Yeah that's correct but yeah not the slashing part of it so it's not going to be let's just or front the block will program.

**Danny Ryan**

* But it's like if you did a proof of work on an invalid block that is going to be gossiped around the network but then it would be quickly dropped because the like and they would be seen as invalid and there's a huge opportunity cost in in doing so it's kind of like the analog.

**Micah Zoltu**

* Okay because you can only produce one block for your slot and so you sign if you sign two blocks or slot then you get slashed and so if you sign a bad block you're just wasting your slot basically, is that right? 

**Danny Ryan**

* Correct and there would be a you know minor amount of work you can do on the network similar to like wasting your proof of work block.

**Micah Zoltu**

* Okay.

**Mikhail Kalinin**

* This actually could be verified by the beacon chain part but it needs to get rlp on board and catch up to 56 to do this 
* So yeah it's proposed to to make it the responsibility of the application layer.

**Peter Szilagyi**

* But hashing a block is on the order of microseconds so i don't think it's really relevant you can just hash it and done.

**Vitalik Buterin**

* It's not about execution time it's about like where the code complexity lives i guess.

**Peter Szilagyi**

* From a geth developer perspective i would say that anything i get from somebody else i'm going to check anyway. i don't care whether i should check it or shouldn't.
* I think it makes sense for ethereum clients to actually validate that the requests are meaningful and not just blindly trust everything.

**Vitalik Buterin**

* Actually one one quick question here so when a beacon chained client passes a block the application client like over that wire is it is the intent for it to still be in an ssz form or in like a list of fields form or is the intent for it to already be an rlp form?

**Danny Ryan**

* It's like a json payload at that point.

**Vitalik Buterin**

* Right where the json payload just contains like the fields so it would be so okay so that so the application clients would be doing the rlp-ing.

**Danny Ryan**

* Correct they would bundle up the fields it gets plus some of these constants like difficult equals one and a couple things like that.

**Vitalik Buterin**

* Okay that makes sense.

**Mikhail Kalinin**

* Just a quick note for non-devs who may be watching the recording, i guess there's a slight abuse of notation when we talk about consensus layer and application layer like traditionally the application layer is what you think of uniswap and maker and all the dapps in this case for us the application layer is kind of the evm layer so it's the management of the evm mempool the management of the evm states and and and all the execution layer and then the consensus layer is just the beacon chain layer and the proof of stake.

**???** 18.39

* Yeah i actually added a little bit of a glossary in the beginning of this document so just describe exactly that what is it like the the consensus block application block yeah it's very basic but yeah so we use this term so that it's more consistent.

**Mikhail Kalinin**

* Yeah thanks for this very helpful comment. i forget to mention this like the notation you know implications.

**???**

* Can we find a better name for it 

**Mikhail Kalinin**

* For the application layer

**???**

* Actually a bad name i think because that's already in use

**???**

* Execution layer?

**Peter Szilagyi**

* Yeah something like that.

**Mikhail Kalinin**

* The execution there it's not it's not actually about the execution only it will cover much more than the execution like the core thing is the execution right...

**Danny Ryan**

* We should probably take this one offline yeah i think that we will we can debate this for a while.

**Mikhail Kalinin**

* Yeah for for the record it covers like the transaction pool it covers the man the chain management history retrieval so much more than the execution.
* Okay so peter mentioned that the geth like in the good design the geth would validate everything that is coming from the consensus counter party right?

**Peter Szilagyi**

* Well i mean obviously things that we can validate i mean whether something is a chain head or not we're just going to have to trust you on that.

**Mikhail Kalinin**

*  Okay yeah yeah i was just like you know i i was just going to mention this that there will be a trust you know between consensus and evocation anyway and it's going to be a trust trusted communication channel between them

**Danny Ryan**

* But yeah any any sort of consistency checks and things like that are extremely valuable especially if they're cheap.

**Mikhail Kalinin**

* Right and i guess well if the consensus layer will check the block numbers right that they are consecutive and check the parent hash that is matching the head of the the previous head of the chain so the geth will do the same checks actually and check the gas limit formula so yeah that makes sense i mean to do in both sides so it doesn't take much computation resources yeah okay so some particular fields.

**Peter Szilagyi**

* Sorry quick question you probably possibly will get to this later too so feel free to tell me to but basically currently the beacon chain node would notify the eth1 client of these various event does that mean that there's a one-way communication where the eth1 client is running the server and the rpc server so to say and if your client dials in as a client.

**Mikhail Kalinin**

* Yeah right yeah it at least it proposed this way like the unidirectional communication but we can think about like b-directional bi-directional if it makes sense to do it.

**Peter Szilagyi**

* No i'm just asking for clarifications on documents i'm not saying we should do it this way or that way.

**Mikhail Kalinin**

* Yeah so currently it's unidirectional communication so the consensus layer just sends the message and waits for response and according action from the application part.

**Danny Ryan**

* Yeah i think this is a natural design because like the whole point of the beacon chain is pretty much to be like this is the head i want to build a new head it's kind of the driver in that respect so i think it simplifies reasoning about it that way.

**Peter Szilagyi**

* Yes there's one slight detail for example if i just start on the eth1 client then the client needs to wait for these two clients to do something otherwise it's just idling so it cannot initiate any actions which means that i must wait for a new head rpc call and just wait until then so i don't have the capability to just tell these to client that hey i just crashed i just recovered give me a head that's not necessarily a problem and i'm just again it's just exploring the design 

**Danny Ryan**

* Yeah interesting i mean i would yeah okay 

**???** 23.33

* You can't even do that using rpcs if you're streaming endpoints like it doesn't have to be that one party is always the initiator

yeah of course it's just it's just a thought

**Danny Ryan**

* Yeah i presume if you do crash and you restart you're going to get a new head very soon but the also the well we can talk about this but i think the the beacon chain would then be kind of stuck because it wouldn't have its end point so it would be no it no it's just be waiting all right yeah recovery there 

**Peter Szilagyi**

* This means you've got gas crashes and restarts and i'm going to wait for the beacon chain then the beacon chain will be stuck because it just lost his guest and then yeah anyway so it's just a funky detail yeah 

**Mikhail Kalinin**

* That's right and if you have like two separated pieces of software then this is still like a client so the consensus node and the application node this is still one client and if the application part just to crash then we can say that the entire client crashed so yeah it should be some kind of status message or ping or whatever or yeah or we can put a response into one of these messages because they will be frequently sent by the consensus layer like the block on your head that the application crashed and act accordingly on the consensus part so yeah but i think that this is the like implementation details more so and for consensus purposes for for chain management purposes like this unidirectional channel should be enough to go with.

**Peter Szilagyi**

* So although it seems like an implantation detail the reason i kind of want to highlight that it's not necessarily because for example synchronization code or events that we react upon they also depend on what we can do so it's not just something internal it kind of some what drives synchronization to it and it's essentially we can do it either way so it's there's no good or bad solution because obviously i know design will work it's just the implementation kind of has to follow the capabilities of the api anyway.

**Mikhail Kalinin**

* Okay yeah so yep need to think about it more i guess.
* okay so some fields here difficulty and nouns are yep deprecated and set to constants y difficulty is one here it's set to one instead of like being zero i think it makes some some sort of sense on the like network but let's not go into details like it would make sense to keep the difficulty increasing for the probably if status message and that is sent by the application client and by current ethereum client one once it starts and connects to the other peers so i think we can not like focus on this now so time stamp will be when we communicate it from the consensus part it's going to be the the time stamp of the current slot where the block is producing or executing so there will be no rewards for the block and yeah transaction fees or transaction tips after 1559 will go to the beneficiary or to the coinbase so that's it about the block processing part.

**Danny Ryan**

* There are rewards but there's no rewards given out to like the no issuance given out by the the evm you know the to the coinbase anymore it's all handled on beacon chain side to the validator.

**Micah Zoltu**
* So does will that change when the coinbase's balance increases from the perspective when it's usable?

**Vitalik Buterin**

* Would this be an implementation challenge well okay i guess a block would be aware of whether or not it's first transition because i can check its mix hash

**Mikhail Kalinin**

* Could you ask the question once again?

**Micah Zoltu**

* Sure to take a step back currently when you are a block author you are rewarded with ETH fees and i don't actually know if that happens at the beginning of the block or the end of the block but you definitely can spend them as soon as the next block happens and is that changing with when we move the consensus and therefore block rewards?

**Danny Ryan**

* So there's still there's still a beneficiary there's just zero issuance that beneficiary the fees still go there.

**Micah Zoltu**

* Okay and the fees will be accounted for in as part of the state route like in the accountant tree right and so it'll still be usable like right away by users is that accurate?

**Danny Ryan**

* It's usable in the same exact time it's used usable now.

**Mikhail Kalinin**

* The only thing that changed that we don't have this 2 ETH per block like we have now 

**Micah Zoltu**

* Gotcha okay and so i'm assuming the consensus layer when it tells the application layer to make a block it will send and use this coinbase as part of that package is that correct?

**Danny Ryan**

* Correct.

**Peter Szilagyi**

* So i just wanted to highlight something i i'm guessing most clients are already capable of it so essentially once we set the block subsidy to zero or maybe even with 1559 on mainnet an interesting thing happens that all of a sudden you can have blocks multiple blocks having the same state root hash this currently on mainnet is impossible because the ether is always accumulating so you cannot have repeating hashes but this for example can happen on click networks like Goerli and Rinkeby and it's a pain in the ass to always make sure that the clients handle it correctly so i just wanted to emphasize that once we remove the block subsidy every empty block will actually produce the same root hash as the previous one which may or may not be desirable i mean it's fine just clients need to be aware of this work.

**Vitalik Buterin**

* If we want to be lazy we can just decrease the subsidy to one way right? 

**Peter Szilagyi**

* Well in theory yes but in practice 1559 if it starts burning things we still might end up with a duplicate state.

**Vitalik Buterin**

* Wait but are the base fees in 1559 paid by the transaction senders and not the coinbase? 

**Micah Zoltu**

* Yeah but a coin you could have a coinbase send one transaction that burns exactly with the fees so the state root would be the same which is actually an optimization you could make as of 1559 because you can mine you can get your first block on the wire much faster because you don't need to actually calculate the state route.

**Vitalik Buterin**

* So this is this is this is theoretically possible even before the marriage has never ended right?

**Micah Zoltu**

* Correct assuming 1559 goes into London and in fact i think this is would be wise for miners to implement this because it gives them a slight edge.

**Danny Ryan**

* One more kind of related follow-up is that the if you have the the overlay beacon chain and you have this kind of application chain embedded inside of it the application chain i think at this point in this current design could have two branches that have the same roots at the end of them because you essentially you don't have this proof of work you don't have the nonce you can have the same application payload on two different branches from the same parent and so there we said there's like a one-to-one relationship i think we could probably make it potentially there was a one relationship but including something in there but it is subtly not a one-on-one relationship but we can maybe talk about that in another context.

**Mikhail Kalinin**

* Right so it will have like two block hashes like it will have identical block hash right?

**Danny Ryan**

* Which is i'm almost certainly fine because if the beacon chain says that head to this and set head to this from the layer from the perspective of the application layer it's like it's totally it's the same thing it's just the beacon chain can be consensus on the same state in terms of the application layer so again that's probably actually not much of a design issue.

**Mikhail Kalinin**

* Yeah but worth considering anyway yeah.
* okay so we went a bit forward the external force rule it just means that there is no more total difficulty focus rule and the application layer tracks the messages from the consensus about not notifying that there is a new head and it must do the rework or to not the real work if it's not needed according to what's you had to the observation of the consensus there is currently eased so that's it sounds pretty simple and but i guess it will be big chunk of work to you know to make the current minute client to modify it to like follow this external for choice rule but...

**Peter Szilagyi**

* In theory it it's okay as long as one specific condition holds and actually that was my question. so by setting the difficulty to one that's actually nice because we can still track the longest chain the question is can it happen that the beacon chain will tell me that up until now i had a chain of three blocks and the new head will be block number two on the side chain? yes it happens that it shortens the chain economical chain.

**Vitalik Buterin**

* Yes.

**Mikhail Kalinin**

* Okay and so yeah the difficulty will not work because in the like current focus role it's very simple and each block is like self-sufficient in terms of the fork choice so it adds some difficulty and you can decide right away whether it's the head or not but on the beacon chain the things like more complicated because the new head can be updated like the block can become a new head like a couple of slots after it's been observed it's been inserted and processed so and that's why replacing this mechanism by just increasing the difficulty won't work.

**Peter Szilagyi**

* And currently on the beacon chain how do we have reorgs and if yes how deep are those reorgs? so i'm not necessarily saying how deep can they be rather naturally while the system is operating what's the practical debt that happened? 

**Vitalik Buterin**

* Has there been even a single rework on main net? like maybe one?

**Danny Ryan**

* There are orphaned blocks from time to time so presumably at least one node the person who produced it is having to reorg out of that block but other than that i don't think we've seen much deeper orgs and maybe we should at least anecdotally no, but we should take a look in terms of the like i can tell you that there's nothing really deeper than one and i don't think that again that's just a kind of a local observation from a single node rather than the whole network.

**Peter Szilagyi** 

okay so the reason i was asking is because at least in case the whole synchronization and block propagation is a lot of ugly complexity is due to handling these reorgs and side forks and whatnots and at least from synchronization perspective things can get a lot simpler if we don't expect rears of course we need to handle it but it's one thing to handle it as a special occasion that happens once a day or once a week and it's other to handle it five times per minute but if it happens only occasionally. 

**???** 37.50

* i just wanted to say that they happen all the time on the test nets especially on the bigger ones so when the validator accounts are high and maybe people are not running on the best machines then there's like multi-block reorgs. the other place where it typically happens is when people are sinking and they think they're already think they're not quite those are two common cases at least.

**Danny Ryan**

* yeah another thing that kind of fits into there is that you have you also have this notion of finality which becomes kind of a natural place to do sort of state cleanups and pruning things whereas i know that's probably now handled as fixed step so that's something to consider is that you would maybe only do those actions upon signal from speaking know that there was finality which in the normal case should be a nicer you know potentially more optimal place to prune but in the extreme might be a worse place but it ends up being a variable place at least not that we've seen any variance in finality on mainnet but you kind of have to be able to plan for it.

**Mikhail Kalinin**

* So the folk choice yeah pretty simple this like second condition second second like approach then you can update the head like if the new block is the child of the current like chain head so this is i guess this is the implementation detail that might be taken or not so yeah the main message here is the new head so okay anything here before we move to the network part anything that probably missed and we want to discuss by the way?

**Peter Szilagyi** 

* just a random question you had you have the two messages new block and new head does new head actually in the current spec or prototypes sending the entire block or only a hash.

**Mikhail Kalinin**

* well it's not yet you know there is no new head in current prototype but it was supposed to send just the hash.

**Danny Ryan**

* new head could be used as signal reorgs on things that it should already have in there so it should only be the hash.

**Mikhail Kalinin**

* yeah so yeah and these two messages are causally dependent so then you block a new head must be processed sequentially as they come to avoid weird case when the new head points to the new block that hasn't been yet persistent 
* and the the like from the sender perspective they will be consistent from the beacon chain perspective because new head won't point to the like the block that hasn't been yet persist 
* okay yeah and yeah also assemble a block it's like to produce the the new block it should point to the already processed block as well so yeah that's also dependency here 
* and yeah network like what's the first change that the block gossip should be turned off on the application side, it should be like deprecated and we are now talking about the like if just imagining that the merge has happened some like some few epochs ago and it's completely like proof of stake mode, we can touch like this corner cases in the transition process later transition process is like complicated yep has a lot of edge cases and yeah so the block gossip just doesn't work yeah that's because the application layer doesn't know about the beacon state about validators and it just can't verify that the block is eligible that seal is correct and so that's handled completely by the beacon chain after the merge 
* so there is the state sync proposal and the block sync proposal this is just a proposal with an idea how could this be implemented so the basic idea behind state sync is that it can use the fast or snap sync or whatever with the underlying network layer that is currently on the mainnet so use the same messages the only like the big change here is that the application layer will know what the current head of the chain is and it will be able to start download the state upon receiving this new block and new head so request like new block will contain the state route the new head will say that this is the head so let's just start download this state with that yeah with this state route. The chain history data which are headers, bodies and receipts it would make sense to wait until the block is gets finalized and it will mean that there is one chain between starting from genesis and ending up with this finalized block so it makes sense to not you know to not to to wait for this event to get rid of the fork management during the sync and just go backward as it is now in the fast sync download headers the whole bodies receipts so for us so and yeah one additional thing here is that there is no need to verify the heat hash anymore because it's proved by the proof of stake consensus of the previous chain and yeah and...

**Danny Ryan**

* Meaning when you're doing when you if you're handling kind of historic blocks prior to the merge that have any hash you don't have to validate it because the chain would be finalized on proof of stake side invested as a chain with a known head and consistency of that chain is all you really need right

**Mikhail Kalinin**

the question is do i understand correctly that the state downloader is just you know bootstrapped with some state routes that is taken from the wire from the observation of the network and then constantly update it with the new state routes as the new block and or new block hash a new block coming from the y is it correct 

**Peter Szilagyi** 

* yes almost correctly it doesn't get updated every time the the chain progresses because that there are about a few thousand modifications in every block so it would it would keep downloading data that will get go stale in 40 seconds so currently what we do is if the route gets older than 128 blocks and that's the threshold for which get maintains the state so if the route is older than 128 blocks then we just jump to a fresh root and this way we we just restart staging every 15 minutes instead of every 15 seconds but essentially yes we are surfing the chain head until the downloader until the block retrieval catches up.

**Mikhail Kalinin**

* so it will make sense to you know and probably jump between finalized checkpoints and then yeah but no we it will need to yeah and and it can process blocks from the last recent finalized checkpoints just to execute them all. 

**Danny Ryan** 

* it sounds like you could you could be told the head consistently throughout that process and guest can just make the decision on locally on on kind of where it's updating where it's pointing this thing.

**Peter Szilagyi** 

* yeah i just wanted to highlight that yes there's actually probably not a good idea to mix in the finalization into it because tracking a few tiny forks on the head of the chain is fine so if i have to download 12 million blocks it doesn't really matter whether the top two or three blocks keep reworking each other that's going to be fairly trivial to maintain or to manage and the finalized block i don't know how how deep is the finalization layer currently how many blocks?

**Danny Ryan**

* 64 blocks. My intuition too was that kind of just signaling new blocks and new head is probably enough to keep consistency with what you're doing today rather than mixing in finality i don't i don't know if there's a big gain there

**Peter Szilagyi** 

* so the thing is that after so even if we mix in finality and i sync up to to the last finalized block and then start executing on top the execution on top will need to do exactly the same s ide fork thingy management so i'm not saving anything but anyway it's it's really a detail having a bit more information and context from the beacon though cannot hurt so it's definitely not a bad thing to know that something was finalized it just might be useless

**Danny Ryan**

* yeah i mean those signals should be spent and then you can figure out what to do with them you have to do with them 

**Mikhail Kalinin**

* okay so the sync is in progress and there is need there is a need to like notify the consensus lawyer that the sync is done so like what i propose is just to you know have like more rich status for each new block message but probably it looks like a crutch here so but that makes sense because if the application node is able to execute a block then it means that this thing is finished so probably it was doing it this way probably it's worth like you know to expo to use the eth sync json rpc method so that's like you know not sufficient detail but just need to know that the consensus is like knows that the application node got synced and is able to produce blocks doing this 

**???** 49.53

* but i think you want something like it's block number or something because it's sinking or some whatever it might be just synced to half of the chain and then that just doesn't have enough peers to know that more chain exists so you better like look at to which like to which block the node was synced to so you so does it could it like basically execute the block or not

**Peter Szilagyi** 

* well once you enter proof of stake mode the beacon chain is telling us the head so we know exactly whether we're in sync or not 

**???**

* yeah but it's also possible that for the first like 12 million blocks we were stuck somewhere and we but we stopped sinking already why 

**Peter Szilagyi** 

* yeah but if the beacon chain told me that i'm if i should be at block 15 million and i know i'm really behind yeah so this issue kind could arise right before the transition so before the first take no takes over the difficulty 

**???**

* yeah because as soon as we have a new head then we definitely can figure out if we synced to this or not yeah okay 

**Peter Szilagyi** 

* yeah but i mean this is probably i mean it's probably a legit issue but only if you are synchronizing exactly during the transition which probably won't take too much time so anyway it's a it's a definitely a corner case that needs to be kept in mind 

**Mikhail Kalinin**

* yep lucas 

**Lucas**?????? 51.55

* so two things we are talking about block numbers here i don't see block number and new block or new heads so will we get that and the second thing is we are blocking the from the network we are blocking the block gossip so when we get a new block to the application layer the application layer now needs to download that block from other application layer parts like from is the payload of the block going in like all the transactions and etc 

**???**

* right so the new block will send the payload it doesn't need to be downloaded from other peers and regarding the number yeah the number the block number will retain so it will be as subsequent as subsequent block numbers of the application blocks as we have them today so it will be sent within this new block message as well so as a part of the application payload

**Lucas**

* thanks 

**Mikhail Kalinin**

* okay any any questions regarding this state scene or any concerns

**???** 

* yeah just a tiny addition that i think that's what we said about the new block it's true when we already caught up to to the head but we're we initially thinking i guess we still need to just it won't be gossiped but we still need to like proactively download it from the blocks from the other peers from the application layer right if we just got a new head and we have like zero state then it's it's up to us too 

**Peter Szilagyi** 

* yeah so the block symbolization method would stay the same it's just the block broadcast or the block announcement that would get nuked out 

**???** 

* okay okay so def p2p will just so we'll not use a new head and new block 

**Peter Szilagyi** 

* yeah notifications anymore okay 

**Mikhail Kalinin**

* yep and to give like the whole perspective once the client this new client this new like combined client starts up with like a fresh state so well with the empty state and the empty chain what will happen the first step is for consensus layer to catch up the head of the beacon chain and then once it's caught up then it will be communicated down to the application layer signaling that it can start that it may start to download the state or whatever or download blocks 

**Micah Zoltu**

* can the consensus layer follow consensus head and with a sense of authority without the application layer being fully synced yet or at all?

**Vitalik Buterin** 

* i think so. in the long run there's the nuance that the the the thing in the consensus layer that's dependent on application act layer activity is deposits which like right after the merge that's not an issue because deposits are just like computer or because Eth 1 data voting is an honest majority thing but eventually we would want to get rid of that mechanism and so i guess like the validation might have to be redone a bit like first you would sync the consensus chain and if and if the application chain isn't verified yet then you would just like take the deposit the deposit routes on the trust and then and remember them and then later on when you get the application chain you would check that everything matches up 

**Danny Ryan** 

* there's also a difference between following the head and necessarily being able to participate in the head so like you wouldn't be able to build blocks with an application layer payload and and there's also there's certainly grades of being able to follow the head like you can there's a light claim protocol right they're just following the beacon chain there's doing full validity checks there's you know 

**Vitalik Buterin** 

* there's a lot of things right but the default algorithm for our clients following the consensus chain is going to be that like as part of the process of verifying a consensus block they'll pass the corresponding application block along to the application clients and check if it's correct 

**Danny Ryan**

* right so it's like if you just followed the proof of work chain and you knew that the proof of work was the biggest total difficulty but you never checked consistency of execution you can certainly be tricked

**Micah Zoltu**

* could someone running a consensus client who didn't want to or couldn't for whatever reason run an application client could they produce empty blocks if their turn came up? like you actually need a full application client to produce a block or you just need something that can give you a thing that's shaped like a block?

**Peter Szilagyi** 

* well if there are no transactions then the state route remains the same so you just you just take the last new block you got and then you just feed it back to or maybe just change the coin base and feed it back to the consensus client

**Micah Zoltu**

* is that valid like would that work?

**Peter Szilagyi** 

* based on the current spec yes it seems to me 

**???** 57.35

* yeah you wouldn't actually be able to kind of validate that you are actually even on the right chain right so basically you could build on top of one block and just hope there would be a valid one but you you wouldn't would have no way of knowing 

**Peter Szilagyi** 

* well if you trust the easter client that this was the head block then i mean yeah sure you didn't validate it but if in general there aren't attacker blocks in the network then it's a good heuristic 

**Micah Zoltu** 

* it's not a bad strategy it's either that or nothing and you at least get your reward if you produce something 

**???**

* it's a bad strategy in terms of verifying the block if you're attesting to a block with that 

**Micah Zoltu**

* i don't know if this is healthy or not 

**Peter Szilagyi** 

* by the way just to go back to the previous note previous question i think the question was whether the the beacon chain or the consensus chain needs to be able to sync without the application layer and i think that would be a hard yes i mean you can debate the trust model but the thing is that the expectation is that the state try will only be available for the head few blocks maybe head 64 or 128 blocks this means that in order for the application chain to synchronize the state it must have the root hash a recent root hash so the consensus chain the consensus client needs to be able to provide a recent. 

**Danny Ryan**

* and ultimately rely on the application layer to get to the head and know that things were consistently processed rather than kind of knowing it in real time passing things in there during sync

**Peter Szilagyi**

* so i guess it's the security model would be similar to fast sync essentially just to download not the latest head or not the latest state but some recent issue state and then just execute a whole bunch of blocks on top and make sure that nothing goes wrong 

**???**

* right yeah yep at the end of the state sync it's as it is now it executes some block on top of the most recent state rate to catch up with that 

**Peter Szilagyi**  

* well it doesn't execute it to catch up with the head because it could download it could end up exactly on the head it's just rather a security mechanism that in order for you to defeat somebody a bad chain or bad state you would also need to mine 64 blocks on top and that's the instance

## Block sync proposal

**Mikhail Kalinin**

* okay yeah so block sync proposal the idea is pretty much the same so the once the head is known the application where i may download headers backward backwards in reversed order and then execute that application... it could be hybrid strategy when the application now starts up and starts sinking blocks from the first block and at the same time the consensus layer catch up with the head communicate this hat to the application layer and the sinking forward and downloading the headers in reversed order then this chain these two like downloading processes converge at some point and then goes forward so it's also like an option here 

**Peter Szilagyi**  

* yeah you don't want to do that it's way too complicated i mean it's right to go horribly wrong and then you would need to check the proof of work and if you run out of proof of works then you cannot verify anything and the other thing is that if currently the proof of work chain is kept alive because everybody is keeping mining proof of works on top but once once the head is directed by proof of stake essentially i can mine an alternative reality for ethereum that is heavier than the original ethereum 

**???** 1.02.42 

* so you don't have a very high profile stay a proof of work because you're going downwards and you always have information about the parent hash so when you when you receive the hat from the proof of stake chain then you have information about the parent house you're always verifying the parent hashes and at some point you reach genesis which means that you are sure that you reach the same genesis as you would be in the normal chain it's actually how we currently synchronize nethermind so so it's exactly the same behavior as you have currently 

**Peter Szilagyi**  

* yeah of course i was just saying that you if you start from the head then you cannot also start from genesis and meet in the middle 

**Danny Ryan** 

yeah agreed on that

**????**

oh sorry yeah sorry no

**Peter Szilagyi** 

so starting from head and down the header chain and then filling it that's completely valid that's 

**????**

sorry i didn't hear that part

**???**

okay so by the way how much time does it take to download the chain of headers for the current main net?

**???**

15 minutes it's about three gigs no okay so actually for 5.5 gigabytes currently 

**???**

yeah so 15 minutes doesn't sound that bad because this block sync is like desirable for and useful for running the archive node so the entire sync process after it's bootstrapped with headers will take much more time 

**???**

i mean it's it's the mechanism is very similar to turbo geth and it's header and block body downloads is this it's the minority of time so it's i don't think it's a problem

**Mikhail Kalinin**

okay cool 

okay any questions for the network what's probably missed here anything that comes to your mind 

**???**

* so i have a question about do we consider here any adjustments to where the bodies are stored like did you consider discussing that also with this idea that comes from piper steam at trinity on the dht around block bodies because block bodies are quite heavy so they take like i believe 150 gigs nowadays and they take a bit longer to download so do you consider everything 

**Danny Ryan**

* yeah the nice thing about this proposal is that it doesn't it's not opinionated about what happens kind of on how the application layer gets synced and so by default we reuse things as is but that can those promises can be broken you know where things are stored can be changed protocols can be changed but for the purposes of getting this merge kind of in place and basically expected that this does work whereas similarly in the future if you if you move bodies to dht and you had a different way of retrieving them and like the the current protocols were the promise that they were there was broken you can still get kind of set head from from beacon chain and choose how to go retrieve that information so they're definitely decoupled in a nice way but we still should be pushing on and considering how to make that sustainable in its own right

**???**

* makes perfect sense thank you

## Transition Process

**Mikhail Kalinin**

* okay anything else before we move to transition process?
* okay so the transition process the like the complexity of this process comes with the requirement for the software to like be able to operate in these three modes so the software like the client will be you know updated like with some some decent amount of time before the merge before the like potential point of the match and then it will have to operate in the proof-of-work mode for unless the transition conditions are met then transition mode comes where the like the transition mode means that the total difficulty rule is replaced by the external fortress rule by the fortress rule that is driven by by the beacon chain but blocks are still gossiped on the on the application network and once these first first block that is proposed by the proof-of-stake proposer gets finalized then the software turns into proof-of-stake mode which is after the merge mode or the app and operates in that normally so that's the complexity of the process.

**Peter Szilagyi** 

* I have one question here what happens in the in the case of consensus issue between major ethereum one clients 

**???** 

* what do you mean by consensus issue? you mean like there is a consensus break right so one chain is yeah i see so that's interesting the it depends on how big chunk of you know it depends on how big chunk of notes on like the main net went out of consensus so if it 

**Peter Szilagyi** 

* will be like ethereum two nodes that are listening to minority theorem one client will be slashed or 

**???** 

* they won't be slashed they will be our fans so their blocks will be offend by the folk choice rule of the beacon chain yeah 

**Danny Ryan** 

* so they would be penalized slowly you know they would stand to lose about as they stand to make so like if they were on that orphan chain for a year they would you know lose eight nine percent of their their stake and yeah it's similar to what would happen today you know if 75 of the miners were on client a and 25 percent are on client a and client b disagreed then you know the chain weight of client a would be much greater than the chain rate of client b once things kind of resolved but it ultimately becomes like a what is correct and which which version of software do people need a fork and go in that direction 
* but in terms of proof of stake if you had greater than two thirds on one of them there would be like a finality signal happening so that's something to consider so like two epochs after this chain break things would likely finalize which would be a much stronger signal than say just a proportion but even then it's definitely a catastrophic scenario for depending on how much of the network is on that and should be avoided similar today 

**???** 

* thanks 

**Mikhail Kalinin**

* okay so the transition process like on the consensus layer looks like as follows so there is the total difficulty is a certain value for the total difficulty and once it's reached by the mainnet the beacon chain will like track all the blocks from the main net so it will already be a combined client with the beacon chain and the with beacon node and the application node which the application node is still operating on the proof of work conditions and once detailed difficulty met the consensus layer we'll take this block this last proof of work block and build a block the first proof of stake block on top of this one and yep communicate this to the application layer so it will send this block in a new block message and then in the new head will be sent accordingly so and once the application now receives these message messages it turns to the external factors rule and starts following these messages from the consensus layer there will be also a sample block for some cases when you will have to produce a block so so it's eligible for the report mode as well and then after some time the finalized block for the first finalized block message is called and then the application node understand that this is the time to turn off the block gossip and turn to the proof of stake mode so that's how it look like from the chain progress perspective. 

**???** 

* yeah just a question so basically if you're in proof of work mode then if you've been choosing as a blog blog proposer on the beacon chain then youwill receive assemble block if you've been choosing as a block validator then you will receive a new block and the rest will receive a new head right when the first block is being proposed 

**Mikhail Kalinin**

* right right and when you send this new block to the application node and the application doesn't have like the that doesn't know the parent of this block it will have to download its parent and its ancestors you have to verify it so otherwise the tester will not be able to attest to this block unless it's fully executed this is important yeah peter 

**Peter Szilagyi** 

* two questions one of them you mentioned that while we are in proof of work mode the beacon chain will follow the eth1 chain to figure out when it wants to transition but how exactly will the beacon chain follow the crucial function? 

**Mikhail Kalinin** 

* yeah that's a good question right like it get blocked by hash currently contains total difficulty right it returns total difficulty double difficulty 

**Vitalik Buterin** 

* when i checked the rpc interface they could see it or the doc said that it returns total diff yeah but if it doesn't we can always add it so it's not yeah 

**Mikhail Kalinin** 

* there will have to be an rpc endpoint that will contain this total difficulty the block hash like the head you know this information yeah for the block and also it will need to be it it will have to contain the flag where whether this block is valid or not so it also like required the 

**Vitalik Buterin** 

* the beacon node already like asks the application node for like the head because it has to do i do eth1 data voting right right

**Danny Ryan** 

* yeah i mean there's they all have are able to communicate to each one notes today on some limited interface about state and head 

**Mikhail Kalinin** 

* probably it would make sense to since these rpc methods if they will be implemented as json rpc will sit on the separate port for security reasons it probably will make sense to implement one more rpc method that will aid this process 

**Peter Szilagyi**

* okay another question here you have between the proof of work mode and the proof of stake mode you have this transition mode and isn't it this i mean i don't really understand why we need this middle ground i mean obviously we didn't finalize a block yet but why does that matter ?

**Mikhail Kalinin** 

* we want block gossip to keep working on the application layer until the we get the first finalized block 

**Peter Szilagyi**

* so if you expect so if the eth1 client is expected to receive new block a new head then how i mean i propagate a block what i don't know whether it's relevant or not i don't know how to choose the fork i mean what do 

**Vitalik Buterin**

* i guess the the idea is that like while the transition is not finalized there is still the possibility of the beacon chain reorg-ing to a different beacon chain that has a new first embedded block and to check that different first embedded blog like that first embedded blog would have a proof of work parent and that proof of work parents like could potentially be well would be mined and it could potentially be mined at some point later and so you still need the ability to keep broadcasting them but after the trans the first embedded block is finalized then like there's nothing that can possibly happen on the proof of work site that's relevant to the validity of any beacon block and so you can stop broadcasting PoW blocks 

**Peter Szilagyi**

* okay but then the important detail here is that i'm only broadcasting the proof of work part of the blocks so if i have three new proof of work blocks and 100 new proof of stake blocks and i will only broadcast three proof of work once right 

**Vitalik Buterin**

* correct i don't think there is any reason to broadcast proof of stake blocks over using the application clients 

**Danny Ryan**

* you could even probably not you could even restrict proof of work block gossip such that you only broadcast blocks that are past the total difficulty of one by one block and no further children on such chains because the only valid blocks to include on the proof of stake side would be like that first child passed the total difficulty or depending on how if you're doing greater than or equal to just right at that threshold 

**Peter Szilagyi**

* okay does that make sense 

**Mikhail Kalinin** 

* okay cool Peter anything else here 

**Peter Szilagyi**

* just a quick question in proof of work mode you have the assemble block and when i call the assemble block that means that i'm switching over to proof-of-stake i don't need a valid proof-of-work mine on that one anymore so i just need the transactions executed and that's it? 

**Mikhail Kalinin** 

* yeah right so yeah so this is just give me a block on top of this one 

**Peter Szilagyi**

* okay and in this case the block hash, i mean the oh wait so okay never mind 

**Mikhail Kalinin** 

* actually assembling a block will happen on top of the current head so the current proof of work had this is likely to happen so the first proposer of the proof-of-stake block with embedded application payload will get its head of the proof of work chain proof of work chain and asked to assemble a block on top of it yeah and it might not be the head for the rest of the network but until this block is valid until this proof-of-work block this last work block is valid and mets meets the transition conditions then everybody is okay with that so it's valid okay cool okay anything else for the transition part and we'll yeah by the way one thing here is that the transition is that clients with the transition mode will exist sometime after the merge happened so if you started this client it will need to be designed in a way that it can handle everything correctly so the merge happened but it doesn't know about it yet so it will need to take this information from the network but i don't see any big issues with that but yeah definitely worth to think that through and what and after some time you know some after some time of the merge i guess the clients will just throw away this transition process from the code base and yeah just 

**Peter Szilagyi**

* Mikhail that's a interesting question so essentially when i start up an ethon client i need to know whether i'm in proof of what i should start syncing the network using proof-of-work mode or whether i should wait for the beacon chain to give me something 

**Mikhail Kalinin** 

* yeah so that's i guess it could be an implementation detail so you may have this flag right if you know that the merge has happened but if you if you don't know for some reason you you can start operating the proof of work mode and then once the some message comes from the proof-of-stake like new block and you had you can like you know readjust your mode yeah node can the client can readjust its mode 

**Peter Szilagyi**

* yeah it's going to be a bit messy for example if i start up a fresh client combo so neither eth1 client or eth2 client are synced at all i don't know how much time it takes for the eth2 client to sync up but up until that point the eth1 client will do weird things i mean i will start downloading the state route for something that might be completely invalid because maybe some miner remained on the original chain and didn't fork off and then they are just advertising some weird states that i will actually sink to or try to sync to up until the point where the proof of stake node says that hey hey stop much already happened 

**Mikhail Kalinin** 

* yeah and you can like add the block hash for the first proof of stake block you know so just to er the same way they dial hard fork block has been handled on the network if it helps but it it requires some intervention you know so this is the same to say that the merge has happened you know it requires some intervention from the user 

**Peter Szilagyi**

* yeah so i guess it would be advisable to well for one thing to have some form of flag or somehow to control this employer thing to for client that's eth1 client has to maybe do a release after the merge a quick release to just flip the switch yeah okay 

**???**

* yeah i mean if it's still required to sync that all the old like proof of work chain then i think it makes sense after the merge to make a kind of release that's kind of hard codes the block and maybe the root hash of the last proof of work block and just start syncing to this block immediately because why not even though proof of stake might not be synced yet because you will know after the merge actually happens 

**Peter Szilagyi**

* now you cannot really sync to the to that specific state because it will be pruned from the network so it's the i guess the only important thing is to know whether the merge happened or not so that we know whether we should wait another

[Garbled]


**Mikhail Kalinin** 

* okay micah

**Micah Zoltu**

* so would it be reasonable to assume that given the most pathological situation where miners are running some custom code towards the end that we should expect to see many many peers of the last block so we will just see like assuming miners are running like no client that was going to code this but as we miners all write their own code the rational thing for them to do would be to just repeatedly mine that last block over and over and over again right?

**Peter Szilagyi**

* you mean to not to avoid meeting these transition conditions right?

**Micah Zoltu**

* not to avoid mean condition just to increase your chances that your block is picked as the last block is like your last chance to make money and there's no reason you've got hardware it's running you might as well just keep mining that remining that head

**Peter Szilagyi**

* there is i don't think there is a reason not to do that for miners but that's okay for the transition process because yeah the proposer will pick what whatever the heck it observes it's the moment i think i mean that's basically the best 

**???**

* like that we wanted to find that block that's nice no that's best that's good who cares 

**Danny Ryan**

* it's also not very incentivized because once the beacon chain picks a block to build on and there's at the stations it quickly becomes very difficult to reorg that the beacon chain the the miner can't do anything to reor you can change that point to try to get their new head around that point picked in unless the miner is there 

**Mikhail Kalinin** 

* yeah okay  we have like one more minute left any significant questions so far or or we can continue offline 
* okay cool like my last question what do you think are the reasonable next steps towards the eaps to sp towards specific specifying this all for the application layer 
* do we want to discuss it more like go round and round through details or yep does it make sense to work on the spec

**Peter Szilagyi**

* so i personally for me this is fairly clear i mean the exact format of these assemble block new block rpc methods they don't really matter so whoever writes up an initial spec i think we can run with it i think there's already an initial implementation in catalyst so i don't think if there's a need to detail it too much one thing that's a bit murky for me and maybe that would be nice to to investigate is what happens swith the difficulty and okay you might say that this is a client implementation on how the clients handle canonical chains that are not the most difficult ones but i think that might be an interesting thing to discuss a bit 

**Mikhail Kalinin** 

* you mean how to replace this fork choice? 

**Peter Szilagyi**

* no i mean client implementation wise how to make sure that so currently the clients have it hard coded so to say that the canonical changes is chosen based on difficulty and it might be worthwhile to investigate just how deeply this choice is who is rooted in the clients 

**Danny Ryan**

* does clique do a a simulation of that or is clique independent of disability sorry the clique consensus mechanism does it simulate some sort of total difficulty or is it totally independent of the word? so i'm implying if we have clique that's not proof of work so i assume that it's maybe not too deep but you would can you help me understand 

**Peter Szilagyi**

* now so the total difficulty is independent of proof of work so click also uses total difficulty for the fork choice

**Danny Ryan**

* okay interesting 

**Peter Szilagyi**

* yeah so in click essentially what happens is that you have a batch of signers that can sign but every time one is in turn and everybody else is out of turn and then if you sign when you're supposed to sign then your block has a difficulty of two otherwise one and this ensures that there's always one block that is heavier than the rest 

**Danny Ryan**

* interesting i didn't i didn't realize that so it might be deeper than my expectation i just kind of thought that eth1 clients can handle generic engines there 

**Vitalik Buterin**

* i'm guessing eth1 clients do have a some kind of lower level set head method right that just like sets the head to whatever you want and does a reorg 

**Peter Szilagyi**

* yes that just happened there are a few problems with it at least for example in geth if you do a set head then that kind of deletes everything afterwards so you cannot just jump between chains with the set head because it nukes things that's what's supposed to be the rewind method and the other thing is that for example what geth does when you get the side block is that it doesn't import it it just stores it in the database as a flat thing it doesn't execute anything and it only starts executing the size chain once the total difficulty exceeds the canonical one and then we have this implicit thing behavior that we need to hack out somehow i'm not saying it's hard or not possible i haven't thought about it but it's a non-obvious question 

**Danny Ryan**

* sorry you said that head can nuke things i didn't understand what you meant it can nuke ?

**Peter Szilagyi** 

* no for so for us i think italic mentioned that there's a method called sat head in geth but that sat head is meant to rewind the chain it's not meant to jump between branches 

**Danny Ryan**

* got it okay so you would go to a common ancestor if you were jumping between branches then you would set head to the head of the branch after that 

**Peter Szilagyi** 

* yeah but i cannot do that so stafford is just okay you can rename it rewind you can only go backwards you cannot go forward 

**Mikhail Kalinin** 

* okay yeah so cool let's just i think we should rip up and continue flying this is a good comment this is like good come and i think that exercise was difficulty probably it will be a good task for the hackathon trying to do some something with any of the clients also there is like a question or proposal like to yeah virtual for total difficulty value transition d plus slot number it's not gonna work because the in the beacon chain the block is not self-sufficient in terms of fork choice because it's a test later and could better sit later and at the station could be included on chain like one slot after and it can it affects the item it has an impact on the folk choice so virtual total difficulty will not work in this case okay so with anything else before we wrap up 

**Danny Ryan**

* fantastic document mikhael this is awesome 

**Mikhail Kalinin** 

* thanks everybody for this great discussion yep i'm happy that we go went through all these documents and even happy that we didn't cover other aspects of the agenda well it can be due later on the subsequent call so this call is bi-weekly so anybody who wants to have an invitation let me know just dm your email address so see you tomorrow on the ACD call. 

**Danny Ryan**

* it's now on this shared calendar for these types of calls i don't know who maintains it.

**Tim Beiko**

* Yes i added it. There's a protocols call google calendar which lists all of the different eth1 eth2 and now merge calls. I'll put the link in the chat right here if anybody wants to subscribe to it and these calls are included there.

**Pooja Ranjan**

* And the cat herders will be documenting the notes for the call so maybe it will be available and will be posted here in the github repository. 

**Mikhail Kalinin** 

* great well thanks everyone thanks everyone for joining see you guys.

-------------------------------------------
## Attendees
- Mikhail Kalinin
- Protolamda
- Vitalik Buterin
- Danny Ryan
- Dmitry Shmatko
- Micah Zoltu
- Peter Szilagyi (GETH)
- Tim Beiko
- Pooja Ranjan

---------------------------------------
## Next Meeting
April 15th, 2021 @ 1400 UTC






