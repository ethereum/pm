# Ethereum 2.0 Implementers Call 65 Notes
### Meeting Date/Time: Thursday 2021/06/03 at 14:00 GMT
### Meeting Duration: 90 mins
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/220)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=cgH8OsCg9tY)
### Moderator: Danny Ryan
### Notes: Joel Cahill

## Decisions Made
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
| **1**   | +0.5 -0.5 reward variance | [34:54](https://youtu.be/cgH8OsCg9tY?t=2101) |

   
## Client Updates

**Danny Ryan**
[2:01](https://youtu.be/cgH8OsCg9tY?t=121)

* Lets start with Lodestar updates

**Cayman Nava**

* Hello everyone. We are passing the alpha 5 spec tests, and working on getting to alpha 6 but we first want to get the preset config split stuff finished first.
* Other than that, we’re working on Altair interop, by syncing to the Teku devnets. Thats been really helpful, we’ve fixed a bunch of Altair performance issues and we’re currently syncing to the head of the recent one.

**Danny**

* Cool, lets do Prysm next.

**Raul Jordan**

* We’ve had quite a lot of work done on Altair. Significant updates on networking transition work, by end of this month we’ll be ready for multi-client testnets.
* We’re still ironing out a lot of things passing spec tests, and aside from that our team has also been looking into sharding work trying to understand were we can be most impact on on that front. 
* Still working to align with eth2 API effort, its been one of the biggest engineering challenges for us, spanning a few months for now but we’re close to the finish line.

**Danny**

* Great, thank you. Teku?

**Meredith Baxter**

* Hey everyone. We finished implementing the Altair REST APIs and we now have remote validation working on Altair.
* All the outstanding eth2.0 API PRs have merged. 
* We updated Teku to ingest new config file format. For backwards compatibility we have the git spec REST API endpoint, including the constants that have been removed from the new config – We’re just manually injecting this for now. 
* We removed our Java BLS library – it was too slow to be useful at this point. 
* We have been working on updating eth1 tracking to fix an issue discovered through Rayonism – We had been using a static follow distance and instead need to calculate follow distance based on timestamp. That fix is implemented, but its toggled off for now because we need to do some more real world testing. 
* And finally, we’ve launched a couple of devnets to test the Altair transition – I won’t try to pronounce them – through that we found a few issues in Teku. We’re not publishing updated ENRs correctly, and we had a bug in our transition logic which caused us to produce an invalid chain on the first devnet. The transition bug is fixed, and we’re still looking into the issue on ENR publishing. On the current devnet, we’re seeing some issues with sync committee gossip that need to be tracked down. We’ll likely keep that current devnet up for a while so that we can get to the bottom of networking issues. If any other teams would like to join that devnet, and you need validator keys, you can reach out to Adrian.

**Danny**

* Great. Yeah thanks for putting those devnets up, thats a great way to get started. Nimbus?

**Zahary Karadjov**

* We started to work on Altair late because we were focused on the merge recently, but our focus is now entirely on Altair. We hope to be ready for the first testnet by the end of this month.
* Our REST API will be coming out of beta soon. We’ve addressed a lot of feedback from our endusers with small incompatibilities.
* We are introducing the use of multi-cores in Nimbus, and so far we will be only focusing on BLS key verifications. Since the majority of CPU usage in our client will be able to do verification of attestation signatures, we hope that this will be enough to take advantage of all cores, without changing the architecture.

**Danny**

* Very nice. Remind me, are you doing any sort of batching on the wire when attestations are coming in?

**Zahary**

* Yes, we’ve introduced a special form of batching were we bundle the incoming attestation into groups, which could mean either 16 attestations arrive in a short interval of time (10 milliseconds), or the 10 milliseconds elapse, and we verify the number of attestations that arrived during that time. Usually these bunches are grouped, we receive many more attestations than 16 during this time-frame, so thats the granularity that we do right now. If any of the signatures are invalid, you have to verify each individual attestation again, which is a potential cost if someone is attacking the network, but we believe that the trade-off is worth it.

**Danny** 

* Great, thank you. And Lighthouse?

**Paul Hauner**

* Hello everyone. We have got our Altair implementation syncing and following the chain with Teku, and perhaps Lodestar (I’m not sure). Once again, big thanks to Teku for doing the legwork on setting that testnet up.
* We’re presently on alpha spec 6, and we’re passing the new config format and we have backwards compatibility to the old format.
* Loosely speaking, we have all the features required for Altair implemented, but now we’re working on updating some components to alpha 6 – namely our sync committee. And we also need to get everything reviewed and merged into our primary branch. Presently we’re doing interop with a branch that merges together a few work-in-progress PRs – so we’re doing interop on the branch with work in progress PRs. No doubt we also have some Altair issues that we don’t know about yet that we’ll have to deal with.
* We’ve done today a pre-release for the first time, so we’ve done a bunch of outgoing comms to users to tell them not to run it on mainnet and explain what we’re doing with it. If there’s any power users on this call running Lighthouse, I'd suggest giving it a run on testnets – theres some good memory improvements and we’d like to see how they run on lots of different hardware.
* Finally, we’re expecting to publish a release next week, assuming the pre-release goes well. This is not the full feature set we announced previously, but it is earlier than we initially announced so we’re just going to split up those features into two releases. We’re expecting to have the rest of the features, including Doppleganger and Altair being released later this month.

**Danny**

* Great, thank you. Moving on to Altair discussion.

## Altair Discussion

[feature: reduce reward variance](https://github.com/ethereum/eth2.0-specs/pull/2453)
[9:56](https://youtu.be/cgH8OsCg9tY?t=596)

**Danny**

* It sounds like engineering progress is moving along. Thanks again for setting up those testnets, I think thats a great way to start.
* We did patch the test spectors for alpha 6, there were a couple that were incorrect. I accidentally had a couple that were missing, but the tar’s on that release should be good and correct at this point. We are targeting an alpha 7 tomorrow, pending discussion of this feature. So I’d like to shift the discussion into that. Potuz has identified how the sync rewards work, and can create a pretty asymmetric-ness in rewards that can be unfair based off how you win the lottery or not – as in if you get selected for the sync committee  – you see something like a 15% boost in rewards, and if you don’t (which could happen to a not insignificant amount over the course of a year and half), you forgo those rewards.
* So there are two PRs up, I only linked to one – apologies – one essentially shifts the entirety of the sync rewards to be a penalty. So essentially by default you do get all of these rewards, and then if you are in that sync committee, you don't get that penalty and reduce that lottery effect or eliminating the lottery effect in the positive direction.
* Vitalik has an alternative, which is 2453, which modifies some of the logic, reduces the magnitude of the effect of this reward, and has not only a reward but also a penalty for non participation which in effect reduces the magnitude of the effect of the lottery to something like 3% rather than 15%. Vitalik also noted in this PR that the sync committee being as valuable in the long run as proposing was probably not a good idea. So both of these should reduce the magnitude of the sync committee.
* There’s two questions here. One would be the fact that this is a breaking change, and it would need to be introduced very soon. It’s very small, the test vectors would be rerun and we’d get good coverage on this thing, but it is breaking none-the-less. The other is the balance between these two, I think some have signaled into Vitalik’s, some for Potuz. Vitalik – can you make the argument for your PR?

**Vitalik**

* Basically the way to think about it is status quo +1 if you participate, 0 if you don’t participate. Potuz’ proposal is 0 if you participate, -1 if you don’t. My proposal is 0.5 if you participate, -0.5 if you don’t. * The two biggest arguments in favor of mine were: if you do peer penalties and no rewards, then this introduces the first proposer reward that is not directly computed as a multiple of rewards for things that it includes. That breaks the invariant that we currently have about how proposer rewards are calculated, which is not fatal but it does make it continually harder to make sure that rewards add up to one in the future. The second reason is that we’ve historically had a goal of not wanting innocent people to lose a lot of money – during situations like validator leaks – if you do the +0 -1 thing, say half the validators are offline then half the next slot proposers will be missing and that means that if you are part of the committee during that time you’ll lose quite a bit. If you have 0.5 and -0.5 then being in a sync committee only becomes a net negative if more than 50% of participants are missing – and even then its a much smaller net negative.
* I saw Potuz replied in the discord that proposer are rewarded by what they include. Just clarifying what I mean – if you do the +0 -1, proposers entire reward comes from the idea that if you include a message that causes someone else to get +X, then proposers would get +X/7. Whereas if you do the +0 -1 thing, you would have to give proposers a reward, but that reward would not be any kind of +X/7. It would be like +(something else)/7.

**Danny**

* Question on the penalty mechanism here. These rewards are only run in process sync committee, which are only run if there is a block, and so in the event that there isn't a block, no one gets a reward and no one gets penalized in both proposals, correct? 

**Vitalik**

* That’s a good point. Hmm. That makes things even weirder, especially for the more penalty-based approach, because that means that you can gain by knocking proposers offline – which is generally the sort of thing we try to prevent. I guess that would be an argument in favor of keeping the penalties milder.

**Danny**

* Right.. you can either do your job or DOS proposers. But your job is also entangled with getting blocks online with attestations, so the incentive to DOS is actually extremely minimal.

**Vitalik**

* Potuz was saying that the penalty computation is not correct. Looks like Potuz just jumped in the call.

**Potuz**

* The way that PR works is you get the reward and you don’t really get a penalty. You just lose that reward if you don’t participate in that particular slot. The worst thing that can happen to a validator that is not participating – on my PR – is exactly what would happen now as it is in the specs.

**Vitalik**

* I’m confused. Then how does that address the lottery issue?

**Potuz**

* Everyone gets –  by default – the sync reward upfront, and if you're not participating in it, you just take it back from it. So it’s not really a 0 -1. In your PR, it is an actual penalty.

**Vitalik**

* Oh – so you’re saying you’ve made a new approach. You’re saying in this new approach that the sync committee reward is just always by default given to everyone, and its even given to people that are not a part of a sync committee, so that it doesn’t get modified by a probability factor.

**Potuz**

* Exactly. The proposer does get penalized if he doesn't include a sync reward.

**Vitalik**

* But then does this not make the incentive to participate in sync committees and the incentive to include sync committees signatures fairly tiny?

**Potuz**

* The proposer gets an award according to how much he includes.

**Vitalik**

* But it’s 1/7 of something much smaller right? Like if there is 10,000 validators and there is 100 sync committee members: for the status quo if you’re in a sync committee and you get included then you get +100, and if you don’t get included its 0, and everyone else gets 0. But with your proposal – if you’re not in the sync committee then you get +1, and if you’re in the sync committee and you participate you get +1, and if you're in the committee and you don't participate you get +0. Am I understanding that correctly?

**Potuz**

* Exactly.

**Vitalik**

* So the incentive to participate in the sync committee does go down from being +100 to +1.

**Potuz**

* Yes, that is true. So far participants, the incentive goes up. However, you can make the penalty independent in that PR. So you can increase the penalty by quite a bit so that it actually becomes negative, without changing the proposal mechanism.

**Vitalik**

* Okay, I see. But then the proposer reward is it +1 * 1/7 or is it…

**Potuz**

* It is exactly as it is now. Same numbers. 

**Vitalik**

* Okay, so for example lets say 80% of people in the sync committee get a reward or participate. Then there would be 80 people that get +1, then 9900 other people that get +1, then 20 people that get plus 0. Would the proposer reward bet 99.8% of the maximum, or would it be 80% of the maximum?

**Potuz**

* It’ll be 80% of the maximum.

**Vitalik**

* That still is a bit decoupled from rewards, but I guess that decoupled in a less harmful way.
* Hmm. My main concern is you are cutting the reward down by a factor of 100. Cutting down the incentive by a factor of 2 seems reasonable, but cutting down the incentive by realistically a greater than a factor of 100 feels a bit on the risky side.
* As a client developer for example, say I make a custom client and just never bother to code the sync committee code I would still get over 99.9+% of the rewards. You could fix that with penalties, but then we’re back to having penalties.

**Potuz**

* On the incentive part – say you already are in the lottery and you’re in the committee. Given that conditional probability, you’re now evaluating whether or not you should include or not include your signature. So given that conditional probability, I think my proposal doesn't change anything. You lose the exact same that you would gain by participating.

**Vitalik**

* Well status quo is that being on a committee is +100 vs +0, but here you’re saying its +1 vs +0.

**Potuz**

* So currently if you’re not participating one slot, you do not get that reward for that slot. And it’s exactly the same reward that you would get for the penalty. So in my situation it is exactly the same. If you do not participate in the slot, you just get a penalty for what you would have gotten for that reward.

**Dankrad Feist**

* The question is that penalty the same magnitude that the reward is now.

**Potuz**

* Yes, so currently it is now set up that way. But it is independent. You can just change that parameter and make it harsher.

**Dankrad**

* So that means that actually your proposal is something like +1 for participation and -99 for penalty? Except the +1 also applies when you aren't in the sync committee.

** Potuz**

* That’s correct, but I don't see the -99 analogy. The penalty only applies when you don’t participate in that slot. 

**Dankrad**

* I think Vitalik question was – okay you get this tiny reward every slot that is 100 times smaller than it is now, because right now we have this huge reward when you are in the sync committee but none when you are outside of it. So making it that much smaller, and you give it always. I think Vitalik understood that the penalty is just a negative of this tiny reward, but I am understanding you now that this penalty is actually much much larger.
* Basically 100 is what our number for what the reward is now.

** Vitalik** 

* Right, but then in that case if the proposal is +1 -99 then the problem that you’re in the sync committee during an activity leak you’re going to lose a lot.

**Potuz**

* I think so, but you will only lose what you already gained, so you lose less than what is in your PR. In your PR, if you do not participate, you actually have a negative income. 

**Dankrad**

* So you’re proposal is equivalent to say we have a universal basic income for all validators no matter what they do, and then we add a penalty if you don’t participate in the sync committee which is exactly equivalent to taking on average that universal basic income away.

**Potuz**

* That is correct.

**Vitalik**

* Right, okay, but if the penalty is just taking away then its +1 +0, not +1 -99, so that still means the incentive is small.

**Dankrad**

* No no, the incentive is large in this proposal. The problem now is you have to inverse the lottery. So before you had the lottery – oh you can be lucky and gain lots – and now we have like a death lottery, you can be unlucky and selected exactly when (cutoff)

**Potuz**

* I agree its an inverse lottery, but that inverse lottery in general that lottery only applies to a tiny set of validators. Its not only that you have 512 (cutoff again)

**Dankrad**

* Exactly, but you can’t just be unlucky and that can feel pretty horrible

**Potuz**

* In the other way, everyone is unlucky. The way on Vitaliks now, which actually Vitaliks PR reduces a lot the variances, but even when computing with those numbers you see that you get 17-18% validators would be over four times in a committee in two years. And only 11% of validators would not be in any committee in two years. So thats a 15% of the rewards difference between those two.

**Dankrad**

* The other possibility is to just make the committees larger overall, even if we don't currently foresee anyone using it, we could just make them ten times larger.

**Vitalik**

* But does that mean we are bringing back the aggregate public (cutout), does that mean we have to change things on … yeah that feels like a nonstarter. Hmm.
* It does feel to me like there’s this kind of fundamental trade off of theres either a lottery or theres a (cutout the next few words) – … during a leak-fee the penalty lottery becomes pretty severe and thats at least a violation of a property we’ve been trying to uphold
**Dankrad**

* The other thing is that after the Merge we probably have a much bigger issue than this lottery, with the MEV lottery, so its not clear that we’re gaining much by optimizing this now. Maybe this problem is tiny to what we’re going to inherit – and this kind of feels a bit, yeah

**Vitalik**

* Right, so the post merge lottery will be you get elected as a proposer at the same time there happens to be a large market movement (cutout)

**Danny**

* You’re breaking out pretty bad

**Vitalik**

* Sorry. I was saying we can calculate the size of the sync committee lottery. You gain the equivalent of one and half weeks of revenue, and one and a half weeks of revenue for a single validator is going to be something like two eth multiplied by 3%, so something like 0.06 – 0.1eth. So I can easily see that being much smaller than MEV lotteries.

**Dankrad**

* Yeah, one block can probably net you something like more than that in eth even. We need to fix that as well, obviously, in some way.

**Vitalik**

* Mhm, agreed. I feel like MEV we’re never going to fix 100%, there’s always going to be very unusual market crunches.

**Paul**

* We are happy to implement either of those two. In terms of complexity, its fine. Not a problem for us.

** terence (prysmaticlabs)**

* Yup, same here.

**Adrian Sutton**

* Same here. I guess the one concern I have is that we’re struggling to come to a decision. So I guess to step back – the other question to ask is if we don’t fix this before Altair, how much of a problem is it and how soon? If it waited until next fork, could we pick one of these two solutions and implemented it, is it a problem? Or it’s probably two forks away, given the merge is next. \

**Danny**

* Right, I think probably for one the constant is too high to begin with. Thats an easy fix. I think it would be better to put one of these two in, than not. But not catastrophic if we let it go.

**Adrian**

* Yeah I guess the other variant of that is lets just pick one, practically randomly – we don’t have to agree on it, just pick either – put it in, then we can continue the argument and change it if theres a reason.

**Dankrad**

* To me after this discussion, it feels like the +0.5 -0.5 variant is the best because it minimizes variance. It’s only 0.5 reduction variance, but thats better than nothing so I would go for that one.

**Danny**

* Does anyone else feel strongly one way or the other?
* (Silence)
*Okay

**Vitalik**

* So does that mean we’re going with the +0.5 -0.5?

**Danny**

* I would like to do that because I think it’s reasonable and it’s simple. And it generally achieves our goals.

[34:54](https://youtu.be/cgH8OsCg9tY?t=2101)

* Okay, we’re going to do a final review on that PR, and likely merge it today and get it out in alpha 7.

## Altair Planning
[35:11](https://youtu.be/cgH8OsCg9tY?t=2111)

**Danny**

* Generally, it sounds like people are willing and able to target something more substantial than these short lived devnets – end of June, maybe first week of July. I think Proto, (inaudible name), and myself will put some work into planning and getting some configuration parameters and some timing in place to plan something more coordinated than the short lived testnets. I would encourage – maybe Adrian – to stand up an alpha 7 version of what he did this past week, I think that was really valuable. From there, in the next two weeks, we will pick a date and a set of parameters for an official more coordinated testnet.
* Assuming that goes well, and we get some fuzzing action going, and we continue to enhance the tests, that would be a positive signal towards moving towards picking upgrade dates on our two existing testnets. Probably doing another testnet in the meantime, and then looking towards mainnet.
* I think the big unknown for client teams sounds like – sure the big bones are in place, the tests are passing, but we want to get some more time to sit with it and more time to test and iron out the bugs. Security obviously is a priority, and we will make informed decisions over the next few weeks.

** Mehdi Zerouali** 

* Quick question. Is Alpha 7 expected to be the final spec change? At least in terms of consensus code?

**Danny**

* Yes. Alpha 6 was also the final expected spec until Potuz identified that asymmetric issue with rewards. So yes, it is the intention, unless something serious with security is identified, it will be stable.

**Mehdi**

* Sweet, thanks.

**Jacek Sieka**

* What about the state group change?

**Danny**

* Whats the state of that conversation?

**Jacek**

* There is kind of agreement that its useful, there is one contention point that there is backfilling which is considered complex for some kinds. The proposal is to make it into a two phase operation so that on this fork we make the change to the beacon state, and on the next fork we backfill existing values as sort of a one off operation.

**Danny**

* So the alternative that meets the same need is on the network side, serving batches of blocks along with a state root list root, and defining a network format that gives you the extra little piece of data which is 32 bytes to be able to prove against the current items and state. Right?

**Jacek**

* Sorry can you ask again, I didn’t really understand the question.

**Danny**

* Right now what we want to do is to be able to serve batches of blocks against the block root list, right now that is obfuscated in historical roots by combining those two lists. What that looks like from an SSE proof, if I wanted to serve you the block roots, is I can give you along with the block roots the 32 byte root as a single proof. That 32 byte root is the root of the state root list for that batch – historical batch. So if I define a network format that allows me to pass essentially a small proof, which is the 32 byte root, and the block roots then I don’t have to change the state. Right?

**Jacek**

* Umm, I think it’s the other way around. I think its that once you do have a state, you have the ability to verify and batch of blocks, any 8k batch of blocks that you happen to have. For the whole history of eth. Right? So the idea here is there are a few use cases. The first, is the weak subjectivity thing. You are given a state that you already trust, and with this change you can quickly prove that any batch of blocks are apart of that particular state. Whether you receive that from the network or disk or wherever else. The other nice feature about it is gives us a natural identifier for a days worth of blocks. We can use that later on for archive purposes and its very easy to coordinate around these chunks of blocks. It allows easy out-of-bands transfer of these chunks of blocks. For example, when you want to dig into the history of voting, you can very easily prove that a particular block was a part of a particular state that you are trying to work with.

**Danny**

* Right. I guess for a number of those use cases, say for weak subjectivity sync where somebody is giving me batches of blocks, they can give me the batch of blocks along with a single 32 byte root and I can prove it against what is currently in the state.
* So I’m saying if no change happened, you can define a batch block format, which is essentially a batch of blocks and a small proof, where many of those cases you could just pass those along rather than batches of blocks. I’m not saying that is optimal, I’m just saying if this didn’t go in this would be the alternative.
* What is the state of the PR with respect to testing and – okay so the current state has, yeah okay so at this point would could introduce a breaking change because Alpha 7 is going to introduce a breaking change, I want to hear what other engineering teams think.

**Paul**

* To be completely honest from our end, we haven’t been particularly focused on this one. I think we’re pretty full with bandwidth, and this one got left out. But we can look into it.

**Terence**

* Yeah, same here. I haven’t really studied the PR as well. I’ll have to look at it again and then get back to you guys.

**Danny**

* Okay, so if we delay Alpha 7 until Wednesday (June 9th), then we can make a call on this. Alpha 7 looks a lot like Alpha 6 as of now, so it’s not adding too much in complexity. Is that reasonable? Can I get people to look at this by end of Monday?

**Paul**

* Yeah totally. I like what the PR is delivering, I just cant make any calls on implementation at the moment.

**Adrian**

* Yeah, I guess my only concern is the backfill stuff, if we did it in two pulls I think its simple to drop in …

**Danny**

* So if we don’t do backfill, is this still useful?

**Adrian**

* Well I think the thing for me is we probably wind up with a two fork approach anyway because its the simplest way to do this. Its kind of where eth1 landed on this approach a while back. If we start building the new state now, then next fork we can do the backfill. And we’re kind of where we are if we punt this, even if we sort out backfill its going to push it into the next fork anyway. So I can’t think we get the usefulness next fork regardless of how we do this. And there is a risk maybe it becomes two forks away if we cant sort out the backfill by next fork.

**Danny**

* I see. Is there a reason that you cant pre-set the backfill so that you can do the backfill at the same fork? Or is it just kind of a compromise at this point, because backfill isn't ready?

**Adrian**

* It’s probably doable, you’d have to get client releases out that add tot he storage and keep stuff around that we don't currently keep. But that increases the engineering scope quite significantly over the change. We could probably do it, but its a big change that we’d be putting in late at that point.

**Danny**

* I wasn’t necessarily saying do it for this fork, but that if the backfill was going to happen at a fork later from now, and this isn’t necessarily entirely useful without the backfill, then if you can batch both together and do it in a next fork then you’ve gotten the usefulness at the same point in time.
* I need to study the PR as well.

**Adrian**

* Yeah, I think backfill is likely to be workable if we have the time to do it well. That is probably preferable to shoving in something in, especially if its not particularly useful. I’d be happy to be told that if building that state now is useful, I think we could fit it in.

**Jacek**

* It is usable in the sense that we can compute the backfill a day before the fork. We can actually ship that as a constant in clients way before the next fork. That means we can start using this feature right after the fork. By shipping that backfill together with the client in the next client update after the fork. The difficulty doing the backfill is you can only create a constant for up to – like theres only a day of data in the state, then its lost. But that doesn't mean you cant ship a new version with the backfill. By doing the fork now, all the clients start recording this data in the state. If we do not do the fork, we will have to record the data out of state until the next fork – and then do the backfill. For us, it doesn't really matter much, we can just attach stuff to the beacon state in our storage, but it does increase implement ion complexity. So I would say it is useful to get it in now in this state, and it becomes immediately useful when clients make a new release.

**Adrian**

* Yeah, thats a good point. I hadn’t thought of that. I think that is a strong argument of doing a two fork release regardless, because you can get the benefit very quickly, and its just so much easier and simpler to test. You keep the property of one state plus a block, and thats what we need for the transition.

**Jacek**

* Yeah it’s a good compromise. I agree.

**Danny**

* So lets study up on the PR. I am worried about scope creep on Altair, I know that we’re making a breaking change on the way sync committee rewards work in the next couple of days, but thats a few lines and the testing remains largely the same. Whereas this is kind of a larger unknown item. Given that we are delayed on Altair, and given that one of the reasons for Altair is just to kind of do a warm up fork, I just want to caution digging deep into a new feature.

**Jacek**

* As Proto mentioned in his comments, the actual change is one line, two lines. One in the beacon state, and one in the historical batch calculation function. We already calculate all this data in the current version of the clients, its just that instead of storing one group we will be storing two.

**Paul**

* Not trying to poop on this idea, it does add work in terms of storing the stuff in our database, we have to spread that thing out. I don’t think we can just copy the existing code we have, so there are some more changes there than just a few lines in the spec.

**Proto**

* I think even though I like to minimize the spec changes, we should really take the backfill serious. I am also worried about scope creep.

**Paul**

* Do you mean take it serious as in don’t do it in a two fork solution?

**Proto**

* I mean you will have to test a two fork solution, we have to document a two fork solution, and that has to all happen in parallel with the already delayed fork.

**Danny**

* Meaning don’t put this feature in unless you’ve figured out what the second fork looks like. Which takes more time and effort at this point.
* Okay, we are not quite running late. Let’s continue. We’ll continue that discussion on Altair the next few days on the PR. Moving on to 0x02 credentials, the author of that PR is here. Would you like to give a TL;DR on that?

## 0x02 credentials – [53:12](https://youtu.be/cgH8OsCg9tY?t=3192)

[0x02 PR](https://github.com/ethereum/eth2.0-specs/pull/2454)

**Joe Clapis**

* I’m Joe Clapis, joined by Darren Langley from the Rocket Pool team. We’ve been paying attention to the merge quite closely as you might expect. I don’t want to assume everybody has read that PR, so I will summarize it really quickly, discuss our proposed solution, and go from there.
* Right not there exists cases where a validator isn’t owned entirely by one party, or its not owned by the party running the consensus client or execution client. In those cases, we still submit that the owners of that validator should be entitled to their fair share of all of the rewards that are generated by validation duty.
* The 0x01 withdrawal prefix solves this problem for block proposals, and for attestation rewards by sending them to an address on eth1 during a withdrawal. That address can be a smart contract that handles the distribution logic appropriately.
* With the current merge approach, priority fees for transactions that are included in blocks are sent to the blocks coinbase address, which is set by the execution client owner as a command line argument. It’s not controlled by the validator owners, so there is a decoupling there.
* This is a problem because the execution client owner can take those priority fees for themselves by simply setting the coinbase to an address they control, and not distribute those rewards to the validator owners. This is a problem because the execution client owner – they take all of those fees and the validator owners don’t get their fair share of those rewards. That’s kind of the issue here.
* In a decentralized staking context, we can’t force a node operator to share with the rest of the pool – for example by setting that coinbase address to a splitter contract that handles the delegation appropriately. If those node operators behave selfishly, and they pocket those fees, it means the overall return is diminished for the stakers that invested in that validator but who don’t run the execution client. That means decentralized staking solutions based on this model don’t really have an equal footing compared to the other platforms. That, in a nutshell, is the TL;DR of the problem.
* Now a solution has to fix 4 criteria that we’ve come up with. 1) It has to allow for fair distribution of the priority fees to everybody invested in that validator.
* 2) It has to scale to arbitrary balances. This is one of the sticking points with us. If you go via a punishment model, for example, where you withhold the initial investment into a validator that the node operator made, you can only punish them up to that investment. You can’t punish them beyond it. If somebody abuses this mechanism could accumulate rewards beyond that. So that punishment model doesn’t really scale.
* 3) We need something that doesn’t interfere with existing validators on mainnet today that use the 0x0 or 0x1 prefixes. Based on some discussion we’ve had in the Eth R&D discord, it turns out there is 3200 validators that use the 0x1 prefix on mainnet right now. They didn’t sign up for any of the changes that need to be made to support a solution to this problem, and we don’t want to enforce those on them. So we need something that doesn’t interfere with all of the validators today.
* 4) We want something that doesn’t add any appreciable complexity to the Merge. As we’ve heard today, it’s already gone through some delays and we don’t want to further exacerbate that problem.
* With those 4 criteria, we started looking for a solution within the Rocket Pool protocol itself, and we couldn’t find one that fits all 4. The problem really ends up being scaling, and those being able to steal arbitrary rewards in perpetuity. The decision we came down to was this needs to be addressed at the consensus protocol layer. We workedshoped this with a couple of the core devs in the R&D discord, and we came up with a potential solution.
* 0x02 is a new prefix. It is an extension of the 0x01 in that it also specifies an eth1 address to withdraw to when the validator exits, but it comes with an additional condition – blocks proposed by 0x02 validators are only valid if the coinbase for that block is equal to the withdrawal address set in the withdrawal credentials.
* Mikhail wrote some sample code on the PR for that. It looks promising, its actually a pretty light change. This issue would have some implications for coinbase logic for the execution client, as well, especially in the case for a lightclient provider, like Infura. But his code addresses that problem too.
* This proposal has benefits not just for Rocket Pool, but also for users beyond Rocket Pool. Blox staking could provisionally use this so they don’t need to internally manage a map of the coinbase rewards that they earn, to the withdrawal addresses for all of their clients. That is something they have specified they would like to investigate.
* So at the end of the day, thats not the only solution. It is a promising one, but its not the only one. It’s just the current mechanics disincentivize decentralized staking on Ethereum, and we are simply looking for some solution that levels the playing field for all the platforms.

**Danny**

* Alright, thank you. So for one, I don’t think we’re going to come to a solution on this call, but I do think this is a good educational context for everybody.
* I do see the problem. I think the naive solution of fraud proofs or something that could burn somebody's capital does, as you pointed out, have a limitation on how much can be taken. Especially if withdrawal credentials cannot initiate exits from the smart contracts, then they can just hold on to that validation capital forever.
* 0x01 was put in place as a compromise because it required no consensus changes to support and just a future promise. The 0x02, for it to be enforced at the point of Merge would require some line changes to the Merge, and will therefore encumber that process some. Ultimately it ends up being a feature request on top of trying to do the Merge, which in general we have been trying to avoid.
* There are two potential paths there. One would be to try and avoid that and not define 0x02 until after the merge, which I’m sure the people that want to use it would not necessarily like. The other alternative, is that there is a time between the Merge and when 0x02 is actually forked in, where you can be using 0x02 but you don’t actually get the guarantee of the enforcement.
* Given that this call is primarily focused on Altair, and shipping that, I don’t think we’re going to get too far into this. I’d be curious if anyone has any remarks.

**Dankrad**

* Quick question, why not just fork this in for the 0x01, that seems to make more sense to me.

**Danny**

* Because there is 3200 already using the 0x01, and its an unknown implication change for the people already using it. But I suppose the setting of the coinbase was already an unknown introduction to that, so you could argue both ways probably.

**Dankrad**

* I don't know, I would disagree. My assumption is that the withdrawal dress is the owner of the funds, and whatever you get as a return on block rewards is part of those funds. Shouldn't the coinbase be signed by the withdrawal key in this case its a BLS key as well.

**Danny**

* Right, so you’re saying the issue exists with 0x0 already as well.

**Dankrad**

* I think so, I might have given someone – I might have a contract with someone to stake for me, and I keep the withdrawal keys. Now suddenly it changes, and before the only way they could extract value is extortion but now they can propose blocks for their own eth1 address.

**Adrian**

* I guess the other way of looking at that it would have been perfectly reasonable to pay the inclusion fees to the validator balance, which would then put it under the control of the withdrawal key.

**Joe**

* That was one of the solutions we looked at originally, and we decided to not go down that route because it adds an extra synchronization portion between the execution and the consensus layer.

**Adrian**

* Yeah, I don’t mean we actually do it. I just mean logically, if it were paid there, it would seem quite reasonable and have the same net effect as having the coinbase address requiring to be the same as the withdrawal address.

**Dankrad**

* And now im going to saw the exact opposite of what I just said. I just realized that it doesn't make sense because the only thing the coinbase address receives after 1559 is the tip. A tip can also easily be paid out of band. So this is kind of like, I agree it should be paid to the validator owner, but theres actually no way to force it. If we make this kind of change, then you can still easily get someone to pay you out of band.

**Joe**

* This doesn’t solve side channel problems, and it’s not intended to solve those.

**Danny**

* It doesn’t solve MEV as well. That can go to any address.

**Joe**

* Right, it’s not intended to solve MEV. Although if I understand right, the way FlashBots works is they use the coinbase to do that distribution, so it might provisionally help there as long as you play along, but again this isn't intended to solve the side channel problem and I would submit that ignoring it because side channel problem exists isn’t very fair because this problem still exists for honest node operators.

**Danny**

* But there not necessarily acting honestly if they put a different coinbase in, right?

**Joe**

* Yeah, and there’s also people that don’t know how to run MEV, but can still leverage this mechanism.

**Micah**

* So I worry that by making it more financially profitable to accept transactions over a side channel makes the situation worse, because you’re saying – hey im about to produce a block, if you pay me over the side channel, im willing to work for less because I'm going to get 100% of that. And if I have to pull a transaction out of gossip, that ends up going to someone else, so I’m just going to ignore gossip transactions because that gets distributed to 100 other people.
* And so we’re kind of creating and incentivization – hey its cheaper to send transactions over the side channel because block producers get to keep the whole thing. Whoever is actually running that execution client gets all of the side channel stuff, and they only get a very small percentage of the gossip tip transactions. I worry we’re actually disincentivizing good behavior of transaction submission and block producers in other ways by encouraging side channel work.

**Joe**

* It’s definitely a related part of the problem, and perhaps an entire solution needs to account for both the coinbase issue we’ve highlighted and side channels. We don’t have any solution to the side channel thing, we just have a solution to the coinbase problem.

**Micah**

* My worry is the side channel problem is insurmountable because you can always do side channel payments. As long as you’re not required to pay the miner, if its entirely optional like the tip for 1559 is, then ultimately its the block producer that gets to decide the transaction order and whats included, and getting out of that is a really hard problem.
* I’m concerned that solving half of it just makes it worse.

**Mikhail Kalinin**

* I just wanted to add if we enforce this logic for 0x01, then we remove the option of changing the coinbase, so it will be the same address because we don't have a way to change the withdrawal credentials on the beacon chain – so thats something to consider if we go this road.
* Also if we don’t want to add extra complexity to the merge, and we will likely enable this logic after the merge (if we decide to), then there will be a period of time where coinbase is configured as it is now, and that would change the behavior that users are already used to having for 0x01, and that will probably be an issue for them. That’s why the new prefix makes sense.

**Danny**

* Okay, this PR is up for continued discussion. I think that everyone has a good introduction to the problem at hand. I do tend to think that half solving the coinbase problem exacerbates the side channel problem.
* I don’t think we need to make a decisioned at this point, but if you are interested in chiming in please jump into 2454, and look at the withdrawal-credentials chat in the Eth R&D discord. Thank you Joe.

**Joe**

* Thank you.

**Danny**

* Okay, longer meeting than usual. Lets wrap things up. Any research updates today?
* No response
* Any other spec discussion other than what we’ve been discussing for the Altair context?
* No response
* Additionally, if you weren’t on the merge call this morning, there is a merge PR up for transition total difficulty and dynamically calculating that at the point of fork.
* Okay, and other closing points?
* No response – Okay we will close for today.

-------------------------------------------
## Attendees

* Ansgar Dietrichs
* Danny
* Paul Hauner
* Adrian Sutton
* Mehdi Z
* Cayman Nava
* Protolambda
* lightclient
* Zahary Karadjov
* Adrian Manning
* terence(prysmaticlabs)
* Hsiao-Wei Wang
* Meredith Baxter
* Parithosh Jayanthi
* Pooja – ECH
* Ben Edginton
* Mikhail Kalinin
* Dankrad Feist
* Joe Clapis
* Carl Beekhuizen
* Langers
* Aditya Asgaonkar
* Jacek Sieka
* Vitalik
* Leo (BSC)
* Trenton Van Epps
* Mamy R
* Micah Z
---------------------------------------
## Next Meeting
June 17th, 2021





 

