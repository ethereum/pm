# Execution Layer Meeting 181 [2024-01-18]
### Meeting Date/Time: Feb 15, 2024, 14:00-15:30 UTC
### Meeting Duration: 1:30:21
#### Moderator: Tim Beiko
###  [GitHub Agenda](https://github.com/ethereum/pm/issues/952)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=UTgnbE6jTuE)  
### Meeting Notes: Metago
# Agenda
## Introduction
**Tim**
Okay, welcome everyone to ACDE number 181. Bunch of things on the call today so first just going to go through Dencun updates. I know some of the El clients already have releases so yeah. Shout about that and see where everyone's at. Then Martin had an EIP he wanted to discuss that should be retroactively applied from Genesis and then so we can discuss that there was another one by Peter who can't make it but left the big comment in the Discord that also is a retroactive EIP, so finalizing those two discussions, after that moving to Prague Electra. There's three EIPs that people wanted to present and then tomorrow we have inclusion list breakout room so go over those things, and then hear from client teams how they're thinking about filling up the rest of Prague given what we've decided around Verkle and Osaka and one thing there as well. So we had sort of committed to 2537 but yeah, just confirming that we're still good with that. Yeah hopefully we get through all of that. 

## Dencun updates [4:00](https://www.youtube.com/live/UTgnbE6jTuE?si=lO-J6sBxKTDO5har&t=240) 
To kick it off anyone have any specific Dencun topics they wanted to discuss? Otherwise any clients want to share where they're at with regards to client releases? 

**Barnabus**
thinking some may not notes for the of the main should probably take place on next week the not that have not seen yet are and rest which are expected 

**Tim**
You're breaking up a bit but I think I understood 90% of what you said. So you're syncing mainnet nodes you're missing Reth and another client 

**Paritosh**
Yeah it's just the archive notes take a bit longer to sync but we should be hopefully ready sometime next week and that should be in time for when client teams have releases up. **Tim**
Nice, oh okay yeah Reth and Aragon are the one still syncing, got it sweet, yeah and how are I know I think Geth and Basu have releases out. Nethermind, Aragon, Geth yeah how are things looking there? 

**Marek**
Yes, we are testing our release. We plan to release tomorrow or on Monday. 

**Tim**
Nice.

**Andrew**
Yeah the same with Aragon will publish a release tomorrow or on Monday.

**Tim**
Sweet. Reth is out so one alpha 18 is the mainnet release for Dencun and then Besu, Geth, what was the release number for your clients?

**Justin**
Besu is 24.12.

**Tim**
Got it. 

**Justin**
At least yesterday

**Tim**
And Geth? Anyone? Okay I don't have the number quick but I think Geth release came like right after the call last week so it's been out for a few days now. Any CL folks have updates on their release? I know that on the call last week teams on the CL side needed a bit more time but yeah any updates people want to share?

**Terence**
Prism is going to release by next Thursday, but just heads up, we're still blocked by the CL release because we have this unit test that basically set a mainnet for art but it puts the mainnet upstream release so until the Cl’s back does release for the mainnet part we are currently blocked so yeah just wanted to flag that.

**Danny**
Okay, I was a bit AFK the past couple days, I know we did approvals on the little PRs that needed to be done. I'll check in with Hsiao Wei and we'll get it out by tomorrow morning.

**Terence**
Thank you so much.

** **
is already can you hear me sorry yeah we can oh cool yeah teos is already releasing so we are in the final stage of releasing.

**Tim**
Nice.

**Gajinder**
Lodestar is also ready to release so we are just doing some final things so we most probably can release early next week.

**Tim**
Sweet anyone from limus or Lighthouse I think those are the two we didn't hear from yet, okay and then yeah there's a comment in the chat, Barnabas saying we should wait until we have all the Y pairs for the release I think that's reasonable so probably means that we have all the releases out by say like late next week and then maybe we schedule the mainnet shadow fork for like the Monday after that or something so that we can put out the blog post one day after, once we're sure everything's all right, does that seem reasonable having like the last mainnet Shadow Fork on say Monday the 26th?

**Barnabus**
If we can have all the by Thursday then we can do it on Friday because expensive not to run so we wouldn't necessarily want to wait over weekend if can do it by next week. Thursday releases are out and we can do it next week Friday.

**Tim**
Yeah I like that, yeah okay so let's aim for Friday the 23rd and then yeah we'll have the blog post out early the week after assuming there's no issues that we find on the shadow fork would argue even try to do the Shadow from the Okay sweet. I guess anything else on Dencun? Oh yeah Carl?

**Carl**
Yeah I know there's previously some mention from l2s about not quite being ready or it might being a while after that. We had a long call yesterday, there lots of discussion around this, it seems like we’re at least going to have one of the l2s ready being polygon, but many others are still trying to have some kind of mainnet release ready very soon after, or even on the 13th. 

**Tim**
Nice. 
So that's looking nice see anything else on Dencun?

## Retroactive EIPs – [EIP 7610](https://ethereum-magicians.org/t/eip-7610-revert-creation-in-case-of-non-empty-storage/18452) [EIP 7523](https://eips.ethereum.org/EIPS/eip-7523) [10:37](https://www.youtube.com/live/UTgnbE6jTuE?si=L8xsJzuhpwcvGc93&t=637) 

Okay then next up, yeah these two retroactive EIPs. First one 7610, I don't know if Martin is on the call, if not there someone else he's Sor, he's not here today unfortunately. Yeah can you give the context on this Maris or someone else, I could probably try but I think someone else might be more equipped to do it.

**Marius**
He is not here today, unfortunately.

**Tim**
Can you give a context of this Marius?

**Marius**
I could try but I think someone else might be more equipped to do it.

**Danno**
I'll take a stab yeah, so this is looking to amend the contract creation rules right now, if a contract's being created in address and it has a non-zero nodes it fails, this rule would extend it to say if that address has any storage, it also fails, and there are a few contracts that existed before on the Shanghai attacks that have a zero nonce but have storage but also have no code so I think yeah the two things need to have no code and a zero nonce for it to succeed so if there's code it'll fail if there's a nodes of one, it'll fail and they change the rules and the Shanghai attacks require nodes of one on all creation attempts successor failure, well not successor failure, but if they leave code or not. So there are a few codes, there are a few addresses prior to Shanghai that have a zero nodes, no code and storage because of failed creates and these are all coming from create one attempts.
Now because it's a create one depends on the nodes the nodes has been incremented, by rule it is impossible to recreate the situations to create that already so this can't be created unless there is a hashing accident of one of those you know impossibly large hashing numbers where the collisions are basically impossible, so we're so to change this rule we make it so that we don't care if there's a hashing accident or not if there's any storage or any nodes or any code the create will fail, now what's not mentioned in the EIP that we realized on the basic team this week is this, have positive impacts for Verkle trees, because when you do a create you're supposed to delete all the storage, and that's why we got rid of self-destruct, is because enumerating through all of the storage and deleting it is prohibitively expensive in Verkle and we'd have to either change the rules for create or prohibit creates like this, so I think we should just retroactively activate this if there's going to be highly unlikely to and impossible for it to happen on mainnet and formalizing this rule will make a lot of client code simpler when it comes to the create process especially in vertical.

