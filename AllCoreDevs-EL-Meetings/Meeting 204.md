# Ethereum Core Devs Meeting #204
### Meeting Date/Time: Jan 30, 2025, 14:00-15:30 UTC
### Meeting Duration: 1 hour 30 mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1253)
### [Video of the meeting](https://youtu.be/JW2IWwVKRec)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | Video ref |
| ------------- | ------------------------------------------------------------------------ | ------------- |
| 204.1 | **Devnet 5 Updates**  A developer by the screen name “pk910” shared updates about Pectra Devnet 5. Though the devnet is finalizing again and the gas estimation bug shared on last week’s ACD call is now resolved among clients, it appears there is a new consensus bug impacting the Nethermind client. Senior software engineer at Nethermind Marek Moraczyński said the bug was caused due to a BLS precompile optimization in the Nethermind client. Moraczyński added that the bug should not be a blocker for the launch of Pectra Devnet 6 as a fix for it has already been implemented by his team.
| 204.2 | **Devnet 6 Updates**  On the topic of Pectra Devnet 6, Pk910 said a new hive release for Pectra is ready. Once most client teams pass the new hive tests, the EF Developer Operations team will launch Pectra Devnet 6. Pk910 said there is a pending change for Devnet 6 specifications impacting system contract addresses. The change will update all system contract addresses created through Pectra to be more recognizable and follow a pattern that highlights which EIP each specific system contract address relates to. Developers agreed to merge these changes on GitHub and finalize them for Devnet 6.
| 204.3 | **Testnet Fork Slot Proposals**  On the prior ACD call, Beiko shared tentative dates for upgrading public Ethereum testnets. Given that developers have not yet launched Pectra Devnet 6, Beiko asked if developers should update their initial timeline and when they would feel comfortable picking more specific times for upgrade activation. Prysm developer Terence Tsao said it was “premature” for developers to commit to specific times for public testnet activations. “Obviously, there are a lot more issues than we expected for Devnet 5 and those are actually consensus issues. They’re quite serious,” Tsao said. Agreeing with Tsao, Beiko said that developers should wait an additional week, until the launch of Devnet 6, before picking slot numbers for testnet upgrades.
| 204.4 | **A few potential slot numbers that were shared by Beiko before this week’s call include:**  Holesky: 3620864 (Wed, Feb 12 at 09:32:48 UTC), 3670016 (Wed, Feb 19 at 05:23:12 UTC), 3710976 (Mon, Feb 24 at 21:55:12)
| 204.5 | **A few potential slot numbers that were shared by Beiko before this week’s call include:**  Sepolia: 7020544 (Wed, Feb 19 at 15:48:48 UTC), 7061504 (Tue, Feb 25 at 08:20:48), 7118848 (Wed, Mar 5 at 07:29:36)
| 204.6 | **Geth Security Bug**  Geth developer Marius van der Wijden shared details about a bug in Geth. As background, Geth is the most widely run execution layer client in the Ethereum ecosystem. Van der Wijden said the bug impacts Ethereum’s peer to peer layer and Layer-2 rollups built on top of Ethereum. His team has since published a new release for Geth that fixes the issue. Nodes running a version of Geth that is 1.14 or later should update immediately to the newest version. Nodes running a version of Geth that is 1.13 are not affected.
| 204.7 | **Geth Security Bug**  When asked how this bug could impact nodes in a worst-case scenario, Van der Wijden said that the bug could enable malicious nodes to shut down other nodes or peers that it is connecting to. A Geth developer by the screen name “Felix” said in the Zoom chat that the bug is a “P2P DoS issue.”
| 204.8 | **Geth Security Bug**  Pectra Timeline Beiko encouraged client teams to focus on getting their client releases ready for the launch of Pectra Devnet 6. He also stressed that both EL and CL client teams should be present for next week’s ACD call where developers may decide on slot numbers for the public testnet upgrades, assuming Pectra Devnet 6 launch goes over well.
| 204.9 | **Geth Security Bug**  EF Researcher Ansgar Dietrichs asked in the Zoom chat if developers should also pick slot numbers for the Ethereum mainnet upgrade as early as next week. Beiko said, “I can look at possible mainnet fork slots for next week’s All Core Devs as well if people find that helpful. I do feel like this can backfire though because sometimes I’ll say this is the tentative mainnet fork block and then it will be tweeted, and people will just assume it’s that and they’ll be disappointed if it’s not.”
| 204.10 | **Pectra System Contracts Audits**  EF Security Research Lead Fredrik Svantes shared an overview of the process for auditing system contracts in the Pectra upgrade. As background, system contracts are smart contracts that extend the functionality of the Ethereum Virtual Machine (EVM). They create built-in functions such as ECDSA signature recovery or SHA-256 hashing that smart contract developers can access at specific addresses on Ethereum without having to deploy their own smart contracts to enable these widely used functions.
| 204.11 | **Pectra System Contracts Audits**  Pectra system contracts were audited by four security firms: Blackthorn, Dedaub, PlainShift, and Sigma Prime. Each audit was performed sequentially, meaning that fixes based on a previous report were integrated first before the next audit commenced. All audit reports have been published on GitHub. Representatives from each of the security firms shared a summary of their key findings on the ACD call.
| 204.12 | **Pectra Retrospective**  Last week, Beiko started an Ethereum Magicians thread sourcing feedback on the upgrade planning process. Beiko said that one of the key takeaways for implementation when planning the Fusaka upgrade should be that developers refrain from adding new EIPs into the upgrade scope until existing EIPs are implemented on a devnet. In the context of Fusaka, this means not including new EIPs into Fusaka until EOF and PeerDAS are implemented on a multi-client devnet. Beiko clarified that by “devnet”, he means a dedicated test network for the official upgrade, as opposed to a “feature” devnet, which may only be testing for one code change in isolation. Beiko also suggested further discussion on the upgrade planning process on the next ACDE call in two weeks.
| 204.13 | **Fusaka Planning**  As developers are getting close to finalizing Pectra and preparing it for mainnet activation, Beiko asked developers to start reviewing the EIPs proposed for inclusion in Fusaka. The two that developers have already agreed to include in Fusaka as a baseline for the upgrade are EOF and PeerDAS. Potuz asked if developers could schedule a Fusaka devnet featuring these two code changes on the call. However, Beiko, independent Ethereum developer Danno Ferrin, and EF DevOps Engineer Parithosh Jayanthi were in favor of focusing on Pectra Devnet 6 launch first. Jayanthi said in the Zoom chat that a new PeerDAS-only devnet should be ready to launch in a week or two.
| 204.14 | **Fusaka Planning**  Nethermind developer Marc Harvey Hill presented two EIPs for consideration in Fusaka, EIP 7793 and 7843. EIP 7793 proposed a new precompile that returns the index of the transaction being executed within the current block for the purposes of improving support for encrypted mempools. EIP 7843 proposes a new precompile that returns the corresponding slot number for the current block, which would also be useful for encrypted mempool applications. Hill requested feedback from application developers and protocol developers on the two EIPs.
| 204.15 | **Fusaka Planning**  Independent Ethereum developer Kevaundray Wedderburn presented EIP 7870 which formalized the hardware and bandwidth recommendations of Ethereum validating nodes and full nodes. Nixo, who is part of the EF Protocol Support Team, pushed back on the requirement of 50 Mbps upload bandwidth for local block builders. Potuz also voiced concerns about “max blobs flag” which would indicate when block builders do not have enough bandwidth to support building maximum size blocks. Due to limited time on the call, Beiko recommended taking the discussion to Discord.
| 204.16 | **ACD Call Bot and RPC Standards Breakout Meeting**  Nicolas Consigny, an employee at the EF, shared that he is working on a bot to help organize ACD calls and share summaries of the calls on different platforms. Consigny said that he will give a demo of the tool on a future ACD call but in short, the bot can automatically create GitHub entries for ACD meetings and cross-post meeting summaries onto platforms like Eth Magicians and Farcaster. He also mentioned the use of AI like granola.ai to create summaries of the meetings and in general , improve the efficiency of the calls.



