# All Core Devs Meeting 144 Notes

## Meeting Date/Time: Thursday 2022/08/04 at 14:00 UTC (10:00 ET)
### Meeting Duration: 1.5 hours
### [GitHub Agenda](https://github.com/ethereum/pm/issues/583)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=vJYzfRH62Ok&t=20s&ab_channel=EthereumFoundation)
### Moderator: Tim Beiko
### Notes: Rory Arredondo
—----------------------------

# Merge Updates

## Sepolia


**Tim Beiko (3:43) -** Okay. Hi everyone. Welcome to All Core Devs number 144. We have a long list of Merge dated stuff to discuss. And then towards the end also wanted to touch on the executable specs work that's been going on. So I guess just to start with like a quick announcements for everyone. We discussed this on the last call and I believe two calls ago, but Sepolia is going to be having a post merge upgrade (inaudible) merge blog for peer management. This is scheduled for August 17. There's a blog post that went out yesterday with all the client releases. So if you're listening and you run a node off Sepolia, you need to upgrade. The upgrade basically just changes peer management that doesn't add any new features or remove any other functionality. And also the client releases that were advertised for the Goerli proof of stake transition, also work for Sepolia upgrade. And lastly, this upgrade is only something on the execution layer. So if you run a node you only need to update your execution layer clients. Not necessarily your consensus layer client. So people can check out the blog.ethereum.org for client releases, but yeah, please upgrade that. Anything or anyone on Sepolia upgrade? If not, we had an upgrade on Prater just a few hours ago. So getting it ready for the merge. I know it seems like overall it went quite well. I don't know Danny, Pari, do either of you want to give a quick update on what happens on Prater.


## Bellatrix


**Danny Ryan (5:58) -** I think Pari has a bit more detailed view.

**Parithosh Jayanthi (6:02) -**  Sure I can go. So the network was roughly at 90ish percent attestation performance pre Bellatrix for (inaudible) before Bellatrix and after we dropped down to the roughly 81,82ish percent. It seems to be stable and holding there, at least according to the tags on Beacon chain. I think that one client team might have a subset of the validators that need to be updated. But besides that, everyone looks perfectly fine, I guess the missing attestation date might just be from community run validators that haven't been updated. I haven't heard of any issues. And in general proposals look healthy. There aren't too many unexpected mis-proposals or anything. So I'd say it was a it was as good as we could hope for upgrade for an (inaudible) testnet.

**Danny Ryan (7:01) -** Yeah, that's what it looks like to me as well.

**Parithosh Jayanthi (7:08) -** It would be awesome if any validator is running on Prater who has an updated if you could update and get participation rates back up. It would just be nice to have a bigger buffer when the merge happens. 

**Danny Ryan (7:30) -** And I believe one of the one of the client teams didn't update their execution layer client. So just a warning. You have to do both. I know that. It seems like configuration errors are reasonably you know the primary things that we're battling with so we'll continue to work on guides but make sure if you're listening to this that you work extra hard on getting both sides of that thing upgraded.

**Tim Beiko (8:02) -** Anyone else have thoughts about Bellatrix operator?

**Adrian Sutton (8:13) -** It's probably worth noting that we've discovered the Teku and Prysm no longer talk to each other on the network. It's a multiplexer on big thing in the latest (inaudible) Prysm and will be fixed it's not actually related but hardfork made it quite clear as we watched all the upgraded nodes disconnect and all of the all the non upgraded ones mostly disconnected because they didn't have Bellatrix so it was actually really good to see that working in that we quickly disconnected is that hadn't updated, that were formed. And at the moment, there's something like, I don't know it must be about 40% of the network between Teku and Prysm's team nodes that aren't in any way directly connected and their routing find around the gossip through other clients and it's all just still working, which is actually really cool experiment. So that's kind of good.

**Terence (Prysmatic Labs) (9:04) -** Yeah, I just want to confirm as well. We fix it right away. We were sending the right byte code. So yeah, it should be out in our next week's release.

**Adrian Sutton (9:18) -** Thanks for the quick support on that, by the way. That was awesome.


## GSF6


**Tim Beiko (9:28) -** Sweet, anything else on Bellatrix or Prater Bellatrix? Ok and then one more network upgrade. We had Goerli shadow fork 6 literally hours ago as well. You want to give us an update on this Pari?

**Parithosh Jayanthi 9:55 -** Yea. So Goerli shadow fork 6 hit TTD earlier today, just a primer on the network. It's a Goerli shadow fork and roughly 30% of the network was running MEV boost it was planned to test MEV boost through the transition. We were at roughly 97 ish percent attestation participation pre TTD and drop down to about 94 post. But it seems like the drop isn't really related to the merge but rather a couple of nodes ran out of disk space and one or two nodes were still syncing up ahead. But otherwise, we look great there. On the MEV boost front no real issues noticed, at least from a network standpoint, we did notice that one of the nodes that was farther away so it was in India, whereas the relayer was I'm not wrong in the US. There was a severely high latency, but it could be related to the machine itself. Like the network card just looks weird. If I'm not getting great throughput on it. I'll look into the node itself but yeah, otherwise I don't think we've noticed any other issues. You can check for up on ETH stats to have a live view of what's going on that.


## Engine API RFC


**Tim Beiko (11:17) -** Any thoughts, comments on the shadow fork? Okay so you've done well across the various upgrades. Mikhail, I you had a whole bunch of things you want to chat about so I think yeah, we can start going through them. You had two Requests for Comments on the Engine API spec. I'll share the first one in the chat here. Issue 270. You want to get some quick context there?

**Mikhail Kalinin (12:02) -** Yeah, sure. Thanks Tim. First of all, both of these RFCs like just a discussion around proposals that we will have after the merge not for merge definitely. This one this have been dropped in the chat is about removing invalid block hash is basically about replacing the invalid block hash status with invalid status plus latest valid hash set to nil it has been this opportunity has been opened recently by a recent change to the Engine API. The other one is about like it's like more involving is below status is worth reworking it actually not like complete rework of them but making them the payload status is more clear. To allow for CL to distinguish the two states of EL it is communicating with one state is when EL have to go to the network pull some data from remote peers to validate a particular payload and the other state status when it has enough, it has all data required to do the validation locally. But it just needs to make some computation basically executing like a bunch of blocks to validate the payload in question. As for now, current status is that we have like accepted and syncing. They're a bit weak with respect to these, like distinguishing between these two states. And this is probably what CLs would like to have to start like utilizing this and to start making a making a difference between accepted and syncing status'. So I'm just yeah, just want to engage the EL and CL client developers to look into these two RFCs for their comments. I don't you have like a lot of things to do. And this is a post merge but anyway, would be great if more people take a look at them.


## Checkpoint Sync API


**Tim Beiko (14:17) -** Thanks. Any thoughts people wanna share now about these? Okay, it seems like the second one already has some comments from some CL developers. So I suspect we'll be talking about that on the CL calls as well. Okay, I guess the next step, you also had a PR about checkpoint sync in the beacon API.

**Mikhail Kalinin (14:55) -** Yeah, this PR proposes to introduce two endpoints like, yeah, the idea of these two endpoints came out of discussion in Discord, All Core Devs channel with Mike, Adrian and Paul probably some other members. But the the idea of these two endpoints is to allow for the following separation of concerns. The rest state providers that provides a state at a finalized checkpoint within big subject days period. But this finalized checkpoint is on on the choice of the state provider. So it may be like the most recent finalized or the previous one. It can be updated on the face that the state provider choose. And the other endpoint is for trust providers. So they expose the tiny API to verify that the book route from this point (inaudible) checkpoint state is matches the block route that all trust providers, expose all dress providers. Has to basically request the state first. Presumably is like the most recent, the state of the most recent finalized checkpoint. Then you take a slot from the state from from the block header that is in the states. Take a spot ask as many transpo editors as you have about the finalised routes, finalize block route in this slot, if they all agree on this route, and if this route actually matches the one that you can compute out of these states that you have just below then you're free to start syncing from this, like checkpoint. Yeah, the idea is to make these checkpoints sync easier for state providers and increase the like the number of state providers and networks so they raise the adoption of the checkpoints sync from from that standpoint. And yeah, if Adrian or anybody else wants to elaborate on that. For you to chime in.

