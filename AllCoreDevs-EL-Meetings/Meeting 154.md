# Ethereum Core Devs Meeting #154
### Meeting Date/Time: February 2, 2023, 14:00 UTC
### Meeting Duration: 1 hour 30 mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/715)
### [Video of the meeting](https://youtu.be/E0w8NX5ksWo)
### Moderator: Tim Beiko
### Notes: Rory Arredondo

-------------------------------------------

## Action Items and Decision notes from [Tim Beiko](https://twitter.com/TimBeiko/status/1621209312050954240?s=20&t=Ym4ta2K9RrN6irzQakBwHQ)

## Intro
## [Shanghai Updates](https://github.com/ethereum/pm/issues/450#issuecomment-1242103736)
## [Zhejiang Testnet Launch](https://zhejiang.ethpandaops.io/)

**Tim Beiko** (2:50) -  Hi everyone. Welcome to All Core Devs 154. A couple of things to cover today. So some Shanghai updates as we had a new testnet launch earlier this week and then sort of talking about how we go from here to the existing public testnets and whether clients are ready to start looking at that. Then on the Cancun side, there was a lot of discussion around 4844 in the past week or two. So there's a few things that make sense to there's a few things that make sense to go over today. And I thought I had added this to the agenda. So there's three things there around the transactions with zero blobs, transaction pool spec blob/block coupling, and then there's something else. We've had some benchmarks done for the pre compiles so we can go over those as well. Then Matt had an execution API, PR has been open for a few weeks he wanted feedback on and to wrap up we've also been discussing SEZ, SSZ, sorry, quite a lot these past few weeks and there's a couple of proposals there. So maybe just the start. Anyone from the DevOps team want to give us an update on the new Shapella testnet?

**Barnabas Busa** (4:20) - Sure. Hi, everyone. So we launched the Zhejiang testnet yesterday at 3pm UTC time, and we have 61,000 active validators, 58,000 of them is run by the EF currently and our assessment is running 2000 more and we have another 1000 keys to get to different projects. They still have about 400 keys to give out if anyone has any client of team is interested just let me know. And we have fully working faucets and Beacon Chain and transaction explorers. So (inaudible) and Zhejiang both have a working explorer up and running. And we have a launch pad and all of this information can be found on the link I posted below. Currently, we are not able to process any new deposits because we have some trouble on loading new deposits into the Beacon Chain, but I'm sure it's gonna be sorted out in a few hours or days and we will have Shapella on Tuesday at 3pm UTC time.

**Tim Beiko** (5:47) - And then one question So you mentioned that you have about 400 validator keys. Is that the only way if somebody has a validator and they want to run through the transition?

**Barnabas Busa** (5:59) - No. So we'll have the launchpad and also so you will be able to get some 33 ETH at the faucet request and ensure that you can go through the launchpad exactly the same way as you would for any other testnet. 

**Tim Beiko** (6:18) - Awesome that's great. Anyone have questions? Comments?

**Marius Van Der Wijden** (6:28) - Can you quickly explain the issue is?

**Barnabas Busa** (6:34) - I I'm not really familiar with how new voting is taking place on the consensus layer, but maybe one of the CL client members can explain because we've been having some discussion in the Interop channel about this. Basically, we've been waiting for a long time to have some new deposits included but they just seemed to be more than they had except Lighthouse.

**Danny Ryan** (7:04) - So generally, there's a mechanism that some (inaudible) has since they're following the EL and vote on deposit route and process deposits. And this is definitely proven to be brittle, especially when we're configuring new networks from time to time. So I would suspect it's likely configuration given all these clients handle this final mainnet, but I don't have details beyond that.

**Tim Beiko** (7:44) - Anything else on the new testnet?

**Barnabas Busa** (7:56) - We had one (inaudible) question about whether BLS changes should be allowed or not (inaudible) All Core Devs. 

**Tim Beiko** (8:09) - Got it. Okay, um, then I guess, you know, I'd be curious to hear from some of the client teams how they feel about the general readiness of their Shapella code. And, you know, when it makes sense to potentially consider forking some of the existing public testnets so with Goerli or Sepolia and if you know people have preference around the the ordering of those two not that we have to like make a final decision today, but I think it just be good to like to put this in context where the different teams are at and how they'd like to approach the existing public testnets.

**Danny Ryan** (8:51) - Quickly on an ordering standpoint, I think it makes sense to do Sepolia before Goerli given that Goerli is used by much more validators outside of like, a limited set so that gives a bit more time for documentation and tooling to be more robust. So just from an ordering standpoint, that's my preference.

**Tim Beiko** (9:14) - Yeah, that would be mine as well. Does anyone disagree with that? Think that we should do Goerli first? Okay, so assuming we go Sepolia to Goerli, yeah, I'd be curious to hear yeah, from client teams, you know, is are you like close to a spot where you could put out a release to fork Sepolia? Not quite. Yeah. Any other concern about public testnets?

**Marek Moraczyński** (9:43) - So from Nethermind's side, we don't see any major issues. We have a few things to polish but I don't see any blockers now.

**Ben Edgington** (10:00) - Speaking of Teku we're good to go. No blockers.

**Tim Beiko** (10:04) - Awesome. 

**Gajinder** (10:06) - Same with Besu here. And agreement on Sepolia first. Lodestar is also good to go. 

**Tim Beiko** (10:17) - Okay.

**Gajinder** (10:19) - EthereumJS for customers. 

**Tim Beiko** (10:21) - Sorry, you said also EtheriumJS, is that right?

**Gajinder** (10:25) - EthereumJS, no testnet yet. 

**Tim Beiko** (10:27) - Okay.

**Gajinder** (10:29) - We are not on Mainnet.

**Terence** (10:32) - On the Prysm side we're also good to go. 

**Tim Beiko** (10:37) - Okay.

**Marius Van Der Wijden** (10:46) - Yes, I Geth is like, I'm pretty confident in our code. I'm like, I don't know having a testnet testnet breaking this close to two forking the testnets something that we should really look into. And I hope that from my point of view, it looks like a consensus layer problem. That would be really good to look into that. Otherwise, our our plan should be okay.

**Danny Ryan** (11:21) - So to be clear, this is that network has not gone through the Shapella upgrade. Is that correct?

**Barnabas Busa** (11:27) - That's correct. 

**Danny Ryan** (11:28) - Okay.

**Barnabas Busa** (11:28) - There's a config issue. Shapella is gonna happen Tuesday, next week. So um, if we can get everything up and running by Capella, I think it should be very good to go.

**Danny Ryan** (11:43) - Yea I'm gonna lean towards calling this a configuration issue and not a Shapella issue until proven otherwise. But agreed that we need to figure it out.

**Barnabas Busa** (11:51) - I would ask all client teams to try to give me a hand and try to figure out what kind of config issue that might be. Because at this point, I'm not really sure.

**Tim Beiko** (12:12) - Right, and obviously, you know, I think it would make sense to see Shapella work well on this testnet before we put out releases and set a specific date for for Sepolia yeah, but yeah, assuming it's just a config issue. Yeah, that that's obviously not the same as an issue with the actual fork transition.

**Barnabas Busa** (12:36) - I think next week, Thursday, we will have a much better oversight on like how things are going.

**Tim Beiko** (12:44) - That makes sense. I don't know if anyone from Erigon wants to share their view?

**Andrew Ashikhmin** (12:54) - I'm sorry. So what was the question?

