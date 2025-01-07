# Consensus Layer Call 146

### Meeting Date/Time: Thursday 2024/11/28 at 14:00 UTC
### Meeting Duration: 1.5 hour
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1200) 
### [Audio/Video of the meeting](https://youtu.be/HcjuY3WDa9A) 
### Moderator: Stokes
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
146.1  |**Mekong Deposit Processing Bug** Validator deposits on the Mekong testnet triggered major network disruptions earlier in the week on Monday, November 25. The testnet has since recovered and is finalizing again. Several fixes have either been implemented in clients or are in the process of being implemented, said Stokes.
146.2  |**Mekong Deposit Processing Bug** Prysm developer “Potuz” raised the need for more Pectra specification testing in light of the deposit processing bug on Mekong. Consensys Researcher Mikhail Kalinin pushed on this sentiment saying that there are already tests for deposits but client code in some cases is different from specifications and there is a need for more extensive testing that covers client dependencies. Stokes said all types of efforts to bulk up testing for Pectra would be useful.
146.3  |**Devnet-5 Specifications** The first issue is related to EIP 7685, general purpose execution layer requests. It is a corresponding Engine API change to an earlier one already merged and finalized for Devnet 5. The original code change proposes excluding empty items from the “requests_hash” commitment to ensure easier testing and mirror the behavior of other types of EL commitments. Both were proposed by Geth developer Felix Lange. Developers agreed on the call to merge the corresponding Engine API change into Devnet 5 specifications.
146.4  |**Devnet-5 Specifications** The second is an update to EIP 7742, uncouple blob count between CL and EL, to ensure that the gas fee mechanism for blobs correctly scales when the target/max values are updated, even if the target value is not half of the max value like it is currently. EF Researcher Ansgar Dietrichs said that the EIP is “nice to have” but it can be included later in the Fusaka upgrade to avoid delays to Pectra activation. In its place, Dietrichs recommended a minimal “one-line” change to the update fraction in EIP 7742 such that a block without any blobs triggers a reduction in the base fee by less than 21%. In effect, the one-line change would reduce the volatility of negative base fee adjustments.
146.5  |**EIP 7691** The Ethereum Foundation’s PandaOps team conducted a study on the performance of home stakers and solo stakers since the introduction of blobs in the Dencun upgrade. They found that stakers operating on the most resource-constrained devices relative to other types of stakers on the network are performing well and would not be negatively affected by a blob capacity increase to either 4/8 or 6/9 target/max blobs per block.
146.6  |**EIP 7691** Prysm developer “Potuz” was not in favor of an increase to 6/9, while Reth developer “Oliver” was. Wahrstätter pointed out that increasing the target/max such that the target value is not 50% of the max would introduce strange dynamics to blob base fee adjustments, that is the blob base fee would decrease at a faster rate than blob base fee increases. However, developers could address this kink later in the Fusaka upgrade. Dietrichs stressed that rollups care more about increasing the blob capacity than a perfect UX when it comes to blob base fee adjustments. Potuz cautioned against a “radical” change to blob capacity in Pectra and recommended that developers go with 4/8 values.
146.7  |**EIP 7691** In favor of doubling the blob target, Dietrichs wrote in the Zoom chat, “I don’t think anyone argues that a throughput increase is without cost but we have to be willing to make tradeoffs and it’s a very modest ask for very big payoff… We are at real risk of losing L2s to alt-DA providers. That is much more impactful to real-world Ethereum users than any mild extra load for stakers.”
146.8  |**EIP 7623** Related to the discussion on EIP 7691, developers discussed the inclusion of EIP 7623 in Pectra. EIP 7623 proposed an increase to the cost of call data such that the maximum size of Ethereum blocks is reduced. The EIP, proposed by Wahrstätter, is especially important to address a “worst case scenario” in the size of EL payloads given the inclusion of EIP 7691 in Pectra and a potential gas limit increase organized independently by validators.
146.9  |**EIP 7623** Geth developer “Lightclient” was strongly opposed to this code change in Pectra, stressing that even without its inclusion, developers are not ready to implement existing Pectra code changes on mainnet. “I feel like we just had a major testnet failure and should add as few additional things as possible,” wrote Lightclient in the Zoom chat. Stokes agreed that this was the main reason in his view against EIP 7623 inclusion in Pectra. Nethermind developer Ahmad Bitar wrote in the Zoom chat that in his view the EIP should be a “prerequisite” EIP 7691. Dietrichs added, “EIP 7623 is a fix of an active security vulnerability. … This should have been the first EIP in the fork.”
146.10  |**EIP 7623** Others like Nethermind developer Marek Moraczyński and EthereumJS developer Gajinder Singh agreed with Dietrich's comments. Reth developer “Roman” chimed in reiterating that developers should not increase blob throughput without coupling it with a lowering of the maximum block size. Stokes recommended moving forward with EIP 7623 in Pectra. Lightclient opposed the decision again. Stokes recommended tabling the discussion for further input from EL client teams on the next ACD call.
146.11  |**EIP 7251** The final issue related to Devnet 5 specifications that developers discussed was related to EIP 7251, the increase to validators’ maximum effective balance. There is an edge-case scenario where a malicious actor can trigger validator-staked ETH balance consolidations on behalf of another validator. It would require the malicious actor to send the validator their staked ETH in exchange. Albeit expensive, Stokes said it was “a potential attack vector” that Consensys Researcher Mikhail Kalinin has proposed a fix for. Stokes said the fix is a relatively “simple change” and confirmed specs and relevant tests for it would be pushed out post haste for CL teams to start their work on it.
146.12  |**PeerDAS** EF DevOps Engineer Barnabas Busa shared an update on PeerDAS. He said that client teams are waiting on Pectra Devnet 5 specifications before rebasing PeerDAS on top of Pectra. Once the rebase is complete, client teams will move ahead with coordinating a new PeerDAS devnet launch. This is also the status of EOF implementation progress as well, Busa said.
146.13  |**EIP-7805** Thomas Thiery, an Ethereum Foundation Researcher, gave a presentation on EIP 7805, fork-choice enforced inclusion lists (FOCIL). FOCIL essentially enables validators to define a set of transactions that builders must include in their blocks. In doing so, validators can boost the censorship resistance of Ethereum by ensuring that builders do not have full control over transaction inclusion in a block.

**Stokes**
* We will proceed. Okay. Great everyone. Let's see. This is ACDC 146. It is issue 1200 and the PM repo. I put the link here in the chat. And yeah, there's a number of things here on the agenda today we'll touch on Mekong testnet. The intent is to finalize Pectra for devnet five, and presumably that's the last sort of spec updates we'll need for Pectra itself. otherwise, yeah, there's some other other research things at the end here. So in any case, let's go ahead and dive in because there's quite a bit here. So first, yeah I wanted to talk about Mekong. this was essentially from Devnet four as I believe. And it was a public facing test net. There were a number of deposits, I think Monday or Tuesday that caused some issues. And I think every client, well, at least every CL client had some bug. that being said, the test net is finalizing again, which is very nice. So good work everyone. And in any case, is there anything else we should be discussing here? Any follow ups or contacts clients would like to add are on this bug. Okay, we've got an all good from our side in the chat. Fair enough. Okay, great. So yeah, there are some issues with the deposits and yeah, I think there's a number of different places we can add tasks, just to make sure that there aren't any, regressions. And, yeah, we definitely need more spec test as post calls out here. Mikhail. 

**Mikhail**
* I just wanted to add on the spec test side, we have tests already in the PR, for this specific case and for other potential cases. There is an issue that I've recently opened. so we need tests to cover the epoch processing in a bit different way than it's covered today in the consensus spec tests. So today we use kind of like code coverage metric for like for the epoch, processing tests, which is the code used that is that the spec has. And the problem with the on the Mekong that happened recently was because the spec and the client code are different because clients use caches. So we need to do more extensive testing and find it potentially an ideal situation. We find all these kind of dependencies. When one epoch processing function does the change to the beacon state, and the other function uses this change in its logic. So if anyone wants to. If anyone wants to help with this, with writing these tests, there is an issue. And yeah, I'm happy to to help on that. 

