# Consensus Layer Meeting 124

### Meeting Date/Time: Thursday 2023/12/14 at 14:00 UTC
### Meeting Duration: 37 Mins
### Moderator: Danny
### [GitHub Agenda](https://github.com/ethereum/pm/issues/922)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=1mLDIRmGtNk)
### Moderator: Danny
### Notes : Avishek Kumar

--------------------
## Agenda

**Danny** [5:31](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=331s): Okay we should be live. Welcome to All Core Dev's Consensus Layer Call 124. This is issue 922 in the PM repo. Light schedule it seems but we shall see. We'll quickly talk about Deneb status testing Etc. A server side event being discussed for the block and I think how it changes in Deneb and then open discussion from there. Let's go ahead and get started deneb, General testing and devnet updates. I think, I saw new client pair syncing.

## Deneb & General Testing and Devents

**Barnabas Busa** [6:15](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=375s): Yes. So devnet 12 is now onboarded all the different clients. And all the different client combinations and we currently have prysm thinking to the Head. We didn't want to enable checkpoint thing for that because we wanted to go through a genesis thing.  Just to be able to make sure that genesis thing still works. We have enabled MEV for most of the different CL’s except for prysm at this point and everything seems to be on track.

**Danny** [6:58](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=418s): Cool. So there's just one instance of prysm or was that many?

**Barnabas Busa** [7:04](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=424s): So this morning I have added all instances. Yesterday we added one with gas but now it's with all the different EL’s.

**Danny** [7:18](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=438s): Cool and other than MEV. Are we kind of putting the testnet through the ringer? Is it moderately kind of just stable functionality right now?

**Paritosh** [7:28](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=448s): A little bit of stable functionality for now. There was this one Lighthouse bug with MEV for local payloads that's been fixed and just patched I think like an hour ago. Besides that there seems to be an issue with one Besu node. We're not particularly sure how it got to the state but it's trying to convert an invalid block to a valid one. So maybe someone from Besu can have a look at that one.

**Danny** [7:59](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=479s): What do you mean by convert? 

**Justin** [8:08](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=488s): No I was just agreeing with Danny that's a good question this is Besu team here. I'd like to hear more.

**Barnabas Busa** [8:15](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=495s): We have put all the error messages in our chat.

**Justin** [8:19](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=499s): I've got those thank you. 

**Paritosh** [8:25](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=505s): With TLDR there was could not persist world for root hash for a certain block and then I think Besu tried doing that like twice. And then I guess the note restarted but at that point Teku then says cannot change node validity from valid to invalid. Sorry from yeah from valid to invalid and then Teku get stuck as well.

**Barnabas Busa** [8:51](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=531s): We started another s in a totally different machine with the same pair also on arm and it passed by that block. So it might be just some corrupted DP element. 

**Paritosh** [9:05](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=545s): Yeah could be that's why we're still not sure how we got that node into that state. 

**Barnabas Busa** [9:10](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=550s): We used to have blobber running on it and Lighthouse validator. So it's a bit different than what you would normally have.

**Danny** [9:20](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=560s): Are we purposely sending bad blocks or not?

**Paritosh** [9:26](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=566s): Not yet. We need an updated Bad Block. We don't have one yet.

**Barnabas Busa** [9:35](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=575s): Is anyone from prysm can confirm that we should be good to go with the Shadow Fork. 

**Terence** [9:42](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=582s): Yeah we can try it. We the only thing I did not test is the Builder path for the proposal but given that there's not much change since the last commit. I think we should be fine there. But do let me know if you see an issue at the same time. I will also monitor the setup.

**Danny** [10:07](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=607s): Yeah Terence it might be nice to have some call around. Is this prysm syncing and but needs a lot of work or is this like prysm getting close to what you'll feel like is stable and might need some iteration but isn't.

**Terence** [10:25](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=625s): Wait I'm sorry is there a syncing issue?

**Danny** [10:29](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=629s): No sorry I just meant like prysm the thing that we currently have on testnet is that like prysm is working but there's a lot of kind of productionizing doesn't need.


**Terence** [10:43](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=643s): Yeah, no so right now the only thing we're missing is basically bad feeling blob and some and then more verification check on the on the syncing path the syncing to head but other than that it's pretty production nice.


**Danny** [11:02](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=662s): Yeah! Cool.