**Danny Ryan (17:23) -** Yeah, I agree. This is good. I agree that it's the most sane way to do kind of multi verification when you're doing this bootstrapping. And we can take the API repo I guess My one concern is defining it in the API repo where that API generally is not expected to be exposed publicly. And then having a namespace that is I just want to be very careful when we're making that decision. If we make that decision to kind of couple these things just because it might result in more users exposing, accidentally exposing endpoints that are easily lost. But nonetheless, I like the like the pattern a lot.

**Micah Zoltu (18:10) -** Is the trust endpoints easy to be (inaudible) or just the state endpoint?

**Danny Ryan (18:17) -** Well, I guess what I'm saying is the rest of the API in the beacon API's, those are user API's, you know, which all of them are easy to (inaudible). You know, it's stuff that you just don't in such a way that it's like hard and like p2p interface, so just having it in the same kind of definition makes me a bit worried. But you already you can big bolded. If you're using this namespace this is, you know, be careful.

**Micah Zoltu (18:43) -** Yeah. It's a reasonable argument for putting it somewhere else. And in particular, the trust provider like it would really want as many people exposing that as possible. And so making it very easy for an operator to expose that without exposing everything else feels like a win.

**Adrian Sutton (19:00) -** Yeah, so I think everything has been said, is spot on. But I also think it's useful to be able to see those two API's as kind of a separate thing as well. So like you're not not expecting to provide the whole API. They are kind of a concept in themselves. And some of the details of how you'd implement them as a particularly as a state provider might defer to what a beacon node would expose directly. This you could add caching or not pull the state as regularly. It doesn't have to be the latest finalized. SOoI think that's just a matter of making it clear in the description, and I need to read out a bit more carefully, but generally, it looked good, and I think the API's make an awful lot of sense and should work really well. Probably the only catch with it is that it does bake in the idea of being able to start from a single state which is possible but use a bunch more work for people, for clients that that haven't gone that far yet and are using state and the block that goes with it. A couple of clients have some extra conditions on exactly which finalized checkpoint needs to be used and that kind of thing as well. So I don't know how much that's a problem for other clients or we're planning to get further along and make it easy and this API can push them along or whether we need to also provide access to a matching block or something like that.

**Mikhail Kalinin (20:45) -** I mean, so they have to pull the block with body. Right?

**Adrian Sutton (20:50) -** Yeah. So I'd much prefer being able to just start from state I think it opens up a lot of simplicity for observing it and a whole bunch of options. But I do appreciate is a bunch of work.

**Micah Zoltu (21:06) -** Is there any compelling argument for not having this long term or is the argument here just that not all the clients have this feature yet? And it may be a while before they have it?

**Adrian Sutton (21:20) -** It does have some impact into your database a bit. There might be some arguments there. I don't know. I think once you've done the work, it's disappeared in Teku, and it's not something I ever think about again. But I don't know how that plays out in other client architectures necessarily. And whether that becomes more of a burden, longer term to keep supporting this one case where you might only have a block header. that said if you wanted to, you can get started with just a block header and connect to the network. And request that full block to make the problem go away. It just depends again, on how that fits into the architecture.

**Danny Ryan (22:03) -** Should we take into the issue and then maybe bring it up again on the next consensus layer call as we thought about a bit more maybe done a bit with refinement? 

**Adrian Sutton (22:17) -** Sounds good.

**Micah Zoltu (22:21) -** Can we get the same feature in the execution client?

**Adrian Sutton (22:28) -** Only if you can shrink the state by about 100 (inaudible).

**Danny Ryan (22:35) -** (inaudible) not needed at all. You just start with the final (inaudible) you can fit in and go from there.

**Mikhail Kalinin (22:49) -** Yeah, you've mentioned you've mentioned the probably published unit like yeah, it's already in a separate namespace which is called checkpoint. But if there is an idea to put it like a separately from beacon API's I don't know if that makes sense. I mean, the complexity and maintaining like separate it as a separate API. But yeah, let's just discuss this probably in discord. 


## TTD Block Gossip


**Tim Beiko (23:25) -** And then, last thing, Mikhail you had another comment about basically competing TTD blocks based on some conversations on the discord this week, I do want to give some quick background on that as well?

**Mikhail Kalinin (23:41) -** Yes, this is like generally to check to double check this one of assumptions. Yeah, let me explain why it appears. So we have we recently we learned that some execution layer clients do not instantly process blocks that are not from like the canonical chain. So in particular, it was the issue with  Nethermind. It received like terminal block a with a total difficulty reaching the terminal total difficulty barrier and then we have like the terminal block B which also like a terminal block, in terms of terminal TTD, but it has either lower total difficulty or simple difficulty of as the previous one. And in this case, Nethermind, Erigon, they don't instantly process these blocks. So they just put them into the block three and that's it. Yeah, we had the test cases for for for this and we had fixes in these clients. If the transition block built off of like, the Block B will appear then these clients will just execute all they have after this transition block and (inaudible) distribution block to prevent the CL from getting stuck at the merge transition block because of safe slots to (inaudible) optimistically. And one related question too, I assume that every EL clients do propagates every proof of work block in spite of like, executing it or not. Like if in this case, if a terminal block B hasn't been executed it will be propagated to after verifying the proof of work seal. If it's correct, it's replicated. This is where we Yeah, this is also critical for the transition. And yeah, my assumption that every client does this. Just wanted to double check it if any, if any client does not do it, like it does not propagate the block, that it hasn't processed, let us know.

**Marek Moraczyński (26:13) -** So I think client what clients are doing is they are propagate the blocks without processing but only to small fraction of the peers. If this is correct, and after purchasing they are propagate to all peers and I have to verify Nethermind behavior here. And I'm a bit worried that we are not working in exactly in this way that we describe it. I will check.

**Mikhail Kalinin (26:47) -** But if it propagates a block to a small fraction of peers but other peers will should receive like this new block hashes message isn't it?

**Marek Moraczyński (27:00) -** After processing right, yes. 

**Mikhail Kalinin (27:02) -** Not after but before this file.

**Marek Moraczyński (27:07) -** No no no. Let me send (inaudible) into specification. 

**Peter Szilágyi (27:15) -** So the way block processing should work is that execution client precedes the blocking. I mean, pre merge block will proof of work verification. If that passes they broadcast it to square root of peers then actually imports the block locally. And what's important before succeeds delegates it announces it is such an important block locally before announcing it is because if I announce the block to my peers, and I don't have it yet imported that one of my peers actually requested a block I will not have it in my local (inaudible) I won't be able to serve. So we do need to actually import it before announcing it to the rest of our peers, but during the square root broadcast or the propagates through the entire network, it's just each other they already have some star topology or some many nodes hidden behind some (inaudible) gateway. Only those are actually requiring an arcing mechanism. As for the so the TTD split at least in gas, we have only transition we have two markers. One of them is that we left proof of work and the other is that we entered proof of stake. Entering proof of stake means that we received the finalized block of proof of stake so give or take six blocks and we only disabled block propagation when we actually finalize proof of stake. So within those initial 32 block transitional time period we will still broadcast all the TTD blocks so if I have ten different TTD blocks in broadcasting and announcing them on US (inaudible).

**Tim Beiko (29:19) -** Thanks. Yeah Besu, Erigon Yeah. How does it work on your end?

**Andrew Ashikhmin (29:27) -** I think currently we have some problems, some flaws in the logic around multiple terminal POW blocks so I look into improving the logic and yeah, just in making sure I'll check how because if terminal POW blocks and try to improve the logic.

**Tim Beiko (29:51) -** Got it. Thanks. And Besu?

**Gary Schulte (29:58) -** Yeah we have a similar behavior to disable block propagation after finalized. I'm not certain I'm gonna have to get back with you about our behavior for gossiping non processed blocks though, noncanonical blocks

**Justin Florentine (30:14) -** Only other thing I would add to that is that it is the second finalized that we stop after.

**Marek Moraczyński (30:21) -** Yea, I want to add that for Nethermind it is the same we stopping block propagation when we finalized 

**Tim Beiko (30:32) -** Got it, OK. 

**Micah Zoltu (30:39) -** Second finalized.

**Tim Beiko (30:42) -** I guess this is for Besu?

**Micah Zoltu (30:46) -** Yea.

**Justin Florentine (30:47) -** Sorry, Micah. Could you repeat that?

**Micah Zoltu (30:50) -** Why do you wait until the second finalized instead of the first finalized?

**Justin Florentine (30:53) -** It's how we interpreted the spec.

