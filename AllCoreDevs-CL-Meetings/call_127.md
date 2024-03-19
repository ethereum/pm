# Consensus Layer Call 127

### Meeting Date/Time: Thursday 2024/2/8 at 14:00 UTC
### Meeting Duration: 1.5 hour  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/951) 
### [Audio/Video of the meeting](https://youtu.be/FLB61CpMB70) 
### Moderator: Danny Ryan
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
127.1  |**Dencun Testing:** Parithosh Jayanthi said the activation of the Dencun upgrade on the Holesky testnet on Wednesday, February 7 went smoothly. “There’s been nothing we’ve noticed at least on Holesky,” said Jayanthi. “We’ve passed the blob expiry window for Goerli so we ran a bunch of nodes and are doing a mixture of genesis sync, as well as checkpoint sync [tests].”
127.2  |**Dencun Testing** Terence Tsao mentioned that the fork transition block was missed during the Holesky upgrade. While “not a big deal,” Tsao said the incident led to an 11 second block delay for his node. He recommended that client teams double check to see if their implementations had somehow caused this delay during the upgrade.
127.3  |**Dencun Testing** “Sean” said that the Lighthouse team has implemented logic in their client related to node recovery in a scenario where the chain has not finalized blob transactions. In such a scenario, a node could recover by relying on a checkpoint sync from an unfinalized checkpoint. However, implementing this logic, Sean said, was more involved than his team had anticipated and encouraged CL client teams to reach out if they come across similar difficulties.
127.4  |**Dencun Testing** Nethermind developer Marcin Sobczak said that his team is continuing to investigate a potential bug in their client mentioned during last Thursday ACD call. Sobczak his team has started spamming the Goerli network with blob transactions and so far, have found no issues. He said that the tests on Goerli should wrap up in a few hours.
127.5  |**Dencun Mainnet Activation** Beiko mentioned that he had reached out to the teams behind the top 10 Ethereum rollups on L2Beat.com to evaluate their readiness for Dencun. “All the teams are pretty much in testing phases at various stages. I think teams will be ready on the L2 side to use 4844 on mainnet around early to mid-March,” said Beiko. “I don’t think we should block anything based on where L2 teams are at.”
127.6  |**Mainnet Missed Blocks Incident** Bloxroute Max Profit relay delivered 9 blocks to validators that failed to be added to the Ethereum blockchain. This was due to a bug in the relay that did not work to correctly demote the block builder responsible for submitting the faulty blocks. Bloxroute has since patched their relay and reimbursed validators for lost block rewards.
127.7  |**Electra Portmanteau** Ryan asked developers whether they supported a combined upgrade name of “Pectra” for Prague/Electra. Developers on the call did not appear to have a strong opinion about the portmanteau. Ryan moved on with the discussion about what code changes should be prioritized for Electra.
127.8  |**Electra SSZ**  ACDC #126, developers are considering the inclusion of five EIPs related to SSZ formatting. Sean from Lighthouse said that he would need to evaluate the code changes in more detail but initially from his perspective the code changes are “a good thing to have”. Another developer reportedly wrote in the Zoom chat that they would like to see the SSZ formatting changes bundled as one large change to the protocol as opposed to implemented piecemeal. Ryan recommended that client teams do more due diligence on understanding the SSZ changes proposed by Nimbus developer Etan Kissling and re-discuss the topic on the next ACDC call.
127.9  |**Electra SSZ**  ACDC #126, developers are considering the inclusion of five EIPs related to SSZ formatting. Sean from Lighthouse said that he would need to evaluate the code changes in more detail but initially from his perspective the code changes are “a good thing to have”. Another developer reportedly wrote in the Zoom chat that they would like to see the SSZ formatting changes bundled as one large change to the protocol as opposed to implemented piecemeal. Ryan recommended that client teams do more due diligence on understanding the SSZ changes proposed by Nimbus developer Etan Kissling and re-discuss the topic on the next ACDC call.

# Intro
**Danny**
* Okay. We should be live.  YouTube people, let us know if you cannot hear us. Well. You know you can't hear me. So anyway,  All core devs consensus layer call 127. This is issue 951 in repo. There is the link we have quite a bit to talk about.  
* I have a feeling that. We're going to have to again, keep continuing this conversation over the next couple of calls, but hopefully we can make some good progress today. generally on the agenda, we're going to go over to NAB. Anything we must discuss as well as some discussion around maintenance scheduling.  there was a what I would call,  pretty minor incident on main net, but one that might have, you know, significant things to talk about. 
* So I don't know if there's a. Post mortem out, but I do want to just give us room to talk about that in the event that there are critical things to discuss. Now, I'd like to keep that relatively independent of the discussion of EPBS, which would come a bit later. Then we'll talk about a lecture again. Maybe we're settling on a joint name, and have already. But let's talk about that briefly EIP 7549, which has been agreed to be included, has a bit just some, I think, minor design considerations that we want to escalate. 
* Then the conversation around,  various things, that may or may not go in the continued conversation, then open discussion. Okay. Let's go ahead and get started. On the Deneb, I believe we have forked another public test net. is there a general status update or any,  thing that we want to discuss in related to test nets and testing? 

# Deneb [5:39](https://youtu.be/FLB61CpMB70?t=339)
**Parithosh**
* Yeah. So we had the whole Sky Foxx yesterday and since, the fork went well, we we barely lost any participation rate, and it looks like we were getting blobs from quite early on besides that, there's been nothing we've noticed,  at least on whole sky. 
* And we've done, we've passed the blob expiry window for Goerli. So we ran a bunch of nodes and are doing a mixture of Genesis sync as well as checkpoint sync and all the checkpoint sync nodes, EL and KL, other than the archive ones, have already sync to head and the archive ones. We should have information within another day or so. 

**Terence**
* First. Notice that I'm not sure if anyone is watching, but,  the slot zero where the four transaction block. It's actually missed. So someone didn't send that block. And then the slot one was arrived, but it was arrived at my local node. It was 11 seconds later. So like, honestly,  this is probably not a big deal. 
* But like as a client team, it's probably worth checking whether this is your implementation that's,  causing the delay.  We are also checking the background to make sure,  present validator is okay under those scenario because I suspect maybe the for transaction may take like more than a few seconds here. 

**Danny**
* So yeah this is on. 

**Terence**
* Yeah this is on Holesky. Got it. 

**Danny**
* Any further comment or discussion on that point. Specifically Terence's. Okay.  when I'm curious, when you're thinking from Genesis, past the prune window. Is that? Do you have to bring in a piece of main net information that is within the prune window, or can you do so trustlessly. 

