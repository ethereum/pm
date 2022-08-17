## Meeting Date/Time: Thursday 2022/07/28 at 14:00 UTC (10:00 ET)
### Meeting Duration: 1 hour
### [GitHub Agenda](https://github.com/ethereum/pm/issues/574)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=XDfNg8mdC10&ab_channel=EthereumFoundation)
### Moderator: Danny Ryan
### Notes: Rory Arredondo
—----------------------------


**Tim Beiko (8:56) -** We are live. 

**Danny Ryan (9:02) -** Great. Welcome to Consensus Layer call number 92. This is Issue 574 in the PM Repo. If someone could share that link on YouTube I don't have the chat handy. So we'll go over anything merge related. Then we'll have a segue into MEV boost, some current points of discussion, any other client updates and general discussion from there. Give me one second. Alright, before we get into any particular discussion points, Pari, is there anything to share with respect to any of the shadow forks any of the testing going on, on the side?

## MERGE
## Shadow Fork Updates


**Parithosh Jayanthi (9:56) -** Yeah, so we had two shadow forks since the last call. We had a Goerli shadow that happened last week. And one of the things so we don't really find any big issues. I think there was one that I don't recall right now, but it should be fixed by now, the Nethermind team I think, wrote a big post about and ETH (inaudible). Yeah, but besides that, we've been testing MEV boost on Goerli shadow fork five. It looks good so far. We started with about 8% of the network and I think now we're at about 30% of the network. I looked at your Excel that late blocks, stuff like that everything looks normal from my side, but in case someone notices something or has an idea on what else we need to look at, then please do let us know. We have mainnet shadow fork yesterday that merged on Tuesday, and there weren't any outright client compatibility issues, so that's great. I think it's the first time we didn't have any problems. But now that it's been a few days, I think a few of the Erigon nodes have lost here special feeling to find blocks but that's part of the Erigon doesn't really like the shadow forks. And I had to rethink a couple of the Besu nodes because they were on an older version. And I think they're still not up to date yet. But in general, the network's looking good, we have healthy proposals otherwise, and we're good to go. We would be having a Goerli shadow fork six next week. And the idea for that one is to have MEV boost enabled before the transition. So we can also test how the transition would look with it enabled.

**Terence (Prysmatic Labs) (11:44) -** Hey Pari, for the for the MacBooks testing, which clients are testing it right now?

**Parithosh Jayanthi (11:53) -** I'm just going by the flashbots chart, so it should be Prysm as well as Lodestar and Teku, I think. So those are the three that are listed as yeah, those are the three that are listed as finished the I think Lighthouse as well as Nimbus are posted PRs

**Danny Ryan (12:20) -** Can you share that chart in the chat? 

**Parithosh Jayanthi (12:22) -** Of course. 

**Danny Ryan (12:25) -** Any other questions for Pari or general comments around shadow forks or testing?

## Execution Layer Behavior Around Terminal Blocks

**Danny Ryan (12:40) -** Awesome, great work on the last one. Okay, the next agenda item is the execution layer behavior around terminal blocks. This has been a bit of a conversation over the past week on what happens what to do around multiple valid terminal blocks and if the consensus layer picks something that is unexpected from the execution layer and how to handle reorgs and optimistic sync. Mikhail, can you give us a TLDR and if there's any questions or any like words of advice, make sure to pass that along.

**Mikhail Kalinin (13:13) -** Yeah, sure. Yeah, that's related to go to shadow fork. Basically the case secured there with Nethermind in particular. Yeah, just let me give a quick description of what has happened. So there was like a terminal block A that Nethermind perceived via gossip. It's been imported. And this block reached terminal difficulty. And after that, the other terminal block, or let's call it Terminal Block B has arrived via gossip. But Nethermind has base optimization. It does not process blocks that are not becoming part of the chain like similar to Erigon behavior. So Nethermind could this terminal block B into their block tree, but didn't process it. So there is no state court. There is no like post state for this block. Then the the first transition block built on top of terminal block B that hasn't been processed by by a node has arrived via new payloads method call. And what happened next is like Netherminds return syncing because it does not have this does not have a state to validate this transition payload and then consensus layer has this safe slots to invert optimistically thing which protects us from poachers poisoning and here we got the compound effect of (inaudible) basically the node get got stuck because it can't invert. It can't switch to this fork for 128 blocks the default value for six loss to improve them to basically and that's it. So the the outcome from this case is as follows. The expected DL behavior around the transition block is that whatever happens with like multiple terminal block receive once EL has received a transition block and when and when it has all the data required to recreate the current state and validate this transition block. It must do so. So the fix is like I think in my opinion and we have been in touch with Marek from Nethermind discussing this. The optimal fix would be if you receive like a transition block that is built on top of terminal block B like in this situation. They have to execute terminal block B first and then execute a transition block and respond with that correspondence status, valid or invalid, to allow CL to proceed with this with this branch. That's actually them that this is what is expected basically and I'm curious if I don't know. I guess that Go Ethereum behavior around this is that they are processing all blocks that are received from gossip. Marius can you confirm that?

**Danny Ryan (16:39) -** All blocks up until a valid terminal block and then not necessarily the children? 

**Mikhail Kalinin (16:46) -** Yeah. 

**Danny Ryan (16:48) -** Put on any branch.

**Marius van der Wijden (16:51) -** Yes. And we process of the submitted blocks the terminal block.

**Mikhail Kalinin (17:01) -** So they are instantly processed upon receiving, receiving them from Gossip right?

**Marius van der Wijden (17:12) -** I'm pretty sure.

**Mikhail Kalinin (17:19) -** Yeah, and I believe that Erigon has a fix for this as well. I don't know Andrew, do you do have any information about that?

**Andrew Ashikhmin (17:32) -** Fix? Sorry, regarding what like multiple terminal blocks?

**Mikhail Kalinin (17:37) -** Yeah, like. Like Erigon? Yeah, there was like a PR in the discord shared in the discord that actually do the execution memory or whatever. On the side fork. 

**Andrew Ashikhmin (17:57) -** Yeah, that's right. That's still somewhat experimental. And I also have to double check our logic sort of specifically for multiple terminal POW blocks. I'll look into it.

**Mikhail Kalinin (18:11) -** Cool. Thank you. And I'm curious what is the (inaudible) behavior in this case?

