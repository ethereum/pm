# Execution Layer Meeting 185 [2024-04-11]
### Meeting Date/Time: April 11, 2024, 14:00-15:30 UTC
### Meeting Duration: 95 Mins
#### Moderator: Tim Beiko
###  [GitHub Agenda](https://github.com/ethereum/pm/issues/997)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=FWvi_z1_gB0)
### Meeting Notes: Meenakshi Singh
___

## Summary


| S No |  Summary |
| -------- | -------- | 
| **185.1**    | **EIP Update:**  One notable update was lowering the token floor from 16 to 12. This change aims to strike a balance between minimizing impact while achieving a significant reduction in the maximum possible block size1.|
|**185.2**| **Standardized Historical Data Retrieval:**  Developers also discussed a proposal for a standardized way for nodes to structure historical pre-Merge data and retrieve it from an external source2.|
|**185.3**| Developers will include EIP 2935 and EIP 3074 in the first devnet for the Pectra upgrade.|
|**185.4**| Developers will decide later whether to include EOF in the Prague hard fork, and if so, they will focus on testing.|
|**185.5**| Developers will defer a decision on EIP 7623.|

___

## Agenda	
## Pectra Update

**Tim Beiko** [4:03](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=243s): Okay I was just going over what's in the agenda. Sorry about that. But yeah we're going to talk about the scope of the fork today and mostly focus on like what client teams want to see alongside what's already been included. And then the last thing is yeah there's been a couple updates on a few specific EIPs. So we'll make sure to cover those and I think if we can end today in a spot where like 90-95% of the fork scope is set at least on the EL side. I think will be in a good place. I know there were some discussions about like the Blob count in the R&D discord. So it feels like if we can get most of the scope done today you know maybe in a few months we can do a small tweak to the fork at like a simple EIP. But if we don't want to delay things significantly, all of the big large changes should be figured out sooner rather than later. So okay the kick us off there's a couple updates on just the EIPs that are already in the fork. There's been a lot of discussion around MaxEB these past couple weeks. Some of which might affect the EL side. Alex you put together a dock explaining how or what the implications would be and sort of questions around. If we want to add EL consolidations to 7002 to help with MaxEB. You want to give a bit of context on this. 

##  [Adding EL-initiated consolidations to EIP-7002 to support EIP-7251](https://notes.ethereum.org/@ralexstokes/r1gFJt4xC)

**Alex** [5:38](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=338s): Sure yeah. So I don't know if anyone was on the most recent MaxEB breakout call maybe if we give like a short update from that. It would be nice. But yeah I think the other stuff's probably more important to discuss. So let's not linger here too long and maybe if there's time at the end we can Circle back around. But ultimately yeah so there's essentially demand from staking pools to change or at least extend how MaxEB would work with the introduction of another like execution layer operation for this notion of consolidating two validators into one and yeah the doc is just like a quick sketch of what that could look like. I think for us today mainly I just wanted to get it on people Radars and also just you know do like a quick temperature check. Like do we feel like this is something that we can do. It would mainly be changing the pre-deployment. So its not like anything much more beyond 7002 itself. Yeah I don't know if anyone had a chance to look at this or thought about it. 


**Tim Beiko** [6:59](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=419s):  Seems like it. And I guess the reason I wanted to flag this early on is obviously if this changes like the scope of 7002. We need to consider that in like you know the broader Fork context but.


**Alex** [7:17](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=437s):  Right yeah. So I think there's still some questions on MaxEB that we're figuring out the best way to handle. you know there's like we could say hey MaxEB is like big enough already. There's nice to have features but we could put them in like a future fork or something like this. But yeah just something to keep in mind that there might be and with this in particular there's not that much like there's a little bit more the CL has to do but ultimately with the EL yeah it's all kind of contained in the pre deploy. So its actually pretty sure intend.


**Tim Beiko** [7:51](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=471s): There is a comment in the chat about having a more generalised message bus by Vasilliy from Lido. I don't know if you want to take it. Yeah, a couple seconds to like talk to what that could look like.

**Vasilliy** [8:06](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=486s): Yeah it's not ready right now. It's like just in the back of my head for now. Had the idea this night but I think I'll try to bother Alex to review it when it's ready if that's okay. 


**Tim Beiko** [8:26](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=506s): Yeah awesome thanks. Okay so that was the first Petra update. Second Alex you had a 2537 BLS precompiled one as well. 

### EIP-2537: Precompile for BLS12

**Alex** [8:40](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=520s): Sure yeah so this can also be pretty brief. We've done a little bit more work on benchmarking the pre-compiled and figuring out you know if we need to change anything or what that looks like. I think after some various discussions I think the EIP is pretty much going to be as is. There's this notion of like subgroup checks and this one is kind of I mean yeah like the core issue is we could put them into the pre-compiles and things would be harder to misuse by people you know users but they'll be more expensive. So I think Antonio's done some benchmarking work and basically found that we can get them pretty cheaply for some of the pre-compiles except for the  additional ones. So yeah either way just wanted to give a short update there. And yeah I think from there the main thing left would just be finalising the gas schedule but otherwise yeah that one's moving along. 

**Antonio** [9:43](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=583s): Alex I just want to add something I agree with you with what you've been saying about sub group checks. I want actually to raise something that I spot today and it's not about sub group check but it's about the gas of the pairings and it's something that Dankrad has been mentioning a while ago. So basically if you see the point evaluation precompile gas on the 4844 it is 50,000 of gas. And so and it will be basically that is two pairings. And Dankrad was saying that would be nice to have the gas of the 2537 pairings compatible with that Gas. But in our case instead with the current gas two pairings corresponds to 151,000 gas. So it's kind of bit awkward to have the same operations. I mean two pairings in one side paying 50,000 and in this case 151,000. So I just spotted today because I've been writing the Test vectors. 


**Alex** [10:51](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=651s): Yeah, I hear that I mean we could kind of claim that we're subsidizing the 4844 stuff with the lower gas cost but yeah definitely something to look at.


**Antonio** [11:05](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=665s): I will raise offline as well in the Github. There's no sense to waste time here for this but just want to like to mention this. 


**Alex** [11:12](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=672s): Yeah thanks.

## [Pectra-devnet-0 Updates](https://notes.ethereum.org/@ethpandaops/pectra-devnet-0)

**Tim Beiko** [11:18](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=678s): Okay thanks and then the last thing I wanted to cover quickly was the devet-0. So as I understand it no team has implemented like all of the EIPs that were included already on the I think on both sides there's still a fair amount of change in the specs but is that a correct assessment? Are there any updates beyond that. Yeah, are there any updates beyond just people are working on it or any questions or blockers that people have? Okay I guess anything else people want to discuss on the EIPs that are already included in the fork. If not, I think the best way to do this with regards to what else do we include is to zoom in on the few EIPs which seem to have broad support although not unanimous at least the start. 

### Client team preferences

