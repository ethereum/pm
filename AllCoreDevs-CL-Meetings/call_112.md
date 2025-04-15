# Consensus Layer Call 112

### Meeting Date/Time: Thursday 2023/6/29 at 14:00 UTC
### Meeting Duration: 1 hour
### [GitHub Agenda](https://github.com/ethereum/pm/issues/821) 
### [Audio/Video of the meeting](https://youtu.be/zdqtl9x_UjA) 
### Moderator: Danny
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
112.1  | **Deneb**: As raised on ACDE #164, Kalinin has proposed a deprecation schedule for the “engine_exchangeTransitionConfiguration” method, which was a method used for transitioning Ethereum nodes through the Merge upgrade. All EL clients have already ceased to log error messages for this method and to remove it completely from EL clients, Kalinin asked CL client teams to either stop calling this method or remove it entirely from their code base. Doing so by the Cancun/Deneb upgrade would ensure a smooth deprecation schedule and a clear deadline after which EL client teams can then start to remove the method safely from their codebases. There was no opposition to Kalinin’s proposal. Kalinin agreed to check-in with the progress of CL client teams on this matter when developers start coordinating the launch of public Deneb test networks.
112.2  | **Deneb**: Engine API proposed by Kalinin for inclusion in Deneb is the builder override flag. It is a new Boolean field that the EL can use to indicate to the CL node that it should consider falling back on local block production instead of relying on a third-party builder. According to Prysm (CL) developer Terence Tsao, this field is meant to give validators “more control” over block production and in the event of censoring activity by third-party block builders, give validators an easy way to pick up and react to this activity. The field was originally proposed for inclusion in the Shanghai upgrade. However, developers agreed to continue prototyping the flag and allow CL client teams to implement it asynchronously without a hard fork. On ACDC #112, Kalinin proposed using the upcoming Deneb hard fork as a rallying point for requiring all CL client teams to implement this field. Danny Ryan was supportive of the idea. Ryan asked whether the idea to make the builder override flag a breaking change in the Engine API for Deneb had been raised with EL client teams. Kalinin agreed to circulate the proposal and get the conversation going with the relevant EL developers.
112.3  | **Deneb**: Discussed testing efforts around EIP 4844, proto-danksharding, which is the main code change being implemented in the next Ethereum hard fork. For more information about proto-danksharding, read this Galaxy Research report. Parithosh Jayanthi from the DevOps team at the Ethereum Foundation said that all EL and CL client teams were passing the relevant Hive tests for Devnet #7. Therefore, Jayanthi said that his team plans on launching Devnet #7 as early as Friday, June 30 or Monday, July 3. As background, Devnet #7 is a dedicated short-lived test network for EIP 4844. It will not test other code changes, that is EIPs, that have been approved for the Cancun/Deneb upgrade. Additionally, Devnet #7 is launching with a target blob limit of 3 instead of 2, and a maximum blob limit of 6 instead of 4. The increase in blob capacity was proposed by Ethereum Foundation Research Dankrad Feist after he conducted a data experiment testing network capacity for processing large blocks.
112.4  | **Holesky Testnet Update**: Developers are preparing to deprecate the public Goerli test network by the end of this year. To replace Goerli, Ethereum client teams are working on spinning up a new testnet known as Holesky that will host an active validator set size larger than Goerli and Ethereum mainnet. During Holesky Coordination Call #1, representatives from Ethereum client teams committed to collectively spinning up roughly 800,000 validators. Other Ethereum stakeholders likely blockchain infrastructure companies and teams will be standing up roughly 900,000 validators. In total, Parithosh Jayanthi said that he has received enough commitments for the validator set size on Holesky to be 1.7mn. Each participating institution will receive roughly 100mn Holesky testnet ETH at network genesis. The goal is to complete testing to ensure that CL client software can handle the large active validator set size by the end of July and launch Holesky in September.
112.5  | **Research Discussion - Making EL triggered partial withdrawals a prerequisite for increasing the maximum effective balances of validators:** This would ensure that independent validators that want to withdraw some portions of their accrued ETH rewards do not have to fully exit their validator and opt out of auto-compounding their rewards.
112.6  | **Research Discussion - Bundling this proposal with EIP 7002 which has already been proposed by Danny Ryan to enable EL triggered validator exits:** This would be to create synergies and parallel workflows with other ongoing EIP initiatives.
112.7  | **Research Discussion - Changing slashing penalties for validators chosen to propose blocks based on their balance of 32 ETH, not their increasing effective balance:** The change would be to help de-risk validator consolidation, especially for large staking institutions, after the increase to validator effective balances is implemented.
112.8  | **Research Discussion - Removing the partial withdrawals sweep all together:** There is an automatic and recurring sweep of validator reward balances. Removing this sweep and making auto-compounding the default behavior for accrued staking rewards may make the implementation of this proposal much simpler.
112.9  | **Changing the minimum balance before validator ejection:** Validators are automatically ejected from the network if their effective balance drops to 16 ETH. Given that an increasing effective balance beyond 32 ETH might mean that some validators have an extremely long runway before being automatically ejected from the network, there is discussion around changing the minimum ejection balance to a more dynamic number based on a validator’s highest effective balance. The change is meant to address the issue of validator node operators losing their validator keys and being forced to wait for the inactivity penalty leak to automatically eject their validator from the network.