**Gary Schulte (18:25) -** I don't know off the top of my head to be honest, I'd have to get back to you on that exactly how we deal with conflicting blocks coming over gossip for TTD. I think our expected behavior though is that we're going to not reorg unless we receive from the CL an expectation like fork choice update that will revert to that different TTD block.

**Danny Ryan (18:50) -** Right. When you just improve work mode or improve stake mode when you have short range forks, say two ancestors, different. Do you execute those or do you just accept them and then only execute on them, fork choice overtaking? Do you execute short range forks or not?

**Gary Schulte (19:14) -** I think that we're in proof of work mode. We're going to just rely on the heaviest chain and then from then we're not going to reorg at all until specifically we get direction from the CL so a different bit different block coming from (inaudible) probably would probably reorg that for TTD block. But we would immediately switch back when the client consensus client directs us to.

**Mikhail Kalinin (19:44) -** Yea, it's important when you are switching back and you have like this blocked not yet processed, tt's important to to have it processed. This is like one of the ways to to resolve this particular thing. Yeah, why I'm asking is, Marek is here. 

**Marek Moraczynski (20:05) -** Hello. Yes. So I think you can have the same issue like we've had so we didn't brought the block and we returned and syncing. So it will be good to verify it in the Besu. Feel free to ask me if you want more details.

**Marek Moraczynski (20:30) -** Yea, definitely will do.

**Danny Ryan (20:32) -** If you if you do execute these short range forks that I think you're generally protected, but there's probably needs to be a note added to the spec that kind of all of these all valid TTD blocks up until probably finalization should just be executed immediately even if it is expensive. And I think that will resolve the issue here. And we also need to surface a couple of tests here. The interesting thing here was that TTD terminal block B was of less difficulty than terminal block A and so it wasn't like by default, executed and I think we can easily put that into a test as well.

**Marek Moraczynski (21:13) -** I think one of the other considerations is as soon as we hit TTD in Besu, we immediately disable our block propagation manager. So we probably would have to be very, it'd be a tight race to get an alternative TTD block because we're gonna we rely on a backwards sync in that case to reorg back to a different TTD block.

**Justin Florentine (21:36) -** I think we wait until the second finalized block before we disable that propagation.

**Danny Ryan (21:42) -** Yea you disable probably propagation a while I would hope disabled propagation of children of and descendants of a valid TTD block but I think the spec says not to turn off the gossip until syncing has been finalized and then it turns it off. 

**jgold (22:01) -** Terminal blocks should be (inaudible) was finalized. 

**Mikhail Kalinin (22:06) -** Yeah, yeah. This is like important part of of the transition to have the ability to switch between terminal blocks. And yeah, we will have, Marek can confirm we'll have a testnet reproduces the same scenario in hive. 

**Mario Vega (22:34) -** Yea that's correct. We are working on this specific test case to reproduce the issue. One thing I would like to mention, would be favorable to have the specific behavior expected in the spec. For example, how many blocks do we expect to gossip after the TTD and so on? Not sure measures are already included and but it will be nice to have.

**Danny Ryan (23:07) -** Yeah, Mikhail and I can work to make sure that this edge case is very clear.

**Marek Moraczynski (23:15) -** Two additional things from my side that we should be careful is that in new block message we can send we are receiving terminal total difficulty, but we can't rely on that. So please be careful when you are doing checks. And what is more, we need to reject everything after terminal blocks from Proof of Work chain otherwise we could have problems.

**Danny Ryan (24:00) -** So all chains should be processed, incorporated and accepted via gossip up to valid terminal blocks and then no children no descendants of such valid blocks. And then after the chain has been finalized, we can stop gossip on that layer. Okay, but yeah, we'll we'll make sure that this is abundantly clear in specs and make sure that the test gets out soon. Anything else on this?

## Exchange Configuration Before TTD Configured

**Danny Ryan (24:35) -** Okay, next up, exchange configuration before TTD is actually set for mainnet. There's a desire to do this to allow people to get their setups going. And probably some details to decide if we're going to do that. Paul, can you give us what's going on here?

**Paul Hauner (24:57) -** Yeah, sure thing. So previously, we talked about enabling this endpoint before the TTD is set for the purpose that we want to do this. So that people can set up the big node and so the execution layer and consensus layer in a one to one relationship like they would before the merge. So I think all teams have turned it on, which is awesome. It seems that from the EL side, it's unspecified how they should like what the values they should put in the exchange transition configuration struct when the TTD has not announced. The consensus layer has a standard around this. We have these two the two the 256 minus two to the 10 values that I believe all the consensus clients would use. So one option is for the execution clients to just use those values. And then another one is to kind of modify what we have now to send nils or nones around. I have slight preference for the first one. It means that I don't need to change anything as a disclaimer but it's also a kind of an existing specification that exists that could be expanded and then everyone would work with it. Once again, I feel super strongly about how it goes.

**Danny Ryan (26:09) -** Right. So that value was put in to our mainnet configurations for the ability to do testing and to do so without the value that was saying I mean value that was not going to accidentally trigger this on mainnet, if things work they're way into mainnet. So I do think it's a reasonable value to show up in there if people want to be able to do the configuration.

**Paul Hauner (26:37) -** So I think it would probably mean for all the execution clients to just have this kind of one really big number that's a constant, and then instead of returning like nil, you just return that constant and check against that constant.

**Gary Schulte (26:28) -** What was that constant again? There's two to the 256. Would you repeat that again?

**Paul Hauner (27:04) -** Two to the 256 minus two to the 10 in that merge interrupt channel admin a few times also on the issues this one out he's got a two, it's a weird number.

**Danny Ryan (27:21) -** Yeah, the history on that number is because we do use it for test vector generation we didn't want to go over to the 256 by accident by creating some blocks on top of stuff. So almost the biggest number. Okay. Any other comments on this any desire not to do this? I'm not exactly sure if or where this number should land other than in code bases. I mean it's in the consensus layer specs as a placeholder until the final releases. But I don't know if there's an equivalent place that should go on the execution layer.

**Marius van der Wijden (28:12) -** So the problem is if we start adding it to Geth, then we will have like a big like messages around the place that the merge is configured at this point. And then there's like a really big number.

**Danny Ryan (28:33) -** If not configured, use this value for exchange configuration rather than nil. I think that probably be the extent of it. Yeah.

**Paul Hauner (28:47) -** Yeah, that'd be cool. We don't need it to actually actually be in effect, just lie to us.

**Danny Ryan (28:58) -** Okay. If someone from the execution layer thinks this should land in a spec or an issue or something to help coordinate, then by all means do so. But I don't know where that place would be.

