# Consensus Layer Meeting 140 #1129
### Meeting Date/Time: Thursday 2024/8/22 at 14:00 UTC
### Meeting Duration: 75 Mins
#### Moderator: Alex Stokes
###  [GitHub Agenda](https://github.com/ethereum/pm/issues/1129)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=hSNJ6vURfmE) 
### Meeting Notes: Meenakshi Singh
____
| S No | Agenda | Summary |
| -------- | -------- | -------- |
| 140.1   | **Consensus-Specs Release:** | v1.5.0-alpha.5 is now available.|
|140.2| **Pectra Devnets:**|Overview of devnet-2, with a bad block likely due to early EIP-7702 implementation; clients are debugging.|
| | |Minor JSON-RPC issue discussed.|
| | |Update to EIP-2935 for clarification around behavior.|
| | |Devnet-3 launch expected next week.|
|140.3|**Pectra EIP Updates:** |EIP-7251 update to adjust correlated slashing penalty and fix an overflow issue.|
| | | Proposal to refactor beacon chain data types for streamlined execution request processing in Electra.|
| | | Proposal to refactor engine API for better execution request handling between EL and CL, with some support and ongoing feedback.|
|140.4|**PeerDAS :**|Implementation updates and client status for peerdas-devnet-2 specs, with a devnet launch expected soon.|
| | | Clarifications on EIP-7742, including engine API payload attributes and blob flexibility issues.| 
| | | Discussion on blob limits per transaction and handling in the mempool or networking layer.|
|140.5|**Closing Remarks:**  |Agreement to label the next hard fork after Pectra as “Fulu” (portmanteau Fusaka).|
| |  | Update from Probelab on gossipsub and control messages analysis, with related slides available on IPFS.|

---- 
## Agenda

### Electra 
### Devnet-2 and Devnet-3 status

**Alex Stokes** [1:44](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=104s): Okay and we should be live. Hey everybody this is Consensus Layer call 140. I put the agenda in the chat there and yeah there's quite a bit on the agenda today. Okay so let's go ahead and dive in   quickly just to kick things off. There was a Specs release version 150. This is Alpha 5. I think it's exclusively  things for peerDAS but yeah just a heads up there. And I believe this is the target for peerDAS Devnet 2. So might be relevant later in the call but just be aware and take a look if it's relevant to you. Cool so then let's jump into Electra. And if we could start with updates on  Devnet 2 that would be super nice. Looks like there might have been a bad block recently. 

**Paritosh** [2:51](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=171s): Yeah I can give an update on that. So if we go to if you guys are interested in more details please have a look at the interop channel on  ethR&D Discord. There's a few bad blocks we've noticed on the network. They seem to have been produced by geth. But are also not importable by geths. So we need to look into why I have a timeline there as to what I'm seeing at least please validate that and there's two threads right now. One for debugging the get bad block and two Erigon has forked off but each Erigon node seems to be on its own Fork. So there's also something going on there that needs debugging. But yeah we don't really have more than just a few open questions right now. And there's a link to the trace of both the specific bad block that has been posted earlier as well as in general which bad blocks we've seen on the network over the last like a day or so. 

**Alex Stokes** [3:54](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=234s): Okay. Awesome! Thanks, Pari. Yeah so please take a look. We can work on debugging that.

**Paritosh** [4:02](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=242s): I think that's it for me. Yeah mainly it's Marius looked in and he said it was likely 7702 even though we did not actively test that but yeah.

**Alex Stokes** [4:14](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=254s): Okay thanks. Yeah we'll take a look at that. Otherwise it seems like Devnet 2 is in a pretty good place. Yeah any other updates from anyone else on  Devnet 2 

**Paritosh** [4:33](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=273s): Oh yeah there's one more thing we noticed that's JSON RPC standardization issue. We tried making the eth call that we spoke about at the testing call and then after some debugging kind of found that the nethermind team uses a different default from than the Geth team. So when you send like a raw RPC call if you don't specify the from then you don't really get output in nethermind. It seems like an under specification of the JSON RPC right now. And there's a similar bug in besu where if you call debug Trace call. It complains that the gas price is less than the base fee. But if you send a regular eth call it works fine. So yeah, I guess the teams have already been notified. I think they're looking into it. But yeah if there's some update on that then please bring it up.


**Alex Stokes** [5:41](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=341s): Great! Okay good should we touch on  Devnet 3. I don't know if there's anything we really need to do. If 7702 is the issue with this  Devnet 2 bad block then yeah maybe that will just resolve naturally in  Devnet 3. Any 7702 updates worth discussing right Now? 

**Paritosh** [6:11](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=371s): Someone from the Reth team brought up if this EIP 2935 chain should go into the next Devnet or if there's still like an open discussion. So I wanted to bring it up here. It's been merged as an update. I think I'm more in favour of having it ready for Devnet 3 but yeah up for discussion. I guess I've posted it in chat.

**Alex Stokes** [6:36](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=396s): Thanks yeah anyone working on that can you chime in? As far as I understood, yeah there was something around the semantics to clarify. So I agree it would make sense to put into down three. I don't think it's a huge change or departure from what we had before. So sounds good to me.

**Lightclient** [7:05](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=425s): I mean what does what needs to be put into Devnet 3?

**Stokes** [7:09](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=429s): I think this PR, Pari, put. 

**Lightclient** [7:12](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=432s): Yeah PR shouldn't change anything. Okay there's no semantic change. It's just saying like you have to call the system contract to do the update. But I think everyone is doing that and you can still not call it if you want but like you have to make sure it's right. 

