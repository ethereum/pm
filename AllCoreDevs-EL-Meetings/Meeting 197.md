# Ethereum Core Devs Meeting #197
### Meeting Date/Time: Sep 26, 2024, 14:00-15:30 UTC
### Meeting Duration: 1 hour 30 mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1153)
### [Video of the meeting](https://youtu.be/PWhn8KdgCl8)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | Video ref |
| ------------- | ------------------------------------------------------------------------ | ------------- |
| 197.1 | **Pectra Devnet 3 Updates**  EF Developer Operations Engineer Parithosh Jayanthi reported that a fix to a Teku-Erigon bug has been deployed to Pectra Devnet 3. He also said that further investigation is needed on a Lighthouse state root mismatch issue and an issue with increased block propagation times during an influx of pending validator deposits.On Monday, September 23, developers created 100,000 deposits on Devnet 3 to test the network’s capacity to handle influxes in deposit activity. A DevOps Engineer by the screen name “Philip” noted that the test led to “badly increased block propagation times” for unknown reasons. Teku developer Mikhail Kalinin is working on a change to consensus layer (CL) specifications to help address the issue. It remains unclear what the root cause of the issue is.
| 197.2 | **Pectra Devnet 3 Updates**  Jayanthi highlighted that his team is starting to plan the next Pectra devnet launch. He stated that the outstanding issues related to the MEV workflow should be addressed before the launch of Pectra Devnet 4 so that stakeholders in the MEV space, such as builders and relays, can start to test their operations on devnets. Jayanthi said aiming for the launch of Devnet 4 in two weeks would be a realistic goal for developers to target.
| 197.3 | **BLS MSM Benchmarks**  Beiko asked if client teams have had the opportunity to conduct their own benchmarking analysis on the BLS precompiles. Geth developer Jared Wasinger who had run the initial analysis reiterated that he is in favor of increasing the cost of these operations by 20%. Besu developer Gary Schulte said that his team had performed initial benchmarking tests on EIP 2537 and agreed that the precompiles are underpriced. Nethermind developer Marc Harvey also agreed with Wasinger’s proposal but added that his team has only completed a preliminary analysis, and further tests are still needed. Erigon developer Andrew Ashikhmin said that the benchmarking analysis completed by Wasinger should not differ greatly from any analysis done by Erigon given that the two software clients share the same code libraries and base implementation. A representative from the Reth team said that they have not yet had the time to investigate the matter of repricing EIP 2537.
| 197.4 | **Make Execution Requests a Sidecar**  For the last several ACD calls, developers have weighed different proposals to simplify EL-triggerable requests such as validator withdrawals and consolidations to the CL. This week, Kalinin shared an updated proposal that would generalize these requests on the EL and pass them through for parsing on the CL. The proposal garnered widespread support among developers on the call. Geth developer Felix Lange said, “I think it's a great … proposal because it means that we [the EL] have to care even less about the request. In my previous proposal, we still had to know about the output size of the contract objects in order to be able to split it into lists. So, this is now also removed from the EL. Basically, it's just even less knowledge about the contracts.
| 197.5 | **Make Execution Requests a Sidecar**  Other developers such as Prysm developer “Potuz”, Teku developer Enrico del Fante, Reth developer “Oliver”, Lodestar developer Gajinder Singh, Besu developer Daniel Lehrner, and Reth developer “Oliver” all supported the simplified approach proposed by Kalinin. Beiko and Jayanthi noted that this proposal would supersede prior proposals that had been made to simplify EL triggerable requests. Additionally, it would require updating aspects of EIP 6110, 7251, 7002, and 7685. Lange said that he would prioritize these updates over the next week and prepare them for implementation on Pectra Devnet 4.
| 197.6 | **Pectra Contract Audit RFP**  Beiko noted that the EF is seeking third-party security audits of the smart contracts used by three EIPs in Pectra. As stated in the announcement post, “The audit should focus exclusively on the smart contract bytecode, referenced in the EIPs below. It should not encompass all of the EIPs, or client implementations of the EIPs, including their interactions with the contracts.
| 197.7 | **Pectra Contract Audit RFP**  Bids for these audits should be emailed to rfp@ethereum.org with the subject line "Pectra System Contracts Bytecode Audit" by October 11, 2024. Additionally, the post states, “Proposals should include a summary of work to be performed, a timeline for completion of the audit, and a price for the engagement. … Accepted proposals will be confirmed by October 22, 2024 at the latest.”

**Tim**
* Okay. We're on. Welcome, everyone to ACDC number 197. basically two big things to chat about today. So first is LA live implementation Rotation and minor spec updates on the Pectra work. I think it makes sense to first go through this and make sure we're all on the same page around where things are at. And then next up, talking about the Pectra. the Pectra scope. So we discussed splitting the fork on the last call, as seems there was some rough consensus around, around the first half, but then a lot of open questions around what to do about the second half. many people and teams have shared their thoughts since then, so we can have a discussion around that. then a couple of minor things throughout as well. But those are the two big ones. first, I guess to kick us off, does anyone want to give an update on where things are with Devnet 3 right now? 

**Parithosh**
* Yeah, so we've had done actually three running for a bit now. And, there has been the Teku Aragon fix that's already been deployed and I think the tech team or the Aragon team was looking at, illegal state exception that's happening there. besides, that lighthouse has a state route mismatch. I've, it could potentially be a memory issue on the node, but, yeah, we still have to figure out what's going on there. besides those two points, there's one sort of deposit test that, Philip like PK has done from the team, and he's, written down some, some observations here. So please have a look. And I don't know, Philip, do you want to maybe say something about the deposit test? 

**PK**
* Yes, I do. so, yeah, we basically tried to fill up the pending, deposit queue on Pectra with 1000 pending deposits to see how the network behaves. And, we expected, increase of the epoch transition times because most clients need to, recompute the hashing times, 100, 100,000. And, yeah, that could already also be observed. But, more significantly, is that, who showed, quite badly increased block propagation time during these time frames. And, we are not sure where this is coming from, but, yeah, basically further investigation is needed to find out the root case here. 

**Parithosh**
* Yeah. Thanks. and Mikhail, already, I think posted, change in the consensus specs. That should potentially help with this. So we will be, like, redoing this analysis. once, once some PR is done or if there's some new proposal, Or rate limiting or whatever we choose. We definitely want to make sure that this is not happening before we, we start doing, I guess, more public events, etc.. even though that 100,000 deposits is a large number, especially because main net has like 1.1 million valid or 1 million validators, but still, it's a it's something we've observed for now. besides that, we've slowly started planning for Devnet for devnet for is essentially the same scope as Devnet three, along with a bunch of open APIs. ideally with everything related to builder, also with the MeV workflow also included. there's a bunch of open PRS as well as yeah, clarifications. So please have a look. And I guess we should first focus on merging those in and finishing the discussions. And ideally we'd have spec releases done after that. And we can point to the spec release for, for the devnet, timeline, at least in my head, is roughly two ish weeks. Unless that is unrealistic. 

