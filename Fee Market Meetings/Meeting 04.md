# EIP-1559 Implementers' Call 4 Notes
### Meeting Date/Time: Friday August 28, 2020, 15:00 UTC
### Meeting Duration: 1hr 50 mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/197)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=fI2IhcvuJA0)
### Moderator: Tim Beiko
### Notes: Pooja Ranjan

---

# Summary
## Decision & action items

* Change the spec and implementation to have a minimum increment or decrement of 1.
* Documenting the transaction pool issues and mitigation.
* Research and communication has to happen and that needs to be funded.
* Tim to connect with clients to get an estimate of a  reasonable amount of engineering work & funds needed if every client has a dedicated resource for 1559 as a top priority.  
 
---------



**Tim**: Good morning/evening depending on where you are. This is implementers' call 4 for EIP-1559. There are a couple things we've on the agenda to cover today. First up the status update and then the biggest part, the next steps to get this deployed on the mainnet, intermediate milestones to get there. There is also dicsussion of EIP-2718, and finally something that came up on Twitter about is there ways to speed up development by adding up more resources, if people have more thoughts/comments on that.

# 1. Status updates from implementers and researchers


Video | [01:00](https://youtu.be/fI2IhcvuJA0?t=60) 
-|-


**Tim**: First let's start with the updates. Anyone wants to jump in first, otherwise I can call on people. 

## GoEthereum 

**Ian**: I can go first, I don't have much to update really. This is Ian from Vulcanize, 
* working on the GoEthereum implementation. My role is to keep Geth implementation up to date and make any fixes and changes that needs to be incorporated based on the results of the testnet. 
* There have been minor bug fixes, besides, there are no major updates from my side.


## Besu 

**Abdel**: Abdel from Consensys working on Besu implementation. Pretty same as Ian said. 
* aligned with the latest specification
* did some bug fixes
* started testnet with 3 Geth and 3 Besu nodes
* trying to do performance test, sending high throughput of transactions and we found some issues, now fixed.
We think there might be some issue, we try to define the minimum value. Otherwise, it can be a problem. If we let it go to 1 or even 0, it can be problematic and it can maybe go up again.
We can discuss about that later. 

**Tim**: Yeah, we definetly come back to that. I see Barnabé is also on the call. Do you have an update?

**Barnabé**: not too much

* working on simulation
* a new notebook soon on strategic users
* trying to investigate when you have a sudden spike in demand and users are trying to upbeat each other
* trying to add more things to library to handle this case 
Giving a shout out to Fred, who is also joining. If you want to introduce yourself, Fred?

**Fred**: Hey! I'm Fred. I'm going to be helping out  (?) based model and implement other behaviors. I worked a bit with this, in a first price auction and now adopting my work towards the implementation of EIP-1559.

**Tim**:  Great and I see  Tomasz and Alexey,  you're also on the call. Are there any updates from either TurboGeth or Nethermind?

## TurboGeth
**Alexey**: No update from TurboGeth. I just came on the call just to see what's going on because there has been a lot of, I suppose misunderstandings, on Twitter specifically. I just wanted to see if anybody here would come to talk about it. 

**Tim**: That is the last bullet on the agenda, so hopefully we can get to that. 
Tomasz, any updates on your end?

## Nethermind
**Thomas**: Yeah sure.

* spending time on research side. Analyze and testing different numbers. making mistakes and finding some insights
* next 2-3 weeks, connecting to Besu Geth testnet for EIP-1559. It seems very reasonable prediction

**Tim**: Did I forget anyone else have an update they wanted to share?

**James**: Maybe we could do an update on the funding group.

**Tim**: Sure, do you want to go ahead James?

## Funding group
**James**: We did Gitcoin funding round and we had a lot of participation, awesome!
* Funds so far have gone to funding Ian's work on maintaining the Geth project 
* The other participants are funded through EF and Consensys.

**Tomasz**: Is there any transparency about how these funds are allocated?

**Tim**: For Gitcoin Grant, it’s public multisig, anybody can review it. We made it clear that we want to pay it for research and development of the EIP and not go to people employed by the EF and ConsenSys. That was kind of the high-level of transparency. In terms of transactions, the only one has gone to Vulcanize. Does that make sense?

**Tomasz**: Yeah, thank you!

**Tomasz**: There is one interesting thing that I’ve seen someone posting about some blockchain, Ethereum Research Foundation or something like this, posting information about funding the analysis mathematical and gave it to EIP-1559 with some mathematician from …

**Tim**: Yes, it's Tim Roughgarden is the researcher. He is not on the call today and so this was kind of a single individual who themselves funded this research effort. I think it's called [The Decentralization Foundation](https://twitter.com/d24nOrg/status/1296195184070234112). Basically, Tim’s background is in Computer Science and Game Theory and so he's going to work on doing a formal analysis at 1559 and comparing it to the current fee model on Ethereum today. Hopefully highlighting some potential improvements or some issues with the EIP.

**Tomasz**: This is very exciting and looks amazing. Will he work with Barnabe to get help because I think this work is somehow maybe like, they would probably help each other, because one side we have this mathematical analysis and the other side we have this running on simulations. 

**Barnabe**:  I don't know yet, I’ve been talking in the initial stage and we had a chat with Tim Beiko and Tim Roughgarden. I mean,  I think it is very complimentary. I know that he's also planning to publish some open source code, so I don't know how much will go into simulation but I want to maintain the line with him. 

**Tomasz**:  Right, sorry probably this is outside of the Agenda. 

**Tim**: No, no worries. I think it might be worth mentioning it. 

**Tim**: It might be worth just going back to the issue that Abdel was mentioning with the base fee on the testnet.  I just kind of more like on that. Abdel, you want to share more details on this?

**Abdel**: I was not there. Ian can you show more details about that? because if I remember correctly, you work on that?

**Ian**: So essentially with the current mechanism, if the BASE FEE gets down to 0 we can never go back above 0, that’s the hard cut off. There’s also a little bit of issue at low numbers above 0. For eg. at 1, the gas usage needs to be 9 times higher than the gas limit for the increase up to 2. From 2-3, it needs to be 5 times higher and so on so forth. It is some sort of function that I haven't actually figured out that describes the behavior.

**Vitalik**: That sounds about correct.  

**Abdel**: Should we define a safe minimum value, then?

**Vitalik**:  I think the thing that we did on the Eth2 implementation of 1559 is to just set the   minimum value to be either equal to quotient or twice the quotient. I guess twice the equation will be a bit safer. 


**Tim**: Because like one (?) [video](https://www.youtube.com/watch?v=fI2IhcvuJA0&feature=youtu.be&t=670) needs to be 9 times higher just because there's not enough block space. 

**Vitalik**: The other alternative of setting a minimum is setting in so that minimum change is 1 in either direction. So that if it is smaller, the target is, it always goes down by 1 and if it is higher, the target goes up by at least 1.   

**Ian**: I like that idea more but just intuitively.

**Tim**: And so that it means in the worst-case you kind of go from 1 to 2 to 3 and it takes you a couple blocks until it starts actually going up. it'll take you I guess a bit less than 10 blocks because then you'll be back to the 12.5% right?

**Vitalik**:  Right, exactly. It'll take you an extra 8 blocks but then they could going up from 8 to a billion or whatever it is going to take something like 100 blocks anyway, even longer to 200 blocks.

**Tim**: Micah has a question “How many blocks between 1 nanoeth to 0 assuming 100% empty blocks?” 

**Vitalik**: [video](https://youtu.be/fI2IhcvuJA0?t=750 )Going between 1 Gwei and each Gwei  has a factor of 125 million and 1 over it. I think that would be 148 blocks, that sound right? I'm sure give or take.

**Tim**: Yeah! So does anyone disagree with the idea of having like a minimum increment of 1?

**Danny**: Yeah, sounds reasonable. 

**Tim**: Ok Cool! **Let's make an action item to change the spec and implementation to have a minimum increment or decrement of 1**. 
Was that kind of the only outstanding issue on the testnet? I know there was like a transaction pool issue as well when we tried to put in a bunch of transactions? Did that gets resolved?

**Ian**: No I don't think it has, maybe we can speak to that. There is a branch that I pushed up today, hopefully fixes that issue. It’s likely due to a bug that I introduced to the last update. 

 **Abdel**: We will try with this branch and see if the issue is still there.

**Tim**: And those were kind of the two big issues, right? obviously that we’ve found so far.

**Abdel**: Yes!


# 2. Roll out plan


Video | [14:30](https://youtu.be/fI2IhcvuJA0?t=870) 
-|-


**Tim**: This leave nicely into the next agenda item which was what are the intermittent steps to get this eventually to the mainnet. **Right now there is this one kind of small private testnet which has 6 nodes on it. It's been pretty useful to find all these kinds of corner cases and small bugs but assuming like in the next week or two the spec gets a bit more stable and Nethermind is ready to join as well. Will the next step be kind of a more public testnet and if so  what do we want to get out of that?**

**Danny**: You mean on the public testnet side if so that people can begin to experiment on the wallet side? Is that  we want to get out of it or is it more technical betting and hoping for more randomness due to user activity?

**Tim**:  I would say that the 2nd. At least my perspective.

**Danny**: Cool! I mean that’s reasonable. I think that have spinning up. It's going to be hard to get people to just show up and send transactions that are like semi meaningful if it's non-existent testnet. But I wonder how they will?

**Tim**: I believe there was a miner on the chat who said they would be willing to supply hash power if it was a proof of work tesnet. Because the present testnet that Besu and Geth are working is a Clique testnet. So I think also testing the proof of work testnet is important part of this.

**Rick**:  I'm personally concerned that we just test the right code paths, so maybe we don't need competitive mining but we do want to test the actual code paths that would be used in production.

**Tim**: To be clear, by code paths you’re referring to do the proof of work that the mining wants, right?

**Rick**: Yeah.

**Tim**:  And I think that if you get like a small proof of work testnet, you’re kind of proving correctness. You know the EIP works is intended in a process of doing a non-proof of work and I think a step after that is then trying to go with testnet that has a larger existing state and seeing you know this performance degrade on that because Rick's the last time you brought this up on all core devs, I think that was the biggest piece of feedback that you got that it wasn’t clear client could process these large blocks especially with state access. So I feel like that would be step 3. 

**Step 1**: What we’ve now.

**Step 2**: An empty proof of work testnet.

**Step 3**: Maybe going to forward something like Ropsten where we can get an existing state and maybe get some tooling, get some tooling adapted EIP. Does that seem reasonable to people?

**Alexey**: Can I just ask a question here? Please excuse my ignorance but does the current implementation imply that the two transaction types that you point is co-exists? Or is the change to switch to the new transaction type? 
I suppose when this EIP is implemented, will all transaction have to have a new format or there will be possibility to the old type transaction to be sent as well?

**Abdel**: There will be a transition period, where both transactions are accepted during a certain number of blocks (800,000 blocks) ans gas pool available for legacy transactions will decrease on each block. 

**Alexey**: Okay.

**Tim**: One thing that is nice is because you have 2x blocksize even when it's 50-50 you'll still be able to deploy a contract that would say pick up a full block today because you'll just fill half the block with your legacy transaction or your 1559 transaction. so we're also, even though you split the available blocks space in half between the types of transactions, you're not actually decreasing the max block size that someone can use.

**Alexey**: So based on your experience with the implementation so far, where is the kind of biggest complexity in terms of the code lies? In which part of the code?

**Abdel**:  Personally I would say maybe the handling of different RLP encoding decoding based on the transaction because we don’t have typed transaction envelope but if we make it a requirement for this EIp, I think it will become easier but yeah, to me it has been pain point of this implementation is about encoding-decoding of different types of transactions.

**Ian**: I am also a big proponent for 2718 but for the Geth implementation, I’d say the less complicated area is the mempool, the transaction pool more accurately. 

**Alexey**: Are the rules of the transaction pool very different for this EIP than for the existing transactions.

**Ian**: No, not really. Actually you’re just comparing the gas prices between the two types of transactions but the gas prices derived from the base fee and fee cap for gas premium in the case of EIP-1559 transaction, so it's it's just a different process of arriving at that value. 

**Danny**: The complexity in the transaction  mempool because you then have two transaction mempools with different logic or because it’s altered in new logic?

**Ian**: Actually the latter. **It’s actually the single mempool right now ordering them all based on the gas price and we do need to update the implementation to rebase on top of 1.919 which adds the deterministic ordering when two transactions have the same gas price.**


**Alexey**: okay so the reason i was asking this question is because my suspicion was that the most complexity would be in the implementation of the transaction pool and therefore when you're previously asked the question like what would be the you know what needs to happen for this to go into the mainnet i think one of the main things to basically preempt any possible questions or problems that would arise with this particular implementation. For example you know is this a code resilient towards any kind of dos attacks and then tick that box yes it is because of such and such and such you know. Like could we do any stress testing on this and such and such so basically yeah so I think that would help a lot because then you go into the uh let's say go ethereum developers and you'll say these are the things that we're preempting or the most of the questions you're going to be asking.

**Ian**: yeah that makes sense and I think you know if we roll 2718 of which we may be getting ahead of ourselves because I think that's the next item on the agenda. If we decide to implement that first that kind of introduces some uncertainty into the you know unlimited uncertainty into the mempool and that there's no real clear defined way to order transactions between all these arbitrary types.

**Tim**: Interesting so it's like on one hand 2718 helps with the rlp encoding stuff and makes the trend transactions easier to manage but then yeah if it makes a transaction pool which is the other most complicated bit more complicated it's not clear it's a like net win?

**Abdel**:  But we can say that maybe the transaction pool is a bigger problem than the RLP, we can deal with that. This is not clean but yeah we can deal with that.

**Rick**: Yeah I just think it's a little underspecified where it's at right now for what we're trying to do. So I think that the spec needs to be cleaned up a little bit in order for us or completed frankly in order for us to really start talking about how it would Impact the work that we're doing uh to Georgios's point as well.

**Tim**: Yeah there's a couple comments in the chat i'll just read them so people not on the zoom call can see but Georgios says that uh 2718 seems to generalize uh do we really want oh is it important to bundle this with 1559 you could add an optional version field if present and set it to v2 and decode it as 1559 transaction otherwise it defaults to the current format.
Micah  says 1559 is one of the transaction types that you want uh and there's a question about whether we need a generalized versioning scheme for transaction um and 2718 isn't just 1559 transaction there's  a bunch of other transaction types that people are proposing.
So given i guess yeah that's like the transaction pool is kind of the most complicated bit on the Geth side so far, does it make sense to try and Maybe just like specify that somewhere else in the code so that I don't know if the EIP is the right place for it but uh just so like like i said we can kind of proactively address some of the objections around it.


**Abdel**: But transaction ordering is not a consensus thing.

**Tim**: Yeah i know but at least just saying this is how we did it and kind of explaining that not as like it's something people have to conform just as something people can kind of critique 

**James**: And it should be added to security considerations in the eip

**Tim**: yeah that's a good point so yeah maybe just adding something about the transaction pool ordering in the security consideration section and why like you know the potential issues can be mitigated.

**James**: And although as part of the specification it in this strict eip sense it isn't as important in the inclusion in a hard fork it's really important for that discussion uh that might happen more as those kind of processes are separating in a different place i'm hoping my audio is better than it was.

**Tim**:  It is.

**James**: Okay good! I'm just starting to think of it as not just the eip specification but how do we get this through the hard proposal.

**Alexey**:  And in another comment I wanted to make about this transition period, there is some kind of number: was it 800 sort of blocks or something or eight thousand blocks?

**Tim**: 800,000

**Alexey**: 800,000 blocks okay and so where does this number come from ? Where is it coming from?

**Danny**:  4 months time for ballots to adapt and change.

**Alexey**y**:  This is it actually. is this going to be okay or would we need to have another emergency hard fork to postpone this because that's how I think it's going to happen?

**rick**: Yeah so I think that I mean Alexey you bring up a very salient point. Yeah I think that we need to be prepared for a series, multiple hard forks based on what happens when we don't see sufficient transition from wallet providers, exchanges and what have you and consequently we don't see the shift in transaction volume. I think that's to me that is one of the biggest to me that's the biggest risk because we can all as engineers or you know have these conversations about these engineering problems but we can find a path to engineering problems what do we do if if like you know Omisego just doesn't change their transaction type and they have Tether you know i think that's a pretty big issue. 

**Alexey**: So originally when I remember in when we met in 2019, I think was it when we discussed this in Berlin, so I suggested basically the dual transaction types and one of the reasons I did that is because we could monitor the uptake of the second transaction type and based on this information to inform when the transition period needs to end because what we really want to see is that the number of the new type transaction increasing the number of old type transactions decreasing and then when it gets to a certain threshold we just say okay fine now we're going to make that mandatory. I don't know, do you think it's sensible or maybe some fundamental issue that makes it a bad idea?

**Rick**: I think there's a psychological component. I think that there needs to be a hard number and a legitimate threat to motivate people. You have to have a carrot and a stick frankly. So way back when this the stick was going to hard fork and the carrot was lower gas costs and in the new transaction type, over time that lower gas cost narrative you know people didn't like that idea which is fine with me and so this is we're still trying to figure that out.

**Alexey**:  But this is actually quite an interesting point. Let's say that if we had two transaction pools I mean basically two spaces inside the block. One space dedicated to let's say they're equal in size right or in gas sort of limit and one part can only take the transaction of the new type and another part you can take the transaction of old type and then with everything else being equal if we can see that the users of the first type actually have a benefit that was promised by this eip then you can say that look these are the transactions in this pool and they are actually benefiting because they have all sorts of benefits that people are promising if that doesn't happen that maybe there is something wrong with it maybe the modeling wasn't correct.

**Barnabe**: But this assumes that the benefits will come even if users have a choice  between first price auction and eip 1559. like it's not clear that uh given the choice between the old transaction and the new transaction, I might want to choose the old transaction Sometimes but if I didn't have a choice, you see what I mean like there's not necessarily like an equilibrium where both transactions are working at the same time there could be interactions between the two.

**Alexey**:  No but this is actually going to be an experiment because essentially you can look at this as two different blockchains running with two different rules but we are basically just combining them in one block chain.

**Barnabe**: That's interesting because you're testing both groups on the same blockchain so at the end of the day there's going to be interactions based on the gas price right?

**Alexey**: No that's that's true but don't you think that model should win even in that case or does it depend on some sort of uh coercion that you have to force everybody to stick with the new rules?


**Barnabe**: Like it might win but it might not as well. It's not clear to me that in the presence of let's say 1559 the first price auction is an unstable equilibrium where little by little you see people migrating to a different format and you might have interaction between the two and I agree with Rick. I think unless you have some sort of psychological deadline where okay that's it if you don't have a space to do it then you avoid being in this equilibrium in the first place. But it's an interesting question actually like if there are interactions between the two like what does the film market look like even for the transition period like it could help sort of anticipate what will happen during these 800,000 blocks or however many.

**Alexey**:  Yeah I just saw a question from Micah that he said that the issue is that tools the developers don't have the same incentive as users. We need metamask tether and etc to update since the users can't update without them. So, yes, I thought about it just now. Given the fact that this EIP has such a wide well wide support, you would think that basically support from the wallets and stuff would actually be a competitive advantage. However if uh the if the basically the benefits are so weak that we're not even sure that this this sort of eip is going to win against the status quo then is it really is it really good?

**James**: Even if the first one isn't the benefits being so weak i don't think is the only explanation for what could happen like the interactions of the two could be complicated and then also just people not  like the stickiness of the way that things have been done. So, I  don't think it's fair to say that because there are other reasonable explanations besides they're not seeing the benefit.

**Tim**:  But is it like one of the carrots here kind of block space inclusion, right? So if you have this 800 000 transition period, at 400 000 blocks you go 50 50 and then under 400 000 it means more than 50 % of the block space is for 1559 transactions and at some point the benefit is like well if you want the large number of transactions included in the block without raising the base fee then you kind of need to support 1559 style transactions. And then this is kind of where large applications like a coinbase or Tether or something else and you actually have a significant amount of on-chain volume you have a really strong incentive to use that block space and then the first person to use like it kind of creates a race like you want to be the first person  to access that block space so you implement it first. yeah because otherwise I guess after you know the 800 000 block period it's like if you didn't implement this change you can't send transactions to the chain, which seems like a pretty big distance.

**Alexey**: I mean one of the kind of ways to probably address this. I don't know if this does the EIP1559 fixes the maximum block dust limit or does it not ?

**Ian**: It no longer does; it's just using the miner set limit now.

**Alexey**:  Okay so what if you essentially fix the old style block cast limit like forever and then or maybe just make it so that you can only be reduced but you allocate all future gas block increases to the new transaction type and this in this situation whenever there is a increase in block size limit it only increases it for the eip 1559, which means that the people who did not upgrade they still have a functionality but they will have to cram into much smaller space and so that actually probably is going to be enough incentive for people to migrate.

**Rick**: This is my original suggestion was that we overt almost exactly verbatim what you just said. I think the complexity of the conversation sort of put people off from that but if we're coming back to it i'm very strongly in favor of it.

**Danny**: Increases or shifts in distribution ?

**Alexey**: Increase 

**Vitalik**: I think we do want to retire the old version at some points like in general the protocol can't just kind of keep on including increasing complexity by adding new types of things forever without removing old things, right? So,  it's just a question of you know is it four months or eight or twelve or whatever amount.

**Alesexy**:  I mean you can but what i'm saying is that  we you could do these decisions with having some data because we what I don't want to do is that make all decisions before we even know what's going to happen so we can first say that yeah we can say that now we're going to fix the the old old block size and then we're going to reserve all future increases for the new ones and then we look back into six months and say okay what happened, did anybody still use the old type and if not then we say okay we're just doing a ditch it or something like that.

**Danny**:  So one I don't know if we're advocating, anyone's advocating for block size increases right now and so I don't know if there's like much room to grow there. Two I mean if there's two distinct spaces of block space they both will be used because there's going there will be sufficient demand regardless of the fee structure to use both of them. so I don't think you're going to see like the pre-1559 half or portion just kind of die because blocks space to block space to a certain extent.

**James**: And another thing to think about it would be nice if the two markets were actually separated. But what will happen in practice is we have the standard market or the legacy market and then we have the 1559 market and if they exist at the same time, there's a supermarket that encompasses both of them of people being able to play against them or not against them.

**Alexey**:  But actually this is going to be great because that means that people have implemented the new transaction type. The fact that they're going to be arbitraging it.

**James**: Yeah but  that will make the one being adopted versus the other information not as useful because you're not seeing you're not seeing the adoption you're seeing the result of you of the both markets existing at once and then playing against each other.
**Alexey**:  No what i'm saying is that what it is not possible for a third party to modify let's say if I send the old style Transaction it's not possible for the third party to trustlessly modify my transactions into the upgraded into EIP1559, it has to be me to create that transaction in the first place. So the only people who can arbitrage this are the people who create transactions and if they do that it means that they've already upgraded they can already send the second transaction type. So I don't see it as a bad issue.

**Rick**: yeah so the way that I envisioned it Originally was that 1559 transactions always happen first. So you double the total gas limit and then you basically make like a sort of like a special block if you want to think of it like a the block you know that much bigger block that double block is split in whatever ratio and 1559  transactions always come in first and then they're ordered uh based on gas price and then the old transactions are ordered after that. So if you're in some sort of auction, if you're one of these users that's a you know using so much of the of the gas or what have you um you're going to want to switch to1559 because you're you're always going to beat who's ever in the traditional transaction type.

**Vitalik**:  So another possible idea would be that if we want old-style transactions to continue being valid forever then we Just make it valid to include them as being part of the 1559 space and we would just like map the gas price to be into the max gas price and like say just set the bribe to like some standard group five way or whatever. It's a bit ugly but you know.

**Tim**: Well does anybody want to have those transactions valid forever?

**Alexey**: No, I don't think.

**Vitalik**: Yeah and the idea would be that at least we would be able to retire the old like basically everything about the old rules except for the format and like we can retire the format later.

**Alexey**:  I think what I suggest is to basically do at least two hard forks. In the first hard fork we do what I just suggested and then once we get some more information let's say in six months time we if we see that the adoption is happening, like people are really migrating and then we can say okay after that we introduce the linear sort of shift of the ratio down to zero so over a period of time the ratio is just simply going to drop to zero of the old transaction type. I  basically suggest not to introduce this uh kind of cliff edge moment right now but introduce it after we've seen what happened.

**Tim**: Then there's no incentive for people to adopt 1559 in the first hard fork, right?

**Rick**:  Well it would only be carrying.

**Vitalik**: If nobody adopts the 1559 then the base fee on 1559 that'll be tiny and they're all well and there will just be this space ready for people to claim it, right? Like the economic equilibrium is basically that the ratio of adoption is the same as the ratio of the gas elements of the two spaces.

**Danny**:  Right if you allocate some portion 1559 it will be adopted by somebody because block space is in high demand.

**Alexey**:  Oh yeah if that is happening then this is good data to say okay after this we're going to just go do the kind of cliffhanger not cliff edge but basically gradual reduction of the other option.

**Danny**: Or another option is have the gradual reduction start 400 000 blocks in because at that point you can have an emergency hardfork turned off if nobody's been using the other half, but otherwise you don't have to schedule a multiple hardfork.

**Rick**:  Yes i was going to suggest something similar to that so yeah I agree with that.

**Alexey**:  I understand, now Micah is saying that we are consuming too much time on the call but I think it's probably worth talking about it because it will make the rollout easier or harder.

**Tim**:  Yeah and I think personally i'm in favor of something that doesn't absolutely require a second hard fork because so this idea of like having the the transition period only kick in halfway through I think it's nice because it gives you know more warning although there will be warning by this being deployed on test nets right like if you look at the the whole process um but what's nice with having this transition period in the first ep it means that at some point it goes to zero, worst case we have an emergency hard fork to push it back but if it does reach kind of zero block space for all transactions then the second hard fork is really optional it's like do we want to do this to clean up the protocol and make it simpler um but if for whatever reason like we don't want to do another hard fork on Eth1 or something like that, we kind of don't have to.

**James**: I understand the uh trepidation towards, it looks like someone relying on an emergency hardfork we needed it but I would tend to the if we were able to do something and then say hey we can do something if we really need it versus we have to push something we have to push this six months to nine months further back that the preference of the community would be we have and we can have an emergency fork. They would rather have us move forward.

**Alexey**: well this is more uh I think this is I guess a bit more philosophical question about I  mean my personal view that it should be a matter of principle that if you don't do it don't touch it, just keep working. You don't have to rely on something happening in the future but you know other people have different opinions than that.

**Tim**:  Just to make sure I understand this, what would be the advantage of having the kind of transition period only kick in halfway rather than linear over the whole time, right?

 Are we just saying we give more today because another way to achieve that is like you literally plan the hard forks two months later.

**Rick**:  It's psychological I mean  it's a game of chicken right I mean we have to tell people we're going to drive off the cliff or else they're not going to do anything.

**Tim**:  Yeah that's what i'm thinking as well. So, I’m kind of in favor of just having the transition period over the whole, you know, to go from a 100% old transaction to 99-98 rather than just giving this kind of I don't know 400 000 blocks of slack  which we can get by just delaying the hard fork 400 000 blocks.

**rick**:  I think it's a question of, we have this evaluation inflection point,  that I think is very difficult I think Alexey, it's a good idea that Alexey is suggesting that we that we have this point where we as a community make a decision and decide which way do we go and i think that again from almost like a game theory perspective what we have to say is okay we've started the car going towards the cliff and now we can like turn the wheel but we have to turn the wheel to like stop from going off the cliff or we do nothing at 400 000 blocks and we continue to go off the cliff so it's like that kind of game.

**Tim**:  Yeah yeah okay that makes sense. And is there a way we can get you know some preliminary data on that right like obviously if it's live on the network then people can start can start kind of playing around with it, yeah I don't know, like what's you know is there a way to test this before we get the mainnet basically?

**Barnabe**:  Has anybody looked at filecoin yet like the data that we have already well the problem with that is every other example is someone implementing something where they don't they don't have you know billions of dollars literally running on an old transaction type and they need to switch to a new transaction type I mean for us there's two separate problems right there's the mechanism there's the new set of mechanisms of 1559  which I think can be verified and reasoned about and are not that you know that's a pretty well-defined problem and it looks like other teams have sort of taken this what we've started here and gone off and implemented that and I  think that's fine and then and I think that's pretty like well-defined and then there's the fact that we have to have a transition period because we so many existing users that other chains obviously don't have and  it's that transition period that really changes the conversation and is what gets lost on people is that there's there's a social problem that we have that other teams simply don't have.

**Alexey**:  Yes and also you have to project, I mean we could obviously all argue that yeah yes we're gonna just give them a big stick at the end and then  everybody has to migrate within 800 000 blocks. But it's sort of like you have to be a cooperative towards uh basically everybody else um and uh it's reasonable uh to introduce this and then they say we're going to do another valuation and decide how quick the remainder of the transition should be. Because we might find that in four months time everybody migrated and we're just going to say oh let's just turn the old thing off or if we see that the migration happens slower.The the new transaction types is taking on but like there is it takes a bit of time, we can say okay let's just do it over next year or something and we're gonna program the linear function to to slope down.

**James**:  there's also a risk of, the idea of getting data to then support, the decisions on how to turn off or down is great. I still am not sure that the data that we'll get is going to be very easily digestible because it is the union of two markets.

**Alexey**: It will be clearly visible how many transactions of the new type got into the block and how many transactions of the old type go in the block. You can chart it and make a little chart out of it. I don't know why it wouldn't be clear.

**Barnabe**”  But if both markets end up having the same gas price which they should, people are arbitraging, you should expect that both would be filled to capacity right?

**Alexey**:  Yeah that means,  it's a great result . you mean that there is adoption of the new type. You can also see, with some analysis,  you can probably identify kind of the where the transactions are coming to and from,  like what web like at the moment you have like a lot of websites which uh inject transactions for users like all the uh whatever you will have,  like a you know lending websites and stuff like that. So what they do there they can just connect to your ledger wallet or what have you and then create a transaction for you to inject them blah blah. And so you can see how many of these actually transitioned uh but then because you know a lot of transactions will be going into this contract and so forth there could be some way of estimating you know whether the adoption is going on or is it just arbitraging happening.

**Barnabe**: Yeah I mean assume that the 1559 pool is empty but then base fee should go towards zero and then it will be very quickly like full again. at least until the gas price in both pools are the same right? Like the problem is that you don't really have a counterfactual if you have both things living at the same time that you'll have yeah you were mentioning like a testing but that's not really what you have because you constantly have this interaction between the markets in the gas price, right?

**Alexey**:  No but as I said before the  arbitrage actually does require you to upgrade that's what i'm saying.

**Barnabe**:  Yeah but I’m sure people will have good reasons to upgrade the base fees.

**Alexey**:  Exactly okay so if everybody upload charges that's already a great result that everybody upgraded to the new format type.

**James**: But that won't show us who hasn't upgraded.

**Rick**: Well yes it won't show us who hasn't upgraded and i'm and i'd like to point out that given the current realities of the chain, you know the users the actual humans who uh tweet and use discord are not the largest gas consumers, right? The gas consumption is not really indicative, it doesn't map. You know there's heavy gas users there are people using a hundred of  thousand times as much gas as other people and so those people are obviously going to be optimizing and arbitrating. I mean there are gas arbiters who exist in the market today.

They will be doing this price manipulation not end users and it doesn't matter if there are these gas manipulators out there manipulating the price even if it's to our mechanistic benefit if metamask doesn't support our change for example.

**Barnabe**: Yeah I agree with that, I think we don't really see like the iceberg of transactions on the chain yeah.

**Alexey**:  I mean if you look at the gas consumption right now, so number one is probably Uniswap, right? Uniswap would be one of the first people to upgrade I'm pretty sure.

**Rick**: Yes I think we could get them to upgrade and I think that is sort of the conversation as well. Can we get Uniswap to upgrade? Can we get Metamask to upgrade? Can we get Etherscan to upgrade? Can we get Coinbase to upgrade? If we can get these different community members to upgrade, if we have a process for engaging them, then we can really lower, I mean we can talk about this risk from a mechanism perspective until we're blue in the face but at the end of the day someone has to go talk to someone and make sure that they're switching.

**Alexey**: Well actually Micah said that the 90% Uniswap are bots but that's actually it's fine because the bots will also upgrade pretty much.

**Tim**:  And just one thing I'm not sure I understand. So if you don't have a transition period, how do you split the block size? Do you just say, you know the gas limit is x and whatever type of transactions go in and there's no carrot or stick it's just you can send either type and one block can be 99% 1559 transaction and the other can be you know whatever percent?

**Rick**:  I've never seen that proposal explicitly. I think I understand your question but I don't know that anyone has ever proposed what you're describing so I'm not sure how they imagine it to work.

**Tim**:  Yeah but basically what we're talking about right now right if you remove this transition period  to see what happens on the chain how do you actually, allow that, right?

**James**:  You just have two buckets and then leave them as buckets and then say have fun.

**Tim**:  Yeah exactly but then for example how do you calculate the base fee? Do you take into account normal transactions to calculate the base fee? You obviously can't do that because then you're kind of know removing this incentive to use 1559 style transactions. I know maybe it's something I'm not understanding well but..

**Alexey**:  You just treat them as two different sorts of pools and you look at them as two different blockchains I think in a way.

**Tim**:  Yeah i know it seems to me like maybe this actually adds complexity to the EIP, whereas having the separate like clean buckets makes it simpler but i'm not sure if that's just from a high level.

**Rick**:  My intuition is that you have to have two very clear buckets and if you don't do that it just doesn't work.

**Tim**: Okay got it, yeah that's what i'm thinking as well and then in the chat there's a couple comments that say, you just leave it 50 50 and defend it like forever but the challenge there is that's actually more aggressive than the current proposal because the current proposal starts at like 0% 1559 and then gradually you know gets to 50-50. oh the current proposal starts at 50-50?

**Rick**:  Well it doubles the block size and starts at 50-50. 

**Tim**:  Got it.  

**Alexey**: Yeah so there's basically, there's an immediate boost in terms of block gas limit after the hardfork.

**Tim**: Yeah yeah, I thought it doubled the block size and started at 100-0, sorry that's my bad because if you did that, if you doubled the block size start at still 100 % legacy transaction and over time allow more 1559 transaction, then you get to this 50- 50 spot midway through the transition.

**Rick**: Right and the the other option,  I mean I think that there is this sort of desire for engineering parsimony and I'm sorry I can't read the chat and listen at the same time but uh you know, but I appreciate the desire for engineering parsimony,  where you don't increase the block size  and then what would have to happen is you'd have to ramp in 1559 and then ramp down the classic transactions, which would basically be throttling potential 1559 adoption which we don't want to do which is why we **double the blocks size**.

**Tim**:  Got it,  yeah yeah. So it's kind of circling back to Alexey’s proposal of just leaving it at 50-50 until we get more data on the chain. The strongest objection to that is basically that it doesn't create an incentive for people to switch but if people already kind of want to support this we'll see how much organic interest there is for it,  right?

**Alexey**:  I think it will, it isn't correct to say that there is no incentive to switch because **if you did create this extra new bucket which is the same as the current one, anybody who hasn't migrated they are actually sort of using only half of the space that could be using. So like all the new smart people who are implemented the 1559 will be using the new new bucket while it's still empty**.

**Rick**:  Yes I also think that making sure that 1559 transactions simply happen first is a huge huge huge incentive that will cause many bots to go to apply it, as well as uh exchanges in any number of people.

**Barnabe**:  And my objection to Alexey’s proposal is more that the data won't be able to tell us that 1559 was adopted or not because of the lack of counterfactual so we could set up some kind of experiment but this is not one that would tell us uh what we want to know, like there's no way to interpret the data in a sense of who  people prefer 1559 to the old style transaction.

**Rick**:  So I think that's super important to keep in mind. I appreciate the technical point there but  that the evaluation that has to happen just necessarily because of what you're saying is social. You can't, there is no data on chain that you're going to look at that's going to answer this question for you, which is in part why we need to have this thing that Alexey is talking about. If we could just use on-chain data then we wouldn't need to give this social decision point but because there is this large social component to the problem we have to create this decision point where we will not have enough data. I mean well where we can't say positively that the experiment will give us sufficient data. We have to run the experiment at this inflection point and then see what happens in the community and actually go out and do the analysis by talking to people,  as opposed to looking at what's going on chain.

**Barnabe**:  Okay yeah I can agree with this. yeah yeah this is fine.

**James**: My objection is that there will be people that will adopt 1559 because there will be low gas and those early adopters will just run for it. There is a large group of people that are slow and won't adapt without some kind of hard limit, in the end. If there's an option to keep doing 1559, there are people that will just keep doing it. If there's the option to do standard transactions, there'll be a large long tail of people that don't support it unless there is some kind of hard deadline.

**Tim**:  And then yeah just for I guess completeness Micah had a couple comments in the chat saying his objection to an excise proposal is that he doesn't think we'll see we'll get any usable data from that change that there's not a scenario where we don't see both bucket fills under other than Ethereum usage going to zero and then what's the objection to just be willing to hard fork away if we see people not adopting?

**Rick**:  I think we just got some time. I'm not sure I understand Micah's point completely. I think that Alexey’s point sort of encompasses both of those responses.  I mean we have to set a time so that we can say okay we should expect a hard fork here to incentivize people to be prepared and just give people notice. 

**Alexey**: I mean from my point of view, it goes back to our disagreements about let's say difficulty bomb. Because I see the approach with the difficulty bomb actually mirrors what has been baked into this current EIP-1559 proposal is essentially this what is kind of insecurity over the developers, that you know we have to always kind of in embed some sort of threat or cliff edge, just in case that people don't do what we want. Instead of saying yeah we have a clear roadmap this is what we're going to do and we are basically secure. We know what we're doing and we are going to do what we're going to do and you just basically. If you're with us you're with us. We don't have to threaten you and that's kind of my approach to this and so I don't like creating threats in the future that if you don't do this, this is going to be hardfork and it's going to kill you or something like that.

**Rick**:  I think the difficulty bomb is a great example because I think that what the difficulty bomb has actually demonstrated is that we make empty threats, right? I mean, to your point  I personally believe we should be making threats but they should be legitimate threats not empty threats.  So if we aren't going to commit to actually doing the thing to your point  and I guess and that's also sort of an interesting again psychological difference like are we threatening people or are we just saying that you know, as the operators of some level as the as the architects of the system, collectively the architects are telling you this is imperative and it must happen and so the the architects are going to do everything they can to make it happen be prepared or are we going to as architects capitulate to people who we all sort of collectively believe are actually making things worse for everyone else probably out of more incompetence than malice. I think that to your opponent Alexey,  there's a deep philosophical discussion that we have to answer here and I think that the difficulty bomb has actually set a precedent of the EF says that something's gonna happen and then it doesn't happen and that's what I think we have to fight against.

**Alexey**:  Yeah so to summarize this basically if we say that okay it's gonna happen in 800,000 blocks everybody understands that if people didn't have time to upgrade we're just going to emergency hardfork. Everybody knows that and therefore I agree this is a completely empty threat because it doesn't serve any purpose. It just basically creates more work for us. Everybody knows that if somebody puts the pressure on and says oh we didn't migrate you're going to kill Ethereum, we're going to do an emergency hardfork and it's also going to look quite bad.

**James**: Well when I'm thinking about it this way, just so I can clear for myself. I am confident that there are people that will wait for the last one to upgrade. You've seen this with every hardfork and every deployment, so there will be people.

**Alexey**: So, you need to wait, that they are in the minority and then you can basically get through with it. So you have to make sure that your threats are not empty threats, that's what Rick was saying. 

**Tim**: Assuming this is not an empty threat, what's the worst that happens you know if uh we just put in the transition from the start? Right, we get to the point where there's no more space for old transactions, obviously some amount of altruistic or smart  incentivized people have upgraded to 1559, there are some people who are kind of stuck at that point and they can't do anything until they upgrade. How big of a group that is and what's the impact on them?

**Rick**: It depends on who they are. If someone on this call just sort of like you know grits their teeth and provides the fork to metamask if someone goes out and talks to uniswap if someone goes out and talks to these important you know these people and make sure that they actually hands them the patch, then you know maybe there are a bunch of scrap stragglers that are irrelevant. I think it's really hard to say you know we have to take a strategy that's much softer,  again to Alexey’s point, I think **we have to just be willing to go out and talk to people and make the change as opposed to sort of decreeing it from on high and hoping that people then listen to our decree**.

**Tim**: And when you say make the change, I think it's possible to reach out to people right like James has done it for the hardforks,  the CatHerders have done it, i'm happy to help with that as well. It gets obviously harder if we have to implement it for coinbase and for metamask or whatnot, so what do you see as the best or most effective path there ?

**Rick**: Well yeah I usually stop thinking about this problem, at right where you ask this question but I think we will actually have to be providing forks. When I say we,  I mean I think that anyone who wants to see 1559 implemented and has the means and is on this call also needs to be willing to go out and talk to  implementer you know implementers of auxiliary services to make sure that they implement it as well. You can't just talk to us here and and think that you're gonna accomplish your goal, you're not.

**Tim**:  Yeah so that's definitely something we can do like before the next call is just like reach out to various you know large users of the chain and or you know both individual large users and like kind of gateways for a lot to small users like folks like metamask and and exchanges and whatnot  and just kind of gauge where they're at regarding this ? And that would give us some preliminary data around what they think is the biggest hurdle, how realistic it is, how much advance notice you know they need?

**James**: That might be worth looking at funding some of that outreach. Cause it's just a lot more work than I think people realize and having done this with hardfork,  it is a very high touch to even get a rough spawn.

**Tim**:  Got it.

**James**:  Which translates into that's a lot of man hours to be able to do.

**Tim**:  Yeah yeah and just yet to be mindful of time, maybe that's something we can take offline and James. I'm happy to follow up with you and Rick also or anyone who has thoughts about this.

**James**: Yeah, that's a good call.

**Tim**: Okay great so just **coming back to the actual implementations then, what do we see as the biggest blocker now?** I don't think we have enough data to make like a big change to the spec. If we assume that what we had was good you know was kind of the good conceptual thing, it seemed like the **documenting better the transaction pool issues and mitigation was one big action item**. **What are the other things that we can be working on to move this forward?**

**Ian**: **Implementer-wise the only other thing that I've picked up is to update the spec so that the base fee is only incremented a minimum of 1**. 

**Tim**:  **Is there value in going and doing test nets, you know beyond what we have now? Does anyone see value in that or do we think that we kind of need this answer to the large users before we do any of that?**

**James**:  I see some value in having a more public testnet that we put a bounty on breaking the mempool.

**Rick**:  Yeah I think we should do both at the same time. I think we should continue forward with the testnets until we get up to like a Ropsten level test net because I think that we're going to need that anyway to demonstrate seriousness and commitment and for other reasons as well.

**Alexey**: Yeah, so I also wanted to say that there are these test nets which basically tend to be nexus of activity, like say at the moment that Rinkeby that was (?) [video](https://youtu.be/fI2IhcvuJA0?t=4393) before where you can actually see serious action going on in terms of like number of transaction people deploying all sorts of stuff there and so it would be good i mean if it's possible to get that kind of network to be running on this change to just show that it's actually working.

**Tim**: Yeah and I feel like that's really valuable but it's maybe like a step ahead? Is there value to having like a smaller public testnet before forking one of the larger ones?

**Rick**:  Yeah I think we should have a **phased approach**.

**Tim**: Okay!

**James**: And then the step after Rick just said would be to get it into a YOLO style testnet and then the step after that put it into Ropsten.

**Tim**:  Yeah so right now we're kind of like that pre-YOLO step. I think over the next couple weeks we can do a sort of 1559 style YOLO testnet. The question here is do we want it to be a proof of work test net? It seemed like yes based on testing all the code paths, does anyone have like a strong objection to that?

**James**:  I'd say yes!

**Tim**:  Okay, cool ! So proof of work kind of early testnet. Is there anything else? **It seems like there's definitely like a month or so of work and we can have another call after that but like 

- just reaching out to the large users, 

- having the spec updates and 

- just the clarification for the transaction pools and 

- the increments setting up a testnet and 

- then obviously there's all the research Barnabe and Tim Roughgarden are working on as well in parallel is anything else missing from this? Okay!

**James**:  I think that's good until next time and then after that stage then it's getting more clients to adopt but we don't want to do that yet, so that's good for now. 



# 3. EIP-2718 (see [comment](https://github.com/ethereum/pm/issues/197#issuecomment-675805644))


Video | [75:35](https://youtu.be/fI2IhcvuJA0?t=4535) 
-|-

**Tim**:  Micah said 2718 is also like a thing you should be thinking about. 

**James**: This is probably just a throwing out there in the air question. Does anyone have a sense for how long it would take to get the transaction envelope EIP into a yolo testnet?

**Tim**:  Basically, I didn't get like the current implementations, right?

**James**: Yeah, how long would it take for us to get implementations or things into the point that we could deploy it as part of a YOLO?

**Ian**:  As part of it, would it include eip-1559 or would it be on the base?

**James**:  No it would just be the transaction.

**Alexey**: What is YOLO?

**James**: That’s the testnet that Peter and the GoEthereum team has made. 

**Alexey**: Oh okay!

**James**:  That's what they're using for integration testing.

**Tim**:  Basically a pre-testnet.

(There’s a blog [YOLO: An ephemeral test network for Ethereum](https://medium.com/ethereum-cat-herders/yolo-an-ephemeral-test-network-for-ethereum-356d43179b1a) on the Ethereum Cat Herders Medium)

**Ian**:  I think it would take about a week or two, if that was my focus to get that implemented and go ethereum.

**Abdel**:  Yeah two weeks for Besu, I would say.

**James**:  Okay uh if we do that, then **it's pretty reasonable to start targeting Berlin** in mind. 

**Tim**: To target 2718 or 1559?

**James**: 2718

**Tim**:  Okay, do you think we should do that now? I feel it might be valuable to just set up the testnets with our current Implementation because it already took a lot of debugging to get them to work and we might be making some other pretty major changes based on you know feedback from large users. So given that, does it make sense to hold off these large spec changes for now, except increment change  which is a small one and actually makes things run smoother but to kind of put 2718 and the potential transition period change on hold until we have more data?

**james**: I wouldn't put the 2718 into the1559 implementations until that it's 2718 is on some kind of road testnet. So it should be a separate fork that then is trying to get included in an upcoming.

**Tim**: Okay! Got it.

**James**:  And then one once that's been accepted then we can go back and do the 1559. but it we start on getting 2718 into what it will be implemented, then the sooner we can have 1559.

**Rick**:  Also I just want to draw attention to Micah's comment where he mentions that Peter from the Geth team would like to see that implemented with the second transaction type not just the legacy type.

**James**: Yeah so we can have 2718 implemented but not like on yolo but not in mainnet and then wait until there is something to include but we can still have it Implemented and in the form of what it would be like when it goes to mainnet that the 1559 team can adopt.

**Rick**:  Right, what everyone's talking about James is that we're being thorough. You can just have 2718 by itself you need 2718 or 2711 in order for 2718 to actually be work. you need the second type.

**Tim**:  Yeah and I'm just wondering is that like out of scope for what we're talking about right now?

**Rick**: Well I think it's presumably all the same people so we might as well talk about it, but it is out of scope, yes.

**Tim**:  Got it.

**James**: You have to have a second type to be able to even have transaction envelopes be implemented?

**Ian**: Well for this, not strictly but to demonstrate it.

**Rick**: To have it to verify its purpose, to have it to verify that it actually is safe and that it works, right? If you just deploy 2718 by itself you just have this weird sort of vestigial thing you need a 1718 plus,  you need to have two envelopes. Because it's relevant now the thing that was confusing to me about 2718 was it wasn't clear to me how it treated the transaction pool, it just sort of acted like the two envelopes were equivalent which I think more times than not that's not going to be the case.

**James**:  Yeah, so I want to be clear here that i'm not talking about mainnet, where the stuff that you're talking about how Peter and and 2718 and another transaction type going into mainnet, all of those things need to be verified but going into yolo which is the pre-test net that is used for testing client integration we could just put the transaction envelopes onto that so at least the 1559 implementers can implement it and then test it and then have that.

**Rick**:  I think probably put in a dummy second envelope, if for some reason it's too hard to implement, my inclination would be to do 2718 and 2711 at the same time. If there's some reason why we can't do that, as from an engineering perspective then we should come up with a dummy shim for 2711 but I can't imagine that's significantly easier from an engineering perspective.

**James**:  Yeah the reason i'm getting into this is the changes that 1559 will need to make in order to adopt 2718 is a future bond. So if we can get 2718 to a point where  it is moving forward and well specified and the clients all agree and it gets to the it's on yolo's test net stage, then the work of redoing 1559 to use that makes sense because we have what it would eventually be here.

**Rick**:  Yeah I agree with all that. I think that they're two separate things. I think that 1559 and 2718 are separate. The question is what goes with 2718 since we're basically excluding 1559 from that list.

**James**:  Yeah and either 2711 or a dummy transaction that was only going to work on yolo would also be there.

**Rick**: Yeah I think that makes sense.

**Tim**:  Yeah and just in terms of priorities due because Rick said it's kind of the same people working on this stuff; should we get the 1559 testnet up and running kind of before getting this YOLO 2718 assuming there's not teams that can't do it in parallel?

**James**: What is that Ian and Abdel think because I would go with what they would want to tackle first ?

**Tim**: Well first of all just like the increments change to the spec so  that's probably the highest priority because it's like a small change that has a big impact but then basically setting up a proof of work testnet with 1559 as is specified right now.

**James**: How long, is that a long process with the minimum changes? I don't want to make the decision, I don't have enough information on implementations and stuff I think to make that decision. I'm just bringing the point that there is this future bottleneck that we can get ahead of and so we should.

**Ian**:  Right yeah I guess it's not even clear to me. If I would be the one doing 2718 since it is a separate EIP but yeah I don't know exactly how we should prioritize that. The immediate focus would be the changes that Tim just iterated.

**Tim**:  Yeah and my bias would also be towards getting the 1559 network up like before and and uh you know getting that to work because if there's bugs found there, it's a higher priority at least for us, like for the 1559 kind of effort to fix the bugs in the spec. I don't know and maybe if other people really want to push 2718 they can start working on the test net as well.

**James**:  Yeah, that sounds good. 

**Rick**: I don't know how it's funded amongst the various implementers; but at vulcanized we're definitely only working on 1559 just as a practical matter so uh wherever however that other teams handle, that's on a per team basis.

**Tim**: And I think for us at PegaSys it's just kind of the same like you know we want to focus on 1559 and and kind of put the bulk of our efforts there and obviously 2718 ends up being a part of that you know we'll support it and we'll do that but we we definitely can't be like champions for that.

# 4. Speeding up development with more resources (context)


Video | [85:30](https://youtu.be/fI2IhcvuJA0?t=5130) 
-|-

**Tim**: I  guess with two minutes to go uh uh the idea of funding and accelerating development was the last thing on the agenda. I know Alexey, you kind of mentioned that at the beginning I don't know if you had some specific thoughts to give some context as it seems like a lot of people would like to see 1559 happen quicker and and and potentially you know provide funding to accelerate that. My biggest question for the people here is just what do we see as the biggest bottlenecks in terms of like our execution speed? Would money actually help there? I can stay on like 10-15 minutes if people want to chat about that but if everyone has to drop in one minute,  it's probably too big of a can of worms.

**Alexey**:  We could probably make it optional, yes if anybody wants to stay on we can discuss this.

**Rick**:  I'll have to go but I’ll just make my two cents. I don't feel like development in my whole time working on this project, **I don't think that developers have been or engineering has been what's slow I think it's been communicating to the community, that you need to have research** like basic research like Tim Roughgarden type stuff  and I’m sorry the other guy's name is french i don't want to mangle it uh stuff going on. I think that getting people to understand that that has to be funded and that has to happen is like a huge milestone and then in a similar vein what James was talking about earlier about someone has to like go you know go door-to-door and make sure that integrations happen and funding that and I think that you know those two things getting funded is way more important frankly I mean we'll figure out how to do the engineering but from a financial standpoint but getting the community to understand that we're not you know we're not incrementing a variable we're not incrementing a constant here we're really changing a lot of, a large swath of what's going on and that requires doing a lot more than just engineering. I think paying for that is where the money should go and on that note, I have to go. So thanks to everyone and uh i'll talk to you all later, thank you.

**Ian**:  I have to drop as well, thank you.

**Alexey**:  Thank you, fine. Okay, let's see who is left. Let's see who's left?

**Tim**:  Yeah I can stay, Tomasz, you can stay.

**Alexey**: Yeah so I just kind of wanted us to discuss a tiny bit because i know that twitter is basically a really bad platform for trying to explain these things and people get offended very quickly. Like yesterday that was you know, they started like lashing at each other and it's very bad, you know somebody said the wrong word or like whatever. Basically, what I picked out from the recent conversation is that they seemed to be this sort of expectation that okay now we threw some money in there's Gitcoin grant, you got 60 grand whatever how much I don't remember but where is the result, right?  They're basically saying like when this is going to happen, what is the blockers which is all reasonable questions and yes but yeah we need to wait to actually explain as Rick said that what are the expensive bits of it. It reminds me on the statement project where eventually the reason why I decided to stop doing it is because I discovered that we would need a lot of this door-to-door people to go, doing really unexciting work of just basically just having meetings with people all the time trying to figure out, who can migrate, how they migrate and all sorts of stuff and obviously I couldn't do that. I don't think we can sort of address this because we don't really have a lot of people from the other side of the from the other side of argument what anybody else thinks?

**Tim**: I agree that like there's a lot of uh communications and outreach that needs to happen. I don't think that's an impossible problem. I guess it kind of depends like how you look at it like i'm not an engineer so for me the engineering stuff looks harder than having tons of meetings and I guess like vice versa. I think with regards to like the community's expectations two things I'm a bit anxious about is one explaining the uncertainty of 1559. So, a lot of people have brought up a bunch of issues today with the EIP. To me, it's still not like a done deal and I think there's a perception in the community that you know this is just it's all downhill from here and it's really not.  So, I think articulating that and making it clear. Because that also translates the funding,  so like if people funded the Gitcoin grant are kind of mad that it's not moving fast enough,  uh they'll be really mad if they find out there's a fatal flaw. I think it's really important to manage that expectation.

**Alexey**: You look at the Gitcoin grant, it's 60 or whatever; how much did it …?

**Tim**: Yeah I think it's 80,000 because the price of ether went up.

**Alexey**:  Okay that's a sort of reasonable amount of money, but then how many people can you know hire with this kind of money, how long? When you start thinking of these terms it actually turns out that it's not that much. It sort of underscores the point that the Gitcoin grant is still not capable of completely funding this project and this is what people need to understand that here's much more. If you really want to make it sort of happening at the kind you at a decent pace, with people not getting stressed about doing 10 jobs at the same time, yeah you do need to basically splash a little bit more money into this. And who is going to splash this money this is the question.

**Tim**:  Yeah and I think yeah some people have brought this up and reached out that I’ve been trying to chat with some of them and one thing like you said that I've made it clear, so right now how things are funded right there's this eighty thousand dollar grant which will probably mostly go to Vulcanize you know modulo some other things. ConsenSys is, we have me and Abdel and Kareem that we can put kind of part-time on this but obviously there's an opportunity cost there we have paid customers and you know that's always like a prioritization thing. The EF has people working on this you know pretty much full-time so Barnabe which is great and then Tim Roughgarden has been paid kind of independently by somebody else. But this means that the bulk of the work is happening by like one or two people by the EF and then one or two developers on both the Vulcanize and in our side. It will move along but it will be, I’m not even sure slow is the right word but it'll be like not as quick as it could be.

**Alexey**:  Also, there is another issue here you know sometimes uh there are certain things that need to happen before you reach your full speed. So, sometimes you have to do some proprietary work. An example is this transaction enveloping things, right?  If it existed before, the things would be a bit easier and so what might be interesting is to have this understanding that you know kind of you not only have to wait for one year for all the work to happen but for all the people the things to fall into their places, all the pieces to fall into the places. When you launch a testnet you cannot put an extra hundred thousand dollars and make sure that the testnet needs to be run for like 10 times shorter than that. You actually have to wait.

**Tim**:  Yeah, yeah and I think that's why you know like personally I've been reticent about going back on like all core devs and discussing this again because there's just like known issues with the EIP that we're still you know addressing and you probably need more than one implementation to like start addressing them like think it's been helpful to have Besu and Geth kind of disagree on stuff and fix those. But like we definitely don't necessarily need everybody to have this at the top of their priority list because we might find some other issues with it because of this weird in-between period.

**Alexey**: Also, what just Tomasz is asking on the time I know it's a sort of joke but it's actually not a joke but of course we should not uh undersell ourselves and then it applies to pretty much everybody in in the core development, that our work does cost money and it probably cost a lot of money. So it is okay to expect to be paid for these things I don't know how exactly but the expectation is it should be there.

**James**: I was just gonna say that **an opportunity for others to contribute funding in a meaningful way would be to provide funding to help the other clients implement 1559**. So, Nethermind, OpenEthereum. The sooner those happen the sooner it can happen and those teams are already over right all of the client teams are busy, so to get resources to build to implement them in all the clients would necessarily make that the time.

 **Alexey**: Yeah because basically what happens is that all the development teams at the moment they have their own priorities, they have their own agenda, because partly some of them basically are thinking about how they're gonna get some money to pay their people, right?  It was Rick saying it on twitter is that okay some of them actually have to pay out of their own pocket to make things happen because they actually sort of like because they have a bit of money or because they hope that they're gonna make something out of it in the future. But just basically piling on to that and expecting things to go faster that's you know that's not gonna happen. I think that has to be sort of appreciation and respect for uh for people and you know to expect him to slow in 30 grand and things happening in a month it's not realistic. So if you have if you basically throw in half a million then you probably can have these much bigger expectations.

**James**: So if someone came in and did an implementation into nethermind, separate from the team; does that fit what you're saying or not what you're saying Alesexy?
**Alexey**:  I mean it depends. I don't want to talk for Tomasz but it depends on the ability to do that also depends on the code structure and how it's structured? It's like sometimes in some of the implementations it has to be pretty much the people who are owning that to be made to making changes. In some implementations it's easier to just come from the side and propose the implementation for example what we are trying to do in our implementation; we're trying to split everything as much as possible so that to allow people to come and do things on the side. I don't know about the others.

**Tim**: I guess it's also worth noting like this is kind of a weird eip because, for normal eips, some team that's usually not a client developer that kind of does a PoC implementation and then they bring it to all core devs and then the clients, all kind of implement it “for free” and it moved up. This one is kind of weird because it's applied R&D in a way. So there needs to be an early implementation and it's also a much larger change than other eips and it's not clear where the boundary is from paying like a third party to provide a reference implementation and then paying all the clients to prioritize that on the roadmaps. The level of like alignment you need, like how do we get funds for like all the clients to prioritize this um and is that like the model we want if there's this huge change that happens then we basically need to pay for an implementation and by we, I guess like the community needs to find a way to pay for these end implementations.

**Alexey**:  If we wanted to eventually come to a much healthier kind of model of development so that goes back to what we'll be discussing again in July as well if we want to come to a much healthier model with a better development then there has to be an expectation that any work which needs to be done, is done and the money has to come from somewhere. So far, as far as I know, the core developers haven't figured out the way to finance their development completely without some kind of subsidies and therefore, for now, the subsidies have to be applied.

**Barnabe**: I think,  we already know we have a couple of **milestones to hit** and 

* the first one is like **freezing the specs**, 

* then we know that we have a YOLO testnet, we know that after this we want 

* to have a proof of work testnet or something and then we know that other clients will need to implement it.

So a good way also to manage the expectation of a community would be to have a reasonable let's say roadmap with some kind of timeline. Because it's currently like there's a lot of momentum around EIP-1559, like a lot of people even on twitter have said oh if money is the issue we can always like to throw more. But, a good way to say, okay you can give us now but we might not. We don't really need to throw like half a million dollars on it currently, is to have this sort of timeline, and to say, this will be useful later on. I guess after four months if people don't really see improvement, or for the community improvement anyways is very binary like either it's on the main net or not whatever is happening in between like they don't really see as an improvement so yeah having like …

**Alexey**: The thing about this uh kind of drip financing is also problematic, as I think Tim mentioned on twitter is that. The reason I'm talking about throwing in for half a million dollars is because if you know that the money is there then you can actually really hire somebody to do the work for a reasonable time. You don't have to keep everybody on sort of zero-hour contracts and stuff like that and yeah we're just saying that any time when the money runs out 
you're fired.

**Tim**:  Yeah and I think that's exactly the situation we're kind of in with the Gitcoin grant to be sure. We have a not-insignificant amount of money, but you don't know if it's going to last you three months, six months, 12 months, right? Obviously the rate at which you spend, you kind of want to be conservative on it. 

**Alexey**: That's why the model which works the best is either you have a very reliable counterparty like let's say Ethereum  Foundation,  that basically has a contract with you or something, like this that they give you money as long as you don't do anything really stupid or you have a pool of money in front of you.

**Tim**: I think Barnabe's points are just what I find, I think the hardest is like yeah how do you know for those intermediate milestones like setting up a proof of work test net and whatnot like,  what's the right amount of funding? Should we fund client implementations for all the clients to join the testnet, which might not work, right?  If not how money do we fund and how do we choose it?

**Alexey**: I mean you don't need to be so fine-grained. I mean this project is not so huge that you have to be obsessed about fine-grained details. So what you could do simply is that uh let's say that you say okay for this to happen, you choose the implementation, let's say we need to goEthereum,  Nethermind, Open Ethereum and what else,  I mean choose them. Let's say everybody should get one developer on each team implementing this and get to make sure that everything works, for how many months, whatever. That's basically a really rough idea. But, then you know that in each team there is one person doing this job and of course, they can do some other things at the same time, you cannot stop That but at least the money is allocated you know that it's there. i mean if this project was for five million Dollars then, of course, you have to have extra scrutiny about you know where exactly this money is going. But even if it's half a million, i don't see the point of obsessing over the details.

**Tim**:  I guess Justin has a comment around like you know the precise funding needs for fast-tracking this.  I'm not sure if there is a way to fast track it? It guesses, I don't know, past like one developer per team, I think there might be like diminishing returns and I'm not sure if like the funding actually fast tracks things or just puts them at like a normal pace.

**James**:  The things that would fast track would be 

* funding the community outreach stuff so that there is a group of people that are ready to go out and make sure people are adopting, 

* other things would be having bounties for team Metamasks and put in and implementing 1559 interaction support so you just put up a list of major wallets and major things and say hey anyone that does implements 1559 into it, gets this bounty and

* then the last one would be after this kind of round of R&D that's happening for the next month or so, when it turns into all the clients need to implement, giving them support through however it is for each client team,  is the kind of the last.

**Alexey**: I mean i don't know if the issue with the bounties or something like this. But, I just like to simplify this. Because essentially if you say that there is money to pay let's say one developer in each team for six months right that's it you know and they suppose this developer is supposed to be doing the EIP-1559.  They can do basically if they're not coding all the time, they can do other things, testing, right more testing, doing spinning out testnets, talking to each other, whatever. I mean whatever they could be whatever they can do to make this to make sure that it happens really and if they're doing something else, as I said it's fine, as well. Would you be really upset if they spend some money on improving the performance of their client as well?

**Tim**: I think, at least from our perspective like there's value in saying one developer is like you know paid to do this and it can help prioritize 1559 about other stuff, on a day-to-day thing.
 Obviously like I'd be curious to chat with other client teams to see that and I'm happy to take that action item to reach out like Tomasz, I know you have a bunch of comments in the chat  and I know you can't talk right now. But I can set up a call maybe with Nethermind, I don't know Alexey if you want Turbogeth to be part of this but just to talk with the different client teams to see what's like a reasonable amount of engineering work. And can we just get like one person on each client team to put this at the top of their priority list and then the other kind of more ops works as well and what would be just like a rough amount for that.

**Alexey**:  Okay somebody needs to save the chat, before we go.

**Tim**:  I'm recording on zoom, so it'll save. I’ll send it to Griffin. Griffin does a transcript uh based on the zoom recording, so i'll send them the chat as well. 

**Alexey**: Okay, cool!

**Pooja**: I’m also doing the notes, detailed notes for it and I have the chat saved with me.

**Tim**:  Awesome! yeah so i'm happy to take that as an action item to follow up with the different client teams next week and see what we think makes sense.

**Alexey**:  Okay!

**Tim**: Anything else anyone wants to discuss?

**James**:  I think that's pretty good.

**Pooja**: Just one last thing I wanted to throw out. In the beginning of the call, we were discussing about having the transparency on the funds. I have just created [this sheet](https://docs.google.com/spreadsheets/d/1toow2aa-94n76dQ1VL_jlwGJmN14mjtpnFxYwemaBnE/edit) for reference and we would be sharing it with people who are interested. It will include all kind of outgoing transactions will be recorded here.

**Tim**:  Okay let me just share my screen,  so it's in the recording. Okay yeah like we said the two only transactions so far have been for Vulcanize. Cool, anything else?
Okay then there's a pretty huge amount of work to get done in the next couple weeks - some changes on the spec, trying to get a testnet with POW out. Following up the conversations around that 2718, There's some R&D work and then the whole funding discussion. Yeah that's a lot.  I think it makes sense to probably have another one of these calls in like a month to give an update on on all those things.

**Alexey**:  Okay thank you very much!

**Tim**: Of course, thanks everybody!!

# Annex
## Attendees

* Abdelhamid Bakhta
* Alexey Akhunov
* Barnabé Monnot
* Danny Ryan 
* Georgios Konstantopoulos
* James Hancock
* Ian Nordan
* Karim Taam
* Lightclient
* Micah
* Pooja Ranjan
* Rick Dudley
* Tim Beiko
* Trent Van Epps
* Tomasz Stanczak
* Vitalic Buterin 
This lists people shown on the recording and zoom chat.

## Next Meeting Date/Time

In a month. 

## Zoom chat

From Tim Beiko to Everyone: (11:02 AM)
 https://github.com/ethereum/pm/issues/197
 
From Trent Van Epps to Everyone: (11:10 AM)
 Decentralization Foundation https://d24n.org/blog/ 

From Micah to Everyone: (11:12 AM)
 If base_fee goes to 0, it can never go above 0.  :) 

From Abdelhamid Bakhta to Everyone: (11:13 AM)
 Yeah totally thanks 

From Micah to Everyone: (11:14 AM)
 How many blocks between 1 nanoeth to 0 assuming 100% empty blocks? That is a much smaller number than I expected.  I was expecting millions. I'm 👍 of minimum increment/decrement of 1. We also need to start getting tooling to implement, which is more likely once it hits Kovan/Ropsten/Rinkeby.

From Tomasz Stanczak to Everyone: (11:19 AM)
 sorry I will not be able to answer questions for a while - it is noisy here 

From Micah to Everyone: (11:20 AM)
 The problem with Kovan/Ropsten/Rinkeby is that they have a *lot* of empty blocks I believe (there is not congestion like mainnet). 

From Trent Van Epps to Everyone: (11:20 AM)
 just a heads up James - your audio is cutting in and out/ might be an aggressive noise gate on your mic 

From James Hancock to Everyone: (11:20 AM)
 I think it is my computer is chugging after being on too long 

From James Hancock to Everyone: (11:20 AM)
 thanks for the heads up. I'll go slower 

From Georgios Konstantopoulos to Everyone: (11:26 AM)
 EIP2718 seems too generalized to me. Do we really wantHow important do people think it’s to bundle the tx envelope with 1559? You could add an optional version field, if present and set to v2 (or smith) it tries to decode it as eip1559 txs, otherwise defaults to current format (Ugh, omit the “do we really want” part)
 
From Micah to Everyone: (11:27 AM)
 1559 is one of new transaction types that are desired and have been desired in the past. 

From Georgios Konstantopoulos to Everyone: (11:27 AM)
 Yeah, but do we need a generalized tx versioning scheme? 

From Micah to Everyone: (11:27 AM)
 2718 isn't *just* add 1559 transactions, it is to add that plus a bunch of other future transaction types in open EIPs. 

From James Hancock to Everyone: (11:27 AM)
 There are others that people are proposing 

From Georgios Konstantopoulos to Everyone: (11:29 AM)
 Can you link some? Didn’t see any in the agenda / in the PRs
 
From Micah to Everyone: (11:30 AM)
 https://eips.ethereum.org/EIPS/eip-2711 is the one I care about.  There is also the possibility of 2803 being a typed transaction instead of a precompile, though I am currently preferring precompile. THere was another one that is open... but I'm blanking on it at the moment. https://eips.ethereum.org/EIPS/eip-2733 (though overlaps with 2711) 

From Abdelhamid Bakhta to Everyone: (11:32 AM)
 @Vitalik you mentioned implementation of EIP-1559 for Eth 2.0, am I right ? I am curious, what group / people are working on that ? Could we try to leverage efforts 

From lightclient to Everyone: (11:34 AM)
 @rick, what aspect of 2718 do you find underspecified? 

From Micah to Everyone: (11:34 AM)
 I think he was referring to 1559 being underspecified. 

From Micah to Everyone: (11:34 AM)
 I have heard him complain about that in the past.  :)
 
From lightclient to Everyone: (11:34 AM)
 ah okay, i heard it as "2718 should be completed before we consider depending on it" 

From Micah to Everyone: (11:35 AM)
 I have an open PR to clean up 1559, but struggling to get agreement on it.  :) 

From Rick Dudley to Everyone: (11:35 AM)
 I think they are both underspecified. 

From Micah to Everyone: (11:35 AM)
 Alexey, I think the issue is that tool developers don't have the same incentive as users.  We need MetaMask, Tether, etc. to update since their users can't update without them (effectively). And MetaMask isn't suffering directly when their user's suffer. 

From Ian Norden to Everyone: (11:36 AM)
 Yes if people could please provide feedback here, that would be great https://github.com/ethereum/EIPs/pull/2859 I don’t want to approve it on my own accord, particularly when I don’t completely agree :D
 
From Micah to Everyone: (11:37 AM)
 @Rick I would love your feedback on 2718 (after meeting perhaps) on how we can improve it. 

From lightclient to Everyone: (11:38 AM)
 also curious ^ 

From Micah to Everyone: (11:39 AM)
 We don't *want* miners increasing the block size right now is the problem. 

From Georgios Konstantopoulos to Everyone: (11:43 AM)
 Sorry why are we talking about blocksize 

From Micah to Everyone: (11:43 AM)
 If 40% of users only can send legacy, 40% can only send 1559, and 20% can do either, that 20% will ensure that both pools are always full and you won't be able to tell which pool is *actually* in higher demand (what those percentages are).
 
From Georgios Konstantopoulos to Everyone: (11:43 AM)
 lol 

From James Hancock to Everyone: (11:44 AM)
 > Sorry why are we talking about blocksize
Increasing blocksize (increasing the gas limit) isn't something we want to do in the short term 

From Georgios Konstantopoulos to Everyone: (11:45 AM)
 Adjusting block size is a 100% separate discussion which we shouldn’t be allocating bandwidth in this call :P EIP1559 long term block size is same as today’s 

From James Hancock to Everyone: (11:45 AM)
 IF we only allow block increases to the 1559 pool then that is no longer true 

From Georgios Konstantopoulos to Everyone: (11:46 AM)
 Why would we? Do 1 thing and do it well instead of doing 10 

From Rick Dudley to Everyone: (11:47 AM)
 The incentives don't allow for that.
 
 From Micah to Everyone: (11:51 AM)
 Basically, no one pays attention to client development until hard fork lands on mainnet.  :) 
 
 From Georgios Konstantopoulos to Everyone: (11:52 AM)
 BaseFee on file coin for anybody that didn’t see it yet https://filfox.info/en/stats/gas 

From Barnabé Monnot to Everyone: (11:52 AM)
 👍 

From Georgios Konstantopoulos to Everyone: (11:52 AM)
 Mostly at 0, which makes sense since the chain is empty (duh) Switch to 7 day 

From Barnabé Monnot to Everyone: (11:53 AM)
 Much higher than last time I checked still, it increased in the last hour?

From Micah to Everyone: (11:54 AM)
 I think there is almost 0% chance that we don't see both pools always 100% full. 

From Georgios Konstantopoulos to Everyone: (11:55 AM)
 Mapping this to prior events, this is like segwit and introduction of P2WSH. What about not enforcing a transition time to the new format? 

From Micah to Everyone: (11:55 AM)
 And let miners decide by vote or something? 

From Georgios Konstantopoulos to Everyone: (11:56 AM)
 Potentially, or just leave it unspecified, whatever the miner decides
 
 From Micah to Everyone: (11:57 AM)
 Uniswap is something like 90% bots. Uniswap *UI* is actually not that much gas usage total. 

From danny to Everyone: (11:58 AM)
 gotta run! thanks everyone 

From James Hancock to Everyone: (11:58 AM)
 thanks danny 

From Georgios Konstantopoulos to Everyone: (11:58 AM)
 @Micah false :p
 
From Micah to Everyone: (11:59 AM)
 I don't remember the exact number, but a while back Hayden indicated that a very disproportionate percentage of Uniswap usage is bots (it was well over 50%, I think it was like 75%+).
 
From Micah to Everyone: (11:59 AM)
 IIUC, the currest proposal Alexey is making is to just fix it to 50:50 indefinitely. 

From Georgios Konstantopoulos to Everyone: (11:59 AM)
 50% is probably right About uniswap volume form bots Just checked with the team 

From Micah to Everyone: (12:00 PM)
 Current proposal starts at 50:50. Sort of... 

From Georgios Konstantopoulos to Everyone: (12:00 PM)
 Gotta run too, ty all. 

From Micah to Everyone: (12:01 PM)
 At fork time, legacy transactions have 50% of space.  1559 *target* is 50% of space (but it is 2x ellastic). 
 
 From Micah to Everyone: (12:02 PM)
 My objection to Alexey's proposal is that I don't think we'll get any *usable* data from that change.  I don't see any scenario where we don't see both buckets full other than Ethereum usage going to 0.
 
 From Micah to Everyone: (12:04 PM)
 What is the objection to just being willing to hard fork away if we see people not adopting? 
 IIUC, the debate is basically "we have to hardfork to stop it" vs "we have to hardfork to keep going".
 
 From Micah to Everyone: (12:13 PM)
 Do we have contact info for the centralized stuff?  I know how to contact the decentralized stuff (Uniswap, MetaMask, MEW, etc.) but not any of the centralized providers. 
 
 From Micah to Everyone: (12:20 PM)
 I think Peter (of Geth team) was against 2718 without having a new transaction type included as part of it.  e.g., 2718 + 2711 or 2718 + 1559. 
 
 From Micah to Everyone: (12:22 PM)
 You *can* have 2718 without a second transaction type, Peter just doesn't like the idea of having 2718 with only legacy type.
 
 From Abdelhamid Bakhta to Everyone: (12:29 PM)
 I have to drop, thanks, bye 

From Micah to Everyone: (12:31 PM)
 I'm here, still chat only though.  :P 

From Tomasz Stanczak to Everyone: (12:31 PM)
 :) 

From Me to Everyone: (12:33 PM)
 Cat Herders will help with communications as much as possible 

From Micah to Everyone: (12:33 PM)
 100 hours of engineering is easier than 3 meetings with sales reps.  😛 

From James Hancock to Everyone: (12:33 PM)
 lol
 
 From Tomasz Stanczak to Everyone: (12:36 PM)
 can vulcanize implement it in Nethermind too? :) 

From Micah to Everyone: (12:36 PM)
 Don't forget about the unemployed strangers on the internet that are too stupid to ask for money for their work.  😉 
 
 From Micah to Everyone: (12:43 PM)
 I don't get the *impression* that 1559 is a particularly hard engineering problem.  Of course depends heavily on how your code is structured, and I wish we had someone still on the call who had already implemented it in a real client.  😢 

From James Hancock to Everyone: (12:43 PM)
 yeah 

From Micah to Everyone: (12:43 PM)
 We could probably use some of that grant to fund development in additional clients and it won't be *too* expensive.
 
 From Justin Leroux to Everyone: (12:46 PM)
 I think if the precise funding needs for fast-tracking this are outlined, it seems likely the community will quickly meet goals in the range being discussed by Alexey. It's easier to rally companies and individuals when the funding target and goals are more clearly defined. 

From Tomasz Stanczak to Everyone: (12:47 PM)
 would be nice to be able to bid for delivery
 
 From Tomasz Stanczak to Everyone: (12:47 PM)
 because if Nethermind prices delivery at $20k and other project at $100k then maybe we can have more economic allocations :) 

From Justin Leroux to Everyone: (12:47 PM)
 I mean, within the constraints Alexey outlined - you can't expedite observing a testnet.  :) 
 
 From Micah to Everyone: (12:48 PM)
 $10k per team for implementation $20k for operational work $470,000 for talking to to CoinBase + Tether + MetaMask + MyEtherWallet + MyCrypto. 
 
 @Tomasz, curious how much you would consider a reasonable amount to prioritize this over other things on your plate?
 
 From Micah to Everyone: (12:48 PM)
 $10k per team for implementation $20k for operational work $470,000 for talking to to CoinBase + Tether + MetaMask + MyEtherWallet + MyCrypto. @Tomasz, curious how much you would consider a reasonable amount to prioritize this over other things on your plate? 

From Micah to Everyone: (12:51 PM)
 Feel free to leave out my troll comments from the permanent record.  😉 

From Me to Everyone: (12:52 PM)
 https://docs.google.com/spreadsheets/d/1toow2aa-94n76dQ1VL_jlwGJmN14mjtpnFxYwemaBnE/edit#gid=0 

From Tomasz Stanczak to Everyone: (12:52 PM)
 g2g thanks everyone! 

From James Hancock to Everyone: (12:52 PM)
 thanks tomasz 

From Micah to Everyone: (12:52 PM)
 👋 
 
