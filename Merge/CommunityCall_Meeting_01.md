# Merge Community Call 1

### Meeting Date/Time: Friday, Nov 5 14:00 UTC
### Meeting Duration: 1 hour
### [Agenda](https://github.com/ethereum/pm/issues/402)
### [Video of the meeting](https://www.youtube.com/watch?v=_kfS9jAUY6g)
### Moderator: Trent
### Notes: Stefan Wüst

-----------------------------

# Intro

**Trent**

* So this call is the first merged call that we're running tim and i it's not the only one uh puja has run some related to this as well you should definitely check out those videos but this is the first one that we're running we're going to go over what the merge is what it's not and some quick updates on the state of things and hopefully answer any questions that people have about things we are recording tim do you want to start with anything

# Summary on the state of things

**Tim**

* sure i guess um there's a lot of like new faces on this call so maybe it's worth just taking five or so minutes to walk through what the merge actually implies from like an ethereum node perspective um then um i have like a couple kind of um just things that i think people should be aware of uh at the application and like infrastructure level and then i think we can take most of the call to just answer people's questions or chat about it and yeah and see also yeah one thing that that would be helpful is knowing you know if people have questions even though we can't answer them on this call we can schedule you know calls in the future and so as you'll you'll find out where you know we're still i wouldn't say early in the merge progress but we're you know we're still at the spot where we have enough time to to have kind of dedicated calls about specific topics uh yeah over the next couple months

**Trent**

* um cool yeah so i guess yeah i'll just share my screen um and i'll post the link to what i'm sharing in the chat here but at a high level so i i tried to summarize what the merge actually oh i can't actually share my screen trends the host has disabled screen sharing

**Trent**

* embarrassing um go ahead try now

**Tim**

* uh oh yes i can okay awesome cool okay so i tried to like summarize what the merge actually is uh in the post i showed in the chat um a lot of this is is based on uh diagrams and and kind of work that uh danny ryan had put together um a very high level the way to think about like an ethereum node after the merge is is this diagram that i'm sharing right now where um you're gonna have uh you're gonna have to run both a beacon node and what we call an execution node which is the equivalent of an eth1 client today um and basically what the merge is is it's just taking uh the current eth1 clients and instead of having them follow uh proof of work or proof of authority for their consensus and to find out like the the chain head um we have them follow the beacon chain so um you have kind of your whole theorem client which is the sum of your beacon node which will maintain its peer-to-peer connections like it does right now so you know the whole peer-to-peer network where at the stations and and blocks are shared uh will remain part of the beacon node

* similarly all the beacon apis that already exists will remain you know part of those beacon nodes and you can query your node directly for that then the execution engine is a modification to eth1 clients but those will be made available by the different uh the different teams so you'll be able to downline the aragon version of this um and this is basically an eth1 client which uh strips down everything related to consensus so it just relies on the beacon node for consensus but it'll still be in charge of block execution validating that transactions are are valid um and maintaining its own transaction pool as well as gossiping the transactions so this is why you also keep kind of the same peer-to-peer layer where the main difference is you are not broadcasting blocks anymore on the the execution peer-to-peer layer but the the transaction propagation still happens there um and similarly all of the json rpc apis uh will still be present and then in order to kind of facilitate communication between the beacon node and the execution engine we've introduced a new api called the engine api and this is basically the uh api by which the beacon node will share a new head a new finalized block with the execution engine and will also query the execution engine when it's uh when it's the validator's time to produce a block uh for a valid block that you can share with the network and at a high level

