# Consensus Layer Call 98

### Meeting Date/Time: Thursday 2022/11/17 at 14:00 UTC
### Meeting Duration: 1 hour  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/660) 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=IK1jNCQz5yk&ab_channel=EthereumFoundation) 
### Moderator: Danny Ryan
### Notes: Rory Arredondo

--------- 

## Action Items and Decision notes from [Ben Edgington](https://hackmd.io/@benjaminion/rJBcqhXIo)

Capella - Alex to keep working on the [PR](https://github.com/ethereum/consensus-specs/pull/3095).

BlobSideCar mutability issue - We will go ahead with full blob verification for now on the testnets and make sure there is no problem in practice. Implementing this is not a blocker for standing up testnets.

Discuss the following on the [issue](https://github.com/ethereum/execution-apis/issues/321):

 - getCapabilities API vs error codes
 - Structure of documentation.

This is not particularly blocking for Shanghai. Comments in the next week for discussion either at ACD next week, or here in two weeks.

## Intro


**Danny Ryan** (1:52) - Okay, we should be live. Great. Sorry about the delay everyone had a little bit of audio issues, but welcome to Consensus Layer Call #98. This is issue 660 on ethereum/pm repo. I think, oh I have just realized so Capella, 4844 are the things that are discussion, primarily under discussion today. And we have a few issues that we'll tackle. Metachris, you wanted to give us an MEV boost update and also have to leave early so why don't we start there?

## @metachris mev-boost summary and questions

**Chris Hager** (2:35) - Yeah, sounds good. I'll try to keep it short and only the most important updates. There was the release of MEV boost 140, which has a bunch of minor improvements and most notable feature is it allows setting a minimum bid value. There is more details in the release notes. Let me paste a link to the updates in the chat here. There's an upcoming post about implications and potential impact of setting various values. Otherwise, there's a proposal and ongoing progress replacing the types of MEV boost with those from a testnet also related to the upcoming changes for Capella and EIP 4844 which have a bunch of payload changes and we need to plant these in and rather than duplicating the work, we've typed in multiple repositories, it seems preferable to use a test and (inaudible). There was, moving to the relay, there was a vulnerability with incomplete block builder, submission validations that lead to incorrect timestamps or preferential values being delivered to CL clients. The CL clients didn't like them and fell back to local block production. I'm posting the full postmortem here in the chat. So that's resolved. It's anyone using MEV boost relay, use version 014, please. It has all the solutions. (inaudible) this uses to (inaudible) beacon API endpoint that is not yet in attacked beacon API documentation. And not all beacon nodes have that implemented. So my ask is consensus teams, please implement this endpoint. That would be usually helpful. Second,

**Danny Ryan** (4:46) - Where is that documented?

**Stokes** (4:52) - It's in the beacon APIs. It's just not, like an official release yet.

**Chris Hager** (4:58) - But here's the link. It's only in the Dev beacon API. And I think all the Teku has this implemented yet and Prysm has to merge PR, but it's not yet in a release. Not sure about the other CL clients. There is big thanks to Justin (inaudible). There is the relay API specs is now in the same format as the other specs in an open API format. In its own repository. We see a relay, relayooor.WTF, gaining a little bit of traction and they slowly ramp up their available payloads. About the builder ecosystem. There's a screenshots in the (inaudible) status update notes that I posted, which shows that the leading builder right now is builder 0x69, who delivers about 2000 blocks in 24 hours followed by the flashbots builders with about 1200 blocks 24 hours, followed by blocks route beaver build, and then a few others. There is a website relayscan, that just shows the the 24 hour statistics on an ongoing basis. And lastly, there are a bunch of flashbots relay updates. And we also open sourced the priority load balancer. That may be useful for anyone running the MEV boost relay, which allows distribution of the block limitations across a number of validation nodes with a high and low priority queuing. Okay, I think that's like a quick run through of the most notable updates. And I'll be happy to take any questions.

**Danny Ryan** (6:57) - Nice, thank you. I was just scanning through the execution API's do we is for anyone that's aware of it. Are we doing the the recipient diff is that in APR to be to come out maybe in the next upgrade a bit execution API's?

**Milkhail Kalinin** (7:19) - We have actually had a raft consensus to not do it. But to do it in other way just computing just a sum of all transaction types. 

**Danny Ryan** (7:37) - Okay. Got it.

**Mikhail Kalinin** (7:42) - Correct me if I'm wrong. 

**lightclient** (7:42) - Yeah. Is that still an extension to the Engine API though? Right. Like well will update the get payload? Yeah. Are you saying it's EL? Well, I thought the EL and calculate the like there's the question of like, who will calculate this like if the EL is going to calculate? Or like how sorry, there's a question of like how you calculate the value of the block. And then who calculates the value of the block? And so if the EL is doing it, regardless of the way they do it, we need to return it to the CL. But are you saying that the CL is going to calculate the sum?

**Mikhail Kalinin** (8:29) - I'm not sure actually CL can calculate this (inaudible) so it should be taking by

**lightclient** (8:38) - Yeah, I guess they don't have the gas use for every transaction. But yeah, yes.

**Danny Ryan** (8:42) - It would still be a field. It's just a matter of what that field the semantics.

**lightclient** (8:47) - Yeah. And there was a PR issue for it.

## [Capella bounded withdrawals sweep](https://github.com/ethereum/consensus-specs/pull/3095)

**Danny Ryan** (8:56) - Any other questions for Chris. Okay. Thank you Chris. Moving on, so I have Capella and then I actually have a point for issue. A Cappella element that we'll start with with Capella. Alex or anyone else can you give us the context on the bounded withdrawals sweep?

**Stokes** (9:34) - Yeah. So we recently changed a little bit how we're doing withdrawals. So there's no sort of formal queue in the stage and instead, rather than process things at epoch boundaries, and you kind of do them every block, and right now the version of the spec says basically in the worst case, we have the entire validator sets. The, you know, obvious question then is if you want some bound on that sweep, and so there's a PR, let's go grab it, but there's a PR that basically introduces a sweep, and it's more just sort of like a RFQ at this or RFC at this point. But yeah, we should decide if we want this or not.

**Danny Ryan** (10:19) - Thank you. Any strong proponents want to make the case to get this in there? No, Potez and Dapplion are on the PTR but are not here. My last comment was, you know that this does add a little bit of complexity. And I don't think there's currently a very strong case for the complexity or at least the value being selected. That said, I'm only kind of weakly against this point. If we don't have the proponents on here, then I will take this up as a priority to get discussed in the next couple days.

**Lion Dapplion** (11:11) - I'm here. 

**Danny Ryan** (11:11) - Oh cool, how's it going?

**Lion Dapplion** (11:15) - Yeah, so quickly. I agree. I don't think it's critical. We have not I mean, we have not run this on a main network. So it's not clear that this would be better. Like it just, it just felt nice from someone concerned with those issues to have that as a bound. But I don't feel strongly for it.

**Danny Ryan** (11:37) - Right, so it's, I wouldn't call it a classic dos because it's not somebody somebody can, or something somebody can induce on us. It's just like the maximum work that certain edge cases will have. But I guess the logic right now for the value is we can we have a validator set today. some fraction of it, we can reasonably sweep, thus found it to that fraction that we know we can do. I guess

**Lion Dapplion** (12:06) - The reasoning for that is in normal circumstance, that value is completely irrelevant, but God forbid we may end up seeing an adverse situation where where that value matters. And in a situation where that matter is probably where the nodes are already overloaded for a particular set of conditions. So having that gives some peace of mind. So I wonder what are the drawbacks of having that in?

**Danny Ryan** (12:32) - One of I guess one thing is additional code that's almost never run, except in adversarial conditions. So then the likelihood of the code atrophying is higher. That would be my main thing.

**Stokes** (12:56) - Yeah, so here's a question for CL devs, like it's about errors that were double in size. Is this an issue to have to like scan the whole set? Like does that make you uncomfortable?

**Danny Ryan** (13:07) - I guess we do that, right. We do that a lot on the epoch transition, but also a lot of work has been put into optimizing epoch transitions and making sure we're doing it early and stuff and I guess, if we ended up in a 4x 10x validator set size here are we are you going to have to put in a bunch of extra work to kind of do pre computation on this.

**Lion Dapplion** (13:32) - So I think the issue is, we risk having to do a full sweep per block, not per epoch and that was more worrying.

**Danny Ryan** (13:47) - Yeah, I understand that. And I guess we'll take the other side of the argument. Now, the if doing a full sweep would require which we almost would never have to do in this case, would require additional like, pre computations than other special logic that would almost never get used than that all of a sudden becomes more complexity that is potentially never having to be used or is only is being added even though we almost never need to use it. So maybe the argument is actually that the these minor code paths prevent having to do all that additional complexity that we almost never going to use. So yeah, I'm

**Ben Edgington** (14:30) - How much more complex is it? Is it not as simple as a bound on a for loop? I mean, is that the.

**Lion Dapplion** (14:37) - It's not that bad. It's just it's pretty simple in my opinion.

**Stokes** (14:42) - So there's like a second dimension too so like, the first thing is bound in the sweep. But then also, there's a question of like, do we want to try to make it like fair in some sense, so you track where you go? And yeah, I don't know. It's like, it's not major, but I do feel like the full thing, you know, does add all this complexity and if it's just for this, like tail case that we probably don't ever see. I think we have to ask if it's that important.

**Danny Ryan** (15:05) - Yeah. I mean, so here's where I say like, I'd rather do nothing. But if doing nothing actually means doing a bunch of like optimizations for this tail end case, then I'd rather do this. So if you think that if we don't add this code paths, that actually means we have to like highly optimize this for a tail edge case. Then let's add these code paths. I've kind of changed my mind.

**Stokes** (15:46) - Do we know though like, do we know if clients will need to optimize like this? Anyone on the call? Want to chime in? 

**Lion Dapplion** (15:56) - We haven't.

**Danny Ryan** (16:03) - But we won't even have to know if we just put this bound and in that case, I'd argue for a smaller bound.

**Lion Dapplion** (16:15) - Yeah, wouldn't have more time to properly answer.

**Stokes** (16:20) - Okay, so yeah, I think I was weekly for and I became weekly against but it sounds like we're going the other way. So let's see if we can make a smaller bound. And then also, does anyone care about this like this fairness thing? Because then it does become like just very, very simple. Sorry.

**Sean Anderson** (16:51) - I was just gonna ask, like, what is the fairness component, like more concretely?

**Stokes** (16:56) - So like, right now, we're gonna start somewhere in the dollar sets and go say like two the 17 validators? The question is, if there are no withdrawals, do you just stay in the same spot every time? Or do you want to advance your pointer two to the 17 every time? Does that make sense make?

**Danny Ryan** (17:13) - An argument that this is not actually a fairness criteria. This is a mechanism criteria, because you could have a range, whatever that bound is where everyone's already withdrawn and you can't withdraw them anymore, and it would actually get stuck. So this is in an edge case on stuckness required criteria. So say, yes, it does help with fairness in the normal case, but there's an edge case that it's requisite. So I think I don't think it's to be debated. I think it has to go in if we do this bound. Does that make sense?

**Stokes** (17:51) - Yeah, it does to me. Okay, so I will keep polishing this PR and I guess yeah, we can just build more consensus asynchronously.

## [Capella BlobSideCar mutability issue](https://github.com/ethereum/consensus-specs/issues/3103)

**Danny Ryan** (18:05) - Sounds good. And because I think this code path will maybe never fingers crossed, be hit on mainnet. We need to make sure we have a lot of good tests. So that in the event that it is it's not attributes. Okay, are there any outstanding Capella issues? Other than the span of withdrawal sweep? Okay, great. So we want to 4844 this BlobSideCar is currently mutable and gossip. There'll be two ways to fix it. All we need to do the actual KZG verifications. At each pop the other would be to reintroduce that sidecar signature. It seems like due to complexity, especially rippling into validator signatures. And stuff that that is the former is the preferable path here. So we do have some benchmarks that Shawn and Kev have done on various operations in the issue. And I believe there might even be a PR that I haven't looked at yet, 3108 that Shawn put up there. Is there any outstanding discussion from points that have not been made on this issue? People want to bring it up? Are there any questions for additional context? If you're not caught up on this? Okay, so it does seem both of these operations, signing signature verification and the full aggregate verify both scale with the size of the number of blobs here, both on the order of four blobs per block look like a pretty reasonable amount of verification time with respect to what we're already doing at each hub, but both especially on singular or tertiary education if you're doing the full route calculation, and in the blob verification scale to something like slightly more than what our verification time is per hop. There is one hack that's at least worth mentioning. The flat hash, so instead of doing the Z, hash tree root of the blobs, or the signature, you could do a flat hash, which greatly reduces the time. But it looks like from this discussion and these benchmarks which could probably move forward with just doing full blob verification at each hop, and if that becomes untenable, actually, maybe discussed doing this blob hash each.

**Dankrad Feist** (21:08) - So in terms of scaling right, the so the blob verification already does that hash. So and I think the rest of the computation like the so you don't have to do any KZG stuff per blob, or any like group operations that are maybe a minimum of one like maybe one group multiplication, but just like, really small operation. So so maybe like I mean, at least if we're comparing it to to a full signature without flat hash, this might already be more efficient than verifying a signature, at least asymptotically.

**Danny Ryan** (21:56) - Yeah, we're, I guess, I don't know exactly where it scales to. But if you're looking at these benchmarks, which were done on different machines, you know, for 16 blobs for block for the same as your verification with the route you know, we're at something like 11 milliseconds. Oh, no.

**Dankrad Feist** (22:16) - What is the marginal cost? What's the marginal cost per blob? Because I think my estimate is for, for full verification, it's, it's about half a millisecond per blob.

**Danny Ryan** (22:32) - Yeah. On the signature verification were three milliseconds, six milliseconds, and then 11 or 12 milliseconds for four, eight and 16. Okay.

**Dankrad Feist** (22:43) - So fairly similar numbers.

**Danny Ryan** (22:49) - And then on. On the full blob verification, I think we're at four milliseconds, eight milliseconds and 14 milliseconds for the same set of numbers. So it actually is pretty, pretty similar. That's, that's what the signature verification with the full route calculation. So with the flat hash, we're at 1.7 2.1 2.8, which makes sense that it's scaling it significant subset of those. Nonetheless, I believe the general consensus is to move forward with full blob verification, as it does not really add any additional complexity. It also doesn't do very much adds no additional complexity, it's likely a tenable number at the lower end of the blobs per block. And we can get more data as we move into test nets. Is that the general consensus here?

**Dankrad Feist** (24:00) - Sorry, did we have any Do we have any number what it causes for 16 blobs or blobs versus four? On four verification?

**Danny Ryan** (24:10) - Yes, and what verification is for four, eight and 16, it is four eight and 18, although he mentioned that this is

**Dankrad Feist** (24:28) - That were feels wrong somehow. Because I would expect that there would be a higher marginal cost for the first blob, because you have to do pairings so like the first blob probably should take like something like three milliseconds, and then additional blobs should be like, half a millisecond. So that's what I would expect. Okay, so that's my that's my I'm surprised basically to hear that. I was somehow it's more of a like I my expectation would be that it's should actually become less of a problem as the blobs become larger because like, it's very, compared to,

**Danny Ryan** (25:09) - If you look, if you look at some of these numbers between 11 and 16, it ends up like it goes 10 14 13 13 15 14. So there's maybe some error here, and I don't know exactly how it would scale if we ran a bunch of these.

**Kevaundray** (25:30) - Tankard what did you say you was expecting?

**Dankrad Feist** (25:33) - I'm expecting something like three milliseconds plus point five times number of blobs some of blobs.

**Kevaundray** (25:49) - So each blob (inaudible) point five milliseconds.

**Dankrad Feist** (25:55) - I don't know like Danny's number sounded very linear. That surprised me.

**Danny Ryan** (26:01) - Other (inaudible).

**Dankrad Feist** (26:08) - Alright, sorry. Okay let's let's discuss those benchmarks. That would be great. And let's 

**Danny Ryan** (26:12) - How much help me understand how much parallelisation is being utilized in this? Would I see similar numbers on single core?

**Kevaundray** (26:25) - Yea, I haven't actually checked, but yeah, I do have 16 cores. Right.

**Danny Ryan** (26:36) - Dankrad does that calculation utilizing parallelization?

**Dankrad Feist** (26:42) - I don't know. You can definitely paralyze it. But I mean, the numbers don't sound like it's paralyzed. Because otherwise we'd expect it to decrease a lot more with more blobs

**Danny Ryan** (26:57) - I guess but to that in the paralyzation of wherever we go. I'd like to know what this looks like. Not throwing on 16 cores. Which, if that's that's what we're at. That's good. Yeah. Okay, well, let's um, circle back and just sanity check some of these numbers. As for the gossip validation, we can toss it in there. I don't think this is going to greatly affect our smaller test nets. But we might revisit it if if we hit a wall with some of these numbers, but does that seem reasonable path forward? I guess the only thing that we expect to come out of revisiting the the numbers is actually a lower verification cost. Which would be another checkmark for going this direction. So I'm going to review Shawn's PR Thank you, Shawn. And we'll try to get this out soon. This isn't a blocker on test nets. This somebody could add an additional load on the test net by allowing that data to be gossiped but I don't think that's what we're going to run into for the next month. Cool. Anything else on this one? Okay, I know we had the 4844 call, we can call earlier this week. But are there any other discussion items that we needed to bring up today? On 4844. Okay, great, Mikhail. Mikhail has an Engine API spec improvement proposal. Mikhail, can you give us the details on that?

## [@mkalinin's Engine API spec improvement process Engine API spec improvement proposal execution-apis#321](https://github.com/ethereum/execution-apis/issues/321)

**Mikhail Kalinin** (29:00) - Thanks Danny. Okay so we call the review? There is issues. Yeah. Yeah. The proposal basically contains two, two main parts in it in itself. So the first part is the proposed change to the Engine API itself. And it's just introducing the get caps or GetCapabilities method, which we have, which we came up to the workshop for Devcon. And this method allows us it basically returns the list of currently supported Engine API methods supported by the EL client, as to clients just request this list and understand what's going on what version it is talking to and what's next. So basically, this list allows us to introduce new methods introduced them outside of like, hard forks, without any coordination efforts for upgrade. So client software also allows deprecate methods. So it's basically about this Engine API change itself. And the other part of this puzzle is establishing some kind of process of how can we how do we want to or how can we work on the engine API specs to make it a bit more structure structural level is reduced the degree of mass dissipate and the upcoming hard forks and all this kind of stuff? Quickly about this, this part. So what propose is like basically we will have a reference table of all methods that is that were historically proposed, and were historically included in the Engine API specs. This table will contain the actually the status of better like, is it like, final or it's deprecated? Final means it's stable and should be implemented by every EL clients or there could be experimental status, which is helpful towards when prototypes and all this kind of stuff. Also, the other part of it is like how the spec files actually going to be, should be structured. And what's what's proposed in this what suggests in this proposal is that we will have like kind of files with different methods required or this or that the EIP like EIP for it for for like withdrawals. And alongside the work, it is going around these features, these new features, and we're close and as long as we're getting closer to, to the new hard fork, we create a new hard fork documents we put everything that we decided to be in the scope of this hard fork in this document. Then we do some rounds of iteration on the on this spec document. Then we finalize it after we decided that okay, there is a spec freeze, we finalize this file and we basically never change this file. The purpose of this is to have like a structured set of changes that we did to the Engine API, and to allow for cross references between the files. So like, for example, I shouldn't (inaudible) refer to Paris and say that okay, so this up log method is basically the same, but we're changing these, these three things and just list them so it's a differential spec description should be useful. And yep, and yeah, that's basically it. Basically, lightclient has a different opinion on how should we structure those files and probably can share it as well.

**lightclient** (33:18) - Yeah, my comment was just around the, like, overloading the use of the hard forks as the organization mechanism for the you know, all the different RPCs. I think that this makes sense for people who are going in and just implementing these, like client developers and stuff, because, you know, we've already sort of implemented all the past forks historically, the new fork and it kind of makes sense that this is like the minimal set of changes that needs to be done to get to the latest, but I think it is not a great way of doing the Engine API and spec if you are not, like very deep in like implementing these things. And I think this is like the similar problem that the CL specs have, where if you're just trying to go in and view what something does right now. It's hard because you have to like kind of start the latest fork and look and see if the thing you're looking for is enough fork and then go back one fork and look and see if it's not fork. And I'm afraid to like recreate that with the Engine API where if I want to see like what does get payload v3, do, I started some fork. I don't see it there I go back another fork. I don't see it there, you know, and so like, it goes forward in that way. So I think that if we do a logical separation of the different methods so we might have a method it's like a file it's in blobs that MD and that would just have like all the things related to blob so it's just right now mostly just 4844 and then maybe like payload dot empty because like all the like new payload good payload types of stuff. That I think is not much worse for client developers, because we can still say within the method like, Hey, this is Shanghai or we can say I'm like the overview of methods like these are the methods that we're doing for Shanghai, but to most people who just want to view and see what the Engine API is doing. I think that's a better way of interacting with it.

**Mikhail Kalinin** (35:06) - Yeah yeah (inaudible) see some really practical (inaudible) based approach. So we will just basically have we're talking about (inaudible) we will have all the change. So this matters in one file and you can track them back. And yeah, implemented easily. You will just have it on one screen. Instead of like jumping from one hard fork to another figuring out what was introduced. Saying in comparison session Hi, what's needed to be demanded in Cancun? If someone is implemented from scratch? I don't know. But yeah, what I like about these hard fork, MD files is that you can just you know, have it speced out and then finalize and then just never touch this file. And valid change anything and that's unless there is like some blob that we want to fix. Yeah, also, it more aligns with like this feature approach. So if you have like EIP 4844 feature in a separate file, you can just download it, it's, it's introduces changes to different parts of engine API. It will contain them all in one file. And we want to keep those changes separate, like from the main stack until some point in time when we decide to put to include this feature into hard fork and yeah, so definitely functional approach also, functional (inaudible) approach for this (inaudible) files makes make sense. So there is a kind of trade off.

**Danny Ryan** (36:53) - I don't feel very strongly here, but I do question Who is the Engine API spec for? And I would say almost entirely is for client developers, because it's not a user facing API, you know, so as opposed to the API, where we want it to be organized such that it's highly functional for users to be up in this is like so I think should be optimized for client developers because it's not something that other people would be using. That said, I think both are relatively both pads are relatively functional for client developers.

**lightclient** (37:35) - I feel like if we had a list of these are the things that were added or changed for each fork and then we the file level, organize it logically, I think that's the best of both worlds. Or vice versa, like have a list of like this is a logical things it within related to payloads and the files as forks. I think, just going with one of those approaches where you have both give us gives us the best of both worlds.

**Danny Ryan** (38:00) - Are we so when we originally writing this we kind of planned on moving it to a more functional description like the API's and like the beacon API's are that can be better rendered and stuff. Instead, it looks like we're at least currently doubling down on markdown. I'm not. Markdown works for me. I don't really mind but I do wonder if it's worth revisiting if markdown serving us as we wanted to.

**lightclient** (38:30) - Well, the proposal does have a like folder section for the open RPC definition.

**Danny Ryan** (38:36) - Okay, so we would do both.

**lightclient** (38:38) - Yeah. I think so.

**Danny Ryan** (38:41) - Do we have the for Paris or not?

**Mikhail Kalinin** (38:48) - Oh, we'll have to introduce them. And we will started (inaudible) this proposal (inaudible) on it. And yeah, from my my smallest short experience on like, trying to put some specification or finalized save and blob bags into an open RPC description. It's really hard to spec anything in in this form. So I think markdown works better at least better than often our specification. Specification was given.

**Arnetheduck** (39:38) - I had a question. You mentioned a request for a list of methods that the client supports or the execution client supports. Not not so much a question but a comment. That that's often not terribly useful because what users do often is that they upgrade their execution layer separately after consensus layer client. So one thing that that I think is useful is that we also kind of think a little about how to standardize error codes for something that's been deprecated and removed. And then how we reason about methods that don't exist yet because typically what we'll do as consensus clients is that if there exists a newer version of a method, we'll try the newer version first. And if that doesn't work, we'll try the older one, or maybe the other way around. Like it depends on where were in the deployment phase we are right so I'm calling a function that lists all the functions available is kind of useless. If we can just try and try each one separately and see if it works, and then get like reasonable errors to to pick one.

**Mikhail Kalinin** (41:05) - I think that (inaudible) also already has this kind of error. So if you call an ad that's I don't know what these are, specifically is but yeah, this this, this may also I don't know work. It's just you know, it just looks ugly. From my perspective. To be honest.

**Arnetheduck** (41:24) - It's reality, because they don't. I think the core issues here that we don't know when, when the execution client is restarted and upgraded as consumers that might happen anytime. There is no signal.

**Mikhail Kalinin** (41:47) - But it depends on the dialogue. That is if you use WebSockets you may know the session and got expired. Right. And you had you had a new session established that can query every time that the session is just just started. You can query this this method so for (inaudible) it is more complicated. And basically, probably it is like fallen back to error. And calling a list of methods if you see that a method is unavailable or yet unavailable. Oh yeah, yeah, but but it will not work if some method is still available, but EL has been upgraded and has new capabilities that can switch that can that can have both. So CL will have the glaring errors will not work in this case.

**Andrew Ashikhmin** (42:49) - So sorry, guys. Clarification. My understanding is that the the switch to the new 2v2 methods is quite dramatic. It's it's not a transitionary period. So for all (inaudible) and high blocks, we should use V1 methods and for starting with the Shanghai for all Shanghai blocks we should use V2 methods because the the head to hash will be different depending on whether there is like even it's there are no withdrawals. The hash of an empty list should present so it's not like a gradual switch to to unused set of methods.

**Mikhail Kalinin** (43:35) - Yeah, I I can understand this point pretty well, because I was trying to make this point as well. And yeah. I think it's another thing to debate whether we want 2v2 to be backwards compatible to V1 or not. And I suppose that CL clients, they will be just, well, it was just easier for CL developers to implement something like okay, we see v2 method and we use it for every for every interaction after we requested and got this method to support it via EL. And so like we should called or trigger whether this block is, is up to the fork or the fork to decide on which method we use. Firstly, like reducing complexity by having a bit too backwards compatible to move on. What if this is not the case that we would like to solve? I would argue that we should be clear on which method is called new fork and hard fork. So just making it backwards compatible.

**Arnetheduck** (44:51) - Backwards compatible is nice because then, like again, we can just try the new method if it works. We get, we get you know either the new data or the old data regardless of if the fork has happened or not. In general, of course, that's not possible. But that's what we've done in consensus, like the beacon API a couple of times where we upgraded no between block v1 and v2, you could first query only phase zero blocks, and then you could query any fork blocks, including phase zero. And that was very nice because then you just tried with the new one, and if it worked, it worked. If it didn't, then you try the old one. And that's it. You don't make lists or anything you just give it a shot.

**Mikhail Kalinin** (45:39) - Yeah, yeah, that's that's (inaudible). Just you know, can work out what we have currently. I'm not sure. I've said that it's just seems ugly to me and looks ugly. But yeah, it definitely reduces the spec complexity. I don't know about engineering complexity and the mess in the code that's this like pullback would introduce about backwards compatibility. I have a pretty strong opinion that we should not support more than, like two forks. In one methods were efficient, because if we will support all forks and like we return methods will, you know, contain all the logic that is needed for V1, V2 and so forth? That's there's gonna be a huge mess. But backwards compatibility for like, one fork is probably fine. Again, if it's reduced engineering complexity. So we need probably client developer inputs on the gap capabilities methods versus try and pull back when there is an error and the other one is like the yeah, the other two things are backward, backwards compatibility and the structure of this back basically hard forks versus functional grouping. Anybody wants to chime in?

**Danny Ryan** (47:45) - Okay, based on this conversation in the discussion in 321 Mikhail, are there any immediate changes you're going to make or is it still in a good shape for other people to read and chime in at this point?

**Mikhail Kalinin** (47:59) - I think it's still good to read. Probably until next week.

**Danny Ryan** (48:06) - Okay. And then how much is this? Is this a critical blocker as we're moving towards Shanghai or is this something that won't block our development efforts? And what's our timing criticality?

**Mikhail Kalinin** (48:22) - Now that's a good question. I don't think it's blocking really, anything right now. But yeah, we just need to start like if we were if we're going to have some process and yeah, the earlier we do it, the better for us. The less cleanups we will have to do in the future.

**Danny Ryan** (48:49) - Okay. So, please take a look this week. If you want to chime in on this process. We might have a feeling we might not be able to get to an all core Devs next week, but maybe we'll throw it on the agenda. And if we don't, then in two weeks time, we'll revisit this conversation. Sounds good? Any final closing comments here? Okay. 

## Open Discussion/Closing Remarks

**Danny Ryan** (49:30) - Now for general open discussion anything anybody wants to bring up today? Any anything at all? Okay, great. Thank you, everyone. Talk to you very soon. Take care.

### Attendees:
* Gajinder
* Tim Beiko
* Pooja Ranjan
* Mikhail Kalinin
* Chris Hager
* Ben Edgington
* lightclient
* carlbeek
* Eugene Mamin
* Damian
* Enrico Del Fante (tuber)
* Marek Moraczyński
* Protolambda
* Hsiao-Wei Wang
* stokes
* Joshua Rudolf
* Sean Anderson
* George Avsetsin
* łukasz Rozmej
* Stefan Bratanov
* Ashraf
* Zahary
* Daniel Lehrner
* Ruben
* Danny Ryan
* Tomasz Stańczak
* Brechy
* Ayman
* Marcin Sobczak
* Saulius Grigaitis
* Andrew Ashikhmin
* Dankrad Feist
* Justin Florentine
* Cayman Nava
* Lion Dapplion
* Mehdi Aouadi
* Kevaundray
* olegjakushkin
* Roberto B
* Arnetheduck
* mrabino1
* Trent