**Tim**
* Okay. well, are we good? Okay. Awesome. welcome, everyone to ACDE 204. we have a fairly packed agenda today. So, first off, we can discuss what happened, on Devnet five, where we're at there. I know there were a couple bugs that came up, and then, plans for Devnet six related for that related to that story? I believe, people want to revisit the, forks slots that we had proposed, a couple of weeks ago. I think it'd be good to align on a schedule based on, where client teams are at, what they expect to be done, and when they expect to have releases. and then, there was a conversation as well on the chat this week around how long we want to wait after picking these testnet slots to pick a minute slot.
* And then two other things on the one, we have many of the auditors here who reviewed the system contracts for the fork. So we'll be going over the audit reports. And then, I think there was also a point around the system contract addresses that we needed to clarify. So figuring out what the final set of addresses will be for the testnet and, and then starting to look forward a bit, so there's this retrospective thread, that I wanted to follow up on. start to look at some stuff for the next fork. And then there were, two specific EIPs, if we have time that people wanted to bring up. So I guess to get us started, do we have, someone from Panda Ops to give an update on the nets? 

**PK910**
* Yep. Can give an update? Thanks. So the first good news is, devnet phase 5 is finalizing again after all the bug fixes from last week. thanks to all the client teams working on that. the bad news is, we have tried to run the execution spec tests again yesterday, and, Nethermind has a consensus bug and basically split out at Pacific Park. the team is aware they are fixing it. do they want to say anything to that? 

**Marek**
* Yes, it is fixed right now. and so that's the most important update. it was like, optimization combined with DLS Precompile that caused this issue. yeah. I think Nethermind was stable for months and break last night Devnet1. But yeah, it is generally fixed. So I think it shouldn't be a any blocker for devnet Six for sure. And for me as well. 

**PK910**
* Cool. can you send me the branch and I can deploy the images? 

**Marek**
* Yeah. So I'm running this image for already on some nodes, but, it would be good to update a few nodes. All nodes as well. So let me send you. 

**Ahmed**
* I already shared the image name on the telegram group. 

**PK910**
* All right. Thanks. the next thing is, we have the Devnet 6 hive up. please, also send branches to that so we can update, the image, the clients that are executed so we can have the latest results. we'll launch, definite six. as soon as most of the clients pass these tests, Mario will also release an East release. yeah, but we already have an early version to test on five, so please send in images. 

**Tim**
* Mario. 

**Mario**
* Yeah. One. One thing worth mentioning is that, there's a PR currently open in the repo. One for each of the, system contracts, and that's just to update the addresses to late last, update that's going to happen before, Prague launches. So I think we should get those merged and then, yeah. Please review. So then we can just, proceed and update yields, and then we can proceed and update east, and then we can, it should be fairly quickly. but yeah, just just just a heads up that the addresses are going to change in definite six if these Iprs go in. 

**Tim**
* Got it. Do you want to share the PRS in the chat when you have a chance? Um. Are these. And these latest addresses are like the nice ones with the number of the IP at the end? Correct. 

**Mario**
* Exactly. Yeah. Yeah. Okay. Open those, those PRS and these are the addresses that we are going to probably potentially going to use for, for mainnet. Yeah. Cool. 

**PK910**
* Thank you. Going to talk about that later on too. 

**Tim**
* So I mean yeah. Do you want to cover it now if we're talking about it's not a huge topic. Yeah. 

**PK910**
* Let me finish the update first. the last thing I want to mention is, I should remind the clients of the, BlockFi update and the genesis for note six. So that's the last update. Okay. so, regarding the, the contract addresses. we have generated a set of, nicer looking addresses starting with zero bytes and basically having the IP number as a suffix for the contract. It's now quite late in the release cycle as we plan to have releases on next Monday, but I guess it's a one line change hopefully for most clients. We've updated, we've opened PRS for them. So yeah, it's basically up to decide if we want to use the nicer looking addresses or if we stay on the not so nice ones. 

**Tim**
* I think given they're going to stay on chain forever, it's worth doing the change. and it is. It is kind of a nice, pattern if we can use it going forward for system contracts to have like, leading zeros, then, yeah, zeros at the end and the EIP number. Is there anyone for whom this would be like a significant change, or do you think that it would delay things? Yeah, let's just do it quickly. So I guess let's maybe leave the PR up today and then merge it tomorrow morning. Or do people want to merge it even quicker than that? It would be nice to have someone sanity check it, but. Okay, I'm hearing merge now. Anyone opposed? Anyone opposed to merging yet? Okay, let's get merged then. And yeah, Mario has a comment in the chat, which is that like, it's nice for smart contract writers to know that they're calling the right thing by looking at the EIP number?
* So I agree, this is like a neat feature. we should have thought about this a couple of weeks ago, but second best time is today. Anything else on the Devnet? 

**PK910**
* I think that's it for now. 

**Tim**
* And so then. And so, to be clear, Devnet six would then include all of these new addresses. Correct? 

**PK910**
* Yes. 

**Tim**
* Perfect. okay. So, last call or two calls ago, we had tentatively agreed to some, fork slots on Testnets. we were aiming to, fork hoski on February 12th, and then the week after on the 19th. and this meant having releases out by February 3rd. so meaning, this Monday or this coming Monday? we do not have them at six yet. And I know there were some concerns in the chat about, hitting the state. I guess I want to open up the conversation of one like, you know, should we pick a new time today? And if not, when should we pick it? I think, it's worst to pick a date and then not hit it. Then it is to just not pick a date if people are not ready. so. Yeah, open up the floor to this. Terence. 

**Terance**
* Does it make sense to pick a date like, after six, just to see how things went? Because obviously there are, like, a lot more issues than we expected for five, right? And those are actually consensus issues. They're quite serious. And even if you look at today, the participation for N95 is still not 100%. So I don't know. do you think it's slightly premature to pick test dates right now? 

**Tim**
* Yeah. I'm fine. I would rather wait. If we're not confident than pick one that we have to change. and then there's comments in the chat as well about the death issue. So I don't know. Marius, do you want to talk a bit about that? And if it affects the get timelines? 

**Marius**
* Yeah, I can talk about that. I can't really like it doesn't really impact the timeline too much. I cannot really, I cannot really talk about the timeline because I was, on sick leave. but, yeah, we had a pretty bad issue today. Or we fixed a pretty bad issue today. We made a release. it's a bug in the P2P that also affects some of the L2, but the L2 s have been, have been notified and they most of them have already put out a release, themselves. And yeah, just the general if you're running a gas, you should either downgrade to one to like a 113 release or upgrade to the latest release. because with the 114 release cycle, we introduced a bug and, um. Yeah, but as always, we we, we we would prefer if you updated to the newest release, or. Yeah, if you don't want to update, then don't update if you are, if you're running a version below one.
* Oh, yeah. Downgrading is not possible because we changed the database version. 

**Tim**
* Okay. So if you're running 114 you should upgrade. If you're not yet running 114, you should either keep your old version or upgrade to the latest release. 

**Roman**
* And if I may ask a question. if this bug is triggered, what? What would happen? Like, what is the worst case scenario? the 

**Marius**
* You can shut down nodes. like a peer can shut down the, the node that they're connecting with. 

**Tim**
* Okay. Okay, so I guess any question on any more questions on get before we go back to the test net? 

**Tim**
* Okay. Then. on the Hoseky. Yeah. Timing. So, with the rough plan, then be get definite six launched, which we can hopefully do, in the next few days. ideally, you know, if not by the Monday testing call, then shortly after that, assuming this works, then we feel confident to pick the the test network blocks. so I guess realistically this would mean picking them on, on next week's AC, DC. And then if, if that was, you know, if that went well, would people be ready to put out a release these days after ACDC, basically, so that, if we say pick the blocks on the sixth, which is next week, then by the 10th we have all the client releases and we can make an announcement on the 10th or 11th. Is this something that's, that people feel is possible? yeah. Justin. 