**Stokes**
* Cool. 

**Mikhail**
* Yeah. Yeah. I'll just send a link to this issue. 

**Stokes**
* Another thing to add there is at least I looked at one of the bugs and it wasn't so much a caching issue. It was just like an, you know, an accident, really. And spec tests should catch this kind of thing. one thing to add is the spec tests though, are, you know, I would say primarily more like unit tests. Not so much like Indian integration tests. there are some types of spec tests that start to get towards more end to end things. But that being said, yeah, clients should be careful writing code and, you know, do testing on their end as well and not just rely on the spec test parents. 

**Terence**
* Sort of mutation testing that's happening with the CI/CD. Sorry for the stupid question. I think like a couple of months ago, I went through, basically what I did in Prism is that I started commenting out every single line of the state function, and to see whether the basically the spec will still fail. And then if it doesn't fail, I make a note of it, because that typically means that there is a spec test missing coverage. And then I think I opened like three PRS on the spec test because of that. So I wonder if it's worth doing again from my end?
* Or do we feel like there is sufficient coverage on the spec test today? 

**Mikhail**
* I would say if you if you're willing to do this, please go ahead and, you know, just just do it. But for this particular case, on my own, even if the even if this this spec would have a perfect test coverage And probably it has. In this particular case, it would not mean that. Yeah, that we would reproduce this bug using those tests. 

**Terence**
* Yeah, definitely. Yeah. 

**Stokes**
* Yeah. I think with testing the more the merrier. So everyone should always be thinking about testing from, you know, the more angles, the better. Cool. Well, that being said, we quickly resolved the the bug and I think everyone has shipped fixes or will soon. So nice work. And yeah, anything else on that. Otherwise we'll go to Devnet five spec. 

# Devnet-5 spec [10:30](https://youtu.be/HcjuY3WDa9A?t=630)
**Stokes**
* Okay, cool. So there's a number of things here. let's start with this first one. There was an update to 7685. to change how we handle empty requests with the hashing and the commitment on the EL. So this one. Yeah. So it's a in a bit of a weird spot because I linked the execution APIs PR here. these are the updates for the engine API. There was a corresponding EIP update and then also a CL PR update. The CL specs PR and the EIP have been merged. this has not been merged, but it sounds like just going off of a comment from Felix here on the agenda that there's maybe still some open discussion. my understanding is that we wanted this change and we were going to merge it, and.
* Yeah, I guess we should figure this out now. if we want to walk it back, which I don't really recommend at this point, we need to go and merge some things in other places. So then I guess the question is. Yeah. Does anyone feel strongly against this change at this point? We have support. So. Yeah. And this is my sense. So I think we just go ahead and merge this one in. Okay. 

**Mikhail**
* Yeah. Just Felix wrote that probably we should not, like, have a requirement on a strict order on the engine API and just leave this requirement to the CL side. So the requests are sent in the right order. And this is kind of enforced by CL specs rather than by engine API. This is one of the recent Felix comments. other than that, I had some, you know, some comments about this ordering. Why not doing it on EL, but I don't mind to merge it as is. It's not like super strong, super strong, opinionated that it should not have the order statement in the engine API spec. So if there is a strong, consensus, if there is a strong willing to to merge this as is and there is no opposition from the client teams, then just let's just merge it. 

**Stokes**
* Okay. Yeah. I mean, that sounds like that's where we're at. We're getting support in the chat. And yeah, I think given that we've merged other things that move in lockstep with this one, I think would be a way to merge this. And we can close out this question for Pectra. So let's go ahead and merge it. And that was pretty straightforward. 

# finalize EIP-7742: include? Update EIP-7742: update the required EL headers and the gas fee mechanism EIPs#9047 [13:35](https://youtu.be/HcjuY3WDa9A?t=815)
**Stokes**
* Next up. Okay. So the next I think the big thing here with Devnet five would be 7.742. So let me grab this update And there are a number of 7742 pairs for the feature. They've kind of been ready to go for a while now and let's say maybe like a couple of weeks now ago in the process, as people kind of dug into this, there was a question about changing the fee market, because especially as we go to more flexible target and max values, that's 7742 unlocks. You get to a place where the fee market that sort of was hard coded in 4844 doesn't respond in the best way. So that all being said, there's an update here. It's PR 947. And what we had said from a discussion at Devcon was that we'd have this PR and essentially make a decision today. So there's been some comments on it.
* But yeah, I guess the question here is what's the consensus? do client teams want to include this change or just move ahead with 7742 without it? I'm sorry. 

**Ansgar**
* Yeah. Just wanted to say for for context, that basically this like two different basically like, most of these changes are not very nice to have. They definitely all make the market somewhat nicer. and, and for all compatible like we will have to do this anyway, but we could also do a lot of this in Osaka. And the one thing like if we end up rejecting this kind of bundle of features and that is proposed in the PR, then what we should do is at least have a minimal, change, although I think the better target would actually be the throughput increase EIP itself. So 7691 and which just with just a small adjustment to the update fraction, because if we don't do this, if we basically don't make that one small change, which is literally one line change. And then what would happen is basically after the fork.
* Now any empty block would reduce the base fee by 21%, which I think is a little bit much because basically because because the sensitivity just becomes higher and because now basically we have six blocks under the target in a single block. And and so that would be like a 21% drop, which I think we should adjust that value, which is literally like a one parameter change. So that would be the very minimal change. I think I would recommend at least doing that. The other things are still nice to have, but if clients prefer it, we can do them in Osaka instead. 

**Stokes**
* Yeah, and you're talking about the update fraction. Like we would just change that to reflect the new target. 

**Ansgar**
* Yeah. And there's some ugliness. Like for example by doing that at the time of the fork, the base fee jumps a little bit, which of course this is part of the things that would be cleaned up with this more expensive change. But if we are saying we are going for like the bare bones version here, then we could basically just ignore that. Only change the update fraction. That's a one line change. And and do the nice clean up in in Osaka. 

**Stokes**
* Right. Yeah. So I'm well. Does anyone else have thoughts? I have thoughts on this but. 

**Dustin**
* I yeah just to some extent. So one of the tensions that has come up in these discussions is, is question of, incentive to propagate blobs at all. And so they're obviously expensive and getting more expensive. And there are good for the network as a whole. Yes. But and, and so one of the and it would be, I think maybe we'll say maybe my what I would ideally target and I don't know what other people think about this is actually for the target price, the target market to be a little more to incentivize people to care about. Bob's a little more right now. CLs actually are better off avoiding Bob's mostly, honest validator shenanigans aside. and because they're just not paid enough for it to be worthwhile. And then the trouble is, as soon as you get above the target, it this price ramps up fairly quickly. And so there's not a happy equilibrium really above that either, which would have been otherwise kind of nice.
* So it would be one possibility. I don't know if this is feasible in this particular time frame for for Pectra or if people want this is to explicitly target, a slightly higher like a just enough of a base fee that it is reasonable to for people to actually want to carry Bob's in the same way that people complain when they miss attestations or other things in committee messages, etc. right now nobody complains if they miss Bob, so to speak. But that's a problem with Bob's. And people are being browbeaten into like, you know, you have to have to do Bob's. So yeah, that that's what I'm my thoughts, I guess. 

**Stokes**
* Yeah. I mean, Bob's are a critical part of the protocol, so we should make sure that they're supported. Ansgar has the comment here that you could have, like client side that basically a for inclusion as you build. so yeah, that's an option. And in any case, that was another. Yeah. I mean there was another EIP for raising the floor. that's something we could get into. Tony, you had your hand up. 