**Stokes** [7:36](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=456s): Right okay. So yeah let's just go ahead and assume this goes in  Devnet 3 but it should be transparent with the behavior we had. Cool anything on  Devnet 3 to talk about. I think we had said last week that we aim for two weeks so next week would be Devnet 3 launch. But it sounds like it's going pretty well. Not sure if there are any implementation updates or anything else to discuss there.


**Paritosh** [8:22](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=502s): Yeah I think once client teams have branches please just ping them on the interrop chat or DM either Barnabas or me and then we'll update configs and start sharing them around. And yeah Mario’s posted the spec release for Devnet 3 as well. So the EL specs.

### [EIP-7251:Update correlation penalty computation consensus-specs#3882](https://github.com/ethereum/consensus-specs/pull/3882)

**Stokes** [8:43](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=523s): Okay great! cool! Then next up we had let's see this was a PR to update the maxEB  EIP. Let me grab a link here. I'll put it in the chat. So  essentially yeah I believe this was only an issue sort of like an education maxEB where if there was a lot of eth staked say like more than 30 million. There was an issue with Consolidated validators essentially like validators with a lot of stake interacting with the calculation of the correlation penalty for slashing. And essentially there's an overflow with the way that we have the spec today and this PR fixes that. It looks like in a pretty nice way so let's see. I don't know if anyone like is Mikhail on the call? I don't see him. Hey, would you like to say anything else about this?

**Mikhail** [9:48](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=588s): Yeah just a quick overview of the problem and the fix as Alex mentioned. So this is the about the correlation penalty computation the parallel to that is apply in roughly 18 days after validators gets slashed. And actually the cause of the bug is in the inter division  and the result the outcome the potential outcome of the problem is quite U becomes much more severe with the max effective balance increase. So to highlight the problem we should consider two cases where the same balance. Say 2048ETH is distributed in the first case it is just one while  which has the all this eth on its effective balance and the other cases like 64 validators that has each of them has 32 eth and under some condition each of those 32 eth will get zero penalty. So the total penalty the total correlation penalty apply to this balance this entire balance will be zero for 32 eth validators but for 1 x  2048 while 2048 eth validators will it will be not zero so this is where we get the discrepancy and actually this  PR proposes fix to this problem. Also the other problem is the Overflow in the same computation but yeah it's the detail of the Overflow and this discrepancy and the amount of correlation penalty can be found in the description. So the fix basically changes a bit the correlation penalty curve. It makes it linearly dependent on the effect balance on the effective balance on the number of effective balance increments. So it's like 32, 2048 and the side effect of the fix is that  we'll get correl correlation penalty for even when the one validators gets  slashed but this penalty is going to be negligible in this case the detailed analysis is also in the post and you can take a look at this as well. So what else is here? Yeah the correlation penalty becomes bit higher on average but the curve is much more smoother than when I was with the before Electra computation so we can see it as well. And the total s penalty will anyway  go down and decrease with this in Electra because the initial penalties is significantly decreased. So for all these details you can just read the post. Yeah that's what this PR is about. I know Franchesco on the call and want to give more information.

**Francesco** [13:12](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=792s): No that's that yeah that's enough for me.

**Mikhail** [13:18](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=798s): Cool! so it would be great  for more eyes to take a look to this PR because it changed the penalty that we used to have for all the time and yeah but from our perspective the fix looks good. And I think we can. I think we just aiming to merge it sometime next week. Maybe if there is the desire we can wait till the next call and make the last call the next time.

**Stokes** [13:57](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=837s): Cool thanks! Yeah nice catch. This is a very important computation for slashing penalties. So please take a look. I looked the other day and yeah it seems equivalent to what we had say if we were working with like the real numbers. The issue kind of comes in when we move to like integer arithmetic that we use in the spec and then you start hitting different overflows and things and yeah so take a look. We'll probably at least I'd probably wait for like a few other client teams to chime in on the PR but but after that should be ready to Merge. Cool if that's it on that one we can go to the next agenda item. 


### Migrate execution requests out of ExecutionPayload in CL data type

**Stokes** [14:41](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=881s): So this one I think has had a bit of work put into it and essentially it's refactoring how the execution requests are put in the data type on the beacon chain. And the reason we want this is because the sort of natural thing to do is just mirror the EL here where the execution request would be and the execution payload in the beacon chain type. Generally I think all the clients  pretty aggressively prune these because there's no reason to have them duplicated both on CL and EL and so if you do this then you don't have access to these execution request which you now need for the CL State transition. So there was another proposal by Potuz. I think there's some back and forth and people have landed on this new PR here I just put in the chat. And yeah it looks generally pretty good to me yeah again call to take a look. I think there was still one thing we'll need to do is pass the request to the EL say in the new payload call that was missing but otherwise it looks pretty good. So  I'm not sure if any other client teams or anyone else has had a chance to look at this or if there are any questions about it at the moment. Yeah Potuz? 

**Potuz** [16:11](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=971s): Yeah so one of the reasons we well I guess you can ask the author but one of the reasons that this approach  turns out to be much simpler to write in the python spec than having an extra envelope. Than having an extra layer but the problem is still that you need to have like tests for this and pass the pythons test. Are we going to agree on like starting Implement that's going to take some time. So are we going to agree on like starting implementing this thing on clients before having test on the python spec or it's fine by me. I actually want this change so yeah.

**Stokes** [16:50](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1010s): I mean they can go in parallel but yeah I guess the sooner other client teams can take a look the better at the PR.

