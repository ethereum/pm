# Execution Layer Meeting #156
### Meeting Date/Time: Mar 2, 2023, 14:00-15:30 UTC
### Meeting Duration: 1hour 30 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/729)
### [Video of the meeting](https://youtu.be/GNhrb5txJ4M)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)

## Intro [2.49](https://youtu.be/GNhrb5txJ4M?t=169)
**Tim Beiko**
* Okay, we are live, for ACDE #156. Many things on the agenda today. Talking about, Sepolia obviously, and then, what we wanna do about Goerli, potentially main net. then Peter had a bunch of, client related topics, that it would make sense to go over. And then finally, some updates on Cancun. 
* So we had some breakout yesterday, and then there's some EIP that are, starting to wanna be considered for the upgrade. So I think it's sort of challenging a bit about like how we wanna approach that. And then, there's a couple eip, to discuss today. but I guess to start, does someone want to give a quick recap of Sepolia this week? 

## Sepolia Upgrade Recap [3.47](https://youtu.be/GNhrb5txJ4M?t=226)
**Pari**
* Sure, I can go. so we had the Sepolia fork on Tuesday early morning, and we had a couple of BLS changes lined up just before the fork, and they were executed as expected. After the Capella Fork. We noticed some participation dropped immediately after, but it was mainly due to, some validators running an older version of the EL and updating it, resolve the issue. 
* The BLS changes made it on change as expected, and we did have one full withdrawal as well. mainly the reason for such a low number of changes in withdrawals is that the validator set is very small, but everything seems to be functioning normally right now. 

**Tim Beiko**
* Nice. Any other comments? 

**Marius**
* There was some issue, some bad block created by, Nethermind. if, Nethermind I could talk about it. 

**Marek**
* Yeah, we produced a few bad blocks on Sepolia, what can I say? It's definitely not related to Shanghai, it's some kind of regression. it's not like, we produce it, every time, but only, a few of them and I think we will fix it soon. 
* But I can't share full details because we are still investigating it, but of course it shouldn't affect any hard fork. Yeah. 

**Marius**
Is something very Nethermind specific or is It

**Marek**
* Yes, It's how we produce block and I'm not sure if it's possible at all on a, when we have less validators than on Sepolia, but yeah, I will explore it more. I can, share details later, but, yeah, we need to investigate it more. 

**Tim Beiko**
* Okay. Any other team ran into some issues or had anything they wanted to highlight? Okay, then, oh yeah, please. 

**Marek**
* What about this meta mask thing? Is that fixed? 

**Tim Beiko**
* I don't know if it's fixed. Someone from Meta Mask replied that, they were using, I believe each Eth get balance. and so it's not clear if it's an issue with the JSON RPC implementation of that in a specific client. and yeah, maybe they give just some background. 
* So meta masks seem to have an issue re-updating user balances when withdrawals happened, which, you know, ether scan or others like would do correctly. but I don't know that we found like the root cause of that, 

**Pari**
* At least the symptom seems to be fixed. If I checked the wallet on meta mass right now, it shows the right balance. 

**Tim Beiko**
* Oh, okay. 

**Pari**
* So I'm not sure if it was a caching thing or if they pushed an update or it's fixed or what happened, but yeah. 

**Tim Beiko**
Yeah, and I guess it's, oh yeah, Marius, 

**Marius**
* That's, that's good to know. yeah, so I checked, in with the Geth client on Sepolia and it works. So I think every client team should just double check it, that everything works fine. And then I would consider this issue like resolved. 

**Danny**
* Yeah, double check the get balance endpoint is what you mean. 

**Marius**
Yes, yes. It's, it's a five minute thing. 

**Tim Beiko**
* Yeah. And if there's any wallet developers or anyone who works with Balances listening to this, basically the withdrawals are not a user transaction, so if you're like scanning user transactions to get a balance, withdrawals would not be counted as part of that. So get balance, should work. but yeah, withdrawals are not like a specific transaction in the block that, you can kind of fetch.
* And I think that was the only sort of infrastructure level issue we saw with Sepolia. Was there anything else? 

**Pari**
* Nope. I think that was the only one we saw, but most of what we see on Sepolia would also be reproducible on Shanghai. So, please test your infrastructure. 

**Tim Beiko**
* Nice. 

**Marek**
* Yeah, one more thing on Sepolia, we could, we could, could consider adding more boot notes because, Ahmed from our team, was testing all EL clients and all have some problems with finding peers, etc, so we could add, more boot notes to help with this issue. 


**Marius**
* Yeah. We also had some similar issue also because no one, except for Geth is able to, snap serve. it's kind of very difficult to sync on Sepolia, because we don't have many peers that are able to serve it. and so yeah, it would be really, really good if other teams could implement Snap serving, as soon as possible, so that we don't rely on one client for, for all of Snap and, yeah. 

**Tim Beiko**
* Okay. yeah, so Snap serving and if we can get more people to run boot nodes on the network, that would be great. I don't think those two things are pretty, unrelated to Shanghai though. So just, I guess to be clear, is there any other like Chappelle related issues we saw in Sepolia or concerns that teams have? 

## Goerli Upgrade Date [11.24](https://youtu.be/GNhrb5txJ4M?t=684)
**Tim Beiko**
* If not, I guess I'm curious how people feel about, Goerli. should we go ahead and set, time for it? do we wanna do Goerli first and then, wait to see how that goes and then schedule mainnet? I know Perry, you had a comment basically proposing two epoch, one for, March 14th and one for March 22nd. yeah, so I guess I'm curious to hear just from different client teams what they think the next, like the best steps forward is here. Is it just Goerli, Gordian, mainnet, and, when, you know, should we aim for these, Ahmad? Oh, we can't hear you. 

**Ahmad**
can you hear Me now? 

## Goerli Upgrade
Yes, we can. Yeah. 

**Ahmad**
Ah, okay. so, speaking of Sepolia, during, when we faced some problems with peering, when we tried to find peers in Sepolia to think the client, that is not related to Chappelle at all, but we Already talked about it. 

**Marek**
Ah, Okay. Sorry, I missed That. 

**Ahmad**
No worries. 

**Tim Beiko**
Matt, Yeah, 

**Matt**
Back on the original topic. our suggestion would be to just set Goerli date today. I have a feeling that when a lot of the public validators are testing, we'll uncover a slew of more issues, but that's just a hunch. 

**Tim Beiko**
* Okay. And do you, does Besu have a preference between the two dates? Like, I mean, more for the 14th versus like 22nd or so? 