**Tim Beiko** (12:57) - How ready are you guys for potentially forking Sepolia? Do you?

**Andrew Ashikhmin** (13:05) - Yea I think we are ready. That's just Shanghai, yeah?

**Tim Beiko** (13:08) - Yeah.

**Andrew Ashikhmin** (13:09) - Yes, I think for Shanghai, we have everything implemented. 

**Tim Beiko** (13:15) - Okay. By this year. So I think that's all the EL folks. And I think we're missing Lighthouse. I don't know if anyone's on the call?

**Adrian Manning** (13:25) - Yeah yeah, we're good as well. 

**Tim Beiko** (13:28) - Okay, and I'm missing one client. Anyone didn't go? Sorry? No, we got Besu. 

**Marek Moraczyński** (13:41) - Nimbus. 

**Tim Beiko** (13:42) - Nimbus Nimbus. Yes, yes. Thank you.

**Etan (Nimbus)** (13:45) - From what I've heard, everything is ready. Like feature wise, we are still doing some optimizations on ELS to execution changes. And I think that's it.

## [Cancun Updates](https://ethereum-magicians.org/t/cancun-network-upgrade-meta-thread/12060)

**Tim Beiko** (14:00) - Okay. So I guess um assuming that this this fork on the new testnet goes smoothly and we'll know that Tuesday, I think it would make sense on Thursday to agree to like a fork Epoch for Sepolia. And, and then if we get it out to, you know, like midweek the week after, it gives people sort of three four days to put out a release for Sepolia. And usually, you know, we can probably fork Sepolia like a week after that. Just to give folks some time to upgrade but it's a pretty small set of validators on the network. So I guess just yeah, from client teams, if if you can be ready to put out a release shortly after next week's consensus layer call, I think that would be that'd be great. Again, assuming we don't find anything going terribly wrong with this fork on on the new testnet. Does that make sense to people? Cool, um, and then yeah, I guess if you're a staker node operator, infrastructure provider listening, please, this is a time where you need to start paying attention. So we'll have a fork on Sepolia. You can join this new testnet if you if you want to try things before. I think once when Sepolia forks, we can start talking about talking about Goerli and how we want to handle that one. Anything else on testnets or Shapella generally? Okay, um, so, Cancun, lots of work has happened on 4844 in the past couple of weeks. There's a couple of things that sort of made sense to bubble up here. And maybe first I don't know if we're Radek is on to talk about the bench marks? Yea Radek?

**Jacek Glen** (16:16) - Hi Tim. That's actually me. 

**Tim Beiko** (16:19) - Okay. Sorry. 

**Jacek Glen** (16:20) - I will take for the benchmarks. Let me share the screen with you guys. First here we go. Can you see it? 

**Tim Beiko** (16:33) - Yes.

## [4844 gas costs benchmarking](https://github.com/imapp-pl/benchmarking/tree/precompiles_benchmark/shanghai)

**Jacek Glen** (16:35) - Okay. So, some time ago, we got this lovely little repo. The point of this repo was to track some benchmark data across different implementations and across different versions. So what was started off here. Let me just show here. Well, I'm not sure if you guys seen it or not, but let me just go quickly through it. So different click compiles and tracking to timestamp execution on the different machines here. Point of executing precompiles was actually to see if the gas cost of it is accurate. How how do we know if it's accurate? Well, we took or maybe let me show you the latest Shanghai version of it. No, not this one. Constantinople? Maybe. Yeah, I just wanted to show it to all the the results are normalised to one of the precompiles which is EC recover. EC recover being the most standard one and if we look here on the last column, this actually tells us what would be the cost of better precompiled execution if we normalise it to EC recover time, right. Maybe this is going to be more clearly we look at this world that we actually have. So the problem with the the current state of these people is that we only have Go Ethereum as a client, and we didn't lay track all the benches and all the precompiles and there's no way to compare them and that's exactly what we did here. So that's the selection of the precompiles that we decided to track executed them on this some reference machine being my laptop. It doesn't really matter what machine it is we all we want that is to compare the timings and the EC recover precompile is the basis and all the other precompiles are tested against the EC recover. So the first benchmark we've done is actually duplicating the one that was already done. And that's something we call the direct execution. So we take an appropriate method in Go Ethereum, executed in case of freedom This is a method called Run Precompiler contract. We executed measure the time using some benchmarking library. We we got this and we did it for most of the precompiles. Calculate the times or normalise them to EC recover and okay, let's take some examples here, Pairing 256 pairing time that the nominal costs so the current cost is 113000. And the calculated costs is 158 so close enough that's not too bad. The same for more so the nominal cost is 6000 calculated 6200. That's actually very good. The point of the main point of the exercise was actually to try to estimate the cost of the new point valuation precompile. So for the point evaluation, we have two failed tests and one valid test. So, this implementation all the all the precompiles for the point of valuation are valued at 50,000 at the moment. The failed test actually in this implementation, they complete quite quickly. And the calculated cost is 9000. The valid test is the 76,000. Right so now it's decision whether we need to change that nominal cost to adjust it to something for like 76 or or leave it as it is. But that was the first step with Go Ethereum. The second step was to say okay, this executions done in more direct direct way, what we want to do is to run them in in more real life scenario. So for all the precompiles, maybe I show you here for all the precompiles we've created simple contracts, which all they do is they push some parameters, known parameters and then call the precompile and execute bit bytecode and we benchmark the bytecode execution which is something (inaudible). So for the again, Go Ethereum case, let's take maybe Point Evaluation. So the direct ah that's a bad choice. Let me let me start with this one. The Pairing one the direct execution was maybe better give the better again bad choice because we have had multiple pairtings. EC Recover ah, that's the good one. The direct execution was 48 milliseconds on my machine. The bytecode execution was 70 milliseconds on my machine. The point evaluation, something similar I said it's a bad choice because for some reason, the bytecode execution was slightly faster on my machine than the direct execution execution. It's it's weird because it the bytecode execution we expect all the EVM machine overhead to be able to calculate it. But, you know, benchmarking is not the exact science just measuring some timings. Anyway, having the bytecode execution. Now we said, okay, the same bytecode we can execute against all other clients. And that's the (inaudible) time and that's exactly what we did. So we measured the same bytecodes against Nethermind, Erigon and Besu. And then, at the bottom of the page was a small comparison between clients for the Geth we also got a different implementation of point evaluation precompiled (inaudible). So well, we can compare it of course, it's not the kind of a competition between the clients it's more like to know what the gas cost estimation is is what we actually pay in terms of the computer resources. In here you have also this thing here the specification tells you exactly how it was executed and which version of clients we used. And that's it. Yeah.

**Tim Beiko** (25:21) - Thanks. Um, I guess do you maybe want to quickly go over the cross client comparison for the point evaluation precompile directly, and then then grab. Let's see. Yeah,

**Jacek Glen** (25:33) - Let's go here. So the top line is the actual timing. The bottom line is the gas calculated to gas cost for that specific client.

**Tim Beiko** (25:52) - Got it. Thanks. Dankrad. I see you've had your hand up for a while.

**Dankrad Feist** (26:00) - Sure. Yeah. I just wanted to comment that I don't know why we're doing this benchmarks with Go cases (inaudible)

**Tim Beiko** (26:16) - Yeah, we can definitely rerun the benchmarks with Gnark.

**Dankrad Feist** (26:21) - Probably like wasting time discussing these results.

