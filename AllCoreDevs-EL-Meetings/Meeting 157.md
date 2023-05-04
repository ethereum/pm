# Execution Layer Meeting #157
### Meeting Date/Time: Mar 16, 2023, 14:00-15:30 UTC
### Meeting Duration: 1hour 30 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/737)
### [Video of the meeting](https://youtu.be/ViLwzeIuJUc)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 157.1 | **Shanghai Updates** Shanghai Scheduled for April 12 |
| 157.2 | **Cancun EIPs** After Shanghai, developers will activate EIP 4844, proto-danksharding, which is a code change designed to significantly reduce the cost of Layer-2 rollups and thereby, increase the scalability of Ethereum |
| 157.3 | **SELFDESTRUCT removal** Similar to SSZ formatting, the removal of the SELFDESTRUCT opcode is a topic that developers have discussed several times on prior calls. In fact, developers initially considered including the removal of SELFDESTRUCT as a code change for the Shanghai upgrade. Developers ultimately decided on simply including EIP 6049 in Shanghai, which does not change anything about the Ethereum protocol but acts as a warning message to smart contract developers about the forthcoming behavior change of the opcode in the future. 
| 157.4 | **EVMMAX** Presented by Geth (EL) developer Jared Wasinger, EVMMAX represents code changes that would introduce more flexibility to the arithmetic operations and signatures schemes that could be used on Ethereum. Initially, Wasinger presented these changes as part of EOF implementation.
| 157.5 | **Precompile for BLS Curve Operations** Also called EIP 2537, this code change like EVMMAX represents the addition of new cryptographic signature schemes to Ethereum. This EIP in specific creates a new precompile to efficiently perform BLS signature verification and SNARK verifications.
| 157.6 | **Transient Storage** Also called EIP 1153, this code change was originally proposed for inclusion in the Shanghai upgrade. It introduces two new opcodes for reducing smart contract gas costs. Notably, the code change has already been implemented across nearly all EL clients and a dedicated test suite has been created for the EIP.
| 157.7 | **Unlimited SWAP and DUP Instructions** Can only be implemented alongside or after EOF implementation.
| 157.8 | **PAY Opcode** This code change introduces a new smart contract operation that allows users to send ETH to an address without calling any of the functions of that address. The main rationale for creating this opcode would be reduce the attack vectors and costs of ETH transfers.

## Intro
**Tim Beiko**
* Okay. good morning everyone. All Core Dev 157. today we have a bunch of things on the agenda. the first ones are around Shanghai. Goerli Upgrade Recap. and we can recap that, figure out if we wanna set a mainnet update, today. then, Terrence and Putuz had a PR around, local block building. so it makes sense to go over that after that.
* I've tried to basically list out all the stuff that's been proposed for Cancun so far to kind of give people a picture. we discussed SSZ last time and wanted to come back to it. and then there's kind of all these other things that have been discussed. So, might be worth, if not, like, touching on every one of them, at least the biggest ones. And, and, at least putting it out there so people know sort of what's being proposed. And, we can start having those conversations. and then we'll try to keep a couple minutes at the end. Pooja, I know have put out a report around, EL client diversity and just, yeah, basically what node operators feel they like and dislike about the various clients. 
* So, yeah, I guess to kick off, so we had the Goerli Fork this week. does anyone want to give a quick recap of how things went? and if, yes. Nice. thank you. Any, anyone else have any thoughts they wanna share about Goerli or, yeah, anything they noticed beyond that? Okay. so if not, it seems like it went relatively well. so I think we can probably set a date for maintenance. I had proposed three in the agenda, so, basically April 6th, 12th, and 19th. 
* There's a couple comments in the chat around April 12th. yeah. Does anyone, I guess, you know, does anyone think we should not do April 12th? Otherwise we can, we can go for that. I, I picked out an slot, an EPOCH number. I'll copy paste them in the chat. that I am 90% sure. 99% sure. End up on a historical roots boundary. I'll double check it right now, but, yeah. oh, and there's a comment in the chat from, so does Basu have any issues if we, okay. Okay. So people like the 12, there's a comment in the chat about like, it's in the evening for the EU, and, that's unfortunate. 
* But if we wanted to cleanly map to like a historical roots boundary, it needs to divide by 12 by 8192. Sorry. so this is why it's kind of a weird time and you get like one of those every day and a half or something. yeah. Oh damn. oh, okay. Oh, okay. Sorry. I know, yeah, I know what's wrong. Sorry. thanks.

**Tim Beiko**
* In short, Goerli went well, saw a drop in participation because of unupdated clients, but, even regardless of that, BLS changes and withdrawals went well. and the network, reached finality and then everything was fine. And we were we were just discussing, the fork date for main net. And it seems like people like April 12th. so the comments, the chat reflect as well. and we were about to start talking about like, whether or not the time can be a bit better, but it seems unlikely because we need an, historical roots boundary, which happens every like 27 hours. sorry, YouTube. but yeah, April 12th, is what's being discussed right now. 
* So I guess, yeah, this current epoch is late for Europe. how big of a deal breaker is that we can always go like 27 hours later. which would be the next, it would be later, yes. Which would be like the 14th or something. 

**Danny**
* Oh no, but that would be later in Europe, right? 

**Tim Beiko**
* Well, oh yeah, actually, yeah, it'll be worse. It'll be like, you know, plus three hours or something. 

**Danny**
* So yeah, There you go. You go day four. But also it's kind of nice that we have this forcing function that slowly rotates and would be different next time, so that, yeah, we get a nice distribution across time zone. 

**Tim Beiko**
* Okay. We'll get Nethermind, some energy drinks and, yeah, any objection. So this would be, epoch, 6209536 on, mainnet. Okay. So Cool. We have a date for Shapella. we'll give teams like a weaker, you know, so to put out releases, I think it would be nice, like ideally if I'm the next, on next week's, call, we could like have the team releases out, so we can announce them there. But then at the very latest, I think if like early the week after that, we can, put out the announcement. That'd be great. 
* So that'll give people like a proper two weeks to upgrade. yeah. So from today, I guess, you know, we have,  four weeks, to the fork. Anything else on Shapella? Okay. if not next up, Terrance you had, PR you wanted to discuss. I'll post it in the chat, but if either of you want to go the floor is yours. 