**Matt**
* It doesn't really matter too, too much for us. We didn't have very many issues at all with Sepolia and, we can adjust our release timing for either, selfishly the later date is always better in my opinion, but the neither will be, there's a weekly held opinion. 

**Tim Beiko**
* Okay. And I guess, yeah, so for the, to hit the earlier date, so that's like, 12 days from now, it means that like in the first half of next week, we'd have to like put out the, pull out the blog post, and so we'd need like client releases, you know, in the next like four or five days. yeah. Danny?, 

**Danny**
* Just a quick comment on the dates or the epochs chosen Perry, you mentioned that it would be a Sink committee boundary, which I don't think we really care about. On the Consesus layer side, we care about it being a historic roots boundary, which I believe are on like 8,192 slot boundaries. So it does rotate, but you can get one about every day, unless those boundaries are in sync, which would be funny, but, so we should check epoch against that rather than against the, Yeah, and I think for Sepolia we got one that was both basically, okay. Maybe they, maybe they're always in sync. 
* Yeah. If, if, I'm not sure. Yeah, if someone wants the sanity check, the exact numbers, that would be great. 
* Okay. I'm, I apologize. They're always in sync. Okay. but I guess the reason we're doing it is because of historic roots. Got it. Not sync. 

**Tim Beiko**
* Matt's your hand was still up. Did you have something else you wanted to add first? Just forget. Nope, Sorry. Okay, all good. Marius, I see you've come off mute. 

**Marius**
* Yeah, it, for us it's, I think, having early date for Goerli is, the earlier date is better because then we have more time, between Goerli and mainnet. from my point of view, we could schedule mainnet and Goerli at this now. but if other client teams don't like, are kind of scared about it, then it's fine to do one and then the other. 

**Tim Beiko**
* Okay. yeah, there's a proposal in the chat from Marek, what about like around the 16th for Goerli? So more like the Thursday than the Tuesday. if we did that, I guess the, the difference with doing that is like, if we do it on the Tuesday, then we know by like All core devs on the Thursday how it went. If we do it on the Tuesday, on the Thursday, at best we get, you know, maybe a couple hours before all core devs, to see how it went. So it, you know, the, the potential risk is like to delay the fork two days we might delay. I see. Analysis like a week. Yeah. got it. Got it. Yeah, 
* So I guess so far it seems like people would rather have Goerli a bit sooner and potentially split out the main netrelease. Does anyone disagree strongly with that? Okay. in that case, so the epoch that, you had proposed Perry was, 162304. if we can just sanity check that this, I guess what time this happens and, whether it's a historic roots boundaries, I think that would be good, but any objections to that otherwise? Okay. It doesn't seem like it. And let me scroll down on Adrian's 162304, 162304. So it would be at around 10:00 PM UTC, which is 3:00 PM Pacific. there's no European, I guess that's, yeah, it's like , late Europe, , early Australia and, midday, US. Yeah. Potuz?

**Potuz**
* Yeah, so, what are more lessed timelines that we had because, so we're gonna be working into weeks in Goerli and then we will need at least one meeting to set up the and then we'll need some time to soak clients for, mainnet. So, so I'm not sure what was the consensus on how much time do we want between release? I'm waiting for, for people to upgrade and whether or not we should be talking about at least tentative dates now. 

**Tim Beiko**
* Yeah, I mean, the April For main net, we usually want to give people at least like two weeks after the announcement. That seems reasonable. So like imagine, you know, Goerli happens on the 14th, and then everything goes well on the 16th. we agreed to move forward with MainNet. you know, I think the earliest that puts us as like the first week of April, basically. 

**Potuz**
* Yeah, well, I was counting at least the second, like sort of like a month after after Goerli's work. 

**Tim Beiko**
* Yeah. I think that's interesting, right? Yeah. I, at least to me, I don't know if anyone feels strongly. 

**Potuz**
* Yeah. Then I don't see anything wrong with not, not bling this. 

**Tim Beiko**
* Yeah. I don't think it should be as close, you know, like I think it's, it's fine to move the test net and like quicker succession than we, we move main net, but basically, okay. So I guess, I'll open a PR for, the, EPOCH 162304, and then, yeah, we can, we can go with that again, assuming that, I'm pretty sure the Matt checks out for the, for the Roots battery. and, yeah, if clients can have a release, either you know, tomorrow or early next week, that would be great. 
* Then we'll put out, the announcement, around midweek next week. Still let people know, but, people should expect Goerli's upgrade to happen on, Tuesday the 14th around, what was it? It was 10:10 PM utc, more or less.  Anything else on that? Okay. and yeah, on the next call we can talk about the main update, but, I think people should expect no sooner than like three, four weeks after Goerli. 

**Tim Beiko**
## Cancun Updates SSZ Transactions Breakout Room #2 #727 [20.08](https://youtu.be/GNhrb5txJ4M?t=1208)
* Yeah. do we have Peter on the call? No. Okay. So Peter had like three topics he wanted to bring up, but he is not here, so we'll skip those for now and then, potentially get to them at the end if he, if he shows up or if other people have opinions. on the Cancun side, we had, we had 2nd SSZ breakout yesterday. and Etan, I saw you added some notes. do you wanna maybe give a quick update there? 

**Etan**
* Sure. can you hear me? Yes, That's good. Yeah. So, yesterday we, summarized the two approaches. Again, like  I did a lot of, metrics testing that I measured, like whe whether the SSC Union or the normalized transaction approaches better. And as usual with those things, we came up with even more ideas that also affect the Receipt three so just to summarize once more, for the people new to this, the goal here is to update the representation of transactions and receipts as part of the block, as part of the consensus execution payload as well. 
* And the goal is, that we can prove any individual field of a transactional or receipt. Like you can create a proof that checks, hey, a transaction with this transaction hash was successful in this block without, having to download the entire transaction. So there are three pieces of information that you can request in JSON RPC, that are not part of the serialized transaction. Namely, that is the transaction hash itself, which is computed from, the RLP serialization or the hash history route for an SSE transaction. 
* There is also the from address, like who is sending the transaction, who signed it. and the third piece of information is for transactions that deploy a new contract, there is the address of this new contract. And the question that we have here is, whether we should put those three items into the transactions three or into the receipts. there are arguments both ways, and transaction tree, kinda makes more sense because, those three items, the transaction hash, the from address and the contract deploy address, they are statically computable based on just the transaction. 
* They do not depend on the Ethereum state like the rest of the receipts. And it's also this approach that we did in the execution payload where we put a little field in there, that says block hash, even though the block hash can be computed from all the other fields. so any time that we put something into the consensus object that is computed, but requires algorithms that are unused in consensus, we could continue this tradition and make those three items available as part of the transaction object. 
* The problem is that it consumes more space in consensus objects. that's, 32 bytes for the transaction id. It's 20 bytes for the contract employee address, and it's another 20 bytes for the from address. So it's about 50 bytes, that we are talking per transaction that is about 10 kilobytes per block, that it is bigger if we include those in that, the alternative is to put it into the receipts object, and there are arguments in favor of that as well. because those receipts already contain information about the outcome of a transaction, it's kind of fitting to put stuff like, hey, a contract was deployed at this new address, or a transaction was included into a block with this, additional hash or with this from address, arguments can be made both ways in the JSON RPC currently, the transaction hash and the from address, they are exposed in both Get blocked by number and in Get transaction receipts and the contract address is exposed only as part of the receipt, but that's just JSON RPC. 
* So yeah, just as an additional point. So if someone has, big preference one way or the other, that would be nice to speak up. 