**Mikhail Kalinin (29:13) -** Yeah, my preference not to include it stack basically, because it's just like one time functionality. I guess it's just easier to have it in code bases than it was like, one time and done for.


## Opti-sync Clarification


**Danny Ryan (29:30) -** Okay. Okay, Mikhail, you have an issue open on the consensus layer. Specs. I wrote clarification. I think it's an extension. Can you let us know what's going on here?

**Mikhail Kalinin (29:46) -** Yeah, there's a PR that extends the optimistic the definition of what is an optimistic node and as small context behind this. Yeah, suppose like, yeah, we have like currently we have an optimistic node definition as follows. A node is optimistic when it's head is an optimistic block and his head is optimistic. And the case the case that these PR addresses may happen due to optimistic sync but it's not like related to Optimistic (inaudible) directly. So the case is as follows. Just imagine you have like a you have a optimistic branch branch of optimistic blocks that justifies some checkpoints. So it has just has enough at the stations to justify the new checkpoint and it goes beyond the epoch boundary. So the checkpoint is actually just becomes justified and this justification comes into the block store. So is that justified checkpoint is updated is increased in the block store. But it happens. Like while all these blocks are optimistic, while the EL catch up with the state of this pay lots of correspondent pay lots in parallel. And after the justify checkpoint in this store, has found it appears that a portion of blocks that actually do these justification appears to be invalid so CL have to remove these invalid blocks from from a block from the block tree. And after that we can get into a situation when there is no branch that realizes that that there is no viable branch viable in terms of (inaudible) meaning that there is no chip in the block tree that has justify a checkpoint equal to what we have in the store. So and the question is what to do in this case. So what what how the node should behave? First of all, yeah, like there could be different solutions. Like for example, we can roll back that justify a checkpoint at the first glance it seems okay but it can't may lead to the surrounds broken. So it's potentially dangerous. And probably the right thing to do here is to keep the node optimistic. And keep node like in syncing mode, and wait for more blocks to come. From like valid viable chain coming from the network and then nodes stick to the business viable chain syncs up to the head and then get that gets back to normal operation. So this PR is just about like if this kind of situation happens, and due to optimistic sync and invalidation of optimistic blocks, a big node stuck in this like position where there is no viable branches in the block tree. It should just keep being optimistic. That that's what it is. The alternative opinion of that approach is that we should address this stage not only an optimistic case, but in all general case. Like it doesn't matter how we get to this. But we should be like beginners should behave correctly around this situation. Potuz, want to give his opinion on that.

**Potuz (34:10) -** No, I kind of agree with you. It's just what I would like to see is some some sort of standard of how we are we have to add. So I think currently, perhaps Adrian if he's here can correct me, but I think Teku would revert back to the justified checkpoints and accepted as head so that they can continue importing blocks. I think Paul was about to set up to stay with them invalid head and being able to continue accepting blocks this way. Prysm hasn't solved this issue yet. We don't really know what is the best way. And what I kind of see on both Teku and Lighthouse approaches is that if they reboot the node, they might be gossiping blocks that they knew they were invalid. Prysm removes invalid blocks from the database so so that once we know what block is invalid, we're not going to go (inaudible) it back. Yeah, I have no feelings. I just don't know if a good solution to this problem yet. 

**Dankrad Feist (35:20) -** Um, yeah, like sorry, I missed this question right now before my connection. But can you say like you mentioned something about having to revert to justify nodes. Like do we consider justified blocks from optimistic saying actually is justified? Like before we have actually verified that the chain is correct? 

**Danny Ryan (35:48) -** Nodes generally do so to not disrupt internal machinery so much, this is a critical failure. The node that was an optimistic sync, and there was either an attack or a chain split. I mean, the general the general notion since the beginning of this is that is a failure and likely requires manual intervention. So that the answer the question is, what do you do until somebody (inaudible)

**Dankrad Feist (36:19) -** Right, I mean, I guess my question is, is it possible that a node votes votes with this source being an invalid?

**Danny Ryan (36:30) -** No a validator should not be voting on (inaudible) optimistic.

**Dankrad Feist (36:38) -** So the so So, so being dangerous, it's not actually 

**Danny Ryan (36:44) -** It's also not dangerous because your database database it would be down here from (inaudible). 

**Dankrad Feist (36:52) -** Why would you slash a database for them? Oh, like okay, as in, you will be locked out (inaudible).

**Danny Ryan (36:56) -** Being locked out is different than (inaudible). 

**Dankrad Feist (37:00) -** Yes. Well, yeah, okay. Well, I mean, in practice, in any situation where you're locked out, you're probably gonna be part of inactivity.

**Danny Ryan (37:17) -** Sure, well, not. You can have an accidental sign message that isn't for (inaudible) other people.

**Dankrad Feist (37:25) -** Yeah, but if the block is justified, then that's probably not the case.

**Mikhail Kalinin (37:34) -** I would like not rely only on discretion protection here. I mean, the node that got into this state. It's just must not must not test at all.

**Danny Ryan (37:56) -** Yeah, that's an that's defined in the specification.

**Mikhail Kalinin (38:02) -** Yes, but but when you're invalidating optimistic blocks, you're just have no had no viable have. That could be the case.

**Adrian Sutton (38:16) -** Yeah, I think it's just important to clarify that in this case, the justified checkpoint is fully validated. But we've had a sequence of optimistic blocks that caused us to update justify checkpoint, and that sequence turned out to be invalid, so we shouldn't have updated the checkpoint. But we're kind of stuck. Because we aren't able to revert that in clients currently.

**Danny Ryan (38:42) -** Right. 

**Paul Hauner (38:43) -** So that's the justify checkpoint need to be fully valid. It can be optimistic, right?

**Danny Ryan (38:49) -** Well, it needs to be fully valid if you're gonna actually act on it. But

**Adrian Sutton (38:52) -** Yeah, so it might be optimistic in the normal case, it would be and then this all kind of resolved itself. And we're still optimistic regardless. It's the case when the justified checkpoint is valid, but we had to fall back to it because of an update to justify from a sequence of blocks that turned out to be invalid, that we wind up in this case, but we might be attesting based on changes from optimistic blocks that we've since reverted, even though a head is an optimistic.