Any other questions or discussion points on the devnet? 
Any other testing related discussion points? 

**Mario Vega** [11:29](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=689s): I haven't run the hive test for prysm but I will do as soon as possible and just report but I think we can go ahead and prepare for the shell Fork. If I find anything I will reset it immediately.

**Danny** [11:50](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=710s): Cool yeah! Anything testing a devnet related other than that. 

## Block SSE in deneb


Okay, Dapplion did raise two points. It looks like the former is merge which is adding proposer_slashing and attester_slashing to the Server Side Event. So Dapplion, we don't need to discuss that right.


**Dapplion** [12:16](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=736s): Yeah first point issue 376. It's closed. So I think that's fine if there is any objection just do on the PR itself. So let's go for Point number two. Issue 349 this was originally raised by Paritosh, so the context here is them and we're not sure if other consumers are using the SSE events for timing data. They and we are aware that this is not ideal but that's the best they can do at the moment. When we add blocks to the mix if the event is emitted after importing that means waiting for all the blobs. So now the data would be heavily distorted. So the discussion is around should we change the event definition such that it is emitted after Gossip validation or at some timing data or if anyone else wants to provide any other option for timing data via Server Side  Events. That's the context. 


**Danny** [13:27](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=807s): So just to clarify when we add blobs the point at which we would admit this event might be delayed even more because where the dependencies on the network. And so it deviates further from when you actually receive the block on Gossip which is a valuable piece of information.



**Dapplion** [13:46](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=826s): Exactly. So okay I can recap the discussion so far. I think what seems the easiest option is to emit the event after full import but attach a new property where it's a scene timestamp at where each client has perceived the event. It's not incredibly important for that definition of scene to be uniform across implementations because at least you have the Devops. They do correlation timings. So as long as these timings are consistent within an implementation it's fine and this seems to satisfy all concerns.

**Danny** [14:39](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=879s): Okay the alternative that you originally suggested was two separate events rather than bundling the timing into the previous event.


**Dapplion** [14:47](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=887s):  Yeah! So we could have an event after gossip validation a second event after full blog import. 

**Danny** [14:56](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=896s):  But you think the additional field is the better path right now.

**Dapplion** [15:03](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=903s): With the current requirements I think yes because it's not clear who really wants this blog gossip event except people timing data. And if they can just get it from this one event then it seems simpler but both options would work.

**Danny** [15:27](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=927s): Right. Yeah. Enrico? We can barely hear you it sounds.

**Enrico** [15:41](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=941s):  Sorry maybe now it's better. I was thinking that adding the time stamp in the data itself would be better for two reason. One is that this event can be served well with low priority. So it doesn't mean that when you receive on the other side the event itself. It is their correct timing. And also adding another event that says this is when I received the gossip this is when I imported it. Maybe it is just an overkill for the use case that we are thinking about. So maybe it's just easier to leave things like our now just adding the arrival attribute.

**Danny** [16:38](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=998s): And it is I know you said there can be a little bit of inflation detail on that the definition that time stamp. But will it be defined as gossip validation conditions have been completed or is there ambiguity on whether they could be pre-os that well?


**Enrico** [16:56](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1016s):  Currently we take all. So the arrival before the gossip validation. So it's more it's closer to the real message arriving over the wire. But I don't know other clients.


**Danny** [17:17](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1037s):  Real quick and then we'll go to Sean dine do you do you intend to specify if that's pre- or post executing the gossip conditions like immediately upon wire or otherwise or do we not care.

**Dapplion** [17:34](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1054s): I'm not sure. I'm on the fence. I think whatever is easier for implementation to be honest. I think for this use case it doesn't matter but it would be good to specify it yes.


**Danny** [17:47](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1067s): Sean?

**Sean** [17:50](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1070s):  So maybe I miss this but if we're thinking of just submitting an event when we import a block would we then like not get any indication about what happened to gossip blocks that we didn't import. Like some a block that filed consensus somewhere or wasn't available maybe like that would be a reason to maybe have two Events. 

**Dapplion** [18:21](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1101s): Right that would be the point of having the second event there has not been demand for that we can add it but it's like a a bit of a scope grip for this specific Issue.

**Danny** [18:34](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1114s):  You could also put a May upon block failure at any point in the pipeline or must I don't see how it precludes in a failed block. 

