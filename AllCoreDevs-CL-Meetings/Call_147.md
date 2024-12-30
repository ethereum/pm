# Consensus Layer Call 147

### Meeting Date/Time: Thursday 2024/12/12 at 14:00 UTC
### Meeting Duration: 1.5 hour
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1211) 
### [Audio/Video of the meeting](https://youtu.be/VpYzaCzEVe8) 
### Moderator: Stokes
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
147.1  |**Mekong** Mekong, the public Pectra devnet based on Pectra Devnet 4 specifications, is stable and there were no new updates reported about the network’s health. Stokes mentioned that the testnet recently underwent a block gas limit increase from 30m to 36m gas and no network disruptions have been reported since.
147.2  |**Pectra Devnet 5** Developers are still finalizing specifications for the launch of a new Pectra devnet, Devnet 5. Stokes confirmed a minor renaming to the “PendingPartialWithdrawal.index” field in the consensus specifications so that the naming convention is aligned with other fields related to validator withdrawals. Then, Stokes raised a proposal by Erigon developer Giulio Rebuffo to increase the “GOSSIP_MAX_SIZE” value in consensus specifications from 10 to 15 mebibyte (MiB). This would allow validators to safely increase the block gas limit on the EL from 30m to 60m gas.
147.3  |**Pectra Devnet 5** EF DevOps Engineer Barnabas Busa said that any change to the gossip limit should be done at a hard fork to ensure consistency across all clients. Otherwise, there could be issues with consensus failures if clients had different values. Besu developer Paul Harris noted that to some extent the variation among clients is “already happening” and what is needed now is consistency moving forward on a plan regarding the gossip limit. EF Researcher Dankrad Feist stressed the urgency of the situation, calling the discrepancy in the gossip limit across clients “a bug”. He said, “I think that we need to make sure that there are no consensus failures due to this limit. This should just be treated as a bug, and we should fix that right now and then independently we can raise that limit. There should be no case where raising the gas limit leads to a consensus failure.”
147.4  |**Pectra Devnet 5** Stokes noted that changes to gas costs in Pectra like EIP 7623, which increases calldata costs and limits the maximum size of an EL block, will alleviate gossip limit issues. However, until Pectra is activated on mainnet, aggressive increases to the block gas limit, such as a doubling, could cause networking issues on Ethereum. As background, changes to the block gas limit are controlled by validator node operators and in recent weeks, prominent Ethereum community figureheads have called for a doubling to the block gas limit.Busa proposed in the Zoom chat removing the ability for validators to change the block gas limit. Another solution raised on the call was to update the gossip limit such that it is a function of the gas limit to prevent cases where increases to the gas limit on the EL cannot be supported by the gossip limit on the CL.
147.5  |**Pectra Devnet 5** There was a lack of consensus among developers about what to do and concerns that the implementation of any long-term solution would require deep changes in both EL and CL clients, which could further delay Pectra. So, Stokes recommended that CL clients stick with conforming to current specifications for the gossip limit at 10MiB. “First off, CLs should double-check that they follow the spec as written today, correctly, if not definitely, they need to send out updates. That one's straightforward. Then, it sounds like what we want to do is take a little more time to think about what the nice solution here is with respect to the gossip limit and the gas limit,” said Stokes.
147.6  |**EIP 7742** Developers agreed to remove EIP 7742, uncouple blob count between CL and EL, from Pectra and instead implement a doubling to the blob count in Pectra through a change to the genesis configuration in clients. EIP 7742 would have required that the blob target and max values be dynamically sent from the CL to the EL through the Engine API. Upon closer inspection of this EIP, developers have noticed a few complications in implementation. One includes the fact that the EIP currently only uses the target blob count of the current block when in fact the target blob count of the parent block is needed for the excess blob gas computation. Other changes to the EIP needed are listed in more detail on this GitHub page.
147.7  |**EIP 7742** Rather than deal with the implementation complexity of EIP 7742 and delay Pectra further, most developers on the call were in favor of removing the EIP and instead changing the genesis configuration. This would mean that blob count values can be updated in Pectra but that future changes to blob count still require updates to both the CL and EL.EF Researcher Dankrad Feist was the only person on the call who strongly argued against this decision. Regarding blob count values, he said, “I think it's crazy to have this in both clients and keep this as something that has to be kept in sync between the two. To me, that's tech debt, and we should eliminate it.”
147.8  |**EIP 7742** Geth developer “Lightclient” pushed back on Feist’s comments, arguing that the dependencies between the EL and CL go much deeper than considerations about the blob count. “I just don't think these things are in pure isolation, like bumping this constant on the CL for the gossip max size. This is not something that you could just mindlessly do, just as you can't mindlessly increase the blob limit with respect to the transaction pool on the execution layer. So, I think the conversation is just always going to have to go both ways. There's always going to be a discussion about the safety of doing these things. Has the other side implemented the necessary protections to deal with this higher load?” said Lightclient.
147.9  |**EIP 7251** There were a few updates to the design of EIP 7251, increasing the maximum effective balance, shared on the call. The first addresses an edge case where a validator node operator could trigger consolidations for validators it does not control. Stokes reiterated that the changes to prevent this edge case from happening will be finalized over the next few days and feedback on it should be shared post haste asynchronously from the call.The second update to EIP 7251 fixes an oversight in the validator selection process for signing block headers and proposing blocks. Stokes called in a “more invasive” change than the first one and recommended that CL client teams review it as the intention is to include it in Pectra Devnet 5 specifications.
147.10  |**EIP 7762** EF Researcher Ansgar Dietrichs highlighted a few takeaways from the latest RollCall meeting, a meeting series organized by the Ethereum Foundation to encourage coordination and communication between EVM-like Layer-2s. One of the takeaways was that EIP 7762, increasing the minimum blob base fee, should indeed be left out of the Pectra upgrade, as decided last week on ACDE #201. About EIP 7762, Dietrichs said, “On RollCall, we talked about it, and it seems like basically, rollups have been able to work around this for now. So actually, it is lower urgency than I had [thought]. So, with that feedback in mind, and given that, we said last week to only include it if really there was a strong case for it, it seems to me like that the best thing to do here is to just go ahead without it for Pectra.”
147.11  |**EIP 2537** The repricing model for EIP 2537, BLS precompiles, is nearing completion. Nethermind developer Marek Moraczyński presented 3 GitHub pull requests with the latest numbers. He noted there is still some discussion on the gas pricing for MSM operations but that the final benchmarking for these operations would be completed by next week’s ACD call.
147.12  |**PeerDAS** Stokes highlighted a pull request (PR) from EF Researcher Justin Traglia to rename EIP 7549, PeerDAS, specifications as “Fulu” specifications. Fulu is the name of the next CL upgrade after Electra. The renaming of EIP 7549 to Fulu further solidifies developers’ intention to ship PeerDAS in the next upgrade after Pectra. Stokes said that the PR from Traglia would be merged if there were no objections from client teams.
147.13  |**EIP 7723** EF Protocol Support Lead Tim Beiko shared a proposal to update EIP 7723. This EIP is not a change to the core protocol of Ethereum. It is a document that provides an overview of the various stages that an EIP impacting the Ethereum protocol must go through before their activation in a network-wide upgrade. Beiko recommended that EIPs labeled as “Considered for Inclusion” or CFI should be considered as EIPs that developers plan on including in a devnet, any future devnet, for an upgrade. Secondly, EIPs labeled as “Scheduled for Inclusion” or SFI should be considered as EIPs that developers plan on including in the next immediate devnet for an upgrade. “The rationale here is that this could help us sort of throttle how many things we bring in at once [on a devnet],” said Beiko, adding, “So, if we say we're putting 10 things to SFI, we should be saying in the next devnet we want to implement those 10 things, and if we think that's too much, then we have to pick which subset do we actually want to put in the next devnet?