**Tim Beiko**
* Thank you for the overview. Any thoughts? I guess one, one question there was on the agenda and, I think  I also have after, hearing this is like what's the best place to just, read the sort of, basically longer version of what you just went through. Is there, I saw you put like a couple notes on the agenda.
*  Is there a specific EIP Oh, you have actually the Hack.md. Okay. So you, you posted this hack.md and the agenda, is that the main thing people should look at if they wanna wrap their heads around all of this? 

**Etan**
* Yeah, I think the Hack.md is the best entry point. Yeah. I just created that one yesterday, so it's not yet complete. Yeah. but it contains this mention as well. yeah, so I guess right now no one has a clean idea there yet. so the other point that we have is related to SSZ transaction signature schemes. that's EIP 6493. 
* And there we had a question. Right now I sort of mix in the genesis hash, the fork version when a transaction type was introduced and the chain ID into the, into the hash that we are signing. And yesterday in the call we had a question like, do we need all three of these? Or, could we, for example, drop the genesis hashtag if we already have the fork version, and the chain id. 
* So if someone is still familiar with the, the decision process of why the genesis validators route and the fork versions are both used in consensus, maybe that could, put some more light into this. Like  what actually should be put into our signatures on execution. 

**Tim Beiko**
* Okay. Any thoughts, comments? Okay. So I guess if in the next couple weeks, client teams can look into this, we, there's a type transaction channel on Discord, these conversations are happening as well. but obviously figuring out how we wanna approach teams for Cancun with regards to SSZ, is, is pretty important. okay. I guess, as we're kind of moving to Cancun stuff, there is two other EIP wanted to bring you up today, but before we do those, we have sort of this thread on Eth magicians where people can, you know, share what they'd like to see for the upgrades. There's been a couple things there already.
* I think it would be really valuable if in the next couple weeks client teams can sort of chime in there or at least think about like, what are the most important things that they see for Cancun. and you know, beyond just like whether each specific EIP or not, sh you know, should be cfid. Like, what's like, we already have 4844 scheduled for Cancun. You know, are there other sort of significant things we wanna accomplish there? Are there, you know, some EIP that like client teams feel are, are much more, needed or urgent? and I guess similarly, you know, for EIPs champions, this is the spot where like, it would make sense to, advertise that you want an EIP considered for the, for the upgrade.
* There's also a Cancun candidate tag you can use on Eth magicians. so there's, you can sort of see all the different candidates, all in one, all in one page. yeah, so, and I think over the next couple weeks, like as Shanghai wraps up, we can spend more and more time discussing like what the right scope is for Cancun and, what we want to, add alongside 4844. I don't know. Yeah. Before we go into more details there, any thoughts by clients or other people? I sees a couple comments in the chat. okay, so bls, PREPA and, 4788 date is this, I believe the Beacon State route in the el there are two that got mentioned. anything else teams feel strongly about today? 

**Andrew**
* I have a question. so is the cryptography in, 2537 the same as in block transactions? So is it different?  my thinking is whether it was the same then Mike May make sense to bundle them together. 

**Tim Beiko**
* Alex Dunno if you have a mic. 

**Alex(stokes)**
* Yeah, so, well, the other Alex actually looked at this a bit. so the thing with this is that there's kind of been a whole saga of these pre-compiles, and I think the current one, current direction is actually to say, well no pre-compiles, cuz they're actually like kind of involved. 
* There's like at least nine, I think we could bump that number up to like 11. So that's a lot of pre piles. And instead the question's like, what if we can do this without pre piles? And one way we could think about doing that is, basically doing it natively and then the bottleneck there is having modular method. 
* So Jared from the Geth team has been looking at what he calls EVM Mac. I don't know if there's an EIP number yet, but the point being is there's an alternative fork here or like a different design route we could take. And, yeah, this is kind of just the question of like, do we want to ship this now versus take the time to explore this other path, separately. 
* Yeah, the cryptography is the same or at least, you know, the 2537 stuff is like a foundational layer for 4484. I don't know if we wanna like  block them on each other though. 

**Tim Beiko**
* Got it. Thanks. Danny. 

**Danny**
* Yeah, I mean,these other things that can help us not have to write pre-compiles in the future. I kind of, I mean at this point I see BLS as like a native, Ethereum curve, a native Ethereum crypto. And so, we have tools, we have the libraries, we have like extremely robust versions of these.
* And so, exposing those, the EVM makes sense to me, whereas  I totally agree that we shouldn't have to, we should do things to not have to maintain and build, all of these curbs outside of the evm. But this one seems pretty native. 

**Danno**
* Danno, one of the things I'd like to raise, against the idea of random, curves as, a pre-compiled is the gas pricing  is sometimes overfitted to a specific algorithm to try and fix a particular curve. and then sometimes there's like holes and don't map specifically if we use something like EVM Max to charge per instruction and there's optimizations or there's de optimizations that are needed and the gas prices are reflected natively in the contract bringing the code they want, and that reduces, risks related to gas-based consumption, in a block. So I think that's why we should be very skeptical of bringing random curves in as new pre-com compiles. the, and also the EIP for EDMXI think is 5843. I posted that in chat. 

