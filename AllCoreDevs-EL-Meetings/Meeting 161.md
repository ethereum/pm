# Execution Layer Meeting 161
### Meeting Date/Time: May 11, 2023, 14:00-15:30 UTC
### Meeting Duration: 1:49:39 
### [GitHub Agenda](https://github.com/ethereum/pm/issues/768)
### [Video of the meeting](https://www.youtube.com/watch?v=s6q5z53SICE&t=2s)
### Moderator: Tim Bieko
### Notes: Metago

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 161.1 | 4844 precompile input/output endianness mismatch: Gajinder can make a pr to suggest all field elements be big endian. More discussion will be moved offline and feedback will be solicited before merging the pr.
| 161.2 | RLPing 4844: EL, CL vs. SSZ: Move 4844 to use RLP, a PR can be stood up for all of version of the block. Add that to the block, move the EL to RLP, not introducing RLP on the CL and use all of this for devnet 6. , if possible, if people could review it in the next couple of days, and it can be discussed on Monday’s 4844 call.
| 161.3 | Explicit Clarification on Block Validity with Blob Transactions using an Invalid Versioned Hash: Mario will open a pr for the small issues. 
| 161.4 | KZG libraries: A transaction type channel will be used to continue KZG libraries discussion offline.
| 161.5 | Mcopy, payoff, BLS precompiles, and EIP 4478 will be bumped to next ACDE meeting. 





# Agenda

# [Cancun Scope Planning]( https://ethereum-magicians.org/t/cancun-network-upgrade-meta-thread/12060) [03:04]( https://www.youtube.com/watch?v=s6q5z53SICE&t=2s) 

**Tim**
We are now live. Morning everyone and welcome to ACDE 161. So yesterday, if people have any more thoughts or, you know, discussions we want to have around Cancun's scope, we can do that first. Then it probably makes sense to spend most of the call talking about implementation for the current Cancun stuff and specifically for 4844. There's a bunch of open issues that I've listed on the agenda. And at the end, we have Zak on, who wants to talk about a kind of a funky EIP because it would only apply to L2 and, you know, whether this should even be part of all core devs is an open question. So we can go through that towards the end. 

Yeah, I guess the kick us off on the Cancun stuff. So on the last call, we sort of agreed to include a bunch of EIPs. So at 1153, 4844 was obviously included. This SSZ optional EIP and then the self-destruct removal. We also see a few more so the BLS precompile, the beacon block root and the SSZ transaction signature scheme. I guess that if any of the clients feel like have any updated views on that, like anything that they think we should be considering or, yeah, I'll pause here. Otherwise, its fine to keep it as is and keep going with that. 

Okay. So we'll leave this as is and I assume based on the SSZ conversation, we might make some changes, if not today, then maybe in the next few calls or at least changing the actual specs. 

Okay. So next up, actually, sorry, just before we wrap up here, I guess I'll assume that by default, we sort of keep this scope for Cancun and if anybody wants to change it going forward, just put something in the agenda around the Eth Magicians thread and I'll pick it up from there. But this way, we don't have to go over this every call. Okay. Yeah. 

# Implementation & testing progress [05:34]( https://www.youtube.com/live/s6q5z53SICE?feature=share&t=334) 

## EIP 4844

### 4844 precompile input/output endianness mismatch

And so next up, 4844. So there were a couple open issues or concerns. So you can just go through them. First, Andrew, you mentioned the difference between the input and outputs in the precompile being little endian versus big endian. Do you want to give some context on that? 

**Andrew**
Yeah, sure. I think the little endian encoding was inherited from CL or was just taking from CL and on the CL side, things are little endian, but now the reason and on the outside, in the EVM, most things are big endian. There are some kind of some inconsistencies, I think, break to precompile might have some inconsistency, but most things are big endian. And now we have this weird situation where Z and Y are like the two inputs. I'm not sure about the rest of the inputs, but at least two inputs are little endian while the outputs are big endian of the point evaluation precompile. And I'm just thinking, we can be okay with it, but maybe we should just explicitly clarify it in the EIPs that we do have this inconsistency. 

Oh, I don't know, what other views are. We might want to reconsider this. 

**Tim**
Does anyone either have strong opinion on this or like a rationale for why we should keep it this way? 

**Andrew**
I think the output is kind of mostly for informational purposes, the output of the precompile, so it's static, maybe it's not to be good ?. So if we leave it as this, I think we should just have the extra clarification to the EIP that we just highlighted the inconsistency. 

**Tim**
Okay, and there's some comments in the chat from I think all the other CL clients saying they don't like little endian on the EL. 

**Marius**
So I think we should have like a really good reason to have the inputs little endian otherwise we should just make it big endian. 

**Justin**
I think if there's any order or transition between little endian and big endian, it should be as a high level as possible. And what we're talking about is way too low level to make that affordance. 

**Tim**
Okay, so this, and yeah, there's like plus ones from all the EL teams on Marius' comments. Should we just make this change the spectrum, put everything to big endian, and that means everything on the EL stays low endian. Oh, yeah, Ethan has a good question. Does this affect some of the underlying crypto libraries if we switched everything to big endian?

**Andrew**
I think it can read the inputs in both big endian and little endian, you just have to specify which. 

**Etan**
But does it convert twice because usually the libraries have like a native order that they prefer to operate on. 

**Andrew**
Even if it converts, so it will read the inputs in its native representation. So there might be some conversion, but it's a very fast operation. Because it's negligible compared to the main runtime of the precompile. 

**Marius**
Yeah, I think we shouldn't take the time for the conversion into account when making this decision. This is more about, like if for some reason all the inputs that are going to be into this precompile are already little endian, then it would kind, still not really much for me would make that much sense to have it little endian. But I would see the point. I don't think execution speed should be like should be a consideration here. Like the big endian to little endian conversion is so fast, like that makes no sense. And if there's a really important issue why we need this, then I would accept it. But from my point of view, I have no idea what authors thought about. So I would just go and say let's make it big Endian as everything else. 

**Tim**
Okay, does anyone disagree with that? 

**Guillaume**
Not disagreement per se, but we should check whoever created this effect. I mean, there must be a reason why it's just because we can't say why it's little endian doesn't mean there's no reason. I mean, Dankrad, I believe is on the call is here, but Dankrad, do you have any thoughts on that?

**Dankrad**
Sorry, just joined. I didn't get the contextjust now.

**Tim**
Is there a reason why the precompile in 44 for uses little endian? And would there be a problem if we converted everything to big endian just to be consistent with the entire rest of the EL?

**Dankrad**
Oh, I see. All right, that's a very good question. Yeah, I mean, this is like a difficult one because we are like starting to switch. Yeah, like the CL everything is big endian. Yeah, I don't know. Honestly. I don't know. I don't know how much we thought about this.

Okay, so yeah, so there's no reason within 4844 for why it's like much better to have the inputs be little endian. It's kind of a default design on the CL that sort of?

**Dankrad**
Yes, I mean, I guess like there are two things like the CL is big endian, but also crypto libraries tend to be big endians. So I guess they tend to be bigger.
And I'm sorry. So it's actually the opposite. Yeah, it might actually make more sense than to make it big endian also because the EL might be some computations in using those integers. Yeah.

**Tim**
Okay, and I don't know if pro's on the call. No, so I guess what we can do is at least we can open a PR on the EIP to make it big endian and leave it up for a few days for, you know, if pro lows, the other major author that's not here or if anyone else have like has objections, they can obviously raise it on the PR, but assuming that there's no objections, we just move it to big endian. Mikhail?

