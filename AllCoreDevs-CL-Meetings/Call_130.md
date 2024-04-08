

# Consensus Layer Meeting 130 [2024-3-21]
### Meeting Date/Time: Thursday 2024/3/21 at 14:00 UTC
### Meeting Duration: 95 Mins
#### Moderator: Tim Beiko
###  [GitHub Agenda](https://github.com/ethereum/pm/issues/987)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=3rRJ1H0MJDY) 
### Meeting Notes: Meenakshi Singh
___


| S.NO. | AGENDA | SUMMARY |
| ----- | ------ | ------- |
| 130.1 |    Dencun Upgrade Insights: |Devs discussed about Development leading up to the Dencun upgrade. **“Dencun Diary,”** features perspectives from over 45 Ethereum developers, highlighting both the successes and challenges encountered during Dencun’s preparation. |
| 130.2  | Pectra Upgrade Proposals:| Developers discussed proposals for the upcoming **Pectra upgrade**. Notably, they agreed to include EIP 7251, which aims to increase the **MAX_EFFECTIVE_Balance**.  |
| | | The team is also scoping out EIP 7547, related to **Inclusion lists**, for potential inclusion in the Pectra upgrade|
| 130.3 | Networking Layer Improvements: | The ACDC call addressed improvements to Ethereum’s **networking layer**|
|    |      | Parithosh reported that a small number of blobs are arriving on the network delayed, approximately four seconds into a slot. Further investigation is underway to understand the cause of this behavior, with a presumption that it may be related to MEV builder specifications. |

____


**Danny** [7:09](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=429s): Okay great. We should live. This is All Core Devs Consensus Layer call 130. This is issue 987 in the PM repo. Just shared the link. Anything related to deneb then we'll move on to a quick discussion around local block boost defaults and we have a lot of things to talk about in Electra. and then some networking stuff to discuss. So quite a pack schedule. Before we jump into it Trent you had something more to share?

### Dencun Action Items 

**Trent** [7:46](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=466s): Yeah. So for the past couple weeks like starting in the beginning of February. Actually, that's like a month and a half. I've been collecting submissions for this thing called Dencun Diaries. I just dropped it into chat and it's just a compilation of core devs perspectives looking back on the last two years and looking forward to pectra. And just future ways that we can better improve the processes. So check out the link. I think it's a really useful resource if you people have been around they'll know that I've done this for the merge and also the beacon chain launch. So just adding to that collection of historic record. Hopefully we're starting to build a institutional memory of how core Dev and how the community around it works. So thanks to everybody who submitted I think it's a really nice snapshot of sentiment and hopefully we're learning as we go. But I'd love for anybody to check it out if you weren't included for some reason or you missed the deadline. Please just DM me and we can get you added to it. Thanks.

**Danny** [8:53](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=533s): Great thank you. Okay we still have the Deneb on here one item from Tim.

**Tim Beiko** [9:03](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=543s): Yes if you wrote an EIP for the fork that went live we should move those to final. I've opened PRs for every single one of them that were not final. I think Alex Stokes was the only one who did it. So shout out to Alex they're all linked in this PR. So again if you're an author on one of those EIPs please just take a look. I think pretty much all of them only require an approval. Yeah and then hopefully we can get all of those finalized in the next couple days.

**Danny** [9:43](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=583s): Yeah cool it also needs an approval from editors,  from an author and editor.


**Tim Beiko** [9:49](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=589s):  Yeah once we have all the authors approved I'll bug the EIP editors to get them to approve the
Batch.

**Danny** [9:57](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=597s): Terence? 

**Terence** [9:59](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=599s): Yeah I guess this is somewhat related. It's probably easier to use this forum. So we have been seeing  blocks that have KGZ commitment. But the blobs never arrived. So these are unavailable blobs block. So by definition these blocks never gets imported. So they are reorg but consider these are actually somewhat validated blocks. It's pretty interesting. So if you're running a validator so I kind of presume this is a builder issue already because like standard clients has been tested. So if you so say if you use so say today if you're validator you are missing blocks. And yeah but then for some reason your blogs are not getting included then please take a look. So here are some numbers so on March 18 we have 3, March 19 we have 10, March 20 we have 6, and March 21 we have 4 of those incidents. And I finally capture those blocks. It turns out that no one's capturing those blocks by default. So I have 4 of those blocks and I will look into them and find out what's going on. Yes I also have the slots as well. I can share those. 


**Danny** [11:16](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=676s): Yeah interesting. It might be worth doing a Sanity check through block print if they are all the same client. Well yeah if they are all the same client that might be telling them maybe it's on a builder issue. Maybe you can also tell if they're be any questions for Terrence that's interesting. Okay something we don't have to get into today but something that I think as if. And as we do have any sort of meaningful data analysis on performance block distribution times things like that please add them to the call. I think people are eager to get an insight into how things are performing. Are there any interesting metrics or things worth sharing right now other than looks okay. Primarily to 4844. 

**Paritosh** [12:21](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=741s): We did it short blog post on some of the metrics we're seeing. I've just linked it. Just have a look at it. Yes I think one of the thing that we wanted to keep a close eye on is that the P95 value for blog blob arrivals with respect to a slot are getting relatively close to 4 seconds. This was based on the first day of data. So we still haven't done a follow-up analysis after the week but that's something we want to keep an eye on. 


**Danny** [13:00](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=780s): Got it. Potus?

**Potuz** [13:03](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=783s): Yeah just looking at this blog post about resources usage. It might be slightly misleading there's we changed the timeline for attestations to be included on the net. So we're allowed to include attestations from more than 32 slots ago. And both at least prysm an Teku will have this problem that they would just remove this attestation from the pool and re gossip
them if they see them again. So someone is sending these attestations very late. We do not know who but certainly prysm and teku will just keep resending them and this blows up CPU and bandwidth. So I mean certainly bandwidth has increased because of the Block fork but the numbers we're getting are just exacerbated by this box just this is already fixed on prysm I suppose on teku as well.

**Enrico** [14:01](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=841s): Yeah I can confirm and we have merged a couple of fix to actually accommodate the change reflecting all the configuration around different pools and gases that we have. So the next release should have that fixed.

**Danny** [14:29](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=869s): Got it. Any questions on either Pari's metrics or the attestation kind of amplification relaying. All right cool. Anything else on Dencun? 

**Gajinder** [15:28](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=928s): I have a small cleanup PR that I think is also linked to the agenda regarding just renaming of blob base Fee to blob base Fee per gas basically to make sure that the unit is more aligned with what it Conveys. 