**Tim Beiko** [12:32](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=752s): So every single team on the EL side sent in a sort of list of preference and stuff that they like really want to see in the fork stuff that they're sort of neutral towards and stuff that they're against. Skimming through all of this before the call. It seems like there's three that sort of stand out where most of the teams support them but there's still like some you know teams either objecting or you know ambivalent towards it. So those three are like 3074, EOF and 2935. I think it probably makes sense to start with just 3074 because this is the most complex of them. And I think if we went forward with this would affect sort of you know the bandwidth and room for everything else. So on that front it seems like Erigon, Besu,  Nethermind and Reth were in favour of including it. And then Geth was the one opposed. So I guess maybe let's start with like let's start with Geth if someone wants to make the case like why they don't think it should be in and then we can sort of take it from there. And reading your doc Geth it seems to be about it being too big but also the interaction with Verkles. I don't know if anyone? 

**Guillaume** [14:11](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=851s): Oh yeah I can address this. I thought we were talking about another one. Sorry. Yeah so there's been this conversation happening a couple months back and I raised some concerns that yeah it might paint ourselves into a corner for a Verkle later down the road. I didn't see any progress on this front. The EOF spec is not when yes it's supposedly complete. But there hasn't been any implementation to speak of there hasn't been a testnet. There hasn't been any noticeable progress at least if there was the case it hasn't been brought to my attention. And we feel that this is a big change. The initial design or the initial intent behind the prague was to make a small feature Fork ahead of Verkle that really goes against this objective and as a result we oppose it. 

**Tim Beiko** [15:19](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=919s ): Got it. I guess in terms of the progress and the implementations. Does anyone on the EOF front want to talk about that?

**Danno Ferrin** [15:27](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=927s ): Sure I can talk about it. As far as implementation Besu has a complete implementation. It's on a branch right now. Mega EOF if you were on the calls we talk about it frequently.  Reth's implementation is almost complete. There's also a status checklist we've been attaching with all of our updates for EOF as far as which clients have been working on it. As far as the Verkle compatibility one thing is that the current formulation of how we're going to store the story for EOF v0 is a bit of an overfit on the Legacy dealing with the whole jump test analysis leaking into there. We can continue to use that for EOF if we need to. There are better ways to store it but if we were to use the existing way that the storage was going to be stored in it's 100% compatible. It's just data. All of our overhangs would be zero. There's no jump test analysis. So as far as fitting EOF into Verkle with that concern. It's not terribly difficult. I mean there's better ways to do it but the way that exists right now can be done just fine and I know there's been discussions with Asic been talking about possible ways to do an EOF V0 where you could encode the jump testing encoding into it as a wrapper. But you know my understanding is that you know it was given us ideas to the verkle team to see if they want to pursue it and there are other issues that were being pursued at the time. So the concern was implementations and Verkle integration was another one that EVM listed. 

**Guillaume** [17:01](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1021s): Yeah I mean when okay it's not exactly another one it's Verkle integration. When I said I wanted to see Verkle integration I wanted EOF implemented on Verkle testnet. That's  what I clearly asked for back in the day. So yeah integration is not happening. It hasn't happened.


**Danno Ferrin** [17:23](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1043s ): That totally feels like gold post moving to be honest but I'll let Tim talk.


**Tim Beiko** [17:27](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1047s): Yeah I guess what I was gonna say is like you know we don't like we don't speculatively Implement EIPs on like the next fork. And I understand that like Verkle is a bit different here. But it feels like the best way to actually get there is we would have EOF as part of Pectra then all the Petra builds would have EOF and then verkle Builds on top of Pectra and by default it gets EOF. So like yeah I don't know like otherwise if you know we're sort of asking all the client teams to like speculatively Implement EOF on the devnet for two forks from now which seems like unlikely anyone would prioritize in terms of resources. Is there like a specific thing you're concerned about with regards to Verkle? Guillaume?  Where like why?


**Guillaume** [18:21](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1101s): Yeah I mean like like I said so first of all no there was no go post moving. It was actually said on the during the last ACD we talked about and second what I'm concerned of is that the the argument that was already raised back then is that we paint ourselves into a corner we Implement some hand wavy version of of EOF and we found ourselves blocked. We realized there's a problem and Verkle can no longer happen. I just want to have this cleared out, that's all I'm asking.

**Tim Beiko** [18:56](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1136s ): I guess what would be the thing out of from EOF that affects basically how the Verkle tree is constructed or migrated that you think is there like a specific area basically that you think or a specific. I don't know part of like the EOF proposal that you think like oh you know if we do this thing then that actually overlaps with how the Verkle. l migration happens or like the way State access works I mean.


**Guillaume** [19:36](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1176s): To be to be fully convinced I need to be able to have an EOF testnet that converts to Verkle and we find out there's no problem but even having a proposal of Verkle enabled like even a spec would be enough I haven't even seen this all I had was and wav thinks that this should not be a problem. But I don't even know how to implement this if I have no spec to work with.  So yeah even having this I cannot agree.

**Tim Beiko** [20:07](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1207s ): Yeah on that front so there is the Mega spec for EOF but Danno do you maybe want to like dive a bit more into that like what the current spec includes what like EIP is map to it because I know that has changed a lot yeah in the past like six months or so so I just want to make it.

**Danno** [20:33](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1233s): Sure like yeah we're so it started out as kind of a modular EOF because there was a lot of features we could add or remove out of EOF and the ipsilon team is trying to figure out what the scope they needed so they took all the parts that could be severed and they made separate EIPs out of them. so that I agree that contributes to some of the early confusion about what EOF is what features are in and what features are out. Once's it an out it's been fairly well settled the implementation metrics that I've been passing out has all of the EIPs that are in. There is a mega spec let me find. Once I stop talking I'll find the link for that on the ipsilon website. That lists it in one concise unified document but historically because it was pieced out in separate EIPs we have that there we go that's not the current one there's one on on GitHub which we've been referring to in all our past meetings I'll find that one. But yes that one and we've been using EOF you know there's a unified spec and then we've been splitting it out to the EIP to respect the historical separation of it. So there is a spec and it's been implemented we were writing reference tests they just merged a bunch of reference tests for the container format into EIP into the ethereum test Network the test repo just the other day for some of the the things we the stage we're at is we writing reference tests for this. Bases reference test apart from Bugs we find during testing has implemented all the EIPs. Reth is mostly there. I know nethermind and Geth for Mega EOF not for Mega for big EOF which was back in Shanghai. They had complete implementations and there's just you know a handful of things that need to be changed to support. Code introspection blocking code introspection and blocking gas introspection. So the major work of building the container is is done for most of these clients. But I agree
it's kind of a moving thing because we took advantage of being pulled out of Shanghai to put features that were requested for in to make sure that the one breaking change for ethereum virtual machine is done with all the things that we need now. So that was bringing in code introspection rejection gas introspection rejection and making sure that you know we had all the analysis we need for the things that we needed. And so that's why it seems like it's been moving around because we took the time that we were given by being kicked out of Shanghai and then not considered it for  Cancun to make sure that we had all those features in. But what we have now is what we intend to ship for Prague. 


**TIm Beiko** [23:02](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1382s):Got it.


**Maurius** [23:03](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1383s): One thing that like how many new opcodes would this add or like how many new versions of opcodes are
being touched by this by the Mega new versions of opcodes.


