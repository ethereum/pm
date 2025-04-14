# Consensus Layer Call 133

### Meeting Date/Time: Thursday 2024/5/2 at 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1031) 
### [Audio/Video of the meeting](https://youtu.be/LazOhUu1Tew) 
### Moderator: Terence
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
133.1  | **Confirmation Rule Research**: Roberto Saltini, Lead Researcher in Formal Verification of Distributed Systems at ConsenSys, presented research on a confirmation rule for Ethereum that can be used to determine if a block will be part of the canonical chain before the block becomes finalized. The rule relies on a set of assumptions about the network such as the absence of any validator controlling more than 1/3 of ETH staked. Based on the research findings, Saltini has submitted a pull request on GitHub to introduce a confirmation rule that Ethereum nodes can rely on to confirm blocks. He asked for feedback from developers on the rule’s implementation and pointed to the full research paper where developers can get more details about the rule’s motivation and set of assumptions.
133.2  | **Electra**: Andrew Coathup, the editor of a weekly Ethereum newsletter called Week In Ethereum News, asked on the meeting agenda if the “Considered For Inclusion” (CFI) for EIP 7547, Inclusion Lists, should be removed given that the EIP will not be included in the Electra upgrade. Stokes was under the impression that the CFI status is not generally removed from EIPs once it is granted by developers. EF Protocol Support Lead Tim Beiko said that in his view the CFI status is removed from all EIPs that do not end up making it into an upgrade once the scope of the upgrade is finalized. Regardless of the meaning or utility of the CFI label, what’s clear is that EIP 7547 will not be included in Electra. Developers may re-discuss the EIP later for a different upgrade.
133.3  | **Electra**: developers discussed preparations for Pectra Devnet 0, the first developer-focused, multi-client test network implementing client software that supports Prague and Electra EIPs. EF researchers have released a new version of Electra specifications that contains bug fixes from the prior one and new test vectors. EF Researcher Hsiao-Wei Wang said that she has received reports of issues in the latest release and said that a hotfix for the specifications will be ready early next week. In the meantime, she encouraged developers to reach out if they encounter any new bugs.
133.4  | **Electra**: Pectra Devnet 0 in roughly two weeks. It was clear from the discussion that CL client teams would not be ready for a launch the following week, but possibly the week after, starting May 13. EF Developer Operations Engineer Barnabas Busa shared a link to the client tracker document for keeping tabs on the readiness of client teams for Devnet 0. On the call, representatives of various client teams shared more detailed updates on their progress.
133.5  | **Lighthouse**: nstead of working on the implementation of Electra EIPs one by one, the team is working on implementing all Electra EIPs in tandem according to the area of the client code base these EIPs impact. For example, working on all changes impacting state, then blocks, then networking, and so on. Thus, while the client tracker document may not reflect much progress on each individual EIP, “Sean” from the Lighthouse team assured developers that progress was being made. He noted that most of the time’s focus and energy has been on EIP 7549, Move committee index outside Attestation, which he noted “touches a lot of the code base.
133.6  | **Lodestar**: The team is making progress and working on the implementation of EIP 7549.
133.7  | **Teku**: The implementation of EIP 6110 and EIP 7002 are both complete. MaxEB and EIP 7549 are a work in progress.
133.8  | **Prysm**: The team is taking a similar approach to Lighthouse for implementing Electra EIPs. James He representing the Prysm team noted that EIP 7549 requires a lot of work and has slowed down the team’s progress.
133.9  | **Grandine**: Saulius Grigaitis, representing the Grandine client, said “huge work” still needs to be done for completing the attestation refactoring necessary for EIP 7549.
133.10  | **Nimbus**: The team is taking a similar approach to Lighthouse and Prysm for implementing Electra EIPs. “Dustin” from the Nimbus team expressed concerns about the challenges of implementing EIP 7549.
133.10  | **EIP-7684**: EIP 7684, Return deposits for distinct credentials. The main motivation for this code change is to prevent front-running attacks against smart contract-based staking pools. The EIP document states, “Some staking operations feature two distinct entities, one operating the validating key, and one funding the deposit. The funding entity delegates control of the stake operation but must retain ultimate control of funds. If the funding entity naively submits a single deposit with the full stake amount and the other entity's validating key, it is subject to a front-run attack.” While there are workarounds to prevent such attacks, the mitigation techniques are difficult to deploy exclusively through smart contracts and as Shapovalov notes often expensive and inefficient. To offer a more effective solution, the EIP suggests the creation of “a distinct execution withdrawal credential” that can automatically withdraw deposits for validator records.
133.11  | **PeerDAS**: Developers have been making progress on enabling data availability sampling (DAS) on Ethereum. The initiative to greatly enhance Ethereum’s capacity to support blob transactions is called PeerDAS. Stokes said that an initial alpha release for the specifications of PeerDAS has been created. “It's really exciting to see the progress there,” said Stokes. Representatives from the Lighthouse, Prysm, and Teku team all shared updates on their progress with the alpha release specifications. Developers also discussed a few open questions about the specs, specifically assumptions about data synchrony. For initial testnets, developers agreed to use the strategy that works the best for them and come to a consensus about the standard for data synchrony later.

