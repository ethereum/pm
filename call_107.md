# Consensus Layer Call 107

### Meeting Date/Time: Thursday 2023/4/20 at 14:00 UTC
### Meeting Duration: 1:08:20  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/756) 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=tJULkA5YgP4&t=9s) 
### Moderator: Danny Ryan
### Notes: Metago

## Capella [5:15](https://www.youtube.com/live/tJULkA5YgP4?feature=share&t=316)

### Fork Retro

**Danny**
Welcome to all core devs, consensus layer call 107. This is issue 756 in PM repo. The first gen item is a bit ceremonial. I think that we don't have much to discuss. The Capella fork was last week and we did have the execution there call soon after and did a bit of a retro there just in case there are additional discussion points on Capella. Before we move on now is the time. Anything else on Capella?

**Peter**
Thank you. 

**Danny**
Hey Peter. Okay….has an owl art spec…

**Etan**
It's more about the documentation thing just we displayed the owl on the Capella transition and the owl then displayed whenever someone converts a credential. It's just a spec to document the actual behavior. But yeah, Capella was nice. 

**Danny**
Yeah, vanity art specs, take a look if you feel strongly about it. Thank you. Okay, anything else on Capella before we close this off? Okay. Congratulations. Thank you. 

## Deneb [07:03]( https://www.youtube.com/live/tJULkA5YgP4?feature=share&t=423) 

### Potential blockers for [4844-devnet-5](https://hackmd.io/@inphi/HJZo4vQGn) 

Moving on to Deneb. There's a couple of discussion points from Tim before we get into discussing a few features that are under consideration in addition to 4844. Tim, can you kick it off on you had a link to some potential blockers for 4844 devnet five?

**Tim**
Yeah, so actually that yes, there's three things they're just things that came out in the call. So the potential blockers is not that there was a blocker, but we said that we would just check in with the client teams today to make sure that if there are any issues as we're trying to stand this up, you can bring them up on the call. And then hopefully have the devnet up sometime next week. 

So yeah, I guess if anyone has. I guess, or I guess, you know, if anyone can give an update, maybe I'm like setting up the devnet and any and show issues you run into that might be…yeah, that would be good. 

**pari**
Maybe I can speak up to this. Rafael is sitting next to me right now and trying the dry run of the testnet that so they're actually. I'm not sure. I'm sure that's. The project is expected. Currently, the lodestar and ? in here, so the two that said they want to be involved in the dry run. But if other clients want to please give us your images and we'll add you to the dry run. The current plan is to have devnet five next week. If the plans are ready in course. 

### PR to merge getPayloadV3 & getBlobsBundleV1 [08:41]( https://www.youtube.com/live/tJULkA5YgP4?feature=share&t=521) 

**Tim**
Anyone else have. Comments or thoughts on that? Okay. Okay, and the next one, Mikhail, I believe you put up the PR that was mentioned, but it was. Yeah, do you want to talk about that? Yeah, I'm not sure. Is Mikhail here? 

**Danny**
Yeah. I thought I saw him. Now I do not see him. 

**Tim**
No, he actually said he was not going to make the call. So basically the pr he posted was also in the first 4844 call. We discussed this just to merge payload be three and get blobs bundle V one engine API calls. And to try and get this live on the devnets as soon as possible. And so if people want to review the specific pr so we can get it merging the next couple days that would be ideal. 

### Blob re-orgs & newPayload([context]( https://ethereum.karalabe.com/talks/2023-ethtokyo.html#15)) [10:02]( https://www.youtube.com/live/tJULkA5YgP4?feature=share&t=602) 


And then the last item from the 4844 call, Danny, was the new payload and reorg stuff. Yeah, you want to get some context on that? And I think Peter is also on the call so…

**Danny**
Yeah, I knew a good context and certainly Peter can try them. Yeah, so I think what one of the things that came out of mempool discussions at eight device was how to handle and reinsert blob transactions into the mempool upon reorgs, which is a facility we can provide to users today because all the transactions, the full nature of the transaction is in the block. 

Given the decoupled nature of the blobs, you might only have blobs available to do these reinsertions from what you've seen on the mempool, but plenty of things do bypass the mempools. And then we can have blobs. I think the two potential paths here are to have new payload insert the blobs and the consensus layer such that the execution layer can have them and choose to do what they want with them like cash them until finality or anything like that. 

The alternative is to not provide, not be able to provide this quality service to users that bypass the mempool and just leave the payload as is. And if you want to handle reorg transactions, only handle what you've seen in the mempool and can locally do. I think this is the two paths on that. 