**Mikhail**
Yes, far as I can see this back for it for us back. First to verify case, it's a true function that is defined in the one's TL, which is little endian then I believe. So that's that's probably the reason for that. 

**tim*8
Sorry, which function did you say?


**Mikhail**
Verify KZG proof. 

**Tim**
Oh

**Mikhail**
So the precompile, precompile as it is specified calls to this function and this dysfunction is specified in the in CL spec and CL spec is little endian I believe so that's why it is specified this way. I mean, like this, why inputs should be little endian to align with the CL. 

**Tim**
And I guess otherwise we would have to do this like conversion engine API or something like that. 

**Marius**
But what's the what's the output on the contents layer? Is it also big endian? 

**Mario**
Well, I think this is insertion, right? Is it it's a search that the verification is.


**Andrew**
Yeah, the output is fixed and it is specified in the currently that the output is big endian. So that's why it's inconsistent at the moment.

**Dankrad**
So I don't think the CL directly calls verify KZG proof, right? It does the blob verification, but never verifies KZG proof as far as I know. So it's fine to change that function, but I mean, it is going to be a bit weird because now the KZG library will have both big and little endian interfaces. 

**Tim**
Right. And I guess the question is where should those like if we're using big endian somewhere and little endian somewhere else, we're going to need to have both like interfaces somewhere and the question is where's like the least awkward part for that. And I guess the argument from the EL folks was that it is really weird to have this as part of a single precompile input and output on the EL.

I guess, yeah, if we can at least put up the PR to propose the change and, you know, move the discussion there in the next couple of days, that would be good. There's a 4844 call on Monday if we want to talk about this in more detail, or if there's any sort of objections that come up in the next couple of days. Which seems reasonable to at least draft this spec and yeah, take it from there? And I guess if there's no strong objections, just merge it in the EIP?
Does anyone want to volunteer to write that PR? 

**George**
So just to understand this one, if the PR gets merged and then we definitely need to change the KZG libraries, but does anything else change? What changes to do with things?

**Mikhail**
What do you need to change the libraries? 

**George**
Because my understanding is that we're talking about the input output of the verified KZG proof, which is what the library does or am I off-topic. What is it?

**Mikhil**
I think that it can be stacked in a way that, okay, so we do a conversion from big endian to little endian, yeah, but that will be a bit of an overhead. But it can be stacked out in this way to emphasize that verify KZG function is little endian. I mean, like, accepts little endian inputs. So I know that's one of the ways, not necessarily change the libraries, but just change this stack. It depends on how we want to handle this. 

**Tim**
Okay. Oh, Andrew? 

**Andrew**
Yeah, I was just thinking, so we can add a parameter to that function that passes the inputs or whatever, like, verify. So basically, a parameterized the function where it's a big endian or little endian, and then explicitly is set it on the outside. And I was thinking about the BLAST libraries. The BLAST library can be both, but maybe on top of BLAST, the libraries might have to be too...We might need to change the intermediate libraries…KZG libraries. 

**Tim**
And I guess, yeah, so even if we need to modify the libraries a bit, do we still think it's a worthwhile change? 

**Andrew**
Well, I think it just adds clarity, because...So if you have that little endian parameter as an extra explicit parameter to the  function, then there is no ambiguity. You see it, okay, in my definition of the precompile, everything is big endian, and it's explicit, because right now, it's as a specified...It's not immediately obvious that there is an inconsistency, because that function is defined on the CL side, and without that extra knowledge that everything is CL is little endian then you don't... Just reading the EIP, you don't see it, you don't see the inconsistency. With explicit endian argument, everything is just more explicit. 

**Tim**
Okay, any other thoughts? 

**Marius**
I think the important part is actually how are contracts going to use this? And if the smart contracts are going to use big endian in everything else, and they now need to do the big endion to little endion conversion in their contract to call the precompile that does this conversion in reverse, then that's kind of bad, I think. So we should make sure that whatever we choose, we choose it into accordance to the people that call the precompile. 

**Dankrad**
I do agree with that. I think it hasn't been given that much thought. One thing that is going to be interesting here is that obviously the group elements are also in theory, I mean they're large integers. I guess they are kind of compressed according to the BLS standard. But it's also potentially possible that in the future someone would want to do computations with these, especially once we have BLS precompiles. But yeah, I agree that for the field elements, it does seem to make much more sense to have them be big endian. 

**Tim**
Okay, yeah, I think it's worth at least making the suggestion in the EIP, so Gajinder said he can do that, and kind of moving the discussion offline and getting more feedback on it before we merge it in. Yeah, does that make sense, everyone? 

### RLPing 4844: [EL]( https://github.com/ethereum/EIPs/pull/6985), [CL]( https://github.com/ethereum/consensus-specs/pull/3345#issuecomment-1540820234)  v [SSZ]( https://hackmd.io/nz-IqXLPQ-yahFPFlPl62A) [23:05]( https://www.youtube.com/live/s6q5z53SICE?feature=share&t=1385)  

Okay, next up then, so the big thing we discussed over the past two weeks was what to do with SSZ on the EL as well. There was a bunch of issues trying to get the libraries working in some courts of SSZ on the EL and then Matt put up a PR to show what it would look like if we just use RLP instead of SSZ for 4844 and Hsiao Wei put up a PR on the CL side as well to kind of show the impact this would have on the CL specs. And there was some recent conversation on that second PR. So, I guess I'd be curious to hear, yeah, from teams, what do people feel is the best path forward at this point? Should we move the EL transactions to use RLP? 

If so, what can we do on the CL specs to minimize the pain of bringing it in? Yeah, and I know like Ryan, Potuz, Danny, you were all chatting about that on the issue in the past few days. If any of you want to share your thoughts, yeah, that'd be it. 

**Danny**
Yeah, so there's definitely a desire not to have RLP as an explicit dependency on the CL for more than one reason, but the, so I think if we did go this path of RLP as the blob transaction encoding, we would want to do something like Matt’s proposal, but I think Matt’s proposal mentioned that to put these version hashes in the blob sidecars. Instead, I think that what we think makes sense is that they would be some sort of adjunct list inside of the actual block body. We want to have the requirement that the block can be executed on the consensus layer and execution layer without having the blob sidecars on hand. And so we would shove them into the block body. I think that's kind of in line with the proposal. It is a bit more of a breaking change, but this is a breaking change. So I don't think that's a, does that makes sense?

**Tim**
 Yes, Andrew?

**Andrew**
Yeah, I was just thinking like the thinking again, and to my mind, the current situation is not too bad. Because the main concern with the current spec is that we are going to have a different SSZ format for transactions. So we will have to change the current like the block transactions into something else. But on the other hand, we are going to do the same if now we revert back to using ROP for block  transactions, then I think Marius told that with that, like the block transactions will be temporary. And when we figure out how to do SSZ properly, we kind of introduce a new type of block transactions like which is proper SSZ. But then again, if we are doing that, then like having this temporary SSZ transaction type of block transactions, again, it's only an intermediate solution. And on the upside, we don't have to introduce RLP into SSZ and so on. So I kind of currently, my thinking is that the current solution is not too bad. The current spec. 

**Danny**
So I hear you on that. The main question is, okay, if we're going to have to change it, do we want to introduce a very limited additional SSZ dependency on the execution layer that might ripple outward into potentially how L2 wallets and other things utilize this? So it's the question of if we're not going to do it right, should we limit the dependency addition through the subject mechanism? The nice thing about the method on the consensus layer that was proposed by Lightclient is that it actually makes whatever the encoding is of these transactions, whether they change in the future kind of transparent to the consensus layer. Like the consensus layer right now can't really read transactions. And this is like a, we have this exceptional way to try to read a component of these blob transactions. And by going down this path, it makes it so that the consensus layer doesn't have to read these transactions and that the validations that have to happen occur on the execution layer regardless of the encoding. So it's a nice generic way to do it regardless as well. 