# Intro
**Stokes**
* Okay. Great. Hi, everyone. this is consensus layer. Call 147, and let's see, there's the agenda in the chat. It's PM issue 1211. And yeah, we have a pretty big agenda today. hopefully we can get to some sort of closure on Pectra. And, yeah, let's go ahead and dive in.
* So, first we could just have, like, a quick update or check in with any devnets we have going on. we have Mekong, and then otherwise, today we'll talk about F5. So I'm not sure if there's much else to discuss there, but I'll open it up. Are there any updates? We should discuss any bugs or issues we should talk about. 

**Barnabas**
* Mekhong is very stable, so there's no update on Mekong side. 

**Stokes**
* Okay, great. I guess one thing you did go to 36 million gas, right? 

**Barnabas**
* Yes. 

**Stokes**
* Cool. And yeah, so it's been stable. So that's good to see. Cool. Okay, then. Yeah, let's get into it.  pectra-devnet-5. So, there's a spec, and. Yeah, today there's a number of things, essentially finalizing that spec so we can move forward with the devnet and. Yeah. Okay, so the first one here

# FYI: Rename PartialPendingWithdrawal field index to validator_index consensus-specs#4043 [4:39](https://youtu.be/VpYzaCzEVe8?t=280)
**Stokes**
* This is kind of an FYI.  there was a PR to rename a field, in the pending partial withdrawal, and it's been merged. It was just simply changing the name of one of the fields. So, yeah, it's kind of a heads up, that's there. And we'll be in the next release. And yeah, from here there's like a number of things to discuss. people wanted some time to engage with this question around changing the gossip limits. let me grab this PR as kind of a concrete thing to ground the conversation.
* And yeah. So this PR, proposed was raising the gossip limit and the sort of in the spec that we have from ten megabytes where it is today to 15. And this came up, sort of via investigation into raising the gas limit on mainnet. And, yeah, it's 30 million today. There's even been calls from the community to raise up to 60 million over, like, a pretty short timeline. One thing that we consider doing here is changing this gossip limit.  yeah.
* I don't know if anyone wants to add any more context or otherwise. we can discuss if we want to include this change for Pectra, if not sooner. 

**Barnabas**
* I would ideally like to see this gossip limit change at a fork instead of just change a value. So maybe gossip max size with Electra. If we end up bumping it. 

**Stokes**
* Right. Because I think otherwise it would be weird if some nodes had different limits and there was a block that triggered it. 

**Barnabas**
* Exactly. 

**Stokes**
* Yeah. Okay, to be. 

**Paul**
* Fair, we're kind of getting into that situation where that might happen anyway because,  some clients are talking about changing the uncompressed limit on blocks, and that would cause a similar scenario to changing it at any time in the clients. So I think whatever we do, do we need to be consistent across all of the CL? 

**Stokes**
* Yeah. They're good. 

**Dankrad**
* Right. Yeah. I mean, I agree, I think like, we need to make sure that there's no like consensus failures due to this limit. And I think like, I feel like that should just be treated as a bug, that it is the case right now and we should fix that, like right now and then independently we can raise that limit. But there should be no case where like raising the gas limit leads to a consensus failure. Or like an ineffective consensus failure. Yeah. 

**Stokes**
* Right. Yeah. Do you have your hand up? 

**atd**
* Yeah.  so I've taken a little bit of a look at,  what the implications are of this limit. 
* So basically we're talking about a limit of the gossip message size when it's uncompressed like the payload is uncompressed.  and the payload is of course the block itself,  using the SSE encoding and in the SSE encoding,  all of the fields are actually,  constant sized, or rather, they have a constant upper bound,  except for the transactions.
* And the way we encode the transactions is simply a byte list of nearly infinite size.  so this kind of simplifies the problem a little bit, at least because it means that let's say that we have, you know, ten megabytes is the maximum gossip size and the maximum transaction list size can easily be derived from there, and it's roughly 300 K lower than those ten megabytes. So we could say that,  we have, you know, 9.7MB of space available for transactions. And this is the only thing that determines whether or not this limit gets hit.
* So,  in this way, we can actually reduce this, problem into a, you know, an upper bound on the transaction size that an execution client can possibly create, which is good news, I guess, because it then at least we can also explore other kinds of options where,  well, the two that come to mind is that either we compute a maximum possible gossip size.  from the gas limit with a little bit of spare room to handle it and the gas limit going up and down.  and we can do this solely based on this transaction field or, consensus layer.
* Clients can actually inform the execution layer that you have this, this much space available for transactions. if you wish.  and then, the the other nice thing about the transaction field being the determinant. 
* Entirely. in general. And it is encoded using, you know, LP or whatever it is that, they declare. But but it's nothing that the consensus layer has to care about. They don't have to know about the encodings and so on. And conversely, by, by giving this limit this way, the execution layer doesn't have to know anything about the gossip layer either. So I feel like, going forward, like, retrospective about now, there are a couple of fairly straightforward ways of addressing this problem, properly,  regarding an increase,  I think that this is our one of the few mechanisms that we have to protect against spam, against amplification attacks.
* And it's fairly blunt. the smaller it is, the better, as is, a five megabyte increase there can give an attacker like 13GB of traffic.  if you compute the full amplification. And the reason for this is that we validate the execution, Component of the block way later than we do gossip propagation. And the final thing I wanted to say on this topic is that I have a PR up that also fixes the ambiguity,  in spec. The spec is a little bit poorly worded, so there has been a little bit of confusion of compressed versus uncompressed. but  kind of summary of that PR is that we do want to target the compress the uncompressed size with the limit for, for a lot of reasons.
* One is because it's easy to reason about, it's easy to derive a transaction limit from it and so on. And it also protects against snappy decompression bombs, which is good.  and then from that limit, we can actually compute the maximum allowable compressed size as well. **atd**
* And this is based on the fact that snappy has an upper bound on how much, how much data can expand when you try to compress it. And this is, about 10% more than I think it's like 13 or 14% more than the incoming data size. So we can put a bound on the, compressed message by deriving it from the uncompressed maximum size. And this is also good news. And there's a PR coming up for this. Yeah. Soon. 

**Stokes**
* Okay. Thanks. Yeah, that's that's helpful to know. your connection was a little garbled, but essentially, yeah, it sounds like, you're open to raising this limit or at least thinking about it more intelligently.  then the question is. Yeah, on what timelines do we do? What? There is a number of comments in the chat around. Yeah, how we do this.  the catch here is that like the only real guarantee we have that all nodes have a certain profile. Is that a hard fork? then the question is like, yeah, let's say we want to change this ASAP. how would client teams thinking?
* How would client teams think about, you know, pushing this to their users and actually making this happen? Like, for example, there was a comment, I think, from Preston, just to put minimum versions on this pump, the gas website. Do we feel like that's like a sufficient directive? 