Peter, you’ve been thinking about this a lot. 

**Peter**
Yeah, well. Sorry, I have a sore throat, its a bit hard to talk. Yeah, so I guess you kind of summarize it kind of correctly. In my opinion, it's kind of nicer to provide that service for everybody. So if there, a consensus client has the blobs anyway, I mean, the blobs aren't that big so the new payload, I mean, currently the limit is set to 2 to 4 blobs per block. So that's a 500 kilo bytes. 

I don't think that's such a big overhead as to be prohibitively expensive to just give that to the execution client. My two cents would be to just send it over. And if for some reason we think it's maybe it's kind of a bit excessive, then we can always make it a bit...we could create a ping pong, maybe I were you just tell us that hey, these block contains these blobs. And if I don't have them that I can return some specific error message and then you can reissue the new payload. 

It gets a bit messy. So I will try to keep it simple first. And if it for whatever reason is insufficient, maybe then complicate it. And so the whole overhead of execution clients maintaining these blobs until finalities pretty much insignificant. So yeah. The only thing you need to do is maybe create either in memory or on this just a spokey value store where you map block numbers to blobs and then if there's a real you just resurrect the blog back into your mempool if there's a finality you just delete everything that's below some threshold. 

There might be some very, very weird quirks or even that some of the execution layer block numbers might not correspond to finality. So I mean, in a very, very weird situation can happen that you have reorgs with varying that. And finality belong to varying block numbers, but I think protecting against that kind of weird behaviorism isn’t really relevant. So I mean, we don't really expect reorgs to happen at all. And if they happen and we can handle it gracefully that's fine and if something really wonky happens and we lose to blob transactions then yeah, they can just trust resubmit. 

So my two cents, the simplest solution would be for consensus clients to give the blobs to execution clients when essentially they send a new payload. And even now the new payload, you can't really say that this would maybe make it look a lot more expensive because the maximum permitted transaction size in a block, in a new payload can be quite significant even now, so it's not like we all have a sudden permit some wild big numbers to be passed there. 

Anyway, it's a bit random, but kind of those are my thoughts. 

**Danny**
Yeah, and I think. There's probably two primary counter arguments will be the, and I know we hashed these up for one is this just kind of further breaks the abstraction between these two layers. So from kind of like an abstraction cleanly standpoint, maybe not to go down that path. 

The other one is more future looking is that a. On average a consensus layer node in the event of data availability sampling wouldn't actually have all the blobs. And would have sampled and might have a subset and so we're then creating a facility and maybe a user expectation that is not coherent with what we believe to be our most likely future. And I know we can push back on that and say I don't want to design for what we think is going to happen in two years. But that's definitely the primary counter here. 

**Peter**
There's may so I have no idea what that future will bring but the quick question. Is this whole data availability sampling, is this relevant for the next executable block? So. So is the expectation that in the future consensus clients will not even have the blobs for the block just produced by the network?

**Danny**
Correct. Yes. The network as a whole has the blocks has all of the blobs, whereas individual full nodes, super full nodes, people that want to download them, certainly will. But it's more distributed across the p to p and you've sampled to proves yourself that they're available but not have all of them. 

**Peter**
That's kind of interesting however I so currently the expected flow apart from M.E.V. bundles is that essentially the transactions, including the blobs kind of originate from the execution layer. So my guess is that the general expectation is that most blobs will traverse your machine because they will pop into your executables. 

**Danny**
Yeah, I mean, In such a design, if you build locally, you're likely building smaller than the potential maximum blobs. And otherwise you're asking higher powered specialized nodes that you pay to package blobs. You know, if you move into a regime in which you have 10 megabyte or 20 megabyte total blobs, then the average node is not going to be touching them all. 

So that is the in theory, the design of extending data availability beyond the capacity of a single full node or a consumer machine, is that you have to bypass touching all the blobs on the normal case. 

**Peter**
I see, yeah, so my gut response to that would be that maybe we should try to cross that bridge when we get there. So if we want to allow that to happen, then my guess is that it would require a bit of redesigns on the blobs too and so we would need to change the expectations on what happens with these blobs over the network in general across entire network. 

So I don't think it would be too big of an expectation to say that okay until now it worked like this, from now on it will work like that. 