**Danny Ryan (39:27) -** So I would argue that it's important that you're not attesting to optimistic things. And that this is then acknowledging there's the failure case. And then the failure case, I don't know needs to be standardized because the failure cases are either stuck. And I have to have user intervention. I have more sophisticated machinery and I can try to work myself out of these optimistic blocks, which, by default, I think a lot of people don't want to do but it's not necessarily a bad thing to do if I'm if I'm able to actually go and revert this machinery knowing that if I wasn't attesting, I'm not actually doing anything bad. I'm just trying to get out of that reality. But I don't know if one or the other needs to be the exact thing that we do.

**Mikhail Kalinin (40:20) -** The problem currently is not guaranteed follows this stack. It will have it will have the justified route as the head so it will just revert the head back to its justified through it. Which was like pushed by invalid logs but it's not a problem. It's like a valid justified route with enough at the stations to justify the problem is that there could be some some honest blocks on top of this route as well. And yeah, if if like majority starts to vote on the justified route right. And I don't know be able to block on top of this. So some some of the honest block a portion upon his block and yeah, but it definitely is like a very much edge case scenario. And probably I should like put more context to these PR. I mean, like the example of what can happen and what the situation that's right like to just

**Potuz (41:33) -** Say it's not so much edge case. Given the fact that suppose an attacker can actually get some nodes into optimistic mode. So this is along those lines of attacks that get worse once they managed to get to optimistic because they only need two blocks. If they get the last block of an epoch and return is syncing, and then the next block of the epoch and turns out to be invalid. Then they can just pull they can just trigger justification of opening up a new block. So only only two blocks is enough to trigger this

**Paul Hauner (42:11) -** I don't want to get into details of how we can do this here. But it's a little bit more difficult than that with some some changes.

**Mikhail Kalinin (42:27) -** Yeah, that's probably take the discussion into discord, this PR.

**Potuz (42:35) -** So Prysm is going to do what what Lighthouse is thinking on doing on keeping an invalid head within for choice. Just ignoring the fact that in this situation we're importing blocks that where we're fortress is in a coherent state.

**Paul Hauner (43:04) -** Yeah, I think all the approaches pretty reasonable, that are on the table as well. It was one I didn't see any problems with it. I think all of them if all the nodes in it all at once. We've been in a lot of trouble, but I don't see any problems either way at the moment.

**Adrian Sutton (43:24) -** Yea, I'm not a huge fan of trying to have an invalid head. Just it's very hard to reason about what the knock on effects of that will be. But I need to take a bit of time and look at whether we can be sure to stay in optimistic mode. I think that's quite reasonable in this case. Probably doable.

**Paul Hauner (43:53) -** My latest thinking with regards to optimistic is that the node doesn't care. It doesn't distinguish between optimistic and invalid. The only scenario it cares about is trying to avoid the invalid ones when it's choosing ahead which it can't always do the I've been trying to take that approach now. Where invalid and optimistic are the same thing because you can't trust them. And all we do is try and fork around the valid ones if we can.

**Potuz (44:21) -** That will work for us because we do differentiate between them we actually remove everything that is invalid. So we're gonna have a root for head that is not no longer important. We can treat those that situation that's a very special situation where our head is no longer in fortress. Optimistic but but it will be something new.

**Paul Hauner (44:49) -** Yeah, leaving the invalid ones around and just keeping as optimistic is I don't know if it's, it's generally easier but maybe it's harder if you haven't gone down that path.

**Potuz (45:02) -** It's it's easier and broader array but we have another fortress implementation where it's really trivial to remove everything invalidate it. Just remove one node in a tree and automatically removes the whole subtree but now we're getting technical

**Danny Ryan (45:21) -** Okay, let's circle back on Discord and this issue and refine it thanks for the details on discussion.


## MEV-Boost

## MEV-Boost During Merge Transition

**Danny Ryan (45:42) -** Okay, any other merge related discussion points for today? Okay, great moving on MEV boost. There is an open issue around MEV boost during the transition. I think there's been some general agreement on the past call or two but Alex is there anything else to do before we merge this?

**Stokes (46:15) -** I don't think so. Let me grab a link here. Basically on the last call, we agreed that we would, more or less have an embargo of using MEV boost through the merge transition. And when we would stop this quote embargo would be once we have finality. So this PR reflects that and I just wanted to call it out before it gets merged in. I think a number of you have approved it on the PR so I guess this is your final chance. Otherwise, that's what we'll move forward with.

**Danny Ryan (47:00) -** Okay great. And MEV boost liveness discussion. Alex, looks like you have a doc and maybe some quick discussion points you can give us here and then we can do some review outside of the call.

**Stokes (47:18) -** Sure. Let me also grab the link here. So let's see. What I'll drop in the chat is a very helpful sketch of a proposal. So the proposal was to address a problem. And the problem is the following. There's essentially a very extreme failure case where nodes are using MEV boost, post merge. And what happens is there's this actor called a relay who should release the block after it's been committed to after proposer has signed that this is the block they want to propose. And this relay could fail to release the data they need to and suddenly there's a liveness failure on chain because the block just can't be a symbol. So you know, to be clear We don't expect this to happen. But in the event that it does, we should maybe have some mitigation, what this would look like on chain suddenly slots are missed. And so this proposal says why don't we just use this as a circuit breaker condition? So if there say like five blocks in a row are missing, there's luckily (inaudible) stop using MEV boost, this might be you know, there's gonna be a lot of false positives, because there's a lot of reasons there cannot be blocks suddenly, but sort of like a safety thing where it's like, we should at least do this and maybe do some other things as to figure out why there's suddenly no blocks but yeah, so I wanted to bring this point up. There's this documents here. The document if you review it, it's like again, I pretty simple and straightforward and part of that reasoning is because ideally, this is something implemented and beacon nodes before the merge even happens. So pretty soon. There's a bigger conversation around how sophisticated these heuristics should be around when we, you know, stop using MEV boost or when we re enable it and things like that. And yeah, maybe you're welcome to leave comments on the dock or maybe actually taking them to the Discord as plant would be a good place to continue.

**Danny Ryan (49:28) -** Right. So it's easy to say you produce a block and you commit to produce the sum bid and then you don't get the full block. It's easy to know locally. Okay, well, I shouldn't use that relay anymore. But I also might be one validator and might not get another validator for make another proposal for quite a while. And so that information isn't actually useful to everyone else. If it's something systemic that's happening, and then there's not really a way to demonstrate that easily to your neighbors. Maybe there is some sort of gossip and timing analysis and things like that. But but we're not there. So instead, circuit breaker and make sense.