**Danny** [15:51](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=951s): Where is this PR? Okay this is 8316. This is a clarification or this is a bug fix or this is just a naming change?

**Paritosh** [16:11](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=971s): Yeah I mean it doesn't affect any of the headers. So basically just yeah sort of renaming of some helper functions and references.

**Danny** [16:26](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=986s): I see okay so maybe the fork for authors take a look and if anyone else wants to chain in anything else on Dencun. Okay I did notice on some of the charts that the base fee has gone above one a couple times but I think last time I checked is still sitting there. Okay.

**Mark** [17:07](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1027s): Well just on that note I did a very cruded look at the blocks and it seemed like we're posting about 30% of the target number of blobs per block on average. It was just over a thousand blocks but makes sense why the base fee is glued to one right now.

**Danny** [17:30](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1050s): Yeah that's what I've been seeing. We're kind of still on the average of oneish over time one. All right cool. Let's keep our eyes peeled on interesting developments here and surface anything here that's relevant to either client stability or potential future improvements. Next up Frederick has to leave at halfway through the call. So he's had some comments around local block boost defaults. Fredrik?

## Local block boost defaults

**Fredrik** [18:02](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1082s): Yeah I'm in the SAA but I hope the microphone is working fine. Otherwise I'll go outside sounds good. So yeah this is basically about doing a client change which should hopefully improve the censorship resistance. If you look at the one of the pages that Tony created censorship. The pics we can see that I think it's around 64% of all the external  block Builders are censoring blocks basically by not adding certain transactions and about 51% of the relays. also block these kind of blocks and since basically today I think it's around 95% of all the blocks being built are done using relays and external Builders. This PO is a bit of an issue because some of the blocks will be censored. So basically what we could do to kind of help mitigate this a bit is to adjust the default local value boost to 10%. Currently in all clients this is set to 0% but by changing it to 10% it means that the local blocks will receive a 10% boost. So instead of like if there is a block that's built that can be built locally for .004 eth and an external block coming can be built by 041 eth than the external would be design be used in these cases but by setting the default to 10% the local block would be prioritized in that case. The way that clients have implemented this differs a bit some of them have a boost on the external blocks and some other boost on the local blocks but this can always be changed by a flag So even if the default is set to  10% a user who don't want to do that could always change it to 0%. Or they could set it to 100% if they want that and the current status here there are some PRs that's been made they're linked on the issues for this Call. Nimbus and Teku have already merged these changes, the other clients have PRs for it and are thinking about approving them I think and the EOF testing team are also implementing some additional tests for this which was based on some feedback from the prysm team. So yeah that's it in Nut Shell. 

**Danny** [21:20](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1280s): Terence?


**Terence** [21:22](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1282s): Yeah I'm supportive of this change I guess one question I have was that like this will also I break some testing percent right? If before we're just adding a little bit of Builder bit that's that's higher than local bit now we have to make sure we add this at 10% more so that's one thing the second thing is that can we get some testing on hive for this test case just because for the prism side I don't think we have end to end test that cover this scenario yet. So I hope hive can do it. 

**Fredrik** [21:54](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1314s): Yeah I think Mario, is here and can probably mention something about that he created the tickets for it. 

**Mario** [22:00](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1320s): Yeah I created a ticket. I’'m going to work on making Hive aware of this flag. So we can reliably configure it depending on the test case. it's going to be very simple basically just if you are setting it to a high number a higher than normal number we should expect that the the blocks are locally built and the other way around or the other case yeah super simple but yeah.

**Enrico Del Fante** [22:26](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1346s): And not all client have the same parameter working the same way I guess. So that this is the only thing.

**Mario** [22:35](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1355s): Of course. So probably what we'll have to do is that we have a high value that's going to be transformed into a client specific value.


**Enrico Del Fante** [22:45](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1365s): Oh yeah, it makes sense and set the flag. 

**Danny** [22:50](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1370s): Potuz?

**Potuz** [22:51](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1371s): I want to be the voice of descent. We should stop specifying these kind of things. We should stop doing this in a coordinated fashion. The reason this wasn't merged in prysm to start with even before the merge when we started designing this was that it would be controversial if we had a value that was bigger than zero. And now we're coordinating to have something and even thinking about texting this. I think clients should be free of setting these kind of things however they want. They're configurable by the user and we should be less afraid of actually acting on this in our beliefs. 

**Danny** [23:34](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1414s): Right I guess the testing infrastructure can should probably be neutral to defaults it should just in the event that this flag exists be able to still test building. Right. Can we track that balance?

**Mario** [23:54](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1434s): Yeah in my opinion yes it's going to be like just when in the case the flag exists and it's set. It functions properly that's the idea behind test.


**Danny** [24:07](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1447s): But agreed I mean there's some of these things that there's a reason other than just kind of network resilience that many different clients exist. Different design different philosophy different failure. Sean? 


**Sean** [24:25](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1465s): Yeah I generally agree with Potuz is that it should be sort of a recline thing. And a reason like not to set it to 10% for example would be that it would be kind of an unexpected default. And it's kind of like taking advantage of the fact that a user might not be aware of this feature whereas like a better approach, maybe in Lighthouse, we could do this would be to like require a user to set that value if they're using a builder. So it like raises awareness of the flag without like I guess giving opinion towards what it should be and that might have like a similar effect. 

**Danny** [25:05](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1505s): I am curious maybe some of those that do some analysis on this like obviously we know that me is quite chunky. So a lot of the margin you get on most blocks is pretty small. Do we actually know as a function of call it 5/ 10/ 20% whatever that margin is like how many blocks additionally would be locally built. 

**Potuz** [25:29](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1529s): Well but we are seeing relays playing some games that actually are making this margin as small as  possible right. So over time we're seeing this margin being getting lower.

**Danny** [25:54](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1554s): Okay. Are there any other comments on this other than just kind of surfacing awareness and knowing that there is a design space for clients in their default and ux are on this  perimeter.  Yeah Tim that but that's kind of this absolute value on.

**Tim Beiko** [26:24](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1584s): Right you need to map that to a percentage but yeah.

**Fredrik** [26:34](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1594s): I think it's you know it probably depends a lot on the on the current market conditions as well like if it's if it's a scenario where a lot of transactions are being done. We can probably make a bit more juicy MEV blocks and then the margin for might be higher compared to a bare market for example. But yeah I don't have any stats right now. 


**Danny** [27:05](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1625s): Sure, that's why that absolute number is kind of tough to deal with because the market can change quite a bit. Whereas like the percentage that a builder usually gets on top of a local build might actually not have the same type of Market function/  Market Dynamic function. But