**Danno** [23:22](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1402s): I had a chart. So if you're judging it by opcode number it does sound larger than it is but all the implementation is reusing existing stuff. So there's the three ones for the call that we're changing. We're adding 6603 Swap and dupen. We're replacing the jump opcodes. So there's another three there and adding a vector jump opcode which is something that's been requested by a lot of people. So that there is we're only touching the things we have to touch because of the container format and these are features that have been requested since 2018 at least. I think is that current list the Tim just back yeah. So it's 18 I think.

**Maurius** [24:09](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1449s ): Yes. So my concern is that for everytime we touch an opcode there's a risk right. And I don't know we're talking about I don't know the  to store repricing that is one single opcode that has like a whole debate around it or we we did the analysis for the pay opcode and we found out that it can be like called in like 25 different contexts. And they each interact with each other and just making a full table of in which context can this one opcode be called is already kind of extreme work. And so I just don't see that our like spending our time there is more beneficial than spending our time on other features. And this is not only like the time to implement it but especially the time to to test it to make to  benchmark it to make sure nothing breaks. Yeah that this is kind of my view. I don't know anything about don't know much about worker. So I cannot speak on Yoav’s concerns about worker but those were my concerns when saying we wouldn't like to get EOF in. 

**Danno** [25:56](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1556s): Okay. So it's too large as the complaint and that in some sense that's a bit frustrating to me. Because we came up with a smaller patch back in Shanghai and then other people requested it to be larger and we just can't get a consistent request on what people want out of EOF from the All Core Devs Group. So that's it's kind of frustrating to hear that from both sides and they're both valid complaints. But you know the other option is to unify as it is now. And I don't think that's a good place for ethereum. I think it's going to drain most of what we have for the EVM and the greater EVM ecosystem. if we freeze it where it is now. 


**Tim Beiko** [26:32](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1592s): I guess on the testing front like is this something that we have like significant test vectors for already like for example you know if we are changing the behaviour of like 18 opcodes. Do we have reference tests for all of them part of them, none of them at this point, what's the status there?

**Danno** [26:51](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1611s ): So that's where I'm working at right now writing the reference tests for these and helping ipsilon write the reference tests. And get some of these features out. We just pushed a bunch of tests for the newest test surface would be the container format. And back in Shanghai there was a fuzzing setup done. So we could test the container format from a fuzzer and found a lot of stuff. As far as fuzzing the opcodes the same fuzzing Frameworks that work there can be easily adapted. I think the best work we're going to get in addition to writing deliberate reference test the test the spec is written is the fuzzing and that's where we're going to find all of it those. You know the fuzzing stuff is an understood problem just needs to be adapted for the structure of the EOF. And you know a couple more things written to make sure it works well with the EOF. 

**Tim Beiko** [27:39](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1659s ): Got it. I guess one thing I'd be curious to hear as well is so it seems like Reth and Nethermind alongside with basu both have pretty Advanced implementations like do either of you want to talk about like what you see as the current state and like the current like potential risks or open issues. Yeah Merek?

**Marek** [28:03](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1683s): Yeah. So we are not against EOF and it definitely adds value but the previous commitment from fin teams was to do small fork and do Verkle Tree as soon as possible. If we add EOF here then we can think about Pectra as medium or large Fork and our implementation is up to the latest spec but EOF brings a significant risk of consensus issues which will require lots of testing. And it cannot be rushed. So on the other hand we know that if we do not ship EOF now. We will wait two three years of see EOF  on Mainnet. So that is why we see two options here. We can Implement a medium large Pectra with EOF and sacrifice testing capacity for Verkle and maybe EIP 4844 continue with Verkles in parallel and immediately after pectra focus on 4844s and even more focus on Verkle trees or just do as we planned before. So small pectra Fork on Verkle in parallel, delay EOF and release it after Verkle hard fork. I think both options are good but yeah that is how we see that.

**Tim Beiko** [29:45](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1785s): Got it and yeah I don't know if anyone from Reth or Erigon has thoughts you want to share?


**Gakonst** [29:55](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1795s): I'm not sure if dragon is on the call? This is Georgio from Reth. We already have a work in progress EOF implementation and we are generally supportive of it. We hope to have something done and merged in the coming weeks.

**Tim Beiko** [30:11](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1811s): Okay and yeah anyone on the Erigon team. 

**Somnath (Erigon)** [30:20](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1820s ): So for Erigon we have parallel works going on for both Verkle and EOF. So we favour EOF for Pectra because Verkle seems to be pushed. And I know why you know the scope is increasing but I think we can pull through. That's about the comment from Erigon. 

**Tim Beiko** [30:55](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1855s ): Got it and then yeah in the in the chat there's a comment about the cross client testing being the bigger lift than the actual implementation. So like it seems you know from this that like most client teams can get, yeah can get an implementation fairly easily. But then testing things will be a lot of work. I feel like instead of making a decision on EOF right now. It's probably worth covering some of the other EIPs that people were on the defence about and see like getting more context around those. And then coming back to seeing like do we want to include any of them or EOF because EOF being so big. I think means like you know if we go forward with it there's probably a lot of stuff we have to push out. so I want to make sure we understand what we'd be pushing out or trading it off against. So any I guess any other just like comments thoughts on like the Readiness or concerns around EOF. Okay yeah thanks everyone for sharing your thoughts on this. 

### EIP-3074: AUTH and AUTHCALL opcodes

**Tim Beiko** [32:20](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1940s ): The next one that pretty much every team seemed to be in favour of was 3074. The one caveat, so Reth's preference post was a bit old. It was from like January so their stance was like we want one of the account abstraction EIPs. But not really you know specified which one. In January we were still going through a bunch of different ones and debating them. It seems like 3074 is the one that all the other teams would prefer to see today. So I guess maybe to start there like on the Reth’s side like assuming the other Clients teams like 3074 and would want to move that one forward. Is that one that you're still comfortable with? And would be happy to to see as part of the fork. 


**Gakonst** [33:12](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=1992s): Reth is supportive of 3074 and only 3074 for the next hard fork. And we already have it implemented and tested. 


**Tim Beiko** [33:24](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2004s ): Okay. So I guess yeah do any of the client teams feel like we should not do 3074 in the next hard Fork? I know in the chat a bit earlier there were some concerns around some of the security risks and then a bunch back and forth there I couldn't read but we've talked about the security risks of 3074 for a few years now. Do people feel like we're happy to move forward with it even if you know being aware of all of those? Does anyone have any more objection or things you know that they feel uncomfortable with?


**Danno** [34:06](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2046s ): My objection was always safety oriented and to move to require the current notes to allow it to require the current notes allows for single action revocation which is what my big ask was and that's been delivered
so my past concerns on it have been resolved by that action.


**Tim Beiko** [34:28](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2068s ):  Proto?


**Protolambda** [34:31](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2071s): Hello I'm in favour of the EIP but I am concerned about the The Edge case of not being able to enforce as a contract that some data aesthetically declared in a transaction like the top level call detection the lose with this EIP. I drafted a EOF for a replacement but there might be other options too. Having some sort of you know fallback for this feature would be really useful.


**Tim Beiko** [35:08](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2108s): Marius?


