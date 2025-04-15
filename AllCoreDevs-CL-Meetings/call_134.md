# Consensus Layer Meeting 134 [2024-5-30]
### Meeting Date/Time: Thursday 2024/5/30 at 14:00 UTC
### Meeting Duration: 95 Mins
#### Moderator: Alex Stokes
###  [GitHub Agenda](https://github.com/ethereum/pm/issues/1050)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=Lrk99mKiWaU) 
### Meeting Notes: Meenakshi Singh
____

| S No | Agenda | Summary |
| -------- | -------- | -------- |
|134.1| EIP 7549 and Attestation Behavior:| During the launch of Pectra on Devnet 0, client teams decided to keep attestation behavior impacted by EIP 7549 unchanged during hard fork activation.|
| | | Developers considered various options to prevent a large number of invalid attestations due to EIP 7549 during the fork.|
| | | They chose to activate EIP 7549 on the same epoch as other Pectra EIPs without altering attestation behavior before or after the fork.|
|134.2| EIP 7251 and Staked ETH Consolidations:| Uncertainty remains regarding whether staked ETH consolidations should be triggerable from the execution layer (EL).|
| | | Implementing this feature would benefit staking pools allowing stake consolidations through smart contracts rather than relying on node operators.|
| | | Planned to monitor progress on client implementations for validator stake consolidation and decide whether EL or CL operations are appropriate.|
|134.3 | Validator Deposit Finalization under EIP 6110: | Open questions persist regarding validator deposit finalization.|
| | | Teku developer Mikhail Kalinin outlined the path forward in a GitHub comment.| 
||| Sean raised a version control question related to the “GetPayloadBodies” request in the Engine API. |
| | | Developers asked to share their thoughts in the GitHub pull request addressing this issue. |
|134.4| EIP 7549 Implementation Adjustment:| Etan Kissling proposed a minor change to the implementation of EIP 7549.|
 | | | The change aims to improve stability for generalized indexes. |
| | | By moving a new field to the end of a container, it avoids issues with proofs based on EIP 4788 in the execution layer (EL) and reduces confusion. |

________

## Agenda

### Electra
### Devnet-0, interop recap

**Alex Stokes**[4:30](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=270s):  Good  morning everyone. So there's the agenda this is consensus layer call 134 and yeah we have quite a bit to talk about with Electra. So let's just go ahead and dive into it. The first thing is just to recap Devnet 0 and all the things that interop. So maybe just to get started we had an open question with EIP 7549 essentially how to handle attestations at the fork boundary and after discussions with the various client teams we just decided to keep that as is. So that was pretty easy. Let's see next up we can go ahead and move to EIP 7251. So this is MaxEB and yeah I mean I think generally things went pretty well. You know there was a Devnet 0. I think all the CL client teams joined and they went pretty well. Given it was the first Devnet. That being said, yeah there were a few things to consider with maxEB. One of them being consolidations. So we kind of said originally we were going to aim for EL consolidations. I don't know if anyone has thought any more about this or how we want to handle this. I think later on the call. We'll discuss Fork scoping and I think some people have even suggested taking consolidations out. Obviously that makes the feature a little bit less useful. but that's an option on the table. Yeah does anyone have any thoughts here on this one just having EL triggered consolidations. 

**ef Office** [7:22](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=442s): I think sorry. I think Lighthouse had some Alpha implementation that Mark was hacking on. I think he had a fork that had an API as well. But I'm not sure if anyone else tried tackling consolidations.

**Sean** [7:41](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=461s): Yeah I'm not sure Mark's status on it but I know he did like a point of applications to see whether they prefer EL or CL triggered consolidations and it was definitely support for EL. And yeah I think we should include if we can. 

**Stokes**[8:08](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=488s): Okay. Sounds good. So I don't know if we want to aim for Devnet 1 for that or something later but yeah let's just keep that in mind. 

**Mikhail Kalinin**[8:18](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=498s): I can briefly provide the status from the EL side. So we have the smart contract for trigger consolidations Works. One question kind of the next natural step would be to outline the ELs pack for them and before doing this I'd like us to come through the proposal of treating EL trigger request as a sidecar to make a decision here because it can affect this pack of this thing on the EL side. So this kind of an an agree critical path to outline in this spec for EL triggered consolidations. And for consolidations in general I think that it was a great that we want them and we want them trigger it from EL.  

**Stokes**[9:20](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=560s): Yeah. Sounds good. 

**Ef Office**[9:26](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=566s): Does someone have maybe an overview on how complicated the EL triggered consolidations would be from I don't know from a CL or EL implementation perspective.


**Sean**[9:56](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=596s): Like so I haven't worked directly on it but I think it's about as like it's very similar to any other EL triggered operation. So since we already have like an idea of how to do this it's not really that much extra work.

**Stokes**[10:15](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=615s): All right. So we'll need the logic for consolidations either way assuming we have the feature and then the source if it's EL or CL doesn't make too much difference. I think if anything EL is simpler. Okay so let's move on to something else then sounds like we're pretty much in agreement there the next thing just to round up some of the devnet 0 stuff was this let's see. So there was a question around handling deposit finalization with EIP 6110. Let's see if I can grab the link to this comment here again there were like various conversations at interop and Mikhail summarized. I think generally the path forward here. And this comment I just linked in the chat. So yeah update is just generally we move forward on that some and you can check out the comment for the details. So from there let's see the other stuff is going to be additions to Electra was there any other Devnet 0 things or stuff from the interop that people wanted to bring up kind of around the existing stuff. 

**Sean**[11:53](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=713s): Yeah I actually had something it was related to the get payload bodies requests in the execution engine API. So the V1 and V2 versions of these are both fully backwards compatible. So I was thinking we might as well just extend the V1 rather than adding V2. Yeah just a thought.

**Stokes**[12:27](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=747s): Is that in line with how we usually handle this I'd have to go look at the comment to say more. 

**Sean**[12:36](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=756s): Well so with this particular endpoint we use it during sync and the like types we're getting are going to change at forks. And be better not to like switch at boundaries. So I think that's why it's specified as fully backwards compatible with other endpoints think we usually do actually Incremented the version as the type changes. So it's kind of different in that sense I guess from my point of view though like if this one's specified as backwards compatible. We might as well not increment the version.