**Preston**
* I can add to that. I think that it's, you know, wherever we're pushing the message of, you know, hey, if 40 million is okay or, you know, even 60 million is okay, you say, as long as you're looking at this because there's a known issue, my support for releasing as soon as possible, this change is that the gas limit will change outside of the hard fork. And we know there's a problem and we can fix it, so why not fix it now? It doesn't seem that, controversial to me.  yeah. Some validators don't update often, but, you know, they're missing out on other bugs that happen on a regular basis anyway. So, you know, they should be updating frequently I think, as well. 

**Stokes**
* Right. yeah. I mean, it does seem like it's a little bit split, like one option is to go ahead and try to get this updated as soon as possible. would anyone be against that? And yeah, there's another comment that made a good point. Like with Petra, this should all be resolved. 7623 here helps quite a bit. Then the question is just like between now and then, how do we want to handle this?  what we probably don't want is to have different clients do different things in the meantime. So ideally we could agree to do the same thing, whether that's no change today or that's, push for some raise, as quickly as possible. Yeah. 

**atd**
* Yeah. So I'm kind of against upgrading on principle.  I think that we still have a little bit of time to reason about this problem. It seems that the response from the community about not going into a gas limit situation that exceeds these bounds has been fairly positive so far. and like this would effectively mean that we're changing the rules of the protocol outside of a hard fork, which is a new kind of expectation that we have on the community. Like, normally we should expect that unless there's like a die hard bug,  we should expect, in fact, that users should not have to update their clients between, you know, hard forks, as it were. but if we are going to do this, we should certainly do it all together.
* And we should certainly also. update the config because there exists the possibility for users to simply override their local config and use whatever version they already have. And then we should put out that recommendation as well. I think the risk here is, is indeed the upgraded nodes. because what happens with unupgraded nodes is that we effectively create a split in the network, right? A network based split instead of a consensus based split. But at the end of the day,  those nodes that have an old version are still capable of building a new block or following a new chain, or building a different chain, depending on the relative weights of validators that they have on them. Right. And and this is this is not pretty either.
* Like none of these two options are really fantastic. 

**Stokes**
* Right? I mean, one small pushback is like, if there was a consensus failure today, like we would go fix it today. So, you know, it's not that, but there isn't can never touch the, you know, the protocol in between hard forks. 

**atd**
* I mean of. 

**Barnabas**
* Course, but but is. 

**Dankrad**
* Effectively a bug like this is like we like there is like if this limit was enforced consistently, then they would not be a problem. Like then. We would just have like an effective additional block size limit. So the problem right now, in my opinion, is just that it's not consistent. We don't need to raise it if every client has exactly the same way of determining it. And of course, if we stop self-builders from building blocks that are too large. 

**atd**
* I mean, the spec is unambiguous,  or the spec is the sense. Correct.  the differences in interpretation are rather minimal, to the best of my knowledge.  we all talk about the limit being on the uncompressed size, except maybe a few older versions of clients. Or maybe this has been fixed recently.  but by and large, in the tests that at least I have run,  we certainly see this limit kicking in. Right? It does disrupt the network when blocks become larger. So it's in so far as practical reality goes, it's correctly implemented. 

**Dankrad**
* Okay. So then what's the problem then? We just don't build blocks at large and then it's fine. 

**atd**
* The problem is that, execution clients or like, we don't know if, for example, builders, can build smaller blocks once, a large transaction hits their mempool whether they are able to exclude large transactions from their,  mempool when they are building blocks. And this limit has been exceeded. So, somebody posting a really large transaction could kind of poison the mempool, and it would be hard for block builders to not include this transaction except by, you know, a lower gas limit. And they would have to implement a new feature in order to put a limit on the total length of the transaction. RLP, which is which is the the real limit here or the size limit.
* I mean, that's a feasible way forwards as well. 

**Dankrad**
* I think we should do. 

**atd**
* That, but that requires their agreement. 

**Stokes**
* Henry, could you have your hand up? 

**Enrico**
* Yeah. So in that case, I guess the short circuit breaker will save us. And, anyway, progress the chain with some bumps, and they builder will be forced to implement something to fix quickly.  so I would say that in general, I think that I agree with Dankard that there is a bug around here, and this has been must be fixed, to have all the clients behave the same. And this is the most important thing. And I also agree with that having something better in, in controlling how the block is built is definitely, a very good thing to have that give us a better control over the sizes of data floating around. And I think this is a valuable thing to implement.
* And if it is safe at the end to have, to limit to, to to remain with a ten megabyte limit for a while, I think it makes sense.
* And, by we have time to address this, these details and have a better control over the block size. And we may not need to move this this limit. never. Essentially. 

**Stokes**
* Yeah. Terence. So just to clarify. 

**Terence**
* On the bug a little bit, it's also mentioned in the chat. Right. Because now the issue is that the attacker could just flood the local mempool with cheap transactions and then like, do the one like probably like will be whether they're whether they will be fast enough to react. That's a different story. But then like the problem here is that say today like no one can build a block anymore. So the only way to fix this is literally to send transactions to the main pool that end up paying more to the attackers, stuff.
* So I don't think the circuit breaker can save us unless today we basically override those transactions on the public pool. 

**Enrico**
* Oh, right. Right. So you're not so. Yes. It was meant to say that this is a problem in the building process of every execution. Client is not a builder problem. 

**Stokes**
* Right? Is that correct? Well, a little bit of both. And like. Yeah, maybe to summarize so far it sounds like a pragmatic path forward at this moment would be one like ensuring that all clients have conformance to the spec around this limit as specified today at ten megabytes. And then separately, the ask would be to change the transaction rules and clients such that you can't get these massive transactions. Was that correct? 

**atd**
* I think that's correct. Insofar as that proposal goes, the counter proposal here is simply that we just wing it and everybody increases their limits to a point where, you know, realistically, all these blocks get through and we hope that people upgrade and maybe there will be a few chain splits along the way. Right. And then we also increased the attack surface. And we deal with that later. 

**Stokes**
* Right. I think the. 

**atd**
* Urgency of the matter is, is is is the crux here. I think most of the things get solved by Petra, which addresses the root cause of this problem, which is a gas mispricing in my in my view, because it's simply too cheap to create. Like, the thing to remember here is that is is what the IP about increasing the gas cost for certain things says, which is basically that the average block is something like, you know, let's say 100kB or less even. And, and that's the useful kind of transactions that people post on chain.
* And then these, attack transactions, if we will, these massive transactions there.  first of all, filled with zeros.  which means that they compress. Well. So so it's not not that bad. But,  the second thing is that, it's the gas pricing that allows people to create these transactions, and the gas prices don't correctly capture the true cost of, of transactions this big.
* So increasing the gas price kind of solves this.  in the same way that. Yeah, in the same way that Shanghai, we had a gas mispricing on, you know, hard drive access and the gas price failed to capture the, the true cost of, of that particular thing. 