**Tim Beiko** (26:28) - Yeah, that's definitely something that's doable. And we this is why we had like the the libraries using the specs, but now that we have the infrastructure, it's, I assume, pretty easy to just rerun it. Oh, it's already there actually with Geth. 

**Jacek Glen** (26:44) - For for the Gnark we have for the Geth. Yeah. 

**Tim Beiko** (26:47) - Nice. And um, any other questions? Thoughts? And I guess that the original kind of motivation to do this was to figure out whether the 50,000 gas price for the point evaluation precompile was reasonable. It does seem 

**Jacek Glen** (27:17) - That's correct. Yeah.

**Tim Beiko** (27:18) - Looking at it or looking at this as a non expert, it seems like none of those and none of the clients have like an execution time that that would imply a gas price of higher than 50k. Is that Is that correct?

**Jacek Glen** (27:31) - That's correct. Yeah.

**Tim Beiko** (27:32) - Yeah. Yeah. So I guess. Yeah, I, my takeaway would be that like, we've probably priced this correctly, but does anyone disagree? I'm looking at this. Okay, um, well, yeah. Thank you. For walking through this. The repo is obviously available so that I've linked it on the call agenda and shared in the chat here. If any client teams have like, small tweaks they'd like to see or whatnot, yeah, let me or Jacek know and we can we can look into getting those done.

**Jacek Glen** (28:13) - Okay, Cheers, guys.

## 4844 0-blobs transactions

**Tim Beiko** (28:14) - Yeah, thank you. Okay, next topic. Also 4844 stuff, so the zero blob transactions. So the idea here is, you know, should transaction 4844 transaction that does not contain blob data be valid? And basically should, if it's not, where should the sort of blocker be? Do we want this as a consensus rule? Do we just want clients to disallow those in the mempool? I know, Peter had originally kind of came up with a transaction pool spec that had some implications there. Then yeah, Ansgar, Dankrad, you both have some comments on the agenda, so Ansgar, how about you go first?

**Ansgar Dietrichs** (29:02) - So yeah, I think basically the concerns were that on the mempool side is pretty hard to have logic for zero blob transactions, because a couple assumptions that otherwise you can make with transactions are basically no longer valid. The question is just would we would we simply want to exclude them from mempools but still have them be valid in that case, they could still be included by a safe, a (inaudible) like system or not? I think there was some disagreement, my personal preference would be to still allow them on the consensus rule side and only ban them from mempools. But at the same time, I think just given that I think our priority is just to make compromises and get out of the door as soon as possible. I think there wouldn't be any big harm in restricting them on the consensus roots level as well. Now, we could always lift that ban later on. But yeah, I prefer to only do it on the mempool side if possible.

**Dankrad Feist** (30:06) - Pretty much agree with Ansgar on this. 

**Tim Beiko** (30:10) - Łucasz? Yeah. Oh sorry.

**Dankrad Feist** (30:14) - Yeah. No, no.

**Łukasz Rozmej** (30:16) - So from my side, I don't okay, but the potential problem is that we will have to have specialised logic if we will want to include them in case of reorgs which we now have. There's a question, do we want to keep the logic in in (inaudible) but we (inaudible) reorg transactions back to mempool. And then we have the we come to the same problem of having specialised cases in mempool. In my opinion, there is also a question mark on the general, like UX, user experience and usability because if we mark those transactions as logged transactions, they have in my opinion, special domain meaning and they are easier to reason about in all of the cases if they went to block if they only mempool, et cetera, et cetera, that they have blobs and they have special treatment because of this. And if we allow zero blob transaction, this reasoning is broken, and then you have to also inspect how many blobs they have in terms of the rules that was used for this transaction. So in my opinion, is just clear, makes the clear boundaries, what is what and that's why I'm for banning those kinds of transactions.

**Tim Beiko** (31:44) - Thanks. Vitalik?

**Vitalik Buterin** (31:47) - Yeah, one thing just worth mentioning is that this does kind of intersect that with the discussion that we're going to have later in the call on changing to SSZ because, like, my proposal, for example, does end up banning zero blob transactions as a side effect, but introducing a new transaction type for those. 

**Tim Beiko** (32:05) - Got it. Danny? 

**Danny Ryan** (32:10) - Just a quick comment on like the UX that we necessarily want to provide with the mempool. I think providing if someone's blob transaction was in the mempool, providing them with the faculty to have it be back in the mempool upon a reorg is probably reasonable UX, whereas I think if they bypass the mempool and are using special faculties and have zero blobs, or blobs and are seen in the mempool reorganising, and thus putting those back in the mempool it's kind of requires a number of like abstraction, breaking changes to the Engine API, and also seems like an extension of the like what we actually need to provide, you know, there's not necessarily because people are bypassing them in the first place, so I don't think we should design our systems to put them into the mempool in the case of there's a reorg. Nonetheless, I know that's not the direct comment, the direct point of what we're talking about here, but it was brought up peripherally. 

**Tim Beiko** (33:11) - Thanks. Łukasz?

**Łukasz Rozmej** (33:14) - So but then you have special cases right? Some of things, you know, put mempool some (inaudible) so it's, it's fine, right? But it's like, why? So if I can reverse the question and why zero blob transactions are helpful and useful because that's that's unclear for me? Why it would be good to have zero blob transactions?

**Tim Beiko** (33:35) - Dankrad?

**Dankrad Feist** (33:38) - So first, I mean, you will have special use cases anyway. Because you also don't want transaction with several blocks in the mempool. At least I think we should have them. And why do you need them? I don't think there's any strict case for needing them. But I also think there's a good reason to (inaudible) them. And it might simplify someone's logic say if like a rollup builds a pipeline that handles one type of transactions for everything. And maybe there are some cases where they just want to push a new state root and no blobs or something like that. So I can see I can't see a good reason not to happen, because everything just like it's simply a case of like executing everything was zero blobs. So my opinion is fine.

**Tim Beiko** (34:22) - But say just in your example of like the rollup infrastructure, I understand they might want to use the same address right like the same sign in key basically for those transactions. But why? Why couldn't they sign like a type two transaction instead of a type three transaction to do this?

**Dankrad Feist** (34:42) - Now that would mean they would also need infrastructure for LP transactions. And all that. So it is. I don't think this is a very strong argument. I also just don't personally see any argument for not allowing zero. 

**Tim Beiko** (34:58) - Got it. Vitalik?

**Vitalik Buterin** (35:02) - Yeah, just wanted to also point out that in the case where we do not end up accepting like either my proposals or some of the other more detailed proposals that include a new SSZ transaction type. We were if we get like if we don't include those and we also mandate that blob transactions have to have at least one blob that we lose an opportunity for regular users to kind of get acquainted and set up their infrastructure and start using SSZ transactions more quickly.

**Tim Beiko** (35:35) - Right. Yeah.

**Łukasz Rozmej** (35:39) - Yeah, my understanding is that we will go with with having another type of SSZ transaction so that's why one simplifies for the users right? It just specify different type and it's works mostly the same. Right.

## Transaction pool spec/test suite

