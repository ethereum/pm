# Consensus Layer Call #86 Notes 

### Meeting Date/Time: Thursday 2022/5/5 at 14:00 UTC
### Meeting Duration: 1.5 hour  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/521) 
### [Audio/Video of the meeting](https://youtu.be/nnjeqZK7jgU) 
### Moderator:  Danny Ryan
### Notes: Alen (Santhosh)



**Tim Beiko**
## Intro [0.51](https://youtu.be/nnjeqZK7jgU?t=52)
* Okay. The call should be transitioned. This is Consensus layer Call 86 and here it is the issue is you 521 on the Ethereum repo. we will focus on the merge as much as there's an appetite for it. Do a little bit of client updates. There's a couple of things that have come up for discussion topics, episode and build our API. And we'll go from there. Okay. to kick it off, we did have a merge testing call on Monday, I believe. so if there's anything else in addition to what we've covered on that call that we'd like to cover today, we can cover it now in the testing section,I know that there was a mainnet shadow fork, #3 today. Does anybody want to fill us in on the details?

## Mainnet Shadow fork updates 1.53 (https://youtu.be/nnjeqZK7jgU?t=113)
**Pari**
* Yeah, heavy one. so we had three today. I think we hit TTB around 1:00 PM. so pre TTD, we were at something like 99.8% participation. We were seeing really healthy block production.I think the only issue PTD was sometimes prism based who was missing a couple of blocks, missing proposing a couple of blocks.And I think the besu team already had a theory for why that could be, but you have to be charged, post TTD.We were at 97.6%. So the same prism base that had some issues before was then dropping off the chain post TTD. A while later we noticed something with prism Nethermind as well. Mike was looking into it, but it's also not like a static issue.It's like that combination of test and propose for awhile then dropped off and I think came back again, but there was also, someone looking into it and there Mike have already been a fixed.So it might just need to be updated. I'm not sure. so all in all, I think it was a great, shadow folk. We were almost bugless this time and we're still seeing really healthy block production.I have like a monitor, enabled on Teku.I don't really see any blocks being late. So we're seeing that's produced on time. the sites that there was an additional test and the shadow fork, I've just posted us out of that test as well. essentially what we did was we spun up a couple of nodes. We allowed them to sync up the head, before TTD about one to two hours before we paused either the cl or the el to simulate them having the sync. And the moment TTD was hit, we unpause them.So this is before post TTD finality. there is, we're kind of mixed. I think the prism gets and lighthouse get combo, had some issues sinking up,but prism, Nethermind, lighthouse, had more problems. They seem to be centered perfectly. this is still new. So I don't think any of the client teams have had time to look into why this happened,but yeah, that's setting the overall status update. Congratulations, everyone!

**Danny**
* Any other comments or questions about the mainnet fork? Great.Thanks.cool.The next thing I wanted to talk about, and I believe some of you are on the call or at least are aware of some of the discussion last week on the, Allcore dev call around the difficulty bomb. I just want to do a quick status update and get everyone on the same page there. on the execution side, the proof of work side still, it was discussed as to still attempt to not diffuse the bomb, but to revisit this, on the next call and the call after, given status with testing and that shadow forks and things like that. I think essentially in may, we need to be either making decisions about for being public testsnet and dates around those, or making beginning to make a decision about diffusing, the bomb, a much discussion ensued. Tim, are there any other relevant points from that discussion you want to share here? 

**Tim Beiko**
* No, that's, that's pretty much it it's like we're in this weird spot where if everything goes well, we might be able to merge without delaying the bomb, but if we have some delay in the merge, then what we'll probably have to, and, and for, for everything to go well, we kind of have to start looking at, at moving testnets in the next couple of weeks. Yeah. 

**Danny**
* All right. Cool. any discussion points around that? Obviously it takes two to tango. you know, if we're having issues on the consensus layer, that would cause the delay, the vomit for having issues on the execution layer that would as well. so I don't mean to say this decision because it wasn't necessarily decision was made without y'all, it's a kind of a we're in this phase in may where we really need we're monitoring, whether we're on go or no, go to the next testnet phase,Speaking of the next testnet, that phase, Ropsten, spolia and Gorley are planned to be go through the merge. I believe Ropsten is at the beginning of that list, although that might be a for discussion, and to do a Ropsten merge, we have to make a Ropsten, you can beaconchain or parallel to Ropsten to make it be contained. so I think to be prepared for that and maybe to give that beacon chain, at least a couple of weeks of activity before doing the merge, when you'd have that conversation now, quick question is Ropsten to be maintained after going through this fork or will it be deprecated? I saw in like the OG council, there was some discussion of deprecating it after the fork, but I hadn't heard of that prior. 

