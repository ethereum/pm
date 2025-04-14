# Consensus Layer Call 144

### Meeting Date/Time: Thursday 2024/10/17 at 14:00 UTC
### Meeting Duration: 1.5 hour
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1178) 
### [Audio/Video of the meeting](https://youtu.be/p3FRr5umt4U) 
### Moderator: Stokes
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
144.1  |**Pectra Devnet 3 & 4 Updates** EF Developer Operations Engineer Barnabas Busa said that he plans on shutting off Pectra Devnet 3 imminently and asked if any client teams still needed the devnet for testing purposes. Busa noted that there is an issue with block proposals in the Grandine client that has not yet been resolved on Devnet 3. Busa said that he would troubleshoot this issue with Grandine developer Saulius Grigaitis off the call before shutting down the devnet.
144.2  |**Pectra Devnet 3 & 4 Updates** Regarding the launch of Pectra Devnet 4, Busa said that he would like to see one more execution layer (EL) client passing local Kurtosis tests to kick-start the new test network. So far, Busa said the Geth and Ethereum JS clients are ready to go, as are the Lighthouse, Teku, and Nimbus clients on the CL side. Stokes recommended that client teams aim to launch Devnet 4 by tomorrow, October 18.
144.3  |**Pectra Code Specifications** Consensus Specs, PR#3900: As discussed last week on ACDE #198, developers refrained from including additional changes to EIP 7549 in Pectra Devnet 4. They discussed whether these should be considered for inclusion in a future devnet. However, the consensus on the call was to exclude these changes from the upgrade due to implementation complexity. Stokes said that he would follow up directly with the author of the issue to ensure that they are okay with this decision.
144.4  |**Pectra Code Specifications** Consensus Specs, PR#3767: Similarly, developers also leaned towards excluding other major changes to the networking layer of Ethereum, as defined by PR #3767. Teku developer Enrico del Fante noted that the changes are too large to include in Pectra this late in the upgrade planning process. Prysm developer Terence Tsao agreed. Stokes said that he would follow up directly with the author of the issue to ensure that they are okay with this decision.
144.5  |**Pectra Code Specifications** Consensus Specs, PR#3979: Teku developer Mikhail Kalinin encouraged developers on the call to review a bug fix proposed for EIP 7251.
144.6  |**Pectra Code Specifications** Builder Specs, PR #104: Developers agreed to work on adding SSZ support to the builder API when handling execution layer triggerable requests such as validator deposits, withdrawals, and consolidations. Stokes said that he would speak with the MEV-Boost team and other MEV stakeholders to ensure that SSZ support is implemented across the entire MEV tech stack.
144.7  |**Pectra Code Specifications** BLS precompile repricing: Developers conducted a breakout meeting on October 14 on the topic of pricing BLS precompiles in EIP 2537. There remain questions about the optimal way to structure the inputs for each precompile. Stokes asked that developers and other stakeholders on the call chime in with any thoughts or recommendations on this matter.
144.8  |**PeerDAS & Blob Scaling Discussion** CL client teams are implementing a new Engine API specification aimed at helping users that propose blocks locally, that is without the use of a third-party builder and MEV relay, include blob transactions in their blocks. The Engine API specification is called the “engine_getBlobsV1” method and Tsao shared takeaways from Prysm’s implementation of it on the call. His takeaways are also summarized in written form on HackMD. Both Tsao and del Fante noted that the method does reduce node download bandwidth, as nodes receive blobs faster, but node upload bandwidth increases, because the node is now servicing other nodes over the P2P network with more blob data. Developers discussed various methods to address this issue and agreed to continue working on optimizations to the implementation of engine_getBlobsV1 asynchronously.
144.9  |**PeerDAS & Blob Scaling Discussion** developers discussed rebasing PeerDAS specifications so far on top of Pectra specifications. Representatives of the Lighthouse, Nimbus, and Teku client teams said they were in favor of this change. Busa said the current PeerDAS specifications which are based on top of the latest Ethereum upgrade, Deneb, are not stable, and therefore, rebasing these specifications on top of Pectra will make debugging and testing the code changes more difficult. Even so, Stokes said that developers should lean towards moving forward with the rebase. Stokes said that he would reach out to other CL client teams not represented on today’s call to ensure they are okay with this decision.
144.10  |**PeerDAS & Blob Scaling Discussion** Thirdly, Francis Li, a developer for the Layer-2 rollup Base, gave a presentation on the urgency and rationale behind including an increase to blob capacity in Pectra. Li’s full presentation is also publicly available in written form on Google Docs. Li recommended increasing the blob gas target to 5 and max to 8, along with additional work on the networking layer, such as the implementation of engine_getBlobsV1. Developers discussed whether they could commit to including a blob capacity increase in Pectra on this week’s call
144.11  |**PeerDAS & Blob Scaling Discussion** Busa noted that an increase in blob capacity should be coupled with the implementation of EIP 7742, which introduces a mechanism to dynamically set blob gas targets and max limits through the CL. Busa said that the current mechanisms for setting these parameters are difficult to change and introducing EIP 7742 would ensure that developers can easily adjust these settings in the future, for example, for an upgrade like PeerDAS. However, Busa also noted that EIP 7742 requires additional work from both EL and CL client teams to implement and could push back the timeline for Pectra by 1 to 2 months. He urged developers to consider starting the work for implementing EIP 7742 sooner rather than later to avoid unnecessary delay to the Pectra upgrade. Stokes recommended revisiting this discussion on the next ACD call. EF Researcher Ansgar Dietrich pushed back on this and encouraged developers to make a decision about EIP 7742 and a blob increase on the current call. Stokes said that developers should focus on plans to launch Pectra Devnet 4.
144.12  |**EIP 7782 & 7783 Update** On the last ACD call, ACDE #198, there were two new EIPs proposed for inclusion in the Pectra upgrade, EIP 7782 and 7783. They were presented as alternative ways to scale Ethereum without any changes to blob capacity. Erigon developer Giulio Rebuffo reiterated that his proposal, EIP 7783, does not require a hard fork and would introduce a mechanism to increase the block gas limit gradually, instead of in a cliff-like manner. Nethermind developer Ben Adams said that EIP 7782 is a proposal to scale Ethereum both in terms of blob and block capacity by reducing slot times. Adams asked CL client teams how difficult changes to the slot time would be to implement
144.13  |**EIP 7782 & 7783 Update** Rebuffo pushed back on Adams’ proposal, saying that the EIP would increase node bandwidth requirements and complicate research toward single-slot finality. EF Researcher Francesco D’Amato agreed that developers should be wary about changes to the slot time due to their impact on active research initiatives such as enshrined propose builder separation (ePBS) and inclusion lists (ILs). D’Amato said, “One thing that might not be obvious is just how much it kind of has the potential to get in the way of future changes to the CL which there might be things that we haven't agreed on. There might be things that we haven't even talked about on ACD because they're just research at this point. There's just a whole bunch of things that we might potentially want to do in the future from ePBS to ILs to other stuff that do interact with the structure of the slot a lot.”

**Stokes**
* Hey, everyone. So this is Consensus Layer Meeting 144. And, yeah, I think people have kind of been pretty heads down with, the Electra devnets. That being said, there's quite a bit on the agenda today. So yeah, let's go ahead and just dive right in. first we'll start up with Electra, and I'm not sure if there's anything to speak to around Devnet three. I think we killed it this week. But if there are any comments, to close this out there, that this would be a good time for that. 