**Toni**
* Yeah. first of all, I would agree what Anne said. I think the nice to have EIP can be or they're nice to have. Changes can be postponed until Lusaka. And regarding the question to put them into 7742 or not. I would say we don't put them into there. and keep 7742 and anything that touches the block base fee separate just because I think it's much cleaner that way. And then we can still put like the thing with the block base fee fraction into the ERP that eventually changes the blob to the max. So that could also work. And yeah, I think we have it on the agenda at a later time. Anyway, to talk about the blobs and what Dustin mentioned would basically be something new. We can also think about as a nice to have when we eventually touch the blob base fee. 

**Stokes**
* Yeah, that makes sense. And it does sound like a simple path forward for Pectra, thank God. 

**Dankrad**
* Yeah, I mean, it's two different things, right? We have both the base fee and the tip. And I think there's like confused them a little bit. But what we want Is, like that? Yes. Like, block builders want to include blocks and that's like, that's already possible. Right now you can just set a manual tip at which you include them. It would be nice if like blobs just came with like a little bit of a tip because they do, was like increase the risk of being reworked more significantly and more significantly than other transactions. like I would also be very much for like setting some minimum base fee for blobs and like, I think like it's been really obvious, like, over the last half year, everyone's complaining, oh, rollups don't pay. And like they don't contribute, they are parasitic, which is of course complete bullshit.
* But I think like having a small, just like, base fee would, like, end this, annoying charade where, we will increase blobs a little bit, and then suddenly I will be like, oh, now we're not burning anything again. and like, we'll make it a little bit more kind of a little bit smoother. so I would actually think that it would be a great idea  to actually increase the base field a little bit. 

**Stokes**
* Okay. 

**Potuz**
* Yeah, I agree, and I think rollups also agree that that increasing the minimum base fee is something that it's useful. unless we are always on congestion as now. regarding the issue of, like, deep, the markets with deep inclusion, there's a bunch of us that are not really well studied, in my opinion. One of them is the issue. That tip applies the same for blobs that carry execution, that blobs that don't carry execution. And this makes a huge difference for different rollups. That's one thing. The other thing is timing games. even if the builder has the blobs with paint chips. As long as the pool is requesting the headers late enough because they want, they know that they can. And they do this now. then the timing game dynamics changes whether or not you are or not going to include blobs. If you increase the limit to ten blobs, then either pools are going to start requesting earlier and playing less timing games,
* Or they will continue requesting as they do today, and the builder will have to adjust the number of blobs that it includes. so I think these two problems are need to be taken into account and they need to be studied. if we're going to be like counting with tips as to decide on the blob limits or blob targets or blob inclusion event. So I would suggest that we keep it to base fee considerations when we talk about the market until we understand these other sub topics. 

**Stokes**
* Yeah, I think that makes sense. Just around gaining a better understanding of the actual market out there. And a quick interjection. it sounds like maybe from the chat people were confused. So like, right now we're talking about just this one update to 7742 that would touch the market. We are not talking about raising the target or max or anything. We will talk about that in a second. But that's very separate from these basic mechanics where like very zoomed in right now.

**Gajinder**
* Yep. Just want to add that, I mean this if we don't have any plan to update any target before, I mean, then this PR is basically rendered useless in the sense that it won't add any value. But if we are trying to update the target, then this PR is a bit relevant. Although we can also update target with with some hard coded update fraction like we have done in 4844. But I feel that, this is, this is a good way to go forward. And, maybe we can even have time based target unlocks, with, Osaka. But, yeah, that can happen. That can this PR can be merged with other PRS at that point as well. 

**Stokes**
* Right. So I mean, the question answer now is do we. Yeah. Essentially like how like what what is good enough. We could do a very simple thing. Like there does seem to be quite a bit of demand to raise the target, and max in Petra. And because of that, then we can ask about the fee market. And this current PR is one proposal, another proposal that Ansgar Antonio were just talking about, that is even simpler, is just changing, essentially this update fraction that we have That would do exactly what we want. That's like literally a one line change. You're changing a constant. This one that is under discussion at the moment has some normalization involved. It's a little a little bit more complicated. So the alternative would be to do like they were suggesting, like we just change this update fraction. And then we kind of bundle this with a number of other things because as we're discussing, there are other things around the markets that we could imagine changing. I don't think they're quite, you know, in the endgame state.
* So that would be the idea is to go ahead and do the simple thing that works now and then hold, you know, these more invasive changes off until pusaka. 

**Gajinder**
* Yeah. One thing I want to add, so there are two changes in this. One is normalization, which which as you are saying is a bit more complex. And the second thing is to, to add targets. target blobs per block in el header. So maybe I think we should at least keep that one. 

**Stokes**
* Well, that's already in seven, seven, four, two. 

**Gajinder**
* Okay. All right. Thanks. Yeah. 

**Stokes**
* Okay, so we have, essentially a plus one from Tony to what we just described, basically ignoring this update for now and just bundling it with Pusaka. Then in Petra, this is a topic we will get to soon. around actually changing the blob counts and yeah, just having some some for to for that possibly with updating this update function there. Does anyone feel strongly about doing this more invasive change at the moment or would you rather go the simpler route? 

**Ansgar**
* Sounds good. Yeah. Just just to say basically like I also said it in chat to me, there's three questions. It's the definitely do the simple definitely do the one simple change which is the um update fraction. and then probably it seems like the majority wants to push the bigger change the normalization. And that was working on to to Lusaka, which would then still leave. The one extra decision that we have to make is, the minimum base fee change. That's the one that Max Resnick originally proposed and argued for just now, like five minutes ago on this call. And we can also push that to, for Osaka. It's basically in the middle of those two. It's like small but not a one line change. And also nice to have, but not as important as the other one. So basically we should still, if we want to do the the very small thing and push the very large thing, then we should make the an extra assessment of the the. We also want to increase the minimum base fee in in Petra. Or do we also push that to Vaisakha? 

**Stokes**
* Yeah. Well, does anyone have thoughts? I would say it's like pretty late in the game because my sense is that Max is VIP. Well, I guess that's a question. Like, was Max's VIP ready to go? 

**Ansgar**
* It's almost a one line change. The only reason it's not a one line change is that we would have to basically at the time of the fork, then reset the excess gas to zero. So basically there would also it's like basically it's two lines. It's like in the in the way you now calculate the excess gas. There has to be an if statement. You know, if it's the time of the fork return zero and and and change the one value. So basically like the max gap is like a two or 3 or 4 line change. But my in my understanding is that that is not fully specked out. I think he only specked the one line and not the if statement. 

**Stokes**
* Right? Yeah. So I'm trying to ship Petra, and my concern would be that if we take another cycle to get that ready, Already, then it's just going to delay things even further. So I guess I'd want a sense of like how important raising the base fee would be. Or maybe I'll say minimum fee. yeah. My sense from previous conversations is that there wasn't, like, strong consensus that it was super urgent. 

**Gajinder**
* Although the normalization with 9047 is that it will give a nice treatment to the current excess gas that is out there, and make sure that when the target is updated, that is sort of taken care of in a nice way and there is no irregularity. So that is something that is there in 9047, which could be considered. 

**Stokes**
* Sure. But then that's still a slightly different point to actually raising the minimum fee. There are some comments in the chat that this is a nice to have, but not existential. Do we all agree to that. Anyone disagree? I don't know. Just so strongly about this. Okay. Yeah. Peter. 

**Peter**
* Yeah. No. Um. Just. Sorry, I just joined. this is seven seven, four two. You're talking about. Right? 

**Stokes**
* Well, we're talking about a number of things. So right now we're talking about raising the blob base fee. So right now, the way the protocol works is it's a one way. And there have been proposals to raise it to some higher number. 

**Peter**
* Okay. Yeah. I mean, I feel it isn't existential, but like if we're going to do, a version of seven, seven, four two, we kind of have to because otherwise, because we don't want the consensus layer to have to deal with greater than 60 four's. 

**Stokes**
* Right. So this would be within the domain of the L, and so the CL should be fine there. 