**Lightclient**
I also just want to be very wary of introducing changes that we think are intermediary. We don't really know when we'll be able to make the full change. We don't know what the full change is going to end up looking like. And I think we've seen in past forks where we try to do something that's forward compatible when it ends up not being as forward compatible as we want it to be. So that's kind of why I feel like if we're not going to go full SSZ and like find the right solution now, it's probably best to just stick with what we know, which is these RLP type transactions and continue thinking about how to do SSZ later. 

**Tim**
There's a question in the chat around like, why don't we think the like Etan’s doing SSZ well or 

**Lightclient**
Which one? 

**Tim**
Yeah, I don't know, Etan or Roberto, do either of you want to give context on that? 

**Etan**
I guess he's talking about 6493 for the signature scheme or 6404 overall. I'm not sure which one. 

**Lightclient**
Yeah, I think 6404 is definitely approaching, you know, what we want to do with SZ, but it doesn't really seem like there's appetite from the other developers to try and pursue this for Cancun. I generally think that that's what we want to be looking at doing for SSZ, but like what is in the proposal right now is not rare. And like specifically, I think taking the hash of a serialized SSZ value is not the idiomatic way of hashing SZ objects. And it just doesn't make any sense.

**Roberto**
So I was saying 6493, which I think is out of the 6404. 

**Lightclient**
Yeah, but it's just for the signature scheme. And so it really provides no value to users. The only value it provides is maybe not having to change the signature scheme in the future, which helps us avoid, you know, potentially breaking or making like hardware wallets change how they compute the signature hash of the transaction. So it doesn't give us any of the benefits that we are looking for in SSZ. 

**Etan**
One benefit that it gives you is right now, if you use this flat hash function that just takes the serialization and then hashes that one and you sign that, you don't get any benefits from SSZ for this transaction type. But if you use this idiomatic approach of the hash tree root, what you gain from it is that the hardware wallet can, for example, display certain fields, like you can send just a part of the transaction to the hardware wallet and it can verify that those parts are actually included in the hash that it is signing. That is not possible with the flat hash, for that you need the tree structure, right? 

**Lightclient**
Why would you not send the full transaction to the hardware wallet? 

**Etan**
If you are sending the full transaction, then why use SSZ for the transaction? 

**Lightclient**
That's what I'm saying. I don't think it really matters that much for the signature hash because for you to verify the signature hash is like what you expect. You need all the elements anyways. 

**Etan**
Can you send the full transaction? Isn't it like a big gig? 

**Lightclient**
I think that's how hardware wallets are implemented. Like if you just send the hash and you don't actually know what is behind the hash. 

**Etan**
No, I mean like the hash plus, multiple proof of individual fields in the transaction. So that you can, for example, check the destination, but you don't have to send all the blob contents. I'm not sure if that's useful or not, but it's possible with SSZ. 

**Danny**
The blobs not hash though. The blob is a KZG commit. So likely the transaction going into a hardware wallet would just be the field plus the KZG code not the whole problem. Okay, yeah. 

**Etan**
Now then it makes sense to just send the full thing. And I agree that, I mean it depends on the overall thing of this union thing or the normalized transaction, this bigger thing, right? But right now the 6404 has this conversion step where it just takes the main pool transaction using whatever format they are on and then it converts them to a normalised representation when it is building a new block, right? So for that EIP, it doesn't matter how it looks before. We could even add like ZK commitments to it as part of the conversion. But yeah. 

**Gajinder**
Also it was argued before that hardware wallets won't actually be doing SSZ block transactions because this is mostly we gonna use by L2 sequencers. 

**Lightclient**
I still think L2 sequencers probably would want some sort of hardware solution for Stein transactions even if it doesn't exist yet. 

**Danny**
Yeah, I agree.

**Lightclient**
And I think the code ends up being pretty similar whether it requires manual input like a ledger or if it's some sort of like, you know, other hardware like key mechanism where the key is just stored there and you're sending requests to it online. 

**Danny**
Yeah, I still want to make the case that going down the path of what Lightclient just does make this much more future compatible such that if and when the transaction type changes on the execution layer, the CL doesn't really have to know about that but just changes the validation of these version hashes that come in through the engine API. And if we're going to go that path, which I think is more generically future compatible, doing the least invasive thing on the execution layer would be my suggestion, which I think you can make a strong case that RLP is that, but potentially you can make the other case given that at least SSZ exists today in the test. 

**Etan**
Okay. I could share the link to this proposal on the CL side. Is it in the agenda? 

**Tim**
Yes, it's like basically a comment though. Let me, yeah, it's like the first comment on Hsiao Wei's PR basically and then Danny and basically if last century

**Danny**
We have to pull out the version hashes from the transactions which are otherwise opaque to the consensus layer. And so we were doing that by using all sets where this is the, if it's RLP, we would have to integrate an RLP library to do the recursive lookup. And then we have to make sure that those version hashes are actually the hashes and the commitments that we expect, instead we could make those version hashes an explicit component of the block. And when we pass them into the engine API, such the execution layer does the check that those version hashes are actually the ones that are inside of the transactions. And then we can do the higher level check in the consensus layer and not have to worry about the encoding of the otherwise opaque transactions. 

It sounds convoluted. It's moderately straightforward and prevents having to do any sort of like peering into the user transactions and the consensus layer. 

**Tim**
Andrew, is your hand newly? 

**Andrew**
Yeah, I'm just thinking loud here, like, would it be too much to just do 6404 in Cancun? Because it seems to me that it's the direction we want to go. So maybe we should just bite the bullet and implement proper SSZ with block transactions. 

**Tim**
Across all the transaction types, right?

**Andrew**
Maybe. 

**Lightclient**
6404 is changing all the transactions to SSZ and removing the Merkle tree root for the transactions and making an SSZ root. 

**Andrew**
What about legacy transactions? Because there was like plenty of hardware was like that will never change. 

**Lightclient**
It just changes the formatting that goes into the Merkle Particia tree. Is it goes into the SSZ root and the signature scheme, the signature hash, the legacy transaction stays the same. So the hardware wall still sign the legacy signature hash. 

**Andrew**
Right. I see. Oh, okay. So it seems to me it's the direction we want to go. Right?

**Andrew**
I think so. 

**Tim**
Alexey?

**Alexey**
Say it's kind of new idea, but probably it is possible to separate all transactions and new transactions. So we do not need to invent something new for all transactions to be to become a part of the Merkle Tree, instead we could have them separated and marked as deprecated. So we will have clean SSZ solution and a little p part which is a work is deprecated and then we will not allow these legacy transactions in the future, but after some time and we will not mix these parts somehow. 

**Andrew**
Well, a bad solution because hardware wallets like we cannot make them obsolete and so but I think the new EIP 6404, it just it takes it into account, it just introduces a backwards compatibility layer, which is nice. 

**Alexey**
But we will have a LP all the time to that. 

**Andrew**
That's not a problem. It's always the problem that we have different transaction route between CL and EL. I don't think that having RLP on the outside is a problem. 

**Lightclient**
Also having two list of transactions seems to complicate block production. You start to get to points where if you are a mev builder, you are trying to extract value from transactions that are at the end of the legacy transaction list and maybe you want to put your transaction at the beginning of the non-legacy list. It just doesn't really seem ideal to have two ordering mechanisms now. 