**Mikhail Kalinin (50:17) -** Yeah. I'm wondering if we can increase the maximum (inaudible) laws to something like I don't know 16 probably. And what what like the what how to say what we get if we have this value, too big. I mean, what downsides we can get is for value it's it's like pretty easy to be exploited by adversary like I don't know if that was like 10%. So let's take that we'll just have a chance to to just with all these five blocks in a row, then publish them after some time when everyone has switched from that goes to the ELs. If there there is any gain from there is any payout from from from this game from this behavior. The other 

**Danny Ryan (51:15) -** Yea there probably is because they can have MEV boost on. Is Micah talking? Is someone talking? I heard someone talking very quietly in the background. 

**Dankrad Feist (51:36) -** Would it really be like me, how would that work if you release those blocks? I mean,

**Danny Ryan (51:41) -** You don't have to really release the blocks Dankrad, you can just miss them, and everyone else turns off MEV boost.

**Dankrad Feist (51:47) -** Yea but then you but then like you missed five blocks. I mean, that that

**Danny Ryan (51:55) -** Yea but you might have multiple like you might have many epochs in which you're the only one successfully getting

**Dankrad Feist (52:01) -** Wait, how long are we turning MEV boost off for?

**Danny Ryan (52:04) -** The current suggested condition is (inaudible) I mean, I would say I would say 16. 

**Dankrad Feist (52:17) -** How about making about making it an exponentially increasing recovery periods? Like first time you do like 16 blocks, then 32 blocks and 64 or something?

**Danny Ryan (52:33) -** Yeah, I think that's reasonable. I think we're also probably, we're gonna be balancing simplicity. Just if we want to ship something like this. It would also the other one is to say model your adversary. And then find the number. You know what size adversary we're talking about. And what number of blocks is it, diminishingly small chance that they're gonna get in a row?

**Mikhail Kalinin (53:00) -** And just, I think that it's not necessarily you miss those slots. You may just recall these blocks and release them later. So you will not miss the opportunity to propose all this stuff. Not sure how this difficult to do. But

**Dankrad Feist (53:16) -** I mean, there's one downside side of this even with five block. This means MEV boost can can only deliver every block and then everyone will be (inaudible)

**Sean Anderson (53:42) -** So we've actually implemented this in Lighthouse or at least something similar. And generally what we were thinking is to allow whatever the conditions for not using MEV boost are to be configurable, but the user and then like, I think, generally maybe it'd be better not to strictly specify the exact values so that they aren't capable. Or at least like harder again. And then we can maybe have like, diverse like defaults across clients about like, Oh, is it five slots in one client and like 10 in another, something like that? 

**Terence Prysmatic Labs (54:23) -** Yeah, I think I agree with that. I think most of it should be client implementation detail. Just because like, some policy might be easier to implement on one client versus the other client. But I do think like, every client should implement something just to prevent it. 

**Adrian Sutton (54:45) -** I think the concern I have here is that we're adding a bunch more complexity to try and avoid a real corner case. And when we've done that in various ways in the past, like Doppelganger support, we've been seeing bugs where it kicked in when it shouldn't have which then causes kind of more problems. So particularly if you can keep this simple, as simple as possible. It's not so bad because you are pulling back to local VL. But I can kind of see a bunch of problems coming out just because we're trying to track a whole bunch of new stuff or have all these conditions. 

**Martin Holst Swende (55:30) -** Yea, I disagree with Adrian, what you said about adding complexity. Because what we're talking about it's very, basically a switch that disables integration before MEV boost and in the way I see it, everything should continue working perfectly. If MEV boost goes offline and if all is central things are, if all the components that are not layer zero goes down, platform should still continue working. So I don't I don't see if we if we think that MEV boost going down will cost lots of problems, then we're in a bad place. And based on that reasoning. I don't mind adding complexity that may cause them MEV boost to start fading if we you know, yeah, so I think it's a good thing. Circuit Breaker. And I agree, though, we do different choices and compliance and we could even do some randomization in individual nodes. So they have different levels.

**Danny Ryan (57:00) -** I generally agree. I mean, right now there's probably going to be one relay, maybe two and that they can take down the whole network. If there's not a circuit breaker here, I do think that the circuit breaker can be simple. And I do think if we model their adversary and we pick it even 32 slots can be simple and it can be you know, very unlikely to be hit by an attacker.

**Adrian Sutton (57:27) -** I think that's one of the simplifications I quite like to see is at the moment, there's a (inaudible) that we've got to count blocks even if they're not on the same chain in working out if we've missed the slot or not. Which is definitely required for a small number of slots. But if we can make that big and be able to just look at the state and go, Hey, I've not had a block, look at the block routes in the state and go yeah, we've missed 30 slots. They're not gonna stop using their boost. That would simplify implementations quite a lot. You're not having to track anything new at all.

**Stokes (58:03) -** Is it okay to not have an epoch or (inaudible) though?

**Danny Ryan (58:08) -** I mean, and to automatically recover, probably once and then we figure out what the hell went wrong and try to make it not happen ever again.

**Adrian Sutton (58:22) -** I mean, that's also assuming that everyone sets up MEV boost and isn't paying attention to it so. Like big providers probably see one block proposal go missing and start worrying a lot because they've been given unblinded block. They have that insight across their nodes. If you're running a lot of validators, and then there'll be a variety of Homestakers that don't use MEV boost because it's just too much for them to set up.

**Dankrad Feist (58:55) -** This is my main concern with having a fixed number especially a large number of blocks and I can see lots of conditions where we have quite a bad failure case, but people will continue using MEV boost, like say MEV boost only delivered every third block is a possible failure case. And nobody would stop using it. Maybe it was so like,

**Danny Ryan (59:24) -** That would be using it automatically. But we would also work on figuring out

**Dankrad Feist (59:30) -** Right but it would be in a pretty terrible state in that case. Already. Like

**Danny Ryan (59:35) -** Right but that's also like in more particular. I mean, there's there's failures that can happen. And there's a certain amount of like automatic detection that we can do or is worth the complexity of doing. 

**Dankrad Feist (59:48) -** Right. Maybe, maybe the threshold I mean, you can also say like less than x blocks over a period of y and that's a much more robust conditions than zero blocks over period y.

**Micah Zoltu (1:00:07) -** Are blocked builders in this version. of MEV boost bonded in any way?

