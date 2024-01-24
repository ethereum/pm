# Execution Layer Meeting 178 [2024-01-04]
### Meeting Date/Time: Jan 4, 2024, 14:00-15:30 UTC
### Meeting Duration: 99 Mins
#### Moderator: Tim Beiko
### [GitHub Agenda](https://github.com/ethereum/pm/issues/931)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=6xgxmKfVjtA) 
### Meeting Notes: Meenakshi Singh
## Summary
	
    

| S.no. | Summary |
| -------- | -------- |
| 178.1    | No Updates Dencun due to Holidays |
|178.2| Goerli Testnet fork date is agreed on Jan 17, 6:32 UTC|
|178.3|Sepolia is scheduled for January 30th|
|178.4|Add testnet fork times [execution-specs#860](https://github.com/ethereum/execution-specs/pull/860)|
|178.5|Update EIP-7569 to [Add Testnet times  #8051](https://github.com/ethereum/EIPs/pull/8051)|
|178.6|Discussed Prague/ Electra Network Upgrades|


## Agenda

### Dencun Updates 
          
**Lightclient** [5:16](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=316s): Cool thanks a lot. Hey everyone welcome to All Core Devs 178. First All Core Devs of 2024 Happy New Year's everybody. Hope you guys had a good holidays. First thing on the agenda is Dencun updates. I know that this wasn't listed on the agenda but I just want to check if anything happened over the holidays. I know Devnet 12 has been up is there anything around that people want to talk about, before we talk about timelines.


**Paritosh** [5:53](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=353s): Don't think we tried any specific tests over the holidays. So we were just keeping notes up and if a client team has something updated we just updated.

**Lightclient** [6:06](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=366s): Right on. Okay with that Marius wants an update from Prysm. Marius, what exactly are you looking for here?

### Updates on Prysm

**Marius** [6:21](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=381s): I don't know last time I don't think anyone from Prysm was there. And since Prysm was the one client that was kind of delaying stuff. It would be really nice to know how they are progressing and if they think everything is fine now or if they need more time? 


**Terence** [6:44](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=404s): Yeah I can give a brief update. So also like next week we'll do a Goerli release but this will be a pre-release. Meaning that I wouldn't recommend you using Goerli release from mainnet. And separately will also have a mainnet release. So right now we're be couple because right now we wouldn't recommend our latest block future to be part of the mainnet release. So I think we're okay with the Goerly timeline. But I think like we're too early to setting the Sepolia and the holeskey one having them one week apart is kind of crazy. Because it's definitely harder to change if something Goerli goes wrong. Because then you have to do a very like immediate client release to change the data again. So we would not recommend setting the holskey and the Sepolia for a day right now. 

**Lightclient** [7:45](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=465s): Okay yeah that kind of leads us into the next topic point but I just want to confirm with everyone that we are good with the Goerli date that we agreed on in the last All Core Devs which is Jan 17, 632UTC meaning clients would want to release sometime next week. Is that still what we're expecting to do?

**Marius** [8:14](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=494s): I think Gaskt is fine with that.

**Paritosh** [8:18](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=498s): Loadstar is good with it. 

**Sean** [8:21](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=501s): So for Lighthouse we've got all the Deneb changes done and merged. I'm not positive we'll be able to Release next week because we've also got a lot of networking changes that we're still testing. But if not I think we could do a pre-release similar to prysm.




**Stefan** [8:43](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=523s):  Yeah for Teku we planning to release Monday or Tuesday next week. 
	
**Justin** [8:53](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=533s): Besu is here we're going to be releasing end of this week we just had to put out the for clashes.


**Lightclient** [9:05](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=545s): Okay great! Yeah it sounds like we are all in agreement on that Fork time. I don't have the epoch right in front of me but it's out there. So on to the next two testnets Sepolia and Holesky, we last meeting discussed some days and there was some agreement but now it sounds like there's a little bit less confidence in those specific days. Tim went ahead and came up with Epochs on those days to try and agree on. But it sounds like we're not 100% confident on what days we want to do those Forks. So maybe we start with Sepolia. Sepolia is scheduled for January 30th. That's almost two weeks after the Goerli hard Fork. Is that the day that we still feel okay with? I mean obviously we can't foresee the future if something actually falls apart on Goerli then we'll have to rethink that. But in the optimistic case is that date that we can just go ahead and lock in. Potuz?


**Potuz** [10:18](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=618s): Yeah so I feel that it'll be much safer since there seems to be sort of like an interest in in shipping the actual mainnet as soon as possible it seems to me that it'll be healthier if we don't schedule the next testnets and we schedule them very soon after Goerly. If everything goes fine but sort of like having the back of our head if everything goes fine. It's going to be around these dates but try not to commit to dates now because things might not really go fine with Goerli. And going back from that is a problem like adding a new release with the  right epoch with no changes is easy but removing a release and fixing bugs is a problem. And it takes much longer than a couple of weeks.


**Lightclient** [11:10](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=670s): Yeah I mean my understanding is that you probably wouldn't release until the week before. But what how do other client teams feel about that timeline or what Potuz is saying? 




**Marius** [11:26](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=686s): So I generally feel feel pretty good about the timeline.  I don't really get what this would like bring us to not say right now that this is going to be the date. The clients can put out the release shortly before that anyway. So the only thing that this would like and if something goes wrong then like it's we have to break anyway. So we have to pull the break anyway. So if this late in the process something goes very wrong then we will have to delay anyway. So I don't see a point in not setting the dates now and just like have every client release on their schedule however they like.


**Lightclient** [12:41](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=761s): Gajinder you're unmuted did you have something you want to say?


**Gajindert** [12:47](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=767s): Yeah no I basically am muted through my Hardware mic. 

**Lightclient** [12:59](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=779s): Yeah Potuz is saying if we set the dates now and something goes wrong we will definitely need to re-release on the rush. Yeah I think that Pari is right here. Marius is saying that we don't necessarily have to release like we're not going to release next week with all of the forks, the testnet Fork schedules. I think the idea is that we would release them as we gain confidence in the roll out. Is that not something that clients feel like they're able to do. So if we do move forward with Jan 17 Goerly and then Jan 30 Sepolia that means we'd have about one week is to see if the roll out and Goerli is working as expected. And if it is we can go ahead and do that release you know 7 to 5 days before the Sepolia fork and allow people at that time to upgrade their clients. Do clients agree or disagree with that timeline.


**Sean** [14:13](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=853s): I think the timeline makes sense and we could say like January 30 is like a tentative date and then after see how Goerli goes and we're setting the date. 


**Lightclient** [14:28](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=868s): Potuz?


**Potuz** [14:30](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=870s): So these numbers are we release Goerli. We test for a week or so. Then we make a release. I guess without soaking just adding the fork for Sepolia and that gives teams to update their Sepolia validators for just one week. So it seems to me that that this this schedule will just remove the soaking of clients which presumably is fine if everything goes perfect because there presumably won't be changes. But if there's any changes then teams are not going to be able to soak them.


**Paritosh** [15:12](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=912s): Well I guess if there's changes we wouldn't Fork on that date right because nothing has been released. 


**Potuz** [15:17](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=917s): Oh there's regular changes that don't need to be urgent or anything but the thing is that whatever whatever we release for Goerli we are going to have to take the same release candidate for Sepolia and  not make a new release cut their new release from the developed Branch or main branch or whatever Branch you're using that continue to advance Because those changes are not going to be tested.


**Paritosh** [15:45](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=945s): I'd make the case that we have to test those changes in the subsequent testnet otherwise we make a release for mainnet and the mainnet changes haven't been tested anywhere.


**Potuz** [15:55](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=955s): And that's my point that we're going to be shipping some something without soaking.


**Paritosh** [16:01](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=961s): But isn't that always the issue? I mean every Fork we have shipped with changes that were tested at the last.




**Potuz** [16:09](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=969s): That has never been an issue we always have had at least one week to soak before cutting a release for the next testnet or the next mainnet.


**Lightclient** [16:19](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=979s): Is the proposal not to have a week to soak though. Lke I'm saying you don't need to create your release until around the 24th of January. That's would be one week after the the 17th hard Fork.


**Potuz** [16:33](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=993s): Right but if you can't after one week from Goerli you cut your release candidate then so that means on the 24th to actually release it you need to have it soak in a few days and that means that there's no time to actually test for to I mean to deploy for the people that are actually running validators. I think the two weeks is just too close that's what I'm pointing.


**Marius** [16:54](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1014s): So you mean we would need three weeks between each testnet basically in order to have your process.


**Potuz** [17:06](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1026s): Well I don't really mind the last two Holesky and Goerli.  I'm sorry Holesky and Sepolia but I think we do need
three weeks after Goerli because Goerli might go wrong.


**Marius** [17:26](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1046s): Yeah I don't like when we always only had two weeks between testnets and then three weeks three or four weeks to mainnet. So I don't know like I see your point. I'm not sure if I agree though. 




**Lightclient** [17:48](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1068s): It feels a little bit like the most client teams seem okay with two weeks. I know prysm feels kind of strongly about going with something slightly longer. I don't know if how strongly people have on their feelings for this. 


**Potuz** [18:08](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1088s): We don't really feel very very strongly about this if Goerli goes fine. We're fine with releasing the same deploying the same release this is not something that I'm willing to die in a on a hill and also I'm not really sure if prysm feels like this. I myself I'm not comfortable with it dates that were set.


**Lightclient** [18:32](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1112s): Understood. Ansgarr? 




**Ansgar** [18:35](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1115s): Yeah I just wanted to briefly say that this seems like basically more general question right that we should figure out for future forks as well. And maybe for the future we could try and and kind of have a more specified roll out plan for forks that we can discuss and agree upon not right before we have a fork coming up. Because I think now it's the unfortunate situation have to make that decision today. But I think I would agree with Marius in principle that we should be hesitant with kind of keep extending the times between kind of first test Network and Mainnet launch. Just because usually that's in a way like a that time anyway in terms of feature work because we already have everything ready to go and and we can't really work on the next work either yet. Yeah so I think if we there's the desire to have a more kind of drawn out process that's something we should probably then discuss some like when we have time and not right before hard Fork. 


**Lightclient** [19:44](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1184s): Yeah I mean it would be nice to come up with a consistent Fork pattern. I think also part of it is we wanted to ship this in the fall of last year. So now we're really trying to make make it happen and I think we're picking a little bit more aggressive timelines than had we had this conversation been happening in like October. I think we would have been a little bit more okay with stretching things out but you know. yeah we we we want to get this Fork shipped. Pari in the chat has proposed or kind of reposed what we accept what we had already talked about which is the for or 17th of January Fork Goerly, 30th of January optimistically fork or sorry is that still you're saying release in the week of the 29th with the expectation of optimistic Target 30th.


**Paritosh** [20:41](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1241s):  Yeah but I think that's way too close. So if we're going with that timeline we would go with the assumption that Sepolia is being delayed by at least a week or two. Because if we are shipping Goerli on the 17th and we need at least a week to analyze stuff. Then 25th is the earliest where we can say Okay Goerli has gone well or has not gone well. Let's assume it did go well then we can commit to making a release on the week of the 29th which means we've already passed
the 30th deadline for Sepolia. 


**Marius** [21:14](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1274s): So what I would really like to prevent is for us to have to go to another All Core Dev to confirm the dates. I think like All Core Dev is it's usually on a Thursday. And so afterwards we cannot cut a release because it's like the weekend already. So the next like possible day to cut the release is like the next Monday. So what I would prefer if we would say okay these are the dates if everything goes right we everyone will cut a release in the week of on the All Core Dev call and on the 25th and not have this and then we can discuss on All Core Dev if actually something really really bad came up and then we can  still stop it but I would I would just really like like I would hate to go onto another All Core Dev call just to say okay Sepolia is go now and now we have another two weeks to wait until we can actually do Sepoli.




**Paritosh** [22:30](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1350s): Yeah but coming to Potuz's point that would basically mean from the 17th till let's say even if we do stuff over the weekend the 21st that gives us about a 4 to 5 day timeline with the weekend where we have to find everything that's realistically wrong with Goerli.




**Marius** [22:50](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1370s): No we have all the time to discuss and to find stuff like we can always just say dont cut the release.


**Paritosh** [23:01](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1381s): We can always start making releases right. Yeah okay I guess we have to switch to async then.


**Marius** [23:06](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1386s): Yeah we can always say okay this is just like we will deprecate this release or we will just say we will remove the fork date or push the fork date or whatever. I like if this is if this is before mainnet
Release. I would also be more hesitant to say okay we can just move the mainnet  release in the last two days before it chips but for testnets I don't I don't really I don't think it's too Bad. 


**Lightclient** [23:42](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1422s): Guillaume?


**Guillaume** [23:44](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1424s): Yeah I mean would it be possible to just agree on two sets of releases two sets of dates that happen if everything goes well? And if something goes wrong you iMed immediately make the release like you don't have to go through a ACD. You just say something happen on Goerli. So the protocol is we move to the other set of dates you just make the new release. And that's it no need to discuss dates again on ACD and do the delay that Marius was talking about.


**Lightclient** [24:19](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1459s): I just think that if something goes wrong it's hard to be able to just unilaterally say this is the next date
that we should do. Like we're probably just going to have to discuss and depending on what we're wrong to yeah mean as Ansgar saying we need to figure out how much time it's going to take to fix. How much time we need to continue reviewing. So I think coming up with an optimistic date for assuming things continue to go correctly. We ship the forks on these dates as like what we're trying to do. And if something goes wrong then I kind of think we have to revisit the conversation a bit.


**Guillaume** [24:54](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1494s): Yeah I meant more like if something goes  wrong like yeah there's a couple bug fixes that are quite light but yeah of course if there's a major bug that gets uncovered then all bits are sorry all bits are off. Yeah I mean okay just trying to avoid the bike shading a bit like it's fine by me honestly. I don't care if it's an extra week if we just push we just add an extra week between Goerli and the next testnet but yeah if it can save some some discussion and I would rather do this and hope.




**Lightclient** [25:34](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1534s): Yeah it's sounding a little bit like client teams are wavering a bit  on the Jan 30th dates. Am I understanding this correctly? Are people kind of also open now to maybe having that one week later or five week days later? So that would be early that would either be late in that week of the 29th February 1 maybe or early in the week of February 5th so February 6/7 that would be for the Sepolia. Or do we just want to move with the January 30th? Marius says January 30th. Okay.


**Dan** [26:29](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1589s): Basic is fine with 30 of 2. We don't we're good to go. I'm a little more compelled by the side of our conversation that happening in the chat but we can maybe put a agenda item on for that.


 **Sean** [26:45](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1605s): Yeah Dan brought it up it's related to like the blob expiration. So like do we want to wait long enough to observe blobs expiring and the implications of that on a testnet before working the next testnet.


**Justin** [27:04](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1624s): I think can I add a little something to the question Matt. I think we also want to I think apps and L2s might want to go through that as well.


**Lightclient** [27:15](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1635s): Yeah I mean does any client team feel strongly that that we need to see this happen before moving to the next testnet. My two sense is that we're going to see it happen on the testnets before  mainnet and that's really the big thing that we want to see. But care for perspectives.


**Sean** [27:34](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1654s):  Yeah I kind of also think it's not really worth waiting between each testnet that long but it might be justification for waiting longer between the last testnet and Mainnet.


**Lightclient** [27:52](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1672s): Okay so you're saying you might want to see on Holesky the blobs expire before moving to mainnet or any testnet.


**Sean** [28:02](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1682s): Definitely any testnet. Yeah I'm not sure it would really make a difference with Holesky but with like between testnets. I mean but yeah. 


**Potuz** [28:13](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1693s): Most probably Sepolia right. I think most teams have deployed either Goerli or Sepolia not that much in Holesky. And since the is supposed to be the stable one I'd expect that we should mainnet after we tested availability and expiry on Sepolia.




**Lightclient** [28:35](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1715s): Yeah that makes sense to me let's keep that in mind when we were thinking about the mainnet at Fork date but we're not out of the woods yet. Tim proposed a Epoch for the Sepolia fork. We kind of agreed January 30th. Can we just get a thumbs up on the epoch that was in the PR 132608. That's okay for everyone, that's 22:51 UTC on the 30th. I see a thumbs from Basu and Guillaume. I'll assume the silence is agreement from the other clients. Okay Sepolia we have some agreement on January 30th on that Epoch. Holesky the proposed date is the 7th of February. I'm guessing people want to push that back one week. Is anyone in favor of doing that or would rather keep with the more aggressive timeline of giving one week between Sepolia and Holesky. Gak, is okay with the week. One week is good.  Fantastic. All right. Well let's stick with the 7th of February then. The epoch that Tim proposed is 29696, that's 11:34 UTC on Feb 7. Any last comments on the fork scheduling or should we just put that into a box and put a bow on it. And ship the releases. Great, that's awesome.  Any last Denon questions or comments before we open up the next fork for
discussion. Cool.


### Prague / Electra Proposals


So the next agenda item is the Prague Electra hard fork. And in the agenda we have a link to Eth magicians for which is a bunch of proposals that people would like to see in the next execution layer hard Fork. I don't know how you guys would like to go through this but I think it might be useful to answer the question of what is our vision for the next hard fork in the first place before we just rattle off 10 or 20 EIP proposals. So I know that there's been a lot of discussion about should we do Verkle in this next fork or should we have a smaller fork with some of these EIPS that people are really requesting right now. Do any client teams have a perspective on a smaller EVM Fork this year or do teams feel that we should really lean into Verkle and make that the main priority and not ship another Fork until Verkle is ready. 


**Marius** [32:44](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=1964s): So my personal opinion is that we should focus on Verkle and not ship anything between in because just the just the scheduling and the discussions will take up so much time because everyone like if we start opening this kind of worms then everyone will start lobbying and pushing for the EIPs to go through. Two small caveats with this. One is that I would like to have a get a more concrete overview of the progress of Verkle and second thing that I think we should also take into consideration is what's happening on the Consensus Layer. I went through all the EIPs that were proposed and there are some that I would like to see on the Execution Layer eventually but there are none that I would say this is high priority super urgent. But I think there might be some on the Consensus Layer. So I think it's important for the Consensus Layer forks to discuss whether it would make sense for them to have a hard fork with those changes. And if that can be done without involvement of the EL or whether it needs involvement of the EL and we would need to do a joint hard fork anyway. And then I would be okay with having a smaller hard for so highest priority is Verkle definitely and we should push for it but with these two caveats.  


**Lightclient** [34:47](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=2087s): Understood. Thanks Marius. Lucaz?


**Lucaz** [34:51](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=2091s): So my experience tells me that state redesigns are extremely hard. And they take extremely long time. So for example Gas delivering flat layout took few years. We are working on our flat layout for over a year and it will take at least another half a year to deliver it or at least few months to deliver it properly. So while I think Verkle is great and it's doing great progress I think if we just focus on Verkle it would take at least a year for an next hard fork and even more. So my proposition would be to potentially focus on some smaller hard Fork while each team would  commit to Verkle and assign appropriate  resources appropriate workforce brain power however you want to call it to this topic. So we can have similar situations as with withdrawals and 4844 that we are working in the background on it. And like working really really  in a concrete deliberate way. Yeah so that's that's in my opinion  minimizes risk of  just stalling for over a year while having the greatest potential to move Verkle as quick as  possible.


**Lightclient** [36:33](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=2193s): Thanks Lucasz. Yeah, one of my concerns and I'm curious here about what how teams view this is that it's going to be difficult to have a small fork and keep a lot of band team bandwidth towards Verkle, that's my guess  as people are commenting. I would like to hear your perspectives on that. But I also just wanted to mention that this isn't necessarily something we're going to decide today. We're really just starting the discussion so don't feel like we're going to make the decision now. Guillaume? You had your hand up. 


**Guillaume** [37:13](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=2233s): Yeah! So trying to unpack stuff that has been said. So yes updates there are updates being provided  there's Verkle info if you want to know a bit about the current state and also Joshua is Joshua Rudolph is making regular updates on Twitter. So if you want  something to help you decide  there are some resources. And also we agreed with Tim that we would make  another like the 3rd I think by now presentation about the current state of Verkle but that there will be either end of January or start of February. I don't remember. So there's that. But when it comes to the question proper. Yeah I also think there's no such thing as a small Fork I mean if we could for example commit to only do the BLS precompile for example I think that'd be fine because this has already been considered for a fork in the past so it should be ready enough. But otherwise I mean yeah otherwise don't fool yourself that will not be a small Fork. And we still have the problem that all that data needs to be translated. So the more we wait the worse it gets. So I would caution against scheduling a olive fork in between there's there needs to be a lot of attention and that also addresses what Lukaz has said yes there's a lot of clients have to have to redesign their database I mean Gask is still working on some on some back in things that will affect the way Verkle is implemented. So it is a pretty heavy Fork it needs a lot of attention from client teams this being said. I think every client team except maybe re and even them I think are looking into it. So everybody's looking into it, everybody's working on it. So I wouldn't expect any surprises in this respect. I think everybody knows what's coming. Everybody realizes that this is the thing they need to work on. So I don't really have any worries about the timeline proper assuming everybody takes the fork seriously. And starts investing more resources in it.


**Lightclient** [39:53](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=2393s): Makes sense. Thanks Guillaume. Tomasz?


**Tomasz** [39:59](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=2399s): That being ambitious at this is stage is better and being cautious later. Might be fine which means take a big lead Verkle for the next Fork but also be ambitious more and include things that are very important for staking will be important for the network. There are things like 702/ 37251. Just will be very much welcome and support all our efforts for handling liquid staking and any regulatory issues around operators for validators. Also I would say pick one model for the account abstraction Support. So go for all of this and take advantage of the team's capacity in the year where we have to show that we handle our biggest challenges. If Verkle end up showing to the teams that there's more and more difficulties piling up by march. Then maybe will just ask this question once again and say okay Verkle drops but then we stay with a pretty good set of other EIPs that we Include.


**Lightclient** [41:22](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=2482s): Yeah I mean I guess one concern of having the ability to constantly open this debate you know you can never permanently close it. But if this is really an 18 to 24 month project that we're committing ourselves because this is something that we believe is important to do for the network. If we're just have that in the back of our mind you know we could just take a break and spend 6-12 months shipping another Fork. I think motivate it'll be difficult to motivate client teams to motivate people to stay focused on this for the longer Hall. So I would be worried about opening these debates these debates back up. But I think coming to a coming to a conclusive decision is going to be challenging. Ansgar?


**Ansgar** [42:10](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=2530s): Yeah I just wanted to say I in my mind basically given that Verkle is an the outside only change. It makes a lot of sense to at least kind of. Basically when we think about the next set of CL changes that we don't commit to combining both of them and basically have that be the next book.  and I think in the chat also a lot of people have the same sentiment. So that we basically
at least have we plan them as independent forks and if Verkle goes really quick then we just combine them and ship them at the same time but if Verkle like six months from now Verkle is still nowhere near ready then we could just start to roll out the kind of the next CL side fork and then as part of that I personally but I'm not sure if that is majority kind of Consensus. I personally would very strongly also want us to not pre-commit to Verkle being definitely the next thing on the EL side.  If we basically think of it like a separate CL and a separate EL for then I think we should at least be open that say in six months if Verkle still looks very far out that we say okay hey we the set of CL features. We actually add a few small EL side features and make it a proper hard fork. But I think basically thinking of them as like a separate EL and CL workflow for the next fork. I think that's very productive. 


**Lightclient** [43:26](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=2606s): Yeah that's a I think that's pretty fair. I do think that we need to have confidence at least today. And or not as just day but we need to make a decision and move towards that and if in 6 months we have to revisit it we have to revisit it. But I don't think that we should sit in some halfway halfway out points and say you know this is kind of what we're working on but maybe we'll do something different like to ship a Verkle. We're going to have a lot of focus and attention from client teams which isn't going to come unless we say this is what we're doing. Andrew? 


**Andrew** [44:03](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=2643s): Yeah I'd like to say that I totally support Verkle. And I think for Aragon it's the easiest because we've already transitioned to the flat  data model. But I kind of think because some other clients might like what Lukasz said that some other clients might need time to redesign the data models. And I'm thinking that a smaller, more isolated Fork before Verkle makes sense tactically. Because if you consider things like EOF or the BLS precompile it might be a kind of a complicated change, say EOF but it is an isolated change. So you need maybe one or two people looking deeply into it but it doesn't touch like the entire code base. Right. So you can say only have a couple people implementing say EOF provided that the spec is ready. So yeah to my mind EOF or BLS precompile makes sense as a tactical walk.  


**Lightclient** [45:11](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=2711s):  So just to confirm your perspective is it's better to ship the smaller fork and kind of in parallel
also have the isolated the people working on Verkle continue and ramp up on
Verkle.


**Andrew** [45:27](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=2727s): Right. Yeah, so absolutely we should like Verkle should be our main focus and I mean if we decide that Verkle will be in the next Fork. I'm fine with it, like for Aragon it's doesn't is relatively easy but I'm just saying if we decide that Verkle will happens slightly later then maybe we can like CL client teams can allocate one or two people to work on more isolated things. But Verkle should be the main focus. 




**Lightclient** [46:07](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=2767s): Got it. Guillaume, you're back up.  


**Guillaume** [46:12](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=2772s): Yeah I I mostly agree with what Andrew and others before him said. I'm perfectly fine with the giving priority to Verkle and if it turns out it takes longer than than expected we come up with a with a temporary well not temporary but a smaller fork in between that's totally fine. One thing I wanted to add because I think there might be a misunderstanding Verkle is on the scale of the merge, if not worse in terms of complexity. So yeah you cannot really ship anything at the same time on the EL side. But I had the discussion with Tim in Istanbul and we were talking about pushing Das at the same time. So when I say at the same time it's actually in the same
release but not necessarily activated at the same time. So it's not like we're holding everything back fork Verkel. We only holding EL back fork like all other EL changes back fork for Verkle. So that's the first point. When it comes to EOF that's yeah I mean I've supported EOF. I mean I still support it. I think it does change a lot more than Andrew seems to seems to think all over the code base. And it does increase the complexity of Verklel itself unless we could somehow convert every single contract out there to EOF then it actually makes things simpler. But I would not I would not consider EOF you know small enough to make it into a fork that goes before Verkle. 


**Lightclient** [48:07](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=2887s): Got it. Potus?


**Potuz** [48:10](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=2890s): Yeah I just wanted to reply to Marius and Ansgar that made some points about like decoupling CL forks from EL forks and while this sounds like interesting in theory in practice. It's kind of useless at least in this case from the list of changes that you see for the coming Fork. There's only
one minor change that is in the original list in the first list on this that is purely CL which is removing an attestation index a committee index from from the attestation. And all the other changes  even those that look like they will be only CL like increasing the max CB they depend on other changes that are from the EL. So I think pure CL Forks are not going to happen happen at least I don't Envision them happening not this year not the next year. We don't have enough proposals that are purely CL. So we all will always need changes from the EL in whatever CL Fork. We propose having said so I do agree with Andrew that since this for an Ansgar mentioned this Verkle is purely EL. So if we are committing to Verkle in 18 months we're going to have CL teams that can work in parallel in whatever changes are majorly CL. And there are some changes that require small components from the EL. It wouldn't be nice to since Verkle would just delay those EL changes. It wouldn't be nice to delay those Forks that would be mainly CL. So I think we can ship smallish Forks on the EL side that are mainly
CL in the timeline that you're working on Verkle.


**Lightclient** [49:56](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=2996s):  Yeah that seems reasonable  just very quickly. Does any EL just disagree with that sentiment from Potuz or does that seem fair? 


**Gakonst** [50:09](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3009s): So what's the one liner?


**Lightclient** [50:13](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3013s): Yeah I mean the DAS is a good example it's you know the EL is checking the The Blob gas limit but adding that to a fork. A bit more than one line but still.


**Potuz** [50:27](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3027s): One like triggerable exits is something that is mainly.


**Lightclient** [50:30](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3030s): That's not really a simple change for the Execution Layer though. Ansgar?


**Ansgar** [50:45](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3045s): Yeah I mean I just was going to plus one list. And say that I think basically clearly it doesn't make sense to have the distinction of like literally CL side only and EL side only changes like probably still have a client release on the other side as well. But that basically we use it as a shelling fence right. So the problem is always with forks once we open them up at all. Then everyone wants to get in so if we have the shelling Fence of saying hey this is a CL fork. So you can only get in if your EIP is like 90% on the CL side. And if you need like one constant change or one small thing here then at least we can talk about it you know but basically I think just having the shelling fence of a of a clear theme of a focus super super important


**Lightclientr** [51:38](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3098s): Tomasz? 


**Tomasz** [51:42](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3102s): I agree with the Insight that those changes related to staking. The ones that have CL will be driven very much by the project management structure on the Consensus Calls. While the Execution Layer clients may have the Verkle as the main driver because on the testing side Verkle trees will be the ones that will cause the most of the headache to testers on the Execution Layer. For the Consensus Layer testing everything that is like Execution Layer triggerable exits. It might be feeling slightly complex to implement on the Execution Layer but I don't think it will create the same level of interdependencies between the changes that are in the Execution Layer. You'll test them very much independently and then there'll be a bit more burden testing of Consensus Layer. That's a different thing if you if you want to do both Verkle trees and stay account abstraction support. But I think that you should still opt for both because if Verkle Tree indeed ends up being a 18 months project. I think the account obstruction will be something that will happily ship within the next 6 to 12 months.


**Lightclient** [53:04](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3184s): Rodiazet?


**Rodiazet** [53:05](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3185s): Hi guys! So basically I can confirm what Andrew said that from the Epsilon team the EOF specification is ready. And we've been discussing it a lot with the clients and language teams. So basically I would support the EOf to be introduced or start being introducing already as soon as possible. Of course workers are very important but not sure if we can say that the specification of the workers are as ready as EOF already is. So I wouldn't say that the EOF is such a big change especially for the execution client. And I think it's a matter of just understanding what really is happening there and it's very separated as you mentioned. So I would support EOF and of course in the meantime just finishing specification of the Verkles.


**Guillaume** [54:11](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3251s): What specifications are not ready in Verkle exactly? 


**Rodiazet** [54:16](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3256s): I'm just asking if we can say that specification of the Verkle trees are ready? So this is just a question, not sure if it can be say about this  it can be safe for Verkle but for sure for EOF it is ready.




**Guillaume** [54:37](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3277s): I mean, I
would say they as ready as they are for EOF IE everything every like when it will end into the backlog or of every team out there it will be up for discussions again. So can you say any of them are ready. No but I don't see the Verkle specification being less ready than.


**Rodiazet** [55:04](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3304s): Okay if you say so. As I said I just a question here for you.

**Lightclient** [55:10](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3310s): let's not get too Sidetrack down. The Readiness Road I would do want to kind on bring it back to that original question sort of been keeping track of what client teams have been saying but I wanted to hear I don't know if I've specifically heard Besu or JS do you guys have a preference on on what to move forward with next again like we're not making this decision now it's just trying to collect this information. So we can mull over it for the next couple weeks.


**Justin** [55:43](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3343s): Yeah we were on Besu right now. So we're making progress on both fronts. You know we're looking at what comes next with the whole driver and passengers plan and I think we agree that EOF is definitely not a passenger. However, we've got a lot of progress on EOF  for quite some time actually. So I mean I would be very comfortable personally with EOF being the driver for the next one as we work on Verkle because we are making a ton of progress on Verkle as well. And I don't see any of our teams remaining capacity being diminished by having to support EOF. During the 18 months that we're forecasting out required for Verkle. Not a strong opinion. And you know a bit of a sunk cost fallacy at work I'll admit but that really seems for us kind of the ideal way to go. 


**Jochem** [56:36](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3396s): Yeah from my side I focus on the Verkle. 


**Lightclient** [56:42](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3402s): Okay got it . Great. So most teams seem to be leaning towards Verkle right now. Rests seems to be the the most feature leaning team and Nethermind and Besu also leaning a little bit with features but you know pretty much everyone is okay with making Verkle the next big priority. I again like I don't think it's the call to make this decision like I think we're going to spit another couple calls debating it. But I did want to give some time to people who wanted to talk about their proposals for Prague if not Verklel because I know some people have joined the call to discuss that and just to add color to the whole discussion of like what are we missing out. If we choose to go Verkle for the next 18 months. But before we move over that is there any last comments or questions  with respect to Verkle as the main priority in the next Work. 


**Lukasz** [57:51](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3471s): Like I said, in my opinion it's a very risky move to just focus on Verkle. But that's my understanding.  


**Lightclient** [58:12](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3492s): Georgios did I say that Reth was signaling support? I thought I said that you guys were leaning towards a feature Fork.


**Georgios** [58:22](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3502s): Oh Matt, maybe I missunderstood but wanted to clarify for avoidance of confusion.


**Lightclient** [58:28](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3508s): Yeah okay thanks. Yeah Guillaume?


**Guillaume** [58:34](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3514s): Sorry for jumping out of order. No I just wanted to understand why Luk was saying it's risky like long I can understand but why do you mean? What do you mean by risky?


**Lukasz** [58:47](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3527s): Okay so in order to have just touching the state takes tremendous amount of work and testing every time I've seen that happening. And while Verkle is already progressing. I still think that maybe for example go implementation is closer to being production ready but for example Nethermind implementation while quite future reach at the moment. It's very unoptimized and also for example depends on the transition for us depends on delivering  flat layout properly which we haven't delivered yet. So there are multiple risk there for nethermind. And optimization for example for the maths we have some problem there for example if we use  the existing libraries which are for fast and optimized. We have a problem of interoperability the cost that because actually accumulates quite a lot and if we try to implement it in C native C#. We were having issues with getting good performance. So there's a question what to do unanswered question and what to do with that I'm not sure if Besu for example, doesn't have similar problem. It would be great to hear about it. 


**Gary Schulte** [1:00:36](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3636s): Yeah Klen is leading and only dust are working  pretty heavily on the Verkle implementation but we're outside of the JVM for Verkle we're using JNI and the rust libraries for that.


**Lukasz** [1:00:51](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3651s): Okay so Hall three will be outside of JVM?


**Gary Schulte** [1:00:57](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3657s): No just like the IPA multipoint and any of the you know cryptographic implementations are in JNI.


**Lukasz** [1:01:07](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3667s): Okay and you don't have any problems for performance with that? 


**Gary Schulte** [1:01:13](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3673s): We yet to fully join the test net right now. So we'll have better numbers on it as we get join the testnet but I don't think we've noticed you like showstopping performance issues yet. 


**Lukasz** [1:01:30](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3690s): Okay testnet is quite small so not at least. I think it is I'm not sure if it will scale to mainnet levels without proper mainnet testing like importing the whole main net into Verkle. It's really hard to say if the performance is there in my opinion.


**Gary Schulte** [1:01:50](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3710s): Yeah that's fair. Has have we have other clients has geth tried to import main net into the
Verkle implementation and Go?


**Guillaume** [1:02:06](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3726s): Yes sorry if the question was gas? Yes we tried and I'm currently working on the shadow Fork to  make it more reproducible more frequently. So yeah the performance of go is fine but yeah other other clients will need to will discover that when they try to do the same thing yeah. 


**Lukasz** [1:02:34](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3754s): So my point is there is still a lot of unknowns  so if we commit to something. We might just not deliver it for a long time here and I would still commit to it but probably like with 4844 we committed to smaller Fork first and doing this in the background for some time so that's still my
Recommendation.


**Lightclient** [1:03:01](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3781s): Okay you're so you're still recommending feature fork with high prioritization of Verkle in parallel. 


**Lukasz** [1:03:10](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3790s): Yes that's my recommendation because Verkle will take a long time either way. So if we don't prioritize Verkle we won't deliver it in the next fork. For example but if we do and we takes a long time we don't deliver anything for that time which is also bad.


**Lightclient** [1:03:27](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3807s): Yeah Guillaume? 


**Guillaume** [1:03:29](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3809s): Yeah just to give a tiny bit of push back. I totally understand the the position of Lukasz is reasonable. This being said  you know a lot of the development that has been done in Gas is being readapted to other clients so for example Besu has been catching up really fast. Ethereum JS has been catching up really fast. Nimbus I'm not so sure but it seems to me that they are catching up fast. So it's not going to be as  as slow as it has been for guest because a lot of the questions have been solved  by us. So yeah I mean it will take time for sure I'm still not  convinced it will take 18 months. But otherwise yeah I mean Lukasz is right if it does take a lot of a lot of time. There should be members of of each team working on the on the feature
Fork. 


**Lightclient** [1:04:35](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3875s): I think we can probably close the discussion on Verkle for this call we have so many more calls and time to discuss it. And I think it will come up again in the next call in the next couple weeks if you guys could spend a little bit of time discussing internally. Okay Jamie did you have something you want to say. Great! Yeah if you guys could spend some time discussing internally. What your team stance on Verkle is I think that's going to be useful for the next couple calls. Potus?


**Potuz** [1:05:20](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3920s): Yeah not related to Verkle but something that came up last fork was that when The ethereum Magicians  post went up BLS pre compile was something that everyone said I want this in this Fork I want this in this fork and then it never happened. And when we asked on ACD Channel why this didn't happen the reply was essentially well just inertia. And I feel if you go and read that because it's not always the same set of crowd that write on the magician for Forum than would come here and voice their opinion on these meetings. If you go and read this chat now on the Eth Magicians forums, you're going to see that 7002 is the most voted one and where people in the community are asking for it. So I wouldn't want to have the same situation as with the BLS pre compile in the next Fork because of the same reason. 


**Lightclient** [1:06:17](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=3977s): Understood I mean that's a good segue. We've got some time left I think we should give people the platform to discuss the proposals for Prague. If those people happen to be here and yeah hopefully try to convey like how much demand there is for these things from the community. 


So I think maybe the best way to do it is just to go down the list of proposals in the Eth magicians thread. And if there's a person on the call who feels that they can spend 30 seconds to two minutes summarizing and trying to create some momentum behind it that could be useful. So the first one is 2537. Is anyone on the call here who wants to try to motivate a 2537 EIP in the next future Fork.


**Stokes** [1:07:20](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4040s): yeah I can I think this is pretty well accepted. I think everyone here so it's adding BLS arithmetic this is a curve we use on the Execution Layer. So it unlocks a lot of staking use cases inside the EVM making staking poles more trustless. It also helps a lot with Zero knowledge cryptography. So if any of these snark applications want to use this curve in EVM it unlocks them and then also that directly extends to ZK RPS as well. So yeah this one should definitely go in my opinion and would unlock many use cases.




**Lightclient** [1:08:00](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4080s): In the interest of time. I think we can just go to the next ones unless someone has a very critical or strong feeling against the proposal that might be useful for authors or people interested in the EIP going in to spend some time addressing that feedback. So any strong feelings against?


**Marius** [1:08:23](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4103s): One quick thing  I think this proposes 8 new pre- compiles or 6 new pre- compiles and most of them are not really useful for staking related stuff. I think only the verification, basically the verification is useful for that but most of the others are useful for L2 stuff as far as I understood it. But it would be really nice if we could get a document outline the need for every one of those. Why should we not just add one but why should we add like all of this five or eight or whatever pre compile.


#### [EL] EVM Object Format (EOF)


**Lightclient** [1:09:15](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4155s): Sure next on the list is EOF. Anyone on the call want to make the case for EOF.


**Justin** [1:09:36](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4176s): I'd like to just reiterate From besu's perspective that you know we're looking at this that it's it's very close to done. We're eager to ship it and a lot of Works been spent on it but I don't have any additional Community perspective on the interest or need for it that I could bring. 


**Lightclient** [1:09:52](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4192s): Thanks. Ansgar?




**Ansgar** [1:09:56](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4196s): Yeah I just wanted to briefly say I don't myself a super strong opinion but I did talk in Istanbul. For example with some members of the of the solidity team and they were expressing pretty strong  opinions in favor of  EOF. I'm not sure if that was represented of the entire team but I think there's a little bit of risk that EOF might be another one of these features say if we think back to 3074 from two years ago where I think a lot of the Community was really excited about it. But because that excitement didn't quite get to ACD and never moved forward. And I think EOF might be in a somewhat similar spot where there's a lot of more application side  teams and people that actually or like say in this case on the language on the program language side that would actually really like it. And that those are just the kind of people that don't usually come to ACD. So maybe there could be some value in Outreach  to try and get them on the call. 


**Lightclient** [1:10:54](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4254s): Yeah that's fair. I also talked with the solidity team in Istanbul and can Echo that sentiment. Does anyone have any very strong negative reaction to EOF or feel like EOF is not something that we should fork?


### EIP-7002: Execution layer triggerable exits


Okay  So next up is 7002 the alleged number one voted EIP for the next hard Fork. Does anybody want to motivate a case for shipping 7002? Tomasz?


**Tomasz** [1:11:35](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4295s): Yeah. We felt 7002. We cannot really claim fully non-custodial staking in ethereum which means that any professional node operators have to use a bit of a trig to support withdrawals. Which means that you always have the risk and griefing of the Capital provider who is taking not being able to  to draw without collaboration with the node operator. So the solution nowadays is maybe it's not really bad in a sense that the present transactions are offered. But 7002 is the way to go and not only this it also opens a lot of potential very important features related to safer restaking like more Alliance like I mean like better represented actual  Security on the network versus security borrowed and a few other things super Important. 


**Lightclient** [1:12:43](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4363s): Yeah that's a nice summary of it. Any strong pieces of feedback or negative thoughts on 7002? 
Okay next on the list is Verkle but I think we've already discussed Verkle quite a bit. 
So let's just go to the next one. This is a CL only one 7549 move committee index outside attestation.  Yeah Potuz, Do you want to motivate it?


**Potuz** [1:13:20](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4400s): That should definitely be in it's a very very simple change we can do it on the CL side it's it's trivial to implement and it'll save a lot of aggregation time. It can help on like trustless Bridges or ZK Bridges. It's something that should definitely be in whatever Fork we do next.


**LightClient** [1:13:43](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4423s): And is this a CL only change or is it any CL? 


**Potuz** [1:13:47](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4427s):  It's only a CL thing. It's just a bug in the design. We include a number in an attestation that since it's signed it prevents to aggregate different attestations with different of these numbers , which is the committee index of the attester. This removes this committee index outside of the attestation. So that you can actually aggregate different committees signatures.


**Lightclient** [1:14:10](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4450s): Got it. Yeah we'll leave that one to be more deeply discussed on the CL call. 


So next is EIP 3074 is anyone on the call who wants to motivate a case for 3074 and a
fork. 


**Ahmed** [1:14:32](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4472s): I can talk about it. So basically 3074 introduces two opcodes. One will authorize the smart contract to act on the behalf of the externally owned account. The second will call  other contracts from this  invoker contract and when it  will be like a delegate call but for the EOA that authorized the the invoker smart contract to do his bidding. The idea behind this  EIP is to improve the user experience. So for example patching transaction would be become way easier to do even for EOA. It will also pave the way for  EIP 5003 which will basically allow us to convert EOA accounts into  smart contract, enabling more account abstraction adoption. And also it will remove some of the bad design decisions like an ERC20. For example approve and
then   the action. So yeah that that's basically  my summary over it. 


**Lightclient** [1:16:14](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4574s): Thanks Ahmed. Tomasz, you have your hand up?


**Tomasz** [1:16:19](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4579s): Yeah I feel that  some insight support for the accountant construction or like more smart accounts whether it's 3074 or something much simpler like 7553 or anything else. Really that's proposed one of those would be good to have as a Target to deliver. And at the same time maybe one thing that we didn't discuss but Solutions like these Verkle trees are still very much bounce to ethereum L1 being seen mostly as a  High transaction through it user oriented layer and not on the scaling versus Alt. So the question is whether what if all those changes we want to show that we jumping on one what should be the change direction all to but still I think that's having all the implementations of the clients for those changes and the direction and research will be extremely important even at some point. 


**Lightclient** [1:17:30](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4650s): Thanks Tomasz. Andrew?


**Andrew** [1:17:33](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5653s):  Yeah I think  there was an objection from our team against 3074. Because it opens security kind of worms. It kind of there is a change in security assumptions and user assigns something that is lasting forever and can do arbitary things that the user like is not aware. He's signing for so permissions are not revocable things like that I can look deeper into it but and I haven't looked into the EIP for a while but I think there are big big security questions for IT against
It.


**Lightclient** [1:18:14](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4694s): Thanks Andrew. Ansgar? 


**Ansgar** [1:18:18](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4698s): Yeah so of course was one of the EIP. I do I'm happy that it has a second kind of win behind it now but I do I have some consensus at least that we want to voice specifically kind of in the context of layer 1. I think with kind of now Layer Two is being much more mature. It seems if there is demand for something like this it would be a much better can a let to try out in the l two context first via the IP process. Specifically I mean 3074 was always more designed as a stop Gap in between kind of EOA that we have today. And like the glory is actual obstruct in future with smart contact wallets that we'll hopefully get to in the future. And I think we are much closer to that future now. So it's there's less reason for that and I would caution that I think a lot of people that are now supporting the EIP are somewhat unaware of the complexities that it brings with it. So specifically the IP requires this kind of concept of invokers. And all the functionality would have to be standardized by invoker. So there have to be like one standard invoker for bundling one standard invoker for I don't know like time validated transactions all these kind of things. And that will take a lot long time to actually get these standards right. And while in principle they could be comp forward compatible with things like smart contract wallets and everything that would require like a very strong big
change to the way SMS work. So basically instead of having their own bundle functionality they would have to go through the invoker for bundling and everything. So I think basically before we were to even consider this for mainnet. We should basically get all the takes we should. We should basically have commitments from Smart contract wall implementers that they would actually also want to use this invoker design. we would have to actually see invoker implementations already proposed as ERC's. We would have to see tooling support like say Ether JS and these people specifically for some of these invokers. I think otherwise it's just basically really naive because we would ship this feature and then not have anything that could actually use it for the next two years afterwards.


**Lightclient** [1:20:24](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4824s): Thanks Ansgar. Let's go ahead and move on to the next because we're only halfway through. So the next proposed one is 3068 precompile for BN 256 # to curve algorithms. Is anyone here who
wants to support that? Going once, twice. All right on to the next one EIP 6110 Supply validator deposits on chain. Anyone want to motivate the case for that
EIP? 


**Justin** [1:21:14](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4874s): Hey this is Justin Besu to I like the EIP little bit of that again we have an implementation.


**Lightclient** [1:21:27](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4887s): Thanks Justin. Yeah it is mostly a CL EIP. Marius did you want to say something?


**Marius** [1:21:34](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4894s): Yes I can kind of motivate it. Right now basically  CL need to listen to EL receipts for finding out who deposited. And this means we need to keep all of the  receipts for these events for the deposit contract. What this would enable us to do would be to also lessen or lower the requirements for keeping historical receipts. So stuff like 4444 is kind of dependent on this. Because otherwise we cannot really with good conscience remove the receipts from post merge ethereum. Only we can only remove the receipts from rom Genesis up to  the start of
the beacon chain otherwise we would least lose those deposit events. So yeah I'm in favor of this.


**Lightclient** [1:22:51](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4971s): Thanks Marius. Potus? 


**Potuz** [1:22:55](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4975s): I think Dapplion line has his hand up and he's most probably going to say the same as me. 


**Lightclient** [1:23:00](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4980s): Okay Dapplion? 


**Dapplion** [1:23:02](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=4982s): Yeah one of the biggest points is that we will get rid of very bad security assumptions that we had because this is basically a bridge. Now an honest online note would not be convinced to process fake deposits even if there is majority and that's kind of the one of the last about things that we have Pre Merge.


**Potuz** [1:23:31](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5011s): Yeah, just a quick comment is that the fork itself. So the change is not so bad but the fork itself is a problem with the EIP. So it would depend a lot on what kind of fork we're looking at if we're doing this on the verge. I wouldn't add this EIP at the same Fork.


**Lightclient** [1:23:55](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5035s): Got it. Next EIP on the list is 6913 set code instruction. Is anyone here who wants to make a case for that EIP? 


**Marius** [1:24:13](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5053s): I can make a case against it. I don't think it's feasible. Having like changing this the code of a of a smart contract is not great. We have one way to do it with create two and self-destruct  this is
not anymore. But yeah so this has a lot of implications that would need to be tested for example setting code within a contract that just got set code code. So doing set code in a loop or doing set code with cursively. It doesn't play well with basically anything it doesn't play well with Verkle it doesn't play well with yeah a lot of other proposals. So I don't think it's a good. 


**Lightclient** [1:25:12](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5112s): Thanks Marius. We are running a little low on time. So if we can keep the comments pretty short Tomasz? 


**Tomasz** [1:25:24](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5124s): I second this against set code.


**Lightclient** [1:25:28](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5128s): Thanks next up is increase code size limit to 2 to the 16. Anyone want to make a quick argument for or
Against? Tomasz?


**Tomasz** [1:25:49](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5149s): We understand properly it shouldn't be done without Verkle tree done first.


**Lightclient** [1:25:55](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5155s): That's currently my understanding. All right next up  this is CL only one. We're going to skip it.


#### [EL] EIP-7377: Migration Transaction 
Next up after that is 7377 migration transaction. Is there anyone here who wants to make a case for that EIP?


**Gary** [1:26:21](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5181s): Sure okay since I put that on the thread.  I think that  7377 is a pretty elegant way to to migrate EOA’s  on the road map for account abstraction. It's  seems easy to reason about doesn't have a lot of baggage it doesn't seem to have the same kind of security risks that op and Opcode have it seems to me like it's a light touch fix for getting towards account abstraction.




**Lightclient** [1:26:58](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5218s): Thanks for that Gary. Sorry I'm just starting to go a little bit faster. So we could get through there's just about three or four more and we wanted to give some time for Ansgar to mention something about the RIP’s. 


#### [EL+CL] EIP-4444: Bound Historical Data in Execution Clients


So next after that is EIP 4444 is bound historical data this is something that's been brought up again and again. I just want to see if anybody wants to make a quick motivating case for making that a Priority soon. All right there's some people in the chat saying it's useful but we can discuss it more offline.  We've got a canful of things happening from the CL GitHub issue that are pretty related to Execution Layer. Is anyone wanting to make a case for SSZ specification of the transactions withdrawals and receipts. 


**Marius** [1:28:08](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5288s): I think SSZ speciification will add a lot of computational overhead because you need to do a lot of hashes for transactions. Right now you only need to do one to get the transaction hash 
with SSZ  you need, I don't know like a lot. And so every transaction processing will get a lot worse. So I don't think it's very realistic right now. 


**Lightclient** [1:28:35](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5315s): Got it. Okay that's from the list we've completed it. Draganrakita? All right that's the list there's a couple other ones two more that I wanted to bring up. 


**Draganrakita** [1:29:04](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5344s): I just wanted to give a little bit more support for EOF in general. It's not just one a is group of EIPs from like static jumps to limited faps to a lot of like small things that improve VF in good way. So yeah I just want to say few words on that nothing more. 




**Lightclient** [1:29:24](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5364s): Thanks for that. Does anyone want to make a motivating case for 7212 the R1 precompile on  mainnet? 


**Gary** [1:29:42](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5382s): I haven't looked super closely into this but it seems like that's going to enable a lot of account abstraction use cases secure on claves mobile devices things like that. It seems like for user experience that's something that we want to get out there. It's a as as a pre-compile goes I don't want to keep helping on Op base who has an implementation for this but we have an R1 implementation already. So it would be not terribly difficult to get that out there.


**Lightclient** [1:30:08](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5408s): Yep and then last sorry go ahead Ben?


**Ben Adams** [1:30:14](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5414s): I just mentioned something on the code size limit one of the issues with that is I mean it's quite at
24 K.  I don't know if I'd go all the way up to 64k but you know maybe 32 but it does lead to developers making very strange contracts in order to get around it you got the diamond proxy. And all sorts of various hoops and you people end up deploying multiple contracts when you know they've just gone over that Limit. And it becomes a lot more complex with delegate calls Etc. So it's is quite a Eux problem.


**Lightclient** [1:30:57](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5457s): Thanks Ben, the last one that I wanted to give someone a chance to mention was the EIP 7553 draft separated payer transaction. Tomasz I think you wanted to discuss that one? 


**Tomasz** [1:31:14](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5474s): Yeah so this is the EIP that goes like the simplest possible route to allow to separate the signature that is responsible for covering the Gas payment. And the signature that is authorizing execution on behalf of the account. This is alternative to any of the other proposals related to account abstraction like or smart wallet like accounts which means that if we go with something like 3074 and 7553 doesn't really make that much more sense. But 7553 was proposed by me because in Ansgar because there's really much much simpler change. It does still require wallet modifications perhaps if you see this back. Iit doesn't try to be very generic, it doesn't try to solve many problems, it solve something that is very often mentioned as 80 or 90% of the reason for introducing any account abstraction is just to allow for payment for gas from another account by some kind of pay Master. So 7553 we just pass this nothing more and  when you think about later it just opens also a very nice route for replacing  the actual signature that is being used for the authorization so you can leave the  the standard signatures we used to for for gas payments making sure that our transaction pool is still safe safe then we don't have to risk invalidating the transaction pool  but we can change later the signatures responsible for  for the authorization for execution which means that we can start creating some kind of account abstraction by a smart contracts if that signature is dependent on the contract execution. Because you already have promise to pay for that and validated for that in transaction to so that's 7553.


**Lightclient** [1:33:21](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5601s): Thanks Tomasz. We're at time Charles do you have a quick comment on that EIP? 


**Charles C** [1:33:28](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5608s): I actually wanted to advocate for the pay opcode EIP what is this 15920  which was briefly considered for Cancun and wasn't rejected it was postponed for I guess it's an EVM change. And I guess EVM changes that touch State can be a little complicated to implement. So I want to re bring it up for inclusion in Prague. 


**Lightclient** [1:34:07](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5647s): All right guys we're at time Ansgar, did want to mention this EIP 7587 reserving the addresses 
0x100 through 0x1ff address range for RI pre- compiles. Ansgar, do you you want to
take a second to discuss that? 


**Ansgar** [1:34:27](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5667s): Yeah I think Carl’s also on the call he would be better to talk about it. 


**Lightclient** [1:34:31](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5671s): Oh sorry go ahead Carl.


**Carl Beekhuizen** [1:34:33](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5673s): Yeah sure 7587 as discussed on the last ACD call the idea is to reserve a set of pre-compile addresses for the RIP process. So we can start deploying pre- compiles like the R1 curve as you're discussing earlier here but in a way that we can ensure no conflicts between L1s and L2s. The EIP is exactly as we discussed  last time which is basically just reserving the second 256  addresses for the RIP process. The question I have is about  assuming everyone's okay with this. How do we go ahead about formalizing this? It's an informational EIP but like can something like this be included in Forks or yeah how basically how do we turn it from this is something we're discussing and is nice into something that is  we agree to abide by it or not moving forward. I don't if anyone has any strong ideas on that. 


**Lightclient** [1:35:43](https://www.youtube.com/watch?v=6xgxmKfVjtA&t=5743s): It doesn't necessarily seem like something that needs to be quote unquote scheduled. It seems like we can just reserve it. We can talk I'll find like where to where to have that list but maybe something like the execution specs after the EIP is accepted. But does anyone against reserving that address range for RIPs or have a comment on It?
Okay let's say this is the  introduction of that EIP and then we'll Circle back to it in two weeks and try to confirm that and go ahead move forward with it. If you guys have any questions or comments about that in the meantime just go ahead and post on that Eth Magicians forum for the precompile reservation EIP.  And I think we can go ahead and close it out thanks so much for everybody being on their best behavior for The Substitute Teacher. Tim will be back again in two weeks for All Core Devs 179 and we'll again talk about Verkle and all of our EIPs that we would like to see in the next Fork. Happy New Year talk to you all later. 




# Attendees

* Potuz
* Lightclient
* Pooja Ranjan
* Ansgar Dietrichs
* Paritosh
* Guillaume
* Joshua Rudolf
* Justins
* KaydenML
* Marius
* Kolby Moroz Liebl
* PK910
* Tanishq
* Jochem
* Maintainer.eth
* Tomasz Starczak
* Roman
* Ben Edgington
* Spencer-tb
* Stefan Bartanov
* Ignacio
* Barnabas Basu
* Stefan
* Rodiazet
* Sean
* Gajinder
* Terence
* Barnabas Busa
* Gakonst
* Guillaume
* Andrew Ashikhmin
* Ameziane-hamlat
* Andrei
* Dogan
* Alex Stokes
* Danno Ferrin
* Pooja Ranjan
* Marcello
* Pat Stiles
* Marek
* Ayman
* Alexey
* Mikhail kalinin
* Anshal
* Mario Vega
* OxTylerHolmes
* Amirul Ashraf
* Jamie Lokier
* Barnabas Busa
* Kasey
* Marcin
* Charles
* Ben Edginton
* Roberto B 
* Ahmad Bitar
* Sean
* Parithosh
* Tim Bieko
* Mikeneuder
* Lightclient
* Matt Nelson
* EthDreamer
* Fabio Di Fabio
* Jamie Lokier

### Next meeting [18th January, 2023, 14:00-15:30 UTC]