## Allow EL to suggest local execution execution-apis#388 [12:28](https://youtu.be/ViLwzeIuJUc?t=748)
**Terence**
* Yeah, sure. I can get started, but just feel free to, add if I miss anything. So basically one property that will be really nice for, this between the CL and the EL interaction is that the EL basically determines how CL propose pet those blocks based on some sort of, censorship resistant, metrics or, monitoring. Basically you can look at mango and look at just transactions to see whether based on certain things  to determine if the transaction is monitor, to determine the transaction is being censored.
* And the one nice thing about this is that, it's not required in a way that if the EL doesn't implement it, EL changes return us no. And then if the CL doesn't want to use this, CL doesn't have to be use it.
* So right now it's, right now it is like phrase as completely optional, but yeah. But anyway, the PR is out there, it is open for feedback and yeah. And then we also have a prism implementation PR as well. It, I mean, on the CL side, it's relatively simple to implement, I guess the majority of what will be on the EL side. But like I said, this is, this, this currently phrased as an optional thing. 

**Danny**
* I'm pretty supportive of this. Like it's a very small change that can then be very much iterated on, by ELs and CLS as they see fit. and really does open up the design landscape to try to ensure that we have censorship resistant and other potentially nice properties of how the min pool is being utilized. 

**Tim Beiko**
* Potuz

**Potuz**
* I have talked, I have talked with some, EL debts and some CL debts and got some feedback, that I wanted to mention here. Everyone on the EL side told me that it would be absolutely trivial to hard code forks in that return, which means that they could just immediately implement this. And on the CL side, there's no change that is actually needed. 
* So, I think it's, from everyone that I've heard, I've heard that it was absolutely trivial to implement this. And I've got some other, some feedback from the CL polls saying that, they'll be allowed to either use it or not use it. And, and actually there's some diversity as to how to use this, which also makes me happy because, having diversity on when we're gonna fall back to local education or not is something that is quite interesting in itself. 

**Tim Beiko**
* Thanks. Lukasz, did you have your hand up about This? 

**Lukasz Rozmej**
* Yes,so, yeah, but this is just the first step, right? And in order to, for it to make any sense to, to be using the future, we need to also think about the holistics we would potentially use, just even like discuss them because we can add them and not never use it, right? Or, use it in some useful way. 

**Potuz**
* Can I, can I at list the ones that I, that I had in mind? I mean, you can add as many as you wish and you can have them configurable or not. I just focused on like the disturbing a fault because, if we manage to implement this right now, then we will avoid bumping a version on the engine api. That's, if it's absolutely trivial, then I would be in favor of implementing this right now. 
* But, as for the heuristics, the one that I listed in the sites, I think are, are sort of like the more  dramatics for the kind of implementations that I have in mind. One of them is if you have seen a transaction that is constantly being reorged, whenever this transaction appears in the block, then that block is reorged, then that's a very strong indication that there's censoring going on. there are other heuristics that you can apply. If you have seen a transaction that is paying twice the current priority to fee and that transaction is not  has not been included in three blocks, they still violate this payment twice as much as any other transaction, then you should include it and then you should fall back to local execution. 
* If you have seen  something that worried me, and the reason why I'm opening this PR is that, the flash bots community, so is going towards, having the relayer not check the, the execution payload. this is something called optimistic relayer. 
* And this screws up, some statistical analysis that I wanted to do on censorship. And the reason this screws up is that we may see some, some blocks that are invalid that obtain, that contain transactions, that that could contain transactions that were sensors. So that's another heuristic. If you see one transaction that whenever, it appears in blocks, that block is invalid, you should also fall back to local execution. But I'm sure smart people will come up with, with better whether heuristics, or combinations of them. 

**Tim Beiko**
* Thanks, Marek. 

**Marek**
* And then, Quick question right now, do you mean before Shanghai or, what do you mean by right now? 

**Potuz**
* That's, that would be optimal if it's absolutely trivial as everyone has told me we could do this in less than one day and have it in the next release and test it even indefinite immediately. if it's not possible, then I don't mind any, any delay because, I think this is very simple. So you can, it can be shipped later. 
* But the thing is that this would require, more complexity because we will require, like bumping the engine API and then coordinating what I mean either using on the CL side, an endpoint to check that, the endpoint is supported on your EL or other sort of complexity, com. I mean, combinations, if it's absolutely trivial, then I think it's easier to just, for us, it's absolutely trivial because we don't need to do anything. And then for the EL if for the EL it's just sending a false, it's trivial, then I would suggest to do it now. 

**Lukasz Rozmej**
* So, one last thing for me that, so in general, I think I'm far, but that, that I don't like, that it's creates another like complexity on the EL and another responsibility on our side to implement, maintain, and, have this heuristics. 
* And this is potentially something that could be done even outside of EL, right? It doesn't have to be inside of EL and integrated in the API.That's the question that doesn't make sense to have it in the, 

**Potuz**
* I can reply as to why I think it's the EL is the right place. and the reason is, the reason, I want to do this is when I realized that you can on chain, with very mild assumptions, assume like with probability of like one in a, in a million that there's been no censorship, if you know that two consecutive blocks haven't been missed. 
* And this can be verified on chain with an, with the assumption that, the validators will fall back to local execution when they see censorship by forking. And the only, the only way that I can see how to do this is if the CL has access to the repo. 

**Lukasz Rozmej**
* But, one, one more question, but this is basically optional functionality on both CL and EL layer, right? So EL can also always return false calls and CL can always ignore even if it's returned true. 

**Potuz**
* That's correct. But just the fact that, that this is a possibility allows the theoretical assumption that certain percentage of validators will be using it. And with those assumptions you can actually prove things statistically, which if we don't have the option, then you cannot prove anything. I think this is a big, big difference in UX for me. 

**Tim Beiko**
* So I guess there's a couple comments in the chat about, you know, being supportive, but not for, Shanghai. So I guess it seems unlikely we would get this in now. does it make sense to continue the conversation on the PR itself if it's something that's not gonna happen, like in the next couple days?Yeah.Okay, perfect. 
* So let's continue the conversation on the PR. but yeah, clearly it sounds like something there's interest from any of the client to, to support. anything else on this before we wrap? Move on. 