**Danny Ryan (1:00:017) -** No, nor relays. Relays are kind of this. You assume the relay has the block and can make sure the block gets out when you're entering into negotiation with them. And this is your case when it's right in the middle of the negotiation are kind of right at the end where committed but they don't release it.

**Stokes (1:00:43) -** The messages are signed so we'll know who did it. But there's no like actual like crypto economic bond risk. 

**Danny Ryan (1:00:55) -** Is there any reputation around this? These messages can be demonstrated in a certain amount of them could mean I don't use that relay anymore but that's also a lot more complex than this circuit breaker.

**Micah Zoltu (1:01:07) -** Yeah, but I mean, I'm kind of agreement with I think the point that Martin was getting at earlier that the someone should not be able to take the chain down for however long you know, minutes hours whatever, by getting control of the relay. So it's a pretty bad failure mode. Like even if you can't automatically recover.

**Dankrad Feist (1:01:33) -** This is the trade off we're making with MEV boost.

**Danny Ryan (1:01:37) -** The discussion is can we ensure that the trade off isn't so bad? 

**Dankrad Feist (1:01:44) -** Yeah, sure. Yeah. 

**Danny Ryan (1:01:50) -** Adrian, your assessment of complexity on like a percentage of blocks X out of N rather than a series of missing is that is that a similar complexity?

**Adrian Sutton (1:02:03) -** Yeah, I mean, I think a deal for me is anything we can get from the current state rather than having to look across blocks. That saves me a lot of complexity from what I can kind of think initially. Maybe I'm wrong in that, but that's kind of my first take.

**Micah Zoltu (1:02:18) -** The actor who has the ability to or the participant a system that has the ability to withhold the blind a bot blocks that's the relay right and in at the merge the expectation is there'll be very few relays that correct?

**Danny Ryan (1:02:35) -** Yes, there's also a problem with such a relay. Keep if you always, if you didn't know to switch to relay B, because no one's demonstrated that relay A is bad then you also the multiple relay doesn't necessarily help that relay maybe line viewers

**Micah Zoltu (1:02:57) -** Is it visible to all participants in the network when a blinded block is committed to and then never revealed?

**Danny Ryan (1:03:07) -** I do not believe that. But they could be.

**Micah Zoltu (1:03:11) -** So at the moment, at least, only the proposer knows that they relay withheld their never gave them a block is that correct?

**Danny Ryan (1:03:20) -** Correct without additional gossip.

**Micah Zoltu (1:03:27) -** I know we're very close to the merge hasn't asked this, but how hard would it be to fix that and that feels pretty bad. Like it shouldn't be that if the relay is not revealing blinded blocks, they promise to reveal like that should be known to the whole network as soon as possible. And so you can see hey, relay hasn't given up they're blinded block in the last four blocks. I'm gonna stop using the relay and fall back until (inaudible) intervenes. That way we can limit the failure to you know, a few blocks in a row until humans get involved rather than having to continue on for hundred blocks or whatever.

**Stokes (1:04:02) -** I think it's tricky to make it really tight. Meaning like only a few blocks versus say, like an epoch just because of the reasons we've been discussing. But yeah, like Chris put in the chat. There's this idea of like a relay monitor that I think at least flashbots tends to have for the merge, which would handle these like high level, you know, like says the big failure cases that are easy to figure out.

**Micah Zoltu (1:04:29) -** Yeah, but I feel like we're not really solving the problem. If we just say, hey, if if that centralized player turns malicious because they got hacked or whatever, let's just trust this other centralized player to tell us about it, especially when they're both controlled by the same actor in the ecosystem. Like if you're gonna, if someone does manage to compromise the keys of the people running MEV boosts they're probably gonna get both sets.

**Stokes (1:04:53) -** So the alternative then is like to have MEV boost like gossip, some sort of fraud proof around us, which could be done, but it's more of well, you're just saying maybe you haven't seen this block? Yeah.

**Danny Ryan (1:05:12) -** It's not fraud proof though because you can't tell if maybe the proposer which is really late, and giving it give giving it back. Okay, but enough of them signals that it's probably fraud. 

**Dankrad Feist (1:05:26) -** Well, we can we can, there is one solution, where you gossip your choice like basically, we create a channel for proposers because of their assigned block header. And you can watch that channel and if you see several of these, and you don't see a corresponding block, then you know that the relay is bad. The problem is creating that I think it's not realistic for the merge. I think that's too much. Like because you'd also have to consider all the loss possibilities and stuff.

**Paul Hauner (1:06:04) -** Yeah, I would generally say that if you're thinking of a solution and involves adding a new topic to the P2P network, and it's too hard to the merge and I'm pretty sure all of them involve that. So it doesn't seem feasible at this point.

**Dankrad Feist (1:06:21) -** What does seem feasible as like just creating a service that monitors is like, like how hard is it to create a like a simple monitoring daemon that anyone connect to it using their validated data? So like, one of us could run it. It's independent from flashbots that doesn't seem that hard, like, feels like a few 100 lines. 

**Micah Zoltu (1:06:55) -** We still need a mechanism for proposers to be able to (inaudible)

**Stokes (1:07:05) -** (inaudible) needs to be automated, I guess like it can be manual to like, you know, facilitate shipping the merge. And then an obvious enhancement is to make it automated.

**Micah Zoltu (1:07:13) -** If it's manual, then it means that the potential outage if the relayer is compromised is hours to days, because people are not

**Stokes (1:07:22) -** It wouldn't be days. But we also do say we're ok with like an epoch of missing blocks. So

**Micah Zoltu (1:07:35) -** Yeah, definitely appreciate the bind we're in. We've got the merge coming up very soon and we have a centralized point of failure. And we have to decide, you know, how long are we okay with the network being down if that centralized point of failure fails? Until and we have to live with that risk until such time as we have a real solution such as bonding or at least gossiping.

**Stokes (1:08:24) -** All right, so there's some appetite for a circuit breaker of some type. I'll figure out a place to make that more formal and we can keep pushing that separately. There's like other different strategies and tactics we've been discussing around hardening MEV boost. So that's good as well.

**Danny Ryan (1:08:47) -** Okay, cool. Alex, are you going to make you're going to refine the that document share? Is there a place where we're going to discuss this?

**Stokes (1:09:00) -** I suppose the block construction channel and the r&d Discord, but I'm open to anywhere.

**Danny Ryan (1:09:08) -** Yeah, that's good. Okay, cool. Let me find my agenda, your next step. Oh, no live discussion. Perfect. Anything else related to MEV boost?