**Tim**
* Thank you. yeah. Any of the client teams want to chime in on some of the issues we've seen on Devnet three or. yeah. Otherwise, it feels like it was pretty clear. and. Yeah. So there are a couple. Yeah, there are a couple, I think open PRS that people want to discuss on the call so we can, we can cover those as well. I guess one. So. Yeah. So we covered the big Q test. One other thing I think is important as we head to Devnet for is the BLS 12381, re-pricing. I don't know if, all the teams have had time to run the benchmarks and if someone's like looked into the results of that. But if we are to change the gas prices, we should try and do it by the next Devnet 2.

**Jared**
* So just speaking from benchmarking Geth, I would personally say that, increasing the cost 20% across the board would be the most aggressive that I could see the gas model still being, not heavily underpriced. so right now, that's what I would opt for. 

**Gary**
* From the Besu side. we've been doing a lot of, benchmarking with different library options, and it's a little bit difficult for us because, a lot of the kind of gas targets are based off kind of a relative performance of EC Recover. And that's one of the precompiles we've identified that we need to optimize. So I think something that's going to help us with giving a flat target for gas pricing is an agreed upon machine metric that we want to perform a specific, you know, mega gas per second for the BLS Precompiles, specifically the MSM Precompiles. Just initial benchmarking seems to agree that it is underpriced on what seems to be, somewhat agreed upon hardware like using a Gen11 nook and like an M1 arm machine. It seems to be that, our our initial benchmarking agrees with, Geth that it is underpriced. But getting a specific target is I think it's going to be better to have a specific machine target and mega gas per second, rather than kind of a relative performance metric for us. Okay. 

**Tim**
* Thanks. Anyone from Reth,Aragon or Nethermind.

**Marc**
* Yeah. For, Nethermind I think it was, Jared from Geth proposed potentially doubling the discount cost. And based on our initial tests with the, the state, tests, we would support that. because the MSM, particularly the G1 MSM, Precompile seems maybe underpriced. but we're seeing quite high variance between tests. so, yeah, we need to, look into this further and we're going to test out with our own benchmarking framework to verify the accuracy of the state test, benchmarks. 

**Tim**
* Thanks. Anyone from Aragon or attempted akin to this. 

**Andrew**
* Yeah. We are at a team offsite. So we kind of. We've been busy with that. but, for us, the results should be. Very close to those of Geth, because we use the same, library and pretty much the same implementation. 

**Tim**
* Okay. And on the red side. 

**Oliver**
* We did not have time to look at it, unfortunately. Yeah. 

**Tim**
* So I guess maybe one thing we could do to move this forward, especially if we want it for. Net four and that, we, we expect to ship net four in like, two weeks is. It seems like everyone agrees that these calls are underpriced. and at least another mind agrees that, like, you know, the the original proposal of doubling is probably directionally. right. So, Jared, would you be open to just could you open a PR against the IP, effectively proposing the doubling of the change of the gas costs, and then we can. Oh, sorry. Go ahead. 

**Jared**
* No. Sorry. Continue. 

**Tim**
* I was gonna say, if you can open the PR this way, we can track it as part of the net four spec. And then by next week on, even though it's the CL call, if we've had time to make tests on, like, more standardized hardwares, more standardized hardware and also get some numbers potentially from from rest. we can determine whether like those values are correct. But, yeah, assuming that this is all like the information we get, then we can just move forward with the the first proposed. yeah. Repricing. 

**Jared**
* Yeah, sure. That sounds good. Okay. 

**Tim**
* Thank you. Anything else on the BLS repricing? Okay. And then. Yeah. Let's, uh. Yeah, let's discuss this. actually, yeah. So there's a question in the chat about what's the hardware that we recommend? I don't know. Jared, do you have thoughts on this? 

**Jared**
* Not really. No. I, I know for several proposals in the past, we've just, I mean, the XP repricing comes to mind. We've used recover as a base, but I get that that's not that some people are against that. yeah. But no, I don't I don't like, have a, I can't, I don't have an opinion on what the specific hardware should be for a target right now. 

**Gary**
* I think, Merrick had made a recommendation, or like, kind of concurrence of recommendation of, like an Intel NUC, 11 as a baseline with a 50mbps target, 32 pairs. I think that would be like coming up with that as a as a standard would be pretty reasonable. And we're also seeing a. 

**Tim**
* Lot of different. 

**Gary**
* Architecture. 

**Marius**
* Where did the what is what is the what's the rationale for that. 

**Gary**
* For the for the nook as as rationale. I think that's just a common, solo staking rig as a, as a baseline. I don't think that there's going to be many, many, validator nodes out there that are running on, on hardware lesser than that. 

**Tim**
* Okay. And then there's some discussion in the chat about the version number. and yeah, we should probably test multiple, architectures. so I guess maybe. Yeah, the if, if teams have the capacity to, to test it against different architectures, and at least like report those tests, that would be good. I think the more data we can get, the better. but yeah, if we can prioritize this in the next week or so, that'd be really good, so that we can actually make a call for definite for, and not be changing the gas prices, forever. and yeah, I'll let people continue to debate in the chat exactly which nuke version to target. Anything else on the repricing? Okay. okay. Next up is something that, uh. Actually, Mikhail, is this something you wanted to be considered for? devnet. For your, PR about making the execution requests a sidecar? 

**Mikhail**
* Yeah, probably for the Devnet 4, but generally to gather the feedback. And if we want this, this design. So we need to do some more work on the APIs and smart contracts. Okay. And, yeah, actually, ideally, if we, if we want this, kind of design. Yeah. We would like to have it for net four if possible. Yeah. So, yeah. So the, I can briefly go over the, the proposed change. 

**Tim**
* I think that'd be good. Thank you. 