**Alexey**
Well you may have a order transaction list in block. We just can put one with them into root and another one in another root and it will be like two local orders but we will still have it as a global order. Aren't we? 

**Lightclient**
I'm not sure. Maybe we can have a global ordering still but we talked about this in Austin and it didn't seem like people wanted to have two transaction routes. Maybe I'm forgetting other reasons why. 

**Potuz**
Matt is the question to have two transaction routes, one for the block transactions and the other one for the legacy transactions? 

**Lightclient**
I think yeah basically but not just for block transactions for SSZ transactions which happened to only be block right now. 

**Potuz**
I was discussing this for a different reason which I would love if there's a discussion at some point. It's sort of a tangential to what is here but the point is that you would allow to have separate Mev PVS separations so that you can still propose a block built locally and use the builder for block production. I think this is something that we may want to have. 

**Alexey**
We can at least find some. Okay. Well, well we cannot deprecate right? It doesn't seem okay that we can have this legacy for the time maybe. Maybe we could at some point have a tree to fork all transactions. 

**Lightclient**
Yeah, I mean maybe like have a pre-compile that accepts the legacy transaction RLP and signature and instantiate transaction there. I think that's kind of been what it has been thought about for totally getting rid of these legacy transactions but then you start introducing a concept of sort of initiating a transaction with an EVM execution and there's just like things that haven't really been thought fully through yet. 

**Tim**
And I guess if we were to do like a full SSZ transition in Cancun these are all the things we need to figure out before that, correct? Especially if we're saying that the value we get from doing the full SSZ transaction now is like we don't have to change it again. Whereas right now with 4844 we just have a single transaction which might end up changing. 

**Lightclient**
Yeah, that's kind of what I would hope for in a quote unquote for SSZ transition. Does this not say that we have to solve this transaction in a bottle situation? I think that having the legacy signatures is generally okay. That's something that I don't think really comes into play as an issue until we start doing ZK-ing of all the transactions in the blog and you might not want to have any RLP but for today as long as they're represented as SSZ and the transaction route, that is the main thing we're looking for. 

I guess there's still questions about should we have separate transaction tree for the blog transaction so that you can produce things locally. I don't think that this is necessarily relied on SSZ. It's just like another arc to go down. 

**Tim**
I'm curious like do people feel like it is reasonable to potentially figure all that out for Cancun without basically massively delaying 4844, everything else? 

**Danny**
I feel like we had this conversation and we keep saying it would massively delay and there are a lot of uncertainties and it's like a can of worms that will likely take months. Potentially that is less than months now because people have been thinking about it for a while but I don't know. I do think that we keep asking the same question even though we presumably made a decision on
it. 

**Tim**
Right and I guess the point where it is now it seems like the alternative is we move to RLP on 4844. That's also a non-trivial amount of work but at least it seems like work that we have a really good understanding of. 

**Lightclient**
Yeah, I feel like we are at the point where we need to say we are going to go to RLP or say let's just sit down and be a little bit more serious and comb through 6404 and figure out what needs to be changed and what the exact world of SSZ transactions is going to look like. I don't think a lot of EL teams have gone through it deeply. 

**Tim**
Yeah, I guess I'm curious. I'd love to hear from other EL teams. Do you feel like it is something you have the bandwidth to go through deeply in the next, I don't know, two weeks to a month? I think if not then it probably makes sense to either keep what we have now, but that seems like the worst of all worlds or use the RLP scheme so that at least all the transactions are consistent?

**Marek**
We have capacity to go through it. 

**Tim**
Yeah. Anyone from Besu?

**Justin**
Yeah, it doesn't seem like too much of a challenge for us frankly.

**Tim**
Okay and so. I'm sorry, say again?

**Peter**
Which part isn't a particular challenge converting everything to SSZ?

**Justin**
I'm sorry, the RLP adoption.

**Peter**
Ok.
**Justin**
Let me rephrase. Taking the existing SSZ implementation as it exists today in 4844 and reverting it to RLP would not be terribly difficult for us.

**Tim**
Right, to be, yeah, to be clear, the question though was, do you have the bandwidth in like the next month or so to think about a wholesale move to SSZ? If we were to go down that road, I feel like we need to hash out the design in like, you know, the next month. And so, is that like realistic? 

**Justin**
I think a month is a little less realistic but six weeks to eight weeks is more realistic.

**Tim**
Yeah, Danny. 

**Danny**
Just to contextualize it's six to eight weeks, then it becomes implementation which then probably services additional details that weren't previously discovered and has at least a few testnets now, it's early a couple to kind of like go through those iterations. Just to, is it okay if that's the decision being made? I just want to contextualize that that's, that's, yeah.

**Justin**
So to elaborate.

**Danny**
It doesn't mean and then it's done.

**Justin**
Yeah. Right. So I'm actually considering two things going on here. One the actual research and, you know, thinking through that lightclient is suggesting but also our implementation of SSZ right now is very, very thin and very, very specific to a lot of the things that the CL has already adopted and there are a number of gaps there that need to be revisited and implemented. Things like, you know, new data types like optionals, the way that collections and lists are nested, et cetera. So there will be some upstream work that needs to happen on the libraries that we use for SSZ. 

**Roberto**
I thought we already had this discussion around whether we tried to do a more thorough SSZ because we're not really going to do that. 

**Tim**
So I, yeah, but I think, I guess my point is if, yeah, welcome talk or just, if we, if we are not willing to revisit that, then to me, that's like a pretty strong signal we should just do RLP and property take the time to revisit SSZ. It seems like the current spec is like the worst of both worlds. And I'm fine with that, but it seemed from the discussion five, 10 minutes ago that, yeah, others weren't. 

**Roberto**
I wouldn't call those current spec the worst of both worlds. I think the issue with, say we could get a 6493, we wanted that. I think the concern is that we miss something and we just have to introduce a new format anyway, and so all the work we put in SSZ might not be as valuable. 

**Lightclient**
I think the biggest concern is introducing a little bit of SSZ and then never being able to introduce the rest of it. And then forever on the EL, we have this one strange transaction format with strange signature scheme that's totally different than everything else. That to me is like the biggest concern. 

**Roberto**
I guess I don't see why introducing one SSZ type now would make it harder to get introduced to the SSE in future.

**Lightclient**
Oh, I think when it would make it harder, I'm just saying that there's always a large risk of doing any kind of change to the protocol. And I don't want to try and implement something with the expectation of changing it in the future.

**Tim**
Right. 

**Peter**
One example, the issue now, so in order to introduce SSZ, we need to introduce SSZ the signature scheme for the block transactions. And if we, and for example, we need to figure out the optionals and a few other stuff. If we miss something or some of this work will not be fully compatible with the work needed to basically switch everything out. And then for a sudden, we might need to swap out the SSZ signature of block transactions to once again. And then it's going to be super messy. I mean, yeah, everything's doable. But. Yeah.

**Tim**
Andrew?

**Andrew**
Yeah, I think the current spec. It's okayish. Because the signature, what we assign in block transactions, say, like how SSZ works that the first field is this chain ID, which will always be zero one, like one in the little engine form. So zero one and those zero bytes. So it doesn't clash with ROP. It's okay because of that popularity. I don't think that we need to even go in forward. I don't see a reason to introduce kind of any complications to sign in transactions because presumably all the SSZ transactions will start with the chain ID. So there will be no clash. But even if we do change that signature, it will be only for block transactions. Guess no hardware wallet. It's not a big deal. So I kind of think it's okay. 

**Tim**
I don't know. Anyone have. I guess. Yeah. Does anyone still think we should do the full SSZ investigation now? Yes. So there. 

