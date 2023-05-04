# Execution Layer Meeting #60
### Meeting Date/Time: Apr 27, 2023, 14:00-15:30 UTC
### Meeting Duration: 1hour 30 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/759)
### [Video of the meeting](https://youtu.be/ajLQVC3E_mk)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 160.1 | **EIP 6780:** Changes the functionality of the SELFDESTRUCT opcode so that the operation sends all ETH in an account to the caller, except when the opcode is called in the same transaction a contract was created.
| 160.2 | **EIP 6475:** A new Simple Serialize (SSZ) type to represent optional values. This makes the implementation of EIP 4844 more future-compatible with a larger forthcoming SSZ update to the EL of Ethereum.
| 160.3 | **EIP 1153:** Adds new opcodes for manipulating state that behaves identically to storage opcodes but is discarded after every transaction.
| 160.4 | **EIP 6913:** Introduction of the SETCODE instruction which would allow contracts to replace their code without clearing their internal state.
| 160.5 | **EIP 6493:** Defines a signature scheme for SSZ encoded transactions. This would also help make Ethereum more future-compatible with a larger forthcoming SSZ update.
| 160.6 | **EIP 4788:** Expose beacon chain block roots in EL block headers to allow proofs of CL state in the Ethereum Virtual Machine (EVM). This would improve trust assumptions of staking pool, restaking constructions, smart contract bridges, MEV protocols, and more.
| 160.7 | **EIP 2537:** Adds the BLS12-381 curve as a precompile to efficiently perform operations such as BLS signature and SNARK verifications. These operations are useful for various applications including account abstraction, Layer-2 rollups, and CL light client development.
| 160.8 | **EIP 5656:** Introduction of a new EVM instruction for copying memory areas to provide efficient means of building data structures and deploying computationally heavy operations on Ethereum.
| 160.9 | **Big EOF:** A bundle of EIPs that would have made sweeping improvements to the EVM, one of the major ones being separation of code from data.
| 160.10 | **EVMMAX:** A subset of EIPs related to EOF implementation that creates new storage logic for modular arithmetic parameters and memory space to move the values in these parameters to and from the EVM.
| 160.11 | **SELFDESTRUCT Deprecation:** Developers agreed to reassess the candidacy of EIP 6780 once the results of the audit are ready in about a month’s time and consider whether to bundle EIP 6780 with EIP 6913. Regardless of the outcome, developers like Dankrad Feist  and Andrew Ashikhmin affirmed that efforts to prepare EIP 6780 for inclusion in Cancun would be orthogonal and independent to efforts preparing EIP 4844, meaning that EIP 6780 would not delay or negatively impact EIP 4844 progress.


## Intro
**Tim Beiko**
* Hello everyone. Welcome to ACDE #160. I just posted the agenda in the chat. I guess the biggest thing we should do today is, discuss, potential EIPs for Cancun and, yeah, in the context of 4844 being kind of the main thing  we're working on. and then on the 4844 forefront, I think there's two conversations, that, that we wanted to continue. One is just, the reorgs, the reorg handle handling for, blob transactions. 
* And, second, I know that we have been working on the last 4844 devnet this week, so we can kind of share an update on that and how that's going. Yeah, and I guess maybe to kick it off, so on the Cancun side,  so far we only had, 4844, which was, which was, included. 
* We had a bunch of other stuff, which was previously CFI, a bunch of other, even more other stuff that was proposed and, and, and still not quite cfi. I compiled a list in Eth magicians. but maybe to kick it off, I'd be curious to hear from just the different client teams, like what do you all feel is the most important things, to do in Cancun? 
* Yeah, and we can take it from there. I know, I think Nethermind was maybe the only one that answered Async before, so maybe it makes sense to start with Nethermind and then others, can jump in. 

**Lukasz**
* So, I think it's more or less what we, what we answered on Eth magician call tread, so definitely, 4844. definitely we see, need for, 6780. what else? 1153. We would like to proceed with that because that was already postponed from Shanghai and this is kind of ready. So, I don't see like much effort  to push it out. 
* I don't see a point for it to be a delayed. then in the more maybe, state, 2537, 4788 and 5920 while, like bigger things like, EOF, more things around SSZ that are not, if they are not necessary and think like EVM max I would consider for, some of the next hard forks. 

**Tim Beiko**
* Got it. Thank you. 

**Matt**
* Tim, this is Matt. I think from the Besu side, that actually mirrors us pretty much entirely. We have very similar thoughts on the list, maybe with the exception of 4788, but other than that it's pretty much the same, same list as provided by 

**Tim Beiko**
* And what do you think about 4788? Do you think it's more or less important than what other Mine said? 

**Matt**
* It's similar like in terms of, you know, we think it's very useful, but the, the scope wise, you know, maybe kind of in the same bucket as maybe rather like weekly support. 

**Tim Beiko**
* Okay. anyone from Geth, Aragon? 