**Tim Beiko**
* Thank you. yeah, these comments about Twitter BBLs is, is random, are not, I don't think that's worth getting into, too much. Okay. So, yeah,  let's spend more time, I guess in the next two weeks just thinking about, you know, what client teams would like to see and others who are listening to this as well. 
* If you want to chime in, this Eth Magician's thread is probably the best spot to do it. and I'll look over all of it before the next call and make sure to like, summarize it and, yeah, so we can come in the call with a bit more of an informed opinion. and then two other things, that, I guess are proposed for this, are EIP 5920, which is the pay op code and EIP 6190, which is a new approach to dealing with self-destruct, Panda PIP was the, champion for both of those. 
* I don't know, are you on the call? no, I don't think so. I don't know if there's a, I think he's a single author on both. oh, no, actually, Victor was the author on the payoff code. Is Victor on the call? No. Okay. and then he was the only author on the self-destruct one, so I don't know if there's anyone who has comments or thoughts on either of those. If not, we can just, review them async. 

**Guillaume**
* Sorry, I was looking for, I was looking to raise my hand. I couldn't find that. No worries. 
* I didn't go through it very thoroughly, but I did look at, at the self destruct one. Yeah. I don't think it should be called, vertical compatible self destruct, cuz I don't think it's really directly related to ver it's more like the, the new self destruct. we wanted to disable self-destruct. yeah, so that's, that's a nitpick, but  I don't think it should be, it should be called, like ver should be in there. one thing I did not understand, so maybe someone did, or at least maybe I misunderstood. it seems that you have, it's basically, when you self-destruct an account, you create a pointer to a potential new account, that will override the, the older account. And what I see is that effectively self-destruct or, creating or self-destructing an account ill mean you'll have to jump from a, from self-destructed account to self-destructed account to self-constructed account. And, that makes self-destruct. I mean the cost of self-destructed is not constant. And, yeah, I'm also, worried about the need  to jump, all over the database. 
* So, what I would like to have discussed was an opportunity to update the pointer, like basically only have one pointer, so that you don't, you don't jump all over the database. So that was, that was my first comment and I had another comment. Oh yeah, I don't think the, at least I did not understand, how create two would be affected.  I think that's missing from the EIP so yeah, if maybe I missed something, I would like to, to know if someone, under understands it differently. 

**Tim Beiko**
* Thanks. anyone have comments or thoughts? 

**Dankard**
* Sorry, I mean, we're talking about with EIP  6190. Yeah. But, so I don't understand why where, where this pointer, thing comes from that you say agree on. I thought that it simply, I don't, I don't see anything of that in the EIP. 

**Guillaume**
* Well when you self destroy, okay, maybe I misunderstood again, but, from what I understand, when you self-destruct something, you replace the code, with one and you set the nuns to some value, right? It's not when you self destruct that you create a pointer. It's when you create, what you call creator again, it sets, okay, let me just, get the EIP cuz I didn't have it, under, like I wasn't looking at it immediately, but it seems to me that at some point you, you set, oh right, it's this first value of storage that gets, that gets a, like the contract zero slot storage slot, putting the EIP is set to the address that would be issued is a contract, use the create code. So that's what I call the pointer. It's the step two in the self-destruct behavior. 

**Danno**
* There's no pointer in that function. It's just a marker to prove it was self-destructed correctly. 

**Guillaume**
* Well I think you have to traverse. So you read the zero, you read Yeah. You read the zero storage slot and then you go to the, that address that's in that place and see if it's also been self-destructed. If it has, and you go to the next one again, Right? 

**Dankard**
* Oh, oh. So like we are trying this EIP tries to recreate the self distract behavior exactly as it was originally. 
* Yeah. Okay. Because I was right. Sorry. Right. I see. So yeah, and I'm,, that, that doesn't seem viable. Yeah, I agree. 

**Guillaume**
* Yeah, I mean it's not, it's got some nice properties, but indeed it's not, this interaction thing doesn't look super great to me. 

**Dankard**
* Well, because I can, I can potentially create an infinite stack of staff construct like that, right? And yep. Yeah. Okay. Any other? 

**Dankard**
* So, I mean the EIP seems, seems incomplete to me actually. Yeah. Like if this is the intended behavior that basically every time you self contract you compute a new contract address, and next time a contract , is created at that old address, you use this new contract address instead. 
* This behavior is not specified in that EIP. So that seems largely incomplete then. but yeah,  I don't think that would be viable, unless we can somehow make contract invocation and everything, vary, like depend on like the gas cost depend on the number of times it's been self distracted. And I guess for self, oh, sorry. Yeah, go ahead. 

**Andrew Ashikhmin**
* Yeah, I think but if, if the code is overwritten to just, zero one, there is no further possibility of, self destruct. it's only like, cause Yeah, it doesn't, it's self destruct his obliterated by the code rewrite. 

**Dankard**
* Sorry, what? Code rewrite. 

**Andrew Ashikhmin**
* So I think, maybe I'm misunderstanding something, but I think, we, in the EIP if the contract code is set to zero one, so once it's, self-destructed, it, it loses the capability of, further self-destruct because there is no So,but a new contract can be deployed at that address that would've the capability again, right? 

**lightclient**
* No, The address, yeah, the account doesn't actually get removed, so it's Not able to, okay, so what okay, the specification is unclear to me then what it's supposed to mean. Yeah. Why are we, why are we writing this new address at the zero storage slot? 

**Guillaume***
* So it's actually explained in a different EIP which is, 6189 I think, where you Yeah, that's what I was describing with pointers, you forward the calls. I think the, the words they use is, so yeah, you create a new contract. So what if you self destruct the new contract? Like if you dis self destruct the contract and then you recreate on top of it, and then you self-destruct this new contract, the self destruct gets forwarded and every time this is, this is written in Geth cost of self destruct, it says every time you get a forward, or they call it an alliance, you pay 5,000 gas extra. 
* So it is not overwritten, it's you create a new contract, that serves, as an alliance. well the, the self, the self-destructed contract is an alliance to this, newly created contract. And the chain can go on forever, well, not forever, but, long enough. 

**Dankard**
* Why exactly are we considering this EIP  like, I'm mean, my last say was still there. The previous EIP  was the one that simply, So The like, I mean this is a very elaborate construction to reconstruct the original self construct behavior and it's kind of annoying. 

**Tim Beiko**
* Yeah, and I think, so last time there was, basically the, I think it was like 4758 or something, the one that just, converted to Sendal. The problem with that is all these create two, you know, contracts. so then there was this other EIP, which just, swapped the nos, but, but still lets you sort of recreate a contract at the same address if  have been swapped to this, max in number. but then the issue with that is you can get like mutable contracts where like you, the contract storage is not cleared, so you could redeploy a contract, at the same address using the old storage, which is unsafe. and I think this is sort of where we got in stuck. 

**Dankard**
* And okay, but I haven't seen the discussion where, where like there was anyone who was actually affected by this, where Oh yeah, there is, yeah,