**Danny**
So, yeah, I agree. I don't think that's a crazy thing to make such a shift. I just, designing the APIs such that we don't even have to necessarily think about components of that shift would be nice in my opinion, but this is not like a major sticking point, I don’t think. I would like to hear if other people have opinions about the API and about this handling, reorgs. 

**Gajinder**
So I am and ? kind of discussing this in the shared data channel and so one of the points was that since the transactions that will sort of bypass, mempool will most likely be MEV transactions which are directed at a particular state. So they won't actually be mined. They won't mind being dropped if there is a reorg because that straight ? won’t be valid for them. Another thing that Mikhail brought up was that so in case of if CL also wants to optimize and want to sort of send over want to do a lot of transactions, new payloads to evaluate even before they get all the blocks. So to do some sort of a parallel optimization. Even in that case, this assumption breaks down that the CL will be able to pass all the blobs to the EL. It would be very clean. If basically we make the assumption that the blobs that bypass that block transaction that bypass the mempool, they won't be including in the reorgs. 

**Danny**
So are other strong thoughts or hands on this? I do think that the execution layer folks who are not vastly represented on this call might have more to say. 

**Peter**
So in general, it feels a bit strange to have this use case where certain transactions that can appear in blocks cannot be resurrected. So that's definitely would be a new behavior on the fear of mainnet since that currently the expectation is that if your transaction was included in a block then if a reorg happens, there's always a very slight chance that we get lost for whatever reason, but in general, you can rely on the transactions not getting lost. Now, with regard to MEV saying that well, if you submitted your transaction by an MEV then you don't really mind if it gets lost on a reorg. That seems like a double edge sword. I mean, I don't really want to…so I think if you submit a transaction and the MEV maybe where you try to take advantage of a situation and then the situation changes and you the network even helps you undo so that you don't have to pay your initial fees that seems like a bad thing. I don't know. 

**Dankrad**
So I mean, I want to push back on that. I think in reality, as long as your constant transaction is economically valuable, which basically just means it has a tip. Like, even if like normal nodes don't push it back on the chain, someone will, even if its just for MEV, like they like there's an incentive to simply like say as a block builder to take that transaction if it was reorged and put it in MEV block in that block. So I think it will still happen. There's no reason why shouldn't happen. Like people are definitely sophisticated enough to do that now. 

**Peter**
Yeah, but then it means that essentially people running a custom build or custom flag which just forces these blobs back into the execution layer will actually have the potential for more fees. So we essentially would designing by creating a mechanism by design where it's MEV is important where its worthwhile to run custom code versus the stock code because the stock code by design. Discards the data it could it could not discard and or could retain. 

**Dankrad**
But I mean, like I feel like we're talking about very minute amounts like that that already exists, right? Like that that discrepancy is already pretty huge due to existing MEV on chain. And now you're saying in the case where like someone reorgs a block, then in that in those rare cases, like you can make a little bit more money by including that bob transaction. And my might that would be that this is less than 0.1% or so of MEV. 

**Danny**
Yeah, I guess whereas in as the by making type of transaction three be very specific and not even be able to carry non zero blobs, you know, we've tuned this and tailored this to a highly sophisticated user, at least in expectation roll up operators. These highly if these highly sophisticated users are bypassing the pool, they're also probably sophisticated enough to resend and with their transaction. I think one thing that Gajinder mentioned was MEV transactions are often tailored to a particular state, meaning, you know, they're sophisticated enough that they have or should have particular slots that they can be executed and they might have particular conditionals upon state, which otherwise they would fail. And so these transactions often replayed in other contexts to throw. 

**Peter**
But they do need to pay with the block fees. Essentially once it gets propagated to the network, the idea is that once you cost network to bear the bandwidth requirements of getting your transaction all over the place, you should actually be more or less forced to cover those costs. 

**Danny**
Yeah, which I get, especially in the mempool. Um, you know, because the mem pool, even by like you can put that cost without ever getting into consensus if things are tuned poorly. Whereas in this reorg situation. You did put the cost, but you put the cost in the context of blocks, which were reorged, which in the normal case don't so I think the argument's a little bit less strong than if you actually were in the mempool. 

**Peter**
I mean, um, you're still broadcasting or propagating that block through the entire network, at least in the current design. So you're still…

**Danny**
But if it's picked up in a reorg and another block, it's going to be broadcast again. So it doesn't matter what was picked up in that reorg, because it, it's going to represent blob load. 