## Cancun Updates [21.24](https://youtu.be/ViLwzeIuJUc?t=1285)
* Okay. so I guess next up Cancun. so I went over the ETH magician's thread yesterday to try and like look at all the EIP that have been proposed so far. I've updated the Eth Magician's thread and also listed them on, on the agenda here. and I guess, the obviously as well is 4844 . The only thing we've, officially included so far. so that's, that's, you know, something we should take into consideration when, when talking about Cancun. and maybe the first thing to to cover is, all of these SSZ proposals. 
* So last week, or sorry, two weeks ago, we discussed this a bit on the call as well, but it seems like teams didn't have a ton of context. but basically because we are introducing SSZ as part of 4844, on, on the execution layer, as we're figuring out, do we wanna introduce more at the same time, at the very least, what is the format we wanna go with so that even if we don't introduce more, SSZ objects, whatever we do introduce in 4844 consistent with what we'll introduce in the future. so I don't know if any of the client teams have had time to look into this in the past couple weeks, if anyone has any kind of updates they wanna share on this. yeah. Okay. So I guess So. 

**MariusVanDerWijden**
* Oh Yeah, please, Yeah, each, each and I kind of had a discussion, I think it was, it's two weeks ago now, about this, and we kind of came to the conclusion that we're trying to optimize for different things. Yeah, it was in, the discord and hashtag data. so I think my focus was to make, the transaction as small as possible, while his focus was to make it as easy to verify by light clients as possible. 
* And, yeah, I that that there are basically, there are two different, ways we can do the SSC format or the at least two different ways proposed and one is smaller and one is easier to verify. And so we kind, I think we kind of have to make a decision what we want to prioritize. 

**Tim Beiko**
* Got it. Lucas, you have your hand up, is it? 

**Lukasz Rozmej**
* Yeah. So, this, they're like, because this is about only, this is, this is seeing the roots, right? But the question comes up, should we assist SSZ storage and network formats too? Might it be easier  to have just one, one format and or, or maybe we shouldn't, maybe we should keep it RLP, right? It is right now. So that's the question.
* And the other question is, how does this affect Cancun timelines, right? Because if we are cramming more and more, and this is not trivial, in my opinion, then yeah, it depends when we want to come from to right to comment. 

**Etan (Nimbus)**
* The network format is, is not really, does not really have to be bundled. it's only about the storage format for actually not even the storage format is bundled. Like everyone can store the transactions how they want. the format that is affected is how transactions are represented as part of the consensus execution payload. And the size difference that Marius mentioned is, primarily because, I mean one of the goals is to allow clients to use JSON RPC, while having a way to verify that what they receive is correct. 
* And there are three items in there, namely the transaction id, the sender of a transaction like the from address and for transactions that deploy a new contract, that contract address those three items, they are currently not part of the raw transaction and they can be computed from the raw transaction with the secp publicly recovery and some RLP.
* So if we want to include all three items, they either need to go into the receipt three or into the transactions tree. the size differences are mainly if we decide to put it into the transactions tree, then of course the transaction that includes the extra information is a bit bigger than the and than the other one. But the receipt is a bit smaller. And if we do it the other way that, that we put this extra information into the receipt, then the receipt is a bit bigger one way then than the other. 
* So ultimately the total size is probably comparable, but it doesn't affect the networking. That one can still be RLP if that's what people want. but it means that you have to convert back and forth, between one representation and the other whenever you receive a message and when you send it. 

**MariusVanDerWijden**
* And this conversion is, kind of costly actually. So, we try to have as little, conversions, as possible. So we store the transactions in the same format, that we send them on the network. 

**Etan (Nimbus)**
* Okay. I mean, then, then we can just update the network to exchange that in the same format as well, to avoid the conversion. But then it, I mean either the receipts or the transactions are getting a little bit bigger in like, depending on which one we choose. There is also one conversion that we cannot avoid. It is when we convert from a transaction before, like a raw transaction that's in the man pool, that one is using whatever format it originally was signed under, so that one cannot be changed. 
* That one is always an R L P or it's this block transaction with the network wrapper. So when those are bundled into a new, execution payload, they need to be converted, a single time. And when they are validated as part of new payload, they need to be converted back so that you can check the signature against the original representation. So there is this, during new payload and when baling a new block, like new payload get payload, where the conversions cannot be avoided regardless of which SSC format we choose, 

**Lightclient**
* I think that's okay because we already have to do that to calculate the hash anyways. 

**Tim Beiko**
* Danny, oh, sorry Danny, you can finish and then No, no, I just wanted to say Danny has his hands up. Yeah. Okay. 

**Danny**
* Thank you. I am curious before we go deeper on the technicals here and start talking about decision points, have we done an analysis or an ask of the community as to what this is going to break? I imagine it breaks tooling to a decent amount and then it certainly will break some on chain contracts, which I imagine many of them are upgradable, for example, some L tiers. But are there, like, have we done analysis of like, is there anything we're fully breaking by doing this transition? which, you know,  not to make a claim that we must not break anything, but I, I think that to make a decision about how to proceed, we'd need to know the answer to that. 

**Etan (Nimbus)**
* The only analysis that I made there is, to see whether, like, what, use cases would break. JSON RPC would still return the exact same data. it could just be extended to also include proof that it's actually correct. but if you have applications that depend on, the current Merkel, Patricia tri route, those would, essentially break because that, legacy route will will be removed. 
* I'm not sure how to gauge, which projects are affected concretely. I hope that the high profile ones have a mechanism in place to upgrade if they depend on this functionality. 

**Danny**
* Right? And like I know do have such a great functionality, it it's at least, worth at this point if we're seriously considering this, like yelling into the void to see if anyone comes up with something that we can't, patch. 
* Yeah, Tim, I'm there might be some automated analysis we can do here but it's hard to catch everything because this is like a relatively, you know, using, utilizing proofs against a root is like not obvious to Yeah, Automatically. 

**Tim Beiko**
* Okay. That's what I figured. so yeah, we can definitely make a call, for people to show up if, this breaks things. and yeah, it might be worth looking if there is some sort of fancier way that we can scan, you know, potentially transactions in the last year or, yeah, what's been deployed. Peter, 

**Peter Szilagyi**
* Just a very, very slight diversion. So previously it was, somebody asked, whether it makes sense to bundle this together with, Cancun with 4844 or not. just wanted to react to that. In my opinion, based on just the discussion of the past few minutes, you can see that this is a very, very deep, rabbit hole. And I do think, essentially it's, we really don't want to half as this. 
* So if you want to, I think the advantages are super nice and, but the question is what do we want to transition over? And my 2 cents would be to, I, I don't see this going in along with 4844. I would much rather just gather everything that needs to be done so that we can roll this out in one big go and update everything that's needed. And I think that's a completely separate effort and it won't really fit inside One problem. 