**Barnabas**
* I was actually just waiting for ACDE, just to confirm that I can shut it off by the end of the day. Unless there is any opposition. I will proceed with that. Anyone? Devnet three. We still found a proposal issue with Grandine. I'm not sure if they want to still debug that, or whether they just want to focus on Devnet four. 

**Stokes**
* That's a good question. Is anyone from Grandine on the call? Okay, Yeah Barnabas, I would just say use your judgement if you can't get in touch with them by the end of the day, I think it's fine to move ahead and close out. Devnet three. Okay, cool. Okay. Otherwise, then. Devnet four. We've all been very busy getting this ready. I think I even saw a message on discord earlier. A good number of clients I think are ready to go, but I don't think we've launched the Devnet quite yet. anyone have any more information on the status of Devnet 4? 

**Barnabas**
* Yeah, I just saw that just joined in, so maybe we can circle back for one second to that. Would you be okay if I shut off Devnet three by the end of today? Or are you guys still debugging something? regarding the non proposals bugs. 

**Saulius**
* So they just joined us. So, I think I hope that will be, ready, I think, I mean, we pass all the tests and, there could be some integrational stuff that we didn't test in kurtosis. so, yeah, if we are lucky, we will be ready today. Otherwise tomorrow. 

**Barnabas**
* No, the question is whether we want to keep Devnet 3 around. are you are you still actively debugging on it? 

**Saulius**
* Oh, sorry. I don't know, I think I think if you. What was the outcome, when you nuked the the server, was it, running? Okay. 

**Barnabas**
* We can get back to that. okay. Yeah. Let's do offline. Yeah, but it's still not proposing. That's the conclusion. Okay. 

**Saulius**
* Okay. We will check it then. Okay. 

**Barnabas**
* Okay. So regarding, Devnet four, I also have an update for that. So we have two execution layer clients working as an Geth and Ethereum JS. We have a branch for that. But there seems to be some formatting bugs. And for the CL side we have lighthouse Teku, prism and Nimbus working. And Lodestar is able to attach but cannot propose and Grandine cannot propose. 

**Stokes**
* Okay. Awesome. So we've launched the Devnet, or. This is just

**Barnabas**
* This is just  stuff. Gotcha. We can. So I would like at least one more EL to come online, and then we can probably launch it, tomorrow. Possibly. 

**Stokes**
* Okay. Yeah, that works for me cool. Any EL's on the call who aren't quite ready, but maybe could speak to readiness by tomorrow. 

**Oliver**
* Not quite ready, but I'll sprint on getting it ready today so we can launch tomorrow. 

**Stokes**
* Cool. Yeah, I think that would be nice. just to have a week or two of 4 for, we did also want to have, like, a public testnet based on devnet for Devcon, so they, uh. The deadline's approaching. cool. But, yeah, it sounds like there's been a lot of great progress on Devnet for with the various implementations, so that's really cool to see. And yeah, everyone just, keep at it. anything else on Devnet 4? yeah. Just to reiterate, it sounds like we'll aim for a launch tomorrow. pending. Yeah. Another 1 or 2 else who can join? Any other. And? 

**Barnabas**
* And we can always just add them later on as well. Just make some deposits and include them. 

**Stokes**
* Definitely. cool. Any other comments on Devnet 4. Okay. If not, then we can move on to a number of other things. So at this point, yeah, I effectively want to think about, you know, how do we get to a feature complete picture. So, you know, we can start thinking mainnetabout that down the line. There are a number of open issues that we still have. you know, every call there are fewer and fewer, which is also good to see. one of them here is this PR 3900. And this was a refactor to some of the attestation work. we had discussed this last call and basically said, you know, there are some like nice security benefits here.
* It's also possible that implementation wise, because of how core the attestation type is. You know, this could be a lot of code change for clients. So we're going to give it another cycle to kind of assess that a little bit better and then make a call on this change. So yeah, I mean, there's definitely grounds to have this as an update for EIP 7549. I always get that mixed up with PeerDAS. but yeah. So I guess any other CL teams here have you had time to look at this or think about this? I think the PR is pretty much ready to merge. We just need to agree that we want to move ahead with it. Yeah. Enrico. 

**Enrico**
* Yeah. I think like last, last message from Dapper Lion in in the attestation PR is kind of a good point to me. And considering that we had our spike implementation, it kind of, says to us that is doable. a quick, implementation of that, that doesn't really impact anything. It's not very nice currently, but we can we could go through in that direction for sure. but essentially what the plan says is that the, DDoS attack that is supposed to be blocked is not is a problem that remains there anyway, which is kind of weird. And to me is something like this is an argument that convinced me, I don't know if anyone has thought about it, and if this is true, probably makes the entire, change worthless. Do you think, guys? 

**Stokes**
* Right. Yeah. Has anyone had time to take a look? I would need to go review a little bit more myself, but I hear what you're saying. I don't think ison the call. And he was pushing for this. Um hmm. Any other colleagues have any input here at the moment? 

**Sean**
* Well, basically, I would say that, like, the general lighthouse vibe was. Yeah. We didn't see the benefit of the change, so probably not worth doing. for the reasons, Dapplion brought up. 

**Stokes**
* Okay. Thanks. So. Right. Okay. I think then I'll try to circle back with offline and get a better sense of what he thinks. in lighthouse of this recent comment and. Yeah, otherwise, it does not sound like there's a ton of support to move forward. And if anything, it's one less thing for us to do. So we'll get to Pectra sooner rather than later. okay. Yeah. Thanks, everyone. If there's no other comments there, we can move to the next agenda item. 

# Include p2p spec changes around rate-limiting in Pectra? p2p: Deprecate TTFB, RESP_TIMEOUT, introduce rate limiting recommenda… consensus-specs#3767
**Stokes**
* This one was around a number of P2P changes that I think kind of came out, some of the discussions from interop earlier this year. I think, you know, a nice way to think about this is to go ahead and roll out this PR with, with Pectra itself. And yeah, I guess here I'm just calling it out for everyone to take a look. I don't know where we are here. There's a lot of conversation. but, yeah. Do have any CL teams had a chance to look at this PR, feel strongly one way or another about merging it? From what I recall, there was pretty strong support for this direction at interop. This PR would be.
* I think, a pretty like maybe not invasive but somewhat substantial change to the networking layer, which I think would then would imply, you know, a good bit of testing, which again, I my understanding is that the, the PR justifies the cost, but it's just something to think about. 

**Enrico**
* We discussed that later internally and it seems like this is yeah there will be several several changes to to go for. And it seems like a little bit late to target to backtrack for for that could be better to to target the next one. But this was to make to make things, more mostly stable and, and don't add additional things to do for the next fork. It's been there for a while, and, and we were trying to keep Electra stable enough. And having that merged now, seems like a big change. 

**Stokes**
* Right. Okay. this one was also coming from Yasuke, so, yeah, unfortunately, he's not here. But, yeah, we got a thumbs up from Terrence as well. Okay, I'll try to reach out to him as well about this and, get a better sense of how much he wants to push for this and on what timeline? Cool. 

# PTAL: eip7251: Bugfix and more withdrawal tests consensus-specs#3979 [14:02](https://youtu.be/p3FRr5umt4U?t=842)
**Stokes**
* Then next up, we have a bug fix to some of the max ebb things. This is PR 3979. and I think here the ask is just to take a look. it does look like there is another issue with, withdrawals, handling and, Yeah, as far as I know, this is a straightforward bug fix, and it should, should be merged, so. Yeah. Client teams. Just take a look if you have a moment.  Mikhail is here. I don't know if you want to add anything else. 