**Justin**
* So a point on that, we haven't had a great track record with making ACDC decisions on the ACDC call, so I am all for it. I actually think that's a great idea, but I think we should all commit to showing up and not put the ACDC call in a situation where they can't make a decision and they're waiting on us. That that has happened in the past, and I think that we can, try to make sure that everybody shows up there. 

**Tim**
* Yes, good call decision next week and your client is not there, we will ship the release and we'll have a TBD for your client's release in the blog post. yeah. And if you can't make the call for whatever reason, then just post a comment on the agenda with like your, you know, opinion. If it's yeah, if it's wrong. But my hope would be that in the next week we get that sorted. if if there's some issue we find on net six that we hadn't found before, obviously we should address and fix that. so I don't want to, like, assume that everything will go well, but, if it does, then by next week, we should be able to find, a work slot. and then we, um. Yeah. And then we pick it there. But my hope is that we could have fast turnarounds for the releases, after next week's call. So teams should expect to put out a release next, like, Friday or Monday or Monday after that.
* Does that seem reasonable? Okay. No objections. and I do think in general it would be good to have some representation from most teams on most calls. I know that it goes from like a call every two weeks to a call every week. but it's true that it is kind of annoying when you have to wait two weeks instead of one to make a decision. So, I don't think it happens super often, but as especially when we get close to shipping the fork. if yeah, it saves us a week, then we definitely should. yeah, we definitely should have people on both calls. so somewhat. I'm not sure I understand your question. 

**Somnath**
* Sorry, Tim. just wanted to make sure that that was up and running and, completely stable before taking a call on this line. 

**Tim**
* Yes. And I'm saying, can we do this by next Thursday? Ideally, we can get it up in the next few days, and then by Thursday it would be stable. Is this realistic or do people have a strong concern with that? 

**Marius**
* Could you please clarify whether it, moves the, testnet timestamps like provided W6 is stable? Will we still, might commit to the same timestamps or. 

**Tim**
* I would push them back. So yeah. So if we, if we forked next week or sorry if we chose the timestamps next week, I would push it back a week. so my, my proposal would be February 19th for me and then, February 25th for Sepolia. I have some timestamps in the agenda that are like, good times and that meet all the the epoch boundary criteria. yeah. Right. Like, yeah, but I'd rather not commit to those today. But I think if we if everything goes well in the next week, then I think pushing back the timeline we had by a week, would be my proposal. 

**Marius**
* And to, to clarify one more time, we're given these two weeks between we commit to, timestamps and potentially immediately do the release, to actual testnet, fork timestamps to, to give the ability for all of the people to upgrade. 

**Tim**
* Correct. Act. 

**Marius**
* This is two weeks a long time or so. 

**Tim**
* So in practice it's going to be closer to like ten days or a week or something. So if we have, you know, the say the last client release comes out on like the 10th, and then we have the blog post on like the 10th or the 11th or whatever. Then, the first work is on the 19th, so it's like a bit under a week. Historically, that's what we've done for testnet and then for main net, we've tried to had to have a bit more, delay because yeah, because we obviously want like all the main net operators to upgrade and it's, it's, it's worse if we, we don't have that many test nets. But I wouldn't feel super comfortable doing like a week or less unless there was a like a strong reason to do so. And I. And I do think so. And one last thing is like, I think it's kind of nice if the test nets fork before all core devs on those weeks.
* So like, you know, if we have the blog post, I'll say on the 11th. there's a core devs on the 13th. I don't think we'd want to do like a one day heads up before the fork. But then, I think it's quite important to have the test net fork before the core devs of the week after that so that we can actually see it fork and then, you know, make any adjustments. on the call. yeah. And then and the reason I guess, the I think the reason as well, is if we, we probably do want a week between the two test nets, because if something goes wrong with and we want to say have a fix for sepolia, then we can kind of do an emergency release between the two.
* So I wouldn't do wouldn't do like Cholesky and Cipolla quicker than this. Um. And. I guess, I don't know, maybe like a related topic to this is how long do people feel we should have between the test nets being set or forked and then picking the main net slot? So there was conversations on this as well on the discord. my sense from the discord is people wanted to see Holynski fork before picking a main net slot. So would assuming the Cholesky fork went well, would people want to pick the main net slot on like the all core devs after Cholesky? Even if Cipolla had not forked, so that we can give people, something like three weeks or so of heads up. So I guess. Yeah. Anyone opposed to picking a minute after we see one testnet fork? If the testnet goes well so that we can give people a bit more of a heads up. Okay. So the plan would be to summarize all of this, in the next week, get six up and running and stable.
* Assuming it's stable by next all core devs on February 6th. We confirmed the and slots on that call. Teams are expected to make a release on, the on the sixth, seventh or 10th. You know, on the 10th or the 11th. We have an announcement go out. Assuming we follow that timeline, we'd aim to fork on the week of the 19th on that week's awkward EVs. On the 20th, we would pick the main net fork time, and then on the week of the 24th, we would see a fork and assuming forks and doesn't have any issues, then we can start having client releases out and potentially announce, you know, have the fork announcement go out, on like the 27th or 28th if there aren't any issues. 
* And ideally, give people, a few weeks after that to upgrade. So, yeah, that would give us that would get us somewhere around like mid March or something for, for main net assuming we have no, yeah. No delays. Or any objections to this? Okay, so I think we can revisit this, next week, but, so client teams, just please, get the hive test passing. let's try to get them to six working, and, we can agree on the four slots, next week. and then one last thing to. Would it not be useful to have a preliminary timeline by next week? So, I mean, I guess what more do you want in terms of preliminary timeline than I can like, I can look at the main net possible main net four slots for next week as well if people find that helpful. I do like this can backfire though, because sometimes I'll say like this is the tentative main net block work block and then it will be tweeted and people will just assume it's that and they'll be disappointed if it's not.
* So I Yeah. I don't know. I don't have a strong opinion there, but there is kind of a downside of, like, having a tentative, um. Yeah. Anyways, we can discuss that, I think. so we had several people do audits of the system contracts. Frederick can give a quick overview of, like, the entire process. And we have a few of the auditors on as well that can share, that can share their findings. Frederick. 

**Fedrik**
* Yeah. So we did the audits, like, Tim was mentioning, we had, four different, auditing firms looking at this, Blackthorn Dao, Planeshift and Sigma Prime. And, they did the audits sequentially. So we started with, Blackthorn, and, after that one was completed and we had implemented whatever fixes that we felt was, important to implement. we went went forward with the next one. So this was done during the whole process. so that means that the, the findings are, are different. given that they looked at different code bases and, or different commits, rather. And at the same time, we also had, John from A16z who, did a formal verification on the, these contracts, using Hellmuth. So we have all the reports available publicly in a GitHub repo. That I shared. Now. if you look there, you can find all the reports. And, we have at least some of the, I hope all of them, but we'll see. auditors to give a very brief presentation about the report. I'm thinking, like 1 to 2 minutes per, per auditor.
* And, yeah, I'm thinking that we we start in the order that, the, the audits were done. So is there anyone from Blackthorn who is here? 

**Marius**
* Yep. Frederick. Okay, cool. Yeah. 

**Artemy**
* I think that we can start, just to quickly. Quick intro from our side. I'm Artemis from Sherlock and Blackthorn. We also have Wagner here who will go through, you know, our findings. I think we were one of the first, audits on the system contract. And the Blackthorn is kind of like our different brand, from Sherlock. And. Yeah, I'll let Wagner to quickly go through the all the all the issues and the findings that we had. 