**Parithosh**
* Right now we're struggling to sync Genesis on Goerli to begin with, because I'm not sure there's that many Goerli archive nodes. 

**Danny**
* Okay. 

**Parithosh**
* So irrespective of block expiry. And the checkpoint segments. They work fine. Very cool. 

**Danny**
* Any other, discussion points for Denebin relation to testing test nets. 

**Sean**
* So we discussed this a few months ago, but. In a scenario where the chain hasn't finalized for the data availability period. The way to recover would be to checkpoint sync from an Unfinalized checkpoint. Right. And also that generally just be useful for like some sort of social recovery in a long period of non finalization. 

**Danny**
* By recover you mean be able to sync during that environment. You could still follow the head in that environment. 

**Sean**
* Yeah. Yeah. 

**Danny**
* Exactly. 

**Sean**
* So we've been working on like enabling this in lighthouse. And it was actually kind of tricky because  we look at like peers their finalized epoch and compared to our own.
* And we treat this as sort of like a virtual finalization. So we would just assume we were ahead of all our peers and it would stall our, sink on our nodes.  So I would just encourage other client teams to also look into this, because it was the type of thing that we thought should work until we really dug into it. 

**Danny**
* Right. So in the event of issue, don't just assume this is easy you know, running is something I may not, is there? any other any further comment or any, more color on why this is difficult. 

**Sean**
* For us specifically, it was because,  it was because of peering. Like, we treat the Unfinalized checkpoint as finalized. And this is good internally in that, like, you're sure to never reorg and whatnot, right?  but. Your view of the chain. I guess your view of like which peers are useful. That was the specific issue.  yeah. 

**Danny**
* I see. Do you end up reading finalized information from that state and using that for your period information? Was there a different trick? 

**Sean**
* No. We're using the essentially like the Unfinalized checkpoint. And we assume that our node is actually further ahead in sync because we're comparing that to other chains actual finalized checkpoint, which in this scenario would always be lower. So we end up sorting through all our peers and saying that they're all useless. 

**Danny**
* Yeah. What I'm saying is the workaround to then use the finalized information that's actually written in the checkpoint state, not the checkpoint state itself. 

**Sean**
* So now what what we're doing is we're making sure that, like, lighthouse is aware of, if it's in this particular mode. So it's aware of whether it was started up. With a non finalized checkpoint. And when it's comparing itself to peers, it'll take this into account. Instead look at like the head the head of the peer chains. 

**Danny**
* Such a protest. Did you have a comment? 

**Potuz**
* I know. I'll ask in the chat. It's technical. Yeah. 

**Danny**
* All right. Thanks, Sean. Anything else on this one? 

**Sean**
* That's about it. But if anyone runs into similar issues, feel free to reach out. 

**Danny**
* So other Deneb testing items. 

**Marcin**
* Yeah right now I'm spamming, Goerli network with block transactions and as far as I know, issues, but it's like, one third of experiments. So if there will be some issues, we'll see it in, few minutes, maybe half an hour from now. but yeah, as for everything, looks fine. 

**Danny**
* Great. Thank you. Any other testing related items. Okay. Great work. I believe, as has been broadly discussed over the last handful of calls and much more concretely discussed on the last act, there's an intention to talk about and pick a mainnet date then.

# Mainnet schedule [13:28](https://youtu.be/FLB61CpMB70?t=808)
 
**Tim**
* Yes. So Yeah, my feeling is on the EL side. teams are generally pretty ready,  to both pick a date and then start putting out releases for it.  I think there's not too much, strong opinions about what the date should be. And, like, obviously, getting CL folks's perspectives on that, is valuable.  
* And, yeah, I mean, if I can share my screen, I have a bunch of potential dates, like the next, month ish.  So assuming that teams, you know, are ready to put out a release in the next week or so,  I think these all make sense. 
* Generally, we probably want like 2 or 3 weeks between the announcement for main net and then the actual fork. So, we should pick a date that, like, Yeah. Teams, like, we should figure out when teams are all comfortable having a release.  and then pick a date. 
* That's a couple of weeks after that.  and then. Yeah, all the times, on this sheet, I'll put this in the chat. But all of these are like the, epoch, history accumulator boundaries.  and they're all sort of mid week, so between Tuesday and Thursday.  
* So, yeah, curious to hear from client teams if they have any preference on or maybe. Yeah, it makes sense to hear from client teams like when they could have like a mainnet release out. And then based on that, maybe we can pick a date. Yeah. 

**Danny**
* So maybe, maybe a bit more concrete. Tim, when speaking with Execution Layer Teams is everyone we. 

**Tim**
* Could have releases out next week. Yeah. 

**Danny**
* Meaning by Friday of next week by sometime next week. 

**Tim**
* So I think like the earliest that from the EL side we could fork would be the 2728 which would feel. Yeah. So okay, so Marius is saying they can get one out this week. So like I think yeah, the most aggressive timeline on the EL side is really,  is really like the last week of February.  
* And Terence has a question in the chat. So, hearing about L2 testing. So I reached out to all the teams that were in like the top ten ish on L2 beats this week, I think, pretty much all of them got back to me, but no one had any major issues. 
* All the teams are pretty much in testing phases at various stages. The I think teams are like will be ready on the L2 side to use for it 4844 main net around early to mid March.  Yeah. So,  that's that's basically where things, yeah. Where things are at from L2. 
* So I don't think we should block anything based on where L2 teams are at. And I think from the EL side, we can have people start releasing this week and then potentially the releases coming out next week for the other teams and be ready at the earliest, end of February. 

**Danny**
* Real quick. Your doc does not have open access. 

**Tim**
* Just changed the link. 

**Danny**
* Okay, cool. 

**Tim**
* Yeah, I'll post an actual screenshot in the chat too. 

**Danny**
* I think it's understood.  Terrence. 

**Terence**
* Yeah. So from Prism side, we surveyed the question internally on when just like when when we will be ready to do this major release. So we still like two weeks because we still have to do some general cleaning up. And we want to test block file further. So I don't think we'll be ready to cut our release next week. 

**Danny**
* But would be by Wednesday Thursday of the following. 

**Terence**
* Most likely. Yes. Two weeks will. Yes, two weeks will be better. 

**Danny**
* Any other perspective input on. Where you stand on where consensus teams stand on being able to release. 

**Sean**
* I think for Lighthouse, probably same sort of timeline like Wednesday, Thursday, the week after next. 

**Danny**
* Okay. On the consensus layer, is anybody, anybody not able to hit that target?  which would put us at. You know, a main net blog posts on that Friday of the following week at the latest. If we agreed on that target, which then we would have to pick a date. That. Puts us in a good time frame from there. 