**Tim Beiko** (35:58) - Okay, I guess I feel like it probably makes sense to have the SSZ discussion and then come back to this. Does anyone feel like we need to make a decision right now about this? Okay, so before, okay, so make sure to come back to this after SSZ. There were some more. There were just some more 4844 things before I think it makes sense to talk to talk about so, um, something that came up in the 4844 call this week is that with with the 0-blob transactions, obviously, you need to do some different logic in the transaction pool. And it was unclear what's the best way to test that or to have clients know that their implementation works in that like we obviously say that zero blob transactions are blocked at the consensus level, that's that's fine. You know, we can test for that but there will be like degrees of freedoms that clients can have to test a transaction pool and or to implement the transaction pool and is there like something like a test suite or something like that, that we'd want to have? To make sure that even though all the EL clients might have slightly different transaction pool implementations, they know that it meets like, whatever sort of requirements they should have. And this feels like a bit different than all the other testing infrastructure we've had before which is more focused on like consensus. So yeah, I don't there's any anyone feel like it's, there's value in having like a cross client thing for this or and if so, what do you think that would look like?

**Danny Ryan** (37:53) - This kind of thing is hard to test in a cross client manner, because there are it's very non deterministic as to like, it's very stateful for each client and what they're going to do. So I would, I don't know. There might be some like kind of testnet scenario stuff that we can do like, you know, in a given amount of time, under certain scenarios, transactions are included, thus the mempool must be working. But other than that, I don't think it's an easy thing to test in a deterministic way.

**Tim Beiko** (38:27) - Right, and maybe it's more a case of just having a setup where we can run you know, (inaudible) the transaction pools many times over, and almost more like fuzzing the transaction pools.

**Mikhail Kalinin** (38:43) - Quickly probably have a higher test on that because we can use Engine API and just the network appeal clients that are exchanged with these kinds of transactions and then after some time that we expect these transactions should be included in the payload which is the process to build the payload and check whether they are included or not. And probably this kind of approach could work. Yeah, but we need some strict rules that we can enforce this test, which may come out of the certification of this.

**Tim Beiko** (39:21) - Right, and, another option is to say like, you know, obviously, clients will have unit tests and like, we'll test their specific implementations. But, you know, maybe it's fine if there's like, discrepancies and behaviours. Yeah, it just feels like it is kind of something out of protocol, which we're adding some sort of design constraints on. And it would be good if there was a way to know that like the implementations roughly work, maybe shadow forks are sufficient for that. Yeah.

**Danny Ryan** (40:01) - It's also unclear to me how much of this document makes it into like a must on specification. Right? Some of this is just like the quality of service you want to provide to users and your various scenarios that traditionally hasn't really made it into specifications, so I'm hesitant to put it into joint testing.

**Tim Beiko** (40:20) - Okay, fair enough. Does anyone disagree with that?

**Danny Ryan** (40:23) - Some of that like the DOS considerations and other types of things clearly are put in the specs but like how to handle reorgs and stuff, but I don't know if there's precedent for having that sufficient.

**Mikhail Kalinin** (40:35) - At this approach definitely has its own restrictions. Yes. It also already, only could be tested up to like some limited extent.

**Tim Beiko** (41:02) - I mean, Marius to your comments about not accepting blobs, I guess. You could do just today with not accepting 1559 transactions as a client, right? You just provide like a worse product.

**Marius Van Der Wijden** (41:19) - Yes, yeah, but like this. If we were to not put it in, in the spec, and this would be something that clients could do. And I think there might actually be value in not having this not accepting blob transactions.

**Tim Beiko** (41:49) - Why? Obviously they still have to execute. Like they still have to process those transactions as part of the chain but you're saying like there would be value in them, not having to handle the mempool part of it, and you just can't submit your blob transactions without clients. Is that right? 

**Marius Van Der Wijden** (42:07) - Yes.

**Tim Beiko** (42:07) - Okay. Okay, um, yeah, I guess it doesn't seem like anyone is strongly in favour of having like some cross testing for that than that. It's fine. If if if there is some some differences in behaviour, so I think we can just leave it at that. Sorry, Łukasz?

**Łukasz Rozmej** (42:23) - I would potentially be in favour and I think if those transaction type and very special transaction type is in spec, mempool should generally handle them at least they should be able to, if they are not maybe explicitly configured not to. But I have no idea how to design this kind of test because all the mempool implementations are so different. And I have like no idea how to do that.

**Marius Van Der Wijden** (43:01) - So we have a few kind of a big suit of transaction pool unit tests. But they look very deeply into the transaction pool. So it's like we cannot really spin them out into something that that's available for our clients unfortunately. Like we I think we could but this will take a lot of work.

**Danny Ryan** (43:35) - Well, and it would probably take a lot of like, modifications on other clients to be able to have similar structures or similar formats or be able to ingest whatever you output.

**Marius Van Der Wijden** (43:45) - Yes, exactly. Well, ingesting isn't isn't really the problem. It's just it's (inaudible) transaction. The problem is more making sure that the rules are followed, and like verifying this state from the client, and like, getting the state back out of the client to see.

**Łukasz Rozmej** (44:15) - I think like the test could like even use test p2p right and the state to verify would be to produce block that it has those transactions, right that we expect them more or less to have.

**Marius Van Der Wijden** (44:32) - We could do that, but that would be even more complicated and more brittle.

**Łukasz Rozmej** (44:38) - Yeah, so like I said, it's quite hard to do that.


## [Blob/block coupling](https://hackmd.io/cmYisgxkRuGe9NjX4gr97A?view)

**Tim Beiko** (44:42) - Okay, so I feel like yeah, this is not like the most urgent thing we can discuss it I think if there's, yeah, there's test suites we want to come up with but yeah, I would assume that beyond just some basic like, test cases, a lot of the functionality will just be tested by the clients themselves for now. Anything else on this? Okay, the other big 4844 thing was blob and block coupling or decoupling in terms of sync. There was a lot of conversations about that as well. A couple comments on the agenda, Ansgar. Is this what you want to bring up? 

**Ansgar Dietrichs** (45:52) - Yeah, sure, sure, (inaudible) anything else?

**Tim Beiko** (45:54) - No, no, do you just want to give? Yes, I was asking if you want to give it just a quick background and then go into your comments?

**Ansgar Dietrichs** (46:06) - So basically, I think the idea is just that clients (inaudible) having the Consensus block in the blob section to one contiguous (inaudible) message, had some issues some inefficient inefficiencies and wanted to split it up. And as part of that, split up there are several different potential designs and in some of these versions, we would also do, like they just reconfirmed the fee and just given that the libraries are pretty, pretty close to kind of audit. So there's like urgency with any changes there. I think, and given some people are skeptical that whether we should do this change at all because this is something we should make a decision on soon. (inaudible), I just wanted to briefly say this from my perspective. I just basically classify the different types of (inaudible) we could do. So basically, there's one version where we only split blob section as one continuous chunk from from the rest of the consensus block. And in that case, we will not have to adjust accordingly. But also we only get some of the benefits because there will still be a pretty big chunk. One other (inaudible) the one that is proposed right now would be to split it on a per blob basis so we can each blob individually and there I think there would be a pretty strong desire to adjust be otherwise it's a bit silly to have a like subnet where you can download individual blobs, but then they come without individual proofs. So you can't really validate them. So you're that would indeed needs to (inaduible) adjustments. And then I think there's a third option that was discussed, that I personally am in favour of that would be to basically just treat the blob section as a opaque chunk of data and just by some, it's cut out. And in that case, the individual access to the to the blobs but you basically still get the (inaudible) benefits, and you could potentially extend that later on to the normal consensus, as well. And it would require changes to the cryptography. So basically, I wouldn't put today's call, we should just talk about, do we need this change at all? Again, responses CL teams strongly about and I think that's what people who can step it up and if we want to change which version do we want to go with and but mindful that some of these do requires (inaudible) changes and they are the timelines are pretty short.