**Tim Beiko**
* I think the idea is, we would, we being the client devs would like to no longer maintain it, not necessarily, you know, the day after the fork, but like, you know, call it a few months after,  the, then only have Gordy and be like the two clients maintain long live Testnet. yeah, people don't like when we deprecate Testnet so there might be some company that like chooses the maintain Ropsten didn't, but, yeah, I guess from our perspective, we don't want the maintenance burden anymore, 

**Danny**
* Right?So we have two Beacon chains one for Ropsten and one for Sipolia. And I think we should make a plan for them. I think primarily our options are low validator count, high validator count permissioned, or on permissioned permission, we can use the, the ERC 20 variant of the deposit contract, to essentially restrict set of validators and make it, you know, it's not clique, but clique, like in the sense that there would be very known entities and operators that have, validators, or you do the other where you, you open it up for more public testing.Gordly and Pyrmont based off of it is, does serve that function. but you could argue for essentially doing that here as well does anybody have Opinions to share on the value of doing beacon change structures in one way or the other for other of these tests, 

**Micah Zoltu**
* Just to make sure I understood correctly, Gordly will be un-permission,Right? Yeah.I don't have any opinion on the other stuff. 

**Danny**
* Yeah. So I think Ropsten I think it might make sense for us to also make it on permissioned, but for us to have a bunch of the validators, just so that if others want to get in, on practicing the transition and running validators, they can do so, but we also don't care if it becomes unstable eventually, because we don't plan on maintaining it. so then the question is on Sipolia, do we want permissioned or on permissioned, given that Gordly would be kind of the one un-permissioned one, 

**Tim Beiko**
* One thing we discussed like a few months ago when we were here or were talking about this is like, if we have a permission to want, it's easier to actually test some like, chaotic states, like shutting down half the validators for a week and seeing what happened and things like that. and also we probably don't want to do stuff like that on a testnet, which has a ton of end user applications. Gordy obviously does. so I think it probably makes sense versus 

**Danny**
* Sipolia have a bunch of end-user applications. 

**Tim Beiko**
* No, not today and like, yeah, today basically then. so, so like, I think it, it might make sense for us to use the Sipolia as like a consensus level Testnet and people are obviously free to deploy it as well. But, yeah, this way, if we decide we want to shut down the validator or part of them for a week or two, and see like how the AME activity leak happens or long periods of non finalization, I don't think we should do that on Gordy because that affects a lot of people's applications, but probably it might be a good, a good fit for that. And then a permission validators that makes it easier to, to control those things.Yes. 

**Pari**
* I like to add on that point. I do think it makes sense to have Sipolia permission in the end, if we use the permission contract, we'll be token dated. So we could still like, make it on permission, but people are not, using bots to steal like the underlying assets. So we're not like people don't have to fight over Sipolia, rather would fight or whatever we create. so it might be a bit easier to avoid wasting the basically Testnet tokens. 

**Danny**
* Yeah, it makes sense. I mean, we permission meaning large operators could run validators if they wanted to. And if there was demand for individuals to be able to run a validator or two, we could set up one of those, faucets, although those are always ridiculously gamed. okay. Is anybody opposed to keeping validator you're set on the smaller side? you know, on the order of 16,000, 50,000, something like that, and keeping it permissioned. Okay.And then on Ropsten, Micah, Jason, 

**Micah Zoltu**
* And just, you mentioned keeping it on the smart side, is there any functional difference? Like how much money is a state  you're on the money 

**Danny**
* And it effects validator, state size and some other parameters.but no, there's not much functional. 

**Micah Zoltu**
* We want it to be closer to close to mainnet that then if it actually has an impact 

**Danny**
* Gordly And Pyrmont, we have been doing so we try to keep the validators outsize the same as main net. So we don't necessarily need that in this other environment. And it's a chore, it's something of a chore to kind of always keep the queue running and make sure that mainnet doesn't sprint past Pyrmont. So in light of that, I'd say, try something different here. 

**Pari**
* I guess the alternative argument is we could have something that's twice the size of mainnet, and that's something that would take a long time to achieve on Trotter.Just the question of if that brings us in 

**Micah Zoltu**
* The idea, being that we would see a failure there before we see a failure on mainnet, if there is a failure related to size. 

**Pari**
* Exactly. and also people can test the optimizations that are suited for twice the size of mainnet already, whereas of course we can achieve the same thing with Prada, but it still requires a lot of people making deposits all the time. 

**Danny**
* Yeah. I'm okay. Either way. does anybody feel strongly and I'm also kind of implicitly assuming that the entities on this call client teams and otherwise would help run nodes and validators on this new sustained Testnet.obviously if I'm incorrect in that assumption, please speak up. Okay. I'm going to open up all up and an issue about in the PM repo about the three beacon chains Pyrmont, which already exists, and we'll take a reportedly, one to be created for Ropsten, which we can discuss how we want the Genesis of that to be. and that will be, permissioned and then a permissioned one for support, which it seems like there's a desire to go for a larger validator set. And we can, Take that to the issue though. And I do think that we should launch these by the end of may, if not a little bit earlier to just be primed and ready for. 