**Mikhail Kalinin**[13:20](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=800s): Yeah so adding a bit the context on this we usually bump the version as Sean said and makes sense because usually either the new fork and the New Logic should be applied. The New Logic is implemented by this new version or the structure. Yeah it's just yeah it's just mostly about the fork but with this method it's kind of fork agnostic and used as Sean mentioned already. So it's we can actually we could bump the version. We could add a new structure but the structure would have a couple or three more or three more new Fields that will just be set to no for those blocks that do not have withdrawal requests for instance. so probably just be easier to keep the same version and just extend the structure.

	
**Stokes**[14:31](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=871s): Yeah that makes sense. Great if everyone would take a look just go ahead and chime in on the I think this is a PR there yeah 545 in execution API repo. Okay so from there there were a number of agenda items raised.  For Electra essentially either changing the EIPs we have yeah and even some new Ones. So let's just start with the ones that were changing the existing included EIPs. So first up we have this PR here it's 3768 in the consensus specs and essentially it's just changing the order of the fields of the new committee Bits. So let's see I think who raise this Etan. I don't know if  Etans's on the call? Cool do you want to give some just a quick overview?

**Etan**[15:36](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=936s): Yeah it's about stability for generalized Indexes. So when we add a new field in the middle of a container it means that the subsequent Fields get assigned a new index which breaks proofs based on EIP 4788 in the EL and it's also a bit misleading the way how committee bits originally were placed before the signature it sort of suggests that the Signature Signs over them but that's not the case the signature in the attestation only signs over data. So that's why I suggested to move the new field to the end to avoid both of these problems and there is also a comment in the same PR that suggests that we should also consider a new name for the aggregation bits because we changed the length on that list. And if we reuse the old name but change the type it can lead to subtle bugs in implementations that forget to update one of the usages or like still consider it based on the Old length. So yeah it's a small thing mostly for interop operability and forward compatibility.

**Stokes**[17:11](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1031s): Yeah I love to comment that it kind of breaks this like schema pattern we have of having the signature be after everything else but yeah I think generally rational makes sense. So yeah take a look at the PR and but generally yeah I think it sounds like a good idea.

**ATD**[17:33](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1053s): I'll add just a little note to
that which is that for attestation maybe it's not the most important thing but broadly adding fields at the end of a container allows you to use a trick where you read the common parts with a single deserializer and this is useful. We use that in blocks for example to determine the slot. So that we can determine which concrete serializer to use. So it's kind of like always good practice in SSZ to add things at the end. And  not just for the miracle stability but just for General ease of use when trying to upgrade from one container to the other. 

**Stokes**[18:26](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1106s): Yeah that makes sense. So the next one this was I believe it's suggesting to change how we are handling shuttling all of these EL triggered requests from the ELto the CL. This is PR 551 on execution APIs . Mikhail you open this would you like to give us an overview?

**Mikhail**[18:54](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1134s):  Yeah sure. So this proposal thanks Alex, Lightclient for the idea and this proposal is about to remove deposits and withdrawal requests from the execution layer block and instead of that the execution layer client will surface these requests into response to the geth payload method call after that the consensus layer will include these requests into the Beacon block body. So they are moved kind of like from the EL block to the CL block structure structure-wise. And then when the new payload method is being called the requests are dropped are passed to this method call as a separate parameters kind of as a sidecar parameters to the payload and and if the EL has fully synced. So it's online and can fully execute a block it will need to execute a block obtain those requests from the Block execution. And ensure that the requests given from the CL matches the one that are obtained from the execution of the block. It's kind of the the way it it's supposed to work is kind of similar to block KCZ commitments where we obtain them from the geth payload and send version hashes in the call to the new payload. The major difference here is that the requests can only be validated when EL is fully synced. But it does not introduce any new assumption in terms of whether this whether the CL can or cannot apply deposits and withdrawals during the withdrawal request during the optimistic Sync. With respect to the optimistic sync actually nothing is changing this proposal does not affect anything. Yeah that's the description of what is proposed and it yeah it would be great if we think through this and whether we like it or not on the consensus and execution layers side. In my opinion it's it's really quite nice design solution which simplifies the EL part yeah and I forgot to mention that this basically an alternative to generalising requests in the execution layer block. So I'll stop here for any comments or questions? 

**Etan**[22:00](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1320s): I commented on it before. Like I don't yet understand how like how the optimistic Sync would work in this new proposal because if you only have a CL alone how does it know which of these requests are legitimate if they are not part of the EL block hash.

**Mikhail**[22:24](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1344s): I don't think it changes anything EL block hash is basically an EL commitment to the data contained in a block. In this case we just move from EL commitment to the CL commitment. So we'll have them as a part of pick and block body and it does not change anything.

**Etan**[22:45](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1365s): When you receive a block and it contains a couple of these execution layer triggered requests how do you know as a validator whether these requests are the expected ones whether they are legit?

**Mikhail**[23:01](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1381s): If you're in the optimistic sync mode you can't know that for sure and you can't know this for sure even with the existing logic. 

**Etan**[23:12](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1392s): With the existing logic you can recompute the MPT and check that it is part of the block hash and eventually when the EL syncs up it can tell you that this chain is invalid. 

**Mikhail**[23:31](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1411s): Actually yeah but you can do the same that the chain can be invalid even when you're even after this change I really I don't. Maybe I'm over seeing something. But I don't think that it changes anything because today you can't execute you can't validate that deposits that or withdrawal requests that you have in the execution payload are the same as it would be obtained from the Block execution during the optimistic sync. And when the sync is over so you can tell that again the block hash commitment does not a malicious party can produce the valid execution payload in terms of a block hash but with invalid withdrawal request included into.


**Etan**[24:29](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1469s): Yeah I'm not seeing it yet but maybe we can follow up in the thread of that PR. 


**Mikhail**[24:37](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1477s): I also understand that if we accept this proposal then it would probably require some decent amount of engineering efforts to switch from the general request to this approach. Mostly yeah on the EL side.
**Stokes**[25:04](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1504s): What would the EL need to change? 

**Mikhail**[25:08](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1508s): Well they would need to drop the deposits and withdrawals from the Block structure. And they would need to surface this information in the response to the geth payload. And also would need to accept this data on the new payload and do this matching after executing a block.


**Stokes**[25:34](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1534s): Okay yeah I haven't had a chance to look at this PR I will soon and I suggest everyone else to do the same if you have a few moments.

**Mikhail**[25:47](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1547s): Yeah since this change is kind of like really important for how do we handle requests. It would be great to have it sooner than later if we even want it if we want it then yeah. Then we can just you know proceed as this but from my perspective I don't know if it worth discussing on the EL call as well. But if anyone from the CL side or EL side who are listening to this call can think on it and comment out if they're opposed and or not that would be great.

**Stokes**[26:27](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1587s): Yeah feels like something we can make a decision on the next EL call. Cool let's see so from here the rest of the agenda items are discussing new things that we'd want to put in  Pectra which is going to te us up for a fork scoping conversation which is probably why you are all here. So the first one I think will be simpler than PeerDAS. It's EIP 7688. This is essentially using part of the stable container EIP. We had a conversation about this at interop and the basic rationale was essentially we're making these breaking changes with the Attestations. You know if you want this sort of forward compatibility with respect SSZ Layout. We'll have to make more breaking changes in the future and so the argument is essentially to make all of the beacon changes now at one time. So you know that makes sense. What it implies then though is that everyone needs to go and like add this new SSZ functionality into their Library which is not a huge ask given the scope of this particular SSZ feature but it's definitely non trivial. So yeah Cayman or Etan I think you guys were kind of leading the charge on this. Would you like to say anything further? 