**Fredrik** [27:27](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1647s): Yeah exactly.  

**Danny** [27:29](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1649s): Yeah. We have a pack schedule. Is there anything else people want to talk about? I know there's still some active stuff going on the chat which continue. 

**Fredrik** [27:42](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1662s): No nothing.


## Electra maxEB discussion

**Danny** [27:44](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1664s): Great. Thank you Frederick. Okay Electra before we get into it. I do I Max EB. I mean there's a number of like small proposals that might filter in for example blob gas increase think committee slashing maybe is maybe is a small proposal but these two big ones we've gone back and forth. We've thought one or the other was buried and the roof surfaced at various times but we're definitely at the point where if we're not making a decision today . We really need to be making decision soon. There is the intention to have functional prototypes and Devnets of Electra some point in May. And we're closing at the end of March. So I just want to contextualize. These are medium if not large items that we continue to discuss. We can't continue to kick the hand on the curb for too much longer. Otherwise I think the default just becomes no. I guess indecision is a Decision. I have I'm lots of opinions on these but I will leave it at that. I think it's time to make a call. I'm also not going to be here for three months starting at the end of this call. So you might have to make the decision on me. Anyway there have been a number of breakout calls there was an inclusion list breakout call I there is certainly some conformance on design. And some
of the subtle decisions around the design. Mike can you give us an update on where we stand here?

**Mike** [29:32](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1772s): Yeah for sure. Thanks Danny. Hey everyone, hopefully you can hear me. Yeah so just linking the comment in the issue which links to many more links. So kind of links all the way down. Yeah as Danny mentioned there was a breakout room the recording is there it was pretty well attended and I thought quite useful parents took some notes that are linked in that hackmd. And I guess the main takeaway was just everyone coming to consensus on the set of features that we want for the PoC. Yeah that was kind of the last big thing was discussing the whether or not to bundle the inclusion list with the block on gossip. And we all agreed to do the unbundling version and yeah that's kind of where we're at a few more docs that I linked in that comment Potuz has the doc on bundling that. I just mentioned Terence had a short talk on the relationship to blobs to inclusion lists. This isn't part of the proof of concept but it's kind of an interesting thought experiment as we kind of move down the path. I wrote a small doc called the case for Electra that's more of like the meta argument for why this feels important. And then the PoC spec is still being developed in this link here. I'll link this one actually in the zoom chat because it's kind of the source of Truth. Trent put his camera on too. That's funny. So yeah I guess it feels like a lot of the a progress has been made I guess in the last week. Would yeah love to continue jamming on it in the room and I guess a lot of the client teams have started implementing and would definitely be happy to hear from any of them if they would like to chime in here. Seems like generally the implementations are are going well and uncovering lots of like nuances about the spec that we're kind of ironing through the only thing I'll bring up today as far as technical issues is there was this one question about the relationship between enshrined 4337 and inclusion lists. Had we've kind of talked about this once before but this was kind of re-brought up in today's context. And I think I don't think it's a blocker from what I can tell there's nothing that. Oh yeah IO has unknown with AA. Yeah so I don't know if you saw my latest message Terence in the chat but I don't think this actually is a blocker. I think we can deal with it I don't know if it's worth going through the exact mechanics here but yeah Pptuz. 

**Potuz** [32:24](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1944s): Yeah can we, I mean if we have execution layer clients that are not that are actively working on account abstraction. Let's just trace the problem abstractly here what it is it imposes a condition on account of abstraction that forbids an account from being swept by a different account. If there are the signs that are the have chances that are people like looking at that will allow an account to be swept out by a different account by a transaction coming originating from a different account that would break our current design of inclusion lists. this seems like.

**Miike** [33:05](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=1985s): Did you see the message? So I asked Vitalic about this and he said basically one way around this would be to just check a few things you add another condition which is not only if the nonce is being reused but also if the balance of the account decreases. Then you can ignore that transaction for the inclusion list like even if there is a AA world where you can sweep an account without sending a transaction from that account. We could just have this other check on the inclusion list transaction condition. Does that make sense? Right. That's what I was thinking too. Yeah I sent the screenshot of the chat to the I don't think it gives free DA because you can just drop the transaction in the inclusion list because the summary entry is Satisfied by the transaction or by the balance of the account going Down.

**Lightclient** [34:04](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2044s): It does I think it gives you free ability to fill the IL with useless transactions that you sweep.

**Mike** [34:12](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2052s): Well you can leave the IL empty already. IL is yeah.


**Lightclient** [34:22](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2062s): But if you can convince nodes that are trying to construct ILs that some transactions might be good to put in the IL. And then once they make it in the IL taking space for maybe other transactions which might have been better then you can just sweep them. And remove them. 

**Mike** [34:41](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2081s): Yeah I see what you're saying. Yeah I agree with franchesco's point in the chat that like you could already try and stuff really high paying trade transactions into the summary. And then use a  different transaction with the same nonce to replace those transactions. I think you still have to pay the gas. So like it still feels fine maybe there's a slight subtle difference here but yeah maybe we can handle it offline. 

**Danny** [35:19](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2119s): Yeah so one of the attempted things to assess over the past month on this was engineering complex. Does anybody want to chime in on engineering complexity maybe noting any sort of concerning points of design or unknowns or maybe comparing it to some type of work we've done before so that others on this call can better understand the relative complexity. 

**Gajinder** [35:51](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2151s): I'm working on the IL PoC. So I can basically add few points over here. So basically it is a little bit different than blob availability because the next block if you get the next block then which is valid then basically the previous block IL get satisfied. So when you are trying to do range sync basically you don't really need an IL. And when basically you are saying to head and are doing gossip and at that point the IL availability really matters. So that is the only you know gotcha that was around this. And apart from that I think I found that keeping keeping status sort of flag in fork Choice was actually more convenient. Because then it would help me sync forward sync blocks easily through blocks by range. And basically I could just track the status. Okay this is I need to basically check that whether they will have the valid child in the end or not. the tip will have a valid child in the end or not or I will basically then have to start looking for and importing the IL corresponding to the tip. But apart from that I think these are the moving parts and then the engine API  integration that I'm going to start with Geth. But it doesn't seem that challenging. And basically I think IL once we wrap around the head wrap around our head for over the concept that is IL basically is forward and the availability is a bit different and basically just handle it that way. I think it could easily be developed it could easily be targeted in
Electra. 