**Danny**
* Great. We should be live. Welcome to ACDC the consensus layer call # 112. This is issue 821 in the PM repo. If you're following along, that's the agenda. So, a few Deneb items, a couple things from Mikhail about the engine API. and then we had planned to talk about 36 as the blob target max. we, hopefully those, some of y'all looked into the data, but we've also had some testnet hiccups, so, we'll see as to where we are on that conversation. Let's start it off with you Mikhail, the deprecation. 

**Mikhail**
* Yep. yeah, so from the latest call we've learned that, drop the talking to chat. We've learned that basically, execution layer a clients did not log any error anymore if exchange transition configuration is not being called by the CL. 
* So that's, that's great. and yeah, the next step would be, if we take this path, the next step would be for CL clients to stop calling this method or remove it entirely from the code base. and, a requirement, for, according to this procedure requirement would be to, make this change into, Cancun at most.
* So after Cancun, everyone upgrades their node and then, and then EL clients can remove this matter entirely from their code base as well. So, that's basically it about, the deprecation for the, for CL side. Does anyone want to rise any opposition to doing this? 

**Danny**
* So it was, you can remove the call or remove the code entirely now, and you should certainly do so by the fork. 

**Mikhail**
* Yeah, that's the perfect recap In the opposition. 

**Danny**
* And what happens if the client teams do not do so by the fork? That means they'll call a method that, or attempt to call a method that does not exist on the execution layer. Yeah. And would probably see errors. 

**Mikhail**
* Yeah, yeah, exactly that. 

**Danny**
* So, Okay. 

**Mikhail**
* We actually will not be able to safely, say that yeah, EL developers can remove this methods method from, from the code base. I don't think it's a like, super big problem, but still, I guess we want to keep code base as clean, as clean as possible. 

**Danny**
* So I, And this is in the Cancun engine API spec? 

**Mikhail**
* Yeah, it is. It is there basically. So I take silence as no opposition to that. So it would be great if, clients would be, would keep this, documents posted so we can track the progress and be sure that it is done before Cancun there is the table for CL clients in It. 

**Danny**
* Sounds good. I'd say when we are discussing testnet dates that maybe you just kind of do a quick pass on this, on a call once more to make sure everyone's in line. 

**Mikhail**
* Yeah, Cool. Good idea. 

# Scope shouldOverrideBuilder flag for Cancun execution-apis#425 [9.40](https://youtu.be/zdqtl9x_UjA?t=580)
**Danny**
* Great. And the next item is also an engine API item from Mackay. 

**Mikhail**
* Yeah, so it is a tiny change to the engine api, but it's not a tiny conversation as time is the change looks like. So basically, this is about overriding builder, builder block by using, by falling back to local, execution payload, if EL, if local EL  clients suggest that some censorship is happening in the network. 
* And we we had this question before, in one of our conversations after Shanghai and we decided to get back to this, in the context of Cancun. So now is the time to get back to this conversation. and yeah, I think that the change to engine API is really tiny and doesn't look too complicated. But, yeah. I would like to ask Potos since he's on the call to give more context about this and refresh, the background on that. 

**Terence**
* Yeah, I can add more color, right. So the high level idea is just to give your local validator more, find the control today, local validator, look at payload value, decide between the higher value between local, between the local payload versus the builder payloads. 
* But this enables more control such that like we can see whether the censorship, for example, whether the transactions have been included for several slots with higher priority fee or some certainty as keep getting reorged. And I think it's worth mentioning the idea of optionality here is nice because different EL to have different heuristic, it's kind of like herd immunity and this is a feature not a bug and this is also an optional endpoint as well. 
* So yeah, I think we discussed at the end of case Capella, due, and due to timeline we didn't make it in and I think this is a good inclusion for Cancun. 

**Danny**
* Yeah, I mean it seems on the very minimal side of complexity because you can essentially do nothing, on both sides other than just have this field. I'm pretty supportive. 

**Ahmad Bitar**
* I'm sorry, my understanding was that it was a soft fork or does not need to be hard. Like is this field required to be sent? 

**Mikhail**
* According to this spec, yes, it is required to be sent, but the client can just send through if it, sorry, false if it's not support, if it's not supporting any heuristics or do not want to support it And the CL can do a no ops  or can for some amount of time not do anything in relation to the value, but the value needs to be there. 

**Protolambda**
* It Might just ignore it. So it might depend on zero change for us. 

**Ahmad Bitar**
* Why did we not opt for an optional value where someone can add it to the execution engine whenever they want? 

**Mikhail**
* Probably can't think about it, but currently we don't have optional values in the spec. 

**Danny**
* There's also a hard fork coming up, which is a great time to transition and not deal with the complexity of if values exist 

**Speaker: 6**
* On the, on the CL side.  We already do some all back based on other conditions. So I think to support on the yield side, that flag should be quite easy. And as said on the, on the EL side, it just pass false by default and the protocol doesn't turn, doesn't need any option value. 