**Tim Beiko** (48:31) - Got it. I guess. There were a couple of comments on the chat like from you and Ansgar about like, not necessarily separating them. Does anyone want to make the case for why we should split them out? And we can go from there.

**Danny Ryan** (48:47) - I'm pro splitting but I can make the anti splitting argument.

**Tim Beiko** (48:55) - I was gonna say do you want to start with the pro splitting?

**Danny Ryan** (48:58) - Okay, pro splitting. So essentially, by using separate subnets and separate meshes for these individual slice messages, we can probably leverage more efficiency across the network and essentially, more parallelization in propagation of these messages. This is, there's a lot of intuition around this that this is likely the case. There's especially given our understanding of how attestations other things work on rail network, but whether this is a 20% gain 80% gain in terms of propagation times, whether this helps in the normal mode or only in attack modes. Like there's not as clear exactly you know, the benefits that we're buying other than like a notion of this is a more resilient design. So there's a bit of work being done by Anton on TXRX to put this into a simulation framework as are couple of people looking into simulations on load analysis. So hopefully it gets an experimental analysis but I would say that after gossip did propose this seemed like the the networking experts like (inaudible) experts on the various teams were convinced by the arguments.

**Arnetheduck** (50:22) - I cannot do that. Hey, there's actually a bandwidth reduction as well. So there's what Danny mentioned the parallel sending, there's some parallel processing to do inside the client that is attractive with this proposal. And there's also bandwidth reduction due to technique I tend to call lazy sending, in which you simply don't have to send data to some clients thanks to a gossip sub trick and that trick becomes a lot more viable when the pieces of data are smaller, which is what we're doing here. We're basically taking the block and blobs and lining up the blobs each on their own subnets making them amenable to this kind of bandwidth reduction and what we've seen on attestations when we implemented this in Nimbus is like maybe 30% bandwidth reduction. So it sounds really attractive from from that point of view as well.

**Danny Ryan** (51:30) - And another argument here is that although at the current proposed amount of blobs and blobs sizes, sending fully might be sufficient for our propagation time, and bandwidth means that if over the next 18 months, we want to turn up that data gas limit that we're likely going to have to employ more sophisticated means, like this, maybe episode and other things, both to help propagation times, but also to help with bandwidth loads.

**George Kadianakis** (51:58) - So, to to get these benefits, how important is it that isolated blobs that fly on the network are verifiable in isolation, because that's what causes the cryptography layer changes the fact that now we are asked to be able to verify individual blobs whereas in the previous design the status quo we're only verifying all the blobs together with an aggregate proof.

**Danny Ryan** (52:34) - So, generally, the proposer signature, the proposer being a bound unit of one actor is sufficient for most of our baseline anti DOS measures, anything on top of that, that you verify that you can verify cheaply on each (inaudible) is good. It's nice to have, you know, for blocks, we don't execute everything but we do verify the proposal signature and then we do pretty much all the like constant time checks and say all the constant time checks are nice to have. It's really that proposer signature that's the core of our (inaudible). So again, that like crypto check if you can do it cheap. It's it is a nice to have, but I wouldn't say it's critical the signatures

**George Kadianakis** (53:19) - I see okay, because the one of the arguments during the presentation and they Interop was that you're able to like verify the blobs as they come so you basically paralyse the bandwith with the computation, but I guess that's.

**Danny Ryan** (53:35) - A potential argument there but I don't think it's the most critical

**George Kadianakis** (53:39) - Okay, I mean, in that case, I'm closing (inaudible) words no changes with cryptography and and just using the signatures for for authenticity and then doing the blob based creation up and (inaudible).

**Arnetheduck** (53:53) - I don't have a strong opinion either way. There's some minor performance benefits to having the blobs verifiable individually in terms of pipelining in the client, because now that you're receiving blobs you know at random times, it's good to get them verified as much work done on each blob individually as possible before you aggregate them. But it's not a strong opinion. The other one was that it was likely more easy to specify what the message should look like when they're individually proven because we don't really have any natural place to put the aggregate signature anymore. Like it's not like it could go in the block but then it has to stay in the block forever. And

**Danny Ryan** (54:54) - are you gonna send it with all

**Arnetheduck** (54:56) - Zero which is kind of ugly and you know,

**George Kadianakis** (54:58) - Interesting. You mean the proof? Yeah, that's a good point. Yeah, that's fine.

**Arnetheduck** (55:07) - Yeah, so I'm weak in favour of separate proofs weekly. But but I'm still in favour

**Tim Beiko** (55:15) - Vitalik, you've had your hand up for a bit.

**Vitalik Buterin** (55:18) - I also just wanted to make the brief points that splitting is probably more future compatible with more radical ways to verify blobs more official from down the line, such as erasure coding in the medium term and like actual data availability sampling in the long term. It just makes it so that any portion of the network would be able to do it passively on its own without interfering with the rest of the protocol.

**George Kadianakis** (55:42) - What's the erasure coding thing? 

**Vitalik Buterin** (55:45) - Oh, this is this is the thing where like, if if let's say a particular block has like seven blobs then you actually brought like you erasure extends them and you have 14 blobs and you broadcast the 14 blobs and then whenever you receive the first seven of them, you can immediately regenerate the other 14 and broadcast all of them. It's actually is similar to a technique that's been used by peer to peer networks in non blockchain contexts that and you know, it can increase the speed of propagation significantly, and probably also increase like (inaudible) efficiency because you have less redundancy or less overhead for the same redundancy in terms of safety.

**George Kadianakis** (56:27) - I see so it's not there 4844 thing it's 4844.5 thing.

**Vitalik Buterin** (56:33) - Right, exactly. The point is that like this style makes it more future compatible with doing that because that could be done without changing consensus or make really (inaudible) probably possibly even part of the network could do it without the other part.

**Tim Beiko** (56:51) - I'm just gonna get back to a comment in the chat as well. So Terence you asked whether we had a timeline for the simulation results, I don't know Mikhail if you have some thoughts on that. Okay. Maybe the next next week's call.

**Mikhail Kalinin** (57:08) - Yeah, that's that's probably will have like, clear understanding. Like that we have some progress towards the goal.

**Tim Beiko** (57:19) - Okay. And I guess one of the reasons why it was, you know, somewhat urgent to move this conversation forward is the audits of the of the crypto libraries and I believe just scheduled for about a month from now and so if we need to change how we view verification of the blobs, that's that's quite a short notice, and we should do it now. But I guess from this conversation, it seems like even if we didn't do individual verification of the blobs, we might still get some benefits out of this. So it probably makes sense to wait at least a week until we have the simulations results, but from the perspective of the KZG libraries, not not make any major changes now. Does that make sense to people?

**George Kadianakis** (58:06) - It does and we also got, we asked the auditing people about the potential to push the date forward and they said that it should be okay, but we should give them some heads up before so yeah, I think next week is that totally nice to have results in this?

**Tim Beiko** (58:30) - Okay, Mikhail, see how your hand up? Yeah.

**Mikhail Kalinin** (58:35) - Question Why? Why is the audit of crypto libraries? What depends on this decision?

**Tim Beiko** (58:44) - Because if we change blob verification to be for individual blobs rather than an aggregate, I believe that was the (inaudible) that requires changes.

**Mikhail Kalinin** (58:56) - So there is the kind of going to be a different verification function that will do in this case?

**George Kadianakis** (59:03) - Yeah, right now we're verifying all the blobs in aggregate to get some speed boost. Because we have them we get them all in one point. But with this new design, we would be getting blobs incrementally. So there is benefits to to be able to verify the blobs as they come.