**MariusVanDerWijden**
* Like yeah. But one thing that we should, like just be aware of is that we, that the blog transaction is kind of written in a way so that it's, that is also kind of upgradeable  to this, to this new version.But I guess if we do the blog transactions similar to how we do the other transactions, then it should, 

**Tim Beiko**
* So are you saying, I'm not sure I understand, if you're saying that we need to be sure of the format today because blog transactions will use it, or are you saying that like it's fine to change the format of BL transactions in the future and basically I, 

**Peter Szilagyi**
* Yeah, I think Marius was trying to say that, since blog transactions are already introducing partial depend, or sorry, introducing dependencies and SSZ let's make sure that whatever block transactions do will be compatible with Okay. 

**Tim Beiko**
* Yeah, yeah, yeah. I, and yeah, I agree that's like the minimal decision ideally we would make is, even if, and we might not have a hundred percent certainty here, like there might be a format that's like better or worse for some reason. But like if we can have some confidence that whatever  we implement in SSZ for 4484 and is forward compatible, then that's better than having to like rechange it. 

**Etan (Nimbus)**
* And yeah, I, There are, three parts of this proposal and I think for each of them it can be decided separately when they should be included. the one that has to be in Cancun, if the block transaction is as SSZ is signature scheme like EIP  6493, because we need a signature scheme that cannot ever conflict with a future transaction type that we introduce or with an RLP transaction type. And the other one that's kind of orthogonal is the withdrawals route. 
* That one, the idea was to already convert it, with Shapella and that one was only delayed because, it was already late in the cycle when this was proposed. So that one can be moved into Cancun, without any controversies. The only one that is controversial is transactions route and receive route. 

**Peter Szilagyi**
* I wasn't really referring to controversial. I'm referring to simply work and making sure that nothing blows up. So my main issue is that 4484 is huge and anything that's sufficiently complicated beside it will be really messy because people will need to juggle two very complex things at the same time. 

**Tim Beiko**
* Right. But I guess what Ethan are you saying is that like we need a signature scheme for basically because we introduced for it 4844, which is an SSZ type, so we need some signature scheme that we agreed to in order to make sure there's not like conflicts with future transaction types. Is that correct? 

**Etan (Nimbus)**
* Yes. that, let me, I mean, the signature scheme is for transactions in the main pool. So that one is, regardless of how you format the SSZ transaction later as part of the execution tailored, you need to know how, how do we sign those transactions? And I mean,it's probably good to have the same signature scheme for all SSZ transactions. 
* Even, even if the individual transaction payloads can be whatever. I mean, there is no reason to align those, before, they are accessible through APIs. 

**Tim Beiko**
* Got it. 

**Peter Szilagyi**
* Can't we just, so currently 4484 for respect to use the SAP 2256, signatures, and can't we just keep those and then whenever we do this, SSZ switchover, then we also switch the signatures scheme. Is there a specific problem with doing that? 

**Etan (Nimbus)**
* Do you mean like keep it at zero Xfive plus SSZ code? 

**Peter Szilagyi**
* Yeah. 

**Etan (Nimbus)**
* One issue with that is if it's SSZ, you start getting problems when you look at it across different networks, including private networks, because with the SSE  transaction, the chain id, does not always end up at the same offset as it would if it were RLPN coded. 
* So you can have a signature on a private network that is type five, but some RLP format that accidentally serializes to the same hash as, as the SSE transaction on the main net for type five. I'm not sure how big that risk is if, but it could be that if both are using the same hashing and the same transaction type, but different encoding strategies like SSC versus RLP, that there may be a conflict. 

**Peter Szilagyi**
* I'm not really following because currently the with typed transactions, essentially the first bite is the type. 

**Etan (Nimbus)**
* So Yes, yes, that, but that one is network specific. Someone could create a private network like, a layer two that's EVM compatible, and they could define their own type five. Maybe they already have a type five and we don't know about it and someone sign transactions on it and uses the same key on main net as well.it's only across networks where you have those problems, 

**Andrew**
* But it's like hash collision, which is supposed to be extremely rare. So I guess it's like the probability is very low, Not hash. 

**Etan (Nimbus)**
* It's the, it's the serialized unsigned transaction that could, collide. And that one is not a mathematical property, it's just, you can construct an RLP object that has the same encoded value as an SSC object, as an SSC and coding of a different transaction. 

**Peter Szilagyi**
* Yeah, I mean that sounds exceedingly improbable to have an RLP something ma be valid both as an RLP and SSE decoded stuff and be actually meaningful. 

**Etan (Nimbus)**
* Sure. I mean that's, that's the open question whether, whether that is a real risk or, yeah. 

**Tim Beiko**
* So I guess, just based on this conversation, does anyone feel strongly, I guess, that we should do like the, you know, quote unquote full SSZ overhaul as part of Cancun? Or is this more about finding the minimal set of changes we want to do that are forward compatible? basically what, Peter was saying, because that can help just kind of prioritize like the, the future discussions where obviously we wanna understand the full implications, but there's a difference in do we start implementing this wholesale now or are we trying to find a minimum we can, we can do for Cancun? Andrew, 

**Andrew**
* I would concentrate on the minimum because we have to weigh, the, like I agree that with Peter that it is a big change, so we have to weigh the benefits of the SSE overhaul versus the other potential candidates. Our through through throughput is, as developers is limited. So yeah. 

**Tim Beiko**
* Okay. Yeah. And plus one from So I guess, we probably can't take a decision on the exact format right now, but I think, if this is something that teams can look into in the next couple weeks, that would be good. So we can start aligning on what's like, the right minimal scope for SSZ for Cancun. yeah. Does that make sense? Okay.
* So I, do you think we need a cautious about like the breakout rooms now cause it feels like there's all of what every day, but do you think we need a separate call to discuss this or can we have teams review it async in the next couple weeks and, you know, potentially discuss it on the next all core devs? 

**Etan (Nimbus)**
* I think, that's fine. Like just discussing it as part of All core devs.