**Danny**
* Is there EL signal other than Geth? I see, Marius has an implementation. 

**Ahmad Bitar**
* Is there a specific consensus on the heuristic that's gonna be used to determine the value? 

**Protolambda**
* I think it's better not to have consensus. I think it's better to have client diversity here and I think it's better to have, diverse options of to where that each validator can decide on what kind of sensors is censorship or not. 
* I can give some several algorithms that I think are reasonable, but I suspect it's better to have each client team to come up with their own design decisions. 

**Sean**
* Is there a reason for this to be a field in get payload as opposed to like, having a new endpoint that has this sort of more general information? Cause this is sort of like some like transaction pool information to some degree. 

**Protolambda**
* Yeah, so here I think there is, there is an actual reason. So this opens the door, albeit minimally to break in the boundaries between the EL and the CL. 
* So we really wanted to keep it at the absolute minimum and being trivially implementable, like having a different endpoint, this would, definitely, raise more concerns from EL, and it would in increase complexity in like in using this endpoint or not. 
* And I think just, the fact that we're opening the door to, breaking the boundaries between CLs and ELs in a way that we didn't do before, it's better to just keep it absolutely minimal. 

**Mikhail**
* Alternatively, there was a suggestion to, for CL to use Json RPC API endpoint to grab the information required to implement some heuristics and encapsulate this, completely in CL but I should say that EL has, all the information required, for that and probably some information will be really difficult to expose. 
* Why engine Json RPC API and this is additional complexity, definitely to do that. And the existing information that one can grab from JS R CPI might not be enough for, implementing some heuristics. So it's pretty constraints, constrained path. 

**Danny**
* Yeah. Not even, not cuz even like types function, just all sorts of stuff that exists in EL to process. Even if you can get the data on this CL 

**Arnetheduck**
* Yeah, that was actually my suggestion.  I think, the reasoning was more or less that the CL has other information that it might want to weigh against, whatever the EL is claiming. So like, you know, a little bit of censorship is fine, but I'm happy to be bought off by, a big bribe and you still can be right. 

**Danny**
* And you still can be right.  I guess you, you you only see true false, but you can still decide whatever you wanna do with true false. 

**Speaker: 6**
* There is still the value on, on the, that you can read. So it's it's matter of bribe you, you see the value and you can decide to ignore the flag at this point. 

**Danny**
* Yeah. You could also see false and have seen, you know, eight missing blocks and say, you know what, I'm gonna build locally. So Yeah.
* There is information. It's just less granular obviously. Yeah, I mean there is, but like it's, it's, it's very binary By definition but it, it in many, I mean I could be naive, it seems sufficient, but maybe I'm missing something 

**Protolambda**
* And, also it's not really binary, right?  So here is, we have on the CL side all of the information that we can process and we make a decision and then the EL side has whatever information they have and they make a decision and then we get to choose whether we're gonna do or not without having to know how to pass the EL side.
* So you whatever nimbus decide, they might want to say, well, if I'm connected to Geth, I more or less understand what is the implementation of Geth, and I know what true or false means and I implemented this prism, I might say, well, I know what Eric would do and then I'll just pay this or that much attention to what Argon does. But, I think it's, it's not really binary. 

**Danny**
* No, there's more information. Also, it does not preclude a client from hitting the JSON RPC and doing other things. 

**Arnetheduck**
* Do we have a good JSON RPC to query the transaction pool this way? I basically, I don't know, give me the top 10 transactions.

**Marius**
* We,  have the TX pool namespace in, in Geth, and you can query the whole, transactions, but this is a lot of information and it's very, not really meaningful. we don't have a endpoint that like Sorts transactions Yeah. Or sorts of transactions by arrival time or stuff like this that's not really implemented.
* And it's also something that might not be going to be implemented. So we're kind of moving away from this endpoint in Geth because we want to store way more transactions. Right now we, the transaction pool stores roughly 5,000 transactions in memory, and we would like to move to a world where we, can dump some of the transactions to disk and only maintain the metadata for those transactions. 
* And in that case, servicing these, these, transaction per queries that we have right now, wouldn't be possible for us anymore. It's  already not really possible for block transactions. 

**Arnetheduck**
* All right. No, I wanted to explore the idea before, before we commit to this, but I think if we get a boolean, we'll we'll implement it for sure. 

**Danny**
* Okay. Further discussion.  Mikhail  this has not been brought up on the EL call, has it? Sorry, This has not been brought up on the execution layer call, right? 

**Mikhail**
* No, it wasn't. I mean, I was before, but it was While, a long ago I guess. 

**Danny**
* Yeah. But as a breaking change for the Cancun engine API, it has not been brought up. 

**Mikhail**
* Yep. It has. I think it works to do it next, next week. 

**Danny**
* Yeah. And maybe right after the call we can try to circulate it and get some async conversation going. so that there's something that looks like clarity before the call. 

**Ahmad Bitar**
* Do these changes in that engine API require an EIP or no in The Spec? 

**Mikhail**
* Oh, it does not, no. There's just changes in this spec. 