**Alexey**
What is full SSZ? 

**Tim**
So basically, yeah, consider 6404 like, yeah. Yeah, consider 6404 for Cancun, which will probably be like a relatively big exploration. And likely will delay things a bit. So yeah, I guess I'm curious if anyone still thinks that's like the best path forward. It seems to me like no, but it's hard to gauge. And then if not, is it better to keep the spec as is even though it's a bit hacky in a way, or should we just do the work to get it the RLP so it's a bit more upfront work, but at least we have something that's kind of compatible or aligned with everything else on the EL right now. 

And it's, I guess it's also fine if we don't make that decision today, but it does feel like we're kind of bottlenecked on this for a lot of 4444 progress. So if we are going to decide to switch everything to RLP, I think it would be slightly better if we made that call today and people get an extra two weeks to work on it. But another option is as well like sort of fully speccing out what lightclient has in the comments and with the changes proposed by Danny, and maybe we can make a call on that on the on the CL call next week. And Potuz has a comment about this might be received differently on the CL call next week as well. 

**Lightclient**
All right, I don't think that was proposed though, right? Like we were talking about the comment that Danny and I mentioned.

**Danny**
So that so just to be clear, if we went down this path almost certainly the consensus layer would want to do this path where there's the additional data in the block that's passed into the execution layer payload as an additional validation rather than peeking into the opaque transactions. And that I think that's what you were saying, Tim, I just want to make that clear the consensus
layer.
**Marius**
So what you're saying is if we go to RLP route, there will be no RLP in the consensus layer. 

**Danny**
Oh, from a dot. 

**Tim**
Yes, it's what he was saying. Yes. Potuz?

**Potuz**
Yeah, but just Danny just went to talk to the doctor. But I had concerns about that comment too. I left it in the EIP. The latency of getting the blob, even though I'm not following the testnet and it hasn't been tested, I guess, at the level of mainnet, the latency of getting the blobs is much larger than the blob. And if we're going to have to wait for the for the full side card to validate us that common sense that we need to validate the KZG commitment against this extra field in the side car, before using the engine to send it to the EL, then that means that we're going to have the processing blocks much, much later. We currently can just send to the EL, the block as soon as it arrives, even if we don't have the blocks and we're going to lose that ability. It seems to me.

**Lightclient**
Yeah, I think the Danny said in the comment, I think Danny said in the comment that it would probably be in the block peer to peer object. And that's what I missed when I write a set side car, not realizing that you have this timing issue. 

**Potuz**
If you added the block, then my whole complaint is not a problem. So if you just add this extra field to the block, I think I'm fine with that. 

**Lightclient**
Okay. 

**Danny**
So we definitely have wanted to design a variant of that. The block can be executed without blobside cars. 

**Potuz**
Right. So then we're going to go back to this thing of being optimistic. Like later on with the side car appears, then we could just, so if the EL said that it's all right, and we process the thing, we still need to wait for the spool side car before putting in portraits. 

**Lightclient**
Yeah. 

**Danny**
But for any design, that's a very important design. 

**Potuz**
I mean, that's fine.

**Danny**
Yeah. And sorry for the misunderstanding when we were talking on this. 

**Tim**
Okay. So assuming that there's not massive opposition on the CL side to this proposal, if we modify it to put it in the block, I guess does it make sense to fully spec that out? And then in the next week, decide between either doing that and so using RLP on the EL, SSZ on the CL and having the hash as part of the block, it gets passed around. Or we keep the spec as is, but there's no world where we do sort of the full SSZ transition, right now, and we give people basically until the CL call to just review that, so that a week from now we have the decision. Or do people feel strongly enough that like we should make the decision on this now? 

**Roberto**
The sooner the decision the better. 

**Tim**
Ok.

**Roberto**
I don't feel strongly either way. I'm lightly in favor of what we have with SSZ, perhaps extended with the signing rapper from 6943. But I think it's more important just to commit. 

**Tim**
Yeah. Any of the client teams have a strong opinion on?

**Roberto**
I think we've heard strong opinions in favor of RLP as well. Yeah. I don't want to dismiss that. 

**Justin**
I think sooner rather than later is I'm also in agreement with Roberto. I feel 4844 devnet 6 looming. 

**Tim**
Okay. And Marius is showing strong support for RLP in the chat. I guess, yeah, considering this discussion sort of bubbled out of people not being too happy with the current spec, does anyone oppose if we make the decision to move to RLP now? And we can discuss the specifics of how the hash is sent on this CL call, but that we could start working on the EL clients with RLP support basically this week rather than waiting an extra week and potentially get them devnet 6 a bit quicker with this in. Yeah. 

**Marius**
I would not be able to. 

**Tim**
You would what? 

**Marius**
I would be in favor of that. 

**Tim**
Anyone not in favor of it? 

**Danny**
I'm going to go this path, we're going to add the field of the block to avoid the dependency creeping up in the consensus layer. 

**Tim**
Yeah. 

**Danny**
And so I'm okay with committing to that, but committing that with the additional field. 

**Tim**
Okay. Anyone opposed?

**Roberto**
Were there open concerns around adding it to the block? I just wanted to not try to fully understand the implications of that. 

**Danny**
I don't think so. I mean, it adds a list to the block that the execution layer makes sure that that list is in  accordance with the type 3 transactions, which is an additional validation, but it's an additional validation. 

**Tim**
Okay. Last chance for objections. Okay. So, yeah, let's do it then. Move 4844 to use RLP. Add the hash tree root to the blocks, not blobs on the CL and use this for DevNet 6. We can get some PR stood up for all of, sorry, version of the block, not the hash tree root my bad. Add that to the block, move the EL to RLP, not introducing RLP on the CL and use all of this for DevNet 6. Yeah. 
Lightclient, you'd already started some of these PR. So if you can kind of make your draft PR into a proper PR, that would be great. And if someone on the CL side can extend Hsiao Wei's PR, that would be good as well. 

**Lightclient**
So I can't quite make it a full PR until we get more people to review it, because once I make it a PR, because I'm an author, it'll auto merge. So I want to make sure that.

**Tim**
Okay, fair enough.

**Lightclient**
Like, it is a draft right now, but it's like ready for people to review.

**Tim**
Okay. Good to know. Cool. And whenever there's enough reviews, we'll merge it. Yeah. Yes, if possible, if people could review it in the next couple of days, and we can like discuss it on Mondays 4844 call, that would be great. Even if there's no objections by then, maybe we merge it. But if there are objections, at least we can discuss those on the call Monday. 

And Terence asked the question, is anyone working on the CL side? So Hsaio Wei is the one who opened the PR that lightclient commented on, but I don't know how final or like production quality that PR was. 

**Danny**
That PR is not, there's no one to go valid. Because that PR imports an RLP library to do the decoding rather than the version that we're talking about. It's very relatively simple. Certainly my self-reflow can handle it, we can chat about it. 

**Tim**
Okay, cool. Awesome. So, yeah, we're doing a RLP for 4844, and save ourselves another two plus week of discussions on this. So, nice. Anything else on this? 

###  [EIP-4844: Explicit Clarification on Block Validity with Blob Transactions using an Invalid Versioned Hash EIPs#7009]( https://github.com/ethereum/EIPs/issues/7009) [1:05:51](https://www.youtube.com/live/s6q5z53SICE?feature=share&t=3951) 

Okay, next up, Mario, you wanted to chat about an issue that you opened in the EIP. I did not have time to read it before the call. Unfortunately, do you want to give some context on it? 