**Marius** [35:10](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2110s): So why I'm General in favour of 3074. One thing that I would like to remind everyone of is that it's something that came up during our work on the inclusion list. And I'm not sure if all the client teams are aware of it. But with 3074 the design of the miner is kind of more complicated. It makes block building more complicated because you can have transactions that invalidate other transactions. And you don't have that right now well you kind of have that right now but only with transactions that are from the same sender with low nounces. And with 3074 basically transactions can in validate arbitrary many transactions and the transaction code. It can be mitigated by the transaction pool it's just something that we need to think about when when when designing our trans section pools to make them 3074
Ready. 


**Tim Beiko** [36:35](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2195s): Got it and then there's a comment by Yoav about the blob invalidation. I know there's been like a lot of back and forth on this. Yeah Yoav, do you maybe want to just give a quick overview and then yeah we can take it from there.


**Yoav** [36:57](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2217s): Yeah the concern we discussed and I think we we discussed it on Discord already is around the invalid around the denial of service against the Mem pool by sending a lot of blobs and then invalidating a large number of blobs from a single transaction using a value transfer in 3074 AUTH and AUTH call. So we have a rule we have a rule to protect against that using requiring a 2X fee increase for blob for replacing a blob but here we can bypass it for a large number of transactions. Now as Matt suggested it's already possible to invalidate to invalidate them by sending a private transaction to a builder that replaces the current blob but this only affects the blob from the blobs from one EOA. And it's also more expensive because you need to pay the block Builder whereas propagating a lot of mempool transactions that each of them invalidate many blobs is a much cheaper attack.


**Tim Beiko** [38:12](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2292s ): Marius,  did you want to respond to this?


**Marius** [38:15](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2295s): Yes I want to respond to this yes that does have implications but at least and like we created a Benchmark for it or I created a benchmark for it in the gas case. And I think it takes around a less than a second to if I create a block full of 3074 transactions that invalidate the maximum number of block transactions. The thing is in gas we in our block pool implementation we don't delete the block transaction we just tomb storm them. And so sending these kind of attack transactions does not make us do a lot of work. It just means we have bunch of junk on the disc that is not cleaned up that is overwritten the next time we write correct block transactions. It does one thing that might be concerning is if we do reorgs or like how this interacts with reorgs. I haven't tested that where we kind of have to resurrect all of those transactions.

**Yoav** [39:47](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2387s): And did you also did the test also cover the peer-to-peer the communication layer like the load on communication layer of propagating a large number of blobes that end up unpaid?


**Marius** [40:02](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2402s): No but like you can kind of send them right now we have to prevent spam on the on the networking layer anyway. And the way we do it is just check if we have like if a transaction is a blob transaction and if we have the band with to download block transaction and then we fish them. So this like this case is not worse than just someone announcing 10 Gigabytes of block transactions to us. I think.

**Yoav** [40:47](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2447s ): All right thanks for explaining. 


**Tim Beiko** [40:54](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2454s): Okay I guess yeah given this yeah I'd say 3074 was probably the EIP that had like I think it was the only EIP that had basically unanimous support from all of the client teams to be included. So does anyone object to including it. I think this is one we can probably make the call on right now if we're happy with it. So any objections to including 3074 in Pectra otherwise I think we should move forward.

**Cyrus** [41:33](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2493s): I was hoping to hear what 3074 plans to do with origin if they could clarify that. 

**Tim Beiko** [41:41](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2501s): Yeah I guess if someone has a quick response but if this is okay it's in the EIP. So I think yeah let's have this offline. I think everyone has like reviewed the EIP and all the client teams spend time on it. So if there's no objection yeah let's move with 3074 in Pectra. So that's one down.  The next okay so yeah 3074 is in. Any final thoughts, comments. I think we're good on this one.


### EIP -2935: Serve historical block hashes from state

**Tim Beiko** [42:24](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2544s): Okay and the last one I want to make sure that we cover that a lot of teams brought up is 2935. So this is about serving the block hash in the state. Basically I think like Geth, Nethermind Besu were in favour. Erigon was like ambivalent about it. And I don't think we discussed it when like Reth put it right up together. So yeah I guess I'd be curious to hear about either oh and sorry Etherrum JS also in favour. I'd be curious to hear yeah either Aragon, Reth any strong views on this one, 2935 which is about adding the block hash as part of a contract in the state. And this was especially useful in a Verkle context now where it can allow us to keep the block hash opcode or to yeah to keep the block hash opcode behaviour. 

**Gakonst** [43:34](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2614s): Yep Reth neutral positive same simple change it's very similar to how the Beacon change is all the beacon route thing is also implemented if people wanted were down. 

**Tim Beiko** [43:48](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2628s):Yeah Erigon? 

**Somnath** [43:50](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2630s): For similar views it's small if the bigger ones are not included we can give this one a go you know that's are we. It's  not going to make a huge difference.


**Tim Beiko** [44:08](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2648s): Okay but so say we did like EOF for example you think that would like maybe be too much so you'd rather like there's like a trade-off between like doing the small one and then potentially having like a bigger one included is that what you're saying? 


**Somnath** [44:23](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2663s ): Yes so if you potentially are thinking about EOF. I think most other EIPs can sort of jump out of discussion for the next hot fork maybe. And given the fact that you know we're not in a rush to do Verkle anyway. So later on we may or may not make small changes to the EIP. And Associated things like testing and stuff so it's going to evolve again in our opinion. For the next hard fork when you know the verkle is actually implemented. 


**Tim Beiko** [45:00](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2700s): Got it. Okay.



**Guillaume** [45:02](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2702s): I have to descend with that it's currently being used on the Verkle testnet. The EIP as it is specified will not evolve there's no event that let us anticipate that this will ever change. It is currently being used on the Verkle testnet. 


**Tim Beiko** [45:21](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2721s): Okay nice. I guess yeah if we feel like this we might want to like that you know we might not want to do if we do other larger things. I think I'm happy to go through the other couple EIPs that we wanted to discuss and we can end up. We can come back to it and make a decision a bit later. Any objections there? Okay so these were okay so these were like the three big ones that basically all the client teams had like preference towards. I think there's a couple more that people posted updates on that it is worth probably covering real quickly. Let's start actually, yeah so Vitalik had won 7667 which proposes to change a bunch of gas cost to make them more SNARK friendly. I don't know if Vitalik is on the call but I think that the EIP itself is pretty straightforward. So any thoughts from client teams about this one? Okay if there's no oh sorry Danno yeah please I didn't see it. 


**Danno** [46:52](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2812s): So on some of these ethmagician threads it seemed like this also be pushed out to one of things he pitched was having a lot of gas changes with the verkle fork in Osaka. Since we're dramatically blowing up the gas schedule with the way that we're accounting fork trees and storage it seems like a good place for it since we're going to dramatically blow up the way we charge for hashes. So I mean I think that's one that we could list as you know good we just need to schedule it and get the exact values for it down. I kind of agree with it.

**Tim Beiko** [47:31](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2851s): Any other if it has a place I don't know if it has a place in Prague though. Any other client teams or people have thoughts on this. One oh the Dietricks might pop in but yeah I also oh actually yeah Carl yeah?