**Vagner**
* Yeah. Thank you. Artemis. so we conducted an audit with four auditors for the implementation of, especially the AP7002 and 7251. because of the experience needed, you know, the things were pretty specialized. So we needed to find people with a low level coding experience and people who can audit, specification implementation especially. So in our report, we had two low severity findings. The first one would be a semantic finding, which is more like a recommendation, basically to update the counter semantic that will optimize the guest usage when it comes to consolidation and withdrawals. which as I said, it was more like a recommendation. But considering the fact that, the current guest semantics will not always hold true, you know, and the fact that the complexity of the contracts could change. This is not, something that, is expected to to be purposed in the future. And another issue, the second low severity issue that was found was regarding an overflow that could happen in the fake expo.
* That could lead to a mismatch when it comes to specification implementation.
* But again, this is more specific specifically to the Python specification. And in important note that like the reason that, why it was a low severity finding is that in the current setup, in the current settings, it is pretty much impossible to reach that value. But in the possible, you know, in the future, assuming, you know, heavy scalability especially, it could be, possible for, the access to be bigger than, 2892. So because of the fact that in the current settings it is impossible. It's again, it is a low severity issue. but it's important to keep that in mind also for future references. **Vagner**
* So yeah, that was, basically the two findings and the report from, Blackthorn. 

**Fedrik**
* Thank you very much. do we have anyone from Dido here? 

**Sifis Lagouvardos**
* Yes. I'm here. so should I make a small presentation? Should I say or do you think it will delay the thing? 

**Tim**
* Go ahead if you can. Yeah, go to it fairly quickly, but, yeah, I think you can share. And then maybe put the slides in the chat after. 

**Artemy**
* Yeah. 

**Sifis Lagouvardos**
* Okay. Yes. One second. Can you see my screen? 

**Tim**
* Yes. 

**Sifis Lagouvardos**
* Okay. So, since I worked on this, along with my coworker Tony Valentine, who's also on the call, we did the three system contracts. Now I'll speak briefly about the methodology we used. So the two of us audit the contracts for two weeks. And because it was a really low level code audit, we looked at the code at different abstraction levels, bit the source, the EVM bytecode directly. They recovered the decompiled source by the compiler and the three address code of our binary lifter as well. And along with the report, we have some annotated control flow graph and the compilation outputs which you can find. So for the EIP 2935 was the simplest of the three. So I'll not mention much. We only found the discrepancy between spec and implementation regarding the ring buffer size, which has been addressed. now the other two APIs are more important, and they share a common architecture of like a message queue and. Yeah. And so the basically the messages are added, requests are added to the end of the queue. And once that is blocked a system call is performed to remove some of these requests.
* And a request is um is required in order to add a new request. And that request fee is based on the number of access requests. Now, I will, go over some of these things because we have a little time, but basically we identified three issues. And the one, the most important one was a medium severity denial of service vulnerability. And, three advisory issues which are not mentioned. You can go through the report to, to look at them. And the impact of this DOS is not huge. It's basically a lot of convenience. **Sifis Lagouvardos**
* If this is to to happen and but yeah, it will be expensive to perform. And the overview is that because the fee is updated once for every block, if you take it at an extreme, a user can fill a whole block with hundreds of requests or even over a thousand. But, ideal conditions and goes up to a few hours of downtime. Downtime. And we believe this can be mitigated by changing the code to update the number of access requests, at every new whenever new request is added, instead of once per block. And at most, we found that, for example, one can fit 1650 requests in a single block for EIP VIP 751 and 1900. Request for EP 1702. And for example, if you started at a region at a favorable place, and you start from a low fee, you can make the validator consolidation requests for API 7251 cost over one eath for to 288 minutes. And these are the optimal conditions for this attack as we as we found them. We didn't, extensively we don't have an extensive report for this. And, but it's a complex attack.
* It requires it relies on many factors that will not be, controllable by any attacker. And these factors can be the gas price, the current number of access requests, and the contents of the storage slots that will be written. And Yeah. Due to and the IP seven 251 contract is more vulnerable because of its lower throughput. So basically this we also have some user level considerations which you can find in the report. But I don't want to take up more time. Thank you. 

**Tim**
* Thank you. 

**Fedrik**
* Thank you. And we have another from Planeshift. Who's here? 

**Surya**
* Yeah. Yeah. I'm Surya, I'm part of Planeshift. so during our audit, we noticed fairly trivial issues. you know, mainly regarding minor spec deviations as listed in the report. So, like, things like, you know, how, like the IP states to return zero in some cases, whereas the implementation reverts. other deviations from the spec, like length checks for um call data inputs to the system contracts, which we found to not have any, exploitable scenarios. we did find multiple issues regarding the comments, which were a bit confusing. And we briefly used harmless, but I would leave it up to the A16z team to go over their dedicated formal verification report. 

**Fedrik**
* Yeah. Thank you. And, yeah, like Tim mentioned that. Yeah, the audits were sequential, so we do indeed. it was expected that there would be fewer and fewer, issues found. so obviously, the fact that if someone doesn't find anything doesn't mean that they have they have an inability to find the same issues. The same issues just might not have existed in the commit that they were looking at. yeah. Sigma Prime is next. If, anyone from Sigma Prime is friends here? 

**Richard**
* Yes. Hello. I'll also quickly share a screen if I can. okay. So, quite a lot of what we found has already been discussed and covered, so I won't, I won't repeat and go over it again. The main topic we found was the thing that that the people were talking about, and we got similar sorts of numbers here. a talk briefly about some of the possible impacts. It could be done intentionally to, avoid fees. If you did have a large number of validator consolidations or withdrawal requests. if that's a concern. Possible storage bloat. We asked you what were your concerns? What were your reasons for having a fee? And you said, you know, concerns about storage bloat. And I suppose that's if you have no fee at all. But there still could be some storage bloat by having lots of extra requests written into the storage space. And then, yes, as I was talking about the the sudden spike in fees, it would shoot right up instead of curving up. And I think, I think I think he skipped this. It looked to me like he had this. But in the IP it does talk about fetching the fee. and then like, you could have a smart contract that fetches the fee from the contract. this is 7002 and 7251. both of those.
* So you could fetch the fee from the contract and then automatically send that fee. And obviously, you could have that request in the mempool thinking you're going to spend a very small fee and then end up sending like, more than an eath, to make a withdrawal request. So that's, that's that point. And then other smaller findings. one thing, the, the block, block hash, contract. 
* That's, what's the number? 29. 35. Um is payable. which may or may not be a concern to you. In solidity terms, it would. Solidity would put things into check the call value. it's not very natural, obviously, to request a block hash and send lots of lots of ether in that request, but it can be done. And with an ether with a solidity contract that would be blocked. So maybe you want to check the call value at the start and block that. and then talk about this as well. The this is the same point really to just we also investigated the fake expo and found that it starts to overflow at 28.93. And we we did a little test and we didn't find the numbers got sort of suddenly dipped and we went up to 10,000 and that numerator of 10,000. But it is possible that this value beyond that might suddenly dip. there's a test in the report to check that further if you want to do that. I won't go through this. Inconsistencies with the apes. one little oddity, probably an irrelevant edge case, is that in the Genesis block, some of the some of the behavior is is not as expected. Leave that to the report. and then also, as has been mentioned, lots of comment, comment comments, comments about the comments, possible minor, optimization. And yes, that's, that's everything for me. Thank you. 

**Fedrik**
* Thank you. Richard. Do we have, John here as well? 

**Daejun park**
* Yeah. let me share my screen quickly. can you see my screen? 

**Tim**
* Yep. 