**Danny**
* Yeah. Let's start in perspective. Lodestar. Nimbus. 

**Phil Ngo**
* Yeah, we can meet those timelines. For Lodestar. Thanks. 

**Tim**
* So I guess then the two dates that are like most reasonable is either Thursday, March 7th, which would be like a straight two weeks after the releases and or Tuesday, March 12th, which is to, I don't know, two weeks plus like 3 or 4 days, two weeks plus a weekend.  after the releases.  yeah. I don't know if there's a strong. 
* Okay, so there's a debate in the chats between 7 and 12. 

**Stokes**
* Is there a good reason not to do it as quickly as possible? 

**Tim**
* I think as long as we have two weeks. Is from the blog posts. That's like reasonable. Yeah. 

**Danny**
* What's the shortest we've done on mainnet before? Tim, do you know? 

**Tim**
* The big we had one. Yeah, we had one shorter than that, but that was not great. 

**Danny**
* Okay. What's the shortest you've done when we weren't an emergency? 

**Tim**
* Probably on the. I'd have to check.  but probably on the order of like. Yeah, 2 or 3 weeks.  So we can do if people feel uncomfortable with that, we can do like the week of March. We can do like the 13th or the 14th, which is, like closer to a full three weeks if. From the chat that seems to be, the main. You have to bring feedback. So the 12th? 

* The 12th is Tuesday. It's Tuesday, Wednesday, Thursday of the week of the 12th. Each have a slot that would work. So we can, if we want to do like closer to like a proper three weeks then some, you know, doing like the 13th or something is like. Three weeks. 

**Danny**
* Okay. I think given the given the constraints of consensus teams wanting or needing two weeks from now,  I think it's reasonable to land on. Yeah. 13.  You know, like, if there's, if there's I'd prefer about 13 over 14, 15 just given the some room on the post side from the weekend. 

**Tim**
* Yeah. Middle? Yeah. Middle of the week is nice.  And then obviously if client teams have like, client teams can start putting out releases as soon as they're ready. Today, basically, if as long as we have the date. So and then we'll have the blog post out, in about two weeks once we have all the client releases. Okay, so I'll post the information in the chat. 

**Danny**
* Yeah. What are we saying? The actual like deadline for client releases is okay. 

**Tim**
* Absolute latest. Is this called two weeks from now? 


**Tim**
* Yeah. So that's two weeks. Okay. 

**Danny**
* Okay. Any further comments or thoughts on this? Okay, Tim, should we kind of circulate that information in your discord? yes. 

**Tim**
* I'll put it on discord and open some PRs on the specs repo and, tweet about it. Make it properly official. 

**Danny**
* Great. Congratulations. Very exciting. Okay, ike I said, I don't believe,  there's been a postmortem on the officer relay. Invalid block incident. But I think we know relatively what happened. Is there any one? Do people want to surface details here? two. Is is there anything to do today? 
* Obviously other things that might come in the pipeline are very valid and worth discussion, but, you know, are there particular tests that need to be added or, security, things that need to be layered in or really, you know, what's the is there anything to patch today? 

**Potuz**
* That what you mean by tests? What do you mean by things that we can do right now? Yeah, yeah. 

**Danny**
* Just to the surface. Something in hive should this. 

**Potuz**
* Yeah, there's an immediate one. We can just change our circuit breaker so that if we see invalid blocks, we start, we fall back to local production. We are only doing this on missed blocks on an off missed blocks in an epoch. But perhaps we can be much more aggressive with invalid blocks. 

**Danny**
* Is no one circuit breaking as invalid as though invalid is missed or just there weren't enough. 

**Potuz**
* We are all circuit breaking on missed blocks and we are circuit breaking. An invalid block only counts as missed. What I'm saying is that we can add another test that if it's invalid, we just increase the frequency. 

**Dankrad Feist**
* Right. But I mean, that's also like that potentially allows for DDoS attacks, right? If you give a highway to invalid blocks. What do you mean? Basically, turn to local production. 

**Danny**
* Right. But if you can get all of the quote, honest players to fall back to local production with a couple of invalid blocks, then you might be able to dominate the MeV market more easily. So there's certainly a trade off between those. The ability to turn this thing off. or how easy it is to turn this thing off. 

**Mikeneuder**
* Yeah. You could. Sean just said this, but yeah, if you check the proposer signature and that it was invalid, those two things would be pretty strong signal. Then the only person who could send an invalid block would be like a proposer intentionally. 

**Danny**
* Oh, that's what it means for 20% of the network. And you can turn it off with two blocks for everyone. 

**Dankrad Feist**
* Any builder, any builder can do it. Any build I can intentionally just trivially generate and they just have to be the highest bidder. So like I just have to take whatever number, the minimum number of invalid blocks after which return offers. 

**Potuz**
* But I still don't see what's really the the attack here into making people fall back to local execution. I'd be happy if builders didn't exist even. 

**Dankrad Feist**
* Well but okay, so but I as a poor for example, let's say I'm a poor having 20% of blocks and I can disable, like Meth boost for everyone else by sending three invalid blocks. Like the cost of those might be low enough that my 20% blocks that afterwards I get so much MeV out out of it that it's worth it for me.
* So it is an it is an attack on all the other validators who follow this rule. 

**Mikeneuder**
* Yeah. And also, you don't have to circuit break yourself, right? Like that pool can still keep using that MeV boost. 

**Dankrad Feist**
* Exactly. There's no enforcement for the circuit breaking. It's a local thing. So it's basically a disadvantage for you to have two aggressive circuit breaking. So like, a rational people just won't do it. 

**Mikeneuder**
* Yep. Agreed. 

**Sean**
 * So usually when we add something like this though, we make it configurable. So like it'd be hard to specifically.  like, know that you're going to be able to get some proportion of the network offline or even like certain proposers offline. And it's also we wouldn't have to agree across clients on like, let's do this after one bad block. 

**Danny**
* Yeah. Then again, you know, set defaults are strong. And, the more that you send, the more you'd see the network. Switching their behavior. 
* So,yeah, I, I agree with you, but I also agree that, like, depending on the level of the attacker, it can still be a profitable avenue and they can kind of ratchet it up. I guess one question that's worth escalating is,  obviously a lot of the kind of MeV boost MeV monitoring tools are extremely aware of builders and relays. 
* You know, they see this information surfaced in block explorers and all sorts of analysis. you could imagine circuit breaking more specifically on actors, but the protocol doesn't know about the actors. So is it actually is there actually a reasonable path to circuit break on a particular builder or circuit break on a particular relay?  or is that to kind of. Heuristic in trying to decide who those players are. Without a native integration. L1 integration. 