**Guillaume**
If I may add some dissent in the Verkle part, it's not that self-destructing is impossible in Verkle, is prohibitively expensive, its just impossible. We just don't know which storage slots belong to what and that was going to be my question actually, you also can't figure out if a slot belongs to an account so how do you, I don't think that will work for Verkle. Gary who proposed the EIP is aware of that, so all I'm saying is if this EIP makes it which I'm fine with it, it solves a lot of problems on the way to Verkle, it will not be able to work in Verkle.

**Tim**
So what would we have to do when we switch to Verkle?

**Guillaume**
Yeah that's the question and that's the thing that's missing with this, with the EIP.

**Danno**
Oh so there's no State re kept in Verkle anymore that feels taken out of the account.

**Guillaume**
Too sorry, I didn't hear or what you say?

**Danno**
There's a state route hash that is kept in the current account State that's taken of Verkle?

**Guillaume**
 Yeah, I mean the problem is that you would be potentially able to access older, I mean you can no longer delete accounts anyway so it's not really a problem but if you were able to recreate accounts you would potentially have, there's no account there's no rehash, so you would automatically access the old storage, like the storage of the contract that had just that has just been deleted.

**Danno**
So there's no way to tell if address has storage?

**Guillaume**
Exactly, that's one of the reasons why self-destruct is deactivated.

**Danno**
And also you can't do a triac of storage slots which the devs are really going to love let me tell you that. So maybe when we do the transfer the translations we put a flag that you know it's had storage in the past, I mean we need to adjust this for Verkle, when we do the transition if we see that it has a root hash that does not signify empty stay we put some sort of a flag on there that says you can't create this address?

**Draganrakita**
So why don't we just like removed stores when we transition to the Verkle we good opportunity where we like to transition from One Tree to another tree and the hashing is going to be it's like State change that we are doing in some yeah in some way?

**Danno**
Because that opens Pandora's Box that opens Pandora's box of an irregular State transition which is a larger discussion.

**Draganrakita**
But we already doing that with the Verkle transition

**Danno**
But we're not deleting any storage.

**Draganrakita**
But this storage is not accessible because you don't have code for it it's not something that can be used seen or like fetched from the state, is just that data.

**Guillaume**
Yeah I think that's a good idea I'm not sure I understand Danno’s reason not to like that, it would be possible for sure although I'm just wondering but we're going to talk about this later, if 5806 does not, cause this, would not cause a problem with that.

**Tim**
So I guess I know because we have a lot of EIPs to cover today I think it's not obvious that we should just go ahead and include this as is like it seems like there's more conversations to be had on it in the final design so does it make sense to just continue those conversations over the next couple weeks and discuss this on the next call?

**Danno**
Yes it does. Peter will be back and be able to answer more the deeper issues on not Peter, Martin.

**Tim**
Yeah.

**Draganrakita**
Just say I don't have any like Im fine with this EIP to be included my statements were mostly how to remove it fully with like Verkle position that we have.

**Danno**
Well I think without the Verkle issue, it would have been easy for us to just go ahead and do it but because there's Verkle implications, I think we need two more weeks to mull over what it means.

**Draganrakita**
Okay, makes sense.

**Tim**
Sweet, and the next step, so Peter Davies is not here for 7523 but this one seemed pretty uncontentious last time. There's some tests that have been updated and then he mentioned on the Discord the only thing we should potentially discuss is if we want to do an independent verification of the deletion of the empty accounts, he checked but it would be nice to have somebody sanity check that there actually are no more of these accounts before we sort of finalize this.
Any thoughts any volunteers to yeah run another sanity check? Okay if there's no comments I'll follow up offline then with Peter and we'll try to find somebody else to run another check on the chain and publish those results and ideally the script that they use whatnot and yeah assuming that's all good we can we can finalize that.

## [Prague / Electra EL Proposals](https://ethereum-magicians.org/t/prague-electra-network-upgrade-meta-thread/16809) [19:42](https://www.youtube.com/live/UTgnbE6jTuE?si=MsTANMAZhkg1LOSf&t=1182) 

Okay moving on to Prague, so there were a couple EIPS that I added last minute to the agenda because we said we would cover them last time and we didn't so yeah I think it probably makes sense to briefly go over the five or six that we had for discussion today then hear from client teams how they're thinking about all of this and see if yeah we can make any decisions about what we want to include yeah so the first one we had on the list was 5806 which I believe Adrien is here to chat about.

### [EIP 5806 overview](https://ethereum-magicians.org/t/eip-5806-delegate-transaction/11409) [20:20](https://www.youtube.com/live/UTgnbE6jTuE?si=o-jS2KEEHcG4lSDQ&t=1220) 

**Adrien**
Yes hello so thank you for allowing me to discuss it here. I think you have wanted me to present it the context being that 3074 is actively being suggested as a candidate in inclusion Prague and 5806 is a potential alternative or at least an EIP that would somehow implement the same functionality from a user’s point of view. The EIP is to enable EOA to be more expressive in what they can do in particular allowing the Verkle pattern, it's been discussed at length, I'm not going to go over why Verkle is good to have but 5806 allows that in a different way than 3074. So there are big differences between these two EIPs and I think 5806 which is my proposal has some strength that should be considered one of them in my opinion is the fact that unlike in 3074 where you sign a hash and you rely on a smart contract to tightly associate that hash with an intention, like bugs can happen at the contract level, in 5806 the transaction that is being signed is very explicit about its entire context there is no external factors that should temper with it.
I can go into more detail if you want but I think it's more secure in that regard also about the counselling think since it's a normal transaction done by an EA it can be replaced by a du transaction with higher fees and tips so that it it's being cancelled so I think the model is better here in the predictability of how it's going to be executed.
Then 5806 also has a lot of things that it enables in terms of what a user in a new way can do in the sense that it may allow it to access op codes like log to emit an event or create two to create a smart contract in a very predictable way.
The question then is about longlasting changes like storage, for a long time I was an advocate of storage being useful in that context like you could store something under your account that would stay there and be provable. 
I understand that this can create challenges and security issues if an EIP proposed to put code at an EA address because using this 5806 you have the ability to put code before creating the contract and that might hide things so I'm completely open to the idea of preventing s store to being executed in the context of EOA through 5806. I'm not exactly sure what I should say more 