**Mikhail**
* Yeah, yeah. Okay. Cool. So this is, the slide or not? Yeah. It's just an improvement on upon the ideas that already, were, proposed previously by my client, and, some others, okay. So what what this PR, is, is doing actually is the it proposes the design, of the requests, that will be as less impactful for L and which allows to add new type of requests as smooth as possible. so the what exactly proposed is the the first step is to remove the requests from execution layer, beacon block body. and, entirely serve these requests as a sidecar. so we had this idea before, but now it makes more sense because, CL keeps those requests aside of the payload in the beginning block. and, for, you know, for, one of the concerns, of this approach was, the optimistic thing, safety. And to keep optimistic things safe, we will need to keep the request to have the commitment to the list of requests in the L block header. So which is which is fine. Which is perfectly fine. the other part of this, PR, emerged in the discussion with Lucas. so we want to, encode those requests, in a way that l, will not need to parse them at all. so the proposal is actually to, or the system smart contracts, to to return the list of list of requests in a way that they are ready to to be served to. To the CEO. So it's just basically, the modification that is required to. Achieve this goal is to prepare the type byte, before each request entry. 
* And do this in the smart contract implementation. So this is doable. And. I think it's it's not difficult to, to, to have to have this implemented. So then the, the l gets these requests, lists from, from each of the smart contract. concatenates them instead of using RLP. It just concatenates them in a list. This was proposed by Felix in the in the unified request objects PR to the engine. API to use this encoding. And this. This unified request list is used in two places. First, it's it is used in the engine API to surface the request to CL, as is. and the other part is that this exact list is used to, to compute this request hash commitment, which is put into the block header. And that's basically it. So adding a new request type would be a matter of implementing the smart contract. And just saying that this is a new request type to to L and L can handle it by some generic code. so that's that's about it. the design, yeah, it looks quite, quite good, to my opinion and yeah, that's it. And it would be great to get a feedback from CL devs and yeah, whether it's sound or how does it sound to to everyone and from CL as well. So CL will need to parse those requests from, from this kind of encoding and yeah. So that's it. Please take a look. And? If we decide to go, as I said, we need to change the system. Smart contract. We need to update these 7685 EIP, which is the generic request type. So that's that's kind of like the changes that are not done by this PR and just announced there. 
* I'm happy to to do this. Yeah. Cool. Alex. Thank you. 

**Tim**
* Thank you. 

**Mikhail**
* Sorry if it looks like client. Want to elaborate on this or, you know, just provide your comments. Please go ahead. 

**Felix**
* So I think it's a great one. the proposal, because it means that we have to care even less about the requests. In my previous proposal, we still had to, know about the output size of the contract objects in order to be able to split it into a list. So this is now also removed from the URL. Basically, it's just even less knowledge about the about the contracts. and yeah, like you mentioned in the PR, the deposit contract is a special one, but it's also kind of the the OG system contract. So I guess it's fine if we have to handle it a bit special as the only exception for now. And yeah. So I think my big question would just be like, if it has really been determined that it's fully safe, for the, for the sink because, yeah, with this design, I mean, basically the idea behind this design was also a little bit to make it so that we handle the requests in a similar way to how the receipts are actually handled. So the main motivation here is also that within the Ethereum block body like within the L block body. We do not actually have the receipts because the receipts are an output of the block computation. And so the receipts, the, the receipts are a separate entity. and then. so however the but we do have the receipts route and this is similar here. So the requests have the request route within the block body. So, I'm a bit curious how it's going to work during the sync, if we will be, if we will have to somehow sync the requests as a separate object or if they are fully like, if it's totally possible to just not have the requests at all within the L after the sync. 
* So technically we don't need them. They are only for the CL, so I guess it would be fine not to sync. Like during the snap swing for example, we would not sync think the requests, and therefore we would not be able to validate the request route. However, for the blocks which are provided by the CL, we would be able to verify the request route. 

**Mikhail**
* Yeah. So basically this uh request hash uh has has to it will be used in two places, into validations. First is the block hash validation. So the CL gives l the receipts the L computes the receipts hash. so the computation is encapsulated in L. How it's how it's done. It's completely up to you in this according to this proposal. and then, this, the obtained, receipts, sorry, request hash will be used to compute the block hash, and validate the block hash. So if the request passed from CL are not the one that are that the L is committed to the block, hash validation will fail. the other part, is the other validation happens, upon the block execution. So the requests obtained from the block execution will also need to be validated against this block commitment. And if. Yeah, if the block execution gives you, some different something different than that the block is committed to. So the execution of the block will fail. And these two validations actually, makes us safe, during the optimistic thing where L runs blocks on its own and, and it can validate the the requests obtained from the execution against the request hash. And the same is, is done by CL, right. So the the commitment is validated from both sides. So that's That's it. That's how it should. Should work. And snap sync. Of course. Now there is no kind of like, you know, these checks and. Yeah, it's fine. 

**Felix**
* So there's no need to download them during the snap sync. We basically just don't have to have the requests at all for the for the. Yeah yeah yeah okay. That's. Yeah. Exactly. Yeah I think so. 

**Potuz**
* Yeah. You're proposing so this this request, the sidecars are going to be gossiped on the CL side. And you're proposing this for the next devnet. 

**Felix**
* No, there's no gossiping of requests. so the thing is that the requests are purely created when the block is executed. it's just a mechanism for, for the, basically every node computes the request on their own because, the, the only way in which requests can be generated is via Transactions. So in fact, we are already gossiping the requests in a certain way. They are just encoded within the transaction. 

**Potuz**
* Oh I see. But then how will the CL get the request? Is this going to be on notify? New payload? 

**Felix**
* Yeah. Basically I will get it as an output from the CL. 

**Mikhail**
* Yeah CL will get it on the get payload but separately to the payload. This is why it is called the sidecar. 

**Potuz**
* No. Okay. So I'm still lost. So how will the CL sync a block over gossip? When I get the block over gossip, will I be. Will I have this request immediately or would I only get transactions? Send it to the L and then from there get back the requests? 

**Mikhail**
* No, but you will get those requests as a part of the beacon block. 

**Potuz**
* Oh, so that the the proposal will pack requests on the body as it is now. 

**Felix**
* Yeah

**Mikhail**
* Yes. 

**Felix**
* Yeah. The main problem that we are trying to address is that in the previous like another problem we're trying to address in the previous design is that the requests are duplicated. So in the previous design before the PR from Mikhail, the big problem was we had the we had the request in the block body. And we also had that in the CL block body. And I mean, technically it doesn't really matter because they can somehow be discarded or something, but it's just kind of a messy thing to have the same object with like slightly different semantics in the two blocks. And so with this new proposal, they are only in one place, which is the CL block body. And that's kind of where they have to be as well. 

**Potuz**
* Okay. And and this will be constructed one on get payload. It's going to come back from the engine. Yes. As separated from the payload. But uh okay. Perfect. This is the same as now on PBS. Okay. This is exactly as in PBS. So this is good. I like it. 

**Felix**
* It's like the. It's like the ultimate requests design. Like there's no no better one. 

**Parithosh**
* And something you want for the next minute or are we waiting for a few more weeks for people to comment on it before we ship it on a dev net? 

**Felix**
* I mean, I don't really know how. 

**Tim**
* People like it in the in the chat. I guess, does anyone have an objection to bringing it, bringing this in for the next net? Because if everyone is happy with it, then yeah, we should make the decision right now. And this way we can update the specs, update the contracts, update testing. but yeah. Does anyone have any concerns or objections with. 

**Mikhail**
* There might be some objections from KL, but I'm not sure. I mean that, yeah, they have to do more work, which is fair because KL is the consumer. I mean like have to do more work by just, you know, decoding this. 

**Potuz**
* But wait, what's what's the extra work here. I thought that on get payload we're going to get this request. We're going to just import them locally. what's the I mean. 