**Mikhail Kalinin** (59:28) - Okay, see, probably we can chat about this.

## [Define eth_account execution-apis#329](https://github.com/ethereum/execution-apis/pull/329)

**Tim Beiko** (59:35) - Okay, yeah, let's let's do that. Let's bring this up on the on the CL call next week. Once we have also some more detail on the simulations. Anything else on on this? Okay, um, next step, Lightclient you've had this on the agenda for a couple of calls now. So wanted to make sure we got to it but it was adding a new ETH accounts endpoints. Do you want to quickly walk us through it?

**Lightclient** (1:00:13) - Yeah, sure. Just pretty quick. But Martin actually wrote a request into the execution API's repository in November to add this new method ETH getaccount. And the reason is we've had a few users requesting this type of functionality. Basically what it does is it takes in some address, and then returns the trie-leaf-definition of the accounts, which is the balance to store the nonce, the storage and the code hash if the account exists. I just sort of want to get a feel for if clients are okay to add something like this. We kind of want to make sure that we're moving the JSON RPC forward together in unison with all the clients so unless there's any strong feelings against it, then we can work on finalising the spec and merging it soon.

**Tim Beiko** (1:01:15) - Okay, any comments, thoughts? Does it make sense to give people just today and tomorrow to review this and we can merge with Monday if there's no new objections I saw Justin have left like a review yesterday. So like maybe giving people a couple of days from from here but yeah, Merging on Monday if if there's no issues?

**Justin Florentine** (1:01:43) - Yeah. Yeah, I was just gonna say Besu's pretty happy with it, honestly. 

**Lightclient** (1:01:53) - Is anyone from Erigon here? I feel like you guys tend to have different ideas about maybe with RPC would look like or maybe this could affect how you retrieve information. Does it seem okay to you?

**Andrew Ashikhmin** (1:02:08) - No, I think this is a simple method. It should be fine.

**Lightclient** (1:02:14) - Okay, sounds good. I'll give people until early next week, and then we'll get it merged and cut a release for the API's repo.

**Tim Beiko** (1:02:24) - Cool. Oh, yeah. Is this cause issues with verkle-tries? Is (inaudible) on the call?

**Vitalik Buterin** (1:02:36) - What's the what was the exact proposal again?

**Lightclient** (1:02:41) - It takes a request in which is the user's address and it returns whatever the trie-leaf definition is, which right now is balanced non storage root code hash. I don't know exactly how that would have changed. 

**Vitalik Buterin** (1:02:58) - Wait so what's the purpose?

**Lightclient** (1:03:03) - It just allows people to request the account information.

**Vitalik Buterin** (1:03:07) - Right I see like requests the header information. We have verkle-tries have a concept of a header so which is not super different. Rather, they like they don't necessarily have the same hash structure but they do have the concepts that like there is a field for the nonce. There's a field for the balance. There's a field for the code hash and so on.

**Lightclient** (1:03:34) - Okay, and as far as compatible, this doesn't have any hashes or (inaudible). It doesn't have any proofs or anything. So it shouldn't be agnostic.

**Tim Beiko** (1:03:41) - Łukasz, and then.

**Łukasz Rozmej** (1:03:45) - So other existing methods like that have this block parameter parameter that allows you to get the value not that the head is that considers here?

**Lightclient** (1:03:57) - Yeah sorry, that is that is here. It's the same format as for the other state retrieval methods. So it takes block tagged number hash.

**Łukasz Rozmej** (1:04:07) - Okay. I need to dig deeper because it wasn't a test on the PR conversation. It's not obvious maybe it's actual files. 

**Tim Beiko** (1:04:22) - Andrew?

**Andrew Ashikhmin** (1:04:23) - Yeah. I think that we in Erigon it's might be difficult or impossible to return storage root for historical snapshots so we don't stores we only have Merkle Patricia trie roots for the current state. We don't have historical roots.

**Lightclient** (1:04:54) - Yeah, I mean, we also don't have all the historical ones either, so I think they would just return an error like missing trie node or something.

**Andrew Ashikhmin** (1:05:07) - Yeah, we can return balance nonce and code as well, (inaudible) doesn't change however, but, unless it's recreated with grade two but we can simply omit storage root. If it's not the current state.

**Łukasz Rozmej** (1:05:30) - It could be marked as optional if it's not in the node, right.

**Lightclient** (1:05:37) - Yeah, it's possible. I think we should just take this conversation to the PR. But I think it's a possibility. Thanks.

## SSZ
## [Potential Transaction SSZ Refactor](https://notes.ethereum.org/@vbuterin/transaction_ssz_refactoring)
## [EIP-6404](https://github.com/ethereum/EIPs/pull/6404)

**Tim Beiko** (1:05:51) - Good. Yeah. So yeah, let's discuss it in the next couple of days. Ideally, we can merge it if yea there's no strong objections early next week. Okay, um, next, and last big topic for today is SSZ. Vitalik, you had a proposal and then Etan you have like, EIP that was in draft about this. So maybe it makes sense, Vitalik do you want to start and then Etan you can kind of walk through your EIP draft?

**Vitalik Buterin** (1:06:25) - Sure. So what motivated this whole research direction is basically the realisation that the kind of current EIP 4844 design puts the EIP 4844 transactions in this weird halfway house where they have SSZ serialisation but they but there is SSZ based but then they're assigning (inaudible) and their hash root are still based on a serialisation encoding. And like this seems like obviously not what we want in the far future, right? Because there is a goal of eventually moving things over to SSZ in some backwards compatible way and unifying things under one framework. And so the proposal that was that I had is basically like we're starting to think through like, how we can kind of tweak the current EIP in order to achieve that, but then a lot of people at our discussions in the research retreat last week, were of the opinion that is, it might actually be possible and even better to kind of do a more radical reform more quickly, basically, because this would reduce the total amount of work that we need to be done. And the radical reform. What it does is it basically does like three, maybe three quarters of the work of moving the transaction part of Ethereum over to SSZ, right and over to a pure version of SSZ so where the the TX ID of a transaction actually would be the hash trie of a transaction which is compatible with what the consensus layer does. And then the signing root of a transaction would be the hash trie root over the message part, which is also what the consensus layer does for blocks and attestations and all the other structures and so it introduces two new SSZ transaction types one which has a basically the existing 4844 blob transaction except the TX ID has a hash trie root and the signing hash is a hash trie root of the message part. And it introduces a second new transaction which is basically the same thing except it's allowed to have zero blobs. Right. So one of the things that people will seem generally more in favour of where instead of having one a new SSZ transaction type and allowing it to either have zero blobs or one or two blobs you have one type that is intact specifically for blobs and it must have at least one blob and then another which is which does not contain blobs, but that which allows you you to basically do everything purely with SSZ and rely purely on SSZ libraries and hash trie encoding and all of those things to create inside transactions. Now for the three existing Transaction Types, we so this is legacy, which based on the V value covers both kind of like legacy legacy and a chain id base EIP 155. It covers the EIP 2930, which added the access list and it covers the EIP 1559 which added the new gas gas pricing mechanics. For those three transaction types, it basically stores them in the block in an SSZ way. But at the same time, it's still be used like essentially can use as a pure function to convert the transaction from SSZ to RLP in order to compute both the signing hash and the TX ID. Right. So if I send an old style transaction, whichever one of those three types it is, then I could still use old RLP library or LP base libraries. I don't have to upgrade and I would send my transaction then when the transaction gets into the mempool. It would get selected into (inaudible) SSZ format it will get included in a block in the SSZ format and then when it gets that confirmation, has the TX ID I would still see the same kind of RLP constructed a TX ID that I'm used to and so like even as a DAP user I would not need to upgrade anything on chain or off chain in order to continue to be functional. So that's, that's basically it right? So defining five transaction types, three of which are basically legacy backwards compatibility wrappers and two of which are the 4844 type with blobs and the 4844 type without blobs, storing them in the SSZ in the block in SSZ and converting the transactions list in the execution payload away from being an opaque bytes object and into being a an actual SSZ list of SSZ objects. And then of course, creates these backwards compatibility functions of for older transaction types so people who use them can still continue using them the same way without changes