**Tim**
Yeah this is a good yeah this is a good overview definitely yeah if there are questions it's we're going over them now there's a comment in the chat by lightclient but okay Andrew has his hand up, so let's s go with that.

**Andrew**
Yeah I think if we disable store then this keep sounds like a good simple improve and like it will be reasonably simple to implement and it will bring a non-trivial UX improvement like in one of the our previous course we discussed batch transactions so still our batch transactions, yeah so I think we should have it in in Prague but with the store disabled.

**Tim**
So meaning you disable store you disable transaction types those transaction types to use store?
**Andrew**
Exactly yes. 

**Adrien**
Okay yeah. I'm having a look at the comment from lightclient on the chat and I completely agree with point two and three, 5806 doesn't try to do social recovery and I think that's partly because the signatures are, it's like a transaction like if it it's supposed to be mined straight away and if you keep assigned transaction for a while and you do all stuff with the same nodes, it's become invalid.
So it's not something you can store for social recovery, also it doesn't allow bundling transaction from different users and basically impersonating multiple EOAs in the same transaction so that's something that 3074 does that 5806 doesn't do, because the signature pattern is different and because signature of 5806 are way shorter LIF than 3074 which I believe goes into sense of security here but yes it's different approaches.

**Tim**
Okay, any other comments questions? 

**Guillaume**
Yes that's in the light of the discussion we had about the retroactivity EIP, so I understand that yeah you would be very unlikely to call it if your nonce and balance are zero, but assume you just have the key to an account that does not exist yet so you generate your private key the account the associated account does not exist yet on the on the chain and you sign a transaction that sends, that calls a contract the delegates call to a delegate calls to a contract my question is have you thought how it would fail because clearly it doesn't have any fund so it would very quickly go out of gas I mean it would immediately go out of gas but my question is more like what State should be touched in that case, and yeah the question is for Verkle trees and how do you make it work in the context of Verkle trees and how and also in the EIP that Gary was working on. 

**Adrien**
I'm not sure I really understand the question. I mean if the sender has no gas, the type of the transaction here is in my opinion irrelevant. Part of my of the verification of a transaction is that the account has enough funds to pay for the amount of gas required multiplied by however it cost you for each unit of gas and if you don't have enough like type two transaction and type zero transaction will fail and this type of transaction will fail the same.

**Guillaume**
It's not about the type of transaction it's how it fails.

**Adrien**
But would it be a revert or would it be an out of gas, it would be I've not thought of that I think it would be the same as what happened with other types of interaction.

**Guillaume**
Yeah okay, yeah no, just asking if you had thought of that I would have to consider that but yeah it's probably it's probably fine.

**Adrien**
What I was thinking was that everything that is part of the verification of the transaction, including the signature and the encoding except for the value part would be handled similarly, so any revert condition that exist for type two transaction would just be dealt similarly here.

**Guillaume**
Yeah I mean just maybe because my question wasn't very clear but if you try to access a contract that should be deleted under those new rules you know, what should happen and should it be different than what we do but okay it's just me thinking out loud here yeah I'll come back to it if it turns out to be problematic.

**Tim**
Okay any more questions comments on this one, otherwise we can move on to you the next EIP.

**Adrien**
Okay thank you for having me and feel free to ping me if you have any questions.

**Tim**
Sounds great and thank you for coming on.

### [EIP 7557 overview](https://ethereum-magicians.org/t/eip-7557-block-level-warming/16642)  [29:15](https://www.youtube.com/live/UTgnbE6jTuE?si=o-jS2KEEHcG4lSDQ&t=1755) 
Okay so next one is 7557 which Yoav was also asking to discuss so this is for block level warming, I don't know I don't think Yoav have is on the call but I don't know if there's another you are 

**Yoav**
Yes no I am here but Alex is also here and going to present it. 

**Tim**
Alex please yeah 

**Alex**
Hello everybody, can you hear me?

**Tim**
Yes

**Alex**
Yeah great, so I'll try to give a like brief overview of what we are proposing here. So in EIP 2929 and 2930 edited concept of warm and cold storage and accessing a cold storage was made obviously way more expensive than the warm one. 
However this distinction is only made on a transaction level and like if you look at the terms of the block, the same storage may be accessed by each transaction in a block and it becomes cold access for every transaction, which is not exactly the case, because the block builder only needs to look up this data once, and can reuse this data, so while we have a concept of access list, which is an information about which slots might be used in a transaction that is available outside of transaction execution, just as part of a transaction payload. 
So what we are proposing here is after the finalizing the block, when feeling it basically to iterate over the access list and build a table of how to redistribute the cost of accessing the cold storage between the transactions that actually access the same storage or the same addresses and to issue a refund in a way that is similar to maybe beacon chain withdrawal, like a system operation, they just inject value to the code after the block, not in the scope of a transaction, mostly because otherwise doing it as a refund is not really feasible, because then you give like there is a retroactive effect of the last transaction, has an effect on the first transaction.
So that's a high level view, like it's quite simple with a base fee because, it's just the same across all transactions. It gets a little more tricky with priority fee because like each transaction can pay different priority fee, so what we are proposing here is a like proportional distribution of the priority feedback, according to the like marginal contribution of each transaction to the amount that is being refunded, like it's similar but not same to chly values that are like used to define such things and yeah thats it, so yeah its especially but more important in the context of ERC 4337 and maybe like an EIP 7560 that we are working on that will make it native account abstraction, where many transactions are very likely to access the same slots within the block, and also like reference to, there is Verkle 3 EIP that is suggesting that accessing contract code will also be priced in, and in this case such an EIP would also be useful because we expect that many transactions will use the same like wallet implementation in the same entry point and it would be beneficial to just share this cost among the transaction instead of like each one paying full unjust price for it. Yoav, would you like to add anything?

**Yoav**
Yes, so basically the idea is to first of all, make the pricing fair, because to make the pricing fair, because the validator only pays once for a reading from the database and then it's already warm so it makes sense from fance perspective but also for commonly used for any commonly used contract mean account obstruction is one example, but there are many examples of contracts that are used many times during the same block so including them in the access list of multiple transactions, and sharing the cost I think makes a lot of sense. As for concerns that I've seen in the chat about parallelization, this EIP does not affect evm execution in any way because it's not visible.
The change of pricing is not even visible to the individual transaction. Instead, since we calculate it at the end of the block, we calculate and do a refund at the end of the block, similar to how consensus layer withdrawals show up in accounts. It should not affect, at least I don't see how it should affect things like evm parallelization.

**Tim**
Thanks Andrew?

**Andrew**
I haven't looked into this EIP in detail, but on the surface of it, it sounds like a bad idea, because it's like we will be spending time a lot on tweaking the gas, instead of making fundamental improvements to either UX, evm, or whatnot and as to batch transactions, we should address it properly, like with a mechanism to allow batch transactions, rather than trying to tweak multiple transactions in the block to work as a batched transaction. **Yoav**
I didn't quite understand the part about B, it's not about a batch transaction in this case…