**Potuz** [17:05](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1025s): The PR looks good. It's just that the test. 

**Stokes** [17:09](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1029s): Right so yeah I mean it might be simpler to just move ahead with this PR just. So people have like a Target say if it gets into a Specs release test can come along the way. And yeah I guess it would be nice to have a few other client teams take a look at this PR before we go merging. Mikhail? 

**Mikhail** [17:31](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1051s): Okay I just wanted to add that this PR is nice because it does not actually does not introduce any changes to the execution payload struct on the CL. And also I think that I've been putting this comment into the PR thread but I think that we could remove the payload bodies version two request from engine API because CLs will not offload those request from their databases. But yeah that's what I was going to look for. I mean like the answers to this question whether this correct or not to ask scale. That's about it. Like yeah does it make sense to just not have those get payload bodies method in the description definition sorry. 

**Stokes** [18:32](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1112s): Would you not still need those say if you know someone ask their CL for a block and they need to go fetch the execution payload from the EL. Say for like a historical block. 

**Mikhail** [18:46](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1126s): Yes but we already have. So those version one methods that can serve transactions and withdrawals. So request will not be offloaded from the database yeah we don't need to update those.

**Stokes** [19:05](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1145s): Gotcha! Okay. I think you had a comment on the PR about that. So I can follow up there and yeah I can also look at test in the next week or two. So then my ask for client teams is to take a look at the PR. And we'll move ahead there. But yeah generally this makes sense. Okay anything else on that?

**Mikhail** [19:48](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1188s): By the way what does you mention tests what kind of tests do we need to merge this PR. 

**Potuz** [19:55](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1195s): Well the problem is that this change it's going to break essentially every test that we already have. So so fixing those test until those tests are fixed we're not going to have spect vectors to pass. So we need to fix the existing tests have a release with those tests that are going to be applicable for this PR. And then we can just run spec test in our CL ourselves so that's that's the that's just the the inconvenience of having this large change on the pyspec. 

**Mikhail** [20:26](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1226s): Got it so you mean that it's not about the pyspec tests right. 

**Potuz** [20:32](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1232s): Right so whatever we have now currently on spec test is going to start failing once we merge this in our in our develop branches.

**Mikhail** [20:40](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1240s): Yep I see. Thanks.

### Unify requests representation in the Engine API

**Stokes** [20:47](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1247s): Okay so we'll move to the next agenda item. This is related around the execution request and how they are written or represented in the engine API. So Lightclient had this PR. Lightclient do you want to give us any more additional context here? 

**Lightclient** [21:14](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1274s): Sure I think we talked about this a couple weeks ago but just bringing it back up for final call from CL devs. The idea is on the execution layer we don't make the distinction between requests in the block body. And so what we do is we just have this sort of Union like thing where we serialize the request with the type prefix this is the same thing that we do with the transaction types. I'm trying to expose that same type of that same data type to the engine API instead of what we're doing right now which is during the engine API call. We have to actually go in and parse out each individual request type from the list of requests. So really it's just trying to have better parity of the API versus like the data that exists. There are a couple issues with how it is formatted I think like if we were to add more request types in future Forks it won't be so easy for us to parse it out. It's still possible and if this is like a blocker for CLs like we can do it but I think that it's better for the API to match the data type that exists in the block. Yeah if anyone has thoughts on that like happy to hear it. Otherwise probably merge it later this week. 

**Dustin** [22:42](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1362s): Yeah I think some of the issues there have not been addressed in that GitHub issue  And I would personally say I agree with at least one of them. So, for example, this SSZ question, and I think it is going to be useful to be able to have a an SSZ representation of this in the hopefully not too distant future. I think there's been a some consensus although there's been not on timing from the ELs but there's been some consensus that SSZ is probably a good direction to go with representing data in ethereum in general. EL and CL there's been some enthusiasm whenever it's been brought up toward moving towards that direction again. Yes not everybody's ready with their SSZ libraries and Etc but and we have to time that for in other ways. But this would actively make that more challenging and to just kind of toss in well maybe use an SSZ Union is not sufficient because SSZ they are not used they effectively don't exist they don't exist in all libraries. They should not be relied upon. And as such I there is no corresponding representation of this in SSZ currently. So that's I'll stop there for the moment but that's one of the issues that the



**Lightclient** [24:20](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1460s): I mean this is just not an SSZ API though. Like we not only do we have one solution which is the SSZ spec that says there are unions. So if you want to go down the right path we have that and if people don't want to implement SSZ unions. Then we could just revert back to what exists today which is separating them out and setting them over as individual list. Just because we're changing how the JSON RPC is representing this today does not really affect how people want to represent it with SSZ. 

**Dustin** [24:54](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1494s): Well it does to an
Extent. 

**Lightclient** [25:02](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1502s): I mean you can like when we do this in SSZ like you're going to come up with your own SSZ spec for how things are represented? So it's like up to the SSZ designers at that point to decide how do they want to represent it. If they want to represent it as a union like I think it's the best thing to do but if they that's not  possible. Then we could do exactly how it's represented today.

**Dustin** [25:25](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1525s): So generally speaking the way these SSZ transitions have been mapped out not universally and various other people here have been involved in some of them. So and is that they are structurally isomorphic maybe is how I'll put it that not universally but in general. There's often a goal to have them be closely equivalent structurally. So they are just the same kind of information hierarchy but with a different encoding. Rather than saying that they are just a complete reimagining of the API. And if you look for example at the beacon API which has offers SSZ. I know this not EL related but this shows a model for how this has been worked out. The SSZ representations are as close as possible this is not a different API. It's the same API over SSZ. And this so I this does impinge therefore on how SSZ would represent it and again union doesn't effectively exist right now.