**Tim Beiko** (1:11:41) - Or comments on this?

**Łukasz Rozmej** (1:11:55) - So I'm very pro this proposal. I'm not entirely sure if I'm not missing something there but about this conversion, how it will work, but otherwise, if it does work as intended, it's like, silver bullet to have like both combative backwards compatibility as well as go forwards very quickly. So

**Vitalik Buterin** (1:12:21) - There is a the conversion function in both directions is a pure function and then I wrote a Python implementation that even has a test case to confirm that it works. It's in the it's in the documents linked in the EIP.

**Łukasz Rozmej** (1:12:36) - For example, like thinking on the practicality of storage, storage in retrieving those transactions, indexing them, like internally and because now we have like, SSZ and (inaudible) right to define them in some ways and like, Is there a problem there?

**Vitalik Buterin** (1:12:57) - I guess they could many index exit strategies are possible, right, including the very late very lazy one of like just adding a conversion to RLP layer before you have to do the to do the index step. Though it would require a new new SSZ based logic for the two and you so securely (inaudible).

**Łukasz Rozmej** (1:13:29) - Also like this conversion is like fairly intensive in terms of both my specially like CPU memory a bit right. So for example. 

**Vitalik Buterin** (1:13:38) - I would say it's not. 

**Łukasz Rozmej** (1:13:39) - Okay.

**Vitalik Buterin** (1:13:42) - You know, like it's basically like, I think in total, it's like less than 100. Just like it's a bit twiddling operations if you include all of the different things that are happening which is like way less than like even a single cryptographic thing. 

**Łukasz Rozmej** (1:14:00) - Okay.

**Andrew Ashikhmin** (1:14:08) - And does it mean that we have the same transaction root between CL and EL?

**Vitalik Buterin** (1:14:19) - I believe it does. Well, okay. There is one kind of nuance here, which is that if we want to (inaudible) support backwards compatibility, even for applications, which do Merkle groups that go into the historical stage where you like actually have Merkle verification in RLP then I proposed one modification, which basically include like keeps a transaction keeps an MPC transaction root that contains only the old the old sale transactions, and that's something that could could be deprecated an extra one or two versions in the in the future. But, like, aside from that, no, I think there's no reason to have different roots. Is that like they are both they do both become pure SSZ from any coding perspective.

**Andrew Ashikhmin** (1:15:14) - Because I think if we introduced this transitionary period where the two roots then it will be very difficult to get through to the second root and my preference would be not to introduce like as special transition periods and just switch to the CL root.

**Vitalik Buterin** (1:15:34) - That's understood the and I personally have no opposition to this, but that requires the kind of standard I think, you know, back backwards compatibility audit procedure of like, making an effort to go through which importance applications do use those kinds of mechanisms. And, you know, whether or not they can be, you know, we can make sure that they get upgraded fairly quickly. I think the one that might be the most the highest value, I believe, and I'm not sure if anyone from Optimism is on the call, but I believe it's the case that Bedrock which is their view, their newer version, it reduces gas costs for submitting a roll up by or for submitting a batch by allowing batches to be regular transactions and then in fraud proofs, allowing you to make a Merkle Patricia proof of the transaction. But like even that, like I guess, like number one Optimism is a highly capable team that's very involved in the discussions, including deals and number two, they're I think their fraud proofs technically haven't even turned on and they declared an intention to switch the blobs as soon as blobs become possible anyway. So that like that's the main case with significant amounts of value that I know about. But otherwise, I think, like we have been signalling for a long time that the data structures in the Ethereum blocks are going to change and people have had a lot of warning.

**Tim Beiko** (1:17:08) - Proto from Optimism is here so so you want to give some context of that?

**Protolambda** (1:17:14) - So like any roll up, you do have to be able to prove data is included in a transaction or receipt to really verify the (inaudible) so for all transaction data. So we prove that the transaction is indeed committed to this part of this try referenced in the block header that we do not strictly rely on the transaction hash partition try of lab thing that happens in Ethereum. We can just do the proof or not (inaudible)

**Vitalik Buterin** (1:17:51) - Right, but I think I think the issue is what if what what happens when a future and possibly near future version of Ethereum doesn't even have an MPT root. So it just has an SSZ root. And that would 

**Protolambda** (1:18:05) - Probably be better to be honest. If you're less error prone code. 

**Vitalik Buterin** (1:18:12) - Right? Okay. So less error prone code and just like you guys technically, have not taken off training wheels at all yet. So it's very possible for you to upgrade to like a code that handles dealing with blobs or with SSZ transactions.

**Protolambda** (1:18:28) - For rollups in general, I think we should consider the upgrades but at the same time a layer two does not upgrade at the exact same time as layer one for each layer two functionalities it's only really the the blob transition, a (inaudible) it's fine to change the (inaudible) even if, if you have the full proof or secret proof ready, you should be able to prepare the new version. And then based on your right you just deploy both. 

**Vitalik Buterin** (1:19:04) - Okay, any other I guess, questions, comments. I mean, I know I mean, Etan had his proposal but I put that kind of gets into the weeds of how things are serialised, which I'm not sure whether or not we want to necessarily get into into the next that's well now 12 minutes because it is a bit of a rabbit hole topic.

**Etan (Nimbus)** (1:19:31) - Not really. Main question is when we process 4844 transactions as part of a block, like not the block transactions that we have from the network that have to blob so the ones in the block they don't have the blobs anymore. And I was wondering, are we processing them in any different way still, like do we still care when processing blocks if if there were originally some blobs attached to a transaction or not? And if they are if they are processed the same, and we can actually make one normalised transaction type that we store as part of the block. And this essentially guarantees that anyone who wants to do proofs on transactions will be able to use stable generalised in (inaudible) for any field within a transaction. So for example, the transactions value, it would always be at the same index regardless if it's a block transaction or anything else.

**Tim Beiko** (1:20:40) - Lightclient?

**Lightclient** (1:20:45) - Yeah, just wanted to say I assume a lot of clients do this where they end up creating some sort of normalised transaction once they actually get into the transaction processing. But I do want to push back a little bit on using that as the rationale for creating the overall transaction object isn't like a normalised transaction. The reason being is that there's still a lot of processing that happens that's transaction specific, whether it's, you know, on the network level in the mempool or just setting up the state, the state processor, these things do need to exist, like we need to know how to hash different types of transactions that like the transaction still exist. And so I think that it's just much clearer to reason and think about these things whenever they're actually separated. And we can define all the methods in a more generic way rather than having to do it switching on types constantly.