**Mikhail**
* Yeah, previously there were some discussion in the, there was some discussion in the PR, about like, encoding, particularly of the requests, so that the KL has to parse some, you know, some, some encoding that is not generic, like it's not entirely as it's as a Z, but it requires unions, you know, this this kind of discussion. 

**Potuz**
* Yeah. So that, that I think we have already like relented and and and accepted that we can we can do the parsing as long as there's a commitment of not using unions then in SSA. 

**Felix**
* Yeah. So this is one of the things in Michael's proposal that is going to be really interesting, because they now the requests are just going to be provided as a single byte array. And that has to be parsed by the CL. And I mean it's a it is. Let me just put it right. I think it's okay. But it's a custom format. So what we're talking about is basically it's like a byte array where you have these type containers and you have to keep checking for the first byte. Then you will know the size of the next object based on this type byte. And then you can basically take it out of the list. I think it's a it's a great design, honestly. It totally works. And it's the simplest possible way to send this information, but it definitely requires more parsing on the CL side than it ever did before. 

**Parithosh**
* And just one more clarification. This would supersede Lackland's PR to unify request objects as well as your PR to unified list of opaque requests. Right. So instead of doing those two, we would just do Mikhail's PR. 

**Felix**
* Yes, because in Mikhail's PR it's like we changed. It changes the same thing again to make it even simpler, basically. Thanks. 

**Tim**
* And to be clear, the PR that's superseded is this one I'm putting in the chat. Right. so this one we would just close. 

**Mikhail**
* Oh, this this one will need some, I don't know, maybe some changes, but yeah, we need something, you know. 

**Felix**
* Yeah, we need to update. 

**Tim**
* Oh, yeah. Sorry. Yeah, we need to update. 

**Felix**
* Yeah. All of the repos. So we have the, the the engine API and the EIP and the system contracts and they all need changes in some way. Okay. 

**Tim**
* So I guess it seems like everyone is in favor of moving towards this. there's no objections. It would be great if by next week's call, we could have, like, the final set of PRS. I mean, ideally merge. But if, you know, if not merged, at least like a clean set of final PRS across every single EIP, that and the engine API and whatnot that people can review. but yeah, hopefully we can do this async in the next week or so. yeah. Felix. Mikhail, can either of you take this on? 

**Parithosh**
* I left a note in the spec doc as needs updates for. I think there's three EIP that would need updating. Right? There's the, maxdb change request to flat encoding deposits and withdrawals. 

**Felix**
* Yeah. 

**Parithosh**
* And then I think there's one more, change request hash. That hash. 

**Felix**
* Yeah, we need to. Yeah. So the flat hash. I'm not actually. What is the commitment? Can you, sorry for dragging this out, but, Michael, what is the commitment? Is it the flat hash commitment, or is it the nodes? Yeah, it has to be. Right. Because it's just literally it's literally a hash of the whole. Yeah. Yeah. Okay. Yeah, it's fine by me. Okay. Yeah. So that one. So this flat hash thing then has to be changed a little bit to just basically specify that it's the hash of like the request hash is the hash over this over this output. And yeah. Anyway we will get this done. I will implement it in the contracts and. Yeah. 

**Tim**
* Awesome. Oliver. 

**Oliver**
* I seem to recall that right now we're gossiping the requests over P2P in the block bodies. Should we remove this in this case? 

**Mikhail**
* Sorry. What do you mean? So it's in the block body in the beacon block body. It still remains there, but not. It's removed from the execution layer. Body. 

**Oliver**
* Okay. Yeah, that was it. 

**Tim**
* Okay. Well. Thanks, Felix. Thanks, Mikhail. Anything else on this? Okay. And then, next up, so devnet 4 want to make sure that we cover all the other, open questions, so. Okay. So there was the PR 2611 ten. But this we need to change. then there were two PRs to 7702. Not allowing authorization non equals to to to the 64 minus one, and then adding a bunch of clarifications to align the spec with the tests. yeah. Does anyone have context on this or want to chat about them? Let me post them in the chat here. yeah. And it seems there was some conversation, on the PR right before the call. Okay. If no one wants to discuss it, we can move on. But, people should ideally, review this as we, as we finalize the scope for Devnet for, anything else that people feel is kind of urgent to discuss for devnet 4, and that we should get sorted out in the next week or so. 

**Parithosh**
* Yeah, I think the builder spec PR should get some last looks and get merged in so that people can start working on it. 

**Tim**
* Okay. Do you mind sharing it in the chat if you have it handy? 

**Parithosh**
* Yeah. Just it. 

**Tim**
* Thank you. Anything else on Devnet for that? We should be looking into before next week? Okay. Otherwise, yeah. So the two main things are, Mikhail's PR, which, Felix and him will follow up on, and then all of the BLS, repricing. so, hopefully we we get some agreement around benchmarks, but we'll at least have a PR open to change the gas costs by a factor of two, like we originally discussed. and then a bunch of other things that have been flagged in the Devnet four spec already. Anything else? Okay. And if not, yeah. One quick thing as well I'll give a shout for is we've put up an RFP to audit all of the contracts in, in spectra. so we have this open now where it'll be open until, October 11th. Hopefully by then the code is pretty much finalized, but we hope to get a bunch of different, people looking at the contract and, both fuzzing them, doing some static analysis and more. I'll post the link in the chat, but if, you are interested in listening, you can find us on the Ethereum request for proposals repo. And I think that covers everything around implementations. anything else before we move on to the, fork split? Okay. so fork split. So on last week's call, it seems like we had rough agreement on, at least the first half of Pectra. So moving from what, Devnet three was, into production? a bunch of teams shared some thoughts, this week. So Aragon, Aragon was, like, slightly opposed to the idea of, splitting the fork, partially because, one, it would just like, grow the second half of things, and potentially de-prioritize verkolje. 
* I think prism was in favor of a The fork keeping devnet. Three as the first half of Pectra, but then also opening the door for um. More changes in the second half, including potentially the sip. and one thing they were explicit about is not raising the blood count in the first half. Lodestar, wants to basically, keep the first half as a three as well. And then, basically has, like some proposals for the second half, some of which are not already included. never mind feels strongly about keeping the scope as is if we do the split, but it's also fine with keeping the fork in one piece. Then, Vitalik has a proposal, to actually add something to the first half, which is, a blob increase and a seven, six, two three to bound the block size, and then, rez, supports freezing both half both halves as is. so, yeah, there's a lot here. I guess one place to start is maybe, on the first half. So it seems like there's a lot of, support for freezing the first half of the fork. And that's roughly where we ended last call. but then, uh. Yeah, I think Vitalik and, sorry, I forget who was the other one who wanted something else in the first half. I think Vitalik might have been the only one who wants something added to the first half. Aside from the the base people who came on to argue for the blob increase last week. But. Yeah, maybe. Let's start here. if you're on the call, Vitalik, do you want to give the. 

