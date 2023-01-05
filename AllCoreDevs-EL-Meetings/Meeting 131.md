# All Core Devs Meeting 131
### Date/Time: February 4, 2022, 14:00 UTC
### Duration: 90 minutes
### [Recording](https://youtu.be/_kt-r4J8PJc)
### [Agenda](https://github.com/ethereum/pm/issues/459)
### Moderator: Tim Beiko
### Notes: Stefan Wüst
## Decisions Made
| Decision Item | Description                                                              | Video ref |
| ------------- | ------------------------------------------------------------------------ | ------------- |
| 131.1 | Devnet V2 is launched next week so it can be used by everyone who is ready | [19:22](https://youtu.be/_kt-r4J8PJc&t=19m22s) |
| 131.2 | Further prioritisation | [1:16:44](https://youtu.be/_kt-r4J8PJc&t=1h16m44s) |

**Tim Beiko:**
Good morning everyone, afternoon if you're in europe. Welcome to All Dev 131. Pretty packed agenda today, a ton of upgrades around the merge so some Kintsugi stuff then Kiln, the new metaspec, leading to a testnet and then lots of shanghai discussions as well. There were a lot of people with EIP proposals and I think before that we probably want to have a higher level discussion about generally how we want to shape shanghai and the various potential things we could do in them and then a couple announcements at the end.

## Kintsugi 🍵 office hours

First off i guess on the kintsugi side Pari shared an incident report in the in the comments of the agenda about the issue that we saw on the network i don't know if you just want to take like a minute to walk through it Pari and and like what the high level issues were and and the state of things now

**Pari:**
Sure so the high level issues was in the beginning we had an invalid block that was causing an issue with Nethermind and bazoo because they were missing a check the invalid block led to a network split and one being on an invalid block one being without the invalid block and one set that went into an optimistic sync mode when we deployed a fix for the invalid block we realized that the fuzzer had created another block that triggered another issue in geth causing some nodes to fail to be able to even sync and once the get issue was fixed as well then we noticed a few smaller edge cases in some of the clients once everything was had settled down we pruned some forks got all of the nodes back onto onto one fork and afterwards we were able to get the chain back on track.
There's a deeper summary as well as implications in the incident report i'll just post it here again for whoever wants a quick link yeah that's about it i think

**Tim Beiko:**
got it yeah thanks for sharing yeah the link is in the agenda we'll add it we have somewhere in the execution spec repo where we track like these various incidents like the testnet issue we had at london for example so it could just be there forever for people interested but yeah thanks a lot for putting out putting that together Pari

**Danny:**
I'd say if you're working on hive or other simulation tests make sure to come through this and see what scenarios you can pull out of it obviously it's all generally thick but it's good to not have a regression

**Tim Beiko:**
yeah good point

## Kiln 🔥🧱 Meta Spec

**Tim Beiko:**
I guess next up on the agenda there were the kiln specs released last week i guess maybe it's worth it for daniel Mikhail to just like take 30 seconds to walk through like the the main changes and then yeah there's a couple things after that that are still pending for like an upcoming iteration of the spec but yeah danny do you want to just or Mikhail do you want to just give a quick overview of the change

**Danny:**
Yeah i can talk about the consensus layer mika i can pick up the execution. there there are two pr's that were merged on the optimistic sync spec this is when the beacon chain is churning while the execution layer is still in some sort of sync mode this is not although it's just merged and just released it's not new a lot of client teams have been working on the implementation as the pr is up. additionally in the code base merge is was a terrible word to have around and didn't fit the star naming so it was chosen to go with a b star after altair to bellatrix merge you know merge merge the merge vr and things like that was fun. and then a couple of very minor renamings receipt route to receipt routes just to match i think more of what it's actually called maybe yellow paper and a modification this other name to map to the engine api mikko do you want to take the execution layer one.

**Mikhail Kalinin:**
Yeah sure so the major change on the execution side layer side is the cement exchange of execute payload and fork choice updated they both now has a notion of execution and for execute payload it's been renamed to a new payload and the currently execution is optional for this net call like it it may it may be delayed until the payload becomes the becomes belonging to the canonical chain so this is done this was what was discussed during last few calls and this is done to reflect the current logic of extreme layer clients basically also there is the new handle for the case when the terminal block does not satisfy the terminal block conditions which is a minor change and yeah message order and refinement that has been done like a long time ago but yeah a while ago just and this has been released in this in this version so that's that's it also the out indication yeah we can speak about it in the next item right right

**Tim Beiko:**
yeah yeah okay yeah so those are the changes up to now i guess one one thing i wanted to clarify also for kiln is like are there any test vectors yet and if so yeah okay so basically like trying to like try and question but like you know what's the best way for client teams to test their implementations of these changes so far?

**Danny:**
is marius here?

**Tim Beiko:**
no

**Danny:**
marius is talking about doing and maybe he has i'm not sure and we should cater we should catalogue the testing methods available but he was going to cut some engine api test vectors from guess in previous sprints this is surface bugs both in guess and and other clients before we try to do some interrupt so that's probably the minimum one that's going to come up i don't know like client if how if and how people are using merge mock in their processes i know some clients where some clients were we're not so if anybody wants to speak up and say if merge mock is valuable to their iteration let us know

**Mikhail Kalinin:**
isn't it used in hive also in margin?

**lightclient:**
i don't know i don't think so it's been rewritten to be a better fitting with the hive architecture

**Danny:**
another mind or anyone is anybody think merge mock in this sprint will be useful

**Marek Moraczynski:**
i think it will be useful

**Gary Schulte:**
yeah it's just okay definitely useful there's not a test net to participate in

**lightclient:**
okay it's definitely useful i will get it updated by monday or tuesday if that's okay

**Marek Moraczynski:**
yeah sure

**Tim Beiko:**
yeah that'd be great thanks a lot

**lightclient:**
thank you

**Tim Beiko:**
cool okay so yeah so we have the current v1 release of kiln some tests coming there's two pending additions for an upcoming iteration of the spec one the auth for the engine api and two a new api call get transaction configuration which acts as a sort of heartbeat check between the el and cl that that they're upgraded and ready for for the transition. Mikhail do you have like a status on the on the ask for engine api

**Mikhail Kalinin:**
yeah it's better to ask is martin here on the cloud?

**Tim Beiko:**
oh martin's gonna be late yeah that's why i asked you

**Mikhail Kalinin:**
okay yeah so if think it's about to get merged for this to get merged pretty soon so i've got some attention from martin that it's like in the final stage so gotta go like emergent yeah

**Danny:**
yeah they were working on implementation which i think they've done and are happy with it so if you haven't taken a look take a look but i think this is gonna be merged probably by the time i wake up on monday hopefully

**Tim Beiko:**
awesome

**Mikhail Kalinin:**
Yeah i think it's already ready for merge from my side so just need to double check with martin

**Tim Beiko:**
oh and martin just showed up actually

**Martin Holst Swende:**
yes hello i missed a bit of what needs to be said

**Tim Beiko:**
yeah we were talking about the between the el and cl and how just progress is going on that i think get is implementing yet right now

**Martin Holst Swende:**
yeah it's not it's not in any pr yet there's still some work left to be done mainly to make these see the client part yeah. i mean it's not complicated we just need to find a nice way to to expose it

**Mikhail Kalinin:**
what do you think about merging apr to the stack?

**Martin Holst Swende:**
i have no objections to that i don't know if you guys mentioned but the last minute change that was done to it is to not expose the secret in any logs unless someone objects to this whole authentication scheme i think we should go ahead

**Tim Beiko:**
okay i guess maybe we could leave a couple days for people to review but like monday or tuesday merge it in if if there's no objections does that make sense

**Danny:**
yeah i have no objections by monday this thing's getting merged

**Tim Beiko:**
okay cool and then the other change was yeah adding this add get trend or sorry adding this get transaction configuration endpoint which basically pulls to make sure that the the el is actually ready for the merge mikhail do you just like to send your pr do you want to give quick bit more context on that or

**Mikhail Kalinin:**
yeah sure so basically it's been extended with the not only poland but also providing cl's configuration for el so yeah this method is just called with the main settings of transition configurations which are terminal block hash and terminal total difficulty and the cl sends its local values to el and the el responds with the corresponding local values that it has in its configuration and cl and dl both may match received configuration settings from the counter party and if there is a mismatch surface and error to users also it's it should be useful for infrastructures for large infrastructures which there could probably be a script that just queries every el instance in the infrastructure and it checks whether it's been configurated correctly and whether it's ready for for the upcoming transition

**Marius:**
quick question quick question we have in  focus is updated if the head block hash is is a an empty hash we just return status valid or invalid or whatever we can like why do we need another method if we can just use the use default choice updated with the with the empty hash

**Danny:**
talked about it a bit for sure is updated has like super overloaded semantics already so that this is to just have a clean thing that can think that can be deprecated right after the merge i mean i could go either way but fortress updated is a monster stuck already

**Marius:**
okay

**Mikhail Kalinin:**
Also it's not only like you know to check whether engine apis is working or not it's also to check the configuration and and the the configuration on the outside is going to be in a binary distribution likewise on the cl side so it's a matter of checking whether the client is updated is up to date with the most recent release. in case if these parameters will be overridden and yeah that's also one of the use cases it's probably a minor one but still valuable to have these values exchanged with two clients a surface and error in case of mismatch

**Tim Beiko:**
i'm curious i guess so we have we have basically these two these two pending prs one of which will be merged early next week i feel like we might need an extra couple days for get transaction configuration just because it's it's newer and and and maybe we need teams to like review it a bit more. so call it like i don't know mid late next week i suspect we can have all the changes like both these changes merge in the spec oh andrew you have your hands up 

**Andrew Ashikhmin:**
yeah i just want if we make this change i'd like to clarify what happens if the terminal block hash is not set like it's it's whether it's returned at all like all zeros or what happens and also if there is if the terminal block hash is all zeros or not set then what happens to the terminology total difficulty would be like should it return zero or not nothing

**Mikhail Kalinin:**
if basically terminal block hash if it's set then it overrides the terminal total difficulty you mean that what what should happen when it's set right  you call terminal block hash is all serious

**Andrew Ashikhmin:**
yeah yeah so do do in the api does it return all zeros or did nothing in json

**Mikhail Kalinin:**
it should return all zeros

**Andrew Ashikhmin:**
and for for ford oh sorry not like oh sorry terminal block number then and for terminal block number it will return zero or

**Mikhail Kalinin:**
yeah yep

**Andrew Ashikhmin:**
okay okay i just think it just has to be like explicitly mentioned

**Danny:**
yeah i mean and on on timing tim i this has been going back and forth a bunch of the discord i think that if there are issues with this they should just be surfaced soon and that we should target a release with these two additional methods by like wednesday

**Tim Beiko:**
yeah and i guess my question was if we're going to start standing up like fmri ephemeral devnets do we want to wait until those chain those two changes are implemented in clients like is there value to having a kiln v1 devnet or should given those two changes are probably not huge should we just wait and and have kiln the two be like if ideally final or you know feature complete kill spec and then launch devnet

**Martin Holst Swende:**
i just wanted to point out regarding the oauth thing the it's not tied to any to any network per se i mean it's something that is rolled out first in the execution there it's side by side i suppose for like a month or a release with what's already in the in the legacy and then after on the next release we remove the engine from the unauthenticated report and during that time the cl can start using the authenticated one at any point so it's not like they need to rush to to implement it on day one

**Danny:**
yeah so we can do all of our interop experiments with and without auth as people are rolling out off and then the exchange transition configuration is probably one of the simpler methods to implement and i would say that we should just release and get it implemented also if if there was no call if one if it was not implemented on one cl but it was implemented on el you know el might complain that maybe configuration is not set or it's not listed not hearing anybody but also as the transition comes they would still be able to communicate so neither of them really put like a hard blocker on the core of the functionality here

**Tim Beiko:**
okay so does that mean i guess we can probably launch devnet like next week with whatever clients have something ready and obviously the week after that do an another one with with the yeah

**Danny:**
yeah i agree roll out v2 v2 is really an extension to v1 not a breaking of b1 and we should anyone that's ready next week we should begin you know some interrupt experiments and and super transient does that

**Tim Beiko:**
cool and i guess i'm curious yeah generally do teams have a feel when they're ready for that just to help like Pari and others coordinate there  if not we can we can chat about it in yeah in the discord yeah that's yeah let's do that so once once you have something that you think can work on the devnet reach out to Pari just message in the the merge general discord and we'll get a first iteration next week with whoever's ready and and grow it out the week after

**Danny:**
oh and marius you did join are you gonna cut some test vectors on the engine api against Geth

**Marius:**
yeah so we had a bigger refactor of the sync and so i had to rebase so i implemented kiln before that and i had to rebase it now and i managed to f*ck some stuff up so we have some regressions in the code against the test vectors but i'm going to create some new ones i'll be on holiday next week though but i'll be still doing that so yeah nothing changes

**Tim Beiko:**
on holiday but still working okay it's not the end of the world if they're not there next week don't burn out but yeah we'll be waiting for those from you in the next couple weeks.
Cool. Anything else on kiln or the the merge implementations so far?

**Mikhail Kalinin:**
I have a very small thing related to engine api there is the statement in this pack and the engine apis back that eth namespace of json rpc api should be exposed to the same port to provide consistently a client with edh functionality that is needed for to pull eth1 data and there was a suggestion there is a suggestion to restrict this like broad requirement to to have it to have instead of it a list a subset of pth methods that are required by consistently clients i'm just wondering what do people think about it is is there like strong opinions on why should we have a list of methods instead of like entire ideation in space if there is no because we'll just keep it as is in this pack and will not make any changes

**Micah Zoltu:**
so the east namespace currently is not well specified like where there's work going on to try to get it well specified but like clients are inconsistent between each other on what they return how they return and how they deal with certain situations it'd be nice if we don't port that forward to communication with the consensus layer. i would much rather see us have a very much more narrow but very well defined spec for what is required for communicating with the consensus client

**Mikhail Kalinin:**
the problem here is that consent client might have different subsets of methods that they use that they rely on and probably probably they will need to be the functionality of serial client will need to be extended in the future and it will probably depend on on one of the if methods that is presented in all el implementations but is not in this list in this case we'll have to update the engine api stack to provide cl with this that method having this like broad definition makes it easier so this is

**Micah Zoltu:**
i feel like what you just described is the right way to go about it like if if we need to if some new feature is needed for the communication between the two layers i feel like the proper way to go about that would be to you know come to a consensus on it get agreement on what that method is how it's defined specify it well and then have people in the implant rather than just being like hey we've got this giant pile of data that you know maybe some clients and maybe some don't or maybe they implement differently we don't know and then we run into problems later because we're relying on that old thing that isn't well specified

**Danny:**
yeah i do i think i agree with micah i the it'd be good to enumerate which methods clients are using i don't think that there's going to be like a huge disparity between between the clients and you know this endpoint is supposed to be used for very particular things so it's probably good to have it well specified. I think but i don't have the knowledge to enumerate those myself

**Micah Zoltu:**
the other weak argument is just that if someone's building a new execution client they may not immediately implement the full east consensus layer and knowing exactly what is necessary to be a valid execution client in order to work with the cleanse layer but not necessarily everything to provide a full json rpc is valuable so just knowing what the set of requirements are so that you can be confident you will work with all of the consensus clients

**Danny:**
good fine okay

**Mikhail Kalinin:**
i was like assuming that what is listed on the if ricky jason or this api is presented in all clients and supported by all clients and this is the subset that the cl client may rely on

**Micah Zoltu:**
so what is on the someone else might be able to correct me on this but i believe what is on json rpc api is was pulled mostly from guest source code and we have not yet validated that everything on there is available in all execution clients i have not reconciled the differences so you know different clients will return slightly different things for each of those methods depending on which client you're talking to which is part of the problem here is they're not well specified and so you might get you know just as an example i'm off top of my head i don't know if this is real but like one client may send you a number formatted as a you know json number another one might send it as a hexadecimal string and so that's like a subtle difference that could very easily break something if it's not well specified

**Mikhail Kalinin:**
okay okay so yeah one of the way to do this is to just make a table of methods and ask see your client implement their stems just to feel it with yeah

**Danny:**
i i go my god it helps ensure that we make sure those are very well defined as opposed to the whole name space which is still in flux okay

**Tim Beiko:**
yep cool anything else on that  okay last topic we had for the merge

## Post merge testnets

**Tim Beiko:**
last time we discussed test nets and what that would look like post merge to ideally give the community a heads up so that they can start moving the test nets which will be supported post emergent and not be fully surprised if if some of them don't work after the merge the high level we agreed to like saying we would want to have at least one test net that has like a pretty fixed validator set which is stable and people can just use as a as a staging environment for their applications and we'd also like to have ideally another one where maybe the validator set is not as stable and and people and client teams can use as a way to test that their software works when say the network is not finalizing and and stuff like that peter has suggested we fork Ropsten into the merge deprecated shortly after fork sepolia which is the new proof of work test net into the merge and and use that as a new test net so we we get the experience of forking Ropsten moving from proof of work to proof of stake but Ropsten has pretty big legacy so deprecating it means we don't have to like carry that huge chestnut sepolia starts with a smaller state so we can we can reset there for Görli would into the merge we maintain that as well and then Rinkeby would just not not fork there were a couple conversations on on github about that and and generally i think danny you agreed that Görli Prater makes a lot of sense as a as a...

**Danny:**
yeah yeah something that looks close to mainnet and is stable

**Tim Beiko:**
yeah and then there was i think the other concern is how do you actually do an unstable test net so first i think we we discussed the idea of just like you have a public set of stakers and then that means some of them will like you know will drop off and whatnot. adrian in the discord seem to think that this is probably like a weak form of chaos and and we might be able to actually do better if we if the the validator set is also pretty controlled and we can do things like periodically shutting down end portion of the validators and and introducing forks and whatnot so it's that you know by by controlling actually the the set of validators we can we can be more mindful about how we want to create chaos. and then there was also i think nimbus worked on this this insecure test net so to like explicitly explicitly test some some attacks on the beacon chain. i guess generally the people agree with like the idea of having like one at least one application stable test net which would be Görli, Prater after the merge and then we'll have sepolia as well and i'm not sure how exactly but to have that one be a bit more chaotic in a sense does anyone have like oh andrew go ahead

**Andrew Ashikhmin:**
well it's my personal opinion but i see value in having a hairy test net like Ropsten so i i wouldn't kill Ropsten because though it's very hairy it's it's a better reflection of the main net 

**Tim Beiko:**
what part of it do you think is valuable to keep?

**Andrew Ashikhmin:**
well the state the state of course Görli

**Tim Beiko:**
i think Görli state is probably as big right now but it's maybe worth double checking that

**Danny:**
and i will note i think it says before a tool at a disposal is a modified version of the deposit contract which allows for the issuance of like a token so it's gated so we can essentially utilize the proof of stake mechanism with this contract as you know something that looks like a proof of authority so for a net that you wanted to do more structured one you know make sure that the community can't overrun it but two also make sure that you control enough of the validators that you can you know turn half of them off and on the skating mechanism works well and that would it essentially turns it to look like the way Görli's clique works today in some sense right.

**Tim Beiko:**
okay i don't think yeah we don't have to figure this out today i do think it's valuable for for teams to think about it and share you know ideas i saw thomas you just showed something the issue and generally you know i think pushing folks towards Görli sepolia as very likely to be around after the merge i don't think Görli i don't see a reason why gory would shut down so that one seems just obviously going to be around sepolia very likely as well Ropsten seems like there's an uncertain uncertain future there yeah so if if if you're wondering which which Testnet to deploy on i think zepolia and Görli today are probably the most important one rinkaby a lot of people deploy on i think is the likeliest to be the first to be shut down so if you do have your application on ranking b you should start looking at moving over to other other testnets.

any other thoughts comments on that?

## Shanghai Planning

**Tim Beiko:**
Okay so next up on the agenda i guess to put this in context on the last call we had very little time to discuss shanghai but we we in the last couple minutes i brought up a series of of evf object format EIPs so 3540 3670 3860 and and both in like the last couple of minutes of the call and then i think shortly after the discord there seem to be like strong consensus that those three should should go into shanghai or at least you know be moved to cfi so we can start we can start testing them on devnets once once we're we're done with the merge work. and then obviously seeing those three potentially going into shanghai a lot of people came up and proposed a bunch of other EIPs that they would like to see into shanghai so there's different evm related EIPs there's 3074. there's the whole thing about lowering call data costs and and so there's the eip-4048 that we talked about and Vitalik has a couple new proposals today and then beyond that there's obviously other things that like we'd like to do in shanghai that we've mentioned and people just like didn't put on the agenda for this specific call but there's obviously the bls pre-compiled and probably the other biggest one is withdrawal the beacon chain which does not have an eip yet. so i think you know it's probably a mistake to like go over every single eip and and like in a ton of detail and and i think the fear that i have is to like say that say that like you know this and this EIPs are included in shanghai and then in two calls we say this one and this one and two calls will say this one and this one and we get to a spot where like the merge is not even out yet and shanghai is already bigger than any other hard fork in in history so i guess i'm i'd be curious to hear you know from just different client teams what not like high level how do you think about like prioritizing things in shanghai like what are like the i don't know if it's like buckets or like most important things and then from there maybe we can like go into the the yeah go into the different different proposals and actually yeah i'm happy to start with you actually you have a comment and i know there's like like four or five different EIPs that that are all somewhat related so yeah if yeah if you can just explain how they relate to each other and and what the whole call it like evm improvement bucket looks like that would be really really valuable

**Alex Beregszaszi:**
can you guys hear me yes  okay so i would say there are like three different categories of those proposals the first one is what i think should definitely go in as soon as possible and i would start with the limit init code limited metering it code which i believe maybe is 3855  that is that is not introducing a new feature that is rather addressing a missing metering aspect of the system but it also is like a building block for the other changes especially the validation eip and there's another one in the same category which i think is 3860 that puts zero instruction and this was also discussed like i think last year during the last potential hardport and that is a really minor eip but it would help solidity quite a bit so these two are one category i hope this could go in and they're small and have been discussed at least a limited edition has been discussed with the goitrium team and to some extent.
the second category is just the the baseline of the eof ak evm object format changes and that is only two EIPs again so that's 3540 which defines the the core proposal it only introduces the code and data section and some basic rules around those but it doesn't really introduce any any upgrades or any other changes and together with this is a 3670 which is the code validation i think these two should definitely go in together and these have been around for quite a bit.
and then the last category is the actual features and there are two feature EIPs one is the static relative jumps i can't recall the ep number now but i think that is also quite stable it would help solidity and other languages to use static jumps for pretty much everything with the exception of return from headlight function calls because those still need dynamic jumps so the cip just introduces static relative jumps and doesn't remove anything else.
and then the last erp is what we have been working on for the past i would say month and a half but it actually started like half a year ago with an implementation in evm one and this is this functions sections proposal which is i guess quite a bit more complex than everything else i mentioned so far. it all depends on when shanghai would come but at this point i'm not that hopeful that the cip would would be considered for that but this would be the last stepping stone to actually get rid of dynamic jumps entirely. the static relative jumps jump EIP and this function sections both have been discussed with the solidity team and they expressed interest but it's still early so i think this is the summary from epsilon

**Tim Beiko:**
thanks that's that's very helpful i think it's probably worth it yeah to get a couple similar summaries from like different people who who who propose stuff and then we we can have a more general discussion. greg you had basically two as well that are also evm improvements so the simple subroutine yes and then the safer control flow do you want to take a minute to go over those 

**Greg Colvin:**
yeah i'll try and be faster than usual 2315 remains  responsive criticism of the last one it got pushed towards back to where it started and a little further as as almost pure mechanism and is now static and it's relative and using the same conventions as the static relative jumps so those get along together and it's pretty much as fast as i know how to make a subroutine go or as anyone's figured out for oh 75 years now but the most important thing for me is the safer control flow which is not a proposal for any op codes it's a proposal for an algorithm at validation time so that's why it's very important to get the validation algorithms in so that we can do other things like this and we want safety we never seem to know what it means it can mean lots of things but i explicitly define it here as a safe program does not encounter an exceptional halting state and when it's turning complete you can't totally validate that but if you follow reasonable rules you can check a lot so that a valid program will only hit an exceptional halting state if they run out of gas or blow stack in a recursive subroutine call and that can be established at validation time given the other EIPs we have so we have ways to do static jumps and subroutines and given that if you're using the existing jump that you use it in a static manner which doesn't just mean that you have to push the address right before you jump, the algorithm can track the track the constants on the stack enough to say oh this one actually was pushed as a return address for self routine so it's okay. so that's a package that i think it's important to basically get the level of safety we've been talking about for the last five or six years. without imposing any further structure any further up codes just an algorithm to run. so those those are what are on the table for me

**Tim Beiko:**
got it thanks sir thanks for sharing i think the next one on the list was eip3074 i don't know matt do you have any updates on that or i i know we've spent a couple calls in the past discussing it but yeah has anything changed from the proposal for for london or is it still generally the same thing

**lightclient:**
it's generally still the same thing we've talked about adding an extra parameter into the auth op code to allow it to be forward compatible with a world where we want to remove ecdsa as the default authentication mechanism for accounts but generally the proposal has not changed since mid last year

**Tim Beiko:**
cool thanks

**Sam Wilson:**
the only other thing to mention is that they're we're having a couple thoughts on where we could go after 3074 and one is like a create three or or off usurp where you can deploy code and replace an eoa and that's something we're toying with but that's like far down the road

**Tim Beiko:**
got and those would like build on 30 74

**Tim Beiko:**
yeah exactly so yeah you put in 3074 it introduces the authorized address and then you can build on top of that

**Vitalik Buterin:**
is it the replace code with replacing the like m e08 with code things strict not strictly dependent on 3074.

**Sam Wilson:**
like we just have one way of doing it with 30 74. i see it right okay  got it

**Tim Beiko:**
and then Vitalik you had a comment about different basically new transaction types which could carry blobs of data and hence reduce rollups costs there were two proposals do you want to take a minute to like walk through each of those

**Vitalik Buterin:**
sure so the two proposals are very similar basically one of them like just does a little bit more plumbing work to move some stuff into the into the beacon chain that eventually needs to be moved into the beacon chain anyway but the core idea of both of these proposals is that so today we have the execution blocks that have transactions and those transactions have call data and roll-ups today use transaction call data in the future we're going to have shorted data and the way that it's looking like sharded data will be introduced is they through this concept of blob carrying transactions which is basically a new transaction type where there is a transaction header which just looks like a regular transaction except it also has a cryptographic polynomial commitment to the to the blob and the blo the headers of all the transactions would still be like in the long term would still be broadcast that included everything would have would happen with them the same way as today but the blobs would not be like passed around the main beard of your network they would be passed around with like charted beard of your stuff and the data availability sampling and and all of that technology. so the long-term goal is basically that sharding would or that these blobs would give us a total space of like somewhere around 32 megabytes per block and that could be used by rollups and like other data dependent applications and this is 32 megabytes like this data would not be directly accessible to the execution layer because the intent would be that you you should be able to like verify blocks without actually having the blob so the attack would be to make the whole birds of sharding is that it should be possible to have a network where you don't need any single actor to download all of the data and so the blobs would be this extra this extra much bigger piece of data that gets committed to but in the channel that everyone sees but broadcasted through this different channel where not everyone needs to download it so that's the long-term future of sharding right so the idea of both of these proposals is to bring forward the transaction format that would be used in sharding and basically implement it much more quickly but don't yet do the actual starting right so basically yeah we would have these web transactions and the contents of these blob transactions would be if like you would have the the the header you would have the block commitments you would have the blob but the blob would still be part of the transaction contents and it would still be part of a block and like everyone would still have to broadcast it and download it but there are a couple of advantages so one of the advantages is that it has the eip 4488 style benefit that there is a separate limit on the total on the total amount of data in this scheme so like a blog can't have more than two megabytes but there is a separate eip-1559 update update rule that makes sure that it stays basically the the fees adjust and so until like the usage really really picks up if you if you would be extremely cheap for it and it also has this feature that the the transaction execution actually cannot touch the blob the the blob contents it can only touch the blob header which me it which just makes it much easier to have like basically do things like forgetting the blob contents much more quickly and like generally it makes it a much less of a burden than having like just i'm having call data where like you it's it's more difficult to treat it because you don't know like whether or not some piece of execution depends on like accessing some random bytes somewhere in the middle of it. so the yeah different so the there's two EIPs there the simple version of the eip it basically just implements the transaction type and it implements this in this very black boxy way basically it just says there is eu EIP 2017 transaction type and there is this black box function that checks the blob and against against the commit the the commitments in the header and then there are a couple of pre-compiles that let you access the blob like or basically prove things about the blob and those pre-compiles would be needed for optimistic roll-ups and zk roll-ups to be to be able to actually interact with the blob data the more advanced version does a bit more plumbing and it basically moves the blob contents out of the execution chain and it moves them into the beacon chain and this is something that we are going to have to do for full sharding down the line anyway but the basically the more advanced version of this EIP does this basically does this immediately and so the plumbing just immediately turns into you have like this one transaction object that gets passed over the network and then only the header gets included in the execution layer and then the actual blobs and the blob headers would go into the or or the blob commitments would go into the beacon chain and then there's eventually once we do a short like proper sharding and data availability sampling it becomes much easier to take the blobs out and start handling them in a different way. so i guess i yeah yeah in terms of like when i would like walk to stevie is included i like i personally see two possible paths but there could be more one of those paths is to be to try to do the simple version and get it included in shanghai it is like possible like and this could could be as an alternative to 4488 it is more complex than the then for 488 but it's still like totally within you know within reach of implement of implementability and it's like much as simpler than a lot of other things the other possible path would be that if we decide that i think if we decide that either of these is infeasible to do by shanghai then we could basically do the more advanced one possibly in the forecast for shanghai and then still do eip4488 asap and so basically we end up doing both doing both of the stuff gaps

**Tim Beiko:**
got it thanks that's that's really really helpful sorry just yeah moving on because there's a few more so then crowd i know can i

**Danny:**
can i highlight one thing this requires a trusted ceremony to do the kcg commitments correct

**Vitalik Buterin:**
yes correct

**Danny:**
and there's a dependency there right

**Vitalik Buterin:**
but that's cute like that can't be done by an independent by a completely separate group and there's months to do it

**Danny:**
yeah yeah absolutely absolutely i just don't want us to go down this path without acknowledging that that needs to be possible oh yep

**Tim Beiko:**
and so yeah another big bucket Dankrad i know you've been working a lot on on stateless and there's a couple EIPs that would help lay the the the the path for it do you wanna do you wanna walk through those quickly as well

**Dankrad Feist:**
sure yeah so so i i added some EIPs that that we roughly started discussing earlier when i introduced the statelessness roadmap where the general idea was we have some gas cost changes that we need to make for statelessness and we want to get those in as early as possible which is to get applications developers yeah work in the correct model rather than continuing to deploy contracts that will be inefficient in the in the future model and then introduce the market partition sorry freeze the market producer tree and replace it with and add a verkle tree commitment and then as the third step to to replace the frozen root with the verkle tree roots so that we can have full statelessness with witnesses for everything and so the EIPs i introduced for that are 305 8 3060 and 3062. 3058 is about the activating self-destruct that's for me the the highest priority overall like self-destruct it has been discussed many times deactivating it there are many good reasons for it but particularly in the context of statelessness where we where we will have the account storage separated from the from the root of the account so they aren't like there isn't really an easy way to to change to access all that anymore self-destruct would become really complex to implement so we really want to get rid of that 3058 is the simple version which simply says replace self-destruct with send all and it simply sends all the funds to the caller but does nothing else. so there has been an analysis there's basically one major known contract that uses this and there is an alternative way for them to to be upgraded and to implement this so that would be one thing i would suggest for shanghai

**Martin Holst Swende:**
when's the one big contract that uses this do you then refer to upgrade in place by self-destruct and then create two or do they mean something else

**Dankrad Feist:**
no i do not does does anyone use that i'm not aware that anyone uses that i think that the contract that i'm referring to is the spine finance contract and what they do is they actually replace with the same code but they currently there's a problem that's basically a a contract that has been used is in a state where anyone can take the funds so that that that problem can be fixed. i'm not aware of any contract that that upgrades using create two

**Martin Holst Swende:**
yeah but are you not aware because you've searched and not found or?

**Dankrad Feist:**
yes someone has done the search for this yes  that was a few months ago though so i guess

**Vitalik Buterin:**
right this was like some you know like there was someone who like was like be explicitly assigned like what's the deal was it even a grant or something like that like basically the job of like looking for things that it would break and they only found that in that fine finance thing

**Dankrad Feist:**
so in terms of so that's the only one there where some others where the code was unknown and high in finance was the top one the one with the major deployments that had i i don't think they went 100 through all contracts so there's still a long tale of smaller contracts that someone might want to look through but they are much smaller value and much smaller dependence

**Vitalik Buterin:** got it.
by the way after we're done with this one i just reminded there's another breaking change that i think i think right as the importance the the the the verbal thing that we should thought that we should talk about but this is about the chunk gas costs but maybe finish this first but yeah

**Dankrad Feist:**
so if we are very concerned about like self-destruct that we're gonna break something when we introduce it i wrote down an alternative version that's 3060 that basically ends like the end result is the same but it goes through a phase where the the self-destruct upgrade gas cost increases exponentially over a few months and so the idea is that it seems that many people in the ethereum ecosystems don't watch out like for roadmaps and changes that will be introduced and so on and that includes application developers but in this case anyone who still uses self-distract would notice over those months that hey my gas costs are increasing exponentially maybe i should check what's happening and they would hopefully have enough time to safely upgrade their contracts in that time frame or get all the fans out that are still in there coordinate something. so that's 3060 it of course is a little bit more complex but also not super complex and yeah would be would be an alternative if if we think that there's like yeah we should get everyone ample notice and make sure that they will notice that something's happening.
and then so so one of these two i would really like to see included in shanghai if possible then there's also or 3062 which is which i've unloaded previously we have had written it down as one but that's the actual gas cost changes that that basically introduces the yeah the the the witness costs for verkle trees what this basically does is it adds a new cost for accessing code so that increases gas cost and there's also a decrease in gas cost when you access adjacent storage slots or slots that will be adjacent with local trees and the latter means that that clients will have to have a certain database layout implemented in order to not make that  a dos factor i think Guillaume is still in the process of of communicating to all teams whether they will be able to achieve this so this is definitely a somewhat deeper change and yeah and yeah more complex than just the deactivating self-destruct and i guess like there has been the idea of just uncoupling them and just do the increases first which clearly doesn't introduce a dos vector i think i'm not a big fan of that because that yeah i think like application developers would be annoyed if we strictly increase all their gas costs without giving them anything in return so if we can't do that then we might just have to wait with those changes until the actual introduction of work retrieves but i think it's still interesting if the database upgrades are progressing well i think this eip should still be considered because i think it's best to let applications become efficient as early as possible because all the contracts that that are deployed in the meantime are all very likely to going to be sub-optimal once worker trees are introduced.

**Tim Beiko:**
i think one i think this was everyone who posted something on the agenda one thing i think that would be valuable danny i don't know if you have i know there's no eip for it yet but do you have a high level idea of what beacon chain withdrawals will imply yeah execution layer

**Danny:**
yeah so essentially it's the exposing of a commitment to withdrawal receipts and then the consumption of those commitments at the execution layer by a normal transaction which would move the balance of that receipt into a contract or account specified in that receipt so this is a pre-compile or a special contract or something that essentially a normal transaction can be hit with the proof of receipt against commitment and and track there the receipts are indexed so as simple as a bit field in the state can mark the consumption of the receipts. i believe that alex has a lot of this written down and we're actually gonna be meeting in person next week and plan to have something of a draft to be shared by them early it's commitment to receipts consumption of receipts by a normal transaction moving the eth into an account and then the tracking of consumed receipts

**Tim Beiko:**
got it thanks and then finally like there's obviously people who didn't just post their eep on on on the call agenda and and and there's a couple like other valuable ones we've talked about in the past 2537 keeps coming up so the bls pre-compile is is one that people keep saying we should have we we had i think a couple calls ago a discussion about the transient storage up codes eip 1153 and i know there's a couple others that have been pending for like a much longer time i think thomas you were championing eip2937 to have the i actually forget the title sorry yeah saving the historical black hashes in the state oh 29 30 sorry so there are others as well and so you know off the top of my head there's probably like 15 maybe 20-ish that are being considered across like very different buckets there's a couple comments in the chapter about how anything that increases throughput reduces transaction fees is probably something you want to prioritize whether that's a 4488 or or a simple mini sharding i believe it was called and yeah and you know every everything else like i think the evm upgrades have been have been pending for a long time i guess first of all you know i i'd be curious to hear maybe from client teams like what are you think like the top one or two things that are like most important for for for shanghai that's probably a good way to like start thinking about this and yeah and andrew i see you you have your hands up

**Andrew Ashikhmin:**
yes so because we desperately need scalability i would say something along the line of blob carrying transactions is priority number one either in its simple or more complex form and priority number two is the basic blocks of evm improvements so 35 40 36 70 and 38 60. so my understanding that those three are the basic building block and priority number three is deactivating self-destruct is in its simple form maybe or made it more complicated but to deactivate self-destruct that would allow us to that would simplify the evm would allow the code trends things like that that yeah that's my take

**Tim Beiko:**
thanks and any other client team wanted to share your thoughts

**Martin Holst Swende:**
yeah i don't know if i speak about forget though we haven't really discussed it internally i would agree with what andrew said at least for the first two i agree about we need focus on scaling but i have not really started the whole blob proposal in depth so i i think

**Tim Beiko:**
it's a new proposal so yeah

**Martin Holst Swende:**
i mean in theory i think it's great but i i need to get it more also i think the evm improvement with the eof those first steps should be taken because they enabled so much more  regarding self-destruct i don't know if i agree with that  and i think there are a few that are pretty trivial to fix that i think maybe we could include this but i'm not sure what else would be prioritized. i think oh yeah one more thing i just wanted to mention so this 3074 i know that there has been some some opposition not only from me but also there's this counter proposal which would not introduce consensus changes by joao weiss and Vitalik. yeah maybe it's not time for that discussion now but at some point i would be curious to hear like the pros and cons of the two approaches but we can yeah probably not time for that today

**Sam Wilson:**
are you talking about 4337 i think like the account abstraction proposal

**Martin Holst Swende:**
yeah yeah yeah

**Sam Wilson:**
i don't think they're mutually exclusive they just solve different problems

**lightclient:**
yeah i think one of the big differences just to put it in for 10 seconds is that 4337 does not help people who already have eoas only people who will deploy new contracts under that paradigm  

**Tim Beiko:**
oh got it i think that i've had this question asked several times sam and matt i think like and i think matthew actually had a twitter thread about this but i think if if either of you could write like a short hackmd document or something just the tldr and post it in the the 3074 discussion link oh actually this another mine already did it well so i guess martin you can you can read the the post that thomas just shared yep thanks  courses aragon get yeah thomas i'm curious you've been you've been sharing a lot of comments do you want to take a minute or two to walk through what you see like from nethermine's perspective it's as being like a priority and and useful

**Tomasz Stanczak:**
so personally i don't really have priorities it's more about the sheer amount of all the different EIPs that we see on the list it seems long least which is good that we're coming to good old times when you get those lists of 20 and so on and we're filtering them down i think it's up to community and others who actually are champions for those EIPs to say like why and yeah personally i have no priorities here like the simple ones would be on my priority lines like if we all agree they are good to go it's relatively simple to introduce and test i think the ones that deal with the code like the object model and so on i would say yeah they go in as for the ones with subroutines i was thinking maybe and i suggested that on the thread that this might be controversial to split the conversations where the merge conversations happen between the f2 and f1 team on all core devs to merge call and then we have dip teams that work on pushing the modifications to evm and and execution layer clients so this thing can work in parallel and don't feel that there is some conflict between the merge effort the merge work and tips work this those meetings would be even more efficient and we would start seeing those teams since we like when you look at the list here it's 40 people and we have like these two separate parts of the meeting so maybe there's a natural suggestion here that this is the way to go

**Tim Beiko:**
yeah i think i've been thinking about that one of the challenges is that at the end it is blocked on the same people implementing it right like so we can and we can have like separate meetings to like discuss the EIPs but like you do want input from the client developers who who will be implementing it and i think it's probably not the end of the world if they happen in parallel just because like we are still like the merge is not done it's not shipped yet we still have time to like slowly get into this stuff before we we we need to be you know solely focused on it and i think it'll maybe naturally happen once the merge stuff is done then we're not going to talk about the merge stuff anymore we'll be like a hundred percent on shanghai and then like when shanghai is pretty done we'll be like half on the the next fork so i don't know yeah i need to think about it more i but i think there is like i i agree there's a lot of like eip champions who like don't care about the merge stuff but i'm not sure that the opposite is true that like the people working on the merge can be excluded from like the EIP discussions yeah yeah thomas

**Tomasz Stanczak:**
maybe if you ask me about like pushing pushing ethereum the most forward with vips then the blob transactions or something similar would be on the highest interest 

**Tim Beiko:**
thanks that's useful

**Micah Zoltu:**
does your statement the same people are working on the merge as the EIPs i agree the same teams are working on them but i have assumed that within the teams they had multiple people and so it's not necessarily the same humans

**Tim Beiko:**
i think it's harder fully parallelized than people generally assume and you do end up like sure some different people might write the code but it gets merged into the same code base people need to review this stuff and so i yeah i don't know. i guess what would really change my mind here if client teams all signal that hey we can actually do like two fully separate tracks and and and that's that's helpful that i i think that would that would change my mind it's just like from client themes that's usually not the feedback i've gotten

**Martin Holst Swende:**
yeah i was just gonna say you're probably not gonna have any client teams saying hey we can we can work in multiple tracks and do anything you throw at us right because

**Danny:**
there's always another multi-track which is like maintenance optimizations and like all the things that aren't new features yeah

**Tim Beiko:**
yeah that that makes sense thomas is your hand still up is there like another comment or did you just forget to oh okay just forgot cool

curious yeah what you all think about you this

**Danno Ferrin:**
an argument what i've heard before the eofs i think are just foundational for solving a lot of problems going forward with a lot of things particularly the things like jump optimization jump table the size scope separation of the data those have very subtle implications that i think will be long term very valuable my biggest concern is upstream adoption of these issues specifically talking about things like the solidity compiler the viper compiler if if they're not generating the features that are doing an eip then it's a one one one point of view would be a little bit wasted time the other point of view is we're not getting an extra category of test tries of what they're actually gonna try in the field and in the wild we can come up with great ideas and reference tests but we really also need to test it with what's going to come down the pipe from the compilers so of all of these things the next question is also how on board is the solidity team in the viper team with these changes salinity has uf implemented great all the pieces all three of the pieces all five of the pieces just a container you know those those are the questions to come up with that and so it looks like positive for the os stuff would be my take

**Tim Beiko:**
cool i guess you know it seems like there is a general agreement that like eo like the simple fills first building blocks of eos which i think are what we basically discussed on the last call are high priority but beyond that like the blob transactions are are potentially really useful but there's a lot of unknowns i think there were some comments in the chats about trying to prototype that at denver and then the other thing i think we probably have a slight bias here is the the beacon chain withdrawals where i think from the like staking community that's basically impossible to ignore so i know would it make sense in terms of next steps i know like the the first couple eofs i think it was let me just check the numbers it's like 3540 3670 3860 to basically move those street to cfi like we discussed on the last call see over the next couple weeks if the if the transaction the blob transactions can be prototyped at denver and and how you know how complex it is and and what that actually looks like and and based on having more information we can we can see you know whether which one of the two proposals might make sense for shanghai and and if not revert back to to 4048 or if there's something we need to fix we'll have still a few months to fix it and then i think also in the next you know not necessarily a couple weeks maybe we also get like a beacon chain withdrawal eip which which we can we can look at yeah i guess summarize like moving the the i think this would be 3540 which is the eof core eip 3670 which is the eof code validation and 3860 which was limit and meter init code moving those to sort of cfi for being the first we would try out on devnets in shanghai and then prototyping the blob transactions and and once we have a beacon chain withdrawal eip we can we can discuss that in more detail
there's any strong objections now's your chance
okay cool so let's let's go with that i'll put together a draft basically spec for for shanghai either today or early next week which has those i do think so we're probably getting pretty late in terms of considering new proposals i think if if people have stuff that's completely new like it was good to share them today and there's probably you know one or two more calls where we can realistically consider new ideas but it does seem like yeah what's trying to to prioritize what's in there and i think once we once we also are a bit farther along with the merge work and and and we're waiting for it to happen on testnets and mainnet we can actually implement these new things on on devnets and see you know how much work they are how much interplay there is between them how complex it is to test them all and i think that will give us a good idea of how much bandwidth we have if if we do like some evm upgrades we add withdrawals and and something around basically transaction data costs yeah beyond that i think we can decide once we've once we've actually implemented stuff and have a better idea
cool. no objections so i'll take that yeah i think that's a good sign

## Executable EL spec overview

**Tim Beiko:**
two more final things before we wrap up one is the quilt team has been working over the past few months on an executable spec for ethereum so yeah it's a really important piece of work it would move us in line with how the consensus error teams do that and solve a lot of the problems we have when writing EIPs where it can get awkward to specify the changes all in line in the eip sam do you want to take a couple minutes to walk us through yeah to walk us through this

**Sam Wilson:**
sure yeah i won't take too much time drive me to share my screen or yeah yeah yeah if you can go for it okay you have 10 minutes and nothing else except an announcement so you can go for it all right so the execution specs are very very similar to the consensus layer specs the only difference is they're written in python first and then compiled into html as opposed to being written in markdown so here's an example of what it looks like from spurious dragon. it's very idiomatic python well it's actually very simple python very understandable should be easy for most people to contribute to we're looking for feedback on how useful this would be for client teams and maybe have a discussion at some point about how we want to change the eip process so this is the raw view of what it looks like so you can see how like validating a block header works so we haven't actually written the annotations yet nice thing about this is the annotations will be in line with the spec but you can turn them off if you're an experienced user so moving on to like what the rendered specification looks like it sphinx we haven't done a lot of work on the theming yet so we can definitely make this look better but yeah it's searchable it's navigatable you could actually get links to different data types and and it's it's useful there and you know the real killer feature that we're trying to work on is like having a diff so this is a diff between tangerine whistle and spurious dragon for the same file so you can see how a function was removed two were added there are still some bugs in this where the navigation doesn't work properly but we're working on it so you can actually see how exactly the code changes between hard forks and one of the goals of the project is to maintain these diffs so that they're incredibly clean and easy for for client devs to to follow along and implement the changes and we want to integrate this into the eip process like i mentioned earlier so that's like we want an eip to be a text document still but any changes to consensus would also be specified as a diff to the python specification so you can actually see like as you're developing a hard fork you can create one of these rendered documents that describes exactly how the hard fork is gonna look like in in code and you know do you guys think that's gonna be useful is this something you'd like to see if you have any feedback now's a great time to think about it

**Martin Holst Swende:**
i i think it looks awesome but i'm curious does it pass all the blockchain test and state tests and it can can you even take this reference code and throw state tests against it

**Sam Wilson:**
yep yeah so we run the legacy tests right now we're working our way through getting all of the testing framework set up but that is a goal is we want to eventually use it for filling tests as well so we want to implement everything we need for that

**Martin Holst Swende:**
awesome

**Danny:**
yeah so we on the consensus layer side like prs for new features don't get merged without tests that would be generated for client teams so i'm i'm pretty pro getting this on the execution layer side so that when things are specified you by default as part of the process have tests integrated

**Sam Wilson:**
i just want to give a shout out to voice peter and guru who have been helping a lot with us just want to make sure that they get mentioned too

**Tim Beiko:**
yeah i think this is like a really really valuable effort on some of the work that's like yeah behind the scenes and i think it would be really nice if we could be in a spot where we do use this to specify the consensus changes of EIPs and similarly if consensus layer teams could start using EIPs to specify the english definitions of their changes so we could have a single system where you know EIPs are just like the written text that that describes the rationale and and overview of a change and then it just links to a pr on whether it's the execution layer specs or the consensus layer specs which which actually has the technical the the technical details and that will add some EIP editing job for micah which he's not about happy about it seems. but i think and and i think the reason i i guess my short argument for EIPs on the consensus layer is they do make it much much easier to communicate these changes to a broader set of people people are like like it's easy to anchor like this change is eip-1234 and people know that rather than like this pr to the spec it's just like an accessibility thing i think and

**Danny:**
i very much agree like it and it's not always just a pr sometimes it's six prs right after some subsequent changes so like mapping that into a a single place to discuss the change set i think is is very very valuable so i was gonna i was gonna say i do not recommend only having an executable spec and trying to map a you know what we do in the eip process for that i i think you need something to accompany it

**Sam Wilson:**
yeah yeah so i think that direction ideally we'd have both so you'd have like just the specification part of the eip where possible would be rewritten as like a python diff yeah

**Danny:**
okay i mean i i definitely agree 

Guillaume:
could you see you can also generate html from the python spec could you also generate other languages or have a plugin structure to be able to so that client teams can implement their own plugin to generate their own language like yeah the aip directly in the in their target language and then be able to tweak it to make it work that would mean some typing

**Sam Wilson:**
yeah i think it's possible i don't know how practical that would be and i don't think that's something like me personally i'm interested in supporting but yes it's absolutely possible for people to do that their regular python programs you can do whatever you can do with python you can do with this

**Dankrad Feist:**
i just wonder if there's a possible future where we have both specs in one repo because then because otherwise there will always be this awkward situation with all the  or any eip that needs to touch both specs that they they can't really like have like one comprehensive diff
so that would be fairly nice i think but i don't know if that's possible maybe we get there it's yeah i

**Danny:**
i also see the argument for keeping it separate so that you know you don't encumber these processes until you're trying to do some sort of release but the cross cross layer testing on those cross their EIPs i see the value there i i would like on the consensus layer you know sam and the the others that have been working on this have done an awesome job making a more sane approach to doing this and code first that builds really nicely and we we do want to migrate to use at least the same format over time the diff functionality is definitely a killer feature

**Tim Beiko:**
and one thing i'll add is i think the echo with danny says like there's value in trying to keep these processes separate just if it means we can be a bit quicker so like i think literally 10 minutes ago we were talking about in the comments splitting EIPs work from merge work and so i think even though it's a bit awkward at like a organizational level we do gain a lot of velocity from having the consensus layer split as much as possible from the execution layer in terms of processes and and yeah so i think if if we couple stuff we want to be really mindful that we don't we don't end up to a spot where like we're now even more bottlenecked than we currently are.

## Merge Community Call #3

**Tim Beiko:**
cool we have less than a minute the last thing is we have a merge community call trent do you want to give a quick shout out for that

Trent:
not much more than what you just said but it's yeah february 11th alternating friday from this call so if anybody would like to show up and interface with the community answer questions we'd be more than happy to host you

**Tim Beiko:**
yeah so it's actually a week from now at the same start time as awkward ev's 1400 utc yeah we'll answer application and infrastructure tooling developers questions about the merge.
Cool anything else before we go?
Okay thanks on everybody this was this was really really good appreciate everybody's participation

-- End of Transcript -- 

## Highlights from the chat
| From | Description                                                              | Link                                                         |
| -----| ------------------------------------------------------------------------ | -------------------------------------------------------------|
| Pari | Kintsugi Incident Report | https://notes.ethereum.org/@ExXcnR0-SJGthjz1dwkA1A/BkkdHWXTY |
| Marek Moraczyński | yesterday I checked a few last getPayloads for every consensus client and I found that 4 out of 5 CL are giving execution engines only milliseconds to prepare the block. I believe it could be a constant pattern for some CLs. Please take a look at the interop discord channel. |-|
| Marius | Geth right now blocks fcu until the payload is created | https://notes.ethereum.org/@ExXcnR0-SJGthjz1dwkA1A/BkkdHWXTY |
| Greg Colvin | That’s a quick summary of the EVM EIPs on the table. | https://github.com/ethereum/pm/issues/450#issuecomment-1014942130 |
| Tomasz Stańczak | as for EIP-2930, there is a way to do that with STARKs now with Oiler Fossil | https://github.com/OilerNetwork/fossil |
| Tomasz Stańczak | Ethereum wallets today and tomorrow — EIP-3074 vs. ERC-4337 | https://medium.com/nethermind-eth/ethereum-wallets-today-and-tomorrow-eip-3074-vs-erc-4337-a7732b81efc8 |
| Lightclient | also gave a presentation at cscon on aa vs. 3074, tldr; AA/4337 - allows people to deploy smart contract wallets and use them natively (e.g. instantiate txs as them, for 4337 a relay network initiates the tx, but to the user it feels native) 3074 - allows users with EOAs to act like a smart wallets without deploying a new contract + migrating assets | https://www.youtube.com/watch?v=KVrhyTk9_zY |

## Attendees (32)
- Mikhail Kalinin
- Tim Beiko
- Lightclient
- Pooja Ranjan
- Marek Moraczynski
- Greg Colvin
- Trenton Van Epps
- Lukasz Rozmej
- Martin Holst Swende
- Somu Bhargava
- Andrew Ashikhmin
- Fabio Di Fabio
- Alex Beregszaszi
- Guillaume
- SasaWebUp
- Pari
- Micah Zoltu
- Sam Wilson
- Alex Stokes
- Vitalik Buterin
- Gary Schulte
- Dankrad Feist
- Rai Sur
- Jose's iPhone
- Tomasz Stanczak
- Daniel Lehrner
- Tom
- Jorge Mederos
- Tanishq
- Protolambda
- Karim T.
- Danny
- Terence(prysmaticlabs)
- Yuga Cohler
- Stokes
- Andrei Maiboroda
- Shana
- Justin Florentine
- Potuz V
- Marius
- James He
- Ansgar Dietrichs

## Next meeting on: February 18, 2022, 14:00 UTC
[Agenda](https://github.com/ethereum/pm/issues/472)