**Carl** [48:05](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2885s): I think it's a good idea from the perspective of SNARK ifying stuff but it is very extreme. I think we need to like do a lot of Investigation onto the impacts of this hashing is one of the most core features that pretty much every smart contract uses at some point. And so I think we need to be very careful about doing the analysis on exactly what's like who's affected and how much? It's something we've had from the very beginning and I think as a one of those assumptions that's very much baked into the  many contracts. 


**Tim Beiko** [48:48](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2928s ): Yeah Marius?


**Marius** [48:50](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2930s ): Yes I kind of feel the same way. And I think like I don't think we should price stuff for a potential future but for the costs to the nodes right now and the cost to nodes right now the pre- compiles are kind of or the operations are kind of priced correctly. So I think if  we were to reprise it should be at a point where we either see a bunch of ZK EVMs or we even think about ZK EVM ifying mainnet itself. So yes that's kind of that would be my point.

**Tim Beiko** [49:42](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2982s): Got it Danno know did you want to respond to that? 


**Danno** [49:46](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=2986s ): I just wanted to say that the hashers are like the most impossible things to optimize because almost all the clients are already using well optimized implementations. So speeds never going to go up on these. Maybe to get the EVM to access the hash but if we need to increase the GPS then a change in the gas costs would be valuable but I generally agree that Prague's probably not the right place to do this.

**Tim Beiko** [50:14](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3014s): Yeah I guess on I had a suggestion in the chat where like we are going to reprice at all the things with Verkle already in Osaka. I think in terms of just like user experience if we can if these changes are not urgent which it doesn't seem like they are because they're mostly to help you know lt's working on ZK EVMs. And whatnot it feels better to bundle all of the large gas cost changes in like a single Fork. Not to say we can never change gas costs again but for people to know that like this is when they should pay attention and that there will be significant changes like across the Board rather than trying to like make tweaks in like one set of prices in this fork and then the whole other set of prices in the next fork. Carl?

**Carl** [51:11](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3071s): Yeah one quick addition on the L2 side of things. Like I don't think we should be making L1 decisions based on fork for the EVM based on pricing that L2s I think can figure out a way of sorting out themselves or we can coordinate way of sorting out for themselves. This should be based on the needs of L1 for now.


**Tim Beiko** [51:31](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3091s): Got it. Okay so yeah. I think we can move on from this one wait oh please yeah sorry.

**Vitalik** [51:43](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3103s): I just turn at the right time. Yeah I mean I think so one important thing to keep in mind here right is that I think people are like it's very easy to underestimate the extents to which L1 itself is actually not that far away from being ZK SNARKS right. Because like right the L1 the cost of staring 30 million gas like for average case stuff has already gone down from I think like something like five hours a year ago to like 20 minutes now and then it just keeps on decreasing very quickly. And so I think it's very possible to or believe that know even  within one or two years we'll have the capability of proving the ethereum L1 in real time right. So I think it's just important to mentally adapt to the fact that like there's no such thing as a distinction between ZK chains and non-ZK chains like we are basically now entering a mode where every serious chain is a ZK chain. And so like ZK friendliness is not something that is unique to L2s, it's something that is going to be with L1s as well. Especially given the underlying goal of trying to increase the ease of verification with things like the Verge and trying to support more properly verifying for light clients and so forth right. So I think this is something that is super L1 relevant and I think the again the goal is to try to like basically we really need to worry about the worst case rather than worrying about the average case because especially for L1 applications of this actually in a way. It's more important for L1 than for L2 right. Because for an L2 if you have like one or two long blocks then you can just a lot of applications that really depend on having a like a very fixed upper bound like a theoretical maximum number of milliseconds. That it takes to create a stark proof of an1 block right so like for example if like when we get it let's say between two and three seconds. Then you know that gets us to the point where validators and block Builders will be able to take advantage of it. So that's how I see the value of that I see that there's some discussions in the chat on like receipts and Merkle Patricia trees and which definitely also has touches on this topic quite a bit. I think so aside from hash opcodes the other two places where a block did have a huge amount of hashing in it. I think as I wrote in the EIP spec is number one is the Merkle Patricia’s Tree which we're thankfully getting rid of with Verkle trees and number two is receipts. And with receipts there's also this one very particular annoying challenge that there's like these huge individual hashes that could come come up if there's if there is a receipt who's log data is is really huge and I mean of course moving over to SSZ hashing the receipt structure is going to reduce improve things a lot there but fortunately I did the I did the math and like glog data is already kind of almost at the point of being high enough that it's not the not the primary issue in terms of like bounding ZK proving cost of a block in terms of validating ZK improving cost of a block it does feel like the worst case is just like blocks Stake to the  a huge amount of hashing in them.

**TIm Beiko** [55:53](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3353s): Yeah thanks for thanks for sharing all that context. I guess this and then based on a comment in the chat around like should this be like a good RIP as well. If this is something that's important on you know not maybe the next year timeline but like the next few years as the speed of verifying goes down. One path forward is we could try to get this implemented on L2s first as a signal that you know they actually like endorse those gas prices and you know they might argue about them and tweak them and whatnot. And then tentatively commit to doing this in the next Fork alongside with all the other Verkle repricing. So this means that in say you know the next year we can try to run like with a version of this on some of the L2s. Get them actually like using you know those values and production and then that'll help us like refine the actual numbers. And alongside with the verkle gas cost changes. We can include either those as is or you know whatever tweaked version of those in the next Fork. Did people think something like that be reasonable? 

**Vitalik** [57:16](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3436s): Yeah I mean one thing I want to just like also clarify is that like I think it's totally fine if this happens let's say like to in. The second next fork in instead of being in the next Fork because like there's no point in just solving the EVM hashing issues if we the worst case is like 300 megabytes of hashing in the Merkle Patircia tree anyway. So I think realistically the biggest kind of short-term task that I would love to see.  People doing over the next month is actually just like a much more dedicated benchmarking effort figure out two claim two things. So the first thing is basically like what what is the effect on existing applications of raising the cost of both KECCAK and other opcodes by a particular amount and the second is basically figuring out like on existing ZK EVMs. What is the extent to which this is a bottleneck like basically what is the fact of factor n by which we can make hashes more expensive at which point something else actually becomes a bottleneck right and like those two variables are going to be key in determining like what actually is going to like like like both what parameters make sense for this. And if the results end up being unfavourable also what kind of approach makes the most sense. 

**im Beiko** [59:01](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3541s): And I know one thing that's come up over and over in these discussions is like L2s want to signal from L1 that they're actually serious about it because otherwise they don't want to spend the time and and whatnot. So I guess my suggestion with this one would for this one would be can we just CFI it for the next Fork alongside all the other Verkle stuff. So that you know L2s know that like we plan to do this but also that it should sort of be on them to like push this forward before the verkle Forks that like we're kind of happy with yeah with the numbers and what not. But yeah do you think that would help just send a signal to the Verkle Forks. 

**Vitalik** [59:49](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3589s): Yeah so I think that the ecosystem needs is just like a signal of like seriousness that know things are moving in the direction of ZK SNARKS being like a a first class thing that everything get is is getting designed around. And the resource costs are going to be adjusted accordingly. And both for Layer 2s and I think ultimately also for L1 focused ZK EVM designers and I mean the other third target of course is like solidity and app developers to get the ball rolling on kind of reoptimizing applications around some of these adjusted costs.