**Andrew**
But I think one of the motivations that you mentioned is that you exactly batch  transactions, or maybe I misunderstood.

**Yoav**
Now batch transactions, we talked about it in the about the previous EIP, about 5806 this was the batch transaction, for this one, we're talking about sharing the cost of cold access to accounts and storage slots across multiple transactions that use them so…

**Andrew**
But essentially, those multiple transactions they because they will be you there is a need for multiple transactions because you cannot batch them that's what will one of the use cases. If you could batch them you don't need this tweak that much. 

**Yoav**
If you could batch them, I mean they transactions for multiple users, they just happen, let's say in the most common use case would be proxies, you have many proxies that use the same implementation so it doesn't make sense that in each transaction, accessing the implementation is called access because it was already loaded once. So these are not going to be in a batch because they are unrelated. They just happen to be accessing the same contract at some point. 

**Andrew**
Maybe that’s right, but another thing is now transaction pricing depends on the other transactions, like depends even more on the other transactions included into the block and it complicates gas estimations, it complicates transaction pricing, complicates a lot of calculations but doesn't help us to scale the evm, doesn't help us to scale the, through **Tim**
I guess yeah, and one question I had is, do you have a feeling for like how much gas is wasted here, like assuming we went ahead and did this, like what's the amount of transaction fees that you imagine we could distribute back to users?

**Yoav**
So yeah we didn't run a simulation to see how much it happens to a block but I did look at some at some blocks and see some contracts are accessed dozens or sometimes even hundreds of times. So, for example Uniswap, suppose you have I mean yeah in the Uniswap case it's probably going to save users a lot of gas and I agree that during estimation you will not be able to know it so you're going to overestimate, you're going to assume that it's called access but at the end of the block, there's a refund so I assume that in blocks that have a lot of Uniswap trade there's going to be significant gas saving for users.

**Tim**
Yeah I guess it would be useful to see numbers because like first there's like the breakdown between the base fee and the tip. Second there's like yeah how what's like the median like how much overlap is there in the median block versus like say the max block and I can imagine you would save more in cases like say there's like some new NFT that drops or some new like pool on Unisoft, it's like in the cases where the priority fees surge, you'd probably save more, but is that like, yeah if you put this like relative to all the transaction fees paid what percentage or amount does it represent? I think would be useful to know like is this worth the complexity.
Basically right yeah that's I think it's a good idea to run some simulations, and but also I think that some use cases will become more possible once we do it, so we may actually see patterns like usage patterns changing a bit but we can't know that for sure. So for now we should only measure what we can on the current blocks and I think that one another thing that we need to keep in mind is what happens after Verkle, because in Verkle there's going to be an increase in the cost of running contracts, because when you load contract, you're going to pay for the code loading per chunk, so now I know it's not finalized yet, we don't know exactly how the cost is going to be calculated but it will become more expensive to load contracts and and then if you can split the cost of loading the contract, it could be significant saving.

**Tim**
Got it yeah that might be also an interesting to run like if we you know if it's a smaller part of transaction fees now but then it grows a ton after Verkle, and that's yeah that's really useful to know Guillaume, you have your hand up, then Lucas?.

**Guillaume**
Yes speaking of Verkle, I mean I don't really have any comments on the intrinsic merits of this EIP but what I can say, this is the typical thing I would like to see after Verkle, not before, precisely because the gas model is already quite complex as it is, and this is going to make things even more complex. 
It might be nice to have although we have very specific model where every transactions precisely pays the cost of warming their state up so that would go against what has been specified and what we are used to, we've been working with for like three years now. I don't think we should even consider that for Prague or Osaka. It should really come afterwards and yeah it would make Verkle way more complicated than it needs to be already. 

**Yoav**
If it makes Verkle more complicated and we didn't think it's going to affect the calculation for Verkle itself. If it does, then it takes a second priority of course. 

**Guillaume**
I mean, I'm also happy to change my mind, but this is exactly what I said for EOF last time. I would like to see a demo of this happening on the Verkle testnet first.

**Tim**
Lucasz?

**Lucasz**
So first let me ask one question to summarize it up so it works the transaction Deion Works as usual and then at the end you look at the access list and potentially just add some cost back to some sender addresses, that correct? that how it works? or I missed something?

**Yoav**
Yes yeah you can see the EIP, there is a pseudo code of how it is handled so you can see exactly how we proposed to do it. Now of course we don't know, maybe there could even be a better calculation but the general idea is that yes you collect, first of all you only split the cost, you don't look at actual EVM execution because that would complicate things, so instead only transactions that have the slot or the contract in their access list get to share the costs if a transaction doesn't have it in the access list it's going to pay full price for a warming and then you split the cost across all of like if you had 10 transactions accessing the same having the same slot in their access list then you split the cost proportionally across these transactions, proportional to the priority fee and this happens at the end of the block only once.

**Lucasz**
And second question, would that complicate things for block builders because they kind of continuously can improve the block, for example revert one transaction at another right, at the end or something, like that would that complicate this kind of strategy for block building or generally building code?

**Yoav**
So since the calculation only happens at the end of the block after you finished, kind after you finished with the block, you can keep changing transactions and applying any strategy before you do this calculation, and also in order to keep it fair for the you order to keep it fair for the builder, for the block proposer we also didn't want to create a situation where if you add another transaction, you actually end up making less money because of this split cost, so the cost to everyone is actually derived from the cost of the highest priority fee.
So the builder is going to get paid, getting according to the highest priority fee, so hopefully it's not going to break the strategy for any block builders, but that's of course we need some input from h broke me 

**Tim**
Okay let's do one last comment and then we'll move on. Dankrad?

**Dankrad**
Yeah like I mean okay I'm not sure how it works but it feels like it could actually break stuff, if you have to run something at the end of the block to know how much gas exactly was paid and how much fees you get, but I haven't looked at the details but like more generally I was wondering why not like, it seems to be over engineered in terms of trying to refund it to everyone, why not just do it so that the first transaction does pay the full warming fee and then the other transaction is just like get it cheaper and get the warmed up slots, like yes it doesn't seem as fair as a bit of a lottery but it feels much more predictable and much less complex to implement, and it's still like on average you pay the same amount.

**Yoav**
So first of all since the refund is not a transaction it's a more like a consensus layer withdraw, there is no execution at the end of the block you just collect the numbers and then you divide it in the end and do the refund but as for what was your other comment?

**Dankrad**
Well I was wondering why like okay like here's about fairness about fairness yes simply just like considering all the all the slots that have been used by previous transaction as warmed up so then it's exactly predictable what happens at the start of each transaction execution and you don't have to do anything complicated at the end of the block it's less fair but on average it gives you the same result right?