**Tim Beiko**
* There's, So why are we,

**Dankard**
* Why are we not considering that that version of the EIP  which was less complex than it Does so, 

**Tim Beiko**
* So Jared, I believe, like, looked at affected contracts, like there are several contracts which would break, and like non-trivial contracts if we just, you know, convert the sendal, and this is where No,

**Dankard**
* I understand that part. Yeah. I'm talking about the next step, not about the Stand. 

**Tim Beiko**
* Oh, yeah, yeah. So no one, yeah, I guess the short answer is no one has done it. So I think the two next steps Okay. 

**Dankard**
* That, that you probably Like, so like we should, first we should consider that other version of the ap and only default to this crazy construction if we find that that Yeah. Breaks something major. Yeah. 

**Tim Beiko**
* Right. And I guess then the two, the two paths to explore, okay. One is like, 4758 with a tweak. Another is kind of a weird tweak, but like, you know, you allow self-destructing and recreating in the same transaction or something. And I think that would, that would solve most of the affected contracts, but it did add a lot of complexity. 
* And I think, there was another proposal, which is you, allow recreating, new contracts if they've been self-destructed with this like nons change, but you move the storage to a new, like, to a new location. So you're sort of, we're not deleting the old storage from, the tribe, but you're making it inaccessible. And the downside there is obviously you, it's basically state growth, but yeah, there's, 

**Dankard**
* Well, the downside is significant complexity to support an absolutely marginal thing that has no real use case. 

**Tim Beiko**
* The downside of, of what, sorry,

**Dankard**
* Of this latest sort of EIP P is like 6190 and stuff. Oh, yeah, Yeah. But yeah,  I mean it's an insane, it's an insane amount of complexity. That's what we really wanted to avoid. Yeah. 

**Tim Beiko**
* Yeah. And I think it would be good for somebody to just look in the different alt, like how do you not break this create two redeploy flow with the least amount of complexity? I agree that would be like a very valuable thing to do. 

**Dankard**
* Well, I mean, it's not possible with anything less than this. Like if we want to recreate the full behavior, then, I mean this is, this has been possible click clear and possible from the beginning, but I really want to avoid it 

**Tim Beiko**
* At the risk of basically breaking some contracts. Correct.

**Dankard**
* Oh yeah. 

**Tim Beiko**
* Okay. Yeah. Yeah, so I'm, yeah, I feel like having better data, at least on like the different like approaches and being able to actually assess the complexity would be good. and obviously like ideally breaking zero contracts would would be ideal. yeah.

**Dankard**
* By the way, what is the state of, deprecating self desconstruct that we made that Decision? 

**Tim Beiko**
* Yeah, so we, yeah, so we, it's deprecated as a Shanghai basically, so we've told people it's deprecated. yeah, or I guess we'll tell, you know, it hasn't happened on main net yet, but like it's part of the, the Shanghai spec. anything else on self-destruct? Okay. and I guess there was no other comments on the pay opcode. 
* Okay. then Peter, you had three things you wanted to chat about. removing, pending blocks slash pending transaction, 866, and then removing support for non merge networks. Do you wanna give some quick background on those? 

## Client Updates/Discussion [48.41](https://youtu.be/GNhrb5txJ4M?t=2921)
**Peter Szilagyi**
* Sure. So let's stay the easiest one. so 4844, we speced out Eth 68, and I think most clients are already on it, or if they are not, I'm hoping everybody's on Eth 67 at least. And then the question is, can we simply drop the Eth 66? Is anybody opposed to that? 
* Essentially, if any client is over, so unless there's a client that's still on Eth66, it should be fine to drop it.I'm just asking because it's just good 5G to delete all stuff that are not needed anymore. 

**Tim Beiko**
* Does anyone, yeah. Does anyone oppose dropping Eth66 Out of curiosity? 

**Peter Szilagyi**
* Does anyone oppose dropping E67? Might as well drop both. 

**Marek Moraczynski**
* So, we have if Eth68 implemented, but not released on purpose, e i P was in draft, and in case of new breaking changes in EIP  it could break communication between peers, but we, if we all agree today that there will be no changes to this EIP, we can add it in next release, knowing that the hard fork is coming in, it means that all net Nethermind node after hardfork will support, if Eth68, of course, previous version don't support, as I said, on purpose because EIP was in draft. 

**Peter Szilagyi**
* Yeah. So it's, this is just the weirdness of the EIP process. I think everybody was kind of on board with Eth 68 the way it was stacked and since, I mean, even if one client released the thats, or you already cannot really change it anymore without breaking that client. 
* And I think currently almost all the clients haven't implemented and the parent is that, so it, no there's no possibility to change it. Don't make a change if it's just roll out is Eth69 on this point? 

**Marek Moraczynski**
* Yeah. So we'll add it to the next release. 

**Peter Szilagyi**
* Okay. Then I guess what we can do is remove Eth66 now and Eth67, I guess after the work, because then the body should be up to date. Cool. 

**Tim Beiko**
* Yeah. Fabio? 

**Fabio Di Fabio**
* Yes. we in be, were thinking about that and let's say we are also fine, we keep supporting all the, version of the protocol for private network, but we can announce only the new version on main net. But we were also, evaluating that since at the moment only Geth support Snap Sync, removing this will also, remove the support for Fast Sync. And what if we wait, 

**Peter Szilagyi**
* That was already removed, wasn't it? 

**Fabio Di Fabio**
* Yeah, What if wait, for at least another client to implement a Snap Sync server before doing that? This was our suggestions. 

**Tim Beiko**
* Lukasz. 

**Lukasz Rozmej**
* So I think like we cannot deprecate it Eth 66, but that doesn't mean we have to remove it. I think Jeff wants to remove it because, going forward with their, state layout in terms of, Nethermind, we are working on implementing our own state layout changes and supporting snapshots and Snap Sync. 
* But, yeah, I hope this will come somewhere this year. But, yeah,that's it. So I think we can like stay Eth66 is deprecated while still some, clients can support it if needed. So we also need it, on other chains where there aren't Geth nodes to sync, so we won't like remove it entirely right now. 

**Tim Beiko**
* Got it. Andrew,

**Andrew**
* Well, Eric one formally supports Eth66, but not, actually it doesn't because it doesn't sort Geth no data. So like dropping it for Argon would be, actually clearer. We, we don't have this capability and like no intention of supporting Geth node data. 

**Tim Beiko**
* So I guess does it make sense to deprecate it on main net as of, Shanghai basically? and then if client teams can also ship Eth68, as, as part of, the Shanghai release, that'd be good because then we know sort of all the mainet peers support Eth68. 