**Peter**
* So I think we're forced to do it eventually because we're talking about if we do, if we do a version of 742, this is a prereq. 

**Stokes**
* No. So the thing that we're talking about now is essentially a number that's only on the L, so the CL never has to deal with it. 

**Peter**
* I guess I'm confusing something else. 

**Stokes**
* So yeah that's okay. No, there's a number of things in play at the moment. okay. So it sounds like from the chat there's support to table this for the min fee. just because. Yeah, I really would like to move things forward here. I think we all would. And if we, you know, again, take more time, then it's just going to delay Pectra on our. Oh, okay. 

**Ansgar**
* Sorry, I just wanted to briefly ask because we want to actually get through freeze. And so if we say we go ahead and I mean, obviously there's still in the next agenda point for, for the actual Bob throughput increase, but assuming we decide to go with a Bob throughput increase, then  that it does require this one small adjustment to the update fraction. So the question is what is the timeline there? What is the process there. Do we do that async in a PR who's going to open the PR. There's different alternative options for the for that update fraction. I think it's insignificant enough that we can just say that we will figure that out in the PR and just go with anything that has weak agreement over there. But like how do we basically what's the timeline on that decision? 

**Stokes**
* Yeah. Well, it sounds like we should just get into that now. I think there was a suggestion just to put it into the 69 EIP, which is EIP 691. I think that's perfectly workable. So yeah. Ben. And then we will talk about the blob counts. So, Ben, I don't know. You had your hand up. I don't know if you had. Sorry. 

**Ben**
* I think I think the min fee is related to the blob count. So if you're not touching the blob counts, that's fine. But if you. If the blob counts are changing, then the min fee becomes more important because it will immediately crash the market and go back to one way or one way, which is like a crazy small amount. I mean, the way fraction is used to be able to calculate the fractions of gwei. It's not used as a you know, you wouldn't launch a token on Uniswap. It one way. 

**Stokes**
* You could. 

**Ben**
* Know, but well Uniswap would break because it can't handle there's no decimals. Further. There's no you can't go smaller. You know what I mean? So you either. Yeah. Anyway, I mean, so if you're going from, let's say you need to put the price up. where do you go from one one way or you can't put it up by 10%? You have to put it up by 100% because there's no you know, there's no fraction of a of a way, for example. 

**Stokes**
* Right. Yeah. Francis, do you. Yeah, I guess I do want to move to the blob counts, but. Yeah, yeah. 

**Francis**
* Yeah, that's that's why I'm suggesting, like, because I think a lot of this depends on, like, what kind of target do we want to set, right? 

# Include? eip7251: Do not change creds type on consolidation consensus-specs#4020 [https://youtu.be/HcjuY3WDa9A?t=2103](35:03)
**Stokes**
* Okay. Yeah. So, we will come back to this next agenda item. there is a change to 7251. But since we're already here, let's talk about the blob throughput increase in Pectra. Extra. So to kick things off, I think many of you have seen this EIP already. 7691 which proposes raising the target to six and the max to nine. I'll just grab the link here and maybe to kick us off. Sam wanted to give a quick overview of some work that, he did. Is Sam here? 

**Sam**
* Yeah. I'm here. I think we were going to actually get to present first and sort of combine them. 

**Stokes**
* Okay, sure. Yeah. Yeah. 

**Parithosh**
* I'm just gonna give a bit of context first. so there was concern, at least in the past, to, that we're going to have issues once we increase the blob count in terms of, long range syncing as well as how the network heals. Once there was non finality. So in order to collect some data we did do some devnets over the weekend. You can find a summary over here as well as a deeper blog post on the topic. But the TLDR is that we're not. At least the indication from the devnet is that we're not purely bottlenecked by bandwidth. There are some optimizations that could help sync as well as peer performance, but all of these optimizations are something we're going to need to apply on mainnet. Today, even with the current three six limits, and at least the indication is that, even if we were to increase the block count, we wouldn't necessarily, immediately suffer that we would be able to handle an increase. in order to the question of what we can increase to. I will pass it on to Sam. 

**Sam**
* Yeah, thanks. I'll just share my screen. I hope everyone can see that. yeah, I'm Sam from the panda ops team. I'd just like to quickly go over this post I made yesterday about block arrivals home, stakers and bumping the block count. we as a team recently just started ingesting data from community members who are running nodes at home, and this is what made this analysis possible. so a quick shout out to those community members. so our analysis mostly focused on the case where blocks are being built locally by home stakers and then observed by home Stakers on the other end. home stakers are the most bandwidth constrained participants in the network. and this makes them particularly sensitive to any increase in the block count. so we asked three questions. the first question was how is three target and six Max performing today for these users? And it appears to be pretty good. most bundles are arriving well under this four second deadline. onto the second question.
* Does the arrival time of these blocks and and blobs, scale with the count? And. Yeah, to the surprise of really no one. It does. so under the the third question here, how can we how much more can we actually support our main net? the long story short is that we believe that both for target eight Max and six target nine max are achievable. As far as arrival times are concerned, it's just one piece of the puzzle. yeah. While this analysis made some pretty naive assumptions, I. Yeah, I personally believe these numbers are realistic and safe. we also on the way just forecasted how this would look with EIP 7623, which reduces the maximum compressed block size from 1.8 
* Meg down to 720kB. and yeah, in this scenario, even in the worst case scenario possible, it's still possible to do a count bump. that's pretty much it for this. I'll throw the link in the chat if anyone has any questions, hit me up. 

**Stokes**
* Cool. Thanks. Ahmad. 

**Ahmad**
* Yeah. so one thing that I'd like to mention here is that there is also a push for raising the gas limit for the, L1 gas in general. And, this needs to be taken into account because this raise will probably bump up the block size to around 1.1, even with 7623, 1.1 or 1.2 mix. because like the bump is to around the maximum of 45 million, or something like that. So might be also play an effect here. 

**Oliver (Reth)**
* We think not pumping the block count would be a big mistake in Pectra because we're like essentially waiting for pure times to scale blobs. But that's in Osaka. And there's no, like, clear timeline on Osaka. and it's already pretty apparent that from the presentation that basted a few days ago that they are looking at needing more blobs on top of all the l2's, being announced at the moment that they're also going to launch a mainet. So it would be a huge mistake in our eyes to not do anything at all. We think 69 is preferable, but I see in the chat that maybe 510 is easier to do, and I think we'd be fine with that as well. obviously I'm an EL dev, so from my perspective this seems pretty easy because we have 7742 now, and I don't have like a full view of exactly what changes need to be done on the CL here. So I would like some input on on what CL devs think. 

**Stokes**
* Yeah, thanks. So we do have this EIP for 69. And from what I've seen mostly in the chat over here that there's some concern that 69 is not a perfect double. So yeah I guess I'd like to hear more about that. My understanding is that really the only issues there were that it would make the fee market, you know, have some weird kinks, but it's nothing existential. Toni. 

**Toni**
* Yeah. One of the issues. I wouldn't even say it's a it's a big issue. But if we kind of move away from the target being half of the max, then what we could end up with is the base fee, double base fee scaling, faster in one direction than into another, which is not a big problem, I would say. So six nine should would would basically work as 510 would work. So I don't really see a concern there. Why six nine would be from the base fee perspective, worse than 510. 

**Ahmad**
* I mean, in in the case of empty blobs, you will get the base fee going down a lot, whereas with full blobs you will get the base fee raising less than that. 

**Toni**
* So yeah, this is true. This is this is also one of the points that we talked previously about about those blob base fee improvements. There is one point called making it symmetric again. And by doing that we can also kind of account for that. So we agreed earlier on that we might want to do those optimizations at a later fork. In this case, if we say that this asymmetric block base we update is a big problem, then we should stay somewhere where the target is half of the max. 

**Stokes**
* Oscar. 