**Lightclient** [26:40](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1600s): I mean I just don't agree. So that's just why I don't think that this is an outstanding problem. I understand this maybe you guys do. But I don't think that something that we might do in the next one year should impact like what we're doing right now when it like like can it easily be changed in the future if we need to.

**Stokes** [27:03](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1623s): Have other CL teams had a chance to look at this PR? Yeah Potuz?

**Potuz** [27:18](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1638s): I looked at it but personally I can't speak for Prysm. It sounds like something reasonable. I also think that it's easy to change if you want to change that representation later. So I agree with Matt. Although Etan left a comment in that PR that it's also reasonable to me either way works for me they both look like reasonable changes. So that's why I'm asking Matt in chat what he thinks about that comment we just concatenating the Merkle-Patricia Tries roots of the three requests and then hash them and use
That.

**Lightclient** [27:56](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1676s): Yeah I mean it's not a bad idea in General I just prefer to keep things the same when we have mechanisms that look the same. And the reason is that every time that we make a small deviation in an implementation then that just creates a lot more complexity right now the way that it's implemented is exactly how transactions are serialized and merklized. So we get to reuse all of that tooling if we change that then we need to like write more code around that and then it's kind of starts to defeat the purpose a bit. So I think like the way that it's written is simplest and I think it's like the most maintainable for the long term because if you have to understand the Tx root then you get to understand the request roots for free you don't have to go and learn how this other mechanism works.

**Potuz** [28:46](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1726s): So my understanding of this is that the it is actively simpler for you guys to implement your suggestion. And for us it's a very simple change because it's just extracting out that quantity that we don't care the type and just use the right sterilisation to match it into our internal object. So it's very simple change for us as well. I don't see why not to include this now.

**Stokes** [29:14](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1754s): Yeah personally I lean towards merging just because it sounds like it simplifies implementation on the EL. And especially given the uncertainty around SSZ and like how It ultimately looks like  it just sounds like something to
figure out down the line.

**Dustin** [29:31](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1771s): I'm not sure that the comparison to transactions is. I mean I understand from a EL perspective that they may well be represented similarly and or similar structure. Let's say of distinguishing types from each other they that is relatively speaking compared to most of the CL data structure is kind of a let's say from a little bit from the outside and  unmaintainable mess. It has problems and the fact that and so importing that into the CL World which has mostly avoided these problems. I'm not sure is a positive step.

**Lightclient** [30:15](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1815s): Yeah I wasn't really commenting on how it's represented on the CL. I'm talking about on the EL. Like we have these roots that exist in the execution layer header and I'm trying to keep those in sync with each other rather than having every single root means something like slightly different. The way it's represented on the beacon chain is like totally up to the consensus Layer teams. 

**Potuz** [30:53](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1853s): This doesn't change how we represent these things? I mean our internal structure doesn't change at all this just changes how we deserialize over the engine API we just grab this thing grab the quantity. Say ah this has to be deserialized as a request for for withdrawals and then this other thing needs to be deserialized as some deposits but we don't change the SSZ type of these things internally. We don't change the consensus layer python types. We don't change anything so that's why it's very simple change for us if it makes the EL happier why not? 


**Dustin** [31:37](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1897s): And I do see your complaint about the future SSZ but then in that case we can just change the API. It's not it's not a hard fork so if it bugs us when we move to SSZ on both layers then we could just change this again.

## PeerDAS 
**Stokes** [31:58](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1918s): Right so again yeah I think this makes sense and it would simplify implementation. So I would say Let's Do It. Maybe we'll let it sit for another week and I'll try to get another client team or two to take a look and we can go from there. Is that reasonable to everyone? Okay I’ll assume that's yes. Thanks okay so that was all we had I believe for Electra. Any final comments on Electra otherwise we'll move to peerDAS. Okay cool. So first I was just curious if anyone wants to give any implementation updates? I know clients have been working in parallel on peerDAS Devnets. Anything worth discussing there any questions anyone has or anything like that? 

**Barnabas** [33:08](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=1988s): Yeah our goal to launch Devnet 2 peerDAS Devnet 2. Hopefully tomorrow if we will have enough clients to participate. So currently I have done some local test with Prysm, Lighthouse and Nimbus. Prysm and Lighthouse seem to be working fine. Nimbus have some awesome block proposal issue but it's being investigated right now. I'm interested to hear from Teku and Loadstar possibly they have an update.

**Gajinder** [33:48](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2028s): For Loadstar I think it should be ready. I'm not sure. Are there any issues that you're saying Barnabas.

**Barnabas** [33:59](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2029s): I haven't tested yet with Loadstar just I haven't heard anything either that it would be ready to go or not. 

**Gajinder** [34:07](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2047s): So basically with meta deta V3 included I think  you can test it out.

**Stokes** [34:25](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2065s): Cool!  Anyone from Teku on the call here who can speak to peerDAS. 

**Anton Nashatyrev** [34:32](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2072s): Yeah from Teku side we also have metaData V3. Yeah I think we are ready to participate.


**Stokes** [34:50](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2090s): Cool! Thanks and there was a question Loadstar is this the peerDAS branch? Is that the right one to be targeting and similar question for teku? 

**Gajinder** [35:01](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2101s): Yep that's the Branch.


