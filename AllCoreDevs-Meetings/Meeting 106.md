# All Core Devs Meeting 106
### Meeting Date/Time: Friday, Feb 19th, 2021 14:00 UTC
### Meeting Duration: 1 hour 30 min
### [Agenda](https://github.com/ethereum/pm/#acd-106-meeting-info)
### [Video of the meeting](https://www.youtube.com/watch?v=anrbnroO3dc)
### Moderator: Hudson Jameson
### Notes: Avishek Kumar
### Summary
## Decisions Made
| Decision Item | Description |
| ------------- | ----------- |
| **1**   | Pooja Ranjan will update Eth1.0 spec repo with progress on YOLO v3 provided by clients, removing Trinity from the mainnet client list. |      
| **2** | Estimated [Berlin blocks & timeline](https://github.com/ethereum/pm/issues/248#issuecomment-782069875)  Ropsten will be forked around March 10th |
| **3**   | Start discussing London EIP soon and get a consensus in the next 2-3 meetings. Pooja to share the list of EIPs for consideration in ACD Discord. EIP authors may create an issue at pm repo to add it to the next ACD meeting. |  
| **4**   | Eth1-Eth2 Merge team will produce more document for Eth1 client reference to describe what to be expected post merge |
| **5** | Difficulty bomb will be part of every upgrade till the Eth1-Eth2 merge. |
| **6** | Removing ‘refund’ can be targetted to London. Vitalik, Martin and whoever available may help create the EIP. |

---

 **Hudson** : All right hello everyone and welcome to Ethereum core developer meeting number 106. I'm your host Hudson and today we got a pretty full agenda so we can go ahead and get started on. the first one is the status of YOLO V3. James is out sick today so we'll have Tim taking over that as well as Pooja for any support for some of the timing questions under Berlin and then we'll talk about London. First let's do YOLO V3.

 It might also be people who are doing YOLO v3 stuff who has an update.

# YOLO v3 update

### Besu
**Rai**: Besu is synced to YOLO v3.
I still need to look into more detail about whether we want the RPC but I think we should.

**Hudson**:  cool.

### Open Ethereum 
**Dragan**: Same for Open Ethereum. We’re syncing, need to check on calls. 

### Nethermind
**Tomasz**: Nethermind is in sync.

**Hudson**: Great, what about the Geth team?

### Geth
**martin**: Geth is sailing YOLO v3. 
* Some issues surfaced but none related to consensus issues but peripheral. 
* Still working on the PR, will merge on the master soon. 
* work on fuzzing transaction on YOLO v3, looking good so far

**Hudson**: okay great anybody else have any YOLO V3 commentary before we  move on to Berlin timing 

**Pooja**:  For YOLO v3, Spec 1.0 repo is updated with every client's recent update. No update from Ethereum JS & Trinity.

**Martin**: **Trinity does not consider themselves as clients anymore.** 

**Danny**: They might use a component or true for the research stuff but not as a full mainnet client. 

**Hudson**:  yeah and then I can get you in touch with ethereum JS if needed we can see what they're doing back if they do want to be a 1.0 client I don't know where they're at.
Whether they are going to be a part of YOLO v3 or not though.

**Martin**: I might have further details, there are some tests for 2930, they are trying to stand a test repo. I found some problems with them. I am guessing none of the other clients have checked them out. So please do that, there is this PR on the test repo that has 2930 tests and these will require some change in the clients because obviously they have an access list in the transaction.  So yeah please check them out and see if you run into the same problems that I did.

**Hudson**: Thanks so much Martin thanks Pooja.

# Berlin 
**Hudson**:  Next up on the agenda we have Berlin timing we have the pm repo switch stuff now and it to go to the readme there's dropdowns for the agendas and then if you want to add something to an agenda for a specific meeting you make an issue so the issues from the read me or I guess there are agenda items in the readme, than the link to issues where you can have further discussion instead of one agenda issue where there's a lot of net mixmash discussion. This is another way to try and improve asynchronous communications. So thanks, I think Tim, Pooja & James did this, right or was it just Tim and Pooja?

**Pooja**: Tim

**Hudson**: Thanks Tim, this is working really well. I'm seeing a lot of good conversation and these issues and I'll pass it over to you to talk about Berlin timing if you click on the issue number 248 there's some charts and discussion in there.

**Tim**:  Sure, thanks Hudson, I shared the issue on the chat.
There are tons of conversations on blocks for Berlin & in the last call we said February 24th. That's obviously 5 days from now and it’s not going to happen.
Afri has a couple of proposals. There were some concerns with YOLO testnet timings. so I put a fourth proposal today. This is the [last comment](https://github.com/ethereum/pm/issues/248#issuecomment-782069875). 
It suggests all testnet forks separately. The first testnet Ropsten will be on March 10th. Every week you fork a testnet.





Ropsten - 
10 Mar 2021
Goerli - 
17 Mar 2021
Rinkeby - 
24 Mar 2021
Mainnet - 
14 Apr 2021



Open Ethereum will handle Kovan on their own post Berlin. 
And one thing that's worth noting also there's another issue, London. Because of the difficulty bomb will be going out sometime in July, we probably want to have more than a month or two between the two mainnet hardfork and so this scenario D gives us basically three months between mainnet on the two networks.  There might be less delay between the testnets but the mainnet upgrade would have a delay between Berlin and London.

The main blocker is clients thought on forking the first n/w in about three weeks. that means if we want a communicative property we probably need like a release out in the next week or so from all of the client teams which has the block numbers cuz that we can put a blogpost together to link the releases.

**Hudson**: Any comments on that, as far as the clients think of the dates or whether they think having roughly you said how long would they have to put a really sound like a week?

**Tim**:  So the first testnet would fork in 3 weeks, right? so it depends you know what the delay people are comfortable between the how you don't between putting out a release and having to Fork happen? I suspect about two weeks, is probably what we want at minimum. So people can upgrade. so that means if we have 3 weeks total it's basically one week that you know ship the new version and then two weeks to just communicate it.

**Martin**: yeah I think so in the first one is Ropsten. There are high chances of getting messy on Ropsten. However with the clique networks, it’s going to be nicer. 

**Tim**: Are you saying forking Rinkeby first?

**Martin**: No, I am just saying it’s going to be messy on Ropsten. 

**Tim**: Also, Ropsten has the most unpredictable block time whereas two other should be easy to predict.

**Peter**: One thing that we could do better this time, if every client would start up a small node. That’s kind of a personal request that each team please have some small miner running somewhere for a few days after the fork on Ropsten.

**Tim**: We can definitely do that.

**Martin**: Date wise, I don't mind these dates.

**Tim**: To be clear, this is like that last proposal right like so the first four scheduled for the 10th of March.

**Martin**: Yes

**Tim**: Does anyone have an issue with these dates? 

**Micah**: Sorry if I missed it,  but why  Ropsten first instead of Goreli & Rinkeby?

**Tim**:  It was because it was the most messy.

**Martin**: And also Goerli is closer to production.

**Peter**: yeah, the problem with Rinkeby is that it's more or less only Geth testnet. All clients can sync but have Geth signer only. It is not suited to find consensus issues. 

**Micah**: should we keep it in schedule like that?

**Peter**: Well no, the point really is that if anything goes wrong and you want to minimize the damage. If Gorily & Rinkeby are more production,  than if you fork all 3 on the same time and if something goes wrong then you just messed up 3 networks, whereas if you mess up Ropsten then at least you may minimise the risk with risk to only one Network. 

**Tim**: Another reason is in previous forks, I think we've wanted to have like somewhere you know four to six weeks on testnets you know so even if we remove Rinkeby from which you know if we don't have it for one week later for example I'm not sure we'd want to pull mainnet one week earlier. We might but historically we wanted to have 4-6 weeks before the mainnet goes live.

**Micah**: Sounds like a reasonable argument to me. 

**Peter**: One question, more like a rollout question. Let’s suppose that we pick these and we go with these numbers, the question is should clients hard code all the block numbers straight including mainnet or just hardcode the testnet block numbers and let's wait two more weeks for mainnet before telling everybody.

**Tim**: From just like communicating to the community point of view, I think having them all in one release is better because you don't run the risk of people who think they've upgraded the Berlin but they just upgraded to the Berlin testnets.  Although for folks like etherscan and exchanges, I suspect we can handle that nuance but I guess we're just general communications, it makes it easier to say it like this is the release for each client for Berlin, if there is  stronger reason of not having them all in a release is fine as well.

**Hudson**:  Right, if we were going to have it in two separate releases then we can just as easily if something goes wrong have that second released be some kind of well we're delaying things, we're taking out the block number over doing a different block number etcetera we could do that just as easily is for some reason having two separate ones just to be safe and not have mainnet number on there yet.

**Peter**: Okay

**Dragan**: For us having two release for the safety reasons are okay. It’s safe to download and you're okay but for being safe if something happens on the testnet, I would not like to share blocks for the mainnet there. But it is for the clients to decide.

**Tim**: I guess that we don't have anything we don't actually need. It might be the worst option if clients do stuff differently even though there is no rule that forces us all to agree but I think that will be the most confusing for the community to say you're good with OE, you are bad with Besu, You’re good with Besu, bad with Nethermind. 

**Micah**: I think, whether it's worth the risk of needing or not probably comes down to what we think of the probability of needing another client released before mainnet. If everybody thinks there is 99%chance of going with this release to the mainnet then it make sense to hardcode the block number. How do people think about their confidence?

**Martin**: One thing that we’ve done historically in Geth is to have a command line switch so the block can actually be moved or just disabled via command line. So if we put out client with specific block numbers, then the miners and people who run large infrastructure they don't have to pull a last-minute new updates just because the fork got pushed a week or something. they can just postpone at the bit with grand parameter, they don't have to redo the entire devops infrastructure setup. so that's such a pretty good thing to have in place.

**Dragan**:  then most of the clients are okay can start only one release?

**Hudson**:  Sounds like that's what it's coming to do we have any other client issues with having one release with all the block numbers?

**Tomasz**: Fine from our perspective 

**Hudson**: and Besu?

**Tim**: I've been pushing for it so I guess we can do that. I saw Afri proposed the block number on the testnet. We will probably want to have people review before making it official. 

**Hudson**: Let’s try to decide today, so that people can start prepping the release. 

**Tim**: The block number that Afri proposed
Ropsten 9_812_189 (10 Mar 2021)
Goerli 4_460_644 (17 Mar 2021)
Rinkeby 8_290_928 (24 Mar 2021)
Ethereum 12_244_000 (14 Apr 2021)
 
 These match up with the dates, we can have someone double check, did it make sense? 
**Micah**: is mainnet missing?
**Tim**: Yes, mainnet is missing.
**Hudson**: That one is harder to come up with because of variable block times I'm guessing is that right Afri, or is there a reason mainnet off there?
**Afri**: I'm just doing it in parallel. I can't do it right away.
**Tim**: He posted this 3 mins ago. 
**Hudson**: Way to the end of the call, we will bring it again, pending someone checking the math and then by the end of the day have a up or down on chat so that could be helpful right let's go ahead and do that any other final things on Berlin before we move on to London discussion? end of the call will have the numbers go over them one more time. I'll have someone check them and chat and then will approve it in chat today.
# [London](https://github.com/ethereum/pm/issues/245)
**Hudson**: Next up is London timing that's issue number 245 and Tim added that one to the agenda so go ahead Tim.
**Tim**: Just to make people aware. Because the difficulty bomb is going to hit sometime in July and in practice, it might hit a bit later because the hashrate has grown, but you know I don't think we want to make that into our basic assumptions. The difficulty bomb goes on the mainnet around July so we probably want London to go live on mainnet around July with an EIP to push back the difficulty bomb, there is already one written - [EIP-3238](https://eips.ethereum.org/EIPS/eip-3238). Ideally we would want more than just Muir Glacier Part 2 fork for London. So that means if you want that actually choose test EIPs and have a proper roll out, we need testnets to happen in sometimes in late May early June. In early May we need to have a blocks chosen for those testnets and most of the testing done. Basically the equivalent to today for Berlin. 
July: Mainnet
June: Testnets
May: Blocks chosen, London testing done
April: Select final EIPs + Reference Testing + Wrap up ephemeral network testing
March: Select initial EIPs + Start ephemeral network testing
There is no canonical list of EIPs for London yet and we're already in late Feb, so I suspect in call one or two we need to come to a decision on which EIPs we want to see in London. I just wanted to put that out there because it seems far away then when you can I go backwards from there it means like the next two calls is when we need to decide what goes in.
 
**Hudson**: unless there's something catastrophic with Berlin that we would need to figure out during the call which allow that would be async anyway then we can focus on the merge and London EIP is the next two meetings with the idea, right Tim?
**Tim**: Yeah exactly like I think it would make sense for either next call to be focused on EIPs for Berlin, and  at the very least choose what are the big things that go in. I am bised with 1559 but I know there are other big one that are ready. I suspect because of this short timeline, we won;t be able to do multiple big EIPs. It would be useful to choose big EIPs and add smaller simple EIPs also. 
**Artem**: We don't need to rush any EIPs because f the difficulty bomb. Why do we need to rush it for July?
**Tim**:  so I guess that's what I am saying. if we want anything more than the difficulty bomb for July then we need to make the decision about that in the next one or two calls. It’s fine if we don’t want anything aside from the difficulty bomb, it’s fine. But we can’t start in May and be like oh s*** we want this EIP in because there just won't be enough time to test it properly.
**Hudson**: And there might be some EIP that people are just working on that people might decide in a meeting or two.
**Vitalik**: it's worth mentioning that I think the safe margin for the next Fork might also be a little bit after July. you basically of the hashrate like ones out by about a factor of 2 since I know I don't know I think those calculations are done because of the price Rises.
**Tim**:  yeah because July could be the worst case scenario. I guess it doesn't change that much. maybe instead of the next two calls we need to like we have the next 3-4 calls to decide.  so it still has to happen quite soon.
**Pooja**: Just for quick reference, when we were deciding about Berlin, and before that Istanbul, we have some EIPs that were in almost ready condition but they were not considered because of one or the other factor. They are listed here in the Eth1.0 spec repo, in the project board, but what we are looking for is the clarity like 1559 and difficulty bomb. There are some EIPs already proposed indicating they are interested to be considered for the next upgrade but clients have to make decisions on the EIPs list. 
**Hudson**: Where should people propose, create a new issue maybe at pm repo?
**Pooja**: It’s in the [Eth1.0 spec](https://github.com/ethereum/eth1.0-specs/issues) repo. People have already indicated their willingness, we need to know the readiness with the London timeline. 
**Hudson**: So we want a list of EIPs specific to London.
**Tim**: So one thing that we can do here is that if people want that to be considered for London upgrade, they can open an issue and we can add it to the next agenda or the one after that and have like I don't know maybe the next two calls kind of focused on entire call but the next two calls focused on potential EIPs for London.
 
**Pooja**: I may have a fair list of those that I will be happy to bring it for further discussion.
**Hudson**: Wonderful if you do have a list of that and you make that list somewhere where other people can add to it or comment on it just post that in the ACD chat and then we can try to start to ask around to the EIP authors if EIP is ready and should be included on that list or not?
**Pooja**: Sure.
**Hudson**: Thanks a lot Pooja for that, any other comments on London timing or getting EIPs decided on the next month or so?
**Lightclient**:  is it completely out of the question to try and put it in place of difficulty bomb out another two to three months in Berlin that way we're not forking on top of ourselves?
**Hudson**:  Probably at this point too late but I mean not impossible that's what my guess would be,  client devs?
**Peter**: Let’s not go there. the thing if we want to push out difficulty bomb, somebody needs to do some rough calculation which is more meaningful than somebody else needs to check that calculation. Ideally, somebody needs to write up the test just to make sure it works for all clients behave the same way and it needs to be deployed on Ropsten in 3 weeks. So if there would be an already done precalculation everything done with EIP, and the it’s like hey included this 3 lines of codes that could probably work but if we start thinking about it now, then we probably won't; nobody will bring it up sooner than the end of next week. And that’s in my opinion be late.
**Hudson**: I think, this is a good opportunity for us to start on a faster cadence for hard forks as well, just kind of dip our toe in the water with trying to do one within a three month or three and a half period. To try to get more out during the year instead of once a year and if we find out that that's a bad idea we can change it to.
**Tim**: To be clear also we're not doing the hard fork in three months right like we're doing the hard fork in like five six months and they'll just end up hitting mainnet three months apart right. 
**Hudson**: Yeah, that’s what I meant.
**Afri**: just for the record, there is an EIP for difficulty bom that could be used for any of the hardforks, it’s 3238.
**Hudson**:  Okay thanks.  though that's just for difficulty bomb delay in general and we would just tweak it with whatever numbers are effectively what were using is that what you're saying?
**Afri**: Number really doesn’t matter when be activate it because it's just (?) a particular block number, right?
 
**hudson**: Oh Yeah, that’s right. anybody else have comments? thanks everyone.
# [Eth1-Eth2 Merge Requirements Overview](https://github.com/ethereum/pm/issues/247)
 
**Hudson**: We have Danny,Mikhail Kalinin and Guillaume as well as Vitalik and other people from the Eth2 team who can kind of give us some information on the merge and I'll let Danny kind of talk about the purpose of this portion of the agenda and then have you all go through it.
**Danny**:  yeah I'll give a little bit of context and then turned over to others I just shared the link to the issue and I just shared another link to the recent on my workshop a few weeks ago in which Mikhail and Guillaume presented on their work for past 6+ months. up until this point there's been more of like a smaller working group working on what does Eth1 look like in the context of the Beacon chain consensus. And from a specification standpoint it's a essentially, moving the POW and adding POS and keeping the application layer same. There are a number of minor changes that have to be addressed. But, things largely can remain stable. From a s/w standpoint what really what has been created over the past couple of years is a Eth2 client is POS consensus mechanism and that can be coupled in the upper layer and that's been demoed with Teku & Geth with utelizing Eth1 client is going to be application layer. so in addition to the actual consensus spec there are these Eth1-Eth2 communication protocol back which allows in Eth one client application there to be driven by a to client by Eth2 clients consensus layer. that is an opinionated way to build a merge plan, you can also go to merge client without that info specs likely will not have a reference that that implementation detail but because we do have many Eth one client application layer client and we have many Eth2 clients likely this kind of modular approach is a really a way to go. There are many things to think through, especially when it gets to the edges like what if they think look like in then out of these pieces all put together but now is definitely the time to turn this working group or open discussion things to all core devs, maybe set up a monthly call from here and dig in and refine specs. I think a different chain is actually utilizing the Teku plus Geth merge client today for production testnet and claiming they're going to go to the mainnet with it soon. That’s cool, maybe somebody will do it before us and we could learn from them. That’s high level context. there is a merge room in the Eth R&D Discord. we might end up making a subcategory and have some subchannels now the conversation happen more and I'll turn it over to Mikhail and Guillaume who will go through some of the more technical things here and a hackMD document with Eth2 side with specifications of going to go into the spec repo very soon. there's also a kind of conversation you need to have one of them talk to some EIP editors about how the unification of the specs might look. obviously we have POS consensus component , we have Eth1 application layer scattered about EIPs . We kind of have to think about how these specification will look in  the coming weeks and months. 
**Mikhail**: So thanks for the introduction,Danny. I just have a question do you want to go into discussion into detail? how much time do you have now?

**Hudson**:  I would say, let me look real quick at what time we have left you know how much time do we want for removing evm features?  who put that on there?

**Vitalik**:  I put it on there. I definitely don’t want to take haf the call. 

**Hudson**: Would 15 or 20 mins be okay?

**Vitalik**: Okay

**Hudson**: Okay go till 15-20 past the hour, how about that,  merge people?

**Mikhail**: Okay, I have time, thank you. Danny just described almost everything but we can go into the details. For the Ethereum clients that we have them now, a lot of stuff like JSON RPC will remain the same, just a few adjustments. but most of them remains same that means the dapp developers and user infrastructure built around it will also mostly stay the same. the evm will is it is going to be featured with new Opcodes that will allow for applications to read the Beacon State the read the new consensus. one of the use cases is to implement the withdrawals from and the Validator withdrawals from the Ethereum accounts. according to the most recent proposal beacon block will contain the application Payload which consists of user transaction state root and receipt and the means that the parts of the network and stag that is responsible for the blocks sync is going to be deprecated and also Consensus swap means that Ethash and other verification that are related to are also going to be deprecated and that might be some big change in terms of inner structures of the current ethereum clients. Probably Guilluame can give more details on that.  a couple of things more here to mention is a few breaking change, the change that might break the current applications like one of them is the around the block hash. the problem here is that the book hashes with used as the source of random on one hand and on the other hand it's probably also use the applications to work by block headers. so removing the proof of work it means that the source of Randomness is going to be broken it's just that the walk without the proof of work will become malleable and easy to manipulate to roll the dice and just exploited by the block producers. The other thing that is going to be broken is what Peter mentioned in the workshop is the currency of full nodes or in the full history of the blocks in the network. it doesn't mean that nobody will store the history anymore the full history but that just means that the history is not necessarily needed for the consensus purposes and it could be not stored by the consensus nodes. 

**Danny**: In other words, that is a nice thing that falls out of some of those things with finality weeks utility stuff and so like to see user experience of being able to prune is available. obviously from like a strong default from even like sampling node and kind of rejecting peer nodes, you don't have the full history.  you could still induce that as a load requirement but it's definitely something that we should examine here. It’s an opportunity to potentially change the load requirement. 

**Peter**:  I think there's a very very important question that needs to decide here and  this  drives the whole discussion. In the current model, Eth2 clients feeds the blocks to Eth1 clients.  that kind of means that all the block synchronization and propagation is delegated to Eth2 n/w.  if we go down this path, we as Eth1 client will not be able to retrieve history. We can only do what the Eth2 clients permit us to do. From a short perspective, it is a completely acceptable thing to do that the blocks are pruned after finality but from an Eth1-Eth2 merge perspective, I think, it would need some serious thoughts as that would mean that we lose the history. And I am not sure if we can afford to do that just out of the box.  so that's a bit of a steep change and the reason I'm saying it's important to figure this one out because Eth2 clients will be very very heavily pruned and they don’t want to maintain chain and in that case if we want Eth1 client on the merge shard  to still be able to synchronize the chain that we probably need Eth1 clients to retain the chain and be able to swap it between each others which means we can not just delegate how block synchronization to Eth2. **so that's a big design question**.

**Danny**: I agree this is what it like moving parts of the things to decided on there and one thing to note though I mean at least there are number that kind of expected changes at this point of merge and so you could potentially change certain guarantees, especially good point to consider whether some of the guarantees can be changed. I’d argue it's very very very unlikely that blocks would be lost they might be lost in the context of the P2P network but I don't suspect that the blocks would be lost forever. yeah I agree they're certainly watching through some of these more nuance points. 

**Peter**: My point really is, the goal with the merge is to make sure that the Eth1 n/w continues to lives within the Eth2 and there is no funky Eth2 Classic fork and then essentially you don't want to break too many existing users experience things.
If we launch new shards with EVM, I think it's time to break everything for Eth1 shards, that's a big? Another thing from a technical perspective, I do want to emphasize that Eth1 clients with a ton of work into this whole block synchronization and I don't want to be little Eth2 client but they haven't really been battle tested yet. if we were to just drop a 300 Gig chain on Eth2 client I don't know how well they will perform. So let’s try not to delete too much stuff before we prove that the alternative is liable. 

**Danny**: I’ve a question about the effect of user experiences being able to sync the chain from Genesis rather than starting somewhere in the middle and I'm getting a state via some sort of state thing, is that is the primary user experience reconstructing it an archive node? What are the other UX inspirations there?

**Peter**:  My personal thing that I think that people want is access past transactions, past blocks, past receipts. it's not necessarily about re- running the transactions thinking about having the transactions available.

**Dragan**: I’ve a question about Clarity.  Peter said that the block from Eth2 is going to be fed to Eth1 client. Is that all the blocks or just the newly created blocks that created for that particular client? How is the new block going to be distributed to Eth1 clients

**Danny**:  So in the current designs post merge the Eth1 application payload is embedded in the beacon block. The beacon block is like the primary influences objects in Eth2 and so in that beacon block application layer stuff which is the user transactions and some other data as well as the consensus layer thing. From the perspective of Eth2, Eth2 is building the chain core consensus beacon chain. The idea is that the Eth2 client already manages just like beacon block for Network where about the number for these things are being passed around. when I receive the New Block, part of that block has an application layer payload, Eth1 payload and I use the adjunct Eth1 software next to me to verify that component and that  I can verify the other consensus component.  from the perspective of Eth1 POC, adjunct Eth1 client is the driver, kind of like how does the small like that the POW module is kind of the driver of the Eth1 client today or the clique module and it said this would be like Eth2 module which is the adjunct piece of software. Does that answer your question, you need to follow up on that?

**Dragan**: Does it mean the block distribution is done in Eth2 client? 

**Danny**: Correct. That would be post merge, so like the prior to the merge you don't really have to take out or containers that’s driving things but the post merge.

**Dragan**: Yeah.

**Danny**:  And if you look at that that Eth1-Eth2 communication protocol it's unidirectional currently because it's kind of like the Eth2 is like the brain and the driver of the consensus and mix request to the Eth1 clients. Similarly, like when you're constructing a block there's a request like give me the application layer payload.

**Dragan**: Make sense, thank you!

**Hudson**: so continuing on it, was at the end of it or was there more commentary?

**Danny**:  what we got to that juicy item at the end, I guarantee of storing the entire Block history. 

**Vitalik**: Is there anything to talk about in terms of process of actually doing merge, actually how are we doing merge transition works?

**Danny**: Well for one it's probably the most likely point in the Ethereum history for a POW attack.

**Micah**:  What is the attack Vector? Let’s say all the miners decide they want to prevent POW or ruit our day. What’s the worst they can do?

**Vitalik**: Realistically, to say that they’d wants to try to break consensus on which state route gets said to be agreed on as the Genesis State Route out of Eth1 as of subsystem of Eth2. 

**Micah**: Keep re-mining the last block over and over again?

**Vitalik**: yeah, they can keep on making as many changes as flag height.

**Danny**: it depends on the fork choice mechanism. If you have PoS transition happens at a certain proof of work block height, then one attack would be all miners turn off all their nodes, you never go to that height that's not like a great attack attack, it probably also not a very realistic attack. but if you have the choice being on the PoW block, and you get a little bit more power to the miners. whereas if you, you know if it's been set on a slot time on a slot height than the trigger happen.

**Vitalik**: My preference would be the choice should be on the POS side like we should just modify Eth2 data voting so that you could also vote on the flag.

**Danny**: Even if you don't have a pre vote once the slot height is triggered and you have the state route embedded in the or some sort of previous pointer embedded in the POS block, you are getting vote by an attestation at that point. You do get a native voting mechanism once you move over. There could be certain rules that allow what is a correct state root there. 

From a Eth1-Eth2 merge perspective,  Stop are running together it would be a potentially at a time but will there be a trigger at which point the Eth1 client was listening to The proof of work and next one is listening to the PoS RPC  and so that could be a blockhead trigger, that could be a slot trigger that could be voting trigger but at that point the combo software would then be listening to the Eth2 driver. if you weren't running a combo s/w, and you continue to listen to the Pow, then you’re out of the chain.

**Ansgar**: Wouldn’t there ideas atleas to incentivise the empty dummy chain for like at least a couple days after the merge, just to exactly prevent this?

**Vitalik**: Yeah that's definitely a reasonable idea.

**Tim**:  But that occurs at the cost of downtime, right?

**Vitalik**: No, it would come at the cost of someone providing those rewards. so the idea would be a like after the flag height, some organization, provide let’s say 2 ETH per block to miners who mines a couple of thousands of empty block after the flag height. From an application & usage point of view, no one will care about those blocks like that would just be there as a kind of tail of the chain. 

**Danny**: A lot of options, here.

**Hudson**:  interesting okay and are these enumerated in the documents that are listed in the issue that you linked in the chat?

**Danny**: Not entirely,  or I think they're probably pretty light on that actual point of the merge. There's a lot to enumerate all the things that need to be done one thing that Tim & I would like to do after this call is to enumerate things that need to be done. One thing that we haven't talked about is convincing ourselves and convincing the others that Beacon chain is the safe home for Ethereum for the application layer, there’s a number of different things you probably want to do with respect to Benchmark testing and many things. 

**Vitalik**: I think the general idea that we’re focusing on making sure that we have the post-merge behavior spec’ed out as a somewhat higher priority than specifying the merge process and there is couple of reasons for this
It would actually provide more opportunity to test what happens after and 
now there is just give ourselves the opportunity to do a fast emergency merge, if we have to. It just  give us the capability to do that as quickly as possible.

**Danny**: Right, so accompanied with any version of specs that I think we want to have like an emergency version which would shut down certain features for example like you could remove validator withdrawals from beacon chain back in the application layer in the event of the emergency.

**Vitalik**: The **emergency merge** would just say that spec would contain a slot that contain a state root. And everyone will just agree to that state root and they keep going from there.

**Danny**:  there's really no recourse from a 51% attack on work other than changing the proof of work algorithm or doing a POS.

**Ansgar**:  Maybe just mention that briefly and I think I agree with Vitalik that the kind of specing out the endstate, the goal state is more important than the spacing out the merge process. To briefly mention,  one open question as well that's just how can we kind of make execution around the point of the merge as smooth as possible? Ideally we don't want to have the chain hole, even like a short one. Ideally from a user perspective, we want the transition process not even noticeable, see if we can get there.

**Vitalik**: I'm sorry I was just saying there are definitely ways to make the merge that has a very short or close to 0 downtime. 

**Micah**: so we did this Phase 0, are there any other changes that we could make it to partially introduce without going all the way to phase 1.5 is there any intermediate step between right now and 1.5 that we could do?

**Vitalik**: One step that could be taken to modify the Eth1 client so that they watch the Eth1  voting in the POS chain as a kind of canonical marker of like what is a finalize Eth1 block. Basically reduce 51% miner attack risk by a bit. Though, I don’t think it would reduce the complexity of the merge process. 

**Danny**: yeah so I mean if you do that you end up with something that looks like EIP 1011 which was the Hybrid PoS mechanism, that is finalizing a POW block reward mechanism and in terms of  the history and contexts that would have taken Eth1 block and added an additional like validator Pos payload what has happened instead as there's now a proof of stake block and there will be added an application-layer payload, the Eth1 payload. the ultimate result is very similar with different paths.

**Danny**: i was just thinking in terms of how can we reduce reduce risk and make people more confident before we do the big merge. The more things we can do with small stuff will lower the risk. 

**Vitalik**: Agree and I think one big risk lower is just getting the **post merge spec working** and probably just I'm just running them on the testnets just a couple of times.

**Danny**: Figuring out what we are going to do is the most important thing, so that we can do it. 

**Tim**: and just go back to the previous conversation about London, is there anything you suspect that we need to include in London are related to the merge?

**Danny**:  I think, the BLS is the nice thing to the application layer. It is used very natively in PoS but ultimately it does not affect the beacon chain consensus. It’s not requisit, but very nice to have. 

**Mikhail**: One of the ideas was also to use the difficulty bomb for point of merge. 

**Danny**:  **Timing the extension of the difficulty bomb** on our estimate on when the merges is valuable to consider. 

**Tim**: I think and Afri might correct me here I think Afri’s EIP times it for summer 2022 to so basically 18 months from now roughly.

**Ansgar**:  but I do feel like because it's expectations we shouldn't end up making be like to stress that it can be variable in both directions, right? I think it would be unfair for miners for not having at least some period of time for the heads up,  I mean unless there's some conflict or something and I guess we were to communicate now that it's like summer of next year and then all of a sudden it's like December of this year something.

**Dankrad**: What’s stops us from being able to do it in around one year?  I feel like one and a half years is like too much.

**Vitalik**: I’d say it’s like compensating for the planning fallacy.  like we definitely should not commit ourselves to a path that forces us to either get it done within some fixed time frame or have incredibly huge problems, but we should also and not close the doors to doing it as well because it definitely is possible.

**Danny**: yeah I mean there's only the number of people that have that need to touch the things that has not been so I think some of those that have been touching it have something in mind but there's a lot more work.

**Dankrad**: Right, I would just rather plan for the one year timeline and see when there is a problem then push back rather than 1.5 year timeline. 

**Danny**: My guess is this is not the right time to set the timeline but hopefully soon we can do that. 

**Tim**: we can push the difficulty bomb more than one time. If the difficulty bomb is going to  pushback 18 months from now maybe we can make that be like 12 months instead and then push it back again so it's like you know I'm not saying that this is a timeline that we need to use for the merge but it's like right to difficulty bomb to go off soon and we push it the opposite.

**Vitalik**: One thing we could you could do is we could even just say old difficulty Bomb extensions from now on for only 6 months and then it just becomes a part of each hardfork.

**Dankrad**: Yeah I would be in favor of that.

**Hudson**: Nice idea. 

**Tim**: This is something that we could discuss on the next call. What do we want? A difficulty bomb for London?

**Hudson**:  Real quick, Vitalik did you say earlier that the price of ether kind of affects the upcoming difficulty bomb and that it might delay it?

**Vitalik**:  basically what happens, the way the difficulty bomb works it increases the difficulty in every block  by a number and that number goes up exponentially and so if the difficulty of the chain itself goes higher then the increase needed for the bomb to be substantial also goes up and so the time until the increase that goes up higher. If the hashrate until the difficulty doubles, then, that gives us another one hundred thousand blocks, which is about 16 days.

**Danny**: In relation to the price, as the price increases, more miners join in. 

**Vitalik**: One thing to keep in mind that there is good chance of the difficulty is going to keep going up from where it is now even if price stays to constantly decreases somewhat, the reason is because the difficulty is the lagging indicator.

**Hudson**: It’s the moon math meaning if we goes up with the price, it goes up.

**Vitalik**: Correct.

**Hudson**: For the Eth2 talk, was the plan originally to also have Eth2 on here next week to kind of go through some more updates.

**Danny**: I'm kind of here and there a few times but I will be prioritizing this anytime people want to talk about it on this call and offline. Definitely we want to produce a little bit more documentation on all the things that we need to have happen and talk about that and maybe once that's produced and disseminated we might bring it back into the call talk about that. I also think that it's probably makes sense to do at least a monthly more in-depth sync on the different call and we will talk about scheduling that relatively soon.

**Hudson**: Where can people go to talk about this async?

**Danny**: on the Eth R&D Discord does have a merge room right now that is under Eth2  research I think as I mentioned earlier we might make it a subcategory for the merge and after we've been merged some of the subtopics for the address so we can talk about things in more granular fashion. 

**Hudson**: Just announce that in the core dev chat when that happens and then we have Micah and Peter who had comments. so Micah if you want to go first with whatever you're going to say we have three to five minutes on this topic left about.

**Micah**: Sure, it would be great to have a specific documentation that explicitly says this is the minimal amount of work that Eth1 client needs to do for the merge. Because, I know Eth1 client team are very lazy so that they don’t have to go over everything, just one the core piece instead of, just learn this, that would be helpful.

**Danny**:  Yeah and Guillaume can probably help with some of that documentation and it will be evolving to think about state things but will likely have a version of that really soon. 

 **Hudson**: Okay and Peter?

**Peter**:  So my personal request is that I think a lot of decisions evolve around what we want the final chain to look like.  so I think it would be super helpful if he would have some form of documentation of the say at the sea-which would say that post merge how will Eth1 chain look like?  meaning what variance does it have, what blocks does it have, do we want to support or we don’t want to support historical stuff etc. ? In my opinion it is a golden opportunity to just delete a lot of junk that's been accumulated so by all means I'm in favor of trying to simplify and trying to throw out things but before we start working on that solution it is essential to understand that yes this is the model we're going with and they're searching for a solution for that specific issue.

**Danny**: Okay. We may not necessarily write the answers to those are but we can write down what questions are and may be right some began to come or some answers to solutions. 

**Hudson**: Okay, that sounds very promising, do we have any final words on the Eth2, anything with the merge?

**Guillaume**: I have one comment, we're looking for users for contracts that are writing using the instructions difficulty and block hash to do something else that generates randomness, so if you really depend on those on those instructions it would be nice that you got in touch with us.

**Hudson**:  Great and it when you say get in touch with you how they get in touch with you?

**Guillaume**: With Danny, I guess.

**Hudson**: Maybe Eth R&D Discord ?

**Danny**: Yeah.

**Hudson**: Okay.

We move onto item number 5.

# [Backwards-incompatibly changing and/or removing EVM features](https://github.com/ethereum/pm/issues/250)

**Hudson** Vitalik take it away, we have about 14 minutes until the meeting is over and we need one minute for an announcement so 13 mins.

**Vitalik**: Okay! Basically, the time before the merge presents this opportunity that's probably a much better opportunity than anything will ever have after the merge onto a kind of do a cleanup of Ethereum features that were probably introduced with not that good a reason and that it makes sense to either remove or backward in compatible changes in certain ways. The reasons that have to do this are either it's just to simplify the spec or sometimes just to introduce some new variance but make it easier to do things in the future. 

So btw, lightclient asked why the merge is the best time time to do these changes? To be clear, I am saying either the merge or before the merge. the reason why either of those two periods are better than after the merge is basically because any clients that gets developed after the merge could potentially end up like I'm losing the ability to process Ethereum pre-emergent Ethereum history and so it would be able to not need to ever have the codes for processed nodes, which is good for codes simplification. I put in a couple of examples into that [document](https://hackmd.io/@HWeNw8hNRimMm2m2GH56Cw/evm_feature_removing). One of them is the  self destruct offcode, you can follow along the doc. the self-destruct opcode was originally added as a cleanup feature but they just ended up completely failing at as you think that objective and the self destruct offcode is actually quite terrible because it does break some very important invariance that we like. for example is just that it allows you to just send ETH to the address as well without actually calling them and other really important one is that self destruct only because of self destruct there is no upper balance on the number of State objects that can be modified in one single block right like a contract with a million no State objects can self-destruct yourself and this is potentially really nasty. Because it really restricts of the ways that we can change the way we can store the state in the future. Binary tree & Verkle tree are potential other kinds of accumulators that we haven’t vetted yet. If we have a variat that say there is a maximum of 5000m objects that can change within a Block then it  become as much easier to say the state of being a single wait structure and if we treat the state of a single layer structure it just makes it much easier to Implement a new ways of storing it better abstractions for how we deal with the states in the west room for bugs and all of these things.
 and I see another couple of examples in there have to do with side of gas absorbability. We already talked about it many time. Removing the ability to make call for a partial amount of gas is that the big one and the reason why that might be good to remove, basically in order to make future changes to gas costs.
 so those are probably they are the two basic categories and I saw there are some other changes as well like things like getting rid of call code. I encourage everyone to  read the document, I have more arguments in there why I think it would be a good idea to remove a couple of things and some of the ways in which we could mitigate the consequences to it's applications as much as possible. It’s also like a reason why you take it's good to just get it to start so I can do this early and start talking about this explicitly. It is good to just give application developers a maximum amount of lead time. so that they can be sure that they're not dependent upon  any of any of these things and to be clear it is a very small percentage of users. This lists things in EVM that would be worth changing, removing or simplifying. Of course in addition to this there's also non-EVM thing. We already talked abou the block # a bit.  backwards incompatibility changing the way,. how introspection works but it's still ultimately a good idea but it's like its important to talk exclusively about it so people depending on that can move as early as possible.

**Hudson**: Any comments on that?

**Martin**: yes so it'll break some things. I’m wondering  how you see there are cases of ether which will become stuck with Self destruct disappears?

**Vitalik**: My expectation is that the amount of ETH is probably low enough that we can probably organize a community funds to compensate people if there is any really serious cases. Micah suggests a one-time hard fork to rescue the stuck ETH

**Hudson**: Micah is that a suggestion?

**Micah**: Sorry

**Martin**: Yeah I heard another question which is refund. We discussed that fairly recently. Removing those would be great and will be awesome.  I am also wondering can we do that in next fork? 

**vitalik**: **We could**. Removing refund is the least risky of any of these items in my proposal. It does have benefits. Some people concerned about EIP-1559 increasing block size variance. But if you remove refund, then refunds currently are another big source of block size variance. Like  right, now we already have with refunds you could already have watch that contain up to 25 million executed gas and so if we were moving at the same time that could address people's concerns. 

**Peter Szilagyi**: So,  I would vote for refunds going out together with 1559. I mean getting rid of refunds go hand-in-hand for 1559, I preferably target it for London.

**Danny**: I agree.

**Tim**: is there an EIP . I assume there is no EIP for getting rid of refund yet, rights? So just your document Vitalik?

**Vitalik**: correct there is not eip for any of these things.

**Tim**: If that’s one you think can make it into London, I think if we could have an EIP for the next call or to one after that would be really good.

**Hudson**: That would be really nice.

**Micah**: One problem with 2929, there will be some contract potentially, that would no longer execute.

**Vitalik**: In this particular case, actually no. the reason why is that refunds only apply after all the execution is over,  The worst that can happen is if something becomes places expensive.

**Martin**: But it should be noted by for anyone interested, if refunds goes away, then gas tokens will become useless and worthless so and I don't know how much money is tied up in Gas token right now.

**Micah**: About 50 mil USD.

**peter**: I think one is at 4 and the other one is at 12.

**Martin**: Good that we talked about it openly,  so people can start getting out of it and burn it.

**Hudson**: So for the gas token thing, they have a website and I think it listed in your doc
Vitalic; it says that the website says there's no guarantee that there won't be changes in the future to make this obsolete. He would absolutely put a big warning on the side if we ask him,  I think about it .

**Martin**: I think there is the big warning about it. They say that the loophole will be fixed in the future.

**Danny**: I think, they expected loophole to be in public and then to be fixed much sooner. 

**Hudson**:  I actually I was about to ask about one inch chai and GST too, does that use the same mechanism? do we know?

**martin**: No idea.

**Hudson**: Trent & Tomasz said it does. 

**Tomasz**: Some of them are using SELFDISTRUCT and some of them are using refund so they're trying to find an optimization somewhat to brings back the most costs.

**Peter**: But essentially, both of them are based on refunds on getting something back. 

**Tomasz**: Yes.

**Ansgar**: A quick question, I am not an expert, how close 2x block size could get to us today because I would expect that once we can have a fixed date at which those become usable. People will rush to and that might give us some period to sustain larger blocks. Is that a potential issue?

**Peter**:  I think we already have it. I don’t think it’s an issue. It's better if they use it up then if they get angry at us for not giving them the heads up.

**Ansgar**: Make sense. If at all, a long advance warning. 

**Hudson**: Yeah, we can do some outreach.

**Martin**: That’s why I tried to highlight it right now.

**Hudson**: I’ll start getting the word out, I don’t know how many people watch these meetings, actually. Only a 148 right now but will tell more people.
There's about one minute left of the meeting so let's real quick, who is going to **make the EIP for some of the stuff that was just discussed including the refund mechanism**? It could be multiple people assisting on it at the same time.

**Vitalik**:  I'm happy to help.

**Hudson**: Okay, so Vitalik and that anyone who wants to help reach out to Vitalik anyone who has updates to.

**Martin**: I can.

**Hudson**: Thanks Martin. For this list that Vitalik made, talk to Eth R&D Discord and find a place to talk about it I think we have a bunch of chat rooms in there that would work.

# [Ethereum 1559 community call](https://github.com/ethereum/pm/issues/251)


**Hudson**: And for the last-minute Pooja will be announcing the stakeholder call that  we have coming up. Go ahead Pooja

**Pooja**:  So, Ethereum cat Herders are hosting an EIP-1559 community call inviting all the stakeholders of the Ethereum community. this is basically to address any and all my kind of concerns with the proposal. we are having a panelists, list includes EIP Champion, researcher, developers and all the details are available in the blog. the call is planned on Friday 26th February, would be moderated by Hudson Jameson, and the live stream link is provided in the agenda.

**Hudson**: Thanks Pooja and yeah just to be clear we are addressing some concerns in there but there's nothing cordev meeting related about it. it's going to be a lot of people airing out their concerns and getting information and just having kind of a discussion more so than any kind of this is going into a fork this is being decided on nothing like that's happening this is completely separate from the core devs calls and run by the Ethereum cat herders so just to be clear nothing no substantial decisions will be made from that call it'll just be an opportunity for discussion.

**Tim**:  One thing that's likely to come out of it is you know miners are obviously unhappy about 1559 because they loose their fees, they are proposing different alternatives - fight against ASICs, raising the block rewards. one thing I hope is that they can kind of  align on one and you know that if they want to propose that on all core devs, they are free to do. 
I don't know but yeah I think that's one of the things I'm expecting to get out of the call is a sort of concrete about that proposal. We won’t take a decision about the proposal there but that’s likely the come out of it. Then all core devs can consider whether or not
 (a) whether they want to do 1559 which is still not included and
 (b) if we do it whether or not there's one of those proposals that makes it in alongside 1559.

**Hudson**: Pooja Do you have anything final?

**Pooja**:  Just wanted to let people know that we’ve this Reddit post to collect questions that will be shared with the panelist to get answers. 

**hudson**:  alright thank you all so much for coming to this the next meeting is going to be on March 5th 2021 at 1400 UTC that's a Friday thanks everybody for coming out and I will see you then bye !

-------------------------------------------
## Attendees
- Arif Schoe
- Hudson Jameson
- MIkhail Kalinin
- Trent Van Epps
- Tim Beiko
- Danny
- Danno Ferrin
- Pooja Ranjan
- Karim Agha
- SasaWebUp
- Artem Vorotnikov
- Tomasz Stanczak
- Micah Zoltu
-Vitalik
- Jochen
- Dragan Rakta
- Alex B. (Axic)
- Paul D.
- Rai Sur
- Martin Holst Swende
- Lightclient
- Alex Vlasov
- Lakshman Sankar
- Peter Szilagyi
- Gerg Colvin
---------------------------------------
## Next Meeting
March 5th, 2021 @ 1400 UTC