# Intro
**Tim**
Okay. Zoom should be live on my stream. Let's see if it shows up on YouTube 

**Stokes**
* Okay. Okay, I think I see it. I know, I see it, so thank you. Tim,  Okay. Yeah, I tried Barnabas. okay. Sorry again for the technical difficulties. here's the agenda. We'll go ahead and get started. We're a few minutes behind. I'm apparently really bad at operating obs, so apologies. let's see here. This is consensus layer. Call 133. And, yeah, the agenda is, not too packed today. 
* So we'll kind of see how things play out. And yeah, I think we'll just go ahead and hop in. So first up, Roberto had an update on confirmation roll research. He's been doing. Roberto, I think you wanted to, share some content. 

# Update on confirmation rule research [3:21](https://youtu.be/LazOhUu1Tew?t=201)
**Roberto**
* Great. Yeah. Thank you. Yeah, yeah. So this is a work done by myself, Aditya, Francesco, Luca and Kenny. we've been working on this for a while. just give something I think Aditya presented some time ago, but given that there's been some time I saw sort of giving a brief overview of what the confirmation rule is, and it's, it's an algorithm that allows determining whether a block will always be part of the canonical chain. even though it's of course, if a block is finalized, we know that. 
* But this, the idea is to be able to apply this to blocks that are not finalized yet. And you know, another way it can determine that, a block will never be rolled out under some assumption that we'll see later. 
* So there are two properties. one is safety, which is basically what I just said. Essentially, when the confirmation rule says that a block is confirmed, then it means that will this block will always be part of the canonical chain of any honest validator. 
* But there is also another property that is, one that we kind of have been busy working on that it's actually not that easy to get this monotonicity meaning that, that if a validator sees that a block is confirmed now, it will keep seeing that block as confirmed. 
* So that's a thing so different. You know, it could be that you see a block that is confirmed and it will be safe. 
* But then in let's say in in a few minutes you check it again and the algorithm says that it is actually not confirmed even though it's actually safe. 
* So and kind of the two properties they like, fight with each other in a way, you know, trying to achieve both is been a bit of a challenge. But that's one of the thing, we've been working on. 
* So just very quickly now it works. it's kind of it's a bit more complicated than this, but overall, the kind of the the algorithm looks at two aspects of Gaspar LMD and FFG. For LMD, we look at the ratio between the weight for a block and the maximal weight, and this must be larger than what you see on the right hand side of whatever is written there. Half of this one, plus the weight of the proposal is divided by maximum weight plus beta this must be must be verified for all the blocks, in a chain. 
* Until if you want the finalized one. And then for the FFG component, we check, you know, again, high level, we check the we check the essentially the FFG that is supporting, the check point of a block minus what beta is again, the, the maximadversary weight, minus basically what can be slashed plus, one minus beta, which is the weight of the honest multiplied by, the ratio of the honest multiplied by the weight of the remaining slots 
* This must be larger than two thirds of the total weight of the paper. And this, in the paper, we show this this last two together with other conditions to ensure that, this block will never be filtered out by the, for choice filtering rule. And so the two things together that we allow to determine the this block is safe. 
* So I spoke before there are some assumptions made in terms of safety. I think that pretty, expected properties. we need to assume the network is good synchronous is, you know, we have finality for when we assume the network is not synchronous. Also, we assume that given us any sequence of slots, we know that no more than a bit of the state controlled by these committees is Byzantine. 
* This is pretty standard. It's pretty I say sort of probabilistic property. we assume, again, weight is less than one third. And also we assume the Byzantine validators cannot delay for more than one epoch, the inclusion of attestations that justify a checkpoint from the previous epoch. So basically, if by the end of the current epoch in alpha attestations have been sent to justify, the checkpoint from the current epoch by the end of the next epoch, these attestations will be included in a block in 1 in 1 chain. 
* So in a way, you can think of this like there will be at least one honest proposal through. There are limitations on the block size but, you know, another way is also to potentially think of a change where you allow to include more attestations. If those, end up justifying a block, then in terms of to actually to achieve monotonicity, we need stronger assumptions. beta must be less than one sixth. 
* And also in in a way we assume that there is a new checkpoint. That is, there is always new checkpoint that is justified in future epochs. the actual assumption is more complicated this. 
* But you can think it, in this way Lastly, another point that another point that we've been working on that wasn't present in the first, first work, was it's been dealing with entry exit rewards and penalties. So section five of the paper, so we the paper, we present, the algorithms in increase order of complexity. 
* We start with just considering LMD ghost. Then we move to considering FFG. And then we also consider initially considering only basically no changes to the validator set except for slashing. 
* And then in the last section we we show an algorithm that can actually deal with entry exit rewards and penalties. Actually the algorithm, the structure of the algorithm is exactly the same as the one that, doesn't deal with this problem. 
* The only thing that changes are the thresholds that I showed you before. So those thresholds, in the more extended algorithm, they also have components that take into account the reward ratio, penalty ratio and churn ratio. currently there is a spec. The code spec PR of the confirmation rule has been updated as well, with the to reflect the algorithm that we have in the paper. 
* The algorithm there is the one that does not assume entering exit rewards and penalties just because, there wasn't enough time. And again, as I said, it's just the only difference here. So factors that must be multiplied in the former. But the overall structure is the same. So in our opinion that spec PR is ready for review and for comments. this is all from me. 