**Peter**
Yeah, but if it gets lost, then you just broadcast it for free. Anyway, yeah, it's kind of very subtle. So it's not like, uh, yeah. I know, um, I can ? think about it if I. I guess it's kind of, um, if the general long term direction is to, um, it's to try to only have a sample of these blobs. I don't know, maybe in that world, it might make sense to do this limitation now. I have to think about it. 

**Danny**
Yeah, well, you chew on it this week and we'll also ask the execution layer folks to consider this so we can try to make a decision on the execution layer call in one week time. 

**Peter**
Yeah, yeah. 

**Danny**
Yeah, Cool. Thank you, Peter for joining us. Any other just final comments in this for moving on? We have a pretty packed schedule today. 

Great. Tim did we cover everything…the devnet…potential blockers? 

**Tim**
Yeah, that's all the stuff that was from the fork 4844 call. 

### Under Consideration

#### [add EIP-4788 feature consensus-specs#3319]( https://github.com/ethereum/consensus-specs/pull/3319) [28:43]( https://www.youtube.com/live/tJULkA5YgP4?feature=share&t=1723) 

**Danny**
Great. So I want to spend some time at least looking at some of the features that are sitting in the future directories on the consensus layer specs that could be under discussion for Deneb or at least we can start figuring out if not Deneb, um, where they fit in the priorities for potential future forks. My feeling is that there might be room for one or two small things that are not cross layer, other than maybe 4788. But that the opportunity for additional cross layer things beyond that is probably low and for example, like the deposit and protocol deposit processing. 

But let's take a look at some of these. So, 4788 is cross layer. That is that, beacon block root into the EVM. And that was discussed on the execution layer call last week. I do not believe the decision was made, but Alex, can you give us the quick on that and then an opportunity for people to signal if this is, you know, coherent and simple and find enough to get into Deneb, assuming that you also agrees. 

**Alex**
Sure. Yeah. Uh, so at a high level, the idea is we want to expose some computer graphic accumulator from the consensus layer into the execution layer. So this could be like a state route or a block root, the way the feature is written now is passing the previous block root into, you know, the current block, which is then just, you know, passed along to the EVM, uh, where it's exposed there. 

So, you want to look at the yellow details, you can look at the EIP, otherwise this features pretty lightweight at the consensus layer, basically you just need to get the block root and then you send it through the engine API. 

**Danny**
Cool and just, is the general feeling on the execution layer call that this is as a high chance of inclusion, or is this on the contentious zone on the execution? Are we unsure?

**Alex**
So it's super valuable for staking pools and many other use cases. Uh, for the CL, it's like, I think a pretty lightweight lift, you really just have to send over this route and maybe like one slot number, but that's it. 

**Danny**
Cool. I guess assuming there's an appetite for the complexity of the springs in the EL, is anyone strongly against the additional overhead, this is going to take us again in addition to 4844, which is our primary? Okay. Cool. Yeah, this is about as simple of an EIP that can consist on the consensus layer. Okay, so let's continue the conversation on the execution layer with respect to this one. And we would, if there's a green light over there, we'll do a sandy check again on this side, but generally good feeling here. 

#### [EIP6914 - Reuse indexes with full sweep consensus-specs#3307]( https://github.com/ethereum/consensus-specs/pull/3307) [32:32]( https://www.youtube.com/live/tJULkA5YgP4?feature=share&t=1952) 

So, deflion did write a consensus layer spec and we associated it with the new EIP, EIP 6914 to reuse indices on the full suite. This, we brought up a call ago, um, and asked if anyone can take additional look in here, it seems like there's some design discussion points that we can still have and should have. But I wanted to get a feel for…a lot of this the intention here is to reduce the unbounded growth of the validator and balances list and I wanted to get a feel for whether this is urgent, whether we should consider this a couple of ? later…does anybody have strong opinions about if and where this should be placed and when we should take on this complexity, if we do? 

**Alex**
I personally would rather see 4844 just like shipped asap and it seems like this thing is complex enough that it would delay that. Maybe not, but that's just kind of my feeling. So in that case, I think that this is something that's promising and we can keep developing it. But yeah, I don't really see it going to the next hard fork myself. 

**Danny**
Yeah, we'll say there were enough discussion points on the original PR that it doesn't feel like we can click the button today, that this would be multiple, at least a couple of not three, four weeks of discussion and back and forth and then finally to get it to a good place. So under that lens, it also, I think that reinforces your opinion, but do others have opinions here? 

I think that do all the concerned clients think that this is this or something like this is must go in eventually, or is this just a nice to have even in the long term? So by not commenting…yeah, Sean?