**Danny** [38:14](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2294s): Thank you. Any other perspectives on relative complexity or any questions for Gajinder.

**Enrico** [38:26](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2306s): I can jump in saying that I started working on the PoC implementation and I got so I become more and more confident on the implementation complexity generally. And the only thing is still in the back of my mind is the IL signing compared to the block production. So if we need to sign if we could if we want to sign the EL is convenient to sign and send over the network an EL before the actual block production. It will then also require some additional API calls and different and other timing between CN BN. So I'm currently thinking about in for the PoC just having the same at the same moment just sign the block and sign the together but this might be another complexity in the API and the integration between VC and BN if I'm getting if I'm not mistaken.

**Danny** [39:52](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2392s): Potuz asked why is that but I'm not sure what point of the conversation you ask question.

**Potuz** [39:58](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2398s): I'm not sure how technical we want to be here but I didn't understand Enrico's point that we need extra  API methods to send the inclusion list before the slot.

**Enrico** [40:16](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2416s):  Is there a conflict can you repeat here? I haven't check.

**Potuz** [40:22](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2422s): I didn't understand why sending the inclusion list before the start of the slot would require extra API methods. It seems to me that it's the same you're just going to request it from your execution layer before right after you send the FCU of the previous.

**Enrico** [40:38](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2438s): You need to sign that so when currently the block production is started this slot before right. So at the moment of the of the block proposal you the VC just request the block. And you the block okay but you're also mentioning that you it's also possible that you could sign and send it. 

**Potuz** [41:07](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2467s):  Yeah you could sign the inclusion list and send it before the slot the thing is that you're gonna sign that thing anyways you're gonna sign it at your slot or before the slot so that that API call is going to be there either way. 

**Enrico** [41:19](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2479s): Right but you need to request it through the BM right. 

**Potuz** [41:24](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2484s): Yes and you will do that anyways during your slot.

**Enrico** [41:29](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2489s):  Well no. It's because now we have this concept of block content in going through the API. And if like we have for  blobs you got block plus blobs and plus other things. So we could put the EL inside of it and then the VC on the same API call you got you sign the block. 

**Potuz** [41:52](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2512s): So you're saying that instead of like having two different calls you're going to have to overload the call for the blob to return an different envelope with two different messages that you
Sign.

**Enrico** [42:03](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2523s): Yeah I mean if we want to make the flow is the same we can at the moment if we want to release everything at the same moment but if we want to have the freedom of of signing and  sending over the network in different timing we need to design a new API this is I think we  can't avoid that.

**Pawan Dhananjay** [42:27](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2547s):  Yeah I've been implementing ILs on Lighthouse and I agree with Potuz.  I think it is quite  useful complexity wise if you are able to send the IL before the start of your slot because you don't have to touch any of the existing block production logic at all. So it would be a significantly smaller refactor and it would be an addition and I would complexity wise. I would prefer that compared to overloading the current block and blob proposal methods.

**Gajinder** [43:09](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2589s): Unless just at the beginning of the slot your head changes right so that basically can cause you to basically request IL and sign it and send it. But I guess that can be taken care of and I also agree that independent design is better. Because what generally happens in Block production is that it's not just the execution layer that we and wait for they also wait for Builder which basically sends the block a little bit later into the slot. Which I think they they're always trying to Target 1.5 second or more so it would be faster definitely just to you know at the start of the slot just to request and I and send it over independently. 

**Danny** [43:57](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2637s): Right let's table this it's interesting that we're at the point of debating some of these nonces which is certainly if this is to go in. We'll have plenty of time and fun to do that there. I don't want toattempt to make the IL inclusion call without EL maxEB discussion. I will say before we move on to the maxEB discussion that I'm at least a couple of individuals and loadstar seems as an aggregate signal that they would like to see this in the fork. But let's think that we generally have a feel on the status update. It seems like a lot of people have opened this up and taken a look. Let's take a look at maxEB where that stands? There was a breakout call yesterday and there is to be another one on Friday. I there were two because of time zone considerations Phil you wrote up some notes. Can you give us a high level to start? 

**Phil Ngo** [45:03](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2703s): Yeah so yesterday we had a breakout room in which we had participation from loadstar from lighthouses there and also prysm. Overall it seems like at least between the three of us. There seems to be some general consensus on inclusion for this. And mostly because you know we have a lot of validators on here and it's going to be pretty concerning if we don't deal with this. So it seems like we have consensus on that. But we do have some  remaining decisions to make in the spec which is what these follow-up calls are for there is a issue open by Mark for these two. And there is an agenda for the next one which I'll post in here as well. And then if you can come to these meetings with some your thoughts. I believe Mikhail had also updated Dapplion PR in regards to maxEB with some additional points in regards to slashing. But yes that's basically the tldr not sure Mark if you wanted to add anything to that. 


**Mark** [46:25](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2785s): Well yeah. So I think from Lighthouse perspective what I've seen is that we've prioritised MaxEB in then inclusion list but are totally open to doing both in the fork. I believe that's basically the same idea from load star and Preston on prysm expressed a similar sentiment and then I talked to Phil yesterday and teku and he had similar sentiments. 


**Danny** [47:12](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2832s): Can I jump in I'm curious prysm's current perspective on the complexity of MaxEB engineering Complexity that has been something that's been brought up a number of times. But I know that the team is going to come re-evaluate. Can somebody speak to that.

**Potuz** [47:34](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2854s): Is Preston here? So if Preston is not I can just say that he's very op he's in charge of doing this. And he's been he has an implementation that it's almost complete. And he's very confident that it can be included and and that it's he's confident that we can Target maxEB for end of this year. Which was one of the hard requirements that we had on any EIP. 

**Danny** [48:02](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2882s): Right okay.

**Mark** [48:03](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2883s): One of the takeaways from the meeting seemed to be that maxEB required a little bit more of like making decisions around our cleaning up the spec. I guess where but it seems like less
engineering work to actually Implement than inclusion lists whereas inclusion list is a little bit of the opposite the Spec's a little more stable. But it's a little more engineering work but yeah it I mean the things that remain on the spec to decide are it's like we have several good options. It's almost reaching the point of Byte sharing to where you know we just kind of got to pick one nothing that we can't fix.

**Danny** [48:56](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2936s): Okay Mark you were echoing that a number of teams were signalling both but did you also say that those teams were signaling both with a preference for MaxEB in the event that it was one or the other and that consistent across. 