**Danny**
* So the, the merge EIP and the consensus layer specs kind of describe the high level communication and the requisite validations in the abstract. and so that remains stable and all this other stuff is an implementation detail, but doesn't affect the course box. Okay, great. next up, we had committed to revisiting three six, a couple weeks ago.
* I hoped that some engineering folks on the various teams have had a chance to look at the main net three six data experiments. We had hoped that we would have a testnet at this point. Do we have DevNet seven? Is that still work in progress? 

**Parithosh**
* It looks like by passing all the five tests that we wanted to. So we'll start planning it out and most probably launch it tomorrow, if not Monday. 

**Danny**
* Okay, cool. obviously the mash, the type of nodes and the load are certainly very different on our dev nets, but I think there was a desire to see dysfunctioning on there. open it up for conversation. the spec is currently written as 36. Is there any further opinion on the data? thoughts on load, thoughts on, the stability of picking such numbers? 

**Mikhail**
* I haven't been spoken to Anton, about this, thing and he said that he think that this is fine. the only, thing that he is concerned about is, is the flood publish and if the flood publish is adjusted  to these, large bulb messages to the large, messages. and in the context of 4844, and it should be fine from his perspective. I mean, like 36, blob should be fine. 

**Danny**
* What is the status of doing a staggered flood publish? We'll be doing it Pre Deneb, like it will go out for Deneb. And, and will you be doing any sort of like, bandwidth estimation in doing so? Or that will just be the behavior and maybe you can turn it off? 

**Arnetheduck**
* We're gonna start with a reasonable value, probably user configurable. and then we figure out bandwidth estimation, which is tricky. but on the other hand, we're gonna base it like not on the net. Like we're gonna base it on message sizes and, and like reasonable bandwidth for what a node should have.
* And then we're gonna include a couple of fail safes as well so that we like if we run into slow pair, that that pair doesn't break the thing and so on. but we're certainly gonna do something because like, above all for blocks, it's a topic that everybody's subscribed to practically.
* So if you're connected to, you know, 30, 50, 70 pairs, that's a lot of pairs to be flat publishing to. So it's like Right. It's a no-brainer that we need some limit and then what Yeah. 

**Danny**
* Limit is gonna and stagger, I guess there's two things. 

**Arnetheduck**
* Yeah, But like , flood publishing in its pure form would send it all connected pears. 

**Danny**
* And that's not, That's the same thing. 

**Arnetheduck**
* Yes. So like, if you're, if any client is not implementing any kind of limit to flood publishing as it comes in, you know, native gossip sub, then this is, this is bad. but then the staggering  is another thing. And like we have a long conversation about this in, in early P2P repo as well. 
* But the basic idea at least is that, for the first heartbeat we tried to flood as much as possible, but after that we kind of want to leave room for, I have an, I want mechanism to do more of the work, because it's less redundant. 
* So, well that's where the backup mechanism comes from as well, where, and then we're also discussing this other protocol upgrade, which is the, I don't want message, which is basically saying that I got the message, I please don't send it to me anymore. And, and  I think I would really love to push for this to happen before as well, but I dunno if timing wise that's possible, but it's, it's a really important part of the overall strategy, I'd say. 

**Danny**
* Yeah. I don't want is, backwards compatible being, it could be partially upgraded. 

**Arnetheduck**
* Yeah, But, but like, yeah, you get more benefit. It's a significant difference. And it kind of depends on most clients implementing it or other, the more knowns online that implement it, the better it works. 

**Danny**
* What is the status of that spec becoming a spec rather than a PR discussion? 

**Arnetheduck**
* I don't question. I haven't looked at it. Yeah. 

**Danny**
* There is a  That about a couple weeks ago and it was still active discussion rather than something that looked like it was gonna be rolled out into the full spec. 

**Arnetheduck**
* Yeah, I mean, the alternative is really the, like we might pursue an experimental version of it before the spec is out. I mean, I find, I feel that it's that important, but then we'll have to deal with the upgrades somehow. 

**Sean**
* Do other clients have notes about their, flood publish modifications and, or that I do not want, well, I know age has been working on like the flood publish modification, like specs, and I think he's been doing some experimentation, but like, I, I don't have much insight specifically into what you doing. and on top of that, he's also working on like experimenting with using quick as a transport protocol instead of TCP. but yeah, both of those things, like I don't think we really have results from yet. 

**Danny**
* Got it. 

**Mikhail**
* Probably we can in one in the next, for 4844 call, we can recap the networking thing. I mean like, what should be done and what we highly desire to be done before fork on the networking step, so, and discuss more, like, I don't want them to like publish and all this Yeah. And update statuses on, on those implementations and backward. 

**Danny**
* Yeah, agreed. And I can knock on a few doors between now and then and make sure that the information surfaces, so that'll be a one and a half weeks, which hopefully we can talk about on the breakout call and then surface it again here. 
* I guess fortunately the staggering approaches, and blood published modifications can happen very independently of each other. the, I do not want, I would much rather see as like a solidified spec than something experimental, but I guess we can cross that bridge as we get there. 

**Pop**
* I'm quite curious, like, if there is anyone here that, that can merge, the PI into the spec, it seems like, that level is maintained by other group of people, Right? 