**Stokes**
* Great, thanks. do you mind dropping a link to the slides or if there somewhere, people could follow up with your work? That'd be really nice. Anyone have any questions? 
* Okay. Also a PR in the specs repo. Great. Yeah. Thanks. Roberto. 
* Roberto. Thank you. Okay. I wanted to keep it up first. just go ahead and, work around the time zones with Roberto. So next up, we'll move to Electra. again, there was a quick question about, EIP 7547. This is the inclusion list EIP. Andrew was asking essentially, if you know, the EIP won't go in to Electra, should we change the CFE status? 
* I think that was I don't know if Andrew's on the call, but either way, that was basically the question. generally I think we if we CFI something it's there's no like formal bearing on inclusion in 
* The sense and so we don't really on CFE things. I don't know if anyone feels differently. 

**Tim**
* I guess yeah. Usually what we do is we just un cfe it when we have a final scope for the fork and we just remove everything that's been CFE and just keep the stuff that's included. 
* If it's simpler, if, like, we really agree now that we're not going to do this, we can all we can remove it from the list now. but yeah, no strong opinion. I think it'll get removed to delay for the time being. 

**Stokes**
* Yeah. I mean, in some sense, CFE is almost like a moral status. You could imagine if something's been certified, it's always CFE. 

**Tim**
* Yeah, at least for this fork. Right. and then you can discuss for the next one. So. Yeah. Yeah, I guess I can change 

**Stokes**
* Okay. next up, wanted to get into devnet zero and everything there. So the first thing to call out, there was a spec release, the 150 alpha one. I think this is mainly bug fixes for the pectore specs. also PR dos test vectors. 
* So thank you everyone who got that together in particular. Xiaowei. I can go grab a link to them in a second. Just so everyone has that. 
* Otherwise, yeah, I think, are there any questions or things to call out? on the spec there? I think it was pretty straightforward. Just fixing some bugs from the Alpha Zero release. Yeah. Shall we? 

**Speaker E**
* Yeah. So we have received, at least two issues of the test vectors in the latest, spec, test vector release. So I think I can I will share the link to the chat later. if any clients have have tested and, just let me know if you encounter some issues. And I expected that we will have another hotfix of the test vector early next week. Yep. 

**Stokes**
* Great. Thank you. Okay. next up, I did want to talk about, just general progress and where everyone is. let's see, Barnabas dropped this, progress tracker in the chat. I'll go ahead and take a look here. yeah. EIP client teams want to give an update? How are we feeling about Devnet zero implementation progress? 

**Sean**
* So for lighthouse, I'd say we're making progress. We're mostly focused on the changes related to, moving the attestation index because we're talking about that in discord a bit, but it does end up being it touches like a lot of the code base. So that's the majority of our focus right now. we're actually like staging our implementation differently than per EIP. We're 
* Sort of like implementing all the EIP for different components of the code base as we go. So it doesn't quite map to the progress tracker, but, solid progress. And we're grinding, I would say. Great. Sounds good. Anyone else 