**Anton Nashatyrev** [35:05](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2105s): Yeah we also have Branch the same Branch as before.

**Barnabas** [35:11](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2111s): One more question  can Loadstar now be super node or that's still not implemented

**Anton Nashatyrev** [35:18](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2118s): You mean  subscribed? I mean you like cust in every all subnets?

**Barnabas** [35:27](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2127s): Yes.

**Anton Nashatyrev** [35:28](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2128s):  Yeah I think.

**Barnabas** [35:31](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2131s): For Teku it is but for Loadstar we didn't have it for loadstar last time. 

**Gajinder** [35:36](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2136s): Loadstar can also be the Super node and I think I posted the param that you will need to supply to make it a super node.

**Barnabas** [35:47](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2147s): Okay.


### Blob uncoupling b/t EL and CL: EIP-7742 -- Pectra inclusion?

**Stokes** [35:54](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2154s): Okay sounds good. So next up  I wanted to follow up with some questions around the blobs. So the first one is there was some work to think about uncoupling the blob counts between the EL and CL. So right now basically there's like a Target and max value and the max at least is like hardcoded both on CL and EL. And you could imagine that it streamlines development. And just generally you know ops around this stuff if we uncouple them to the extent possible. So I've been working on some stuff recently and it has culminated in an EIP to suggest this chang. This is EIP 7742. I can go grab some links but yeah generally. Oh thanks. I think Justin put this. Yeah so Justin put the CL PR here. There's now this EIP 7742 and then just the other day I started on engine API changes. So that's all here. And yeah I think there's generally pretty broad support to go ahead and include these. Yeah I guess that's the question now I'd suggest we put these into Pectra and curious what people think about that. Mikhail?

**Mikhail** [37:21](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2241s): I have a couple of questions a couple of clarifications. So the first one is the do we need to pass the Max blob count to to payload  attributes as well? 

**Stokes** [37:38](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2258s): I think not. So right the EL just needs the target for the fee accounting and really how it is right now is the max is like kind of redundant on the EL. So this EIP let's say these three PRs they kind of just take the max away from the EL and all it does is pass the target. 

**Mikhail** [38:01](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2281s): But if EL will include more than the max value on the CL then.

**Stokes** [38:10](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2290s): Right but the the CL will validate so like before the EL sees it the CL handles that check.

**Mikhail** [38:19](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2299s): Right but then EL should know that it should not include more than the max value more transactions more block transactions and so that the max. 

**Stokes** [38:30](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2310s): I see yeah. Okay.Yeah that probably you.

**Lightclient** [38:36](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2316s): Either need the max or you need the EL to just like have hardcoded a percentage of the max. So you could say that will just like quote unquote always Target the Target being half of the max. If you want fancy stuff like Barnabas is saying then I do think you need to be passing at both
Target and the max to the EL.

**Barnabas** [38:58](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2338s): I think in the future it would be better to have both of them F because  we might want to do something like with higher blob numbers we might want to  change the Target only but keep the max at a higher level.

**Stokes** [39:17](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2357s): Right and I was kind of the thinking with this as well is just to give us that flexibility.

**Barnabas** [39:22](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2362s): Yeah I mean if you're already changing it we might as well pass both of them. That’s my take. 

**Stokes** [39:28](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2368s): All right okay so yeah I can update that.

**Mikhail** [39:33](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2373s): Yeah it makes sense to me as well. And the other question is about Target block count so the target block count will pass through payload attributes to the  payload build process. So the EL will be able to compute the excess Blob gas right or excess  blob count. Right yeah but in this case the kind of the target blob count is required to validate the EL block. So in order to not break the optimistic sync the target blob count will need to be to become a part of the execution layer block.

**Stokes** [40:19](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2419s): Right so there’s EIP put that value into the header.

**Mikhail** [40:25](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2425s): Okay so there is the target block count in the EL block header. Right Oh I see okay interesting. Okay got it I just probably missed this this part so good. 

**Stokes** [40:47](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2447s): Yeah no worries, cool. So yeah I guess then everyone take a look. Do we want to talk about pectra inclusion or should we wait until these changes are more in a final state. It would be good to get a  temperature check now. We have one thumbs up in the chat. Anyone against including this in pectra? This should simplify development and I think already the PeerDAS implementers are moving to rebase PeerDAS onto Electra and soon. So I think this makes a lot of sense. Yeah we got another plus.


**Mikhail** [41:58](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2518s): Just a quick followup question. Can we just pass the excess block count from CL or not. I mean like it's already in the block probably the target is not that meaningful for EL if the excess will be passed which was computed by CL. So we would not need probably to add one more field to the EL block.

**Stokes** [42:23](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2543s): Right yeah that could be a good compromise. It kind of gets so Dankrad had another proposal that basically hoist like the entire computation into the CL. And I think we kind of stood away from that just because to the extent we can it's nice to have the separation of concerns between CL and EL where the CL more needs to think about just you know dust concerns and things like that around the Max and then the EL primarily just needs to know yeah excess in some sense for the fee accounting. So  that's kind of why we settled on this but it could be yeah I'll think about this some more it could be an option to pass the Excess around rather than pass both Max and Target like we were just discussing. Okay so yeah there's an update then for me to make on that and generally it sounds like people aren't bored with including so I'll bring this back to the next CL call. And yeah we'll go from there. Cool so the next thing yeah the so all needs some help from the client teams but from what I've been hearing it sounds like some implementations essentially have these Blob parameters hard coded. So for example if we wanted to iterate on a you know even very Ephemeral  Devnet with changing these values. It would mean a recompile of the client. So I'm not sure if anyone here has anything to add to that generally we would like these to be configurable. So it's you know very simply just to change very simple just to change some configuration and not need to recompile the entire client if we change blob Counts. Does anyone here I don't know. Barnabas? I think you raised this point. I'm not sure if you know if there are particular clients that had this issue.