**Tim Beiko**
* Oh, I think earlier. Yeah. I think we probably want them launched like in the next two to three weeks, which is like been late may, but not like four weeks from now, 

**Danny**
* Four weeks from now is, 

**Tim Beiko**
* Too late. Yeah. 

**Danny**
* Yeah. 

**Tim Beiko**
* Yeah. 

**Danny**
* And if in two or three weeks, why? I mean, definitely before the end of may, is there going to be test net fork before the end of the May

**Tim Beiko**
* No. Well, I assume you want this thing to be live for more than like a few days before we have maybe not, I guess. Yeah. That was essentially, it's just like you maybe want it to be like for more than a couple of days and if there's a fork in St. June. yeah, 

**Danny**
* Yeah. Okay. 

**Pari**
* We could also do the two separately, for example, the Ropsten one, we could have it smaller, so it's not too much of a task for client teams to spin up nodes, even if it's cost ineffective and just have that index two weeks from now. Whereas if we want to have supplier twice the size of me, and I think it might take a bit longer for client teams to find a place to run them. and that could be like three, four weeks maybe. And that also kind of follows the order in which within a fall, actual Testnet spec drops not happen before supplier anyway, so we should have that extra couple of weeks of weekly. It just comes to the boss of coordination, I guess. 

**Danny**
* Yeah. That all sounds reasonable. And we do have a chance of beacon chain running for a long time that at least for one of the testnets, if that is an interesting parameter in, in these testsnets, Pyrmont serves then 

**Micah Zoltu**
* Give me one sec, great.Three separate issues just so we can keep the discussions isolated rather than one issue. 

**Danny**
* Yeah, that's fine. I'll call it well, and I don't think we need to create one for Pyrmont, then, but I'll make an issue for beacon chain for Ropsten and beacon chain for Sipolia. All right, cool. thank you. Anything else on that one? Great. otherwise on merger discussions, any technical points you will look to discuss any issues. They would like insight on how other people are dealing with things, just in general or discussion. 

**Mikhail Kalinin**
* I have opened the PR today, so just posted in the chat. So this PR is about invalid terminal block and the latest spelling hash around it. there was an RFC, that is mentioned in the PR. So basically the this PR implements one of the options that is listed in the RFC. I would just like, so whoever not seeing this, RFC, previously just take a look at the PR, like to merge it as soon as possible. And if there will be no position, probably been merged will be merged next week. So take a look, please. It also, yeah, this PR is not only about replacing valid terminal block with, like something, but it also covers the blind spot in this bag that has been discovered like, months ago when I was like, we can, go through the list of checks to the engine API spec, and it also mentioned PR. 

**Danny**
* Gotcha. There's also other few PRS open that I believe will be merged very soon. there's, based off of conversations in dev connect to, there was a 216 is open, which is a retake on the engine timeouts, And there's a couple of things related to error codes. So,these will be bundled into a release, but if you're Following them, you can probably, as they get merged to begin to make PRs against Other emerge related discussions, No comment, Perry. 

**Pari**
* I mean, we did the easiest of little figuring out that we need a testnets. Now we have to find the names 

**Danny**
* I haven't.Well,Yeah,I have a suggestion, but once you make a suggestion, you've now begun bike-sharing names. So I will probably not make such a suggestion. 

**Micah Zoltu**
* So you're saying the best way to troll right now would be to make a suggestion to kick off the conversation. 

**Danny**
* Yeah. I think we should sidestep naming them by giving them, Just calling them what they are, the Ropsten beacon chain. But, you know, now I've entered into that conversation. All right. anything y'all want to talk about with relation relation to the merge? Okay. Onward. I know there's lots of conversations that happen at a discord. I know there's lots of conversation that happened these issues. So it's understandable that we don't have a lot to talk about here, moving on,  any other client updates that people like to share? This is going to be an easy call, 

**Micah Zoltu**
* A little bit curious if anyone else is awake besides the four of us 

**lightclient**
* I'm awake The topic I'm just too good. 

## Client updates [23.30](https://youtu.be/nnjeqZK7jgU?t=1417)

**Lion dapplion**
* Quick update. So we released version 55 with lots of improvements as the cost of SAP.This would be five and fixed outstanding networking issues, but we don't score PS without a reason. we also enable the proposal boosts and the both domain, that's it? 