**Mario**
Yeah, it's a principle issue. It's related to the bursting patches on the 4844. Basically there's a discrepancy between the interpretation of the implementations. So in the EIP, it mentions that the only reason to consider a block in ballot, block execution, is that the block bursting patches, I mean, the amount of blocks is zero. But some implementations are also checking the block commitment version of the block transactions. So basically what I would like to do here is just to add a clarification in the EIP because my understanding is that the execution can perceive and is valid even when we have an incorrect commitment version in any of the block transactions. But most of the implementations right now are rejecting these blocks. So yeah, basically it's just I would like to add a clarification of this in the EIP for us to get the correct version. I mean, to get the correct IVN tests, basically. 

And to add a little bit more context, I'm implementing the go-it-room current's implementation does not check the version, the byte of the commitment version. Nethermind does check this and either in the EIS does check this too, if I understand correctly. So the tests right now do not care about this byte on the execution client on the execution payloads. So yeah, basically that's about it.I don't know if anybody has the time to review the issue and we can just come to an agreement whether this is recorded or not, it will be great. 

**Tim**
Anyone have thoughts or comments? Actually, Gajinder and Alexey have a plus one and always requiring the version byte in the chat. 

**Marius**
So one thing that I like about requiring the version byte is that no one can update the version without also updating the client. And that means that updating the version byte would be a hard fork, which it should be. So I'm all for requiring. 

**Tim**
Cool. Anyone against requiring it? Okay. So I guess we can do that. Does this, I assume this requires us change to the spec? Like basically the 4844 and then we can write some tests for it? 

**Mario**
Yes, I can open up here just to make the small changes. That's okay. 

**Tim**
Awesome. Yeah. Great. Okay. 

**Mario**
Thanks. 

**Tim**
Sweet. Anything else on this? 

**Marius**
This might actually issue like one of the issues that we saw on the definite file. So my father most likely sent transactions that did not have the version byte correctly set. And so that's probably some of the breakage that we've seen. 

### KZG libraries [1:10:12]( https://www.youtube.com/live/s6q5z53SICE?feature=share&t=4212) 

**Tim**
Got it. Anything else? Okay. If not, okay. So this next one, Peter, I saw you posting about the KZG libraries a lot on the Discord in the past week or two. I just wanted to check in on that and see is there anything on the library side that like we should be doing or working on to make sure that they're in a good spot for us to use in production? If there's like nothing new or anything, nothing you want to bring up, we can go over it but I just wanted to make sure we have the chance to check it out. 

**Peter**
Yeah. So essentially with the KZG libraries, there are certain quirks that are kind of unexpected. The CKZG library specifically, the BLST sub-library of it has some interesting aspect. It has some optimizations baked in that require failed and modern CPUs and it will pretty much crash on an older CPU. Older CPU basically any CI server will crash. So not older by older CPU, I don't mean ancient CPU. I mean just not the newest and greatest. And the problem with them is that they have a built flag through which you can control whether to enable the optimization or disable it but the author refuses to implement runtime detection. It would probably trivial to do it but for whatever philosophical reason the author just doesn't want to do it. And this makes it particularly hard to integrate into other clients. 

I mean pretty much every concerned client had already issues with it as far as I know. And they had to, I mean even if you look at Lighthouse, they have a modern build and a portable build which is basically boils down to the CBLST library. So screwy details. Now the problem, the other annoying problem is that since you require an environment variable set during build time, it doesn't really play nice with using it as a dependency. And for example because in Go, the Go build system is very simple. You just type Go build. And what if you want to control the C library and make it portable, then you cannot do that with the default Go commands. You have to set an environment variable which means that anybody building GAF has to know about this lame environment variable and if they don't know about it, then there's a really high chance that their build will crash at some point. So this is one of the really annoying issues with the CKZG library. 

With the GOKZG library, again not the GOKZG software, the upstream, I don't know, one of the concerns with the libraries. It makes some strange optimizations. It does a lot of stuff concurrently and this concurrency cannot fully be controlled which is a bit of a strange decision for a Crip library because it's, I mean for example it can verify a blob concurrently on many threads and on default it will verify it on all your threads. And I mean for sure it's three times as faster verifying it on 20 threads but then the question is that feels a bit of a wonky tradeoff to be three times faster on 20 rather loads. 

And there's really no way to control this threading and I would much rather have a crypto library be single threaded and dumb and let me do concurrency by verifying multiple blobs on different threads rather than the crypto library internally deciding on what to do. I did look into it and it's a fairly ugly internal design decision so I guess again with some flags you could maybe have some modifications completely nuke it out somehow. It's a bit wonky. And so this were my two main concerns with the two crypto libraries on top of which the KZG stuff is built. 

Just for the record with geth what we did is we integrated both libraries both GOKZG and CKZG with default to GOKZG. And with regard to CKZG what happens is that if you build geth via make or the Docker images or our own internal build scripts or pretty much almost anything except the go the classical go build command then geth will add the flag to enable CKZG and also add the flag to make it portable. So that's the difference to any more power official builds will be will support both KZG GOKZG and CKZG, you can switch between them with a flag but anyone building geth via a simple go build or go install command will not have CKZG available. 

So that was kind of our best idea on how to solve it. And for us it was in all honesty we have a fairly low level of trust in both KZG libraries and the like of the libraries because it's kind of new and we have an equally low trust in ourselves to fix any issues if they happen. And that's why I want to be this approach of including both of them and making it suitable by a flag because for sure we prefer the go version but if there is let's say an issue a consensus issue between them then you want to be able to have users switch immediately without having to figure out okay how do we swap out the library how do we enable it how do we integrate it etc. So yeah that's kind of the TLDR of the KZG saga that we had on the geth side.

**Tim**
Thanks for sharing. I noticed there was a couple of comments in the chat during this but anyone have thoughts or anything we'd like to add there. 

**Alexey**
Yeah we can solve it by runtime selection of the library but it could be better if for the library could support runtime flag instead. So we need to know whether we need to invest in this additional build and time check or I'll go to wait for a solution in the BLST. 

**Tim**
Potuz? 

**Potuz**
Yeah I was one of the ones that complained about runtime selection on BLST the problem is the way this is coded is not that you have one routine that uses ADX and mulex and another routine that doesn't. There are just bits and pieces that are added or not by preprocessor instructions so I think the only feasible way of changing this without big changes within the library is what the people of Nimbus were going to do which is just disassembling with the flag disassembly without the flag have the full binary ones and just choose at the beginning, so have a much larger library with two copies of the full routines with one flag and the other flag and then choose some runtime, that would be their fork and I don't see any other easy way of doing this change making this change in BLST so I don't expect the author to actually accept a change towards this anytime soon. 

This is really annoying this is something that really annoys me because it's something that the Ethereum Foundation paid for this library and every single client complained before the launch of the beacon chain and this was unsolved and now that the execution clients are also complaining that it's getting some traction again. So this is something that is incredibly annoying on the CL side at the point that Prism is shipping this binary by default which is portable because we did see some crashes a lot of validators are being run on AWS currently and they do crash because they run some old ZNC builds. 

The other comment I wanted to make which is something that makes me uncomfortable with the status of the crypto libraries is that they are still changing quite a bit and in things that are kind of non-trivial on CKZG, I saw Marius that was complaining about the way of loading the trusted setup and on the GOKCC side it's something similar like the version that we were trying did not accept the trusted setup that is posted already in the consensus layer spec repo and the change that fixed this is not long ago which means that if you update the crypto library to use that change then you need to update geth and geth hasnt updated to this so it's becoming very problematic with all of the relations of the different clients with the crypto libraries to even start testing this. 

So I think it's we're still at a prototyping stage I would say that we're very far away from developing production code in that area. 