**Barnabas** [44:33](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2673s): I think it was something to with the c KCZ library. Where some of the blob values were hardcoded but I'm not 100% sure anymore. We haven't been playing around with the variable number of blobs yet  so yeah.

**Sean** [44:52](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2692s): I think we would have had issue in Lighthouse. Puan is working on going through and making it easier to runtime configure blob
count right now so we're trying to fix that.

**Stokes** [45:12](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2712s): Okay cool. So yeah I guess then just a general notice for everyone to the extent that it is runtime configurable. That's much much simpler than the alternative. So please be aware of that and yeah I guess we can just follow up on that asynchronously. Pari was asking if Geth had this issue as well. Yeah Barnabas?

**Barnabas** [45:38](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2738s): Yeah one more question. So right now we have  the max blob limit in the config as a value that you can set but we don't have Target on the CL side. So maybe we can also add that. So we can independently configure both of the values.

**Stokes** [45:59](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2759s): All right yeah that's a good point yeah Lightclient or I don't know if anyone else from Geth is here? Can we speak to this question?

**Lightclient** [46:15](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2775s): Sorry, can you repeat the question?

**Stokes** [46:18](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2778s): Just how easy is it to change the block parameters in Geth? Pari was asking he thought there was an issue in Geth as well to change the parameters for a hard fork or to change the parameters like on demand via the engine API. 

**Stokes** [46:34](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2794s): Well just so like if you build gas those numbers are fixed and then the question is do I need to change the source code to change them in gas and rebuild the client or can I just pass some configuration.

**Lightclient** [46:47](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2807s): Yeah you have to change the source code right now.

**Stokes** [46:50](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2810s): Okay are there
plans to update that? 

**Lightclient** [46:56](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2816s): I mean no but we'll change it when it needs to be changed if there needs to be plans we can make them. I have a PR for the 7743. So that would make it configurable by the engine API if we want it configurable by Genesis like that's something that we can also look into but I think that's going to be a little bit weirder because you need to specify it for like multiple Forks. 

**Paritosh** [47:26](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2846s): I think by engine API makes more sense. If that's the approach we're going with anyway we can configure it on the CL and the CL passes it through to the EL.

**Marius** [47:42](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2862s): Great when we get blocks from the network we don't know how to how to test this right. We don't know how to verify that we have enough blocks.

**Paritosh** [47:54](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2874s): I think that was the same question also for sync right because even if you're syncing. You kind of need to know how many blobs should have been there for the estimation. 


**Marius** [48:05](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2885s): Yeah I think we can only change the set hard Fork boundaries anyway. So I would make it dependent on the hard fork. 


**Paritosh** [48:16](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2896s): Or we put it in the header.

**Marius** [48:37](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2917s): Not more Fields into the headers please.

**Stokes** [48:41](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2921s): Okay he's saying no more stuff in the header right. Okay so we might need to do a little more designer on this. But yeah this has been good feedback and I think we can take it from here. 

**Marius** [48:59](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2939s): While we added one thing I would really like is if we could have a limit on Max blobs per transaction. So that we don't have like one transaction sending six blobs or like the maximum amount of blobs per block. And this was would make also our lives transaction pool and everywhere easier. Because right now someone
could just like always send six blops transactions and either they will get included or they won't and then no one else. So yeah. 

**Stokes** [49:42](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=2982s): Right okay so I mean there's some chat content around just saying one blob one transaction having that be the limit or otherwise it sounds like maybe we just want a fixed whatever the maximum is we just say like that is the actual limit with respect to a single transaction because I think with 4844 right now. It's just not specified Asgar?

**Ansgar** [50:06](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=3006s): Yeah I would personally relatively strongly oppose enforcing such a limit on the protocol level. Just because it seems like there's no strong reason for it. And it just removes a lot of flexibility in the future because it's really hard to predict these usage patterns once we go to this like larger blob counts. I do think though because I've been hearing that quite a bit that like it causes problems on the mempool side. So I think it's perfectly reasonable for the EL clients to just coordinate on a maximum to enforce in the mempool and just ignore all transactions above that maximum that way to pace can choose like if they have a specific way to just reach Builders directly or something they can always just like send transactions with higher accounts but the public mempool is basically just open for transactions up to certain size to me. That seems like a much more sensible minimally restrictive approach.


**Marius** [51:07](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=3067s): In generally I don't like this pattern of having some transactions or most of the transactions valid by the public mempool
 but some transactions not. And so we need to go those people need to go through the builders. I just a general comment I don't I don't really like this pattern this in shines the builders way too much gives them a lot of power.

**Ansgar** [51:41](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=3101s): But it's it's not just about kind of like  private ways to reach build
or something it also just like the protocol should only ever enforce rules that physically unnecessary because say in the future the men pool we have a somewhat more efficient implementation of the pool and then we can go from I don't know maximum of three to maximum of eight or something once we have higher kind of maximums in general. In that scenario it would just be really unfortunate to have to wait for a year for a Hard Fork because if that limit is just not enforced in the protocol we can always just change the implementation in on the mempool side whenever we want but enforcing it on the mempool just significantly restricts our design space or if say an individual client wants to have like a higher limit or something thing. It just to me seems like way too heavy-handed to enforce
it yeah.