**Potuz**
* Well, you could add some logic to MeV boost. Arguably, everyone is using essentially the same software and you could add some logic itself to it. MeV boost to to ban particular relays. 

**Danny**
* Right. But do I do I know that the relay was bad? If you're interacting with the relay, you probably know it's bad. But if you're interacting with the relay and it gives you something invalid, then do I know? Like in the entire network. Know that. So I guess. 

**Dankrad Feist**
* Like currently we don't have a proof that a particular relay created a block. Right? Because just because it goes to two that relays address someone else could fake that. 

**Danny**
* It's presumably authentic. You know, talking with them is authenticated on some level. So you could share that as a proof. Yeah. Yes. 

**Dankrad Feist**
* Right. But we don't currently have that. Right okay. 

**Sean**
Also, bids are signed, right? Aren't they signed by builders? Are they signed by relays? 

**Mikeneuder**
* They're signed by the builder. But the relay verifies it. And that that doesn't go on chain like that. That's just from the relay to verify the identity of the builder that sent it. 

**Danny**
* Right. 

**Sean**
* So we would have to like broadcast bids or something. 

**Potuz**
* Yeah. That's what Francesca's been suggesting. 

**Danny**
* Shatter these things. Yeah. Like if there were a if there were an optional gossip channel, I could I could drop this information to the network. 

**Mikeneuder**
* Yeah, this this kind of sounds like the optimistic V3 version, which we talked about a long time ago, but the idea was like, you have a gossip channel for the headers and you have more observability there.  I think the main issue here is that, like in terms of latency, the proposers probably won't get their bids from there because it's just a lot slower than directly connecting to the the relay builder. 

**Danny**
* Oh, right. I'm not saying I'm not saying utilize that channel for selecting the bid. I'm saying I, as the person that interacts with the relay, can drop information about my interaction into such a channel so that people can act upon that. You know, if I see that who you interact with and I see an invalid block, my local setup could say, oh, I don't want to interact with that entity anymore. Yeah. 

**Mikeneuder**
* That's fair. 

**Danny**
* Okay. I don't mean to say this group should decide. You know what should happen. I just wanted to kind of go through the exercise of deciding if something can happen. That does not require protocol changes to at least contextualize what people might be able to do soon, or talk about and follow up conversations.  Is there anything else that we want to discuss around this incident today? 

**Mikeneuder**
* I guess it's worth mentioning that this was a bug in. Like the non buggy version of optimistic relaying wouldn't would have only resulted in one missed slot. So it's not like the optimistic model allows for this. It was just like there was a bug in the relay end. So I don't see it as like fundamentally changing anything. 

**Danny**
* And was the relay is the was the relay bonded and is the relay doing something with respect to that bond? 

**Mikeneuder**
* Right? Yeah. So the builders, the builders are bonded with the relay.  in this case, since it was the relays fault, they refunded the proposers directly. Then from blocks route was on this Twitter spaces yesterday talking about it. So yeah there that's already taken care of in terms of like the the restitution I guess. 

**Danny**
* Which is kind of one of the one of the attempted things to happen with automatic relay is to surface. Quote, at least via, trust model. Unconditional payment. Yeah. 

**Mikeneuder**
* Yeah, exactly. I mean, it's not really unconditional because you have to trust that the relay will refund you. And I think that's that's the issue that.

**Danny**
* People have. It's trust that they'll run you and otherwise the network probably the assumption is people would then not use that relay anymore because the trust. Yeah. Exactly. 

**Mikeneuder**
* Like if blocks are out chose not to refund the like one ETH worth of missed slots then like the I think they lose a lot of credibility in terms of the validators connecting to them. 

**Danny**
* Okay. Anything else here? We will have some discussion around, current app designs coming up in the Electra discussion. 
* Okay is anyone that works kind of in the specs landscape? Interested in specing? What a gossip channel around groups of this kind of stuff would would work on or is or how that would work? Or is that. Not something that people want to dig into right now. 

**Potuz**
* I'd be strongly against it, because if we are going to go with a protocol change that does something like this is already covered in Epbs. This is literally covered in Epbs. 

**Danny**
* Right. I guess my argument would be, even if we're going to ship Epbs as the next big as the next thing in the next fork we're still talking about 12 months. 

**Dankrad Feist**
* I don't think we've made a decision on Epbs though, right? Like, I mean, we're not. 

**Danny**
* That was a very conditional. 

**Dankrad Feist**
* This depends on actually having a viable construction. So I think like, I don't think we should presume anything at this point. I agree. 

**Potuz**
* It's just that my point would be that having something that pollutes with the Epbs, I would much rather discuss Epbs. 

**Danny**
* All right. And let's discuss it in a couple of points. 

**Dankrad Feist**
* Why does it pollute it? 

**Danny**
* This it continues to. The Band-Aids would would, the argument is the Band-Aids would make it such that, members can continue to live another day instead of actually working on kind of a native solution. 

**Dankrad Feist**
* No, but that's a terrible argument. 

**Danny**
* I think the argument is not terrible. If you consider complexity analysis, like if it's 50% as complex just to patch boosts, right.  then do Epbs rate, then maybe then we're talking about it. If it's 1% of the complexity, then that's a different world. 
* I do want to table this. I do want to talk about a couple of things around Elektra and then get into the ipbes discussion,  in a couple of points. Okay. There is a desire to figure out what the joint name of Elektra is. Elektra and Prague. 
* It seems like some believe it's already been discussed and named as Pectra. I believe I've seen this in testing and a couple of other places. Is there. I don't. This is the last thing in the world that I want to be trying to use our decision making power on, but. Does anybody want to make a case that's not Pectra? Okay. I'm going to take that as some sort of decision or desire not to talk about this and we will continue forward. Great. 
* Okay based on some discussions with that then surfaced into. And others that then surfaced into a comment on 7549 there was a desire to kind of like do seven, five, four, nine all the way and be able to, more unify attestations on chain than, keeping the kind of vestigial. 
* Committee index, but in a different place of the attestation. It seems like that is generally what some of the designers want to do. But Mikhail, can you give us some more context and some of the trade offs here? 