**Sean**
I'm just going to say that I think we will need something like this. But I sort of feel like maybe not in this current fork. 

**Danny**
Okay. So. We will continue to refine this and continue to have discussions around it. But no one thinks that this is pressing enough to get into the next fork. Correct? Speak now. Okay. And also…

**Dankrad**
Yeah, I also want to ask here like it's I mean theoretically, it should be possible to get the same gains by simply forgetting about all validators if they haven't been touched for a long time, right? It's just like is is that just way too complicated to implement in practice or like. 

**Danny**
So one one issue here is that even if you're fully withdrawn, if you make even a one eight deposit, it goes into there and then it would be part of the withdrawal.

**Dankrad**
Yes. Again, so that would be a very like forget. Yeah, not fully. But there's like an ancient database of like all validators that you almost never have to touch. 

**Danny**
And then you need to at least know their pub keys or some sort of mapping there for the causes. Yeah, I think. Like one of the argument is to potentially trade some consensus complexity for the reduction of client complexity here. You know, there are probably management strategies in terms of caching for state recalculations. Probably some management strategies in terms of like shifting things around in and out of memory. If they're old to keep the state the active state size or the active value of their state size bound. My intuition is the same is that it's probably possible to get the gains through engineering complexity instead of consensus complexity. But then that has to happen five times. 

**Dankrad**
Well, I mean, the EIP says it has to be implemented 3 – 5 times.

**Danny**
Right. Right. I guess it's a, but it's a complexity trade off and where it goes. This feels simpler, but I do not have good eyes on that. But I think that's a very important. 

**Dankrad**
Yeah, I mean, that's why I would like to understand why why does this feel simpler because I don't understand. To me they are very close in complexity, but like, but having less complexes, consensus complexity at the same increase in client complexity seems strictly better. 

**Danny**
Yeah, I guess it would depend on the manager’s complexity. If they were equal. 

**Dankrad**
Yeah, exactly. 

**Danny**
I agree. If they're not equal and actually client complexity can lead to consensus failures, you know, for example, if this historic you know, these inactive validators that you kind of like keep out of memory and you know, and you, you mess up like your pub key, hit it, and then you make a new validator instead of adding a new deposit like that's a consensus failure. And so by having machinery that you don't even necessarily utilize much, that represents consensus risk as well on the on the consensus edge cases. And those are even hard to, these caches and I'll abuse that term. They're kind of hard to test in consensus tests because creating a state that actually would use the historic flows and sort of caches and tested in that like very state full manner. 

It's not obvious on how to do in like our consensus test against the execution machinery. So I can't make a full claim. My intuition is that this is simpler than some of the machinery in less aeropron. But I would have to have some engineers speak to that. If anybody, does anybody have additional discussion points here otherwise I think this is not going to go into Deneb, we will continue to refine and certainly have to have the conversation on the complexity trade off here. But can have that a little bit further down the line. 

#### [historic summaries backfill] [40:03]( https://www.youtube.com/live/tJULkA5YgP4?feature=share&t=2403) 

Okay. Another thing that we do not have a spec for but we would like to, presumably would like to do. It was kind of a follow on the historic summaries. The creation of the newest or summaries was to backfill on a fork boundary, essentially with a static list. To have them be complete from Genesis. This can happen whenever, the sooner it happens, the sooner we can standardize things like era file distribution in a simple way and other things like that. 

I think yossics probably one of the main proponents here and is not here and no way of a spec yet so I wanted to get a sense of if this is urgent item. Silence means I do not think it is urgent. Speaking up means I think it's urgent. Okay. I'm going to circle back with ? and can see if we can actually just get a future spec up. So we can have the conversation, but this does not seem urgent. 

#### [Not allow slashed validator to become a proposer consensus-specs#3175]( https://github.com/ethereum/consensus-specs/pull/3175) [41:25]( https://www.youtube.com/live/tJULkA5YgP4?feature=share&t=2485) 

Okay, another item that's sitting in a feature is to not allow slash validators to become a proposer. Essentially, if you're a slashed, you no longer can attest, you still get put into things…can attest. But there's a bit of a degenerate flow in that if you have a very large slashing, these validators get put into the exit queue, but they're still active and they can still be a composer. So if you had a 50% slashing, you'd actually have a 50% proposal rate at that point. 

The get proposal can be modified to not select slash validators. This is likely a relatively simple change. And it does have a spec. This is something that Kyle would like to at least open up for consideration for Deneb. And if not to highlight it as something valuable to get into the next fork. A sense of urgency to get into Deneb, again, it's like on the simple side of implementation. But it is a protection under, you know, a pretty high failure mode. Any client teams feel like this should be prioritized for the next fork? 