**Stokes** [52:38](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=3158s): So the max would be whatever the protocol level Max is right. So it's not that we would say like I mean unless we
wanted to really restrict transactions to say like one blob or something. 

**Ansgar** [52:54](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=3174s): Wait that's my proposal. Marius proposal to restrict per transaction on to something that's much much smaller than the block Maps potentially all the way down to one. 

**Marius** [53:08](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=3188s): Yeah I don't want to take it down to one. But the problem is when you're fetching these transactions and you fetch a blob transaction and you don't really know yet how big it is and then it arrives with like eight blobs that's like I don't know how big that is but it's way bigger than than a block transactions with like two or three blobs. So yeah I don't know.

**Dankrad Feist** [53:41](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=3221s): That can be fix just by fixing the network protocol and announcing how many blops it has right. 

**Marius** [53:49](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=3229s): Yeah could be.

**Dankrad** [53:56](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=3236s): Because as vector exists anyway. I can always send you pretend that I have a huge like transaction send you like megabytes of data. 

**Marius** [54:05](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=3245s): But then you're violating the protocol and we can kick you.

**Dankrad** [54:11](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=3251s): Well you can do the same for this you can also say like right now it's the valuation of the network protocol more than k transactions k blocks like you're still free to do that that's independent of what allow in consensus. Like basically you're trying to use consensus to define a rule for this but like that rule can also exist on the networking layer. 

**Stokes** [54:47](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=3287s): Potus, do you have a comment?

**Potuz** [54:51](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=3291s): Yeah I'm not sure how relevant it is. But  I would ask for input on rollups of about imposing a limit a say of one blob per transaction. I saw francesco's  comment that amortization eventually that's it. But this might actually benefit some rollups over others like rollups that are posting blobs without execution versus rollups that are posting blobs with like expensive execution in the same transaction would see a different benefit into having a limit of one blob versus six blobs. And depending on what's the price of call data. This might actually make a big difference so I would ask them for input on this matter.

**Marius** [55:38](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=3338s): I'm not just to be clear I'm not advocating for a limit of one blob per transaction. What I also see is that if we had some rule about this that you cannot like that one rollup cannot fill up a block full of blobs with one transaction.  I think it might actually be more competitive because and then you cannot just fill up the blank space to be sure that your transactions go in and the others don't. I don't know.

**Dankrad** [56:22](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=3382s): I mean you can always just create 2 transactions with 3 blocks and like use build to get those in a sample like right now you can send panel and they will get in atomic you. So this only makes a difference for self blocks anyway.

**Stokes** [57:03](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=3423s): Okay yeah. Thanks for the discussion everyone. Sounds like Dankrad to keep pushing on. And otherwise let's see I had the agenda somewhere what was next. Right okay so that was all we had on PeerDAS for today. Yeah any other closing comments on the blobs or PeerDAS or anything? Okay I will just call out Etan's comment here. Let's see there are some updates for stable containers. Let me just check this out now. There's a couple things in here. There was this PR here. So I think that this is generally informational or at least rather it's not like a critical issue to fix at the moment but please take a look at this PR. There was something with the engine API and around transaction serialisation. So everyone take a look at that and what else was in here. Updates for stable container and yeah I think that's generally it. Cool so we had that to follow up with and right. 

### Research, spec, etc.
#### F-star name

Next up I did want to Circle back to the name of the f-star and I'll just grab this eth magicians link here. But ultimately after you know some Community input both well from many different people looks like there was some support around fulu and you know we could call the combined name between the portmanteau Fosaka. So yeah I think it'd be nice to go ahead and pick a name for the f-star. Anyone opposed to moving ahead with fulu?  Barnabas says fusaka rather than fosaka. We got another fusaka. Okay so yeah let's move ahead with Fulu then and yeah fusaka is a perfectly fine portamenteau. Cool so that was that and then I think the last thing to touch on today would be an update from probelab. I think around some work on Gossip sub. Let's see someone here from probelab on the call.

