

# Consensus Layer Meeting 138 #1100
### Meeting Date/Time: Thursday 2024/7/25 at 14:00 UTC
### Meeting Duration: 90 Mins
#### Moderator: Alex Stokes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1100)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=lmzAUqsIbIE) 
### Meeting Notes: Meenakshi Singh
____
###  Summary


| S No     | Agenda | Summary |
| -------- | -------- | -------- |
| 138.1    | Pectra Devnet 1    | Launched on July 23, but faced stability issues. Developers are debugging clients and resolving a chain split caused by an EIP 7702 transaction.|
| 138.2 | ExecutionPayloadEnvelope|Prysm developer “Potuz” proposed changes to the Beacon block body structure and Engine API. These aim to help CL clients store necessary data for state transitions efficiently.|
|138.3| Stable Container EIPs| Discussion included EIP 7688 and EIP 7495 inclusion in Pectra.|
|138.4| PeerDAS Updates:| @Etan-status’s summary and proposal to include EIP-7688 and EIP-7495 in Pectra devnet-2 are noteworthy. However, considering Pectra’s size and existing testing/security processes, formal inclusion requires careful consideration.|
|138.5| [Add BeaconBlocksByRange V3](https://github.com/ethereum/consensus-specs/pull/3845) |Developers are encouraged to review the proposal on GitHub.|
| | | Collaborative input ensures robust improvements to Ethereum’s ecosystem.|
|138.6|Arranging PeerDAS| The current approach of activating PeerDAS at a separate epoch from the Pectra fork epoch allows flexibility. Aligning these parameters could simplify coordination.| 


## Agenda

## Petcra Update 
**Alex Stokes** [2:33](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=153s): Hey everyone! Welcome to ACDC. This is call 138. I just put the agenda there in the chat. Yeah, let's go ahead and get into it today. And so first Electra. We just launch Devent 1 a few days ago. Very exciting! I wonder if there are any updates with the list there. Last I looked, it looked like participation was quite low and there were a few forks on the chain. So not looking super great. Anyone here have any more to share.

**Paritosh** [3:16](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=196s): Yeah may be I can give a short update. So Philip set up the network earlier on Tuesday. and I think Erigon had some issues around Epoch 64 and haven’t been participating since but I think team is aware and looking into it. And them some external users started sending transactions at some point around slot 1,800 or so. And chain forked into 3 paths. And then it looks like there’s an EIP 7702 transaction that caused a split but we haven't been able to fully debug it. Nethermind and Besu seems to be building a consistent chain Reth and Geth seems to be consistent to in their chain but these two chains have a lot of forking and reorging amongst themselves. And ethereJS pairs are not proposing since a while. So yeah I think that's the latest status but yeah I'm just getting caught up as well. 


**Alex Stokes** [4:21](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=261s): Cool thanks. So yeah sounds like there's some fun debugging on the horizon. Yeah nice work though it's exciting to see Devnet 1 up and yeah we'll just keep iterating from here. Anything else to say there? It sounds like yeah clients are busy figuring out what's going on with the Devnet. 


**Pari** [4:52](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=292s): Yeah in case Client teams need something for debugging please text on the interop chat and we're happy to help get you whatever you need. 


**Alex Stokes** [5:02](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=302s): Cool! Thank you. Okay we can move on to the next item then let's see this is from Potuz and essentially I mean maybe he can chime in a bit more but it sounds like a suggestion to move some of these request data that we're introducing pectra outside the executionPayLoad type in the beacon chain in the CL broadly. And yeah it sounds like there are some reasons to do this, is Potuz on the call? let's see looks like you're here would you like to give us a summary? 


**Potuz** [5:40](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=340s): Sorry I just I just logged in it seems that on time are you talking about this the issue of the execution PayLoad and a container?


**Alex Stokes** [5:48](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=348s): Right and the request. Yep.


**Potuz** [5:51](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=351s): Okay good. So let me quickly describe the issue. Since Bellatrix oh since shanghai the Beacon block contains inside it Beacon block body the full execution payload that the block itself is broadcast and is transferred on the P2P layer for the consensus clients and the consensus client gets this payload it sends it to the EL for verification. Capella introduced a new thing which is that the fact that the payload has withdrawal that were honoured in that payload on the execution layer. And at the same time these withdrawals needed to access the beacon chain of the beacon state to honor the deduction of those balances from the beacon State. So this was the first time where we actually had to synchronise information that was have some state transition that was happening on both layers at the same time. However since Bellatrix and this was not modified in Capella. The consensus clients would get this full block would send the payload for the execution layer for validation and then they would completely forget about this payload. They will save in their DB in the database will save the full block minus that payload. because that payload anyways is being saved in the execution layer Database. In Capella when we added this withdrawals in principle we could have saved the payload I'm sorry not the payload but the withdrawals part of the payload but since the withdrawals are deterministic from the beacon State this didn't present any problem you could grab an very old Beacon State a very old block without the payload and you can perform the beacon State transition function without ever getting the Payload. Electra changes this. in Electra the execution payload is needed on the consensus layer to perform the state transition because the requests that are included in the execution payload are needed as input this are external input to the beacon state transition function in the consensus layer. this was again I repeat this is not the case for withdrawals even though withdrawals are in the execution payload because the beacon state already knows what withdrawals should have been in the payload. So what I am proposing this presents a problem now for consensus clients because consensus clients often times have an Old State have an old beacon block and they want to perform the state transition to get the new State. In the current status either the consensus client saves this information in whatever schema for the database they want to do. This information meaning the Electra Fields there are new fields that the consensus client requires to perform the state transition function or they don't save it they send the payload as we do now to the execution client and then later on when we need to perform this state transition we request the payload again. this makes it very inefficient and clients will not catch up if they need to sync a block that requires this Old State transition functions. So my proposal is to transform the way that the consens to two changes one is on the consensus side the structure of the beacon block body. Another is in the engine API the structure of the message that is exchanged between the consensus client the execution client. What I'm proposing ensus layer contains an envelope. In this envelope you find these fields that are required for the state transition on the consensus side this meaning the requests and a payload the execution payload but this execution payload doesn't include these same Fields. So this means that the consensus client would be able to Hash the payload and just blind it and just save that. This will make it compatible forward compatible with SSZ when the execution clients move to SSZ. Because then the hash that we're going to keep for the pay would be the actual hash for the block If eventually the consensus client move to SSZ. On the engine we will need this change for get new payload and the Consense to inform that to notify a new payload would send this full envelope and then the execution client will need to add this fields from the container to the payload to compute the block hash. So that's what that's I hope that it was clear what the problem is. 


**Mikhail kalinin** [10:52](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=652s): One clarification here as far as I understand you don't drop the entire payload you just store keep the payload header anyway otherwise you will yeah actually chatting about this in the chat I mean yeah. So this is because you have to serve requests from other peers to get the full block and you can use get payload body to get transactions and withdrawals if you need withdrawals from EL but the header should be kept in the database.


**Terence** [11:42](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=702s): Yeah that's right. We keep the header right and then today the issue is that do P2P request
we only request from the EL through P2P for but for State transition we're okay but then for like Electra now we also have to request from the EL just for State transition. And we are worried about the performance penalty here. 


**MIkhail Kalinin** [12:07](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=727s): Yeah sure. So if yeah let just imagine if we don't have this envelop at all so what then would you have to do in the database? Would you need to introduce execution payload without transactions. 


**Potuz** [12:25](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=745s): You would need to you would need whatever you do because these clients would handle this in a different way each client but whatever you do the consensus client will need to save in the database in whatever schema this new Fields these requests. 


**Mark Mackey** [12:43](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=763s): Yeah so like usually you have just the header and you don't need any of the objects that go along with it because you have the usually only need the root of these requests but now you need actually the requests and usually we're just storing the header. So we'd have to have some either some sidecar pattern which makes the code quite unaesthetic or but yeah you'd have to store it on the consensus side or request it from the EL every time you want to do a state transition.


**Potuz** [13:15](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=795s): Exactly that's the point yes and and it seems to me that the change of just the changing the structure into an envelope it's a very simple change.


**Stokes** [13:28](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=808s): Right yeah go ahead Mikhail.


**Mikhail** [13:32](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=812s): Yeah I have another question. So you mentioned that whenever you validate the payload you then drop the transactions from it. So it happens even for non-finalized blocks right. 


**Potuz** [13:46](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=826s): Correct.


**Mikhail** [13:48](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=828s): Okay I see. I didn't realize it was quite aggressive as that yeah but makes sense.


**Mark Mackey** [13:57](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=837s): Because you don't yeah the whole reason we have the payload bodies method is so that the CLs can drop the bodies and just have the headers.




**Mikhail** [14:09](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=849s): Yeah for sure I was just you know kind of like under impression that it happens for then the finalized prefix of the chain. So if it happens for every payload then I see show problem. Okay so what if clients introduce exe execution payload without transactions. I know it sounds ugly but would that solves the problem. 




**Potuz** [14:40](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=880s): I think it's not. So it's the other way around for me the problem is not about transactions or not the problem is about what information each client needs to perform their state transition. So anything that the consensus layer actually needs to perform transaction should not be at the same tree level SSZ tree level from things that the consensus layer does not need. So anything that we do not need if we keep it one level Below in the hash tree we can just hash that thing, keep the hash of this and only save the objects that we need that the total hash tree root would be the same. 


**Mikhail** [15:23](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=923s): Yes I can understand that but as far you have this header anyway. So it's like header plus two new Fields with requests that I maybe more in the future.


**Mark Mackey** [15:39](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=939s): Like if we don't change this on the P2P layer and we just try to do it internally which we can kind of but the problem is you'd have this extra object that has the extra information that you need but it needs to Hash to the object without the extra information. Because that's not on the you know that's not in the specs. So like
that turns into something really ugly where like the thing you get from the network is different than the thing that's not complete I don't know the ways around that are
quite difficult to deal with. 


**Mikhail** [16:19](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=979s): Right.


**Potuz** [16:21](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=981s): But also Mikhail, why is it that I mean what worries you about having this in an envelope? The envelope comes with the block itself so what what  is what is the the the the push back against having an envelope?


**Mikhail** [16:35](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=995s): Yeah I
I'm just trying to understand how big the problem is? I'm not against this change, it's just you know we used to have the execution payload representing all the fields and containing all the fields that are required to recreate the execution layer block. Now we want to break this.


**Potuz** [17:00](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1020s): No I do not want to break this envelope call the envelope payload if you wish from the point of view of the EL. The EL will get the envelope not only the payload. The EL gets the envelope and if they want to Hash it as SSZ they can just hash it immediately. If they want to Hash it as RLP they need to move the requests alongside the rest of the fields and then hash it. 


**Mikhail**[17:27](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1047s): Yeah I see I can understand that. Okay if I would say that if this problem is common to all CL clients then we should probably you know do the change or this is the change to the API and EL clients will need to change this.


**Potuz** [17:56](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1076s): It's not only the API I'm proposing that the beacon block body structure changes. 


**Mikhail** [18:03](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1083s): Yes that's correct I see because we kind of already have the envelop right which is called execution payload now and we need one one another abstraction level here. 




**Potuz** [18:19](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1099s): That's correct. 


**Mikhail** [18:21](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1101s): So yeah I understand that but I yeah let me think on it. Could you please I don't know could you please outline this in the issue?


**Mark Mackey** [18:36](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1116s): I mean I pasted it in the chat but yeah that I don't think the the actual proposal has been like laid out somewhere other than maybe in Discord but yeah I pasted it from what Potuz had sent me that.


**Potuz** [18:52](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1132s): I can open a CL repo issue. Because anyways this pattern is already used in my PR for EIP 7732. Because it's then is mandatory to have the envelope. So it's just repeating what we already do on EPBS. 


**Terence** [19:14](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1154s): We also need changes for the engine API as well I presume the CL issue will also talk about engine API changes. 


**Mikhail** [19:26](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1166s): Yeah we would need those. This why I just want to see the proposal so we can discuss it there. 




**Mark**[19:42](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1182s): Yeah I think it needs more discussion than a proper proposal. But yeah I think it's good so far from what I've seen because we didn't have a way of dealing with this either that was at all. I know the problem that he's talking about and it was something that was missed in Devnet 0 because technically MEV boost is broken right now on every client if you include. If you test MEV boost with the transactions that are in Electra. We just haven't tested it but we would find that if we did. And this is the problem that awaits us.


**Mikhail** [20:17](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1217s): Right but I just want to mention that fixing MEV boost does not sound like an appealing argument for me to make a change to the court protocol structure. 




**Mark** [20:27](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1227s): It's broken because of this problem whether MEV boost is there or not. 






**Mikhail** [20:32](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1232s): Yeah and actually this proposal can help to solve this problem like it will introduce a structure that could be used by MEV boost and will be kind of like yeah but anyway MEV boost could be fixed without this by introducing the same structure in the Builder API
Level. Right. 

**Mark** [21:03](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1263s): Yeah technically this issue is actually just caused by the fact that we dropped the payloads but it arose. It was easy to see with MEV boost. Anyway.

**Mikhail** [21:14](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1274s): Yeah. Got it. 

**Stokes** [21:20](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1280s): Okay so to summarise the CLs prune the EL data because generally they can but given the way that we have these request structures in pectra. This is no longer sufficient. I think that makes sense. The suggestion is to essentially solve this at the type level if only just to make it sort of clean to still drop the payloads while having the request data you need for the state transition at the CL. Yeah I mean when I first saw this I was thinking like you could just pull out the request and just put them same MEV next to the payload or rather the block. But it sounds like everyone would much prefer this actual sort of you know more specific SSZ structure. Does that sound Right? 




**Mark** [22:11](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1331s): Yeah. It just comes down difficulty of having something that has extra information that doesn't get hashed in that not having to do that makes it way easier.




**Right** [22:24](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1344s): Right. Okay. Yeah pus if you don't mind type an issue. I think that's a good Next Step here.




**Potuz** [22:32](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1352s): Already typing it I'll paste it here before the end of call. 




**Mikhail** [22:37](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1357s): Perfect yeah great thank you. One more thing a little bit of push back that I have is that we are trying to solve implementation complexity with changes to the protocol which are just you know not necessary for the protocol itself. This probably why I have a kind of like a push back on it and want to think more.




**Potuz** [22:59](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1379s): Yeah but I would argue the other way around I would argue that the current design is just philosophically wrong. The current design mixes in the same level in the same message data that is needed on the CL for the state transition that is purely on the CL side with data that is not needed in the CL at all. So I would say that the current design is just wrong and we're trying to fix that mistake. 




**Mikhail** [23:22](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1402s): Right it's not drawn I would say it has just different philosophy because yeah it has all data that are comprising the EL block and that's it. That's the basic stuff that we had before but yeah I completely understand your argument.


**Mark** [23:42](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1422s): And the other reason that we didn't run into this with the version hashes was that we put those in the CL block but they technically came from the execution layer. And so yeah it's  what Potuz said like they removed one layer higher in the tree. And so it worked out nicely. But since we'll presumably be adding more cross EL/ CL transactions in the future we should have them at the correct level.




**Mikhail** [24:10](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1450s): Yeah that's interesting maybe we we probably maybe we can really as Gajinder suggest just have those requests in beacon Block body. And you know send them. 




**Mark** [24:25](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1465s): Yeah that other proposal that you made on the engine API moving everything into the beacon block body would have also worked but it does have those Corner cases around new payload. 




**Mikhail** [24:39](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1479s): Right you mean like those that are related to optimistic sync edge cases. 




**Mark** [24:43](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1483s): Yeah yep in not sending new payload to for every payload that is the only reason that we found at least that not to do that but this is actually a strong argument to do that if we don't do what Potuz is saying.




**Mikhail** [24:59](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1499s): Yes.




**Gajinder** [25:01](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1501s):  I don't actually think that there is a problem in optimistic sync because when CL sends an FCU basically you construct the chain based upon a trusted latest root. So basically the entire chain before that is all trusted and when you're are sending new payloads then you obviously are sending the data for that particular root to be very fights. So I mean I don't really see it as an issue with respect to optimistic sync.




**Mikhail** [25:36](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1536s): Yes I agree with that so as long as EL block has all the data to sync you know and to verify we are not removing these requests from EL block we just sending these request to EL in a different way so it should it should work. They will be have yeah they will be checked by the block hash anyway. 




**Stokes** [26:13](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1573s): Okay yeah I will what Mikhail is saying like it seems like there are a couple different ways to solve this. Potuz has one solution. Yeah so I think if we get something written then we can continue the conversation there. Anything else on this topic? 


## Engine api proposal for devnet-2 [ethereum/execution-apis#565](https://github.com/ethereum/execution-apis/pull/565)


**Stokes** [26:25](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1585s): Okay cool next up we had an item for an engine API update this is from Lightclient for Devnet 2. I haven't had a chance to look into this in detail. Let's see Lightclient on the call.




**Lightclient** [27:04](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1624s): I think this is similar to this question that we've been talking about. So I don't know if we can really make a decision before we decide where the requests actually need to
Live. 




**Stokes** [27:20](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1640s): Okay that would influence this PR you have here.


**Lightclient** [27:24](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1644s): I mean I guess like you could still have the request encoded in the similar way. But it sounds like we're probably going to have some sort of are people wanting to do this like Union of requests or will we still keep them separated at the CL. 


**Mark** [27:40](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1660s): Generally makes it easier to deserialize when they're but that's I can't say for sure. 


**Lightclient** [27:51](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1671s): Basically I'm proposing that over the engine API the requests are sent as an array of the requests as a request object not like the individual type. Because right now on the EL we're converting the list of requests that exists in the EL block into individual lists of individual request types. Unfortunately this adds some requirements to the EL to understand from just a single individual block whether a request type is enabled or not. Because if I just give you an EL block and there's no request of a certain type and we've added like you know we're three or four Forks down the road and we've added some more types of requests like you can't tell just from the Block anymore. If the request is enabled or if there's just no request for that block. And so I think it makes the engine API on the execution layer side a bit more annoying. So I'm basically proposing that we send over the request object as it is on the EL. And if on the CL you use the union of that then that would kind of directly pipe into that data structure if you are separating them out then you would be able to just separate them by reading the list of typed requests and deserializing them into the list that they should go to. 




**Stokes** [29:38](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1778s): Okay so this is related but it sounds like we'd still possibly want to do something like this even if we end up changing the structure on the CL. 


**Lightclient** [29:50](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1790s): I think they're related but yeah it it is it can be done either way for how wherever it lives on the CL. 


**Stokes** [30:01](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1801s): Right. So yeah. 


**Lightclient** [30:05](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1805s):  My proposal is for the requests to come through as a single list of all of the requests and for the type of request to be identified by the type JSON field just as it is with type transactions currently.


**Stokes** [30:22](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1822s): Yeah that makes sense right. Like we have these set of cross layer features and we need to figure out exactly where the boundary is across EL Engine API and CL. That makes sense. Potuz you have your hand up?


**Potuz** [30:38](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1838s):  Yeah so I mean these problems are related but they they seem to address a different area different problem itself which is we currently have a type on the CL a type on the EL and then we have this messages that are being exchanged on the engine API. What my proposal was was about the type on the CL and this doesn't contradict Matt’s proposal. I would still suggest that the type on the CL has this level structure and then we put in that on what level the requests. And this requests can be a list of requests can be a union can be separated. I don't care. On the EL side it seems from what Matt says that it would be better to have the type one request object which is a list of unions which may have different type of requests list of lists. This would be fine as long as the engine API puts them at a different level. This already solves my problem and then the object that goes in the level up we could handle it either the EL has the problem of trying to interpret it and separate them or the CL has the problem of trying to interpret and and separate them. It seems from what Matt is saying that it's better for them if the CL interprets them and separates them in different objects that's fine by me. Well we already to know what those objects are. So I don't see any problem with what Matt is suggesting into putting out on the envelope one object which is the requests.


**Stokes** [32:13](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1933s): Yeah that makes sense. 


**Mikhail** [32:18](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1938s): Yeah one of the ethereum arguments that Lightclient made is like let's just have on the API level the data structure that maps on the core data structure to avoid potential edge cases in the future. One I don't know if it's a problem or not but now CL will have to if this proposal accept CL will have to kind of handle request mapping from different lists to just one but it's not it does not seem like a big surface for bugs. And those bugs can be found easily. 


**Mark** [33:06](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=1986s): It's I think it's just that the different types have to be I think carefully thought of if we have different kinds of requests such that it's not ambiguous on which kind is to serialized into. 


**Lightclient** [33:23](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2003s): Well the type the type fill should disambiguate like what type to Deserialize into. So even if some fields are reused across different types then you can just look at what that type value is and then put them into the correct SSZ object.


**Mark** [33:44](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2024s): Okay so there's a byte or there's a is there something that marks it you said a type value?


**Lightclient** [33:51](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2031s): Yeah I mean it's the same as how we represent transactions over the RPC. So if you require a block with transaction values filled in then you'll get a list of the transactions and the fields are sort of reused in this like generic transaction. But there's a type field that says whether it's type one transaction type two transaction type three whatever and then you can use that to differentiate. So that way you don't have to just like look at the fields and infer based on the presence or non presence. 


**Mark** [34:26](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2066s): As long as we got something like that I think would be fine.


**Lightclient** [34:29](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2069s): Okay.


**Stokes** [34:34](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2074s): Terrence! 


**Terence** [34:36](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2076s): I guess one thing to note is that when we get payload as a proposer that we also have to parse this request on the CL side right because we have to put those on the envelope or become Beacon block body ourself depends on what the decision is.


**Mikhail** [35:06](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2106s): Small comment here. I believe that CL while sending those requests to EL may not respect the order of those requests by type as it is in the EIP. I guess this is true. 


**Stokes** [35:31](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2131s): I don't know if there's an order on spec?


**Lightclient** [35:38](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2138s): I mean the order should be inferred just from the engine API message. So as you're pulling out the values you can just keep it in order and the EL would have placed it in the order that it was already on the execution layer. 


**Stokes** [35:55](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2155s): Right but is it sorted by the type byte?


**Lightclient** [36:00](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2160s): It would be sorted by the type bite and then intra type byte like each proposal has the different way of ordering and the EOA will have already ordered all of that. So as long as you take it from the engine API and interpret it as it's ordered from the engine API it should be the same.


**Stokes** [36:19](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2179s): Right does that address your concern Mikhail? 


**Mikhail** [36:22](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2182s): Yeah I'm just thinking that CL should respect this order or not yeah but that's detail maybe not worth talking about it.


**Stokes** [36:34](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2194s): Well the order is important at least intra type. Yeah so definitely should go in the same order as given.


**Dustin** [36:55](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2215s): I'm wondering like what is the simplification on the EL side here? 


**Lightclient** [37:04](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2224s): When EL converts the block into an engine API message. It doesn't know from the block data how to fill out the presence or emptiness of a request. Bcause in the request object on the E it's a list of typed values. And so if in a future Fork we add another request type then I can't tell from the Block itself whether that request type is empty or if we haven't activated that request type yet on a fork. So propagating that information in is not that simple we can do it but it's kind of weird for us to represent on the engine API. This data in a different way than it's represented on the execution layer I think that this is just like a much better simplification and the CL can much more easily differentiate whether the request is empty or whether that fork is not
Active. 


**Dustin** [38:15](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2295s): You don't know what Fork you're in or what the block for fork the block was it. 


**Lightclient** [38:24](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2304s): Yeah I mean usually we don't Plum the fork work information through every code path in the engine API. It's kind of at the top level of verifying like the method that's coming in. But then when we're dealing with the block itself the block doesn't have the concept of this is a Bellatrix block. Like on the CL I think you guys are very good about separating the different types of fork blocks from each other. But on the EL I think this is how pretty much all clients have implemented it. We have one block that represents all of the block types and we use the presence like the nullness of a value to sort of determine if that thing is active. And so this is again like part of the reason why requests were added in the first place in this format was to take advantage of how ELs have been built historically. And this is just a continuation of trying to avoid rearchitecting a lot of the client or doing things that might be like bug prone just to represent things in a certain way on the engine API.


**Dustin** [39:37](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2377s): Okay fundamentally this is a fragile heuristic the idea of and I don't think this goes against anything you're saying but the idea of checking for the presence or absence of specific Fields. Look we in Nimbus it for certain things too unfortunately because yeah we have to but but that is one of the worst parts of reading certain of these JSON objects because it is a heuristic. And I would say build doubling down on that is maybe not super great. 


**Lightclient** [40:19](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2419s): Yeah I mean we're like 12 Forks into this design. So it's a little bit difficult to just like turn the ship around and change.  How we have to protect the block. So I agree it's fragile but I don't really know if there's much that can be done at this point unless some EL's also agree that they want to like sit down and change the way that they represent the block it seems like this is not a difficult modification to the engine API and makes things simpler for all of the EL’s. 


**Stokes** [40:57](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2457s): Can you not infer which Fork you're in from the engine API method version. 


**Lightclient** [41:04](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2464s): I mean you kind of can. 


**Mark** [41:08](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2468s): But like that those are decoupled.


**Lightclient** [41:14](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2474s): Well I think now they're sort of coupled again. Like now we're pretty strict about checking what Fork the person is requesting. So if you call like Fork Choice updated V4 with a non Prague block. I think it should return error. So I think that you can kind of infer now? 


**Mark** [41:41](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2501s): I think we do oh I'm not sure.


**Lightclient** [41:48](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2508s): No with the parameters like you can't build I don't think you can build a Cancun block with fork Choice updated V4. I might be wrong on that but nevertheless propagating this information down into like our block type is different. I mean if other execution clients don't have this problem at all or think this it doesn't make any sense then you know maybe I can go look at it some more and figure out but I think that this is the case for a lot of different teams.


**Potuz** [42:22](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2542s): Why do we really need to care about typing here on on the API why would it be it sounds from what you're saying Matt that it would be fine for you. If we send you for example a list of lists which are just interpreted as row bytes and then you make the interpretation and change into your into your internal type and we constructed that list from our internal type would that work well. 


**Lightclient** [42:46](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2566s): Then you would need well if you send a list of bytes and we would need to figure out what the byte structure is and then it would have to probably be RLP. Because we haven't done SSZ yet. So it's like you have to interpret the data like the actual data, not just the bytes. So it's different from the transaction data. 




**Potuz** [43:05](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2585s): So then probably it might be an issue for us because I don't think we have unions correctly implemented in SSZ.


**Lightclient** [43:15](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2595s): I mean you don't have to implement SSZ unions I'm just saying that if you happen to implement the SSZ union. Then this format would map very closely to what the union like you can still during Deserialization of the engine API message determine where in like the individual Fields like the list of withdrawal request the list of consolidation requests where those requests should go from that message. That's not a problem. I'm just saying like if you wanted to have if there was a desire.


**Potuz** [43:44](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2624s): It wouldn't be against like we keeping them separated in our internal type. 


**Lightclient** [43:51](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2631s): Yeah it's not for me to say like whatever you feel is right on the CL. I just think over the API it's simpler for EL's to just send what the block data already is rather than doing some interpretation of the block data and combining some Fork logic like we can do it. Don’t get me wrong. 


**Potuz** [44:10](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2650s): To me no that this sounds correct to me it's it's fine it's just moving that the interpretation that seems to be easy on our side. 


**Lightclient** [44:17](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2657s): Yeah that was my take.




**Mark** [44:21](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2661s): Just to we we do call like new payload and get payload V4 before the fork and I haven't seen any errors from any like we're running down that one it's fine. And I'm pretty sure the API was designed that way that's why these fields are nullable in the first place because they have to be null before the fork. So we we've decoupled those I think they're still Decoupled.


**Mikhail** [44:50](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2690s): At least this back requires the AL so the errors should return.


**Lightclient**[44:59](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2699s): I mean yeah it says engine new payload V4 spec the client must return unsupported Fork if the time stamp of the payload does not fall within the time frame of the Prague Fork. So if you're calling new payload V4 before Prague technically that's should return error. 


**Stokes**[45:31](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2731s): Okay yeah Mark you say no.


**Mark** [45:38](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2738s): Same with get payload. So I don't know right I mean we may not be implementing that correctly but that is like the letter of the spec I think. 


**Stokes** [45:49](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2749s): In any case it sounds like this would be helpful to EL's and CL's have Liberty to take data kind of just take the data and then do what they would like with it. So I think it makes sense from here. I think yeah so we have this PR and then the other issue we will iterate on and then yeah I think just having them all together is the next Stop. And then yeah we can go from there but generally it sounds like both of these seem like directions Moving. Any other comments on this otherwise we will move. 


**Dustin** [46:34](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2791s): I guess that what this does make a certain style of JSON decoding a little more a little trickier. Let's say so right now Nimbus does the best it can to decode Json and receives according to as strict a schema as the specs sort of support in each case and these variant types just utterly rake this I mean we we can't. We can then all the usual we read it and figure type is out to new object. I assume I don't think there any bistic alternatives. This is what JSON supports because it's not ordered but it's a mess no matter how it happens. So I mean as long as people are basically just upfront that it is not particularly less messy for CL's to do this than for ELs to do this that's fine. This is just a move of complexity and messiness from the EL to the CL and it's feasible either place but that does not moving into CL does not solve this problem. Let's say as maybe how frame it just moves it. 


**Stokes** [48:09](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2889s): Sure but then CL clients I think are more equipped with just the types they have at hand to handle the problem. So this does seem like the direction to move into me. 

## SSZ StableContainer in devnet2?


**Stokes** [48:28](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2908s): Okay next up Etan has an update on SSZ and stable containers. Essentially he's asking if we want this in Devnet 2 there's a link to the EIPs here. Let me just grab a link to this. There's a very nice comment here on the agenda. So yeah link to the EIPs specs here test and then I believe this is linked to Kurtosis Network they have running. So yeah that's all super exciting to see the question is if we put it in Devnet 2 or not. You know just like process-wise generally we would formally include these things into the fork. And then you know devnet would be Downstream of that. So if we want to consider SSZ and the stable container update for pectra. That's the conversation we will have to have. Maybe I'll just pause there so how do we feel about including these EIPs. Well okay actually maybe Etan is there anything else you'd like to add before we get into that? 


**Etan(Nimbus)** [49:42](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=2982s): Yeah I have minimized the EIPs to the minimum like that. I think we should put in Electra because we have this opportunity now because Beacon State reaches a new power of two number of fields. So gets reindexed so if we don't do this change now then like rocket pool mainly but also other staking pools will have to do yet another redeployment of their contracts every time that this happens again and also when we would introduce this table later on. So this what's in this PR today it does not have SSZ transactions or any of the other SSZ stuff. I think that the other stuff like SSZ transactions can be moved later down into verkle. So that the verkle fork is the one that changes data types more strictly. But we still can do the CL only changes today so that EIP 4788 becomes practically useful I have also obtained support from rocket pool. I just linked it this Discord link where they support the EIP and I can also obtain more similar statements from other staking pools if that's Required. So yeah the PR consensus specs is linked in the comment that stalks linked and I have also generated consensus spec tests. 


**Stokes** [51:33](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3093s): Cool. Right. Let's see I think if I'm interpreting correctly there are some clients Teku here, Load star who are saying plus one for the SSZ feature. Any other clients want to chime in?


**Kasey** [52:00](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3120s): I'll say for prysm. We were ready to say let's try Devnet 2 but I think including in specs like merging into pectra is more of a surprise. So I don't know if the rest of the team wants more time to consider that.


**Tim Beiko** [52:19](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3139s): What would mean? Yeah Devnet 2 is pectra Devnet 2 right.


**Mark** [52:26](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3146s): I think he was did you mean that prysm is ready for Devnet 2 but if we had stable for or stable containers it would take longer.


**Kasey** [52:34](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3154s):  oh sorry no I meant that I guess like a there's I thought it was more experimental like a finality of inclusion. But yeah so I haven't speak to the rest of the team on it but yeah I think we can do Devnet 2. So I don't know if there's opposition to including stable containers for any other reason but I'll say from an implementation side. Like we're working on it on track. 




**Stokes** [53:04](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3184s): Right I mean I think the obvious thing is just the Pectra is incredibly large already I mean especially if we end up with PeerDAS and the fork. So you know at a certain point we do need to be very realistic about how big the fork is and the risk that entails for actually shipping this thing. Again you know I agree with the justifications Etan gave around this feature being valuable and vaccum that being said like this is I think the biggest hard fork or one of the biggest that we've ever done and that should not be taken lightly. Pari had another comment here in the chat that essentially okay maybe an EL person can help me here. But it sounds like EOF is in Pectra but it hasn't you know been on Devnet yet. And so that's how well and good. But then with that would mean then is yeah it's like also another really big change and again just looking at Devnet 1 today. It doesn't seem like Devnet 1 is going super well. So I do want to caution against kind of yeah biting off more than we can digest. So to speak. 


**Mark** [54:19](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3259s): I at the risk of saying something wrong I believe. I mean this is a CL change and CL has less stuff than the EL at this point I think.


**Stokes** [54:36](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3276s): Right.


**Paritosh** [54:37](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3277s): But I only partially agree with that I think peerDAS is still a massive change and there are a lot of shared resources between EL and CL for example we have combined testing teams. And I do think at some point we have to get realistic that we can't just have every EIP in and at the same time just keep increasing the scope. That is a Bottleneck.


**Stokes** [55:02](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3302s): A very real One. Okay I mean unless someone wants to make a very strong case here right Now. I would suggest the following yeah like let's work through devnet 1 and then I would even say wait on devnet 2 and yeah we can reconsider this in the future. 


**Paritosh** [55:42](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3342s): But again one point I do want to make would adding SSZ to a devnet actually change anything like for example we have SSZ Devnets. So don't we kind of have all the data we need to decide if SSZ goes into pectra or not and once we decide if it goes into Pectra or not then we can talk about Devnet scheduling. To me that sounds like the workflow we kind of need to have so the question right now is not when SSZ or stable containers is in a Devnet but rather should it go into Pectra or not and what data do we need to make that decision. 


**Sean** [56:20](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3380s): So I feel like an important part is understanding like how big of a pain breaking Merkel proof is for Appeler teams.We definitely like I've heard from like smart contract Auditors at Sigma Prime about how this impacts their clients and like they're avoiding bugs I guess kind of narrowly by like realizing in upcoming Fork is going to break their contracts. So that's like an anecdote that I can speak to but if it's like easily telegraphed that we can that we're going to break roots for Beacon States in Pectra and then like once more for stable containers and that's it. Like how much worse is that than just having like stable containers in Pectra. So pretty much appler input I feel like is really important in deciding this one as as far as like work for client teams in Lighthouse we have like a pretty far along implementation the changes in the client code isn't very large. It's more impactful on the SSZ libraries obviously but I don't think it's like crazy definitely sympathetic to the fact that the Fork's very big and I want to include peerDAS. So I would definitely lean towards like would rather peerDAS and non step containers if I were to choose but it's also like they're not really weighted equally like stable containers is definitely smaller than peerDAS.


**Mark** [58:04](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3484s): Would also on that on that point about messaging like they're also app developers are trying to develop apps. So knowing sooner rather than later or telegraphing sooner rather than later is also helpful to them. because they know what they can build now and get audited now. 


**Paritosh** [58:27](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3507s): Would that mean if we have like a public SSZ Devnet would that allow app devs to play around with it enough to know what breaks or not breaks or does it need to be Pectra Plus SSZ for them to actually get this data.


**Mark** [58:41](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3521s): They actually just want to know what's in the fork because they've been bugging us about.  I mean just an example like Ian layers they're trying to get their things audited. And they've been bugging us about whether or not the fields that are in the beacon state for pectra right now are likely to be the final fields that are in the Beacon state. But that question is irrelevant if we don't know whether or not we're putting in stable containers. So it's more like what Sean said like it's about knowing what the real schedule is for when what is going in what Fork that makes it easier on them. 


**Stokes** [59:22](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3562s): Sure but like we can tell that you know you could look at Vector today without the stable containers and you would know right like I don't just from what you said it doesn't like they're asking about oh will this be stable forever they just want to know what to Target for the fork. 


**Mark** [59:39](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3579s): I think so. 


**Stokes** [59:41](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3581s): Yeah all right Enrico.


**Enrico** [59:46](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3586s): Yeah I just want to add that so what what's been targeted for be included in Electra is a let's say simplified version of stable gold implementation which does not cover all the full spec that is in the stable container EIP. It's also possible that the client team could implement the the quick version to just enable stable container and then have the full implementation for next forks. 


**Paritosh** [1:00:25](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3625s): So basally the CLs would like to have it included in Pectra have a public Devnet. So that app devs can give them feedback and then decide if it's actually included in Pectra is that kind of the work I'm getting.


**Stokes** [1:00:38](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3638s): Well they can get public feedback from as SSZ Devnets right like it sounds like what has been surfaced on this call at least is like the these  applications just want to know what's in pectra. Not  necessarily that this you know XYZ or Pectra and that will be stable forever . These are two different things.


**Sean** [1:01:06](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3666s): Well I personally don't know which of those is true. So like it could be that application teams actually really hate these like Merkle proof breaks that could be true. It's more like yeah I feel like we just need more input from there and like maybe other teams have other input for for like from application layer devs they interact with but I personally like I don't know how critical this is.


**Stokes** [1:01:44](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3704s): I mean do other CL teams feel that it would not be disastrous to increase pectra scope beyond what it already is like. Do you not feel that it's already quite big? Okay sounds like then maybe we'll take some time to think about that. And then how can we move forward? So yeah again unless someone feels the pressing need to make a decision right now. Sounds like we can decide in the future again. I think we should focus on Devnet 1 for the time being. In the meantime I think we should get more information from App developers to the extent we can. And yeah I would recommend each CL team to think very seriously again about like Petra scope And what that means for a successful hard fork. Every EIP we add is just going to you know add more code more risk for bugs generally complicated testing and you know all the usual bucket of things. Etan?


**Etan** [1:03:19](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3799s): One thing I'm wondering about peerDAS is it's CL spec I think right now it has an optional in there. So I'm not sure if that one is still there or but if it's there it's sort of that's a dependency there. Because if the peerDAS is activated before optionals become a thing then that design needs to change as well.	 


**Stokes** [1:03:55](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3835s): Right I don't recall an optional anyone else?


**Etan** [1:04:01](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3841s): Yeah I can look for it. 


**Stokes** [1:04:02](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3842s): Yeah I guess we should go take a look. I don't recall there being one. Generally we avoid them again because there's limited support and SSZ libraries for them. Okay I think I'm going to call it on that one I do think we have a few things we can do to get a clear picture of SSZ but again I will just call out yet again. Think very carefully with your client team again about pectra scope.  I know that you know hard Forks come very infrequently and so it's tempting to try and get as much in as we can but at the same time if it's you know if there was a problem rolling a hard Fork that would be worse than waiting another fork or two for whichever feature we have under consideration. Okay thank you yeah Etan followed up. It's actually a verkle usage of optional and not peerDAS. 




**Stokes** [1:05:24](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3924s): Okay and speaking of that was the next item on the agenda. Guillame I can’t here you?


**Guillaume** [1:05:49](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3949s): Yeah I was just going to say don't get out of the way to support optionals just for verkle because we're currently looking at other options. We would still like to have it but yeah we it's not the end of the world for us if it's not there.  


**Stokes** [1:06:08](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=3968s): Okay good to know. I think we're early enough in the verkle development process that yeah it's there's plenty of time to handle that. Okay let's move to PeerDAS. So yeah I think there's a couple of things here we do have some time left on the call. Okay good. So let's see, yeah first I don't know if anyone here has been working on the PeerDAS Devnets. If someone has and give a small update that would be very helpful. The last time I looked there were devnets but they had a number of bugs and generally yeah the network was not stable. Does anyone have any later information on that Work. 


**Sean** [1:07:03](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4023s): So I talked to Jimmy from our team and he said on the last breakout call people decided to focus on just like fix fixing existing bugs and stabilizing clients as opposed to like focusing on another testnet. For example, I think there's like a testnet delay while things stabilize the clients. 


**Stokes** [1:07:30](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4050s): Yeah that makes sense.


**Gajinder** [1:07:33](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4053s): Yeah from on the I was also on the breakout call. And I think we also discussed that maybe we want a more cleaner pack in the sense for example we would want a metadata PR that is out there to be included in the next Devnet. So that we can have a Devnet which has sort of all moving Parts together rather than Missing data where we assume something and then we don't have a very good pairing. So I think yeah so for now we also want to focus to get the spec right and to sort of make sure that we have everything that is required to have a very stable Network. 


**Stokes** [1:08:21](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4101s): Yeah certainly right and so kind of on this note taking that all into account and again myself and you know others in the chat here like there's very broad support for PeerDAS as soon as possible. As soon as possible here means in pectra so the question then becomes can we ship here peerDAS and Pectra. If it becomes the case right that there's difficulty with PeerDSA is specified. I did want to bring up an alternative in terms of simplifying the initial PeerDAS roll out. So this would kind of be like let's say like a modification to the road map so to speak. I'm talking with Francesco and a few others. And I think we've at least identified another path and so yeah let me summarize that. So with pectra or sorry with PeerDAS there are kind of three like core functions that the client performs right so the first one would be distribution. So that's taking you know at the very beginning you have a block with many blobs the blobs get split up in these columns The Columns that are gossiped in PeerDAS. This is the distribution phase. There's next then a sampling phase where you then in turn ask your peers for these samples. That then gives you sort of your availability sort of you know evaluation or assessment of a given set of Blobs. Then this third part of the pipeline is reconstruction which is required in the event that there is some issue with  distribution or sampling. So right now the way PeerDAS is specified in pectra is that it's essentially doing all three of these task distribution sampling and reconstruction. And my intuition is that this middle part sampling is going to be where most of the complexity is. It might even be good to hear on this call if clients think otherwise but essentially the suggestion would be to drop sampling from the initial peerDAS rollout this should essentially. Yeah I think there will be a few other parameter changes to maintain the same security level but it would be possible to essentially just have the distribution phase along with the Reconstruction and then we could drop sampling and the idea here is that if sampling does become this sort of you know hairy  implementation concern. Then we can get to a place where we could you know very realistically consider increasing blob counts with this reduced or like modified peerDAS scope in pectra. Okay that was a lot. Do any clients have any takes so far or can I clarify something from what I just said? Any responses? Oh yeah Gajinder?


**Gajinder** [1:11:26](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4286s): Yeah I just I think that is a good thing that we can basically later on add sampling or basically we can also initially launch with having full custody of all the data columns because the blob count has not increased. And so there is not much data and bandwidth blow up anyway. Also what I want to wanted to add was that the PR in which we are able to the CL can specify the blob Target or blob count. I think we should also get that PR in Pectra if it's not already in the scope. And we should basically include it in specs or and in Devnets.


**Stokes** [1:12:10](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4330s): Right and so I think the actual numbers would be some of dependent on what peerDAS looks like but yeah I agree that's a good point and yeah I think it's time to yeah do that very Soon. Right and yeah something that I think would be helpful there's a question in the chat just yeah essentially asking for a written down version of what I just said I'm happy to put something together and I can elaborate a bit more and make this more of a proper proposal for consideration. Essentially this would just be a way to hedge like again like development uncertainty of peerDAS. It could be the case that we do peerDAS as specified. And it's all in time for pectra and everything's good. This is just an option worth considering especially we feel like the peerDAS implementation is not moving along as far or as quickly as we wanted to. So yeah something to get on the radar now.




**Mark** [1:13:15](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4395s): Just want to I think a while back we're still considering PeerDAS might maybe make it in before Electra and that was maybe why we decided not to rebase it on top of the electra spec but I don't remember if that was the reason. I think that's something, yeah.


**Stokes**[1:13:36](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4416s): Yeah that I think was I mean yeah so that's slightly different thing but essentially that was to just simplify development if lur is going be Target then it makes it harder to then rebase PeerDAS on top which is moving Target so they were left separate for for example for the Devnets that we've had so far. We will at some point need to yeah put peerDAS into electra proper to that I would just point to the previous conversation around again. It's the sooner that we can finalize really the sooner we can finalize the pectra scope that we have the better. At least if only to unblock PeerDAS which again is I think everyone agrees an incredibly important Target to aim for.


**Gajinder** [1:14:27](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4467s): And we also need Pectra Devnets running smoothly without any Forks before we decide to rebase because then the debugging for peerDAS would become difficult.


**Stokes** [1:14:41](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4481s): Right.


**Etan** [1:14:42](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4482s):  For peerDAS they like the current design I think still has this special activation Epoch like to make it a here as not a fork. If PeerDAS is actually enabled on Electra like at the same fork Epoch it also allows me to like make the stable container PR even more simpler. Because right now a lot of the changes in there are because the blobs side cars need to be updated because the beacon block body gets reindexed and and if peerDAS activates on Electra there is no more blob sidecar right. So so that inclusion proof doesn't Break. So it's if we can align it makes it more simple as well.


**Stokes** [1:15:43](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4543s): Okay yeah I mean that's good to hear right. So then maybe we go ahead then and we well there is a bit of a chicken and egg here but yeah because essentially we we want to have like enough confidence in PeerDAS that we can then put it on top of Electra but we also want Electra be stable enough to do that. So that was kind of the the issue and that was also why we had this sort of special epoch activation idea. But yeah I mean if everyone's on board then yeah let's go ahead and just go for Electra and move from there. Does anyone feel opposed to moving ahead with that right
Now? 


**Paritosh** [1:16:36](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4596s): Would this mean we do combined peerDAS Electra devnets in the future or do we just want to activate an Electra would keep the branches used Etc separate.


**Stokes** [1:16:50](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4610s): Yeah that's a good question. I mean I think the simplest thing would imply yes it's together
Now.


**Paritosh** [1:16:59](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4619s): Considering we haven't had any stable devnets on anything I think this is going to be really really hard to debug.


**Stokes** [1:17:12](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4632s): Acknowledged. So then maybe this is a little premature and yeah we should just
focus onDevnet 1.


**Paritosh** [1:17:21](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4641s): If it's just about activation I'm on board. We also done this in the past. I think for certain features we've had like Electra Devnet as the activation Epoch. We just keep them as separate Devnet cycles for example a 7702 bug shouldn't then lead to all CL devs having to debug what happened to their Network right. So we can still keep the tests separate we can just change how the features are activated I guess or how they're interpreted by the client. 


**Stokes** [1:17:53](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4673s): Right.


**Dustin** [1:18:06](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4686s): Okay the current issue here with the fork schedule one one of them is that it redefines Deneb. Like so I understand that some CLs apparently are treating this as a flag a feature flag of some sort or I'm not sure precisely what the code structure here. But in Nimbus we tend to refrain from these for any longer term usage and the result is the fact that this has to activate in deneb. This is how the Devnets are defined right now. Means that we cannot incrementally merge this. And so I would actually say this tension that that's being brought up about okay well we can have a for testing purposes separate Devnet or combined Devnet and the separate Devnets though is that the separate Devnets also create this artificial breakage and it is break
bre break sorry breakage it. That is a broken Fork schedule I'm sorry but I'm gonna that it just is that that breakage in the fork schedule is sort of makes hinders that testing in certain way ways and it hinders it means that even if let's say two or three months from now we all agree yeah peerDAS is great you know move forward as quickly as  possible. And but now it has had to at least in Nimbus stay outside of that main development trunk because of this broken Fork schedule. Because we cannot risk redefining the production Fork for this purpose to have columns like it's not that's non-starter. So I mean so I would say it's actually more effective and more efficient for testing as well overall at some point to combine the two. So this is my claim. 


**Paritosh** [1:20:08](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4808s): Yeah I agree as well it should be combined my question is just when we do that if it's more advantageous to do it right now. Sure if there's still open questions for example deciding some parameters that PeerDAS still needs to or some parameters that we think PeerDAS might still change by then we could wait until those are changed and then merge it through. But if it feels like it's stable enough then yeah I'm on board for doing it all. 


**Mark** [1:20:36](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4836s): in a previous call we discussed having like a PeerDAS Epoch type parameter and I think we've got a PR for that. I'm not exactly sure if the current Devnets are just doing peerDAS from Genesis or how it's being done currently. But I don't think that was ever decided either either and that I mean having a peerDAS Epoch is one way to avoid that issue of not being able to test having the test get in the way of each Other. 


**Dustin** [1:21:16](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4876s): So I'm skeptical of the idea of the separate Epoch overall but I agree that for testing it's maybe plausible. However I would say in terms of isolating things it would at least be possible to separate out the fork Epoch. So that it starts at in Electra. There's sort of separate things here one is there a delay in terms of I guess my question right. So when you're saying like this activation Epoch. One is sort of activating at deneb or Electra or sort of fork future Epoch as a pure testing thing. And another is that people were seriously considering at least some weeks ago. Well maybe we'll activate PeerDAS you know 50 epochs after Electra starts. So the the first I think is just a testing concern and we can work with that. the second I think is doesn't make any sense. 


**Stokes** [1:22:29](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=4949s): Okay that's helpful so one other point that was brought up in the chat is essentially that I think many of the peerDAS Implementers are not here right now. There is an implementation call that they have. This is probably or rather that's probably the right form to get into this further. We are also almost at time in this call. So yeah again I would suggest let's focus our attention on the devnets for pectra and yeah it sounds like we're going to need a little more discussion around exactly how to move forward on this issue. It sounds like if we have you know if we get a very stable pectra Devnet going then I think that simplifies a lot of the decision around yeah do we rebase PeerDAS on Electra. And you know get rid of this activation and all of these types of things. Yeah Pari's asking like schedule it during the peerDAS breakout that's the Idea. Okay we just have a few minutes let's see I think dapplion had one last minute thing. Let's take a look. Blocks BeaconBlocksByRange v3. Here's a link to the PR. Is Dapplion on the call? 

**Dapplion** [1:24:11](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=5051s):Yeah I'm here.

**Stokes** [1:24:13](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=5053s): Okay. great oh there you are cool yeah would you like to give us an overview?
 
### [Add BeaconBlocksByRange v3 consensus-specs#3845](https://github.com/ethereum/consensus-specs/pull/3845)


**Dapplion** [1:24:19](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=5059s): Yes very quickly there is an issue with the canonical RPC if you want to sync a situation where you want to pull a long Fork of blocks from which you don't know which Peer’s consider them canonical or not. The current BlocksByRange root is spec in a way that you just submit a range of slots and the node will provide whatever the node considers canonical. You can query that information with status message but that there is some as synchrony on getting those status messages and it forces you to basically pull this status message every time you want to the request. If you want to be sure that you're pulling the right Branch. This has not been an issue because we haven't had like crazy forking on mainnet but if hit the fun this could be an issue. So what BlockByRange V3 introduces is changing the request from just hey Peer give me range of slots to hey Prer give me a range of slots on this specific branch that may be your head or may not be your head. In my opinion that makes it much more resilient to the types of syn that we are implementing in Lighthouse at the moment for these very forky situations. And yeah I think it's an no-brainer. I'm not I'm not sure why this was not introduced at the very beginning and I don't see much downsides. I'm just curious for comment if other clients have specific ways to handle sinking long Forks that may not be canonical. Otherwise this route would be a good addition like as a caveat something that you could do now is use the blocks by root. But with blocks by root you are forced to do reverse sync and that's really easy to be attacked. Because you cannot verify chain of blocks that you backward sync until it gets rooted somewhere and that chain can be very long. So a peer can just give you garbage and DOS-ed. So you need to forward sing somehow that's why this root. So yeah if you can check the PR. Let me know if it makes sense. I think the implementation should be simple. So maybe you can Target Electra it's not terribly urgent but would be nice. That's all. 


**Stokes** [1:27:00](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=5220s): Thanks yeah I've had a chance to look at this myself . Yeah thanks for bringing it up and yeah please everyone take a look. Okay we are almost at time and I think that was essentially yeah looks like that was everything on the agenda. Any closing questions comments, remarks to wrap up the call. Okay then let's call it. Thanks everyone. I'll see you on the next one. 


**Sean** [1:27:57](https://www.youtube.com/watch?v=lmzAUqsIbIE&t=5277s): Thanks everyone bye.

___
## Attendees

* Stokes						
* Etan (Nimbus)
* Terence
* Mark Mackey
* James He
* Enrico Del Fante
* Ben Edgington
* Ansgar
* Saullius Grigaitis
* Mikhail Kalinin
* Trent 
* Tim Beiko
* Rohit
* Guillaume
* Pooja Ranjan
* Potuz
* Dustin
* Mehdi Aouadi
* Ahmad Bitar
* Peter
* NC
* Toni Wahrstaetter
* Annathieser
* Stefan
* Phil
* Mario Vega
* Paritosh
* Gajinder
* Sean
* Francesco
* Nflaig
* Lightclient
* Roberto B
* Scorbajjo 
* PK910
* iPhone
* Kasey
* Katya Ryazantseva
* Lukasz Rozmej
* Preston Van 
* Marius
* Radek
* Justin Florentine Besu
* Joshua Rudolf
* Nishant
* Hopinheimer
* Kolby Moroz
  
___
# Next meeting  Thursday 2024/8/08 at 14:00 UTC

___
## Reference Links: 
* ### EIPs: [https://eips.ethereum.org/EIPS/eip-7688](), [https://eips.ethereum.org/EIPS/eip-7495]()
* ### Specs: [etan-status/consensus-specs@ef-eip7688](https://github.com/etan-status/consensus-specs/commit/ef-eip7688)
* ### Tests: [Adopt EIP-7688: Forward compatible consensus data structures consensus-specs#3844](https://github.com/ethereum/consensus-specs/pull/3844#issuecomment-2239285376)
* ### Kurtosis: [https://stabilitynow.box](https://stabilitynow.box/) (bottom left config)