**Ansgar**
* Yeah, I put I put some examples in the choices we could have. So indeed with the camp mechanism, the sensitivity of of an empty block and a full block would be different because say for example, for six nine, right. Like if an empty block is six blocks under target and a full block would only be three blocks under target. So we could say be very sensitive to downside, then we would have 21% maximum decrease and 12% maximum increase. But we can also choose the opposite. So like 11% maximum decrease like today. And then it's only a 6% increase or anything in between. Right? Like literally this this update function, we can literally just pick any point of that curve. It will always be more sensitive to the downside than to the upside. And the reason why I strongly would argue for six nine over asymmetric change is that in both cases, only really the roll ups are concerned as consumers to blobs the network doesn't care about like about a slightly more flaky, base fee. Right? Like that's only UX problem for roll ups.
* And from talking to roll ups, it really seemed like they are much, much more concerned with overall throughput than the UX of a slightly more, volatile base fee. So basically they they would much rather have overall more, more room. yeah. And they're not so concerned about the base fee. So of course, I mean, we have other concerns here, right, about average throughput levels and all these things. But in terms of like the base fee, I don't think we would actually act in the interest of the people that we're trying to protect by, by avoiding this asymmetric base fee situation. 

**Stokes**
* Right. Which argues for like six nine over say 510. Because the point here is to raise the target as much as we safely can. I think it was POTUS. I'll just go in the order I have here on zoom. So POTUS. 

**Potuz**
* I want to give a perspective on Sam's result. While it looks as though that increasing to those numbers would be safe when we are in congestion, when actually blocks are needed to be posted regularly, then we would be in a situation where we hit on every slot the maximum if the builders are behaving correctly, and then if you see for 9 or 10 for limits, then you're reaching a point where all of those blocks are being trying to be reordered at least five. Not all, I'm sorry, at least 5% of those, because the line of the 95% is very close to the $0.04 to the four seconds. And this is without counting execution, without counting validation, and without counting for choice on clients. so your blocks are arriving near the deadline, which is four seconds, and we need to steal a test. We need to process, and we need to make a signature out of those. So I would expect that at least 5% of those blocks are going to be being reworked. Besides the validators, like losing the attestation and instability in the network, if we see every single block 9 or 10, my proposal would be to not do something radical this fork move to 48 that we kind of know that we can handle.
* Probably 58 if you want to increase the target. 68 my work. But I wouldn't increase the limit without more measurements. 

**Stokes**
* Okay, Sam, I imagine that you're in response to what Pete is saying. 

**Sam**
* Yeah. so, like, the analysis was done off the beacon, event stream and the client submit those events at different times. it essentially looked at each slot. The latest time for a client to emit the head, the maximum blob sidecar or the block event. So I don't actually know. I guess it's a client specific thing on when those events are are emitted, but it's probably worst case scenario at like every stage of this. And reality is that like we're we're actually way under when we say that like 5% of those blocks will be coming in after four seconds, that's. Yeah, probably like a bit too much, I'd say. I'd say the real world picture is way better than that. We've just left it there to be as safe as possible. and this is also 5% of, of, like, home users, not 5% of the network. I know we care about home users, but yeah, it's just worth bringing it up, I think. 

**Stokes**
* Yeah. Thanks. Thanks, Rob. 

**Dankrad**
* Yeah. So I want to say something about the limit targets. I think like, in terms of predictability and everything. Like right now, at least like most roll ups, like what we're seeing now, people starting to build. Base roll up. But other than that, the timing of when roll ups get their blobs in is, like, not very important to them because they like sequence separately anyway. So I think, the, the only concern about it is really the, the potential economic attacks that that can be done. Like basically I think at six, nine, like one third of the Stakers could potentially just like, set the base fee to the minimum and start extracting value via the tip. So that's like the classical EIP 1559, economic attack in quotation marks. But I just think like that this is at the current Karen stayed just like a very, very unlikely scenario. And, like, we should just, eat that and, like, basically, like, as soon as we can, like, put it back into the, in the normal range and then, like, it's much more important to temporarily have this target increase. 

**Stokes**
* Right. So, yeah, I am hearing a lot of support for six, nine. I think one way forward would be six nine. and then a simple sort of patch would be changing this IP to include the target value that we want or. Sorry. Let me be more specific. I mean, the update fraction that we want to help the few markets. In the meantime, anyone want to argue against what I just said six nine with the fee update? Yeah. Miguel, you had your hand raised. I'm not sure if you want to respond to what I said or something else. 

**Mikel**
* No, it will be something else. Okay. 

**Stokes**
* Well, is it relevant? Because I would like to go ahead and just make the decision now. 

**Mikel**
* I mean, is it slightly related to this problem? We already have a session in Bangkok. When we were discussing the whole bandwidth measurements that we were doing. We've been able to do these measurements from other regions in the the geographical location. I can share the screen and show some graphs if there is time for that. But otherwise, like something that I want to raise is we are going to post this anyways around tomorrow. But the idea is that the all the tendency to say that six nine is fine. It's basically on the idea that you still have bandwidth, peak bandwidth available to download everything. Like what happens if you see that people struggle to to fill that bandwidth, like eventually you just get things worse. And it's like, what I want to say is that it's not linear. and what we see is that from home staker like, pretty much half of the network has less than ten megabytes per second. And increasing the target and the max like that could pretty much become a bottleneck when you're trying to resync stuff. I think that this was also something raised by Paul and Nishant on the discord channel. So yeah, I don't know. I would like to bring a bit more of the concern about having such a big increase. 

**Stokes**
* Right? I mean, that is definitely important data. but it sounds like it's a little bit different than the analysis that I did. so I'm not sure if there's a discrepancy there. Dan can. Tell you what. the hand was raised on zoom. Oh, sorry. Maybe. Yeah. No, it's all good. Ben. 

**Ben**
* And that is an important point. if the if we're running at sort of nine blobs per block. Isn't that a problem if you're also suddenly if you're snap serving, will you start losing stations? Because that's also. 

**Stokes**
* So. Yeah. I mean, there are a couple of things here. So you know, the max, like we wouldn't stay at the max for a sustained period of time. It'd be very expensive to do. and then, you know, I guess another thing to note is that we did do some, like, sneaking experiments to this point, and that was, you know, considered in the suggestion from panda ops around their work for 69. So my understanding is that at least with respect to the work they did, they feel this is safe to do. 

**Potuz**
* I think there's a misunderstanding in the chat regarding timing games, and how builders will react to the the cost of like the probability of reorgs of their Software blocks by including more blocks. It's not so easy that the builders are going to now charge more tip, and then they will include those blocks because they might be more likely to be reworked. But the situation is that the proposer doesn't have a visibility over this. So the proposer that is currently requesting the header late enough makes that decision. So if the pools are requesting late enough, then the builder is forced not to include blocks, even if they will. If they would include blocks with a higher tip, they would not when the request for the header comes already late. So this is not a. This is a matter of like the chicken and egg. And I think people should keep this into account when they are thinking about higher limits. 

**Stokes**
* Sure. But if this happens then you know the blob producer would start paying a higher tip, the builders more incentivized to include them, the proposer they. 

**Potuz**
* Are not because the header comes late. That's the point. The header. All the request for the header comes late and the builder doesn't have a control over this. The pull request from the builder at the time that the pool decides if the pool were to, like, start adjusting their timing games because of this extra tip, that could be something. But the thing is that the pool doesn't have visibility over these numbers. 

**Stokes**
* But the builder would have already made the block with the blobs in it right. 

**Potuz**
* At the time. The builder would change the header the according to change the block according to when the header is being requested. If the header request comes like ten milliseconds before four seconds, the pool builder would include zero blocks because they know there will be reordered. 

**Stokes**
* Okay, so I do think timing games are relevant to consider here. That being said, let's zoom out a bit and circle back to my question. So six nine. And that's the fraction change for eight. Okay. So there's okay Oliver. 