**Andrew Ashikhmin**
* Yeah, so, for Aragon, it's important to get 6780, the self-destruct removal and, I think it's unrealistic to deliver EOF, alongside, 4844. So I would postpone EOF to Prague. and yes, now, otherwise I think we can do maybe a couple more smaller EIPs. 

**Tim Beiko**
* Okay. And  do you have any preferences or just not really beyond, self-destructed 4844? 

**Andrew Ashikhmin**
* No preferences. I can ask, the team members, more, but I don't think we have strong preferences yet. 

**Tim Beiko**
* Got it. thank you. And guests? 

**Peter**
* Yeah, so, as for us, I mean we haven't really thought about, specifically what EIP to ship or not ship. personally for me, priorities getting 4844 out. So anything large is, in my opinion, unrealistic beside it. Think about EOF, smaller ones. I mean, self-destruct for sure, and any other smaller stuff. 
* I don't necessarily see an issue with that, but, I kind of feel that 4844 should be the thing that everybody focuses on and the rest is kind of like good to have. Nice to have. 

**Tim Beiko**
* Got it. Thank you. so it seems just, yeah, from those four, clearly the self-destruct one is like the second most important or like the second most, you know, mentioned EIP beyond, 4844. and also, so with 6780, we've hired an, auditing firm to like analyze the impact of it on the chain. So in the next few weeks we should also have some data on like which contracts, might be affected and whatnot. but I think that's probably one where it makes sense to, you know, formally included.
* I see Danny and, Lightclient, you both have your hands up. yeah, if this is about self-destruct, please go ahead, but otherwise I think this is maybe one we can wrap up before we kind of dive into the rest. Okay. So I guess, does anyone like oppose including, 6780, so this self-destruct and this version is the one where you allow self-destruct only if it's in the same transaction as like a create call and otherwise you effectively use like the sendal, semantics where you just return the funds but don't destroy the contract. 

**Danny**
* Is this conditional upon the analysis not finding anything that we don't yet know about? And and if we, if it did, we would at least open up the conversation? 

**Tim Beiko**
* Yeah, I guess it's worth highlighting there was another proposal for self-destruct that was slightly different. So I think, Acik put that one together, which was, you, you do like a sort of fake self-destruct where you actually hide the storage and data, but you don't, you, you don't delete it from the, state. yeah. 
* And, and so yeah, that would be another path forward. It seems like people don't prefer it as much right now, but, yeah, I guess I'm curious, yeah, from client teams, does anyone have an opinion on like, Danny's question? Like if we find what, what would be the thing that we, we would find that we like, you know, potentially make this a show stopper? 

**Danny**
* I don't, I see, I don't know, William, I mean, it's, it's hard for me to say, I just, I just kind of make a commitment to like revisit the report on this call. Yeah, just that seems like the point of doing the report, you know, one is to give information to the community and one is to get the others to give information to us. So I just wanna, like, if we move forward with it right now to make a commitment to looking at the report together. 

**Tim Beiko**
* Yeah, I think we definitely would at least. and I guess the question is do people wanna make this commitment prior to the report being out or, I think it's gonna take probably like, I think it was like three, four weeks. So like, you know, say like a month from now is when we would probably know, do people prefer to wait a month from now before making that, making that decision? 

**Lightclient**
* I think it makes sense to make the decision now if everybody is okay with it, and then revisit it after the report happens. 

**Tim Beiko**
* Does anyone disagree with that? I know Dankard, William, you both have your heads up, so if this is related to self distruct, please. 

**Dankrad**
* I mean,  I just wanna say like, it's very hard to believe that the report will find nothing. Like, I think like we are very likely going to find some contract somewhere that somehow will be broken. the question is like, do we make a judgment call on like, yeah, killing that contract because we believe either it's like so low and value there, it doesn't matter, or that, that the owner can like do something else and rescue their funds and, and all that. Like, basically, yeah, like, I mean, it's, it's just like, it, it's, it's very likely that we'll find something.
* I will say, yeah, I mean if we, if we do start building something now and we see a chance that like,  even the discussions might not even go towards like, we can't do it, but it might just be delayed because like we need to talk to a lot of people, then like we should probably design it in such a way that, we can shift  without that implementation. I think like it should be largely 4844. But yeah, that would be my comment. 

**Tim Beiko**
* Got it. Thanks. Lightclient or William, did you wanna add anything to that? 