**Yoav**
Yeah it gives the same result except that like you said it's a lottery?

**Tim**
Well, first it's not a lottery, because in practice if there's like contentious access or like in demand access for some part like it's maybe because there's like some Arbitrage, or some like profitability so I think it would be interesting to look at that but I feel like for a lot of those you would just see, it's like you're taking away from the Mev profits if you're taking it from the first transaction in the block which might be fine.

**Yoav**
Yeah of course it's yeah in these cases like in in the cases of when there is m contention around some slot it makes perfect sense that the first one that also pays the highest priority is also going to pay for the warming, that's fine but in the case of a proxy implementations, for example let's say in the in the account obstruction case where you have many users many users using a wallet with the same implementation, it may be less fair that one user pays for warming for all the other users.
So we could do it this way does simplify things it also makes things a bit less predictable for users.

**Dankrad**
Right and I think like that makes a big difference, whether that's like there a 200% variation then I see your point but if it's like say a 20 30% extra cost for transaction, then it feels over engineered to me. 

**Tim**
Okay, Lucasz?

**Lucasz**
So I think, actually the current proposition is simpler to implement and simpler to parallelize because it doesn't depend on the full block order, it just at the end turns some funds to the transactions based on the access list if I understood correctly. So what Dankrad is proposing is actually a complicating parallelization, for example a lot and because you have to track the access patterns across the whole block in order which you don't have to with this proposal, so it's actually in my opinion easier to implement and easier to to parallelize in the future.

**Tim**
All right, thanks. Sweet, thank you. Okay next up, I guess yeah Danny you had your hand up but then took it down was there still anything on this?

**Danny**
I just was going to mention that like the asymmetric strategy where the person one pays for it like a builder could pick a user transaction to warm something up and have somebody pay for it and then insert their transactions to use the warm but again like if we're talking about marginal differences, I don't think that strategy matters too much, but I think the parallelization and asymmetry comment previously is important.

**Tim**
Got it thanks okay next. 

**Peter**
So just sorry one very quick note that if we introduce anything where basically execution of the cost of a transaction depends on transaction before it, another issue that you might introduce is gas estimation issues because all of a sudden if your gas estimation runs in a certain context and during a block execution, you change the context, you might end up with basically fail transactions.

**Yoav**
That couldn't happen if you only do the refund at the end of the block, it's because you have to assume that you're going to pay the full warming price and then if you are not alone and others also share the cost at the end of the block, you get something back, but it cannot cause the execution to fail because during execution you're not even exposed to this information.

**Danny**
Yeah, I think that was an argument against the asymmetric version that Dankrad proposed.

**Yoav**
Oh yeah I understand. Okay.

**Peter**
I’m not necessarily saying it as an argument against either version, rather what I'm kind of saying is that this kind of means that during gas estimation, so currently what the gas estimators do is that basically you have this previous state, which is either the latest block or the currently pending block which whatever it means for a client, and then people just run estimate gas transactions on top, and that might get wonky, so basically just the only thing I'm seeing is that gas estimation needs to take care that it's estimating on top of a clean slate, and not this partial warmed up thing.

**Yoav**
Oh yeah in during estimation you should you should not assume anything about this, it's like maybe you'll get something back, maybe you want to but you have to assume that you're going to pay full price during estimation otherwise stuff is going to break.

**Peter**
Yeah of course but the point is that the gas estimator is just a dumb thing which takes a transaction runs it against a pending block or a pending State and just spits out the gas value it doesn't know anything about anything and so basically, so currently the gas estimator is kind of dumb and such a feature would require the gas estimation to be a tiny bit smarter so as to basically know about this refund mechanism and make sure that it doesn't interfere.

**Yoav**
Actually I wouldn't want to know about it.

**Tim**
I'm sorry, yeah I think there's clearly like more discussion to be had on this if we went forward with it but we do have a bunch of other EIPs, so I would table this for now, move to the rest. 
Yeah sorry to cut you off, but I want to make sure we can cover most of stuff. Yeah thanks Yoav for sharing this. 

### [EIP 2935](https://github.com/ethereum/EIPs/pull/8166) [53:32](https://www.youtube.com/live/UTgnbE6jTuE?si=o-jS2KEEHcG4lSDQ&t=3212) 

Next up we have 2935, so this is the Verkle related one. I don't know Guillaume, do you want to give a background on this?

**Guillaume**
Yeah I even have a tiny presentation, I promise I'll keep it short. Can you guys see my screen?

**Tim**
Yes.
**Guillaume**
Okay cool. Yeah so we have this EIP that was initially created by Tomas and Vitalik which is about storing the historical block hashes into a contract or the contract storage more exactly and it's been stagnant or stalled for a while and we discovered while working on the Verkle testnet that we actually needed this for well for stateless clients to execute.
And the reason for this is because you would need to somehow pass the historical block hashes and either you pass it on a side channel but they definitely need to be part of the proof and we know how to do proofs so it looks like the perfect EIP just needs to be updated, so we created this revival PR to like 8166 which is to yeah just meant to update it, because it's quite old, it used to be a like block number based we now it's time stamp based and there were some fairly complicated things. 
I mean things that were not necessarily complicated at the time but now that forks are time stamp based, it got very complicated, so the gist of the update is really to say once the EIP is activated you just take the 256 ancestors and you insert them right off the bat into this contract, which is really simpler than the proposed version until now.
I mean once again it was meant for a different fork model and you no longer like the other major change is that in the initial description, you had to wait 256 blocks after the fork to be able to use the contract. Now with this new approach, because we insert all the historical block hashes that we need we don't need to wait, so you can start using them right off the bat. 
What doesn't change and this is something that is going to probably create some push back, but let me explain why it doesn't change. 