**Oliver (Reth)**
* I just want to quickly ask, um I know like obviously this is very late in the process. We want to freeze picture and all that. what is the potential delay here? And is there anything, my team can help on alleviating the delay? Like, I would imagine it's mostly testing. Correct or incorrect. 

**Stokes**
* I think that would be most of it. And just any analysis, you know, that we can squeeze out of the network basically. Mhm. Okay. Terence. 

**Terence**
* So I'm not aware of any consensus client team that has implemented in a way that you have fought to a different block number that the max and target are different. So we're working on a PR right now. I presume other consensus layer client team are working on PR right now. So after that's done we need testing basically. But yeah, this is something new to us. 

**Stokes**
* Right. Which is what 7742 introduces. So it's not really a surprise but it is new. Okay. So right I mean I guess there are some there's some demand to consider for eight over six nine. I think we've narrowed it down to at least those two. From there I would lean towards moving ahead with six nine again just to provide the most bandwidth that we can. And you know, if we are a month or two down the line and have some reason to think four eight is better, we could always change that. because what we can start doing today is everything around. You know this change. 7742 and any updates? The actual numbers will, you know, ultimately be a configuration change. So it is easy to scale back down. You know, if we really feel like we need to. So do we feel okay moving ahead with this with six nine and the fee update. Okay. I'm just going off the chat their support for this. So let's do that. And I do think it is important to keep doing analysis here. If we find something that is really going to change our minds, we should definitely discuss it as soon as we can. Okay, cool. So I had another note here, which is, you know, let's live in this world where we're doing six, nine.
* Do we want to include seven, six, two, three? I really think at this point we should only be thinking about things for network security, for spectra. So, for example, you know, I would think it would make less sense to talk about raising the base fee for the blobs or, sorry, the fee for the blobs. but this one actually impacts like worst case block numbers. 
* So I think it's at least worth discussing. yeah. Tony, you have something to say here? 

# For any given adjustment, do we want to include EIP-7623? [58:01](https://youtu.be/HcjuY3WDa9A?t=3481) 
**Toni**
* Yeah. Quickly. About 7623. I think we should, ship it together with the blob increase. And this was, the plan for 7623 for quite some time now. So if you remember, it was, CFI for months now. because we were always unsure if we will ever touch the blob count in spectra, and without touching the blob targets 7623 wouldn't have, had that impact really, because now the actual median throughput will increase with the target increase and 7623 only touches the worst case scenario. So I would argue that with the increased, maximum block blob count. We should also decrease the maximum possible EL payload just in order to make sure that. on the side, EL cannot have like almost 20 blobs in size while we are discussing. Like 1 or 2 more blobs on the CL. 

**Stokes**
* Right. That's a good point. I will surface, this comment in the chat from my client. I think this is probably the main argument against 7623, and Pectra is just that. It adds more things to do, and there's already way too many EIPs. We just had a pretty bad bug on Mekong. So it's not that, you know, it's not that we like are super ready to go. And this is just like a marginal add. It will add complexity to, you know, the whole fork. And yeah, we need to make that decision carefully. I don't know lightclient if you want to add anything. To your comment. 

**Lightclient**
* I mean, I think we need a picture and I'm just worried about adding more stuff when I don't think that we have super high confidence on either the EL or the CL about what we have already committed to shipping in this fork and saying this is an active security vulnerability, but no one is actually taking advantage of it. So I don't really think it's that big of a security vulnerability. Should we fix it at some point? Yes, but I see not a strong reason to fix it in the next fork. 

**Stokes**
* Yeah, there are a lot of emoji reacts to his message though. anyone want to say something else to 7623? 

**Terent**
* Yeah. For other people, doing emoji reacts. maybe 2 or 3 of them should unmute and share that perspective. 

**Roman**
* The point that has been made multiple times, but we cannot safely increase the number of blobs without decreasing the maximum possible size of the block. This is my reasoning for adding the emoji reaction. 

**Ben**
* Then, if we're worried about increasing the gas limit because of 7623 and you know you're compounding it with increasing the blobs if you don't have it in, this is the same issue. 

**Lightclient**
* So why did we agree to ship a blob increase before agreeing to do the thing that apparently is the prerequisite for the blob increase? Like now we're kind of just giving this as a writer because we agreed to do a blob increase, and we're just saying that we should, you know, it's a prerequisite. We have to do it too. 

**Stokes**
* I feel like it's always been sort of in the meta, at least over the last couple of months. So this is just now the time to discuss. 

**Toni**
* Tony. Yeah. No, I just wanted to say the same. So it was always kind of bound to the to a potential blob increase or a gas limit. gas limit increase, which is also still in the room. And yeah, for that we were basically saying now for months that 7.623 will be kind of this measurement against yeah, any DOS attacks that might originate from scaling, scaling everything up? 

**Stokes**
* Okay, so I'm hearing a lot of support for seven, six, two three along with the block increase. So let's go ahead and move forward with that. Anyone opposed? 

**Lightclient**
* Opposed. Guys we're adding three EPs in a call after we just had a three fork test net bug. 

**Toni**
* It's two EIPs, right? It's the blob increase and 7623. It's the. 

**Lightclient**
* Blob increase. 7623. And the fee change. 

**Toni**
* But the fee change is in seven six, nine one because it's basically only. Yeah. 

**Lightclient**
* But there's discussion about putting in its own IP. So yeah, you know we could put these all into one EAP. But these are like three conceptual changes. 

**Stokes**
* Yeah, I mean, I would like to decide today. However, I think there's grounds for making a decision on this on next week's AC, DC because this is primarily an L change. I don't know what would change in the next week, though. Francis. 

**Francis**
* I want to provide a like raw data that I collected, for like 7623. So although the serologic, like, block size limit is 2.8MB. Now, from my kind of like analysis over the last like last month or something, the P9 999 block size is like, well under the like 700 or 500kB. So theoretically this could help, but it could be like in, in the real world, you could not It would be like, okay, it's not that big of a deal, but I think it could be helpful to include that if we are worried about the worst, worst case scenario. 

**Ben**
* Maybe you'll be running for, because the base fee being one way, you'll be running an hour at nine blobs per block before it gets to anything that's even remotely pricey. so then you're opening up plenty of time for somebody to start sticking in vast, sized oversized blocks for no purpose, just for fun. 

**Lightclient**
* Okay, what is the failure case here? If someone does do this. I haven't really heard a compelling argument for what actually happened to the network. Like you don't kill the solo stakers if this happens. So are they offline for ten minutes or are they offline for three hours? Did you kind of keep them offline or like a very low participation? permanently. What's I mean? 

**Ben**
* I mean, you won't pay the gas for the block. That didn't happen. So you can keep putting it back in. You. 

**Lightclient**
* Don't think that there's that much of the network that's going to be negatively affected. This like we're talking about, like the bottom 5 or 10% of validators. 

**Ben**
* From what is it, 13 megabyte blocks with um. The addition of nine blocks, 13MB uncompressed. 

**Lightclient**
* Like, what's the compressed value? The compressed value is like 2.5. 

**Stokes**
* Okay. I would like to make a decision today and there's some chat to that end. I would lean towards including this myself. It sounds like only like client is the one opposed at this moment. Um. Okay. I mean, that being said, I do feel like we probably want to, like, have signed off on this because they're going to be the ones implementing it. So that does really motivate pushing it to next week, I guess. Is anyone opposed to that? The downside is just we have one week less of, you know, a spec freeze. Yeah, I'm saying six nine today and then TBD 7623 next week. And yeah, that's the suggestion. 

**Lightclient**
* Yeah I'm happy with that. 