**Tim Beiko** [1:00:36](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3636s): Right so yeah I guess does any client team oppose making this EIP 7667 CFI for like Osaka. And obviously if we get to that Implement in Osaka and we see some issues or the ZK approving time has not gone down or what ever we can always kick it back and another fork. But I think this sends a good signal and then allows hopefully some of the L2 teams to like make progress on this in the next months to finalize the numbers and do the analysis also against L1.  Any objection to that? Okay cool. So yeah let's see if this one is for Osaka alongside the other Verkle EIPs.


### [EIP-7623 updates](https://github.com/ethereum/pm/issues/997#issuecomment-2033643534)

**Tim Beiko** [1:01:26](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3686s ): Moving on the other one which had an update was 7623. The biggest question there was a lot of the numbers originally were done pre dencun. And so we didn't really see the effective blobs on those numbers and then Toni Re-ran, the analysis. I don't know if Toni's on? If you want to give a quick update?

**Toni** [1:01:50](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3710s): Oh yes you're here. Yes I can do that. Yeah so the result is basically that the EL payload size we got it under 100 kilobytes. So the EL payload size was previously before for it 4844 it was around 120 kilobytes and now the average is around 90 or between 80 and 90 kilobytes. So kind of the gap between the maximum possible EL payload size and the average became bigger. And yeah I just wanted to start the discussion on 7623. I already sorted some client team's favorite some didn't had an opinion on it yet. And yeah especially thinking of increasing the gas limit or increasing the blob count. I would say that the EIP is a quite good fit to go in parallel. 

**Tim Beiko** [1:02:47](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3767s): And Ben?

**Ben Admas** [1:02:49](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3769s): Hi yeah I think
there's a hidden problem if gas limit does increases which isn't under Dev control. And then because degenerate blocks can be created full of zeros. It would be good to address it just to diffuse that as a potential problem. 

**Vitalik** [1:03:22](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3802s): So my understanding is that like basically all of our infrastructure or peer tp peer is like wrapped in Snappy compression or some equivalent already is that the case or like not the case?

**Marius** [1:03:39](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3819s ):  The one of the issues is Jason. So if you get Jason the block data is Jason then it doubles up in size and it goes to like 13 megabytes for the large blocks. 

**Vitalik** [1:03:54](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3834s):  Right but this is independent of like the zero bite issue right that like if you get JSON that's just like a dumb factor of two increase on anything.

**Ben Adams** [1:04:05](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3845s ): Yeah and you have that between the CL and the EL. So it's like unnecessary strain from if somebody wanted to create a degenerately large block.

**Vitalik** [1:04:17](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3857s ): Right but right but I guess just to clarify like that feel like an issue that's dependent of like of how details of 7623 work because it's like a 2X penalty that we suffer regardless of what happens. 

**Ben Adams** [1:04:35](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3875s): Yeah but the 7623 would prevent that from being a problem because it removes the excessive large Blocks.

**Vitalik** [1:04:47](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3887s):  I see like like you're basically saying that like there's yet another domain where capping the worst case is a really valuable thing to do.


**Ben Adams** [1:04:57](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3897s): Yeah completely. 


**Vitalik** [1:05:00](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3900s ): Makes sense. Yeah by the way I just in the in the chat Mario Vega says that there's a concern with 7623. It adds a condition to make it a transaction invalid after it has been executed and just to clarify that the EIP does not work that way right. So there is no way that with EIP 7623 transaction can get retroactively made invalid after execution like basically all that 7623 does is that it changes the refund or the rules around like refunds and how available gas is calculated based on call data. 

**Tim Beiko** [1:06:00](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3960s): You're breaking up a bit Vitalik but I think we got the gist of the last comment but like yeah we changed the pricing and so you still have to pay for the worst case pricing and you get a refund.


**Vitalik** [1:06:14](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3974s ): Right the gist of my comage is basically that there's like there isn't some possibility of like retroactive invalidation that 7623 introduces because that's just not how it works. 



**Tim Beiko** [1:06:25](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3985s): Got it. Any other questions comments on it? 

**Carl** [1:06:35](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=3995s): Quick one this came up on roll call yesterday and while not every L2 was represented or had someone present it seemed like no one had any major issues with this EIP on that side.

**Tim Beiko** [1:06:48](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=4008s ): Nice. Thanks for thanks for sharing that. Okay I think it's probably worth just covering real quick a couple more updates and then trying to keep at least 15 minutes to like make some final decisions. There was a comment around changing origin Behavior I know we discussed this in a past call and it didn't seem like there was too much support. But I guess do any of the client teams feel quite strongly about
This? Okay if not?

**Danno** [1:07:31](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=4051s): So sorry. One thing that I had asked for they had come on to the EOF call is statement from Security Professionals. People actually using this what they think about it I think as client teams it's mostly an implementation detail and we don't necessarily see the higher level implications of why it's important to ban it or why it's important to keep it. So I think what we need to hear from is security researchers to say if the origin is bad, should it be banned, should it be change or not. I think that's the level of input we need to make an intelligent decision on this. 

**Cyrus** [1:08:01](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=4081s): Well I do want to make the distinction really quickly. That we're talking about two different things there's the aliasing solution which is 7645 Alias is origin to sender I just posted them in the chat. The second one is Banning origin and EOF of which is not really a full ban because Legacy deployments are still going to be available. But it would start us on the path of getting rid of it Banning it you know Eventually. And then the third option is to do nothing and let each account abstraction solution as 3074 has deal with origin in its own way.

**Tim Beiko** [1:08:38](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=4118s): I guess let me just pause you here because we have a lot of stuff on the agenda. So I think unless client teams have a strong opinion on either of these I think yeah we could probably just move forward and continue this conversation offline. So yeah any okay yeah there's a big comment in the chat but it's not about this yeah any comments from the client teams on Origin? If not okay there's two more changes these aren't super related to the EL but I do want to flag them because we have been talking about them in the past bunch of calls. First, the inclusion list came up a bunch in the chat today. So none or at least definitely not a majority of the EL teams you know showed strong support for inclusion list a couple of the documents sent before shared that like people think it's a lot of complexity and there's still some open questions in the spec. So I guess yeah does anyone feel very strongly on the EL side that like we should do this otherwise it seems like the default path at this point is at least from the EL side like not including this in Pectra. Yeah, does anyone want to make a strong case on the other side? Okay so I think yeah unless on the CL side next week we see like a really strong support for it. Then I think we can consider it excluded from this Fork. But I think that yeah this is mostly a CL conversation and obviously has some EL implications but yeah from the EL side doesn't seem to have a ton of  support now. And then the other one Ansgar and Casper I know on the last call you wanted to take like a minute or two to talk about the issuance proposals again even though they're mostly CL changes. And we didn't have time last week or two weeks ago but do you want to take a minute or two to go over them now?