**Etan**[28:04](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1684s): Sure Cayman, already posted into the chat a link that tracks implementation progress. I hope that I have collected an exhaustive list of all the relevant SSZ libraries there. I think the biggest challenge is on the go one because fast SSZ was a bit of a concern there about its performance and maturity that the teams there considered making an entire new library instead of just patching the stable container support into it. But yeah let me know if anything is missing or if you need any guidance. We also have a PR in consensus specs repo that adds a lot of test like SSZ General tests and the results are the remarkable implementation which also has a PR with even more tests. So there's Grandine with a hands up. 

**Saulius Grigaitis**[29:16](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1756s): Yes sure. So Saulius from the Grandine team. So one question we have regarding the particular implementations of stable  containers. So we are thinking because of the reth language and essential of the nature of the reth language. We're thinking to keep version and containers at the application at the code essentially. So then in this way we can keep the code safety because otherwise all the like or most of the fields will be optional in the struct and I just wanted to ask. So for more Dynamic languages it's probably not an issue but for more static languages was there some some research or or some you know some different attempts to implement different way this. And is there are some you know some conclusions on that because once we get to this stable containers thing then the structs you know it becomes struct full of optional fields which is not very good in terms of safety that compiler can ensure. So I just wanted to ask maybe there was some conclusion on this thing there. 

**Etan**[30:51](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1851s): Like you have two new things one is this merklization layout which is indeed full of optionals. But then you also have these profiles which like have all the fields that are required as required Fields. All the fields that are no longer used are completely gone and you can also keep them as optional if you want like sometimes it makes sense for example a withdrawal request. When you want to request full withdrawal then just omit the amount. So in the implementation. I know what you mean. One approach that could be used if you want to avoid copying is that you just wrap it like you have the internal memory layout which is full of optionals. But then you have a type save wrapper that just provides assessors that access directly into this optionals like into the backing store. But the types that we are discussing here are quite like small like you don't have to convert them between profiles a lot and it's more like comparable to when you read something from JSON into SSZ like you you first look at what fields are there and decide dynamically which type you need and load it in there. So yeah would be interesting to see how the different implementations evolve. I think in typescript ironically they don't even have this type that's full of optionals but just provide a bit Vector that sort of tells you how many holes there are in like in the merklization. So there are different approaches that can be used.

**Saulius Grigaitis**[32:49](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=1969s): Okay so currently we likely will go with the approach where we will keep this version containers and we will see how it evolves because at the moment seems that it will be the smallest change needed right now for us. So we can keep with this version of containers like we did before. But we are on top of that, we are the stable containers here. So we will see but if anyone from more statical languages will have some conclusions on these approaches. I'm happy to hear.

**Sean**[33:33](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2013s): I just posted in the chat an example of what Mac from our team has been working on in Rust. It's got like the stable container struct with optional Fields but then like eight times mentioning the profiles are no optional Fields. Yeah so take a look if you want.

**Etan**[33:57](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2037s): What is the progress right now just to track like what implementations have already started for the like that was the rust the ethereum SSZ right that Library.

**Sean**[34:13](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2053s): That's what we use in Lighthouse.

**Etan**[34:16](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2056s): Okay and Grandine I guess as well started looking into it.


**Saulius Grigaitis**[34:22](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2062s):  yeah we have our own SSZ implementation and we started to look how to add Stable container that's why I was asking here.

**Etan**[34:34](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2074s): What about the Teku library and fast SSZ or the one that prysm is trying to build.


**Enrico**[34:43](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2083s): Teku we haven't started yet planning to do it very quickly.

**Etan**[34:49](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2089s): Okay and the prism?

**James He**[34:56](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2096s):  I don't think we've started yet. Casey would probably be one looking at it. 

**Etan**[35:05](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2105s): Okay yeah there's another thing where it will be useful for Verkle for the optionals there. But if we are considering 7688 for just to do it now to avoid breaking the smart contracts all the time then that will be before verkle So they can also take advantage of that for the optionals that they need. Okay. Another thing that we have to think about is to go through all the containers that exist right now in the beacon chain like there are not that many maybe 50 and to consider which of thems do need future extensibility which of them could benefit from optionals. Like for example for deposits there was a discussion at the interop where this activation eligibility Epoch would no longer be useful in the validator struct. So for example making the validator struct also a stable container would allow to deprecate and remove the those unnecessary Fields. Yeah just think about what containers need extensibility because if we don't do these moves now then when we later decide to extend them then it will break again right so yeah. 

**Stokes**[36:49](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2209s): Right I mean the one caveat is we might not know today which needs that in the future you know.


**Etan**[36:56](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2216s): Sure which is totally fine like it is always possible to just remove a field of a type right and and to add a new field. Like we did for previous Epoch participation in alter where we stored full attestations before and now we switch to these bit fields or the historical roots that got replaced with historical summaries. So that happened a couple times already and if you usejust a new field it is possible with the stable container to just replace the old field with a hole. So that no indit say get reshuffled and then introduce a new field at the end that's fine. 


**Stokes**[37:47](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2267s): Right and I think this conversation just highlights. So you know if you are curious about this EIP. We should probably start doing implementation work soon just to surface any of these things like Solas is talking about so yeah please take a look. And yeah otherwise nice work on the Devnet and yeah is there anything else on that otherwise we can move to PeerDAS. 

## PeerDAS status

**Stokes**[38:22](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2302s): Okay PeerDAS.So there was a ton of progress over interop on PeerDAS which is very exciting to see. Is anyone here on the call who was closer to that and can give an update 

**Barnabas**[38:41](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2321s): I could say a few words about PeerDAS Devnet 0. So we launched PeerDAS devnet 0 during the interop event. Since then we have reached an on finality event and we have about 14% participation. I think lots of clients have discovered lots of issues in the first devnet. And you could potentially relaunch anytime when we have something substantial. 

**Stokes**[39:17](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2357s): Okay sounds good. I mean I think especially given how early it was and it being the kind of first Devnet PeerDAS. That's to be expected. Yeah I think that then just kind of teas us up into the next big question which is you know do we want to include PeerDAS and Electra. And generally thinking about the scope for the fork. I think we'll all be happier in the future if we can finalize Electra as soon as possible, even today. So yeah does anyone have any thoughts on including PeerDAS given the reset progress. There's some stuff in the chat. Let me take a look but yeah I mean maybe to Kickstart the conversation like I think there's a chance that we could ship pectra this year kind of as is but then obviously that probably means that we'll do PeerDAS in the fork after. And then you know that could be sometime into 2025. Otherwise we could say Hey you know maybe it's like a bit more of a
lift but we could reach and include PeerDAS in Electra that would delay pectra some amount of time but I think it might be worth it yeah. Does anyone have any strong feelings about this?