**Danny**
* And we can always fork, but it'd be best to get it into the main, I guess I'm not, I'm just not at the, I'm not sure, given where I last looked at the conversation, it wasn't clear to me that the kind of general R&D effort was ready to merge it in, but that could have changed since I looked at. 

**Mikhail**
* So we can ask for two maintainers, what's block and despair from being merged, so can reach out to them, on Dankard comment about the attacks. I think we should not worry about such attacks because, the system will, be able to pass tho those transactions through. 
* Yeah, there, there could be, empty slots as a result of this attack, but considering the cost of this attack with like, no gain or almost no gain for someone's just, you know, bugging the system for short period of time, this kind of attack does not look like a sustainable attack long term, like a viable attack. 

**Danny**
* Yeah, I mean, I suppose it's unclear what the threshold of making it a viable attack becomes, right? Or we does adding all the, the blobs lower the threshold, thus lowering the cost for such the attack. it's also hard to parse in the context of split meshes, which that block would ride on a split mesh from the rest of the data. So it feels like an unknown. 

**Mikhail**
* Yeah, that's correct. 

**Ansgar**
* Yeah, just wanted briefly say, of course, it's, it's a bit of inside, bo because the main conversation here around is, is of course around just the, the normal case. But  I think it's important to think about a little bit. It's obviously the situation will strictly get worse than before just because blocks can still be as big as they were before and they're still propagated as one thing, and then we have these, these additional blocks now,  I think I personally be fine with just physically not worrying about it too much, just because also it's in the best interest of proposals to make sure that block arrives at in time. 
* So if this actually becomes a problem on mainnet, we could imagine having just slightly modified block building behavior where you just make sure your block never gets too big, which is not actually too bad to do.  so I personally don't worry, wouldn't worry about it too much, but I do think we should at least basically make sure we, we don't just forget about it, we are just basically we make the conscious decision not to worry about it. 

**Mikhail**
* That that's all, yeah, I pretty much agree and I would like to add that it, adding blobs might reduce, the thresholds, but I don't see how it reduces the cost of this kind of attack in terms of spending Eth to keep your transactions, keep your large transactions at the top of the mainpoll or buy the space from, and the space from block building market. 

**Danny**
* So The percentage of the block The same, The percentage of the block you have to consistently buy is lower. 

**Mikhail**
* Yeah, Of course. 

**Danny**
* But, but I guess, But with the exponential considerations, yeah, it maybe it converges that, not sustainable regardless. 

**Mikhail**
* Yeah, I would say that it seems to me that what is, what is like makes this attack cheap. I mean like the space that one can buy and pay, not that big cost. this in this case, I think the network can handle this. It'll not, it'll definitely not be more than one megabyte or even more than a half of a megabyte. yeah. 

**Danny**
* Okay. So we will monitor devnet-7, which will have these configuration values. when is the community biweekly call? Alexa, you mentioned that in the chat. let me check. But most likely actually Tuesday, lemme show the calendar. okay. 
* Yeah. So given the urgency of maybe some of the, I do not want things that might be worthwhile for a couple of us to join that call, we will surface more discussion around flood publish. And I do not want on the 4844 call in a week and a half, and we'll talk about this again, two weeks. Parithosh, you have a Holesky or is that how we pronounce this update? 

# Holesky update -- Holesky Testnet Launch Coordination Call #1 #814 [36.55](https://youtu.be/zdqtl9x_UjA?t=2215)
**Parithosh**
* Yep. we just had the community call roughly in an hour, and we decide we have commitments from all the client teams that basically sign up to about 1.7 million, validators, we're gonna be validating if that actually works. We're just gonna have a small side chain where, where we're gonna load up, every single client combo and make sure that we can handle such a large genesis state. 
* But if that's the case, then you should expect Genesis State to be ready at the end of July. And ideally they're included in all client releases by mid August so that we can, so that we'd be on track for mid-September Genesis. there's a link to the key takeaways as well as call notes. so please have a look and let us know if you oppose anything. 

**Danny**
* Is the allocation, fixed? 

**Parithosh**
* Yes. The allocation is mostly fixed. We have, three tiers, client teams, no operator slash L2s and others. in case someone did not make it in time, please post a comment with a reason and we're still open to evaluating stuff case by case, but ideally we don't want to, cuz we're already over our plan target of 1.5 million. 

**Danny**
* Got it. Well, there's a difference between the validator allocation and the allocation inside of the execution there, right? Is it, or is there a zero allocation in the execution there? 

**Parithosh**
* No, there would be a allocation in the execution layer and there's a separate issue for tracking that. I'll just share a link to that as well. Yes, I'll share a link in the chat for them. 

**Danny**
* Any questions for Parithosh? Great. any other Deneb have discussion points for today? 

**Parithosh**
* There was a, it would be awesome if client teams could, especially CL teams could DM me which branch I should use for DevNet set and keep an eye out for inform that. 

**Danny**
* Okay. so there was a release. The release has 4788, 7044. It's 3045 built into the spec at this point. DevNet seven is only 4844. obviously the divergence here might cause some stickiness, but hopefully after DevNet seven we can move towards full future testnet. if that's not the case, then we might have to revisit kind of how, what test vectors are released, what clients look like and things like that. 
* But at, at this point, I don't think there's much to revisit. I we wanted to get the spec out there so development isn't blocked. hopefully it doesn't cost too much issue. Are there any questions or comments on the state of specs versus devnets right now? Okay, cool. Any other devnet related discussions? 