**William**
* Yes, so we're neutering self-destruct because of the unbounded scope of removing all account storage. The problem gets worse in our vertical trees because vertical trees are flat, but vertical trees don't actually prevent code changes. so if self-destruct is modified, I wish to retain the ability of accounts to retain, to change their code, and also improve the way it's done. I've interacted with three different upgrade patterns in my career. I wrote some of the earliest contracts to upgrade with delegate call, and I've written an account ownership system to facilitate self-destruct upgrades. 
* My proposal is set code, to preserve that ability if we have to remove it from self-destruct. so that is, if we're not doing, Axes proposal, that would just change the nuts to the account and use that as a marker. so set code, improves on the self-destruct upgrade pattern, by, change, allowing a way to create clear storage, or not clear storage when we change the accounts. so, it's, we don't want to be able to, clear storage because that's unbounded. So it just simply makes a way to change code, in a safe way. it's as safe as all the other current upgrade patterns, and it should be a simple change to add on to, to any self-destruct removal. 

**Tim Beiko**
* So this set code, just to make sure I understand, you can change the code at the account, but not the storage. Correct. And this means you can like have a contract who's like semantic, you know, changes it semantics, but, keeps the previous storage right? 

**William**
* Yes, that's correct. And, this is superior to the current self-destructive upgrade pattern because the self-destructive upgrade pattern requires two separate transactions because the self-destruct doesn't happen until the very end of the transaction, whereas set code can happen immediately, this can allow, this is more secure than self-destruct upgrade because there's no downtime where the contract is empty. so you could use it, for example, for a token upgrade. thank you. 

**Tim Beiko**
* Got it. Thanks. Andrew, I saw you both cut your hands up. Was it related to this? 

**Dankrad**
* Yeah, I don't understand why, why we need this. Can  all this be implemented using proxies? Why do we need another methods? I don't understand that. 

**William**
* I can answer that. the main improvements upon being able to replace code in place is that, there's no execution overhead. delegate call is still useful because you can use it to bypass the account code size limit. So if you need a contract, or an account with, a hundred thousand bytes by code of implementation, you can just spread it across multiple contracts with delegate call. but if you need to, replace an account's code itself, then this keeps that functionality, the benefit of having no execution overhead is critical. 
* And without it, many, users might prefer in order to save on the gas, to migrate all of their tokens, for example, to make a new account and transfer all their token ownership, and identity, to new, accounts. That's not great. For example, if you're, a dex and you want to change your code, and you don't want the gas overhead of needing to, call into another contract, 

**Dankrad**
* Yeah, I understand the, the overhead argument, but I mean, functionally, I dunno, like we should think more about the overhead if that can be mitigated, but there, there are, like, there, there are, there are many possible future advantages from having been variants that currently doesn't exist, but could exist in the future with this self destruct, deactivation that in the same, at the same address, you'll always have the same code for no code. So I like you, we should weigh that against, the benefit of, And 

**Tim Beiko**
* I feel like, having, I think axe six, not current self the truck proposal, but the one prior to this effectively had the same semantics if, if I remember incorrectly. And we, so basically what it would do is it would allow you to recreate the contract, at that address, but, it wouldn't change the storage in the meantime. and the challenge with that, so people, were concerned about like their kind of attack risk where, you know, you deploy a smart contract and then, you know, people use it in a way and you sort of change it and you can keep the existing storage and, you know, potentially, change the entire functionality of, of the contract. so I dunno, * I'm, yeah, I'm curious, if, yeah, how others feel about that. cuz it, it sort of feels like a discussion  we had a few months ago, unless I'm mis misremembering the issue. 

**Andrew Ashikhmin**
* I think, from, from everyone's perspective, we'd like to avoid the version of self destruct removal where we have, multiple versions because we already have, those scenario, we call them incarnations and, they complicate the code, quite a lot. So unless we absolutely have to, I would prefer a simpler solution, like in my mind, 6780 is, is a good compromise between simplicity and, like limited backwards compatibility. 
* So maybe we can wait until the report arrives and, like then we can reconsider, but we can tentatively agree that we we're including some variant of self destruct removal, like 6780, and if in the meantime other people come with, like a different tip, then we can revisit this. It's kind of it's, mostly independent from, to 4844, so we can revisit it pretty much independently. 

**Tim Beiko**
* Okay. And I guess this matches sort of what light client was saying, but basically we would sort of include, 6780, as we get the report, we can analyze the impact, see if there's a significant change that's worth making to the spec or not. but, you know, make, basically make that commitment today and, you know, potentially change the actual, semantics of the EIP  if we see something. 
* But, high level from like a, you know, design point of view, it seems like all the client teams are on board with, with making this change. Does that make sense? 

**Andrew Ashikhmin**
* Yes, to me, Yeah. 

**Tim Beiko**
* Any, okay. Any, I guess last chance, yes. 

**William**
* So code mutability, doesn't impact the, or immutability doesn't impact the user space much because code, can still basically be modified via proxy. but, what are the advantages of it, as on the Aragon side? So you said that it complicated your implementation. how is that, when the state, route and all, should still function? 