**Tim Beiko**
* Yeah. and I think if if we get to the next ACD and like there's been literally zero progress, then maybe we can schedule a breakout room. But yeah. okay. So, like Andrew was saying, I guess, there are a lot of things being considered for Cancun. and yeah. 
* I wanted to list them here and it's probably worth of going over them kind of quickly to at least share kind of status updates and, and get some sort of temperature check from different teams about, the efforts. but high level, you know, there's everything around self-destruct. the EVMMAX proposal, solidity had, proposed, EIP 663, which is this unlimited swap and DUP instructions. we had EIP 5920, which we discussed quickly last time, the payoff code, there's everything around EOF, obviously 1153. and, moody had an update about the status in the agenda. 
* And then at the two letters that came up last time were, the BLS pre compile and the Beacon State Route Up code. so this is roughly everything that's, I believe after yesterday was, was proposed. 

## SELFDESTRUCT removal (4758, 6046, 6190, etc.) [44.44](https://youtu.be/ViLwzeIuJUc?t=2684)
* I guess on the self destruct side, I don't know if anyone has an update here. we did have this like deprecation warning as part of Shanghai. so I'd be curious to see if, you know, how strongly do people feel this is a priority? yeah. Where do people think we are in terms of specs and, and whatnot? yeah, Andrew, 

**Andrew**
* I think that removing self-destruct is very much a priority. So, to, yeah, we would like to do it in well as well as possible. I was also thinking that there was this analysis by Jupiter who suggested that there was one, one smart contract, pine Core using self-destruct, ephemerally. 
* So for, contract was created and self-destructed to within a transaction. So if we just, keep that, special case, if we allow, we keep self-destruct for, so if we keep, ephemeral self-destruct and deactivate non femoral self self-destruct, that might be a nice compromise and don't think we have a need. But if people here agree that it's, kind of a viable option, then I can create EIP or somebody can create EIP. But in general, I think remove self destructive is top priority. 

**Tim Beiko**
* Okay. Anyone else have thoughts? 

**Guillaume**
* Sorry. Accidentally raised my hand. Oh, yeah, I mean, apart from the fact, I also think it's a priority. yeah, not much to add. Sorry. 

**Tim Beiko**
* I guess maybe one question for you while you're on, unmuted. like, to be clear, so say we wanted to do vertical trees and, you know, not Cancun, but the fork after that, we need basically self destruct to be removed prior, right? Right. Like it would, if we didn't do this in Cancun, it means at the very least, we would push out vertical trees, another fork, right? 

**Guillaume**
* Yeah, exactly. and I will probably spontaneously combust as well. no, yeah. if, like self destruct needs to happen in Cancun, otherwise, yeah, will be pushed, indefinitely cuz there will, there will always be something, to come before. 

**Tim Beiko**
* Okay. and yeah, so I know there were some proposals around like basically what Andrew was saying, kind of allowing some sort of ephemeral transactions, to use self destruct. I know Alex from Ipson also had, some proposals. 
* So, I think that would probably be like the most important thing here in the next like couple weeks is if we can come up with like a spec for something that does deal with the multiple edge cases that doesn't, you know, break the contracts that use, that, use it the most, and that are like most popular today with this, and have an actual thing  we can look at. We, did review, another spec last call and, there was a lot of, there was a lot of like complexity in it. 
* So, yeah, it does feel like something where having a clear spec is the main blocker, but assuming we have that, I assume people would be pretty on board with, moving forward with it. do we have a self-destruct channel or something like that? I wonder, I guess we could use the execution dev channel at the very least to discuss this in the next couple weeks. if we don't have a self-destruct one. yeah. 

**Tim Beiko**
# EVMMAX: EIP-6601 & EIP-6690 [48.43](https://youtu.be/ViLwzeIuJUc?t=2923)
* Okay. next up, EVMMAX, I don't know, is Jared on the call? yes. 

**Jared**
* Hey, Tim here. 

**Tim Beiko**
* Hey, do you wanna give us an update? 

**Jared**
* Yeah. Hey,  I'm just joining. I just wanted to, just raise awareness. so recently I, or in fact yesterday I posted, EIP 6690, on Ethereum Magicians, which is, just a variant of, 6601, which was the latest, proposal update, update proposal, in 6690 is, the attempt to decouple the proposal from EOF, not to say, but, basically, it would be great to get more people just like clients specifically, like potentially looking into implementing this. And I think a great start, would be, 6690, cause I think that's the easiest to implement. but EOF also brings benefits.
*  I think that, so I would say, like as far as advantages go, I mean, if you compare it to something like EIP  2537, of course you're not gonna, be able to, implement, BLS operations as performantly as pre-compiled. I mean, that's kind of obvious. but, we get several other benefits. Like, for example, like I've noted, in both of both of the recent EIP, this basically allow us to replace the mode XP pre-compiled for all of the inputs that I've seen it used on when I've, scanned the chain. and then, other things like, the ZK friendly hash functions such as MIM C for example the I MIM C and it was 80% faster or 80% more, cost 80% cheaper than the zycom lib implementation, which was being used in production by tornado cash. So I would just say like, just to sum up, it would be great to get more eyes on this and if we do or don't wanna move forward, yeah, it would be good to, to hear something Thanks. 

**Tim Beiko**
* Any thoughts, comments on EVMMAX? Okay. And then, yeah, so I linked both, both your two new proposals in the, in the agenda, Jared, so people can go and, and comment on that, async. 

**Jared**
* Cool. Great. 

**Tim Beiko**
* Sweet. Thanks for the update. and I guess, oh, Marius, do you have something to say? 

**Marius**
* Yeah, so, okay. One thing that I would like to highlight is that, EVMMAX is not only cool for BLS 12381, but can also be used in a bunch of other use cases. so I think we should even consider this even if we decide  to implement the BLS pre-compiled. I think the b like the BLS pre-compiled, which we probably will talk about, are very important and, much needed. 
* But, EVMMAX or like modular arithmatic on, within the EVM is something that is, that has a lot of use cases and, beyond on the, the, the BLS prepo, yeah, that's a good point. 

**Jared**
* I probably should have mentioned that. as far as I could tell, you could, and, and maybe somebody can correct this if this is wrong, but as far as I can tell, basically any elliptic curve, could be implemented with this proposal. 
* And another thing to consider is that if you have a higher, a higher, width base modules, like I know there's some curves that are like at like 768 bits or more, as far as I can tell, this would actually be like pretty close in performance to what you could hypothetically get with a pre-com compiled just because, modular multiplication has quadratic complexity. So, I mean, yeah. But yeah, thank Yeah, good point, Mary. Thanks. 