**Mikhail**
* Thanks, Danny. So basically, this is the,  one more step on top of, what was originally proposed by 7549.  and, yeah, as as Danny said, it allows to pack, attestations and more tightly on chain and on chain structures. And, what's nice about it is that, considering the current validator set size, we can increase the block space in terms of attestations, up to four times. 
* So instead of, currently we, can keep,  attestations for two slots if they're kind of ideally aggregated. This change would allow to do this for eight, slots instead of, two, without increasing the block size in bytes.  
* This is great. at, and, yeah, if, attestations were, kind of like aggregated really well, this change will allow us to reduce the size of a block. Yeah. Keeping the same information, the same number of votes in it. 
* So basically, what's, how to achieve this?  is, turn the,  aggregation bits into a list of, bit lists. So basically, every item of this list will represent the bit list of, each committee of a yeah, of, committee. And also the other change we would need here is to turn committee index into committee bits, of the same size, which is 64 bits. 
* And, yeah, this is going to be a bit vector, which will have bits of yeah, of the committees that are included into the aggregation bits list. So basically it's quite straightforward change. And we can use the reuse the same structure for  on chain aggregates,  where many committees, will be in one attestation obviously signature will be aggregated.

* Yeah. for all of those committees and also it can be used on the network where, just one committee will be, in the attestation, in this, attestation structure, which, yeah, is kind of required by the network, by the aggregation algorithm that we currently have,  relatively small changes to the spec. will have to do some, you know,  will have to go over all committees, when processing the attestation. 
* The, Devlin made a great point about, like, complexity of testers slashing messages. And this is really, one of the,  kind of, complexities here. So it basically,  this tight aggregation would mean that, if we want to create a tester slash message out of on chain data, which are tightly packed, it will mean that we'll have to say if there is just a slot yeah, a committee which is, which will have a size of a slot of, you know, whether is that assigned to a slot. So we'll have to keep,  all those in one, in the indexes of all those while there is in one a tester slash message.  there is a bit of, analysis, linked into, into the comment.   
* Yeah. So we'll have an increase there. but if we have like this. Yeah. This more, kind of, more of a problem for the a tester sessions where slash just one or a couple of validators, they will be, they can be much bigger than what we have now because we have currently we have a,  quite good granularity, protestations, but for kind of like, mass slashing events, this will not be, too bad. 
* Yeah. And, we'll probably have to do something, at least to reduce the max tester slashings to one. So you can read about, in the comments about this analysis and about the proposed changes.   let's have another,  quickly. Really quickly and. Yeah. 

**Danny**
* Yeah. In the proposed changes, you're suggesting reducing the number of stations to eight, given that you can handle a lot in these bit less does that, but that that reduces the diversity of accusations that can make it on chain. Do you see an issue in the event that there's high asynchrony or forking, such that you can only capture kind of eight different views, or is that do you think sufficient? 

**Mikhail**
* Yeah, I think I think, yeah, it's a good point. I think it's pretty much sufficient. I don't think it changes the status quo in that regard. I don't see how it differs to what we have today. You know, it's. Yeah. It might be even better because we increased the capacity of one block so it can accommodate more votes in it. 

**Danny**
* Well, it's a trade off because you increase the capacity, but you decrease the diversity of that capacity, the potential diversity, that capacity, which I it seems like is the proper trade off, is a reasonable trade off. * But one to consider at least because you could do another thing right. You could have like a more sophisticated counter here, that you could have two counters where you have you can have many attestations that have a small number of bit lists, or you could have fewer attestations that have a large number of bit of list. But then you're adding, you're adding certainly more complexity to get that trade off space between the two. 

**Mikhail**
* Right. But if you have many attestations from different slots. Yeah, that that can be right. Right. So it can be. 

**Danny**
* Right. So kind of how I thought about it. 

**Mikhail**
* Reduce. Yeah. 

**Danny**
* Yeah. I thought of it before. It was like you could have essentially two counters.  but then. It's certainly more complexity. 

**Mikhail**
* Yeah, I think overall, overall, I think this anyway, this change requires more deep analysis. And this is basically a temperature check. And, yeah, if there is a desire, willingness of fine depth to extend this EIP, then we can, you know,  invest more time in analyzing. 
* The tradeoffs of this solution. But I think, yeah, this change is what basically what actually the original proposal, was supposed to enable. Yeah and not doing it. I'm not exploring this space. Yeah, I think it's. 

**Danny**
* Yeah. I think something in this direction, makes a lot of sense. If we're going to be cleaning up the meta index. And at least the temperature check on everyone in the PR is good so far. Does anybody have any additional comments? Okay.  I would say you should go for the more cleaned up version. 

**Mikhail**
* Cool. So I'll do some analysis and try to come up to, you know. spec changes and. Yeah. One other question I had is probably that we can have it as a separate EIP, but, we have it in in the next hard fork. 
* I don't see it makes sense to have it as a separate EIP so it can be an,  going in this EIP. But yeah, if we consider it for a later inclusion, it could be separate EIP. 

**Danny**
* Yeah, it seems like the relative complexity is marginal on top of what was already there, so I'd hope not to do it in a two step fashion, but open discussion. Okay, great. we're going to continue the conversation around what to include or not include in a electra.  

# inclusion lists - EIP 7547 [47:55](https://youtu.be/FLB61CpMB70?t=2875)
**Danny**
* I believe two weeks ago we did not have our full conversation around SSK or at least,  give enough time for discussion. Ethan, is there anything additional you want to bring to this group?  or do people have questions for you, Ethan? Again, noting that a lot of this complexity is on the execution layer.  
* And so I do think that a decision point, certainly. Because as I say, we don't want to prioritize this, but I think a lot of the decision point on on the complexity ends up on the other side of this equation. but nonetheless says. 

**Etan**
* From my side. I don't think I need to add some more explanations from last week. I went through all of them, right?  I think on the consensus side, the stable container one EIP 7495  may also be useful to,  have forward compatible generalized index for execution payload beacon state and beacon block just because those structures keep changing. 
* And I think if we can make them forward compatible, it would help decentralized staking pool such as rocket pool to,  require fewer engineering to keep up to date with the various forks. 

**Danny**
* Right and to remove a piece that that might need to be governed.  Yeah engineering is one thing. And then also figuring out if and when and how. Yeah

**Etan**
* Security review and stuff for sure. 

**Danny**
* Yeah. What is the temperature check on doing? Kind of a one time change on these data structures to make them forward compatible. Forwardly stable. 

**Etan**
* For SSZ library. It's quite easy, by the way. It's not a big deal. 

**Danny**
* All right. Does adding that kind of one time break in the structure of the tree, is that a huge engineering complexity? Does anybody want to weigh in on that? 

**Etan**
* It's only for new block though, like From the Fork. You just have a new block type. And the difference is that those blocks you can. That you can then use the same parser also for future blocks. And I'm not sure if everyone reviewed this already. 

**Danny**
* Right. Anybody want to give any signal in one way or the other? I pretty much zero temperature check on this. well, okay. 