**Tim**
Thanks, Solius was your hand up about this as well? 

**Saulius**
Yes, so a few notes on this extension thing where you need to compile the thing with basically the either for new CPU side of all the CPU's I think we also discussed internally and interestingly approach but it's probably similar with a Nimbus one where we just in the runtime we essentially compiled both versions of the BLC library with enabled extension and the disabled extension and then on the runtime we check what CPU is running and if it's a new CPU we use one version and I mean bit enabled extension and if it's not running and if it's running with old CPU then we are taking the old library I think this is a good approach but at least you would not need to have a separate build of your clients. So but this is probably similar with what Nimbus was thinking isn't it? The approach that for Potuz was talking before. 

Anyway, so this is one question. Another question on the parallelized version where we make verification faster but the problem actually is not about using a lot of cores because if it's available you know then why not to use it but the problem is that if it starts to compete with something else that client is doing something else important that client is doing so my question is for original person who raised this question, like how do you deal with this elsewhere? You should have some hard computation that you already parallelized and how do you prioritize it? 

And like if you could tell some examples of that that would help to make a solution that you know some open some built-in solution in the crypto library that helps essentially that solves this competing problem. One way of thinking about is just to lower the thread priority essentially, so the OS operating system scheduler will just make it less competing with other things that client is doing. So I mean if you could tell how do you solve that currently because you talked about that you don't have control in this approach with crypto library but if you had control how do you do that? 

**Peter**
Well I think one of the problems is that this is not solvable at the crypto library level specifically because for example if I'm doing a block processing then I don't want it to be a lower priority then for example if a new block arrived I want it to actually have the highest priority during processing now. If on the other hand the blob is being verified in the transaction pool then for example I would like to have it a lower priority. So these are and this is something that from the library from within you cannot really guess which blob is important now and which blob is not important. 

**Saulius**
So yeah I think a pretty easy approach would be I mean not ideal but something that would be easy to achieve is just to set the thread priority whenever you call the verification function. So if you need that as fast as possible then you say that the crypto library should spin threads for this particular verification with normal or high priority and otherwise if that's not important you just say crypto library that is not important verification and it just spins threads with lower priority so it doesn't compete with things that with everything else that runs on the default priority at your client. I guess this makes sense?

**Peter**
Yeah sure it doesn make sense but. 

**Saulius**
I mean there is no easy solution for that but there are some solutions that probably should work most of the time and the one I just described it could be the solution for this problem. 

**Guillaume**
So just to make sure I understood you want to have a specific scheduling thread scheduling policy for every use case and it will have because it's dependent on what OS you're running on you will have to have an OS like specific library for every platform you want to support basically. 

**Saulius**
I mean we checked on the like a free mean platforms which is like Linux, Windows and the OS X and usually there is a way for these three operating systems there is a way to change the priority of the thread. So disparate much is enough to implement this idea. Maybe for other platforms which we were not interested in maybe it's even not possible to change the priority so then yeah this doesn't work on those platforms. 

**Peter**
So I don't think that will work for example in Go because Go doesn't have real threads. Go uses very few real threads and the multiplex is all the go routines on top and I don't think you will have a way to lower the priority of a thread of a go routine. 

**Saulius**
But if you so I don't know actually how it works. Like if that's only go environment then yes but if that's something external you know something like if you call CKGDR or RAVSKG from Go then it definitely should be able to
use system threads because it's like you know C extension or something  outside of the Go thing. 

**Peter**
That would be super expensive because spinning up threads is at least on Windows sorry on Linux it's a bit faster spinning up threads but for example on Windows it is extremely slow on your draft milliseconds. So if your crypto library will spend 10 milliseconds or 50 milliseconds spinning up threads to do the half millisecond work then that doesn't really fly. So essentially these are kind of also the social highlight issues that once the crypto library is a very very low level stuff and it tries to do threading which is a very very high level stuff and then you hit all these kind of strange issues with how to solve. So it just feels that the crypto is not touch threading. 

**Tim**
So we're... 

**Saulius**
Well I think just last note I think we just ruined it. Do we need like a top performance or think and go on a single thread and everyone is happy with that. 

**Dankrad**
So I mean I just want to chime in here I've been trying to get in for a while but I think the only thing where threading even makes sense is for blob construction and I think we're getting way ahead ourselves by trying to optimize this must. I think it's perfectly fine right now to just completely ignore this because the kind of roll-ups who are going to do blob construction it's still...First it's not a lot of time it's still talking tens of milliseconds here and second like they can start optimizing that they don't even have to use a standard build for that. So I feel like trying to optimize this now is just like I would just say like we don't need threading at the moment and can just ignore it and maybe can have it somewhere in the code and they can have a special build or something. 

**Saulius**
And do we have like is there a decision? But it takes a lot to finality how much of blobs there will be in block on the main. I mean is it like four or sixteen? 

**Dankrad**
What does that have to do with it? Well like on CL side for verification. 

**Dankrad**
Why do we need parallelism? Like this is like we're talking about like a few milliseconds. 

**Saulius**
Well but you know there are few things. There are slow computers like slow nodes where every millisecond just multiplies by the slowness of the computer. This is one thing and there are some use cases where log verification is important like every millisecond is important like in any or whatever else domain. So I actually don't agree that you can just ignore the fact that those milliseconds are up together. And if you have a sixteen.

**Dankrad**
I mean this is on CL right? It can be done in parallel to execution layer verification anyway. So how much does that actually add? 

**Saulius**
Sorry can you repeat that?

**Dankrad**
This is in parallel to execution layer like this is a CL. So it would be in parallel to what execution layer does anyway. So does it actually do block verification any faster if you parallelize this CL? 

**Saulius**
Sure and why it shouldn't be faster if it's

**Dankrad**
Because I would assume that yeah yeah let's just a bottleneck anyway. So if you add a few milliseconds. Oh yes okay. 

**Saulius**
So you're saying okay so your point is that CL will always be significantly faster than EL so it doesn't matter if it's lower on the CL side. 

**Dankrad**
I mean this would be my guess right now. Again I also feel that getting ahead of ourselves optimizing this for someone who's doing MEV interaction like. Okay so I mean I'm still with my opinion that we should do as fast as possible but yeah I get your point that if EL is much slower than CL then technically we shouldn't have the problem here because you know CL will be able to complete even on a single thread notification because EL is taking much more time. 

**Dankrad**
Also like I mean the CL can parallelize other tasks in parallel to this so like I would assume that signature verification is much more work but you can easily like the CL can simply like thread this the blob verification the signature verification again. It just feels like absolutely optimizing the blob verification to like 16 threads just seems crazy to me. Like I mean I don't know like that seems like an insane premature optimization that's like just makes things more complicated. 

**Salius**
Well I think the key thing on CL is that the blobs will come asynchronously not at once you know so naturally I mean naturally like the proper implementation is just to do verification whenever you get the blob immediately. 

**Dankrad**
So that would be an even stronger reason not to parallelize it. No I think if we have a lot of questions. So why are we discussing this? It's just because it's just right. 

**Tim**
So I guess yeah but 

**Saulius**
that was a bit of a topic to the original questionnaire for the original person. So we're already like five minutes over time. I don't know I know there's a telegram channel discussing the libraries, is that the best place to just actually the telegram channel is like for CKZG but is there somewhere that we should continue this conversation? I mean we can use the like we have a bunch of 4844 channels so we can use those. Yeah. I don't know if there's any final comments before we move this offline?

Okay yeah so let's continue. Do you mean, Alexey, like I do you mean SSZ chat or KZG chat? 

**Alexey**
No no it's basically not. 