**Tim Beiko**
* Yeah, and I think like several years ago we had a very similar discussion around, I think this was the Berlin Fork where we discussed BLS versus, EVM 384 at the time. And like, I think, and there was like a similar, you know, concern around like, should, we do one or the other? 
* And we ended up not doing BLS because EVM 384, might happen soon. And I think it probably makes sense given the, importance of like BLS to like consider it, also separately and even if there's like redundant functionality, that might be one of the few cases where it's worth it relative to, delaying BLS if, if we are gonna do EVMMAX, at a later date. Yeah. 

**Jared**
* Yeah. I guess just from the user's perspective, what really would be the difference? I mean, you're saving a bit of gas, but like what it, it would be great to quantify, and maybe like extrapolate out from like how people like are currently using BN128 and just like, I don't know, assume that they'll just move to BLS and then like extrapolate out exactly what we are getting in terms of savings overall, with pre-com compiles. 
* Right. Which, which is hard because I don't have all the EVM max operations or all the BLS operations implemented at EV max, but it's fairly easy to guess how much they'll cost. 

**Tim Beiko**
* Yeah. Right. And, , and I think the, maybe another way to frame this as like, assume we do BLS in the next forks and EVMMAX in the fork after, you know, what's the benefit of users to have access to BLS, you know, six months, 12 months early, right? And maybe they eventually moves to like using it natively and EVMMAX or something.
* But that's, I think that's the other trade off that's like worth considering is, if we do both, but not at the same time, you know, is there like, and, you know, one way to ask this question is like if we, how would things be different if we had had BLS in like Berlin, you know, several years ago? yeah, regardless of just like the raw gas costs, I guess. Yeah. 

**Jared**
* Well if it's not factoring the raw gas costs, wouldn't EVMMAX be strictly like disregarding the raw gas costs? Wouldn't EVMMAX be strictly better in that case? Because you can, I mean, you can just implement more stuff, right? 

**Tim Beiko**
* Right, right. But but if you get it, if you get BLS sooner, right? That's the thing. I mean Oh Yeah, Yeah. Like that's, the cost is like not just the gas cost of like each call, but it's being able to use it and, you know, six months versus 12 months. 

**Jared**
* Yeah. Yeah. I mean, I'm biased, but I would say EVMMAX is, is, seems simpler to me than BLS. and I would implore people to take a look because it's really like, really not that complicated.  I just lifted a few, like all I had to do was like adapt a few hundred lines of assembly code from Blast to get the most performant implementation, anyways. Okay. Yeah. 


# EOF [57.43](https://youtu.be/ViLwzeIuJUc?t=3462)
**Tim Beiko**
* Yeah. Just wanna be mindful of time. Anything else on EVMMAX? Okay. Yeah. So we can continue that discussion, on the threads. and then I guess, the two things it does touch on is EOF, and BBLs, but does anyone have an update on EOF? was Lightclient on the call, oh, I thought he was for a while. Oh yeah, he is. I'm here. Okay. 

**Lightclient**
* I don't have much of an update, honestly. I haven't been working on EOF I've just kind of been running the EOF breakout rooms, which we've got another one scheduled for next week. yeah, I don't know. EOF 1.1 is kind of, taking in a lot of the thoughts around the discussions in Austria and what EOF v2 might look like. 
* And that's, sort of coming together and I think that they've got this implemented in Geth now. I just haven't, followed it super closely the last couple weeks. 

**Tim Beiko**
* What's the best place, for someone to like follow the latest on EOF. 

**Lightclient**
* The #EVM discord. Okay, cool. 

**Tim Beiko**
* Andrew?

**Andrew**
* I have a small technical suggestion. So if we want like EOF whatever, 1.5 or whatnot with, Vatalik idea of non observability, that will be quite different from EOF1. So, my suggestion is to, for ease of referencing, create a single EIP, new EOF so that we have everything that we want in a single release, in a single EIP. 

**Danno**
* Yeah, So there's multiple facets that are easier to understand in single leaves, but I think a single combo eve that says point to these five is probably what we might wind up getting. because some of these are fairly, separated and we put 'em together in one giant document and it looks like impossible, but you break it up into the five key component parts and it's actually, and you know, the sub some is the whole is greater than the sum of the parts. I think, you know, we could write one that would help, help add to it. but I mean like the stuff like the observability.
* I mean if the current plan we're gonna stick with where we, that still have up, up a discussion, if we do the one one in Cancun and the two oh in Prague were in one, one, we remove key features that, would be necessary to preserve observability. And in Prague we would ship the, non observability preserving versions of things that we're taking out. you know, it's, I think a giant  would obscure some of what we're doing and, and the step work in there and to make it harder to explain.
* So  I appreciate the need for, to be able to get your hands around the full scope, but we still need to have clear seat, you know, that the structure of EIP does not really lend itself to like, you know, five different subsections because there's like one big, the rationale and the implementation are often tightly coupled. So  we should have a combo EIP to point to the sub-components, but I don't know if a full leap of everything together is gonna be a good idea. 

**Andrew**
* Understood. 

## EIP-2537: Precompile for BLS12-381 curve operations  [1:01:49](https://youtu.be/ViLwzeIuJUc?t=3709)
**Tim Beiko**
* Okay. anything else on EOF now? Okay, so I guess maybe next up, we did touch on this already a bit, but, BLS pre-complier, I don't know if there's anything to add here. We've discussed it several times, but in case there's any updates or comments people want on this. 

**Stokes**
* Yeah, I'll just say that, kinda echoing what we said earlier in the call, you know, this curve is really important to Ethereum I would really strongly suggest we consider shipping the precompiles even though there's very exciting work with EVM Max. 
* You know, we could go ahead and get the curve today and then when EVM Max is ready, we ship it and you know, there are plenty of other use cases for EVM Max beyond this that are also really important. But, you know, this curve is used on layer, so it's just, something we should do asap in my opinion. 

**Tim Beiko**
* Cool. 

**Danno**
* Deni, The one thing I would ask if we do that is that we, take another look at the gas prices. when we did Berlin, we priced it against, a gas metric of 35 million gas per second, which is about, 28, nanoseconds per gas, performance wise, that, that provides an upward limit as to what we could expect local clients  to perform. and it makes a BLS not the BLS ones, the, the lowest point in, in the, whole EVM architecture in cap at 35 for a lot of performance considerations. 
* I could explain why that's gonna be the case, but I prefer if we were to reprice the gas on some assumption of something more like 50 gas per second, 50 million gas per second, which would result in higher gas prices, but at the same time, would allow, the, the conceptual maximum three foot of EVM to increase up to 50 billion gas per second. 