**Mikhail Kalinin (31:04) -** Okay, so let's not go into the spec details around this first and second. Yeah. So as long as new blocks are assigned to square root of a number of peers. Yeah, it should be fine. Right? We'll have those blocks disseminated across the network. Unless there are some synchrony issues?

**Felix (31:35) -** By the way, can I ask you a quick question, do you feel like it would be necessary at some point to split five the behaviour around the merge in effort or is just sufficient the way it is now? I mean, we will have to remove the propagation from the (inaudible).

**Tim Beiko (32:09) -** You're breaking up a lot Felix but I think we got the gist of what you were asking like should we add the merge to behavior that are expected directly. Mikhail?

**Mikhail Kalinin (32:27) -** Good question we have this network section in the in the EIP, which is a bit odd because rather than should be like a separate EIP on the network track. Probably should deprecate the block announcements and new block propagation. In the spec after the merge.

**Peter Szilágyi (33:01) -** Not sure I understood Felix correctly maybe the way I kind of understood him was he was asking whether we want to spec out this level of behavior during the transition period for the month? And I mean, honestly, it seems if we want some (inaudible), in my opinion, make sense if you wanted to support this merge transition for multiple occasions, but that doesn't really hold to me we transition to learn network so when you're transitioning and we want to transition may not so from that point onward. The question is how, how long we will do we want to maintain this capability to transition one network into the other? And my two cents would be that long term we should try to deprecate supporting non transition networks and then somehow make some small tool to enable spinning up already already condition that works for private networks, then that would actually be the last nail in the coffin and then it would allow us to actually remove quite a lot of code so my two cents and we should try to push the works not supporting long transition which will also entail not documented.

**Tim Beiko (34:28) -** It does seem reasonable to like to be able to drop this at some point, especially if there's like, more like pretty significant changes that happened the execution layer so you know, things like vertical tries and whatnot like, it seems like if we can have a clean slate to start that work on that would be valuable. 

**Peter Szilágyi (34:56) -** I don't know if we ever can because (inaudible) telling (inaudible) in the chain history. So please, they could also entail somehow dropping all the ancient history. So that discussion, but still pre merge and post merge at least synchronization is quite different. Right, right. And it could be like to support both. And also the problem is that currently all the clients that just support this transition, this will be a mechanism that will never be tested anymore. So it will be we just tested out for the testnets now. We will do it for mainnet. And from that point onwards, we will never ever tested again live. So if anyone else relies on it, I mean it always be like this lottery that doesn't still work. We don't know. We don't care. It's probably not something you want to have around for too long.

**Tim Beiko (36:01) -** Okay, I guess just coming back to the TTD block gossip issue. It seems like the next step is for like the different client teams to look into what their actual behavior is and potentially make some changes to ensure that they are gossiping at least a fraction of what would be non canonical blocks that are still valid TTD blocks before things are finalized. Does that sound right to everyone?

**Micah Zoltu (36:29) -** Why only a fraction?

**Tim Beiko (36:33) -** So the spec the spec was say basically that the current peer to peer spec where like, unless you report it to you only gossip a fraction of it. I guess they could gossip to all their peers.

**Micah Zoltu (36:45) -** I see. So you're saying some clients, some clients already don't gossip all blocks. And so that's it's okay if you continue to do that behavior with the TTD blocks that correct?

**Tim Beiko (36:55) -** Yeah, that was my understanding that they don't gossip to all their peers until they've imported it locally. But if they never import that block locally, they still gossip into like the square root of their peers and that would allow the block to propagate to other network.

**Peter Szilágyi (37:11) -** You guys are talking about different things. As far as I know, Tim was talking about self propagating every block so every block would get propagated but not every peer and Micah was talking about certain blocks not getting propagated at all.

**Tim Beiko (37:26) -** Right, right. Yeah, sorry. So yeah, I was just back to like the Mikhail's original issue. If you hit TTD, you get competing TTD blocks, which you don't import because their difficulty is lower than what you see as the as the your kind of canonical TTD block. You should still gossip those to at least the square root of your peers, assuming the proof of work CL is valid. And that, even though that doesn't propagate them to every peer, it should be good enough in the case of multiple conflicting TTD blocks, is that is that correct?

**Mikhail Kalinin (38:09) -** Yea, that's correct. All blocks all to all terminal blocks, disseminated despite of they've been processed not. So that's important.

**Tim Beiko (38:23) -** And obviously it would be ideal if clients said that all their peers, but that might just be more complex. If like the current spec, if they're just following the current spec for sending it to like a square root is good enough. Then that that's that will work.

**Peter Szilágyi (38:46) -** You really don't need to (inaudible) peers. So that's just never worked. I think we'd never ever broadcast the blocks.


## Flashbots MEV Boost Relay


**Tim Beiko (38:59) -** Got it. Okay. Does that make sense for everyone? Okay, sweet. Um, next up we have Chris I believe from the Flashbots team to talk about the latest on the MEV boost side? Yea. 

**Chris Hager (39:30) -** Yeah. Let me start with a quick update on the release from today's Goerli shadow fork. Everything went well. We were just seeing some connectivity issues from servers in India. Sending the (inaudible) registrations like if there is 1000 Better registrations sent at once, it's about half a megabyte of data. And servers with slow peering might not get the data across to the relays within the default two second timeout. That seems rather an edge case bids really bad connectivity. But still something to keep in mind that we will proper documentation on setting the batch sizes, improving or changing the request timeouts, which is by default two seconds. Not everything (inaudible). I really want to announce that we are going to open source that the relay that we are running and we are waiting for some more updates. We have to stabilize some interfaces and clean up the database infrastructure and to a source code audit. But probably release it under the AGPL license. please chime in if you have any opinions. The idea is if HEPL that people that change it or redistributed in big changes would need to publish that changes as well, which might help lead to a active open source ecosystem. And we believe that our relay has been pretty successful stress tested and this should be a good starting point for other people. So we expect that to happen early September. It needs a few more weeks, but maybe we are committed to opening up and the point of opening at open source software. I think many people are not aware that people have an open source builder entry relay, that anybody can. Okay, you know what I will during this call later, I see some chats about licenses. And I'll just create an issue in the MEV boost repository and post this here in the chat in a bit where everybody can chime in with their opinions about licenses. To discussion here, and the repository I just posted the boost geth builder is is a builder and really implementation. So if anybody is interested in just running a simple, like experimental development builder and really, this is a repository that I can use that implements all the signing all the API's and the block productions. I would probably not use that as a production relay because it cannot handle it's like a single process. It cannot handle external submissions. It's probably not cannot handle a lot of concurrent (inaudible) registrations, but it's the starting point for anybody that wants to keep up with the code. And this is the best that we have until we release the proper relay source code. Any any thoughts or questions on this?

**Tim Beiko (43:05) -** Very, very cool to hear you are going to open source the relay so that's yeah, that's pretty good news.

**Chris Hager (43:14) -** Yea we are very happy about it too.


## Mainnet 5GB DAG Size


**Tim Beiko (43:18) -** Anyone have questions? Thoughts? Okay, I guess we can keep an eye on the MEV boost repo for this licensing discussion, because as you said, there seems to be some strong opinion in the chat. Sweet! Um, okay, and then, one last thing I had on on the merge is basically the DAG size. So, for context DAG is like, how much like data, I guess is required in RAM to mine Ethereum and then every time it exceeds some specific amount that makes some hardware that's mining Ethereum obsolete because they just can't store that amount. And so we're about at five gigahertz on Ethereum mainnet right now. And it's expected to exceed five gigs, basically two weeks from now, which will lead to like some drop in hash rate you would expect on the network, like any, any kind of machine that uses a five gig card won't be able to mine. And I guess this kind of affects how we may want to choose a TTD for mainnet. Just because if we have this drop in hash rate, it affects how long it takes to actually hit the TTD. So given I guess, you know the, the rate at which things are going and like the fork onboarding that's happening in the next week or so. The next All Core Devs happens basically the day after this, this DAG size increase so we'd be able to see the impact on mainnet hash rate. Would people feel confident potentially selling like TTD for mainnet right then once we have kind of this number, and can estimate the hash rate setting it before it might just be like bad estimations because we don't know how much we're gonna lose. It might be 1% of hash rate, it might be five, I would download something massive, you know, 20%, that's five gigs. But yeah, I guess just curious about people's thoughts on that like, assuming we do we do exceed kind of this threshold, right. Right before the next Core Devs calls. Yeah. Oh, and there's a good question in the chat. How much did the hash rate drop at the four gigs? I'm not quite sure. But we can probably see it on Etherscan. And if we can't see it, there might be a good indication that the drop is minimal. So it was block 11,000,520 Which should be Etherscan does not give me based on the hash rate chart. So 11 million. Yeah. 11 million that was okay. No, that doesn't make sense. (inaudible) your message here sorry. Okay, so that was December 25, 2020. That we exceeded the hash rate. And so if you look at so on December 2020, the hash rate was going up already. So we were like in a pretty uphill trend. So it seems we had like a pretty minimal drop that was kind of backup in the past few days, but it's yeah, it was in a world where like the hash rate was going up quite quickly. So yeah, I guess. This is like a bit of a different situation. The hash rates were kind of stable for the past month or so and it's definitely gone down in like the past six months. But you know, based on that there wasn't something like a 10 20% drop. So it should be like a minimal impact. Which means, you know, we could potentially choose like a TTD before and maybe we would just hit it slightly later. Yeah. So I guess I'm curious. From client teams, like, does like around, you know, two ish weeks from now seem reasonable, assuming that things go well on Goerli?

