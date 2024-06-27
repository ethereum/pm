

# Consensus Layer Meeting 135 #1069
### Meeting Date/Time:  Thursday 2024/6/13 at 14:00 UTC
### Meeting Duration: 90 Mins
#### Moderator: Alex Stokes
###  [GitHub Agenda](https://github.com/ethereum/pm/issues/1069)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=LpY1JQHl9EY) 
### Meeting Notes: Meenakshi Singh
____



| S No | Agenda | Summary |
| -------- | -------- | -------- |
|135.1 |Migration of the Kurtosis Ethereum Package:| Refer to Issue [#1069](https://github.com/ethereum/pm/issues/1069#issuecomment-2163980030) in the Ethereum/pm repository for details. Ensure you upgrade your infrastructure accordingly. |
|  | | Tim Beiko has submitted Pull Request [#8662](https://github.com/ethereum/EIPs/pull/8662) to refine the different senses of “CFI” in core dev governance.|
|135.2  | Electra Devnet-1 (CL Side):| Merging PR 1 into the devnet-1 specs, which refactors the attestation layout following EIP-7549 and affects SSZ merkelization.|
|   |   | Client teams target v1.5.0-alpha.3 of the consensus specs for devnet-1.|
|  |   |   Rough timelines suggest a couple of weeks after the specs release for implementation readiness.|  
|135.3|  PeerDAS Work: | PeerDAS and Pectra EIPs are currently advancing in parallel, but will also be activated on different devnets to avoid testing interference. The launch time of PeerDAS Devnet 1 may be 2~4 weeks later.  |
|135.4 | Raising the Blob Count in Pectra:| Intent: Increase Ethereum’s data throughput in the upcoming hard fork.| 
|   | | Opinions on raising the blob count: with or without PeerDAS, or deploying PeerDAS alone.| 
|135.5| Uncoupling Blob Count:| Currently set independently on the EL and CL but must match.|
|    |   |  Considerations for handling the change in blob base fee.|
| 135.6 | SSZ-ification of the Protocol:| Expect a devnet by the next CL call.|
|   135.7  |  Research, spec, etc   |   Naming the “F-star” for the next CL fork to accompany Osaka on the EL.| 

____



## Agenda

## 0. Announcement
### Migration of ethereum-package kurtosis module


**Alex Stokes** [4:53](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=293s): This is Consensus  Layer Call 135. I'll grab the issue here for the agenda and we'll just go ahead and get started. So first off there's just a few announcements, the first one is about Kurtosis. If Barnabas is on the call I think he can give us some more details there. I thought I saw him somewhere. 

**Paritosh** [5:23](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=323s): Yeah I can. So we wanted to just announce that we're taking a more active maintainer role in the Kurtosis ecosystem/ethereum package in- general. And one of the steps is that we've done a migration from for the ethereum package itself. So it's moving from Kurtosis Tech organization to eth Panda Ops. You can find the redirect URL and a few other instructions on what might break in Twitter or in the Kutosis Discord but if you wish to continue using the old setup you can always clone the last release and continue using that. But in case you want to keep up with future changes then please update your URLs and  target the latest release onwards. So 4.0 onwards would be maintained mainly by eth panda Ops. 

# Review request for the PFI/CFI/SFI EIP: [ethereum/EIPs#8662](https://github.com/ethereum/EIPs/pull/8662)


**Alex Stokes** [6:19](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=379s): Okay great. Next up Tim I think had an announcement around adding some Nonce to CFI in the EIP process. Tim if you just wanted to give a quick shout out. 

**Tim Beiko** [6:34](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=394s): Yeah so we discussed this on the last ACDE but there was a proposal that came out of Kenya that was to basically improve how it Define CFI and also add a formal way for the community to propose the EIPs to hard forks and then just rename included the scheduled for inclusion before stuff ships because we sometimes remove some stuff that's been marked as included. So if people want to yeah review this async that'd be great. And then hopefully by the next ACDE in like about a week we can just move forward with some version of this as official. 


### 1. Electra
#### Devnet-1

**Alex** [7:20](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=440s): Cool thanks. So next up is Electra and I think the next up that is on everyone's mind is going to be devnet 1. There's a spec floating around for the EL set of EIPs. I don't have that handy right now but we can discuss the CL set of specs and that's generally going to be the alpha 3 release. So I just dropped a link in the chat here. And I think it's pretty ready to go shout out to Hsiao-Wei for assembling all of There was one open question I think on this PR 3768 before we get into that is there anything else around Devnet 1 that people would like to discuss as this more like higher level or should we turn to just these few open questions for the specs. Okay so right let me grab the link let's see it's three yeah this one. Okay so 3786 this PR is really just changing the layout of the fields in the new attestation type that we have and it looks pretty simple.There's some implications just around how SSZ works and how these things are laid out. So that was kind of a I think the original motivation was to not break essentially these indices that come out of the merization yeah. And so this PR suggests moving this field basically to the end. The way it works is like appending things is much nicer than putting stuff in the middle in terms of the layouts. Yeah so it looks like there's been quite a few approvals on the PR. Does anyone have any comments about this. I think I do. At least just because we do have this pattern that the signature of a thing comes after everything else and this kind of breaks the pattern. So it feels at least aesthetically wrong to me but yeah no one else is really chimed in otherwise. So if there are any comments here now would be the time to walk through them. Otherwise I suppose we can just go ahead and Merge this. Yeah Cayman? 


**Cayman** [10:00](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=600s): Yeah I just wanted to note so if we do end up approving like a stable container EIPs that if like in the future like stable containers kind of require us to append only. So in this case this is not a stable container this just a normal container but that's just something to keep in mind that like even if it's something that has a signature kind of by the rules of the EIP that we're setting forward you would we would still be appending in that case. 

**Alex** [10:35](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=635s): Okay yeah that's good to know yeah anyone else have any feedback on this PR. It sounds like I might be in the minority on the field ordering. So I will defer to everyone else in that case.

**Etan (Nimbus)** [10:53](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=653s): Like you mentioned the pattern of signature last. I'm not sure if that's still the case is like the way how it's done now is that there is this envelope that has like the payload and the signature and it's just these two things combined. And the only thing that keeps changing is the payload right. So it's a bit weird in the attestation because the signature is actually not signing over all the fields. It's only signing over the attestation data but it's not signing over aggregation and comedy bits. So I'm just wondering if this pattern that you mentioned like where is it actually being used like the signature loss. 

**Alex** [11:43](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=703s): Like everywhere like i the an ssz type we have where you don't have like a bunch of stuff and then the signature like I don't think there's any like I guess that's my point here is like this would be breaking the pattern and it is arguably just aesthetic. So again you know this is not the end of the world but it definitely sticks out to me. Kasey was asking why did we put the signature last originally and I think it was again more just sort of like an aesthetic thing. Justin has a comment typically RIP you need to read out the data that is signed over right/ Yeah so yeah you could if you're doing some like streaming SSZ thing, then yeah you could kind of argue that it's helpful for that. Yeah I mean I think it's really just a pattern that we kind of settled on and I also don't think we've broken yet. But yeah that being said I think we should ship Devnet 1. So unless there's any other objections we can go ahead and merge this after the call. 


**Radek** [13:10](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=790s): Sorry I don't know how to raise my hand in Zoom but I think this is not something that we can do without breaking things but  what if we had attestation data signature aggregation bits and committee bits that way  signature would come after the stuff we are signing. And then we'll have the rest of things. 


**Etan** [13:36](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=816s): It  would also be fine but we should only do that if we adopt the stable container because right now like aggregation bits is generalized index four data is five signature is six and commit bits is seven. So four five and six like this PR what it achieves is that four five and six stay the same. So aggregation bits is still four data is still five signature is still six. If we adopt a stable container then these indit has break anyway. So we can use that as an additional reordering but yeah I mean it would make sense to to put the aggregation bits after the signature because they are not being signed over anyway. 


**Enrico** [14:40](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=880s): It's safe to say that we can go for it and then if stable container become real thing we can think about reordering the last time. 

**Etan** [14:50](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=890s): Yes like if we adopt stable container we can reorder everything because like the rules break. 

**Enrico** [14:58](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=898s): Yeah.

**Stokes** [15:12](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=912s): Okay sounds like at least on a call we have support for the PRs.. So yeah let's ship it okay I think that was the big thing left on the specs release is there anything else that we should discuss right now. Otherwise the plan I think is to get hear out later today or tomorrow. And have that be done that Devnet 1. I think there was something in the chat okay Pari link something here in the execution APIs. Let's see okay maybe can someone from the EL speak to EL consolidations being ready to go. PR that one. No one knows I think that Mikhail is yeah either Mikhaill or Lightclient working on that and I think they're both out this week . So okay we can follow up on that one after the call and otherwise yeah I think we are in a good place for Devnet 1 with CL specs. Next up I wanted to touch on timing if any CL team is here have you started implementation on this release do you have any sense of like devnet 1 timing. I think it'd be helpful for everyone to kind of start coordinating on what time we could see the devnet up. 

**Enrico** [17:22](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1042s): Yeah I can speak for Dencun. We are waiting for the attestation field to the end to be merged but we have the PR already prepared and ready for merge. And the other thing that we are waiting for is this 3783. We haven't start doing anything there but it's supposed to be not that. So as soon as we have that merged. I think we're kind of safe to having clients ready in days. 

**Gajinder** [18:09](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1089s): And for Loadstar we will basically integrate consolidations as the spec gets finalized and then I think with small amount of changes we should be ready for devnet 1.

**Sean** [18:34](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1114s): For Lighthouse I haven't really gone through the new spec changes but I think we should be in good shape for devnet 1.


**Stokes** [18:47](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1127s): Right so is everyone thinking like weeks or many weeks or we don't know it's fine if we don't know but people have been asking?

**Gajinder** [19:06](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1146s): I mean if spec is sort of finalized then by end of next week.

**Stokes** [19:15](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1155s): Okay.


**Saullius Grigaitis (Grandine)** [19:18](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1158s): Yeah so from Grandine side we also didn't look for latest changes in the spec and we're actually waiting until it's fully finalized but but the rough estimate something like a week or two for us week or two after the spec is finalized. 

**Enrico** [19:44](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1184s): Yeah we would like to have a reference test to run or against consolidation stuff. So code is there but yeah once we got some reference test to run everything over we get some more confident but yeah we are kind of in the next weekish.   


**Stokes** [20:08](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1208s): Okay great. James I think I saw you on mute I don't know if you're going to give a Prysm update. 

**James He**[20:17](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1217s): Yeah we have a couple but still waiting. I think just like everyone else probably like a week or two.we'll need to reform a new devnet 1 branch. 

**Stokes**[20:38](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1238s): Cool and I think that leaves Nimbus. I don't know if anyone from Nimbus is on the call Dustin.

**Dustin** [20:46](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1246s): Hey sure yeah we haven't looked at this in totality. Let's say in terms of devnet 1 Readiness and in a lot of detail that said I mean I didn't see anything in to Waring in it. But what I would certainly Echo is I would want the tests the consensus spec tests in place but aside from that.

**Stokes** [21:19](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1279s): Okay cool. Right so specs are on the way. Hopefully in the next couple days and then it sounds like people are thinking small number of weeks for Devnet 1. So that's super cool.


**Gajinder** [21:39](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1299s): I think for Devnet 1 EL implementing 7702 would be sort of the key Milestone that would need to be achieved.


**Stokes**[21:55](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1315s): Sorry what was it. I missed that.


**Gajinder** [21:59](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1319s): I think for the devnet  run we want 7702 on the EL side right 


**Stokes** [22:08](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1328s): Yes this is the yeah this is the account abstraction one. I don't know if we landed on that being in.

**Paritosh** [22:20](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1340s): Yeah we did that was the main change between 0 and 1 and I think Radek said they weren't ready with it yet but potentially next week and besu said they'd have it this week we haven't gotten updates from the other EL teams yet but we'll follow up and you can keep an eye out in the Interop channel. 

### PeerDAS
#### PEERDAS_ACTIVATION_EPOCH recap


**Stokes** [22:44](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1364s): Cool. Okay so it sounds like we have a pretty good plan for Devnet 1. Anything else there otherwise I think we'll move to PeerDAS. Cool so right PeerDAS. So I kind of just wanted to reiterate the thinking around having the separate activation epoch to kick us off. The way I was looking at it is
that basically there would be this separate Epoch to activate the feature set and the idea is that you know we could theoretically imagine having pectra ship with some delayed peerDAS within sort of the same Fork as pectra. That sounds really complicated and I really don't think we should like if we think peerDASs ready to do that. Then we should just ship it with the fork right. So I think the plan was generally to say okay either this activation epoch will be equal to pectra or it won't be meaning it would be delayed until like the next hard Fork. That then means that it gives us room to implement peerDAS as part of Pectra sort of on top of Pectra. And then what do we gain well we gain not having to like have the separate hard fork with all the code infrastructure to implement that. As we go and sort of develop things these things in parallel. So that at least is how I was thinking about it. I don't know if anyone has had time since the last CL call to like think about this some more or if there are any issues kind of with that approach. But that's how I was seeing It. Barnabas says developing in parallel doesn't sound like a thing if it's built on top of Pectra. Why not? 

**Gajinder** [24:54](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1494s): I think in the PeerDAS breakout call we decided that we will continue doing devnet 1 of peerDAS on top of deneb and at a much latest State we'll basically see whether we want to we want to Revisit on top of electra but I think the plan for now is to just continue doing Devnets on top of deneb. 


**Barnabas** [25:26](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1526s): We had a agreement on how this Fork should actually be activated though. And every team seem to have a different opinion on this. So it would be very good to make an actual decision whether it's going to be a hard fork or whether it's going to be a CL only fork basicall. 


**Gajinder** [25:50](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1550s): I think on this  following the discussion that has happened on R&D Discord basically it doesn't matter whether it's hard fork or not or if it's for activation Epoch as long as the fork question doesn't change. So for our clients may try to implement it anyway they want if they can sort of guarantee that PeerDAS Fork version is same as whatever was on the previous Fork. So basically I think we
are following the approach of activation epoch only But yeah the clients who still want to use their hard fork Machinery can do so by keeping the fork version same. 

**Mark **[26:44](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1604s): So did you say well I don't see much of a point in building it on top of deneb though. You said that's like I don't know there's no plans as far as I can tell to push PeerDAS before Electra.

**Syokes**[27:04](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1624s): Yeah what was the rationale there I can make the break out. 

**Enrico**[27:07](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1627s): I  guess it's just because they don't want to be following the spec changes of Electra having more stable spec that they can focus on PeerDAS and when Electra spec solidifies more than they can rebase on top of electra. That's my impression.

**Gajinder**[27:28](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1648s): Yeah is pretty much orthogonal to Electra and I don't think basically basing on top of Electra is going to be a challenge at any given point but yes rather than spending time on the Cycles now. And sort of getting entangled in the Electra development. I think we can keep PeerDAS sort of orthogonal from Electra as of now.

**Paritosh** [27:53](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1673s): Kind of mirroring that point from testing as well, for example if we do merge the two branches and we're testing PeerDAS specifically. And there's a bug in Pectra we might actually trigger the bug purely because the branches are changed and we're going to have to spend Cycles figuring out if it was a Pectra bug or if it was a peerDAS bug. As opposed to if it was starting from Deneb then at least then we know with most certainty that's a peerDAS bug.

**Stokes** [28:23](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1703s): Right. Okay I mean yeah it sounds like the tradeoff here is like either we have like sort of more upfront development complexity by putting it on top of pectra or yeah we can kind of focus more exclusively on peerDAS by living on top of deneb with the implication being that sometime down the road we will have to rebase on top of Pectra. That sounds okay to me for now I mean it yeah I guess the tricky thing would be if we're like 6 months from now and we're still on top of the and then it's
like okay are we going to ship this or not. But also it doesn't seem like that's a huge issue. 

**Gajinder** [29:06](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1746s): Maybe devnet 5 onwards we can sort of Rebase on top of Petra devnet 5 of Petra I assuming the devent will go till devnet 10. 

**Stokes** [29:19](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1759s): Okay. Why 5?

**Barnabas** [29:21](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1761s): Why 10?

**Stokes** [29:24](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1764s): Yeah I don't know if we can put numbers to it but.

**Gajinder**[29:28](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1768s): I mean just from
the past experience that the amount of testing cycles that we give to a particular fork and assuming pectra has so much stuff going in so just a hunch. 

**Paritosh** [29:41](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1781s): Maybe a good time is to say once we are sure what's going in Petra and we sort of have a feeling that things are stabilizing. That's when we can talk about when the fork is going to be shipped and when we start merging stuff. 


**Stokes** [29:59](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1799s): Yeah I mean if everyone thinks this a blur. I think that sounds like a good path forward for now just having PeerDAS on top of Deneb and then you know maybe even as soon as like a month or two from now. We can revisit the rebase.


**Barnabas** [30:24](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1824s): How are the client team's feeling about PeerDAS by the way. PeerDAS Devnet 1 when could we launch that. And would we need any spec change or is everyone happy to keep all the same flex as it is set right now. 

**Nishant** [30:44](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1844s): For Devnet 1 what are you planning to test is it the same stuff?

**Barnabas** [30:57](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1857s): Yeah, I guess so. There hasn't been many PeerDAS to the consensus packet as far as I can see. 

**Nishant** [31:06](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1866s): Okay yeah I think it should be good on our end. So we would definitely like to test reconstruction in general to see how it works across the network.

**Saullius** [31:22](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1882s): Alright. Yeah I would suggest to think about peerDAS Devnet 1 when we have a quite stable Network which doesn't split in Kurtosis setup. So I think it's it's still not there or or there is some Kutosis config that has like three or four clients that can keep on the same chain for a long time/ What is the current state of PeerDAS can somebody comment on that because on in the interop we ended up
with a network that was splitted to I mean every point was on sound for as far as I remember.

**Gajinder** [32:14](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=1934s): I think in my assessment nodes need to make sure that they are consistently custoding the data columns that they are supposed to even if they restart and that was one of the big reason big reasons basically loadstar was not able to sync. Devnet 0 I mean it was able to sync for a few Epochs but then it would hit into this particular problem that the columns the notes that should should be Custodian they didn't have it. And so most likely it could also be the reason for the split. Otherwise I don't really see I mean in the fork Choice was simple that it is the availability is was same as that we have on blob. So ideally there should not be any other reason for the fork split  in the nodes. But I think this this could be the reason for it and if sort of we can make sure and have the stability around this then I think we should be ready for devnet 1. 

**Saullius** [33:26](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2006s): Yeah but we can test that in Kurtosis. I mean it should be possible to make a Kutosis config that that has a few clients with the issues that you mentioned fixed and if the network is stable there then I think we can think about the devnet one peerDAS. That's my opinion.


**Nishant**[33:53](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2033s): So in interop I think the devnet images that were running they were all images which is why clients split. So we had a few bugs on our end that we fixed but it wasn't deployed to Devnet 0 but yeah before devnet 1. We can you know run a Kutosis setup with all the clients to see how it works. 


**Barnabas** [34:23](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2063s): The client teams just put their latest Branch their peerDAS branch in interop. So we have a good idea of like which branches we should be using on devnet 1 and on Kurtosis as well. And what is the status on peerDAS with loadstar because they didn't participate in the previous Devnet. Do they have something ready?

**Gajinder** [34:56](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2096s): Yeah I'll share.

**Stokes** [35:16](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2116s): Okay so should we is it worth thinking about timelines for peerDAS and Devnet 1 then like do we want to try to say okay aim for something in like a month. Just to give people like sort of a deadline to work towards.

**Mark** [35:34](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2134s):  Not that I want to accelerate things but it seemed like people felt like two weeks as a gut feeling was all right could go three if  you want to give more time or whatever. I mean a month it should certainly be fine but depends on how fast we want to go.I mean yeah sooner it's better but I'm not sure people are I think most people felt like two weeks didn't seem crazy but correct me if I'm wrong.

**Gajinder** [36:01](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2161s): Yeah two weeks and of the month I mean that sounds fine. 

**Stokes**[36:08](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2168s): Okay so let's aim for that and then yeah we can run a devnet and I think that'll give us a lot more clarity on the next stops. Sound good to everyone? 

**Saullius** [36:22](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2182s): One more suggestion I would like to do is maybe Barnabas or some someone else from devops teams could or maybe this already done could could find at least two pair of clients that interops correctly. So this would help for the rest of the teams to you know to take these reference to clients and interop with those two clients that almost sure that are correctly working. So maybe it's already known that there are two clients that interop very stably is it the case or it's unknown that there are two pairs? 

**Barnabas** [37:17](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2237s): We haven't been testing lately because there has been just development so as soon as at least one of the clients say that their branch is ready to go then we can start testing. But without anyone saying that they are ready there is no point.

**Saullius** [37:33](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2253s): Yeah but it's kind of chicken egg because for example for us we really would like to have a two clients working together. So we can join it and it could be that the other teams feel quite similar or at least some teams.

**Barnabas**[37:53](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2273s): Does grandine has a working implementation you think? 

**Saullius**[37:57](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2277s): Yeah no I mean the the idea would be if there are two teams that are quite confident that they are quite done with PeerDAS. I mean given that it's still early stage but that they believe that they should have everything to interrupt then let's get these two teams to make Kurtosis setup that is very stable. So the rest of them could join. That would be my proposal. But do we have these teams that are very confident about their PeerDAS implementation? 

**Sean** [38:45](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2325s): So I'd have to check with Jimmy because he's been doing most of PeerDAS work in dapplion but I think Lighthouse has a pretty solid implementation if I'm following things correctly? 


**Saullius**[38:58](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2338s): Okay is there any is there a second one that feels similarly. 

**Manu** [39:05](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2345s): Yeah Manu. Okay can say for prysm we are quite confident about peerDAS as well.

**Saulllius** [39:16](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2356s): Okay so Barnabas just take Prisma and Lighthouse and try to make a stable Network and if it happens then I think soon we will have a devnet 1. 

**Gajinder** [39:34](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2374s): One thing I want to know that the PR regarding specifying the block count through on the FCU patterns and the associated change for it on the EL block header for adding block gas limit that is part of Pectra or is that part of peerDAS and I guess it will be part of pectra if this is not really a Fork.

**Stokes** [40:10](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2410s): Sorry what were you asking about?

**Gajinder** [40:13](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2413s): So your PR regarding  adding Max blops per block to the FCU pattern. So is that PR part of Petra or is that
PR part of PeerDAS? 

### Inclusion in Pectra Meta-EIP


**Stokes** [40:30](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2430s): Yeah so that was next on the agenda. Do we feel good about devnet 1 just in terms of development timelines. I mean sounds like people are on top of it when clients are ready. We'll start testing soon and then we can move to the Blob count conversation. But do we all feel pretty good with the devnet one plan for peerDAS? Okay I got at least one thumbs up I got two. I'll take it, let's see here. So well okay there was actually one quick thing before we get to the blob count itself. Tim, let's see. Tim has a draft PR here for including PeerDAS into Pectra and yeah this kind of starts to all touch on the same thing. Tim did you want to say a few words about this because I think there was some novelty around the pr and our usual EIP process.

**Tim Beiko**[41:38](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2498s): Sure so yeah I had the reason I kept that as a draft is it just felt a bit. So PeerDAS as it spec is currently a networking change and not like a core protocol change but at the same time. It's literally the biggest feature that we have going into pectra. So it feels like we should include it and then you know the activation stuff we can add to the Meta - EIP later. But I guess anyone think we should not list it in the Meta-EIP and if not I'll just merge this now.

## Proposal to uncouple CL and EL around blob count: [Specify the max blobs per block with each payload consensus-specs#3800](https://github.com/ethereum/consensus-specs/pull/3800)

**Stokes** [42:12](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2532s): I think we should because it just signals that we're serious about this and we are. Okay cool let me go check the agenda. Okay yeah so I think we kind of covered the PeerDAS things themselves. And then the next question then is like yeah somewhat how do we actually ship this do we increase the blob count?  How is it all Roll out and all these things? So Gajinder was just talking about PR I had to suggest a way to have the CL Drive the blog count. I don't know if people have had a chance to look at it but the motivation was essentially to uncouple. Like so right now there's basically a hard coded constant both on CL and EL for the Blob count. This couples together the layers and so it kind of makes things a little less flexible in terms of us having these like shipping timeline discussions and you know Fork scoping and all of this. So it would be kind of nice if we can uncouple them. You could then theoretically have a CL only fork where you know if we want to change the blob count independently. we wouldn't need to update all of the execution clients but just the CL Clients. So I think there's a good reason you know there's a good motivation for doing this and the question is just how would you do it.The suggestion that I have in the PR right now is basically just to send it over with every payload so whether you're like validating a payload or building a payload the CL would just send it as part of the parameters that already exist to tell the EL hey for this block there can only be this many Blobs. The catch here now is that this kind of breaks optimistic sync because the EL can be in regimes where it basically can't talk to the CL synchronously like this. And then it might not know what the Blob count should be. So yeah the question then is like what do we do about this and yeah I think Gajinder maybe Terence there's some conversation on the Discord around this but the suggestion was basically to actually include the blob count and some representation in the EL header which does I think nicely solve all these issues. Yeah has anyone had a chance to look at this PR or think any more about this.

**Dankrad Feist** [44:55](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2695s): I mean, I think not knowing whether it's valid for optimistic sync isn't a problem per set like you can simply accept like whatever you're told it is and then like verify it once you get the beacon block. I think the only problem is that you need to know everything in order to be able to compute the block
Gas. I think that is the problem that approach. so as long as you can do that I think like it doesn't matter like you don't have to care about optimistic sync.


**Stokes** [45:33](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2733s): Right but then you like that suggesting that it does have to go in the header which is I think at least it's a different type of change. Which is fine. But that just needs to be something that then all the execution clients with. 

**Dankrad Feist** [45:49](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2749s): Yeah I tried to think about that as well and it is like a conand how to do that part. I mean the optimal way would be to change the computation. I think it's probably a mistake that block like the gas Price computation happens in the EL like that should have been in the CL. But yeah that's more difficult to change now. I guess.

**Stokes** [46:15](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2775s): We could but I think you didn't have the same issue right it's just more about communicating the information at the right time and the blob count and the blob gas are kind of the same thing.

**Dankrad Feist** [46:27](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2787s): I mean one thing you have to remember as well is if you actually want to change the blob count there is a computation that has to happen to update the excess gas as well. Right. I guess that works automatically if you do maybe the easiest is that what you suggest. Yeah like adding the blob count see would solve that because then you can just keep track of the excess gas. Except that the unit changes right because like when you have more blobs the constant you want to divide by
Changes. This is actually like yeah it's not this is not easy this is why it would be easier to have it in the CL because then it would be part of the part of the fork like in the fork you would just all recompute all the constants whereas if you have it in the EL then there's like a some weird backward math to figure out what the right excess gas and what the right EIP 1559 devisor is. 

**Stokes** [47:52](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2872s): And this is just at the fork boundary when we changed the blob count is that what you're referring to?


**Dankrad Feist** [47:59](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2879s): So there's basically right now right the gas cost is computed as like an exponential of like the excess gas divided by this blob gas Fee constant. I can't remember what it's called. And whenever you change the number of blobs you have to adjust both of these numbers as well. Because they will be like first the constant changes but that at the same time means that the old excess gas is no no longer in the right units either because it was measured in terms of the old constant essentially. 

**Stokes**[48:39](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2919s): Right. Yeah okay that makes sense.

**Dankrad Feist** [48:42](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2922s): So,  okay the more the better way would be yeah if if there is an easy way. I I'll have a look at this later if there isn't is a way to transform the whole thing. So that all the gas computations happen in the CL.  then this is actually more elegant because then it's just part of the Fork boundary right which we'll have anyway as far as I understand. For we have a blob in the EL there's actually no such thing because for the EL we want it not to be a fork. Yeah so this could be easier otherwise we can figure out another way in which the CL messages the EL about the change in those constants but they is need it to.

**Stokes** [49:32](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2972s): Right Ansgar? 

**Ansgar** [49:36](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=2076s): Yeah just to mention if we want to keep it in the EL then one way to get rid of that annoying discontinuity where basically you need or thing where you basically need to make an update to that excess gas at the fork point. You can basically just accept that you will have a discontinuity in the base fee. So basically if you say you double the blob count then then basically base you would have but there's only it's like a 5 to 10 minute period until you basically you're just for for a few minutes you have cheaper blobs and then you're back to the same price these adjustments are very quick and it's a little inelegant but that would turn that those constants back into pure functions from the count Blob count. So that if you communicate the count the blob count then you can compute the adjustment ratio you just cannot compute the you just kind take that you would have to do this one time update to the excess gas. 

**Dankrad Feist** [50:38](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3038s): The constant like the one in the exponential but I assume you just want to make that a function of the blob count? 

**Ansgart** [50:49](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3049s): Yeah exactly that one can be a function of the blob count because you don't have to detect the fork itself it's just basically always some constant ratio. 


 **Dankrad Feist** [50:58](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3058s): Right that is I mean that's probably the simplest solution the question is it the most like is it the most elegant solution. I guess.

**Stokes** [51:16](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3076s): Okay so there's two things here like we kind of started talking about just how to communicate this generally if we took the data away from the EL and then having it go from CL back to the EL. And then also now we're talking about you know if we do actually change the blob count there is going to be this discontinuity with how we compute the actual blob Base fee. And that needs some thought as well. So yeah what I'm hearing is that this is not that simple to change. But I do think it's worth changing. So yeah I would suggest people take a look at the PR and then yeah this has all been good discussion and from there we can try to figure out another path forward if anyone wants to take another look at yeah maybe even a more invasive change to move more of the computations of things into the CL that would be great. And I think we'll just kind of keep turning on this. 

### How to raise the blob count?, EIP-7623

**Stokes** [52:24](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3144s): Cool so yeah I think we've kind of covered a number of the PeerDAS things on the agenda that I had here the other big thing is just actually how do we raise the Blob count and how all of this is this a conversation anyone is Keen to have now and the general you know the intent is to raise the Blob count in pectra. Obviously the question is how much and you know is it coupled with peerDAS. Is PeerDAS coupled with pectra like I think there's a lot of uncertainty here still. But yeah I don't know if anyone has any thoughts or updates on this we're sharing right now. Yeah Tony had a comment here we also want to be mindful of the worst case block size if we do raise the blob count and this calls up EIP 7623. I believe is a number? That's more of an execution
layer change but also worth calling out here. Otherwise yeah from the data I've seen honestly it looks like even already weaker nodes on the network are having issues with the current Bob parameters.  I had a document where I was talking about the uncoupling of the CL and EL with respect to Blob count that we were just discussing. I also suggested another feature essentially where you could like customize your local Blob building to help with this issue. I think these are all things we want to keep in mind as we move forward and yeah I think otherwise at least where I'm at right now is just having more time to have more data analysis around how blobs are actually going on Mainnet. It seems a little bit early to me to say oh yeah we definitely want to go to like 816 or like some concrete number. Especially without seeing how the perrDAS and Devents go and all of this. Ansgar?

**Stokes** [54:28](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3268s): Yeah I think that makes sense I just want to briefly like that in the chat we had a conversation quite a while and there were some people under the impression that we basically did not specifically did not want to increase the the Blob count at all doing pictor just because it would add quite a bit of testing overhead . And other people that were very adamant that we actually should really increase the blob count. So I would just want to flag it as a topic where we will at some point have to have the conversation and neither side should fully assume yet that decision is made either way.

**Stokes** [55:01](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3301s): Yeah definitely I mean I would say if peerDAS is ready with Pectra then we would also raise the blob count just because of the demand. So I think that's understood at least hopefully it's understood.


**Paritosh** [55:20](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3320s): Isn't that starting to get a bit risky though because we don't actually know how peerDAS will play out on Mainnet.

**Stokes** [55:27](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3327s): Sure so they conditional on peerDAS right. I mean I don't know like so that does raise an intermediate stop that I think Fresco is calling out in the chat just now like we could imagine well that's the thing there's a couple things. So like one option is we should peerDAS leave the blob counts alone again. I think if we're confident enough in peerDAS to ship it. Then we're probably also confident enough to raise the blob count. We could also just yeah we could ship here to us and not raise the blob count we could just raise the blob count 4844. I think that's probably not as preferred to everyone but that's an option. And yeah so there's many things to work through here. Barnabas?

**Barnabas** [56:10](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3370s): Just because we are confident enough to Ship peerDAS that is not give that's not going to give us confidence to increase the blob count though. That's not the same thing 

**Stokes** [56:22](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3382s): I agree.
 
**Barnabas** [56:26](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3386s): Because that's what you just said like one minute ago that if you have enough confidence in shipping peerDAS then we have the confidence to increase the Blob count as well. But those two are completely different things.

**Stokes** [56:38](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3398s): They're pretty different I mean I would hope we get to a place where we have confidence in both that like one implies the other but yes I agree with what you're saying.


**Barnabas** [56:49](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3409s): The point is we have so many EIPs and I feel like we just keep shoveling more and more and more into it. And it's just never going to end. So we we'll have to draw some line somewhere where we say okay this is where we're going to end it and I think shipping PeerDAS and an increased block count in the same Fork case is just not something that we can do in like the next year and a half testing wise as well as all the other EIPs that we have included as well.


**Stokes** [57:27](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3387s): Yeah I mean I don't know how valuable it is to have a Forks grouping conversation today but you know I think if we get to that point and it becomes clear in a few months then that motivates splitting peerDAS into a different fork or yeah rethinking Pectra. Francesco?

**Francesco** [57:46](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3466s): Yeah just wanted to point out something which I think Ansgar already mentioned in the chat that like the blob count means something quite different with peerDAS. So I mean this doesn't mean that necessary we can feel confident having I don't know like 6 or 8 or whatever like Target. But it doesn't mean that we can't really just say you know we are okay with a blob count of three because  we know we've seen it in mainnet that like it means something different in peerDAS. Like it's throughput that I mean the bandwidth that you need to handle 36 is very different in peerDAS. It would be like much less. So yeah I don't think they necessarily this seems a bit of like a bias there of like you know we ship peerDAS without doing any change to blob count then we can feel confident that it works. But that's not really to me that's not really necessarily the case. It doesn't mean that like you know, necessarily we should increase it. But that that's one thing to keep in mind and also another thing is I think if we're not willing to do that which I can understand there's like I agree there's there's a ton of EIPs. And things going on and it's hard to test all of it but if we're not willing to do that what benefit are we actually getting from doing PeerDAS with Pectra if that's and that ends up being the case like at that point. Does it not just make more sense to drisk the whole thing just do Pectra without PeerDAS. Just do commit to doing peerDAS as its own Fork like much before verkle. Because I think the only really like stupid outcome that we should avoid all cost is trying to like tie peerDAS and with a blob count increase to like some Fork we in the future. Like that's like really the only outcome that's just like to me unacceptable.But other than that like you know whether we do peerDAS in January or like April or whatever like I mean doing it earlier without Blob count increase to me like just doesn't really add that much. 

**Stokes**[59:47](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3587s): Right I mean it would give us evidence on mainnet that peerDAS is working like we expect right. So like it does actually the shipping peerDAS. 

**Francesco** [59:57](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3597s): But it also increases risk to everything else and like to the whole Fork.

**Stokes** [1:00:01](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3601s): Well I think that's a different conversation and that's where this starts to get tricky is yeah like aligning pectra timelines with peerDAS timelines Blob increase timelines. Paritosh?

**Paritosh** [1:00:16](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3616s): Yeah so the one point I do want to bring up is like we're talking about testing but the issue is that testing networking is extremely hard. We did do a lot of 4844 related testing but the way blobs played out on mainnet is not a one to one analog to how it played out in testing we do see beaconr nodes having issues. We do see timing games being played and stuff like that and that's the main reason why even if we can simulate a perfect world in which peerDAS along with the blog increase does work in all of our Devnets it doesn't actually mean anything for mainnet. And
that's my main argument for why we should probably do things step by step rather than than all at once because just testing doesn't mean anything here you know. 

**Stokes** [1:01:05](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3665s): Ansgar did you have your hand up for.

**Ansgar** [1:01:08](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3668s): Yeah I just wanted to yeah I just want wanted to to briefly say that to me really like this point that is super important that like the meaning of blobs already changes and PeerDAS. So I don't even think it makes sense with PeerDAS to call it a blob count increase because we have to pick a new number of blobs for peerDAS anyway. Even if we happen to go with this kind of 3-6 that we also have today that doesn't mean we can actually reuse anything. I mean maybe like a tiny sliver of el side logic around the gas computation but that's the easiest part anything else changes anyway and then I don't know specifically why mainnet might break under say I don't know 816 or something but it would not break under 36 it could also break under 36. And so the only World in which I see that there's any reason to stick to as a default to the values we have to have in a peerDAS world would be if we ship peerDAS with some sort of fallback mechanism to disable it if there are issues and fall back to the existing version but that seems so incredibly complex including for fork Choice implications. That I don't think it's realistic to ship it that way. So if we already ship it as its own standalone thing that has to not break otherwise Mainnet breaks. Then I don't see why 36 would have any more value as a default than any other other count number we could I just want think calling it an increase makes sense when we have to pick a completely new number anyway for peerDAS.

**Paritosh**[1:02:34](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3754s): Actually Franchesco I think said something earlier that made a lot of sense if we are moving to a paradigm in which the CL is setting the blobs. We could potentially increase the blob count and we already have this mechanism with the circuit breaker where if we see a bunch of Miss slots in a row / non finality / a lot of other circuit breaker conditions that we use for MEV. We could reuse that same circuit breaker conditions for blobs as well. 


**Mark**[1:03:03](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3783s): I think that isn't I don't think we can do that here because all the clients have to be consensus on the maximum blob
Amount and like the circuit breaker rules are not something that all clients
have consensus on and I don't they could either because what they see is
can be different. 

**Francesco** [1:03:26](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3806s): But you could for example just locally say like I'm not going to propose a block with a with more than I don't know two blobs or something if I see that things are not working. I don't know how viable it is but and I mean if someone else does propose a block with a lot of blobs and it turns out that the network is not able to handle that I guess that just get reorg.

**Mark** [1:03:51](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3831s): Yeah I guess but you know if you see a block with three blobs and your node is feeling like the Network's in bad shape and only two need to like we should only ship with two or something like that. Then you have to reject that block and then what if the rest of  I don't know that seems can you really do that unless we have special rules where it doesn't actually make the block invalid to have more blobs than you expect but that's weird. But I would I don't just want to say second what Ansgar was saying like if we have to pick a number even I mean what if we even just picked a small blob size increase I mean if we're going to test with six with peerDAS. We might as well test with eight and then leave it to some future date to increase it further. That would that seems like a safe option and a small increase.

**Barnabas** [1:05:07](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3907s): What's the point of increasing if it's not significant like why risk of increasing if if there's no actual benefit?

**Sean** [1:05:21](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3921s): I think this was franchesco's point where it's not that we're not increasing from known value if we're Implementing peerDAS to us. We are just like kind of picking a number that we think is right and like yeah lower is maybe safer if we imagine there going to be bottlenecks with upload
download but it's not necessarily like like we don't know anything about the new limits.

**Mark** [1:05:47](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3947s): Also eight is a power of two just say.

**Stokes** [1:05:51](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3951s): So we can Target the same amount of bandwidth right like we can do that calculation and we can know that with perrDAS you know the Blob count might change but it's going to be the same amount of bandwidth. So that's like a good starting point. Yeah Francesco?

**Francesco** [1:06:11](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=3971s): Yeah just I mean I don't know how meaningful this is but just to give everyone like a very very rough idea with the current parameters in the spec for a validator you would be using basically like if you're like a really low power validator that's running like one or two or like a few. Then you would be using roughly like 8X less bandwidth for the same amount of data. So you know maybe we don't increase the block count by 8X but like maybe safer to increase it by 2X or something like tha. And as a full Node even it would be even less like you'll be using 1/16th. I mean of course we should like actually confirm these numbers on testnets like compare you know for the same amount of blobs what what are what is the bandwidth usage from 4844 versus PeerDAS but in principle that's what it should be.

**Stokes** [1:07:08](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4028s): Right so you know seems like there's plenty of head dargue for a double but yeah I don't know I think at least I would hope we're going to have a better understanding of how this stuff works you know once we have Devnets that are running and PeerDAS is actually live. And then hopefully the conversation is a little less uncertain. 

**Mark** [1:07:28](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4048s): And I guess I sorry I me to jump. But I just want to say like if the problem is that we're putting too much in the fork like I just think the blob increase and peerDAS are something coupled like changing the blob size by a little bit compared to the other things that we're putting in this Fork is such a small change if you already assume that PeerDAS do is going in. If we have to pull things from the fork I wouldn't I don't I don't think a configuration where pectra ships or where peerDAS ships and the increase doesn't ship makes sense I think we would pull something else.

**Stokes**[1:08:10](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4090s): Enrico? I think you hand up?

**Enrico** [1:08:13](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4093s): Yeah just a comment because we are saying that we are going to the peerDAS activation epoch in Electra. It means that peerDAS will activate later. So it's weird that we get a blob increase and then the peerDAS do activates just later. So picking up the right blobs count at Fork seems weird to me unless we increase the blobs at peerDAS activation which is a different story. Sowe end up not increasing enough because we have to cover first month of non-peerDAS activation and we don't get the full benefit of the right number of blobs that we can support in peerDAS which is weird.

**Stokes** [1:09:25](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4165s): Right and you're just referring to having like some delayed activation of PeerDAS. 

**Enrico** [1:09:32](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4172s): Yes in I mean the moment of if we agree on the delayed activation of the peerDAS.

 **Stokes** [1:09:40](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4180s): Yeah I don't see why we would ever do that myself because it just seems to complicate what's already very very complicated. I think we either ship PeerDAS with Pectra or we don't. Basically  because otherwise yeah it's just's going to add even more sort of huge decision points on top of something that's already quite complex. Yeah Dankrad?

**Dankrads**[1:10:09](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4209s): In terms of The Blob count. I think it's also not crazy to think about what if we just do the same as with call data and make validators just vote on It. I mean it's working there's no crazy increases and it allows us to change it without a hard fork. Because I think largely in the end like the way it's always work with gas the gas limit is that the miners and other the stakers just like listen to the core devs what they think is a safe limit and then increase it to that. So this would be would allow us more  flexibility in the future.


**Stokes**[1:10:57](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4257s): Right I mean do we ever think we're in a situation where you know people on this call for example want to raise the blob count but then the validators let's say aren't listening. Not because they don't want to but just because you know they don't understand how to like go and change Target limits and all this stuff. Okay so yeah I think we just keep charging ahead here I again I hope that having PeerDAS testnets will give some certainty to or at least some insight into some of these things and hopefully we can. Well I mean we will figure something out. So we just have to keep pushing ahead. Is there anything else on PeerDAS or Blob counts or anything like that otherwise we have an SSZ update. Okay Etan I think you're driving this would you like to give an overview of the latest there.

### 4. [SSZ update](https://github.com/ethereum/pm/issues/1084#issuecomment-2191282230)


**Etan** [1:12:18](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4338s): Sure so progress has been going well Teku has joined the SSZ 7688 devnet as well that's the CL one with the stable containers for all the data structures in consensus that keep changing across Forks. Last time Grindine mentioned some questions about type systems. I'm not sure if those are resolved  otherwise I think we can just give it a brief discussion?


**Saullius** [1:13:02](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4382s): Yes so for us we we think that we will go with the approach where will try to keep the types that we have the type system in generally that we already have in the application. And we just trying to to build something like meta structures or so that would accommodate functionality required for stable
containers. so that's the current plan for us but the implementation we have it's not finished and I think we will tell more after it's done.

 **Etan** [1:13:43](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4423s): Do you see any blockers like same goes for Lighthouse and prysm like is there something that we should know about. 

**Saullius** [1:13:51](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4431s): At the moment for Grindine we don't see blockers but you know as the rest environment is quite restricted and not too flexible I think until we finished we cannot fully confirm you that there are no that there will be will not be any blockers but so far we are progressing. 

**Etan** [1:14:21](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4461s): Okay and from Lighthouse I seen in the chat that there is also no blocker so far. 


**Sean** [1:14:27](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4467s): No.

**Etan** [1:14:29](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4469s): Prysm I think Kasey made some comments on the spec as well. 


**Kasey** [1:14:38](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4478s): Yeah we're still looking into it we should have an update by the next ACD. 

**Dankrads** [1:14:44](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4484s): Okay cool yeah I I think we should Target the next ACDC like it seems that everyone started implementing it and that we could resolve the questions there. And it would be really great if we can have the full devnet with all the clients. So that we can decide if we want this in pectra or not. For remarkable
the implementation in Python that we use in consensus specs. I have pushed that one to production quality. But I'm still trying to get hold of proto Lambda is a bit hard to reach if anyone could ping him about this PR. That I just put in the chat would be great just because we need that in consensus spec to do any tests right. And also a small update on the SSZ Transactions. Ethereum JS has started working on that one and Nimbus has a corresponding consensus client. One question that came up is that right now in the CL we we need to know about all the fields in the EL Block header. So every time that there is a new field and the El block header the CL execution payload header and the EL, the CL execution payload have to be updated in log step. And one thing that happens if we go with the SSZ transactions in the same way is that the CL also needs to know how to Hash the transactions in order to do you know the optimistic Sync and also in order to have the transaction type as part of theexecution payload. So that would be a small restriction for the EL. Because right now they can introduce new transaction types unilaterally without a CL Fork. But with that it would mean that whenever there are new fields in the transaction that the CL also needs to be updated at the same time. The same way how it's already done for the EL block header. I'm wondering if that is fine the alternative that I'm seeing is just to make two trees one with the serialized transactions like the same how we do it today. And then a second tree with the transaction IDs in a list like all the test roots in a list. But that would mean like that we essentially double the amount of hashes that are needed and I mean most of the block is transactions. So a bit suboptimal. So yeah just wanted to point that out that whether that's someone sees a problem with the CL knowing how to merklize transactions and what Fields there are. 


**Stokes** [1:18:20](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=s): Yeah I don't think there really any issues it's just yeah it's it opens a lot of sort of future set things to consider. Yeah but thanks for the update. Potuz you had your hand up.

**Potuz** [1:18:35](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4715s): So yeah I have a horrible connection I don't know how much is I'm cutting up but I think we should probably revisit or evaluate whether or not. We can remove completely the execution payload header for currently there's no in protocol usage of it we only check the block hash. We check against the parent hash in my EPBS Branch. I have it essentially with minimal data removed most of it. I understand that there are some concerns about light clients. But Lightclients currently don't really use the header and they can probably check it on the EL side. I think we should probably think about removing all of this information on the execution payLoad header that we're not using and that would solve also Etan’s problem. 


**Etan** [1:19:28](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4768s): The Lightclient stuff should still be fine like full note that serves that data. It can still inspect the block and construct it right, it's just that.


**Potuz** [1:19:39](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4779s): Exactly so and we are not using at all the execution payload header at all. We can only replace the last execution payload header in the beacon state by just the last block hash. 


**Etan** [1:19:59](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4799s): Yeah in the beacon State yeah. In the Builder API it's still relevant of course but that one is not on chain right. But it's a good point like maybe we can go the other way and make the execution payload opaque as well and then the EL would be the one to.

**Potuz** [1:20:25](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4825s): Yeah that makes the life of us of everyone much better. There are some things that we need anyways even in the Builder API you need the KCG commitments and a bunch of things but it can be reduced quite a bit. 

**Etan** [1:20:41](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4841s): Yeah we can think about that once we have an implementation luckily it's quite orthogonal. So the SSZ transaction it can be implemented on EL. And then we can figure out how we want to like whether we want to add the transaction as well to the CL or whether we want to remove the execution payload. Yeah could you send me that Branch as well like the EPBS branch from the chat a big rule as well. Yeah anyway. So yeah that's the SSZ update for this time. The goal is next ACDC to have the full devnet with Grandine prysm Lighthouse as well. Then we can decide whether to include it and yeah if someone can poke proto Lambda about the remarkable PR. Yeah that's all from my side.


**Stokes** [1:21:58](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4918s): Is this a Pectra Devnet or Deneb or something else?

**Etan** [1:22:03](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4923s): It's an Electra devnet. It's on stabilitynow.box the Kurtosis config is there.

### Research, spec, etc
### F-star naming: Fulu, Felis, ?

**Stokes** [1:22:12](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4932s): Cool nice Work. So we only have a few minutes here at the end of the call. And we did have one more thing on the agenda to talk about the name for the F-Star. I think there have been a couple different suggestions flying around. Sounds like we have some leading favorites either fulu or felis? I don't know if people want to discuss now. I think there's also I'll go find a link but I think there's an eth magicians post for it. Does anybody want to Champion their Favorite?

**Mark** [1:23:03](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4983s): Is there a name for the EL side?

**Stokes** [1:23:07](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4987s): Osaka. 

**Mark** [1:23:13](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=4993s): So it's kind of between like fro saka or fri saka for the combination.

**Stokes** [1:23:21](https://www.youtube.com/watch?v=LpY1JQHl9EY&t=5001s): Fri Saka F Saka probably suggested a Sulu which I kind of like or yeah f saka. Okay well I would suggest going to the eth magicians post if you feel strongly and otherwise if there anything else on the F-Star name. It doesn't sound like there's enough demand to make a decision right now. Okay anything else to wrap up the call otherwise I think that is it for the day. Okay sounds good. Thanks everyone and see you on the next call. 


## Attendees

* Cayman
* Stokes
* Etan (Nimbus)
* Terence
* PK910
* Paritosh
* Alex Stokes
* Mark Mackey
* Manu
* Dancertopz
* Justin Florentine Besu
* Joshua Rudolf
* Kevaundray
* Katya Ryazantseva
* Carl Beekhuizen
* Hsiao-Wei Wang
* Anna Thesar
* Trent
* Peter
* Mercy Boma Naps
* Enrico Del Fante
* Stefan Bratnov
* Barnabas
* Toni Wahrstaetter
* Tim Beiko
* Phil NGO
* Gajinder
* Lukasz Rozmej
* nflaig
* Mikeneuder
* Pop
* Kasey
* Radek
* Echo
* Sean Anderson
* James He
* Saullius Grigaitis
* Vasilly Shapavalov
* Matt Nelson
* Daniel Lehmer (Besu)
* Gottfried Herold
* Potuz
* Dustin
* Francesco
* Eitan
* Ansgar Dietrichs

# Next meeting  Thursday 2024/6/27 at 14:00 UTC