**Ansgar** [1:11:02](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=4262s): Yeah sure thanks. So I think basically I just wanted to briefly mention because some people here might have come across kind of that conversation on Twitter or other kind of places. Basically we proposed a while ago we had some research on kind of the long-term direction for kind of the Ethereum Staking and system. We personally see some arguments that that's kind of idea for a while to go to like a targeting mechanism where basically the staking ratio would stay at within a prespecified range instead of being allowed to keep climbing upwards. We see some arguments for that of course that's kind of still in the research process will take some time to figure that out and see what direction we end up wanting to go in. Just because it is much harder to potentially reduce the staking set size after we already have drifted upwards to say 60/ 70/ 80% we felt like there might be some arguments to be made to already have some tempering of the issuance in the in pectra just to basically slow that process down. And give us more time to decide after proposing that it turns out that there's been quite a quite a bit of kind of community push back clearly you know any change like that would require really broad Community Support. So right now it's not in a place where it would be in includable in Electra. It's a really small change of course it's like it was designed it's basically two lines changing the spec. So the idea would be that we will keep pushing for what we know the case that we see for it and if we are successful in convincing people within the next few months. We could always add this very last moment. Again right now we're not on a path towards this but I just wanted to make sure it's mostly a CL side issue but of course it would require really Broad only Community Buy in but also All Core Devs buy in both from the EL and CL side. Just because it's not primarily a technical change but I'm a philosophical one. So I just want to briefly kind of give a quick kind of summary of where we are there that's all. 


**Tim Beiko** [1:13:12](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=4392s): Yeah. Thanks  for the update. I don't want to open the scan of worms on this call but I think yeah it's definitely something people should be mindful of and and pay attention to but yeah we should have the bulk of the conversation on if and how to change this on the CL call but yeah EL team should should definitely share their their point of view there. Okay so I think this covered all of the EIPs which at least had a couple of the client teams supporting them explicitly. All of the ones which had notable updates. Is there any EIP or proposal that people feel that I've missed? If not I think it's worth taking more time to dig into EOF 7623, 2937 and yeah figure out like next steps for the three of those. But yeah before we do that anything else people wanted to bring up. If not okay so I think EOF is the one with the highest uncertainty and also like most consequential whether we do it or not there's been a bit of chat about it. As we were speaking I think that like the question around. So I had a question around whether we could potentially do this as part of Verkle obviously.  I understand that there are two large changes in the same Fork but they seem relatively isolated although maybe that's not the case as per some of the comments. And then the other thread in the chat was around the testing complexity and you know whether we should do something like try to get it implemented and tested in say the next month or so. And then if we realize that we're you know we're nowhere near getting it finalized then we can remove it from the fork. But yeah I guess the client teams have changed or updated opinions on whether it would make sense to yeah whether it would make sense to like try now to like get it included in Devnets doing cross client testing. And that we feel confident we can actually get there if we prioritize it or does it make sense to potentially include it alongside Verkle even though they're two large changes and this gives us way more time. And yeah any thoughts there? Guillaume?

**Guillaume** [1:16:06](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=4566s): Yeah so forget about including it alongside. Verkle is a huge change. It's going to touch roughly. I mean this is the gist of my concern. It's going to touch a lot of the locations at the same time. These are two big complex areas that are going to have strange interplays. This is way too risky. I cannot. I cannot support that.

**Tim Beiko** [1:16:36](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=4596s ):  Georgios?

**Gakonst** [1:16:41](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=4601s ): I just wrote it in the chat but just in case I would feel like a EOF is an EVM change. It's not an integration change; it means that we can test it in isolation can fuzz it very heavily. And we can have very clear boundaries around it. I think on the testing point I think we double click on what the testing looks like and Define requirements for it. And the other thing is that in general EOF is good for performance, it's good for tools, it's good for a lot of things and I feel like people have some implementations of it already, Maybe not published. I don't know but like for us it was pretty simple to implement honestly one mon job. And I feel we should take a very clear-headed look at it.

 **Tim Beiko** [1:17:34](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=4654s ): Yeah Mario? 

**Mario Vega** [1:17:37](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=4657s ): Yeah so my only concern here is that right now. The current set of tests that are written are in the ethereum test repo. And this makes it a little bit more complicated than what we have been doing in the past couple of forks that is using execution spec tests which makes it more easy to review. And understand what is currently the coverage for EOF. So my only concern is that we need to make FORK of the tests of EOF to execution spec tests because otherwise we are not sure of the coverage we're not sure what's really tested or not. And this is going to take a while because currently testing team is with constraint bandwidth. So I would say that if we want to make this EOF happen we need to have this set of tests in the new repository. That's my only ask I would say. 

**Tim Beiko** [1:18:35](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=4715s): And oh yeah I guess Dannol? Do you want to answer to that?

**Danno** [1:18:40](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=4720s): So I mean I guess this is what I have to say is kind of a meta summary of what's going on all the concerns and objections are around scheduling and complexity and difficulty not about the merits of EOF and there's any talk about merits it's generally positive does this warrant moving EOF to CFI but not
necessarily scheduling it for Prague and we can extend the Prague discussion to see how testing and implementation is developed.

**Tim Beiko** [1:19:06](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=4746s): I guess the only concern I can see with that is say that we say okay EOF is CFI but then we also do like say 7623 and 2935. It's like like can we say EOF is like a medium sized set of changes like if we if we CFI it but then include like a couple small changes. Are we taking up all of the teams bandwidth basically. And yeah it does feel like there's a trade-off there right.


**Gakonst** [1:19:38](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=4778s): Sorry for jumping in. One thought for us all to be present is going faster and also upping our bar and being more precise about the size of each change. And the historical hashes change for example is quite small and I would hope that every team including ours can implement it in a small amount of time. And that we shouldn't really think of them of these features as big burdens almost EOF. Yes it is a lot of work. I also think that because of the isolation it is much easier to test. Same thing for the block historical block hash but would strongly encourage everyone to you know let's try to go the extra mile and stretch all ourselves together in this.

**Tim Beiko** [1:20:33](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=4833s): So I guess maybe a a thought of like how we can move this forward is we have the spec right now for Dev Net Zero which had all the current EIPs included We've added 3074 to the list so we should probably have that in the first devnet. I think we can make a call on whether or not we want like 2935 and or the call data repricing one. If and then what I would do is CFI EOF and then have the teams working on devnet-0 in parallel to the testing stuff being figured out like I suspect it is worth taking a couple weeks to look into you know what's the testing infrastructure we need. And whatnot and then then if we're confident with EOF. We can add it to like the devnet after that. But I think having your first Devnet which is like everything that's already included which is non-trivial plus you know a couple small tweaks that we we want to do in parallel figuring out the EOF testing situation and then making a call about whether we want you know whether we think that EOF can be included with like minimal overhead. That seems like the right path forward because I guess otherwise if we start working on EOF and realize the testing effort is going to take you much longer than expected. We've sort of wasted this these next couple weeks. So yeah does that generally make sense to people CFI and EOF having devnet zero not include it and then in parallel to this trying to figure out on the testing side like what exactly do we need and what's the amount of work required and ideally doing some or most of that work. Okay no objections. So yeah no objections so let's move forward with that. So CFI EOF I'll need to get an EIP number from you all at some point. Worst case I can just add the old ones there but it'd be nice to have yeah like an EIP that tracks the latest spec. And then yeah I think to everyone working on EOF like please ping Mario and ask him exactly what he needs from you in terms like testing support. I think he'll be happy to walk through like yeah exactly what we should be migrating and how we should be assessing coverage. And then given that 2935 is probably the most. Before we do 2935 there's another comment in the chat around stopping to serve history which is another like non-trivial change. So I guess like clients do you want to give an overview like what do you see as the effort to do that like what you know to what extent is this like a big ask for teams. Yeah.