**Mark** [49:15](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2955s): So I Preston did I believe he said that he would at least him personally would have preferred maxEB over Electro. That's my opinion and Sean's opinion in Lighthouse. I don't know about Pawan and then I think loadstar Phil you might have expressed a similar opinion in terms of priority but oh did I say MaxEB over?


**Danny** [49:52](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2992s): Yeah I think you meant ILs.


**Mark** [49:53](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=2993s): I meant inclusion list yeah but yeah I think everybody expressed that sentiment and I think that's in the notes. Maybe Phil you can correct me if I'm wrong but yeah I think that's what I certainly remember Lighthouse prysm saying that and I know that Paul said it I don't know about Paul's priority but he did say that MaxEB seem fine to him. 

**Danny** [50:32](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3032s): Yeah so great so there's a couple things I want to bring to the table. Obviously being able to handle the engineering complexity of one of these and isolation is something at a certain point just when we're smashing many things together spec-wise, the spec builds more complex to the testing of that on every single path is more complex. Getting to the point where you're even at testing for clients takes more time. So certainly these things can sometimes  compound an unexpected ways. And I want to keep that in context. Yes they're moderately isolated in terms of the components they're touching but you know I wouldn't naively just say like the complexity is additive in terms of shipping in a entire Fork.  So I just want to keep that in mind if and as people are pushing for two.  I also do want to bring up and reiterate there is a third moderate to Major R&D thing going on which is peerDAS peer data sampling. My intuition is that one of MaxEB or IL's going into a lecture probably does not greatly detract from the paralyzation of being able to do peerDAS R&D but that in the event they're both that we're now you know beginning to trade off and probably not really being able to tackle all those three things. In parallel once that's not to say that some of that will happen. Right that the networking experts are different than people that are touching database this or that. So I do. There is paration that can happen but intuitively it feels like we probably going over a Tipping Point on a lecture where that's going to take out most of the oxygen in the room. And so I just want us to be very conscious about these Dynamics when attempting to make this decision. 

**Mark** [52:53](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3173s): I think we did a little bit and there was I mean just the because PeerDAS can be parallelized provided that team that was kind of why the other two proposals were being pushed more. That's all. I'll say about that that was just kind of a sentiment. 

**Danny** [53:16](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3196s): Yeah I agreed.  I do think that they're im-parallelizable. I just worry that the kind of mounting complexity of Electra will almost certainly across some teams. If not all begin to be a kind of a balance between resources and certain resources at times if not the entire time. 

**Sean** [53:59](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3239s): Yeah I guess I'll just say something. I do agree that like at the end of the day there's only so many  engineering hours so like including both is sort of atacid acceptance to Deprioritize PeerDAS  to some degree. I do think though that we have the capacity on Lighthouse at least. So yeah those my two cents.

**Danny** [54:41](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3281s):  Are we so I at the outset I said from a timing perspective in relation to what we're trying to do in. And by May we're already behind into attempting to make these decisions that. And so kicking the can down the curb for another two weeks puts us certainly in a tough position to try to hit some of those for May targets. So implicit there is today's the day are is there additional information that we are going to gather the next two weeks. It's going to help us make this decision or are we in the place to make this decision today that's a go or no go on both of these moderately large if not large proposals. Sean?

**Sean** [55:38](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3338s): Yeah so I would just say like it seems like the further we've been getting into the PoC's the more confidence there's been from like a development perspective that just implementing these two are doable I definitely get your point about like especially in the spec and the spec tests like flushing all those out at the same time covering all the Edge cases that might take more time. But I think from a development perspective like definitely achievable like in the clients.

**Danny** [56:16](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3376s):  And on the inclusion list side. One thing that I didn't bring up earlier I would like to get the perspective on is the amount of complexity in the execution layer versus the consensus layer is this something where by making this decision here. You know it's really 90  -95% of the complexity is over here. And it's really kind of a small ass on that side or is this something where it's more like 50- 50 , 40 - 60 in terms of complexity Split.

**Potuz** [56:46](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3406s): I think it's not even clear right now today we started discussing that now the EL is going to have to go back. And check if the certain balance decreased in the previous block to validate the inclusion list. We are just learning about this issues now right and this is in part because at least I can speak for myself. My naive not knowing about execution I really thought that this transaction would revert instead of being just not includable.

**Sean** [57:21](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3441s):  Yeah. I think we need to I think we can analyze the damage I guess kind of risk of this new account  abstraction thing in the next day or two. Like I don't think it should fundamentally change anything honestly and as Ansgar mentioned earlier like in Shrine 4337 is a like this only matters in Shrine 4337.

**Potuz** [57:43](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3463s): So no but the thing is the thing is that even if we do include this and we not consider at all what will happen in the future with account abstraction this increases complexity on the EL side for implementation of this. 

**Sean** [58:04](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3484s): Do we Matt or Marius could you talk a little bit about EL complexity or if any of the Geth guys?

**Lightclient** [58:18](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3498s): I think for is it's not too bad on the EL side. I worry slightly about having to keep track of balance changes from the previous block but none of this stuff is intractable. It's just a bit more work bit more things to Think Through.

**Sean** [58:41](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3521s): Yeah super happy to work through the implications of that specific AA thing I guess apart from that though. It seems like everything's well understood. I'm definitely not an EL Dev. So trying to guard my language as much as possible.

**Lightclient** [58:59](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3539s): I think it's I think the work on the EL side is maybe like 20% of the EIP. 


**Sean** [59:06](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3546s): Yeah that's the number I was going to give to 8020. 

**Gajinder** [59:12](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3552s): Yeah from my JS perspective I think IL yeah should be easy to implement on EL side. Because you have so ELs have all the capability they have the mempool, they can gather transaction and just Bunch them up and easy to verify again like executing a payload. 

**Danny** [59:37](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3577s): So are we at the point where these specs could be built into Electra with 7002 and the other things that are already or or you know is it a couple more weeks of of R&D of PoC of of design decisions. It sounds a bit like the latter.

**Sean** [1:00:09](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3609s):  I mean I don't know, I just get the impression that everyone more or less agrees that these things can be done. I don't that there's probably not major unexpected implementation problems that are going to come up. And at this point it might be a question of what do you prioritize More.

**Danny** [1:00:41](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3641s):  Between the two or between.

**Sean** [1:00:42](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3642s):  Yeah I guess complexity I guess makes the decision on whether or not we go for both. And if we have to go for one then it does kind of depend on what do you prioritize that's at least my read. 