**Peter Szilagyi**
* Yeah, actually, I think that the catch that I was missing is, Eth 66 for the last one. Wait, none of Eth 68, did we drop new  data out of E 67? Maybe not. What, yeah. Okay. Okay. That is a bit more complicated because, because of the Geth no data, which means that all clients need to be able to sync via SNAP sync, at least the client side of it should be implemented. Yeah. So, long story short, forget if we want to, when we want to switch to the new, data model, we will need to stop supporting this either way. So it, it would be nice to, nice to have other, other clients also catch up with the synchronization part.
* Plus it would be super nice if other clients could actually start serving it because it's, yeah, currently on Sepolia synchronizing  is a bit hard because, there are relatively few gap nodes, but only Geth nodes can serve, snapshot data.  it's a bit annoying. Anyway, I guess long story short, we should not drop it Eth67, sorry, Eth66 just immediately right now. But, yeah, we will be forced to drop it when we switch the, the try, I guess what we can, 

**Lukasz Rozmej**
* So Nethermind can sync, SNAP sync and I think Basu probably also,but I'm not, not sure.So we can sync through E67, but like it, Eth66 is still relevant for us until we change our, database model, right? So that's what I want to say. 

**Peter Szilagyi**
* Mm-hmm. Yeah. Fair enough. Okay. I guess I'm, for me, the verdict on this question will be that, Geth will retain 67, just so that we have it, and then the moment  we roll out the new data model, then we will in implicitly also stop serving You mean Eth66, right?yeah, sorry, Eth66. 

**Tim Beiko**
* Yeah. Okay. Yeah. Yeah. Okay. 

**Peter Szilagyi**
* I guess at that point, most people will run 68 anyway, so 67 is kind of like, it's boring thing. The interesting thing is the 66, because that's the last generation that supports, Geth market. Okay. then, for me the answer is that we will retain it for now and then when we switch over, probably possibly what we can do is, if somebody's running, so our, we will support both data models initially simply because we cannot upgrade our database, from one model to the other. 
* And then, anybody who's running the old data model will continue serving these 66, and anybody who resync essentially running the new data model, stop serving 16, I guess that will be a,good middle ground and then eventually your colleagues remove it out completely afterwards. Okay. So that one, one question down. 

## Pending block/transaction support [57.54](https://youtu.be/GNhrb5txJ4M?t=3474)

**Tim Beiko**
* Yes. the next ones were, pending block pending transactions and then syncing non merged networks. 

**Peter Szilagyi**
* Yes. lemme just open up my facts. Yeah. So, the pending block is, yeah, that's one of those  in the ongoing things that people that we wanted to boxings forever because it's not really useful, although it's not really harmful either. It's just one of those things that, that get, we get annoying bug reports that, hey, if I'm wanting to subscribe the pending block, then okay, the block number should be, or the block hash will be what? Or, or essentially I'm getting number of pending blocks and is it for the same height? Is it for different height? 
* It, it gets a bit weird. And, and my, suggestion is whether I think it would be clean if we would stop serving the APIs for depending block because, depending block essentially contains a random selection of 200 transactions out of 4,000 that the nodes has. It doesn't include the.Maybe transactions either. So the state that you can retrieve from the pending block will be kind of random, so it's not really the next state, the transactions included, and it will be kind of random. So what's the point? 

**Tim Beiko**
* Yeah.Andrew, 

**Andrew**
* It's, I was thinking that, we can perhaps repurpose spending block for something else because now we have this, with after the merge, we have to wait for, fork choice updated until we, mark a specific block as like as, the, the head of the chain. So we, we before, CL deems it to be the head of the chain. 
* We, have, we are aware of, of some new payloads, but they're not officially yet can canonized. So, but if somebody wants to be able to access , new blocks that we are aware of, we can, I was thinking that we can use spending block for that or maybe some come up with something new, but, it's, I think it's a valid use case for it would be bad to lose access to such available data, but not sanctified by EL, by CL yet. 

**Peter Szilagyi**
* So the problem there is that in theory you can have, sibling heads. So I can give you five new payloads that are all siblings and then which one would you return? Or I could give you even multiple one on top of the other. So it's a bit, 

**Andrew**
* Yeah, true.But,  I guess, in most cases it will be just one block. 

**Peter Szilagyi**
* Yeah.But We, 

**Andrew**
* We can, come up with I heuristic. so it's not, it might be not necessarily, predetermined. It might vary by client to client. but I think it's a useful piece of functionality for people who are  who want access to the latest data. And they, they might not care if about some weird theoretical scenarios because, or you might use heuristics, okay, give me the biggest block, or the most likely somehow by some heuristic to become the, the head of the chain. 

**Peter Szilagyi**
* Yeah. But that kind of changed things a bit again, because  that's, in that case, you can actually, for example, retrieve transactions which belong to a specific block or, those blocks have a proper block from a block hash difficult. So it's a depending block has a lot of these, guest work fields, whereas, if it's included in the chain already, even if it's not set as the head yet, then kind of behaves like the old blocks already. So it's, I don't, it's for me, the, the weird thing is that we have these, for example, you can filter for pending transactions, but then, okay, you have a stream of transactions, but do they belong to the same pending block, different pending blocks? 
* I don't know. It's, can only be interpreted and somehow added necessary context. It just seems like a mental effort that's not really useful. So is there any legitimate use case for depending on like ever anything? We can definitely keep it. It's just,  I'm not sure there's a point in keeping it. 

**Andrew**
* Well, I guess for some MEV or some, some other scenarios when you want to be super fast, and you don't want to lose any latency, then you need access to like, to the most probable pending block and start building on top on top of that. 

**Peter Szilagyi**
* Yeah, but that's my point. That is not the most probable one. So currently with, with all the flash funding and everything, it's the, the next block will be, so if the next signer is actually running, any kind of MEV capable minor, then the next block that the network we'll see will be completely different than, what will be produced actually.So 

**Tim Beiko**
* Is it, I guess is this something that Geth alone can try removing and see what happens? Basically?  

**Peter Szilagyi**
* Nothing.It's, so the pending block is and all the attending APIs are specified and part of the execution layer spec. So it's, it's not only something that we can just your or remove and both nothing collapsed. 

**Tim Beiko**
* So maybe one, one way to like actually see if it's useful is to just make a PR to the, execution API specs, removing it and then, you know, share that with like MEV people or other, I guess developers or users and see, you know, did they like object strongly on the PR? yeah, I don't know if anyone else has thoughts about this, but it seems like we struggle to to see if it's actually useful for end users and if we, if we claim to remove it, then at least people will show up and complain if, if they're actually affected by it. 