**Gajinder**
* Yeah. We are. We have also made, decent progress and, we, for 7549 we are working on few things, but mostly, things seem done. As of now. We are making few changes regarding, with, creating the partial withdrawal request in the new format. but, yeah, we should be ready pretty soon. And for Ethereum JS, I just want to add JS yes. On that. On that end as well, we are doing good for 76. we have incorporated 7685. And so our sort of integrated into individual EIPs. Yeah. Thanks. 

**Stokes**
* Great. Enrico. 

**Speaker G**
* So back to back to tackle. we are complete on 6110 and 7002. And we are close to be ready for, for the max EB, EIP and work in progress for the attestation one. This is 7549. we yeah, we what is missing there mostly is the aggregation logic, but for now, I guess we should be able to follow, a chain where in theory. So. Yeah, still work in progress there. And finalizing Max EB. The TLDR is that. 

**James He**
* Giving an update for Prism, all of the EIPs are being worked on, but we're taking a similar approach to lighthouse, where, we're sort of handling cross components. We're doing like, all the block changes, all the state changes, sort of separately. And, the 7549, slowed us down a little bit, because of, how many things it touches. but we're making progress 

**Saulius**
* So for, the, the progress on all the, APIs except that, there is really huge work. Still need to be done on, on attestations, refactoring. So, I did raise this question on telegram, but it feels from, from the update, from the other teams, it feels that, other teams are progressing, quite good. And it doesn't feel that the teams will not be ableto do this huge refactoring. So correct me if, if I understood that correctly. 

**Stokes**
* Yeah, it sounds pretty good so far. I think, Dustin, you're going to give an enormous update 

**Dustin**
* Yeah. So I would say in. General, I'm going to echo in terms of, say what white House was saying about like, kind of not implementing I'm going, you know, EIP by EIP, but rather say sort of set of test vectors by a set of test vectors or a set of sort of subportion of code base or code base by portion of portion of code base. that being said, viewing it by EIPs, I think I would say is, far as I can tell, we're okay on 6110. for from this is the CL side obviously. 6110, 7002 and 7251 I believe those should all be, I mean, at least okay, enough for  devnet zero.
* As usual, as and this is, I would agree that this is, 7549 is a challenge. and it's, I don't know it or it's underway. and I will I guess my approach here is to try to, to make sure that there's something it can minimally the kind of following the chain is my, I mean, criteria here. So there may or may not be able for, for some for 7549 related stuff. I'll just say this. For example, Nimbus has no intention of posting attestation slashings like, it's not it's fixable. It's not worth fixing in time. that's one of the things affected, one of the little bits of fallout from 7549. We need another. 

**Stokes**
* You just mean for devnet zero, right? 

**Dustin**
* Yeah, eventually. But I'm saying like it's not it won't break consensus and other clients can use that. But you know we've had to use one. But, we're attempting to get this working. We have it looks maybe okay, but for a very, limited view of, okay, honestly, like this. This is. Yeah. I don't know it. Hopefully it will work well enough. 

**Stokes**
* Great 

**Dustin**
* Well, Nimbus does a lot of type level stuff in its construction, and it's. Yeah. So, yeah, the rest are there. Yeah. 

**Stokes**
* Cool. Yeah. I'll take one off. great. I think that was every CL team. And yeah, it sounds like things are progressing well enough. ideally we should be looking at devnet zero, say, in ten days. So I know again it's like a very tight timeline, but, sounds like everyone is moving towards that. 
* So I think we keep things as is there was this question brought up of maybe changing dev net zero scope. it 
* Sounds like again, this attestation refactor is like pretty involved for everyone, but also it sounds like at least 1 or 2 teams are pretty confident that that part will be fine. 
* So yeah, I guess this is now your chance. if we want to have this conversation, we can we can talk about this. But I think generally we should keep things as is for the time being. Does anyone feel incredibly strongly otherwise? 

**Speaker G**
* Going back, for taiga will be a super pain, and I would. I would think that we will stick, we would stick it into the attestation no matter what So if the thing is to participating or not participating in net zero, I would say if we go back, I don't know if that will be able to participate at this point. 

**Stokes**
* Right. And the thing is we do just need one CL and one EL to start a Devnet. So if it takes a day or two after, say, this ten day deadline for others to join, we can still make progress on the actual initial devnet as other people around other implementations. 
* So I know it's a very tight timeline. And yeah, it's I'm sure very stressful for everyone, but it sounds like we can make it. So I would lean towards, keeping everything as is for now. 