**Arnetheduck**
* I have a question. So spec 14 includes this attestation subnet subscription stability subscription model change. Do we have a rollout plan for that? Like when clients start using it? When clients start enforcing it? 

**Danny**
* Yeah, so it's a backwards compatible change right now because of the not any peer scoring. the intention is to turn on the enforcing of it at plus one hard fork, I believe. I would have to circle back with, age on whether he intended to change the spec such that it was at Deneb, but right now it can be rolled out in a backwards compatible way. 
* I guess we should bring up the discussion as to whether that's the never plus one hard work for the enforceability 

**Arnetheduck**
* And the other thing, the enforceability is nice, but obviously you can just not join the mesh. Did we ever solve that? 

**Danny**
* What do you mean? 

**Arnetheduck**
* Well the enforcement says basically that if you're not subscribed to the right topic, you'll get a penalty. but you can subscribe to the topic and then leave the mesh so you still don't take the traffic hit, which is kind of equivalent, 

**Danny**
* By leave the mesh, meaning you don't have any peers on that mesh.  Yeah. Even though you're aggregating topic. 

**Arnetheduck**
* Yeah, Exactly. Yep. Because you can't really detect that somebody else is, on the peer, like has the peers in their mesh already and therefore is grafting you from the mesh when when you try to, Right, sorry, pruning you from their mesh when you're trying to graft them. and the effect is kind of similar-ish actually Similar to what? Similar to just not subscribing your node, Right, Which is what we're trying to sort of enforce here that people subscribe to the subnet that they're supposed to be subscribing to. 
* I mean, the implication that I was thinking about as well was for Lightclients. right now they're kind of uncharted territory. Whether they should be subscribing to the block topic or not, probably not, maybe, and they should be rec grasping, their blocks maybe. But there's no real policy for what happens when a light client like connects to a node. 

**Danny**
* Yeah, like right now, right now, in many ways you'd probably be downs scored. 

**Arnetheduck**
* You might, there's no explicit downs scoring. Like there's nothing that says that you have to subscribe to a block topic, for example. You should, but only if you're synced, for example. So you can't really tell an unsynced node from, like line. And so there are all these little gaps, let's say that that one could think about if you wanted to. 

**Danny**
* Yeah, I'm not sure age is consideration on subscription versus participation and if there's any sort of, I mean, intuitively you would probably not be able to actually know if somebody's forwarding messages along or participating at  the level you expect them to. but maybe there's another consideration that I'm not aware of. 

**Arnetheduck**
* But anyway, rollout is as clients want or Continuous at this point. 

**Danny**
* Yes. 

**Arnetheduck**
* Yeah. Okay. Cool. 

**Danny**
* Cool. Other Deneb items? Any other items for today? 

# Research, spec, etc - max effective balance -- Max eb increase EIPs#7251 [46.31](https://youtu.be/zdqtl9x_UjA?t=2791)