**Ben Edgington (48:22) -** Tim, what leads time would you anticipate I mean, working backwards, you know, if you wanted to target day x of September, then you know, would you want to decide four weeks ahead five weeks or three weeks? 

**Tim Beiko (48:34) -** Yeah, that's a good question. I would like four ish and a reason you know, we've talked a lot about like these potential mining attacks where like, you know, if there's a ton of mining hash rate that comes online, you have you have like the hit before Bellatrix so it seems like having something where it's like you know, we choose that we choose the Bellatrix epoch and the TTD. We give people you know, a bit under a week to put out a release, and then you would expect Bellatrix to hit like two ish weeks after that. And you could aim for a TTD that's like seven to 10 days. After Bellatrix is hit. It's it's just hard. There's like high kind of error bands on the TTD depending on like, how far you look at the current difficulty and what assumptions you make about the rates. But yeah, you could think something like two and a half weeks before Bellatrix, which is effectively when everyone has the upgrade, and then another like seven to 10 days I think before TTD gives us enough like margin so that we're quite confident we would not hit it before Bellatrix. And Okay, yeah. So there is a comment also from YouTube on the ASICs so save that five gigs is actually quite a popular size for ASICs so the drop might be more significant there. Yeah, I guess. Yeah to answer your question Ben, like, if we chose something in two weeks, it means clients would need a release and you know, call it like two and a half weeks from now. So like the week of September, the week of August 22. That would be ready for maintenance. But is that something that's like realistic? Okay, maybe a way to fit this. Does any client team feel like this is not realistic, or that it's just like too early to tell. We can obviously discuss this on this CL next week as well. But yeah, does anyone feel like this is like completely impossible to hit?

**Peter Szilágyi (50:55) -** No honestly, I think we should include everything's fine and good and we should bite the bullet and do something.

**Tim Beiko (51:02) -** Okay. And Goerli by the way is scheduled. I think right now it's gonna hit next Wednesday, so it might happen before the CL call next week. It might not. So I guess we'll see by then. One thing we can also do is, you know, we we can probably set like an epoch for on the CL call, because that's, that's quite fixed in time. And then yeah, wait a couple more days. And agree other TTD if we wanted to set it even like before the All Core Devs call we can do it I think on on the specs repo once we've seen. Yeah, once we've seen Goerli stabilize for a few days after the fork, because I don't think we'll get that. Yeah, I think on the next CL call will have had already live for like less than 24 hours. Okay.

**Adrian Sutton (52:03) -** Is there anything we should try and do before that call, so that we're ready like a lot of the times we have these conversations about TTD decide on a call that we should set a TTD and then someone goes away and works it out?

**Tim Beiko (52:22) -** Yeah, so we've have we have Mario Havel on on the protocol support team at the EF he's been doing a bunch of estimations for different TTDs and like based on historical hash rates. I think it probably makes sense to have him come in and talk about that but like this CL call next week and kind of share with like some numbers could be assuming things are looking good and what the rationale is behind them. And he could probably share that publicly before then. So like people have a chance to review before. But yeah, we can definitely share those estimates. So that's like on the call. Everyone agrees at least like what are like the parameters we're looking at and what's like the rough range which we're going for and then even if we select the actual number a few days after that people should be on the same page.

**Adrian Sutton (53:10) -** Yeah, I mean, I'd almost be keen on next week's call to pick the numbers we would go with. Once we're happy with Goerli. Then it's just a particular Goerli hasn't actually merged or it hasn't been long. We can give it the time, but be close to it anyway. 

**Tim Beiko (53:27) -** Yeah. And then the only the only potential risks of doing that is if five gig ASICs are a significant part of the hash rate. It kind of changes the calculation, right? Like, if we use 10% overnight, it means we whatever TTD we said you could accept 10% Lower kind of hit up this a lot, but that we won't know until basically August 18 Yeah, Ansgar?

**Ansgar Dietrichs (53:55) -** Yea just wanting to quickly, double check so it's basically the idea that because of this (inaudible) issue we would not want to because I think right there was talking about scheduling like an irregular ACD call, right after? Yeah.

**Tim Beiko (54:12) -** Right, right. Yeah. So yeah, I feel like given that the drop would happen. Literally under seven teams. Keeping All Core Devs on the Thursday is probably like the best because if it's like we'll have just more data between the Wednesday and Thursday to make a call about the actual TTD if you want to send it. So I would leave that ignored. Yeah, sorry. If you want to ignore the 5g issue, we can probably have a number on the CL call the Thursday before right?

**Ansgar Dietrichs (54:50) -** Right. Yeah, yeah, I mean, I'm just, I mean, I don't know it. Almost it's (inaudible0 to to to to either just like a couple days back and forth. But I mean, I think every day right we have like, an hour the exact number was like some to double digit millions of dollars of issuance. So there's, it's kind of like, if even if we just you know, a week quicker that's still a couple 100 million, but let's say so. Are we going to because looking at the week, right? We would probably not if we if we keep on the regular Thursday, or whatever that means we won't be able to get a (inaudible) by the end of that week, of course. So that does mean that we can shift everything one week to the right. So I'm just wondering if basically this particular issue is enough of a concern. It doesn't to me it doesn't seem like enough of concern, necessarily to kind of extra one request, but also maybe I don't know we've waited for like a couple of years. We might as well wait one more week.

**Tim Beiko (55:47) -** So yeah, I agree with you though, what we could do, you know, like, like, you know, days and weeks for sure matter. One thing we could do is potentially the sets like agree and sets of values on the call next Thursday. And then don't have clients releases like kind of scheduled clients for the Thursday after like the basically the All Core Devs Thursday and that will give people like around 24 ish hours like to watch the observers there's like a massive hash rate drop and if we want to lower this, this TTD value. If we did, arguably, you could like lower rate on All Core Devs, like you know, agree to, you know, if the hash rate stepped down by 10%, just like run the numbers with the new hash rate. And, you know, maybe clients if they're just literally waiting on that number to make a release can can release quicker. So that might be an option as well. You just send it you assume that like the DAG size is like a non issue and and then if it that, if it is an issue, like you kind of wait until it's exceeded before you actually put out the release and then if it is an issue we updated on the All Core Devs.

**Ben Edgington (57:05) -** I think there's value in Nethermind the TTD I mean that's kind of background stuff. We could we can argue about but I think there's value in setting a target date expectation, which I think will motivate users of Ethereum and infrastructure people exchanges and whoever to plan and get everything ready allocate engineering resources and so forth. So, if we, irrespective of the actual number of the TTD say, we will do the merge on x of September or plus or minus, you know, variants, but that's our target. That might help.

**Tim Beiko (57:44) -** Yeah, and I think one way I agree with that, I think one way to do that quite easily is on the CL call you set the the Bellatrix epoch right because we can set that to a specific timestamp, and any significant like, basically any validator, node operators should upgrade before Bellatrix hits regardless of what TTD happens. So I think for sure on the CL call, we could set Bellatrix that that's like the date by which infrastructure providers and users should have upgraded anyway. And then the kind between that in TTD, you're just kind of waiting around because we don't TTD to hit before the Bellatrix but I think we can probably set that on the next. We could probably set the the Bellatrix epoch height on the next CL call. Does that make.

**Ben Edgington (58:36) -** If governance allows that and that's good with me.

**Tim Beiko (58:38) -** I'll let you chat with Danny. Yeah.