**Dapplion** [18:50](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=s): I would say this event carries the idea that this block has been fully validated if you break that assumption at least you should indicate that done stream somehow.

**Danny** [19:04](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1144s):  Sean does Lighthouse emit invalid blocks right now. 


**Sean** [19:09](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1149s): I'd have to check. I I think yeah I don't know if we do emit events on Gossip blocks. Then that would mean we would potentially be emitting events on invalid blocks but.

**Dapplion** [19:24](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1164s):  I'm pretty certain at least you guys told me the event at the end of the import. So definitely not for right.


**Enrico** [19:32](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1172s): I think Teku has recently added an option to also emit the event before import. I might be wrong but I remember something like that but this is an option that needs to be enabled otherwise by default is emitted afterwards.


**Danny** [20:06](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1206s): Are there any further comments on that? Do we have enough information to keep moving with maybe a suggested PR at this point?

**Dapplion** [20:18](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1218s): In my view it seems we should first figure out if there is a use case for Consumer of events to learn about invalid blocks if that's the case then maybe we should consider the two events or extending the event in that way otherwise seems that we should go for the timestamp property. Anyone opposing?


**Danny** [20:41](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1241s): Does valid slash invalid or valid true false property also satisfy this use case in the event that we wanted to have that use Case.

**Dapplion** [20:53](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1253s): As long as,  so if we have a single event with valid property and the time stamp yes that satisfies the original issue. I think that's all from me.

**Danny** [21:15](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1275s): All right thank you. All right. Cool. Sean added a couple things. Let's do that PR 3561 first Sean if you want to give a quick explanation.

## Slashable message propagation post-deneb #3561

**Sean** [21:39](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1299s): Yeah sure so I just noticed the gossip conditions for Blobs sort of lead to some I guess like unexpected consequences. I don't think it's negative or anything, It's just for example using the beacon API with the broadcast validation of Gossip state. It might be unexpected what messages were valid and invalid and the reason for that is because technically. It's okay to gossip two blobs with different blob indices that have slashbale headers associated with them. So you're allowed to gossip those but you're not allowed to gossip them if they the same blob index. So initially I was thinking maybe it'd be easier to just sort of disallow gossiping of any block or blob message that's like quote unquote it's slashable but then Danny brought up the point that we don't necessarily like elsewhere we don't look between different message types to try to like cross validate what should be sent. So what we could also do is just think about this like slashability within any blob index that would make it make somewhat more sense and then Yasik also brought up the point of we could instead just allow propagation of Slash like block blob messages because you're more likely to gossip to a node around a slasher in that case. And I think the final Point Danny brought up was we could sort of do like a hybrid thing where we propagate slash messages until like a slashing has been seen on Gossip. Yeah that's the general TLDRs.

**Danny** [23:49](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1429s): Yeah my suggestion at the end is like you do want to reduce how easily a message can be gossiped from into one hopefully. Meaning like you want caches or something to make it difficult to send repeat in messages once you're willing to be slashed. And so you know if you're instead monitoring for a slashing message in relation to the message then you can drop and that can be either you created the slashing message if you have the faculty to do so or you've seen it because somebody else saw it and created the message. What are the consequences of doing nothing here?

**Sean** [24:46](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1486s): I don't think there are consequences. I just personally found it confusing when I was trying to implement the broadcast validation function in the beacon API. You can have messages that are like you get messages to this end point with like all block blobs and the block. So like that message can be slashable but like you would still technically publish all parts of it and return to it. So I thought that was weird but I don't think there's any detriments apart from it being somewhat unexpected in my point of view. I think my personal preference I guess would be to I don't think we have to make these changes for Deneb necessarily. But at some point having clear rules around how we should handle slashings and maybe allowing them to propagate further I think that'd be fetting.

**Danny** [25:58](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1558s): Right I suppose there's also the option to upgrade this after Deneb launches with thinking about the analysis of does that put us at like Network partition risk if someone's willing to spam Slash messages. I guess my preference would be if this is secure but leads to weird or confusing scenarios that we take a minute to think about how we want to do this kind of holistically rather than changing this back at this point. But if it's insecure then I feel otherwise.


**Sean** [26:44](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1604s): Yeah no I think that sounds good to me.