**Daejun park**
* Awesome. Um. . Hey, I'm from crypto. Um. One second. Just a quick disclaimer that, my comments are not, business or technical advice. so I'm working on, formal methods at crypto. previously I was at the runtime verification, and I worked on some bunch of the formal verification work holidays. And right now I'm working on, the, formal verification tool. and I used for this verification. so let me clarify the scope of this verification. to set the correct expectation, that, what I focus on is that the bytecode, behaves as specified in the EIP documents. And, I mean, this is this is because that the, the assembly programmings are really, challenging and many things go wrong. so I wanted to make sure that nothing happened there. I did not verify or reason about anything about the IP spec design itself. like all the DDoS attack vectors or any numerical analysis that I discussed before. there's a clear separation, on this. So essentially I focus on the low level. there are some caveats in that bytecode verification that, so the most I'm using is based on the, bounded symbolic execution. So there are two types of bounds. One is the loop bounds, which meaning that how many loop iterations are considered.
* So right now it's set to the 16, which is, sufficient for most parts of the contracts. except that the, the loops, in the fake exponential, which can go to like hundreds or even thousands in principle. so if anything issue, that appears in the higher, iteration, for example, this overflow more than 2000 will be missed, with the current setting. 
* Of course we can increase these bounds, right now, but but, but but it will take longer. so right now, it took ten minutes in my laptop with this, 16 bound, so you can run and increase. But I think that, I'm not positive that it can increase more than thousands. you know, not really practically feasible. there's another types of bounds, which is the core data sizes. so you need to specify, what sizes of that. And whatever is not specified will not be considered. So, but with that caveat, the result is that, all the verification passed. so we have a really high confidence that, the bytecode really matches with the spec, and this is also the automated. So you can actually rerun anytime. the contract is updated. so actually I set up this continuous verification, actually, since last November, and actually it found some actual issues, some mistakes, during the past, refactoring change, which is immediately fixed. So I think this, continuous verification is really, useful. and I hope that the other projects also adopt this idea. so, yeah, I, I will keep running this, continuous, maintain these artifacts, until, this will be finally, deployed. and good thing about it is that, like this, all the audio reports are actually based on a slightly older version of the contracts, and there are some minor changes made since then. of course there are minor. Still want to make sure that, nothing happened. So the my verification is actually run on top of the latest version.
* And then it all passed. So meaning that all the minor changes really didn't break anything. 
* So hoping that I can continue this, all the artifacts available, in this linked repository. So please check out, you can review or run by yourself or even, contribute. So, and, reach out to me if any question. so, yeah, that's all from me. 

**Fedrik**
* Yeah, yeah. Thank you. Thank you very much. And. A very big thank you to all the auditors that took part of this. And, we're very flexible with the timelines. We know that we were a bit late and the auditors were very good to work with in regards to that. they also showed a lot of good faith by providing, reduced fees, given that it's a public good project. So we are very thankful. And, to John, who has been working on this, pro bono. So, yeah, thank you very much. 

**Tim**
* Yeah, I'll echo that. we reached out. On what? On what was pretty last minute payment timelines for, what I know, for for what I know of how book, auditing calendars are. really appreciate everyone who, who participated in this and worked with us. yeah, it's it's nice to know that, we have high confidence in these contracts. I don't think there were any questions. And again, Frederick shared the report. So, last call. Otherwise, I think we can move on. Okay. next up, so we have this thread about the Petra retrospective. I saw some there's some activity there already. but there hasn't been a ton yet. So I just wanted to, flag this again. I think it would be great if in the next week or two, we could hear from most or all of the client teams there so that we can start discussing things, because, people are starting to bring up, plans or suggestions for Osaka. And I think, there's value in reflecting on Petra before we start making decisions about Osaka. that said, on. Yeah, on that note, like one thing we did agree to in the past was to, cap the number of IPS we include based on what's in the devnet. Right now we have peer and EOF already included in Lusaka.
* So, meaning that we should not include anything else until at least these two things are running on a devnet. So in terms of work and prioritization, teams should move those two things along if we have cycles after Petra. but yeah, hopefully, if like, yeah, maybe next week we'll still be quite busy, but perhaps two weeks from now, we can tentatively try and, like, yeah, discuss everything that came up, on the magician thread around how we want to approach Lusaka and, have a bit of a, like, a higher level discussion before we start to get in the weeds. **Tim**
* But. Yes. Any, questions comments on this? If not. Yeah. So Gajendra has a comment saying vertical is in Devnet. So to be clear here, I mean like the real fork devnet not just like it's running on an arbitrary devnet. So the thing we said we would do is that prior to adding more stuff in a fork, we want to get what's already included on a devnet. So Pusaka Devnet one would have like dash and EOF. And then I think until we have that stable and running, we should not include anything else in the fork. And we can obviously, expand that if and when we're comfortable with it. but that would be like the baseline. And in terms of like short term work, I think on both those tracks, there's still a lot to do. so if teams want to move forward as they wrap up, getting both those things, in a spot where they're stable enough to merge together on a dev net would be, like, the highest impact thing to do. yeah. 

**Guillaume**
* Yeah. Just a quick question. So if, it takes for a very long time to if it takes a very long time to get any feature running on a dev net, what do we do? Like we just, or we realize there's a good reason not to do something. And I'm thinking specifically about execution engine like the idea that seems to be coming back. So I think, that would make sense to, to question some choices we did a year ago. but okay. Yeah. Not not trying to start a debate, but more like just, . 

**Tim**
* So it's fine. If we remove, we can choose to remove something from a net. That's fine. What we should not do and what we did wrong with Petra and caused, you know, months of delay is add ten unimplemented or scheduled, ten and implemented things for inclusion and say, okay, we're just going to go and like implement all of this now and then we have 12 different client teams that have to implement ten different things, and we try to like move all of that forward. It's it's just extremely hard to do this in like a coherent way. So we have like these different statuses. So scheduled for inclusion CFI. So we should start SFI should be the stuff that's going to be in the next depth net. And right now for um for Lusaka we have EOF and PDAs. And you know ostensibly that's what we should try to put in the first subnet. If we realize that, you know, these things are wrong, we can always remove them from the death net. but we shouldn't do something like, okay, we have, we have EOF in Lusaka or EOF in PDAs and neither are ready. And there's these five other IPS and they're not ready either. And so we're going to put these seven IPS at the same time. and I guess. Yeah. Lucas, you're saying like, does won't this make us move slower? My strong intuition is it would not. Because then we can at least know everyone's, like, done the thing at the same time. Otherwise, I think it becomes quite hard to like, basically align on, okay, who's who is where in terms of the different clients and different things. And it doesn't mean there should be only like one one new IP per dev net.
* We can agree like okay, say we have iOS and PDAs and then everything is stable and we want to add more stuff and there's like three small IPS. Then we can all agree, okay, those three small IPS will be in the next dev net. But we shouldn't from the start have like more than we think is reasonable for a single dev net. Roman. 

**Roman**
* So first of all, thanks for saying this. Very supportive. my personal view on the ideal schedule of when we scope and when we ship features is so we have fork n fork n plus one and fork N plus two. By the time that fork N hits mainnet, we already have fork N plus one scoped. So immediately after that. So in this case, by the time Pectra hits mainnet, we already have Pusaka scoped with major features and we started iterating on that. And by the time Pusaka hits Mainit, we already have work n plus two scoped and we can immediately start going into development cycle and testing. 

**Tim**
* Thanks, Lukas. 

**Lukasz**
* Well, I'm not sure if you want to start this discussion. Or should I wait for some other time to give the feedback? 

**Tim**
* I mean, we have yeah, we have some time now. So I think it's an important discussion to have. 

**Lukasz**
* So in my opinion, what we should do is try to adopt this kind of, TikTok, situation, schedule. I don't know how to call it. So, and I think what was proposed just before is, to, to short. So I would say when we are hitting main net on one, on one fork, we should already be going to Devnet on the second fork if we want to make it faster. And that, that means we need to, we need to schedule, so we should have now already, for example, a scope defined at this moment right now. And we could potentially, now debate the next, scope. Right. So, we need to see because and, and this is a good example for, from my side, from our side execution client side, because we were thinking that the next after Lusaka fork would be vertical, and we put a lot of, resources to it, a lot of time, a lot of effort. But right now it's in limbo. And we are, completely not sure what will be next. Right. So that's a very good point that we are not there. And, yeah, yeah. And that's kind of we kind of have to parallelize that, parallelize a bit testing in my opinion, which is not parallelized because, development is already quite well parallelized. but testing and shipping is not parallelized at the moment. And it's not like I'm pointing out, anything. It's just I think it's it's more of a, I don't know, coordination. There is always limited resources. So on, on, on all the sides. yeah. So that's kind of what I wanted to say. 