**Sean**
This one seems pretty important to me. And yeah, the diff looks pretty big, but the change seems like it should be relatively more simple. 

**Danny**
Yeah, let me take a look at it. Why is the diff big? Oh, because getting the proposer within the context of the block, because a proposer could be slashed within the block. You have to get it from the I think the inserted block. So essentially the call to get the proposer index because the proproser could self slash or anyone could be slashed during the execution of the block. You can't just repeatedly call get a proposer. You need to get it from a more static place, which is latest block header. 

And so anytime the proposer is gotten in any of these functions. Those functions are copied over and used. And you get the proposer from the latest block header instead. 

**Dankrad**
And easy solutions to just forbid self slashing right?

**Danny**
No, I don't know if it's only self slashing. 

**Dankrad**
Would it. 

**Danny**
No, you're right. But this is also this is a very, this is I would argue an easier solution. It's just that it makes the diff look big because all these functions are copied over to use the new get proposer. And so. Get latest block proposer index is inserted in each of these functions. And so it's essentially a single line change. That's pretty much not changing the functionality of anything. So I, yeah, I agree. I think Sean, the diff looks bigger than the actual because of that. Yeah, and we might be able to get clever and make the diff look smaller. 

**Sean**
Yeah, this one seems worth doing to me. 

**Danny**
Any other input? 

**?**
Yeah, I agree. Im in favor of it. 

**Danny**
Okay. Um, Mikael will clean this up and get test built for it. And maybe keep it in a separate future branch with tests. And in two weeks time, we can do the full thumbs up or thumbs down. It's about as simple as you can get because it never touches the engine API. And I personally, I think we, you know, we're going to always have a few pretty minor things that we want to get in. And so it's worth getting any minor thing. 

Okay. Any other items that people want to bubble up for consideration for Deneb? 

There is the attnet Revamp, although that can happen independent of Deneb. So we will discuss that a bit further down. And we will talk about that. As for the signature for ? Can you make sure…

**Etan**
Sure. I mean. We are still looking for the minimal changes to end up in this SSC world. And right now with, um, block TX type having changed to zero X3. Technically we have this problem that there used to be this, I think, starknet  thing where transaction type three was used for different kinds of signatures. So having something that makes sure that there can never be a conflict. That the same hash is signed with different meanings, depending on the network, could still be something that should go into Deneb. 

I mean it's mostly a conceptual thing, not an engineering thing to develop one of these. I think it was 6493. Yeah, 6493 EIP. Yeah, I don't need to discuss it right now in detail, but just keep it in mind. 

**Danny**
This is for transactions specifically?

**Etan**
Specfically for the block transaction type, the rest is already fixed right? I mean, those are signed the same across all the networks. But the block transaction type. Because it's based on SSC means that the chain ID is serialized at the different offset. So in theory if there is an RLP transaction type, it realizes the chain ID at offset zero, I think. Or offset 1 and then there is the SSC type that serializes it at a different offset. You could craft a message that is valid in both schemes and maybe tricks someone into signing it. I'm not sure if this is possible for the block transaction type, but it should not even be necessary to think about it with a proper signature scheme. 

**Danny**
Does this affect the consensus layer or if this is adopted on the excution layers and being opaque to the consensus layer?

**Etan**
This is only execution layer. 

**Danny**
Okay. So good for us to be informed about, but maybe something that happens on the call next week. Okay. Yeah, thanks for bringing that up any other, any comments on that before we move on? Okay. 

### Engine API
#### [State that payloadId should be unique for each PayloadAttributes instance execution-apis#401](https://github.com/ethereum/execution-apis/pull/401) [49:49]( https://www.youtube.com/live/tJULkA5YgP4?feature=share&t=2989)


We have one engine API point brought up by Mikhail. This is to state the payload, payload ID should be unique for each payload attributes instance. I believe there was an edge case triggered an issue that emerging here does anybody have like the TLDR on what drove bringing this into the spec? 

Okay. So Mikhail has had this up for a week. I believe at least some of the parties are already taking a look. If you are the engine API guy on your team, please take a look. I think this is likely to be merged before at the execution layer call in one week. Okay. Anything else on Deneb before we move on?

### Research, Spec, etc 

#### Consideration for RPC to validate beacon header [51:19]( https://www.youtube.com/live/tJULkA5YgP4?feature=share&t=3079) 

