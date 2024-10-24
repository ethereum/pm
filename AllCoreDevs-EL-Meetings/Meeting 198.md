# Execution Layer Meeting #198
### Meeting Date/Time: October 10, 2024, 14:00-15:30 UTC
#### Meeting Duration: 77 min 
#### [GitHub Agenda](https://github.com/ethereum/pm/issues/1163) | [Ethereum Magicians Post](https://ethereum-magicians.org/t/all-core-devs-execution-acde-198-october-10-2024/21314) | [Video](https://www.youtube.com/live/YQwdKE0d8LI?t=61s)
#### Moderator: Tim Beiko
#### Notes: June 
<br>

| S No | Agenda | Summary |
| -------- | -------- | -------- |
| 198.1 | **Pectra Contract Audit RFP** | Pectra Contract audit RFP
| 198.2 | **Pectra Updates** | devnet-4 specs: CL spec release: v1.5.0-alpha.8, 7702 eth rpc schema, BLS precompile pricing and remove MUL precompiles?
| 198.3 | **Pectra Updates** | devnet-4 launch timelines
| 198.4 | **Pectra Updates** | Public testnet name
| 198.5 | **EIP Discussions** | [EIP-7623](https://github.com/ethereum/execution-specs/pull/966)
| 198.6 | **EIP Discussions** | [EIP-7783](https://github.com/ethereum/EIPs/pull/8933)
| 198.7 | **CL Discussions** | Add EIP: Reduce Slot Time for Lower Peak Bandwidth EIPs#8931
| 198.8 | **CL Discussions** | https://github.com/ethereum/builder-specs/pull/101/files#r1778224447
| 198.9 | **CL Discussions** | Staking bandwidth considerations [(context)](https://github.com/ethereum/pm/issues/1163#issuecomment-2379336862)



 
### 198.1 | Pectra Contract Audit RFP ([:60](https://www.youtube.com/live/YQwdKE0d8LI?t=61s))

**Tim**: Welcome everyone to ACDE #198. A bunch of pectra related things today then some EIP updates and new EIPS to talk about. 
Then if we have time there's a couple more CL-related topics that were also put on the agenda. 
Before we get started, we have this request out for audits for the Petra system contract so
the proposals are closing tomorrow. If there's anyone who still wants to submit their proposal, this is your last day (today and tomorrow) to do so.
I posted the link in the chat here but it's also on the agenda.
<br>

-------------------------------------
### 198.2 | Pectra Updates ([1:50](https://www.youtube.com/live/YQwdKE0d8LI?feature=shared&t=111))

**Tim**: On Pectra itself, I believe there's a CL spec release for devnet-4. Any other updates on overall readiness?

**Barnabus**: Hi everyone, I'm taking over for Pari while he's on holiday. For devnet-4, we have a the spec list right [here](https://notes.ethereum.org/@ethpandaops/pectra-devnet-4)-- I just linked it in. We have a couple more open issues that we should probably discuss during
the call today, but it looks like we managed to close quite some PRs throughout the past week, so I think we should be good to go. 
We also had alpha 8 released just yesterday.

**Tim**: Let's go over the issues now. I know maybe BLS was already on the agenda, but do you want to go over the ones you think are most relevant right
now?

**Barnabus**: We had the update the [submit pool attestation V2 endpoint / 472]((https://github.com/ethereum/beacon-APIs/pull/472)). We haven't got an update on this in a while so I would just like to make sure that we want to include this. If we do then maybe you can merge that in.

|| **Chat**
- stokes: I believe not


**Tim**: Alex are you saying that we do not want to merge this in, basically?

**stokes**: Yeah, for 472. So I think for this it's for a different CL PR that we at least said we would put into a later devnet.

**Tim**: Okay, so we can emit this one from devnet-4? 
stokes: I'm pretty sure that's what's going on okay. 

**Tim**: if we scroll down for future devnets, on the CL spec, we have this one. So I think we're good then on the CL spec and Beacon APIs, unless I'm missing
something?

|| **Chat**
- snflaig:	first CL spec should be merged for this?
- Barnabas:	cl spec has been merged
- Barnabas:	alpha 8 is the target
- stokes:	#3900 is open
- stokes:	That’s the paired CL PR
- nflaig:	https://github.com/ethereum/consensus-specs/pull/3900  is not merged
- Barnabas: ah right my bad

<br>

**Tim**: On the execution API, lightclient already put this one on the agenda but the [pull request 575](https://github.com/ethereum/execution-apis/pull/575) on the execution API. Lightclient, do you want to give some context on that one?

**lightclient**: I think Pelle has been working on this, I don't know if you wanted to just quickly mention the changes?

**Pelle**: Yeah I can screen share too if you need, but it's essentially the same as 4844 minus the blobs and plus the authorization lists. The link is in the agenda as well.

**Tim**:  I guess given this is an execution API scheme, do we want to block launching the devnet on this?

**lightclient**: I would say that we need to get the 7702 changes Upstream to a few places before we can merge this, so I would not block on it, but clients should be aware of the scheme and this is a good time to raise any concerns with the formatting right now.

**Tim**: Okay, anyone have comments now? Otherwise we can point people there to review asyncronously.

**Tim**: It seems like there's a CL PR that was marked as merge but isn't: [Separate type for unaggregated network attestations #3900](https://github.com/ethereum/consensus-specs/pull/3900). I don't know if we have the right people here to make a call about this one, but any updates or things people wanted to flag? Is this something we want for devnet
4?

**stokes**: No. This is the one that was paired with 472. This is change to the attestations along with 7495? Anyway, the attestation EIP in Pectra, this would go with that. But when we discussed, this might have like more code change than it appears and then we want to evaluate that against timelines for Pectra. so what we said was, we'd give another ACDC cycle for client teams to take a look. Point being, it would at least be devnet-5, definitely not devnet-4.

**Tim**: Okay, sounds good.

And then, on the EL-side, there is one last open PR, [8949](https://github.com/ethereum/EIPs/pull/8949)). That changes a bunch of EIPs based on how we adapted the request format. lightclient, any more context you want to share on this?

**lightclient**: I don't think there's anything that people care about here, other than just making the request eips match the new formatting for 7685. Before, request
data referred to a single request and now we're using request data to refer to the output of the system contract, so that's just updating that. The other changes have
already been made to all the EIPs for the devnet so this is not really changing any behavior.

**Tim**: Okay, so we can get this merged in the next day or so if there's no comments on it?

<br>

#### 7702 eth rpc schema [(11:22)](https://www.youtube.com/live/YQwdKE0d8LI?feature=shared&t=682)

**lightclient**: There is some changes to 7702 in the last couple days. One of those was uh fixing up the serialization for 7002 authorization to pull elements. We restricted the sizes to the values that we had previously discussed, but one thing that sort of fell out of that was that we had a serialization requiremen. Previously the s value has this EIP 2 restriction where it has to be on the lower half of the valid range and this exists in transactions today to avoid this transaction hash malleability. We sort of just pushed it into the authorization list because that's how we typically do signatures. I didn't necessarily intent to remove it whenever I updated the spec--my intention was to keep it--but it opened the question and Kim mentioned that it doesn't seem it's necessary to have this check for the signature in 7702 for the autorizations because you don't have the same transaction malleability issue. If you were to change it to be the same valid signature just on the other end of the range, then it would actually change the entire transaction hash, just on the outer EOA to re-sign, etc. All this to say, I'm indifferent to what we do here. I think if people have any feeling one way or another, I'm happy to go with it. I just had the intention to keep the bound check on it because that's how transactions are typically signed and verified against. The reason that it exists for transactions is not necessary for here, so the question is do people want to be consistent with transactions or is it okay to have it slidely different and closer to EC recover, as it is in the precompile.

**Tim**: Anyone have thoughts? Comments about this? 

If not, should we move this conversation to the R&D discord and maybe give more people time to think through it?

**lightclient**: Barring any comments here, I'm just going to add the check back in since that's how tests are and if anyone has any feeling that we should change it for devnet-5, let's do it, but I don't really see a reason to block anything else related to devnet-4 on this.

<br>

#### [BLS precompile pricing](https://ethereum-magicians.org/t/eip-2537-bls12-precompile-discussion-thread/4187/81) and [remove MUL precompiles](https://github.com/ethereum/EIPs/pull/8945)? [(14:58)](https://www.youtube.com/live/YQwdKE0d8LI?feature=shared&t=898)

**Tim**: Okay so while we're talking about spec changes, there were some updates around the BLS precompile pricing saying that there were some mul precompiles are still underpriced and a PR opened to potentially remove them. Do we have the author on the call?

**Paweł**: These requests are not actually related. The biggest issue we have is that the gas price for multiscalar multiplication, one of the precompiles in BLS doesn't fully match the reality of how the implementation works. To my understanding, this is because this discount to the multiscalar multiplication, some like table says how cheaper this is supposed to be based on the number of points you get in the input, it kind of makes the general costs trend sublinear. But, at some point, which to my understanding that was done after this initial gas cost were
proposed, we also added a subgroup checks for the inputs, which is kind of linear factor because you need to do the check on every point. This linear factor relatively quickly dominates the total cost. To my implementation which is based on  BLSt library, around 100 120 points, like half of the time is spent on the subgroup checks of the input and the other half is actually spent on actually doing computation. 
I think there was number of discussions in a number places about whether we need this subgroup checks and there a number of opinions. I don't have strict opinions about it, but I think that's like the the most pending issue we should resolve. 

**Marc Harvey-Hill**: I can speak for Nethermind on this. We ran some native C# benchmarks and these had much lower variance than the state tests and they also agreed with the results that the MSM precompiles seem underpriced, but without the subgroup checks they seem okay. I think one possibility is to increase the cost of the normal MSM check and then have an alternative version without the subgroup checks. I think in a lot of cases you might already be confident that the points are in the correct subgroup so you don't need this overhead, so we could have a cheaper version of the precompiles without the subgroup checks. This would be sort of like an an unsafe version as if you did call it with points from outside of the subgroup it wouldn't be guaranteed to have the same result. So you'd have to be careful about when you use this version.

Also I saw that evmone team made another proposal to remove the multiplication precompile. Generally, we would also support this as it's just redundant as the same functionality is covered by MSM. If we were to add a non-subgroup check version then this would just simplify things a bit and we wouldn't have to add even more precompiles. We'd only have to
add two for MSM and the pairing.

**Gary**: From a Besu perspective, we did a lot of benchmarking, specifically with the proposed discount table bump and with subgroup checks. We found that when we're using Pippengers, the discount table gives us a pretty flat price distribution across different pair counts, but we did find that G1 MSM was still underpriced and G2 MSM is overpriced, at least in comparison to EC recover. So in order to kind of bring those into parity with EC recover, we found that bumping the multiplication cost from 12 to 19 on G1 MSM brought that in line with EC recover and dropping the G2 MSM multiplication cost from 45 to 33 gave this almost flat parity with the cost of EC recover.

One other thing about removing MUL, one of the idiosyncrasies of our implementation is that we initially started with a non-Pippengers version of MSM and found it for single pair counts or low count pairs that we it actually performed better than Pippengers. So if we removed MUL, I think what we probably would do is intercept the single pair count MSM and not use Pippengers specifically for that. But it seems like we could remove MUL and the notion of having a non-subgroup check version seems like maybe we could reuse those pre-compile addresses for a non subgroup check version.

**Potuz**: An advantage of having the separation of the subgroup check and the linear combination is that there's different safety stretch-hold that you you may have in an application. Some applications may not need at all and even those that do need there's two scenarios: you either need to check for every one of the points that you're summing up or you need to check only one that you're adding, so it means that you can check on the total sum and be fine or check independently each one of them and be fine. I'm sure there's application for all of these things, I don't see any reason not to include them separately.

**Gary**: That's an interesting notion you're saying like have a G1 and a G2 subgroup check precompile?

**Potuz**: Yeah, just have them separately and then anyone that actually needs to call this linear combination with the separate check, just check it. There's some that might want to check it before doing the linear combination and some that might want to do the check only after and just check the sum. This is something that is actually happen happening on the CL. There's a lot of times that we have a linear combination that we don't do the the separate checks at all.

**Tim**: Okay and then there's some comments in the chat about maybe we could do this as an input to the precompile, so either it has the subgroup checks or not. Then whether or not we want the same number of precompiles. I guess my sense here is overall there are still things to figure out on this, so I would lean towards potentially not making these changes for devnet-4, unless someone feels it's urgent to do so. I think if we can try to work out the spec on this in the next couple weeks, we shouldn't block devnet-4 on that. 

One question I have is like what's the right next step here? Do people just need more time to review this? Should we have a call specifically focused on this and trying to go more into the details? Any strong opinions there?

**Radek**: There is a one additional thing to add here because this subgroup check now guarantees that you can use the additional optimization in the algorithms, which is the using of the endomorphism. If we remove this subgroup check, not sure what would be the results for this kind of algorithm when the points are not guaranteed to be in the proper group. This is something, which should also be considered here.

**Marius**: I think the issue there is that different libraries might implement different algorithms for this. If the behavior is undefined, if it's not in subgroup, then that might lead to some consensus issue at some point because they behave differently. We might not know 

**Radek**: Exactly, but on the other hand, from the benchmark it looks that these precompiles are kind of useless for many points because the cost of the subgroup check. Exactly the case, which Potuz already mentioned about algorithms, which by design guarantee that the input is in the proper subgroups, don't need the check. So in these cases, these precompiles won't be useful but I don't know how exactly this precompiles are going to be used. 

**Kev**: So I think the subgroup check is mostly useful for the G1 mul for MSMs. Most implementations I've seen don't use this optimization that we're talking about, just because it's
not that useful after a certain threshold. If we don't do the subgroup check, then G1 mul would probably increase by a 2X?

**Tim**: There's a comment in the chat by Alex about potentially having a breakout if we can get all relevant people on the same call. Would it be realistic to try and do a breakout on Monday either before or after the testing call? If not, potentially making that the focus of the testing call? 

Okay people seem to be available at 15:00 UTC so let's do 15:00 UTC Monday breakout on this. I'll put up an agenda for it right after this call.

Is there anything else before we close off here that people feel we should discuss on the BLS pricings or additions or removals of
contracts? 

Okay so let's try to iron this out on Monday and then we'll see how big or large of a change it is that we need to do. Thanks everyone for spending time looking into this over the past couple weeks. 

I think this was the last devnet-4 spec issue and then we'll see whether not we add this based on complexity, but is there anything else around devnet-4 specs that people want to chat about?


-------------------------------------
### 198.3 | devnet-3 ([10:36](https://www.youtube.com/live/YQwdKE0d8LI?feature=shared&t=636))

**Tim**: Okay if not, devnet-3. We're not finalizing right now. Anyone have contexts or things they want to bring up around this?

**Barnabus**: We're running an older version of Geth deploying the new version now and seeing if it will recover. 

**Tim**: So Geth was the only one that had an issue?

**Barnabus**: Yes

**Tim**: It was like a super majority of the devnet?  

**Barnabus**: It is barely over 30%

**Tim**: Okay, I see.

**Barnabus**: We have some other validators that are also not attesting and that's why we just went under finalization. Geth on its own shouldn't have broken the network.

**Tim**: So the other validators, we need to figure out what the issue is there with them?

**Barnabus**: EthereumJS is the other one that is not able to follow the head of the chain, but that is known. We're going to exit those validators and we have some big deposits that we had made in the beginning of the devnet and we're going to exit those validators also. So, we should be able to reach very close to 100% participation.

**Tim**: Nice. Is there anything else we want to be testing on devnet-3, aside from this Geth bug fix or, assuming that works, are we happy with things we're at and ready to shift our focus to devnet-4? 

**Barnabus**: I think we should be good to go to proceed to devnet-4

-------------------------------------
### 198.4 | devnet-4 launch timelines ([10:36](https://www.youtube.com/live/YQwdKE0d8LI?feature=shared&t=636))

**Tim**: In terms of implementation--BLS aside because that's still an open question-- I'm curious how much work the teams feel they have to do to get to readiness for devnet-4. 
Mario, maybe if you want to start with a testing update?

**Mario**: Of course. All the spec changes that we needed to test are ready, so it's just a matter of whether we finalize the changes to the test. 
That should be done today or tomorrow. At the moment, EthereumJS is working on an updated version of the transition tool interface, which will help us to fill the test. 
I think a release for the devnet-4 fixture should be possible for tomorrow.

**Tim**: Amazing. And then Geth is saying a couple days for them in the chat. So, again, taking BLS aside for a second, but assuming we made no changes to BLS, would it be possible to try and launch devnet-4
before next ACDC or does anyone think that's unrealistic? 

Okay, let's try and aim for a pre-ACDC launch date and then see Monday if there's any big BLS changes that we consider urgent. 
Otherwise, it might be worth just trying to ship devnet-4 next week and then deal with BLS in devnet-5.

**Barnabus**: Could we actually just freeze this back in this call maybe and agree that we're not going to do anything with BLS and if we do something with BLS then that would be in devnet-5?
That way teams can actually be ready by next week?
Tim: I'm happy with that. Anyone have any objection here? 

/Point clarification: Not talking about removing BLS; just leaving as is. Any engineering work towards BLS goes towards devnet-5./ 

**Tim**: Okay so let's consider devnet-4 spec frozen and try to get it live before ACDC next week, and then we can deal with BLS in the next devnet. 

As we start talking about devnet-5, there was this idea brought up a couple weeks ago that we'd want to do like a longer-lived Pectra testnet. 
I don't know if we want this to be devnet-5 or maybe it'll be what would be devnet-6. 
We can see how this evolves, but there is a thread on EthMagicians to try and set a name for it, so I think in the next couple weeks, once we finalize the spec for devnet-5 and decide whether or not we want to make this the long live testnet, we should find a name for it. 
Please visit this thread, but I don't know if there's any other thoughts comments on that.

**Barnabus**: Ideally, we also want client teams to make a release for this, so the public can easily sync up this chain. I'm not sure if this is reasonable, but I think it would be nice to have.

-------------------------------------
### 198.5 | Public testnet name discussion ([2:50](https://www.youtube.com/live/HJ9WxAOwTTA?si=Q6RpLK4xTwUNwCPt&t=170))

**Tim**: Okay. There is a comment from Alex saying devnet-4 should be "Moodeng." Let's see how devnet-4 goes and then if there are any issues we can address that.
My arguement for the BLS changes being in the public devnet is if we do something like change the precompile, like remove some or split the subgroup checks out as separate precompiles and stuff like that, there might be value in having that in public devnet if people want to test applications against it.
So, if there is something that is going to change how you'd interact with the BLS precompile, and we think that's important for the community to test, then we should probably try and include it.
If it's just gas pricing, I agree it's probably not the end of the world, but we don't have to make this decision right now.

**Stokes**: I agree, but I'm also just thinking that I think it would be best if "Moodeng," or whatever we call this testnet, is stable for the community. 
I wouldn't want to launch devnet-5 a few days before Devcon and then find issues and it's chaotic.
I think timing-wise we'll have a better chance of having devnet-4 be nice and stable.

**Tim**: I do agree that having it for Devcon would be nice because we'll probably cancel a couple All Core Dev calls during Devcon and a majority of us will be traveling, so
being able to ship off something that's relatively stable either right before or right at the start of Devcon, means that for the couple weeks there might not be as many new devnets going live.
At least there's something for the community to test. So I think that might be the right approach, working backwards from what can we ship before Devcon and then if the BLS changes make it in, great. Otherwise, we just don't include them there and have something stable.

Okay sweet, I think that's everything on Pectra. Anything else that people wanted to discuss that we didn't get to?



-------------------------------------
### 198.6 | **EIP Discussions** | [EIP-7623](https://github.com/ethereum/execution-specs/pull/966) ([37:25](https://www.youtube.com/live/YQwdKE0d8LI?feature=shared&t=2245))

**Tim**: Okay then, EIPs. Toni had an update to 7623. Toni, do you want to give a quick overview of that? 

**Toni**: EIP 7623 increased called data cost. Based on the feedback I got from Tanish, we changed that we don't deduct the intrinsic gas cost before execution.
Now we instead just check if the transaction sender is theoretically able to pay the floor cost. 
You can find all the changes in the execution specs PR. So far, I heard that Reth and Nethermind have already implemented it.
I think Marius was also implementing it and also curious how it is going at Erigon. 

**Tim**: Any comments about this from implementers?

**Marius**: I've not implemented the latest spec. Soon.

**Tim**: Anything else on this? 

-------------------------------------
### 198.7-8| **EIP Discussions** | [EIP-7783](https://github.com/ethereum/EIPs/pull/8933) and Reduce Slot Time for Lower Peak Bandwidth EIPs#8931 ([39:07] (https://www.youtube.com/live/YQwdKE0d8LI?feature=shared&t=2245))

**Tim**: Next up, there were two new EIPs proposed in the past couple weeks that tried to address similar issues around resource consptions. 
First there was one proposed to reduce the slot time and then one that was proposed as a non-core EIP to adjust the gas limit programmatically.
Slot time one, although it was like the first proposal, it is kind of a CL thing, so it probably makes sense to discuss the gas limit one first even though it came after.
Let's just open this up and be mindful that there's these two proposals that are somewhat related.
Giulio, do you want to start with yours? 

**Giulio**: First just to give an introduction to what this EIP does: it's basically just another strategy to adjust the gas limiting client. It doesn't add any hard fork, it just makes it so that with certain parameters you can set your proposed gas limit to increase over time with a cap at some point. The reason why I wrote this was first of all to address some of the problems that were with the the slot time reduction and also because one of the main issues that most people have with increasing gas limit is the uncertainty of potential bugs coming up due to the increase. An example of this is the 413 status code incident, which if we increase the gas limit to 40 million, we would probably have had issue in the chain because then the blocks would have been too big on for mainnet. This type of issue is something that you cannot really predict either, so this EIP mostly tries to decrease the risk related to the actions of increasing the gas limit. It doesn't really help to scale anything, but it does reduce the risk significantly compared to a fixed gas limit strategy, which is now employed by clients. It also addresses some problems that slot time reduction has. For example, the fact that it has to go through the CL and doesn't have a hard fork, it's also simpler. 

I think that the drawbacks can be discussed when the other EIP will be discussed.

**Tim**: Let's maybe do. Let's have Ben share his EIP and then we can take questions and conversations about the set of them.

**Giulio**: Sorry, I just want to say about this is that this, of course, is to increase the gas limit in the short term, so maybe it's also better to get a vibe check of that too.

**Ben**: Mine was in response to Vitalik suggesting that, without peer-das, we increase the blob counts. The idea was that if we speed up the slot time, we increase the blob counts and we increase the gas limit also. But without increasing the block size that any individual block producer or validator has to deal with. For both the EIPs, one of the concerns is what about history growth? what about state growth? State growth isn't pressing immediately, but for history growth we obviously have 444s or 44s, but due to blobs the amount of calldata that's being posted has decreased significantly, so the history growth has also decreased significantly. So we do have some safety margin that wasn't previously expected. That's the summary mostly. 

**Tim**: There's a comment saying that the state size does matter if we do something like verkle or if we transition to a new type of structure for the trie. But yeah, any other thoughts or comments on these two EIPs?

**Guillaume**: Sorry, just to comment about verkle, mandatory comment about verkle: the state size matters before we do the transition. After that. not as much, but before it does.

**Tim**: Let's start with the gas limit one. How do people feel about 1. the overall idea of potential increase and 2. if we were to do an increase, to have the increase be programmatic rather than a one-time number that we propose? Obviously this is something that every validator decides, but there's a difference of the default if all of the client software moves from 30 to 40 million.

Wow after like four days of the Discord being completely flooded with this, not much interest on the call. 
Bigger problems right now than raising the gas limit.

If no one has thoughts on this we can continue discussion async.

**lightclient**: I feel like we've committed to increasing the scalability of Ethereum through blobs, so we need to focus on getting higher blob throughput out there.

**Giulio**: But blobs and gas limit kind of works on two different axis. Blobs are capped by bandwidth, while gas limit is capped by storage--they are two different dimensions. 
If you increase the gas limit, you're not going to increase the bandwidth required by that much because most of the bandwidth right now is from blobs.

**lightclient**: I'm not saying that they're addressing the same thing, but we have sort of made a commitment as an ecosystem that we want activity on L2s and that means that we need to increase
the throughput for activity on L2s, not necessarily on the L1.

**Giulio**: Well, but it's nice to have on L1, isn't it as well?

**lightclient**: Yeah, and we should address it after we finish the things that are the priority right now.

**Giulio**: But my point is that it can be done in parallel because if it doesn't get in the way of priority, why not make it in parallel?

**lightclient**: Because we don't have the ability to do things in parallel. We can barely ship this fork that we're working on right now.

**Giulio**: But this is kind of a trivial change, it doesn't even require a hard fork.

**Tim**: It does require testing and analysis...

**Giulio**: Yes it does, but it's not something big, like blob increase. Because blob increase does require a lot of time right and also seconds per slot require time to test.
This just make sure that every client returns the same number on every client during a devnet, which can be done in parallel with devnet-4 for example.

**Tim**: I think one one thing about this proposal as well is that a lot of the concerns around blob increases is that we have to wait for another hard fork, which will take six months or more.
You could imagine doing something like this right after Pectra. If we actually think that we are bandwidth constrained in the next couple months and we want to maintain our focus on shipping
Pectra, or even when we put out the mainnet client releases at this point we expect clients to be effectively done with the Pectra work, this is something we could literally ship the week after that.

**Giulio**: Another thing is that, again, this is not really that big of a change. But I saw that Stokes said that it's actually riskier. I don't know what he means by that though.

**Stokes**: I haven't looked at this exact EIP yet, so maybe I'm missing something, but the concern is just that if we have some automatic increase schedule, it could be very hard to stop the automatic increase.

**Giulio**: No, you can set a cap, it's not infinite. It's written that there is a cap and after you reach to say 40 million, it stops. Of course if you change the defaults yourself it's going to increase, but the same can be
said by the current fixed strategy. 

**Tim**: So actually, a way to frame this could be that we are expanding the bounds.

**Giulio**: Right, but I think overall, this is just an improvement upon the current strategy, so if anything it should be treated as just a nice improvement to have and eventually to bump up the gas limit. 

**Potuz**: I just wanted to echo what Giulio just said. I'm not advocating for increasing or decreasing or anything on the gas limit, but this EIP seems to make it safer actually than
the way that we currently have of increasing the gas limit. If we decided as a community to go, and we get people that are ramped up and we get validators to move to 45 million for the gas limit, then it would start immediately increasing at the maximum level. We might find out that that it's hard to do and getting back from that is much harder than if we do this at a slow pace, as this EIP is showing. So I actually think it's safer than the core mechanism, not more dangerous.

**Giulio**: I also would like to have a stronger response. For now, I have just heard from Geth and Nethermind. Nethermind seems to be okay with raising the gas limit.
Geth seems to say what lightclient said. But other clients, like Besu, I'd like to hear their opinion too.

**Ameziane**: As I shared on on Discord, we have these two EIPs decreasing slot time and increasing block size. As I said on Discord, decreasing block time seems more CL concern because currently from the metrics I've gathered, we have 5% of the block that arrive after 3 seconds. So we could have attestations missing and maybe block reorgs, so this is more on the CL side and if we're going to keep the 4 second window on the EL side or we're going to review it related to this 8 second. On increasing the block size, there are different areas we need to check here. In terms of block processing, there is no issue. On Besu side, we have a few EVM or precompiles that are slower than other clients that we are currently addressing, but this is on a per second basis.

In terms of bandwidth, solo staker requirements, storage-- I believe we need more testing to know how it's going to behave. My first feeling is to say we are for increasing block size because this is something we already have on L2s. Not exactly on the block size but we have similar configuration on L2s that work very fine, even if it is less decentralized.

So maybe, 'yes,' but for more testing. As I said in the discussions, in a gradual way seems to be the right way to do it.

**Giulio**: If you increase gradually, you also don't have most of these problems. The moment you see that solo stakers cannot stay their computational, you can just alt it. You can just make it release or even set it lower because in the EIP I state that you can still use the fixed gas limit option and it will overwrite the option

**Ben**: One of the advantages with increasing the block size versus increasing the slot time is that increasing the slot time does increase the number of consensus votes that happen, whereas block size has no effect on the consensus layer in that way.

**Giulio**: Right. Also, I did some research around how the block size increase actually affect computationally and the bigger the blocks, the faster actually transactions execute. So actually if you execute a big block, it will actually take on average less time per transaction than for a small block. I think Erigon is not the only one that is like this, by the way. 

**Tim**: This is clearly something people have opinions on.

**Giulio**: Sorry, I was reading the chat. Barnabus said that there is more bandwidth, but in reality the block bandwidth is very low, it's like 70 kilobytes per block and a blob is like 128 kilobytes, so if you increase the block size by 50%, you have like a quarter of a blob. It's really not like a bottleneck on the bandwidth. It's not going to be significant. 

**Potuz**: It's true that the decrease of the slot time is better discussed in the CL meeting. There are a lot of problems on the CL if we were to adopt something like this, it's not trivial at all. But there's one component that is on the EL, which is does it break contracts or not? There's currently, you could you have a linear relation between block height and time stamp. We would break that. This is a breakage at the EVM level so this is something that you guys should discuss.

**Marius**: We didn't have that relationship before the merge.

**Potuz**: Right, but there's contracts that can be right now using this.

**Marius**: There was never the stated thing that we are never going to change the block time. This is not an assumption that we ever made, so developers that relied on this assumption kind of make that assumption on their own. It's not our fault in my opinion.

**Ben**: There is a time parameter for the block, so they should be using that rather than the block number. 

**Tim**: I guess if we were to do this change, we should definitely look at it on chain. I'm not saying that we should posit based on this, but there's a difference between a handful of random contracts and some large and well-used contracts have this bad pattern. I think that's unlikely but it's definitely something we'd want to be sure about if we were to change the slot time.

**Giulio**: Since I have some experience on the CL side, I can kind of give some feedback very quickly on the slot time and my concerns about it. My main stance is that it's probably a good Improvement overall and it's probably going to happen eventually, but it probably should not happen now because the biggest problem with solo staking is bandwidth and this will not only increase the gas limit, but also the blobs. It will increase the bandwidth requirement. After talking to some solo stakers and the guys from DVT, they told me that it will be very punitive to have an increase in bandwidth. Another issue with this is that it will get in the way of research on single slot finality because the times there actually matter. Currently one approach actually does is kind of reliant on time of the slot time, so I wouldn't really do this upgrade before single slot finality, if anything. Also you need to consider that maybe you need to adjust some economic incentives with the CL because now validators will have more money per year and more ETH will be issued, so you need to also think about that.

**Tim**: We can follow this conversation on the CL call next week, but agreed we should consider not just "can the protocol support this today?" but "are there future changes or things that
would be complicated by changing this slot time?" 

Anything else on either of these topics? It doesn't seem like there's an urgent decision to be made here and there's clearly more conversation to be had, but is there anything people feel we should address on this call?


Nice, devnet-3 is close to finalize again, but there's maybe some Lighthouse issue, so we'll take a look at that.




-------------------------------------
### 198.9 | https://github.com/ethereum/builder-specs/pull/101/files#r1778224447 ([1:01:15](https://www.youtube.com/live/YQwdKE0d8LI?feature=shared&t=3675))
**Tim**: Ok, moving on from this. Alex, you had the PR on the builder spec that was also kind of CL related but you wanted to bring up if we have time.

**Stokes**: This is back to the request structuring that we've been talking about and where we landed for devnet-4 was that the engine API would send, essentially, the serialized list of bytes. 
We kind of have the same question to answer in the builder API. I guess I was just looking for feedback on any preferences people would have. The most natural thing to do based on how the builder specs work is to use the Beacon APIs do and then in the Beacon APIs, we have this full JSON structure of the request, rather than this more compressed serialization. It was a question, do we want to mirror the engine APIs or do it this other way? I was curious if anyone has any thoughts on how to handle it here?

If there's no feedback, I'll go with what I had right now, which is essentially to have-- again, following the Beacon APIs, which has like the full JSON structure. The downside to this is that, as a MEV builder, you'll need to get your transactions, which in some way will sort of emit the request data, then that request data will need to be put in the right format. It will require a little deserialization, but that's that's how it works.

**Potuz**: Now, probably for the CLs, but this is bandwith dependent, right? So this is adding latency on the builder path. I wonder if we cannot just blind it? The builders can themselves compute the HDR that we're going to put in the block body and signed over, then we just trust them that they include the right 
requests since we're trusting them on the transactions anyways.

**Stokes**: The issue is that the proposer will need the request to actually execute the state transition, which they need to sign over the blinded block.
 
**Potuz**: Yeah we need it, otherwise we can compute the state root that we are signing over. 

**Stokes**: I had it that way originally because I was concerned more about MEV and maybe some more niche cases, but Terence raised this point, which is correct.

**Tim**: Any other comments?

-------------------------------------
### 198.10| **CL Discussions** | Staking bandwidth considerations [(context)](https://github.com/ethereum/pm/issues/1163#issuecomment-2379336862) ([1:04:44](https://www.youtube.com/live/YQwdKE0d8LI?feature=shared&t=3884))

**Tim**: Ok, the last thing we had on the agenda. Ryan had an Ethresear.ch thread--again more of a CL-related topic--trying to nudge people towards getting better numbers around what we believe home staker bandwidth requirements should be and this way we can make better decisions around things like blob counts. More of a CL topic, but I don't know if anyone has thoughts, comments, or things they want to discuss about this?

If not, this is clearly a topic that'll come up over and over as we start discussing blob counts on the CL side,so we can leave it at that.

That's everything we had on the agenda for today, anything else people wanted to bring up that we didn't get to?

**Ben**: Just on the staking bandwidth considerations, that should hopefully be helped a lot from the Eth get blobs. Most of the CLs are implementing that so the validators can pull the blob from their own transaction pool, if the CL use that, rather than waiting for it to be propagated.

**Tim**: Nice, and then there's a comment in the chat by Alex about 44s? Any updates on this? Any progress made?

**Marek**: At Nethermind, we are working on both, basically Portal Network and ER files as well. Right now we are finalizing Pectra, so we should have more power to push for 44s.

**Tim**: Nice. Anyone else? 

**Lightclient**: Do any client teams have thoughts on how Portal is coming with their implementations or is it still too early?

**Tim**: Anyone from Portal Network here? 

**Giulio**: Erigon is not in sync, if that counts. We don't plan on really using Portal but we can get heavy old blocks without the P2P and old blobs too.

**Kolby**: I think there's three people from Portal in the call. Me, Piper, and Jason Carver, but yeah. For our project, not exactly. I know that two people picked up making a Portal client for Besu in the EPF and that's coming along fairly good. They're just about to integrate with Hive tests, which is cool.

**Tim**: Sweet, anything else people wanted to bring up?

There's a question in the chat how people are integrating Portal into their infrastructure. Does anyone have thoughts on this?

**Kolby**: I could give some ideas. Some of my ideas are running it as an alternative history provider instead of devP2P. Especially because with 44s, you'll no longer be able to retrieve that data over devP2P. It could also be used to seamlessly once 44s is activated no JSON RPC functionality would be lost, which is nice. So if somebody tries to fetch something before the eth44 window, you can actually give a valid message if that data actually existed instead of just saying I have no idea what this data is. I'm sure there's other things I missed.

**Kev**: I was mainly interested in how it's being done now. Is it being integrated? Are the current EL clients calling the Portal Network or is there like some network that's being created that that doesn't integrate well with Portal?

**Ahmad**: For us, the Nethermind implementation, I think we're connecting directly to the P2P of Portal and trying to get the data from P2P directly. Also trying to serve, so not only getting data but also serving. But other clients could choose to do it differently. 

**Kev**: I'm not sure I see benefit in like half of the clients having a separate P2P Network for serving a history like Portal and then half connecting to Portal. Seems like unneeded redundancy.

**Kolby**: I'm a little confused with how that is phrased, but I think every implementation would probably be succinct in the way that Ahmad said. I think that'd be the most sensible implementation.

**Tim**: Okay, anything else on Portal? If not, I think we can wrap up here.

Thanks everyone.

I'll put up the issue for the BLS breakout on Monday, but we have that and then the interop testing call and then hopefully we can finalize specs for devnet-5 and get devnet-4 up before next All Core Devs.

In case you missed the chat, Pectra devnet-3 finalized as we speak! So, thanks everyone and talk to you soon.




-------------------------------------
### Attendees
* Tim
* Stokes
* Pooja Ranjan
* Ben Adams
* Oliver (Reth)
* Lucas
* Trent
* lightclient
* Marius
* Guillaume
* Danno Ferrin
* Justin Florentine
* Ansgar
* Peter Miller
* Jochem-brouwer
* Phil Ngo
* Ben Edginton
* Dankrad Feist
* Paweł Bylica
* Guillaume
* Enrico
* Kolby Moroz Liebl
* Jason Carver
* Mario Vega
* Ahmad Bitar
* Mark
* Mehdi Aouadi
* Hsiao-Wei Wang
* Julian Rachman
* Daniel Lehmer
* Andrew Ashikhmin
* Justin Traglia
* Toni Wahrstaetter
* Alex Forshtat
* Piper Merriam
* terence
* Manu
* Ruben
* Marcin Sobczak
* Carl Beekhuizen
* Ignacios
* Marc Harvey-Hill
* potuz
* Barnabus
* James He
* Nixo
* MarekM
* Ameziane Hamlat
* Somnath-Erigon
* Kev
* Kasey
* Rupam
* Andrei
* lattejed
* Dragan Rakita
* Sophia Gold
* nflaig