**Tim**
* So I, I would like us to get there, but my sense is what you're proposing is almost like one step past what Roman was proposing. So it's like step one is. Yes. So I like my sense is if if we do things well in the next year, then maybe for Amsterdam we can be at where you're at. But it like today we don't have pusaka implemented. Right. And to be fair, we already do. We already do have pusaka partially implemented like there are there are devnet there are. So like I think we're we're maybe 50% of where you're saying we should be. And I agree it would be nice to be better. 

**Lukasz**
* Yeah, exactly. 

**Tim**
* Yeah. yeah. 

**Guillaume**
* Yeah. I, I just wanted to say, I think I think it's a bit of a it's not a very good idea to do this thing, because we have a lot of things changing all the time. And I don't think we're fixing the real problem here. The real problem is that we are not scheduling the stuff that matters on the on the roadmap? We're just adding whatever is currently all the rage on Twitter, and it's going to change in 6 in 6 weeks. And we'll, you know, we'll keep running on the next item without removing the previous one. We've had a lot of this happening for Petra. We've had, for example, inclusion list. We realized after some time that this was not going to that this was not ready enough. So we decided to put it on later. And now, we don't really know when we're getting inclusion lists. So it's not even about just recall. It's about all the very important changes to the. 

**Tim**
* And I think there's so there's two different. So there's two different problems though. One is making good decisions and being better at that. And I agree we can improve that. The other one is basically parallelizing the debating about the fork versus implementing the fork. And I think, like Roman's suggestion is like when we get to, shipping fork A, in this case spectra, then we assume that the debate is closed on port B, so this case pusaka and we can debate the fork after all we want so we can debate Amsterdam. you know all we want, but we don't we don't delay the implementation of Pusaka because of this. And sure, this means like, yes, we have to make decisions about what we implement with imperfect information. And in extreme cases we may want to revisit those. But I do think there's value in locking the scope earlier to sort of move the argument to like the fork after. And, you know, I don't know, say we're debating inclusion lists or virtual for the next year and we still haven't come to a conclusion by the time Pusaka ships. Then whatever we did come to a conclusion for is what we should probably put in Amsterdam. 

**Guillaume**
* Right. But my cancer point would be exactly that. It's virtual, right? I started working on it four years ago. It was always supposed to be the next fork. and every time it's pushed yet another small fork in between and then something more important like. 

**Tim**
* Okay, so that's about vertical, but I think it's different to say we chose not to prioritize vertical for the next fork, which is the case. Like we chose not to put it in and then we chose to split. That's different from saying at a given time we should freeze our decision making. And that's independent of whether, you know, putting vertical in fork A versus fork B is the right thing. It's more when do we close the door about, about the scope of the fork? And can we just have like a clean, set of features that we, we implement and test and then we can continue debating, you know, whatever other features for the next fork? 

**Guillaume**
* Right. But, okay, what I'm getting at is when you talk about parallelism. And I understand there's some scheduling thing that's, that makes sense. it's just that if you keep working on features so that they, they get scheduled, you're still having this problem, like, you're still having people. And. Okay, I'm talking about vertical because that's what I did. But I could talk about se, transactions, stuff that Ethan has been, has been working on. there's there's plenty of examples like this that happen to EOF for the longest time. we we need to have a solution. And I don't think this approach, I mean, okay, I understand why you're saying this, but I think we need to also have some guarantee that stuff we work on, you know, first are useful and that we don't waste time working on stuff that will never make it. 

**Tim**
* I agree with that. And I think that's like a third hard problem because there is, there's things that are just fundamentally high uncertainty. and we should do those. And we don't have a great way to like, make a decision about it. And so it's like, yes, there's three different problems. One is just can we ship stuff quicker? Two is can we separate arguing about stuff versus focusing on the implementation. And three is what do we do with like more speculative projects and how should we frame those. Because and you know, there's a sense where sometimes they're just like not ready. And, you know, they take longer than expected and whatever. So we can like I think that should be expected. But I agree we don't have like a clear way to say, oh, you know, like we actually don't think vertical is the path forward or we don't think iOS is the path forward or we don't think SSD or whatever, like, yeah, that's another can of worms. And I, I don't have like a solution for it right now. 

**Guillaume**
* Right. Just just one last thing. when you say we want to ship stuff quicker, I understand that very much. I'm just saying we also need to be careful, because what happened is that Petteri got super big because people said, oh, this should be quick. Sometimes it was, sometimes it was not. But the scope completely expanded, and we should be very careful to pick what is important and not what is going to be fast. 

**Tim**
* I agree, and this is why I feel extremely strongly that we should only pick what we think is the next most important thing to implement in the net, and move that forward. yeah, I know. Okay, there's a couple extra hands. Ahmad, I think you were next. 

**Ahmed**
* Yeah. one thing that I wanted to say is that probably we need to prioritize EIPs with spec tests already employed or developed, with EIPs that are, have the spec tests already developed then that that that the the development and testing of the developed versions can just go ahead. So what I would suggest is that, to, to to make  tests mandatory for, for, yeah, for, for, for inclusion and any ip  author that does not, that wants to his IP to be included to find if he does not know how to write the spec test, then he needs to find someone to champion and to write the spec test for him. If not, then he should do it himself. Yeah. 

**Tim**
* Yeah, I think this is everyone I've spoken to in any context agrees with this. Um. We should. My gut feeling would be for something to go to SFI. It should have tests. We might want to CFI something when it's still like in a more, like, yeah, in development stage. But to me that should be part of the the gate to move from CFI to SFI. I do not work on testing. I think if someone from either eels, DevOps or testing wants to open a PR against EIP 7723 and propose a sort of formal, like testing requirements, that would be extremely helpful. but yes, I think having a like yeah, having that as gate is quite, quite valuable. yeah. Put this. 

**Potuz**
* I'm sorry. I wanted to make a couple of comments. I heard two different things. One is, let's, freeze early. The scope of the fork and the other one is weaker, which is? Let's just freeze right now. The scope of the first net. I would disagree with the first one, but I would agree with the second one. the way that I believe that we can get to ship things faster is by always having a rolling death net for the next fork. So right now this would be EOF plus per dask and we get that net going. At the same time, we can parallelize and start discussing whether or not we're going to add something else or not. But at any time we have a net that is ready or more or less ready to be shipped right next. So then we can always make the decision, let's just pull the trigger. Right now we ship only EOF and Dask and we or we add things to that net. I agree that the first dev net should be scoped. It seems that it's already scoped. I don't see anyone disagreeing that it should be EOF plus or dask. however, even if we go that way, like having this rolling deep net, the only change that I would make to this, this, proposal of like, freezing the scope is that I think, eips that are widely agreed and that are already implemented It can be added to such a definite. So for example, to give an example, now 7 to 12 seems to be a no brainer that everyone wants to to ship. And somehow, for some reason, no one just like strongly pushes for it. But everyone that I talk to, they say, yeah, it's already implemented. **Potuz**
* It's trivial. It should be there. Those things that are already implemented. I believe that it's easy to change the scope of the current definite and add them. 

**Tim**
* Yes, I agree, and I'll reiterate, when we say devnet like I think we want to clarify like devnet one rather than like some random, you know, feature devnet. But I think, yes, having a clear next fork Devnet. and we should maybe find a better word to talk about non feature either like, yeah, we either we have a call them fork nets or we call them like deep nets or whatever. But yes I think it's it causes confusion to compare, an IP specific devnet with, like the thing that we're building towards the fork. yeah, I guess we can bike share this specific thing, but I think we like. Yeah, we should clarify that. then. 

