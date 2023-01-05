# Consensus Layer Call #94 Notes <!-- omit in toc --> 

### Meeting Date/Time: Thursday 2022/08/25 at 14:00 UTC <!-- omit in toc --> 
### Meeting Duration:  1:15:52 hour  <!-- omit in toc --> 
### [GitHub Agenda](https://github.com/ethereum/pm/issues/598) <!-- omit in toc --> 
### [Audio/Video of the meeting](https://youtu.be/tjmpu8O-xsA) <!-- omit in toc --> 
### Moderator:  Danny Ryan<!-- omit in toc --> 
### Notes: Avishek Kumar <!-- omit in toc --> 


-----------------------------

# Contents <!-- omit in toc --> 

- [1. Merge](#1-Merge)
- [2. Research, spec, etc](#2-Research,-spec,-etc)
- [3. Open Discussion/Closing Remarks](#3-Open-Discussion/Closing-Remarks)


  - [Attendees](#attendees)
  - [Zoom chat](#zoom-chat)
  - [Next Meeting Date/Time](#next-meeting-datetime)

-----------------------------------------------


**Danny** [1:53](https://youtu.be/tjmpu8O-xsA&t=113):  welcome to the 94th Consensus layer call if you are on YouTube, please let us know if you can hear us. The agenda which is  shared is one merge research  spec in discussion as point 2  looks like there is a couple  for it 4 topics that we did not get to  last time, if we have this efficient crew here to go over them we will otherwise we can take it to asynchronous chat if not and then general open discussion.

# 1. Merge

**Danny** [2:39](https://youtu.be/tjmpu8O-xsA&t=159): On the merge we do not have any particular agenda Items. Michael we started 10s when we got here. We do not know particular agenda items but open discussion as anybody wants to take the floor on the merge is anything we need to discuss today.

**Parithosh Jayanthi** [3:01](https://youtu.be/tjmpu8O-xsA&t=159): I am just the updates from the Geth  shadow fork . We had a good one last time and on Monday we updated the notes with the latest get version and with the update. We did see some red dashes notes. We did see a new  issue in the releases that’s been patched already.So please have a look at the Geth released notes and to continue the shadow fork trend. We will be having a Geth shadow for 12 next week and currently I am using the latest version recommended on the blog.

**Danny** [3:39](https://youtu.be/tjmpu8O-xsA&t=219): Great.

**Marius** [3:40](https://youtu.be/tjmpu8O-xsA&t=220): Anyone fromAragon here because we are still seeing a bunch of bad blocks on mainnet default 11. So it would be really nice to know the status of the issues.

**Danny** [3:58](https://youtu.be/tjmpu8O-xsA&t=238): On quick scan, I do not think Aragon is here. I can ping them in the executioner chat after the call and if they do join.

**Parithosh Jayanthi** [4:16](https://youtu.be/tjmpu8O-xsA&t=256): well I don't know if they were able to reproduce the invalid transaction or the invalid proposal. Those also on their blogs to note. So I think they are also looking at some redeployments and some fixes. So potentially the fix would make  the door option before the shadow fork.

**Danny** [4:35](https://youtu.be/tjmpu8O-xsA&t=275): So they are aware of the issue.

**Parithosh Jayanthi** [4:37](https://youtu.be/tjmpu8O-xsA&t=277): Yeah they are aware of the issue. They tried it in one or two fixes that potentially didn’t work but were able to cause a bit too much friction to keep trying it on the shadow fork. So they were able to reproduce it on their own dropson instances and I think they are just testing out trying to figure out what’s going on there  instead. 

**Danny** [5:03](https://youtu.be/tjmpu8O-xsA&t=303): Got it . Other merge discussion items?  Yeah I will mention as merge in the chat the effort bounty program and normally critical vulnerabilities can get up to quarter million US dollars between now and shortly before the target of the merge ? I can’t read the exact date, So they like 8th September . These vulnerabilities are for X or sorry the entire bounty program is for X. so you can receive up to a million dollar for criticals and then quite a range. September 8th . Yes Marius in that depending you know , mid high so find some bugs.

**Micah Zoltu** [5:56](https://youtu.be/tjmpu8O-xsA&t=356):  The 30 a function of like , this is very high for finding the bug in a majority plant as guessed.

**Danny** [6:04](https://youtu.be/tjmpu8O-xsA&t=364): Impact to live network is considered, so I would say to some extent yes. Lukasz

**Lukasz Rozmej** [6:16](https://youtu.be/tjmpu8O-xsA&t=376): So two things from the Nethermind side. One is the ongoing issues with empty blocks if we do not have enough time for FCU, so I think we had issues with Load star and Nimbus and I think we lost our other defects and it will be released before or it was released before. The version that will come before the merge but I think Nimbus already had a fix but didn’t release it yet. So as we will have one more release we are debating if we should just revive the kind of work around that I know . Also Geth has just been waiting for a block for some small amount of time to get payload. If we didn't have enough time in the first place.  so yeah that’s kind of we are debating if we should do that because if not then if someone uses. Nethermind with Nimbus, he will have a bad experience. It is not something we want to do but it’s like being less eager to move for some sort of time.

**Zahary** [7:32](https://youtu.be/tjmpu8O-xsA&t=452): This was one of the kind of fixes that though were supposed to land in the last Nimbus  release but since we discovered kind of some issues in pull request in the last minute we decided to kind of hold this off so but it has been merged now indeed and it will be part of our hardening release just before the launch. 

**Lukasz Rozmej** [7:55](https://youtu.be/tjmpu8O-xsA&t=475): Okay just before the merge. It's like should we release this fix ? So maybe  we should, we will bring this hotfix. What does for one version before the merge just to if anyone has a problem. He could just use this version for short for the amount of time and then we will again remove it okay that’s one thing which we just want to have a good experience on the other hand this is out of spec and we also don’t want to keep this hot fixed but okay, so that’s probably what we’ll do and the second thing is again? I don't have the full picture here, but we also experience some edge cases in syncing  with some clients and this because we are synching a bit differently so basically it is about their tracking if we have a block or get logs for some older blocks and we can get to head and start processing blocks, new blocks on the head while we still haven’t  downloaded the entire ancient history. So we for example cannot serve blocks or cannot answer on some old blocks queries. I think this is fairly unique to nethermind like no one else does this way and they  firstly download the ancient history and then later they  start processing blocks  and so it’s an edge case and it is fine, for example if you want to give time . I think   there was a problem with Prysm. But I am not sure if anything else. So I don't think there is a big deal but generally I would advise consensus clients to have some testing around this scenario when Nethermind sycs they  have but doesn’t have all blocks yet and if they can handle this. Normally we return an error that we don’t have this . So we expect and I know that some cl cancel  behave like that. They will just retry until they get it . Right so because we will eventually get it. But Yeah, that’s it and we are also syncing here but it should not be relied on probably but we are trying to get these syncing that be right now. When we already start processing on, we would be return ETH syncing false but we will be returning ETH syncing true until we have all the historical blocks so that’s potential fix for the future but it’s not a big deal but it is a user experience like it can be potentially a problem for  users that okay. Sometimes they need to wait and restart something or something like that so it is suboptimal and it is because Nethermind  has a bit different sync mode sync order and other clients . Yep, that's all for me.

**Mikhail Kalinin** [11:16](https://youtu.be/tjmpu8O-xsA&t=676): I have a question for you about payload. I think or do I understand correctly that the timeout will only be turned on when there is only empty payload.

**Lukasz Rozmej** [11:32](https://youtu.be/tjmpu8O-xsA&t=692): Yes

**Mikhail Kalinin** [11:33](https://youtu.be/tjmpu8O-xsA&t=693):  Okay and is it in the merge compliance release already ?

**Lukasz Rozmej**  [11:38](https://youtu.be/tjmpu8O-xsA&t=698): No. we are debating because we will have one more release before the merge because we have a 2 to 3 week schedule. We don't want to release a bigger  triangle in a bigger space and we are still doing some bug fixing. Some related to the merge simulated to Jason RPC. so we want to have a release. So yeah that’s the idea. It is not in the current version.

**Mikhail Kalinin** [12:13](https://youtu.be/tjmpu8O-xsA&t=733): Yeah I was say that in discord so and that I am in general against any fixing or optimising the thing on the other layer where the responsibility should be taken on  another one accountability but yeah considering that we are close to the merge. I think  that this is very much in the edge case ? The eth block  will be responded correctly if it works correctly , so it will return the payload immediately if CL sends you in advance . I think Yeah it is up to you but probably, it’s okay to go with this or without it .

**Lukasz Rozmej** [13:05](https://youtu.be/tjmpu8O-xsA&t=785):  So I hope it will be a temporary work around so that we can retire after another version.

**Marek Moraczxyriski** [13:13](https://youtu.be/tjmpu8O-xsA&t=793): on maintenance  it was finally working.

**Gajinder** [13:24](https://youtu.be/tjmpu8O-xsA&t=804): so from loadstar I want to confirm that  we have  included the fix for issuing advanced FCU in our version 1 release . so that should not be an issue.

**Lukasz Rozmej** [ 13:41](https://youtu.be/tjmpu8O-xsA&t=821): okay yeah like I said, I think you fixed it right . So that's the only name of the problem but again we do not want to be discarded as a client because we have a compatibility issue so that’s  why it is a temporary work around.

**Danny** [14:19](https://youtu.be/tjmpu8O-xsA&t=859): Anything else on this one? got it. Any other merge related discussion?

**Mikhail Kalinin** [14:33](https://youtu.be/tjmpu8O-xsA&t=873): I saw  discussion in the interrupt channel about changing the status of the payload after restart which may help to recover in some scenarios which we are  when EL responded invalid and then changed its mind or whatever. I don't have a lot of detail.  I just wanted to ask people if you want to share something about that on call.

**Danny** [15:12](https://youtu.be/tjmpu8O-xsA&t=912): This essentially forgetting the invalid cash on restart or persisting and that design issue  they go?

**Mikhail Kalinin** [15:22](https://youtu.be/tjmpu8O-xsA&t=922): Yeah , that’s essentially all the same client has approached as follows so they just forget that they consider all blocks optimistic after the justified one. So and page send them again to the L to get the status but some clients probably lighthouse and remember they persist the status and restart doesn't help to recover and there was a discussion that an option that is not turned on by default  to do to persist the status should be added to be recover from this case via restart but not doing any manipulation with the database.

**Arnetheduck** [16:17](https://youtu.be/tjmpu8O-xsA&t=977): Yeah I mean it is not switching back from invalid is more like forgetting  is the correct characterization because there is an infinite number of invalid blocks out there potentially that people could create but only an finite set of valid blocks. So I think that's the background to our strategy at least.

**Mikhail Kalinin** [16:42](https://youtu.be/tjmpu8O-xsA&t=1002): I think it makes sense in general?

**Danny** [16:45](https://youtu.be/tjmpu8O-xsA&t=1005): I can speak for everyone  but I know there was some discussion around it and those that were not forgetting did acknowledge that it is probably a reasonable strategy for recovery . I believe that  there was momentum to move in that direction for clients that were not there.  

**Enrico Del Fante** [17:06](https://youtu.be/tjmpu8O-xsA&t=1026): Yeah attack would discard this water start . It considers everything optimistic and actually saves us with some bezu interaction where it changes our mind and we are able to recover within the afterlife .

**Potuz** [17:34](https://youtu.be/tjmpu8O-xsA&t=1054): So pressing something in the middle, so we in an advertently , we are not recalling the persisting because we remove the  in valid blocks from our database . so we restart we don't even have those invalid blocks  to start with but on top of that we do not think other client from 
Poor choice . we don't jump for a choice disk. So when we restart from the final life checkpoint and everything below it is optimistic. So we are forgetting everything anyway. 

**Arnetheduck** [18:10](https://youtu.be/tjmpu8O-xsA&t=1090): Yeah number has a similar thing we do not persist for choice. We just reload on the startup from blocks , basically.

**Danny** [18:27](https://youtu.be/tjmpu8O-xsA&t=1107): any thing else on this one ? Mikhail. Got it .

## MEV Boost

**Danny** [18:40](https://youtu.be/tjmpu8O-xsA&t=1120): Any discussion points around MEV Boost ?

**Rahul Jordan** [18:47](https://youtu.be/tjmpu8O-xsA&t=1127): Hey everyone . So there has been a Post about [removing the trusted relay](https://ethresear.ch/t/removing-trusted-relays-in-mev-boost-using-threshold-encryption/13449) via threshold encryption. I believe Yani is working on it. So yeah, very interesting research is coming up.

**Danny** [19:44](https://youtu.be/tjmpu8O-xsA&t=1184):  Such a design does not preclude essentialized relay as well. right ? you could communicate with some sort of committee relay. You could also say the protocol does not have to fundamentally not remove centralised realisations in lieu of community realisation.

**Mammy** [20:17](https://youtu.be/tjmpu8O-xsA&t=1217): one of my concerns is it is good but if we do this does it delay proposed proposal builders separation or not.
**Arnetheduck** [20:32](https://youtu.be/tjmpu8O-xsA&t=1232): Together with merger releases but what will also  be doing this document for the feature highlighted that some of the release may be potentially be having difference in transaction selection strategies that do not as necessarily reflect the transaction fee.

**Rahul Jordan** [21:05](https://youtu.be/tjmpu8O-xsA&t=1265): Yeah also the issue with this design is that basically there is no way to really validate the kind of the body you know  before the full review is done. So basically they propose a kind of an optimistic approach where there could be some kind of slashing mechanism after the fact they are being invalid blocks being proposed that also adds more complexity to the project  but it seems to be one of the other super proposals that actually  tackles privacy at the core level?

**Micah Zoltu** [21:40](https://youtu.be/tjmpu8O-xsA&t=1300): Securities threshold encryption still not fast enough to actually execute a block in a reasonable amount of time.

**Danny** [21:55](https://youtu.be/tjmpu8O-xsA&t=1315): Fast enough at what angle?

**Micah Zoltu** [ 22:00](https://youtu.be/tjmpu8O-xsA&t=1320): other things  a NBCcommunitee that would validate the block.without anyone actually knowing what is in the block.

**Stokes** [22:26](https://youtu.be/tjmpu8O-xsA&t=1346): What I understand for this design basically or just hide the transaction contents until some other time and I don't think there are some performance considerations with threshold encryption mainly and not being that fast . Transactions in the next block might take a bit longer to gather a blocked out lnd on a chain and you just have to adjust the parameter of the system to account for that.

## Circuit breaker implementation

**Strokes** [23:03](https://youtu.be/tjmpu8O-xsA&t=1383): I have a question about the circuit breaker work and how clients are implementing it? I know Lighthouse and Teku look to have merged PRs.  I guess I would wonder then if Nimbus, Load star or prysm have had a chance  to look at that yet.

**Terence** [23:29](https://youtu.be/tjmpu8O-xsA&t=1409): Yeah so circuit breaker work emerged in Prysm v3 a couple days ago. So we're using 3 parameters , 3 meaning that 3 blocks missed consecutively and 8 blocks meaning missing last 32 blocks within  rolling window style and we don't actually kind of block us miss kind of strategy here.

**Enrico Del Fante** [24:01](https://youtu.be/tjmpu8O-xsA&t=1441): Teku, just merge the logic for moving windows . it’s enabled by default with 32 blocks and maximum 8 missing blocks. The approach is only looking at the state . so we look at the current state we have during the block production proposing so we only look at the block history in the state to find out if there are some missing blocks.

**Gajindra** [24:41](https://youtu.be/tjmpu8O-xsA&t=1481): For Load strat work in progress and we aim to make it next week. 
**Zahary** [25:01](https://youtu.be/tjmpu8O-xsA&t=1501): You also will be focusing on in the coming week still not implementation for inverse.

**Danny** [25:08](https://youtu.be/tjmpu8O-xsA&t=1508): Great thanks everyone. Are there any other merge related items ?

# 2.Research, spec, etc

## points of discussion ([[1]](https://github.com/ethereum/pm/issues/594#issuecomment-1206713478) and [[2]](https://github.com/ethereum/pm/issues/594#issuecomment-1211765927)) for 4844

**Danny** [25:51](https://youtu.be/tjmpu8O-xsA&t=1551): Does anyone have context on the first item weather  the blob gas price update ruled the EIP should be optimised for stable throughout or bursts of blobs , amy be part of them.

**Micah Zoltu** [26:04](https://youtu.be/tjmpu8O-xsA&t=1564): This is about how we adjust the gas price between blocks. Barnabe?


**Barnabe Monnot** [26:13](https://youtu.be/tjmpu8O-xsA&t=1573): Sorry, I don't have an update on this. I don't really look at that question, so we should be burst or average.

**Micah Zoltu** [26:21](https://youtu.be/tjmpu8O-xsA&t=1581): Yes, so just  in order to decide how we adjust the gas price between blocks. Do we prefer  to have things  bursty or spread out between blocks for smooth result. What is easier from a client implementation perspective? 

**Barnabe Monnot** [27:05](https://youtu.be/tjmpu8O-xsA&t=1625): So do we know what is better  on the client side if it is regular processing or processing all at once.

**Danny** [27:24](https://youtu.be/tjmpu8O-xsA&t=1644): any thoughts on this one or do we need to have this asynchronous or in a call where people have read it?

**Danny** [27:42](https://youtu.be/tjmpu8O-xsA&t=1662): okay number 2 here weather blob syncing should be lightly coupled to block sinking quote long term. The desires a couple this but adds  implementation complexity given the low number of blobs you might be best to Sync block along associated blocks.

**Micah Zoltu** [28:09](https://youtu.be/tjmpu8O-xsA&t=1689): Right so their is design goal impact for to essentially have it such that really one of the only things that charging when moving to a larger shadowed data construction is that your  datability is changed if you are a few tightly companies things then add more  work potential in the future when you have to decouple them but presumably if you have just a block sync method mechanism that pulls them simultaneously, then you simplify sync out the good. Somebody wants to take the argument for one of the other.

**Terance** [28:47](https://youtu.be/tjmpu8O-xsA&t=1727): wrote a [design doc](https://hackmd.io/_3lpo0FzRNa1l7XB0ELH7Q?view) and feels that the difference between approaches is small. But would like to hear feedback about having them coupled. How does this interact with checkpoint sync, and potentially backfilling a month of blobs?

**Danny** [30:24](https://youtu.be/tjmpu8O-xsA&t=1824): My  Intuition is to keep them independent. 

**Terence** [31:18](https://youtu.be/tjmpu8O-xsA&t=1824): Yeah I typically agree with you. The code is already there and it is also future . If it is also future extensible , it is totally reusable so that's quite nice.

**Ernico Del Fante** [31:34](https://youtu.be/tjmpu8O-xsA&t=1860): Yeah I tend to agree yet to be more forward compatible and to do the shortcut on if we are slight in time in general. So if you are going to design something that will support a better next version. If it gets a little bit more complex now.

**Danny** [32:04](https://youtu.be/tjmpu8O-xsA&t=1924): Okay, Terence and Enrico spoke in favour of this. As far as the spec goes, treat blobs in a modular fashion. We can reopen this if it becomes a problem. Okay and then there was another link to comment from Proto from two week ago for  number 4844 items. Proto you are not here are you? Does anybody having BLST update or otherCrypto Library update on extending the functionality for optimised KZG.

**Mamy** [34:00](https://youtu.be/tjmpu8O-xsA&t=2040): this is Blst team contacted him last week to gather some requirements for KZG use cases.  The EF research team have also been talking to Supranational.

**Danny** [34:18](https://youtu.be/tjmpu8O-xsA&t=2058): Got it and I know that couple of people on the research team have been speaking with supranational the LSU maintainer about getting some of the requisite Crypto in there  and their stuff in progress but thai is relatively early . and then the final point is in EIP 4844 test net first experimental version is running but new fees approach and need to be restarted include more testee and other facts. Anybody has a status update on the current test net or plans for future testing. All right I think we are all kind of in a merge shell blocks still but lets continue this conversation over the next handful weeks as the merge approaches and may be something pretty important to reboot at devcon  kind of get new target in terms of current specs, current engineering and play with some new testaments from there. Sorry, Anything else that people want to talk about EIP 4844 right now ? okay anything related to merge related research really specification? 

## User experience feedback

**Rahul Jordan** [36:20](https://youtu.be/tjmpu8O-xsA&t=2180):  So regarding merge I wanted to ask How are teams finding user-readiness for the Merge? Lots of confusion is showing up in the Prysm Discord. Lots of folks have had issues with JWT many do not know that you need to run a you know  EL client is  Just quite a bit confusing  but I do feel it is getting better.

**Tomasz Rozmej** [37:12](https://youtu.be/tjmpu8O-xsA&t=2232):    I am getting some negative feedback about the configuration experience. 

**Marek Moraczyriski** [37:41](https://youtu.be/tjmpu8O-xsA&t=2261):  I observed a lot of users asking questions about the need to run a consensus client. So yeah I have noticed some users with problems.

**Arnetheduck** [38:10](https://youtu.be/tjmpu8O-xsA&t=2261): similar experience and Nimbus we have a lot of user asking about JWT secret, and the need to switch to a different port on the execution engine. Also lack of clarity around suggested fee recipients. So we are working on clarifying those things in our documentation as well.

**Danny** [39:07](https://youtu.be/tjmpu8O-xsA&t=2346): Yeah I was sayingEthStaker has validated the workshop check out the [EthStaker Merge workshops](https://www.youtube.com/watch?v=Jra2cx0Wcss). Number 4 was yesterday. Also [Somer’s updated installation guides](https://twitter.com/SomerEsat/status/1562541042120814592).

**Arnetheduck** [39:38](https://youtu.be/tjmpu8O-xsA&t=2378): Another smile is showing also mention that Nimbus does not start calling the execution API until Bellatrix has happened that the different might not be ready for it. This leads to execution clients complaining in the meanwhile.Now execution plan at their side is that no consensus client if it is not calling the execution. Configuration call so we are kind of waiting until September 6 for this warning to go away but that’s just a small thing we have put in our blocks as well for users to expect. 

**Lightclient** [40:53](https://youtu.be/tjmpu8O-xsA&t=2453): How far away are we from the automatic setup of the two clients? I need to like to create these JWT’s in places and it would be preferable if I were to just go into another mind other than my dash out.

**Danny** [41:34](https://youtu.be/tjmpu8O-xsA&t=2494): Handling the JWT secret is always going to be an issue.

**Lightclient** [41:42](https://youtu.be/tjmpu8O-xsA&t=2502): A default location for the JWT token might help.

**Lukasz Rozmej** [45:30]](https://youtu.be/tjmpu8O-xsA&t=2730): Nethermind devops developed [sedge](https://github.com/NethermindEth/sedge) as a way to easily set up nodes. It uses Docker. It is not officially stable, but works well. Only supports Geth and Nethermind on execution side so far, and Lighthouse, Lodestar, Prysm and Teku on consensus side. Feel free to make PRs to this tool.

**Lightclient** [46:53](https://youtu.be/tjmpu8O-xsA&t=2730): 	Yeah I mean that's cool and I think it plays a role in the overall story but I do think that we could pretty set some defaults for the people who want to run the client on bare metal and not go through docker that should also be part of the whole story.

**Lukasz Rozmej** [47:15](https://youtu.be/tjmpu8O-xsA&t=2835) : well yes but it is harder to automate this way and so that is why I think this was chosen. 

**Lightclient** [47:22](https://youtu.be/tjmpu8O-xsA&t=2842) Is there anything that needs to be automated besides a list of places to look for  in the JWT token.

**Lukasz Rozmej** [47:38](https://youtu.be/tjmpu8O-xsA&t=2858): Not entirely sure but it also allows you to pick from different network things like that so yeah depends.

**Micah Zoltu** [47:50](https://youtu.be/tjmpu8O-xsA&t=2870): So each major OS has pretty standard places for storing things as expect the earliest thing to do just to have one go and do the research to find those standard places.then carve out a spot for ethereum propose it as a spec if I would do those interest in this . 

**Danny** [48:13](https://youtu.be/tjmpu8O-xsA&t=2893): Do you show that in the API as a suggestion ?

**Lightclient** [48:16](https://youtu.be/tjmpu8O-xsA&t=2896): I think it goes in the auth portion of the engine API.

## Light client protocol

**Arnetheduck** [48:33](https://youtu.be/tjmpu8O-xsA&t=2913): All right this topic is kind of over I would also one more thing and the light client protocol has been merged.One way of driving an execution client is to use the light client protocol. There is a beta of a Nimbus light client that just follows the protocol and can substitute for a full beacon node. Upsides are reduced network bandwidth, CPU, storage. Downside is that you are following 15 seconds behind head, and rely on light client security assumptions. Might get bundled with the Nimbus Eth1 client eventually. Also planning to publish it as a C library. Also working on a light proxy. An eth_getProof call in Geth allows you to get a Merkle proof of anything in state. The light proxy can validate these proofs. Useful as a wallet verifier.

**Gajinder** [54:52](https://youtu.be/tjmpu8O-xsA&t=2913):  we have a similar demo in Lodestar, running in-browser.

**Danny** [55:12](https://youtu.be/tjmpu8O-xsA&t=3312):  okay other discussion point?

**Saulius Grigaltis** [55:25](https://youtu.be/tjmpu8O-xsA&t=3325):  Yes small note on this discussion regarding the getting this the way the client stores the state  and some highest forgets almost everything and stores  from the start for a check point are so and is it a problem that after the restarts.

**Danny** [56:04](https://youtu.be/tjmpu8O-xsA&t=2913):  Given that  there are 4 choices ? LMD's latest message driven the reconstruction from blocks and then listening to new gossip. I believe it should be very sufficient. You know there might be some sort of generic case where your worldview is slightly off but I would say that it is fine for boot?

**Saulius Grigaltis** [56:47](https://youtu.be/tjmpu8O-xsA&t=3407):  thankyou.
 
## User activated soft fork to deal with bad actors


**Danny** [57:00](https://youtu.be/tjmpu8O-xsA&t=3420):  Micah you had a discussion point you brought up in chat?

**Micah Zoltu** [57:02](https://youtu.be/tjmpu8O-xsA&t=3420): sure this is the last one    Reprise of conversation from the last ACD call. Lots of people don’t understand that having this capability is a deliberate part of the protocol design.Call for core devs to signal that we would be prepared to do such a UASF if circumstances merit it. That is, to ensure that people know that this is part of the protocol; it is an intended part of how proof of stake works.
**Danny** [60:00](https://youtu.be/tjmpu8O-xsA&t=3600):  Any discussion points based of Micah comments 
**Mamy** [60:14](https://youtu.be/tjmpu8O-xsA&t=3614):   We need  to have some kind of constitution setting out our values, against which we come to a decision. 
**Micah** [60:47](https://youtu.be/tjmpu8O-xsA&t=3647):   Tend to agree. The user’s ability to predict the behaviour of the developer that is building the chain that they are using is very valuable . so users knowing that we will eventually move to prove stake  was very valuable for you to stay. Complaining that they can know they can decide as it is a chain . They want to use it long in advance . they don't get bought in first and then later find out you did something that goes against them.
**Danny** [61:41](https://youtu.be/tjmpu8O-xsA&t=3701):   We already have a written protocol, and that could be enough to define bad behaviour. It defines how the head of the chain should be identified.
Okay any other topics for today before we close? If you are listening and you are confused about how to configure system each one of these client does have discord. The ETH proposed are very helpful. There are some guides by somer’s and other they launch pad does have a preparation checklist and there are some videos of people configuring from ethstaker. There is also a merge community call on the 9th this is after upgrading Bellatrix. You know I recommended upgrading consensus layer on execution layer in tandem just to be prepped and ready to go but if you can only introduce upgrade  your consensus layer , you will make it through Bellatrix and there will be a community called 9th potentially very close to the merge. So you know that is a last ditch effort . if you have final questions but try to follow these guys jump ib these discords get your stuff upgraded.
Okay we will close it here. Thankyou every one.
 

----------------------------------------------------------------
## Attendance

- Danny
- Leo BSC
- Vitalik
- Grandine
- Paul Hauner
- Jacek Sieka
- Mamy
- Adrian Sutton
- Lion dappLion
- Patricio Worthalter
- Carl Beekhuizen
-  Lightclient
- Nishant
- Dankrad Feist
- Justin Drake
- Cayman Nava
- Mehdi Zerouali 
- Cem Ozer
- Terence
- Hsiao-wei wang
- Aditya Asgaonkar
- Alex Stokes
- Mikhail Kalinin
- Barnabe Monnot
- Zahary
- Pooja Ranjan
- Ansgar Dietrichs
- Proto Lambda
- Ben Edginton
- Leo BSC

## Next Meeting Date/Time :September 8, 2022 at 1400 UTC.


## Zoom Chat 
- From Marius to Everyone 03:06 PM
 bounty @danny

- From Marius to Everyone 03:07 PM
8 sept
is erigon etc under bounty?

- From danny to Everyone 03:07 PM
yes
known bugs do not count

- From Micah Zoltu to Everyone 03:08 PM
My vote is to not add workarounds because other clients have bugs.

- From Marius to Everyone 03:08 PM
nice, I rebuild my fuzzer today, will start this evening

- From Phil Ngo to Everyone 03:09 PM
Lodestar included the fix Nethermind on payload timings for v1.0.0

- From Łukasz Rozmej to Everyone 03:17 PM
Micah I would love to do that, but user won’t be interested if its Nethermind or Nimbus issue and will just switch
So it hurts our brand, increases (already estimated high) noise around the merge and reduces market share

- From terence(prysmaticlabs) to Everyone 03:17 PM
We added a flag: [https://github.com/prysmaticlabs/prysm/pull/11303](https://github.com/prysmaticlabs/prysm/pull/11303)

- From danny to Everyone 03:18 PM
nice

- From Raul Jordan (Prysm) to Everyone 03:19 PM
[https://ethresear.ch/t/removing-trusted-relays-in-mev-boost-using-threshold-encryption/13449](https://ethresear.ch/t/removing-trusted-relays-in-mev-boost-using-threshold-encryption/13449)

- From Micah Zoltu to Everyone 03:24 PM
If we run out of things to talk about in this call Danny, we can have the same conversation from ACD again (but with CL devs this time). 😬

- From danny to Everyone 03:25 PM
weren’t they there???

- From Micah Zoltu to Everyone 03:25 PM
Not all of them. :)
In particular, I still think it is very important for CL devs (individually) to make a public credible commitment to a UASF/UAHF if we start seeing intentional reorging by validators.

- From danny to Everyone 03:26 PM
[https://github.com/ethereum/pm/issues/594#issuecomment-1206713478](https://github.com/ethereum/pm/issues/594#issuecomment-1206713478)

- From terence(prysmaticlabs) to Everyone 03:29 PM
[https://hackmd.io/_3lpo0FzRNa1l7XB0ELH7Q?view](https://hackmd.io/_3lpo0FzRNa1l7XB0ELH7Q?view)

- From danny to Everyone 03:34 PM     
[https://github.com/ethereum/pm/issues/594#issuecomment-1211765927](https://github.com/ethereum/pm/issues/594#issuecomment-1211765927)

- From terence(prysmaticlabs) to Everyone 03:35 PM
[https://hackmd.io/@inphi/SJMXL1P6c#Endpoints](https://hackmd.io/@inphi/SJMXL1P6c#Endpoints)

- From Victor Zhou (xinbenlv) to Everyone 03:37 PM
QQ: is there a way to find stats of client adoptions of the new verson?
e.g. the GETH v1.10.23/v1.10.22

- From danny to Everyone 03:39 PM
ethstaker validator [https://www.youtube.com/watch?v=Jra2cx0Wcss](https://www.youtube.com/watch?v=Jra2cx0Wcss)

- From Pooja Ranjan to Everyone 03:39 PM
[https://ethernodes.org/merge](https://ethernodes.org/merge)

- From Trent to Everyone 03:40 PM
Merge Community Call #7 will be sept 9
[https://github.com/ethereum/pm/issues/599](https://github.com/ethereum/pm/issues/599)

- From danny to Everyone 03:41 PM
[https://twitter.com/SomerEsat/status/1562541042120814592](https://twitter.com/SomerEsat/status/1562541042120814592)

- From Łukasz Rozmej to Everyone 03:43 PM
[https://github.com/NethermindEth/sedge](https://github.com/NethermindEth/sedge)

- From Parithosh Jayanthi to Everyone 03:45 PM
How do we handle different OS-es?
I doubt there is any path that is standard across operating systems

- From Mario Vega to Everyone 03:46 PM
maybe not even requiring jwt key if request is coming from localhost ?

- From Marek Moraczyński to Everyone 03:46 PM
[https://twitter.com/nethermindeth/status/1555571498894725123](https://twitter.com/nethermindeth/status/1555571498894725123)

- From Trent to Everyone 03:46 PM
[https://github.com/NethermindEth/sedge](https://github.com/NethermindEth/sedge)

- From danny to Everyone 03:47 PM
the fear on not requiring jwt is if ports are accidentally exposed
light CL -> full EL

- From Łukasz Rozmej to Everyone 03:51 PM
If any of CL/EL clients that is missing want to add sedge integration please contact our devops or do a PR :)

- From danny to Everyone 03:58 PM
failure modes that are attributable but not auto-punishable
the protocol for finding the head is spec’d

- From Potuz to Everyone 04:04 PM
it gets tricky with Michael’s PR to fork late blocks
We’ll need to add that to the protocol I think