I have a placeholder from last week for the consideration for RBC to validate the beacon header to help with certain flows. Is this, we wanted to have a bit more thought and discussion on it between last week and last call and now. Is there any update on whether we do want that RPC and whether there's a likelihood of that being spec'd and put in?

**Sean**
I've been supportive of it. Yeah, I think on the last call I said I would write up a spec, but I haven't had time yet. I can have other people are similarly in support. It seems like something that like at least a few clients will have to implement and it'd be nice to have it standardized. But the other hand is like we're sort of expanding the scope of like what is the beacon API, like what sort of things do we support. 

**Danny**
Yeah, I think the argument was if this isn't supported, then people are going to fork clients to support it. And if one client supports it, then they will become a monoculture in some of the building relay. Okay, I don't think there's been any stronger arguments against other than the expansion scope I recommend we write this back and get some final thumbs up from client teams. Thanks Sean.

#### [Attnet revamp: Subnet backbone structure based on beacon nodes consensus-specs#3312]( https://github.com/ethereum/consensus-specs/pull/3312) [53:35]( https://www.youtube.com/live/tJULkA5YgP4?feature=share&t=3215) 

Okay, this is something I've been excited about for a while. Adrian Age can you speak to PR through one to the attnet revamp and the, I guess, a quick on what's going on here. How the strategy can be rolled out is this something that we need high coordination on or can it be done iteratively. 

**Sean**
Not sure if Age is on the call. 

**Danny**
I see his name. He has not spoken, but I do see his name. I don't know. Can't unmute. Okay. So, the motivation is right now the attnet field. One is honestly based. So you add the member of attnet's random at that's in relation to the overall edge running. And also leaks a lot of information. Obviously we leak a lot of information in all sorts of ways, but reducing information leak and not adding additional information lake is very important to further secure validator nodes. And the assumption that our subnets are probably much higher density than we necessarily need. 

What happens here in the attnet revamp is we take the PR ID and some. And we take the that's given a constant, which is the required number of attnets per full node gives us as a function of probably epoch gives us which attnets a peer should be subscribe to, the nice thing is if they're not we can call them dishonest and stop listening to them. 

And then we can also add a little bit of like enforcement here where we don't currently. And gives us the ability to kind of like tune the density based off of all full nodes, it also allows for every full node, I think like half the dht right now because there does not contribute to that nets so distributes that a bit more across all of notes. I need to take the look I believe that this is specified in a, oh hey. Well, Adrian now that you can unmute I believe. Can you tell us about how we can roll this out is this done in a backwards compatible way does this need to be done in a hard fork, etc. 

**Adrian**
Yeah, in principle, we can just do it. If its compatible, if everyone agrees that this is something we want to do. So we can just do it in stage releases as well like lighthouse could release it tomorrow if we wanted to. I guess mainly it's because it's not enforceable at the moment so anyone can kind of subscribe to whatever they like. So. Ideally, yeah, we can just have a client teams as they build it just to slowly release it and then the network will slowly shift to kind of a new regime.

**Danny**
Would lighthouse be downscoring peers that don't do this or would they would you turn that on later?

**Adrian**
Yeah, you would turn that on after a hard fork. Because then like once all the client teams have it and all of the, you know that all the nodes are on a particular version after a hard fork, then you can start. And peaceying and changing the way you do discovery. But in the meantime, you can just, you can just kind of addhoc implement it. 

**Danny**
And. And what's your confidence level and analysis and whatever that this is going to be. Give us the stability that we need to go and up running simulations or is it generally pen and paper on density and number of nodes. 

**Adrian**
Yes, generally pen and paper. So the main factor is the number of nodes, sorry, the number of subnet you subscribe to node. So we're trying to be somewhat conservative by setting it to two. And it will mean that like client teams are probably going to have to, because it'll be like a stack it upgrade as, as people upgrade their nodes. But client teams will probably have to have higher peer counts and probably monitor a little bit closely how they how they choose their peers to make sure that you have a stable set of subnets, save sort of peers per subnet. But I imagine it's tunable and it's not going to destroy the world. 

**Danny**
Okay, I've generally not heard much dissent on moving forward into this strategy and regime. That correct? Is anyone that feels like we should not be opening this can of worms and shouldn't be doing this. Other further discussion points that are not being highlighted on that PR? 

Not that we have the status, but let's call it in last call and that we're going to merge this by the next consensus layer call unless there are additional concerns and moving forward. 