**Vitalik**
* Yeah, yeah. I'm here. Okay. Yeah. I think, basically, a blob called, increase, I think is, something or a blob target increase is something that will be extremely valuable. And to me, the key stat basically is that if you look at the level of usage right now of blobs, that's like basically somewhere around 75% of the target. And I think it's, important to keep in mind, basically, that one big difference between the blob market and the like regular EVM market is that the blob market is made up of a much smaller number of larger actors. And so even though it feels like a nice and constant 75% like, I think it is undoubtedly true that there are layer two that are considered that would in prob would have used blobs if more, more space is available but are making the decision not to. Precisely because they know that if they come in, then they themselves are going to be enough to make blobs be again, no longer cheap for both themselves and for everyone else. so I think it's really important to think about, like some of those long term effects and generally the fact that the Ethereum ecosystem really has turned a corner to the point where layer two is including blob based, layer two is actually can offer people a, like sub $0.01, transaction fees. And this is, momentum that is extremely important to build on. And generally, the ecosystem, needs to scale. It is scaling and then needs to scale and wants to see, assurance, that it actually can scale. And this is, something where that that's the layer one is, committed to, going with going along with the one, and so my, so, so one, so this is, this to me is, an argument for, of, increasing the, blob target. 
* So the reason why I suggested, 76 to 3 along this is because, a lot of people's concerns around a blob, target increase have to do with a worst case, situations. And currently, the worst case, block size is about 2.7MB. that which is using, call data and 7.623 basically knocks that down to roughly one megabyte. And so if we do a blob, 76 two, three and simultaneously a blob surrogate Target increase and even some like two X is which is actually more than I advocated would still reduce the, the, the theoretical maximum block size by a factor of about a third. so yeah, basically view 7623 as, something which, which adds, a really valuable safety feature. another is and so that's, one of the other, suggestions. And then another question is, basically, are there are other ways to mitigate some mitigate the issue involving the, the problem with, like worst cases. And I think, there's two other options, right? One of them is, to basically do the IP that increases the min minimum blob base fee, which basically means that if we ever enter a free market condition, discovery condition, then the period of full blocks would be about three times shorter than it otherwise would be. so that's one option. And then another option is, actually to abandon the idea that there has to be A2X divergence between target and max and basically say, yeah, you know, either increase the target to four without increasing the max or increase the target to 4 or 5, but, increase the increase the max to 7 or 8, for example. 
* I mean, or. Yeah, I guess, more, more aggressively. Yeah. Ansgar suggests A69, right? Yes. Thank you both. EPA. Yeah. Seven seven, six two is the one that I had in mind there. So that would have the practical effect that if we have, if we enter a, one of these, like a blob of price discovery periods, then the it would like cut the maximum possible length of a period of of maximum usage by a factor of about of two thirds. So I think, I mean, the reason why we need to think about this is because like, if you just look realistically to me, it's just clear that a like just scaling, actual usage, usage is just incredibly important. And, you know, if Ethereum does not offer this, then like people will find it elsewhere and people are going to have, like insecure blockchain experiences that are just, not on Ethereum. Right. And the, and I would even argue that, like, even a 33% increase is probably more valuable than like even three of the factor apes at this point. So if you just like, look at, like the ratio of, effort to value, just like the amount of actual value here is, quite high in terms of, increasing the, increasing the amount of activity that can happen. and so I think there's, a lot of value in, doing a, sort of, target, increase and, at the same time as, thinking through, like adding like, seven, six, two, three. Yeah. in order to try to mitigate the effect of this, and, allow some of the other increases to be higher. 

**Tim**
* Okay. Thanks for sharing. There's been a lot of conversation in the chat. so I think there's, definitely one, thread, that the prism team raised last week as well around just like measuring the impact of this. another thread is that, basically the idea that, if we do, increase the blob count and we want seven, six, two, three and we maybe want the free market replacement and we maybe want seven, seven, four, two, now we're like at a four IP fork, effectively. that's like starting to be its own thing. but yeah, I guess maybe the strongest opposition seems to be from around, like, just the measurements of this. So maybe you want to share your thoughts there. 

**Potuz**
* Yeah. I'm just worried that even increasing the target but keeping the limit, which seems like reasonable and safe. But we we have not gotten any data about this. We haven't seen a single study that says how much it takes for nodes to actually be syncing, recovering from a long reorg. I mean, those are the things that will change because it's not bandwidth on the happy case, but bandwidth when you actually need to sync several blocks at a time at a time. And it would be nice to see if if this is actually safe. the measurements that we've seen are based on, on average bandwidth, which is certainly not what you need at the tip. it'd be good to see a serious study that proves that this is safe, and then we'll support it. But without data, it seems that we're just changing numbers because we we just came up with these numbers out of our head. 

**Vitalik**
* Yeah. I mean, I'd argue that honestly, we have had this study and this study is three working, like increasingly fine for nine months of operation, like a 33%, increases, within range of, gas limit increases that we've done in many times, many times on chain. And I think we also just, you know, I have to take Yeah. Like also take seriously the other side of the argument, right? Which is basically, yeah, all of the, risks, that, that come from, like gas prices going up to ten and 100 way again. Like we actually have to balance those considerations at some point. 

**Tim**
* I'm serious. 

**Marius**
* Yeah, but it's not really a 33% increase. It's it's more like a 66% increase because you're not like when we increase the limit. we're not only increasing, the limit on the consensus layer, but we're also increasing the average number of transactions of transactions that are sent to the network on the execution layer in the transaction. 

**Vitalik**
* Right. But that's right. But that's still a 33% increase on the total load, right? 

**Marius**
* Oh, yeah. 

**Vitalik**
* Yeah. 

**Marius**
* That's true. Yeah, yeah. 

**Tim**
* So I guess, yeah, I'd maybe be curious to hear if, like, other teams share kind of prism's view around the like measurement issues, like, or do other teams assuming like for a second like that. We didn't have all the other pectra scope issues, like is like, yeah. Do people generally want to see more measurement on, on on this or like, yeah. How how do we feel about increasing the block capacity? here we go. 

**Enrico**
* Yeah, we just want to share that we we have some discussion internally about this. And for instance, just just a data point to a couple of days ago, a guy showed up in our, discord, saying that he missed the block, and it was, was a homemaker, that fall back building locally. And he had to, his local El, selected six blocks, and then he ended up being reargued. the block has been reached in the network. Fine. But then the blobs was not able to reach on time and has been reordered. And then. And this this is a home stager, and he has not very big upload bandwidth, but still something that is concerning. Some of the long tail of homes that are not doesn't have enough bandwidth. And, so I think that the target increased to to four is kind of reasonable. But I also think that, some of the homes could have been impact also now. And what could be something like having a parameter on the execution layer for these guys that says, please, if you're if we are about to propose a block, please don't kind of limit the number of blobs that, the local yield will select just to accommodate their potential upload bandwidth. In that case, it could be an option that could be abused for sure. yeah. Thinking, I'm just putting my foot in. Yeah. My, my just asking if that could make sense. Something like that. To to go in the direction of helping those situations. 