**Danny Ryan (58:42) -** Yeah, I said that makes sense. Assuming Goerli goes well and we feel the same way about dates as we do today.

**Tim Beiko (58:51) -** Yeah, and obviously, yeah. There's not all the CL teams on this call. So like I would like CL teams seem pretty onboarding like the CL folks we have here as well but want to make sure that all the EL teams like don't have something that's holding them up or whatnot. Okay. Does that seem reasonable does anyone have objections?

**Adrian Sutton (59:18) -** So to clarify, that means that next week, we are assuming Goerli has actually merged we are making a go no, go decision and setting a Bellatrix epoch?

**Tim Beiko (59:29) -** Correct. And I would also set a TTD and like, call it an optimistic TTD and then you hold the clients releases until we've actually exceeded like the five gig DAG size. If we see a massive spike in hash rates downwards because of that we reassess on All Core Devs if not, we assume those releases are good to go and that TTD is basically the mainnet TTD and we'll make sure to like share, kind of some of the calculations or like estimations that we've been doing publicly before the CL call so people have a couple days to review that. 

**Adrian Sutton (1:00:08) -** Sounds good. 


# EIP Process & Execution Specs: Proposals


**Tim Beiko (1:00:15) -** Sweet. So anything else on the merge that people wanted to discuss? Okay, that was that was a lot for an hour. Okay. In that case, there's one more thing we had on the agenda. So just to show some quick background, there's a pretty big difference between how the consensus and execution layer handles specifications for Ethereum today. So we have EIPs and the yellow paper on the execution layer and there's a Python spec on the consensus layer. And with the merge happening, it'd be nice to like, potentially have a process that's a bit more similar on both sides. And so Sam Wilson and a few others have been working on execution specs for the execution layer as well. And it's getting kind of ready. There's like some questions about if and how we want to use this as part of the network upgrade process. Yeah, Sam do you want to take a few minutes and kind of walk us through where things are at and like what are open questions right now?

**Sam (1:01:33) -** Sure. So we've been building Python specification, and if you haven't seen it, go look at it. It's pretty cool. We're up to Berlin. We did a little bit of refactoring and then moving on to London. And we're hoping to have a mainnet parity in time for Shanghai. And a couple of us, you know, mostly people working on the specs and some of the EIP editors want to make the Python specification part of the official EIP process for core changes. And we wanted to bring that up here to see how people feel about it and whether or not you know, that's in line with what Core Devs want or if it's not. Tim and I have a proposal on how we want to structure that change. It's linked to the agenda if you want to take a look at it. That's basically where we're at right now. 

**Felix (1:02:24) -** So, wait, can I ask again. So the question here is, should this execute to specification be a part of the EIP process you (inaudible) change is to the huge executables back in the EIP.

**Sam (1:02:58) -** So your audio is really bad. So it's really

**Felix (1:03:00) -** kind of different in the agenda. It was more about like should this be replaced?

**Tim Beiko (1:03:10) -** Okay, so I think what Felix is asking me is what this replace or, complement the EIP process. So maybe Sam you want to take a couple minutes to talk about like, how, how that could work. Like what would the process be like basically, if if you had your way, like what was like the ideal process?

**Sam (1:03:31) -** Yea, sure. So there are a couple of different options. The biggest open question about that is where to put core EIPs and their associated code changes. But putting that aside for a sec, I guess my ideal vision would be to have core EIPS containing like the motivation, the abstract everything except to the specification section, in a mark markdown document or similar inside the execution specs repository. And then alongside each one of those documents you would have in the same git commit or same branch, you'd have modifications to the code itself. So you you would still write like a human documentation describing why you want to make a change and then you'd have like a commit that describes the technical portion of your change.

**Sam (1:04:40) -** Yes. So there are obviously some downsides to this approach. And there are obviously some upsides so the biggest upside is that there have has been a lot of ambiguity in EIPS that have led to incompatibilities between clients and if your client isn't GPL you can exactly look at Geth and figure out what they're doing. So the execution specs is kind of trying to be like a neutral ground for implementing these kinds of changes unambiguously. And because it's an executable spec, you can also use it to fill the tests so you don't have to necessarily use Geth or any particular client to fill it. You can fill it with a patch that you're writing for the EIP.

**Tim Beiko (1:05:30) -** Yeah, Trent has a question in the chat about integrating the EL CL process. I guess, you know, the it's worth noting to CL process is basically the opposite right now. So the CL process is PRs to the specs without this like, marked down the EIP English portion that we have on the execution side. One thing that would be nice is like adding that to the CL process, but they can be kind of different processes, but having something that's like, that's where somebody who wants to write a change that either goes across both or a change in each doesn't feel like it's two completely different processes. Even though you know, there might be quirks that the one hand up like you don't need to be 100% aligned 

**Danny Ryan (1:06:24) -** After there's an edge case here, but I don't immediately see a reason to like integrate the build and integrate the software of these two specifications. And instead if we wanted instead, you kind of release them as packages and allow the consensus layer to call those functions if you wanted to run them in tandem, but I don't think that although I think the consensus layer specs, how they're formatted and how we handle branches and new features, like I said, I think we can converge on something I still think I keep them as separate repositories. 

**Sam (1:07:06) -** Yeah, that makes sense. I mean, we could probably, you know, migrate to using the same tooling for both that way you don't have to learn two different sets of tools, but keeping them separate or together it doesn't make much of a difference.

**Danny Ryan (1:07:19) -** And, you know, I will say, very biased and you've been working on execution, executable specs for quite a while. I do find it really really nice that when I'm specifying things, I'm also writing tests. And when I'm writing those tests, they also generate tests for client teams to run and it's just a the testing being so tightly coupled to writing specifications has been really valuable to our process. But, you know, it's a different process.

**Sam (1:07:54) -** So Greg is here and he's definitely one of the biggest opponents to this change. So I don't want to speak for him, but some of the big things he's brought up, are you want to talk right because you're more than welcome to.

**Greg (1:08:05) -** Opponents not really the right word. I'm very much in favor of there being an execution spec. CL processes what it is, they've been running, basically running pretty quickly with with the single client that they're working on. And the EL. The EL layers has been working differently for a long time. A lot of different clients. proposals come in at different levels of done this from people working on different clients in different languages. So I don't see that we can pull all of that together right away. But I think there should be an execution client and the team that maintains it. And that can be sure to what they can to keep it aligned to the EIP process. So you can look at the execution client and say, yes, these are the changes that we're putting in to support that EIP work with the EIP authors, but it's not till the EIP goes final, that you really could have those things aligned. The EL layers doesn't work such that everyone when making a proposal is going to know how to make changes to the Python client. It just doesn't work that way.

**Sam (1:09:39) -** So is Python familiarity a problem for a lot of core devs?

**Greg (1:09:45) -** It just isn't like for me, it's not worth it. The parts of the VM I care about I know the yellow paper very well. And I can reason directly from the yellow paper for what I'm doing. And learning how to how to put things into the Python client is just a whole another level of work. That's not worth it to me. If I'm going to implement it. I'm going to do it in EVM one or in Geth. So it's actually useful this on mainnet, so I have numbers for performance. That means something to me. 

**Tim Beiko (1:10:30) -** Andrew has his hand up.

**Andrew Ashikhmin (1:10:32) -** Yes about the yellow paper. I've been updating it for for a number of releases, but I'm running out of steam and I'm not sure whether I'll be able to update it to London and probably not. Not for the merge to Paris. So I'm just thinking that yellow paper unless somebody takes that mantle that yellow paper will become obsolete.

**Felix (1:11:08) -** Can I ask you a quick thing. So I'm sorry for the audio. The issue. Maybe the question would be what area of the spec is covered by the executable spec, for example, the EVM it has been very stable. And the most complicated thing is things like the gas rules and like exact pricing or of course depending on state and things like that. These things are very tricky, and I think it would be nice to have an executable spec for that. But then there's the question like how much like is that? Is that all? Is that where it's going to be about or? Like where does the responsibility of the executable spec end?

**Sam (1:11:54) -** So I'm not like, currently and I'm not talking like theoretically but currently the executable spec, you give it a block and it will tell you if it's valid or not. So it does, you know all of the gas rules all of the Hashimoto stuff, it does everything along those lines and then it doesn't handle reorgs it expects to get the canonical chain one block at a time.

**Micah Zoltu (1:12:18) -** Doesn't do networking or anything?

**Sam (1:12:20) -** No.