**Tim Beiko**
* So I, for me, it seems that depending block is kind of similar to an archive note where it's something that people kind of have there but they don't really use it. And any kind of power user will just need some extra infrastructure on top anyway because whatever's out of the box is, is not sufficient.

**Peter Szilagyi**
* My guess would be that if you're running some MEV stuff, then you would try to collect all the transactions independent of depending, like you don't care about the next 200 transaction that your client thinks are interesting, you care about the next 4,000 and then try to mix and match and dig stuff out of them. 
* So again, you have a spending block, which is somewhat seems a useful functionality, but I think it's too limited to be actually useful for the power user case that it was meant to suffice. Same with archival. Archival are super nice except when you actually want fast access, then you need to index on top because while you're not going to read through the state try anyway, if you're running some production system, it's, anyway, it's, we don't necessarily have to write any conclusion here rather it's more like, it open-ended question that long term, the spending block I think has been playing us for a while and I don't know, we are just in this mode of trying to delete stuff that are not needed. 

**Tim Beiko**
* Yeah. And I guess what do you think would be the best place to collect feedback from users on this? This is sort of why I was suggesting making a PR to execution APIs. Cuz right now mo I suspect right now what happens, like if we removed it, people wouldn't be aware and then they might complain after. so trying to like preempt that, is there a way we can like suggest it and, and if there is strong, strong demand, then yeah And 

**Peter Szilagyi**
* We can always announce that we decided to remove it and then see how big of a fall back there is or full. 

**Tim Beiko**
* Yeah. And that's why I was suggesting basically opening your PR on the execution APIs repo. I think that's like, we don't have to merge the PR, but like you can open it, we can, you know, share that as a thing where people can go and comment on it if they're not happy about it. 

**Peter Szilagyi**
* Okay. Yeah, I'll try.

**Tim Beiko**
* Cool.Yeah, and you had pending transaction as well, which I assume is like the same but Pending block, pending everything. 

**Peter Szilagyi**
* Okay.Yeah. Yeah. But it's the same point. Yeah. Got it. 

**Peter Szilagyi**
* So, with, okay, with pending transaction there's a bit of, a nuance there because, I think for Geth specifically when you retrieve the pending transactions, we don't give you the, the transactions from the pending block, but the transactions from the transaction pool because everybody was kind of interested in that and not the pending block, which kind of already highlighted that the pending block itself is kind of useless and people want something else. 
* So I'm completely fine to retain the functionality to retrieve the pile of transactions from the pool. That, that seems like a useful thing. I just don't see assembling that into a part of that, into a block and then returning that subset. So pending transaction, I would perhaps, if there's , an API between a pending transaction, I would just name rename it to retrieve the pools transaction or whatever, call it something meaningful. 

**Tim Beiko**
* Okay. Okay. 

**Peter Szilagyi**
* I mean it I'm assuming you mean the, that pending string, literal identifier that kind of Yeah, that's the point. Get rid of that I know implication. Cool. Okay. And my last open end question again, it's more like a discussion starter, thinking starter is that, again, one cleaning some stuff up in Geth. currently all the clients and getting included, everybody has kind of two ways to synchronize the network execution lines.
*  I mean they can synchronize in this forward syncing mode kind of like, the proof of work with authority and they can synchronize in this backward billing mode where we have a Beacon client, which tells us the help and then we go backwards, retrieving every everything. And, there are some subtle and not so subtle differences and there are various optimizations and, so you can optimize a lot of stuff if you know that you only need to do one of these options or one of these methodologies. 
* But if you need need to maintain both, it gets a bit wonky and it's, always harder to optimize if you are suddenly can, your stuff can be called in completely different ways. And plus we have all that old, the almost four synchronization code, which is actually not, tested nowadays or not since all the networks and maybe Ring is the last standing network. But once we replicate that will, our networks will be post merge and beacon chain driven. 
* So actually won't have any production network that can either, that can use the old forward SIMP code. So my hunt would be that eventually that in a couple years will just be brought out of the clients and it'll just not work and nobody will have the capacity to make it work because there will be no public network to make it work on.
*  And this is a question again, long-term question that is there an appetite towards five to remove this functionality, but by removing a forward syncing functionality, we would essentially say that we will never be able to synchronize a non merged network ever plus, and it does not that we launch, we'll need to be merged at Genesis already because you won't be able to to mind the first few blocks of transitioning across non status merge pattern. So there are some implications and the question is, what, what do people think about this? 

**Tim Beiko**
* Thanks, Lukasz? 

**Lukasz Rozmej**
* So I think the, centralization methods supported right is fairly internal thing implementation detail. So each client can diverge here easily and we, I think differ a bit , in the synchronization methods, right? The, the API of, of Ethprotocol just supports multiple, approaches. 
* And for example, Nethermind will be supporting, centralizing non merge networks as we have few that we support. And I don't think they will be merging any anytime soon. So, yeah, that's from the Nethermind side, but, we generally, have the approach that we try to go backwards on them. So we kind of have some trusted block hash that we, that we include in the, for example, in the release and we try to use the backwards sync on them, while, while we only have this forward sync doing a small part, which, generally it is less optimized, but it's like not big deal because of that.

**Tim Beiko**
* Thanks. Any other thoughts? 

**Peter Szilagyi**
* So the just one like note that, yeah, it is true that, I mean we can always leave this to every client to decide for themselves whether they want to support this or they don't want to support with the is that, if we ever want to launch desktop networks that are not Genesis merged, then any client which drops this functionality will be unable to participate at least in that phase where the thing gets merged, which might be an interesting limitation. 

**Tim Beiko**
* Any other thoughts, comments? Okay, that, yeah, I mean we can continue the conversation on this and obviously like there'll probably be some divergence between, what we do on mainnet and you know, what we have to do, or what client teams have to do to support, other networks outside of main net. yeah. 

**Andrew**
* Yeah,  I'd like to say that I think, it sounds like a good idea because, in Argon at least the, the forward sync is, fairly complicated and I would like to drop it at some point. 