**Dustin**
* So I guess one. I'm a little less concerned with whether it's in Devnet zero. And, I think that's sure. But the question of, I guess my concern is that this seems to have potentially snuck in a little bit as a let me say, it was framed and during the ACD call as a more, minor change that ended up being and part of this, I think, is in terms of the logic of the change, there wasn't a huge amount, in some way a some level, it's unquote just moving a field around.
* It was not pages of you know, if then statements. but and so I guess I have some kind of process concern there of, of sort of I think that there was a process failure in a way. 

**Sean**
* Yeah, I kind of get that. It definitely looks a lot simpler specked out than like actually an implementation. And it seems like, I don't know, like how do re adjust our, I guess, fork scoping 

**Sean**
* After we start the implementation if we want to in the future? 

**Dustin**
* Yeah, exactly. I think I think that's a good way of putting it. And to say that I think every one of these, these EIP which was considered, which has been considered people have looked at in their various ways, kind of the what phrase it in various ways ROI the risk return benefit cost benefit some kind of relatively speaking, a ratio is it worth implementing this EIP? And this one was framed as kind of well, why not? Isn't it kind of nice? 

**Speaker G**
* And maybe but and to add to that, I think there's, I think there's some. Sorry, I was just adding to your comment about saying that the initial framing of that was also that it will be some very nice benefits in term of networking, and that has been a little bit of misconception initially. And then this turn out that it's just block space that benefits for it in the current form And and you're right that we probably underestimated the impact in the, you know, code basis because touching the attestation that is simply the same for since phase zero, has been underestimated.
* How painful would have been to change the the format even just adding a a field. Yeah. 

**Stokes**
* Yeah. I mean I think that makes sense what everyone's saying you know takeaways I think in the future when we touch types we should just be very mindful of this. Again, it seems like I mean there are benefits. It's not that it's useless IP. And if anything, I think it does lay the groundwork for future changes around networking that would unlock even more benefits. So I think the EIP stays in. yeah, definitely.
* Here. Everyone that this is a big change, you know, implementation wise, but it sounds like we'll make it work. Yeah. Dapplion. 

**Dapplion**
* Just  to remind a bit, I think what what happened here is the, the original EIP had a slightly different implementation. it only set the index  to zero. So, by not having the type change, the fix was supposed to be smaller, but then Mikhail proposed some really nice benefits that we should do, and that I think this mutation through the process is, I think what what we missed. And as you recognize, that's what increased the scope in terms of implementation. so yeah, for next time, if an EIP mutates, we should be mindful of, the consequences, even if it's already considered for inclusion 

**Stokes**
* Right. And just to like, you know, I guess state the obvious. Like this is the process, right? Like we have the EIPs, you know, if they sound good enough to everyone, then we, you know, include them in some sense. And it is the point of like then downstream implementation of that to like sort of raise these issues. I think everyone's just feeling a little extra pain because of pretty tight timelines. 
* So yeah, I hear everyone and yeah, these are all things we should be keeping in mind moving forward. And yeah, that being said, I do think that we'll make it happen, so I'm feeling pretty good about it 

**Sean**
* Something we're trying to move more towards in lighthouse is more flexibility with like, individual EIP implementations. So the like ability to enable disable single features. And that would let us like more easily pull things out of forks, move them to separate forks. 
* If we could like similarly move towards something like that at the spec level two, that would be even better, because then it'd be easier to get like vectors that are testing like individual features and then different combinations of features and yeah, it might help in scenario like this. 

**Stokes**
* Yeah. And generally we have this like features notion in the consensus specs that gives you that. I think again, maybe just due to the timelines, it's like we didn't necessarily have these test vectors, these independent ones per EIP, just ready to go. Terence asked a question. Let me go look at this link. right. Yeah. So Terence was asking about an addition to 7549 this was making essentially the representation a little more flexible on chain. And. Yeah, that is out of scope for Devenet Zero.
* And yeah, the idea would probably be to include it in later devnets.
* But again, we are focusing on just dev net zero for now. And then we'll handle that down the road. Okay. Well thanks everyone for your comments. I think that was some good reflection. And yeah, definitely things we should all keep in mind moving forward 
* is there anything else otherwise we can move on to, another presentation on a new EIP. 

**Gajinder**
* Could we maybe get a timeline on, like, when is the first CL would be ready? Because we initially tried to do it like last week, and now we push it time to like the 6th of May. 

**Barnabas**
* But is any CL team actually can see if they would be ready by next week Monday? 

**Sean**
* We wouldn't be ready by Monday.  Now, I thinkten ish days we're targeting. 