**Ben**
* We should prioritize what's important rather than what's fast. I think as long as we, get the correct prioritization and I'd use, you know, for all of our audience. So I'd use t store as an example there, which was both fast and, for a certain community. I on chain dev's, was very important, but I mean, that took like three years plus to or two years at least to Land, even though it had been implemented before. So we shouldn't forget the little things. and what's important to, wider community rather than just, I don't know, stakers validators, that kind of thing. 

**Tim**
* Yes, I agree. Like, we need to improve the decision making as well. And, justify, like, why we're doing something. Um. Anything else? we can continue this conversation on another call, but I think this has been helpful to at least get some context from different people. And I would reiterate, like, it seems like there's strong agreement on at least moving forward with a tight scope to start. So if you do have spare cycles and you're looking for what to do now, that texture is almost done. here in EOF, I think should form the basis for Or that one. and that should be like our starting point for any other things we consider. and then I'll also flag, mark on the call had proposed, two tips for inclusion in Lusaka. There's been a couple also proposed, as well before. so we don't have to discuss these on the call, but if people want to start reviewing them async, it can help as we start to, um. yeah. As we start to discuss this, there's a comment about scheduling Devnet one for Lusaka. I guess I'd be curious to hear, like, what's the state of the peer and eof devnet, if we want to do this and if it's still. My sense is it's still more valuable to test them independently than to try and merge them together. But I don't know if anyone, has an updated view on that. 

**Potuz**
* They are independent scope, so it's it's easy to test them in the same depth net, because the kind of bugs that you can find are completely different. 

**Tim**
* Yeah. 

**Danno Ferrin**
* So as far as the status of xof. Yeah, it is fairly separate from the consensus layer. I've got four different, clients. never mind Geth and Basu. running under a fuzzing program. They've been fuzzing for almost half a day now. No. No problems found so far. So I'm fairly confident we could ship what we would have shipped for, into a dev net. However, since we have time, since we're not going to ship it in Q2, there are some basic features that we would like to address. that we didn't address because we were trying to hit the timeline. We didn't want to hold things back. I have a list. I'm going to go over it, in the call next week. proposal for draft for, what the dev net's progression would look like before I bring it to a CD, I want to talk it over with it with the EOF call. but I'm fairly confident that we could, it's ordered in wishlist order. We could cut from the bottom and we need a ship, so. 

**Tim**
* Okay. And then that that should be ready the week after. did you want to add something to this? 

**Potuz**
* Yeah. To to to Daniel, I would suggest that we don't change EOF right now, at least not for the scope of the deep net. Let's just schedule a deep net. Let's ship a deep net. Let's start testing on a dev net. And then you have in parallel discussions as to how the the scope of EOF on the next dev net would be. 

**Danno Ferrin**
* You're practically describing the document I have written up. And our dev net zero is shipped. What we have now and then squeak on dev net one and later. 

**Tim**
* Okay, so I guess, yeah, let's maybe, yeah, continue this conversation async, but like, sure, if we can. If we. I'm. I guess I'm cautious about scheduling devnet one now. I'd rather us focus on Devnet six for actually ship this. especially in the next week. Then, like, move people's efforts too much. okay. But it says we can do both. Does anyone else want to schedule the devnet now? Okay. yeah. Let's let's not do this now. Let's ship Petra. and we can also coordinate async on the devnet. and I am cautious about also like. Yeah, having bugs in pure effect, EOF progression and vice versa. Kind of like Donna was flagging. Um. Roman. 

**Roman**
* Yeah. just a quick follow up response to others disagreeing with raising the scope and having the nets for four and plus one running. Again, as I said in the chat, like this would be ideal state of the world, but this is not something we can get to tomorrow or or by the end of this work. Because like we need, we agree that we need to change the process, but we cannot immediately just switch it and get to our North star of how the process should work. So in this case, freezing the scope seems to me like a good first step towards. 

**Tim**
* Yeah, we can actually do this. Okay. So let's yeah, let's continue this conversation. in the next calls. and yeah, I think again, I'll say if teams want to share their views in the eighth magician thread, I think that would be helpful so we can summarize them prior to the call. and then hopefully in the next week or two, we can, yeah, we can agree on a path forward. and then, okay, we have about 15 minutes left. so there's four eips, that people wanted to discuss as well as, Nico from, the EFF has been working on a bot to help streamline some of the ACD stuff so we can cover those. first off, Mark, do you want to briefly touch on the two eips you'd, you'd propose for Lusaka? 

**Marc**
* Hi. yeah. So I'd like to propose these two eips. 7793 and 7843. And both of these add, precompiles, which expose some metadata about the context of where a transaction is currently executing. So the first one, which I think is the more important one is 7793, which adds a PT index Precompile. So this returns the index of where a transaction is being executed in the current block. And the main application for this is in encrypted Mempools. So we can check in a smart contract that a transaction is being executed at the top of the block and otherwise invalidate it. So this can enforce front running protection, and it allows us to implement encrypted mempools at the smart contract level, rather than having to enshrine it in the block validity conditions. So the other precompile is 7843, which is the slot precompile. And this just simply returns the corresponding slot number for the current block. So this is something that is already possible. So we can calculate the slot number from the block timestamp, but to do this you need to hard code the slot length in a contract.
* And so the motivation for adding this precompile is making it easier to change the slot length in future without breaking contracts, so they would be able to migrate to using this precompile at an earlier stage before we potentially change the slot length in future. and it would be good to get some more, feedback from application developers to understand if this is much of a problem, like if there are many existing contracts which are hard coded with the current slot length.
* So to address a few things that people might raise about this. So why make it a precompile instead of an opcode? 
* So this was Danno's suggestion, and it allows, l2's to decide whether or not they want to implement the Precompiles, because it might not make sense to them as if it was an opcode, they would be forced to implement it. And the other one is, could this, kind of introspection be a problem in terms of, zero knowledge proving? and I don't think this is the case because we already have some very similar opcodes such as gas and timestamp, which are very similar to these precompile. So I don't see that there would be a problem with proving these new precompiles if it's not a problem for the existing opcodes. so yeah, I would like us to consider this for Lusaka. Obviously US and EOF are the priorities, but I think they're relatively small changes that yeah, we could consider. 

**Tim**
* Thanks. Ben, you have a question on this? 

**Ben**
* Yeah. Is is the slot number so you can encrypt transactions to a specific slot. And if they're used beyond that, then, like if they don't make the slot you can invalidate them. 

**Marc**
* Yeah. So that that is potentially how it could be used for encrypted mempools. but yeah, I'm not sure. This is kind of why I'd like to kind of start this discussion. Is are there other applications people, with contracts that are using the slot link for other stuff, to actually see if this will be a big problem for changing the slot length or not. 

**Ahmed**
* Yeah. I mean, I'm pretty sure there are, I've already brushed up on some other contracts that are, that they want to calculate some slot length before. that's why we are proposing this, this precompile, to be honest, because future proofing, that's number one, reduce the number of contracts that will be breaking, because, like, right now, if you want to calculate the slot, you have to divide the, the timestamp minus the Genesis timestamp over 12, which is, not always going to be the case if we change the slot time later. And yeah, this this this resolves this issue. So we can have faster, faster blocks eventually. 

**Tim**
* Okay. Any other questions? next up, Kevin had an EIP to discuss hardware and bandwidth requirements, which we've, which we've brought up a bit before, but now it's all been formalized into a single doc. yeah. Kev, do you want to give some context? 

**Kevaundray**
* Yeah. So we now have an EIP. I can copy it into the chat. but essentially it defines the hardware and bandwidth requirements for block builders, Testers and full nodes. if I paste it in here, I think there was some confusion I saw about the block building part. So I'd probably open up discussion for that first. At the moment, it's 50mbps upload for max throughput for block building. Any. anyone? 

**Nixo**
* I just I do want to push back on, 50mbps just because that we have seen a lot of the Staker community, speak up and say that their upload bandwidths are are far below that. And I think that, if we look at median bandwidth upload speeds in a lot of countries and a and a lot of developed nations in Europe and the US and Australia. it's it's far below 50. I would be much more comfortable with something like 25 or 30. 