**Felix (1:12:21) -** I don't think it would really be possible with the networking but the question would be more like so this is basically the like the state transition or 

**Sam (1:12:33) -** Yeah, exactly. 

**Felix (1:12:34) -** State transition. And then also Yeah, more I mean, this is this is pretty good. Like this is the part that that I think can realistically be specified in this way. Anything that goes beyond that, like for example, I know that most of these things are now anyway taken care of by the CL so yeah, I guess it's pretty good.

**Tim Beiko (1:12:55) -** Right, and you can imagine stuff like sync obviously like snap sync or what not be not going to be specified there, right.

**Felix (1:13:05) -** Yeah, it's not. It's not the same type of thing for the format. Yeah.

**Tim Beiko (1:13:09) -** And even like JSON RPC, and even if you look at the CL side, you know, they have to be having a separate metric expect they have to beacon API's as well. So it's like, yeah, it's really about this core state transition.

**Felix (1:13:27) -** Yeah, so I'm, I'm I'm in favor of this. I'm in favor of like trying this like if we can get what what's missing is are the resources missing to get this spec like the executable spec finalized or is it?

**Sam (1:13:43) -** We're on track, I think. I think it's mostly just figuring out if we want to use it as part of the governance or not and I think that's the big open question.

**Tim Beiko (1:13:54) -** I think, on that front, like one idea that had been floated before is that for Shanghai, we can maybe run both processes in parallel. So we get like a, call it like a test drive of the execution spec. And, like, it's, and it might be, you know, it might look something like people have EIPs already and like we just like copy them there and like, you know, kind of mimic what an EIP in the executable spec would look like. And see how we like that. Yeah. Okay, so yeah, Trent has a question about EIPs for CL and no EIPs for EL. So this is I think that if you accept that like we do want to move to something like an executable spec. Then the biggest question is, like, do we keep using quarry EIPs, like in the EIP repo and simply linked the executable spec from them. So you could imagine like an EIP as it exists today. But the specification section was just replaced by a link. And you can imagine doing this on the CL as well. So like, we keep core EIPs. And they are where you describe the rationale, motivation, and whatnot. But when you look at the specification section, it's literally just the link out. And this has the benefit that basically, you could, you know, the EIP process is well known. People kind of know where to go to find the EIPs. And also what's neat is you could specify a single EIP for a change to the EL and CL. So you could imagine something like EIP 444 the actual EIP has all the all the rationale and whatnot. And then for the spec, there's a link to the EL and the link to the CL specs, which implements the different parts of 444. So that's quite nice. The downsides, I guess. With the EIP process is one you then need to sync up like these different repos together. So you need you kind of have this, this change the EIP repo that can affect kind of the change in the both specs repo and vice versa. And then there's also the concerns around like, just, you know, the EIP process, very high friction, which Adrian mentioned earlier in the chat. Yeah, so I yeah, I think that is like probably the biggest question if if we move from like, if we try this with how we do it. And the document the agenda has a section on different pros and cons about that.

**Felix (1:16:39) -** Yeah. Yeah, sorry, I must speak one more time. And for me the, I don't really understand the difference between, again, why, why you're putting these two ideas, the EIP processes and this new executable spec as sort of alternatives. When it is, isn't it more like that the executable spec gives us just another tool to describe changes. And I feel like that that should be its role for now. We could keep everything exactly the same as it is now but just have this additional tool to be able to express changes to the specification and then we can see if it's so much fun using it that we feel like the the EIP process is not needed anymore, or it's becomes less important to know.

**Tim Beiko (1:17:35) -** So when you say you keep it the same, does that mean you have an EIP and then you simply link out the executable spec for the implementation details? Is that what you mean?

**Felix (1:17:48) -** I would rather just include the relevant parts in the EIP. So one nice thing about EIPs in general is that they are standalone documents. So you can always judge the EIP on its own. When you just read the thing, you don't necessarily have to go to another place. And there has always been a goal with EIPs is I feel that you'd be able to I don't know print this document and hanging on your wall and you'd be able to look on that in five years and be like, Oh yeah, that was this idea. And it's like fully, fully self contained in this document. The description of the idea, and that's something that you lose when you when you link to another repository where you have some (inaudible) in some code.

**Tim Beiko (1:18:37) -** Right so I'm not sure what I understand what you're proposing.

**Felix (1:18:42) -** I'm not proposing something I just I'm just trying to yeah, I'm just I'm just physically interested in exploring the the the options here because you guys have been portraying it as like you'd rather like basically, I feel like this whole executable spec is mixed up in this whole other debate of what should the governance process be like? And these are just separate things.

**Micah Zoltu (1:19:10) -** So I think the argument is that if you have the EIP process and the executable spec process, we now have even more work to get a change through and the EIP process is already frustrating enough for most people and having to do the EIP process plus something just makes it worse.

**Tim Beiko (1:19:28) -** I see Sam has had his hand up for a while.

**Sam (1:19:34) -** I don't mind waiting. I have a different topic to talk about.

**Tim Beiko (1:19:37) -** Sorry, sorry Felix I cut you off. 

**Felix (1:19:40) -** I know I would just made acknowledging noise.

**Tim Beiko (1:19:48) -** Dankrad was your comments about this was as well?

**Dankrad Feist (1:19:52) -** Yeah, I guess like I would say that the current process doesn't do a good job of actually specifying exactly the changes. So like, it's like, very cumbersome. You're bringing in this like reference to bring in the past. So I would actually, like, why can't that be? I agree that the EIP changelog should be there, but it should be more of a diff of the executable spec rather than this ad hoc re specification of what is happening because it's nowhere properly specified. Then saying what changes you want to make it and all of these like little scripts that are in there never been properly checked and yeah, being all kind of incompatible and everything. Like that's just terrible at the moment.

**Felix (1:20:37) -** Well, that's a good thing with the executable spec. You can you can have a tool then to have these these snippets that you can actually check out. I feel like the executable specs.

**Sam (1:21:00) -** Sure. So yeah, I think the problem with doing diffs in the current EIP process is when you get into merging things together to make a hard fork. So each EIP would have its own diff section and then, like let's say we actually use like a patch file, then you would end up running into problems when you try to put them all together at the end if there's any kind of conflict. And if EIPs depend on one another, you'd have to apply them in the right order. And I think that just gets really out of hand. So in the proposal that is linked in the chat, we kind of have a branching structure. So we use Git to handle merging all of those things and but that would be kind of a large change in the EIP process. Yeah.

**Tim Beiko (1:21:48) -** So I guess, just like from the general comments, it seems like everyone is kind of interested in see how this could work. Obviously, there's a bunch of like things to figure out. But it probably makes sense to help, sorry, Andrew?

**Andrew Ashikhmin (1:22:08) -** Oh, I just wanted to say that maybe if somebody creates an EIP and also on top of that creates a pull request to the execution spec, then it might be considered as an as a bonus as an an extra argument in favor of that EIP. So like that person has done the extra work so we should maybe like yeah, like err on the side of accepting that team and that would be a nice motivation.

**Tim Beiko (1:22:39) -** That can also backfire. So yeah. Yeah, I think I think it probably makes sense to like at least try this run a parallel process in Shanghai, you know, and see what this would look like in the executable specs. And like also for Shanghai. Most of the changes we do we've already either considered for inclusion or done they're still kind of pending, are already sort of specified as EIPs. So like, you know, realistically, we're not going to ask people to like, throw out all that work and move to something new. But if in parallel, we can, like, make a copy of that EIP as a potential change to the executable spec. I think that would be good. Yeah, does that make sense? And I guess the other thing, and this is maybe more something for the CL call is like if we do want to think about how these processes could eventually be like a bit more in line is like, how, how do we have something resembling the like, English portion of the EIP on the CL side, and whether that's, like, some change in the CL specs, repo or something that's I don't know trialed in parallel. I think this could also be interesting that the test for like the compiler portion of the upgrade.

**Sam (1:24:10) -** Before we before we move on, I just want to bring up a few of the other concerns that people have had about the execution specs. So one of the big ones is that you have to pick a particular algorithm when you're implementing something for the execution specs. You can't leave it specified it like math notation or or a description of the outcomes. And that might influence client developers. So that's kind of a negative. Some things are much easier to specify in English than they are to specify in code. So you might lose some of the clarity you would get by writing it in English. Yeah, and I think there's the big ones, Greg, if I missed anything else, let me know. But I think those were the two other ones that we haven't talked about yet.