**Mikhail**
* Yeah. Thanks, Alex. But, yeah, I don't think it's quite straightforward, as you mentioned. So just take a look, please for the proposed fix. 

**Stokes**
* Cool. Thanks. And nice find. I think we definitely need a round of testing and review, around the specs. And one way to help that is to get to a stable Pectra spec. So, again, I think we're migrating to that regime, and hopefully there are cycles over the next month or two to really flush out any bugs. 

# support SSZ encoding for builder APIs for Pectra [15:11](https://youtu.be/p3FRr5umt4U?t=911)
**Stokes**
* Okay. Next up we have an issue, or at least a proposal to think about as a SSZ support for the builder APIs. So here, let me grab a link to at least this TR here. So this kind of came out of came out of some of the request handling that we were talking about with these execution layer requests going from the EL to the CL. And there was a lot of discussion around how do you structure these, like is there a JSON encoding? Is there an SSZ encoding? And in any case, the same question also comes up with the builder APIs. because then if you're a proposer going to talk to, say, some builder, they have to communicate these to you as well. And the builder APIs right now go with essentially this like JSON encoding that deviates a bit from the engine API.
* And this point was raised as a way to kind of have at least have the option for both, kind of get the best of both worlds via direct SSZ support. the question here for the CL teams at least, is that you would need to support this in your client to talk to boost. And from there there's other like infrastructural things that would need to change. but I guess the first point there is like these other players, like relays and builders generally also support this. 
* It's, you know, lower latency for them, which they like. And yeah, so it would make a lot of sense. The question then is though, you know, the question then is that you need CL buy in as well. So the proposal concretely would be to go ahead and say this is like a, you know, sort of official part of Pectra. You would, expect to have your client have support for this with the Pectra Hardfork. And yeah, I think that's the context there. Anyone disagree or feel like that's unreasonable to aim for? Dustin asked someone was going to talk. 

**Sean**
* That was me. I was going to ask. I was going to ask. it looks like the PR is meant to be backwards compatible. So are we expecting, like, relays to support, like this in a backwards compatible way, which would mean, like, this would actually be, I guess, not mandatory for clients. Not not that I don't think we can or will implement it, but. 

**Stokes**
* Right. So my understanding is that you set essentially like a header in the request that just signals you can work with this transport and then you go from there. And yeah, the idea is to have sort of the existing again this like JSON encoding. Then also just the option for SSZ. 

**Sean**
* Okay. Gotcha. 

**Nflaig**
* Yeah. Also I think Pectra would be a good timing to address this or to test this as well. And because I think this was proposed two years ago already, and even though it's backwards compatible, I think having a stricter timeline maybe pushes it a bit. And yeah, CLs don't even need to implement this. But of course, if you want to profit from the latency gains, then because we only need to implement the client side. So it's mostly important that relays and sidecar software implements this. 

**Stokes**
* Right. So it sounds like there's general agreement that this is interesting. one thing we'll definitely want is support of this in boost. so yeah, that's something I can work on with the relevant parties and then separately. Yeah. CL teams just keep this on your radar. I don't think it's a huge lift implementation wise. and yeah, we can go ahead and also get the PR merged. That's a good first step. so have that into the builder specs and then. Yeah, from there, let's aim to have support for this along with Pectra. And then that can be part of the Petra testing as we move along to main net. Does that sound good to everyone? 

**Nflaig**
* But there was one more question. Also. We discussed on discord, which was basically who will profit from this latency gain? Because I mean, builder could just eat it up with playing timing games, for example. And then in the end there's no real latency gain. But I think since this is also it's in the response of the Getheader request and also in the when you submit the blinded block. And the main latency benefit would be in the second part when you submit the block. So and since we have a strict timeout on the header implemented in clients, I think timing games would not be a profit from this extra latency gain. 

**Stokes**
* Right. I mean, also with SSZ encoding you use less bandwidth, which will be nice in any case. And it also does harmonize with where we might ultimately want the engine API to go, which would also have an SSZ transport. So I think it makes sense. even putting aside that question. Okay. I can move ahead the spec things there and, yeah, let's just keep this on our radars for Pectra. Okay. Next up, I think we just generally have like, a sort of, notice, especially for application developers who happen to be listening. So we have this concept of generalized indices, which basically correlates to, with the SSZ against realization scheme that we use on the CL.
* There's a corresponding localization scheme. There's a way to identify nodes in this Merkle tree for each type that we have on the CL and it facilitates light clients. And you know, anything that looks like a light client for current purposes. It looks like the beacon state then will cross this like key number of like a power of two, in this case 32, which basically means that the current leaf structure gets pushed down a layer. And so these these like fixed numbers all change. The concern here is that if you're writing an application against these things, there's no way at the moment to be abstract to them. And so you need to also update, say, your smart contract. 
* So yeah, I think the ask here is just to flag this again. If you're using things like say 4788, which is the parent beacon block route EIP that we've had, or yeah, different things like this. If you get if you reason about these generalized indices in some other way in your smart contract. Right now with Pectra there will be a breaking change. So, presumably this makes sense to you. If it doesn't, you probably don't need to worry about it. But please be aware. And yeah, Mikhail, you had the comments. I don't know if there's anything else you wanted to add to that. 

**Mikhail**
* Yeah, I just want to add that Ethan proposed a potential solution to not cross this mark. This time, we could group, some new fields into into some logical groups based on, more on request stuff, like withdrawals, consolidations and deposits. So there are going to be three groups and we just put, every new introduced fields in one of those buckets. But, yeah, from my perspective, it's kind of like, artificial, more artificial. And. Yeah, but that's one of the potential solutions. so not breaking, not introducing this breaking change right now and maybe in the future. Once we have a stable container, we will break this thing just once and we'll not have to deal with it after those containers are introduced. So yeah, that's one of the workaround for this problem.
* Just to use kind of logical grouping of of the new fields. But I'm kind of like personally inclined not do anything unless there is a strong reason for that. Like something is completely broken. So that's just a comment I wanted to share. 

**Stokes**
* Yeah. No, that makes sense. And yeah, that's a good option. if it was like a huge issue, I guess it's worth reaching out to some of the like, for example, users of 4788 and running that by them, but otherwise. Yeah. it's probably good just to have this be known and move ahead as is. Because yeah, we could think about restructuring the beacon states, but then they'll just be some more code thrash, which is not ideal. Yeah. 

**Mikhail**
* And so basically, yeah, even even though we are relying on stable containers introduced in the future, this is going to be a breaking change as far as I understand. So these 4788, you can block routes. yeah. Like the applications using them will have to be updated anyway at some point in time, whether we have stable containers or whether we're just increasing the number of fields in the beacon state in the future. So in any possible way it will be, it will happen. 