**Andrew Ashikhmin**
* Well, it just, we have this extra per parameter incarnations, so besides, account, address, we always carry this incarnation and we have to, for instance, kind of, have to make sure that, in case of a reorg that we should arrive at, like all different, different nodes should arrive at the same incarnation or like account code version because, otherwise if it becomes part of the state, then you might have divergent state and so on. 
* So it's all, it's all doable and feasible. It just, it's just an extra complication. And the, the question is, whether the this extra complexity worth it, but I think if, if, if there is another, like are you saying I might have missed the point is are you saying that there is already an alternative if that, solves, that, that is, is is a better alternative or like we are you or you, are you talking about a new I that you have in mind? 

**William**
* So account code can already change on reorg because of create and create two. So when those are reorged, the account code also changes. 

**Andrew Ashikhmin**
* Yeah, but with, with, self destruct removed, we won't have that. 

**William**
* I'm referencing specifically set code as a way to maintain ca code mutability. 

**Andrew Ashikhmin**
* And, is it part, like, is it an EOF already or is it a new in your feature? Any idea? 

**William**
* It's EIP 6913. 

**Tim Beiko**
* So I guess, clearly like I don't think most people on the client teams are super familiar with this. maybe what I would suggest for this is that we move forward with 6780, in like a month when we have the report. 
* Obviously we're gonna have to reassess that. I think that also gives time to people to read 6913 and we could, you know, make that decision sort of at the same time like, you know, whether we want to change 6780, based on the report whether we want to add 6913 alongside it. but it feels like all the teams are like pretty strongly in favor of, you know, moving forward with self-destruct removal. and we probably don't have enough information to go like beyond that, yeah, today, so I guess, yeah, does anyone oppose it that like making including 6780? 
* We revisit the report, or  revisited, sorry, in a month with the report. in the meantime we can also, look at 6913 and kind of go from there. okay. And Marius has a basically comments that says the i'll to do the same thing. so cool, let's do that. 
* I'll update the spec, after this call, but 6780 is included. and just for the people implemented, be mindful that, you know, potentially there'll be changes to this spec based on the findings of the analysis and you know, people's like readings of stuff like 6913 in the next few weeks. Yeah, thanks William for sharing your perspective as well. 
* Light client and Charles, you both have your hand up and you had them for a while. Oh, and now Danny as well. 


**Lighclient**
* Yeah, I guess, yeah, like, sorry, I just wanted to, Yeah, I just wanted to say something before we got into the discussion about self-destruct on like the general, CFI EIP for Cancun. And I would like to look like very seriously at these SSZ EIP, because I don't want to get into a situation where we do whatever the like, like absolute fastest thing is for 4844 with the intention of changing it and just like a fork or a two fork later. So I do think it's important to try and figure out like what is the minimal amount of, work that can be done so that it's kind of like future compatible with this as a SSZ world since that's what we've been talking about doing for a couple years now. versus like just shipping something in RPL  or hackmd

**Tim Beiko**
* Yeah. I think it probably makes sense to chat about now chat about that now actually, because if we have basically 4844 it's already pretty big. self destruct is sort of some medium sized EIP, and if we do need to make some SSZ changes, it's probably good to be on the same page about what those are before we decide about doing anything else. 
* Yeah, I see, I don't know, you and Etan both have your hands up. Do either of you want to, you know, share your thoughts on, on that and you know, what's the either minimal or optimal set of changes we should do as part of Cancun? especially given 4844 is the maintain of the upgrade. 

**Andrew Ashikhmin**
* So the two EIP that should definitely be looked into are 6493 and 6475. the first of them, 6 4 93, that one, defines how signatures should be computed so that they cannot, conflict with other chains, that may use RLP for the same transaction type. And the other 6475, it's quite a small one. 
* It justify defines how we want to represent optional values because 4844 has an optional to like for the destination of the transaction. right now they don't exist anywhere and we should just decide should they be like the unions are today or should they be more compact or something else. 
* The rest, how those trees inside the blocker structured with trials, receipts and transactions that we can also do later doesn't really matter for 4844 compatible. like the, the 6493 is compatible with both the normalized transaction approach and the SSZ union approach. So that one, like those three, they, they are not necessary for Cancun. We can do them later without downside. 

**Tim Beiko**
* Got it. Thank you. Andrew, I see you have your head up. 

**Andrew Ashikhmin**
 * Yeah, so, a question about  66475 SSZ is the optional. So, if I understand, if we adopt, if we implemented in Cancun that affects 4844, right? Because 4844 has some optionals, the two address is optional, right? In the SSZ transactions? 

**Etan (Nimbus)**
* Yes, exactly. I mean right now they are, defined as to use the union type there, but semantically what they should be are optionals. It could be that they are serialized the same that we wanted, but it could also be that there is like a minor change. So at the very least we need to align and switch over to the new representation at the same time for a definite, so that we stay compatible, 

**Andrew Ashikhmin**
 *And does anyone have a view on whether we will need union and it says zero going forward? Cause if we don't, then I guess it makes sense to just have this more limited, solution for, for optional. 