**Greg (1:24:53) -** Yeah, that is a big one. I've got one thing that four sentences of English makes it quite clear that it's a whole page of code actually validated. If you read the code, it'd be very difficult to extract the four sentences.

**Felix (1:25:13) -** But we can basically just accept the way it's basically always worked. So that like we have EIP is as this platform where you can publish your ideas, and I don't know, get feedback on them or whatever. And then eventually, once once the ideas like reasonably accepted, we like put it to the spec. And then like the spec can be executable. That's really nice, but it has, I feel like very little to do with, I don't know.

**Greg (1:25:40) -** No, I'm with you exactly. I think that's exactly you know, right now, the executable spec is what it is, and it runs in parallel. And that about the same time that everything goes final, the executable spec is ready. Like you say, it's another tool for all the clients to communicate and get on the same page.

**Felix (1:26:05) -** And it's just it's just a way to formally like really, like, precisely express what you mean when you're talking about consensus changes, and I feel like that that should be all this does.

**Tim Beiko (1:26:16) -** Yeah. So yeah, just to be clear, so that means you could imagine an EIP which that EIP itself does not contain the actual specification, right? Because it just links.

**Felix (1:26:30) -** Yea you write that after, once you've, yeah, you can put it in there or not, but it shouldn't really be like it's just like it's not, if you can express it in this in the spec language. I guess it's a change that like, I feel like many changes can be expressed in the spec language, if we have a working spec language where we can be like, oh, yeah, I want to make this tweak to the gas costs. And then you just write out the new formula. And you can have a bunch of text that says why you want to make this change, and it's going to be all together. And then once everyone kind of feels like this is good, you can apply that to the actual spec and then yeah, it's gonna be in there. I feel like.

**Sam (1:27:10) -** I think the problem with that is that every change eventually needs to make it into the spec so that you can build on top of it. So why don't make the spec part of the process?

**Danny Ryan (1:27:22) -** You can have spec implementations TBD and if you actually go and implement the PR it helps eliminate what's going on and helps show that it builds properly. But maybe some it's delayed. Some it happens quickly, depending on kind of the style, the process of because I guess, if it's a complex change, and you want to get the English language out there, you probably want to be able to say, dub execution. So I can just like get initial feedback, I guess. 

**Tim Beiko (1:27:53) -** Yeah. I think the question is also, what's the canonical? So imagine you have like a gas costs, like a complex gas schedule change. Right? And you sort of are like a complex algorithm, you know, that like Greg was saying, you specify something like, more of a math notation and the EIP you link out to the executable specs for the actual implementation. If they disagree with each other in some weird edge case, you know, which one is treated as canonical?

**Felix (1:28:21) -** So I feel in this case execution like this, the spec should be canonical, okay. And also, it's under this this this also sort of something that we have right now, where if you have multiple EIPs, applying to the same kind of thing, and they sort of override each other or start interacting with each other, and this is something that you can't really specify in the EIP or in a related scenario, what if you create the EIP and everything seems, seems fine. And then much later, during like hard fork testing, we run into an issue and we find that the spec needs to be changed. In this case, we'd have to now right now we'd have to go back and like change the EIP but I feel like in this new world where we actually have the spec, we wouldn't necessarily change the EIP anymore. We just keep the EIP as a sort of historical document that started the idea but then just like, fix it up in the specs so the edge case removed or something. It creates a bunch of new possibilities that we haven't really had yet. Just having the spec like I said, that's that's like the milestone we should aim for right now. It's just having the spec in the first place because we don't have that right now. Once we have that we can see like oh how we like, we can just check how we integrate that once the spec actually exists and works and.


# Announcements


**Tim Beiko (1:29:45) -** Yea that makes sense. And I think, yeah, it's like, yeah, it seems we need to agree to a free report. But this I think, okay, and we're kind of wrapping up in terms of time. But I think people would agree that this is like a really interesting experiments. It's worth continuing. The link in the agenda has a link to the ETHMagician's thread if people want to comment about like the specifics of how this happened. But I think, yeah, it's pretty clear that people want to see this play out that is a parallel with Shanghai. So I think Sam, that's that's a reasonable next step. Does that make sense? Last thing, I guess just as we wrap up, there is a merge community call next Friday at 1400 UTC. So Friday, August 12. If client developers want to show up, it's always useful. And there's a few flashbots people on the call as well. I suspect it's a couple of you want to show up as well. So people might have questions about MEV boost, and it would be good to have like experts to answer them. Again, this is linked in the agenda at the bottom. Yeah, next Friday, 14 UTC. And right before that, we'll have the CL call as we discussed, to talk about the Bellatrix epochs and potential mainnet. Yeah, thanks. Everyone. was pretty good. 


# Attendees

* Zuerlein
* Tim Beiko
* Parithosh Jayanthi
* Micah Zoltu
* Afri
* Damien
* Gary Schulte
* Roberto Bayardo
* Terence(Prysmatic Labs)
* Ramon Pitter
* Ben Edgington
* jgold
* Adrian Sutton
* Ansgar Dietrichs
* Justin Florentine
* Greg
* Chris Hager
* Mikhail Kalinin
* Trent
* Sean Anderson
* Danny Ryan
* Sam CM
* Leo Arias
* Stokes
* Sam
* Stefan Bratanov
* Lightclient
* Pooja Ranjan
* Viktor
* Helen George
* Matt Nelson
* Marcin Sobczak
* George Kadianakis
* Dankrad Feist
* Paweł Bylica
* Ashraf
* Péter Szilágyi
* Daniel Lehrner
* Mario Vega
* Barnabé Monnot
* Potuz
* Fabio Di Fabio
* Felix
* Jamie Lokier
* Sam Feintech
* Saulius Grigaitis
* SasaWebUp
* Ahmad Bitar
* Ruben
* Alexey
* Marek Moraczyński
* DanielC
* łukasz Rozmej
* Soubhik Deb
* Protolambda


# Zoom Chat

00:05:20	Ramon Pitter: Apologies Tim airpods aren’t on


00:05:27	Ramon Pitter: But have joined in the past

00:05:33	Tim Beiko: All good


00:05:57	stokes:	gm

00:06:07	Trent:	Justin did your panda eyes get messed up recently lol I don't remember that

00:06:09	Leo Arias: 👋

00:07:16	terence(prysmaticlabs): Randao

00:07:50	Trent: LOL

00:08:05	Trent: edgy tim

00:09:15	Tim Beiko: https://github.com/ethereum/pm/issues/583

00:10:00	Tim Beiko: https://blog.ethereum.org/2022/08/03/sepolia-post-merge-upgrade/

00:12:30	Chris Hager: plugging our relay stats: https://builder-relay-goerli-sf6.flashbots.net/

00:15:25	danny: pari MVP

00:15:27	Tim Beiko: FYI there are more people on ACD zoom now than can be seen on the screen - if you aren't part of a client/testing/R&D team, please watch the YT stream instead so we can see all participants on the screen thanks !

00:16:40	Chris Hager: 1k validator registrations is about 0.5MB, and the server couldn't send that within the 2 seconds default request timeout

00:16:57	danny: great shadowfork!!

00:17:15	Chris Hager: thanks Pari 🙏

00:17:20	Tim Beiko: https://github.com/ethereum/execution-apis/issues/270

00:17:25	Parithosh Jayanthi: Yup, its definitely a node NIC issue and not anything related to the relayer 😄

00:17:55	Micah Zoltu: https://github.com/ethereum/execution-apis/issues/270

00:18:03	Micah Zoltu: Oops.

00:18:09	Tim Beiko: https://github.com/ethereum/execution-apis/issues/271

00:20:18	Tim Beiko: https://github.com/ethereum/beacon-APIs/pull/226

00:28:54	danny: thanks mikhail

00:31:33	Mario Vega: Test descripion ("Terminal blocks are gossiped" test) here: https://github.com/ethereum/hive/tree/master/simulators/ethereum/engine

00:32:32	Jamie Lokier: From the spec https://github.com/ethereum/devp2p/blob/master/caps/eth.md

00:32:45	Jamie Lokier: "Newly-mined blocks must be relayed to all nodes. This happens through block propagation, which is a two step process. When a NewBlock announcement message is received from a peer, the client first verifies the basic header validity of the block, checking whether the proof-of-work value is valid. It then sends the block to a small fraction of connected peers (usually the square root of the total number of peers) using the NewBlock message.”