**Sean**
* It seems like a good thing to have.  I don't I haven't personally looked into this, so I don't really know how complicated it is. I know people are generally wary of, like, new SSD types because, like, the ones we have are super well tested, but. It seems like a good thing to have. 

**Radek**
* In terms of engineering work. Changing fast SSZ library is always a pain. But, you know,  if it's not too large of a change, then I guess we can handle it. 

**Danny**
* Yeah, Casey's servicing that. He'd rather wait until this was bundled with more SSZ changes. Okay. Is this something that teams want to do a little bit of diligence on and we can talk about again in two weeks? 
* Okay, I will pop that on the next agenda and,  pop a message into discord saying, if you want to take a look at this to have a more in-depth conversation, now's the time. Okay.  any other SSZ discussions? Great.

# peerDAS [52:55](https://youtu.be/FLB61CpMB70?t=3175)

**Potuz**
* All right. So. I don't know how to start this discussion, actually. So I think the problem that we've seen on main net is not like a light problem or a minor problem. It's not the issue that nine blocks were missing or that validators like got refunded or not by relay. 
* The problem is that we need to trust the relay for this we don't even know what the check was. We don't even know what the fix was. This closed source software and it's happening. 
* This development is happening on a black box and and these are five players that are relaying all of our blocks, or 90% of our blocks and ten players maxim that are building these blocks. 
* I think what we need to do is to decide that this is a priority that we should not have in Ethereum at Trusted Player, making these decisions with a closed source software, being the one that is responsible for paying or not, for refunding validators, for even deciding which transactions are censored or not. 
* Once we make this a priority, then we can discuss whether or not there are viable designs for Epbs. Certainly we're not going to be discussing this in a meeting like today. I maintain that we have a viable solution for Vpbs that could be implemented in less than a year's time, and I am willing to defend this in an actual meeting with the community. 
* And this thing should not be discussed in small meetings where EF research has some point of view, some biased point of view for EF research, some other client deaths like we are on Prism have another biases.  
* And we're focusing on different kinds of design. We should have something like the interop that is going to happen soon in May, and we can, come up with a design there, decide whether or not the current design works or not. but this what I'm asking is for this to be prioritized. 
* And if it's the scope of this fork is kept for 2024, then this cannot be included. But, if the scope of this fork or the next one is maintained for 2025, then I would ask that we use the time to discuss these things seriously and to allow the time for the interop in May and, come up with a compromise to ship this by 2025. 

**Danny**
* Thank you. I have a quick question. Can you. Explain in a theoretically design. What would have gone differently in this incident? 

**Potuz**
* There are many there minor things that are actually different. But, some of them are the following. So the blocks would not have been missed. 
* The blocks would have been empty. The consensus part of the block would have been included in exclusion lists. In those consensus parts would have been included and enforced in the next blocks. 
* No matter how many payloads were missing in the middle, payment would have been immediate, unconditional, and for any amount and not trusted by the relay. 
* And finally the block the payloads themselves would have been signed, so I would have gotten my value by the builder assigned. Yeah, exactly. The payload itself would have been signed by an entity that is in protocol, and validators can actually now they themselves decide whether or not they have a way to ban them or I mean, each client could them, they say, decide if I'm going to, ban those builders or not, instead of like. 

**Danny**
* How to interact with them on an economic level. Right? Much more transparent. 

**Potuz**
* That is building the block sign set, then that entity is responsible for the block. Currently, the validator itself is responsible for something that is not producing. 
* So even if a builder decides to go with a relay instead of opening itself an Http point. So the validators ask for the builder directly for the header even if possible, as the builder decides to use a relay, whomever is building the block will be signing them and we can ban them. We can react to them, which is not something that the validators were allowed to do in this event. 

**Danny**
* Sure. Just real quick. Stokes does note that, as we previously discussed, you could potentially map some of this transparency into a gossip channel because of the way signatures work today.

**Potuz**
* Right. And we can we can continue adding patches. Can continue adding small patches and small patches and small patches instead of actually dealing with the issue, which is relays are trusted players. Let's make them trustless. 

**Danny**
* Thank you. so we got a few hands up. Terrence. 

**Terence**
* I just wanted to add on top to that. Right. So today epbs is one solution to the problem. But the fundamental problem is that like today, the builder API is not like it's basically not like, incentive aligned with the rest of the protocol. Right? 
* Because you have literally 90% of the block that's relaying outside of the protocol but the protocol does not have enforcement on that. 
* Right. And there are two factors, right. The first factor is basically cost, right  because we are spending tons of money a year there doing this work, but they have no way to monetize it. 
* And the second factor is also the schedule, right. For example, when the coin today when how so how often  when the client release already and then we look at each other and then we're like, well, we still have to wait for boots, we still have to wait for boots relay. So we definitely adds a lot more complexity to, to basically, the it adds a lot more complexity to the process of the protocol. And then. Yeah. So basically I think we need to do something here. 

**Danny**
* Got it, Sean. 

**Sean**
 * Yeah. So the I think the idea of separating the consensus information from, like, the incentives is it generally makes sense. Specifically though, like, I feel like a lot of a lot of the problems could be solved without as extreme a solution as bringing builders in protocol. 
 * It's like, maybe that is good, maybe that is the end state. But like for example, guaranteed validator payments, like could you do that via using inclusion lists like in the current inclusion list designs, you just like require the builder to also include with their bid. An inclusion list transaction,  that has the payment.  
 * Then the other thing people have been mentioning is like just gossiping bids, I think would be valuable, and we could pretty easily implement some sort of tracking with like builder signatures. Builder publishes. But. That's it. That's it from me. 

**Dankrad Feist**
* Sorry. Did you say me? Yes Sorry, I didn't hear.  yeah. So I think, um. So I'm, I'm not against Kpbs, but overall I think like realistically, all Kpbs constructions are going to be quite major protocol changes. So the potential tech that that we're getting from these, if we don't implement a good solution, 
* If we find out later that it has major flaws or we come up with a much better one is actually way bigger than fixing fixing a few things around, methods, which doesn't actually involve like core protocol changes at all. * So I think I would be very careful. Like, I think like my feeling is that we are not there at the moment,  specifically with the constructions that I know of that have major flaws in terms of not properly protecting builders from being exploited in like balancing attacks and things like that. 
* This is actually a huge concern I have about them. And I think like before those are fixed, I feel like it's not really worth implementing them because to me, the trust like relays have two kinds of trust. 
* They have the trust by the validator Sso you have to trust the relays.  And I think that is minor because again, like, we can easily like blacklist them if like a relay misbehaves.  
* And like for, for example, if said relay, I don't know well whoever it was like didn't pay out those validators then I think lots of validators would not say, well, I mean, that sounds terrible. 
* I'm not going to use them anymore. So, um. This is a minor part of the trust. A much bigger trust problem is that relays can exploit builders by like analyzing their strategy, stealing the move, and so on. 
* And Like, if we allow  validators to exploit exploit builders, then that part is actually not solved at all. And we will actually continue having relays because builders will still want that, because they can otherwise be exploited and are not willing to include their high MeV transactions. And so then in the end, we haven't fixed anything at all. We will still have the relays and we will still have that problem. 