**Etan (Nimbus)**
* Right now we don't use them. There are some designs that may use them in the future, but regardless of that, the optional is a more restricted type because it can only be none or some, right. But the union is a more complex type. So for example, in the Nimbus implementation, those two are very different code paths. but sure it could also be that we just, encode the optional as a special case of the union. 
* So it's just a syntactic Sure. To make it clear to the reader what is meant. right now, 6475 is not compatible with the union because it doesn't emit the selector it uses, the length instead if it's emptied, it's a none otherwise it's a sum. but union also for the serialization, I think it's a bit underspecified because it doesn't define how to serialize the non-value. so yeah, unions are not used today, but  if we need them, we need to also decide how we want them to look. 

**Dankrad**
* Of course, sorry, I think it is specified. I think it's just selected equal zero estimate and value. 

**Andrew Ashikhmin**
* Okay. As so, 0 and 10, nothing else I guess after, Yes. 

**Dankrad**
* Yeah. so just one idea would be, like if we really like, if we just keep our options open here, we just like we, we can simply implement if nobody is using union at the moment, then we can implement the, optional as you specified it, with the intention that if we do introduce, unions later, that we make them a super set of the optional. 

**Andrew Ashikhmin**
* Okay. So the difference then would be, I guess the 6475 would need an update then just to allow for a future extension for multiple cases, but non-value for example, that one could be reduced to just the empty, like the zero there doesn't provide any value, but the sum would've a leading one, right? That would be the minimum. 

**Dankrad**
* Potentially yes. I mean theoretical you could even what not necessarily, right? You could also say if there is are only the two options, like none or something, then you also don't need to get need to add the one, right? 

**Andrew Ashikhmin**
* That's true. Yeah. If it's a none and another option, 

**Dankrad**
* I guess you have to guarantee that. Yeah. Then you need, well I guess you need to  do a special case that, the second part is non-zero length. I dunno if that's always guaranteed, maybe that's always guaranteed. Yeah. Something to think through, but it might, it might be possible to make, make the union a strict super set of what you specified already. 

**Andrew Ashikhmin**
* Yeah. Another issue is when you update the spec to, like when there is a fork that adds another case to the union and you go from two to three that you can no longer parse the old values with like, Yeah, that is a good point actually. 

**Dankrad**
* Yes, that might be an advantage of adding the one because then it means, that you can more easily upgrade existing SSZ fields with additional  options, right? 

**Andrew Ashikhmin**
* Yes, exactly. So I will, update 6475 then to have the one in the some case, and the none case I keep empty and then also change the existing to use this time. 

**Tim Beiko**
* And so if we, if we make those updates to 6475, are we like fully happy with this, with the state of it? Like should we considered, should we included, you know, pending those modifications? 

**Andrew Ashikhmin**
* I think so. 

**Tim Beiko**
* Okay. So does anyone disagree with that? 

**Andrew Ashikhmin**
* And also I think, we will need to update,4844 to use, the,  for 6475, right? For, for the optional, to address. 

**Tim Beiko**
* Yes, I'm sure there's at least half, if not all of the 4844 authors on this call. So if one of them can make that PR, once we have the 6475, once we have the 6475 changes done, that would be great. okay, so that's for 6475 and then, there's 6493. So the signature scheme, is this, I guess this is something we also have to include. 
* Sorry, I'm trying to read the comments. Yeah, so I guess, okay, so yeah, so anyone opposed to 6493, so the signature scheme for SSZ transactions, 

**Lightclient**
* Does this create the two concepts of transaction ID versus transaction hash, or is this only have to do with signatures? 

**Andrew Ashikhmin**
* It also includes the concept for transaction id. 

**Lightclient**
* Yeah, it's been a while since I've looked into this, but I remember being pretty against referring to transaction transactions by this transaction ID concept and it being different than the transaction hash. 

**Andrew Ashikhmin**
* I mean, it's the same, like it's just not a catch. but instead a hash root, right? 

**Roberto B**
* One disadvantages that involves now bringing in the demoralization aspects of ssy into the execution layer, whereas right now we don't have that minor thing, but Right. 

**Lightclient**
* But I think we need that Eventually. 

**Tim Beiko**1
* Yeah. 

**Tim Beiko**
* Well I guess maybe this is like a dumb question, but if the 4844 transaction type is an SSZ transaction, I guess its signature scheme is defined as part of 4844 or. 

**Roberto B**
* Right now it's just to of the realization with the prefix type. 

**Tim Beiko**
* Got it. Sorry, I can't hear you were saying something. I sort of cut you off. 

**Lightclient**
* No, I'm, I'm just thinking. 

**Tim Beiko**
* Okay. So I think sorry, I think I sort of misunderstood here. I thought this was also sort of a requirement to 4844, but it sort of seems like it isn't. 