**Lightclient** [1:24:00](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=5040s ): I think it's a relatively small ask. I think the maybe big change is that.clients might have to change their behavior for how they start sinking from scratch. So they won't go and request blocks before the the merge . So they'll sort of stop once they get to that merge Point during the backfill. There'll be some changes for the eth wire protocol I don't know if we'll need to I mean yeah we'll probably need to update the eth wire protocol and to say that requests for headers and bodies before a certain point will not be accepted or responded to. In general these are pretty small as from client teams. I think the biggest thing is like as we've talked about in the past is making sure that we want to making sure that this data is available and we have efforts on making that data available with error format and having people provide that data if clients want to continue supporting the pre merge data they wouldn't need a way to process the error files. None of this is particularly difficult. I think some of their clients have already implemented the error format and it's not a huge request, it's not a requirement but if they want to continue serving that data to their users they would need to come up with a way to ingest the data. 

**Tim Beiko** [1:25:23](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=5123s): Yeah Marek?


**Marek** [1:25:26](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=5126s): I very like this idea but there are a few probably more problems. First of all we need to check with CL clients how they are handling deposits. Because deposits are included in checkpoint sync but if CL client do not use them then they have to start doing it before we drop history. Then another thing is I think it might be even more problematic for clients like reth or Erigon when they thinkinking from Genesis. I might be wrong so please clarify if I'm wrong here. And generally Arch I sync might be a little bit problematic after that but we could import data from error files. I don't how do you see that Lightclient. 

**Gakonst** [1:26:28](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=5188s): Sorry Marek can you articulate the question or the risk for the Erigon architecture that reth.

**Marek** [1:26:37](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=5197s): So my question is if it is not problem for you if we drop all blocks pre merge all blocks and you will have to start syncing from after the merge.

**Gakonst** [1:26:53](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=5213s): Ah I see it is true that neither and somebody from Erigon should also weigh in on this. I t is true that the snap Sync functionality is not as is supported by the architecture. We had a conversation with that in the ACD Channel with Felix from Geth. And that is because the snapping protocol gossips sha instead of pre-images and it and an execution in Reth and Erigon are based on preimages of the keys. So there's no way to map back from the chat to the preimages. There is an interesting question to what extent with Verkle we can also and this might already be part of the Verkle spec my apologist. If there's an interesting question to what extent this kind of Sync is, it is kind of like we can do snap sync. Perhaps in Reth or Erigob with Verkle I don't know if that is possible. I think that's a question that we want to explore in the coming weeks or months. So that said it means that we cannot support snap sync which means that it hurts our ability to sync from scratch over P2P. And I would love to have a conversation about it. We don't feel too strongly about it. It's possible that you know we can maybe host premerge history somewhere and maybe that's fine for us. Yeah that that's roughly how I think about it so I don't have a very strong view but yeah and to the extent that you know we get a an archive format whether it is error or something else that might help I think on that on the archive format there are interesting questions around a what is the optimal file format whether having an optimal fire format matters or whether we should move forward with something that just works having clear requirements for the archive format which we have asked in the chat and we think the conversation still needs more work. And finally on the thein method of these networks where I feel like it's great to say that we have portal Network as an answer. Although there I think we need to get again more precise, more clear on timelines and really really be clear about the dependencies between these three the interplay of History expiry picking the right file format which might be a simple decision and a dissemination.


**Tim Beiko** [1:29:17](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=5357s ): Okay I want to just go back to the other EIPs because we only have two now one minute left. I don't think. So math has a draft EIP out. I think we should review that but I don't think we should make like a decision about including the draft EIP even in the fork even though there seems to be a rough consensus towards clients. Generally I want to move towards that and it's more a question of when and how rather than if before we wrap up I guess 2935 feels like something where there's pretty much broad consensus no objection as far as I can tell. And it's fairly simple, does anyone oppose including that in the fork and also having it part of devnet zero so that we can get it prototyped as soon as possible. If there's no objection. I think we should move forward with that so including 2935 the so Marek this is the block hash in the Stake. So like the same thing as 4788 basically but with a different value and then the last one so 7623 there's a lot of discussion about that about blob size increase and and whatnot I feel like we should potentially CFI 7623 but not included yet there's probably some more discussion to to be had there so does that generally make sense to people. Okay if there's no objection we can do that. So to recap we aside from all the stuff that was already included in the fork. We added 374/ 2935 both of which will be part of the devnet zero spec EOF and 7623 We've CFIed. So we'll continue sort of looking into those in the next couple weeks. And then if we feel highly confident in them we can bring them in later. And I think the other thing I want to flag is Potuz EIP to deal with some of the issues with 3074. That's also something we should keep looking at. If we're already over time it feels a bit late to maybe CFI it. But yeah I think at this point though in you know there's probably small things we can bring in the fork as we like find analyze things but generally if EOF comes in that would be like the last big change. And everything else that's there should be yeah kind of the bulk of the Pecra Fork at least on the EL side. Yeah, any final comments thoughts? Okay well yeah thanks a lot everyone yeah I will talk to you all soon and make sure to get all the specs updated. 

**Gakonst** [1:32:31](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=5551s): And yeah Tim could I kindly ask you to in the All Core Devs Channel could we get a written articulation of what got confirmed what is CFI and what are next steps for us to further discuss with precision and clear data driven articulations of where we need to do more work.

**Tim Beiko** [1:32:49](https://www.youtube.com/watch?v=FWvi_z1_gB0&t=5569s): Yes I'll post a recap in a few minutes. Cool of course. Thanks everyone.

# Attendees
* Terence
* Tim Beiko
* Cyrus
* Mrabino1
* Zoom User
* Maurius Van Der Wijden
* Marcello Ardizzone
* Ignacio
* Potuz
* Pooja Ranjan
* Arik Galansky
* Nishant
* Thedevbrib
* Justin Traglia
* Echo
* Antonio Sanso
* Roman Dvorkin
* Danno Ferrin
* Enrico Del Fante
* Ansgar Dietrichs
* Carl Beekhuizen
* Lightclient
* Ben Adams
* Roberto B
* Stefan Bratanov
* Toni Wahrstaetter
* Ruben
* Caspar
* Ahmad Bitar
* Terence
* Sean
* Somnath Erigon
* Ameziane Hamlat 
* Paritosh
* Danceratopz
* Saulius Grigatis
* Andrei
* Piotr
* Yoav
* Guillaume
* Hsiao -Wei Wang
* Phil NGO
* Mikhail Kalinin
* Alex Stokes
* Fabio Di Fabio
* Alex Forshtat
* Matt Nelson
* Mario Vega
* Vasilliy Shapovalov
* Mike Neuder
* Gakonst (Georgios Konstantopoulos)
* Daniel Lehmer
* Vitalik

## Next meeting: Thursday, Apr 25, 2024, 14:00-15:30 UTC 