# Brief update on EIP-2537 breakout call [25:19](https://youtu.be/p3FRr5umt4U?t=1519)
**Stokes**
* So next up, I suppose I just wanted to give a brief update on, this breakout on EIP 2537. This is entirely an EL concern, but there was a breakout call that we had, and we kind of came back to this core question of how to structure the APIs to the Precompiles. And there's a bit of a trade off here between like user safety and essentially cost or performance with how we think about some of these features, like if you want to get into the details, there's a notion of a subgroup, a subgroup check that is very important for the cryptography. but yeah, then the question is just like the right way to structure these, essentially the inputs to each precompile.
* So I think I'll just flag that for now. Again, if you're listening, and especially if you expect to be a user of of these features on mainnet, say for example, you want to use you want to verify zero knowledge proofs that uses curve on the chain. Also the use case of like validators and signatures. So this EIP does let you reason about validator signatures Trustlessly in EVM, which is really cool. And that all being said, yeah, please reach out if you think this concerns you. We would love input. to help answer the question around the right way to structure the, the some of these details of the EIP. Cool. Okay. That was everything on the agenda for Electra. Any other comments about that for the moment. 

# PeerDas [27:06](https://youtu.be/p3FRr5umt4U?t=1626)
**Stokes**
* Otherwise we have PeerDAS. Next up. Okay, then. Yeah. The blobs. Our favorite Ethereum feature. So I think to get started. Well okay, even before that, I'm assuming there aren't any substantial updates with the PeerDAS devnet. 
* From what I've seen. so I believe there was a breakout this week. And yeah, I think clients have been working through maybe some syncing issues there, but otherwise I'm not. I don't think there are any, significant updates on the on the Devnet status. 

**Barnabas**
* Nothing. Cool. Thank you. 

**Stokes**
* So that being said, there are things we can think about in parallel. One of them is this PR which pairs actually with this engine git blobs v1 method that has recently been merged. And there's a question around clarifying sort of the P2P spec here for an honest node. Last call, we discussed this, and essentially we got to the point that, yeah, this PR makes sense. I think the key question here being like, if you get a blob in this way, say from your local min pool, should you then treat it like you've received it from gossip from a peer, meaning that you then gossip to other nodes? So yeah, I think at this point everyone's in agreement on this being the right call. And so we'll go ahead and merge this. I'll bring it up now just sort of as a final call. any comments or questions on this? 
* Okay. Then I think we'll look to merge this even later today. Cool. And then I guess, you know, related to this, I was curious if there are implementation updates around this feature. you know, we can think about ways to structure this where it does provide significant bandwidth savings to nodes. I know last time clients had been looking at this and get blobs gearbox V1 and there is a variety of different states of progress. Any clients care to give an update on this now? Yeah. Terence. 

**Terence**
* Yeah. So we have our implementation since last week and then we have been testing it on the wild. And I wrote a report yesterday. Let me see if I can drop it to the link. But the TLDR is that like the hit rate surprisingly to me is really well. So I was able to recover like one blob sidecar per 12 seconds over like four days. And that's pretty good if you really think about it. Because like say today the target is three. That's kind of assume that you can get like 33% of the blob side passes over the main pool. And then because of that, the import time of the block turns out to be much faster because typically my node waits about like 100 to 500 milliseconds waiting for the blob.
* And now that time is just basically gone, because I can import the block faster without waiting for the block cycle over the wire while and then. So that's one benefit. I did see that I have received less block P2P message over over the gossip sub, and I think that's pretty good as well, but I cannot I couldn't quantify how much like bits per second or megabits per second that's saving is. Right. And then the last thing I observe is that because of that, I am the fastest node on the network in a way that I receive the block the fastest, but it turns out to be sending more blobs out. Right? Because now it's kind of the trade off, because I am on the other end of the spectrum that I am, in a way receiving block the fastest. Therefore, I reduce my download bandwidth, but in parallel, since that I want to serve nodes.
* Because of that, I it turns out to be using more upbeat. I think that will change when more nodes have this feature and then yeah, that's basically my update. 

**Stokes**
* Cool, thanks. is there some way to think about throttling your use of the uplink? You know, assuming you get a blob from them and pull in this way. 

**Terence**
* Yeah. Lighthouse has a write up, which I haven't reviewed, so they're thinking about a similar concept from the PR perspective. Right. So it does make sense to kind of play the trade off fast, to kind of play the trade off in a way that if today you're the fastest node, you kind of want to throttle your, upload. So you can wait, maybe wait a little bit before you broadcast the blobs. 

**Stokes**
* Hey, Enrico? 

**Enrico**
* Yeah, we implemented it, and we also released it and is currently working on mainnet, with bezel correctly. We got problems with Nethermind and yeah, waiting for other clients to to release and test. Currently the tech implementation due to what what Terrence said, is not, using it immediately when you see the blocks. So we wait at least half a second before doing this just to avoid, yeah. To be the super fastest node, faster node than has to be, has to publish. Because actually we  Yeah. Essentially this this this this waiting delay is happening on the attempt to try to recover instead of recovering and then wait before publishing. So yeah, this was the first since we were really one of the first clients implementing it, we decided to go first in this direction. And by the way, we saw a lot of nice recovering.
* So we are systematically grabbing blobs from the EL and this reduced all the attempts that Teku tried in the previous implementation through through recovery via RPC. So we were historically pretty aggressive in trying to recover late blobs. And now though, this thing went down a lot because we try EL first. So so far so good 

**Stokes**
* Oh yeah. That's really exciting to hear. Okay. Anything else on that? Sounds like. Yeah, progress is underway, I guess. Again, I don't know if there are any EL's on the call. but yeah, the more EL's that have this implemented, the better. 

**Sean**
* I was curious if you know how many of the blobs are in that period were expected to be seen over the public pool, because 30% seems lower than I would have guessed, because I had the impression that 80 or 90% of blobs were coming over the public pool. 

**Terence**
* Oh yeah, but then the problem here is that the relay and the builder, they purposely broadcast the blob sidecar before they broadcast the block, right? So because of that, I'm sure the number would have been higher if today they do the reverse. But since that I am receiving blobs called a first before I receive the block. Most of the time it kind of. Yeah, it it it kind of messed up with the number here. 

**Enrico**
* Yeah, essentially, he's not even trying to get it from the EL because he got the blobs first, right? 

**Sean**
* Okay I see. 

**Terence**
* Yeah, yeah. 

**Stokes**
* Doesn't that kind of defeat the point of this being a balance saving thing, though? 

**Ansgar**
* Well, it does not. If the stat is meaningfully different between relay blocks and homebuilder blocks. Right. Because homebuilders do not do this. And we primarily want to help with, the peak bandwidth for their blocks. Right. So it would actually be really interesting to see that stat broken out between the two types of and. 

**Enrico**
* And what is important is the local building here. so when the relay is involved it doesn't really matter because anyway they will they will gossip everything by themselves. But when the when the proposal builds locally, this is where things get interesting. And the local recover really matters. 

**Stokes**
* Right. Terrence, did you have a chance to look at this in the write up you had? The breakdown between relay blocks versus local blocks. 

**Terence**
* That you got. So I will follow up on that. 

**Sean**
* Just feels a little weird because, you know, the nodes have already done this work to get the blobs over the transaction pool. And just because the relays are sending out first, we're not able to take advantage of that work. 

**Terence**
* I also suspect that it will mostly likely be the case because of the timing game. So the relay, their incentive is basically to gossip the block as late as possible to the into the four second mark. Right. So today if we ask them to maybe send a block after, then they would just presumably just censor the blob, I presume so I don't. Yeah, I think that's kind of. Yeah, I think that's kind of I think I think that's a hard one. 

**Enrico**
* To be fair. What I think it will happen is that the players even start. not not sending anything over the P2P in terms of blobs just sending the block when, when the majority of the network just is able to recover from the local EL sending the blobs there and the the EL the CLs will anyway, send will anyway recover and send over the P2P the blobs so they, they will do their work. 