**Lightclient**
* So we can move forward with, I mean We have implementations of 4844 right now, but I think doing things the right way is, is best and we don't really have the concept of hashing an SSZ serialized value. I think that's kind of weird. And so that's why we're talking about having the hash tree roots, but once we start having the hash tree root, we start having to have these other questions about, okay, how do we, you know, have the signature scheme safe? 

**Andrew Ashikhmin**
* And also for, the 6404, if we go with the SSZ based transaction, try later, then that one would've tier eight one that those hashes and IDs, match if we do it the right way from the Geth go. if it's the normalized approach, it doesn't matter to be honest, because the hash is a, is a separate leaf anyway in the tree. So yeah, there's that slight advantage as well. 

**Tim Beiko**
* So I guess, maybe a good next step here is we have the 4844 call on Monday. is it possible to, by Monday, like by that call, have the changes done in 6475 and 4844 so that people can like look at that, prior to Monday and kind of discuss 6493 in the context of 4844 and basically, you know, aligning those two on that call Monday. 
* Okay, I see Monday's a holiday, whoever Etan is. is there anyone else who you think can join and like make the case for, the EIP? 

**Andrew Ashikhmin**
* I mean it's mostly for review, right? yeah. 6493, right? 

**Tim Beiko**
* Yeah, Yeah, yeah. 

**Andrew Ashikhmin**
* Like, I do, do we have to do the review during the call or could we just, 

**Tim Beiko**
* So I guess, yeah. Yeah, and we, we definitely shouldn't make a decision about including it or not in the 4484 call, but I think it's, yeah, if people wanna review it and we can have a, you know, first conversation about it in the Monday call, at least, yeah, if people have questions or, you know, thoughts during the review, we can address some of them there, but it doesn't feel like people have enough context to make a decision about this today. Okay. 
* So let's do that. So let's, so we include 6475, and Ethan, if you can do the changes before Monday, that would be amazing. We also need to do the changes on EIP 4844 to kind of reflect that and we can bring it up on the call on Monday if people wanna discuss it more and two weeks from now we can we can hopefully make a final decision on this call.
* Okay. any other thoughts, concerns about SSZ? Okay, Daniel, you had your hand up for like every long time. is it just accidentally up? 

**Danny**
* Oh, sorry, me. Yep. Yep. I just wanted in the opening when we were kind of getting signal from client teams, I just wanted to say that 4478, which is cross layer, has the support from the consensus layer teams, you know, see it as a moderately high priority to open up trustless pool designs and the barrier to entry to make pools in the execution layer. 
* And that people are willing to get it in. Obviously it's cross layer so it takes two to tango. I just wanted to make sure that information was surfaced here. 

**Tim Beiko**
* Got it. Thanks. yeah, I think it might make sense to actually cover this one and, the BLS pre-compile next, cuz we've talked about them quite a lot, over the past, I mean years in the case of BLS, and at least months in the case of 4788. yeah, I guess I'd be curious to hear from like the EL client teams, it seemed like most teams had appetite for like, you know, maybe if one or two smaller EIP beyond, 4844 self-destructed now, some of these SSZ changes, but would you know, I guess 4788, BLS or, I know 1153 is another one that came up a lot, like, yeah, how do people think about prioritizing between those, potentially smaller EIPs and is there something I guess that people feel is like a must have or, you know, quite important to have? 


**Speaker 0**
* Yeah,  I'd stop short of saying that we think 1153 is a must have, but we're basically remains pretty strong in favor of it. 

**Tim Beiko**
* Okay. And does that mean you would prioritize it over like 4788 if It's already done? 

**Matt Nelson**
* So it's mostly testing overhead. Got It. Least press the force. The same is not true. 

**Tim Beiko**
* Got it. and then Marek has a comment, also say, I guess 1153 would land slightly higher for them. and lightclient has a comment I guess from the Geth side saying 4788 , slightly above them. I don't know if anyone from Aragon has like strong opinions. 

**Andrew Ashikhmin**
* Yeah, I think, we would do, 5920. It's, a simple, usability improvement. yeah. 

**Tim Beiko**
* Okay. So I guess this is the spot where like we have yeah, 4788, 2537, and 1153 are sort of the three I'd say that are like medium that like some client teams feel at least somewhat strongly about. I don't know that we have to make a decision about those today, 
* But, I'm curious if like, are people potentially comfortable with saying like that's, all the scope, like we'll consider for Cancun and maybe what we could do is like literally remove everything else from CFI that's not those, three, so 1153, 2537, 4788 as we start, as we start kind of working on, the DevNet and like implementing the rest of the EIPs, we can kind of revisit those three, but yeah, and I see, yeah, so I, and yeah, I guess let's just start there. 
* Like would people be fined for now like restricting this CFI to those three and that means basically removing all the EOF stuff, which I think was the only other stuff that was cfi. Okay. And then, yeah, so there's a couple comments in the chat about like some other tiny op codes, like maybe we can add those in the future as well, but at least I think we can remove, remove the E O F stuff, yeah, keep those three. so 11 53, 25, 37 we're already cfid. We can 47 88. 
* And then potentially if there's small things or you know, other additions that come up, we can decide those. and I know I guess Charles, you've had your hand up for a while to talk about one of those small things, so if you want to go ahead, we can do that then give context to people. 