**Mikeneuder**
* Yeah, could I chat a bit about the max effect balance stuff if now's a good time? Yep. Cool. Yeah, so I guess conversations have been continuing. thanks very much to dap Lion, Mikail and, and Francesca, we've all been kind of jamming on this together and it's been super helpful. 
* So I wrote up, a short one pager on kind of the status of these discussions. I also opened up a kind of a very draft PR to the EIP directory here. so yeah, I guess a few just kind of running down the, the biggest discussion points right now, I thought that might be useful. So first is the idea of execution layer triggered partial withdrawals being a pre-req for the max effective balance increase. 
* I think this wasn't originally the consensus, but now it's, it's kind of shaping up to be just in terms of UX being pretty unacceptable otherwise. the idea here being if a small validator opts into compounding, they basically will never see withdrawals ever until they fully exit their validator. Even if they stake from like 32 eth up to 40 eth for example, over  months or years, then they need some way of withdrawing some of that without exiting their validator fully.
*  So execution layer partials are kind of what we're saying is a pre-req for the max effective balance increase. the question kind of then becomes, do we do that in the same EIP as the max effective balance increase or do we bundle it into 7002? 7002 is, an EIP from Danny about exits coming from the execution layer. Here's the consensus spec PR, and there's a link to the EIPs PR in there too.
* So yeah, the, the decision around whether to include the partials withdrawals in there or in the max spec balance, EIP I would say is kind of still up for debate, but I don't think it's too consequential. so yeah, the second thing I wanted to bring up is this idea of proposer equivocation issues. So basically slashing penalties are, as written in the spec, are proportional to the effective balance of the validator. This has to be the case for a testing equivocations because that is actually like fork choice weight being thrown around if, if there's an equivocation there. 
* But for proposal equivocations, we think the penalty doesn't necessarily need to be proportional to the full effective balance. And the reason being the proposal equivocations kind of only proportional to 132 eth validator, kind of misbehaving, because, a larger validator doesn't have higher weight on a proposal than a 32 eth validator. So yeah, the, there's a bit of discussion around how to handle that, but that's,  one thing that comes up. The reason, one reason that this would be a desirable is just to help de-risk consolidation. 
* Like  if big stakers consolidate and there still is such a huge slashing penalty for a double proposal, then even like non-malicious double proposals are really heavily penalized, which might not be ideal. additionally, the third thing I wanted to bring up was the pros and cons of just removing the validator sweep altogether. 
* This came up, I think Danny brought this up when, when discussing the fact that if we have execution layer triggered partials, then maybe we should just turn the sweep off altogether. this would make a lot of things easier from the implementation perspective, but it's also like pretty invasive because then everyone who's used to these automatic withdrawals would have to set up some way to trigger them. 
* And you know, it's just a bigger overall change to the network. 
* So not sure if, if that's possible, but yeah, kind of continuing keeping that discussion alive just in case it is possible because then it makes a lot of things like it's almost intuitively like the right way to do it because then everyone's compounding automatically and they only withdraw like as an opt-in thing and they withdraw however much they want to. And then the last thing is this ejection balance consideration. 
* So this was brought up in the ETH research post the proposal. someone commented  on what the ejection balance could look like. So right now the ejection balance is fixed to 16 eth. so  it's kind of like intuitively half of the max effective balance. 
* And the question here is like if someone has a really large effective balance, like 2048 eth, is their ejection balance still 16 eth because then it would take basically forever for them to drain out, through an activity leak or whatever. 
* And the kind of the use case here for who we're trying to protect is people who might lose their keys. Obviously, like a big staker losing their keys is pretty unlikely. And yeah, but there was some back and forth on like, if we could say make the ejection balance like three eth below their highest effective balance that they ever reached, then the most, like we could guarantee that even if you lost your keys and you're a huge staker, the most you're ever gonna lose is three eth and you just have to wait for the inactivity leak to bleed you down to there and then you'll get ejected. So yeah, those are, those are the things I wanted to bring up.
* Again, that doc that I linked initially has kind of some of these discussions and will be updating regularly as, as they evolve, but just to highlight execution layer partials, proposer equivocation penalties instead of slashing pros and cons of removing the validator sweep altogether and considerations around the ejection balance. So yeah, happy to take questions, and definitely to the other folks that have helped work on this. please chime in if I missed anything. 

**Protolambda**
* Yeah, just a quick comment on the sweep. just two comments. one is that, mixing this with the exits,  of PR of Danny, it's a bit of a thing, right? Because the, the exits means, it's easy to implement, at least on the consensus side, and the withdrawals, if you don't take away the sweep, it's very hard to implement on the consensus side, and it's probably even hard to specify how it would work on the consensus side and also when have to take, care of making sure that everyone would be able to, if we remove the sweep, the current addresses that are, that are being forwarding with, with withdrawals now might not have access to like triggered the, To make the call. Yeah, Right. 
* So, I don't think it's even possible to get out of the sweep given the kind of commitment we've made. So I would want to see research on this. 

**Mikeneuder**
* Yeah, that that's a good point. 

**Danny**
* Yeah, and in the past we were able to do, we were trying to figure out if you could do push first pull withdrawals. there was an effort to go and look at the, to do a scan of all the different execution layer contracts, that were set for withdrawal credentials. There weren't that many at the time, so we were able to get like kind of a complete view that has changed so it might be interesting to do an analysis there again. 

**Mikeneuder**
* Yeah, I do think the sweep would probably be met with a lot, like removing the sweep altogether would probably be pretty controversial, so we just we're throwing it out there more as like a, you know, a farfetched idea than necessarily like pushing for it. 

**Protolambda**
* But it would be, you know, kind of if we were designing it from scratch now, I think we would, we would prefer to not have The definitely, but then  if there's no sweep removal, then I would propose that this is considered completely separate than then's PR  7002. 

**Mikeneuder**
* I see. So you're arguing that the partial withdrawals shouldn't necessarily come through the execution layer at all, is that what you're saying? 

**Protolambda**
* Oh, No, I'm hoping that they are. I think this is a very nice UX to have. It's just that mixing it with something that is very simple to implement as Danny's PR, I think it's,  just a way of delaying Danny's pr. 

**Mikeneuder**
* Sure. Yeah. I guess the, the only counter argument is like if we do the partials in Danny's, then the max EB PR is like very simple because then we don't have to do any of the UX considerations. 

**Protolambda**
* But yeah, I Think it's, it's then, then I'm only pointing this out, which is a tiny piece of the max ev then, I mean the max ev, it would be very nice  to see and have a larger conversation about the security issues of it. 
* And we've had had these kind of changes to fork choice and that we kind of rushed into them and then we found, very deep security concerns. It would be nice to have a longer conversation on the max ev and how security is and these things that are probably out of scope of this call. 

**Mikeneuder**
* Yeah, for sure. I linked a doc called Max ev, increased security. This is, something for, and I wrote, so that has, that covers some of those things, but yeah, I agree the, it's a bigger PR than the 7002 for sure. And I guess, and maybe it makes sense to bundle the execution layer partials in with Max ev then just because it's all like one atomic unit, which might be cleaner intuitively. 