**Sean**
* Is there a way to receive a like blob sidecar header? And then before requesting the full blobs from the P2P, ask the EL. 

**Stokes**
* There isn't today. I mean, we could think about that, but it also then is going to complicate things because you like the delivery becomes like partial, right? Like you could have this header state or you could have the header plus payload state, meaning the blob sidecar. Right. Well, in any case, I think this is really helpful. and, yeah, if we could keep drilling into these different metrics of how this actually works live on mainnet, that would be super helpful. to get a better understanding. And, yeah, maybe there's something downstream, Lightclient was suggesting, to deliver these bandwidth savings with this feature.

**Dustin**
* So 11. regarding that, I guess I'll, I don't have a strong view on it yet, I guess, but right now it's explicitly marked as as optional. And I understand this. I think it makes sense as, as introduced in its PR to be optional. because it was not had not been explored the way people are exploring it now. But if we continue to pursue a certain direction that that is being looked at regarding increasing blob space with. And here's the crucial part with the key assumption of it is okay, precisely because of get blobs. And it would not be okay without get blobs. Then I would suggest that the optionality of that be reassessed. 

**Stokes**
* Makes sense. So yes. 

**Saulius**
* Yeah. So I'm interested in kind of, implementation detail here where when we receive a block from, from P2P, this is like, event driven. so, so whenever we receive we just get it. And for  EL we just, mostly pull it, so let's think that, that this, optimization will be implemented. So is it, so the current thinking is that we just, pull EL in order to get, the blocks that EL has whenever we see the block, for example, or, there are discussions that, there may be some, some other way to fetch the blocks from EL. 

**Stokes**
* I believe it's just the first path. So I mean, one way to think about this is it's like another availability sort of avenue for the node. So, you know, you get a block and there's some blobs attached. You need to know that the blobs exist. They're available. And gossip is one way, but the mempool is another. The idea being that at least currently, most blobs are in the public mempool. At least that's sort of our working assumption. the data might suggest otherwise. but in any case, the idea then is that you don't really need to wait for gossip from a peer. You can just go to your local mempool because, you know, in some sense you just already gossip this at the EL layer so the CL doesn't need to like, wait. 

**Saulius**
* Yeah, but, so according to the data, it looks like if a CL block arrived, then I just, ask EL once, and I should get the blobs. So there is no some, no need for some extra, more complicated more event based approach. Here is is it correct? 

**Stokes**
* Well, the issue that just came up was an interplay between this feature and the relays and like the external pipeline because, basically, I mean, it sounds like what was happening is that the relays send out the blobs before you even really think about this. Just do the way like the blocks and blobs are disseminated from the relay. So yeah, to the extent that we also want this, like to the extent we think this will be a savings for bandwidth, for all nodes, even if you're talking to relays, then we'd need to think about some refinement of the mechanism to actually let us get that, because we can't get it right now. 

**Saulius**
* Okay. Thanks. 

**Stokes**
* And, yeah, maybe just to close out the point like we were probably mostly concerned about, nodes not using the relays. So, you know, I don't think it's necessarily a blocker, but it is an interesting interaction between these two different parts of of main net. Cool. Yeah. Thanks everyone. That was I thought really helpful discussion. Next up. yeah. This one might be a pretty straightforward yes or no. The question is just whether to rebase, PeerDAS onto Electra. This is certainly the intent. And then it's just now a question of timing. I don't know if this came up on the breakout this week, but I believe this PR is ready to go. So it's just kind of coordinating with client teams and, yeah, making sure that everyone's okay with, moving ahead with this and the specs. Dustin, I'll assume you're answering yes to this question.
* Any other client teams want to hold off? Okay, we got to do it. That's good. Doing it. Okay, cool. Anyone not ready? 

**Barnabas**
* Anyone working on your PeerDAS already? I think this is going to delay the next subnet, by potentially a couple of weeks. 2 to 3 weeks, even. 

**Stokes**
* The next period of subnet. 

**Barnabas**
* Yeah. If we're going to be requiring this. 

**Stokes**
* Was it anyone at the breakout call? The PeerDAS breakout call this week? 

**Barnabas**
* Yeah. The general consensus was that it's better to do it sooner than later. So everybody seem to agree with that. so that just the two branches don't get too far apart from each other? 

**Barnabas**
* But yeah, the, the major issue is I think that we don't have a stable PeerDAS network right now. So it's just going to complicate things a bit more for us going forward. 

**Stokes**
* Right. I mean we will have to do this at some point. And so the question is just like yeah, do we take the pain now or later? I would lean towards merging it. okay. How about this? I can try to reach out, to different CL teams and in particular the people working on PeerDAS on those teams just to do, like, a final check, in the next couple of days. but yeah. Otherwise if not, then I would expect to see this merged. definitely before the next ACDC. Cool. Let's see what was next. Okay, so yeah, to round out the blob segment of today's call, I believe, Francis was here and even wanted to give a presentation on some of his analysis. are you here, Francis? 

**Francis**
* Yes. let me share my screen. 

**Stokes**
* Okay. 