## Other Client Updates


**Chris Hager (1:09:35) -** Maybe just a quick call for Lighthouse and Nimbus to maybe wrap up to build the specs implementation, so they can be tested in the next shadow fork along with data clients. That that would be ideal.

**Sean Anderson (1:09:53) -** Yea, so our PR is actually under review right now. Getting close.

**Zahary (1:09:59) -** The same is true for Nimbus. We are close to merging this PR and we are planning to release shortly after. 


## Research, Spec, Etc


**Danny Ryan (1:10:11) -** Cool, thank you. Okay, anything else on MEV boost? Great, any notable client updates are happening so you would like to share? Other research specs or other items to discuss today and anything at all that people would like to say announce discuss or otherwise.

**Tim Beiko (1:11:00) -** We have just gonna say quickly we have a 4844 call tomorrow at 14 UTC. If people want to follow up on progress on that. The link is in the PM repo.

**Micah Zoltu (1:11:20) -** Where where's the appropriate place to cry about this, MEV boost situation offline?

**Danny Ryan (1:11:25) -** Maybe on the builder's specs repo. You could write an issue about proposed bonding or other things like that. And also in the Block Protection channel in Discord.

**Dankrad Feist (1:11:45) -** There's going to be no bonding before PBS

**Danny Ryan (1:11:53) -** Meaning any sort of bonding that you would do would without a one support would need to be it would be opt in in some sort of extra protocol mechanism that relays decide to do.

**Dankrad Feist (1:12:06) -** I mean maybe it was Chainlink or something but it would suck

**Danny Ryan (1:12:09) -** Oh yeah, you need you need to like like Alex said a (inaudible).

**Dankrad Feist (1:12:13) -** Like you need and you need an availability or for the science header and the main block and I just...that's not gonna happen. I'm not I'm not just saying before the merge I'm just I'm saying it's doesn't make sense to do this before PBS. Like maybe it was literally our stopgap solution. That's how it was conceived and yea.

**Danny Ryan (1:12:53) -** Yeah, I think we can get better on reputation and more transparency around messages and the circuit breaker but I also agree that

**Dankrad Feist (1:13:05) -** Yeah, I think this is great. I mean, and I think that's totally possible. And I think like it's just like, This doesn't have to be a like a monitoring service doesn't have to be decentralized. We can, we can find solutions for that worked very well. Like I don't know, like, I mean something that like if you build a piece of software that any of us can run, and that all the proposers can submit their blocks to and that can like (inaudible). It's like one relayer I have missed several blocks then. Like why is that a good I think that's a pretty was pretty fine.

**Micah Zoltu (1:13:56) -** Yeah, I would be mentally happy with like that in our situation. I'm saying that. I do think we shouldn't be built focusing on building something. And that something is going to involve clients, like the client or the ones that need to send to that. 

**Dankrad Feist (1:14:14) -** Right, right right, okay, but the client or the client and that's the minimum. 


**Micah Zoltu (1:14:22) -** Yeah, I'm just saying like, I think this should be a focus that we should be figuring out what that solution looks like, even if it is centralized, you know, make it centralized dish, right. So anyone can run with what are your services and you can point your proposer at end of them. And so you can broadcast out to seven different ones run by seven different people around the globe. And if any of them report back of evidence, and they can give (inaudible). 

**Danny Ryan (1:14:45) -** Yea I think, very fortunately that a lot of this actually can be encapsulated inside of the MEV boost sidecar. And so it's much easier for me to MEV boost sidecar to add some sort of like experimental gossip channel to be tracking relays and reputation and that kind of stuff or even me communicating with an external monitoring service. And it's been designed that way, for a reason, right? So I can I can I don't have to go into the internals of the beacon node for everything as long as like the beacon node knows to communicate with the sidecar as you know, to get extra valuable blocks and if the sidecar is not giving anything, go local. And so I think complexity is very nicely carved out there to iterate to build up MEV boost. Ok. Shall we close the meeting, anything else?

**Parithosh Jayanthi (1:15:48) -** Just one more thing, the Goerli blogpost is out so please update your nodes. And all the client teams have releases and Goerli forks should be in the next two weeks. 

**Danny Ryan (1:16:03) -** Very exciting. Okay, thank you, everyone. Very productive conversation. Talk to all soon.



### Attendees
* Micah Zoltu
* Tim Beiko
* xinbenlv.eth
* Mikhail Kalinin
* Potuz
* Terence(Prysmaticlabs)
* Danny Ryan
* Pooja Ranjan
* Parithosh Jayanthi
* Fredrik
* Marius van der Wijden
* Justin Florentine
* Ben Edgington
* Andrew Ashikhmin
* Hsiao-Wei Wang
* Mehdi Aouadi
* Trent Van Epps
* Stokes
* Adrian Sutton
* Stefan Bartanov
* Sean Anderson
* Mario Vega
* Chris Hager
* Gary Schulte
* Guillaume
* Zahary
* Stefan Bratanov
* jgold
* Martin Holst Swende
* Barnabé Monnot
* Lion dapplion
* Enrico Del Fante
* Tomasz Stańczak
* Saulius Grigaitis
* Paul Hauner
* Ashraf
* Ansgar Dietrichs
* Marek Moraczyński
* Nazar Hussain
* Dankrad Feist
* Fabio Di Fabio
* Gajinder
* lightclient
* Matt Nelson
* Zuerlein


### Zoom Chat

10:00:49 From  Trent  to  Everyone: gmgmgm

10:00:51 From  stokes  to  Everyone: gm

10:00:58 From  Ben Edgington  to  Everyone: gm

10:01:00 From  terence(prysmaticlabs)  to  Everyone: gm

10:01:00 From  stokes  to  Everyone: first to gm, first to 'bye'

10:01:02 From  Mehdi Aouadi  to  Everyone: gm

10:01:06 From  Potuz  to  Everyone: gm

10:02:30 From  danny  to  Everyone: https://github.com/ethereum/pm/issues/574

10:05:45 From  Chris Hager  to  Everyone: https://boost.flashbots.net

10:05:55 From  Parithosh Jayanthi  to  Everyone: ^ yea that's the one 😄

10:11:16 From  Potuz  to  Everyone: https://github.com/ledgerwatch/erigon/pull/4812

10:11:19 From  Potuz  to  Everyone: it's merged 

10:13:32 From  danny  to  Everyone: yeah, I think so