**Nishant**[40:56](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2456s): Yeah had a question wasn't the plan to like decouple the PeerDAS fork from Electra. So you would you know set Electra Epoch X and you know PeerDAS like two months into the future but we would have like a point where all clients agree that this particular Epoch is when PeerDAS gets activated. 

**Stokes**[41:19](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2479s): Right so you mean like a CL only fork?

**Nishant**[41:23](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2483s): Yeah exactly. 

**ATD**[41:28](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2488s): I mean that's the same as including it just with a delay doesn't really matter like the point is that all the users have to upgrade before that point in time so we'd have to decide it with the hard Fork. 


**Etan**[41:46](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2506s): Well there's also the EOF stuff and there are the SSZ transactions which are also they could be combined with PeerDAS. So that it's both EL and CL right. 


**Stokes**[42:02](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2522s): Right but then that kind of opens the fork scope quite a bit and that almost suggests that there's a fork after Pectra where we do all of this which I think was kind of the original thinking the question is just yeah what are things do we delay. And how quickly can we get to this next Fork after Pectra and all these types of questions. 

**Etan**[42:22](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2542s): Do you know from the EL's whether like how how important is it that they do Verkle in isolation without any other changes. Like as I understand Verkle only touches the state try and some consensus tracking there like some data structures there. But are they willing to add orthogonal features or is it like if we have Verkle it has to be alone and everything that's not in there in pectra has to come after or what's the sentiment there.

**Stokes**[43:03](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2583s): I think that's generally the sentiment that Verkle would be an independent thing. Guillaume you have your hand up.

**Guillaume**[43:10](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2590s): Yeah the thing is for example EOF can definitely not ship with verkle because it touches the exact same okay. Some of the state that is being touched by Verkle will also be touched by EOF. When it comes to what's the name when it comes to SSZ routes that doesn't really matter because it is indeed completely orthogonal. Same thing with spear by the way if it doesn't really touch the state it doesn't matter as much. 

**Etan**[43:53](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2633s): So the only thing that would have to come before is EOF or like if it's not in there before then it would be after verkle right. 

**Guillaume**[44:04](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2644s): Exactly. I mean it's not the only thing but it's one example of such thing that either has to go before or
After.

**Stokes**[44:18](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2658s): Yeah ATD?

**Atd**[44:22](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2662s): Yeah so my broad feeling is that the stuff that we currently have planned for Electra are kind of unexciting and not worth bothering you know everybody's time with. So I'd be very interested in getting PeerDAS in. Just to have something interesting to ship in it. A lot of the work is also kind
of feels unfinished at this point almost every EIP that we've done for the devnet 0. It felt janky and undeveloped we did a lot of discussions and changes in Kenya to them where we changed really quite significant things about them or should at least in order for them to be good EIPs. So I think throwing PeerDAS in there is in line with like polishing the existing EIPs polishing PeerDAS and then shipping like a really interesting artwork that users will be happy with it rather than just you know some cosmetic changes like ah where do withdrawals come
from. 

**Stokes**[45:36](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2736s): Right I mean the one caveat are pushed back I think to that is just maxEB as a big thing. I personally lean towards including PeerDAS and Electra myself just because I think we'll be happier down the line even if it delays Pectra by a bit. That being said, Pectra is already quite big. Just in terms of a variety of cross layer things and that means you know more risk much more to Test. Maybe not so much a complicated roll out but definitely increases like Security in testing scop. So that's something to keep in mind for sure. Dragon you had your hand up.

**Dragonrakita**[46:17](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2777s): Yeah. I just want to say that EL clients are mostly positive about inclusion of EOF inside Prague but having two forks seems okay. Just want to say I'm not sure how much complexity is there we have it two forks in regards just having any everything inside prague just pushing it for like three months. Just want to mention that. 

**Stokes**[46:48](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2808s): Thanks Nishant you had your hand up.

**NIshant**[46:54](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2814s): Yeah so I would also be in agreement with you know adding PeerDAS to pectra. I feel like it's quite separate from the other EIPs that we have. So it's easy enough to test separately. Also, I don't think this Fork is going to be small. So adding PeerDAS which we have already had quite a bit of work on. I think is fair. 

**Stokes**[47:24](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2874s):  Yeah I agree.

**Atd**[47:25](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2875s): Yeah I agree with that it's kind of separate I would say that having one forks two months after the other is kind of insane. If we're going to coordinate everybody upgrading their clients we don't want to coordinate everybody upgrading the clients again two months down line. That's like not enough time to even, you know, go through a release cycle often. So that means that all the features that we would have in the plus two month fork is they' already have to be there in the previous one and then it's just the technicality whether we call it a work or not everybody like I don't really see that working. 

**Stokes**[48:14](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2894s): Right Saulius I think you add your hands up next.

**Saulius**[48:18](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=2898s): Yes, so if there is strong consensus on adding PeerDAS to Electra then I just wanted to check temperature. Maybe it makes sense to remove the attestations factoring but which exactly a it was the one that move the index makes everything makes a huge factoring. So because I think it also falls under this not so exciting features which was previously in this chart. In this call discussed. So is there a strong against moving this huge factoring if PeerDAS is added. Because I think it's going if PeerDAS is added and we have this huge attestations refactoring and during the interop there was some good ideas that I agree that if attestations refactoring is done. Then maybe we should combine that with stable containers. Because anyway it's a huge change. So I would like to hear reasons against not removing attestation refactoring if if PeerDAS is added. 

**Stokes**[50:09](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3009s): Right so you'd suggest take out 7549 and essentially swap with PeerDAS. 

**Saulius**[50:14](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3014s): Yeah that would be solution. 

**Stokes**[50:17](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3017s): Right I mean and then you could imagine the next Fork on the CL we do that change along with all the stable container stuff. 

**Saulius**[50:25](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3025s): So yeah that would be my suggestion because at least for myself it looks just two huge things if we add the PeerDAS and stable containers at one fork soon. 

**Stokes**[50:53](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3053s): Anyone have any thoughts on that swapping PeerDAS for attestation for EIP.

**Atd**[51:10](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3070s): I think the attestation one is like a lot of coding Community changes but it's not really impactful from a security point of view. I find them kind of worth I know it's just maybe not that much utility but and that would be the reason to not include it but I don't think it conflicts or or interferes with PeerDAS in particular.