**Peter Szilagyi**
* Well, forward sync is one thing. supporting block propagation, block announcements, block patching from the other side is for example, another mechanism that is only useful for non merged networks. So if we assume that a client will not support a non merged network going forward, then all this block retrieval logic can be completely deleted. 
* Again, these are not necessarily big complicated things, especially since they are kind of working now my kind of my, it's just a maintenance thing that the code is there and when you want to refactor some API or something, then you always have to tiptoe around existing code that nobody's using. 
* So it might blow up in your face anyway when somebody tries to use it later. Obviously it might be different f for some clients which wants to support, non Ethereum networks. That's one thing. And the other thing is I'm not sure how layer twos, what layer twos do, so it might be interesting to get some feedback on some layer twos because I know some layer twos are Geth derivatives. So if I would be curious if, how they work internally, if they depend on this or not.

**Marius**
* Can we, can we start by, creating a new protocol to drop the, the messages? 

**Peter Szilagyi**
* So, we definitely can. I guess it'll be kind of similar in similarly with problematic, like if Eth66 where if some client wants to keep supporting this, then they will need to support some, I don't, for example, E 66, which is fine as long as we are just dropping stuff, but what happens when we need to add something and they want to add it to their non version network and then we would have a for in the Eth protocol, But what messages Do you want? 

**Marek**
* What messages do you want to drop? Exactly which one? 

**Marius**
* new block. 

**Marek**
* Okay. 

**Peter Szilagyi**
* I think, so currently the block pro block propagation, block announcement, messages are forbid on post merge networks, but they are still part Protocol. 

**Marek**
* I see,. Yeah. 

**Peter Szilagyi**
* Okay. And then they're always the option to remove it from the protocol, but if we remove it, then it's going to be a problem, for clients who still want to be able to support it. 

**Lukasz Rozmej**
* Ah, so you mean okay, if we remove it then okay. Okay, got it. but we could probably, like if we removed in like Eth69 right, or something, then we could still like support it in the 669, just, have it disabled that we have, have it there, like with some some kind of way. It's not a, it's not a big deal in my opinion. 
* But yeah, the question it's not a, like a question for it's limiting things, so we shouldn't like maybe take it to like be blocked by it, but yeah, if someone especially uses, especially Geth as a fork and for example,  twos et cetera, they wouldn't be able to, they would have to like be very careful when merging stuff, right? Yes. back if this user is there. So I don't know from this perspective, but it shouldn't be a blocker to go forward in general. 

**Peter Szilagyi**
* Yeah. But only for clients who are willing to drop people the non merge that can support. Because if you don't want to drop the non merge that will support the new implicitly needs to keep this, these messages through the block provocation and last messages, that means that we cannot just remove from the protocol unless you willing to create a new satellite for project for block vacation and Yes. 

**Lukasz Rozmej**
* It's around. Right. 

**Peter Szilagyi**
* Sorry. Okay. I didn't hear that, but, anyway, I don't really want to part this whole discussion. I think, my three, issues that  I opened, I wanted to bring it up here is just, it's kind of like a small part of the general direction of, trying to somehow slim clients down so that we, we stop filing new complexity on and somehow try to remove, stop that either were past experiments or past lessons or past implementation details. And it's always a bit annoying to remove stuff because there's always somebody relying on it. and I definitely think we should somehow figure out how to proceed for those people. 
* I don't really want to just leave people hanging in the air, but we, I think need to accept it that we cannot file complexity on top forever. We need to somehow start turning down. 

**Tim Beiko**
* Yeah, I think, I think that makes sense. I think, you know, slowly starting to bring things up here and like suggesting PRS and like making people feel like it's gonna happen or it might happen  is valuable because, it takes a long time for the community to realize that, a deprecation  is happening. Anything else anyone wanted to discuss today? 

**Peter Szilagyi**
* I mean, Matt really loves this, so we need to,

**Tim Beiko**
* Yeah, we need to fill the last eight minutes, for Matt. Is he still leaving on the call? Did he drop off the call? Okay. No, he's still here. the pressure oh, I, yeah, I like the idea Jerry considered for deprecation CFD. and I think that is something though, like we've announced self-destruct being deprecated in this upgrade. 
* Like I think at the very least when we make these network upgrades, we can flag stuff as deprecated. even if there's no actual code changes, that's a good way to, you know, start letting people know. yeah. But yeah. Okay. If there's nothing else, then yeah, I guess that's it for today. 
* I'll put up the PRS for the Goerli, fork Epoc, and we can, yeah, we can announce that, next week when client teams have, have releases out. But yeah, thanks everyone, and talk to you soon. Thank you. Bye-bye. Thank you. Bye. 


### Attendees
* Tim Beiko
* Danny Ryan
* Pooja Ranjan
* Mikhail Kalinin
* Marius
* Wesley
* Barnabas
* Saulius
* Danno
* Lightclient
* Pari
* Ethan
* Mario
* Tomasz
* Oleg 
* Kasey
* Marek
* Crypdough
* Fabio Di
* Terence
* Andrew
* Roman
* Marcin 
* Pop
* Guilaume
* Protolambda
* Carlbeek
* Mike
* Gajinder
* Stefan
* Hsiao-Wei
* Josh
* Phil Ngo
* Alexey
* Holger Drewes
* Dankrad
* Guillaume
* Proto
* Holder Drewes
* Stokes
* Peter Szilagyi
* Sean
* Micah Zoltu
* Jiri Peinlich
* Marius Van Der Wijden
* Potuz
* Evan Van Ness
* Moody
* Tynes
* Alex Beregszaszi
* Marek Moraczyński
* Justin Florentine
* Ben Edgington
* Lion Dapplion
* Mrabino1
* Barnabas Busa
* Łukasz Rozmej
* Péter Szilágyi
* Danno Ferrin
* Andrew Ashikhmin
* Hdrewes
* Crypdough.eth
* Ameziane Hamlat
* Liam Horne
* Georgios Konstantopoulos
* Mehdi Aouadi
* Bob Summerwill
* Jesse Pollak
* Stefan Bratanov
* Sara Reynolds
* Caspar Schwarz-Schilling
* Ahmad Bitar
* Marcin Sobczak
* Kasey Kirkham
* Sean Anderson
* Saulius Grigaitis
* Ruben
* George Kadianakis
* Dankrad Feist
* Andrei Maiboroda
* Gcolvin
* Ansgar Dietrichs
* Jared Wasinger
* Diego López León
* Daniel Celeda
* Trent
* Mario Vega
* Kamil Chodoła
* Ziogaschr
* Kevaundray
* Antonio Sanso
* Oleg Jakushkin
* Leo
* Nishant Das
* Pote
* Sam
* Tomasz K. Stanczak
* Matt Nelson
* Gary Schulte
* Rory Arredondo

-------------------------------------

## Next Meeting
Mar 16, 2023, 14:00-15:30 UTC