**Etan (Nimbus)** (1:21:41) - You would still have to switch on a type, even if it's side by side, right? It's just that instead of having the type on the entire transaction, that type will just be a, something that's used for hashing because that's the only part where it matters, right? So so there will be a number that tells you hey, if it's three than it was originally hash like that. So for the purpose of signature verification and transaction ID I think that's the only part that cares about this. Yeah, I mean, it's the only change really that I had on top of the Vitalik's document is combine combine the different transaction types so that the proofs always have the same shape. There is also one concern I had with the hash trie root being the thing that's being signed because they can conflict with each other. For example, if we have this legacy transaction container in Vitalik's document and then we add another field to it, that can have a zero value that means something different on it being absent it will hash to the same root. So maybe we will still need for the signature purpose to add some version identifier that is not necessarily part of the SSZ trie.

**Lightclient** (1:23:23) - And to be clear, we can have proofs that go that you know have the same generalised index for each transaction element if we use a different Merkleization scheme like this onion format. And if we

**Etan (Nimbus)** (1:23:38) - If the onion format, different fields in the same field ends up at a different index.

**Lightclient** (1:23:50) - Okay, maybe I misunderstand but I don't think we should go into too much depth on that here.

**Tim Beiko** (1:23:58) - Yeah, I guess. What is the best next step for you know, just getting a general roadmap for a physique? I know we've been discussing this type transaction discord to make sense to just keep the conversation there. Is there anything else we should be doing beyond that in the next couple of weeks

**Lightclient** (1:24:29) - Some discussion about these changes to SSZ because I think they even the proposal that Etan came up with there is a new type of like container where you specify the maximum size of the container. And so this is a severe change.

**Tim Beiko** (1:24:48) - Does it make sense to like have separate call just for the SSZ stuff? I'm a bit hesitant given we have our parallel calls going on right now, but maybe that is the best way to make progress on it.

**Etan (Nimbus)** (1:25:04) - Probably yes, I mean, there is also other discussion like whether we can put the entire block in one go instead of this gradual process so that only the stage three would be the final Markle Patricia Tree. But yea a separate call is probably best.

## Block benchmarking

**Tim Beiko** (1:25:25) - Okay, so that's find the time it sees the type transaction channels to find the time to do this. And then yeah, we can we can sort of share updates on this, the CL call as we have a better spec. Anything else on the topic? Okay, if not the last thing, Marius you wanted to talk about block benchmarking?

**Marius Van Der Wijden** (1:25:56) - Yes. So in in Austria, Marek from the Nethermind team had a really good idea. And the idea was that we create bench blocks and and some kind of benchmarking infrastructure on the client so we can feed them these blocks and they will execute them, verify them and spit out the time that it took, took for them to execute. And so we kind of started a bit with the EF security and testing team. And these blocks will most likely not be publicly available, but I will provide them to all of the client teams directly so that we don't leak any weird information. Yeah, just as a heads up to everyone that you might receive a bunch of new blocks in the next couple of weeks.

**Tim Beiko** (1:27:13) - Sounds good? Many blocks by Marius. Łukasz?

**Łukasz Rozmej** (1:27:18) - I have few questions. So will there be some base status blocks will be executed on how it will be this from this like genesis block for first block after.

**Marius Van Der Wijden** (1:27:31) - Right now the ideas to base them on on Genesis. Just because it's easier. And we were like we would probably create a bunch of blocks so that we can set up state as we want to.

**Łukasz Rozmej** (1:27:48) - So what do we want to measure? Right because going through like the opcodes and executing the block, most of the time is accessing state right? At least for Nethermind. And this also is dependent on the storage model of the state that different clients are using. And I think we are working on optimising our one but it's not. So that's one of the thing.

**Marius Van Der Wijden** (1:28:20) - Yeah, state access is only like one part of the equation I think.

**Łukasz Rozmej** (1:28:26) - For example, providing Nethermind state access is like seven at least 70% of block processing time and this scales with how the big state is right, the bigger the state the longer the access. So if we have like a small genesis, what we can really measure correctly is only the actual opcodes time. State access being irrelevant, right?

**Marius Van Der Wijden** (1:28:55) - Kind of Yes. But yeah, that might there might be a future version where we start from a specific state but like setting this up is not as easy as just giving the clients a bunch of blocks.

**Łukasz Rozmej** (1:29:13) - Yeah, in state is big, right? So it's not easily Okay. Okay. Cool. It will be cool to have have this one. Will this be like really mixed blocks are like each blocks will focus on some on some opcode and we will just stress test to the clients based on this approach?

**Marius Van Der Wijden** (1:29:40) - I think it would start out with specific tests for specific things that we think might be might be very heavy,

**Łukasz Rozmej** (1:29:53) - Problematic. 

**Marius Van Der Wijden** (1:29:54) - Yes. 

**Łukasz Rozmej** (1:29:55) - Okay. Okay. Thank you. 

**Marius Van Der Wijden** (1:29:59) - Thanks. 

**Łukasz Rozmej** (1:30:00) - Cool.

**Tim Beiko** (1:30:01) - Anything else, as we wrap up? Okay, yeah, thanks, everyone. See y'all on the CL call next week. Oh, actually, Lightclient is there an EOF breakout next week? Are these still going on? 

**Lightclient** (1:30:21) - Yeah, it should be one Wednesday I think it is. 

**Tim Beiko** (1:30:24) - Okay. So yeah, Wednesday 15 UTC, there's an EOF breakout. And then there's the 4844 call on Tuesday 1530 UTC. CL call next Thursday at 14 UTC. And we'll see about

**Lightclient** (1:30:39) - Do we do we say we want to do an SSZ call too?

**Tim Beiko** (1:30:43) - We said yes. And I think the question is when we'd want to do it so we can talk about that on the discord. But yeah, looking at next week, it's already pretty, pretty packed.

**Lightclient** (1:30:55) - Yeah. Talk on the discord then.

**Tim Beiko** (1:31:00) - Thanks, everyone.


-----------------------------

### Attendees

* Pat Stiles
* Tim Beiko
* DB
* Enrico Del Fante
* Justin Florentine
* Marius Van Der Wijden
* Etan (Nimbus)
* Vitalik
* Gabriel Trintinalla
* Mikhail Kalinin
* Ken Ng
* Jacek Glen
* Ben Edgington
* Josh R
* Ansgar Dietrichs
* Crypdough.eth
* Rodia
* Barnabas Busa
* Adrian Manning
* Lightclient
* Kamil Chodoła
* Andrew Ashikhmin
* Rory Arredondo
* Dustin Brody
* Protolambda
* Alexey
* Danny Ryan
* Danno Ferrin
* Karim T.
* Soubhik Deb
* La Donna Higgins
* Amexiane Hamlat
* Guillaume
* Fabio Di Fabio
* Hsiao-Wei Wang
* Michael Huang
* Mario Vega
* Damian
* Roberto B
* Ayman
* Arnetheduck
* Marcin Sobczak
* Seananderson
* Oleg Jakushkin
* George Kadianakis
* Kasey Kirkham
* Dankrad Feist
* Pawan Dhananjay
* Stefan Bratanov
* Mofi
* Gajinder
* Matt Nelson
* Terence
* Marek Moraczyński
* carlbeek
* Caspar Schwarz-Schilling
* Daniel Lehrner
* Diego López León
* Francesco
* Gary Schulte
* Mark Peter
* Medi Aouadi
* Mike Kim
* Nazar
* Pooja Ranjan
* Potuz
* Radek
* wslyvh

-------------------------------------

## Next Meeting
February 16, 2023, 14:00 UTC
