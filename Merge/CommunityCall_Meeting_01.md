# Merge Community Call 1

### Meeting Date/Time: Friday, Nov 5 14:00 UTC
### Meeting Duration: 1 hour
### [Agenda](https://github.com/ethereum/pm/issues/402)
### [Video of the meeting](https://www.youtube.com/watch?v=_kfS9jAUY6g)
### Moderator: Trent
### Notes: Stefan Wüst

-----------------------------
# Summary
* Validator rewards that are occurring to addresses on the consensus layer will not be transferable just after the merge but at some later point. It will just be the transaction fees so far.
* Transaction fees also include MEV which might outstrip all the other forms of validator rewards and payments. It could be significant.
* There is no Timeline yet for when the validator rewards on the consensus layer will be unlocked but beacon chain withdrawals will be the highest priority after the merge.
* We're trying to adapt different naming schemes. eth2 sent some different messages to people. Execution layer and consensus are the terms that we're trying to shift towards.
* We have a devnet called pitos. Join it only if you want to be at the very forefront it's still quite experimental. I'll be quite manual onboarding to it.
* public long-standing devnet planned before the holidays.
* After that we are going to run the merge on several of the existing test nets (robsten, Rinkeby, etc.) The order and timing is not determined yet. High chance robson would be first
* Fee recipient is a new word that we've use. it's basically the same as a coinbase. the field itself will be on the execution block not the consensus block
* incentive to produce the block becomes even stronger after the merge because they actually get the transaction fees but if a validator is offline when it's their turn to produce a block then that blocks gets in.
* We're currently working on running full test nets without finalizing the sync mechanism. We have a prototype for pitfalls but still work to do in order to get it merged into the clients.
* Explanations about difficulty and randomness regarding [EIP-4399](https://eips.ethereum.org/EIPS/eip-4399)
* the block Time right now is on average 13 seconds but at the merge it'll go to 12 seconds -> we should absolutely reach out to DeFi in general about this
* Explanations on finalized head vs unsafe head and their time difference
* if you are releasing real assets you might decide how many blocks to wait based on what you see in the network or you're relying on the finalized head if you need ultra finality and absolute security
* Explanations about Kintsugi (next iteration of Dev nets)
* Explanations about client sync between proof of work and beacon chain
* There's no migration progress required you're not going to have to redeploy your contracts, ethereum state addresses, user balances contract code, any sort of information, that tells us what happened in the past, about ethereum and and what's going to happen in the future. That state continues throughout.
* No merge related calls with miners directly so far but consistent messaging going into the minor communities trying to make sure that they're aware that this is is imminent
* Explanations about terminal total difficulty in the transition from the proof-of-work to proof-of-stake. Explanations to avoid minority fork attack.

-----------------------------
# Intro

**Trent**

* So this call is the first merge call that we're running Tim and I. It's not the only one Pooja has run some related to this as well you should definitely check out those videos but this is the first one that we're running. We're going to go over what the merge is what it's not and some quick updates on the state of things and hopefully answer any questions that people have about things we are recording. Tim do you want to start with anything?

# Summary on the state of things

**Tim**

* Sure I guess there's a lot of new faces on this call so maybe it's worth just taking five or so minutes to walk through what the merge actually implies from an ethereum node perspective. Then I have a couple just things that I think people should be aware of at the application and infrastructure level and then I think we can take most of the call to just answer people's questions or chat about it.
Also one thing that would be helpful is knowing if people have questions - even though we can't answer them on this call, we can schedule calls in the future. We're still I wouldn't say early in the merge progress but we're still at the spot where we have enough Time to have dedicated calls about specific topics over the next couple of months.

**Trent**

* Cool! So I guess I'll just share my screen and I'll post the link to what I'm sharing in the chat here but at a high level. I tried to summarize what the merge actually is in the post I showed in the chat. A lot of this is is based on diagrams and work that Danny Ryan had put together a very high level.

* The way to think about an ethereum node after the merge is is this diagram that I'm sharing right now where you're have to run both a beacon node and what we call an execution node which is the equivalent of an eth1 client today. And basically what the merge is it's just taking the current eth1 clients and instead of having them follow proof of work or proof of authority for their consensus and to find out the chain head we have them follow the beacon chain so you have your whole ethereum client which is the sum of your beacon node which will maintain its peer-to-peer connections it does right now so the whole peer-to-peer network where at the stations and blocks are shared will remain part of the beacon node.
Similarly all the beacon APIs that already exist will remain part of those beacon nodes and you can query your node directly for that. Then the execution engine is a modification to eth1 clients but those will be made available by the different teams so you'll be able to download the aragon version of this and this is basically an eth1 client which strips down everything related to consensus so it just relies on the beacon node for consensus but it'll still be in charge of block execution validating that transactions are are valid and maintaining its own transaction pool as well as gossiping the transactions.
So this is why you also keep the same peer-to-peer layer where the main difference is you are not broadcasting blocks anymore on the the execution peer-to-peer layer but the the transaction propagation still happens there and similarly all of the Json RPC APIs will still be present.
And then in order to facilitate communication between the beacon node and the execution engine we've introduced a new API called the engine API and this is basically the API by which the beacon node will share a new head a new finalized block with the execution engine and will also query the execution engine when it's the validator's time to produce a block for a valid block that you can share with the network.

* And at a high level that's really it. The way we transition at the merge basically is using a total difficulty value on the ethereum maintenance and there's a couple security reasons for that but at a high level it's just the safest way to go about it so what will happen is that we're going to have an update an upgrade on the beacon chain where we'll add a terminal total difficulty value so the final difficulty that we want to see on the proof of work chain the the beacon chain will be querying the proof of work chain every block asking it did you reach this this total difficulty no did you reach just sold difficulty no and at some point it will so whichever block basically has a total difficulty larger equal than this terminal value will be the final block on the proof of work chain and from that point on the eth1 clients will begin following the beacon chain for consensus rather than than proof of work. And one thing to note is obviously there can be multiple blocks that come at that Time with a similar total difficulty and then we rely on the beacon chain consensus to decide the canonical blocks between say there were two competing blocks that were that were shared at the same Time. And so after the merge what the beacon chain will look or or what blocks sorry will look it's this where on the other layer you have the what's a beacon chain block today which contains things the the current slot, signature randall, all the at the stations, the deposits, the validator exits and within those we'll basically add what we call an execution payload which is the equivalent of an eth1 block today. And this is produced by the execution layer so this execution payload is what gets passed around between the validator layer and the execution layer and these contain exactly what you'd see in an eth1 block today so the hash, the state routes at the list of all the transactions and again when you receive a block on the network it'll go to your your consensus layer and you'll pass it to the execution layer to actually execute the block make sure that it's valid and similarly when you need to produce a block for the network you'll just query it from your execution layer and then propagate it on your on the consensus layer.

* I mentioned earlier there's this engine API that we're working on which is the communication interface we're still finalizing it but at a high level there's three APIs that are going to be added one is called this engine execute payload which is the consensus layer sending a block to the execution layer to just validate it. Execution layer returns whether it's valid or invalid if it's still syncing just return syncing and ask for it to be sent later.
The biggest addition is this for choice updated call which the consensus layer uses to tell the execution layer that there's a new head and then you finalize block on the network and optionally it can also pass it what we call a payload attribute which is asking the execution layer to start producing a block and giving you things the Timestamp the randall value and the fee recipient or the coinbase value that's required and this is how basically if the execution layer gets a call from fork choice updated which contains this payload attribute shield it knows it needs to start producing a block and then there's a final call called engine get payload which asks the execution layer to return its current best block so those come after you've asked it to produce a block and then you just ask it to send one back. And also really ideally the three only endpoints we're going to add as I said it's still being discussed but we we really want to try and keep this communication channel simple.
Just worth noting not much changes on the execution layer so there's an EIP that describes all the chain [EIP-3675](https://eips.ethereum.org/EIPS/eip-3675) but basically the block itself won't change the only thing is any field that's related the proof of work or to uncles gets set to zero (or: the data structure is equivalent to zero) just because we don't need those anymore yeah and obviously once the merge happens there's no more block rewards so that stops but it's worth noting that transaction fees still get processed by the execution engine and one thing that's not really obvious is that transaction fees can be sent to an eth1 address so they don't accrue to the validator addresses but they'll accrue to addresses in the execution layer.
And then here's again a diagram by Danny that shows how the merge happens so at the left side of it you have the proof of work chain as it is today so you have proof of work, within proof of work we have our execution layer engines that produce eth1 blocks and we have a chain of those. Similarly on the beacon chain we have blocks that are empty they contain beacon chain data but they don't contain any executable transactions and then around the merge we're basically just dropping proof of work and this this part that contains the what gets executed in a block becomes the execution payload in in the post merge system and we just remove proof of work and beacon chain is now our source of consensus.
Both the consensus and execution layer maintain a peer-to-peer network they maintain their current user APIs and the big thing that we're still working on is sync so sync obviously needs both parts to interact with each other and there's a couple prototypes for different syncing mechanism but there's not one that's been fully deployed yet

* I'll pause here it feels I went on for a while. Does anyone have questions or thoughts ?

**Speaker 3**

* Hi Tim. I put a question about whether or not validator rewards that are occurring to addresses on the consensus layer if they're going to be transferable after the merge?

**Tim**

* Not in the emerging hard fork at some point after that.

**Speaker 3**

* So it will just be the transaction fees that validators can actually move to an exchange or do anything with?

**Tim**

* Yes yes

**Speaker 3**

* And is there an estimated Timeline for when the validator rewards on the consensus layer will be unlocked?

**Tim**

* It's the main priority after the merge but just not comfortable giving a date given that we haven't done the merge. But after the merge basically the most the highest priority thing is beacon chain withdrawals basically

**Speaker3**

* Gotcha. OK, thank you

**Speaker 4**

* And just for some small additional contacts related to your question: People, when we say transaction fees that also includes MEV type stuff which there's a good chance if current history predicts the future the MEV stuff might actually outstrip all the other forms of validator rewards and payments so don't assume that just because it's transaction fees only that it's going to be some tiny little amount that it could be significant.

**Speaker 3**

* Definitely, thanks!

**Tim**

* So there's a question: What do you mean by MEV? Basically: Yes it's still a transaction fee, yes.

**Speaker 4**

* It not only comes in foreign transaction fees sometimes direct payments to what was previously called coinbase which will now be the fee recipient. So you'll get a transaction that will show up in a block that you as a validator produce and the transaction will just directly send money to the block producer and so if the block producer puts in some ethereum address as their address they want to receive fees at, that MEV payment will also go there.

**Tim**

* Yes

**Speaker 4**

* It's an execution later

**Speaker 5**

* I'll just jump in and say really quick one of the things that we're trying to adapt to is different naming schemes. Many of you are probably familiar with that the merge used to be called or this big project used to be called eth2 but that sent some different messages to people about sequentiality and how product's working so you've probably heard Tim say a few Times execution layer and consensus and these are the terms that we're trying to shift towards as they are more accurate and they don't have to deal with numbers because in reality ethereum is going to exist there won't be separate editions of it. One is going to die and one is going to take its place.
I'll share a graphic later but Tim if you want to keep going yeah and Micah would be angry that's correct.

**Tim**

* Any other questions?

**Speaker 6**

* Yeah this has been super helpful thanks for sending us together.
I'm curious so I for my understanding there's an existing test net which everyone is testing this on. Will the merge happen in other test nets also?

**Tim**

* Yes so that was going to be my next thing but at a high level we have a devnet right now which is called pitos I would recommend joining it only if you want to be at the very forefront it's still quite experimental. The best way to join it on the ethstaker discord there's a pitos channel so it'll be quite manual onboarding to it. Right now throughout november we're working on a second iteration of devnets and the goal is to get a public long-standing one before the holidays so that people end with readmes and actual instructions for people to join so that'll be a new network and hopefully you should have the final spec so if if you want to see see it first that'll be the place to go. And then we are going to run the merge on several of the existing test nets robsten Rinkeby and whatnot. The order and timing is still not determined. There's a high chance robson would be first because robson has a difficulty bomb on it which might go off sometime in january, so if that happens, then it might just make sense to run the merge on robson first. But yeah, before we do that we want to have just new devnets that are up and that we know are working well.

**Speaker 6**

* Why don't you finish your first talk?
sorry I thought you were going to keep going with questions but if you just wanted to wrap up that first thing you were going through

**Tim**

* Greg has another question: Fee recipient is a new word that we've used but it maps the coin base basically just to make it clearer because it's not mining but it's basically the same as a coinbase.

**Speaker 7**

* But the field itself will be on the execution block not the consensus block or because there's a slot I should say.

**Speaker 8**

* Tim can you clarify if the from that diagram that you showed that block propagation will be by the beacon chain and so that all sort of pre-consensus no pending blocks moving around that's going to continue on the pdp layer of the execution engine but the only way that the execution engine knows about blocks is through that engine API

**Tim**

* Exactly yeah and basically what happens is that once once we hit a block with a terminal total difficulty and you stop propagating blocks that have not hit that and then once you've had a finalized block on the beacon chain after that the execution layer just stops propagating blocks altogether.

* Okay so Ben has a question will every beacon chain block have an execution layer block in it?
So no basically so you can still have somebody missed or missed their validator slot. Today if your validator is offline when it needs to propose a block, that block will be missed and we've been looking at the impact of that on [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559). How do we want to treat missed slots with regards to the base fee and the block capacity so there might be some changes that we make alongside the merge to just take into account potential missed slots when you're calculating the the base fee. So we expect validators have an incentive to produce the block and it becomes even stronger after the merge because they actually get the transaction fees but if a validator is offline when it's their turn to produce a block then that blocks gets in.

* And then there's a good question also: How do we plan to run full test nets without finalizing the sync mechanism so we have a couple prototypes of the sync mechanism I'm not super familiar with them I don't know. I see Marius is on the call - Marius if you've been following the the latest sync?

**Marius**

* Yeah so we're currently working on that. We have a prototype for pitfalls but there's still some stuff to do to get it merged into the clients.

**Tim**

* These are really good questions.

**Mikhail Kalinin**

* Basically I just wanted to add that the execution layer will receive all the information required for to bootstrap the sync mechanism and keep it progressing from the consensus layer which is the execution execute payload commands with the payloads and the public choice updated stuff that points to the head to the current head of the chain through observation of contest layer. And another thing to mention here is that consensus layer can reach out to the head of the chain a optimistic way and then the execution layer can use this information about the current head and about the current state of the network to sync up and pull the state and become able to become capable of executing payloads. That's the the strategy that is currently prototyped and evaluate in this being evaluated in the testnets.

# EIP-4399

**Tim**

* I guess Mikhail since you were speaking the next thing I was going to cover is that your new [EIP-4399](https://eips.ethereum.org/EIPS/eip-4399) but do you want to take a few minutes to walk through that and also basically not a lot changes for smart contract layer and anybody using the the execution layer data but that's one of the changes do you want to maybe walk through that and and any other changes that people writing smart contracts are just depending on the execution layer should be aware of?

**Mikhail Kalinin**

* Oh yeah sure. So this EIP is the basically, what it does it just lands the existing difficulty of code. It actually supplies the existing difficulty of code with the new random of code the key okay there are several things here. First of all the number of the instruction is not changed so it's just basically the renaming of the difficulty to random and the change in the semantics a bit. So this number is preserved because we want existing smart contracts that use difficulty of code to obtain randomness to not be being broken at the merge and the new semantics of this opcode which is the new name as random is to return the randomness that is accumulated by the beacon chain. One thing to mention here which might be important is that the new randomness is of a size of a full 32 bytes size usually, while the difficulty is less than I don't remember what exact number of bits but it's less than 64 bits I guess. And the mechanics is just to use the mix hash instead of difficulty to keep this randomness inside of the execution layer block. This is to avoid potential issues with the difficulty field that is used currently as a source of information for the puck choice rule in the proof of work network. So we want this difficulty field to be zero after the merge and this is why we use mix hash, this is why this EIP proposes to use mixed hash to hold this randomness instead of difficulty. And from the smart contracts perspective it's just for existing smart contracts, it should be fine, because this difficulty doesn't matter how it's named. Actually what matters is that the instruction number is preserved so it will start returning some really large (not recorded but kept to 32 bytes, but still large) number With respect to what is returned currently but it's still gonna be a valid random randomness output and for the new smart contracts this is the opportunity to use this random as a source of randomness in their code.

**Speaker 9**

* Just a mention to anyone watching who wants to use randomness: Keep in mind that the random value is revealed to some participants of the system prior to the block. So be very sure that if you're going to build something based on that randomness that you fully understand how random it actually is and who knows what the random value is before the block is produced.

**Tim**

* And Marius do you want to talk about the pending block thing because people have questions in the chat?

**Marius**

* We currently maintain a pending block which is basically we just take the current head and we apply all transactions on top of it and this is the the new pending state and we need that for example for creating transactions. If you have already sent three transactions that are sitting in the mempool and you want to get the nonce for the next transaction you need to know what the current state of the head is basically of the mempool and this is the pending block. The problem is with MEV you don't get to see a lot of the transaction and the transaction ordering is different, so we cannot really rely on the pending block anymore and because we need when we create this pending block, we need to apply all of the transactions we currently spending a lot of CPU Time on that on something that's not really meaningfully anymore and so we would to deprecate this soon

**Speaker 10**

* One more question is the relationship between execution clients and consent clients. One-to-one or one-to-many? Can you run multiple execution clients for one consensus client?

**Marius**

* Great question!
We're currently working on a on a piece of software that can do exactly that. That you run one beacon beacon node with multiple execution clients. You cannot run multiple ex beacon nodes with one execution client because the execution client has to maintain a state but you can run of course multiple validators with one beacon node. So you can run multiple validators with one beacon node with one execution client or you could even run multiple validators with multiple beacon nodes who each run with multiple execution layer clients.
So yeah that there's the possibility for you to run one validator on top of all 25 combinations of consensus of beacon and execution layout.

**Speaker 10**

* Awesome thanks!

**Tim**

* Ben you had a couple questions in the chat about the block Time and should we assume that it stays 12 seconds?
So just to summarize: The block Time right now is on average 13 seconds with very random distribution across that. But at the merge it'll go to 12 seconds, so we effectively get one second quicker blocks, but we can mis-block so you're not getting one specifically every next 12 seconds and that's probably not going to change soon but it might change in the future.
Yeah I guess I'm curious what breaks if the block Time changes does anything break from 13 to 12 seconds. I would think so but if it went from 12 to 16 or something that if there's any applications or tooling that will break.

**Ben**

* Just in my experience, I've seen contracts developed that made some kinds of assumptions about block Times. I actually think the compound contracts do this or at least did this, I don't know if there have been upgrades or changes over Time when it comes to interest rate calculations and that sort of thing. But yeah just as a general idea about making assumptions about block Times in contracts.

**Tim**

* Oh right so they assume say you're getting interest every block and they assume a block is 13 seconds and so there's x blocks in a year and that's how you get the APR.

**Ben**

* Yes yeah

**Speaker 11**

* Yeah definitely. Don't do that. Use the block.Timestamp. If what you care about is Time then use block.Timestamp. Especially after proof of stake that should be very reliable.

**Tim**

* We should absolutely reach out to DeFi in general about this. That's a really good point.

**Speaker 12**

* Any other questions about what we've talked about so far?
I don't think we discussed that yet.

**Tim**

* Yeah kind do you want to share a bit?

**Matt**

* I don't think I'm the best person to to share honestly. I think if Danny ... I'll want to talk about it

**Speaker 13**

* When with proof of stake we have several concepts of heads. So currently we have the latest block and proof of work and that recent block that has validated the most recent block your client has seen, that has validated the work algorithm basically and validated the block is legitimate. It's the state transitions are accurate this is a valid block now as everybody knows re-orders can happen and so this block may know may not always be the current head but and at some point in the future it may get reorged out and no longer be in the chain at all.
But that's what you get so when you ask the execution client "hey give me the latest" you get back that block. It's the most recent thing you have.

* With proof of stake we're switching to a mechanism where there's basically three types of blocks: One is what we're calling the unsafe head. So the unsafe head is basically a block that is we have seen and it appears to be valid but not enough people have attested to it and so we don't have any confidence that this block is going to stick around and so we've seen it there. It's possible this may be the next part next block in the chain but we really can't say for sure.
Then after that we have the what's called the safe head and this is a block where we've seen it we've validated it and a bunch of people have voted on it so the addis they've gotten out of stations on it so a bunch of people that are participating in the consensus clients validation scheme. Validators out there have all said "yep I think that's going to be the next block" and once that reaches a sufficient volume - I don't know what it is 33 or 66 or 50 or something - once it reaches that magic number, then we start calling that the safe head and the reason we call it safehead is because it is very very unlikely that that block will be re-worked out. It still can be reworked out so it's not a guarantee. It's not finality but it is very unlikely and so it's very safe to build on top of that block, use that block and assume that block is probably going to stick around.
The third type block we have is post finality boxes. I don't remember what we're calling it exactly but it's a block that has been finalized and the only way that you're going to undo a finalization is with a user activated fork of something. So user intervention basically. You do not undo finalized head so the finalized head will not be undone unless a user shows up and does something. A human interacts with the node directly and says "no I want you to re-org out that finalization". Finalization does not automatically reorg away so when you're building things, if you're building an exchange you may want to wait to pay people out until you see the finalized head include the transactions. That would be a good way to decide "okay am I going to pay this person out in fiat" or "I'm gonna or not" you'd wait for the finalized head. Once you see a finalized head that includes the transaction somewhere behind that, then you're safe if you're building an app that is pretty much anything else. Any normal sort of app or maybe even doing a merchant payment system where you don't have to worry too much about people doing really complicated reorg attacks. The safe head is probably fine so if you're a merchant and someone pays you and you see that shows up in the safe head 12 seconds later or for 28 seconds later or whatever, you're probably fine. You're not going to get ripped off for 12 or whatever by someone doing some massive chain reorg of a safe head. The unsafe head you really should only use that if you're doing data analytics or you're doing you're running ether scan or something or some sort of block explorer. Then you might want to use the unsafe head because you want very instant information or if you're doing some sort of high frequency trading. To say the unsafe head is very interesting again for most people safe head is what you want and so if you ask the execution client for the latest block you will be getting safe head. There will be new ways to ask for the unsafe head and the finalized head but if you just continue doing what you're doing right now, you're gonna get safehead and safehead will usually be somewhere. I think Mikhail can correct me on this. I think it'll usually be somewhere between 0 and 12 seconds behind the unsafe head.

**Mikhail Kalinin**

* Yeah it should be probably four seconds when we see at the stations in. Yeah if the conditions in the network are good it should be four seconds behind the unsafe head, so it's really close actually.

**Speaker 13**

* Yeah so if the network's behaving healthy which in the vast majority of Time it should be, you'll get on. You'll get safehead pretty quickly after unsafe head and you'll get finalization some number of minutes later. I forget how many if the network's unhealthy then you might actually end up with unsafe head for quite a while. You could in theory end up with the safe head never showing up. Finalizations may never show up in the network's very unhealthy these are very edge cases that you should program for but these are not a common case you don't need to worry about them for ux for the most part.

**Speaker 14**

* Yeah I think the interesting thing here for people building applications is if you are releasing real assets whether that's money or physical assets in the physical world and you're looking at a non-komodo consensus chain, we have on either one today, then you might decide how many blocks to wait until you think that it's unlikely everywhere is going to happen and so some exchanges say maybe 35 blocks at that point we don't think that reorg is going to happen. But there's a large spectrum you could choose five blocks if you're doing something much lower a much lower value and with this the spectrum is reduced a little bit where you're either relying on the safe head that the consensus clients are sort of deciding based on what they see in the network or you're relying on the finalized head if you need ultra finality and absolute security.

**Speaker 15**

* That's super interesting: Is there a quantifiable definition? Is safe here a percentage of validators that haven't tested or a probability that won't get reworked out?

**Speaker 16**

* That's what I would also to know this is something I was trying to figure out from some of the consensus people if they had an idea of how much value is behind safehead because nakamoto consensus you can easily determine. If I reorg five blocks that cost roughly this much in hash rate and so I it would be good to know that number for the beacon chain safe head.

**Speaker 17**

* So to answer your question we don't know.

**Speaker 18**

* I understand this is incredibly substantial on the order of one third of state east.

**Speaker 19**

* Yeah Mikhail what is the percentage of validators required to it's not?

**Mikhail Kalinin**

* It's not that easy to quantify it in the percentage of validators. There is a couple of assumptions that were that we make when we're reasoning about the safehead the first one is that your view of the network is the same as everybody else's view which means that you are not eclipsed and there is a synchrony assumption. There is a four second symphony in the network so every message is propagated across the network participant within four seconds and in this case we can say that safehead will be eventually finalized and if we see the safe hat but how the safeguard is computed there is a good presentation by democrat so it's you're starting with the most recent justified checkpoints and counts how many votes, how many other stations we received in this since this checkpoint and for each block in the block tree starting from these checkpoints and if everything is good and enough votes has been done for each block in this chain, I'm pretty much simplifying currently, then we can conclude that this head is safe or not. If we see five percent of other stations for for a block so we it can be real worked for lmd goes the threshold is fifty percent before there is voting for a block. It's not the only condition so it's better to to get this visitation and watch it.

**Speaker 12**

* I feel we got a little bit deep in some stuff there for a second and I know there's some application developers and other people on the call.
I'm just going to share really quickly my screen to show a really simple diagram I put together. This is a diagram I made actually this one was recently but it shows the architecture for how these two chains are interacting.
We have a proof of stake chain the beacon chain formerly called eth2 and the current eth1 chain now which we're calling execution layer is that it's wrapped in this proof of work red bubble and as you can see these two chains have been operating side by side since the beacon chain launched at the end of last year. And then eventually they will come together at the merge. The disclaimer being that Timelines are approximate these dates are always subject to change but we're hoping for let's say q2 next year is the the rough idea but the thing to note here for any application devs is there's no migration progress required you're not going to have to redeploy your contracts, ethereum state addresses, user balances contract code, any sort of information, that tells us what happened in the past, about ethereum and and what's going to happen in the future. That state continues throughout. there's no some previously there had been talks of what what does it look for applications going between are they gonna have to choose which shard to go on the merge is just the replacement of the consensus mechanism so you don't have to worry about migrating your users, migrating your contract, migrating your state. This is all going to happen automatically in the background really unless you're watching the the merged community call you and your users will not really even realize that it has happened aside from there being more dependable block Times, that's probably the most obvious thing that'll happen. And then at the top I just put together a quick summary of the things that have happened so far there's a longer article which go with these but earlier the work for the merge has been going on starting earlier this year. In may there was a month long rainism hackathon that Mikhail was a part of, helped to organize, and then in october we had an amphora event in greece which was we got a bunch of the client teams together and we worked on taking the output of rainism to the next level.
And then right now we're in this last blue blob at the far right and that's devnet's iterating on the spec broadening the participation and that's going to keep going the next hack or the next test net or actually maybe, I'll let Tim talk about this but we're moving into the next step of this which is towards the end of the year. We're gonna move into different test nets Tim I don't know if you want to talk about what's what's next with Kintsugi or somebody else on the call?

# Kintsugi

**Tim**

* We think that at the beginning, we're having a next iteration of devnets right now called Kintsugi in which we're redoing the same thing we did in greece where we're gonna get every client to implement the spec then once they've implemented the spec, you get one one-to-one combinations between execution and consensus layer clients then once you have that working you try to get many too many and then you grow the amount of pairs that you have on the network you send some transactions on the network which which basically test all of the the functionality for example just testing the changes to the difficulty op code and then towards the end we hope that we have a def net that's run through the transition from proof of work the proof of stake and that stays hosted so that people can join that and that's what we're hoping to get before the holidays. And then this way people can start playing around it during the holidays or integrating it right after in january.

**Speaker 12**

* Does anybody have any questions about this diagram before I stop sharing it? Can be high level those are welcome. Key thing to remember is no developers will have to manage migration no users will really experience any sort of downtime. It'll be a as Danny Ryan likes to say: It'll be a consensus hot swap proof of stake, swapped in for proof of work and it'll just happen. All right, cool. Sometimes no questions are a good indicator. I think Tim you also had a link to the Kintsugi talk but maybe we share that actually.

**Tim**

* Yeah I shared that here. If people are really interested they can read through it but it basically walks through what each of the milestones implements. The status for every client so if you're really waiting for your favorite clients to have this implemented, this is the spot where they're gonna post updates. But unless you're following the implementations very closely this is maybe too in the weeds.

**Trent**

* Someone probably answer Stefan's question in the chat.

**Marius**

* Yeah I can quickly answer it. This is because it's easier to say, so you will not run a client that stores both the proof of work chain and the beacon chain. You will run two different clients. One for the beacon chain, one for the proof of work chain. You will run two different clients, the execution layer client will be will be syncing from genesis and executing all the blocks but the block propagation for all the historical blocks will be handled by the execution layer client, and all the new blocks and the block propagation will be handled by the consensus layer client. So you would need to run a gath note or ? and a beacon chain note prism or lighthouse or whatever.

**Speaker 12**

* Thanks Marius. I'm just going through the questions that are coming in the chat. Looks the next one was from Ben about communicating with miners.
We haven't had any merge related calls directly with them but earlier this year we had a few . I mean Pooja who has ran at least one that I know of and I've made a point to engage with miners on reddit which is the ether mining and gpu mining subreddits, to try and communicate these things. Especially because in the build up to 1559 we wanted to make sure, people were aware of this. I think proof of stake has been on the horizon for miners for a long Time. They're aware of it but the the issue is, since it's been on the Timeline for so long, that many have just discounted it or they think, it's never going to happen. So even if we started communicating these things that may or may not have an effect, hopefully they start to pay attention and can see that things are happening and specs are being released. Things that we have test nets it's more than just a meme and it's gonna happen sooner rather than later. But all throughout this year we've been telling people conservatively that mining was going to end at the end of the year. Obviously that's not the case but I think we've started the communication process and I know some of the mining pools are also planning to participate in staking so they'll be communicating this again hopefully sooner rather than later to their constituent hash rate to make sure that they're aware of what's happening once we get closer to the merge. And I expect that they'll be doing their own sort of messaging and marketing. We're not going to be able to reach every miner but as for what's going to happen between now and the merge, possibly something to consider, but we'll definitely continue at least what we've been doing, which is regular and consistent messaging going into the miner communities, trying to make sure that they're aware that this is is imminent.

**Tim**

* And one thing I'll add to that is a lot of people don't upgrade until there's a blog post on ethereum.org. So we're definitely gonna have that, I think what we want probably before having that is just a much more finalized specs and whatnot and not only for miners but given the uniqueness of this upgrade which isn't the same as previous upgrades where you just tell people "download the new version and that's it". We're probably gonna have to be much more thorough in explaining that and what should people do. Not only for miners but people that are running a validator, people that are running in each one node not mining so we're gonna need to just be pretty explicit to what all the different types of users need to do.
I just think we want to be a bit farther along in the process before we have that so that people so that the things we point people towards are stable.

**Trent**

* So miners, we have discussed quite a bit the various attack factors that miners could launch against ethereum on the way out, so as we approach the merge the incentives to be good citizens decreases the way the merge is designed and the way the process will happen is designed specifically to deal with that. We could do the merge much simpler if we didn't have to deal with that and so: Yes we have talked about it, we believe that the way the terminal difficulty stuff is set up mitigates the biggest set of attack vectors without going completely crazy and delaying the merge by another two years in engineering effort. We should actually have Mikhail talk about that he knows it better than I do.

**Speaker 12**

* Is he still here Mikhail?

**Mikhail Kalinin**

* Yeah what do you want me to tell you?

**Speaker 12**

* Do you want to give a just a really short summary of what total terminal difficulty is and yeah it's safe?

**Mikhail Kalinin**

* Terminal total difficulty is the trigger for the actual merge for the transition from the proof-of-work to proof-of-stake and the question that often arises here is why we don't use the block number as in the regular hard forks. In simple words the the fortress rule the fork choice rule handover between the proof-of-work and proof-of-stake is happening in at the point of transition and since the workforce rule is based on the total difficulty. It means that we need to to do this handover at a certain total difficulty because the block number. If we use a block number there could be a minority fork that is built and withheld by some adversary and is revealed later at the point of merge and this fork may has much less value, much less solid difficulty value, so it could be easier to be built and it's possible the minority fork attack and if we have also the adversarial leader or it could be the same party and this father the proposer of the first proof-of-stake block can take this minority fork and build a block on top of it. And with respect to the block number, block height rule, everything will be okay but with respect to the work contributed to this fork and it will not be okay because it will be a minority of work and not the one that would be the canonical one in terms of total difficulty focus rule. So that's why the terminal total difficulty is used to trigger the actual transition. I think 104 lincoln. There is also the original section in the [EIP-3675](https://eips.ethereum.org/EIPS/eip-3675).

**Trent**

* This may may impact people in this call and the reason for that is because we're doing total sort of terminal total difficulty. We can't pick a ttd terminal total difficulty until very close to time and so normally when we do hard forks, we pick the hard fork block a month ahead of Time. We say "okay is going to be the hard fork block whenever we get there" that's when the hard fork happens. We hand wave when that is with terminal total difficulty because the difficulty can fluctuate quite a bit over Time, especially if miners start selling their hardware off early or something. We can't advertise what the ttd is going to be early because it could end up that now we've gotta wait two years for us to actually reach that ttd when we meant to plan for a month. And so more than likely what's gonna happen is the clients will be released that have all the code for the merge in and then some placeholder ttd maybe and then when we're a week away from when we want to actually run the merge, we'll release. We'll do two things. One we'll announce what the actual ttd is and we'll release an updated client. Updated clients that include that ttd baked in. Also these the clients will have a mechanism for overriding the ttd so that way if you've already upgraded your infrastructure and everything when we release the clients a month in advance, you only have to change one config option in order to use that new ttd that we're going to announce a week before the merge happens and so users can either choose to just upgrade their clients again for home users. It's probably the easiest one whereas if you're running some sort of infrastructure of your infrastructure provider and you want to do a bunch of testing against the clients as far in advance as possible and you probably don't want to upgrade a week before the merge in which case you can just change the config option the environment variable or cli option or config file or whatever the mechanism you use to configure your client. And so that may impact people and again slightly different than our normal forking process and this is specifically to mitigate attacks against the merge.

**Speaker 12**

* Yeah the beautiful thing about difficulty leading up to the merge trying to balance between miner, our miners going to stay on the network or are they going to leave is that it's self-adjusting and that if if too many miners leave, there'll be a ton of profit left leading up to the merge and it should auto balance. Should but those are what we're thinking about and it seems it should be all right leading up to the merge.
We are almost exactly at Time Tim. Do you have anything that we missed or wanted to cover?

**Tim**

* I don't. I was going to say if people have questions or at least topics they'd want to cover on the next one of these if you can leave them on the [GitHub Issue](https://github.com/ethereum/pm/issues/402) the agenda of this call that's really helpful. I feel it probably makes sense to have another one of those a month from now probably not two weeks but a month.
Ideally if we by then we might not have the Kintsugi devnets but we'll probably be close enough to it to tell you what to expect and then if people have other questions we can just spend Time entering those. But yeah, this was really really valuable. Thanks for everyone who asked questions and showed up!

**Trent**

* If someone wants to get invited to the next version iteration of this where should they follow or watch.

**Tim**

* So trent can give you a calendar invite if that's what you're after. If you don't want a calendar invite, the ethernet discord and then the ethereum/pm repo we'll have the information.

**Speaker 12**

* Yeah and if you're part of something, a web3 provider or something related to infrastructure in some way, just give me your email and I will add you to the list of people that get this invite automatically. But I do keep it scoped to just people who are working on infra because a public call could blossom pretty quickly into something much larger than it needs to be so we to keep it small when they can be small. And yeah it will be uploaded after the recording of this will be uploaded to the ef youtube sabotage just dm me on discord or twitter and I can give you the link to the discord.
Anything else last minute?

**Tim**

* A quick question: Would a transcript of this call be useful to someone is it worthwhile for us to just get some transcripts done?

**Speaker 12**

* Yeah or at least, at the very least a rough summary of the stuff that came up and that would be okay, cool.

**Tim**

* Okay we'll try and get some notes for the call and at least so if people just want to follow that and not watch the whole video, that they can do that.

**Speaker 12**

* Great, thanks everybody for showing up and participating in the discussions and we're all excited for the merge. I know everybody has always been excited about the merge but it's real, it's happening, it's going to be amazing. All right thanks for coming everybody!

## Attendees
- Tim
- Trent
- Mikhail Kalinin
- Marius
- Matt
- Ben
- Various unidentified speakers

## Links discussed in the call (zoom chat)
- [EIP-3675](https://eips.ethereum.org/EIPS/eip-3675)
- [EIP-4399](https://eips.ethereum.org/EIPS/eip-4399)
- [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559)
- [EIP-3675](https://eips.ethereum.org/EIPS/eip-3675)

## Next Meeting
TBD (about a month from now)