**Stokes**
* Yeah. So POTUS has a good point here that you can still do this with many smaller transactions. So yeah, that kind of puts a hole in this proposal to think about limiting this just at the El. 

**atd**
* Well, no, the El can still bound the list. The transaction list seems like an entirely dumb implementation in the in, the in the transaction pool is actually to just construct your list of transactions as normal and then cut it off at the limit. Like that will solve the problem. And it's a byte limit on the RLP encoding. So it's something that the L can comfortably do on its own if it wants. If we go down that route. 

**Stokes**
* So then it wouldn't necessarily be about changing mempool propagation limits. But just when you're building look at the actual size. 

**atd**
* Yeah, that's one possible solution. And it's not there's not a lot of interaction going on here between, EL and CL. The EL can implement this with a chain constant, basically. And I've put this the exact value for this constant in ETH research. We can easily derive it from the gossip max limit. It's a simple function. 

**Stokes**
* Right? Yeah. I mean, my one thing with this proposal is that then we need EL make a change. And then the question is like, can we coordinate ASAP?  you know, the next act would be next week. And it's also, I think, the last one this year. So just something to keep in mind. Like, logistically, you have your hand up. I can't hear you if you're speaking, but you did unmute. Yeah. I think yeah, I think you might have some audio issues. Dan? 

**Dankrad**
* Yeah. I mean, I think like, so right now we are on track for, an increase to 36 million. So it's not like something that will have to be fixed right now in a way, because I don't think many people will increase beyond that. but I think generally speaking, like whatever else we do, like even with 7623, like still having an inconsistent limit and having like an EL that can can create blocks larger than that is still a bug in my opinion. Like even if we now have a like have a fix that means oh yeah, like we can't imagine hitting that again.
* Like, well, who knows, in five years we might be at a billion gas and suddenly out of nothing, the same bug hits again. Like, I think, like, we should just really make sure that we squash this once and for all, even if it takes like a few more weeks. But I think, like, it's not acceptable to have this discrepancy. 

**Stokes**
* Yeah. I mean, I think everyone agrees with that.  and it seems like the path forward there is having this gossip limit somehow be a function of the gas limit.  yeah. You shot your hands back up. I don't know if you can talk. Okay. He had a comment in the chat. My point was that it's much easier to change the limit in the CL rather than mess with the ELs. Yeah. Okay. Well, okay, so it sounds like the immediate thing we can do is, again, ensure conformance with CLs and spec and. Yeah. I don't know if any EL devs are on the call and want to speak to the complexity of bounding payload sizes during build time. Yeah. I mean. 

**Ben**
* More complicated and you're also just pushing a consensus failure into a different place because then you've still got the issue with all the ELs trying to coordinate outside hard fork to get the right version. You know, it doesn't it doesn't make the problem any easier. 

**Dankrad**
* Well, the ELs not doing anything would not make like would not create a consensus failure. It would just be a failure to produce blocks by those who haven't upgraded. 

**Ben**
* So they would only it would only be in block production. They would accept blocks over size. Is that what you're saying? So if a non-upgraded EL produces an oversized block. You know, that's fine. Okay, now you put the problem again. 

**Dankrad**
* No. The that. Yeah. That block would just be, like, not accepted. It would just disappear. 

**Ben**
* And if you also change the validation rules for the ELs to reject blocks that are too large. 

**Dankrad**
* I don't think anyone is proposing that. 

**Ben**
* In which case the ELs would accept the blocks and you hit CL issue inconsistency. 

**Dankrad**
* All all blocks like to be accepted by the EL, a block has to be accepted by the CL. 

**Ben**
* Yeah. Which has inconsistent rules. 

**Dankrad**
* Right. Yeah. This has to be fixed for sure. 

**Lightclient**
* What is what needs to be fixed? I'm like, it seems like the EL will never even received a block, because the CL will not be able to send it over. Gossip. Yeah. So what is the change that you propose for? 

**Stokes**
* Me? Okay. So yeah, for for CLs, there's some question of like following the spec as it is today. And so that will be resolved ASAP. Then the question is like what do we want to do now versus, you know, wait until Pectra. And one option would be thinking about bounding the size of the payload produced.  the other option I'm kind of hearing is we just go with a more sort of reasoned solution that might take a little bit longer. But again, given this isn't like an immediate issue today, we probably have some time to do that. 

**Lightclient**
* Is there something that we can actually do outside the fork, like we are putting 763 in the fork, and that's going to solve this issue on the EL side. 

**Stokes**
* Yeah. So the longer term solution here would be having this Gossip limit be a function of the gas limit, which would just like solve it for all time. 

**Lightclient**
* But why not just make the gossip limit 50MB or something much larger? Like what function does it actually serve? 

**Stokes**
* Well, it prevents those attacks. So, you know, like as a CL client, you don't want to like have to think about handling a huge block and then, you know, the resulting propagation through the network and everything that entails. 

**Dankrad**
* I feel like also here there's something weird like does the current like my intuition is the current limit doesn't really effectively prevent any attacks. Like does it can someone speak to that? 

**Stokes**
* Like someone if someone sends like a if someone sends like 100 megabyte block, that would just be rejected. Whereas like if it's much smaller, then, you know, you don't have to think about that. 

**Dankrad**
* That's that's just a local thing, right? Like that is my a peer of mine. Because, like, I will not forward the like 100%. That's an invalid block. So I will never forward it anyway. So the only thing that could happen is that one of my peers sends me that block. But like a peer spamming me with messages like is a problem that you can't really prevent anyway. So I don't really exactly know what this prevents. Why ten megabytes really makes a difference there. 

**Lightclient**
* Yeah, I agree with that. And also I think that the in general, you're always going to be able to make the peer do work,  where you have some sort of message that you send the peer and they do an amount of work that is not really,  that does not really correlate with the message size that you send. And that attack is always going to be worse than just blindly tossing them with big pieces of data. 

**atd**
* So I can actually answer to that. This limit exists because if we don't have it, there is an amplification attack, and the amplification attack happens because the execution payload is validated asynchronously with respect to gossip propagation. So the way it works is that we receive the message in full. We perform a couple of gossip pre-checks we can call them the most significant check there is really the proposer signature. but other than that we don't check anything really. So in particular, we don't check that the execution payload is valid. So it could be stuffed with invalid transactions.
* It could be stuffed with junk. We don't know. We don't care. We give that to the El to validate. And then the El takes, you know, it's 1 or 2 seconds to validate the block. But all that happens asynchronously. By this time we've already started propagating the message.  so, what happens basically is that we, we can ask the network to propagate invalid messages through this little loophole. so, for example, I did a quick, like, back of the envelope calculation. And, if I did the math right, which I don't always do, but in this case, I landed at like 13GB of traffic for a five megabyte increase.
* And this is because, you know,  we have a fairly high, fanout on the messages seven, seven ish, eight. And this kind of repeats for every hop. So you cause these big pulses of data just flooding the network if you're hell bent on, on, on executing this, this particular attack and the reason we have the limit is because that amount of data is like feasible to clear within a slot, and we get a new chance for a new block at the next slot to sort of clear the pipes. **atd**
* The larger that limit is,  the more potent this particular attack becomes, and the easier it becomes to kind of make the next guy miss their slot because the gossip subchannel is busy spamming this massive message around. So that's what we're protecting against here. 