**Danny** [1:01:05](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3665s): How much of I mean one interesting thing is that the anti- censorship parameter changes from Execution Layer call. You know if that really moved the needle on quality assurance of transaction economically viable transactions making into the block.  Then can wait , you know, is there any Intuition or data on how much we can move the needle with smaller things because if that could be moderate even moderate not even massively substantially moderate. I would make the case for being afraid of the complexity of both of these things together. And knowing how timelines go and knowing how tough it is to test these systems and tabling that. If there aren't some moderate winds to be had there or in other other places then  maybe it's worth taking the complexity now. Yeah Potuz just to contextualise we're talking about what to include in the electra fork. Obviously there is another major R&D stream which is peerDAS. So it will occur in some amount in parallel. So it's but it is there's it is there in the trade-off space the more that goes to electra the more that that parallel work stream will not get us as much fire. What's OOP, Oh out of protocol Mike says my two cents don't depend on OOP for CR. I do agree but on what time frame right like if we can help reaffirm the norm of CR and be in a reasonable spot for a stretch of time with smaller changes than it advises time for the protocol to then take on that complexity, that's at least the argument I would make. Yeah so ILs  decision can't be made without the execution Layer. We have Execution Layers call  is here but if there was an attempt to go on on this side this I think have to surface in a week on the execution layer call to do an affirmation on that side. Certainly the decision on MaxEB I believe is almost entirely in isolation. Tim says we can see if ILs start with my ELs Dev and see how feel that get the first that's time you want to speak to them one right. 


**Tim Beiko** [1:05:00](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=3900s): Yeah so I think yeah for two reasons I guess I'm proposing that like one obviously there's high uncertainty about whether we can fit ILS and MaxEB in the same Fork. So we should probably just start I should probably just start working on it. Two like yeah MaxEB is clearly just a you know CL thing whereas IL does have implications on the EL side as well. So it'd be good to sanity check with the other EL stuff that we are considering you know  the team like or bandwidth. So if we include MaxEB we have this CFI thing that we've used for the EL in the past that basically signals things. We are strongly considering for the fork but not fully committed to yet we can put ILs there work on a first devnet with maxEB. All the other stuff we've already included if next week we make some decisions on ACDE about small EIPs. You know new OPcodes or whatever we can have that part of the first Devnets. And also I think this gives us a couple more weeks to figure out some of these spec level issues for ILs where yeah like two you know if like two to four weeks after that we have a first devnet or two with everything else a better understanding of the IL complexity. Then we can decide to merge it all together. Or you know potentially to push ILs out to the next fork or something like that. 

**Danny** [1:06:45](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=4005s): So it's the proposal to finalize MaxEB spec to build into the electra spec while over the next two weeks to continue the IL EIPs. And go no go in two weeks based off of that and at which point we either building into the spec or setting aside.


**Tim beiko** [1:07:03](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=4023s): Yeah and I don't know if I'd want to put two weeks but maybe you know two to four or something like like I think the data point that we should be looking for is like implementation Readiness on everything else alongside like the IL spec Readiness. So like if in like four weeks we have a working devnet with MaxEB and like people people are feeling very confident about the whole thing then great maybe we can add IL and that's additional complexity. But if in four weeks we're in a spot where like it feels really hard to even get what's already done implemented. Then yeah that's a signal that like is probably like additional complexity that we can't take on. 

**Sean** [1:07:49](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=4069s): My only concern there is like would there ever be a case where we then decide ILs are more important and switch it out with MaxEB. 

**Tim Beiko** [1:07:59](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=4079s): You know like if probably not.

**Danny** [1:08:04](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=4084s): Because of this my attempted aggregation of signal that MaxEB is the preference. I know that you feel otherwise but I think that's what most people have echoed so far in the chat. 

**Tim beiko** [1:08:21](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=4101s): But yeah but it is I think it is worth emphasizing though like yeah if we go that route it gets hard to pull out MaxEB because we've like merged it with every everything else.

**Danny** [1:08:41](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=4121s): Yeah and again my read has been for the majority of people in this call if it were one of the other MaxEB. So begin the spec build with MaxEB I also just from a spec build  complexity standpoint. You know that's going to take the next 10 days next at least week. So and I don't I don't really want to build those two things into electra at the same time. So there's kind of a sequential thing that has to happen anyway. I'm going to say again I personally believe that these two things together we've entered into a much more complex space than we have been discussing and intended to over the past couple months. So just do so knowingly. Oh say at this point in the process we're also always very confident and excited to take on complexity and there's a lot of work to do. Okay we do have a current plan. I'll just say it MaxEB spec to be worked on gotten into a very stable place and integrated into the electra spec build as soon as possible. IL PoC's final design decisions and things to be done over the course of the next one to four weeks. And be make kind of informed
decision on IL inclusion in the two to four week time Horizon probably more like four based off of continued understanding of complexity PoC's electra PoC's Etc. Okay thanks everyone tough conversations. Potus?

**Potuz** [1:11:15](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=4275s): Yeah I just wanted to confirm that it seems that it's not really certain but it seems that we're aligned with prysm that maxEB is a yes. And if we do commit to maxEB then ILs will be a no.

**Danny** [1:11:33](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=4293s):  Okay good to know I think that we can still have the conversation in two to four weeks and yo'all can if you stand firm in that Echo that in that at that juncture. But good to know going into it. Any other comments on these two proposals before we move on and the implicit proposal of peerDAS that is in competition with them. Just a quick update on that very active work on specs and subal prototyping and eager to have other teams really at this juncture jumping into certainly the spec and Design discussion and project as well. Okay we have we're not going to make it through this whole schedule today Ansgar timebase blob gas increase proposal can you give us just a quick perspective on that. 


### Time-based blob gas increase