00:32:46	Marek Moraczyński: https://github.com/ethereum/devp2p/blob/master/caps/eth.md#block-propagation

00:38:01	Felix: It will be temporary anyway

00:38:11	danny: https://eips.ethereum.org/EIPS/eip-3675#network

00:38:14	Tim Beiko: Peter, did you want to add something else or is your hand still up from last time?

00:38:15	Felix: We will remove block propagation from the eth spec later

00:38:18	danny: "Beginning with receiving the finalized block next to the FIRST_FINALIZED_BLOCK,"

00:38:20	Felix: after the merge

00:38:28	danny: I think the word next here implied second finalized to besu

00:38:36	danny: I think this is just a language issue

00:38:48	Tim Beiko: Meaning it should be the first finalized block correct?

00:38:55	danny: yes

00:39:03	danny: but doing second probably doesn't hurt anything

00:40:12	Mikhail Kalinin: after the FIRST_FINALIZED messages must be discarded, after the second finalized handlers must be remove and remote peers gossiping blocks should be penalized

00:41:50	Justin Florentine: yes, danny is describing our interpretation correctly

00:43:03	Mikhail Kalinin: > I think this is just a language issue. I can see the issue now. Let's fix it

00:46:14	danny: great news!

00:46:42	Micah Zoltu: I have opinions on licenses.  Unlicense please!

00:46:58	Felix: AGPL usually does not lead to an 'active community'

00:47:06	Chris Hager: https://github.com/flashbots/boost-geth-builder

00:47:09	Felix: I can very much advise against using AGPL

00:48:23	Leo Arias: we have a plan for active community 💥 more on that next week. Independent on the license.

00:49:18	Tim Beiko: https://minerstat.com/dag-size-calculator

00:51:01	danny: 👍

00:51:18	Jamie Lokier: How much did the hashrate drop at the 4GB threshold?

00:51:19	Gary Schulte: fortuitous timing

00:51:56	Trent: do ASICs have 4gb models?

00:52:05	Trent: if not it's irrelevant

00:52:18	Micah Zoltu: We don't know what ASICs exist.

00:52:22	danny: or gpus with 4gb

00:52:29	Micah Zoltu: *we don't know *all* ASICs that exist

00:52:35	Trent: right, GPUs or ASICs

00:53:40	Trent: from danno in the YT chat "​4GB was the drop of for a class of graphics cards. 5GB is the drop off for most ASICs"

00:56:23	Adrian Sutton: Ship it.

00:56:28	Zuerlein: Do it.

00:56:56	Parithosh Jayanthi: *Insert Shia LeBeouf's Just do it meme here*

00:57:04	danny: https://bordel.wtf/

00:57:28	Justin Florentine: Trent, there is nothing wrong with the panda, he is just crosseyed from #testingthemerge

00:57:33	Trent: lolol

00:57:40	Mikhail Kalinin: lol

00:58:08	Justin Florentine: The Panda remains excited and eager to merge. LFG.

00:58:37	Chris Hager: The issue about open sourcing the relay, and which license to use. Please chime in with your opinion! https://github.com/flashbots/mev-boost/issues/237

01:01:45	Zuerlein: That's a good idea.

01:04:11	Micah Zoltu: Danny is "governance"?

01:04:15	Micah Zoltu: I didn't vote for him.

01:04:18	Trent: so that would be next week CL call, correct?

01:04:24	stokes: yes

01:04:31	Trent: 👍

01:04:42	Ansgar Dietrichs: @Micah benevolent dictators are not a thing you have a vote on

01:04:58	Micah Zoltu: Ah, good point.

01:07:08	Tim Beiko: https://github.com/ethereum/execution-specs

01:07:48	Tim Beiko: https://notes.ethereum.org/@timbeiko/executable-eips

01:08:13	Micah Zoltu: Or better yet, *replace* the EIP process.

01:08:15	Trent: felix ur audio is pretty bad

01:08:31	Tim Beiko: micDAO

01:08:40	Trent: bandwidthDAO

01:08:41	Micah Zoltu: I think this is internetDAO.

01:08:44	Trent: fiberDAO

01:09:56	Felix: it's a cool idea

01:10:07	Felix: thanks for explaining!

01:10:37	Trent: any details on how to integrate the EL / CL process?

01:10:48	Micah Zoltu: None yet.

01:10:56	Trent: but that's the assumption right?

01:11:02	Trent: that they should

01:11:03	Micah Zoltu: 🤷

01:11:21	Micah Zoltu: I don't think they should merge, personally.

01:11:24	Trent: any CL devs want to weigh in here?

01:11:52	Adrian Sutton: I'm finding the CL process work really well. EIPs were insanely frustrating.

01:11:58	Micah Zoltu: Modularizing and setting up clean boundaries is valuable for maintaining velocity.

01:13:08	Tim Beiko: @Adrian, do you think that adding .mds to the CL specs with EIP-esque english descriptions would make things significantly worse?

01:13:23	Potuz: +1 on the tests

01:13:30	terence(prysmaticlabs): Spectest is the MVP

01:13:52	Adrian Sutton: I think we have that in the PR description. It's not a formal as the EIP format but that's kind of nice since we then don't a heap of time arguing about formatting rules.

01:14:08	Tim Beiko: Right, my personal gripe with PRs is they are very tied to Github

01:14:16	Adrian Sutton: True.

01:14:27	Micah Zoltu: Do you think there is value in retaining the content/discussion from those PRs @Adrian?

01:14:29	Tim Beiko: I'm fine about having a loose template, but would rather the artefact be part of the actual code repo

01:14:32	danny: I'm pro a parallel development with eips for time being

01:14:36	Micah Zoltu: Or do you see it as transiently useful, but not useful long term?

01:15:03	Tim Beiko: @danny does that include CL EIPS 😛?

01:15:18	Adrian Sutton: Mostly the discussion is not useful once merged, but sometimes it can be. You generally don't know if it will be useful later or not at the time though.

01:15:30	Micah Zoltu: 👍

01:15:39	Tim Beiko: I do think something like a rationale is pretty useful even post-merge, no?

01:16:07	Adrian Sutton: That said EIP discussion is tied to magicians but also have spread through github comments and discord and twitter etc…

01:16:26	Adrian Sutton: And not all the discussion of CL PRs is on the PR either obviously.

01:17:58	danny: state_transition(pre_state, block) is CL

01:18:09	danny: returning a post state

01:18:34	danny: we specify networking in written language

01:18:50	Mikhail Kalinin: I am finding rationale and motivation written in English as a very useful things that consensus specs are lacking (we have annotated specs tho)

01:19:49	Trent: why should the two layers have different processes (EIPs for CL and no EIPs for CL) struggling to reconcile

01:20:05	Trent: if the CL process is so much better why not use it

01:20:25	danny: CL process has warts

01:20:44	danny: CL *lack of process* has warts**

01:21:53	Tim Beiko: https://notes.ethereum.org/@timbeiko/executable-eips#Keeping-Core-EIPs-vs-Specs-Only

01:23:19	Adrian Sutton: Yeah I definitely wouldn't hold the CL process up as perfect. It can be easy to miss changes which EIPs solve because they have more of their own identity and partly because the process is more heavy-weight so it takes more attention to get it through.

01:24:01	protolambda: To me the EIPs are a living formal changelog of ethereum. The EL/CL specs can contain the full changes imho.

01:25:39	danny: handholding parallel in Shanghai assuming EELS team is willing to hold the hands

01:25:48	danny: is what I think

01:28:03	Felix: execution-specs PR overflow incoming

01:28:53	Sam: Bring it >:)

01:29:37	Felix: not from me, just saying, if you tie EIPs to specs PRs, you will have hundreds of PRs on the spec repo, and most of them will never be merged

01:30:18	Tim Beiko: We wanted to tie it to branches so yes, you would imagine a large number of branches on the repo

01:30:39	Tim Beiko: see https://notes.ethereum.org/@timbeiko/executable-eips#EIP-Process

01:33:55	protolambda: Old process: Idea>Draft>Review>Last Call>Final/Withdrawn

01:34:24	protolambda: New process proposal: Idea>Draft>Spec draft>Review>Last Call>Final/Withdrawn

01:34:54	Micah Zoltu: 👆 is my preference.  You can create a draft without executable spec changes, but to move to Review phase you need to have a spec.

01:35:02	Sam: +1

01:35:02	protolambda: The spec can be a later stage

01:35:13	danny: have to go. thank you!