10:14:46 From  Mario Vega  to  Everyone: I am working on exactly this scenario in hive, it would be nice to have the expected behavior in spec too

10:16:50 From  Justin Florentine  to  Everyone: i believe spec says to keep gossip up till 2 finalized epochs

10:18:10 From  Marek Moraczyński  to  Everyone: Mario I wrote some tests in Nethermind for gossip: https://github.com/NethermindEth/nethermind/pull/4327 it could be useful for you

10:20:15 From  danny  to  Everyone: TTD_NOT_SET = big_value

10:20:21 From  Mikhail Kalinin  to  Everyone: 2**256 - 2**10

10:20:25 From  danny  to  Everyone: 2^256 - 2^10

10:20:34 From  danny  to  Everyone: **

10:20:41 From  Marek Moraczyński  to  Everyone: https://github.com/ethereum/consensus-specs/blob/981b05afb01d5b19be3a5a60ccb12c3582e4c0cf/configs/mainnet.yaml#L16

10:22:59 From  Mikhail Kalinin  to  Everyone: https://github.com/ethereum/consensus-specs/pull/2955

10:27:14 From  xinbenlv.eth  to  Pooja Ranjan(Direct Message): Pooja, do you know if there is a live note?

10:28:31 From  Pooja Ranjan  to  xinbenlv.eth(Direct Message): I am not aware of but, Ben will post one quick notes right after the meeting. Christine May have started recently, may want to check.

10:29:04 From  Potuz  to  Everyone: yes

10:29:25 From  Micah Zoltu  to  Everyone: Your mic background is quite loud @Dankrad, can you mute when you aren't talking?

10:29:46 From  Potuz  to  Everyone: the justified checkpoint may be completely VALID in this situation

10:29:53 From  Potuz  to  Everyone: and still need a reversal

10:30:51 From  Lion dapplion  to  Everyone: Who has kids in the background :heart:

10:31:01 From  Micah Zoltu  to  Everyone: @host can you mute Dankrad?

10:31:04 From  Micah Zoltu  to  Everyone: Nevermind.

10:31:07 From  danny  to  Everyone: done

10:32:04 From  Potuz  to  Everyone: it can be

10:37:22 From  danny  to  Everyone: I was misunderstanding the scope of the problem. understood now and will think on it

10:39:16 From  Parithosh Jayanthi  to  Everyone: Update nodes for goerli!

10:39:38 From  stokes  to  Everyone: https://github.com/ethereum/builder-specs/pull/38

10:40:44 From  stokes  to  Everyone: https://hackmd.io/@ralexstokes/BJn9N6Thc

10:45:27 From  Gary Schulte  to  Everyone: lol

10:45:29 From  Micah Zoltu  to  Everyone: Haha!

10:45:34 From  Micah Zoltu  to  Everyone: Dankrad's background is amazing.

10:45:39 From  Justin Florentine  to  Everyone: Guillaume might be the only one off mute not speaking

10:45:43 From  Potuz  to  Everyone: does the EF buy mics in bulk?

10:45:47 From  Micah Zoltu  to  Everyone: Having a family dinner in the middle of an airstrip.

10:46:00 From  Mikhail Kalinin  to  Everyone: > does the EF buy mics in bulk? LOL

10:46:00 From  terence(prysmaticlabs)  to  Everyone: Wen micsDAO

10:46:01 From  Trent  to  Everyone: jgold is unmuted

10:46:53 From  Hsiao-Wei Wang  to  Everyone: Bird strike

10:47:49 From  stokes  to  Everyone: default is a random value

10:47:55 From  Micah Zoltu  to  Everyone: Majority clients have a longer delay than minority clients.

10:48:03 From  danny  to  Everyone: still the upper bound is how you game it

10:48:23 From  danny  to  Everyone: upper bound on the defaults

10:48:38 From  stokes  to  Everyone: yeah if any value is known it will be gamed

10:48:43 From  Micah Zoltu  to  Everyone: I concur with Adrian.

10:48:46 From  stokes  to  Everyone: which kind of suggests uniformity

10:51:40 From  Micah Zoltu  to  Everyone: I feel like I'm missing something.  Why would MEV boost going down result in an outage?

10:51:47 From  danny  to  Everyone: not going down

10:51:50 From  Micah Zoltu  to  Everyone: I thought the clients *always* built a fallback block?

10:51:57 From  danny  to  Everyone: if you already comit to the blinded blokck

10:52:01 From  stokes  to  Everyone: proposers would attempt to use it but then rugged by mev-boost network

10:52:03 From  danny  to  Everyone: you can't fallback locally anymore

10:52:03 From  Micah Zoltu  to  Everyone: Ah.

10:52:13 From  danny  to  Everyone: so it's a malicious relay  or a very very particular bug

10:53:12 From  danny  to  Everyone: gas limit elasticity

10:54:44 From  Chris Hager  to  Everyone: That kind of reputation and monitoring is basically the idea of the relay monitor: https://github.com/flashbots/mev-boost/issues/142

10:57:20 From  Paul Hauner  to  Everyone: It’s hard

10:57:21 From  Chris Hager  to  Everyone: the relay monitor 👆would also know about withholdings, but would be a trusted entity

11:00:56 From  danny  to  Everyone: more than 1/3 blocks missing over 32 or 64 blocks

11:01:15 From  stokes  to  Everyone: do we count orphans?

11:01:28 From  danny  to  Everyone: or 40% -- at lesat then you still have block elasticity to help with the gas limit

11:01:29 From  stokes  to  Everyone: otherwise a reorging attacker can corrupt things

11:01:49 From  Chris Hager  to  Everyone: mev-boost could disconnect from penalized relays, wouldn't need to be a BN change

11:02:21 From  Micah Zoltu  to  Everyone: I didn't realize proposers and relay wasn't bonded in The Merge version.  😢

11:02:41 From  stokes  to  Everyone: won't really have in-protocol bonding till in-proto PBS

11:02:43 From  Micah Zoltu  to  Everyone: I thought it was, which meant that it had some amount of sybil resistance and incentives to defend against this.

11:03:00 From  stokes  to  Everyone: hey can opt-in to be bonded,

11:03:05 From  stokes  to  Everyone: but it wouldn't be enshrined in any sense

11:03:20 From  stokes  to  Everyone: e.g. DA commitee for relays

11:03:27 From  Micah Zoltu  to  Everyone: We would need them to be bonded in a way that can be slashed for it to be effective I think.