**Danny** [26:53](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1613s): Okay I would propose maybe towards mid late January if you or anyone else has like a design they want to propose and feel comfortable with, to pick it up then. Cool. Are there any other further comments on this one before we move on. 
Okay next up Sean  IDONTWANT control message.

## [GossipSub 1.2] IDONTWANT control message #548


**Sean** [27:37](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1657s):  Yeah. so I'm not super familiar with this change but I believe it can be used as an optimization and gossip to reduce the amplification factor. I think it's because you can tell modes not to send you a blocker app Blob we've already seen for example. And I think both age and Yasik have looked at this and then Anton raised it but I think we're waiting for consensus to merge it. And perhaps for it to be moved along a little bit more but I think it's something that's useful for Deneb and people looking to implement it possible.

**Danny** [28:31](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1711s): Yeah and this can also be kind of upgraded transparently. I believe. I guess the problem here is if the P2P spec maintainers want it bundled in a big one version 1.2. I guess even if it's merged sensitively we could potentially start using it. And I believe if I remember correctly this helps more when they're large message sizes than smaller meaning you're more likely to kind of reduce the amplification Factor if there's slower larger messages being sent around rather than tiny messages or maybe more like attestations I feel like the assessment was that it wouldn't do much. But it would do a lot for blob.

**Sean** [29:28](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1768s): I don't know enough to comment but I think that is the case on the PR. It says this is reduces bandwidth by 30% seems pretty good. 

**Danny** [29:47](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1787s): Yeah I just left the comment that it looks good. I'll try to hit up vizo in a separate forum as well. I mean at a certain point if we want this and we're blocked on libp2p spec maintainers we're going to have to figure out a different path. So let's see if we can get this moved along in there. And have the conversation on the next call if we cannot okay. And Mikhail did Echo that. It makes sense for large messages only. Thanks Sean. 
Okay those are the only items that we have on the agenda for today. Are there any other discussion points?

Okay call schedule next Consensus Layer Call is in between Christmas and New Year's. I will not be available. I do not intend to host this call. I was thinking if there is demand for a call. It could be labeled more of kind of like a testing and kind of devnet check-in call. If there's people that want to get on a call on that date. Is there demand for that? Let's see one heart emoji. 

**Tim Beiko** [31:49](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1909s): We can also decide this. So next week we should have All Core Devs. So on the 21st we can also decide this  then because this came up as well on the testing call Monday. Where the next testing call is on December 25th we're obviously going to cancel that. So yeah I think if next week people feel like we should have something yeah we we can make that a sort of combined call.

**Danny** [32:19](https://www.youtube.com/watch?v=1mLDIRmGtNk&t=1939s):  Very cool. So if we do something on that week. It would be at the 2 pm UTC slot on Thursday. It would not be a full All Core Devs but anyone that is working on devnets and things on the holidays and wants to check in or chat about anything we can make that decision in one week on  whether we have haven't host that. And even if the decision is no people can  certainly jump on the Discord drop a call link or jump in some of the audio chats at that time. Okay cool. So we will have ACDE in one week. And if there's any further things to figure out on calls we can do so then. All right, Any other  discussion points for today. Great, well talk to you all next week on ACDE. And enjoy the end of the year. Take care. Thanks

--------------------------------------------------------------------------------
## Attendees

* Danny
* Pk910
* Barnabas Busa
* Lightclient
* Peter  Garamolgyi
* Ben Edington
* Mikhail Kalinin
* Sean
* Mikeneuder
* Lion Dapplion
* AndersHolmbjerg
* Mario vega
* Toni Wahrstaetter
* Enrico
* Joshua Rudolff
* Dan 
* Tim Beiko
* Gajinder
* Pooja Ranjan
* Matt Nelson
* Scorbajjo
* Caspar Sachwarz
* Paritosh
* Maintainer.eth
* Justin Traglia
* Ahmad Bitar
* Justin Florentine
* Preston Van Loon
* Ben Adams
* Sean
* Echo 
* Nishant	
* Saulius Grigaitis
* Mehdi Aouadi
* Hsiao-Wei Wang
* Trent
* James He
* Zahary
* Ansgar Dietricks
* Dankrad Feist
* Pop
* Kasey 
* Lukasz Rozmej
* Fabio Di Fabio
--------------------------------------------------------------------

### Next Meeting Date/Time: 28 December, 2023 at 14:00 UTC

------------------------------------------------------------------------