**Tim**
We have a transaction type channel which I think we can probably reuse for that. Yeah we have a transacton type transaction channel which we used for that in the past. So you can just keep using that. 

# Other EIPs: [1:37:09]( https://www.youtube.com/live/s6q5z53SICE?feature=share&t=5829) 

## [Contract Secured Revenue on an EVM based L2]( https://github.com/ethereum/EIPs/pull/6969) 

## L2 EIPs/standards on ACD?

## EIP-5656

Yeah. Okay so we're already a bit over time. I know we had Zak and Charles who wanted to like give a bit of context on their EIPs. We can take you know two-ish minutes on each of them if folks can stick around. If either of you Zak or Charles prefer to do this on the other call on the next call would a bit more time we can do that as well. But if not Zak do you want to go first and give some context? 

**Zak**
Hey yeah hey Zak cool coming at you live. We'll have to yield. Just coming to discuss the 8669 and I guess out of respect for time. I'll be bumped to the next call. But is this the best forum to discuss it assuming that this EIP target specifically L2 implementation? With that in mind there's a caveat that it does involve additional state transitions and may have implications on supply as well. Since it's a modification of the 1559. 

**Tim**
So yeah we haven't, Dano had some comment about this on the chat but like L2s can do things without all core devs, you know permission or authority or away. If people have like technical feedback on the EIP it probably makes sense to share it and I know there's already a bit on ETH magicians. Yeah anyone else have thoughts on either the EIP or whether we should even be discussing
that now? 

**Danno**
So to add on to that about the jurisdiction I mean if we say something and the L2s ignore us there's like no side effect versus if something for me and that something to decide on is call and say get the sides not to do it or you know the Nethermind decides not to do it well they're out of sync with mainnet. So there's a bit of jurisdiction because we define what's standard but L2s can do what they want. I mean I mean it sure you know so that's that's my concern is that there's no stick just carrot. 
**Tim**
I think maybe one difference is and this is maybe not the best EIP for this but you could imagine L2s wanting to do something before mainnet and wanting like some sort of sanity check of like you know if this goes well on an L2 does L1 want to do this. So that might be a case where I give a sense to get the feedback or do you write it in later.

**Danno**
And I do see that this EIP might have that along other ones like 4337 and maybe in the future EVM changes so that is a question we need to resolve you know beyond just this EIP. 

**Tim**
William do you have your hand up is all? 

**William**
Yeah I wanted to add a  point somewhere to the one you just made Tim so I mean full disclosure I work at Polygon. A lot of times there's a certain level of coordination that I feel ACDE should be open to though I mean there's an opinion definitely open to debate. I understand your point Danno and I think that it does like there needs to be some kind of resolution to that but looking at an EIP like 3074 or other ones that involve actual EVM state changes, I think that there's a lot of value in a certain level of coordination effort going through ACDE even if it's not necessarily going to land on Ethereum's EVM right now. 

It is the best rallying point around EVM engineering and like Tim mentioned also just being able to get some level of sanity check that things potentially make sense or also to be able to send signal I think is valuable. I think there's also a value to that for Ethereum itself which is that L2s have much more of a potential of all the ones for experimenting with things that Ethereum probably should not be  experimenting with but if our successful on L2s can kind of trickle back up to Ethereum. So I think also kind of in that cycle there's at least some value there but that's just my side of things. 

**Tim**
Thanks for sharing. Ansgar’s last comment on this and then we'll move on to Charles. 

**Charles**
Yeah I just wanted to bear with you say because I talked to some people about tonight's in the past and I do think it makes sense to have some sort of coordination between all EVM chains including L2s. I'm not so sure that at least in the long run ACDE would be a good forum because we can never actually promise to bring things on Mainnet right it could always be that even if we think we might do it then we decide not to do it and so then I think in the long run it makes sense to have these kind of processes be separate although I wouldn't be necessarily opposed to like use ACDE in some form for like bootstrapping a process like that once there's sufficient interest but yeah. But this should continue this discussion. 

**Tim**
Yeah. And so I guess for the specific IP we can use ETH magicians and for this like meta discussion I agree this is probably something we need to figure out. I'm not quite sure what's the best way to have the conversation but it's been on my mind as well. I would definitely want to avoid a new permanent call if we can for as long as possible. Yeah but let's see. 

**Zak**
One more. 

**Tim**
Yeah please Zak. 

**Zak**
I'm sorry. Just one more thing. Is there any way that we could just get this EIP merged so we can alleviate any bottlenecks from the active working group? No, sorry that's not the best place to ask. 

**Tim**
So I don't know if it's an issue with the numbering. I think it's probably easier to resolve those on GitHub or Discord and not open that can of worms here. 

**Zak**
Yes. Sounds fair. Thank you. Yeah. 

**Tim**
Sorry for the delay and sort of jamming this right at the end. Okay. No problem. Charles. 

**Charles**
Hey I know we're really over time now. I wanted to bring up again, copy and secondarily K which we brought up last time. And I think at the time Tim said that to give everybody a bit of time to review it and I was wondering, I'm happy to punt to next week but I'll keep asking if we can include at least mcopy and also pay in Cancun. 

**Tim**
So I guess we definitely shouldn't be making this decision 15 minutes over time. It seems so there was some like support for mcopy last time. Seems like there is in the chat still. Maybe and then payoff code is a bit more controversial it seems. Maybe what we can do is like put mcopy on the agenda for and we can put payoff well. Like put it on the agenda to make a decision about on the next call. So like two weeks from now we have an idea and generally as well try to figure out that there's other smaller EIPs that people want to see in because I know like 4788 or the BLS precompiles were also kind of wanted. 

So if client teams can have like an idea of which small EIPs are important and would want to be included in Cancun by the next call we can have a conversation. 

**Charles**
Okay, great. I do want to point out that EVM1 did merge support for mcopy. I think they're also working on state tests and there is also an open for request on Geth for mcopy. Nice. I think Gumbo and like have already reviewed but if one of the maintainers wants to at least not necessarily do a full review but at least take a look at it. They can get an idea of how nice mcopy is and how useful it is and it's not too hard. So I think that might help a little bit. 

**Tim**
Awesome. 

**Charles**
Anyway, yeah, yeah we can continue next call.

**Tim**
Cool. I think this is a good spot to add. We're already 15 minutes over. The same final anyone wants to bring up before we wrap up. Okay. Well, thanks everyone. Talk to you all on the CL call next week. Thank you. Sorry.


## Attendees

* Tim Beiko
* Danny
* Andrew Forman
* Alexey
* Mikhail Khalinin
* Saulius Grigaitis
* Guillaume
* Mario Vega
* Marek Moraczynski
* Ken NG
* Pooja Ranjan
* Marius Van Der Wijden
* Danno FErrin
* Roberto B
* Lukasz Rozmej
* Yoavw
* Zak Cole
* Justin Traglia
* Mario Havel
* Fabio Di Fabio
* Dan (Danceratopz)
* Kamil Chodola
* Charles C
* Etan (Nimbus)
* Alexey
* William Schwab
* Andrew Ashikhmin
* Phil Ngo
* Georgios Konstantop
* Lightclient
* Joshua Rudolf
* Terence
* Ansgar Dietrichs
* Ben Adams
* Pawel Bylica
* Spencer
* Daniel Lehrner
* Mehdi Aouadi
* Gajinder
* Carlbeek
* Stefan Bratanov
* Dankrad Feist
* Kasey
* Justin Florentine
-* Crypdough.eth
* Roman Krasiuk
* Peter Szilagyi
* Matthew Keil
* Nazar Hussain