**Age Manning**
* Yeah. I'll also throw some stuff in. I think everyone's seen this, but Michael posted an issue about running fork toasts before block proposals. I'll put it in the chat just in case anyone hasn't seen it, but it looks like everyone has. the other thing that way roughly looking at is trying to, we've got a bit of pressure from the community to implement IPV six. So I'm not sure if anyone else has other looking at that or not, because I think happy V6 only nodes they're kinda gonna segregate themselves.But anyway, that's something in our pipeline. I'm not sure if anyone's looked at that. 

**Danny**
* What, what does the, I mean, IPV six is great. Why do your community members want it specifically? 

**Age Manning**
* Well, we're starting to get, get coined bounties specifically. They're saying that, a lot of them have IPV six only nodes behind, I know some, some moral involved infrastructure, and so they want IPB six support, but I'm not entirely sure how that, how that's gonna play out. Especially like when you're discovering other nodes that are mainly IPV four and Clare communicate WB six. So a lot of them have jewel stacks. So there's this kind of complication we have to kind of add into the lower protocols, which is where we're working through. 

**terence(prysmaticlabs)**
* Yeah. I can chat me as well. So, prison release version 2.1, that once this has the merge, the, the, so this has the most support also as web three sinus support. We also have experimental which such activities, things support as well. You also need for a propulsive boost. It has a bunch of nice of batteries shot, but vascularized shot 2 56 optimization. So yeah, that's pretty much from us. 

**Zahary**
* All right. We are quite focused from a shallow for vestments, but we are shipping one interesting feature that I'd like to share a Nimbus like to now work with in the web three signers set up in such a way that, we connect to multiple remote signers and we will obtain parcels partial signatures from them, which are combined. This is similar to the secret, the validators setup. And it was actually requested, by some staking posts, which have, this concern that a lot of employees have access to the validator keys. So this creates a slashing green risk from potential rogue employees. So in this configuration, it's possible for the staking taking to set up their infrastructure in a way where no employees have access to a full validator key. So that's quite interesting feature. I think, it's possible to extend the key manager API, for example, that's a portal for this type of configuration. 

**Danny**
* Thanks.Alright. Any other, client of? We move on to some discussion points. 

**Saulius Grigaitis**
* Oh,Sorry. Go ahead. 

**Enrico Dei Fante**
* Yeah. So, from, from Teku side, we, there, you have some, some optimization in the backlog around the transition, calculating, applying the transition.So we are in the next release. We'll, we'll include some, some of these action there. We are currently working, implementing the builders, API APIs and, on the merge sides, or just a minor, minor things to improve, not nothing, nothing important 

**Saulius Grigaitis**
* From optimizations.We, we worked on autumn 64 support and also some other teams on the assign their support. And I would say all the initial functionality of the website, we sign our support.That's all 

**Danny**
* Got it. Okay. Moving on. There's a couple of discussion points, but in the chat, Age would like to discuss a potential upgrade for Gusto so-called epi sub age. What's the status on that spec is that actually well-defined spec or is there R&D to do, to actually get it to an implementable place? 

**Age Manning**
* Yeah, so they're like from two years ago, I think in like 2019, there was a planned upgrade from going from like flood sub random sub gossip sub, and then its final thing called epi sub. And I've been looking into just the bandwidth that all that clients are using and trying to minimize it, which we've had discussions with various people about. in particular I wanted to try and make like some of the mesh parameters, a little bit more dynamic of, cause we're seeing, we're seeing, quite a few duplicates, but anyway, the, the concept of epi sub is to make the mesh more efficient without having to, change all that much about gossip. So the, I talked to, who's the one of the main authors of course, et cetera. and he is essentially saying there's very minimal modifications. So he essentially explained the modifications to me.I won't go over in this call, but they're something they're very, they're very minor. So there's some small changes we can do to gossip sub that would be backwards compatible that should make our meshes and stuff more efficient. the reason that it hasn't been specked out or built in limpy to pay yet is because gossip seems to work for, for, for file coin and IPFS and everyone else using it. and no one really has the, I guess, the interest to kind of reduce the bandwidth. So I think the current plan is, given what, visor visor and I discussed is for me to either give, an implementation of these metaphor modifications that we can then spec and ideally I'm chasing, hopefully I go developer to, either mimic the implementation, copy that, helped me, I guess copy, whatever we build up, in rust and port it to go because they have a lot more kind of testing infrastructure in go so that we can test this thing out before actually check it on to, test nets. So it's, it's, it's essentially, there's just some very small modifications to gossip side that we can do that hopefully could have a, a big impact to our bandwidth usage by re minimizing duplicates, making the mesh more efficient. 

**Danny**
* Is there anywhere that's a good source to read about this? 

**Age Manning**
* Yeah, so I think the answer's no, I went through and read all the previous specs for episode and then reached out to advisor and in the call that I had with him, he was just kind of like, I don't know, every, don't worry about all that. We just have to do this, this, this, and it's all kind of small. So, I can, I can write up some documentation that people can read about if, if there's interest In macro. 