**Kevaundray**
* But this is for block building, right? Like, solar stickers aren't just like, not all of them are block building. Some of them are using boost. And this is for Max. 

**Tim**
* Look, local block building. Right? 

**Kevaundray**
* Yeah. Sorry. Local block building. 

**Nixo**
* Yeah, this this means that they're not able to anymore. If we if we benchmark to 50. 

**Kevaundray**
* They would be able to but it wouldn't, they wouldn't be able to go to the max throughput. So they'd have to have like less maybe like half a block or something like this. Or like one block in the block. 

**Marius**
* Yeah. 

**Kevaundray**
* Yeah. So, yeah. 

**Tim**
* On that note, I saw, recently, there's, there's data saying, like, you know, the public mempool, gets very little, transactions anymore. So this do we know what's the average gas size? Gas limit of a locally built block at this point? Like, my sense is that they're they're actually not full because, there's just like. Yeah, not that many, public transactions anymore. 

**Kevaundray**
* I think the data always said it was, like, 6 million. I'd have to double check. POTUS. 

**Potuz**
* Yeah. So the the local block building gets triggered for everyone. if the circuit breaker gets triggered, that's our fallback. And, if the circuit breaker gets triggered, if the builders are not building, for whatever reason, transactions will be on the mempool. Blocks are always on the mempool, and currently clients do not have a way of saying, I want to build a blog, but I want to build a small blog so that I can actually broadcast it. so it's, I think it's not correct to have an, an uplink bandwidth neither required nor recommended. That is far beyond the average that can be found in most countries, but not the average. I'm sorry, the median that can be found in most countries. The average is also a bad number to have here. 

**Kevaundray**
* Great. So you're saying that if we had this flag that basically said, I want to put in one. 

**Potuz**
* I, that I definitely disagree with that flag, but that's a different conversation. all I'm saying is that now you're taking averages on countries that have mill, that have like over a thousand, megabits per second for of, on, on, on fast connections. And this certainly drives the average up, but the median is much lower than that. 

**Kevaundray**
* Right? So I did actually look into some of the countries that people were quoting. And I think a better indicator was like the fiber coverage. Germany definitely, had the lowest one, but like most of the countries being cited, had like 70% fiber coverage. 

**Nixo**
* But when you look at those, those numbers, it like in the US, for example, when the fiber coverage is reported, it's per census block and only one residents per census block needs to be, able to get fiber for that census block to be considered covered. So that's not actually representative of who has fiber. 

**Kevaundray**
* Right. But if. Right, I mean, maybe this is debatable, but like if an ISP is saying they're giving 1000 megabits or 5000 or whatever it is, I don't know if it's like a good argument to say that they're going to be giving less than, like whatever the 40 or 50 that's being, suggested, like you'd have to be giving. You'd have to be shaving off like 99%. Right? 

**Nixo**
* No. But for, for example, these census blocks say that like, Brooklyn is covered, because they offer fiber to a few residences in that neighborhood and that that way they can say that they offer it to that census block when actually it's not available to most residents in that neighborhood. 

**Kevaundray**
* Okay I see. 

**Tim**
* Yeah. We do only have five minutes left and there's a couple other things. So I think it's worth continuing this conversation on the node requirements. channel in the discord I guess. 

**Kevaundray**
* Can I quickly ask do people have a problem with the max blobs flag because this solves the issues that we're having. Right. I mean, I know people has a problem with it, but do people generally have a problem with just saying, if you can't do the max throughput, then just build as much as you're based on your hardware requirement or based on your bandwidth requirement. Like. 

**Tim**
* Okay, there's definitely some concerns. So yeah, let's move this back to discord. yeah. But yeah, thanks for bringing this up, Kev. And doing the, hard work of trying to get some consensus on this, which no one has wanted to do for years, in part because it's, contentious. So. Yeah. Really appreciate you pushing this forward. okay. Next up we had EIP 7823. Alex put this on the agenda. I don't know if you're still on the call to set some upper bound for the mod exp. Precompile. 

**Marius**
* I'm here. Um. 

**Kevaundray**
* Yeah. 

**Marius**
* So the the mod precompile has three variable length inputs. And these inputs are unbounded. this has caused multiple consensus bugs. many of the bugs happen with, like, practically useless inputs. if you just craft, those kind of transactions. and the second problem is that it is kind of hard to implement it in VMs, and many VMs have chosen to put limits in place already. an example is polygon VM or scroll. and some others just purely decided not to implement this recompile. The CIP proposes to put a reasonable upper bound on the same upper bound. 10,028 bytes to each of these three inputs. And the reason choosing this value is that this enables still allows RSA um hk RSA verification, which is the highest  key size for RSA which is in use. it's not the highest reasonably used key size that's half this size. but nevertheless, this seems like a fairly good limit. It turns out that polygon VM has chosen the same limit. And we have also performed, some analytics on, the actual main net starting from 2018 when this recompile was introduced. Ending January.
* January the 4th. these statistics are in the EIP itself, and it shows that, the highest width, using successful transactions has been 512 bits. And the, the actually useful, like, regularly used sizes are up to 256 bits.
* This basically means that the IP wouldn't, change the outcome of any past successful transaction, but we don't propose to, introduce this retroactively, rather introduce it in a hard fork. and then furthermore, one more outcome of this would be that this would make it much more simple to be implemented with something like EVM. there are a number of other questions we could put in further limitations, and those are being posted on the magician's forum link. Speaker AA
* So that's a guess. I just want to get some temperature check if Check if anybody is having any thoughts about this. Maybe we don't have time for the feedback today. 

**Tim**
* It seems like there's some loose support in the chat. Does anyone have like an objection that they wanted to bring up? Otherwise I think we can continue async, but is there anyone who feels strongly against this or sees an issue? Okay then if not, like yeah, it seems like there's some support. we can continue this async. we had one last thing on the agenda. So Niko's been working on a bot to help automate some awkward dev stuff. Niko, are you on the call? 

**Nicolas**
* Yes. Can you hear me? 

**Tim**
* Yes. 

**Nicolas**
* Great. so I'm not going to do the full, demo today. maybe I'll do it next week because we don't have time. basically, just to give, context, it's a bot that will automate everything from the Ethereum PM repo. So when an issue is created, it will automatically like create, recording, meeting and cross-post on different platforms. So it's going to Cross-post on Eth Magician and probably also on podcaster. I still need to finish this one. so and then once the meeting is, is done, it will record, it will give a summary and the transcript, automatically posted in in the Ethereum magician thread. And that way people can like, access, the text, like the text transcript to search, precise words with timestamp and all of this. so hopefully it will help people to win some time and to be more effective. And, yeah, I'm open to suggestion.
* I think there is a lot we could like, automate and we could have a good solution that helped everyone to get good information from ACDE without spending a lot of time, into like the YouTube recordings and stuff. And yeah, and we can probably iterate on the AI summaries to find the best ones. And yeah, this way we can have a more efficient ACDE process. 

**Tim**
* Yeah. Thank you. This is yeah, this is really helpful. And then maybe one last thing to mention is I think the bot is open source or will be open sourced. So, yeah, we can get, other people to extend it and add some cool features to it. but hopefully we can automate a bunch of these things that we have to do every time and make it easier, because now there's about ten plus breakouts running in parallel. So Yeah, that'll be nice. and I know. Sorry. Last thing before we wrap up, there's an RPC standardization call next Monday, so I'll just put the link there in the chat. Anything else people wanted to flag before we conclude today? Okay. Well thanks everyone. talk to you all soon and, yeah, let's get, sorted in the next week. 

**Marius**
* Thank you. 

**Ahmed**
* Thank you. 



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
Next meeting on [Feb 13, 2025, 14:00-15:30 UTC](https://github.com/ethereum/pm/issues/1271)