**Enrico**[51:44](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3104s): But in terms of utility I would say that we discussed interop that there are good very good side effects of all of having that included which is much more space in blocks and very better reorg handling.


**Atd**[52:02](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3122s): So yeah that was the one reason to have it and I agree with that but it's also like a lot of work for the community. 

**Enrico**[52:14](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3134s): Which been well for us has been already kind of done for probably most of the client already implemented excluding the APIs. But if we have it if we have enough time to also include a stable container with it I see it as a I guess a good thing.

**Enrico**[52:42](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3162s): Yeah I my point was more not to link it to PeerDAS. I would link it to stable container and do both in one because they indeed are very linked. I do think that that change needs a few more improvements. I don't think it's read in its current shape. I do think that the confusion between the network form of attestations and the onchain or in block form of attestations needs addressing at type level and a few things like this. But if we throw in stable container I think we might as well do the attestations as well and doesn't really add a significant burden. 

**Mikhail Kalinin**[53:31](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3211s): Do you mean that we should rather have different attestation type for network and for the onchain?

**Atd**[53:41](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3221s): Yeah totally and also for the single single attestation single voter topic. So that when you create an attestation with just one validator signing it. W should have that as a separate
type because then we can have the validator index there instead of the index in committee which means that we can  increase security of the
Goss of validation or at least reduce like like make it easier to validate those. And that's
quite a win because we have a lot of attestations to process. 

**Mikhail**[54:30](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3270s): Yeah so you mean you would not need to have a state to compute the shuffling in order to validate the Attestation.

**Atd**[54:39](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3279s): Yeah I could pick up the public key without without the shuffling and do that before the shuffling and that's
always good. 


**Mikhail**[54:47](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3287s): Yeah but what would be the reason to have different types for Network Aggregate and for onchain aggregate. I don't the argument the points on the single attestation but it's the other. 

**Atd**[55:08](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3308s): They are  semantically different. So you interpret them in different ways. One of them has a large list the other one has a small list. It's just very easy to confuse the two in code flow. So when doing security audits on the code base like regardless what happens at the spec level we we are going to do two types for them just just to keep them apart and and and there's really no benefit of having the same type for them like they the network variant it kind of it appears
in places that are completely separate from the onchain version. So like there's no spec burden it's just it's not increasing complexity it's clarifying complexity in my eyes to have two types.

**Mikhail**[56:08](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3368s): Yeah see I honestly thought that if we have the just one type and we can reuse it here and there that will just reduce the complexity but if it's not just. Yeah sorry Sean.

**Sean**[56:23](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3383s): I was just going to say in Lighthouse we had a few bugs that probably would have been avoided if we had separate types. 


**Mikhail**[56:32](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3392s): I don't see any big problem from this fact perspective to introduce separate type mean like to have the all the attestation for you know. All  the attestation for the network Aggregates to keep it and to introduce the new one for and onchain aggregates.



**Stokes**[56:56](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3416s): Enrico you had your hand up. 

**Mikhail**[56:59](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3419s): Yeah so having a single type I see that is more future. So open up a possible future in which we don't have to change the type. And we enable earlier aggregation if we change the way we do that. I mean we don't force to have only single committee aggregation in the first place and you could potentially have very different way of aggregating in early stage. So the type will be exactly the same. 

**Atd**[57:45](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3465s): My feeling is that in order to do that we would have to have a hard work and introduce some kind of incompatible changes also. Because the gossip rules dictate that we have to send single vote attestations on that topic. So like anything that only goes on the network is entirely Emerald. And This only affects the encoding of the object on the network on one topic. I feel that it's entirely discardable this type in any future hard work like the single attestation and the same really for the aggregate.


**Enrico**[58:30](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3510s): Yeah I see your point now. So the only thing that is really matter what goes in onchain. And the other thing is just SSZ types that are floating around Network and doesn't really affect the validation of
Block. 


**Atd**[58:51](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3531s): Yeah exactly. 


**Mikhail**[58:55](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3535s): Yeah so to summarize a bit if we see that introducing the onchain aggregate separate type for it and to not change the attestation data type and use it for Network Aggregates as it is today. Would it be easier? Would alleviate some engineering complexities and potentially reduce the risk of introducing bugs. Then from my perspective it should be relatively easy to do on this backside. So yeah if we come to agreement on that. So I would be open to to do this
Change. 

**Atdl**[59:41](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3581s): Well I'm in favor.

**Enricol**[59:44](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3584s): I'm in favor theoretically but on practice I don't know how much will be the code base of tech would be
affected by such a change. Might be painful but I don't know at the moment. 

**Sean**[1:00:01](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3601s): Yeah I kind of feel the same way as Enrico where it's like it seems like it would have made more sense from the start but now it's like we sort of hashed all this out. And we' have to redo a lot of work to support it but I'm not entirely sure I'd have to think on it more. 


**Enrico**[1:00:20](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3620s): Yeah kind of roll back on some say on some things and then we already have felt the pain of making this working. And yeah I have mixed feeling.


**Atd**[1:00:38](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3638s): I've thought about this a bit and this change mostly affects the gossip layer. The reason I want to do it is really the single attestation security argument like I really like that one.

**Enrico**[1:00:51](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3651s): Yeah I like that one as well to have the validator index in there as much better. 

**Stokes**[1:01:00](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3660s): Okay I feel like we kind of went off on a bit of a tangent on the attestation thing. Is there a place? We can follow up async on this topic because then I kind of want to jump back to the chat. Mikhail, If you're able to make the PR. I can commit to making the change in this and then everybody can look at the code. And see how much it changed.


**Mikhail**[1:01:34](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3694s): You mean the PR to this back. 

**Atdl**[1:01:38](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3698s): Yeah exactly. 

**Stokes**[1:01:44](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3704s): Or if that's too much Mikhail even just like an issue with the change that you can just describe that would even be starting point. 

**Mikhail**[1:01:53](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3713s): Yeah but I think it should be easy. 

**Stokes**[1:01:58](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3718s): Okay great. There was a lot of chat in parallel and essentially we were discussing two Fork verses one. Does someone there want to maybe explain what they mean with two forks like is this essentially keeping pectra as is and then just putting PeerDAS in a fork after or were we talking about something else. 

**Tim Beiko**[1:02:30](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3750s): I thought that's what we were discussing but then people were saying an even smaller Fork than  Pectra and I'm not sure what that would even represent that's maybe were.

**Stokesl**[1:02:44](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3764s): Okay I also kind of lost track through all the chat so maybe people had different ideas of what two forks meant. Does someone want to argue for a specific two Fork configuration?