**Stokes**
* Okay. I do think we should timebox this to get to other things on the agenda. What I'm hearing is okay, one first off, like, see, I should double check that they follow the spec as written today correctly. if not, definitely need to send out updates. That one's straightforward. Then it sounds like what we want to do is take a little more time to think about what like the nice solution here is with respect to this Glossop limits and the gas limit.  the other sort of path would be moving ahead with bumping the gossip limit. to me, given the fact that. Yeah, it'll be, you know, a messy rollout or at least, you know, it could be messy.
* And what I mean when I say that is just we won't know, you know, which nodes have updated and which have not. that, to me, feels like more of a nuclear option that we should have in the back pocket if we need it. But again, given that gas limits probably won't raise before Petra, in a way that's going to be an issue. We have a little breathing room there.  does that sound like a good path forward to anyone, or does anyone want to suggest something else? Okay, I'll take the silence as agreement. There is some thumbs up in the chat, so let's do that. And yeah, I mean, I think everyone's very aware of what's going on, so please just keep an eye on things.
* You know, if, for example, the gas limit does raise over the next few weeks, we'll need to be pretty active in addressing those. Cool. So we'll just table this PR for now. But it's here okay. We can then move on to other things for F5. **Stokes**
* The next I think big thing I want to talk about is 7742. And there are some helpful context here, reaching out to rollups.  what do I want to say? So, yeah, maybe to, like, kick things off. So seven seven, four two. right now, the EPA proposes passing the target to the L, but not the max. And as people implemented this, we kind of found their places where we would want the the max, for the l to have, in particular, this came up with the RPC.
* There's like an API endpoint that gives you, like, the blob fee history. I think it's something like blob gas use ratio or something like this where you do need the max. And then there's from there sort of the bigger question, like, are there other places where the CL might want the max?  another place that kind of came up would be the Mempool. And in any case, it sounds like,  yeah, just passing the target is probably not the way to go. So then the question is, how do we want to address this?  we did reach out to Roll Call that happened the other day and asked them if they use this particular API.  Carl, I think you had some updates there. If you want to give us just a quick overview. 

# updates from roll call around pectra EIPs [41:05](https://youtu.be/VpYzaCzEVe8?t=2465)
**Carl**
* Yeah. Very quickly.  so, of course, we don't have necessarily everyone on the call who was able to answer this question, but from the people that were there have reached out after, roll call.  currently scroll zksync arbitrum and, the op stack chains. don't use this blob gas use ratio, endpoint.  and the only one that I have heard back that does is linear.  they said if we were to remove it, they could figure out an alternative solution. But, they have a preference for living in, if possible.  and then the other concern that was raised is,  potentially wallets might use this for, pricing in the future, but this is not something that anyone was aware of happening at the moment.
* So overall I'd say weak preference for leaving this endpoint in. yeah, that's that's all I have on that. 

**Stokes**
* So, yeah, I mean, someone does use it.  but yeah, it sounds like they're workarounds and otherwise there's not like, it's it's not like, critically used, generally. So that being said,  then the question is, okay, like, if we do want to keep the max, do we send it over, in the engine API? How is that structured? There's like a couple different options. one of them is just sending it over with the target on every block. We then probably want to put it in the header.  or at least it needs to kind of live somewhere that the Yale has access to.  and to that point, another option would be some sort of like status sort of exchange when the boot over the engine API.
* And then the Yale would just like, capture the max and, like, save it somewhere.  but, you know, point being is, as we started exploring all of this, we kind of even asked a question like, should we have seven, seven, four, two at all?  the reason we initially had it was to well, I mean, a couple of things. I think two big things was one, it wasn't as flexible to change these limits in seals and eels, and this would kind of be a forcing function to make this more easily configurable. The other thing is, if you do go all the way with seven, seven, four, two, you do uncouple the eel and seal.
* And then you can imagine a seal only fork,  where you change these blob limits, which is just like really nice flexibility to have.
* So that all being said,  there was another proposal to handle this differently, where you just essentially have this configurability notion. 
* You would remove seven, seven, four, two from Petra and then, you know, for example, you can imagine in like the Genesis JSON that clients have, you in the configuration they have. You would have these limits there instead. So you still have them coupled. You would kind of lose the seal only fork option, but it would probably be a much simpler implementation. It would take an EIP out of spectra and probably simplify things on that front. So yeah, there's a comment from my client in favor of removing, anyone else have any thoughts here? What could also be helpful is if others have implemented this just speaking to like its complexity.
* I mean, it could be the case that. Yeah, given that we want to ship spectra ASAP, and where we are in that, sort of the development process, and we might just prefer a simpler solution. 

**Dustin**
* Yeah. So this was actually something that Mikhail,  observed.  but I would agree with it. And that the 7742 creates this assumption effectively, or bakes it in that every single block is coming over this engine, API, or some other interface. Whether you however, specified I figure I assume that if 7742 happens, then people will like realize this and backfill this and look out every other way to specify a block and say, oh, we need to add it there too. But the point is that EL will will start assuming, I mean, the the point of how this works is EL start assuming that this is how they get sort of, let's say full complete and block packages,  and Nimbus.
* And at least I believe at least one of the CL has a situation where it will send will, verify block cache locally.
* That saves a lot of time while syncing to not send every single block we've benchmarked this, etc..  that creates problems. And again, I'm just sort of repeating what Mikhail kind of said in this quote. But  about especially around forks, but in general is like there's this uncertainty of, well, what if the number of blobs changes, etc. if it is truly dynamic, then it might change frequently. And at that point the EL needs its own access, either to get hear about it from the CL every block, or for it to be not that important or to have access in some other way. But if it has access in some other way, then it doesn't need the CL to provide that information. 

**Stokes**
* Right. I mean, another option is we essentially do 7742, but then still have like some config in the genesis.  yeah. I mean it'd be helpful, I think, to hear how we're feeling around implementation complexity, or even like the testing load. I think that would help us think about, Pectra collision. Yeah. Mario. 

**Mario**
* Yeah, I think I think in terms of at least execution layer testing. We're almost there. We have all the changes implemented.  I think the max limit inclusion wouldn't be such a burden.  but, yeah, it's basically almost there. 

**Mikhail Kalinin**
* A quick question. Even if max value is included in each EL block. So EL has this information, won't it be required by any potential use case that EL client should know the max in advance? So if the max is going to be updated since the next block maybe somehow also needed. Like what I'm trying to say is that, probably there is a use case where EL needs to know this the schedule of the schedule of target and max for kind of like dependent on the forks, not only the historical max and target. 

**Stokes**
* Yeah. I'm not sure if any devs can speak to that.  but yeah, I'm trying to keep up with the chat here. I mean, it looks like there is some preference for going with the simpler approach at the moment. 

**Lightclient**
* Yeah, I guess just from my perspective, it this the proposal is just not really doing quite what we had originally hoped. And we realized, like we're realizing with many things like gas limit, gossip, size of the CL, there's not a these things don't live in isolation, and it's just not realistic to expect there to be one uniform place to change these things.
* When we have two different clients with two different stacks, with two different networks, and we are just seeing places where max blobs are needed in the EL, so we're going to find a way to get that data over there. And if we're not changing the value of the max blob count on like a per block basis, it's still on a per fork basis.
* Then it's pretty straightforward for us to have a unified config between the two clients, and adding it to the engine API adds just like unnecessary complexity. Adding it to the header adds unnecessary complexity. 