**Francis**
* All right. okay. So more blobs, I believe everybody, like or like most of us, on this call have already, like, reviewed this talk. So I'll try to be quick and, like, just reiterate on some of the importance, like, points, I guess. so, the analysis is broken into, like, I guess three parts. First is Firstly, like why we want to like increase the blobs and secondly like what? What's the current problems. And then thirdly, like what's the kind of like solutions to alleviate the concerns for those problems. so the first section is like why the urgency? So these two pictures I just took them from last night, and you can see that the blobs are trending toward the target, the three blob target already. so that comes to the first point.
* Like the existing consumers are like continuous to scale and based on that, have plans to increase their scale and increasing like significant increases in blob usage.
* For example, uh base has increased, started to increase like the gas per second from like late September, and it has increased from ten megabytes per second to 14MB per second as of yesterday. So a lot of those changes are kind of like eaten up by the base scaling as well. the second point is that there are new chains trying to join and use blog space. For example, Uni Chain recently just announced and they are aiming to launch with blogs at Da later this year for their mainnet. So that's kind of another, new blog like requirement. The third part would be the loss of opportunities for other l2's if they see that, okay, it's already our target and the Da is going to be super expensive, then they are probably gonna like reevaluate it and maybe go with like all Da solutions or some other things. 
* So, I guess to quote Vitalik, we cannot afford to let the momentum slip and moving more layer twos over to using blocks. so what are the concerns today? there are like very legit concerns about, like, different aspects of the network. And I think the from what I gathered, there are two like main concerns. The first one is that solo stakers, their proposed blocks can be like reorg due to their low upload bandwidth, because they cannot gossip out their blobs and blocks like in time for them to be tested. So that's like the first concern. The second part. The second concern is that if we increase the target number, that could potentially impact the network, like sinking performance, especially for the unhappy case where the network like does not finalize.
* And everybody needs to catch up with like thinking the historical blocks, but also have to keep up to the tip of the chain. So there might be some added bandwidth there that might push things over the fence. So, what we are trying to do is to like take a look at this like situation in terms of like block bandwidth, in terms of bandwidth from a first principle like perspective, and try to really see, okay, in the worst case scenario, what are the upload bandwidth needed to be able to like fulfill the network requirements. So before that I'd like to reiterate reiterate these things. the some of the things that we are not talking about to just focus us on the same thing, the same problems.
* So first, we are not going to focus about block based fees. we believe that it's important here, but they are kind of like orthogonal to the analysis. 
* And with the current flow of markets close to being saturated, we believe that the entire kind of like fee discovery will happen very, very soon. The second part is that we will not talk about like solo stakers who have MeV enabled. So this is specifically for the solo stakers who are trying to propose in that situation. So I think for this situation, there is broad community consensus that with MeV enabled, the burden of distributing blocks and blocks is offloaded to the Relayers. So not the solo status. And we're not going to talk about timeouts and fallback to local building situation because it should happen very, very rarely. And the assumption is that download bandwidth here is not the bottleneck. At least we didn't hear anybody complain about.
* They cannot download things like in time, etc. and in most places download bandwidth is much higher than upload bandwidth. okay. So this is like the things that we are not going to talk about and the things we are going to focus on is like the solo speaker that does local building and tries to propose their blocks to the entire network. The true bottleneck here is basically, I think, the number five step where the after. It's kind of like the proposer, the **Dustin**ike builds its own block. It needs to like gossip out both the block and blocks over the P2P layer on the on the consensus layer side, and it has to happen within four seconds of the slot to get majority attestation.
* And, it's If semiotically like this should be a bit faster so that like it can propagate or disseminate properly throughout the network. So with that we have done some like um first principle analysis, like we using very conservative and numbers and some of them we use the like empirical data that we observed from the network. **Francis**
* And also using the worst case scenario data for flow to illustrate the need. So for example, for situations like the worst case upload bandwidth we observed is like 300kB per second, as shown. Like, sorry. Uh. Thank you. Okay. Never mind. I think he's here like 300, like, kilobytes per second for the upload bandwidth. and there are, like, other points that I'm not going to go through, like, point by point, just in case of time. But one thing I want to call out is that for the calculation we are using like two seconds of the window of transmission for the three layers to broadcast to all the things out, blocks and blocks. So some people have like mentioned that maybe two seconds is not enough. But the general the general sense of this calculation is that to showcase, okay, what are the kind of like approximate like network bandwidth we need with different block numbers.
* And the and then we can lead to the like optimizations we have and see what are the benefits of those optimizations. So we don't need to like actually like look at the numbers here. We just need to know that okay. For different blocks, like the more blocks you have, the more like upload bandwidth that is required. So, what can we do here to basically make it safe to increase the block target and block number? And I believe we've discussed extensively about the engine like GitHub blocks we want that is already showing like very promising results from both the lighthouse design on the pier that, dot net, and also from like Terrence who just did the like analysis from his like own nodes on the network, which showcases that the block import time is like much faster. 
* And there are benefits of the reductions on like download bandwidth and for the upload bandwidth like we are, I think we will continue to monitor the network and once more and more, nodes with this new kind of like changes, like being like online, then we should hopefully see that the upload bandwidth will like decrease as well. The point here with the engine Getproperty one is that with that, the core layers doesn't have to broadcast the blocks out during that stringent time window, thus relieving the like peak bandwidth, peak upload bandwidth they need. So if we might use that and deduct all the like CL needs to gossip out the, like, blobs. We can see that with five blobs target and eight blobs. Maps, maps. The actual like peak and peak upload bandwidth need is low, even lower than three blobs, although like you still need to like gossip out those blobs. But it doesn't have to be like that quickly.
* And there are optimizations that has already been talked about like a little bit prior basically means that, okay, we can potentially like delay gossip blobs a little bit later so that it doesn't mess up with the block gossip and also maybe potentially save some like block bandwidth if you can, if all the other people can get their like blobs like from their local pools. So the client readiness parts I've done some like search by myself. This probably is not like entirely accurate. But so for the other side I believe nevermind, nevermind. And Basu has already done the implementation for the engine block V1. Gas has a PR ready and everyone has an implementation yet for the CL side. With what I know is that Prysm and Lighthouse are about to release a new version that supports utilizing this new API. 
* So the point here is that it seems like most of the clients are ready or almost ready, and if we make it kind of like the into the hard fork, then everybody like after hard fork should have this change and should have or like potentially will have like a lot of like savings for the network bandwidth. The second point is to disable publishing. I think this is more about like Kotaku and they are already releasing that already. So I'm not going to talk about this extensively. And the third part is like implement. I don't want P2P protocol messages. And from the like multiple researchers that are we've seen, it seems like with that we could resort to like 330 to 50% traffic reduction And some of the latency reduction as well. But understand that the these are kind of preliminary numbers and will the results will like we will see it on the minute to be sure. But these are definitely like promising like, advancements I guess.
* So there are like another one which is proposed by Ben Adams, I believe. And we to suggest that we adopt like P2P like quick so that we will have like a better RTT latency. And I think this could be a good add as well. So with all the like improvements, I'd like to go through the like proposed options here. so we believe that with the suggested like modifications, if we take it at the face value right now, it will be safe to increase the target to five and max to eight without basically increasing the load on the various, like, solo speakers. And also because the blobs are almost close to being saturated, it would be great to have a little bit more like 66% more like blob capacity, just for the like interior to space or for Ethereum to scale as a whole on top. 
* That's coming into play like after Petra. And regarding the work, I believe that with the required work is like implement this one engine capable to be one implement. I don't want message which are already being done mostly by or like majority of the clients. So you shouldn't add a lot of like extra work or workload on the client teams and hopefully they should they could be done within like 1 or 2 weeks of time window. And with that there are other options like we don't increase or we just increase this like target to for to give a little bit more Capacity to the network. so the, the actual like path forward that we want to recommend is that, there are I think the, the right approach with this is like, let the client teams to implement this and roll it out to their network, and then we use the real network data from minute to see, okay, how much bandwidth do did we actually save.
* Let's say is if we see that with this we saved like 30% of the network bandwidth for upload link. Then with the extra like blocks, it should be like on par with previous prior requirements or even lower. Then it should be safe to like increase the block number, at that time. So the proposal is that client teams like implement the mentioned features and changes and make them make the releases releases as soon as possible. We let it run on minutes and observe for some period of time and answer the questions like, okay, can we get more blocks directly from Yale without having to download them from the cloud layer. Like all sorts of optimizations that we can, we can do and have all the data ready. 
* And then if and when we observe the real benefits to the metrics we care about, which hopefully we will, then we officially commit to the change. And on the off chance that we don't see enough improvements, we fall back to just increase the target to four. I believe that's it. Any questions, comments or suggestions? 

**Stokes**
* Thank you. that was really great to see. There was also a lot to digest. but yeah, I mean, I think the different options you laid out at the end, could be really promising. Fast forward. Anyone else have any feedback at the moment? There are a number of you that left comments on the doc I saw. Okay, well, so I do think this doc helps ground the conversation around like potential options for changing the blob parameters and Pectra and otherwise. Yeah, it's like your Saint Francis. If we have a little more time to gather some data that will help inform the decision. 

**Ansgar**
* Yeah, I was just wondering, so it seems, general consensus that we want to kind of make a call on this a bit later into the fork process, but I was wondering at what point would it make sense to if we at least think there's a reasonable chance we want to increase, include a blob increase that we, add that to the to a devnet. ideally I would, I would argue for like the most ambitious version of it, say, I don't know, 6 or 9, add it to the devnet. Just so we already have kind of make sure double check that that the actual kind of making the change on the technical side does not run into any issues. Obviously, that itself wouldn't give us like much data on like, you know, the real world kind of constraints. But but still, would that make sense or would we want to wait with that until we made the final decision? 