**Phil NGO**[1:03:04](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3784s): Us here at loadstar we did publish a blog post in regards to a two Fork proposal. Basically we just want to keep the scope of Pectra with the most of the stuff that we've already implemented as is. And try to ship something within 2024 and then the stuff that being worked on Parallel which still has like implementation details and stuff that needs to be worked on which would delay having a 2024 Fork would hopefully go into this second Fork is sort of the way that we outlined it. So that will include stuff like PeerDAS. 

**Tim Beiko**[1:03:53](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3833s): And yeah how about MaxEB. So I don't have your post ahead of me but oh.

**Phil NGO**[1:03:59](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3839s): I'll repost the link but MaxEB is mostly it's just like slight implementation detailed outside of consolidations. I believe that needs to be worked out but that that would get included in 2024 in the first fork. 

**Tim Beiko**[1:04:15](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3855s): Yeah and then you'd also want to add some SSZ stuff but yeah generally keeping in as is. 

**Phil NGO**[1:04:21](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3861s): Correctly we were're advocating really for stable container to really get pushing this first fork because some of the teams like nimbus and us have already implemented it didn't take too much Fork in our opinion. So that's why we were pushing for that to get included in the first Fork. 

**Stokes**[1:04:45](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3885s): Okay so then we could imagine essentially pectra as is with the intent to ship this year. Then there's  Pectra part two which is really just whatever you know the start with osaka forks. And then that would have PeerDAS but you know it might be mid next year or later right. And I guess that's kind of the decision to make is like how okay are we with having peerDAS potentially roll out you know much later.  I just feel like if we said okay Pectra this year and then PeerDAS and the next Fork will probably be a year from whenever  Pectra ships right. 

**Tim Beiko**[1:05:33](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3933s): We can tell ourselves it'll be six months.


**Stokes**[1:05:37](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3937s): Right and so I mean I guess that's it right but the time between that one and chapella was quite long.

**Atd**[1:05:54](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3954s): I mean in the E they I think it was reth that raised a good point which is basically that shipping in November is bad. So we'd have to ship it before November and that's night and PeerDAS is like a really exciting feature compared to pretty much most of the other things. 

**Ef Office**[1:06:27](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=3987s): One thing I do want to mention is that if we are thinking about splitting it into two forks. We have to be really careful that we don't then just overload the next for with new EIPs. Yeah I have no idea if we're ever going to be able to do that if we can actually commit to something a year and a half in advance because we're always coming up with new ideas, priorities change and so on. So yeah there's also an argument to be if for example we swap maxEB and PeerDAS. So that there's more focus on PeerDAS but yeah I think those are all just points. I wanted to have.

**Stokes**[1:07:12](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4032s): All right I mean we can commit today to saying hey only peerDAS in the dev star Fork but as you point out you know we feel differently in 12 months. I mean I do think having less stuff in one fork is better right. So everything is severely risked if there's two versus one and that does argue for pectra essentially as this. And then having PeerDAS in the next fork. We just have to be okay with the world where you know it's next summer before we get PeerDAS. 

**Tim Beiko**[1:07:58](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4078s): Or work faster. 

**Stokes**[1:08:02](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4082s): Yeah we should probably always be working faster. Franisco says that sounds like a pretty bad world says in the chat if PeerDAS is so exciting we should focus on that. So then you know that gets us back to  Pectra PeerDAS and then the question is do we want to make PeerDAS smaller by swapping something out and then the questions what. 

**Saulius**[1:08:35](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4115s): Yeah my argument would be that we still have some debate on on multiple EIPs in Pectra. The good thing about PeerDAS do that it's one thing not multiple. So if the Focus would be shifted completely to PeerDAS then I think PeerDAS could happen sooner but if we keep focusing on pectra and then in parallel on peerDAS. I think this is maybe something that keeps us dragging.

**Stokes**[1:09:36](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4176s): Yeah so Ansgaris basically suggesting we include PeerDAS and then reevaluate down the line which might be a good way forward.

**Tim Beiko**[1:09:47](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4187s): I guess from the spec and testing side. What I like to better understand is it more work to combine these things and one spec and then split them out. If it takes too much time or is it less work to like have them be two forks at worst case activate at the same Epoch or one Epoch after each other. My sense is like untying everything will be much more work than like having two clean separated things that we want to merge and if we don't even want to merge them we can just activate them you know I don't know if on on the same block probably causes some weird issues but like you could literally do one epoch after or you know 8192 epochs after or Something. But have it in a single release from a user perspective on the like on the EL side we've had bugs historically. When we take stuff out things end up like interacting with each other and it's like a non-trivial amount of work to safely remove something. So yeah I'm not a client implementor but my sense is it might be easier to spec them as two forks and decide later on if we want to ship them combined.

**Stokes**[1:11:02](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4262s): Yeah I think the issue is having like one fork dependent on another. I mean the CL teams must please try in. But I think that would generally be the catch but maybe we decide it's kind of worth the pain.


**Tim Beiko**[1:11:17](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4277s): Because it means you can't test anything on Pectra until you have stable specs for anything on PeerDAS sorry until you have singles. 

**Stokes**[1:11:27](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4287s): Yeah any change in the prior Fork is going to impact the fork after.

**Sean**[1:11:35](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4295s): Like these two PeerDAS versus rest of Pectra. I think are pretty segmented that maybe I'm wrong but I can't think of like inter Fork dependencies there but that would typically be an issue but like I can't see it here.

**Stokes**[1:11:54](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4314s): Right so we  Pectra is and then just for sake of argument there's like the f star fork in the seals that's
essentially off of the  Pectra stuff and then of fstar has PeerDAS. 


**Ef Office**[1:12:10](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4330s): We kind of had the scenario also with 4844 and chappella where we wanted to ship 4844 in chapella and then we pulled it out. So maybe client teams can say if that was in retrospect a good idea or if it would have been smarter for us to have just waited because we're kind of agreeing on doing the same thing right now. Right we're saying we ship everything together and in a few months decide if we have to RIP something out.

**Stokes**[1:12:41](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4361s): With the caveat that it would be in a separate Fork. So it might be a bit easier just to have it disabled.

**Atd**[1:12:50](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4370s): I'm going to put this in real easy terms for everybody which is basically that we're trying to pack a block here right which transactions go in and the way you pack transactions is whether they affect each other right. And I think pretty much everybody is agreeing here that PeerDAS is kind of orthogonal to everything else. So like it doesn't conflict with any other of the transactions that we're trying to pack into this block and that's the main reason why shipping it together with this Fork makes sense whereas some other changes that you know have complex interdependencies perhaps should go out that's why we wouldn't ship you know Verkle and EOF and everything in one. So in those terms I think all the items that are on Devnet 0 plus PeerDAS plus stable container. Nicely can be tested almost isolated until they're just put together and and we shouldn't see much risk in putting them together. 