**Adrian**
Yeah, it's worth highlighting that it's somewhat controversial as to how it's going to affect the networks of people that I guess doing network stuff on the consensus layer as well as having a look if you haven't already and getting a thoughts in. 

**Danny**
Okay, anything else on this one? 

#### Verge number field in json in engine api [1:00:03]( https://www.youtube.com/live/tJULkA5YgP4?feature=share&t=3603) 

Okay, we have a discussion point from Guillaume on the verge specification around the usage of a number field adjacent engine api. Guillaume. 

**Guillaume**
Right, yes, so exactly in the in the spec for for the verge like when we put the proofs in the blocks. There's basically a structure that's that is very nested with a lot of arrays and the same structure is repeated over and over again. And like this structure that is repeated is basically just representing a diff so it says this last byte, which is the suffix of the key is used to be this value before and now it's this value. And because this value, this type of structure is repeated a lot in the in the structure. It feels a bit wasteful to encode it as a string and from what I understand currently in the in the CL specs, every number is supposed to be encoded as a hex string. 

And I understand the origin of this requirement was that there is some GS library that does not handle some yeah exactly some GS library does not handle like big numbers, but this is a byte. So it will always be a value between 0 and 255 and I don't know it felt a bit wasteful. So I wanted to know if there was a possibility to change the specs so that only large value values are encoded as strings but smaller values that are always bytes could be encoded as numbers. 

**Danny**
So I think the guy would probably have most input here he did say we can use Jason entry type of this field implementation complexity should be trivial. And I can't remember the exact history of the libraries that were causing the issues here. What are what are a couple examples of the number fields that were putting in hex that are a bit strange right now like all of the base V and that kind of stuff. 

**Guillaume**
So I am from one I just that came from a discussion with Mac, my understanding is that everything should be in the trying spec everything should be should be encoded as a hex string. And so yeah, that's true of the true of every of the base V for example, but yeah, even smaller numbers should they should exist, like the block number that could perfectly fit in any integer is also encoded as a hex string. 

**Danny**
Is that the case because I am looking at the like execution payload V1 under the specs and I'm seeing things labeled as quantity what is that type?

**Guillaume**
So are you asking?

**Danny**
…have the familiar here. Anybody have the familiar with how quantity is encoded. And that's like a json common json type that we're leveraging there, not something we made up?

**Guillaume**
No, its a string. 

**Danny**
Yeah, I meant the parsing and encoding and definition of that string is a common like. And then I think that's a question here, I would imagine that you make the PR to the engine API. It would get a bit more discussion. I also, I guess just to point out like this API is, you know, optimizing a byte or optimizing a number of bites is probably not going to like make or break this other than just like the aesthetic nature of what we want out of it. Right? And then it's not going to be broadcast to the whole network, right?

**Guillaume**
Yeah, its mostly cosmetic. It also depends its not gonna make things noticeably slower. Its just a feeling that its wasteful.  So if you say it's a quality, it isn't coded as a string. So yeah, just wanted to write I just I just checked. No, yeah, okay, I'll create the PR then and see if there's some pushback. Yeah, if no one else has anything to say that's enough for me, thanks. 

**Danny**
Yeah, anything else on that. Great. Okay, let's see. So that is the end of the agenda. Are there any other discussion points or closing remarks for today? Yeah, and thanks Mario for linking directly to the encoding. I can see that initially. Okay cool. Good luck on devnet 5 and talk to you all very soon. 

Participants say thank you and goodbye. Meeting ends.

## Attendees

* Danny Ryan
*  IHavenothingToSay
* Marek Moraczynski
* Etan (Nimbus)
* Trenton
* Adrian Manning
* Terence
* Guillame
* F
* tim
* Ben Edngington
* Anton Nashatyrev
* zahary
* sean
* Gajinder
* James He
* Mike Kim
* pari
* Roberto B
* Andrew Ashikhmin
* Ben Adams
* Dankrad Feist
* stokes
* pop
* dhruv
* Mario Vega
* Pooja ranjan
* Peter Szilagyi
* Hsiao Wei Wang
* Ruben
* mrabino1
* Enrico Del Fante
* Fredrik
* zahary
* Crypdough.eth
* Matt Nelson
* Tomasz Stanczak
* Fabio Di Fabio
* Justin Florentine
* lightclient
* dan (danceratopz)
* Mehdi Aouadi
* mike neuder
* spencer (EF Testing)
* Mario Vega
* Soubhik Deb