**Speaker G**
* We might be have something for Monday, but, maybe probably high probability with being broken. So we were thinking more about targeting mid next week to have something more stable. But I even see the benefit if we have something kind of working to spin up some definites by Monday or Tuesday and see where they break 

**Gajinder**
* Yeah, we'd be doing this stuff locally, so the cost of stuff failing is extremely low. 

**Barnabas**
* Yeah, I think that devnet zero could possibly wait, to Kenya and then we would just do all local testing all next week. Still 

**Stokes**
* Okay, great. Sounds like everyone will be very busy. Good luck with, the rest of the implementation. so next up, I think this is, Vasiliy wanted to give a short presentation over EIP 7684. would you like to do that? 

**Vasiliy**
* Yeah Hey, I'm going to post two links into the call, chat. So bear with me for now. Yeah. so there is an EP 7684 by Dublin. the gist is, at this moment, when there is a deposit coming for a validator, on Beacon Chain to the that already exists. Uh then it doesn't matter what withdrawal credentials are in the deposit that is coming. What only matters what are withdrawal credentials are for the validator that already exists.
* So imagine there is, for example, a malicious, not operator, who is accepting a delegated stake They, provide deposit data to the client, client posts, a deposit transaction, and, the malicious validator front runs this transaction with their own deposit, with their own withdrawal credentials. And, the staker who wanted to just delegate, their error will be gifting them to the malicious node. Operator. this is, so-called deposit front runner vulnerability.
* It's a pretty subtle one, like it was pointed out out that I think, like half a year before the Beacon Chain launched, but, it was actually found in the code of rocket pool and lido back in the day. And, both protocols had to both protocol teams had to like, fix it asap. just before the launch of Rocket Pool, as far as I remember, this is mostly mitigated and largest protocols and probably mitigated, in the largest custodial services like exchanges and custodies. though the second one is like, just probably true. there is no way of checking, but this mitigations are pretty cumbersome or capital inefficient.
* Like there are basically two. One is just in time. Checking the deposit like Lido does with the, special committed to check it. this is, worse in the trust model. And the costs, development costs operation, and, like, increased brittleness. there is an option of only allocating stake to the validator that up redeposited. But this limits, like this makes, model capital inefficient, because if there is not enough stake coming, then this pre-post validators are just sitting there, like, doing nothing.
* And this makes the process of stake delegation, like two step process, which is, like makes it more cumbersome and worse user experience. Most of the stake in existence actually just wing it.
* They don't, like clients. The Stakers don't check that the validator is not on chain. They're not operator does not provide a mitigation. that that is entirely like a trust issue. I don't think it has been, exploited in, like, in actual, life there is I think like 5 or 6 deposit deposits that override withdraw credentials, but they mostly look like honest mistakes, like, 080 withdraw credentials, something like that. but there is like 7684 proposals are pretty simple. fix here. now, when withdrawals are, possible, when a deposit comes with a withdrawal credential that is different from the validator that is actually registered on Beacon Chain.
* These,other can immediately be withdrawn to the back to the, execution layer, maybe with like some fee to prevent spam or something like that.
* I think, like, I'm not sure, like, I'm pretty sure that it's pretty late to get anything to Petra at this point, but I'm pretty sure this would be a good change for, Ethereum staking mechanism. 

**Stokes**
* Got it. Thanks. I've had time to look at the CIP in depth. I hear you on the concern. Does anyone else have any thoughts or comments at the moment? Otherwise, we might need a few minutes to digest. I guess one question is, you know, if we wanted to move ahead with this EIP, would you be pushing for Electra, the EF star fork, or you're more just wanting to raise awareness today? 

**Vasiliy**
* I like, my intuition. That is like a super small, proposal that is, like, entirely can fit, like, in, in, I don't know, but, like, not much work. but I'm not a client developer, and, that's like, what I wanted to understand what the feeling people have, like, is it something that is so small that can fit into spectra last minute or, if it's even desirable to write, what's the public sentiment on this? Or. That is like, just something that, I'm presenting for now to raise awareness. 