**Stokes**[1:13:51](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4431s): So that's a suggestion for Mega fork and including pectra and then just charging ahead. Yeah Barnabas?

**Barnabas**[1:14:03](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4443s): Yeah my point for testing p and pectra at the same time is currently they are being activated at a different activation Fork EPOC. And we could keep that potentially even till we hit the Pectra. So what we could do is keep these two features absolutely separate till the last second and then we would just activate it on the same Epoch in the end. So instead of triggering the PeerDAS on Pectra Fork Epoch we would just trigger it on its own fork. So this way we can even in the last minute we could just decide hey we are not ready with PeerDAS. Let's delay that and let's not include that in the Pectra fork Epoch. 


**Stokes**[1:14:53](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4493s): Right so is everyone okay implementing it that way where essentially there is pectra and then there's a separate Epoch for PeerDAS activation and then we can.

**Barnabas**[1:15:06](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4506s): This is already the case right now so nothing really has to change. 

**Enrico**[1:15:12](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4512s): It will be effectively a parameter of the pectra network. 

**Stokes**[1:15:20](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4520s): It could be I mean it could also not be like it's not today right. 

**Barnabas**[1:15:28](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4528s): Yeah so I think this would be the best way going forward we say that we want to include it and we see how client teams are done with implementation or they are not done and if they're done by pectra time then we include it and if they're not done then we just delay
It.

**El Office**[1:15:47](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4547s): I think the complicating part in this is that both pectra as well as PeerDAS would be rebased off of dap starting point and both  Pectra and PeerDAS are changing at the same time. So one of them would have to be rebased on the other once it's considered complete. I guess so it depends on client teams if that's an easy thing to do or if it's a hard thing to do. 

**Sean**[1:16:16](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4576s): Since we're not changing consensus types in PeerDAS it doesn't seem hard to me to rebase the two so.

**Nishant**[1:16:26](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4586s): Yeah so the same for us. It's purely a networking change. So it can be cleanly separated or join together. 

**Ef Office**[1:16:37](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4597s): But one question there was wasn't PeerDAS changing Fork Choice as well because there's now sampling before a block is considered valid as opposed to right now the current Paradigm being that you get all the blobs and then it's valid. So wouldn't that touch some amount of consensus code and not just networking. 

**Terence**[1:16:56](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4616s): But the current Electra code or current Electra spec does not touch any fork Choice code. So that part is completely independent. 

**Nishant**[1:17:07](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4627s): Well for peerDAS it only touches justification . So that'll be the only Edge case.

**Stokes**[1:17:29](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4649s): Okay so then suggestion would be to have  Pectra as is there's now a separate Fork Epoch for PeerDAS but then PeerDAS is on top of pectra not an up. Does that sound good to everyone.

**Atd**[1:17:51](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4671s): I think there were arguments where introducing an entirely new fork in client code is difficult just for one Feature. So I think yeah.

**Enrico**[1:18:07](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4687s): That's why I was thinking is it was not an actual Fork but actually a feature that enables at a particular point in Electra Fork it was will be something like that for.

**Stokes**[1:18:26](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4706s): Okay so it's all time new Fork right. It's all  Pectra but then there's just a different fork Epoch.


**Enrico**[1:18:33](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4713s): No fork. Fork  enabling Epoch. Yes feature enabled Epoch PeerDAS Epoch enable and everything.

**Tim Beiko**[1:18:42](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4722s): Why is that different Like the CL Clients.

**Enrico**[1:18:46](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4726s): Because when you do and a fork you actually have completely different domains and signatures and everything changes.

**Eth dreamer**[1:19:02](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4742s): Bitcoin. 

**Sean**[1:19:06](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4746s): Yeah so we'd have to like resubscribe to different gossip topics for example change.


**Tim Beiko**[1:19:12](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4752s): Okay got it.

**Sean**[1:19:13](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4753s): Okay usually
change types but since there's no types changing here that's why we can do this.

**Stokes**[1:19:19](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4759s): Just running this through what happens if we do end up putting PeerDAS in F star is that going to cause any issues if we go with this approach that we're discussing right now.

**Sean**[1:19:33](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4773s): I think it would be pretty easy to bump bump it out with this approach. 

**Tim beiko**[1:19:41](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4781s): Okay so what you're saying is like you can do PeerDAS as part of pectra with a different activation Epoch this saves you the like overhead of all the news Fork implementation details but then if we wanted to move PeerDAS to its own separate Fork the only additional work is effectively that like Fork scaffolding overhead. Is that right?

**Sean**[1:20:09](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4809s): Like I mean scaffolding overhead would be required by the new Fork anyway so it's kind of like right. 

 **Tim Beiko**[1:20:15](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4815s): yes yeah yeah so it's like we can hold off on doing that implementation work until we decide
basically. 

**Sean**[1:20:23](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4823s): Yeah like from my perspective if we just have  Pectra as a separate enable Epoch whatever we can either set it to the  Pectra Epoch or disable it and then just like wait till we Implement fstar on top and then just set it to the fstar Epoch,

**Tim Beiko**[1:20:41](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4841s): Yeah makes sense. 

**Ethdreamer**[1:20:45](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4845s): One thing though is ik I think especially if they do it a fork quickly after the electra epoch. I guess if we don't do it a separate Fork we run the risk of people being able to run an electra Client that isn't Peerdas by the time the PeerDAS. 

**Adt**[1:21:10](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4870s): No I mean the code would have to be there in Electra if we I feel as if what we're saying here really is that we want to provisionally put it into Electra but it's easy to pull out if we don't want it in Electra like the story we're selling and from a technical point of view the way we solve that is with a separate constant for PeerDAS Activation Epoch.

**Stokes**[1:21:38](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4898s): Right which I think maps on to the thing everyone wants on this call today.

**EthDreamer**[1:21:47](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4907s): But then I guess  that we do rebase the on top of the fork and then we can decide whether to
combine it later.

**Stokes**[1:22:01](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4921s): Essentially yeah I we would just have this activation Epoch and then that could be whatever we want.

**Adt**[1:22:08](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4928s):The constraint that that introduces is that PeeDAS must come after electra then I think something that's
that makes sense. 

**Stokes**[1:22:16](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4936s): Well after epoch right which is what we're going to have yeah after the epoch.

 **Barnabas**[1:22:22](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4942s): Is it an actual problem though. 

**Atd**[1:22:25](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4945s): No it's not a problem I'm just saying that like then we for the fork rules to make sense we would that PeerDAS Epoch would have to be higher or equal than whatever we use in Electra Epoch
intestines for example which is fine it's totally fine. 

**Stokes**[1:22:46](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4966s): Terence?