**Cortze** [1:00:19](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=3619s): Yep I'm here. Can you hear me? Do you mind if I share my screen? I have some slides prepared. Do you know if the action is limited is it not letting you share your screen. I'm not able to find the option. Yeah so mostly what I was going to do is make a small introduction of a report we did on the performance of gossip sub at probelab in collaboration with the  ethereum foundation. My colleague Guillaume did previous update on The Last Call on the Discovery 5 status. And this one was going to be on the gossip sub one. The main idea was also to prepare the tool that we build to generate this data which is called Herms which basically acts on the network as a light network node which has like a custom P2P Tracer. With light Network note I don't mean like this is like a light consensus client it's mostly like a networking  node who supports all the protocols. Let's say Discovery 5 gossipsub and all the P2P protocols like pinich chains metadata chains. All these ones and the interesting thing is that it's generate plag with a trusted prysm node which allow us to reply any chain status that someone is asking us in an honest way. So that we keep honest connections and stable connections. This is the biggest let's say change if we compare it to other tools that are out there that pretty much do the same thing and the final purpose is that we want to reproduce the stability of any node that it's out there in the wild. What do we do with this? Basically this custom lip2 Tracer it's streaming all kind of bents at the lip top host level. Let's say connection  disconnections send and receive RPCs but also at the gossipsub level. So we have  we have control and we Trace down all the control messages that are happening at the gossipsub level. Let's say craft that pruns at any mess that we are subscribed to on all topics. Subscriptions to these messages control I have and I wants internal PS scores and also like message arrivals to each of these topics. And there is some extensions towards ethereum field where we are able also to trace down request response on Beacon status metadata chains so on so on. I don't want to take much of your time but the idea was I had some slides with some graphs and the idea was mostly to introduce like some of the outcomes that we presented previously in some eth research posts. I'll try to make sure I share on the GitHub issue at least the link to the slide. So that anyone that is interested could check it but something that we were really excited about was that we were able to retrieve the gossipsub Effectiveness. This means how many I on do we send or receive based on the ones that we send or we receive. Sorry my voice is going over but something that we identified is that this radio of I on we send or receive per all that we send or receive. It's pretty low which isn't bad per se but it shows that the network is healthy enough to the point that we might be spending a lot of bandwidth on control messages and this was something that was pretty much a stable for all the topics except for the blocks which had like certain spikes where we could see radius of 600 messages per each I one that we were sending or receiving. There was also like further interest on researching duplicates. This was a pretty well-known issue but there was no public data on it and this is something that we were consciously  analyzing. And what we realized is that of course the bigger the message size the bigger the number of duplicates that we received but something that we  were able to trace them with all these traces was that the time between the first original arrival and the first duplicate on a mean basis at least for blocks. It was around 80 milliseconds going up to a full second in some occasions which means that for example the we were pushing a lot  towards a protocol upgrade towards I want I don't want. Because we understand that the time games that it's or that are involved on ethereum allow us to pretty much send I don't one messages and try to avoid all these extra bandwisth that we are using. Because right now all the message that we are sending and receiving represent around 64% of the total bandwidth. And if we are able to reduce the duplicates from a let's say a million of three four messages per each unique message ID. We were saving like a huge band with holy and yeah I have a band of links and interesting outcomes that we came up from this study. Some of them were related to the Java virtual machine implementation where we were able to identify that. They weren't implemented the control messages especially the I haves on the same way as the other on were doing. Which mostly were making them not taking full advantage of gossips at all. And furthermore we also push a little bit more  towards the one or two version of Gossipsub to be only a scope to the I don't want message inclusion. And this is pretty much the the update that I have for you. I'm sorry that my voice is pretty much stress like with all these AC's it's pretty much over and that I couldn't really share the slides but I will make sure I make them a PDF and I will share them on the issue for anyone that is interested. Something that we are also taking care at the moment which is a little bit on work in progress is that we were also analyzing the block arrival time and we are about to make this on an automated way in our website. So I would like to share the link with you here in the chat. Feel free to drop any question that you have out there. Any feedback there are possibly new collaboration with the foundation towards PeerDAS. So yeah happy to reply any question if I can. 

**Stokes** [1:09:33](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=4173s): Great thanks. Yeah, now super exciting. I think that from what I hear your analysis kind of correlates with other analyses people have done around this. So super good to see some confirmations and just more data. Yeah if you have any links we should take a look at  you can put them in the chat or otherwise yeah just follow up on the GitHub issue. 

**Cortze** [1:10:05](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=4205s): Thank you very much. 

**Stokes** [1:10:07](https://www.youtube.com/watch?v=hSNJ6vURfmE&t=4207s): Yeah thank you. Okay so yeah we'll be looking for any links there on the issue for the analysis. And otherwise I think that was pretty much it for the agenda today. I don't know if anyone has any other topics they'd like to discuss. We could Circle back to the blobs if there is more to discuss there. Okay well then that's it for the day. Thanks everyone and I'll see you next time. Thank you bye.

___

## Attendees

* Stokes						
* Mikhail Kalinin
* Marius
* Cortze
* Paritosh
* Francesco
* Tomasz Stanczak
* 0xTylerHolmes
* Mark Mackey
* Barnabas
* Ansgar Dietrichs
* SauliusGrigaitis
* NC
* Justin Traglia
* Carl Beekhuizen
* Toni Wahrstaetter
* Tim Beiko
* Ignacio
* Pedromiranda
* Hasio-Wei Wang
* Terence
* Dancertopz
* Katya Riazantseva
* Dustin
* Mario Vega
* Sean
* Gajinder
* Scorbasjjo
* Phil
* Pooja Ranjan
* Pop
* Anton Nashatyrev
* Ahmad
* Preston Van Loon
* Dankrad Feist
* Echo
* Joshua Rudolf
* Lightclient
* Hadrien Croubois
* Ben Adams
* Kev
* Potuz
* Matt Nelson
* Anders Holmbjerg Kristiansen
* Lukasz Rozmej

---

## Next meeting:  Thursday 2024/9/5 at 14:00 UTC
--- 
## Reference Links: 
1. https://github.com/ethereum/pm/issues/1129
2. https://github.com/ethereum/EIPs/pull/8816
3. Tests for devnet-3 here: https://github.com/ethereum/execution-spec-tests/releases/tag/pectra-devnet-3%40v1.0.0 
4. https://github.com/ethereum/consensus-specs/pull/3882
5. Updated spec sheet for devnet-3: https://notes.ethereum.org/@ethpandaops/pectra-devnet-3
6. https://github.com/ethereum/consensus-specs/pull/3875
7. https://github.com/ethereum/execution-apis/pull/565 
8. Justin Traglia:  https://github.com/ethereum/consensus-specs/pull/3800
9. Alex Stokes: https://eips.ethereum.org/EIPS/eip-7742
10. Alex Stokes: https://github.com/ethereum/execution-apis/pull/574
11. Cortze: https://probelab.io/ethereum/block_arrival/2024-29/