**Dapplion**
Yeah. So regarding complexity, so unless someone finds a clever, more clever way to do it than than what I found, there is an interesting quirk about, withdrawals. And after EIP 6117, there is a recursive dependency on building blocks. The execution layer needs to be supplied from the consensus layer. What are the withdrawals that have to be, processed? And then the the block of the consensus cannot be dependent on these withdrawals. Otherwise we have a recursive dependency. 
So the solution of this EIP is to evict immediately any withdrawal that attempts to to have a different withdrawal credentials. 
But because of this recursive dependency we cannot immediately withdraw a deposit. what that means is that we have to accumulate the withdrawals in the state and then process them afterwards. And after EIP 6110, the amount of deposits is not bounded anymore. And I think the maximum number at current gas, parameters is about 1200, which means that either we would have we can have an unbounded queue of pending withdrawal deposits on the state, or we have to remove the cap of withdrawals if we want to evict all these, undesirable withdrawals at deposit. Sorry, within the next block. 
So that's something that we have to talk with the execution teams to see how much of an issue it is to have, unbounded withdrawals or up to, 1300. 
So it's it's not terribly complex, but definitely I don't I would not consider something trivial. And. Yeah, I think it's good that, that we look at this solution and see if we can find something, simpler. But I'm not sure if this is. This fits for Pectra. 

**Stokes**
* Right. Yeah. Thanks. I mean, I think we probably need a couple of months just to digest, consider different solutions, and then get to, like, sort of a final EIP. So So, you know, that process will need to play out. And then ultimately, you know, I guess this is the place to come back once that's done. And then we can we can see where things have stacked up. 

**Dapplion**
* Yeah. And as a final comment, I think to to motivate the solution this does not this affects every single, LST or feature list protocol and especially for those that want to be maximally trustless. definitely all the solutions involve some sort of, heavy trade off or centralized actor. So it's definitely an equalizing force. agnostic to any specific, lst. 

**Vasiliy**
* Yeah. In general, like this is the tax on development instead of like a straight blocker, for implementing like, trustless things. But it's a pretty significant tax, actually. A lot of efforts going into, like mitigating this. 

**Stokes**
* Okay. Good to know. So, yeah. Everyone just, please take a look when you have some time, and. Yeah, we'll keep it on our radar. Okay. next, I wanted to leave some time for PeerDAS.

# PeerDAS [44:42](https://youtu.be/LazOhUu1Tew?t=2682)
**Stokes**
* I don't know if anyone has any update there. I know the client teams have been pretty busy with Pectra. there has been some work on the spec lately. like I said, there are some test vectors even released in this alpha one consistent specs release, so it's really exciting to see the progress there. I don't know if anyone else has anything they want to discuss right now with respect to PeerDAS, either an implementation update or spec update spec questions, anything like that. 

**Gajinder**
* I've been working on this for the last two weeks and, basically we'll try a local loadstar,  to loadstar, on custody, testnet. And, if that works, then we'll try to integrate, with any other peer that is out there. 

**Stokes**
* Great. Good to hear. Yeah, yeah. 

**Dapplion**
* Lighthouse. I think as of yesterday, we can we have completed sampling, a sampling, lighthouse only testnet so we can. So as of now, we can produce blocks with, garbage extended data. We are not actually using, CKG library yet. I think, we can custody. We can serve custody, and we can do sampling, something some specifics of what we are going for.
* We are going for trailing Da at the moment, we are not using yet the new, network charts formula, but we plan to do that, this week. And we implemented, a feature that was suggested by the Codex team, I think, where we allow so as a cost to the serving, we allow people to request the samples before we have them, and then we put that request on hold And we will resolve this request once we get the cost of the samples from gossip.
*  So it will be cool to agree on this set of features with everyone. Otherwise we'll have interrupt problems. That's it for me. 

**Nishant**
* So on on prisms and, we've been making good progress on implementation. we are right now in the process of trying to get a prism to prism node, working. So we have integrated all the, CSD methods So it seems to be working for us. we are running into issues with, getting the columns gossiped out, having a block proposed with the extended columns, being received by the other Prism peers. But we are, positive that, uh by interop, we would be able to communicate with other clients, at least as the current spec as it is. 

**Stokes**
* Okay, that's great news. 

**Speaker G**
* You're just an update  I don't have the details, but, there is a branch in work in progress, and we could have something.  yeah, we could hack something. Maybe during the the interop, but not sure. 

**Stokes**
* Sounds good. yeah. In that line, I think I might have Dapplion over this was. Did you have a question around the spec or, like, sort of what what to initially target? 

**Dapplion**
* Yeah. So the I think that the two questions and I'm not sure if the spec is precise on this. So first one is if we're going to do trailing Da or same slot DA, I'm not I don't think we have agreed on either way yet. And then the second one is this, this feature of if someone requests your custody column that you are supposed to have but you don't yet have, instead of returning immediately, resource and available, you hold this request for some time in the expectation that you will get a column. And if you do not after some time out, then the request gets canceled. And that's okay. But if you get the custody with a within this window, then you resolve the request.
*  And what that allows is to have, 00 lag, dissemination mechanism without actually having to do many retries or having gossip amplification. 