**Stokes**
* Yeah, I guess the question I have there, if we go with the route to just have it in the config on both EL and CL, like how like do we need to specify this somewhere. Like how do we actually implement that. I don't believe there's like an EIP for this Genesis config structure. 

**Lightclient**
* I think that the Genesis config most like we can create any EIP, we can create a gist. It doesn't really matter. But if this is how we're going to be doing the devnets, then every client is going to implement the thing or else they're not going to get included in the devnets. So I think that's like a pretty strong forcing function for getting people to do this. 

**Stokes**
* Yeah. Do you have your hand up? I'm not sure if that was from. 

**Dankrad**
* Oh, sorry, I forgot to unmute. yeah. Like, I think it's crazy to have this in both clients and keep this as, like, something that has to be kept in sync between the two. Like, to me, that's tech debt. And we should eliminate it. Like, back when we started with the two like CL and EL, we were like, yes, this is cool. So we can iterate on both sides independently.
* But now we end up having always having to have all hard forks. Exactly. And so and like yeah, I mean my prediction is this is going to be okay.
* So now Pectra has to be coupled to the next EL fork. And then I mean that that's just insane to me like that we that we are okay with like slowing down something potentially by month like because one constant has to be changed and the other time. 

**Stokes**
* Yeah. I mean, I don't think there'd be a slowdown of months. 

**Lightclient**
* Yeah. I mean. 

**Dankrad**
* Right now we're talking about like, a constant being fixed in the CL in order to have a higher gas limit. And we already practically saying, oh, we can't really do it before Pectra.  I think practically speaking, it does feel like that's where it's going to end up. 

**Lightclient**
* If I feel like it's not that we can't do it before Pectra. It's just, how are you going to get everyone to update their clients to support this new constant before Pectra? Like, do you want to just have a new hard fork in one month that just does this config? 

**Dankrad**
* But isn't this the same thing? Like, I. 

**Lightclient**
* Mean it is the same thing, but like I feel like this doesn't really have to do as much with the CL breakdown here. It's that CLs are also focusing on shipping their own portion of the fork, and it's kind of a side quest to just update this constant and push the releases out and get everybody on board with that. 

**Dankrad**
* Like, exactly. And then we will be, let's say like we're like, we're ready to ship PeerDas, but like, the EL needs another two months for their side of the next fork. You don't think we'll be in the same situation where EL clients will now say, oh, yeah, but, like, it doesn't make sense to make this mini release now. Let's just do it together with the hard fork. 

**Lightclient**
* I just don't think these things are in, like, pure isolation. Like bumping this constant on the CL for the gossip. Max size. This is not something that you could just mindlessly do. Just as you can't mindlessly increase the blob limit with respect to the transaction pool on the execution layer. So I think that the conversation is just always going to have to go both ways. There's always going to be discussion about the safety of doing these things. Has the other side implemented the necessary protections to deal with this higher load? 

**Stokes**
* Right. So there are a few other updates around the cap that have come in. So maybe we'll take a look at those. And that might give us a sense of, you know, impact for spectra.  one of them is pretty simple, but there was an EIP update that, the effort kind of merged on me when I didn't want it to.  it's this here in the chat, and it was just clarifying the EIP because the way it was written, well, more than clarification, but the way it was written, it was suggesting to look at the current, target blob count, when really we should be using the parent. So that's all this does.
* But point being is there is a small change here and that will then, you know, we'll need a round of updating testing around updating implementations.
* So that will take some time. The other thing is there was another conversation on the engine API. And again, this is somewhat minor, but I think we'll probably want to refactor some of how this PR is written,  to align it with essentially how we handled the parent beacon block. It's like a similar thing where the CL is passing this data.  so again, pretty minor change, but we will likely need to address that. So that all being said,  it does feel tight to do all that, get it ready and then have Devnet 5 and say like the next week or two. I guess maybe then we could check in, like, do we have a timeline for F5?
* I mean, I think we'd like to get it done this month, but then realistically that is only a couple weeks left. And then I guess the alternative. Yeah. Mario? 

**Mario**
* Yeah, I think I mean, from the side of testing, at least for the execution part,  we're, I think, almost ready. the problem is that even if we make a release, let's say today or tomorrow, with every change that we had already considered before this call, even then, I think there's going to be like a lot of, in my opinion, a lot of issues that need to be addressed when the clients start consuming these tests.
* So even optimistically releasing today,  I don't see that happening even maybe next week, I don't. But I'm not that that optimistic to be honest.  yeah. Just wanted just wanted to put that out. 

**Stokes**
* Right. I mean, the other option is if we go with the configuration route for the time being, that will also take some time to, to build out.  yeah. And it seems like consensus is somewhat split on this. I see some comments that say preference to take it out. There's definitely a demand to leave it in.  I mean, I guess one question is like, how much thrash would it be to take it out now? Like, is it the case that it's pretty much there?  if we do move ahead with it, then we'd probably need to think about this RPC endpoint.
* And I think for like Devnet five, let's say we could just kind of leave it as is, even if it would be broken.  but yeah, that is something we need to address down the line. I will say I very much like simplicity.
* And while I hear the benefits of having sort of the full 7742. If we do think it's just simpler at the moment to go with the configuration approach, that sounds. Sounds nice.  we need to undo some work. Okay. So then if we leave it in,  yeah. Would we be? Yeah. I think this is a hard call to make. so if we leave it in, then we would want to figure out some way to handle the max. but then we could just kind of leave it broken Devnet 5, and then we need to address it in Devnet 6. 

**Barnabas**
* Why can't we solve it the same way as the target? 

**Stokes**
* Well so we can. But then it's just like you're sending over this, this number that basically never changes. And then it's just there for all time. Yeah. And then there was this comment, like adding them to the header is probably more work than undoing it. And I guess that's the other. 

**Barnabas**
* Knew what that this number will rarely ever change. Like when 7742 was. 

**Stokes**
* Right. Right. And but we also didn't think we would need to send it over to the EL.  I mean, it feels to me like removing it would just simplify. Pectra, honestly.  And I'm going ahead with the configuration change and having that for demo five. Yeah, keeping it in but without the max seems like the worst option. Okay. Yeah. Okay. I mean, I think that's what I lean towards. And I mean, there's always the option to revisit this in the future,  and go for, you know, a more sort of at least having more time to think about how to handle this without then having to delay Pectra.
* So, yeah, I mean, there's some other comments here in favor of simplicity.
* So, yeah, I mean, I think we should just go ahead and take it out.  anyone super strongly opposed to that? Otherwise, I think we just go ahead and do that.  yeah.
* Which simplifies the. Yeah. So you don't need to do that.
* But we can just kind of ignore the EIP, the engine API. We can ignore that.  and then yeah, there was some work merged into the CL specs, but yeah, I can. I think Justin made a comment, but yeah, I can help you with that as well. Justin. we can get that done ASAP. So yeah, let's go ahead and do that.  I suppose the like, if there's a compromise here, the compromise is that, we cannot let like, for example, if we're ready to, like, ship a PeerDas or change the blob counts in any future fork, we should we cannot let, the ELs kind of hold things hostage here. So let's just agree to that. Let's keep moving. 