**Charles C*
* Sure. this is actually my first ACD call, so I don't know what the yeah, protocol is, but, so I don't wanna derail everything, but, well first off, I think that 1153 and 5920 are quite useful, if you are already talking about this. 
* So I wanted to bring up, mcopy EIP 5656, which, is quite useful, from a compiler perspective. It would, you know, enable us to reduce spike code quite a lot and it, it also just makes sense to have it, you know, there's call data copy, there's code copy, there's even X code copy, but there's no mem copy and I don't think there's any contention about the spec or it's like usefulness. there's a even open up portal request on Geth the to implemented. 
* So, and it seemed quite straightforward, so I just don't see that there would be any problem with it and yeah, it would be super useful. 

**Tim Beiko**
* Okay. thank you. So I guess we can, yeah, we can have that in the list and we can potential or we, you know, have people look at it and potentially cfi it, in another call when folks have had time to review it.  And generally we try to not like CFI something on the first time it's been presented just so people can have some time to, to kind of digest it before.
*  But, and I saw you posted in the Eth magician thread so people can can review it there. Andrew, Daniel, I see you both have your hand up Andrew first. 

**Andrew Ashikhmin**
* Alright, so, I just think, that because we've been defying 1153 for quite a while and we moved it from Shanghai to Cancun and so on, and it seems to be a small EIP that people are mostly in favor of. I think it would be fair to include it because otherwise we just, yeah, we've been, it is been a lot of, it is been a lot of opportunity for people to look at it and we, yeah, we generally agree that it makes sense, so why not? And small enough I guess. 

**Tim Beiko**
* Yeah. Does anyone have objections to that? It's true. It's been discussed for a long time. I know there were some people were sort of opposed from like a design perspective, but, it seems like most client teams are in favor now. 
* Yeah. Does anyone have an objection or, okay, so I guess, so we, okay, so that means we include 1123 in Shanghai alongside 4844 and  the self-destruct and as small SSD changes, and the, the potential trade off there is like the two other ones that people mentioned earlier so the 4788, those would be sort of cfid but not included for now. Does that make sense to people? Okay. so we can move 1153 as well, to included, Daniel, I see you have your hand up. 

**Danno Ferrin**
* Yeah, so, I am in support of moving EOF out of Cancun. one of the things that's gonna give us time is more time to get some, some core deep questions, right? we're still working on questions around whether or not Geth observability should be in and about, you know, how create should be handling and a couple of other issues and pulling it out of Cancun solves a lot of the time pressure. 
* So we can, we can focus on getting it right instead of getting it ready for, a Q3 shipment. So as much as it hurts, I think it's the right decision. 

**Tim Beiko**
* Okay. Ansgar?

**Ansgar**
* Yeah, I would general mirror the sentiment. I would just wanna say, because I think it's always helpful to set at least like some very rough expectations for the long term roadmap. I personally would prefer if we could at least end afterwards aim to have PR be like an EOF focused, fork and hopefully come relatively soon, after Cancun, instead of then basically shooting for combining it. 
* I know with and have be like, I don't know, nine, nine months after or something. 
* That seems like, because if we keep, keep trying to combine it with another big ticket item, I think it just will keep slipping because it's too big to to basically be the, the second place in a fork. So I think at some point we just have to then say, okay, it'll get it on it's own fault and because most of the limitations will be ready at that point, it will just be a quick fork. 

**Tim Beiko**
* Yeah. So, I think it does make sense that, you know, think about this way, I don't want us to commit strongly to something today when we're not even like, we don't even have implementations for Cancun. but yeah, it does seem that, yeah it does seem that like EOF and vertical trees are like the two potential next big things EOF is potentially, smaller and far along and it would almost be sort of like we did with the merge and withdrawals where you have the big fork with 4844 and then the small fork, with EOF. so yeah, we can definitely discuss that.
* I think as, as like we have a clear picture for Cancun, that's probably the highest level decision to make, so that we can get teams to work on it in parallel. and Lucas? Yeah, to be clear, I'm not saying EOFs small. I'm saying though that if you had, you know, the merge and withdrawals, the merge was such bigger than withdrawals, even though withdrawals were not trivial and it feels like we're in a similar spot with like 4 84 an EOF  where 4844 is like much bigger. and obviously sort of can't quite be combined practically with, with EOF but yeah, eof is also big and you know, can maybe be a smaller, it's a smaller big thing for an next fork basically. Yeah. Greg, oh Greg, you're on mute. 