**Stokes**
* Yeah, I think it's four 30. Revisiting the EIP, especially if you wanna like very seriously consider it for Cancun. a question I have, since we're all here, does anyone feel strongly about the EIP 2537 having like a large number of pre-compiles versus say just one? 

**Marius**
* Yeah, I kind of do. 

**Stokes**
* I'm just wondering cuz like, it be pretty easy I think to rewrite the EIP where like, you know, basically there's a type switch in the first bite, something like that. and the question then is like, is one more palatable than the other? 

**Marius**
* What, what do you mean by having a type switch? 

**Stokes**
* Well, just like, rather than say like nine EIP or sorry, 9 peep-an-eip, you just basically call one peep-an-eip, but the first bite says, okay, this is an ad, this is a bowl, this is a pairing, whatever. 

**Marius**
* Oh, I don't care about that. But I think maybe we should think about not doing all nine pre-compiles, how many of them can I actually need it. 

**Stokes**
* All of them. I think if anything we actually should add two more Okay. 

**Marius**
* I don't like that. Yeah. Okay. 

**Dankrad**
* Just wanted to comment on the gas costs because they, like if the benchmarks were done two years ago, I think the BLS libraries are also significantly faster now, so it's likely that gas costs from back then would be an overestimate rather than underestimate. Now even if we want to target 50 million gas per second, or rather what's been done recently, I think it's more just compared to existing and pre-compiled sent off codes Right. 

**Tim Beiko**
* Then it's probably pretty easy to rebenchmark them cuz we just ran benchmarks on every client's for the 444 pre-compiled. So it shouldn't be hard to do it for BLS as well. 


**Danno**
* So I would prefer to keep all nine or possibly 11 pre-compiled. one of the reasons is right now pre-compiled, they do one thing, each pre-compiled does one function and we don't have any pre-compiles that have like a switch bit to do different things based on what's coming in. so we would also have to test in addition to the nine or 11 forks coming  that pre-com compiled, we need to write test cases to test the switching logic, which would increase the testing load. It's not necessarily that bad. 
* But I think the real concern there that I have with it is by putting all into one pre-compiled, we're asking the true complexity of what's being asked to implement this and what it really means to the E V M that we're doing nine different functions behind one pre-com compile. So I think it's being more upfront and clear about what the complexity of what's going on is, because originally this started out, as a arbitrary length and arbitrary distance, you know, arbitrary bit width and arbitrary, sized, set of precompile that in theory could have enabled anything random times. And the issue there is that they were gonna, you know, in theory could turn more stuff on as we go later, you know, it, it makes a compatibility problem cause what if we add more switches, and we add, you know, 13, 14 and 15, then all of a sudden code out there, we're gonna have to have different versions of the pre-compiled. whereas before, you know, if you switch on version 13, the pre-compiled would fail, then all of a sudden it works. I think switching inside the pre-compile is the wrong place to add the complexity, weekly held. I can be talked away from that, but that's why I prefer multiple pre-compiles. 

**Stokes**
* Yeah, that makes sense to me. 

**Tim Beiko**
* Yeah, and we, we did switch it out to multiple pre-compiles when we were testing BBLs for Berlin, so it feels like it's, probably a mistake if we say we're gonna rebundle them together and then start re-implementing and then we'll come to testing and figure out it might be better to separate them again. So yeah, unless something has changed, probably makes sense to keep them separate. that was your hand still up from last Dankard or was there anything else you wanted to add? 

# EIP-1153 Transient Storage [1:08:17](https://youtu.be/ViLwzeIuJUc?t=4097)
**Tim Beiko**
* No worries. okay, anything else on BLS? okay, next one. So 1153. I don't think, I don't know if there's any, champion if Sarah or Moody or on the call. 

**Saraeynolds**
* Hi Tim. Yes. yeah, I posted an update in the agenda, so feel free, people can look there, but only new update is that we have the tests now merged in the Ethereum test repo. and then yeah, just again calling out that the implementations in Geth, Nethermind, Besu and Ethereum JS have been run against this suite and those are all merged as well. Thanks. 

**Tim Beiko**
* Nice. Thank you. anyone have questions, comments on 1153? Okay, almost done. We have three left. 4788. this is the Beacon state root in the EVM. I guess, yeah, Lucas, do you wanna, sure, I just saw your chat message. Do you wanna share more? 

**Lukasz**
* Oh, no, I'm just saying I'm okay. I'm pro including 1153 to Cancun. like it's, most of things are done, so why should be, postponed? I don't see any point. 

**Tim Beiko**
* Cool. I guess I wouldn't, because we have like a bunch of open EIP, I probably wouldn't make a decision today about including any of them, but, yeah, we can definitely do that in like the next couple calls. yeah. Anything else on 1153? Sorry, before we move on to the next one? 

**Gcolvin**
* No, I very much support it will save a lot of gas and, save a lot on the tax surface. we've just got to get ways to use storage that aren't so hard to get right. So thanks very much for, for pushing this forward. 


## EIP-4788: Beacon state root in the EVM [1:10:32](https://youtu.be/ViLwzeIuJUc?t=4232)
**Tim Beiko**
* Cool. anything else? Okay, Yeah, so next one. Yeah, so 47 88, that's the Beacon State route in the E V M. We also discussed this briefly last time. I think Danny had a comment, plus wanting this as well before he left. Alex is there any updates there? Anything you wanted to share? 

**Stokes**
* Yeah, I mean I would just also plus one this, this along with like the BLS picking piles or just be less etic generally is like really important for a lot of, staking pool use cases, which given the predominance of Lido and sort of the, you know, fragile position that one dominant staking pool provider as the network, I think it's really important to encourage and support alternatives. 
* So, for that reason I think this one and also some sort of BLS solution is like really to do quite quickly. yeah, the EIP itself 4788 I think is pretty ready to go. I can make a pass on it before the next Allcoredev, but yeah, this one, this one should be pretty lightweight and yeah, I think generally is pretty good support for it. So I think we should include it. 


##EIP-663 unlimited swap and dup instructions [1:11:59](https://youtu.be/ViLwzeIuJUc?t=4319)
**Tim Beiko**
* Thanks. Any comments, thoughts on 4788? Okay, two to go. next up, 663. So this was mentioned by the Solidity team, right before we, actually right when we were discussing EOF for Shanghai and they mentioned that this would actually be very helpful for them. in addition, I don't know if anyone on the call is a strong supporter of 663 or has any updates or, yeah, concerns to Share. 

