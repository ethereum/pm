# All Core Devs Meeting 114
### Meeting Date/Time:Friday, 28 May 2021
### Meeting Duration: 1:37:45
### [GitHub Agenda:London Updates](https://github.com/ethereum/pm/issues/321)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=7MSYLbn-Xro&ab_channel=EthereumFoundation)
### Moderator: Tim Beiko
### Notes: David Schirmer

## Decisions Items
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
| **1**   | Malicious bloated 1559 transactions ethereum/go-ethereum#22963 | [9:14](https://youtu.be/7MSYLbn-Xro?t=554) |     
| **2**   | Baikal status & next steps |  [41:55](https://youtu.be/7MSYLbn-Xro?t=2515) |  
| **3**   | Testnet Fork Blocks confirmation |  [52:20](https://youtu.be/7MSYLbn-Xro?t=3140) |  
| **4**   | Ropsten Stress Test |  [55:41](https://youtu.be/7MSYLbn-Xro?t=3339) |  
| **5**   | Gas: DoS protection & decoupling worst/average performance |  [1:03:45](https://youtu.be/7MSYLbn-Xro?t=3821) |  
| **6**   | EIP-3584 |  [1:19:00](https://youtu.be/7MSYLbn-Xro?t=4741) | 
| **7**   | Gas API Call |  [1:02:11](https://youtu.be/7MSYLbn-Xro?t=3731) | 

## Decisions Made
114.1 - Clients agreed adding consensus rules:
* [1] maxFeePerGas < 2²⁵⁶
* [2] maxPriorityFeePerGas < 2²⁵⁶
* [3] maxFeePerGas >= maxPriorityFeePerGas
* [4] sender.balance >= gasLimit * maxFeePerGas (Cap on consensu level and mempool level)

114.2 
* Calaveras, a new devnet will be spun to test new changes.

114.3
* Assuming the testnet forks smoothly, then a dork block for mainnet will be purposed.

114.4
* Once the the fork on the testnet is complete, stress testing will continue.

114.5
* Alexey's proposal to seperate the transaction pool for the clients to diffuse execution bombs. Promising area of research. Moved to Eth R&D to discuss further.

114.6
* Addition of access lists to blocks may complicate things. Continued discussion on Eth R&D channel.

114.7
* Call scheduled for June 5, 14:00 UTC to discuss the impact on gas price oracles.

###  Malicious bloated 1559 transactions
Tim Beiko:
* Hi everybody welcome to All Core Devs 114 and a couple things on the agenda today lots of London updates that if we have time there are two others on the list. First, on the list Martin you identify an issue with 1559 for you yesterday for me do you want to take you may be just a few minutes to kind of walk through like at a high-level what it was and I know that Micah I don't know if he is on the call had put together a set of like potential ways we can fix it.

Martin Swende:
*  yes so the issue is that a transaction and has two new fields which are integers and like any other integers they are arbitrary large integers the same is true for the previous, you're going to gas price but in practice, you can not set a high gas price however these two new fields, we only use one of them and the price that you are paying is based on the minimum of the two. It is perfectly fine to set a 1MB large integer into the other fields unless you can create some type of nasty transactions which do not cost more and you do not pay for the extra size. This is ugly. It turned out nethermine also C++ implementations that hyperbase is working on are actually capping to 256 bit which is not according to the specification which would lead to consensus issues if one of the seeders included this in the block. It's a consensus problem already. Are there any questions? 


Tim:
 * looks like everyone gets in. A few options on the table. One,  these fields can be 256 bits or less or some other value. 64 bit is probably too small but we can talk about that. Another option is that we can say that the premium must be less than the max because it doesn’t make sense to have your premium higher than your max. Then we could separately say that if the max gas times the gas limit, you must have that much in your account. The last option, Is there any reason we don’t just say throw out the entire protocol, numbers will always be 256 bits or less. Do we have any use for anything bigger than 256 bits?

Vitalik:
* I think there wasn’t really a good reason behind doing something like that. The beacon chain protocol is constraining everything to 64 bits anyway. I do think that an implementation of that scale will take longer than London if we go down that direction we might need to make it a special feature or exclusively for the U5050 and then do something more comprehensive for the next fork.

 Tim
*  Yea sure, Ansgar you had your hand up?

Ansgar:
 * I was wondering what the arguments are for or against requiring that the balance of the sender is sufficient to cover the peak gas because in some sense it feels like the right thing to do regardless because somehow it’s a mis- specified transaction if you can’t pay for it.

Micah: 
* So I think the point of contention around that is. So the first rule would be that the max fee for gas should be more than the max priority fee for gas. The total should be larger than the part of the total right? I think people are agreeing on that. The other one says that the sender balance should be larger than the gas times the max fee for the gas whereas the actual cost is the gas limit times the effective fee for gas which is one of the two and it might not be the max fee for gas. It might be only the priority fee for gas. This rule adds a harder requirement than the actual execution. It requires you to have more money on your account than you will be charged. So that’s the non-intuitiveness of the last rule but I think it still makes sense to have that.

Ansgar:
* Would it also simplify meme pool handling because otherwise, you might let a transaction into your meme pool that at the time of inclusion it all of the sudden can’t pay for itself.

Micah:
*  I think that it will simplify many things and  I don’t really see a downside.

Rai: 
* Yea there are edge cases around like the sender’s transactions varying to accommodate then not accommodate the max fee but it does sound like an edge case.

Alexey:
* I would say that it makes sense to limit these numbers by the formula binding it to the account balance but I don't think it should be the only protection. I think there should be two places where protection his place because they kind of like you know there I think that we should at least for these fields just introduced a limit on how big they are and then if we want to on top of that we can introduce a limit with the balance because it is much easier to reason with the first limit than to reason about the second limit.

Micah:
* So let's talk about the consensus changes. Were you talking about non-consensus changes Alexey?

Alexey:
* No, I assume that EIP 1559 has to be modified to address these issues and I suggest that if we modify it we introduce two rules in it. The first rule would be a consensus rule that would require that this specific field for now we don't want to mess up the whole and go through the whole protocol. These specific fields and potential all of the new fields that EIP 1559 needs to be limited by 256 bits but then on top of that a non-consensus requirement to not allow those transactions that can’t pay for themselves but I can see that it is not normative. It's some sort of an optimization thing.

Martin:
*  In my opinion of the implementation it doesn’t really matter what we do because if someone can mine a block where the gas limit times the max fee for gas is larger than the sender’s balance. It does matter if the clients have implemented this in consensus or not. We need to be really careful here in what is consensus and what is not.

Alexey: 
* I would suggest a change in consensus which just simply limits the size of the numbers because it’s the simplest thing you can reason about.

Martin:
* I mean it’s pretty simple to reason about in my opinion whether the sender balance is above the gas limit times max fee for gas. Also, the max fee for gas is larger than the priority fee for gas. If those two, max fee for gas and priority fee for gas, places a constraint on priority fee of gas. The other rule places a constraint on the max fee for gas which implicitly makes them both need to be less than 256 bits because the balance cannot be above 256 bits. in my suggestion but I put on the agenda I posted the four rules but the top two rules are implicit by the top two rules. They can be made early, a cheap early check before accessing the state or they could be omitted if you follow the other two rules.

Tim:
* Am I right in saying at least you the clients already have those first checks right like I believe nethermine said and I think open ethereum they said they're already doing this check so it's almost like they have this rule even though it's not explicitly documented.

Martin:
* yes and that's yeah that's that's what I said, it's a consensus issue right now.

Lucasz:
* To clarify we're not doing the check we are just using the type that won't accept anything else so we will have an error when we try, like, something bigger?

Martin:
* Yea except you won’t accept the transaction so the effect is that you will reject it.

Tim:
* So is anyone actually opposed to putting all four rules? I'm just because this way we can know it seems like the first two are fairly trivial and the last two are kind of needed and just for maximum kind of clarity and Alignment between implementation. Is everybody fine just put it in those four checks at the ones that Martin had at the ACD so max fee for gas and priority fee smaller than 256 bits then Max fee be bigger than the max priority and the balance bigger than gas limit times max fee for gas.

Vtalik: 
* Both times you say bigger do you mean bigger or equal right?

Tim:
* Yes sorry bigger or equal.

Alexey:
* I would put the first three as the consensus rule. The 4 one which is to Center balancing I don't know if we should because it will be enforced anyway right in a different way.

Martin:
* No it won't, so if we don't explicitly specify it. 

Vitalik:
* Right the idea is that that if you have a transaction with an insanely high max fee and you don’t have enough money for it then if we do nothing the transaction would be valid if the base fee is just not high so it doesn’t get that high but if the base fee does get that high then the transaction would get excluded whereas this proposal it would always be excluded.

Tim:
* Yeah and if we did not have the last ones are there weird things that's like MEV could do for example like I have a transaction in spot one that then sends money to an account that had like one of these funky transactions which is right after the transaction kind of only becomes valid I don't know.

Thomasz:
 * yeah, I just wanted to write this so I guess if any check that happens in the transaction pool is up to the clients, and it’s not part of the consensus. If we are checking if it is greater than max fee per gas times gas limit since it’s not necessary and it's done just before the transactions are executed, it how I understand it. This rule is proposed to verify just before the transaction is executed. I'm sorry I’m starting to think I need more info on why we would need to enforce this extra. it might be that you want to keep that transaction alive does it attack the transaction pool if we base it on the max fee per gas? you could push a lot of transactions with a high max fee per gas for the accounts that have a low balance and it would just stay in the pool for a long time because we think that they are valuable right? 

Rai:
* Well is anyone prioritizing not by effective max fee because the way we do the eviction is that if you did send those you know really high max fee per gas low balances it’s not going to get evicted.

 Thomasz:
* Yea but affects your effective max fee per gas is one of your components.

Rai:
* Okay got it.

Ansgar:
* How about not enforcing it on the consensus side but still recommending that clients don't accept those transactions in the meme pool.

Martin:
* I think we should discuss the consensus rules first. So with the consensus rule. We can also discuss the transaction poll and how they should behave and what we recommend but we should try to determine what consensus rules we should have.

Lightclient:
* So we agreed on the first three requirements that you posted and we are on the fourth one now or are there still questions about the first three?

Thomasz:
* I agree with the first three and I would prevent the fourth from being installed for now.

Micah:
* we don't actually don’t need the third one; the first two would be sufficient, just a 256-bit check. If we are looking for the absolute minimum change?

Martin:
* I think if we need to change this at this point if we have two checks or three checks I don't think it matters a lot and I think it's if we add this check which makes sense is it sensible to check I think yeah I don't think that adds more overhead. I would prefer to have all three of them.

Lightclient:
* Do you prefer to have the fourth one as well?

Martin:
* personally yes.

Lightclient:
* so it seems like the last check is mainly to avoid some free call data. This is bound to 256 bits. I don't know what the average size of the cap will be. Maybe it's like 16 bits or something but the rest of it could potentially be free call data? 

Martin:
* I totally exploit that because when we were going MEV stuff every bit counts since you want to minimize your gas cost and so I would definitely bit pack stuff into the max fee per gas because if you are doing MEV stuff you want to be first your max fee is whatever just bit pack that with all of your data.

Micah:
* But you can’t access it on-chain can you?

Lightclient:
* You can’t access it now but in the future, there might be opt code to access it. I was assuming that we would add opt code for that be I would protect it.

Alexey:
* I would also add, for the moment, for example, there is an implicit consensus rule regarding the gas price where gas limit multiplied by gas price and it happens Because by the rules first before the transaction get executed at has to purchase the gas, the balance gets subtracted by this amount and then if there's anything left then this gets returned and then it's important because during the execution of transaction if the transaction observe the standard balance it will be without this Ether that has been used for purchase so what now if we introduce the rule that standard balance more gas limit multiplied by max gas fee then we purchased the gas using affective or whatever, I don't know, remember basically we are using the different formula. It is a bit more confusing if you observe the balance. I think if we reduce this requirement we should also change the way that the gas is purchased. It will have to be purchased in the amount of gas limit multi because then that would make sense if its a consensus rule.

Micah:
* So just another weak argument for number four. Generally when building things that are security-critical I’m a big fan of having as many insertions as possible. I'm just it makes it easier to think about software and reason about it if you know that there are certain constraints in place. In this case it doesn't make sense to allow the sender balance to be less than the max and users and wallets whatnot can easily implement that and make sure that's true. It gives us one more thing that we can assume while we are writing the software and working on it. This isn’t a strong argument. Engineering tends to be easier if you have more constraints because there's less to think about.

Alexey:
* What I am suggesting is that if we do introduce this constraint we also change the logic of the gas purchase then it will be consistent. If we require already this is the balance is enough why don't you just purchased that much gas and then that would automatically be implementing their restriction will be consistent so you don't have to have like differences in terms of how much you purchase the gas for and then there's another constraint and so I think it will be cleaner to do that.

Martin:
* What you're describing sounds to me like a very large change in the mechanics of EIP 1559?

Alexey:
* I think it's in the same level of changes as the fourth constraint and I think this is actually the equivalent in terms of complexity because all you need to change the high gas function I mean another client is a different name but essentially by changing this function to go to purchase gas differently your implicitly introducing in the restriction number four. 

Lightclient:
* I think we will need to change how we refund gas? The actual cost I think is the same thing. I'm not sure which would be more complicated, my intuition would be that the check itself, just have a one line check somewhere and then do the gas purchasing as it is but their equivalent. 

Micah:
* if we did that it would have intentionally affect somewhere down the line if we ever implemented transaction type to let you execute as the EOA because it such transactions you hypothetically would be able to check your balance from the EOA context and so that would have an impact like you want to sweep your account for example being able to do that will be much harder if you fee per gas with what the base fee is going to be in your future block. Again this is just trying to future proof things because we have talked about adding that type of transaction at some point.

Ansgar:
* Isn't the only reason that the right now is your charged in advance full gas limit just to insure that you are actually able to pay and so i don't see a reason to do that with a full tcap because you know you will only be charged the actual base fee. It seems artificial.

Lightclient:
* I think the only reason to do it is to avoid people using this as free call data and its not useful right now because there's no way to access it but it might be in the future 

Micah:
* so you could use this for something like if you were bitpacking this for something that looks at call data, like a layer 2 solution, that's using call data for its mechanism for data storage.

Martin:
* Basically you cannot put 1 mb in it. We will fix that but you could still pack 256 bits into a field that will not be validated and will just tag along with the original transaction. If we bound it by the balance there is a lot less freedom which is why it's my favorite. I also did not think it was good when Micah suggested it. It doesn't matter to the actual calls. I will not die on the hill but I prefer the fourth rule as well.


Micah:
* I am in favor of capping it.

Lucasz:
* Martin and Micah, do you want to cap it on a meme pool level or consensus level? So reject blocks?

Martin:
* Yea I am speaking about the consensus rules here.

Tim: 
* It's worth noting that if we cap just in the meme pool especially now with stuff like MEV geth most of the miners will be modifying the memepool implementation so I doubt that it will make a big difference into what actually gets into the block if someone really wants it there.

LightClient:
* Where's the argument for not doing this check?

Asngar:
* Well you could have a situation where lets say I am sending two transactions and they both are barely able to pay for the transaction but then I maybe fam the first one and it goes in a diaprise and basically slightly misspecified the second one and I couldn’t be able to pay at the highest price but if the base fee is low enough I can pay for it so what's the reason It should not just go in. It seems like it's not a malicious transaction, it's a transaction that does everything right, it just is mispecified for the highest possible price. I think this could organically happen.

Lightclient:
* I just think that would be an incredibly uncommon experience this is likely to be exploited by many people on a regular basis if there is no check.

Martin:
* yeah I mean it kind of feels like a scenario where an auction and you make a high bid and it turns out you didn't have to pay the highest bid you have to pay the second highest. So you made it and no one called your bluff but the bid shouldn't have been accepted in the first place because you made a bid you couldn't cover for. That's one way to see it maybe.

Peter:
* How easy would it be to remove this kind of requirement? In the future if we say like EIP 1159 is new and we want to be a restrictive as possible in the beginning but if someone really feels strongly about it , they could just create an EIP for future to remove this change? 

Micah: 
* It is generally easier to remove constraints than to add them if we want.

Peter:
* That might be the most practical way forward then.

Peter:
* So Thomasz I think you were weakly against the fourth one. Would you be okay if we went with it and then remove it if we see a valid reason too?

Thomasz:
* Yea weakly against means that if others think that it's worth doing then I am totally fine.

Peter:
* Is anyone strongly against going with the fourth set of constraints by Martin that I won't try to describe again i'll make mistakes with the ACD, sorry on the issue for this call.

Lucasz:
* So the fourth constraint as Alexey explained it? So when we are reserving gas for the transaction before the actual execution. We would just reserve more or how would that work?

Alexey:
* No, you would still reserve what you reserve now but additionally, you also require that the sender balance equals more. I think what we are trying to agree on is not what I suggested but I think what Martin originally went with. So there will be different numbers that you have to reserve and we that you have to restrict.

Martin:
* it'll just be one assertion added to the code that just asserts that this is true at this point. Technically two assertions if we go with all four. The minimum change for any client is just two assertions to be added. Of course, we will specify and get it into the EIP if we agree on that so we can where they go

Micah:
* Thinking if there are any potential issues or if we liked don't specify when the session happens exactly.

Martin:
* Yea as you are processing a block you process the transactions one by one and for every transaction, you check the validity of one of the existing constraints, the intrinsic gas must be more than any intrinsic gas times the gas price and this is just two more of these rules that validated during block processing.

Lucasz:
* You would have to validate it during block production to complete the transaction.


Martin:
* Yea, you try to add it to the book that you are trying to build you would do the same thing.

Ansgar:
* Would clients be expected to make sure that these transactions could never make it into the meme pool?

Martin:
* Yes for one perspective. I think the clients have a pretty clear distinction between what is consensus and what is meme pool. Those two don’t really share the same rules. The meme pool, for example, can be more restrictive about things.  It can throw gas costs of 1, 0, or 3 and whereas the consensus you have to just accept the zero fee transactions. Otherwise you break consensus. 

Ansgar:
* Makes sense.

Tim:
* Okay, so it seems like we are good for all four rules. Does anyone want to voice a final disagreement on that and if we decide that the fourth rule isn’t needed in the future then we can submit an EIP to remove it. Obviously, there are more checks, more code, more complexity.  That’s the trade-off there. Okay so no blockers, let's go with the four consensus rules. Does anyone want to submit a PR against 1559 either today or monday.

Martin:
* I can.

Tim:
* So Martin once your PR is there we will need an author to merge it. Either Vatalik or I can ping Andel. Once that PR is merged I will make sure to update London with the latest commit

Vitalik:
* Sounds Good.

### Update on Baikal

Tim:
* Cool. Anything else on that issue? Okay if not, the next thing I had was a quick update on Baikal. Testing on it in the past couple of days. There seems to be some issues with some signers not including all transactions. I don't know if anyone wants to recap the testing that has happened and the issues seen?

Martin:
* Nobody knows what's going on right.

Tim:
* from the outside it seems like I think it was Karim and somebody else who were trying to kind of spam the network with transactions.

Karim:
* Yes. I can say I did some spamming on the test net. I sent some 1559 and legacy transactions. I tried to send the transactions directly. It seems that it was forking fine sometimes nethermine would not completely fill the block and geth and I was sending directly the transactions. So I tried today another thing to send the transactions to another node. It seems better. Geth fills the block. I think when I did the test nethermine was not running. So I don't really know what the status for nethmine, yesterday mine had some issues. Maybe nethermine will have more context but for me, geth, it seems okay. I can continue, I have a test to do with different feecaps. So I will try to do tests the next day.

Thomasz:
* Ya I see that the transaction pool is misbehaving slightly. We are in the process of merging some Immediate Solutions to the transaction pulling nethermine and also I like rewriting some basic transaction pools so we see a lot more instability still being caused internally as well but we had more discussion today and yesterday about it.

Tim:
* Was Open Ethereum on Baikal yet?

Sunce86:
* Not officially.

Tim:
* Did you see any issues? Nodes working fine?

Sunce86:
* Until today we were in a sync.

Tim:
* On the turbo Geth side. Did you see anything special?

Alexey:
* No, we just had one issue where I forgot to activate the EIP with the refunds. I think it's interesting it occurred five days ago so I think that was the first transaction that had this kind of thing but now it is fixed. It's called Arragon now, not turbo geth by the way. 

Tim:
* Given there are still some finalizations that we need to do with Baikal and we will have some changes in 1559. What do people feel are the best ways to test those changes? Do we want to hard fork baikal? Do we want to write a test for it and test on the proper test nets. We could spin up a new devnet? It's a bit more complicated to do that. How do people think we should go about it with a test on 1559 and the issues on Baikal?

Peter:
* So I don’t think you want to fork Baikal because that means you need to define the fork and essentially you have something of EIP or four pools on top of four pools. If the consensus was changed like Baikal was always meant to be and just nuke it.

Tim:
* Is it possible to just restart Baikal and we just change the genesis but like all the current infrastructure stays there? Or should we have another network with another name to make it simpler? Or people comfortable to say we implement these things and add references and then fork Ropsten. That’s the part I don’t have an intuition for.

Peter: 
* We change the EIP rules so we need to do another round of testing.

Tim:
* So in that case should we create a third one?

Peter:
* I don’t know who created Baikal and how much effort it was so I cannot say. I personally don’t mind just nuking the chain and starting a genesis.

Martin:
* It’s pretty simple.

Tim:
* To create a new one? Does anyone oppose creating a new one?

Alexey:
* Will it have the same name?

Tim:
* Does that make a difference to people?

Alexey:
* I suppose it would create confusion if it's the same name.

Tim:
* Will we have to change those things if we create a new network or will they work if we just reset the genesis.

Alexey:
* Do we have transactions that are breaking those rules?

Martin: 
* I would suspect that we have transactions that are breaking the fourth rule. Possibly the third rule as well. I know someone mentioned experimenting stuffing crap into these two fields, I think jochen.

Alexey:
* One option would be to shut it down right now, Baikal, and examine whether we had any rule breakers and if we didn’t then we simply restart it with the new rules and if we did then we would have to start a new network.

Martin:
* We don’t have to stop it. If we just add these checks and try to sync then it should be parallel.

Alexey:
* Right optimistically we should try to salvage Baikal and if it doesn't work then we launch a new one.

Tim:
* I like that approach. Does anyone disagree with that?

Alexey:
* Na makes sense.

Tim: 
* Okay so we add the new checks to 1559, try to sync Baikal and if it works, great, we will just update the Baikal spec with the new commit. If it doesn’t work then we will start Calavaras. Which will be a copy of Baikal but with the 1559 changes. Nobody please break Baikal in the next couple hours. 

Martin:
* It is not possible to do the first two rules unless you can hack the seeder. I’m fairly certain they have already broken rule three or four.


### Test net block confirmation 

Tim:
* Okay, let’s try that. It’s worth it after the call, we can ping him in discord and ask him directly. Obviously, this invalidates the testnet blocks we had potential for June 9th. I’m curious what the teams feel, what’s the best approach to get to testnets. Do we want to do this and then potentially set the blocks on the next call if the people want to look at potential blocks that are a week or two from now. I don’t know what is easier in terms of, obviously, knowing that these changes work and managing the relief cycle for the clients? Do we know enough to set a new block for clients to test?

Martin:
* My five cents is that I still have some work to do. It's going to be pretty hard to get everything done in time but on the other hand I am personally not too scared about breaking or screwing up the testnets a little bit and we will be fine but other people may have other opinions. 

Alexey:
* we are planning to modify, heavily modify, the transaction pool I know that these people would say this is not critical for the testnet but still has some work to do there and the result of that, if we do go ahead with this testnet, it's likely that the test the first testnet that we will fork will not look anything like the main net running the code which is very different regarding the transaction pool and i don't know if anyone is actually planning to test transaction pool changes. Is there any plan for that? Or are we going to just do some unit tests and other things?

### Ropsten Stress Test

Tim:
* So one thing that we should do at the very least on the test nets is have a kind of time where we spam them and send a very high number of transactions and you know make sure that that works like the base fee is working and the clients and miners are including transactions.  Beyond that, I don’t know. 

Alexey: 
* Do we have tools for this sort of thing? Somebody said, Karim i think, he is spamming. Do you use some sort of tools that you created, could they be used in the test net? Is it easy to interpret the results?

Tim:
* so yes we have the tool. Basically, we have to just send a very large number of transactions and I think the only constraint on it is we need a large Ether balance on that Network. So for Ropsten specifically I think we would need to find you know some Ropsten whale.

Alexey:
* Ropsten whale no?

Tim:
* I have been looking for one this week so I will ask him.

Alexey:
* I think he might have some Ropsten Ether.

Tim:
* It’s because the base fee increases exponentially like the amount that you are going to burn during this for one hour is very high. Aside from that I don’t think we have any tool in the infrastructure to test more complex things for the transaction pool.

Alexey:
* Another thing, on the old testnet, I would suggest, it is easier to test something like this on a very constrained Network where you have a very low gas limit because then you get to exponential thing quicker. At the same time, using public testnets which are heavily used, you don't really want to constrict those too early.

Tim:
* I agree with that. My preference there is to do Ropsten and then Gordie so we can do this spam test on Ropsten which doesn't have a ton of real world usage. Then we can do a small one on Gordie, but that one does have actual users. I think we should try to go from the most artificial to the most used network.

Alexey:
* With this spam test we might price everybody out for whatever the duration of time.

Tim:
* For like an hour yea. So clearly Geth/Aragon still has some work to do. I don't know whether the other teams feel? Thoamsz, you mentions you had some transaction pool work that you are doing. So it's out of it seems to me like people will probably be much more confident in the state of things two weeks from now. You know want it to be realistic, do we want to just have it in two weeks and potentially kind of a set a block that fairly I guess close from the next call. The constraint being we don't want the difficulty bomb to go off on main net and we want some f large amount of time that. A more concrete way of asking this question is if we come to the next call and things are generally good with regard to the clients. Is like a few days sufficient for clients to put in for blocks and put out a release right? like if we come to the next call we decide we’re forking in the test net like 10 days and can clients have a release just like 2-3 days out after that so that we can then kind of advertise those releases and an empty bucket update? Okay, I am not hearing any objections. So let's do that then. Let's take the next two weeks to do the changes to the spec and test things on the dev nets, make sure that the transaction pool stuff is done. On the next call, assuming everything goes right, we can pick a block. It doesn’t have to be too far out in the future for the first testnet and teams should probably expect that we will be putting out the release with the fork blocks in a couple of days after the next call. Okay, anything else that people wanted to discuss for London specifically. Okay, if not, we do have some extra time. Alexey, I know you had something you wanted to talk about in regards to gas pricing and denial of service protections?

Martin:
* Really quick just the gas API call? You want to mention it.

### Gas API Call #328

Tim:
* Sure, I was going to at the end. So this week, we had a discussion with wallet providers to discuss UI changes to 1559, Setting defaults for users. One thing that came up during that call is that all of the wallet providers rely on the gas estimator Oracles/API like ETH gas station and how they implement their predictions for gas prices will matter a lot. So I'm organizing a call next week, next Friday, at all core devs time with these gas API providers to discuss the best way to provide these estimates post 1559. The link is shared in the agenda. Obviously, anyone that is affected is welcome to join.

Trenton:
* Just send me an email of anyone that would be interested in joining.

Tim:
* Lightclient found the transaction that invalidates the fourth rule on Baikal already. So we will have to restart it. So in that case, we will go with Calaveras.  I will put the spec together today as soon as the new PR on 1559 has been merged and we can use that and stand it up next week. Anything else on London? Okay, Alexey over to you.

### Gas: DoS protection and decoupling worst/average performance 


Alexey:
* Okay so I'm going to just introduce this topic briefly so just to make sure the people are aware of it. It's not normal to call for action but it's just for your awareness that is what we are planning to experiment with. To explain that when I talked about the coupling all the worst-case performance and average performance that's what I would mean. so context is essentially the question about the safe gas limit, how is it determined, and like where are you know he's at the correct/ good way of determining the limit. So as far as I understand the current limit for the safe gas price is determined by a couple of things or one of them is is kind DOS limit. what is the worst time to run the worst construction transaction that would consume this entire limit and as we saw in the book was recently published is that they used to be some really I mean really simple but very potent transaction that could cause a very large run times and so it was mostly based on the state access which was under price so now even if we do reduce the state's access cost and we also put filters and all the things even if we do that . The other bottleneck that will appear on the surface is the precompiles for example the precompiles will be the second target because they currently priced, like when we do the pricing, precompiles sometimes, I think there are certain mega gas per second, keep in mind, I don't know what that number is right now maybe 25 maybe 40. The repricing of the precompiles actually using this kind of made-up number, which is kind of the targets, of a safe gas limits and 40 or 25 I don't know. the different precompiles were computed using different targets. What it means is that yeah that could be like a worst-case transaction which then targets those precompiles like there's lots and lots and lots precompiles and even if you optimize the state access you know you're going to hit those things. It doesn’t mean that we are completely constrained by those things well actually I think it would not we're not. So my idea is that we are going to experiment with and I want to make people aware is to try to stop, I call them execution bombs. If you think about an analogy,  that is the transaction that carries that explosive load that is really hard to execute. Currently, it is not getting stopped anywhere because the transactions are usually not executed on the way to the miner node  and it goes straight into the core and just explodes there essentially. like a different type of node have different implications for that. For example, miners may start mining empty blocks. The other nodes might stop processing things and stuff like this. The idea that I am going to look at is to try to stop those transactions bombs before they reach the core 
and stuff before they reach the core to form some kind of protective perimeter around the nodes to stop those things. So that implies that the things that will form the protective perimeter will need to be able to verify or check or try to figure out whether this particular transaction is actually going to explode. So that's the main idea and the way we are going to experiment with this is according to our architecture plan, at some point we will split out the transaction pool component using some interfaces and we going to experiment with the transaction pool component actually trying to execute transaction and capture those execution bombs and try to defuse them before they reach the core. The reason why you have to get it separated is because you might want to have multiple transaction pools around you a node so it's one of them, kind of is being slow down, by the bomb the other ones that still working and so forth as to create a little flexible architecture, flexible deployment to do that. That is the crux of the idea and I just wanted to introduce it and to let you know that we are going to try to experiment with that and if anybody wants to contribute to that is obviously welcome. 

Lucasz:
* I have a comment. If you are protecting transaction pools you are not really protecting the chain much because someone can just mine this block and put it directly on the chain.

Alexey:
* I didn't go into details on that but so you can go deeper so you can notice that there are two cases that you have to think about. First case is where attack is basically performed by no miner basically just putting the transactions in the pool and a second type of attack is made by the miner itself and so you need to look at them differently and they might need to have different protections because I think generally the miners are incentivized to bomb the other miners around unless they are the majority but the people who are not mining and they might have completely different incentives.

Dankrad:
* Isn’t gas our protection against these DOS attacks?

Alexey:
* Yes, however gas is a very blunt instrument unless we sort it. We actually do need to modify the gas cost quite frequently and a lot of times we have to keep the real reason for gas modification some kind of secret because we cannot disclose that this was because of some kind of violence. So you either you have to change it in a rush, it was done in 2016, where you have to keep it as a secret kind of or maybe an open secret and then try to introduce the change on a different pretext. So what I'm suggesting is it does not negate their role of gas is the protection but it creates an additional layer of protection which allows us to be but more relaxed about you know those vulnerabilities. If they are found we can actually fix them in a good time and we can we could be kind of much more professional about it rather than trying to let you know having secrets and stuff like this.

Dankrad:
* I guess I feel like it's very lucky that you can find some sort of metrics that work well but the concern is what about the transactions that are caught by your metrics but are not malicious they just happen to have very high resource consumption

Alexey:
* I would like to listen to the other couple of people that raised their hands if you don't mind and we can return to this discussion as well.

Martin:
* I think it is an interesting idea and I think it is worth pursuing. I don’t think it changes the threat model and I think because I do think that miners have an incentive to bomb other miners because once you start building on top of the block it is hard to just throw it away and try another bucket. Once you have spent a minute importing that block, why not build upon it. So it doesn't change anything intrinsically but it will be interesting to see what you come up with.

Mikhail:
* I was going to ask about what metrics have you thought of? The first obvious thing is the execution time of the transaction but it is too subjective. What else could we use, like CPU cycles, could be difficult to measure for transactions. So what are your thoughts on this?

Alexey:
* My thoughts go very far on this and so in the first approximation we could simply use some kind of time out and some other limits. When we execute the transactions inside the perimeter we can use some kind of physical constraints in terms of like how long is it allowed to run like how much state access is it performing and aport the transactions once its is past these limits but on the second iteration which might come later I actually was trying to run some through preprocessing on the transaction to try to figure out before even running it on the specifics state. To  try to figure out if it's possible to figure out to predict whether it's going to hit a lot of State for example that would catch those DOS attacks that were published on the log and lots of others including the ones that we also found which were targeting specific Aragon. All of those attacks that I could think about, all these classes of attacks that could be eliminated by static analysis interpretation but obviously that is a bit further away into iteration 2 or 3 on this project.

Mikhail:
* I was asking because after the merge we will be operating in a time-restricted London this matters more probably than it  matters today. I mean it could be like one of the simple but effective protection for block proposers so they see that the block is not being proposed or it takes a lot of time to execute a block they are about to publish.

Alexey:
* Yes and you just reminded me of another connection I made yesterday. So I think this goes in a similar direction of another train that is going on right now which is MEV and the flash bots trying to democratize the MEV system and apparently the way that it works is that you have independent flash bot runners who are running essentially their own transaction pools to try to construct the bundles and so and the separation of transaction pools from the core has already happened it's already happening in flashbots - MEV world and I think it's only natural to basically just follow that as well. So I think I'm suggesting what is happening in flashbots and he's already steps in the similar directions. I also think that these special checks for the transaction to go to the pools will increase the latency of the transaction propagation especially for transactions is a bit strange it's a bit hard to find out what it does and it takes some time obviously as it hops through those perimeters it will take time but that's okay because straight forward transactions would go very quickly because you can simply see that they're fine but the strange ones they will go slower so the pool and they will end up with the miners later But if the miner wants to take a risk with taking those things I can simply do it it via flashbots. So it furthers the idea of two lanes. A fast lane where people take risks and a slower lane where the public lives which has all of these protections where the bombs are getting intercepted and things like this. So this is the vision of the future I have when considering the problem with the flash bots. Thanks for listening and I appreciate the feedback so far.
 
### EIP 3584

11crypt:
* Hey guys I have co-written this draft EIP with Piper which is circulating the transaction level access list which the clients will be generating for EIP 2930 and what we are doing is trying to collect this access list on block level. So we want to present this EIP and get some feedback again. This is nothing we want to put on the table as of now. So if you look at the EIP. So the EIP says that the block level access list is posted between access addresses which basically its address is accessed and this transaction number and is consumed this slot in that list of source index transaction number. So that is the sort of access list we are trying to build on the block level and a construction of and sort of civilizing it And what we are saying that for this list to have any meaning as an index and do the block so that other miners can look at it or the people want to validate the blocks, they can sort of do any optimization because you can look at this blocklist and you can something access and then you can sort of create the computation chains on the transactions, so there are a couple ways the access list can be used, and for any of them can be valid. What we are trying to say is that need for access list need to be included and for that, we will have to have an economical definition on how to serialize access list and how to hash them and in our proposal, we are saying that it can be as of now straightforward something as of now or hash it with 256 and have sort of have something you or I  encoding the constriction for something list. We are just civilizing it in a normal way or we are sort of forming a merkle tree out of it to hash but we are also saying you know we are saying two things what is the construction byte for hashing and what is the civilization format so civilization format could also be SSD and hashing could also be Merkel that is any way to go about, but the thing is that we have access path for authorization list for these access-list over the time without changing anything in the block list.

Piper:
* Yeah, so at a high level the details of serialization and hashing things like that are up for grabs, the general thing we’re going to propose here is putting this in a subsequent hard fork to get a new field into the header it represents the economical hash of this access list so that there is a mechanism for us to begin to start essentially experimenting with block witnesses at a verifiable level. So that’s the general gist not the upcoming hard fork i’d be looking at adding this after that hard fork to get a new header field for this. Anyone have feedback for this?


Martin:
* So if I’m correct it is not just about taking the access list and um collecting them into a big heap it’s about taking the generated access list that were found during this execution is that correct?

Piper:
* That is correct, yes, this is the referenced at 2930 is that we already have an access list format.

Martin:
* So my concern here is that something which is not explicitly spelled out is that you want to use this in some way to form verification for witnesses, what i think is problematic is in the rules of 2929 if you call something in that scope it accesses something then something else and it reverts out of that scope then that access list touch becomes undone so it doesn’t actually leave a footprint on the global access list, but if you want to execute this in a status way and use to generate global things as soon as you enter to this new scope which will revert you will find yourself in a  scenario where it makes an axis to which you would also have the data bc it wasn’t present in the global list and it becomes kinda hard to execute from that point on bc even though you can infer that yes, probably this goes over yes you can’t really verify it bc you don’t have all the data, I think that might be a problem with this.

Piper:
* So, I think maybe there’s a miscommunication here in my mental model of this construction, storage slots that were accessed in call frames that ended up reverting would need to be included in the access list.

Martin:
* Ah, but then you are talking either added a new type of global access or modifying an existing ones, which means that this would cannot utilize existing framework 2929.

Piper:
* Got it. That wasn’t clear to me so that is something we will have to dig into. How hard of a blocker is that for you? Is that significant?

Martin:
* It is actually significant--and the reason we made it this way, it could have been simpler to just have if someone tries to access something, or someone actually does, and it runs out of gas,and we just let it sit there, that would have been easier instead of having this journal. That means you could have called into something bc you already paid interest that could try to touch something else costing 2600 doesn’t have the gas for it 100 or something and it reverts back and now all of a sudden you only paid 100 gas but you called successfully made but you didn’t pay extra 2600 for call that failed but somehow you still have this other thing in the access list so that would have been a back door to put anything and access this stuff.

Piper: 
* Got it, so the naive approach to this would be to have a separate tracking for this. Anyways, this is just me solution-ing off the top of my head. Yeah, but I can see that this does not easily piggy-back on the existing framework so thanks for letting me know.

Micah:
* Yeah, do we need to add this to the block header or can we just add a key in the state route essentially?

Piper:
* I’m not following what you mean by that.

Martin:
* I think that is the proposal.I think Micah suggested that we just add the state route for that thing, is what you meant Piper.

Piper:
* Yes, I am not suggesting we add a big payload of data to the block header, I’m suggesting we add a 32-byte hash of some sort to the block header it represents economical serialized form of the access list so that out of banned somebody could receive an access 
list or a witness and from the witness can construct an access list and then from that verify that yes this is the access list for a specific block. Otherwise, you have creeping vectors if you start trying to build anything that really matters off of witnesses because right now you cant verify that is the witness until you actually do the execution. There is also a benefit to listing clients right now, if access lists become something that is circulated independently and clients prefetch these and create load  States and speed up execution of blocks.

Alexey:
* I have comment on this but it's a bit more general is that what I started to look at is you know with the Advent our access list previously  different rules for computation of gas cost for different operations which I never really liked, but now I'm still kind of how to how I would fix this and that is start writing it soon so we are trying to introduce them called  TEVM via is basically like a i version of EVM that would be would not have those things like self destruct list access list all sorts of other things which kind of goes on top. Which essentially is that if you look at EVM now, it has a sort of clear EVM and a certain number of resources: it's got stack, it's got memory, it's got IO, storage operations and that is fine. Those things are manipulated by op code but then on top of that you have a ever growing femoral structures which are also modified in the behavior and not really treated as source of EVM.For example,access list, self destruct list and now there's a proposal to have another one and there all different caches of state which affects the cost of the store. So my idea is to propose a different modification to the EVM in the form of TEVM which brings those femoral structures into the lights which means that assigns a specific resource is like I see it has associative memory which has its proper op codes to operate them rather than building them as kind of an add on to the logic. Actually have them cleanly implemented in the virtual machine. I know it's not a small project but I don't like those add ons. The more addons we bring the harder, the less cleanly specified it actually becomes. I have noted in some of my talks  last year most consensus issues are actually happening in these addons not in the EVM itself because these addons are harder to specify.

Piper:
* I don't think this has any effect on execution. There's no proposal in here that would modify execution in any way. This would be the result of the execution, so it's more like metadata about execution 

Alexey:
* So if it does not modify execution then Martin's comments about backdooring the access list  are invalid.

Piper:
* I think martins argument was that in our proposal we suggested that this framework was already in place with clients and what Martin wanted to find out was that what clients are doing is not sufficient for what we are wanting to do and so we can’t piggyback on top of that.

Alexey: 
* So in this case I agree if what you are suggesting is not in any way affecting the behavior of EVM then of course it's not an addon but it's simply something else that you are adding to the consensus field.

Piper:
* yes it is more akin to like the  bloom filter.

Micah: 
* The bloom filter does affect the EVM, so it's in the EVM that you have to record those metadata that you have to record as part of the EVM execution. So in your EVM module is where you're gathering the data and so I think that's where Alexey is getting at. Those types of add ons were adding stuff to the EVM execution and we are getting a lot of complexity issues from the clients.

Piper:
* Correct but this is overhead. This should have the complexity that things like , this doesn't affect gas prices, this doesn't affect execution. This is pure record keeping during execution and then afterward you serialize it , hash it and stick it in the header similarly to how you record bloom filter entries and stick them in the header. There was a question in chat but I lost it about why but i didn't see it.

Micah:
* It was probably mine. So I was just asking before I disconnected. I was asking why not include this in the state root. Have a well defined path that everyone knows. If you go to this path in the state root you will find the access list. Is there a situation where we would want to be able to validate the access list in a scenario where we do not have the ability to validate the state root?

Piper:
* Yes, so if you are fetching state on demand and you don't have that state. There is maybe an argument here that says if you can fetch data on demand then you can fetch state on demand. Suppose someone hands you a witness and you want to verify it that they didn't give you the wrong witness or that they didn't give you an extra or they're not griefing you in some way. Having the access list is a mechanism for verifying that it doesn't buddle the protocol to the witness format itself. That's kind of why we do the access list.

Micah:
* When that person hands you the witness bundle would it include a proof of the access list  along with all the proof of the state they are giving you right?

Piper: 
* So I will say that my preference towards the header is mere convenience but I recognize that changing the block header is complex and so I am willing to put that into whether we us SSC or do we use a tree to hash the access list. I am not married to one or the other . this is more about, I am curious if I am going to get resistance from this since we don't have statelessness. Do some one want to make the argument we shouldn't do this because we can't use it yet but my argument here is that we need to start using the stuff so that we can start understanding how we pass witnesses around and start being able to build things ahead of the ability to do formal protocol support statelessness. 

Tim: 
* so we just have a minute left so I guess it probably makes sense to move this conversation.

Piper:
* Totally we do not have to resolve this. I am glad I got to put this out for everyone and the link is out there so let me know what you think.

Micah:
* What channel?
 
Piper:
* Witness is a good one and R and D.

Tim:
* Cool, so just to summarize for the viewers the London stuff in case that was not in the recording. So we are updating the EIP1559 spec, we are going to start the new dev net Calaveras which will have the fix from 1559. Focus on that over the next two weeks have the client teams finish their implementations especially regarding the transaction pool and then in the next two week depending on how that went we can figure out about the public test net and when we want to fork those. That's about it. Thanks everyone for joining and I will see you in two weeks.

-------------------------------------------
## Attendees
- Martin Van Swende
- Micah Zoltu
- Tim Beiko
- Rai
- Trenton Van Epps
- Karim T.
- Gary Schulte
- Piper Merriam
- ECH-Pooja 
- Lightclient
- Ansgar Dietrichs
- Mikhial Kalinin
- o_O
- Marek Moraczyynski
- Artem V.
- Eugene D.
- Sunce86
- Alex Viasov
- Thomasz S
- Dankrad Feist
- Lucasz R.
- jochen
- Boris Petrov
- Alexey A
- Gary Schulte
- 11cyrpt
- Pamel B.
- Peter S
- Vitalik


---------------------------------------
## Next Meeting
June 11, 2021