**Stokes**
* Right The latest I heard on the first point with regards to the trailing fork choice, I think, lighthouse was thinking that they would not do it. But then the latest I heard is that they would do it. So I'm not sure anyone else has enough implementation to have like a strong view on that right now. 

**Dapplion**
* Yeah, I can summarize. We had a chat internally about this. And I think the what we realize is that if you don't do trailing Da, then the the timing game pressure would be very, very high. because you are, you will be supposed to perform all the sampling within a very short time window between when you receive the block and when you have to attest so those peers that do not have very, very fast internet connections, they will suffer, as builders and proposers will delay the block as much as possible to get enough votes at the expense of the slowest peers on the network. if we do trailing Da, then at least you will have 12 seconds and then there is no much pressure.
*  You only have like the situation would not be worse than today. We just have. You just have to, press the block soon enough. 

**Stokes**
* Right. Yeah. I wonder if there's a middle ground. We've talked before about moving the attestation deadline to say, like eight seconds rather than four, which, with respect to timing games, maybe doesn't change much. 

**Dapplion**
* No, I think that that wouldn't that doesn't fix anything because then you would just publish the blog later, right? Yeah. 

**Stokes**
* Yeah, Potuz

**Potuz**
* So I'm, I can't speak for Pierre Das, but if by training the. It's only this, it's on fork choices. This implementation of filtering the branches where you don't have them and act like that, that would be a very simple change in first choice for prism. So it's easy to implement. 

**Stokes**
* Okay, that's good to hear. it seems like. Yeah, the the consensus seems to be leaning towards trailing Saulius. 

**Saulius**
* Yeah. For, I think for Testnets, maybe it makes sense to not do this trailing port choice just for, just to try and to see, maybe it, you know, maybe they are all the way does. It just doesn't work on a small testnet for some reason. So then we can automatically rule out that, that would be one argument. The other argument that so far, the fork choice was always, always protected from, from these blocks that, are not available. So far the, the current approach is to include, include the block only when is the data available is true So so this trailing four choices. I would say very different approach than we have now. 

**Stokes**
* Right. Yeah. There's another comment from Nishant. we should just increase the custody count and not use trailing. You get stronger guarantees from gossip. So, yeah, it sounds like we're actually kind of undecided on this. You do have a point that maybe just for, like, initial implementations, it's simpler to do non trailing, like synchronous within the same slot. So there there's some benefit there. Although it kind of sounds like we are undecided. 

**Dapplion**
* Yeah I think in practice it doesn't matter. Like we definitely don't want to do that for mainnet eventually. But for an initial interrupt, people can just sample whenever they want and it should be fine because it's it only impacts your local view of the first choice. 

**Nishant**
* For for interop, I don't think we need to actually align so much on how we're going to sample, because it just matters for your local view. So you could have some nodes doing trailing and some nodes not doing it. And technically the network should still function fine. 

**Stokes**
* So then I guess it sounds like do whatever is easiest for your implementation. At least to get started. And I guess we can come to some, stronger consensus on this down the line. 
* Okay. Thanks, everyone for that. anything else anyone would like to bring up? I think otherwise, yeah. We can go ahead and close out the call here in a few minutes. Saulius, your hand is still up. I don't know if that was from the last time. I'll assume it was. Unless you say something. I guess just the conversation now does kind of bring to mind that, we might eventually want to break out for pure DDoS to dig into some of these things, but that can happen after we get the first, net running. 
* Yeah. Okay. Yeah. I mean, that sounds like it for the the day. I do have one final remark. we'll go ahead and cancel the next ACDC many of us will be working at an interop, so it will not make sense to have the call. That means the next ACDC will be May 30th at the usual time. So, I'll post again in the usual channels just to remind everyone, but just, keep that in mind. And I think that's it 
* Thanks, everyone.

__

### Attendees
* Terence
* Tim
* Trent
* Pooja
* Barnabas
* Terence
* Pari
* Ethdreamer
* Mikhail Kalini
* Mike Kim
* Zahary
* Pawan
* Chris Hager
* Gajinder
* Andrew
* Mario
* Shana
* Carlbeek
* Roberto
* Sammy
* Protolambda
* Saulius
* Marek
* James
* Dankrad
* Kevaundray
* Radek
* Fabio

____

### Next meeting
Thursday 2023/8/24 at 14:00 UTC