* that's really it um the way we transition uh at the merge basically is using a total difficulty value on the ethereum maintenance and uh there's a couple security reasons for that um but at a high level it's just kind of the safest way to go about it so what will happen is that we're going to have an update an upgrade on the beacon chain where we'll add a terminal total difficulty value so the kind of final difficulty that we want to see on the proof of work chain uh the the beacon chain will be querying kind of the proof of work chain every block asking it you know did you reach this this total difficulty no did you reach just sold difficulty no and at some point it will so whichever block basically has a total difficulty larger equal than this terminal value will be the final block uh on the proof of work chain and from that point on uh the eth1 clients will begin following the beacon chain for consensus rather than than proof of work um and one thing to note is obviously there can be multiple blocks kind of that come at that time with a similar total difficulty and then we rely on the beacon chain consensus to kind of decide the canonical blocks um between say there were two competing blocks that were that were shared at the same time um and so after the merge um what kind of the beacon chain will look or or what blocks sorry will look like it's kind of like this where on the other layer you have the what's a beacon chain block today uh which contains you know things like the the current slot uh signature randall all the at the stations the deposits the validator exits and within those um will basically add what we call an execution payload which is the equivalent of an eth1 block today and this is produced by the execution layer so this execution payload is what gets passed around between the validator layer and the execution layer um and these contain exactly what you'd see in an eth1 block today so you know the hash the state routes at the list of all the transactions um and again you know when kind of you receive a block on the network it'll it'll go to your your consensus layer and you'll pass it to the execution layer to actually execute the block make sure that it's valid um and similarly when you need to produce a block for the network you'll just query it from your execution layer and then propagate it on your on the consensus layer um i mentioned earlier there's uh this engine api that we're working on which is the communication interface we're still kind of finalizing it but at a high level there's three kind of apis that are that are going to be added one is called this engine execute payload which is the consensus layer sending a block to the execution layer to just validate it uh execution layer returns whether it's valid or invalid if it's still syncing you know just return syncing and ask you know for it to be sent later um the kind of biggest uh addition is this for choice updated call which the execution the consensus layer uses to tell the execution layer that there's a new head and then you finalize block on the network and optionally it can also pass it what we call a payload attribute which is uh asking the execution layer to start producing a block and giving you things like the timestamp the randall value and the the fee recipient or the coinbase value that's that's required um and this is how basically if the execution layer gets a call from fork choice updated which contains this payload attribute shield it knows it needs to start producing a block and then uh there's a final call called engine get payload which asks the execution layer to retur to return its current best block so those come kind of come after you've asked it to produce a block and then you just ask it to uh send one back um and also really ideally the three only endpoints we're going to add as i said it's still kind of being discussed but we we really want to try and keep this uh communication channel simple um and then yeah so just worth noting not much changes on the execution layer um so there's an eip that describes all the chain [EIP-3675](https://eips.ethereum.org/EIPS/eip-3675) um but basically the block itself won't change the only thing is any field that's related the proof of work or to uncles gets set to zero uh or you know like the data structure is equivalent to zero um just because we don't need those anymore um yeah and uh obviously once the merge happens there's no more block rewards so that stops um but it's worth noting that transaction fees still get processed by the execution engine um and one thing that's kind of not really obvious is that transaction fees can be sent to an like eth1 address so they don't accrue to the validator addresses but they'll accrue to addresses um in uh in the execution layer um and then yeah here's again a diagram by danny that kind of shows how how the merge happens so at the left side of it um you have kind of the proof of work chain as it is today so you have proof of work within proof of work we have our execution layer engines that produce eth1 blocks and we have a chain of those similarly on the beacon chain you know we have uh blocks that are kind of empty they don't oh they contain kind of beacon chain data but they don't contain any executable transactions and then around the merge we're basically just dropping proof of work and this this part that contains kind of the what gets executed in a block becomes the execution payload in in uh kind of the post merge system um and we just remove proof of work and beacon chain is now our source of consensus um and then i already kind of covered yeah so basically both both uh both the consensus and execution layer maintain a peer-to-peer network they maintain their current user apis and the big thing that we're still working on is sync so sync obviously needs uh both parts to interact with each other and there's a couple prototypes for different syncing mechanism but there's not one that's been kind of fully uh fully uh deployed yet um so i'll i'll probably i'll pause here uh it feels like i went on for a while um just and i see there's a lot in the chat um is there i guess where there are questions in the chat i see there's like mica like client and marius okay uh yeah before i guess we just got does anyone have questions or thoughts ?

**Speaker 3**

* oh can you guys hear me okay yes yes let's go ahead hi tim so i put a okay i put a question about whether or not validator rewards that are occurring to addresses on the consensus layer if they're going to be transferable after the merge

**Tim**

* not in the emerging hard fork like at some point after that

**Speaker 3**

* so it will just be the transaction fees that validators can actually like say move to an exchange or like do anything with 

**Tim**

* yes yes

**Speaker 3**

* okay gotcha and is there like an estimated timeline for when the validator rewards on the consensus layer will be unlocked

**Tim**

* um no given that work i mean like it's the main priority after the merge but just not comfortable giving like a a month or like a date given that like we we haven't done the merge but after the merge basically the most you know the highest priority thing is beacon chain withdrawals basically

**Speaker3**

* gotcha gotcha okay thank you

**Speaker 4**

* and just for some small additional contacts related to your question people when we say transaction fees um that also includes mev type stuff which there's a good chance if current history predicts the future um the mev stuff might actually you know outstrip all the other forms of validator rewards and payments so don't assume that just because it's transaction fees only that it's going to be some tiny little amount that it could be significant

**Speaker 3**

* definitely thanks

**Tim**

* um so there's a question what do you mean by mev so basically yes it's still a transaction fee yes

**Speaker 4**

* but it's not just not all not only comes in foreign transaction fees sometimes direct payments to the what was previously called coinbase which will now be the fee recipient so you'll get a transaction that will show up in a block that you as a validator produce and the transaction will just directly send money to the block producer and so if the block producer puts in you know some ethereum address as their address they want to receive fees at that mev payment will also go there