Unlike the beacon hash contract the 4788 contract, we don't want to use a ring buffer and in fact the argument is that we might actually also have to give up on the ring buffer for 4788, we are still gathering information but the reason behind this is because well okay first this whole EIP was created to be able to access historical block hashes and so that would be really hijacking this EIP if we did not provide that, and the other reason is because hashing in a Verkle context is way more expensive, and takes way more time than it does in a kak or Kack context and so we feel that an attacker could potentially increase the depth of that ring buffer in the tree, and therefore for relatively cheap make block production slower in the future.
So this still needs to be confirmed, we're working on getting data to confirm if this is a problem or not, but until we have not confirmed this is not a problem. I think not using a ring buffer is actually the best approach, because then it will move in the tree and so it will make the attack more expensive.
We also considered putting all of the data during the Verkle transition but we decided so I mean all the historical hashes during the Verkle transition but I think it's not really useful unless there's a clear use case for that and we also didn't want to do any solidity implementation, so it's just at the beginning of the block, writing the contract that's what's specified in the initial version of the EIP, and we want to keep it this way.
Yeah there's a couple discussion points, what address should we use, yeah like for example, I mean we don't want necessarily to use the one that's currently specified in the EIP. The EIP 158 currently deletes every contract that has a zero nonce and zero balance so we in our implementation, we had to create an exception, and yes currently it's deployed. The first time it's being accessed but we could change that if people disagree.
Just want to point out that it has actually been tested, it's currently tested, the bar prevents me from showing the other tab, here we are, so if you look at kelen so this is the block Explorer for kelen and you have a Stateless tab that tells you what gets touched and if you look at the first slot use, I mean okay if you're not really familiar with Verkle, most of those numbers will not talk to you but basically this is the location of the first slot in the contract, the suffix is 64, that's normal, I mean once again if you don't know Verkle, you don't care about this number and what you can see is the new value is some hash, and that happens to be the Genesis hash which is right here exactly, so yeah so just to point out that that it's working.
So yeah why would you consider that in Prague? Well okay, the first argument is that it's easy to do it's already implemented, it's being tested, it's necessary for Verkle, and because I was explaining the trick of inserting 256 ancestors at the fork block, it's not conceptually very hard but this is something I would like to avoid doing when the transition starts so that would be the reason why we would be pushing for this in Prague and yeah that's pretty much it.

**Tim**
Thank you and Danny has his hands up?

**Danny**
I definitely support this I would be curious to hear a bit more about the ring buffer argument maybe later after you done some analysis but I just want to point out on the consensus layer, this we've had the design principle since zero that the state transition be should be a function of pre-state and block and no other explicit or hidden inputs and so I'm a major fan of the execution layer moving in that direction for the statelessness reasons, but I also want to just elevate it as a design principle in general, and when people are designing EIPs to think in that mode because I've seen EIP drafts where you know they'll assume access to some maybe the parent block or something like that but anytime that we want to do that kind of thing, we should be writing it into the state to elevate it into this kind of stateless mode so just a comment and definitely support it. 

**Tim**
Thanks any other questions comments? Danno?

**Danno**
Yeah I'm still wondering how using a ring buffer introduces new attacks scenarios that storing everything in history supports. 4788 works, it's out there you can't change the numbers, it's not going to get any larger than storing all of the history and it has a process that is already established and work, we just change it with a different contract address and a different value we put in. So I'm wondering why that simpler solution is not preferable. 

**Guillaume**
So yeah, right now it's working that's precisely the thing because the hashing you use is SHA-3 based and currently you don't see the problem but as soon as you switch to Verkle, we need to get more data we're working on it we'll get them as soon as possible but if it's confirmed that greatly increasing the tree depth is going to be a potential attack your ring buffer will and I'm talking about the one in 4788 will be attacked. Now what do you need to do if you want to change it, you have to 

**Danny**
Can you define attack like is this and if you manipulate the beacon block roots then you can change the depth of the rain?

**Guillaume**
Yeah no you just need to create a contract because everything ends up in the same tree, all you need to do is to find a account to slot whatever that will hash to the same prefix as the stem or the PA to the ring buffer in the tree and as soon as you get that, you can artificially increase the depth of this ring buffer, which means you will need to compute more levels of commitments and that means it might potentially make things really much longer to compute.

**Danny**
And how is this different than targeting high use contract? Obviously this is system level and it must be, it's going to be updated every time in hash but why is that different than something that just has very high usage? 

**Guillaume**
Exactly. It's not very different from any high usage contract, in fact Peter pointed out that you could do the same thing on a Gateway contract, for example, but the system contract is like this system contract is executed on every single block so you could do this and attack, for example a competing app and they would have to redeploy and everything Dano talked about, so that's a pain but if you start attacking the system contract, you would have to do a new fork to fix it, and that's a bit more involved so that's why we would like to avoid that and as it turns out

**Danny**
Yeah if Uniswap is attacked like this, does the cost of executing Uniswap become more expensive or is so cost in terms of gas or just cost so they have no incentive to like re to move it similar right?

**Guillaume**
It's just in terms yeah that's true Uniswap itself doesn't have to, has no incentive to move it but people that client developers that see the time frame getting closer and closer to the limit, the block production time getting closer and closer to the limit, we'll have an incentive to change that

**Danny**
And what but they have no control over that.

**Guillaume**
They have no control over that no 

**Danny**
So they have more control over the system level contract probably than attacking the application there okay yeah I'm still wrapping my head around it. Thanks

**Guillaume**
Sure and but what I was getting at is if you get rid of the Ring buffer you will automatically move those this target all over the tree so it makes it very expensive to attack because you really have 256 blocks to find the collision and then it's only effective for 256 blocks and then you move to another part of the tree where you have to start over so it's way more expensive.

**Danny**
The cost of linear state growth on the system contract right?

**Guillaume**
Yes absolutely.

**Danny**
Got it. Thank you. 

**Tim**
Okay, lightclient?

**Lightclient**
I mean I'm just kind of echoing what Danny said, I don't really see why this is a specific problem for the system contracts. I think this is also a huge problem if it significantly is affecting block production time for any kind of Dapp. I don't think it's reasonable to expect dapps to go into some PVP battle where they're expanding state branches around the contract and then forcing others to redeploy.

**Danny**
Sure but especially if the gas cost doesn't escalate.

**Tim**
But also some apps just like can't and shouldn't redeploy right?

**Danny**
Yeah I'm not I'm not saying they should but they don't even have an incentive to because it's not going to even show up in their gas.

**Tim**
Yeah or I mean you know we have the deposit contract as well like yeah there's plenty of contracts that get used in yeah Andrew?

**Andrew**
Yeah well of course we have to figure out whether to include the ring buffer or not but in general I support inclusion of this EIP into Prague. It makes sense yeah do before Verkle.

**Tim**
Yeah, Peter?

**Peter**
So just circling slightly back to this attack vector. Basically my concern was kind of the same that whether we use a ring buffer here or a non-ring buffer I kind of feel that if the attack is viable on the ring buffer, then we will have bigger problems, because I can basically target any high profile proxy contract and make it super expensive and if basically targeting Uniswap is, my point is that if the attack works then both attacks will be very potent and if it doesn't work then it doesn't really matter.
Then we can just keep the ring buffer so I that's why I was kind of suggesting that we should really have a number on how effective or non-effective this attack is, because I kind of feel it that you cannot make an attack ineffective on Uniswap but effective on the ring buffer, so it's going to be both or none and we should really keep this.
I mean I really like the ring buffer approaching that the state is kind of constant, I really like constant stuff so changing it to a non-ring buffer would really need some motivation and I think the problem is that the motivation that would prompt the ring buffer to be swapped out would also be a huge problem for the Dapp ecosystem in general, so it's I think that issue is a bit deeper than just changing the data structure here. 