**Danny**
* Yeah. Oone consideration for 7002 is, is at least even if you're not doing things like, removing the sweep or other stuff like that, you know, do you add maybe  a balance field where if it's max sense it's an exit, otherwise you can interpret it as something else like a partial withdrawal so that in the event that you do want to trigger information from, more information from the execution layer, you have it there rather than having to go back and make a cross layer change at that point. 
* Obviously we've shot ourselves in the foot prematurely optimizing like that before, so, but at least a consideration to, you know, do you try to make 7002 slightly more generic? 

**Mikeneuder**
* Cool. Yeah, I think, yeah, big action item for me is to do due diligence on 7002. 

**Protolambda**
* So that's something I'll Just throwing this out, as not depending on how much we're willing to wait, it's even possible to do this in stages. We could deprecate the sweep and allow validators to exit, even if it's that that might be impossible, impossible as well. But we could do this in stages on deprecating one hard fork hard for and then implementing without the sweep in the next one. 

**Danny**
* By deprecation you mean a signal, a commitment in the spectrright? 

**Protolambda**
* A commitment that you, you need to exit your validators. That now that we are allowing them to exit this way or another way by the these many forks, we are going to remove the sweep. 

**Danny**
* Yeah, certainly an option. I think we're probably not quite there. 

**Mikeneuder**
* I mean the, we could also do the other order, which is like if we have max ev and partials, then we signal removing the sweep after that, right? Because now suddenly the sweep becomes like less relevant and if people wanna exit they can, I think that might be a more reasonable track, but yeah, Either seem good 

**Danny**
* Regardless of deprecation.  Notice a validator presumably can exit. So they would always be able to exit, you know, even if he did instantly. if they can't then that's a problem. Yeah, I mean, and there are, there are validators that can't exit. 

**Mikeneuder**
* There are people that have lost, Yeah, that's the ejection balance stuff too, right? 

**Danny**
* Like Yeah. Yeah. So they're just waiting for 16 E one day. Okay, cool. So, this is a PR for EIP think the design doc, is where a lot of the considerations might go if you're interested in following this, design path. Do you have any other questions for Mike today? Cool, thanks Mike. 
* I'm gonna get 7002 merged. and it's something I would like to discuss in the coming weeks, coming months, just as another potential feature, but not for them. We'll probably do a process. Is it merged now? 

**Mikhail**
* Yeah, the EIP is merged. 

**Danny**
* Wow. I didn't even know, was EIP Recently? The editors are EIP yeah. Okay, cool. I'm gonna do a pass on that. But anyway, check out 7002. I think it's a nice to have feature in the coming works for the theoretical fork after deneb. That will be a star name starting with we will create a tracking issue, and people can toss potential stuff into it. I think we're probably a little bit early, but it's the beginnings of that conversation probably start today too soon, almost too soon. 

**Mikhail**
* One quick thing with, 7002, I think there is a bit of a space, to pass the balancing, to pack the balance as a part of other pop key. The second part, because it's 48 bytes and we break this down and into two pieces, but definitely would be cleaner to have a separate storage slot for the balance if you want that. 

**Danny**
* Sorry, what field were you gonna pack it into? 

**Mikhail**
* There is the validator pop key, which was sore right in the, in the storage, when this brick file is being called and the pop key is broken into parts first 32 bytes and the next 16 bytes. So we have like 16 bytes of space, which yeah, which probably not enough, Okay, sorry. Yeah, sorry for degrading the main conversation. 

**Danny**
* Well, but the, you could pass it in as an argument, but it wouldn't then pass into the message. Would it pass into the message because the message is actually packed 48 bytes? 

**Mikhail**
* I don't know. 

**Danny**
* Yeah, That's alright. We can take a look at it. If there's probably not a reason to shove stuff into the extra bytes of another field at this point if we want it, we still, this design's pretty wide open so we can revisit that. 
* Okay, Cool. other discussion points for today? Yeah, Potos, just to a quick comment on that. in terms of the consensus layer, it can be a binary operation of the time, right? It can either be, if it's max accent it's an exit, if not it's a no op. so there are, there are pretty simple ways to have that field available and, and really not change

**Protolambda**
* Oh, so you wanted just to have the field so that for future, like we just keep it as a no op and, but then the field is there. 

**Danny**
* Yeah, the argument there would be to reduce the changes you have to make on the execution layer to make further changes on the consensus layer to have this, the data available that, but we've done that many times and have weird fields sitting around that we never use like whistleblower index. 
* So like it's just, it's a possibility. I just wanna bring up, I would not argue to do 7002 and utilize that field in a meaningful way because that changes a lot of things, right? Like all of a sudden partial withdrawals have to think about the queue in relation to the validators that churn and, and things like that. which is a much, much deeper consideration as you noted. Okay. Anything else for today, Tim? Was that a spicy enough blob data size conversation for you? 

**Tim**
* Yes. And you're finishing right as I'm done packing, so couldn't have asked for a better call. 

**Danny**
* Thank You Have a great vacation. Okay, thank you everyone. talk to you all soon. Bye-bye everyone. Thanks all. Bye. 


____

### Attendees
* Danny
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