**Greg**
* I'd like to reiterate just that we commit to getting EOF in at some point. The basic functionality is the same as EIP  615, which I proposed in 2016. So we've been discussing this for seven years. Is it's just time. Well I Think I've got, Yeah, I think it's, I've got work I've been wanting, I've got work I've been wanting to do on the EVM for seven years that I can't do until this is in. 

**Tim Beiko**
* Yeah, I mean I think look, all the client teams are pretty on board with EOF be too big to be included alongside Cancun. I think the strongest like commitment we can make is to have it be the main thing for the next fork. but even that is probably not something we can like a hundred percent agree to today. and there's some comments in the chat to that effect. yeah, Okay, so I think we covered pretty much all the like proposed eip maybe to just recap, sort of where we landed. So 4844 is obviously part of, included for, for Cancun. 6780. This is a self-destruct removal. EIP. We also agreed to include this, review it in a month or so when we have the impact analysis out. And in the meantime we can also look at the set code EIP, which was 6913, and then we agreed to include 6475, which is the SSZ optional type.
* There's still some changes that need to be made to that. Etan will do 'em in the next couple days and we'll re we will update for it 4844  to reflect those changes as well. Lastly, we agreed to include 1153 alongside that. so this would be kind of the current scope for Cancun. two things we've, well 2735, the BLS was already cfid, it stays out Liz 4788. 
* We also cfi and then we remove all the EOF EIP from cfid and that's basically, oh, yeah, we should CFI the signature scheme as well. 6493. but we didn't agree to it, quite yet. Does that make sense to people? Okay.
* Cool. And yeah, so on on Monday's call, we can on Monday's call we can chat about the 6493 EIP as well a bit more. And then two weeks from now we can, we can bring it back up here.

## EIP-4844 blob re-orgs & newPayload(context) [50.50](https://youtu.be/ajLQVC3E_mk?t=3477)
* Yeah, So, okay, so there were two more things on the agenda. first was, also related to 4844, the conversation around like the blob reorgs and the new payloads spec. I know at Peter and Danny, we sort of discussed this on the CL call last week. I don't know if there's any updates from either of you or Yeah, Yeah, I don't, I don't have an update. 

**Danny**
* I know Peter wanted to spend a bit more time thinking about it and I know maybe everyone else who hadn't thought about it that much. I wanted to spend some time thinking about it. so it's something we can obviously talk about now, we can talk about before, before a call. it's a breaking change to the engine API if we go down that route. So we need to figure it out sooner, rather later. 

**Tim Beiko**
* Peter, any thoughts from your end? you're off mute but we can't hear you. At least I can't, So, Oh no we can't. 

**Peter**
* So essentially what I was saying is that, I was working on 4844, but not this specific part, so I don't really have any update. 

**Tim Beiko**
* Okay. So we'll see. We can keep chatting about this on the discord as well as it comes up, but it's just something we should be aware of. yeah, that basically, yeah, we need to agree on a design for this. 


## 4844 devnet-5 updates [59.19](https://youtu.be/ajLQVC3E_mk?t=3559)
**Tim Beiko**
* And then, last thing we had on the agenda, so DevNet five, there's been a lot of work on this this week. I don't know if anyone wants to give a quick update to kind of share where things are at. 

**Barnabas Busa**
* Sure, I can do that. so basically DevNet five, we had a driver on, starting last Friday and then we had the actual launch yesterday. The main utc. We are running this, with the 1000 validators. we have three working cl clients, lighthouse and Prism, and we have four-ish, EL clients. Another mine JS and a fork of everyone and, and a fork of geth. 
* Currently we have working block scout for called the tooling is, coming online now and we don't have a block scan bl BL scanner, working just yet, but hopefully it should come online by the end of the week. Nice. We currently don't do any fuzzing, but I'm open for it. And, probably the timeline for this is, I don't know, a week or two, maybe more, but I would like to see more clients getting onboarded. Do you also have the dead net force still running for this? and we would like to shut that off hopefully end of the week if there's no opposition for that. 

**Tim Beiko**
* Does it seem to be so we can, yeah. Go ahead and shut it down. yeah, thanks for sharing the update. Anyone else have thoughts? Questions? 

**Barnabas Busa**
* I also linked in the chat the specs that you would need to do if you want to participate. 

**Tim Beiko**
* Nice, thank you. Okay. so yeah, I guess that's it. anything else people wanted to chat about today? Okay, well if not then I guess, yeah for the next call, figuring out this SSZ stuff and yeah, if there's any other, I guess small EIP that people want to discuss, this is probably like the beginning of the end for them to be considered. 
* Yeah, so please add them on the Eth magician thread, so we can, yeah, so we can keep track of them. But yeah, thanks everyone. We'll talk to you all soon. 

* Thank you. Thank you. Thank you. 

-------------------------------------
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
May 11, 2023, 14:00-15:30 UTC