# Updates around EIP-7251 [1:01:27](https://youtu.be/VpYzaCzEVe8?t=3687)
**Stokes**
* So that's for two. Okay, so there are a few things around 7251 one. what do we have here? So this first one, Mikhail, had a PR to, limit the consolidation balance via the effective balance.  I have not had a chance to look at this yet, but there is there are some approvals on the PR. Mikhail, would you want to give an overview of the changes here? 

**Mikhail Kalinin**
* Yeah, sure. So,  just recall on how consolidation happens first. the source is exiting where we churn validator where we churn the effective balance. So which is actually the balance that, that is exiting.  and then after it exited, we moved the balance.  when the withdrawal epoch comes and, the existence pack uses max effective balance as the limitation for the balance that will be moved. And yeah, this is a bit of it's a bit, create some asymmetry and discrepancy because we like to want to use it's more reasonable to use effective balance. And this place as well is kind of effective balance is is exiting.
* And then we we move it move the effective balance of max the balance that was that has exited.
* So now it's yeah it's it's different. And there is uh there are some edge cases with that as well,  that are listed in this PR description.
* So yeah. Basically that's, that's fixed  this small,  discrepancy. And also,  there are some tests in the PR,  more extensively testing the balance and that it moved the balance moved during consolidation. So this I think it would be great to have this in Devnet five. So we need to just merge it. And if there is an opposition from client teams to I don't think it's like a deal to implement it. It's basically fixing one line. So if there is an opposition, please let us know. 

**Stokes**
* Yeah. Has anyone else had a chance to look at this?  but yeah, I mean, I think that makes sense. It seems like a pretty simple change. I would think we go ahead and get it merged, you know, in the next day or two for Devnet five. So, yeah. In the interest of time, if anyone wants to review this async. Yeah. Take your feedback to the PR. otherwise. Yeah. Mikael, I can work with you on getting this merged. this seems like a straightforward change. Okay, so there's that one, 

# eip7251: Limit consolidating balance by validator.effective_balance consensus-specs#4040 [1:04:25](https://youtu.be/VpYzaCzEVe8?t=3865)
**Stokes**
* And then the other 7251.One thing was this PR,  this one is a little more complex.  but essentially there is an issue with, like the distribution of, like, sampling when you go to think about proposal shuffling and also the same committees, given the way that we have this like Max eb,  basically the math kind of just doesn't work out with what we have using sort of one byte as this point of comparison. And this PR suggests using two bytes.  there's some really nice, there's a nice spreadsheet here that makes the math, I think pretty concrete, and it essentially just smooths out all these different,  probabilities, let's say, given maxdb.
* So again, I'm not sure if people have had a chance to look at this.  but yeah, it's a pretty straightforward change and seems to make things a bit nicer. So,  yeah. Any feedback on this at the moment? I don't know if there's something else. Justin to add. This was a pre raised. 

**Stokes**
* Okay. We got a let's merge. I mean, this one is a little more invasive even than the prior one, but yeah, it does seem to make things much nicer. So,  how about this? Yeah. Please. See all clients take a look. And even later today. Definitely by tomorrow.  otherwise, yeah, the intent will be to have it in the next release for Devnet 5. Cool.  okay. I think from here there were some EL focus things, and one of them was another comment from Roll Call. Ansgar brought up this in the chat, and Karl had a summary, in his commentary on the agenda. And it was around 7762. Ansgar. Karl, I'm not sure if you want to give us an update there. 

# EIP-7762  [1:06:27](https://youtu.be/VpYzaCzEVe8?t=3987)
**Ansgar**
* Yeah. So basically, actually, this is basically a no op update because,  last week we decided preliminarily to not include this EIP, which is this, EIP to, to, to basically establish a minimum block base fee. I had argued last week quite vehemently that that we should add it.  and so we, decided to revisit this week with some,  feedback from from roll ups in between.
* And in the past, there had actually been quite a bit of desire from, from roll ups to have have this and but now on roll call, we talked about it and it seemed like basically,  roll ups have been able to more or less work around this for now. And so actually it is lower urgency than I had, perceived it. So with that feedback in mind, and given that we decided last week to only include it if really there was a strong case for that, it seems to me like the best thing to do here is to just go ahead without it for for Pectra. And then,  given that in Osaka, we wanted to make bigger changes to the market anyway.
* I would assume that it will be part of that change then.
* And apologies for taking up so much space last week then, given that that seemed to be lower urgency than I expected it to be. 

**Stokes**
* Okay. And sorry, I was looking at something else. Basically, you're saying we don't need to think about this EIP for Pectra. 

**Ansgar**
* I think it would still be a good change. But given the situation in Pectra, I think, yeah, it's fine to leave it out. 

**Stokes**
* Okay, then I would suggest we don't put it in and. Yeah, thanks for the update. Thanks for reaching out to roll call, both of you. That's super helpful to get L2 inputs on these questions. Okay. there was a point to follow up with the  precompiles. I know there was a separate thread of work to finalize the gas schedule. I'm not sure if anyone here has any updates there on the progress mark. 

# BLS precompile updates [1:08:35](https://youtu.be/VpYzaCzEVe8?t=4115)

**Marek**
* Yes. So we split it into three PRs to discuss different operations separately. And first we are. This includes simple operation like add multiplication and map. And we have a strong consensus among all people. second PR for pairing. I think we have consensus here as well, at least no objections. And third PR this is for multi scalar multiplication. And in this case we got consensus from all clients because numbers from benchmarks are correct across all clients.
* However, Pavel raised a valid concern today that if we proceed with the current pricing, it will create a weird pattern in smart contracts where they might implement a fallback to normal multiplication for multi scalar multiplication with a single point.
* And Pavel just sent a new numbers that take this issue into account. So clients will have to add a small simple if with a fallback to multi multiplication on their side.
* And we will benchmark it again. And I think that's it.

**Stokes**
* Okay and the idea would be to merge all of these PRs. I haven't had a chance to look at these yet. 

**Marek**
* So I think after we merge them all together. So after we benchmark this first PR with multi scalar multiplication, we could merge it. 

**Stokes**
* Okay. Is that something we can do by next ACDE. 

**Marek**
* Yes we have to. 

**Stokes**
* Okay. Great.  cool. Okay then. Yeah. Any ELs clients listening? Take a look at these PRS.  thanks, everyone who's been busy working on this. I know there's been a pretty active investigation to get this over the line. And then, yeah, we'll have these final benchmarks for the MSM and sort that out next week. Cool. Okay. I think that was the Devnet 5 stuff. Were there any other like spec level issues or concerns people had? Yeah. So that was my next question.
* Barnabas. So then, yeah, we can turn to timing.  you know, there's still a number of things that will change from today's call and even next week's call. Then the question is, yeah, how quickly can we get all of that together?  it would be great to launch Devnet5 before the end of the year, but we are halfway through December, so that is what it is.  yeah. Barnabas says launch it on Christmas. Yeah. I mean, the one thing is, I'm not like, I imagine there'll be things around Pectra that will need to discuss next week.
* So definitely, you know, we can move as quickly as we can. I think the CL thing should be settled today and so people can get a head start there, but otherwise. Yeah, I am not sure how to make things move faster. Yeah. I mean, I guess, yeah, something that could be helpful here is like, do people have a sense of like how long implementation would take given the changes today?  you know, is it something you feel like you could turn around in the next week, or is it maybe going to take a little bit longer? 