**Tim**
* Thanks. we have Francis and then Ansgar. 

**Francis**
* Thanks, guys. I just want to mention one thing. Like we are always talking about some stickers with, like, low bandwidth. Cannot think, like, properly, but we haven't actually defined a minimum requirement about bandwidth like limit. Like, are we going to say that if they have only one megabytes per second upload link and we are going to tolerate that like forever? I guess like what I'm trying to say is that we probably need a better measurement or like better minimum spec for the network requirement so that we can talk about things like in more concrete manners, like not kind of like in like people's like reports about, okay, I have issues, but I don't know what your bandwidth and what I don't know what to expect, etc.. 

**Tim**
* Yeah. Like I think this would be good like the to do. We clearly don't have this today. And like if I were doing it, what I suggest is something like you look at around the world what is like some medium amount of bandwidth that you can get across different countries and what's like the share of countries that you want to cover with Ethereum. but yeah, I doubt we're going to get this today. 

**Francis**
* Actually, like one quick, information about that. I actually did a like kind of like quick search. so according to like those speed testing sites, the medium is about like 60 or 70MB per second upload Link. and like for the like maybe a long tail of things like for the two 200th country, it's around like 3 to 4MB per second of the link. so depends on, like, how we are thinking about, like, thinking in terms of like max, like burst speed that is needed for block propagation. It seems kind of like reasonable, like we within that range. But we definitely need, like, more concrete analysis of that. 

**Tim**
* Thanks. Yeah. Ansgar. 

**Ansgar**
* I just wanted to briefly say my proposal for what to do today would be that we, ideally agree on at least a target increase to for, um. I think the case for that. I mean, I said there's a little bit of pushback there on the call today as well, but I think we have relatively broad agreement on that. And specifically going from 3 to 4, a year later. Right. We ship for it for four at the beginning of this year. We'll ship that at the beginning of next year. I think the average global bandwidth increases by like 30% every year anyway. So like that's basically just keeping step with that. And given how strategically important it is, I think that would be a good baseline to agree on. And then maybe we just delay delay the decision on whether we go beyond that with also max increase on collecting a few some additional data. First, I think I personally would prefer to also do that then later on, but I see that there's a bit more resistance there. So maybe postpone that decision and just agree on the as a minimum basically that we will increase the target to for that, that I think would be very productive to do. 

**Tim**
* Yeah. I guess I'd be curious if this is something that there is broad agreement on. and then, you know, if again, trying to keep the scope of Pectra tight, like if this is something there is agreement on, like, is this the one thing we would change in Pectra if we could only change? And then there. There are some concerns around the homesteaders, and I don't know how we resolve those, but. Yeah, maybe. Like, I guess maybe one question is like, if Yeah, what would we want to know to, like, be confident that we could do this increase? yeah. I don't know if like anyone who has some concerns around just like the the current stickers like, what's yeah, what's the data that we'd want to see to be confident with this? 

**Lightclient**
* I mean, isn't there already a lot of data from homestakers saying the current load is too high? 

**Gary**
* Is that anecdotal data from folks that are bandwidth constrained, though? I mean, we're only going to hear from the squeaky wheels. 

**Lightclient**
* I'm just saying that we are already at capacity for some people, and increasing the target is going to put more people at capacity and beyond. So, like, I don't really know what data we can provide since there's already data saying that we're kicking people off the network or making it difficult for them to do their duties as a home validator. 

**Tim**
* And then, yeah, there's a yeah, there's a comment in the chat around, rolling out, I don't want to prod and that this will help with bandwidth, but, yeah, I don't know if anyone has more context on that. I want to share, like the timeline. yeah. Okay. Perry saying this would take months to roll out and analyze. yeah. 

**Lightclient**
* I mean, is it crazy to have a fork after what's already specified for Devnet 3, that's focused just on increasing the blob throughput and doing the preparations for PeerDAS Like, to me, that de-risks the situation of just making the current fork take even longer gives us more time to roll out. These improvements for the CL, networking gives us some time to improve the bandwidth consumption of the EL transaction pool for blobs, and still keeps us from getting into a situation where we bundle it with the full PeerDAS and EOF, or whatever else is in the next hard fork. That could take another one one and a half years. 

**Tim**
* Yeah, I guess it's worth having that conversation. I just want to make sure so we don't forget, the hands that were already up. So, like, POTUS is the POTUS, Ben and  Perry and then come back to this. Yeah. 

**Potuz**
* Yeah. So just a quick comment, a couple of quick comments. I kind of feel that there's a double standard here in that, the data that we have that our users are complaining about being reordered and losing blobs is anecdotal. but then on the other hand, the data that we have that the notes are safe with an increase. It's also mostly anecdotal. We don't have good metrics. and I would like this, these two sets of data to be put up to the same standards. And second, it seems to me that this change is just very minor. So it's easy to implement. It's just as much as when we were talking about changing the issuance curve, which was a one liner, it's one of these kind of things that we can actually measure. We can take some time to measure, and if we decide that it is safe, this is shipped in less than a day, so  I don't see how why would need to agree today on an increase when we have a lot of time to measure and make this change in less than just a few minutes on every client? 

**Tim**
* Thanks. Yeah. Ben. 

**Ben**
* Following up on, like, clients who have maybe three forks. just a comment that, you know, us could go in that second one. Probably. but I just wanted to say, with any, increase, increase in target blob limit, we should probably seriously consider 7762, which is the min fee. just so that the fee market isn't unpredictable. and there's been a research study on that, and they support it, for instance. 

**Tim**
* Thanks. 

**Ben**
* And again, it's a one line change. 

**Tim**
* Okay. That's you. Yeah. Pari. Max and Tony. 

**Parithosh**
* Yeah. I think I mostly agree with what, Potuz is saying. I don't necessarily think we have to agree today, but we have to agree that we intend to do this so we can collect the data required. I do think clients are anyway implementing. I don't want messages. There's going to be a reduction there. And we can analyze the reduction as well as figure out, for example, reorg rates for home speakers. we mostly know what validator indexes comply to Homestake IP addresses. and we can check the reorg rate for that and see how bad it is now. So then we eliminate the anecdotal part and we actually have raw facts in front of us. And then we can make a decision based on that. I guess the commitment now is then to figure out that is this stuff we want to spend time analyzing and doing, or is something else higher priority? 

**Tim**
* I think Max and Tony. 