**Mikhail Kalinin**
* Yeah. Just to confirm it's not what is proposed on the episode, documentation, in the PTP. I mean, you, you want to try some, particular mechanics from, from this back stuff like implementing this spac. Cause when I was like reading it, I was under the impression that it's, it's not the ads like it's yet in an active research and was not implemented or is there any reference implementation for episodic? 

**Age Manning**
* Yeah, so the previous research was quite involved and I think I've seen like there's some PRS or some issues around and also a different kind of spec version. I kind of read through all of these and the modifications are kind of scattered and, convoluted, let's say the, the actual changes that we would need that create what I advisor calls the episode is we just add an extra control message. I'm not sure if I want to go into these details, but we keep the mesh the same size. And if we start seeing a number of duplicates from some particular node, we, we send like a choke message so that they stop sending us on the mesh and they only send us gossips gossip messages. So it's just, it's more of like throttling the mesh, not changing its actual size. And this is just adding a single control message. the, this is not written any way that I've seen on internet. it was only after the conversation that I had with, with Pfizer that this came out. 

**Mikhail Kalinin**
* Yeah. I see. Thank you. Well, I wouldn't be interested to stay in sync on this. 

**Age Manning**
* Okay. Maybe if there's people that are interested in this in particular go, I go dev either, just reach out to me, cause I'll probably start doing a little bit of work on this because if we can make it backwards compatible, then at least the nodes that are running this can, can get some bandwidth saving. 

**Danny**
* Cool, thanks Age. any other questions or comments for Age before we move on? And I presume once we got this into go implementation, we might want to run it through the mainnet. Like was under all those different attack scenarios. 

**Age Manning**
* Yeah. Yeah. That's the main reason I want a go version and a go dev to kind of help out because we don't have that in yet. 

**Danny**
* Okay. Thank you. Moving on. like client wanting to discuss the builder API status, like Lightclient, can you give us a status update? 

**lightcient**
* Yeah. So a couple update points and then a few questions. we talked about the builder API a bit on all core doves last week, and I wanted to get an idea of how important it was for validators to still control the gas limit that they want their blocks, that they will propose to target, even if they're not performing the production of the block. And the overwhelming answer was yes. So we extended some of the assigned messages to also sign over a preferred gas limit that the builders should adhere to. And there was a small discussion within that about whether they should be siting over the gas target or the gas limits because out there 1559, the actual independent variable is the gas target. But because most clients today still take gas limits to target what's the size of the block will be. we ended up going with the gas limit there.We've had a lot of feedback in general on the builder API PR, which is in the execution PR repo. And I think a couple of things have come out of, most notably, some teams started implementing it and they felt that there was a lot of work going into redefining the serialization schemes for beacon types that need to go over the adjacent RPC, methods that was originally proposed. And there was a request to, to pivot that, API to the HTTP rest style of the beacon API is using. So it seemed like all of the people in the block construction channel were okay with this pivot. And so I've started rewriting the API in that style and hopefully have that done the next couple of days, the core logic will be the same, but you know, people who have a lot of experience working in the beet beacon API and the open API format would love to have some feedback to make sure that the style is consistent with the beacon API and all those other things. So I'll post that some more information about that the next couple of days when that's available.a couple of questions. One is right now, these things have been living in the execution API repo. It doesn't really feel like that's the right place. And I don't know if anybody has an objection for this living in its own repo. Maybe the builder API is repo under the Ethereum of organization. Is that something that seems like a reasonable home? 

**Danny**
* Yeah, I think so. I mean, I think that this isn't necessarily something that like an execution engine and the L client implement,Right.It's another piece of software. you had suggested builder specs instead of builder API, the builder specs repo against I can probably rename it. 

**lightcient**
* Oh it does. Oh, okay. yeah, I don't know. It's like the builder API or the API APIs postfix has been used for the specific specs and the specs postfix has been used for like markdown. It feels like we kind of need both, like there's still some specification related things, but we can talk about that offline. Cool. there's a pending, Okay, thanks. There's a pending PR right now. It's the beacon API has repo into the prepared beacon proposer method. I'm wondering what needs to be done to keep that moving because it's been sitting now for, can be a week and a half. And I think that's like the main thing on the critical path for consensus layer clients to implement so that they can, we can actually get these, non-consensus messages signed by the validator keys. 

**Danny**
* Is this 206? 

**lightcient**
* Yeah. 

**Danny**
* I can just review it right after. It seems like there's been a lot of comments here. was there anything contentious lingering in here? I don't think it is Because it's primarily 