**Ansgar** [1:12:45](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=4365s): Yeah sure. So right so basically that initially we had like a big debate about the right super level 4844 ended up going with three Target six Max so maximum of 750 kilobytes per block. Trade off of course P2P load and the validated disk space. And yeah the intention of course is that we want to scale up DA from here to full draft starting over the next. I know three to five years or something and most of that we will have to do via actual sampling methods. So PeerDAS do and then potentially steps afterwards and but for PeerDAS we will need to have an EIP anyway that increases the throughput because that's the only kind of in protocol change that  needs. Also separately we could even before peerDAS already try to just basically make the most of the current Headroom that we have. B6 was of course cautious by Electra. I was thinking we'll have like six to 12 months of experience with kind of 36 and how stable the network will be with that. We have this EIP by Tony 7623 to increase the call data cost. So that will decrease the worst case normal block size from from roughly 2 megabytes almost 2 megabytes today to to roughly half a megabyte at count gas limits. So and the idea of course for that is to to both just basically protect against Count Worst case attacks but also just give us a bit more head room both to increase the one Gas limit but also hopefully some extra blob throughput of course for blob throughput. It's not just about worst case it's also about average case considerations  but still. So with kind of both from both these perspectives both called potential peerDAS. But also like using the headroom that we have today. And there was the idea of basically having an EIP for potential kind of increase in  the Blob throughput so we created one just mostly as a basic Shing point for compensation run this. It's currently in draft there's a link in the agendas. The idea would be although of course we could change that to maybe pays in the blob throughput increase gradually the count EIP proposes to go from count 36 to a total of 816. So one megabyte Target Two megabytes Max over the over a span of four months basically every month ship one extra Target blob Basically. Right and so in base case we could use that for we still with full 4844 download logic and then gradually scale that and make sure we have this emergency escape hatch that if we see any problems with the network we could and basically cancel that those further future increases. But also if we are shipping if we are successful shipping peerDAS on a similar timeline to electra. Then we could of course just seamlessly use that as the kind of throughput increase that would be powered by DAS instead. Yeah so the idea is of course kind of like it's a little early to make the decision now it was more to now have EIP that we can specifically reference whenever we talk about this. And in my personal belief at least is that like basically sticking to this rough meme of trying to 3x the ethereum DA every year from now on over the next three to four years until we are dank sharing levels would be like a very very nice thing that we could provide for L2’s to that would be roughly reliable in terms of the time timeline for increases and this would just be a first step on that path. 

**Danny** [1:16:32](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=4592s): Thanks Ansgar. Just quick context. I am a co-author on this. I do I would support something in this direction one assuming we get solid data on 4844 in production two in the event that
the Tony's called repricing scheme does go in. And three I'm certainly a proponent of this timebase increase of timing and maximums to be debated in this case. And also in the case that we're doing PeerDAS type or datability sampling type things. Really going from testnet simulations testing analysis to mainnet is I think always going to be come with with quite a bit of uncertainty. And so this like time based approach where we do have the Escape Patch of kind of an upgrade to cancel is I think a tool that's going to be quite useful as we're changing things around data. We have a lot on this agenda this is certainly just to kind of open up the dialogue does anybody have additional comments or questions at this time?


**Kasey** [1:17:55](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=4675s):  I can't figure out how to raise my hand? How does the kill switch on this work if we decide that we want to stop the progression of increasing the limits?

**Danny** [1:18:03](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=4683s):  That would be just a quick Fork. it would be an additional EIP and a fast upgrade so in the that that should be considered when thinking about automated time based increases. essentially at these various junctures you get you get new main main net data there would not you can certainly designed some sort of like kill switch where it's like a like how the the gas increase is done you know essentially consensus voting or something like that.  I would try to avoid that complexity and governance point. All right anything else on this one? Thank you Ansgar. Next up a couple of EIPs were dropped in by on Etan sync committee slashing. This is in draft status Etan do you have any you want to comment on here other than it's distance ? 

**Etan** [1:19:22](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=4762s):  Yeah it's like essentially the current state of the research of what was previously in consensus specs there was an issue where I already made this proposal last year and for the lightclient data backfill there is an open PR but because they affect consensus. I think it's appropriate that they are also tracked in the EIPs. The lightclient Sync Committee Slashings they are especially interesting together with maxEB. Because maxEB allows the Sync committee to have a larger total balance. So larger total balance there means that more eth can be slashed in case of an attack right now many use cases even if the slashing is perfect are limited in how much they can secure because there is only
512 validators. Even if they are slash down to zero it's not that much if it's like a bridge that secures a lot but with maxEB this could become interesting to follow and the like cine data back fill what this one enables is eventually decentralized chain synchronization for the beacon nodes similar to what we have on the EL with SNAP sync we can build it for the CL as well once we have that because it allows to sync The Trusted block route decentralized and then also enable snaps in from there own getting rid of the servers like checkpoints. And those are no longer necessary.

**Danny** [1:21:29](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=4889s): One thing that's worth contextualizing at least in my mind on the Sync community slashings is that there have been at  least a number of R&D efforts to attempt to ZK the FFG portions of the beacon chain to get these bridges that end up having full CTO Economic Security with kind of a default slashing default consensus. And just bypassing the sync committee. Do you have any perspective on whether these are likely to come into production fruition in  reasonable time frames or are they still priorities.

**Etan** [1:22:07](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=4927s): From what I was told and what I heard like no I didn't check personally but it's still quite far definitely post verkle as I understand but I'm not an expert in this area so if such transition Could Happen earlier of course it would be much greater than the sync committee which yeah it's still heuristic are to say with the ZK proof you know that it's correct right. 

**Danny** [1:22:43](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=4963s): Yeah I'm Gonna Knock on a couple doors. I heard you a year ago moderately promising result but I haven't heard of any of these projects actually finishing. Any questions for Etan or intuitions or opinions on where this these two might fit in relation to Electra? Okay any further comment on this? 

## Research, spec, etc
### [Network shards (Attnet Revamp + DAS Distribution Columns) consensus-specs#3623](https://github.com/ethereum/consensus-specs/pull/3623)


**Danny** [1:23:35](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5015s): Okay we do have a number of P2P discussion points there is a new proposal up by Age Manning on Network shards which would be in relation to kind of how nodes are selected for Attnet and future DAS distribution. Age or Etan can you give us a brief on that?



**Age Manning** [1:24:01](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5041s): Yeah I can just give it. Yeah I'll just give a quick overview of maybe just all the things that I raised just to save save time essentially I just wanted to make some of the teams aware of these things so there's this PR which we've called Network shard something that Anton suggested but it currently isn't super important for what we have right now but when we start having extra gossip subtopics that we need to form like stable backbones for this introduces A New Concept that essentially allows us to tag a a node ID or a pier ID to which topics they should subscribe to and allows us to have essentially an easier way of keeping track of those peers to make the the topics stable so essentially I'm just trying to get some attention from client teams to have a look at that PR and just signal whether they think it's a good idea bad idea so that we can kind of progress and move forward with it the second thing that I suggested is the I don't want message which is in Gossip sub it's in the gosip sub specs at the moment it's the implementation at least for us anyway is quite small but it it promises to significantly reduce some of the bandwidth on Gossip sub where we we're planning on starting to test this practically now in Lighthouse but it's one of those things where we need the entire network to upgrade before we start seeing some of the effects so if you have some spare bandwidth it's probably worth the effort to try and implement this into your client and you'll share the benefits of it it should be fairly easy to understand if you just have a look at these two PRs. 