**Danno**
* I think it's important to point out that it's gonna be EOF only because of the use of immediates and this is the story to stuff the EOF opens the door for, in evolution of the EVM.

**Tim Beiko**
* So generally I'm in favor of it When you say EOF only, so you're saying we should do 663 in like EOF V1. 

**Danno**
* Basically We can't do it without EOF, so we do it in neither EOFone or it comes in later, we may as well do it now while Solidity is rebuilding their compiler. 

**Tim Beiko**
* Okay. This might be a stupid question, but given this is like an EIP from 2017 and EOF, like I guess they, they've adapted the EIP like recently to reflect this? 

**Danno**
* Yeah, they've called out EOF I think at one point they were gonna do the immediates until the issues with immediates, was shown to be a, a security problem and then it was adapted I think to be stack based, but now they're back to immediate based. 

**Tim Beiko**
* Okay. And EOF enabled them to do that basically. 

**Danno**
* Exactly. 

## EIP-5920: PAY opcode [1:13:48](https://youtu.be/ViLwzeIuJUc?t=4428)
**Tim Beiko**
* Got It. Okay. Any other thoughts, comments about 663? Okay. and then last one, so we discussed this briefly on the last call, but was the PAY opcode code is the other one that's been proposed? I don't know if there's anything new since the last call that anyone wanted to bring up about that. 

**Danno**
* I'm skeptical on this one. I don't see what it adds that provides significant value. some of the rationale, is based on, well there's a radio security exploit, you can do this stuff anyway. But I dunno if the answer to that security exploit is to open the door wide open and make it cheaper, weekly held, I can be talked back, but generally speaking I'm skeptical. 

**Tim Beiko**
* Got it. Any other thoughts, comments? Okay. so we made it through the list. I guess high level, you know, for client teams, it's probably really important in the next couple weeks to start thinking through like all of these and, you know, what makes the most sense to potentially bundle together.
* I think for like the sort of three bigger efforts, so like, well I guess the four bigger efforts, right? Like for SSZ, self-destruct, EOF, EVMMAX, like thinking what's a, what's like reasonable subsets to consider for Cancun is probably the most important thing. and then for these, I guess smaller EIP, you know, whether they make sense bundled with, 4844 and then potentially some of the larger, other things. yeah, and we can keep discussing this in the next couple weeks, but any other comments or thoughts about Cancun generally? 
* Okay. sweet. So, last up, Puja, you've put together a survey these past few weeks, for node operators. do you wanna take a couple minutes to walk us through that? 

**Pooja**
* Yes. thank you Tim, for that. So exactly two months ago we floated a survey for validators users to share their experience about client node running and what can be done to improve, present network distribution. Tim, if you can maybe pull up the, Oh yeah, I posted it there. 

**Tim Beiko**
* If you wanna share your screen and, and, and give a quick overview, we we have some time, we can do that as well. I can put it up if you, if you want otherwise, but it might be easier if you're the one talking. 

**Pooja**
* Sure. Oh, I just lost my listing Oh, I got it. You got it. I hope my screen is visible. 

**Tim Beiko**
* It is, yes. 

**Pooja**
* Are we able to see the medium block? 

**Tim Beiko**
* Yeah, we do. 

**Pooja**
* Okay. so a couple of weeks, not exactly a couple of weeks, actually, exactly. Two months ago we floated a survey for Etherum validators to, like collect their feedbacks and thoughts on what they think about present client distribution. What are their experience with the working with those clients like, if they are staking or they are running client node for any different purposes, they have, responded quite generously by sharing all their thoughts. the service sample size was really low in comparison to the present active validator on the network and it's less than 1%. but we believe that the data provided by them could be useful for client team to understand, what are the requirement of users, what they like and dislike most about, every individual client. 
* So we received this response from about, users from about 40 countries. And obviously staking is the most, prevalent reason for running, Ethereum network node. The representation of, chart here is different from what we do see at, client diversity.org. That's because again, of the sample size of the data, that may not be the exact, they may not be consistent with the percentage that is being shown there. However, the information shared is, almost, similar like, Prism, Lighthouse are the favorite client on the consensus side and Geth is predominant on the execution side. 
* We did receive a response to different questions in terms of how many pairs are being run by a single validator, like are they planning to have backups of it or not. I have tried to put together some comments. Obviously all the responses could not be added to this, report. So we have tried to add, multiple repeated comments by user and we also ask questions about if they have to switch clients for client diversity or for any purpose. What would be the reason you would like to switch and what could be done for you from client teams that you would consider running minority client like client, which is not in the majority network shareholder right now.
* So these are the, these are the responses that we have tried to capture and there is one very interesting thing like what can be done, what features should be added by different client team providers for you to help out with the staking of Ethereum the help of what can be added to help you, continue doing the staking on Ethereum blockchain. And they have provided quite a lot of input in that direction. Like they would love to have a ELCL client packages and like their testing could be more thorough. 
* One click could be really good to, include more users and all. there are some suggestions on MEV Boost site as well. So I would, encourage your client teams to maybe go through the report and other users to understand what features are being provided by the these clients. What can be like, you know, suit their particular need. As I mentioned earlier, we could not add all the data points, but we have tried to include multiple comments. 
But if any client team is interested in learning about, what all comments did we receive for individual clients, please reach out to me and I will share the, responses received from users. So, yeah, that's all. Thank you. 

**Tim Beiko**
* Thank you. Yeah, there was a comment on the chat. I'm not a hundred percent sure about this, but, basically some of the like numbers of clients use end up being greater than a hundred percent, but I assume this is because people were able to say like they used more than one client, right? So there people that is correct saying like they use like Geth and Besu or something like that. 

**Pooja**
* That is correct. So the option, the questions were multiple, multiple answers so they can choose more than one client if they're running multiple nodes. 

**Tim Beiko**
* Got it. Any questions, comments, thoughts on their reports? Okay, well thank you Pooja. And yeah, I guess we can wrap up then. Thanks everyone. and talk to you all soon. Thank you. 
* Thanks everyone. Thanks. Bye everyone. Bye everyone. Thanks. Bye. 

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
Mar 30, 2023, 14:00-15:30 UTC