**Francis**
* I think how can we do this? Like, can we maybe, like, soft commit to this change, like to this increase on the call so that we can both do it on the devnet, like in Pectra a little bit later and also like, try the changes on the main net to gather like information from both sides. And with that we could like have more data and more basically informed like information to make the decision like finally. 

**Stokes**
* Yeah. I mean, I don't know what exactly we mean around soft committing to have this infection formally, but definitely I think everyone has soft committed to, you know, answering the question. so, you know, from there there's a question of, yeah, do we want to touch, the blob counts at all. And then if we do, there's a question of how, Barnabas brought up this comment. And  7742, I think is generally our answer to this. anyone feel. Well, I guess one thing is, you know, maybe just to confirm, has anyone started thinking about 7742 implementation? or is that not really where we're at at the moment? The strategy here would be to, like, have 7742, because it becomes far simpler to actually change these numbers. and then from there we can think about actually changing them. Especially I think this is more attractive if we want to think about Experimenting with different numbers, say, on a net.
* My understanding is that it's really hairy to actually go and make changes to these just given implementations today. 

**Barnabas**
* I think this can potentially push the hardfork back a month or even two months, assuming that there's not a single client that has any implementation with 7742. So if we do want to increase the blob count in picture, then we really need to relay on 7742. 

**Speaker N**
* I'm curious. 

**Francis**
* Is it possible to just like do a hard increase? Like like hard coded increase for now and not adding like, something for two? Because it seems like it's not like entirely ready. And it does require extra bandwidth for like both SEO and a year to implement that. 

**Barnabas**
* As far as I know, there's not like a single constant that needs to be bumped up, but it's like multiple different things and multiple different libraries that have to be recompiled and stuff. So it's not a very straightforward change. 

**Stokes**
* Yeah. So I don't want to distract people from devnet 4. But we could consider on the next ACDC revisiting this question around 7742, with the idea being that we are going to make some blob target or max increase in Pectra. Does that sound reasonable to everyone? 

**Ansgar**
* But just one one last question on this. If we say that even now already, basically if we if we were to start prioritizing it, it would it would possibly create a one month delay or more to the hard fork. Wouldn't that mean that, like, if we only think about this in two weeks now, we are basically adding two extra weeks of physical time on the critical path of shipping this if we decide to still include it into the hard fork. Like if this is the case, we should probably just make the decision as early as possible. 

**Stokes**
* Right? And so I mean, that's the thing. Like if a client team has time to go ahead and start with something for 7742 before the next call, that's great. but again, like we should focus on Devnet4. And this is what we had said with like this original split decision was like we focus on the core factor stuff. there is in, you know, for very good reasons. The point made that we should really think about the blobs and picture as well. So we're just here at this moment in time. And yeah, I mean, that seems reasonable to me. I don't think, you know, just adding 7742 is going to add like a two month delay. You know, don't hold me to that. But that sounds like a lot of time. Especially if it's like the exclusive focus of all the different CL teams. So that being said, it seems reasonable. because, you know, we'll launch for tomorrow. There might be bugs and then it's it's the whole thing.
* So, I mean, yeah, that being said, to your point, Ansgar, yeah. Various CL teams, EL teams, if you're listening, if you have bandwidth, like, the sooner you can start thinking about  7742, the better. if you could even have it implemented in the next couple of weeks, that would be amazing. 

**Sean**
* So is there any is there syncing concerns with  7742? Because if we don't have the if we're being driven by the CL, we need to validate the blob limit the blob target. We're going to have the same types of issues that we're having with requests and we're optimistic syncing. 

**Stokes**
* Yeah, I believe we work through these questions with the EIP already. And so I think, let's see, I think we settled on having the target in the header for this reason. 

**Sean**
* Got it. I mean, I think we. 

**Barnabas**
* Need both actually in the header. 

**Sean**
* Yeah, we need the max. 

**Barnabas**
* We need the target and the max, too. Yeah. Especially if you want to have different values. Not just always half of it. Yeah

**Sean**
* Yeah. That's a good stab at implementing it like a month ago. And it seems okay. It's not a one line change by any means, but I would much rather do it than hardcoding new values then. But I am curious, like from a CL perspective, how difficult it will be to drive this new API. 

**Francis**
* It seems like from the like chat people have not like really looking to like implement it, but they are down to start implementing today. So maybe we can do this async and understand a little bit more. Well, like people are trying to implement it. 

**Sean**
* Sure. I'm just curious. Like what when do we cut a Pectra spec release for mainnet, and we started forking test nuts because we're talking about making this decision later. But I feel like we're right now already rushing towards wanting to fork testnets 

**Francis**
* I guess, do we have any like, optimizations or like, objections to doing it this way? Just try to implement the same thing for 7742 and prepare them for target and max increase. 

**Stokes**
* Yeah. I mean, if the client team wants to correct me, please do. But my sense is that, uh. Yeah. I just wouldn't want this to become a distraction. with the other Pectra stuff. So, like, my sense would be kind of what I said. I mean, look, the other way to think about this is we can have latency and make a decision on a ACD next week. that actually might be the way to do this. And yeah, if we can get implementations, the sooner the better. I just wouldn't want this to become a distraction for the other. yeah. The other Pectra stuff. 

**Terence**
* May I ask what other Pectra stuff are there? Because my understanding is that devnet four consists of older APIs, right? For Pectra. So if you're if you're deep net four ready, you're mostly maintaining the feature set, right? Finding bugs and stuff. So another question is that whether do we include this EIP and have a Devnet 5. Or do we just cut that Devnet for short basically. 

**Stokes**
* I expect we'll have a Devnet five. You know We'll launch them before you even say tomorrow. They'll be bugs that will take up some attention to fix. but yeah, I mean, okay, like, do we want to commit to moving ahead with this today? It does feel like process wise. I mean, yes, like I think we all agree, but like, yeah, like I think I didn't. 

**Barnabas**
* Agree to include this, by the way. Well what is what is talking about this. 

**Stokes**
* What is what is this. It's 7742. And then a commitment to change the bulb count somehow, right? 

**Barnabas**
* Well, I would I would commit to 7742. And then we can discuss all the changes later on. But 7742 two will be a requirement for peerdas anyway. So might as well discuss about including that and then just, pressing the bulb limit once every client has actually implemented it. 

**Stokes**
* Okay. I do think we'd want to have all the ELs also buy into this, but we could go ahead and say today, are there any CLs who are opposed to 7742? And moving that to I think we call it scheduled for inclusion now. Okay. Anyone disagree? 

**Stokes**
* I will assume that's unanimous consensus then. so right. If you have time, please move ahead and start looking at 7742 implementation. And I'll be sure this is on the agenda for next week. And again, I don't really expect any surprises. but then yeah, we can move ahead and yeah, just keep moving towards a blob increase for Pectra. Okay, we have a little time left, and there were some. Ask for another set of EIPs. Are there any other final blob points to make? before we move to those? Anything with Peerdas or blobs or scaling. Okay. cool. 
* So there are two that were kind of related. I'll just go in the order. They're on the agenda. So the first one was 7783. right. Yeah. Let me double check actually. Right. So yeah. 7783. So, this was on last week's ACDC call. And essentially it's just, having some more structure around, how the gas limit would change, assuming there was a targeting within the protocol that would raise it or lower it. let's see, is Julio on the call? 

**Giulio**
* Yes. 

**Stokes**
* Okay, cool. Yeah. Do you want to say more? 