**lightcient**
* The main question that's a little contentious is people feel it's weird to have an optional elements on this method. That was something that came out of the discussion in Amsterdam. I really don't have a preference, whether this is a new method or, an optional add on to this existing method. I just want to go down a route Other than that, is anybody have additional comments or feedback on the builder API or the timeline that we're on? It feels like this is something that should be integrated into merge testing right now. And we're still at the specking stage.So I don't know if people are worried about this for Anything.

**Micah Zoltu**
* You said, posers will provide a, gas target and then the builders should respect that. Did you mean must? 

**lightcient**
* They will provide a gas limit and the builders should adhere to it. I mean, I don't know the builders can do what they want, but the validators you know, don't have to build a block if the builder doesn't adhere to there's, 

**Micah Zoltu**
* I'd say, so it shouldn't a sense of if you want your block to actually be picked up, you'd probably do this. 

**lightcient**
* Right. But again, like if you earn double the rewards through external blocks, you might be coerced into just going along with whatever limit they choose.I think defaults are really powerful there, but it's something, 

**Tim Beiko**
* Is there a reason to not make that a must to kind of remove that the vector of like bribing? 

**Micah Zoltu**
* We Don't have a fee. Well, sorry, go ahead 

**lightcient**
* And put it as a must in the spec. That's fine. It's just that, there's no way .You Actually enforced it. 

**Tim Beiko**
* Right, right. But yeah, if you put it as a must in the spec and you put it as a must in the software, ready said it does raise the bar slightly, like yeah. Probably people this way.Yep. That's definitely what we'll do. 

**Potuz**
* I know. So if it goes signed, we can oppose sorority backwards last year on product 

**lightcient**
* Backwards slash who the builder. 

**Potuz**
* Well, the proposer that actually signed a blog that didn't include his, his, limit his gas limit. Now we can, In the future, we might. 

**lightcient**
* But the thing is, is that I could just, as a proposer go back and sign some message that says, oh, right before I posted my block actually updated my preferred limit. And there's no way cause these aren't posted on chain. There's no way for the network to say, oh, I didn't see that. Or I did see that. 

**Micah Zoltu**
* We can say that if we can assert that if we see two signatures for the same block, with different limits that you were in violation and we reserved the right to, 

**lightcient**
* But it's not per block.It's the validator basically registers with the external builder network by saying, this is my public key. This is the fee recipient address I would like to receive. And this is the gas limit. I prefer my blocks to be built towards. 

**Micah Zoltu**
* Gotcha. Okay. 

**Mikhail Kalinin**
* Oh, also, which like take into account that the gas limit may be like, say 10,000. I have no gas higher than the current gas limit. And in this case, what builders should do should probably increase the gas limit as much as possible towards the gas limit announced they propose it. Right. 

**lightcient**
* Exactly. Any other general, comments or feedback on the status to the builder API do clients seems to feel like this is something that they're going to have the ability to implement in the next couple of weeks, assuming that we have a spec and some testing infrastructure available in the next 10 days 

**Micah Zoltu**
* Just only needed to be implemented consistently, or is there a consensus and execution layer, things need to be done. 

**lightcient**
* The execution or things that need to be done is really in the hands of the external builders who, you know, right now it's Bailey flashlights. And so they have people working on things, implementing that interface. I'm working on a testing,implementation in merge mock.So the people who are implementing this have something that can respond, to request against, but it's our expected execution layer teams, one of them with this, 

**Danny**
* But locally from like a market from accessing the market, just to beacon node for a node that has validators on it is communicating to this like market mechanism. And it uses it's locally able to just be processing things. There's no Right locally how communications to market. 

**Micah Zoltu**
* So I encourage all clients except for prism to integrate this. 

**Danny**
* Hey, the,Distribution is looking much more reasonable on one website lighthouse center, the quote yellow's zone. Cause it looks like they might be a third of the network. Yeah. 

**lightcient**
* So I guess one last question. Oh, go ahead, Danny.  I have a question after you. 

**Danny**
* Okay. I guess one other question from me is there is this situation right now where there's no way to compare a block. I get from the external network versus my local EO. I was 

**lightcient**
* Just about To say. And so I'm curious what client teams are interested in doing about this because I think the right thing to do here is obviously return some value, a field in the execution payload. that's responded by, the geth payload. I think maybe we're too late in the game to have that change, but it still seems something that's important to have some heuristic for CLS to figure out if the relays are just giving you blocks that say are, they're only going to pay you 0.01 ease. And just the basic tip from the ELL block would be higher. That would be a good start. 

**Danny**
* Yeah. It's like for multiple reasons you should always build in parallel because one, you don't want to be hosed by the realtors. And two, you know, you want a, you want like a backup in case the relay just fails. You can do the water, but you can't do the former, can you utilize the ether API to actually get this information? Or is that not? 

**lightcient**
* I mean, I think CLs can do whatever they want, 

**Danny**
* Can CL get the fee difference via using the ether API. 

