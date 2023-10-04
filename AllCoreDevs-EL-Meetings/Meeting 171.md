
# Execution Layer Meeting 171 <!-- omit in toc --> 

### Meeting Date/Time: September 28, 2023, 14:00-15:30 UTC <!-- omit in toc --> 
### Meeting Duration: 90 Mins <!-- omit in toc --> 
### [GitHub Agenda](https://github.com/ethereum/pm/issues/867) <!-- omit in toc --> 
### [AudioVideo of the Meeting](https://www.youtube.com/watch?v=CPt3f3ughFM) <!-- omit in toc --> 
#### Moderator: Tim Beiko <!-- omit in toc --> 
### Notes: Avishek Kumar <!-- omit in toc --> 

---------------------------------------------------------------------------------
 ## Agenda

 ## Dencun Updates
 
**Tim Beiko** [1:23](https://www.youtube.com/watch?v=CPt3f3ughFM&t=83s): Thank youand we are live. Welcome everyone to EL call number 171. So today obviously the discussing dencun. We can talk about devnets to start and then we have the different audits that have come in for 4788. We have some of the Auditors on the call. I'm not sure if all three firms are on the call but I think we have either a copy of the report or someone from every one of the auditing firms so we can go over the results there. Then I understand Holesky relaunch today and so we can get a status update on that. And after that there were two other topics people want to discuss so one is a new EIP 7503. And then Guillaume and Danno had some discussion points around self-destruct Behavior after a verkle trials are implemented. Yes I guess maybe to kick it off Barnabas you posted this spec for Ddevnet 9 do you want to maybe give us a high level overview of where things are at with regards to devnet?

 ### [Devnet-9](https://notes.ethereum.org/@ethpandaops/dencun-devnet-9)

**Barnabas Busa** [2:48](https://www.youtube.com/watch?v=CPt3f3ughFM&t=168s): Yeah sure! So I have prepared all the different images already for Devnet 9. Based on the feedback that the different client teams have given us. and we should be pretty much good to go hopefully tomorrow. But we are still hoping that we can get some more years to pass some more Hive tests. So the general idea is to have about 1300 validators for this test with a split of 75% for nethermind, 18.8% for Brazilion Aragon, 3.7% for ethereum JS and 1.8% for RF.


**Tim Beiko** [3:30](https://www.youtube.com/watch?v=CPt3f3ughFM&t=210s): Yes you only have the specific client teams want to comment on where they're at.


**Marek** [3:38](https://www.youtube.com/watch?v=CPt3f3ughFM&t=218s):  So I can start I think we are ready and a few failing tests on the hivecancun page is mostly testing setup issue and we are talking with Mario just to fix it and that's it no we don't see serious issue.


**Tim Beiko** [3:59](https://www.youtube.com/watch?v=CPt3f3ughFM&t=239s): Got it nice.


**Paritosh** [4:05](https://www.youtube.com/watch?v=CPt3f3ughFM&t=245s): Just one other point. So devnet 9 we're doing the updated address for 788 so that's the one that we'd be using on mainnet as well. And we'd be doing the manual deployment which is also the approach we use for mainnet. The only open question is what do we do about the trusted setup file? Ddo we continue using the one we've used in the past or is there an updated trusted setup file?


**Carl Beek** [4:33](https://www.youtube.com/watch?v=CPt3f3ughFM&t=273s): File so the setup file is not updated yet.


**Paritosh** [4:38](https://www.youtube.com/watch?v=CPt3f3ughFM&t=278s): Okay then we'll continue using the previous one and then we'll do Devnet 9 and possibly a future devnet can use the new just set up there.


**Carl Beek** [4:47](https://www.youtube.com/watch?v=CPt3f3ughFM&t=287s): That's good.


**Barnabas Busa** [4:49](https://www.youtube.com/watch?v=CPt3f3ughFM&t=289s): One more quick note we probably will need to have Devnet 10 also to test out each churn limit change where we can actually spin up. You know 350 to like 40000 Validators. And then see if the churn limit change is actually working for all the different CS but that is expected to be a much shorter lived devnet.

**Paritosh** [5:20](https://www.youtube.com/watch?v=CPt3f3ughFM&t=320s): And one one more Point following that one the MEV workflow works with the mock Builder now we've tested 4 of the 5 CL’s and it works fine. Which means if we would like to start pushing for everyone to have map workflows and ideally in devnet 9 / devnet 10 also test Builders and relays. So if you have a builder a relay please reach out and we'd like to get you set up.

**Barnabas Busa** [5:52](https://www.youtube.com/watch?v=CPt3f3ughFM&t=352s): And one more a quick note that we're going to be deprecating the Bellatrix  Genesis. So from now on devnet9 and any future devnet and testnet will
probably use capella Genesis.

**Tim Beiko** [6:15](https://www.youtube.com/watch?v=CPt3f3ughFM&t=375s): Got it one quick question before Mario so you mentioned the validator churn limit  so that and the blob base fee. Are they implemented in clients for devnet9  I recall that was what we had agreed on.

**Danny** [6:33](https://www.youtube.com/watch?v=CPt3f3ughFM&t=393s): Yeah it's just that the the noticeability of that churn limit cap is not going to be hit until a certain validator thresholds. There's logic there but you're not going to hit that code path. 

**Tim Beiko** [6:45](https://www.youtube.com/watch?v=CPt3f3ughFM&t=405s): Got it.

**Danny** [6:52](https://www.youtube.com/watch?v=CPt3f3ughFM&t=412s):You know this is a configuration variable so we could change it to be lower. But I'm also fine with doing a big test that uses mainnet configuration.


**Barnabas Busa** [7:03](https://www.youtube.com/watch?v=CPt3f3ughFM&t=423s): Yeah I would not do anything lower than four. So that's why I said we would need at least 360000 Validators for big bigger tests because you also don't want to run a you know 400000 Validators test for multiple weeks that  devnet 9 is supposed to live. 


**Tim Beiko** [7:22](https://www.youtube.com/watch?v=CPt3f3ughFM&t=442s): So cool got it so because the number of validators hired and just having a short run once devnet 9 is stable to make sure we hit those code paths and everything works is the plan. 


**Barnabas Busa** [7:34](https://www.youtube.com/watch?v=CPt3f3ughFM&t=454s): Yep my phone's about right.


**Paritosh** [7:37](https://www.youtube.com/watch?v=CPt3f3ughFM&t=457s): And we'll be testing it with holeskey anyway. So eventually we'll be testing it with a bigger set. 



**Tim Beiko** [7:44](https://www.youtube.com/watch?v=CPt3f3ughFM&t=464s): Right got it. Sweet Mario Vega you had your hand up a couple minutes ago I don't know.


**Mario Vega** [7:56](https://www.youtube.com/watch?v=CPt3f3ughFM&t=476s): Just a couple comments. So on the side of the tests running on the hivecancun. Some of the errors might be that we bumped up the parallelism on the test execution. So we're lowering it down so probably we'll see more passing tests from the clients later today. And another comment is that I think at least one of the clients has not updated their the address for typical route. So I'm passing it over the chat so make sure that you have this address for all the tests and for devnet 9 too.


**Tim Beiko** [8:35](https://www.youtube.com/watch?v=CPt3f3ughFM&t=515s): Got it. Did any of the other client teams want to share progress updates or blockers or anything with regards to the devnets.


**Lightclient** [8:52](https://www.youtube.com/watch?v=CPt3f3ughFM&t=532s): I can say that we're passing a lot of the hive tests tests now I think we've gotten it down to about 10 or 11 of the hiveCancun ones that we're not passing and most of them are pretty small Edge case things like you know what happens if you try and send some of the Cancun data objects in an old method like fork Choice V2 or new payload V2 and just trying to find the best way to implement these changes. I think the only notable thing is that we still haven't added the code path to actually propagate blob transactions on the P2P. So we have the a lot of pool to keep track of the Blob tx's. If they're submitted directly to us via an RPC but right now we're not sharing them on the P2P with our peers.


**Tim Beiko** [9:46](https://www.youtube.com/watch?v=CPt3f3ughFM&t=586s): Got it I'm curious. Do other clients have peer-to-peer that's working for Block transactions? Okay so nethermind in ref have it.


**Andrew Ashikhmin** [10:07](https://www.youtube.com/watch?v=CPt3f3ughFM&t=607s): But sorry I'm a bit confused I think in the EIP says that gossip is not allowed like or there should be no gossip for Block transactions. But if it should be in the cash announcement but not in Gossip but maybe I'm missing. 


**Lightclient** [10:32](https://www.youtube.com/watch?v=CPt3f3ughFM&t=632s): But we're not announcing them at all.




**Andrew Ashikhmin** [10:36](https://www.youtube.com/watch?v=CPt3f3ughFM&t=636s): Yeah we have a different code path  transaction fetching.


**Ligthclient** [10:40](https://www.youtube.com/watch?v=CPt3f3ughFM&t=640s): And that just hasn't been connected with the Blob pool. So it's not really aware when transactions are submitted to the Blob pool to share with its peers.


**Gajinder** [10:52](https://www.youtube.com/watch?v=CPt3f3ughFM&t=652s): I think EDH 629 should have their gossip announcements right?


**Tim Beiko** [11:09](https://www.youtube.com/watch?v=CPt3f3ughFM&t=669s): Yeah I'm not sure if this specific number, but okay, so get does it have that. Yeah Andrew does Aragon have the announcement?


**Andrew Ashikhmin** [11:25](https://www.youtube.com/watch?v=CPt3f3ughFM&t=685s): I think we will have them okay. You can double check.


**Tim Beiko** [11:33](https://www.youtube.com/watch?v=CPt3f3ughFM&t=693s): But yeah we should and I guess on the on the EL side besides some


**Peter** [11:41](https://www.youtube.com/watch?v=CPt3f3ughFM&t=701s): One moment but Matt you said that cat doesn't have it. Are you sure I don't really see a reason why we wouldn't announce?


**Lightclient** [11:50](https://www.youtube.com/watch?v=CPt3f3ughFM&t=710s): Yeah there's a Channel That's not um hooked between the blob pool and the transaction fetcher so we don't really push anywhere that we've received a new transaction in the blob pool.


**Peter** [12:09](https://www.youtube.com/watch?v=CPt3f3ughFM&t=729s): At the transaction fetcher is not relevant when announcing transactions.


**Lightclient** [12:16](https://www.youtube.com/watch?v=CPt3f3ughFM&t=736s): Or the ETH Handler sorry.


**Peter** [12:21](https://www.youtube.com/watch?v=CPt3f3ughFM&t=741s): Yeah anyway I have to look into this it's a bit weird.


**Lightclient** [12:25](https://www.youtube.com/watch?v=CPt3f3ughFM&t=745s): We're if it is connected then it's failing the Hive test for propagating the transaction. So we can look more into that but when I looked at it there's the transaction announcement Channel and it's just not hooked into the blob pool right now.


**Maurius** [12:47](https://www.youtube.com/watch?v=CPt3f3ughFM&t=767s): Are we not working the other way around that you're subscribing to the transaction announcements?


**Tim Beiko** [13:06](https://www.youtube.com/watch?v=CPt3f3ughFM&t=786s): Okay I guess maybe you all can figure this out offline. But I just like to check broadly so blob gossiping. And then you know there's a few failing hive tests for it seems like most of the EL clients. Are there any other sort of big blockers or big chunk of work left on any of the EL clients?




**Marcin Sobczak** [13:33](https://www.youtube.com/watch?v=CPt3f3ughFM&t=813s):Yes so one week ago I did an experiment with sending high amount of block transactions with only six Block in transaction. And like devnet 8 were not healthy on the under such high load and in Nethermind, we had a bug in broadcaster. We are sometimes requesting transactions which we already have in blob pool. So after fixing it like the condition of our notes were way better. But there is still some work to be done on building blocks well. And there is a high amount of block transactions in the pool but it's definitely not a blocker it's optimization.


**Tim Beiko** [14:36](https://www.youtube.com/watch?v=CPt3f3ughFM&t=876s): Got it thanks. Any other team have blockers or just optimizations or things that they're working on they want to share?


**Fabio Di Fabio** [14:54](https://www.youtube.com/watch?v=CPt3f3ughFM&t=894s): So for Basil regarding the blob transaction, we still have to apply some optimization. Now it's possible to crash the node if you send too many blob transactions because the limits are not yet in place for that kind of transaction. On the other way I was following some rescue notes. So I'm not sure if before you were talking about transaction broadcast is broadcasting also blob transaction. 


**Tim Beiko** [15:34](https://www.youtube.com/watch?v=CPt3f3ughFM&t=934s): Got it. Thanks. I think that's most of this CL or EL team sorry if anyone else has anything you want to share and folks on the CL side have updates I want to share as well feel free to.


**Gajinder** [15:58](https://www.youtube.com/watch?v=CPt3f3ughFM&t=958s): PMGS also gossips develop transactions.


**Tim Beiko** [16:03](https://www.youtube.com/watch?v=CPt3f3ughFM&t=963s): Got it. 
Okay so I guess then if we have devnet 9 going live hopefully tomorrow or you know maybe early next week. We can see how the different clients  work on it. And then yeah it probably makes sense to test the cloud transaction gossip code paths on it. And yeah hopefully have things stable then run another another one on another devnets with a high validator account for the churn limit. And then start moving to testnets once things are stabilized does that seem reasonable to people. And yeah we can follow up either next week or the week after once we have a bit more data on how the devnet 9 tests went. To figure out next steps. But it seems like we're in the final stages of just polishing everything and getting it ready anything else on the devnets. 

### 4788 audits review

okay next up then so we had three audits done for the smart contract that's part of 4788. So I linked 2 of them in the chat sorry in the agenda here and then the third report we expect to have tomorrow. But I believe we have folks from most of these teams on the call. So is anyone from chain Security on?


**Hubert (Chain Security)** [17:57](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1077s): Hi yeah, this Hubert from Chain Securty. 


**Tim Beiko** [17:58](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1078s): Do you want to give a quick just overview of your report the audit in general and sort of any thoughts you have on on the contract?


  - Chainsecurity


**Hubert** [18:07](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1087s): Yeah sure! So yeah I guess super quick recap but most are aware. So EIP 4788 will introduce this smart contract that will store the beacon roots where only the system address is allowed to set Beacon routes. And anyone can otherwise query. So the primary refining of our report was that the you could query the zero timestamp and would get back a zero hash as long as the slot for the zero hash was still uninitialized which in a in the original version of the code would have taken a long time to initialize. Because of how it was set up. But that directly brings me to the secondary finding in our report. Where we suggested that the size of the two ring buffers so we have ring buffers for the timestamps that of the corresponding Beacon roots. And the beacon through Roots themselves. So we suggested that the ring buffer sizes become prime numbers. So that the storage ones are the storage size of the contract is more predictable. Even when the block interval might change in the future. Yeah that being said, I mean I'm happy to talk more about how what we did a bunch of tests. And even some form of verification but like I guess to conclude the most interesting Insight that we had towards the end now. Based on the updated review where we reviewed what the prime buffer ring size means is that the really the property because the original EIP said that Beacon route should be held for 24 hours. So the real property that the contract has at the moment is that Beacon routes will be held for 8191 seconds at least. Because so as long as the block interval doesn't change then everything is fine. And every Beacon route will only be overwritten after let's say 8000 blocks. But the moment the block interval changes for this time period like where the change happens this property doesn't hold anymore. So we just want to point out that in this somehow very tight transition time you only have let's say two hours guaranteed history of Beacon routes. So yeah um I would say these are our primary findings. But yeah sorry I hope this wasn't too quick but Team linked our report in the chat Https://chainsecurity.com/security-audit/eip-4788-contract/ . So obviously feel free to read the whole thing or ask questions now or directly again.


**Tim Beiko** [21:13](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1273s): Thanks. Yeah we'll see if there's other Auditors on the call and sort of get everyone to go through their findings. And then we can do questions to everyone after that. I don't know if there's anyone from Trail of bits on the call. I don't think there is. So I link the reports of PDF it's not published on their website yet but I linked it in the agenda. If people want to check it out.

  - Dedaub

And then last we had Dedaub also do an audit and I believe they have someone on the call and we expect the report to be out tomorrow.


**Sifis Lagouvardos** [21:49](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1309s): Yes hello. So essentially our find it similar to the previous one. So the only let's say real finding was that the zero timestamp can be quite successfully. And according to our analysis with the block time it would never be overwritten. but that was my reason it was sold. And then the other thing we did is we how does an exercise what would happen if the block times were to change. And we resulted into advisory items. Basically that the storage footprint would change for different parameters or even possible block time parameters. And that some stale values would remain stored but again with the changes this is resolved as well. Now we have reviewed the changes but we just haven't updated the report. So it will be up in the same link again and we'll update it tomorrow now in terms of methodology. What we mostly did we use the we inspected the code in different representations using like from the assemblers to our own the compiler and binary lifter to get to see how it works here. So that's all if there are any questions? We have to answer also Mikhaill the bonus on the call here with me. He also worked on the audit. 


**Tim Beiko** [23:40](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1420s): So Marius has a question in the chat about push3. Do you wanna give more context of that Maurius?


**Maurius** [23:49](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1429s): Yeah in the updated code we use push3 to push a constant that is only two bytes long from here. But yeah it's not a big deal. It's just like I was wondering if someone else got this as well.


**Hubert** [24:14](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1454s): Yeah we noted this in our updated report 24:18 yes but I'm not sure if it's relevant enough for a change. But we noted this in our report.


**Maurius** [24:29](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1469s): It's not relevant enough I think I would say for changing it now.

**Sifis Lagouvardos** [24:39](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1479s):  Yeah we didn't see that.


**Tim Beiko** [24:45](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1485s): Are there any other questions? Okay so we'll have obviously all three reports people can review them. And bring up questions if there's any in subsequent calls. But I think at this point we're pretty confident in the changes in the final version of the bytecode. It's anyone have anything to add or questions concerns? 


**Hubert** [25:16](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1516s): Yeah just maybe one quick addition. I know this is not necessarily the target audience here but indirectly it might be. So it might be useful to push to Smart project developers the info that when you're querying for a timestamp x you're not getting the beacon route from time x you're getting the beacon route that was inserted at time x but originates from an earlier timestamp. I think that will otherwise lead to likely  implementation issues.


**Tim Beiko** [25:52](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1552s): Right good point. Okay anything else on the 4788 contract?


**Lightclient** [26:08](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1568s): Just wanted to say thanks a lot for all the Auditors who took time to look through this. And all the people who we didn't engage directly who took a chance to look through it and all the client teams who updated the address 54 or 5 times. 


**Tim Beiko** [26:23](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1583s): And also yeah special thank you to the Auditors who looked we were a bit late in sending the updated commits around so appreciate the quick turnaround  for the additional review.

## Holesky launch

Okay then next step we had a Holeski relaunched this morning. I'm not sure Barnabas /  Pari who's the right person to give a high level update.

**Barnabas Busa** [26:53](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1613s): Yep, we had the lunch this morning. We had the first epochs a bit struggling but since then vaidators came online. And now we are finalizing with about 78% to 80% participation. We are still trying to get as many validator groups online as possible. And hopefully we are going to be closer to 90% by the end of today.

**Tim Beiko** [27:20](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1640s): And is there like 20- 30% missing validators that are like struggling to keep up or is it just people who forgot about the launch and are not online at all. 

**Barnabas Busa** [27:32](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1652s): There was a bug with vouch and prison and because of that we saw a bigger group being offline. And also some people just run a lot more validators than a smaller machine which caused some performance issues and missed proposals. So but it's slowly getting there.

**Tim Beiko** [27:58](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1678s): Nice anyone else have thoughts comments questions about the launch. As of all congrats on getting it live. And then, you have some nice graphs that we can all retweet nice.

## [EIP-7503](https://eips.ethereum.org/EIPS/eip-7503) Overview

Okay then moving on. So we had two EIP’s or at least one EIP and one sort of modification to discuss. So first up we have some folks on the call who want to introduce EIP 7503 which it's called zero knowledge wormholes and enables minting secretly burnt if directly on L1. Yah I forget who was the author but if you want to speak up when I was here.

**Tim Beiko** [28:59](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1739s): Yeah we are here and hi Tim Beiko. And my friend now trying to share him a slides and introduce the whole idea and the whole EIP.  Keyvan? R u online?

**Keyvan** [29:12](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1752s): Yeah can you guys hear me?

**Tim Beiko** [29:15](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1755s): Yes we can hear you both. 

**Keyvan** [29:18](https://www.youtube.com/watch?v=CPt3f3ughFM&t=1758s): Sounds good. So let me share my screen. Do you have my we see the slides? Perfect. So okay thanks guys for having me here. I am Keyvan, a member of nobitex labs and I've been researching on privacy solutions that are based on Zero-knowledge proofs in the past few months. And recently we have found a new privacy solution that we found interesting. And it's the topic of this presentation you have name did Zero- knowledge wormholes. And we have made an EIP for it which is EIP - 7503. It's currently in the draft stage but you can check it out if you want so yeah let's get deeper. So if I want to describe it in a single sentence it's a proposal that is proposing ethereum L1 clients to enable remitting of ethers that are secretly burnt. And so before going further we first have to define what is a Parent Ether. So Ethers are burnt if they are in addresses that are not Expendable. As you know there are two kinds of addresses in
ethereum blockchain there are externally owned that cons under smart contracts and both of them are derived from getting the keccak hash of something. So in case of externally owned accounts you get the keccak of a public key and you just cut the first 20 bytes of it. And in case of a smart contrast you get the keccak of the combination of the deployer address and its icons nonce and then you just get the first 20 bytes. And we Define Unspendable Addresses. So an address is Unspendable if there exists no private Keys such that keccak of its public key is equal with the account address or there exists No Address and nonce pair which is Keccak is equal with with the accounts address. And so if we send the ethereum to an address that is definitely random and not a result of like getting a keccak of public key or something like that the
the address the phones in that address are burnt because you can't suspend them anymore. And the reason this happens comes back to the fact hash functions are a preimage resistance and which means that it is invisible to find an X such that the keccak of X is equal with some arbitrary value.  And so if you know that some phone has been sent to an address that is definitely random you know that the phones are burnt. And so the question is how can one convey confidently know that someone else has burned his ethers. We can have an interactive vertical be let someone else to choose the random bytes for us. And he gives the random bytes to us and we send our ethers to add that address. And then we can be sure that like those phones are not Expendable anymore. And so this is kind of an interactive protocol and yeah this was a meme I found a bit ago on Twitter which I found funny it says like cryptographers use this Fiat-Shamir	 heuristic trick in order to turn interactive protocols into non-interactive versions of them. And yeah we can use some an idea like that here too we can use hash functions are as sources of  Randomness. So in case of a non-interactive protocol one can choose a preimage r and send his ethers to Hash (r) like the 21st of hash ( r ). And yeah the hash function the use should be something other than keccak it could be like I don't know Shot 2 or  some ZK friendly hash function like MIMC or Poseidon or something like that. So I will generate this preimage r and I give it to you as a proof that the address I have sent my ethers to is indeed random. Because it is very hard to find the private key, the public key is equal with hash of something. And the next trick is that using the help of zkSNARKs we can hide the
value of this preimage R and imagine that in our ethereum clients we are recording all of the ethereum transfers that are happening in a giant Merkle-tree sparse Merkle-tree to be specific. And using the help of zkSNARKs, I can prove that an ethereum transfer has happened which has burned some amount of ethereum. But I won't show which transfer was it. And yes so the whole idea behind the EIP-7503 is that let's build a new kind of transaction in ethereum that allows us to Mint ethereum. When someone actually provides such a proof that some amount of ethers have been burned. And the beauty of this method and the reason it is better than other cryptocurrency mixers is that it gives you a bigger anonymity set we we can somehow say that all of the icons that have not transferred anything yet are included in the anonymity set and as the sender you can always deny that you have ever used this protocol which is very good for you as as a sender. And here I have like an implementation proposal of how something like this can be implemented on Twitter implants.So we can have a like something like an event handler in our code that is called whenever and ETH transfer happens it could be a transfer that is happening as a result of a function called in a smart contract. So we gather all of the ETH transfers in a single function. And we put the hash of the destination address and the value that is being transferred in a ZK- friendly Sparse-merkle- tree. And then we should have a new transaction type which we call it the mint transaction which means some amount of ether in case on like someone proves that he knows that preimage or their h ( h (r ) combined with amount) exists in the miracleRoot of the merkle tree we were maintaining. And we can also have a nullifier to like prevent double spendings very similar to cash style mixers. So that that was the basic idea and this could have like some extra
features like we can allow people to merge and split their nullifiers to bring some unique private utxo model on ethereum whenever someone migrates his  phones into this private anonymity pool. And in case we are able to split our coins we will be able to spend only a portion of our money. Like we can burn 10 ethers and only spend one ether something like that. And we can like instead of  using hash functions we can like do elliptical multiplications and this will allow us to like have Stealths burn-addresses. Like someone will give me a burn-address and people can like someone can publicly provide a burnt address. And we can drive other parent addresses which are expendable by the master parent address holder and they can have like stealths addresses. Andwe can also obfuscate the amounts. In case people transfer their ethereum in the pool. And as an extra feature of the cap we can also have proof of innocency. And there is also implication if we Implement such a thing in ethereum and it's about scalability. And so the thing is the centralized exchange usually like gather the user response into their hot /cold wallets from time to time by making a lot of transactions. So they will give different users different addresses. And after some time they will like move all of these phones into single a single letters which is like a huge source of transaction traffic on ethereum blockchain and imagine we are able to pre-mint our multiple Burns in a single proof imagine like there is an exchange that gives burn addresses to its users. And it's able to generate a proof like proving that 1000 Burns have happened and the sum of those parents is like 100 ethers. And remains them in a single transaction. This will save a lot of space and using this solution we will only store a single nullifier value instead of a whole transaction with a giant signature on our database. And that's it thank you if you have any questions? We are happy to answer.

**Tim Beiko** [41:37](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2497s):  Thanks for sharing. Yeah so there was one question in the chat asking you about how would you track the ETH Supply under this scheme would it still be possible to just track the total Supply.

**Keyvan** [41:52](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2512s): Yes absolutely. There is Supply in this case like you can get the total Supply by subtracting the amount that has been minted from the total ethereums in all of the ethereum accounts.

**Tim Beiko** [42:15](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2535s): So you're able to track how much has been reminted. And so if you look at the balance of every account which includes the burns account and you would remove it, however was minted in a new Mint transaction that gives you the circulating supplies all right.

**Keyvan** [42:32](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2552s): Yeah exactly.

**Tim Beiko** [42:33](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2553s): Got it. Any other questions thoughts?

**Guillaume** [42:48](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2568s): Yeah quick question so you're putting everything in a merkle tree. Why do you bother doing this because if you can make your a snark proof that zkSanrk proof that you burnt like that you sent funds to a to a burnt address? Why would you incur the extra issue that is plaguing tornado cash for example to that you're pulled with potentially other criminal transactions. And therefore you would become immediately suspicious of by using this system.

**Keyvan** [43:29](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2609s): Yeah the point is as the sender you can always deny that you have been in this protocol so you are safe but as the receiver your phones may be like fact or something like that. And the reason we are using a merkle trees because we want to hide the addresses that are actually like burn addresses.

**Tim Beiko** [44:02](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2642s): This is another question in the chats that's asking can't you deploy a contract to an unspendable address with create two.

**Hamid Bateni** [44:11](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2651s): Not yet but we are working on it and this we can't find any solution for doing that but we're working on it.

**Ahmand Bitar** [44:22](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2662s): No sorry the question is the opposite. Is that this should not be possible because if you can deploy a contract on the unspendable address or the burn address would be a problem. So if you use create two you create two does not depend on the deployer's address and Nonce. It depends on other factors like the contract's codes.

**Hamid Bateni** [44:48](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2688s): I got it let's say in this way. We can prevent this event with using the random number and providing the proof with that in the r circuit. And we can prevent this event using and deploying a contract on the same address with using the Creator. because the Creator using some sort of parameter and I can't put these parameters in my circuit to prevent this event. But what if we can do some sort of thing if we can find a way to doing some this way we don't need the protocol change. And we can do the hour mixer in the contract Level. But I don't think so there is an easy easy way to find this approach. If we find it we can do it on the contrast level not to protocol.

**Guillaume** [45:44](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2744s): How do you guarantee that you're circuit is going to have a random number?

**Keyvan** [45:54](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2754s): Yes I think the thing is it is very almost impossible to find the appropriate parameters for generating your contract address that is equal for example the MIMC of some random number. I don't think this is possible
it's I mean a hash function that is not Keccak is a source of Randomness in our case and you can just easily found the find the parameters that are used for generating contract addresses that will result in an address that is exactly equal with the output of our other hash function.

**Hamid Bateni** [46:56](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2816s): We're using the hash function as a source of randomness.

**Danny** [47:01](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2821s): And the input to the hash function is given by the protocol like randow or the state route or something.

**Keyvan** [47:07](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2827s): And no the user can actually pick anything.

**Guillaume** [47:14](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2834s): Right so they could pick something that they like exactly. Therefore you cannot prove that this address has been burnt.

**Keyvan** [47:30](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2850s): Yeah you will need your preimage value in order to prove that this address is a burn address. Because if you lose your preimage then no one can like be
convinced that this address is really a burn address and not the result of like hashing public-Key for example.

**Guillaume** [45:54](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2754s): Right if your preimage is not shared because you said it's part of your private witness right so it's not shared. So how do I prove to you that my number was indeed random?

**Keyvan** [48:09](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2889s): Yes so you do the hash function, you do the hashing in the circuit and you like your argument is that so there is a transaction that has happened in the previous works that have sent some ethers to an address that is that is actually the output of like zk -friendly hash function and not a Keccak. If you prove that the address is the output of like a ZK- friendly hash function then people can be convinced that these addresses indeed random and by that they can be sure that there is a very very low probability that people can spend the money in that address. But the transaction itself and the address itself is hidden. No one can  know that which address is the burn address. But they will definitely know that one of the addresses is a burn address something like that.

**Hamid Bateni** [49:20](https://www.youtube.com/watch?v=CPt3f3ughFM&t=2960s): Exactly in the whole network view no one can see or understand what his address is the parent address or a normal address. But let's see we just need to find a point on the elliptic curve that we don't know the private key and we should provide the proof we don't know the private key. And for doing that we can do it simply get a random number on the curve and multiply it ETHs with the hash of our premium h Hash of our privat key. And we can provide a proof with our circuit for doing this and finding a null random point on the curve we don't know the privat key. 

**Ahmad Bitar** [50:12](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3012s): So like what you need is to prove that this address is can never be produced from acute check hash can you prove that?

**Keyvan** [50:22](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3022s): Yeah

**Ahmad Bitar** [50:25](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3025s): From any Keccak Hash, not only from like deployer plus nonce cash from any Keccak Hash.

**Keyvan** [50:34](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3034s):  Yeah exactly actually let me write something in the chat so it is very fine.

**Hamid Bateni** [50:43](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3043s): You are talking about the Collision? 

**Keyvan** [50:49](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3049s): 
50:49 the argument is that you can find the preimage ( x ) for a keccak hash that is equal with a preimage (y ) applied on another hash function this is impossible to do.

**Guillaume** [51:07](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3067s): Right that's actually my other question so you want to build the transaction that would mint token that is based on the premise that Poseidon is trustworthy. My understanding is that currently it's not or at least it's not been used enough in the field that we trusted. So we should consider it as non-trustworthy for the time being. And assuming we're right to consider it not trustworthy that means it would be possible to find a preimage and therefore to Mint tokens.

**Danny** [51:43](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3103s): But I mean the the construction is sound if you just use if you use shot 256 or something like yes we can debate the hash function and which hash functions you know are safe versus optimal but the construction is safe if you have a safe hash function.

**Keyvan** [52:00](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3120s): Any Hash function link 256 folks too but it will make the circuit bigger and it will take more time to generate such as your knowledge proof. 

**David** [52:14](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3134s): 
So the ZK friendly hash functions basically there's like Mimsy Poseidon a few others and even these that are the most used are very relatively well Unknown. Their properties they're kind of new and this technology is you know being experimented with multiple L2s and other privacy pools. But we've seen inflation bugs in Aztec privacy pools different versions of tornado cash. We saw one in Z cash that we don't actually know if it was used or not.  So the issues with introducing like relatively untested versions of privacy pools whether it's this construction or others have inherently huge risk. And I would argue that we don't gain much by putting it in the base layer. Now we stand to potentially lose the credibility of all ethereum and the ability to say like how much ethereum actually there actually is which would be detrimental. I'm a huge advocate for privacy. I think there's a lot of reasons for it but to be honest we still have Solutions whether it be an L2s or other mixing contracts where people can get these sort of functions when they need them that don't bring the same inherent risk to the base layer. And I guess what I would like to know is like all constructions and technical details aside what is the argument for bringing this into the base layer now versus leaving it in L2s and other things.

**Keyvan** [53:45](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3225s): Yes so the whole advantage of such a thing compared to other privacy Solutions is that like. There are no smart contract interactions as the sender. So that is some kind of a new thing people like considering it's very large anonymity set.

**David** [54:15](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3255s): I think that we have sufficient anonymity sets for this purpose. I mean we do make some so we have to like kind of give up some things like we have to have fixed size pools right now. Otherwise we have to trust newer technology like Nova but for what it's worth like from the security side. And I've probably I'm not an expert but I spent the last 8 months kind of collecting ZK bugs. And looking at various bugs and we've seen inflation in double spin bugs in almost every some version of almost every single major mixing technology. And so I would argue that like long term maybe this is something like this is where we do want to go for various reasons especially like a pre-compile making this cheap that would be really great. But short term I would advise against using these hash functions that are not like relatively tested to other hash functions have. You know 20 years of testing and and we're starting to see collisions in them and we have a better understanding of like where we're at there but like circuits themselves I would advocate in being cautious of adding these directly into the base layer. And I think the only other EIPs that we've even considered using ZK proofs for are still relatively simple versions of things. And we're you know we're hesitant to even go there, that's just my two cents. I think it's about like a win, maybe not so much an if and I think that testing the technology significantly more and finding the right construction and stuff. It sounds like there's still some dispute about the construction itself.

**Tim Beiko** [55:57](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3357s): Yeah and I think just also to be super clear. I didn't want to bring this up today in the context of like dude. We do this in the next hard Forge but it's more like is this something we can start to get people thinking about. And obviously you know the first path the the easiest way to get something like this use is you could imagine it being deployed unlike an EVM equivalent L2 right. Then running that for a couple years and having you know significant funds use it. And you know, like building confidence over time because obviously there's been many cases of ZK bugs and it's all still quite new.

**David** [56:42](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3402s): Yeah I definitely think that's a good path forward. um one thing I will say is that if you look at ethereum and you trust the way it works right now and you say like okay ethereum works if you know keccak works if BLS signatures work if like we're saying there's not like some serious bug in the base layer and if we did add this. We would be adding circuits. We would be adding dependencies on a ZK friendly hash function. And other things that we don't have yet and that is a big leap. And there's you know in Bogota there was like some discussion about like when would you be okay zking the entire EVM in the base layer. And there's you know benefits for that and I think like the general answer at least that I was like the school of mine that I almost never there's some benefits to having transparency at the base layer. Because you can count the total Supply. If if there's you know full privacy in an L2 and there is a serious bug or there is some issue with circuits you know ZK technology has been around in in theory since the 70s but in application for like five years at a larger scale and maybe eight beyond that. And we would be basically opening  ourselves up to that like right now. If there is an inflation bug or if a privacy pool goes in solvent or something an entire L2 we wouldn't even know but if the base layer has transparency we always know at least the base layer can like sever that limb and survive. And I don't think that this is like a Perfect Analogy because these these pools would be slightly smaller than like a huge L2. And you're using them to mix so it's not like one address has like you know 100 billion dollars in it. But we do open ourselves up to like a question and fud about the actual of total amount of ethereum. and I also do think Lucas kind of mentioned something about like the regulatory perspective here. I'm not saying ethereum should bow to the ideologies of governments or anything like that. But there is a happy medium. Before there where you can still get things like privacy and you can still get things like provable total inflation right. Anyways I've said my part. I do think this is a very exciting construction. let me just say that I don't want to complain about that. I think it's exciting I think we should just use a lot of caution and it's not just for legal reasons it's not just for security reasons. I think there's like a ideological aspect to this. I think we should discuss all of them. And I'm happy to put my thoughts into the IP directly. 

**Tim Beiko** [59:28](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3568s): Yeah I agree you know both from a technical soundness you know analysis and also from do we eventually want to do this on L2s on L1 and what not.
There's a lot of discussions to be had then maybe this is a good place to like wrap up. What would be the best place for people to like discuss this EIP. I assume is like an ETH magician's thread but if there's somewhere else the authors think is better.

**Keyvan** [1:00:00](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3600s): We haven't built a like discussion group for that unfortunately yet.

**Tim Beiko** [1:00:07](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3607s): And got it. So let's maybe just use the discussion link on ETH magicians for now. And then if you have a new and better place we can move to that in the future. 

**Keyvan** [1:00:22](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3622s): Sounds good.

**Tim Beiko** [1:00:24](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3624s): Yeah but  thank you so much for presenting and if you can share the slides either here on the Discord or on ETH magicians that would be great for people to be able to review them.

**Keyvan** [1:00:36](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3636s): Sure thing I will put it in the chat too.

## Post-Verkle SELFDESTRUCT behavior

**Tim Beiko** [1:00:40](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3640s): Awesome thank you. Sweet then last up so Guillaume you wanted to discuss some SELFDESTRUCT behavior changes with regards to verkle Choice

**Guillaume** [1:01:01](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3661s): Yeah something very simple in fact I don't know if I can share my screen. Okay well it doesn't really matter. So what's happening is that when you like if you look at the text of the of the EIP 6780. It says when selfdestruct is executed in the same transaction as the one the contract was created in you retain the old Behavior. But there's one thing where the old behavior is not retained. And that's in the case of verkle trees in which case it says the clear storage will be marked as having been written before but empty. That's something we would like okay. I would like to change but it's a request that also came from  from dragon from Red. Because if you look at the code when you when you do the deletion. Basically nothing hits the tree layer. So we would have to create a special case to write to zero. and it's a departure from the current behavior and that's something that indeed has no observable difference from the EVM point of view. But from the code base from the client code base point of view does have an impact. So I would like to to remove this and just keep the  current behavior which is no like the tree doesn't get updated in that case. so yeah I would like to know if someone is against that. I know Dano has countered but I don't think it's really a counter. It's still compatible with this approach. Dano has suggested we we simply deactivate selfdestruct with vertical trees period. That's going to spark a lot of debate and we don't necessarily need to have this debate now. But yeah I would like to just focusing on on the EIP proper leaving open the possibility to Deactivate selfdestruct all together at a later stage. I would like to know if there's some disagreement with this approach of keeping the old behavior in the verkle Tree World.


**Tim Beiko** [1:03:51](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3831s): Any thoughts comments? 

**Guillaume** [1:04:00](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3840s): I mean there's a comment by Ahmad that's exactly what like the effect would be except you don't even delete what's in the tree because that account has
been created and selfdestructed before the cleanup code. The cleanup process at the end of the block writes it to the writes to the tree so it would be an in-memory EIP 168. Basically I mean this is how it works already I would like to retain this behavior in verkle.

**Andrew Ashikhmin** [1:04:39](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3879s): That sounds reasonable to me.

**Tim Beiko** [1:04:45](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3885s): And when you say this is how it works already you mean width 67 AV.

**Guillaume** [1:04:55](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3895s): Yeah even if you if you write if you create a contract and you selfdestruct. It in the same transaction. Okay all of a sudden I'm being unsure but I'm
still pretty sure that it never hits the disk. Basically so it's as if nothing was created.

**Ahmad Bitar** [1:05:15](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3915s): My understanding is the same it's as if nothing is created so like my question to Guillaume again is what exactly is the proposed changed because like if nothing hits the disk what's the problem?

**Guillaume** [1:05:32](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3932s): The  problem is that this is not what the EIP says currently. The EIP says in the vorkle Tree World when a contract is created and selfdestructed in the same transaction we should overwrite all the, for example, the balance should be set to zero and that should like the tree should be updated with a zero instead of the account being non-existent.

**Tim Beiko** [1:06:01](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3961s): Okay so this is the last bullet I'm looking at the EIP now this is like the last bullet of the second like exactly bullet two okay. Yeah so removing that. And I assume this would not change anything about current  implementations because it's all based on when verkle trees are implemented but.

**Guillaume** [1:06:23](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3983s): Exactly.

**Ahmad Bitar** [1:06:26](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3986s):Okay now it's clear. Let's check who added this point and why because like there must be a reason for adding this.

**Guillaume** [1:06:36](https://www.youtube.com/watch?v=CPt3f3ughFM&t=3996s):  So it's Dankrad and I asked him and he said he thought that would be. I don't know I saw him earlier maybe he can confirm directly I don't see him right now. Oh yes he's here. But yeah basically he said he thought that was simpler but turns out it's not. So unless Dankrad wants to add something that's my answer.

**Dankrad** [1:07:07](https://www.youtube.com/watch?v=CPt3f3ughFM&t=4027s): Yeah no, I don't have a strong opinion on what the state of those search addresses should be. Yes it was simply seemed like that would be the straightforward to implement it but if it's the other way around then we can just re-specify it like in practice it shouldn't matter in practice like in from the EVM point of view. Both of them look completely empty. So it's only about the state commitment where we need one unique definition.

**Tim Beiko** [1:07:45](https://www.youtube.com/watch?v=CPt3f3ughFM&t=4065s): So in that case Guillaume if you want to open the PR to just remove it maybe give people a couple days to comment if they weren't on this call or whatever um but then I would push for us to make that change now. Because when the EIP is deployed on mainnet and it's set the final. It'll be harder to change. So yeah now feels like the right time to just remove that. And it won't change anything in terms of client implementations but at least the spec will be a future proof.

**Guillaume** [1:08:21](https://www.youtube.com/watch?v=CPt3f3ughFM&t=4101s): Yep okay I'll do that thanks.

**Tim Beiko** [1:08:23](https://www.youtube.com/watch?v=CPt3f3ughFM&t=4103s): Cool Any other thoughts questions?

**Ahmad Bitar** [1:08:28](https://www.youtube.com/watch?v=CPt3f3ughFM&t=4108s): Why are we defining Behavior about verkle in an EIP 4678 when Merkle did not hit mainnet yet. EIP standards yeah.

**Tim Beiko** [1:08:39](https://www.youtube.com/watch?v=CPt3f3ughFM&t=4119s): So we should have. I agree it's kind of weird, yeah.

**Ahmad Bitar** [1:08:48](https://www.youtube.com/watch?v=CPt3f3ughFM&t=4128s): Yeah my understanding is that if you want to add such specification it should go into how verkle is implemented not how the 6780 is implemented that's just how I think about it. 

**Guillaume** [1:09:03](https://www.youtube.com/watch?v=CPt3f3ughFM&t=4143s):  Yeah that makes sense at the same time the vertical EIP is already pretty
long. So it would typically for I assume you know people there's a risk that people might forget stuff but yeah if everybody wants it I don't mind removing the entire paragraph because yeah it makes no difference to me.

**Tim Beiko** [1:09:32](https://www.youtube.com/watch?v=CPt3f3ughFM&t=4172s): Okay anything else on the EIP. Okay and that was the last thing on the agenda anything else anyone wants to add before we Hop Off. Okay well thanks everyone and talk to you all on the calls next week.

**Lightclient** [1:09:58](https://www.youtube.com/watch?v=CPt3f3ughFM&t=4198s):  All right thanks.

# Attendees
Sifis Lagouvard
Marek
Mauris Van der Wijden
Trent
Paritosh
JOSHUA Rudolf
Ignacio
Potuz
Nishant
Den Edigington
Echo
Ahmad Bitar
Keyvan
Hamidreza Moradi
Mikhail kalinin
Ruben
FLCL
Andrew Ashikhmin
Barnabas Busa
Mark
SPENCER
Carl Beek
Peter
Pooja Ranjan
Roman Krasiuk
Caspar Schwarz- schilling
Hubert
Afri
Haiao-Wei- Wang
Danceratopz
Danny
Stokes
Marcin Sobczak
Fredrik
Guillaume
Dan cline
La Donna Higgins
Light client
Jochem
Keyvaan
Mario Vega
Anna thiesar

### Next Meeting Date/Time: October 12,2023, 14:00 UTC