**Guillaume**
Just to be clear I mean I agree with most of what you said but we're not changing like DS change like switching from a ring buffer to something else, should be completely transparent to devs, because they would just ask for their block number and they would they don't care where it's stored. They just want their block number so it's really how the storage is laid out that changes. 

**Peter**
Yeah of course but my point is that if the ring buffer needs a change because otherwise it can be attacked then so can Uniswap’s proxies contract and any proxy contract and you cannot really I mean with upgradable contracts you can redeploy the implementation itself but you still have one proxy which is kind of your entry pointer into the system and that's the thing that you can attack and you can't deploy that unless you actually change the contract address of Uniswap and I mean that's going to be a huge pain. Nobody's going to do that, so my point really is that if this attack is realistic, then we have to rethink big things. If it's not realistic then the ring buffer is not relevant.

**Tim**
Thanks Peter, Danny?

**Danny**
Yeah I was say very much agreed with Peter like this is either fundamental and affects both or not either so I would say you know if there's a write up if there's numbers on like us being able to wrap our head around this attack in general, system contract aside, it seems like very important to the Verkle conversation, you know rather than it more in the abstract, I think Anar said you know potentially doing simulations where we mining maximally adversarial depths might be important but it just seems we need to elevate it to a fundamental concern rather than like a system contract concern but I think we're many of us are saying the same thing this.

**Tim**
Got it. Thanks, yeah I think this is probably a good place to wrap this one up given we still have a couple more EIPs to cover, but yeah thanks G for sharing in I think it was a useful discussion.

### [EIP 5920](https://eips.ethereum.org/EIPS/eip-5920) [1:11:26]( https://www.youtube.com/live/UTgnbE6jTuE?si=o-jS2KEEHcG4lSDQ&t=4286) 

Okay so next up we have two EIPs which we were going to discussed last call and didn't have time for so Charles is on to discuss them. First is the pay op code and then the second is a transient storage reduction.
Yeah Charles, are you on the call? Yes, hey, I'm Charles I work on Viper. I want to advocate for the pay op code, which was considered last time for Cancun, but it was deferred because of complexity, but basically just to give a quick gist of it, it's a way to transfer ether without transferring calling context and I think this is just generally important because sending ether shouldn't have to transfer the call in contact because the called contract can like do whatever it wants.
One of these things that it can do is of course re-entrance the attacks and it's just a huge foot gun for users in general and if we have a payoff code then an entire class of smart contract vulnerabilities can be mitigated. I think one issue kind of that's been brought up is that you can do the same thing by creating a contract and then self-destructing it, but first of all it's like a kind of a hack and second of all we know that the semantics of self-destruct are kind of always in flux so I don't think that users should have to depend on the semantics of self-destruct to do a specific thing, and in fact people relying on this behavior forces us to kind of forces self-destruct to actually be a little bit brittle in that it can't be changed as much. 
So yeah that's the overview and the motivation for it I can go over my second EIP.

**Tim**
Let's maybe just get the questions or comments on pay and then we can do the other one just so yeah we can keep them separate so yeah any thoughts, comments on 5920?

**Andrew**
Yeah I think it's a simple EIP and it's a nonrival improvement for the UX so we should include it.

**Tim**
Thanks. Any other thoughts, comments? Okay if there's not, I think we'll punt the discussions of like what we actually include a bit later and maybe next call based on how it's going so far, but yeah we can go over the second EIP.

### [EIP 7609](https://github.com/ethereum/EIPs/pull/8158/files)  [1:14:45]( https://www.youtube.com/live/UTgnbE6jTuE?si=o-jS2KEEHcG4lSDQ&t=4485) 

**Charles**
Okay cool. The second EIP is it's still a draft, which I just threw up recently because I realized that we're discussing Prague already and basically the core motivation is also kind of branches related but basically transient storage in my opinion is overpriced and the reason it was priced the way it was, and it's of course too late to change for Cancun, but the reason it was priced that way is first of all it's like kind of concept, the same as warm storage, sorry it's not the same, it's conceptually similar to warm storage but there's important differences and also there's some discussion of Dos so you don't want people to be able to allocate too much memory on a client, and I think in EIP 1153 there was some discussion and calculation of like how many slots you can allocate given that pricing, so I think it's fundamentally over priced because it just doesn't require as much resources as warm storage.
Yeah it doesn't interact with refunds and it doesn't interact with the physical database you don't need a new allocation every call you only need an allocation when you touch a contract for the first time I also did some benchmarking with Revan and it seems to be just compared to other you know relatively speaking it should be about 10 times cheaper to address the issue with allocating too many slots. 
I added this kind of super linear component so that every time you allocate a new transit storage slot you pay an increasing amount so if you want to allocate like 100 Keys then you need to pay you know three gas for the first key, six gas for the second, and so on until you're paying 300 gas for the final key, and I think for most use cases this decreases the cost of transit storage for users.
Interestingly, it actually decreases the total amount of transit storage you can use, which I think is good for clients because you know they have like stronger caps on how much memory you can allocate and I have the calculations and all this stuff and benchmarks in the EIP and the Eth magician so I think we can open for questions.

**Tim**
Yeah thanks, Andrew?

**Andrew**
Well you know my position is against weakening the gas schedule unless absolutely necessary because in my mind we have much bigger fish to fry. We need to somehow tackle the scalability issues because if we don't, it's we can like have a super precise work and guess she cannot be super precise because you have different client implementations, but even if it's more accurate than what we have now it still doesn't help us much because it doesn't help with this with total throughput unless so yeah we should focus on actually improving the total throughput rather than tweaking the gas schedule all the time.

**Charles**
I don't think it's exactly a tweak I mean it kind of is like uh quote unquote micro optimization but I think it's a fairly easy to change to implement and it allows compilers to and users to implement global re-entrancy walks, so re-entrancy can be mitigated by default instead of people having to opt into it, depending on if it's cheap enough, and I think it's 2024. You know we have the capability to prevent it, and you know make the evm modern. I think it's an easy and fairly inexpensive win. 

**Tim**
Okay any other questions comments on this one if not Mike you wanted to talk about inclusion list right?