**Terence**[1:22:49](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=4969s): I think there's one thing that we probably miss that we should be careful of is that when you activate Electra before PeerDAS does right like which fouk Choice should you be using should you be using a fouk Choice rule that is specified in PeerDAS or should you use the fouk Choice rule today right. So that's something that's probably worth thinking about and whether there is risk there by going either way.

**Stokes**[1:23:21](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5001s): Right but don't you only change the implementation of this data available in Spec?

**Terence**[1:23:28](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5008s): I haven't looked at the latest for spec I suppose there's changes yeah I I think Franchesco is that answer that.

**Stokes**[1:23:36](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5016s): Say no as in it's not that encapsulated.

**Francesco**[1:23:40](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5020s): Yeah so it's not it's not just changing implementation is data available it's a bit more complicated than that but not not really that complicated. Like I think someone already mentioned before the actual peer sampling part of things is really basically restricted to checking for justifications. So it's something that like you have a lot of time to do. And doesn't kind of really get in the way the critical path but there is a change in the fork choice. So it's yeah there is something to  consider there I mean I don't see what it would even mean to switch to the PeerDAS fork Choice before PeerDAS is live because like you're not doing sampling and yeah I think it would make sense to just keep using the regular fork Choice until you actually switch to the PeerDAS Networking. 

**Stokes**[1:24:42](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5082s): Okay we only have a few minutes. Carl?

**Carl**[1:24:51](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5091s): Gaining here by having it as a separate Epoch off the fact it seems to me we're just assuming the worst that things might not work out timing wise and putting in all the effort of splitting it ahead of time which means you kind of have to just take the loss on that the the the time Delta to to to implement separating them out anyway. It just seems like we take a pessimistic route or no particular gain. 

**Stokes**[1:25:22](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5122s): Well the game is we want to ship pectra in time. Like it's I think all we're really doing is just uncoupling this activation Epoch and so we could decide that's equal to pectra or we could have it later. If we need the option.


**Carl**[1:25:38](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5138s): And adding that option like how bad is it to add that optionality because if it's not that bad to add that optionality. Then truly it's not that bad to add it down the line to me this just seems like a thing that complicates testing and a bunch of client work and stuff between now and then this is not something we've really had before I don't think for any features or am I wrong.


**Tim Beiko**[1:25:58](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5158s): I think the difference though is you're saying you're adding like this huge new feature to the fork and the base case shouldn't be it's going to like ship super quick you know not going to cause any issues and going to go smoothly like the base case should be it's going to add some complexity there's stuff we don't know yet about it that we're going to figure out and it's probably easier to hedge like not delay all of Pectra because we've added this huge thing and if we turn out they' be surprised that like it's actually easier than we thought which I don't think has ever happened for any like large feature then we can couple it easily but yeah that does it does seem worthwhile to have like some separation to not tie the fate of everything else that has higher certainty to this.

**Carl**[1:26:54](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5214s): I mean fed to me it doesn't seem much worse than just stripping it out if we just if we reach the point where this is not going to work but if everyone disagrees with me on that that's totally Fine.


**Sean**[1:27:05](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5225s): I kind of get what you're saying and I kind of agree you have like a little bit more flexibility where you can just like enable PeerDAS like an arbitrary epoch. Like maybe that's good for testing or something but yeah don't I get that it's we could just package it in this fork and we can do this work if it ends up not being able to do this Fork because the work to actually make it enable based on the epoch isn't that much.


**Ethdreamer**[1:27:37](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5257s): Yeah like basically doesn't it come down to testing like either we tie Pectra Readiness to having PeerDAS adequately tested and then we activate PeerDAS or if we decide that like PeerDAS isn't ready and then we let we don't we don't have  Pectra weight then we need to implement here as a second for just to force clients to update.

**Nishant**[1:28:12](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5292s): Yeah so with PeerDAS. Do we also want to increase the target blob count?

**Stokes**[1:28:21](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5301s): I think generally but that's a whole different conversation okay. So summarize pectra as is. There's some threads to follow up on the existing EIP set we'll move ahead with PeerDAS with a separate activation Epoch with the idea being that it will go live in pectra and then we'll see how PeerDAS implementation goes to determine if you know PeerDAS activates pectra or maybe some later date. Does it sound good to everyone.

**Etan**[1:29:06](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5346s): I think the 7688 still needs to be added to the list.

**Stokes**[1:29:14](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5354s): That was stable containers.

**Etan**[1:29:16](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5356s): Exactly yeah the CL portion of it.

**Stokes**[1:29:20](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5360s): Do we feel confident that implantations will be ready?

**Etan**[1:29:27](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5367s): I have a working Devnet.

**Stokes**[1:29:31](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5371s): Okay yeah I mean that to me feels like something we could discuss on the next CL cal. We're also at time. So we will close soon. I'd probably personally like to see a little more implementation progress across all of the production implementations  before including it for.

**Sean**[1:29:57](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5397s): We have a lighthouse implementation sorry we have it in the library we use we haven't yet tried to integrate it into Lighthouse. 

**Atd**[1:30:14](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5414s): Is anybody against including it?

**Stokes**[1:30:19](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5419s): The concern is just making the fork even bigger than it already is.

**Atd**[1:30:28](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5428s): That didn't answer my question?

**Enrico**[1:30:33](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5433s): We haven't even started working on it so is a question Mark for us. 

**Stokes**[1:30:41](https://www.youtube.com/watch?v=Lrk99mKiWaU&t=5441s): Okay we're at time why don't we table stable containers until the next CL call and in the meantime if you want to support the EIP you should work on implementation. Okay thank you everyone we're at time. That was a lot of different conversation but thank you all for joining and yeah I'll see you on the next call.




## Attendees

* Alex Stokes
* Saulius Grigaitis
* ef Office
* Etan(Nimbus)
* Pooja Ranjan
* Guillaume
* Enrico Del Fante
* Roman
* pk910
* Ansgar Dietichs
* Toni Wahrstaetter
* James He
* Dankrad Feist
* Terence
* Mikhail Kaliin
* Tim Beiko
* Ben Edgington
* Matt Nelson
* Barnabas
* Carl Beekhuizen
* Kaesy
* Phil NGO
* Sean
* Justin Traglia
* Mikhail Kalinin
* Justin Florentine (Besu)
* Peter
* Cayman
* Mehdi Aouadi
* Eitan
* Echo 
* Hsiao-Wei Wang
* Manu 
* Lightclient
* Joshua Rudolf
* Barnabas
* Draganrakita
* Lukasz Rojmez
* Trent
* Fredrik
* Nishant
* Atd
* NC
* Francesco
* Mikenueder
* Vasilli Shapobalov
* Daniel Lehmer
* nflaig
* mario Vega
* Danno Ferrin
* Phil NGO
* fabio Di Fabio
* ethDreamer

# Next meeting [Thursday] June 13, 2024, 14:00 UTC]