**Danny** [1:25:48](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5148s): The backwards compatible but the more people that do it the more aggregate effect it's going to have on the network meaning you could roll on Lighthouse independently but you're just going to be a bit in isolation in usage of it


**Age Manning** [1:26:01](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5161s): Exactly yeah so so it's entirely backers compatible we'll we'll probably try and release it into Lighthouse and see if it is useful but we only have you know X percentage of the network the more clients that do it the the the better the effects yeah 

**Danny** [1:26:17](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5177s): And isation Final in the is it in state that you would release it yet or do we need to go through some P2P hurdles to kind of get it into the spec. I see it's not merged.

**Age Manning** [1:26:30](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5190s): Yeah so it's not merged in my opinion. So the general premise is pretty much outlined in the specification that you can go and implement it. And you won't have any issues there's some parts that aren't specified and there's some discussion around like some DAS vectors that can come up because scoring hasn't been introduced into the spec but I think that's not a huge hurdle for not implementing like at least the base version of it. 

**Danny** [1:26:57](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5217s): But like the message format and things like that.

**Age Manning** [1:27:00](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5220s): Yeah that's all spec'd out yeah okay yeah so that should all be fairly good. Yeah I'll take questions on all three if after this. If anyone has any but the last thing is implex I think there was a discussion about this earlier on where some of the client teams only had implex and were going to upgrade to YX implex. I think in libP2P is now being deprecated. Joao is on our networking team and may have some extra things to say. But just curious about any client teams whether they still require mplex because our plan is to kind of deprecated at some point. Yeah that's it for me.


**Danny** [1:27:39](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5259s): Let's take the last question. Frst does anybody still relying on solely on Implex? 

**Teku** [1:27:46](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5266s): For Teku our implementation of Yamux is not really production ready yet. So yeah we still rely on Mplex.


**Danny** [1:27:58](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5278s): And it looks like loadstar does as well.


**Phil Ngor** [1:28:01](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5281s): Yes we still working on our yamux implementation right now just dealing with some performance issues with it.

**Danny** [1:28:10](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5290s):Given the deprecation of Mplex in Spec can we start talking about a timeline to deprecate in rspec. You know is for four six months end of year is there any intuition on when we can do this.

**Phil Ngor** [1:28:37](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5317s): I wouldn't be able to give you a confident answer today without talking to Cayman. I'll have to get back to you on this.

**Danny** [1:28:49](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5329s): Dapplion, I'm the only reason would be if there are security concerns  rush it which I do not have good visibility.

**Age Manning** [1:29:04](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5345s): Oh yeah Joao has been looking at it. I think a little bit in more daytown. Okay yeah maybe not.

**Danny** [1:29:24](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5364s): Yeah Joao and Age if there are particular security or optimization or other reasons to do this on you know fast timeline. Can we surface that outside of the call. And if not you know obviously we have a lot of different engineering items going on maybe both teku and loadstar can can if there's not a reason to rush. They can take a look at the potential timelines does something.

**Joao** [1:29:55](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5395s): I would just ask for us to move on with the spec because on the spec and Mplex is still required if you could move into optional would be a great update already.


**Danny** [1:30:18](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5418s): Yeah we certainly could but we would just know that that would fragment communication the network as of now given them Teku loadstars imputation. Maybe it's worth opening up a PR that makes it optional to Galvanize the conversation in one place. I have a do question on network shards is the obviously we use Discovery to find bage particular attestation subnets already live. Is this compatible with that or if you implemented Network shards you now would have an issue finding peers that haven't implemented meaning is it is it backwards.

**Age Manning** [1:31:17](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5477s): Yeah it's Backward Compatible. Essentially I don't plan on changing any of the discovery things at least until all the clients have kind of upgraded. You wouldn't get any benefit if you tried to do the discovery kind of optimization at the moment. Yeah, we're still using the same Discovery we've always used for forever. Even though we have, we currently have the current iteration of the node ID to attestation subnet. That's in the spec at the moment but it is backward compatible yeah. 

**Danny** [1:31:51](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5511s): But once everyone does upgrade you would make some changes. 

**Age Manning** [1:31:55](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5515s): Yeah once everybody's upgraded we'd probably have two one I Pro initially I would try and use the fast optimization where you search for the prefix and then fall back to just
the standard one where we just search for everything. But it yeah.

**Danny** [1:32:12](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5532s): That's not a spec change. That's an engineering change once you have confidence that the network is upgraded.


**Age Manning** [1:32:17](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5537s): Yeah exactly.

**Danny** [1:32:24](https://www.youtube.com/watch?v=3rRJ1H0MJDY&t=5544s): Yeah I mean given that we want to use something similar with data availability. This layer of Attraction does make a lot of sense to me. Yeah essentially making it a tool we can reuse analyze and understand. Any other questions on any of these? I don't want has been close for a long time I think that at least a couple of teams implementing this could get this over the get this over the edge and especially when thinking about Network load and relation blobs and other things like that. I don't want to make you know at a moderate impact seems very very with well especially for the relative Simplicity that it is. All right, any other questions or comments on any of these networking proposals? I was not confident we're going to make it through. Any other discussion points or closing remarks?  And with a couple minutes to spare thank you everyone Alex Stokes will be running this call for the next few months. Please don't give him too much trouble. Take care. 

## Attendees

* Danny
* Potuz
* Recordbot
* Mikeneuder
* Trent
* Joao Oliveira
* Tomasz Stanczak
* Pooja Ranjan
* Terence
* Mark
* Ignacio
* Mikhail Kaliin
* Anders
* Josh 
* Tim Beiko
* Age Manning
* Fredrik
* Justin Traglia
* Etan (Nimbus)
* Peter
* Ben Edgington
* Matt Nelson
* Barnabas
* Pawan Dhananjay
* Saulius Grigaitis
* Echo
* Toni Wahrstaetter
* Bayram
* Alexey
* PK910
* Enrico Del
* Scorbajjo
* Lightclient
* Dankrad Feist
* Carl Beekhuizen
* Stefan
* Kaesy
* Phil NGO
* Sean
* Mario Vega
* Caspar
* Lukasz Rozmej
* James He
* Spencer -tb
* Kolby Moroz Liebl
* Gajinder
* Dan
* Taran
* Paritosh
* Ansgar Dietrichs 
* Dapplion
* Francesco
* Ahmad Bitar
* Mrabino1
* Fabio Di Fabio

# Next meeting [ Thursday]  April 4, 2024, 14:00 UTC]
_______