**Peter**
Can I just quickly add a very very short comment, so I was I kind of also agree that it's a micro optimization and we shouldn't really go very very deeply, on one hand on the other hand I think if these micro optimizations are simple enough then, I mean if it takes 5 minutes to implement or 10 minutes okay I'm being deliberately very extreme here then, even if it's a micro optimization, I don't think we should necessarily say no because we have bigger fish to fry.
I mean sure if it's a big enough effort then yes, but if it's very very trivial, then I think it's it could be a valid consideration, now the catch on the other side is that basically the suggestion I mean making transient storage cheaper all together, I mean that's super easy to implement now, making the cost steered as to how many slots you allocate, that gets a bit I think you enter into this territory where it gets a bit wonky, because okay, you say that the compiler could generate these re-entrancy locks super cheap, yeah but if I call a big enough stack of contracts then already I'm going into this okay every subsequent T store or slot gets a bit more expensive, and then if I have a deep enough stack of contracts then this thing gets starts to get expensive, and it starts it's kind of harder to reason about.
So I don't want to challenge this specific design because I haven't studied it so please don't take it as a specific attack on this design, rather I think basically if this EIP can keep the modifications needed and the mental model needed simple and I think it's perfectly fine to include in some form but the more complex gas mechanisms it includes, the harder it is to rationalize the optimization. 

**Charles**
Yeah and in the EIP I did do the calculation for like how much memory you can allocate if you do T store on a single contract versus like if you do this wonky nested thing and you try to like optimize, as an attacker you try to optimize how much storage you can allocate another suggest and I'm quite open to feedback on the design but I just would like to see it in some form being included, something that decreases the base cost for transit storage.
Another suggestion was to just keep the gas price flat and then just introduce a harm limit on how many slots can be allocated, and maybe I'm not a client developer so maybe for clients that's easier to implement. I don't know again I'm open to feedback.

**Peter**
So I would probably say that introducing a hard cap would be very very problematic. It's kind of like with the hard cap on the stack limit that it's just very annoying when solidity tells you that okay some stack limit exceeded or something so it's, ideally you want to avoid these hard limits so I think raising the price is infinitely more preferable than just throwing or basically aborting execution, because you reach some arbitrary limit.

**Charles**
Okay thanks Peter. 

**Tim**
Yeah and thanks Charles for presenting the two EIPs. I'll move us on the inclusion list because I want to make sure we can cover it. Mike do you want to give some context and then share the info on the breakout tomorrow?

### [Inclusion List](https://github.com/ethereum/pm/issues/954) [1:23:36](https://www.youtube.com/live/UTgnbE6jTuE?si=o-jS2KEEHcG4lSDQ&t=5016)  

**Mike**
Yeah thanks Tim and hey everyone, yeah I guess I probably only need like a minute here and all I wanted to call out was kind of two documents. I guess, the first being this is spec overview this is kind of taking the some of these unconditional design properties that I mentioned two weeks ago and trying to put it into the spec for the consensus execution APIs and the EEL spec the eel spec, so yeah I guess the only other thing to mention iss the call that Tim brought up, so you know this is scheduled for tomorrow at the same time as the beginning of the all core devs.
I think there'll be kind of both consensus teams and some execution layer teams there so if you're curious and kind of like want to want to know more I'll probably start by just running through the spec doc, and then happy to kind of take questions and brainstorm and think through what might make sense, so yeah I think that's all I'd like to share. Thanks Tim for the floor. 

**Tim**
Thank you, any questions comments in advance of the inclusion risk? Okay so we can chat about this tomorrow. We only have five minutes left and we've discussed a ton of EIPs today and so I think what might make sense in terms of next steps is to not try and like figure out what we include in Prague today but give teams like the next two weeks to think through this and then maybe two specific things are one we had CFI 2537 last time, and we moved all the other EIPs to include it once the CL devs plus one them but 2537 is the only one that didn't require any CL help, so anybody object moving it to inclusion so that we can clearly have it part of the fork?

**Danno**
I think it should be in I think we just need to revisit gas costing on it but other than that I think it's a good add.

**Tim**
Okay last call for objections, okay, and then the other thing I would propose so we discussed 5806 today and then 3074 and I know that in the past we talked about wanting to do something around just like better account UX, but not really being your line on like the strategy or like if we do a single, how does it fit in like the broader account abstraction road map? So would it make sense to have a sort of account abstraction EOA upgrade management breakout room, in the next two weeks before the next ACDE, so that we can discuss that in more depth, maybe have some wallet devs and some application devs joined?
So that you know if we do want to do something whether it's like 3074 or 5806 or whatever like at least we've sort of gone down that rabbit hole a bit more.
Yeah any interest for that sometime in the next two weeks? 
Okay so there's some plus ones, okay I'll propose the time after this call, because I want to make sure we can at least ping a couple wallet devs and other folks to see like when they can attend, but we should have this like, before the next ACDE, and ideally probably sometime next week, so that like there's basically a week between when we have this AA breakout and when we have to make the final decisions. 
Yeah anything else people would like to discuss before we wrap up? 

**Peter**
Yes yeah, basically just a very short note. I'm not sure whether the de already mentioned this or not that he was kind of a bit concerned that what we're kind of targeting for this hard fork to be very very short so the next big thing being Verkle, and maybe something I wanted to voice his concern too, is that we usually suck at estimating when artworks should ship and what we should cram in and not cram in, because obviously everybody wants to cram in as lot as possible, and basically just to try to keep things on track, perhaps it would be helpful to try to at least guesstimate when we want the next hardware to ship in point of date and then based on that try to cram in as much as possible, but try to enforce that date so that it doesn't really overflow by one more year.

**Tim**
Yeah and I think people like definitely agreed with that. I think the rough sentiment I've like gathered is people want something to ship this year and so yeah like this means and we haven't started working on it, so you know assume that like Dencun goes live in a month. It means there's only like nine months left to the year at that point, so if we want a bit of buffer like it should be something we think we can probably get done in like six months or less, and then we know maybe we'll get it done by the end of the year so I agree. Yeah that's something that we should consider when planning to scope for Prague. 
Yeah anything else before we wrap up okay well thanks everyone I'll coordinate the breakout for the AA stuff on the Discord and talk to you all next week.

## Attendees
* Guillaume
* Tim Beiko
* Danno Ferrin
* Alto
* Linds
* Justin Florentine
* Ignacio
* George Kadianakis
* Gary Schulte
* Barnabus Busa
* Peter Garamvolgyi
* Ben Edgington
* Draganrakita
* Marek
* Toni Wahrstaetter
* Pooja Ranjan
* Guru
* Mikeneuder
* Mehdi Aouadi
* Francesco
* Daniel Lehrner
* Anny
* Ben Adams
* Carl Beekhuizen
* Ameziane Hamlat
* Paritosh
* Mrabino1
* Enrico Del Fante
* Echo
* Jochem
* Terence
* Andrew Ashikhmin
* Mario Vega
* Zach Kolodny
* Roman
* Lukasz Rozmej
* Dankrad Feist
* Hsiao Wei Wang
* Stokes
* Lightclient
* Yoav
* Hadien Croubois
* Saulius Grigaitis
* Shahaf
* Ashraf
*Carl Beekhuizen
* Trent
* Ignacio
* Alto