**Tim**

* yes 

**Speaker 4**

* it's an execution later

**Speaker 5**

* i'll just jump in and say really quick one of the things that uh we're trying to uh adapt to is different naming schemes many of you are probably familiar with that the merge used to be called or you know this big project used to be called eth2 um but that sent some different messages to people about like sequentiality and how product's working so you've probably heard tim say a few times execution layer and consensus and these are kind of the terms that we're trying to shift towards as they are more accurate and they don't have to deal with numbers um because in reality uh ethereum is going to exist there won't be separate editions of it you know one is going to die and one is going to take its place things like that i'll share a graphic later but tim if you want to keep going yeah and micah would be angry that's correct

**Tim**

* any other questions?

**Speaker 6**

* yeah this has been super helpful thanks for sending us together um i'm curious so i for my understanding there's an existing test net which everyone is testing this on will the merge happen in other test nets also?

**Tim**

* Yes um so that was going to be kind of my next thing but at a high level um we have a devnet right now which is called pitos i would recommend joining it only if you know you want to be at the very forefront it's still it's still quite experimental the best way to join it on the eatstaker discord there's a pitos channel so um it'll be quite manual onboarding to it um right now throughout november we're working on a second uh iteration of devnets and the goal is to get kind of a public long-standing one uh before the holidays so that people end with you know kind of readmes and actual instructions for people to join so that'll be a new network um and and hopefully you should have kind of the final spec so if if you want to kind of see see it first uh that'll be the place to go um and then we are going to run the merge on uh several of the existing test nets like robsten wrinkby and whatnot um the order and timing is still not determined there's a high chance robson would be first because robson has a difficulty bomb on it uh which might go off sometime in january so if that happens then it might just make sense to run the merge on robson first um but yeah before we do that we want to have just new devnets that are up uh and that we know are kind of working well um yeah um yeah 

**Speaker 6**

* why don't you finish your first talk
sorry i thought you were going to keep going with questions but if you just wanted to wrap up that first thing you were going through

**Tim**

* i have another question okay so sorry greg has another question fee recipient is a new word that we've used but it maps the coin base basically uh just to make it clearer because it's not mining but it's basically the same as a coinbase uh

**Speaker 7**

* but the field itself will be on the execution block not the consensus block or because there's a slot i should say oh

**Speaker 8**

* tim can you clarify if the from that diagram that you showed that block propagation will be by the beacon change and so that all sort of pre-consensus no pending blocks moving around that's going to continue on the pdp layer of the execution engine but the only way that the execution engine knows about blocks is through that engine api

**Tim**

* exactly yeah and basically what happens is that once once we hit a block with a terminal total difficulty and you stop propagating blocks that have not hit that and then once you've had like a finalized block on the beacon chain after that the execution layer just stops propagating blocks altogether

* um okay so ben has a question uh will every beacon chain block have an execution layer block in it?
so no basically so you can still have somebody missed or missed their validator slot right um so just like today if your validator is offline when it needs to propose a block um that block will be missed um and uh we've been looking at uh kind of the impact of that on [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559) so like how do we want to treat missed slots um with regards to like the base fee and like the block capacity so there might be some changes that we make alongside the merge uh to just take into account uh potential missed slots when you're calculating the the base fee so we we expect obviously you know like validators have an incentive to produce the block and and it becomes even stronger after the merge because they actually get the transaction fees but if a validator is offline when it's their turn to produce a block then uh that blocks kind of kind of get skin um

* and then there's a good question also
how do we plan to run full test nets without finalizing the sync mechanism so we have a couple prototypes of the sync mechanism um i'm not like super familiar with them i don't know if i see marius is on the call i don't know marius if you've been following the the latest sync

**Marius**

* yeah so um we're currently working on that we have a prototype for pitfalls but yeah there's still some stuff to do to get it merged into the clients

**Tim**

* these are really good questions

**Mikhail Kalinin**

* basically i just wanted to add that the execution layer will receive all the information required for to bootstrap the sync mechanism and keep it progressing from the consensus layer which is the execution execute payload commands with the payloads and the public choice updated stuff that points to the head to the current head of the chain through observation of contest layer and another thing to mention here is that consensus layer can reach out to the head of the chain a kind of optimistic way and then the execution layer can use this information about the current head and about the current state of the network to sync up and pull the state and become able to become capable of executing payloads that's the kind of the strategy that is currently prototyped and evaluate in this being evaluated in the testnets

# EIP-4399

**Tim**