**Stokes**
* Some thumbs up. Okay. Lots of thumbs up. Cool. Okay, great. So let's do that. And yeah, if you're here and or if you're an El client listening to this, please have a view for ACD next week. Cool. Okay. thanks everyone for that. There's a lot of discussion there, but it's a very important topic. I think that's everything on the blobs we wanted to touch on today. Let's circle back to this item that we skipped over with the sequencing of the agenda. So there was a PR to update how consolidations work under 7215. And yeah, basically, so I think where this is coming from, is that the way that Electra is scoped now, you could essentially trigger a consolidation for any validator, not just the ones that you control. And that's weird. you know, you it would be a very expensive attack, but you could imagine someone you know is wanting to troll some other validator and basically force a consolidation on them. So there is some back and forth on ways to address this. And we got to this. PR 4020. Mikhail, I'm not sure if you want to say anything else. this is from you. in any case, yeah, it looks good to me. I think we should go ahead and move forward with this.
* And, yeah, I would rather go ahead and agree to this today rather than wait another cycle. in the interest of a spec freeze. Yeah. So maybe, just maybe just add one more comment. From what Francesco said, it would cost you your stake. So it is a very expensive attack, but it could be done right. 

**Mikhail**
* You still can do consolidation. So. But what this is about. Yeah Sorry. 

**Lightclient**
* Sorry. Go ahead. 

**Mikhail**
* Yeah. There was a concern that it could cause some. So basically, this PR prevents, the target to be switched to compounding. So if it's compounding, the anyone can do consolidation to the target. And the concern was about that anyone can switch any validator to compounding credentials. And that can have some legal implications in some jurisdictions. So that's that's one of the reasons. The other one is the we have just this, in this place, the There is the way to switch to compounding upon request and in protocol, we have this automatic switch to compounding on consolidation two, which is a bit of a quirk in the design. So we're just removing that as well. And yeah that's about it. And also yeah there is the the UX trade off. So if you want to consolidate your validator you will have to first switch to compounding target and then do consolidation. This is going to be two different requests. And but that's not a big problem because if you have like say ten validators to to consolidate you should just do the switch once and yeah, then send those to ten messages or ten requests for consolidations.
* If you are a soul taker and you have just two validators, you want to consolidate them, then it will result in two messages instead of just one as per existing logic. So it's not a big UX reduction. And also to a bit alleviate this UX thing. I think we should increase the max consolidation requests to to two instead of one. So we can basically switch to compound and then do consolidation in one block. 

**Stokes**
* Yeah, I think that makes sense. And I guess one other point here is like this does actually simplify, like the whole state transition, just thinking about validator lifecycle states and how you transit between them. so I really like that. There was the here. 

**Lightclient**
* Is the compounding. Just get set today by whenever you have something as the destination of a consolidation, it becomes compounding. And the problem is that you can set any target without authorization from the target. 

**Mikhail**
* Yes. One of the concerns come from that. 

**Lightclient**
* So now you're separating the compounding from consolidation. 

**Mikhail**
* Right. So you cannot do you will have to to authorize the compounding switch first before doing consolidation. 

**Stokes**
* Yeah. And I'll just waste Francesca's comment here. It is a very simple change. And I think it does simplify things quite a bit, which is nice. 

**Lightclient**
* How do you authorize it ahead of time? 

**Stokes**
* How do you. Oh, sorry. What was that. 

**Lightclient**
* Like? Today we authorize consolidations by looking at the like, using the message sender, comparing it to the ETH one credential. Is it going to be like that again or is it different. 

**Stokes**
* No it's the same. Okay. 

**Lightclient**
* Sounds good to me. Yeah. 

**Stokes**
* Yeah. This just restricts what you can do basically. Okay. So I think the people who have looked at this before this moment are in favor. And it sounds like there's. Yeah, some support on the call as we talk through it. anyone want to avoid this? Not move ahead. Otherwise, I think we go ahead and do it for Pectra. Okay, great. Let's see. Yeah. So it does need testing. But yeah this is something that we can get to the next release. And yeah. Mikhail I can help you get this tidied up ASAP so we can keep things moving. Cool. 

**Mikhail**
* Yeah. Also requires the update to the consolidation smart contract to bump the max value from 1 to 2. But it's trivial change. 

**Stokes**
* Right? Okay. Yeah, we should track that. It is worth noting that it's okay if that doesn't change in the smart contract. It would be nice if we do it. It's not the end of the world. Cool. So let's see. I think that was everything for the next Devnet spec and should have picture in a pretty good spot. okay, we don't have a lot of time left, so we'll just keep going. Okay. I guess. Were there any very quick updates with PeerDas or anything? Any Devnet there? My sense is that they've kind of been waiting for, Pectra to settle down. 

**Barnabas**
* Exactly. So the idea is, that process is going to launch once factor five is, stable, and then everyone can revisit their code. I think most of the CL are already working on a S3 based on top of Pectra, so we didn't want to complicate things by launching some very old spec. 

**Stokes**
* Yeah. 

**Barnabas**
* Yeah. The same. True for update, by the way. 

**Stokes**
* Okay, great. 

**Barnabas**
* They both expect to arrive once Pectra five is stable. 

**Stokes**
* Okay. Sounds good. Thank you. 

**Barnabas**
* And for Pectra devnet five, then we can probably calculate with A69 change already, right? 

**Stokes**
* Yes. Yeah. So Devnet five would be essentially the final Pectra spec. 

**Wei-Wang**
* Can we confirm the scope of the Pectra Devnet 5? Definitely. Right now we talk about many. Sounds like. 

**Stokes**
* It sounds like 7623 is still up in the air for next week. I did want to leave some time for the other agenda items, but yeah, I guess. Are there any specific questions right now? Shall we? 

**Wei-Wang**
* Do we have for the CL update? Do we need to wait for this discussion before we got the release? 

**Stokes**
* Not for 7623. That's a good point. So let's see. Right. So from this list here on this issue, 7691, which is the throughput increase that would need an update for the target or. Sorry I keep calling it out. The update fraction. Let's see. Do one of the authors want to go ahead and handle that change? Mike Perry. Tony, Sam, Andrew, some of you are here on this call. Okay. We at least got a thumbs up from Tony. So, yeah, if we could do that, like. I mean, today's a holiday for some of us, but yeah, if we could do this, like, in the next day or two, that would be great. Okay, Oscar says he's writing one right now. Perfect. cool. So. Otherwise, yeah. This list, looks pretty good. Shall we? This issue 4026. I can follow up with you after, and we can double check everything if that sounds good. Cool. Okay. 
* So I think that was everything on Pectra and or PeerDas to discuss at the moment. again, very nice work everyone. I'm getting to this point. 
* Been a big one. but yeah. So now let's keep moving to the agenda. next up, we had a request to discuss another EIP 7805, which is fossil, and this is a solution for resistance. Uh. Let's see, so I spoke. Are you on the call? 

# EIP-7805: FOCIL [https://youtu.be/HcjuY3WDa9A?t=4718](1:18:38)
**Thomas**
* Yeah, yeah. I'm here. Hey. 

**Stokes**
* Yeah. yeah. Take it away. 

**Thomas**
* Hi. Thanks. I'll share my screen. 

**Stokes**
* It only shows, like, the upper corner of your screen for some reason. 

**Thomas**
* Oh. Hold on. 

**Stokes**
* I'm not sure why. 

**Thomas**
* Does this work now? 

**Stokes**
* It's better. Yeah. I think this is everything. 