**Giulio**
* Yeah. Actually, I wanted to say more in context of 7782. because this is not, a CL specific. Yep. I just want to give a small introduction. so, yeah. So basically, instead of increasing gas limit in a cliff like manner, you increase it gradually and you can kind of pick away some of the, some unknowns. one of which could be, for example, if you guys don't remember, if you guys remember the 413 status code error. and also, yeah, this app is not part of the protocol. So it's also easy to implement. It's not an hard fork. yeah. So it's basically it's basically, it's basically a country app to Eth 7782 and yeah, that's pretty much it. Next week I will give an update on it. yeah. I just wanted to present it. I don't want to waste people's time on EIP too much here.

**Stokes**
* Cool. Thanks. And yeah, I mean, this was the next one. paired with this one was 7782. let's see, I think. Yeah. This is from Ben. and it looks like you're here on the call. Would you like to give us an overview? 

**Ben Adams**
* Sure. So the the idea of rather than raising blobs or gas, directly, at least initially, would be to decrease the slot time from 12 to 8 seconds, which would also in effect increase the blob count and gas limit in aggregate. UHowever, rather than loading any increases on a single validator by speeding up the slot time, any increases are shared between one and a bit validators. And rather than. So again, this was brought up in ACDE but it's more of a consensus change than execution change. And I suppose one of the most important, questions would be how difficult? technically a change of changing the slot time would be, some. One of the other benefits is for, for instance, based roll ups where their latency is directly dependent on, the layer one latency, outside of things like doing pre confirmations and other more complex changes. So yeah any feedback on what changing the slot time would mean. 

**Giulio**
* So yeah. Yeah. So I. So just to repeat what I said also in the last ACDE about this is that probably this is a good change to have eventually because it makes the chain more lively. But by talking around with some people, especially from the distributed validator camps, they told me that this EIP is punitive because it it actually it actually still increases bandwidth quite significantly. And another concern I personally have is that it may slow down the development of single slot finality, because one of the approaches being researched  is basically trying to just brute force, just brute force with some smart strategy of aggregating the signatures. So having a lower slot times will not help there that much. and, yeah. So these are just my concerns from last time that I just restated the year. 

**Oliver**
* Yeah. yeah. 

**Guillaume**
* I just dispute  Bit the fact that this is mostly an EL change. Like, yes, the change happens in CL, but the history is going to grow 30% faster. and while the performance itself is not really linked to the size of the history, because at least in Geth, we moved those, those old blocks outside of the DB. if the it's going to take more space on the disk and, you know, a typical gas plus lighthouse install is like 1.3TB at this point. if we start making, like, the chain grow faster and faster, which, by the way, the chain is the biggest. I think we're going to have a lot of, validators out there that are going to have to upgrade much sooner than anticipated. is it 50% faster? Like, once you get there, it's 50%. But until now, it's 30%. Okay. My math is probably terrible. 

**Ben Adams**
* 33. on the history growth that's significantly decreased since blobs. because a lot of, a lot of that's called data that has moved off to blobs. And then 404 also. 

**Guillaume**
* Yeah. Okay. That's that's possible. but just, I don't think we should, you know, jump into this without making some concrete measurements. 

**Giulio**
* I have the measurements. I mean, I basically asked for the guys from, I mean, I talked with the guys from Eth Stacker, and they basically told me that whether you increase throughput of gas or not in around six months. validator. In order to comfortably run, we need to switch anyway to four terabytes. So, I mean, since you're basically since the hardware works in power of two, if that's going to happen anyway, might as well just, you know, increase throughput, right. Like if you don't do anything it you still increase the requirements. If you do nothing you increase the requirements. So just make some people happy. I guess that's but yeah. so that's the answer to your question, but I think this should be discussed in ACDC probably if anything. 

**Ben Adams**
* Any feedback from consensus plans? 

**Stokes**
* One thing I would say is, you know, the slot time is very critical to many, many things, in the protocol and also with implementations. One concern I would have with this is that, you know, it might sound pretty straightforward, but then ultimately has like all these huge implementation load, sort of like with the attestation EIP we have in Pectra, where, you know, it only sounds like it sounds pretty self-contained. But then again, just given how critical this concept is to like the protocol and its semantics, it does, you know, it implies like a lot of, a lot of work. So, yeah, I mean, I agree with others that we should, you know, sit more with, like, the actual performance benefits and, you know, weigh that against what we're actually aiming for.
* One path forward to de-risk the, like, implementation question, would be to, yeah, work on a devnet or something off in parallel, just to get a sense of like how much work this would actually be. Francesco. 

**Terence**
* Yeah. 

**Francesco**
* Just wanted to say that one thing that, might not be obvious is just how much it kind of has the potential to get in the way of future changes to the code, which you might think be things that we haven't agreed upon, might be even things that we haven't even talked about, on a ACDC because they're just research at this point, but there's just like a whole bunch of things that, we might potentially want to do in the future, from Ipbes to IELTS to, all kinds of stuff that do, interact with the structure of the slot a lot. And, yeah, just compressing the slot might, might really not be good for that. I'm not saying that we can never do it, but just I think it's something that we should only do it for in like an extremely deliberate way, like really being sure of what we're doing.
* So if this is really about just increasing the gas limit or, block throughput and so on, then I think in the short term it would be much safer to just do that as opposed to do it in this way. 

**Stokes**
* Was that helpful, Ben? In terms of feedback. 

**Ben Adams**
* Yeah. 

**Stokes**
* Or I mean, yeah, I guess from here, like, would there be a place to continue the conversation? 

**Ben Adams**
* I mean, yeah. There's a, magicians, thread, and I do think it's. So I originally raised the, EIP because there's been a lot of talk about changing slot times, but nobody's actually put anything down to to focus and center the discussion. so sort of putting it out there as something to consider and think about. Because it does impact quite a lot of things. based roll ups, for instance is one, one thing that seems to be seen as a more aligned rollout, but then that has the disadvantage of being quite dependent on, L1 speed compared to other types of rollout. 

**Stokes**
* Great. Okay. any other comments on this for now? My client has a question. How hard is it for CLs to change slot times in general, which I think is a good question. And that's kind of what I was getting at, is it could be the case that yeah, it sounds simple but is actually more complex than it sounds. Do any CLs today have a sense of this? Like is it as easy as just changing a constant or some configuration? Or would it be, you know, more invasive than that? Henrico says it's not simple. Yeah. Julio says it's not. Which I think just lends credence to the other arguments made that, you know, we should be very sure about this and do it very intentionally if we do it. 
* Cool. Well thank you. we are almost at time. There was one final thing, just more administrative. So, ACDC on November 14th, this is right in the middle of Devcon. I would propose we go ahead and cancel that call, because I think most of us will be there. I'm happy to have it if we want it. but yeah. 
* Would anyone be opposed to canceling that call, given that, yeah, most of us will be at Devcon, and if anything can just, uh. Yeah, chat in person or at various times through the week. Anyone opposed to that? Otherwise, I'll move ahead with cancelling that one. 
* Then yeah, I think that was it for the day. Unless there are any other final comments, we'll go ahead and wrap up. Henrik. You're unmuted. I don't know if you had something to say. 

**Enrico**
* Just bye bye. 

**Stokes**
* Okay, then. That's that. Thanks, everyone, and I'll see you around. 



---- 


### Attendees
* Stokes
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
* Barnabas Busa
* Potuz
* Trent
* Jesse Pollak