**Max**
* Yeah. I just wanted to say on the data point, I do respect the desire for data driven decision making, and I think we already have a lot of data on this because of the fact that the fee market is sort of broken. We know that we've had periods of sustained, you know, high percentage of the gas or of the blob limit used. So we've had six blobs used for a long time, and we can use that data to support a move, which what Ansgar suggested would be 46, which is the same limit. And we've already had periods where we're operating near the limit for a long period of time. So I think we can go look at that data and make a decision based on that. I also think we should consider doing, 7762 as other sub mentioned, because much of the much of the disagreement about that was basically, oh, we're going to reach capacity soon and then this isn't going to matter. But of course, now we're increasing capacity again. We should expect to see more periods of price discovery happening. 

**Tim**
* Toni? 

**Toni**
* Yeah. I've just published, some analysis on the Rio. Great. a very recent analysis of how the whole situation played out. And it looked like, since we shipped for it for, for the reorg rate is basically trending down. So we are at a level, that is way better where we were, let's say a year ago, for example. And especially interesting is the fact that blocks with six blocks are not way more often, are not significantly more often reorg than, for example, a blob, a block with three blobs, or even one blob. So I think it's very hard nowadays to really attribute the re the fact of being reorg to the number of blobs. I think there are many more variables like the slot in index in an epoch. the fact if the previous um proposal is playing timing games and so on that have a way bigger impact on the, on the real grade nowadays than the number of blobs. So I would say, it looks like the network is definitely ready to, to have more blobs. I would be more concerned about the maximum L payload side size than the block size, just because it can be so variable. compared to blobs that are just a constant size increase. Just if you haven't seen it, I will also post the the most recent analysis that I just did today in the chat. And I think it's a good idea, like Perry said, to make it more granular to look into what our solo stake is doing, and also split between my boost users and Non-math boost users, because I think even that has a way bigger impact on the Rio grade than the number of blobs nowadays. 

**Tim**
* Thank you. Ahmad. Yeah, just. 

**Ahmad**
* Wanted to agree with the last two points, Tony said about solo stickers and the boost that no boost because, trending down, rewards does not mean that solo stickers are not struggling. It just means that, big operators are finding better ways to optimize against being rewarded and, like adjusting their timings of of posting the blocks, adjusting their timings to be exactly profitable and at the same time, not get reorged out. So, Yeah, I think that's mostly it. Not that Ben Cohen suddenly fixed the organ. but. Yeah. 

**Tim**
* Thanks.  Enrico. 

**Enrico**
* Yeah. It's exactly the same things from Ahmed. I do think that the improvement is just, infrastructure optimization rather than, uh. Yeah. Clients being more optimized for for sort of saying, actually what my, my example before was actually an example specifically for a home **Ben**hat fall back to local, local, product, local build. And if he had not fallen back and choose the builder, he probably wouldn't haven't been reordered out. So it's just, be more resilient, to, to maintain local building instead of just, Systematically give block production away. 

**Tim**
* Okay. I guess trying to summarize all of this and then, yeah, the past couple calls we spent discussing scoping, like, I think it's pretty clear that there's like a strong bias towards keeping the first half of spectra as close to three as possible. And then there's like, some desire to maybe increase, capacity in this fork, with a lot of caveats. and the work for that could be relatively small, but obviously not trivial. I think the four eEIP that sort of, are being discussed around this are, seven, six, two, three. So capping the call data, 7742, the assigning the block count only to the CL and Potentially 7760 with the fee. The minimum fee repricing. And then there's no IP for the blob count change but something around that. and then it seems also clear that like for the second half of Pectra, we have these two huge things, Pectra and EOF that are in progress that are not stable yet, like neither of their individual dev nets are stable, and we haven't even tried to put a dev net with the two together. So there's still a lot of work there. And as much as people say that we would want to keep the spec frozen there, it seems unrealistic that like nothing will come out in the next, you know, six months that we decide to include. so I think one way to move forward is we keep the scope of factor A as definite three. We keep these blob EIP, these four EIP I just mentioned, modulo, the one that doesn't exist yet to actually increase the blob count as CFO for Pectra. in the In the next few weeks. Slash months, depending on how long it takes. 
* We actually run the numbers on staking, and I think there's a broader conversation to have around that. Like, what numbers do we actually want? What does it look like? and then try to like, build the confidence around whether we think this is the right time to do it or not. If it turns out that we're all happy with the numbers, then we just include these relatively small changes alongside picture A and, you know, we shouldn't delay things too much and we get some increase in capacity. If we're unhappy with the numbers, we can debate what to do. Then. and then for spectra B, which I think we should just accept is effectively pusaka at this point, which is the next fork, we have EOF and PeerDAS, which we've already included in picture A, b the main things and we can CFI as much stuff as we want, but we, I think having the commitment B that we don't include new things until we're actually ready to implement them is probably the best gate gates because, you know, once we have EOF and pure dask relatively stable, then we'll have a big list of things that everyone thinks is extremely important and we can debate what to include from that. But at least we're not gradually adding more things as we haven't. While we haven't actually implemented EOF in pure DS. And I think in the world where like 763 and all the blob stuff doesn't make it to spectra A, we can decide to either move it to vector B or, you know, if we feel that it's so urgent, it needs its own fork in the middle, we can have that conversation, but that feels like the most practical way forward. 
* Yeah. And as much as I would like to, like, close the scope and say that we're going to commit to these things and not add anything else, I think it's just like an unrealistic thing to commit to. But I think we can commit to not making decisions about inclusions until we're actually ready to write more code. And this maximizes how long we have to actually think about different proposals. Um. Um. And can we commit to some set of facts that would not move out? So I would say yes, I would say EOF and pure Das, which are already included. so like my proposal is that picture B is EOF and pure Das, and we don't add anything else until both those two things work on dev nets, and we feel confident that we can actually add a bunch of other EIP. and I don't think that, like, we can make a decision today about whether we want some small blob increase fork in between picture A and B. I think if you know the situation changes a lot, we'll be able to make that call. It's relatively trivial to implement this like set of blob EIP, but we, uh. Yeah, I don't know that this is like something we should commit to today. but at least we get a scope for picture A that's relatively finalized. it's pretty clear that we prioritize looking into the blob increase, and then we keep EOF and pure Dask as the focus for picture B, and we don't do anything else until that fork until those two are done. But it's possible we add more stuff like, you know, prism was talking about seven, seven, three, two, for example, and stuff like that. **Tim**
* But we can have that discussion when we actually have EOF and implemented. 

**Tim**
* Any strong objections? and yeah, we call this a yes. Thanks, Trent. So like what I would do practically if we agree to this is I'll update the picture IP, I'll remove EOF and move those as included for Lusaka. I'll remove anything else that was CFI for spectra except 7623 and 7742. and I think we should add the max fee. The min fee, for the blobs increase. We don't have a PR yet for the blob in the actual blob increase, but we we can, add that when it's there. And then if anything else with CFI for, for Pusaka or spectra, we just moved that there. And the only two things included in Osaka would be, EOF and Dask for now. 

**Oliver**
* Okay. 

**Tim**
* Any objections? yeah. Guillaume. 