**Potuz**
* Yeah. So I think I know what attack Dankrad is referring to on, which is something that is not guaranteed on by the CDC sort of like the science. Yeah. I'm not I'm not willing to enter into like a technical discussion of what is a good design of or what's not. 
* But I do want to say that I would argue against this being a large protocol change. If you look at every design that we have, they all will have the same set of ingredients. So this is not going to change whether or not you go with BTC or another authorization. 
* All of them more or less rely on the same sort of like two slots. Approach two reveals two rounds of voting, some one two rounds of attestation in one way or another. So they're all more or less the same. 
* And we are already discussing there were serious proposals of having inclusion lists and maxev for the current fork, even scoped for 2024. And those are the largest changes from the point of view of the CL side. The multi. 

**Danny**
* Component you don't think is is like a huge engineering change. No. 

**Potuz**
* So no actually not I'm not from the CL side. Payload validation changes a lot because of the inclusion list. But this is already part of inclusion list, the part that the changes that are actually on for choice, for the CL on the implementation side are the minor part I am actually already implementing for Prism. 
* The one design of Apbs and Epbs alone is much simpler than the rest, so adding Mactcp is the most costly one, which is the one that I'm delaying for the end of the implementation. 

**Danny**
* Okay, so, my intuition here is like getting into timing and fundamental data structures of having kind of this two part data structure would be a massive engineering dhange. But but you you say otherwise. That is. No. 

**Potuz**
* So adding changes that are that are poor choice are typically not that complicated to implement changes. Some processing are the things that are most complicated to implement. It's true that it's not a light change and it's not something that is going to happen this year, certainly. 
* But I claim that the biggest part of the complexity of implementing Epbs comes from massive changes and inclusion lists. I mean, if we go with a, with a bonded, in Protocol Builder, which is, state. 

**Danny**
* Okay. So there has been a lot of design and research and discussion over the past more than two years on this.  and you have something of a spec that you're working off of and a prototype to demonstrates your level of complexity there are the last. 
* Whenever I see this opened up, there's a lot of questions like, what are we even optimizing? What is the right end goal of this? And it seems like there's a lot of varying opinions on that. And so the decision to include. this first becomes the decision to figure out what is the design.  
* And I guess, are you making the case that over the next few months figuring out if and what? The consensus design is on here. It should be prioritized. Are you making the case that. 

**Potuz**
* Yeah. So my case has been always the same on these meetings in the last few weeks. But I think we should prioritize in deciding what's the scope for the current focus. 
* If the scope for the current focus is 2024, then I don't argue anything and I'll argue against any big change. And I will hope that we plan something on the interop in May for 2025.
* If the scope is 2025, then I would argue that we need to consider Epbs for the next fork. And either way, I would want to have by the time of the interrupt, some designs so that we go there and we fix one particular design. 

**Danny**
* During daylight and there's another and that's what that's what I was going to argue is,  if there is a sense of either urgency or a sense of the ability to actually hone in on design at this point,  you know, regardless of the electric conversations that happen over the next. 
* However many weeks there can be kind of a parallel thread that attempts to in on this design, with maybe some breakout calls and hone in on this design as we meet in person in May. 
* You know, I don't think that we can an so that's my that's my big question is like do are we at that point I believe you believe we're at that point that we can we can have like a very productive, three months to kind of hone in on on this. is that the general feeling or is that is the feeling that there are many people from, or at least a couple people from various teams are willing to be a part of that conversation to hone in on design. 
* Who is the next logical step to have the breakout call about this? To at least begin to answer the question of whether people are willing to be putting a lot of effort into this, or even moderate and consistent effort over the next many months. 
* Okay, I see some thumbs up. I see some comments. It seems like at least we'll have five people on the breakout call. Okay. We'll. Tim do we usually schedule breakout call times on the call, or do we circulate something async? 

**Tim**
* Let's try to do it. Let's try to do it in the chat. 

**Danny**
* Okay. 

**Tim**
* 14 UTC is usually a good time, but yeah. 

**Danny**
* Ether clock. Yeah.  okay. Cool. Let's, let's bounce some times around on the chat, see if that we can get on a call.  you know, again, R&D call that's trying to bring together the threads or at least,  bring together. 
* The attempts to bring together the threads. Very cool. Thank you. Thank you everyone for that discussion. 
* Let's move on to the next thing. so I'll just to be frank, my read after the call two weeks ago was, inclusion lists. We're going to the general consensus was was to table.  my read on that was challenged by a number of folks, and said, no, there's still discussion to be had and not just from the authors of inclusion lists, but from a number of folks. 
* So it is back on the agenda and Mike has had some. I think very illuminating, especially the spec change overview to help us understand the complexity. Mike, do you want to reintroduce this topic? 

# unconditional inclusion on ETH research [1:10:00](https://youtu.be/FLB61CpMB70?t=4226)
**Mikeneuder**
* Yeah, sure. Thanks, Teddy.  I guess I'll post two links in the chat. the first is this unconditional inclusion, this post on ETH research. And then the second is the one Danny mentioned, which is this, overview. And, yeah, I guess the the second doc, the first doc is kind of going through this new design and,  kind of discussing the relationship with the post and kind of like bringing back some of these, these designs that we've been hashing.  
* I think actually we're kind of converging on something that, that we're all happy with. And so I started kind of just taking a look at the spec, which is that second doc,  in general. It seems to me like the goal of that doc was, rather than trying to, like, iron out each of the kind of individual points fully more to kind of scope what the changes in the spec would look like, which parts of the spec it would touch. 
* So both on the consensus layer side and the state transition function for the execution layer and in the engine API. Just kind of defining the interface between the two. So yeah, I guess thanks to all the, the members, most of them in this call who helped kind of scope that out and review those PRs. 
* But  yeah, I think in general trying to convey the message that it's doesn't have to be a massive change and that it could be really beneficial to include it in electrode from both the timing perspective of like that. Censorship could change dramatically over the next months and weeks.  there's one kind of one builder, one neutral builder that we depend on to include, you know, a certain subset of transactions.