* i guess Mikhail since you were speaking the next thing i was going to cover is that your new [EIP-4399](https://eips.ethereum.org/EIPS/eip-4399) but do you want to take a few minutes to kind of walk through that and also basically not a lot changes for like smart contract layer and anybody using the the kind of execution layer data but that's one of the changes do you want to maybe walk through kind of that and and any other changes that people writing smart contracts are just depending on the execution layer should be aware of

**Mikhail Kalinin**

* oh yeah sure so this eip is the basically what it does it just lands the um existing difficulty of code yeah okay thanks for sharing this screen it actually supplies the existing difficulty of code with the new random of code the key okay there are several things here first of all the number of the instruction is not changed so it's just basically the renaming of the difficulty to random and the change in the semantics a bit so this number is preserved because we want existing smart contracts that use difficulty of code to obtain randomness to not be being broken at the merge and the new semantics of this opcode which is the new name as random is to return the randomness that is accumulated by the beacon chain um one thing to mention here which might be important is that the new randomness is of a size like of a full 32 bytes size usually while the difficulty is like less than i don't remember what exact number of bits is currently is but it's less than 64 bits i guess um so yeah and the mechanics is just i don't know if we want to dive into mechanics the mechanics is just to use the mix hash instead of difficulty to uh keep this randomness inside of the execution layer block this is to avoid potential issues with the difficulty field that is used currently is as a source of information for the puck choice rule in the proof work network so we want we really want this difficulty field to be zero after the merge and this is why we use mix hash this is why this EIP proposes to use mixed hash to hold these randomness instead of difficulty so and from the smart contracts perspective it's just for existing smart contracts it should be fine because this difficulty doesn't matter how it's named actually uh what matters is that the instruction number is preserved so it will start returning some really large uh like not recorded but kept to 32 bytes but still large number with respect to what is returned currently but it's still gonna be a valid random randomness output and for the new smart contracts this is the opportunity to use this random as a source of randomness in their code so that's basically it

**Speaker 9**

* just a mention to anyone watching who wants to use randomness keep in mind that the random value is revealed to some participants of the system prior to the block so be very sure that if you're going to build something based on that randomness that you fully understand how random it actually is and who knows what the random value is before the block is produced

**Tim**

* and marius do you want to talk about the pending block thing because people have questions in the chat

**Marius**

* yeah so basically um we currently maintain a pending block which is basically we just take the current head and we apply all transactions on top of it and this is the the new pending state and we need that for example for uh for creating transactions basically like if you if you have already like sent three transactions that are sitting in the mempool um and you want to get the nonce for for the next transaction uh you basically you need to know what the current state of what the current state of the the head is basically of of of the of the mempool and this is the pending block the problem is with mev you don't get to see a lot of the transaction and the transaction ordering is different so we cannot really rely on the pending block anymore and because we need like when we create this pending block we need to apply all of the transactions uh we currently like spending a lot of cpu time on that on something that's not really meaningfully anymore and so we would like to deprecate this soon

**Speaker 10**

* one more question um is the relationship between execution clients and consent clients one-to-one or one-to-many like can you run multiple execution clients for one consensus client

**Marius**

* great question we're currently working on a on a piece of software that can do exactly that that you run one beacon beacon node uh with multiple execution clients you cannot run multiple ex beacon nodes with one execution client um because uh the execution client has to maintain a state but you can can run of course run multiple validators with one beacon node so you can run multiple validators with one beacon node with one execution client or you could even run multiple validators with multiple beacon nodes uh who each run with multiple uh uh execution layer clients so yeah that that there's there's there's there's the possibility for you to run one validator on top of all 25 combinations of consensus of beacon and execution layout 

**Speaker 10**

* awesome thanks

**Tim**

* yeah i'm curious yeah ben you had a couple questions in the chat about like the block time and should we assume that it stays 12 seconds so just to kind of summarize like the block time right now is on average 13 seconds with very random distribution across that but at the merge it'll go to 12 seconds so we effectively get like one second quicker blocks um but we can mis-block so you know you're not getting one specifically every next 12 seconds um and that's probably not going to change soon but it might change in the future um yeah i guess i'm curious what what breaks if like the block time changes um like does anything break from 13 to 12 seconds i would think so but like if it went from like 12 to 16 or something like that yeah i'm curious if there's any applications or tooling that that will break uh

**Ben**

* just in my experience i've seen uh contracts developed that made like some kinds of assumptions about block times i actually think the compound contracts do this or at least did this i don't know if there have been upgrades or changes over time when it comes to like interest rate calculations and that sort of thing um but yeah just as a general idea about making assumptions about block times in contracts

**Tim**

* oh right so they assume like say you're getting interest every block and they assume a block is 13 seconds and so there's like x blocks in a year and that's how you get the apy or something like that

**Ben**

* yes yeah

**Speaker 11**

* yeah definitely don't do that use the block.timestamp if you need to do to if you if if what you care about is time then use block.timestamp especially after proof of stake that should be very reliable

**Tim**

* okay well yeah we should absolutely reach out to DeFi in general about this that's a really good point

**Speaker 12**

* any other questions about what we've talked about so far i don't think we discussed that yet

**Tim**

* yeah like kind do you want to share a bit

**Matt**

* i don't think i'm the best person to to share honestly i think i don't know if danny or um okay i'll want to talk about it

**Speaker 13**

* i can't if matt wants chicken out um so the uh so when with proof of stake we have several concepts of heads so currently we have the latest block and proof of work and that recent block that has validated the most recent block your client has seen that has validated the work algorithm basically and validated the block is legitimate it's like the state transitions are accurate this is a valid block now as everybody knows re-orders can happen and so this block may know may not always be the current head but and at some point in the future it may you know get reorged out and no longer be in the chain at all um but that's what you get so when you you ask the execution client hey give me the latest you get back that block it's the most recent thing you have with proof of stake we're switching to a mechanism where there's basically three types of blocks one is what we're calling the unsafe head i think someone correct me if i misremembering the name we're using so the unsafe head is basically a block that is we have seen and it appears to be valid but not enough people have attested to it and so we don't have any confidence that this block is going to stick around and so we've seen it there it's possible this may be the next part next block in the chain but we really can't say for sure then after that we have the what's called the safe head and this is a block where we've seen it we've validated it and a bunch of people have voted on it so the addis they've gotten out of stations on it so a bunch of people that are participating in the consensus clients validation scheme uh yes by people i mean validators sorry so a bunch of validators out there have all said yep i think that's going to be the next block and once that reaches a sufficient volume i don't know what it is 33 or 66 or 50 or something some some number um once it reaches that magic number then we start calling that the safe head and the reason we call it safehead is because it is very very unlikely that that block will be worked re-worked out it still can be reworked out so it's not a guarantee it's not finality but it is very unlikely and so it's very safe to build on top of that block use that block and assume that block is probably going to stick around the third type block we have is uh post finality boxes i don't remember what we're calling it exactly but it's a block that has been finalized and the only way that you're going to undo a finalization is with a user activated fork of something so user intervention basically you do not undo finalized head so the finalized head will not be undone unless a user shows up and does something like a human interacts with the node directly and says no i want you to re-org out that finalization finalization does not automatically reorg away um so when you're building things like if you're building an exchange you may want to wait to pay people out until um you see the finalized head include the transactions that would be a good way to um decide okay am i going to pay this pay this person out in fiat or i'm gonna or not you'd wait for the finalized head once you see a finalize head that includes the transaction somewhere behind that then you're safe if you're building an app that you know is pretty much anything else like any normal sort of app or maybe even doing like a merchant payment system where you don't have to worry too much about people doing like really complicated reorg attacks the safe head is probably fine so if you're a merchant and someone pays you and you see that shows up in the safe head you know 12 seconds later or for 28 seconds later or whatever you're probably fine like you're not going to get ripped off for 12 or whatever by someone doing some massive chain reorg of a safe head um the unsafe head you really should only use that if you're doing like data analytics or you're doing you're like running ether scan or something or some sort of block explorer then you might want to use the unsafe head because you know you want very instant information or if you're doing some sort of high frequency trading to say the unsafe head is very interesting again for most people safe head is what you want and so if you ask the execution client for the latest block you will be getting safe head there will be new ways to ask for the unsafe head and the finalized head um but if you just continue doing what you're doing right now you're gonna get safehead and safehead will usually be you know somewhere i think Mikhail can correct me on this i think it'll usually be somewhere between 0 and 12 seconds behind the unsafe head um

**Mikhail Kalinin**

* yeah it should be like probably four seconds when we see at the stations in in the yeah if the conditions in the network are good it should be four seconds behind the unsafe head so it's really close actually yeah

**Speaker 13**

* yeah so if the network's behaving healthy which in the vast majority of time it should be you'll get on you'll get safehead pretty quickly after unsafe fed and you'll get finalization some number of minutes later i forget how many um if the network's unhealthy then you might actually end up with unsafe head for quite a while like you could in theory end up with the safe head kind of never showing up finalizations may never show up in the network's very unhealthy these are very edge cases that you should program for but these are not a common case you don't need to worry about them for like ux for the most part

**Speaker 14**

* yeah i think the interesting thing here for people building applications is if you are like releasing real assets whether that's like money or physical assets in the physical world and you're looking at like a non-komodo consensus chain like we have on either one today then you might decide how many blocks to wait until you think that it's unlikely everywhere is going to happen and so like some exchanges say like maybe 35 blocks at that point we don't think that uh reorg is going to happen but there's like a large spectrum you could choose five blocks if you're doing something much like lower uh like a much lower value and with this the spectrum kind of is reduced a little bit where you're either relying on the safe head that the consensus clients are sort of deciding based on what they see in the network or you're relying on the finalized head if you need like ultra finality and absolute security

**Speaker 15**

* that's super interesting is there like a quantifiable definition is safe here like a percentage of validators that haven't tested or a probability that won't get reworked out

**Speaker 16**

* that's what i would also like to know this is something i was trying to figure out from some of the consensus people if they had an idea of like how much value is behind safehead because like nakamoto consensus you can easily determine like if i reorg five blocks that cost roughly this much in hash rate and so i it would be good to know that number for um the beacon chain safe head

**Speaker 17**

* so to answer your question we don't know

**Speaker 18**

* i understand this is incredibly substantial like on the order of like one third of state east

**Speaker 19**

* yeah Mikhail what is the percentage of validators um required to it's not

**Mikhail Kalinin**

* it's not that easy to quantify it in the percentage of validators there is a couple of assumptions uh that were that are that we make when we're reasoning about the safehead the first one is that your view of the network is the same as everybody else's view which is which means that you are not eclipsed and there is a synchrony assumption there is a four second symphony in the network so every message is propagated across the network participant within four seconds and in this case uh we can we we may say that we can say that safehead will be eventually finalized um and it if we see the safe hat but how the safeguard is computed there is a good presentation by democrat so it's like um you're starting with the most recent justified checkpoints and counts how many um votes uh how many other stations we received in this since this checkpoint and for each block um in the block tree starting from these checkpoints and if everything is good and enough votes has been done for each block in this chain i'm pretty much simplifying currently then we can conclude that this head is safe or not if we like see like five percent of other stations for uh for a block um so we it can be real worked uh for lmd goes the threshold is fifty percent um before there is voting for a block so but yeah it's not the only condition so it's better to to get this visitation and watch it

**Speaker 12**

* all right really quick i'm going to jump way back out for a second i feel like we got a little a little bit deep in some stuff there for a second and i know there's some application developers and other people on the call i'm just going to share really quickly my screen to show a really simple diagram i put together yeah this is a diagram i made a actually this one was recently but it shows the architecture for how these two chains are interacting right we have a proof of stake chain the beacon chain formerly called eth2 and the current eth1 chain now which we're calling execution layer is that it's wrapped in this proof of work uh red bubble and as you can see these two chains have been operating side by side since the beacon chain launched at the end of last year and then eventually they will uh come together at the merge the disclaimer being that you know timelines are approximate these dates are always subject to change but we're hoping for let's say q2 next year is the uh the rough idea um but the thing to note here for any application devs is there's no migration progress there's no migration process required you're not going to have to redeploy your contracts ethereum state you know addresses user balances uh contract code any sort of information that tells us what happened in the past about ethereum and and what's going to happen in the future that state continues throughout there's no um you know some previously there had been talks of like uh what what does it look like for applications going between are they gonna have to you know choose which shard to go on the merge is just the replacement of the consensus mechanism so you don't have to worry about migrating your users migrating your contract migrating your state this is all going to happen automatically in the background really unless you're watching you know the the merged community call you and your users will not really even realize that it has happened aside from there being more dependable block times uh that's probably the most obvious thing that'll happen but um yeah and then at the top i just put together a quick uh summary of the things that have happened so far there's a longer article which go with these but earlier the work for the merge has been going on starting earlier this year in may there was a month long rainism hackathon that Mikhail was a part of helped to organize and then in october we had an amphora event in greece which was we got a bunch of the client teams together and we worked on you know taking the the output of rainism to the next level and then right now we're in this last blue blob at the far right and that's you know devnet's iterating on the spec um broadening the participation and that's going to keep going uh the next hack or the next um test net or actually maybe i'll let tim talk about this but we're moving into the next uh step of this which is towards the end of the year we're gonna move into different test nets tim i don't know if you want to talk about what's what's next with kinsuki or somebody else on the call

# Kintsugi

**Tim**

* i can so um basically kind of like we we think that at the beginning um we're having like a next iteration of devnets right now called Kintsugi which were in which we're kind of redoing the same thing we did in greece where we're gonna get every client to implement uh the spec then once they've implemented the spec you kind of get one one-to-one combinations between execution and consensus layer clients then once you have that working you try to get many too many and then you kind of grow the amount of pairs that you have on the network uh you send some transactions on the network which which basically test all of the uh the functionality um for example just testing kind of the changes to the difficulty op code um and then towards the end we hope uh that we have kind of a def net that's run through the transition from proof of work the proof of stake and that kind of stays uh hosted so that people can join that and that's what we're hoping um yeah that's what we're hoping to get before the holidays and then this way people can start playing around it during the holidays or integrating it right after in january

**Speaker 12**

* does anybody have any questions about this diagram before i stop sharing it can be high level uh those are welcome key thing to remember is no developers will have to manage migration no users will really experience any sort of downtime it'll be a as danny ryan likes to say it'll be a consensus hot swap proof of stake swapped in for proof of work and it'll just happen all right cool yeah sometimes no questions are a good indicator um i think tim you also had a link to the Kintsugi talk but maybe we share that actually okay perfect yeah

**Tim**

* yeah i shared that here i mean it's not i mean if people are really interested they can read through it but it basically walks through what each of the milestones implements kind of the status for every client so you know if you're like really waiting for your favorite clients to have this implemented this is the spot where they're gonna post updates um but yeah unless you're following the implementations very closely this is maybe two in the weeds uh

**Trent**

* someone probably answer stefan's question in chat

**Marius**

* yeah i i can i can quickly answer it uh like this because it's easier to to to say um so you will not run a client that stores both the proof of work chain and the beacon chain you will run two different clients one for the beacon chain one for the proof of work chain sorry i'm in the in the df office now it's really loud here uh you will run two different clients uh the the um the execution layer client will be uh will be uh syncing from genesis and executing all the blocks but the block propagation for the so all the historical blocks will be handled by the execution layer client and all the new blocks and the block propagation will be handled by the consensus layer client so you would need to run a gath note or nether mind obisu and a beacon chain note like prism or lighthouse or whatever

**Speaker 12**

* thanks marius i'm just going through the questions that are coming in the chat looks like the next one was from ben about communicating with miners we haven't had any merge related calls directly with them but earlier this year we had a few uh by we i mean puja who's iran at least one that i know of and i've made a point to engage with miners on reddit which is the ether mining and gpu mining subreddits to try and communicate these things especially because in the build up to 1559 we wanted to make sure people were aware of this um i think you know proof of stake has been on the horizon for miners for a long time they've they're aware of it um but the the issue is you know since it's been on the timeline for so long that many have just discounted it or they think it's never going to happen so um even if we started communicating these things uh that may or may not have an effect hopefully they um start to pay attention and can see that things are happening and uh specs are being released things like that we have test nets it's it's more than just a meme um and it's gonna happen sooner rather than later but yeah all throughout this year we've been telling people conservatively that mining was going to end at the end of the year obviously that's not the case but i think we we've started the communication process and i know some of the mining pools are also planning to participate in staking so they'll be communicating this again hopefully sooner rather than later to their uh constituent hash rate to make sure that they're aware of what's happening once we get closer to the merge and i i expect that they'll be doing their own sort of messaging and marketing um we're not going to be able to reach every minor but um as for what's going to happen between now and the merge possibly something to consider but we'll definitely continue at least what we've been doing which is regular and consistent messaging um going into the minor communities trying to make sure that they're aware that this is is imminent um

**Tim**

* and one thing i'll add to that is um a lot of people kind of don't upgrade until there's a blog post on ethereum.org so we're definitely gonna have that i think what we want probably before having that is just a much more kind of finalized specs and whatnot and um not only for miners but like given uh the kind of uniqueness of this upgrade which isn't the same as like previous upgrades where you just tell people download the new version and that's it um we're probably gonna have to be like much more thorough in explaining that and what should people do um not only for miners but like you know people that are running a validator people that are running in each one node and and and not mining uh so we're gonna need to just be pretty explicit to what all the different types of users need to do um i just think we want to be a bit farther along in the process uh before we have that so that people kind of uh so that the things we point people towards are are stable

**Trent**

* so miners we have discussed quite a bit the various attack factors that miners could launch against ethereum on the way out so as we approach the merge the incentives to be good citizens decreases um the way the merge is designed and the way the process will happen is designed specifically uh to deal with that like we could do the merge much simpler if we didn't have to deal with that and so um yes we have talked about it uh we believe that the way the terminal difficulty stuff is set up mitigates the biggest set of attack vectors with without you know going completely crazy and delaying the merge my other two years in engineering effort um we should actually have Mikhail talk about that he knows it better than i do

**Speaker 12**

* is he still here mikhail

**Mikhail Kalinin**

* yeah what do you want me to tell you

**Speaker 12**

* do you want to give a just a really short summary of what total terminal terminal difficulty is and yeah it's safe

**Mikhail Kalinin**

* yeah right terminal total difficulty is the trigger for the actual merge for the transition from the proof-of-work to proof-of-stake um and the question that often arises here is why we don't use the block number as in the regular hard forks in simple words uh the the fortress rule uh the fork choice rule handover uh between the proof-of-work and proof-of-stake is happening uh in at the point of transition and since the workforce rule is based on the total difficulty um it means that we need to to do this handover at a certain total difficulty because the block number um if we use a block number uh there could be a minority fork that is built and withheld by some adversary and is revealed later at the point of merge and this fork may has much less value much less solid difficulty value so it could be easier to to be to be built and it's possible the kind of minority fork attack and if we have a like suppose we have a also the adversarial uh leader or is it it could be the same party and this father the proposer of the first proof-of-stake block can take this minority fork and build a block on top of it and with respect to the block number block height rule everything will everything will be okay but with respect to the work contributed to this fork and yeah it will not be okay because it will be a minority of work and yeah not not the one that would be the canonical one in terms of total difficulty focus rule so that's why the terminal total difficulty is used to trigger the um yeah the actual transition yeah i think 104 lincoln um yeah there is also the original section in the [EIP-3675](https://eips.ethereum.org/EIPS/eip-3675).

**Trent**

* this may may impact um people in this call and the reason for that is because we're doing total sort of terminal total difficulty we can't pick a ttd terminal total difficulty until very close to time and so normally when we do hard forks we pick the hard fork block like a month ahead of time we say okay is going to be the hard fork block whenever we get there that's when the hard fork happens we hand wave when that is with terminal total difficulty because the difficulty can fluctuate quite a bit over time especially if miners start selling their hardware off early or something we can't advertise what the ttd is going to be early because it could end up that now we've gotta wait two years for us to actually reach that ttd uh when we meant to plan for like a month and so more than likely what's gonna happen is the clients will be released that have all the code for the merge in and then some placeholder ttd maybe and then when we're like a week away from when we want to actually run the merge we'll release we'll do two things one we'll announce what the actual ttd is and we'll release an updated client updated clients that include that ttd baked in also these the clients will have a mechanism for overriding the ttd so that way if you've already upgraded your infrastructure and everything when we release the clients like a month in advance you only have to change like one config option in order to use that new ttd that we're going to announce you know a week before the merge happens and so users can either choose to just upgrade their clients again for home users it's probably the easiest one whereas if you're running like some sort of infrastructure of your infrastructure provider and you want to do a bunch of testing against the clients you know as far in advance as possible and you probably don't want to upgrade a week before the merge in which case you can just change the config option the environment variable or cli option or config file or whatever the mechanism you use to configure your client and so that may impact people and again slightly different than our normal forking process and this is specifically to mitigate attacks against um the merge

**Speaker 12**

* yeah the beautiful thing about difficulty leading up to the merge you know trying to balance between minor our miners going to stay on the network or are they going to leave is that it's uh self-adjusting and that you know if if too many miners leave there'll be a ton of profit left leading up to the merge and it should auto balance uh should but um those those are kind of what we're thinking about and it seems like it should be should be all right leading up to the merge we are almost exactly at time tim do you have anything that we missed or wanted to cover

**Tim**

* so i don't i was going to say if people have questions or at least topics they'd want to cover on the next one of these if you can leave them on the [GitHub Issue](https://github.com/ethereum/pm/issues/402) like the agenda of this call that's really helpful i feel like it probably makes sense to have another one of those like a month from now um probably not two weeks but like a month ideally if we uh by then we we might not have like the Kintsugi devnets but we probably will have you know we'll probably be close enough to it to tell you what to expect and then uh if people you know have other questions we can just spend time entering those um but yeah this was really really valuable uh thanks for everyone who asked questions and showed up

**Trent**

* if someone wants to get invited to the next version iteration of this where should they follow or watch

**Tim**

* so trent can give you a calendar invite if that's what you're after if you don't want a calendar invite the ethernet discord and then the ethereum/pm repo um we'll have the information 

**Speaker 12**

* yeah and if you're part of a something like a web3 provider or something related to infrastructure in some way just give me your email and i will add you to the list of people that get this invite automatically but i do keep it scoped to just people who are working on infra because a public call could blossom pretty quickly into something much larger than it needs to be so we like to keep it small when they can be small uh and yeah it will be uploaded after the recording of this will be uploaded to the ef youtube um sabotage just dm me on discord or twitter and i can give you the link to the discord anything else last minute?

**Tim**

* a quick question would like a transcript of this call be useful to someone like is it worthwhile for us to just get some transcripts done?

**Speaker 12**

* yeah or at least uh at the very least a rough summary of the stuff that came up and that would be okay cool

**Tim**

* so we could yeah we'll okay we'll try and get like some notes for the call and at least so if people just want to follow that and not watch the whole video um that they can do that

**Speaker 12**

* great thanks everybody for showing up and participating in the discussions and uh we're all excited for the merge i know everybody has always been excited about the merge but you know it's real it's happening um it's going to be amazing all right thanks for coming everybody

## Attendees
- Tim
- Trent
- Mikhail Kalinin
- Marius
- Matt
- Ben
- Various

## Links discussed in the call (zoom chat)
- [EIP-3675](https://eips.ethereum.org/EIPS/eip-3675)
- [EIP-4399](https://eips.ethereum.org/EIPS/eip-4399)
- [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559)
- [EIP-3675](https://eips.ethereum.org/EIPS/eip-3675)

## Next Meeting
TBD