**lightcient**
* Sure. 

**Mikhail Kalinin**
* The problem is that it will have to, you'll have to have executed blog before doing this request. 

**lightcient**
* Right. But it's constructed the block already. Like I'm assuming it's asking it at the point that it's already received the payload. 

**Mikhail Kalinin**
* If I understand correctly, the constructed block is not like to the beaconchain, the canonical chain automatically by L I might their own. 

**Marius van der**
* Yes, you're right. 

**lightcient**
* So there's no way to query against that state if it's not in the conical train. 

**Marius van der**
* No, but you can execute the block as, for example, trace call or something, Right. 
 
**Micah Zoltu**
* Yeah. But how does the seal, like, what would that look like? How would the CLL say execute that block, hand wavy?You know, that one, like what, what does it mean takes you that block basically depending 

**lightcient**
* On the block and received as a, from its eel, like it's about to propose, it's told it in the next, in the fourth choice updated, it's about to propose it got a payload. And now it's trying to figure out how much is my favorite sippy gonna earn from proposing this payload and mark 

**Micah Zoltu**
* And send the whole block again, just to get the balance. 

**lightcient**
* I think that that would be the only way right now to get the full picture of how much was earned. I think you can statically do it by just going through the list of transactions, figuring out how much gas, each transaction executed and checking the tip, but that doesn't account for Coinbase payments. 

**Micah Zoltu**
* Sure. But even that would require you to still reexecute everything it feels. I mean, I don't know. Maybe it's letters have lots of headroom and doesn't matter if it's, 

**lightcient**
* Well, you can figure out what the gas used without re executing. It's already been executed. I guess you might have to get the receipts though, which isn't a query. I don't think that's given in the current, return of get payload. Right. 

**Micah Zoltu**
* So I think what we have right now, if the execution layer didn't do anything, like the best case scenario is you'd have to execute things again. because we don't surface the information that we need. Right. 

**Mikhail Kalinin**
* Right.But execute in a block will cause a delay. and there is like, if, if CCL will make a decision after executing the block, various state probably will just miss the opportunity to propose time, timely block. Like it reduces the amount of time to propose a blog yeah. And disseminated over the network. I would suggest, the thing that we have discussed on dev connect, they have a get payload. We too. And, yeah. See how it can be implemented. Probably it can be implemented given pre-marriage or like shortly after the merge. I don't think we need like a hard for it to release these feature. So it could be a bit independent. 

**Danny**
* Yeah. I was going to say spec it as a V2 and not have it on the most critical path to get out in the merge. assuming rely is don't hose. You, we could also run, you know, some sort of century node to see if the reloads three layers are acting. If areas here and expedite V2, if needed. 

**lightcient**
* Sounds good. 

**Micah Zoltu**
* Currently on, if a CL is unable to reach the relayer today, will it correctly execute its own block, at least defended against that, 

**Danny**
* That that is allowed in this design.I hope that that's how the condenser being constructed. Like you should always build one in parallel, but you wouldn't be able to, once you get from the relay and once you get from local to know which one was more valuable, 

**terence(prysmaticlabs)**
* I was wondering if there's any sort of like, should we show you if I came out in inside him for life?So my recommendation, if you don't get a reply back within this time, you should just go with your own blog versus because it's pretty easy. If you get an error, if you get an error on that, if you just use your own Blackbaud that if they can sell them to respond like all of the wait for, 

**Danny**
* Yeah.I think it probably makes sense to add recommended On the order of what we're having in timeouts for like requesting a payload from your execution there, which is like one second. 

**Mikhail Kalinin**
* It should be a local request, right. To maybe boost, so it should be related to 

**Danny**
* Right.But MEV boost is making requests, external relay. It's making external request and then making a decision on which block is the most valuable and stuff. 

**Mikhail Kalinin**
* Yeah. And before it's like, we have this delivery from elders over P2P, like a delivery of payload theaters. Heather is in advance. Yeah. What kind of to expect that this will happen immediately, right? I mean that this request solver resolve to make you responded with header. 

**Danny**
* That's all I have for the builder API, information. We'll try and, cut a release for this, with the HTTP style sometime the next week. So keep an eye out. 
* Great. Thanks. Okay. other research spec or other discussion points for your day? 

## Research Spec or other discussion points [53.00](https://youtu.be/nnjeqZK7jgU?t=3179)

**Micah Zoltu**
* I would like to, I mean, we're out of time, but I would like to continue the IPV six discussion if possible, like in discord later, perhaps 

**Danny**
* We're not out of time.we can also continue that in discord, unless you have something in particular you want to talk about. 
* I just want to discuss it more or something like it, it seems like a legitimate problem. Like if there really are people that are running IPV six only I'm concerned that we could end up with a network partition pretty easily. If, if we don't have enough nodes that can speak both IPV six and NYPD four. So for example, if one, minority client implements, IPB six only support anyone else and everybody else's IPV four only, then that could very easily lead to a partition. 

