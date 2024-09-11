

# Execution Layer Meeting 193[2024-08-01]#1104


## Meeting Date/Time: Aug 1, 2024, 14:00-15:30 UTC


### Meeting Duration: 99 Mins
#### Moderator: Tim Beiko
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1104)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=vbh9C2_-TIc)
### Meeting Notes: Meenakshi Singh
___

## Summary

| S No | Agenda | Summary |
| -------- | -------- | -------- |
| 193.1  | **Pectra Updates** | Devnet-2: Spec remains unchanged.  |
| | **Devnet-3:**|  Will include the latest EIP-7702 changes and minor tweaks, but no major features like EOF.|
| | |EOF devnet readiness to be discussed on [ACDE#194].|
| 193.2  | **Engine_getBlobsV1:**	| General support with an update needed for the honest validator spec. @tbenr / Teku will open a PR soon, with a final decision expected next week. |
| 193.3  | **EIP/RIP-7212:** 	|  No decision yet. Champions should extend testing coverage to improve inclusion chances.	|
| 193.4  |**Quantum Resistance:** | Discussions to continue in the #[cryptography channel on the R&D Discord](https://discord.gg/BsPm3Ncc).|
| 193.5  |**Verkle Tree Alternatives** 	| Discussions of possible alternatives to Verkle Tree are welcome in the Verkle Implementers calls 4. |
|193.6| **[New state expiry proposal](https://notes.ethereum.org/@gballet/leaf-level-state-expiry)** | Discussion to continue on [EthMagicians](https://ethereum-magicians.org/t/eip-7736-leaf-level-state-expiry-in-verkle-trees/20474). |
|193.7| **EIP-7463 Proofs:** | @parithosh has added EIP-7463 proofs to his [4444 torrent prototype](https://ethresear.ch/t/torrents-and-eip-4444/19788/17).|

___

## Pectra Updates

**Tim Beiko** [2:21](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=141s): And we are live. Welcome everyone to ACDE number 193. A bunch of things to talk about today. Lots of updates on the Pectra front. So we went from devnet 1 to Devnet 2 this week. We can discuss that and the issues we encountered. then there was the AA 7702 breakout yesterday. We can chat about that. And then there's two engine API related topics one around the encoding and one around a new end point for get blobs V1. So yeah let's get through all of that. Then last call we had the 7212 discussion where we couldn't quite get to like a final decision about what we wanted to include it in pectra. And so let's try to wrap this up today. And then if we have time there's a couple more topics that are a bit less pressing but less urgent but we're going over. So Andrew had something around Quantum resistance and the implications potentially on the verkle road map. There's a new State expiry proposal and then yeah if anyone has updates on 4444s. We can cover those two but yes to kick us off. Pari do you want to walk through what happened with devnet 1 what Devnet 2 is and kind of over at around that? 

**Paritosh** [3:56](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=236s): Yeah so with devnet 1 we had the launch last week and we did have a few 7702 tests that were run we're sort of working with a bunch of people who are working on 7702 to help us get our testing stack up. And that seems to have broke the clients in ways that we were called the forking. Because of the forking it was quite hard to actually figure out which bugs were treated well on devnet 1. So we decided it was a bit easier to keep 7702 out of the picture for now and relaunch the devnet and focus on testing the other EIP. So we had the relaunch on Tuesday. and since then we've had like a few bugs that have been already caught and fixed and a few more open. So there's a bunch of open threads on the interop Channel in case someone's interested. On a high level there was an Erigon block production issue that's since been fixed. There's still an open Prysm issue and an open Reth issue and both the teams are looking into it. For grandine. So the network was non- finalizing for a while and during that time grandine seemed to have issues but now it's fine. So I still need to look into if that was during non- finality or if there was some other reasoning for it. But those are most of the open topics. So we back up to relatively healthy percentage but the idea is to first get all of these bugs sorted out. So that we have a clean Baseline and then we can start testing whatever we want on Pectra. 

**Tim Beiko** [5:36](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=336s): Awesome! Thanks. Any of the client teams want to chime in with more details on their end. Okay if not then I guess one thing that's is it worth trying to Spec devnet 3 today or do we want to wait another two weeks for that? Do we want to try and Run devnet 2 basically as is. I know there's been some changes on the 7702 side. So we can discuss those right after but then I guess more broadly you know would we feel ready and bringing say something like EOF in the next Devnet or do we still need a couple weeks to be ready for that? 

**Danno Ferrin** [6:36](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=396s): I think for EOF a lot of us are focused on the fuzz testing part of it we got fuzzers working on the various clients fuzzing differentially other clients. So I would want to see successful Kurtosis was asserted before I would propose putting in the Devnet. So holding off two weeks we could be there. It might work but I feel better seeing working Kutosis first. 


**Tim Beiko** [6:56](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=416s): Okay. S 	o then yeah let's we can reopen this thread in two weeks and worst case if we launch a Devnet before then you know we can launch a new one in two weeks with with EOF. Mario? 

**Mario Vega** [7:12](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=432s): Yeah so I'm still worried about the interactions between EOF and the rest of EIPs because we are still in the process of writing these tests. Generally EOF and 7702 I think that's my main worry. So we're still writing those tests and I think they are not ready. 

**Tim Beiko** [7:33](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=453s): Okay so let's table eof for another two weeks we can discuss it on the next call. What we want to bring it in or not. And I think this is kind of a good transition to talk about 7702 some more. So there was a breakout yesterday. Nico let it. I don't know if Nico's on the call but otherwise anyone want to give it a recap about the conversation there. If not, maybe I can try and summarise it but my biggest takeaway from listening to it afterwards was that We've seems like we've reached consensus on not having 7702 be like a full migration to Smart accounts. And I know a lot of the you know potential design changes had to do with Enabling that. So I think keeping the scope of 7702 to a temporary giving temporary extra extra functionality to the account. Since we would yeah we've landed on I'm not sure though in terms of specific specs PRs what that would mean is this the currently merged 7702 spec or whether there's an extra PR we'd want to merge in and see as part of the EIP. Have one plus one from Julian is this we keep the EIP as is. 


**Ahmad Bitar** [9:22](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=562s): From what I remember from attending, yes we decided to keep it as is for now. There are some minor discussions that we want to have maybe a little bit later at the point that EOF has made a decision on what they're going to do with code introspection features. Because there was discussions around if we should allow code introspection to the delegated account. Like what happens when you do exit code hash, exit code size and exit code copy of a delegated account. Currently as spec it just delegates those calls to the delegated account. So it Returns the hash and the size of the delegated account as far as I know, not sure if that changed. But yeah as far as I know that's how it spec right now so there was some discussions around changing that behaviour or not yeah. waiting on this decision on the EOF side.

**Danno Ferrin** [10:26](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=626s): I wasn't aware that was something that was blocking EOF to decide. But my off the cut thought is whatever the ultimate resolve byte code is that's where we apply the EOF 00 Rule and make the decision about the EXT code introspection.

**Tim Beiko** [10:43](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=643s): So that if it's dedicated to an EOF smart account then it cannot introspect but if it's delegated to a non EOF contract then it can introspect. Is that correct?

**Danno Ferrin** [10:56](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=656s): Exactly if it sees an EOF account it's still going to think it's nothing more than EOF 00. 

**Ahmad Bitar** [11:02](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=662s): Yeah there was discussions last on the chat yesterday that we want to potentially only restrict delegation to EOF accounts. Yeah but we still want to go through more Devnets on Pectra probably with EOF to see if this is actually what we're going to do with 7702 just in case.

**Danno Ferrin** [11:28](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=688s): By restrict delegation you mean not allow EOF accounts to be delegated to.

**Ahmad Bitar** [11:34](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=694s): No only allow EOF accounts to be delegated to contract sorry.


**Danno Ferrin** [11:42](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=702s): That's an interesting idea. Okay.

**Ahmad Bitar** [11:51](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=711s): Yeah but all of these are like not anything immediate all of them as far as I know. Or as far as I understood from yesterday meeting is something to look into at a later Stage.

**Tim Beiko** [12:04](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=724s): Okay so I think it makes sense to then move forward with 7702 in like the next Devnet. And then keeping the EOF stuff in mind basically and then when we've actually shipped the Devnet. What not we can make a decision about potentially tweaking the spec with regards to EOF and maybe do that after we bring EOF in. One question I do have though so looking at the Devnet 2 specs it links the Devnet 2 specs. I'll put them in the chat right here. So the Devnet 2 specs link a relatively old commit of 7702 which is like two months old. Whereas lightclient merged something like 19 hours ago. So just to make sure we're all on the same page like should what we have in Devnet 2. I know Devnet 2 is already live so does
it make sense to talk about Devnet 3 actually. But like is the thing that we want is the thing that we want this list PR that light Cent just merged for 7702 or do we want the thing from two months ago.

 **Ahmad Bitar** [13:20](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=800s):  So for Devnet 2 we decided two things. We decided to keep the exact spec of Devnet 1 because it's just basically a basic relaunch of Devnet 1 and second is to not proc any 7702 transactions because the spec is going to change. So we felt like there's no need to test an
old spec. 

 **Tim Beiko** [13:39](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=819s):  Yeah and so Devnet 3 we have the latest 7702 spec and just to make sure we're all on the same page here. It's the spec would be including the PR that was merged 19 hours ago. That I just posted in the chat. And no other or I don't know minimal other changes to Devnet 2 like we're not including EOF or anything like that. 


**Paritosh** [14:06](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=846s):  Yeah exactly. So we wouldn't include EOF but we would just bump up whatever spec releases are there besides that. 

 **Tim Beiko** [14:15](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=855s):  Okay I think this makes sense so yeah so I posted the PR in the commit in the chat here. So we can bump Devnet 3 to use that for 7702. And then see if there's other tiny tweaks but no other major additions. Anything else on that? Okay and then one other thing that was proposed that might affect Devnet 3. So Felix from the Geth team said that we should discuss encoding the EIP 6110 request objects in the engine API using SSZ rather than RLP. I don't know if Felix ? 

**Felix** [15:07](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=907s):  No. So basically at the moment so this came up a couple times during the code review of the 6110 implementation Geth so we kind of noticed that basically there's a lot of code now in Geth to specifically serialize the requests in and more specifically there's only the deposit request right now. and the deposits we have to serialize them to the JSON. But we also have to basically be able to decode them from JSON. And it's kind of the same issue we have in other RPC APIs where we get adjacent object. And then depending on the fields in that object we have to figure out like what type of object is this because there can be more than one type of request. And we kind of thought that it's a bit silly that to have all this complexity on the API layer when these objects ultimately have to be handled as SSZ by the Consensus Layer. So we thought that maybe it will be would be wise to just handle them as SSZ like all the way. So basically make the execution layer in charge of encoding them as SSZ. And then we would just relay them over the engine API as Opaque hex encoded blobs just like we do transactions now. So when it comes to transactions over the engine API we actually don't and call them as JSON but we just pass them as a hex blob. And we would we were suggesting to do the same for these new request objects. The downside to this proposal is just that the execution layer will now have to perform the SSZ coding which they haven't really had to do before however we will have to start using SSZ at some point so we feel like this is very minimal entry into the world of SSZ for the ELs. Because in the absolute worst case where no suitable libraries available. You could always because these objects are purely fixed size they could just be decoded like by hand. Basically like it doesn't require like if there's no Library available that you can trust. Then you could probably just wing it and implement it like in a different way. And it wouldn't be too much code either I guess would be about the same as just using JSON. So that's why I think I we were making this proposal and this was specifically me and Peter shilagi who's not here today. We're thinking like you know why don't we just start with this because we got to add the SSZ at some point anyways. And we just wanted to hear like what do other people think about it or is it a bad idea? 

**Tim Beiko** [17:46](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1066s):  Thank you. Yeah Mikhail. 

**Mikhail** [17:48](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1068s):  Yeah one potential issue is not only the SSZ support on EL but also SSZ Union support by all SSZ Library is I'm not sure it's the union is not used anywhere else at this moment. So that might be an issue as well. We need Union because for different requests. We have this type field and we need to go them differently. They have different views.

**Felix** [18:20](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1100s): Yeah I understand this but at same time I think it is a pretty again we also talk about this Union problem. However in the end this is such a simple. these types are so simple that it makes sense to start with this. I mean we were discussing adding like encoding transactions at s at some point and we've also been discussing just generally converting the whole engine API over to SSZ at some point. But for now just as sort of minimal starting point we could just like try to get this in and then just see how it feels prep like the libraries and stuff to make it work. And then yeah I don't know I just wanted to hear it from maybe the clients as well. Anyone has a has an opinion about it? 

 **Tim Beiko** [19:26](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1166s):  This is maybe a dumb question but I assume given that 6110 is on the devnets. Everyone's already implemented it with JSON right. Like there's no team who hasn't done it with JSON. Correct?

**Felix** [19:41](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1181s):  No implement it's already implemented it's more like also a cleanliness question I mean on both sides of the of the API we have to deal with these objects in JSON which are not really right.  I mean they are just internal consensus internal objects.

**Tim Beiko** [19:59](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1199s):  So I guess my proposal if no one feels strongly about it is. I would maybe keep it as JSON for now at least like for the next couple Devnets because we still have some pretty big things we have not tested yet. And then I don't know it feels like something we can also choose to add basically like later on if we want to do it. But yeah given we're still working on 7702 we're still working on EOF. My sense is teams bandwidth is probably limited to like take on another piece of work. And if we can effectively just add it later on. Yeah I know I personally feel more comfortable seeing the rest of  Pectra like a bit.

**Felix** [20:50](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1250s):  I mean like I said if it's not I just wanted to hear I mean we can totally live with it being JSON for now for the future we definitely have this plan to work on converting the whole engine API to SSZ. So sooner or later and at that point we probably also we will redesign maybe some of the functions to have a slightly different structure or something. And then so I guess maybe we will get another chance then to really clean this up. I just felt like would it would make our life simpler anyways. But it's fine. 

**Tim Beiko** [21:25](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1285s):  Anyone else have thoughts or on this. Okay yeah and then there's a good comment by besu that they just haven't had time to evaluate it. So we could decide this in the future All Core Devs.

**Felix** [21:44](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1304s):  So pretty quick yeah yeah I just thought. 

**Tim Beiko** [21:48](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1308s):  Yeah so okay so let's yeah let's review it. I think and then you know we can decide this if on the next call or the call after that like it doesn't seem super urgent. But if it's something that we want to do we can do it later in the fork process. Okay, anything else on SSZ. 

## [Define engine_getBlobsV1 execution-apis#559](https://github.com/ethereum/execution-apis/pull/559)

**Tim Beiko** [22:16](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1336s): Okay then next up there was a proposal by Michael on the light house team for getBlobsV1. I believe he's not on the call unfortunately. So I don't know if anyone else has the context around this or is able to talk about it. I see I guess Mikhail you approved it about a month ago. So I don't know if there was anything else we were waiting on or any feedback. We wanted specifically before merging this.

**Mikhail** [22:53](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1373s):  yeah the change looks good in terms of this Spec and it's just you know adoption and consensus of core devs is needed for to move forward. I think it's pretty good optimization. We have discussed some caveat some potential issues with Michael Sproul about using this optimization in the sense when it can hinder Blob propagation. So yeah but I think it's why optimization use carefully should be quite helpful.

**Tim Beiko** [23:38](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1418s): 
Enrico?

**Enrico** [23:41](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1421s): Yeah I just want to say that we like that and we probably use this optimization because we tend to try to get from peers pretty soon. Blobs that we missed or we are receiving late. So it could be very nice if we can try first on our local EL to get those before trying to get it from the peers and will be nice thing for us. But I also think that this should not be abused from the CL side. I think I was thinking lately because if CL pretends to get it a lot of those blobs from EL. And I see like the we should not do something like that affects the dissemination on the P2P like a super optimized way of trying to get it. And response I don't want to all the messages that I receive because you are not actively participating on the P2P anymore. If you abuse that channel. 

**Tim Beiko** [25:06](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1506s): Thanks! Is there a way we can add a limit or I guess not really right.

**Enrico** [25:15](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1515s):  I think like we should be add some more clean way of clean usage context. Let's say the Honest validator should use this in such cases but not maybe in others.


**Tim Beiko** [25:34](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1534s): I see Potuz. 

**Potuz** [25:37](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1537s): So what is the problem the problem is that you're not going to be gossiping those blocks but can you just get it from the EL if you have it you consider the Gi already satisfied and you gossip them anyways on the P2P side.

**Enrico** [25:50](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1550s): Image that you you receive a block first and the blobs come after so you you know in advance a way to look up your local EL for all the blobs and then you construct and I don't want message over the P2P because you say I already have those. So don't even send it to me and it means that you're not even disseminating anything. So you're not participating in the dissemination of the blobs.

**Potuz** [26:24](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1584s): But can you just send the I have messages and just gossip them anyways because you have them?

**Enrico** [26:30](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1590s): Yeah I mean you if you do that it's okay. But it should be in the honest behavior of the validator you say if I get it from the EL, I disseminate and then give give the send the I  don't want. If you ascend only the I don't want I'm cheating essentially.

**TIm Beiko** [26:52](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1612s): I think yeah that seems reasonable I guess the the weird thing is it would be we need to open a PR in the CL specs that effectively mentions that correct.

**Potuz** [27:07](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1627s): Yeah it can be done on the honest validator guide or on the P2P Network perhaps.

**TIm Beiko** [27:12](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1632s): Got it. Mikhail?

**Mikhail** [27:15](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1635s):  I just wanted to add that disregarding yeah we need CL to use it first. So it makes sense to implement this method but EL DAS should implement this. So where is also check temperature on this whether it's easy or not and how much of the efforts it requires to get implemented on the EL side probably not that much.

**Tim Beiko** [27:46](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1666s): Anyone on the EL side have thoughts on this? Okay I guess if there's not a ton of feedback now. What I would maybe do is I don't know Enrico if you'd be able to open a PR against the the specs like the honest validator specs to kind of describe the the gossiping Behavior. If we can have that PR open by like early next week. We can bring it up on the call on the CL call next week. And then if people are happy with that PR then we can merge both the spec PR and the engine API one. And if there's any objections on the El side with regards to complexity we can also yeah have last week be the final place to have next week be the last place to race them. 

**Enrico** [28:41](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1721s): Yeah I can open the the the PR but I will be off from from next week. So maybe it will be Carry On from by someone else.

**TIm Beiko** [28:50](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1730s): Okay great yeah. If you if you have a time to do it before you leave that'd be valuable. And so let's try and get this result in the next week or so. And then worst case make a final decision on this CL call. Anything else on this? Okay yeah thanks a lot everyone for the context. So that's everything we had around pectra anything else people wanted to discuss about the current Devnets current Forks? Okay and then I guess one thing we can also decide next week is assuming we did merge this engine API change. Do we want this to be part of devnet 3 but yeah for now we'll keep devnet 3 as Devnet 2 and the change on 7702.

## RIP/EIP-7212(https://hackmd.io/@ulerdogan/B1QikMxdC)

**TIm Beiko** [29:52](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1792s): Sweet I guess yeah moving on next thing on the agenda so 7212 the R1 precompile. We discussed it a few times Already. There's some desire I think by some of the teams to bring it in to L1. On in large part because it's already implemented on L2s at the same time Pectra is already huge in scope. We you know don't have it implemented. There are some concerns around the complexity of different EIPs being tested together. So I guess yeah the people think we should be including this is now the right time to make a final call on this. The people want to see how Pectra goes and then you know potentially push this back a bit more. I know we've pushed it back over and over again but we're also in a spot where we we don't have all of pectra implemented and so we're not necessarily yeah we're not necessarily like waiting to implement Stuff. So yeah I guess Ansgar as in favor. There's Nethermind in favor Lightclient?

**Lightclient** [31:12](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1872s): Yeah I kind of would like to see how Pectra plays out over the next couple months. I feel like we're restarting Dev in the process of restarting Devnets the things that have been accepted into Pectra aren't in the Devnets fully yet. It feels a little bit like yes 7212 is very easy to do but we're not we're not on top of Pectra right now and it doesn't feel like. The time right now is a good time to be adding additional stuff onto it regardless of the simplicity. So I would rather make that call in three months like if Pectra is going great and it's easy to add great but if not then you know we haven't added more stress to our Testing load which is already being pushed to limits. 

**Tim Beiko** [31:59](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1919s): Okay yeah Besu seems okay waiting as well. Pari is highlighting we have 20 EIPs. I guess yeah does anyone feel strongly that we should add this now? Otherwise yeah I am inclined to agree I guess I don't know Ansgar do you want to explain why you think we should make a decision now. I'm kind of inclined to agree that we can wait three months with this and it doesn't really change anything. But is there a reason why it's yeah there's it like some urgency. 

**Ansgar** [32:36](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1956s): So I mean I think in general I just think it's valuable to make the decision as early as possible because there's a bunch of things that depend on it. Specifically with this there's a lot of tooling a lot of like wallet developers. And whatnot that I think would really appreciate knowing is early as possible. At least that there some sort of preliminary decision towards yes and then even if we can still work the back but at least that they have some signaling that they can rely on.

**Tim Beiko** [33:02](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1982s): Isn't the EIPs on L2s though like for Tool engine wallets did they.

**Ansgar** [33:10](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=1990s): Yeah more like in terms of strategy of like do you do you forever basically have to maintain two separate like the chains that do and the chains that don't or I mean I don't have a strong preference If people really want to keep it out for now and then make the decision later. It just feels to me unrealistic that three months from now we'll add any EIP in. And so I would just I would just make the decision now to add it in at least on a preliminary basis and then just look at a later point which Devnet it would be a good fit for bringing it into the process form. But I'm happy to be over I don't feel strongly about it.

**Tim Beiko** [33:49](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2029s): Anyone else have strong opinion? 

**Andrew** [33:55](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2035s): Yeah I think I'm slightly in favor of including it. 

**Tim Beiko** [34:08](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2048s): And I guess yeah maybe on the client implementation side like do all the teams already have this done? I guess yeah does any team not have an implementation of this already or does everyone have it done. So Besu has like an open pull request on the EIP/RIP process Ansgar what I know yeah there's some stuff in the dock that UL has shared but like can you give a quick summary of what the like core things are?

**Ansgar** [35:01](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2101s): Yeah and I'm also happy wants to explain a little bit. In my mind it's a several things. So for one it's just more procedural questions so like what do we do about numbering? Do we create a new EIP copy over the specs? How do we physically reference the kind of the status  between the two but then also in terms of actually just making decisions do we ship it at the same address. So that is within the R2 pre-compile range or do we move it over to the R1 pre-compile range on L1. How important is it that basically daps can just use them as is across the different layers. Do we want to make small changes to the spec or are we okay with using the absolutely identical spec? Like I think those yeah those are questions they're like terribly like hard to figure out but I would just hate to have them to have to do them on a rushed call three months from now. 

**Tim Beiko** [35:52](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2152s): Yeah that makes sense. I think Danno has a good question around reference tests. Does anyone no like we it does feel like we are bottlenecked on L1 by testing because there's just so much stuff already. So like is this in a spot where if we include it like the testing work is already gone is already done or like would we expect there to be a you know some fair amount of testing because I think that's probably one of the things as well that that should play like do we include it now versus 3 months from now like if there's there's a bunch of testing work. Yeah it feels it feels kind of unreasonable to to add more now. But if you know the testing coverage is pretty much complete that I think that's Interesting. Okay Ulas do you have a link to the testing coverage but I yeah and I guess oh yeah Mario?

**Mario** [37:13](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2233s): Yeah even if it's already covered I don't think it's going to be so easy just to merge it into the L1 tests there's still going to be we're still going to have to review this and eventually merge it. Yes but it's not like it's not free is what I mean.

**Tim Beiko** [37:32](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2252s): And the tests yeah and the test that us just shared are like geth tests. They're not like specs tests.

**Mario** [37:42](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2262s): So no the process would be that we have to review them then convert them then merge them to L1 tests. So it's not free it's definitely not it's definitely extra work. 

**Tim Beiko** [37:56](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2276s): So I don't know I think given that I probably lean fairly heavily against including it now I think if the 7212 forks want to like you know continue pushing for it like it seems like there's support but yeah having like proper like L1 level test coverage. 


**Mario Vega** [38:21](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2301s): What I would suggest is that to help push this on the testing side is just converting if if if someone that is championing this EIP could help Port these tests into the execution spec test Repository.  That would be a very good help and that can be done in parallel because right now the testing team is focusing on brag accepted EIPs. So if someone that is championing this EIP could help us out to port to that would be I think that will help the EIP to get into PR. Thanks. 

**Ulas** [39:00](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2340s): Yeah I guess me and my team can help lot yeah. 

**TIm Beiko** [39:04](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2344s): And I think yeah Mario do you want to just share the two repos but basically like yeah we can kind of show you where we need to get the cross client testing and what it would look like. And I assume something we'd want to do as well for this precompile is like pretty extensive fuzzing of the implementations against each other like we tend to do for other  pre-compiles. I don't know if there's been any work done there as well. I guess I assume not but I think if we want to add this on top of the already sort of really huge Fork that we have yeah effectively having very thorough test coverage coming from the champions of the EIP. I think is what we'll need. And there's also some comments in the chat Tony around you know concerns about the quote unquote government curve. I don't think most client teams have raised it but yeah do you want to just maybe give a quick overview so that everyone has a context. 

**Tony** [40:32](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2432s): Yeah I can do that I hope you can hear me well enough. Yeah so I'm basically against the just because yeah secp256K1 was initially chosen for certain reasons and R1 was is different when it comes to the parameters of the curve and also the kind of a second reason would be that this is kind of a perfect example what we can ship on L2. And yeah my opinion not needed for L1. 

**Tim Beiko** [41:09](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2469s): Thanks yeah I don't know if there's any comments or thoughts about that? Okay then I guess on the testing front it probably makes sense for the 7212 Champions to kind of get it into a spot where it wouldn't be kind of an additional burden on the testing team. Yeah it's still CFI so we can reconsider it like in a few months when we've done a bit more progress on Pectra. But it seems like the main objection from the client team side is really just or the main objection I guess you from including it is you know do we actually have the bandwidth to test this property. So to the extent that you can help with that Ulas and your team. Then I think it might make it more likely to it will make it more likely for it to be included in Pectra. But yeah I think not making a decision today is probably the right call given how early we are. Anything else I don't know Ansgar, Lightclient both your hands are up but are they still up from last time. Ansgar gone and times if you have final comment you can save now. Okay I'll just assume your hand is still up.

## Quantum Resistance Attacks

**Tim Beiko** [42:46](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2566s): Okay sweet so next up Andrew you wanted to chat about Quantum resistance. So do you want to give a bit of context there and I think it's worth breaking this into two different topics. So first just the risks and and concerns around Quantum and then second you know if that has implications on Verkle and what they are. 

**Andrew** [43:15](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2595s): Right so it's like what Vitalic highlighted at EthCC that a lot of experts forecast that in the 2030s quantum computers will become powerful enough to break non-trivial cryptography. So I mean it's difficult to forecast, especially the future. But assuming that there is a good chance of that happening. So we are essentially with Verkle being Quantum resistant we are replace sorry not not being Quantum resistant. We are replacing the commitment scheme in ethereum with the current commitment scheme which is Merkle Patricia try. With something that is potentially potentially vulnerable. So two questions if I am no expert on quantum computers and cryptography. So  it's a genuine question that the vulnerability of  Verkle to quantum computers is this like super theoretical. And it's something that we is we can like sleep well and not worry too much or is it a very real thing that's that's one question. And assuming that it is real then maybe we should actually change the cryptography in verkle to something Quantum resistant. Because I imagine that well so the cryptography will have to change of course. But things like maybe the key embedding scheme and the migration strategies a lot of work there can be reused. So it will not be like a total waste so yeah we have something like so and yeah assuming that this vulnerability of Verkle is re. Then we perhaps should move to something like Quantum resistant verkle rather than because it will be a massive change. For not only for the protocol but like for the clients but for the entire ecosystem and if we are asking for this bigger change we shouldn't ask for another massive change in five years. Yeah that that that's my I just want us to start thinking strategically about it.

**Tim Beiko** [45:54](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2754s): Thanks for the context and yeah Sudip shared the talking question in the chat as well for reference for people. Yeah Felix have your hand up. 

**Felix** [46:05](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2765s): So basically one thing to understand is from what I understand about it. The Verkle implementation is very vulnerable to Quantum Computing should it come to pass because it's like 100% based on the elliptic curve cryptography. However current ethereum is generally reliant on elliptic curve cryptography and it's built into the protocol at a very low level. So basically it is if an exploit like if a quantum computer comes to pass which is capable of breaking this cryptography then we are screwed generally. Because I mean in the future there are these long-term plans to introduce full account obstruction but until this is done we are going to be vulnerable to these types of things. And it's a we are very far away from implementing full account obstruction. I think. So this just something to keep in mind.

**Tim Beiko** [47:15](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2835s): Thanks, Ignacio

**Ignacio** [47:19](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2839s): Yeah so just to add what on What Felix said I want to also remind that on like three months ago. We included blobs in the protocol and blobs used KZG commitments which also use elliptic Curves. So as far as I know the strategy there was considering in the future changing KZG commitments to Starks to make blobs be Quantum resistant. So yeah I just want to make the point that unless something really relevant changed in the last three months regarding a real risk of quantum computers being real. I think maybe the overall sentiment around this risk shouldn't change. But what I know is that Scor has started talking with the research team in the EOF. So they can start talking with like experts in the field. So we can get a more updated forecast. I wouldn't call it forecast. But you know sentiment around this risk which usually like people always think is 10 years away but at some point that will be actually true. And we should have a more like overall plan on this topic not only for Verkle but as said before for a lot of other things for blobs for signatures for having a accounts abstraction or things like that. So yeah just that.

**Tim Beiko** [49:01](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2941s): Thanks Guillaume? 

**Guillaume** [49:05](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=2945s): Yeah try to answer all the questions by Andrew in order. So one of them is can we rescue  Verkle. Not really because yes like others said it's based on elliptic curves and in fact it gets a lot of properties from elliptic curves. Unfortunately elliptic curves rely all that cryptography relies on DeFi  assumption which is broken in by Quantum algorithm namely some form of the ore algorithm. So if quantum computers come like become a reality which is still a big if even in the 30s. It would break Verkle and like Ignacio and Felix pointed out other areas of ethereum that are probably just as important as the state is not it's not the state is big. But yeah there's a lot of security assumptions in ethereum that's are beyond the state that also rely on that. One thing I wanted to add is or at least to dispute is the idea that if we switch directly to Quantum resistance feature well first we we lose a lot of the features of that verkle was created like there's a lot of things like smaller proofs this is something you you will lose homomorphism things like this that are extremely useful for building for stemming State growth. And doing other things but what I'm getting at is. If we go straight to the final product it assumes we know what the final product is and that's a really tall order because for example we expect to use binary trees for Starks but the Stark like the concept of star star the security of stars is mostly conjectured so in a 15 years frame. Let's say quantum computers happen mid-30s we might discover something that is going to break Starks or um or even some hash function we use. So I think it's a bit optimistic to say we should go straight to the last tree model because we don't know what the tree model is. We will have to upgrade the tree no matter what this is not the last time we upgrade the tree and the advantage of verkle is that we are currently developing all the techniques to update the tree which can be reused later on. So I don't think if we go to Verkle now or let's say in two years and we find in 10 years that quantum computers are approaching fast which is I mean I haven't really heard any experts say that I hear a lot of stuff on the news but I don't see any actual progress. We still don't have a big registers like big enough registers that this would be a Quantum registers that would that would be a danger. But even if it happens we'll be able to react because we'll have all the tools already. So I'm not worried about having to to change in a rush well in a rush in a relative Rush of course if it happens from one day to the next will be will be taken by surprise but if it's like a two-year process. We'll be ready to do this and on top of that there's no guarantee that I mean yeah it's it's a bit naive to expect that we will never upgrade the tree ever again. It will happen the the MPT tree you know. It was created in 2013 -2014. Since I joined the EOF people have been talking about replacing the tree. So there's nothing there's nothing guaranteed like there's definitely no guarantee that we will never have to replace the tree whatever it is. So that doesn't mean we want to ignore everything that is like that doesn't mean we want to ignore Quantum resistance we should have this conversation but I think we should separate it from the question of verkle. It should really be is Ethereum Quantum resistant is the internet Quantum resistant and then not make that a showstopper of Verkle.

**Tim Beiko** [53:38](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3218s): Thank you. Yeah so I agree that separating out the quantum risk broadly from like Verkle and possible  Verkle Alternatives is probably the best way to think about this. And you know there's a lot of different ways in which you know quantum computers could affect ethereum and and more you know things much beyond that. So I guess what's the right place for people to discuss this like we're not going to figure out ethereum's Quantum strategy in the next 20-35 minutes. Yeah, is there some place that people are discussing this or people would want to discuss this or some concrete thing that people would want to see happen.


**Guillaume** [54:33](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3273s): I was hoping for Josh to answer that but if he's not around. Oh yeah Josh is here.

**Joshua Rudolf** [54:44](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3284s): Yes so I'm creating a group where we can continue discussions around this if anyone would like to join I guess I'll drop a link in the Discord after that. 

**Tim Beiko** [54:53](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3293s): Should we should we create just a Discord channel for quantum resistance?

**Joshua Rudolf** [54:58](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3298s): Can also do that yeah. 

**Tim Beiko** [55:00](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3300s): Yeah so we have a cryptography Discord channel. Does it make sense and it's not? I don't know it gets a couple messages every now and then but does it make sense to use that. And then just direct people there and I see Vitalic is among the frequent posters. So if we want to like ask him for more context on the talk might be a good place to yeah to
have that.

**Joshua Rudolf** [55:31](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3331s): Yeah that sounds good. We can continue the conversation there. 

**Tim Beiko** [55:36](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3336s): Cool okay so let's do the cryptography Discord. And continue there and I think trying to figure out like yeah specifically what the estimates are based on. And then what the actual risks are?

**Guillaume** [55:56](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3356s): Yeah if I may add something regarding design itself it's also been built in a way that we can swap last minute a Verkle tree with a Binary tree. But yeah like I said we would lose something but it's still an option. So we can take our time to study the thing and make a decision when you know first we identify that the danger is present and that we have the response to that Danger.

**Tim Beiko** [56:27](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3387s): Thanks and yeah I guess that is that so there's a couple comments in the chat as well. Like this is kind of the second thread is you know given this and potentially other things like different you know developments on different type of trees and whatnot? What's the best place to discuss whether Verkle is the right next thing. So we have sort of scheduled it for the next Fork already. We decided this I think early this year because we wanted to make sure we would keep it as a priority. I know there's the Verkle implementers calls but obviously those are kind of focused on you know actually working on the Verkle Implementations. But yeah, are those the best place for people to come and discuss potential alternatives to  Verkle. Should we do this here and if so what are the factors we want to consider?

**Guillaume** [57:26](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3446s): Yeah so to be clear there is no alternative to verkle currently. There's a couple ideas that maybe in three years will be a correct like an unacceptable competitor to Verkle. But if you want to discuss those ideas yeah we are happy to discuss that on the Verkle implementor call. Just because if those ideas are relevant we want to hear and discuss them.

**Tim Beiko** [57:50](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3470s): Okay anyone else have thoughts on this. Okay so if people have you know alternatives for Verkle. We can discuss them on the Verkle call. And then obviously yes like once we ship pectra we should make sure that Verkle is still the right thing for the fork after. But I think that will be that will be late in if what we want is to ship a state transition and use a different approach than Verkle. So like if we arrived after pectra and we said you know there's this other completely different urgent thing to ship and maybe it's more urgent than Verkle you know that seems reasonable that we would we could make that decision but if we arrive to Osaka and you know we think like Verkle is the thing. We still think we should ship but there might it might be worth exploring another type of tree. That feels like the type of thing we want to start doing now so that by the time we get to Osaka we actually understand what the trade-offs are very deeply. So if people do have candidate Alternatives yeah I think it'd be worth looking into it now and we can discuss those on the Verkle calls. Potus? 

**Potuz** [59:20](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3560s): Can we phrase the commitment of the form by Osaka we're changing the tree. And if there's any alternative to Verkle that wants it to make it to Osaka then it should be at a level that we feel confident as we feel today about verkle being in Osaka. So this might be this might sound impossible but what would be a tragedy would be to delay changing the tree because of some statements about being in early research at the time. So we should probably commit to changing the tree in Osaka with the candidate today being Verkle. 


**Tim Beiko** [59:56](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3596s): Ansgar? Do you want to explain why you don't think it's a reasonable commitment? 

**Ansgar** [1:00:01](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3601s): Yeah I think physically making that commitment would very severely restrict the design space. It basically only realistically would allow for Verkle and maybe one or two potential alternative. And I think what very realistically could happen is that we basically agree that hey given these advances in Decay or something. We think that verkle already has these and these downsides. That we don't like and that within the next 3 years or so. We would
will be at a point we will have Superior Alternatives. And we will not make two upgrades. So we would rather wait for a few more years. I think I'm not sure I'm not definitely not  confident that's where this conversation will end up in. But I think it should definitely be a option that should be one outcome that we might land on. And so I think making this commitment now seems arbitrary. And no I don't see a strong reason for it.

**Tim Beiko** [1:00:56](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3656s): Okay I guess Josh when is the next virkle implementor call? 

**Joshua** [1:01:03](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3663s) So we had one this week next one is in not this not this upcoming Monday but the following Monday. Every 2 weeks.

**Tim Beiko** [1:01:10](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3670s): Okay. So I think yeah it probably makes sense to discuss specific Alternatives there I don't know if anyone wants to do this in the next two weeks. It doesn't feel like the most super urgent thing but yeah it would be good to not wait you know 6 months to do this if we think there are other options. But yeah I agree that like having a discussion there and like people having time to prep and and like actually read up on things is the most valuable way to approach this rather than trying to like come up with Alternatives right now on the spot. Yeah so I guess yeah moving this to the vertical calls and then if I don't know nothing has happened in like 3 four month 3 four months we can follow up on it here again. And yeah maybe one last question I so like what's the urgency to making to changing the tree in the next 24 months. I know we talked about this a few months ago around the state size growth. But I don't know if Guillaume or Joshua you have a quick answer to that.

**Guillaume** [1:02:26](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3746s): I mean yeah it's a stat State Side growth. It's also unlocking a lot of things with statelessness including smaller proofs to do many communication like improve the way we communicate for example between shards sorry rollups if they choose to adopt. There's a lot of features we want to have. And yeah it's also like you said initially it's mostly a state growth thing.


## [EIP-7736 (Leaf-level State Expiry)](https://notes.ethereum.org/@gballet/leaf-level-state-expiry)

**Tim Beiko** [1:02:57](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3777s): Got it. Thanks. Anything else on Verkle or Quantum? Otherwise next steps are the cryptography channel for Quantum and then add a Verkle implementers call for Verkle. Okay next up then we had an EIP by a few different authors Guillaume and Wei a Leaf Level State expiry. I'll post it I guess the draft the EIP but yeah Guillaume you want to give a some
Overview? 

**Wei Han Ng** [1:03:36](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=3816s): I think I can take this. Is okay if I share my screen? Okay so just going to do that and I've also put the link to the EIP in the chat. So I'm just going to spend like 10 minutes going through this EIP. So this better me everyone. So thanks for having me here. I'm going to introduce this EIP called 7736 this level State expiry. It's written by Guillaume and I. So the goal here is to get some feedbacks on this EIP and at the same time to reintroduce the concept of State expiry to everyone because the progress of State expiry has been stagnant in the past few years due to different complications and research paths. So we not only want to make this EIP work but we also want to spark disc discussion on the concept of State expiry how we can integrate different ideas into the protocol. Yeah so without further do let's get right into it. So the motivation for this EIP as I say the previous state expiry Solutions are very complicated and complex to implement and they usually require heavy changes in the ethereum structure I.E address Base extension. So because they are so complicated people are not motivated to proceed with the research. So hence we came up with this EIP 7736 which is a much simpler approach to state expiry and it's also better compatible with  Verkle tree. So this EIP is a state expiry solution that can be enabled after verkle tree is implemented. Yeah let's talk about specifications and the specific details on how this EIP work. I'm just going to talk briefly on the constants that introduced in this EIP but want to highlight on three particular concerns here. We are going to introduce a new concept or new domain or a new field whatever you want to call it called Epoch but this Epoch is not the epoch that we know in the current protocol. But you can think of it as an expiry Epoch. So you have like Epoch length which is the duration of the epoch. Here we denote it as six months then you have the initial Epoch counter which basically the initial epoch and when we implement or execute this EIP. Then we have NUM_ACTIVE_EPOCH which is the number of concurrent unexpired Epoch which is the default value is two. So if you combine this information together you can just think of it as these values denotes when a state is considered as active or not. We will look into it in the next few slides. So changes to the  Verkle tree. So the current Verkle tree structure is like internal nodes. You have internal nodes, you have extension nodes and you also have leaf node. After this EIP implementer we are going to make a change to the extension Node in which we'll add a last EPOCH field or variable to the extension node right. So this additional field is going to denote if a set of value is considered as expired or not. And the exact expired rule which I'm going to show here is as follow right. So for every ‘write event’ the ‘last_epoch’ field is going to be updated with the value of the current Global Epoch that we have. The epoch here again I'm referring to the expiry Epoch. And for any read / write events if the current Epoch the ‘current Global Epoch’ >= ‘last_Epoch’ + the ‘NUM_ACTIVE_EPOCHS’ then is this particular event or this particular operation is reverted because the set of values of this particular extension node is deemed as expired right. So this is the expiry logic that we have. In regards to the how client teams want to do the expired logic like putting away the expired nodes it can be implemented themselves right. Whichever logic you guys prefer but minimally for each extension node data that needs to be kept our the stand value of the Leaf_node sorry for the extension node this needs to be kept. Because we need to find the location of the extension node and we also need to keep the commitment of the expired extension node which is used for validation when we do Resurrection. So talking about resurrection of the extension Node. We will need to introduce a new transaction type called RESURRECT_TX_TYPE which essentially contains the encoded form of a vector which contains the stem the last epoch and the values right. So this three simple field we are also going to introduce a new form of cost which is based on Resurrection gas cost based on the constants introduced in EIP-4672. The brief logic of how this work is that you send a
transaction then we want to resurrect a certain State. We are going to charge the gas cost after the gas house is charged we proceed with the validation and the validation process is on the high level is something like to just reconstruct the extension Node and from there you can validate against the one that is in the database and you can do a comparison between the commitment if to check if they they are valid or not right. So why or rational of this EIP. So again no ASE (Address SpaceExtension) is required. It's simple it only references the Verkle tree that we have right now except for the additional field that we add to the extension node. And we don't have to introduce like multiple per-epoch trees as compared to the previous expiry Solutions. We are going to have like smaller Resurrection proofs because we just need to provide the necessary data through the transaction. The gas cost for the Resurrection is clear and o Verklel we only need to expire the cold data the hot data or the active data will still remain in the state it's for comp compatible so in the future if you want to do like es or multiple epoch trees is still possible right. And some questions that we have while writing this proposal. Most important question how effective is the expiry? So it's a simple approach but we expect that most but not all data are deleted. We still have to do the simulation to check against the corner cases. So we need to post the statistics when we have done that. And the second question kind of the also the important one is why only right events update the last epoch counter because if you think about if it include read events as well it will refresh the last epoch in the extension node. Then essentially it's considered as a right event because you have to recalculate the commitment of the exension Node. Then you have to update your database so it's potentially adds a DoS Vector. So some potential solutions that we have is to increase the read event for the initial epoch read to match that of a right event but we are still exploring other Solutions as well. So feel free to give your opinions. Yeah, that's it for my introduction of this EIP again. Welcome everyone to go to the discussion page to give your opinions and feedbacks on this EIP and hope to spuc some more discussions on the expiry as a whole. Thank
You.

**Tim Beiko** [1:11:01](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4261s): Thank you Han. That was great presentation. Yeah if if you can share the slides either here on the agenda that would be great. I had a question and then there's another one by Lightclient but basically this is clearly more efficient on like flatter trees but is there is there aside from like the efficiency Gain Is there any other like reason why this has to be closely coupled with Verkle like if we switch to like some other pectra tree in the future? Or if we did it on the merkle petricia tree would it still work but just be sort of less efficient or are there some other like dependencies or earth type coupling with Verkle.

**Wei Han Ng** [1:11:44](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4304s): Yeah understood. So I think the nice thing about Verkle tree that let us to this proposal is that the invergo tree the values are sort of like you can think of it as group under an extension known. So when they are group we can expiry all of them at once. If all of them are not being access together right. So if you compare that to like for example MPT it's not the case. So it's harder to do that on MPT currently based on what I know for other types of tree it depends on what kind of data structure that you're referring to but if you have the sort of an a feature of group elements together then maybe a similar proposal will work if not then I think is we have to consider other alternatives. Yeah so that's my take on that.

**Tim Beiko** [1:12:35](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4355s): Awesome thanks. Then there was a question by Lightclient asking does this stop the state from growing or does it just means it keeps growing but slower forever?

**Wei Han Ng** [1:12:50](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4370s): Yeah I think that's a good question. So definitely we are not bounding the state completely.  Definitely the state is going to grow slower but at at what rate is going to grow at and how efficient it is again at expiring the values we still have to do a simulation on against the all the entire state that we have and do the expiration and get the statistics. So I don't have the exact answer for that we have to do more analysis on that, yeah. 

**Guillaume** [1:13:25](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4405s): Can me add something, yes like it's not necessarily tied to Verkle trees but it's really especially interesting with  Verkle trees. Because the Verkle tree is very shallow and has very extensive nodes. The nodes are very large but their storage on disc is very small. So while you're not bounding the disc sorry while you're not bounding the size on disc you only retain long term the smallest part of the tree like yeah the structure that remains on this long term is much smaller than it would be in the MPT. 

**Tim Beiko** [1:14:02](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4442s): Got it. Thank you. And there's a last question by Lukasz asking would client teams be expected to prune expired nodes in the background? 

**Wei Han Ng** [1:14:13](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4453s): Yeah I think that's a logic that you guys determine. It really depends like some client teams you can choose not to put it at all right. So it really depends on the implementation.

**Tim Beiko** [1:14:27](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4467s): Got it. Thanks. Any other questions or comments? Oh yeah Daniel?

**Daniel** [1:14:32](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4472s): Yeah so I just wanted to say that the the EIP from a from a teku point of view I think is very good for me it's just really the questions I mean every sort of State expiry comes potentially with very bad ux. Because I think it's very hard for users to understand that whatever state have
disappears after some time if they do not write it in the last year something like this. So I mean for me is more the question if you really want to do that in in the first
Place. 

**Tim Beiko** [1:15:11](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4511s): I guess this is more a Dev ux than user ux thing in a way right. Because as a user you would expect that your wallet would sort of handle this for you right. Like you tell them you want to interact with this contract track make this transaction and then the wallet will have to figure out like what when is it but.

**Daniel** [1:15:32](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4532s): I mean yeah but there are some cases you know people are losing their their phones with the wallets or they I don't know they just uninstall their old wallets and reinstall a new one  and it might not have all the data for the resurrection. So I mean it's not impossible that there would be users who cannot resurrect State anymore. The only the the only thing would be if there's like a third party where you can go to like verkles or something like this. 

**Tim Beiko** [1:16:05](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4565s): Yeah and I think that's always been the assumption that like either you can save your like copies of the state or you rely on some third party to give you a proof and then you know this is like many many years ago the other idea that we had was like State rent where you can think of a way you can think of like State expiry as like an out of protocol market for the state where either you you manage it yourself or you pay some third party and state rent is effectively an in protocol market for the state where you could pay ethereum to keep it for you forever. But I think we would need to discuss this but I don't think there's a way to resolve that. It's kind of like the core tradeoff. Any other comments or thoughts? Okay Ansgar has some comments around just understanding the density of the nodes which might be worth looking into where. yeah so there's the discussion trail on eth magician is that the main way for people to continue the conversation and and like reach out to you. 

**Wei Han Ng** [1:17:27](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4647s): Yeah I think just go into the discussion link we can yeah continue our discussions there. 

**Lightclient** [1:17:36](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4656s): Yeah maybe I missed this but was this something that needs to really go in with Verkle from the beginning or was the expectation that this would be something that is added in at a later point?

**Wei Han Ng** [1:17:48](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4668s): No we can do both right if you choose that we think that this EIP is good to go with verkle directly then we can do that. Or we can decide when we want to enable this EIP after Verkle is implemented. Yeah so that's one of the good things as well about this EIP. 

**Lightclient** [1:18:04](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4684s): What do you mean by the ladder like we can just decide to enable at a later Point like we have the same similar situation with the MPT. We could decide to change it or to change the format of the account header but we don't ever end up doing it because this is a complicated piece of code and we're afraid to change it. So is there something about verkle that makes it different in that sense?

**Wei Han Ng** [1:18:27](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4707s): Yeah I think this is mentioned in the EIP as well under the backward compatibility section. So it's power compatible with Verkle because in the the default value for the fork evaluation Point. If you check the extension node structure it is zero it's default to zero. So even if we add this new EIP this new counter field to the extension node. When we recalculate the commitment is still going to be the same. And hence it's better compatible. 

**Lightclient** [1:19:01](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4741s): Yeah okay I understand thank you.

**Guillaume** [1:19:04](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4744s): Yeah just to chime in like Han’s said it's been built to be very backwards compatible because yeah the value zero. All you need to do next time you activate the EIP is to add the timestamp on every right. And then the older tree values the values that were not written since the fork are automatically seen as old but we will definitely not do this during the  Verkle fork because the Verkle fork is complex enough. So that would come in a later Fork. 

**Tim Beiko** [1:19:40](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4780s): Thanks Lukasz?

**Lukasz** [1:19:43](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4783s): So my two sense here is that if the portal Network the devs manage to start the state Network
before we go to Verkle trees and I supposedly heard that they planned to start in like alpha or beta stage this year. Well then I'm I'm all for this kind of expiration and pruning because there would be a good decentralized way to resurrect that. For example the wallet or anyone could integrate to. So just my two cents here. Would be good to catch up with them? How are they going? How is it going for them with the State Network?

EIP-4444 updates

**Tim Beiko** [1:20:39](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4839s): Yeah, we can definitely do that. Okay anything else on this EIP? And okay if not last thing I had on the agenda so I know we've wanted to prioritize EIP 4444s more. Anyone have updates on this? 

**Paritosh** [1:21:11](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4871s): Yeah there was just one tiny update I had made an eth research post on using Torrents for EIP 4444s and there was a request to add the proofs in the torrents. So I've done that and publish a new torrent file. So in case someone wants to I guess download it or use it make sure you use the latest version of the torent. 

**Tim Beiko** [1:21:31](https://www.youtube.com/watch?v=vbh9C2_-TIc&t=4891s): Thanks. Can you share the post? Anything else? Okay then otherwise we can wrap up here. Yeah Thanks everyone. We'll talk to you all on the CL call next week. Cheers Everyone
___


## Attendees 
* Gabriel Rocheleau
* Guillaume
* Enrico Del Fante
* Milos
* Mark Mackey
* Peter
* Justin Florentine
* Scorbajjo
* Damian
* Daniel Lehrner(Besu)
* Lucas Lim
* Ahmad Mazen Bitar
* Ignacio
* Ben Edgington
* Guru
* Kevin King
* Potuz
* Dave
* Danno Ferrin
* Lightclient
* MIkhail Kalinin
* Pooja Ranjan
* Matt Nelson
* Mario Vega
* Andrew Ashikhmin
* Marcus
* Terence
* Mega
* Ulas
* Paritosh
* Julian Rachman 
* Hadrien Croubois
* Mathew Smith
* Pedro
* Spencer-TB
* Ben Adams
* Milen
* Jared Washinger
* Phil NGO
* Somnath (Erigon)
* Felix
* Shruti Gandhi
* Arik Galansky
* Alex Beregszaszi
* Fabio Di Fabio
* Sean
* Joshua Rudolf
* Justin Traglia
* Ayman (Nethermind)
* Marcin Sobczak
* Andrei
* Piotr
* Elias Tazartes
* Toni Wahrstatter
* Ansgar
* Gajinder
* Wei Han Ng
* Ade Lucas
* Daniel Celeda
* Kolby Moroz Liebl
* Anders Kristiansen
* Sudeep (Erigon)
* Radek
* Gary Schulte
* Jamie Lokier
* Saulius
* Lukasz Rozmej
___

## Next Meeting : Aug 15, 2024, 14:00-15:30 UTC
___
## Refrence Links: 

1. [https://notes.ethereum.org/@gballet/leaf-level-state-expiry](https://notes.ethereum.org/@gballet/leaf-level-state-expiry)
 2. EIP -7736: [https://eips.ethereum.org/EIPS/eip-7736](https://eips.ethereum.org/EIPS/eip-7736)
3. [https://ethresear.ch/t/torrents-and-eip-4444/19788](https://ethresear.ch/t/torrents-and-eip-4444/19788)
4. [https://docs.google.com/presentation/d/1zCTf54E7OaMrppUeA_T2S4YWvvgGixvlGt4j0E0s1zg/edit#slide=id.g2f0280057b0_0_274](https://docs.google.com/presentation/d/1zCTf54E7OaMrppUeA_T2S4YWvvgGixvlGt4j0E0s1zg/edit#slide=id.g2f0280057b0_0_274)
5. Call summary on Eth Magicians: [https://ethereum-magicians.org/t/all-core-devs-execution-acde-193-august-1-2024/20648/2](https://ethereum-magicians.org/t/all-core-devs-execution-acde-193-august-1-2024/20648/2)
6. Podcast (audio only)- [https://open.spotify.com/episode/297davcrPXeRxIHnO7BdPK](https://open.spotify.com/episode/297davcrPXeRxIHnO7BdPK)
___


