**Thomas**
* Yeah. Okay. I'll just start. yeah. thanks for letting me present this. I'm Toma. I'm a researcher in the robust incentives group at the EFF. And, yeah, today, I want to talk to you guys about IP 785805, which is on for choice inclusion lists and shortest fossil. So, yeah, I don't want to take too much time. So I'll dive right in and just give a quick, context. But yeah, proposal builders operation was kind of quite successful Awful at keeping the validator set relatively unsophisticated and decentralized, I think. But builders have become like super, super centralized. On the other hand, probably more than we expected. And so today we rely on like literally two very sophisticated and centralized entities to build more than 90% of all blocks. And this is obviously like super bad for censorship resistance properties, because now those two entities can basically arbitrarily decide what transactions get included or excluded from almost all blocks.
* And so, for example, like a couple of months ago, you have like a major builder that just decided to stop censoring some transactions and for some reasons that are actually still kind of unknown, at least to me.
* And we got like this huge drop in censorship out of kind of nowhere. And so, yeah, it's directionally good in this case, but it also just kind of shows how fragile A CR is on Ethereum right now. And so you guys, know about this, but one good way to drastically improve the censorship resistance properties is just to use inclusion lists. And just to say it again, the very basic idea is super simple. It's to let the decentralized set of validators define a set of transactions that must be included in building blocks for them to be considered valid by testers. 
* And yeah, there was like a lot of research done in the past couple of years, on inclusion lists, obviously, since there was even like EIP 7547 that was considered for inclusion, but it was then rejected because of some issues regarding its compatibility with account abstraction and equivocation. but there was also some, like really cool and relevant research on block code construction by multiple parties is or the concept of view merge for, for choice. And so we took kind of inspiration from these different research threads and came up with fossil, which is actually like a very simple mechanism. And that allows multiple validators to propose inclusion lists, plural and co-construct a template roadblock made of transactions that have to be included in builders blocks. And so we kind of think of it as like a very important step forward, because fossil, what actually allows to give some power back to the validator set and allows them to like, reclaim some control over block production and reintroduce some kind of neutrality at the protocol level.
* Another important aspect worth mentioning is that fossil can also kind of be seen as a way to boost the signal provided by the solar stakers. So today, if you assume like there are like 6% of total stakers, we have to wait quite a long time, like a 1770 slot on average, I think, before a block gets proposed by a solo taker. And we can often, like, rely heavily on solo takers to ensure, like the censorship resistance properties of the network are like that. Censorable transactions are eventually included and with fossil like still assuming around like 6% solo stakers there will be like a 63% chance of at least one solo taker being in a committee if we had like 16, committee members per slot. 
* And so, yeah, here's how it basically works. There are like three main steps that I'll just briefly describe. The first step is about building and broadcast broadcasting IELTS. So each slot you have 16 validators that are randomly selected to become Ill committee members. And each of them will just like monitor the public mempool and include transactions that are pending there in their IELTS up to eight kilobytes, which is about 40 transactions per day per URL. If you take the median transaction size and then they broadcast their IELTS on the global topic over the P2P network, and what validators and testers have to do is just like monitor the P2P network and store store URLs that are broadcast until the view freeze deadline, which is at nine seconds into the slot. And basically at this point they keep forwarding IELTS, but like stop storing new ones. And in the second step it's about what the like the builder actually including IELTS and IL transactions in its block in its payload.
* So yeah, the builder will do just like the validators and will collect and store is, but it actually has additional time after the view freeze deadline to ensure there is enough time for him to see all the available ills that were broadcast by committee members. And so about like, like around 11 seconds into the slot. So two more seconds after the red line. The builder just basically takes the union of transactions across all its stored aisles, and he includes them in the the payload before the full block is, is then like just proposed to the rest of the network by the proposer. And the step three is how it's enforced. So a tester will do exactly the same. They will take the union of transactions from the stored, but in their case until the view freeze deadline.
* And then they will check whether all these transactions were actually included in the block's execution payload that was proposed. And this is kind of where the fork choice and forced comes from, because the tester will only vote for the block if it satisfies all conditions according to their view. And yeah, I'll go quickly. But I want to highlight like like Fossil Core properties. I guess the first one is that IELTS and the payload are actually built in parallel, and they only kind of need to be merged together towards the end of the slot. So that's quite nice because it provides some almost real time censorship resistance. Having multiple proposals made for makes also like a really robust to commitment attacks, but it also actually allows us to get like a super nice one out of an honest assumption. So we only need one committee member to build its ill honestly. And just like include transactions from the mempool without censoring for the mechanism to work. and then we have the conditional property.
* That just means the builder must include all all transactions. But until the block is full and the builder is also not constrained on where transactions, of the order of transactions in each block. And so these two last properties are actually quite important to just prevent IELTS from being crowded out by MeV transactions. Like, imagine if there was some dedicated block space, or like if all transactions had to be included at the top or end of the block, then we probably have seen something like ILP boost emerge. But in the fossil case, like transactions have like no ordering guarantees and they must be created before the builder actually has the last look and builds the full payload. They're also broadcast publicly. 
* So there is really no point in trying to include like valuable or MeV transactions via fossil. yeah. And all our all these are I'll just mention them quickly because it also addresses like some issues that were present in like the previous proposals. There is no 3D problem because in our case I'll stay on the P2P network and they never go on chain. we've thought about, like, handling scenarios in which transactions can be invalidated. We made sure it's compatible with other APIs, those that are considered for inclusion, and others like account abstraction APIs and PDAs and apps. we we handle equivocation. I always say that with it's quite robust against against commitment attacks. So bribing and extortion because we do have multiple validators, and multiple community members, and against following attacks.
* And yeah, it's also like critical because like, if you want to move towards like a apps or a tester proposal separation, it's, it's actually critical to have a mechanism like fossil to ensure there is validators that are unsophisticated and decentralized, involved in like building these roadblocks, before moving towards a world in which we might want to sell off execution rights to sophisticated parties. and yeah, finally, I just want to say that fossil can be seen, like, as a core mechanism to enforce chain neutrality and improve censorship resistance quite drastically. But it's also, like quite well suited for extensions in the future. So so far we've thought the most about extending fossil for blockchain transactions because like that's very obvious. But we are also actively researching how, for example, to properly reward committee members if we wanted to do so, because in the current version, we rely on altruistic behavior or how to secretly select, committee members so they can contribute to the mechanism with without actually revealing their identity, which also might be very useful. 
* And all of these are like super exciting research direction that can extend fossil to give even better censorship resistance guarantees in the future. so thanks everyone for listening. and thanks to all the authors of fossil, and we just released today a censorship resistance website using ENS and IPFs for resources that are related to fossil. So it's called fossil dot f dot. So check it out. Thanks. 

**Stokes**
* Cool. Thank you. yeah. I mean, it's really exciting to see and especially, like, the history of research that got us to this place. I guess one question I have that might be relevant for people here is if you thought about implementation at all, I don't know if you've thought about prototypes or anything like that to accompany the EIP. 

**Thomas**
* Yeah. We like, opened the EIP a few weeks ago. And now that that's all an author has starting working on a Geth implementation that although that's quite recent, Terence is also planning to work on a Prism implementation, but that's all like that's a great problem because like anyone who's willing to work with us on this, who are like pretty active and we are looking for other people to help us, on the implementation side. 

**Stokes**
* Cool, awesome. yeah. We will not get into future forks today, but, this is something definitely everyone should have on their radar. we only have a few minutes. There was a question here. How does fossil work? Any caveats?

**Thomas**
* No. so we discussed, about, like, the potential compatibility with the PBS. and it is about like, timing things. Right? So we allow for enough time for deadlines and view frees and like everything to to like not to to eat too much time for each of the proposal to go together. But it seemed like it was actually like quite compatible and that we can make it work. so we had like a lot of back and forth discussions in the inclusion lists channel on the R&D, ETH, R&D, discord. So if you want to check it out you can and happy to like yeah, work on this even more once like I don't know maybe we have also more clarity on what gets included or not. 

**Stokes**
* Cool. Okay. Well we are actually at time now and yeah, I think we'll go ahead and wrap up. I guess I'll ask, are there any closing comments? Very briefly. Otherwise that will be that. 

**Tim**
* Quick. Yeah. We didn't have time to get to it and it's fine, but I had some acid process stuff on the agenda. If people can review those before next week's call and leave any comments, I think that'd be great. yeah, just posted the link in the chat. Cool. 

**Stokes**
* Thanks, Tim. great. Okay then. nice call everyone. I think we made a lot of good progress on packaging, and I'll see you next time. 

**Potuz**
* Bye bye. 



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