**Micah Zoltu**
* Right. I believe IPV four support is a must in the phase  PP spec. in terms of the client needing to be able to be able to then implement it.Sure, sure. So the client can support it, but that doesn't mean user on some particular network has access IP before, right? It's like we're, if we were actually to the, in the future, living in the future where there exists people who only have IPV six access, the question becomes, do we want them, do we want to give them good guarantees that they will be able to connect to the network and stay connected? Or do we want to say, if you're on an IPP six you're on your own, you may get partitioned off and we don't care. 

**Danny**
* Yeah. I believe the specs written in a way that we do care.but the actual nuance of how this is coming out of production is Maybe 

**Micah Zoltu**
* It's a prep, perhaps a starter to the discussion that is just how many clients support IPV six, like just in their client today. 

**Age Manning**
* I mean, I think we can, you can set an IP V6, like listening address and kind of get TCP connections for discoveries or a whole other thing that way we're kind of currently working on. 

**Micah Zoltu**
* I see. So you have like, you have IPV six in the sense that like you're, you're the libraries you're using everything support at BB six, but currently discovery doesn't. Is that correct? 

**Age Manning**
* Yeah. So inherently with Lupita pay in tasty pay, you can, you can have an IB basics listening address, if they can set up TCB connections, but yeah. Discovering nodes, the way that ENS, so ENR is kind of divided. It can have an IP V6 port and an IP and a UDP, sorry. And then an IPV four port. And then I guess we have to decide where they're, you're gonna put them in your local route routing table and advertise them.And then if you have one that has both which, which Deconnect to, you have to kind of make these kinds of decisions, 

**Micah Zoltu**
* Any other comments of IPV, six support in some fashion, take that as just the one and which, which client is that age. Okay. do any other clients have plans on adding IPV six support? 

**Ben Edgington**
* I believe we have an intake, but it's not something that we actively, test or, or anyone is using as far as I know. 

**Danny**
* Yeah. I believe like go with P2P is going to have a lot of baseline support, but, it doesn't necessarily play nicely with how discoveries are working. 

**Micah Zoltu**
* So for the merge, is this something that we care about or are we okay at merge time, being kind of under the risk of it and network partition between V6 only and before only notes possible? 

**Age Manning**
* Yeah. I think weight wagon to try and avoid not releasing this kind of stuff before the merge. 

**Danny**
* Right. But I don't know why the point of the merge increases risk of partition here, age, the issues with discovery would exist on the existing preferred network as well. Right? 

**Age Manning**
* Yeah. I, I mainly just because the changes are quite involved, especially in discovery, so I kind of don't want to make any massive changes just before we, we do the merge. 

**Danny**
* Right. So status quo is not going to induce additional risk, give of how the network is structured today, but altering it might. So we should do it after the merge. 

**Age Manning**
* That's my thinking. Yes. 

**Danny**
* Got it. 

**Micah Zoltu**
* So he's probably let the people who are asking for it, know that at least just to set expectations, let's tell them, Hey, we're working on it, but well, you may be able to make something work in some clients. you also make it partitions. 

**Age Manning**
* Yeah, yeah, yeah. We will do. we're still trying to figure out the best way to make some of these, I know preferences, I guess, or biases in discovery before I tell everyone how it, how an IPV six only node would work on the network, whether it just it's gonna be that cell phone, whether it can like, you know, find some geo stack thing and, and connect. But yeah, we will inform the people that are asking. 

**Danny**
* Cool. Anything else people want to discuss today? Perry? Are we going to be doing another shadowfork for soon? 

**Pari**
* Yep. Next week. I would make some announcements tomorrow or today. 

**Danny**
* Okay. Well, in that case, we will close the call and take the rest of discussions in discord. Thanks everyone. Talk to y'all soon. 

**Tim Beiko**
* Thank you. Thanks. Bye. Bye. Bye 

----------------------------------------------------------------
## Attendance

- Danny
- Leo BSC
- Vitalik
- Grandine
- Paul Hauner
- Jacek Sieka
- Mamy
- Adrian Sutton
- Lion dappLion
- Patricio Worthalter
- Carl Beekhuizen
-  Lightclient
- Nishant
- Dankrad Feist
- Justin Drake
- Cayman Nava
- Mehdi Zerouali 
- Cem Ozer
- Terence
- Hsiao-wei wang
- Aditya Asgaonkar
- Alex Stokes
- Mikhail Kalinin
- Barnabe Monnot
- Zahary
- Pooja Ranjan
- Ansgar Dietrichs
- Proto Lambda
- Ben Edginton
- Leonardo Bautista
- Arnetheduck