* And that could change very quickly. And also just getting some version of censorship resistance in prod and like starting to collect data on its usage. And you know, I think of, I think of censorship resistance as like this defense in depth thing where. 
* There might be. This might not be the end game, but like some of these farther out research ideas like multiplicity and, you know, they could all kind of synergize well with inclusion lists. And yeah, I guess in general it feels worth worth trying something rather than letting it go go longer with the current censorship, that we're seeing on main net now. 
* So yeah, I guess that's the pitch. That's the the reason I wanted to get the spec doc out there. I think, have talked to a number of different client teams, both on the execution and consensus side,  just to kind of get their take. And, and generally people seem keen to learn more and, and happy to engage. 
* So I'm not sure exactly. I think maybe like a breakout call for inclusion specifically could also make sense, So if that feels like a reasonable next step, we could bundle it with the epb's talk. I mean, I definitely think there's a lot of overlap in terms of the themes that will be discussed there. 
* But, I also think having its own talk could be useful potentially. So yeah thanks for the time. I think I'll leave it there unless there's any urgent questions, I guess. 

**Danny**
* Yeah. has anyone been able to look at Mike's spec change overview and want to weigh in on complexity? Perceived complexity? Okay is there an appetite to get a call with Mike and others that have been doing R&D on this to dig a bit deeper.

**Potuz**
* So I this design is essentially exactly the same as what's already included in our Epb's proposal. and I definitely want this Sean. But as I said before, if we're going to scope this work for this year, I think it's impossible. I think a big chunk of the complexity of Epb's is included in this and in Maxdb. 

**Danny**
* You keep saying Maxdb in relationships, Maxie, be a dependency for us. 

**Potuz**
* Well, not not for Epbs the same thing for inclusion list. Inclusion list shouldn't be a dependency of Epbs, but both of them are. Right. Pretty much a requirement for my kind of epbs. 

**Danny**
* Is it? Right I did. I did take a look at the spec change overview and was. Moderately convinced that it's actually not a super complex change. But you you believe that it is a large portion of the EPBS complexity already. Like you would say, it's 50% of the EPBS complexity or 35%. 

**Potuz**
* No, not not yet. I think the EL maxdb is the thing that scares me the most. 

**Sean**
* I also checked out my spec, and I did think it looks simpler than I was expecting, so I definitely think it's feasible to include an Electra.  I think. I still think Maxie Beast seems like a more important change to me just because like at some point the size of the validator set like is going to be an issue and the migration itself could take a while. 
* But yeah, I think right now, I would lean towards trying to include both maxdb and inclusion lists and not do full epbs. But yes, just. Personal vibe right now. I don't know if that's too much, but. 

**Danny**
* And what's your perspective on it since we're here? period. Us and where that may or may not fit into what we want to do here. 

**Sean**
* Well so like. I think the changes are like since they aren't hardfork dependent like. I'm not thinking about them as much like Right. But like to me it seems like they can be worked on in parallel to like a greater degree in some of these other things. But it's I mean, for us, it's like I would say that's the been the highest priority change and it's got. The most progress on it already. So. Yeah. 

**Danny**
* Okay, back to the question.  Is their desire to have an inclusionist breakout. Is their desire to have it as 15 minutes of the breakout that's scheduled for epbs? 
* How do people want to approach discussing this further, or at least wrapping their heads around complexity and making informed decisions from here? If there was a separate one, would people attend? There's like Francesco. Terrence, Mike. Others would attend. Okay well a few people will be there. 
* Let us discuss in the chat - what are we agreeing on other EIPs for inclusion in this call? We're continuing to talk about some of these big ticket items, that have a difficult trade off space in terms of when to add them, if to add them, when to prioritize them, and competing complexity and priorities. 
* So yes, I don't know if we're going to agree, but we're going to continue to talk. So the next thing is on the list is, Like, I'll echo my opinion on one of the authors here. I think it's. At least from my interpretation. * A number of teams intend to put networking resources on this. It is has a good degree of high parallelizability and doesn't necessarily have to be shipped. You know, with the same type of work.  
* The shipping pier does without a hard fork means that there's no gas change. But that's also that is a potential strategy to do here.  
* Also shipping pier does with a tiny fork to change the gas. The data gas limit is also kind of a feasible path. And so I do personally think that like, it can continue to be on kind of an independent R&D rail that is highly parallelized. 
* And I guess that's. At least for a at least for a few teams, seemingly the intention, because that's just what's happening. Um. Is there? Does anyone want to make the case for not only having it on independent R&D call, to be shipped when it's ready, but to also make the case for having it stated and intended to actually go out with lecture at this point. Or is that just not where people stand on this? Again, does anyone make the case to say peerDAS should be stated and intended and put into the list for Electra? Or should it just remain as a high priority? Parallelized rail? The default is the latter. Speak now if you believe the former. 

**Sean**
* So I just sort of think that if we pursue some of the bigger ticket items in Elektra and it's, I think it's possible that since peerDAS is just CL and would require, like, smaller, changes for a hard fork, then maybe it might even come sooner. So I think at least Elektra is kind of my. My point of view. 

**Danny**
* My other strategy here is that, you know, you could say sensitive inclusion for Elektra, but it's because it's super CL dependent and because it's. that doesn't touch the state transition. 
* It's also something that can be ripped out meaning if it were to be the blocker, it's easy to for it to not be the blocker on getting the main. 
* Any other opinions people want to surface on how to handle this. Okay, I would say very much agreement on but that we can have these breakout calls and continue to discuss a couple of these other things that may or may not go in before, peer does surfaces anywhere in relation to Elektra, but that we can. 
* Regardless, it's something that people are and will and be working on, but that we can pop this up in a couple weeks and and contextualize it after the breakout calls. 
* Okay. And then another fun one. Maxeb where do people stand in relation to that? Is there further discussion,  that can be had today, or does it need to also be contextualized by. what comes out of some of the discussions that are going to happen outside of this call the next couple weeks? 
* Any status update here? Any any further? That's. Okay. So this is going to this will come up in the conversation again in two weeks. 
* And potentially there will be the ability to contextualize or foil against some of the other things that have been thought about in that interim. Okay. As these people want to talk about in relation to Elektra today. Other discussion points for today. Anything related to research specification or just general open discussion? Am I live? 

**Danny**
Thank you.  okay. I appreciate it. This is these are these are tough conversations to have. there's a lot of really important work to do.  a lot of great research and specifications, to dig through. So thank you for bearing with me and and working through it all. And we will pick it up again in two weeks. Take care everyone. Thank you. 

**Terence**
See you guys. Thank you. Thanks. 

**Danny**
Thank you everyone. 



---- 


### Attendees
* Danny
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
* Carlbeek