**Barnabas**
* I mean, the config adding the target and max to a config should be very simple. Yes. So I think the only thing we are waiting for now is the BLS stuff. Right? 

**Stokes**
* Yeah, there's a few other PRs here. but they're all pretty minor. Stay with 7251.  what else did we talk about? Yeah, and there's this one at the beginning, but that's just a renaming of field. So, yeah, I mean, it is all somewhat small in scope.  and yeah, we're getting a bunch of chat comments that would be pretty quick. So do we want to look at the calendar here. Let's see. Yeah I don't know. Do we want to try to launch Devnet five on the 20th or is that, unwise? 

**Barnabas**
* I mean, if the scale changes. 

**Parithosh**
* Yeah, I think at the very least, we'll get, local config. So whichever clients are ready, they can have stuff to test on, and we'll have,  hive up so we can see how clients are doing. But, yeah,  if there are enough clients ready, I think I'm happy to launch the devnet between Christmas and New Year's. 

**Stokes**
* So, yeah. Then let's, you know, directionally aim for net five as soon as it's ready. And that's going to be in the next couple of weeks.  so yeah. Yeah. As my client says, Mary kindness.  but that being said, I think the sooner we can get this together, the sooner we can ship. So, Yeah, that that would definitely be best. And, yeah. Terence, we can update the the spec, reflect the the sorry Devnet five spec reflecting these updates after the call. Okay, cool. Okay. I think that was it on Petra. 

**Stokes**
* There are any other comments, please raise them. But if not, then we can turn to a few other things. I put this here under sort of the the PeerDAS bucket. there's this PR for a spec, and the reason this is relevant to the blob stuff is that, this was essentially the next step for PeerDas.  everyone's very busy with Pectra. that being said, as soon as Pectra is stable, then we can think about putting, period on top of it. And that means fuller. So I think the concrete ask here is just double check that we can go ahead and move forward with this, refactoring.
* Anyone opposed to that? Front of us had a comment here on the PR, but it looks like you crossed it out.  I think this was discussed on either the another desk call or the testing call earlier this week. And from what I heard, there was, you know, agreement to move ahead with this. So yeah, let's go ahead and merge that then. unless there are any final objections. And I'm not hearing them. So we'll go ahead and do that and. Nice. Okay. there was one last thing. Tim had an ask to discuss this PR, clarifying the relationship between CFI and SFI. Tim, do you want to take it over? 

**Tim**
* Don't have the PR handy, but,  so actually the idea is to clarify the definitions of CFI and SFI based on the Devnet development stage.  so I think there's two failure modes we run into when we plan these hard forks. The first is that,  we're not we don't have quite a formal definition of what CFI means, and it's hard for different people to interpret that. They sort of have to read the TD leaves a little bit. And then the second is we commit to having a bunch of stuff in the fork in advance of actually knowing how hard or how much time it will take to implement it. 
* So my proposal would be to map CFI and SFI to Devnet inclusion status, where we just formally say that CFI means these are things we want to put in a devnet for the fork. And so it's kind of a clear a clearer signal, and it's already sort of implied by it. But you can think of CFI as the list of anything that we think will be in any of the current forks. Devnet.  and, you know, assuming everything goes well, they're probably on the main network, but there's always some uncertainty. And then I'd make SFI mean the things that are in the next devnet. And the, the rationale there is that this could help us sort of throttle how many things we bring in at once.
* And whereas with Pectra, as we saw, we brought in 20 things in the fork early on before most of them were implemented.  and one challenge with that is not only do we not know how, how long things will actually take to implement, but then if we have many different things that many different teams have to implement, not everyone makes progress on the same thing at the same time. 
* And that slows things down overall.  so basically we would say, you know, like in this case, SFI would be the things we think will be in devnet five. And if we want to add more things to that after the fork, that's great. They can be in CFI, but we sort of don't move something up until we feel like in the next devnet we can implement it. So that's the overall idea. thanks, Alex, for sharing the PR in the chat. Yeah. Any thoughts? Comments? Concerns? 

**Stokes**
* Yeah. I mean, I think this makes a lot of sense.  Pectra was an unwieldy fork, and I think it's in part because of what you were calling out that, yeah, there was maybe not as much structure around having an EIP or some proposal and then thinking about how it goes through the process to get to the nuts. And yeah, my read is that this is not meant to add more bureaucracy or slow things down, but more just to give us a little more structure so that it's clear and we can all coordinate better around that. 

**Tim**
* The one thing you would slow down is like the rate at which we can SFI stuff, which I think is a good thing. So we if we say we're putting ten things to SFI, we should be saying in the next Devnet we want to implement those ten things. And if we think that's too much, then we have to pick, you know, which subsets do we actually want to put in the next step. 

**Stokes**
* Not sure, but yeah, so there's more discipline. But the whole point is to make like it's maybe slower in the short run, but it's better in the long run, right? 

**Tim**
* Yeah that's at least my idea. And I'd be curious to hear I don't know from like client devs and the people who actually end up implementing this stuff, like, does this seem reasonable?  yeah. I guess if there's no comments, I'll leave the PR open up for a few more days for people to review, and I'll merge it by the by next week's all core devs if there's no concerns or pushback. 

**Stokes**
* I think that was everything on the agenda. I'll see if there are any last minute additions. I don't see anything. yeah. Anything else? Otherwise, yeah. We're all very busy with Pectra, and we'll close a little bit early and get to shipping. Okay. We got a ship in the chat. Cool. Okay. Well, thanks, everyone. Happy holidays and, happy Pectra. I'll see you next time. 


---- 


### Attendees
* Stokes
* Tim
* Arnetheduck
* Marek
* Lance
* Micah
* Paul Hauner
* Ben Edgington
* Loin Dapplion
* Terence
* Enrico Del Fante
* Pooja Ranjan
* Hsiao-Wei Wang
* Saulius Grigaitis 
* Roberto B
* Olegjakushkin
* Chris Hager
* Stokes
* Dankrad Feist
* Caspar Schwarz
* Seananderson
* Andrew
* Crypdough.eth
* Zahary
* Matt Nelson
* George Avsetsin
* James HE
* Marius
* Ansgar Dietrichs
* Lightclient
* Stefan Bratanov
* Afri 
* Ahmad Bitar
* Lightclient
* Nishant
* Gabi
* Pari
* Jimmy Chen
* Gajinder
* Ruben
* Mikhail
* Zahary
* Daniel Lehrner
* Andrew
* Daniel Lehrner
* Fredrik
* Kasey Kirkham
* Protolambda
* Cayman Nava
* Stefan Bratanov
* Ziad Ghali
* Barnabas Busa
* Potuz
* Trent
* Jesse Pollak


**Next meeting**
* [Thursday 2025/1/9 at 14:00 UTC](https://github.com/ethereum/pm/issues/1218)