**Guillaume**
* Not an objection, per se. Just, clarification. what happens to whatever? Well, the only thing that was, that was, CFI for for Osaka so far. 

**Tim**
* Right. So I think, look, we can leave it in the Osaka. We can leave it as CFI for Osaka. Realistically, we're not going to do this all in the same fork if we want to open another. Yeah, if we want to open another meta EIP today for Amsterdam, like I can do that too. I think at this point I would almost wait until we're like farther along with Lusaka to open the Amsterdam EIP, but so, yeah. So yeah, Verkal should stay. I mean, I'm happy to open an Amsterdam meta EIP as well to, like, have it be clear. 

**Guillaume**
* Yeah, as you want. Just, uh. 

**Tim**
* Okay. Yeah, I think I think that's right. Yeah. 

**Guillaume**
* Don't drop it. 

**Tim**
* Yeah, yeah. Okay. Yeah. Makes sense. And I'll try. I don't know if the EIP bot will let me do this, but I'll try and do this all in a single PR so that it's all kind of clear in one place. But, I'll see if the EIP bot is Yeah. Let me push this through. Okay. Anything else on the fork scope? And there there was a comment in the chat around from Barnabas around like implementation estimates for the for blob EIP. so I think yeah, in the next couple of weeks it would be good to like think through both the data we want to see, but also the overhead of implementing these. And you know, we can make a call about the inclusion once once we know a bit better. But I think, for everyone who's like in favor of pushing this, we should yeah, now's the time to collect data and then also try to, like, look into reasons why this could be an issue. Okay. Anything else on Pectra?  

**Ben**
* Anyone implemented. 

**Marius**
* 7742 on. 

**Ben**
* The side by any chance? Because then we can already start doing some basic tests and seeing if we can start increasing the blob easily just from the side. But we would need at least one team to do this one and one team to do this. 

**Parithosh**
* I would hold off on that, at least for now, purely because there's enough changes for Devnet for maybe we can coordinate on this after, and by then we should have some more analysis data. 

**Tim**
* Thanks. and I know max who came on today as well, because you wanted to share some share some updates about 7762. I'm surprised we have the time to actually go into this, but, it seems like we do. So yeah. Do you want to give some updates on the conversation that happened on the about the EIP over the past couple of weeks? 

**Max**
* Yeah, I would just, like to plug a few things from data always basically gave a very thorough database investigation of what this would mean for prices. And I think the maximum increase this would cause to the average price per blob for the roll ups was, I believe 18% for, base going from like an average of $0.06 to an average of 72, which will very, cheap. And then also some of the roll ups have expressed support for this, whereas they would be the ones that are kind of potentially buy them including base expressed strong support for the proposal. So I added those to the eth magicians thread if anybody's interested in taking a look at those. Sorry, the eth magicians thread. 

**Tim**
* Thank you. And I just posted that data always analysis in the chat as well. anything else people want to chat about before we wrap up? Okay. Well. Oh, yeah. Makes sense. 

**Lightclient**
* Yeah. So what is the target for Pectra at this point? 

**Tim**
* So Devnet 3, we CFI these four blob related EIP or three EIP that exist, and then this hypothetical blob increase. We investigate all the blob stuff in the next few weeks. if Pectra that is ready to ship, you know, before that's, that's decided, then we ship this. At that point, we can have a conversation around whether we want a special small blob fork in between which we'll call for Osaka. We have EOF and Pectra included. We implement those. We don't add anything else until those two are implemented. We cfi a bunch of stuff in the coming months as it comes up. and then when we have a stable Devnet running both PeerDAS and EOF, then we decide what, if anything, we want to include alongside those in the fork. And then we also, yeah, draft the meta EIP for Amsterdam to highlight that Verkal is CFI for it. 

**Lightclient**
* Yeah. I think I'm asking more about what when are we trying to have a frozen spec for Pectra. And do like, do we have a target that we're working for right now? Because there's been some things thrown around even like forking early next year. And to do that, working backwards, it kind of means that we really need things frozen in November, and we need to start thinking about doing testnets in December. 

**Tim**
* So I think based on yeah. 

**Lightclient**
* Yeah. 

**Tim**
* Based on like the discussions we had around Devnet 4 today, it seems we need at least a couple weeks for Devnet 4 to go live. I think it would be ideal if by next I guess if by next ACDE we are launching Devnet 4, we should figure out whether this is the last step that we want to launch for Pectra or not. And this includes, you know, do we want to include all the blob stuff? 

**Lightclient**
* I'm pretty certain that we will have another devnet after Devnet 4. 

**Tim**
* Yeah. So this gives us I think this gives us roughly like a month to make the final decision around. Yeah. all the blob stuff. And then in parallel to this. yeah. Once we have the devnet, you know, devnet for find some bugs, fix them. You know, we start getting towards a spec freeze. and I think how quickly we can freeze the specs depends on how many bugs and issues we find. but, yeah, I would consider this. We don't quite have this Ethereum development, but I consider today, like, the feature freeze of Pectra and like, maybe we do this blob stuff, maybe we don't, but we don't consider anything else. And then, hopefully in the next month we get to a spec freeze. 

**Lightclient**
* Okay. So Devnet four is a good target before all core devs in two weeks to have that launched. 

**Tim**
* That would be great. 

**Lightclient**
* Or is that too optimistic Or can we do sooner? 

**Tim**
* Perry said we could do two weeks. 

**Lightclient**
* Yeah, I mean, that feels that feels like a good timeline because there is now still some changes that need to be made, given the removal of of the request from the L block and some updates to the engine API. 

**Tim**
* And then the gas prices for like kind of small, but gas prices for BLS and then a bunch of other small PRS. So yeah, I think two weeks is like realistic, but one week would feel very short. and obviously we can we can chat about this on next week's call, but I yeah, I mean for, for two weeks from now feels. Yeah. Feels good. 

**Lightclient**
* Okay. So let's try and get all of the spec changes merged by early next week. Definitely before all core devs next week. I think everything is open that we want to change about definite for. I don't think there's anything that's being discussed that doesn't have a have a PR yet. It's just a matter of putting them all into the specs and then hopefully the week after before we can launch. 

**Tim**
* Yeah, I think I like that. Devnet for specs by AC, DC and then devnet for live by AC, DC. 

**Lightclient**
* Cool. 

**Parithosh**
* And we also have one more avenue for discussion. Does the testing call on Monday. So if there's some PR that I don't know needs some more discussion, please raise it. And we can do this synchronously on Monday. So we have everything closed by next week. 

**Tim**
* Okay. Anything else before we wrap up? Great. Well yeah. Thanks everyone. And then five minutes early. That's the picture scoped. Timeline for definite for, um. Yeah. Appreciate everyone's participation. And we'll talk to you all very soon. 

**Andrew**
* Bye.


---------------------------------------

### Attendees
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

---------------------------------------






